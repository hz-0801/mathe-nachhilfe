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
    "jahr": "2022",
    "papier": "B",
    "datei": "22_FOS_Ma_B_LH.pdf",
    "seiten": 10,
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
# Ein Eintrag je Teilaufgabe der Punktetabelle.

row(id="2022-B-1a", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="a", seite="2", punkte="5",
    leitidee="Differentialrechnung", thema="Ableitungen bilden",
    typ="Verhalten im Unendlichen bestimmen",
    typ_neben="Ableitung ganzrationale Funktion",
    stichwoerter="Grenzwert|ungerader Grad|positiver Leitkoeffizient|Potenzregel|dritte Ableitung",
    voraussetzungen="Summanden höchsten Grades erkennen",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Notieren Sie", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3x^3 − x^2 − 20x − 12; x aus IR",
    gesucht="Verhalten der Funktionswerte im Unendlichen|erste, zweite und dritte Ableitung von f",
    verfahren="am Summanden höchsten Grades das Verhalten für beide Richtungen ablesen, dann die Potenz-, Faktor- und Summenregel dreimal hintereinander anwenden",
    schritte="4", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="für x gegen +unendlich streben die Funktionswerte gegen +unendlich, für x gegen −unendlich gegen −unendlich|f'(x) = 9x^2 − 2x − 20|f''(x) = 18x − 2|f'''(x) = 18 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="bei ungeradem Grad für beide Richtungen dasselbe Vorzeichen angeben",
    bemerkung="Gutachten: Angabe der Grenzwerte 2 BE, Notieren der ersten drei Ableitungen 3 BE. thema nach dem Punkt-Schwerpunkt 3 zu 2 gewählt, der typ steht unter Verhalten im Unendlichen")

row(id="2022-B-1b", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="b", seite="2", punkte="5",
    leitidee="Differentialrechnung", thema="Nullstellen ganzrationaler Funktionen",
    typ="Nullstellen mit Polynomdivision",
    typ_neben="Schnittpunkt mit der y-Achse berechnen",
    stichwoerter="Probierlösung|Polynomdivision|Lösungsformel|y-Achsenabschnitt|Bruchlösung",
    voraussetzungen="eine Nullstelle durch Probieren finden|Linearfaktor abspalten",
    format="Rechnung", operator="Bestimmen Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3x^3 − x^2 − 20x − 12; x aus IR",
    gesucht="alle Nullstellen von Gf|Schnittpunkt mit der y-Achse",
    verfahren="durch Probieren eine ganzzahlige Nullstelle finden, den zugehörigen Linearfaktor abspalten, die verbleibende quadratische Gleichung mit der Lösungsformel lösen und für den y-Achsenschnitt x = 0 einsetzen",
    schritte="4", zahlenraum="ganz|Bruch|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Nullstellen x1 = 3, x2 = −2/3 und x3 = −2|Sy(0; −12) (amtlich)",
    zwischenergebnis="Probierlösung x1 = 3|Polynomdivision durch x − 3 ergibt 3x^2 + 8x + 4",
    niveau_geschaetzt="II",
    fehlerquelle="vor der Lösungsformel nicht durch den Faktor 3 teilen und mit falschen Koeffizienten rechnen",
    bemerkung="Gutachten: Bestimmen aller Nullstellen 4 BE, Angabe des Schnittpunktes mit der y-Achse 1 BE. Der Erwartungshorizont nennt als Alternative das Abspalten von x + 2 mit dem Restterm 3x^2 − 7x − 6")

row(id="2022-B-1c", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="c", seite="2", punkte="7",
    leitidee="Differentialrechnung", thema="Extrem- und Sattelpunkte",
    typ="Extrem- und Sattelpunkte über zweite Ableitung",
    typ_neben="Monotonieverhalten angeben",
    stichwoerter="notwendige Bedingung|hinreichende Bedingung|Lösungsformel|Hochpunkt|Tiefpunkt|Monotonieintervalle",
    voraussetzungen="Ableitungen aus Teilaufgabe a verwenden|Intervallgrenzen aus den Extremstellen bilden",
    format="Rechnung|Kurzantwort", operator="Ermitteln Sie|Geben Sie an", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 3x^3 − x^2 − 20x − 12; x aus IR; als Kontrolle sind die Extremstellen x1 ungefähr 1,61 und x2 ungefähr −1,38 genannt",
    gesucht="Koordinaten aller Extrempunkte von Gf|Monotonieverhalten der Funktion f",
    verfahren="die erste Ableitung null setzen und mit der Lösungsformel die beiden Stellen berechnen, das Vorzeichen der zweiten Ableitung dort prüfen, die Funktionswerte berechnen und aus den Extremstellen die drei Monotonieintervalle ablesen",
    schritte="5", zahlenraum="dezimal|negativ|Potenz|Wurzel", einheiten="", abhaengig_von="2022-B-1a",
    ergebnis="T(1,61; −34,27)|H(−1,38; 5,81)|f ist streng monoton steigend für x < −1,38, streng monoton fallend für −1,38 < x < 1,61 und streng monoton steigend für x > 1,61 (amtlich)",
    zwischenergebnis="f''(1,61) = 26,98 und f''(−1,38) = −26,84",
    niveau_geschaetzt="II",
    fehlerquelle="aus dem positiven Wert der zweiten Ableitung auf einen Hochpunkt schließen und beide Punkte vertauschen",
    bemerkung="Gutachten: Berechnen der Extremstellen 2 BE, Nachweis der Art samt Koordinaten 3 BE, Angabe des Monotonieverhaltens 2 BE")

row(id="2022-B-1d", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="d", seite="2", punkte="5",
    leitidee="Differentialrechnung", thema="Wendepunkte",
    typ="Wendepunkte über zweite Ableitung",
    typ_neben="Krümmungsverhalten angeben",
    stichwoerter="zweite Ableitung null setzen|dritte Ableitung|Rechtskrümmung|Linkskrümmung|Bruchstelle",
    voraussetzungen="Ableitungen aus Teilaufgabe a verwenden",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 3x^3 − x^2 − 20x − 12; x aus IR",
    gesucht="Koordinaten des Wendepunktes von Gf|Krümmungsverhalten des Graphen",
    verfahren="die zweite Ableitung null setzen, über die von null verschiedene dritte Ableitung den Wendepunkt nachweisen, den Funktionswert berechnen und links und rechts der Wendestelle das Vorzeichen der zweiten Ableitung deuten",
    schritte="4", zahlenraum="Bruch|dezimal|negativ", einheiten="", abhaengig_von="2022-B-1a",
    ergebnis="W(0,11; −14,23)|Rechtskrümmung für x < 1/9 und Linkskrümmung für x > 1/9 (amtlich)",
    zwischenergebnis="Wendestelle x = 1/9 ungefähr 0,11|f'''(x) = 18 ungleich 0",
    niveau_geschaetzt="II",
    fehlerquelle="Rechts- und Linkskrümmung vertauschen, weil das Vorzeichen der zweiten Ableitung falsch gedeutet wird",
    bemerkung="Gutachten: Nachweis des Wendepunktes samt Koordinaten 3 BE, Angabe des Krümmungsverhaltens 2 BE")

row(id="2022-B-1e", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="e", seite="2", punkte="3",
    leitidee="Differentialrechnung", thema="Graph zeichnen und zuordnen",
    typ="Graph ganzrationaler Funktion im Intervall zeichnen", typ_neben="",
    stichwoerter="Intervall|Achseneinteilung|markante Punkte|großer Wertebereich",
    voraussetzungen="Ergebnisse der Teilaufgaben b bis d eintragen|Achsen unterschiedlich einteilen",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="keins",
    skizze="der Prüfling legt das Koordinatensystem selbst an; entstehen soll der Verlauf mit den Nullstellen −2, −2/3 und 3, dem Hochpunkt (−1,38; 5,81), dem Wendepunkt (0,11; −14,23) und dem Tiefpunkt (1,61; −34,27), Randwerte f(−2) = 0 und f(3) = 0",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3x^3 − x^2 − 20x − 12; x aus IR; zu zeichnen im Intervall −2 <= x <= 3; auf eine geeignete Achseneinteilung ist zu achten",
    gesucht="Graph von f im angegebenen Intervall",
    verfahren="die berechneten Nullstellen, den Hochpunkt, den Wendepunkt und den Tiefpunkt eintragen und den Verlauf durchzeichnen, dabei die y-Achse wegen des Wertebereichs von rund −34 bis rund 6 gröber einteilen als die x-Achse",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="",
    abhaengig_von="2022-B-1b|2022-B-1c|2022-B-1d",
    ergebnis="Graph durch (−2; 0), H(−1,38; 5,81), (−2/3; 0), W(0,11; −14,23), T(1,61; −34,27) und (3; 0) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="beide Achsen gleich einteilen und den Tiefpunkt bei −34,27 nicht mehr auf das Blatt bekommen",
    bemerkung="Gutachten: Zeichnen des Graphen 3 BE. Der Aufgabentext verlangt ausdrücklich eine geeignete Achseneinteilung, weil x- und y-Bereich stark verschieden sind")

row(id="2022-B-1f", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="f", seite="2", punkte="5",
    leitidee="Differentialrechnung", thema="Normale",
    typ="Funktionswert an einer Stelle berechnen",
    typ_neben="Anstieg des Graphen an einer Stelle berechnen|Normalengleichung im Punkt",
    stichwoerter="Funktionswert einsetzen|Ableitungswert|negativer Kehrwert|Normalengleichung|y-Achsenabschnitt",
    voraussetzungen="erste Ableitung aus Teilaufgabe a verwenden|Punkt in die Geradengleichung einsetzen",
    format="Rechnung", operator="Berechnen Sie|Ermitteln Sie", antwort="Zahl|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 3x^3 − x^2 − 20x − 12; x aus IR; der Punkt P(1; yP) liegt auf Gf",
    gesucht="Funktionswert yP|Anstieg des Graphen in P|Gleichung der Normalen von Gf im Punkt P",
    verfahren="x = 1 in f einsetzen, x = 1 in die erste Ableitung einsetzen, den negativen Kehrwert des Ableitungswerts als Anstieg der Normalen bilden und den Punkt P einsetzen, um den y-Achsenabschnitt zu bestimmen",
    schritte="4", zahlenraum="ganz|Bruch|dezimal|negativ", einheiten="", abhaengig_von="2022-B-1a",
    ergebnis="yP = −30|Anstieg f'(1) = −13|Normale n(x) = (1/13)x − 30,08 (amtlich)",
    zwischenergebnis="Anstieg der Normalen 1/13|y-Achsenabschnitt n ungefähr −30,08",
    niveau_geschaetzt="II",
    fehlerquelle="den Anstieg der Tangente statt den negativen Kehrwert in die Normalengleichung einsetzen",
    bemerkung="Gutachten: Berechnen von Funktionswert und Anstieg 2 BE, Ermitteln der Normalengleichung 3 BE. thema nach dem Punkt-Schwerpunkt 3 zu 2 gewählt, der typ steht unter Schnittpunkte von Funktionsgraphen")

row(id="2022-B-2a", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="a", seite="5", punkte="7",
    leitidee="Differentialrechnung", thema="Schnittpunkte von Funktionsgraphen",
    typ="Schnittpunkte zweier Funktionsgraphen berechnen",
    typ_neben="Nullstellen über Substitution biquadratisch",
    stichwoerter="gleichsetzen|Substitution|Lösungsformel|negative Hilfslösung verwerfen|Kontrollergebnis",
    voraussetzungen="Brüche und Dezimalzahlen gemeinsam zusammenfassen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Werbetechnik/Pappaufsteller", textumfang="mittel",
    gegeben="der obere Teil des Aufstellers wird durch g(x) = −(1/8)x^4 + (1/4)x^2 + 3/2 beschrieben, der untere durch f(x) = 0,5x^4 − 1,5x^2 − 1,5; x aus IR; als Kontrolle sind x1 = −2 und x2 = 2 genannt",
    gesucht="Koordinaten der gemeinsamen Schnittpunkte der Graphen Gf und Gg",
    verfahren="beide Terme gleichsetzen und auf null bringen, x^2 = z substituieren, die quadratische Gleichung lösen, die negative Hilfslösung verwerfen, zurücksubstituieren und die Funktionswerte berechnen",
    schritte="5", zahlenraum="Bruch|dezimal|negativ|Potenz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="S1(−2; 0,5) und S2(2; 0,5) (amtlich)",
    zwischenergebnis="0 = (5/8)x^4 − (7/4)x^2 − 3|z1 = 4 und z2 = −1,2|x1/2 = ±2",
    niveau_geschaetzt="II",
    fehlerquelle="auch die negative Hilfslösung z2 zurücksubstituieren und zwei weitere Schnittpunkte behaupten",
    bemerkung="Gutachten: Gleichsetzen und Substituieren 2 BE, Lösen der quadratischen Gleichung 3 BE, Berechnen der Funktionswerte und Angabe der Schnittpunkte 2 BE")

row(id="2022-B-2b", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="b", seite="5", punkte="4",
    leitidee="Grundlagen", thema="Größen und Einheiten",
    typ="Streckenlänge im Koordinatensystem in Meter umrechnen",
    typ_neben="Prozentsatz aus Anteil berechnen",
    stichwoerter="Längeneinheit|Maßstab 20 cm|Abstand zweier Schnittpunkte|Verschnitt|Prozentsatz",
    voraussetzungen="Schnittpunkte aus Teilaufgabe a verwenden|y-Achsenabschnitte beider Funktionen bilden",
    format="Rechnung", operator="Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="Skizze",
    skizze="Abbildung 2 zeigt die Umrisszeichnung des Zahns mit einer waagerechten Leiste 1 auf Höhe der beiden Schnittpunkte und einer senkrechten Leiste 2 auf der Mittelachse zwischen oberem und unterem Rand",
    kontext="Werbetechnik/Pappaufsteller", textumfang="mittel",
    gegeben="eine Längeneinheit entspricht 20 cm in der Wirklichkeit; Leiste 1 verläuft waagerecht zwischen den Schnittpunkten S1(−2; 0,5) und S2(2; 0,5), Leiste 2 senkrecht zwischen den y-Achsenschnittpunkten von Gg und Gf; beide Leisten werden aus einem 1,50 m langen Stück geschnitten",
    gesucht="Länge der waagerechten Leiste 1|Länge der senkrechten Leiste 2|Verschnitt in Prozent",
    verfahren="die Abstände in Längeneinheiten ablesen, jeweils mit 20 cm multiplizieren, beide Längen vom 150 cm langen Stück abziehen und den Rest durch 150 teilen",
    schritte="4", zahlenraum="ganz|dezimal|Prozent", einheiten="LE|cm|m|%", abhaengig_von="2022-B-2a",
    ergebnis="Leiste 1 ist 80 cm lang|Leiste 2 ist 60 cm lang|Verschnitt rund 6,67 % (amtlich)",
    zwischenergebnis="Abstand der Schnittstellen 4 LE|Abstand der y-Achsenschnittpunkte 3 LE, weil g(0) = 1,5 und f(0) = −1,5|Rest 10 cm",
    niveau_geschaetzt="II",
    fehlerquelle="den Verschnitt auf die Summe der Leisten statt auf die 150 cm beziehen",
    bemerkung="Gutachten: waagerechte Leiste 1 BE, senkrechte Leiste 2 BE, Verschnitt 1 BE. leitidee Grundlagen, weil Umrechnung und Prozentrechnung den Inhalt stellen, nicht die Analysis")

row(id="2022-B-2c", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="c", seite="5", punkte="2",
    leitidee="Differentialrechnung", thema="Graph zeichnen und zuordnen",
    typ="Koordinatenachsen in eine Abbildung einzeichnen", typ_neben="",
    stichwoerter="Symmetrieachse|Achseneinteilung|Lage des Ursprungs|Umrisszeichnung",
    voraussetzungen="aus den Funktionstermen auf die Lage der y-Achse schließen",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Skizze",
    skizze="Abbildung 1 zeigt die Umrisszeichnung des Zahns auf einem blassen Gitter, ohne Achsen und ohne Beschriftung; einzuzeichnen sind x- und y-Achse mit passender Einteilung",
    kontext="Werbetechnik/Pappaufsteller", textumfang="kurz",
    gegeben="g(x) = −(1/8)x^4 + (1/4)x^2 + 3/2 und f(x) = 0,5x^4 − 1,5x^2 − 1,5; x aus IR; Abbildung 1 zeigt den Umriss des Aufstellers ohne Koordinatensystem",
    gesucht="ein geeignetes kartesisches Koordinatensystem mit entsprechender Achseneinteilung in Abbildung 1",
    verfahren="beide Terme sind achsensymmetrisch, also die y-Achse durch die Symmetrieachse der Figur legen und die x-Achse so, dass die berechneten Funktionswerte zur Umrisszeichnung passen",
    schritte="2", zahlenraum="Bruch|dezimal|negativ", einheiten="LE", abhaengig_von="2022-B-2a",
    ergebnis="y-Achse auf der Symmetrieachse der Figur, x-Achse so, dass der obere Rand bei 1,5 und der untere bei −1,5 liegt und die Schnittpunkte bei x = ±2 auf Höhe 0,5 fallen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die x-Achse an den unteren Rand der Figur legen und dadurch negative Funktionswerte verlieren",
    bemerkung="Gutachten: Skizzieren des Koordinatensystems 2 BE")

row(id="2022-B-2d", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="d", seite="5", punkte="7",
    leitidee="Grundlagen", thema="Größen und Einheiten",
    typ="Fläche zwischen zwei Graphen berechnen",
    typ_neben="Flächeninhalt im Koordinatensystem in Quadratmeter umrechnen|Preis aus Fläche und Quadratmeterpreis berechnen",
    stichwoerter="Differenzfunktion|bestimmtes Integral|Nachweis|beidseitiger Druck|quadrierter Maßstab|Druckkosten",
    voraussetzungen="Integrationsgrenzen aus den Schnittstellen nehmen|eine Flächeneinheit als 400 cm^2 deuten",
    format="Rechnung", operator="Weisen Sie nach|Berechnen Sie", antwort="Zahl",
    material="Skizze",
    skizze="Abbildung 1 zeigt die zu berechnende Zahnfläche als geschlossene Umrisszeichnung zwischen dem oberen Bogen und den beiden unteren Zacken",
    kontext="Werbetechnik/Druckkosten", textumfang="lang",
    gegeben="g(x) = −(1/8)x^4 + (1/4)x^2 + 3/2 und f(x) = 0,5x^4 − 1,5x^2 − 1,5; die Schnittstellen liegen bei x = ±2; eine Längeneinheit entspricht 20 cm; der Aufsteller wird beidseitig bedruckt; der Druck kostet 25 Euro pro Quadratmeter; nachzuweisen ist der Flächeninhalt 40/3 Flächeneinheiten",
    gesucht="Nachweis des Flächeninhalts von 40/3 FE|Größe der beidseitig zu bedruckenden Fläche in cm^2|entstehende Druckkosten",
    verfahren="die Differenz der beiden Terme integrieren und an den Grenzen −2 und 2 auswerten, die Maßzahl mit dem quadrierten Maßstab in Quadratzentimeter umrechnen und verdoppeln, dann in Quadratmeter umrechnen und mit 25 Euro multiplizieren",
    schritte="6", zahlenraum="Bruch|dezimal|negativ|Potenz", einheiten="FE|LE|cm^2|m^2|€",
    abhaengig_von="2022-B-2a",
    ergebnis="Flächeninhalt 40/3 FE|zu bedruckende Fläche 32 000/3 cm^2, rund 10 666,67 cm^2|Druckkosten 80/3 Euro, rund 26,67 € (amtlich)",
    zwischenergebnis="Stammfunktion (1/8)x^5 − (7/12)x^3 − 3x mit den Werten −20/3 und 20/3|eine Flächeneinheit entspricht 400 cm^2|32 000/3 cm^2 sind 16/15 m^2",
    niveau_geschaetzt="III",
    fehlerquelle="beim Umrechnen den Maßstab nicht quadrieren und mit 20 statt mit 400 multiplizieren",
    bemerkung="Gutachten: Nachweis des Flächeninhalts 3 BE, Berechnen der zu bedruckenden Fläche 2 BE, Berechnen der Druckkosten 2 BE. thema nach dem Punkt-Schwerpunkt 4 zu 3 gewählt, der typ steht unter Fläche zwischen zwei Graphen")

row(id="2022-B-3a", aufgabe="3", titel="Stochastik",
    teilaufgabe="a", seite="7", punkte="3",
    leitidee="Stochastik", thema="Laplace-Wahrscheinlichkeit",
    typ="Ergebnismenge eines Zufallsexperiments angeben",
    typ_neben="Laplace-Bedingung begründen",
    stichwoerter="Ergebnismenge|geordnete Paare|zweimaliges Drehen|gleich wahrscheinlich|Laplace-Experiment",
    voraussetzungen="Reihenfolge der beiden Drehungen beachten",
    format="Kurzantwort|Begründung", operator="Stellen Sie auf|Entscheiden und begründen Sie",
    antwort="Text",
    material="Skizze",
    skizze="Abbildung 1 zeigt Glücksrad 1 als Kreis mit drei gleich großen Sektoren, beschriftet mit 5, 3 und 2",
    kontext="Glücksspiel/Glücksrad", textumfang="mittel",
    gegeben="Glücksrad 1 hat drei gleich große Sektoren mit den Zahlen 2, 3 und 5; es wird pro Spiel zweimal gedreht",
    gesucht="geeignete Ergebnismenge für diesen Zufallsversuch|begründete Entscheidung, ob ein Laplace-Experiment vorliegt",
    verfahren="alle geordneten Paare aus den drei Zahlen bilden und begründen, dass alle neun Ergebnisse gleich wahrscheinlich sind, weil die Sektoren gleich groß sind",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Ergebnismenge aus den neun Paaren (2,2), (2,3), (2,5), (3,2), (3,3), (3,5), (5,2), (5,3) und (5,5)|es liegt ein Laplace-Experiment vor, weil alle Ergebnisse gleich wahrscheinlich sind (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Reihenfolge vernachlässigen und nur sechs statt neun Paare angeben",
    bemerkung="Gutachten: Aufstellen der Ergebnismenge und begründete Entscheidung zum Laplace-Experiment 3 BE")

row(id="2022-B-3b", aufgabe="3", titel="Stochastik",
    teilaufgabe="b", seite="7", punkte="3",
    leitidee="Stochastik", thema="Laplace-Wahrscheinlichkeit",
    typ="Laplace-Wahrscheinlichkeit berechnen",
    typ_neben="Gegenereignis in Worten formulieren",
    stichwoerter="mindestens einmal|nur ungerade Zahlen|günstige Ergebnisse abzählen|Gegenereignis",
    voraussetzungen="Ergebnismenge aus Teilaufgabe a nutzen|mindestens und höchstens unterscheiden",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl|Text",
    material="Skizze",
    skizze="Abbildung 1 zeigt Glücksrad 1 als Kreis mit drei gleich großen Sektoren, beschriftet mit 5, 3 und 2",
    kontext="Glücksspiel/Glücksrad", textumfang="mittel",
    gegeben="Glücksrad 1 mit den Zahlen 2, 3 und 5 wird pro Spiel zweimal gedreht; Ereignis A die Zahl 2 erscheint mindestens einmal; Ereignis B es werden nur ungerade Zahlen erzielt",
    gesucht="Wahrscheinlichkeit von A|Wahrscheinlichkeit von B|Gegenereignis von B in Worten",
    verfahren="in der neunelementigen Ergebnismenge die günstigen Paare abzählen und durch neun teilen, dann das Gegenereignis zu nur ungeraden Zahlen sprachlich formulieren",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="2022-B-3a",
    ergebnis="P(A) = 5/9, rund 0,56|P(B) = 4/9, rund 0,44|Gegenereignis von B: höchstens eine ungerade Zahl wird erzielt (amtlich)",
    zwischenergebnis="fünf der neun Paare enthalten mindestens eine 2, vier bestehen nur aus 3 und 5",
    niveau_geschaetzt="II",
    fehlerquelle="das Gegenereignis von B als keine ungerade Zahl statt als höchstens eine ungerade Zahl formulieren",
    bemerkung="Gutachten: Berechnen der beiden Wahrscheinlichkeiten 2 BE, Angabe des Gegenereignisses 1 BE")

row(id="2022-B-3c", aufgabe="3", titel="Stochastik",
    teilaufgabe="c", seite="7", punkte="4",
    leitidee="Stochastik", thema="Statistische Kenngrößen",
    typ="Mittelwert aus Werteliste",
    typ_neben="Standardabweichung aus Werteliste",
    stichwoerter="Augensummen|Stichprobe aus zehn Werten|arithmetisches Mittel|Varianz|Standardabweichung",
    voraussetzungen="Summe durch Anzahl teilen|Wurzel aus der Varianz ziehen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle",
    skizze="vorgedruckte einzeilige Tabelle mit den zehn Augensummen 8, 8, 5, 5, 4, 6, 6, 7, 10 und 7",
    kontext="Glücksspiel/Probelauf", textumfang="mittel",
    gegeben="beim Probelauf mit Glücksrad 1 ergaben sich nach zehn Spielen die Augensummen 8, 8, 5, 5, 4, 6, 6, 7, 10 und 7",
    gesucht="arithmetisches Mittel dieser Stichprobe|Standardabweichung dieser Stichprobe",
    verfahren="die zehn Werte summieren und durch zehn teilen, dann die quadratischen Abweichungen vom Mittelwert summieren, durch neun beziehungsweise durch zehn teilen und die Wurzel ziehen",
    schritte="3", zahlenraum="ganz|dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="Mittelwert 6,6|Standardabweichung rund 1,78 mit dem Nenner 9 beziehungsweise rund 1,69 mit dem Nenner 10 (amtlich)",
    zwischenergebnis="Summe 66|Summe der quadratischen Abweichungen 28,4|Varianz 142/45 rund 3,16",
    niveau_geschaetzt="II",
    fehlerquelle="gleiche Werte nur einmal zählen und durch die Zahl der verschiedenen Augensummen teilen",
    bemerkung="Gutachten: Berechnen des arithmetischen Mittelwerts 2 BE, Berechnen der Standardabweichung 2 BE. Anders als in 2022-C-3b und 2026-B-3a führt der Erwartungshorizont hier den Nenner n − 1 als Hauptweg und n als Alternative")

row(id="2022-B-3d", aufgabe="3", titel="Stochastik",
    teilaufgabe="d", seite="7", punkte="5",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zweistufig darstellen",
    typ_neben="Pfadregel zweistufig anwenden|Vertauschung der Reihenfolge bei unabhängigen Stufen begründen",
    stichwoerter="zwei verschiedene Glücksräder|ungleiche Sektoren|Pfadmultiplikation|Reihenfolge vertauschen|Kommutativität",
    voraussetzungen="aus den Sektorgrößen die Wahrscheinlichkeiten 1/2 und 1/4 ableiten",
    format="Zeichnen|Rechnung|Begründung",
    operator="Zeichnen Sie|Bestimmen Sie|Entscheiden und begründen Sie", antwort="Grafik|Zahl|Text",
    material="keins",
    skizze="der Prüfling zeichnet das Baumdiagramm selbst; entstehen soll ein zweistufiger Baum mit den drei Ästen 2, 3 und 5 zu je 1/3 in der ersten Stufe und darunter jeweils den Ästen 5 zu 1/2 sowie 7 und 10 zu je 1/4",
    kontext="Glücksspiel/zwei Glücksräder", textumfang="lang",
    gegeben="Glücksrad 1 hat drei gleich große Sektoren mit 2, 3 und 5; Glücksrad 2 hat drei Sektoren mit 5, 7 und 10, wobei die Sektoren mit 7 und 10 je 25 % einnehmen und der Sektor mit 5 die Hälfte; beide Räder werden nacheinander je einmal gedreht, begonnen wird mit Glücksrad 1",
    gesucht="Baumdiagramm für diesen Zufallsversuch|Wahrscheinlichkeit, dass beide Glücksräder die Zahl fünf zeigen|begründete Entscheidung, ob sich diese Wahrscheinlichkeit ändert, wenn mit Glücksrad 2 begonnen wird",
    verfahren="den zweistufigen Baum mit den Wahrscheinlichkeiten 1/3 in der ersten und 1/2 beziehungsweise 1/4 in der zweiten Stufe zeichnen, den Pfad 5 und 5 multiplizieren und begründen, dass die Vertauschung der Stufen nur die Reihenfolge der Faktoren ändert",
    schritte="4", zahlenraum="Bruch|dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(5; 5) = 1/6, rund 0,17|die Wahrscheinlichkeit ändert sich nicht, weil derselbe Pfad durchlaufen wird und nur die Faktoren vertauscht werden (amtlich)",
    zwischenergebnis="Glücksrad 2 liefert P(5) = 1/2 sowie P(7) = P(10) = 1/4",
    niveau_geschaetzt="II",
    fehlerquelle="für Glücksrad 2 alle drei Sektoren mit 1/3 ansetzen und die unterschiedlichen Sektorgrößen übersehen",
    bemerkung="Gutachten: Zeichnen des Baumdiagramms 3 BE, Bestimmen der Wahrscheinlichkeit und begründete Entscheidung zur Reihenfolge 2 BE. Zwei Stufen mit Zurücklegen, thema nach der Arbeitsregel in fhr.md Abschnitt 6")

row(id="2022-B-3e", aufgabe="3", titel="Stochastik",
    teilaufgabe="e", seite="7", punkte="3",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeitsverteilung der Augensumme aufstellen",
    typ_neben="Wahrscheinlichkeit über mehrere Pfade summieren",
    stichwoerter="alle Augensummen|Verteilung|gleiche Summe auf mehreren Wegen|einstellig",
    voraussetzungen="Summen mehrfach auftretender Paare zusammenfassen",
    format="Tabelle|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Tabelle|Zahl",
    material="keins",
    skizze="der Prüfling legt die Tabelle der Augensummen selbst an; entstehen soll eine zweizeilige Tabelle mit den Summen und ihren Wahrscheinlichkeiten",
    kontext="Glücksspiel/zwei Glücksräder", textumfang="mittel",
    gegeben="Glücksrad 1 mit 2, 3 und 5 zu je 1/3 und Glücksrad 2 mit 5 zu 1/2 sowie 7 und 10 zu je 1/4; beide Räder werden einmal gleichzeitig gedreht",
    gesucht="alle möglichen Augensummen und deren Wahrscheinlichkeiten|Wahrscheinlichkeit dafür, dass die Augensumme einstellig ist",
    verfahren="alle neun Paare bilden und ihre Summen berechnen, gleiche Summen durch Addition der Pfadwahrscheinlichkeiten zusammenfassen und anschließend die Wahrscheinlichkeiten der einstelligen Summen addieren",
    schritte="4", zahlenraum="ganz|Bruch|dezimal", einheiten="", abhaengig_von="2022-B-3d",
    ergebnis="Augensummen 7, 8, 9, 10, 12, 13 und 15 mit den Wahrscheinlichkeiten 1/6, 1/6, 1/12, 1/4, 1/6, 1/12 und 1/12|Wahrscheinlichkeit für eine einstellige Augensumme 5/12, rund 0,42 (amtlich)",
    zwischenergebnis="die Summe 10 entsteht auf zwei Wegen, 3 und 7 sowie 5 und 5, die Summe 12 ebenfalls, 2 und 10 sowie 5 und 7",
    niveau_geschaetzt="III",
    fehlerquelle="Summen, die auf zwei Wegen entstehen, nur einmal zählen und die Wahrscheinlichkeiten nicht addieren",
    bemerkung="Gutachten: Angabe aller Augensummen mit Wahrscheinlichkeiten 2 BE, Berechnen der Wahrscheinlichkeit für eine einstellige Summe 1 BE")

row(id="2022-B-3f", aufgabe="3", titel="Stochastik",
    teilaufgabe="f", seite="7", punkte="2",
    leitidee="Stochastik", thema="Mehrstufige Zufallsexperimente",
    typ="Wahrscheinlichkeit über mehrere Pfade summieren", typ_neben="",
    stichwoerter="vier Drehungen|gleiche Zahl viermal|drei günstige Pfade|Potenzen von Wahrscheinlichkeiten",
    voraussetzungen="Pfadwahrscheinlichkeit als vierte Potenz bilden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel/Glücksrad", textumfang="kurz",
    gegeben="Glücksrad 2 mit 5 zu 1/2 sowie 7 und 10 zu je 1/4 wird viermal hintereinander gedreht",
    gesucht="Wahrscheinlichkeit dafür, dass viermal die gleiche Zahl erscheint",
    verfahren="für jede der drei Zahlen die vierte Potenz ihrer Wahrscheinlichkeit bilden und die drei Werte addieren",
    schritte="2", zahlenraum="Bruch|dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Wahrscheinlichkeit 9/128, rund 0,07 (amtlich)",
    zwischenergebnis="(1/4)^4 + (1/4)^4 + (1/2)^4 = 1/256 + 1/256 + 1/16",
    niveau_geschaetzt="II",
    fehlerquelle="nur den Pfad mit der Zahl 5 betrachten und die beiden Viertelsektoren vergessen",
    bemerkung="Gutachten: Ermitteln der Wahrscheinlichkeit 2 BE. Vier Stufen mit Zurücklegen; kein eigener Typ nur wegen der Stufenzahl, der Kern ist die Summe über drei Pfade")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Funktionswert an einer Stelle berechnen", "Differentialrechnung", "Schnittpunkte von Funktionsgraphen",
     "Eine gegebene Stelle in den Funktionsterm einsetzen und den zugehörigen Funktionswert berechnen; Umkehrung zu Stelle zu gegebenem Funktionswert berechnen.",
     "2022-B-1f"),
    ("Prozentsatz aus Anteil berechnen", "Grundlagen", "Prozentrechnung",
     "Aus Prozentwert und Grundwert den Prozentsatz als Quotienten bestimmen und in Prozent angeben.",
     "2022-B-2b"),
    ("Vertauschung der Reihenfolge bei unabhängigen Stufen begründen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Begründen, dass die Wahrscheinlichkeit eines Pfades sich nicht ändert, wenn die Reihenfolge voneinander unabhängiger Stufen vertauscht wird, weil nur die Faktoren die Plätze tauschen.",
     "2022-B-3d"),
    ("Wahrscheinlichkeitsverteilung der Augensumme aufstellen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Zu einem zweistufigen Versuch alle möglichen Summen bilden, gleiche Summen durch Addition ihrer Pfadwahrscheinlichkeiten zusammenfassen und die Verteilung als Tabelle angeben.",
     "2022-B-3e"),
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
