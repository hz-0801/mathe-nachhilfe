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
    "jahr": "2023",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "",         # zweiteiliges Heft ab 2019, siehe "dateien"
    "dateien": ["23_P10_Ma_Gym_A1.pdf", "23_P10_Ma_Gym_A2.pdf"],
    "seiten": {"Basis": 3, "Kontext": 9},  # eigene Fußzeile je Teildatei (msa.md § 3)
    "soll": {"1": 5, "2": 5, "3": 11, "4": 10, "5": 10, "6": 9},
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
    ("Symmetrie einer geraden Funktion zur Bestimmung eines Funktionswertes ohne Rechnung nutzen",
     "Gleichungen und Funktionen", "Funktionen allgemein",
     "Ohne erneute Rechnung den Funktionswert an der Stelle −x angeben, wenn der Funktionswert an der "
     "Stelle x bekannt und die Funktion achsensymmetrisch zur y-Achse ist.",
     "2023-GYM-K3a"),
    ("Flächeninhalt eines Vierecks aus den Achsenschnittpunkten zweier Funktionsgraphen berechnen",
     "Raum und Form", "Ebene Figuren und Winkel",
     "Flächeninhalt eines Vierecks berechnen, dessen Eckpunkte die Schnittpunkte zweier "
     "Funktionsgraphen mit den Koordinatenachsen sind, z. B. über die Diagonalenlänge bei einer Raute.",
     "2023-GYM-K3c"),
    ("Innendurchmesser eines Kreisrings aus Flächeninhalt und Außendurchmesser berechnen",
     "Größen und Messen", "Flächeninhalt und Umfang",
     "Innendurchmesser eines Kreisrings durch Umstellen der Formel für die Ringfläche "
     "(A = π·(R² − r²)) aus dem Flächeninhalt und dem Außendurchmesser berechnen.",
     "2023-GYM-K4b"),
    ("Gesamtmenge aus Pro-Kopf-Angabe, Anteil und Einwohnerzahl berechnen", "Zahlen und Operationen",
     "Prozentrechnung",
     "Gesamtmenge einer Größe aus einer Pro-Kopf-Angabe, einem Anteil davon (Bruch oder Prozent) und der "
     "Einwohnerzahl berechnen und in eine größere Einheit umrechnen.",
     "2023-GYM-K4c"),
    ("Prozentualen Zuwachs aus Anfangs- und Endwert berechnen", "Zahlen und Operationen",
     "Prozentrechnung",
     "Prozentuale Veränderung zwischen einem Anfangs- und einem Endwert berechnen "
     "(Differenz bezogen auf den Anfangswert).",
     "2023-GYM-K5b"),
    ("Grundstücksbreiten aus einem in Teilflächen zerlegten Trapez bestimmen", "Raum und Form",
     "Ähnlichkeit und Strahlensätze",
     "Breiten der einzelnen Grundstücke an der Basis eines Trapezes bestimmen, das durch zwei zur "
     "Grundseite parallele Schnitte in ein rechteckiges Mittelstück (Fläche gegeben) und zwei "
     "kongruente, symmetrisch anschließende Trapeze zerlegt ist, unter Nutzung der über die "
     "Strahlensätze linear verlaufenden Gesamtbreite.",
     "2023-GYM-K6c"),
    ("Trapezhöhe über den aus einem angrenzenden Dreieck übertragenen Winkel berechnen", "Raum und Form",
     "Ähnlichkeit und Strahlensätze",
     "Höhe eines Trapezes berechnen, dessen Schenkel geradlinig in die Schenkel eines angrenzenden "
     "gleichschenkligen Dreiecks übergehen: den Basiswinkel des Dreiecks aus dessen Spitzenwinkel "
     "bestimmen, über die parallelen Grundlinien auf den entsprechenden Trapezwinkel übertragen und "
     "damit die Höhe aus der bekannten Schenkellänge berechnen.",
     "2023-GYM-K6d"),
]

row(id="2023-GYM-B1a", block="Basis", aufgabe="1", titel="", teilaufgabe="a", seite="2",
    punkte="2", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Nullstelle lineare Funktion berechnen",
    stichwoerter="Nullstelle|lineare Funktion", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −0,5x + 2",
    gesucht="Nullstelle von f",
    verfahren="−0,5x + 2 = 0 nach x auflösen", schritte="1", zahlenraum="dezimal",
    ergebnis="x = 4", niveau_geschaetzt="I", fehlerquelle="das Vorzeichen von −0,5x beim Auflösen falsch "
                 "umstellen")

row(id="2023-GYM-B1b", block="Basis", aufgabe="1", titel="", teilaufgabe="b", seite="2",
    punkte="3", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Lage zweier Geraden bestimmen",
    stichwoerter="Schnittpunkt|Gleichsetzen", format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz", abhaengig_von="2023-GYM-B1a",
    gegeben="f(x) = −0,5x + 2 und g(x) = 0,5x",
    gesucht="Koordinaten des Schnittpunktes S von f und g",
    verfahren="−0,5x + 2 = 0,5x nach x auflösen, dann y berechnen", schritte="2", zahlenraum="dezimal",
    ergebnis="S(2|1)", niveau_geschaetzt="II",
    fehlerquelle="nach dem Bestimmen von x vergessen, den y-Wert durch Einsetzen zu berechnen")

row(id="2023-GYM-B2a", block="Basis", aufgabe="2", titel="", teilaufgabe="a", seite="3",
    punkte="3", hilfsmittel="nein", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Term zu Figur angeben",
    stichwoerter="Fünfeck|Rechteck minus Dreieck|Flächeninhalt", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur",
    skizze="Fünfeck ABCDE: rechte Winkel bei A und B, AB=a (unten), BC=b (rechts, senkrecht), CD=c (oben, "
           "waagerecht), DE=d (links, senkrecht, von D nach unten zu E), EA schließt das Fünfeck "
           "diagonal; nicht maßstabsgerecht", kontext="ohne", textumfang="mittel",
    gegeben="a = 6 cm, b = 2·a, c = a:3, d = a",
    gesucht="Flächeninhalt des Fünfecks ABCDE",
    verfahren="Rechteck mit den Seiten a und b als Grundfigur, davon das Dreieck mit den Katheten (a−c) "
              "und (b−d) am linken Rand abziehen: A = a·b − 0,5·(a−c)·(b−d)", schritte="3",
    zahlenraum="dezimal", einheiten="cm|cm²",
    ergebnis="a=6 cm, b=12 cm, c=2 cm, d=6 cm; Fläche = 36 cm²", niveau_geschaetzt="III",
    fehlerquelle="das Fünfeck als einfaches Rechteck a·b ohne Abzug des Dreiecks berechnen")

row(id="2023-GYM-B2b", block="Basis", aufgabe="2", titel="", teilaufgabe="b", seite="3",
    punkte="2", hilfsmittel="nein", leitidee="Größen und Messen", thema="Satz des Pythagoras",
    typ="Streckenlänge aus Koordinaten berechnen",
    stichwoerter="Fünfeck|Term|Pythagoras", format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Figur", skizze="wie 2023-GYM-B2a", kontext="ohne", textumfang="kurz",
    abhaengig_von="2023-GYM-B2a",
    gegeben="Fünfeck ABCDE mit den Bezeichnungen a, b, c, d wie in der Abbildung",
    gesucht="Term für die Länge der Seite AE mithilfe von a, b, c und d",
    verfahren="AE ist die Hypotenuse eines rechtwinkligen Dreiecks mit den Katheten (a−c) und (b−d)",
    schritte="1",
    ergebnis="AE = √((a−c)² + (b−d)²)", niveau_geschaetzt="III",
    fehlerquelle="die Katheten des Hilfsdreiecks mit a und b statt mit den Differenzen (a−c) und (b−d) "
                 "ansetzen")

row(id="2023-GYM-K3a", block="Kontext", aufgabe="3", titel="Quadratische Funktionen", teilaufgabe="a",
    seite="2", punkte="3", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Punktprobe durchführen",
    typ_neben="Symmetrie einer geraden Funktion zur Bestimmung eines Funktionswertes ohne Rechnung nutzen",
    stichwoerter="Punktprobe|Achsensymmetrie|ohne Rechnung", format="Rechnung|Begründung",
    operator="Weisen Sie nach|Geben Sie an", antwort="Text|Zahl", material="Koordinatensystem",
    skizze="nach oben geöffnete Parabel f(x)=x²−4 mit Scheitelpunkt (0|−4), Nullstellen bei −2 und 2",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x² − 4; Punkt A(1/3 | −35/9); Punkt B(−1/3 | yB) ebenfalls auf dem Graphen von f",
    gesucht="Nachweis, dass A auf dem Graphen liegt; fehlende Koordinate yB ohne Rechnung",
    verfahren="f(1/3) = (1/3)² − 4 = −35/9 einsetzen und mit dem gegebenen Wert vergleichen; f ist "
              "achsensymmetrisch zur y-Achse (nur gerade Potenzen von x), also f(−1/3) = f(1/3)",
    schritte="2", zahlenraum="Bruch",
    ergebnis="f(1/3) = −35/9 bestätigt; yB = −35/9", niveau_geschaetzt="III",
    fehlerquelle="yB dennoch durch erneutes Einsetzen statt durch das Symmetrieargument bestimmen")

row(id="2023-GYM-K3b", block="Kontext", aufgabe="3", titel="Quadratische Funktionen", teilaufgabe="b",
    seite="3", punkte="2", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Nullstellen quadratische Funktion berechnen",
    stichwoerter="Nullstellen|Nachweis", format="Rechnung", operator="Zeigen Sie rechnerisch",
    antwort="Text", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    abhaengig_von="2023-GYM-K3a",
    gegeben="f(x) = x² − 4",
    gesucht="Nachweis, dass −2 und 2 Nullstellen von f sind",
    verfahren="f(−2) und f(2) einsetzen und beide Male 0 als Ergebnis zeigen", schritte="1",
    zahlenraum="ganz", ergebnis="f(−2) = 0 und f(2) = 0", niveau_geschaetzt="I",
    fehlerquelle="nur eine der beiden Nullstellen nachrechnen")

row(id="2023-GYM-K3c", block="Kontext", aufgabe="3", titel="Quadratische Funktionen", teilaufgabe="c",
    seite="3", punkte="6", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parabel an der x-Achse spiegeln",
    typ_neben="Flächeninhalt eines Vierecks aus den Achsenschnittpunkten zweier Funktionsgraphen "
              "berechnen",
    stichwoerter="Spiegelung an x-Achse|Raute|Diagonalen", format="Zeichnen|Kurzantwort|Zeichnen|Rechnung",
    operator="Zeichnen Sie|Geben Sie an|Zeichnen Sie|Berechnen Sie", antwort="Grafik|Term|Grafik|Zahl",
    material="Koordinatensystem",
    skizze="Parabel f(x)=x²−4 und ihr Spiegelbild g an der x-Achse; die vier Schnittpunkte der beiden "
           "Graphen mit den Achsen bilden ein Viereck (Raute)", kontext="ohne", textumfang="mittel",
    abhaengig_von="2023-GYM-K3b",
    gegeben="f(x) = x² − 4; g entsteht durch Spiegelung von f an der x-Achse; Schnittpunkte von f und g "
            "mit den Koordinatenachsen: (−2|0), (2|0), (0|−4), (0|4)",
    gesucht="Graph und Gleichung von g; Flächeninhalt des von den vier Achsenschnittpunkten gebildeten "
            "Vierecks",
    verfahren="g(x) = −f(x) = −x² + 4; das Viereck ist eine Raute mit den Diagonalen entlang der Achsen "
              "(Länge 4 und 8), Fläche = 0,5 · Diagonale1 · Diagonale2", schritte="2", zahlenraum="ganz",
    einheiten="FE",
    ergebnis="g(x) = −x² + 4; Flächeninhalt = 16 FE", niveau_geschaetzt="III",
    fehlerquelle="das Viereck als Rechteck mit den Seiten 4 und 8 statt als Raute mit halbem "
                 "Diagonalenprodukt berechnen")

row(id="2023-GYM-K4a", block="Kontext", aufgabe="4", titel="Abfallbehälter", teilaufgabe="a", seite="4",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Volumen Zylinder berechnen",
    stichwoerter="Zylinder|Fassungsvermögen|Einheitenumrechnung", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur",
    skizze="Abfallbehälter als gerader Kreiszylinder, Höhe 80 cm, Innendurchmesser 57 cm; nicht "
           "maßstabsgerecht", kontext="Umwelt", textumfang="kurz",
    gegeben="Höhe 80 cm, Innendurchmesser 57 cm",
    gesucht="maximales Fassungsvermögen in dm³",
    verfahren="V = π · (57:2)² · 80 in cm³, anschließend durch 1000 in dm³ umrechnen", schritte="2",
    zahlenraum="dezimal", einheiten="cm|dm³", ergebnis="V ≈ 204,1 dm³", niveau_geschaetzt="II",
    fehlerquelle="den Durchmesser statt des Radius in die Formel einsetzen, oder die Umrechnung von cm³ "
                 "in dm³ vergessen")

row(id="2023-GYM-K4b", block="Kontext", aufgabe="4", titel="Abfallbehälter", teilaufgabe="b", seite="4",
    punkte="4", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Innendurchmesser eines Kreisrings aus Flächeninhalt und Außendurchmesser berechnen",
    stichwoerter="Kreisring|Abdeckplatte|Mülleinwurf", format="Rechnung", operator="Ermitteln Sie",
    antwort="Zahl", material="Figur",
    skizze="kreisringförmige Abdeckplatte mit Außendurchmesser 60 cm und einer kreisrunden Öffnung "
           "(Mülleinwurf) in der Mitte; nicht maßstabsgerecht", kontext="Umwelt", textumfang="kurz",
    gegeben="Außendurchmesser 60 cm, Flächeninhalt des Kreisrings ≈ 2120,6 cm²",
    gesucht="Durchmesser des Mülleinwurfs (Innendurchmesser des Kreisrings)",
    verfahren="A = π·(R² − r²) nach r umstellen: r = √(R² − A:π), mit R = 30 cm", schritte="1",
    zahlenraum="dezimal", einheiten="cm", ergebnis="r ≈ 15 cm, Durchmesser ≈ 30 cm",
    niveau_geschaetzt="III",
    fehlerquelle="den gegebenen Außendurchmesser 60 cm direkt als Radius R in die Formel einsetzen")

row(id="2023-GYM-K4c", block="Kontext", aufgabe="4", titel="Abfallbehälter", teilaufgabe="c", seite="5",
    punkte="3", leitidee="Zahlen und Operationen", thema="Prozentrechnung",
    typ="Gesamtmenge aus Pro-Kopf-Angabe, Anteil und Einwohnerzahl berechnen",
    stichwoerter="Restmülltonne|Mülltrennung|Einwohnerzahl", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="Umwelt", textumfang="mittel",
    gegeben="128 kg Haushaltsmüll je Einwohner in der Restmülltonne (2021); zwei Drittel davon fälschlich "
            "einsortiert; Einwohnerzahl Brandenburgs ≈ 2,5 Millionen",
    gesucht="insgesamt fälschlich in der Restmülltonne entsorgter Haushaltsmüll in Tonnen",
    verfahren="128 kg · 2 500 000 · 2/3, anschließend von kg in Tonnen umrechnen", schritte="2",
    zahlenraum="ganz", einheiten="kg|t", ergebnis="≈ 213 333 t", niveau_geschaetzt="II",
    fehlerquelle="die Umrechnung von Kilogramm in Tonnen (Faktor 1000) vergessen")

row(id="2023-GYM-K5a", block="Kontext", aufgabe="5", titel="Fahrrad", teilaufgabe="a", seite="6",
    punkte="3", leitidee="Daten und Zufall", thema="Daten darstellen",
    typ="Streifendiagramm zeichnen",
    stichwoerter="Fahrradarten|Streifendiagramm|Anteile", format="Zeichnen", operator="Zeichnen Sie",
    antwort="Grafik", material="keins", skizze="keine", kontext="Freizeit/Sport", textumfang="mittel",
    gegeben="72 Fahrräder insgesamt; ein Viertel Rennräder; 45 Jugendliche kommen mit dem Mountainbike, "
            "der Rest mit dem Tourenrad; Streifen 10 cm lang, 1 cm breit",
    gesucht="Streifendiagramm der drei Fahrradarten",
    verfahren="Rennräder = 72:4 = 18, Mountainbikes = 45, Tourenräder = 72 − 18 − 45 = 9; Streifenlängen "
              "proportional zu den Anteilen: 18:72·10 cm, 45:72·10 cm, 9:72·10 cm", schritte="2",
    zahlenraum="dezimal", einheiten="cm",
    ergebnis="Rennräder 2,5 cm, Mountainbikes 6,25 cm, Tourenräder 1,25 cm", niveau_geschaetzt="II",
    fehlerquelle="die Anzahl der Tourenräder nicht als Rest, sondern als weiteres Viertel ansetzen")

row(id="2023-GYM-K5b", block="Kontext", aufgabe="5", titel="Fahrrad", teilaufgabe="b", seite="6",
    punkte="2", leitidee="Zahlen und Operationen", thema="Prozentrechnung",
    typ="Prozentualen Zuwachs aus Anfangs- und Endwert berechnen",
    stichwoerter="Fahrradbestand|prozentualer Anstieg", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="Freizeit/Sport", textumfang="kurz",
    gegeben="2011 etwa 70 Millionen Fahrräder in Deutschland, 2021 etwa 81 Millionen",
    gesucht="prozentualer Anstieg in den zehn Jahren",
    verfahren="(81 − 70) : 70 · 100 %", schritte="1", zahlenraum="dezimal", einheiten="Prozent",
    ergebnis="≈ 15,7 %", niveau_geschaetzt="II",
    fehlerquelle="die Differenz auf den Endwert 81 statt auf den Anfangswert 70 beziehen")

row(id="2023-GYM-K5c", block="Kontext", aufgabe="5", titel="Fahrrad", teilaufgabe="c", seite="6",
    punkte="3", leitidee="Daten und Zufall", thema="Kenngrößen",
    typ="Arithmetisches Mittel berechnen", typ_neben="Modalwert bestimmen",
    stichwoerter="Modalwert|Mittelwert|Umfrage", format="Kurzantwort|Rechnung",
    operator="Geben Sie an|Berechnen Sie", antwort="Zahl|Zahl", material="Tabelle",
    skizze="keine", kontext="Freizeit/Sport", textumfang="mittel",
    gegeben="Anzahl Fahrradtage von 20 Jugendlichen: 4,12,14,0,20,20,4,3,12,5,14,3,14,1,0,14,5,5,20,10",
    gesucht="Modalwert; durchschnittliche Anzahl Fahrradtage",
    verfahren="häufigster Wert der Liste bestimmen; Summe aller Werte durch 20 teilen", schritte="2",
    zahlenraum="ganz", einheiten="Tage",
    ergebnis="Modalwert 14 (viermal); Durchschnitt 9 Tage", niveau_geschaetzt="II",
    fehlerquelle="beim Mittelwert durch die Anzahl verschiedener Werte statt durch die Anzahl der "
                 "Jugendlichen (20) teilen")

row(id="2023-GYM-K5d", block="Kontext", aufgabe="5", titel="Fahrrad", teilaufgabe="d", seite="7",
    punkte="2", leitidee="Daten und Zufall", thema="Kenngrößen",
    typ="Fehlenden Wert aus Mittelwert bestimmen",
    stichwoerter="verspätete Jugendliche|neuer Mittelwert|Ergänzung", format="Rechnung",
    operator="Bestimmen Sie", antwort="Zahl", material="Tabelle", skizze="keine", kontext="Freizeit/Sport",
    textumfang="mittel", abhaengig_von="2023-GYM-K5c",
    gegeben="ursprüngliche Liste von 20 Werten (Summe 180, aus Teilaufgabe c); vier weitere Werte "
            "verspäteter Jugendlicher ergänzt; neuer Durchschnitt über 24 Werte beträgt 10 Tage",
    gesucht="eine mögliche Ergänzung der vier fehlenden Werte",
    verfahren="neue Gesamtsumme = 10 · 24 = 240; Summe der vier neuen Werte = 240 − 180 = 60, also im "
              "Mittel 15 Tage je ergänztem Wert", schritte="2", zahlenraum="ganz", einheiten="Tage",
    ergebnis="z. B. vier Werte mit Summe 60, etwa 15, 15, 15, 15", niveau_geschaetzt="III",
    fehlerquelle="die neue Gesamtsumme aus 10 · 20 statt aus 10 · 24 berechnen")

row(id="2023-GYM-K6a", block="Kontext", aufgabe="6", titel="Wohngebiet", teilaufgabe="a", seite="8",
    punkte="2", leitidee="Größen und Messen", thema="Satz des Pythagoras",
    typ="Pythagoras Hypotenuse",
    stichwoerter="gleichschenkliges Dreieck|Wohngebietsgrenze|Höhe", format="Rechnung",
    operator="Zeigen Sie", antwort="Text", material="Figur",
    skizze="gleichschenkliges Dreieck (Wohngebiet), Basis Lessingstraße 80 m, Höhe (Breite) 100 m, "
           "Schenkel Goethestraße und Schillerstraße; nicht maßstabsgerecht", kontext="Bauwesen",
    textumfang="kurz",
    gegeben="gleichschenkliges Dreieck mit Basis 80 m (Lessingstraße) und Höhe 100 m",
    gesucht="Nachweis, dass die Schillerstraße (Schenkel) etwa 107,7 m lang ist",
    verfahren="Satz des Pythagoras im halben Dreieck: Schenkel = √((80:2)² + 100²)", schritte="1",
    zahlenraum="ganz", einheiten="m", ergebnis="≈ 107,70 m", niveau_geschaetzt="II",
    fehlerquelle="die volle Basis 80 m statt der halben Basis 40 m als Kathete verwenden")

row(id="2023-GYM-K6b", block="Kontext", aufgabe="6", titel="Wohngebiet", teilaufgabe="b", seite="8",
    punkte="1", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Strecke aus Teilstrecken berechnen",
    stichwoerter="Zaun|Umfang|Dreieck", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bauwesen", textumfang="kurz", abhaengig_von="2023-GYM-K6a",
    gegeben="gleichschenkliges Dreieck mit Basis 80 m und Schenkellänge ≈ 107,7 m (aus Teilaufgabe a)",
    gesucht="Länge des Zauns entlang der gesamten Wohngebietsgrenze",
    verfahren="Umfang = Basis + 2 · Schenkellänge", schritte="1", zahlenraum="dezimal", einheiten="m",
    ergebnis="≈ 295,4 m", niveau_geschaetzt="I",
    fehlerquelle="nur einen Schenkel statt beider Schenkel zur Basis addieren")

row(id="2023-GYM-K6c", block="Kontext", aufgabe="6", titel="Wohngebiet", teilaufgabe="c", seite="9",
    punkte="3", leitidee="Raum und Form", thema="Ähnlichkeit und Strahlensätze",
    typ="Grundstücksbreiten aus einem in Teilflächen zerlegten Trapez bestimmen",
    stichwoerter="Trapez|rechteckiges Grundstück|Strahlensatz", format="Rechnung", operator="Ermitteln Sie",
    antwort="Zahl", material="Figur",
    skizze="Bereich I (Trapez, Basis 80 m an der Lessingstraße, Höhe 30 m) in drei Grundstücke A "
           "(Trapez), B (Rechteck), C (Trapez, kongruent zu A) geteilt; nicht maßstabsgerecht",
    kontext="Bauwesen", textumfang="mittel", abhaengig_von="2023-GYM-K6a",
    gegeben="Bereich I ist 30 m breit (Höhe); Gesamtdreieck Basis 80 m, Höhe 100 m; Grundstück B "
            "rechteckig mit 600 m² Flächeninhalt; A und C sind gleich große Trapeze",
    gesucht="Länge der Grundstücksgrenzen von A, B und C zur Lessingstraße",
    verfahren="obere Breite des Bereichs I (Grenze zu Bereich II) über den Strahlensatz: 80 · (1 − 30:100) "
              "= 56 m; Breite von B (rechteckig, konstant) = 600 m² : 30 m = 20 m; verbleibende Breite "
              "80 − 20 = 60 m verteilt sich gleich auf A und C: je 30 m", schritte="3",
    zahlenraum="ganz", einheiten="m|m²",
    ergebnis="Grenze von A zur Lessingstraße 30 m, von B 20 m, von C 30 m", niveau_geschaetzt="III",
    fehlerquelle="die Breite von B aus der oberen (56 m) statt aus der unteren Gesamtbreite (80 m) "
                 "ermitteln")

row(id="2023-GYM-K6d", block="Kontext", aufgabe="6", titel="Wohngebiet", teilaufgabe="d", seite="9",
    punkte="3", leitidee="Raum und Form", thema="Ähnlichkeit und Strahlensätze",
    typ="Trapezhöhe über den aus einem angrenzenden Dreieck übertragenen Winkel berechnen",
    stichwoerter="Bereich II|Bereich III|Basiswinkel|Breite x", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur",
    skizze="Bereich III als gleichschenkliges Dreieck mit Spitzenwinkel α an der Spitze und Basis a; "
           "Bereich II als gleichschenkliges Trapez darunter mit Grundlinien a (oben) und Schenkeln b, c "
           "(a=b=c=32 m), Basiswinkel β an den unteren Ecken; nicht maßstabsgerecht",
    kontext="Bauwesen", textumfang="mittel", abhaengig_von="2023-GYM-K6c",
    gegeben="Bereich II: a = b = c = 32 m; Bereich III: Spitzenwinkel α = 43,6°",
    gesucht="Breite x des Bereichs II",
    verfahren="Basiswinkel des gleichschenkligen Dreiecks III: (180° − 43,6°) : 2 = 68,2°; da "
              "Goethestraße und Schillerstraße gerade Linien sind, ist dies auch der Basiswinkel β des "
              "Trapezes II; Breite x = b · sin(β)", schritte="3", zahlenraum="dezimal", einheiten="m",
    ergebnis="β = 68,2°, Breite x ≈ 29,71 m", niveau_geschaetzt="III",
    fehlerquelle="den Spitzenwinkel α unverändert als Basiswinkel β des Trapezes verwenden, statt ihn "
                 "über die Winkelsumme im gleichschenkligen Dreieck III umzurechnen")
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
