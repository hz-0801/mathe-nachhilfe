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
    "jahr": "2016",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "16_P10_Gym_Ma_A.pdf",  # einteiliges Heft (2014–2018 ein Heft, msa.md § 3)
    "dateien": [],
    "seiten": 11,
    "soll": {"1": 10, "2": 12, "3": 9, "4": 10, "5": 9},
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
    ("Parameter einer Exponentialfunktion aus Graph bestimmen", "Gleichungen und Funktionen",
     "Exponentialfunktionen und Wachstum",
     "Parameter c (Anfangswert) und a (Wachstumsfaktor) einer Exponentialfunktion f(x) = c · a^x aus dem "
     "y-Achsenabschnitt und einem weiteren Punkt des Graphen bestimmen.",
     "2016-GYM-K2a"),
    ("Wertetabelle auf Exponentialfunktion prüfen", "Gleichungen und Funktionen", "Exponentialfunktionen und Wachstum",
     "Prüfen, ob eine Wertetabelle zu einer Exponentialfunktion gehören kann, indem die Quotienten "
     "aufeinanderfolgender y-Werte bei gleichen x-Schritten verglichen werden (bei einer "
     "Exponentialfunktion müssen sie gleich sein).",
     "2016-GYM-K2b"),
    ("Lineare Funktion aus Steigung und Schnittbedingung bestimmen", "Gleichungen und Funktionen", "Lineare Funktionen",
     "Gleichung einer linearen Funktion aus einer gegebenen Steigung und der Bedingung, einen anderen "
     "Funktionsgraphen in einem bestimmten Punkt (hier auf der y-Achse) zu schneiden, bestimmen und "
     "zeichnen.",
     "2016-GYM-K2c"),
    ("Schnittpunktanzahl von Graphen begründen", "Gleichungen und Funktionen", "Quadratische Funktionen",
     "Begründen, dass zwei Funktionsgraphen unterschiedlichen Typs (hier eine Parabel und eine "
     "Exponentialfunktion) genau einen gemeinsamen Punkt haben, anhand von Monotonie und Funktionswerten an "
     "ausgewählten Stellen.",
     "2016-GYM-K2d"),
    ("Flächeninhalt eines Dreiecks aus Koordinaten berechnen", "Raum und Form", "Ebene Figuren und Winkel",
     "Flächeninhalt eines im Koordinatensystem gegebenen Dreiecks berechnen, z. B. über eine Grundseite auf "
     "einer Achse und die Höhe als Abstand des dritten Punkts von dieser Achse.",
     "2016-GYM-K2e"),
    ("Materialbedarf aus Längen berechnen", "Größen und Messen", "Einheiten umrechnen",
     "Gesamtbedarf an Ausgangsmaterial (Länge) aus Stückzahl und Einzellänge berechnen und durch die "
     "gelieferte Gebindegröße teilen, um die Anzahl der zu bestellenden Einheiten (aufgerundet) zu "
     "bestimmen.",
     "2016-GYM-K3a"),
    ("Masse eines zusammengesetzten Körpers berechnen", "Größen und Messen", "Volumen und Oberfläche",
     "Volumen eines aus mehreren Körpern (z. B. Zylinder, Kegel, Halbkugel) zusammengesetzten Werkstücks "
     "berechnen und daraus über die Dichte die Masse bestimmen.",
     "2016-GYM-K3b"),
    ("Anzahl Objekte aus Masse und Tragfähigkeit berechnen", "Größen und Messen", "Volumen und Oberfläche",
     "Aus der Masse eines einzelnen Objekts und einer maximalen Tragfähigkeit die größtmögliche Anzahl "
     "Objekte bestimmen, die diese nicht überschreitet (Abrunden).",
     "2016-GYM-K3b"),
    ("Modalwert bestimmen", "Daten und Zufall", "Kenngrößen",
     "Modalwert (häufigster Wert) einer Datenliste bestimmen.",
     "2016-GYM-K3c"),
    ("Funktionswerte einer Parabel im Sachkontext berechnen", "Gleichungen und Funktionen", "Quadratische Funktionen",
     "Werte einer quadratischen Funktion im Sachkontext für gegebene x-Werte berechnen und umgekehrt einen "
     "x-Wert zu einem gegebenen Funktionswert (z. B. eine Nullstelle als Rand des Gültigkeitsbereichs) "
     "bestimmen.",
     "2016-GYM-K4c"),
    ("Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen", "Größen und Messen", "Flächeninhalt und Umfang",
     "Flächeninhalt eines gleichseitigen Dreiecks aus seinem Umfang berechnen (Seite = Umfang : 3, dann "
     "A = √3/4 · a²).",
     "2016-GYM-K5b"),
]

row(id="2016-GYM-B1a", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="a", seite="2",
    punkte="1", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Arithmetisches Mittel berechnen",
    stichwoerter="arithmetisches Mittel|Durchschnitt", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="drei Werte: 8; 40; 60", gesucht="arithmetisches Mittel", verfahren="(8+40+60) : 3",
    schritte="1", zahlenraum="ganz", ergebnis="36", niveau_geschaetzt="I",
    fehlerquelle="durch die Anzahl der Ziffern statt durch die Anzahl der Werte (3) teilen")

row(id="2016-GYM-B1b", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="b", seite="2",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Lineare Gleichungen",
    typ="Lineare Gleichung aus Sachverhalt aufstellen",
    stichwoerter="Gleichung aufstellen|Achtfache|vermindert", format="Kurzantwort", operator="Stellen Sie auf",
    antwort="Term", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="„Das Achtfache einer Zahl vermindert um zwölf ist gleich 36.“", gesucht="passende Gleichung",
    verfahren="Zahl als x: 8x − 12 = 36", schritte="1", zahlenraum="ganz|negativ", ergebnis="8x − 12 = 36",
    niveau_geschaetzt="II", fehlerquelle="„vermindert um zwölf“ als 12 − 8x statt 8x − 12 lesen")

row(id="2016-GYM-B1c", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="c", seite="2",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Eigenschaften eines Graphen beurteilen",
    stichwoerter="Gerade|monoton fallend|Graphen vergleichen", format="Ankreuzen", operator="Kreuzen Sie an",
    antwort="Kreuz", material="Koordinatensystem",
    skizze="Koordinatensystem x von −1 bis 3, y von −2 bis 1, Gitter 1; Gerade f mit positiver Steigung durch "
           "etwa (−1|−2) bis (3,3|0,3); Gerade g mit negativer Steigung durch etwa (−1|1) bis (2|−2)",
    kontext="ohne", textumfang="kurz",
    gegeben="zwei Geraden f (positive Steigung) und g (negative Steigung) im Koordinatensystem",
    gesucht="monoton fallender Graph", verfahren="Steigung ablesen: g steigt, f fällt", schritte="1",
    ergebnis="f", niveau_geschaetzt="I",
    fehlerquelle="die Beschriftung der Geraden vertauschen (g statt f als fallend ankreuzen)")

row(id="2016-GYM-B1d", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="d", seite="2",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Zuordnungen proportional und antiproportional",
    typ="Proportionale Zuordnung Dreisatz",
    stichwoerter="Leberwurst|Fettgehalt|Dreisatz", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Ernährung", textumfang="kurz",
    gegeben="100 g Leberwurst enthalten 30 g Fett", gesucht="Fettgehalt in 20 g Leberwurst",
    verfahren="30 : 100 · 20", schritte="1", zahlenraum="ganz", einheiten="g", ergebnis="6 g",
    niveau_geschaetzt="I", fehlerquelle="30 g direkt übernehmen, ohne auf 20 g umzurechnen")

row(id="2016-GYM-B1e", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="e", seite="2",
    punkte="1", leitidee="Raum und Form", thema="Ebene Figuren und Winkel", typ="Eigenschaft einer Figur zuordnen",
    stichwoerter="Parallelogramm|Winkel|Eigenschaft", format="Ankreuzen", operator="Kreuzen Sie an", antwort="Kreuz",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="drei Aussagen über Winkel im Parallelogramm: benachbart gleich groß; gegenüberliegend gleich "
            "groß; alle gleich groß",
    gesucht="richtige Ergänzung", verfahren="Definitionseigenschaft des Parallelogramms: gegenüberliegende "
                                           "Winkel sind gleich groß",
    schritte="1", ergebnis="gegenüberliegende Winkel gleich groß", niveau_geschaetzt="I",
    fehlerquelle="Eigenschaft des Rechtecks (alle Winkel gleich) auf das allgemeine Parallelogramm übertragen")

row(id="2016-GYM-B1f", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="f", seite="3",
    punkte="1", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit einstufig", typ="Wahrscheinlichkeit einstufig",
    stichwoerter="Laplace|defekt|Energiesparlampe", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Qualitätskontrolle", textumfang="kurz",
    gegeben="Kiste mit 100 Energiesparlampen, davon 5 defekt", gesucht="Wahrscheinlichkeit, eine defekte zu ziehen",
    verfahren="5 : 100", schritte="1", zahlenraum="Bruch|Prozent", ergebnis="P = 5/100 = 0,05 = 5 %",
    niveau_geschaetzt="I", fehlerquelle="mit den 95 intakten Lampen statt den 5 defekten rechnen")

row(id="2016-GYM-B1g", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="g", seite="3",
    punkte="1", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen", typ="Scheitelpunktform aufstellen",
    stichwoerter="Normalparabel|Scheitelpunkt|Scheitelpunktform", format="Ankreuzen", operator="Kreuzen Sie an",
    antwort="Kreuz", material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="verschobene Normalparabel mit Scheitelpunkt S(1|3); Auswahl y=(x+1)²+3, y=(x−1)²−3, y=(x−1)²+3",
    gesucht="passende Gleichung", verfahren="Scheitelpunktform y=(x−d)²+e mit Scheitel (d|e)=(1|3)",
    schritte="1", zahlenraum="negativ", ergebnis="y = (x − 1)² + 3", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen von d in der Klammer vertauschen (y=(x+1)²+3 wählen)")

row(id="2016-GYM-B1h", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="h", seite="3",
    punkte="1", leitidee="Zahlen und Operationen", thema="Zehnerpotenzen und Näherungswerte",
    typ="Zehnerpotenzschreibweise umwandeln",
    stichwoerter="Zehnerpotenz|ausschreiben", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="8,5 · 10⁵", gesucht="Zahl ohne abgetrennte Zehnerpotenz", verfahren="Komma um 5 Stellen nach rechts",
    schritte="1", zahlenraum="ganz", ergebnis="850 000", niveau_geschaetzt="I",
    fehlerquelle="Komma um 5 Stellen nach links statt nach rechts verschieben")

row(id="2016-GYM-B1i", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="i", seite="3",
    punkte="1", leitidee="Zahlen und Operationen", thema="Rationale Zahlen rechnen", typ="Termwert berechnen",
    stichwoerter="Termwert|einsetzen|negative Zahlen", format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Term (a+b)/c mit a=2, b=−4, c=−2", gesucht="Wert des Terms",
    verfahren="(2 + (−4)) : (−2) = (−2) : (−2)", schritte="1", zahlenraum="negativ", ergebnis="1",
    niveau_geschaetzt="I", fehlerquelle="Vorzeichenfehler beim Dividieren zweier negativer Zahlen (Ergebnis −1)")

row(id="2016-GYM-B1j", block="Basis", aufgabe="1", titel="Basisaufgaben", teilaufgabe="j", seite="3",
    punkte="1", leitidee="Raum und Form", thema="Körper, Netze, Schrägbilder",
    typ="Gegenfläche im Würfelnetz bestimmen",
    stichwoerter="Würfelnetz|Grundfläche|Deckfläche", format="Eintragen", operator="Markieren Sie", antwort="Kreuz",
    material="Figur",
    skizze="Würfelnetz aus 6 Quadraten: oben ein Quadrat über dem dritten Quadrat einer mittleren Dreierreihe "
           "(die grau markierte Grundfläche ist das erste Quadrat dieser Reihe); unten rechts zwei weitere "
           "Quadrate, das erste davon unter dem dritten Quadrat der mittleren Reihe",
    kontext="ohne", textumfang="mittel",
    gegeben="Würfelnetz mit grau markierter Grundfläche (erstes Quadrat der mittleren Dreierreihe)",
    gesucht="Deckfläche (dem Grundflächen-Quadrat gegenüberliegende Fläche nach dem Falten)",
    verfahren="Netz gedanklich falten (Abrollen eines Würfels über die Nachbarquadrate): die Deckfläche ist "
              "das dritte, mit drei Nachbarn verbundene Quadrat der mittleren Reihe (Knotenpunkt zum oberen "
              "und zum unteren rechten Quadrat)",
    schritte="1", ergebnis="drittes Quadrat der mittleren Reihe (verbunden mit dem oberen und dem unteren "
                          "rechten Quadrat) markiert", niveau_geschaetzt="III",
    fehlerquelle="das am weitesten von der Grundfläche entfernte Quadrat (unten rechts außen) als Deckfläche "
                 "wählen, statt das Netz tatsächlich zu falten",
    bemerkung="Lage der Deckfläche durch Falt-Simulation (Abrollen eines Würfels über die Netzquadrate) "
              "bestimmt, nicht durch bloßes Abzählen des Abstands im Netz.")

row(id="2016-GYM-K2a", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="a", seite="4",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Parameter einer Exponentialfunktion aus Graph bestimmen",
    stichwoerter="Exponentialfunktion|Parameter|Graph", format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem",
    skizze="Koordinatensystem x von −3 bis 4, y von 0 bis 5; Graph f einer wachsenden Exponentialfunktion "
           "durch (0|2) und den markierten Punkt P(2|4,5)",
    kontext="ohne", textumfang="mittel",
    gegeben="f(x) = c·aˣ mit a,c,x ∈ ℝ, a>0, c≠0; Graph durch (0|2) (y-Achsenabschnitt) und P(2|4,5)",
    gesucht="Parameter c und a", verfahren="c = f(0) = 2; aus f(2)=c·a²=4,5 folgt a² = 2,25, a = 1,5",
    schritte="2", zahlenraum="dezimal", ergebnis="c = 2, a = 1,5", niveau_geschaetzt="II",
    fehlerquelle="a direkt am Graphen als Steigung statt als Wachstumsfaktor über die Gleichung bestimmen")

row(id="2016-GYM-K2b", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="b", seite="4",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Exponentialfunktionen und Wachstum",
    typ="Wertetabelle auf Exponentialfunktion prüfen",
    stichwoerter="Wertetabelle|Quotient|Exponentialfunktion", format="Begründung", operator="Prüfen und "
                                                                                             "begründen Sie",
    antwort="Text", material="Tabelle", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Wertetabelle x=−3,−1,1 und y=1/3, 4/3, 3; f(x) = 2·1,5ˣ aus a)",
    gesucht="ob die Tabelle zu f gehören kann",
    verfahren="Quotienten bei gleichem Δx=2 vergleichen: (4/3):(1/3)=4, aber 3:(4/3)=2,25 – ungleiche "
              "Quotienten, also keine Exponentialfunktion mit konstantem Faktor; zusätzlich f(−3)=2·1,5⁻³=16/27 "
              "≠ 1/3",
    schritte="2", zahlenraum="Bruch", abhaengig_von="2016-GYM-K2a",
    ergebnis="nein, die Tabelle gehört nicht zu f (die Quotienten aufeinanderfolgender Werte sind nicht "
             "gleich, und f(−3) ≠ 1/3)", niveau_geschaetzt="III",
    fehlerquelle="nur einen der drei Tabellenwerte mit f vergleichen, statt die Konsistenz der Tabelle selbst "
                 "zu prüfen")

row(id="2016-GYM-K2c", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="c", seite="5",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Lineare Funktion aus Steigung und Schnittbedingung bestimmen", typ_neben="Gerade aus Gleichung zeichnen",
    stichwoerter="Schnittpunkt y-Achse|Steigung|verschobener Graph", format="Zeichnen|Kurzantwort",
    operator="Zeichnen Sie|Geben Sie an", antwort="Grafik|Term", material="Koordinatensystem",
    skizze="Gerade g mit Steigung −2 durch (0|3) in dasselbe Koordinatensystem wie f einzeichnen",
    kontext="ohne", textumfang="mittel",
    gegeben="f um 1 Einheit nach oben verschoben schneidet die Gerade g (Steigung −2) genau auf der y-Achse",
    gesucht="Gerade g und ihre Gleichung",
    verfahren="verschobenes f(0)+1 = c+1 = 3 ist der gemeinsame y-Achsenabschnitt; g(x) = −2x + 3",
    schritte="2", zahlenraum="negativ", abhaengig_von="2016-GYM-K2a", ergebnis="g(x) = −2x + 3",
    niveau_geschaetzt="III", fehlerquelle="den y-Achsenabschnitt von f (c=2) statt den der verschobenen "
                                          "Funktion (c+1=3) verwenden")

row(id="2016-GYM-K2d", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="d", seite="5",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Schnittpunktanzahl von Graphen begründen", typ_neben="Parabel aus Gleichung skizzieren",
    stichwoerter="Parabel|Exponentialfunktion|ein Schnittpunkt", format="Zeichnen|Begründung",
    operator="Zeichnen Sie|Begründen Sie", antwort="Grafik|Text", material="Koordinatensystem",
    skizze="Parabel p mit Scheitel (3|2) in dasselbe Koordinatensystem wie f einzeichnen",
    kontext="ohne", textumfang="mittel",
    gegeben="Parabel p(x) = (x−3)² + 2; Exponentialfunktion f(x) = 2·1,5ˣ",
    gesucht="Nachweis, dass p und f genau einen gemeinsamen Punkt haben",
    verfahren="Wertevergleich: bei x=0 ist p(0)=11 > f(0)=2 (p oberhalb), am Scheitel x=3 ist p(3)=2 < f(3)"
              "=6,75 (f oberhalb) – dazwischen liegt mindestens ein Schnittpunkt; für x<0 wächst p schneller "
              "als f gegen 0 geht (p bleibt oberhalb), für x>3 wächst f als Exponentialfunktion schließlich "
              "schneller als die Parabel p und bleibt oberhalb – also genau ein Vorzeichenwechsel von p−f",
    schritte="3", zahlenraum="dezimal", abhaengig_von="2016-GYM-K2a",
    ergebnis="genau ein Schnittpunkt (zwischen x=1,6 und x=1,8)", niveau_geschaetzt="III",
    fehlerquelle="aus der Zeichnung eine grobe Schätzung übernehmen, ohne die Werte an mehreren Stellen zu "
                 "vergleichen")

row(id="2016-GYM-K2e", block="Kontext", aufgabe="2", titel="Funktionen", teilaufgabe="e", seite="5",
    punkte="2", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Flächeninhalt eines Dreiecks aus Koordinaten berechnen",
    stichwoerter="Dreiecksfläche|Koordinaten|Ursprung", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="Dreieck aus Ursprung O, P(2|4,5) und Q(0|5) im selben "
                                         "Koordinatensystem",
    kontext="ohne", textumfang="kurz",
    gegeben="Punkte P(2|4,5), Q(0|5) und der Koordinatenursprung O bilden ein Dreieck",
    gesucht="Flächeninhalt des Dreiecks",
    verfahren="Grundseite OQ auf der y-Achse (Länge 5), Höhe = waagerechter Abstand von P zur y-Achse (2); "
              "A = 0,5 · 5 · 2",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="LE²", ergebnis="A = 5 LE²", niveau_geschaetzt="II",
    fehlerquelle="OP oder PQ statt OQ als Grundseite auf einer Achse verwenden und die Höhe falsch ablesen")

row(id="2016-GYM-K3a", block="Kontext", aufgabe="3", titel="Werkstück", teilaufgabe="a", seite="6",
    punkte="3", leitidee="Größen und Messen", thema="Einheiten umrechnen", typ="Materialbedarf aus Längen berechnen",
    stichwoerter="Rundstahl|Strang|Gesamtlänge", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur",
    skizze="Rundstahl-Werkstück: kegelförmige Spitze (Länge 60 mm) + zylindrischer Mittelteil (Länge 100 mm, "
           "Durchmesser 40 mm) + halbkugelförmiges Ende (Radius 20 mm)",
    kontext="Fertigung/Industrie", textumfang="mittel",
    gegeben="33 000 Werkstücke, je Werkstück Kegel 60 mm + Zylinder 100 mm + Halbkugel (Radius 20 mm); "
            "Rundstahl in Strängen von 6 m Länge",
    gesucht="Anzahl der zu bestellenden Rundstahlstränge",
    verfahren="Werkstücklänge = 60+100+20 = 180 mm = 0,18 m; Gesamtlänge = 33 000 · 0,18 m = 5 940 m; "
              "Stränge = 5 940 : 6",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="mm|m", ergebnis="990 Stränge",
    zwischenergebnis="Werkstücklänge 180 mm; Gesamtlänge 5 940 m", niveau_geschaetzt="III",
    fehlerquelle="den Radius der Halbkugel (20 mm) bei der Werkstücklänge vergessen (dann 160 mm statt "
                 "180 mm)")

row(id="2016-GYM-K3b", block="Kontext", aufgabe="3", titel="Werkstück", teilaufgabe="b", seite="7",
    punkte="4", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Masse eines zusammengesetzten Körpers berechnen", typ_neben="Anzahl Objekte aus Masse und Tragfähigkeit "
                                                                       "berechnen",
    stichwoerter="Kegel|Zylinder|Halbkugel|Masse|Gitterbox", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur", skizze="dieselbe Werkstückskizze wie in a)", kontext="Fertigung/Industrie",
    textumfang="mittel",
    gegeben="Radius 20 mm, Zylinderlänge 100 mm, Kegellänge 60 mm; 1 cm³ Stahl hat Masse 7,8 g; Tragfähigkeit "
            "einer Gitterbox 1 Tonne",
    gesucht="maximale Anzahl Werkstücke je Gitterbox",
    verfahren="V = π·r²·h(Zylinder) + 1/3·π·r²·h(Kegel) + 2/3·π·r³(Halbkugel) ≈ 167 551,6 mm³ = 167,55 cm³; "
              "Masse = 167,55 · 7,8 ≈ 1 306,9 g; Anzahl = 1 000 000 g : 1 306,9 g, abgerundet",
    schritte="4", zahlenraum="dezimal", einheiten="mm|cm³|g|t", abhaengig_von="2016-GYM-K3a",
    ergebnis="765 Werkstücke", zwischenergebnis="V ≈ 167,55 cm³; Masse ≈ 1 306,9 g", niveau_geschaetzt="III",
    fehlerquelle="aufrunden statt abrunden und damit die Tragfähigkeit überschreiten")

row(id="2016-GYM-K3c", block="Kontext", aufgabe="3", titel="Werkstück", teilaufgabe="c", seite="7",
    punkte="2", leitidee="Daten und Zufall", thema="Kenngrößen", typ="Spannweite berechnen", typ_neben="Modalwert bestimmen",
    stichwoerter="Stichprobe|Spannweite|Modalwert", format="Kurzantwort|Kurzantwort", operator="Geben Sie an",
    antwort="Zahl|Zahl", material="Tabelle", skizze="keine", kontext="Fertigung/Industrie", textumfang="mittel",
    gegeben="Stichprobe von 10 Werkstücklängen in mm: 181; 180; 182; 182; 181; 180; 179; 180; 179; 180",
    gesucht="Spannweite und Modalwert der Stichprobe",
    verfahren="Spannweite = 182 − 179; Modalwert = häufigster Wert (180 kommt viermal vor)", schritte="2",
    zahlenraum="ganz", einheiten="mm", ergebnis="Spannweite = 3 mm|Modalwert = 180 mm", niveau_geschaetzt="I",
    fehlerquelle="den Mittelwert statt des häufigsten Werts als Modalwert angeben")

row(id="2016-GYM-K4a", block="Kontext", aufgabe="4", titel="Stadtbrücke", teilaufgabe="a", seite="8",
    punkte="2", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang", typ="Flächeninhalt Rechteck berechnen",
    typ_neben="Kosten aus Menge und Preis berechnen",
    stichwoerter="Fahrbahn|Sanierungskosten|Rechteck", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze="Brücke von oben, Fahrbahn als Rechteck 252 m x 15,2 m", kontext="Bauwesen",
    textumfang="kurz",
    gegeben="Brückenlänge 252 m, Fahrbahnbreite 15,2 m, Sanierungskosten 150 €/m²",
    gesucht="Gesamtkosten der Fahrbahnsanierung",
    verfahren="A = 252 · 15,2 = 3 830,4 m²; Kosten = 3 830,4 · 150 €", schritte="2", zahlenraum="dezimal",
    einheiten="m|m²|€", ergebnis="574 560 €", zwischenergebnis="A = 3 830,4 m²", niveau_geschaetzt="II",
    fehlerquelle="Länge und Breite vertauschen oder die Fläche nicht in m² vor der Kostenrechnung bilden")

row(id="2016-GYM-K4b", block="Kontext", aufgabe="4", titel="Stadtbrücke", teilaufgabe="b", seite="8",
    punkte="1", leitidee="Zahlen und Operationen", thema="Prozentrechnung", typ="Prozentwert berechnen",
    stichwoerter="Prozentsatz|Rest|Stadtgrenze", format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bauwesen", textumfang="kurz",
    gegeben="252 m Brückenlänge, 30 % gehören zu Stadt A, der Rest zu Stadt B",
    gesucht="Länge des zu Stadt B gehörenden Teils",
    verfahren="Anteil B = 100 % − 30 % = 70 %; 252 · 0,7", schritte="2", zahlenraum="dezimal|Prozent",
    einheiten="m", ergebnis="176,4 m", niveau_geschaetzt="II",
    fehlerquelle="30 % von 252 m als Ergebnis angeben, ohne den Rest (70 %) zu bilden")

row(id="2016-GYM-K4c", block="Kontext", aufgabe="4", titel="Stadtbrücke", teilaufgabe="c", seite="8",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Funktionswerte einer Parabel im Sachkontext berechnen",
    typ_neben="Nullstellen quadratische Funktion berechnen|Scheitelpunkt ablesen",
    stichwoerter="Parabelbogen|Wertetabelle|Spannweite", format="Rechnung|Rechnung|Kurzantwort",
    operator="Vervollständigen Sie|Berechnen Sie|Geben Sie an", antwort="Zahl|Zahl|Zahl", material="Tabelle",
    skizze="Wertetabelle x=0,10,20 (y gesucht) und eine vierte Spalte mit y=0 (x gesucht); x-Achse liegt auf "
           "Fahrbahnhöhe",
    kontext="Bauwesen", textumfang="lang",
    gegeben="p(x) = −0,0085x² + 12 (x ≥ 0), x-Achse auf Fahrbahnhöhe; Tabelle x=0,10,20 sowie ein Punkt mit "
            "y=0",
    gesucht="fehlende Tabellenwerte; Spannweite des Parabelbogens; maximale Höhe über der Fahrbahn",
    verfahren="p(0)=12, p(10)=11,15, p(20)=8,6; Nullstelle: 0,0085x²=12, x=√(12:0,0085)≈37,57; Spannweite = "
              "2·37,57 (Symmetrie zu x=0); maximale Höhe = p(0), da x-Achse auf Fahrbahnhöhe liegt und der "
              "Scheitel bei x=0 liegt",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="m",
    ergebnis="p(0)=12, p(10)=11,15, p(20)=8,6|Spannweite ≈ 75,15 m|maximale Höhe = 12 m",
    zwischenergebnis="Nullstelle bei x ≈ 37,57 m", niveau_geschaetzt="III",
    fehlerquelle="die Spannweite als einfachen Nullstellenwert (37,57 m statt des doppelten Werts) angeben")

row(id="2016-GYM-K4d", block="Kontext", aufgabe="4", titel="Stadtbrücke", teilaufgabe="d", seite="9",
    punkte="3", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Seite im rechtwinkligen Dreieck berechnen",
    stichwoerter="Klappbrücke|Neigungswinkel|Höhe über Wasser", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur",
    skizze="geöffnetes Fahrbahnstück (Länge 37,6 m) um 30° gegenüber der Waagerechten geneigt, Fußpunkt 8 m "
           "über der Wasseroberfläche",
    kontext="Bauwesen", textumfang="mittel",
    gegeben="Fahrbahn normal 8 m über der Wasseroberfläche; geöffnetes Fahrbahnstück 37,6 m lang, 30° gegen "
            "die Waagerechte geneigt",
    gesucht="Abstand zwischen Wasseroberfläche und höchstem Punkt des geneigten Stücks",
    verfahren="zusätzliche Höhe = 37,6 · sin(30°); Gesamthöhe = 8 + zusätzliche Höhe", schritte="2",
    zahlenraum="dezimal", einheiten="m|Grad", ergebnis="26,8 m", zwischenergebnis="zusätzliche Höhe = 18,8 m",
    niveau_geschaetzt="II", fehlerquelle="cos(30°) statt sin(30°) verwenden (falsche Zuordnung von Ankathete "
                                         "und Gegenkathete)")

row(id="2016-GYM-K5a", block="Kontext", aufgabe="5", titel="Pumpspeicherwerk Goldisthal", teilaufgabe="a", seite="10",
    punkte="3", leitidee="Daten und Zufall", thema="Daten darstellen", typ="Kreisdiagramm zeichnen",
    typ_neben="Prozentsatz berechnen",
    stichwoerter="Pumpspeicherleistung|Summe|Kreisdiagramm", format="Rechnung|Zeichnen", operator="Geben Sie "
                                                                                                    "an|Stellen "
                                                                                                    "Sie dar",
    antwort="Zahl|Grafik", material="Tabelle",
    skizze="leerer Kreis zum Eintragen des Sektors für die Thüringer Pumpspeicherleistung",
    kontext="Energie/Umwelt", textumfang="mittel",
    gegeben="Pumpspeicherleistung Deutschland 7·10³ MW; Thüringen: Goldisthal 1060 MW, Hohenwarte I+II 320 MW, "
            "Bleiloch 80 MW",
    gesucht="Summe der Thüringer Leistungen; Kreisdiagramm-Darstellung des Anteils an Deutschland",
    verfahren="Summe = 1060+320+80 = 1460 MW; Anteil = 1460 : 7000 ≈ 20,86 %; Mittelpunktswinkel ≈ 0,2086·360°"
              " ≈ 75,1°",
    schritte="3", zahlenraum="ganz|Prozent", einheiten="MW|Grad", ergebnis="Summe = 1460 MW|Sektor mit "
             "Mittelpunktswinkel ≈ 75,1° (Anteil ≈ 20,86 %)", zwischenergebnis="Anteil ≈ 20,86 %",
    niveau_geschaetzt="II", fehlerquelle="die Summe direkt als Prozentsatz ohne Bezug auf die "
                                         "Gesamtleistung 7000 MW eintragen")

row(id="2016-GYM-K5b", block="Kontext", aufgabe="5", titel="Pumpspeicherwerk Goldisthal", teilaufgabe="b", seite="11",
    punkte="4", leitidee="Größen und Messen", thema="Flächeninhalt und Umfang",
    typ="Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen", typ_neben="Volumen Prisma berechnen",
    stichwoerter="Oberbecken|gleichseitiges Dreieck|Wasserstand", format="Begründung|Rechnung",
    operator="Zeigen Sie durch Rechnung|Berechnen Sie", antwort="Zahl|Zahl", material="Foto|Figur",
    skizze="Oberbecken als gerades Prisma mit gleichseitigem Dreieck als Grund- und Deckfläche, Dammlänge "
           "3370 m als Umfang",
    kontext="Energie/Umwelt", textumfang="mittel",
    gegeben="Damm um das Oberbecken 3370 m lang (Umfang des gleichseitigen Dreiecks); Wasserstand schwankt "
            "innerhalb von 8 Stunden um 20 m",
    gesucht="Nachweis, dass die Wasseroberfläche bei vollem Becken ≈ 55 Hektar beträgt; abfließendes "
            "Wasservolumen bei der Schwankung",
    verfahren="Seite a = 3370 : 3 ≈ 1123,33 m; A = √3/4 · a² ≈ 546 409 m² ≈ 54,64 ha ≈ 55 ha; Volumen = A · "
              "Höhenschwankung ≈ 55 ha · 20 m = 550 000 m² · 20 m",
    schritte="3", zahlenraum="dezimal", einheiten="m|m²|ha|m³", ergebnis="A ≈ 54,64 ha ≈ 55 ha|Volumen ≈ "
             "11 000 000 m³", zwischenergebnis="Seite a ≈ 1123,33 m", niveau_geschaetzt="III",
    fehlerquelle="den Umfang direkt durch 4 statt durch 3 teilen (Rechteck- statt Dreiecksseite) oder ha und "
                 "m² bei der Volumenrechnung nicht umrechnen")

row(id="2016-GYM-K5c", block="Kontext", aufgabe="5", titel="Pumpspeicherwerk Goldisthal", teilaufgabe="c", seite="11",
    punkte="2", leitidee="Gleichungen und Funktionen", thema="Zuordnungen proportional und antiproportional",
    typ="Dauer aus Menge und Rate berechnen",
    stichwoerter="Rundweg|Wandergeschwindigkeit|Dauer", format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Freizeit/Wandern", textumfang="kurz",
    gegeben="Rundweg 12 km, Wandergeschwindigkeit 5 km/h", gesucht="benötigte Zeit für den Rundweg",
    verfahren="12 : 5", schritte="1", zahlenraum="dezimal", einheiten="km|h", ergebnis="2,4 h = 2 h 24 min",
    niveau_geschaetzt="I", fehlerquelle="Geschwindigkeit und Strecke vertauschen (5:12 statt 12:5)")

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
