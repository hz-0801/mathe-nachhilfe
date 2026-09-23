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
    "jahr": "2018",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "18_P10_Ma_Gym_A.pdf",  # einteiliges Heft (2014–2018 ein Heft, msa.md § 3)
    "dateien": [],
    "seiten": 11,
    "soll": {"1": 10, "2": 11, "3": 10, "4": 8, "5": 11},
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
    ("Wertebereich einer Funktion angeben", "Gleichungen und Funktionen", "Exponentialfunktionen und Wachstum",
     "Wertebereich einer Exponentialfunktion angeben (stets positiv, unabhängig vom Exponenten).",
     "2018-GYM-K2a"),
    ("Graph einer Exponentialfunktion an der y-Achse spiegeln", "Gleichungen und Funktionen",
     "Exponentialfunktionen und Wachstum",
     "Graph und Gleichung einer Exponentialfunktion nach Spiegelung an der y-Achse angeben (der Exponent "
     "wechselt das Vorzeichen, aus a^x wird (1/a)^x).",
     "2018-GYM-K2c"),
    ("Geradengleichung aus Steigung und Punkt bestimmen", "Gleichungen und Funktionen", "Lineare Funktionen",
     "Gleichung einer Geraden aus einer gegebenen Steigung und einem Punkt, durch den sie verläuft, durch "
     "Einsetzen bestimmen.",
     "2018-GYM-K2d"),
    ("Neigungswinkel einer Geraden berechnen", "Größen und Messen", "Trigonometrie im rechtwinkligen Dreieck",
     "Winkel, den eine Gerade mit der x-Achse einschließt, aus dem Betrag ihrer Steigung über den Tangens "
     "berechnen.",
     "2018-GYM-K2d"),
    ("Höhe eines Drachenvierecks aus geteiltem Winkel und Diagonalen berechnen", "Größen und Messen",
     "Trigonometrie im rechtwinkligen Dreieck",
     "Länge einer Diagonale eines Drachenvierecks (als Summe zweier Abschnitte) aus der anliegenden Diagonale, "
     "dem vollen Winkel an einer Spitze und der Bedingung berechnen, dass beide Diagonalenabschnitte "
     "denselben Fußpunkt auf der anderen Diagonale haben (zwei rechtwinklige Teildreiecke mit gemeinsamer "
     "Kathete).",
     "2018-GYM-K4a"),
    ("Ereignis zu Wahrscheinlichkeitsterm beschreiben", "Daten und Zufall", "Wahrscheinlichkeit mehrstufig",
     "Zu einem gegebenen Wahrscheinlichkeitsterm (Produkt von Bruchfaktoren) das zugehörige mehrstufige "
     "Zufallsereignis in Worten beschreiben (Umkehrung der üblichen Aufgabenstellung).",
     "2018-GYM-K4c"),
    ("Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen", "Gleichungen und Funktionen",
     "Quadratische Funktionen",
     "Begründen, warum eine vorgeschlagene Funktionsgleichung (falscher Funktionstyp oder falsche "
     "Öffnungsrichtung bzw. falscher Koeffizient) einen beschriebenen Kurvenverlauf nicht darstellen kann.",
     "2018-GYM-K5a"),
    ("Parabelgleichung aus Spannweite und Höhe eines Bogens bestimmen", "Gleichungen und Funktionen",
     "Quadratische Funktionen",
     "In einem an der Symmetrieachse ausgerichteten Koordinatensystem die Koordinaten eines Randpunkts "
     "angeben und die Gleichung der Parabel (Scheitel im Ursprung) aus Spannweite und Bogenhöhe bestimmen.",
     "2018-GYM-K5b"),
    ("Wahrscheinlichkeit für die Position des ersten Treffers berechnen", "Daten und Zufall",
     "Wahrscheinlichkeit mehrstufig",
     "Wahrscheinlichkeit berechnen, dass das erste Element eines bestimmten Typs innerhalb einer zufälligen "
     "Reihenfolge an einer von mehreren möglichen frühen Positionen auftritt (Summe der Einzelwahrscheinlich"
     "keiten je Position).",
     "2018-GYM-K5d"),
]

row(id="2018-GYM-B1a", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="a", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Brüche und Dezimalzahlen", typ="Bruchteil einer Größe berechnen",
    stichwoerter="Bruchteil|Masse|Kilogramm", format="Kurzantwort", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="3/4 von 1,2 kg", gesucht="Wert des Bruchteils", verfahren="1,2 kg · 3/4", schritte="1",
    zahlenraum="Bruch|dezimal", einheiten="kg", ergebnis="0,9 kg", niveau_geschaetzt="I",
    fehlerquelle="1,2 durch 4 statt mit 3 zu multiplizieren, das Ergebnis der Multiplikation vergessen")

row(id="2018-GYM-B1b", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="b", seite="2",
    punkte="1", leitidee="Größen und Messen", thema="Einheiten umrechnen", typ="Strecke aus Teilstrecken berechnen",
    stichwoerter="Stab|absägen|Restlänge", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Handwerk", textumfang="kurz",
    gegeben="5 m langer Stab, fünf Teile von je 30 cm werden abgesägt", gesucht="restliche Stablänge",
    verfahren="5 m − 5·30 cm = 500 cm − 150 cm", schritte="2", zahlenraum="ganz|dezimal", einheiten="m|cm",
    ergebnis="3,5 m", niveau_geschaetzt="I", fehlerquelle="nur ein Teilstück (30 cm) statt fünf abziehen")

row(id="2018-GYM-B1c", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="c", seite="2",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Lineare Gleichungen", typ="Lösung durch Einsetzen prüfen",
    stichwoerter="Gleichung|Probe|Einsetzen", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="vier Gleichungen: 4x−8=0; 2x+10=2; 5x+12=2; −2x+4=0; gesucht ist x=−2",
    gesucht="Gleichung, für die x=−2 gilt", verfahren="x=−2 in jede Gleichung einsetzen und prüfen",
    schritte="4", zahlenraum="negativ", ergebnis="5x + 12 = 2", niveau_geschaetzt="I",
    fehlerquelle="nur eine Gleichung nach x auflösen statt alle durch Einsetzen zu prüfen")

row(id="2018-GYM-B1d", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="d", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Prozentrechnung", typ="Größen vergleichen",
    stichwoerter="Prozent|Dezimalzahl|Vergleich", format="Eintragen", operator="Setzen Sie ein", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="5 % und 0,5", gesucht="richtiges Vergleichszeichen (<, > oder =)",
    verfahren="5 % = 0,05; 0,05 < 0,5", schritte="1", zahlenraum="Prozent|dezimal", ergebnis="5 % < 0,5",
    niveau_geschaetzt="I", fehlerquelle="5 % direkt mit 5 statt mit 0,05 vergleichen")

row(id="2018-GYM-B1e", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="e", seite="2",
    punkte="1", leitidee="Größen und Messen", thema="Einheiten umrechnen", typ="Zeiteinheiten umrechnen",
    stichwoerter="Stunden|Minuten|Dezimalzeit", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="3,5 h", gesucht="Angabe in Minuten", verfahren="3,5 · 60", schritte="1", zahlenraum="dezimal",
    einheiten="h|min", ergebnis="210 min", niveau_geschaetzt="I",
    fehlerquelle="3,5 h als 3 h 50 min statt 3 h 30 min lesen")

row(id="2018-GYM-B1f", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="f", seite="2",
    punkte="1", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang", typ="Rechteckseite aus Umfang berechnen",
    stichwoerter="Rechteck|Umfang|Seite", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Figur", skizze="Rechteck mit Seite a=8 cm unten, Seite b rechts gesucht", kontext="ohne",
    textumfang="kurz", gegeben="Rechteck mit Umfang u=26 cm, Seite a=8 cm", gesucht="Länge der Seite b",
    verfahren="u = 2a+2b; b = (26−2·8):2 = 13−8", schritte="2", zahlenraum="ganz", einheiten="cm",
    ergebnis="5 cm", niveau_geschaetzt="II", fehlerquelle="den Umfang direkt durch 2 teilen und a nicht abziehen")

row(id="2018-GYM-B1g", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="g", seite="3",
    punkte="1", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Winkelfunktion Seitenverhältnis angeben",
    stichwoerter="Sinus|Kosinus|rechtwinkliges Dreieck", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="Figur",
    skizze="rechtwinkliges Dreieck mit rechtem Winkel unten links, Kathete b links, Hypotenuse a oben "
           "(von links nach rechts), Winkel β unten rechts",
    kontext="ohne", textumfang="kurz",
    gegeben="rechtwinkliges Dreieck mit Katheten und Hypotenuse a, gesuchter Winkel β; drei Gleichungen zur "
            "Auswahl",
    gesucht="zur Berechnung von β geeignete Gleichung",
    verfahren="Gegenkathete zu β ist b, Hypotenuse ist a: sin β = Gegenkathete : Hypotenuse", schritte="1",
    ergebnis="sin β = b/a", niveau_geschaetzt="II",
    fehlerquelle="Ankathete und Gegenkathete vertauschen (cos β = a/b wählen)")

row(id="2018-GYM-B1h", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="h", seite="3",
    punkte="1", leitidee="Raum und Form", thema="Symmetrie und Abbildungen", typ="Figur nach Spiegelung benennen",
    stichwoerter="Spiegelung|Dreieck|Viereck", format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Figur", skizze="schmales Dreieck, an einer seiner Seiten (Gerade g) gespiegelt", kontext="ohne",
    textumfang="kurz",
    gegeben="Dreieck wird an einer seiner Seiten (Gerade g) gespiegelt",
    gesucht="Name des aus Original und Spiegelbild entstehenden Vierecks",
    verfahren="Spiegelung an einer Dreiecksseite erzeugt zwei Paare gleich langer Nachbarseiten", schritte="1",
    ergebnis="Drachenviereck", niveau_geschaetzt="II",
    fehlerquelle="„Raute“ statt „Drachenviereck“ angeben, ohne zu prüfen, ob alle vier Seiten gleich lang sind")

row(id="2018-GYM-B1i", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="i", seite="3",
    punkte="1", leitidee="Raum und Form", thema="Körper, Netze, Schrägbilder", typ="Körper aus Netz oder Schrägbild benennen",
    stichwoerter="Netz|Tetraeder|Pyramide", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="Figur", skizze="großes gleichseitiges Dreieck, durch Verbindung der Seitenmitten in vier "
                             "kongruente kleinere Dreiecke unterteilt", kontext="ohne", textumfang="kurz",
    gegeben="Netz aus vier kongruenten Dreiecken; Auswahl Prisma, Pyramide, Quader",
    gesucht="zugehöriger Körper", verfahren="vier Dreiecke als Netz eines Tetraeders (dreiseitige Pyramide)",
    schritte="1", ergebnis="Pyramide", niveau_geschaetzt="II",
    fehlerquelle="die Dreiecksform pauschal mit „Prisma“ statt mit dem passenden Pyramidennetz verbinden")

row(id="2018-GYM-B1j", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="j", seite="3",
    punkte="1", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit einstufig", typ="Zufallsgerät zu Wahrscheinlichkeit entwerfen",
    stichwoerter="Glücksrad|Laplace|rote Felder", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Foto", skizze="keine", kontext="Glücksspiel", textumfang="kurz",
    gegeben="Glücksrad mit 5 gleich großen Feldern (rot, grün, weiß), P(rot)=40 %",
    gesucht="Anzahl der roten Felder", verfahren="40 % von 5 Feldern", schritte="1", zahlenraum="ganz|Prozent",
    ergebnis="2 Felder", niveau_geschaetzt="I", fehlerquelle="40 % direkt als Feldanzahl übernehmen")

row(id="2018-GYM-K2a", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="a", seite="4",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Wertebereich einer Funktion angeben",
    stichwoerter="Exponentialfunktion|Wertebereich", format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze="Graph von f(x)=1,5^x, streng monoton steigend, durch (0|1)",
    kontext="ohne", textumfang="kurz", gegeben="f(x) = 1,5^x, x ∈ ℝ", gesucht="Wertebereich von f",
    verfahren="Exponentialfunktion liefert für jedes x nur positive Werte", schritte="1",
    ergebnis="f(x) > 0 für alle x (Wertebereich: alle positiven reellen Zahlen)", niveau_geschaetzt="II",
    fehlerquelle="den Wertebereich mit dem Definitionsbereich (alle reellen Zahlen) verwechseln")

row(id="2018-GYM-K2b", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="b", seite="4",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Zeit aus Exponentialgleichung berechnen",
    stichwoerter="Exponentialgleichung|Logarithmus|x-Koordinate", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Punkt P(x|1000) liegt auf dem Graphen von f(x)=1,5^x", gesucht="x-Koordinate von P",
    verfahren="1,5^x = 1000; x = log(1000) : log(1,5)", schritte="2", zahlenraum="dezimal",
    abhaengig_von="2018-GYM-K2a", ergebnis="x ≈ 17,04", niveau_geschaetzt="III",
    fehlerquelle="1000 durch 1,5 dividieren statt zu logarithmieren")

row(id="2018-GYM-K2c", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="c", seite="5",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Graph einer Exponentialfunktion an der y-Achse spiegeln",
    stichwoerter="Spiegelung|y-Achse|Exponentialfunktion", format="Zeichnen|Kurzantwort",
    operator="Zeichnen Sie|Geben Sie an", antwort="Grafik|Term", material="Koordinatensystem",
    skizze="Spiegelbild f* von f an der y-Achse einzeichnen: streng monoton fallende Kurve durch (0|1), "
           "symmetrisch zu f",
    kontext="ohne", textumfang="mittel", gegeben="Graph f wird an der y-Achse gespiegelt",
    gesucht="gespiegelter Graph f*; zugehörige Funktionsgleichung",
    verfahren="Spiegelung an der y-Achse ersetzt x durch −x: f*(x) = 1,5^(−x) = (2/3)^x", schritte="1",
    abhaengig_von="2018-GYM-K2a", ergebnis="f*(x) = 1,5^(−x) = (2/3)^x", niveau_geschaetzt="II",
    fehlerquelle="den Exponenten unverändert lassen und nur das Vorzeichen der Funktionswerte wechseln")

row(id="2018-GYM-K2d", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="d", seite="5",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Geradengleichung aus Steigung und Punkt bestimmen",
    typ_neben="Gerade aus Gleichung zeichnen|Neigungswinkel einer Geraden berechnen",
    stichwoerter="Steigung|Schnittpunkt|Neigungswinkel", format="Rechnung|Zeichnen|Rechnung",
    operator="Ermitteln Sie|Stellen Sie dar|Geben Sie an", antwort="Term|Grafik|Zahl",
    material="Koordinatensystem", skizze="Gerade g mit Steigung −3 durch S(1|1,5) in dasselbe Koordinatensystem "
                                         "wie f einzeichnen",
    kontext="ohne", textumfang="lang",
    gegeben="Gerade g mit Anstieg m=−3, schneidet f im Punkt S(1|1,5); die Gerade schließt mit den "
            "Koordinatenachsen eine Dreiecksfläche ein",
    gesucht="Funktionsgleichung von g; Darstellung im Koordinatensystem; Winkel zwischen g und der x-Achse",
    verfahren="1,5 = −3·1+n, n=4,5, also g(x)=−3x+4,5; Neigungswinkel: tan(α)=|−3|, α=arctan(3)", schritte="2",
    zahlenraum="negativ|dezimal", einheiten="Grad", abhaengig_von="2018-GYM-K2a",
    ergebnis="g(x) = −3x + 4,5|Winkel ≈ 71,57°", zwischenergebnis="n = 4,5", niveau_geschaetzt="III",
    fehlerquelle="den stumpfen Nebenwinkel (180°−71,57°) statt den spitzen Neigungswinkel angeben")

row(id="2018-GYM-K2e", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="e", seite="5",
    punkte="2", leitidee="Größen und Messen", thema="Satz des Pythagoras", typ="Streckenlänge aus Koordinaten berechnen",
    stichwoerter="Abstand|Ursprung|Schnittpunkt", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="Punkt S(1|1,5) im selben Koordinatensystem wie f und g", kontext="ohne",
    textumfang="kurz", gegeben="Schnittpunkt S(1|1,5) von f und g", gesucht="Abstand von S zum Koordinatenursprung",
    verfahren="d = √(1²+1,5²)", schritte="1", zahlenraum="Wurzel|dezimal", einheiten="LE",
    abhaengig_von="2018-GYM-K2d", ergebnis="d = √3,25 ≈ 1,80 LE", niveau_geschaetzt="II",
    fehlerquelle="nur eine Koordinate als Abstand angeben")

row(id="2018-GYM-K3a", block="Kontext", aufgabe="3", titel="Goldreserven", teilaufgabe="a", seite="6",
    punkte="2", leitidee="Größen und Messen", thema="Einheiten umrechnen", typ="Volumen aus Masse und Dichte berechnen",
    stichwoerter="Goldmünze|Volumen|Dichte", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Foto", skizze="keine", kontext="Wirtschaft/Rohstoffe", textumfang="mittel",
    gegeben="Goldmünze (Zylinderform) Masse 100 kg, 1 cm³ Gold wiegt 19,3 g",
    gesucht="Volumen der Münze", verfahren="V = m : ϱ = 100 000 g : 19,3 g/cm³", schritte="1",
    zahlenraum="dezimal", einheiten="g|cm³", ergebnis="V ≈ 5 181,35 cm³", niveau_geschaetzt="II",
    fehlerquelle="Durchmesser und Höhe schätzen und das Volumen geometrisch statt über die Dichte berechnen",
    bemerkung="Durchmesser (53 cm) ist für die Volumenberechnung nicht nötig, da Masse und Dichte direkt das "
              "Volumen liefern; er dient nur der Einordnung der Münzgröße.")

row(id="2018-GYM-K3b", block="Kontext", aufgabe="3", titel="Goldreserven", teilaufgabe="b", seite="6",
    punkte="2", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Winkel im rechtwinkligen Dreieck berechnen",
    stichwoerter="Trapez|Goldbarren|Winkel β", format="Begründung", operator="Zeigen Sie rechnerisch", antwort="Zahl",
    material="Figur",
    skizze="gleichschenkliges Trapez (Querschnitt des Barrens): obere Parallelseite 60 mm, untere "
           "Parallelseite 80 mm, Höhe 51,4 mm, Winkel β an der unteren linken Ecke",
    kontext="Wirtschaft/Rohstoffe", textumfang="mittel",
    gegeben="gleichschenkliges Trapez mit Parallelseiten 60 mm und 80 mm, Höhe 51,4 mm",
    gesucht="Nachweis, dass der Winkel β ≈ 79° beträgt",
    verfahren="Überhang je Seite = (80−60):2 = 10 mm; tan(β) = 51,4 : 10; β = arctan(5,14)", schritte="2",
    zahlenraum="dezimal", einheiten="mm|Grad", ergebnis="β ≈ 78,99° ≈ 79°", niveau_geschaetzt="III",
    fehlerquelle="die volle Differenz der Parallelseiten (20 mm) statt des halben Überhangs (10 mm) als "
                 "Ankathete verwenden")

row(id="2018-GYM-K3c", block="Kontext", aufgabe="3", titel="Goldreserven", teilaufgabe="c", seite="7",
    punkte="4", leitidee="Größen und Messen", thema="Volumen und Oberfläche", typ="Volumen Prisma berechnen",
    typ_neben="Masse aus Volumen und Dichte berechnen|Portionen aus Gesamtmenge berechnen",
    stichwoerter="Barren|Prisma|Materialwert", format="Rechnung|Rechnung", operator="Berechnen Sie|Ermitteln Sie",
    antwort="Zahl|Zahl", material="Foto|Figur", skizze="dasselbe Trapezprisma wie in b), Länge 180 mm",
    kontext="Wirtschaft/Rohstoffe", textumfang="mittel",
    gegeben="Trapezquerschnitt aus b), Barrenlänge 180 mm, Dichte 19,3 g/cm³, Materialwert der Münze "
            "entspricht 100 kg Gold",
    gesucht="Masse eines Barrens; Anzahl der Barren mit demselben Materialwert wie die Münze",
    verfahren="Trapezfläche = 0,5·(60+80)·51,4 = 3 598 mm²; V = 3 598·180 mm³ = 647,64 cm³; Masse = 647,64 · "
              "19,3 g; Anzahl = 100 000 g : Barrenmasse",
    schritte="4", zahlenraum="dezimal", einheiten="mm|cm³|g|kg", abhaengig_von="2018-GYM-K3b",
    ergebnis="Barrenmasse ≈ 12 499,45 g ≈ 12,5 kg|8 Barren", zwischenergebnis="V ≈ 647,64 cm³",
    niveau_geschaetzt="III",
    fehlerquelle="die Trapezfläche mit der vollen statt der halben Summe der Parallelseiten berechnen")

row(id="2018-GYM-K3d", block="Kontext", aufgabe="3", titel="Goldreserven", teilaufgabe="d", seite="7",
    punkte="2", leitidee="Daten und Zufall", thema="Diagramme lesen und beurteilen", typ="Wert aus Diagramm ablesen",
    typ_neben="Arithmetisches Mittel berechnen",
    stichwoerter="Goldkurs|Diagramm|Mittelwert", format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie",
    antwort="Zahl|Zahl", material="Diagramm",
    skizze="Liniendiagramm „Hoch und Tief der historischen Goldkursentwicklung“ 2010–2016, US$ pro Feinunze "
           "(0 bis 2000, Gitter 200); Hoch-Kurve mit Maximum bei 2011 (genau auf der 1900-Gitterlinie) und "
           "Endpunkt 2016 „1366,25“; Tief-Kurve mit Endpunkt 2016 „1077,00“",
    kontext="Wirtschaft/Rohstoffe", textumfang="mittel",
    gegeben="Diagramm mit Hoch- und Tief-Goldkurs 2010–2016, 2016 beschriftet mit 1366,25 (Hoch) und 1077,00 "
            "(Tief)",
    gesucht="höchster Goldkurs im abgebildeten Zeitraum; mittlerer Goldwert 2016",
    verfahren="Maximum der Hoch-Kurve bei 2011 an der 1900-Gitterlinie ablesen; Mittelwert 2016 = "
              "(1366,25+1077,00):2",
    schritte="2", zahlenraum="dezimal", einheiten="US$", ergebnis="1900,00 US$ (2011)|1221,625 US$",
    niveau_geschaetzt="II",
    fehlerquelle="den Endwert 2016 (1366,25) statt des Maximums 2011 als höchsten Kurs im gesamten Zeitraum "
                 "angeben")

row(id="2018-GYM-K4a", block="Kontext", aufgabe="4", titel="Drachen", teilaufgabe="a", seite="8",
    punkte="3", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Höhe eines Drachenvierecks aus geteiltem Winkel und Diagonalen berechnen",
    stichwoerter="Drachen|Leiste|Winkel β", format="Begründung", operator="Zeigen Sie rechnerisch", antwort="Zahl",
    material="Figur",
    skizze="Drachenviereck (Drachengerüst) mit den Spitzen oben (T), links (L), rechts (R) und unten (Bo); "
           "die Leisten kreuzen sich rechtwinklig im Punkt M; Kante LT = 51 cm, Winkel β bei L zwischen LT "
           "und der unteren Kante L-Bo",
    kontext="Basteln", textumfang="lang",
    gegeben="Schnurlänge (Umfang) 2,65 m, Kante LT = 51 cm (= Kante RT, Symmetrie), Winkel β bei L = 95,9°",
    gesucht="Nachweis, dass die senkrechte Leiste (T bis Bo) ca. 1 m lang ist",
    verfahren="Kante L-Bo = (265 − 2·51):2 = 81,5 cm (aus dem Umfang); β zerlegt sich in β₁ (bei Dreieck "
              "L-T-M) und β₂ (bei Dreieck L-Bo-M) mit β₁+β₂=95,9° und gemeinsamer Kathete LM: "
              "51·cos(β₁) = 81,5·cos(95,9°−β₁); daraus β₁≈36,22°, β₂≈59,68°; TM=51·sin(β₁)≈30,14 cm, "
              "BoM=81,5·sin(β₂)≈70,35 cm",
    schritte="5", zahlenraum="dezimal", einheiten="cm|Grad", ergebnis="TM+BoM ≈ 100,5 cm ≈ 1 m",
    zwischenergebnis="L-Bo = 81,5 cm; β₁≈36,22°, β₂≈59,68°", niveau_geschaetzt="III",
    fehlerquelle="β als rechten Winkel an M statt als vollen Kantenwinkel bei L deuten und dadurch keine "
                 "lösbare Gleichung aufstellen",
    bemerkung="β=95,9° ist stumpf und kann daher nicht der Winkel im rechtwinkligen Teildreieck L-T-M allein "
              "sein (dort wäre er wegen des rechten Winkels bei M kleiner als 90°); β ist der volle "
              "Kantenwinkel bei L, geteilt durch die waagerechte Leiste LM in β₁ (oben) und β₂ (unten). Das "
              "Ergebnis 100,5 cm ≈ 1 m bei einem auf eine Nachkommastelle gerundeten β bestätigt diese "
              "Deutung.")

row(id="2018-GYM-K4b", block="Kontext", aufgabe="4", titel="Drachen", teilaufgabe="b", seite="9",
    punkte="3", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Seite im rechtwinkligen Dreieck berechnen",
    stichwoerter="waagerechte Leiste|Kathete|Drachen", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze="dieselbe Drachenskizze wie in a)", kontext="Basteln", textumfang="kurz",
    gegeben="Kante LT = 51 cm, Winkel β₁ ≈ 36,22° (aus a)", gesucht="Länge der waagerechten Leiste (L bis R)",
    verfahren="LM = 51·cos(β₁); waagerechte Leiste = 2·LM (Symmetrie)", schritte="2", zahlenraum="dezimal",
    einheiten="cm|Grad", abhaengig_von="2018-GYM-K4a", ergebnis="≈ 82,29 cm", zwischenergebnis="LM ≈ 41,14 cm",
    niveau_geschaetzt="III", fehlerquelle="nur LM statt der doppelten Strecke (L bis R) als Leistenlänge angeben")

row(id="2018-GYM-K4c", block="Kontext", aufgabe="4", titel="Drachen", teilaufgabe="c", seite="9",
    punkte="2", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Ereignis zu Wahrscheinlichkeitsterm beschreiben",
    stichwoerter="Schleifen|ohne Zurücklegen|Ereignis beschreiben", format="Begründung", operator="Beschreiben Sie",
    antwort="Text", material="keins", skizze="keine", kontext="Basteln", textumfang="mittel",
    gegeben="Karton mit sechs roten und zwei blauen Schleifen; P(E) = 6/8 · 5/7 · 4/6 · 3/5 = 3/14",
    gesucht="Beschreibung des Ereignisses E, zu dem dieser Term gehört",
    verfahren="vier Faktoren mit sinkendem Nenner und stets der Anzahl roter Schleifen im Zähler → vier "
              "Ziehungen ohne Zurücklegen, bei denen jedes Mal eine rote Schleife gezogen wird",
    schritte="1", ergebnis="E: Bei viermaligem Ziehen ohne Zurücklegen werden ausschließlich rote Schleifen "
                          "gezogen (die ersten vier gezogenen Schleifen sind rot).", niveau_geschaetzt="III",
    fehlerquelle="den Term als Wahrscheinlichkeit für „mindestens eine rote Schleife“ statt für "
                 "„ausschließlich rote Schleifen“ deuten")

row(id="2018-GYM-K5a", block="Kontext", aufgabe="5", titel="Brücke", teilaufgabe="a", seite="10",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen",
    stichwoerter="Parabelbogen|falsche Gleichung|Hängebrücke", format="Begründung", operator="Begründen Sie",
    antwort="Text", material="Figur", skizze="Hängebrücke mit parabelförmigem Hauptseil zwischen den Punkten "
                                            "A und B, Spannweite 40 m, Höhe 12,5 m", kontext="Bauwesen",
    textumfang="mittel",
    gegeben="vorgeschlagene Gleichungen (1) y=−40x²+12,5 und (2) y=12,5x+40 für den Parabelbogen",
    gesucht="Begründung, warum beide Gleichungen ungeeignet sind",
    verfahren="(1) hat einen negativen, betragsmäßig viel zu großen Koeffizienten (−40 statt eines kleinen "
              "positiven Werts) und öffnet nach unten – ein an den Türmen hochgezogenes, in der Mitte "
              "durchhängendes Seil muss aber nach oben geöffnet sein; (2) ist eine lineare Gleichung ohne "
              "x²-Term und damit überhaupt keine Parabel",
    schritte="2", ergebnis="(1) öffnet in die falsche Richtung (nach unten) und hat einen unpassenden "
                          "Koeffizienten; (2) ist keine quadratische Gleichung, sondern eine Gerade",
    niveau_geschaetzt="III",
    fehlerquelle="nur die fehlende x²-Potenz bei (2) nennen und die falsche Öffnungsrichtung von (1) übersehen")

row(id="2018-GYM-K5b", block="Kontext", aufgabe="5", titel="Brücke", teilaufgabe="b", seite="10",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Parabelgleichung aus Spannweite und Höhe eines Bogens bestimmen",
    stichwoerter="Koordinatensystem|Scheitelpunkt|Parabelgleichung", format="Zeichnen|Kurzantwort|Rechnung",
    operator="Zeichnen Sie|Geben Sie an|Bestimmen Sie", antwort="Grafik|Term|Term", material="Figur",
    skizze="Koordinatensystem in die Brückenskizze einzeichnen: x-Achse entlang der Fahrbahn, y-Achse durch "
           "den Scheitelpunkt (Mitte der Spannweite)",
    kontext="Bauwesen", textumfang="lang",
    gegeben="Spannweite 40 m, Höhe der Punkte A und B über der Fahrbahn 12,5 m",
    gesucht="Koordinatensystem mit x-Achse auf der Fahrbahn und y-Achse durch den Scheitelpunkt; Koordinaten "
            "von A; Parabelgleichung",
    verfahren="Scheitel bei (0|0); A liegt am Rand der Spannweite: A(−20|12,5); Ansatz y=a·x², Einsetzen von "
              "A: 12,5 = a·20², a = 12,5:400 = 1/32",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="m", abhaengig_von="2018-GYM-K5a",
    ergebnis="A(−20|12,5)|y = 1/32 · x² (= 0,03125 · x²)", niveau_geschaetzt="III",
    fehlerquelle="die volle Spannweite (40 m) statt der halben Spannweite (20 m) als x-Koordinate von A "
                 "verwenden")

row(id="2018-GYM-K5c", block="Kontext", aufgabe="5", titel="Brücke", teilaufgabe="c", seite="11",
    punkte="2", leitidee="Daten und Zufall", thema="Zählen und Kombinatorik",
    typ="Anzahl Kombinationen nach dem Zählprinzip bestimmen",
    stichwoerter="Verkehrszählung|Fahrzeugarten|Reihenfolge", format="Rechnung", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Verkehr", textumfang="mittel",
    gegeben="vier Fahrzeugarten (LKW, Bus, Motorrad, PKW), für die ersten beiden gezählten Fahrzeuge ist die "
            "Reihenfolge zu beachten",
    gesucht="Anzahl der Möglichkeiten für die Fahrzeugarten der ersten beiden gezählten Fahrzeuge",
    verfahren="je Position 4 mögliche Fahrzeugarten (Wiederholung möglich, da mehrere Fahrzeuge je Art "
              "vorhanden sind): 4 · 4", schritte="1", zahlenraum="ganz", ergebnis="16", niveau_geschaetzt="II",
    fehlerquelle="Wiederholung ausschließen und mit 4·3=12 statt 4·4=16 rechnen")

row(id="2018-GYM-K5d", block="Kontext", aufgabe="5", titel="Brücke", teilaufgabe="d", seite="11",
    punkte="3", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Wahrscheinlichkeit für die Position des ersten Treffers berechnen",
    stichwoerter="LKW|Position|ohne Zurücklegen", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Verkehr", textumfang="mittel",
    gegeben="20 registrierte Fahrzeuge, davon 5 LKW, zufällige Reihenfolge",
    gesucht="Wahrscheinlichkeit, dass der erste LKW das zweite oder dritte gezählte Fahrzeug ist",
    verfahren="P(2.)=(15/20)·(5/19); P(3.)=(15/20)·(14/19)·(5/18); gesucht ist P(2.)+P(3.), da sich die "
              "Ereignisse ausschließen",
    schritte="3", zahlenraum="Bruch|dezimal", ergebnis="P = 15/76 + 35/228 = 20/57 ≈ 35,09 %",
    zwischenergebnis="P(2.) = 15/76 ≈ 19,74 %; P(3.) = 35/228 ≈ 15,35 %", niveau_geschaetzt="III",
    fehlerquelle="die beiden Wahrscheinlichkeiten multiplizieren statt zu addieren (Ereignisse schließen "
                 "sich gegenseitig aus)")
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
