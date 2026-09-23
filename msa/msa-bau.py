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
    "jahr": "2014",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "14_P10_Gym_Ma_A_Set1.pdf",  # einteiliges Heft (2014–2018 ein Heft, msa.md § 3)
    "dateien": [],
    "seiten": 7,
    "soll": {"1": 10, "2": 10, "3": 8, "4": 10, "5": 12},
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
    ("Kreisumfang berechnen", "Größen und Messen", "Flächeninhalt und Umfang",
     "Umfang eines Kreises aus dem Durchmesser oder Radius berechnen (U = π·d bzw. U = 2π·r).",
     "2014-GYM-B1a"),
    ("Antiproportionale Zuordnung Dreisatz", "Gleichungen und Funktionen", "Zuordnungen proportional und antiproportional",
     "Bei einer antiproportionalen Zuordnung (z. B. Vorrat für mehr oder weniger Personen oder Tiere) aus "
     "einem Wertepaar über das konstante Produkt den fehlenden vierten Wert bestimmen.",
     "2014-GYM-B1c"),
    ("Fehlenden Wert aus Spannweite bestimmen", "Daten und Zufall", "Kenngrößen",
     "Aus der vorgegebenen Spannweite und den übrigen Werten einer Liste den fehlenden Wert (neues Maximum "
     "oder Minimum) bestimmen.",
     "2014-GYM-B1e"),
    ("Prozentanteil einer Rasterfläche markieren", "Zahlen und Operationen", "Prozentrechnung",
     "In einem Rechteckraster aus gleich großen Kästchen die zu einem vorgegebenen Prozentsatz gehörende "
     "Anzahl an Kästchen markieren.",
     "2014-GYM-B1g"),
    ("Lage zweier Geraden bestimmen", "Gleichungen und Funktionen", "Lineare Funktionen",
     "Aus den Gleichungen zweier linearer Funktionen (Steigung, y-Achsenabschnitt) entscheiden, ob sich die "
     "Geraden schneiden, parallel oder identisch sind.",
     "2014-GYM-B1i"),
    ("Gerade an der x-Achse spiegeln", "Gleichungen und Funktionen", "Lineare Funktionen",
     "Spiegelbild einer linearen Funktion an der x-Achse zeichnen und die Gleichung des Spiegelbilds angeben "
     "(Vorzeichenwechsel des gesamten Funktionsterms).",
     "2014-GYM-K2b"),
    ("Gerade an der y-Achse spiegeln", "Gleichungen und Funktionen", "Lineare Funktionen",
     "Erläutern oder angeben, wie sich die Gleichung einer linearen Funktion bei Spiegelung an der y-Achse "
     "ändert (Vorzeichenwechsel der Steigung, y-Achsenabschnitt bleibt gleich).",
     "2014-GYM-K2b"),
    ("Parabelgleichung aus Scheitel und Punkt bestimmen", "Gleichungen und Funktionen", "Quadratische Funktionen",
     "Koeffizienten a, b, c einer Parabel p(x) = ax² + bx + c aus dem Scheitelpunkt und einem weiteren Punkt "
     "des Graphen bestimmen und den Graphen zeichnen.",
     "2014-GYM-K2c"),
    ("Datenreihen anhand von Kenngrößen vergleichen und begründen", "Daten und Zufall", "Kenngrößen",
     "Zwei Datenreihen mit gleichem oder unterschiedlichem Mittelwert anhand einer weiteren Kenngröße (z. B. "
     "der Spannweite) vergleichen und eine Entscheidung begründen.",
     "2014-GYM-K3b"),
    ("Maximale ganzzahlige Menge aus Grenzwert berechnen", "Zahlen und Operationen", "Runden und Überschlag",
     "Aus einer Höchstmenge (z. B. Dosisgrenze) und der Menge je Einheit (Kapsel, Packung) die größte ganze "
     "Anzahl an Einheiten bestimmen, die die Grenze nicht überschreitet (Abrunden).",
     "2014-GYM-K4a"),
    ("Graph eines exponentiellen Vorgangs zeichnen", "Gleichungen und Funktionen", "Exponentialfunktionen und Wachstum",
     "Punkte eines exponentiellen Wachstums- oder Zerfallsprozesses aus einer Wertetabelle oder "
     "Rekursionsvorschrift in ein vorgegebenes Koordinatensystem eintragen.",
     "2014-GYM-K4b"),
    ("Zeit aus Exponentialgleichung berechnen", "Gleichungen und Funktionen", "Exponentialfunktionen und Wachstum",
     "Aus einer Exponentialgleichung a · b^t = c den Exponenten t durch Logarithmieren berechnen.",
     "2014-GYM-K4c"),
    ("Winkel im allgemeinen Dreieck über Kosinussatz berechnen", "Größen und Messen", "Sinussatz",
     "Im allgemeinen Dreieck einen Winkel aus den drei gegebenen Seiten mit dem Kosinussatz berechnen.",
     "2014-GYM-K5b"),
    ("Transportanzahl aus Volumen und Masse berechnen", "Größen und Messen", "Volumen und Oberfläche",
     "Aus einem Gesamtvolumen, der Dichte und einer maximalen Ladekapazität die Anzahl der nötigen "
     "Transportfahrten (aufgerundet) berechnen.",
     "2014-GYM-K5c"),
]

row(id="2014-GYM-B1a", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="a", seite="2",
    punkte="1", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang", typ="Kreisumfang berechnen",
    stichwoerter="Kreis|Umfang|Durchmesser", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="kreisförmige Uhr mit Durchmesser 15 cm", gesucht="Umfang der Uhr",
    verfahren="U = π · d = π · 15", schritte="1", zahlenraum="ganz|dezimal", einheiten="cm",
    ergebnis="47,12 cm", niveau_geschaetzt="I",
    fehlerquelle="Radius statt Durchmesser einsetzen (U = π·r statt π·d)")

row(id="2014-GYM-B1b", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="b", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Zinsrechnung", typ="Prozentwert berechnen",
    stichwoerter="Zinsen|Zinssatz|Kapital|ein Jahr", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bank/Sparen", textumfang="kurz",
    gegeben="Kapital 2 000 €, Zinssatz 2 % pro Jahr, Laufzeit 1 Jahr", gesucht="Zinsen nach einem Jahr",
    verfahren="2 000 € · 0,02", schritte="1", zahlenraum="ganz|Prozent", einheiten="€",
    ergebnis="40 €", niveau_geschaetzt="I",
    fehlerquelle="Prozentsatz als Wachstumsfaktor statt als Zins berechnen")

row(id="2014-GYM-B1c", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="c", seite="2",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Zuordnungen proportional und antiproportional",
    typ="Antiproportionale Zuordnung Dreisatz",
    stichwoerter="Futtervorrat|antiproportional|Dreisatz", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Landwirtschaft", textumfang="kurz",
    gegeben="Futtervorrat für 4 Pferde reicht 8 Tage", gesucht="Reichdauer für 8 Pferde",
    verfahren="4 · 8 = 32 (Pferdetage); 32 : 8", schritte="2", zahlenraum="ganz", einheiten="Tage",
    ergebnis="4 Tage", niveau_geschaetzt="II",
    fehlerquelle="proportional statt antiproportional rechnen (16 Tage statt 4)")

row(id="2014-GYM-B1d", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="d", seite="2",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parabelgleichung zu Graph zuordnen",
    stichwoerter="Parabel|Scheitel|Normalparabel", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="Koordinatensystem",
    skizze="Koordinatensystem x von −2 bis 2, y von −4 bis 1, Gitter 1; Normalparabel mit Scheitel (0|−4) und "
           "Nullstellen (−2|0) und (2|0)",
    kontext="ohne", textumfang="kurz",
    gegeben="Parabel y = x² + c im Koordinatensystem (Scheitel bei y = −4, Nullstellen bei x = ±2); Auswahl "
            "c = 2, c = −2, c = −4",
    gesucht="richtiger Wert für c",
    verfahren="Scheitel der Normalparabel y = x² + c liegt bei (0|c); abgelesen c = −4",
    schritte="1", zahlenraum="negativ", ergebnis="c = −4", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen von c vertauschen (c = 4 statt −4 ablesen)")

row(id="2014-GYM-B1e", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="e", seite="2",
    punkte="1", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Fehlenden Wert aus Spannweite bestimmen",
    stichwoerter="Spannweite|Zahlenliste|Maximum", format="Kurzantwort", operator="Ergänzen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Zahlenliste 13; 18; 21; 21; 24; ___, Spannweite soll 25 sein", gesucht="fehlende Zahl",
    verfahren="Spannweite = Maximum − Minimum; bei Minimum 13 muss das neue Maximum 13+25=38 sein",
    schritte="1", zahlenraum="ganz", ergebnis="38?", niveau_geschaetzt="II",
    fehlerquelle="25 direkt als fehlende Zahl angeben statt zur Spannweite zu ergänzen",
    bemerkung="Ergebnis unsicher: Die aufsteigende Reihe legt eine sechste, größte Zahl nahe, daher 38 als "
              "neues Maximum; rechnerisch wäre auch −1 als neues Minimum möglich, im Heft nicht ausgeschlossen.")

row(id="2014-GYM-B1f", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="f", seite="2",
    punkte="1", leitidee="Raum und Form", thema="Ebene Figuren und Winkel", typ="Eigenschaft einer Figur zuordnen",
    stichwoerter="Trapez|Eigenschaft|parallele Seiten", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="drei Aussagen über Trapeze: rechter Winkel; ein Paar paralleler Seiten; gleich lange Diagonalen",
    gesucht="einzig richtige Aussage",
    verfahren="Definitionseigenschaft des Trapezes ist das Paar paralleler Seiten",
    schritte="1", ergebnis="ein Paar paralleler Seiten", niveau_geschaetzt="I",
    fehlerquelle="Eigenschaft des Rechtecks oder der Raute mit der des allgemeinen Trapezes verwechseln")

row(id="2014-GYM-B1g", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="g", seite="3",
    punkte="1", leitidee="Zahlen und Operationen", thema="Prozentrechnung",
    typ="Prozentanteil einer Rasterfläche markieren",
    stichwoerter="Prozent|Raster|Kästchen markieren", format="Eintragen", operator="Markieren Sie", antwort="Grafik",
    material="Diagramm", skizze="quadratisches Raster aus 5 mal 5 gleich großen Kästchen (25 Kästchen), unmarkiert",
    kontext="ohne", textumfang="kurz",
    gegeben="Raster aus 25 gleich großen Kästchen", gesucht="Markierung von 8 % der Fläche",
    verfahren="8 % von 25 Kästchen = 2 Kästchen; zwei beliebige Kästchen markieren",
    schritte="1", zahlenraum="ganz|Prozent", ergebnis="2 von 25 Kästchen markiert", niveau_geschaetzt="II",
    fehlerquelle="8 Kästchen markieren (Prozentzahl direkt als Kästchenzahl gelesen)")

row(id="2014-GYM-B1h", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="h", seite="3",
    punkte="2", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang", typ="Quadratseite aus Fläche berechnen",
    stichwoerter="Rechteck|Quadrat|Flächeninhalt", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Rechteck mit a = 4 cm, b = 16 cm", gesucht="Seite s eines flächengleichen Quadrats",
    verfahren="A = 4 · 16 = 64; s = √64", schritte="2", zahlenraum="ganz", einheiten="cm",
    ergebnis="8 cm", zwischenergebnis="A = 64 cm²", niveau_geschaetzt="II",
    fehlerquelle="Umfang statt Flächeninhalt gleichsetzen")

row(id="2014-GYM-B1i", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="i", seite="3",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen", typ="Lage zweier Geraden bestimmen",
    stichwoerter="Geraden|parallel|Steigung", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g(x) = 3x + 7, f(x) = 3x − 7", gesucht="Lagebeziehung der Geraden",
    verfahren="gleiche Steigung (3), unterschiedlicher y-Achsenabschnitt (7 ≠ −7) → parallel, nicht identisch",
    schritte="1", ergebnis="Die Geraden sind parallel.", niveau_geschaetzt="II",
    fehlerquelle="gleiche Steigung sofort als „identisch“ werten, ohne den y-Achsenabschnitt zu vergleichen")

row(id="2014-GYM-K2a", block="Kontext", aufgabe="2", titel="Quadratische und lineare Funktionen", teilaufgabe="a",
    seite="4", punkte="1", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Eigenschaften eines Graphen beurteilen",
    stichwoerter="Gerade|Monotonie|fallend", format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Koordinatensystem",
    skizze="Koordinatensystem x von −2 bis 6, y von −4 bis 4, Gitter 0,5 (Beschriftung ganzzahlig); Gerade g "
           "durch (0|3) und (1,5|0), Steigung −2, gezeichnet etwa von (−0,7|4,5) bis (3,8|−4,7)",
    kontext="ohne", textumfang="kurz",
    gegeben="Gerade g im Koordinatensystem (Gleichung noch nicht angegeben; g(x) = −2x + 3)",
    gesucht="Monotonieverhalten von g", verfahren="Steigung von g ist negativ (Graph fällt von links nach rechts)",
    schritte="1", ergebnis="streng monoton fallend", niveau_geschaetzt="I",
    fehlerquelle="aus der Lage im Koordinatensystem statt aus der Steigung auf die Monotonie schließen")

row(id="2014-GYM-K2b", block="Kontext", aufgabe="2", titel="Quadratische und lineare Funktionen", teilaufgabe="b",
    seite="4", punkte="4", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Gerade an der x-Achse spiegeln", typ_neben="Gerade an der y-Achse spiegeln",
    stichwoerter="Spiegelung|x-Achse|y-Achse|Geradengleichung", format="Zeichnen|Kurzantwort|Begründung",
    operator="Zeichnen Sie|Geben Sie an|Erläutern Sie", antwort="Grafik|Term|Text",
    material="Koordinatensystem",
    skizze="Spiegelbild g' von g an der x-Achse einzeichnen: Gerade durch (0|−3) und (1,5|0), Steigung 2",
    kontext="ohne", textumfang="mittel",
    gegeben="Gerade g: g(x) = −2x + 3 (aus a) bestimmt); g soll an der x-Achse, danach an der y-Achse "
            "gespiegelt werden",
    gesucht="Spiegelbild g' und seine Gleichung; Vorgehen zur Gleichung von g'' ohne Zeichnung",
    verfahren="Spiegelung an der x-Achse: Vorzeichen des gesamten Funktionsterms wechselt, g'(x) = −g(x) = "
              "2x − 3; Spiegelung an der y-Achse: x wird durch −x ersetzt, g''(x) = g(−x) = 2x + 3",
    schritte="2", zahlenraum="negativ", abhaengig_von="2014-GYM-K2a",
    ergebnis="g'(x) = 2x − 3|x in der Gleichung von g durch −x ersetzen; dadurch wechselt nur das Vorzeichen "
             "der Steigung, g''(x) = 2x + 3",
    niveau_geschaetzt="II",
    fehlerquelle="bei der Spiegelung an der y-Achse zusätzlich das Vorzeichen von n ändern")

row(id="2014-GYM-K2c", block="Kontext", aufgabe="2", titel="Quadratische und lineare Funktionen", teilaufgabe="c",
    seite="4", punkte="5", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parabelgleichung aus Scheitel und Punkt bestimmen", typ_neben="Parabel aus Gleichung skizzieren",
    stichwoerter="Parabel|Scheitelpunkt|Koeffizienten", format="Kurzantwort|Zeichnen", operator="Ermitteln Sie|Zeichnen Sie",
    antwort="Term|Grafik", material="Koordinatensystem",
    skizze="Parabel p mit Scheitel (1,5|0) und y-Achsenabschnitt (0|3) in dasselbe Koordinatensystem wie g "
           "einzeichnen",
    kontext="ohne", textumfang="mittel",
    gegeben="Scheitelpunkt von p liegt auf dem Schnittpunkt von g mit der x-Achse (1,5|0); Graph von p "
            "schneidet die y-Achse im gleichen Punkt wie g (0|3); p(x) = ax² + bx + c mit a, b, c, x ∈ ℝ, a ≠ 0",
    gesucht="Koeffizienten a, b, c; Graph von p",
    verfahren="Scheitelpunktform p(x) = a(x−1,5)²; aus p(0)=3 folgt a·2,25=3, a=4/3; ausmultipliziert "
              "p(x) = 4/3 x² − 4x + 3",
    schritte="3", zahlenraum="Bruch|negativ", abhaengig_von="2014-GYM-K2a",
    ergebnis="a = 4/3, b = −4, c = 3", zwischenergebnis="Scheitel S(1,5|0)", niveau_geschaetzt="III",
    fehlerquelle="Scheitelpunktform mit a = 1 ansetzen und den zweiten Punkt nicht zur Bestimmung von a nutzen")

row(id="2014-GYM-K3a", block="Kontext", aufgabe="3", titel="Sportfest", teilaufgabe="a", seite="5",
    punkte="2", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Arithmetisches Mittel berechnen",
    stichwoerter="Mittelwert|Weitsprung|Vergleich", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze="keine", kontext="Sport", textumfang="mittel",
    gegeben="Weitsprungergebnisse Peter: 4,58 m; 3,97 m; 5,30 m; 7,05 m; 5,55 m. Franz: 5,10 m; 5,55 m; "
            "5,05 m; 4,30 m; 6,45 m",
    gesucht="Mittelwert je Sportler", verfahren="Summe der fünf Werte durch 5",
    schritte="2", zahlenraum="dezimal", einheiten="m", ergebnis="Peter 5,29 m|Franz 5,29 m",
    niveau_geschaetzt="I", fehlerquelle="durch die Anzahl unterschiedlicher Werte statt durch 5 teilen")

row(id="2014-GYM-K3b", block="Kontext", aufgabe="3", titel="Sportfest", teilaufgabe="b", seite="5",
    punkte="2", leitidee="Daten und Zufall", thema="Kenngrößen",
    typ="Datenreihen anhand von Kenngrößen vergleichen und begründen",
    stichwoerter="Spannweite|Vergleich|Begründung", format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Sport", textumfang="kurz",
    gegeben="beide Sportler haben denselben Mittelwert (5,29 m); der Sportlehrer delegiert Franz zur "
            "Kreismeisterschaft",
    gesucht="Begründung der Entscheidung anhand eines Vergleichs der Ergebnisse",
    verfahren="Spannweite vergleichen: Peter 7,05−3,97=3,08 m, Franz 6,45−4,30=2,15 m; Franz springt "
              "gleichmäßiger",
    schritte="1", zahlenraum="dezimal", einheiten="m", abhaengig_von="2014-GYM-K3a",
    ergebnis="Franz hat trotz gleichen Mittelwerts die kleinere Spannweite (2,15 m gegen 3,08 m) und damit "
             "die konstantere Leistung", niveau_geschaetzt="III",
    fehlerquelle="nur den gleichen Mittelwert vergleichen und keine weitere Kenngröße heranziehen")

row(id="2014-GYM-K3c", block="Kontext", aufgabe="3", titel="Sportfest", teilaufgabe="c", seite="5",
    punkte="4", leitidee="Daten und Zufall", thema="Zählen und Kombinatorik", typ="Anzahl der Anordnungen bestimmen",
    typ_neben="Wahrscheinlichkeit einstufig",
    stichwoerter="Anordnung|Startreihenfolge|Wahrscheinlichkeit", format="Rechnung|Rechnung",
    operator="Ermitteln Sie|Berechnen Sie", antwort="Zahl|Zahl", material="keins", skizze="keine",
    kontext="Sport", textumfang="mittel",
    gegeben="5 Schüler im Finale, Startnummern werden aus einer Urne mit 5 Losen gezogen; Franz ist im Finale",
    gesucht="Anzahl der möglichen Reihenfolgen; Wahrscheinlichkeit, dass Franz als Erster oder Zweiter startet",
    verfahren="Anordnungen: 5! = 120; Wahrscheinlichkeit über Symmetrie: jeder Platz für Franz gleich "
              "wahrscheinlich (1/5), Platz 1 oder 2 also 2/5",
    schritte="2", zahlenraum="ganz|Bruch", ergebnis="120 Möglichkeiten|P = 2/5 = 0,4", niveau_geschaetzt="II",
    fehlerquelle="Reihenfolge mit Auswahl verwechseln (5 statt 5! Möglichkeiten) oder Franz auf einen festen "
                 "Platz setzen")

row(id="2014-GYM-K4a", block="Kontext", aufgabe="4", titel="Im Krankenhaus", teilaufgabe="a", seite="6",
    punkte="3", leitidee="Zahlen und Operationen", thema="Runden und Überschlag",
    typ="Maximale ganzzahlige Menge aus Grenzwert berechnen",
    stichwoerter="Dosis|Körpermasse|Abrunden", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Medizin", textumfang="mittel",
    gegeben="Einzeldosis 15 mg je kg Körpermasse, Körpermasse 85 kg, eine Kapsel enthält 500 mg",
    gesucht="Anzahl ganzer Kapseln ohne Gesundheitsgefährdung",
    verfahren="Grenzmenge 85 · 15 = 1 275 mg; 1 275 : 500 = 2,55, abgerundet 2 Kapseln",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="mg|kg", ergebnis="2 Kapseln", niveau_geschaetzt="II",
    fehlerquelle="auf 3 Kapseln aufrunden statt aus Sicherheitsgründen abzurunden")

row(id="2014-GYM-K4b", block="Kontext", aufgabe="4", titel="Im Krankenhaus", teilaufgabe="b", seite="6",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Graph eines exponentiellen Vorgangs zeichnen", typ_neben="Funktionswert berechnen|Wachstumsart begründen",
    stichwoerter="exponentieller Zerfall|Halbierung|Diagramm", format="Zeichnen|Rechnung|Begründung",
    operator="Zeichnen Sie|Ermitteln Sie|Begründen Sie", antwort="Grafik|Zahl|Text", material="Diagramm",
    skizze="Diagramm Masse in mg (0 bis 600, Gitter 100) über Zeit in Stunden (0 bis 6); einzutragen die "
           "Punkte (1|500), (2|250), (3|125), (4|62,5), (5|31,25)",
    kontext="Medizin", textumfang="lang",
    gegeben="1 Kapsel mit 500 mg, vollständige Aufnahme nach 1 Stunde, danach Halbierung der Masse je Stunde",
    gesucht="Verlauf des Abbaus für vier Stunden ab t=1h; Masse drei Stunden nach der Einnahme; Begründung "
            "für exponentiellen Zerfall",
    verfahren="je Stunde Halbierung: 500, 250, 125, 62,5, 31,25 mg; bei t=3h (zwei Halbierungen nach t=1h) "
              "500 · 0,5² = 125 mg; konstanter Verhältnisfaktor 0,5 je Stunde statt konstanter Differenz "
              "kennzeichnet den exponentiellen Zerfall",
    schritte="3", zahlenraum="dezimal", einheiten="mg|h", abhaengig_von="2014-GYM-K4a",
    ergebnis="Punkte (1|500) bis (5|31,25)|125 mg|gleichbleibender Faktor 0,5 je Stunde statt konstanter "
             "Differenz", niveau_geschaetzt="II",
    fehlerquelle="„drei Stunden nach der Einnahme“ mit „drei Stunden nach Abbaubeginn“ verwechseln (dann "
                 "62,5 mg statt 125 mg)",
    bemerkung="Zeitpunkt „drei Stunden nach der Einnahme“ ab t=0 (Einnahme) gezählt, nicht ab t=1 "
              "(Abbaubeginn); daher t=3 in f(t).")

row(id="2014-GYM-K4c", block="Kontext", aufgabe="4", titel="Im Krankenhaus", teilaufgabe="c", seite="6",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Zeit aus Exponentialgleichung berechnen",
    stichwoerter="Exponentialgleichung|Logarithmus|Abbauzeit", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="Medizin", textumfang="mittel",
    gegeben="f(t) = 1 000 · 0,5^t mit t ≥ 1, f(t) Masse des Wirkstoffes in mg, t Zeit in Stunden ab Einnahme",
    gesucht="Zeit t, zu der die Masse auf 5 mg gesunken ist",
    verfahren="1 000 · 0,5^t = 5; 0,5^t = 0,005; t = log(0,005) : log(0,5)",
    schritte="3", zahlenraum="dezimal", einheiten="mg|h", abhaengig_von="2014-GYM-K4b",
    ergebnis="t ≈ 7,64 h", niveau_geschaetzt="III",
    fehlerquelle="Gleichung durch schrittweises Halbieren statt durch Logarithmieren lösen und dabei nur "
                 "ganze Stunden probieren")

row(id="2014-GYM-K5a", block="Kontext", aufgabe="5", titel="Abraumhalde", teilaufgabe="a", seite="7",
    punkte="4", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang", typ="Kreisfläche berechnen",
    typ_neben="Flächeninhalt zusammengesetzter Figur berechnen",
    stichwoerter="Halbkegel|Pyramide|Bodenfläche", format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Foto|Figur",
    skizze="räumliche Skizze: Kegelspitze S über Halbkreisgrundfläche mit Mittelpunkt M, Radius DM=154 m; "
           "D und A als Endpunkte des Durchmessers; Pyramide mit Grundpunkten A, B (und Bogenpunkt C) und "
           "Spitze S; Winkel α bei D, Winkel β bei S zwischen SD und SB; Strecken BS=214 m, AS=DS=193 m, "
           "BD=334 m",
    kontext="Bergbau/Umwelt", textumfang="lang",
    gegeben="Halde aus halbem Kreiskegel (Radius r=DM=154 m) und schiefer Pyramide zusammengesetzt; von der "
            "Pyramide allein abgedeckte Fläche ca. 27 720 m²",
    gesucht="von der gesamten Halde abgedeckte Fläche",
    verfahren="Grundfläche Halbkegel = 0,5 · π · r² = 0,5 · π · 154²; Gesamtfläche = Pyramidenfläche + "
              "Halbkreisfläche",
    schritte="2", zahlenraum="dezimal", einheiten="m²", ergebnis="ca. 64 973 m²",
    zwischenergebnis="Halbkreisfläche ≈ 37 253 m²", niveau_geschaetzt="II",
    fehlerquelle="vollen statt halben Kreis für die Kegelgrundfläche ansetzen (dann ca. 102 226 m²)",
    bemerkung="Deutung der Skizze: A und D als Endpunkte des Kegeldurchmessers (AS=DS=193 m bestätigt die "
              "Symmetrie), B zusätzlicher Pyramidenpunkt, C Bogenpunkt ohne eigene Maßangabe; α und C werden "
              "für die Teilaufgaben a–c nicht gebraucht.")

row(id="2014-GYM-K5b", block="Kontext", aufgabe="5", titel="Abraumhalde", teilaufgabe="b", seite="7",
    punkte="3", leitidee="Größen und Messen", thema="Sinussatz",
    typ="Winkel im allgemeinen Dreieck über Kosinussatz berechnen",
    stichwoerter="Kosinussatz|Winkel|Dreieck", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze="Dreieck DSB aus der Skizze von a) mit den drei gegebenen Seiten", kontext="Bergbau/Umwelt",
    textumfang="kurz", gegeben="Dreieck DSB mit BS=214 m, DS=193 m, BD=334 m",
    gesucht="Winkel β = ∠DSB an der Spitze",
    verfahren="Kosinussatz BD² = BS² + DS² − 2·BS·DS·cos(β); cos(β) = (214²+193²−334²) : (2·214·193)",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="m|Grad", abhaengig_von="2014-GYM-K5a",
    ergebnis="β ≈ 110,19°", niveau_geschaetzt="III",
    fehlerquelle="Sinussatz statt Kosinussatz ansetzen, obwohl kein Winkel gegeben ist",
    bemerkung="Thema „Sinussatz“ ersatzweise gewählt: die Themenliste (msa.md § 6) führt keine eigene "
              "Kosinussatz-Zeile; nächstliegendes Thema ist die allgemeine Dreiecksberechnung ohne rechten "
              "Winkel.")

row(id="2014-GYM-K5c", block="Kontext", aufgabe="5", titel="Abraumhalde", teilaufgabe="c", seite="7",
    punkte="5", leitidee="Größen und Messen", thema="Volumen und Oberfläche", typ="Volumen Kegel berechnen",
    typ_neben="Transportanzahl aus Volumen und Masse berechnen",
    stichwoerter="Kegelvolumen|Erdmasse|LKW-Ladungen", format="Rechnung|Rechnung",
    operator="Ermitteln Sie|Berechnen Sie", antwort="Zahl|Zahl", material="Figur",
    skizze="dieselbe räumliche Skizze wie in a)", kontext="Bergbau/Umwelt", textumfang="lang",
    gegeben="Pyramidenvolumen ca. 1 070 000 m³, 1 m³ Erdreich hat Masse 1,8 t, Ladekapazität je Transporter "
            "höchstens 25 t; Kegelradius r=154 m, Kegelkante (Mantellinie) DS=193 m",
    gesucht="Volumen des halben Kegels; Anzahl der LKW-Ladungen für das gesamte Erdreich",
    verfahren="Kegelhöhe h = √(193²−154²) ≈ 116,33 m (Pythagoras); V(halber Kegel) = 0,5 · (1/3) · π · r² · h; "
              "Gesamtvolumen = Pyramidenvolumen + Kegelvolumen; Masse = Gesamtvolumen · 1,8; Ladungen = "
              "Masse : 25, aufgerundet",
    schritte="5", zahlenraum="dezimal", einheiten="m|m³|t", abhaengig_von="2014-GYM-K5a",
    ergebnis="V(halber Kegel) ≈ 1 444 565 m³|181 049 Ladungen",
    zwischenergebnis="h ≈ 116,33 m; Gesamtvolumen ≈ 2 514 565 m³; Gesamtmasse ≈ 4 526 217 t",
    niveau_geschaetzt="III", fehlerquelle="Ladungen abrunden statt aufrunden (letzte, nicht volle Ladung "
                                          "vergessen)",
    bemerkung="Kegelhöhe h nicht gegeben, aus Radius r=154 m und der Mantellinie DS=193 m über den Satz des "
              "Pythagoras hergeleitet (S senkrecht über M angenommen).")

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
