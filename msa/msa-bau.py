# -*- coding: utf-8 -*-
"""msa-bau.py – Gerüst für die Erfassung eines Hefts im Profil msa und Selbstprüfung des Bestands.
Version 0.3 · 23.09.2026 · gilt mit katalog-prompt.md v0.9 und msa.md v0.7

Änderungen gegenüber 0.2 (Auftrag Gymnasialhefte, 23.09.2026): papier-Muster um
GYM erweitert (msa.md § 4); KONFIG führt daneben „dateien" (Liste, weil ab 2019
zwei PDF je Heft), der Altwert „datei" bleibt gültig – beide Felder sind rein
informativ und werden vom Skript nicht ausgewertet. Zeilen mit papier GYM
werden unabhängig von block nach msa-katalog-gym.csv geschrieben (beide
Blöcke in einer Datei, Feld block trennt sie wie gehabt); OS/EBR/FOR/MUSTER
unverändert nach msa-katalog-basis.csv/msa-katalog-kontext.csv. Die
Selbstprüfung liest jetzt alle drei Katalogdateien. KONFIG["seiten"] darf für
zweiteilige Hefte ein dict {block: seiten} sein (Seite zählt je PDF-Datei neu,
die beiden Gymnasialteile haben getrennte Fußzeilen "Seite N von M"); ein
einzelner int bleibt wie bisher gültig. Selbstprüfung für OS/EBR/FOR/MUSTER
byteidentisch zu 0.2 (393 Zeilen, 185 Typen, gleiche Hashes, vor dem ersten
GYM-Heft geprüft).

Änderungen gegenüber 0.1 (Auftrag F, Punkt 1, 17.09.2026): Die Dateien des
Profils tragen das Präfix msa- (KAT, TYP: msa-katalog-basis.csv,
msa-katalog-kontext.csv, msa-typen.csv; namensschema.md § 4, Variante B).
Nur die Namen, keine Prüfung geändert; Selbstprüfung byteidentisch zu 0.1.

Angelegt in Auftrag E (Punkt 6, 17.09.2026). Der msa-Bestand (2014–2026, 393
Zeilen in zwei Katalogdateien, 185 Typen) wurde ohne Skript im Chat erfasst
(Kern v0.3, konzept.md § 7); dieses Gerüst folgt fhr-bau.py v0.2 und prüft
nach Kern § 7, damit msa denselben Weg hat wie die anderen Profile: Skript
prüft, Skript schreibt, keine Handedits in den CSV-Dateien.

Je Heft werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Zwei
Katalogdateien (msa.md § 4, Entscheidung 14): block „Basis" → msa-katalog-basis.csv,
block „Kontext" → msa-katalog-kontext.csv. Leitideen und Themenliste liest das
Skript aus msa.md § 5 und § 6.

Ist ZEILEN leer, läuft die Selbstprüfung über den Bestand (beide Kataloge
gegen Kern § 5 und msa.md, jede Typenverwendung, jede beispiel_id, kein Typ
unbenutzt) und schreibt nichts – außer eine Feldkorrektur in TYPEN_KORREKTUR
steht noch aus.

TYPEN_KORREKTUR: Feldkorrektur an msa-typen.csv (leitidee, thema, definition eines
vorhandenen Typs). Das Profil msa hat kein Abgleichskript; die Korrektur läuft
deshalb hier, wird einmal angewendet (Liste alt → neu im Bericht) und ist
danach wirkungslos, weil der Zielzustand schon steht – ein erneuter Lauf
schreibt nichts. Angewendet 17.09.2026 (Auftrag E, Punkt 6; Vorschlag 4 aus
befund-typenlisten.md § 3): „Behauptung prüfen" bekommt Leitidee und Thema
seiner ersten Fundstelle 2025-OS-K3b, weil der Kern § 6 jedem Typ leitidee und
thema gibt; der Typ bleibt Nebentyp über alle Leitideen (Definition).

Ablauf:
  1. katalog-prompt.md, msa.md, msa-typen.csv, msa-katalog-basis.csv, msa-katalog-kontext.csv
     neben dieses Skript legen (aus dem Repo).
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen – oder leer lassen für die Selbstprüfung.
  3. python msa-bau.py – schreibt die CSV-Dateien, gibt Prüftabelle und Bericht
     aus. Bei einem Fehler wird nichts geschrieben.
"""
import csv, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")

# ===================================================================== KONFIG
KONFIG = {
    "jahr": "2022",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "",         # zweiteiliges Heft ab 2019, siehe "dateien"
    "dateien": ["22_P10_Ma_Gym_Aufgaben_1_und_2.pdf", "22_P10_Ma_Gym_Aufgaben_3_bis_6.pdf"],
    "seiten": {"Basis": 3, "Kontext": 9},  # eigene Fußzeile je Teildatei (msa.md § 3)
    "soll": {"1": 5, "2": 5, "3": 11, "4": 12, "5": 9, "6": 8},
    "soll_gesamt": 50,
}

# ---- technischer Block, nicht ändern ----
HEAD = ("id;jahr;papier;block;aufgabe;titel;teilaufgabe;seite;punkte;stern;hilfsmittel;afb_amtlich;"
        "leitidee;thema;typ;typ_neben;stichwoerter;voraussetzungen;format;operator;antwort;material;"
        "skizze;kontext;textumfang;gegeben;gesucht;verfahren;schritte;zahlenraum;einheiten;"
        "abhaengig_von;ergebnis;zwischenergebnis;niveau_geschaetzt;fehlerquelle;bemerkung").split(";")

ZEILEN = []

def row(**kw):
    z = {k: "" for k in HEAD}
    z.update(jahr=KONFIG["jahr"], papier=KONFIG["papier"], stern="", hilfsmittel="ja", afb_amtlich="")
    unbekannt = set(kw) - set(HEAD)
    if unbekannt:
        sys.exit(f"unbekanntes Feld: {sorted(unbekannt)}")
    z.update(kw)
    ZEILEN.append(z)

# ============================================================ ZEILEN JE HEFT

# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Kantensumme eines Quaders mit Seitenlängen in Abhängigkeit von der Höhe berechnen",
     "Größen und Messen", "Volumen und Oberfläche",
     "Gesamtlänge aller Kanten eines Quaders berechnen, dessen beide Grundkanten als Differenz bzw. "
     "Summe eines gegebenen Wertes mit der Höhe beschrieben sind.",
     "2022-GYM-B1a"),
    ("Term mit Klammern und Potenzen vereinfachen", "Zahlen und Operationen", "Terme umformen",
     "Einen Term mit mehreren Klammern, darunter eine binomische Formel, ausmultiplizieren und so weit "
     "wie möglich zusammenfassen.",
     "2022-GYM-B2b"),
    ("Parabeltransformation gegenüber der Normalparabel beschreiben", "Gleichungen und Funktionen",
     "Quadratische Funktionen",
     "Anhand des Graphen beschreiben, durch welche Verschiebung (und ggf. Streckung) eine Parabel aus der "
     "Normalparabel y = x² entstanden ist.",
     "2022-GYM-K3a"),
    ("Parabelgleichung aus zwei Nullstellen aufstellen und Nullstellen bestätigen", "Gleichungen und "
     "Funktionen", "Quadratische Funktionen",
     "Gleichung einer Parabel in Produktform p(x) = a·(x−x1)·(x−x2) aus dem Graphen und zwei vermuteten "
     "Nullstellen aufstellen und die Nullstellen durch Einsetzen bestätigen.",
     "2022-GYM-K3b"),
    ("Durchmesser einer Halbkugel aus der Oberfläche berechnen", "Größen und Messen",
     "Volumen und Oberfläche",
     "Durchmesser oder Radius einer Halbkugel durch Umstellen der Oberflächenformel O = 2·π·r² aus der "
     "gegebenen Oberfläche berechnen.",
     "2022-GYM-K4a"),
    ("Kegelhöhe aus Mantellinie und Radius berechnen", "Größen und Messen", "Satz des Pythagoras",
     "Höhe eines Kegels aus der Mantellinie und dem Radius über den Satz des Pythagoras berechnen "
     "(Umkehrung zu „Mantellinie Kegel bestimmen“).",
     "2022-GYM-K4b"),
    ("Farbmenge aus Fläche und Ergiebigkeit berechnen", "Größen und Messen", "Einheiten umrechnen",
     "Benötigte Menge eines Anstrichmittels aus einer zu streichenden Fläche und der Ergiebigkeit einer "
     "gegebenen Menge je Fläche berechnen, für mehrere gleiche Stücke, und daraus die Anzahl benötigter "
     "Gebinde (aufgerundet) bestimmen.",
     "2022-GYM-K4c"),
    ("Volumen eines aus Kegel und Halbkugel zusammengesetzten Körpers mit Nebenbedingung berechnen",
     "Größen und Messen", "Volumen und Oberfläche",
     "Volumen eines aus Kegel und Halbkugel gleicher Grundfläche zusammengesetzten Körpers berechnen, "
     "dessen Maße durch eine zusätzliche Bedingung (Durchmesser gleich Gesamthöhe) aneinander gekoppelt "
     "sind, durch Aufstellen und Lösen einer Gleichung in einer Variablen.",
     "2022-GYM-K4d"),
    ("Streckenlänge über ein konstruiertes Parallelogramm im Vieleck begründen", "Raum und Form",
     "Kongruenz und Konstruktion",
     "Länge einer Strecke in einem Vieleck begründen, indem sie als Gegenseite in einem aus einer "
     "gegebenen Parallelität und einem Streckenmittelpunkt gebildeten Parallelogramm erkannt und daher "
     "gleich der bekannten gegenüberliegenden Seite gesetzt wird.",
     "2022-GYM-K5b"),
    ("Prozentuale Abweichung einer Modellfläche von der tatsächlichen Fläche berechnen",
     "Zahlen und Operationen", "Prozentrechnung",
     "Fläche eines aus Teilflächen zusammengesetzten Modells mit der tatsächlichen Fläche vergleichen und "
     "die Abweichung in Prozent der tatsächlichen Fläche angeben.",
     "2022-GYM-K5c"),
]

row(id="2022-GYM-B1a", block="Basis", aufgabe="1", titel="", teilaufgabe="a", seite="2",
    punkte="3", hilfsmittel="nein", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Kantensumme eines Quaders mit Seitenlängen in Abhängigkeit von der Höhe berechnen",
    stichwoerter="Quader|Kantensumme|Höhe", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Quader mit Höhe h; eine Grundkante ist 2 m kürzer, die andere 1 m länger als h; hier h = 5 m",
    gesucht="Gesamtlänge aller Kanten des Quaders",
    verfahren="Grundkanten: 5−2=3 m und 5+1=6 m; Kantensumme = 4·(3+6+5)", schritte="2",
    zahlenraum="ganz", einheiten="m", ergebnis="56 m", niveau_geschaetzt="II",
    fehlerquelle="nur eine der drei verschiedenen Kantenlängen statt aller drei vierfach zählen")

row(id="2022-GYM-B1b", block="Basis", aufgabe="1", titel="", teilaufgabe="b", seite="2",
    punkte="2", hilfsmittel="nein", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Term zu Körper angeben",
    stichwoerter="Quader|Volumen|Term in Abhängigkeit von h", format="Kurzantwort", operator="Geben Sie an",
    antwort="Term", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    abhaengig_von="2022-GYM-B1a",
    gegeben="Quader mit Höhe h, Grundkanten (h−2) und (h+1)",
    gesucht="Gleichung zur Berechnung des Volumens in Abhängigkeit von h",
    verfahren="Volumen = Länge mal Breite mal Höhe", schritte="1",
    ergebnis="V(h) = (h − 2) · (h + 1) · h", niveau_geschaetzt="II",
    fehlerquelle="die Reihenfolge der Faktoren mit einer der beiden Kantenbeschreibungen vertauschen "
                 "(z. B. h+2 statt h−2)")

row(id="2022-GYM-B2a", block="Basis", aufgabe="2", titel="", teilaufgabe="a", seite="3",
    punkte="2", hilfsmittel="nein", leitidee="Zahlen und Operationen", thema="Rationale Zahlen rechnen",
    typ="Termwert berechnen",
    stichwoerter="Termwert|Klammer|negative Zahlen", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Term (a − 3)² − 2·(a + 4,5) − a mit a = −2",
    gesucht="Termwert",
    verfahren="a = −2 einsetzen: (−5)² − 2·2,5 − (−2)", schritte="1", zahlenraum="negativ",
    ergebnis="22", niveau_geschaetzt="II",
    fehlerquelle="das Vorzeichen von a beim Einsetzen in (a−3)² oder bei −a vertauschen")

row(id="2022-GYM-B2b", block="Basis", aufgabe="2", titel="", teilaufgabe="b", seite="3",
    punkte="3", hilfsmittel="nein", leitidee="Zahlen und Operationen", thema="Terme umformen",
    typ="Term mit Klammern und Potenzen vereinfachen",
    stichwoerter="binomische Formel|Klammern auflösen|zusammenfassen", format="Rechnung",
    operator="Lösen Sie die Klammern auf und fassen Sie zusammen", antwort="Term", material="keins",
    skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Term (a − 3)² − 2·(a + 4,5) − a",
    gesucht="vereinfachter Term",
    verfahren="binomische Formel: (a−3)² = a² − 6a + 9; Klammer auflösen: −2·(a+4,5) = −2a − 9; "
              "zusammenfassen: a² − 6a + 9 − 2a − 9 − a", schritte="2",
    ergebnis="a² − 9a", niveau_geschaetzt="III",
    fehlerquelle="beim Anwenden der binomischen Formel das mittlere Glied −6a vergessen")

row(id="2022-GYM-K3a", block="Kontext", aufgabe="3", titel="Quadratische Funktionen", teilaufgabe="a",
    seite="2", punkte="2", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parabeltransformation gegenüber der Normalparabel beschreiben",
    stichwoerter="Normalparabel|Verschiebung|Scheitelpunkt", format="Begründung", operator="Beschreiben Sie",
    antwort="Text", material="Koordinatensystem",
    skizze="Parabel p mit Scheitelpunkt bei etwa (2,5|−1), Nullstellen bei 1,5 und 3,5, gleich weit "
           "geöffnet wie die Normalparabel", kontext="ohne", textumfang="kurz",
    gegeben="Graph der Parabel p mit Scheitelpunkt bei (2,5|−1)",
    gesucht="Beschreibung der Entstehung von p aus der Normalparabel",
    verfahren="Vergleich der Öffnung (gleich weit wie die Normalparabel) und der Lage des Scheitelpunkts",
    schritte="1",
    ergebnis="p entsteht aus der Normalparabel durch Verschiebung um 2,5 nach rechts und 1 nach unten",
    niveau_geschaetzt="II",
    fehlerquelle="zusätzlich eine Streckung oder Stauchung behaupten, obwohl die Parabel gleich weit "
                 "geöffnet ist wie die Normalparabel")

row(id="2022-GYM-K3b", block="Kontext", aufgabe="3", titel="Quadratische Funktionen", teilaufgabe="b",
    seite="2", punkte="4", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parabelgleichung aus zwei Nullstellen aufstellen und Nullstellen bestätigen",
    stichwoerter="Produktform|Nullstellen|Nachweis", format="Rechnung|Rechnung",
    operator="Geben Sie an|Zeigen Sie", antwort="Term|Text", material="Koordinatensystem",
    skizze="wie 2022-GYM-K3a", kontext="ohne", textumfang="kurz", abhaengig_von="2022-GYM-K3a",
    gegeben="Graph der Parabel p mit Nullstellen bei x = 1,5 und x = 3,5, Öffnungsfaktor 1 (wie "
            "Normalparabel)",
    gesucht="Gleichung von p; Nachweis, dass 1,5 und 3,5 Nullstellen von p sind",
    verfahren="Produktform p(x) = 1·(x−1,5)·(x−3,5) ausmultiplizieren; Nachweis durch Einsetzen von "
              "x=1,5 und x=3,5 in p(x) = 0 oder in die Produktform", schritte="2", zahlenraum="dezimal",
    ergebnis="p(x) = x² − 5x + 5,25; p(1,5) = 0 und p(3,5) = 0 bestätigt", niveau_geschaetzt="II",
    fehlerquelle="den Öffnungsfaktor nicht aus dem Vergleich mit der Normalparabel übernehmen, sondern "
                 "willkürlich setzen")

row(id="2022-GYM-K3c", block="Kontext", aufgabe="3", titel="Quadratische Funktionen", teilaufgabe="c",
    seite="3", punkte="5", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parabelgleichung aus Scheitel und Punkt bestimmen",
    stichwoerter="Scheitelpunkt auf y-Achse|Schnittpunkt|Parameter a und c", format="Rechnung|Zeichnen",
    operator="Ermitteln Sie|Zeichnen Sie", antwort="Zahl|Grafik", material="Koordinatensystem",
    skizze="Koordinatensystem −2 bis 2 für die Parabel h", kontext="ohne", textumfang="kurz",
    abhaengig_von="2022-GYM-K3b",
    gegeben="Parabel h(x) = a·x² + c mit Scheitelpunkt Sy(0|−4,5) und Schnittpunkt mit p bei Sx(1,5|0)",
    gesucht="Werte für a und c; Graph von h mindestens im Intervall −2 ≤ x ≤ 2",
    verfahren="Scheitelpunkt auf der y-Achse liefert c = −4,5 direkt; Einsetzen von Sx: a·1,5² − 4,5 = 0 "
              "nach a auflösen", schritte="2", zahlenraum="dezimal",
    ergebnis="a = 2, c = −4,5, also h(x) = 2x² − 4,5", niveau_geschaetzt="III",
    fehlerquelle="c mit dem y-Wert von Sx statt mit dem Scheitelpunkt Sy bestimmen")

row(id="2022-GYM-K4a", block="Kontext", aufgabe="4", titel="Boje", teilaufgabe="a", seite="4",
    punkte="2", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Durchmesser einer Halbkugel aus der Oberfläche berechnen",
    stichwoerter="Halbkugel|Oberfläche|Durchmesser", format="Rechnung", operator="Zeigen Sie rechnerisch",
    antwort="Text", material="Figur",
    skizze="Querschnitt einer Boje: Halbkugel oben mit Durchmesser d, darunter ein Kegel mit "
           "Mantellinie s=1,9 m, Gesamthöhe h; nicht maßstabsgerecht", kontext="Technik", textumfang="kurz",
    gegeben="Oberfläche des halbkugelförmigen Teils der Boje 2,26 m²",
    gesucht="Nachweis, dass der Durchmesser der Boje etwa 1,2 m beträgt",
    verfahren="O = 2·π·r² nach r umstellen: r = √(O:(2π))", schritte="1", zahlenraum="dezimal",
    einheiten="m", ergebnis="r ≈ 0,60 m, d ≈ 1,2 m", niveau_geschaetzt="II",
    fehlerquelle="die Oberflächenformel einer ganzen Kugel (4πr²) statt der Halbkugel (2πr²) verwenden")

row(id="2022-GYM-K4b", block="Kontext", aufgabe="4", titel="Boje", teilaufgabe="b", seite="4",
    punkte="3", leitidee="Größen und Messen", thema="Satz des Pythagoras",
    typ="Kegelhöhe aus Mantellinie und Radius berechnen",
    stichwoerter="Kegelhöhe|Mantellinie|Gesamthöhe", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur", skizze="wie 2022-GYM-K4a", kontext="Technik", textumfang="kurz",
    abhaengig_von="2022-GYM-K4a",
    gegeben="Radius r ≈ 0,6 m (aus Teilaufgabe a); Mantellinie des Kegels s = 1,9 m",
    gesucht="Gesamthöhe der Boje",
    verfahren="Kegelhöhe über Pythagoras: h_Kegel = √(s² − r²); Gesamthöhe = Halbkugelradius + Kegelhöhe",
    schritte="2", zahlenraum="dezimal", einheiten="m",
    ergebnis="h_Kegel ≈ 1,80 m; Gesamthöhe ≈ 0,60 m + 1,80 m ≈ 2,40 m", niveau_geschaetzt="III",
    fehlerquelle="die Mantellinie s selbst als Kegelhöhe verwenden, ohne den Satz des Pythagoras "
                 "anzuwenden")

row(id="2022-GYM-K4c", block="Kontext", aufgabe="4", titel="Boje", teilaufgabe="c", seite="5",
    punkte="4", leitidee="Größen und Messen", thema="Einheiten umrechnen",
    typ="Farbmenge aus Fläche und Ergiebigkeit berechnen", typ_neben="Mantelfläche Kegel berechnen",
    stichwoerter="Rostschutzfarbe|Ergiebigkeit|Kanister", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="Technik", textumfang="mittel",
    abhaengig_von="2022-GYM-K4b",
    gegeben="250 ml Farbe reichen für 1,3 m²; Mantelfläche des Kegels aus r ≈ 0,6 m und s = 1,9 m; "
            "50 Bojen; Kanister zu je 5 Liter",
    gesucht="Anzahl benötigter Kanister für 50 Bojen",
    verfahren="Mantelfläche M = π·r·s ≈ 3,58 m²; Farbmenge je Boje = M : 1,3 · 250 ml ≈ 688,7 ml; für 50 "
              "Bojen ≈ 34,4 L; Kanisterzahl = 34,4 : 5, aufgerundet", schritte="4", zahlenraum="dezimal",
    einheiten="m²|ml|L", ergebnis="≈ 34,44 L insgesamt, davon 7 Kanister zu 5 Litern (aufgerundet)",
    niveau_geschaetzt="III",
    fehlerquelle="die berechnete Literzahl runden statt aufzurunden, obwohl ein angebrochener Kanister "
                 "trotzdem vollständig gebraucht wird")

row(id="2022-GYM-K4d", block="Kontext", aufgabe="4", titel="Boje", teilaufgabe="d", seite="5",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Volumen eines aus Kegel und Halbkugel zusammengesetzten Körpers mit Nebenbedingung berechnen",
    typ_neben="Volumen Kugel berechnen",
    stichwoerter="Museumsboje|Nebenbedingung|Gesamthöhe gleich Durchmesser", format="Rechnung",
    operator="Berechnen Sie", antwort="Zahl", material="keins", skizze="keine", kontext="Technik",
    textumfang="mittel",
    gegeben="alte Boje aus Halbkugel und Kegel gleicher Grundfläche; Durchmesser der Grundfläche = "
            "Gesamthöhe der Boje; Volumen 10,6 m³",
    gesucht="Gesamthöhe der alten Boje",
    verfahren="Radius r, Gesamthöhe 2r, also Kegelhöhe = 2r − r = r; V = 2/3·π·r³ + 1/3·π·r²·r = π·r³; "
              "π·r³ = 10,6 nach r auflösen; Gesamthöhe = 2r", schritte="3", zahlenraum="dezimal",
    einheiten="m", ergebnis="r = 1,5 m, Gesamthöhe = 3 m", niveau_geschaetzt="III",
    fehlerquelle="die Kegelhöhe gleich der Gesamthöhe 2r statt gleich r (Gesamthöhe minus Halbkugelradius) "
                 "setzen")

row(id="2022-GYM-K5a", block="Kontext", aufgabe="5", titel="Algerien", teilaufgabe="a", seite="6",
    punkte="2", leitidee="Größen und Messen", thema="Satz des Pythagoras",
    typ="Pythagoras Hypotenuse",
    stichwoerter="Sechseck|Landesmodell|Diagonale", format="Rechnung", operator="Zeigen Sie",
    antwort="Text", material="Figur",
    skizze="unregelmäßiges Sechseck ABCDEF als Näherung für Algerien, mit rechtem Winkel β bei B; "
           "Diagonale AC verbindet den südlichsten Punkt A mit dem nördlichsten Punkt C",
    kontext="Sonstiges", textumfang="kurz",
    gegeben="Dreieck ABC mit AB = 695 km, BC = 1980 km, rechter Winkel β = 90° bei B",
    gesucht="Nachweis, dass die Entfernung AC etwa 2100 km beträgt",
    verfahren="Satz des Pythagoras: AC = √(695² + 1980²)", schritte="1", zahlenraum="ganz",
    einheiten="km", ergebnis="AC ≈ 2098,4 km ≈ 2100 km", niveau_geschaetzt="II",
    fehlerquelle="AB und BC addieren statt den Satz des Pythagoras anzuwenden")

row(id="2022-GYM-K5b", block="Kontext", aufgabe="5", titel="Algerien", teilaufgabe="b", seite="7",
    punkte="3", leitidee="Raum und Form", thema="Kongruenz und Konstruktion",
    typ="Streckenlänge über ein konstruiertes Parallelogramm im Vieleck begründen",
    stichwoerter="Mittelpunkt|Parallelogramm|Landesgrenze", format="Begründung", operator="Begründen Sie",
    antwort="Text", material="Figur", skizze="Sechseck mit Punkt G als Mittelpunkt von AC, EG ∥ FA",
    kontext="Sonstiges", textumfang="kurz", abhaengig_von="2022-GYM-K5a",
    gegeben="G ist Mittelpunkt der Strecke AC (AC ≈ 2100 km aus Teilaufgabe a); EG ∥ FA",
    gesucht="Begründung, dass die Strecke EF etwa 1050 km lang ist",
    verfahren="AG = AC : 2 ≈ 1050 km; da FA ∥ EG das Viereck AFEG zu einem Parallelogramm ergänzt, ist "
              "die Gegenseite EF gleich lang wie AG", schritte="1", zahlenraum="dezimal", einheiten="km",
    ergebnis="EF = AG ≈ 1050 km", niveau_geschaetzt="III",
    fehlerquelle="EF mit der halben Strecke BC oder mit AB gleichsetzen statt mit AG")

row(id="2022-GYM-K5c", block="Kontext", aufgabe="5", titel="Algerien", teilaufgabe="c", seite="7",
    punkte="4", leitidee="Zahlen und Operationen", thema="Prozentrechnung",
    typ="Prozentuale Abweichung einer Modellfläche von der tatsächlichen Fläche berechnen",
    typ_neben="Flächeninhalt Dreieck berechnen",
    stichwoerter="Modellfläche|Abweichung in Prozent|Sechseck", format="Rechnung", operator="Zeigen Sie",
    antwort="Text", material="keins", skizze="keine", kontext="Sonstiges", textumfang="mittel",
    abhaengig_von="2022-GYM-K5a",
    gegeben="Fläche des Fünfecks ACDEF = 1 739 232 km²; Dreieck ABC mit AB = 695 km, BC = 1980 km, "
            "rechter Winkel bei B; tatsächliche Fläche Algeriens 2 382 000 km²",
    gesucht="Nachweis, dass die Sechseckfläche ABCDEF um weniger als 5 % von der tatsächlichen Fläche "
            "abweicht",
    verfahren="Fläche Dreieck ABC = 0,5 · 695 · 1980 ≈ 688 050 km²; Sechseckfläche = 1 739 232 + 688 050 "
              "≈ 2 427 282 km²; Abweichung = (2 427 282 − 2 382 000) : 2 382 000", schritte="3",
    zahlenraum="ganz", einheiten="km²",
    ergebnis="Sechseckfläche ≈ 2 427 282 km², Abweichung ≈ 1,9 % < 5 %, Behauptung bestätigt",
    niveau_geschaetzt="III",
    fehlerquelle="die Abweichung auf die berechnete Modellfläche statt auf die tatsächliche Fläche "
                 "beziehen")

row(id="2022-GYM-K6a", block="Kontext", aufgabe="6", titel="Pinguine", teilaufgabe="a", seite="8",
    punkte="3", leitidee="Daten und Zufall", thema="Daten darstellen",
    typ="Kreisdiagramm zeichnen",
    stichwoerter="Futterzusammensetzung|Kreisdiagramm|Restmenge", format="Zeichnen", operator="Stellen Sie dar",
    antwort="Grafik", material="keins", skizze="keine", kontext="Freizeit/Sonstiges", textumfang="mittel",
    gegeben="6 kg Futter täglich: 3,4 kg Fische, 600 g Krebstiere, Rest kleine Meereslebewesen",
    gesucht="Kreisdiagramm der Futterzusammensetzung",
    verfahren="Restmenge = 6 kg − 3,4 kg − 0,6 kg = 2 kg; Mittelpunktswinkel je Anteil: Fische "
              "3,4:6·360° ≈ 204°, Krebstiere 0,6:6·360° = 36°, Meereslebewesen 2:6·360° = 120°",
    schritte="2", zahlenraum="dezimal", einheiten="kg|Grad",
    ergebnis="Meereslebewesen 2 kg; Sektoren 204°/36°/120° für Fische/Krebstiere/Meereslebewesen",
    niveau_geschaetzt="II",
    fehlerquelle="die Restmenge (kleine Meereslebewesen) vor der Winkelberechnung vergessen zu bestimmen")

row(id="2022-GYM-K6b", block="Kontext", aufgabe="6", titel="Pinguine", teilaufgabe="b", seite="8",
    punkte="3", leitidee="Daten und Zufall", thema="Kenngrößen",
    typ="Spannweite berechnen", typ_neben="Median bestimmen",
    stichwoerter="Körpergröße|Spannweite|Median", format="Kurzantwort|Kurzantwort",
    operator="Geben Sie an|Ermitteln Sie", antwort="Zahl|Zahl", material="Tabelle",
    skizze="keine", kontext="Freizeit/Sonstiges", textumfang="kurz",
    gegeben="Körpergrößen von 10 Pinguinen: 129, 95, 98, 105, 99, 105, 105, 89, 101, 98 (in cm)",
    gesucht="Spannweite und Median der Körpergrößen",
    verfahren="sortieren: 89, 95, 98, 98, 99, 101, 105, 105, 105, 129; Spannweite = 129 − 89; Median = "
              "Mittel der 5. und 6. Zahl (99 und 101)", schritte="2", zahlenraum="ganz",
    einheiten="cm", ergebnis="Spannweite 40 cm; Median 100 cm", niveau_geschaetzt="II",
    fehlerquelle="beim Median die unsortierte Liste verwenden oder bei gerader Anzahl nur einen der "
                 "beiden mittleren Werte nehmen")

row(id="2022-GYM-K6c", block="Kontext", aufgabe="6", titel="Pinguine", teilaufgabe="c", seite="9",
    punkte="2", leitidee="Daten und Zufall", thema="Diagramme lesen und beurteilen",
    typ="Aussage zu Diagramm prüfen",
    stichwoerter="Säulendiagramm|gestauchte Achse|Prozentangabe", format="Begründung",
    operator="Entscheiden Sie|Begründen Sie", antwort="Text", material="Diagramm",
    skizze="Säulendiagramm mit y-Achse von 40000 bis 130000 (nicht bei 0 beginnend), Säule 1981 = "
           "120000, Säule 2021 = 60000", kontext="Freizeit/Sonstiges", textumfang="mittel",
    gegeben="Säulendiagramm: 1981 = 120 000 Pinguinpaare, 2021 = 60 000 Pinguinpaare; Behauptung: Abnahme "
            "um 75 %",
    gesucht="Wahrheitsgehalt der Behauptung",
    verfahren="tatsächliche Abnahme = (120000 − 60000) : 120000 = 50 %; die y-Achse beginnt nicht bei 0 "
              "(bei 40000), wodurch die Säulen in der Abbildung optisch einen viel stärkeren Rückgang "
              "zeigen als tatsächlich vorliegt", schritte="1", zahlenraum="Prozent",
    ergebnis="Behauptung ist falsch, die tatsächliche Abnahme beträgt 50 %, nicht 75 %",
    niveau_geschaetzt="III",
    fehlerquelle="die Säulenhöhen im Diagramm direkt ablesen und ins Verhältnis setzen, ohne die "
                 "gestauchte (nicht bei 0 beginnende) y-Achse zu berücksichtigen")
# Feldkorrektur an vorhandenen Typen: typ -> {feld: neuer Wert}; siehe Kopf.
TYPEN_KORREKTUR = {
    "Behauptung prüfen": {
        "leitidee": "Daten und Zufall",
        "thema": "Wahrscheinlichkeit mehrstufig",
        "definition": ("Eine vorgegebene Aussage rechnerisch oder argumentativ als wahr oder falsch "
                       "nachweisen; leitideenübergreifend, tritt nur als typ_neben auf. Leitidee und "
                       "Thema nach der ersten Fundstelle 2025-OS-K3b (zugeordnet 17.09.2026, Kern § 6: "
                       "jeder Typ trägt leitidee und thema); die Zeilen behalten ihr eigenes Thema."),
    },
}
# ======================================================== AB HIER UNVERÄNDERT
KAT = {"Basis": "msa-katalog-basis.csv", "Kontext": "msa-katalog-kontext.csv"}
GYM_DATEI = "msa-katalog-gym.csv"  # papier GYM: beide Blöcke in einer Datei, Feld block trennt sie
TYP = "msa-typen.csv"
PROFIL = "msa.md"
KERN = "../katalog-prompt.md"  # Umbau 2026-09-19: liegt in der Repo-Wurzel
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]
STATUS = {"gültig", "neu"}
PAPIER = re.compile(r"\d{4}-(OS|EBR|FOR|MUSTER-EBR|MUSTER-FOR|GYM)-[BK]\d+[a-z]?")
# Stämme, die eine ASCII-Umschrift von ä, ö, ü oder ß verraten (wie fhr-bau.py).
UMSCHRIFT = ("flaeche", "laenge", "naechst", "haeufig", "zufaell", "waehl", "aender", "aeusser",
 "gefaess", "verhaeltnis", "erklaer", "zaehl", "traeg", "gaeng", "maessig", "hoehe", "groesse",
 "groess", "loesung", "loes", "moegl", "koerper", "oeffn", "schoen", "pruef", "stueck", "gewuerz",
 "kruemmung", "ueber", "fuer", "muess", "fuehr", "gueltig", "zurueck", "huelle", "schluessel",
 "urspruengl", "gross", "massstab", "masszahl", "schliess", "heisst", "weiss", "strasse",
 "gemaess", "fuss")
PFLICHT = ("id jahr papier block aufgabe teilaufgabe seite punkte hilfsmittel leitidee thema typ format "
           "operator antwort material skizze kontext textumfang gegeben gesucht verfahren schritte "
           "ergebnis niveau_geschaetzt fehlerquelle").split()


def lies(pfad):
    if not os.path.exists(pfad):
        sys.exit(f"{pfad} fehlt – Datei neben das Skript legen.")
    return io.open(pfad, encoding="utf-8").read()


def liste_aus_klammer(text, feld):
    """'feld (a; b c; d)' -> {'a','b','d'} – erstes Wort je Teil (Kern § 5)."""
    m = re.search(r"\b" + re.escape(feld) + r" \(([^()]*)\)", text)
    if not m:
        sys.exit(f"{KERN}: Werteliste für {feld} nicht gefunden.")
    return {t.strip().split()[0] for t in m.group(1).split(";") if t.strip()}


def vokabular():
    """Kopfzeile und Formvokabular aus dem Kern, Leitideen und Themen aus msa.md § 5–6."""
    kern, profil = lies(KERN), lies(PROFIL)
    m = re.search(r"^Kopfzeile:\s*\n(id;.+)$", kern, re.M)
    if not m or m.group(1).strip().split(";") != HEAD:
        sys.exit(f"{KERN}: Kopfzeile fehlt oder weicht von HEAD ab.")
    v = {feld: liste_aus_klammer(kern, feld)
         for feld in ("format", "antwort", "material", "zahlenraum", "textumfang", "niveau_geschaetzt")}
    m = re.search(r"^## 5 Leitideen.*?\n\s*\n(.+?)\n", profil, re.S | re.M)
    if not m:
        sys.exit(f"{PROFIL}: Leitideen (§ 5) nicht gefunden.")
    leitideen = [s.strip() for s in m.group(1).split("·") if s.strip()]
    sec = profil.split("## 6 Themenliste", 1)[1].split("\n## ", 1)[0]
    themen = {}
    for l in sec.splitlines():
        m = re.match(r"^([^:]+): (.+)$", l)
        if m and m.group(1).strip() in leitideen:
            themen[m.group(1).strip()] = [s.strip() for s in m.group(2).split("·") if s.strip()]
    fehlt = [l for l in leitideen if l not in themen]
    if fehlt:
        sys.exit(f"{PROFIL}: keine Themenzeile für {fehlt}")
    return v, leitideen, themen


VOK, LEITIDEEN, THEMEN = vokabular()


def lade(pfad, kopf):
    if not os.path.exists(pfad):
        return kopf, []
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    if not rows:
        return kopf, []
    if rows[0] != kopf:
        sys.exit(f"{pfad}: Kopfzeile weicht ab")
    return rows[0], rows[1:]


def schreibe(pfad, kopf, zeilen):
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(kopf)
        for z in zeilen:
            w.writerow(z)


def pruefe_zeile(z, a, typ_namen, alle_ids, konfig=None):
    """Prüfungen je Katalogzeile nach Kern § 5 und § 7; konfig nur für neue Zeilen."""
    i = z["id"]
    for k in PFLICHT:
        a(z[k].strip() != "", f"{i}: Pflichtfeld leer: {k}")
    a(PAPIER.fullmatch(i) is not None, f"{i}: Kennung folgt nicht dem Muster Jahr-papier-BlockAufgabeTeilaufgabe")
    a(i.startswith(f"{z['jahr']}-{z['papier']}-"), f"{i}: jahr oder papier passt nicht zur Kennung")
    a(z["block"] in KAT, f"{i}: block muss Basis oder Kontext sein")
    a(i.split("-")[-1][0] == ("B" if z["block"] == "Basis" else "K"), f"{i}: Blockkürzel passt nicht zu block")
    a(z["leitidee"] in THEMEN, f"{i}: Leitidee unbekannt: {z['leitidee']}")
    a(z["thema"] in THEMEN.get(z["leitidee"], []), f"{i}: Thema passt nicht zur Leitidee: {z['thema']}")
    a(z["stern"] in ("ja", "nein", ""), f"{i}: stern ungültig")
    a(z["hilfsmittel"] in ("ja", "nein"), f"{i}: hilfsmittel ungültig")
    a(z["afb_amtlich"] == "" or re.fullmatch(r"I{1,3}(\|I{1,3})*", z["afb_amtlich"]), f"{i}: afb_amtlich ungültig")
    for feld in ("textumfang", "niveau_geschaetzt"):
        a(z[feld] in VOK[feld], f"{i}: {feld} ungültig: {z[feld]}")
    for feld in ("format", "antwort", "material", "zahlenraum"):
        for teil in [s for s in z[feld].split("|") if s]:
            a(teil in VOK[feld], f"{i}: {feld} hat unbekannten Wert: {teil}")
    for feld in ("typ", "typ_neben"):
        for t in [s for s in z[feld].split("|") if s]:
            a(t in typ_namen, f"{i}: Typ nicht in {TYP}: {t}")
    for dep in [s for s in z["abhaengig_von"].split("|") if s]:
        a(dep in alle_ids, f"{i}: abhaengig_von zeigt ins Leere: {dep}")
    for k, v in z.items():
        a("?" not in v or k == "bemerkung" or z["bemerkung"].strip() != "",
          f"{i}: Fragezeichen in {k} ohne Grund in bemerkung")
        a(not re.search(r"(?<=[\d\s(])-(?=\d)", v), f"{i}: ASCII-Bindestrich als Minus in {k}")
        a(k in ("stichwoerter",) or not [w for w in UMSCHRIFT if w in v.lower()],
          f"{i}: ASCII-Umschrift in {k}: {v[:40]}")
    if konfig:
        a(z["jahr"] == konfig["jahr"] and z["papier"] == konfig["papier"], f"{i}: Heftkennung falsch")
        grenze = konfig["seiten"][z["block"]] if isinstance(konfig["seiten"], dict) else konfig["seiten"]
        a(int(z["seite"]) <= grenze, f"{i}: Seite größer als der Heftumfang")


def main():
    fehler = []
    def a(cond, msg):
        if not cond:
            fehler.append(msg)

    alt = {b: lade(p, HEAD)[1] for b, p in KAT.items()}
    alt_gym = lade(GYM_DATEI, HEAD)[1]
    _, alt_typ = lade(TYP, TYP_HEAD)
    typ_namen = {r[0] for r in alt_typ} | {t[0] for t in NEUE_TYPEN}

    # Feldkorrektur an der Typenliste (Kopf): nur, was noch nicht so dasteht
    korrigiert = []
    for r in alt_typ:
        if r[0] in TYPEN_KORREKTUR:
            for feld, neu in TYPEN_KORREKTUR[r[0]].items():
                j = TYP_HEAD.index(feld)
                if r[j] != neu:
                    korrigiert.append((r[0], feld, r[j], neu)); r[j] = neu
    fremd = sorted(set(TYPEN_KORREKTUR) - {r[0] for r in alt_typ})
    a(not fremd, f"TYPEN_KORREKTUR nennt unbekannte Typen: {fremd}")

    if not ZEILEN:
        # ------------------------------------------------ Selbstprüfung des Bestands
        alle = [dict(zip(HEAD, r)) for b in KAT for r in alt[b]] + [dict(zip(HEAD, r)) for r in alt_gym]
        alle_ids = [z["id"] for z in alle]
        a(len(set(alle_ids)) == len(alle_ids), "doppelte id im Bestand")
        for b in KAT:
            for r in alt[b]:
                z = dict(zip(HEAD, r))
                a(z["papier"] != "GYM", f"{z['id']}: GYM-Zeile steht in {KAT[b]}, gehört nach {GYM_DATEI}")
                a(z["block"] == b, f"{z['id']}: steht in {KAT[b]}, trägt aber block {z['block']}")
                pruefe_zeile(z, a, typ_namen, set(alle_ids))
        for r in alt_gym:
            z = dict(zip(HEAD, r))
            a(z["papier"] == "GYM", f"{z['id']}: Nicht-GYM-Zeile steht in {GYM_DATEI}")
            a(z["block"] in KAT, f"{z['id']}: block muss Basis oder Kontext sein")
            pruefe_zeile(z, a, typ_namen, set(alle_ids))
        verwendet = {t for z in alle for f in ("typ", "typ_neben") for t in z[f].split("|") if t}
        for r in alt_typ:
            t = dict(zip(TYP_HEAD, r))
            a(t["leitidee"] in THEMEN and t["thema"] in THEMEN.get(t["leitidee"], []),
              f"Typ {t['typ']}: Leitidee oder Thema unbekannt ({t['leitidee']} / {t['thema']})")
            a(t["beispiel_id"] in alle_ids, f"Typ {t['typ']}: beispiel_id nicht im Katalog")
            a(t["typ"] in verwendet, f"Typ {t['typ']}: in keiner Zeile verwendet")
            a(t["status"] in STATUS, f"Typ {t['typ']}: status ungültig: {t['status']}")
            a(len(t["definition"]) > 20, f"Typ {t['typ']}: Definition zu knapp")
        if fehler:
            print(f"Selbstprüfung: {len(fehler)} Fehler:")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        if korrigiert:
            schreibe(TYP, TYP_HEAD, alt_typ)
            print(f"Feldkorrektur an {TYP} ({len(korrigiert)} Felder):")
            for typ, feld, vorher, nachher in korrigiert:
                print(f"  {typ} · {feld}: {vorher!r} → {nachher!r}")
        n_b, n_k, n_g = len(alt["Basis"]), len(alt["Kontext"]), len(alt_gym)
        hefte = sorted({(z["jahr"], z["papier"]) for z in alle})
        print(f"Selbstprüfung bestanden: {n_b + n_k} Katalogzeilen ({n_b} Basis, {n_k} Kontext) plus "
              f"{n_g} GYM-Zeilen aus {len(hefte)} Heften, {len(alt_typ)} Typen, alle verwendet, jede "
              f"beispiel_id im Katalog. ZEILEN ist leer, "
              f"{'nur die Feldkorrektur geschrieben' if korrigiert else 'nichts geschrieben'}.")
        return

    # ------------------------------------------------------- Heftlauf
    alt_ids = {r[0] for b in KAT for r in alt[b]} | {r[0] for r in alt_gym}
    neue_ids = [z["id"] for z in ZEILEN]
    a(len(set(neue_ids)) == len(neue_ids), "doppelte id in ZEILEN")
    for i in neue_ids:
        a(i not in alt_ids, f"{i}: Kennung steht schon im Katalog")
    for t in NEUE_TYPEN:
        a(t[0] not in {r[0] for r in alt_typ}, f"Typ {t[0]}: steht schon in {TYP}")
        a(t[1] in THEMEN and t[2] in THEMEN.get(t[1], []), f"Typ {t[0]}: Leitidee oder Thema unbekannt")
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog")
        a(len(t[3]) > 20, f"Typ {t[0]}: Definition zu knapp")
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        a(ist == soll, f"Aufgabe {nr}: Punkte {ist}, Soll {soll}")
    a(sum(int(z["punkte"]) for z in ZEILEN) == KONFIG["soll_gesamt"],
      f"Gesamtpunktzahl weicht von {KONFIG['soll_gesamt']} ab")
    verwendet = set()
    for z in ZEILEN:
        pruefe_zeile(z, a, typ_namen, alt_ids | set(neue_ids), KONFIG)
        verwendet |= {t for f in ("typ", "typ_neben") for t in z[f].split("|") if t}
    a(not ({t[0] for t in NEUE_TYPEN} - verwendet),
      f"neue Typen unbenutzt: {sorted({t[0] for t in NEUE_TYPEN} - verwendet)}")
    if fehler:
        print(f"ABBRUCH – {len(fehler)} Fehler, nichts geschrieben:")
        for f_ in fehler:
            print(" -", f_)
        sys.exit(1)

    for b, p in KAT.items():
        neu = [[z[k] for k in HEAD] for z in ZEILEN if z["block"] == b and z["papier"] != "GYM"]
        if neu:
            schreibe(p, HEAD, alt[b] + neu)
    neu_gym = [[z[k] for k in HEAD] for z in ZEILEN if z["papier"] == "GYM"]
    if neu_gym:
        schreibe(GYM_DATEI, HEAD, alt_gym + neu_gym)
    schreibe(TYP, TYP_HEAD, alt_typ + [[t[0], t[1], t[2], t[3], t[4], "neu"] for t in NEUE_TYPEN])

    # Rückweg: geschriebene Dateien mit echtem Leser einlesen und vergleichen
    DATEIEN_GESCHRIEBEN = [(p, [z for z in ZEILEN if z["block"] == b and z["papier"] != "GYM"], alt[b])
                            for b, p in KAT.items()] + [(GYM_DATEI, [z for z in ZEILEN if z["papier"] == "GYM"], alt_gym)]
    for p, zeilen_p, alt_p in DATEIEN_GESCHRIEBEN:
        if not zeilen_p:
            continue
        _, zurueck = lade(p, HEAD)
        for gel, z in zip(zurueck[len(alt_p):], zeilen_p):
            if len(gel) != 37 or any(v != z[k] for k, v in zip(HEAD, gel)):
                sys.exit(f"{z['id']}: Rückweg verändert die Zeile")
        roh = io.open(p, encoding="utf-8", newline="").read()
        if "\r" in roh or not all(l.startswith('"') and l.endswith('"') for l in roh.splitlines()):
            sys.exit(f"{p}: Ausgabe nicht vollständig gequotet oder CRLF")

    print(f"Heft {KONFIG['jahr']} {KONFIG['papier']} – {len(ZEILEN)} Zeilen, {len(NEUE_TYPEN)} Typen neu\n")
    print(f"{'id':<16} {'P':>2}  {'thema':<38} {'typ':<44} ergebnis")
    for z in ZEILEN:
        print(f"{z['id']:<16} {z['punkte']:>2}  {z['thema']:<38} {z['typ']:<44} {z['ergebnis'][:60]}")
    print()
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        print(f"Aufgabe {nr}: Ist {ist} / Soll {soll}")
    print(f"Gesamt: {sum(int(z['punkte']) for z in ZEILEN)} / {KONFIG['soll_gesamt']}")
    unsicher = [z["id"] for z in ZEILEN if any("?" in v for v in z.values())]
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
