# -*- coding: utf-8 -*-
"""iqb-abgleich.py – Abgleichlauf über die Typenliste des Profils iqb (Kern § 9).
Version 0.2 · 13.09.2026 · gilt mit iqb.md v0.6 und iqb-bau.py v0.4

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
"""
import csv, io, sys, collections
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

LAEUFE = {
    1: (PRAEFIX_1, ZUSAMMEN_1, NEUE_DEFINITION_1, NEUES_THEMA_1),
    2: ({}, ZUSAMMEN_2, NEUE_DEFINITION_2, {}),
}
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

    schreibe(TYP, kopf_t, neue_typen)
    schreibe(KAT, kopf_k, kat)

    # Bericht
    print(f"Abgleichlauf {LAUF}")
    print(f"Typen vorher {vorher}, nachher {len(neue_typen)}; {geaendert} Typfelder im Katalog geändert; "
          f"{len(kat)} Zeilen, {len(kat)/len(neue_typen):.2f} Zeilen je Typ.")
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
