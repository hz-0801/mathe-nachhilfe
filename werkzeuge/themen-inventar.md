# Themeninventar der vier Prüfungskataloge

Erzeugt am 2026-09-19 von `themen-inventar.py v0.1` aus `msa/msa-katalog-basis.csv`, `msa/msa-katalog-kontext.csv`, `fhr/fhr-katalog.csv`, `abitur/abi-katalog.csv`, `abitur/iqb-katalog.csv`; Typenlisten `msa/msa-typen.csv`, `fhr/fhr-typen.csv`, `abitur/abitur-typen.csv`; Sek-I-Referenz aus `katalog/`.

**Diese Datei wird abgeleitet und nie von Hand geändert.** Namen stehen wortgleich wie in den Dateien, samt Tippfehlern; ein leeres Feld heißt „(leer)". Vorstufe der Themenkonkordanz – das Zusammenführen entscheidet der Chat, nicht das Skript.

## 1 Kennzahlen

| Profil | Zeilen gesamt | Themen gesamt | Typen gesamt |
|---|---:|---:|---:|
| msa | 393 | 32 | 175 |
| fhr | 253 | 28 | 86 |
| abi | 794 | 44 | 565 |
| iqb | 1443 | 47 | 1044 |

Themen gesamt = verschiedene Werte in `thema`; Typen gesamt = verschiedene Werte in `typ` (nur Haupttyp, `typ_neben` nicht gezählt).

## 2 Themen je Profil

### msa

| Leitidee | Thema | Zeilen | Typen | drei häufigste Typen |
|---|---|---:|---:|---|
| Daten und Zufall | Kenngrößen | 22 | 7 | Arithmetisches Mittel berechnen (8) · Spannweite berechnen (7) · Median bestimmen (2) |
| Daten und Zufall | Wahrscheinlichkeit mehrstufig | 17 | 6 | Baumdiagramm ergänzen (6) · Wahrscheinlichkeit mehrstufig unabhängig (4) · Wahrscheinlichkeit mehrstufig ohne Zurücklegen (3) |
| Daten und Zufall | Wahrscheinlichkeit einstufig | 14 | 2 | Wahrscheinlichkeit einstufig (12) · Zufallsgerät zu Wahrscheinlichkeit entwerfen (2) |
| Daten und Zufall | Diagramme lesen und beurteilen | 11 | 6 | Aussage zu Diagramm prüfen (3) · Verzerrung eines Diagramms erklären (2) · Achsenskalierung aus Säule bestimmen (2) |
| Daten und Zufall | Daten darstellen | 7 | 5 | Säulen- oder Balkendiagramm ergänzen (2) · Sektor im Kreisdiagramm zuordnen (2) · Prozentsatz berechnen (1) |
| Daten und Zufall | Zählen und Kombinatorik | 6 | 4 | Ergebnismenge aufzählen (2) · Anzahl der Anordnungen bestimmen (2) · Größte Zahl aus Ziffern bilden (1) |
| Gleichungen und Funktionen | Quadratische Funktionen | 31 | 17 | Scheitelpunkt ablesen (8) · Punktprobe durchführen (3) · Schnittpunkte Gerade und Parabel berechnen (3) |
| Gleichungen und Funktionen | Lineare Funktionen | 28 | 19 | Gerade aus Gleichung zeichnen (5) · Graph nach Eigenschaft auswählen (2) · Gerade durch zwei Punkte zeichnen (2) |
| Gleichungen und Funktionen | Exponentialfunktionen und Wachstum | 21 | 10 | Wachstumstabelle ergänzen (5) · Funktionswert berechnen (3) · Wachstumsfaktor aus Tabelle bestimmen (2) |
| Gleichungen und Funktionen | Zuordnungen proportional und antiproportional | 10 | 4 | Proportionale Zuordnung Dreisatz (3) · Kosten aus Menge und Preis berechnen (3) · Dauer aus Menge und Rate berechnen (3) |
| Gleichungen und Funktionen | Lineare Gleichungen | 9 | 4 | Lineare Gleichung lösen (3) · Lösung durch Einsetzen prüfen (2) · Term zu Sachtext angeben (2) |
| Gleichungen und Funktionen | Lineare Gleichungssysteme | 6 | 3 | Lineares Gleichungssystem aufstellen (3) · Gleichung im Sachzusammenhang deuten (2) · Lineares Gleichungssystem lösen (1) |
| Gleichungen und Funktionen | Funktionen allgemein | 5 | 4 | Achseneinteilung wählen (2) · Punktprobe durchführen (1) · Graph zu Tarif zuordnen (1) |
| Gleichungen und Funktionen | Quadratische Gleichungen | 2 | 2 | Lösung durch Einsetzen prüfen (1) · Lösbarkeit quadratischer Gleichung beurteilen (1) |
| Größen und Messen | Flächeninhalt und Umfang | 26 | 18 | Term zu Figur angeben (5) · Flächeninhalt Dreieck berechnen (3) · Rechteckseite aus Fläche berechnen (2) |
| Größen und Messen | Trigonometrie im rechtwinkligen Dreieck | 19 | 4 | Seite im rechtwinkligen Dreieck berechnen (8) · Winkelfunktion Seitenverhältnis angeben (5) · Winkel im rechtwinkligen Dreieck berechnen (5) |
| Größen und Messen | Satz des Pythagoras | 17 | 7 | Pythagoras Kathete (6) · Pythagoras Gleichung zuordnen (4) · Pythagoras Hypotenuse (3) |
| Größen und Messen | Volumen und Oberfläche | 16 | 13 | Volumen Zylinder berechnen (4) · Volumen Würfel berechnen (1) · Mantelfläche Kegel berechnen (1) |
| Größen und Messen | Einheiten umrechnen | 14 | 10 | Zeiteinheiten umrechnen (3) · Größen vergleichen (2) · Strecke aus Teilstrecken berechnen (2) |
| Größen und Messen | Sinussatz | 9 | 1 | Sinussatz Seite berechnen (9) |
| Größen und Messen | Maßstab | 3 | 2 | Länge im Maßstab umrechnen (2) · Draufsicht maßstabsgerecht zeichnen (1) |
| Raum und Form | Ebene Figuren und Winkel | 19 | 10 | Winkelsumme im Dreieck anwenden (4) · Winkel im Viereck berechnen (3) · Eigenschaft einer Figur zuordnen (2) |
| Raum und Form | Körper, Netze, Schrägbilder | 12 | 9 | Netz eines Prismas vervollständigen (3) · Körper aus Netz oder Schrägbild benennen (2) · Kantenzahl eines Körpers angeben (1) |
| Raum und Form | Symmetrie und Abbildungen | 3 | 2 | Symmetrieachsen bestimmen (2) · Figur nach Spiegelung benennen (1) |
| Raum und Form | Koordinaten und Zeichnen | 1 | 1 | Lage eines Punktes zu den Achsen erkennen (1) |
| Zahlen und Operationen | Prozentrechnung | 22 | 9 | Prozentwert berechnen (5) · Prozentuale Veränderung berechnen (3) · Prozentsatz berechnen (3) |
| Zahlen und Operationen | Brüche und Dezimalzahlen | 17 | 5 | Bruchteil einer Fläche bestimmen (9) · Zahlen in verschiedenen Darstellungen vergleichen (4) · Bruchteil einer Größe berechnen (2) |
| Zahlen und Operationen | Rationale Zahlen rechnen | 7 | 5 | Termwert berechnen (3) · Zahl zu Bedingung angeben (1) · Vorzeichenregel anwenden (1) |
| Zahlen und Operationen | Potenzen und Wurzeln | 6 | 3 | Zahlen in verschiedenen Darstellungen vergleichen (3) · Exponent einer Potenz bestimmen (2) · Wurzel eines Quadrats berechnen (1) |
| Zahlen und Operationen | Zehnerpotenzen und Näherungswerte | 6 | 2 | Zehnerpotenzschreibweise umwandeln (5) · Große Zahl mit Zehnerpotenz multiplizieren (1) |
| Zahlen und Operationen | Zinsrechnung | 5 | 4 | Prozentwert berechnen (2) · Prozentsatz berechnen (1) · Guthabentabelle mit Zinsen ergänzen (1) |
| Zahlen und Operationen | Terme umformen | 2 | 1 | Term zu Sachtext angeben (2) |

### fhr

| Leitidee | Thema | Zeilen | Typen | drei häufigste Typen |
|---|---|---:|---:|---|
| Differentialrechnung | Extrem- und Sattelpunkte | 23 | 5 | Extrem- und Sattelpunkte über zweite Ableitung (17) · Gegebene Stelle als Extremstelle nachweisen (2) · Aussagen zu Stellen mit waagerechter Tangente beurteilen (2) |
| Differentialrechnung | Graph zeichnen und zuordnen | 23 | 7 | Graph ganzrationaler Funktion im Intervall zeichnen (13) · Wertetabelle erstellen (3) · Graph einer ganzrationalen Funktion zuordnen (2) |
| Differentialrechnung | Nullstellen ganzrationaler Funktionen | 19 | 10 | Nullstellen über Substitution biquadratisch (5) · Nullstelle durch Einsetzen nachweisen (3) · Nullstellen durch Ausklammern (2) |
| Differentialrechnung | Wendepunkte | 13 | 3 | Wendepunkte über zweite Ableitung (11) · Punktprobe am Graphen (1) · Steilsten Anstieg über den Wendepunkt bestimmen (1) |
| Differentialrechnung | Anstieg und Tangente | 12 | 8 | Tangentengleichung im Punkt (3) · Punktprobe am Graphen (2) · Tangenteneigenschaft einer Geraden nachweisen (2) |
| Differentialrechnung | Funktionsgleichung bestimmen | 10 | 5 | Funktionsgleichung mit Symmetriebedingung über LGS (4) · Funktionsgleichung aus drei Punkten über LGS (3) · Markante Punkte im Sachzusammenhang markieren und ablesen (1) |
| Differentialrechnung | Extremwertaufgaben | 9 | 5 | Zielfunktion aus Haupt- und Nebenbedingung aufstellen (3) · Maximum der Zielfunktion bestimmen (3) · Flächeninhalt bei gegebener Nebenbedingung berechnen (1) |
| Differentialrechnung | Schnittpunkte von Funktionsgraphen | 9 | 2 | Schnittpunkte zweier Funktionsgraphen berechnen (6) · Stelle zu gegebenem Funktionswert berechnen (3) |
| Differentialrechnung | Ableitungen bilden | 8 | 2 | Ableitung ganzrationale Funktion (6) · Verhalten im Unendlichen bestimmen (2) |
| Differentialrechnung | Symmetrie nachweisen | 6 | 1 | Symmetrie am Funktionsterm beurteilen (6) |
| Differentialrechnung | Verhalten im Unendlichen | 4 | 2 | Symmetrie am Funktionsterm beurteilen (3) · Verhalten im Unendlichen bestimmen (1) |
| Differentialrechnung | Monotonie und Krümmung | 3 | 1 | Krümmungsverhalten angeben (3) |
| Differentialrechnung | Normale | 3 | 3 | Normalengleichung im Punkt (1) · Anstieg des Graphen an einer Stelle berechnen (1) · Funktionswert an einer Stelle berechnen (1) |
| Grundlagen | Größen und Einheiten | 9 | 6 | Streckenlänge im Koordinatensystem in Meter umrechnen (3) · Funktionswert im Sachzusammenhang deuten (2) · Fläche zwischen zwei Graphen berechnen (1) |
| Grundlagen | Terme umformen | 2 | 1 | Produkt zweier Funktionsterme ausmultiplizieren (2) |
| Grundlagen | Prozentrechnung | 1 | 1 | Grundwert aus Prozentwert berechnen (1) |
| Integralrechnung | Fläche zwischen Graph und x-Achse | 12 | 3 | Fläche zwischen Graph und x-Achse berechnen (10) · Ganzzahlige Nullstellen durch Probieren finden (1) · Gesamtfläche aus mehreren Teilflächen berechnen (1) |
| Integralrechnung | Fläche zwischen zwei Graphen | 6 | 1 | Fläche zwischen zwei Graphen berechnen (6) |
| Integralrechnung | Rotationsvolumen um die x-Achse | 4 | 1 | Rotationsvolumen um die x-Achse berechnen (4) |
| Integralrechnung | Körpervolumen aus Grundfläche und Länge | 2 | 2 | Volumen aus Querschnittsfläche und Länge (1) · Länge aus Volumen und Querschnittsfläche berechnen (1) |
| Stochastik | Statistische Kenngrößen | 18 | 6 | Mittelwert aus Häufigkeitstabelle (6) · Mittelwert aus Werteliste (5) · Median aus Werteliste (3) |
| Stochastik | Mehrstufige Zufallsexperimente | 16 | 6 | Baumdiagramm mehrstufig ohne Zurücklegen darstellen (10) · Wahrscheinlichkeit über mehrere Pfade summieren (2) · Pfadregel mehrstufig mit Zurücklegen anwenden (1) |
| Stochastik | Kombinatorische Abzählverfahren | 15 | 6 | Kombination ohne Wiederholung berechnen (9) · Permutation ohne Wiederholung berechnen (2) · Kombination mit Wiederholung berechnen (1) |
| Stochastik | Daten darstellen und aufbereiten | 8 | 3 | Relative Häufigkeit berechnen (6) · Vierfeldertafel vervollständigen (1) · Mittelwert aus Häufigkeitstabelle (1) |
| Stochastik | Laplace-Wahrscheinlichkeit | 7 | 3 | Ergebnismenge eines Zufallsexperiments angeben (3) · Laplace-Wahrscheinlichkeit berechnen (3) · Laplace-Bedingung begründen (1) |
| Stochastik | Baumdiagramm und Pfadregeln | 5 | 2 | Baumdiagramm zweistufig darstellen (4) · Wahrscheinlichkeitsverteilung aufstellen (1) |
| Stochastik | Unabhängigkeit von Ereignissen | 4 | 2 | Vierfeldertafel vervollständigen (2) · Stochastische Unabhängigkeit prüfen (2) |
| Stochastik | Erwartungswert | 2 | 1 | Erwartungswert berechnen (2) |

### abi

| Leitidee | Thema | Zeilen | Typen | drei häufigste Typen |
|---|---|---:|---:|---|
| Analysis | Kurvenuntersuchung | 58 | 39 | Lage und Art aller lokalen Extrempunkte bestimmen (6) · Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen (5) · Wendepunkte über die zweite Ableitung berechnen (5) |
| Analysis | Funktionsscharen und Ortskurven | 56 | 46 | Scharparameter aus einem Punkt des Graphen angeben (4) · Parameterwerte nach der Anzahl der Extrempunkte über die Lösbarkeit der Extremstellengleichung begründen (3) · Gemeinsamen Extrempunkt einer Funktionenschar nachweisen (2) |
| Analysis | Funktionsklassen und Eigenschaften | 53 | 33 | Symmetrie: Symmetrieart am Term über die Exponenten begründen (6) · Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen (6) · Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen (4) |
| Analysis | Tangente, Normale, Schnittwinkel | 51 | 44 | Tangentengleichung in einem Punkt des Graphen aufstellen (5) · Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen (2) · Schnittwinkel zweier Graphen im gemeinsamen Punkt über die Tangentensteigungen berechnen (2) |
| Analysis | Flächeninhalt durch Integration | 42 | 33 | Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen (7) · Integralwert: Mittelwert einer Funktion als Integral geteilt durch die Intervalllänge berechnen und deuten (3) · Fläche: Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen (2) |
| Analysis | Ableitung und Änderungsrate | 23 | 20 | Sekantengleichung durch zwei Punkte eines Graphen ermitteln (2) · Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen (2) · Mittlere Änderungsrate aus dem Funktionsterm im Sachzusammenhang berechnen (2) |
| Analysis | Stammfunktion und Hauptsatz | 21 | 15 | Stammfunktion durch Ableiten nachweisen (5) · Aussage über Extrempunkte einer Stammfunktion beurteilen (2) · Extremstelle aller Stammfunktionen über den Vorzeichenwechsel der gegebenen Ableitung begründen (2) |
| Analysis | Gleichungen lösen | 15 | 12 | Lösungsmenge einer Ungleichung zwischen zwei Funktionstermen über die faktorisierte Differenz bestimmen (2) · Schnittstelle von Graph und Ableitungsgraph nachweisen (2) · Schnittstellen zweier Graphen durch Lösen einer quadratischen Gleichung nachweisen (2) |
| Analysis | Rekonstruktion von Funktionsgleichungen | 15 | 11 | Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren (3) · Funktionsgleichung aus knickfreiem Übergang und einer Wertbedingung rekonstruieren (2) · Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren (2) |
| Analysis | Grenzwerte und Verhalten im Unendlichen | 12 | 4 | Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (5) · Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (3) · Grenzverhalten einer ganzrationalen Funktion angeben (3) |
| Analysis | Ableitungsgraph und Funktionsgraph | 11 | 10 | Graphen von Funktion und Ableitung einander zuordnen (2) · Beziehung f'(a) · f''(a) = −1 als Orthogonalität der Tangenten an Graph und Ableitungsgraph deuten (1) · Sattelpunkt über die Berührnullstelle des Ableitungsgraphen begründen (1) |
| Analysis | Rekonstruktion von Beständen | 8 | 7 | Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten (2) · Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen (1) · Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen (1) |
| Analysis | Ableitungsregeln | 7 | 4 | Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen (4) · Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden (1) · Ableitungsfunktion und Stammfunktion einer ganzrationalen Funktion angeben (1) |
| Analysis | Extremalprobleme | 7 | 4 | Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen (4) · Dreieck zu Schnittpunkten mit einer Parallelen zur x-Achse einzeichnen (1) · Achsenparalleles Rechteck maximaler Fläche zwischen Ursprung und Graphenpunkt bestimmen (1) |
| Analysis | Rotationsvolumen | 4 | 3 | Umbeschriebenes Prisma zu einem Rotationskörper bestimmen (2) · Integralfunktion im Sachzusammenhang deuten (1) · Fehlerhaftes Verfahren zur Volumenberechnung beurteilen und berichtigen (1) |
| Analysis | Integrationsregeln | 1 | 1 | Integral über eine vorgegebene Regel für g' · e^g berechnen (1) |
| Analysis | Umkehrfunktion | 1 | 1 | Flächenbeziehung zwischen Funktion und Umkehrfunktion über die Spiegelung an y = x beurteilen (1) |
| Analysis | Uneigentliche Integrale | 1 | 1 | Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten (1) |
| Analytische Geometrie | Abstände | 27 | 20 | Streckenlänge im Raum berechnen (3) · Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen (3) · Abstand zweier Punkte auf parallelen Ebenen mit dem Abstand der Ebenen vergleichen (2) |
| Analytische Geometrie | Flächeninhalt und Volumen im Raum | 26 | 22 | Körper: Pyramidenvolumen aus Grundfläche und Höhe berechnen (2) · Körper: Trapezgrundfläche nachweisen und Pyramidenvolumen berechnen (2) · Ebene Figur: Parameter einer Ecke aus dem Flächeninhalt eines gleichschenkligen Dreiecks bestimmen (2) |
| Analytische Geometrie | Punkte und Strecken im Koordinatensystem | 24 | 22 | Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen (2) · Ebene Figur: Gleichschenkligkeit oder Gleichseitigkeit eines Dreiecks über die Seitenlängen prüfen (2) · Ebene Figur: Benachbarte Ecke eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen (1) |
| Analytische Geometrie | Scharen von Geraden und Ebenen | 22 | 21 | Zugehörigkeit einer Ebene zu einer Schar prüfen (2) · Parameter einer Geradenschar aus einem vorgegebenen Durchstoßpunkt bestimmen (1) · Ganzzahligen Scharparameter aus einer Bereichsbedingung an den Durchstoßpunkt bestimmen (1) |
| Analytische Geometrie | Ebenen | 20 | 10 | Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen (9) · Parametergleichung einer Ebene aus Punkten angeben (2) · Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen (2) |
| Analytische Geometrie | Geraden | 15 | 12 | Punktprobe an einer Geraden durchführen (4) · Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen (1) · Existenz eines Geradenschnittpunkts über die gemeinsame Ebene begründen (1) |
| Analytische Geometrie | Orthogonalität | 14 | 11 | Geraden und Ebenen: Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen (2) · Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen (2) · Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen (2) |
| Analytische Geometrie | Schnittmengen | 14 | 12 | Schnittpunkt von Gerade und Ebene berechnen (3) · Gegebene Rechnung zum Geradenschnittpunkt erläutern (1) · Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen (1) |
| Analytische Geometrie | Skalarprodukt und Winkel | 14 | 5 | Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen (8) · Winkel zwischen zwei Kanten über das Skalarprodukt berechnen (3) · Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen (1) |
| Analytische Geometrie | Lagebeziehungen | 13 | 7 | Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen (5) · Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen (2) · Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen (2) |
| Analytische Geometrie | Spiegelung | 7 | 6 | Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen (2) · Spiegelpunkt an einem Punkt bestimmen (1) · Spiegelpunkt an einer Ebene über die Lotgerade bestimmen (1) |
| Analytische Geometrie | Linearkombination und lineare Abhängigkeit | 1 | 1 | Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen (1) |
| Analytische Geometrie | Vektoren und Rechenoperationen | 1 | 1 | Lage eines Punktes zu einem Vektorterm im Quader beschreiben (1) |
| Stochastik | Binomialverteilung | 57 | 30 | Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln (7) · Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen (6) · Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln (6) |
| Stochastik | Baumdiagramm und Pfadregeln | 42 | 30 | Baumdiagramm zu einer zweistufigen Situation erstellen (4) · Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen (4) · Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen (3) |
| Stochastik | Zufallsexperimente und Urnenmodelle | 34 | 20 | Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben (6) · Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen (4) · Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen (4) |
| Stochastik | Kenngrößen von Verteilungen | 23 | 13 | Unbekannte Größe aus einer Erwartungswertbedingung bestimmen (7) · Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen (5) · Summand eines Erwartungswertterms im Sachzusammenhang deuten (1) |
| Stochastik | Bedingte Wahrscheinlichkeit und Bayes | 11 | 4 | Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen (4) · Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen (3) · Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen (3) |
| Stochastik | Hypothesentests | 10 | 6 | Entscheidungsregel eines einseitigen Signifikanztests bestimmen (3) · Wahl der Nullhypothese aus der Sicht des Entscheiders begründen (2) · Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen (2) |
| Stochastik | Unabhängigkeit | 8 | 7 | Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen (2) · Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen (1) · Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen (1) |
| Stochastik | Vierfeldertafel | 8 | 3 | Vierfeldertafel aus Anteilen vervollständigen (6) · Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen (1) · Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen (1) |
| Stochastik | Hypergeometrische Verteilung | 5 | 3 | Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen (3) · Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen (1) · Größte Trefferzahl, bis zu der die kumulierte hypergeometrische Wahrscheinlichkeit unter einer Schranke bleibt, ermitteln (1) |
| Stochastik | Ereignisse und Mengenoperationen | 4 | 3 | Anteil für genau eines von zwei Ereignissen aus Anteilen und Schnitt berechnen (2) · Term P(A) + P(B) − 2 · P(A ∩ B) als Wahrscheinlichkeit für genau eines der Ereignisse deuten (1) · Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben (1) |
| Stochastik | Kombinatorik | 4 | 4 | Auswahlen mit Abstandsbedingung aufzählen (1) · Anzahl der Sitzordnungen mit Abstandsbedingung berechnen (1) · Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen (1) |
| Stochastik | Normalverteilung und Sigma-Regeln | 3 | 3 | Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen (1) · Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen (1) · Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen (1) |
| Stochastik | Zufallsgrößen und Verteilungen | 1 | 1 | Wahrscheinlichkeit eines Ereignisses aus einer symmetrischen Verteilung und einem Einzelwert bestimmen (1) |

### iqb

| Leitidee | Thema | Zeilen | Typen | drei häufigste Typen |
|---|---|---:|---:|---|
| Analysis | Funktionsklassen und Eigenschaften | 99 | 73 | Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen (8) · Transformation: Abbildung zwischen zwei Graphen angeben (5) · Symmetrie: Symmetrieart am Term über die Exponenten begründen (5) |
| Analysis | Funktionsscharen und Ortskurven | 86 | 76 | Scharparameter aus einem Punkt des Graphen angeben (5) · Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen (2) · Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen (2) |
| Analysis | Flächeninhalt durch Integration | 62 | 49 | Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen (7) · Integralwert: Integral mit Wert null am Graphen begründen (2) · Integralwert: Integralwert grafisch durch Kästchenzählen bestimmen (2) |
| Analysis | Tangente, Normale, Schnittwinkel | 61 | 48 | Tangentengleichung in einem Punkt des Graphen aufstellen (6) · Tangentengleichung aus der Abbildung ablesen (2) · y-Achsenabschnitt der Tangente allgemein nachweisen (2) |
| Analysis | Kurvenuntersuchung | 53 | 37 | Extrempunkt an vorgegebener Stelle nachweisen (6) · Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen (3) · Verlauf eines Graphen im Sachzusammenhang beschreiben (3) |
| Analysis | Ableitung und Änderungsrate | 31 | 26 | Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion berechnen (3) · Zeitpunkt der größten Rate aus der Ableitung angeben (2) · Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen (2) |
| Analysis | Stammfunktion und Hauptsatz | 31 | 21 | Bestimmtes Integral einer ganzrationalen Funktion berechnen (3) · Stammfunktion mit einer Wertebedingung bestimmen (3) · Stammfunktion durch Ableiten nachweisen (3) |
| Analysis | Gleichungen lösen | 19 | 19 | Nullstelle einer Logarithmusfunktion berechnen (1) · Schnittstellen zweier Graphen über den gemeinsamen Exponentialfaktor nachweisen (1) · Gleichung aus Differenzenquotient und Ableitung lösen (1) |
| Analysis | Rekonstruktion von Beständen | 19 | 16 | Term für einen Bestand aus einer Rate über ein Integral angeben (2) · Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten (2) · Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen (2) |
| Analysis | Ableitungsgraph und Funktionsgraph | 10 | 7 | Graphen von Funktion und Ableitung einander zuordnen (3) · Monotonie aus dem Vorzeichen der Ableitung am Graphen begründen (2) · Tangentensteigung aus dem Graphen der Ableitung ablesen (1) |
| Analysis | Rekonstruktion von Funktionsgleichungen | 10 | 10 | Parameter einer Logarithmusfunktion aus Asymptote und Punkt ermitteln (1) · Parameter einer Linearkombination aus Funktion und Gerade aus zwei Punkten bestimmen (1) · Steigung einer aus Periode und Extrempunkt rekonstruierten Kosinusfunktion allgemein bestimmen (1) |
| Analysis | Ableitungsregeln | 9 | 8 | Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen (2) · Ableitung eines Produkts aus Graphenwerten mit der Produktregel bestimmen (1) · Bedingung für eine waagerechte Tangente eines Produkts mit e^x nachweisen (1) |
| Analysis | Extremalprobleme | 7 | 6 | Parameter für den größten Flächeninhalt über die Ableitung bestimmen (2) · Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen (1) · Aufgabenstellung zu einer Extremwertaufgabe mit Dreiecksfläche aus dem Lösungsweg formulieren und Schritte erläutern (1) |
| Analysis | Grenzwerte und Verhalten im Unendlichen | 6 | 4 | Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (2) · Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben (2) · Monotonie, Nullstelle und Grenzwert einer e-Funktion am Term begründen (1) |
| Analysis | Rotationsvolumen | 5 | 5 | Rotationsvolumen über einbeschriebene Zylinder abschätzen (1) · Aufgabenstellung zu einem Rotationsvolumen-Anteil aus dem Lösungsweg formulieren (1) · Integranden als Querschnittsfläche über den Satz des Pythagoras deuten und Umrechnungsfaktor erläutern (1) |
| Analysis | Umkehrfunktion | 5 | 5 | Flächenbeziehung zwischen Funktion und Umkehrfunktion über die Spiegelung an y = x beurteilen (1) · Definitionsbereich der Umkehrfunktion angeben und ihren Term nachweisen (1) · Tangente an Funktion und Umkehrfunktion über die Spiegelung an y = x begründen (1) |
| Analysis | Integrationsregeln | 1 | 1 | Integral über eine vorgegebene Regel für g' · e^g berechnen (1) |
| Analysis | Uneigentliche Integrale | 1 | 1 | Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten (1) |
| Analytische Geometrie | Matrizen und Übergangsprozesse | 154 | 115 | Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen (9) · Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten (5) · Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen (4) |
| Analytische Geometrie | Punkte und Strecken im Koordinatensystem | 59 | 50 | Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen (4) · Körper: Koordinaten eines Eckpunkts eines Prismas angeben (3) · Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen (2) |
| Analytische Geometrie | Flächeninhalt und Volumen im Raum | 52 | 45 | Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen (4) · Körper: Höhe einer Pyramide aus dem Volumen bestimmen (2) · Ebene Figur: Parameter eines Punktes aus einer Flächengleichheit bestimmen (2) |
| Analytische Geometrie | Abstände | 31 | 25 | Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen (4) · Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen (3) · Streckenlänge im Raum berechnen (2) |
| Analytische Geometrie | Orthogonalität | 29 | 19 | Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen (4) · Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen (3) · Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln (3) |
| Analytische Geometrie | Ebenen | 28 | 16 | Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen (11) · Lage einer Ebene zu einer Koordinatenachse aus der Koordinatengleichung begründen (2) · Achsenparallele Ebene einer Bewegung aus der Parameterdarstellung angeben (2) |
| Analytische Geometrie | Skalarprodukt und Winkel | 28 | 17 | Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen (9) · Winkel zwischen zwei Kanten über das Skalarprodukt berechnen (3) · Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen (2) |
| Analytische Geometrie | Scharen von Geraden und Ebenen | 27 | 24 | Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben (3) · Scharparameter für einen vorgegebenen Winkel zwischen Ebene und Scharebene berechnen (2) · Identität aller Geraden einer Schar beurteilen (1) |
| Analytische Geometrie | Lagebeziehungen | 25 | 15 | Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen (5) · Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen (5) · Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen (2) |
| Analytische Geometrie | Geraden | 21 | 14 | Punktprobe an einer Geraden durchführen (7) · Geradengleichung durch zwei Punkte aufstellen und windschiefe Lage begründen (2) · Parametergleichung einer Strecke im Sachzusammenhang deuten (1) |
| Analytische Geometrie | Spiegelung | 20 | 15 | Symmetrieebenen eines Körpers aus den Koordinaten begründen (3) · Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen (3) · Spiegelebene aus Punkt und Spiegelpunkt bestimmen (2) |
| Analytische Geometrie | Vektoren und Rechenoperationen | 19 | 16 | Koordinate eines Vektors aus vorgegebener Länge bestimmen (2) · Punkt zu einem Vektorterm in das Schrägbild einzeichnen (2) · Verbindungsvektor zweier Kantenmittelpunkte als Linearkombination der Kantenvektoren angeben (2) |
| Analytische Geometrie | Schnittmengen | 17 | 11 | Schnittpunkt von Gerade und Ebene berechnen (3) · Parameter aus dem Schnitt zweier Geraden ermitteln (2) · Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen (2) |
| Analytische Geometrie | Lineare Gleichungssysteme | 14 | 12 | Lösbarkeit eines Gleichungssystems mit Parameter beurteilen (2) · Lösungsanzahl eines gestaffelten Gleichungssystems mit Parameter durch Fallunterscheidung begründen (2) · Lösung eines unterbestimmten Gleichungssystems unter Zusatzbedingungen auswählen (1) |
| Stochastik | Binomialverteilung | 98 | 52 | Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln (16) · Kumulierte Binomialsumme als Sachaussage formulieren (7) · Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben (5) |
| Stochastik | Baumdiagramm und Pfadregeln | 61 | 36 | Baumdiagramm zu einer zweistufigen Situation erstellen (7) · Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen (4) · Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen (4) |
| Stochastik | Zufallsexperimente und Urnenmodelle | 59 | 30 | Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben (15) · Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen (5) · Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen (4) |
| Stochastik | Kenngrößen von Verteilungen | 48 | 32 | Unbekannte Größe aus einer Erwartungswertbedingung bestimmen (13) · Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln (3) · Erwartungswert der Auszahlung mit dem Einsatz vergleichen (2) |
| Stochastik | Bedingte Wahrscheinlichkeit und Bayes | 28 | 12 | Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen (8) · Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen (5) · Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen (3) |
| Stochastik | Vierfeldertafel | 21 | 8 | Vierfeldertafel aus Anteilen vervollständigen (13) · Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen (2) · Vierfeldertafel mit Parameter vervollständigen und einen Parameterwert ausschließen (1) |
| Stochastik | Normalverteilung und Sigma-Regeln | 17 | 15 | Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen (3) · Wahrscheinlichkeit eines Einzelwerts einer stetigen Zufallsgröße angeben (1) · Näherung einer Normalverteilungswahrscheinlichkeit über Rechteck und Symmetrie erläutern (1) |
| Stochastik | Unabhängigkeit | 15 | 8 | Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen (5) · Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen (2) · Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen (2) |
| Stochastik | Kombinatorik | 13 | 12 | Anzahl der Sitzordnungen mit Abstandsbedingung berechnen (2) · Auswahlen mit Abstandsbedingung aufzählen (1) · Term für die Wahrscheinlichkeit aufstellen, dass jede Zahl mindestens einmal fällt (1) |
| Stochastik | Hypothesentests | 12 | 8 | Entscheidungsregel eines einseitigen Signifikanztests bestimmen (3) · Wahl der Nullhypothese aus der Sicht des Entscheiders begründen (3) · Fehler zweiter Art aus dem Graphen der Ablehnwahrscheinlichkeit ermitteln (1) |
| Stochastik | Konfidenzintervalle | 12 | 9 | Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben (2) · Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen (2) · Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen (2) |
| Stochastik | Ereignisse und Mengenoperationen | 9 | 6 | Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben (2) · Anteil für genau eines von zwei Ereignissen aus Anteilen und Schnitt berechnen (2) · Anteil eines Entweder-oder-Ereignisses aus einer Tafel berechnen (2) |
| Stochastik | Zufallsgrößen und Verteilungen | 5 | 5 | Wahrscheinlichkeitsverteilung über ein unmögliches Ergebnis vervollständigen (1) · Verteilungen zweier Zufallsgrößen den Säulendiagrammen zuordnen (1) · Wahrscheinlichkeit p aus der Summe 1 im Diagramm nachweisen (1) |
| Stochastik | Lage- und Streumaße einer Stichprobe | 4 | 4 | Fehlenden Wert aus dem arithmetischen Mittel berechnen (1) · Medianklasse aus einem Säulendiagramm relativer Häufigkeiten begründen (1) · Gewichtete Summe der Intervallgrenzen als Schranke des Mittelwerts deuten (1) |
| Stochastik | Hypergeometrische Verteilung | 2 | 1 | Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen (2) |

## 3 Namensgleiche Themen

Themenname wortgleich in mehr als einem Profil:

| Thema | Profile |
|---|---|
| Ableitung und Änderungsrate | abi, iqb |
| Ableitungsgraph und Funktionsgraph | abi, iqb |
| Ableitungsregeln | abi, iqb |
| Abstände | abi, iqb |
| Baumdiagramm und Pfadregeln | fhr, abi, iqb |
| Bedingte Wahrscheinlichkeit und Bayes | abi, iqb |
| Binomialverteilung | abi, iqb |
| Ebenen | abi, iqb |
| Ereignisse und Mengenoperationen | abi, iqb |
| Extremalprobleme | abi, iqb |
| Flächeninhalt durch Integration | abi, iqb |
| Flächeninhalt und Volumen im Raum | abi, iqb |
| Funktionsklassen und Eigenschaften | abi, iqb |
| Funktionsscharen und Ortskurven | abi, iqb |
| Geraden | abi, iqb |
| Gleichungen lösen | abi, iqb |
| Grenzwerte und Verhalten im Unendlichen | abi, iqb |
| Hypergeometrische Verteilung | abi, iqb |
| Hypothesentests | abi, iqb |
| Integrationsregeln | abi, iqb |
| Kenngrößen von Verteilungen | abi, iqb |
| Kombinatorik | abi, iqb |
| Kurvenuntersuchung | abi, iqb |
| Lagebeziehungen | abi, iqb |
| Lineare Gleichungssysteme | msa, iqb |
| Normalverteilung und Sigma-Regeln | abi, iqb |
| Orthogonalität | abi, iqb |
| Prozentrechnung | msa, fhr |
| Punkte und Strecken im Koordinatensystem | abi, iqb |
| Rekonstruktion von Beständen | abi, iqb |
| Rekonstruktion von Funktionsgleichungen | abi, iqb |
| Rotationsvolumen | abi, iqb |
| Scharen von Geraden und Ebenen | abi, iqb |
| Schnittmengen | abi, iqb |
| Skalarprodukt und Winkel | abi, iqb |
| Spiegelung | abi, iqb |
| Stammfunktion und Hauptsatz | abi, iqb |
| Tangente, Normale, Schnittwinkel | abi, iqb |
| Terme umformen | msa, fhr |
| Umkehrfunktion | abi, iqb |
| Unabhängigkeit | abi, iqb |
| Uneigentliche Integrale | abi, iqb |
| Vektoren und Rechenoperationen | abi, iqb |
| Vierfeldertafel | abi, iqb |
| Zufallsexperimente und Urnenmodelle | abi, iqb |
| Zufallsgrößen und Verteilungen | abi, iqb |

46 namensgleiche Themen.

## 4 Sek-I-Referenz (Dateinamen in katalog/)

| Name | wortgleich als Thema in |
|---|---|
| binomische-formeln | – |
| bruchrechnung | – |
| brueche-dezimalzahlen | – |
| daten | – |
| einheiten | – |
| flaechen | – |
| koerper | – |
| kreis | – |
| lineare-funktionen | – |
| lineare-gleichungen | – |
| lineare-gleichungssysteme | – |
| potenz-exponentialfunktionen | – |
| potenzen-wurzeln | – |
| prozentrechnung | – |
| pyramide-kegel-kugel | – |
| pythagoras | – |
| quadratische-funktionen | – |
| quadratische-gleichungen | – |
| rationale-zahlen | – |
| reelle-zahlen | – |
| strahlensaetze | – |
| symmetrie-abbildungen | – |
| terme | – |
| trigonometrie | – |
| trigonometrische-funktionen | – |
| wahrscheinlichkeit | – |
| winkel-dreiecke | – |
| zinsrechnung | – |
| zuordnungen | – |

29 Namen, 0 mit Treffer, 29 ohne.

## 5 Befunde

Paare (Leitidee, Thema) je Typenliste gegen die Kataloge der Profile, die sie abdeckt.

### `msa/msa-typen.csv` gegen msa

In der Typenliste, in keinem Katalog (0):

- keine

Im Katalog, nicht in der Typenliste (0):

- keine

### `fhr/fhr-typen.csv` gegen fhr

In der Typenliste, in keinem Katalog (1):

- Grundlagen / Gleichungen lösen

Im Katalog, nicht in der Typenliste (0):

- keine

### `abitur/abitur-typen.csv` gegen abi, iqb

In der Typenliste, in keinem Katalog (1):

- Analysis / Lineare Gleichungssysteme

Im Katalog, nicht in der Typenliste (0):

- keine
