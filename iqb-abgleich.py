# -*- coding: utf-8 -*-
"""iqb-abgleich.py – Abgleichlauf über die Typenliste des Profils iqb (Kern § 9).
Version 0.5 · 14.09.2026 · gilt mit iqb.md v0.8 und iqb-bau.py v0.7

Benennt Typen um und zieht Typen zusammen, in iqb-typen.csv und in beiden
Typfeldern von iqb-katalog.csv. Die Regeln je Lauf stehen in LAEUFE: PRAEFIX
(alt → Gegenstandsklasse), ZUSAMMEN (alt → neu; mehrere alte Namen auf
denselben neuen Namen heißt zusammenziehen, die erste Zeile der Typenliste
bleibt mit ihrer beispiel_id), NEUE_DEFINITION und NEUES_THEMA (nur für
zusammengezogene oder umgewidmete Typen). Aufruf `python iqb-abgleich.py [N]`
führt Lauf N aus (ohne Angabe den jüngsten); jeder Lauf setzt den Stand nach
dem vorigen voraus und wird genau einmal gefahren. Schreibt beide Dateien im
Format von iqb-bau.py und gibt die Liste alt → neu für iqb-pruefungen.md § 5
aus. Danach iqb-bau.py mit leerem ZEILEN laufen lassen.

Lauf 1 (13.09.2026, Entscheidung 24): Gegenstandsklasse als Präfix nach
iqb.md § 6, neun Zusammenziehungen (183 → 174 Typen).
Lauf 2 (13.09.2026, nach 2022-ea-A): vier Zusammenziehungen (268 → 264).
Lauf 3 (14.09.2026, nach 2020-ea-A): drei Zusammenziehungen, zwei erweiterte
Definitionen (341 → 338).
Lauf 4 (14.09.2026, nach 2018-ea-A): fünf Zusammenziehungen, eine Umbenennung,
eine erweiterte Definition (406 → 401).
Lauf 5 (14.09.2026, nach dem Probestapel Teil B): zwei erweiterte Definitionen,
Feldkorrektur bemerkung (Markierung Traegerbindung), keine Zusammenziehung (433).
"""
import csv, io, re, sys, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

KAT, TYP = "iqb-katalog.csv", "iqb-typen.csv"

# ======================================================================= Lauf 1
# ---- Präfixe (Gegenstandsklasse: Feinetikett) für Themen mit Klassen, iqb.md § 6
PRAEFIX_1 = {
    # Funktionsklassen und Eigenschaften
    "Flächeninhalt eines Dreiecks aus Extrempunkten der Sinusfunktion berechnen": "Extrempunkte",
    "Abstand von Extrempunkten einer gestreckten Sinusfunktion vergleichen": "Extrempunkte",
    "Abbildung zwischen zwei Graphen angeben": "Transformation",
    "Fehlende Punktsymmetrie aus der Wertemenge begründen": "Symmetrie",
    "Wertemenge einer transformierten Funktion begründen": "Transformation",
    "Nullstelle durch Einsetzen nachweisen": "Nullstellen und Werte",
    "Verschobenen Graphen in die Abbildung skizzieren": "Transformation",
    "Extrempunkt eines transformierten Graphen angeben": "Transformation",
    "Punktsymmetrie am Term über ungerade Exponenten begründen": "Symmetrie",
    "Aussage über eine Verschiebung zwischen zwei Graphen beurteilen": "Transformation",
    # Flächeninhalt durch Integration
    "Summe zweier Integrale als Flächeninhalt beurteilen": "Integralwert",
    "Integral einer Differenzfunktion grafisch abschätzen": "Integralwert",
    "Fläche zwischen zwei Graphen mit vorgegebener Stammfunktion berechnen": "Fläche",
    "Integral null über die Punktsymmetrie begründen": "Integralwert",
    "Fläche zwischen Graph und Koordinatenachsen berechnen": "Fläche",
    "Verschiebung für die Halbierung einer Fläche über ein Integral bestimmen": "Fläche",
    "Integralwert grafisch durch Kästchenzählen bestimmen": "Integralwert",
    "Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen": "Fläche",
    "Vorzeichen eines Integrals am Graphen beurteilen": "Integralwert",
    # Punkte und Strecken im Koordinatensystem
    "Koordinaten eines Eckpunkts eines Prismas angeben": "Körper",
    "Dreieck in ein Schrägbild einzeichnen": "Ebene Figur",
    "Lage zweier Punkte zu einer Koordinatenebene begründen": "Punkt",
    "Eckpunkt mit vorgegebenen Vorzeichen nach einer Verschiebung angeben": "Körper",
    "Projektion eines Parallelogramms in eine Koordinatenebene einzeichnen": "Ebene Figur",
    "Kantenlänge eines Würfels aus gegenüberliegenden Oktaederecken nachweisen": "Körper",
    # Lagebeziehungen
    "Punktprobe an einer Ebenengleichung durchführen": "Punkt und Ebene",
    "Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen": "Punkt und Ebene",
    "Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden": "Gerade und Ebene",
    # Orthogonalität
    "Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen": "Dreieck",
    "Rechten Winkel eines Dreiecks mit Parameter nachweisen": "Dreieck",
    "Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen": "Geraden und Ebenen",
    "Orthogonalität zweier Geraden über das Skalarprodukt untersuchen": "Geraden und Ebenen",
    "Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen": "Geraden und Ebenen",
    "Parameter für einen rechten Winkel über das Skalarprodukt ermitteln": "Dreieck",
    # Flächeninhalt und Volumen im Raum
    "Höhe einer Pyramide aus dem Volumen bestimmen": "Körper",
    "Parameter eines Punktes aus einer Flächengleichheit bestimmen": "Ebene Figur",
    "Volumen eines Prismas über einer Raute berechnen": "Körper",
    "Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen": "Ebene Figur",
    "Volumen eines Teilkörpers eines Würfels berechnen": "Körper",
    "Flächenverhältnis von Dreieck und Trapez über einen Vektorterm ermitteln": "Ebene Figur",
    "Diagonalenschnittpunkt und Flächeninhalt eines Quadrats aus dem Spurpunkt einer Geraden bestimmen": "Ebene Figur",
    # Matrizen und Übergangsprozesse
    "Fehler in einem Übergangsdiagramm gegen die Matrix begründen": "Übergangsprozess",
    "Parameter einer Übergangsmatrix aus einer Zykluslänge bestimmen": "Übergangsprozess",
    "Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen": "Matrizenalgebra",
    "Gleichung mit inverser Matrix über die Eigenvektorbeziehung lösen": "Matrizenalgebra",
    "Matrix mit vorgegebener Eigenschaft angeben": "Matrizenalgebra",
    "Existenz von Matrizen mit vorgegebener Eigenschaft über ein Gleichungssystem beurteilen": "Matrizenalgebra",
    "Parameter einer Matrix aus einer Matrix-Vektor-Gleichung untersuchen": "Matrizenalgebra",
    "Parameter einer Matrix aus der Orthogonalität von v und M · v bestimmen": "Matrizenalgebra",
    "Bedingungen für die Vertauschbarkeit zweier Matrizen aus einer binomischen Gleichung untersuchen": "Matrizenalgebra",
    "Verflechtungsdiagramm zu einer Matrix zeichnen": "Verflechtung",
    "Matrixeintrag aus Mengenbedingungen ermitteln": "Verflechtung",
    "Existenz mehrerer Lösungen von M · a = 0 begründen": "Matrizenalgebra",
    "Alle Fixvektoren einer Matrix ermitteln": "Matrizenalgebra",
    "Rohstoffbedarf über die Verflechtungsmatrix berechnen": "Verflechtung",
    "Verflechtungsmatrix aus Sachbedingungen und Matrixprodukt bestimmen": "Verflechtung",
    "Wirkung einer Permutationsmatrix beschreiben und Einträge aus M · A · M = A bestimmen": "Matrizenalgebra",
    # Zufallsexperimente und Urnenmodelle
    "Sektorwinkel eines Glücksrads aus einer Wahrscheinlichkeitsbedingung berechnen": "Laplace-Experiment",
    "Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen": "Ziehen ohne Zurücklegen",
    "Laplace-Wahrscheinlichkeit für den ersten Zug angeben": "Laplace-Experiment",
    "Gleichheit zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen": "Laplace-Experiment",
}

# ---- Zusammenziehungen und Umwidmungen (alt → neu, neu kann schon existieren)
ZUSAMMEN_1 = {
    "Graph der Funktion vom Graphen der Ableitung unterscheiden":
        "Graphen von Funktion und Ableitung einander zuordnen",
    "Graph einer Stammfunktion unter vorgegebenen Graphen begründet auswählen":
        "Graphen von Funktion und Ableitung einander zuordnen",
    "Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln":
        "Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln",
    "Verhältnis zweier Trefferwahrscheinlichkeiten aus den Erwartungswerten im Diagramm nachweisen":
        "Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln",
    "Integral mit Wert null am Graphen veranschaulichen":
        "Integralwert: Integral mit Wert null am Graphen begründen",
    "Integralwert aus der Symmetrie des Graphen angeben":
        "Integralwert: Integral mit Wert null am Graphen begründen",
    "Orthogonalität von Gerade und Ebene über Normalen- und Richtungsvektor begründen":
        "Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen",
    "Vektor als Normalenvektor einer Ebene über Kollinearität nachweisen":
        "Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen",
    "Wahrscheinlichkeit für zweimal kein Treffer über die Pfadregel begründen":
        "Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen",
    "Pfadwahrscheinlichkeit für lauter Treffer berechnen und mit einer Schranke vergleichen":
        "Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen",
    "Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben":
        "Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben",
    "Hypergeometrischen Term im Sachzusammenhang deuten":
        "Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben",
    "Unbekannte Werte einer Zufallsgröße aus dem Erwartungswert bestimmen":
        "Unbekannte Größe aus einer Erwartungswertbedingung bestimmen",
    "Anzahl der Kugeln aus einer Fairnessbedingung bestimmen":
        "Unbekannte Größe aus einer Erwartungswertbedingung bestimmen",
    "Punkt auf einer Lotgeraden mit vorgegebenem Abstand zur Ebene bestimmen":
        "Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen",
    "Punkt mit vorgegebenem Abstand zu seinem Spiegelbild an einer Ebene bestimmen":
        "Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen",
    "Stammfunktionen mit einer Wertebedingung bestimmen":
        "Stammfunktion mit einer Wertebedingung bestimmen",
    "Stammfunktion durch einen vorgegebenen Punkt bestimmen":
        "Stammfunktion mit einer Wertebedingung bestimmen",
}

NEUE_DEFINITION_1 = {
    "Graphen von Funktion und Ableitung einander zuordnen":
        "Unter abgebildeten Graphen den einer Funktion, ihrer Ableitung oder einer Stammfunktion "
        "erkennen, indem Nullstellen, Extremstellen und Wendestellen einander zugeordnet werden.",
    "Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln":
        "Den ganzzahligen Erwartungswert einer Binomialverteilung an der höchsten Säule ablesen und "
        "daraus p, eine Anzahl oder das Verhältnis zweier Trefferwahrscheinlichkeiten ermitteln.",
    "Integralwert: Integral mit Wert null am Graphen begründen":
        "Am Graphen begründen oder veranschaulichen, dass ein bestimmtes Integral den Wert null hat, "
        "weil sich die orientierten Flächen über und unter der Achse aufheben (Symmetrie).",
    "Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen":
        "Begründen, dass ein Vektor oder eine Gerade senkrecht auf einer Ebene in Koordinatenform "
        "steht, weil der Vektor ein Vielfaches des ablesbaren Normalenvektors ist.",
    "Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen":
        "Die Wahrscheinlichkeit, dass alle Versuche dasselbe Ergebnis liefern, als Potenz der "
        "Einzelwahrscheinlichkeit berechnen oder begründen, gegebenenfalls mit einer Schranke vergleichen.",
    "Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben":
        "Zu einem gegebenen Term (Produkt, Summe, Potenz oder Quotient von Binomialkoeffizienten) "
        "das Ereignis und gegebenenfalls das Zufallsexperiment im Sachzusammenhang beschreiben.",
    "Unbekannte Größe aus einer Erwartungswertbedingung bestimmen":
        "Eine unbekannte Auszahlung, einen Wert der Zufallsgröße oder eine Anzahl (etwa Kugeln) aus "
        "einer Bedingung an den Erwartungswert bestimmen, etwa Erwartungswert gleich Einsatz.",
    "Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen":
        "Einen Punkt bestimmen, der von einer Ebene einen vorgegebenen Abstand hat: vom Ebenenpunkt "
        "oder Lotfußpunkt aus den normierten Normalenvektor abtragen; der Abstand kann als halber "
        "Abstand zum Spiegelbild gegeben sein.",
    "Stammfunktion mit einer Wertebedingung bestimmen":
        "Die allgemeine Stammfunktion bilden und die Integrationskonstante aus einer Wertebedingung "
        "oder einem vorgegebenen Punkt des Graphen bestimmen.",
}

NEUES_THEMA_1 = {
    "Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen":
        ("Analytische Geometrie", "Orthogonalität"),
    "Unbekannte Größe aus einer Erwartungswertbedingung bestimmen":
        ("Stochastik", "Kenngrößen von Verteilungen"),
    "Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen":
        ("Analytische Geometrie", "Abstände"),
}

# ======================================================================= Lauf 2
# Vier Zusammenziehungen nach Kern § 6 (gleiche Fertigkeit, gleiches Etikett); keine Präfixe.
ZUSAMMEN_2 = {
    "Ergebnisse zur Schnittmenge zweier Ereignisse angeben":
        "Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben",
    "Ergebnisse zum Gegenereignis zweier Ereignisse aufzählen":
        "Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben",
    "Matrizenalgebra: Alle Fixvektoren einer Matrix ermitteln":
        "Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen",
    "Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen":
        "Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen",
    "Laplace-Experiment: Gleichheit zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen":
        "Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen",
    "Laplace-Experiment: Verhältnis zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen":
        "Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen",
    "Symmetrie: Punktsymmetrie am Term über ungerade Exponenten begründen":
        "Symmetrie: Symmetrieart am Term über die Exponenten begründen",
    "Symmetrie: Achsensymmetrie am Term über gerade Exponenten begründen":
        "Symmetrie: Symmetrieart am Term über die Exponenten begründen",
}

NEUE_DEFINITION_2 = {
    "Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben":
        "Die Ergebnisse angeben, die zu Schnitt, Vereinigung oder Gegenereignis zweier beschriebener "
        "Ereignisse eines Zufallsexperiments gehören.",
    "Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen":
        "Die Lösungen von M · v = t · v für einen vorgegebenen Wert t (t = 1: Fixvektoren) als Vielfache "
        "eines Vektors angeben, oder einen einzelnen solchen Vektor ungleich null bestimmen.",
    "Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen":
        "Gleichheit oder Verhältnis der Wahrscheinlichkeiten zweier Ereignisse über die Anzahl ihrer "
        "gleich wahrscheinlichen Ergebnisse begründen.",
    "Symmetrie: Symmetrieart am Term über die Exponenten begründen":
        "Achsensymmetrie zur y-Achse oder Punktsymmetrie zum Ursprung damit begründen, dass der Term "
        "nur gerade bzw. nur ungerade Exponenten enthält.",
}

# ======================================================================= Lauf 3
# Drei Zusammenziehungen nach Kern § 6; zwei Definitionen um die neue Fundstelle erweitert.
ZUSAMMEN_3 = {
    "Matrizenalgebra: Bedingungen für die Vertauschbarkeit zweier Matrizen aus einer binomischen Gleichung untersuchen":
        "Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln",
    "Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln":
        "Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln",
    "Fläche: Fläche zwischen zwei Graphen mit vorgegebener Stammfunktion berechnen":
        "Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    "Fläche: Fläche zwischen zwei Graphen bis zu einer vorgegebenen Grenze berechnen":
        "Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    "Besondere Lage einer Ebene im Koordinatensystem beschreiben":
        "Lage einer Ebene zu einer Koordinatenachse aus der Koordinatengleichung begründen",
    "Parallelität einer Ebene zu einer Koordinatenachse über die Koordinatengleichung begründen":
        "Lage einer Ebene zu einer Koordinatenachse aus der Koordinatengleichung begründen",
}

NEUE_DEFINITION_3 = {
    "Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln":
        "Alle Matrizen B mit A · B = B · A für eine gegebene Matrix A ermitteln – die Bedingung kann auch "
        "aus einer binomischen Gleichung (A + B)² = A² + 2AB + B² folgen: allgemeiner Ansatz, Produkte "
        "vergleichen, Lösungsmenge mit freien Parametern.",
    "Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen":
        "Den Inhalt der Fläche zwischen zwei Graphen zwischen Schnittstellen oder bis zu einer vorgegebenen "
        "Grenze als Integral der Differenz berechnen; die Stammfunktion kann vorgegeben sein.",
    "Lage einer Ebene zu einer Koordinatenachse aus der Koordinatengleichung begründen":
        "Aus einer Koordinatengleichung ohne eine Variable die Lage der Ebene zu dieser Koordinatenachse "
        "begründen oder beschreiben (parallel; enthält die Achse, wenn zusätzlich das Absolutglied null ist).",
    "Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten":
        "Einen Eintrag der Übergangsmatrix oder eine Zahl des Übergangsdiagramms als Anteil oder Faktor "
        "eines Übergangs zwischen zwei Zuständen deuten.",
    "Matrizenalgebra: Erhalt der Spaltensumme unter einer stochastischen Matrix allgemein nachweisen":
        "Mit allgemeiner Matrix zeigen, dass eine stochastische Matrix die Komponentensumme eines Vektors "
        "erhält oder dass ihr Quadrat wieder stochastisch ist (Spaltensummen über a + c = 1, b + d = 1).",
}

# ======================================================================= Lauf 4
# Fünf Zusammenziehungen nach Kern § 6, eine Umbenennung (Name enger als die
# Definition), eine erweiterte Definition.
ZUSAMMEN_4 = {
    "Matrizenalgebra: Einträge der inversen Matrix mit Platzhaltern angeben":
        "Matrizenalgebra: Inverse Matrix über A · B = E bestimmen",
    "Matrizenalgebra: Inverse Matrix über ein Gleichungssystem aus A · B = E bestimmen":
        "Matrizenalgebra: Inverse Matrix über A · B = E bestimmen",
    "Wahrscheinlichkeit für mindestens einmal über das Gegenereignis im Baumdiagramm nachweisen":
        "Wahrscheinlichkeit für mindestens oder höchstens einmal bei zwei Stufen über das Gegenereignis berechnen",
    "Wahrscheinlichkeit für höchstens einmal bei zwei Zügen über das Gegenereignis berechnen":
        "Wahrscheinlichkeit für mindestens oder höchstens einmal bei zwei Stufen über das Gegenereignis berechnen",
    "Nullstellen und Werte: Nullstelle durch Einsetzen nachweisen":
        "Nullstellen und Werte: Nullstelle oder Schnittstelle mit einer waagerechten Geraden durch Einsetzen nachweisen",
    "Nullstellen und Werte: Schnittstelle mit einer waagerechten Geraden durch Einsetzen nachweisen":
        "Nullstellen und Werte: Nullstelle oder Schnittstelle mit einer waagerechten Geraden durch Einsetzen nachweisen",
    "Fläche: Fläche zwischen Graph und waagerechter Gerade über einem Intervall berechnen":
        "Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    "Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen":
        "Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    "Fläche: Steigung einer Ursprungsgeraden aus dem Flächeninhalt zwischen Parabel und Gerade bestimmen":
        "Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen Graph und Gerade bestimmen",
    "Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen zwei Graphen bestimmen":
        "Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen Graph und Gerade bestimmen",
    "Tangentensteigung an einer Nullstelle über die Ableitung nachweisen":
        "Tangentensteigung in einem Punkt über die Ableitung nachweisen",
}

NEUE_DEFINITION_4 = {
    "Matrizenalgebra: Inverse Matrix über A · B = E bestimmen":
        "Die Einträge der inversen Matrix über A · B = E bestimmen – Platzhalter einer vorgegebenen Form (auch "
        "über Kehrwerte) oder alle Einträge über das Gleichungssystem aus dem Produkt.",
    "Wahrscheinlichkeit für mindestens oder höchstens einmal bei zwei Stufen über das Gegenereignis berechnen":
        "In einem zweistufigen Experiment die Wahrscheinlichkeit für mindestens einmal oder höchstens einmal "
        "über das Gegenereignis (kein Treffer bzw. zweimal Treffer) berechnen oder nachweisen; die Stufen "
        "können eine Weiche haben.",
    "Nullstellen und Werte: Nullstelle oder Schnittstelle mit einer waagerechten Geraden durch Einsetzen nachweisen":
        "Durch Einsetzen zeigen, dass eine genannte Stelle Nullstelle ist oder dass der Graph dort eine "
        "waagerechte Gerade schneidet (Funktionswert berechnen und vergleichen).",
    "Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen":
        "Den Inhalt der Fläche zwischen zwei Graphen (auch Graph und waagerechte Gerade) zwischen "
        "Schnittstellen oder zwischen vorgegebenen senkrechten Grenzen als Integral der Differenz berechnen; "
        "die Stammfunktion kann vorgegeben sein.",
    "Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen Graph und Gerade bestimmen":
        "Den Parameter einer Geraden (Steigung oder Achsenabschnitt) so bestimmen, dass die mit einem Graphen "
        "eingeschlossene Fläche einen vorgegebenen Inhalt hat: Grenzen fest oder als Schnittstellen mit "
        "Parameter, Integral als Term im Parameter, Gleichung lösen.",
    "Ziehen ohne Zurücklegen: Kugelzahl aus einer Wahrscheinlichkeitsbedingung beim Umlegen einer Kugel bestimmen":
        "Eine unbekannte Kugelzahl bestimmen, indem eine Bedingung an die Behälter auf die Farben der "
        "umgelegten Kugeln (ein- oder mehrmaliges Umlegen) zurückgeführt und als Gleichung gelöst wird.",
}

# ======================================================================= Lauf 5
# Nach dem Probestapel Teil B (Auftrag des Lehrers): zwei erweiterte Definitionen,
# keine Zusammenziehung, keine Umbenennung. Dazu eine Feldkorrektur in bemerkung:
# die Markierung der Trägerbindung aus dem Probestapel wird auf den festen
# Wortlaut „Traegerbindung: Kontext" am Feldanfang gebracht (iqb.md § 7); die
# Markierung „frei" entfällt (kein Vermerk heißt frei).
ZUSAMMEN_5 = {}
NEUE_DEFINITION_5 = {
    "Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen":
        "Aus einer Von-nach-Tabelle oder der Übergangsmatrix das Übergangsdiagramm mit Schleifen und "
        "Pfeilen zeichnen.",
    "Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen":
        "Eine bedingte Wahrscheinlichkeit als Quotient aus dem Anteil des Schnitts und dem Anteil der "
        "Bedingung berechnen; die Anteile können im Text oder in einer Vierfeldertafel stehen.",
}
BEMERKUNG_5 = re.compile(r"\s*Trägerbindung: (frei|Kontext)( \([^)]*\))?\.")


def bemerkung_5(text):
    """Trägerbindung: „frei" streichen, „Kontext" mit fester Markierung an den Feldanfang."""
    m = BEMERKUNG_5.search(text)
    if not m:
        return text
    rest = text[:m.start()] + text[m.end():]
    if m.group(1) == "Kontext":
        return "Traegerbindung: Kontext" + (m.group(2) or "") + ". " + rest.lstrip()
    return rest


LAEUFE = {
    1: (PRAEFIX_1, ZUSAMMEN_1, NEUE_DEFINITION_1, NEUES_THEMA_1),
    2: ({}, ZUSAMMEN_2, NEUE_DEFINITION_2, {}),
    3: ({}, ZUSAMMEN_3, NEUE_DEFINITION_3, {}),
    4: ({}, ZUSAMMEN_4, NEUE_DEFINITION_4, {}),
    5: ({}, ZUSAMMEN_5, NEUE_DEFINITION_5, {}),
}
FELDKORREKTUR = {5: ("bemerkung", bemerkung_5)}
LAUF = int(sys.argv[1]) if len(sys.argv) > 1 else max(LAEUFE)
PRAEFIX, ZUSAMMEN, NEUE_DEFINITION, NEUES_THEMA = LAEUFE[LAUF]


def neu_name(alt):
    if alt in ZUSAMMEN:
        return ZUSAMMEN[alt]
    if alt in PRAEFIX:
        return f"{PRAEFIX[alt]}: {alt}"
    return alt


def lade(pfad):
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    return rows[0], rows[1:]


def schreibe(pfad, kopf, zeilen):
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(kopf)
        for z in zeilen:
            w.writerow(z)


def main():
    kopf_t, typen = lade(TYP)
    kopf_k, kat = lade(KAT)
    namen = [r[0] for r in typen]
    unbekannt = [a for a in list(PRAEFIX) + list(ZUSAMMEN) if a not in namen]
    if unbekannt:
        sys.exit(f"Typen nicht in {TYP}: {unbekannt}")
    abbildung = {n: neu_name(n) for n in namen}
    vorher = len(typen)

    # Typenliste: umbenennen, Zusammengezogenes nur einmal behalten
    neue_typen, gesehen = [], {}
    for r in typen:
        neu = abbildung[r[0]]
        if neu in gesehen:
            continue
        r = list(r)
        r[0] = neu
        if neu in NEUE_DEFINITION:
            r[3] = NEUE_DEFINITION[neu]
        if neu in NEUES_THEMA:
            r[1], r[2] = NEUES_THEMA[neu]
        gesehen[neu] = r
        neue_typen.append(r)

    # Katalog: beide Typfelder
    i_typ, i_neben = kopf_k.index("typ"), kopf_k.index("typ_neben")
    geaendert = 0
    for r in kat:
        for i in (i_typ, i_neben):
            teile = [abbildung.get(t, t) for t in r[i].split("|") if t]
            neu = "|".join(teile)
            if neu != r[i]:
                geaendert += 1
                r[i] = neu

    # Feldkorrektur (Lauf 5: Markierung der Trägerbindung in bemerkung)
    korrigiert = 0
    if LAUF in FELDKORREKTUR:
        feld, fn = FELDKORREKTUR[LAUF]
        i_feld = kopf_k.index(feld)
        for r in kat:
            neu = fn(r[i_feld])
            if neu != r[i_feld]:
                korrigiert += 1
                r[i_feld] = neu

    schreibe(TYP, kopf_t, neue_typen)
    schreibe(KAT, kopf_k, kat)

    # Bericht
    print(f"Abgleichlauf {LAUF}")
    print(f"Typen vorher {vorher}, nachher {len(neue_typen)}; {geaendert} Typfelder im Katalog geändert; "
          f"{len(kat)} Zeilen, {len(kat)/len(neue_typen):.2f} Zeilen je Typ."
          + (f" Feldkorrektur: {korrigiert} Zeilen." if korrigiert else ""))
    ziel = collections.defaultdict(list)
    for alt, neu in abbildung.items():
        if alt != neu:
            ziel[neu].append(alt)
    for neu in ziel:  # bestehender Name als Ziel einer Zusammenziehung
        if neu in namen and neu in ZUSAMMEN.values():
            ziel[neu].append(neu)
    print("\nZusammengezogen:")
    for neu, alte in ziel.items():
        if len(alte) > 1:
            print(f"  {' + '.join(alte)}\n    → {neu}")
    print("\nUmbenannt (Präfix oder neuer Name):")
    for neu, alte in ziel.items():
        if len(alte) == 1:
            print(f"  {alte[0]} → {neu}")


if __name__ == "__main__":
    main()
