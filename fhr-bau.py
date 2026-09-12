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
    "jahr": "2023",
    "papier": "A",
    "datei": "23_FOS_Ma_A_LH.pdf",
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
# Vorlage:
#   row(id="2026-B-1a", aufgabe="1", titel="Differentialrechnung",
#       teilaufgabe="a", seite="2", punkte="3",
#       leitidee="...", thema="...", typ="...", typ_neben="",
#       stichwoerter="...|...", voraussetzungen="",
#       format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
#       material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
#       gegeben="...", gesucht="...", verfahren="...", schritte="2",
#       zahlenraum="dezimal", einheiten="", abhaengig_von="",
#       ergebnis="... (amtlich)", zwischenergebnis="",
#       niveau_geschaetzt="II", fehlerquelle="...", bemerkung="Gutachten: ...")

row(id="2023-A-1a", aufgabe="1", titel="Differentialrechnung", teilaufgabe="a", seite="2", punkte="3",
    leitidee="Differentialrechnung", thema="Verhalten im Unendlichen",
    typ="Achsensymmetrie am Funktionsterm beurteilen",
    typ_neben="Verhalten im Unendlichen bestimmen",
    stichwoerter="Achsensymmetrie|gerade Exponenten|Grenzwert|gerader Grad",
    voraussetzungen="Grenzwertschreibweise verwenden",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/8)x^4 + 4x^2 + 8; x aus IR; der Graph heißt Gf; der Punkt Q(2; 22) liegt auf Gf",
    gesucht="Begründung für die Achsensymmetrie von Gf zur y-Achse|Verhalten der Funktionswerte von f im Unendlichen",
    verfahren="an den ausschließlich geraden Exponenten die Achsensymmetrie erkennen oder f(−x) = f(x) zeigen; am geraden Grad und am negativen Koeffizienten der höchsten Potenz beide Grenzwerte ablesen",
    schritte="2", zahlenraum="Bruch|ganz|negativ|Potenz",
    ergebnis="der Graph ist achsensymmetrisch zur y-Achse, weil nur gerade Exponenten vorkommen, gleichwertig f(−x) = f(x)|für x gegen −∞ und für x gegen ∞ geht f(x) jeweils gegen −∞ (amtlich)",
    niveau_geschaetzt="I",
    fehlerquelle="beim Verhalten im Unendlichen das negative Vorzeichen der höchsten Potenz übersehen und beide Grenzwerte gegen plus unendlich angeben",
    bemerkung="Gutachten: Begründen der Symmetrie 1 BE, Angeben des Verhaltens im Unendlichen 2 BE; thema nach dem Punkt-Schwerpunkt gewählt, der typ steht in fhr-typen.csv unter Symmetrie nachweisen")

row(id="2023-A-1b", aufgabe="1", titel="Differentialrechnung", teilaufgabe="b", seite="2", punkte="8",
    leitidee="Differentialrechnung", thema="Extrem- und Sattelpunkte",
    typ="Extrem- und Sattelpunkte über zweite Ableitung",
    typ_neben="Ableitung ganzrationale Funktion|Nullstellen durch Ausklammern",
    stichwoerter="Extrempunkte|notwendige Bedingung|zweite Ableitung|Ausklammern|Hoch- und Tiefpunkt",
    voraussetzungen="Satz vom Nullprodukt anwenden|reinquadratische Gleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/8)x^4 + 4x^2 + 8; x aus IR",
    gesucht="Art und Koordinaten aller Extrempunkte von Gf",
    verfahren="erste und zweite Ableitung bilden, f'(x) = 0 durch Ausklammern von x lösen, die drei Stellen in f'' einsetzen und die Art bestimmen, dann die Funktionswerte berechnen",
    schritte="6", zahlenraum="dezimal|ganz|negativ|Potenz",
    ergebnis="T(0; 8) als Tiefpunkt|H1(−4; 40) und H2(4; 40) als Hochpunkte (amtlich)",
    zwischenergebnis="f'(x) = −0,5x^3 + 8x|f''(x) = −1,5x^2 + 8|x1 = 0 und x2,3 = ±4|f''(0) = 8 > 0|f''(±4) = −16 < 0",
    niveau_geschaetzt="II",
    fehlerquelle="beim Ausklammern die Lösung x = 0 verlieren und nur die beiden Hochpunkte angeben",
    bemerkung="Gutachten: Notieren der ersten und zweiten Ableitung 2 BE, Berechnen der Extremstellen von f 3 BE, Angeben der Extrempunkte mit Begründung 3 BE")

row(id="2023-A-1c", aufgabe="1", titel="Differentialrechnung", teilaufgabe="c", seite="2", punkte="4",
    leitidee="Differentialrechnung", thema="Normale",
    typ="Anstieg des Graphen an einer Stelle berechnen",
    typ_neben="Normalengleichung im Punkt",
    stichwoerter="Anstieg 12|Nachweis|negativer Kehrwert|Normale|absolutes Glied",
    voraussetzungen="Ableitung an einer Stelle berechnen|Geradengleichung aus Anstieg und Punkt bestimmen",
    format="Rechnung", operator="Weisen Sie nach|Bestimmen Sie", antwort="Zahl|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −(1/8)x^4 + 4x^2 + 8; x aus IR; der Punkt Q(2; 22) liegt auf Gf",
    gesucht="Nachweis, dass Gf im Punkt Q den Anstieg m = 12 hat|Gleichung der Normalen an Gf im Punkt Q",
    verfahren="f'(2) berechnen und mit 12 vergleichen, den Anstieg der Normale als negativen Kehrwert bilden und das absolute Glied durch Einsetzen von Q bestimmen",
    schritte="4", zahlenraum="Bruch|dezimal|negativ|Potenz",
    abhaengig_von="2023-A-1b",
    ergebnis="f'(2) = 12, der Anstieg beträgt also 12|n(x) = −(1/12)x + 133/6, das sind rund −(1/12)x + 22,17 (amtlich)",
    zwischenergebnis="f'(x) = −0,5x^3 + 8x|Anstieg der Normale −1/12|absolutes Glied 133/6 ≈ 22,17",
    niveau_geschaetzt="II",
    fehlerquelle="den Anstieg 12 der Tangente für die Normale übernehmen oder nur das Vorzeichen wechseln, ohne den Kehrwert zu bilden",
    bemerkung="Gutachten: Nachweisen des Anstiegs und Umwandeln in den Anstieg der Normalen 2 BE, Berechnen der Normalengleichung 2 BE; thema Normale gewählt, der typ steht unter Anstieg und Tangente; zweite Fundstelle des Themas Normale nach 2025-A-1h, damit ist die Wortsuche für dieses Heft bestätigt")

row(id="2023-A-1d", aufgabe="1", titel="Differentialrechnung", teilaufgabe="d", seite="2", punkte="4",
    leitidee="Differentialrechnung", thema="Graph zeichnen und zuordnen",
    typ="Wertetabelle aufstellen",
    typ_neben="Graph ganzrationaler Funktion im Intervall zeichnen",
    stichwoerter="Wertetabelle|mindestens sieben x-Werte|geeignete Achseneinteilung|Achsensymmetrie",
    voraussetzungen="Funktionswerte mit dem Taschenrechner berechnen|Achsen geeignet skalieren",
    format="Tabelle|Zeichnen", operator="Erstellen Sie|Zeichnen Sie|Wählen Sie", antwort="Tabelle|Grafik",
    material="keins",
    skizze="entstehen sollen eine selbst angelegte Wertetabelle mit mindestens sieben x-Werten aus dem Intervall −6 <= x <= 6 und ein selbst angelegtes kartesisches Koordinatensystem mit x von −6 bis 6 und y von etwa −20 bis 45; der Graph ist achsensymmetrisch zur y-Achse, kommt bei (−6; −10) von unten, steigt zum Hochpunkt (−4; 40), fällt zum Tiefpunkt (0; 8), steigt zum Hochpunkt (4; 40) und fällt bis (6; −10)",
    kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −(1/8)x^4 + 4x^2 + 8; x aus IR; Intervall −6 <= x <= 6",
    gesucht="Wertetabelle mit mindestens sieben x-Werten aus dem Intervall|Graph von Gf in diesem Intervall mit geeigneter Achseneinteilung",
    verfahren="mindestens sieben Funktionswerte berechnen, wegen der Achsensymmetrie paarweise übernehmen, in eine eigene Tabelle eintragen, die Achsen so einteilen, dass Werte von −10 bis 40 Platz haben, und die Punkte verbinden",
    schritte="3", zahlenraum="dezimal|ganz|negativ|Potenz",
    abhaengig_von="2023-A-1b",
    ergebnis="Wertetabelle zum Beispiel f(±1) = 11,88; f(±3) = 33,88; f(±5) = 29,88; f(±6) = −10|Graph achsensymmetrisch zur y-Achse mit den Hochpunkten (±4; 40) und dem Tiefpunkt (0; 8) (amtlich)",
    zwischenergebnis="f(0) = 8|f(±2) = 22",
    niveau_geschaetzt="II",
    fehlerquelle="die y-Achse zu grob einteilen, sodass der Hochpunkt bei 40 und der Wert −10 nicht beide ins Bild passen",
    bemerkung="Gutachten: Wertetabelle mit mindestens 7 Wertepaaren 1 BE, Zeichnen des Graphen ohne Dreieck 3 BE; der Erwartungshorizont nennt die Wertepaare zu ±1, ±3, ±5 und ±6 und weist darauf hin, dass das Dreieck OPQ erst in Teilaufgabe e ergänzt wird")

row(id="2023-A-1e", aufgabe="1", titel="Differentialrechnung", teilaufgabe="e", seite="2", punkte="5",
    leitidee="Differentialrechnung", thema="Extremwertaufgaben",
    typ="Dreieck in das Koordinatensystem einzeichnen",
    typ_neben="Dreiecksfläche aus Punktkoordinaten berechnen|Zielfunktion aus Haupt- und Nebenbedingung aufstellen",
    stichwoerter="rechtwinkliges Dreieck|Grundseite und Höhe|Hauptbedingung|Nebenbedingung|Zielfunktion",
    voraussetzungen="Punkte in die eigene Zeichnung übertragen|Klammern ausmultiplizieren",
    format="Zeichnen|Rechnung", operator="Ergänzen Sie|Berechnen Sie|Zeigen Sie", antwort="Grafik|Zahl|Term",
    material="keins",
    skizze="in die selbst angelegte Zeichnung aus Teilaufgabe d wird das rechtwinklige Dreieck OPQ eingetragen: von O(0; 0) waagerecht zu P(2; 0), von dort senkrecht hinauf zu Q(2; 22) und zurück zu O; der rechte Winkel liegt bei P",
    kontext="ohne", textumfang="lang",
    gegeben="f(x) = −(1/8)x^4 + 4x^2 + 8; x aus IR; die Punkte O(0; 0), P(2; 0) und Q(2; 22) bilden ein rechtwinkliges Dreieck; für ein beliebiges rechtwinkliges Dreieck OP'Q' ist Q'(x; f(x)) ein beliebiger Punkt auf Gf im Intervall 0 < x < 6 und P'(x; 0) liegt senkrecht unter Q' auf der x-Achse; die Zeichnung aus Teilaufgabe d liegt vor",
    gesucht="Dreieck OPQ in der Zeichnung aus Teilaufgabe d|Maßzahl des Flächeninhalts des Dreiecks OPQ|Nachweis, dass A(x) = −(1/16)x^5 + 2x^3 + 4x den Flächeninhalt eines beliebigen Dreiecks OP'Q' angibt",
    verfahren="das Dreieck mit den Eckpunkten O, P und Q eintragen; den Flächeninhalt aus Grundseite 2 und Höhe 22 berechnen; für den allgemeinen Fall die Hauptbedingung A = (1/2) g · h mit den Nebenbedingungen g = x und h = f(x) besetzen und ausmultiplizieren",
    schritte="4", zahlenraum="dezimal|ganz|negativ|Potenz", einheiten="FE",
    abhaengig_von="2023-A-1d",
    ergebnis="Dreieck OPQ eingezeichnet|Flächeninhalt 22 FE|A(x) = (1/2)x · (−(1/8)x^4 + 4x^2 + 8) = −(1/16)x^5 + 2x^3 + 4x (amtlich)",
    zwischenergebnis="Hauptbedingung A = (1/2) g · h|Nebenbedingungen g = x und h = f(x)",
    niveau_geschaetzt="II",
    fehlerquelle="bei der Zielfunktion den Faktor 1/2 vergessen und den Term von f unverändert mit x multiplizieren",
    bemerkung="Gutachten: Ergänzen des Dreiecks in der Zeichnung 1 BE, Berechnen des Flächeninhalts für x = 2 1 BE, Ermitteln der Zielfunktion A 3 BE; thema nach dem Punkt-Schwerpunkt Zielfunktion gewählt; das Heft nennt A(x) als Vorgabe")

row(id="2023-A-1f", aufgabe="1", titel="Differentialrechnung", teilaufgabe="f", seite="2", punkte="6",
    leitidee="Differentialrechnung", thema="Extremwertaufgaben",
    typ="Maximum der Zielfunktion bestimmen",
    typ_neben="Ableitung ganzrationale Funktion|Nullstellen über Substitution biquadratisch",
    stichwoerter="Extremstelle der Zielfunktion|Substitution|Lösungsformel|maximaler Flächeninhalt|Intervallgrenzen",
    voraussetzungen="quadratische Gleichung mit Lösungsformel lösen|negative Lösung der Substitution verwerfen",
    format="Rechnung", operator="Ermitteln Sie|Weisen Sie nach", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="die Zielfunktion A(x) = −(1/16)x^5 + 2x^3 + 4x aus Teilaufgabe e beschreibt den Flächeninhalt des Dreiecks OP'Q' im Intervall 0 < x < 6",
    gesucht="Extremstelle xE der Funktion A im Intervall 0 < x < 6|Nachweis, dass das durch xE festgelegte Dreieck OP'Q' den maximalen Flächeninhalt besitzt",
    verfahren="A'(x) bilden, A'(x) = 0 mit der Substitution z = x^2 auf eine quadratische Gleichung bringen und lösen, zurücksubstituieren und die Lösung außerhalb des Intervalls verwerfen, dann mit A''(xE) < 0 das Maximum nachweisen",
    schritte="6", zahlenraum="dezimal|Bruch|negativ|Potenz|Wurzel",
    abhaengig_von="2023-A-1e",
    ergebnis="xE ≈ 4,45|A''(4,45) ≈ −56,75 < 0, für xE ≈ 4,45 besitzt das Dreieck also den maximalen Flächeninhalt (amtlich)",
    zwischenergebnis="A'(x) = −(5/16)x^4 + 6x^2 + 4|nach der Substitution z^2 − (96/5)z − 64/5 = 0|z1 ≈ 19,84 und z2 ≈ −0,64|A''(x) = −(5/4)x^3 + 12x",
    niveau_geschaetzt="III",
    fehlerquelle="die zweite Wurzel x ≈ −4,45 mit angeben, obwohl sie nicht im Intervall liegt, oder die negative Lösung z2 zurücksubstituieren",
    bemerkung="Gutachten: Notieren der Ableitung A'(x) 1 BE, Berechnen der Extremstellen von A 3 BE, Nachweisen des maximalen Flächeninhalts 2 BE; eigene Rechnung mit der ungerundeten Extremstelle 4,4548 ergibt A'' ≈ −57,05, der Erwartungshorizont rechnet mit der gerundeten Stelle 4,45 und erhält −56,75; ohne Folge, weil nur das Vorzeichen zählt")

row(id="2023-A-2a", aufgabe="2", titel="Differential- und Integralrechnung", teilaufgabe="a", seite="5", punkte="5",
    leitidee="Differentialrechnung", thema="Funktionsgleichung bestimmen",
    typ="Funktionsgleichung mit Symmetriebedingung über LGS",
    stichwoerter="quadratische Funktion|Achsensymmetrie|verkürzter Ansatz|LGS mit zwei Unbekannten",
    voraussetzungen="aus der Symmetrie auf das fehlende lineare Glied schließen|LGS mit zwei Unbekannten lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="der Graph Gg einer quadratischen Funktion g verläuft symmetrisch zur y-Achse; die Punkte A(2; −6) und B(6; 10) liegen auf Gg",
    gesucht="eine zugehörige Funktionsgleichung der Funktion g",
    verfahren="wegen der Achsensymmetrie den verkürzten Ansatz g(x) = ax^2 + b wählen, beide Punkte einsetzen und das lineare Gleichungssystem lösen",
    schritte="4", zahlenraum="Bruch|ganz|negativ|Potenz",
    ergebnis="g(x) = (1/2)x^2 − 8 (amtlich)",
    zwischenergebnis="Ansatz g(x) = ax^2 + b|4a + b = −6 und 36a + b = 10|a = 1/2 und b = −8",
    niveau_geschaetzt="II",
    fehlerquelle="den vollen Ansatz ax^2 + bx + c verwenden und mit nur zwei Punkten ein unterbestimmtes System erhalten",
    bemerkung="Gutachten: Aufstellen des LGS 3 BE, Lösen des LGS und Angabe der Funktionsgleichung 2 BE; das Heft nennt g(x) als Kontrollergebnis")

row(id="2023-A-2b", aufgabe="2", titel="Differential- und Integralrechnung", teilaufgabe="b", seite="5", punkte="5",
    leitidee="Integralrechnung", thema="Fläche zwischen Graph und x-Achse",
    typ="Fläche zwischen Graph und x-Achse berechnen",
    typ_neben="Nullstellen einer quadratischen Funktion über Wurzelziehen",
    stichwoerter="vollständig eingeschlossene Fläche|Nullstellen als Grenzen|Stammfunktion|Betrag",
    voraussetzungen="Stammfunktion bilden|Betrag bei negativem Integral nehmen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g(x) = (1/2)x^2 − 8; der Graph Gg schließt mit der x-Achse eine Fläche vollständig ein",
    gesucht="Maßzahl des Flächeninhalts dieser Fläche",
    verfahren="g(x) = 0 setzen und die Nullstellen durch Wurzelziehen als Integralgrenzen bestimmen, die Stammfunktion bilden, das bestimmte Integral von −4 bis 4 berechnen und den Betrag nehmen",
    schritte="4", zahlenraum="Bruch|dezimal|negativ|Potenz", einheiten="FE",
    abhaengig_von="2023-A-2a",
    ergebnis="Flächeninhalt 128/3 ≈ 42,67 FE (amtlich)",
    zwischenergebnis="Nullstellen x1,2 = ±4|Stammfunktion G(x) = (1/6)x^3 − 8x|Integral von −4 bis 4 ergibt −128/3",
    niveau_geschaetzt="II",
    fehlerquelle="den negativen Integralwert ohne Betrag als Flächeninhalt angeben",
    bemerkung="Gutachten: Berechnen der Nullstellen von g 2 BE, Ermitteln des Flächeninhalts 3 BE")

row(id="2023-A-2c", aufgabe="2", titel="Differential- und Integralrechnung", teilaufgabe="c", seite="5", punkte="2",
    leitidee="Grundlagen", thema="Terme umformen",
    typ="Produkt zweier Funktionsterme ausmultiplizieren",
    stichwoerter="Produkt zweier Funktionen|ausmultiplizieren|zusammenfassen|vorgegebene Darstellung",
    voraussetzungen="Klammern ausmultiplizieren|gleichartige Glieder zusammenfassen",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g(x) = (1/2)x^2 − 8; h(x) = x − 4; die ganzrationale Funktion f ergibt sich als Produkt der Funktionen g und h",
    gesucht="Nachweis, dass sich f als f(x) = (1/2)x^3 − 2x^2 − 8x + 32 darstellen lässt",
    verfahren="beide Terme multiplizieren, jedes Glied mit jedem, und die entstandenen Glieder ordnen und zusammenfassen",
    schritte="2", zahlenraum="Bruch|ganz|negativ|Potenz",
    abhaengig_von="2023-A-2a",
    ergebnis="f(x) = ((1/2)x^2 − 8) · (x − 4) = (1/2)x^3 − 2x^2 − 8x + 32 (amtlich)",
    niveau_geschaetzt="I",
    fehlerquelle="nur die jeweils ersten Glieder multiplizieren und die gemischten Produkte vergessen",
    bemerkung="Gutachten: Berechnen der Funktionsgleichung von f 2 BE; das Heft nennt f(x) als Vorgabe")

row(id="2023-A-2d", aufgabe="2", titel="Differential- und Integralrechnung", teilaufgabe="d", seite="5", punkte="2",
    leitidee="Differentialrechnung", thema="Nullstellen ganzrationaler Funktionen",
    typ="Nullstellen eines Produkts von Funktionen begründen",
    stichwoerter="Produkt von Funktionen|Satz vom Nullprodukt|keine weiteren Nullstellen|gemeinsame Nullstelle",
    voraussetzungen="Nullstelle einer linearen Funktion bestimmen|Nullstellenmengen vergleichen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g(x) = (1/2)x^2 − 8 mit den Nullstellen ±4; h(x) = x − 4; f ist das Produkt von g und h mit f(x) = (1/2)x^3 − 2x^2 − 8x + 32",
    gesucht="Begründung, dass f genau dieselben Nullstellen wie g und keine weiteren besitzt",
    verfahren="aus dem Satz vom Nullprodukt folgt, dass sich die Nullstellen von f aus denen von g und h zusammensetzen; h hat nur die Nullstelle 4, die schon Nullstelle von g ist, also kommt keine hinzu",
    schritte="2", zahlenraum="ganz|negativ",
    abhaengig_von="2023-A-2b|2023-A-2c",
    ergebnis="da f das Produkt von g und h ist, setzt sich die Menge der Nullstellen von f aus den Nullstellen von g und h zusammen; h besitzt nur die Nullstelle 4, die zugleich Nullstelle von g ist, also haben f und g genau die Nullstellen ±4 (amtlich); eine Begründung durch Rechnung ist ebenfalls zugelassen",
    zwischenergebnis="Nullstelle von h bei x = 4",
    niveau_geschaetzt="III",
    fehlerquelle="die Nullstelle von h als zusätzliche dritte Nullstelle von f angeben",
    bemerkung="Gutachten: Begründen der Nullstellen von f 2 BE; der Erwartungshorizont lässt alternative Begründungen ausdrücklich zu")

row(id="2023-A-2e", aufgabe="2", titel="Differential- und Integralrechnung", teilaufgabe="e", seite="5", punkte="6",
    leitidee="Differentialrechnung", thema="Wendepunkte",
    typ="Wendepunkte über zweite Ableitung",
    typ_neben="Ableitung ganzrationale Funktion",
    stichwoerter="Wendepunkt|erste drei Ableitungen|notwendige Bedingung|dritte Ableitung ungleich Null",
    voraussetzungen="lineare Gleichung lösen|Bruch als Stelle einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = (1/2)x^3 − 2x^2 − 8x + 32; x aus IR",
    gesucht="Koordinaten aller Wendepunkte des Graphen von f",
    verfahren="erste bis dritte Ableitung bilden, f''(x) = 0 lösen, mit f'''(x) ungleich Null die Wendestelle bestätigen und den Funktionswert berechnen",
    schritte="5", zahlenraum="Bruch|dezimal|ganz|negativ|Potenz",
    abhaengig_von="2023-A-2c",
    ergebnis="W(4/3; 18,96) (amtlich)",
    zwischenergebnis="f'(x) = (3/2)x^2 − 4x − 8|f''(x) = 3x − 4|f'''(x) = 3|Wendestelle x = 4/3|f(4/3) = 512/27 ≈ 18,96",
    niveau_geschaetzt="II",
    fehlerquelle="die Wendestelle 4/3 als Ergebnis angeben und den Funktionswert nicht berechnen",
    bemerkung="Gutachten: Notieren der ersten drei Ableitungen von f 3 BE, Berechnen des Wendepunkts mit Nachweis 3 BE")

row(id="2023-A-3a", aufgabe="3", titel="Stochastik", teilaufgabe="a", seite="7", punkte="2",
    leitidee="Stochastik", thema="Daten darstellen und aufbereiten",
    typ="Vierfeldertafel vervollständigen",
    stichwoerter="vier Tarifoptionen|Randsummen|Erwachsene und Kinder|Saunatarif",
    voraussetzungen="Restanzahl über die Gesamtzahl bilden",
    format="Tabelle", operator="Ermitteln Sie", antwort="Tabelle",
    material="Tabelle",
    skizze="im Aufgabentext stehen zwei Tabellen: die Preistabelle Happy-Hour-Tarif mit den Zeilen Schwimmbad (15 € für Erwachsene, 10 € für Kinder) und Schwimmbad + Sauna (25 €, 18 €), daneben die Übersicht Happy-Hour-Tarif Gästezahlen mit denselben Zeilen und den Spalten Erwachsene und Kinder, deren vier Felder als Punktreihen zum Ausfüllen vorgedruckt sind",
    kontext="Freizeit/Schwimmbad", textumfang="mittel",
    gegeben="80 Happy-Hour-Gäste, darunter 30 Erwachsene, der Rest Kinder; 60 Personen haben den Saunatarif gewählt, davon 35 Kinder; Preistabelle Schwimmbad 15 € für Erwachsene und 10 € für Kinder, Schwimmbad mit Sauna 25 € für Erwachsene und 18 € für Kinder",
    gesucht="Anzahl der Gäste zu jeder der vier Tarifoptionen",
    verfahren="aus 80 und 30 die 50 Kinder bestimmen, aus 60 Saunagästen und 35 Saunakindern die 25 Erwachsenen mit Sauna, und die beiden Felder der Zeile Schwimmbad über die Randsummen ergänzen",
    schritte="3", zahlenraum="ganz",
    ergebnis="Schwimmbad 5 Erwachsene und 15 Kinder|Schwimmbad mit Sauna 25 Erwachsene und 35 Kinder (amtlich)",
    zwischenergebnis="50 Kinder insgesamt|25 Erwachsene mit Saunatarif",
    niveau_geschaetzt="II",
    fehlerquelle="die 35 Saunakinder von den 30 Erwachsenen statt von den 50 Kindern abziehen",
    bemerkung="Gutachten: Ermitteln der Gästeanzahlen in der Übersicht 2 BE; die Übersicht ist eine Vierfeldertafel mit absoluten Anzahlen, thema Daten darstellen und aufbereiten gewählt, weil die Teilaufgabe keine Unabhängigkeit verlangt – der typ steht unter Unabhängigkeit von Ereignissen")

row(id="2023-A-3b", aufgabe="3", titel="Stochastik", teilaufgabe="b", seite="7", punkte="4",
    leitidee="Stochastik", thema="Statistische Kenngrößen",
    typ="Mittelwert aus Häufigkeitstabelle",
    typ_neben="Standardabweichung aus Häufigkeitstabelle",
    stichwoerter="arithmetisches Mittel|gewichtete Eintrittspreise|Standardabweichung|80 Gaeste",
    voraussetzungen="Gästezahlen aus Teilaufgabe a übernehmen|Wurzel ziehen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle",
    skizze="die Preistabelle aus dem Aufgabenstamm und die in Teilaufgabe a gefüllte Übersicht der Gästezahlen werden weiterverwendet",
    kontext="Freizeit/Schwimmbad", textumfang="kurz",
    gegeben="vier Tarifgruppen mit Anzahl und Eintrittspreis: 5 Erwachsene zu 15 €, 15 Kinder zu 10 €, 25 Erwachsene zu 25 €, 35 Kinder zu 18 €; insgesamt 80 Gäste",
    gesucht="arithmetisches Mittel des Eintrittspreises aller 80 Gäste|zugehörige Standardabweichung",
    verfahren="die vier Preise mit ihren Anzahlen gewichten und die Summe durch 80 teilen, dann die mit den Anzahlen gewichteten quadratischen Abweichungen vom Mittelwert summieren, durch 80 teilen und die Wurzel ziehen",
    schritte="4", zahlenraum="dezimal|Bruch", einheiten="€",
    abhaengig_von="2023-A-3a",
    ergebnis="arithmetisches Mittel 18,50 €|Standardabweichung etwa 5,26 € (amtlich)",
    zwischenergebnis="Summe der Eintrittspreise 1480 €|s^2 = 221/8 = 27,625",
    niveau_geschaetzt="II",
    fehlerquelle="den Mittelwert aus den vier Preisen ohne Gewichtung mit den Gästezahlen bilden",
    bemerkung="Gutachten: Berechnen des arithmetischen Mittels 2 BE, Berechnen der Standardabweichung 2 BE; der Erwartungshorizont nennt zusätzlich die Werte nach der Formel mit n − 1, s^2 ≈ 27,97 und s ≈ 5,29")

row(id="2023-A-3c", aufgabe="3", titel="Stochastik", teilaufgabe="c", seite="7", punkte="2",
    leitidee="Stochastik", thema="Kombinatorische Abzählverfahren",
    typ="Kombination ohne Wiederholung berechnen",
    stichwoerter="drei aus 80|Binomialkoeffizient|Reihenfolge unerheblich|Auswahlmoeglichkeiten",
    voraussetzungen="Binomialkoeffizient mit dem Taschenrechner berechnen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Freizeit/Schwimmbad", textumfang="kurz",
    gegeben="von allen 80 Happy-Hour-Gästen erhalten drei Personen ein kostenloses Mittagessen",
    gesucht="Anzahl der Möglichkeiten, aus 80 Gästen drei Personen auszuwählen",
    verfahren="den Binomialkoeffizienten 80 über 3 berechnen, weil die Reihenfolge der drei Personen keine Rolle spielt",
    schritte="1", zahlenraum="ganz",
    ergebnis="82 160 Möglichkeiten (amtlich)",
    niveau_geschaetzt="II",
    fehlerquelle="die Reihenfolge mitzählen und 492 960 angeben",
    bemerkung="Gutachten: Bestimmen der Auswahlmöglichkeiten 2 BE")

row(id="2023-A-3d", aufgabe="3", titel="Stochastik", teilaufgabe="d", seite="7", punkte="7",
    leitidee="Stochastik", thema="Mehrstufige Zufallsexperimente",
    typ="Baumdiagramm dreistufig ohne Zurücklegen darstellen",
    typ_neben="Pfadregel dreistufig ohne Zurücklegen anwenden|Wahrscheinlichkeit über mehrere Pfade summieren",
    stichwoerter="Verlosung von drei Mittagessen|dreistufig ohne Zuruecklegen|vollstaendiges Baumdiagramm|mindestens zwei Kinder",
    voraussetzungen="Nenner in jeder Stufe verkleinern|Ereignis mindestens zwei in Pfade zerlegen",
    format="Zeichnen|Rechnung", operator="Ermitteln Sie", antwort="Grafik|Zahl",
    material="keins",
    skizze="zu zeichnen ist ein vollständig beschriftetes dreistufiges Baumdiagramm für das Ziehen von drei Personen ohne Zurücklegen aus 30 Erwachsenen (E) und 50 Kindern (K): erste Stufe 30/80 und 50/80, zweite Stufe mit Nenner 79, dritte Stufe mit Nenner 78, insgesamt acht Pfade",
    kontext="Freizeit/Verlosung", textumfang="lang",
    gegeben="unter den 80 Happy-Hour-Gästen sind 30 Erwachsene und 50 Kinder; drei Personen werden für ein kostenloses Mittagessen zufällig verlost, eine Person kann nur einmal gewinnen; Ereignis A drei Erwachsene erhalten ein kostenloses Mittagessen, Ereignis B mindestens zwei Kinder erhalten ein kostenloses Mittagessen",
    gesucht="geeignetes vollständiges Baumdiagramm|P(A)|P(B)",
    verfahren="das dreistufige Baumdiagramm ohne Zurücklegen mit in jeder Stufe sinkenden Nennern zeichnen, für A den Pfad mit drei Erwachsenen multiplizieren und für B die vier Pfade mit mindestens zwei Kindern addieren",
    schritte="5", zahlenraum="Bruch|Prozent",
    ergebnis="P(A) = 203/4108 ≈ 4,94 %|P(B) = 5635/8216 ≈ 68,59 % (amtlich)",
    zwischenergebnis="P(A) = 30/80 · 29/79 · 28/78|P(B) als Summe der Pfade EKK, KEK, KKE und KKK",
    niveau_geschaetzt="III",
    fehlerquelle="bei B nur den Pfad mit drei Kindern oder nur genau zwei Kinder berücksichtigen",
    bemerkung="Gutachten: Erstellen des vollständigen Baumdiagramms 4 BE, Berechnen der Wahrscheinlichkeit von A 1 BE, Berechnen der Wahrscheinlichkeit von B 2 BE; dreistufig und ohne Zurücklegen, daher nach der Arbeitsregel in fhr.md Abschnitt 6 bei Mehrstufige Zufallsexperimente geführt")

row(id="2023-A-3e", aufgabe="3", titel="Stochastik", teilaufgabe="e", seite="7", punkte="3",
    leitidee="Stochastik", thema="Unabhängigkeit von Ereignissen",
    typ="Stochastische Unabhängigkeit prüfen",
    stichwoerter="Ereignis C Erwachsenentarif|Ereignis D Saunabesuch|Produkt der Wahrscheinlichkeiten|Schnittereignis",
    voraussetzungen="Anteile an 80 bilden|Schnittereignis aus der Übersicht ablesen",
    format="Rechnung|Begründung", operator="Prüfen Sie", antwort="Zahl|Text",
    material="Tabelle",
    skizze="die in Teilaufgabe a gefüllte Übersicht der Gästezahlen wird weiterverwendet",
    kontext="Freizeit/Schwimmbad", textumfang="mittel",
    gegeben="80 Happy-Hour-Gäste, davon 30 Erwachsene und 60 mit Saunatarif, darunter nach Teilaufgabe a 25 Erwachsene mit Saunatarif; für eine beliebige Person bedeutet Ereignis C sie hat den Erwachsenentarif bezahlt und Ereignis D sie hat den Saunabesuch gewählt",
    gesucht="Prüfung, ob die Ereignisse C und D stochastisch unabhängig sind",
    verfahren="P(C), P(D) und P(C und D) als Anteile an 80 bestimmen und das Produkt der Einzelwahrscheinlichkeiten mit der Wahrscheinlichkeit des Schnittereignisses vergleichen",
    schritte="4", zahlenraum="Bruch",
    abhaengig_von="2023-A-3a",
    ergebnis="P(C) · P(D) = 9/32 ist ungleich P(C und D) = 5/16, also sind C und D stochastisch abhängig (amtlich)",
    zwischenergebnis="P(C) = 30/80 = 3/8|P(D) = 60/80 = 3/4|P(C und D) = 25/80 = 5/16",
    niveau_geschaetzt="III",
    fehlerquelle="P(C und D) auf die 60 Saunagäste beziehen und 25/60 ansetzen",
    bemerkung="Gutachten: Prüfen der stochastischen Unabhängigkeit von C und D 3 BE")

row(id="2023-A-3f", aufgabe="3", titel="Stochastik", teilaufgabe="f", seite="7", punkte="2",
    leitidee="Stochastik", thema="Kombinatorische Abzählverfahren",
    typ="Permutation ohne Wiederholung berechnen",
    stichwoerter="alle 50 Kinder|Warteschlange|Fakultaet|Anordnungen",
    voraussetzungen="Anzahl der Kinder aus dem Aufgabenstamm bestimmen|Fakultät mit dem Taschenrechner berechnen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Freizeit/Wasserrutsche", textumfang="kurz",
    gegeben="unter den 80 Happy-Hour-Gästen sind 30 Erwachsene und der Rest Kinder; zur Einweihung der Wasserrutsche stellen sich alle Kinder zum Rutschen an",
    gesucht="Anzahl der verschiedenen Warteschlangen, die sich ergeben können",
    verfahren="die 50 Kinder aus dem Aufgabenstamm bestimmen und 50 Fakultät berechnen, weil alle Kinder unterscheidbar sind und jede Reihenfolge zählt",
    schritte="2", zahlenraum="ganz|Potenz",
    ergebnis="etwa 3,04 · 10^64 verschiedene Warteschlangen (amtlich)",
    zwischenergebnis="50 Kinder als Anzahl der Elemente",
    niveau_geschaetzt="II",
    fehlerquelle="mit allen 80 Gästen statt mit den 50 Kindern rechnen",
    bemerkung="Gutachten: Bestimmen der Anzahl an Warteschlangen 2 BE")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Dreieck in das Koordinatensystem einzeichnen", "Differentialrechnung", "Graph zeichnen und zuordnen",
     "Ein durch seine Eckpunkte gegebenes Dreieck in ein vorhandenes oder selbst angelegtes Koordinatensystem eintragen.",
     "2023-A-1e"),
    ("Dreiecksfläche aus Punktkoordinaten berechnen", "Differentialrechnung", "Extremwertaufgaben",
     "Aus den Koordinaten der Eckpunkte Grundseite und Höhe eines rechtwinkligen Dreiecks bestimmen und dessen Flächeninhalt berechnen.",
     "2023-A-1e"),
    ("Produkt zweier Funktionsterme ausmultiplizieren", "Grundlagen", "Terme umformen",
     "Zwei gegebene Funktionsterme multiplizieren, ordnen und zusammenfassen, um eine vorgegebene Darstellung nachzuweisen.",
     "2023-A-2c"),
    ("Nullstellen eines Produkts von Funktionen begründen", "Differentialrechnung", "Nullstellen ganzrationaler Funktionen",
     "Über den Satz vom Nullprodukt begründen, welche Nullstellen ein als Produkt gegebener Funktionsterm besitzt, und ausschließen, dass weitere hinzukommen.",
     "2023-A-2d"),
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
