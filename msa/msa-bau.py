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
    "jahr": "2025",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "",         # zweiteiliges Heft ab 2019, siehe "dateien"
    "dateien": ["25_P10_Ma_Gym_A1.pdf", "25_P10_Ma_Gym_A2.pdf"],
    "seiten": {"Basis": 3, "Kontext": 8},  # eigene Fußzeile je Teildatei (msa.md § 3)
    "soll": {"1": 5, "2": 5, "3": 12, "4": 9, "5": 13, "6": 6},
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
    ("Gleich große oder doppelt so große Winkel in einer aus kongruenten Dreiecken zusammengesetzten "
     "Figur kennzeichnen", "Raum und Form", "Ebene Figuren und Winkel",
     "In einer aus mehreren kongruenten rechtwinkligen Dreiecken zusammengesetzten Figur einen zu einem "
     "gegebenen Winkel gleich großen bzw. einen doppelt so großen Winkel markieren, unter Nutzung der "
     "Kongruenz der Teildreiecke und der Symmetrie der Figur.",
     "2025-GYM-B1a"),
    ("Flächeninhalt eines aus vier kongruenten rechtwinkligen Dreiecken zusammengesetzten Vierecks "
     "berechnen", "Größen und Messen", "Flächeninhalt und Umfang",
     "Flächeninhalt eines Vierecks (Drachen/Raute) berechnen, das aus vier kongruenten rechtwinkligen "
     "Dreiecken mit gegebenen Katheten zusammengesetzt ist.",
     "2025-GYM-B1b"),
    ("Term durch Zusammenfassen gleichartiger Glieder vereinfachen", "Zahlen und Operationen",
     "Terme umformen",
     "Einen Term durch Zusammenfassen gleichartiger Glieder (ohne Klammern oder binomische Formeln) "
     "vereinfachen und anschließend den Wert für eine gegebene Variablenbelegung berechnen.",
     "2025-GYM-B2a"),
    ("Aussage über einen Logarithmusterm als Abstand zur y-Achse prüfen", "Gleichungen und Funktionen",
     "Exponentialfunktionen und Wachstum",
     "Prüfen, ob der x-Wert eines Punktes einer Exponentialfunktion (als Abstand zur y-Achse) einem "
     "gegebenen Logarithmusterm entspricht, unter Beachtung von Basis und Numerus des Logarithmus.",
     "2025-GYM-K3c"),
    ("Exponentialfunktion vertikal verschieben und Schnittpunkt mit der y-Achse angeben",
     "Gleichungen und Funktionen", "Exponentialfunktionen und Wachstum",
     "Gleichung einer Exponentialfunktion nach vertikaler Verschiebung angeben und den Schnittpunkt des "
     "verschobenen Graphen mit der y-Achse bestimmen.",
     "2025-GYM-K3d"),
    ("Seite im rechtwinkligen Dreieck aus Winkel und Kathete berechnen", "Größen und Messen",
     "Trigonometrie im rechtwinkligen Dreieck",
     "Eine fehlende Seite (Kathete oder Hypotenuse) eines rechtwinkligen Dreiecks aus einem gegebenen "
     "Winkel und einer bekannten Kathete über eine Winkelfunktion berechnen.",
     "2025-GYM-K4a"),
    ("Winkel im allgemeinen Dreieck über Sinussatz berechnen", "Größen und Messen", "Sinussatz",
     "Im allgemeinen Dreieck einen Winkel aus zwei gegebenen Seiten und dem einer der Seiten "
     "gegenüberliegenden Winkel mit dem Sinussatz berechnen.",
     "2025-GYM-K4b"),
    ("Fläche zweier Mantelflächen eines Prismas mit trapezförmiger Grundfläche berechnen",
     "Größen und Messen", "Volumen und Oberfläche",
     "Fläche der beiden zu den Schenkeln eines trapezförmigen Prismenquerschnitts gehörenden "
     "rechteckigen Mantelflächen berechnen, wobei die Schenkellänge zuvor über den Satz des Pythagoras "
     "aus der Höhe und dem halben Längenunterschied der parallelen Seiten bestimmt wird.",
     "2025-GYM-K5d"),
    ("Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen", "Daten und Zufall",
     "Wahrscheinlichkeit einstufig",
     "Erwartete Anzahl von Ereignissen in einer Stichprobe aus der Einzelwahrscheinlichkeit und dem "
     "Stichprobenumfang berechnen (Produkt aus Wahrscheinlichkeit und Anzahl).",
     "2025-GYM-K6b"),
    ("Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen",
     "Daten und Zufall", "Wahrscheinlichkeit mehrstufig",
     "Aus der Wahrscheinlichkeit, dass mehrere unabhängige gleichartige Ereignisse gemeinsam eintreten, "
     "durch Wurzelziehen die Einzelwahrscheinlichkeit (den Anteil) zurückrechnen und mit einem "
     "Vergleichswert in Beziehung setzen.",
     "2025-GYM-K6c"),
]

row(id="2025-GYM-B1a", block="Basis", aufgabe="1", titel="", teilaufgabe="a", seite="2",
    punkte="2", hilfsmittel="nein", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Gleich große oder doppelt so große Winkel in einer aus kongruenten Dreiecken zusammengesetzten "
        "Figur kennzeichnen",
    stichwoerter="kongruente Dreiecke|Winkel kennzeichnen|Symmetrie", format="Ankreuzen",
    operator="Kennzeichnen Sie", antwort="Kreuz", material="Figur",
    skizze="Viereck (Raute) aus vier kongruenten rechtwinkligen Dreiecken mit Katheten a (waagerecht) "
           "und b (senkrecht), rechter Winkel im Mittelpunkt; α am rechten Mittelpunkt, β an der "
           "oberen Spitze", kontext="ohne", textumfang="mittel",
    gegeben="Viereck aus vier kongruenten rechtwinkligen Dreiecken mit Katheten a und b, Winkel α und β "
            "eingezeichnet",
    gesucht="ein Winkel γ, der genauso groß wie α ist; ein Winkel δ, der doppelt so groß wie β ist",
    verfahren="γ am entsprechenden Winkel des kongruenten Dreiecks auf der gegenüberliegenden Seite "
              "kennzeichnen (z. B. am linken Mittelpunkt); δ als volle Winkelspanne der Spitze aus beiden "
              "angrenzenden β-Winkeln (oben oder unten) kennzeichnen", schritte="1",
    ergebnis="γ am linken (oder unteren) Mittelpunktswinkel; δ als voller Spitzenwinkel oben (oder "
             "unten), zusammengesetzt aus zwei β",
    niveau_geschaetzt="II",
    fehlerquelle="δ als einzelnen Winkel eines Teildreiecks statt als Summe zweier β-Winkel kennzeichnen")

row(id="2025-GYM-B1b", block="Basis", aufgabe="1", titel="", teilaufgabe="b", seite="2",
    punkte="3", hilfsmittel="nein", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Flächeninhalt eines aus vier kongruenten rechtwinkligen Dreiecken zusammengesetzten Vierecks "
        "berechnen",
    stichwoerter="Raute|vier kongruente Dreiecke|Flächeninhalt", format="Rechnung",
    operator="Berechnen Sie", antwort="Zahl", material="Figur", skizze="wie 2025-GYM-B1a",
    kontext="ohne", textumfang="kurz", abhaengig_von="2025-GYM-B1a",
    gegeben="vier kongruente rechtwinklige Dreiecke mit Kathete a = 4 cm und Kathete b = 2·a",
    gesucht="Flächeninhalt des abgebildeten Vierecks",
    verfahren="ein Dreieck hat die Fläche 0,5·a·b; das Viereck besteht aus vier solchen Dreiecken",
    schritte="2", zahlenraum="ganz", einheiten="cm|cm²",
    ergebnis="a = 4 cm, b = 8 cm, Flächeninhalt = 64 cm²", niveau_geschaetzt="II",
    fehlerquelle="nur ein oder zwei Dreiecke statt aller vier in die Flächenberechnung einbeziehen")

row(id="2025-GYM-B2a", block="Basis", aufgabe="2", titel="", teilaufgabe="a", seite="3",
    punkte="2", hilfsmittel="nein", leitidee="Zahlen und Operationen", thema="Terme umformen",
    typ="Term durch Zusammenfassen gleichartiger Glieder vereinfachen",
    stichwoerter="Term vereinfachen|Termwert", format="Rechnung", operator="Vereinfachen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Term 6x − 3x² − 4x",
    gesucht="vereinfachter Term; Wert für x = 2",
    verfahren="gleichartige Glieder zusammenfassen: 6x − 4x = 2x, Term wird 2x − 3x²; x = 2 einsetzen",
    schritte="2", zahlenraum="ganz",
    ergebnis="2x − 3x²; Wert für x = 2 ist −8", niveau_geschaetzt="II",
    fehlerquelle="6x und −4x nicht zusammenfassen oder −3x² mit −3x verwechseln")

row(id="2025-GYM-B2b", block="Basis", aufgabe="2", titel="", teilaufgabe="b", seite="3",
    punkte="3", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Quadratische Gleichungen",
    typ="Nullstellen quadratische Funktion berechnen",
    stichwoerter="quadratische Gleichung|pq-Formel|Faktorisieren", format="Rechnung",
    operator="Ermitteln Sie", antwort="Zahl", material="keins", skizze="keine", kontext="ohne",
    textumfang="kurz",
    gegeben="Gleichung x² + 2x − 8 = 0",
    gesucht="Lösungen der Gleichung",
    verfahren="pq-Formel oder Faktorisieren: (x+4)(x−2) = 0", schritte="1", zahlenraum="ganz",
    ergebnis="x1 = −4, x2 = 2", niveau_geschaetzt="II",
    fehlerquelle="nur eine der beiden Lösungen angeben")

row(id="2025-GYM-K3a", block="Kontext", aufgabe="3", titel="Exponentialfunktion", teilaufgabe="a",
    seite="2", punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und "
    "Wachstum",
    typ="Punktprobe durchführen",
    stichwoerter="Punktprobe|Exponentialfunktion", format="Rechnung", operator="Überprüfen Sie",
    antwort="Text", material="Koordinatensystem",
    skizze="Graph von f(x)=2^x im Koordinatensystem, streng monoton steigend, durch (0|1)",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 2^x; Punkt P(−4|0,05)",
    gesucht="ob P auf dem Graphen von f liegt",
    verfahren="f(−4) = 2^(−4) = 1:16 = 0,0625 berechnen und mit 0,05 vergleichen", schritte="1",
    zahlenraum="Bruch",
    ergebnis="f(−4) = 0,0625 ≠ 0,05, P liegt nicht auf dem Graphen", niveau_geschaetzt="II",
    fehlerquelle="2^(−4) als negative Zahl (−2^4) statt als 1:2^4 berechnen")

row(id="2025-GYM-K3b", block="Kontext", aufgabe="3", titel="Exponentialfunktion", teilaufgabe="b",
    seite="2", punkte="1", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und "
    "Wachstum",
    typ="Wertebereich einer Funktion angeben",
    stichwoerter="Wertebereich|Exponentialfunktion", format="Kurzantwort", operator="Geben Sie an",
    antwort="Term", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    abhaengig_von="2025-GYM-K3a",
    gegeben="f(x) = 2^x",
    gesucht="Wertebereich von f",
    verfahren="Exponentialfunktionen mit positiver Basis nehmen nur positive Werte an", schritte="1",
    ergebnis="f(x) > 0 für alle x (Wertebereich ℝ⁺)", niveau_geschaetzt="I",
    fehlerquelle="0 fälschlich zum Wertebereich zählen")

row(id="2025-GYM-K3c", block="Kontext", aufgabe="3", titel="Exponentialfunktion", teilaufgabe="c",
    seite="2", punkte="3", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und "
    "Wachstum",
    typ="Aussage über einen Logarithmusterm als Abstand zur y-Achse prüfen",
    stichwoerter="Logarithmus|Basiswechsel|Abstand zur y-Achse", format="Rechnung", operator="Prüfen Sie",
    antwort="Text", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    abhaengig_von="2025-GYM-K3a",
    gegeben="f(x) = 2^x; Punkt R(x|10) auf dem Graphen von f; Behauptung: Abstand von R zur y-Achse ist "
            "log₁₀(2)",
    gesucht="Wahrheitsgehalt der Behauptung",
    verfahren="Abstand zur y-Achse ist |x| mit 2^x=10, also x=log₂(10) ≈ 3,32; log₁₀(2) ≈ 0,301 "
              "berechnen und vergleichen (log₂(10) und log₁₀(2) sind zueinander reziprok, nicht gleich)",
    schritte="2", zahlenraum="dezimal",
    ergebnis="Behauptung ist falsch: log₂(10) ≈ 3,32 ≠ log₁₀(2) ≈ 0,301", niveau_geschaetzt="III",
    fehlerquelle="log₂(10) und log₁₀(2) für denselben Wert halten, statt Basis und Numerus zu "
                 "unterscheiden")

row(id="2025-GYM-K3d", block="Kontext", aufgabe="3", titel="Exponentialfunktion", teilaufgabe="d",
    seite="3", punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und "
    "Wachstum",
    typ="Exponentialfunktion vertikal verschieben und Schnittpunkt mit der y-Achse angeben",
    stichwoerter="Verschiebung nach unten|y-Achsenabschnitt", format="Kurzantwort", operator="Geben Sie an",
    antwort="Term", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    abhaengig_von="2025-GYM-K3a",
    gegeben="f(x) = 2^x wird um 4 LE entlang der y-Achse nach unten verschoben",
    gesucht="Funktionsgleichung des verschobenen Graphen; Koordinaten des Schnittpunkts S mit der "
            "y-Achse",
    verfahren="Verschiebung um 4 nach unten: neue Funktion 2^x − 4; Schnittpunkt mit der y-Achse bei "
              "x=0 berechnen", schritte="1", zahlenraum="ganz",
    ergebnis="2^x − 4; S(0|−3)", niveau_geschaetzt="II",
    fehlerquelle="die Verschiebung auf den Exponenten statt auf den Funktionswert anwenden (2^(x−4))")

row(id="2025-GYM-K3e", block="Kontext", aufgabe="3", titel="Exponentialfunktion", teilaufgabe="e",
    seite="3", punkte="3", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und "
    "Wachstum",
    typ="Funktionswert berechnen", typ_neben="Wertetabelle als Punkte darstellen",
    stichwoerter="Wertetabelle|Graph zeichnen", format="Kurzantwort|Zeichnen",
    operator="Geben Sie an|Skizzieren Sie", antwort="Zahl|Grafik", material="Koordinatensystem",
    skizze="Koordinatensystem für g(x)=2^(−x), Wertetabelle mit x = −2 und x = 1,5", kontext="ohne",
    textumfang="kurz", abhaengig_von="2025-GYM-K3a",
    gegeben="g(x) = 2^(−x); Wertetabelle für x = −2 und x = 1,5",
    gesucht="Funktionswerte g(−2) und g(1,5); Graph von g mindestens im Intervall [−2;1,5]",
    verfahren="g(−2) = 2^2 = 4; g(1,5) = 2^(−1,5) ≈ 0,354; Punkte eintragen und verbinden", schritte="2",
    zahlenraum="dezimal",
    ergebnis="g(−2) = 4; g(1,5) ≈ 0,35", niveau_geschaetzt="II",
    fehlerquelle="beim negativen Exponenten das Vorzeichen falsch behandeln (g(−2) = 2^(−2) statt 2^2)")

row(id="2025-GYM-K3f", block="Kontext", aufgabe="3", titel="Exponentialfunktion", teilaufgabe="f",
    seite="3", punkte="1", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und "
    "Wachstum",
    typ="Graph einer Exponentialfunktion an der y-Achse spiegeln",
    stichwoerter="Spiegelung an der y-Achse|Exponent negiert", format="Begründung",
    operator="Beschreiben Sie", antwort="Text", material="keins", skizze="keine", kontext="ohne",
    textumfang="kurz", abhaengig_von="2025-GYM-K3e",
    gegeben="f(x) = 2^x, g(x) = 2^(−x)",
    gesucht="Beschreibung, wie der Graph von g aus dem Graphen von f hervorgeht",
    verfahren="g(x) = f(−x), also Vorzeichenwechsel im Exponenten", schritte="1",
    ergebnis="g entsteht durch Spiegelung des Graphen von f an der y-Achse", niveau_geschaetzt="I",
    fehlerquelle="eine Spiegelung an der x-Achse statt an der y-Achse angeben")

row(id="2025-GYM-K4a", block="Kontext", aufgabe="4", titel="Dorfteich", teilaufgabe="a", seite="4",
    punkte="2", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Seite im rechtwinkligen Dreieck aus Winkel und Kathete berechnen",
    stichwoerter="Peilung|rechtwinkliges Dreieck|Hypotenuse", format="Rechnung",
    operator="Weisen Sie rechnerisch nach", antwort="Text", material="Figur",
    skizze="Viereck PSZQ am Dorfteich: P und Q auf einer Standlinie (PQ=150 m), bei P Winkel 50° (zu S) "
           "und 40° (zu Z, zusammen 90° zu PQ), bei Q Winkel β (zu Z) und 20° (zu S, zu PQ); S liegt am "
           "Teichrand, Z gegenüber; nicht maßstabsgerecht", kontext="Freizeit/Sport", textumfang="mittel",
    gegeben="rechtwinkliges Dreieck SPQ (rechter Winkel bei P, da 50°+40°=90°), PQ = 150 m, Winkel SQP "
            "= 20°",
    gesucht="Nachweis, dass SQ ≈ 159,6 m",
    verfahren="cos(20°) = PQ:SQ, also SQ = PQ:cos(20°)", schritte="1", zahlenraum="dezimal",
    einheiten="m", ergebnis="SQ ≈ 159,63 m ≈ 159,6 m", niveau_geschaetzt="II",
    fehlerquelle="sin und cos vertauschen und SQ = PQ:sin(20°) berechnen")

row(id="2025-GYM-K4b", block="Kontext", aufgabe="4", titel="Dorfteich", teilaufgabe="b", seite="4",
    punkte="4", leitidee="Größen und Messen", thema="Sinussatz",
    typ="Winkel im allgemeinen Dreieck über Sinussatz berechnen",
    stichwoerter="Sinussatz|Winkelsumme|Dreieck PQZ", format="Rechnung", operator="Zeigen Sie rechnerisch",
    antwort="Text", material="Figur", skizze="wie 2025-GYM-K4a; zusätzlich QZ = 117,7 m eingezeichnet",
    kontext="Freizeit/Sport", textumfang="mittel", abhaengig_von="2025-GYM-K4a",
    gegeben="Dreieck PQZ mit PQ = 150 m, Winkel bei P (ZPQ) = 40°, QZ = 117,7 m (Seite gegenüber P)",
    gesucht="Nachweis, dass Winkel α (bei Z) ≈ 55° ist; Nachweis, dass Winkel β ≈ 65° ist",
    verfahren="Sinussatz: QZ:sin(P) = PQ:sin(Z), also sin(Z) = PQ·sin(40°):QZ, α = Z = arcsin(...); "
              "Winkel bei Q im Dreieck PQZ = 180° − 40° − α; davon ist 20° der Winkel SQP (aus "
              "Teilaufgabe a), der Rest ist β = (180° − 40° − α) − 20°", schritte="3",
    zahlenraum="dezimal", einheiten="Grad", ergebnis="α ≈ 55,0°; β ≈ 65,0°", niveau_geschaetzt="III",
    fehlerquelle="den Sinussatz mit der falschen Seiten-Winkel-Zuordnung ansetzen (QZ gegenüber Z statt "
                 "gegenüber P)")

row(id="2025-GYM-K4c", block="Kontext", aufgabe="4", titel="Dorfteich", teilaufgabe="c", seite="5",
    punkte="3", leitidee="Größen und Messen", thema="Sinussatz",
    typ="Seite im allgemeinen Dreieck über Kosinussatz berechnen",
    stichwoerter="Kosinussatz|Mindestlänge|Bedingung prüfen", format="Rechnung", operator="Prüfen Sie",
    antwort="Text", material="keins", skizze="keine", kontext="Freizeit/Sport", textumfang="kurz",
    abhaengig_von="2025-GYM-K4b",
    gegeben="Dreieck SQZ mit SQ ≈ 159,6 m, QZ = 117,7 m, Winkel SQZ = β ≈ 65°; geforderte Mindestlänge "
            "SZ ≥ 150 m",
    gesucht="ob die Strecke SZ mindestens 150 m lang ist",
    verfahren="Kosinussatz: SZ² = SQ² + QZ² − 2·SQ·QZ·cos(65°)", schritte="1", zahlenraum="dezimal",
    einheiten="m", ergebnis="SZ ≈ 153,1 m ≥ 150 m, die Bedingung ist erfüllt", niveau_geschaetzt="III",
    fehlerquelle="den falschen (nicht eingeschlossenen) Winkel in den Kosinussatz einsetzen")

row(id="2025-GYM-K5a", block="Kontext", aufgabe="5", titel="Verpackung", teilaufgabe="a", seite="6",
    punkte="2", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Flächeninhalt Trapez berechnen",
    stichwoerter="Trapez|Grundfläche|Prisma", format="Rechnung", operator="Weisen Sie nach",
    antwort="Text", material="Figur",
    skizze="Prisma, Grundfläche gleichschenkliges Trapez mit parallelen Seiten 6 cm und 12 cm, Abstand "
           "6 cm, Prismenhöhe 10 cm; nicht maßstabsgerecht", kontext="Freizeit/Konsum", textumfang="kurz",
    gegeben="Trapez mit parallelen Seiten 6 cm und 12 cm, Abstand (Höhe) 6 cm",
    gesucht="Nachweis, dass die Grundfläche 54 cm² beträgt",
    verfahren="A = 0,5 · (a + c) · h mit a=6, c=12, h=6", schritte="1", zahlenraum="ganz",
    einheiten="cm|cm²", ergebnis="A = 54 cm²", niveau_geschaetzt="I",
    fehlerquelle="nur eine der beiden parallelen Seiten in die Formel einsetzen")

row(id="2025-GYM-K5b", block="Kontext", aufgabe="5", titel="Verpackung", teilaufgabe="b", seite="6",
    punkte="4", leitidee="Raum und Form", thema="Körper, Netze, Schrägbilder",
    typ="Körper im Schrägbild darstellen",
    stichwoerter="Schrägbild|Maßstab 1:1|Verzerrungsfaktor", format="Zeichnen", operator="Zeichnen Sie",
    antwort="Grafik", material="keins",
    skizze="Schrägbild des Prismas mit trapezförmiger Grundfläche, Verzerrungsfaktor q=0,5, "
           "Winkel α=45°, Maßstab 1:1", kontext="Freizeit/Konsum", textumfang="kurz",
    abhaengig_von="2025-GYM-K5a",
    gegeben="Prisma mit trapezförmiger Grundfläche (Maße aus Teilaufgabe a) und Höhe 10 cm; "
            "Schrägbildparameter q=0,5, α=45°",
    gesucht="Schrägbild der Verpackung im Maßstab 1:1",
    verfahren="Grundfläche wahr zeichnen, Tiefenachse im Winkel α=45° mit dem Verzerrungsfaktor q=0,5 "
              "antragen, Prismenhöhe 10 cm senkrecht antragen", schritte="1",
    ergebnis="Schrägbild des Prismas mit trapezförmiger Grundfläche", niveau_geschaetzt="II",
    fehlerquelle="die Tiefenachse ohne den Verzerrungsfaktor q in wahrer Länge abtragen")

row(id="2025-GYM-K5c", block="Kontext", aufgabe="5", titel="Verpackung", teilaufgabe="c", seite="7",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Volumen Prisma berechnen", typ_neben="Masse aus Volumen und Dichte berechnen",
    stichwoerter="Prismenvolumen|Füllgrad|Masse", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="Freizeit/Konsum", textumfang="mittel",
    abhaengig_von="2025-GYM-K5a",
    gegeben="Grundfläche 54 cm² (aus Teilaufgabe a), Prismenhöhe 10 cm; Seifenstücke füllen 80 % des "
            "Volumens; 1 cm³ Seife hat eine Masse von 0,9 g",
    gesucht="Volumen der Verpackung; Masse der enthaltenen Seife",
    verfahren="V = Grundfläche · Höhe; Seifenvolumen = 80 % von V; Masse = Seifenvolumen · 0,9 g/cm³",
    schritte="3", zahlenraum="ganz", einheiten="cm³|g",
    ergebnis="V = 540 cm³; Seifenvolumen = 432 cm³; Masse ≈ 388,8 g", niveau_geschaetzt="II",
    fehlerquelle="die 80 % auf die Masse statt auf das Volumen anwenden")

row(id="2025-GYM-K5d", block="Kontext", aufgabe="5", titel="Verpackung", teilaufgabe="d", seite="7",
    punkte="4", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Fläche zweier Mantelflächen eines Prismas mit trapezförmiger Grundfläche berechnen",
    typ_neben="Mantellinie Kegel bestimmen",
    stichwoerter="Körpernetz|Schenkel|Folie", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur",
    skizze="Netz des Prismas: zwei schräg abstehende, mit Blumenmotiv gemusterte Flächen (die beiden "
           "Schenkelflächen des Trapezquerschnitts) neben einem mittleren Rechteckband und den beiden "
           "Trapezflächen (Grund-/Deckfläche); nicht maßstabsgerecht", kontext="Freizeit/Konsum",
    textumfang="mittel", abhaengig_von="2025-GYM-K5a",
    gegeben="Trapez mit parallelen Seiten 6 cm und 12 cm, Abstand 6 cm (aus Teilaufgabe a); "
            "Prismenhöhe 10 cm; zwei Schenkelflächen werden mit Folie beklebt",
    gesucht="benötigte Fläche Folie für die beiden mit Blumenmotiv bedruckten Flächen",
    verfahren="Schenkellänge über Pythagoras: √(((12−6):2)² + 6²) = √(3² + 6²) = √45 = 3√5 cm; jede "
              "Schenkelfläche (Rechteck) hat die Fläche Schenkellänge · 10 cm; zwei Flächen zusammen",
    schritte="3", zahlenraum="Wurzel", einheiten="cm|cm²",
    ergebnis="Schenkellänge = 3√5 cm ≈ 6,71 cm; Folie insgesamt = 2 · 3√5 · 10 ≈ 134,2 cm²",
    niveau_geschaetzt="III",
    fehlerquelle="den halben Längenunterschied (3 cm) statt des vollen Unterschieds (6 cm) als Kathete "
                 "im Satz des Pythagoras verwenden, oder nur eine statt beider Flächen berechnen")

row(id="2025-GYM-K6a", block="Kontext", aufgabe="6", titel="Computerchip", teilaufgabe="a", seite="8",
    punkte="2", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Wahrscheinlichkeit mehrstufig unabhängig",
    stichwoerter="Computerchip|fehlerfrei|unabhängige Entnahme", format="Rechnung",
    operator="Berechnen Sie", antwort="Zahl", material="keins", skizze="keine", kontext="Technik",
    textumfang="kurz",
    gegeben="98,5 % der Computerchips des Herstellers LINE sind fehlerfrei; fünf zufällig entnommene "
            "Chips",
    gesucht="Wahrscheinlichkeit, dass alle fünf Chips fehlerfrei sind",
    verfahren="0,985 hoch 5", schritte="1", zahlenraum="Prozent",
    ergebnis="≈ 92,72 %", niveau_geschaetzt="II",
    fehlerquelle="0,985 mit 5 multiplizieren statt zu potenzieren")

row(id="2025-GYM-K6b", block="Kontext", aufgabe="6", titel="Computerchip", teilaufgabe="b", seite="8",
    punkte="2", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit einstufig",
    typ="Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen",
    stichwoerter="fehlerhafte Chips|erwartete Anzahl|Stichprobe", format="Rechnung",
    operator="Ermitteln Sie", antwort="Zahl", material="keins", skizze="keine", kontext="Technik",
    textumfang="kurz", abhaengig_von="2025-GYM-K6a",
    gegeben="98,5 % der Chips sind fehlerfrei; 1000 zufällig entnommene Chips",
    gesucht="Anzahl der zu erwartenden fehlerhaften Chips",
    verfahren="Anteil fehlerhaft = 1 − 0,985 = 0,015; erwartete Anzahl = 1000 · 0,015", schritte="1",
    zahlenraum="ganz",
    ergebnis="15 fehlerhafte Chips", niveau_geschaetzt="I",
    fehlerquelle="mit dem Anteil fehlerfreier statt fehlerhafter Chips rechnen")

row(id="2025-GYM-K6c", block="Kontext", aufgabe="6", titel="Computerchip", teilaufgabe="c", seite="8",
    punkte="2", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen",
    stichwoerter="Herstellervergleich|Wurzelziehen|Anteil zurückrechnen", format="Rechnung",
    operator="Zeigen Sie", antwort="Text", material="keins", skizze="keine", kontext="Technik",
    textumfang="kurz", abhaengig_von="2025-GYM-K6a",
    gegeben="Hersteller PAL: Anteil fehlerfreier Chips p %; Wahrscheinlichkeit, dass zwei zufällig "
            "entnommene Chips beide fehlerfrei sind, beträgt 98,01 %; Hersteller LINE: 98,5 % fehlerfrei",
    gesucht="Nachweis, dass PAL einen höheren Anteil fehlerfreier Chips als LINE hat",
    verfahren="(p:100)² = 0,9801 nach p auflösen (Quadratwurzel ziehen) und mit 98,5 % vergleichen",
    schritte="2", zahlenraum="Prozent",
    ergebnis="p = 99 %, und 99 % > 98,5 %, also produziert PAL einen höheren Anteil fehlerfreier Chips",
    niveau_geschaetzt="III",
    fehlerquelle="0,9801 durch 2 teilen statt die Quadratwurzel zu ziehen")
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
