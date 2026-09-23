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
    "jahr": "2024",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "",         # zweiteiliges Heft ab 2019, siehe "dateien"
    "dateien": ["24_P10_Ma_Gym_A1.pdf", "24_P10_Ma_Gym_A2.pdf"],
    "seiten": {"Basis": 3, "Kontext": 9},  # eigene Fußzeile je Teildatei (msa.md § 3)
    "soll": {"1": 5, "2": 5, "3": 13, "4": 12, "5": 6, "6": 9},
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
    ("Geradengleichung einer Parallelen durch einen Punkt bestimmen", "Gleichungen und Funktionen",
     "Lineare Funktionen",
     "Gleichung einer Geraden bestimmen, die parallel zu einer gegebenen (auch erst aus zwei Punkten zu "
     "ermittelnden) Geraden ist und durch einen gegebenen Punkt verläuft.",
     "2024-GYM-B1b"),
    ("Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen", "Größen und Messen",
     "Trigonometrie im rechtwinkligen Dreieck",
     "Eine behauptete Gleichung für sin, cos oder tan eines Winkels im rechtwinkligen Dreieck anhand der "
     "gegebenen Seitenlängen als wahr oder falsch prüfen (typische Verwechslung von Ankathete und "
     "Gegenkathete).",
     "2024-GYM-B2a"),
    ("Dreieck aus Koordinaten als gleichschenklig-rechtwinklig nachweisen", "Raum und Form",
     "Ebene Figuren und Winkel",
     "Für ein durch Koordinaten gegebenes Dreieck nachweisen, dass es gleichschenklig und rechtwinklig "
     "ist, durch Berechnung zweier gleich langer Seiten und Nachweis der Rechtwinkligkeit über das "
     "Skalarprodukt oder über den Mittelpunkt der Hypotenuse (Satz des Thales).",
     "2024-GYM-K3c"),
    ("Sachaufgabe zu einer Gleichungskette formulieren", "Gleichungen und Funktionen",
     "Exponentialfunktionen und Wachstum",
     "Zu einer vorgegebenen Kette von Gleichungen, die gemeinsam eine Sachaufgabe zu einer "
     "Exponentialfunktion lösen, die einzelnen Schritte erläutern und eine passende Aufgabenstellung "
     "formulieren.",
     "2024-GYM-K4c"),
    ("Parameter einer Exponentialfunktion aus einer Wertetabelle bestimmen", "Gleichungen und Funktionen",
     "Exponentialfunktionen und Wachstum",
     "Parameter a (Anfangswert) und b (Wachstumsfaktor) einer Exponentialfunktion g(x) = a·bˣ aus zwei "
     "Wertepaaren einer Tabelle bestimmen und das Wachstumsverhalten im Vergleich zu einer anderen "
     "Exponentialfunktion beschreiben.",
     "2024-GYM-K4d"),
    ("Prozentuale Abweichung eines Werts von einem Vergleichswert berechnen", "Zahlen und Operationen",
     "Prozentrechnung",
     "Prozentuale Abweichung eines gegebenen Werts von einem aus einer Datenreihe (z. B. Diagramm) "
     "ermittelten Vergleichswert (Summe oder Mittelwert) berechnen.",
     "2024-GYM-K5a"),
    ("Mehrere Kenngrößen zweier Datenreihen vergleichend bestimmen", "Daten und Zufall", "Kenngrößen",
     "Für zwei parallele Datenreihen (z. B. ein Jahr im Vergleich zu langjährigen Mittelwerten) mehrere "
     "Kenngrößen (Spannweite, Mittelwert, Median) jeweils bestimmen und gegenüberstellen.",
     "2024-GYM-K5b"),
    ("Winkel als Differenz zweier Teilwinkel in einem zusammengesetzten rechtwinkligen Dreieck "
     "nachweisen", "Raum und Form", "Ebene Figuren und Winkel",
     "In einer aus zwei rechtwinkligen Teildreiecken zusammengesetzten Figur einen Winkel als Differenz "
     "zweier über den jeweiligen Komplementwinkel bzw. eine gegebene Winkelangabe bestimmter Teilwinkel "
     "nachweisen und daraus eine Höhe berechnen.",
     "2024-GYM-K6a"),
]

row(id="2024-GYM-B1a", block="Basis", aufgabe="1", titel="", teilaufgabe="a", seite="2",
    punkte="2", hilfsmittel="nein", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Flächeninhalt eines Dreiecks aus Koordinaten berechnen",
    stichwoerter="Koordinatenursprung|rechtwinkliges Dreieck|Flächeninhalt", format="Rechnung",
    operator="Berechnen Sie", antwort="Zahl", material="keins", skizze="keine", kontext="ohne",
    textumfang="kurz",
    gegeben="Dreieck mit den Eckpunkten O(0|0), A(0|−3) und B(6|0)",
    gesucht="Flächeninhalt des Dreiecks",
    verfahren="OA liegt auf der y-Achse (Länge 3), OB auf der x-Achse (Länge 6), rechter Winkel bei O: "
              "A = 0,5 · 3 · 6", schritte="1", zahlenraum="ganz", einheiten="FE",
    ergebnis="9 FE", niveau_geschaetzt="I",
    fehlerquelle="das Vorzeichen der y-Koordinate von A in die Längenberechnung übernehmen")

row(id="2024-GYM-B1b", block="Basis", aufgabe="1", titel="", teilaufgabe="b", seite="2",
    punkte="3", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Geradengleichung einer Parallelen durch einen Punkt bestimmen",
    typ_neben="Geradengleichung aus zwei Punkten",
    stichwoerter="parallel|Anstieg übernehmen|Punkt", format="Rechnung", operator="Ermitteln Sie",
    antwort="Term", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    abhaengig_von="2024-GYM-B1a",
    gegeben="Gerade g durch A(0|−3) und B(6|0); Gerade h parallel zu g durch S(0|2)",
    gesucht="Gleichung der Geraden h",
    verfahren="Anstieg von g: (0−(−3)):(6−0) = 0,5; h hat denselben Anstieg und den y-Achsenabschnitt "
              "von S", schritte="2", zahlenraum="dezimal",
    ergebnis="h(x) = 0,5x + 2", niveau_geschaetzt="II",
    fehlerquelle="einen neuen, falschen Anstieg statt des Anstiegs von g für h verwenden")

row(id="2024-GYM-B2a", block="Basis", aufgabe="2", titel="", teilaufgabe="a", seite="3",
    punkte="5", hilfsmittel="nein", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Umfang Trapez berechnen",
    typ_neben="Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen",
    stichwoerter="Trapez|Umfang|Kosinus|Verwechslung Ankathete Gegenkathete", format="Rechnung|Begründung",
    operator="Berechnen Sie|Überprüfen Sie", antwort="Zahl|Text", material="Figur",
    skizze="Trapez ABCD, AB ∥ CD, rechte Winkel bei A und D, AD = 8 cm, DC = 4 cm, CB = 10 cm "
           "(Mantellinie/Schenkel), Winkel β bei B", kontext="ohne", textumfang="mittel",
    gegeben="Trapez ABCD mit AB ∥ CD, AD = 8 cm (rechter Winkel zu AB und DC), DC = 4 cm, CB = 10 cm",
    gesucht="Umfang des Trapezes; ob cos(β) = 8:10 gilt",
    verfahren="Hilfsdreieck: Höhe vom Punkt C auf AB (Fußpunkt F) mit CF = AD = 8 cm; FB = "
              "√(CB² − CF²) = √(10² − 8²) = 6 cm; AB = AF + FB = DC + FB = 4 + 6 = 10 cm; Umfang = AB + "
              "BC + CD + DA; cos(β) = Ankathete:Hypotenuse = FB:CB = 6:10, nicht 8:10 (das wäre sin(β))",
    schritte="3", zahlenraum="ganz", einheiten="cm",
    ergebnis="Umfang = 32 cm; die Behauptung cos(β) = 8:10 ist falsch, richtig ist cos(β) = 6:10 (8:10 "
             "ist sin(β))", niveau_geschaetzt="III",
    fehlerquelle="Ankathete und Gegenkathete von β vertauschen und die Behauptung fälschlich bestätigen")

row(id="2024-GYM-K3a", block="Kontext", aufgabe="3", titel="Quadratische Funktion", teilaufgabe="a",
    seite="2", punkte="3", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Nullstellen quadratische Funktion berechnen",
    stichwoerter="Nullstellen|pq-Formel", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x² + 4x + 3",
    gesucht="Nullstellen von f",
    verfahren="pq-Formel oder Faktorisieren: f(x) = (x+1)(x+3)", schritte="1", zahlenraum="ganz",
    ergebnis="x1 = −1, x2 = −3", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichenfehler bei der pq-Formel")

row(id="2024-GYM-K3b", block="Kontext", aufgabe="3", titel="Quadratische Funktion", teilaufgabe="b",
    seite="2", punkte="3", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Funktionswert berechnen", typ_neben="Wertetabelle als Punkte darstellen",
    stichwoerter="y-Achsenabschnitt|Graph zeichnen", format="Kurzantwort|Zeichnen",
    operator="Geben Sie an|Zeichnen Sie", antwort="Term|Grafik", material="Koordinatensystem",
    skizze="nach oben geöffnete Parabel f(x)=x²+4x+3 mit Nullstellen −3 und −1", kontext="ohne",
    textumfang="kurz", abhaengig_von="2024-GYM-K3a",
    gegeben="f(x) = x² + 4x + 3",
    gesucht="Schnittpunkt des Graphen mit der y-Achse; Graph von f mindestens im Intervall [−4;0]",
    verfahren="f(0) berechnen; Wertetabelle im Intervall aufstellen und Punkte verbinden", schritte="1",
    zahlenraum="ganz",
    ergebnis="Schnittpunkt (0|3)", niveau_geschaetzt="I",
    fehlerquelle="das Vorzeichen des konstanten Glieds beim Ablesen des y-Achsenabschnitts vertauschen")

row(id="2024-GYM-K3c", block="Kontext", aufgabe="3", titel="Quadratische Funktion", teilaufgabe="c",
    seite="3", punkte="3", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Dreieck aus Koordinaten als gleichschenklig-rechtwinklig nachweisen",
    stichwoerter="gleichschenklig|rechtwinklig|Mittelpunkt|Skalarprodukt", format="Begründung",
    operator="Begründen Sie", antwort="Text", material="Koordinatensystem",
    skizze="Punkte A(−3|0), B(−1|0), C(−2|−1) auf dem Graphen von f, M Mittelpunkt von AB",
    kontext="ohne", textumfang="mittel", abhaengig_von="2024-GYM-K3a",
    gegeben="A(−3|0), B(−1|0), C(−2|−1) auf dem Graphen von f; M Mittelpunkt von AB",
    gesucht="Nachweis, dass Dreieck ABC gleichschenklig und rechtwinklig ist",
    verfahren="AC = BC = √2 (gleich lange Schenkel); Skalarprodukt der Vektoren CA und CB ist 0, also "
              "rechter Winkel bei C; alternativ: M(−2|0), CM = 1 = AB:2, nach dem Satz des Thales liegt "
              "C auf dem Kreis über AB, also rechter Winkel bei C", schritte="2", zahlenraum="Wurzel",
    ergebnis="AC = BC = √2, rechter Winkel bei C (Skalarprodukt 0 bzw. CM = AB:2), also gleichschenklig-"
             "rechtwinklig", niveau_geschaetzt="III",
    fehlerquelle="die Rechtwinkligkeit ohne Nachweis (z. B. nur aus der Zeichnung) behaupten")

row(id="2024-GYM-K3d", block="Kontext", aufgabe="3", titel="Quadratische Funktion", teilaufgabe="d",
    seite="3", punkte="4", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parabelgleichung aus zwei Nullstellen aufstellen und Nullstellen bestätigen",
    stichwoerter="Produktform|Nullstellen vorgegeben|Koeffizientenvergleich", format="Rechnung",
    operator="Ermitteln Sie", antwort="Zahl", material="keins", skizze="keine", kontext="ohne",
    textumfang="kurz",
    gegeben="g(x) = x² + px + q mit p,q ∈ ℝ; Nullstellen x1 = −2 und x2 = 1",
    gesucht="Werte für p und q",
    verfahren="Produktform g(x) = (x+2)(x−1) ausmultiplizieren und mit x²+px+q vergleichen", schritte="2",
    zahlenraum="ganz",
    ergebnis="p = 1, q = −2", niveau_geschaetzt="II",
    fehlerquelle="beim Ausmultiplizieren von (x+2)(x−1) ein Vorzeichen vertauschen")

row(id="2024-GYM-K4a", block="Kontext", aufgabe="4", titel="Fruchtfliegen", teilaufgabe="a", seite="4",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Funktionswert berechnen",
    stichwoerter="Anfangswert|Exponentialfunktion", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="keins", skizze="keine", kontext="Biologie", textumfang="kurz",
    gegeben="f(x) = 200 · 2,5^x für x ≥ 0, x in Tagen",
    gesucht="Anzahl der Fruchtfliegen zu Beginn des Versuchs",
    verfahren="f(0) berechnen", schritte="1", zahlenraum="ganz",
    ergebnis="200 Fruchtfliegen", niveau_geschaetzt="I",
    fehlerquelle="den Vorfaktor 200 mit dem Wachstumsfaktor 2,5 verwechseln")

row(id="2024-GYM-K4b", block="Kontext", aufgabe="4", titel="Fruchtfliegen", teilaufgabe="b", seite="4",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Funktionswert berechnen",
    stichwoerter="Fruchtfliegen|Funktionswert", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="Biologie", textumfang="kurz",
    abhaengig_von="2024-GYM-K4a",
    gegeben="f(x) = 200 · 2,5^x",
    gesucht="Anzahl der Fruchtfliegen nach 6 Tagen",
    verfahren="f(6) berechnen", schritte="1", zahlenraum="dezimal",
    ergebnis="f(6) = 48 828,125, also rund 48 828 Fruchtfliegen", niveau_geschaetzt="I",
    fehlerquelle="6 mit dem Vorfaktor statt als Exponenten verwenden")

row(id="2024-GYM-K4c", block="Kontext", aufgabe="4", titel="Fruchtfliegen", teilaufgabe="c", seite="4",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Sachaufgabe zu einer Gleichungskette formulieren",
    stichwoerter="Logarithmus|Rückwärtsaufgabe|Aufgabenstellung formulieren", format="Begründung",
    operator="Erläutern Sie", antwort="Text", material="keins", skizze="keine", kontext="Biologie",
    textumfang="mittel", abhaengig_von="2024-GYM-K4a",
    gegeben="Gleichungskette: (1) 500 000 = 200 · 2,5^x; (2) x = log_2,5(2500); (3) x ≈ 9",
    gesucht="Erläuterung der drei Gleichungen; passende Aufgabenstellung",
    verfahren="Gleichung (1) setzt f(x) mit dem Zielwert 500 000 gleich; Division durch 200 und "
              "Logarithmieren zur Basis 2,5 liefert (2); (3) ist der gerundete Zahlenwert",
    schritte="1",
    ergebnis="Aufgabenstellung z. B.: „Bestimmen Sie, nach wie vielen Tagen sich die Population auf "
             "500 000 Fruchtfliegen vermehrt hat.“ – Antwort: nach etwa 9 Tagen", niveau_geschaetzt="III",
    fehlerquelle="die Bedeutung des Logarithmus in Gleichung (2) nicht erklären, sondern nur das "
                 "Ergebnis (3) wiederholen")

row(id="2024-GYM-K4d", block="Kontext", aufgabe="4", titel="Fruchtfliegen", teilaufgabe="d", seite="5",
    punkte="5", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Parameter einer Exponentialfunktion aus einer Wertetabelle bestimmen",
    stichwoerter="Wachstumsfaktor|Wertetabelle|Wachstumsvergleich", format="Rechnung|Begründung",
    operator="Bestimmen Sie|Beschreiben Sie", antwort="Term|Text", material="Tabelle",
    skizze="keine", kontext="Biologie", textumfang="mittel", abhaengig_von="2024-GYM-K4a",
    gegeben="g(x) = a · b^x; Tabelle: g(0) = 550, g(6) = 25 875",
    gesucht="Gleichung von g; Beschreibung des Effekts der geänderten Bedingungen",
    verfahren="a = g(0) = 550; b^6 = 25875:550 = 47,045..., also b = ⁶√47,045...; Vergleich von b mit "
              "dem Wachstumsfaktor 2,5 aus Teilaufgabe a", schritte="2", zahlenraum="dezimal",
    ergebnis="g(x) = 550 · 1,9^x; die geänderten Bedingungen führten zu einem langsameren Wachstum "
             "(Faktor 1,9 statt 2,5), aber weiterhin zu einem größeren Anfangswert (550 statt 200)",
    niveau_geschaetzt="III",
    fehlerquelle="beim Wurzelziehen die sechste Wurzel mit einer Division durch 6 verwechseln")

row(id="2024-GYM-K5a", block="Kontext", aufgabe="5", titel="Wasser - eine wertvolle Ressource",
    teilaufgabe="a", seite="6", punkte="3", leitidee="Zahlen und Operationen", thema="Prozentrechnung",
    typ="Prozentuale Abweichung eines Werts von einem Vergleichswert berechnen",
    stichwoerter="Niederschlag|langjährige Mittelwerte|Abweichung", format="Rechnung",
    operator="Ermitteln Sie", antwort="Zahl", material="Diagramm",
    skizze="Säulendiagramm der langjährigen monatlichen Mittelwerte des Niederschlags (Januar bis "
           "Dezember): 61, 49, 57, 58, 71, 85, 78, 77, 61, 56, 66, 70 Liter je Quadratmeter",
    kontext="Umwelt", textumfang="kurz",
    gegeben="Summe der langjährigen Monatsmittelwerte (aus dem Diagramm): 789 L/m²; Niederschlag 2022: "
            "675 L/m²",
    gesucht="prozentuale Abweichung des Jahres 2022 von der Summe der langjährigen Mittelwerte",
    verfahren="(675 − 789) : 789 · 100 %", schritte="2", zahlenraum="dezimal", einheiten="L/m²|Prozent",
    ergebnis="≈ −14,4 % (also rund 14,4 % weniger Niederschlag als im langjährigen Mittel)",
    niveau_geschaetzt="III",
    fehlerquelle="die Monatswerte im Diagramm falsch ablesen oder addieren, oder die Abweichung auf 675 "
                 "statt auf 789 beziehen")

row(id="2024-GYM-K5b", block="Kontext", aufgabe="5", titel="Wasser - eine wertvolle Ressource",
    teilaufgabe="b", seite="7", punkte="3", leitidee="Daten und Zufall", thema="Kenngrößen",
    typ="Mehrere Kenngrößen zweier Datenreihen vergleichend bestimmen",
    stichwoerter="Spannweite|Mittelwert|Median|Klimavergleich", format="Rechnung",
    operator="Bestimmen Sie", antwort="Zahl", material="Tabelle|Diagramm",
    skizze="wie 2024-GYM-K5a; zusätzlich Tabelle der Monatswerte 2022: 60, 80, 20, 55, 50, 60, 35, 50, "
           "100, 50, 50, 65", kontext="Umwelt", textumfang="mittel", abhaengig_von="2024-GYM-K5a",
    gegeben="Monatswerte 2022 (Summe 675 L/m²) und langjährige Monatsmittelwerte (Summe 789 L/m², aus "
            "Teilaufgabe a)",
    gesucht="drei Kennwerte von 2022 im Vergleich zu den langjährigen Mittelwerten",
    verfahren="Spannweite, arithmetisches Mittel und Median beider Reihen berechnen und gegenüberstellen",
    schritte="3", zahlenraum="dezimal", einheiten="L/m²",
    ergebnis="Spannweite 2022 = 80 (langjährig 36); Mittelwert 2022 = 56,25 (langjährig 65,75); Median "
             "2022 = 52,5 (langjährig 63,5) – 2022 zeigt größere Schwankungen bei insgesamt weniger "
             "Niederschlag", niveau_geschaetzt="III",
    fehlerquelle="beim Median die unsortierte Liste verwenden")

row(id="2024-GYM-K6a", block="Kontext", aufgabe="6", titel="Marder", teilaufgabe="a", seite="8",
    punkte="5", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Winkel als Differenz zweier Teilwinkel in einem zusammengesetzten rechtwinkligen Dreieck "
        "nachweisen",
    typ_neben="Winkel im rechtwinkligen Dreieck berechnen",
    stichwoerter="Wildkamera|zusammengesetztes Dreieck|Höhe", format="Rechnung|Rechnung",
    operator="Zeigen Sie|Berechnen Sie", antwort="Text|Zahl", material="Figur",
    skizze="Wildkamera in Höhe h am Baum bei D über C (rechter Winkel bei C); A und B liegen auf der "
           "Standlinie, AB = 8 m (Aufnahmebereich); Winkel bei A zwischen AB und AD = 6,3°; Winkel bei D "
           "zwischen DC und DB = 60°; nicht maßstabsgerecht",
    kontext="Natur/Umwelt", textumfang="mittel",
    gegeben="rechtwinkliges Dreieck ACD (rechter Winkel bei C) mit Winkel bei A = 6,3°; Winkel BDC = 60° "
            "im Teildreieck BCD (rechter Winkel bei C); AB = 8 m",
    gesucht="Nachweis, dass Winkel ADB = 23,7° beträgt; Höhe h der Wildkamera",
    verfahren="Winkel ADC = 90° − 6,3° = 83,7° (Winkelsumme im Dreieck ACD); Winkel ADB = Winkel ADC − "
              "Winkel BDC = 83,7° − 60°; für die Höhe: AC = h:tan(6,3°) und BC = h·tan(60°), mit AC = AB "
              "+ BC ergibt sich h aus 8 = h:tan(6,3°) − h·tan(60°)", schritte="3", zahlenraum="dezimal",
    einheiten="Grad|m", ergebnis="Winkel ADB = 23,7° bestätigt; h ≈ 1,09 m", niveau_geschaetzt="III",
    fehlerquelle="AC mit AB gleichsetzen und BC bei der Streckenaddition vergessen")

row(id="2024-GYM-K6b", block="Kontext", aufgabe="6", titel="Marder", teilaufgabe="b", seite="9",
    punkte="2", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Wahrscheinlichkeit mehrstufig unabhängig",
    stichwoerter="Marder|Gegenwahrscheinlichkeit|unabhängige Nächte", format="Rechnung",
    operator="Berechnen Sie", antwort="Zahl", material="keins", skizze="keine", kontext="Natur/Umwelt",
    textumfang="kurz",
    gegeben="an 20 % der Nächte wird mindestens ein Marder fotografiert; drei aufeinanderfolgende, "
            "unabhängige Nächte",
    gesucht="Wahrscheinlichkeit, dass an keiner der drei Nächte ein Marder fotografiert wird",
    verfahren="P(kein Marder an einer Nacht) = 1 − 0,2 = 0,8; für drei unabhängige Nächte: 0,8³",
    schritte="1", zahlenraum="Prozent",
    ergebnis="0,8³ = 0,512 = 51,2 %", niveau_geschaetzt="II",
    fehlerquelle="0,2³ statt 0,8³ berechnen")

row(id="2024-GYM-K6c", block="Kontext", aufgabe="6", titel="Marder", teilaufgabe="c", seite="9",
    punkte="2", leitidee="Daten und Zufall", thema="Zählen und Kombinatorik",
    typ="Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen",
    stichwoerter="Wochentage|Ankreuzen|Kombination", format="Rechnung", operator="Ermitteln Sie",
    antwort="Zahl", material="Tabelle", skizze="keine", kontext="Natur/Umwelt", textumfang="kurz",
    gegeben="7 Wochentage, davon werden 4 verschiedene angekreuzt (Reihenfolge ohne Bedeutung)",
    gesucht="Anzahl der Möglichkeiten, 4 von 7 Wochentagen anzukreuzen",
    verfahren="Kombination ohne Wiederholung: C(7,4)", schritte="1", zahlenraum="ganz",
    ergebnis="35 Möglichkeiten", niveau_geschaetzt="II",
    fehlerquelle="die Reihenfolge der angekreuzten Tage mitzählen und mit der Variationenformel statt "
                 "der Kombinationsformel rechnen")
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
