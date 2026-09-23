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
    "jahr": "2019",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "",         # zweiteiliges Heft ab 2019, siehe "dateien"
    "dateien": ["19_P10_Ma_Gym_A_1.pdf", "19_P10_Ma_Gym_A_2.pdf"],
    "seiten": {"Basis": 3, "Kontext": 9},  # eigene Fußzeile je Teildatei (msa.md § 3)
    "soll": {"1": 10, "2": 10, "3": 12, "4": 10, "5": 8},
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
    ("Anteil einer unterteilten Kreisfläche bestimmen", "Zahlen und Operationen", "Brüche und Dezimalzahlen",
     "Den Anteil markierter Sektoren an einer in ungleiche Teile geteilten Kreisfläche bestimmen und als "
     "Bruch angeben (nicht die Anzahl der sichtbaren Sektoren zählen, sondern die tatsächlichen Winkel "
     "vergleichen).",
     "2019-GYM-B1c"),
    ("Binomische Formel anwenden", "Zahlen und Operationen", "Terme umformen",
     "Einen Term der Form (a±b)² oder (a+b)(a−b) mithilfe einer binomischen Formel ausmultiplizieren oder "
     "das Ergebnis unter mehreren Optionen auswählen.",
     "2019-GYM-B1f"),
    ("Trigonometrische Funktionsgleichung zu Graph zuordnen", "Gleichungen und Funktionen", "Trigonometrische Funktionen",
     "Zu einem abgebildeten Graphen einer trigonometrischen Funktion aus mehreren Gleichungen "
     "(unterschiedliche Amplitude, Streckung oder Verschiebung) die passende auswählen.",
     "2019-GYM-B1i"),
    ("Scheitelpunkt einer Parabel rechnerisch nachweisen", "Gleichungen und Funktionen", "Quadratische Funktionen",
     "Durch Einsetzen der Koordinaten in die Funktionsgleichung (oder über die Scheitelformel) nachweisen, "
     "dass ein gegebener Punkt der Scheitelpunkt einer Parabel ist.",
     "2019-GYM-K2a"),
    ("Schnittpunktgleichung zweier Parabeln herleiten", "Gleichungen und Funktionen", "Quadratische Funktionen",
     "Durch Gleichsetzen zweier Parabelgleichungen eine vorgegebene quadratische Gleichung herleiten und "
     "eine geeignete Lösungsmethode (z. B. pq-Formel) für die Schnittpunktberechnung erläutern.",
     "2019-GYM-K2b"),
    ("Flächeninhalt eines Dreiecks aus drei Seiten berechnen", "Raum und Form", "Ebene Figuren und Winkel",
     "Flächeninhalt eines Dreiecks aus den drei Seitenlängen mit der Heronschen Flächenformel berechnen.",
     "2019-GYM-K3a"),
    ("Körper im Schrägbild darstellen", "Raum und Form", "Körper, Netze, Schrägbilder",
     "Einen zusammengesetzten Körper (z. B. Turm aus Quader und Pyramide) in einem selbst gewählten Maßstab "
     "als Schrägbild darstellen.",
     "2019-GYM-K4a"),
    ("Mantelfläche einer Pyramide berechnen", "Größen und Messen", "Volumen und Oberfläche",
     "Mantelfläche einer quadratischen Pyramide aus der Grundkante und der über den Satz des Pythagoras "
     "ermittelten Seitenhöhe (Neigungshöhe der Dreiecksflächen) berechnen.",
     "2019-GYM-K4b"),
    ("Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen", "Daten und Zufall", "Zählen und Kombinatorik",
     "Anzahl der Möglichkeiten bestimmen, aus einer Gruppe eine bestimmte Anzahl von Elementen auszuwählen, "
     "wenn die Reihenfolge der Auswahl keine Rolle spielt (Kombination ohne Wiederholung).",
     "2019-GYM-K5b"),
    ("Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen", "Daten und Zufall", "Wahrscheinlichkeit mehrstufig",
     "Im mehrstufigen Baumdiagramm die Anzahl der Pfade zählen, die ein vorgegebenes Ereignis (z. B. "
     "mindestens k von n Erfolgen) erfüllen.",
     "2019-GYM-K5c"),
]

row(id="2019-GYM-B1a", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="a", seite="2",
    punkte="1", hilfsmittel="nein", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Winkel über Scheitel- oder Nebenwinkel bestimmen",
    stichwoerter="Scheitelwinkel|verlängerte Seite|überflüssige Angabe", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="Figur",
    skizze="Dreieck mit Winkel 65° an einer Spitze; die Grundseite und die gegenüberliegende Seite werden "
           "über die dritte Spitze hinaus gestrichelt verlängert; β liegt zwischen Grundseite und der "
           "verlängerten Seite (innen), 35° liegt als Scheitelwinkel zu β zwischen den beiden Verlängerungen",
    kontext="ohne", textumfang="kurz",
    gegeben="Dreieck mit einem Winkel von 65° an einer Spitze; an einer anderen Spitze sind beide Seiten "
            "über die Spitze hinaus verlängert, der von den Verlängerungen eingeschlossene Winkel beträgt 35°",
    gesucht="Winkel β (Innenwinkel an dieser Spitze)",
    verfahren="β und 35° sind Scheitelwinkel an der verlängerten Spitze, also gleich groß; die 65°-Angabe "
              "wird dafür nicht benötigt",
    schritte="1", zahlenraum="ganz", einheiten="Grad", ergebnis="β = 35°", niveau_geschaetzt="II",
    fehlerquelle="mit dem Winkelsummensatz und der überflüssigen 65°-Angabe rechnen, statt den Scheitelwinkel "
                 "direkt zu erkennen")

row(id="2019-GYM-B1b", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="b", seite="2",
    punkte="1", hilfsmittel="nein", leitidee="Größen und Messen", thema="Einheiten umrechnen", typ="Größen vergleichen",
    stichwoerter="Meter|Zentimeter|Vergleich", format="Eintragen", operator="Setzen Sie ein", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="0,06 m und 60 cm", gesucht="richtiges Vergleichszeichen", verfahren="0,06 m = 6 cm; 6 cm < 60 cm",
    schritte="1", zahlenraum="dezimal", einheiten="m|cm", ergebnis="0,06 m < 60 cm", niveau_geschaetzt="I",
    fehlerquelle="0,06 mit 60 direkt vergleichen, ohne beide Werte in dieselbe Einheit zu bringen")

row(id="2019-GYM-B1c", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="c", seite="2",
    punkte="1", hilfsmittel="nein", leitidee="Zahlen und Operationen", thema="Brüche und Dezimalzahlen",
    typ="Anteil einer unterteilten Kreisfläche bestimmen",
    stichwoerter="Kreis|Sektoren|Anteil", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="Figur", skizze="Kreis mit sechs Radien in ungleichen Abständen, zwei nicht benachbarte Sektoren "
                             "markiert (ein größerer oben, ein kleinerer unten rechts)", kontext="ohne",
    textumfang="kurz", gegeben="Kreis mit zwei markierten Sektoren unterschiedlicher Größe; Auswahl 3/7, "
                               "3/5, 1/4, 5/7",
    gesucht="Anteil der markierten Fläche an der Gesamtfläche",
    verfahren="Winkel der markierten Sektoren schätzen und zur Vollwinkelsumme 360° ins Verhältnis setzen "
              "(nicht die Anzahl der sechs sichtbaren Sektoren als gleich groß annehmen)",
    schritte="1", zahlenraum="Bruch", ergebnis="1/4?", niveau_geschaetzt="II",
    fehlerquelle="die zwei markierten von sechs sichtbaren, aber ungleich großen Sektoren als 2/6=1/3 zählen",
    bemerkung="Ergebnis unsicher: Die Sektoren sind in der Vektorgrafik ungleich groß; aus den "
              "Randpunkt-Koordinaten grob vermessen ergeben sich Sektorwinkel von ca. 57° und 29° (Summe "
              "ca. 86°) – deutlich näher an 90° (1/4) als an den übrigen Antwortoptionen, aber nur "
              "überschlägig (aus Pixelkoordinaten der Randpunkte, keine exakten Vektordaten) bestimmt.")

row(id="2019-GYM-B1d", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="d", seite="2",
    punkte="1", hilfsmittel="nein", leitidee="Zahlen und Operationen", thema="Rationale Zahlen rechnen", typ="Termwert berechnen",
    stichwoerter="Termwert|Bruchterm|negative Zahlen", format="Kurzantwort", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Term (a−b):(2a+b) mit a=4, b=−3", gesucht="Wert des Terms",
    verfahren="(4−(−3)) : (2·4+(−3)) = 7 : 5", schritte="1", zahlenraum="negativ|Bruch", ergebnis="7/5 = 1,4",
    niveau_geschaetzt="II", fehlerquelle="Vorzeichenfehler bei b=−3 im Zähler oder Nenner")

row(id="2019-GYM-B1e", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="e", seite="2",
    punkte="1", hilfsmittel="nein", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang", typ="Term zu Figur angeben",
    stichwoerter="Rechteck|zusammengesetzt|Flächenterm", format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Figur", skizze="Rechteck aus zwei nebeneinanderliegenden Teilrechtecken der Breiten a und b, "
                             "gemeinsame Höhe c", kontext="ohne", textumfang="kurz",
    gegeben="zusammengesetztes Rechteck mit Breiten a und b nebeneinander, Höhe c",
    gesucht="Gleichung für den Flächeninhalt der gesamten Fläche", verfahren="Höhe mal Summe der Breiten",
    schritte="1", ergebnis="A = c · (a + b)", niveau_geschaetzt="I",
    fehlerquelle="nur eines der beiden Teilrechtecke (a·c oder b·c) angeben")

row(id="2019-GYM-B1f", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="f", seite="2",
    punkte="1", hilfsmittel="nein", leitidee="Zahlen und Operationen", thema="Terme umformen", typ="Binomische Formel anwenden",
    stichwoerter="binomische Formel|Klammer auflösen", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Term (2a−b)²; Auswahl 2a²+4ab−b², 4a²−4ab+b², 2a²−2ab+b², 4a−2ab+b²",
    gesucht="Term nach Auflösen der Klammer", verfahren="zweite binomische Formel: (2a−b)² = (2a)²−2·2a·b+b²",
    schritte="1", ergebnis="4a² − 4ab + b²", niveau_geschaetzt="II",
    fehlerquelle="das mittlere Glied nicht verdoppeln (2a²−2ab+b² wählen)")

row(id="2019-GYM-B1g", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="g", seite="3",
    punkte="1", hilfsmittel="nein", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit einstufig",
    typ="Zufallsgerät zu Wahrscheinlichkeit entwerfen",
    stichwoerter="Baumdiagramm|Gefäß|Kugeln ergänzen", format="Eintragen", operator="Ergänzen Sie", antwort="Grafik",
    material="Figur", skizze="Baumdiagramm mit einer Stufe: Ast „weiß“ mit 2/3, Ast „schwarz“ mit 1/3; "
                             "darunter ein zylindrisches Gefäß mit vier vorgezeichneten unausgefüllten "
                             "(weißen) Kreisen, zu ergänzen um schwarze Kugeln",
    kontext="Glücksspiel", textumfang="mittel",
    gegeben="einstufiges Baumdiagramm mit P(weiß)=2/3, P(schwarz)=1/3; vier weiße Kugeln bereits im Gefäß "
            "eingezeichnet",
    gesucht="Ergänzung des Gefäßes um die passende Anzahl schwarzer Kugeln",
    verfahren="4 weiße Kugeln sollen 2/3 des Inhalts sein: Gesamtzahl = 4 : (2/3) = 6, also 2 schwarze Kugeln "
              "ergänzen (4 : 2 = 2/3 : 1/3)",
    schritte="2", zahlenraum="Bruch", ergebnis="2 schwarze Kugeln ergänzt (insgesamt 4 weiße und 2 schwarze)",
    niveau_geschaetzt="III",
    fehlerquelle="eine beliebige Anzahl schwarzer Kugeln ergänzen, ohne das Verhältnis 2:1 zu den vier "
                 "vorgegebenen weißen Kugeln zu prüfen")

row(id="2019-GYM-B1h", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="h", seite="3",
    punkte="1", hilfsmittel="nein", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Winkelfunktion Seitenverhältnis angeben",
    stichwoerter="rechtwinkliges Dreieck|trigonometrische Beziehung", format="Kurzantwort", operator="Geben Sie an",
    antwort="Term", material="Figur",
    skizze="Dreieck mit rechtem Winkel oben (markiert mit Punkt) zwischen den Seiten s und r, Winkel α unten "
           "links zwischen s und t, Seite t unten (Hypotenuse)",
    kontext="ohne", textumfang="kurz",
    gegeben="rechtwinkliges Dreieck mit Katheten s, r und Hypotenuse t, rechter Winkel gegenüber t, Winkel α "
            "zwischen s und t",
    gesucht="eine trigonometrische Beziehung für α", verfahren="Gegenkathete r, Ankathete s, Hypotenuse t: "
                                                              "tan α = r/s (auch sin α = r/t oder cos α = s/t "
                                                              "richtig)",
    schritte="1", ergebnis="tan α = r/s", niveau_geschaetzt="II",
    fehlerquelle="Gegenkathete und Ankathete vertauschen")

row(id="2019-GYM-B1i", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="i", seite="3",
    punkte="1", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Trigonometrische Funktionen",
    typ="Trigonometrische Funktionsgleichung zu Graph zuordnen",
    stichwoerter="Sinusfunktion|Amplitude|Verschiebung", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="Koordinatensystem",
    skizze="periodischer Graph zwischen −2π und 2π, Wertebereich −3 bis 1, zwei volle Perioden im "
           "dargestellten Bereich (Periode 2π)",
    kontext="ohne", textumfang="kurz",
    gegeben="Graph einer trigonometrischen Funktion; Auswahl f(x)=1·sin(x)−1, f(x)=2·sin(x)−1, "
            "f(x)=−3·sin(2x)−1, f(x)=2·sin(2x−1)",
    gesucht="passende Funktionsgleichung",
    verfahren="Wertebereich [−3;1] → Amplitude 2, Verschiebung −1; zwei volle Perioden auf [−2π;2π] → "
              "Periode 2π, also Faktor 1 vor x",
    schritte="2", ergebnis="f(x) = 2 sin(x) − 1", niveau_geschaetzt="III",
    fehlerquelle="aus der Kurvenform vorschnell auf eine doppelte Frequenz (sin(2x)) schließen")

row(id="2019-GYM-B1j", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="j", seite="3",
    punkte="1", hilfsmittel="nein", leitidee="Zahlen und Operationen", thema="Zehnerpotenzen und Näherungswerte",
    typ="Zehnerpotenzschreibweise umwandeln",
    stichwoerter="Zehnerpotenz|negativer Exponent", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="2,1 · 10⁻⁴", gesucht="Zahl ohne Zehnerpotenz", verfahren="Komma um 4 Stellen nach links",
    schritte="1", zahlenraum="dezimal", ergebnis="0,00021", niveau_geschaetzt="I",
    fehlerquelle="Komma um 4 Stellen nach rechts statt nach links verschieben (negativer Exponent)")

row(id="2019-GYM-K2a", block="Kontext", aufgabe="2", titel="Quadratische Funktionen", teilaufgabe="a", seite="2",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Scheitelpunkt einer Parabel rechnerisch nachweisen", typ_neben="Parabel aus Gleichung skizzieren",
    stichwoerter="Scheitelpunkt|Nachweis|Parabel zeichnen", format="Begründung|Zeichnen", operator="Zeigen Sie|"
                                                                                                    "Zeichnen Sie",
    antwort="Zahl|Grafik", material="Koordinatensystem",
    skizze="Koordinatensystem x von −1 bis 8, y von −5 bis 7; Parabel f mindestens im Intervall 1≤x≤6 "
           "einzeichnen, Scheitel bei (3,5|5)",
    kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −x² + 7x − 7,25, x ∈ ℝ; Punkt S(3,5|5)",
    gesucht="Nachweis, dass S Scheitelpunkt von f ist; Graph von f im Intervall 1≤x≤6",
    verfahren="f(3,5) = −12,25+24,5−7,25 = 5 = y-Koordinate von S; alternativ Scheitel-x über −b:(2a) = "
              "3,5 nachweisen",
    schritte="1", zahlenraum="dezimal", ergebnis="f(3,5) = 5, also ist S(3,5|5) der Scheitelpunkt",
    niveau_geschaetzt="II", fehlerquelle="nur den x-Wert über −b:(2a) prüfen und den y-Wert nicht durch "
                                         "Einsetzen bestätigen")

row(id="2019-GYM-K2b", block="Kontext", aufgabe="2", titel="Quadratische Funktionen", teilaufgabe="b", seite="3",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Schnittpunktgleichung zweier Parabeln herleiten",
    stichwoerter="Gleichsetzen|Schnittpunkte|pq-Formel", format="Begründung|Begründung", operator="Zeigen Sie|"
                                                                                                    "Erläutern Sie",
    antwort="Text|Text", material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −x² + 7x − 7,25; h(x) = x² − 3x − 2,75", gesucht="Nachweis, dass Gleichsetzen 0 = x²−5x+2,25 "
                                                                    "ergibt; geeignete Vorgehensweise für die "
                                                                    "Schnittpunktberechnung",
    verfahren="h(x)−f(x) = 2x²−10x+4,5, geteilt durch 2 ergibt x²−5x+2,25 = 0; Lösung z. B. über die "
              "pq-Formel mit p=−5, q=2,25",
    schritte="2", zahlenraum="dezimal", abhaengig_von="2019-GYM-K2a",
    ergebnis="0 = x²−5x+2,25 bestätigt|pq-Formel anwenden: x = 2,5 ± √(2,5²−2,25) = 2,5 ± 2",
    zwischenergebnis="Schnittstellen x=0,5 und x=4,5", niveau_geschaetzt="III",
    fehlerquelle="f(x) und h(x) beim Gleichsetzen vertauschen und dadurch das falsche Vorzeichen der "
                 "Gleichung erhalten")

row(id="2019-GYM-K2c", block="Kontext", aufgabe="2", titel="Quadratische Funktionen", teilaufgabe="c", seite="3",
    punkte="2", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Flächeninhalt eines Dreiecks aus Koordinaten berechnen",
    stichwoerter="Dreiecksfläche|Koordinaten|Ursprung", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="Dreieck aus O(0|0), P(6,5|−4) und Q(0,5|f(0,5))", kontext="ohne",
    textumfang="kurz", gegeben="P(6,5|−4), Koordinatenursprung O, Q(0,5|f(0,5)) mit f aus a)",
    gesucht="Flächeninhalt des Dreiecks OPQ",
    verfahren="f(0,5) = −0,25+3,5−7,25 = −4, also Q(0,5|−4); PQ ist waagerecht mit Länge 6,5−0,5=6, Höhe von "
              "O zu dieser Geraden ist 4; A = 0,5·6·4",
    schritte="3", zahlenraum="dezimal", einheiten="LE²", abhaengig_von="2019-GYM-K2a", ergebnis="A = 12 LE²",
    zwischenergebnis="Q(0,5|−4)", niveau_geschaetzt="III",
    fehlerquelle="nicht erkennen, dass P und Q dieselbe y-Koordinate haben, und die Grundseite/Höhe falsch "
                 "wählen")

row(id="2019-GYM-K3a", block="Kontext", aufgabe="3", titel="Sonnensegel", teilaufgabe="a", seite="4",
    punkte="5", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Flächeninhalt eines Dreiecks aus drei Seiten berechnen", typ_neben="Kosten aus Menge und Preis berechnen",
    stichwoerter="Sonnensegel|Heron|Dreiecksfläche", format="Rechnung|Rechnung", operator="Berechnen Sie|"
                                                                                            "Geben Sie an",
    antwort="Zahl|Zahl", material="Figur", skizze="dreieckiges Sonnensegel mit Seiten 5 m, 4,5 m, 3,5 m "
                                                   "zwischen drei Pfeilern", kontext="Garten/Bauen",
    textumfang="mittel",
    gegeben="dreieckiges Sonnensegel mit Seiten 5 m, 4,5 m, 3,5 m; Preis 19,90 €/m²",
    gesucht="Fläche des Sonnensegels; Preis für das neue Sonnensegel",
    verfahren="Heron: s=(5+4,5+3,5):2=6,5; A=√(6,5·1,5·2·3); Preis = A · 19,90 €", schritte="3",
    zahlenraum="Wurzel|dezimal", einheiten="m|m²|€", ergebnis="A ≈ 7,65 m²|Preis ≈ 152,21 €",
    niveau_geschaetzt="III",
    fehlerquelle="die Fläche über Grundseite mal Höhe schätzen, ohne die Höhe zu kennen, statt die "
                 "Heronsche Formel zu nutzen")

row(id="2019-GYM-K3b", block="Kontext", aufgabe="3", titel="Sonnensegel", teilaufgabe="b", seite="5",
    punkte="4", leitidee="Größen und Messen", thema="Satz des Pythagoras", typ="Pythagoras Hypotenuse",
    typ_neben="Größen vergleichen",
    stichwoerter="Spannseil|Pythagoras|Zuschlag", format="Begründung", operator="Prüfen Sie rechnerisch",
    antwort="Text", material="Figur", skizze="Pfeiler mit Spannseil vom Punkt 2,50 m Höhe zu einem 1,50 m "
                                             "vom Pfeiler entfernten Bodenpunkt", kontext="Garten/Bauen",
    textumfang="mittel",
    gegeben="Seilbefestigung 2,50 m Höhe am Pfeiler, 1,50 m Abstand am Boden, je 25 cm Zuschlag an beiden "
            "Enden; vorhandenes Seil 3,20 m",
    gesucht="Prüfung, ob das vorhandene Seil ausreicht",
    verfahren="benötigte Seillänge = √(2,50²+1,50²) + 2·0,25 = √8,5 + 0,5", schritte="2", zahlenraum="Wurzel|dezimal",
    einheiten="m", ergebnis="benötigt ≈ 3,42 m > vorhandene 3,20 m, das Seil reicht nicht",
    zwischenergebnis="Pythagoras-Strecke ≈ 2,92 m", niveau_geschaetzt="III",
    fehlerquelle="den Zuschlag von 25 cm je Ende vergessen oder nur einmal statt zweimal addieren")

row(id="2019-GYM-K3c", block="Kontext", aufgabe="3", titel="Sonnensegel", teilaufgabe="c", seite="5",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche", typ="Höhe eines Zylinders aus Volumen berechnen",
    stichwoerter="Planschbecken|Wasserstand|Zylinder", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Garten/Freizeit", textumfang="mittel",
    gegeben="zylinderförmiges Planschbecken, Innendurchmesser 1,20 m; eingefüllt 10 Eimer à 5 l und 5 Kannen "
            "à 2 l",
    gesucht="Wasserstand im Becken",
    verfahren="Wassermenge = 10·5+5·2 = 60 l = 60 000 cm³; h = V : (π·r²) mit r=60 cm", schritte="3",
    zahlenraum="dezimal", einheiten="l|cm³|cm", ergebnis="h ≈ 5,31 cm", zwischenergebnis="V = 60 000 cm³",
    niveau_geschaetzt="II", fehlerquelle="mit dem Durchmesser (120 cm) statt dem Radius (60 cm) rechnen")

row(id="2019-GYM-K4a", block="Kontext", aufgabe="4", titel="Turm", teilaufgabe="a", seite="6",
    punkte="4", leitidee="Raum und Form", thema="Körper, Netze, Schrägbilder", typ="Körper im Schrägbild darstellen",
    stichwoerter="Turm|Schrägbild|Maßstab", format="Zeichnen|Kurzantwort", operator="Stellen Sie dar|Geben Sie an",
    antwort="Grafik|Text", material="Figur",
    skizze="Turm als Schrägbild: Quader mit quadratischer Grundfläche (Kante 4 m, Höhe 10 m) und "
           "aufgesetzter quadratischer Pyramide (Dach) darstellen, Fenster unberücksichtigt",
    kontext="Bauwesen", textumfang="mittel",
    gegeben="13 m hoher Turm: Quader mit quadratischer Grundfläche 4 m, Höhe des Quaders 10 m, "
            "pyramidenförmiges Dach (Resthöhe 3 m)",
    gesucht="Schrägbild des Turms mit angegebenem Maßstab",
    verfahren="Quader und aufgesetzte Pyramide in einem einheitlichen, selbst gewählten Maßstab (z. B. "
              "1:100) zeichnen", schritte="1", zahlenraum="ganz", einheiten="m",
    ergebnis="Schrägbild aus Quader (4 m x 4 m x 10 m) und Pyramide (Höhe 3 m), Maßstab z. B. 1:100",
    niveau_geschaetzt="II", fehlerquelle="Quader und Pyramide in unterschiedlichen Maßstäben zeichnen")

row(id="2019-GYM-K4b", block="Kontext", aufgabe="4", titel="Turm", teilaufgabe="b", seite="7",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche", typ="Mantelfläche einer Pyramide berechnen",
    stichwoerter="Pyramide|Dachfläche|Seitenhöhe", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze="dieselbe Turmskizze wie in a)", kontext="Bauwesen", textumfang="kurz",
    gegeben="quadratische Pyramide (Dach) mit Grundkante 4 m und Höhe 3 m", gesucht="Größe der Dachfläche "
                                                                                  "(Mantelfläche)",
    verfahren="Seitenhöhe (Neigungshöhe) h_s = √(3²+2²) = √13; Mantelfläche = 4 · 0,5 · 4 · h_s",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="m|m²", abhaengig_von="2019-GYM-K4a",
    ergebnis="≈ 28,84 m²", zwischenergebnis="Seitenhöhe ≈ 3,61 m", niveau_geschaetzt="III",
    fehlerquelle="die Pyramidenhöhe (3 m) statt der Seitenhöhe (√13 m) für die Dreiecksflächen verwenden")

row(id="2019-GYM-K4c", block="Kontext", aufgabe="4", titel="Turm", teilaufgabe="c", seite="7",
    punkte="3", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang", typ="Restfläche berechnen",
    typ_neben="Größen vergleichen",
    stichwoerter="Anstrichfläche|Fenster|Farbe reicht", format="Begründung", operator="Prüfen Sie", antwort="Text",
    material="Figur", skizze="dieselbe Turmskizze wie in a), oberer Wandbereich von 6 m bis 10 m Höhe mit "
                             "vier kreisförmigen Fenstern", kontext="Bauwesen", textumfang="mittel",
    gegeben="Turm mit quadratischer Grundfläche (Kante 4 m); der Bereich von 6 m bis 10 m Höhe soll "
            "gestrichen werden, vier kreisförmige Fenster mit Durchmesser 1,50 m; vorhandene Farbe für 60 m²",
    gesucht="Prüfung, ob die Farbe für die zu streichende Fläche reicht",
    verfahren="Wandfläche = Umfang(4·4 m) · Höhe(4 m) = 64 m²; Fensterfläche = 4·π·0,75² ≈ 7,07 m²; "
              "zu streichende Fläche = 64 − 7,07",
    schritte="3", zahlenraum="dezimal", einheiten="m|m²", ergebnis="zu streichende Fläche ≈ 56,93 m² < "
                                                                   "60 m² vorhandene Farbe, die Farbe reicht",
    zwischenergebnis="Wandfläche 64 m², Fensterfläche ≈ 7,07 m²", niveau_geschaetzt="III",
    fehlerquelle="die Fensterflächen nicht von der Wandfläche abziehen")

row(id="2019-GYM-K5a", block="Kontext", aufgabe="5", titel="Tag der Verkehrserziehung", teilaufgabe="a", seite="8",
    punkte="3", leitidee="Daten und Zufall", thema="Daten darstellen", typ="Kreisdiagramm zeichnen",
    stichwoerter="Verkehrsmittel|Kreisdiagramm|Umfrage", format="Zeichnen", operator="Fertigen Sie an", antwort="Grafik",
    material="Tabelle", skizze="leerer Kreis zum Eintragen der drei Sektoren Bus, Fahrrad, zu Fuß",
    kontext="Schule/Verkehr", textumfang="mittel",
    gegeben="Klasse 10a: 15 Bus, 5 Fahrrad, 7 zu Fuß (27 Schüler insgesamt)",
    gesucht="Kreisdiagramm der Verkehrsmittelwahl",
    verfahren="Mittelpunktswinkel je Kategorie: Bus 15:27·360°, Fahrrad 5:27·360°, zu Fuß 7:27·360°",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="Grad",
    ergebnis="Bus ≈ 200°, Fahrrad ≈ 66,7°, zu Fuß ≈ 93,3°", niveau_geschaetzt="II",
    fehlerquelle="die Winkel auf 100 Schüler statt auf die tatsächliche Gesamtzahl 27 beziehen")

row(id="2019-GYM-K5b", block="Kontext", aufgabe="5", titel="Tag der Verkehrserziehung", teilaufgabe="b", seite="9",
    punkte="1", leitidee="Daten und Zufall", thema="Zählen und Kombinatorik",
    typ="Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen",
    stichwoerter="Auswahl|Kombination|Fahrradkontrolle", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Schule/Verkehr", textumfang="kurz",
    gegeben="5 Fahrradfahrer der Klasse 10a, 3 werden zufällig für eine Kontrolle ausgewählt",
    gesucht="Anzahl der Auswahlmöglichkeiten", verfahren="Kombination ohne Wiederholung: C(5,3) = 5!:(3!·2!)",
    schritte="1", zahlenraum="ganz", ergebnis="10", niveau_geschaetzt="II",
    fehlerquelle="die Reihenfolge der Auswahl mitzählen und mit der Anordnungszahl (5·4·3=60) statt der "
                 "Kombination rechnen")

row(id="2019-GYM-K5c", block="Kontext", aufgabe="5", titel="Tag der Verkehrserziehung", teilaufgabe="c", seite="9",
    punkte="4", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen",
    typ_neben="Wahrscheinlichkeit mehrstufig unabhängig|Ereignis zu Wahrscheinlichkeitsterm beschreiben",
    stichwoerter="Baumdiagramm|Fahrradkontrolle|mindestens zwei", format="Kurzantwort|Rechnung|Begründung",
    operator="Geben Sie an|Berechnen Sie|Beschreiben Sie", antwort="Zahl|Zahl|Text", material="Figur",
    skizze="dreistufiges Baumdiagramm Licht(L)/Reifen(R)/Bremsen(B), je Stufe bestanden(+)/nicht "
           "bestanden(−): P(L+)=0,87, P(R+|L+)=0,85, P(R+|L−)=0,85, P(B+)=0,9 an jedem Endast",
    kontext="Schule/Verkehr", textumfang="lang",
    gegeben="Baumdiagramm mit drei Stufen (Licht, Reifen, Bremsen), P(L+)=0,87, P(R+)=0,85, P(B+)=0,9 an "
            "jeder Verzweigung",
    gesucht="Anzahl der Pfade für „mindestens zwei Kontrollen bestanden“; Wahrscheinlichkeit, dass alle drei "
            "Kontrollen bestanden wurden; Beschreibung des Ereignisses zu "
            "P(A)=0,13·0,85·0,9+0,87·0,15·0,9+0,87·0,85·0,1",
    verfahren="von 8 Pfaden erfüllen 4 „mindestens zwei von drei +“ (+++ sowie die drei Pfade mit genau "
              "einem −); P(+++) = 0,87·0,85·0,9; die drei Summanden von P(A) sind jeweils genau ein − an "
              "einer der drei Stufen, die anderen beiden +",
    schritte="3", zahlenraum="dezimal", ergebnis="4 Pfade|P(+++) = 0,66555|A: „Genau zwei der drei "
             "Kontrollen wurden bestanden“", niveau_geschaetzt="III",
    fehlerquelle="bei der Pfadzählung auch „genau ein + \" oder „kein +\" Pfade mitzählen")
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
