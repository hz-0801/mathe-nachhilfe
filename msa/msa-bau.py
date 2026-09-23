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
    "jahr": "2015",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "15_P10_Ma_Gym_A.pdf",  # einteiliges Heft (2014–2018 ein Heft, msa.md § 3)
    "dateien": [],
    "seiten": 7,
    "soll": {"1": 10, "2": 11, "3": 10, "4": 10, "5": 9},
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
    ("Graph einer trigonometrischen Funktion durch Streckung und Verschiebung beschreiben",
     "Gleichungen und Funktionen", "Trigonometrische Funktionen",
     "Beschreiben, wie der Graph einer trigonometrischen Funktion durch Streckung in y-Richtung und "
     "Verschiebung aus einer gegebenen trigonometrischen Funktion hervorgeht, und eine passende Gleichung "
     "notieren.",
     "2015-GYM-K2a"),
    ("Eigenschaften trigonometrischer Funktionen vergleichen", "Gleichungen und Funktionen", "Trigonometrische Funktionen",
     "Zwei trigonometrische Funktionen anhand einer unterscheidenden Eigenschaft (z. B. Amplitude, "
     "Wertebereich, Achsenschnittpunkt) vergleichen.",
     "2015-GYM-K2b"),
    ("Umfang eines Dreiecks aus Koordinaten berechnen", "Raum und Form", "Ebene Figuren und Winkel",
     "Umfang eines im Koordinatensystem gegebenen Dreiecks berechnen, indem die drei Seitenlängen aus den "
     "Eckpunktkoordinaten (ggf. über den Satz des Pythagoras) bestimmt und addiert werden.",
     "2015-GYM-K2c"),
    ("Gleichung einer Senkrechten aufstellen", "Gleichungen und Funktionen", "Lineare Funktionen",
     "Gleichung einer Geraden aufstellen, die durch einen gegebenen Punkt verläuft und senkrecht zu einer "
     "gegebenen Strecke oder Geraden ist (Steigung als negativer Kehrwert).",
     "2015-GYM-K2d"),
    ("Kugeloberfläche berechnen", "Größen und Messen", "Volumen und Oberfläche",
     "Oberfläche einer Kugel aus Radius oder Durchmesser mit O = 4 · π · r² berechnen.",
     "2015-GYM-K4c"),
    ("Seite im allgemeinen Dreieck über Kosinussatz berechnen", "Größen und Messen", "Sinussatz",
     "Im allgemeinen Dreieck eine Seite aus den zwei anliegenden Seiten und dem eingeschlossenen Winkel mit "
     "dem Kosinussatz berechnen.",
     "2015-GYM-K5a"),
    ("Sinussatz Winkel berechnen", "Größen und Messen", "Sinussatz",
     "Im allgemeinen Dreieck einen Winkel mit dem Sinussatz aus zwei Seiten und dem einer der Seiten "
     "gegenüberliegenden Winkel berechnen.",
     "2015-GYM-K5b"),
    ("Maximale Anzahl rechteckiger Objekte auf einer Fläche bestimmen", "Größen und Messen", "Flächeninhalt und Umfang",
     "Auf einer rechteckigen Fläche die größtmögliche Anzahl gleich großer rechteckiger Objekte (Längs- oder "
     "Querformat) durch Anordnen bestimmen.",
     "2015-GYM-K5c"),
]

row(id="2015-GYM-B1a", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="a", seite="2",
    punkte="1", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit einstufig",
    typ="Zufallsgerät zu Wahrscheinlichkeit entwerfen",
    stichwoerter="Topf|Laplace|50 Prozent", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="Foto",
    skizze="drei Töpfe mit je 6 Kugeln: Topf 1 vier weiße/zwei dunkle, Topf 2 zwei weiße/vier dunkle, "
           "Topf 3 drei weiße/drei dunkle",
    kontext="Glücksspiel", textumfang="kurz",
    gegeben="drei Töpfe mit je 6 Kugeln in unterschiedlicher Verteilung weiß/dunkel (Topf 1: 4w/2d, Topf 2: "
            "2w/4d, Topf 3: 3w/3d)",
    gesucht="Topf mit P(weiß) = 50 %",
    verfahren="Anteil weißer Kugeln je Topf bilden und mit 50 % vergleichen: 4/6, 2/6, 3/6",
    schritte="1", zahlenraum="Bruch|Prozent", ergebnis="Topf 3 (3 von 6 Kugeln weiß)", niveau_geschaetzt="II",
    fehlerquelle="Topf mit den meisten weißen Kugeln wählen statt den mit dem Anteil 50 %",
    bemerkung="Kugelzahl je Topf (6) durch Auszählen der Abbildung bestimmt, nicht im Text genannt.")

row(id="2015-GYM-B1b", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="b", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Rationale Zahlen rechnen", typ="Zahl zu Bedingung angeben",
    stichwoerter="rationale Zahl|Bedingung|negativ", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Bedingung: Zahl größer als −150", gesucht="eine passende Zahl",
    verfahren="eine beliebige Zahl > −150 wählen, z. B. −140", schritte="1", zahlenraum="negativ",
    ergebnis="−140 (Beispiel; jede Zahl > −150 ist richtig)", niveau_geschaetzt="I",
    fehlerquelle="Betrag statt Vorzeichen vergleichen (z. B. −200 als „größer“ werten)")

row(id="2015-GYM-B1c", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="c", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Brüche und Dezimalzahlen",
    typ="Zahlen in verschiedenen Darstellungen vergleichen",
    stichwoerter="Bruch|Dezimalzahl|Wurzel|Vergleich", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="drei Aussagen: 1,5 < 3/2; 8/5 > 3/2; √2 > 3/2",
    gesucht="wahre Aussage",
    verfahren="alle Werte als Dezimalzahl: 1,5 = 3/2 (also < falsch); 8/5 = 1,6 > 1,5 (wahr); √2 ≈ 1,414 < 1,5 "
              "(falsch)",
    schritte="3", zahlenraum="dezimal|Bruch|Wurzel", ergebnis="8/5 > 3/2", niveau_geschaetzt="II",
    fehlerquelle="1,5 < 3/2 als wahr werten, weil beide Seiten gleich aussehen (Gleichheit übersehen)")

row(id="2015-GYM-B1d", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="d", seite="2",
    punkte="1", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Winkel an geschnittenen Parallelen bestimmen",
    stichwoerter="Parallelen|Transversale|Ergänzungswinkel", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Figur",
    skizze="zwei parallele Geraden h (oben) und g (unten), geschnitten von der senkrechten Geraden k; bei h "
           "der Winkel 53° zwischen k (abwärts) und h, bei g der Winkel α zwischen k (aufwärts) und g, beide "
           "auf derselben Seite von k",
    kontext="ohne", textumfang="kurz",
    gegeben="g ∥ h, Transversale k, Winkel 53° an h zwischen k und h auf der linken Seite",
    gesucht="Winkel α an g auf derselben Seite von k",
    verfahren="α und 53° sind Ergänzungswinkel zwischen den Parallelen auf derselben Seite der Transversale: "
              "α = 180° − 53°",
    schritte="1", zahlenraum="ganz", einheiten="Grad", ergebnis="α = 127°", niveau_geschaetzt="II",
    fehlerquelle="α = 53° setzen (Wechselwinkel statt Ergänzungswinkel)")

row(id="2015-GYM-B1e", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="e", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Zinsrechnung", typ="Prozentwert berechnen",
    stichwoerter="Zinsen|Konto|ein Jahr", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bank/Sparen", textumfang="kurz",
    gegeben="Kontostand 400 €, Zinssatz 2 % im Jahr", gesucht="Zinsen nach einem Jahr",
    verfahren="400 € · 0,02", schritte="1", zahlenraum="ganz|Prozent", einheiten="€", ergebnis="8 €",
    niveau_geschaetzt="I", fehlerquelle="2 € statt 2 % vom Kontostand abziehen")

row(id="2015-GYM-B1f", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="f", seite="2",
    punkte="1", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Median bestimmen",
    stichwoerter="Median|Zentralwert|Messdaten", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Tabelle", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Messdaten 5°C; 7°C; 3°C; 8°C; 1°C; 8°C; 5°C", gesucht="Zentralwert (Median)",
    verfahren="sortieren: 1; 3; 5; 5; 7; 8; 8 (7 Werte), mittlerer Wert (4. von 7)",
    schritte="2", zahlenraum="ganz", einheiten="°C", ergebnis="5 °C", niveau_geschaetzt="I",
    fehlerquelle="ohne Sortieren den mittleren Listenwert nehmen")

row(id="2015-GYM-B1g", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="g", seite="3",
    punkte="1", leitidee="Zahlen und Operationen", thema="Rationale Zahlen rechnen", typ="Vorzeichenregel anwenden",
    stichwoerter="Vorzeichen|Multiplikation|rationale Zahlen", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Multiplikation zweier rationaler Zahlen mit unterschiedlichen Vorzeichen; drei Antwortmöglichkeiten "
            "(immer positiv, immer negativ, nicht entscheidbar)",
    gesucht="wahre Aussage über das Vorzeichen des Ergebnisses",
    verfahren="Vorzeichenregel: Plus mal Minus ergibt immer Minus", schritte="1",
    ergebnis="immer negativ", niveau_geschaetzt="I",
    fehlerquelle="„nicht entscheidbar“ ankreuzen, weil die Beträge unbekannt sind")

row(id="2015-GYM-B1h", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="h", seite="3",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen", typ="Parabel verschieben",
    stichwoerter="Normalparabel|Verschiebung|Scheitelpunkt", format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Koordinatensystem",
    skizze="Koordinatensystem x von −2 bis 2, y von −1 bis 4, Gitter 1; Normalparabel mit Scheitel (0|0)",
    kontext="ohne", textumfang="kurz",
    gegeben="abgebildete Normalparabel, Verschiebung um zwei Einheiten nach rechts",
    gesucht="Koordinaten des Scheitelpunkts der verschobenen Parabel",
    verfahren="Scheitel (0|0) um 2 nach rechts: x-Koordinate +2, y-Koordinate unverändert", schritte="1",
    zahlenraum="ganz", ergebnis="S (2|0)", niveau_geschaetzt="I",
    fehlerquelle="Verschiebung nach rechts als Verschiebung nach oben deuten (S (0|2))")

row(id="2015-GYM-B1i", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="i", seite="3",
    punkte="1", leitidee="Zahlen und Operationen", thema="Potenzen und Wurzeln", typ="Wurzel eines Quadrats berechnen",
    stichwoerter="Wurzel|Quadrat|negative Zahl", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Term √((−4)²); drei Antwortmöglichkeiten (−4, +4, nicht definiert)",
    gesucht="richtige Aussage", verfahren="(−4)² = 16, √16 = 4 (Wurzel ist nie negativ)", schritte="2",
    zahlenraum="negativ", ergebnis="√((−4)²) = +4", niveau_geschaetzt="I",
    fehlerquelle="Quadrieren und Wurzelziehen als sich gegenseitig aufhebend ansehen und −4 ankreuzen")

row(id="2015-GYM-B1j", block="Basis", aufgabe="1", titel="Basisaufgabe", teilaufgabe="j", seite="3",
    punkte="1", leitidee="Zahlen und Operationen", thema="Brüche und Dezimalzahlen", typ="Bruchteil einer Größe berechnen",
    stichwoerter="Bruchteil|Fassungsvermögen|Restmenge", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Haushalt", textumfang="kurz",
    gegeben="Wassertonne 600 Liter Fassungsvermögen, noch zu 2/3 gefüllt", gesucht="nachzufüllende Menge in Litern",
    verfahren="gefüllt: 600 · 2/3 = 400 l; fehlend: 600 − 400", schritte="2", zahlenraum="ganz|Bruch",
    einheiten="l", ergebnis="200 l", zwischenergebnis="gefüllt: 400 l", niveau_geschaetzt="II",
    fehlerquelle="2/3 von 600 als gesuchte Menge angeben, ohne die Differenz zu 600 zu bilden")

row(id="2015-GYM-K2a", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="a", seite="4",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Trigonometrische Funktionen",
    typ="Graph einer trigonometrischen Funktion durch Streckung und Verschiebung beschreiben",
    stichwoerter="Sinusfunktion|Streckung|Verschiebung", format="Begründung|Kurzantwort",
    operator="Beschreiben Sie|Notieren Sie", antwort="Text|Term", material="Koordinatensystem",
    skizze="Koordinatensystem x von −2 bis 6, y von −2 bis 6; durchgezogener Graph f mit Amplitude 2, "
           "Periode 4, Nullstelle bei O; gestrichelter Graph g mit Amplitude 4, Periode 4, "
           "y-Achsenabschnitt P(0|2); Punkt R(5|2) auf f",
    kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 2 · sin(0,5π · x), x ∈ ℝ; Graph von g im selben Koordinatensystem (Maximum 6, Minimum −2, "
            "y-Achsenabschnitt 2)",
    gesucht="Beschreibung der Abbildung f → g; eine mögliche Gleichung von g",
    verfahren="Amplitude verdoppelt sich (2 → 4) und der Graph wird um 2 Einheiten nach oben verschoben: "
              "g(x) = 2 · f(x) + 2",
    schritte="2", ergebnis="Streckung in y-Richtung mit Faktor 2, danach Verschiebung um 2 nach oben|"
                          "g(x) = 4 · sin(0,5π · x) + 2", niveau_geschaetzt="II",
    fehlerquelle="nur die Verschiebung nennen und die Streckung der Amplitude übersehen")

row(id="2015-GYM-K2b", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="b", seite="4",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Trigonometrische Funktionen",
    typ="Eigenschaften trigonometrischer Funktionen vergleichen",
    stichwoerter="Amplitude|Wertebereich|Vergleich", format="Kurzantwort", operator="Nennen Sie", antwort="Text",
    material="Koordinatensystem", skizze="dasselbe Koordinatensystem wie in a)", kontext="ohne", textumfang="kurz",
    gegeben="Graphen von f und g aus a)", gesucht="eine unterscheidende Eigenschaft, für beide Funktionen angegeben",
    verfahren="Amplitude vergleichen: f hat Amplitude 2, g hat Amplitude 4 (bzw. Wertebereich f: [−2;2], "
              "g: [−2;6])",
    schritte="1", abhaengig_von="2015-GYM-K2a",
    ergebnis="f: Amplitude 2 (Wertebereich [−2;2])|g: Amplitude 4 (Wertebereich [−2;6])",
    niveau_geschaetzt="II", fehlerquelle="Periode als Unterscheidungsmerkmal nennen, obwohl sie bei f und g "
                                         "gleich ist")

row(id="2015-GYM-K2c", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="c", seite="4",
    punkte="2", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Umfang eines Dreiecks aus Koordinaten berechnen",
    stichwoerter="Dreieck|Umfang|Koordinaten", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="dasselbe Koordinatensystem wie in a), Dreieck O(0|0), P(0|2), R(5|2)",
    kontext="ohne", textumfang="mittel",
    gegeben="Schnittpunkt P der Funktion g mit der y-Achse, Koordinatenursprung O, Punkt R(5|2); 1 cm = 1 LE",
    gesucht="Umfang des Dreiecks ORP",
    verfahren="OP = 2 (senkrecht); PR = 5 (waagerecht); RO = √(5²+2²) = √29 über Pythagoras; Summe der drei "
              "Seiten",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="LE", abhaengig_von="2015-GYM-K2a",
    ergebnis="Umfang ≈ 12,39 LE", zwischenergebnis="OP = 2 LE; PR = 5 LE; RO = √29 LE ≈ 5,39 LE",
    niveau_geschaetzt="II", fehlerquelle="RO als waagerechte oder senkrechte Strecke ohne Pythagoras schätzen")

row(id="2015-GYM-K2d", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="d", seite="4",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Gleichung einer Senkrechten aufstellen",
    stichwoerter="senkrecht|Steigung|Kehrwert", format="Zeichnen|Kurzantwort", operator="Zeichnen Sie|Geben Sie an",
    antwort="Grafik|Term", material="Koordinatensystem",
    skizze="Gerade h durch P(0|2) mit Steigung −2,5 in dasselbe Koordinatensystem wie g einzeichnen",
    kontext="ohne", textumfang="mittel",
    gegeben="Gerade h verläuft durch P(0|2) und senkrecht zur Dreiecksseite OR (Steigung von OR: 2/5)",
    gesucht="Gerade h im Koordinatensystem; Gleichung von h",
    verfahren="Steigung senkrecht: negativer Kehrwert von 2/5 ist −5/2; h durch P(0|2): y = −2,5x + 2",
    schritte="2", zahlenraum="Bruch|negativ", abhaengig_von="2015-GYM-K2c",
    ergebnis="h(x) = −2,5x + 2", niveau_geschaetzt="III",
    fehlerquelle="Steigung von OR unverändert übernehmen statt den negativen Kehrwert zu bilden")

row(id="2015-GYM-K3a", block="Kontext", aufgabe="3", titel="Klassenfahrt", teilaufgabe="a", seite="5",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen", typ="Graph zu Tarif zuordnen",
    typ_neben="Tarife vergleichen",
    stichwoerter="Tarifvergleich|Buchungsgebühr|Graph", format="Kurzantwort|Begründung|Rechnung",
    operator="Ordnen Sie zu|Entscheiden und begründen Sie|Prüfen Sie", antwort="Text|Text|Zahl",
    material="Diagramm",
    skizze="Koordinatensystem Fahrtkosten in € (0 bis 800) über Fahrtstrecke in km (0 bis 500); zwei Geraden "
           "I und II, II mit höherem y-Achsenabschnitt (200) und flacherer Steigung, I durch den Ursprung mit "
           "steilerer Steigung, Schnittpunkt bei 400 km/800 €",
    kontext="Reise/Vertrag", textumfang="lang",
    gegeben="Eurobus: 200 € Buchungsgebühr + 1,50 €/km; Travelbus: 2,00 €/km ohne Grundgebühr; "
            "Hin- und Rückfahrt 2 · 175 km = 350 km",
    gesucht="Graph von Eurobus; günstigeres Angebot für 350 km; ob das gewählte Angebot bei zusätzlichen "
            "100 km (450 km) weiterhin günstiger ist",
    verfahren="Eurobus (höherer Achsenabschnitt 200, flachere Steigung 1,5) = Graph II; bei 350 km: Eurobus "
              "200+1,5·350=725 €, Travelbus 2·350=700 € → Travelbus günstiger; Schnittpunkt 200+1,5x=2x → "
              "x=400 km; bei 450 km: Eurobus 875 €, Travelbus 900 € → Eurobus jetzt günstiger",
    schritte="4", zahlenraum="dezimal", einheiten="€|km",
    ergebnis="Eurobus = Graph II|Travelbus ist bei 350 km günstiger (700 € gegen 725 €)|nein, ab 400 km wird "
             "Eurobus günstiger, bei 450 km ist Eurobus (875 €) günstiger als Travelbus (900 €)",
    zwischenergebnis="Schnittpunkt bei 400 km / 800 €", niveau_geschaetzt="III",
    fehlerquelle="das für 350 km günstigere Angebot ohne erneute Rechnung auch für 450 km annehmen")

row(id="2015-GYM-K3b", block="Kontext", aufgabe="3", titel="Klassenfahrt", teilaufgabe="b", seite="5",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Lineare Gleichungssysteme",
    typ="Lineares Gleichungssystem lösen", typ_neben="Lineares Gleichungssystem aufstellen",
    stichwoerter="Zimmeranzahl|Gleichungssystem|Betten", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Reise/Vertrag", textumfang="kurz",
    gegeben="16 Zimmer, 66 Betten, Dreibett- und Fünfbettzimmer",
    gesucht="Anzahl der Zimmer je Art",
    verfahren="x+y=16, 3x+5y=66 (x Dreibett-, y Fünfbettzimmer); x=16−y einsetzen: 3(16−y)+5y=66, 2y=18, y=9, "
              "x=7",
    schritte="3", zahlenraum="ganz", einheiten="Zimmer",
    ergebnis="7 Dreibettzimmer, 9 Fünfbettzimmer", niveau_geschaetzt="II",
    fehlerquelle="66 Betten gleichmäßig auf 16 Zimmer verteilen, ohne die zwei Zimmerarten zu unterscheiden")

row(id="2015-GYM-K3c", block="Kontext", aufgabe="3", titel="Klassenfahrt", teilaufgabe="c", seite="5",
    punkte="3", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Wahrscheinlichkeit mehrstufig ohne Zurücklegen",
    stichwoerter="Zimmerlosung|ohne Zurücklegen|Dreibettzimmer", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="keins", skizze="keine", kontext="Reise/Vertrag", textumfang="mittel",
    gegeben="6 Mädchen, zwei Dreibettzimmer, Belegung ausgelost; Lisa zieht zuerst, Petra als zweite",
    gesucht="Wahrscheinlichkeit, dass beide im gleichen Zimmer landen",
    verfahren="nach Lisas Zug bleiben 5 Plätze, davon 2 im selben Zimmer wie Lisa; P = 2/5", schritte="2",
    zahlenraum="Bruch", ergebnis="P = 2/5 = 0,4", niveau_geschaetzt="III",
    fehlerquelle="mit 1/2 (zwei Zimmer zur Auswahl) statt mit den verbleibenden Plätzen rechnen")

row(id="2015-GYM-K4a", block="Kontext", aufgabe="4", titel="Fingerpuppe", teilaufgabe="a", seite="6",
    punkte="2", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Seite im rechtwinkligen Dreieck berechnen",
    stichwoerter="Kegel|Öffnungswinkel|Tangens", format="Begründung", operator="Zeigen Sie durch Rechnung",
    antwort="Zahl", material="Figur", skizze="Kegel (Hut) mit Grundkreisradius 1,73 cm, Öffnungswinkel α=60° an "
                                             "der Spitze, Höhe gesucht", kontext="Basteln", textumfang="mittel",
    gegeben="Hut ist ein Kreiskegel mit Grundkreisradius ≈ 1,73 cm, Öffnungswinkel α = 60°",
    gesucht="Nachweis, dass die Höhe des Huts ≈ 3 cm beträgt",
    verfahren="halber Öffnungswinkel 30° im rechtwinkligen Dreieck aus Höhe und Radius: tan(30°) = r/h, "
              "h = r : tan(30°) = 1,73 : tan(30°)",
    schritte="2", zahlenraum="dezimal", einheiten="cm|Grad", ergebnis="h ≈ 3,00 cm", niveau_geschaetzt="II",
    fehlerquelle="mit dem vollen Öffnungswinkel 60° statt dem halben Winkel 30° rechnen")

row(id="2015-GYM-K4b", block="Kontext", aufgabe="4", titel="Fingerpuppe", teilaufgabe="b", seite="6",
    punkte="5", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Strecke aus Teilstrecken berechnen", typ_neben="Mantelfläche Kegel berechnen|Mantelfläche Zylinder berechnen",
    stichwoerter="Gesamthöhe|Mantelfläche|Zeichenkarton", format="Rechnung|Begründung",
    operator="Berechnen Sie|Entscheiden und begründen Sie", antwort="Zahl|Text", material="Figur",
    skizze="Fingerpuppe von unten nach oben: Zylinder (Rumpf) 6 cm, Kugel (Kopf) Durchmesser 4 cm zu einem "
           "Viertel im Hut verborgen, Kegel (Hut) Höhe 3 cm",
    kontext="Basteln", textumfang="lang",
    gegeben="Rumpf (Zylinder) Höhe 6 cm, gleicher Radius wie der Hut (1,73 cm); Kugel Durchmesser 4 cm, ein "
            "Viertel des Durchmessers verschwindet im Hut; Zeichenkarton 11 cm x 15 cm",
    gesucht="Gesamthöhe der Fingerpuppe; ob der Karton für Hut und Rumpf ausreicht",
    verfahren="Gesamthöhe = Rumpf (6) + sichtbarer Kugelanteil (4 − 1 = 3) + Huthöhe (3) = 12 cm; "
              "Mantelfläche Hut = π·r·s mit s=√(1,73²+3²)≈3,46 cm, ≈18,80 cm²; Mantelfläche Rumpf = 2π·r·6 "
              "≈65,22 cm²; Summe ≈84,02 cm² gegen 165 cm² Karton",
    schritte="4", zahlenraum="dezimal", einheiten="cm|cm²",
    ergebnis="Gesamthöhe 12 cm|ja, der Karton reicht (84,02 cm² Bedarf gegen 165 cm² Fläche)",
    zwischenergebnis="Mantelfläche Hut ≈ 18,80 cm², Mantelfläche Rumpf ≈ 65,22 cm²", niveau_geschaetzt="III",
    fehlerquelle="beim Zuschnitt keine Nesting-Verluste bedenken oder Grund-/Deckfläche fälschlich mitrechnen "
                 "(Hut unten, Rumpf oben und unten offen)")

row(id="2015-GYM-K4c", block="Kontext", aufgabe="4", titel="Fingerpuppe", teilaufgabe="c", seite="6",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche", typ="Kugeloberfläche berechnen",
    typ_neben="Anzahl der Anordnungen bestimmen",
    stichwoerter="Kugeloberfläche|Farbe|Kombinationen", format="Begründung|Rechnung",
    operator="Zeigen Sie|Ermitteln Sie", antwort="Zahl|Zahl", material="Foto", skizze="keine",
    kontext="Basteln", textumfang="mittel",
    gegeben="Kugel (Kopf) Durchmesser 4 cm; gelbe Farbe reicht für ca. 60 cm²; drei Teile (Hut, Kopf, Rumpf) "
            "je eine andere Farbe, Kopf ist gelb, für Hut und Rumpf stehen rot, grün, blau zur Verfügung",
    gesucht="Nachweis, dass die gelbe Farbe für den Kopf reicht; Anzahl möglicher Farbkombinationen",
    verfahren="Kugeloberfläche O = 4·π·r² = 4·π·2² ≈ 50,27 cm² < 60 cm²; für Hut und Rumpf 2 von 3 Farben in "
              "Reihenfolge verteilen: 3 · 2 = 6",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="cm²", abhaengig_von="2015-GYM-K4b",
    ergebnis="Kugeloberfläche ≈ 50,27 cm², reicht|6 Farbkombinationen", niveau_geschaetzt="III",
    fehlerquelle="Kugelvolumen statt Kugeloberfläche berechnen, oder die Kopf-Farbe bei den Kombinationen "
                 "mitzählen")

row(id="2015-GYM-K5a", block="Kontext", aufgabe="5", titel="Solardach", teilaufgabe="a", seite="7",
    punkte="2", leitidee="Größen und Messen", thema="Sinussatz",
    typ="Seite im allgemeinen Dreieck über Kosinussatz berechnen",
    stichwoerter="Kosinussatz|Dachkante|Neigungswinkel", format="Begründung", operator="Zeigen Sie rechnerisch",
    antwort="Zahl", material="Foto|Figur",
    skizze="Hausskizze mit Satteldach; am First zwei Kanten der Länge 6 m und 10 m mit eingeschlossenem "
           "Winkel α=70°, Dachkante s als Gegenseite von α, Winkel β an der Traufe zwischen s und der 10 m "
           "Kante; Ridge-Länge 12 m",
    kontext="Bauwesen", textumfang="mittel",
    gegeben="zwei Dachkanten 6 m und 10 m mit eingeschlossenem Neigungswinkel α = 70°",
    gesucht="Nachweis, dass die Dachkante s ≈ 9,7 m lang ist",
    verfahren="Kosinussatz: s² = 6² + 10² − 2·6·10·cos(70°)", schritte="1", zahlenraum="dezimal",
    einheiten="m|Grad", ergebnis="s ≈ 9,74 m", niveau_geschaetzt="III",
    fehlerquelle="Satz des Pythagoras statt Kosinussatz ansetzen, obwohl kein rechter Winkel vorliegt",
    bemerkung="Thema „Sinussatz“ ersatzweise gewählt wie 2014-GYM-K5b: die Themenliste (msa.md § 6) führt "
              "keine eigene Kosinussatz-Zeile. Deutung der nicht maßstäblichen Skizze: die Zahlenprobe "
              "(6²+10²−2·6·10·cos70°≈94,96, √94,96≈9,74) bestätigt, dass 6 m und 10 m die α einschließenden "
              "Seiten sind und die dritte Seite s ist; „10 m“ ist zugleich die mit der großen Dachfläche "
              "geteilte Kante (Grundlage von c).")

row(id="2015-GYM-K5b", block="Kontext", aufgabe="5", titel="Solardach", teilaufgabe="b", seite="7",
    punkte="2", leitidee="Größen und Messen", thema="Sinussatz", typ="Sinussatz Winkel berechnen",
    stichwoerter="Sinussatz|Neigungswinkel|Modul", format="Rechnung", operator="Prüfen Sie", antwort="Zahl",
    material="Figur", skizze="dasselbe Dreieck wie in a)", kontext="Bauwesen", textumfang="kurz",
    gegeben="Dreieck mit Seiten 6 m, 10 m, s≈9,74 m und Winkel α=70° gegenüber s; optimaler Neigungswinkel β "
            "der Module zwischen 30° und 40°",
    gesucht="Winkel β und ob er im Bereich 30°–40° liegt",
    verfahren="Sinussatz: sin(β)/6 = sin(70°)/9,74; β = arcsin(6·sin(70°)/9,74)", schritte="2",
    zahlenraum="dezimal", einheiten="m|Grad", abhaengig_von="2015-GYM-K5a",
    ergebnis="β ≈ 35,4°, liegt im Bereich 30°–40° → Bedingung erfüllt", niveau_geschaetzt="III",
    fehlerquelle="6 und 10 in der Sinussatz-Gleichung vertauschen (falscher Gegenwinkel)")

row(id="2015-GYM-K5c", block="Kontext", aufgabe="5", titel="Solardach", teilaufgabe="c", seite="7",
    punkte="3", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Maximale Anzahl rechteckiger Objekte auf einer Fläche bestimmen",
    stichwoerter="Solarmodule|Längsformat|Querformat", format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Foto", skizze="größere (dunkle) Dachfläche 12 m x 10 m", kontext="Bauwesen", textumfang="mittel",
    gegeben="größere Dachfläche 12 m x 10 m (a) ergänzt); Solarmodule 1 640 mm x 990 mm, nur einheitlich im "
            "Längs- oder Querformat verlegbar",
    gesucht="maximale Anzahl der Solarmodule",
    verfahren="Längsformat: ⌊12:1,64⌋·⌊10:0,99⌋ = 7·10 = 70; Querformat: ⌊12:0,99⌋·⌊10:1,64⌋ = 12·6 = 72; "
              "Maximum der beiden Anordnungen",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="m|mm", abhaengig_von="2015-GYM-K5a",
    ergebnis="72 Module (Querformat)", zwischenergebnis="Längsformat: 70 Module", niveau_geschaetzt="III",
    fehlerquelle="Gesamtfläche durch Modulfläche teilen (120 m² : 1,62 m² ≈ 74) statt die beiden Anordnungen "
                 "seitenweise mit Abrunden zu prüfen")

row(id="2015-GYM-K5d", block="Kontext", aufgabe="5", titel="Solardach", teilaufgabe="d", seite="7",
    punkte="2", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Arithmetisches Mittel berechnen",
    typ_neben="Prozentuale Veränderung berechnen",
    stichwoerter="Sonnenscheindauer|Mittelwert|Prozent", format="Rechnung|Rechnung",
    operator="Bestimmen Sie|Berechnen Sie", antwort="Zahl|Zahl", material="Diagramm",
    skizze="gestapeltes Balkendiagramm je Monat: tatsächliche Sonnenscheindauer (grau, mit Zahl beschriftet: "
           "65, 64, 70, 204, 278, 235, 100, 212, 146, 85, 97, 62) unter astronomisch möglicher (weiß); Juli "
           "Gesamthöhe 500 h",
    kontext="Umwelt/Klima", textumfang="lang",
    gegeben="monatliche tatsächliche Sonnenscheindauer 2000 in Berlin (12 Werte, siehe Skizze); astronomisch "
            "mögliche Sonnenscheindauer im Juli 500 h laut Diagramm",
    gesucht="mittlere tatsächliche Sonnenscheindauer 2000; prozentuale Abweichung im Juli",
    verfahren="Summe der 12 Monatswerte durch 12; Juli: (500−100):500",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="h",
    ergebnis="Mittelwert ≈ 134,83 h|80 % unter der astronomisch möglichen Dauer", niveau_geschaetzt="II",
    fehlerquelle="die astronomisch mögliche Dauer im Juli aus der Gesamthöhe falsch ablesen oder die "
                 "Differenz auf die tatsächliche statt die astronomische Dauer beziehen")

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
