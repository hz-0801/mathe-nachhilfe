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
    "papier": "C",
    "datei": "22_FOS_Ma_C_LH.pdf",
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
# Ein Eintrag je Teilaufgabe der Punktetabelle. Nicht genannte Felder bleiben
# leer; jahr, papier, hilfsmittel und die leeren Festwerte setzt row() selbst.

row(id="2022-C-1a", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="a", seite="2", punkte="4",
    leitidee="Differentialrechnung", thema="Symmetrie nachweisen",
    typ="Symmetrie am Funktionsterm beurteilen",
    typ_neben="Verhalten im Unendlichen bestimmen",
    stichwoerter="Achsensymmetrie|Punktsymmetrie|gerade Exponenten|Grenzwert|negativer Leitkoeffizient",
    voraussetzungen="Exponenten eines Terms als gerade oder ungerade erkennen",
    format="Begründung|Kurzantwort", operator="Treffen Sie eine begründete Aussage|Geben Sie an",
    antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −0,25x^4 + 1,75x^2 + 2,5; x aus IR",
    gesucht="begründete Aussage zur Symmetrie von Gf bezüglich y-Achse und Koordinatenursprung|Verhalten der Funktionswerte im Unendlichen",
    verfahren="am Term prüfen, ob nur gerade Exponenten auftreten, und das über f(−x) = f(x) begründen; dann den Summanden höchsten Grades betrachten und für beide Richtungen den Grenzwert angeben",
    schritte="2", zahlenraum="dezimal|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Gf ist achsensymmetrisch zur y-Achse, weil nur gerade Exponenten auftreten beziehungsweise f(x) = f(−x) gilt|für x gegen −unendlich und für x gegen +unendlich streben die Funktionswerte gegen −unendlich (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="das Absolutglied als ungeraden Exponenten deuten oder wegen des geraden Grades +unendlich angeben und den negativen Leitkoeffizienten übersehen",
    bemerkung="Gutachten: Symmetrieangabe mit Begründung 2 BE, Angabe der Grenzwerte 2 BE. thema bei Punktgleichstand 2 zu 2 nach der ersten verlangten Leistung gewählt")

row(id="2022-C-1b", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="b", seite="2", punkte="5",
    leitidee="Differentialrechnung", thema="Nullstellen ganzrationaler Funktionen",
    typ="Nullstellen über Substitution biquadratisch",
    typ_neben="Schnittpunkt mit der y-Achse berechnen",
    stichwoerter="biquadratische Gleichung|Substitution|Lösungsformel|Rücksubstitution|Achsenschnittpunkte",
    voraussetzungen="Gleichung durch den Leitkoeffizienten teilen|negative Lösung der Hilfsvariablen verwerfen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −0,25x^4 + 1,75x^2 + 2,5; x aus IR",
    gesucht="alle Schnittpunkte des Graphen mit den Koordinatenachsen",
    verfahren="für den y-Achsenschnitt x = 0 einsetzen; für die Nullstellen die Gleichung durch −0,25 teilen, x^2 = z substituieren, die quadratische Gleichung lösen, die negative Lösung verwerfen und zurücksubstituieren",
    schritte="4", zahlenraum="dezimal|negativ|Potenz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="Sy(0; 2,5)|Sx1(−2,87; 0) und Sx2(2,87; 0) (amtlich)",
    zwischenergebnis="0 = z^2 − 7z − 10 mit z1 ungefähr −1,22 und z2 ungefähr 8,22|x1/2 ungefähr ±2,87",
    niveau_geschaetzt="II",
    fehlerquelle="auch die negative Lösung z1 zurücksubstituieren und die Wurzel aus einer negativen Zahl ziehen",
    bemerkung="Gutachten: Angabe des Schnittpunktes mit der y-Achse 1 BE, Berechnen der Nullstellen von f 3 BE, Angabe der Schnittpunkte mit der x-Achse 1 BE")

row(id="2022-C-1c", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="c", seite="2", punkte="8",
    leitidee="Differentialrechnung", thema="Extrem- und Sattelpunkte",
    typ="Extrem- und Sattelpunkte über zweite Ableitung", typ_neben="",
    stichwoerter="notwendige Bedingung|hinreichende Bedingung|Ausklammern|Hochpunkt|Tiefpunkt",
    voraussetzungen="erste und zweite Ableitung bilden|Produkt gleich null setzen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −0,25x^4 + 1,75x^2 + 2,5; x aus IR",
    gesucht="Koordinaten und Art aller Extrempunkte von Gf",
    verfahren="erste und zweite Ableitung bilden, die erste Ableitung durch Ausklammern von x null setzen, die drei Stellen in die zweite Ableitung einsetzen und über das Vorzeichen die Art bestimmen, dann die Funktionswerte berechnen",
    schritte="5", zahlenraum="dezimal|negativ|Potenz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="H1(−1,87; 5,56)|T(0; 2,5)|H2(1,87; 5,56) (amtlich)",
    zwischenergebnis="f'(x) = −x^3 + 3,5x|f''(x) = −3x^2 + 3,5|Extremstellen x1 = 0 und x2/3 ungefähr ±1,87|f''(±1,87) ungefähr −6,99 und f''(0) = 3,5",
    niveau_geschaetzt="II",
    fehlerquelle="beim Ausklammern die Lösung x = 0 verlieren und nur die beiden Hochpunkte angeben",
    bemerkung="Gutachten: Notieren der ersten und zweiten Ableitung 2 BE, Berechnen der Nullstellen der ersten Ableitung 3 BE, Nachweis der Art der Extrempunkte samt Koordinatenangabe 3 BE. Die Ableitungen sind Vorstufe und stehen deshalb nicht als typ_neben")

row(id="2022-C-1d", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="d", seite="2", punkte="7",
    leitidee="Differentialrechnung", thema="Wendepunkte",
    typ="Wendepunkte über zweite Ableitung",
    typ_neben="Krümmungsverhalten angeben",
    stichwoerter="zweite Ableitung null setzen|dritte Ableitung|Kontrollergebnis|konvex|Linkskrümmung",
    voraussetzungen="dritte Ableitung bilden|Intervallschreibweise verwenden",
    format="Rechnung|Kurzantwort", operator="Ermitteln Sie|Notieren Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −0,25x^4 + 1,75x^2 + 2,5; x aus IR; als Kontrolle sind die Wendepunkte W1/2(±1,08; 4,20) genannt",
    gesucht="Koordinaten der beiden Wendepunkte|Intervall für x mit linksgekrümmtem Verlauf von Gf",
    verfahren="die zweite Ableitung null setzen und die beiden Stellen berechnen, über die dritte Ableitung ungleich null den Wendepunkt nachweisen, die Funktionswerte berechnen und anschließend das Intervall angeben, in dem die zweite Ableitung positiv ist",
    schritte="5", zahlenraum="dezimal|negativ|Potenz|Wurzel", einheiten="", abhaengig_von="2022-C-1c",
    ergebnis="W1(−1,08; 4,20) und W2(1,08; 4,20)|Linkskrümmung für −1,08 < x < 1,08 (amtlich)",
    zwischenergebnis="f'''(x) = −6x|Wendestellen x1/2 = ±Wurzel aus 7/6 ungefähr ±1,08|f'''(−1,08) = 6,48 und f'''(1,08) = −6,48",
    niveau_geschaetzt="II",
    fehlerquelle="Links- und Rechtskrümmung vertauschen und das Intervall außerhalb der Wendestellen angeben",
    bemerkung="Gutachten: Notieren der dritten Ableitung 1 BE, Bestimmen der Nullstellen der zweiten Ableitung 2 BE, Nachweis der Wendepunkte samt Koordinatenangabe 3 BE, Angabe des Intervalls mit Linkskrümmung 1 BE")

row(id="2022-C-1e", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="e", seite="2", punkte="3",
    leitidee="Differentialrechnung", thema="Anstieg und Tangente",
    typ="Tangenteneigenschaft einer Geraden nachweisen",
    typ_neben="Tangentengleichung im Punkt",
    stichwoerter="Wendetangente|Punktprobe|Anstieg vergleichen|zweite Tangente|Achsensymmetrie",
    voraussetzungen="Wendepunkte aus Teilaufgabe d verwenden|Ableitungswert an der Wendestelle berechnen",
    format="Rechnung|Begründung", operator="Weisen Sie nach|Geben Sie an", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −0,25x^4 + 1,75x^2 + 2,5; x aus IR; die Wendepunkte W1/2(±1,08; 4,20); die Gerade t mit t(x) = 2,52x + 1,48; die Genauigkeit beträgt zwei Nachkommastellen",
    gesucht="Nachweis, dass t eine Wendetangente an Gf ist|Gleichung der zweiten Wendetangente",
    verfahren="den Wendepunkt in t einsetzen und die Übereinstimmung des Funktionswerts zeigen, dann den Anstieg von Gf an der Wendestelle berechnen und mit dem Anstieg von t vergleichen; die zweite Tangente über die Achsensymmetrie spiegeln oder als Tangentengleichung im zweiten Wendepunkt aufstellen",
    schritte="3", zahlenraum="dezimal|negativ|Potenz", einheiten="", abhaengig_von="2022-C-1d",
    ergebnis="t(1,08) ungefähr 4,20 und f'(1,08) ungefähr 2,52, also verläuft t durch W2 und hat dort denselben Anstieg wie Gf, damit ist t eine Wendetangente|t2: y = −2,52x + 1,48 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Punktprobe führen und den Vergleich der Anstiege weglassen",
    bemerkung="Gutachten: Nachweis der gegebenen Wendetangente 2 BE, Angeben der zweiten Wendetangente 1 BE. Der Weg über die Symmetrie ist eine Abkürzung des Aufstellens im Punkt W1 und bekommt keinen eigenen Typ")

row(id="2022-C-1f", aufgabe="1", titel="Differentialrechnung",
    teilaufgabe="f", seite="2", punkte="3",
    leitidee="Differentialrechnung", thema="Graph zeichnen und zuordnen",
    typ="Graph ganzrationaler Funktion im Intervall zeichnen", typ_neben="",
    stichwoerter="Intervall|kartesisches Koordinatensystem|markante Punkte|Achseneinteilung",
    voraussetzungen="Ergebnisse der Teilaufgaben b bis d eintragen|Randwerte f(±3) berechnen",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="keins",
    skizze="der Prüfling legt das Koordinatensystem selbst an; entstehen soll der nach unten geöffnete doppelhügelige Verlauf mit den Hochpunkten (−1,87; 5,56) und (1,87; 5,56), dem Tiefpunkt (0; 2,5), den Wendepunkten (±1,08; 4,20), den Nullstellen bei ±2,87 und den Randpunkten (−3; −2) und (3; −2)",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −0,25x^4 + 1,75x^2 + 2,5; x aus IR; zu zeichnen im Intervall −3 <= x <= 3",
    gesucht="Graph von f im angegebenen Intervall",
    verfahren="die berechneten Achsenschnittpunkte, Extrem- und Wendepunkte eintragen, die Randwerte ergänzen und den Verlauf durchzeichnen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="",
    abhaengig_von="2022-C-1b|2022-C-1c|2022-C-1d",
    ergebnis="Graph durch (−3; −2), Sx1(−2,87; 0), H1(−1,87; 5,56), W1(−1,08; 4,20), T(0; 2,5), W2(1,08; 4,20), H2(1,87; 5,56), Sx2(2,87; 0) und (3; −2) (amtlich)",
    zwischenergebnis="f(−3) = f(3) = −2",
    niveau_geschaetzt="II",
    fehlerquelle="die Achseneinteilung so wählen, dass der Bereich bis y = 5,56 nicht auf das Blatt passt",
    bemerkung="Gutachten: Zeichnen des Graphen 3 BE")

row(id="2022-C-2a", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="a", seite="5", punkte="2",
    leitidee="Differentialrechnung", thema="Graph zeichnen und zuordnen",
    typ="Graph einer ganzrationalen Funktion zuordnen",
    typ_neben="Verhalten im Unendlichen bestimmen",
    stichwoerter="vier Abbildungen|Verhalten im Unendlichen|Anstieg einer Geraden|begründete Entscheidung",
    voraussetzungen="aus zwei Punkten auf ein Vorzeichen des Anstiegs schließen",
    format="Begründung", operator="Treffen Sie eine begründete Entscheidung", antwort="Text",
    material="Diagramm",
    skizze="vier nebeneinanderliegende, mit A bis D beschriftete Kästen ohne Achsen und ohne Skalierung, in jedem der Verlauf einer Funktion dritten Grades und eine Gerade; A steigende Gerade mit einer Kurve, die nach einem Hochpunkt wieder fällt; B fallende Gerade mit einer nach dem Hochpunkt steil fallenden Kurve; C fallende Gerade mit einer Kurve, die nach Hoch- und Tiefpunkt nach rechts oben steigt; D steigende Gerade mit einer Kurve, die nach dem Hochpunkt fällt",
    kontext="ohne", textumfang="mittel",
    gegeben="f(x) = x^3 − 12x^2 + 39x − 28; x aus IR; von der linearen Funktion g ist bekannt, dass ihr Graph durch P(0; 20) und Q(4; 0) verläuft; vier Abbildungen A bis D, von denen nur eine beide Graphen richtig zeigt",
    gesucht="begründete Entscheidung, welche der vier Abbildungen zutrifft",
    verfahren="am Summanden höchsten Grades das Verhalten im Unendlichen ablesen und aus den beiden Punkten von g das Vorzeichen des Anstiegs bestimmen, dann die Abbildungen daran ausschließen",
    schritte="2", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Abbildung C, weil f für x gegen +unendlich gegen +unendlich strebt und Gg wegen P und Q einen negativen Anstieg hat (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur ein Merkmal prüfen und eine Abbildung wählen, die zwar den Kurvenverlauf, aber nicht die Richtung der Geraden trifft",
    bemerkung="Gutachten: Angeben der Abbildung mit Begründung 2 BE")

row(id="2022-C-2b", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="b", seite="5", punkte="4",
    leitidee="Differentialrechnung", thema="Funktionsgleichung bestimmen",
    typ="Geradengleichung aus zwei Punkten bestimmen",
    typ_neben="Anstieg einer senkrechten Geraden angeben",
    stichwoerter="Zweipunkteform|Anstieg|y-Achsenabschnitt|senkrechte Geraden|Kontrollergebnis",
    voraussetzungen="Differenzenquotient aufstellen|negativen Kehrwert bilden",
    format="Rechnung|Kurzantwort", operator="Ermitteln Sie|Geben Sie an", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="von der linearen Funktion g ist bekannt, dass ihr Graph durch P(0; 20) und Q(4; 0) verläuft; als Kontrolle ist g(x) = −5x + 20 genannt",
    gesucht="Funktionsgleichung von g|Anstieg einer beliebigen Funktion h, deren Graph senkrecht zum Graphen von g verläuft",
    verfahren="den Anstieg als Quotient der Koordinatendifferenzen berechnen, den y-Achsenabschnitt aus P ablesen und die Gleichung notieren; dann den negativen Kehrwert des Anstiegs bilden",
    schritte="3", zahlenraum="ganz|dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="g(x) = −5x + 20|Anstieg von h ist 0,2 (amtlich)",
    zwischenergebnis="m = (0 − 20) : (4 − 0) = −5|n = 20 wegen P",
    niveau_geschaetzt="II",
    fehlerquelle="beim senkrechten Anstieg nur den Kehrwert ohne Vorzeichenwechsel bilden und −0,2 angeben",
    bemerkung="Gutachten: Ermitteln der Geradenfunktionsgleichung 3 BE, Angabe des Normalenanstiegs 1 BE")

row(id="2022-C-2c", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="c", seite="5", punkte="5",
    leitidee="Integralrechnung", thema="Fläche zwischen Graph und x-Achse",
    typ="Ganzzahlige Nullstellen durch Probieren finden",
    typ_neben="Fläche zwischen Graph und x-Achse berechnen",
    stichwoerter="ganzzahlige Nullstellen|Wertetabelle|bestimmtes Integral|Betrag|Flächeneinheiten",
    voraussetzungen="Stammfunktion bilden|negativen Integralwert als Betrag deuten",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = x^3 − 12x^2 + 39x − 28; x aus IR; die Funktion f hat drei ganzzahlige Nullstellen; betrachtet wird das Intervall von 4 bis 7",
    gesucht="die drei ganzzahligen Nullstellen|Maßzahl des Inhalts der Fläche zwischen Gf und der x-Achse im Intervall von 4 bis 7",
    verfahren="die Nullstellen über eine Wertetabelle oder durch Probieren ganzer Zahlen finden, dann die Stammfunktion bilden, an den Grenzen 7 und 4 auswerten und vom Ergebnis den Betrag nehmen",
    schritte="4", zahlenraum="ganz|dezimal|negativ|Potenz", einheiten="FE", abhaengig_von="",
    ergebnis="Nullstellen x1 = 1, x2 = 4 und x3 = 7|Flächeninhalt 20,25 FE (amtlich)",
    zwischenergebnis="Stammfunktion F(x) = 0,25x^4 − 4x^3 + 19,5x^2 − 28x|F(7) = −12,25 und F(4) = 8",
    niveau_geschaetzt="II",
    fehlerquelle="den negativen Integralwert ohne Betrag als Flächeninhalt angeben",
    bemerkung="Gutachten: Nullstellen zum Beispiel mit Wertetabelle 2 BE, Berechnung des Flächeninhalts 3 BE. thema nach dem Punkt-Schwerpunkt gewählt, der typ steht unter Nullstellen ganzrationaler Funktionen")

row(id="2022-C-2d", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="d", seite="5", punkte="6",
    leitidee="Differentialrechnung", thema="Schnittpunkte von Funktionsgraphen",
    typ="Schnittpunkte zweier Funktionsgraphen berechnen",
    typ_neben="Nullstellen mit Polynomdivision",
    stichwoerter="gleichsetzen|Polynomdivision|Lösungsformel|bekannte Lösung|Kontrollergebnis",
    voraussetzungen="den gemeinsamen Punkt Q als bekannte Lösung nutzen|Gleichung dritten Grades ordnen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = x^3 − 12x^2 + 39x − 28 und g(x) = −5x + 20; Q(4; 0) ist ein gemeinsamer Punkt beider Graphen; als Kontrolle sind S1(2; 10) und S2(6; −10) genannt",
    gesucht="Koordinaten der beiden weiteren Schnittpunkte von Gf und Gg",
    verfahren="beide Terme gleichsetzen und auf null bringen, durch den bekannten Linearfaktor x − 4 dividieren, die entstehende quadratische Gleichung lösen und die Funktionswerte berechnen",
    schritte="5", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="2022-C-2b",
    ergebnis="S1(2; 10) und S2(6; −10) (amtlich)",
    zwischenergebnis="x^3 − 12x^2 + 44x − 48 = 0|Polynomdivision durch x − 4 ergibt x^2 − 8x + 12|x1 = 2 und x2 = 6",
    niveau_geschaetzt="II",
    fehlerquelle="beim Gleichsetzen das Vorzeichen von −5x falsch übernehmen und 34x statt 44x erhalten",
    bemerkung="Gutachten: Ermitteln der Differenzfunktion 1 BE, Berechnen ihrer Nullstellen 4 BE, Angabe der vollständigen Koordinaten der Schnittpunkte 1 BE")

row(id="2022-C-2e", aufgabe="2", titel="Differential- und Integralrechnung",
    teilaufgabe="e", seite="5", punkte="3",
    leitidee="Integralrechnung", thema="Fläche zwischen zwei Graphen",
    typ="Fläche zwischen zwei Graphen berechnen", typ_neben="",
    stichwoerter="Differenzfunktion|bestimmtes Integral|Integrationsgrenzen|Flächeneinheiten",
    voraussetzungen="Differenzfunktion aufstellen|Stammfunktion bilden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x^3 − 12x^2 + 39x − 28 und g(x) = −5x + 20; betrachtet wird das Intervall von 2 bis 4",
    gesucht="Maßzahl des Inhalts der zwischen Gf und Gg eingeschlossenen Fläche im Intervall von 2 bis 4",
    verfahren="die Differenz der beiden Terme bilden, davon die Stammfunktion aufstellen und an den Grenzen 4 und 2 auswerten",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="FE", abhaengig_von="2022-C-2d",
    ergebnis="Flächeninhalt 4 FE (amtlich)",
    zwischenergebnis="f(x) − g(x) = x^3 − 12x^2 + 44x − 48|Stammfunktion 0,25x^4 − 4x^3 + 22x^2 − 48x|Werte −32 und −36",
    niveau_geschaetzt="II",
    fehlerquelle="die Differenz in der falschen Reihenfolge bilden und ein negatives Ergebnis stehen lassen",
    bemerkung="Gutachten: Berechnen des eingeschlossenen Flächeninhalts 3 BE. Die Differenzfunktion verlangt der Aufgabentext nicht ausdrücklich und steht deshalb nicht als typ_neben")

row(id="2022-C-3a", aufgabe="3", titel="Stochastik",
    teilaufgabe="a", seite="7", punkte="4",
    leitidee="Stochastik", thema="Kombinatorische Abzählverfahren",
    typ="Kombination ohne Wiederholung berechnen",
    typ_neben="Permutation ohne Wiederholung berechnen",
    stichwoerter="Binomialkoeffizient|Auswahl ohne Reihenfolge|Fakultät|Anordnung|Geschenke verteilen",
    voraussetzungen="Auswahl und Anordnung unterscheiden",
    format="Rechnung", operator="Bestimmen Sie|Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Marktforschung/Supermarkt", textumfang="mittel",
    gegeben="vor einem Supermarkt wurden 60 Personen befragt; fünf von ihnen erhalten als Dank ein Geschenk; die fünf Geschenke sind verschieden",
    gesucht="Anzahl der Möglichkeiten, fünf Personen aus allen Befragten auszuwählen|Anzahl der Möglichkeiten, die fünf verschiedenen Geschenke an die fünf Ausgewählten zu vergeben",
    verfahren="für die Auswahl den Binomialkoeffizienten 60 über 5 berechnen, weil die Reihenfolge keine Rolle spielt; für die Verteilung die Fakultät von 5 bilden, weil die Reihenfolge zählt",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="5 461 512 Möglichkeiten für die Auswahl|120 Möglichkeiten für die Verteilung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="für die Auswahl die Reihenfolge mitzählen und statt des Binomialkoeffizienten eine Variation berechnen",
    bemerkung="Gutachten: Bestimmung der Auswahlmöglichkeiten 2 BE, Bestimmung der Anordnungsmöglichkeiten 2 BE")

row(id="2022-C-3b", aufgabe="3", titel="Stochastik",
    teilaufgabe="b", seite="7", punkte="3",
    leitidee="Stochastik", thema="Statistische Kenngrößen",
    typ="Mittelwert aus Werteliste",
    typ_neben="Standardabweichung aus Werteliste",
    stichwoerter="arithmetisches Mittel|Varianz|Standardabweichung|fünf Rechnungsbeträge",
    voraussetzungen="Summe durch Anzahl teilen|Wurzel aus der Varianz ziehen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Marktforschung/Einkaufsbeträge", textumfang="kurz",
    gegeben="die fünf zu beschenkenden Personen haben die Rechnungsbeträge 23,75 €, 10,50 €, 107,28 €, 2,05 € und 46,42 € angegeben",
    gesucht="arithmetischer Mittelwert dieser Angaben|Standardabweichung dieser Angaben",
    verfahren="die fünf Beträge summieren und durch fünf teilen, dann die quadratischen Abweichungen vom Mittelwert summieren, durch fünf beziehungsweise durch vier teilen und die Wurzel ziehen",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="€", abhaengig_von="",
    ergebnis="Mittelwert 38 €|Standardabweichung ungefähr 37,74 € mit dem Nenner 5 beziehungsweise ungefähr 42,20 € mit dem Nenner 4 (amtlich)",
    zwischenergebnis="Summe 190 €|Summe der quadratischen Abweichungen ungefähr 7122,33",
    niveau_geschaetzt="II",
    fehlerquelle="die Wurzel vergessen und die Varianz als Standardabweichung angeben",
    bemerkung="Gutachten: Berechnen des arithmetischen Mittelwerts 1 BE, Berechnen der Standardabweichung 2 BE. Der Erwartungshorizont lässt wie 2026-B-3a beide Nenner gelten und nennt beide Werte")

row(id="2022-C-3c", aufgabe="3", titel="Stochastik",
    teilaufgabe="c", seite="7", punkte="5",
    leitidee="Stochastik", thema="Mehrstufige Zufallsexperimente",
    typ="Baumdiagramm dreistufig ohne Zurücklegen darstellen",
    typ_neben="Wahrscheinlichkeit über mehrere Pfade summieren",
    stichwoerter="Ziehen ohne Zurücklegen|drei Stufen|Pfadregeln|günstige Pfade|Adresszettel",
    voraussetzungen="Nenner von Stufe zu Stufe verkleinern|alle günstigen Pfade finden",
    format="Zeichnen|Rechnung", operator="Stellen Sie dar|Ermitteln Sie", antwort="Grafik|Zahl",
    material="keins",
    skizze="der Prüfling zeichnet das Baumdiagramm selbst; entstehen soll ein dreistufiger Baum mit den Ästen Frau und Mann, den Startwahrscheinlichkeiten 3/5 und 2/5 und den in jeder Stufe kleiner werdenden Nennern 4 und 3, alle Äste beschriftet",
    kontext="Marktforschung/Verlosung", textumfang="lang",
    gegeben="unter den fünf zu beschenkenden Personen sind drei Frauen und zwei Männer; die Adresse jeder Person steht auf je einem von fünf Zetteln; für jedes Geschenk wird nacheinander ein Zettel gezogen und nicht zurückgelegt; betrachtet werden die ersten drei Geschenke",
    gesucht="vollständig beschriftetes Baumdiagramm für die ersten drei Ziehungen|Wahrscheinlichkeit dafür, dass die beiden Männer schon unter den ersten drei Gewinnern sind",
    verfahren="das dreistufige Baumdiagramm ohne Zurücklegen mit den passenden Nennern anlegen, die drei Pfade mit zwei Männern und einer Frau bestimmen, ihre Wahrscheinlichkeiten über die Pfadmultiplikation berechnen und addieren",
    schritte="4", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Wahrscheinlichkeit 3/10, also 30 % (amtlich)",
    zwischenergebnis="die drei günstigen Pfade Mann-Mann-Frau, Mann-Frau-Mann und Frau-Mann-Mann haben je die Wahrscheinlichkeit 1/10",
    niveau_geschaetzt="II",
    fehlerquelle="nur einen der drei Pfade berücksichtigen und 1/10 angeben",
    bemerkung="Gutachten: Zeichnen und Beschriften des Baumdiagramms 3 BE, Berechnen einer Wahrscheinlichkeit 2 BE. Drei Stufen ohne Zurücklegen, thema nach der Arbeitsregel in fhr.md Abschnitt 6")

row(id="2022-C-3d", aufgabe="3", titel="Stochastik",
    teilaufgabe="d", seite="7", punkte="8",
    leitidee="Stochastik", thema="Daten darstellen und aufbereiten",
    typ="Mittelwert aus Häufigkeitstabelle",
    typ_neben="Relative Häufigkeit berechnen|Häufigkeitsdiagramm zeichnen|Änderung der Häufigkeiten bei größerer Stichprobe begründen",
    stichwoerter="Klasseneinteilung|Klassenmitte|relative Häufigkeit|Säulendiagramm|Vervielfachung der Stichprobe",
    voraussetzungen="Klassenmitten bilden|Anteile in Prozent umrechnen",
    format="Rechnung|Zeichnen|Begründung",
    operator="Bestimmen Sie|Geben Sie an|Stellen Sie auf", antwort="Zahl|Grafik|Text",
    material="Tabelle",
    skizze="vorgedruckte Tabelle mit drei Zeilen: Klasse 1 bis 4, Rechnungsbetrag in € mit den Grenzen 0 bis 25, 25 bis 50, 50 bis 100 und 100 bis 200 sowie Anzahl unter den Befragten 22, 12, 18 und 8; das Diagramm zeichnet der Prüfling selbst",
    kontext="Marktforschung/Rechnungsbeträge", textumfang="lang",
    gegeben="die Angaben aller 60 Befragten sind in vier Klassen zusammengefasst: 0 < x <= 25 mit 22 Personen, 25 < x <= 50 mit 12 Personen, 50 < x <= 100 mit 18 Personen und 100 < x <= 200 mit 8 Personen",
    gesucht="arithmetischer Mittelwert der Rechnungsbeträge bezüglich dieser Klasseneinteilung|relative Häufigkeit je Klasse|Darstellung dieser Anteile in einem geeigneten Diagramm|begründete Vermutung über die Änderung der absoluten und relativen Häufigkeiten bei 180 Befragten und gleichem Einkaufsverhalten",
    verfahren="je Klasse die Klassenmitte mit der Anzahl multiplizieren, die Produkte summieren und durch 60 teilen; dann jede Anzahl durch 60 teilen, die Anteile in einem Säulendiagramm auftragen und begründen, dass sich bei verdreifachter Stichprobe nur die absoluten Häufigkeiten verdreifachen",
    schritte="6", zahlenraum="ganz|dezimal|Prozent", einheiten="€", abhaengig_von="",
    ergebnis="Mittelwert ungefähr 54,58 €|relative Häufigkeiten ungefähr 36,67 %, 20 %, 30 % und ungefähr 13,33 %|Säulendiagramm mit diesen vier Anteilen|bei gleichem Einkaufsverhalten verdreifachen sich die absoluten Häufigkeiten, die relativen bleiben unverändert, weil Zähler und Nenner mit demselben Faktor wachsen (amtlich)",
    zwischenergebnis="Klassenmitten 12,5, 37,5, 75 und 150|Summe der Produkte 3275",
    niveau_geschaetzt="II",
    fehlerquelle="statt der Klassenmitten die oberen Klassengrenzen verwenden und einen zu hohen Mittelwert erhalten",
    bemerkung="Gutachten: Berechnen des Mittelwerts der Klasseneinteilung 2 BE, Angabe der relativen Häufigkeiten 2 BE, Darstellung der relativen Häufigkeiten im Diagramm 2 BE, begründete Vermutung 2 BE. thema nach dem Punkt-Schwerpunkt 6 zu 2 gewählt, der typ steht unter Statistische Kenngrößen")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Geradengleichung aus zwei Punkten bestimmen", "Differentialrechnung", "Funktionsgleichung bestimmen",
     "Aus zwei gegebenen Punkten den Anstieg als Quotient der Koordinatendifferenzen und den y-Achsenabschnitt bestimmen und die Gleichung der linearen Funktion notieren.",
     "2022-C-2b"),
    ("Anstieg einer senkrechten Geraden angeben", "Differentialrechnung", "Normale",
     "Zu einer Geraden mit bekanntem Anstieg den Anstieg einer dazu senkrechten Geraden als negativen Kehrwert angeben, ohne eine vollständige Geradengleichung aufzustellen.",
     "2022-C-2b"),
    ("Ganzzahlige Nullstellen durch Probieren finden", "Differentialrechnung", "Nullstellen ganzrationaler Funktionen",
     "Bei gegebener Anzahl ganzzahliger Nullstellen diese über eine Wertetabelle oder durch systematisches Einsetzen ganzer Zahlen auffinden, ohne Polynomdivision oder Lösungsformel.",
     "2022-C-2c"),
    ("Änderung der Häufigkeiten bei größerer Stichprobe begründen", "Stochastik", "Daten darstellen und aufbereiten",
     "Begründen, wie sich absolute und relative Häufigkeiten verhalten, wenn der Stichprobenumfang bei gleichem Verhalten der Grundgesamtheit vervielfacht wird.",
     "2022-C-3d"),
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
