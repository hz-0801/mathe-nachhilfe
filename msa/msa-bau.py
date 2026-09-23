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
    "jahr": "2017",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "17_P10_Ma_Gym_A.pdf",  # einteiliges Heft (2014–2018 ein Heft, msa.md § 3)
    "dateien": [],
    "seiten": 11,
    "soll": {"1": 10, "2": 11, "3": 10, "4": 9, "5": 10},
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
    ("Parameter einer Parabel aus Graph bestimmen", "Gleichungen und Funktionen", "Quadratische Funktionen",
     "Parameter b und c einer Parabel in der Form y = ax² + bx + c (a gegeben) aus zwei Punkten des "
     "abgebildeten Graphen bestimmen (z. B. Nullstellen oder Scheitelpunkt).",
     "2017-GYM-K2c"),
    ("Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen", "Raum und Form", "Ebene Figuren und Winkel",
     "Umfang eines Drachenvierecks berechnen, dessen vier Seiten aus den (ungleich geteilten) Abschnitten der "
     "beiden zueinander senkrechten Diagonalen über den Satz des Pythagoras bestimmt werden; benötigte "
     "Randstücke werden je Seite einzeln aufgerundet.",
     "2017-GYM-K3b"),
    ("Flächeninhalt eines Drachenvierecks aus Diagonalen berechnen", "Größen und Messen", "Flächeninhalt und Umfang",
     "Flächeninhalt eines Drachenvierecks (oder einer Raute) aus den beiden Diagonalen mit A = 0,5 · e · f "
     "berechnen; die Formel gilt unabhängig davon, wo die Diagonalen einander schneiden.",
     "2017-GYM-K3c"),
    ("Winkel eines Drachenvierecks aus Diagonalenabschnitten berechnen", "Größen und Messen",
     "Trigonometrie im rechtwinkligen Dreieck",
     "Innenwinkel eines Drachenvierecks an einer Spitze aus den anliegenden Diagonalenabschnitten "
     "(rechtwinklige Teildreiecke) mit dem Tangens berechnen.",
     "2017-GYM-K3d"),
    ("Kantenlänge einer quadratischen Grundfläche aus Volumen berechnen", "Größen und Messen", "Volumen und Oberfläche",
     "Kantenlänge der quadratischen Grundfläche eines Quaders aus Volumen und Höhe durch Wurzelziehen "
     "bestimmen.",
     "2017-GYM-K4c"),
    ("Gleichverteilung der Trefferwahrscheinlichkeit begründen", "Daten und Zufall", "Wahrscheinlichkeit mehrstufig",
     "Begründen, dass bei zufälliger Reihenfolge ohne Zurücklegen jede Position dieselbe "
     "Trefferwahrscheinlichkeit hat (Symmetrieargument), am Beispiel der ersten und letzten Position.",
     "2017-GYM-K5c"),
    ("Anzahl Kombinationen nach dem Zählprinzip bestimmen", "Daten und Zufall", "Zählen und Kombinatorik",
     "Anzahl möglicher Kombinationen aus mehreren unabhängigen Auswahlkategorien durch Multiplikation der "
     "jeweiligen Möglichkeiten bestimmen (Zählprinzip).",
     "2017-GYM-K5d"),
]

row(id="2017-GYM-B1a", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="a", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Brüche und Dezimalzahlen", typ="Bruchteil einer Fläche bestimmen",
    stichwoerter="Bruchteil|Rechteck|schraffieren", format="Eintragen", operator="Schraffieren Sie", antwort="Grafik",
    material="Diagramm", skizze="Rechteck, in 7 gleich breite Spalten unterteilt, unmarkiert", kontext="ohne",
    textumfang="kurz", gegeben="Rechteck in 7 gleiche Teile unterteilt", gesucht="6/7 des Rechtecks schraffiert",
    verfahren="6 von 7 Spalten schraffieren", schritte="1", zahlenraum="Bruch",
    ergebnis="6 von 7 Spalten schraffiert", niveau_geschaetzt="I",
    fehlerquelle="7 von 7 (das ganze Rechteck) statt 6 von 7 schraffieren")

row(id="2017-GYM-B1b", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="b", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Prozentrechnung", typ="Prozentwert berechnen",
    stichwoerter="Rabatt|Prozent|Bohrmaschine", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Einkauf/Rabatt", textumfang="kurz",
    gegeben="Bohrmaschine 120,00 €, 20 % Rabatt an der Kasse", gesucht="Rabatt in Euro",
    verfahren="120 € · 0,20", schritte="1", zahlenraum="ganz|Prozent", einheiten="€", ergebnis="24 €",
    niveau_geschaetzt="I", fehlerquelle="den Restpreis (96 €) statt des Rabattbetrags angeben")

row(id="2017-GYM-B1c", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="c", seite="2",
    punkte="1", leitidee="Raum und Form", thema="Körper, Netze, Schrägbilder", typ="Körper aus Netz oder Schrägbild benennen",
    stichwoerter="Schrägbild|Prisma|Körper erkennen", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="Figur", skizze="Schrägbild eines dreiseitigen Prismas (liegend, mit sichtbarer Dreiecksfläche "
                             "vorn und gestrichelten Kanten hinten)", kontext="ohne", textumfang="kurz",
    gegeben="Schrägbild eines Körpers; Auswahl Pyramide, Prisma, Quader", gesucht="abgebildeter Körper",
    verfahren="zwei parallele deckungsgleiche Dreiecksflächen, verbunden durch Rechtecke → Prisma",
    schritte="1", ergebnis="Prisma", niveau_geschaetzt="I",
    fehlerquelle="die dreieckige Stirnfläche als Hinweis auf eine Pyramide statt auf ein Prisma deuten")

row(id="2017-GYM-B1d", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="d", seite="2",
    punkte="1", leitidee="Größen und Messen", thema="Satz des Pythagoras", typ="Pythagoras Gleichung zuordnen",
    stichwoerter="Pythagoras|rechtwinkliges Dreieck|Hypotenuse", format="Ankreuzen", operator="Kreuzen Sie an",
    antwort="Kreuz", material="Figur",
    skizze="rechtwinkliges Dreieck mit rechtem Winkel oben links (zwischen den Seiten x und z), Kathete x "
           "links, Kathete y unten, Hypotenuse z schräg von oben nach rechts unten",
    kontext="ohne", textumfang="kurz",
    gegeben="rechtwinkliges Dreieck mit Seiten x, y, z, rechter Winkel zwischen x und der Spitze; vier "
            "Gleichungen zur Auswahl",
    gesucht="zutreffende Gleichung", verfahren="Hypotenuse ist z (der Seite gegenüber dem rechten Winkel)",
    schritte="1", ergebnis="z² = x² + y²", niveau_geschaetzt="II",
    fehlerquelle="die Hypotenuse anhand der Zeichenposition statt anhand des rechten Winkels bestimmen")

row(id="2017-GYM-B1e", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="e", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Brüche und Dezimalzahlen",
    typ="Zahlen in verschiedenen Darstellungen vergleichen",
    stichwoerter="negative Zahlen|Zehnerpotenz|Vergleich", format="Ankreuzen", operator="Kreuzen Sie an",
    antwort="Kreuz", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="vier Zahlen: −0,01; −10³; −10²; −0,1", gesucht="kleinste Zahl",
    verfahren="Potenzen auswerten: −10³=−1000, −10²=−100; Vergleich aller vier Werte auf dem Zahlenstrahl",
    schritte="2", zahlenraum="negativ|Potenz", ergebnis="−10³", niveau_geschaetzt="II",
    fehlerquelle="den Betrag statt den tatsächlichen (negativen) Wert vergleichen und −0,01 als kleinste "
                 "Zahl wählen")

row(id="2017-GYM-B1f", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="f", seite="2",
    punkte="1", leitidee="Daten und Zufall", thema="Zählen und Kombinatorik", typ="Ergebnismenge aufzählen",
    stichwoerter="Münzwurf|Ergebnismenge|Zahl/Wappen", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Foto", skizze="keine", kontext="Glücksspiel", textumfang="kurz",
    gegeben="Münze wird zweimal geworfen, unterschieden wird Zahl (Z) und Wappen (W)",
    gesucht="Anzahl der möglichen Ergebnisse", verfahren="Ergebnisse auflisten: ZZ, ZW, WZ, WW", schritte="1",
    zahlenraum="ganz", ergebnis="4", niveau_geschaetzt="I",
    fehlerquelle="ZW und WZ als ein Ergebnis zählen (Reihenfolge nicht beachten, dann 3 statt 4)")

row(id="2017-GYM-B1g", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="g", seite="3",
    punkte="1", leitidee="Zahlen und Operationen", thema="Zehnerpotenzen und Näherungswerte",
    typ="Zehnerpotenzschreibweise umwandeln",
    stichwoerter="Zehnerpotenz|100000", format="Kurzantwort", operator="Schreiben Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Zahl 100 000", gesucht="Zahl als Zehnerpotenz", verfahren="Anzahl der Nullen als Exponent",
    schritte="1", zahlenraum="ganz", ergebnis="10⁵", niveau_geschaetzt="I",
    fehlerquelle="10⁴ oder 10⁶ statt 10⁵ angeben (Nullen falsch gezählt)")

row(id="2017-GYM-B1h", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="h", seite="3",
    punkte="1", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Arithmetisches Mittel berechnen",
    stichwoerter="Durchschnitt|arithmetisches Mittel|Längen", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="vier Werte: 1,8 m; 1,7 m; 1,6 m; 1,7 m", gesucht="arithmetisches Mittel",
    verfahren="(1,8+1,7+1,6+1,7) : 4", schritte="1", zahlenraum="dezimal", einheiten="m", ergebnis="1,7 m",
    niveau_geschaetzt="I", fehlerquelle="durch 3 statt durch 4 Werte teilen")

row(id="2017-GYM-B1i", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="i", seite="3",
    punkte="1", leitidee="Zahlen und Operationen", thema="Terme umformen", typ="Term zu Sachtext angeben",
    stichwoerter="Term|Dreifache|vermindert", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="„Das Dreifache einer Zahl wird um fünf vermindert.“; Auswahl 3(x−5), 5−3x, 3x−5, 3x−5x",
    gesucht="passender Term", verfahren="Dreifache: 3x; vermindert um fünf: 3x − 5", schritte="1",
    zahlenraum="ganz", ergebnis="3x − 5", niveau_geschaetzt="I",
    fehlerquelle="3(x−5) wählen (Reihenfolge von Verdreifachen und Vermindern vertauscht)")

row(id="2017-GYM-B1j", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="j", seite="3",
    punkte="1", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Winkelfunktion Seitenverhältnis angeben",
    stichwoerter="Sinus|rechtwinkliges Dreieck|Seitenverhältnis", format="Kurzantwort", operator="Geben Sie an",
    antwort="Term", material="Figur",
    skizze="rechtwinkliges Dreieck mit rechtem Winkel unten links (markiert), Kathete r links, Kathete s "
           "unten, Hypotenuse t schräg oben; Winkel β unten rechts zwischen s und t",
    kontext="ohne", textumfang="kurz",
    gegeben="rechtwinkliges Dreieck mit Katheten r, s und Hypotenuse t, Winkel β anliegend an s",
    gesucht="Gleichung für sin β", verfahren="sin β = Gegenkathete : Hypotenuse = r : t", schritte="1",
    ergebnis="sin β = r/t", niveau_geschaetzt="II",
    fehlerquelle="s (Ankathete) statt r (Gegenkathete) im Zähler verwenden")

row(id="2017-GYM-K2a", block="Kontext", aufgabe="2", titel="Quadratische Funktionen", teilaufgabe="a", seite="4",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Lösbarkeit quadratischer Gleichung beurteilen", typ_neben="Parabel aus Gleichung skizzieren|Funktionswert "
                                                                      "berechnen",
    stichwoerter="Scheitelpunktform|keine Nullstellen|Parabel zeichnen", format="Zeichnen|Begründung|Kurzantwort",
    operator="Zeichnen Sie|Zeigen Sie rechnerisch|Geben Sie an", antwort="Grafik|Text|Term",
    material="Koordinatensystem",
    skizze="Parabel f mit Scheitel (3|1,5), schmale Normalparabel, in dasselbe Koordinatensystem wie h "
           "einzeichnen; verläuft u. a. durch (0|10,5) und (6|10,5)",
    kontext="ohne", textumfang="lang",
    gegeben="f(x) = (x−3)² + 1,5, x ∈ ℝ",
    gesucht="Graph von f; Nachweis, dass f keine Nullstellen besitzt; Schnittpunkt von f mit der y-Achse",
    verfahren="(x−3)² ≥ 0 für alle x, also f(x) ≥ 1,5 > 0 für alle x → keine Nullstellen; f(0) = 9+1,5 = 10,5",
    schritte="2", zahlenraum="dezimal", ergebnis="f besitzt keine Nullstellen, da f(x) ≥ 1,5 > 0 für alle x|"
                                                 "Schnittpunkt mit der y-Achse: (0|10,5)", niveau_geschaetzt="III",
    fehlerquelle="die Diskriminante der ausmultiplizierten Form berechnen, statt das Vorzeichenargument über "
                 "die Scheitelpunktform zu nutzen")

row(id="2017-GYM-K2b", block="Kontext", aufgabe="2", titel="Quadratische Funktionen", teilaufgabe="b", seite="5",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen", typ="Parabel verschieben",
    stichwoerter="Verschiebung|Normalform|Parabel", format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Parabel f (aus a) um 2 Einheiten in positive x-Richtung und 3 Einheiten in negative y-Richtung "
            "verschoben",
    gesucht="Funktionsgleichung der verschobenen Parabel in Normalform",
    verfahren="neuer Scheitel (3+2|1,5−3)=(5|−1,5); (x−5)²−1,5 ausmultiplizieren", schritte="2",
    zahlenraum="negativ", abhaengig_von="2017-GYM-K2a", ergebnis="y = x² − 10x + 23,5",
    zwischenergebnis="neuer Scheitel (5|−1,5)", niveau_geschaetzt="II",
    fehlerquelle="die Verschiebungsrichtungen vertauschen (Scheitel (1|4,5) statt (5|−1,5))")

row(id="2017-GYM-K2c", block="Kontext", aufgabe="2", titel="Quadratische Funktionen", teilaufgabe="c", seite="5",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parameter einer Parabel aus Graph bestimmen",
    stichwoerter="Parabel h|Parameter b und c|Nullstellen ablesen", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Koordinatensystem",
    skizze="Koordinatensystem x von −5 bis 6, y von −2 bis 4; Parabel h mit Nullstellen bei x=−3 und x=1, "
           "Scheitel bei (−1|−2)",
    kontext="ohne", textumfang="mittel",
    gegeben="h(x) = 0,5x² + bx + c, b,c,x ∈ ℝ; Graph von h mit erkennbaren Nullstellen bei x=−3 und x=1",
    gesucht="Parameter b und c",
    verfahren="h(x) = 0,5(x−(−3))(x−1) = 0,5(x+3)(x−1) ausmultiplizieren: 0,5x²+x−1,5", schritte="2",
    zahlenraum="negativ|dezimal", ergebnis="b = 1, c = −1,5", niveau_geschaetzt="III",
    fehlerquelle="die Nullstellen mit dem Scheitelpunkt verwechseln und b,c über die Scheitelpunktform statt "
                 "über das Produkt der Nullstellen bestimmen",
    bemerkung="Nullstellen und Scheitel aus der Vektorgrafik des Graphen abgelesen (Kontrolle: h(−2)=−1,5, "
              "h(−3,5)=1,125, h(1,7)=1,645 stimmen mit dem gezeichneten Kurvenverlauf überein).")

row(id="2017-GYM-K2d", block="Kontext", aufgabe="2", titel="Quadratische Funktionen", teilaufgabe="d", seite="5",
    punkte="2", leitidee="Größen und Messen", thema="Satz des Pythagoras", typ="Streckenlänge aus Koordinaten berechnen",
    stichwoerter="Abstand|Ursprung|Schnittpunkt", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="Punkt P(2|2,5) im selben Koordinatensystem wie f und h", kontext="ohne",
    textumfang="kurz",
    gegeben="die Parabeln f und h schneiden sich im Punkt P(2|2,5)",
    gesucht="Abstand des Punktes P vom Koordinatenursprung",
    verfahren="d = √(2² + 2,5²)", schritte="1", zahlenraum="Wurzel|dezimal", einheiten="LE",
    abhaengig_von="2017-GYM-K2a", ergebnis="d = √10,25 ≈ 3,20 LE", niveau_geschaetzt="II",
    fehlerquelle="nur eine Koordinate als Abstand angeben, statt den Satz des Pythagoras anzuwenden")

row(id="2017-GYM-K3a", block="Kontext", aufgabe="3", titel="Spielplatz", teilaufgabe="a", seite="6",
    punkte="2", leitidee="Größen und Messen", thema="Maßstab", typ="Länge im Maßstab umrechnen",
    stichwoerter="Maßstab|Zeichnung|Planskizze", format="Zeichnen", operator="Fertigen Sie an", antwort="Grafik",
    material="Diagramm", skizze="Zeichnung des Drachenvierecks im Maßstab 1:250 in das vorgegebene Karo-Feld",
    kontext="Bauwesen", textumfang="kurz",
    gegeben="Drachenviereck mit den Diagonalenabschnitten 8,5 m und 7,5 m (Bezugsstrecke Spitze–Spitze), "
            "Maßstab 1:250",
    gesucht="maßstäbliche Zeichnung",
    verfahren="Längen durch 250 teilen und in cm umrechnen, z. B. 8,5 m = 850 cm : 250 = 3,4 cm", schritte="1",
    zahlenraum="dezimal", einheiten="m|cm", ergebnis="8,5 m → 3,4 cm; 7,5 m → 3 cm", niveau_geschaetzt="II",
    fehlerquelle="durch 250 teilen, aber die Einheit m statt cm im Ergebnis belassen")

row(id="2017-GYM-K3b", block="Kontext", aufgabe="3", titel="Spielplatz", teilaufgabe="b", seite="7",
    punkte="3", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen",
    stichwoerter="Bordsteine|Umfang|Drachenviereck", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur",
    skizze="Drachenviereck mit Eckpunkten L (linke Grundstücksseite, mittig), R (rechte Grundstücksseite, "
           "mittig), T und B (obere/untere Grundstücksseite, 8,5 m von R und je 7,5 m von der Mittellinie "
           "entfernt); Grundstück 30 m x 15 m als Rahmen",
    kontext="Bauwesen", textumfang="lang",
    gegeben="Grundstück 30 m x 15 m; die Diagonale des Drachenvierecks verläuft von Seitenmitte zu "
            "Seitenmitte (30 m lang), die andere Diagonale von Rand zu Rand (15 m lang) und schneidet die "
            "erste 8,5 m von der rechten Grundstücksseite entfernt; Bordsteine je 1 m Länge, Reststücke "
            "nicht weiterverwendbar",
    gesucht="Anzahl der benötigten Bordsteine",
    verfahren="rechte Seiten: √(8,5²+7,5²) ≈ 11,34 m, je aufgerundet 12 m → 2·12; linke Seiten: "
              "√(21,5²+7,5²) ≈ 22,77 m (21,5 = 30−8,5), je aufgerundet 23 m → 2·23",
    schritte="4", zahlenraum="Wurzel|dezimal", einheiten="m",
    ergebnis="70 Bordsteine", zwischenergebnis="rechte Seite ≈ 11,34 m, linke Seite ≈ 22,77 m",
    niveau_geschaetzt="III",
    fehlerquelle="den Gesamtumfang zuerst aufsummieren und erst danach einmal aufrunden, statt jede der vier "
                 "Seiten einzeln aufzurunden",
    bemerkung="Deutung der Skizze (Grundstück 30 m x 15 m aus der Einleitung als Rahmen; die beiden "
              "Diagonalen des Drachenvierecks reichen bis an die Grundstücksränder): 8,5 m/7,5 m sind laut "
              "der Bemaßungspfeile die waagerechte bzw. senkrechte Teilstrecke von der Spitze T zur Spitze R, "
              "nicht die vollen Diagonalen; daraus folgt die volle waagerechte Diagonale (30 m, "
              "Grundstückslänge) und die volle senkrechte Diagonale (15 m = 2·7,5 m, Grundstücksbreite). Die "
              "Rechnung 0,5·30·15=225 m² (Kontrollrechnung c) bestätigt runde 50 % Rasenanteil – starkes "
              "Indiz für diese Lesart.")

row(id="2017-GYM-K3c", block="Kontext", aufgabe="3", titel="Spielplatz", teilaufgabe="c", seite="7",
    punkte="3", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Flächeninhalt eines Drachenvierecks aus Diagonalen berechnen",
    typ_neben="Restfläche berechnen|Volumen Prisma berechnen",
    stichwoerter="Sandfläche|Rasenanteil|Kubikmeter Sand", format="Rechnung|Rechnung", operator="Bestimmen Sie|"
                                                                                                   "Berechnen Sie",
    antwort="Zahl|Zahl", material="Figur", skizze="dieselbe Skizze wie in b)", kontext="Bauwesen",
    textumfang="mittel",
    gegeben="Grundstück 30 m x 15 m; Diagonalen des Drachenvierecks 30 m und 15 m; Sand 0,5 m dick",
    gesucht="prozentualer Anteil der Rasenfläche am Spielplatz; Sandmenge in Kubikmetern",
    verfahren="Sandfläche = 0,5 · 30 · 15 = 225 m²; Grundstücksfläche = 30 · 15 = 450 m²; Rasenfläche = "
              "450−225 = 225 m², Anteil = 225:450; Sandvolumen = 225 m² · 0,5 m",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="m²|m³", abhaengig_von="2017-GYM-K3b",
    ergebnis="Rasenanteil = 50 %|Sandmenge = 112,5 m³", zwischenergebnis="Sandfläche = 225 m²",
    niveau_geschaetzt="III",
    fehlerquelle="beim Sandvolumen die Sandfläche mit der Grundstücksfläche statt mit der Drachenfläche "
                 "verwechseln")

row(id="2017-GYM-K3d", block="Kontext", aufgabe="3", titel="Spielplatz", teilaufgabe="d", seite="7",
    punkte="2", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Winkel eines Drachenvierecks aus Diagonalenabschnitten berechnen",
    stichwoerter="Winkel α|Tangens|Drachenviereck", format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur", skizze="dieselbe Skizze wie in b), Winkel α an der linken Spitze L", kontext="Bauwesen",
    textumfang="kurz",
    gegeben="rechtwinklige Teildreiecke an der linken Spitze L mit Katheten 21,5 m (waagerecht) und 7,5 m "
            "(senkrecht)",
    gesucht="Winkel α an der Spitze L", verfahren="halber Winkel: tan(α/2) = 7,5 : 21,5; α = 2 · arctan(7,5:21,5)",
    schritte="2", zahlenraum="dezimal", einheiten="m|Grad", abhaengig_von="2017-GYM-K3b",
    ergebnis="α ≈ 38,46°", niveau_geschaetzt="III",
    fehlerquelle="nur den halben Winkel berechnen und als Ergebnis für α angeben, ohne zu verdoppeln")

row(id="2017-GYM-K4a", block="Kontext", aufgabe="4", titel="Milchwerk", teilaufgabe="a", seite="8",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche", typ="Höhe eines Zylinders aus Volumen berechnen",
    stichwoerter="Zylinder|Speicher|Höhe", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Foto", skizze="keine", kontext="Industrie/Lebensmittel", textumfang="mittel",
    gegeben="drei baugleiche zylinderförmige Speicher, Gesamtkapazität 600 000 Liter, Durchmesser je 4 m",
    gesucht="Höhe eines Speichers",
    verfahren="V je Speicher = 600 000 : 3 = 200 000 l = 200 m³; h = V : (π·r²) = 200 : (π·2²)", schritte="3",
    zahlenraum="dezimal", einheiten="l|m³|m", ergebnis="h ≈ 15,92 m", zwischenergebnis="V je Speicher = 200 m³",
    niveau_geschaetzt="II", fehlerquelle="mit dem Durchmesser (4 m) statt dem Radius (2 m) in der Formel rechnen")

row(id="2017-GYM-K4b", block="Kontext", aufgabe="4", titel="Milchwerk", teilaufgabe="b", seite="8",
    punkte="2", leitidee="Größen und Messen", thema="Einheiten umrechnen", typ="Portionen aus Gesamtmenge berechnen",
    stichwoerter="Tankfahrzeug|Fahrten|Milchmenge", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Industrie/Lebensmittel", textumfang="kurz",
    gegeben="täglich 170 000 Liter Milch, ein Tankfahrzeug transportiert 25 000 Liter",
    gesucht="Anzahl der nötigen Fahrten", verfahren="170 000 : 25 000 = 6,8, aufgerundet", schritte="2",
    zahlenraum="dezimal|ganz", einheiten="l", ergebnis="7 Fahrten", niveau_geschaetzt="II",
    fehlerquelle="auf 6 Fahrten abrunden und damit die Liefermenge nicht vollständig anliefern")

row(id="2017-GYM-K4c", block="Kontext", aufgabe="4", titel="Milchwerk", teilaufgabe="c", seite="9",
    punkte="4", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Kantenlänge einer quadratischen Grundfläche aus Volumen berechnen", typ_neben="Grundwert berechnen",
    stichwoerter="Magerquarkbecher|Grundkante|Füllstand", format="Rechnung|Rechnung", operator="Berechnen Sie",
    antwort="Zahl|Zahl", material="keins", skizze="keine", kontext="Industrie/Lebensmittel", textumfang="lang",
    gegeben="500-Gramm-Becher (Quader, quadratische Grundfläche) bisher 5 cm hoch gefüllt; neuer Becher "
            "gleicher Form, 3 cm höher gefüllt; 100 g Magerquark = 100 cm³; neuer Becher bei 500 g zu 93 % "
            "gefüllt",
    gesucht="Grundkantenlänge des neuen Bechers; Gesamthöhe des neuen Bechers",
    verfahren="Füllvolumen konstant 500 cm³; neue Füllhöhe 5+3=8 cm; a² = 500:8, a=√62,5; Gesamthöhe: "
              "8 cm entsprechen 93 %, Gesamthöhe = 8 : 0,93",
    schritte="3", zahlenraum="Wurzel|dezimal|Prozent", einheiten="cm|cm³",
    ergebnis="Grundkante ≈ 7,91 cm|Gesamthöhe ≈ 8,60 cm", zwischenergebnis="alte Grundkante zur Kontrolle: "
             "a₁=√(500:5)=10 cm", niveau_geschaetzt="III",
    fehlerquelle="die neue Füllhöhe mit der alten Grundkante (10 cm) statt der neu berechneten verwechseln, "
                 "oder 93 % als Zuschlag statt als Anteil der Gesamthöhe verwenden")

row(id="2017-GYM-K5a", block="Kontext", aufgabe="5", titel="Studentenwohnung", teilaufgabe="a", seite="10",
    punkte="2", leitidee="Zahlen und Operationen", thema="Zinsrechnung", typ="Zinseszins Endkapital berechnen",
    stichwoerter="Mietsteigerung|Zinseszins|sechs Jahre", format="Begründung", operator="Zeigen Sie rechnerisch",
    antwort="Zahl", material="keins", skizze="keine", kontext="Wohnen/Miete", textumfang="mittel",
    gegeben="Anfangsmiete 310 €/Monat, jährliche Steigerung 1,1 %, Mietdauer 6 Jahre",
    gesucht="Nachweis, dass die Miete im letzten (6.) Mietjahr 327,43 € beträgt",
    verfahren="310 € · 1,011⁵ (fünf Steigerungen bis zum sechsten Jahr)", schritte="1", zahlenraum="dezimal|Prozent",
    einheiten="€", ergebnis="327,43 €", niveau_geschaetzt="III",
    fehlerquelle="mit 1,011⁶ (sechs statt fünf Steigerungen) rechnen und ein zu hohes Ergebnis erhalten")

row(id="2017-GYM-K5b", block="Kontext", aufgabe="5", titel="Studentenwohnung", teilaufgabe="b", seite="10",
    punkte="2", leitidee="Zahlen und Operationen", thema="Prozentrechnung", typ="Tarife vergleichen",
    stichwoerter="Stromtarif|Steuer|Vergleich", format="Begründung", operator="Prüfen Sie", antwort="Text",
    material="Tabelle", skizze="keine", kontext="Wohnen/Miete", textumfang="lang",
    gegeben="Jahresverbrauch 1000 kWh; Anbieter 1: 25,47 ct/kWh + 57 €/Jahr; Anbieter 2: 24,02 ct/kWh + "
            "81 €/Jahr; beide zzgl. 0,015 €/kWh Stromsteuer und 19 % Umsatzsteuer auf alle Beträge",
    gesucht="günstigeres Angebot",
    verfahren="Anbieter 1 netto: 1000·0,2697 €+57 €=326,70 €, brutto ·1,19=388,77 €; Anbieter 2 netto: "
              "1000·0,2552 €+81 €=336,20 €, brutto ·1,19=400,08 €",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="ct|€",
    ergebnis="Anbieter 1 ist günstiger (388,77 € gegen 400,08 € im Jahr)",
    zwischenergebnis="Anbieter 1 netto 326,70 €; Anbieter 2 netto 336,20 €", niveau_geschaetzt="III",
    fehlerquelle="die Umsatzsteuer nur auf den Arbeitspreis statt auf die Summe aus Arbeits-, Grundpreis und "
                 "Stromsteuer anwenden")

row(id="2017-GYM-K5c", block="Kontext", aufgabe="5", titel="Studentenwohnung", teilaufgabe="c", seite="11",
    punkte="4", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Wahrscheinlichkeit mehrstufig ohne Zurücklegen", typ_neben="Gleichverteilung der Trefferwahrscheinlichkeit "
                                                                       "begründen",
    stichwoerter="Schlüsselbund|ohne Zurücklegen|Symmetrie", format="Rechnung|Begründung",
    operator="Berechnen Sie|Vergleichen Sie", antwort="Zahl|Text", material="keins", skizze="keine",
    kontext="Wohnen/Miete", textumfang="mittel",
    gegeben="Schlüsselbund mit 7 Schlüsseln, nacheinander ausprobiert, genau einer passt",
    gesucht="Wahrscheinlichkeit, dass der zweite Schlüssel passt; Vergleich mit der Wahrscheinlichkeit für "
            "den ersten bzw. letzten Schlüssel",
    verfahren="P(2. passt) = (6/7)·(1/6) = 1/7; durch Symmetrie ist die Trefferwahrscheinlichkeit für jede "
              "Position gleich groß",
    schritte="2", zahlenraum="Bruch", ergebnis="P(2. Schlüssel) = 1/7|P(1. Schlüssel) = P(letzter Schlüssel) "
             "= 1/7, also gleich groß", niveau_geschaetzt="III",
    fehlerquelle="annehmen, der letzte Schlüssel habe eine höhere oder niedrigere Wahrscheinlichkeit als der "
                 "erste")

row(id="2017-GYM-K5d", block="Kontext", aufgabe="5", titel="Studentenwohnung", teilaufgabe="d", seite="11",
    punkte="2", leitidee="Daten und Zufall", thema="Zählen und Kombinatorik",
    typ="Anzahl Kombinationen nach dem Zählprinzip bestimmen",
    stichwoerter="Brötchen|Zählprinzip|Belag", format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Freizeit/Feier", textumfang="mittel",
    gegeben="helle oder dunkle Brötchen (2), Belag: 2 Käse- oder 4 Wurstsorten (6), zusätzlich Gurke oder "
            "Tomate (2)",
    gesucht="Anzahl möglicher belegter Brötchen", verfahren="2 · (2+4) · 2", schritte="1", zahlenraum="ganz",
    ergebnis="24", niveau_geschaetzt="II",
    fehlerquelle="Käse- und Wurstsorten multiplizieren statt zu addieren (Belag ist Käse ODER Wurst, nicht "
                 "beides)")

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
