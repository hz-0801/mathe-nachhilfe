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
    "jahr": "2021",
    "papier": "A",
    "datei": "21_FOS_Ma_LH_A.pdf",
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

row(id="2021-A-1a", aufgabe="1", titel="Differential- und Integralrechnung",
    teilaufgabe="a", seite="2", punkte="5",
    leitidee="Differentialrechnung", thema="Ableitungen bilden",
    typ="Verhalten im Unendlichen bestimmen",
    typ_neben="Ableitung ganzrationale Funktion",
    stichwoerter="Grenzwert|ungerader Grad|negativer Leitkoeffizient|Potenzregel|dritte Ableitung",
    voraussetzungen="Summanden höchsten Grades erkennen|Bruchkoeffizient ableiten",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Nennen Sie", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR",
    gesucht="Verhalten der Funktion f im Unendlichen|erste, zweite und dritte Ableitung von f",
    verfahren="am Summanden höchsten Grades für beide Richtungen den Grenzwert angeben, dann die Potenz-, Faktor- und Summenregel dreimal hintereinander anwenden",
    schritte="4", zahlenraum="Bruch|dezimal|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="für x gegen +unendlich streben die Funktionswerte gegen −unendlich, für x gegen −unendlich gegen +unendlich|f'(x) = −0,75x^2 + 4x − 1|f''(x) = −1,5x + 4|f'''(x) = −1,5 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="das Vorzeichen des negativen Leitkoeffizienten übersehen und beide Grenzwerte vertauschen",
    bemerkung="Erwartungshorizont: Angabe der Grenzwerte 2 BE, Notieren der ersten drei Ableitungen 3 BE. thema nach dem Punkt-Schwerpunkt 3 zu 2 gewählt, der typ steht unter Verhalten im Unendlichen")

row(id="2021-A-1b", aufgabe="1", titel="Differential- und Integralrechnung",
    teilaufgabe="b", seite="2", punkte="4",
    leitidee="Differentialrechnung", thema="Nullstellen ganzrationaler Funktionen",
    typ="Nullstellen mit Polynomdivision",
    typ_neben="Anstieg des Graphen an einer Stelle berechnen",
    stichwoerter="gegebene Nullstelle|Polynomdivision|Restterm ohne Lösung|Einzigkeit|Anstieg an der Nullstelle",
    voraussetzungen="Linearfaktor abspalten|eine Gleichung ohne reelle Lösung erkennen",
    format="Rechnung", operator="Weisen Sie nach|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR; x = 8 ist eine Nullstelle",
    gesucht="Nachweis, dass es außer x = 8 keine weiteren Nullstellen gibt|Anstieg des Graphen Gf an dieser Stelle",
    verfahren="den Linearfaktor x − 8 abspalten, den quadratischen Restterm null setzen und zeigen, dass die entstehende Gleichung keine reelle Lösung hat, dann x = 8 in die erste Ableitung einsetzen",
    schritte="3", zahlenraum="Bruch|ganz|negativ|Potenz", einheiten="", abhaengig_von="2021-A-1a",
    ergebnis="die Polynomdivision ergibt −0,25x^2 − 1, und −0,25x^2 − 1 = 0 führt auf x^2 = −4 ohne reelle Lösung, also ist x = 8 die einzige Nullstelle|f'(8) = −17 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="aus x^2 = −4 die Lösungen ±2 ziehen und zwei weitere Nullstellen behaupten",
    bemerkung="Erwartungshorizont: Nachweis der Einzigkeit 3 BE, Angabe des Anstiegs 1 BE")

row(id="2021-A-1c", aufgabe="1", titel="Differential- und Integralrechnung",
    teilaufgabe="c", seite="2", punkte="8",
    leitidee="Differentialrechnung", thema="Extrem- und Sattelpunkte",
    typ="Extrem- und Sattelpunkte über zweite Ableitung",
    typ_neben="Monotonieverhalten angeben",
    stichwoerter="notwendige Bedingung|Lösungsformel|Hochpunkt|Tiefpunkt|Monotonieintervalle",
    voraussetzungen="Ableitungen aus Teilaufgabe a verwenden|Gleichung durch den Leitkoeffizienten teilen",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR",
    gesucht="Koordinaten und Art aller Extrempunkte von Gf|Monotonieverhalten",
    verfahren="die erste Ableitung null setzen, durch −0,75 teilen und mit der Lösungsformel die beiden Stellen berechnen, dort das Vorzeichen der zweiten Ableitung prüfen, die Funktionswerte bestimmen und die drei Monotonieintervalle angeben",
    schritte="5", zahlenraum="dezimal|Bruch|negativ|Potenz|Wurzel", einheiten="", abhaengig_von="2021-A-1a",
    ergebnis="H(5,07; 21,76)|T(0,26; 7,87)|Gf ist streng monoton fallend für x < 0,26, streng monoton steigend für 0,26 < x < 5,07 und streng monoton fallend für x > 5,07 (amtlich)",
    zwischenergebnis="Extremstellen x1 ungefähr 5,07 und x2 ungefähr 0,26|f''(5,07) ungefähr −3,61 und f''(0,26) = 3,61",
    niveau_geschaetzt="II",
    fehlerquelle="die Monotonieintervalle nach dem Vorzeichen der zweiten statt der ersten Ableitung angeben",
    bemerkung="Erwartungshorizont: Berechnen der Extremstellen 3 BE, Art und Koordinaten 3 BE, Monotonieverhalten 2 BE")

row(id="2021-A-1d", aufgabe="1", titel="Differential- und Integralrechnung",
    teilaufgabe="d", seite="2", punkte="3",
    leitidee="Differentialrechnung", thema="Wendepunkte",
    typ="Wendepunkt aus vorgegebenen Punkten auswählen", typ_neben="",
    stichwoerter="vier Kandidaten|Bruchkoordinaten|zweite Ableitung prüfen|dritte Ableitung|mathematische Begründung",
    voraussetzungen="Ableitungen aus Teilaufgabe a verwenden|Brüche als x-Koordinaten einsetzen",
    format="Rechnung|Begründung", operator="Prüfen Sie|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR; zur Auswahl stehen W1(−1/3; 925/108), W2(7/3; 1445/108), W3(8/3; 400/27) und W4(8/3; 350/11)",
    gesucht="Prüfung, welcher der vier Punkte der Wendepunkt des Graphen ist, mit mathematischer Begründung",
    verfahren="die Wendestelle aus der zweiten Ableitung bestimmen, über die von null verschiedene dritte Ableitung den Wendepunkt bestätigen und den Funktionswert berechnen, dann mit den vier Kandidaten vergleichen",
    schritte="3", zahlenraum="Bruch|dezimal|negativ", einheiten="", abhaengig_von="2021-A-1a",
    ergebnis="W3(8/3; 400/27), rund (2,67; 14,81), ist der Wendepunkt, weil f''(8/3) = 0 und f'''(8/3) = −1,5 ungleich null gilt (amtlich)",
    zwischenergebnis="f''(8/3) = 0|f'''(8/3) = −1,5",
    niveau_geschaetzt="II",
    fehlerquelle="W4 wählen, weil die x-Koordinate stimmt, und den Funktionswert nicht nachrechnen",
    bemerkung="Erwartungshorizont: Prüfung und Begründung 3 BE. W3 und W4 haben dieselbe x-Koordinate und unterscheiden sich nur im Funktionswert")

row(id="2021-A-1e", aufgabe="1", titel="Differential- und Integralrechnung",
    teilaufgabe="e", seite="2", punkte="4",
    leitidee="Differentialrechnung", thema="Schnittpunkte von Funktionsgraphen",
    typ="Stelle zu gegebenem Funktionswert berechnen", typ_neben="",
    stichwoerter="gegebener Funktionswert 8|Ausklammern|Lösungsformel|zwei weitere Stellen",
    voraussetzungen="den Funktionsterm dem Wert gleichsetzen|x ausklammern",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR; der Punkt Sy(0; 8) liegt auf Gf",
    gesucht="x-Koordinaten der beiden weiteren Punkte von Gf mit dem Funktionswert y = 8",
    verfahren="den Funktionsterm gleich 8 setzen, die 8 auf beiden Seiten streichen, x ausklammern und die verbleibende quadratische Gleichung mit der Lösungsformel lösen",
    schritte="3", zahlenraum="dezimal|Bruch|negativ|Potenz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="x2 ungefähr 7,46 und x3 ungefähr 0,54 (amtlich)",
    zwischenergebnis="x · (−0,25x^2 + 2x − 1) = 0 mit der bekannten Lösung x1 = 0|x^2 − 8x + 4 = 0",
    niveau_geschaetzt="II",
    fehlerquelle="die durch Ausklammern gewonnene Lösung x = 0 als eine der beiden gesuchten Stellen angeben",
    bemerkung="Erwartungshorizont: Ermitteln der beiden Stellen 4 BE. Die Lösung x1 = 0 gehört zum bereits gegebenen Punkt Sy und zählt nicht mit")

row(id="2021-A-1f", aufgabe="1", titel="Differential- und Integralrechnung",
    teilaufgabe="f", seite="2", punkte="3",
    leitidee="Differentialrechnung", thema="Graph zeichnen und zuordnen",
    typ="Graph ganzrationaler Funktion im Intervall zeichnen", typ_neben="",
    stichwoerter="Intervall|Achseneinteilung|Hochpunkt|Tiefpunkt|Wendepunkt|einzige Nullstelle",
    voraussetzungen="Ergebnisse der Teilaufgaben b bis e eintragen",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="keins",
    skizze="der Prüfling legt das Koordinatensystem selbst an; entstehen soll der Verlauf mit dem Tiefpunkt (0,26; 7,87), dem Wendepunkt (2,67; 14,81), dem Hochpunkt (5,07; 21,76) und der einzigen Nullstelle bei x = 8",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR; zu zeichnen im Intervall −2 <= x <= 8",
    gesucht="Graph von f im angegebenen Intervall",
    verfahren="die Nullstelle, den Tiefpunkt, den Wendepunkt und den Hochpunkt eintragen, den y-Achsenschnitt bei 8 ergänzen und den Verlauf durchzeichnen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="",
    abhaengig_von="2021-A-1b|2021-A-1c|2021-A-1d",
    ergebnis="Graph durch (−2; 20), Sy(0; 8), T(0,26; 7,87), W(2,67; 14,81), H(5,07; 21,76) und (8; 0) (amtlich)",
    zwischenergebnis="f(−2) = 2 + 8 + 2 + 8 = 20",
    niveau_geschaetzt="II",
    fehlerquelle="die x-Achse nur bis 5 einteilen und die Nullstelle bei x = 8 nicht mehr darstellen",
    bemerkung="Erwartungshorizont: Zeichnen des Graphen 3 BE")

row(id="2021-A-1g", aufgabe="1", titel="Differential- und Integralrechnung",
    teilaufgabe="g", seite="2", punkte="3",
    leitidee="Integralrechnung", thema="Fläche zwischen Graph und x-Achse",
    typ="Fläche zwischen Graph und x-Achse berechnen", typ_neben="",
    stichwoerter="Fläche mit beiden Achsen|Integrationsgrenzen null und acht|Stammfunktion|Flächeneinheiten",
    voraussetzungen="die Nullstelle als obere Grenze und die y-Achse als untere Grenze erkennen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/4)x^3 + 2x^2 − x + 8; x aus IR; Gf schließt zusammen mit den beiden Koordinatenachsen eine Fläche vollständig ein; die einzige Nullstelle liegt bei x = 8",
    gesucht="Maßzahl des Flächeninhalts dieser Fläche",
    verfahren="die Stammfunktion bilden und von null bis zur Nullstelle acht integrieren",
    schritte="2", zahlenraum="Bruch|dezimal|negativ|Potenz", einheiten="FE",
    abhaengig_von="2021-A-1b",
    ergebnis="Flächeninhalt 352/3 FE, rund 117,33 FE (amtlich)",
    zwischenergebnis="Stammfunktion −(1/16)x^4 + (2/3)x^3 − 0,5x^2 + 8x",
    niveau_geschaetzt="II",
    fehlerquelle="die untere Grenze bei −2 statt bei null ansetzen, weil das Zeichenintervall dort beginnt",
    bemerkung="Erwartungshorizont: Berechnen des Flächeninhalts 3 BE")

row(id="2021-A-2a", aufgabe="2", titel="Anwendung der Differential- und Integralrechnung",
    teilaufgabe="a", seite="5", punkte="7",
    leitidee="Differentialrechnung", thema="Funktionsgleichung bestimmen",
    typ="Funktionsgleichung mit Symmetriebedingung über LGS",
    typ_neben="Funktionsgleichung mit Extremalbedingung über LGS",
    stichwoerter="Funktion vierten Grades|Achsensymmetrie|nur gerade Exponenten|Tiefpunktbedingung|LGS|Kontrollergebnis",
    voraussetzungen="aus der Achsensymmetrie den Ansatz ohne ungerade Exponenten bilden|Tiefpunkt als Extremalbedingung übersetzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="Skizze",
    skizze="Abbildung 2 zeigt den Querschnitt der neuen Luftkammerdichtung als geschlossene Form aus einem oberen Bogen und einem unteren, in der Mitte eingedellten Rand",
    kontext="Bauteil/Gummidichtung", textumfang="lang",
    gegeben="der untere Teil des Querschnitts wird durch den Graphen Gf einer Funktion vierten Grades beschrieben; Gf ist achsensymmetrisch zur y-Achse und verläuft durch P(0; −1,5) sowie den Tiefpunkt T(1; −2); als Kontrolle ist f(x) = 0,5x^4 − x^2 − 1,5 genannt",
    gesucht="eine zugehörige Funktionsgleichung für f",
    verfahren="wegen der Achsensymmetrie den Ansatz mit nur geraden Exponenten aufstellen, die Ableitung bilden und aus dem Punkt P, dem Funktionswert im Tiefpunkt und der Bedingung, dass die Ableitung dort null ist, ein Gleichungssystem für die drei Koeffizienten aufstellen und lösen",
    schritte="5", zahlenraum="dezimal|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f(x) = 0,5x^4 − x^2 − 1,5 (amtlich)",
    zwischenergebnis="Ansatz f(x) = ax^4 + bx^2 + c mit f'(x) = 4ax^3 + 2bx|c = −1,5 aus P|a + b + c = −2 aus dem Funktionswert im Tiefpunkt|4a + 2b = 0 aus der Extremalbedingung",
    niveau_geschaetzt="III",
    fehlerquelle="den allgemeinen Ansatz vierten Grades mit fünf Koeffizienten wählen und die Achsensymmetrie nicht als Vereinfachung nutzen",
    bemerkung="Erwartungshorizont: Ansatz und Ableitung 2 BE, Aufstellen des Gleichungssystems 3 BE, Lösen 2 BE")

row(id="2021-A-2b", aufgabe="2", titel="Anwendung der Differential- und Integralrechnung",
    teilaufgabe="b", seite="5", punkte="4",
    leitidee="Differentialrechnung", thema="Schnittpunkte von Funktionsgraphen",
    typ="Schnittpunkte zweier Funktionsgraphen berechnen", typ_neben="",
    stichwoerter="gleichsetzen|quadratische Glieder heben sich|vierte Wurzel|zwei Schnittpunkte",
    voraussetzungen="Funktionsgleichung aus Teilaufgabe a verwenden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze",
    skizze="Abbildung 2 zeigt den Querschnitt der Luftkammerdichtung; die Schnittpunkte liegen an den beiden seitlichen Spitzen der Luftkammer",
    kontext="Bauteil/Gummidichtung", textumfang="mittel",
    gegeben="g(x) = −x^2 + 2 beschreibt den oberen Teil des Querschnitts, f(x) = 0,5x^4 − x^2 − 1,5 den unteren; x aus IR",
    gesucht="Koordinaten der gemeinsamen Schnittpunkte der Graphen Gf und Gg",
    verfahren="beide Terme gleichsetzen, wobei sich die quadratischen Glieder aufheben, die verbleibende Gleichung nach x^4 auflösen, die vierte Wurzel ziehen und die Funktionswerte berechnen",
    schritte="4", zahlenraum="dezimal|negativ|Potenz|Wurzel", einheiten="", abhaengig_von="2021-A-2a",
    ergebnis="S1(−1,63; −0,66) und S2(1,63; −0,66) (amtlich)",
    zwischenergebnis="0,5x^4 − 3,5 = 0|x^4 = 7|x1/2 ungefähr ±1,63",
    niveau_geschaetzt="II",
    fehlerquelle="aus x^4 = 7 die Quadratwurzel statt der vierten Wurzel ziehen",
    bemerkung="Erwartungshorizont: Berechnen der Schnittpunkte 4 BE. Der Erwartungshorizont weist selbst darauf hin, dass sich mit der exakten x-Koordinate oder über f Abweichungen in der zweiten Dezimalstelle von y ergeben können; eigene Rechnung mit der exakten Stelle liefert −0,65 statt −0,66")

row(id="2021-A-2c", aufgabe="2", titel="Anwendung der Differential- und Integralrechnung",
    teilaufgabe="c", seite="5", punkte="3",
    leitidee="Grundlagen", thema="Größen und Einheiten",
    typ="Streckenlänge im Koordinatensystem in Meter umrechnen", typ_neben="",
    stichwoerter="Maßstab 0,5 cm je Längeneinheit|Gesamthöhe|Gesamtbreite|Tiefpunkt und Scheitelpunkt|Differenz der Schnittstellen",
    voraussetzungen="Scheitelpunkt von Gg ablesen|Schnittstellen aus Teilaufgabe b verwenden",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze",
    skizze="Abbildung 2 zeigt den Querschnitt der Luftkammerdichtung mit dem höchsten Punkt auf der y-Achse und dem tiefsten Punkt der unteren Begrenzung",
    kontext="Bauteil/Gummidichtung", textumfang="mittel",
    gegeben="g(x) = −x^2 + 2 mit dem Scheitelpunkt S(0; 2) und f(x) = 0,5x^4 − x^2 − 1,5 mit dem Tiefpunkt T(1; −2); die Schnittstellen liegen bei x ungefähr ±1,63; eine Längeneinheit entspricht 0,5 cm in der Wirklichkeit",
    gesucht="Gesamthöhe einer solchen Gummidichtung|Gesamtbreite einer solchen Gummidichtung",
    verfahren="den senkrechten Abstand zwischen dem Tiefpunkt von Gf und dem Scheitelpunkt von Gg in Längeneinheiten bestimmen, den waagerechten Abstand der beiden Schnittstellen ebenso, und beide Werte mit 0,5 cm multiplizieren",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="LE|cm", abhaengig_von="2021-A-2b",
    ergebnis="Gesamthöhe 2 cm|Gesamtbreite 1,63 cm (amtlich)",
    zwischenergebnis="Höhendifferenz 4 LE|Breitendifferenz 3,26 LE",
    niveau_geschaetzt="II",
    fehlerquelle="die Längeneinheiten ohne Maßstab als Zentimeter übernehmen und 4 cm beziehungsweise 3,26 cm angeben",
    bemerkung="Erwartungshorizont: Bestimmen von Gesamthöhe und Gesamtbreite 3 BE")

row(id="2021-A-2d", aufgabe="2", titel="Anwendung der Differential- und Integralrechnung",
    teilaufgabe="d", seite="5", punkte="6",
    leitidee="Integralrechnung", thema="Fläche zwischen zwei Graphen",
    typ="Fläche zwischen zwei Graphen berechnen",
    typ_neben="Flächeninhalt im Koordinatensystem in Quadratmeter umrechnen|Volumen aus Querschnittsfläche und Länge",
    stichwoerter="Differenzfunktion|bestimmtes Integral|quadrierter Maßstab|Rolle von acht Metern|Luftvolumen",
    voraussetzungen="Schnittstellen als Integrationsgrenzen nehmen|eine Flächeneinheit als 0,25 cm^2 deuten",
    format="Rechnung", operator="Zeigen Sie|Geben Sie an", antwort="Zahl",
    material="Skizze",
    skizze="Abbildung 2 zeigt den Querschnitt der Luftkammerdichtung; die Luftkammer ist die zwischen oberem und unterem Rand eingeschlossene Fläche",
    kontext="Bauteil/Gummidichtung", textumfang="lang",
    gegeben="g(x) = −x^2 + 2 und f(x) = 0,5x^4 − x^2 − 1,5; die Schnittstellen liegen bei x ungefähr ±1,63; eine Längeneinheit entspricht 0,5 cm; die Materialstärke bleibt unberücksichtigt; die Dichtungen werden auf Rollen von 8 m Länge geliefert; zu zeigen ist ein Querschnittsflächeninhalt von etwa 2,28 cm^2",
    gesucht="Nachweis des Querschnittsflächeninhalts von etwa 2,28 cm^2|Luftvolumen, das auf einer Rolle in der Luftkammer eingeschlossen ist",
    verfahren="die Differenz beider Terme zwischen den Schnittstellen integrieren und den Betrag nehmen, die Maßzahl mit dem quadrierten Maßstab in Quadratzentimeter umrechnen und anschließend mit der Rollenlänge in Zentimetern multiplizieren",
    schritte="5", zahlenraum="dezimal|negativ|Potenz", einheiten="FE|LE|cm^2|cm|cm^3",
    abhaengig_von="2021-A-2b",
    ergebnis="Querschnittsfläche rund 9,1 FE, das entspricht rund 2,28 cm^2|Luftvolumen 1824 cm^3, also rund 1,824 Liter (amtlich)",
    zwischenergebnis="f(x) − g(x) = 0,5x^4 − 3,5|Stammfunktion 0,1x^5 − 3,5x mit den Werten −4,55 und 4,55|eine Flächeneinheit entspricht 0,25 cm^2",
    niveau_geschaetzt="III",
    fehlerquelle="beim Umrechnen den Maßstab nicht quadrieren und die Fläche mit 0,5 statt mit 0,25 multiplizieren",
    bemerkung="Erwartungshorizont: Nachweis des Querschnittsflächeninhalts 5 BE, Angabe des Luftvolumens 1 BE. Der Typ Flächeninhalt im Koordinatensystem in Quadratmeter umrechnen trägt hier Quadratzentimeter; der Name ist enger als die Definition")

row(id="2021-A-3a", aufgabe="3", titel="Stochastik",
    teilaufgabe="a", seite="7", punkte="6",
    leitidee="Stochastik", thema="Statistische Kenngrößen",
    typ="Mittelwert aus Häufigkeitstabelle",
    typ_neben="Standardabweichung aus Häufigkeitstabelle|Häufigkeitsdiagramm zeichnen",
    stichwoerter="Rosenpreise|Verkaufszahlen|gewichtetes Mittel|Varianz|Säulendiagramm",
    voraussetzungen="Preise mit den Verkaufszahlen gewichten|Gesamtzahl 90 bilden",
    format="Rechnung|Zeichnen", operator="Berechnen Sie|Stellen Sie dar", antwort="Zahl|Grafik",
    material="Tabelle",
    skizze="vorgedruckte Tabelle mit drei Zeilen: Rosenfarbe rosa, rot, orange, violett und weiß; Preis pro Stück 1,20, 2,10, 1,50, 0,90 und 1,70 Euro; Anzahl verkauft 12, 33, 15, 10 und 20; das Diagramm zeichnet der Prüfling selbst",
    kontext="Einzelhandel/Blumengeschäft", textumfang="lang",
    gegeben="im Vorjahr wurden Rosen in fünf Farben verkauft: rosa zu 1,20 € (12 Stück), rot zu 2,10 € (33), orange zu 1,50 € (15), violett zu 0,90 € (10) und weiß zu 1,70 € (20)",
    gesucht="durchschnittliche Einnahmen pro verkaufter Rose|zugehörige Standardabweichung|Darstellung der Verkaufszahlen in einem geeigneten Diagramm",
    verfahren="jeden Preis mit seiner Verkaufszahl multiplizieren, die Produkte summieren und durch 90 teilen, dann die mit den Verkaufszahlen gewichteten quadratischen Abweichungen summieren, durch 90 teilen und die Wurzel ziehen; die fünf Verkaufszahlen als Säulendiagramm auftragen",
    schritte="5", zahlenraum="dezimal|Wurzel", einheiten="€", abhaengig_von="",
    ergebnis="durchschnittliche Einnahme rund 1,66 € je Rose|Standardabweichung rund 0,41 €|Säulendiagramm mit den Säulenhöhen 12, 33, 15, 10 und 20 (amtlich)",
    zwischenergebnis="Gesamtzahl 90 Rosen|Gesamteinnahme 149,20 €|Varianz rund 0,17",
    niveau_geschaetzt="II",
    fehlerquelle="die fünf Preise ungewichtet mitteln und 1,48 € statt 1,66 € erhalten",
    bemerkung="Erwartungshorizont: Berechnen von Mittelwert und Standardabweichung 4 BE, Diagramm 2 BE. Der Erwartungshorizont vermerkt, dass der Nenner n − 1 wegen der Rundung auf zwei Stellen dieselben Werte liefert. thema nach dem Punkt-Schwerpunkt 4 zu 2 gewählt")

row(id="2021-A-3b", aufgabe="3", titel="Stochastik",
    teilaufgabe="b", seite="7", punkte="2",
    leitidee="Stochastik", thema="Statistische Kenngrößen",
    typ="Fehlenden Wert aus vorgegebenem Mittelwert bestimmen", typ_neben="",
    stichwoerter="Zielmittelwert 1,70 €|Umkehrung des gewichteten Mittels|violette Rosen|Gleichung mit Unbekannter",
    voraussetzungen="die Mittelwertformel nach dem unbekannten Preis auflösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle",
    skizze="vorgedruckte Tabelle der Rosenfarben mit Preisen und Verkaufszahlen aus dem Aufgabenstamm",
    kontext="Einzelhandel/Blumengeschäft", textumfang="mittel",
    gegeben="die Verkaufszahlen 12, 33, 15, 10 und 20 und die Preise 1,20 €, 2,10 €, 1,50 € und 1,70 € bleiben unverändert; der Preis der violetten Rosen ist unbekannt; angestrebt wird eine durchschnittliche Einnahme von 1,70 € je Rose",
    gesucht="Betrag, auf den der Preis für die violetten Rosen hätte festgelegt werden müssen",
    verfahren="die Formel für das gewichtete Mittel mit dem unbekannten Preis aufstellen, gleich 1,70 setzen und nach der Unbekannten auflösen",
    schritte="2", zahlenraum="dezimal", einheiten="€", abhaengig_von="2021-A-3a",
    ergebnis="der Preis für die violetten Rosen hätte 1,28 € betragen müssen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="mit dem gerundeten Mittelwert 1,66 € aus Teilaufgabe a weiterrechnen statt die Gleichung neu aufzustellen",
    bemerkung="Erwartungshorizont: Ermitteln des Preises 2 BE. Der Erwartungshorizont vermerkt selbst, dass Wege über den gerundeten Mittelwert aus a zu Abweichungen in der zweiten Dezimalstelle führen können")

row(id="2021-A-3c", aufgabe="3", titel="Stochastik",
    teilaufgabe="c", seite="7", punkte="2",
    leitidee="Stochastik", thema="Kombinatorische Abzählverfahren",
    typ="Kombination ohne Wiederholung berechnen", typ_neben="",
    stichwoerter="drei aus fünf Farben|Binomialkoeffizient|Auswahl ohne Reihenfolge|Strauß",
    voraussetzungen="erkennen, dass die Reihenfolge der Farben keine Rolle spielt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle",
    skizze="vorgedruckte Tabelle der fünf Rosenfarben aus dem Aufgabenstamm",
    kontext="Einzelhandel/Blumengeschäft", textumfang="kurz",
    gegeben="es sind fünf Rosenfarben erhältlich; für einen Strauß werden drei davon ausgewählt",
    gesucht="Anzahl der Möglichkeiten, drei der erhältlichen Farben auszuwählen",
    verfahren="den Binomialkoeffizienten 5 über 3 berechnen, weil die Reihenfolge der ausgewählten Farben keine Rolle spielt",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="10 Möglichkeiten der Auswahl (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Reihenfolge mitzählen und 60 statt 10 Möglichkeiten angeben",
    bemerkung="Erwartungshorizont: Bestimmen der Auswahlmöglichkeiten 2 BE")

row(id="2021-A-3d", aufgabe="3", titel="Stochastik",
    teilaufgabe="d", seite="7", punkte="8",
    leitidee="Stochastik", thema="Mehrstufige Zufallsexperimente",
    typ="Baumdiagramm zweistufig ohne Zurücklegen darstellen",
    typ_neben="Pfadregel zweistufig ohne Zurücklegen anwenden|Wahrscheinlichkeit über mehrere Pfade summieren|Gegenereignis nutzen",
    stichwoerter="70 Tulpen|drei Farben|ohne Zurücklegen|mindestens eine gelbe|Gegenereignis",
    voraussetzungen="die Zahl der weißen Tulpen aus dem Rest bestimmen|Nenner in der zweiten Stufe auf 69 verkleinern",
    format="Zeichnen|Rechnung", operator="Stellen Sie dar|Berechnen Sie", antwort="Grafik|Zahl",
    material="keins",
    skizze="der Prüfling zeichnet das Baumdiagramm selbst; entstehen soll ein zweistufiger Baum mit den Ästen gelb, rot und weiß, den Startwahrscheinlichkeiten 30/70, 25/70 und 15/70 und in der zweiten Stufe den jeweils um eins verringerten Zählern über dem Nenner 69",
    kontext="Einzelhandel/Tulpen", textumfang="lang",
    gegeben="ein Korb enthält 70 Tulpen, davon 30 gelbe, 25 rote und der Rest weiße; jede Kundin darf zwei Tulpen mitnehmen, die Farbe ist beim Ziehen nicht erkennbar; Ereignis A die erste Kundin erhält zwei weiße Tulpen; Ereignis B sie erhält mindestens eine gelbe Tulpe; Ereignis C sie erhält keine gelbe Tulpe",
    gesucht="vollständiges Baumdiagramm der zufälligen Auswahl der ersten zwei Tulpen|Wahrscheinlichkeit von A|Wahrscheinlichkeit von B|Wahrscheinlichkeit von C",
    verfahren="die 15 weißen Tulpen aus dem Rest bestimmen, den zweistufigen Baum ohne Zurücklegen zeichnen, für A den einen Pfad multiplizieren, für B die drei Pfade mit mindestens einer gelben Tulpe addieren und für C das Gegenereignis zu B nutzen",
    schritte="5", zahlenraum="Bruch|dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(A) = 1/23, rund 4,35 %|P(B) = 109/161, rund 67,70 %|P(C) = 52/161, rund 32,30 % (amtlich)",
    zwischenergebnis="15 weiße Tulpen|P(B) als Summe von 30/70 sowie 25/70 mal 30/69 und 15/70 mal 30/69",
    niveau_geschaetzt="III",
    fehlerquelle="bei der zweiten Tulpe den Nenner 70 beibehalten und mit Zurücklegen rechnen",
    bemerkung="Erwartungshorizont: Zeichnen des Baumdiagramms 3 BE, P(A) 1 BE, P(B) 2 BE, P(C) 2 BE")

row(id="2021-A-3e", aufgabe="3", titel="Stochastik",
    teilaufgabe="e", seite="7", punkte="2",
    leitidee="Stochastik", thema="Mehrstufige Zufallsexperimente",
    typ="Pfadregel dreistufig ohne Zurücklegen anwenden", typ_neben="",
    stichwoerter="zwei Kundinnen|vier Tulpen|alle gelb|Nenner von 70 bis 67|ein Pfad",
    voraussetzungen="zwei Kundinnen mit je zwei Tulpen als vier Ziehungen deuten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Einzelhandel/Tulpen", textumfang="kurz",
    gegeben="der Korb enthält 70 Tulpen, davon 30 gelbe; jede Kundin nimmt zwei Tulpen ohne Zurücklegen mit",
    gesucht="Wahrscheinlichkeit dafür, dass die ersten beiden Kundinnen nur gelbe Tulpen bekommen",
    verfahren="erkennen, dass zwei Kundinnen zusammen vier Tulpen ziehen, und die vier Wahrscheinlichkeiten mit den von 70 auf 67 fallenden Nennern und den von 30 auf 27 fallenden Zählern multiplizieren",
    schritte="2", zahlenraum="Bruch|dezimal|Prozent", einheiten="", abhaengig_von="2021-A-3d",
    ergebnis="Wahrscheinlichkeit rund 2,99 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur zwei statt vier Ziehungen ansetzen, weil von zwei Kundinnen die Rede ist",
    bemerkung="Erwartungshorizont: Ermitteln der Wahrscheinlichkeit 2 BE. Vier Stufen ohne Zurücklegen; wie in 2022-B-3f kein eigener Typ nur wegen der Stufenzahl, die Definition des Typs ist entsprechend erweitert")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Wendepunkt aus vorgegebenen Punkten auswählen", "Differentialrechnung", "Wendepunkte",
     "Aus einer Liste vorgegebener Punkte denjenigen als Wendepunkt bestimmen, der die Bedingungen der zweiten und dritten Ableitung erfüllt, und die Auswahl mathematisch begründen.",
     "2021-A-1d"),
    ("Fehlenden Wert aus vorgegebenem Mittelwert bestimmen", "Stochastik", "Statistische Kenngrößen",
     "Bei bekannten Häufigkeiten und bekanntem Zielmittelwert den einen unbekannten Einzelwert über eine Gleichung bestimmen; Umkehrung der Mittelwertberechnung.",
     "2021-A-3b"),
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
