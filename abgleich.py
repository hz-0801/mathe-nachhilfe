# -*- coding: utf-8 -*-
"""abgleich.py – Abgleichlauf über die gemeinsame Typenliste der Profile abi und iqb (Kern § 9).
Version 0.22 · 17.09.2026 · gilt mit abitur-vokabular.md v1.4, abi-bau.py v0.9 und iqb-bau.py v1.5
(bis Lauf 11 als iqb-abgleich.py nur für das Profil iqb)

Benennt Typen um und zieht Typen zusammen, in abitur-typen.csv und in beiden
Typfeldern aller Kataloge (KATALOGE: iqb-katalog.csv, abi-katalog.csv). Die
Regeln je Lauf stehen in LAEUFE: PRAEFIX (alt → Gegenstandsklasse), ZUSAMMEN
(alt → neu; mehrere alte Namen auf denselben neuen Namen heißt zusammenziehen,
die erste Zeile der Typenliste bleibt mit ihrer beispiel_id), NEUE_DEFINITION
und NEUES_THEMA (nur für zusammengezogene oder umgewidmete Typen). Aufruf
`python abgleich.py [N]` führt Lauf N aus (ohne Angabe den jüngsten); jeder
Lauf setzt den Stand nach dem vorigen voraus und wird genau einmal gefahren.
Schreibt die Dateien im Format der Bau-Skripte und gibt die Liste alt → neu
für abi-pruefungen.md bzw. iqb-pruefungen.md § 5 aus. Danach beide Bau-Skripte
mit leerem ZEILEN laufen lassen.

Lauf 1 (13.09.2026, Entscheidung 24): Gegenstandsklasse als Präfix nach
iqb.md § 6, neun Zusammenziehungen (183 → 174 Typen).
Lauf 2 (13.09.2026, nach 2022-ea-A): vier Zusammenziehungen (268 → 264).
Lauf 3 (14.09.2026, nach 2020-ea-A): drei Zusammenziehungen, zwei erweiterte
Definitionen (341 → 338).
Lauf 4 (14.09.2026, nach 2018-ea-A): fünf Zusammenziehungen, eine Umbenennung,
eine erweiterte Definition (406 → 401).
Lauf 5 (14.09.2026, nach dem Probestapel Teil B): zwei erweiterte Definitionen,
Feldkorrektur bemerkung (Markierung Traegerbindung), keine Zusammenziehung (433).
Lauf 6 (14.09.2026, nach vier Erfassungsstapeln Teil B): eine Zusammenziehung,
zwei erweiterte Definitionen (572 → 571).
Lauf 7 (14.09.2026, Vorarbeit „Teil B absichern"): zwei Zusammenziehungen mit
neuem Namen (Entscheidungsregel einseitig; Koordinatengleichung aus Punkten
oder Geraden), neues Thema Konfidenzintervalle für fünf Typen und ihre Zeilen
(Feldkorrektur thema und bemerkung), 571 → 569.
Lauf 8 (14.09.2026, nach 2024-ea-B, 2023-ga-B und 2026-ga-B-mms): zwei
Umbenennungen (Wendepunkt Zu- oder Abnahme; Symmetrieebene eines Körpers),
vier erweiterte Definitionen, keine Zusammenziehung (671).
Lauf 9 (15.09.2026, MMS als Delta): Bereinigung – Zeilen von Dateien mit
dublette_von in iqb-quellen.csv v0.3 gestrichen (17 Zeilen aus 2026-ga-B-mms),
STREICHEN als neue Regelart; Typen unverändert (671).
Lauf 10 (15.09.2026, nach 2023-ea-B und 2022-ea-B): eine Zusammenziehung mit
neuem Namen (Grenze k gegen eine Schranke), 774 → 773.
Lauf 11 (15.09.2026, nach 2026-ea-B-mms): zwei Zusammenziehungen mit neuem
Namen (Quaderhöhe aus den Raumdiagonalen mit Volumen oder Oberflächeninhalt;
Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion),
794 → 792.
Lauf 12 (15.09.2026, Entscheidung 25 – Umstellungslauf): iqb-typen.csv (792)
und abi-typen.csv (146) werden zu abitur-typen.csv zusammengeführt; 50 abi-Typen
gehen in ihr inhaltsgleiches iqb-Gegenstück auf, 2 tragen denselben Namen,
11 überlappende Paare werden mit erweiterter Definition zusammengezogen
(drei iqb-Typen dabei umbenannt), 15 abi-Typen in Klassen-Themen bekommen
den Präfix, 2 wechseln das Thema; beide Kataloge werden umetikettiert
(abi-iqb-typen.md, Bericht in abi-pruefungen.md § 4). Die Quelldateien
iqb-typen.csv und abi-typen.csv entfallen.
Lauf 13 (16.09.2026, Themenfeld bereinigen): Zeilenthema = Typthema. Ein
Präfix (Term und Ereignis), drei Themenwechsel von Typen, Feldkorrektur
leitidee/thema in 21 Zeilen plus Vermerke und ein doppeltes typ_neben; Typen
unverändert (875). Seitdem prüft jeder Lauf, dass keine Zeile vom Thema ihres
Typs abweicht.
Lauf 14 (16.09.2026, Pool-Abgleich des abi-Bestands bis 2018): Vermerk
„Poolaufgabe (nicht erfasst): <Kennung>" in 15 wortgleichen und
„(nicht erfasst, abgewandelt)" in 2 abgewandelten Zeilen (Feldkorrektur
bemerkung); Typen unverändert (913).
Lauf 15 (16.09.2026, Verweise schließen nach den Reserve-Stapeln 2017-ea-A,
2018-ga-B, 2018-ea-B): die 17 Vermerke aus Lauf 14 werden zu Verweisen –
15 wortgleiche auf „Dublette von: <id>." (mit der AB-Spalte der Poolzeile in
bemerkung; afb_amtlich bleibt bei Heften bis 2018 leer), die abgewandelte 2018-be-gk 3.2 a auf „Abgewandelt von: <id>;
<Unterschied>."; 3.2 e und g zeigen jetzt auf den wortgleichen grundlegenden
Pool statt auf den erhöhten. Typvergleich je Paar (alle 17 gleich), Abbruch
bei einem Unterschied oder bei mehr als 17 angefassten Zeilen; Typen
unverändert (990).
Lauf 16 (16.09.2026, Reste schließen): 2018-be-gk 3.2 f → „Dublette von:"
Stochastik WTR 2 f; fünf Teil-B-Zeilen von 2018-be-gk (2.2 a, b, 3.2 b, c, d)
in niveau_geschaetzt auf die enge Fassung nachgezogen (Wert der wortgleichen
Poolzeile); Typen unverändert (1006).
Lauf 17 (16.09.2026, Abgleich nach den vier Stark-Heften 2022-bebb-gk,
2025-bebb-gk, 2022-bebb-lk, 2023-bebb-lk): drei Zusammenziehungen mit neuem
Namen – Steckbriefaufgabe dritten Grades (Bedingungsarten stehen in der
Zeile), Rekonstruktion aus knickfreiem Übergang (quadratisch oder mit zwei
Parametern), Fehler zweiter Art für selbst gewählte Anteile (Schranke oder
Deutung); 1090 → 1087.
Lauf 18 (17.09.2026, Verweise schließen nach dem Reserve-Stapel 2022-ga-B):
die 19 Vermerke von 2022-bebb-gk werden zu Verweisen – 16 wortgleiche auf
„Dublette von: <id>." (AB-Spalte der Poolzeile in afb_amtlich und bemerkung),
3 abgewandelte (2.1 m, 3 g, 4 j) auf „Abgewandelt von: <id>; <Unterschied>.".
Typvergleich je wortgleichem Paar, Abbruch bei Abweichung oder mehr als 19
Zeilen; Typen unverändert (1115).
Lauf 19 (17.09.2026, Abgleich nach dem Stapel 2022-ga-B und den Heften
2026-bb-gk, 2026-bb-ea): drei Zusammenziehungen mit neuem Namen –
Näherungswert eines Integrals als Vielecksfläche (Dreieck 2025-ga-B, Trapez
2022-ga-B), Produkt aus Potenz und Binomialterm als Ereignis mit festem
Abschnitt (Endstück 2022-bebb-lk, Anfangsstück mit kumulierter Summe
2022-ga-B), passenden Graphen zu einem Term auswählen (ausschließen 2021-ga-A,
auswählen 2022-ga-B); 1127 → 1124.
Lauf 20 (17.09.2026, Auftrag „Eichung korrigieren, Prüfungsgeschichte und
Prüfungsstruktur festhalten, Heftordner ordnen", Teil 1 – Vorrang des
Amtlichen, Kern § 5): Feldkorrektur niveau_geschaetzt in 20 Zeilen – die neun
Poolzeilen von 2022-ga-B, deren aus der Landeszeile übernommene Schätzung
neben der Spalte Anforderungsbereich lag, auf den amtlichen Bereich; elf
wortgleiche Landeszeilen, die vor ihrer Poolzeile geschätzt wurden und vom
amtlichen Bereich abweichen (2022-bebb-gk 7, 2017-bb-ea 2, 2018-bb-ea 2),
nachgezogen. Grund je Zeile in bemerkung, alter Wert bleibt dort. Abbruch bei
mehr als 20 Zeilen oder wenn ein Zielwert nicht der amtliche ist. Typen
unverändert (1124).
Lauf 21 (17.09.2026, Auftrag B Teil 1 – Abgleich nach den fünf Stark-Heften
2019-be-gk, 2020-be-gk, 2021-be-gk, 2024-bebb-lk, 2025-bebb-lk): vier
Zusammenziehungen – Maximum einer ganzrationalen Modellfunktion (Gewinnfunktion
2018-ga-B ist ein Sonderfall), Stellen mit waagerechter Tangente aus der
faktorisierten Ableitung (mögliche Extremstellen 2024-bebb-lk), mindestens oder
höchstens einmal über das Gegenereignis bei zwei oder drei Stufen (spätestens
dritter Erfolg 2020-be-gk), quadratische Steckbriefaufgabe aus Wert- und
Steigungsbedingungen (wie Lauf 17 für dritten Grad); 1215 → 1211.
Lauf 22 (17.09.2026, Auftrag C Teil 0 – Maßstab der Schätzung, Kern § 5
v0.7): Feldkorrektur afb_amtlich in den 21 Dubletten der Hefte bis 2018
(2017-bb-ea und 2018-bb-ea Teil A aus dem Bereichswert der Poolzeile,
2018-be-gk Teil B aus der AB-Spalte), damit „afb_amtlich leer" im ganzen
Bestand „Schätzung ohne Maßstab" heißt; Typen unverändert (1211).
"""
import csv, io, os, re, sys, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

TYP = "abitur-typen.csv"
KATALOGE = ["iqb-katalog.csv", "abi-katalog.csv"]  # in dieser Reihenfolge, nur vorhandene
# Lauf 12 liest die beiden alten Listen und schreibt erstmals abitur-typen.csv (iqb zuerst:
# bei gleichem oder zusammengezogenem Namen bleibt der iqb-Eintrag mit seiner beispiel_id).
QUELL_TYPEN_12 = ["iqb-typen.csv", "abi-typen.csv"]

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


# ======================================================================= Lauf 6
# Nach den vier Erfassungsstapeln Teil B (2026-ea, 2025-ga, 2025-ea, 2024-ga, WTR):
# eine Zusammenziehung (der neue Fixvektor-Typ aus 2025-ga-B deckt dieselbe
# Fertigkeit wie der Teil-A-Typ 328, der bestehende Name bleibt), eine erweiterte
# Definition. Offen, weil Umbenennung: Entscheidungsregel links-/rechtsseitig zu
# „einseitig" zusammenziehen; Koordinatengleichung durch drei Punkte gegen durch
# zwei sich schneidende Geraden (seit Lauf 5 offen).
ZUSAMMEN_6 = {
    "Übergangsprozess: Matrixeintrag aus einem beobachteten Fixvektor bestimmen":
        "Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen",
}
NEUE_DEFINITION_6 = {
    "Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen":
        "Aus der Bedingung M · v = v mit teilweise bekanntem Vektor v unbekannte Einträge der Übergangsmatrix "
        "und fehlende Komponenten des Bestands bestimmen (Gleichungssystem).",
    "Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen":
        "Prüfen, ob zwei Ereignisse stochastisch unabhängig sind: über P(A ∩ B) = P(A) · P(B) oder "
        "gleichwertig über den Vergleich einer bedingten mit der unbedingten Wahrscheinlichkeit.",
}

# ======================================================================= Lauf 7
# Vorarbeit zum Auftrag „Teil B absichern" (Entscheidungen des Lehrers, 14.09.2026):
# die beiden bisher offenen Umbenennungen ausführen (Entscheidungsregel
# einseitig; Koordinatengleichung aus Punkten oder Geraden), und das neue Thema
# Konfidenzintervalle (iqb.md § 6) an die fünf bisher ersatzweise unter
# Hypothesentests geführten Typen und ihre Zeilen geben.
ZUSAMMEN_7 = {
    "Entscheidungsregel eines linksseitigen Signifikanztests bestimmen":
        "Entscheidungsregel eines einseitigen Signifikanztests bestimmen",
    "Entscheidungsregel eines rechtsseitigen Signifikanztests bestimmen":
        "Entscheidungsregel eines einseitigen Signifikanztests bestimmen",
    "Koordinatengleichung einer Ebene durch drei Punkte bestimmen":
        "Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen",
    "Koordinatengleichung der Ebene durch zwei sich schneidende Geraden bestimmen":
        "Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen",
}
NEUE_DEFINITION_7 = {
    "Entscheidungsregel eines einseitigen Signifikanztests bestimmen":
        "Für eine einseitige Nullhypothese (p ≤ p0 oder p ≥ p0) die Entscheidungsregel bestimmen: die "
        "Grenze des Ablehnungsbereichs über kumulierte Binomialwahrscheinlichkeiten so wählen, dass die "
        "Irrtumswahrscheinlichkeit das Signifikanzniveau nicht überschreitet; die Richtung steht in der Zeile.",
    "Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen":
        "Die Koordinatengleichung einer Ebene bestimmen, die durch drei Punkte oder durch zwei sich "
        "schneidende Geraden gegeben ist: Normalenvektor aus zwei Richtungsvektoren (Skalarprodukte oder "
        "Ansatz mit Einsetzen), Konstante aus einem Punkt.",
}
KONFIDENZ_TYPEN = [
    "Konfidenzintervall aus dem Diagramm identifizieren und Stichprobenergebnis aus der Grenze berechnen",
    "Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben",
    "Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen",
    "Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen",
    "Verträglichkeit zweier Annahmen mit demselben Stichprobenanteil über den Stichprobenumfang beurteilen",
]
NEUES_THEMA_7 = {t: ("Stochastik", "Konfidenzintervalle") for t in KONFIDENZ_TYPEN}
ERSATZ_7 = re.compile(r"\s*Thema ersatzweise Hypothesentests( \(Konfidenzintervalle haben keine Themenzeile\))?\.")


def zeile_7(d):
    """Zeilen der Konfidenzintervall-Typen auf das neue Thema umstellen, Vermerk „ersatzweise" streichen."""
    if d["typ"] not in KONFIDENZ_TYPEN:
        return False
    d["thema"] = "Konfidenzintervalle"
    d["bemerkung"] = ERSATZ_7.sub("", d["bemerkung"]).strip()
    return True


# ======================================================================= Lauf 8
# Nach den drei Stapeln des Auftrags „Teil B absichern, MMS-Delta messen"
# (2024-ea-B, 2023-ga-B, 2026-ga-B-mms): zwei Umbenennungen, bei denen das
# Etikett enger war als die Fertigkeit (Zu- oder Abnahme; Körper statt
# Pyramide, Definitionen mitgezogen), zwei erweiterte Definitionen um die
# neuen Fundstellen (Tabelle statt Graph; bedingter Anteil). Keine
# Zusammenziehung.
ZUSAMMEN_8 = {
    "Wendepunkt als Zeitpunkt stärkster Abnahme im Sachzusammenhang deuten":
        "Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten",
    "Symmetrieebene einer Pyramide unter vorgegebenen Gleichungen auswählen und eine ausschließen":
        "Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen",
}
NEUE_DEFINITION_8 = {
    "Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten":
        "Die Bedeutung eines Wendepunkts als Zeitpunkt der stärksten Zunahme (steigender Bereich) oder "
        "der stärksten Abnahme (fallender Bereich) einer Größe im Sachzusammenhang beschreiben; die "
        "Wendestelle ist gegeben oder wird abgelesen.",
    "Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen":
        "Unter mehreren Ebenengleichungen die Symmetrieebene eines Körpers (Pyramide, Quader) auswählen "
        "und für eine andere über eine Punktprobe oder einen Kantenmittelpunkt begründen, dass sie keine ist.",
    "Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen":
        "Für ein Zeitintervall die Werte am Graphen ablesen oder aus einer Tabelle entnehmen und den "
        "Differenzenquotienten als Durchschnitt je Zeiteinheit berechnen.",
    "Vierfeldertafel aus Anteilen vervollständigen":
        "Aus zwei Randanteilen und einem Schnittanteil – oder einem Randanteil und einem bedingten Anteil, "
        "aus dem der Schnittanteil folgt – alle Felder einer Vierfeldertafel ergänzen.",
}

# ======================================================================= Lauf 9
# Bereinigung (Entscheidung des Lehrers, 15.09.2026: MMS als Delta): Zeilen von
# Dateien, die in iqb-quellen.csv (v0.3, Textvergleich Teil B) als Dublette einer
# WTR-Datei stehen, werden gestrichen – die 17 aus dem WTR-Zweig übernommenen
# Zeilen des Stapels 2026-ga-B-mms. Keine Umbenennung, keine Definition.
QUELLEN = "iqb-quellen.csv"


def dubletten_quellen():
    with io.open(QUELLEN, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter=";"))
    return {r["kennung"]: r["dublette_von"] for r in rows if r["dublette_von"]}


def streiche_9(d, dubl=dubletten_quellen()):
    """True, wenn die Zeile zu einer Datei mit dublette_von gehört."""
    return d["id"].split("-")[0] in dubl


# ======================================================================= Lauf 10
# Nach 2023-ea-B und 2022-ea-B (Auftrag „Erhöhtes Niveau absichern"): eine
# Zusammenziehung mit neuem Namen – kleinstes k über der Schranke (2025-ga-B)
# und größtes k unter der Schranke (2022-ea-B) sind dieselbe Fertigkeit
# (Grenze am Rechner mit Nachbarwerten, Richtung steht in der Zeile).
ZUSAMMEN_10 = {
    "Kleinstes k mit kumulierter Wahrscheinlichkeit über einer Schranke mit dem Rechner ermitteln":
        "Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln",
    "Größtes k mit kumulierter Wahrscheinlichkeit unter einer Schranke mit dem Rechner ermitteln":
        "Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln",
}
NEUE_DEFINITION_10 = {
    "Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln":
        "Das kleinste bzw. größte k ermitteln, für das P(X ≤ k) oder P(X < k) eine vorgegebene Schranke "
        "über- bzw. unterschreitet, mit beiden Nachbarwerten am Rechner; die Richtung steht in der Zeile.",
}

# ======================================================================= Lauf 11
# Nach 2026-ea-B-mms (Auftrag „Teil B schließen, Rechnerfassung klären"): zwei
# Zusammenziehungen mit neuem Namen. (1) Höhe eines Quaders aus der
# Orthogonalität der Raumdiagonalen – WTR-Fassung fragt das Volumen, MMS-Fassung
# den Oberflächeninhalt, dieselbe Fertigkeit; (2) Zeitpunkt der größten Rate
# über die Ableitung der Ratenfunktion – bei gegebenem Bestand ist das die
# zweite Ableitung (2026-ga-B-mms), bei gegebener Rate die erste (2026-ea-B-mms
# zweimal, einmal nur der Zeitpunkt); die Größe der Rate ist ein Ablesen mehr.
ZUSAMMEN_11 = {
    "Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen berechnen":
        "Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen oder Oberflächeninhalt berechnen",
    "Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Oberflächeninhalt berechnen":
        "Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen oder Oberflächeninhalt berechnen",
    "Zeitpunkt und Größe der maximalen Änderungsrate über die zweite Ableitung berechnen":
        "Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion berechnen",
    "Zeitpunkt der maximalen Rate über die Ableitung der Ratenfunktion berechnen":
        "Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion berechnen",
}
NEUE_DEFINITION_11 = {
    "Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen oder Oberflächeninhalt berechnen":
        "Die unbekannte Höhe eines Quaders aus dem verschwindenden Skalarprodukt zweier Raumdiagonalen bestimmen und "
        "daraus das Volumen oder den Oberflächeninhalt berechnen; welches Maß, steht in der Zeile.",
    "Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion berechnen":
        "Die Stelle der größten Rate als Nullstelle der Ableitung der Ratenfunktion berechnen (ist der Bestand gegeben, "
        "der zweiten Ableitung), Randstellen prüfen und, wenn verlangt, den Wert der Rate dort angeben.",
}

# ======================================================================= Lauf 12
# Umstellungslauf (Entscheidung 25, 15.09.2026): gemeinsame Typenliste für abi
# und iqb. Zuordnung je abi-Typ und Begründung in abi-iqb-typen.md § 6; die
# (b)-Zusammenziehungen M1–M11 und die vier Klassenentscheidungen im Bericht
# (abi-pruefungen.md § 4, 15.09.2026).
ZUSAMMEN_12 = {
    # (a) inhaltsgleich: abi-Name → iqb-Name (abi-iqb-typen.md § 6)
    "Unterschreiten einer Steigungsschranke über das Minimum der Ableitung nachweisen":
        "Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen",
    "Ableitung mit Produkt- und Kettenregel bilden":
        "Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden",
    "Zweite Ableitung nachweisen":
        "Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen",
    "Zielfunktion für den Flächeninhalt eines Dreiecks aufstellen":
        "Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen",
    "Fläche zwischen zwei Graphen berechnen":
        "Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    "Achsensymmetrie am Funktionsterm nachweisen":
        "Symmetrie: Symmetrieart am Term über die Exponenten begründen",
    "Nullstellenfreiheit über das Vorzeichen des Funktionsterms begründen":
        "Nullstellen und Werte: Nullstellenfreiheit und Wertemenge einer e-Funktion aus dem Term begründen",
    "Parameter einer Parallelen zur x-Achse aus einer Abstandsbedingung berechnen":
        "Symmetrie: Höhe einer waagerechten Sekante aus dem Abstand ihrer Schnittpunkte über die Symmetrie bestimmen",
    "Punktsymmetrie am Funktionsterm begründen":
        "Symmetrie: Symmetrieart am Term über die Exponenten begründen",
    "Schnittpunkt mit der y-Achse angeben":
        "Nullstellen und Werte: Schnittpunkt mit der y-Achse und Steigung des Graphen dort angeben",
    "Gemeinsamen Punkt aller Graphen einer Schar nachweisen":
        "Gemeinsame Punkte aller Graphen einer Schar bestimmen",
    "Parameterwert aus dem Graphen einer Schar ermitteln":
        "Scharparameter aus einem Punkt des Graphen angeben",
    "Punkt in vorgegebener Entfernung auf einer Geraden bestimmen":
        "Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen",
    "Grenzverhalten einer Exponentialfunktion untersuchen":
        "Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben",
    "Art eines Extrempunktes über die zweite Ableitung bestimmen":
        "Extrempunkt an vorgegebener Stelle nachweisen",
    "Fehlen von Extrempunkten einer Schar über die Diskriminante nachweisen":
        "Parameterwerte nach der Anzahl der Extrempunkte über die Lösbarkeit der Extremstellengleichung begründen",
    "Fehlen von Extrempunkten über das Vorzeichen der Ableitung begründen":
        "Fehlende Extrempunkte über eine positive Ableitung begründen",
    "Hochpunkt über die notwendige Bedingung bestimmen":
        "Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen",
    "Stelle des stärksten Gefälles über die zweite Ableitung bestimmen":
        "Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen",
    "Parameter einer Exponentialfunktion aus zwei Wertepaaren bestimmen":
        "Parameter einer Exponentialfunktion aus zwei Punkten des Graphen bestimmen",
    "Gleichschenkligkeit des Achsenabschnittsdreiecks einer Tangente nachweisen":
        "Gleichschenkligkeit des Dreiecks aus Tangente und Koordinatenachsen allgemein begründen",
    "Normalengleichung an einer Stelle ermitteln":
        "Gerade senkrecht zu einer gegebenen Tangente durch einen Punkt aufstellen",
    "Relative Abweichung zweier Funktionswerte prüfen":
        "Näherung durch die Tangente mit dem Funktionswert im Sachzusammenhang vergleichen",
    "Tangente aus einer Bedingung an das Achsenabschnittsdreieck bestimmen":
        "Berührpunkt der Tangente mit gleichschenkligem Achsendreieck über die Steigung −1 berechnen",
    "Tangentengleichung an einer Stelle ermitteln":
        "Tangentengleichung in einem Punkt des Graphen aufstellen",
    "Koordinatengleichung einer Ebene aus drei Punkten aufstellen":
        "Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen",
    "Trägerebene über Normalenvektor begründen":
        "Lage einer Figur in einer Koordinatenebene aus Eckpunkt und orthogonaler Geraden begründen",
    "Lage eines durch eine Linearkombination gegebenen Punktes beschreiben":
        "Lage eines Punktes zu einem Vektorterm im Quader beschreiben",
    "Rechtwinkligkeit eines Dreiecks über Skalarprodukte ausschließen":
        "Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen",
    "Geschwindigkeit aus Weg und Zeit berechnen und in Kilometer pro Stunde umrechnen":
        "Körper: Geschwindigkeit entlang einer Kante aus Kantenlänge und Zeit berechnen",
    "Koordinaten der Eckpunkte einer Pyramide aus der Beschreibung angeben":
        "Körper: Koordinaten der Eckpunkte eines beschriebenen Körpers wählen",
    "Trapezform eines Vierecks im Raum nachweisen":
        "Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen",
    "Durchstoßpunkt einer Geraden durch eine Ebene bestimmen":
        "Schnittpunkt von Gerade und Ebene berechnen",
    "Gesamthöhe eines zusammengesetzten Körpers über die Spitze bestimmen":
        "Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen",
    "Innenwinkel eines Dreiecks über das Skalarprodukt berechnen":
        "Winkel zwischen zwei Kanten über das Skalarprodukt berechnen",
    "Schnittwinkel zweier Ebenen über die Normalenvektoren berechnen":
        "Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen",
    "Schnittwinkel zwischen Gerade und Ebene berechnen":
        "Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen",
    "Totale Wahrscheinlichkeit bei zufälliger Auswahl einer Urne berechnen":
        "Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen",
    "Wahrscheinlichkeit einer festgelegten Trefferfolge berechnen":
        "Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen",
    "Anteil einer Teilgruppe aus der totalen Wahrscheinlichkeit berechnen":
        "Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen",
    "Bedingte Wahrscheinlichkeit aus der Vierfeldertafel berechnen":
        "Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen",
    "Kumulierte Wahrscheinlichkeit einer Binomialverteilung berechnen":
        "Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    "Wahrscheinlichkeit einer Binomialverteilung für genau k Treffer berechnen":
        "Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    "Auszahlung eines fairen Spiels aus der Fairnessbedingung bestimmen":
        "Unbekannte Größe aus einer Erwartungswertbedingung bestimmen",
    "Vierfeldertafel aus Anteilen aufstellen":
        "Vierfeldertafel aus Anteilen vervollständigen",
    "Anzahl der Kugeln aus einer Fairnessbedingung bestimmen":
        "Unbekannte Größe aus einer Erwartungswertbedingung bestimmen",
    "Wahrscheinlichkeit beim Ziehen ohne Zurücklegen mit der Pfadregel nachweisen":
        "Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen",
    "Punktprobe an einer Ebenengleichung durchführen":
        "Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen",
    "Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben":
        "Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben",
    "Entscheidungsregel für einen einseitigen Signifikanztest bestimmen":
        "Entscheidungsregel eines einseitigen Signifikanztests bestimmen",
    # (b) zusammengezogen, Definition erweitert (M1–M11 im Bericht)
    "Parameterwert einer Schar aus einer Funktionswertbedingung exakt bestimmen":
        "Scharparameter aus einem Punkt des Graphen angeben",
    "Art eines Extrempunktes über den Vorzeichenwechsel der ersten Ableitung begründen":
        "Extrempunkt an vorgegebener Stelle nachweisen",
    "Parabelgleichung aus Symmetrie und einer Flächenbedingung rekonstruieren":
        "Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen",
    "Flächeninhalt des Achsenabschnittsdreiecks einer Tangente berechnen":
        "Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen",
    "Lage eines Punktes auf einer Strecke über die Parameterform nachweisen":
        "Punktprobe an einer Geraden durchführen",
    "Mittelpunkt eines Quadrates als Diagonalenmittelpunkt bestimmen":
        "Punkt: Mittelpunkt einer Strecke im Raum bestimmen",
    "Wahrscheinlichkeit eines Intervalls als Differenz kumulierter Werte berechnen":
        "Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    "Wahrscheinlichkeit aus den Sektorwinkeln eines Glücksrads bestimmen":
        "Laplace-Experiment: Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben",
    "Wahrscheinlichkeit für den ersten Treffer bei der k-ten Wiederholung berechnen":
        "Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen",
    "Punktprobe mit gerundeten Koordinaten durchführen":
        "Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen",
    "Eckpunkt eines Quadrates nachweisen":
        "Ebene Figur: Benachbarte Ecke eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen",
    # Umbenennungen bestehender iqb-Typen (Ziel der Zusammenziehung)
    "Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen":
        "Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen",
    "Laplace-Experiment: Laplace-Wahrscheinlichkeit für den ersten Zug angeben":
        "Laplace-Experiment: Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben",
    "Nullstellen und Werte: Nullstelle oder Schnittstelle mit einer waagerechten Geraden durch Einsetzen nachweisen":
        "Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen",
}
PRAEFIX_12 = {
    "Definitionsbereich einer Logarithmusfunktion angeben": "Nullstellen und Werte",
    "Einzige Nullstelle über den positiven Exponentialfaktor nachweisen": "Nullstellen und Werte",
    "Vertikalen Abstand zweier Punkte als Differenz von Funktionswerten berechnen": "Nullstellen und Werte",
    "Abschnittsweise begrenzte Fläche durch Integration berechnen": "Fläche",
    "Flächenmaßstab eines Modells auf eine Realfläche anwenden": "Fläche",
    "Körper in ein räumliches Koordinatensystem einzeichnen": "Körper",
    "Mittelpunkt einer Strecke im Raum bestimmen": "Punkt",
    "Schatten einer Fläche in eine Abbildung einzeichnen": "Ebene Figur",
    "Orthogonalität zweier Ebenen über die Normalenvektoren nachweisen": "Geraden und Ebenen",
    "Bedarfsgröße aus einem Volumen im Sachzusammenhang nachweisen": "Körper",
    "Flächeninhalt eines Dreiecks aus den Spurpunkten einer Ebene berechnen": "Ebene Figur",
    "Höhe eines Dreiecks im Raum über den Flächeninhalt berechnen": "Ebene Figur",
    "Pyramidenvolumen aus Grundfläche und Höhe berechnen": "Körper",
    "Mindestanzahl beim Ziehen ohne Zurücklegen über das Gegenereignis bestimmen": "Ziehen ohne Zurücklegen",
    "Sektorenzahlen eines Glücksrads aus Wahrscheinlichkeiten ermitteln": "Laplace-Experiment",
}
NEUES_THEMA_12 = {
    "Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen": ("Analysis", "Kurvenuntersuchung"),
    "Existenz eines Geradenschnittpunkts über die gemeinsame Ebene begründen": ("Analytische Geometrie", "Geraden"),
}
NEUE_DEFINITION_12 = {
    # (a)-Ziele, deren Definition den abi-Fall noch nicht nannte
    "Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden":
        "Die Ableitung eines Terms p(x) · e^(g(x)) (p Polynom, auch nur x) mit Produkt- und Kettenregel "
        "bilden und den gemeinsamen Faktor ausklammern.",
    "Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen":
        "Eine vorgegebene erste oder zweite Ableitung eines Produkts aus Potenz oder Polynom und e-Funktion "
        "mit Produkt- und Kettenregel nachweisen und in die vorgegebene Form bringen.",
    "Symmetrie: Symmetrieart am Term über die Exponenten begründen":
        "Achsensymmetrie zur y-Achse oder Punktsymmetrie zum Ursprung begründen – über die Parität der "
        "Exponenten oder über f(−x) = f(x) bzw. f(−x) = −f(x).",
    "Nullstellen und Werte: Nullstellenfreiheit und Wertemenge einer e-Funktion aus dem Term begründen":
        "Am Term begründen, dass eine Funktion (etwa a · e^x + c oder eine Summe stets positiver Bestandteile) "
        "keine Nullstelle hat, und, wenn verlangt, ihre Wertemenge angeben.",
    "Nullstellen und Werte: Schnittpunkt mit der y-Achse und Steigung des Graphen dort angeben":
        "Den Schnittpunkt eines Graphen mit der y-Achse als (0 | f(0)) angeben und, wenn verlangt, die "
        "Steigung dort als f'(0).",
    "Gerade senkrecht zu einer gegebenen Tangente durch einen Punkt aufstellen":
        "Die Gleichung der Normalen in einem Graphenpunkt (Steigung −1/f'(x₀)) oder einer Geraden durch einen "
        "Punkt senkrecht zu einer gegebenen Tangente aufstellen.",
    "Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen":
        "Ein Viereck über kollineare Verbindungsvektoren zweier Seiten als Trapez nachweisen und, wenn "
        "verlangt, seinen Flächeninhalt mit der Trapezformel berechnen.",
    "Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen":
        "Eine Wahrscheinlichkeit berechnen, wenn erst die Urne oder ihre Zusammensetzung zufällig gewählt wird "
        "und dann daraus gezogen wird: bedingte Wahrscheinlichkeiten je Fall gewichtet addieren (totale Wahrscheinlichkeit).",
    "Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen":
        "Den Hochpunkt eines Produkts aus Polynom und e-Funktion über die notwendige Bedingung berechnen "
        "(Produktregel); die Art folgt aus der Abbildung oder dem Sachzusammenhang, die hinreichende Bedingung entfällt.",
    # (b)-Zusammenziehungen M1–M11
    "Scharparameter aus einem Punkt des Graphen angeben":
        "Den Parameterwert einer Funktionsschar angeben oder durch exaktes Auflösen bestimmen, für den ein "
        "gegebener Punkt auf dem Graphen liegt oder ein Funktionswert eine Bedingung erfüllt.",
    "Extrempunkt an vorgegebener Stelle nachweisen":
        "Für eine genannte Stelle zeigen, dass dort ein Hoch- oder Tiefpunkt liegt: erste Ableitung null "
        "(notwendige Bedingung) und Art über das Vorzeichen der zweiten Ableitung oder über den "
        "Vorzeichenwechsel der ersten Ableitung.",
    "Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen":
        "Zwei Parameter einer Schar oder einer symmetrisch angesetzten Parabel aus einer vorgegebenen "
        "Nullstelle und dem Inhalt eines Flächenstücks zwischen Graph und x-Achse bestimmen.",
    "Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen":
        "Die Tangente in einem Punkt aufstellen, ihre Achsenabschnitte bestimmen und daraus den Flächeninhalt "
        "oder den Umfang (Satz des Pythagoras) des von Tangente und Koordinatenachsen begrenzten Dreiecks "
        "berechnen; welches Maß, steht in der Zeile.",
    "Punktprobe an einer Geraden durchführen":
        "Prüfen, ob ein Punkt auf einer Geraden in Parameterform liegt, indem der Parameter aus den Koordinaten "
        "bestimmt und auf Widerspruch geprüft wird; bei einer Strecke zusätzlich, ob der Parameter zwischen "
        "null und eins liegt.",
    "Punkt: Mittelpunkt einer Strecke im Raum bestimmen":
        "Den Mittelpunkt einer Strecke – auch einer Diagonalen eines Vierecks, also den Mittelpunkt der Figur – "
        "als halbe Summe der Ortsvektoren der Endpunkte berechnen.",
    "Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln":
        "Eine kumulierte Wahrscheinlichkeit einer Binomialverteilung (weniger als, mehr als, höchstens, "
        "mindestens) mit dem Rechner oder aus der Tabelle ermitteln; „mehr als“ über das Gegenereignis, ein "
        "Intervall als Differenz zweier kumulierter Werte mit richtig eingeschlossenen Grenzen.",
    "Laplace-Experiment: Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben":
        "Die Wahrscheinlichkeit eines Ergebnisses als Anteil der günstigen an allen gleich wahrscheinlichen "
        "Fällen angeben – Objekte beim ersten Ziehen oder Sektorwinkel am Vollwinkel beim Glücksrad.",
    "Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen":
        "Die Wahrscheinlichkeit einer in fester Reihenfolge vorgegebenen Folge von Ergebnissen als Produkt "
        "der Einzelwahrscheinlichkeiten berechnen, etwa erster Treffer erst beim k-ten Versuch.",
    "Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen":
        "Durch Einsetzen zeigen, dass ein Punkt (auch mit gerundeten Koordinaten) auf dem Graphen liegt, dass "
        "eine Stelle Nullstelle ist oder dass der Graph dort eine waagerechte Gerade schneidet.",
    "Ebene Figur: Benachbarte Ecke eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen":
        "Nachweisen, dass ein Punkt eine zu einer gegebenen Ecke benachbarte Ecke eines Quadrats ist: "
        "Diagonalenschnittpunkt als Spurpunkt einer Geraden bestimmen, gleiche Länge und Orthogonalität der "
        "Halbdiagonalen zeigen (schließt den gegenüberliegenden Eckpunkt aus).",
}

# Pool-Teilaufgaben in Landesheften (Entscheidung des Lehrers, 15.09.2026, Punkt 3):
# eigene abi-Zeile mit geteiltem Typ, Verweis „Dublette von: <iqb-id>" am Anfang
# von bemerkung. Der hilfsmittelfreie Teil 2018-bb-ea nimmt Analysis 2 und AG/LA
# A2 2 des Pools 2018 erhöht (gleiche Zahlen und Aufträge; 2017 nicht prüfbar,
# Pool 2017 erhöht A ist Reserve).
DUBLETTEN_12 = {
    "2018-bb-ea-A1.1a": "2018MerhoehtAAnalysis2-a", "2018-bb-ea-A1.1b": "2018MerhoehtAAnalysis2-b",
    "2018-bb-ea-A1.2a": "2018MerhoehtAAGLAA22-a", "2018-bb-ea-A1.2b": "2018MerhoehtAAGLAA22-b",
}


def zeile_12(d):
    """Verweis auf die Poolzeile an den Anfang von bemerkung setzen."""
    if d["id"] not in DUBLETTEN_12 or d["bemerkung"].startswith("Dublette von:"):
        return False
    d["bemerkung"] = f"Dublette von: {DUBLETTEN_12[d['id']]}. " + d["bemerkung"]
    return True


# ======================================================================= Lauf 13
# Themenfeld bereinigen (Entscheidung des Lehrers, 16.09.2026): Zeilenthema und
# Typthema müssen übereinstimmen, der Schnitt wird über das Thema des Typs
# gemessen. 21 Zeilen (13 abi, 8 iqb) trugen ein anderes Thema als ihr Typ. Je
# Fall entschieden (Bericht in abi-pruefungen.md § 4): bei 18 Zeilen folgt die
# Zeile dem Typ (leitidee und thema aus abitur-typen.csv); drei Typen wechseln
# das Thema, weil ihre Fertigkeit dort zu Hause ist, und ihre Zeilen folgen –
# kleinste Tangentensteigung ist ein Extremwert der Ableitung (Ableitung und
# Änderungsrate), der Trapeznachweis ist die feste Leistung, der Flächeninhalt
# „wenn verlangt" (Punkte und Strecken, Klasse Ebene Figur bleibt), das Ergänzen
# eines Wahrscheinlichkeitsterms ist Term und Ereignis (Zufallsexperimente und
# Urnenmodelle, Präfix). Feldkorrektur: leitidee und thema jeder Zeile aus dem
# Typ; vier Vermerke in bemerkung, die dem alten Thema folgten, angepasst; in
# 2017-bb-ea-B4.2a stand der Typ noch einmal in typ_neben (gestrichen).
PRAEFIX_13 = {"Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen": "Term und Ereignis"}
NEUES_THEMA_13 = {
    "Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen":
        ("Analysis", "Ableitung und Änderungsrate"),
    "Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen":
        ("Analytische Geometrie", "Punkte und Strecken im Koordinatensystem"),
    "Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen":
        ("Stochastik", "Zufallsexperimente und Urnenmodelle"),
}
BEMERKUNG_13 = {
    "2025MgrundlegendAStochastik13-b": (
        "Erste Fundstelle des Themas Hypergeometrische Verteilung.",
        "Term hypergeometrisch (Quotient von Binomialkoeffizienten); Thema folgt dem Typ (Lauf 13)."),
    "2025MerhoehtAAGLAA221-a": (
        "Thema Scharen von Geraden und Ebenen (nicht für das grundlegende Niveau in BE und BB).",
        "Geradenschar nur als Kontext; Thema folgt dem Typ (Lauf 13)."),
    "2026MgrundlegendBStochastikWTR1-1a": (
        "Typ wiederverwendet (2026-ea-A; Thema hier Binomialverteilung).",
        "Typ wiederverwendet (2026-ea-A); Binomialterm, Thema folgt dem Typ (Lauf 13)."),
    "2017-bb-ea-B4.2a": (
        "Drei Ereignisse in einer Einheit; thema folgt dem ersten Typ.",
        "Drei Ereignisse in einer Einheit, zwei davon Pfadprodukte (ein Typ); thema folgt dem Typ (Lauf 13)."),
    "2017-bb-ea-B2.2e": (
        "Eigene Rechnung.",
        "Teilaufgabe der Analysis-Aufgabe Straßenverlauf; leitidee und thema folgen dem Typ (Lauf 13). Eigene Rechnung."),
}
TYP_THEMA = {}  # typ → (leitidee, thema) nach dem Lauf, füllt main()


def zeile_13(d):
    """leitidee und thema der Zeile aus dem Typ; Vermerke und typ_neben bereinigen."""
    war = False
    if d["id"] in BEMERKUNG_13:
        alt, neu = BEMERKUNG_13[d["id"]]
        if alt not in d["bemerkung"]:
            sys.exit(f"{d['id']}: Vermerk nicht gefunden: {alt}")
        d["bemerkung"] = d["bemerkung"].replace(alt, neu)
        war = True
    neben = [t for t in d["typ_neben"].split("|") if t and t != d["typ"]]
    if "|".join(neben) != d["typ_neben"]:
        d["typ_neben"] = "|".join(neben)
        war = True
    leitidee, thema = TYP_THEMA[d["typ"]]
    if (d["leitidee"], d["thema"]) != (leitidee, thema):
        d["leitidee"], d["thema"] = leitidee, thema
        war = True
    return war


# ======================================================================= Lauf 14
# Pool-Abgleich des abi-Bestands bis 2018 (Auftrag des Lehrers, 16.09.2026):
# Textvergleich der Landeshefte gegen die Pooldateien 2017 (Teil A und B) und
# 2018 (Teil B), die im Profil iqb nicht erfasst sind (Reserve). Wortgleiche
# Teilaufgaben bekommen den Vermerk „Poolaufgabe (nicht erfasst): <Kennung>-
# <Teilaufgabe>." am Anfang von bemerkung – die Vorstufe des Verweises
# „Dublette von:" nach Entscheidung 3, den abi-bau.py erst prüfen kann, wenn die
# Poolzeile im iqb-Katalog steht; die Kennung ist die voraussichtliche iqb-id.
# Abgewandelte Teilaufgaben tragen „(nicht erfasst, abgewandelt)" und den
# Unterschied. Keine Typänderung; Bericht in abi-pruefungen.md § 4.
POOL_14 = {
    # 2017-bb-ea Teil 1 = Pool 2017 erhöht Teil A: Analysis 1.1, AG/LA (A2) 2, Stochastik 2
    "2017-bb-ea-A1.1a": "2017MerhoehtAAnalysis11-a", "2017-bb-ea-A1.1b": "2017MerhoehtAAnalysis11-b",
    "2017-bb-ea-A1.2a": "2017MerhoehtAAGLAA22-a", "2017-bb-ea-A1.2b": "2017MerhoehtAAGLAA22-b",
    "2017-bb-ea-A1.3a": "2017MerhoehtAStochastik2-a", "2017-bb-ea-A1.3b": "2017MerhoehtAStochastik2-b",
    # 2018-be-gk 2.2 Kletteranlage = Pool 2018 grundlegend Teil B AG/LA (A2) WTR 2 a–e
    "2018-be-gk-B2.2a": "2018MgrundlegendBAGLAA2WTR2-1a", "2018-be-gk-B2.2b": "2018MgrundlegendBAGLAA2WTR2-1b",
    "2018-be-gk-B2.2c": "2018MgrundlegendBAGLAA2WTR2-1c", "2018-be-gk-B2.2d": "2018MgrundlegendBAGLAA2WTR2-1d",
    "2018-be-gk-B2.2e": "2018MgrundlegendBAGLAA2WTR2-1e",
    # 2018-be-gk 3.2 Bildschirme = Pool 2018 grundlegend Stochastik WTR 2 b–d, erhöht Stochastik WTR 2 d
    "2018-be-gk-B3.2b": "2018MgrundlegendBStochastikWTR2-1b", "2018-be-gk-B3.2c": "2018MgrundlegendBStochastikWTR2-1c",
    "2018-be-gk-B3.2d": "2018MgrundlegendBStochastikWTR2-1d", "2018-be-gk-B3.2g": "2018MerhoehtBStochastikWTR2-1d",
}
POOL_14_ABGEWANDELT = {
    "2018-be-gk-B3.2a": ("2018MgrundlegendBStochastikWTR2-1a",
                         "Ereignis B im Heft mit 50 statt 200 Bildschirmen (mehr als 10 und weniger als 15 statt mehr als 30 und weniger als 50)"),
    "2018-be-gk-B3.2e": ("2018MerhoehtBStochastikWTR2-1b",
                         "das Heft gibt den Netzteil-Anteil 3,0 % vor, der Pool „entweder Display oder Netzteil 11,7 %“; 3 statt 4 BE"),
}


def zeile_14(d):
    """Vermerk auf die nicht erfasste Poolaufgabe an den Anfang von bemerkung setzen."""
    if d["bemerkung"].startswith("Poolaufgabe (nicht erfasst"):
        return False
    if d["id"] in POOL_14:
        d["bemerkung"] = f"Poolaufgabe (nicht erfasst): {POOL_14[d['id']]}. " + d["bemerkung"]
        return True
    if d["id"] in POOL_14_ABGEWANDELT:
        k, warum = POOL_14_ABGEWANDELT[d["id"]]
        d["bemerkung"] = f"Poolaufgabe (nicht erfasst, abgewandelt): {k}; {warum}. " + d["bemerkung"]
        return True
    return False


# ======================================================================= Lauf 15
# Verweise schließen (Auftrag des Lehrers, 16.09.2026): Die Reserve-Stapel
# 2017-ea-A, 2018-ga-B und 2018-ea-B sind erfasst; die 17 Vermerke aus Lauf 14
# werden zu Verweisen. Wortgleich → „Dublette von: <id>." (typ muss gleich sein,
# afb_amtlich aus der Poolzeile, bei Teil B dazu „AB amtlich: X."); abgewandelt
# → „Abgewandelt von: <id>; <Unterschied>." (kein Typzwang). Zwei Ziele wandern
# vom erhöhten auf den wortgleichen grundlegenden Pool (Befund beim Stapel
# 2018-ga-B). Sicherung: Abbruch, wenn ein typ abweicht oder mehr als 17 Zeilen
# angefasst würden; 2018-be-gk 3.2 f (wortgleich mit dem grundlegenden Pool,
# ohne Vermerk) bleibt bewusst unangetastet und offen.
ZIEL_15 = {"2018-be-gk-B3.2e": "2018MgrundlegendBStochastikWTR2-1e",   # statt erhöht WTR2-1b (abgewandelt)
           "2018-be-gk-B3.2g": "2018MgrundlegendBStochastikWTR2-1g"}   # statt erhöht WTR2-1d
HOECHSTENS_15 = 17
VORSTUFE_15 = re.compile(r"^Poolaufgabe \(nicht erfasst(, abgewandelt)?\): ([A-Za-z0-9-]+)(?:; ([^.]*(?:\.[^ ][^.]*)*))?\. ?")
AB_15 = re.compile(r"AB amtlich: (I{1,3})\.")
_POOL_15 = {}
_PROTOKOLL_15 = []


def poolzeilen_15():
    if not _POOL_15:
        kopf, rows = lade("iqb-katalog.csv")
        _POOL_15.update({r[kopf.index("id")]: dict(zip(kopf, r)) for r in rows})
    return _POOL_15


def zeile_15(d):
    """Vermerk aus Lauf 14 in den Verweis umstellen; typ vergleichen; afb_amtlich übernehmen."""
    m = VORSTUFE_15.match(d["bemerkung"])
    if not m:
        return False
    abgew, pid, unterschied = m.group(1), ZIEL_15.get(d["id"], m.group(2)), m.group(3)
    q = poolzeilen_15().get(pid)
    if q is None:
        sys.exit(f"{d['id']}: Poolzeile {pid} nicht im iqb-Katalog – Vermerk bleibt")
    rest = d["bemerkung"][m.end():]
    if abgew and d["id"] not in ZIEL_15:
        d["bemerkung"] = f"Abgewandelt von: {pid}; {unterschied}. " + rest
        _PROTOKOLL_15.append((d["id"], pid, "abgewandelt", d["typ"] == q["typ"]))
    else:
        if d["typ"] != q["typ"]:
            sys.exit(f"{d['id']}: typ weicht von {pid} ab – nicht umstellbar:\n  abi: {d['typ']}\n  iqb: {q['typ']}")
        ab = AB_15.search(q["bemerkung"])
        zusatz = f"AB amtlich: {ab.group(1)}. " if ab else ""
        if abgew:  # 3.2 e: als abgewandelt vorgemerkt, wortgleich mit dem neuen Ziel
            zusatz += f"Wortgleich mit dem grundlegenden Pool (Lauf 15; in Lauf 14 auf {m.group(2)} als abgewandelt vorgemerkt: {unterschied}). "
        elif d["id"] in ZIEL_15:
            zusatz += f"Wortgleich mit dem grundlegenden Pool (Lauf 15; in Lauf 14 auf {m.group(2)} vorgemerkt). "
        d["bemerkung"] = f"Dublette von: {pid}. " + zusatz + rest
        if not d["afb_amtlich"] and d["jahr"] > "2018":  # Hefte bis 2018 weisen keinen Bereich aus (abi-bau.py)
            d["afb_amtlich"] = q["afb_amtlich"]
        _PROTOKOLL_15.append((d["id"], pid, "dublette", True))
    if len(_PROTOKOLL_15) > HOECHSTENS_15:
        sys.exit(f"Lauf 15 fasst mehr als {HOECHSTENS_15} Zeilen an – Abbruch (Auftrag 16.09.2026)")
    return True


# ======================================================================= Lauf 16
# Reste schließen (Auftrag des Lehrers, 16.09.2026): 2018-be-gk 3.2 f bekommt den
# Verweis „Dublette von:" auf Stochastik WTR 2 f (wortgleich, Befund beim Stapel
# 2018-ga-B, in Lauf 15 als 18. Zeile ausgespart); die fünf Teil-B-Zeilen von
# 2018-be-gk, deren Schätzung vom amtlichen Bereich der Poolzeile abwich, werden
# gegen die enge Eichfassung nachgezogen – sie übernehmen die Schätzung der
# wortgleichen Poolzeile (dort nach der engen Fassung geschätzt, Treffer), der
# alte Wert bleibt in bemerkung. Genau sechs Zeilen.
DUBLETTE_16 = {"2018-be-gk-B3.2f": "2018MgrundlegendBStochastikWTR2-1f"}
NACHZIEHEN_16 = ["2018-be-gk-B2.2a", "2018-be-gk-B2.2b", "2018-be-gk-B3.2b", "2018-be-gk-B3.2c", "2018-be-gk-B3.2d"]
_PROTOKOLL_16 = []


def zeile_16(d):
    war = False
    if d["id"] in DUBLETTE_16 and not d["bemerkung"].startswith("Dublette von"):
        pid = DUBLETTE_16[d["id"]]; q = poolzeilen_15().get(pid)
        if q is None or q["typ"] != d["typ"] or q["punkte"] != d["punkte"]:
            sys.exit(f"{d['id']}: Poolzeile {pid} fehlt oder typ/BE weichen ab")
        ab = AB_15.search(q["bemerkung"])
        d["bemerkung"] = (f"Dublette von: {pid}. " + (f"AB amtlich: {ab.group(1)}. " if ab else "")
                          + "Wortgleich mit dem grundlegenden Pool (Lauf 16; in Lauf 14 als Landesvariante ohne Vermerk geführt, weil gegen den erhöhten Pool verglichen wurde). "
                          + d["bemerkung"])
        _PROTOKOLL_16.append((d["id"], f"Dublette von {pid}")); war = True
    if d["id"] in NACHZIEHEN_16:
        m = re.match(r"Dublette von: ([A-Za-z0-9-]+)\.", d["bemerkung"])
        q = poolzeilen_15().get(m.group(1)) if m else None
        if q is None:
            sys.exit(f"{d['id']}: kein Dublettenverweis für das Nachziehen")
        if d["niveau_geschaetzt"] != q["niveau_geschaetzt"]:
            alt = d["niveau_geschaetzt"]
            d["niveau_geschaetzt"] = q["niveau_geschaetzt"]
            d["bemerkung"] += f" Schätzung nach der engen Fassung nachgezogen (Lauf 16): {q['niveau_geschaetzt']} statt {alt}, wie die wortgleiche Poolzeile."
            _PROTOKOLL_16.append((d["id"], f"niveau {alt} → {q['niveau_geschaetzt']}")); war = True
    if len(_PROTOKOLL_16) > 6:
        sys.exit("Lauf 16 fasst mehr als sechs Zeilen an – Abbruch")
    return war


# ======================================================================= Lauf 17
# Nach den vier Stark-Heften des Auftrags „Geltung klären, Reste schließen,
# vier Stark-Hefte erfassen" (2022-bebb-gk, 2025-bebb-gk, 2022-bebb-lk,
# 2023-bebb-lk): Etiketten der Hefte gegen die Liste gehalten (Ähnlichkeits-
# suche über alle neuen Typen der vier Hefte, dann Definitionen verglichen).
# Drei Paare tragen dieselbe Fertigkeit unter verschiedenen Bedingungslisten:
# (1) Steckbriefaufgabe dritten Grades – Extrempunkt, Nullstelle, Parallelität
# sind Wert- und Steigungsbedingungen desselben LGS (2023-bebb-gk, 2022-bebb-lk);
# (2) Rekonstruktion aus knickfreiem Übergang und Wertbedingung – quadratisch
# (2018-be-gk) oder mit zwei Parametern (2022-bebb-gk), derselbe Ansatz;
# (3) Fehler zweiter Art für selbst gewählte Anteile – Vergleich mit einer
# Schranke (2024-ea-B) oder Deutung im Sachzusammenhang (2023-bebb-lk), die
# erste Leistung ist dieselbe. Nicht zusammengezogen: „Parabel ohne lineares
# Glied … aus einem Flächeninhalt" (2023-bebb-lk, Integralbedingung), die
# Lösungsweg-Typen (verschiedene Wege), Raute/Drachenviereck.
ZUSAMMEN_17 = {
    "Ganzrationale Funktion dritten Grades aus Wert-, Steigungs- und Extrempunktbedingungen rekonstruieren":
        "Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren",
    "Ganzrationale Funktion dritten Grades aus Nullstellen-, Steigungs- und Parallelitätsbedingungen rekonstruieren":
        "Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren",
    "Quadratische Funktion aus knickfreiem Übergang und einer Wertbedingung rekonstruieren":
        "Funktionsgleichung aus knickfreiem Übergang und einer Wertbedingung rekonstruieren",
    "Ganzrationale Funktion mit zwei Parametern aus einem Punkt und knickfreiem Übergang rekonstruieren":
        "Funktionsgleichung aus knickfreiem Übergang und einer Wertbedingung rekonstruieren",
    "Fehler zweiter Art für einen selbst gewählten Anteil berechnen und mit einer Schranke vergleichen":
        "Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen",
    "Fehler zweiter Art für zwei selbst gewählte Anteile berechnen und im Sachzusammenhang deuten":
        "Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen",
}
NEUE_DEFINITION_17 = {
    "Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren":
        "Aus dem allgemeinen Ansatz dritten Grades die vier Koeffizienten über ein lineares Gleichungssystem aus "
        "Wert- und Steigungsbedingungen bestimmen; Punkte, Nullstellen, Extrempunkte (Wert und Ableitung null) und "
        "Parallelität zu einer Geraden (gleiche Steigung) sind solche Bedingungen, welche vorliegen, steht in der Zeile.",
    "Funktionsgleichung aus knickfreiem Übergang und einer Wertbedingung rekonstruieren":
        "Aus der Forderung, dass zwei Graphen an einer Stelle ohne Knick ineinander übergehen (gleicher Funktionswert, "
        "gleicher Anstieg), und einer weiteren Wertbedingung die Parameter einer Ansatzfunktion (quadratisch oder mit zwei "
        "Parametern wie a · x⁴ + b · x²) über ein Gleichungssystem bestimmen.",
    "Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen":
        "Für einen oder mehrere selbst gewählte Anteile, bei denen die Nullhypothese falsch ist, die Wahrscheinlichkeit "
        "des Annahmebereichs berechnen und das Ergebnis einordnen – gegen eine Schranke oder als Fehlentscheidung im "
        "Sachzusammenhang; was verlangt ist, steht in der Zeile.",
}

# ======================================================================= Lauf 18
# Nach dem Reserve-Stapel 2022-ga-B (Auftrag „2026 Brandenburg erfassen, Reserve
# 2022-ga-B öffnen", 17.09.2026): die 19 Vormerkungen von 2022-bebb-gk (Heftlauf
# 16.09.2026) werden wie in Lauf 15 zu Verweisen. Die Poolzeilen tragen Typ und
# Schätzung der Landeszeilen (aus ihnen erzeugt), der Typvergleich ist die Probe.
# Teil-B-Zeilen ab 2019 bekommen afb_amtlich aus der AB-Spalte der Poolzeile
# (wie dubletten.py bei den Heften 2023–2025). Genau 19 Zeilen.
HOECHSTENS_18 = 19
_PROTOKOLL_18 = []


def zeile_18(d):
    m = VORSTUFE_15.match(d["bemerkung"])
    if not m:
        return False
    abgew, pid, unterschied = m.group(1), m.group(2), m.group(3)
    q = poolzeilen_15().get(pid)
    if q is None:
        sys.exit(f"{d['id']}: Poolzeile {pid} nicht im iqb-Katalog – Vermerk bleibt")
    rest = d["bemerkung"][m.end():]
    ab = AB_15.search(q["bemerkung"])
    if abgew:
        d["bemerkung"] = f"Abgewandelt von: {pid}; {unterschied}. " + (f"AB amtlich der Poolzeile: {ab.group(1)}. " if ab else "") + rest
        _PROTOKOLL_18.append((d["id"], pid, "abgewandelt", d["typ"] == q["typ"]))
    else:
        if d["typ"] != q["typ"] or d["typ_neben"] != q["typ_neben"]:
            sys.exit(f"{d['id']}: typ weicht von {pid} ab – nicht umstellbar:\n  abi: {d['typ']}|{d['typ_neben']}\n  iqb: {q['typ']}|{q['typ_neben']}")
        d["bemerkung"] = f"Dublette von: {pid}. " + (f"AB amtlich: {ab.group(1)}. " if ab else "") + "Wortgleich mit dem grundlegenden Pool 2022 (Lauf 18; im Heftlauf vorgemerkt). " + rest
        if not d["afb_amtlich"]:
            d["afb_amtlich"] = ab.group(1) if ab else q["afb_amtlich"]
        _PROTOKOLL_18.append((d["id"], pid, "dublette", True))
    if len(_PROTOKOLL_18) > HOECHSTENS_18:
        sys.exit(f"Lauf 18 fasst mehr als {HOECHSTENS_18} Zeilen an – Abbruch")
    return True


# ======================================================================= Lauf 19
# Nach dem Reserve-Stapel 2022-ga-B und den Heften 2026-bb-gk und 2026-bb-ea
# (Auftrag „2026 Brandenburg erfassen, Reserve 2022-ga-B öffnen", 17.09.2026):
# Ähnlichkeitssuche über die 40 neuen Typen, Definitionen verglichen. Drei
# Paare tragen dieselbe Fertigkeit unter verschiedener Figur oder Richtung:
# (1) Näherungswert eines Integrals als Fläche eines eingezeichneten Vielecks –
# Dreieck (2025-ga-B) oder Trapez aus Tangenten (2022-ga-B); (2) Produkt aus
# Potenz und Binomialterm als Ereignis mit festem Abschnitt – festes Endstück
# mit einem Binomialterm (2022-bebb-lk) oder festes Anfangsstück mit kumulierter
# Summe (2022-ga-B), die Zerlegung der Kette ist dieselbe; (3) passenden Graphen
# zu einem Term über Funktionswerte auswählen – als Ausschluss (2021-ga-A) oder
# Auswahl (2022-ga-B) gefragt. Getrennt gelassen: die beiden Stichprobenumfänge
# (aus dem Erwartungswert gegen Suche am Rechner), Sinusparameter aus
# Extremstelle und Wert gegen zwei Extrempunkte (anderer Ansatz für b).
ZUSAMMEN_19 = {
    "Integralwert: Näherungswert eines Integrals als Dreiecksfläche am Graphen begründen":
        "Integralwert: Näherungswert eines Integrals als Vielecksfläche am Graphen begründen",
    "Integralwert: Näherungswert eines Integrals als Trapezfläche am Graphen begründen":
        "Integralwert: Näherungswert eines Integrals als Vielecksfläche am Graphen begründen",
    "Term und Ereignis: Produkt aus Potenz und Binomialterm als Ereignis mit festem Endstück deuten":
        "Term und Ereignis: Produkt aus Potenz und Binomialterm als Ereignis mit festem Abschnitt deuten",
    "Term und Ereignis: Produkt aus Potenz und kumulierter Binomialsumme als Ereignis beschreiben":
        "Term und Ereignis: Produkt aus Potenz und Binomialterm als Ereignis mit festem Abschnitt deuten",
    "Nullstellen und Werte: Unpassende Graphen zu einem Funktionsterm ausschließen":
        "Nullstellen und Werte: Passenden Graphen zu einem Funktionsterm über Funktionswerte auswählen",
    "Nullstellen und Werte: Passende Abbildung des Graphen über einen Funktionswert auswählen":
        "Nullstellen und Werte: Passenden Graphen zu einem Funktionsterm über Funktionswerte auswählen",
}
NEUE_DEFINITION_19 = {
    "Integralwert: Näherungswert eines Integrals als Vielecksfläche am Graphen begründen":
        "Einen vorgegebenen Term als Flächeninhalt eines in die Abbildung eingezeichneten Vielecks (Dreieck, Trapez aus "
        "Tangenten oder Sehnen) deuten und als Näherung des Integrals begründen; welche Figur, steht in der Zeile.",
    "Term und Ereignis: Produkt aus Potenz und Binomialterm als Ereignis mit festem Abschnitt deuten":
        "Einen Term aus einer Potenz q^k und einem Binomialterm oder einer kumulierten Binomialsumme einem Ereignis "
        "zuordnen, bei dem ein Abschnitt der Bernoulli-Kette festliegt und im übrigen Abschnitt eine feste oder "
        "beschränkte Trefferzahl auftritt.",
    "Nullstellen und Werte: Passenden Graphen zu einem Funktionsterm über Funktionswerte auswählen":
        "Unter vorgelegten Graphen den zum Term passenden auswählen bzw. die unpassenden ausschließen, über einen "
        "Funktionswert oder eine Eigenschaft wie die Nichtkonstanz der Steigung.",
}

# ======================================================================= Lauf 20
# Vorrang des Amtlichen (Entscheidung des Lehrers, 17.09.2026; Kern § 5 v0.6):
# Wird eine Poolzeile mit amtlichem Standardbezug erfasst und weicht die aus
# einer Landeszeile übernommene Schätzung davon ab, wird die Schätzung
# korrigiert, nicht die Schwelle; die Landeszeile zieht nach. Betroffen: die
# neun Poolzeilen von 2022-ga-B (Analysis WTR 2 1 a, d, 2 a, b, d; AG/LA (A2)
# WTR 2 a, c, e, f), deren Schätzung aus 2022-bebb-gk übernommen war (10 von 19
# trafen), und die Landeszeilen: in 2022-bebb-gk die sieben wortgleichen
# Dubletten neben dem amtlichen Bereich (2.1 a, g, j, k; 3 b, e, i); in den
# früher erfassten Heften 2017-bb-ea (1.2 b, 1.3 b) und 2018-bb-ea (1.2 b, 1.1 a)
# vier Dubletten, deren eigene Schätzung nach der Erfassung der Poolzeile
# (2017-ea-A, 2018-ea-A) vom amtlichen Bereich abwich – dort hatten die
# Poolzeilen eine eigene Schätzung, die Lage von 2022 lag nicht vor. Nicht
# angefasst: abgewandelte Fassungen (2.1 m, 3 g, 4 j; 2018-be-gk 3.2 a – eigene
# Fassung, eigene Schätzung) und Poolzeilen mit eigener, abweichender Schätzung
# (Messwert der Eichung). Zielwert je Zeile ist der amtliche Bereich (AB-Spalte
# in Teil B, höchster Bereich in Teil A); die Funktion prüft das und bricht ab.
KORREKTUR_20 = {
    "2022MgrundlegendBAnalysisWTR2-1a": "I", "2022MgrundlegendBAnalysisWTR2-1d": "II",
    "2022MgrundlegendBAnalysisWTR2-2a": "I", "2022MgrundlegendBAnalysisWTR2-2b": "II",
    "2022MgrundlegendBAnalysisWTR2-2d": "III", "2022MgrundlegendBAGLAA2WTR2-1a": "I",
    "2022MgrundlegendBAGLAA2WTR2-1c": "I", "2022MgrundlegendBAGLAA2WTR2-1e": "II",
    "2022MgrundlegendBAGLAA2WTR2-1f": "III",
    "2022-bebb-gk-B2.1a": "I", "2022-bebb-gk-B2.1g": "II", "2022-bebb-gk-B2.1j": "I",
    "2022-bebb-gk-B2.1k": "II", "2022-bebb-gk-B3b": "I", "2022-bebb-gk-B3e": "I",
    "2022-bebb-gk-B3i": "III",
    "2017-bb-ea-A1.2b": "III", "2017-bb-ea-A1.3b": "III",
    "2018-bb-ea-A1.2b": "III", "2018-bb-ea-A1.1a": "III",
}
HOECHSTENS_20 = 20
ORD_20 = {"I": 1, "II": 2, "III": 3}
ENG_20 = re.compile(r"Schätzung enge Fassung: (I{1,3})")
_PROTOKOLL_20 = []


def amtlich_20(q):
    """Amtlicher Bereich einer Poolzeile: Spalte AB (Teil B) oder höchster Bereich (Teil A)."""
    m = AB_15.search(q["bemerkung"])
    if m:
        return m.group(1)
    werte = [t for t in q["afb_amtlich"].split("|") if t in ORD_20]
    return max(werte, key=ORD_20.get) if werte else ""


def zeile_20(d):
    if d["id"] not in KORREKTUR_20:
        return False
    neu, alt = KORREKTUR_20[d["id"]], d["niveau_geschaetzt"]
    if alt == neu or ENG_20.search(d["bemerkung"]):
        sys.exit(f"{d['id']}: Schätzung schon {alt} oder Vermerk enge Fassung vorhanden – Abbruch")
    pool = poolzeilen_15()
    if d["id"] in pool:  # Poolzeile mit übernommener Schätzung
        if "aus der Landeszeile" not in d["bemerkung"] or amtlich_20(d) != neu:
            sys.exit(f"{d['id']}: keine übernommene Schätzung oder Zielwert {neu} nicht amtlich ({amtlich_20(d)})")
        d["bemerkung"] += (f" Schätzung nach dem amtlichen Bereich korrigiert (Lauf 20, Vorrang des Amtlichen, "
                           f"Kern § 5): {neu} statt {alt}; die aus der Landeszeile übernommene Schätzung wich von der "
                           f"Spalte Anforderungsbereich ab.")
    else:  # Landeszeile: wortgleiche Dublette, zieht nach
        m = re.match(r"Dublette von: ([A-Za-z0-9-]+)\.", d["bemerkung"])
        q = pool.get(m.group(1)) if m else None
        if q is None or amtlich_20(q) != neu:
            sys.exit(f"{d['id']}: kein Dublettenverweis oder Zielwert {neu} nicht amtlich ({amtlich_20(q) if q else '-'})")
        d["bemerkung"] += (f" Schätzung nach dem amtlichen Bereich der Poolzeile nachgezogen (Lauf 20, Vorrang des "
                           f"Amtlichen, Kern § 5): {neu} statt {alt}.")
    d["niveau_geschaetzt"] = neu
    _PROTOKOLL_20.append((d["id"], alt, neu))
    if len(_PROTOKOLL_20) > HOECHSTENS_20:
        sys.exit(f"Lauf 20 fasst mehr als {HOECHSTENS_20} Zeilen an – Abbruch")
    return True


# ======================================================================= Lauf 21
# Nach den fünf Stark-Heften des Auftrags B, Teil 1 (2019-be-gk, 2020-be-gk,
# 2021-be-gk, 2024-bebb-lk, 2025-bebb-lk; 17.09.2026): Ähnlichkeitssuche über
# die 91 neuen Typen der fünf Hefte (Wortmenge und Zeichenfolge, gleiches
# Thema), Definitionen der Kandidatenpaare verglichen. Vier Paare tragen
# dieselbe Fertigkeit: (1) Maximum einer ganzrationalen Modellfunktion über
# die Ableitung – die Gewinnfunktion (2018-ga-B, 2018-ea-B) ist der Sonderfall
# mit vorherigem Aufstellen als Differenz, die Maximumsbestimmung ist
# dieselbe (2019-be-gk); (2) Nullstellen einer faktorisiert vorgegebenen
# Ableitung ablesen – als Stellen mit waagerechter Tangente (2023-bebb-lk)
# oder als mögliche Extremstellen (2024-bebb-lk, Nebentyp) gefragt, das Thema
# des Typs bleibt Tangente, Normale, Schnittwinkel; (3) mindestens oder
# höchstens einmal über das Gegenereignis – bei zwei Stufen (2020-ea-A,
# 2019-ga-A, 2022-bebb-lk) oder bei drei Stufen mit Abbruch nach dem ersten
# Treffer („spätestens der dritte Erfolg", 2020-be-gk, Nebentyp); (4)
# quadratische Steckbriefaufgabe – aus Nullstelle und Scheitel (2021-be-gk)
# oder aus Punkt und Tangentengleichung (2020-ga-A), beides Wert- und
# Steigungsbedingungen desselben LGS, wie Lauf 17 für den dritten Grad.
# Getrennt gelassen: Parallelität prüfen gegen Nichtidentität begründen (beide
# über die Richtungsvektoren, aber entgegengesetzter Schluss); Fläche mit
# vorgegebener Stammfunktion (2020-be-gk) gegen vorgegebenen Flächenterm
# (2025-ea-B); größte Änderungsrate eines Bestands (2019-be-gk) gegen
# maximale Rate einer Ratenfunktion (2026-ga-B, Lauf 11).
ZUSAMMEN_21 = {
    "Maximum einer Gewinnfunktion über die Ableitung berechnen":
        "Maximum einer ganzrationalen Funktion im Sachzusammenhang über die Ableitung berechnen",
    "Mögliche Extremstellen aus der faktorisierten Ableitung ohne Rechnung angeben":
        "Stellen mit waagerechter Tangente aus der faktorisierten Ableitung angeben",
    "Wahrscheinlichkeit für mindestens oder höchstens einmal bei zwei Stufen über das Gegenereignis berechnen":
        "Wahrscheinlichkeit für mindestens oder höchstens einmal bei mehreren Stufen über das Gegenereignis berechnen",
    "Wahrscheinlichkeit für spätestens den dritten Erfolg über die Pfade oder das Gegenereignis berechnen":
        "Wahrscheinlichkeit für mindestens oder höchstens einmal bei mehreren Stufen über das Gegenereignis berechnen",
    "Quadratische Funktion aus Nullstelle und Scheitelpunkt rekonstruieren":
        "Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren",
    "Quadratische Funktion aus Ursprung und Tangentengleichung bestimmen":
        "Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren",
}
NEUE_DEFINITION_21 = {
    "Maximum einer ganzrationalen Funktion im Sachzusammenhang über die Ableitung berechnen":
        "Den größten Wert einer ganzrationalen Modellfunktion (maximale Höhe, größter Gewinn – die Gewinnfunktion "
        "gegebenenfalls zuvor als Differenz von Erlös und Kosten aufgestellt) über die Nullstellen der Ableitung mit "
        "hinreichender Bedingung oder Auswahl im zulässigen Bereich berechnen und die Stelle im Sachzusammenhang deuten.",
    "Stellen mit waagerechter Tangente aus der faktorisierten Ableitung angeben":
        "Aus einer faktorisiert vorgegebenen Ableitung die Nullstellen ablesen und als Stellen mit waagerechter Tangente "
        "bzw. als mögliche Extremstellen (notwendige Bedingung, ohne hinreichende Prüfung) angeben.",
    "Wahrscheinlichkeit für mindestens oder höchstens einmal bei mehreren Stufen über das Gegenereignis berechnen":
        "In einem zwei- oder dreistufigen Experiment (auch mit Abbruch nach dem ersten Treffer) die Wahrscheinlichkeit für "
        "mindestens einmal oder höchstens einmal über das Gegenereignis (kein Treffer bzw. lauter Treffer) berechnen oder "
        "nachweisen, ersatzweise über die Summe der Pfade; die Stufen können eine Weiche haben.",
    "Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren":
        "Aus dem allgemeinen Ansatz zweiten Grades (oder der Scheitelpunktform) die Koeffizienten über ein Gleichungssystem "
        "aus Wert- und Steigungsbedingungen bestimmen; Punkte, Nullstellen, Scheitel (Wert und Ableitung null) und eine "
        "Tangentengleichung (Wert und Steigung an der Berührstelle) sind solche Bedingungen, welche vorliegen, steht in der Zeile.",
}

# ======================================================================= Lauf 22
# Maßstab der Schätzung (Auftrag C, Teil 0, Entscheidung des Lehrers,
# 17.09.2026; Kern § 5 v0.7): niveau_geschaetzt ist genau dort an einem
# amtlichen Bereich messbar, wo afb_amtlich gefüllt ist – leer heißt Schätzung
# ohne Maßstab, ohne eigene Markierung. Damit das im abi-Bestand gilt, bekommen
# die Dubletten der Hefte bis 2018 afb_amtlich aus ihrer Poolzeile, wie es die
# Dubletten ab 2019 seit Lauf 15/18 und dubletten.py tragen: Teil A den
# Bereichswert der Poolzeile (Standardbezug, Liste wie I|II), Teil B die
# AB-Spalte, die schon als „AB amtlich: X." in bemerkung steht. Betroffen sind
# genau 21 Zeilen (2017-bb-ea Teil A 6, 2018-bb-ea Teil A 4, 2018-be-gk Teil B
# 11); die frühere Regel „afb_amtlich bleibt bei Heften bis 2018 leer"
# (abi-bau.py bis v0.8, Lauf 15) entfällt: abi-bau.py v0.9 verlangt
# afb_amtlich genau bei „Dublette von:". Sonst bleibt alles unverändert.
HOECHSTENS_22 = 21
_PROTOKOLL_22 = []


def zeile_22(d):
    if d["jahr"] > "2018" or d["afb_amtlich"]:
        return False
    m = re.match(r"Dublette von: ([A-Za-z0-9-]+)\.", d["bemerkung"])
    if not m:
        return False
    q = poolzeilen_15().get(m.group(1))
    if q is None:
        sys.exit(f"{d['id']}: Poolzeile {m.group(1)} nicht im iqb-Katalog – Abbruch")
    ab = AB_15.search(d["bemerkung"])
    if d["block"] == "B":
        if not ab or not AB_15.search(q["bemerkung"]) or ab.group(1) != AB_15.search(q["bemerkung"]).group(1):
            sys.exit(f"{d['id']}: AB-Spalte fehlt oder weicht von der Poolzeile ab – Abbruch")
        d["afb_amtlich"] = ab.group(1)
    else:
        if ab or not q["afb_amtlich"]:
            sys.exit(f"{d['id']}: Teil A mit AB-Spalte oder Poolzeile ohne afb_amtlich – Abbruch")
        d["afb_amtlich"] = q["afb_amtlich"]
    _PROTOKOLL_22.append((d["id"], m.group(1), d["afb_amtlich"]))
    if len(_PROTOKOLL_22) > HOECHSTENS_22:
        sys.exit(f"Lauf 22 fasst mehr als {HOECHSTENS_22} Zeilen an – Abbruch")
    return True


LAEUFE = {
    1: (PRAEFIX_1, ZUSAMMEN_1, NEUE_DEFINITION_1, NEUES_THEMA_1),
    2: ({}, ZUSAMMEN_2, NEUE_DEFINITION_2, {}),
    3: ({}, ZUSAMMEN_3, NEUE_DEFINITION_3, {}),
    4: ({}, ZUSAMMEN_4, NEUE_DEFINITION_4, {}),
    5: ({}, ZUSAMMEN_5, NEUE_DEFINITION_5, {}),
    6: ({}, ZUSAMMEN_6, NEUE_DEFINITION_6, {}),
    7: ({}, ZUSAMMEN_7, NEUE_DEFINITION_7, NEUES_THEMA_7),
    8: ({}, ZUSAMMEN_8, NEUE_DEFINITION_8, {}),
    9: ({}, {}, {}, {}),
    10: ({}, ZUSAMMEN_10, NEUE_DEFINITION_10, {}),
    11: ({}, ZUSAMMEN_11, NEUE_DEFINITION_11, {}),
    12: (PRAEFIX_12, ZUSAMMEN_12, NEUE_DEFINITION_12, NEUES_THEMA_12),
    13: (PRAEFIX_13, {}, {}, NEUES_THEMA_13),
    14: ({}, {}, {}, {}),
    15: ({}, {}, {}, {}),
    16: ({}, {}, {}, {}),
    17: ({}, ZUSAMMEN_17, NEUE_DEFINITION_17, {}),
    18: ({}, {}, {}, {}),
    19: ({}, ZUSAMMEN_19, NEUE_DEFINITION_19, {}),
    20: ({}, {}, {}, {}),
    21: ({}, ZUSAMMEN_21, NEUE_DEFINITION_21, {}),
    22: ({}, {}, {}, {}),
}
FELDKORREKTUR = {5: [("bemerkung", bemerkung_5)], 7: [("*", zeile_7)], 12: [("*", zeile_12)],
                 13: [("*", zeile_13)], 14: [("*", zeile_14)], 15: [("*", zeile_15)], 16: [("*", zeile_16)],
                 18: [("*", zeile_18)], 20: [("*", zeile_20)], 22: [("*", zeile_22)]}
STREICHEN = {9: streiche_9}  # Lauf → fn(Zeile als dict) → True: Zeile entfällt
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
    if LAUF == 12:
        # Umstellungslauf: beide alten Listen hintereinander, iqb zuerst
        if os.path.exists(TYP):
            sys.exit(f"{TYP} existiert schon – Lauf 12 wird genau einmal gefahren")
        typen, kopf_t = [], None
        for p in QUELL_TYPEN_12:
            k, rows = lade(p)
            kopf_t = kopf_t or k
            typen += rows
    else:
        kopf_t, typen = lade(TYP)
    kataloge = [(p, *lade(p)) for p in KATALOGE if os.path.exists(p)]
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
    TYP_THEMA.update({r[0]: (r[1], r[2]) for r in neue_typen})

    # Kataloge: beide Typfelder, je Katalog
    geaendert, zeilen_geaendert, korrigiert, gestrichen, benutzt, alle_ids = {}, {}, 0, [], set(), set()
    for p, kopf_k, kat in kataloge:
        i_typ, i_neben = kopf_k.index("typ"), kopf_k.index("typ_neben")
        geaendert[p] = zeilen_geaendert[p] = 0
        for r in kat:
            war = False
            for i in (i_typ, i_neben):
                teile = [abbildung.get(t, t) for t in r[i].split("|") if t]
                neu = "|".join(teile)
                if neu != r[i]:
                    geaendert[p] += 1
                    war = True
                    r[i] = neu
            zeilen_geaendert[p] += war

        # Feldkorrektur (Lauf 5: Markierung der Trägerbindung in bemerkung; Lauf 7:
        # Thema Konfidenzintervalle). Ein Eintrag (feld, fn) korrigiert ein Feld aus
        # seinem Text; ("*", fn) bekommt die ganze Zeile als dict und ändert sie in place.
        for feld, fn in FELDKORREKTUR.get(LAUF, []):
            if feld == "*":
                for r in kat:
                    d = dict(zip(kopf_k, r))
                    if fn(d):
                        korrigiert += 1
                        r[:] = [d[k] for k in kopf_k]
                continue
            i_feld = kopf_k.index(feld)
            for r in kat:
                neu = fn(r[i_feld])
                if neu != r[i_feld]:
                    korrigiert += 1
                    r[i_feld] = neu

        # Streichen (Lauf 9: Zeilen von Dubletten).
        if LAUF in STREICHEN:
            fn = STREICHEN[LAUF]
            bleibt = []
            for r in kat:
                (gestrichen if fn(dict(zip(kopf_k, r))) else bleibt).append(r)
            kat[:] = bleibt
        benutzt |= {t for r in kat for i in (i_typ, i_neben) for t in r[i].split("|") if t}
        alle_ids |= {r[kopf_k.index("id")] for r in kat}

    # Kein Typ darf seine beispiel_id verlieren, kein Typ unbenutzt sein, keine
    # Zeile einen Typ tragen, der nicht in der Liste steht.
    verwaist = [t[0] for t in neue_typen if t[4] not in alle_ids]
    if verwaist:
        sys.exit(f"beispiel_id in keinem Katalog: {verwaist}")
    unbenutzt = [t[0] for t in neue_typen if t[0] not in benutzt]
    if unbenutzt:
        sys.exit(f"Typen ohne Zeile: {unbenutzt}")
    fremd = sorted(benutzt - {t[0] for t in neue_typen})
    if fremd:
        sys.exit(f"Typen im Katalog, aber nicht in der Liste: {fremd}")
    # Seit Lauf 13: leitidee und thema jeder Zeile sind die ihres Typs (die
    # Bau-Skripte prüfen dasselbe; ein Lauf darf den Zustand nicht verlassen).
    if LAUF >= 13:
        abweichend = [r[kopf_k.index("id")] for _, kopf_k, kat in kataloge for r in kat
                      if (r[kopf_k.index("leitidee")], r[kopf_k.index("thema")]) != TYP_THEMA[r[kopf_k.index("typ")]]]
        if abweichend:
            sys.exit(f"Zeilenthema ≠ Typthema nach dem Lauf: {abweichend}")

    schreibe(TYP, kopf_t, neue_typen)
    for p, kopf_k, kat in kataloge:
        schreibe(p, kopf_k, kat)
    if LAUF == 12:
        for p in QUELL_TYPEN_12:
            os.remove(p)

    # Bericht
    zeilen = sum(len(kat) for _, _, kat in kataloge)
    print(f"Abgleichlauf {LAUF}")
    print(f"Typen vorher {vorher}, nachher {len(neue_typen)}; Typfelder geändert: "
          + ", ".join(f"{p} {n} (in {zeilen_geaendert[p]} Zeilen)" for p, n in geaendert.items())
          + f"; {zeilen} Zeilen in {len(kataloge)} Katalogen, {zeilen/len(neue_typen):.2f} Zeilen je Typ."
          + (f" Feldkorrektur: {korrigiert} Zeilen." if korrigiert else "")
          + (f" Gestrichen: {len(gestrichen)} Zeilen." if gestrichen else ""))
    for r in gestrichen:
        print("  gestrichen:", r[0])
    if LAUF == 18:
        print(f"\nVerweise geschlossen ({len(_PROTOKOLL_18)} Zeilen, höchstens {HOECHSTENS_18}):")
        for i, pid, art, gleich in _PROTOKOLL_18:
            print(f"  {i} → {pid} [{art}] typ {'gleich' if gleich else 'VERSCHIEDEN'}")
        rest = [r[kopf_k.index("id")] for _, kopf_k, kat in kataloge for r in kat
                if r[kopf_k.index("bemerkung")].startswith("Poolaufgabe (nicht erfasst")]
        print("  offen bleibende Vermerke:", ", ".join(rest) if rest else "keine")
    if LAUF == 22:
        if len(_PROTOKOLL_22) != HOECHSTENS_22:
            sys.exit(f"Lauf 22: {len(_PROTOKOLL_22)} statt {HOECHSTENS_22} Zeilen angefasst")
        print(f"\nafb_amtlich aus der Poolzeile übernommen ({len(_PROTOKOLL_22)} Zeilen, Hefte bis 2018):")
        for i, pid, wert in _PROTOKOLL_22:
            print(f"  {i} ← {pid}: {wert}")
    if LAUF == 20:
        fehlt = sorted(set(KORREKTUR_20) - {i for i, _, _ in _PROTOKOLL_20})
        if fehlt:
            sys.exit(f"Lauf 20: Zeilen nicht gefunden: {fehlt}")
        print(f"\nSchätzungen auf den amtlichen Bereich gesetzt ({len(_PROTOKOLL_20)} Zeilen, höchstens {HOECHSTENS_20}):")
        for i, alt, neu in _PROTOKOLL_20:
            print(f"  {i}: {alt} → {neu}")
    if LAUF == 16:
        print(f"\nReste geschlossen ({len(_PROTOKOLL_16)} Zeilen):")
        for i, was in _PROTOKOLL_16:
            print(f"  {i}: {was}")
    if LAUF == 15:
        print(f"\nVerweise geschlossen ({len(_PROTOKOLL_15)} Zeilen, höchstens {HOECHSTENS_15}):")
        for i, pid, art, gleich in _PROTOKOLL_15:
            print(f"  {i} → {pid} [{art}] typ {'gleich' if gleich else 'VERSCHIEDEN'}")
        rest = [r[kopf_k.index("id")] for _, kopf_k, kat in kataloge for r in kat
                if r[kopf_k.index("bemerkung")].startswith("Poolaufgabe (nicht erfasst")]
        print("  offen bleibende Vermerke:", ", ".join(rest) if rest else "keine")
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
