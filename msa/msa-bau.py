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
    "jahr": "2026",
    "papier": "EBR",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "26_P10_Ma_EBR_A.pdf",
    "seiten": 10,
    "soll": {"1": 10, "2": 5, "3": 4, "4": 6, "5": 5, "6": 5, "7": 5},
    "soll_gesamt": 40,
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
# Keine – jede Fertigkeit dieses Hefts steht schon in msa-typen.csv, siehe Bericht.
NEUE_TYPEN = []

row(id="2026-EBR-B1a", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="a", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Prozentrechnung", typ="Prozentwert berechnen",
    stichwoerter="Prozent|Prozentwert|Geld", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="30 % von 70 €", gesucht="Prozentwert", verfahren="0,3 · 70", schritte="1",
    zahlenraum="ganz|Prozent", einheiten="€", ergebnis="21 €", niveau_geschaetzt="I",
    fehlerquelle="70 : 30 rechnen oder 30 % als 0,03 nehmen",
    bemerkung="Wortgleich mit 2026-FOR-B1a.")

row(id="2026-EBR-B1b", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="b", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Brüche und Dezimalzahlen",
    typ="Bruchteil einer Fläche bestimmen",
    stichwoerter="Drittel|Anteil|Figur|Kreissektor", format="Ankreuzen", operator="Kreuzen Sie an",
    antwort="Kreuz", material="Figur",
    skizze="vier Figuren nebeneinander, je ein Ankreuzfeld darüber: 1 Rechteck mit schmalem grauem "
           "Streifen am linken Rand (etwa ein Sechstel der Breite); 2 auf der Spitze stehendes Quadrat "
           "aus vier gleichen Teilquadraten, das rechte grau; 3 Parallelogramm, durch eine Diagonale "
           "geteilt, das linke Dreieck grau; 4 Kreis mit grauem Sektor von 120° (von oben gegen den "
           "Uhrzeigersinn bis etwa 8 Uhr)",
    kontext="ohne", textumfang="kurz",
    gegeben="vier Figuren mit grauer Teilfläche: Rechteck (ca. 1/6), Quadrat (1/4), Parallelogramm "
            "(1/2), Kreis (120°-Sektor)",
    gesucht="Figur, deren grauer Anteil 1/3 ist",
    verfahren="120° von 360° sind ein Drittel; die anderen Anteile sind 1/6, 1/4, 1/2", schritte="1",
    zahlenraum="Bruch", ergebnis="vierte Abbildung (Kreis mit 120°-Sektor)", niveau_geschaetzt="I",
    fehlerquelle="grauen Streifen des Rechtecks nach Augenmaß als Drittel schätzen",
    bemerkung="Wortgleich mit 2026-FOR-B1b (eigene Bildvermessung bestätigt Rechteck ≈ 1/6, Quadrat "
              "1/4, Parallelogramm 1/2, Kreissektor 120° = 1/3).")

row(id="2026-EBR-B1c", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="c", seite="2",
    punkte="1", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Eigenschaft einer Figur zuordnen",
    stichwoerter="Trapez|parallele Seiten|Vierecke", format="Ankreuzen", operator="Kreuzen Sie an",
    antwort="Kreuz", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Satzanfang „In jedem Trapez …“ mit drei Optionen: sind alle Winkel gleich groß; gibt es "
            "ein Paar paralleler Seiten; sind alle Seiten gleich lang",
    gesucht="zutreffende Eigenschaft",
    verfahren="Definition des Trapezes: mindestens ein Paar paralleler Seiten", schritte="0",
    zahlenraum="ganz", ergebnis="gibt es ein Paar paralleler Seiten", niveau_geschaetzt="I",
    fehlerquelle="Trapez mit Raute oder Rechteck verwechseln",
    bemerkung="Wortgleich mit 2026-FOR-B1c.")

row(id="2026-EBR-B1d", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="d", seite="2",
    punkte="1", leitidee="Größen und Messen", thema="Einheiten umrechnen", typ="Größen vergleichen",
    stichwoerter="Meter|Zentimeter|Vergleichszeichen", format="Eintragen", operator="Setzen Sie ein",
    antwort="Term", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="3,5 m □ 35 cm, Zeichen <, = oder >", gesucht="richtiges Zeichen",
    verfahren="3,5 m = 350 cm > 35 cm", schritte="1", zahlenraum="dezimal", einheiten="m|cm",
    ergebnis=">", niveau_geschaetzt="I", fehlerquelle="3,5 m als 35 cm lesen und = setzen",
    bemerkung="Wortgleich mit 2026-FOR-B1d.")

row(id="2026-EBR-B1e", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="e", seite="2",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Wertetabelle einer Funktion zuordnen",
    stichwoerter="Wertetabelle|y = 3x²|Funktionsgleichung", format="Ankreuzen", operator="Kreuzen Sie an",
    antwort="Kreuz", material="Tabelle",
    skizze="drei Wertetabellen nebeneinander, je ein Ankreuzfeld darüber; x-Zeile jeweils −2, −1, 0, 1, "
           "2; y-Zeilen: 12, 3, 0, 3, 12 | −6, −3, 0, 3, 6 | 4, 1, 0, 1, 4",
    kontext="ohne", textumfang="kurz",
    gegeben="y = 3x²; drei Wertetabellen für x = −2 … 2 mit y = 12, 3, 0, 3, 12 bzw. −6, −3, 0, 3, 6 "
            "bzw. 4, 1, 0, 1, 4",
    gesucht="passende Tabelle", verfahren="einen Wert prüfen: 3 · 2² = 12", schritte="1",
    zahlenraum="ganz|negativ|Potenz", ergebnis="erste Tabelle (y = 12, 3, 0, 3, 12)",
    zwischenergebnis="Tabelle 2 gehört zu y = 3x, Tabelle 3 zu y = x²", niveau_geschaetzt="I",
    fehlerquelle="3x² als 3x oder als (3x)² lesen", bemerkung="Wortgleich mit 2026-FOR-B1e.")

row(id="2026-EBR-B1f", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="f", seite="2",
    punkte="1", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Volumen Würfel berechnen",
    stichwoerter="Würfel|Volumen|Kantenlänge", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Würfel mit Kantenlänge a = 3 cm", gesucht="Volumen", verfahren="V = a³ = 3 · 3 · 3",
    schritte="1", zahlenraum="ganz|Potenz", einheiten="cm|cm³", ergebnis="27 cm³",
    niveau_geschaetzt="I", fehlerquelle="3 · 3 = 9 oder Oberfläche 54 cm²",
    bemerkung="Wortgleich mit 2026-FOR-B1f.")

row(id="2026-EBR-B1g", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="g", seite="2",
    punkte="1", leitidee="Zahlen und Operationen", thema="Rationale Zahlen rechnen",
    typ="Termwert berechnen",
    stichwoerter="Term|Einsetzen|negative Zahlen", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Term 5 · (x − 3), x = −2", gesucht="Wert des Terms", verfahren="5 · (−2 − 3) = 5 · (−5)",
    schritte="2", zahlenraum="ganz|negativ", ergebnis="−25", niveau_geschaetzt="I",
    fehlerquelle="−2 − 3 = −1 oder Vorzeichen des Produkts", bemerkung="Wortgleich mit 2026-FOR-B1g.")

row(id="2026-EBR-B1h", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="h", seite="3",
    punkte="1", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Umfang Rechteck berechnen",
    stichwoerter="Rechteck|Umfang|Dezimalzahlen", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Rechteck mit a = 3,5 cm und b = 1,5 cm", gesucht="Umfang", verfahren="u = 2 · (a + b) = 2 · 5",
    schritte="1", zahlenraum="dezimal", einheiten="cm", ergebnis="10 cm", niveau_geschaetzt="I",
    fehlerquelle="Flächeninhalt 5,25 cm² statt Umfang oder a + b",
    bemerkung="Wortgleich mit 2026-FOR-B1h.")

row(id="2026-EBR-B1i", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="i", seite="3",
    punkte="1", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Winkel im Viereck berechnen",
    stichwoerter="Parallelogramm|Nebenwinkel|180°", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="Figur",
    skizze="Parallelogramm, lange Seiten waagerecht, nach rechts geneigt; Winkel 75° an der linken "
           "unteren Ecke, β an der rechten unteren Ecke; Hinweis „Abbildung nicht maßstabsgerecht“",
    kontext="ohne", textumfang="kurz",
    gegeben="Parallelogramm mit Winkel 75° links unten; β ist der benachbarte Winkel rechts unten",
    gesucht="β", verfahren="benachbarte Winkel im Parallelogramm ergänzen sich zu 180°: 180° − 75°",
    schritte="1", zahlenraum="ganz", einheiten="Grad", ergebnis="105°", niveau_geschaetzt="I",
    fehlerquelle="β = 75° (gegenüberliegende statt benachbarte Winkel)",
    bemerkung="Wortgleich mit 2026-FOR-B1i.")

row(id="2026-EBR-B1j", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="j", seite="3",
    punkte="1", leitidee="Größen und Messen", thema="Satz des Pythagoras",
    typ="Pythagoras Gleichung zuordnen",
    stichwoerter="Pythagoras|Hypotenuse|Formel wählen", format="Ankreuzen", operator="Kreuzen Sie an",
    antwort="Kreuz", material="Figur",
    skizze="rechtwinkliges Dreieck, rechter Winkel unten rechts markiert, Kathete u waagerecht unten, "
           "Kathete v senkrecht rechts, Hypotenuse w von links unten nach rechts oben; links drei "
           "Optionen mit Ankreuzfeld: w = √(v² − u²), w = √(u² − v²), w = √(u² + v²)",
    kontext="ohne", textumfang="kurz",
    gegeben="rechtwinkliges Dreieck mit Katheten u, v und Hypotenuse w; drei Gleichungen zur Auswahl",
    gesucht="Gleichung für w", verfahren="w ist die Hypotenuse, also w² = u² + v²", schritte="0",
    zahlenraum="Wurzel|Potenz", ergebnis="w = √(u² + v²) (dritte Option)", niveau_geschaetzt="I",
    fehlerquelle="w als Kathete ansehen und eine Differenz wählen",
    bemerkung="Wortgleich mit 2026-FOR-B1j.")

row(id="2026-EBR-K2a", block="Kontext", aufgabe="2", titel="Turm", teilaufgabe="a", seite="4",
    punkte="2", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Volumen Zylinder berechnen",
    stichwoerter="Zylinder|Volumen|Turm", voraussetzungen="Formel aus der Formelsammlung entnehmen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl", material="Körper",
    skizze="Turm als Körper: grau schattierter Zylinder mit Höhe h (Maßpfeil rechts) und Radius r "
           "(Pfeil am Boden), darauf ein Kegel mit Mantellinie s (Pfeil an der Schräge); Maße im Text "
           "links: h = 25,0 m, r = 4,7 m, s = 8,6 m; Hinweis „Abbildung nicht maßstabsgerecht“; "
           "Karokästchen",
    kontext="Bauwesen/Architektur", textumfang="mittel",
    gegeben="Zylinder mit r = 4,7 m und h = 25,0 m", gesucht="Volumen des Zylinders",
    verfahren="V = π · r² · h = π · 4,7² · 25", schritte="1", zahlenraum="dezimal", einheiten="m|m³",
    ergebnis="≈ 1734,9 m³", niveau_geschaetzt="I",
    fehlerquelle="r² als 2r rechnen oder r mit dem Durchmesser verwechseln",
    bemerkung="Wortgleich mit 2026-FOR-K2a.")

row(id="2026-EBR-K2b", block="Kontext", aufgabe="2", titel="Turm", teilaufgabe="b", seite="4",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Mantelfläche Kegel berechnen", typ_neben="Kosten aus Menge und Preis berechnen",
    stichwoerter="Kegel|Mantelfläche|Dachziegel|Kosten", voraussetzungen="Formel Kegelmantel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl", material="Körper",
    skizze="Turm als Körper: grau schattierter Zylinder mit Höhe h (Maßpfeil rechts) und Radius r "
           "(Pfeil am Boden), darauf ein Kegel mit Mantellinie s (Pfeil an der Schräge); Maße im Text "
           "links: h = 25,0 m, r = 4,7 m, s = 8,6 m; Hinweis „Abbildung nicht maßstabsgerecht“ "
           "(Abbildung im Stamm auf Seite 4)",
    kontext="Bauwesen/Architektur", textumfang="mittel",
    gegeben="Kegeldach mit r = 4,7 m und Mantellinie s = 8,6 m; 1 m² Dachziegel kostet 20,00 €",
    gesucht="Kosten der Dachziegel",
    verfahren="M = π · r · s = π · 4,7 · 8,6 ≈ 127,0 m²; Kosten 127,0 · 20 €", schritte="2",
    zahlenraum="dezimal", einheiten="m|m²|€", ergebnis="≈ 2539,66 € (rund 2540 €)",
    zwischenergebnis="M ≈ 126,98 m²", niveau_geschaetzt="II",
    fehlerquelle="Grundfläche des Kegels mitrechnen oder s als Höhe einsetzen",
    bemerkung="Wortgleich mit 2026-FOR-K2b.")

row(id="2026-EBR-K3a", block="Kontext", aufgabe="3", titel="Viereck", teilaufgabe="a", seite="5",
    punkte="2", leitidee="Größen und Messen", thema="Satz des Pythagoras", typ="Pythagoras Kathete",
    stichwoerter="Parallelogramm|Höhe|Pythagoras|Kathete", voraussetzungen="Wurzel ziehen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl", material="Figur",
    skizze="Parallelogramm ABCD (A links unten, B rechts unten, C rechts oben, D links oben, nach "
           "rechts geneigt); Seite BC mit 32 cm beschriftet; AB über B hinaus bis F verlängert, "
           "BF = 13 cm; von C gestrichelt senkrecht nach unten die Höhe h bis F, rechter Winkel in F; "
           "Winkel ε bei B zwischen BF und BC; Hinweis „Abbildung nicht maßstabsgerecht“; Karokästchen",
    kontext="ohne", textumfang="mittel",
    gegeben="Parallelogramm ABCD; BC = 32 cm; F auf der Verlängerung von AB mit BF = 13 cm; CF = h "
            "steht senkrecht auf AF; ε = Winkel CBF",
    gesucht="h", verfahren="h = √(32² − 13²) = √855", schritte="2", zahlenraum="ganz|Wurzel|dezimal",
    einheiten="cm", ergebnis="h ≈ 29,2 cm", zwischenergebnis="h² = 1024 − 169 = 855",
    niveau_geschaetzt="I", fehlerquelle="32² + 13² addieren",
    bemerkung="Wortgleich mit 2026-FOR-K4a.")

row(id="2026-EBR-K3b", block="Kontext", aufgabe="3", titel="Viereck", teilaufgabe="b", seite="5",
    punkte="2", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Winkel im rechtwinkligen Dreieck berechnen",
    stichwoerter="Kosinus|Ankathete|Hypotenuse|Nachweis",
    voraussetzungen="Umkehrfunktion cos⁻¹ am Taschenrechner", format="Rechnung",
    operator="Weisen Sie nach", antwort="Zahl", material="Figur",
    skizze="Parallelogramm ABCD (A links unten, B rechts unten, C rechts oben, D links oben, nach "
           "rechts geneigt); Seite BC mit 32 cm beschriftet; AB über B hinaus bis F verlängert, "
           "BF = 13 cm; von C gestrichelt senkrecht nach unten die Höhe h bis F, rechter Winkel in F; "
           "Winkel ε bei B zwischen BF und BC; Hinweis „Abbildung nicht maßstabsgerecht“ (Abbildung im "
           "Stamm auf Seite 5)",
    kontext="ohne", textumfang="kurz",
    gegeben="Parallelogramm ABCD; BC = 32 cm; F auf der Verlängerung von AB mit BF = 13 cm; CF = h "
            "steht senkrecht auf AF; ε = Winkel CBF",
    gesucht="Nachweis ε ≈ 66°",
    verfahren="cos ε = 13 : 32 = 0,406; ε = cos⁻¹(0,406); alternativ tan ε = h : 13 mit h aus a)",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="cm|Grad", ergebnis="ε ≈ 66,0°",
    niveau_geschaetzt="I", fehlerquelle="sin statt cos (13 als Gegenkathete)",
    bemerkung="über cos unabhängig von a); über tan abhängig von 2026-EBR-K3a. Übrige Angaben "
              "wortgleich mit 2026-FOR-K4b.")

row(id="2026-EBR-K4a", block="Kontext", aufgabe="4", titel="Benzinpreise", teilaufgabe="a", seite="6",
    punkte="1", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Spannweite berechnen",
    stichwoerter="Spannweite|Maximum|Minimum|Preise", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="Tabelle",
    skizze="Tabelle mit Kopfzeile „Wochentage“ (Mo bis So) und Zeile „Benzinpreis in € pro Liter“: "
           "1,77; 1,78; 1,77; 1,79; 1,84; 1,82; 1,85; Zapfsäulen-Piktogramm",
    kontext="Tankstelle/Preise", textumfang="kurz",
    gegeben="Benzinpreise: Mo 1,77; Di 1,78; Mi 1,77; Do 1,79; Fr 1,84; Sa 1,82; So 1,85 (€ pro Liter)",
    gesucht="Spannweite", verfahren="1,85 − 1,77", schritte="1", zahlenraum="dezimal", einheiten="€",
    ergebnis="0,08 € pro Liter", niveau_geschaetzt="I",
    fehlerquelle="Sa statt So als Maximum nehmen (0,05)",
    bemerkung="Wortgleich mit 2026-FOR-K3a.")

row(id="2026-EBR-K4b", block="Kontext", aufgabe="4", titel="Benzinpreise", teilaufgabe="b", seite="6",
    punkte="2", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Arithmetisches Mittel berechnen",
    typ_neben="Behauptung prüfen", stichwoerter="Mittelwert|Teilzeitraum|Behauptung", format="Rechnung",
    operator="Zeigen Sie rechnerisch", antwort="Zahl", material="Tabelle",
    skizze="Tabelle mit Kopfzeile „Wochentage“ (Mo bis So) und Zeile „Benzinpreis in € pro Liter“: "
           "1,77; 1,78; 1,77; 1,79; 1,84; 1,82; 1,85; Zapfsäulen-Piktogramm",
    kontext="Tankstelle/Preise", textumfang="mittel",
    gegeben="Benzinpreise: Mo 1,77; Di 1,78; Mi 1,77; Do 1,79; Fr 1,84; Sa 1,82; So 1,85 (€ pro Liter); "
            "Behauptung: Mo bis Fr liegt der Durchschnittspreis unter 1,80 €",
    gesucht="Nachweis der Behauptung", verfahren="(1,77 + 1,78 + 1,77 + 1,79 + 1,84) : 5 = 8,95 : 5",
    schritte="2", zahlenraum="dezimal", einheiten="€",
    ergebnis="Mittel Mo–Fr = 1,79 € < 1,80 €, Aussage richtig", zwischenergebnis="Summe 8,95",
    niveau_geschaetzt="I", fehlerquelle="alle sieben Tage mitteln (1,803) und die Aussage verwerfen",
    bemerkung="Wortgleich mit 2026-FOR-K3b.")

row(id="2026-EBR-K4c", block="Kontext", aufgabe="4", titel="Benzinpreise", teilaufgabe="c", seite="6",
    punkte="2", leitidee="Zahlen und Operationen", thema="Prozentrechnung",
    typ="Prozentuale Veränderung berechnen",
    stichwoerter="Preissteigerung|Prozent|Grundwert alt", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Tabelle",
    skizze="Tabelle mit Kopfzeile „Wochentage“ (Mo bis So) und Zeile „Benzinpreis in € pro Liter“: "
           "1,77; 1,78; 1,77; 1,79; 1,84; 1,82; 1,85; Zapfsäulen-Piktogramm",
    kontext="Tankstelle/Preise", textumfang="kurz",
    gegeben="Preis Do 1,79 €, Fr 1,84 €", gesucht="Steigerung in Prozent",
    verfahren="1,84 : 1,79 = 1,0279, also 2,8 %; oder 0,05 : 1,79", schritte="2",
    zahlenraum="dezimal|Prozent", einheiten="€|%", ergebnis="≈ 2,8 %", zwischenergebnis="Differenz 0,05 €",
    niveau_geschaetzt="II", fehlerquelle="Differenz auf den neuen Preis beziehen (0,05 : 1,84 = 2,7 %)",
    bemerkung="Wortgleich mit 2026-FOR-K3c.")

row(id="2026-EBR-K4d", block="Kontext", aufgabe="4", titel="Benzinpreise", teilaufgabe="d", seite="7",
    punkte="1", leitidee="Daten und Zufall", thema="Daten darstellen",
    typ="Säulen- oder Balkendiagramm ergänzen",
    stichwoerter="Säulendiagramm|Skala|ergänzen", format="Zeichnen", operator="Zeichnen Sie ein",
    antwort="Grafik", material="Diagramm",
    skizze="Säulendiagramm mit y-Achse „Benzinpreis in € pro Liter“ von 1,75 bis 1,90 (Beschriftung "
           "alle 0,05, Hilfslinien alle 0,01) und x-Achse Mo bis So („Wochentag“); blaue Säulen Mo "
           "1,77, Di 1,78, Mi 1,77, Do 1,79, Fr 1,84, Sa 1,82; Platz für So leer",
    kontext="Tankstelle/Preise", textumfang="kurz",
    gegeben="Diagramm mit sechs Säulen Mo–Sa (Werte wie in der Tabelle), Preis So = 1,85 €",
    gesucht="Säule für So", verfahren="Wert 1,85 auf der Skala (1,75 bis 1,90, Schritt 0,01) abtragen",
    schritte="1", zahlenraum="dezimal", einheiten="€", ergebnis="Säule So bis 1,85 (höchste Säule)",
    niveau_geschaetzt="I", fehlerquelle="Skala falsch lesen (Hilfslinie = 0,01)",
    bemerkung="Wortgleich mit 2026-FOR-K3d.")

row(id="2026-EBR-K5a", block="Kontext", aufgabe="5", titel="Funktionen", teilaufgabe="a", seite="8",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Gerade aus Gleichung zeichnen",
    stichwoerter="lineare Funktion|Steigung|y-Achsenabschnitt|zeichnen",
    voraussetzungen="Steigungsdreieck", format="Zeichnen", operator="Zeichnen Sie ein",
    antwort="Grafik", material="Koordinatensystem",
    skizze="Kästchenraster ohne Achsen oder Beschriftung, für den Graphen von f; weiter unten auf der "
           "Seite ein zweites, beschriftetes Koordinatensystem mit Ursprung O, x von −2 bis 5, y von "
           "−2 bis 5, Gitter 1 mit Hilfslinien alle 0,5, darin die nach oben geöffnete Parabel p mit "
           "Scheitel (2|−2) bereits eingezeichnet (für Teilaufgabe c)",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −2x + 2", gesucht="Graph von f",
    verfahren="y-Achsenabschnitt 2, Steigungsdreieck 1 nach rechts, 2 nach unten; Gerade durch (0|2) "
              "und (1|0)",
    schritte="1", zahlenraum="ganz|negativ",
    ergebnis="Gerade durch (0|2) und (1|0), fallend mit Steigung −2", niveau_geschaetzt="I",
    fehlerquelle="Steigung −2 als 2 nach rechts, 1 nach unten",
    bemerkung="Koordinatensystem für den Graphen hier ein unbeschriftetes Kästchenraster, anders als "
              "2026-FOR-K5a, wo dieselbe beschriftete Achse mit Parabel für a), c) und d) zugleich "
              "dient (FOR hat kein eigenes Blatt-Aufgabenäquivalent zu d) in diesem Heft); die "
              "Rechnung ist sonst wortgleich.")

row(id="2026-EBR-K5b", block="Kontext", aufgabe="5", titel="Funktionen", teilaufgabe="b", seite="8",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Punktprobe durchführen",
    stichwoerter="Punktprobe|Einsetzen|negative Zahlen", format="Rechnung",
    operator="Untersuchen Sie rechnerisch", antwort="Text", material="keins", skizze="keine",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −2x + 2; Punkt P(−4|10)", gesucht="ob P auf dem Graphen liegt",
    verfahren="f(−4) = −2 · (−4) + 2 = 10 mit y-Wert vergleichen", schritte="1",
    zahlenraum="ganz|negativ", ergebnis="f(−4) = 10, P liegt auf dem Graphen", niveau_geschaetzt="I",
    fehlerquelle="−2 · (−4) = −8", bemerkung="Wortgleich mit 2026-FOR-K5b.")

row(id="2026-EBR-K5c", block="Kontext", aufgabe="5", titel="Funktionen", teilaufgabe="c", seite="8",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Scheitelpunkt ablesen",
    stichwoerter="Scheitelpunktform|Scheitelpunkt|verschobene Normalparabel", format="Eintragen",
    operator="Geben Sie an", antwort="Zahl", material="Koordinatensystem",
    skizze="Koordinatensystem mit Ursprung O, x von −2 bis 5, y von −2 bis 5 beschriftet, Gitter 1 mit "
           "Hilfslinien alle 0,5; eingezeichnete nach oben geöffnete Parabel p mit Scheitel (2|−2), "
           "Nullstellen bei etwa 0,6 und 3,4, y-Achsenabschnitt 2; Eintragfeld „S( | )“",
    kontext="ohne", textumfang="kurz",
    gegeben="p(x) = (x − 2)² − 2, Parabel abgebildet", gesucht="Scheitelpunkt",
    verfahren="aus der Scheitelpunktform oder am Graphen ablesen", schritte="1",
    zahlenraum="ganz|negativ", ergebnis="S(2|−2)", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen: S(−2|−2)", bemerkung="Wortgleich mit 2026-FOR-K5c.")

row(id="2026-EBR-K6a", block="Kontext", aufgabe="6", titel="Würfel", teilaufgabe="a", seite="9",
    punkte="1", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit einstufig",
    typ="Wahrscheinlichkeit einstufig",
    stichwoerter="Würfel|Laplace|Netz|günstige Fälle", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="Figur",
    skizze="zwei Würfelnetze in Kreuzform (waagerechte Reihe von vier Feldern, über und unter dem "
           "zweiten Feld je ein Feld); Würfel A: oben 2, Reihe 1 2 4 1, unten 5; Würfel B: oben 3, "
           "Reihe 3 1 2 1, unten 3",
    kontext="Glücksspiel", textumfang="mittel",
    gegeben="Würfel A mit den Zahlen 1, 1, 2, 2, 4, 5; Würfel B mit 1, 1, 2, 3, 3, 3; Würfel A wird "
            "einmal geworfen",
    gesucht="P(2) bei Würfel A", verfahren="zwei von sechs Flächen zeigen 2", schritte="1",
    zahlenraum="Bruch", ergebnis="2/6 = 1/3", niveau_geschaetzt="I",
    fehlerquelle="1/6, weil die 2 nur einmal gezählt wird",
    bemerkung="Wortgleich mit 2026-FOR-K6a.")

row(id="2026-EBR-K6b", block="Kontext", aufgabe="6", titel="Würfel", teilaufgabe="b", seite="9",
    punkte="4", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Baumdiagramm ergänzen", typ_neben="Wahrscheinlichkeit mehrstufig unabhängig",
    stichwoerter="Baumdiagramm|gerade/ungerade|Pfadregel|Gegenwahrscheinlichkeit",
    voraussetzungen="Summe der Wahrscheinlichkeiten an einem Knoten ist 1",
    format="Eintragen|Rechnung", operator="Ergänzen Sie|Ermitteln Sie", antwort="Zahl|Zahl",
    material="Diagramm",
    skizze="zweistufiges Baumdiagramm: Startpunkt links, Stufe „Würfel A“ mit Ästen gerade (3/6 "
           "vorgegeben) und ungerade (leeres Feld), Stufe „Würfel B“ an jedem Ast gerade/ungerade; "
           "vorgegeben 1/6 am Ast gerade→gerade, die drei übrigen Felder leer; darunter Karokästchen",
    kontext="Glücksspiel", textumfang="mittel",
    gegeben="Würfel A mit den Zahlen 1, 1, 2, 2, 4, 5; Würfel B mit 1, 1, 2, 3, 3, 3; erst A, dann B "
            "geworfen; betrachtet wird gerade/ungerade; im Baum vorgegeben P(A gerade) = 3/6 und "
            "P(B gerade | A gerade) = 1/6",
    gesucht="fehlende Wahrscheinlichkeiten im Baum|P(beide ungerade)",
    verfahren="A ungerade 3/6; bei B gerade 1/6 und ungerade 5/6 auf beiden Ästen; Pfadregel 3/6 · 5/6",
    schritte="3", zahlenraum="Bruch",
    ergebnis="A ungerade 3/6; B ungerade 5/6 (nach gerade), gerade 1/6 und ungerade 5/6 (nach "
             "ungerade)|P(beide ungerade) = 15/36 = 5/12",
    niveau_geschaetzt="II", fehlerquelle="B ungerade wie A mit 3/6 ansetzen oder 3/6 + 5/6 rechnen",
    bemerkung="zwei Leistungen in einer Einheit, Punkte ungeteilt. Wortgleich mit 2026-FOR-K6b.")

row(id="2026-EBR-K7a", block="Kontext", aufgabe="7", titel="Mietkosten", teilaufgabe="a", seite="10",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Wachstumstabelle ergänzen",
    stichwoerter="prozentuales Wachstum|Wachstumsfaktor 1,019|Tabelle",
    voraussetzungen="Prozentsatz in Wachstumsfaktor umrechnen", format="Eintragen",
    operator="Vervollständigen Sie", antwort="Zahl", material="Tabelle",
    skizze="Tabelle mit Zeilen „Jahr“ (2026, 2027, 2028, 2029) und „Miete in €“ (leer, 662,35, 674,93, "
           "leer); Foto Haus mit Schlüsseln neben dem Text",
    kontext="Wohnen/Miete", textumfang="mittel",
    gegeben="Miete im ersten Jahr (2026) 650 € monatlich, jährlich +1,9 %; Tabelle mit 2027: 662,35 € "
            "und 2028: 674,93 €",
    gesucht="Miete 2026 und 2029", verfahren="2026 ist der Anfangswert 650; 2029 = 674,93 · 1,019",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="€",
    ergebnis="2026: 650,00 €|2029: 687,76 €", niveau_geschaetzt="I",
    fehlerquelle="2026 als 650 · 1,019 setzen oder jedes Jahr 12,35 € addieren (linear)",
    bemerkung="Wortgleich mit 2026-FOR-K7a.")

row(id="2026-EBR-K7b", block="Kontext", aufgabe="7", titel="Mietkosten", teilaufgabe="b", seite="10",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Graph zu Wachstumsprozess zuordnen", typ_neben="Eigenschaften eines Graphen beurteilen",
    stichwoerter="exponentiell|linear|Startwert|Graph erkennen", format="Ankreuzen|Begründung",
    operator="Entscheiden Sie|Kreuzen Sie an|Begründen Sie", antwort="Kreuz|Text", material="Diagramm",
    skizze="drei kleine Koordinatensysteme A, B, C nebeneinander (Achsen „Miete in €“ und „Zeit in "
           "Jahren“, Gitter, keine Zahlen), je ein Ankreuzfeld darunter: A nach oben gekrümmte Kurve, "
           "die im Ursprung beginnt; B nach oben gekrümmte Kurve, die auf der y-Achse oberhalb des "
           "Ursprungs beginnt; C Gerade, die auf der y-Achse oberhalb des Ursprungs beginnt; "
           "Karokästchen",
    kontext="Wohnen/Miete", textumfang="mittel",
    gegeben="Miete im ersten Jahr (2026) 650 € monatlich, jährlich +1,9 %; drei Graphen: A exponentiell "
            "ab Ursprung, B exponentiell ab positivem Startwert, C linear ab positivem Startwert",
    gesucht="passender Graph|Begründung, warum die zwei anderen nicht passen",
    verfahren="Startwert 650 > 0 schließt A aus; gleicher Prozentsatz bedeutet wachsende Zuwächse "
              "(gekrümmt), schließt C aus",
    schritte="0", zahlenraum="ganz",
    ergebnis="B|A: Miete beginnt bei 0 € statt bei 650 €; C: linear, also jedes Jahr gleicher Betrag "
             "statt gleicher Prozentsatz",
    niveau_geschaetzt="III",
    fehlerquelle="C wählen, weil „1,9 % pro Jahr“ als konstanter Zuwachs verstanden wird",
    bemerkung="Wortgleich mit 2026-FOR-K7b.")
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
