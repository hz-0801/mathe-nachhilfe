# -*- coding: utf-8 -*-
"""fhr-bau.py – Gerüst für die Erfassung eines Hefts im Profil fhr.
Version 0.2 · 12.09.2026 · gilt mit katalog-prompt.md v0.3 und fhr.md v0.10

Je Heft werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles darunter
bleibt unverändert und prüft nach Kern Abschnitt 7.

Ablauf:
  1. Vorhandene fhr-katalog.csv und fhr-typen.csv neben dieses Skript legen
     (aus dem Repo, mit dem geprüften SHA). Fehlen sie, wird neu angelegt.
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen.
  3. python3 fhr-bau.py – schreibt beide CSV-Dateien und gibt Prüftabelle
     und Bericht aus. Bei einem Fehler wird nichts geschrieben.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    "jahr": "2019",
    "papier": "C",
    "datei": "19_Mathematik_FOS_Lehrer_C.pdf",
    "seiten": 9,
    # Sollpunkte je Aufgabe aus der Punktetabelle am Ende jeder Aufgabe
    "soll": {"1": 30, "2": 20, "3": 20},
    "soll_gesamt": 70,
}

# ---- technischer Block, nicht ändern ----
HEAD = ("id;jahr;papier;block;aufgabe;titel;teilaufgabe;seite;punkte;stern;hilfsmittel;afb_amtlich;"
        "leitidee;thema;typ;typ_neben;stichwoerter;voraussetzungen;format;operator;antwort;material;"
        "skizze;kontext;textumfang;gegeben;gesucht;verfahren;schritte;zahlenraum;einheiten;"
        "abhaengig_von;ergebnis;zwischenergebnis;niveau_geschaetzt;fehlerquelle;bemerkung").split(";")

ZEILEN = []

def row(**kw):
    z = {k: "" for k in HEAD}
    z.update(jahr=KONFIG["jahr"], papier=KONFIG["papier"], block="", stern="",
             hilfsmittel="ja", afb_amtlich="")
    unbekannt = set(kw) - set(HEAD)
    if unbekannt:
        sys.exit(f"unbekanntes Feld: {sorted(unbekannt)}")
    z.update(kw)
    ZEILEN.append(z)

# ============================================================ ZEILEN JE HEFT
# ============================================================ ZEILEN JE HEFT

row(id="2019-C-1a", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="a", seite="2", punkte="8",
    leitidee="Differentialrechnung", thema="Symmetrie nachweisen",
    typ="Symmetrie am Funktionsterm beurteilen",
    typ_neben="Nullstellen und y-Achsenschnitt unterscheiden|Verhalten im Unendlichen bestimmen|Punktprobe am Graphen",
    stichwoerter="Aussage 1 Achsensymmetrie zur y-Achse|Aussage 2 S(−2; 0) ist der y-Achsenschnittpunkt|Aussage 3 die beiden Grenzwerte sind verschieden|Aussage 4 P(−1; 1,5) liegt auf Gf",
    voraussetzungen="y-Achsenschnitt an der x-Koordinate null erkennen|Verhalten von Funktionen geraden Grades kennen|Funktionswert einsetzen",
    format="Begründung|Rechnung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="lang",
    gegeben="f(x) = −(1/2)x^4 + 4x^2 − 2; x aus IR; zu beurteilen sind vier Aussagen: (1) Gf ist achsensymmetrisch zur y-Achse, (2) S(−2; 0) ist der Schnittpunkt von Gf mit der y-Achse, (3) die Grenzwerte für x gegen minus unendlich und gegen plus unendlich sind verschieden, (4) der Punkt P(−1; 1,5) liegt auf Gf",
    gesucht="Entscheidung und Begründung für jede der vier Aussagen",
    verfahren="die Symmetrie an den geraden Exponenten oder über f(−x) prüfen; am Punkt S die x-Koordinate betrachten; beim Grenzverhalten den geraden Grad nutzen; für P den Funktionswert an der Stelle −1 berechnen",
    schritte="4", zahlenraum="Bruch|dezimal|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(1) wahr, denn f(−x) = f(x) beziehungsweise es treten nur gerade Exponenten auf|(2) falsch, denn die x-Koordinate von S ist ungleich null|(3) falsch, denn bei Funktionen vierten Grades sind beide Grenzwerte gleich|(4) wahr, denn f(−1) = 1,5 (amtlich)",
    zwischenergebnis="f(−1) = 1,5",
    niveau_geschaetzt="II",
    fehlerquelle="bei Aussage (2) nur prüfen, ob S auf dem Graphen liegt, statt die x-Koordinate zu betrachten",
    bemerkung="Erwartungshorizont: je Aussage 2 BE, Begründungen beispielhaft. Aussagenliste nach Kern § 4, stichwoerter nennt jede Aussage. Alle vier Aussagen tragen gleich viele Punkte, deshalb thema nach der ersten Leistung. Dieses Heft hat keinen Gutachtenbogen, die Punkteaufteilung stammt aus dem Erwartungshorizont")

row(id="2019-C-1b", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="b", seite="2", punkte="4",
    leitidee="Differentialrechnung", thema="Nullstellen ganzrationaler Funktionen",
    typ="Nullstellen über Substitution biquadratisch", typ_neben="",
    stichwoerter="Substitution|vier Nullstellen|irrationale Werte|Ausklammern des Faktors −1/2",
    voraussetzungen="quadratische Gleichung mit der Lösungsformel lösen|rücksubstituieren und beide Wurzeln angeben",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/2)x^4 + 4x^2 − 2; x aus IR",
    gesucht="alle Nullstellen von f",
    verfahren="mit z = x^2 auf eine quadratische Gleichung zurückführen, beide z-Werte bestimmen und je zwei Wurzeln zurücksubstituieren",
    schritte="4", zahlenraum="dezimal|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="x1/2 = ±2,73|x3/4 = ±0,73 (amtlich)",
    zwischenergebnis="z^2 − 8z + 4 = 0 mit z1 = 7,46 und z2 = 0,54",
    niveau_geschaetzt="II",
    fehlerquelle="beim Ausklammern des Faktors −1/2 die Vorzeichen der Koeffizienten nicht anpassen",
    bemerkung="Erwartungshorizont: Nullstellen 4 BE. Heft ohne Gutachtenbogen")

row(id="2019-C-1c", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="c", seite="2", punkte="7",
    leitidee="Differentialrechnung", thema="Extrem- und Sattelpunkte",
    typ="Extrem- und Sattelpunkte über zweite Ableitung", typ_neben="",
    stichwoerter="zwei Hochpunkte|ein Tiefpunkt|Ausklammern von x|Art über zweite Ableitung",
    voraussetzungen="erste und zweite Ableitung bilden|Produkt gleich null setzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/2)x^4 + 4x^2 − 2; x aus IR",
    gesucht="Koordinaten aller Extrempunkte von Gf|Art jedes Extrempunktes",
    verfahren="f' gleich null setzen, x ausklammern und die drei Stellen bestimmen, in f'' einsetzen und über das Vorzeichen die Art bestimmen, dann die Funktionswerte berechnen",
    schritte="4", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="H1(−2; 6)|T(0; −2)|H2(2; 6) (amtlich)",
    zwischenergebnis="f'(x) = −2x^3 + 8x|f''(x) = −6x^2 + 8|Stellen x1 = 0 und x2/3 = ±2|f''(±2) = −16 < 0 und f''(0) = 8 > 0",
    niveau_geschaetzt="II",
    fehlerquelle="nach dem Ausklammern die Stelle x = 0 vergessen und nur die beiden Hochpunkte angeben",
    bemerkung="Erwartungshorizont: Ableitungen 2 BE, Extremstellen 2 BE, Art und Koordinaten 3 BE. Heft ohne Gutachtenbogen")

row(id="2019-C-1d", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="d", seite="2", punkte="5",
    leitidee="Differentialrechnung", thema="Wendepunkte",
    typ="Wendepunkte über zweite Ableitung", typ_neben="",
    stichwoerter="zwei Wendepunkte|dritte Ableitung ungleich null|Wurzel aus 4 durch 3|symmetrische Lage",
    voraussetzungen="dritte Ableitung bilden|Wurzel aus einem Bruch ziehen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/2)x^4 + 4x^2 − 2; x aus IR",
    gesucht="Koordinaten aller Wendepunkte von Gf",
    verfahren="f'' gleich null setzen, beide Wendestellen bestimmen, mit f''' ungleich null bestätigen und die Funktionswerte berechnen",
    schritte="4", zahlenraum="dezimal|negativ|Wurzel", einheiten="", abhaengig_von="2019-C-1c",
    ergebnis="W1(1,15; 2,42)|W2(−1,15; 2,42) (amtlich)",
    zwischenergebnis="f'''(x) = −12x|Wendestellen ±Wurzel aus 4/3, rund ±1,15|f'''(1,15) = −13,8 und f'''(−1,15) = 13,8",
    niveau_geschaetzt="II",
    fehlerquelle="die Bestätigung über die dritte Ableitung weglassen",
    bemerkung="Erwartungshorizont: dritte Ableitung 1 BE, Wendepunkte 4 BE; an den exakten Wendestellen ±1,1547 ergibt sich der Funktionswert 2,44 statt amtlich 2,42, weil der Erwartungshorizont mit den gerundeten Stellen ±1,15 weiterrechnet. Heft ohne Gutachtenbogen")

row(id="2019-C-1e", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="e", seite="2", punkte="3",
    leitidee="Differentialrechnung", thema="Graph zeichnen und zuordnen",
    typ="Graph ganzrationaler Funktion im Intervall zeichnen", typ_neben="",
    stichwoerter="Intervall −3 bis 3|achsensymmetrischer Verlauf|zwei Hochpunkte|Randwerte −8,5",
    voraussetzungen="Achseneinteilung selbst wählen|Achsensymmetrie zum Zeichnen nutzen",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="keins",
    skizze="zu zeichnen ist der Graph von f im Intervall −3 <= x <= 3 in einem selbst angelegten Koordinatensystem: achsensymmetrisch zur y-Achse, vom Randwert (−3; −8,5) steigend über die Nullstelle bei −2,73 zum Hochpunkt (−2; 6), von dort fallend über den Wendepunkt (−1,15; 2,42) und die Nullstelle bei −0,73 zum Tiefpunkt (0; −2), dann spiegelbildlich wieder steigend zum Hochpunkt (2; 6) und fallend zum Randwert (3; −8,5)",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/2)x^4 + 4x^2 − 2; x aus IR; das Intervall −3 <= x <= 3",
    gesucht="Zeichnung von Gf im angegebenen Intervall",
    verfahren="Nullstellen, Extrem- und Wendepunkte eintragen, die Randwerte berechnen und den Graphen durchziehen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="2019-C-1b|2019-C-1c|2019-C-1d",
    ergebnis="Graph im Intervall −3 <= x <= 3 mit H1(−2; 6), H2(2; 6), T(0; −2), den Wendepunkten (±1,15; 2,42), den Nullstellen ±2,73 und ±0,73 sowie den Randwerten (±3; −8,5) (amtlich)",
    zwischenergebnis="Randwerte f(±3) = −8,5",
    niveau_geschaetzt="I",
    fehlerquelle="den Tiefpunkt im Ursprung statt bei −2 eintragen",
    bemerkung="Erwartungshorizont: Zeichnung 3 BE; der Erwartungshorizont zeigt den Graphen ohne Angabe der Achseneinteilung. Heft ohne Gutachtenbogen")

row(id="2019-C-1f", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="f", seite="2", punkte="3",
    leitidee="Differentialrechnung", thema="Anstieg und Tangente",
    typ="Tangentengleichung im Punkt", typ_neben="",
    stichwoerter="Berührstelle x gleich −1|Anstieg −6|Achsenabschnitt −4,5|Geradengleichung",
    voraussetzungen="Anstieg als Ableitungswert bestimmen|Punkt in die Geradengleichung einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/2)x^4 + 4x^2 − 2; x aus IR; die Tangente t berührt Gf an der Stelle x = −1",
    gesucht="Gleichung der Tangente t",
    verfahren="den Anstieg als f'(−1) und den Berührpunkt über f(−1) bestimmen, beides in y = mx + n einsetzen und nach n auflösen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="2019-C-1c",
    ergebnis="t: y = −6x − 4,5 (amtlich)",
    zwischenergebnis="m = f'(−1) = −6|y = f(−1) = 1,5|n = −4,5",
    niveau_geschaetzt="II",
    fehlerquelle="beim Einsetzen des negativen Anstiegs und der negativen Stelle das Vorzeichen von n verfehlen",
    bemerkung="Erwartungshorizont: Tangentengleichung 3 BE. Heft ohne Gutachtenbogen")

row(id="2019-C-2a", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="a", seite="5", punkte="6",
    leitidee="Differentialrechnung", thema="Funktionsgleichung bestimmen",
    typ="Funktionsgleichung aus drei Punkten über LGS", typ_neben="",
    stichwoerter="quadratische Funktion|y-Achsenschnitt −4|Punkte P und Q|Kontrollergebnis vorgegeben",
    voraussetzungen="den y-Achsenschnitt als Punkt deuten|lineares Gleichungssystem mit drei Unbekannten lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Skizze",
    skizze="Abbildung neben dem Aufgabentext: die um die Hochachse gedrehte Karte eines Sees als schraffierte Fläche, oben die waagerechte x-Achse und rechts die senkrechte y-Achse, dazu eine Windrose mit Norden nach oben; die nördliche Uferlinie ist mit Gf, die südliche mit Gg beschriftet; eingezeichnet sind die Punkte Q links, R rechts und P unten am Rand der Fläche, in der Mitte steht das Wort See",
    kontext="Geografie/Seeufer", textumfang="lang",
    gegeben="die Uferlinie eines Sees wird durch die Graphen zweier ganzrationaler Funktionen beschrieben, eine Längeneinheit entspricht 2 km; der nördliche Bereich liegt auf Gf mit f(x) = x^3 − (1/2)x^2 − 4x − 2, der südliche auf Gg; von der quadratischen Funktion g ist bekannt, dass ihr Graph die y-Achse bei y = −4 schneidet und die Punkte P(−1; −5) und Q(−2; −4) auf Gg liegen; zur Kontrolle ist g(x) = x^2 + 2x − 4 angegeben",
    gesucht="Funktionsgleichung von g",
    verfahren="den allgemeinen Ansatz g(x) = ax^2 + bx + c aufstellen, die drei bekannten Punkte einsetzen und das lineare Gleichungssystem lösen",
    schritte="4", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="g(x) = x^2 + 2x − 4 (amtlich)",
    zwischenergebnis="c = −4 aus g(0) = −4|a − b + c = −5 aus g(−1) = −5|4a − 2b + c = −4 aus g(−2) = −4",
    niveau_geschaetzt="II",
    fehlerquelle="den y-Achsenschnitt nicht als dritte Bedingung nutzen und mit zwei Gleichungen für drei Unbekannte enden",
    bemerkung="Erwartungshorizont: Ansatz und Gleichungssystem 4 BE, Lösung 2 BE. Das Heft schreibt die Punkte als P(–1|–5) und Q(–2|–4); im Katalog gilt die Schreibweise P(x; y). Heft ohne Gutachtenbogen")

row(id="2019-C-2b", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="b", seite="5", punkte="6",
    leitidee="Differentialrechnung", thema="Extrem- und Sattelpunkte",
    typ="Extrem- und Sattelpunkte über zweite Ableitung",
    typ_neben="Streckenlänge im Koordinatensystem in Meter umrechnen",
    stichwoerter="nördlichster Punkt|Hochpunkt von Gf|gleiche x-Koordinate wie P|Abstand 5,5 Längeneinheiten|Maßstab 2 km",
    voraussetzungen="den nördlichsten Punkt als Hochpunkt deuten|den Abstand bei gleicher x-Koordinate als Differenz der y-Werte bilden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Skizze", skizze="Abbildung des Sees wie in Teilaufgabe a",
    kontext="Geografie/Seeufer", textumfang="kurz",
    gegeben="f(x) = x^3 − (1/2)x^2 − 4x − 2; auf Gf liegt der nördliche Bereich der Uferlinie; der Punkt P(−1; −5) liegt auf Gg; eine Längeneinheit entspricht 2 km",
    gesucht="Abstand des nördlichsten Punktes des Sees vom Punkt P",
    verfahren="f' gleich null setzen, beide Stellen bestimmen und über f'' den Hochpunkt als nördlichsten Punkt auswählen; da er dieselbe x-Koordinate wie P hat, den Abstand als Differenz der y-Werte bilden und über den Maßstab in Kilometer umrechnen",
    schritte="5", zahlenraum="Bruch|dezimal|negativ", einheiten="km", abhaengig_von="2019-C-2a",
    ergebnis="der nördlichste Punkt ist H(−1; 0,5), der Abstand zu P beträgt 5,5 Längeneinheiten, also 11 km (amtlich)",
    zwischenergebnis="f'(x) = 3x^2 − x − 4|f''(x) = 6x − 1|Stellen x1 = 4/3 mit f''(4/3) = 7 > 0 und x2 = −1 mit f''(−1) = −7 < 0",
    niveau_geschaetzt="III",
    fehlerquelle="den Tiefpunkt als nördlichsten Punkt nehmen, weil die Karte gedreht dargestellt ist",
    bemerkung="Erwartungshorizont: Ableitungen 2 BE, Auswahl des Hochpunktes und Abstand 4 BE. Der Typname der Umrechnung nennt Meter, der Fall rechnet in Kilometer; die Definition trägt. Heft ohne Gutachtenbogen")

row(id="2019-C-2c", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="c", seite="5", punkte="8",
    leitidee="Differentialrechnung", thema="Schnittpunkte von Funktionsgraphen",
    typ="Schnittpunkte zweier Funktionsgraphen berechnen",
    typ_neben="Nullstellen mit Polynomdivision|Fläche zwischen zwei Graphen berechnen|Flächeninhalt im Koordinatensystem in Quadratmeter umrechnen",
    stichwoerter="Differenzfunktion|Polynomdivision durch x plus 2|dritte Lösung verwerfen|Seeoberfläche in Quadratkilometer",
    voraussetzungen="die gegebene Schnittstelle −2 als bekannte Nullstelle nutzen|die passende Lösung anhand der Abbildung auswählen",
    format="Rechnung", operator="Berechnen Sie|Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze="Abbildung des Sees wie in Teilaufgabe a, mit den eingezeichneten Punkten Q und R als Schnittpunkte der beiden Uferlinien",
    kontext="Geografie/Seeufer", textumfang="lang",
    gegeben="f(x) = x^3 − (1/2)x^2 − 4x − 2 und g(x) = x^2 + 2x − 4; die beiden Graphen schneiden sich unter anderem im gegebenen Punkt Q(−2; −4) und im Punkt R; eine Längeneinheit entspricht 2 km",
    gesucht="x-Koordinate des Punktes R|Inhalt der Seeoberfläche in km^2",
    verfahren="die Differenzfunktion h = f − g bilden, mit der bekannten Nullstelle −2 die Polynomdivision durchführen, die verbleibende quadratische Gleichung lösen und die passende Lösung auswählen; danach h von −2 bis zu dieser Stelle integrieren und die Maßzahl mit dem quadrierten Maßstab in Quadratkilometer umrechnen",
    schritte="6", zahlenraum="dezimal|negativ|Potenz", einheiten="km^2", abhaengig_von="2019-C-2a",
    ergebnis="R hat die x-Koordinate 0,31|die Seeoberfläche beträgt rund 33,28 km^2 (amtlich)",
    zwischenergebnis="h(x) = x^3 − 1,5x^2 − 6x + 2|Polynomdivision ergibt x^2 − 3,5x + 1 mit den Lösungen 0,31 und 3,19|Flächenmaßzahl rund 8,32 Flächeneinheiten",
    niveau_geschaetzt="III",
    fehlerquelle="die Lösung 3,19 als x-Koordinate von R nehmen, ohne sie an der Abbildung zu prüfen",
    bemerkung="Erwartungshorizont: Schnittstelle 4 BE, Integral 3 BE, Umrechnung 1 BE; der Erwartungshorizont verwirft 3,19 mit dem Hinweis, dass 0,31 dichter am Hochpunkt von Gf liegt. Schnittstelle und Fläche tragen je 4 BE, deshalb thema nach der ersten Leistung. Der Typname der Umrechnung nennt Quadratmeter, der Fall rechnet in Quadratkilometer; die Definition trägt. Heft ohne Gutachtenbogen")

row(id="2019-C-3a", aufgabe="3", titel="Stochastik",
    teilaufgabe="a", seite="7", punkte="3",
    leitidee="Stochastik", thema="Laplace-Wahrscheinlichkeit",
    typ="Laplace-Bedingung begründen",
    typ_neben="Beispiele für Laplace-Experimente nennen",
    stichwoerter="1000 gleichartige Enten|gleiche Wahrscheinlichkeit|0,1 % je Ente|zwei eigene Beispiele",
    voraussetzungen="Gleichwahrscheinlichkeit der Elementarereignisse prüfen",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Nennen Sie", antwort="Text",
    material="Tabelle",
    skizze="Gewinnplan als Tabelle im Aufgabenstamm mit zwei Spalten: Nummer der Ente und Gewinn; Zeilen 1 und 1000 mit 100 €, die Nummern 2 bis 9 mit 20 €, 10 bis 99 mit 10 € sowie 111, 222, 333, 444, 555, 666, 777, 888 und 999 mit 5 €",
    kontext="Jahrmarkt/Entenangeln", textumfang="lang",
    gegeben="in einer Wanne schwimmen 1000 gleichartige Badeenten, die verdeckt von 1 bis 1000 nummeriert sind; für einen Einsatz darf eine Ente geangelt werden, sie wird nach dem Ablesen der Nummer sofort zurückgesetzt",
    gesucht="Begründung, warum das Angeln einer Ente ein Laplace-Experiment ist|zwei weitere Beispiele für Laplace-Experimente",
    verfahren="prüfen, ob alle Elementarereignisse dieselbe Wahrscheinlichkeit haben, und diese als 1 durch 1000 angeben; danach zwei bekannte Versuche mit gleich wahrscheinlichen Ergebnissen nennen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="es ist ein Laplace-Experiment, weil alle Elementarereignisse dieselbe Wahrscheinlichkeit von 0,1 % haben|als Beispiele genügen etwa der Wurf einer Münze und die Ziehung beim Lotto 6 aus 49 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Gleichwahrscheinlichkeit an den Gewinnkategorien statt an den einzelnen Enten prüfen",
    bemerkung="Erwartungshorizont: Begründung 1 BE, zwei Beispiele 2 BE. Zwei der drei Punkte hängen am Nennen eigener Beispiele, deshalb dafür ein eigener Typ. Heft ohne Gutachtenbogen")

row(id="2019-C-3b", aufgabe="3", titel="Stochastik",
    teilaufgabe="b", seite="7", punkte="4",
    leitidee="Stochastik", thema="Laplace-Wahrscheinlichkeit",
    typ="Laplace-Wahrscheinlichkeit berechnen", typ_neben="",
    stichwoerter="vier Gewinnkategorien|günstige durch mögliche|2, 8, 90 und 9 Enten|Anzahlen aus dem Gewinnplan",
    voraussetzungen="die Anzahl der Enten je Kategorie aus dem Gewinnplan abzählen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Gewinnplan aus dem Aufgabenstamm wird weiterverwendet",
    kontext="Jahrmarkt/Entenangeln", textumfang="mittel",
    gegeben="1000 von 1 bis 1000 nummerierte Enten; der Gewinnplan zahlt 100 € für die Nummern 1 und 1000, 20 € für die Nummern 2 bis 9, 10 € für die Nummern 10 bis 99 und 5 € für 111, 222, 333, 444, 555, 666, 777, 888 und 999",
    gesucht="Wahrscheinlichkeit für jede der vier Gewinnkategorien beim einmaligen Angeln",
    verfahren="je Kategorie die Anzahl der zugehörigen Enten abzählen und durch 1000 teilen",
    schritte="4", zahlenraum="Bruch|dezimal", einheiten="€", abhaengig_von="2019-C-3a",
    ergebnis="100 € mit 2/1000 = 1/500|20 € mit 8/1000 = 1/125|10 € mit 90/1000 = 9/100|5 € mit 9/1000 (amtlich)",
    zwischenergebnis="die Kategorie 10 € umfasst die 90 zweistelligen Nummern",
    niveau_geschaetzt="II",
    fehlerquelle="die Kategorie 10 bis 99 mit 89 oder 100 Enten ansetzen",
    bemerkung="Erwartungshorizont: vier Wahrscheinlichkeiten 4 BE. Heft ohne Gutachtenbogen")

row(id="2019-C-3c", aufgabe="3", titel="Stochastik",
    teilaufgabe="c", seite="7", punkte="3",
    leitidee="Stochastik", thema="Laplace-Wahrscheinlichkeit",
    typ="Laplace-Wahrscheinlichkeit berechnen",
    typ_neben="Gegenereignis nutzen|Pfadregel mehrstufig mit Zurücklegen anwenden",
    stichwoerter="Ente mit Gewinn|kein Gewinn|viermal Nummer 1 bis 500|mit Zurücklegen",
    voraussetzungen="die Gewinnanzahlen addieren|das Zurücklegen als gleichbleibende Wahrscheinlichkeit deuten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze="Gewinnplan aus dem Aufgabenstamm wird weiterverwendet",
    kontext="Jahrmarkt/Entenangeln", textumfang="mittel",
    gegeben="1000 Enten, davon 109 mit Gewinn nach dem Gewinnplan; jede geangelte Ente wird sofort zurückgesetzt; Ereignis A eine Ente mit Gewinn wird gezogen, Ereignis B mit einer gezogenen Ente wird kein Gewinn erzielt, Ereignis C viermal direkt nacheinander wird eine Ente mit einer Nummer von 1 bis 500 geangelt",
    gesucht="Wahrscheinlichkeiten der Ereignisse A, B und C",
    verfahren="für A die Anzahlen aller Gewinnkategorien addieren und durch 1000 teilen, für B das Gegenereignis nutzen und für C die gleichbleibende Wahrscheinlichkeit 1/2 viermal multiplizieren",
    schritte="3", zahlenraum="Bruch|dezimal|Prozent", einheiten="", abhaengig_von="2019-C-3b",
    ergebnis="P(A) = 0,109, also 10,9 %|P(B) = 0,891, also 89,1 %|P(C) = 0,0625, also 6,25 % (amtlich)",
    zwischenergebnis="109 von 1000 Enten bringen einen Gewinn|P(C) = (1/2)^4",
    niveau_geschaetzt="II",
    fehlerquelle="bei Ereignis C mit sinkenden Nennern rechnen, obwohl die Ente zurückgesetzt wird",
    bemerkung="Erwartungshorizont: drei Wahrscheinlichkeiten 3 BE. Zwei der drei Ereignisse sind einstufig, deshalb thema Laplace-Wahrscheinlichkeit. Heft ohne Gutachtenbogen")

row(id="2019-C-3d", aufgabe="3", titel="Stochastik",
    teilaufgabe="d", seite="7", punkte="3",
    leitidee="Stochastik", thema="Erwartungswert",
    typ="Erwartungswert berechnen",
    typ_neben="Überschuss aus Einsatz und durchschnittlicher Auszahlung berechnen",
    stichwoerter="durchschnittlicher Gewinnbetrag|gewichtete Summe|Einsatz 2 Euro|500 Spiele|Überschuss",
    voraussetzungen="die vier Gewinnhöhen mit ihren Wahrscheinlichkeiten gewichten|Einnahmen und Auszahlungen gegenüberstellen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Gewinnplan aus dem Aufgabenstamm wird weiterverwendet",
    kontext="Jahrmarkt/Entenangeln", textumfang="mittel",
    gegeben="Gewinnhöhen 100 €, 20 €, 10 € und 5 € mit den Wahrscheinlichkeiten 2/1000, 8/1000, 90/1000 und 9/1000; der Einsatz je Spiel beträgt 2 €; an einem Abend werden 500 Enten geangelt",
    gesucht="durchschnittlicher Gewinnbetrag für eine zufällig geangelte Ente|Überschuss des Standbetreibers bei 500 Spielen",
    verfahren="jede Gewinnhöhe mit ihrer Wahrscheinlichkeit multiplizieren und die Produkte addieren; danach die Einsätze von 500 Spielen um die durchschnittliche Auszahlung je Spiel vermindern",
    schritte="3", zahlenraum="dezimal|Bruch", einheiten="€", abhaengig_von="2019-C-3b",
    ergebnis="durchschnittlicher Gewinn rund 1,30 € je Ente|Überschuss bei 500 Spielen 350 € (amtlich)",
    zwischenergebnis="Einzelbeiträge 0,20 €, 0,16 €, 0,90 € und 0,045 €",
    niveau_geschaetzt="III",
    fehlerquelle="den Einsatz nicht vom Gewinn abziehen und 500 mal 2 € als Überschuss angeben",
    bemerkung="Erwartungshorizont: Gewinnbetrag und Überschuss 3 BE; der Erwartungshorizont rundet mathematisch auf 1,30 € und rechnet damit 350 €, als Alternative sind bei kaufmännischer Rundung 1,31 € und 345 € zugelassen. Mit dem ungerundeten Erwartungswert 1,305 € ergeben sich 347,50 €. Zweite Fundstelle des Themas Erwartungswert nach 2021-B-3e. Heft ohne Gutachtenbogen")

row(id="2019-C-3e", aufgabe="3", titel="Stochastik",
    teilaufgabe="e", seite="7", punkte="7",
    leitidee="Stochastik", thema="Mehrstufige Zufallsexperimente",
    typ="Baumdiagramm mehrstufig ohne Zurücklegen darstellen",
    typ_neben="Wahrscheinlichkeit über mehrere Pfade summieren|Überschuss aus Einsatz und durchschnittlicher Auszahlung berechnen",
    stichwoerter="20 Enten davon 8 markiert|drei ohne Zurücklegen|mindestens zwei markierte|Mindesteinsatz",
    voraussetzungen="mindestens zwei als drei Pfade mit genau zwei plus einen Pfad mit drei deuten|aus Auszahlung und Zielüberschuss auf den Einsatz schließen",
    format="Zeichnen|Rechnung", operator="Verdeutlichen Sie|Ermitteln Sie", antwort="Grafik|Zahl",
    material="keins",
    skizze="zu zeichnen ist ein dreistufiges Baumdiagramm für das Ziehen von drei aus 20 Enten ohne Zurücklegen, davon 8 markiert; erste Stufe zwei Äste mit 8/20 und 12/20, zweite Stufe vier Äste mit Nennern 19, dritte Stufe acht Äste mit Nennern 18; die Äste sind mit markiert und nicht markiert beschriftet",
    kontext="Jahrmarkt/Entenangeln", textumfang="lang",
    gegeben="bei einer Variante gibt es 20 Enten, von denen 8 eine versteckte Markierung tragen; je Spiel werden 3 Enten entnommen und nicht zurückgelegt; bei mindestens zwei markierten Enten gewinnt der Spieler 10 €; der Betreiber will nach 100 Spielen durchschnittlich 150 € Überschuss erzielen",
    gesucht="Baumdiagramm des Spiels|Gewinnwahrscheinlichkeit|Mindesthöhe des Spieleinsatzes",
    verfahren="das dreistufige Baumdiagramm ohne Zurücklegen zeichnen; die Pfade mit drei markierten und die drei Pfade mit genau zwei markierten Enten addieren; aus der erwarteten Auszahlung bei 100 Spielen und dem Zielüberschuss die nötige Einnahme je Spiel bestimmen",
    schritte="5", zahlenraum="Bruch|dezimal|Prozent", einheiten="€", abhaengig_von="",
    ergebnis="dreistufiges Baumdiagramm ohne Zurücklegen|Gewinnwahrscheinlichkeit 98/285, rund 34 %|der Spieleinsatz muss mindestens 4,90 € betragen (amtlich)",
    zwischenergebnis="P = 8·7·6/(20·19·18) + 3 · 8·7·12/(20·19·18)|Auszahlung bei 100 Spielen rund 340 €|nötige Einnahme 490 €",
    niveau_geschaetzt="III",
    fehlerquelle="bei genau zwei markierten Enten nur eine Reihenfolge ansetzen und den Faktor 3 vergessen",
    bemerkung="Erwartungshorizont: Baumdiagramm 3 BE, Gewinnwahrscheinlichkeit 2 BE, Mindesteinsatz 2 BE; mit der ungerundeten Wahrscheinlichkeit 0,3439 ergibt sich ein Mindesteinsatz von 4,94 € statt amtlich 4,90 €. Heft ohne Gutachtenbogen")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Beispiele für Laplace-Experimente nennen", "Stochastik", "Laplace-Wahrscheinlichkeit",
     "Eigene Zufallsversuche mit lauter gleich wahrscheinlichen Ergebnissen angeben, etwa Münzwurf oder Lottoziehung.",
     "2019-C-3a"),
    ("Überschuss aus Einsatz und durchschnittlicher Auszahlung berechnen", "Stochastik", "Erwartungswert",
     "Aus dem Einsatz je Spiel, der durchschnittlichen Auszahlung und der Zahl der Spiele den zu erwartenden Überschuss des Anbieters bestimmen oder umgekehrt aus einem Zielüberschuss den nötigen Mindesteinsatz.",
     "2019-C-3d"),
]
# ======================================================== AB HIER UNVERÄNDERT
KAT = "fhr-katalog.csv"
TYP = "fhr-typen.csv"
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]

# Themenliste nach fhr.md Abschnitt 6. Bei Änderung dort hier mitziehen.
THEMEN = {
 "Differentialrechnung": ["Ableitungen bilden", "Nullstellen ganzrationaler Funktionen",
   "Extrem- und Sattelpunkte", "Monotonie und Krümmung", "Wendepunkte", "Symmetrie nachweisen",
   "Verhalten im Unendlichen", "Graph zeichnen und zuordnen", "Anstieg und Tangente", "Normale",
   "Schnittpunkte von Funktionsgraphen", "Funktionsgleichung bestimmen", "Extremwertaufgaben"],
 "Integralrechnung": ["Stammfunktion bilden", "Bestimmtes Integral berechnen",
   "Fläche zwischen Graph und x-Achse", "Fläche zwischen zwei Graphen",
   "Rotationsvolumen um die x-Achse", "Körpervolumen aus Grundfläche und Länge"],
 "Stochastik": ["Daten darstellen und aufbereiten", "Statistische Kenngrößen",
   "Mehrstufige Zufallsexperimente", "Baumdiagramm und Pfadregeln",
   "Unabhängigkeit von Ereignissen", "Erwartungswert", "Kombinatorische Abzählverfahren",
   "Laplace-Wahrscheinlichkeit"],
 "Grundlagen": ["Prozentrechnung", "Gleichungen lösen", "Größen und Einheiten", "Terme umformen"],
}
FORMATE = {"Ankreuzen","Kurzantwort","Rechnung","Begründung","Zeichnen","Konstruieren","Tabelle","Eintragen"}
ANTWORTEN = {"Zahl","Term","Text","Grafik","Kreuz","Tabelle"}
MATERIAL = {"keins","Figur","Körper","Koordinatensystem","Diagramm","Tabelle","Skizze","Foto"}
ZAHLENRAUM = {"ganz","dezimal","Bruch","negativ","Prozent","Potenz","Wurzel"}
# Stämme, die eine ASCII-Umschrift von ä, ö, ü oder ß verraten. Positivliste: der frühere
# Mustertest auf ae|oe|ue|ss schlug bei Wörtern wie Paprikastreuer oder Koeffizient fehl.
UMSCHRIFT = ("flaeche", "laenge", "naechst", "haeufig", "zufaell", "waehl", "aender", "aeusser",
 "gefaess", "verhaeltnis", "erklaer", "zaehl", "traeg", "gaeng", "maessig", "hoehe", "groesse",
 "groess", "loesung", "loes", "moegl", "koerper", "oeffn", "schoen", "pruef", "stueck", "gewuerz",
 "kruemmung", "ueber", "fuer", "muess", "fuehr", "gueltig", "zurueck", "huelle", "schluessel",
 "urspruengl", "gross", "massstab", "masszahl", "schliess", "heisst", "weiss", "strasse",
 "gemaess", "fuss")
PFLICHT = ("id jahr papier aufgabe teilaufgabe seite punkte hilfsmittel leitidee thema typ format "
           "operator antwort material skizze kontext textumfang gegeben gesucht verfahren schritte "
           "ergebnis niveau_geschaetzt fehlerquelle").split()

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

def main():
    if not ZEILEN:
        sys.exit("ZEILEN ist leer – erst die Datensätze des Hefts eintragen.")
    fehler = []
    def a(cond, msg):
        if not cond:
            fehler.append(msg)

    _, alt_kat = lade(KAT, HEAD)
    _, alt_typ = lade(TYP, TYP_HEAD)
    alt_ids = {r[0] for r in alt_kat}
    typ_namen = {r[0] for r in alt_typ} | {t[0] for t in NEUE_TYPEN}
    neue_ids = [z["id"] for z in ZEILEN]

    # Kennungen
    a(len(set(neue_ids)) == len(neue_ids), "doppelte id in ZEILEN")
    for i in neue_ids:
        a(i not in alt_ids, f"{i}: Kennung steht schon im Katalog")
        a(re.fullmatch(r"\d{4}-[ABC]-\d[a-h]", i), f"{i}: Kennung folgt nicht dem Muster Jahr-papier-AufgabeTeilaufgabe")
    for t in NEUE_TYPEN:
        a(t[0] not in {r[0] for r in alt_typ}, f"Typ {t[0]}: steht schon in {TYP}")
        a(t[1] in THEMEN and t[2] in THEMEN.get(t[1], []), f"Typ {t[0]}: Leitidee oder Thema unbekannt")
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog")
        a(len(t[3]) > 20, f"Typ {t[0]}: Definition zu knapp")

    # Punkte
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        a(ist == soll, f"Aufgabe {nr}: Punkte {ist}, Soll {soll}")
    a(sum(int(z["punkte"]) for z in ZEILEN) == KONFIG["soll_gesamt"],
      f"Gesamtpunktzahl weicht von {KONFIG['soll_gesamt']} ab")

    # Felder
    verwendet = set()
    for z in ZEILEN:
        for k in PFLICHT:
            a(z[k].strip() != "", f"{z['id']}: Pflichtfeld leer: {k}")
        a(z["jahr"] == KONFIG["jahr"] and z["papier"] == KONFIG["papier"], f"{z['id']}: Heftkennung falsch")
        a(z["leitidee"] in THEMEN, f"{z['id']}: Leitidee unbekannt")
        a(z["thema"] in THEMEN.get(z["leitidee"], []), f"{z['id']}: Thema passt nicht zur Leitidee")
        a(z["niveau_geschaetzt"] in ("I", "II", "III"), f"{z['id']}: Niveau ungültig")
        a(z["textumfang"] in ("kurz", "mittel", "lang"), f"{z['id']}: textumfang ungültig")
        a(int(z["seite"]) <= KONFIG["seiten"], f"{z['id']}: Seite größer als der Heftumfang")
        for wert, menge, name in ((z["format"], FORMATE, "format"), (z["antwort"], ANTWORTEN, "antwort"),
                                  (z["material"], MATERIAL, "material"), (z["zahlenraum"], ZAHLENRAUM, "zahlenraum")):
            for teil in [s for s in wert.split("|") if s]:
                a(teil in menge, f"{z['id']}: {name} hat unbekannten Wert: {teil}")
        for feld in ("typ", "typ_neben"):
            for t in [s for s in z[feld].split("|") if s]:
                verwendet.add(t)
                a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        for dep in [s for s in z["abhaengig_von"].split("|") if s]:
            a(dep in neue_ids or dep in alt_ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
        for k, v in z.items():
            a("?" not in v or k == "bemerkung" or z["bemerkung"].strip() != "",
              f"{z['id']}: Fragezeichen in {k} ohne Grund in bemerkung")
            a(not re.search(r"(?<=[\d\s(])-(?=\d)", v),
              f"{z['id']}: ASCII-Bindestrich als Minus in {k}")
            a(k in ("stichwoerter",) or not [w for w in UMSCHRIFT if w in v.lower()],
              f"{z['id']}: ASCII-Umschrift in {k}: {v[:40]}")
    a(not ({t[0] for t in NEUE_TYPEN} - verwendet),
      f"neue Typen unbenutzt: {sorted({t[0] for t in NEUE_TYPEN} - verwendet)}")

    if fehler:
        print(f"ABBRUCH – {len(fehler)} Fehler, nichts geschrieben:")
        for f_ in fehler:
            print(" -", f_)
        sys.exit(1)

    schreibe(KAT, HEAD, alt_kat + [[z[k] for k in HEAD] for z in ZEILEN])
    schreibe(TYP, TYP_HEAD, alt_typ + [[t[0], t[1], t[2], t[3], t[4], "neu"] for t in NEUE_TYPEN])

    # Rückweg: geschriebene Datei mit echtem Leser einlesen und vergleichen
    _, zurueck = lade(KAT, HEAD)
    for gel, z in zip(zurueck[len(alt_kat):], ZEILEN):
        if len(gel) != 37 or any(v != z[k] for k, v in zip(HEAD, gel)):
            sys.exit(f"{z['id']}: Rückweg verändert die Zeile")
    roh = io.open(KAT, encoding="utf-8", newline="").read()
    if "\r" in roh or not all(l.startswith('"') and l.endswith('"') for l in roh.splitlines()):
        sys.exit("Ausgabe nicht vollständig gequotet oder CRLF")

    # Prüftabelle
    print(f"Heft {KONFIG['jahr']} {KONFIG['papier']} – {len(ZEILEN)} Zeilen, "
          f"{len(NEUE_TYPEN)} Typen neu, Katalog jetzt {len(alt_kat) + len(ZEILEN)} Zeilen\n")
    print(f"{'id':<12} {'P':>2}  {'thema':<38} {'typ':<44} ergebnis")
    for z in ZEILEN:
        print(f"{z['id']:<12} {z['punkte']:>2}  {z['thema']:<38} {z['typ']:<44} {z['ergebnis'][:60]}")
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
