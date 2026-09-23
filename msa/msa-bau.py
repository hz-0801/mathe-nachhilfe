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
    "jahr": "2021",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "",         # zweiteiliges Heft ab 2019, siehe "dateien"
    "dateien": ["21_P10_Ma_Gym_A1.pdf", "21_P10_Ma_Gym_A2.pdf"],
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
    ("Aussage über eine mehrfach gebrochene Streckenteilung prüfen", "Zahlen und Operationen",
     "Rationale Zahlen rechnen",
     "Eine Aussage über das schrittweise Zurücklegen von Bruchteilen einer Gesamtstrecke (z. B. zuerst "
     "ein Drittel, dann ein Viertel des Rests) durch Nachrechnen als wahr oder falsch prüfen.",
     "2021-GYM-B1b"),
    ("Trapezfläche im Koordinatensystem aus Funktionsgraph und Geraden berechnen", "Raum und Form",
     "Ebene Figuren und Winkel",
     "Flächeninhalt eines von beiden Koordinatenachsen, einer Geraden und einer Parallelen zur y-Achse "
     "begrenzten Trapezes berechnen, dessen parallele Seiten die y-Achsenabschnitte zweier Punkte sind.",
     "2021-GYM-K3c"),
    ("Vieleck aus Seiten und Winkeln im Maßstab konstruieren", "Raum und Form", "Kongruenz und Konstruktion",
     "Ein Vieleck aus einer Folge gegebener Seitenlängen und eingeschlossener Winkel im vorgegebenen "
     "Maßstab konstruieren.",
     "2021-GYM-K4a"),
    ("Flächenberechnung eines Vielecks anhand einer vorgegebenen Gleichung erläutern", "Raum und Form",
     "Ebene Figuren und Winkel",
     "Eine vorgegebene Gleichung zur Flächenberechnung eines zusammengesetzten Vielecks als Summe eines "
     "Rechtecks und eines über den Satz des Pythagoras bestimmten Dreiecks erläutern.",
     "2021-GYM-K4d"),
    ("Formel für die Tiefe eines Kegels aus Durchmesser und Öffnungswinkel herleiten", "Größen und Messen",
     "Trigonometrie im rechtwinkligen Dreieck",
     "Eine Formel für die Tiefe eines kegelförmigen Gefäßes aus dem oberen Durchmesser und dem "
     "Öffnungswinkel über ein rechtwinkliges Teildreieck (halber Durchmesser, halber Öffnungswinkel) "
     "herleiten und begründen.",
     "2021-GYM-K5a"),
    ("Länge auf der Mantellinie eines Kegels bei Teilfüllung über Ähnlichkeit bestimmen", "Raum und Form",
     "Ähnlichkeit und Strahlensätze",
     "Bei teilweiser Füllung eines kegelförmigen Gefäßes die Lage einer Füllstandsmarkierung entlang der "
     "Mantellinie aus der Füllhöhe über die Ähnlichkeit von großem und kleinem Kegel bestimmen.",
     "2021-GYM-K5b"),
]

row(id="2021-GYM-B1a", block="Basis", aufgabe="1", titel="", teilaufgabe="a", seite="2",
    punkte="2", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Lineare Gleichungen",
    typ="Lineare Gleichung lösen",
    stichwoerter="Klammer|Gleichung|lösen", format="Rechnung", operator="Lösen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Gleichung 2x + 4·(−5 − 3x) = −(x + 2)",
    gesucht="Lösung x",
    verfahren="Klammern auflösen: 2x − 20 − 12x = −x − 2; zusammenfassen: −10x − 20 = −x − 2; nach x "
              "auflösen", schritte="3", zahlenraum="negativ", ergebnis="x = −2", niveau_geschaetzt="II",
    fehlerquelle="beim Ausmultiplizieren von 4·(−5 − 3x) ein Vorzeichen vergessen")

row(id="2021-GYM-B1b", block="Basis", aufgabe="1", titel="", teilaufgabe="b", seite="2",
    punkte="3", hilfsmittel="nein", leitidee="Zahlen und Operationen", thema="Rationale Zahlen rechnen",
    typ="Aussage über eine mehrfach gebrochene Streckenteilung prüfen",
    stichwoerter="Radtour|Bruchteil vom Rest|Aussage prüfen", format="Begründung", operator="Überprüfen Sie",
    antwort="Text", material="keins", skizze="keine", kontext="Freizeit/Sport", textumfang="mittel",
    gegeben="Radtour von 60 km Länge; Aussage: nach einem Drittel der Strecke Pause, danach nur noch ein "
            "Viertel vom Rest fahren, dann sei bereits die Hälfte der Gesamtstrecke geschafft",
    gesucht="Wahrheitsgehalt der Aussage",
    verfahren="ein Drittel von 60 km = 20 km; Rest = 40 km; ein Viertel vom Rest = 10 km; insgesamt "
              "20 km + 10 km = 30 km; die Hälfte von 60 km ist ebenfalls 30 km", schritte="3",
    zahlenraum="Bruch", einheiten="km", ergebnis="Aussage ist richtig: 20 km + 10 km = 30 km = die Hälfte "
             "von 60 km", niveau_geschaetzt="II",
    fehlerquelle="„ein Viertel vom Rest“ fälschlich als ein Viertel der Gesamtstrecke (15 km) rechnen")

row(id="2021-GYM-B2a", block="Basis", aufgabe="2", titel="", teilaufgabe="a", seite="3",
    punkte="2", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Geradengleichung aus Steigung und Punkt bestimmen",
    stichwoerter="Anstieg|Punkt|Geradengleichung", format="Rechnung", operator="Bestimmen Sie",
    antwort="Term", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Gerade g mit Anstieg m = −2 durch den Punkt P(3|−4)",
    gesucht="Gleichung der Geraden g",
    verfahren="−4 = −2·3 + n auflösen: n = 2", schritte="1", zahlenraum="negativ",
    ergebnis="g(x) = −2x + 2", niveau_geschaetzt="II",
    fehlerquelle="das Vorzeichen von P beim Einsetzen vertauschen")

row(id="2021-GYM-B2b", block="Basis", aufgabe="2", titel="", teilaufgabe="b", seite="3",
    punkte="3", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Lage zweier Geraden bestimmen",
    stichwoerter="Schnittpunkt|Anstieg vergleichen|Aussage beurteilen", format="Begründung",
    operator="Beurteilen Sie", antwort="Text", material="keins", skizze="keine", kontext="ohne",
    textumfang="kurz", abhaengig_von="2021-GYM-B2a",
    gegeben="Gerade g(x) = −2x + 2 (aus Teilaufgabe a); Gerade h mit h(x) = 5x − 12; Aussage: h schneidet "
            "g in genau einem Punkt",
    gesucht="Wahrheitsgehalt der Aussage",
    verfahren="g und h haben unterschiedliche Anstiege (−2 ≠ 5), also sind sie weder parallel noch "
              "identisch und schneiden sich in genau einem Punkt; Kontrolle durch Gleichsetzen: "
              "−2x + 2 = 5x − 12 liefert x = 2, y = −2", schritte="2", zahlenraum="negativ",
    ergebnis="Aussage ist richtig, Schnittpunkt (2|−2)", niveau_geschaetzt="II",
    fehlerquelle="ohne Vergleich der Anstiege direkt und unbegründet zustimmen oder widersprechen")

row(id="2021-GYM-K3a", block="Kontext", aufgabe="3", titel="Funktionen", teilaufgabe="a", seite="2",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Wertetabelle als Punkte darstellen",
    stichwoerter="Exponentialfunktion|Wertetabelle|Graph zeichnen", format="Zeichnen",
    operator="Zeichnen Sie", antwort="Grafik", material="Tabelle|Koordinatensystem",
    skizze="Koordinatensystem 0 bis 7 (y) und −2 bis 2,5 (x), Wertetabelle mit f(−2)=1/18, f(−1)=1/6, "
           "f(0)=0,5, f(1)=1,5, f(2)=4,5", kontext="ohne", textumfang="kurz",
    gegeben="Funktion f der Form f(x) = 0,5 · a^x mit Wertetabelle für x = −2 bis 2",
    gesucht="Graph von f mindestens im Intervall −1 ≤ x ≤ 2",
    verfahren="Wertepaare aus der Tabelle als Punkte eintragen und durch eine Exponentialkurve verbinden",
    schritte="1",
    ergebnis="steigende Exponentialkurve durch (−1|1/6), (0|0,5), (1|1,5), (2|4,5)",
    niveau_geschaetzt="I", fehlerquelle="Punkte linear statt exponentiell gekrümmt verbinden")

row(id="2021-GYM-K3b", block="Kontext", aufgabe="3", titel="Funktionen", teilaufgabe="b", seite="2",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Wachstumsfaktor aus Tabelle bestimmen", typ_neben="Punktprobe durchführen",
    stichwoerter="Wachstumsfaktor|Quotient|Punktprobe", format="Rechnung|Rechnung",
    operator="Zeigen Sie rechnerisch|Prüfen Sie rechnerisch", antwort="Text|Text", material="Tabelle",
    skizze="keine", kontext="ohne", textumfang="kurz", abhaengig_von="2021-GYM-K3a",
    gegeben="f(x) = 0,5 · a^x mit f(0) = 0,5 und f(1) = 1,5; Punkt Q(3,5|40,5)",
    gesucht="Nachweis a = 3 anhand zweier Wertepaare; ob Q auf dem Graphen von f liegt",
    verfahren="f(1) : f(0) = 1,5 : 0,5 = 3 = a; Punktprobe: f(3,5) = 0,5 · 3^3,5 ≈ 23,38 ≠ 40,5",
    schritte="2", zahlenraum="dezimal",
    ergebnis="a = 3 bestätigt; Q gehört nicht zum Graphen (f(3,5) ≈ 23,38 ≠ 40,5)",
    niveau_geschaetzt="III",
    fehlerquelle="bei der Punktprobe den x-Wert 3,5 als 3 oder 4 runden statt mit dem gebrochenen "
                 "Exponenten zu rechnen")

row(id="2021-GYM-K3c", block="Kontext", aufgabe="3", titel="Funktionen", teilaufgabe="c", seite="3",
    punkte="5", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Geradengleichung aus zwei Punkten",
    typ_neben="Trapezfläche im Koordinatensystem aus Funktionsgraph und Geraden berechnen",
    stichwoerter="Geradengleichung|Trapez|Flächeninhalt", format="Rechnung|Ankreuzen|Rechnung",
    operator="Ermitteln Sie|Kennzeichnen Sie|Berechnen Sie", antwort="Term|Kreuz|Zahl",
    material="Koordinatensystem", skizze="Koordinatensystem mit den Punkten A(0|0,5) und B(2|4,5) sowie "
             "der Geraden x=2; die begrenzte Fläche liegt zwischen den Achsen, der Geraden g und x=2",
    kontext="ohne", textumfang="mittel",
    gegeben="Gerade g schneidet den Graphen von f in A(0|0,5) und B(2|4,5)",
    gesucht="Funktionsgleichung von g; Flächeninhalt der von beiden Achsen, g und der Geraden x=2 "
            "begrenzten Fläche",
    verfahren="Anstieg m = (4,5−0,5):(2−0) = 2, y-Achsenabschnitt aus A: n = 0,5, also g(x) = 2x + 0,5; "
              "die Fläche ist ein Trapez mit den parallelen Seiten 0,5 (bei x=0) und 4,5 (bei x=2) und der "
              "Breite 2: A = 0,5 · (0,5 + 4,5) · 2", schritte="2", zahlenraum="dezimal", einheiten="FE",
    ergebnis="g(x) = 2x + 0,5; Flächeninhalt = 5 FE", niveau_geschaetzt="III",
    fehlerquelle="die Fläche als Dreieck statt als Trapez auffassen und nur mit einer der beiden "
                 "parallelen Seiten rechnen")

row(id="2021-GYM-K4a", block="Kontext", aufgabe="4", titel="Jugendclub", teilaufgabe="a", seite="4",
    punkte="3", leitidee="Raum und Form", thema="Kongruenz und Konstruktion",
    typ="Vieleck aus Seiten und Winkeln im Maßstab konstruieren",
    stichwoerter="Fünfeck|Grundstück|Maßstab|Konstruktion", format="Konstruieren", operator="Konstruieren Sie",
    antwort="Grafik", material="Figur",
    skizze="Fünfeck ABCDE: A und B unten mit rechten Winkeln (Punktmarkierung), AB = 30 m, BC = 30 m "
           "(senkrecht), Innenwinkel bei C = 155°, CD = 35 m, Innenwinkel bei D = 63°, DE = 25 m, Seite EA "
           "schließt das Fünfeck; nicht maßstabsgerecht",
    kontext="Bauwesen", textumfang="mittel",
    gegeben="Fünfeck ABCDE mit AB = 30 m, rechten Winkeln bei A und B, BC = 30 m, Innenwinkel bei C = "
            "155°, CD = 35 m, Innenwinkel bei D = 63°, DE = 25 m",
    gesucht="Konstruktion des Grundstücks im Maßstab 1:500",
    verfahren="AB als Strecke von 6 cm (30 m im Maßstab 1:500) zeichnen, an A und B rechte Winkel "
              "antragen, BC = 6 cm senkrecht abtragen, bei C den Winkel 155° antragen und CD = 7 cm "
              "abtragen, bei D den Winkel 63° antragen und DE = 5 cm abtragen, E mit A verbinden",
    schritte="5", zahlenraum="dezimal", einheiten="m|cm",
    ergebnis="maßstabsgerechte Konstruktion des Fünfecks (Seiten im Maßstab 1:500: 6 cm, 6 cm, 7 cm, 5 cm)",
    niveau_geschaetzt="II",
    fehlerquelle="einen der beiden rechten Winkel bei A oder B auslassen oder die Winkel bei C und D "
                 "seitenverkehrt antragen")

row(id="2021-GYM-K4b", block="Kontext", aufgabe="4", titel="Jugendclub", teilaufgabe="b", seite="5",
    punkte="3", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Flächeninhalt Dreieck berechnen",
    stichwoerter="Liegewiese|Rasensamen|Dreiecksfläche", format="Begründung", operator="Prüfen Sie",
    antwort="Text", material="keins", skizze="keine", kontext="Bauwesen", textumfang="mittel",
    abhaengig_von="2021-GYM-K4a",
    gegeben="Dreieck CDE mit CD = 35 m, DE = 25 m, Innenwinkel bei D = 63°; acht Tüten Samen, eine Tüte "
            "reicht für 50 m²",
    gesucht="ob acht Tüten für die Fläche CDE ausreichen",
    verfahren="A(CDE) = 0,5 · CD · DE · sin(63°); Vergleich mit 8 · 50 m² = 400 m²", schritte="2",
    zahlenraum="dezimal", einheiten="m²",
    ergebnis="A(CDE) ≈ 389,8 m² ≤ 400 m², die acht Tüten reichen aus", niveau_geschaetzt="III",
    fehlerquelle="den Winkel bei D nicht in die Flächenformel für ein allgemeines Dreieck einbeziehen und "
                 "stattdessen CD · DE rechnen")

row(id="2021-GYM-K4c", block="Kontext", aufgabe="4", titel="Jugendclub", teilaufgabe="c", seite="6",
    punkte="2", leitidee="Größen und Messen", thema="Sinussatz",
    typ="Seite im allgemeinen Dreieck über Kosinussatz berechnen",
    stichwoerter="Kosinussatz|Diagonale|Kontrollergebnis", format="Rechnung", operator="Zeigen Sie rechnerisch",
    antwort="Text", material="keins", skizze="keine", kontext="Bauwesen", textumfang="kurz",
    abhaengig_von="2021-GYM-K4a",
    gegeben="Dreieck CDE mit CD = 35 m, DE = 25 m, Innenwinkel bei D = 63°",
    gesucht="Nachweis EC ≈ 32,5 m",
    verfahren="Kosinussatz: EC² = CD² + DE² − 2·CD·DE·cos(63°)", schritte="1", zahlenraum="dezimal",
    einheiten="m", ergebnis="EC ≈ 32,49 m ≈ 32,5 m", niveau_geschaetzt="II",
    fehlerquelle="den Kosinussatz mit einem falschen Winkel (z. B. 155° statt 63°) ansetzen")

row(id="2021-GYM-K4d", block="Kontext", aufgabe="4", titel="Jugendclub", teilaufgabe="d", seite="6",
    punkte="2", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Flächenberechnung eines Vielecks anhand einer vorgegebenen Gleichung erläutern",
    stichwoerter="Vielecksfläche|Rechteck plus Dreieck|Satz des Pythagoras", format="Begründung",
    operator="Erläutern Sie", antwort="Text", material="keins", skizze="keine", kontext="Bauwesen",
    textumfang="mittel", abhaengig_von="2021-GYM-K4c",
    gegeben="Gleichung A(ABCE) = 30 · 30 + 0,5 · 30 · √(32,5² − 30²) zur Berechnung der Fläche ABCE",
    gesucht="Erläuterung des dargestellten Vorgehens",
    verfahren="Die Fläche ABCE wird zerlegt in das Quadrat ABC X (X senkrecht über A auf Höhe von C, "
              "Seitenlänge 30 m, da AB = BC = 30 m und die Winkel bei A und B rechte Winkel sind) und das "
              "Dreieck XCE darüber; dessen Höhe wird über den Satz des Pythagoras aus der Diagonale EC "
              "(≈32,5 m) und der Grundseite XC = 30 m als Kathete berechnet: √(32,5² − 30²) = 12,5 m",
    schritte="2", zahlenraum="dezimal", einheiten="m|m²",
    ergebnis="Zerlegung in Quadrat 30 m × 30 m plus Dreieck mit Grundseite 30 m und über Pythagoras aus "
             "EC und der Kathete 30 m berechneter Höhe 12,5 m", niveau_geschaetzt="III",
    fehlerquelle="√(32,5² − 30²) als einfache Differenz 32,5 − 30 statt über den Satz des Pythagoras "
                 "deuten")

row(id="2021-GYM-K5a", block="Kontext", aufgabe="5", titel="Messbecher", teilaufgabe="a", seite="7",
    punkte="5", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Formel für die Tiefe eines Kegels aus Durchmesser und Öffnungswinkel herleiten",
    typ_neben="Volumen Kegel berechnen",
    stichwoerter="Kegel|Öffnungswinkel|Tiefe|Fassungsvermögen", format="Begründung|Rechnung",
    operator="Begründen Sie|Berechnen Sie", antwort="Text|Zahl", material="Figur",
    skizze="kegelförmiger Messbecher, Spitze unten, oberer Durchmesser d = 10 cm, Öffnungswinkel α = "
           "36,8° an der Spitze", kontext="Haushalt", textumfang="mittel",
    gegeben="kegelförmiger Messbecher mit oberem Durchmesser d = 10 cm und Öffnungswinkel α = 36,8°",
    gesucht="Begründung für t = (d/2) : tan(α/2); maximales Fassungsvermögen",
    verfahren="das rechtwinklige Teildreieck aus der halben Kegelachse (Tiefe t), dem halben Durchmesser "
              "(d/2) und dem halben Öffnungswinkel (α/2) liefert tan(α/2) = (d/2):t, also t = (d/2):tan(α/2); "
              "Volumen V = 1/3 · π · (d/2)² · t", schritte="2", zahlenraum="dezimal", einheiten="cm|cm³",
    ergebnis="t ≈ 15,03 cm; V ≈ 393,5 cm³ ≈ 0,39 L", niveau_geschaetzt="III",
    fehlerquelle="mit dem vollen Öffnungswinkel α statt mit α/2 im rechtwinkligen Teildreieck rechnen")

row(id="2021-GYM-K5b", block="Kontext", aufgabe="5", titel="Messbecher", teilaufgabe="b", seite="8",
    punkte="5", leitidee="Raum und Form", thema="Ähnlichkeit und Strahlensätze",
    typ="Länge auf der Mantellinie eines Kegels bei Teilfüllung über Ähnlichkeit bestimmen",
    typ_neben="Mantellinie Kegel bestimmen",
    stichwoerter="Mantellinie|Ähnlichkeit|Füllhöhe|Markierung", format="Rechnung|Rechnung",
    operator="Berechnen Sie|Berechnen Sie", antwort="Zahl|Zahl", material="keins",
    skizze="keine", kontext="Haushalt", textumfang="mittel", abhaengig_von="2021-GYM-K5a",
    gegeben="Messbecher wie in Teilaufgabe a (d = 10 cm, t ≈ 15,03 cm); 300-ml-Markierung bei Füllhöhe "
            "13,7 cm [Kontrollergebnis Mantellinie s ≈ 15,8 cm]",
    gesucht="Länge der Mantellinie s des ganzen Kegels; Entfernung der 300-ml-Markierung entlang der "
            "Mantellinie vom oberen Rand",
    verfahren="s = √((d/2)² + t²) ≈ 15,84 cm; der kleine, bis zur Füllhöhe 13,7 cm reichende Kegel ist "
              "ähnlich zum ganzen Kegel mit dem Streckfaktor 13,7:t; seine Mantellinie (Abstand der "
              "Markierung von der Spitze) ist s · 13,7/t; der gesuchte Abstand vom oberen Rand ist "
              "s − s · 13,7/t", schritte="3", zahlenraum="dezimal", einheiten="cm",
    ergebnis="s ≈ 15,84 cm; Entfernung der 300-ml-Markierung vom oberen Rand ≈ 1,40 cm",
    niveau_geschaetzt="III",
    fehlerquelle="die Füllhöhe direkt von der Mantellinie s abziehen, statt den ähnlichen kleinen Kegel "
                 "über den Streckfaktor zu berücksichtigen")

row(id="2021-GYM-K6a", block="Kontext", aufgabe="6", titel="Kugelstoßen", teilaufgabe="a", seite="8",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Funktionen allgemein",
    typ="Punktprobe durchführen", typ_neben="Gleichung im Sachzusammenhang deuten",
    stichwoerter="Flugbahn|Punktprobe|absolutes Glied|Abwurfhöhe", format="Rechnung|Kurzantwort",
    operator="Zeigen Sie rechnerisch|Geben Sie an", antwort="Text|Text", material="Tabelle",
    skizze="keine", kontext="Freizeit/Sport", textumfang="mittel",
    gegeben="Flugbahn h(x) = −0,4x² + 2,4x + 1,5; Punkt P(2|4,7) aus der Tabelle",
    gesucht="Nachweis, dass P auf der Flugbahn liegt; Bedeutung des Gliedes c = 1,5",
    verfahren="h(2) = −0,4·4 + 2,4·2 + 1,5 = −1,6 + 4,8 + 1,5 einsetzen und mit 4,7 vergleichen; c ist der "
              "Funktionswert bei x = 0, also die Höhe beim Abstoß", schritte="2", zahlenraum="dezimal",
    einheiten="m", ergebnis="h(2) = 4,7, Punkt bestätigt; c = 1,5 ist die Abwurfhöhe der Kugel über dem "
             "Boden", niveau_geschaetzt="II",
    fehlerquelle="c = 1,5 als Wurfweite oder als maximale Höhe statt als Abwurfhöhe deuten")

row(id="2021-GYM-K6b", block="Kontext", aufgabe="6", titel="Kugelstoßen", teilaufgabe="b", seite="9",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Funktionen allgemein",
    typ="Achseneinteilung wählen", typ_neben="Scheitelpunkt ablesen",
    stichwoerter="Achsenskalierung|Scheitelpunkt|maximale Höhe", format="Eintragen|Kurzantwort",
    operator="Skalieren Sie|Geben Sie an", antwort="Grafik|Zahl", material="Diagramm",
    skizze="Koordinatensystem ohne Skala mit eingezeichneter Flugbahn (Parabelbogen)", kontext="Freizeit/Sport",
    textumfang="kurz", abhaengig_von="2021-GYM-K6a",
    gegeben="Diagramm mit der Flugbahn h(x) = −0,4x² + 2,4x + 1,5 ohne Achsenskala",
    gesucht="passende Achseneinteilung; maximale Höhe der Kugel",
    verfahren="Scheitelpunkt über x_s = −b/(2a) = −2,4/(−0,8) = 3, h(3) = −0,4·9 + 2,4·3 + 1,5 = 5,1; "
              "Achsen so einteilen, dass x von 0 bis über die Nullstelle (≈6,6) und y bis über 5,1 "
              "sichtbar sind", schritte="2", zahlenraum="dezimal", einheiten="m",
    ergebnis="maximale Höhe 5,1 m bei x = 3 m", niveau_geschaetzt="III",
    fehlerquelle="die Achsen zu klein wählen, sodass der Scheitelpunkt oder die Nullstelle nicht mehr "
                 "sichtbar sind")

row(id="2021-GYM-K6c", block="Kontext", aufgabe="6", titel="Kugelstoßen", teilaufgabe="c", seite="9",
    punkte="3", leitidee="Größen und Messen", thema="Einheiten umrechnen",
    typ="Fehler in Rechnung erklären und korrigieren",
    stichwoerter="pq-Formel|Vorzeichenfehler|Stoßweite", format="Begründung|Rechnung",
    operator="Beschreiben Sie|Berechnen Sie", antwort="Text|Zahl", material="keins",
    skizze="keine", kontext="Freizeit/Sport", textumfang="mittel", abhaengig_von="2021-GYM-K6a",
    gegeben="Franz' Rechnung: 0 = x² − 6x − 3,75; x1/2 = 3 ± √(9 − 3,75); x1 = 5,29; x2 = 0,71",
    gesucht="Fehler in Franz' Rechnung; korrekte Stoßweite",
    verfahren="in der pq-Formel muss unter der Wurzel (p/2)² − q stehen, mit q = −3,75 also 9 − (−3,75) = "
              "12,75; Franz hat stattdessen 9 − 3,75 gerechnet (Vorzeichenfehler bei q); korrekt: x1/2 = "
              "3 ± √12,75", schritte="2", zahlenraum="dezimal", einheiten="m",
    ergebnis="Fehler: falsches Vorzeichen von q unter der Wurzel; korrekt x1 ≈ 6,57 (Stoßweite), x2 ≈ "
             "−0,57 (nicht physikalisch)", niveau_geschaetzt="III",
    fehlerquelle="den negativen Wert x2 als Stoßweite verwenden, obwohl nur der positive Wert physikalisch "
                 "sinnvoll ist")
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
