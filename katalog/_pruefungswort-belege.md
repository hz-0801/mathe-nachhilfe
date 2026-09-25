# Prüfungswort-Belege je Lerneinheit und Typ
Abgeleitet von `werkzeuge/pruefungswort-belege.py` aus den Einträgen, `themen.csv`, den msa-, abi- und fhr-Katalogen und den Zuordnungsdaten `werkzeuge/pruefungswort-belege-daten.py`, nie von Hand ändern.
Eingaben auf Stand unbekannt. Die Datei schlägt vor, sie entscheidet nicht: die Schwelle „oft“ setzt der Lehrer.

Lesart (Einzelheiten im Skriptkopf): Die P10-Typen einer Einheit sind die der Zuordnungszeile des Eintrags und die, die eine Typzuordnung nennt; ein P10-Typ prüft einen Katalogtyp, wenn dessen Fertigkeit Teil der Leistung ist, die der P10-Typ verlangt (Definition oder Original, Vorstufen desselben Verfahrens eingeschlossen); nicht wortgleiche Zuordnungen tragen einen Grund. Gezählt werden nur P10-Typen der Themen, die `themen.csv` dem Eintrag zuweist, und der Themen, aus denen seine Zuordnungszeile Typen führt; P10-Typen fremder Themen stehen als Hinweis da und zählen nicht, „Behauptung prüfen“ (themenübergreifend) zählt nie. „P10-Jahrgänge“ = Jahre 2014–2026, in denen ein P10-Typ der Einheit als Haupt- oder Nebenleistung vorkam (msa-katalog-basis/-kontext wie `ertrag.py`, ohne GYM); „davon Haupt“ nur als Hauptleistung.

## Zahlenblock

- Sek I: 29 Einträge, 116 Lerneinheiten (ohne Sek-II-Einheiten), 1334 Typen; Einheiten mit P10-Typ 93, ohne P10-Typ 23; Typen mit P10-Typ 650, ohne 684 (davon 196 nur mit P10-Typen fremder Themen, zählen nicht).
- Sek II: 47 Einträge mit Sek-II-Typen (davon 3 Sek-I-Einträge mit Sek-II-Teil), 162 Einheiten.

## Verteilung für die Schwelle „oft“ – Sek-I-Einheiten

Sortiert nach P10-Jahrgängen (Haupt oder Neben), dann nach Summe ertrag.

| Eintrag | Einheit | P10-Jahrgänge (von 13) | davon Haupt | P10-Typen | Summe ertrag |
|---|---|---|---|---|---|
| trigonometrie | 4 · Sinussatz | 13 | 13 | 5 | 52 |
| trigonometrie | 1 · Seite berechnen mit Sinus, Kosinus und Tangens | 13 | 11 | 5 | 42 |
| trigonometrie | 2 · Winkel berechnen | 13 | 10 | 3 | 36 |
| trigonometrie | 3 · Rechtwinklige Teildreiecke in Figuren und Vermessung | 13 | 10 | 4 | 36 |
| lineare-funktionen | 3 · Punkte und Werte | 13 | 10 | 8 | 33 |
| daten | 4 · Kenngrößen | 12 | 12 | 8 | 45 |
| prozentrechnung | 5 · Prozentuale Veränderung | 12 | 11 | 6 | 25 |
| daten | 2 · Säulen-, Balken- und Liniendiagramme | 11 | 11 | 7 | 43 |
| quadratische-funktionen | 2 · Scheitelpunktform | 11 | 11 | 11 | 29 |
| prozentrechnung | 2 · Prozentsatz berechnen | 11 | 8 | 2 | 19 |
| terme | 1 · Terme aufstellen und berechnen | 11 | 11 | 5 | 19 |
| winkel-dreiecke | 2 · Winkel an Geradenkreuzungen und Parallelen | 11 | 11 | 6 | 17 |
| winkel-dreiecke | 3 · Winkelsummen, Dreiecke und Vierecke | 11 | 9 | 6 | 17 |
| brueche-dezimalzahlen | 1 · Bruch als Anteil | 11 | 11 | 2 | 13 |
| wahrscheinlichkeit | 2 · Wahrscheinlichkeit einstufig | 10 | 9 | 5 | 36 |
| pythagoras | 1 · Satz und Hypotenuse | 10 | 9 | 4 | 30 |
| quadratische-funktionen | 3 · Normalform | 10 | 9 | 5 | 18 |
| quadratische-funktionen | 1 · Normalparabel und Streckfaktor | 10 | 10 | 6 | 16 |
| flaechen | 1 · Rechteck, Quadrat, Umfang | 10 | 9 | 7 | 15 |
| wahrscheinlichkeit | 4 · Ohne Zurücklegen | 9 | 8 | 5 | 46 |
| lineare-funktionen | 2 · Lineare Funktion f(x) = m·x + n | 9 | 9 | 8 | 33 |
| lineare-funktionen | 1 · Proportionale Funktion | 9 | 8 | 3 | 30 |
| pythagoras | 3 · Pythagoras in Figuren und Körpern | 9 | 8 | 5 | 30 |
| prozentrechnung | 4 · Grundwert berechnen | 9 | 9 | 3 | 22 |
| kreis | 2 · Kreisfläche | 9 | 7 | 4 | 12 |
| brueche-dezimalzahlen | 2 · Kürzen und Erweitern | 9 | 9 | 1 | 11 |
| wahrscheinlichkeit | 3 · Baumdiagramm und Pfadregeln | 8 | 8 | 6 | 43 |
| lineare-funktionen | 5 · Anwendungen | 8 | 5 | 6 | 28 |
| quadratische-funktionen | 4 · Nullstellen und Schnittpunkte berechnen | 8 | 7 | 5 | 24 |
| pythagoras | 2 · Kathete und Umkehrung | 8 | 8 | 3 | 22 |
| flaechen | 5 · Zusammengesetzte Figuren | 8 | 8 | 6 | 20 |
| koerper | 1 · Körper erkennen, Netze, Schrägbilder | 8 | 8 | 8 | 18 |
| prozentrechnung | 1 · Prozente als Anteile | 8 | 6 | 4 | 10 |
| brueche-dezimalzahlen | 4 · Dezimalzahlen | 8 | 8 | 2 | 8 |
| brueche-dezimalzahlen | 5 · Vergleichen, Ordnen, Runden | 8 | 8 | 2 | 8 |
| potenz-exponentialfunktionen | 1 · Lineares und exponentielles Wachstum unterscheiden | 7 | 7 | 6 | 36 |
| potenz-exponentialfunktionen | 2 · Wachstumsfaktor und Wachstumstabelle | 7 | 7 | 4 | 23 |
| quadratische-gleichungen | 3 · Normalform und p-q-Formel | 7 | 6 | 3 | 22 |
| flaechen | 3 · Dreieck | 7 | 7 | 3 | 21 |
| zuordnungen | 4 · Zuordnungstypen erkennen und anwenden | 7 | 6 | 4 | 21 |
| koerper | 2 · Quader und Würfel | 7 | 5 | 6 | 17 |
| daten | 3 · Streifen- und Kreisdiagramm | 7 | 4 | 4 | 11 |
| potenzen-wurzeln | 1 · Potenzen | 7 | 7 | 4 | 9 |
| brueche-dezimalzahlen | 3 · Brüche vergleichen | 7 | 7 | 1 | 7 |
| koerper | 4 · Zylinder | 6 | 5 | 8 | 29 |
| lineare-gleichungssysteme | 4 · Sachaufgaben | 6 | 5 | 3 | 25 |
| wahrscheinlichkeit | 1 · Zählen und Ergebnismengen | 6 | 5 | 6 | 13 |
| prozentrechnung | 3 · Prozentwert berechnen | 6 | 6 | 1 | 9 |
| zuordnungen | 2 · Proportionale Zuordnungen und Dreisatz | 6 | 5 | 2 | 8 |
| lineare-gleichungen | 1 · Gleichungen verstehen | 6 | 6 | 2 | 6 |
| winkel-dreiecke | 1 · Winkel messen und zeichnen | 6 | 3 | 3 | 5 |
| einheiten | 2 · Zeit | 6 | 4 | 2 | 4 |
| zuordnungen | 1 · Zuordnungen darstellen | 5 | 5 | 3 | 17 |
| quadratische-gleichungen | 1 · Wurzelziehen und Lösbarkeit | 5 | 4 | 3 | 13 |
| daten | 5 · Diagramme beurteilen und Boxplot | 5 | 5 | 2 | 11 |
| einheiten | 4 · Mit Größen rechnen im Sachzusammenhang | 5 | 4 | 6 | 10 |
| lineare-gleichungen | 4 · Gleichungen aufstellen | 5 | 4 | 2 | 8 |
| potenz-exponentialfunktionen | 3 · Exponentialfunktion aufstellen und auswerten | 5 | 3 | 3 | 6 |
| potenzen-wurzeln | 2 · Zehnerpotenzen | 5 | 5 | 2 | 6 |
| terme | 2 · Terme zusammenfassen | 5 | 5 | 4 | 5 |
| kreis | 1 · Kreisumfang | 5 | 2 | 2 | 4 |
| lineare-gleichungen | 2 · Äquivalenzumformungen | 5 | 3 | 1 | 3 |
| lineare-gleichungen | 3 · Gleichungen mit x auf beiden Seiten, Klammern, Brüchen und Dezimalzahlen; Sonderfälle keine/alle Lösungen. | 5 | 3 | 1 | 3 |
| quadratische-gleichungen | 2 · Satz vom Nullprodukt | 4 | 3 | 2 | 10 |
| daten | 1 · Häufigkeiten | 4 | 4 | 5 | 9 |
| einheiten | 1 · Länge, Masse, Geld | 4 | 4 | 4 | 8 |
| rationale-zahlen | 4 · Terme und Sachaufgaben | 4 | 4 | 3 | 7 |
| symmetrie-abbildungen | 2 · Achsensymmetrie und Spiegeln | 4 | 4 | 2 | 7 |
| rationale-zahlen | 3 · Multiplizieren und Dividieren | 4 | 4 | 2 | 5 |
| zuordnungen | 3 · Antiproportionale Zuordnungen | 4 | 2 | 2 | 5 |
| lineare-gleichungssysteme | 1 · Gleichungen mit zwei Variablen und grafisches Lösen | 4 | 1 | 1 | 3 |
| lineare-gleichungssysteme | 2 · Einsetzungsverfahren | 4 | 1 | 1 | 3 |
| pyramide-kegel-kugel | 2 · Kegel | 3 | 3 | 5 | 14 |
| koerper | 3 · Prisma | 3 | 3 | 4 | 12 |
| flaechen | 4 · Trapez, Drachenviereck, Raute | 3 | 3 | 4 | 10 |
| lineare-funktionen | 4 · Gleichung bestimmen | 3 | 3 | 6 | 10 |
| strahlensaetze | 1 · Maßstab | 3 | 3 | 2 | 9 |
| einheiten | 3 · Flächen- und Volumeneinheiten | 3 | 3 | 3 | 8 |
| koerper | 5 · Zusammengesetzte Körper und Anwendungen | 3 | 3 | 5 | 8 |
| potenz-exponentialfunktionen | 4 · Verdopplungs- und Halbwertszeit | 3 | 3 | 5 | 6 |
| rationale-zahlen | 2 · Addieren und Subtrahieren | 3 | 3 | 1 | 4 |
| pyramide-kegel-kugel | 3 · Kugel | 2 | 2 | 6 | 6 |
| kreis | 3 · Kreisteile | 2 | 2 | 3 | 5 |
| potenzen-wurzeln | 3 · Quadratwurzeln | 2 | 2 | 2 | 2 |
| rationale-zahlen | 1 · Negative Zahlen kennen und ordnen | 2 | 2 | 1 | 2 |
| binomische-formeln | 2 · Binomische Formeln | 1 | 1 | 1 | 4 |
| zinsrechnung | 2 · Zinseszins und Guthabentabelle | 1 | 1 | 2 | 4 |
| winkel-dreiecke | 5 · Besondere Linien im Dreieck und Satz des Thales | 1 | 1 | 2 | 2 |
| zinsrechnung | 1 · Jahreszins, Monats- und Tageszins | 1 | 1 | 1 | 2 |
| symmetrie-abbildungen | 1 · Koordinatensystem | 1 | 1 | 1 | 1 |
| winkel-dreiecke | 4 · Dreiecke konstruieren | 1 | 1 | 2 | 1 |
| binomische-formeln | 1 · Summe mal Summe | 0 | 0 | 0 | 0 |
| binomische-formeln | 3 · Faktorisieren | 0 | 0 | 0 | 0 |
| bruchrechnung | 1 · Brüche addieren und subtrahieren | 0 | 0 | 0 | 0 |
| bruchrechnung | 2 · Dezimalzahlen addieren und subtrahieren | 0 | 0 | 0 | 0 |
| bruchrechnung | 3 · Brüche multiplizieren und dividieren | 0 | 0 | 0 | 0 |
| bruchrechnung | 4 · Dezimalzahlen multiplizieren und dividieren | 0 | 0 | 0 | 0 |
| bruchrechnung | 5 · Rechengesetze und Punkt vor Strich | 0 | 0 | 0 | 0 |
| daten | 7 · Vierfeldertafel (Sek I) | 0 | 0 | 0 | 0 |
| flaechen | 2 · Parallelogramm | 0 | 0 | 0 | 0 |
| lineare-gleichungssysteme | 3 · Additionsverfahren | 0 | 0 | 0 | 0 |
| potenz-exponentialfunktionen | 5 · Potenzfunktionen mit natürlichem Exponenten | 0 | 0 | 0 | 0 |
| pyramide-kegel-kugel | 1 · Pyramide | 0 | 0 | 1 | 0 |
| quadratische-gleichungen | 4 · Sachaufgaben | 0 | 0 | 0 | 0 |
| reelle-zahlen | 1 · Irrationale Zahlen und Zahlbereiche | 0 | 0 | 0 | 0 |
| reelle-zahlen | 2 · Potenzgesetze | 0 | 0 | 0 | 0 |
| reelle-zahlen | 3 · Wurzelgesetze und rationale Exponenten | 0 | 0 | 0 | 0 |
| strahlensaetze | 2 · Zentrische Streckung und Ähnlichkeit | 0 | 0 | 0 | 0 |
| strahlensaetze | 3 · Strahlensätze | 0 | 0 | 0 | 0 |
| symmetrie-abbildungen | 3 · Punktsymmetrie, Drehung, Verschiebung | 0 | 0 | 0 | 0 |
| terme | 3 · Klammern auflösen | 0 | 0 | 1 | 0 |
| terme | 4 · Ausklammern | 0 | 0 | 0 | 0 |
| trigonometrische-funktionen | 1 · Einheitskreis und Bogenmaß | 0 | 0 | 0 | 0 |
| trigonometrische-funktionen | 2 · Sinus- und Kosinusfunktion und ihre Merkmale | 0 | 0 | 0 | 0 |
| trigonometrische-funktionen | 3 · Parameter und Transformationen | 0 | 0 | 0 | 0 |
| trigonometrische-funktionen | 4 · Periodische Vorgänge modellieren | 0 | 0 | 0 | 0 |

Zahl der Einheiten je Wert:

| P10-Jahrgänge | Einheiten (Haupt oder Neben) | Einheiten (nur Haupt) |
|---|---|---|
| 13 | 5 | 1 |
| 12 | 2 | 1 |
| 11 | 7 | 7 |
| 10 | 5 | 4 |
| 9 | 7 | 8 |
| 8 | 9 | 10 |
| 7 | 9 | 7 |
| 6 | 8 | 5 |
| 5 | 11 | 10 |
| 4 | 9 | 10 |
| 3 | 9 | 14 |
| 2 | 4 | 6 |
| 1 | 6 | 8 |
| 0 | 25 | 25 |

## Verteilung für die Schwelle „oft“ – Sek-I-Typen

Sortiert nach P10-Jahrgängen; aufgeführt die 650 Typen mit P10-Typ, die übrigen 684 zählen unten unter 0.

| Eintrag | Typ | P10-Jahrgänge | davon Haupt | P10-Typen |
|---|---|---|---|---|
| trigonometrie | 1.1 rechten Winkel und markierten Winkel finden, Hypotenuse, Gegenkathete und Ankathete beschriften (Dreieck in verschiedener Lage: rechter Winkel unten links, unten rechts, oben; Hypotenuse unten oder oben) | 13 | 11 | Winkelfunktion Seitenverhältnis angeben · Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen · Seite im rechtwinkligen Dreieck berechnen · Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.1 „Seite oder Winkel gesucht“ erkennen | 13 | 10 | Winkel im rechtwinkligen Dreieck berechnen · Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.1 rechtwinkliges Teildreieck in der Figur markieren, rechten Winkel und gegebenen Winkel finden, Seiten vom Winkel aus benennen | 13 | 10 | Seite im rechtwinkligen Dreieck berechnen · Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.6 Parallelogramm: Höhe mit Fußpunkt auf der Verlängerung, Winkel dort, Diagonale aus Höhe und Winkel | 13 | 10 | Seite im rechtwinkligen Dreieck berechnen · Winkel im rechtwinkligen Dreieck berechnen |
| brueche-dezimalzahlen | 1.6 Bruchteil einer Menge oder Größe berechnen (Ganzes : Nenner · Zähler; auch mit Komma und Einheit) | 11 | 11 | Bruchteil einer Größe berechnen · Bruchteil einer Fläche bestimmen |
| prozentrechnung | 2.5 Rabatt in Prozent aus altem und neuem Preis (erst Rabatt in Euro) | 11 | 8 | Prozentsatz berechnen · Prozentuale Veränderung berechnen |
| pythagoras | 1.1 rechten Winkel im Dreieck finden, Hypotenuse und Katheten benennen (Dreieck in verschiedener Lage: rechter Winkel unten links, unten rechts, oben; Hypotenuse waagerecht) | 10 | 9 | Pythagoras Gleichung zuordnen · Satz des Pythagoras formulieren · Pythagoras Hypotenuse · Pythagoras Kathete |
| quadratische-funktionen | 2.5 Scheitelpunktform aus dem Graphen aufstellen (Scheitel ablesen, Öffnung prüfen, nach unten: Minus vor der Klammer) | 10 | 9 | Scheitelpunktform aufstellen · Scheitelpunkt ablesen |
| wahrscheinlichkeit | 2.6 Zufallsgerät entwerfen: Anzahl der Felder oder Kugeln zu gegebener Wahrscheinlichkeit; Kugeln einzeichnen; Topf mit P = 50 % auswählen | 10 | 9 | Zufallsgerät zu Wahrscheinlichkeit entwerfen · Wahrscheinlichkeit einstufig |
| trigonometrie | 1.5 sin-, cos- und tan-Werte mit dem Taschenrechner, Grad-Modus prüfen | 10 | 8 | Seite im rechtwinkligen Dreieck berechnen · Trigonometrische Gleichung nach Seite umstellen |
| trigonometrie | 1.9 Hypotenuse aus Gegenkathete und Winkel (geteilt durch den Sinus) | 10 | 8 | Seite im rechtwinkligen Dreieck berechnen · Trigonometrische Gleichung nach Seite umstellen |
| winkel-dreiecke | 2.7 Winkel an einer Figur mit verlängerten Seiten (Scheitelwinkel des Innenwinkels; überflüssige Angabe) | 10 | 6 | Winkel über Scheitel- oder Nebenwinkel bestimmen · Winkelsumme im Dreieck anwenden |
| winkel-dreiecke | 3.8 Winkel im Teildreieck (Höhe, Diagonale, Drachen mit rechtem Winkel der Diagonalen) | 10 | 6 | Winkelsumme im Dreieck anwenden · Rechten Winkel begründen · Gleichschenkliges Dreieck erkennen |
| brueche-dezimalzahlen | 1.1 Anteil an einer gleich geteilten Figur ablesen | 9 | 9 | Bruchteil einer Fläche bestimmen |
| brueche-dezimalzahlen | 1.2 Anteil einzeichnen (Kästchen, Streifen, Kreis) | 9 | 9 | Bruchteil einer Fläche bestimmen |
| brueche-dezimalzahlen | 1.3 Anteil bei ungleichen Teilen (erst gleich groß machen: halbe Kästchen, Sektoren verschiedener Größe) | 9 | 9 | Bruchteil einer Fläche bestimmen |
| brueche-dezimalzahlen | 1.4 unter mehreren Figuren die mit dem gegebenen Anteil auswählen (Ankreuzen) | 9 | 9 | Bruchteil einer Fläche bestimmen |
| brueche-dezimalzahlen | 2.3 Kürzen mit gegebener Zahl | 9 | 9 | Bruchteil einer Fläche bestimmen |
| brueche-dezimalzahlen | 2.4 vollständig kürzen | 9 | 9 | Bruchteil einer Fläche bestimmen |
| prozentrechnung | 4.5 gemischte Aufgaben: erst zuordnen (Prozentwert, Prozentsatz oder Grundwert gesucht), dann rechnen | 9 | 9 | Grundwert berechnen · Prozentwert berechnen · Prozentsatz berechnen |
| trigonometrie | 4.1 rechtwinklig oder nicht: sin, cos, tan oder Sinussatz (Vorstufe) | 9 | 9 | Sinussatz Seite berechnen · Kosinussatz Seite berechnen |
| trigonometrie | 4.10 Seite als Teil einer Weglänge oder Differenz zu einer Teilstrecke (P10-Form) | 9 | 9 | Sinussatz Seite berechnen |
| trigonometrie | 4.2 Seite und Gegenwinkel als Paar markieren, das vollständige Paar finden | 9 | 9 | Sinussatz Seite berechnen · Sinussatz Winkel berechnen |
| trigonometrie | 4.3 dritter Winkel aus der Winkelsumme | 9 | 9 | Sinussatz Seite berechnen |
| trigonometrie | 4.4 Sinussatz aufstellen (Seite durch Sinus des Gegenwinkels gleich Seite durch Sinus des Gegenwinkels) | 9 | 9 | Sinussatz Seite berechnen · Sinussatz Winkel berechnen |
| trigonometrie | 4.5 nach der Seite umstellen und mit dem Taschenrechner berechnen | 9 | 9 | Sinussatz Seite berechnen |
| trigonometrie | 4.6 stumpfer Winkel im Sinussatz (Taschenrechner rechnet direkt; der stumpfe Winkel gehört in die Winkelsumme) | 9 | 9 | Sinussatz Seite berechnen |
| trigonometrie | 4.7 Nachweis mit vorgegebenem Ergebnis (P10-Form) | 9 | 9 | Sinussatz Seite berechnen |
| trigonometrie | 4.8 Aussage über zwei Seiten prüfen (P10-Form) | 9 | 9 | Sinussatz Seite berechnen |
| trigonometrie | 4.9 Sinussatz im Viereck mit Diagonale: Teilwinkel zuerst, dann das Dreieck mit dem vollständigen Paar wählen (P10-Form) | 9 | 9 | Sinussatz Seite berechnen |
| daten | 4.6 arithmetisches Mittel aus einer Liste | 9 | 8 | Arithmetisches Mittel berechnen |
| daten | 4.7 aus Tabelle oder Diagramm | 9 | 8 | Arithmetisches Mittel berechnen |
| daten | 4.8 sinnvoll runden (Zuschauer je Spiel) | 9 | 8 | Arithmetisches Mittel berechnen |
| daten | 4.9 Mittel aus Gesamtsumme und Anzahl | 9 | 8 | Arithmetisches Mittel berechnen |
| pythagoras | 3.1 rechtwinkliges Teildreieck in der Figur markieren und seine drei Seiten benennen (Hypotenuse gegenüber dem rechten Winkel) | 9 | 8 | Pythagoras Kathete · Pythagoras Hypotenuse · Mantellinie Kegel bestimmen · Streckenlänge aus Koordinaten berechnen |
| quadratische-funktionen | 1.3 Eigenschaften nennen (Scheitel, Symmetrieachse, Öffnung, kleinster Wert) | 9 | 8 | Scheitelpunkt ablesen |
| quadratische-funktionen | 2.1 Scheitel aus der Scheitelpunktform ablesen (Vorzeichen von d) | 9 | 8 | Scheitelpunkt ablesen |
| quadratische-funktionen | 2.2 Scheitel am Graphen ablesen und als S(d | e) schreiben | 9 | 8 | Scheitelpunkt ablesen |
| quadratische-funktionen | 3.5 Scheitel einer Normalform-Parabel am Graphen ablesen | 9 | 8 | Scheitelpunkt ablesen |
| wahrscheinlichkeit | 2.1 P eines Ergebnisses beim Würfel, Glücksrad mit gleich großen Feldern, Urne | 9 | 8 | Wahrscheinlichkeit einstufig |
| wahrscheinlichkeit | 2.10 Behauptung prüfen | 9 | 8 | Wahrscheinlichkeit einstufig |
| wahrscheinlichkeit | 2.2 P als Bruch, gekürzt, als Dezimalzahl und Prozent | 9 | 8 | Wahrscheinlichkeit einstufig |
| wahrscheinlichkeit | 2.3 Ereignis aus mehreren Ergebnissen (Summenregel: „gerade Zahl“, „weder 1 noch 6“) | 9 | 8 | Wahrscheinlichkeit einstufig |
| wahrscheinlichkeit | 2.4 Gesamtzahl aus dem Text finden (Nieten plus Gewinne; Lose 101 bis 900 sind 800) | 9 | 8 | Wahrscheinlichkeit einstufig |
| wahrscheinlichkeit | 2.5 Gegenereignis einstufig (1 − P) | 9 | 8 | Wahrscheinlichkeit über Gegenereignis berechnen · Wahrscheinlichkeit einstufig |
| wahrscheinlichkeit | 2.7 veränderte Grundmenge (zwei Pfannkuchen sind schon weg) | 9 | 8 | Wahrscheinlichkeit einstufig · Wahrscheinlichkeit mehrstufig ohne Zurücklegen |
| wahrscheinlichkeit | 2.8 Grundmenge einschränken (nur die Lose mit Endziffer 6) | 9 | 8 | Wahrscheinlichkeit einstufig |
| trigonometrie | 1.10 Hypotenuse aus Ankathete und Winkel (geteilt durch den Kosinus) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.11 Gegenkathete aus Ankathete und Winkel (Tangens, mal) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.12 Ankathete aus Gegenkathete und Winkel (geteilt durch den Tangens) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.13 Funktion selbst wählen: welche zwei Seiten sind beteiligt | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.15 Winkel als Dezimalgrad, Seiten als Dezimalzahlen | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.16 Einheit beim Ergebnis, Runden auf eine Dezimale | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.17 Ergebnis prüfen: Kathete kürzer als Hypotenuse | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.18 Nachweis mit vorgegebenem Ergebnis (P10-Form) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.19 Sachaufgabe mit gegebener Skizze (Leiter an der Wand, Dachschräge mit Wand, Rampe, Diagonale eines Vierecks mit rechtem Winkel) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.7 Gegenkathete aus Hypotenuse und Winkel (Sinus, mal) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 1.8 Ankathete aus Hypotenuse und Winkel (Kosinus, mal) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.10 Teilwinkel: den Winkel des Teildreiecks als Differenz zweier gegebener Winkel bilden (P10-Form) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.11 zwei Teildreiecke nacheinander an derselben Höhe (P10-Form) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen · Diagonale eines Drachenvierecks über Winkelfunktion berechnen |
| trigonometrie | 3.12 Strecke aus Teilstrecken nach der Trigonometrie | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.13 Rechenweg als Lösungsplan ohne Zahlen (P10-Form) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen · Formel über Winkelfunktion herleiten |
| trigonometrie | 3.14 zweiter Weg mit dem Satz des Pythagoras, Vergleich der Ergebnisse | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.15 Seitenhöhe oder Mantellinie aus Grundkante oder Radius und Neigungswinkel im Stützdreieck (kein P10-Original, RLP G, LISUM-PH „Körper“) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen · Formel über Winkelfunktion herleiten |
| trigonometrie | 3.2 Höhe im gleichschenkligen Dreieck aus Schenkel und Basiswinkel | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.3 Höhe im beliebigen Dreieck aus Seite und Winkel, dann Fläche (Typ in flaechen.md) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.4 Trapez: Schenkel aus Höhe und Basiswinkel, Höhe aus Schenkel und Winkel, Überstand mit dem Tangens | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.7 Drachen und Raute: halbe Diagonale aus Seite und Winkel | 9 | 7 | Diagonale eines Drachenvierecks über Winkelfunktion berechnen · Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.8 Vermessung: Höhe eines Turms oder Bergs aus Abstand und Höhenwinkel, Gerätehöhe oder Sockel addieren (P10-Form) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.9 Plattform oder Aufbau zur Höhe addieren | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| trigonometrie | 4.11 zweiter Weg über zwei rechtwinklige Teildreiecke mit der Höhe (Vergleich) | 9 | 7 | Seite im rechtwinkligen Dreieck berechnen |
| wahrscheinlichkeit | 4.7 Vergleich mit Zurücklegen (Behauptung „doppelt so hoch“) | 9 | 6 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen · Wahrscheinlichkeit mehrstufig unabhängig |
| winkel-dreiecke | 3.1 dritter Winkel im Dreieck (ganze Grade, Dezimalgrade) | 9 | 4 | Winkelsumme im Dreieck anwenden |
| winkel-dreiecke | 3.4 gleichschenklig: Basiswinkel gleich, dritter Winkel | 9 | 4 | Winkelsumme im Dreieck anwenden |
| winkel-dreiecke | 3.6 gleichseitig 60° | 9 | 4 | Winkelsumme im Dreieck anwenden |
| winkel-dreiecke | 3.7 rechtwinklig: die zwei spitzen Winkel ergeben 90° | 9 | 4 | Winkelsumme im Dreieck anwenden |
| brueche-dezimalzahlen | 5.11 mit negativen Zahlen (Vorrat, rationale-zahlen.md Einheit 1) | 8 | 8 | Zahlen in verschiedenen Darstellungen vergleichen · Mitte zweier Zahlen bestimmen |
| daten | 2.4 größte und kleinste Säule, Differenz zweier Säulen | 8 | 8 | Minimum und Maximum ablesen · Spannweite berechnen |
| daten | 4.1 Minimum und Maximum aus Liste, Tabelle, Diagramm | 8 | 8 | Minimum und Maximum ablesen · Spannweite berechnen |
| trigonometrie | 1.2 Seiten vom zweiten spitzen Winkel aus neu benennen (Gegen- und Ankathete tauschen) | 8 | 8 | Winkelfunktion Seitenverhältnis angeben · Winkel im rechtwinkligen Dreieck berechnen |
| pythagoras | 1.13 Ergebnis mit sinnvoller Genauigkeit angeben | 8 | 7 | Pythagoras Hypotenuse · Pythagoras Kathete |
| pythagoras | 1.3 Gleichung zum beschrifteten Dreieck aufstellen (a² + b² = c², mit x, y, z oder u, v, w nach der Beschriftung) | 8 | 7 | Pythagoras Gleichung zuordnen · Pythagoras Hypotenuse |
| pythagoras | 3.16 Rampe, Leiter, Seil an der Wand mit Skizze | 8 | 7 | Pythagoras Hypotenuse · Pythagoras Kathete |
| pythagoras | 3.4 gleichschenkliges Trapez: Überstand als halbe Differenz der parallelen Seiten, Schenkel oder Höhe | 8 | 7 | Pythagoras Hypotenuse · Pythagoras Kathete |
| wahrscheinlichkeit | 4.1 Baum für zweimal Ziehen ohne Zurücklegen (Nenner minus 1) | 8 | 7 | Baumdiagramm ergänzen · Wahrscheinlichkeit mehrstufig ohne Zurücklegen |
| wahrscheinlichkeit | 4.5 Baum mit leeren Feldern nach verschiedenen Vorgeschichten ergänzen | 8 | 7 | Baumdiagramm ergänzen · Wahrscheinlichkeit mehrstufig ohne Zurücklegen |
| brueche-dezimalzahlen | 3.6 drei bis vier Brüche ordnen | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 4.2 Zehnerbruch ↔ Dezimalzahl (auch mit Nullen: 3/100, 3/1000) | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 4.5 Bruch → Dezimalzahl durch Erweitern auf 10, 100, 1000 (Halbe, Viertel, Fünftel, Zwanzigstel, Fünfundzwanzigstel) | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 5.1 zwei Dezimalzahlen mit gleich vielen Stellen vergleichen | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 5.10 Aussagen prüfen und die wahre ankreuzen | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 5.12 mit Wurzeln über Näherungswert (Vorrat, potenzen-wurzeln.md) | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 5.2 verschieden viele Stellen (Nullen anhängen) | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 5.3 Dezimalzahlen ordnen | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 5.7 Bruch gegen Dezimalzahl (Vergleichszeichen) | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 5.8 Prozent gegen Dezimalzahl | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| brueche-dezimalzahlen | 5.9 gemischte Liste ordnen (Bruch, Dezimalzahl, Prozent, Potenz einer Dezimalzahl) | 7 | 7 | Zahlen in verschiedenen Darstellungen vergleichen |
| daten | 4.2 Spannweite (auch Dezimalzahlen und große Zahlen) | 7 | 7 | Spannweite berechnen |
| flaechen | 3.2 rechtwinklig: Katheten als g und h | 7 | 7 | Flächeninhalt Dreieck berechnen · Term zu Figur angeben · Grundseite aus Dreiecksfläche berechnen |
| potenzen-wurzeln | 1.13 Exponent mit Basis 10 (10^x = 100 000; Brücke zu Einheit 2) | 7 | 7 | Exponent einer Potenz bestimmen · Zehnerpotenzschreibweise umwandeln |
| pythagoras | 2.1 Gleichung nach einer Kathete umstellen (a² = c² − b², b² = c² − a²) | 7 | 7 | Pythagoras Kathete · Pythagoras Gleichung zuordnen |
| quadratische-gleichungen | 3.1 Normalform erkennen und p, q mit Vorzeichen ablesen | 7 | 6 | Nullstellen quadratische Funktion berechnen · Argument zu Funktionswert berechnen · Schnittpunkte Gerade und Parabel berechnen |
| quadratische-gleichungen | 3.4 p-q-Formel mit ganzzahligen Lösungen (Diskriminante Quadratzahl) | 7 | 6 | Nullstellen quadratische Funktion berechnen · Argument zu Funktionswert berechnen · Schnittpunkte Gerade und Parabel berechnen |
| wahrscheinlichkeit | 3.10 Zufallsgerät mehrstufig belegen (Produkt 1/4; Würfelnetz für P(Summe 2)) | 7 | 6 | Zufallsgerät zu Wahrscheinlichkeit entwerfen · Wahrscheinlichkeit mehrstufig unabhängig · Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen |
| lineare-funktionen | 3.4 Punktprobe | 7 | 5 | Punktprobe durchführen |
| lineare-funktionen | 2.1 n am Graphen ablesen | 7 | 4 | y-Achsenabschnitt ablesen · Geradengleichung zu Graph zuordnen · Eigenschaften eines Graphen beurteilen |
| lineare-funktionen | 2.5 Parameter deuten (steigend, fallend, parallel, Sonderfall m = 0) | 7 | 4 | Graph nach Eigenschaft auswählen · Eigenschaften eines Graphen beurteilen · Lage zweier Geraden bestimmen |
| lineare-funktionen | 3.6 Schnittpunkt mit y-Achse | 7 | 3 | y-Achsenabschnitt ablesen · Eigenschaften eines Graphen beurteilen |
| flaechen | 5.3 Fläche durch Ergänzen (Rechteck minus Ecke) | 6 | 6 | Restfläche berechnen · Term zu Figur angeben |
| prozentrechnung | 3.1 50 %, 25 %, 10 % vom Ganzen | 6 | 6 | Prozentwert berechnen |
| prozentrechnung | 3.2 1 %-Weg (G : 100, mal p) | 6 | 6 | Prozentwert berechnen |
| prozentrechnung | 3.3 10 %-Schritte (30 %, 15 %, 5 %) | 6 | 6 | Prozentwert berechnen |
| prozentrechnung | 3.4 Dezimalzahl mal Grundwert (0,3 · G) | 6 | 6 | Prozentwert berechnen |
| prozentrechnung | 3.5 Grundwert mit Komma (3,50 €) | 6 | 6 | Prozentwert berechnen |
| prozentrechnung | 3.6 Ersparnis und neuer Preis unterscheiden | 6 | 6 | Prozentwert berechnen |
| prozentrechnung | 3.7 Prozentsatz über 100 % | 6 | 6 | Prozentwert berechnen |
| prozentrechnung | 3.8 Mehrwertsteuer in Euro | 6 | 6 | Prozentwert berechnen |
| prozentrechnung | 5.7 Prozentpunkte gegen Prozent | 6 | 6 | Prozentwert berechnen |
| terme | 1.3 Term zu Figur angeben (Umfang, Fläche aus Rechtecken) | 6 | 6 | Term zu Figur angeben · Term zu Körper angeben |
| wahrscheinlichkeit | 3.1 Baum zu zwei Drehungen oder zwei Würfeln zeichnen | 6 | 6 | Baumdiagramm ergänzen |
| wahrscheinlichkeit | 3.2 Astwahrscheinlichkeiten ergänzen (Summe an jedem Punkt 1) | 6 | 6 | Baumdiagramm ergänzen |
| koerper | 4.11 Sachaufgabe (Dose, Regentonne, Turm, Becher, Rohr) | 6 | 5 | Volumen Zylinder berechnen · Mantelfläche Zylinder berechnen |
| lineare-gleichungssysteme | 4.1 Unbekannte benennen und mit Einheit beschriften | 6 | 5 | Gleichung im Sachzusammenhang deuten · Lineares Gleichungssystem aufstellen |
| potenz-exponentialfunktionen | 1.4 Zunahme und Abnahme unterscheiden (Faktor größer oder kleiner als eins) | 6 | 5 | Exponentialfunktion aufstellen · Wachstumstabelle ergänzen |
| potenz-exponentialfunktionen | 2.1 Prozentsatz in den Faktor umrechnen, Zunahme und Abnahme | 6 | 5 | Wachstumstabelle ergänzen · Exponentialfunktion aufstellen |
| trigonometrie | 2.10 Steigungswinkel einer Rampe oder Seilbahn aus Höhe und Länge | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen · Neigungswinkel einer Geraden berechnen |
| trigonometrie | 2.11 Winkel eines Dreiecks im Koordinatensystem aus abgelesenen Katheten (P10-Form) | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen · Neigungswinkel einer Geraden berechnen |
| trigonometrie | 2.12 Winkel im Teildreieck mit gezeichneter Höhe | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.13 Nachweis mit vorgegebenem Winkel („Zeigen Sie rechnerisch, dass α ≈ …“; P10-Form) | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.14 Winkel prüfen: die längere Kathete liegt dem größeren Winkel gegenüber | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.2 zwei gegebene Seiten vom gesuchten Winkel aus benennen und die Funktion wählen | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.3 Verhältnis als Bruch und als Dezimalzahl | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.4 Umkehrtaste am Taschenrechner (SHIFT sin, cos, tan; Anzeige sin⁻¹) | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.5 Winkel aus Gegenkathete und Hypotenuse (sin⁻¹) | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.6 aus Ankathete und Hypotenuse (cos⁻¹) | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.7 aus beiden Katheten (tan⁻¹) | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.8 Runden auf eine Dezimale, Gradzeichen | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 2.9 zweiter spitzer Winkel als Ergänzung zum rechten Winkel, Kontrolle mit der zweiten Funktion | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| trigonometrie | 3.5 rechtwinkliges Trapez: Hilfsdreieck mit der Differenz der beiden Höhen als Kathete, Winkel darin (P10-Form) | 6 | 5 | Winkel im rechtwinkligen Dreieck berechnen |
| wahrscheinlichkeit | 4.6 „unter den ersten drei“ (Summe dreier Pfade oder Gegenereignis) | 6 | 4 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen · Wahrscheinlichkeit über Gegenereignis berechnen |
| prozentrechnung | 5.4 Veränderung in Prozent aus zwei Werten (Differenz : Ausgangswert) | 6 | 3 | Prozentuale Veränderung berechnen |
| winkel-dreiecke | 1.8 Strecke aus Teilstrecken (Summe, Differenz, Einheiten m/km) | 6 | 3 | Strecke aus Teilstrecken berechnen |
| daten | 2.9 Liniendiagramm lesen (Verlauf, Anstieg, Rückgang) | 5 | 5 | Wert aus Diagramm ablesen · Aussage zu Diagramm prüfen |
| flaechen | 1.8 Term zu Figur (Fläche oder Umfang mit Variablen) | 5 | 5 | Term zu Figur angeben |
| flaechen | 3.7 Term zu Figur (Umfang gleichseitig 3 · a; Fläche rechtwinklig) | 5 | 5 | Term zu Figur angeben |
| flaechen | 5.5 Umfang einer zusammengesetzten Figur | 5 | 5 | Term zu Figur angeben |
| kreis | 2.7 Term zu Figur (Viertelkreis: 1/4 · π · r²) | 5 | 5 | Term zu Figur angeben |
| lineare-funktionen | 1.3 Graph zeichnen | 5 | 5 | Gerade aus Gleichung zeichnen |
| lineare-funktionen | 2.3 Gerade aus Gleichung zeichnen | 5 | 5 | Gerade aus Gleichung zeichnen |
| potenz-exponentialfunktionen | 2.11 Tabelle für einen Zerfall mit Faktor kleiner eins fortschreiben | 5 | 5 | Wachstumstabelle ergänzen |
| potenz-exponentialfunktionen | 2.4 nächsten Tabellenwert berechnen (Wert mal Faktor) | 5 | 5 | Wachstumstabelle ergänzen |
| potenz-exponentialfunktionen | 2.5 Lücke mitten in der Tabelle füllen | 5 | 5 | Wachstumstabelle ergänzen |
| potenz-exponentialfunktionen | 2.6 Anfangsbestand als Wert im Schritt null eintragen (nicht rückwärts rechnen, wenn der Startwert im Text steht) | 5 | 5 | Wachstumstabelle ergänzen |
| potenz-exponentialfunktionen | 2.7 einen Schritt zurückrechnen (geteilt durch den Faktor) | 5 | 5 | Wachstumstabelle ergänzen |
| potenz-exponentialfunktionen | 2.8 Wert über mehrere Schritte mit der Potenz des Faktors | 5 | 5 | Wachstumstabelle ergänzen |
| potenz-exponentialfunktionen | 2.9 fehlende Zeitangabe im Tabellenkopf über die Zahl der Schritte bestimmen und prüfen | 5 | 5 | Wachstumstabelle ergänzen |
| potenzen-wurzeln | 2.1 Zehnerpotenz ausschreiben (10⁶ = 1 000 000) und Zahl als Zehnerpotenz schreiben (100 000 = 10⁵; P10-Form) | 5 | 5 | Zehnerpotenzschreibweise umwandeln |
| potenzen-wurzeln | 2.14 Sachaufgabe aus Astronomie oder Mikrowelt (Lichtjahr, Atommasse; Einheit mitführen) | 5 | 5 | Große Zahl mit Zehnerpotenz multiplizieren · Zehnerpotenzschreibweise umwandeln |
| potenzen-wurzeln | 2.4 Zahl in Zehnerpotenzschreibweise a · 10ⁿ mit a zwischen 1 und 10 schreiben (Komma setzen, Stellen zählen) | 5 | 5 | Zehnerpotenzschreibweise umwandeln |
| potenzen-wurzeln | 2.5 fehlenden Exponenten in „a · 10^□“ eintragen (P10-Form) | 5 | 5 | Zehnerpotenzschreibweise umwandeln |
| potenzen-wurzeln | 2.6 Zehnerpotenzschreibweise ausschreiben: Komma nach rechts, Nullen auffüllen (P10-Form) | 5 | 5 | Zehnerpotenzschreibweise umwandeln |
| potenzen-wurzeln | 2.7 passende ausgeschriebene Zahl unter drei Angeboten ankreuzen (P10-Form) | 5 | 5 | Zehnerpotenzschreibweise umwandeln |
| potenzen-wurzeln | 2.8 kleine Zahl mit negativem Exponenten: Komma nach links, Nullen vorn (2,1 · 10⁻⁴ = 0,00021; P10-Form) | 5 | 5 | Zehnerpotenzschreibweise umwandeln |
| potenzen-wurzeln | 2.9 Zahl kleiner als eins in Zehnerpotenzschreibweise schreiben (0,00035 = 3,5 · 10⁻⁴) | 5 | 5 | Zehnerpotenzschreibweise umwandeln |
| prozentrechnung | 2.1 Teil von 100 | 5 | 5 | Prozentsatz berechnen |
| prozentrechnung | 2.2 Teil von 50, 25, 20, 10 (erweitern) | 5 | 5 | Prozentsatz berechnen |
| prozentrechnung | 2.3 beliebiges Ganzes: W : G mit Taschenrechner, runden | 5 | 5 | Prozentsatz berechnen |
| prozentrechnung | 2.4 Anteil aus Sachtext (Ganzes zuerst finden) | 5 | 5 | Prozentsatz berechnen |
| pythagoras | 2.3 Kathete aus Hypotenuse und Kathete mit aufgehender Wurzel | 5 | 5 | Pythagoras Kathete |
| pythagoras | 2.4 mit nicht aufgehender Wurzel: Zwischenergebnis a², Näherungswert | 5 | 5 | Pythagoras Kathete |
| pythagoras | 2.5 Dezimalzahlen | 5 | 5 | Pythagoras Kathete |
| pythagoras | 2.6 Ergebnis prüfen: die Kathete ist kürzer als die Hypotenuse | 5 | 5 | Pythagoras Kathete |
| pythagoras | 2.7 Nachweis mit vorgegebenem Ergebnis („Weisen Sie nach, dass … ≈ …“; P10-Form) | 5 | 5 | Pythagoras Kathete |
| pythagoras | 2.8 Kathete im Sachzusammenhang (Höhenunterschied der Seilbahn, Abstand auf dem Platz, Höhe des Parallelogramms mit Fußpunkt außerhalb) | 5 | 5 | Pythagoras Kathete |
| pythagoras | 3.12 Kegelhöhe aus Mantellinie und Radius | 5 | 5 | Kegelhöhe aus Mantellinie und Radius berechnen · Pythagoras Kathete |
| pythagoras | 3.14 Gesamthöhe eines Turms aus Zylinderhöhe und Kegelhöhe | 5 | 5 | Pythagoras Kathete · Kegelhöhe aus Mantellinie und Radius berechnen |
| pythagoras | 3.2 Höhe im gleichschenkligen Dreieck aus Schenkel und halber Grundseite | 5 | 5 | Pythagoras Kathete |
| pythagoras | 3.5 Parallelogramm: Höhe mit Fußpunkt auf der Verlängerung der Grundseite | 5 | 5 | Pythagoras Kathete |
| pythagoras | 3.6 stumpfwinkliges Dreieck mit Höhe: Teilstrecke der Grundseite | 5 | 5 | Pythagoras Kathete |
| terme | 1.2 Term zu Sachtext angeben (Doppeltes, vermindert um) | 5 | 5 | Term zu Sachtext angeben |
| terme | 2.7 Term aus Situation aufstellen und zusammenfassen | 5 | 5 | Term zu Figur angeben |
| trigonometrie | 1.3 sin, cos oder tan zum beschrifteten Dreieck als Bruch eintragen (P10-Form, Buchstaben r, s, t; a, b; u, v, w) | 5 | 5 | Winkelfunktion Seitenverhältnis angeben |
| trigonometrie | 1.4 die richtige von drei Gleichungen ankreuzen (P10-Form) | 5 | 5 | Winkelfunktion Seitenverhältnis angeben · Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen |
| koerper | 2.3 Einheiten cm³, dm³ = l, m³ (1 l = 1000 cm³) | 5 | 4 | Volumen Zylinder berechnen · Höhe eines Zylinders aus Volumen berechnen |
| koerper | 4.1 V = π · r² · h | 5 | 4 | Volumen Zylinder berechnen |
| koerper | 4.2 r aus d | 5 | 4 | Volumen Zylinder berechnen · Höhe eines Zylinders aus Volumen berechnen |
| koerper | 4.3 Liter (cm³ → dm³) | 5 | 4 | Volumen Zylinder berechnen |
| koerper | 4.9 Behauptung prüfen (Herstellerangabe „ca. 400 ml“) | 5 | 4 | Volumen Zylinder berechnen |
| lineare-funktionen | 3.3 Wertetabelle | 5 | 4 | Wertetabelle einer Funktion zuordnen · Funktionswert berechnen |
| lineare-gleichungen | 4.5 Gleichung aus Sachverhalt aufstellen und lösen (P10-Form) | 5 | 4 | Lineare Gleichung aus Sachverhalt aufstellen · Lineare Gleichung lösen |
| lineare-gleichungssysteme | 4.10 Gleichung als Satz formulieren („x + y = 20“: zusammen zwanzig Stück) | 5 | 4 | Gleichung im Sachzusammenhang deuten |
| lineare-gleichungssysteme | 4.11 Bestandteile einer Gleichung deuten (Vorzahl, Absolutglied; bei linearen Funktionen → lineare-funktionen.md Einheit 5, bei Wachstum → potenz-exponentialfunktionen.md) | 5 | 4 | Gleichung im Sachzusammenhang deuten |
| lineare-gleichungssysteme | 4.9 Gleichung im Sachzusammenhang deuten: Variablen benennen (Preis oder Anzahl?) | 5 | 4 | Gleichung im Sachzusammenhang deuten |
| wahrscheinlichkeit | 3.6 „mindestens einmal“ über 1 − P(nie) | 5 | 4 | Wahrscheinlichkeit über Gegenereignis berechnen · Wahrscheinlichkeit mehrstufig unabhängig |
| kreis | 2.6 Halbkreis- und Viertelkreisfläche | 5 | 3 | Flächeninhalt zusammengesetzter Figur berechnen · Kreisfläche berechnen |
| lineare-funktionen | 1.4 Wert ablesen und berechnen | 5 | 3 | Funktionswert berechnen |
| lineare-funktionen | 3.1 Funktionswert berechnen | 5 | 3 | Funktionswert berechnen |
| lineare-gleichungen | 1.3 Gleichung mit Umkehroperation lösen | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 2.1 einschrittig (+, −, ·, :) | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 2.2 zweischrittig (erst Strich, dann Punkt) | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 2.3 negative Lösung | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 2.4 negative Vorzahl (−4x = 20) | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 2.6 Umformung anschreiben (Vorstufe, s. Voraussetzungen) | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 3.1 x beidseitig | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 3.2 erst zusammenfassen | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 3.3 Klammer auflösen (Plus, Minus, Zahl mal Klammer) | 5 | 3 | Lineare Gleichung lösen |
| lineare-gleichungen | 3.5 Dezimalzahlen | 5 | 3 | Lineare Gleichung lösen |
| wahrscheinlichkeit | 3.3 P eines Pfades (Pfadregel) | 5 | 3 | Wahrscheinlichkeit mehrstufig unabhängig |
| wahrscheinlichkeit | 3.4 P eines Ereignisses aus mehreren Pfaden (Summenregel: „12 oder 21“) | 5 | 3 | Wahrscheinlichkeit mehrstufig unabhängig |
| wahrscheinlichkeit | 3.5 „zweimal derselbe Buchstabe“ (drei Pfade) | 5 | 3 | Wahrscheinlichkeit mehrstufig unabhängig |
| wahrscheinlichkeit | 3.8 dreistufig („mindestens zwei Sechsen“) | 5 | 3 | Wahrscheinlichkeit mehrstufig unabhängig · Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen |
| wahrscheinlichkeit | 3.9 Behauptung prüfen (P(22) = P(33)? P(gleich) gegen P(erst 6)) | 5 | 3 | Wahrscheinlichkeit mehrstufig unabhängig |
| wahrscheinlichkeit | 4.2 P zweier gleicher Farben | 5 | 3 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen |
| wahrscheinlichkeit | 4.3 zweite Person zieht (erste Stufe mitrechnen: erst kein Joker, dann Joker) | 5 | 3 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen |
| wahrscheinlichkeit | 4.4 dreistufig, ein Pfad (drei rote Stifte) | 5 | 3 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen |
| kreis | 1.3 d = 2 · r und r = d : 2 | 5 | 2 | Kreisfläche berechnen |
| kreis | 2.1 A aus r | 5 | 2 | Kreisfläche berechnen |
| kreis | 2.2 A aus d (erst halbieren) | 5 | 2 | Kreisfläche berechnen |
| kreis | 2.3 A mit Dezimalzahlen, runden | 5 | 2 | Kreisfläche berechnen |
| kreis | 2.8 Sachaufgabe (Abwurfring, Pizza, Deckel, Grundfläche eines Kegels oder Zylinders) | 5 | 2 | Kreisfläche berechnen |
| kreis | 2.9 Fläche oder Umfang: die passende Formel wählen | 5 | 2 | Kreisfläche berechnen |
| prozentrechnung | 1.1 Bruch → Prozent (Nenner 100; Nenner, der in 100 aufgeht) | 5 | 2 | Prozent und Anteil umwandeln |
| prozentrechnung | 1.2 Dezimalzahl ↔ Prozent | 5 | 2 | Prozent und Anteil umwandeln |
| prozentrechnung | 1.3 Anteil am Streifen oder an einer Figur ablesen und einzeichnen | 5 | 2 | Prozent und Anteil umwandeln · Prozentanteil einer Rasterfläche markieren |
| prozentrechnung | 1.4 Anteilsformulierung ↔ Prozent („jeder fünfte“, „ein Viertel“, „4 von 100“) | 5 | 2 | Prozent und Anteil umwandeln |
| quadratische-funktionen | 2.4 Scheitelpunktform aus dem Scheitel aufstellen | 5 | 2 | Scheitelpunktform aufstellen |
| quadratische-funktionen | 3.6 Scheitelpunktform aus Normalform und abgelesenem Scheitel aufstellen, Probe mit q | 5 | 2 | Scheitelpunktform aufstellen |
| daten | 3.3 Prozent → Mittelpunktswinkel (Anteil mal 360°) | 5 | 1 | Mittelpunktswinkel berechnen · Kreisdiagramm zeichnen |
| daten | 3.4 Bruchteil oder Anzahl → Winkel (12 von 508) | 5 | 1 | Mittelpunktswinkel berechnen · Kreisdiagramm zeichnen |
| flaechen | 3.3 Höhe zur passenden Grundseite wählen (drei Höhen) | 4 | 4 | Flächeninhalt Dreieck berechnen · Grundseite aus Dreiecksfläche berechnen |
| lineare-gleichungssysteme | 4.3 Anzahl-und-Preis mit Dezimalzahlen (Eintritt, Blumen, Bäume) | 4 | 4 | Lineares Gleichungssystem aufstellen · Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 4.4 Anzahl-und-Bestand (Zimmer und Betten, Räder von Autos und Rädern) | 4 | 4 | Lineares Gleichungssystem aufstellen · Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 4.7 System aufstellen, lösen, Lösung zuordnen, Antwortsatz | 4 | 4 | Lineares Gleichungssystem aufstellen · Lineares Gleichungssystem lösen |
| pythagoras | 1.4 Gleichung aus vier Optionen ankreuzen (Summe, Differenz, mit und ohne Wurzel; P10-Form) | 4 | 4 | Pythagoras Gleichung zuordnen |
| pythagoras | 2.2 Kathetengleichung aus Optionen ankreuzen (P10-Form) | 4 | 4 | Pythagoras Gleichung zuordnen |
| quadratische-gleichungen | 3.2 Gleichung ordnen: alles auf eine Seite, Reihenfolge x², x, Zahl | 4 | 4 | Argument zu Funktionswert berechnen · Schnittpunkte Gerade und Parabel berechnen |
| rationale-zahlen | 3.1 plus mal minus, minus mal minus | 4 | 4 | Vorzeichenregel anwenden · Termwert berechnen |
| rationale-zahlen | 3.2 dividieren mit Vorzeichen | 4 | 4 | Termwert berechnen · Vorzeichenregel anwenden |
| symmetrie-abbildungen | 2.12 Symmetrieachse als Diagonale nutzen (Drachenviereck: die Achse halbiert die andere Diagonale senkrecht; Voraussetzung in pythagoras.md) | 4 | 4 | Symmetrieachsen bestimmen · Figur nach Spiegelung benennen |
| winkel-dreiecke | 2.8 Winkel im Parallelogramm und Trapez an den parallelen Seiten | 4 | 4 | Winkel im Viereck berechnen · Eigenschaft einer Figur zuordnen |
| zuordnungen | 4.7 Dauer aus Menge und Rate, Zeiteinheit umrechnen | 4 | 4 | Dauer aus Menge und Rate berechnen |
| einheiten | 2.1 Zeiteinheiten nennen und ordnen | 4 | 3 | Zeiteinheiten umrechnen |
| einheiten | 2.11 Dauer in eine sinnvolle Einheit bringen (Sekunden in Minuten, Stunden in Tage) | 4 | 3 | Zeiteinheiten umrechnen |
| einheiten | 2.2 Minuten in Stunden und Stunden in Minuten | 4 | 3 | Zeiteinheiten umrechnen |
| einheiten | 2.3 Sekunden in Minuten | 4 | 3 | Zeiteinheiten umrechnen |
| einheiten | 2.4 Dezimalstunden in Minuten (P10-Form: eineinhalb Stunden, drei Komma zwei fünf Stunden) | 4 | 3 | Zeiteinheiten umrechnen |
| einheiten | 2.5 Minuten als Dezimalstunde schreiben | 4 | 3 | Zeiteinheiten umrechnen |
| pythagoras | 1.10 Diagonale im Rechteck und Quadrat | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 1.11 Sachaufgabe mit gegebener Skizze (Rampe, Leiter an der Wand, Abkürzung über die Wiese, Stab in der Kiste) | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 1.12 Überstand oder Zuschlag zum Ergebnis addieren | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 1.6 Hypotenuse aus zwei Katheten mit aufgehender Wurzel | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 1.7 mit nicht aufgehender Wurzel: Zwischenergebnis c², Näherungswert gerundet | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 1.8 Katheten als Dezimalzahlen | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 1.9 Einheit beim Ergebnis, gemischte Einheiten vorher angleichen | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 3.10 Seitenhöhe der Pyramide aus Höhe und halber Grundkante | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 3.15 Stab oder Stange schräg im Zylinder oder Quader mit Überstand | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 3.3 Schenkel aus Höhe und halber Grundseite | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 3.7 Drachen und Raute: Seite aus den halben Diagonalen | 4 | 3 | Pythagoras Hypotenuse |
| pythagoras | 3.8 Diagonale im Rechteck, Raumdiagonale im Quader in zwei Schritten | 4 | 3 | Pythagoras Hypotenuse |
| quadratische-funktionen | 4.4 vorher durch den Streckfaktor teilen | 4 | 3 | Nullstellen quadratische Funktion berechnen · Argument zu Funktionswert berechnen |
| quadratische-gleichungen | 1.6 (x − d)² = c rückwärts rechnen (zwei Fälle x − d = √c und x − d = −√c, dann d hinüberbringen) | 4 | 3 | Lösbarkeit quadratischer Gleichung beurteilen · Nullstellen quadratische Funktion berechnen |
| quadratische-gleichungen | 3.3 Normieren: durch die Vorzahl von x² teilen, auch bei negativer Vorzahl | 4 | 3 | Nullstellen quadratische Funktion berechnen · Argument zu Funktionswert berechnen |
| wahrscheinlichkeit | 1.1 Möglichkeiten aufzählen (Kleidung, Menü, Wege) und zählen | 4 | 3 | Ergebnismenge aufzählen · Anzahl Kombinationen nach dem Zählprinzip bestimmen |
| wahrscheinlichkeit | 1.3 alle zweistelligen Zahlen aus zwei Ziffernscheiben (doppelte Ziffern nur einmal) | 4 | 3 | Ergebnismenge aufzählen |
| wahrscheinlichkeit | 1.6 Ergebnismenge zweier Münzen (ZZ, ZW, WZ, WW) | 4 | 3 | Ergebnismenge aufzählen |
| wahrscheinlichkeit | 1.7 Paare beim zweifachen Würfeln mit Bedingung (zweiter Wurf 2) | 4 | 3 | Ergebnismenge aufzählen |
| wahrscheinlichkeit | 1.8 Ergebnisse zu „mindestens einmal …“ aufzählen | 4 | 3 | Ergebnismenge aufzählen |
| winkel-dreiecke | 2.3 drei Geraden durch einen Punkt (Teilwinkel, Scheitelwinkel minus Teil) | 4 | 3 | Winkel über Scheitel- oder Nebenwinkel bestimmen · Winkel aus Teilwinkeln berechnen |
| daten | 3.8 Sektoren nach Größe den Angaben zuordnen | 4 | 2 | Sektor im Kreisdiagramm zuordnen |
| daten | 3.9 Anteil aus einem Sektor schätzen (Viertel, Drittel, Hälfte) | 4 | 2 | Sektor im Kreisdiagramm zuordnen |
| potenz-exponentialfunktionen | 3.1 Anfangswert und Faktor im Text finden | 4 | 2 | Exponentialfunktion aufstellen |
| potenz-exponentialfunktionen | 3.2 Gleichung y = a · qˣ aufstellen (Zunahme und Abnahme) | 4 | 2 | Exponentialfunktion aufstellen |
| potenz-exponentialfunktionen | 3.3 passende Gleichung unter vier Vorschlägen ankreuzen | 4 | 2 | Exponentialfunktion aufstellen |
| zuordnungen | 1.2 Punkte ins Koordinatensystem eintragen | 4 | 2 | Wertetabelle als Punkte darstellen |
| zuordnungen | 2.7 Graph zeichnen (Ursprungsgerade) und Werte ablesen | 4 | 2 | Wertetabelle als Punkte darstellen |
| zuordnungen | 3.5 Graph als fallende Kurve, Werte ablesen | 4 | 2 | Wertetabelle als Punkte darstellen |
| lineare-gleichungssysteme | 1.3 Gleichung nach y umstellen | 4 | 1 | Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 1.8 systematisches Probieren mit Tabelle bei ganzzahliger Lösung | 4 | 1 | Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 2.1 eine Gleichung ist nach y aufgelöst, in die andere einsetzen | 4 | 1 | Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 2.10 zweite Variable berechnen und Probe in beiden Gleichungen | 4 | 1 | Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 2.2 I nach y umstellen (Vorzahl 1) | 4 | 1 | Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 2.3 nach x umstellen | 4 | 1 | Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 2.4 Klammer mit Zahl davor auflösen | 4 | 1 | Lineares Gleichungssystem lösen |
| lineare-gleichungssysteme | 2.6 Dezimalzahlen (Geld) | 4 | 1 | Lineares Gleichungssystem lösen |
| daten | 2.2 Achsenbeschriftung „in Tausend“, „in Mio.“, „in %“ anwenden | 3 | 3 | Wert aus Diagramm ablesen · Werte im Diagramm nach Bedingung auswählen |
| daten | 5.1 Aussage zum Verlauf prüfen („immer weniger“ – gibt es einen Anstieg dazwischen?) | 3 | 3 | Aussage zu Diagramm prüfen |
| daten | 5.2 Aussage zur Veränderung prüfen („mehr als die Hälfte“, „um ein Drittel mehr“) | 3 | 3 | Aussage zu Diagramm prüfen |
| daten | 5.3 „jede 15.“ gegen 15 % | 3 | 3 | Aussage zu Diagramm prüfen |
| daten | 5.4 zwei Teilaussagen getrennt prüfen | 3 | 3 | Aussage zu Diagramm prüfen |
| daten | 5.7 Fortschreibung eines Trends prüfen | 3 | 3 | Aussage zu Diagramm prüfen |
| einheiten | 1.3 in die Nachbareinheit umrechnen, größer nach kleiner (mal) | 3 | 3 | Größen vergleichen · Fehler in Rechnung erklären und korrigieren |
| flaechen | 3.1 A aus g und h | 3 | 3 | Flächeninhalt Dreieck berechnen |
| flaechen | 3.4 stumpfwinklig, Höhe außerhalb | 3 | 3 | Flächeninhalt Dreieck berechnen |
| flaechen | 5.6 Sachaufgabe mit Entscheidung (reicht die Platte?) | 3 | 3 | Rechteckseite aus Fläche berechnen · Restfläche berechnen |
| koerper | 1.6 Netz von Quader oder Würfel mit Maßen zeichnen | 3 | 3 | Netz eines Prismas vervollständigen |
| koerper | 3.8 Netz eines Prismas vervollständigen (fehlende Rechtecke, Maße) | 3 | 3 | Netz eines Prismas vervollständigen |
| lineare-gleichungen | 1.1 Lösung durch Einsetzen prüfen (wA/fA) | 3 | 3 | Lösung durch Einsetzen prüfen |
| lineare-gleichungen | 1.2 Lösung durch Probieren finden | 3 | 3 | Lösung durch Einsetzen prüfen |
| lineare-gleichungssysteme | 4.2 aus zwei Angaben „zusammen …“ zwei Gleichungen aufstellen (nur aufstellen) | 3 | 3 | Lineares Gleichungssystem aufstellen |
| potenz-exponentialfunktionen | 1.1 an einer Tabelle entscheiden, ob die Zunahme immer gleich groß ist (Differenzen) oder immer derselbe Faktor wirkt (Quotienten) | 3 | 3 | Wachstumsart begründen · Wachstumsfaktor aus Tabelle bestimmen |
| prozentrechnung | 1.7 Anteilsaussage prüfen und korrigieren (Tabellenwerte) | 3 | 3 | Anteilsaussage prüfen und korrigieren |
| quadratische-funktionen | 4.7 Schnittpunkte Gerade und Parabel (gleichsetzen, alles auf eine Seite, lösen, y-Werte über die Gerade) | 3 | 3 | Schnittpunkte Gerade und Parabel berechnen |
| quadratische-funktionen | 4.8 Parabel in Scheitelpunktform gleichsetzen (Klammer auflösen) | 3 | 3 | Schnittpunkte Gerade und Parabel berechnen |
| quadratische-gleichungen | 3.11 Klammer oder Produkt zuerst auflösen (binomische Formel, x·(x + a)), dann ordnen | 3 | 3 | Schnittpunkte Gerade und Parabel berechnen |
| quadratische-gleichungen | 3.12 Gerade und Parabel gleichsetzen als Anwendung (Verfahren hier, Typ in quadratische-funktionen.md Einheit 4) | 3 | 3 | Schnittpunkte Gerade und Parabel berechnen |
| quadratische-gleichungen | 3.5 p ungerade: p halbe als Dezimalzahl | 3 | 3 | Schnittpunkte Gerade und Parabel berechnen |
| rationale-zahlen | 2.1 positive Zahl dazu oder weg von negativer Zahl (Zahlengerade) | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 2.2 negative Zahl addieren (Klammer) | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 2.3 negative Zahl subtrahieren (zwei Minus) | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 2.4 Zeichen zusammenfassen und rechnen | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 2.5 Beträge: gleiche Vorzeichen addieren, verschiedene subtrahieren | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 2.7 mehrere Summanden | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 2.8 Dezimalzahlen und Brüche | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 3.4 Potenzen: (−2)² gegen −2² | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 3.5 Punkt vor Strich mit negativen Zahlen | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 3.6 Termwert mit Klammer (5 · (x − 3) für x = −2) | 3 | 3 | Termwert berechnen |
| rationale-zahlen | 4.3 Termwert für gegebene Werte, auch Bruchterm (a + b) : c | 3 | 3 | Termwert berechnen |
| strahlensaetze | 1.10 Rechteck und Kreis im gegebenen Maßstab zeichnen (Durchmesser umrechnen, Radius halbieren, Zirkel) | 3 | 3 | Draufsicht maßstabsgerecht zeichnen · Länge im Maßstab umrechnen |
| strahlensaetze | 1.3 Länge von der Wirklichkeit in die Zeichnung umrechnen: durch n teilen, vorher in cm umrechnen (Zaun 4 m bei 1 : 200 → 2 cm) | 3 | 3 | Länge im Maßstab umrechnen · Draufsicht maßstabsgerecht zeichnen |
| symmetrie-abbildungen | 2.1 Symmetrieachse einer Figur einzeichnen | 3 | 3 | Symmetrieachsen bestimmen |
| symmetrie-abbildungen | 2.11 Symmetrie der Vierecksarten im Haus der Vierecke zuordnen | 3 | 3 | Symmetrieachsen bestimmen |
| symmetrie-abbildungen | 2.2 prüfen, ob eine eingezeichnete Gerade Symmetrieachse ist (falten oder messen) | 3 | 3 | Symmetrieachsen bestimmen |
| symmetrie-abbildungen | 2.3 Anzahl der Symmetrieachsen einer Figur angeben (P10-Form: Quadrat, Rechteck, Raute, gleichschenkliges Trapez, Drachenviereck, gleichseitiges und gleichschenkliges Dreieck, Kreis, Buchstaben, Verkehrszeichen) | 3 | 3 | Symmetrieachsen bestimmen |
| symmetrie-abbildungen | 2.4 Figuren ohne Symmetrieachse erkennen (Parallelogramm) | 3 | 3 | Symmetrieachsen bestimmen |
| terme | 1.1 Termwert berechnen (auch negative Einsetzung) | 3 | 3 | Termwert berechnen · Term durch Zusammenfassen gleichartiger Glieder vereinfachen |
| winkel-dreiecke | 3.2 fehlender Winkel im Viereck (360°) | 3 | 3 | Winkel im Viereck berechnen |
| zuordnungen | 2.1 Tabelle ergänzen durch Verdoppeln und Halbieren | 3 | 3 | Proportionale Zuordnung Dreisatz |
| zuordnungen | 2.2 Hochrechnen (mal 3, mal 10) | 3 | 3 | Proportionale Zuordnung Dreisatz |
| zuordnungen | 2.3 Runterrechnen | 3 | 3 | Proportionale Zuordnung Dreisatz |
| zuordnungen | 2.4 auf eine Portion runterrechnen, dann hochrechnen (Dreisatz, Minitabelle) | 3 | 3 | Proportionale Zuordnung Dreisatz |
| zuordnungen | 2.5 fester Faktor angeben (Preis je Einheit), Gleichung y = k · x | 3 | 3 | Proportionale Zuordnung Dreisatz |
| daten | 2.7 Säule oder Balken mit gegebenem Wert ergänzen | 3 | 2 | Säulen- oder Balkendiagramm ergänzen |
| daten | 2.8 Diagramm aus einer Tabelle zeichnen (Skala wählen) | 3 | 2 | Säulen- oder Balkendiagramm ergänzen |
| daten | 5.12 Fehler finden (Verdopplung der Säulenhöhe als Verdopplung des Werts; nur „die Säulen sind verschieden hoch“ ohne die Achse) | 3 | 2 | Verzerrung eines Diagramms erklären |
| daten | 5.13 Begründen (warum die Achse bei 0 beginnen sollte) | 3 | 2 | Verzerrung eines Diagramms erklären |
| daten | 5.5 abgeschnittene Achse erklären (Säulenhöhe zeigt nur den Teil über dem Achsenanfang) | 3 | 2 | Verzerrung eines Diagramms erklären |
| daten | 5.6 gedehnte Achse | 3 | 2 | Verzerrung eines Diagramms erklären |
| koerper | 2.1 V = a · b · c mit ganzen Zahlen | 3 | 2 | Volumen Würfel berechnen · Volumen Prisma berechnen |
| lineare-funktionen | 5.1 Lineare Funktion aus Sachverhalt aufstellen | 3 | 2 | Lineare Funktion aus Sachverhalt aufstellen |
| prozentrechnung | 5.1 „um“ und „auf“ unterscheiden | 3 | 2 | Wert nach prozentualer Erhöhung berechnen |
| prozentrechnung | 5.2 neuer Wert über Prozentwert (dazu, weg) | 3 | 2 | Wert nach prozentualer Erhöhung berechnen |
| prozentrechnung | 5.3 neuer Wert über Faktor (1,2; 0,8) | 3 | 2 | Wert nach prozentualer Erhöhung berechnen |
| prozentrechnung | 5.6 Brutto/Netto (19 %, 7 %) | 3 | 2 | Wert nach prozentualer Erhöhung berechnen |
| quadratische-funktionen | 4.1 Nullstellen aus der Scheitelpunktform durch Wurzelziehen | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-funktionen | 4.3 Nullstellen aus der Normalform mit der p-q-Formel | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-funktionen | 4.5 Nullstellen mit Wurzel als Ergebnis (Näherungswert) | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-gleichungen | 1.2 x² = c ohne Quadratzahl (Wurzel stehen lassen, Näherungswert mit dem Taschenrechner) | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-gleichungen | 1.4 x² freistellen bei a·x² + b = 0 und a·x² = b (erst umformen, dann Wurzel) | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-gleichungen | 2.1 Produktform (x − a)·(x − b) = 0, jeden Faktor null setzen | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-gleichungen | 2.10 Nullstellen einer Normalform durch Faktorisieren als Alternative zur Formel (Vorrat) | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-gleichungen | 2.2 Vorzeichen in den Klammern (x + a) | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-gleichungen | 3.10 Probe mit einer Lösung | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| quadratische-gleichungen | 3.6 Lösungen mit Wurzel, Näherungswert runden | 3 | 2 | Nullstellen quadratische Funktion berechnen |
| zuordnungen | 1.4 Achseneinteilung für gegebene Werte wählen | 3 | 2 | Achseneinteilung wählen |
| zuordnungen | 4.5 Kosten aus Menge und Preis je Einheit | 3 | 2 | Kosten aus Menge und Preis berechnen |
| daten | 1.2 Häufigkeitstabelle aus einer Urliste | 3 | 1 | Kreisdiagramm zeichnen |
| daten | 3.5 Sektor mit dem Geodreieck ab dem Radius zeichnen | 3 | 1 | Kreisdiagramm zeichnen |
| daten | 3.6 Kreisdiagramm mit drei bis vier Sektoren aus Prozentangaben | 3 | 1 | Kreisdiagramm zeichnen |
| flaechen | 1.1 Rechteck A und u aus a und b | 3 | 1 | Flächeninhalt Rechteck berechnen · Umfang Rechteck berechnen |
| flaechen | 1.2 Quadrat A und u aus a | 3 | 1 | Flächeninhalt Rechteck berechnen · Umfang Rechteck berechnen |
| lineare-funktionen | 4.1 Gleichung aus Graph | 3 | 1 | Geradengleichung aus zwei Punkten |
| lineare-funktionen | 4.2 aus m und Punkt | 3 | 1 | Geradengleichung aus Punkt und einem Parameter bestimmen · Geradengleichung aus zwei Punkten · Gleichung einer Senkrechten aufstellen · Geradengleichung einer Parallelen durch einen Punkt bestimmen |
| lineare-funktionen | 4.3 aus zwei Punkten | 3 | 1 | Geradengleichung aus zwei Punkten · Geradengleichung einer Parallelen durch einen Punkt bestimmen |
| winkel-dreiecke | 1.7 Winkel aus Teilwinkeln (nebeneinander: Summe; ineinander: Differenz; Rest zum gestreckten oder vollen Winkel) | 3 | 1 | Winkel aus Teilwinkeln berechnen · Winkel in zusammengesetzter Figur kennzeichnen |
| brueche-dezimalzahlen | 1.7 Rest zum Ganzen (Tonne zu 2/3 voll – wie viel fehlt) | 2 | 2 | Bruchteil einer Größe berechnen |
| daten | 1.7 relative Häufigkeit aus einem Diagramm (Anzahl und Gesamtzahl ablesen) | 2 | 2 | Relative Häufigkeit angeben · Wert aus Diagramm ablesen |
| daten | 2.1 Wert einer Säule an der Skala ablesen (Hilfslinien zählen) | 2 | 2 | Wert aus Diagramm ablesen |
| daten | 2.3 Werte über oder unter einer Schwelle auswählen (Grenzwert zählt nicht mit) | 2 | 2 | Werte im Diagramm nach Bedingung auswählen |
| daten | 2.5 Achseneinteilung aus einer Säule mit bekanntem Wert bestimmen | 2 | 2 | Achsenskalierung aus Säule bestimmen |
| daten | 2.6 unbeschriftete Säule anhand der Höhe zuordnen | 2 | 2 | Achsenskalierung aus Säule bestimmen |
| daten | 4.4 Median bei ungerader Anzahl (sortieren) | 2 | 2 | Median bestimmen |
| daten | 4.5 Median bei gerader Anzahl | 2 | 2 | Median bestimmen |
| einheiten | 1.1 Einheiten der Länge, der Masse und des Geldes der Größe nach ordnen | 2 | 2 | Größen vergleichen |
| einheiten | 1.5 über zwei Stufen umrechnen (Millimeter in Meter) | 2 | 2 | Größen vergleichen · Materialbedarf aus Längen berechnen |
| einheiten | 1.8 Komma setzen: Größe in der Stellenwerttafel lesen | 2 | 2 | Größen vergleichen |
| einheiten | 1.9 zwei Größen mit verschiedenen Einheiten vergleichen und das Zeichen setzen (P10-Form) | 2 | 2 | Größen vergleichen |
| einheiten | 3.7 Liter in Milliliter und zurück (P10-Form) | 2 | 2 | Portionen aus Gesamtmenge berechnen · Materialbedarf aus Fläche berechnen |
| flaechen | 1.3 Umfang eines Vielecks aus allen Seiten | 2 | 2 | Umfang Rechteck berechnen · Umfang Trapez berechnen |
| flaechen | 1.4 Seite aus A und anderer Seite (A : b) | 2 | 2 | Rechteckseite aus Fläche berechnen |
| flaechen | 1.9 Einheit wechseln vor dem Rechnen (cm und m gemischt) | 2 | 2 | Rechteckseite aus Fläche berechnen |
| koerper | 1.1 Körper in der Umwelt, aus Schrägbild oder Netz benennen (Prisma, Pyramide, Quader – Ankreuzen) | 2 | 2 | Körper aus Netz oder Schrägbild benennen |
| koerper | 1.2 Grund- und Deckfläche, Seitenflächen benennen (auch beim liegenden Prisma) | 2 | 2 | Körper aus Netz oder Schrägbild benennen · Grundfläche im Netz kennzeichnen |
| koerper | 1.7 Schrägbild lesen: verdeckte Kanten, Maße entnehmen | 2 | 2 | Körper aus Netz oder Schrägbild benennen |
| koerper | 3.10 Sachaufgabe (Dach, Vitrine, Werbeprisma, Zelt, Schokoladenverpackung) | 2 | 2 | Volumen Prisma berechnen · Mantelfläche Prisma berechnen |
| koerper | 4.10 Volumen bei doppeltem Radius (vierfach) | 2 | 2 | Volumenänderung bei doppeltem Radius begründen · Volumen Kegel und Zylinder vergleichen |
| koerper | 4.5 Netz: Rechtecklänge gleich Umfang | 2 | 2 | Netz eines Zylinders erkennen · Mantelfläche Zylinder als Netz skizzieren |
| lineare-funktionen | 1.1 Proportionalität erkennen (Tabelle, Text) | 2 | 2 | Graph zu Tarif zuordnen |
| lineare-funktionen | 2.2 m mit Steigungsdreieck ablesen (auch negativ, auch Bruch) | 2 | 2 | Geradengleichung zu Graph zuordnen · Graph nach Eigenschaft auswählen |
| lineare-funktionen | 2.7 Begründen (ohne Rechnung: welche Gerade steiler) | 2 | 2 | Graph zu Tarif zuordnen |
| lineare-funktionen | 4.4 Gerade durch zwei Punkte zeichnen | 2 | 2 | Gerade durch zwei Punkte zeichnen |
| lineare-funktionen | 5.3 Graph zu Tarif zuordnen | 2 | 2 | Graph zu Tarif zuordnen |
| lineare-funktionen | 5.4 Endwert berechnen | 2 | 2 | Endwert linearer Veränderung berechnen |
| lineare-funktionen | 5.5 Tarife vergleichen mit Entscheidung | 2 | 2 | Tarife vergleichen |
| lineare-gleichungen | 4.1 Zahlenrätsel | 2 | 2 | Lineare Gleichung aus Sachverhalt aufstellen |
| lineare-gleichungen | 4.2 Alter, Geld, Verteilung | 2 | 2 | Lineare Gleichung aus Sachverhalt aufstellen |
| lineare-gleichungen | 4.6 Deutung der Lösung im Kontext | 2 | 2 | Lineare Gleichung aus Sachverhalt aufstellen |
| potenz-exponentialfunktionen | 1.12 Begründen (warum „jedes Jahr gleich viel Prozent“ nicht „jedes Jahr gleich viel Euro“ heißt) | 2 | 2 | Wachstumsart begründen |
| potenz-exponentialfunktionen | 1.2 Wachstumsart begründen: gleicher Prozentsatz vom jeweils vorigen Wert bedeutet gleicher Faktor, die Zuwächse in Euro oder Kilogramm werden größer (bei Abnahme kleiner) | 2 | 2 | Wachstumsart begründen |
| potenz-exponentialfunktionen | 1.3 dieselbe Entscheidung aus einem Text ohne Tabelle | 2 | 2 | Wachstumsart begründen |
| potenz-exponentialfunktionen | 1.7 Graph zu einem Wachstumsprozess auswählen: Startwert auf der y-Achse gegen Beginn im Ursprung, Gerade gegen gekrümmte Kurve | 2 | 2 | Graph zu Wachstumsprozess zuordnen |
| potenz-exponentialfunktionen | 1.8 begründen, warum die beiden anderen Graphen nicht passen | 2 | 2 | Graph zu Wachstumsprozess zuordnen |
| potenz-exponentialfunktionen | 1.9 Graph einer Abnahme (fallend, flacher werdend) erkennen | 2 | 2 | Graph zu Wachstumsprozess zuordnen |
| potenz-exponentialfunktionen | 2.10 Wachstumsrate aus zwei Werten bestimmen | 2 | 2 | Wachstumsfaktor aus Tabelle bestimmen · Parameter einer Exponentialfunktion bestimmen |
| potenz-exponentialfunktionen | 2.2 Faktor in den Prozentsatz zurück | 2 | 2 | Wachstumsfaktor aus Tabelle bestimmen |
| potenz-exponentialfunktionen | 2.3 Faktor als Quotient zweier aufeinanderfolgender Tabellenwerte nachweisen, mehrere Quotienten prüfen | 2 | 2 | Wachstumsfaktor aus Tabelle bestimmen |
| potenz-exponentialfunktionen | 4.1 Startwert verdoppeln oder halbieren und den Zielwert notieren | 2 | 2 | Verdopplungs- oder Halbwertszeit bestimmen |
| potenz-exponentialfunktionen | 4.2 Zielwert in einer Tabelle suchen und die Zeit ablesen | 2 | 2 | Verdopplungs- oder Halbwertszeit bestimmen |
| potenz-exponentialfunktionen | 4.3 Zielwert am Graphen suchen: Wert an der y-Achse, waagerecht zum Graphen, senkrecht zur x-Achse, Zeit ablesen | 2 | 2 | Verdopplungs- oder Halbwertszeit bestimmen |
| potenz-exponentialfunktionen | 4.4 das eigene Vorgehen in Worten beschreiben | 2 | 2 | Verdopplungs- oder Halbwertszeit bestimmen |
| potenz-exponentialfunktionen | 4.5 zwischen zwei Tabellenwerten die nächstliegende Zeit angeben (der Zielwert liegt selten genau auf einem Tabellenwert) | 2 | 2 | Verdopplungs- oder Halbwertszeit bestimmen |
| potenz-exponentialfunktionen | 4.7 Halbwertszeit beim Zerfall, Verdopplungszeit beim Wachstum benennen | 2 | 2 | Verdopplungs- oder Halbwertszeit bestimmen |
| potenzen-wurzeln | 1.1 Potenz als Malkette schreiben (3⁴ = 3 · 3 · 3 · 3) und Malkette als Potenz (2 · 2 · 2 · 2 · 2 = 2⁵) | 2 | 2 | Exponent einer Potenz bestimmen |
| potenzen-wurzeln | 1.11 Exponent bestimmen durch wiederholtes Malnehmen (2^x = 16: 2, 4, 8, 16 → x = 4; P10-Form) | 2 | 2 | Exponent einer Potenz bestimmen |
| potenzen-wurzeln | 1.12 Exponent bestimmen durch Zerlegen (256 = 4 · 4 · 4 · 4) | 2 | 2 | Exponent einer Potenz bestimmen |
| potenzen-wurzeln | 1.3 Potenz von Produkt unterscheiden und beide ausrechnen (4³ = 64, 4 · 3 = 12) | 2 | 2 | Exponent einer Potenz bestimmen |
| potenzen-wurzeln | 1.4 Quadratzahlen bis 20² aus dem Kopf, Kubikzahlen bis 10³ | 2 | 2 | Wurzel eines Quadrats berechnen · Quadratseite aus Fläche berechnen |
| potenzen-wurzeln | 3.1 Quadratzahl erkennen und Wurzel im Kopf (√169 = 13; Quadratzahlen bis 20²) | 2 | 2 | Wurzel eines Quadrats berechnen · Quadratseite aus Fläche berechnen |
| potenzen-wurzeln | 3.2 Wurzel als Umkehrung: „welche Zahl mal sich selbst gibt …“ | 2 | 2 | Wurzel eines Quadrats berechnen · Quadratseite aus Fläche berechnen |
| prozentrechnung | 4.1 glatte Sätze (50 %, 25 %, 20 %, 10 %: mal 2, 4, 5, 10) | 2 | 2 | Grundwert berechnen |
| prozentrechnung | 4.2 1 %-Weg (W : p, mal 100) | 2 | 2 | Grundwert berechnen |
| prozentrechnung | 4.3 beliebiger Satz mit Taschenrechner | 2 | 2 | Grundwert berechnen |
| prozentrechnung | 4.4 Sachtext („das sind 60 % der Klasse“) | 2 | 2 | Grundwert berechnen |
| prozentrechnung | 5.5 alter Wert aus neuem Wert und Prozentsatz | 2 | 2 | Grundwert berechnen |
| pyramide-kegel-kugel | 2.18 Begründen (drei Kegel füllen den Zylinder; warum das Volumen beim dreifachen Radius neunfach wird) | 2 | 2 | Volumen Kegel und Zylinder vergleichen · Volumenänderung bei doppeltem Radius begründen |
| quadratische-funktionen | 2.6 Parabel verschieben (nach oben/unten über e, nach rechts/links über d) und neue Gleichung oder neuen Scheitel angeben | 2 | 2 | Parabel verschieben · Parabeltransformation gegenüber der Normalparabel beschreiben |
| rationale-zahlen | 1.2 Zahlen an der Zahlengeraden eintragen und ablesen (ganze, Dezimalzahlen, Brüche) | 2 | 2 | Zahl zu Bedingung angeben |
| rationale-zahlen | 1.4 zwei Zahlen vergleichen (< >) | 2 | 2 | Zahl zu Bedingung angeben |
| rationale-zahlen | 1.6 Zahl zu Bedingung angeben („größer als −150“, „zwischen zwei Zahlen“) | 2 | 2 | Zahl zu Bedingung angeben |
| strahlensaetze | 1.1 Maßstab lesen und in Worten sagen (1 : 200 – ein Zentimeter auf dem Plan sind 200 cm = 2 m) | 2 | 2 | Länge im Maßstab umrechnen |
| strahlensaetze | 1.14 Landkarte: Strecke aus Kartenzentimetern (1 : 25 000 → 1 cm ≙ 250 m) | 2 | 2 | Länge im Maßstab umrechnen |
| strahlensaetze | 1.4 Länge von der Zeichnung in die Wirklichkeit: mal n, Ergebnis in eine sinnvolle Einheit (3 cm bei 1 : 200 → 600 cm = 6 m) | 2 | 2 | Länge im Maßstab umrechnen |
| strahlensaetze | 1.5 Modellmaße aus Originalmaßen (h = 30 m, 1 : 50 → 60 cm; P10-Form) und Originalmaße aus Modellmaßen (0,68 m bei 1 : 10 → 6,8 m; P10-Form) | 2 | 2 | Länge im Maßstab umrechnen |
| strahlensaetze | 1.6 zwei Größen in einer Aufgabe umrechnen (Höhe und Durchmesser) | 2 | 2 | Länge im Maßstab umrechnen |
| wahrscheinlichkeit | 1.2 Zählprinzip: Anzahl der Kombinationen als Produkt | 2 | 2 | Anzahl Kombinationen nach dem Zählprinzip bestimmen · Anzahl der Anordnungen bestimmen |
| wahrscheinlichkeit | 1.4 Anordnungen von drei Ziffern oder drei Personen (auflisten, dann 3 · 2 · 1) | 2 | 2 | Anzahl der Anordnungen bestimmen |
| winkel-dreiecke | 2.1 Scheitel- und Nebenwinkel benennen | 2 | 2 | Winkel über Scheitel- oder Nebenwinkel bestimmen |
| winkel-dreiecke | 2.2 aus einem Winkel die drei anderen an der Kreuzung | 2 | 2 | Winkel über Scheitel- oder Nebenwinkel bestimmen |
| winkel-dreiecke | 2.4 Stufenwinkel an Parallelen | 2 | 2 | Winkel an geschnittenen Parallelen bestimmen |
| winkel-dreiecke | 2.5 Wechselwinkel | 2 | 2 | Winkel an geschnittenen Parallelen bestimmen |
| winkel-dreiecke | 2.6 Nebenwinkel des Stufenwinkels (180° − …) | 2 | 2 | Winkel an geschnittenen Parallelen bestimmen |
| winkel-dreiecke | 3.11 Vierecksart-Eigenschaft ankreuzen („In jedem Trapez …“, „In jedem Parallelogramm …“) | 2 | 2 | Eigenschaft einer Figur zuordnen |
| zuordnungen | 1.6 Graph zu Situation qualitativ zuordnen (Füllgraph, Weg-Zeit) | 2 | 2 | Graph zu Tarif zuordnen |
| zuordnungen | 4.2 aus Text (je mehr, desto mehr – reicht nicht: Nullwert prüfen) | 2 | 2 | Graph zu Tarif zuordnen |
| zuordnungen | 4.3 aus Graph (Ursprungsgerade, fallende Kurve, andere) | 2 | 2 | Graph zu Tarif zuordnen |
| zuordnungen | 4.4 Gegenbeispiele (Alter und Größe, Tarif mit Grundgebühr) | 2 | 2 | Graph zu Tarif zuordnen |
| einheiten | 2.7 Endzeit aus Startzeit und Dauer mit Übertrag bei sechzig Minuten (P10-Form) | 2 | 1 | Uhrzeit aus Startzeit und Dauer berechnen |
| einheiten | 2.8 Startzeit aus Endzeit und Dauer | 2 | 1 | Uhrzeit aus Startzeit und Dauer berechnen |
| einheiten | 2.9 Dauer mit Pause (zwei Abschnitte addieren) | 2 | 1 | Uhrzeit aus Startzeit und Dauer berechnen |
| koerper | 3.1 Grundfläche erkennen und markieren (auch liegend) | 2 | 1 | Volumen Prisma berechnen · Grundfläche im Netz kennzeichnen |
| koerper | 3.2 V = G · h mit gegebener Grundfläche | 2 | 1 | Volumen Prisma berechnen |
| koerper | 3.3 Rechteckgrundfläche (Quader als Prisma) | 2 | 1 | Volumen Prisma berechnen |
| koerper | 3.4 Dreiecksgrundfläche (G = g · h_g : 2) | 2 | 1 | Volumen Prisma berechnen |
| koerper | 3.5 Trapezgrundfläche | 2 | 1 | Volumen Prisma berechnen |
| koerper | 5.10 Fehler finden (Klammer fehlt, h wirkt nur auf einen Teil; Radius als Mindestbreite) | 2 | 1 | Term zu Körper angeben · Verpackungsmaße aus Körpermaßen bestimmen |
| lineare-funktionen | 3.2 Argument zum Funktionswert | 2 | 1 | Nullstelle lineare Funktion berechnen |
| lineare-funktionen | 3.5 Nullstelle berechnen | 2 | 1 | Nullstelle lineare Funktion berechnen |
| pyramide-kegel-kugel | 2.16 Sachaufgabe (Trichter, Eistüte, Verkehrshütchen, Sandhaufen, Sektglas, Zelt) | 2 | 1 | Volumen Kegel berechnen · Mantelfläche Kegel berechnen |
| flaechen | 1.7 aus Rechtecken zusammengesetzte Fläche (Summe) | 2 | 0 | Flächeninhalt Rechteck berechnen |
| quadratische-funktionen | 2.7 an der x-Achse spiegeln (Minus vor den ganzen Term) | 2 | 0 | Parabel an der x-Achse spiegeln |
| binomische-formeln | 2.1 gleiche Klammer zweimal erkennen ((a + b)² ist (a + b)·(a + b)) | 1 | 1 | Scheitelpunktform in Normalform umformen |
| binomische-formeln | 2.10 Klammer mit Formel auflösen und mit dem Rest zusammenfassen (Scheitelpunktform → Normalform) | 1 | 1 | Scheitelpunktform in Normalform umformen |
| binomische-formeln | 2.11 Nachweis „Normalform stimmt“ (P10-Form) | 1 | 1 | Scheitelpunktform in Normalform umformen |
| binomische-formeln | 2.2 erste binomische Formel mit x und Zahl | 1 | 1 | Scheitelpunktform in Normalform umformen |
| brueche-dezimalzahlen | 4.3 Dezimalzahl am Zahlenstrahl (Zehntel-, Hundertstelskala) eintragen und ablesen | 1 | 1 | Mitte zweier Zahlen bestimmen |
| brueche-dezimalzahlen | 5.5 Mitte zweier Zahlen (Mittelwert oder Zahlenstrahl eine Stelle feiner) | 1 | 1 | Mitte zweier Zahlen bestimmen |
| daten | 1.3 relative Häufigkeit als Bruch (22 von 34) | 1 | 1 | Relative Häufigkeit angeben |
| daten | 1.4 als Dezimalzahl und in Prozent (Taschenrechner, runden) | 1 | 1 | Relative Häufigkeit angeben |
| daten | 1.6 häufigster und seltenster Wert | 1 | 1 | Modalwert bestimmen · Kenngrößen einer Liste prüfen |
| daten | 3.1 Anteil in Prozent → Streifenabschnitt (1 mm je 1 % bei 10 cm) | 1 | 1 | Streifendiagramm zeichnen |
| daten | 3.2 Streifen mit vier Abschnitten zeichnen und beschriften | 1 | 1 | Streifendiagramm zeichnen |
| daten | 4.10 fehlender Wert aus Mittelwert und den übrigen Werten | 1 | 1 | Fehlenden Wert aus Mittelwert bestimmen |
| daten | 4.12 Aussagen zu Kenngrößen prüfen und korrigieren | 1 | 1 | Kenngrößen einer Liste prüfen |
| daten | 4.3 Modalwert | 1 | 1 | Modalwert bestimmen · Kenngrößen einer Liste prüfen |
| einheiten | 1.11 Umrechnen mit gegebenem Faktor bei nichtmetrischen Einheiten (Fuß, Meile, Zoll; P10-Form) | 1 | 1 | Längeneinheit mit Faktor umrechnen |
| einheiten | 1.12 Nachweis einer vorgegebenen Länge mit dem Faktor (P10-Form) | 1 | 1 | Längeneinheit mit Faktor umrechnen |
| einheiten | 3.13 Fehler finden (Flächeneinheit mit zehn statt hundert umgerechnet; Kubikmeter mit hundert statt tausend in Liter) | 1 | 1 | Fehler in Rechnung erklären und korrigieren |
| einheiten | 3.9 Portionen aus einer Gesamtmenge nach Umrechnung (P10-Form) | 1 | 1 | Portionen aus Gesamtmenge berechnen |
| einheiten | 4.1 gegebene Größen vor dem Rechnen auf eine Einheit bringen | 1 | 1 | Portionen aus Gesamtmenge berechnen |
| einheiten | 4.10 eine fremde Rechnung nachrechnen und den Einheitenfehler benennen (P10-Form) | 1 | 1 | Fehler in Rechnung erklären und korrigieren |
| einheiten | 4.11 die Rechnung berichtigen und die Behauptung korrigieren (P10-Form) | 1 | 1 | Fehler in Rechnung erklären und korrigieren |
| einheiten | 4.12 Fehler finden (Faktor tausend statt hundert bei Euro und Cent; nur eine der beiden Größen umgerechnet) | 1 | 1 | Fehler in Rechnung erklären und korrigieren |
| einheiten | 4.2 Ergebnis in eine sinnvolle Einheit umrechnen (0,6 m als 60 cm angeben) | 1 | 1 | Materialbedarf aus Fläche berechnen |
| einheiten | 4.4 Volumen aus Masse und Dichte durch Umstellen (P10-Form) | 1 | 1 | Volumen aus Masse und Dichte berechnen |
| einheiten | 4.7 Materialbedarf aus Fläche und Ergiebigkeit, mehrere Flächen, zweiter Anstrich (P10-Form) | 1 | 1 | Materialbedarf aus Fläche berechnen |
| einheiten | 4.8 Bedarf mit Gebindegrößen vergleichen und entscheiden (P10-Form) | 1 | 1 | Materialbedarf aus Fläche berechnen · Materialbedarf aus Längen berechnen |
| einheiten | 4.9 Euro und Cent in einer Rechnung | 1 | 1 | Fehler in Rechnung erklären und korrigieren |
| flaechen | 1.5 Seite aus u und anderer Seite | 1 | 1 | Rechteckseite aus Umfang berechnen |
| flaechen | 1.6 Quadratseite als Wurzel aus A | 1 | 1 | Quadratseite aus Fläche berechnen |
| flaechen | 3.5 g oder h aus A (umstellen) | 1 | 1 | Grundseite aus Dreiecksfläche berechnen |
| flaechen | 4.1 Trapez A aus a, c, h | 1 | 1 | Flächeninhalt Trapez berechnen |
| flaechen | 4.2 Höhe aus A und den parallelen Seiten | 1 | 1 | Trapezhöhe aus Fläche berechnen |
| flaechen | 4.3 Umfang mit gegebenen Schenkeln | 1 | 1 | Umfang Trapez berechnen |
| flaechen | 4.4 Umfang mit Schenkel aus Pythagoras oder Sinus (Vorrat) | 1 | 1 | Umfang Trapez berechnen |
| flaechen | 4.5 Drachen und Raute A aus e und f | 1 | 1 | Flächeninhalt Drachenviereck berechnen |
| flaechen | 5.1 Teilflächen erkennen und benennen (Rechteck, Dreieck, Halbkreis) | 1 | 1 | Figur in Teilflächen zerlegen |
| flaechen | 5.2 Fläche als Summe | 1 | 1 | Flächeninhalt zusammengesetzter Figur berechnen |
| flaechen | 5.4 Restfläche (Rechteck minus Kreis oder Quadrat) | 1 | 1 | Restfläche berechnen |
| flaechen | 5.7 Verschnitt in Prozent (Vorrat, Niveau III) | 1 | 1 | Verschnitt in Prozent berechnen |
| koerper | 1.10 Körper in ein Schrägbild einzeichnen (Kegel im Quader) | 1 | 1 | Körper in Schrägbild skizzieren |
| koerper | 1.3 Ecken, Kanten, Flächen zählen (Quader, Dreiecksprisma, quadratische Pyramide) | 1 | 1 | Kantenzahl eines Körpers angeben |
| koerper | 1.5 Gegenfläche im Würfelnetz markieren | 1 | 1 | Gegenfläche im Würfelnetz bestimmen |
| koerper | 1.9 Schrägbild beschriften, Körperhöhe einzeichnen | 1 | 1 | Körperskizze beschriften |
| koerper | 2.2 Würfel a³ | 1 | 1 | Volumen Würfel berechnen |
| koerper | 3.6 Mantel als Rechtecke (Umfang der Grundfläche · h) | 1 | 1 | Mantelfläche Prisma berechnen |
| koerper | 4.13 Begründen (warum vierfach) | 1 | 1 | Volumenänderung bei doppeltem Radius begründen |
| koerper | 4.4 Mantel M = 2 · π · r · h (Umfang mal Höhe) | 1 | 1 | Mantelfläche Zylinder berechnen |
| koerper | 4.7 h aus V | 1 | 1 | Höhe eines Zylinders aus Volumen berechnen |
| koerper | 4.8 r aus V (Wurzel) | 1 | 1 | Radius eines Zylinders aus Volumen berechnen |
| koerper | 5.1 Körper in Teilkörper zerlegen und benennen (Haus = Quader + Dreiecksprisma; Pool = Quader + Halbzylinder) | 1 | 1 | Term zu Körper angeben · Volumen zusammengesetzter Körper berechnen |
| koerper | 5.11 Begründen (Zerlegung erklären; warum Volumen teilen nicht reicht) | 1 | 1 | Packungsanzahl in Quader bestimmen |
| koerper | 5.2 Term zum Volumen aufstellen oder vorgegebene Terme prüfen (Klammer) | 1 | 1 | Term zu Körper angeben |
| koerper | 5.3 Volumen zusammengesetzter Körper | 1 | 1 | Volumen zusammengesetzter Körper berechnen · Term zu Körper angeben |
| koerper | 5.4 Restvolumen (Verpackung minus Inhalt) | 1 | 1 | Restvolumen berechnen |
| koerper | 5.6 Packungsanzahl in einer Kiste durch Anordnen | 1 | 1 | Packungsanzahl in Quader bestimmen |
| kreis | 3.1 Anteil aus dem Mittelpunktswinkel als Bruch (90° → 1/4) und als Prozent | 1 | 1 | Kreissektor Anteil berechnen |
| kreis | 3.6 Kreisring (großer Kreis minus kleiner Kreis) | 1 | 1 | Kreisringmaß aus Fläche berechnen · Restfläche berechnen |
| lineare-funktionen | 2.4 Gleichung zu Graph zuordnen | 1 | 1 | Geradengleichung zu Graph zuordnen |
| lineare-funktionen | 5.2 Gleichung zu Tarif zuordnen | 1 | 1 | Gleichung zu Tarif zuordnen |
| potenz-exponentialfunktionen | 3.10 Zerfall bis unter eine Schwelle | 1 | 1 | Zeitpunkt für Schwellenwert bei Wachstum bestimmen |
| potenz-exponentialfunktionen | 3.6 Zeitschritte zählen, wenn Jahreszahlen gegeben sind (Startjahr ist der Schritt null) | 1 | 1 | Zeitpunkt für Schwellenwert bei Wachstum bestimmen |
| potenz-exponentialfunktionen | 3.9 Zeitpunkt für einen Schwellenwert durch schrittweises Multiplizieren finden, Schritte zählen und den erreichten Wert angeben | 1 | 1 | Zeitpunkt für Schwellenwert bei Wachstum bestimmen |
| potenz-exponentialfunktionen | 4.6 durch Probieren mit dem Faktor rechnen, bis der Zielwert erreicht ist | 1 | 1 | Zeitpunkt für Schwellenwert bei Wachstum bestimmen |
| potenzen-wurzeln | 1.6 Potenz mit negativer Basis: Vorzeichen aus gerader oder ungerader Hochzahl ((−3)⁴ = 81, (−3)³ = −27), Klammer gegen kein Klammer (−3⁴ = −81) | 1 | 1 | Wurzel eines Quadrats berechnen |
| potenzen-wurzeln | 2.3 große Zahl mit 10, 100, 1000 vervielfachen: Nullen anhängen, Ergebnis ausgeschrieben (P10-Form) | 1 | 1 | Große Zahl mit Zehnerpotenz multiplizieren |
| potenzen-wurzeln | 3.11 Quadratseite aus dem Flächeninhalt (a = √A; Typ in flaechen.md Einheit 1) | 1 | 1 | Quadratseite aus Fläche berechnen |
| potenzen-wurzeln | 3.7 Wurzel eines Quadrats: erst das Quadrat, dann die Wurzel (√((−4)²) = √16 = 4; die richtige von drei Aussagen ankreuzen; P10-Form) | 1 | 1 | Wurzel eines Quadrats berechnen |
| potenzen-wurzeln | 3.9 Wurzel aus einer negativen Zahl: kein Wert (√(−9) gegen −√9) | 1 | 1 | Wurzel eines Quadrats berechnen |
| prozentrechnung | 1.6 fehlenden Anteil zu 100 % ergänzen | 1 | 1 | Fehlenden Prozentanteil ergänzen |
| prozentrechnung | 5.8 Steigung in Prozent deuten und berechnen | 1 | 1 | Steigung in Prozent deuten · Steigung in Prozent berechnen |
| pyramide-kegel-kugel | 2.12 Kegeldach auf einem Zylinder: Dachfläche, Materialkosten, Gesamthöhe | 1 | 1 | Mantelfläche Kegel berechnen |
| pyramide-kegel-kugel | 2.13 Kegel in Zylinderverpackung (Restvolumen → koerper.md Einheit 5) | 1 | 1 | Restvolumen berechnen · Volumen Kegel berechnen |
| pyramide-kegel-kugel | 2.14 Volumen des Kegels gegen den Zylinder mit gleichem r und h (ein Drittel) | 1 | 1 | Volumen Kegel und Zylinder vergleichen |
| pyramide-kegel-kugel | 2.15 Aussage über den dreifachen Radius rechnerisch prüfen (Niveau III) | 1 | 1 | Volumen Kegel und Zylinder vergleichen |
| pyramide-kegel-kugel | 2.7 Mantel M = π · r · s | 1 | 1 | Mantelfläche Kegel berechnen |
| pyramide-kegel-kugel | 3.11 Kugel in der Würfelschachtel: Kante gleich Durchmesser, Restvolumen | 1 | 1 | Restvolumen berechnen · Kugeldurchmesser aus Anordnung bestimmen |
| pyramide-kegel-kugel | 3.2 V = 4/3 · π · r³ mit r | 1 | 1 | Volumen Kugel berechnen |
| pyramide-kegel-kugel | 3.3 aus d | 1 | 1 | Volumen Kugel berechnen |
| pythagoras | 1.2 Satz in Worten: die richtige von drei Aussagen ankreuzen (Kathetenquadrate und Hypotenusenquadrat; P10-Form) | 1 | 1 | Satz des Pythagoras formulieren |
| pythagoras | 2.10 rechten Winkel mit der Umkehrung begründen (Verfahren; Typ in winkel-dreiecke.md Einheit 3) | 1 | 1 | Rechten Winkel begründen |
| pythagoras | 2.13 Begründen (warum bei gesuchter Kathete subtrahiert wird; warum die Zwölfknotenschnur mit den Abschnitten drei, vier, fünf einen rechten Winkel liefert) | 1 | 1 | Rechten Winkel begründen |
| pythagoras | 2.9 Umkehrung: drei Seiten gegeben, längste Seite als c, a² + b² mit c² vergleichen, rechtwinklig oder nicht (Antwort mit Rechnung) | 1 | 1 | Rechten Winkel begründen |
| pythagoras | 3.11 Mantellinie des Kegels aus Radius und Höhe, Radius zuerst aus dem Durchmesser | 1 | 1 | Mantellinie Kegel bestimmen |
| pythagoras | 3.13 Rechenweg ohne Zahlen beschreiben (P10-Form) | 1 | 1 | Mantellinie Kegel bestimmen |
| pythagoras | 3.9 Streckenlänge aus Koordinaten: Differenzen der x- und y-Werte als Katheten, auch negative Koordinaten (P10-Form) | 1 | 1 | Streckenlänge aus Koordinaten berechnen |
| quadratische-funktionen | 1.2 Punkte eintragen und Normalparabel zeichnen (Bogen, kein Lineal) | 1 | 1 | Parabel aus Gleichung skizzieren |
| quadratische-funktionen | 1.7 Öffnung und Breite an a erkennen (a < 0 nach unten; a größer als 1 schmaler; a zwischen 0 und 1 breiter) | 1 | 1 | Parabelgleichung zu Graph zuordnen · Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen · Parabeltransformation gegenüber der Normalparabel beschreiben |
| quadratische-funktionen | 1.8 Parabel zu a·x² zeichnen (Schablone reicht nicht; LISUM G, kein P10-Original) | 1 | 1 | Parabelgleichung aus Scheitel und Punkt bestimmen · Parabel aus Gleichung skizzieren |
| quadratische-funktionen | 1.9 Parabelgleichung zu Graph zuordnen über Öffnung, Streckung und Startwert, mit Begründung | 1 | 1 | Parabelgleichung zu Graph zuordnen |
| quadratische-funktionen | 2.10 Lage zweier Parabeln begründen (gleicher Scheitel, entgegengesetzte Öffnung; Scheitel über- oder untereinander) | 1 | 1 | Lage zweier Parabeln begründen · Anzahl gemeinsamer Punkte zweier Graphen begründen |
| quadratische-funktionen | 2.3 Parabel aus der Gleichung skizzieren (Scheitel setzen, Normalparabel-Punkte vom Scheitel aus) | 1 | 1 | Parabel aus Gleichung skizzieren |
| quadratische-funktionen | 2.8 an der y-Achse spiegeln (d wechselt das Vorzeichen) | 1 | 1 | Parabel an der y-Achse spiegeln |
| quadratische-funktionen | 2.9 Parabel zu Eigenschaften angeben (Scheitel auf einer Achse, keine Nullstellen, Öffnung; mehrere Lösungen) | 1 | 1 | Parabel zu Eigenschaften angeben |
| quadratische-funktionen | 3.3 Scheitelpunktform ausmultiplizieren (binomische Formel) und zusammenfassen | 1 | 1 | Scheitelpunktform in Normalform umformen |
| quadratische-funktionen | 3.4 Nachweis „Normalform stimmt“ (Behauptung prüfen) | 1 | 1 | Scheitelpunktform in Normalform umformen |
| quadratische-funktionen | 4.10 Gerade ohne gemeinsamen Punkt mit der Parabel angeben (waagerecht jenseits des Scheitels) | 1 | 1 | Gerade ohne gemeinsamen Punkt mit Parabel angeben |
| quadratische-funktionen | 4.6 Argument zu gegebenem Funktionswert (Gleichung aufstellen, ordnen, lösen) | 1 | 1 | Argument zu Funktionswert berechnen |
| quadratische-gleichungen | 1.1 x² = c mit Quadratzahl lösen, beide Lösungen (x₁ = √c, x₂ = −√c) | 1 | 1 | Argument zu Funktionswert berechnen |
| quadratische-gleichungen | 1.11 Gleichung ohne Lösung angeben | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| quadratische-gleichungen | 1.12 Aussagen zu Lösungen als wahr oder falsch beurteilen (P10-Form) | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| quadratische-gleichungen | 1.13 Fehler finden (nur die positive Wurzel; Vorzeichen von d beim Rückwärtsrechnen; Wurzel aus einer negativen Zahl „gezogen“) | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| quadratische-gleichungen | 1.14 Begründen (warum x² = c mit positivem c zwei Lösungen hat; warum x² = c mit negativem c keine hat) | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| quadratische-gleichungen | 1.3 x² = c mit negativem c: keine Lösung | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| quadratische-gleichungen | 1.5 a·x² + b = c mit beliebiger rechter Seite und Fallbetrachtung (GYM) | 1 | 1 | Argument zu Funktionswert berechnen |
| quadratische-gleichungen | 1.7 (x − d)² = 0: genau eine Lösung | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| quadratische-gleichungen | 1.8 Lösung durch Einsetzen prüfen, auch negativ, (wA)/(fA) | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| quadratische-gleichungen | 1.9 Zahl der Lösungen an c begründen (positiv, null, negativ) | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| quadratische-gleichungen | 2.3 gleiche Faktoren (x − a)² = 0: eine Lösung | 1 | 1 | Lösbarkeit quadratischer Gleichung beurteilen |
| rationale-zahlen | 3.3 mehrere Faktoren (Anzahl der Minuszeichen) | 1 | 1 | Vorzeichenregel anwenden |
| rationale-zahlen | 3.7 Vorzeichenregel als Aussage prüfen | 1 | 1 | Vorzeichenregel anwenden |
| rationale-zahlen | 4.6 Ausgangswert aus Differenz („8 512 mehr als“) | 1 | 1 | Ausgangswert aus Differenz berechnen |
| rationale-zahlen | 4.7 günstigste Preiskombination (Vorrat, Niveau III) | 1 | 1 | Günstigste Preiskombination bestimmen |
| strahlensaetze | 1.11 Draufsicht eines Körpers als Figur erkennen (Zylinder → Kreis, Quader → Rechteck, Turm auf Platte → Kreis im Rechteck) | 1 | 1 | Draufsicht maßstabsgerecht zeichnen |
| strahlensaetze | 1.12 Maßstab für ein Zeichenfeld wählen (passt 1 : 5, 1 : 10 oder 1 : 20 ins Feld?), angeben und die Zeichnung beschriften (P10-Form) | 1 | 1 | Draufsicht maßstabsgerecht zeichnen |
| strahlensaetze | 1.13 an der Zeichnung entscheiden (bedeckt die Platte die Tonne? Überstand ablesen; P10-Form) | 1 | 1 | Draufsicht maßstabsgerecht zeichnen |
| symmetrie-abbildungen | 1.1 Achsen und Ursprung benennen, Einteilung ablesen | 1 | 1 | Lage eines Punktes zu den Achsen erkennen |
| symmetrie-abbildungen | 1.4 Schreibweise P(x | y) lesen und schreiben (erste Zahl nach rechts, zweite nach oben) | 1 | 1 | Lage eines Punktes zu den Achsen erkennen |
| symmetrie-abbildungen | 1.7 Lage zu den Achsen erkennen: Punkt auf der Rechtsachse, auf der Hochachse, im Ursprung (P10-Form) | 1 | 1 | Lage eines Punktes zu den Achsen erkennen |
| symmetrie-abbildungen | 2.10 die Figur aus Dreieck und Spiegelbild benennen (P10-Form: Drachenviereck, bei gleichschenkligem Dreieck Raute) | 1 | 1 | Figur nach Spiegelung benennen |
| trigonometrie | 1.14 Gleichung ohne Figur nach der Seite umstellen, Seite im Nenner (P10-Form) | 1 | 1 | Trigonometrische Gleichung nach Seite umstellen |
| wahrscheinlichkeit | 1.5 größte und kleinste Zahl aus Ziffern | 1 | 1 | Größte Zahl aus Ziffern bilden |
| wahrscheinlichkeit | 1.9 Dreiecke aus fünf Punkten (Punkte auf einer Geraden ausschließen) | 1 | 1 | Anzahl der Dreiecke aus Punkten bestimmen · Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen |
| wahrscheinlichkeit | 3.7 „nicht zweimal gerade“ | 1 | 1 | Wahrscheinlichkeit über Gegenereignis berechnen |
| winkel-dreiecke | 3.5 aus gleichen Winkeln auf gleiche Schenkel schließen (Seite angeben) | 1 | 1 | Gleichschenkliges Dreieck erkennen |
| winkel-dreiecke | 3.9 rechten Winkel begründen (gleichschenklig-rechtwinklig 45° + 45°; Winkelsumme) | 1 | 1 | Rechten Winkel begründen |
| winkel-dreiecke | 4.9 Dreiecksungleichung: konstruierbar oder nicht (b + c > a) | 1 | 1 | Dreiecksungleichung anwenden |
| winkel-dreiecke | 5.8 rechten Winkel mit Thales begründen | 1 | 1 | Rechten Winkel begründen · Dreiecksart aus Koordinaten nachweisen |
| zinsrechnung | 1.3 Guthaben nach einem Jahr: Kapital plus Zinsen (408 € – nicht mit den Zinsen verwechseln) | 1 | 1 | Guthabentabelle mit Zinsen ergänzen |
| zinsrechnung | 2.1 Zinsen ans Guthaben anhängen, neues Guthaben nach einem Jahr (200 € → 204 €) | 1 | 1 | Guthabentabelle mit Zinsen ergänzen · Zinseszins Endkapital berechnen |
| zinsrechnung | 2.12 Ratenkauf und Kredit mit Zinseszins (Vorrat, Verbrauchersicht) | 1 | 1 | Zinseszins Endkapital berechnen |
| zinsrechnung | 2.2 Zinsen im zweiten Jahr vom neuen Guthaben (204 · 0,02 = 4,08 €), Guthaben nach zwei Jahren Schritt für Schritt | 1 | 1 | Guthabentabelle mit Zinsen ergänzen · Zinseszins Endkapital berechnen |
| zinsrechnung | 2.3 Guthabentabelle mit den Spalten Zinsen, Einzahlung und Guthaben um eine Zeile fortschreiben (Zinsen = Zinssatz vom Guthaben der Vorzeile; Guthaben = altes Guthaben + Zinsen + Einzahlung) | 1 | 1 | Guthabentabelle mit Zinsen ergänzen |
| zinsrechnung | 2.4 zwei fehlende Felder in einer gegebenen Tabelle ergänzen, Kontrolle über die nächste gegebene Zeile (P10-Form 2014-OS-K3b) | 1 | 1 | Guthabentabelle mit Zinsen ergänzen |
| zinsrechnung | 2.5 Wachstumsfaktor: „plus 2 %“ ist „mal 1,02“, q = 1 + p/100 | 1 | 1 | Zinseszins Endkapital berechnen |
| zinsrechnung | 2.6 Endkapital nach n Jahren: Startkapital mal q hoch n mit dem Taschenrechner (1 000 € zu 3 % über 5 Jahre: 1000 · 1,03⁵ ≈ 1 159,27 €; P10-Form 2014-OS-K3c) oder Jahr für Jahr | 1 | 1 | Zinseszins Endkapital berechnen |
| zinsrechnung | 2.7 einfache Verzinsung und Zinseszins nebeneinander (1 150 € gegen 1 159,27 €) | 1 | 1 | Zinseszins Endkapital berechnen |
| zinsrechnung | 2.9 Guthaben nach n Jahren mit jährlicher Einzahlung (Tabelle statt Formel) | 1 | 1 | Guthabentabelle mit Zinsen ergänzen |
| zuordnungen | 4.6 Geschwindigkeit aus Weg und Zeit mit Einheitenwechsel | 1 | 1 | Geschwindigkeit aus Weg und Zeit berechnen |
| daten | 4.11 Mittelwert nach Hinzufügen oder Entfernen begründen | 1 | 0 | Veränderung des Mittelwerts begründen |
| einheiten | 4.3 Masse aus Volumen und Dichte (P10-Form) | 1 | 0 | Masse aus Volumen und Dichte berechnen |
| einheiten | 4.6 Masse eines Anteils (Füllgrad in Prozent) und Leermasse addieren (P10-Form) | 1 | 0 | Masse aus Volumen und Dichte berechnen |
| koerper | 5.5 kleinste Quaderverpackung aus Körpermaßen (Durchmesser, nicht Radius) | 1 | 0 | Verpackungsmaße aus Körpermaßen bestimmen |
| pyramide-kegel-kugel | 2.2 V = 1/3 · π · r² · h | 1 | 0 | Volumen Kegel berechnen |
| pyramide-kegel-kugel | 2.3 r aus d | 1 | 0 | Volumen Kegel berechnen |
| pyramide-kegel-kugel | 2.4 Liter (cm³ → dm³) | 1 | 0 | Volumen Kegel berechnen |
| einheiten | 1.13 Größen mit gleicher Einheit addieren und subtrahieren | 0 | 0 | Materialbedarf aus Längen berechnen |
| koerper | 1.8 Schrägbild eines Quaders auf Rasterpapier zeichnen (Tiefe halb, schräg) | 0 | 0 | Körper im Schrägbild darstellen |
| koerper | 2.6 Kante aus V und zwei Kanten | 0 | 0 | Grundkante aus Volumen berechnen |
| koerper | 2.8 aus zwei Quadern zusammengesetzt (Treppe, L-Form) | 0 | 0 | Volumen zusammengesetzter Körper berechnen |
| koerper | 5.7 Masse aus Volumen und Dichte (1 m³ Wasser = 1000 kg) | 0 | 0 | Volumen zusammengesetzter Körper berechnen |
| kreis | 1.10 Sachaufgabe (Rad: Weg bei mehreren Umdrehungen; Baumstamm; Reifen) | 0 | 0 | Kreisumfang berechnen |
| kreis | 1.5 u aus r | 0 | 0 | Kreisumfang berechnen |
| kreis | 1.6 u aus d | 0 | 0 | Kreisumfang berechnen |
| kreis | 2.5 r aus A (Wurzel) | 0 | 0 | Kreisringmaß aus Fläche berechnen |
| lineare-funktionen | 4.5 Schnittpunkt zweier Geraden rechnerisch | 0 | 0 | Lage zweier Geraden bestimmen |
| lineare-funktionen | 4.7 Begründen (Lage zweier Geraden) | 0 | 0 | Lage zweier Geraden bestimmen |
| potenz-exponentialfunktionen | 1.5 Wertepaare aus einer Tabelle als Punkte eintragen, Skala mit größeren Schritten lesen | 0 | 0 | Graph eines exponentiellen Vorgangs zeichnen |
| potenz-exponentialfunktionen | 3.4 Bestandteile einer gegebenen Gleichung deuten: Anfangswert, Faktor als „hundert Prozent plus Zuwachs“, Variable als Zeit | 0 | 0 | Gleichungskette im Sachzusammenhang erläutern |
| potenz-exponentialfunktionen | 4.9 Logarithmus für den genauen Zeitpunkt (Vorrat) | 0 | 0 | Zeit aus Exponentialgleichung berechnen · Aussage zu Logarithmusterm prüfen · Gleichungskette im Sachzusammenhang erläutern |
| pyramide-kegel-kugel | 1.13 Sachaufgabe (Zeltdach: Stoff; Glaspyramide: Volumen und Glasfläche; Kirchturmspitze; Modell im Maßstab) | 0 | 0 | Mantelfläche einer Pyramide berechnen |
| pyramide-kegel-kugel | 1.5 Seitenhöhe aus h und a/2 (Stützdreieck, Pythagoras) | 0 | 0 | Mantelfläche einer Pyramide berechnen |
| pyramide-kegel-kugel | 1.6 Flächeninhalt einer Seitenfläche (Dreieck mit h_s) | 0 | 0 | Mantelfläche einer Pyramide berechnen |
| pyramide-kegel-kugel | 1.7 Mantel M = 4 · a · h_s : 2 | 0 | 0 | Mantelfläche einer Pyramide berechnen |
| pyramide-kegel-kugel | 3.12 Sachaufgabe (Silo oder Turm mit Halbkugeldach, Eiskugel in der Tüte – Kegel plus Halbkugel) | 0 | 0 | Volumen zusammengesetzter Körper berechnen |
| pyramide-kegel-kugel | 3.4 Oberfläche O = 4 · π · r² | 0 | 0 | Kugeloberfläche berechnen |
| pyramide-kegel-kugel | 3.6 Halbkugel: Volumen halb, Oberfläche halb plus Schnittkreis | 0 | 0 | Volumen zusammengesetzter Körper berechnen · Kugelmaß aus Oberfläche berechnen |
| pyramide-kegel-kugel | 3.7 Masse aus Volumen und Dichte (Stoßkugel, Stahlkugel) | 0 | 0 | Volumen zusammengesetzter Körper berechnen |
| pyramide-kegel-kugel | 3.8 r aus O (Wurzel) | 0 | 0 | Kugelmaß aus Oberfläche berechnen |
| pyramide-kegel-kugel | 3.9 r aus V (Kubikwurzel, Vorrat) | 0 | 0 | Volumen zusammengesetzter Körper berechnen |
| quadratische-funktionen | 2.12 Streckfaktor vor der Klammer erkennen und Merkmale der gestreckten Parabel bestimmen (LISUM G, kein P10-Original) | 0 | 0 | Parabelgleichung aus Scheitel und Punkt bestimmen · Parabeltransformation gegenüber der Normalparabel beschreiben |
| quadratische-funktionen | 3.2 Funktionswert und Punktprobe in der Normalform mit negativem x | 0 | 0 | Scheitelpunkt einer Parabel rechnerisch nachweisen |
| quadratische-funktionen | 3.9 allgemeine Form a·x² + bx + c erkennen und Öffnung an a ablesen (Vorrat, H) | 0 | 0 | Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen |
| quadratische-funktionen | 4.11 Schnittpunkte zweier Parabeln berechnen (LISUM G, kein P10-Original) | 0 | 0 | Schnittpunkte zweier Parabeln berechnen |
| terme | 2.1 gleichartige Glieder zusammenfassen | 0 | 0 | Term durch Zusammenfassen gleichartiger Glieder vereinfachen · Term mit Klammern und Potenzen vereinfachen |
| terme | 2.2 Zusammenfassen mit Potenzen (x, x²) | 0 | 0 | Term durch Zusammenfassen gleichartiger Glieder vereinfachen · Term mit Klammern und Potenzen vereinfachen |
| terme | 2.3 Zahl mal Term | 0 | 0 | Binomische Formel anwenden |
| terme | 2.4 Term mal Term (x · x = x²) | 0 | 0 | Binomische Formel anwenden · Term mit Klammern und Potenzen vereinfachen |
| terme | 3.4 negative Zahl mal Klammer | 0 | 0 | Term mit Klammern und Potenzen vereinfachen |
| terme | 3.5 Klammer auflösen und zusammenfassen | 0 | 0 | Term mit Klammern und Potenzen vereinfachen |
| trigonometrie | 4.12 Winkel mit dem Sinussatz (kein P10-Original, RLP G) | 0 | 0 | Sinussatz Winkel berechnen |
| trigonometrie | 4.13 Kosinussatz für die dritte Seite aus zwei Seiten und dem eingeschlossenen Winkel (kein P10-Original, RLP G) | 0 | 0 | Kosinussatz Seite berechnen |
| trigonometrie | 4.14 Kosinussatz nach dem Winkel umgestellt (Vorrat, RLP H, LISUM-PH „nur GYM“) | 0 | 0 | Kosinussatz Winkel berechnen |
| wahrscheinlichkeit | 2.9 relative Häufigkeit einer Versuchsreihe mit P vergleichen; erwartete Anzahl bei n Versuchen | 0 | 0 | Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen |
| wahrscheinlichkeit | 4.8 Ereignis zu einer gegebenen Rechnung in Worten | 0 | 0 | Ereignis zu Wahrscheinlichkeitsterm beschreiben |
| winkel-dreiecke | 1.6 Winkel benennen, Scheitel und Schenkel markieren | 0 | 0 | Winkel in zusammengesetzter Figur kennzeichnen |
| winkel-dreiecke | 3.3 Dreieck nach Winkeln und Seiten einteilen (Ankreuzen) | 0 | 0 | Dreiecksart aus Koordinaten nachweisen |
| winkel-dreiecke | 4.10 kongruente Figuren erkennen und Ecken zuordnen | 0 | 0 | Winkel in zusammengesetzter Figur kennzeichnen |
| zuordnungen | 3.1 Tabelle ergänzen: doppelt → halb, dreifach → Drittel | 0 | 0 | Antiproportionale Zuordnung Dreisatz |
| zuordnungen | 3.2 Produkt prüfen (x · y gleich) | 0 | 0 | Antiproportionale Zuordnung Dreisatz |
| zuordnungen | 3.3 Dreisatz umgekehrt (auf eine Einheit hochrechnen, dann runter) | 0 | 0 | Antiproportionale Zuordnung Dreisatz |
| zuordnungen | 3.4 Sachtext (Arbeiter und Tage, Pumpen und Stunden, Geschwindigkeit und Fahrzeit bei fester Strecke) | 0 | 0 | Antiproportionale Zuordnung Dreisatz |

Zahl der Typen je Wert:

| P10-Jahrgänge | Typen (Haupt oder Neben) | Typen (nur Haupt) |
|---|---|---|
| 13 | 4 | 0 |
| 12 | 0 | 0 |
| 11 | 2 | 2 |
| 10 | 7 | 3 |
| 9 | 63 | 20 |
| 8 | 10 | 24 |
| 7 | 22 | 45 |
| 6 | 34 | 19 |
| 5 | 87 | 60 |
| 4 | 55 | 30 |
| 3 | 80 | 98 |
| 2 | 95 | 125 |
| 1 | 145 | 169 |
| 0 | 730 | 739 |

## Sek-I-Einheiten ohne P10-Typ („keine P10-Aufgabe“)

- bruchrechnung, Einheit 1 · Brüche addieren und subtrahieren – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- bruchrechnung, Einheit 2 · Dezimalzahlen addieren und subtrahieren – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- bruchrechnung, Einheit 3 · Brüche multiplizieren und dividieren – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- bruchrechnung, Einheit 4 · Dezimalzahlen multiplizieren und dividieren – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- bruchrechnung, Einheit 5 · Rechengesetze und Punkt vor Strich – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- reelle-zahlen, Einheit 1 · Irrationale Zahlen und Zahlbereiche – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- reelle-zahlen, Einheit 2 · Potenzgesetze – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- reelle-zahlen, Einheit 3 · Wurzelgesetze und rationale Exponenten – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- flaechen, Einheit 2 · Parallelogramm – themen.csv: „enthält Kreisaufgaben; kreis hat kein msa-Thema“
- symmetrie-abbildungen, Einheit 3 · Punktsymmetrie, Drehung, Verschiebung
- strahlensaetze, Einheit 2 · Zentrische Streckung und Ähnlichkeit – themen.csv: „Maßstab als proportionale Zuordnung; bis 27.09.2026 bei zuordnungen, katalog/index.md führt ihn bei strahlensaetze Einheit 1“
- strahlensaetze, Einheit 3 · Strahlensätze – themen.csv: „Maßstab als proportionale Zuordnung; bis 27.09.2026 bei zuordnungen, katalog/index.md führt ihn bei strahlensaetze Einheit 1“
- terme, Einheit 4 · Ausklammern – themen.csv: „binomische-formeln stecken hier oder in quadratische Gleichungen“
- lineare-gleichungssysteme, Einheit 3 · Additionsverfahren
- binomische-formeln, Einheit 1 · Summe mal Summe – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- binomische-formeln, Einheit 3 · Faktorisieren – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- quadratische-gleichungen, Einheit 4 · Sachaufgaben
- potenz-exponentialfunktionen, Einheit 5 · Potenzfunktionen mit natürlichem Exponenten
- trigonometrische-funktionen, Einheit 1 · Einheitskreis und Bogenmaß – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- trigonometrische-funktionen, Einheit 2 · Sinus- und Kosinusfunktion und ihre Merkmale – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- trigonometrische-funktionen, Einheit 3 · Parameter und Transformationen – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- trigonometrische-funktionen, Einheit 4 · Periodische Vorgänge modellieren – themen.csv: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“
- daten, Einheit 7 · Vierfeldertafel (Sek I)

## Sek I je Eintrag

### brueche-dezimalzahlen

themen.csv: „Brüche und Dezimalzahlen“.

**Einheit 1 · Bruch als Anteil** – P10-Jahrgänge 11 von 13 (davon Haupt 11); P10-Typen 2; Summe ertrag 13.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Bruchteil einer Fläche bestimmen | 11 | 9 | 9 | 2014 | 2026 | 10 | 0 |  |
| Bruchteil einer Größe berechnen | 2 | 2 | 2 | 2015 | 2018 | 2 | 0 |  |

- 1.1 Anteil an einer gleich geteilten Figur ablesen → „Bruchteil einer Fläche bestimmen“ – P10-Jahrgänge 9 (Haupt 9). Grund: Definition „Bruchteil einer markierten Teilfläche an einer Figur angeben“; 2014-OS-B1i (9 von 15 gleichen Feldern) und 2024-OS-B1b (8 von 16 Kästchen).
- 1.2 Anteil einzeichnen (Kästchen, Streifen, Kreis) → „Bruchteil einer Fläche bestimmen“ – P10-Jahrgänge 9 (Haupt 9). Außerhalb der Themen des Eintrags (zählt nicht): „Prozentanteil einer Rasterfläche markieren“. Grund: Definition „einen Bruchteil einer Figur durch Zerlegen markieren“ (2017-OS-B1a 6/7 schraffieren, 2021-OS-B1b 3/8 kennzeichnen, 2025-OS-B1c ein Viertel eines Quadrats); als Prozentanteil in 2014-GYM-B1g (8 % von 25 Kästchen).
- 1.3 Anteil bei ungleichen Teilen (erst gleich groß machen: halbe Kästchen, Sektoren verschiedener Größe) → „Bruchteil einer Fläche bestimmen“ – P10-Jahrgänge 9 (Haupt 9). Grund: 2019-OS-B1c (Sektoren zu 60° und 30° erst auf das Maß 30° bringen, 3/12) und 2024-OS-B1b (graue Fläche mit halben Kästchen).
- 1.4 unter mehreren Figuren die mit dem gegebenen Anteil auswählen (Ankreuzen) → „Bruchteil einer Fläche bestimmen“ – P10-Jahrgänge 9 (Haupt 9). Grund: Definition „unter mehreren Figuren die mit einem vorgegebenen Anteil auswählen“; 2026-FOR-B1b (Figur mit dem Anteil 1/3).
- 1.5 Anteil an einer Menge (Kinder, Plättchen) angeben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit einstufig“ · „Relative Häufigkeit angeben“. Grund: Anteil an einer Menge als Bruch im Kontext Zufall und Daten: 2015-OS-B1a (Anteil weißer Kugeln je Topf 4/6, 2/6, 3/6), 2019-OS-K6a (3 von 20 Stiften) und 2015-OS-K7b (22 von 34 Spielen als relative Häufigkeit).
- 1.6 Bruchteil einer Menge oder Größe berechnen (Ganzes : Nenner · Zähler; auch mit Komma und Einheit) → „Bruchteil einer Größe berechnen“ · „Bruchteil einer Fläche bestimmen“ – P10-Jahrgänge 11 (Haupt 11). Außerhalb der Themen des Eintrags (zählt nicht): „Aussage über Bruchteile einer Größe prüfen“ · „Gesamtmenge aus Pro-Kopf-Angabe berechnen“. Grund: Definition „Bruchteil einer Größe mit Einheit berechnen“ (2018-OS-B1a, 3/4 von 1,2 kg); dasselbe Verfahren in 2017-OS-B1a (28 : 7 · 6 = 24 Kästchen), 2021-GYM-B1b (ein Drittel von 60 km) und 2023-GYM-K4c (zwei Drittel von 128 kg je Einwohner).
- 1.7 Rest zum Ganzen (Tonne zu 2/3 voll – wie viel fehlt) → „Bruchteil einer Größe berechnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Aussage über Bruchteile einer Größe prüfen“. Grund: 2015-OS-B1h (Tonne zu 2/3 gefüllt, Rest 200 l statt der Füllmenge) und 2021-GYM-B1b (Rest der Strecke nach einem Drittel, davon ein Viertel).
- 1.8 Ganzes aus Bruchteil (Vorrat: ein Viertel sind 6 – wie viel ist alles) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Grundwert berechnen“. Grund: Ganzes aus einem Bruchteil ist das Verfahren des Grundwerts mit glattem Satz: 2023-OS-B1b (25 %, also ein Viertel, sind 200 €, mal 4).
- 1.9 Fehler finden (Zähler als Anzahl gelesen; Teil zu Rest statt Teil zu Ganzem) → kein P10-Typ
- 1.10 Begründen (warum das Stück kleiner wird, wenn mehr Kinder teilen) → kein P10-Typ

**Einheit 2 · Kürzen und Erweitern** – P10-Jahrgänge 9 von 13 (davon Haupt 9); P10-Typen 1; Summe ertrag 11.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Bruchteil einer Fläche bestimmen | 11 | 9 | 9 | 2014 | 2026 | 10 | 0 | nicht in der Zuordnungszeile der Einheit |

- 2.1 gleichwertige Brüche am Streifen finden → kein P10-Typ
- 2.2 Erweitern mit gegebener Zahl → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozent und Anteil umwandeln“ · „Wahrscheinlichkeit mehrstufig unabhängig“. Grund: Vorstufe des Erweiterns auf einen gegebenen Nenner: 1/5 = 20/100 in 2022-OS-B1f und 1/4 = 16/64 in 2014-OS-K6c.
- 2.3 Kürzen mit gegebener Zahl → „Bruchteil einer Fläche bestimmen“ – P10-Jahrgänge 9 (Haupt 9). Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit einstufig“. Grund: Vorstufe des vollständigen Kürzens mit einer Zahl: 9/15 = 3/5 in 2014-OS-B1i, 20/100 = 1/5 in 2014-OS-B1b.
- 2.4 vollständig kürzen → „Bruchteil einer Fläche bestimmen“ – P10-Jahrgänge 9 (Haupt 9). Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit einstufig“ · „Relative Häufigkeit angeben“ · „Wahrscheinlichkeit mehrstufig unabhängig“ · „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ · „Baumdiagramm ergänzen“ · „Wahrscheinlichkeit über Gegenereignis berechnen“. Grund: Das Ergebnis gilt erst vollständig gekürzt als fertig: 2014-OS-B1i (9/15 = 3/5, Voraussetzung „Bruch kürzen“), 2014-OS-B1d (4/6 = 2/3), 2015-OS-K7b (22/34 = 11/17), 2014-OS-K6c (26/64 = 13/32), 2019-OS-K6c (120/6840 = 1/57), 2026-FOR-K6b (15/36 = 5/12) und 2026-FOR-K6c (33/36 = 11/12).
- 2.5 auf gegebenen Nenner erweitern (Zwölftel, Hundertstel) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozent und Anteil umwandeln“ · „Wahrscheinlichkeit mehrstufig unabhängig“. Grund: Auf Hundertstel erweitern in 2022-OS-B1f (1/5 = 20/100 = 20 %), auf Vierundsechzigstel in 2014-OS-K6c (1/4 = 16/64 vor dem Addieren).
- 2.6 zwei Brüche gleichnamig machen (ein Nenner Vielfaches des anderen; beide erweitern; Nenner multiplizieren) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit mehrstufig unabhängig“. Grund: Summenregel mit einem Nenner als Vielfachem des anderen: 2014-OS-K6c (16/64 + 9/64 + 1/64) und 2025-OS-K3c (1/4 + 1/16 = 5/16).
- 2.7 unechter Bruch ↔ gemischte Zahl → kein P10-Typ
- 2.8 Bruch als Geteilt-Aufgabe (3 : 4 = 3/4, 5 : 2 = 2 1/2) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit einstufig“ · „Relative Häufigkeit angeben“ · „Termwert berechnen“. Grund: Quotient als Bruch: 20 : (80 + 20) = 20/100 in 2014-OS-B1b und 22 : 34 = 22/34 in 2015-OS-K7b; umgekehrt der Bruchterm (a + b)/c als 7 : (−2) in 2021-OS-B1g.
- 2.9 Fehler finden (nur der Zähler erweitert; mit einer Zahl gekürzt, die nur einen von beiden teilt) → kein P10-Typ
- 2.10 Begründen (warum Erweitern den Bruch nicht größer macht) → kein P10-Typ

**Einheit 3 · Brüche vergleichen** – P10-Jahrgänge 7 von 13 (davon Haupt 7); P10-Typen 1; Summe ertrag 7.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Zahlen in verschiedenen Darstellungen vergleichen | 7 | 7 | 7 | 2014 | 2023 | 7 | 0 | nicht in der Zuordnungszeile der Einheit |

- 3.1 gleicher Nenner (größerer Zähler) → kein P10-Typ
- 3.2 gleicher Zähler (größerer Nenner, kleinerer Bruch) → kein P10-Typ
- 3.3 Vergleich mit 1/2 und mit 1 → kein P10-Typ
- 3.4 gleichnamig machen und vergleichen → kein P10-Typ
- 3.5 Brüche am Zahlenstrahl ablesen und eintragen (Skala in Vierteln, Zehnteln, Zwölfteln) → kein P10-Typ
- 3.6 drei bis vier Brüche ordnen → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: Definition „Zahlen in … Bruchschreibweise in dieselbe Form bringen und ordnen“; Vorstufe mit Brüchen allein, kein Original ordnet nur Brüche.
- 3.7 Zahl zwischen zwei Brüchen angeben (erweitern, dann dazwischen wählen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahl zu Bedingung angeben“. Grund: Definition nennt „zwischen 1/2 und 4/5“; Original 2014-OS-B1c wird hier geführt, der Typ liegt in rationale-zahlen.md Einheit 1.
- 3.8 Anteile in Situationen vergleichen (Pizza, Download-Balken) → kein P10-Typ
- 3.9 Fehler finden („es fehlt nur ein Stück, also größer“) → kein P10-Typ
- 3.10 Begründen (warum 1/7 größer als 1/8 ist) → kein P10-Typ

**Einheit 4 · Dezimalzahlen** – P10-Jahrgänge 8 von 13 (davon Haupt 8); P10-Typen 2; Summe ertrag 8.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Zahlen in verschiedenen Darstellungen vergleichen | 7 | 7 | 7 | 2014 | 2023 | 7 | 0 | nicht in der Zuordnungszeile der Einheit |
| Mitte zweier Zahlen bestimmen | 1 | 1 | 1 | 2020 | 2020 | 1 | 0 | nicht in der Zuordnungszeile der Einheit |

- 4.1 Zahl in die Stellenwerttafel eintragen und ablesen (Zehntel, Hundertstel, Tausendstel) → kein P10-Typ
- 4.2 Zehnerbruch ↔ Dezimalzahl (auch mit Nullen: 3/100, 3/1000) → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit einstufig“. Grund: Hundertstel mit Null: 5 % = 5/100 = 0,05 in 2018-OS-B1d (Fehlerquelle 0,5) und P = 5/100 = 0,05 in 2016-GYM-B1f.
- 4.3 Dezimalzahl am Zahlenstrahl (Zehntel-, Hundertstelskala) eintragen und ablesen → „Mitte zweier Zahlen bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „als Mittelwert oder am Zahlenstrahl“; 2020-OS-B1f (Zahlenstrahl mit Hundertsteln zwischen −0,6 und −0,5).
- 4.4 Nachbarzahlen (Nachbar-Einer, -Zehntel, -Hundertstel) und Zählen in Schritten (0,2er-Schritte; über 2,9 hinaus) → kein P10-Typ
- 4.5 Bruch → Dezimalzahl durch Erweitern auf 10, 100, 1000 (Halbe, Viertel, Fünftel, Zwanzigstel, Fünfundzwanzigstel) → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Zahl zu Bedingung angeben“. Grund: Halbe und Fünftel als Dezimalzahlen: 3/2 = 1,5 und 8/5 = 1,6 in 2015-OS-B1c, 1/2 = 0,5 und 4/5 = 0,8 in 2014-OS-B1c.
- 4.6 Dezimalzahl → Bruch und kürzen (auch größer als 1) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Anteilsaussage prüfen und korrigieren“. Grund: 2023-OS-K6b: der Quotient 0,25 ist als „ein Viertel“ zu lesen, um die Aussage „ein Drittel“ zu widerlegen.
- 4.7 Bruch → Dezimalzahl durch Division (Achtel; Taschenrechner) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozent und Anteil umwandeln“ · „Relative Häufigkeit angeben“. Grund: Division mit Taschenrechner: 3 : 8 = 0,375 = 37,5 % in 2014-OS-K6a (Nebentyp) und 22 : 34 ≈ 0,65 in 2015-OS-K7b.
- 4.8 periodische Dezimalzahl erkennen und schreiben (Drittel, Sechstel) → kein P10-Typ
- 4.9 Fehler finden (Bruchstrich als Komma gelesen; Nullen bei Hundertsteln vergessen) → kein P10-Typ
- 4.10 Begründen (warum 7/20 = 0,35) → kein P10-Typ

**Einheit 5 · Vergleichen, Ordnen, Runden** – P10-Jahrgänge 8 von 13 (davon Haupt 8); P10-Typen 2; Summe ertrag 8.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Mitte zweier Zahlen bestimmen | 1 | 1 | 1 | 2020 | 2020 | 1 | 0 |  |
| Zahlen in verschiedenen Darstellungen vergleichen | 7 | 7 | 7 | 2014 | 2023 | 7 | 0 |  |

- 5.1 zwei Dezimalzahlen mit gleich vielen Stellen vergleichen → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: Vorstufe des Ordnens: in 2023-OS-B1f sind 0,44 und 0,16 zu vergleichen, nachdem alle Zahlen Dezimalzahlen sind.
- 5.2 verschieden viele Stellen (Nullen anhängen) → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: 2014-OS-B1h (1,4 gegen 1,414; −0,5 gegen −0,512) und 2018-OS-B1d (0,05 gegen 0,5).
- 5.3 Dezimalzahlen ordnen → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: Definition „… in dieselbe Form bringen und ordnen“; aufsteigende Reihe in 2014-OS-B1h.
- 5.4 runden auf Zehntel und Hundertstel (auch Größen mit Einheit) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozentsatz berechnen“ · „Relative Häufigkeit angeben“ · „Pythagoras Kathete“. Grund: Runden auf Zehntel oder Hundertstel verlangen die Ergebnisse von 2023-OS-K6a (≈ 16,0 %), 2015-OS-K7b (≈ 0,65) und als Größe mit Einheit 2026-FOR-K4a (h ≈ 29,2 cm).
- 5.5 Mitte zweier Zahlen (Mittelwert oder Zahlenstrahl eine Stelle feiner) → „Mitte zweier Zahlen bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Median bestimmen“. Grund: Definition „Zahl genau in der Mitte zweier Dezimalzahlen … als Mittelwert“ (2020-OS-B1f); dieselbe Mitte beim Median gerader Anzahl in 2024-OS-B1h (Mitte zwischen 18 und 20).
- 5.6 Zahl zwischen zwei Zahlen angeben (auch zwischen zwei Brüchen über Dezimalzahlen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahl zu Bedingung angeben“. Grund: Definition „zwischen 1/2 und 4/5“; 2014-OS-B1c über die Dezimalzahlen 0,5 und 0,8.
- 5.7 Bruch gegen Dezimalzahl (Vergleichszeichen) → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: 2015-OS-B1c: 1,5 < 3/2 und 8/5 > 3/2 prüfen.
- 5.8 Prozent gegen Dezimalzahl → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: 2018-OS-B1d: Vergleichszeichen zwischen 5 % und 0,5.
- 5.9 gemischte Liste ordnen (Bruch, Dezimalzahl, Prozent, Potenz einer Dezimalzahl) → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: 2023-OS-B1f (4,4; 0,44; 0,4²; 44 %) und 2014-OS-B1h (−1/2; 1,4; −0,512; √2).
- 5.10 Aussagen prüfen und die wahre ankreuzen → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: 2015-OS-B1c verlangt genau diese Leistung: die wahre von drei Ungleichungen ankreuzen.
- 5.11 mit negativen Zahlen (Vorrat, rationale-zahlen.md Einheit 1) → „Zahlen in verschiedenen Darstellungen vergleichen“ · „Mitte zweier Zahlen bestimmen“ – P10-Jahrgänge 8 (Haupt 8). Grund: Negative Zahlen in 2014-OS-B1h (−1/2 gegen −0,512), 2017-OS-B1e (−10³ als kleinste) und 2020-OS-B1f (Mitte von −0,6 und −0,5).
- 5.12 mit Wurzeln über Näherungswert (Vorrat, potenzen-wurzeln.md) → „Zahlen in verschiedenen Darstellungen vergleichen“ – P10-Jahrgänge 7 (Haupt 7). Grund: 2015-OS-B1c und 2014-OS-B1h vergleichen √2 über den Näherungswert 1,41 (Voraussetzung „Wurzel abschätzen“).
- 5.13 Fehler finden (Länge statt Stellenwert verglichen; Potenz als Verdopplung) → kein P10-Typ
- 5.14 Begründen (warum 0,5 > 0,45) → kein P10-Typ

### bruchrechnung

themen.csv: kein msa-Thema – Vermerk: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“.

**Einheit 1 · Brüche addieren und subtrahieren** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 1.1 gleichnamig addieren und subtrahieren → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit mehrstufig unabhängig“ · „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ · „Baumdiagramm ergänzen“. Grund: Summenregel mit gleichnamigen Brüchen: 2014-OS-K6c (16/64 + 9/64 + 1/64), 2017-OS-K6b (1/6 + 1/6, Nebentyp) und 2020-OS-K6c (15/216 + 1/216).
- 1.2 Ergebnis kürzen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit mehrstufig unabhängig“ · „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ · „Baumdiagramm ergänzen“ · „Wahrscheinlichkeit über Gegenereignis berechnen“. Grund: Summe oder Differenz wird gekürzt: 26/64 = 13/32 (2014-OS-K6c), 2/6 = 1/3 (2017-OS-K6b), 16/216 = 2/27 (2020-OS-K6c) und 33/36 = 11/12 (2026-FOR-K6c).
- 1.3 über ein Ganzes hinaus (unechter Bruch, gemischte Zahl) → kein P10-Typ
- 1.4 gleichnamig machen mit einem Nenner als Vielfachem des anderen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit mehrstufig unabhängig“. Grund: 2014-OS-K6c (1/4 = 16/64 neben 9/64 und 1/64) und 2025-OS-K3c (1/4 + 1/16 = 5/16).
- 1.5 beide erweitern (Hauptnenner) → kein P10-Typ
- 1.6 ganze Zahl plus Bruch → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit über Gegenereignis berechnen“ · „Baumdiagramm ergänzen“ · „Wahrscheinlichkeit einstufig“. Grund: Eins minus Bruch: Definition „über 1 − P(Gegenereignis)“ (2026-FOR-K6c, 1 − 3/36), Knotensumme 1 im Baum (2015-OS-K7d, 1 − 1/11 = 10/11) und 2014-OS-B1d (1 − 2/6 als Rechenweg).
- 1.7 gemischte Zahlen addieren und subtrahieren → kein P10-Typ
- 1.8 Sachaufgabe (Zeit, Liter, Pizza) → kein P10-Typ
- 1.9 Fehler finden (Zähler und Nenner addiert) → kein P10-Typ
- 1.10 Begründen (warum erst gleichnamig) → kein P10-Typ

**Einheit 2 · Dezimalzahlen addieren und subtrahieren** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 2.1 gleich viele Stellen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Spannweite berechnen“ · „Guthabentabelle mit Zinsen ergänzen“. Grund: Dezimalzahlen mit gleich vielen Stellen: 1,85 − 1,77 in 2026-FOR-K3a, 9,9 − 9,5 in 2019-OS-B1i und 612,08 + 12,24 in 2014-OS-K3b.
- 2.2 verschieden viele Stellen (Nullen anhängen) → kein P10-Typ
- 2.3 mit Übertrag → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Spannweite berechnen“ · „Guthabentabelle mit Zinsen ergänzen“ · „Wert nach prozentualer Erhöhung berechnen“. Grund: Übertrag: 85,1 − 19,2 in 2024-OS-K2a, 612,08 + 12,24 (Hundertstel) in 2014-OS-K3b und 3,50 € + 0,70 € in 2024-OS-B1e.
- 2.4 ganze Zahl plus Dezimalzahl → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Guthabentabelle mit Zinsen ergänzen“ · „Wert nach prozentualer Erhöhung berechnen“. Grund: 612,08 + 12,24 + 200 = 824,32 in 2014-OS-K3b und 36 € + 7,50 € in 2015-OS-K2b.
- 2.5 Größen mit Komma (2,50 € + 0,75 €; 1,2 m − 0,45 m) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Spannweite berechnen“ · „Guthabentabelle mit Zinsen ergänzen“ · „Wert nach prozentualer Erhöhung berechnen“. Grund: Größen mit Komma: 1,85 € − 1,77 € (2026-FOR-K3a), 9,9 m − 9,5 m (2019-OS-B1i), die Euro-Beträge der Guthabentabelle (2014-OS-K3b) und 3,50 € + 0,70 € (2024-OS-B1e).
- 2.6 Überschlag vorab → kein P10-Typ
- 2.7 Fehler finden (Komma nicht untereinander) → kein P10-Typ
- 2.8 Begründen → kein P10-Typ

**Einheit 3 · Brüche multiplizieren und dividieren** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 3.1 Bruch mal natürliche Zahl (vervielfachen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit mehrstufig unabhängig“ · „Baumdiagramm ergänzen“. Grund: 2020-OS-K6c: drei gleich wahrscheinliche Pfade, 3 · 5/216 = 15/216.
- 3.2 Bruch geteilt durch natürliche Zahl (teilen) → kein P10-Typ
- 3.3 Bruch von Bruch (Zähler mal Zähler, Nenner mal Nenner; Bruchteil einer Zahl oder Größe → brueche-dezimalzahlen.md Einheit 1) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit mehrstufig unabhängig“ · „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ · „Baumdiagramm ergänzen“ · „Wahrscheinlichkeit über Gegenereignis berechnen“ · „Zufallsgerät zu Wahrscheinlichkeit entwerfen“. Grund: Pfadregel als Bruch mal Bruch: 2025-OS-K3b (1/4 · 2/4), 2019-OS-K6c (6/20 · 5/19 · 4/18), 2026-FOR-K6b (3/6 · 5/6), 2026-FOR-K6c (3/6 · 1/6) und 2025-OS-K3d (2/4 · 2/4 = 1/4).
- 3.4 vor dem Rechnen kürzen → kein P10-Typ
- 3.5 gemischte Zahl mal Bruch (erst in unechten Bruch) → kein P10-Typ
- 3.6 Zahl geteilt durch Bruch, Bruch geteilt durch Bruch (Kehrbruch) → kein P10-Typ
- 3.7 Sachaufgabe (Rezept, Flaschen füllen) → kein P10-Typ
- 3.8 Fehler finden (Kehrbruch beim Multiplizieren; beim Teilen den Zähler geteilt) → kein P10-Typ
- 3.9 Begründen (warum durch ein Halb mal zwei) → kein P10-Typ

**Einheit 4 · Dezimalzahlen multiplizieren und dividieren** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 4.1 Komma verschieben (mal 10, 100, 1000; geteilt durch 10, 100) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zehnerpotenzschreibweise umwandeln“ · „Große Zahl mit Zehnerpotenz multiplizieren“ · „Kosten aus Menge und Preis berechnen“. Grund: Komma verschieben mit Zehnerpotenzen: 8,5 · 10⁵ = 850 000 (2016-OS-B1h), 2,1 · 10⁻⁴ = 0,00021 (2019-OS-B1j), mal 100 durch Nullen anhängen (2015-OS-K3a) und 145,5 ct = 1,455 € (2014-OS-K4c).
- 4.2 Dezimalzahl mal natürliche Zahl → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Kosten aus Menge und Preis berechnen“ · „Prozentwert berechnen“. Grund: 16 · 0,14 ct (2024-OS-K2d), 9 000 · 1,455 € (2014-OS-K4c), 400 · 0,02 (2015-OS-B1e) und 550 · 0,2 (2021-OS-B1c).
- 4.3 Dezimalzahl mal Dezimalzahl (Kommastellen zählen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“ · „Guthabentabelle mit Zinsen ergänzen“ · „Wert nach prozentualer Erhöhung berechnen“. Grund: Kommastellen zählen: 0,4² = 0,16 (2023-OS-B1f, Fehlerquelle 0,8), 824,32 · 0,02 (2014-OS-K3b) und 43,50 · 0,8 (2015-OS-K2b).
- 4.4 Dezimalzahl geteilt durch natürliche Zahl → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Bruchteil einer Größe berechnen“ · „Mitte zweier Zahlen bestimmen“ · „Arithmetisches Mittel berechnen“. Grund: 1,2 : 4 (2018-OS-B1a), −1,1 : 2 (2020-OS-B1f) und 78,3 : 9 (2021-OS-K5a, Nebentyp).
- 4.5 geteilt durch Dezimalzahl (beide Kommas verschieben) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Rechteckseite aus Fläche berechnen“. Grund: 2014-OS-K5d: Plattenlänge 1,8 : 1,2 = 1,5 m.
- 4.6 Ergebnis mit Nullen (0,3 · 0,2) → kein P10-Typ
- 4.7 Größen (Preis mal Anzahl, Cent und Euro) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Kosten aus Menge und Preis berechnen“. Grund: Definition „Gesamtpreis aus einer berechneten Menge und einem Einheitspreis“; 2024-OS-K2d (Cent bleibt Cent) und 2014-OS-K4c (Cent in Euro).
- 4.8 Fehler finden (Kommastellen nicht gezählt) → kein P10-Typ
- 4.9 Begründen (warum das Komma wandert) → kein P10-Typ

**Einheit 5 · Rechengesetze und Punkt vor Strich** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 5.1 Punkt vor Strich mit Brüchen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wahrscheinlichkeit mehrstufig unabhängig“ · „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ · „Baumdiagramm ergänzen“. Grund: Pfad- und Summenregel als Punkt vor Strich: (1/2)² + (3/8)² + (1/8)² (2014-OS-K6c), 1/6 + 5/6 · 1/5 (2017-OS-K6b) und 1/11 + 10/11 · 1/10 + 10/11 · 9/10 · 1/9 (2015-OS-K7d).
- 5.2 mit Dezimalzahlen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wert nach prozentualer Erhöhung berechnen“ · „Term zu Sachtext angeben“ · „Termwert berechnen“. Grund: 3 · 12 + 7,50 (2015-OS-K2b), 2 · 12 € + 2 · 7,50 € (2015-OS-K2a) und (−5)² − 2 · 2,5 − (−2) (2022-GYM-B2a).
- 5.3 Klammern → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Termwert berechnen“ · „Term zu Sachtext angeben“. Grund: Klammer zuerst: (8 + (−1)) : (−2) (2021-OS-B1g), 5 · (−2 − 3) (2026-FOR-B1g) und 1/5 · (36 € + 7,50 €) (2015-OS-K2a).
- 5.4 Kommutativ- und Assoziativgesetz für Vorteile (0,25 · 7 · 4) → kein P10-Typ
- 5.5 Distributivgesetz (Ausklammern bei Dezimalzahlen) → kein P10-Typ
- 5.6 Überschlag und Prüfen → kein P10-Typ
- 5.7 Fehler finden (von links nach rechts gerechnet) → kein P10-Typ
- 5.8 Begründen (welche Rechnung zuerst) → kein P10-Typ

### rationale-zahlen

themen.csv: „Rationale Zahlen rechnen“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Aussage über Bruchteile einer Größe prüfen“.

**Einheit 1 · Negative Zahlen kennen und ordnen** – P10-Jahrgänge 2 von 13 (davon Haupt 2); P10-Typen 1; Summe ertrag 2.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Zahl zu Bedingung angeben | 2 | 2 | 2 | 2014 | 2015 | 2 | 0 |  |

- 1.1 Situation ↔ Zahl (3 °C unter null, 20 € Schulden) → kein P10-Typ
- 1.2 Zahlen an der Zahlengeraden eintragen und ablesen (ganze, Dezimalzahlen, Brüche) → „Zahl zu Bedingung angeben“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Mitte zweier Zahlen bestimmen“ · „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: Zahlengerade mit negativen Zahlen: Definition „am Zahlenstrahl“ (2020-OS-B1f), „jede Zahl rechts von −150“ (2015-OS-B1b) und „am weitesten links auf dem Zahlenstrahl“ (2017-OS-B1e).
- 1.3 Gegenzahl und Betrag angeben → kein P10-Typ
- 1.4 zwei Zahlen vergleichen (< >) → „Zahl zu Bedingung angeben“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2015-OS-B1b (größer als −150, Fehlerquelle −200) und 2014-OS-B1h (−1/2 = −0,5 > −0,512).
- 1.5 Zahlen ordnen (gemischt: Bruch, Dezimalzahl, negativ) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: Definition „… in dieselbe Form bringen und ordnen“; 2014-OS-B1h (−1/2; 1,4; −0,512; √2) und 2017-OS-B1e (−0,01; −10³; −10²; −0,1).
- 1.6 Zahl zu Bedingung angeben („größer als −150“, „zwischen zwei Zahlen“) → „Zahl zu Bedingung angeben“ – P10-Jahrgänge 2 (Haupt 2). (wortgleich)
- 1.7 Mitte zweier Zahlen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Mitte zweier Zahlen bestimmen“. Grund: 2020-OS-B1f: Mitte von −0,6 und −0,5 (Fehlerquelle −0,65 in die falsche Richtung); Typ bei brueche-dezimalzahlen.md.
- 1.8 runden → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Nullstellen quadratische Funktion berechnen“. Grund: 2017-OS-K5d rundet die negativen Nullstellen −3 ± √2 auf −1,59 und −4,41 (Nebentyp).
- 1.9 Punkte in vier Quadranten (Verfahren und Kette in symmetrie-abbildungen.md Einheit 1; hier nur als Anwendung der negativen Zahlen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Gerade durch zwei Punkte zeichnen“ · „Streckenlänge aus Koordinaten berechnen“. Grund: Punkte mit negativen Koordinaten eintragen und ablesen: K(−4|−1) in 2017-OS-K5a, B(3|−1,5) in 2025-OS-K5a, A(0|−2) und B(2|−2) aus dem Bild in 2019-OS-K2d.
- 1.10 Fehler finden (Betrag statt Wert verglichen) → kein P10-Typ
- 1.11 Begründen (warum −5 < −3) → kein P10-Typ

**Einheit 2 · Addieren und Subtrahieren** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 1; Summe ertrag 4.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Termwert berechnen | 4 | 3 | 3 | 2016 | 2026 | 4 | 0 | nicht in der Zuordnungszeile der Einheit |

- 2.1 positive Zahl dazu oder weg von negativer Zahl (Zahlengerade) → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2026-FOR-B1g: −2 − 3 = −5 in der Klammer (Fehlerquelle −1).
- 2.2 negative Zahl addieren (Klammer) → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Mitte zweier Zahlen bestimmen“. Grund: 8 + (−1) in 2021-OS-B1g, 2 + (−4) in 2016-OS-B1i und −0,6 + (−0,5) in 2020-OS-B1f.
- 2.3 negative Zahl subtrahieren (zwei Minus) → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Geradengleichung aus zwei Punkten“. Grund: 4 − (−3) in 2019-GYM-B1d, − (−2) in 2022-GYM-B2a und die Koordinatendifferenzen 3 − (−2) in 2025-OS-K5a und 2 − (−4) in 2017-OS-K5a (Nebentyp).
- 2.4 Zeichen zusammenfassen und rechnen → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Erster Schritt der Termwert-Originale: 8 + (−1) = 8 − 1 (2021-OS-B1g) und 2 + (−4) = 2 − 4 (2016-OS-B1i).
- 2.5 Beträge: gleiche Vorzeichen addieren, verschiedene subtrahieren → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Mitte zweier Zahlen bestimmen“. Grund: 2 + (−4) = −2 (2016-OS-B1i), −2 − 3 = −5 (2026-FOR-B1g) und −0,6 + (−0,5) = −1,1 (2020-OS-B1f).
- 2.6 Unterschied zweier Zahlen (Abstand) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Geradengleichung aus zwei Punkten“. Grund: Die Steigung aus zwei Punkten verlangt den Unterschied der Koordinaten über null hinweg: 3 − (−2) = 5 und −1,5 − 6 = −7,5 in 2025-OS-K5a, 2 − (−4) = 6 in 2017-OS-K5a.
- 2.7 mehrere Summanden → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2022-GYM-B2a: 25 − 5 + 2 nach dem Einsetzen von a = −2.
- 2.8 Dezimalzahlen und Brüche → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Mitte zweier Zahlen bestimmen“. Grund: Dezimalzahlen mit Vorzeichen: −0,6 + (−0,5) in 2020-OS-B1f und −2 + 4,5 in 2022-GYM-B2a.
- 2.9 Fehler finden (−2 − 3 = −1) → kein P10-Typ
- 2.10 Begründen (warum minus minus plus ist) → kein P10-Typ
- 2.11 Umkehrung: Rechnung zu Ergebnis finden → kein P10-Typ

**Einheit 3 · Multiplizieren und Dividieren** – P10-Jahrgänge 4 von 13 (davon Haupt 4); P10-Typen 2; Summe ertrag 5.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Vorzeichenregel anwenden | 1 | 1 | 1 | 2015 | 2015 | 1 | 0 |  |
| Termwert berechnen | 4 | 3 | 3 | 2016 | 2026 | 4 | 0 |  |

- 3.1 plus mal minus, minus mal minus → „Vorzeichenregel anwenden“ · „Termwert berechnen“ – P10-Jahrgänge 4 (Haupt 4). Außerhalb der Themen des Eintrags (zählt nicht): „Punktprobe durchführen“. Grund: Definition „Vorzeichen des Ergebnisses beim Multiplizieren“ (2015-OS-B1g); 5 · (−5) in 2026-FOR-B1g und −2 · (−4) in 2026-FOR-K5b.
- 3.2 dividieren mit Vorzeichen → „Termwert berechnen“ · „Vorzeichenregel anwenden“ – P10-Jahrgänge 4 (Haupt 4). Grund: 7 : (−2) = −3,5 (2021-OS-B1g) und (−2) : (−2) = 1 (2016-OS-B1i); die Definition der Vorzeichenregel nennt das Dividieren.
- 3.3 mehrere Faktoren (Anzahl der Minuszeichen) → „Vorzeichenregel anwenden“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Vorzeichen des Ergebnisses beim Multiplizieren … positiver und negativer Zahlen“ ohne Beschränkung auf zwei Faktoren; kein Original mit drei Faktoren.
- 3.4 Potenzen: (−2)² gegen −2² → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Punktprobe durchführen“ · „Wurzel eines Quadrats berechnen“. Grund: p(−3) = −(−3)² = −9 in 2014-OS-K7a (Fehlerquelle +9), (−5)² = 25 in 2022-GYM-B2a und (−4)² = 16 in 2015-OS-B1j.
- 3.5 Punkt vor Strich mit negativen Zahlen → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Punktprobe durchführen“ · „Funktionswert berechnen“. Grund: (−5)² − 2 · 2,5 − (−2) (2022-GYM-B2a), −2 · (−4) + 2 (2026-FOR-K5b) und ½ · (−10) + 1 (2017-OS-K5b).
- 3.6 Termwert mit Klammer (5 · (x − 3) für x = −2) → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Definition „Wert eines Terms für einen gegebenen Variablenwert … auch mit negativen Zahlen“; 2026-FOR-B1g ist genau 5 · (x − 3) für x = −2.
- 3.7 Vorzeichenregel als Aussage prüfen → „Vorzeichenregel anwenden“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „oder eine Regel dazu auswählen“; 2015-OS-B1g lässt die wahre Aussage zu plus mal minus ankreuzen.
- 3.8 Fehler finden (Vorzeichen des Produkts vergessen) → kein P10-Typ
- 3.9 Begründen (Permanenzreihe oder Spiegelung) → kein P10-Typ

**Einheit 4 · Terme und Sachaufgaben** – P10-Jahrgänge 4 von 13 (davon Haupt 4); P10-Typen 3; Summe ertrag 7.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Ausgangswert aus Differenz berechnen | 1 | 1 | 1 | 2017 | 2017 | 0 | 1 |  |
| Günstigste Preiskombination bestimmen | 2 | 1 | 1 | 2016 | 2016 | 0 | 1 |  |
| Termwert berechnen | 4 | 3 | 3 | 2016 | 2026 | 4 | 0 | nicht in der Zuordnungszeile der Einheit |

- 4.1 Rechenvorteile (Tauschen, geschickt zusammenfassen) → kein P10-Typ
- 4.2 Plus- und Minusklammer auflösen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Term mit Klammern und Potenzen vereinfachen“. Grund: 2022-GYM-B2b: −2 · (a + 4,5) = −2a − 9 beim Vereinfachen.
- 4.3 Termwert für gegebene Werte, auch Bruchterm (a + b) : c → „Termwert berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Bruchterme (a + b)/c in 2021-OS-B1g und 2016-OS-B1i, (a − b) : (2a + b) in 2019-GYM-B1d.
- 4.4 Kontostand nach mehreren Buchungen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Endwert linearer Veränderung berechnen“. Grund: Kontostand aus Anfangsguthaben und gleichen Buchungen: 1 472 € + 12 · 22 € in 2022-OS-K6a (Definition nennt Sparen).
- 4.5 Temperatur- und Höhenunterschied → kein P10-Typ
- 4.6 Ausgangswert aus Differenz („8 512 mehr als“) → „Ausgangswert aus Differenz berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „x mehr/weniger als“ mit Umkehroperation; 2017-OS-K2a (682 069 − 8 512).
- 4.7 günstigste Preiskombination (Vorrat, Niveau III) → „Günstigste Preiskombination bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2016-OS-K2d: Eintrittspreise mit Familienkarte, Großeltern-Enkel-Ticket und Altersgrenzen, Niveau III.
- 4.8 Fehler finden (Minusklammer nur beim ersten Glied) → kein P10-Typ
- 4.9 Begründen (Rechenweg erklären) → kein P10-Typ

### prozentrechnung

themen.csv: „Prozentrechnung“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Gesamtmenge aus Pro-Kopf-Angabe berechnen“.

**Einheit 1 · Prozente als Anteile** – P10-Jahrgänge 8 von 13 (davon Haupt 6); P10-Typen 4; Summe ertrag 10.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Prozent und Anteil umwandeln | 2 | 2 | 5 | 2014 | 2022 | 2 | 0 |  |
| Fehlenden Prozentanteil ergänzen | 2 | 1 | 1 | 2021 | 2021 | 0 | 1 |  |
| Anteilsaussage prüfen und korrigieren | 6 | 3 | 3 | 2017 | 2023 | 0 | 3 |  |
| Prozentanteil einer Rasterfläche markieren | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Bruch → Prozent (Nenner 100; Nenner, der in 100 aufgeht) → „Prozent und Anteil umwandeln“ – P10-Jahrgänge 5 (Haupt 2). Grund: Definition „Anteil als Prozentsatz angeben“; Nebenleistung in 2014-OS-B1i (9 von 15 Feldern als Prozentsatz) und 2014-OS-K6a (3/8 in Prozent).
- 1.2 Dezimalzahl ↔ Prozent → „Prozent und Anteil umwandeln“ – P10-Jahrgänge 5 (Haupt 2). Grund: Vorstufe desselben Umwandelns: die Dezimalzahl ist die Anteilsform, über die der Anteil in Prozent geschrieben wird (Definition „Anteil als Prozentsatz angeben“).
- 1.3 Anteil am Streifen oder an einer Figur ablesen und einzeichnen → „Prozent und Anteil umwandeln“ · „Prozentanteil einer Rasterfläche markieren“ – P10-Jahrgänge 5 (Haupt 2). Grund: Ablesen an einer Figur: 2014-OS-B1i (graue Felder eines Rechtecks als Prozentsatz, Nebentyp); Einzeichnen: Definition „zum Prozentsatz gehörende Kästchen markieren“ (2014-GYM-B1g).
- 1.4 Anteilsformulierung ↔ Prozent („jeder fünfte“, „ein Viertel“, „4 von 100“) → „Prozent und Anteil umwandeln“ – P10-Jahrgänge 5 (Haupt 2). Grund: Definition nennt „jeder fünfte“, „ein Viertel“ und „4 von 100“; Originale 2022-OS-B1f und 2020-OS-B1a.
- 1.5 Prozentangaben ordnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: Definition „Zahlen in Dezimal-, Prozent-, Bruch- … schreibweise in dieselbe Form bringen und ordnen“; Typ bei brueche-dezimalzahlen.md.
- 1.6 fehlenden Anteil zu 100 % ergänzen → „Fehlenden Prozentanteil ergänzen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „fehlenden Prozentsatz als Rest zu 100 %“; Original 2021-OS-K5b.
- 1.7 Anteilsaussage prüfen und korrigieren (Tabellenwerte) → „Anteilsaussage prüfen und korrigieren“ – P10-Jahrgänge 3 (Haupt 3). (wortgleich)
- 1.8 Fehler finden (Nenner als Prozent gelesen) → kein P10-Typ
- 1.9 Begründen (warum 1/5 = 20 %) → kein P10-Typ

**Einheit 2 · Prozentsatz berechnen** – P10-Jahrgänge 11 von 13 (davon Haupt 8); P10-Typen 2; Summe ertrag 19.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Prozentsatz berechnen | 11 | 5 | 5 | 2014 | 2025 | 1 | 4 |  |
| Prozentuale Veränderung berechnen | 8 | 3 | 6 | 2016 | 2026 | 0 | 4 | nicht in der Zuordnungszeile der Einheit |

- 2.1 Teil von 100 → „Prozentsatz berechnen“ – P10-Jahrgänge 5 (Haupt 5). Grund: Vorstufe des Verfahrens Teil durch Ganzes mit dem Ganzen 100 (Definition „aus Teil und Ganzem den Anteil in Prozent“).
- 2.2 Teil von 50, 25, 20, 10 (erweitern) → „Prozentsatz berechnen“ – P10-Jahrgänge 5 (Haupt 5). Grund: Vorstufe desselben Verfahrens: Anteil auf Hundertstel erweitern (Definition „aus Teil und Ganzem den Anteil in Prozent“).
- 2.3 beliebiges Ganzes: W : G mit Taschenrechner, runden → „Prozentsatz berechnen“ – P10-Jahrgänge 5 (Haupt 5). Grund: Prüfungsform: 2023-OS-K6a (Anteil an 7,8 Mrd., gerundet) und 2015-OS-K7c (12 : 83 ≈ 14,5 %).
- 2.4 Anteil aus Sachtext (Ganzes zuerst finden) → „Prozentsatz berechnen“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2018-OS-K7a: das Ganze aus 14 und 2 Pfannkuchen erst bilden; ebenso 2015-OS-K7c (verwandelt und nicht verwandelt).
- 2.5 Rabatt in Prozent aus altem und neuem Preis (erst Rabatt in Euro) → „Prozentsatz berechnen“ · „Prozentuale Veränderung berechnen“ – P10-Jahrgänge 11 (Haupt 8). Grund: Rabatt in Euro durch alten Preis ist der Prozentsatz (Definition); aus altem und neuem Preis ist es die Abnahme in Prozent des Ausgangswerts (Definition „Prozentuale Veränderung berechnen“, 2022-OS-K4b).
- 2.6 Fehler finden (G und W vertauscht; Teil zu Rest statt Teil zu Ganzem) → kein P10-Typ
- 2.7 Begründen (warum durch das Ganze teilen) → kein P10-Typ
- 2.8 Umkehrung: zu einem Prozentsatz ein Zahlenpaar angeben → kein P10-Typ

**Einheit 3 · Prozentwert berechnen** – P10-Jahrgänge 6 von 13 (davon Haupt 6); P10-Typen 1; Summe ertrag 9.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Prozentwert berechnen | 9 | 6 | 6 | 2014 | 2026 | 6 | 2 |  |

- 3.1 50 %, 25 %, 10 % vom Ganzen → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: Vorstufe mit bequemen Sätzen; die Originale rechnen 20 % (2017-OS-B1b, 2021-OS-B1c) und 30 % (2026-FOR-B1a) vom Grundwert.
- 3.2 1 %-Weg (G : 100, mal p) → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: Rechenweg des Prozentwerts (Definition „aus Grundwert und Prozentsatz den Prozentwert“), etwa 13 % von 50 € (2014-OS-B1a).
- 3.3 10 %-Schritte (30 %, 15 %, 5 %) → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: Rechenweg für 30 % von 70 € (2026-FOR-B1a) und 20 % von 550 € (2021-OS-B1c).
- 3.4 Dezimalzahl mal Grundwert (0,3 · G) → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: Lösungswege der Originale „0,3 · 70“ (2026-FOR-B1a) und „550 · 0,2“ (2021-OS-B1c).
- 3.5 Grundwert mit Komma (3,50 €) → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: 20 % von 7,50 € in 2015-OS-K2a (Nebentyp) und 20 % von 3,50 € als Schritt in 2024-OS-B1e.
- 3.6 Ersparnis und neuer Preis unterscheiden → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: 2021-OS-B1c (Ersparnis, Restpreis 440 € als Distraktor) und 2017-OS-B1b (Rabatt in Euro, Fehlerquelle Restpreis).
- 3.7 Prozentsatz über 100 % → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: Definition „aus Grundwert und Prozentsatz den Prozentwert“ ohne Grenze für p; kein Original mit p über 100 %.
- 3.8 Mehrwertsteuer in Euro → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: Prozentwert (19 % vom Nettopreis) im Kontext Mehrwertsteuer (Definition); kein Original mit diesem Kontext.
- 3.9 Fehler finden (30 % als 0,03; Restpreis statt Ersparnis) → kein P10-Typ
- 3.10 Begründen (warum erst 1 %) → kein P10-Typ

**Einheit 4 · Grundwert berechnen** – P10-Jahrgänge 9 von 13 (davon Haupt 9); P10-Typen 3; Summe ertrag 22.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Grundwert berechnen | 2 | 2 | 2 | 2023 | 2025 | 2 | 0 |  |
| Prozentwert berechnen | 9 | 6 | 6 | 2014 | 2026 | 6 | 2 | nicht in der Zuordnungszeile der Einheit |
| Prozentsatz berechnen | 11 | 5 | 5 | 2014 | 2025 | 1 | 4 | nicht in der Zuordnungszeile der Einheit |

- 4.1 glatte Sätze (50 %, 25 %, 20 %, 10 %: mal 2, 4, 5, 10) → „Grundwert berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2023-OS-B1b (25 % sind 200 €, mal 4) und 2025-OS-B1a (20 % sind 6 €, mal 5).
- 4.2 1 %-Weg (W : p, mal 100) → „Grundwert berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Lösungsweg von 2025-OS-B1a: „1 % = 0,30 €, 100 % = 30 €“.
- 4.3 beliebiger Satz mit Taschenrechner → „Grundwert berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „aus Prozentwert und Prozentsatz den Grundwert“ ohne Einschränkung des Satzes.
- 4.4 Sachtext („das sind 60 % der Klasse“) → „Grundwert berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Beide Originale sind Sachtexte der Form „… das sind p %“: 2023-OS-B1b (Gewinn), 2025-OS-B1a (Rabatt).
- 4.5 gemischte Aufgaben: erst zuordnen (Prozentwert, Prozentsatz oder Grundwert gesucht), dann rechnen → „Grundwert berechnen“ · „Prozentwert berechnen“ · „Prozentsatz berechnen“ – P10-Jahrgänge 9 (Haupt 9). Grund: Die P10 stellt die drei Grundaufgaben einzeln, das Zuordnen ist ihre Hürde (Fehlerquelle „p % von W statt Grundwert“ in 2023-OS-B1b und 2025-OS-B1a).
- 4.6 Fehler finden (p % von W gerechnet) → kein P10-Typ
- 4.7 Begründen (warum mal 100) → kein P10-Typ

**Einheit 5 · Prozentuale Veränderung** – P10-Jahrgänge 12 von 13 (davon Haupt 11); P10-Typen 6; Summe ertrag 25.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Wert nach prozentualer Erhöhung berechnen | 3 | 2 | 3 | 2015 | 2024 | 1 | 1 |  |
| Prozentuale Veränderung berechnen | 8 | 3 | 6 | 2016 | 2026 | 0 | 4 |  |
| Steigung in Prozent deuten | 3 | 1 | 1 | 2025 | 2025 | 0 | 1 |  |
| Steigung in Prozent berechnen | 0 | 0 | 1 | 2025 | 2025 | 0 | 0 |  |
| Grundwert berechnen | 2 | 2 | 2 | 2023 | 2025 | 2 | 0 | nicht in der Zuordnungszeile der Einheit |
| Prozentwert berechnen | 9 | 6 | 6 | 2014 | 2026 | 6 | 2 | nicht in der Zuordnungszeile der Einheit |

- 5.1 „um“ und „auf“ unterscheiden → „Wert nach prozentualer Erhöhung berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Vorstufe des Verfahrens: „um 20 % erhöht“ (2024-OS-B1e) und „20 % Rabatt“ (2015-OS-K2b) richtig lesen.
- 5.2 neuer Wert über Prozentwert (dazu, weg) → „Wert nach prozentualer Erhöhung berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: 2024-OS-B1e (3,50 € plus 0,70 €) und 2015-OS-K2b (Rabattbetrag abziehen).
- 5.3 neuer Wert über Faktor (1,2; 0,8) → „Wert nach prozentualer Erhöhung berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Definition nennt den Wachstumsfaktor; 2015-OS-K2b über den Faktor 0,8.
- 5.4 Veränderung in Prozent aus zwei Werten (Differenz : Ausgangswert) → „Prozentuale Veränderung berechnen“ – P10-Jahrgänge 6 (Haupt 3). Grund: Definition „Zu- oder Abnahme zwischen zwei Werten in Prozent des Ausgangswerts“; 2016-OS-K2c, 2022-OS-K4b, 2026-FOR-K3c.
- 5.5 alter Wert aus neuem Wert und Prozentsatz → „Grundwert berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Der neue Wert ist der Prozentwert zum Satz 80 % bzw. 120 % (Definition „aus Prozentwert und Prozentsatz den Grundwert“); kein Original mit verändertem Grundwert.
- 5.6 Brutto/Netto (19 %, 7 %) → „Wert nach prozentualer Erhöhung berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Brutto aus Netto ist die Erhöhung um 19 % (Definition, Wachstumsfaktor); kein Original im Kontext Mehrwertsteuer.
- 5.7 Prozentpunkte gegen Prozent → „Prozentwert berechnen“ – P10-Jahrgänge 6 (Haupt 6). Grund: 2019-OS-K5a: Zunahme von 72 % auf 95 % als 23 % von 1 200, Fehlerquelle „Prozentpunkte als Anzahl“ (Typ bei Einheit 3).
- 5.8 Steigung in Prozent deuten und berechnen → „Steigung in Prozent deuten“ · „Steigung in Prozent berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Beide Steigungs-Typen; einziges Original 2025-OS-K4b (deuten als Haupt-, berechnen als Nebentyp).
- 5.9 Fehler finden (Differenz auf den neuen Wert bezogen) → kein P10-Typ
- 5.10 Begründen (welcher Wert ist 100 %) → kein P10-Typ

### zinsrechnung

themen.csv: „Zinsrechnung“.

**Einheit 1 · Jahreszins, Monats- und Tageszins** – P10-Jahrgänge 1 von 13 (davon Haupt 1); P10-Typen 1; Summe ertrag 2.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Guthabentabelle mit Zinsen ergänzen | 2 | 1 | 1 | 2014 | 2014 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 1.1 Kapital, Zinssatz und Zinsen im Text finden und den Prozentbegriffen zuordnen (Kapital = Grundwert, Zinssatz = Prozentsatz, Zinsen = Prozentwert) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozentwert berechnen“ · „Prozentsatz berechnen“. Grund: Vorstufe der Zins-Originale: vor der Rechnung ist das Kapital als Grundwert und der Zinssatz als Prozentsatz zu erkennen (2015-OS-B1e, Fehlerquelle 408 €; 2014-OS-B1e).
- 1.2 Jahreszinsen aus Kapital und Zinssatz: Prozentsatz als Dezimalzahl mal Kapital (400 € zu 2 %: 400 · 0,02 = 8 €; P10-Form) oder 1 %-Weg (ein Prozent von 400 € sind 4 €, zwei Prozent 8 €) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozentwert berechnen“. Grund: Definition „auch Jahreszinsen aus Kapital und Zinssatz“; 2015-OS-B1e (400 € · 0,02 = 8 €).
- 1.3 Guthaben nach einem Jahr: Kapital plus Zinsen (408 € – nicht mit den Zinsen verwechseln) → „Guthabentabelle mit Zinsen ergänzen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Wert nach prozentualer Erhöhung berechnen“. Grund: Kapital plus Zinsen ist der erhöhte Wert (Definition „neuen Wert nach Erhöhung um einen Prozentsatz“) und der Rechenschritt „altes Guthaben + Zinsen“ der Tabelle in 2014-OS-K3b.
- 1.4 Zinssatz aus Zinsen und Kapital: Zinsen geteilt durch Kapital, als Prozent schreiben (230 € von 10 000 €: 230 : 10 000 = 0,023 = 2,3 %; P10-Form) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozentsatz berechnen“. Grund: Definition „auch Zinssatz aus Kapital und Jahreszinsen“; 2014-OS-B1e (230 : 10 000 = 2,3 %).
- 1.5 Kapital aus Zinsen und Zinssatz (1 %-Weg rückwärts: 45 € sind 3 % → 1 % = 15 € → 1500 €) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Grundwert berechnen“. Grund: Das Kapital ist der Grundwert (Definition „aus Prozentwert und Prozentsatz den Grundwert“); kein Original im Kontext Zinsen.
- 1.6 Nachweis „stimmt der Zinssatz?“ in einer Tabelle (4,00 € Zinsen bei 200 € Guthaben sind 2 %; P10-Form 2014-OS-K3a) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozentwert berechnen“ · „Prozentsatz berechnen“. Grund: 2014-OS-K3a: Haupttyp Prozentwert (200 · 0,02 = 4,00 €), alternativ 4 : 200 = 2 %.
- 1.7 Zinsen für mehrere Jahre ohne Zinseszins: Jahreszins mal Jahre (Kredit, Vergleich mit Einheit 2) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozentwert berechnen“ · „Endwert linearer Veränderung berechnen“. Grund: Jahreszins als Prozentwert, jedes Jahr gleich: Definition „Anfangswert plus … n-fache konstante Änderung (Sparen …)“ wie in 2022-OS-K6a; kein Original mit einfacher Verzinsung über Jahre.
- 1.8 Kredit: Zinsen als Kosten, Rückzahlung = Kreditsumme plus Zinsen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozentwert berechnen“ · „Wert nach prozentualer Erhöhung berechnen“. Grund: Kontextvariante: Zinsen als Prozentwert, Rückzahlung als um den Zinssatz erhöhter Betrag; kein Original im Kontext Kredit.
- 1.9 zwei Angebote vergleichen (Zinssatz, Kapital, Laufzeit) → kein P10-Typ
- 1.10 Überschlag: 1 % von … , dann grob mal p → kein P10-Typ
- 1.11 Monatszinsen: Jahreszinsen durch 12 mal Anzahl der Monate (Laufzeit ein halbes Jahr, drei Monate) → kein P10-Typ
- 1.12 Tageszinsen: Jahreszinsen durch 360 mal Anzahl der Tage (Bankjahr 360 Tage, jeder Monat 30 Tage) → kein P10-Typ
- 1.13 Laufzeit aus zwei Daten zählen (Vorrat) → kein P10-Typ
- 1.14 Fehler finden (Guthaben statt Zinsen angegeben; Prozentsatz ohne Komma eingesetzt; Zinssatz mit falschem Komma; Monate nicht durch zwölf) → kein P10-Typ
- 1.15 Begründen (warum 2 % von 10 000 € mehr sind als 5 % von 300 €; warum die Zinsen bei doppeltem Kapital doppelt sind) → kein P10-Typ

**Einheit 2 · Zinseszins und Guthabentabelle** – P10-Jahrgänge 1 von 13 (davon Haupt 1); P10-Typen 2; Summe ertrag 4.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Guthabentabelle mit Zinsen ergänzen | 2 | 1 | 1 | 2014 | 2014 | 0 | 1 |  |
| Zinseszins Endkapital berechnen | 2 | 1 | 1 | 2014 | 2014 | 0 | 1 |  |

- 2.1 Zinsen ans Guthaben anhängen, neues Guthaben nach einem Jahr (200 € → 204 €) → „Guthabentabelle mit Zinsen ergänzen“ · „Zinseszins Endkapital berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Wert nach prozentualer Erhöhung berechnen“. Grund: Erster Schritt der Tabelle in 2014-OS-K3b und des Rechenwegs „Jahr für Jahr“ in 2014-OS-K3c; Definition „neuen Wert nach Erhöhung um einen Prozentsatz“.
- 2.2 Zinsen im zweiten Jahr vom neuen Guthaben (204 · 0,02 = 4,08 €), Guthaben nach zwei Jahren Schritt für Schritt → „Guthabentabelle mit Zinsen ergänzen“ · „Zinseszins Endkapital berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Zinsen vom neuen Guthaben: 824,32 · 0,02 in 2014-OS-K3b (Fehlerquelle vom alten Guthaben); Definition Zinseszins „oder schrittweise“.
- 2.3 Guthabentabelle mit den Spalten Zinsen, Einzahlung und Guthaben um eine Zeile fortschreiben (Zinsen = Zinssatz vom Guthaben der Vorzeile; Guthaben = altes Guthaben + Zinsen + Einzahlung) → „Guthabentabelle mit Zinsen ergänzen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Guthaben = altes Guthaben + Zinsen + Einzahlung, Zinsen = Zinssatz vom Guthaben“; 2014-OS-K3b.
- 2.4 zwei fehlende Felder in einer gegebenen Tabelle ergänzen, Kontrolle über die nächste gegebene Zeile (P10-Form 2014-OS-K3b) → „Guthabentabelle mit Zinsen ergänzen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2014-OS-K3b: zwei Felder ergänzen, Kontrolle an 1040,81 € in der nächsten Zeile.
- 2.5 Wachstumsfaktor: „plus 2 %“ ist „mal 1,02“, q = 1 + p/100 → „Zinseszins Endkapital berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Wert nach prozentualer Erhöhung berechnen“ · „Wachstumstabelle ergänzen“ · „Exponentialfunktion aufstellen“. Grund: q = 1,03 in 2014-OS-K3c, Definition „(Wachstumsfaktor)“ mit 3,50 · 1,2 in 2024-OS-B1e, Voraussetzung „Prozentsatz in Wachstumsfaktor umrechnen“ in 2026-FOR-K7a und 13 % Abnahme als 0,87 in 2017-OS-K7c.
- 2.6 Endkapital nach n Jahren: Startkapital mal q hoch n mit dem Taschenrechner (1 000 € zu 3 % über 5 Jahre: 1000 · 1,03⁵ ≈ 1 159,27 €; P10-Form 2014-OS-K3c) oder Jahr für Jahr → „Zinseszins Endkapital berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „als K · q^n (oder schrittweise)“; 2014-OS-K3c (1000 · 1,03⁵).
- 2.7 einfache Verzinsung und Zinseszins nebeneinander (1 150 € gegen 1 159,27 €) → „Zinseszins Endkapital berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2014-OS-K3c: 1 159,27 € statt der einfachen Verzinsung 1 150 € (Fehlerquelle und Bemerkung des Originals).
- 2.8 Zinsen insgesamt = Endkapital minus Startkapital → kein P10-Typ
- 2.9 Guthaben nach n Jahren mit jährlicher Einzahlung (Tabelle statt Formel) → „Guthabentabelle mit Zinsen ergänzen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „mit jährlichen Zinsen, Einzahlungen und Guthaben … fortschreiben“; 2014-OS-K3b (Einzahlung je 200 €).
- 2.10 Startkapital aus Endkapital: Endkapital geteilt durch q hoch n (Vorrat) → kein P10-Typ
- 2.11 Laufzeit für eine Verdopplung durch Probieren mit der Tabelle oder 72er-Regel (Vorrat) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Verdopplungs- oder Halbwertszeit bestimmen“ · „Zeitpunkt für Schwellenwert bei Wachstum bestimmen“. Grund: Kontextvariante: Verdopplung bei 3 % im Jahr in 2020-OS-K4b, schrittweise mal 1,08 bis zur Schwelle in 2018-OS-K2c.
- 2.12 Ratenkauf und Kredit mit Zinseszins (Vorrat, Verbrauchersicht) → „Zinseszins Endkapital berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Kontextvariante von K · qⁿ: 2017-GYM-K5a (Miete mit jährlich 1,1 % Steigerung, 310 € · 1,011⁵); kein Original zu Ratenkauf.
- 2.13 Fehler finden (Zinsen jedes Jahr vom Startkapital; Einzahlung vergessen; q = 1,3 statt 1,03; mal 0,03 statt mal 1,03) → kein P10-Typ
- 2.14 Begründen (warum das Guthaben mit Zinseszins jedes Jahr um mehr Euro wächst, obwohl der Zinssatz gleich bleibt) → kein P10-Typ

### potenzen-wurzeln

themen.csv: „Potenzen und Wurzeln“, „Zehnerpotenzen und Näherungswerte“ – Vermerk: „Typen sind alle Zehnerpotenzen“.

**Einheit 1 · Potenzen** – P10-Jahrgänge 7 von 13 (davon Haupt 7); P10-Typen 4; Summe ertrag 9.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Exponent einer Potenz bestimmen | 2 | 2 | 2 | 2020 | 2024 | 2 | 0 |  |
| Wurzel eines Quadrats berechnen | 1 | 1 | 1 | 2015 | 2015 | 1 | 0 | nicht in der Zuordnungszeile der Einheit |
| Quadratseite aus Fläche berechnen | 1 | 1 | 1 | 2020 | 2020 | 1 | 0 | nicht in der Zuordnungszeile der Einheit |
| Zehnerpotenzschreibweise umwandeln | 5 | 5 | 5 | 2015 | 2025 | 4 | 1 | nicht in der Zuordnungszeile der Einheit |

- 1.1 Potenz als Malkette schreiben (3⁴ = 3 · 3 · 3 · 3) und Malkette als Potenz (2 · 2 · 2 · 2 · 2 = 2⁵) → „Exponent einer Potenz bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2020-OS-B1h: 16 als Malkette 2 · 2 · 2 · 2, also x = 4.
- 1.2 Basis und Exponent in einer Potenz benennen (Beschriftung) → kein P10-Typ
- 1.3 Potenz von Produkt unterscheiden und beide ausrechnen (4³ = 64, 4 · 3 = 12) → „Exponent einer Potenz bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: Die Fehlerquellen „16 : 2 = 8“ (2020-OS-B1h) und „256 : 4 = 64“ (2024-OS-B1g) verwechseln Potenz und Produkt; 2019-OS-B1d verlangt 4³ = 64 ausgerechnet.
- 1.4 Quadratzahlen bis 20² aus dem Kopf, Kubikzahlen bis 10³ → „Wurzel eines Quadrats berechnen“ · „Quadratseite aus Fläche berechnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: (−4)² = 16 in 2015-OS-B1j, √36 = 6 in 2020-OS-B1d und die Kubikzahl 4³ = 64 in 2019-OS-B1d.
- 1.5 Potenzwert mit dem Taschenrechner (Tasten x² und ^, Klammern bei negativer Basis) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zinseszins Endkapital berechnen“ · „Funktionswert berechnen“ · „Wahrscheinlichkeit mehrstufig unabhängig“. Grund: Voraussetzung „Potenz mit Taschenrechner“: 1,03⁵ in 2014-OS-K3c, 1,03¹⁴ in 2020-OS-K4c, 1,019¹⁴ in 2026-FOR-K7c (Nebentyp) und 0,985⁵ in 2025-GYM-K6a.
- 1.6 Potenz mit negativer Basis: Vorzeichen aus gerader oder ungerader Hochzahl ((−3)⁴ = 81, (−3)³ = −27), Klammer gegen kein Klammer (−3⁴ = −81) → „Wurzel eines Quadrats berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Punktprobe durchführen“ · „Termwert berechnen“ · „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: (−4)² in 2015-OS-B1j, −(−3)² in 2014-OS-K7a (Voraussetzung „Potenz mit negativer Basis“), (−5)² in 2022-GYM-B2a und −10³ ohne Klammer in 2017-OS-B1e.
- 1.7 Potenz einer Dezimalzahl (0,4² = 0,16, 1,5³ = 3,375) und eines Bruchs ((2/3)² = 4/9) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“ · „Wahrscheinlichkeit mehrstufig unabhängig“. Grund: 0,4² = 0,16 in 2023-OS-B1f und die Brüche (1/2)², (3/8)², (1/8)² in 2014-OS-K6c.
- 1.8 zwei Potenzen vergleichen, indem beide ausgerechnet werden (2⁸ gegen 3⁵) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: Definition „… Potenzschreibweise in dieselbe Form bringen und ordnen“; 2019-OS-B1d (4³, 8⁴, 2⁸ ausrechnen).
- 1.9 Potenzen ordnen, größte oder kleinste unterstreichen (P10-Form) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2019-OS-B1d: die größte von drei Potenzen unterstreichen.
- 1.10 Potenz gegen Dezimalzahl und Prozent vergleichen (Vergleichszeichen eintragen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 0,4² gegen 44 % in 2023-OS-B1f und 2⁻⁵ gegen 0,25 in 2022-OS-B1j.
- 1.11 Exponent bestimmen durch wiederholtes Malnehmen (2^x = 16: 2, 4, 8, 16 → x = 4; P10-Form) → „Exponent einer Potenz bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Parameter einer Wurzelfunktion aus einem Punkt bestimmen“. Grund: Definition „durch Probieren“ (2020-OS-B1h, 2024-OS-B1g); 2^n = 8 in 2020-GYM-K3a.
- 1.12 Exponent bestimmen durch Zerlegen (256 = 4 · 4 · 4 · 4) → „Exponent einer Potenz bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „durch Probieren oder Zerlegen“; 2024-OS-B1g (256 als Viererpotenz).
- 1.13 Exponent mit Basis 10 (10^x = 100 000; Brücke zu Einheit 2) → „Exponent einer Potenz bestimmen“ · „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 7 (Haupt 7). Grund: Definition „a^x = b“ mit a = 10; 100 000 = 10⁵ in 2017-OS-B1g.
- 1.14 Potenz mit negativem Exponenten als Bruch und als Dezimalzahl (2⁻³ = 1/8 = 0,125), hoch null → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2022-OS-B1j: 2⁻⁵ = 1/32 = 0,03125 (Fehlerquelle −32).
- 1.15 negative Potenz gegen Dezimalzahl vergleichen (P10-Form) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2022-OS-B1j: Vergleichszeichen zwischen 2⁻⁵ und 0,25.
- 1.16 Fehler finden (Basis mal Exponent; Vorzeichen bei negativer Basis; negative Hochzahl als negative Zahl; „größere Basis, größere Zahl“) → kein P10-Typ
- 1.17 Begründen (warum 2¹⁰ größer ist als 10²; warum 5⁰ = 1 ist – die Kette der Potenzen 5³, 5², 5¹ wird jedes Mal durch fünf geteilt) → kein P10-Typ

**Einheit 2 · Zehnerpotenzen** – P10-Jahrgänge 5 von 13 (davon Haupt 5); P10-Typen 2; Summe ertrag 6.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Zehnerpotenzschreibweise umwandeln | 5 | 5 | 5 | 2015 | 2025 | 4 | 1 |  |
| Große Zahl mit Zehnerpotenz multiplizieren | 1 | 1 | 1 | 2015 | 2015 | 0 | 1 |  |

- 2.1 Zehnerpotenz ausschreiben (10⁶ = 1 000 000) und Zahl als Zehnerpotenz schreiben (100 000 = 10⁵; P10-Form) → „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2017-OS-B1g: 100 000 als 10⁵.
- 2.2 Zahlwörter zuordnen (Tausend, Million, Milliarde, Billion) → kein P10-Typ
- 2.3 große Zahl mit 10, 100, 1000 vervielfachen: Nullen anhängen, Ergebnis ausgeschrieben (P10-Form) → „Große Zahl mit Zehnerpotenz multiplizieren“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „mit 10, 100 oder 1000 vervielfachen (Nullen anhängen)“; 2015-OS-K3a.
- 2.4 Zahl in Zehnerpotenzschreibweise a · 10ⁿ mit a zwischen 1 und 10 schreiben (Komma setzen, Stellen zählen) → „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „Eine Zahl in der Form a · 10^n schreiben“; 2025-OS-B1d (850 000 = 8,5 · 10⁵). 2025-OS-B1d: Komma in 8,5 um fünf Stellen, Fehlerquelle Nullen gezählt.
- 2.5 fehlenden Exponenten in „a · 10^□“ eintragen (P10-Form) → „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „den fehlenden Exponenten angeben“; 2025-OS-B1d. Zweite Hälfte desselben Typs „fehlenden Exponenten in a · 10^□ eintragen“, die die Liste am Malpunkt trennt; 2025-OS-B1d.
- 2.6 Zehnerpotenzschreibweise ausschreiben: Komma nach rechts, Nullen auffüllen (P10-Form) → „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „als Dezimalzahl ausschreiben“; 2016-OS-B1h (8,5 · 10⁵ = 850 000).
- 2.7 passende ausgeschriebene Zahl unter drei Angeboten ankreuzen (P10-Form) → „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2015-OS-K3b: zu 9,46 · 10¹² die passende von drei ausgeschriebenen Zahlen ankreuzen.
- 2.8 kleine Zahl mit negativem Exponenten: Komma nach links, Nullen vorn (2,1 · 10⁻⁴ = 0,00021; P10-Form) → „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2019-OS-B1j: 2,1 · 10⁻⁴ = 0,00021.
- 2.9 Zahl kleiner als eins in Zehnerpotenzschreibweise schreiben (0,00035 = 3,5 · 10⁻⁴) → „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „Eine Zahl in der Form a · 10^n schreiben“ ohne Beschränkung des Exponenten; kein Original mit negativem Exponenten in dieser Richtung.
- 2.10 Zahlen in Zehnerpotenzschreibweise vergleichen und ordnen (erst Exponent, dann Faktor) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: Definition „… Potenzschreibweise in dieselbe Form bringen und ordnen“; 2017-OS-B1e (−10³ und −10² unter Dezimalzahlen).
- 2.11 negative Zehnerpotenzen auf der Zahlengerade ordnen (−10³ gegen −0,01; P10-Form) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2017-OS-B1e: die kleinste von −0,01; −10³; −10²; −0,1.
- 2.12 Taschenrechner-Anzeige „8.5E5“ lesen und Zahl mit der EXP- oder ×10ˣ-Taste eingeben → kein P10-Typ
- 2.13 gerundeter Wert in Zehnerpotenzschreibweise (9 460 730 472 581 km ≈ 9,46 · 10¹² km) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Dauer aus Menge und Rate berechnen“. Grund: 2015-OS-K3c: Ergebnis ≈ 1,34 · 10¹⁰ s als gerundeter Wert in Zehnerpotenzschreibweise.
- 2.14 Sachaufgabe aus Astronomie oder Mikrowelt (Lichtjahr, Atommasse; Einheit mitführen) → „Große Zahl mit Zehnerpotenz multiplizieren“ · „Zehnerpotenzschreibweise umwandeln“ – P10-Jahrgänge 5 (Haupt 5). Außerhalb der Themen des Eintrags (zählt nicht): „Dauer aus Menge und Rate berechnen“. Grund: Stamm „Sterne“ 2015: Lichtjahre in km (2015-OS-K3a), 9,46 · 10¹² ausgeschrieben (2015-OS-K3b) und Lichtlaufzeit (2015-OS-K3c).
- 2.15 Zehnerpotenzen multiplizieren und dividieren (Exponenten addieren, subtrahieren; Vorrat, Nebenleistung 2015-OS-K3c) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Dauer aus Menge und Rate berechnen“. Grund: 2015-OS-K3c: 4,03 · 10¹⁵ : (3 · 10⁵), Voraussetzung „Zehnerpotenzen dividieren“.
- 2.16 Fehler finden (Nullen statt Kommastellen gezählt; Nullen an alle Ziffern gehängt; Vorzeichen des Exponenten übersehen; Exponent als Zahl der Nullen bei einer Dezimalzahl) → kein P10-Typ
- 2.17 Begründen (warum 3,5 · 10⁴ und 35 · 10³ dieselbe Zahl sind; warum ein Exponent von minus vier eine Zahl kleiner als eins ergibt) → kein P10-Typ

**Einheit 3 · Quadratwurzeln** – P10-Jahrgänge 2 von 13 (davon Haupt 2); P10-Typen 2; Summe ertrag 2.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Wurzel eines Quadrats berechnen | 1 | 1 | 1 | 2015 | 2015 | 1 | 0 |  |
| Quadratseite aus Fläche berechnen | 1 | 1 | 1 | 2020 | 2020 | 1 | 0 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |

- 3.1 Quadratzahl erkennen und Wurzel im Kopf (√169 = 13; Quadratzahlen bis 20²) → „Wurzel eines Quadrats berechnen“ · „Quadratseite aus Fläche berechnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Argument zu Funktionswert berechnen“ · „Schnittpunkte Gerade und Parabel berechnen“. Grund: Wurzel aus einer Quadratzahl: √16 in 2015-OS-B1j und in der p-q-Formel von 2023-OS-K4c, √36 in 2020-OS-B1d und √9 in 2024-OS-K3d.
- 3.2 Wurzel als Umkehrung: „welche Zahl mal sich selbst gibt …“ → „Wurzel eines Quadrats berechnen“ · „Quadratseite aus Fläche berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Vorstufe: Definition „Quadrat zuerst, Wurzel ist nie negativ“ (2015-OS-B1j) und „Seitenlänge eines Quadrats als Wurzel aus dem Flächeninhalt“ (2020-OS-B1d, 6 · 6 = 36).
- 3.3 Wurzel mit dem Taschenrechner, Anzeige ablesen, auf zwei Dezimalen runden (√7 ≈ 2,65) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Pythagoras Kathete“ · „Pythagoras Hypotenuse“ · „Radius eines Zylinders aus Volumen berechnen“ · „Nullstellen quadratische Funktion berechnen“. Grund: Voraussetzung „Wurzel ziehen“ mit gerundetem Ergebnis: √855 ≈ 29,2 (2026-FOR-K4a), √29 156 ≈ 170,8 (2025-OS-K4a), r ≈ 4,40 (2022-OS-K2d) und 3 ± √2 ≈ 1,59 und 4,41 (2025-OS-K5c).
- 3.4 Wurzel zwischen zwei Nachbar-Quadratzahlen abschätzen (√50 liegt zwischen 7 und 8) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: Voraussetzung „Wurzel abschätzen“ in 2015-OS-B1c und 2014-OS-B1h.
- 3.5 Wurzel mit Dezimalzahl und Bruch vergleichen (√2 gegen 1,4; P10-Form) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: √2 gegen 3/2 in 2015-OS-B1c und gegen 1,4 in 2014-OS-B1h.
- 3.6 Zahlen mit Wurzel aufsteigend ordnen (P10-Form) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2014-OS-B1h: −1/2; 1,4; −0,512; √2 aufsteigend ordnen.
- 3.7 Wurzel eines Quadrats: erst das Quadrat, dann die Wurzel (√((−4)²) = √16 = 4; die richtige von drei Aussagen ankreuzen; P10-Form) → „Wurzel eines Quadrats berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Wert eines Terms wie √((−4)²) bestimmen oder die richtige Aussage dazu auswählen“; 2015-OS-B1j.
- 3.8 Quadrat einer Wurzel ((√5)² = 5) → kein P10-Typ
- 3.9 Wurzel aus einer negativen Zahl: kein Wert (√(−9) gegen −√9) → „Wurzel eines Quadrats berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Lösbarkeit quadratischer Gleichung beurteilen“. Grund: Gleichung ohne Lösung wie x² = −1 in 2021-OS-K7c; in 2015-OS-B1j ist „nicht definiert“ zu verwerfen, weil (−4)² nicht negativ ist.
- 3.10 Wurzel aus Dezimalzahl und Bruch (√0,25 = 0,5, √(1/4) = 1/2; nicht „halbieren“) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen“. Grund: 2025-GYM-K6c: √0,9801 = 0,99, Fehlerquelle „0,9801 durch 2 teilen statt die Quadratwurzel zu ziehen“.
- 3.11 Quadratseite aus dem Flächeninhalt (a = √A; Typ in flaechen.md Einheit 1) → „Quadratseite aus Fläche berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Grundkante aus Volumen berechnen“. Grund: Definition „Seitenlänge eines Quadrats als Wurzel aus dem Flächeninhalt“ (2020-OS-B1d); a = √62,5 für die quadratische Grundfläche in 2017-GYM-K4c.
- 3.12 Wurzel als letzter Schritt einer Formel: erst den Term unter der Wurzel ausrechnen, dann die Wurzel (Hypotenuse, Zylinderradius r = √(V : (π · h)), p-q-Formel) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Pythagoras Hypotenuse“ · „Pythagoras Kathete“ · „Radius eines Zylinders aus Volumen berechnen“ · „Nullstellen quadratische Funktion berechnen“. Grund: Die drei Beispiele des Typs: √(170² + 16²) in 2025-OS-K4a, √(384² − 255²) in 2024-OS-K6a, r = √(425 : (π · 7)) in 2022-OS-K2d und x = 3 ± √(9 − 7) in 2025-OS-K5c.
- 3.13 Kubikwurzel (³√27 = 3; Vorrat) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parameter einer Wurzelfunktion aus einem Punkt bestimmen“ · „Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen“. Grund: ³√8 = 2 in 2020-GYM-K3a und ³√x als Umkehrung von x³ in 2020-GYM-K3b.
- 3.14 Fehler finden (Wurzel halbiert statt gezogen; Wurzel termweise aus einer Summe; „nicht definiert“ bei √((−4)²); −4 als Wurzelwert; √2 als zwei gelesen) → kein P10-Typ
- 3.15 Begründen (warum √16 nicht −4 ist, obwohl (−4)² = 16 gilt; warum √50 näher an sieben als an acht liegt) → kein P10-Typ

### reelle-zahlen

themen.csv: kein msa-Thema – Vermerk: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“.

**Einheit 1 · Irrationale Zahlen und Zahlbereiche** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 1.1 Bruch in Dezimalzahl umwandeln und einordnen: abbrechend oder periodisch (3/8 = 0,375; 1/3 = 0,333…) → kein P10-Typ
- 1.2 Dezimalzahl als Bruch schreiben (rational) → kein P10-Typ
- 1.3 Wurzel rational oder irrational: Radikand Quadratzahl (√49 = 7) oder nicht (√50 ≈ 7,07 – kein Bruch) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Nullstellen quadratische Funktion berechnen“ · „Argument zu Funktionswert berechnen“ · „Schnittpunkte Gerade und Parabel berechnen“. Grund: Ob die Wurzel der p-q-Formel aufgeht, entscheidet über exakte oder genäherte Lösungen: √16 in 2023-OS-K4c und √9 in 2024-OS-K3d gegen √2 in 2025-OS-K5c.
- 1.4 irrationale Zahlen nennen (√2, √3, √5, π) und mit dem Taschenrechner den Näherungswert ablesen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: Näherungswert √2 ≈ 1,41 in 2015-OS-B1c und ≈ 1,414 in 2014-OS-B1h.
- 1.5 Zahlen in ℕ, ℤ, ℚ, ℝ einordnen (Tabelle mit Kreuzen, Venn-Diagramm: −4, 0,75, √16, √17, π, 2/3) → kein P10-Typ
- 1.6 Teilmengenkette ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ erklären (jede natürliche Zahl ist ganz, jede ganze rational, jede rationale reell) → kein P10-Typ
- 1.7 irrationale Zahl auf der Zahlengeraden zwischen zwei Zehntel einordnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2014-OS-B1h: √2 ≈ 1,414 liegt zwischen 1,4 und 1,5 und steht darum hinter 1,4.
- 1.8 reelle Zahlen vergleichen und ordnen über Näherungswerte (√10, 3,2, 3 1/5) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2015-OS-B1c und 2014-OS-B1h ordnen √2 über den Näherungswert zwischen Brüche und Dezimalzahlen.
- 1.9 exakt und gerundet: Wurzel als exaktes Ergebnis stehen lassen, dann Näherungswert mit ≈ (P10-Form 2025-OS-K5c „x = 3 ± √2“) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Nullstellen quadratische Funktion berechnen“ · „Streckenlänge aus Koordinaten berechnen“. Grund: P10-Form 2025-OS-K5c (x = 3 ± √2 und N1(1,59|0)), ebenso 2017-OS-K5d (Nebentyp) und BC = √20 ≈ 4,47 in 2019-OS-K2d.
- 1.10 Rechnen mit Wurzeln, das rational wird (√2 · √2 = 2; √8 : √2 = 2; √2 − √2 = 0) → kein P10-Typ
- 1.11 Einschachtelung von √2: Tabelle Zehntel, Hundertstel (Vorrat, H, GYM) → kein P10-Typ
- 1.12 Fehler finden (Taschenrechner-Anzeige als exakter Wert; periodische Dezimalzahl für irrational gehalten; √4 als irrational, weil Wurzel) → kein P10-Typ
- 1.13 Begründen (warum √2 kein Bruch sein kann – Widerspruchsidee in Worten; warum 22/7 nicht π ist) → kein P10-Typ

**Einheit 2 · Potenzgesetze** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 2.1 Produkt gleicher Basen als Malkette schreiben, Faktoren zählen, Exponenten addieren (2³ · 2⁴ = 2⁷) → kein P10-Typ
- 2.2 Quotient gleicher Basen: Exponenten subtrahieren (5⁶ : 5² = 5⁴; 3² : 3² = 3⁰ = 1; 2³ : 2⁵ = 2⁻²) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Dauer aus Menge und Rate berechnen“. Grund: 2015-OS-K3c: 10¹⁵ : 10⁵ = 10¹⁰, Fehlerquelle 10³.
- 2.3 Potenz einer Potenz: Exponenten multiplizieren ((3²)⁴ = 3⁸) → kein P10-Typ
- 2.4 gleicher Exponent: Basen multiplizieren (2⁵ · 3⁵ = 6⁵) oder dividieren (10⁴ : 5⁴ = 2⁴) → kein P10-Typ
- 2.5 Gesetz erkennen: gleiche Basis, gleicher Exponent oder keins (dann ausrechnen) → kein P10-Typ
- 2.6 gemischte Terme mit Zahlen: erst das Gesetz, dann ausrechnen (2³ · 2² · 5 = 2⁵ · 5 = 160) → kein P10-Typ
- 2.7 Terme mit Variablen (x³ · x⁴ = x⁷; a⁵ : a² = a³; (y²)³ = y⁶) → kein P10-Typ
- 2.8 Vorzahlen getrennt (3x² · 4x³ = 12x⁵) → kein P10-Typ
- 2.9 Potenzen mit negativem Exponenten in Brüche und zurück (Blatt 0 aus potenzen-wurzeln.md; LISUM-PH) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Zahlen in verschiedenen Darstellungen vergleichen“. Grund: 2022-OS-B1j: 2⁻⁵ = 1 : 2⁵ = 1/32.
- 2.10 Potenzen addieren: nur gleiche zusammenfassen (2⁵ + 2⁵ = 2 · 2⁵ = 2⁶; 2³ + 2⁴ = 24) → kein P10-Typ
- 2.11 Terme mit zwei Variablen und Klammern (Vorrat: (2ab)³ = 8a³b³) → kein P10-Typ
- 2.12 Fehler finden (Basen multipliziert; Exponenten multipliziert statt addiert; Potenzen addiert wie multipliziert) → kein P10-Typ
- 2.13 Begründen (warum 2³ · 2⁴ nicht 4⁷ ist – Malkette zählen; warum a⁰ = 1 sein muss – Quotient gleicher Potenzen) → kein P10-Typ

**Einheit 3 · Wurzelgesetze und rationale Exponenten** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 3.1 Wurzel aus Produkt: beide Wege rechnen und vergleichen (√4 · √9 = 2 · 3 = 6 = √36) → kein P10-Typ
- 3.2 Wurzel aus Quotient (√(36/4) = √36 : √4 = 3) → kein P10-Typ
- 3.3 teilweises Wurzelziehen: Quadratzahl als Faktor abspalten (√50 = √25 · √2 = 5√2; √72 = 6√2) → kein P10-Typ
- 3.4 Wurzeln mit gleichem Radikanden zusammenfassen (3√2 + 5√2 = 8√2) → kein P10-Typ
- 3.5 Summe unter der Wurzel erst ausrechnen (√(9 + 16) = 5, nicht 3 + 4; Pythagoras-Form) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Pythagoras Hypotenuse“ · „Pythagoras Kathete“ · „Streckenlänge aus Koordinaten berechnen“ · „Mantellinie Kegel bestimmen“. Grund: Summe oder Differenz unter der Wurzel zuerst: √(170² + 16²) (2025-OS-K4a), √(32² − 13²) = √855 (2026-FOR-K4a), BC² = 2² + 4² = 20 (2019-OS-K2d) und s = √(r² + h²) (2018-OS-K6d).
- 3.6 Nenner rational machen (Vorrat: 1/√2 = √2/2) → kein P10-Typ
- 3.7 Wurzel als Potenz mit Exponent 1/2 (√a = a^(1/2)), Taschenrechner mit Klammer (8^(1/3)) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parameter einer Wurzelfunktion aus einem Punkt bestimmen“. Grund: 2020-GYM-K3a rechnet ⁿ√8 als 8^(1/n) = 2.
- 3.8 n-te Wurzel als a^(1/n), Kubikwurzel (³√8 = 2, ³√27 = 3) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parameter einer Wurzelfunktion aus einem Punkt bestimmen“ · „Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen“. Grund: 2020-GYM-K3a (8^(1/n) = 2, also ³√8 = 2) und 2020-GYM-K3b (³√x mit der Umkehrung x³).
- 3.9 Potenzgesetze auf Wurzeln übertragen (√a · √a = a^(1/2 + 1/2) = a; ⁴√(a²) = a^(1/2)) → kein P10-Typ
- 3.10 Wurzelgesetz mit den Potenzgesetzen begründen (Vorrat, H, GYM) → kein P10-Typ
- 3.11 einfache Gleichung mit Potenz oder Wurzel: x³ = 27, √x = 4 (Vorrat; x² = c → quadratische-gleichungen.md) → kein P10-Typ
- 3.12 Fehler finden (Wurzeln addiert wie Faktoren; Wurzel halbiert; Bruch-Exponent als Bruch der Basis; Taschenrechner ohne Klammer) → kein P10-Typ
- 3.13 Begründen (warum √(a + b) nicht √a + √b ist – Zahlenbeispiel; warum √a = a^(1/2) gelten muss – Quadrat mit dem Potenzgesetz) → kein P10-Typ

### einheiten

themen.csv: „Einheiten umrechnen“ – Vermerk: „Sammelthema; Typen gemischt“.

**Einheit 1 · Länge, Masse, Geld** – P10-Jahrgänge 4 von 13 (davon Haupt 4); P10-Typen 4; Summe ertrag 8.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Größen vergleichen | 3 | 2 | 2 | 2019 | 2026 | 3 | 0 |  |
| Längeneinheit mit Faktor umrechnen | 1 | 1 | 1 | 2016 | 2016 | 0 | 1 |  |
| Fehler in Rechnung erklären und korrigieren | 4 | 1 | 1 | 2014 | 2014 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Materialbedarf aus Längen berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Einheiten der Länge, der Masse und des Geldes der Größe nach ordnen → „Größen vergleichen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Vorstufe des Vergleichens: welche Einheit die größere ist, legt in 2019-OS-B1b (0,06 m □ 60 cm) und 2026-FOR-B1d (3,5 m □ 35 cm) die Richtung der Umrechnung fest.
- 1.2 Repräsentanten zuordnen (welche Angabe passt zu welchem Gegenstand) → kein P10-Typ
- 1.3 in die Nachbareinheit umrechnen, größer nach kleiner (mal) → „Größen vergleichen“ · „Fehler in Rechnung erklären und korrigieren“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: Grundschritt der Umrechnungen Meter in Zentimeter in 2019-OS-B1b, 2026-FOR-B1d und 2018-OS-B1b (Definition „nach Umrechnung in eine gemeinsame Einheit“); als einzelner Schritt Euro in Cent in 2014-OS-K4e (585 € = 58 500 ct).
- 1.4 in die Nachbareinheit umrechnen, kleiner nach größer (geteilt) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“ · „Dauer aus Menge und Rate berechnen“. Grund: 2014-OS-K2a rechnet 2800 m in 2,8 km um (Definition „nach Umrechnung in eine gemeinsame Einheit (cm, m, km)“), 2014-OS-K2c 2500 m in 2,5 km vor der Division durch 5 km/h.
- 1.5 über zwei Stufen umrechnen (Millimeter in Meter) → „Größen vergleichen“ · „Materialbedarf aus Längen berechnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: Meter in Zentimeter über zwei Stufen in 2019-OS-B1b (0,06 m = 6 cm), 2026-FOR-B1d (3,5 m = 350 cm) und 2018-OS-B1b (5 m = 500 cm); Millimeter in Meter in 2016-GYM-K3a (180 mm = 0,18 m).
- 1.6 Kilometer und Meter (Umrechnungszahl tausend) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“ · „Dauer aus Menge und Rate berechnen“. Grund: 2014-OS-K2a (2800 m + 1,5 km = 4,3 km, Fehlerquelle 2801,5) und 2014-OS-K2c (2500 m = 2,5 km bei 5 km/h).
- 1.7 gemischte Angabe in eine Einheit bringen (2 m 30 cm) und zurück → kein P10-Typ
- 1.8 Komma setzen: Größe in der Stellenwerttafel lesen → „Größen vergleichen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Die Hürde beider Originale ist die Kommastelle: 2019-OS-B1b (Fehlerquelle 0,06 m als 60 cm) und 2026-FOR-B1d (Fehlerquelle 3,5 m als 35 cm).
- 1.9 zwei Größen mit verschiedenen Einheiten vergleichen und das Zeichen setzen (P10-Form) → „Größen vergleichen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „Zwei Größen mit verschiedenen Einheiten vergleichen und <, = oder > setzen“; 2019-OS-B1b, 2026-FOR-B1d.
- 1.10 drei bis vier Größen ordnen → kein P10-Typ
- 1.11 Umrechnen mit gegebenem Faktor bei nichtmetrischen Einheiten (Fuß, Meile, Zoll; P10-Form) → „Längeneinheit mit Faktor umrechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „mit gegebenem Umrechnungsfaktor (Fuß, Meile, Zoll) in Meter oder Zentimeter umrechnen“; 2016-OS-K3a (7 · 0,305 m).
- 1.12 Nachweis einer vorgegebenen Länge mit dem Faktor (P10-Form) → „Längeneinheit mit Faktor umrechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2016-OS-K3a: die vorgegebene Angabe d ≈ 2,14 m mit 7 · 0,305 m = 2,135 m nachweisen (Nebentyp „Behauptung prüfen“).
- 1.13 Größen mit gleicher Einheit addieren und subtrahieren → „Materialbedarf aus Längen berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: Definition „als Summe oder Differenz gegebener Teilstrecken“: 2018-OS-B1b (500 cm − 5 · 30 cm) und 2014-OS-K2a (2,8 km + 1,5 km); 2016-GYM-K3a addiert 60 + 100 + 20 mm.
- 1.14 Fehler finden (mal statt geteilt; Komma um eine Stelle verrutscht; Zahlen ohne Umrechnung verglichen) → kein P10-Typ
- 1.15 Begründen (warum 0,06 m weniger ist als 60 cm) → kein P10-Typ

**Einheit 2 · Zeit** – P10-Jahrgänge 6 von 13 (davon Haupt 4); P10-Typen 2; Summe ertrag 4.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Zeiteinheiten umrechnen | 3 | 3 | 4 | 2015 | 2025 | 3 | 0 |  |
| Uhrzeit aus Startzeit und Dauer berechnen | 1 | 1 | 2 | 2014 | 2021 | 1 | 0 |  |

- 2.1 Zeiteinheiten nennen und ordnen → „Zeiteinheiten umrechnen“ – P10-Jahrgänge 4 (Haupt 3). Grund: Vorstufe: die Zeiteinheiten mit ihren Umrechnungszahlen trägt jede Umrechnung der Definition „Zeitangaben zwischen h, min und s umrechnen“.
- 2.2 Minuten in Stunden und Stunden in Minuten → „Zeiteinheiten umrechnen“ – P10-Jahrgänge 4 (Haupt 3). Grund: Definition „Zeitangaben zwischen h, min und s umrechnen“; Grundfall der Originale 2018-OS-B1e, 2025-OS-B1b und 2024-OS-B1a.
- 2.3 Sekunden in Minuten → „Zeiteinheiten umrechnen“ – P10-Jahrgänge 4 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Dauer aus Menge und Rate berechnen“. Grund: 2024-OS-K6c: 120 s = 2 min als Nebentyp „Zeiteinheiten umrechnen“ im Haupttyp „Dauer aus Menge und Rate berechnen“ (Definition „in die verlangte Zeiteinheit umrechnen“).
- 2.4 Dezimalstunden in Minuten (P10-Form: eineinhalb Stunden, drei Komma zwei fünf Stunden) → „Zeiteinheiten umrechnen“ – P10-Jahrgänge 4 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Dauer aus Menge und Rate berechnen“. Grund: Definition „auch aus Dezimalstunden“: 2018-OS-B1e (3,5 h), 2025-OS-B1b (1,5 h), 2024-OS-B1a (3,25 h); dazu 2014-OS-K2c (0,5 h = 30 min).
- 2.5 Minuten als Dezimalstunde schreiben → „Zeiteinheiten umrechnen“ – P10-Jahrgänge 4 (Haupt 3). Grund: Andere Richtung derselben Definition „Zeitangaben zwischen h, min und s umrechnen“; kein Original in dieser Richtung.
- 2.6 Zeitspanne zwischen zwei Uhrzeiten → kein P10-Typ
- 2.7 Endzeit aus Startzeit und Dauer mit Übertrag bei sechzig Minuten (P10-Form) → „Uhrzeit aus Startzeit und Dauer berechnen“ – P10-Jahrgänge 2 (Haupt 1). Grund: Definition „die End- oder Startzeit bestimmen, mit Übertrag bei 60 Minuten“; 2021-OS-B1a (11:38 Uhr + 2 h 35 min = 14:13 Uhr).
- 2.8 Startzeit aus Endzeit und Dauer → „Uhrzeit aus Startzeit und Dauer berechnen“ – P10-Jahrgänge 2 (Haupt 1). Grund: Definition „die End- oder Startzeit bestimmen“; kein Original in dieser Richtung.
- 2.9 Dauer mit Pause (zwei Abschnitte addieren) → „Uhrzeit aus Startzeit und Dauer berechnen“ – P10-Jahrgänge 2 (Haupt 1). Grund: 2014-OS-K2c: 11:30 Uhr + 45 min Pause + 30 min Weg = 12:45 Uhr (Nebentyp, Fehlerquelle Pause vergessen).
- 2.10 Fahrplan: nächste Abfahrt, Fahrzeit → kein P10-Typ
- 2.11 Dauer in eine sinnvolle Einheit bringen (Sekunden in Minuten, Stunden in Tage) → „Zeiteinheiten umrechnen“ – P10-Jahrgänge 4 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Dauer aus Menge und Rate berechnen“. Grund: 2024-OS-K6c (120 s als 2 min) und 2015-OS-K3c (1,34 · 10¹⁰ s in Jahren), beide mit „Zeiteinheiten umrechnen“ als Nebentyp.
- 2.12 Fehler finden (Dezimalstunde als Minutenangabe gelesen; Übertrag bei sechzig vergessen) → kein P10-Typ
- 2.13 Begründen (warum die Umrechnungszahl hier nicht zehn ist) → kein P10-Typ

**Einheit 3 · Flächen- und Volumeneinheiten** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 3; Summe ertrag 8.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Portionen aus Gesamtmenge berechnen | 1 | 1 | 1 | 2022 | 2022 | 1 | 0 |  |
| Materialbedarf aus Fläche berechnen | 3 | 1 | 1 | 2015 | 2015 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Fehler in Rechnung erklären und korrigieren | 4 | 1 | 1 | 2014 | 2014 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 3.1 Flächeneinheiten ordnen (mm² bis km², a und ha einordnen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen“. Grund: Vorstufe von 3.2 und 3.3: das einzige Original mit Flächenumrechnung, 2016-GYM-K5b, verlangt Hektar (546 409 m² ≈ 54,6 ha).
- 3.2 Flächeneinheit in die Nachbareinheit umrechnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen“. Grund: Teilschritt von 2016-GYM-K5b: Quadratmeter über Ar in Hektar (Fehlerquelle „ha und m² bei der Volumenrechnung nicht umrechnen“).
- 3.3 über zwei Stufen (mm² in dm²) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen“. Grund: 2016-GYM-K5b rechnet 546 409 m² in 54,64 ha um, zwei Stufen mit der Umrechnungszahl hundert.
- 3.4 Volumeneinheiten ordnen (mm³ bis m³) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Volumen Zylinder berechnen“ · „Höhe eines Zylinders aus Volumen berechnen“ · „Dauer aus Menge und Rate berechnen“. Grund: Vorstufe von 3.5: die Richtung der Umrechnung in 2021-OS-K4a (cm³ in dm³), 2023-OS-K5d (1 l = 1000 cm³) und 2017-OS-K3d (m³ in l).
- 3.5 Volumeneinheit in die Nachbareinheit umrechnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Volumen Zylinder berechnen“ · „Höhe eines Zylinders aus Volumen berechnen“ · „Dauer aus Menge und Rate berechnen“. Grund: Umrechnungszahl tausend in 2021-OS-K4a (250 998 cm³ ≈ 251 dm³, Fehlerquelle Faktor 100), 2023-OS-K5d (1 l als 1000 cm³, Fehlerquelle 100 cm³) und 2017-OS-K3d (140 m³ = 140 000 l, Fehlerquelle 1 m³ = 100 l).
- 3.6 Liter und Kubikdezimeter, Milliliter und Kubikzentimeter gleichsetzen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Volumen Zylinder berechnen“ · „Höhe eines Zylinders aus Volumen berechnen“ · „Radius eines Zylinders aus Volumen berechnen“. Grund: 2021-OS-K4a („1 l = 1 dm³“), 2022-OS-K2b und 2023-OS-K5b („1 cm³ = 1 ml“), 2023-OS-K5d (1 l = 1000 cm³) und 2022-OS-K2d (425 ml als 425 cm³).
- 3.7 Liter in Milliliter und zurück (P10-Form) → „Portionen aus Gesamtmenge berechnen“ · „Materialbedarf aus Fläche berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2022-OS-B1h (1,5 l = 1500 ml, Fehlerquelle 150 ml) und 2015-OS-K6d (0,256 l = 256 ml gegen Dosen zu 375 ml).
- 3.8 Kubikmeter in Liter (P10-Form) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Dauer aus Menge und Rate berechnen“. Grund: 2017-OS-K3d: 140 m³ = 140 000 l vor der Division durch 17 500 l je Stunde (Original hier geführt, Typ bei zuordnungen.md).
- 3.9 Portionen aus einer Gesamtmenge nach Umrechnung (P10-Form) → „Portionen aus Gesamtmenge berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Anzahl gleicher Portionen aus Gesamtmenge und Portionsgröße berechnen, nach Umrechnung der Einheiten“; 2022-OS-B1h.
- 3.10 Repräsentanten zuordnen → kein P10-Typ
- 3.11 Einheitenvorsatz als Name für eine Zehnerpotenz lesen (Milli, Zenti, Kilo; Verfahren in potenzen-wurzeln.md Einheit 2) → kein P10-Typ
- 3.12 Vorsätze von Nano bis Tera (Vorrat) → kein P10-Typ
- 3.13 Fehler finden (Flächeneinheit mit zehn statt hundert umgerechnet; Kubikmeter mit hundert statt tausend in Liter) → „Fehler in Rechnung erklären und korrigieren“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „den Fehler (z. B. falscher Umrechnungsfaktor zwischen Einheiten) benennen“ – dieselbe Leistung wie in 2014-OS-K4e (Faktor 1000 statt 100), hier mit Flächen- und Volumeneinheiten.
- 3.14 Begründen (warum bei Flächen die Umrechnungszahl hundert ist – zwei Längen) → kein P10-Typ

**Einheit 4 · Mit Größen rechnen im Sachzusammenhang** – P10-Jahrgänge 5 von 13 (davon Haupt 4); P10-Typen 6; Summe ertrag 10.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Volumen aus Masse und Dichte berechnen | 2 | 1 | 1 | 2016 | 2016 | 0 | 1 |  |
| Masse aus Volumen und Dichte berechnen | 0 | 0 | 1 | 2019 | 2019 | 0 | 0 |  |
| Materialbedarf aus Fläche berechnen | 3 | 1 | 1 | 2015 | 2015 | 0 | 1 |  |
| Fehler in Rechnung erklären und korrigieren | 4 | 1 | 1 | 2014 | 2014 | 0 | 1 |  |
| Portionen aus Gesamtmenge berechnen | 1 | 1 | 1 | 2022 | 2022 | 1 | 0 | nicht in der Zuordnungszeile der Einheit |
| Materialbedarf aus Längen berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 4.1 gegebene Größen vor dem Rechnen auf eine Einheit bringen → „Portionen aus Gesamtmenge berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“ · „Dauer aus Menge und Rate berechnen“. Grund: Definitionen „nach Umrechnung der Einheiten“ (2022-OS-B1h) und „nach Umrechnung in eine gemeinsame Einheit“ (2014-OS-K2a, Fehlerquelle 2800 + 1,5); 2017-OS-K3d rechnet 140 m³ vor der Division in Liter um.
- 4.2 Ergebnis in eine sinnvolle Einheit umrechnen (0,6 m als 60 cm angeben) → „Materialbedarf aus Fläche berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Länge im Maßstab umrechnen“ · „Dauer aus Menge und Rate berechnen“. Grund: 2018-OS-K6c (0,6 m = 60 cm, Definition „mit passender Einheit“), 2015-OS-K6d (0,256 l = 256 ml) und 2024-OS-K6c (120 s = 2 min, Definition „in die verlangte Zeiteinheit umrechnen“).
- 4.3 Masse aus Volumen und Dichte (P10-Form) → „Masse aus Volumen und Dichte berechnen“ – P10-Jahrgänge 1 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Volumen zusammengesetzter Körper berechnen“. Grund: Definition „Masse aus Volumen und Masse je Volumeneinheit (Dichte) berechnen“, einziges Original 2019-OS-K4c (Nebentyp); GYM-Definition „und daraus über die Dichte die Masse bestimmen“ (2016-GYM-K3b).
- 4.4 Volumen aus Masse und Dichte durch Umstellen (P10-Form) → „Volumen aus Masse und Dichte berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „durch Umstellen von ϱ = m : V“; 2016-OS-K3d (4000 : 7,8 ≈ 512,8 cm³).
- 4.5 Dichte aus Masse und Volumen (Vorrat) → kein P10-Typ
- 4.6 Masse eines Anteils (Füllgrad in Prozent) und Leermasse addieren (P10-Form) → „Masse aus Volumen und Dichte berechnen“ – P10-Jahrgänge 1 (Haupt 0). Grund: Definition „ggf. mit Füllgrad in Prozent und Leermasse“; 2019-OS-K4c (10 % von 1,2 m³ Wasser ≙ 120 kg, plus 200 kg).
- 4.7 Materialbedarf aus Fläche und Ergiebigkeit, mehrere Flächen, zweiter Anstrich (P10-Form) → „Materialbedarf aus Fläche berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „aus zu bearbeitender Fläche (mehrere Flächen, mehrere Anstriche) und Ergiebigkeit (m² je Liter)“; 2015-OS-K6d (4 · 0,32 m² · 2 bei 10 m² je Liter).
- 4.8 Bedarf mit Gebindegrößen vergleichen und entscheiden (P10-Form) → „Materialbedarf aus Fläche berechnen“ · „Materialbedarf aus Längen berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: Definition „und mit Gebindegrößen vergleichen“; 2015-OS-K6d entscheidet mit Nebentyp „Behauptung prüfen“, ob Dose S (375 ml) reicht; 2016-GYM-K3a teilt durch die Stranglänge 6 m.
- 4.9 Euro und Cent in einer Rechnung → „Fehler in Rechnung erklären und korrigieren“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Kosten aus Menge und Preis berechnen“. Grund: 2014-OS-K4e (585 € = 58 500 ct, dann 58 500 ct : 100 000) und 2024-OS-K2d (16 · 0,14 ct, Fehlerquelle 0,14 ct als 0,14 €).
- 4.10 eine fremde Rechnung nachrechnen und den Einheitenfehler benennen (P10-Form) → „Fehler in Rechnung erklären und korrigieren“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „In einer vorgegebenen Schülerrechnung den Fehler (z. B. falscher Umrechnungsfaktor zwischen Einheiten) benennen“; 2014-OS-K4e.
- 4.11 die Rechnung berichtigen und die Behauptung korrigieren (P10-Form) → „Fehler in Rechnung erklären und korrigieren“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: Definition „die Rechnung berichtigen und die daraus abgeleitete Behauptung korrigieren“; 2014-OS-K4e korrigiert „ca. 6 ct“ auf ca. 0,6 ct je Kilometer (Nebentyp „Behauptung prüfen“).
- 4.12 Fehler finden (Faktor tausend statt hundert bei Euro und Cent; nur eine der beiden Größen umgerechnet) → „Fehler in Rechnung erklären und korrigieren“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2014-OS-K4e verlangt genau diesen Fehler zu benennen: 585 € als 585 000 ct, Faktor 1000 statt 100.
- 4.13 Begründen (warum das Ergebnis in dieser Einheit unhandlich ist) → kein P10-Typ

### flaechen

themen.csv: „Flächeninhalt und Umfang“ – Vermerk: „enthält Kreisaufgaben; kreis hat kein msa-Thema“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Kreisfläche berechnen“; „Kreissektor Anteil berechnen“; „Kreisumfang berechnen“; „Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen“; „Anzahl gleicher Rechtecke auf Fläche bestimmen“; „Kreisringmaß aus Fläche berechnen“.

**Einheit 1 · Rechteck, Quadrat, Umfang** – P10-Jahrgänge 10 von 13 (davon Haupt 9); P10-Typen 7; Summe ertrag 15.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Umfang Rechteck berechnen | 2 | 1 | 1 | 2026 | 2026 | 2 | 0 |  |
| Rechteckseite aus Fläche berechnen | 3 | 2 | 2 | 2014 | 2023 | 1 | 1 |  |
| Rechteckseite aus Umfang berechnen | 1 | 1 | 1 | 2018 | 2018 | 1 | 0 |  |
| Quadratseite aus Fläche berechnen | 1 | 1 | 1 | 2020 | 2020 | 1 | 0 |  |
| Flächeninhalt Rechteck berechnen | 0 | 0 | 2 | 2017 | 2018 | 0 | 0 |  |
| Term zu Figur angeben | 5 | 5 | 5 | 2014 | 2025 | 5 | 0 |  |
| Umfang Trapez berechnen | 3 | 1 | 1 | 2023 | 2023 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 1.1 Rechteck A und u aus a und b → „Flächeninhalt Rechteck berechnen“ · „Umfang Rechteck berechnen“ – P10-Jahrgänge 3 (Haupt 1). Grund: Definitionen „Flächeninhalt eines Rechtecks aus Länge und Breite“ und „Umfang eines Rechtecks aus Länge und Breite“; 2026-FOR-B1h (u = 10 cm), A als Nebenleistung in 2017-OS-K3b und 2018-OS-K6a.
- 1.2 Quadrat A und u aus a → „Flächeninhalt Rechteck berechnen“ · „Umfang Rechteck berechnen“ – P10-Jahrgänge 3 (Haupt 1). Grund: Das Quadrat ist der Grundfall a = b derselben Rechteckformeln (Definitionen „aus Länge und Breite“); kein eigenes Original.
- 1.3 Umfang eines Vielecks aus allen Seiten → „Umfang Rechteck berechnen“ · „Umfang Trapez berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Der Umfang als Summe aller Seiten ist Teilschritt von 2026-FOR-B1h (u = 2 · (3,5 + 1,5)) und Schlussschritt von 2023-OS-K2c (U = 15 + 25,8 + 2s).
- 1.4 Seite aus A und anderer Seite (A : b) → „Rechteckseite aus Fläche berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „Länge oder Breite eines Rechtecks aus Flächeninhalt und der anderen Seite“; 2023-OS-B1c (42 000 : 400) und 2014-OS-K5d.
- 1.5 Seite aus u und anderer Seite → „Rechteckseite aus Umfang berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „aus Umfang und der anderen Seite durch Umstellen von u = 2a + 2b“; 2018-OS-B1f.
- 1.6 Quadratseite als Wurzel aus A → „Quadratseite aus Fläche berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „als Wurzel aus dem Flächeninhalt“; 2020-OS-B1d (√36 = 6 cm).
- 1.7 aus Rechtecken zusammengesetzte Fläche (Summe) → „Flächeninhalt Rechteck berechnen“ – P10-Jahrgänge 2 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Mantelfläche Prisma berechnen“. Grund: Definition „auch als Summe mehrerer Rechtecke“; 2019-OS-K4b addiert drei gleiche Rechtecke (3 · 1,5 · 1,2), Original hier in Einheit 1, Typ bei koerper.md.
- 1.8 Term zu Figur (Fläche oder Umfang mit Variablen) → „Term zu Figur angeben“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „den Term für Flächeninhalt oder Umfang angeben“; 2019-OS-B1e und 2025-OS-B1i (Rechtecke), 2014-OS-B1g (Kreuz aus Quadraten, u = 16a).
- 1.9 Einheit wechseln vor dem Rechnen (cm und m gemischt) → „Rechteckseite aus Fläche berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2014-OS-K5d: Rückwand in cm, Platte in m² und m (Voraussetzung „m² und cm umrechnen“, 1,65 m gegen 1,5 m).
- 1.10 Fehler finden (Fläche und Umfang vertauscht) → kein P10-Typ
- 1.11 Begründen (warum a · b) → kein P10-Typ

**Einheit 2 · Parallelogramm** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 2.1 A aus g und h → kein P10-Typ
- 2.2 Höhe zur Grundseite erkennen (nicht die schräge Seite) → kein P10-Typ
- 2.3 A mit zwei verschiedenen Grundseiten (gleicher Wert) → kein P10-Typ
- 2.4 g oder h aus A → kein P10-Typ
- 2.5 Umfang aus den Seiten → kein P10-Typ
- 2.6 Begründen (Dreieck abschneiden und anlegen) → kein P10-Typ
- 2.7 Fehler finden (schräge Seite als Höhe) → kein P10-Typ

**Einheit 3 · Dreieck** – P10-Jahrgänge 7 von 13 (davon Haupt 7); P10-Typen 3; Summe ertrag 21.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Flächeninhalt Dreieck berechnen | 14 | 3 | 3 | 2015 | 2022 | 0 | 4 |  |
| Grundseite aus Dreiecksfläche berechnen | 2 | 1 | 1 | 2020 | 2020 | 0 | 1 |  |
| Term zu Figur angeben | 5 | 5 | 5 | 2014 | 2025 | 5 | 0 |  |

- 3.1 A aus g und h → „Flächeninhalt Dreieck berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Definition „Flächeninhalt eines Dreiecks aus Grundseite und Höhe“; 2015-OS-K6c, 2022-OS-K5e, 2019-OS-K4c.
- 3.2 rechtwinklig: Katheten als g und h → „Flächeninhalt Dreieck berechnen“ · „Term zu Figur angeben“ · „Grundseite aus Dreiecksfläche berechnen“ – P10-Jahrgänge 7 (Haupt 7). Grund: Katheten als Grundseite und Höhe in 2015-OS-K5d (A = ½ · AE · DE), 2022-OS-B1e (A = d · e : 2) und 2020-OS-K7b (A = ½ · QC · BC).
- 3.3 Höhe zur passenden Grundseite wählen (drei Höhen) → „Flächeninhalt Dreieck berechnen“ · „Grundseite aus Dreiecksfläche berechnen“ – P10-Jahrgänge 4 (Haupt 4). Grund: 2022-OS-K5e (h_c zur Seite c, Fehlerquelle „a als Höhe verwenden“) und 2020-OS-K7b (Fehlerquelle „AC statt BC als Höhe“).
- 3.4 stumpfwinklig, Höhe außerhalb → „Flächeninhalt Dreieck berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Definition „aus Grundseite und Höhe“ ohne Einschränkung der Dreiecksform; kein Original mit Höhe außerhalb.
- 3.5 g oder h aus A (umstellen) → „Grundseite aus Dreiecksfläche berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Grundseite oder Höhe eines Dreiecks aus Flächeninhalt und der anderen Größe durch Umstellen“; 2020-OS-K7b (QC = 2 · 90 : 12).
- 3.6 Umfang → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Umfang eines Dreiecks aus Koordinaten berechnen“. Grund: GYM-Definition „indem die drei Seitenlängen … bestimmt und addiert werden“ (2015-GYM-K2c); der Umfang als Summe der Seiten ist deren Schlussschritt.
- 3.7 Term zu Figur (Umfang gleichseitig 3 · a; Fläche rechtwinklig) → „Term zu Figur angeben“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „den Term für Flächeninhalt oder Umfang angeben“; 2024-OS-B1c (u = 3 · a) und 2022-OS-B1e (A = d · e : 2).
- 3.8 Fehler finden (Faktor ½ vergessen; Hypotenuse als Höhe) → kein P10-Typ
- 3.9 Begründen (halbes Parallelogramm) → kein P10-Typ

**Einheit 4 · Trapez, Drachenviereck, Raute** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 4; Summe ertrag 10.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Flächeninhalt Trapez berechnen | 2 | 1 | 1 | 2023 | 2023 | 0 | 1 |  |
| Trapezhöhe aus Fläche berechnen | 3 | 1 | 1 | 2014 | 2014 | 0 | 1 |  |
| Umfang Trapez berechnen | 3 | 1 | 1 | 2023 | 2023 | 0 | 1 |  |
| Flächeninhalt Drachenviereck berechnen | 2 | 1 | 1 | 2025 | 2025 | 0 | 1 |  |

- 4.1 Trapez A aus a, c, h → „Flächeninhalt Trapez berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „aus den parallelen Seiten und der Höhe“; 2023-OS-K2b.
- 4.2 Höhe aus A und den parallelen Seiten → „Trapezhöhe aus Fläche berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „aus Flächeninhalt und den parallelen Seiten durch Umstellen der Trapezformel“; 2014-OS-K5c (h = 2 · 5 225 : 190).
- 4.3 Umfang mit gegebenen Schenkeln → „Umfang Trapez berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Vorstufe: der Schlussschritt von 2023-OS-K2c (U = 15 + 25,8 + 2s) ohne die Schenkelberechnung.
- 4.4 Umfang mit Schenkel aus Pythagoras oder Sinus (Vorrat) → „Umfang Trapez berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „dessen Schenkel erst über Trigonometrie oder Pythagoras bestimmt werden müssen“; 2023-OS-K2c.
- 4.5 Drachen und Raute A aus e und f → „Flächeninhalt Drachenviereck berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „eines Drachenvierecks oder einer Raute aus den Diagonalen“; 2025-OS-K2b.
- 4.6 Diagonale aus A → kein P10-Typ
- 4.7 Fehler finden (Grundseite mal Höhe ohne Mittelung; ½ vergessen) → kein P10-Typ
- 4.8 Begründen (zwei Trapeze ergeben ein Parallelogramm) → kein P10-Typ

**Einheit 5 · Zusammengesetzte Figuren** – P10-Jahrgänge 8 von 13 (davon Haupt 8); P10-Typen 6; Summe ertrag 20.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Figur in Teilflächen zerlegen | 2 | 1 | 1 | 2017 | 2017 | 0 | 1 |  |
| Flächeninhalt zusammengesetzter Figur berechnen | 3 | 1 | 1 | 2017 | 2017 | 0 | 1 |  |
| Restfläche berechnen | 3 | 1 | 1 | 2018 | 2018 | 0 | 1 |  |
| Verschnitt in Prozent berechnen | 4 | 1 | 1 | 2023 | 2023 | 0 | 1 |  |
| Term zu Figur angeben | 5 | 5 | 5 | 2014 | 2025 | 5 | 0 | nicht in der Zuordnungszeile der Einheit |
| Rechteckseite aus Fläche berechnen | 3 | 2 | 2 | 2014 | 2023 | 1 | 1 | nicht in der Zuordnungszeile der Einheit |

- 5.1 Teilflächen erkennen und benennen (Rechteck, Dreieck, Halbkreis) → „Figur in Teilflächen zerlegen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „in bekannte Teilflächen (Rechteck, Halbkreise, Dreiecke) zerlegen und diese benennen“; 2017-OS-K3a.
- 5.2 Fläche als Summe → „Flächeninhalt zusammengesetzter Figur berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „als Summe der Teilflächen“; 2017-OS-K3b (10 · 5 + π · 2,5²).
- 5.3 Fläche durch Ergänzen (Rechteck minus Ecke) → „Restfläche berechnen“ · „Term zu Figur angeben“ – P10-Jahrgänge 6 (Haupt 6). Grund: Ergänzen ist die Differenz zweier Flächen (Definition „Differenz der Flächeninhalte zweier Figuren“); 2023-GYM-B2a berechnet das Fünfeck als Rechteck minus Dreieck.
- 5.4 Restfläche (Rechteck minus Kreis oder Quadrat) → „Restfläche berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Differenz der Flächeninhalte zweier Figuren (Rechteck minus Kreis)“; 2018-OS-K6a.
- 5.5 Umfang einer zusammengesetzten Figur → „Term zu Figur angeben“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2014-OS-B1g: Umfang des Kreuzes aus Quadraten als Term (u = 16a, Fehlerquelle Kanten falsch gezählt).
- 5.6 Sachaufgabe mit Entscheidung (reicht die Platte?) → „Rechteckseite aus Fläche berechnen“ · „Restfläche berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2014-OS-K5d fragt genau, ob die Platte reicht (Nebentyp „Behauptung prüfen“); 2019-GYM-K4c entscheidet, ob die Farbe für Wand minus Fenster reicht.
- 5.7 Verschnitt in Prozent (Vorrat, Niveau III) → „Verschnitt in Prozent berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „den Abfall als Prozentsatz der Ausgangsfläche berechnen“; 2023-OS-K5c.
- 5.8 Fehler finden (Teilfläche doppelt oder vergessen; Kreisfläche addiert statt abgezogen) → kein P10-Typ
- 5.9 Begründen (Zerlegung erklären) → kein P10-Typ

### kreis

themen.csv: kein msa-Thema – Vermerk: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“.

**Einheit 1 · Kreisumfang** – P10-Jahrgänge 5 von 13 (davon Haupt 2); P10-Typen 2; Summe ertrag 4.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Kreisfläche berechnen | 4 | 2 | 5 | 2016 | 2024 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |
| Kreisumfang berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Radius, Durchmesser, Mittelpunkt in einer Figur benennen und einzeichnen → kein P10-Typ
- 1.2 Kreis mit gegebenem Radius oder Durchmesser zeichnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Draufsicht maßstabsgerecht zeichnen“. Grund: 2021-OS-K4c: die Tonne als Kreis mit d = 5,8 cm (Maßstab 1 : 10) in die Draufsicht zeichnen.
- 1.3 d = 2 · r und r = d : 2 → „Kreisfläche berechnen“ – P10-Jahrgänge 5 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Volumen Kugel berechnen“ · „Mantellinie Kegel bestimmen“ · „Verpackungsmaße aus Körpermaßen bestimmen“ · „Draufsicht maßstabsgerecht zeichnen“. Grund: r = d : 2 in 2016-OS-K3b, 2016-OS-K3c und 2018-OS-K6d (Voraussetzung „Radius aus Durchmesser“), d = 2 · r in 2024-OS-K4b (Voraussetzung „Durchmesser = 2r“) und 2021-OS-K4c (Kreis d = 58 cm aus r = 29 cm), jeweils mit der Fehlerquelle Radius und Durchmesser vertauscht.
- 1.4 Umfang messen und u : d bilden (Entdeckung von π) → kein P10-Typ
- 1.5 u aus r → „Kreisumfang berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Mantelfläche Zylinder als Netz skizzieren“ · „Netz eines Zylinders erkennen“. Grund: Länge des Mantelrechtecks als 2 · π · r in 2023-OS-K5a (r = 4 cm) und 2022-OS-K2a (r = 3,2 cm); GYM-Definition „aus dem Durchmesser oder Radius“ (2014-GYM-B1a).
- 1.6 u aus d → „Kreisumfang berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Mantelfläche Zylinder berechnen“. Grund: 2014-GYM-B1a (U = π · 15) und 2018-OS-K6b (M = π · d · h, Definition „als Umfang mal Höhe“).
- 1.7 d oder r aus u (Umstellen) → kein P10-Typ
- 1.8 Umfang mit Dezimalzahlen, auf eine Stelle runden → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Mantelfläche Zylinder als Netz skizzieren“ · „Netz eines Zylinders erkennen“. Grund: 2023-OS-K5a (a ≈ 25,1 cm) und 2022-OS-K2a (Länge ≈ 20,1 cm) runden den Umfang auf eine Stelle.
- 1.9 Halbkreisbogen (mit und ohne Durchmesser) → kein P10-Typ
- 1.10 Sachaufgabe (Rad: Weg bei mehreren Umdrehungen; Baumstamm; Reifen) → „Kreisumfang berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: Kontextvariante des Umfangs aus d: 2014-GYM-B1a (Umfang einer Uhr mit d = 15 cm).
- 1.11 Fehler finden (Durchmesser als Radius; π · r² für den Umfang) → kein P10-Typ
- 1.12 Begründen (warum u : d bei jedem Kreis gleich ist) → kein P10-Typ

**Einheit 2 · Kreisfläche** – P10-Jahrgänge 9 von 13 (davon Haupt 7); P10-Typen 4; Summe ertrag 12.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Kreisfläche berechnen | 4 | 2 | 5 | 2016 | 2024 | 0 | 2 |  |
| Kreisringmaß aus Fläche berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Flächeninhalt zusammengesetzter Figur berechnen | 3 | 1 | 1 | 2017 | 2017 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Term zu Figur angeben | 5 | 5 | 5 | 2014 | 2025 | 5 | 0 | nicht in der Zuordnungszeile der Einheit |

- 2.1 A aus r → „Kreisfläche berechnen“ – P10-Jahrgänge 5 (Haupt 2). Grund: Definition „Flächeninhalt eines Kreises aus dem Radius“; 2024-OS-K4a (r = 30 cm).
- 2.2 A aus d (erst halbieren) → „Kreisfläche berechnen“ – P10-Jahrgänge 5 (Haupt 2). Grund: 2016-OS-K3b (d = 2,14 m, π · 1,07²); als Nebentyp in 2018-OS-K6a (d = 6,4 m) und 2017-OS-K3b (d = 5 m), jeweils Fehlerquelle Durchmesser als Radius.
- 2.3 A mit Dezimalzahlen, runden → „Kreisfläche berechnen“ – P10-Jahrgänge 5 (Haupt 2). Grund: 2016-OS-K3b (≈ 3,60 m²) und 2024-OS-K4a (≈ 2827,4 cm²).
- 2.4 Tabelle r, d, u, A ergänzen → kein P10-Typ
- 2.5 r aus A (Wurzel) → „Kreisringmaß aus Fläche berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Radius eines Zylinders aus Volumen berechnen“. Grund: Teilschritt: den Radius aus π · r² über die Wurzel in 2022-OS-K2d (r = √(425 : (π · 7))) und 2023-GYM-K4b (r = √(R² − A : π)).
- 2.6 Halbkreis- und Viertelkreisfläche → „Flächeninhalt zusammengesetzter Figur berechnen“ · „Kreisfläche berechnen“ – P10-Jahrgänge 5 (Haupt 3). Grund: Zwei Halbkreise in 2017-OS-K3b (Fehlerquelle nur einen addiert); Halbkreisfläche 0,5 · π · 154² in 2014-GYM-K5a (Haupttyp „Kreisfläche berechnen“).
- 2.7 Term zu Figur (Viertelkreis: 1/4 · π · r²) → „Term zu Figur angeben“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „Zu einer beschrifteten Figur … den Term für Flächeninhalt oder Umfang angeben“ ohne Einschränkung der Figur; kein Original mit Kreisteil.
- 2.8 Sachaufgabe (Abwurfring, Pizza, Deckel, Grundfläche eines Kegels oder Zylinders) → „Kreisfläche berechnen“ – P10-Jahrgänge 5 (Haupt 2). Grund: 2016-OS-K3b (Abwurfring) und 2024-OS-K4a (Grundfläche eines Kegels); Deckel als Nebenleistung in 2023-OS-K5c.
- 2.9 Fläche oder Umfang: die passende Formel wählen → „Kreisfläche berechnen“ – P10-Jahrgänge 5 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Mantelfläche Zylinder als Netz skizzieren“ · „Netz eines Zylinders erkennen“. Grund: Die Verwechslung ist Fehlerquelle in 2024-OS-K4a (2πr statt πr²), 2023-OS-K5a (a = πr²) und 2022-OS-K2a (Länge = πr²).
- 2.10 Fehler finden (d in die Formel; 2 · π · r als Fläche; r² als 2 · r) → kein P10-Typ
- 2.11 Begründen (Tortenstücke aneinandergelegt ergeben ungefähr ein Rechteck mit den Seiten u/2 und r) → kein P10-Typ

**Einheit 3 · Kreisteile** – P10-Jahrgänge 2 von 13 (davon Haupt 2); P10-Typen 3; Summe ertrag 5.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Kreissektor Anteil berechnen | 2 | 1 | 1 | 2025 | 2025 | 1 | 0 |  |
| Kreisringmaß aus Fläche berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Restfläche berechnen | 3 | 1 | 1 | 2018 | 2018 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 3.1 Anteil aus dem Mittelpunktswinkel als Bruch (90° → 1/4) und als Prozent → „Kreissektor Anteil berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Bruchteil einer Fläche bestimmen“ · „Prozentsatz berechnen“. Grund: Definition „Anteil eines Kreissektors an der Kreisfläche aus dem Mittelpunktswinkel“ (2025-OS-B1e, 145 : 360, Nebentyp „Prozentsatz berechnen“); als Bruch an Sektoren in 2019-OS-B1c (3/12) und 2026-FOR-B1b (120° = 1/3).
- 3.2 Winkel aus dem Anteil (1/3 → 120°) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Mittelpunktswinkel berechnen“ · „Kreisdiagramm zeichnen“. Grund: Definitionen „Mittelpunktswinkel eines Anteils … aus Teil und Ganzem“ (2022-OS-K4d: 0,16 · 360° = 57,6°) und „Anteil in Prozent in den Mittelpunktswinkel umrechnen“ (2017-OS-K2c).
- 3.3 Bogenlänge b = α/360° · 2 · π · r → kein P10-Typ
- 3.4 Ausschnittsfläche A = α/360° · π · r² → kein P10-Typ
- 3.5 Umfang des Ausschnitts (Bogen plus zwei Radien) → kein P10-Typ
- 3.6 Kreisring (großer Kreis minus kleiner Kreis) → „Kreisringmaß aus Fläche berechnen“ · „Restfläche berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: GYM-Typ mit der Ringformel A = π · (R² − r²) (2023-GYM-K4b); die Differenz zweier Kreisflächen ist ein Fall der Definition „Differenz der Flächeninhalte zweier Figuren“.
- 3.7 Sachaufgabe (Rasensprenger, Tortenstück, Sektor im Kreisdiagramm) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Mittelpunktswinkel berechnen“ · „Kreisdiagramm zeichnen“ · „Sektor im Kreisdiagramm zuordnen“. Grund: Kontext „Sektor im Kreisdiagramm“: 2015-OS-K7c (≈ 52°), 2017-OS-K2c (Sektor mit 40° einzeichnen), 2022-OS-K4d und 2024-OS-K2c (Sektoren nach Größe zuordnen).
- 3.8 Fehler finden (mit dem Restwinkel gerechnet; α : 180; Umfang ohne die Radien) → kein P10-Typ
- 3.9 Begründen (warum der Halbkreis zu 180° gehört) → kein P10-Typ

### koerper

themen.csv: „Volumen und Oberfläche“, „Körper, Netze, Schrägbilder“ – Vermerk: „enthält Kegel/Pyramide; pyramide-kegel-kugel hat kein msa-Thema“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Mantelfläche Kegel berechnen“; „Volumen Kegel berechnen“; „Volumen Kugel berechnen“; „Kugeloberfläche berechnen“; „Mantelfläche einer Pyramide berechnen“; „Maße aus Netz im Maßstab ablesen“; „Kugeldurchmesser aus Anordnung bestimmen“; „Kugelmaß aus Oberfläche berechnen“.

**Einheit 1 · Körper erkennen, Netze, Schrägbilder** – P10-Jahrgänge 8 von 13 (davon Haupt 8); P10-Typen 8; Summe ertrag 18.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Körper aus Netz oder Schrägbild benennen | 2 | 2 | 2 | 2017 | 2018 | 2 | 0 |  |
| Kantenzahl eines Körpers angeben | 1 | 1 | 1 | 2019 | 2019 | 1 | 0 |  |
| Gegenfläche im Würfelnetz bestimmen | 1 | 1 | 1 | 2016 | 2016 | 1 | 0 |  |
| Körperskizze beschriften | 2 | 1 | 1 | 2015 | 2015 | 0 | 1 |  |
| Körper in Schrägbild skizzieren | 4 | 1 | 1 | 2024 | 2024 | 0 | 1 |  |
| Grundfläche im Netz kennzeichnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Netz eines Prismas vervollständigen | 8 | 3 | 3 | 2014 | 2020 | 0 | 3 | nicht in der Zuordnungszeile der Einheit |
| Körper im Schrägbild darstellen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Körper in der Umwelt, aus Schrägbild oder Netz benennen (Prisma, Pyramide, Quader – Ankreuzen) → „Körper aus Netz oder Schrägbild benennen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „Zu einem gezeichneten Netz oder Schrägbild den Körper (Prisma, Pyramide, Quader) benennen oder auswählen“; 2017-OS-B1c, 2018-OS-B1i.
- 1.2 Grund- und Deckfläche, Seitenflächen benennen (auch beim liegenden Prisma) → „Körper aus Netz oder Schrägbild benennen“ · „Grundfläche im Netz kennzeichnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2017-OS-B1c erkennt das liegende Prisma an zwei kongruenten Dreiecken als Grund- und Deckfläche (Fehlerquelle Dreiecke als Seitenflächen); GYM-Definition „eine Fläche markieren, die als Grundfläche des Prismas dienen kann“ (2020-GYM-K5a).
- 1.3 Ecken, Kanten, Flächen zählen (Quader, Dreiecksprisma, quadratische Pyramide) → „Kantenzahl eines Körpers angeben“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Anzahl der Kanten, Ecken oder Flächen eines benannten Körpers“; 2019-OS-B1f (quadratische Pyramide, 8 Kanten).
- 1.4 Würfelnetz: gültig oder nicht → kein P10-Typ
- 1.5 Gegenfläche im Würfelnetz markieren → „Gegenfläche im Würfelnetz bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „In einem Würfelnetz die Fläche markieren, die beim Falten einer markierten Fläche gegenüberliegt“; 2016-OS-B1j.
- 1.6 Netz von Quader oder Würfel mit Maßen zeichnen → „Netz eines Prismas vervollständigen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Grundfall: der Quader ist das Prisma mit Rechteckgrundfläche; 2014-OS-K5b ergänzt Rechtecke mit Maßen (57 × 165, 110 × 165).
- 1.7 Schrägbild lesen: verdeckte Kanten, Maße entnehmen → „Körper aus Netz oder Schrägbild benennen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2017-OS-B1c: den Körper aus einem Schrägbild mit gestrichelten verdeckten Kanten erkennen.
- 1.8 Schrägbild eines Quaders auf Rasterpapier zeichnen (Tiefe halb, schräg) → „Körper im Schrägbild darstellen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Typ: 2019-GYM-K4a (Quader mit Pyramide) und 2025-GYM-K5b (Tiefenachse unter 45° mit q = 0,5).
- 1.9 Schrägbild beschriften, Körperhöhe einzeichnen → „Körperskizze beschriften“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „eine Strecke (Körperhöhe) einzeichnen und die Skizze mit gegebenen Maßen beschriften“; 2015-OS-K6b.
- 1.10 Körper in ein Schrägbild einzeichnen (Kegel im Quader) → „Körper in Schrägbild skizzieren“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Einen Körper in ein vorgegebenes Schrägbild (z. B. in einen Quader) einzeichnen“; 2024-OS-K4b.
- 1.11 Fehler finden (Dreiecksprisma als Pyramide; angrenzende statt gegenüberliegende Fläche) → kein P10-Typ
- 1.12 Begründen (warum ein Netz nicht zum Würfel faltet) → kein P10-Typ

**Einheit 2 · Quader und Würfel** – P10-Jahrgänge 7 von 13 (davon Haupt 5); P10-Typen 6; Summe ertrag 17.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Volumen Würfel berechnen | 2 | 1 | 1 | 2026 | 2026 | 2 | 0 |  |
| Volumen Prisma berechnen | 2 | 1 | 2 | 2014 | 2019 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Volumen Zylinder berechnen | 10 | 4 | 5 | 2021 | 2026 | 0 | 5 | nicht in der Zuordnungszeile der Einheit |
| Höhe eines Zylinders aus Volumen berechnen | 3 | 1 | 1 | 2023 | 2023 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Grundkante aus Volumen berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Volumen zusammengesetzter Körper berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 2.1 V = a · b · c mit ganzen Zahlen → „Volumen Würfel berechnen“ · „Volumen Prisma berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Der Würfel ist der Fall a = b = c (2026-FOR-B1f, Fehlerquelle 3 · 3 = 9), der Quader das Prisma mit Rechteckgrundfläche (Definition „Volumen eines geraden Prismas als Grundfläche mal Höhe“).
- 2.2 Würfel a³ → „Volumen Würfel berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Volumen eines Würfels aus der Kantenlänge“; 2026-FOR-B1f (3 · 3 · 3 = 27 cm³).
- 2.3 Einheiten cm³, dm³ = l, m³ (1 l = 1000 cm³) → „Volumen Zylinder berechnen“ · „Höhe eines Zylinders aus Volumen berechnen“ – P10-Jahrgänge 5 (Haupt 4). Grund: 2021-OS-K4a (cm³ in Liter, Fehlerquelle Faktor 100) und 2023-OS-K5d (1 l als 1000 cm³, Fehlerquelle 100 cm³).
- 2.4 Oberfläche als sechs Rechtecke, Würfel 6 · a² → kein P10-Typ
- 2.5 Oberfläche ohne Deckel (Kiste, Aquarium) → kein P10-Typ
- 2.6 Kante aus V und zwei Kanten → „Grundkante aus Volumen berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Typ: 2017-GYM-K4c stellt die Quaderformel nach der Kante um (a² = 500 : 8, dann Wurzel).
- 2.7 Würfelkante aus V (Kubikzahlen) → kein P10-Typ
- 2.8 aus zwei Quadern zusammengesetzt (Treppe, L-Form) → „Volumen zusammengesetzter Körper berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: Grundfall der GYM-Definition „Volumen eines aus mehreren Körpern … zusammengesetzten Werkstücks“ (2016-GYM-K3b).
- 2.9 Aquarium: Füllmenge in Litern, Füllhöhe → kein P10-Typ
- 2.10 Fehler finden (a · b · c als Oberfläche; 3 · 3 statt 3 · 3 · 3; Oberfläche als Volumen angegeben) → kein P10-Typ
- 2.11 Begründen (Schichten aus Einheitswürfeln) → kein P10-Typ

**Einheit 3 · Prisma** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 4; Summe ertrag 12.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Volumen Prisma berechnen | 2 | 1 | 2 | 2014 | 2019 | 0 | 1 |  |
| Mantelfläche Prisma berechnen | 2 | 1 | 1 | 2019 | 2019 | 0 | 1 |  |
| Netz eines Prismas vervollständigen | 8 | 3 | 3 | 2014 | 2020 | 0 | 3 |  |
| Grundfläche im Netz kennzeichnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 3.1 Grundfläche erkennen und markieren (auch liegend) → „Volumen Prisma berechnen“ · „Grundfläche im Netz kennzeichnen“ – P10-Jahrgänge 2 (Haupt 1). Grund: Teilschritt von „Grundfläche mal Höhe“ (2019-OS-K4c: die dreieckige Deckfläche als G); GYM-Definition „eine Fläche markieren, die als Grundfläche des Prismas dienen kann“ (2020-GYM-K5a).
- 3.2 V = G · h mit gegebener Grundfläche → „Volumen Prisma berechnen“ – P10-Jahrgänge 2 (Haupt 1). Grund: Definition „Volumen eines geraden Prismas als Grundfläche mal Höhe“; 2014-OS-K5a (gegebene Trapezfläche 5 225 cm² · 165 cm).
- 3.3 Rechteckgrundfläche (Quader als Prisma) → „Volumen Prisma berechnen“ – P10-Jahrgänge 2 (Haupt 1). Grund: Grundfall der Definition „Volumen eines geraden Prismas als Grundfläche mal Höhe“ mit rechteckiger Grundfläche.
- 3.4 Dreiecksgrundfläche (G = g · h_g : 2) → „Volumen Prisma berechnen“ – P10-Jahrgänge 2 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt Dreieck berechnen“. Grund: 2019-OS-K4c: Deckfläche ½ · 1,5 · 1,3 (Haupttyp „Flächeninhalt Dreieck berechnen“), dann V = A · 1,2 (Nebentyp „Volumen Prisma berechnen“).
- 3.5 Trapezgrundfläche → „Volumen Prisma berechnen“ – P10-Jahrgänge 2 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt Trapez berechnen“. Grund: 2014-OS-K5a (gegebene Trapezfläche mal Prismenhöhe); 2018-GYM-K3c sowie 2025-GYM-K5a und 2025-GYM-K5c berechnen die Trapezfläche und daraus das Volumen.
- 3.6 Mantel als Rechtecke (Umfang der Grundfläche · h) → „Mantelfläche Prisma berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Gesamtfläche der rechteckigen Seitenflächen eines geraden Prismas“; 2019-OS-K4b (3 · 1,5 · 1,2).
- 3.7 Oberfläche = 2 · G + M → kein P10-Typ
- 3.8 Netz eines Prismas vervollständigen (fehlende Rechtecke, Maße) → „Netz eines Prismas vervollständigen“ – P10-Jahrgänge 3 (Haupt 3). (wortgleich)
- 3.9 Höhe aus V und G → kein P10-Typ
- 3.10 Sachaufgabe (Dach, Vitrine, Werbeprisma, Zelt, Schokoladenverpackung) → „Volumen Prisma berechnen“ · „Mantelfläche Prisma berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Werbeprisma in 2019-OS-K4c (Volumen) und 2019-OS-K4b (Werbefläche), Kühlvitrine in 2014-OS-K5a.
- 3.11 Fehler finden (Höhe der Grundfläche und Prismenhöhe vertauscht; Faktor 1/2 beim Dreieck vergessen; nur eine Seitenfläche) → kein P10-Typ
- 3.12 Begründen (warum Grundfläche mal Höhe) → kein P10-Typ

**Einheit 4 · Zylinder** – P10-Jahrgänge 6 von 13 (davon Haupt 5); P10-Typen 8; Summe ertrag 29.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Volumen Zylinder berechnen | 10 | 4 | 5 | 2021 | 2026 | 0 | 5 |  |
| Mantelfläche Zylinder berechnen | 2 | 1 | 1 | 2018 | 2018 | 0 | 1 |  |
| Mantelfläche Zylinder als Netz skizzieren | 3 | 1 | 2 | 2022 | 2023 | 0 | 1 |  |
| Netz eines Zylinders erkennen | 3 | 1 | 1 | 2022 | 2022 | 0 | 1 |  |
| Höhe eines Zylinders aus Volumen berechnen | 3 | 1 | 1 | 2023 | 2023 | 0 | 1 |  |
| Radius eines Zylinders aus Volumen berechnen | 3 | 1 | 1 | 2022 | 2022 | 0 | 1 |  |
| Volumenänderung bei doppeltem Radius begründen | 2 | 1 | 1 | 2021 | 2021 | 0 | 1 |  |
| Volumen Kegel und Zylinder vergleichen | 3 | 1 | 1 | 2026 | 2026 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 4.1 V = π · r² · h → „Volumen Zylinder berechnen“ – P10-Jahrgänge 5 (Haupt 4). Grund: Definition „Volumen eines Zylinders aus Radius und Höhe“; 2026-FOR-K2a (Fehlerquelle r² als 2r), 2021-OS-K4a, 2022-OS-K2b, 2023-OS-K5b.
- 4.2 r aus d → „Volumen Zylinder berechnen“ · „Höhe eines Zylinders aus Volumen berechnen“ – P10-Jahrgänge 5 (Haupt 4). Grund: Radius aus dem Durchmesser in 2023-GYM-K4a (d = 57 cm), 2017-GYM-K4a und 2019-GYM-K3c; Fehlerquelle Durchmesser statt Radius in 2026-FOR-K2a und 2021-OS-K4a.
- 4.3 Liter (cm³ → dm³) → „Volumen Zylinder berechnen“ – P10-Jahrgänge 5 (Haupt 4). Grund: 2021-OS-K4a: 250 998 cm³ ≈ 251 dm³ = 251 l (Fehlerquelle Faktor 100 statt 1000).
- 4.4 Mantel M = 2 · π · r · h (Umfang mal Höhe) → „Mantelfläche Zylinder berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Mantelfläche eines Zylinders als Umfang mal Höhe (M = π · d · h)“; 2018-OS-K6b (Fehlerquelle Grund- und Deckfläche mitgerechnet).
- 4.5 Netz: Rechtecklänge gleich Umfang → „Netz eines Zylinders erkennen“ · „Mantelfläche Zylinder als Netz skizzieren“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2022-OS-K2a (die Rechtecklänge muss dem Umfang 2πr entsprechen) und 2023-OS-K5a (a = 2πr, b = h).
- 4.6 Oberfläche O = 2 · π · r² + M, ohne Deckel nur eine Grundfläche → kein P10-Typ
- 4.7 h aus V → „Höhe eines Zylinders aus Volumen berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Höhe eines Zylinders aus Volumen und Radius durch Umstellen der Volumenformel“; 2023-OS-K5d.
- 4.8 r aus V (Wurzel) → „Radius eines Zylinders aus Volumen berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „durch Umstellen der Volumenformel und Wurzelziehen“; 2022-OS-K2d.
- 4.9 Behauptung prüfen (Herstellerangabe „ca. 400 ml“) → „Volumen Zylinder berechnen“ – P10-Jahrgänge 5 (Haupt 4). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2023-OS-K5b weist die Herstellerangabe „ca. 400 ml“ nach, 2022-OS-K2b die Angabe „200 ml passen hinein“ (beide Nebentyp „Behauptung prüfen“).
- 4.10 Volumen bei doppeltem Radius (vierfach) → „Volumenänderung bei doppeltem Radius begründen“ · „Volumen Kegel und Zylinder vergleichen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2021-OS-K4b (doppelter Radius, rechnerisch π · 58² · 95 ≈ 1004 l); dieselbe Wirkung des vervielfachten Radius in 2026-FOR-K2d (Definition „Volumenformeln von Körpern mit Variablen vergleichen“).
- 4.11 Sachaufgabe (Dose, Regentonne, Turm, Becher, Rohr) → „Volumen Zylinder berechnen“ · „Mantelfläche Zylinder berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: Dose 2023-OS-K5b, Regentonne 2021-OS-K4a, Becher 2022-OS-K2b, Turm 2026-FOR-K2a und Außenmauer des Turms 2018-OS-K6b.
- 4.12 Fehler finden (d statt r; 2 · π · r · h als Volumen; Grund- und Deckfläche beim Mantel mitgerechnet) → kein P10-Typ
- 4.13 Begründen (warum vierfach) → „Volumenänderung bei doppeltem Radius begründen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Der P10-Typ verlangt genau diese Begründung: Definition „Begründen, wie sich das Volumen eines Zylinders (Kegels) ändert, wenn der Radius vervielfacht wird“; 2021-OS-K4b.

**Einheit 5 · Zusammengesetzte Körper und Anwendungen** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 5; Summe ertrag 8.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Term zu Körper angeben | 3 | 1 | 1 | 2017 | 2017 | 0 | 1 |  |
| Restvolumen berechnen | 3 | 1 | 1 | 2024 | 2024 | 0 | 1 |  |
| Verpackungsmaße aus Körpermaßen bestimmen | 0 | 0 | 1 | 2024 | 2024 | 0 | 0 |  |
| Packungsanzahl in Quader bestimmen | 2 | 1 | 1 | 2020 | 2020 | 0 | 1 |  |
| Volumen zusammengesetzter Körper berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 5.1 Körper in Teilkörper zerlegen und benennen (Haus = Quader + Dreiecksprisma; Pool = Quader + Halbzylinder) → „Term zu Körper angeben“ · „Volumen zusammengesetzter Körper berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Teilschritt: 2017-OS-K3c (Pool, Grundfläche a · b + π · (a/2)²) und 2016-GYM-K3b (Werkstück aus Zylinder, Kegel und Halbkugel).
- 5.2 Term zum Volumen aufstellen oder vorgegebene Terme prüfen (Klammer) → „Term zu Körper angeben“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „den Term für das Volumen angeben … oder vorgegebene Terme daraufhin prüfen, ob sie das Volumen richtig beschreiben (Grundfläche mal Höhe, Klammerung)“; 2017-OS-K3c.
- 5.3 Volumen zusammengesetzter Körper → „Volumen zusammengesetzter Körper berechnen“ · „Term zu Körper angeben“ – P10-Jahrgänge 1 (Haupt 1). Grund: GYM-Definition „Volumen eines aus mehreren Körpern … zusammengesetzten Werkstücks berechnen“ (2016-GYM-K3b); 2017-OS-K3c verlangt das Volumen des Pools als Term.
- 5.4 Restvolumen (Verpackung minus Inhalt) → „Restvolumen berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Differenz der Volumen zweier Körper (Verpackung minus Inhalt)“; 2024-OS-K4c.
- 5.5 kleinste Quaderverpackung aus Körpermaßen (Durchmesser, nicht Radius) → „Verpackungsmaße aus Körpermaßen bestimmen“ – P10-Jahrgänge 1 (Haupt 0). Grund: Definition „Kleinste Quaderverpackung aus Durchmesser und Höhe eines Körpers auswählen und begründen“; 2024-OS-K4b (Nebentyp).
- 5.6 Packungsanzahl in einer Kiste durch Anordnen → „Packungsanzahl in Quader bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Größtmögliche Anzahl gleicher Körper in einer quaderförmigen Kiste durch Anordnen“; 2020-OS-K5c.
- 5.7 Masse aus Volumen und Dichte (1 m³ Wasser = 1000 kg) → „Volumen zusammengesetzter Körper berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Masse aus Volumen und Dichte berechnen“. Grund: 2019-OS-K4c (1 m³ Wasser = 1 000 kg, Nebentyp) und GYM-Definition „daraus über die Dichte die Masse bestimmen“ (2016-GYM-K3b).
- 5.8 Füllstand in Prozent → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Masse aus Volumen und Dichte berechnen“. Grund: Definition „ggf. mit Füllgrad in Prozent“; 2019-OS-K4c (zu 10 % gefüllt).
- 5.9 Oberfläche eines zusammengesetzten Körpers (Vorrat) → kein P10-Typ
- 5.10 Fehler finden (Klammer fehlt, h wirkt nur auf einen Teil; Radius als Mindestbreite) → „Term zu Körper angeben“ · „Verpackungsmaße aus Körpermaßen bestimmen“ – P10-Jahrgänge 2 (Haupt 1). Grund: Beide Fehler sind die verlangte Leistung: 2017-OS-K3c lässt vorgegebene Terme prüfen (zweite Formel ohne Klammer), 2024-OS-K4b begründen, warum 31 cm schmaler als der Durchmesser 60 cm sind.
- 5.11 Begründen (Zerlegung erklären; warum Volumen teilen nicht reicht) → „Packungsanzahl in Quader bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „durch Anordnen (nicht nur Volumendivision) bestimmen und erläutern“; 2020-OS-K5c (Fehlerquelle nur Volumen teilen, 8,4).

### pyramide-kegel-kugel

themen.csv: kein msa-Thema – Vermerk: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“.

**Einheit 1 · Pyramide** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 1; Summe ertrag 0.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Mantelfläche einer Pyramide berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Teile der Pyramide im Schrägbild benennen (Grundfläche, Seitenflächen, Höhe h, Seitenhöhe h_s, Seitenkante; Kantenzahl → koerper.md Einheit 1) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Körperskizze beschriften“. Grund: 2015-OS-K6b: die Höhe der Pyramide von der Spitze zum Diagonalenschnittpunkt einzeichnen (Fehlerquelle Seitenkante oder Höhe einer Seitenfläche).
- 1.2 V = 1/3 · G · h mit gegebener Grundfläche → kein P10-Typ
- 1.3 quadratische Grundfläche a² → kein P10-Typ
- 1.4 rechteckige Grundfläche a · b → kein P10-Typ
- 1.5 Seitenhöhe aus h und a/2 (Stützdreieck, Pythagoras) → „Mantelfläche einer Pyramide berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Pythagoras Hypotenuse“. Grund: 2015-OS-K6c: h_s = √(0,68² + 0,40²) als Nebentyp „Pythagoras Hypotenuse“ (Voraussetzung „Höhe der Seitenfläche über rechtwinkliges Dreieck aus h und a/2“); GYM-Definition „über den Satz des Pythagoras ermittelten Seitenhöhe“ (2019-GYM-K4b).
- 1.6 Flächeninhalt einer Seitenfläche (Dreieck mit h_s) → „Mantelfläche einer Pyramide berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt Dreieck berechnen“. Grund: 2015-OS-K6c: A = ½ · 0,80 · 0,789 ≈ 0,32 m² (Fehlerquelle Pyramidenhöhe als Dreieckshöhe); Teilschritt der Mantelfläche in 2019-GYM-K4b.
- 1.7 Mantel M = 4 · a · h_s : 2 → „Mantelfläche einer Pyramide berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Definition „Mantelfläche einer quadratischen Pyramide aus der Grundkante und der über den Satz des Pythagoras ermittelten Seitenhöhe“; 2019-GYM-K4b (4 · 0,5 · 4 · h_s).
- 1.8 Oberfläche O = a² + M → kein P10-Typ
- 1.9 Netz der quadratischen Pyramide mit Maßen zeichnen oder vervollständigen (Netz der Pyramide mit rechteckiger Grundfläche: GYM) → kein P10-Typ
- 1.10 Schrägbild zeichnen, Höhe einzeichnen und beschriften → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Körperskizze beschriften“ · „Körper im Schrägbild darstellen“. Grund: 2015-OS-K6b (Höhe einzeichnen und beschriften) und 2019-GYM-K4a (Turm aus Quader und Pyramide als Schrägbild zeichnen).
- 1.11 Seitenkante aus h und der halben Diagonale der Grundfläche (Stützdreieck) → kein P10-Typ
- 1.12 h aus V und G (**GYM**) → kein P10-Typ
- 1.13 Sachaufgabe (Zeltdach: Stoff; Glaspyramide: Volumen und Glasfläche; Kirchturmspitze; Modell im Maßstab) → „Mantelfläche einer Pyramide berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt Dreieck berechnen“ · „Länge im Maßstab umrechnen“. Grund: Modellpyramide in 2015-OS-K6c (Sperrholz für eine Seitenfläche) und 2015-OS-K6a (Maßstab 1 : 10); Turmdach in 2019-GYM-K4b (Mantelfläche).
- 1.14 Fehler finden (Faktor 1/3 vergessen; Pyramidenhöhe als Höhe der Seitenfläche; a statt a/2 im Stützdreieck; nur eine Seitenfläche) → kein P10-Typ
- 1.15 Begründen (warum ein Drittel: drei gleiche Pyramiden füllen das Prisma mit derselben Grundfläche und Höhe) → kein P10-Typ

**Einheit 2 · Kegel** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 5; Summe ertrag 14.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Volumen Kegel berechnen | 0 | 0 | 1 | 2024 | 2024 | 0 | 0 |  |
| Mantelfläche Kegel berechnen | 6 | 1 | 1 | 2026 | 2026 | 0 | 2 |  |
| Volumen Kegel und Zylinder vergleichen | 3 | 1 | 1 | 2026 | 2026 | 0 | 1 |  |
| Restvolumen berechnen | 3 | 1 | 1 | 2024 | 2024 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Volumenänderung bei doppeltem Radius begründen | 2 | 1 | 1 | 2021 | 2021 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 2.1 Radius, Höhe, Mantellinie im Bild benennen (welche Strecke steht senkrecht) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Mantellinie Kegel bestimmen“ · „Pythagoras Kathete“. Grund: Voraussetzung „rechtwinkliges Dreieck im Kegel erkennen“ in 2018-OS-K6d und 2026-FOR-K2c (Fehlerquelle s als Kegelhöhe).
- 2.2 V = 1/3 · π · r² · h → „Volumen Kegel berechnen“ – P10-Jahrgänge 1 (Haupt 0). Grund: Definition „Volumen eines Kegels aus Radius und Höhe berechnen“; 2024-OS-K4c (Nebentyp, Fehlerquelle Faktor 1/3 vergessen).
- 2.3 r aus d → „Volumen Kegel berechnen“ – P10-Jahrgänge 1 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Mantellinie Kegel bestimmen“. Grund: 2021-GYM-K5a (V = 1/3 · π · (d/2)² · t, Nebentyp „Volumen Kegel berechnen“) und 2018-OS-K6d (Radius 3,2 m aus d = 6,4 m als Kathete).
- 2.4 Liter (cm³ → dm³) → „Volumen Kegel berechnen“ – P10-Jahrgänge 1 (Haupt 0). Grund: 2021-GYM-K5a: 393,5 cm³ ≈ 0,39 l (Nebentyp „Volumen Kegel berechnen“).
- 2.5 s aus r und h (Stützdreieck) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Mantellinie Kegel bestimmen“. Grund: Definition „Mantellinie eines Kegels aus Radius und Höhe über den Satz des Pythagoras berechnen“; 2018-OS-K6d.
- 2.6 h aus s und r → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Pythagoras Kathete“ · „Kegelhöhe aus Mantellinie und Radius berechnen“. Grund: 2026-FOR-K2c (Kegelhöhe √(8,6² − 4,7²), Haupttyp „Pythagoras Kathete“); GYM-Definition „Höhe eines Kegels aus der Mantellinie und dem Radius“ (2022-GYM-K4b).
- 2.7 Mantel M = π · r · s → „Mantelfläche Kegel berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Mantelfläche eines Kegels aus Radius und Mantellinie berechnen“; 2026-FOR-K2b (Fehlerquelle Grundfläche mitgerechnet, s als Höhe).
- 2.8 Oberfläche O = π · r² + M → kein P10-Typ
- 2.9 Schrägbild eines Kegels skizzieren (Ellipse, Spitze, Höhe gestrichelt) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Körper in Schrägbild skizzieren“. Grund: 2024-OS-K4b: den Kegel in den Quader skizzieren (Ellipse auf der Bodenfläche, Spitze mittig oben).
- 2.10 Netz des Kegels erkennen und beschriften: Kreis und Kreisausschnitt mit dem Radius s (Sektorwinkel Vorrat) → kein P10-Typ
- 2.11 h aus V und r → kein P10-Typ
- 2.12 Kegeldach auf einem Zylinder: Dachfläche, Materialkosten, Gesamthöhe → „Mantelfläche Kegel berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Kosten aus Menge und Preis berechnen“ · „Pythagoras Kathete“ · „Strecke aus Teilstrecken berechnen“. Grund: Turm 2026: Dachfläche und Ziegelkosten in 2026-FOR-K2b (Nebentyp „Kosten aus Menge und Preis berechnen“), Gesamthöhe 25,0 m plus Kegelhöhe in 2026-FOR-K2c (Nebentyp „Strecke aus Teilstrecken berechnen“).
- 2.13 Kegel in Zylinderverpackung (Restvolumen → koerper.md Einheit 5) → „Restvolumen berechnen“ · „Volumen Kegel berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2024-OS-K4c: Zylinderverpackung minus Kegel (Haupttyp „Restvolumen berechnen“, Nebentyp „Volumen Kegel berechnen“).
- 2.14 Volumen des Kegels gegen den Zylinder mit gleichem r und h (ein Drittel) → „Volumen Kegel und Zylinder vergleichen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Volumenformeln von Körpern mit Variablen vergleichen“; 2026-FOR-K2d rechnet mit V_Kegel = 1/3 · π · r² · h gegen V_Zylinder.
- 2.15 Aussage über den dreifachen Radius rechnerisch prüfen (Niveau III) → „Volumen Kegel und Zylinder vergleichen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2026-FOR-K2d prüft genau diese Aussage (Nebentyp „Behauptung prüfen“, Ergebnis dreifaches Volumen).
- 2.16 Sachaufgabe (Trichter, Eistüte, Verkehrshütchen, Sandhaufen, Sektglas, Zelt) → „Volumen Kegel berechnen“ · „Mantelfläche Kegel berechnen“ – P10-Jahrgänge 2 (Haupt 1). Grund: Kontextvarianten: kegelförmiger Messbecher 2021-GYM-K5a und Halde 2014-GYM-K5c (Volumen), Boje 2022-GYM-K4c (Mantelfläche als Nebentyp).
- 2.17 Fehler finden (Faktor 1/3 vergessen; s als h eingesetzt; Grundfläche beim Dach mitgerechnet; (3r)² als 3r²) → kein P10-Typ
- 2.18 Begründen (drei Kegel füllen den Zylinder; warum das Volumen beim dreifachen Radius neunfach wird) → „Volumen Kegel und Zylinder vergleichen“ · „Volumenänderung bei doppeltem Radius begründen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2026-FOR-K2d verlangt die Begründung über (3r)² = 9r² als Antworttext; Definition „Begründen, wie sich das Volumen eines Zylinders (Kegels) ändert, wenn der Radius vervielfacht wird“.

**Einheit 3 · Kugel** – P10-Jahrgänge 2 von 13 (davon Haupt 2); P10-Typen 6; Summe ertrag 6.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Volumen Kugel berechnen | 3 | 1 | 1 | 2016 | 2016 | 0 | 1 |  |
| Kugeloberfläche berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Volumen zusammengesetzter Körper berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Kugelmaß aus Oberfläche berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Restvolumen berechnen | 3 | 1 | 1 | 2024 | 2024 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Kugeldurchmesser aus Anordnung bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 3.1 Radius und Durchmesser am Bild benennen → kein P10-Typ
- 3.2 V = 4/3 · π · r³ mit r → „Volumen Kugel berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Volumen einer Kugel aus Radius oder Durchmesser mit V = 4/3 · π · r³ berechnen“; 2016-OS-K3c (Fehlerquelle 4/3 vergessen).
- 3.3 aus d → „Volumen Kugel berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „aus Radius oder Durchmesser“; 2016-OS-K3c (d = 12 cm, Fehlerquelle 12 statt 6).
- 3.4 Oberfläche O = 4 · π · r² → „Kugeloberfläche berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Definition „Oberfläche einer Kugel aus Radius oder Durchmesser mit O = 4 · π · r² berechnen“; 2015-GYM-K4c.
- 3.5 Liter und Milliliter → kein P10-Typ
- 3.6 Halbkugel: Volumen halb, Oberfläche halb plus Schnittkreis → „Volumen zusammengesetzter Körper berechnen“ · „Kugelmaß aus Oberfläche berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM: Halbkugelvolumen 2/3 · π · r³ in 2016-GYM-K3b und 2022-GYM-K4d, gewölbte Halbkugelfläche 2 · π · r² in 2022-GYM-K4a.
- 3.7 Masse aus Volumen und Dichte (Stoßkugel, Stahlkugel) → „Volumen zusammengesetzter Körper berechnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Masse aus Volumen und Dichte berechnen“. Grund: Definition „Masse aus Volumen und Masse je Volumeneinheit (Dichte) berechnen“ (2019-OS-K4c); Stahlwerkstück mit Halbkugel über 7,8 g je cm³ in 2016-GYM-K3b.
- 3.8 r aus O (Wurzel) → „Kugelmaß aus Oberfläche berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Definition „Durchmesser oder Radius einer Halbkugel durch Umstellen der Oberflächenformel“; 2022-GYM-K4a (r = √(O : (2π))).
- 3.9 r aus V (Kubikwurzel, Vorrat) → „Volumen zusammengesetzter Körper berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: 2022-GYM-K4d löst π · r³ = 10,6 nach r auf (r = 1,5 m).
- 3.10 Kugel skizzieren (Kreis mit Äquatorellipse, Radius gestrichelt) → kein P10-Typ
- 3.11 Kugel in der Würfelschachtel: Kante gleich Durchmesser, Restvolumen → „Restvolumen berechnen“ · „Kugeldurchmesser aus Anordnung bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Verpackungsmaße aus Körpermaßen bestimmen“. Grund: Mindestmaß gleich Durchmesser in 2024-OS-K4b (Definition „aus Durchmesser und Höhe eines Körpers“), Restvolumen nach Definition „Verpackung minus Inhalt“ (2024-OS-K4c), Kante gleich vier Durchmesser in 2020-GYM-K5d.
- 3.12 Sachaufgabe (Silo oder Turm mit Halbkugeldach, Eiskugel in der Tüte – Kegel plus Halbkugel) → „Volumen zusammengesetzter Körper berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Definition „aus mehreren Körpern (z. B. Zylinder, Kegel, Halbkugel) zusammengesetzt“; Boje aus Halbkugel und Kegel in 2022-GYM-K4d.
- 3.13 Volumen bei doppeltem Radius (achtfach) → kein P10-Typ
- 3.14 Fehler finden (d statt r; r² statt r³; 4/3 vergessen; Oberfläche und Volumen vertauscht) → kein P10-Typ
- 3.15 Begründen (warum achtfach; warum die Oberfläche der Halbkugel mehr als halb so groß ist) → kein P10-Typ

### pythagoras

themen.csv: „Satz des Pythagoras“.

**Einheit 1 · Satz und Hypotenuse** – P10-Jahrgänge 10 von 13 (davon Haupt 9); P10-Typen 4; Summe ertrag 30.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Satz des Pythagoras formulieren | 1 | 1 | 1 | 2022 | 2022 | 1 | 0 |  |
| Pythagoras Gleichung zuordnen | 5 | 4 | 4 | 2017 | 2026 | 5 | 0 |  |
| Pythagoras Hypotenuse | 9 | 3 | 4 | 2015 | 2025 | 0 | 3 |  |
| Pythagoras Kathete | 15 | 5 | 5 | 2016 | 2026 | 0 | 7 | nicht in der Zuordnungszeile der Einheit |

- 1.1 rechten Winkel im Dreieck finden, Hypotenuse und Katheten benennen (Dreieck in verschiedener Lage: rechter Winkel unten links, unten rechts, oben; Hypotenuse waagerecht) → „Pythagoras Gleichung zuordnen“ · „Satz des Pythagoras formulieren“ · „Pythagoras Hypotenuse“ · „Pythagoras Kathete“ – P10-Jahrgänge 10 (Haupt 9). Grund: Teilschritt jeder Pythagoras-Aufgabe: 2017-OS-B1d erkennt die Hypotenuse gegenüber dem rechten Winkel, 2022-OS-B1g hat den Distraktor „Dem rechten Winkel liegt eine Kathete gegenüber“, die falsche Hypotenuse ist Fehlerquelle in 2020-OS-K7a und 2016-OS-K7b.
- 1.2 Satz in Worten: die richtige von drei Aussagen ankreuzen (Kathetenquadrate und Hypotenusenquadrat; P10-Form) → „Satz des Pythagoras formulieren“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „unter mehreren Aussagen die korrekte sprachliche Fassung … auswählen“; Original 2022-OS-B1g mit drei Aussagen.
- 1.3 Gleichung zum beschrifteten Dreieck aufstellen (a² + b² = c², mit x, y, z oder u, v, w nach der Beschriftung) → „Pythagoras Gleichung zuordnen“ · „Pythagoras Hypotenuse“ – P10-Jahrgänge 8 (Haupt 7). Grund: Vorstufe des Auswählens (2017-OS-B1d z² = x² + y², 2026-FOR-B1j mit u, v, w) und erster Schritt der Hypotenusenrechnung (2020-OS-K7a AB² = 12² + 34²).
- 1.4 Gleichung aus vier Optionen ankreuzen (Summe, Differenz, mit und ohne Wurzel; P10-Form) → „Pythagoras Gleichung zuordnen“ – P10-Jahrgänge 4 (Haupt 4). Grund: Definition „die richtige Pythagoras-Gleichung auswählen“; 2021-OS-B1h und 2017-OS-B1d mit vier Optionen aus Summe, Differenz, mit und ohne Wurzel.
- 1.5 Quadrate über den Seiten zeichnen und Flächen vergleichen (Kästchen zählen) → kein P10-Typ
- 1.6 Hypotenuse aus zwei Katheten mit aufgehender Wurzel → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: Grundfall der Definition „Hypotenuse … aus beiden Katheten“; 2020-GYM-B1a rechnet √(6² + 8²) = 10.
- 1.7 mit nicht aufgehender Wurzel: Zwischenergebnis c², Näherungswert gerundet → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2020-OS-K7a: AB² = 1300 als Zwischenergebnis, AB ≈ 36,1 m.
- 1.8 Katheten als Dezimalzahlen → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: Dezimalkatheten in 2022-OS-K2c (7 cm und 6,4 cm) und 2015-OS-K6c (0,68 m und 0,40 m, Nebentyp).
- 1.9 Einheit beim Ergebnis, gemischte Einheiten vorher angleichen → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2019-GYM-K3b rechnet mit Längen in Meter und dem Zuschlag 25 cm; alle Originale verlangen die Einheit im Ergebnis (2020-OS-K7a ≈ 36,1 m).
- 1.10 Diagonale im Rechteck und Quadrat → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2022-OS-K2c: Diagonale im Rechteck 7 cm × 6,4 cm des Becherquerschnitts.
- 1.11 Sachaufgabe mit gegebener Skizze (Rampe, Leiter an der Wand, Abkürzung über die Wiese, Stab in der Kiste) → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: Rampe 2025-OS-K4a, Stab im Becher 2022-OS-K2c, Seil am Pfeiler 2019-GYM-K3b, jeweils mit Skizze.
- 1.12 Überstand oder Zuschlag zum Ergebnis addieren → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: 2022-OS-K2c (plus 2 cm Überstand) und 2019-GYM-K3b (plus 2 · 25 cm Zuschlag); das Addieren ist „Strecke aus Teilstrecken berechnen“ (Definition, Nebentyp in 2026-FOR-K2c).
- 1.13 Ergebnis mit sinnvoller Genauigkeit angeben → „Pythagoras Hypotenuse“ · „Pythagoras Kathete“ – P10-Jahrgänge 8 (Haupt 7). Grund: Die Wurzel geht in der P10 nie auf, verlangt ist ein gerundeter Näherungswert (2020-OS-K7a ≈ 36,1 m, 2019-OS-K3a ≈ 8,1 m).
- 1.14 Fehler finden (Kathete als Hypotenuse angesetzt; Wurzel vergessen; c = a + b; Wurzel aus jedem Summanden einzeln) → kein P10-Typ
- 1.15 Begründen (warum die Hypotenuse die längste Seite ist; warum c = a + b nicht gelten kann – Dreiecksungleichung) → kein P10-Typ

**Einheit 2 · Kathete und Umkehrung** – P10-Jahrgänge 8 von 13 (davon Haupt 8); P10-Typen 3; Summe ertrag 22.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Pythagoras Kathete | 15 | 5 | 5 | 2016 | 2026 | 0 | 7 |  |
| Pythagoras Gleichung zuordnen | 5 | 4 | 4 | 2017 | 2026 | 5 | 0 |  |
| Rechten Winkel begründen | 2 | 1 | 1 | 2025 | 2025 | 0 | 1 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |

- 2.1 Gleichung nach einer Kathete umstellen (a² = c² − b², b² = c² − a²) → „Pythagoras Kathete“ · „Pythagoras Gleichung zuordnen“ – P10-Jahrgänge 7 (Haupt 7). Grund: Erster Schritt der Kathetenrechnung (2019-OS-K3a BC² = 9² − 4²) und Kathetenform des Auswählens (2024-OS-B1f z = √(x² − y²)).
- 2.2 Kathetengleichung aus Optionen ankreuzen (P10-Form) → „Pythagoras Gleichung zuordnen“ – P10-Jahrgänge 4 (Haupt 4). Grund: Original 2024-OS-B1f: Kathete z gesucht, vier Gleichungen zur Auswahl.
- 2.3 Kathete aus Hypotenuse und Kathete mit aufgehender Wurzel → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: Grundfall der Definition „Kathete … aus Hypotenuse und anderer Kathete“ mit leichteren Zahlen; die Originale haben nie eine aufgehende Wurzel.
- 2.4 mit nicht aufgehender Wurzel: Zwischenergebnis a², Näherungswert → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2019-OS-K3a (BC² = 65, ≈ 8,06 m) und 2026-FOR-K4a (h = √855 ≈ 29,2 cm).
- 2.5 Dezimalzahlen → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: Dezimalzahlen in 2022-OS-K5a (√(14,1² − 7,4²)) und 2026-FOR-K2c (√(8,6² − 4,7²)).
- 2.6 Ergebnis prüfen: die Kathete ist kürzer als die Hypotenuse → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: Kontrollschritt gegen die Fehlerquelle aller sechs Kathete-Originale „Quadrate addiert“, die eine Kathete länger als die Hypotenuse liefert (2024-OS-K6a 461 m bei AB = 384 m).
- 2.7 Nachweis mit vorgegebenem Ergebnis („Weisen Sie nach, dass … ≈ …“; P10-Form) → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2022-OS-K5a: Nachweis AD ≈ 12,0 m, Nebentyp „Behauptung prüfen“ zu genau dieser Behauptung.
- 2.8 Kathete im Sachzusammenhang (Höhenunterschied der Seilbahn, Abstand auf dem Platz, Höhe des Parallelogramms mit Fußpunkt außerhalb) → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: Seilbahn 2024-OS-K6a, Abstand 2019-OS-K3a, Parallelogrammhöhe mit Fußpunkt auf der Verlängerung 2026-FOR-K4a.
- 2.9 Umkehrung: drei Seiten gegeben, längste Seite als c, a² + b² mit c² vergleichen, rechtwinklig oder nicht (Antwort mit Rechnung) → „Rechten Winkel begründen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Begründen, dass ein Winkel 90° misst (… Umkehrung des Pythagoras)“; 2025-OS-K2c lässt AD² + DC² = 2500 = AC² als Weg zu (Typ in winkel-dreiecke.md).
- 2.10 rechten Winkel mit der Umkehrung begründen (Verfahren; Typ in winkel-dreiecke.md Einheit 3) → „Rechten Winkel begründen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition nennt die Umkehrung des Pythagoras als Begründungsweg; 2025-OS-K2c, dritter Weg.
- 2.11 pythagoreische Tripel erkennen und vervielfachen (Vorrat) → kein P10-Typ
- 2.12 Fehler finden (Quadrate addiert statt subtrahiert; kürzeste Seite als Hypotenuse; Umkehrung mit einer Kathete als c; „rechtwinklig“ aus der Skizze abgelesen statt gerechnet) → kein P10-Typ
- 2.13 Begründen (warum bei gesuchter Kathete subtrahiert wird; warum die Zwölfknotenschnur mit den Abschnitten drei, vier, fünf einen rechten Winkel liefert) → „Rechten Winkel begründen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Die zweite Begründung ist genau die Leistung der Definition „Begründen, dass ein Winkel 90° misst (… Umkehrung des Pythagoras)“, vgl. 2025-OS-K2c; die erste hat keinen P10-Typ.

**Einheit 3 · Pythagoras in Figuren und Körpern** – P10-Jahrgänge 9 von 13 (davon Haupt 8); P10-Typen 5; Summe ertrag 30.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Streckenlänge aus Koordinaten berechnen | 4 | 1 | 1 | 2019 | 2019 | 0 | 1 |  |
| Mantellinie Kegel bestimmen | 2 | 1 | 1 | 2018 | 2018 | 0 | 1 |  |
| Pythagoras Kathete | 15 | 5 | 5 | 2016 | 2026 | 0 | 7 |  |
| Pythagoras Hypotenuse | 9 | 3 | 4 | 2015 | 2025 | 0 | 3 |  |
| Kegelhöhe aus Mantellinie und Radius berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 3.1 rechtwinkliges Teildreieck in der Figur markieren und seine drei Seiten benennen (Hypotenuse gegenüber dem rechten Winkel) → „Pythagoras Kathete“ · „Pythagoras Hypotenuse“ · „Mantellinie Kegel bestimmen“ · „Streckenlänge aus Koordinaten berechnen“ – P10-Jahrgänge 9 (Haupt 8). Außerhalb der Themen des Eintrags (zählt nicht): „Gleichung zu Figur erläutern“. Grund: Teilschritt der Figurenaufgaben: Teildreieck ADC in 2022-OS-K5a, Rechteck im Becherquerschnitt 2022-OS-K2c, Stützdreieck aus Radius, Dachhöhe und Mantellinie 2018-OS-K6d, rechter Winkel bei A in 2019-OS-K2d, Teildreieck XCE in 2021-GYM-K4d.
- 3.2 Höhe im gleichschenkligen Dreieck aus Schenkel und halber Grundseite → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „Kathete … aus Hypotenuse und anderer Kathete“ mit dem Schenkel als Hypotenuse; kein Original mit dieser Figur.
- 3.3 Schenkel aus Höhe und halber Grundseite → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2023-GYM-K6a: Schenkel = √(40² + 100²) im halben gleichschenkligen Dreieck, Fehlerquelle volle Basis.
- 3.4 gleichschenkliges Trapez: Überstand als halbe Differenz der parallelen Seiten, Schenkel oder Höhe → „Pythagoras Hypotenuse“ · „Pythagoras Kathete“ – P10-Jahrgänge 8 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Umfang Trapez berechnen“ · „Trapezhöhe aus Fläche berechnen“. Grund: Definitionen von „Umfang Trapez berechnen“ (Schenkel über Pythagoras, 2023-OS-K2c mit Überstand 5,4 m) und „Trapezhöhe aus Fläche berechnen“ (aus Schenkel und halber Seitendifferenz, 2014-OS-K5c √(57² − 15²)); der Schenkel ist Hypotenuse, die Höhe Kathete.
- 3.5 Parallelogramm: Höhe mit Fußpunkt auf der Verlängerung der Grundseite → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2026-FOR-K4a: h = √(32² − 13²) mit F auf der Verlängerung von AB.
- 3.6 stumpfwinkliges Dreieck mit Höhe: Teilstrecke der Grundseite → „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2022-OS-K5a: Teilstrecke AD = √(14,1² − 7,4²) im Teildreieck mit der Höhe hc.
- 3.7 Drachen und Raute: Seite aus den halben Diagonalen → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen“. Grund: 2025-OS-K2a: AB = √(25² + 55²) aus den Diagonalenabschnitten (Nebentyp); Definition des GYM-Typs, Seiten aus den Diagonalenabschnitten über den Satz des Pythagoras (2017-GYM-K3b).
- 3.8 Diagonale im Rechteck, Raumdiagonale im Quader in zwei Schritten → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: Diagonale im Rechteck in 2022-OS-K2c; die Raumdiagonale ist dieselbe Hypotenusenrechnung zweimal, ohne Original.
- 3.9 Streckenlänge aus Koordinaten: Differenzen der x- und y-Werte als Katheten, auch negative Koordinaten (P10-Form) → „Streckenlänge aus Koordinaten berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Umfang eines Dreiecks aus Koordinaten berechnen“ · „Dreiecksart aus Koordinaten nachweisen“. Grund: Definition „über die Koordinatendifferenzen mit dem Satz des Pythagoras“, 2019-OS-K2d mit A(0|−2); dieselbe Rechnung in 2015-GYM-K2c (RO = √29) und 2024-GYM-K3c (AC = BC = √2).
- 3.10 Seitenhöhe der Pyramide aus Höhe und halber Grundkante → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Mantelfläche einer Pyramide berechnen“. Grund: 2015-OS-K6c: h_s = √(0,68² + 0,40²) als Nebentyp „Pythagoras Hypotenuse“; Definition „… über den Satz des Pythagoras ermittelten Seitenhöhe“ (2019-GYM-K4b).
- 3.11 Mantellinie des Kegels aus Radius und Höhe, Radius zuerst aus dem Durchmesser → „Mantellinie Kegel bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Mantellinie eines Kegels aus Radius und Höhe“; 2018-OS-K6d mit r = 3,2 m aus d = 6,4 m.
- 3.12 Kegelhöhe aus Mantellinie und Radius → „Kegelhöhe aus Mantellinie und Radius berechnen“ · „Pythagoras Kathete“ – P10-Jahrgänge 5 (Haupt 5). Grund: GYM-Typ gleichen Inhalts (2022-GYM-K4b); 2026-FOR-K2c rechnet die Kegelhöhe √(8,6² − 4,7²) als „Pythagoras Kathete“.
- 3.13 Rechenweg ohne Zahlen beschreiben (P10-Form) → „Mantellinie Kegel bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „… oder den Rechenweg beschreiben“; 2018-OS-K6d verlangt den Rechenweg für den Dachbalken ohne Zahlenergebnis.
- 3.14 Gesamthöhe eines Turms aus Zylinderhöhe und Kegelhöhe → „Pythagoras Kathete“ · „Kegelhöhe aus Mantellinie und Radius berechnen“ – P10-Jahrgänge 5 (Haupt 5). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: 2026-FOR-K2c (Kegelhöhe, dann 25,0 m + 7,2 m, Nebentyp „Strecke aus Teilstrecken berechnen“) und 2022-GYM-K4b (Gesamthöhe der Boje aus Halbkugelradius und Kegelhöhe).
- 3.15 Stab oder Stange schräg im Zylinder oder Quader mit Überstand → „Pythagoras Hypotenuse“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2022-OS-K2c: Stab diagonal im Becher, 2 cm Überstand.
- 3.16 Rampe, Leiter, Seil an der Wand mit Skizze → „Pythagoras Hypotenuse“ · „Pythagoras Kathete“ – P10-Jahrgänge 8 (Haupt 7). Grund: Rampe 2025-OS-K4a und Seil 2019-GYM-K3b mit gesuchter Hypotenuse, Höhenunterschied an der Seilbahn 2024-OS-K6a mit gesuchter Kathete.
- 3.17 Fehler finden (Radius statt Durchmesser oder umgekehrt; ganze statt halbe Seite; Mantellinie als Höhe; Teilstrecke oder Überstand vergessen; Koordinaten falsch abgelesen) → kein P10-Typ
- 3.18 Begründen (warum im gleichschenkligen Dreieck die halbe Grundseite gilt; warum die Raumdiagonale zwei Rechnungen braucht) → kein P10-Typ

### trigonometrie

themen.csv: „Trigonometrie im rechtwinkligen Dreieck“, „Sinus- und Kosinussatz“.

**Einheit 1 · Seite berechnen mit Sinus, Kosinus und Tangens** – P10-Jahrgänge 13 von 13 (davon Haupt 11); P10-Typen 5; Summe ertrag 42.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Winkelfunktion Seitenverhältnis angeben | 5 | 5 | 5 | 2017 | 2025 | 5 | 0 |  |
| Trigonometrische Gleichung nach Seite umstellen | 1 | 1 | 1 | 2020 | 2020 | 1 | 0 |  |
| Seite im rechtwinkligen Dreieck berechnen | 23 | 7 | 9 | 2014 | 2026 | 0 | 8 |  |
| Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Winkel im rechtwinkligen Dreieck berechnen | 13 | 5 | 6 | 2019 | 2026 | 0 | 6 | nicht in der Zuordnungszeile der Einheit |

- 1.1 rechten Winkel und markierten Winkel finden, Hypotenuse, Gegenkathete und Ankathete beschriften (Dreieck in verschiedener Lage: rechter Winkel unten links, unten rechts, oben; Hypotenuse unten oder oben) → „Winkelfunktion Seitenverhältnis angeben“ · „Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen“ · „Seite im rechtwinkligen Dreieck berechnen“ · „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 13 (Haupt 11). Grund: Teilschritt aller Aufgaben des Themas: 2025-OS-B1g („Gegenkathete von γ ist u“), GYM-Definition „typische Verwechslung von Ankathete und Gegenkathete“, Fehlerquellen in 2016-GYM-K4d (Seite) und 2024-OS-K6b (Winkel, 255 als Gegenkathete).
- 1.2 Seiten vom zweiten spitzen Winkel aus neu benennen (Gegen- und Ankathete tauschen) → „Winkelfunktion Seitenverhältnis angeben“ · „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 8 (Haupt 8). Grund: 2017-OS-B1j und 2018-OS-B1g fragen nach β statt α; Fehlerquelle „Winkel am anderen Ende“ in 2020-OS-K5b und 2019-OS-K2d (tan β = 2/4).
- 1.3 sin, cos oder tan zum beschrifteten Dreieck als Bruch eintragen (P10-Form, Buchstaben r, s, t; a, b; u, v, w) → „Winkelfunktion Seitenverhältnis angeben“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „sin, cos oder tan eines Winkels als Verhältnis der beschrifteten Seiten angeben“; 2025-OS-B1g (Eintragen), 2017-OS-B1j, 2019-OS-B1h, 2020-OS-B1c.
- 1.4 die richtige von drei Gleichungen ankreuzen (P10-Form) → „Winkelfunktion Seitenverhältnis angeben“ · „Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2018-OS-B1g (sin β = b/a unter drei Gleichungen); je Option dieselbe Prüfung wie im GYM-Typ „eine behauptete Gleichung für sin, cos oder tan … als wahr oder falsch prüfen“ (2024-GYM-B2a).
- 1.5 sin-, cos- und tan-Werte mit dem Taschenrechner, Grad-Modus prüfen → „Seite im rechtwinkligen Dreieck berechnen“ · „Trigonometrische Gleichung nach Seite umstellen“ – P10-Jahrgänge 10 (Haupt 8). Grund: Rechenschritt jeder Seitenrechnung; Fehlerquelle „Taschenrechner in Bogenmaß“ in 2021-OS-K3a, sin 30° = 0,5 in 2020-OS-B1j.
- 1.6 Seitenverhältnis aus gegebenen Längen als Dezimalzahl und Vergleich mit dem Taschenrechnerwert des Winkels → kein P10-Typ
- 1.7 Gegenkathete aus Hypotenuse und Winkel (Sinus, mal) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: 2021-OS-K3a (AB = 1500 · sin 55°) und 2018-OS-K4d (CB = 112,8 · sin 30°).
- 1.8 Ankathete aus Hypotenuse und Winkel (Kosinus, mal) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: 2021-OS-K3b (AD = 1500 · cos 55°) und 2023-OS-K7b (AF = 131,5 · cos 45°).
- 1.9 Hypotenuse aus Gegenkathete und Winkel (geteilt durch den Sinus) → „Seite im rechtwinkligen Dreieck berechnen“ · „Trigonometrische Gleichung nach Seite umstellen“ – P10-Jahrgänge 10 (Haupt 8). Grund: 2022-OS-K5d (a = 7,4 : sin 52°) und 2026-FOR-K4c (AC = 29,24 : sin 22°); ohne Figur dieselbe Umstellung in 2020-OS-B1j (x = 7 : sin 30°).
- 1.10 Hypotenuse aus Ankathete und Winkel (geteilt durch den Kosinus) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: 2023-OS-K7b (BC = BF : cos 65°) und 2025-GYM-K4a (SQ = PQ : cos 20°).
- 1.11 Gegenkathete aus Ankathete und Winkel (Tangens, mal) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: 2016-OS-K7c: BD = AD · tan 34°.
- 1.12 Ankathete aus Gegenkathete und Winkel (geteilt durch den Tangens) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: 2017-OS-K4b (PB = 1,20 : tan 34,9°) und 2022-OS-K5e (DB = 7,4 : tan 52°, Nebentyp).
- 1.13 Funktion selbst wählen: welche zwei Seiten sind beteiligt → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: Definition „über sin, cos oder tan“ ohne Vorgabe der Funktion; Fehlerquellen „Sinus verwenden“ (2017-OS-K4b) und „cos statt sin“ (2018-OS-K4d).
- 1.14 Gleichung ohne Figur nach der Seite umstellen, Seite im Nenner (P10-Form) → „Trigonometrische Gleichung nach Seite umstellen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „sin α = a/x ohne Figur nach x umstellen“; Original 2020-OS-B1j.
- 1.15 Winkel als Dezimalgrad, Seiten als Dezimalzahlen → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: 2017-OS-K4b (tan 34,9°, 1,20 m) und 2018-OS-K4d (112,8 m).
- 1.16 Einheit beim Ergebnis, Runden auf eine Dezimale → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: Muster der Kontextaufgaben: Ergebnis auf eine Dezimale mit Einheit, etwa 2022-OS-K5d (a ≈ 9,4 m) und 2026-FOR-K4c (≈ 78,1 cm).
- 1.17 Ergebnis prüfen: Kathete kürzer als Hypotenuse → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: Kontrollschritt gegen die Fehlerquelle „a = 7,4 · sin 52°“ in 2022-OS-K5d, die eine Hypotenuse kürzer als die Kathete liefert.
- 1.18 Nachweis mit vorgegebenem Ergebnis (P10-Form) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2021-OS-K3a (zu zeigen AB ≈ 1229 m) und 2023-OS-K7b (Nachweis BF ≈ AF ≈ 93,0 cm, Nebentyp „Behauptung prüfen“ zu genau dieser Behauptung).
- 1.19 Sachaufgabe mit gegebener Skizze (Leiter an der Wand, Dachschräge mit Wand, Rampe, Diagonale eines Vierecks mit rechtem Winkel) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: Dachwand 2017-OS-K4b, Viereck mit rechtem Winkel und Diagonale 2021-OS-K3a und 2021-OS-K3b.
- 1.20 Fehler finden (Ankathete als Gegenkathete; Sinus statt Kosinus; mal statt geteilt; Verhältnis umgedreht; Taschenrechner im Bogenmaß) → kein P10-Typ
- 1.21 Begründen (warum sin α kleiner als eins ist; warum das Verhältnis in einem größeren Dreieck mit demselben Winkel gleich bleibt) → kein P10-Typ

**Einheit 2 · Winkel berechnen** – P10-Jahrgänge 13 von 13 (davon Haupt 10); P10-Typen 3; Summe ertrag 36.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Winkel im rechtwinkligen Dreieck berechnen | 13 | 5 | 6 | 2019 | 2026 | 0 | 6 |  |
| Seite im rechtwinkligen Dreieck berechnen | 23 | 7 | 9 | 2014 | 2026 | 0 | 8 | nicht in der Zuordnungszeile der Einheit |
| Neigungswinkel einer Geraden berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 2.1 „Seite oder Winkel gesucht“ erkennen → „Winkel im rechtwinkligen Dreieck berechnen“ · „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 13 (Haupt 10). Grund: Die Stämme mischen beide Fragen (2022-OS-K5b Winkel, 2022-OS-K5d Seite; 2026-FOR-K4b und 2026-FOR-K4c), das Zuordnen gehört zu jeder Teilaufgabe.
- 2.2 zwei gegebene Seiten vom gesuchten Winkel aus benennen und die Funktion wählen → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2024-OS-K6b (cos β1 = 255 : 384, Fehlerquelle sin statt cos) und 2019-OS-K3b (cos α = 4/9).
- 2.3 Verhältnis als Bruch und als Dezimalzahl → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2026-FOR-K4b: cos ε = 13 : 32 = 0,406, dann ε.
- 2.4 Umkehrtaste am Taschenrechner (SHIFT sin, cos, tan; Anzeige sin⁻¹) → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: Definition „über tan, sin oder cos und die Umkehrfunktion“; 2019-OS-K3b α = cos⁻¹(4/9).
- 2.5 Winkel aus Gegenkathete und Hypotenuse (sin⁻¹) → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2022-OS-K5b: sin α = 7,4 : 14,1.
- 2.6 aus Ankathete und Hypotenuse (cos⁻¹) → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2019-OS-K3b, 2024-OS-K6b und 2026-FOR-K4b rechnen den Winkel mit cos⁻¹.
- 2.7 aus beiden Katheten (tan⁻¹) → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2020-OS-K5b (tan α = 14/9), als Nebentyp 2025-OS-K4a (tan α = 16 : 170) und 2019-OS-K2d (tan β = 4/2).
- 2.8 Runden auf eine Dezimale, Gradzeichen → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: Ergebnisse der Originale auf eine Dezimale, etwa 2022-OS-K5b (α ≈ 31,7°) und 2024-OS-K6b (β1 ≈ 48,4°).
- 2.9 zweiter spitzer Winkel als Ergänzung zum rechten Winkel, Kontrolle mit der zweiten Funktion → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Außerhalb der Themen des Eintrags (zählt nicht): „Winkelsumme im Dreieck anwenden“. Grund: 2022-OS-K5c: γ₁ = 180° − 90° − α (Definition „Dritten Winkel … aus der Winkelsumme“); die zweite Funktion ist der Alternativweg in 2022-OS-K5b (cos α = 12 : 14,1) und 2024-OS-K6b.
- 2.10 Steigungswinkel einer Rampe oder Seilbahn aus Höhe und Länge → „Winkel im rechtwinkligen Dreieck berechnen“ · „Neigungswinkel einer Geraden berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: Rampe 2025-OS-K4a (Nebentyp), Seilbahn 2024-OS-K6b; Steigungswinkel der Seilbahn über den Tangens in 2020-GYM-K4b.
- 2.11 Winkel eines Dreiecks im Koordinatensystem aus abgelesenen Katheten (P10-Form) → „Winkel im rechtwinkligen Dreieck berechnen“ · „Neigungswinkel einer Geraden berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2019-OS-K2d: tan β = 4/2 im Koordinatendreieck (Nebentyp); Definition des GYM-Typs, Winkel einer Geraden zur x-Achse über den Tangens (2018-GYM-K2d).
- 2.12 Winkel im Teildreieck mit gezeichneter Höhe → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2022-OS-K5b: α im Teildreieck ADC mit der Höhe hc.
- 2.13 Nachweis mit vorgegebenem Winkel („Zeigen Sie rechnerisch, dass α ≈ …“; P10-Form) → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2019-OS-K3b („also rund 64°“) und 2026-FOR-K4b (Nachweis ε ≈ 66°).
- 2.14 Winkel prüfen: die längere Kathete liegt dem größeren Winkel gegenüber → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Grund: Kontrollschritt gegen die Fehlerquelle „Katheten vertauscht“, die den anderen spitzen Winkel liefert (2020-OS-K5b 32,7° statt 57,3°, 2019-OS-K2d 26,6°).
- 2.15 Fehler finden (Katheten beim Tangens vertauscht – der andere Winkel; sin statt cos; Verhältnis größer als eins beim Sinus – Taschenrechner meldet Fehler; Umkehrtaste vergessen, Verhältnis als Winkel angegeben) → kein P10-Typ
- 2.16 Begründen (warum der Taschenrechner zu einem Sinuswert über eins keinen Winkel liefert) → kein P10-Typ

**Einheit 3 · Rechtwinklige Teildreiecke in Figuren und Vermessung** – P10-Jahrgänge 13 von 13 (davon Haupt 10); P10-Typen 4; Summe ertrag 36.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Seite im rechtwinkligen Dreieck berechnen | 23 | 7 | 9 | 2014 | 2026 | 0 | 8 |  |
| Winkel im rechtwinkligen Dreieck berechnen | 13 | 5 | 6 | 2019 | 2026 | 0 | 6 |  |
| Diagonale eines Drachenvierecks über Winkelfunktion berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Formel über Winkelfunktion herleiten | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 3.1 rechtwinkliges Teildreieck in der Figur markieren, rechten Winkel und gegebenen Winkel finden, Seiten vom Winkel aus benennen → „Seite im rechtwinkligen Dreieck berechnen“ · „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 13 (Haupt 10). Grund: Teilschritt der Figurenaufgaben: Dreieck AFC in 2026-FOR-K4c, Teildreiecke ABF und CBF in 2023-OS-K7b, Hilfsdreieck im Trapez 2020-OS-K5b.
- 3.2 Höhe im gleichschenkligen Dreieck aus Schenkel und Basiswinkel → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: Definition „Seite aus einer Seite und einem Winkel“ im halben gleichschenkligen Dreieck; kein Original mit dieser Figur, verwandt die Kegelhöhe im gleichschenkligen Achsenschnitt 2015-GYM-K4a.
- 3.3 Höhe im beliebigen Dreieck aus Seite und Winkel, dann Fläche (Typ in flaechen.md) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt Dreieck berechnen“. Grund: 2022-OS-K5e und 2015-OS-K5d: Teilstrecken über Sinus oder Tangens (Nebentyp „Seite im rechtwinkligen Dreieck berechnen“), dann die Fläche (Definition „Flächeninhalt Dreieck berechnen“).
- 3.4 Trapez: Schenkel aus Höhe und Basiswinkel, Höhe aus Schenkel und Winkel, Überstand mit dem Tangens → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Umfang Trapez berechnen“. Grund: Definition „Umfang eines Trapezes …, dessen Schenkel erst über Trigonometrie … bestimmt werden müssen“, 2023-OS-K2c (s = 8 : sin 56°, Nebentyp „Seite …“); Höhe aus Schenkel und Winkel in 2023-GYM-K6d (x = b · sin β).
- 3.5 rechtwinkliges Trapez: Hilfsdreieck mit der Differenz der beiden Höhen als Kathete, Winkel darin (P10-Form) → „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 6 (Haupt 5). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: 2020-OS-K5b: Kathete 15 − 6 = 9 (Nebentyp „Strecke aus Teilstrecken berechnen“), dann tan α = 14/9.
- 3.6 Parallelogramm: Höhe mit Fußpunkt auf der Verlängerung, Winkel dort, Diagonale aus Höhe und Winkel → „Seite im rechtwinkligen Dreieck berechnen“ · „Winkel im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 13 (Haupt 10). Grund: 2026-FOR-K4b (Winkel ε an der Verlängerung) und 2026-FOR-K4c (Diagonale AC = 29,24 : sin 22°).
- 3.7 Drachen und Raute: halbe Diagonale aus Seite und Winkel → „Diagonale eines Drachenvierecks über Winkelfunktion berechnen“ · „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: Definition des GYM-Typs (2018-GYM-K4a, TM = 51 · sin β₁); 2018-GYM-K4b (LM = 51 · cos β₁) und der zweite Weg in 2015-OS-K5c (AE = 4,1 · sin 21°) als „Seite im rechtwinkligen Dreieck berechnen“.
- 3.8 Vermessung: Höhe eines Turms oder Bergs aus Abstand und Höhenwinkel, Gerätehöhe oder Sockel addieren (P10-Form) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: 2018-OS-K4d: CB = 112,8 · sin 30° plus Gerätehöhe 1,5 m (Nebentyp „Strecke aus Teilstrecken berechnen“); ebenso 2016-GYM-K4d (8 m plus 37,6 · sin 30°).
- 3.9 Plattform oder Aufbau zur Höhe addieren → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: 2018-OS-K4d: Höhe von D mit der Plattform 12,0 m (69,9 m), Nebentyp „Strecke aus Teilstrecken berechnen“.
- 3.10 Teilwinkel: den Winkel des Teildreiecks als Differenz zweier gegebener Winkel bilden (P10-Form) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Winkel aus Teilwinkeln berechnen“. Grund: 2016-OS-K7c: Winkel DAB = 70° − 36° als Nebentyp „Winkel aus Teilwinkeln berechnen“, dann BD = AD · tan 34°.
- 3.11 zwei Teildreiecke nacheinander an derselben Höhe (P10-Form) → „Seite im rechtwinkligen Dreieck berechnen“ · „Diagonale eines Drachenvierecks über Winkelfunktion berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: 2023-OS-K7b: BF im Dreieck ABF, dann BC im Dreieck CBF; Definition des GYM-Typs „zwei rechtwinklige Teildreiecke mit gemeinsamer Kathete“ (2018-GYM-K4a).
- 3.12 Strecke aus Teilstrecken nach der Trigonometrie → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: Nebentyp „Strecke aus Teilstrecken berechnen“ in 2018-OS-K4d und 2020-OS-K5b; BD = DE + EB aus zwei Teildreiecken im zweiten Weg von 2015-OS-K5c.
- 3.13 Rechenweg als Lösungsplan ohne Zahlen (P10-Form) → „Seite im rechtwinkligen Dreieck berechnen“ · „Formel über Winkelfunktion herleiten“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Flächeninhalt Dreieck berechnen“. Grund: Definition „Flächeninhalt Dreieck berechnen … auch als Beschreibung des Rechenwegs ohne Zahlen“, 2015-OS-K5d mit Nebentyp „Seite …“ (AE = AD · sin δ); die allgemeine Formel über ein Teildreieck in 2021-GYM-K5a.
- 3.14 zweiter Weg mit dem Satz des Pythagoras, Vergleich der Ergebnisse → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Außerhalb der Themen des Eintrags (zählt nicht): „Pythagoras Kathete“. Grund: 2016-OS-K7b führt beide Wege („Pythagoras Kathete“, Nebentyp 920 · sin 54°), 2021-OS-K3b lässt den Pythagoras neben dem Kosinus zu.
- 3.15 Seitenhöhe oder Mantellinie aus Grundkante oder Radius und Neigungswinkel im Stützdreieck (kein P10-Original, RLP G, LISUM-PH „Körper“) → „Seite im rechtwinkligen Dreieck berechnen“ · „Formel über Winkelfunktion herleiten“ – P10-Jahrgänge 9 (Haupt 7). Grund: Stützdreieck im Kegel aus Radius und halbem Öffnungswinkel in 2015-GYM-K4a (h = r : tan 30°) und 2021-GYM-K5a (Tiefe über tan(α/2)); dort ist die Höhe gesucht, nicht die Mantellinie.
- 3.16 Fehler finden (ganzer Winkel statt Teilwinkel; ganze Höhe statt Differenz; Gerätehöhe vergessen; Dreieck ohne rechten Winkel mit Sinus gerechnet; Winkel am falschen Punkt angetragen) → kein P10-Typ
- 3.17 Begründen (warum im gleichschenkligen Dreieck die halbe Grundseite zum Basiswinkel gehört; warum in einem Dreieck ohne rechten Winkel erst eine Höhe nötig ist) → kein P10-Typ

**Einheit 4 · Sinussatz** – P10-Jahrgänge 13 von 13 (davon Haupt 13); P10-Typen 5; Summe ertrag 52.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Sinussatz Seite berechnen | 29 | 9 | 9 | 2014 | 2025 | 0 | 9 |  |
| Kosinussatz Seite berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Sinussatz Winkel berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Seite im rechtwinkligen Dreieck berechnen | 23 | 7 | 9 | 2014 | 2026 | 0 | 8 | nicht in der Zuordnungszeile der Einheit |
| Kosinussatz Winkel berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 4.1 rechtwinklig oder nicht: sin, cos, tan oder Sinussatz (Vorstufe) → „Sinussatz Seite berechnen“ · „Kosinussatz Seite berechnen“ – P10-Jahrgänge 9 (Haupt 9). Grund: Fehlerquelle „Dreieck ACD als rechtwinklig behandeln“ in 2018-OS-K4c und „Satz des Pythagoras statt Kosinussatz“ in 2015-GYM-K5a.
- 4.2 Seite und Gegenwinkel als Paar markieren, das vollständige Paar finden → „Sinussatz Seite berechnen“ · „Sinussatz Winkel berechnen“ – P10-Jahrgänge 9 (Haupt 9). Grund: Fehlerquelle „falsche Paarung Seite–Gegenwinkel“ in 2025-OS-K4c und 2024-OS-K6d, ebenso in 2025-GYM-K4b beim Winkel.
- 4.3 dritter Winkel aus der Winkelsumme → „Sinussatz Seite berechnen“ – P10-Jahrgänge 9 (Haupt 9). Außerhalb der Themen des Eintrags (zählt nicht): „Winkelsumme im Dreieck anwenden“. Grund: Nebentyp „Winkelsumme im Dreieck anwenden“ in 2019-OS-K3c, 2020-OS-K7c und 2021-OS-K3c; Schritt im Verfahren von 2024-OS-K6d (γ = 34°) und 2025-OS-K4c.
- 4.4 Sinussatz aufstellen (Seite durch Sinus des Gegenwinkels gleich Seite durch Sinus des Gegenwinkels) → „Sinussatz Seite berechnen“ · „Sinussatz Winkel berechnen“ – P10-Jahrgänge 9 (Haupt 9). Grund: Erster Schritt beider Sinussatz-Typen (2024-OS-K6d, 2015-GYM-K5b).
- 4.5 nach der Seite umstellen und mit dem Taschenrechner berechnen → „Sinussatz Seite berechnen“ – P10-Jahrgänge 9 (Haupt 9). Grund: 2024-OS-K6d: BC = 384 · sin 38° : sin 34°.
- 4.6 stumpfer Winkel im Sinussatz (Taschenrechner rechnet direkt; der stumpfe Winkel gehört in die Winkelsumme) → „Sinussatz Seite berechnen“ – P10-Jahrgänge 9 (Haupt 9). Grund: Stumpfe Winkel in vier Originalen: 2015-OS-K5c (123°), 2020-OS-K7c (115°), 2024-OS-K6d (108°), 2025-OS-K4c (141°).
- 4.7 Nachweis mit vorgegebenem Ergebnis (P10-Form) → „Sinussatz Seite berechnen“ – P10-Jahrgänge 9 (Haupt 9). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2018-OS-K4c: Nachweis AC ≈ 112,8 m, Nebentyp „Behauptung prüfen“ zu genau dieser Behauptung.
- 4.8 Aussage über zwei Seiten prüfen (P10-Form) → „Sinussatz Seite berechnen“ – P10-Jahrgänge 9 (Haupt 9). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2021-OS-K3c: Aussage „BC ist genauso lang wie DC“ mit Nebentyp „Behauptung prüfen“.
- 4.9 Sinussatz im Viereck mit Diagonale: Teilwinkel zuerst, dann das Dreieck mit dem vollständigen Paar wählen (P10-Form) → „Sinussatz Seite berechnen“ – P10-Jahrgänge 9 (Haupt 9). Grund: 2019-OS-K3c (Teilwinkel 26° und 60°) und 2021-OS-K3c (35°, 74°, 46°) im Viereck mit Diagonale.
- 4.10 Seite als Teil einer Weglänge oder Differenz zu einer Teilstrecke (P10-Form) → „Sinussatz Seite berechnen“ – P10-Jahrgänge 9 (Haupt 9). Außerhalb der Themen des Eintrags (zählt nicht): „Strecke aus Teilstrecken berechnen“. Grund: 2014-OS-K2b (plus 2500 m) und 2020-OS-K7c (DP = DE − 10), beide mit Nebentyp „Strecke aus Teilstrecken berechnen“.
- 4.11 zweiter Weg über zwei rechtwinklige Teildreiecke mit der Höhe (Vergleich) → „Seite im rechtwinkligen Dreieck berechnen“ – P10-Jahrgänge 9 (Haupt 7). Grund: Nebentyp „Seite im rechtwinkligen Dreieck berechnen“ als zweiter Weg über die Höhe in 2014-OS-K2b und 2015-OS-K5c.
- 4.12 Winkel mit dem Sinussatz (kein P10-Original, RLP G) → „Sinussatz Winkel berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Typ mit Definition „einen Winkel mit dem Sinussatz … berechnen“; 2015-GYM-K5b und 2025-GYM-K4b.
- 4.13 Kosinussatz für die dritte Seite aus zwei Seiten und dem eingeschlossenen Winkel (kein P10-Original, RLP G) → „Kosinussatz Seite berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Typ mit Definition „eine Seite aus den zwei anliegenden Seiten und dem eingeschlossenen Winkel“; 2015-GYM-K5a, 2021-GYM-K4c, 2025-GYM-K4c.
- 4.14 Kosinussatz nach dem Winkel umgestellt (Vorrat, RLP H, LISUM-PH „nur GYM“) → „Kosinussatz Winkel berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Typ mit Definition „einen Winkel aus den drei gegebenen Seiten mit dem Kosinussatz“; 2014-GYM-K5b und 2020-GYM-K4c.
- 4.15 Fehler finden (Seite mit fremdem Winkel gepaart; Nebenwinkel statt Innenwinkel in der Winkelsumme; Dreieck als rechtwinklig behandelt; Symmetrie angenommen, die nicht gegeben ist) → kein P10-Typ
- 4.16 Begründen (warum der Sinussatz gilt – die Höhe zerlegt das Dreieck in zwei rechtwinklige Teildreiecke mit derselben Gegenkathete; die Herleitung ist in der LISUM-PH mit „nur GYM“ markiert, deshalb GYM-Sprosse) → kein P10-Typ

### winkel-dreiecke

themen.csv: „Ebene Figuren und Winkel“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Umfang eines Dreiecks aus Koordinaten berechnen“; „Flächeninhalt eines Dreiecks aus Koordinaten berechnen“; „Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen“; „Flächeninhalt eines Dreiecks aus drei Seiten berechnen“; „Flächeninhalt einer von Graphen begrenzten Figur berechnen“; „Gleichung zu Figur erläutern“.

**Einheit 1 · Winkel messen und zeichnen** – P10-Jahrgänge 6 von 13 (davon Haupt 3); P10-Typen 3; Summe ertrag 5.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Winkel aus Teilwinkeln berechnen | 1 | 1 | 3 | 2014 | 2018 | 0 | 1 |  |
| Strecke aus Teilstrecken berechnen | 4 | 3 | 6 | 2014 | 2026 | 1 | 2 |  |
| Winkel in zusammengesetzter Figur kennzeichnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Winkelart ankreuzen (spitz, recht, stumpf, gestreckt, überstumpf) → kein P10-Typ
- 1.2 Winkel schätzen (Viertel-, halber, Dreiviertel-Rechter) → kein P10-Typ
- 1.3 Winkel mit dem Geodreieck messen (innere oder äußere Skala) → kein P10-Typ
- 1.4 überstumpfen Winkel messen (Rest von 360°) → kein P10-Typ
- 1.5 Winkel mit gegebener Größe an einen Schenkel zeichnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Kreisdiagramm zeichnen“ · „Vieleck aus Seiten und Winkeln im Maßstab konstruieren“. Grund: Der Sektor wird mit dem berechneten Winkel an einen Radius angetragen (2015-OS-K7c „Sektor mit 52° am Radius abtragen“, 2017-OS-K2c mit 40°); im GYM-Typ werden 155° und 63° angetragen (2021-GYM-K4a).
- 1.6 Winkel benennen, Scheitel und Schenkel markieren → „Winkel in zusammengesetzter Figur kennzeichnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: Definition „einen … Winkel markieren“; 2025-GYM-B1a kennzeichnet γ und δ in der Figur.
- 1.7 Winkel aus Teilwinkeln (nebeneinander: Summe; ineinander: Differenz; Rest zum gestreckten oder vollen Winkel) → „Winkel aus Teilwinkeln berechnen“ · „Winkel in zusammengesetzter Figur kennzeichnen“ – P10-Jahrgänge 3 (Haupt 1). Grund: Definition „Winkel als Differenz oder Summe gegebener Winkel“, 2018-OS-K4a (35° − 30°); den doppelt so großen Winkel als Summe zweier β kennzeichnet 2025-GYM-B1a.
- 1.8 Strecke aus Teilstrecken (Summe, Differenz, Einheiten m/km) → „Strecke aus Teilstrecken berechnen“ – P10-Jahrgänge 6 (Haupt 3). Grund: Definition „als Summe oder Differenz gegebener Teilstrecken, ggf. nach Umrechnung“; 2016-OS-K7a und 2014-OS-K2a (Meter und Kilometer).
- 1.9 Fehler finden (falsche Skala: 130° statt 50°; Teilwinkel addiert statt subtrahiert) → kein P10-Typ
- 1.10 Begründen (warum ein Winkel über 90° stumpf heißt, wo die Grenze liegt) → kein P10-Typ

**Einheit 2 · Winkel an Geradenkreuzungen und Parallelen** – P10-Jahrgänge 11 von 13 (davon Haupt 11); P10-Typen 6; Summe ertrag 17.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Winkel über Scheitel- oder Nebenwinkel bestimmen | 2 | 2 | 2 | 2014 | 2019 | 2 | 0 |  |
| Winkel an geschnittenen Parallelen bestimmen | 2 | 2 | 2 | 2015 | 2020 | 2 | 0 |  |
| Winkel im Viereck berechnen | 4 | 3 | 3 | 2021 | 2026 | 3 | 1 |  |
| Winkel aus Teilwinkeln berechnen | 1 | 1 | 3 | 2014 | 2018 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Winkelsumme im Dreieck anwenden | 5 | 4 | 9 | 2015 | 2023 | 0 | 4 | nicht in der Zuordnungszeile der Einheit |
| Eigenschaft einer Figur zuordnen | 3 | 2 | 2 | 2016 | 2026 | 3 | 0 | nicht in der Zuordnungszeile der Einheit |

- 2.1 Scheitel- und Nebenwinkel benennen → „Winkel über Scheitel- oder Nebenwinkel bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Teilschritt: 2019-OS-B1a erkennt β und 35° als Scheitelwinkel, 2014-OS-B1f hat die Fehlerquelle „Nebenwinkel statt Scheitelwinkel“.
- 2.2 aus einem Winkel die drei anderen an der Kreuzung → „Winkel über Scheitel- oder Nebenwinkel bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „über Scheitel- oder Nebenwinkel …, ohne Parallelen“; 2014-OS-B1f an der Kreuzung zweier Geraden.
- 2.3 drei Geraden durch einen Punkt (Teilwinkel, Scheitelwinkel minus Teil) → „Winkel über Scheitel- oder Nebenwinkel bestimmen“ · „Winkel aus Teilwinkeln berechnen“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2014-OS-B1f: β = 50° − 30° am Scheitelwinkel, Nebentyp „Winkel aus Teilwinkeln berechnen“.
- 2.4 Stufenwinkel an Parallelen → „Winkel an geschnittenen Parallelen bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „über Stufen-, Wechsel-, Scheitel- oder Nebenwinkel“; Stufenwinkel in 2020-OS-B1g und 2020-GYM-B1b.
- 2.5 Wechselwinkel → „Winkel an geschnittenen Parallelen bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2020-OS-B1g: α = 74° als Wechselwinkel an Parallelen.
- 2.6 Nebenwinkel des Stufenwinkels (180° − …) → „Winkel an geschnittenen Parallelen bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2015-OS-B1d: α = 180° − 53°.
- 2.7 Winkel an einer Figur mit verlängerten Seiten (Scheitelwinkel des Innenwinkels; überflüssige Angabe) → „Winkel über Scheitel- oder Nebenwinkel bestimmen“ · „Winkelsumme im Dreieck anwenden“ – P10-Jahrgänge 10 (Haupt 6). Grund: Definition „in einer Figur mit verlängerten Seiten … überflüssige Angaben erkennen“, 2019-OS-B1a; Nebenwinkel 120° an der verlängerten Seite in 2018-OS-K4b („Winkelsumme im Dreieck anwenden“).
- 2.8 Winkel im Parallelogramm und Trapez an den parallelen Seiten → „Winkel im Viereck berechnen“ · „Eigenschaft einer Figur zuordnen“ – P10-Jahrgänge 4 (Haupt 4). Grund: Definition „in Trapez oder Parallelogramm über Neben- oder Gegenwinkel an den parallelen Seiten“ (2026-FOR-B1i, 2023-OS-K2a); 2016-OS-B1e fragt „gegenüberliegende Winkel gleich groß“.
- 2.9 Parallelität aus gleichen Stufenwinkeln prüfen → kein P10-Typ
- 2.10 Fehler finden (Nebenwinkel statt Scheitelwinkel; Stufenwinkel benutzt, obwohl die Geraden nicht parallel sind) → kein P10-Typ
- 2.11 Begründen (warum Scheitelwinkel gleich groß sind – beide sind Nebenwinkel desselben Winkels) → kein P10-Typ

**Einheit 3 · Winkelsummen, Dreiecke und Vierecke** – P10-Jahrgänge 11 von 13 (davon Haupt 9); P10-Typen 6; Summe ertrag 17.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Winkelsumme im Dreieck anwenden | 5 | 4 | 9 | 2015 | 2023 | 0 | 4 |  |
| Gleichschenkliges Dreieck erkennen | 3 | 1 | 1 | 2023 | 2023 | 1 | 1 |  |
| Eigenschaft einer Figur zuordnen | 3 | 2 | 2 | 2016 | 2026 | 3 | 0 |  |
| Rechten Winkel begründen | 2 | 1 | 1 | 2025 | 2025 | 0 | 1 |  |
| Winkel im Viereck berechnen | 4 | 3 | 3 | 2021 | 2026 | 3 | 1 | nicht in der Zuordnungszeile der Einheit |
| Dreiecksart aus Koordinaten nachweisen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 3.1 dritter Winkel im Dreieck (ganze Grade, Dezimalgrade) → „Winkelsumme im Dreieck anwenden“ – P10-Jahrgänge 9 (Haupt 4). Grund: Definition „Dritten Winkel eines Dreiecks aus der Winkelsumme 180°“; 2015-OS-K5b (ganze Grade) und 2017-OS-K4a (Dezimalgrade).
- 3.2 fehlender Winkel im Viereck (360°) → „Winkel im Viereck berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2021-OS-B1i: α = 360° − 50° − 140° − 130°.
- 3.3 Dreieck nach Winkeln und Seiten einteilen (Ankreuzen) → „Dreiecksart aus Koordinaten nachweisen“ – P10-Jahrgänge 0 (Haupt 0). Grund: Der GYM-Typ verlangt den Nachweis „gleichschenklig und rechtwinklig“ und setzt die Einteilung nach Seiten und Winkeln voraus (2024-GYM-K3c).
- 3.4 gleichschenklig: Basiswinkel gleich, dritter Winkel → „Winkelsumme im Dreieck anwenden“ – P10-Jahrgänge 9 (Haupt 4). Grund: 2023-OS-B1g: γ = 180° − 2 · 70° bei gleichen Basiswinkeln (Nebentyp).
- 3.5 aus gleichen Winkeln auf gleiche Schenkel schließen (Seite angeben) → „Gleichschenkliges Dreieck erkennen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „aus gleichen Basiswinkeln auf gleiche Schenkel schließen, als Angabe der Seite“; 2023-OS-B1g (BC = 6 cm).
- 3.6 gleichseitig 60° → „Winkelsumme im Dreieck anwenden“ – P10-Jahrgänge 9 (Haupt 4). Grund: Drei gleiche Winkel aus der Winkelsumme 180° (Definition); kein Original mit gleichseitigem Dreieck.
- 3.7 rechtwinklig: die zwei spitzen Winkel ergeben 90° → „Winkelsumme im Dreieck anwenden“ – P10-Jahrgänge 9 (Haupt 4). Grund: 2022-OS-K5c (γ₁ = 180° − 90° − α) und der zweite Weg in 2018-OS-K4b (δ und der Winkel bei A ergänzen sich zu 90°).
- 3.8 Winkel im Teildreieck (Höhe, Diagonale, Drachen mit rechtem Winkel der Diagonalen) → „Winkelsumme im Dreieck anwenden“ · „Rechten Winkel begründen“ · „Gleichschenkliges Dreieck erkennen“ – P10-Jahrgänge 10 (Haupt 6). Grund: Teildreieck mit Höhe 2022-OS-K5c, Drachen-Teildreieck 2015-OS-K5b; 45° im Teildreieck AFD mit rechtem Winkel der Diagonalen in 2025-OS-K2c, 45° im Teildreieck ABF an der Höhe in 2023-OS-K7a.
- 3.9 rechten Winkel begründen (gleichschenklig-rechtwinklig 45° + 45°; Winkelsumme) → „Rechten Winkel begründen“ – P10-Jahrgänge 1 (Haupt 1). (wortgleich)
- 3.10 Innenwinkelsumme von Fünf- und Sechseck über Dreiecke (Vorrat) → kein P10-Typ
- 3.11 Vierecksart-Eigenschaft ankreuzen („In jedem Trapez …“, „In jedem Parallelogramm …“) → „Eigenschaft einer Figur zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge im Vieleck begründen“. Grund: Originale 2026-FOR-B1c („In jedem Trapez …“) und 2016-OS-B1e („In jedem Parallelogramm …“); die Parallelogramm-Eigenschaft „Gegenseiten gleich lang“ trägt den GYM-Typ in 2022-GYM-K5b.
- 3.12 Fehler finden (Winkelsumme 180° im Viereck; Gegenwinkel statt Nachbarwinkel; Symmetrie im Drachen an der falschen Diagonale) → kein P10-Typ
- 3.13 Begründen (warum die Winkelsumme 180° ist – Wechselwinkel an der Parallelen durch C) → kein P10-Typ

**Einheit 4 · Dreiecke konstruieren** – P10-Jahrgänge 1 von 13 (davon Haupt 1); P10-Typen 2; Summe ertrag 1.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Dreiecksungleichung anwenden | 1 | 1 | 1 | 2020 | 2020 | 1 | 0 |  |
| Winkel in zusammengesetzter Figur kennzeichnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 4.1 Dreieck skizzieren und beschriften (Planfigur, gegebene Stücke markieren) → kein P10-Typ
- 4.2 Kongruenzsatz zu gegebenen Stücken benennen → kein P10-Typ
- 4.3 Konstruktion SSS (Zirkel) → kein P10-Typ
- 4.4 SWS → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Vieleck aus Seiten und Winkeln im Maßstab konstruieren“. Grund: Definition „aus einer Folge gegebener Seitenlängen und eingeschlossener Winkel … konstruieren“, Schritt für Schritt Seite, eingeschlossener Winkel, Seite (2021-GYM-K4a).
- 4.5 WSW → kein P10-Typ
- 4.6 SsW (Gegenwinkel der längeren Seite) → kein P10-Typ
- 4.7 gleichschenkliges Dreieck aus Basis und Schenkel, rechtwinkliges aus den Katheten → kein P10-Typ
- 4.8 Konstruktionsbeschreibung (drei bis vier Schritte) → kein P10-Typ
- 4.9 Dreiecksungleichung: konstruierbar oder nicht (b + c > a) → „Dreiecksungleichung anwenden“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Summe zweier Dreiecksseiten zur dritten (b + c > a)“; 2020-OS-B1i mit der Fehlerquelle entartetes Dreieck.
- 4.10 kongruente Figuren erkennen und Ecken zuordnen → „Winkel in zusammengesetzter Figur kennzeichnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: Definition „unter Nutzung der Kongruenz der Teildreiecke“: 2025-GYM-B1a kennzeichnet den gleich großen Winkel am entsprechenden Punkt des kongruenten Dreiecks.
- 4.11 Fehler finden (WWW als Kongruenzsatz; Winkel an der falschen Ecke angetragen; b + c = a als Dreieck) → kein P10-Typ
- 4.12 Begründen (warum drei Winkel nicht reichen) → kein P10-Typ

**Einheit 5 · Besondere Linien im Dreieck und Satz des Thales** – P10-Jahrgänge 1 von 13 (davon Haupt 1); P10-Typen 2; Summe ertrag 2.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Rechten Winkel begründen | 2 | 1 | 1 | 2025 | 2025 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Dreiecksart aus Koordinaten nachweisen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 5.1 Mittelsenkrechte einer Strecke mit dem Zirkel → kein P10-Typ
- 5.2 Umkreis (Schnittpunkt zweier Mittelsenkrechten) → kein P10-Typ
- 5.3 Winkelhalbierende konstruieren → kein P10-Typ
- 5.4 Inkreis → kein P10-Typ
- 5.5 Höhe zur Seite mit dem Geodreieck (beim stumpfwinkligen Dreieck auf die Verlängerung) → kein P10-Typ
- 5.6 Seitenhalbierende und Schwerpunkt → kein P10-Typ
- 5.7 Thales: Punkt auf dem Halbkreis, rechter Winkel; rechtwinkliges Dreieck über einem Durchmesser konstruieren → kein P10-Typ
- 5.8 rechten Winkel mit Thales begründen → „Rechten Winkel begründen“ · „Dreiecksart aus Koordinaten nachweisen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Rechten Winkel begründen“ nennt Thales als Weg (2025-OS-K2c, Alternative); 2024-GYM-K3c weist den rechten Winkel bei C über CM = AB : 2 mit dem Satz des Thales nach.
- 5.9 Fehler finden (Höhe als Seitenhalbierende gezeichnet; Umkreismittelpunkt beim stumpfwinkligen Dreieck innen gesucht; Thaleskreis mit der Hypotenuse als Radius statt als Durchmesser) → kein P10-Typ
- 5.10 Begründen (warum der Umkreismittelpunkt von allen Ecken gleich weit entfernt ist) → kein P10-Typ

### symmetrie-abbildungen

themen.csv: „Symmetrie und Abbildungen“.

**Einheit 1 · Koordinatensystem** – P10-Jahrgänge 1 von 13 (davon Haupt 1); P10-Typen 1; Summe ertrag 1.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lage eines Punktes zu den Achsen erkennen | 1 | 1 | 1 | 2020 | 2020 | 1 | 0 |  |

- 1.1 Achsen und Ursprung benennen, Einteilung ablesen → „Lage eines Punktes zu den Achsen erkennen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition unterscheidet x-Achse, y-Achse und Ursprung; Vorstufe von 2020-OS-B1b.
- 1.2 Punkt im ersten Quadranten eintragen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wertetabelle als Punkte darstellen“. Grund: Definition „Wertepaare einer Tabelle in ein vorgegebenes Koordinatensystem eintragen“; 2025-OS-K7a mit Punkten im ersten Quadranten.
- 1.3 Koordinaten eines eingezeichneten Punktes ablesen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Scheitelpunkt ablesen“ · „Schnittpunkt am Graphen ablesen“ · „Streckenlänge aus Koordinaten berechnen“. Grund: Scheitel am Graphen ablesen (2021-OS-B1d), Schnittpunkt am Bild ablesen (2023-OS-K4a), Punkte nur im Bild gegeben in 2019-OS-K2d (Fehlerquelle „Koordinaten falsch ablesen“).
- 1.4 Schreibweise P(x | y) lesen und schreiben (erste Zahl nach rechts, zweite nach oben) → „Lage eines Punktes zu den Achsen erkennen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Scheitelpunkt ablesen“. Grund: 2020-OS-B1b liest D(3|0) gegen B(0|2); Fehlerquelle „Koordinaten vertauschen“ beim Scheitelpunkt in 2021-OS-B1d (S(−1|−2)) und 2018-OS-K5b.
- 1.5 Punkte mit negativen Koordinaten eintragen (vier Quadranten) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Gerade durch zwei Punkte zeichnen“ · „Wertetabelle als Punkte darstellen“. Grund: A(−2|6) und B(3|−1,5) eintragen in 2025-OS-K5a, K(−4|−1) in 2017-OS-K5a; Punkte mit negativem x in 2021-GYM-K3a.
- 1.6 Quadrant eines Punktes angeben → kein P10-Typ
- 1.7 Lage zu den Achsen erkennen: Punkt auf der Rechtsachse, auf der Hochachse, im Ursprung (P10-Form) → „Lage eines Punktes zu den Achsen erkennen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „auf der x-Achse (y = 0), der y-Achse (x = 0) oder im Ursprung“; Original 2020-OS-B1b.
- 1.8 Figur nach gegebenen Koordinaten zeichnen und benennen → kein P10-Typ
- 1.9 fehlende Ecke eines Rechtecks oder Parallelogramms ergänzen → kein P10-Typ
- 1.10 Streckenlänge parallel zu einer Achse abzählen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge aus Koordinaten berechnen“ · „Flächeninhalt eines Dreiecks aus Koordinaten berechnen“ · „Umfang eines Dreiecks aus Koordinaten berechnen“. Grund: Achsenparallele Katheten AB = 2 und AC = 4 in 2019-OS-K2d; Grundseite und Höhe parallel zu den Achsen in 2016-GYM-K2e und 2024-GYM-B1a, Seiten OP = 2 und PR = 5 in 2015-GYM-K2c.
- 1.11 Fehler finden (Koordinaten vertauscht; Punkt auf der Hochachse für einen auf der Rechtsachse gehalten) → kein P10-Typ
- 1.12 Begründen (warum bei einem Punkt auf der Rechtsachse die zweite Koordinate null ist) → kein P10-Typ

**Einheit 2 · Achsensymmetrie und Spiegeln** – P10-Jahrgänge 4 von 13 (davon Haupt 4); P10-Typen 2; Summe ertrag 7.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Symmetrieachsen bestimmen | 6 | 3 | 3 | 2021 | 2025 | 2 | 1 |  |
| Figur nach Spiegelung benennen | 1 | 1 | 1 | 2018 | 2018 | 1 | 0 |  |

- 2.1 Symmetrieachse einer Figur einzeichnen → „Symmetrieachsen bestimmen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Definition „Anzahl oder Lage der Symmetrieachsen einer Figur angeben“.
- 2.2 prüfen, ob eine eingezeichnete Gerade Symmetrieachse ist (falten oder messen) → „Symmetrieachsen bestimmen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Beim Zählen wird jede mögliche Achse geprüft; Fehlerquelle „waagerechte Achse wie beim Rechteck“ in 2022-OS-B1i.
- 2.3 Anzahl der Symmetrieachsen einer Figur angeben (P10-Form: Quadrat, Rechteck, Raute, gleichschenkliges Trapez, Drachenviereck, gleichseitiges und gleichschenkliges Dreieck, Kreis, Buchstaben, Verkehrszeichen) → „Symmetrieachsen bestimmen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Definition „Anzahl … der Symmetrieachsen“; 2022-OS-B1i (Trapez), 2021-OS-B1j (Quadrat), 2025-OS-K2a (Drachenviereck).
- 2.4 Figuren ohne Symmetrieachse erkennen (Parallelogramm) → „Symmetrieachsen bestimmen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Die Anzahl null ist eine der Ankreuzoptionen 0 bis 5 in 2021-OS-B1j und 2022-OS-B1i (Definition „Anzahl … angeben“).
- 2.5 Punkt an einer Geraden spiegeln (Kästchen abzählen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabel an der y-Achse spiegeln“. Grund: 2020-OS-K3d: der Scheitel (−2|−4) wird an der y-Achse zu (2|−4) gespiegelt.
- 2.6 Figur an einer senkrechten oder waagerechten Geraden spiegeln → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabel an der y-Achse spiegeln“. Grund: Definition „Spiegelbild einer Parabel … an der y-Achse skizzieren“; 2020-OS-K3d verlangt die Skizze.
- 2.7 Figur an einer schrägen Achse spiegeln (Vorrat) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen“. Grund: Definition „durch Spiegelung an der Geraden y=x skizzieren“; 2020-GYM-K3b.
- 2.8 Figur an einer Koordinatenachse spiegeln und die Koordinaten des Bildpunkts angeben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabel an der y-Achse spiegeln“ · „Parabel an der x-Achse spiegeln“ · „Gerade an der x-Achse spiegeln“ · „Graph einer Exponentialfunktion an der y-Achse spiegeln“. Grund: Spiegelbild an einer Koordinatenachse mit Bildpunkt: 2020-OS-K3d (Scheitel (2|−4)), Definition „Parabel an der x-Achse spiegeln“ (Scheitel-y-Wert wechselt, Graph in 2023-GYM-K3c), Spiegelbild zeichnen in 2014-GYM-K2b und 2018-GYM-K2c.
- 2.9 halbe Figur zur achsensymmetrischen ergänzen → kein P10-Typ
- 2.10 die Figur aus Dreieck und Spiegelbild benennen (P10-Form: Drachenviereck, bei gleichschenkligem Dreieck Raute) → „Figur nach Spiegelung benennen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „welche Figur beim Spiegeln … zusammen mit dem Urbild entsteht“; Original 2018-OS-B1h.
- 2.11 Symmetrie der Vierecksarten im Haus der Vierecke zuordnen → „Symmetrieachsen bestimmen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Achsenzahl von Vierecksarten: gleichschenkliges Trapez 2022-OS-B1i, Quadrat 2021-OS-B1j, Drachenviereck 2025-OS-K2a.
- 2.12 Symmetrieachse als Diagonale nutzen (Drachenviereck: die Achse halbiert die andere Diagonale senkrecht; Voraussetzung in pythagoras.md) → „Symmetrieachsen bestimmen“ · „Figur nach Spiegelung benennen“ – P10-Jahrgänge 4 (Haupt 4). Außerhalb der Themen des Eintrags (zählt nicht): „Pythagoras Hypotenuse“ · „Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen“. Grund: 2025-OS-K2a: Achse BD, AF = AC : 2 für die Hypotenuse AB (Fehlerquelle AF = 50 cm); 2018-OS-B1h begründet das Drachenviereck mit der halbierten Diagonale; 2017-GYM-K3b halbiert die 15-m-Diagonale.
- 2.13 Fehler finden (beim Trapez eine zweite, waagerechte Achse angenommen; beim Quadrat nur die zwei Mittelsenkrechten gezählt; Spiegelpunkt nicht senkrecht zur Achse) → kein P10-Typ
- 2.14 Begründen (warum das Parallelogramm keine Symmetrieachse hat, obwohl es „gleichmäßig“ aussieht) → kein P10-Typ

**Einheit 3 · Punktsymmetrie, Drehung, Verschiebung** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 3.1 Punkt an einem Punkt spiegeln (Symmetriezentrum, gleicher Abstand auf der Geraden durch das Zentrum) → kein P10-Typ
- 3.2 Figur am Punkt spiegeln → kein P10-Typ
- 3.3 prüfen, ob eine Figur punktsymmetrisch ist → kein P10-Typ
- 3.4 Punktsymmetrie als halbe Drehung erkennen → kein P10-Typ
- 3.5 Figur um einen Punkt drehen (Vierteldrehung, halbe Drehung, Dreivierteldrehung) → kein P10-Typ
- 3.6 drehsymmetrische Figuren erkennen und den Drehwinkel angeben (Vorrat) → kein P10-Typ
- 3.7 Figur mit einem Pfeil verschieben (Länge und Richtung) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabel verschieben“. Grund: 2015-OS-B1i: Scheitel der Normalparabel um 2 nach rechts, S(2|0) (Definition „oder nur den neuen Scheitelpunkt nennen“); ebenso 2017-GYM-K2b.
- 3.8 Verschiebung im Koordinatensystem beschreiben (so viele Kästchen nach rechts, so viele nach oben) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabeltransformation gegenüber der Normalparabel beschreiben“. Grund: Definition „beschreiben, durch welche Verschiebung … eine Parabel aus der Normalparabel entstanden ist“; 2022-GYM-K3a (2,5 nach rechts, 1 nach unten).
- 3.9 Bandornament fortsetzen (Verschiebung, Spiegelung) → kein P10-Typ
- 3.10 Parkett aus einer Figur legen und die Abbildung benennen → kein P10-Typ
- 3.11 Original und Bild vergleichen: Längen und Winkel bleiben gleich, kongruente Figuren → kein P10-Typ
- 3.12 Abbildung benennen, die zwei gegebene Figuren ineinander überführt → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Graph einer Exponentialfunktion an der y-Achse spiegeln“ · „Parabeltransformation gegenüber der Normalparabel beschreiben“. Grund: 2025-GYM-K3f benennt die Spiegelung an der y-Achse, die f in g überführt; 2022-GYM-K3a die Verschiebung der Normalparabel.
- 3.13 Fehler finden (Drehung mit Spiegelung verwechselt; beim Verschieben nur eine Ecke verschoben; Punktspiegelung als Achsenspiegelung gezeichnet) → kein P10-Typ
- 3.14 Begründen (warum Original und Bild bei allen drei Abbildungen deckungsgleich sind, obwohl die Lage anders ist) → kein P10-Typ

### strahlensaetze

themen.csv: „Maßstab“ – Vermerk: „Maßstab als proportionale Zuordnung; bis 27.09.2026 bei zuordnungen, katalog/index.md führt ihn bei strahlensaetze Einheit 1“.

**Einheit 1 · Maßstab** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 2; Summe ertrag 9.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Länge im Maßstab umrechnen | 4 | 2 | 2 | 2015 | 2018 | 0 | 2 |  |
| Draufsicht maßstabsgerecht zeichnen | 5 | 1 | 1 | 2021 | 2021 | 0 | 1 |  |

- 1.1 Maßstab lesen und in Worten sagen (1 : 200 – ein Zentimeter auf dem Plan sind 200 cm = 2 m) → „Länge im Maßstab umrechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Vorstufe des Umrechnens (Definition „mit einem gegebenen Maßstab“); 2018-OS-K6c mit 1 : 50.
- 1.2 Vergrößerungs- gegen Verkleinerungsmaßstab unterscheiden (5 : 1 gegen 1 : 5) → kein P10-Typ
- 1.3 Länge von der Wirklichkeit in die Zeichnung umrechnen: durch n teilen, vorher in cm umrechnen (Zaun 4 m bei 1 : 200 → 2 cm) → „Länge im Maßstab umrechnen“ · „Draufsicht maßstabsgerecht zeichnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Vieleck aus Seiten und Winkeln im Maßstab konstruieren“. Grund: 2018-OS-K6c (30 m : 50 = 60 cm) und 2017-GYM-K3a (850 cm : 250); in der Draufsicht 2021-OS-K4c 55 cm → 5,5 cm, im GYM-Typ 30 m → 6 cm bei 1 : 500 (2021-GYM-K4a).
- 1.4 Länge von der Zeichnung in die Wirklichkeit: mal n, Ergebnis in eine sinnvolle Einheit (3 cm bei 1 : 200 → 600 cm = 6 m) → „Länge im Maßstab umrechnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Maße aus Netz im Maßstab ablesen“. Grund: 2015-OS-K6a (0,68 m · 10 = 6,8 m); Definition des GYM-Typs „durch Ausmessen der Zeichnung und Umrechnen über den Maßstab“ (2020-GYM-K5b, mal 3).
- 1.5 Modellmaße aus Originalmaßen (h = 30 m, 1 : 50 → 60 cm; P10-Form) und Originalmaße aus Modellmaßen (0,68 m bei 1 : 10 → 6,8 m; P10-Form) → „Länge im Maßstab umrechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „Originalmaße … in Modellmaße umrechnen (oder umgekehrt)“; 2018-OS-K6c und 2015-OS-K6a.
- 1.6 zwei Größen in einer Aufgabe umrechnen (Höhe und Durchmesser) → „Länge im Maßstab umrechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2018-OS-K6c (Höhe und Durchmesser) und 2015-OS-K6a (Höhe und Grundkante; Fehlerquelle „nur eine der beiden Größen“).
- 1.7 Maßstab aus zwei Längen bestimmen (3 cm zu 12 m → 1 : 400) → kein P10-Typ
- 1.8 Kästchenmaßstab eines Rasters lesen (ein Kästchen ≙ 2 cm; Voraussetzung in koerper.md) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Netz eines Prismas vervollständigen“. Grund: 2020-OS-K5a (15 cm als 7,5 Kästchen, ein Kästchen ≙ 2 cm) und 2019-OS-K4a (1,50 m als 5 Kästchen, ein Kästchen ≙ 0,3 m).
- 1.9 Figur auf Karo vergrößern und verkleinern (jede Seite mal 2, mal 3, halbieren) → kein P10-Typ
- 1.10 Rechteck und Kreis im gegebenen Maßstab zeichnen (Durchmesser umrechnen, Radius halbieren, Zirkel) → „Draufsicht maßstabsgerecht zeichnen“ · „Länge im Maßstab umrechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2021-OS-K4c: Rechteck 5,5 cm × 8 cm und Kreis d = 5,8 cm; 2017-GYM-K3a zeichnet eine Figur im gegebenen Maßstab 1 : 250.
- 1.11 Draufsicht eines Körpers als Figur erkennen (Zylinder → Kreis, Quader → Rechteck, Turm auf Platte → Kreis im Rechteck) → „Draufsicht maßstabsgerecht zeichnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2021-OS-K4c: Draufsicht der Regentonne auf der Platte als Kreis im Rechteck.
- 1.12 Maßstab für ein Zeichenfeld wählen (passt 1 : 5, 1 : 10 oder 1 : 20 ins Feld?), angeben und die Zeichnung beschriften (P10-Form) → „Draufsicht maßstabsgerecht zeichnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Körper im Schrägbild darstellen“. Grund: Definition „passenden Maßstab wählen und angeben, Zeichnung beschriften“ (2021-OS-K4c, Fehlerquelle 1 : 5 passt nicht ins Feld); Schrägbild im selbst gewählten Maßstab in 2019-GYM-K4a.
- 1.13 an der Zeichnung entscheiden (bedeckt die Platte die Tonne? Überstand ablesen; P10-Form) → „Draufsicht maßstabsgerecht zeichnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2021-OS-K4c: Entscheidung, ob die Platte die Tonne bedeckt, mit Nebentyp „Behauptung prüfen“.
- 1.14 Landkarte: Strecke aus Kartenzentimetern (1 : 25 000 → 1 cm ≙ 250 m) → „Länge im Maßstab umrechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Kontextvariante der Definition „mit einem gegebenen Maßstab … umrechnen (oder umgekehrt)“; kein Original mit Landkarte.
- 1.15 Fehler finden (mal statt geteilt; Einheit nicht umgerechnet; Radius statt Durchmesser gezeichnet; Maßstab passt nicht ins Feld) → kein P10-Typ
- 1.16 Begründen (warum 1 : 100 eine kleinere Zeichnung ergibt als 1 : 50; warum eine Fläche im Maßstab 1 : 10 nicht ein Zehntel, sondern ein Hundertstel so groß ist) → kein P10-Typ

**Einheit 2 · Zentrische Streckung und Ähnlichkeit** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 2.1 Figur auf Karo vom Zentrum in einer Ecke aus mit k = 2 und k = 3 strecken → kein P10-Typ
- 2.2 Zentrum außerhalb der Figur: Strahlen vom Zentrum durch die Ecken, Abstände mal k abtragen, Bildpunkte A′, B′, C′ → kein P10-Typ
- 2.3 Verkleinern mit k = 0,5 und k = 1/3 → kein P10-Typ
- 2.4 Eigenschaften prüfen: Bildseiten parallel, alle Seiten k-mal so lang, Winkel gleich → kein P10-Typ
- 2.5 Streckfaktor aus einer Original- und Bildstrecke berechnen (k = Bildstrecke : Originalstrecke) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge über Ähnlichkeit berechnen“. Grund: 2021-GYM-K5b: Streckfaktor 13,7 : t aus Füllhöhe und Kegelhöhe.
- 2.6 Zentrum aus Original und Bild finden (Strahlen durch entsprechende Punkte schneiden; Vorrat) → kein P10-Typ
- 2.7 ähnliche Figuren erkennen (gleiche Winkel und gleiche Verhältnisse gegen „nur eine Seite gestreckt“) → kein P10-Typ
- 2.8 ähnliche Dreiecke erkennen an zwei gleichen Winkeln (dritter folgt aus der Winkelsumme) → kein P10-Typ
- 2.9 entsprechende Seiten paaren (gegenüber dem gleichen Winkel) und Verhältnisse prüfen → kein P10-Typ
- 2.10 fehlende Seite in ähnlichen Dreiecken über die Verhältnisgleichung → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge über Ähnlichkeit berechnen“. Grund: Definition „über die Ähnlichkeit von großem und kleinem Kegel bestimmen“; 2021-GYM-K5b und 2023-GYM-K6c.
- 2.11 zwei ähnliche rechtwinklige Dreiecke messen und das Verhältnis Gegenkathete zu Hypotenuse vergleichen (Grundvorstellungs-Geber für trigonometrie.md) → kein P10-Typ
- 2.12 Fläche der Bildfigur: mal k² (Vorrat) → kein P10-Typ
- 2.13 Modell eines Körpers maßstäblich vergrößern, Kanten und Flächen (Modellbau, RLP G; Vorrat) → kein P10-Typ
- 2.14 Fehler finden (Streckfaktor als Differenz; Seiten falsch gepaart; Fläche mal k statt k²) → kein P10-Typ
- 2.15 Begründen (warum zwei Winkel für ähnliche Dreiecke genügen; warum alle Quadrate ähnlich sind, aber nicht alle Rechtecke) → kein P10-Typ

**Einheit 3 · Strahlensätze** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 3.1 Strahlensatzfigur erkennen: Zentrum, zwei Geraden, zwei Parallelen (V-Figur und X-Figur) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge über Ähnlichkeit berechnen“. Grund: Teilschritt: 2023-GYM-K6c nutzt die V-Figur aus Dreieck und paralleler Bereichsgrenze, 2021-GYM-K5b den Achsenschnitt des Kegels.
- 3.2 Voraussetzung prüfen: sind die zwei Linien wirklich parallel? → kein P10-Typ
- 3.3 erster Strahlensatz in der V-Figur: Abschnitte vom Zentrum aus im selben Verhältnis (ZA : ZA′ = ZB : ZB′) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge über Ähnlichkeit berechnen“. Grund: 2021-GYM-K5b: Abschnitt auf der Mantellinie s · 13,7 : t im Verhältnis der Abschnitte auf der Achse.
- 3.4 zweiter Strahlensatz: Parallelen wie die Abschnitte vom Zentrum (AB : A′B′ = ZA : ZA′) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge über Ähnlichkeit berechnen“. Grund: 2023-GYM-K6c: Breite 80 · (1 − 30 : 100) = 56 m an der parallelen Bereichsgrenze.
- 3.5 X-Figur mit denselben Sätzen → kein P10-Typ
- 3.6 Verhältnisgleichung aufstellen, gesuchte Strecke allein auf eine Seite, ausrechnen (auch Dezimalzahlen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge über Ähnlichkeit berechnen“. Grund: Rechenweg beider Originale 2021-GYM-K5b (13,7 cm und 15,03 cm) und 2023-GYM-K6c.
- 3.7 Abschnitt gesucht, wenn die Gesamtstrecke gegeben ist (ZA′ = ZA + AA′; Teilstrecke berechnen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge über Ähnlichkeit berechnen“. Grund: 2021-GYM-K5b: Abstand der Markierung vom oberen Rand als s − s · 13,7 : t; 2023-GYM-K6c mit 100 m − 30 m vom Zentrum.
- 3.8 Sachaufgabe mit Skizze: Höhe eines Baums aus Schatten und Stab, Breite eines Flusses aus Peilung, Försterdreieck, Lochkamera, Leiter an der Wand → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Streckenlänge über Ähnlichkeit berechnen“. Grund: Sachkontexte Messbecher (2021-GYM-K5b) und Wohngebiet (2023-GYM-K6c) mit Skizze.
- 3.9 Strecke in n gleiche Teile teilen (Vorrat) → kein P10-Typ
- 3.10 Umkehrung des ersten Strahlensatzes: aus gleichen Verhältnissen auf Parallelität schließen (Vorrat; die Umkehrung des zweiten gilt nicht) → kein P10-Typ
- 3.11 Fehler finden (Abschnitt nicht vom Zentrum aus gemessen; Parallele mit Strahlabschnitt in einer Gleichung gemischt; nicht parallele Linien; Verhältnisgleichung falsch umgestellt) → kein P10-Typ
- 3.12 Begründen (warum die Strahlensätze aus der zentrischen Streckung folgen; warum der Schatten eines Baums zur Höhe eines Stabs passt – gleiche Sonnenstrahlen sind parallel) → kein P10-Typ

### zuordnungen

themen.csv: „Zuordnungen proportional und antiproportional“.

**Einheit 1 · Zuordnungen darstellen** – P10-Jahrgänge 5 von 13 (davon Haupt 5); P10-Typen 3; Summe ertrag 17.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Wertetabelle als Punkte darstellen | 5 | 2 | 4 | 2016 | 2025 | 0 | 2 |  |
| Achseneinteilung wählen | 8 | 2 | 3 | 2016 | 2021 | 0 | 2 |  |
| Graph zu Tarif zuordnen | 4 | 2 | 2 | 2016 | 2023 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |

- 1.1 Wertetabelle aus Text anlegen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Endwert linearer Veränderung berechnen“ · „Graph eines exponentiellen Vorgangs zeichnen“. Grund: In 2021-OS-K6a sind leere Tabellenfelder aus dem Text zu füllen (Anfangshöhe 40 cm, Höhe nach 80 min), in 2014-GYM-K4b entstehen die Wertepaare aus der Vorschrift „Halbierung je Stunde“ (Definition „aus einer Wertetabelle oder Rekursionsvorschrift“).
- 1.2 Punkte ins Koordinatensystem eintragen → „Wertetabelle als Punkte darstellen“ – P10-Jahrgänge 4 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Graph eines exponentiellen Vorgangs zeichnen“. Grund: Definition „Wertepaare einer Tabelle in ein vorgegebenes Koordinatensystem eintragen“ (2025-OS-K7a, 2021-OS-K6b); Kontextvariante Zerfall in 2014-GYM-K4b.
- 1.3 Werte aus Graph ablesen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wert aus Diagramm ablesen“ · „Nullstelle am Graphen ablesen“. Grund: Definition „Einzelwert … aus einem Funktionsgraphen im Sachzusammenhang (z. B. Startwert bei t = 0) … ablesen“; 2015-OS-K4a liest am Höhe-Zeit-Graphen die Absprunghöhe und als Nullstelle die Zeit bis zur Landung ab.
- 1.4 Achseneinteilung für gegebene Werte wählen → „Achseneinteilung wählen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Definition „für ein Kästchenraster ohne Skala eine Achseneinteilung wählen, mit der alle Werte einer Tabelle darstellbar sind“; Originale 2021-OS-K6b, 2016-OS-K4b, 2017-OS-K7b.
- 1.5 Zuordnung in Worten beschreiben („je mehr …, desto …“) → kein P10-Typ
- 1.6 Graph zu Situation qualitativ zuordnen (Füllgraph, Weg-Zeit) → „Graph zu Tarif zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Graph zu Wachstumsprozess zuordnen“. Grund: Beide verlangen zu einer beschriebenen Situation den qualitativ passenden Graphen (Definitionen; 2016-OS-K6a und 2023-OS-K3a für Tarife, 2019-OS-K7c und 2026-FOR-K7b für Wachstum).
- 1.7 Formel aus Tabelle (y = 4 · x) → kein P10-Typ
- 1.8 Fehler finden (Achsen vertauscht, Punkt falsch gesetzt) → kein P10-Typ
- 1.9 Begründen → kein P10-Typ

**Einheit 2 · Proportionale Zuordnungen und Dreisatz** – P10-Jahrgänge 6 von 13 (davon Haupt 5); P10-Typen 2; Summe ertrag 8.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Proportionale Zuordnung Dreisatz | 3 | 3 | 3 | 2016 | 2023 | 3 | 0 |  |
| Wertetabelle als Punkte darstellen | 5 | 2 | 4 | 2016 | 2025 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |

- 2.1 Tabelle ergänzen durch Verdoppeln und Halbieren → „Proportionale Zuordnung Dreisatz“ – P10-Jahrgänge 3 (Haupt 3). Grund: Vorstufe des Dreisatzes mit den Faktoren 2 und ½ (Definition „aus einem Wertepaar den fehlenden vierten Wert“).
- 2.2 Hochrechnen (mal 3, mal 10) → „Proportionale Zuordnung Dreisatz“ – P10-Jahrgänge 3 (Haupt 3). Grund: Vorstufe des Dreisatzes mit ganzzahligem Faktor (Definition „aus einem Wertepaar den fehlenden vierten Wert“).
- 2.3 Runterrechnen → „Proportionale Zuordnung Dreisatz“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2016-OS-B1d: Fett in 20 g aus 30 g in 100 g durch Runterrechnen (30 : 5).
- 2.4 auf eine Portion runterrechnen, dann hochrechnen (Dreisatz, Minitabelle) → „Proportionale Zuordnung Dreisatz“ – P10-Jahrgänge 3 (Haupt 3). Grund: Lösungsweg der Originale 2023-OS-B1a (25 : 4 = 6,25 min je km, mal 6) und 2022-OS-B1b (4,80 : 3 = 1,60 € je kg, mal 5).
- 2.5 fester Faktor angeben (Preis je Einheit), Gleichung y = k · x → „Proportionale Zuordnung Dreisatz“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Funktion aus Sachverhalt aufstellen“. Grund: Fester Faktor als Lösungsweg des Dreisatzes in 2016-OS-B1d („0,3 · 20“); die Gleichung y = k · x ist der Grundfall ohne Anfangswert von „Lineare Funktion aus Sachverhalt aufstellen“ (Definition „Anfangswert und konstante Änderung je Einheit“).
- 2.6 Preisvergleich über gleiche Portion → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Tarife vergleichen“. Grund: Definition „Gesamtkosten zweier Tarife … für eine konkrete Nutzung berechnen und den günstigeren wählen“: der Vergleich läuft über dieselbe Menge (2023-OS-K3b: 5 Tage und 470 km; 2017-GYM-K5b: 1000 kWh).
- 2.7 Graph zeichnen (Ursprungsgerade) und Werte ablesen → „Wertetabelle als Punkte darstellen“ – P10-Jahrgänge 4 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Wert aus Diagramm ablesen“. Grund: Zeichnen über eingetragene Wertepaare (Definition „Wertepaare einer Tabelle … eintragen“, in 2021-OS-K6b zur Strecke verbunden) und Ablesen am Funktionsgraphen im Sachzusammenhang (Definition „Wert aus Diagramm ablesen“, 2015-OS-K4a).
- 2.8 Verhältnisgleichung aufstellen (Vorrat) → kein P10-Typ
- 2.9 Fehler finden (Wert für eine Portion falsch; addiert statt multipliziert) → kein P10-Typ
- 2.10 Begründen (warum links und rechts dasselbe) → kein P10-Typ

**Einheit 3 · Antiproportionale Zuordnungen** – P10-Jahrgänge 4 von 13 (davon Haupt 2); P10-Typen 2; Summe ertrag 5.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Antiproportionale Zuordnung Dreisatz | 0 | 0 | 0 |  |  | 0 | 0 | nur GYM |
| Wertetabelle als Punkte darstellen | 5 | 2 | 4 | 2016 | 2025 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |

- 3.1 Tabelle ergänzen: doppelt → halb, dreifach → Drittel → „Antiproportionale Zuordnung Dreisatz“ – P10-Jahrgänge 0 (Haupt 0). Grund: 2014-GYM-B1c: doppelt so viele Pferde, halb so viele Tage (Vorrat für 4 Pferde 8 Tage, für 8 Pferde 4 Tage).
- 3.2 Produkt prüfen (x · y gleich) → „Antiproportionale Zuordnung Dreisatz“ – P10-Jahrgänge 0 (Haupt 0). Grund: Definition „über das konstante Produkt“; 2014-GYM-B1c rechnet 4 · 8 = 32 Pferdetage.
- 3.3 Dreisatz umgekehrt (auf eine Einheit hochrechnen, dann runter) → „Antiproportionale Zuordnung Dreisatz“ – P10-Jahrgänge 0 (Haupt 0). Grund: 2014-GYM-B1c: auf ein Pferd hochrechnen (32 Tage), dann durch 8 teilen.
- 3.4 Sachtext (Arbeiter und Tage, Pumpen und Stunden, Geschwindigkeit und Fahrzeit bei fester Strecke) → „Antiproportionale Zuordnung Dreisatz“ – P10-Jahrgänge 0 (Haupt 0). Grund: Definition „Vorrat für mehr oder weniger Personen oder Tiere“; Sachtext Futtervorrat in 2014-GYM-B1c.
- 3.5 Graph als fallende Kurve, Werte ablesen → „Wertetabelle als Punkte darstellen“ – P10-Jahrgänge 4 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Wert aus Diagramm ablesen“. Grund: Punkte einer Tabelle eintragen und zur fallenden Kurve verbinden verlangen 2016-OS-K4b und 2017-OS-K7b (Nebentyp „Wertetabelle als Punkte darstellen“); Ablesen nach Definition „Wert aus Diagramm ablesen“ (Funktionsgraph im Sachzusammenhang).
- 3.6 Fehler finden (proportional gerechnet) → kein P10-Typ
- 3.7 Begründen (warum das Produkt gleich bleibt) → kein P10-Typ

**Einheit 4 · Zuordnungstypen erkennen und anwenden** – P10-Jahrgänge 7 von 13 (davon Haupt 6); P10-Typen 4; Summe ertrag 21.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Kosten aus Menge und Preis berechnen | 4 | 2 | 3 | 2014 | 2026 | 0 | 3 |  |
| Geschwindigkeit aus Weg und Zeit berechnen | 2 | 1 | 1 | 2015 | 2015 | 0 | 1 |  |
| Dauer aus Menge und Rate berechnen | 11 | 4 | 4 | 2014 | 2024 | 0 | 4 |  |
| Graph zu Tarif zuordnen | 4 | 2 | 2 | 2016 | 2023 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |

- 4.1 Zuordnungstyp aus Tabelle (Quotient oder Produkt prüfen) → kein P10-Typ
- 4.2 aus Text (je mehr, desto mehr – reicht nicht: Nullwert prüfen) → „Graph zu Tarif zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2016-OS-K6a: aus dem Text „ohne Grundpreis“ auf die Ursprungsgerade schließen, der Tarif mit 200 € Grundpreis beginnt nicht bei null (Definition „mit oder ohne Grundpreis“).
- 4.3 aus Graph (Ursprungsgerade, fallende Kurve, andere) → „Graph zu Tarif zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Graph einer linearen Funktion erkennen“. Grund: Ursprungsgerade gegen Gerade mit Achsenabschnitt in 2016-OS-K6a; unter Gerade, Hyperbelast, Parabel und Streckenzug die Gerade wählen in 2025-OS-B1f.
- 4.4 Gegenbeispiele (Alter und Größe, Tarif mit Grundgebühr) → „Graph zu Tarif zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „auch bei rein linearen Tarifen (mit oder ohne Grundpreis)“: der Tarif mit Grundgebühr ist das Gegenbeispiel zur proportionalen Zuordnung (2016-OS-K6a, 2023-OS-K3a).
- 4.5 Kosten aus Menge und Preis je Einheit → „Kosten aus Menge und Preis berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Definition „Gesamtpreis aus einer … Menge und einem Einheitspreis“; 2014-OS-K4c, 2024-OS-K2d.
- 4.6 Geschwindigkeit aus Weg und Zeit mit Einheitenwechsel → „Geschwindigkeit aus Weg und Zeit berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „… in die verlangte Einheit (m/s, km/h) umrechnen“; 2015-OS-K4c (5 m/s = 18 km/h).
- 4.7 Dauer aus Menge und Rate, Zeiteinheit umrechnen → „Dauer aus Menge und Rate berechnen“ – P10-Jahrgänge 4 (Haupt 4). Außerhalb der Themen des Eintrags (zählt nicht): „Zeiteinheiten umrechnen“. Grund: Definition „in die verlangte Zeiteinheit umrechnen“; 2024-OS-K6c und 2015-OS-K3c tragen „Zeiteinheiten umrechnen“ als Nebentyp (120 s = 2 min).
- 4.8 Fehler finden (antiproportional gerechnet; Einheit) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Fehler in Rechnung erklären und korrigieren“. Grund: 2014-OS-K4e: im Aufgabenstamm der Kraftstoffkosten den Einheitenfehler (585 € als 585 000 ct) in der Rechnung „Mehrkosten je Kilometer“ finden und berichtigen.
- 4.9 Begründen (warum nicht proportional) → kein P10-Typ

### terme

themen.csv: „Terme umformen“ – Vermerk: „binomische-formeln stecken hier oder in quadratische Gleichungen“.

**Einheit 1 · Terme aufstellen und berechnen** – P10-Jahrgänge 11 von 13 (davon Haupt 11); P10-Typen 5; Summe ertrag 19.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Term zu Sachtext angeben | 7 | 5 | 5 | 2015 | 2023 | 4 | 1 |  |
| Termwert berechnen | 4 | 3 | 3 | 2016 | 2026 | 4 | 0 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |
| Term zu Figur angeben | 5 | 5 | 5 | 2014 | 2025 | 5 | 0 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |
| Term zu Körper angeben | 3 | 1 | 1 | 2017 | 2017 | 0 | 1 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |
| Term durch Zusammenfassen gleichartiger Glieder vereinfachen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Termwert berechnen (auch negative Einsetzung) → „Termwert berechnen“ · „Term durch Zusammenfassen gleichartiger Glieder vereinfachen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“. Grund: Definition „auch mit negativen Zahlen“ (2026-FOR-B1g, 2021-OS-B1g); derselbe Schritt als Funktionswert, etwa ½ · (−10) + 1 in 2017-OS-K5b, und nach dem Zusammenfassen in 2025-GYM-B2a (Wert für x = 2).
- 1.2 Term zu Sachtext angeben (Doppeltes, vermindert um) → „Term zu Sachtext angeben“ – P10-Jahrgänge 5 (Haupt 5). Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Gleichung aus Sachverhalt aufstellen“. Grund: Definition „Differenz, Doppeltes, verdreifachen, vermindert um“ (2023-OS-B1h, 2017-OS-B1i); dieselbe Übersetzung als Gleichung in 2016-GYM-B1b („das Achtfache einer Zahl vermindert um zwölf“).
- 1.3 Term zu Figur angeben (Umfang, Fläche aus Rechtecken) → „Term zu Figur angeben“ · „Term zu Körper angeben“ – P10-Jahrgänge 6 (Haupt 6). Grund: Definition „Term für Flächeninhalt oder Umfang“ (2025-OS-B1i, 2014-OS-B1g); Kontextvariante am Körper in 2017-OS-K3c und 2022-GYM-B1a (Kantensumme 4 · (3 + 6 + 5)).
- 1.4 Situation zu Term angeben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Gleichung im Sachzusammenhang deuten“ · „Gleichung zu Figur erläutern“. Grund: Definition „eine gegebene Gleichung als Satz im Sachzusammenhang formulieren“ (2024-OS-K7b: „r + t = 13“); zu einer gegebenen Flächengleichung die Zerlegung der Figur erläutern in 2021-GYM-K4d.

**Einheit 2 · Terme zusammenfassen** – P10-Jahrgänge 5 von 13 (davon Haupt 5); P10-Typen 4; Summe ertrag 5.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Term durch Zusammenfassen gleichartiger Glieder vereinfachen | 0 | 0 | 0 |  |  | 0 | 0 | nur GYM |
| Term mit Klammern und Potenzen vereinfachen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Binomische Formel anwenden | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Term zu Figur angeben | 5 | 5 | 5 | 2014 | 2025 | 5 | 0 | nicht in der Zuordnungszeile der Einheit |

- 2.1 gleichartige Glieder zusammenfassen → „Term durch Zusammenfassen gleichartiger Glieder vereinfachen“ · „Term mit Klammern und Potenzen vereinfachen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Gleichung lösen“ · „Lineares Gleichungssystem lösen“. Grund: Definitionen der beiden Termtypen (2025-GYM-B2a: 6x − 4x = 2x; 2022-GYM-B2b); beim Gleichungslösen in 2018-OS-K3b (x + 3x = 400, Nebentyp), 2021-GYM-B1a und nach dem Einsetzen in 2022-OS-K7b (9x − 3x = 6x).
- 2.2 Zusammenfassen mit Potenzen (x, x²) → „Term durch Zusammenfassen gleichartiger Glieder vereinfachen“ · „Term mit Klammern und Potenzen vereinfachen“ – P10-Jahrgänge 0 (Haupt 0). Grund: 2025-GYM-B2a: 6x − 3x² − 4x = 2x − 3x² (x² bleibt getrennt); 2022-GYM-B2b: Ergebnis a² − 9a.
- 2.3 Zahl mal Term → „Binomische Formel anwenden“ – P10-Jahrgänge 0 (Haupt 0). Grund: 2019-GYM-B1f: das Mittelglied 2 · 2a · b = 4ab bilden.
- 2.4 Term mal Term (x · x = x²) → „Binomische Formel anwenden“ · „Term mit Klammern und Potenzen vereinfachen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Scheitelpunktform in Normalform umformen“. Grund: Teilschritt der binomischen Formel: (2a)² = 4a² in 2019-GYM-B1f, x · x = x² in (x + 3)² (2017-OS-K5d) und a · a in (a − 3)² (2022-GYM-B2b).
- 2.5 Fehler finden → kein P10-Typ
- 2.6 Begründen (zusammenfassbar oder nicht) → kein P10-Typ
- 2.7 Term aus Situation aufstellen und zusammenfassen → „Term zu Figur angeben“ – P10-Jahrgänge 5 (Haupt 5). Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Gleichung aus Sachverhalt aufstellen“. Grund: 2014-OS-B1g: Umfangsterm des Kreuzes aufstellen und zu 16a zusammenfassen; 2018-OS-K3b: aus „Pasta = 3 · Salat“ den Term x + 3x bilden und zusammenfassen.

**Einheit 3 · Klammern auflösen** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 1; Summe ertrag 0.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Term mit Klammern und Potenzen vereinfachen | 0 | 0 | 0 |  |  | 0 | 0 | nur GYM |

- 3.1 Plusklammer weglassen → kein P10-Typ
- 3.2 Minusklammer (alle Vorzeichen drehen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Gleichung lösen“. Grund: 2021-GYM-B1a: die rechte Seite −(x + 2) zu −x − 2 auflösen.
- 3.3 Zahl mal Klammer → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Gleichung lösen“ · „Lineares Gleichungssystem lösen“. Grund: Lösungsweg „2x − 8 = 6“ zu 2(x − 4) = 6 in 2020-OS-B1e; nach dem Einsetzen 3 · (63 − x) = 189 − 3x in 2022-OS-K7b und 2,30 · (13 − t) in 2024-OS-K7b.
- 3.4 negative Zahl mal Klammer → „Term mit Klammern und Potenzen vereinfachen“ – P10-Jahrgänge 0 (Haupt 0). Grund: 2022-GYM-B2b: −2 · (a + 4,5) = −2a − 9.
- 3.5 Klammer auflösen und zusammenfassen → „Term mit Klammern und Potenzen vereinfachen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Gleichung lösen“ · „Lineares Gleichungssystem lösen“ · „Scheitelpunktform in Normalform umformen“. Grund: Definition „mehrere Klammern … ausmultiplizieren und so weit wie möglich zusammenfassen“ (2022-GYM-B2b); ebenso 2021-GYM-B1a, 2022-OS-K7b (9x + 189 − 3x) und 2017-OS-K5d (x² + 6x + 9 − 2).
- 3.6 Fehler finden → kein P10-Typ
- 3.7 Begründen (Gleichwertigkeit) → kein P10-Typ

**Einheit 4 · Ausklammern** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 4.1 gemeinsamen Zahlfaktor ausklammern → kein P10-Typ
- 4.2 Variable ausklammern → kein P10-Typ
- 4.3 Zahl und Variable ausklammern → kein P10-Typ
- 4.4 Umkehrung prüfen (ausmultiplizieren als Probe) → kein P10-Typ
- 4.5 Fehler finden → kein P10-Typ

### lineare-gleichungen

themen.csv: „Lineare Gleichungen“.

**Einheit 1 · Gleichungen verstehen** – P10-Jahrgänge 6 von 13 (davon Haupt 6); P10-Typen 2; Summe ertrag 6.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lösung durch Einsetzen prüfen | 3 | 3 | 3 | 2018 | 2025 | 3 | 0 |  |
| Lineare Gleichung lösen | 3 | 3 | 5 | 2018 | 2024 | 3 | 0 | nicht in der Zuordnungszeile der Einheit |

- 1.1 Lösung durch Einsetzen prüfen (wA/fA) → „Lösung durch Einsetzen prüfen“ – P10-Jahrgänge 3 (Haupt 3). (wortgleich)
- 1.2 Lösung durch Probieren finden → „Lösung durch Einsetzen prüfen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Probieren mit vorgegebenen Kandidaten: 2022-OS-B1c (x = 2, 4, 6, 8 einsetzen), Definition „Vorgegebene Werte … einsetzen und die Lösung auswählen“.
- 1.3 Gleichung mit Umkehroperation lösen → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Ausgangswert aus Differenz berechnen“. Grund: Definition „den Ausgangswert durch Umkehroperation berechnen“ (2017-OS-K2a: 682 069 − 8 512); als Vorstufe des Lösens geht 2(x − 4) = 6 in 2020-OS-B1e rückwärts (6 : 2 = 3, 3 + 4 = 7, Lösungsweg „x − 4 = 3“).
- 1.4 richtig/falsch entscheiden ohne Rechnung → kein P10-Typ

**Einheit 2 · Äquivalenzumformungen** – P10-Jahrgänge 5 von 13 (davon Haupt 3); P10-Typen 1; Summe ertrag 3.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lineare Gleichung lösen | 3 | 3 | 5 | 2018 | 2024 | 3 | 0 |  |

- 2.1 einschrittig (+, −, ·, :) → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Grund: Grundfall des Verfahrens (Definition „Eine lineare Gleichung mit einer Unbekannten lösen“), letzter Schritt jedes Originals, etwa 2x = 14 in 2020-OS-B1e.
- 2.2 zweischrittig (erst Strich, dann Punkt) → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Nullstelle lineare Funktion berechnen“. Grund: 2020-OS-B1e (2x − 8 = 6); die Nullstelle führt auf eine zweischrittige Gleichung 0 = −2x + 3 (2022-OS-K3a) bzw. 0 = −0,2x + 40 (2021-OS-K6d).
- 2.3 negative Lösung → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Grund: 2021-GYM-B1a: Lösung x = −2.
- 2.4 negative Vorzahl (−4x = 20) → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Nullstelle lineare Funktion berechnen“. Grund: 2021-GYM-B1a (−9x = 18 nach dem Zusammenfassen); 0 = −2x + 3 in 2022-OS-K3a und 0 = −0,2x + 40 in 2021-OS-K6d.
- 2.5 Vorzahl als Bruch (x/5 = 3) → kein P10-Typ
- 2.6 Umformung anschreiben (Vorstufe, s. Voraussetzungen) → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Grund: Vorstufe des Verfahrens (Katalog: Blatt 0): die Umformung hinter dem Strich notieren, Teil jeder Lösung mit Äquivalenzumformungen (2020-OS-B1e, 2023-OS-B1e).
- 2.7 Fehler finden (falsche Umkehroperation) → kein P10-Typ
- 2.8 Begründen (warum darf man auf beiden Seiten …) → kein P10-Typ
- 2.9 Gleichung mit Lösungsvorgabe aufstellen (Umkehrung) → kein P10-Typ

**Einheit 3 · Gleichungen mit x auf beiden Seiten, Klammern, Brüchen und Dezimalzahlen; Sonderfälle keine/alle Lösungen.** – P10-Jahrgänge 5 von 13 (davon Haupt 3); P10-Typen 1; Summe ertrag 3.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lineare Gleichung lösen | 3 | 3 | 5 | 2018 | 2024 | 3 | 0 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |

- 3.1 x beidseitig → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Lage zweier Geraden bestimmen“. Grund: 2021-GYM-B1a (−10x − 20 = −x − 2); Schnittpunkt aus −0,5x + 2 = 0,5x in 2023-GYM-B1b.
- 3.2 erst zusammenfassen → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Lineares Gleichungssystem lösen“. Grund: Vor dem Umformen zusammenfassen: x + 3x = 400 in 2018-OS-K3b (Nebentyp „Lineare Gleichung lösen“), −10x − 20 in 2021-GYM-B1a, 9x + 189 − 3x in 2022-OS-K7b.
- 3.3 Klammer auflösen (Plus, Minus, Zahl mal Klammer) → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Lineares Gleichungssystem lösen“. Grund: 2020-OS-B1e (2(x − 4) = 6), 2021-GYM-B1a (4 · (−5 − 3x) und −(x + 2)); nach dem Einsetzen 3 · (63 − x) in 2022-OS-K7b.
- 3.4 Brüche (mit Hauptnenner malnehmen) → kein P10-Typ
- 3.5 Dezimalzahlen → „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Lineares Gleichungssystem lösen“ · „Nullstelle lineare Funktion berechnen“. Grund: 2024-OS-B1d (2 · (x − 6,5) = 0), 2022-OS-K7b (6x = 163,20), 2024-OS-K7b (29,9 − 0,6t = 26,90) und 2021-OS-K6d (0 = −0,2x + 40).
- 3.6 keine Lösung / alle Zahlen → kein P10-Typ
- 3.7 Fehler finden → kein P10-Typ
- 3.8 Begründen (Sonderfall erkennen) → kein P10-Typ

**Einheit 4 · Gleichungen aufstellen** – P10-Jahrgänge 5 von 13 (davon Haupt 4); P10-Typen 2; Summe ertrag 8.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lineare Gleichung aus Sachverhalt aufstellen | 5 | 2 | 2 | 2018 | 2020 | 0 | 2 |  |
| Lineare Gleichung lösen | 3 | 3 | 5 | 2018 | 2024 | 3 | 0 | nicht in der Zuordnungszeile der Einheit |

- 4.1 Zahlenrätsel → „Lineare Gleichung aus Sachverhalt aufstellen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Term zu Sachtext angeben“. Grund: Zahlenrätsel als Gleichung: 2016-OS-B1b, 2021-OS-B1e („das Fünffache einer Zahl vermindert um 4 ist gleich 36“) und 2016-GYM-B1b.
- 4.2 Alter, Geld, Verteilung → „Lineare Gleichung aus Sachverhalt aufstellen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Geld in 2020-OS-K2e (12 · (520 + x) = 7920 € Einnahmen), Verteilung in 2018-OS-K3b (1000 Befragte, Pasta = 3 · Salat).
- 4.3 Geometrie (Umfang, Winkel) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Rechteckseite aus Umfang berechnen“. Grund: Definition „durch Umstellen von u = 2a + 2b“; 2018-OS-B1f (b aus u = 26 cm und a = 8 cm).
- 4.4 Formel umstellen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Rechteckseite aus Umfang berechnen“ · „Grundseite aus Dreiecksfläche berechnen“ · „Trapezhöhe aus Fläche berechnen“ · „Höhe eines Zylinders aus Volumen berechnen“ · „Radius eines Zylinders aus Volumen berechnen“ · „Volumen aus Masse und Dichte berechnen“ · „Trigonometrische Gleichung nach Seite umstellen“ · „Kreisringmaß aus Fläche berechnen“ · „Kugelmaß aus Oberfläche berechnen“. Grund: Die Definitionen verlangen das Umstellen einer Formel: u = 2a + 2b (2018-OS-B1f), A = ½ · g · h (2020-OS-K7b), Trapezformel (2014-OS-K5c), Zylindervolumen (2023-OS-K5d, 2022-OS-K2d), ϱ = m : V (2016-OS-K3d), sin α = a/x (2020-OS-B1j), Ringfläche (2023-GYM-K4b) und Halbkugeloberfläche (2022-GYM-K4a).
- 4.5 Gleichung aus Sachverhalt aufstellen und lösen (P10-Form) → „Lineare Gleichung aus Sachverhalt aufstellen“ · „Lineare Gleichung lösen“ – P10-Jahrgänge 5 (Haupt 4). Grund: Definition „… aufstellen, die anschließend gelöst wird“; 2020-OS-K2e und 2018-OS-K3b mit Nebentyp „Lineare Gleichung lösen“.
- 4.6 Deutung der Lösung im Kontext → „Lineare Gleichung aus Sachverhalt aufstellen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Funktion aus Sachverhalt aufstellen“. Grund: Aus der Lösung die gefragten Größen ableiten (2018-OS-K3b: Salat 100, Pasta 300; 2020-OS-K2e: 140 Besucher) und im Kontext runden (2022-OS-K6b: x ≥ 18,4 heißt 19 Monate).

### lineare-funktionen

themen.csv: „Lineare Funktionen“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Gerade an der x-Achse spiegeln“; „Gerade an der y-Achse spiegeln“.

**Einheit 1 · Proportionale Funktion** – P10-Jahrgänge 9 von 13 (davon Haupt 8); P10-Typen 3; Summe ertrag 30.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Graph zu Tarif zuordnen | 4 | 2 | 2 | 2016 | 2023 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |
| Gerade aus Gleichung zeichnen | 16 | 5 | 5 | 2021 | 2026 | 0 | 6 | nicht in der Zuordnungszeile der Einheit |
| Funktionswert berechnen | 10 | 3 | 5 | 2016 | 2026 | 0 | 5 | nicht in der Zuordnungszeile der Einheit |

- 1.1 Proportionalität erkennen (Tabelle, Text) → „Graph zu Tarif zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2016-OS-K6a: aus dem Text erkennen, dass der Tarif ohne Grundpreis proportional ist und zur Ursprungsgeraden gehört (Definition „mit oder ohne Grundpreis“).
- 1.2 Proportionalitätsfaktor bestimmen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Proportionale Zuordnung Dreisatz“. Grund: Fester Faktor als Lösungsweg des Dreisatzes: 0,3 g Fett je Gramm in 2016-OS-B1d („0,3 · 20“).
- 1.3 Graph zeichnen → „Gerade aus Gleichung zeichnen“ – P10-Jahrgänge 5 (Haupt 5). Grund: Die Ursprungsgerade ist der Grundfall n = 0 der Definition „Graph einer linearen Funktion aus der Gleichung mit y-Achsenabschnitt und Steigungsdreieck zeichnen“ (2021-OS-K2a).
- 1.4 Wert ablesen und berechnen → „Funktionswert berechnen“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Wert aus Diagramm ablesen“. Grund: Berechnen nach Definition „Wert einer Funktion für ein gegebenes Argument“ (2017-OS-K5b), Ablesen nach Definition „aus einem Funktionsgraphen im Sachzusammenhang“ (2015-OS-K4a).
- 1.5 Dreisatz als Kontrolle → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Proportionale Zuordnung Dreisatz“. Grund: Definition „aus einem Wertepaar den fehlenden vierten Wert per Dreisatz“ (2023-OS-B1a, 2022-OS-B1b).

**Einheit 2 · Lineare Funktion f(x) = m·x + n** – P10-Jahrgänge 9 von 13 (davon Haupt 9); P10-Typen 8; Summe ertrag 33.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Gerade aus Gleichung zeichnen | 16 | 5 | 5 | 2021 | 2026 | 0 | 6 |  |
| Geradengleichung zu Graph zuordnen | 3 | 1 | 1 | 2019 | 2019 | 0 | 1 |  |
| Graph einer linearen Funktion erkennen | 1 | 1 | 1 | 2025 | 2025 | 1 | 0 | kein Katalogtyp zugeordnet |
| Graph nach Eigenschaft auswählen | 3 | 2 | 2 | 2016 | 2019 | 1 | 1 |  |
| y-Achsenabschnitt ablesen | 1 | 1 | 1 | 2024 | 2024 | 1 | 0 |  |
| Eigenschaften eines Graphen beurteilen | 5 | 2 | 6 | 2018 | 2026 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |
| Lage zweier Geraden bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Graph zu Tarif zuordnen | 4 | 2 | 2 | 2016 | 2023 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |

- 2.1 n am Graphen ablesen → „y-Achsenabschnitt ablesen“ · „Geradengleichung zu Graph zuordnen“ · „Eigenschaften eines Graphen beurteilen“ – P10-Jahrgänge 7 (Haupt 4). Außerhalb der Themen des Eintrags (zählt nicht): „Wert aus Diagramm ablesen“. Grund: Definition „Schnittpunkt einer Geraden mit der y-Achse … ablesen und markieren“ (2024-OS-B1i); n am Graphen lesen in 2019-OS-K2c (Auswahl über den y-Achsenabschnitt) und 2025-OS-K5a (Aussage „schneidet die y-Achse in (0|3)“); Startwert bei t = 0 in 2015-OS-K4a.
- 2.2 m mit Steigungsdreieck ablesen (auch negativ, auch Bruch) → „Geradengleichung zu Graph zuordnen“ · „Graph nach Eigenschaft auswählen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2019-OS-K2b und 2019-OS-K2c: am Steigungsdreieck von f den Anstieg −2 ablesen (Auswahl mit y = −½x + 2 als Ablenker).
- 2.3 Gerade aus Gleichung zeichnen → „Gerade aus Gleichung zeichnen“ – P10-Jahrgänge 5 (Haupt 5). (wortgleich)
- 2.4 Gleichung zu Graph zuordnen → „Geradengleichung zu Graph zuordnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „zu gezeichneten Geraden aus einer Auswahl die passende Gleichung“; 2019-OS-K2c.
- 2.5 Parameter deuten (steigend, fallend, parallel, Sonderfall m = 0) → „Graph nach Eigenschaft auswählen“ · „Eigenschaften eines Graphen beurteilen“ · „Lage zweier Geraden bestimmen“ – P10-Jahrgänge 7 (Haupt 4). Grund: Fallend und parallel zur x-Achse (m = 0) in 2016-OS-B1c und 2019-OS-K2b, Monotonie aus m in 2021-OS-K2b, parallel bei gleicher Steigung in 2014-GYM-B1i.
- 2.6 Fehler finden (Steigungsdreieck falsch gelesen) → kein P10-Typ
- 2.7 Begründen (ohne Rechnung: welche Gerade steiler) → „Graph zu Tarif zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2016-OS-K6a verlangt die Begründung der Zuordnung; der Graph des Tarifs mit Grundpreis steigt flacher (1,50 € je km gegen 2,00 €).

**Einheit 3 · Punkte und Werte** – P10-Jahrgänge 13 von 13 (davon Haupt 10); P10-Typen 8; Summe ertrag 33.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Nullstelle lineare Funktion berechnen | 2 | 1 | 2 | 2021 | 2022 | 0 | 1 |  |
| Nullstelle am Graphen ablesen | 1 | 1 | 2 | 2015 | 2019 | 0 | 1 | kein Katalogtyp zugeordnet |
| Schnittpunkt am Graphen ablesen | 0 | 0 | 1 | 2023 | 2023 | 0 | 0 | kein Katalogtyp zugeordnet |
| Funktionswert berechnen | 10 | 3 | 5 | 2016 | 2026 | 0 | 5 |  |
| Punktprobe durchführen | 12 | 5 | 7 | 2014 | 2026 | 1 | 5 |  |
| Wertetabelle einer Funktion zuordnen | 2 | 1 | 1 | 2026 | 2026 | 2 | 0 |  |
| y-Achsenabschnitt ablesen | 1 | 1 | 1 | 2024 | 2024 | 1 | 0 | nicht in der Zuordnungszeile der Einheit |
| Eigenschaften eines Graphen beurteilen | 5 | 2 | 6 | 2018 | 2026 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |

- 3.1 Funktionswert berechnen → „Funktionswert berechnen“ – P10-Jahrgänge 5 (Haupt 3). (wortgleich)
- 3.2 Argument zum Funktionswert → „Nullstelle lineare Funktion berechnen“ – P10-Jahrgänge 2 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Gleichung lösen“. Grund: Die Nullstelle ist das Argument zum Funktionswert null (Definition); 2022-OS-K6b: aus 55x + 990 = 2 000 die Monatszahl bestimmen (Nebentyp „Lineare Gleichung lösen“).
- 3.3 Wertetabelle → „Wertetabelle einer Funktion zuordnen“ · „Funktionswert berechnen“ – P10-Jahrgänge 5 (Haupt 4). Grund: Definition „zu einer Funktionsgleichung die passende Wertetabelle auswählen oder prüfen“ (2026-FOR-B1e); fehlende Tabellenwerte berechnen in 2016-GYM-K4c.
- 3.4 Punktprobe → „Punktprobe durchführen“ – P10-Jahrgänge 7 (Haupt 5). Grund: Definition „Rechnerisch prüfen, ob ein Punkt auf dem Graphen einer Funktion liegt“; 2026-FOR-K5b, 2023-OS-B1i.
- 3.5 Nullstelle berechnen → „Nullstelle lineare Funktion berechnen“ – P10-Jahrgänge 2 (Haupt 1). Grund: Definition „Nullstelle einer linearen Funktion aus der Gleichung berechnen“; 2022-OS-K3a, 2021-OS-K6d.
- 3.6 Schnittpunkt mit y-Achse → „y-Achsenabschnitt ablesen“ · „Eigenschaften eines Graphen beurteilen“ – P10-Jahrgänge 7 (Haupt 3). Grund: Definition „Schnittpunkt einer Geraden mit der y-Achse aus der Gleichung ablesen“ (2024-OS-B1i); Aussage „schneidet die y-Achse in P(0|1)“ in 2021-OS-K2b.
- 3.7 Fehler finden → kein P10-Typ
- 3.8 Begründen → kein P10-Typ

**Einheit 4 · Gleichung bestimmen** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 6; Summe ertrag 10.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Gerade durch zwei Punkte zeichnen | 7 | 2 | 2 | 2017 | 2025 | 0 | 2 |  |
| Geradengleichung aus zwei Punkten | 3 | 1 | 3 | 2015 | 2025 | 0 | 1 |  |
| Geradengleichung aus Punkt und einem Parameter bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Gleichung einer Senkrechten aufstellen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Geradengleichung einer Parallelen durch einen Punkt bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Lage zweier Geraden bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 4.1 Gleichung aus Graph → „Geradengleichung aus zwei Punkten“ – P10-Jahrgänge 3 (Haupt 1). Grund: 2015-OS-K4d: die Gleichung h(t) = −5t + 1300 aus zwei Punkten des gezeichneten Graphen bestimmen.
- 4.2 aus m und Punkt → „Geradengleichung aus Punkt und einem Parameter bestimmen“ · „Geradengleichung aus zwei Punkten“ · „Gleichung einer Senkrechten aufstellen“ · „Geradengleichung einer Parallelen durch einen Punkt bestimmen“ – P10-Jahrgänge 3 (Haupt 1). Grund: Definition „aus einer gegebenen Steigung und einem Punkt … durch Einsetzen“ (2021-GYM-B2a); derselbe Schritt für n in 2025-OS-K5a („6 = −1,5 · (−2) + n“), mit der Steigung der Senkrechten in 2015-GYM-K2d und der Parallelen in 2024-GYM-B1b.
- 4.3 aus zwei Punkten → „Geradengleichung aus zwei Punkten“ · „Geradengleichung einer Parallelen durch einen Punkt bestimmen“ – P10-Jahrgänge 3 (Haupt 1). Grund: Definition „Steigung und y-Achsenabschnitt aus zwei Punkten“ (2025-OS-K5a, 2017-OS-K5a); in 2024-GYM-B1b die Steigung von g aus A und B.
- 4.4 Gerade durch zwei Punkte zeichnen → „Gerade durch zwei Punkte zeichnen“ – P10-Jahrgänge 2 (Haupt 2). (wortgleich)
- 4.5 Schnittpunkt zweier Geraden rechnerisch → „Lage zweier Geraden bestimmen“ – P10-Jahrgänge 0 (Haupt 0). Grund: 2023-GYM-B1b: den Schnittpunkt S(2|1) von f und g durch Gleichsetzen −0,5x + 2 = 0,5x berechnen.
- 4.6 Fehler finden (Steigung mit vertauschter Differenz) → kein P10-Typ
- 4.7 Begründen (Lage zweier Geraden) → „Lage zweier Geraden bestimmen“ – P10-Jahrgänge 0 (Haupt 0). Grund: 2021-GYM-B2b: mit den verschiedenen Anstiegen begründen, dass sich g und h in genau einem Punkt schneiden (Definition „schneiden, parallel oder identisch“).

**Einheit 5 · Anwendungen** – P10-Jahrgänge 8 von 13 (davon Haupt 5); P10-Typen 6; Summe ertrag 28.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lineare Funktion aus Sachverhalt aufstellen | 6 | 2 | 3 | 2016 | 2023 | 0 | 2 |  |
| Gleichung zu Tarif zuordnen | 2 | 1 | 1 | 2021 | 2021 | 0 | 1 |  |
| Endwert linearer Veränderung berechnen | 3 | 2 | 2 | 2021 | 2022 | 0 | 2 |  |
| Tarife vergleichen | 8 | 2 | 2 | 2016 | 2023 | 0 | 2 |  |
| Graph zu Tarif zuordnen | 4 | 2 | 2 | 2016 | 2023 | 0 | 2 |  |
| Eigenschaften eines Graphen beurteilen | 5 | 2 | 6 | 2018 | 2026 | 0 | 2 | kein Katalogtyp zugeordnet |

- 5.1 Lineare Funktion aus Sachverhalt aufstellen → „Lineare Funktion aus Sachverhalt aufstellen“ – P10-Jahrgänge 3 (Haupt 2). (wortgleich)
- 5.2 Gleichung zu Tarif zuordnen → „Gleichung zu Tarif zuordnen“ – P10-Jahrgänge 1 (Haupt 1). (wortgleich)
- 5.3 Graph zu Tarif zuordnen → „Graph zu Tarif zuordnen“ – P10-Jahrgänge 2 (Haupt 2). (wortgleich)
- 5.4 Endwert berechnen → „Endwert linearer Veränderung berechnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „Anfangswert plus oder minus n-fache konstante Änderung“; 2022-OS-K6a, 2021-OS-K6a.
- 5.5 Tarife vergleichen mit Entscheidung → „Tarife vergleichen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „… berechnen und den günstigeren wählen“; 2023-OS-K3b, 2016-OS-K6b.
- 5.6 Situation zu Gleichung beschreiben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Gleichung im Sachzusammenhang deuten“. Grund: Definition „auch bei linearen … Funktionen“; 2021-OS-K6c: Bedeutung von y, x und 40 in y = −0,2x + 40.

### lineare-gleichungssysteme

themen.csv: „Lineare Gleichungssysteme“.

**Einheit 1 · Gleichungen mit zwei Variablen und grafisches Lösen** – P10-Jahrgänge 4 von 13 (davon Haupt 1); P10-Typen 1; Summe ertrag 3.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lineares Gleichungssystem lösen | 3 | 1 | 4 | 2016 | 2024 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 1.1 Zahlenpaar als Lösung einer Gleichung prüfen (wA/fA) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Punktprobe durchführen“ · „Lösung durch Einsetzen prüfen“. Grund: Die Punktprobe prüft ein Zahlenpaar an y = f(x) (Definition; 2026-FOR-K5b), in 2014-OS-K7a an zwei Gleichungen; Kontextvariante der Definition „Vorgegebene Werte in eine Gleichung … einsetzen“.
- 1.2 Lösungspaare einer Gleichung finden (Tabelle) → kein P10-Typ
- 1.3 Gleichung nach y umstellen → „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 1). Grund: Teilschritt des Einsetzens: x + y = 63 zu y = 63 − x in 2022-OS-K7b, r + t = 13 zu r = 13 − t in 2024-OS-K7b.
- 1.4 Gerade zu einer Gleichung zeichnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Gerade aus Gleichung zeichnen“. Grund: Definition „aus der Gleichung mit y-Achsenabschnitt und Steigungsdreieck zeichnen“, nach dem Umstellen nach y (2026-FOR-K5a).
- 1.5 zwei Geraden zeichnen, Schnittpunkt ablesen, Probe → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Gerade aus Gleichung zeichnen“ · „Schnittpunkt am Graphen ablesen“. Grund: 2023-OS-K4a: die Gerade f zeichnen und den Schnittpunkt S(1|2) mit dem gegebenen Graphen ablesen.
- 1.6 Lösung eines Systems am gegebenen Bild ablesen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Schnittpunkt am Graphen ablesen“. Grund: Definition „Koordinaten eines Schnittpunkts zweier Graphen aus dem Koordinatensystem ablesen“; 2023-OS-K4a.
- 1.7 Sonderfälle erkennen (parallel: keine Lösung; identisch: unendlich viele) am Bild und an der Gleichung (gleiche Steigung) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lage zweier Geraden bestimmen“. Grund: Definition „aus den Gleichungen … entscheiden, ob sich die Geraden schneiden, parallel oder identisch sind“; 2014-GYM-B1i.
- 1.8 systematisches Probieren mit Tabelle bei ganzzahliger Lösung → „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 1). Grund: 2016-OS-K6d (Nebentyp): Zimmer und Betten mit ganzzahliger Lösung, laut Katalogzeile „auch durch systematisches Probieren lösbar“.
- 1.9 Fehler finden (Schnittpunkt ungenau abgelesen, keine Probe; Umstellen mit falschem Vorzeichen) → kein P10-Typ
- 1.10 Begründen (warum der Schnittpunkt beide Gleichungen erfüllt; warum Parallelen keine Lösung haben) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lage zweier Geraden bestimmen“. Grund: 2021-GYM-B2b (format Begründung): die Zahl der gemeinsamen Punkte zweier Geraden über ihre Anstiege begründen.

**Einheit 2 · Einsetzungsverfahren** – P10-Jahrgänge 4 von 13 (davon Haupt 1); P10-Typen 1; Summe ertrag 3.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lineares Gleichungssystem lösen | 3 | 1 | 4 | 2016 | 2024 | 0 | 1 |  |

- 2.1 eine Gleichung ist nach y aufgelöst, in die andere einsetzen → „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 1). Grund: Kern des Einsetzungsverfahrens (Definition „rechnerisch lösen“): y = 63 − x in II einsetzen (2022-OS-K7b).
- 2.2 I nach y umstellen (Vorzahl 1) → „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 1). Grund: 2022-OS-K7b: I x + y = 63 nach y = 63 − x umstellen; ebenso 2024-OS-K7b.
- 2.3 nach x umstellen → „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 1). Grund: 2015-GYM-K3b: x = 16 − y; 2021-OS-K7b: e = 64,90 − 3k.
- 2.4 Klammer mit Zahl davor auflösen → „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 1). Grund: Nach dem Einsetzen 3 · (63 − x) in 2022-OS-K7b, 2,30 · (13 − t) in 2024-OS-K7b, 3 · (16 − y) in 2016-OS-K6d.
- 2.5 Minus vor der Klammer → kein P10-Typ
- 2.6 Dezimalzahlen (Geld) → „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 1). Grund: Preise mit Dezimalzahlen in 2022-OS-K7b (352,20 €), 2024-OS-K7b (26,90 €) und 2021-OS-K7b (77,80 €).
- 2.7 negative Lösung → kein P10-Typ
- 2.8 Bruch als Lösung (Vorrat) → kein P10-Typ
- 2.9 Gleichsetzen bei zwei Gleichungen der Form y = … (→ lineare-funktionen.md Einheit 4 für Schnittpunkte) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lage zweier Geraden bestimmen“ · „Schnittpunkte Gerade und Parabel berechnen“. Grund: 2023-GYM-B1b: −0,5x + 2 = 0,5x; Definition „durch Gleichsetzen der Funktionsterme“ für Gerade und Parabel (2024-OS-K3d, 2021-OS-K2c).
- 2.10 zweite Variable berechnen und Probe in beiden Gleichungen → „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 1). Grund: Aus x = 27,20 die zweite Variable y = 35,80 (2022-OS-K7b), aus t = 5 die Zahl r = 8 (2024-OS-K7b).
- 2.11 Lösung als Zahlenpaar angeben → kein P10-Typ
- 2.12 Fehler finden (Term in dieselbe Gleichung eingesetzt; Vorzahl nur auf das erste Glied der Klammer; zweite Variable vergessen) → kein P10-Typ
- 2.13 Begründen (warum nach dem Einsetzen nur noch eine Variable übrig ist) → kein P10-Typ

**Einheit 3 · Additionsverfahren** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 3.1 Gegenzahlen: Gleichungen addieren → kein P10-Typ
- 3.2 gleiche Vorzahlen: subtrahieren → kein P10-Typ
- 3.3 eine Gleichung vervielfachen → kein P10-Typ
- 3.4 beide Gleichungen vervielfachen (kleinstes gemeinsames Vielfaches) → kein P10-Typ
- 3.5 negative Zahlen → kein P10-Typ
- 3.6 Dezimalzahlen und Brüche → kein P10-Typ
- 3.7 Verfahren wählen (Einsetzen, Gleichsetzen, Addition) und begründen → kein P10-Typ
- 3.8 Sonderfälle rechnerisch (0 = 5 keine Lösung; 0 = 0 unendlich viele) → kein P10-Typ
- 3.9 Fehler finden (nur die linke Seite vervielfacht; beim Subtrahieren nur ein Vorzeichen gewechselt) → kein P10-Typ
- 3.10 Begründen (warum man Gleichungen addieren darf) → kein P10-Typ

**Einheit 4 · Sachaufgaben** – P10-Jahrgänge 6 von 13 (davon Haupt 5); P10-Typen 3; Summe ertrag 25.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lineares Gleichungssystem aufstellen | 10 | 3 | 3 | 2016 | 2024 | 0 | 3 |  |
| Gleichung im Sachzusammenhang deuten | 12 | 4 | 5 | 2018 | 2024 | 0 | 4 |  |
| Lineares Gleichungssystem lösen | 3 | 1 | 4 | 2016 | 2024 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 4.1 Unbekannte benennen und mit Einheit beschriften → „Gleichung im Sachzusammenhang deuten“ · „Lineares Gleichungssystem aufstellen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2022-OS-K7a: x und y als Preis eines Baums in € benennen (Definition „ihre Variablen … benennen“); beim Aufstellen in 2021-OS-K7b und 2016-OS-K6d die Unbekannten selbst festlegen.
- 4.2 aus zwei Angaben „zusammen …“ zwei Gleichungen aufstellen (nur aufstellen) → „Lineares Gleichungssystem aufstellen“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2024-OS-K7a: aus „Rose und Tulpe zusammen 3,80 €“ und „6 Rosen und 5 Tulpen 21,20 €“ nur die Gleichungen aufstellen.
- 4.3 Anzahl-und-Preis mit Dezimalzahlen (Eintritt, Blumen, Bäume) → „Lineares Gleichungssystem aufstellen“ · „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 4). Grund: Blumen in 2024-OS-K7a und 2024-OS-K7b, Eintritt in 2021-OS-K7b, Bäume in 2022-OS-K7b.
- 4.4 Anzahl-und-Bestand (Zimmer und Betten, Räder von Autos und Rädern) → „Lineares Gleichungssystem aufstellen“ · „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 4). Grund: Zimmer und Betten in 2016-OS-K6d (aufstellen, lösen als Nebentyp) und 2015-GYM-K3b.
- 4.5 Zahlenrätsel (Summe und Differenz, Vielfache) → kein P10-Typ
- 4.6 Mischungen und Alter (Vorrat) → kein P10-Typ
- 4.7 System aufstellen, lösen, Lösung zuordnen, Antwortsatz → „Lineares Gleichungssystem aufstellen“ · „Lineares Gleichungssystem lösen“ – P10-Jahrgänge 4 (Haupt 4). Grund: 2021-OS-K7b und 2016-OS-K6d: aufstellen und lösen in einer Teilaufgabe, Fehlerquelle „Ergebnisse den Personen falsch zuordnen“.
- 4.8 Probe im Text (Rechnung mit den Zahlen der Aufgabe) → kein P10-Typ
- 4.9 Gleichung im Sachzusammenhang deuten: Variablen benennen (Preis oder Anzahl?) → „Gleichung im Sachzusammenhang deuten“ – P10-Jahrgänge 5 (Haupt 4). Grund: Definition „ihre Variablen … benennen“; 2022-OS-K7a (x und y sind Preise, nicht Anzahlen).
- 4.10 Gleichung als Satz formulieren („x + y = 20“: zusammen zwanzig Stück) → „Gleichung im Sachzusammenhang deuten“ – P10-Jahrgänge 5 (Haupt 4). Grund: Definition „als Satz im Sachzusammenhang formulieren“; 2024-OS-K7b („r + t = 13“).
- 4.11 Bestandteile einer Gleichung deuten (Vorzahl, Absolutglied; bei linearen Funktionen → lineare-funktionen.md Einheit 5, bei Wachstum → potenz-exponentialfunktionen.md) → „Gleichung im Sachzusammenhang deuten“ – P10-Jahrgänge 5 (Haupt 4). Grund: Definition „Bestandteile (Koeffizient, Absolutglied, Wachstumsfaktor) benennen“; 2021-OS-K6c, 2019-OS-K7b.
- 4.12 Fehler finden (Anzahlen und Preise vertauscht; Lösung den falschen Größen zugeordnet) → kein P10-Typ
- 4.13 Begründen (warum zwei Gleichungen nötig sind) → kein P10-Typ

### binomische-formeln

themen.csv: kein msa-Thema – Vermerk: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“.

**Einheit 1 · Summe mal Summe** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 1.1 Termwert mit zwei Variablen berechnen (auch negativ) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Termwert berechnen“. Grund: Definition „auch mit negativen Zahlen“; 2021-OS-B1g und 2016-OS-B1i ((a + b) : c mit negativen Werten), 2019-GYM-B1d ((a − b) : (2a + b) mit b = −3).
- 1.2 zusammenfassen mit zwei Variablen (gleichartige Glieder sortieren) → kein P10-Typ
- 1.3 zusammenfassen mit Potenzen und Produkten (x², xy, x getrennt) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Term mit Klammern und Potenzen vereinfachen“ · „Term durch Zusammenfassen gleichartiger Glieder vereinfachen“. Grund: 2022-GYM-B2b (a² − 6a + 9 − 2a − 9 − a = a² − 9a) und 2025-GYM-B2a (2x − 3x²): Potenz und lineares Glied getrennt halten.
- 1.4 Zahl mal Klammer mit zwei Variablen → kein P10-Typ
- 1.5 Klammer mal Klammer mit lauter Plus: vier Produkte hinschreiben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabelgleichung aus Nullstellen aufstellen“ · „Parameter einer Parabel aus Graph bestimmen“. Grund: Grundfall des Ausmultiplizierens, das 2024-GYM-K3d ((x + 2)(x − 1)) und 2017-GYM-K2c (0,5(x + 3)(x − 1)) verlangen.
- 1.6 zusammenfassen zum dreigliedrigen Term → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabelgleichung aus Nullstellen aufstellen“ · „Parameter einer Parabel aus Graph bestimmen“. Grund: 2024-GYM-K3d: (x + 2)(x − 1) = x² + x − 2; 2022-GYM-K3b: x² − 5x + 5,25; 2017-GYM-K2c: 0,5x² + x − 1,5.
- 1.7 ein Minus in einer Klammer → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabelgleichung aus Nullstellen aufstellen“ · „Parameter einer Parabel aus Graph bestimmen“. Grund: (x + 2)(x − 1) in 2024-GYM-K3d, 0,5(x + 3)(x − 1) in 2017-GYM-K2c.
- 1.8 Minus in beiden Klammern → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabelgleichung aus Nullstellen aufstellen“. Grund: 2022-GYM-K3b: (x − 1,5)(x − 3,5) ausmultiplizieren.
- 1.9 mit Vorzahl vor x → kein P10-Typ
- 1.10 Klammer mal Klammer mit zwei Variablen (a + b)·(c + d) → kein P10-Typ
- 1.11 Fehler finden (nur Erstes mal Erstes und Letztes mal Letztes; Vorzeichen des Produkts; ungleichartig zusammengefasst) → kein P10-Typ
- 1.12 Begründen (warum vier Produkte entstehen – Flächenbild eines Rechtecks) → kein P10-Typ

**Einheit 2 · Binomische Formeln** – P10-Jahrgänge 1 von 13 (davon Haupt 1); P10-Typen 1; Summe ertrag 4.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Scheitelpunktform in Normalform umformen | 4 | 1 | 1 | 2017 | 2017 | 0 | 1 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |

- 2.1 gleiche Klammer zweimal erkennen ((a + b)² ist (a + b)·(a + b)) → „Scheitelpunktform in Normalform umformen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Binomische Formel anwenden“. Grund: Vorstufe gegen die Fehlerquelle „Mittelglied fehlt“ in 2017-OS-K5d ((x + 3)² = x² + 9) und 2019-GYM-B1f (Mittelglied nicht verdoppelt).
- 2.2 erste binomische Formel mit x und Zahl → „Scheitelpunktform in Normalform umformen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Binomische Formel anwenden“. Grund: 2017-OS-K5d: (x + 3)² = x² + 6x + 9; Definition „(a±b)² … mithilfe einer binomischen Formel ausmultiplizieren“.
- 2.3 zweite Formel (Minus im Mittelglied) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Binomische Formel anwenden“ · „Schnittpunkte Gerade und Parabel berechnen“ · „Term mit Klammern und Potenzen vereinfachen“ · „Parabelgleichung aus Scheitel und Punkt bestimmen“. Grund: (2a − b)² in 2019-GYM-B1f, (x − 2)² vor dem Gleichsetzen in 2022-OS-K3c, (a − 3)² in 2022-GYM-B2b, (x − 1,5)² in 2014-GYM-K2c.
- 2.4 dritte Formel (Mittelglied fällt weg) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Binomische Formel anwenden“. Grund: Definition nennt (a + b)(a − b); kein Original mit der dritten Formel.
- 2.5 Formel zuordnen (welche der drei, oder keine) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Binomische Formel anwenden“. Grund: 2019-GYM-B1f: die zweite Formel erkennen und das Ergebnis unter vier Termen auswählen.
- 2.6 mit Vorzahl vor x (a ist die ganze Vorzahl mit x) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Binomische Formel anwenden“. Grund: 2019-GYM-B1f: (2a)² = 4a², unter den Ablenkern Terme mit 2a².
- 2.7 mit zwei Variablen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Binomische Formel anwenden“. Grund: 2019-GYM-B1f: (2a − b)² mit den Variablen a und b.
- 2.8 Vorfaktor vor der Klammer → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Parabelgleichung aus Scheitel und Punkt bestimmen“. Grund: 2014-GYM-K2c: 4/3 · (x − 1,5)² zu 4/3 x² − 4x + 3 ausmultiplizieren.
- 2.9 Minus vor der Klammer → kein P10-Typ
- 2.10 Klammer mit Formel auflösen und mit dem Rest zusammenfassen (Scheitelpunktform → Normalform) → „Scheitelpunktform in Normalform umformen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Schnittpunkte Gerade und Parabel berechnen“ · „Term mit Klammern und Potenzen vereinfachen“. Grund: Definition „Scheitelpunktform durch Ausmultiplizieren der binomischen Formel in die Normalform“ (2017-OS-K5d); ebenso (x − 2)² − 4 in 2022-OS-K3c und 2022-GYM-B2b.
- 2.11 Nachweis „Normalform stimmt“ (P10-Form) → „Scheitelpunktform in Normalform umformen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „ggf. als Nachweis“; 2017-OS-K5d: die vorgegebene Normalform y = x² + 6x + 7 aus (x + 3)² − 2 nachweisen.
- 2.12 Kopfrechnen mit der Formel (Vorrat) → kein P10-Typ
- 2.13 Fehler finden (Mittelglied fehlt; Vorzeichen des Mittelglieds; Vorzahl nicht quadriert; Minus vor der Klammer nur aufs erste Glied) → kein P10-Typ
- 2.14 Begründen (warum (a + b)² nicht a² + b² ist – Zahlenprobe, Flächenbild) → kein P10-Typ

**Einheit 3 · Faktorisieren** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 3.1 Quadrat erkennen (welche Terme sind Quadrate) → kein P10-Typ
- 3.2 dritte Formel rückwärts (Differenz zweier Quadrate) → kein P10-Typ
- 3.3 erste Formel rückwärts mit Prüfung des Mittelglieds (doppeltes Produkt der Wurzeln) → kein P10-Typ
- 3.4 zweite Formel rückwärts (Minus im Mittelglied) → kein P10-Typ
- 3.5 mit Vorzahl (Quadrat von 2x) → kein P10-Typ
- 3.6 erst gemeinsamen Faktor ausklammern, dann Formel → kein P10-Typ
- 3.7 kein Binom erkennen (Mittelglied passt nicht; Summe zweier Quadrate) → kein P10-Typ
- 3.8 Probe durch Ausmultiplizieren → kein P10-Typ
- 3.9 Anwendung: Produktform gleich null (Verfahren in quadratische-gleichungen.md Einheit 2) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lineare Gleichung lösen“. Grund: Verfahren der Originale 2024-OS-B1d („Produkt ist null, wenn die Klammer null ist“: 2 · (x − 6,5) = 0) und 2023-OS-B1e (3 · (x − 8) = 0, also x − 8 = 0).
- 3.10 quadratische Ergänzung (Vorrat, H; → quadratische-funktionen.md Einheit 3) → kein P10-Typ
- 3.11 Fehler finden (Summe zweier Quadrate „faktorisiert“; Mittelglied nicht geprüft; Vorzeichen in der Klammer) → kein P10-Typ
- 3.12 Begründen (warum eine Summe zweier Quadrate keine binomische Formel ist) → kein P10-Typ

### quadratische-funktionen

themen.csv: „Quadratische Funktionen“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Parameter einer Parabel aus Graph bestimmen“; „Parabelgleichung aus Nullstellen aufstellen“.

**Einheit 1 · Normalparabel und Streckfaktor** – P10-Jahrgänge 10 von 13 (davon Haupt 10); P10-Typen 6; Summe ertrag 16.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Parabelgleichung zu Graph zuordnen | 3 | 1 | 1 | 2015 | 2015 | 0 | 1 |  |
| Parabel aus Gleichung skizzieren | 2 | 1 | 1 | 2024 | 2024 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Scheitelpunkt ablesen | 11 | 8 | 9 | 2017 | 2026 | 1 | 8 | nicht in der Zuordnungszeile der Einheit |
| Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Parabeltransformation gegenüber der Normalparabel beschreiben | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Parabelgleichung aus Scheitel und Punkt bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Wertetabelle zu p(x) = x² ausfüllen (auch negative x) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“ · „Wertetabelle einer Funktion zuordnen“. Grund: Jeder Tabelleneintrag ist ein Funktionswert (Definition „Wert einer Funktion für ein gegebenes Argument berechnen“); Grundfall a = 1 zu 2026-FOR-B1e (Tabellen für x = −2 bis 2 zu y = 3x² prüfen).
- 1.2 Punkte eintragen und Normalparabel zeichnen (Bogen, kein Lineal) → „Parabel aus Gleichung skizzieren“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Wertetabelle als Punkte darstellen“. Grund: Definition „Wertepaare einer Tabelle in ein vorgegebenes Koordinatensystem eintragen“ (an einer Parabel 2024-GYM-K3b, Nebentyp); die Normalparabel ist der Grundfall von „Verschobene Normalparabel aus der Gleichung … skizzieren“ (2024-OS-K3b).
- 1.3 Eigenschaften nennen (Scheitel, Symmetrieachse, Öffnung, kleinster Wert) → „Scheitelpunkt ablesen“ – P10-Jahrgänge 9 (Haupt 8). Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert über Symmetrie bestimmen“. Grund: Der Scheitel S(0 | 0) ist der Grundfall von „Scheitelpunkt … am Graphen ablesen oder aus der Gleichung bestimmen“ (Definition); die Symmetrie zur y-Achse nutzt 2023-GYM-K3a (f(−1/3) = f(1/3) ohne Rechnung).
- 1.4 Funktionswert berechnen (auch negatives x) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“. Grund: 
- 1.5 Punktprobe rechnerisch → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Punktprobe durchführen“. Grund: Definition „Rechnerisch prüfen, ob ein Punkt auf dem Graphen einer Funktion liegt“; an Parabeln 2020-OS-K3b und 2024-OS-K3c.
- 1.6 Wertetabelle zu p(x) = a·x² ausfüllen und zuordnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wertetabelle einer Funktion zuordnen“ · „Funktionswert berechnen“. Grund: 2026-FOR-B1e: zu y = 3x² unter drei Wertetabellen die passende wählen, Kontrolle 3 · 2² = 12; Ausfüllen heißt Funktionswerte berechnen (Definition).
- 1.7 Öffnung und Breite an a erkennen (a < 0 nach unten; a größer als 1 schmaler; a zwischen 0 und 1 breiter) → „Parabelgleichung zu Graph zuordnen“ · „Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen“ · „Parabeltransformation gegenüber der Normalparabel beschreiben“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „über Öffnung, Streckung …“ (2015-OS-K4b: −3t² für den fallenden Bogen); falsche Öffnung am Koeffizienten −40 in 2018-GYM-K5a; Breite im Vergleich zur Normalparabel in 2022-GYM-K3a (Definition „und ggf. Streckung“).
- 1.8 Parabel zu a·x² zeichnen (Schablone reicht nicht; LISUM G, kein P10-Original) → „Parabelgleichung aus Scheitel und Punkt bestimmen“ · „Parabel aus Gleichung skizzieren“ – P10-Jahrgänge 1 (Haupt 1). Grund: GYM-Originale: Definition „… und den Graphen zeichnen“ mit gestreckten Parabeln in 2014-GYM-K2c (a = 4/3, Nebentyp „Parabel aus Gleichung skizzieren“) und 2022-GYM-K3c (h(x) = 2x² − 4,5 zeichnen).
- 1.9 Parabelgleichung zu Graph zuordnen über Öffnung, Streckung und Startwert, mit Begründung → „Parabelgleichung zu Graph zuordnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2015-OS-K4b: h(t) = −3t² + 2400 über Startwert und Öffnung wählen und begründen; ebenso 2014-GYM-B1d (y = x² + c).
- 1.10 Fehler finden (negatives x falsch quadriert; 3x² als 3x oder (3x)² gelesen) → kein P10-Typ
- 1.11 Begründen (warum p(−x) = p(x); warum a < 0 nach unten öffnet) → kein P10-Typ

**Einheit 2 · Scheitelpunktform** – P10-Jahrgänge 11 von 13 (davon Haupt 11); P10-Typen 11; Summe ertrag 29.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Scheitelpunkt ablesen | 11 | 8 | 9 | 2017 | 2026 | 1 | 8 |  |
| Scheitelpunktform aufstellen | 3 | 2 | 5 | 2016 | 2025 | 1 | 1 |  |
| Parabel aus Gleichung skizzieren | 2 | 1 | 1 | 2024 | 2024 | 0 | 1 |  |
| Parabel verschieben | 3 | 2 | 2 | 2015 | 2017 | 1 | 1 |  |
| Parabel an der x-Achse spiegeln | 0 | 0 | 2 | 2017 | 2018 | 0 | 0 |  |
| Parabel an der y-Achse spiegeln | 3 | 1 | 1 | 2020 | 2020 | 0 | 1 |  |
| Parabel zu Eigenschaften angeben | 4 | 1 | 1 | 2018 | 2018 | 0 | 1 |  |
| Lage zweier Parabeln begründen | 3 | 1 | 1 | 2026 | 2026 | 0 | 1 |  |
| Parabeltransformation gegenüber der Normalparabel beschreiben | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Anzahl gemeinsamer Punkte zweier Graphen begründen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Parabelgleichung aus Scheitel und Punkt bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 2.1 Scheitel aus der Scheitelpunktform ablesen (Vorzeichen von d) → „Scheitelpunkt ablesen“ – P10-Jahrgänge 9 (Haupt 8). Grund: Definition „… oder aus der Gleichung bestimmen“; 2022-OS-K3b ((x − 2)² − 4) und 2017-OS-K5c ((x + 3)² − 2).
- 2.2 Scheitel am Graphen ablesen und als S(d | e) schreiben → „Scheitelpunkt ablesen“ – P10-Jahrgänge 9 (Haupt 8). Grund: Definition „am Graphen ablesen“; 2021-OS-B1d (S(−2 | −1) unter vier Angaben) und 2020-OS-K3a.
- 2.3 Parabel aus der Gleichung skizzieren (Scheitel setzen, Normalparabel-Punkte vom Scheitel aus) → „Parabel aus Gleichung skizzieren“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2024-OS-K3b (p(x) = x² − 4); Nebentyp in 2016-GYM-K2d und 2019-GYM-K2a.
- 2.4 Scheitelpunktform aus dem Scheitel aufstellen → „Scheitelpunktform aufstellen“ – P10-Jahrgänge 5 (Haupt 2). Grund: Definition „in der Form p(x) = (x − d)² + e angeben“; 2016-OS-B1g (zu S(1 | 3) die Gleichung ankreuzen).
- 2.5 Scheitelpunktform aus dem Graphen aufstellen (Scheitel ablesen, Öffnung prüfen, nach unten: Minus vor der Klammer) → „Scheitelpunktform aufstellen“ · „Scheitelpunkt ablesen“ – P10-Jahrgänge 10 (Haupt 9). Grund: 2023-OS-K4b: Scheitel (−1 | 6) ablesen (Haupttyp) und p(x) = −(x + 1)² + 6 mit Minus vor der Klammer aufstellen (Nebentyp).
- 2.6 Parabel verschieben (nach oben/unten über e, nach rechts/links über d) und neue Gleichung oder neuen Scheitel angeben → „Parabel verschieben“ · „Parabeltransformation gegenüber der Normalparabel beschreiben“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „Gleichung … nach Verschiebung … angeben oder nur den neuen Scheitelpunkt nennen“ (2015-OS-B1i, 2017-OS-K5e); die Verschiebung aus der Lage des Scheitels beschreiben verlangt 2022-GYM-K3a.
- 2.7 an der x-Achse spiegeln (Minus vor den ganzen Term) → „Parabel an der x-Achse spiegeln“ – P10-Jahrgänge 2 (Haupt 0). Grund: Definition „Vorzeichen des gesamten Funktionsterms wechselt“; 2017-OS-K5e und 2018-OS-K5d (Nebentyp), 2023-GYM-K3c.
- 2.8 an der y-Achse spiegeln (d wechselt das Vorzeichen) → „Parabel an der y-Achse spiegeln“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2020-OS-K3d: Scheitel (−2 | −4) wird (2 | −4), Gleichung (x − 2)² − 4.
- 2.9 Parabel zu Eigenschaften angeben (Scheitel auf einer Achse, keine Nullstellen, Öffnung; mehrere Lösungen) → „Parabel zu Eigenschaften angeben“ – P10-Jahrgänge 1 (Haupt 1). (wortgleich)
- 2.10 Lage zweier Parabeln begründen (gleicher Scheitel, entgegengesetzte Öffnung; Scheitel über- oder untereinander) → „Lage zweier Parabeln begründen“ · „Anzahl gemeinsamer Punkte zweier Graphen begründen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2026-FOR-K5d (gleicher Scheitel, entgegengesetzte Öffnung); Scheitel übereinander mit entgegengesetzter Öffnung in 2020-GYM-B2b (x² − 2 und −x² − 3 ohne gemeinsamen Punkt).
- 2.11 Aussagen zur Parabel als wahr/falsch beurteilen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften eines Graphen beurteilen“. Grund: Definition „Aussagen zu … Verlauf eines Graphen als wahr oder falsch bewerten“; an der Parabel 2018-OS-K5a (Typ bei lineare-funktionen.md).
- 2.12 Streckfaktor vor der Klammer erkennen und Merkmale der gestreckten Parabel bestimmen (LISUM G, kein P10-Original) → „Parabelgleichung aus Scheitel und Punkt bestimmen“ · „Parabeltransformation gegenüber der Normalparabel beschreiben“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Originale: Ansatz a · (x − 1,5)² mit a = 4/3 in 2014-GYM-K2c; Definition „durch welche Verschiebung (und ggf. Streckung)“ (2022-GYM-K3a).
- 2.13 Fehler finden (Vorzeichen in der Klammer; Verschieben und Spiegeln in falscher Reihenfolge; nur das Vorzeichen von x² gewechselt) → kein P10-Typ
- 2.14 Begründen (warum (x − d)² bei x = d am kleinsten ist; warum e der kleinste Funktionswert ist) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lösbarkeit quadratischer Gleichung beurteilen“. Grund: 2017-GYM-K2a begründet genau das: (x − 3)² ≥ 0, also f(x) ≥ 1,5, darum keine Nullstelle (Typ bei quadratische-gleichungen.md).

**Einheit 3 · Normalform** – P10-Jahrgänge 10 von 13 (davon Haupt 9); P10-Typen 5; Summe ertrag 18.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Scheitelpunktform in Normalform umformen | 4 | 1 | 1 | 2017 | 2017 | 0 | 1 |  |
| Scheitelpunkt einer Parabel rechnerisch nachweisen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Scheitelpunkt ablesen | 11 | 8 | 9 | 2017 | 2026 | 1 | 8 | nicht in der Zuordnungszeile der Einheit |
| Scheitelpunktform aufstellen | 3 | 2 | 5 | 2016 | 2025 | 1 | 1 | nicht in der Zuordnungszeile der Einheit |
| Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 3.1 y-Achsenabschnitt q aus der Normalform ablesen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“ · „Eigenschaften eines Graphen beurteilen“. Grund: q ist p(0): Schnittpunkt mit der y-Achse über f(0) in 2024-GYM-K3b und 2017-GYM-K2a (Nebentyp); Aussage zum y-Achsenschnittpunkt (0 | 2) in 2018-OS-K5a.
- 3.2 Funktionswert und Punktprobe in der Normalform mit negativem x → „Scheitelpunkt einer Parabel rechnerisch nachweisen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“ · „Punktprobe durchführen“. Grund: 2018-OS-K5a: p(−1) = 1 + 4 + 2 = 7 (Nebentyp Punktprobe); 2021-GYM-K6a (h(2) = 4,7); 2019-GYM-K2a setzt den Scheitel in die Normalform ein (f(3,5) = 5).
- 3.3 Scheitelpunktform ausmultiplizieren (binomische Formel) und zusammenfassen → „Scheitelpunktform in Normalform umformen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Binomische Formel anwenden“. Grund: Definition „durch Ausmultiplizieren der binomischen Formel in die Normalform überführen“ (2017-OS-K5d); der Teilschritt (x + 3)² ist „Binomische Formel anwenden“ (Definition, Thema Terme umformen).
- 3.4 Nachweis „Normalform stimmt“ (Behauptung prüfen) → „Scheitelpunktform in Normalform umformen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: Definition „ggf. als Nachweis“; 2017-OS-K5d lässt genau die Behauptung y = x² + 6x + 7 prüfen (Nebentyp Behauptung prüfen).
- 3.5 Scheitel einer Normalform-Parabel am Graphen ablesen → „Scheitelpunkt ablesen“ – P10-Jahrgänge 9 (Haupt 8). Grund: 2018-OS-K5b (x² − 4x + 2) und 2025-OS-K5b (x² − 6x + 7), Scheitel jeweils am Graphen.
- 3.6 Scheitelpunktform aus Normalform und abgelesenem Scheitel aufstellen, Probe mit q → „Scheitelpunktform aufstellen“ – P10-Jahrgänge 5 (Haupt 2). Grund: 2018-OS-K5c (p(x) = (x − 2)² − 2 aus x² − 4x + 2) und 2025-OS-K5b (Nebentyp).
- 3.7 Aussagen zur Parabel als wahr/falsch beurteilen (Punktprobe, Verschiebung, y-Achsenabschnitt) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften eines Graphen beurteilen“ · „Punktprobe durchführen“. Grund: 2018-OS-K5a mit genau diesen drei Aussagen (Punktprobe als Nebentyp).
- 3.8 quadratische Ergänzung (Vorrat, H) → kein P10-Typ
- 3.9 allgemeine Form a·x² + bx + c erkennen und Öffnung an a ablesen (Vorrat, H) → „Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen“ – P10-Jahrgänge 0 (Haupt 0). Grund: Definition „falsche Öffnungsrichtung bzw. falscher Koeffizient“: 2018-GYM-K5a liest an y = −40x² + 12,5 die Öffnung am Koeffizienten vor x² ab.
- 3.10 Fehler finden (Mittelglied der binomischen Formel fehlt; Vorzeichen des Scheitels; Koordinaten des y-Achsenschnittpunkts vertauscht) → kein P10-Typ
- 3.11 Begründen (warum q der y-Achsenabschnitt ist; warum die Öffnung bei x² + px + q gleich bleibt) → kein P10-Typ

**Einheit 4 · Nullstellen und Schnittpunkte berechnen** – P10-Jahrgänge 8 von 13 (davon Haupt 7); P10-Typen 5; Summe ertrag 24.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Nullstellen quadratische Funktion berechnen | 7 | 2 | 3 | 2017 | 2025 | 0 | 2 |  |
| Argument zu Funktionswert berechnen | 3 | 1 | 1 | 2023 | 2023 | 0 | 1 |  |
| Schnittpunkte Gerade und Parabel berechnen | 12 | 3 | 3 | 2021 | 2024 | 0 | 3 |  |
| Gerade ohne gemeinsamen Punkt mit Parabel angeben | 2 | 1 | 1 | 2014 | 2014 | 0 | 1 |  |
| Schnittpunkte zweier Parabeln berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 4.1 Nullstellen aus der Scheitelpunktform durch Wurzelziehen → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Lösungsweg „(x + 3)² = 2, x = −3 ± √2“ in 2017-OS-K5d (Nebentyp); 0,0085x² = 12 durch Wurzelziehen in 2016-GYM-K4c (Nebentyp).
- 4.2 Zahl der Nullstellen am Scheitel begründen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lösbarkeit quadratischer Gleichung beurteilen“. Grund: 2017-GYM-K2a (nachweisen, dass (x − 3)² + 1,5 keine Nullstellen hat) und 2021-OS-K7c ((x + 7)² = 0 hat genau eine Lösung); Typ bei quadratische-gleichungen.md.
- 4.3 Nullstellen aus der Normalform mit der p-q-Formel → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: 2025-OS-K5c (x² − 6x + 7 = 0 mit der p-q-Formel) und 2024-GYM-K3a.
- 4.4 vorher durch den Streckfaktor teilen → „Nullstellen quadratische Funktion berechnen“ · „Argument zu Funktionswert berechnen“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2020-OS-K3e (2x² + 8x + 6 = 0 durch 2 teilen); 2023-OS-K4c (Minus vor x², zu x² + 2x − 15 = 0 normiert).
- 4.5 Nullstellen mit Wurzel als Ergebnis (Näherungswert) → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: 2025-OS-K5c (3 ± √2 ≈ 1,59 und 4,41) und 2017-OS-K5d (−3 ± √2, Nebentyp).
- 4.6 Argument zu gegebenem Funktionswert (Gleichung aufstellen, ordnen, lösen) → „Argument zu Funktionswert berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2023-OS-K4c (−x² − 2x + 5 = −10) und 2020-GYM-B2a (x² − 2 = 23).
- 4.7 Schnittpunkte Gerade und Parabel (gleichsetzen, alles auf eine Seite, lösen, y-Werte über die Gerade) → „Schnittpunkte Gerade und Parabel berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Definition „durch Gleichsetzen der Funktionsterme“; 2021-OS-K2c und 2024-OS-K3d (y-Werte über die Gerade).
- 4.8 Parabel in Scheitelpunktform gleichsetzen (Klammer auflösen) → „Schnittpunkte Gerade und Parabel berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2022-OS-K3c: (x − 2)² − 4 = −2x + 3, Klammer auflösen zu x² − 2x − 3 = 0.
- 4.9 Punktprobe als Schnittpunkt-Nachweis (in beide Funktionen einsetzen) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Punktprobe durchführen“. Grund: 2014-OS-K7a: S(−3 | −9) in p(x) = −x² und g(x) = 2x − 3 einsetzen (Typ bei lineare-funktionen.md).
- 4.10 Gerade ohne gemeinsamen Punkt mit der Parabel angeben (waagerecht jenseits des Scheitels) → „Gerade ohne gemeinsamen Punkt mit Parabel angeben“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2014-OS-K7b: waagerechte Gerade f(x) = 1 über dem Scheitel von p(x) = −x².
- 4.11 Schnittpunkte zweier Parabeln berechnen (LISUM G, kein P10-Original) → „Schnittpunkte zweier Parabeln berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Typ mit dem Original 2019-GYM-K2b (Gleichsetzen führt auf x² − 5x + 2,25 = 0).
- 4.12 Fehler finden (nur eine Lösung; y-Werte vergessen; Vorzeichen beim Umstellen; Klammer ohne Mittelglied aufgelöst) → kein P10-Typ
- 4.13 Begründen (warum Nullstellen Schnittpunkte mit der x-Achse sind; warum eine waagerechte Gerade unter dem Scheitel die nach oben geöffnete Parabel nicht trifft) → kein P10-Typ

### quadratische-gleichungen

themen.csv: „Quadratische Gleichungen“.

**Einheit 1 · Wurzelziehen und Lösbarkeit** – P10-Jahrgänge 5 von 13 (davon Haupt 4); P10-Typen 3; Summe ertrag 13.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Lösbarkeit quadratischer Gleichung beurteilen | 3 | 1 | 1 | 2021 | 2021 | 0 | 1 |  |
| Argument zu Funktionswert berechnen | 3 | 1 | 1 | 2023 | 2023 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Nullstellen quadratische Funktion berechnen | 7 | 2 | 3 | 2017 | 2025 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |

- 1.1 x² = c mit Quadratzahl lösen, beide Lösungen (x₁ = √c, x₂ = −√c) → „Argument zu Funktionswert berechnen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Quadratseite aus Fläche berechnen“. Grund: 2020-GYM-B2a endet mit x² = 25, x = ±5; im Sachzusammenhang 2020-OS-B1d (a² = 36 cm², nur die positive Lösung; Typ bei flaechen.md).
- 1.2 x² = c ohne Quadratzahl (Wurzel stehen lassen, Näherungswert mit dem Taschenrechner) → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Radius eines Zylinders aus Volumen berechnen“. Grund: 2016-GYM-K4c: x = √(12 : 0,0085) ≈ 37,57 (Nebentyp Nullstellen); 2022-OS-K2d: r = √(425 : (π · 7)) ≈ 4,40 cm (Typ bei koerper.md).
- 1.3 x² = c mit negativem c: keine Lösung → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „eine Gleichung ohne Lösung angeben“ (2021-OS-K7c, etwa x² + 1 = 0); 2017-GYM-K2a (keine Nullstelle von (x − 3)² + 1,5).
- 1.4 x² freistellen bei a·x² + b = 0 und a·x² = b (erst umformen, dann Wurzel) → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Radius eines Zylinders aus Volumen berechnen“. Grund: 2022-OS-K2d: r² aus V = π · r² · h freistellen, dann Wurzel (Nebenbestand, Typ bei koerper.md); 2016-GYM-K4c: −0,0085x² + 12 = 0 zu 0,0085x² = 12 (Nebentyp Nullstellen).
- 1.5 a·x² + b = c mit beliebiger rechter Seite und Fallbetrachtung (GYM) → „Argument zu Funktionswert berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2020-GYM-B2a: x² − 2 = 23 zu x² = 25 umformen, x = ±5.
- 1.6 (x − d)² = c rückwärts rechnen (zwei Fälle x − d = √c und x − d = −√c, dann d hinüberbringen) → „Lösbarkeit quadratischer Gleichung beurteilen“ · „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2021-OS-K7c: (x + 8)² = 16, x + 8 = ±4, x = −4 oder −12; Lösungsweg „(x + 3)² = 2, x = −3 ± √2“ in 2017-OS-K5d (Nebentyp Nullstellen).
- 1.7 (x − d)² = 0: genau eine Lösung → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2021-OS-K7c: Aussage „(x + 7)² = 0 hat genau eine Lösung“ beurteilen.
- 1.8 Lösung durch Einsetzen prüfen, auch negativ, (wA)/(fA) → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Lösung durch Einsetzen prüfen“. Grund: Definition „Vorgegebene Werte in eine Gleichung (linear oder quadratisch) einsetzen“ (2025-OS-B1h, Typ bei lineare-gleichungen.md); die Aussage „4 und 12 sind Lösungen von (x + 8)² = 16“ in 2021-OS-K7c widerlegt man durch Einsetzen.
- 1.9 Zahl der Lösungen an c begründen (positiv, null, negativ) → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Aussagen zur Anzahl … der Lösungen … prüfen“; 2021-OS-K7c (rechte Seite null: eine Lösung) und 2017-GYM-K2a (keine Nullstelle begründen).
- 1.10 Zahl der Lösungen am Graphen ablesen (Parabel und waagerechte Gerade y = c; Nullstellen als Sonderfall c = 0) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Gerade ohne gemeinsamen Punkt mit Parabel angeben“. Grund: 2014-OS-K7b: eine waagerechte Gerade ohne Schnittpunkt mit p(x) = −x² wählen heißt, am Graphen ein c mit null Lösungen zu finden (Typ bei quadratische-funktionen.md).
- 1.11 Gleichung ohne Lösung angeben → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „und eine Gleichung ohne Lösung angeben“; 2021-OS-K7c (etwa x² + 1 = 0).
- 1.12 Aussagen zu Lösungen als wahr oder falsch beurteilen (P10-Form) → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2021-OS-K7c: zwei Aussagen zu (x + 7)² = 0 und (x + 8)² = 16 als wahr oder falsch ankreuzen.
- 1.13 Fehler finden (nur die positive Wurzel; Vorzeichen von d beim Rückwärtsrechnen; Wurzel aus einer negativen Zahl „gezogen“) → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2021-OS-K7c: die Aussage „4 und 12 sind Lösungen von (x + 8)² = 16“ ist genau das Ergebnis des Vorzeichenfehlers bei d; sie als falsch zu erkennen heißt, diesen Fehler zu finden.
- 1.14 Begründen (warum x² = c mit positivem c zwei Lösungen hat; warum x² = c mit negativem c keine hat) → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2017-GYM-K2a verlangt die Begründung, dass ein Quadrat nie negativ ist: (x − 3)² = −1,5 hat keine Lösung, also hat f keine Nullstelle.

**Einheit 2 · Satz vom Nullprodukt** – P10-Jahrgänge 4 von 13 (davon Haupt 3); P10-Typen 2; Summe ertrag 10.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Nullstellen quadratische Funktion berechnen | 7 | 2 | 3 | 2017 | 2025 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |
| Lösbarkeit quadratischer Gleichung beurteilen | 3 | 1 | 1 | 2021 | 2021 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |

- 2.1 Produktform (x − a)·(x − b) = 0, jeden Faktor null setzen → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Lösungsweg „Faktorisieren (x + 1)(x + 3)“ in 2020-OS-K3e, ebenso 2024-GYM-K3a und 2025-GYM-B2b ((x + 4)(x − 2) = 0): jeden Faktor null setzen.
- 2.2 Vorzeichen in den Klammern (x + a) → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Die Faktorisierungen der Lösungswege tragen Plus in der Klammer: (x + 1)(x + 3) in 2020-OS-K3e, (x + 4)(x − 2) in 2025-GYM-B2b.
- 2.3 gleiche Faktoren (x − a)² = 0: eine Lösung → „Lösbarkeit quadratischer Gleichung beurteilen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2021-OS-K7c: Aussage „(x + 7)² = 0 hat genau eine Lösung“.
- 2.4 x·(x + a) = 0 → kein P10-Typ
- 2.5 x² + px = 0 durch Ausklammern (x = 0 oder x + p = 0) (GYM) → kein P10-Typ
- 2.6 Minus vor dem x-Glied (GYM) → kein P10-Typ
- 2.7 Vorzahl vor x² (a·x² + bx = 0: x ausklammern, Klammer lösen) (GYM) → kein P10-Typ
- 2.8 Lösung durch Einsetzen prüfen bei Produktform, negativ (Klammer zuerst, Punkt vor Strich) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Lösung durch Einsetzen prüfen“ · „Parabelgleichung aus Nullstellen aufstellen“. Grund: 2025-OS-B1h: x·(x + 5) = −6 mit x = −2 prüfen (Typ bei lineare-gleichungen.md); 2022-GYM-K3b bestätigt die Nullstellen durch Einsetzen in die Produktform (Definition „… durch Einsetzen bestätigen“).
- 2.9 Produkt gleich einer Zahl ungleich null: Satz nicht anwendbar – ausmultiplizieren, ordnen, weiter mit Einheit 3 → kein P10-Typ
- 2.10 Nullstellen einer Normalform durch Faktorisieren als Alternative zur Formel (Vorrat) → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: Lösungsweg „p-q-Formel oder Faktorisieren“ in 2020-OS-K3e, 2024-GYM-K3a und 2025-GYM-B2b.
- 2.11 Fehler finden (durch x geteilt und Lösung null verloren; Vorzeichen beim Nullsetzen; Nullprodukt bei Produkt ungleich null) → kein P10-Typ
- 2.12 Begründen (warum ein Produkt null ist, sobald ein Faktor null ist; warum man nicht durch x teilen darf) → kein P10-Typ

**Einheit 3 · Normalform und p-q-Formel** – P10-Jahrgänge 7 von 13 (davon Haupt 6); P10-Typen 3; Summe ertrag 22.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Nullstellen quadratische Funktion berechnen | 7 | 2 | 3 | 2017 | 2025 | 0 | 2 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |
| Argument zu Funktionswert berechnen | 3 | 1 | 1 | 2023 | 2023 | 0 | 1 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |
| Schnittpunkte Gerade und Parabel berechnen | 12 | 3 | 3 | 2021 | 2024 | 0 | 3 | Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei) |

- 3.1 Normalform erkennen und p, q mit Vorzeichen ablesen → „Nullstellen quadratische Funktion berechnen“ · „Argument zu Funktionswert berechnen“ · „Schnittpunkte Gerade und Parabel berechnen“ – P10-Jahrgänge 7 (Haupt 6). Außerhalb der Themen des Eintrags (zählt nicht): „Schnittpunkte zweier Parabeln berechnen“. Grund: Erster Schritt der p-q-Formel in den Verfahrensgebern 2025-OS-K5c, 2023-OS-K4c und 2024-OS-K3d; 2019-GYM-K2b nennt p = −5, q = 2,25 ausdrücklich.
- 3.2 Gleichung ordnen: alles auf eine Seite, Reihenfolge x², x, Zahl → „Argument zu Funktionswert berechnen“ · „Schnittpunkte Gerade und Parabel berechnen“ – P10-Jahrgänge 4 (Haupt 4). Außerhalb der Themen des Eintrags (zählt nicht): „Schnittpunkte zweier Parabeln berechnen“. Grund: 2023-OS-K4c (−x² − 2x + 5 = −10), 2024-OS-K3d (4x + 1 = x² − 4 zu x² − 4x − 5 = 0), 2019-GYM-K2b (h − f).
- 3.3 Normieren: durch die Vorzahl von x² teilen, auch bei negativer Vorzahl → „Nullstellen quadratische Funktion berechnen“ · „Argument zu Funktionswert berechnen“ – P10-Jahrgänge 4 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Schnittpunkte zweier Parabeln berechnen“. Grund: 2020-OS-K3e (durch 2), 2023-OS-K4c (durch −1), 2019-GYM-K2b (2x² − 10x + 4,5 durch 2).
- 3.4 p-q-Formel mit ganzzahligen Lösungen (Diskriminante Quadratzahl) → „Nullstellen quadratische Funktion berechnen“ · „Argument zu Funktionswert berechnen“ · „Schnittpunkte Gerade und Parabel berechnen“ – P10-Jahrgänge 7 (Haupt 6). Grund: 2020-OS-K3e (−1 und −3), 2023-OS-K4c (−5 und 3), 2022-OS-K3c und 2024-OS-K3d (Wert unter der Wurzel 4 bzw. 9).
- 3.5 p ungerade: p halbe als Dezimalzahl → „Schnittpunkte Gerade und Parabel berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Schnittpunkte zweier Parabeln berechnen“. Grund: 2021-OS-K2c (x² − x − 2 = 0, p halbe = 0,5) und 2019-GYM-K2b (p = −5, p halbe = 2,5).
- 3.6 Lösungen mit Wurzel, Näherungswert runden → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Grund: 2025-OS-K5c (3 ± √2 ≈ 1,59 und 4,41) und 2017-OS-K5d (−3 ± √2, Nebentyp).
- 3.7 unter der Wurzel null: genau eine Lösung → kein P10-Typ
- 3.8 unter der Wurzel negativ: keine Lösung → kein P10-Typ
- 3.9 Zahl der Lösungen am Wert unter der Wurzel beurteilen (der Begriff „Diskriminante“ dafür: GYM, LISUM-PH Gymnasium Zeile 1965, Niveaustufe H) → kein P10-Typ
- 3.10 Probe mit einer Lösung → „Nullstellen quadratische Funktion berechnen“ – P10-Jahrgänge 3 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Lösung durch Einsetzen prüfen“. Grund: Definition „Vorgegebene Werte in eine Gleichung (linear oder quadratisch) einsetzen“ (Typ bei lineare-gleichungen.md); 2023-GYM-K3b weist Nullstellen durch Einsetzen nach (f(−2) = 0, f(2) = 0).
- 3.11 Klammer oder Produkt zuerst auflösen (binomische Formel, x·(x + a)), dann ordnen → „Schnittpunkte Gerade und Parabel berechnen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Scheitelpunktform in Normalform umformen“. Grund: 2022-OS-K3c: (x − 2)² − 4 = −2x + 3, Klammer auflösen; 2017-OS-K5d: (x + 3)² − 2 zu x² + 6x + 7 ausmultiplizieren, dann null setzen.
- 3.12 Gerade und Parabel gleichsetzen als Anwendung (Verfahren hier, Typ in quadratische-funktionen.md Einheit 4) → „Schnittpunkte Gerade und Parabel berechnen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Die drei Verfahrensgeber 2021-OS-K2c, 2022-OS-K3c und 2024-OS-K3d (Typ bei quadratische-funktionen.md Einheit 4).
- 3.13 Lösungsweg wählen: Wurzelziehen, Nullprodukt oder Formel → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Schnittpunkte zweier Parabeln berechnen“. Grund: Definition „eine geeignete Lösungsmethode (z. B. pq-Formel) … erläutern“ (2019-GYM-K2b).
- 3.14 grafische Kontrolle an der Parabel (Vorrat) → kein P10-Typ
- 3.15 Fehler finden (ohne Normieren; Vorzeichen von −p/2; Diskriminante mit Plus; nur eine Lösung; Wurzel aufgeteilt) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Fehler in Rechnung erklären und korrigieren“. Grund: 2021-GYM-K6c: in einer vorgegebenen p-q-Rechnung den Vorzeichenfehler unter der Wurzel (9 − 3,75 statt 9 + 3,75) benennen und berichtigen.
- 3.16 Begründen (warum die Formel nur für die Normalform gilt; warum bei negativer Diskriminante keine Lösung existiert) → kein P10-Typ

**Einheit 4 · Sachaufgaben** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 4.1 Zahlenrätsel mit dem Quadrat einer Zahl (Wurzelziehen) → kein P10-Typ
- 4.2 Produkt einer Zahl mit ihrem Nachfolger (Nullprodukt oder Formel) → kein P10-Typ
- 4.3 Rechteck mit Seitenbeziehung und Fläche (Skizze, geg./ges., Gleichung, Formel) → kein P10-Typ
- 4.4 Quadrat mit Rand (Vorrat) → kein P10-Typ
- 4.5 Lösungen im Kontext prüfen: negative Länge ausschließen, beim Zahlenrätsel beide Zahlen zulassen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Quadratseite aus Fläche berechnen“ · „Fehler in Rechnung erklären und korrigieren“. Grund: 2020-OS-B1d: als Seitenlänge gilt nur die positive Lösung von a² = 36 (Nebenbestand, Typ bei flaechen.md); 2021-GYM-K6c: der negative Wert x₂ ≈ −0,57 ist als Stoßweite auszuschließen.
- 4.6 Antwortsatz mit Einheit → kein P10-Typ
- 4.7 Fehler finden (negative Länge als Antwort; Gleichung mit Umfang statt Fläche) → kein P10-Typ
- 4.8 Begründen (warum beim Rechteck nur eine Lösung gilt, beim Zahlenrätsel beide) → kein P10-Typ

### potenz-exponentialfunktionen

themen.csv: „Exponentialfunktionen und Wachstum“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Wertebereich einer Funktion angeben“; „Graph einer Exponentialfunktion an der y-Achse spiegeln“; „Exponentialfunktion verschieben“.

**Einheit 1 · Lineares und exponentielles Wachstum unterscheiden** – P10-Jahrgänge 7 von 13 (davon Haupt 7); P10-Typen 6; Summe ertrag 36.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Wachstumsart begründen | 4 | 2 | 2 | 2016 | 2018 | 0 | 2 |  |
| Graph zu Wachstumsprozess zuordnen | 9 | 2 | 2 | 2019 | 2026 | 0 | 3 |  |
| Wachstumsfaktor aus Tabelle bestimmen | 6 | 2 | 2 | 2018 | 2025 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |
| Exponentialfunktion aufstellen | 4 | 2 | 4 | 2016 | 2026 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |
| Wachstumstabelle ergänzen | 13 | 5 | 5 | 2016 | 2026 | 0 | 6 | nicht in der Zuordnungszeile der Einheit |
| Graph eines exponentiellen Vorgangs zeichnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 an einer Tabelle entscheiden, ob die Zunahme immer gleich groß ist (Differenzen) oder immer derselbe Faktor wirkt (Quotienten) → „Wachstumsart begründen“ · „Wachstumsfaktor aus Tabelle bestimmen“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2016-OS-K4d (Differenzen 0,55; 0,49 … werden kleiner, Faktor 0,89 bleibt); 2016-GYM-K2b (ungleiche Quotienten, also keine Exponentialfunktion).
- 1.2 Wachstumsart begründen: gleicher Prozentsatz vom jeweils vorigen Wert bedeutet gleicher Faktor, die Zuwächse in Euro oder Kilogramm werden größer (bei Abnahme kleiner) → „Wachstumsart begründen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2018-OS-K2b (gleicher Faktor 1,08, Zuwächse werden größer) und 2016-OS-K4d (Abnahme, Differenzen werden kleiner).
- 1.3 dieselbe Entscheidung aus einem Text ohne Tabelle → „Wachstumsart begründen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „ob ein beschriebener Vorgang linear … oder exponentiell … wächst“; 2018-OS-K2b nur aus dem Text „jährlich um 8 %“.
- 1.4 Zunahme und Abnahme unterscheiden (Faktor größer oder kleiner als eins) → „Exponentialfunktion aufstellen“ · „Wachstumstabelle ergänzen“ – P10-Jahrgänge 6 (Haupt 5). Grund: 2017-OS-K7c: bei 13 % Abnahme 1000 · 0,87^x statt 1000 · 1,13^x wählen; Definition „Faktor > 1 oder < 1“ bei der Wachstumstabelle.
- 1.5 Wertepaare aus einer Tabelle als Punkte eintragen, Skala mit größeren Schritten lesen → „Graph eines exponentiellen Vorgangs zeichnen“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Wertetabelle als Punkte darstellen“. Grund: 2025-OS-K7a (Bakterien, Skala in größeren Schritten); GYM-Typ mit 2014-GYM-K4b (Punkte eines Zerfalls eintragen).
- 1.6 Achseneinteilung für gegebene Werte wählen und die Punkte zur Kurve verbinden → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Achseneinteilung wählen“ · „Wertetabelle als Punkte darstellen“. Grund: 2017-OS-K7b und 2016-OS-K4b: Achsen einteilen, Punkte eintragen und zur fallenden Kurve verbinden (Nebentyp Wertetabelle als Punkte darstellen).
- 1.7 Graph zu einem Wachstumsprozess auswählen: Startwert auf der y-Achse gegen Beginn im Ursprung, Gerade gegen gekrümmte Kurve → „Graph zu Wachstumsprozess zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „den passenden auswählen und die anderen ausschließen“; 2019-OS-K7c und 2026-FOR-K7b (Startwert größer null, gekrümmt statt gerade).
- 1.8 begründen, warum die beiden anderen Graphen nicht passen → „Graph zu Wachstumsprozess zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften eines Graphen beurteilen“. Grund: Definition „… und die anderen ausschließen“; die Begründung je Graph tragen 2019-OS-K7c und 2026-FOR-K7b als Nebentyp „Eigenschaften eines Graphen beurteilen“.
- 1.9 Graph einer Abnahme (fallend, flacher werdend) erkennen → „Graph zu Wachstumsprozess zuordnen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „zu einem linearen oder exponentiellen Sachverhalt“ schließt die Abnahme ein; beide Originale (2019-OS-K7c, 2026-FOR-K7b) zeigen Zunahmen.
- 1.10 Grenzen des Modells nennen (ein Bestand wächst nicht ewig) → kein P10-Typ
- 1.11 Fehler finden (Tabelle als linear gelesen, weil der Prozentsatz gleich bleibt) → kein P10-Typ
- 1.12 Begründen (warum „jedes Jahr gleich viel Prozent“ nicht „jedes Jahr gleich viel Euro“ heißt) → „Wachstumsart begründen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2018-OS-K2b verlangt genau diese Begründung: gleicher Prozentsatz vom jeweils vorigen Wert, die absoluten Zuwächse werden größer.

**Einheit 2 · Wachstumsfaktor und Wachstumstabelle** – P10-Jahrgänge 7 von 13 (davon Haupt 7); P10-Typen 4; Summe ertrag 23.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Wachstumstabelle ergänzen | 13 | 5 | 5 | 2016 | 2026 | 0 | 6 |  |
| Wachstumsfaktor aus Tabelle bestimmen | 6 | 2 | 2 | 2018 | 2025 | 0 | 2 |  |
| Exponentialfunktion aufstellen | 4 | 2 | 4 | 2016 | 2026 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |
| Parameter einer Exponentialfunktion bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 2.1 Prozentsatz in den Faktor umrechnen, Zunahme und Abnahme → „Wachstumstabelle ergänzen“ · „Exponentialfunktion aufstellen“ – P10-Jahrgänge 6 (Haupt 5). Außerhalb der Themen des Eintrags (zählt nicht): „Wert nach prozentualer Erhöhung berechnen“. Grund: Teilschritt aller Originale: 3 % zu 1,03 (2020-OS-K4a), 11 % Abnahme zu 0,89 (2016-OS-K4a), 1,9 % zu 1,019 (2026-FOR-K7c); Definition „Erhöhung oder Senkung … (Wachstumsfaktor)“ bei prozentrechnung.md.
- 2.2 Faktor in den Prozentsatz zurück → „Wachstumsfaktor aus Tabelle bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Gleichung im Sachzusammenhang deuten“. Grund: 2018-OS-K2a (Nachweis der 8 % über 1,08); 2019-OS-K7b (1,04 als Zunahme um 4 % deuten, Typ bei lineare-gleichungssysteme.md).
- 2.3 Faktor als Quotient zweier aufeinanderfolgender Tabellenwerte nachweisen, mehrere Quotienten prüfen → „Wachstumsfaktor aus Tabelle bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „als Quotient aufeinanderfolgender Tabellenwerte nachweisen“; 2025-OS-K7b (112 : 80 = 1,4, weitere Quotienten ≈ 1,40).
- 2.4 nächsten Tabellenwert berechnen (Wert mal Faktor) → „Wachstumstabelle ergänzen“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2026-FOR-K7a (674,93 · 1,019) und 2020-OS-K4a (57,3 · 1,03).
- 2.5 Lücke mitten in der Tabelle füllen → „Wachstumstabelle ergänzen“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2016-OS-K4a (Wert bei 1 h: 5,00 · 0,89) und 2017-OS-K7a (Wert bei 2 km).
- 2.6 Anfangsbestand als Wert im Schritt null eintragen (nicht rückwärts rechnen, wenn der Startwert im Text steht) → „Wachstumstabelle ergänzen“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2026-FOR-K7a (2026: 650 €), 2020-OS-K4a (2019: 54) und 2019-OS-K7a (Woche 0: 10 kg).
- 2.7 einen Schritt zurückrechnen (geteilt durch den Faktor) → „Wachstumstabelle ergänzen“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „Fehlende Werte … über den Wachstumsfaktor ergänzen“ schließt den Wert vor einem bekannten ein; in den Originalen steht der Anfangswert im Text (2020-OS-K4a: 55,6 : 1,03 ≈ 54 als Kontrolle).
- 2.8 Wert über mehrere Schritte mit der Potenz des Faktors → „Wachstumstabelle ergänzen“ – P10-Jahrgänge 5 (Haupt 5). Grund: 2019-OS-K7a (10 · 1,04⁵) und 2017-OS-K7a (498 · 0,87³).
- 2.9 fehlende Zeitangabe im Tabellenkopf über die Zahl der Schritte bestimmen und prüfen → „Wachstumstabelle ergänzen“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „auch eine fehlende Zeitangabe“; 2016-OS-K4a (3,14 mg gehört zu 4 h, Kontrolle 5,00 · 0,89⁴).
- 2.10 Wachstumsrate aus zwei Werten bestimmen → „Wachstumsfaktor aus Tabelle bestimmen“ · „Parameter einer Exponentialfunktion bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Prozentuale Veränderung berechnen“. Grund: 2018-OS-K2a (48 000 : 600 000 = 8 %); Definition „Zu- oder Abnahme zwischen zwei Werten in Prozent des Ausgangswerts“ (prozentrechnung.md); Faktor aus nicht benachbarten Werten in 2016-GYM-K2a (a² = 2,25) und 2024-GYM-K4d (b⁶ = 25 875 : 550).
- 2.11 Tabelle für einen Zerfall mit Faktor kleiner eins fortschreiben → „Wachstumstabelle ergänzen“ – P10-Jahrgänge 5 (Haupt 5). Grund: Definition „Faktor > 1 oder < 1“; 2016-OS-K4a (0,89) und 2017-OS-K7a (0,87).
- 2.12 Fehler finden (immer denselben Betrag addiert; Faktor aus dem Prozentsatz ohne die Eins gebildet; Startwert schon einmal verzinst) → kein P10-Typ
- 2.13 Begründen (warum der Quotient und nicht die Differenz den Faktor zeigt) → kein P10-Typ

**Einheit 3 · Exponentialfunktion aufstellen und auswerten** – P10-Jahrgänge 5 von 13 (davon Haupt 3); P10-Typen 3; Summe ertrag 6.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Exponentialfunktion aufstellen | 4 | 2 | 4 | 2016 | 2026 | 0 | 2 |  |
| Zeitpunkt für Schwellenwert bei Wachstum bestimmen | 2 | 1 | 1 | 2018 | 2018 | 0 | 1 |  |
| Gleichungskette im Sachzusammenhang erläutern | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 3.1 Anfangswert und Faktor im Text finden → „Exponentialfunktion aufstellen“ – P10-Jahrgänge 4 (Haupt 2). Grund: Teilschritt der Definition „aus Anfangswert und Wachstumsfaktor angeben“; 2026-FOR-K7c (650 € und 1,9 % im Text).
- 3.2 Gleichung y = a · qˣ aufstellen (Zunahme und Abnahme) → „Exponentialfunktion aufstellen“ – P10-Jahrgänge 4 (Haupt 2). Grund: Erste Hälfte von „Gleichung y = a · qˣ aufstellen“; Definition „Gleichung N(t) = a · q^t … angeben“ (2026-FOR-K7c). 2026-FOR-K7c (Zunahme, M(t) = 650 · 1,019^t) und 2017-OS-K7c (Abnahme, y = 1000 · 0,87^x).
- 3.3 passende Gleichung unter vier Vorschlägen ankreuzen → „Exponentialfunktion aufstellen“ – P10-Jahrgänge 4 (Haupt 2). Grund: 2017-OS-K7c: y = 1000 · 0,87^x unter vier Gleichungen ankreuzen.
- 3.4 Bestandteile einer gegebenen Gleichung deuten: Anfangswert, Faktor als „hundert Prozent plus Zuwachs“, Variable als Zeit → „Gleichungskette im Sachzusammenhang erläutern“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Gleichung im Sachzusammenhang deuten“. Grund: 2019-OS-K7b (10, 1,04 und x in f(x) = 10 · 1,04^x; Typ bei lineare-gleichungssysteme.md); 2024-GYM-K4c erläutert 500 000 = 200 · 2,5^x im Sachzusammenhang.
- 3.5 Wert nach einer gegebenen Zahl von Schritten berechnen (Potenz mit dem Taschenrechner, Ergebnis mit ≈ und Einheit) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“ · „Zinseszins Endkapital berechnen“. Grund: 2016-OS-K4e (5 · 0,89²⁴ ≈ 0,31 mg), 2026-FOR-K7c (Nebentyp; Typ bei lineare-funktionen.md); dieselbe Rechnung im Zinskontext 2014-OS-K3c (1000 · 1,03⁵, Typ bei zinsrechnung.md).
- 3.6 Zeitschritte zählen, wenn Jahreszahlen gegeben sind (Startjahr ist der Schritt null) → „Zeitpunkt für Schwellenwert bei Wachstum bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“. Grund: 2026-FOR-K7c (2040 heißt t = 14) und 2020-OS-K4c (2033 heißt x = 14, Fehlerquelle „x = 2033 einsetzen“); 2018-OS-K2c zählt die Jahre ab 2017 bis 2020.
- 3.7 Behauptung prüfen: Wert berechnen und mit dem genannten vergleichen, Entscheidung mit Begründung → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“ · „Behauptung prüfen“. Grund: Definition „ggf. mit einer Vorgabe vergleichen“; genau diese Behauptungen prüfen 2017-OS-K7d (etwa 4 km Höhe bei 573 hPa) und 2025-OS-K7b (mehr als 250 000 Bakterien nach 24 Stunden), beide mit Nebentyp Behauptung prüfen.
- 3.8 zwei Vorhersagen vergleichen (exponentiell gegen einen festen Gesamtprozentsatz) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“ · „Wert nach prozentualer Erhöhung berechnen“ · „Behauptung prüfen“. Grund: 2020-OS-K4c: 54 · 1,03¹⁴ ≈ 81,7 gegen 54 · 1,4 = 75,6 (Nebentypen Wert nach prozentualer Erhöhung berechnen und Behauptung prüfen).
- 3.9 Zeitpunkt für einen Schwellenwert durch schrittweises Multiplizieren finden, Schritte zählen und den erreichten Wert angeben → „Zeitpunkt für Schwellenwert bei Wachstum bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „durch schrittweises Multiplizieren … und den Wert angeben“; 2018-OS-K2c (2020, ≈ 1 028 294 €).
- 3.10 Zerfall bis unter eine Schwelle → „Zeitpunkt für Schwellenwert bei Wachstum bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Dasselbe Verfahren mit Faktor kleiner eins (Definition „schrittweises Multiplizieren mit dem Wachstumsfaktor“); kein Original mit Zerfall.
- 3.11 Fehler finden (Jahreszahl statt Zahl der Schritte eingesetzt; Prozentsatz statt Faktor als Basis; Faktor mit der Schrittzahl multipliziert statt potenziert) → kein P10-Typ
- 3.12 Begründen (warum das Ergebnis mit einer Potenz und nicht mit einer Multiplikation entsteht) → kein P10-Typ

**Einheit 4 · Verdopplungs- und Halbwertszeit** – P10-Jahrgänge 3 von 13 (davon Haupt 3); P10-Typen 5; Summe ertrag 6.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Verdopplungs- oder Halbwertszeit bestimmen | 4 | 2 | 2 | 2016 | 2020 | 0 | 2 |  |
| Zeitpunkt für Schwellenwert bei Wachstum bestimmen | 2 | 1 | 1 | 2018 | 2018 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Zeit aus Exponentialgleichung berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Aussage zu Logarithmusterm prüfen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Gleichungskette im Sachzusammenhang erläutern | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 4.1 Startwert verdoppeln oder halbieren und den Zielwert notieren → „Verdopplungs- oder Halbwertszeit bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Teilschritt: 2020-OS-K4b (108 = 2 · 54) und 2016-OS-K4c (2,50 mg als Hälfte von 5,00 mg).
- 4.2 Zielwert in einer Tabelle suchen und die Zeit ablesen → „Verdopplungs- oder Halbwertszeit bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „aus … der Wertetabelle“; 2016-OS-K4c.
- 4.3 Zielwert am Graphen suchen: Wert an der y-Achse, waagerecht zum Graphen, senkrecht zur x-Achse, Zeit ablesen → „Verdopplungs- oder Halbwertszeit bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „aus dem Graphen“; 2020-OS-K4b (y = 108 suchen, zugehöriges x ablesen).
- 4.4 das eigene Vorgehen in Worten beschreiben → „Verdopplungs- oder Halbwertszeit bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „ggf. das Vorgehen beschreiben“; 2020-OS-K4b.
- 4.5 zwischen zwei Tabellenwerten die nächstliegende Zeit angeben (der Zielwert liegt selten genau auf einem Tabellenwert) → „Verdopplungs- oder Halbwertszeit bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2016-OS-K4c: 2,50 mg liegt zwischen 2,79 (5 h) und 2,48 (6 h), Antwort etwa 6 h.
- 4.6 durch Probieren mit dem Faktor rechnen, bis der Zielwert erreicht ist → „Zeitpunkt für Schwellenwert bei Wachstum bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Exponent einer Potenz bestimmen“. Grund: Abgrenzung in der Definition von „Verdopplungs- oder Halbwertszeit bestimmen“: schrittweises Multiplizieren bis zur Schwelle ist der Schwellenwert-Typ (2018-OS-K2c); Probieren über die Potenzen in 2024-OS-B1g (4^x = 256, Typ bei potenzen-wurzeln.md).
- 4.7 Halbwertszeit beim Zerfall, Verdopplungszeit beim Wachstum benennen → „Verdopplungs- oder Halbwertszeit bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „verdoppelt oder halbiert“: Halbierung in 2016-OS-K4c, Verdopplung in 2020-OS-K4b.
- 4.8 prüfen, dass die Zeit unabhängig vom Startwert immer gleich lang ist → kein P10-Typ
- 4.9 Logarithmus für den genauen Zeitpunkt (Vorrat) → „Zeit aus Exponentialgleichung berechnen“ · „Aussage zu Logarithmusterm prüfen“ · „Gleichungskette im Sachzusammenhang erläutern“ – P10-Jahrgänge 0 (Haupt 0). Grund: GYM-Typen: Definition „den Exponenten t durch Logarithmieren berechnen“ (2014-GYM-K4c, 2018-GYM-K2b); derselbe Schritt in 2025-GYM-K3c (x = log₂ 10) und 2024-GYM-K4c (x = log₂,₅ 2500 erläutern).
- 4.10 Fehler finden (die Zeit statt des Wertes verdoppelt; beim Ablesen die Achsen vertauscht) → kein P10-Typ
- 4.11 Begründen (warum es genügt, den doppelten Wert einmal zu suchen) → kein P10-Typ

**Einheit 5 · Potenzfunktionen mit natürlichem Exponenten** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 5.1 Wertetabelle zu y = x³ ausfüllen (auch negative x) → kein P10-Typ
- 5.2 Wertetabelle zu y = x⁴ → kein P10-Typ
- 5.3 Punkte eintragen und Graph zeichnen → kein P10-Typ
- 5.4 Symmetrie am Exponenten erkennen (gerade: y-Achse, ungerade: Ursprung) → kein P10-Typ
- 5.5 Öffnung und Breite an a erkennen → kein P10-Typ
- 5.6 Funktionswert berechnen, auch negatives x (−2)³ → kein P10-Typ
- 5.7 Punktprobe → kein P10-Typ
- 5.8 Argument zu gegebenem Wert (dritte Wurzel) → kein P10-Typ
- 5.9 Gleichung unter vier Graphen zuordnen → kein P10-Typ
- 5.10 Graph zu gegebener Gleichung ankreuzen → kein P10-Typ
- 5.11 Sachaufgabe (Volumen eines Würfels aus der Kante, Kante aus dem Volumen) → kein P10-Typ
- 5.12 Fehler finden (−x² gegen (−x)²; x³ als 3 · x) → kein P10-Typ
- 5.13 Begründen (warum y = x⁴ nie negativ wird; warum y = x³ durch den dritten Quadranten geht) → kein P10-Typ
- 5.14 Potenzfunktion vom exponentiellen Term unterscheiden (Variable in der Basis gegen Variable im Exponenten) → kein P10-Typ

### trigonometrische-funktionen

themen.csv: kein msa-Thema – Vermerk: „kein Prüfungsthema; Aufgaben in anderen Themen oder nicht geprüft“.

**Einheit 1 · Einheitskreis und Bogenmaß** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 1.1 zu einem gegebenen Winkel den Punkt auf dem Einheitskreis einzeichnen → kein P10-Typ
- 1.2 zu einem eingezeichneten Punkt den Winkel angeben → kein P10-Typ
- 1.3 Sinuswert als Hochkoordinate und Kosinuswert als Rechtskoordinate ablesen → kein P10-Typ
- 1.4 Werte der vier Achsenwinkel angeben → kein P10-Typ
- 1.5 abgelesenen Wert mit dem Taschenrechner prüfen (Grad-Modus) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Sinussatz Seite berechnen“. Grund: Nebenleistungsbestand: sin 123°, sin 115° und sin 141° mit dem Taschenrechner im Grad-Modus bilden (2015-OS-K5c, 2020-OS-K7c, 2025-OS-K4c; Typ bei trigonometrie.md).
- 1.6 Vorzeichen von Sinus und Kosinus im angegebenen Quadranten bestimmen → kein P10-Typ
- 1.7 zu einem gegebenen Sinuswert die beiden Winkel im Vollkreis finden → kein P10-Typ
- 1.8 Winkel vom Gradmaß ins Bogenmaß umrechnen → kein P10-Typ
- 1.9 Winkel vom Bogenmaß ins Gradmaß umrechnen → kein P10-Typ
- 1.10 geläufige Winkel als Vielfache von Pi angeben und zuordnen → kein P10-Typ
- 1.11 Taschenrechner-Modus erkennen und wechseln (DEG, RAD) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Seite im rechtwinkligen Dreieck berechnen“. Grund: 2021-OS-K3a nennt als Fehlerquelle „Taschenrechner in Bogenmaß“; das richtige Ergebnis setzt den Grad-Modus voraus (Typ bei trigonometrie.md).
- 1.12 Fehler finden (Bogenmaß statt Grad eingegeben; Sinus- und Kosinuskoordinate vertauscht; Vorzeichen im zweiten oder dritten Quadranten übersehen) → kein P10-Typ
- 1.13 Begründen (warum der Sinuswert nie größer als eins wird – der Radius ist eins; warum dem Vollwinkel das Bogenmaß zwei Pi entspricht – der Umfang des Einheitskreises) → kein P10-Typ

**Einheit 2 · Sinus- und Kosinusfunktion und ihre Merkmale** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 2.1 Wertetabelle in gleichmäßigen Winkelschritten ausfüllen (am Einheitskreis oder mit dem Taschenrechner) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“. Grund: Definition „Wert einer Funktion für ein gegebenes Argument berechnen“ gilt für jede Funktion (Typ bei lineare-funktionen.md); kein Original an der Sinusfunktion.
- 2.2 Punkte eintragen und den Graphen zeichnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wertetabelle als Punkte darstellen“. Grund: Definition „Wertepaare einer Tabelle in ein vorgegebenes Koordinatensystem eintragen“ ohne Einschränkung des Funktionstyps; kein Original an der Sinusfunktion.
- 2.3 Achseneinteilung wählen und beschriften → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Achseneinteilung wählen“. Grund: Definition „eine Achseneinteilung wählen, mit der alle Werte einer Tabelle darstellbar sind, und sie beschriften“; kein Original an der Sinusfunktion.
- 2.4 Funktionswert zu einem Winkel ablesen → kein P10-Typ
- 2.5 Winkel zu einem Funktionswert ablesen (beide Lösungen im Vollkreis) → kein P10-Typ
- 2.6 Funktionswert berechnen und Punktprobe durchführen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Funktionswert berechnen“ · „Punktprobe durchführen“. Grund: Beide Definitionen gelten für jede Funktion (Typen bei lineare-funktionen.md); kein Original an der Sinusfunktion.
- 2.7 Wertebereich angeben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften trigonometrischer Funktionen vergleichen“. Grund: Grundfall a = 1 zu 2015-GYM-K2b (Wertebereich [−2; 2] gegen [−2; 6] als unterscheidende Eigenschaft).
- 2.8 Nullstellen angeben und die Regelmäßigkeit beschreiben → kein P10-Typ
- 2.9 Hoch- und Tiefpunkte angeben → kein P10-Typ
- 2.10 kleinste Periode angeben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: 2019-GYM-B1i: zwei volle Perioden auf [−2π; 2π], also Periode 2π ablesen.
- 2.11 Monotonie in einem Abschnitt beschreiben (steigt, fällt) → kein P10-Typ
- 2.12 Symmetrie beschreiben (Sinuskurve punktsymmetrisch zum Ursprung, Kosinuskurve achsensymmetrisch zur senkrechten Achse) → kein P10-Typ
- 2.13 Sinus- und Kosinusgraph vergleichen und die Verschiebung angeben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften trigonometrischer Funktionen vergleichen“. Grund: Definition „Zwei trigonometrische Funktionen anhand einer unterscheidenden Eigenschaft (z. B. … Achsenschnittpunkt) vergleichen“ (2015-GYM-K2b).
- 2.14 Graph einer Gleichung zuordnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: Grundfall zu 2019-GYM-B1i (Gleichung unter vier Vorschlägen dem Graphen zuordnen).
- 2.15 Wertetabelle einem Graphen zuordnen → kein P10-Typ
- 2.16 Fehler finden (Welle als Parabelbogen gezeichnet; Werte über eins eingetragen; Periode von Nullstelle zu Nullstelle statt über die ganze Welle gemessen) → kein P10-Typ
- 2.17 Begründen (warum sich die Kurve wiederholt – der Punkt läuft wieder um den Kreis; warum die Kosinuskurve dieselbe Form hat) → kein P10-Typ

**Einheit 3 · Parameter und Transformationen** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 3.1 Amplitude aus einer Gleichung ablesen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften trigonometrischer Funktionen vergleichen“ · „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: 2015-GYM-K2b (f(x) = 2 · sin(0,5π · x) hat Amplitude 2); 2019-GYM-B1i (Amplituden der vier Vorschläge vergleichen).
- 3.2 Amplitude an einem Graphen ablesen (halber Abstand zwischen Hoch- und Tiefpunkt) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften trigonometrischer Funktionen vergleichen“ · „Transformation einer trigonometrischen Funktion beschreiben“ · „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: 2015-GYM-K2b und 2015-GYM-K2a (g mit Maximum 6 und Minimum −2, Amplitude 4); 2019-GYM-B1i (Wertebereich [−3; 1], Amplitude 2).
- 3.3 Wertebereich zu gegebenem a angeben → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften trigonometrischer Funktionen vergleichen“. Grund: 2015-GYM-K2b: Wertebereich [−2; 2] zu a = 2 als unterscheidende Eigenschaft (Definition „z. B. Amplitude, Wertebereich“).
- 3.4 Spiegelung an der waagerechten Achse bei negativem a erkennen → kein P10-Typ
- 3.5 Periode aus dem Parameter b berechnen (Vollkreis geteilt durch b) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: 2019-GYM-B1i: die Vorschläge mit sin(2x) haben Periode π und scheiden aus.
- 3.6 Parameter b aus der abgelesenen Periode berechnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: 2019-GYM-B1i: Periode 2π abgelesen, also Faktor 1 vor x.
- 3.7 Graph zu gegebener Gleichung skizzieren → kein P10-Typ
- 3.8 Gleichung aus einem gegebenen Graphen aufstellen (erst Amplitude, dann Periode, dann b) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Trigonometrische Funktionsgleichung zu Graph zuordnen“ · „Transformation einer trigonometrischen Funktion beschreiben“. Grund: 2019-GYM-B1i (Amplitude, Periode und Verschiebung am Graphen, Gleichung wählen); 2015-GYM-K2a (zum Graphen von g eine passende Gleichung notieren).
- 3.9 Graphen und Gleichungen einander zuordnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: Definition „aus mehreren Gleichungen (unterschiedliche Amplitude, Streckung oder Verschiebung) die passende auswählen“ (2019-GYM-B1i).
- 3.10 Wirkung eines Parameters in Worten beschreiben (höher, flacher, schneller, langsamer) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Transformation einer trigonometrischen Funktion beschreiben“. Grund: Definition „Beschreiben, wie der Graph … durch Streckung in y-Richtung und Verschiebung … hervorgeht“ (2015-GYM-K2a).
- 3.11 zwei Graphen mit verschiedenen Parametern vergleichen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Eigenschaften trigonometrischer Funktionen vergleichen“ · „Transformation einer trigonometrischen Funktion beschreiben“. Grund: 2015-GYM-K2b (Amplitude 2 gegen 4) und 2015-GYM-K2a (g aus f durch Streckung und Verschiebung).
- 3.12 Verschiebung nach oben und unten mit d, Verschiebung zur Seite mit c (Vorrat, H, GYM) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Transformation einer trigonometrischen Funktion beschreiben“ · „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: 2015-GYM-K2a (Verschiebung um 2 nach oben) und 2019-GYM-B1i (Verschiebung um −1, Vorschlag 2 · sin(2x − 1) zur Seite).
- 3.13 Kosinusfunktion als verschobene Sinusfunktion beschreiben (Vorrat, H, GYM) → kein P10-Typ
- 3.14 Lage der Nullstellen und Extremstellen mit Parameter und Periode angeben (Vorrat, H, GYM) → kein P10-Typ
- 3.15 Fehler finden (Periode mit b malgenommen statt geteilt; Amplitude als Höhe über der waagerechten Achse gelesen; a und b vertauscht) → kein P10-Typ
- 3.16 Begründen (warum ein größeres b die Welle schmaler macht – der Vollkreis wird schneller durchlaufen) → kein P10-Typ

**Einheit 4 · Periodische Vorgänge modellieren** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 4.1 einen Vorgang als periodisch oder nicht periodisch einordnen und die Entscheidung begründen → kein P10-Typ
- 4.2 die Periode eines Vorgangs aus einer Beschreibung oder einem Diagramm angeben → kein P10-Typ
- 4.3 Größtwert und Kleinstwert einer Tabelle entnehmen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Minimum und Maximum ablesen“. Grund: Definition „Kleinsten und größten Wert einer Datenreihe oder eines Diagramms angeben“ (Typ bei daten.md).
- 4.4 Mittellinie und Amplitude daraus bestimmen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Trigonometrische Funktionsgleichung zu Graph zuordnen“ · „Transformation einer trigonometrischen Funktion beschreiben“. Grund: Aus Größt- und Kleinstwert Mittellinie und Amplitude: 2019-GYM-B1i ([−3; 1] ergibt Amplitude 2, Verschiebung −1), 2015-GYM-K2a (6 und −2 ergeben Amplitude 4, Verschiebung 2).
- 4.5 Sinusgleichung zu einem Sachverhalt aufstellen → kein P10-Typ
- 4.6 Sachkontext, Gleichung und Graph einander zuordnen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Trigonometrische Funktionsgleichung zu Graph zuordnen“. Grund: Kontextvariante des Zuordnens von Gleichung und Graph in 2019-GYM-B1i; kein Original mit Sachkontext.
- 4.7 einen Funktionswert im Sachzusammenhang deuten → kein P10-Typ
- 4.8 den Zeitpunkt des Größtwerts oder Kleinstwerts angeben → kein P10-Typ
- 4.9 eine Frage am Graphen beantworten (Ablesen mit Hilfslinien) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Wert aus Diagramm ablesen“. Grund: Definition „aus einem Funktionsgraphen im Sachzusammenhang … an der Skala ablesen“ (Typ bei daten.md).
- 4.10 beurteilen, wie gut das Modell zum Vorgang passt, und die Grenzen benennen → kein P10-Typ
- 4.11 Funktionstypen gegenüberstellen (Gerade, Parabel, Exponentialkurve, Sinuskurve) und Merkmale in einer Tabelle sammeln → kein P10-Typ
- 4.12 zu einem Sachverhalt den passenden Funktionstyp auswählen und die übrigen ausschließen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Graph zu Wachstumsprozess zuordnen“. Grund: Nebenleistungsbestand des Eintrags: 2019-OS-K7c und 2026-FOR-K7b (linear gegen exponentiell, die anderen Graphen ausschließen; Typ bei potenz-exponentialfunktionen.md).
- 4.13 Fehler finden (Graph als Bild des Vorgangs gedeutet, etwa die Sinuskurve als Weg der Sonne; Mittellinie mit dem Größtwert verwechselt; Periode als halbe Wiederholung gelesen) → kein P10-Typ
- 4.14 Begründen (warum ein Wachstumsvorgang keine Sinuskurve ergibt; warum die Tageslänge im Jahresverlauf annähernd periodisch ist) → kein P10-Typ

### daten

themen.csv: „Kenngrößen“, „Diagramme lesen und beurteilen“, „Daten darstellen“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Fehlenden Wert aus Spannweite bestimmen“; „Datenreihen anhand von Kenngrößen vergleichen“.

**Einheit 1 · Häufigkeiten** – P10-Jahrgänge 4 von 13 (davon Haupt 4); P10-Typen 5; Summe ertrag 9.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Relative Häufigkeit angeben | 1 | 1 | 1 | 2015 | 2015 | 0 | 1 |  |
| Kreisdiagramm zeichnen | 3 | 1 | 3 | 2015 | 2025 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Modalwert bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Kenngrößen einer Liste prüfen | 2 | 1 | 1 | 2025 | 2025 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Wert aus Diagramm ablesen | 3 | 2 | 2 | 2015 | 2016 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |

- 1.1 Strichliste auszählen → kein P10-Typ
- 1.2 Häufigkeitstabelle aus einer Urliste → „Kreisdiagramm zeichnen“ – P10-Jahrgänge 3 (Haupt 1). Grund: 2020-GYM-K6c zeichnet das Kreisdiagramm aus einer Urliste von zehn Trefferzahlen und muss dafür erst die Häufigkeit je Trefferzahl auszählen (Fehlerquelle „die Trefferzahlen selbst statt der Häufigkeiten“).
- 1.3 relative Häufigkeit als Bruch (22 von 34) → „Relative Häufigkeit angeben“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Quotient aus absoluter Häufigkeit und Gesamtzahl (Bruch, Dezimalzahl oder Prozent)“; einziges Original 2015-OS-K7b mit 22 von 34 Spielen als 22/34.
- 1.4 als Dezimalzahl und in Prozent (Taschenrechner, runden) → „Relative Häufigkeit angeben“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Prozentsatz berechnen“. Grund: Die Definition nennt Dezimalzahl und Prozent (2015-OS-K7b ≈ 0,65 ≈ 64,7 %); in 2025-OS-K6b (hier geführt, Typ bei prozentrechnung.md) ist der Anteil 5 von 11 in Prozent der Haupttyp „Prozentsatz berechnen“.
- 1.5 Summe der relativen Häufigkeiten prüfen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Fehlenden Prozentanteil ergänzen“. Grund: Vorstufe desselben Verfahrens: die Anteile ergänzen sich zu 100 % (Definition „fehlenden Prozentsatz als Rest zu 100 %“, 2021-OS-K5b, hier geführt, Typ bei prozentrechnung.md).
- 1.6 häufigster und seltenster Wert → „Modalwert bestimmen“ · „Kenngrößen einer Liste prüfen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Modalwert (häufigster Wert)“ (2016-GYM-K3c, 2023-GYM-K5c); in 2025-OS-K6a ist der häufigste Wert 2 (fünfmal) zu bestimmen, um die falsche Modalwert-Aussage zu berichtigen.
- 1.7 relative Häufigkeit aus einem Diagramm (Anzahl und Gesamtzahl ablesen) → „Relative Häufigkeit angeben“ · „Wert aus Diagramm ablesen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Kontextvariante des Quotienten aus Anzahl und Gesamtzahl (Definition „Relative Häufigkeit angeben“), die Anzahlen liefert das Ablesen an der Skala (Definition „Wert aus Diagramm ablesen“); kein Original verbindet beides.
- 1.8 Anzahl aus relativer Häufigkeit und Gesamtzahl (Umkehrung) → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Prozentwert berechnen“. Grund: Anzahl gleich Anteil mal Gesamtzahl ist der Prozentwert (Definition „aus Grundwert und Prozentsatz den Prozentwert“); 2019-OS-K5a rechnet 23 % von 1 200 Befragten (Typ bei prozentrechnung.md).
- 1.9 zwei Gruppen verschiedener Größe über relative Häufigkeiten vergleichen → kein P10-Typ
- 1.10 Fehler finden (absolute Zahl als relative Häufigkeit angegeben; durch die Zahl der anderen statt durch alle geteilt) → kein P10-Typ
- 1.11 Begründen (warum relative Häufigkeiten zwei Klassen vergleichbar machen) → kein P10-Typ
- 1.12 Klassen zu einer Urliste bilden (gleich breit, Randregel) → kein P10-Typ
- 1.13 Häufigkeitstabelle mit Klassen auszählen → kein P10-Typ
- 1.14 Säulendiagramm der Klassen zeichnen → kein P10-Typ
- 1.15 Aussage aus der Klassentabelle prüfen (in welcher Klasse liegen die meisten) → kein P10-Typ

**Einheit 2 · Säulen-, Balken- und Liniendiagramme** – P10-Jahrgänge 11 von 13 (davon Haupt 11); P10-Typen 7; Summe ertrag 43.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Wert aus Diagramm ablesen | 3 | 2 | 2 | 2015 | 2016 | 0 | 2 |  |
| Werte im Diagramm nach Bedingung auswählen | 2 | 2 | 2 | 2016 | 2020 | 0 | 2 |  |
| Achsenskalierung aus Säule bestimmen | 5 | 2 | 2 | 2018 | 2023 | 0 | 2 |  |
| Säulen- oder Balkendiagramm ergänzen | 3 | 2 | 3 | 2020 | 2026 | 0 | 3 |  |
| Minimum und Maximum ablesen | 5 | 2 | 2 | 2014 | 2022 | 0 | 2 | nicht in der Zuordnungszeile der Einheit |
| Spannweite berechnen | 17 | 7 | 7 | 2014 | 2026 | 1 | 7 | nicht in der Zuordnungszeile der Einheit |
| Aussage zu Diagramm prüfen | 8 | 3 | 3 | 2018 | 2022 | 0 | 3 | nicht in der Zuordnungszeile der Einheit |

- 2.1 Wert einer Säule an der Skala ablesen (Hilfslinien zählen) → „Wert aus Diagramm ablesen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „Einzelwert einer Kategorie … an der Skala ablesen“; 2016-OS-K2b (Säule 2015 auf Höhe 250).
- 2.2 Achsenbeschriftung „in Tausend“, „in Mio.“, „in %“ anwenden → „Wert aus Diagramm ablesen“ · „Werte im Diagramm nach Bedingung auswählen“ – P10-Jahrgänge 3 (Haupt 3). Grund: Definition „ggf. mit Einheit ‚in Tausend‘ umrechnen“ (2016-OS-K2b: 250 Tausend sind 250 000 Besucher); 2016-OS-K2a vergleicht Säulen „in Tausend“ mit der Schwelle 300 000.
- 2.3 Werte über oder unter einer Schwelle auswählen (Grenzwert zählt nicht mit) → „Werte im Diagramm nach Bedingung auswählen“ – P10-Jahrgänge 2 (Haupt 2). Grund: 2020-OS-K2b (mehr als 190 Besucher, der Freitag mit genau 190 zählt nicht) und 2016-OS-K2a (weniger als 300 000).
- 2.4 größte und kleinste Säule, Differenz zweier Säulen → „Minimum und Maximum ablesen“ · „Spannweite berechnen“ – P10-Jahrgänge 8 (Haupt 8). Grund: 2022-OS-K4a liest kleinste und größte Säule ab; die Differenz der größten und der kleinsten Säule ist die Spannweite am Besucherdiagramm in 2020-OS-K2d (280 − 130).
- 2.5 Achseneinteilung aus einer Säule mit bekanntem Wert bestimmen → „Achsenskalierung aus Säule bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „aus einer Säule mit bekanntem Wert die fehlende Einteilung der Achse ermitteln“; 2023-OS-K6d (50 Mio. je Kästchen), 2018-OS-K3a (20 je Gitterlinie).
- 2.6 unbeschriftete Säule anhand der Höhe zuordnen → „Achsenskalierung aus Säule bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „… und weitere Säulen zuordnen“; 2023-OS-K6d (unbeschriftete Säule ist Hindi), 2018-OS-K3a (Balken den Gerichten zuordnen).
- 2.7 Säule oder Balken mit gegebenem Wert ergänzen → „Säulen- oder Balkendiagramm ergänzen“ – P10-Jahrgänge 3 (Haupt 2). Grund: 2020-OS-K2a (Balken 180), 2026-FOR-K3d (Säule 1,85), Nebenleistung in 2023-OS-K6d (Säule Arabisch).
- 2.8 Diagramm aus einer Tabelle zeichnen (Skala wählen) → „Säulen- oder Balkendiagramm ergänzen“ – P10-Jahrgänge 3 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Achseneinteilung wählen“. Grund: Die Säulen trägt „Säulen- oder Balkendiagramm ergänzen“ ab (2026-FOR-K3d), die Skala zu einer Tabelle wählt „Achseneinteilung wählen“ (Definition, 2021-OS-K6b, Typ bei zuordnungen.md); 2023-OS-K6d verlangt Achsenbeschriftung und Säule zusammen.
- 2.9 Liniendiagramm lesen (Verlauf, Anstieg, Rückgang) → „Wert aus Diagramm ablesen“ · „Aussage zu Diagramm prüfen“ – P10-Jahrgänge 5 (Haupt 5). Grund: Die Definition von „Wert aus Diagramm ablesen“ nennt das Liniendiagramm (2018-GYM-K3d: Maximum der Hoch-Kurve); Verlauf, Anstieg und Rückgang beurteilt „Aussage zu Diagramm prüfen“ (Definition „Behauptung über Verlauf oder Veränderung“, 2022-OS-K4c).
- 2.10 Fehler finden (Hilfslinie als 100 statt 10 gelesen; „in Tausend“ übersehen; Grenzwert mitgezählt) → kein P10-Typ
- 2.11 Begründen (warum für Zeitverläufe Säulen oder Linien, nicht ein Kreis) → kein P10-Typ

**Einheit 3 · Streifen- und Kreisdiagramm** – P10-Jahrgänge 7 von 13 (davon Haupt 4); P10-Typen 4; Summe ertrag 11.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Streifendiagramm zeichnen | 2 | 1 | 1 | 2018 | 2018 | 0 | 1 |  |
| Kreisdiagramm zeichnen | 3 | 1 | 3 | 2015 | 2025 | 0 | 1 |  |
| Mittelpunktswinkel berechnen | 0 | 0 | 4 | 2015 | 2024 | 0 | 0 |  |
| Sektor im Kreisdiagramm zuordnen | 6 | 2 | 4 | 2017 | 2024 | 0 | 2 |  |

- 3.1 Anteil in Prozent → Streifenabschnitt (1 mm je 1 % bei 10 cm) → „Streifendiagramm zeichnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Prozentanteile als Abschnitte eines vorgegebenen Streifens (Gesamtlänge = 100 %) abtragen“; 2018-OS-K3c (Streifen 10 cm).
- 3.2 Streifen mit vier Abschnitten zeichnen und beschriften → „Streifendiagramm zeichnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2018-OS-K3c trägt vier Abschnitte (10 %, 15 %, 55 %, 20 %) ab und beschriftet sie; 2023-GYM-K5a mit drei Abschnitten.
- 3.3 Prozent → Mittelpunktswinkel (Anteil mal 360°) → „Mittelpunktswinkel berechnen“ · „Kreisdiagramm zeichnen“ – P10-Jahrgänge 5 (Haupt 1). Grund: Definition „Kreisdiagramm zeichnen“: Anteil in Prozent in den Mittelpunktswinkel umrechnen; 2022-OS-K4d (0,16 · 360°) und 2017-OS-K2c (0,112 · 360°).
- 3.4 Bruchteil oder Anzahl → Winkel (12 von 508) → „Mittelpunktswinkel berechnen“ · „Kreisdiagramm zeichnen“ – P10-Jahrgänge 5 (Haupt 1). Grund: Definition „Mittelpunktswinkel … aus Teil und Ganzem“ (2024-OS-K2c: 12 : 508 · 360°); 2025-OS-K6b und 2015-OS-K7c zeichnen den Sektor aus Anzahlen (5 von 11, 12 von 83).
- 3.5 Sektor mit dem Geodreieck ab dem Radius zeichnen → „Kreisdiagramm zeichnen“ – P10-Jahrgänge 3 (Haupt 1). Grund: Definition „als Sektor in einen Kreis eintragen“; 2015-OS-K7c (Sektor mit 52° am vorgegebenen Radius), 2017-OS-K2c (Sektor mit 40°).
- 3.6 Kreisdiagramm mit drei bis vier Sektoren aus Prozentangaben → „Kreisdiagramm zeichnen“ – P10-Jahrgänge 3 (Haupt 1). Grund: Definition „Anteil in Prozent … als Sektor eintragen“; die OS-Originale tragen je einen Sektor ein (2017-OS-K2c, 2025-OS-K6b), vollständige Kreisdiagramme mit drei bis fünf Sektoren verlangen 2019-GYM-K5a, 2022-GYM-K6a und 2020-GYM-K6c.
- 3.7 fehlenden Anteil zu 100 % ergänzen → kein P10-Typ der eigenen Themen. Außerhalb der Themen des Eintrags (zählt nicht): „Fehlenden Prozentanteil ergänzen“. Grund: Definition „fehlenden Prozentsatz als Rest zu 100 %“; 2021-OS-K5b (hier geführt, Typ bei prozentrechnung.md).
- 3.8 Sektoren nach Größe den Angaben zuordnen → „Sektor im Kreisdiagramm zuordnen“ – P10-Jahrgänge 4 (Haupt 2). Grund: Definition „unbeschrifteten Sektor anhand der Anteile einer Tabelle identifizieren“; 2024-OS-K2c, 2022-OS-K4d, Nebenleistung in 2021-OS-K5b und 2017-OS-K2c.
- 3.9 Anteil aus einem Sektor schätzen (Viertel, Drittel, Hälfte) → „Sektor im Kreisdiagramm zuordnen“ – P10-Jahrgänge 4 (Haupt 2). Außerhalb der Themen des Eintrags (zählt nicht): „Kreissektor Anteil berechnen“. Grund: Die Größe eines Sektors als Anteil einschätzen ist der Schritt beim Zuordnen (2022-OS-K4d: 18 %, 27 %, 39 % nach Größe); rechnerisch ist es der „Anteil eines Kreissektors an der Kreisfläche aus dem Mittelpunktswinkel“ (2025-OS-B1e, Typ bei kreis.md).
- 3.10 Fehler finden (Prozent als Grad eingetragen; Winkel als Prozent des Grundwerts; Sektor nach Reihenfolge statt Größe zugeordnet) → kein P10-Typ
- 3.11 Begründen (warum 1 % genau 3,6° sind) → kein P10-Typ

**Einheit 4 · Kenngrößen** – P10-Jahrgänge 12 von 13 (davon Haupt 12); P10-Typen 8; Summe ertrag 45.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Arithmetisches Mittel berechnen | 17 | 8 | 9 | 2015 | 2026 | 3 | 6 |  |
| Median bestimmen | 3 | 2 | 2 | 2015 | 2024 | 2 | 0 |  |
| Spannweite berechnen | 17 | 7 | 7 | 2014 | 2026 | 1 | 7 |  |
| Minimum und Maximum ablesen | 5 | 2 | 2 | 2014 | 2022 | 0 | 2 |  |
| Fehlenden Wert aus Mittelwert bestimmen | 1 | 1 | 1 | 2022 | 2022 | 1 | 0 |  |
| Kenngrößen einer Liste prüfen | 2 | 1 | 1 | 2025 | 2025 | 0 | 1 |  |
| Veränderung des Mittelwerts begründen | 0 | 0 | 1 | 2025 | 2025 | 0 | 0 |  |
| Modalwert bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 4.1 Minimum und Maximum aus Liste, Tabelle, Diagramm → „Minimum und Maximum ablesen“ · „Spannweite berechnen“ – P10-Jahrgänge 8 (Haupt 8). Grund: 2014-OS-K4a (Tabelle), 2022-OS-K4a (Säulendiagramm); 2023-OS-K6c fragt Minimum und Maximum als eigene Angaben vor der Spannweite.
- 4.2 Spannweite (auch Dezimalzahlen und große Zahlen) → „Spannweite berechnen“ – P10-Jahrgänge 7 (Haupt 7). Grund: Definition „Differenz von Maximum und Minimum“; Dezimalzahlen in 2019-OS-B1i (0,4 m) und 2026-FOR-K3a (0,08 €), große Zahlen in 2023-OS-K6c (1010 Mio.).
- 4.3 Modalwert → „Modalwert bestimmen“ · „Kenngrößen einer Liste prüfen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „Modalwert (häufigster Wert)“ (2016-GYM-K3c, 2020-GYM-K6c, 2023-GYM-K5c); in 2025-OS-K6a ist der angegebene Modalwert 4 auf 2 zu berichtigen.
- 4.4 Median bei ungerader Anzahl (sortieren) → „Median bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „nach dem Sortieren bestimmen“; 2015-OS-B1f (sieben Werte, der vierte ist 5 °C).
- 4.5 Median bei gerader Anzahl → „Median bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „bei gerader Anzahl als Mitte der beiden mittleren Werte“; 2024-OS-B1h (sechs Werte, 19 °C).
- 4.6 arithmetisches Mittel aus einer Liste → „Arithmetisches Mittel berechnen“ – P10-Jahrgänge 9 (Haupt 8). Grund: Definition „Durchschnitt einer Datenliste“; 2021-OS-B1f, 2017-OS-B1h, 2016-OS-B1a.
- 4.7 aus Tabelle oder Diagramm → „Arithmetisches Mittel berechnen“ – P10-Jahrgänge 9 (Haupt 8). Grund: Werte aus einem Diagramm in 2020-OS-K2c (Besucher), 2022-OS-K4a (Bücher-Säulen, Nebentyp) und 2024-OS-K2b (Niederschläge).
- 4.8 sinnvoll runden (Zuschauer je Spiel) → „Arithmetisches Mittel berechnen“ – P10-Jahrgänge 9 (Haupt 8). Grund: 2015-OS-K7a: 680 353 : 17 = 40 020,76 …, auf ganze Zuschauer oder Tausender sinnvoll gerundet.
- 4.9 Mittel aus Gesamtsumme und Anzahl → „Arithmetisches Mittel berechnen“ – P10-Jahrgänge 9 (Haupt 8). Grund: Aus der Summe durch die Anzahl in 2015-OS-K7a (680 353 Zuschauer auf 17 Heimspiele) und 2024-OS-K2b (Jahressumme 581,7 mm durch 12).
- 4.10 fehlender Wert aus Mittelwert und den übrigen Werten → „Fehlenden Wert aus Mittelwert bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „aus dem Mittelwert und den übrigen Werten einer Liste den fehlenden Wert“; 2022-OS-B1d (7 · 20 − 122 = 18 °C), 2023-GYM-K5d.
- 4.11 Mittelwert nach Hinzufügen oder Entfernen begründen → „Veränderung des Mittelwerts begründen“ – P10-Jahrgänge 1 (Haupt 0). Grund: Der P10-Typ verlangt genau diese Begründung (Definition „Erklären, wie sich Hinzufügen oder Entfernen einzelner Werte auf den Mittelwert auswirkt“); 2025-OS-K6c (Nebentyp).
- 4.12 Aussagen zu Kenngrößen prüfen und korrigieren → „Kenngrößen einer Liste prüfen“ – P10-Jahrgänge 1 (Haupt 1). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: Definition „Aussagen zu Spannweite, Modalwert, Median oder Mittelwert … prüfen und korrigieren“ (2025-OS-K6a); Behauptungen zu Kenngrößen prüfen 2020-OS-K2d (Spannweite 150) und 2026-FOR-K3b (Durchschnitt unter 1,80 €), beide mit Nebentyp „Behauptung prüfen“.
- 4.13 Mittelwert und Median vergleichen (Ausreißer) → kein P10-Typ
- 4.14 Fehler finden (Median ohne Sortieren; Spannweite als Intervall; Mittel aus Minimum und Maximum; durch die falsche Anzahl geteilt) → kein P10-Typ
- 4.15 Begründen (warum der Median bei Ausreißern der bessere „typische Wert“ ist) → kein P10-Typ

**Einheit 5 · Diagramme beurteilen und Boxplot** – P10-Jahrgänge 5 von 13 (davon Haupt 5); P10-Typen 2; Summe ertrag 11.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Aussage zu Diagramm prüfen | 8 | 3 | 3 | 2018 | 2022 | 0 | 3 |  |
| Verzerrung eines Diagramms erklären | 3 | 2 | 3 | 2014 | 2026 | 0 | 2 |  |

- 5.1 Aussage zum Verlauf prüfen („immer weniger“ – gibt es einen Anstieg dazwischen?) → „Aussage zu Diagramm prüfen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2022-OS-K4c prüft „Von Jahr zu Jahr lesen immer weniger“ trotz Anstieg 2018 → 2019, mit Nebentyp „Behauptung prüfen“; ebenso 2019-OS-K5c („nimmt von Jahr zu Jahr extrem ab“).
- 5.2 Aussage zur Veränderung prüfen („mehr als die Hälfte“, „um ein Drittel mehr“) → „Aussage zu Diagramm prüfen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Prozentuale Veränderung berechnen“ · „Behauptung prüfen“. Grund: „Um mehr als die Hälfte reduziert“ prüft 2022-OS-K4c, „Abnahme um 75 %“ 2022-GYM-K6c; „ein Drittel mehr“ weist 2020-OS-K2d mit den Nebentypen „Prozentuale Veränderung berechnen“ und „Behauptung prüfen“ nach.
- 5.3 „jede 15.“ gegen 15 % → „Aussage zu Diagramm prüfen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Prozent und Anteil umwandeln“ · „Behauptung prüfen“. Grund: 2018-OS-K3d: „jede 15. Frau“ als 1/15 ≈ 6,7 % gegen 15 % im Diagramm, mit den Nebentypen „Prozent und Anteil umwandeln“ (Typ bei prozentrechnung.md) und „Behauptung prüfen“.
- 5.4 zwei Teilaussagen getrennt prüfen → „Aussage zu Diagramm prüfen“ – P10-Jahrgänge 3 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: Zwei Teilbehauptungen getrennt prüfen 2022-OS-K4c (Fehlerquelle „nur den ersten Teil prüfen“) und 2018-OS-K3d, zwei Aussagen nachweisen 2020-OS-K2d, alle mit Nebentyp „Behauptung prüfen“.
- 5.5 abgeschnittene Achse erklären (Säulenhöhe zeigt nur den Teil über dem Achsenanfang) → „Verzerrung eines Diagramms erklären“ – P10-Jahrgänge 3 (Haupt 2). Grund: Definition „abgeschnittene Achse“; 2014-OS-K3d (ab 1060 €), 2026-FOR-K3e (ab 1,75 €), Nebentyp in 2019-OS-K5c (ab 30 %).
- 5.6 gedehnte Achse → „Verzerrung eines Diagramms erklären“ – P10-Jahrgänge 3 (Haupt 2). Grund: Definition „abgeschnittene Achse, Skalierung“; 2014-OS-K3d: die y-Achse ist abgeschnitten und stark gedehnt.
- 5.7 Fortschreibung eines Trends prüfen → „Aussage zu Diagramm prüfen“ – P10-Jahrgänge 3 (Haupt 3). Grund: 2019-OS-K5c: „in wenigen Jahren liest kein Jugendlicher mehr ein Buch“ – bei zwei Prozentpunkten je Jahr erst nach rund 18 Jahren, die Fortschreibung ist unzulässig.
- 5.8 Diagramm mit Achse ab 0 neu skizzieren und vergleichen → kein P10-Typ
- 5.9 Boxplot lesen (Median, Quartile, Spannweite, Box) → kein P10-Typ
- 5.10 Boxplot zeichnen (Vorrat) → kein P10-Typ
- 5.11 zwei Boxplots vergleichen (Vorrat) → kein P10-Typ
- 5.12 Fehler finden (Verdopplung der Säulenhöhe als Verdopplung des Werts; nur „die Säulen sind verschieden hoch“ ohne die Achse) → „Verzerrung eines Diagramms erklären“ – P10-Jahrgänge 3 (Haupt 2). Grund: Der P10-Typ verlangt genau diese Fehleranalyse: 2026-FOR-K3e erklärt Fabios Schluss von der verdoppelten Säulenhöhe auf den verdoppelten Preis, und die Fehlerquelle von 2014-OS-K3d ist die Antwort „die Säulen sind unterschiedlich hoch“ ohne Bezug zur Achse.
- 5.13 Begründen (warum die Achse bei 0 beginnen sollte) → „Verzerrung eines Diagramms erklären“ – P10-Jahrgänge 3 (Haupt 2). Grund: Definition „Erklären, warum ein Diagramm (abgeschnittene Achse, Skalierung) einen falschen Eindruck erzeugt“ ist dieselbe Begründung am konkreten Diagramm (2014-OS-K3d, 2026-FOR-K3e).

**Einheit 7 · Vierfeldertafel (Sek I)** – P10-Jahrgänge 0 von 13 (davon Haupt 0); P10-Typen 0; Summe ertrag 0 – keine P10-Aufgabe.

- 7.1 Tafel mit gegebenen Zahlen ausfüllen und Summen bilden → kein P10-Typ
- 7.2 fehlendes Feld aus Zeilen- oder Spaltensumme berechnen → kein P10-Typ
- 7.3 Tafel aus einem Text aufstellen (Merkmale benennen, Zahlen einordnen) → kein P10-Typ
- 7.4 Anteil an allen als Bruch und in Prozent → kein P10-Typ
- 7.5 Anteil innerhalb einer Zeile („von den 120 Mädchen“) → kein P10-Typ
- 7.6 beide Anteile zu derselben Zelle unterscheiden → kein P10-Typ
- 7.7 Aussage prüfen („mehr als die Hälfte der Brillenträger sind Jungen“) → kein P10-Typ
- 7.8 Fehler finden (falsche Bezugsgröße) → kein P10-Typ
- 7.9 Begründen (warum die Anteile einer Zeile zusammen eins ergeben) → kein P10-Typ

### wahrscheinlichkeit

themen.csv: „Wahrscheinlichkeit mehrstufig“, „Wahrscheinlichkeit einstufig“, „Zählen und Kombinatorik“.
P10-Typen der Themen ohne Einheit in diesem Eintrag: „Gleichverteilung der Trefferwahrscheinlichkeit begründen“.

**Einheit 1 · Zählen und Ergebnismengen** – P10-Jahrgänge 6 von 13 (davon Haupt 5); P10-Typen 6; Summe ertrag 13.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Ergebnismenge aufzählen | 5 | 3 | 4 | 2017 | 2025 | 1 | 2 |  |
| Anzahl der Anordnungen bestimmen | 6 | 2 | 2 | 2016 | 2017 | 0 | 2 |  |
| Größte Zahl aus Ziffern bilden | 1 | 1 | 1 | 2016 | 2016 | 0 | 1 |  |
| Anzahl der Dreiecke aus Punkten bestimmen | 1 | 1 | 1 | 2015 | 2015 | 0 | 1 |  |
| Anzahl Kombinationen nach dem Zählprinzip bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 1.1 Möglichkeiten aufzählen (Kleidung, Menü, Wege) und zählen → „Ergebnismenge aufzählen“ · „Anzahl Kombinationen nach dem Zählprinzip bestimmen“ – P10-Jahrgänge 4 (Haupt 3). Grund: Systematisches Auflisten wie in 2017-OS-B1f und 2025-OS-K3a, hier als Kontextvariante außerhalb eines Zufallsversuchs; das Zählen von Menü-Kombinationen verlangt 2017-GYM-K5d (belegte Brötchen, 2 · 6 · 2 = 24).
- 1.2 Zählprinzip: Anzahl der Kombinationen als Produkt → „Anzahl Kombinationen nach dem Zählprinzip bestimmen“ · „Anzahl der Anordnungen bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „durch Multiplikation der jeweiligen Möglichkeiten“ (2017-GYM-K5d, 2018-GYM-K5c: 4 · 4); „Anzahl der Anordnungen bestimmen“ zählt nach Definition auch über das Zählprinzip (2017-OS-K6b: 3 · 2 · 1).
- 1.3 alle zweistelligen Zahlen aus zwei Ziffernscheiben (doppelte Ziffern nur einmal) → „Ergebnismenge aufzählen“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2025-OS-K3a: neun zweistellige Zahlen aus den Scheiben 1, 2, 1, 3 und 2, 3, 2, 1.
- 1.4 Anordnungen von drei Ziffern oder drei Personen (auflisten, dann 3 · 2 · 1) → „Anzahl der Anordnungen bestimmen“ – P10-Jahrgänge 2 (Haupt 2). Grund: Definition „durch Auflisten oder Zählprinzip“; 2016-OS-K5b (sechs Zahlen aus 2, 3, 6 auflisten), 2017-OS-K6b (3 · 2 · 1 = 6).
- 1.5 größte und kleinste Zahl aus Ziffern → „Größte Zahl aus Ziffern bilden“ – P10-Jahrgänge 1 (Haupt 1). Grund: Definition „die größte (oder kleinste) Zahl bilden“; 2016-OS-K5a (632).
- 1.6 Ergebnismenge zweier Münzen (ZZ, ZW, WZ, WW) → „Ergebnismenge aufzählen“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2017-OS-B1f: zwei Münzen, vier Ergebnisse ZZ, ZW, WZ, WW (ebenso 2017-GYM-B1f).
- 1.7 Paare beim zweifachen Würfeln mit Bedingung (zweiter Wurf 2) → „Ergebnismenge aufzählen“ – P10-Jahrgänge 4 (Haupt 3). Grund: 2020-OS-K6a: alle Augenpaare mit zweiter Augenzahl 2 aufzählen.
- 1.8 Ergebnisse zu „mindestens einmal …“ aufzählen → „Ergebnismenge aufzählen“ – P10-Jahrgänge 4 (Haupt 3). Grund: Nebenleistung in 2018-OS-K7c: alle Ergebnisse mit mindestens einem Senf-Pfannkuchen aufzählen.
- 1.9 Dreiecke aus fünf Punkten (Punkte auf einer Geraden ausschließen) → „Anzahl der Dreiecke aus Punkten bestimmen“ · „Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2015-OS-K5a (8 Dreiecke, Punkte auf einer Geraden ausgeschlossen); sein Rechenweg „10 Dreierauswahlen aus 5 Punkten“ ist die Auswahl ohne Reihenfolge der Definition „Kombination ohne Wiederholung“ (2019-GYM-K5b: fünf über drei gleich 10).
- 1.10 Fehler finden (ZW und WZ als ein Ergebnis; Kombination vergessen; 3³ statt 3 · 2 · 1) → kein P10-Typ
- 1.11 Begründen (warum die Liste vollständig ist – Ordnung nach dem ersten Element) → kein P10-Typ

**Einheit 2 · Wahrscheinlichkeit einstufig** – P10-Jahrgänge 10 von 13 (davon Haupt 9); P10-Typen 5; Summe ertrag 36.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Wahrscheinlichkeit einstufig | 19 | 8 | 9 | 2014 | 2026 | 4 | 9 |  |
| Zufallsgerät zu Wahrscheinlichkeit entwerfen | 6 | 4 | 4 | 2018 | 2026 | 2 | 2 |  |
| Wahrscheinlichkeit über Gegenereignis berechnen | 2 | 1 | 1 | 2026 | 2026 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Wahrscheinlichkeit mehrstufig ohne Zurücklegen | 9 | 3 | 5 | 2015 | 2024 | 0 | 3 | nicht in der Zuordnungszeile der Einheit |
| Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 2.1 P eines Ergebnisses beim Würfel, Glücksrad mit gleich großen Feldern, Urne → „Wahrscheinlichkeit einstufig“ – P10-Jahrgänge 9 (Haupt 8). Grund: Definition „günstige durch mögliche Fälle“; Würfel 2026-FOR-K6a, Glücksrad 2014-OS-K6a, Stiftekiste 2019-OS-K6a.
- 2.2 P als Bruch, gekürzt, als Dezimalzahl und Prozent → „Wahrscheinlichkeit einstufig“ – P10-Jahrgänge 9 (Haupt 8). Außerhalb der Themen des Eintrags (zählt nicht): „Prozent und Anteil umwandeln“. Grund: P als Bruch und in Prozent in 2014-OS-K6a (3/8 = 37,5 %) und 2017-OS-K6a (1/10 = 10 %), beide mit Nebentyp „Prozent und Anteil umwandeln“ (Typ bei prozentrechnung.md).
- 2.3 Ereignis aus mehreren Ergebnissen (Summenregel: „gerade Zahl“, „weder 1 noch 6“) → „Wahrscheinlichkeit einstufig“ – P10-Jahrgänge 9 (Haupt 8). Grund: 2014-OS-B1d („weder 1 noch 6“: 4/6) und Nebenleistung in 2016-OS-K5b (P(gerade) = 4/6).
- 2.4 Gesamtzahl aus dem Text finden (Nieten plus Gewinne; Lose 101 bis 900 sind 800) → „Wahrscheinlichkeit einstufig“ – P10-Jahrgänge 9 (Haupt 8). Grund: 2014-OS-B1b (80 Nieten und 20 Gewinne), 2016-OS-B1f (100 Lampen, 5 kaputt), 2016-OS-K5c (Lose 101 bis 900 sind 800).
- 2.5 Gegenereignis einstufig (1 − P) → „Wahrscheinlichkeit über Gegenereignis berechnen“ · „Wahrscheinlichkeit einstufig“ – P10-Jahrgänge 9 (Haupt 8). Grund: Definition „über 1 − P(Gegenereignis)“, der einstufige Fall ist der Grundfall desselben Verfahrens; 2014-OS-B1d löst „weder 1 noch 6“ auch als 1 − 2/6.
- 2.6 Zufallsgerät entwerfen: Anzahl der Felder oder Kugeln zu gegebener Wahrscheinlichkeit; Kugeln einzeichnen; Topf mit P = 50 % auswählen → „Zufallsgerät zu Wahrscheinlichkeit entwerfen“ · „Wahrscheinlichkeit einstufig“ – P10-Jahrgänge 10 (Haupt 9). Grund: Felder und Kugeln zu einer Wahrscheinlichkeit in 2018-OS-B1j (40 % sind 2 von 5 Feldern) und 2019-OS-B1g (Kugeln einzeichnen); den Topf mit P = 50 % wählt 2015-OS-B1a mit Haupttyp „Wahrscheinlichkeit einstufig“.
- 2.7 veränderte Grundmenge (zwei Pfannkuchen sind schon weg) → „Wahrscheinlichkeit einstufig“ · „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ – P10-Jahrgänge 9 (Haupt 8). Grund: 2018-OS-K7b (nach zwei entnommenen Pfannkuchen 2/14 statt 2/16); die nach einer Entnahme verkleinerte Grundmenge ist die Stufe der Definition „ohne Zurücklegen“ (2015-GYM-K3c: nach Lisas Zug bleiben 5 Plätze).
- 2.8 Grundmenge einschränken (nur die Lose mit Endziffer 6) → „Wahrscheinlichkeit einstufig“ – P10-Jahrgänge 9 (Haupt 8). Grund: 2016-OS-K5d: nur die 80 Lose mit Endziffer 6 bilden die Grundmenge, P = 7/80.
- 2.9 relative Häufigkeit einer Versuchsreihe mit P vergleichen; erwartete Anzahl bei n Versuchen → „Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen“ – P10-Jahrgänge 0 (Haupt 0). Grund: Die erwartete Anzahl ist das „Produkt aus Wahrscheinlichkeit und Anzahl“ der Definition (2025-GYM-K6b: 1000 · 0,015 = 15); den Vergleich einer Versuchsreihe mit P verlangt kein P10-Typ.
- 2.10 Behauptung prüfen → „Wahrscheinlichkeit einstufig“ – P10-Jahrgänge 9 (Haupt 8). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: Einstufige Behauptungen mit Nebentyp „Behauptung prüfen“ in 2016-OS-K5c (P = 1/800), 2016-OS-K5d (P = 7/80) und 2018-OS-K7b (Pias 2/16).
- 2.11 Fehler finden (5/95; 20/80; Sektoren gezählt statt Anteile; 40 % als vier Felder) → kein P10-Typ
- 2.12 Begründen (warum Laplace nur bei gleich großen Feldern gilt) → kein P10-Typ

**Einheit 3 · Baumdiagramm und Pfadregeln** – P10-Jahrgänge 8 von 13 (davon Haupt 8); P10-Typen 6; Summe ertrag 43.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Baumdiagramm ergänzen | 25 | 6 | 6 | 2014 | 2026 | 0 | 7 |  |
| Wahrscheinlichkeit mehrstufig unabhängig | 10 | 3 | 5 | 2014 | 2026 | 0 | 4 |  |
| Wahrscheinlichkeit über Gegenereignis berechnen | 2 | 1 | 1 | 2026 | 2026 | 0 | 1 |  |
| Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |
| Zufallsgerät zu Wahrscheinlichkeit entwerfen | 6 | 4 | 4 | 2018 | 2026 | 2 | 2 | nicht in der Zuordnungszeile der Einheit |
| Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 3.1 Baum zu zwei Drehungen oder zwei Würfeln zeichnen → „Baumdiagramm ergänzen“ – P10-Jahrgänge 6 (Haupt 6). Grund: Die P10 gibt das Astgerüst vor und verlangt alle Wahrscheinlichkeiten: 2014-OS-K6b (zwei Drehungen, nur P(C) = 1/8 eingetragen), 2026-FOR-K6b (zwei Würfel).
- 3.2 Astwahrscheinlichkeiten ergänzen (Summe an jedem Punkt 1) → „Baumdiagramm ergänzen“ – P10-Jahrgänge 6 (Haupt 6). Grund: Definition „Fehlende Wahrscheinlichkeiten in einem Baumdiagramm eintragen (Knotensumme 1)“; 2014-OS-K6b, 2024-OS-K5b.
- 3.3 P eines Pfades (Pfadregel) → „Wahrscheinlichkeit mehrstufig unabhängig“ – P10-Jahrgänge 5 (Haupt 3). Grund: Definition „mit Pfad- und Summenregel“; ein Pfad in 2025-OS-K3b (P(33) = 1/4 · 1/4) und 2026-FOR-K6b (3/6 · 5/6).
- 3.4 P eines Ereignisses aus mehreren Pfaden (Summenregel: „12 oder 21“) → „Wahrscheinlichkeit mehrstufig unabhängig“ – P10-Jahrgänge 5 (Haupt 3). Grund: 2025-OS-K3c: P(12 oder 21) = 4/16 + 1/16 = 5/16.
- 3.5 „zweimal derselbe Buchstabe“ (drei Pfade) → „Wahrscheinlichkeit mehrstufig unabhängig“ – P10-Jahrgänge 5 (Haupt 3). Grund: 2014-OS-K6c: zweimal derselbe Buchstabe als Summe der Pfade AA, BB und CC.
- 3.6 „mindestens einmal“ über 1 − P(nie) → „Wahrscheinlichkeit über Gegenereignis berechnen“ · „Wahrscheinlichkeit mehrstufig unabhängig“ – P10-Jahrgänge 5 (Haupt 4). Grund: Definition „mit ‚mindestens‘ formuliertes Ereignis über 1 − P(Gegenereignis)“; P(nie) ist ein Pfad mit unabhängigen Stufen (2024-GYM-K6b: in keiner der drei Nächte 0,8³).
- 3.7 „nicht zweimal gerade“ → „Wahrscheinlichkeit über Gegenereignis berechnen“ – P10-Jahrgänge 1 (Haupt 1). Grund: 2026-FOR-K6c: P(nicht zweimal gerade) = 1 − 3/36 = 11/12.
- 3.8 dreistufig („mindestens zwei Sechsen“) → „Wahrscheinlichkeit mehrstufig unabhängig“ · „Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen“ – P10-Jahrgänge 5 (Haupt 3). Grund: 2020-OS-K6c berechnet P(mindestens zwei Sechsen) über drei Stufen (Nebentyp „mehrstufig unabhängig“); die Pfade zu „mindestens zwei von drei“ zählt 2019-GYM-K5c.
- 3.9 Behauptung prüfen (P(22) = P(33)? P(gleich) gegen P(erst 6)) → „Wahrscheinlichkeit mehrstufig unabhängig“ – P10-Jahrgänge 5 (Haupt 3). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: Genau diese Behauptungen prüfen 2025-OS-K3b (P(33) gegen P(22)) und 2020-OS-K6b (zwei gleiche Augenzahlen gegen zuerst eine 6), beide mit Nebentyp „Behauptung prüfen“.
- 3.10 Zufallsgerät mehrstufig belegen (Produkt 1/4; Würfelnetz für P(Summe 2)) → „Zufallsgerät zu Wahrscheinlichkeit entwerfen“ · „Wahrscheinlichkeit mehrstufig unabhängig“ · „Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen“ – P10-Jahrgänge 7 (Haupt 6). Grund: Definition „ein- oder mehrstufig“: 2025-OS-K3d (P(13) = 2/4 · 2/4) und 2026-FOR-K6d (Würfel B für P(Summe 2) = 1/6), beide mit Nebentyp „mehrstufig unabhängig“; die Einzelwahrscheinlichkeit aus dem Produkt zurückrechnen verlangt auch 2025-GYM-K6c.
- 3.11 Fehler finden (Pfade multipliziert statt addiert; zweite Stufe mit verkleinertem Nenner; Anteile addiert statt multipliziert) → kein P10-Typ
- 3.12 Begründen (warum die Äste an einem Punkt zusammen 1 ergeben) → kein P10-Typ

**Einheit 4 · Ohne Zurücklegen** – P10-Jahrgänge 9 von 13 (davon Haupt 8); P10-Typen 5; Summe ertrag 46.

| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |
|---|---|---|---|---|---|---|---|---|
| Wahrscheinlichkeit mehrstufig ohne Zurücklegen | 9 | 3 | 5 | 2015 | 2024 | 0 | 3 |  |
| Baumdiagramm ergänzen | 25 | 6 | 6 | 2014 | 2026 | 0 | 7 |  |
| Wahrscheinlichkeit über Gegenereignis berechnen | 2 | 1 | 1 | 2026 | 2026 | 0 | 1 | nicht in der Zuordnungszeile der Einheit |
| Wahrscheinlichkeit mehrstufig unabhängig | 10 | 3 | 5 | 2014 | 2026 | 0 | 4 | nicht in der Zuordnungszeile der Einheit |
| Ereignis zu Wahrscheinlichkeitsterm beschreiben | 0 | 0 | 0 |  |  | 0 | 0 | nicht in der Zuordnungszeile der Einheit; nur GYM |

- 4.1 Baum für zweimal Ziehen ohne Zurücklegen (Nenner minus 1) → „Baumdiagramm ergänzen“ · „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ – P10-Jahrgänge 8 (Haupt 7). Grund: Baum mit verkleinertem Nenner in 2019-OS-K6b (16/20, 3/18) und 2015-OS-K7d (10/11, 1/10), beide mit Nebentyp „ohne Zurücklegen“ (Definition „verkleinerte Grundmenge“).
- 4.2 P zweier gleicher Farben → „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ – P10-Jahrgänge 5 (Haupt 3). Grund: 2018-OS-K7c (P(beide Marmelade) = 14/16 · 13/15, Ereignis E „beide gleich“) und 2015-GYM-K3c (beide im gleichen Zimmer).
- 4.3 zweite Person zieht (erste Stufe mitrechnen: erst kein Joker, dann Joker) → „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ – P10-Jahrgänge 5 (Haupt 3). Grund: 2024-OS-K5c: Klara zieht als Zweite den Joker, 4/5 · 1/4; ebenso 2017-GYM-K5c (zweiter Schlüssel, 6/7 · 1/6).
- 4.4 dreistufig, ein Pfad (drei rote Stifte) → „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ – P10-Jahrgänge 5 (Haupt 3). Grund: Dreistufig ein Pfad in 2019-OS-K6c (drei blaue, drei gelbe Stifte) und als Nebenleistung in 2019-OS-K6b (dreimal rot, 4/20 · 3/19 · 2/18).
- 4.5 Baum mit leeren Feldern nach verschiedenen Vorgeschichten ergänzen → „Baumdiagramm ergänzen“ · „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ – P10-Jahrgänge 8 (Haupt 7). Grund: 2019-OS-K6b (zwei leere Felder nach verschiedenen Vorgeschichten) und 2015-OS-K7d (vier leere Felder), beide Haupttyp „Baumdiagramm ergänzen“ mit Nebentyp „ohne Zurücklegen“.
- 4.6 „unter den ersten drei“ (Summe dreier Pfade oder Gegenereignis) → „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ · „Wahrscheinlichkeit über Gegenereignis berechnen“ – P10-Jahrgänge 6 (Haupt 4). Grund: 2015-OS-K7d: P(Ronny unter den ersten drei) als Summe dreier Pfade oder als 1 − 10/11 · 9/10 · 8/9 (Gegenereignis als Rechenweg laut Prüfungsform); 2018-GYM-K5d summiert zwei Pfade.
- 4.7 Vergleich mit Zurücklegen (Behauptung „doppelt so hoch“) → „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ · „Wahrscheinlichkeit mehrstufig unabhängig“ – P10-Jahrgänge 9 (Haupt 6). Außerhalb der Themen des Eintrags (zählt nicht): „Behauptung prüfen“. Grund: 2019-OS-K6c widerlegt „doppelt so hoch“ ohne Zurücklegen (Nebentyp „Behauptung prüfen“, Fehlerquelle „mit Zurücklegen rechnen“); den Vergleichswert mit Zurücklegen rechnet die Definition von „Wahrscheinlichkeit mehrstufig unabhängig“.
- 4.8 Ereignis zu einer gegebenen Rechnung in Worten → „Ereignis zu Wahrscheinlichkeitsterm beschreiben“ – P10-Jahrgänge 0 (Haupt 0). Außerhalb der Themen des Eintrags (zählt nicht): „Gleichung im Sachzusammenhang deuten“. Grund: Definition „zu einem gegebenen Wahrscheinlichkeitsterm das Ereignis in Worten beschreiben“ (2018-GYM-K4c, Nebentyp in 2019-GYM-K5c); in 2018-OS-K7c trägt dieselbe Leistung den Nebentyp „Gleichung im Sachzusammenhang deuten“ (Typ bei lineare-gleichungssysteme.md).
- 4.9 Fehler finden (Nenner nicht weitergezählt: 3/19 statt 3/18; 1/4 ohne die erste Stufe; mit Zurücklegen gerechnet) → kein P10-Typ
- 4.10 Begründen (warum sich Nenner und Zähler ändern) → kein P10-Typ

## Sek II je Eintrag

Abitur-Jahrgänge aus abi-katalog.csv (GK: 9 erfasste Jahrgänge 2018–2026; LK: 7, 2017, 2018, 2022–2026), FHR-Jahrgänge aus fhr-katalog.csv (8, 2019–2026); gezählt „Haupt oder Neben“, dazu „Haupt“ (nur als Hauptleistung); die Jahre stehen in Klammern, wenn es nicht alle sind. Der IQB-Pool zählt nicht; „nur Pool“ = der Typ hat nur Poolzeilen.

### kurvenuntersuchung

**Einheit 1 · Monotonie und erste Ableitung** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Extremstellen berechnen und Monotonieverhalten angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Monotonieintervalle und Wertebereich einer Differenzfunktion auf einem Intervall über die Ableitung ermitteln (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 1.3 Monotonie über das Vorzeichen der Ableitung am Term nachweisen (4) → wortgleich; GK 1 (2024), Haupt 1 · LK 1 (2022), Haupt 1 · FHR 0
- 1.4 Fehlende Extrempunkte über eine positive Ableitung begründen (2) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 1.5 Monotonieverhalten aus einem bekannten Extrempunkt angeben (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 1.6 Länge der Monotoniebereiche zweier Modellfunktionen vergleichen und eine Aussage beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Fehler finden (Monotonie nach dem Vorzeichen von f'' statt f' angegeben; Intervallgrenzen bei null statt an der Extremstelle; f'(x₀) = 0 an einer Stelle als Gegenargument gegen die Monotonie) → didaktischer Typ, kein Prüfungstyp
- 1.8 Begründen (warum ein Quadrat plus eine positive Zahl nie null wird; warum aus f' > 0 überall folgt, dass es keinen Extrempunkt gibt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Extrempunkte** – Abitur-Jahrgänge GK 8 von 9 (Haupt 8) · LK 6 von 7 (Haupt 5) · FHR-Jahrgänge 8 von 8 (Haupt 8).

- 2.1 Extrem- und Sattelpunkte über zweite Ableitung (17) → wortgleich; GK 0 · LK 0 · FHR 8, Haupt 8
- 2.2 Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen (8) → wortgleich; GK 5 (2018, 2019, 2020, 2024, 2025), Haupt 4 · LK 1 (2025), Haupt 1 · FHR 0
- 2.3 Lage und Art aller lokalen Extrempunkte bestimmen (6) → wortgleich; GK 6 (2018, 2020, 2021, 2022, 2023, 2024), Haupt 6 · LK 0 · FHR 0
- 2.4 Abstand zweier Extrempunkte verschiedener Graphen mit einer Schranke vergleichen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 2.5 Abstand zweier Extrempunkte über die Punktsymmetrie berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.6 Extrempunkte berechnen und ihre Verbindungsgerade als Winkelhalbierende nachweisen (1) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 2.7 Extremstellen aus den Nullstellen der Ableitung berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 2.8 Nullstellen einer e-Funktion nachweisen und Tiefstelle berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Nullstellen und Extremstelle einer Parabel berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Stellen mit maximalem Funktionswert einschließlich Rand bestimmen (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.11 Wertebereich einer ganzrationalen Funktion über den globalen Tiefpunkt ermitteln (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.12 Extrempunkt an vorgegebener Stelle nachweisen (9) → wortgleich; GK 1 (2021), Haupt 1 · LK 2 (2017, 2025), Haupt 1 · FHR 0
- 2.13 Achsenschnittpunkte angeben und Hochpunkt aus der gegebenen Ableitung begründen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 2.14 Gegebene Stelle als Extremstelle nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 1 (2021), Haupt 1
- 2.15 Anstieg null nachweisen und fehlende Extremstelle über die doppelte Nullstelle der Ableitung ohne Rechnung begründen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.16 Berührung des Graphen mit der x-Achse über die Extrempunkte begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.17 Einzigen Tiefpunkt über die streng monotone Ableitung nachweisen und berechnen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.18 Extremstelle einer Logarithmusfunktion über die Ableitung oder die Symmetrie begründen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.19 Extremstelle über den Vorzeichenwechsel der Ableitung in ein Intervall einschließen (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 2.20 Größten Funktionswert über Monotonie, Grenzverhalten und Symmetrie begründen und Wertemenge angeben (1) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 2.21 Hochpunkt mit vorgegebenen Koordinaten und waagerechte Tangente im Ursprung rechnerisch nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.22 Tiefpunkt angeben und Fehlen weiterer Extrempunkte über die Ableitung nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.23 Aussagen zu Stellen mit waagerechter Tangente beurteilen (2) → wortgleich; GK 0 · LK 0 · FHR 2 (2019, 2020), Haupt 2
- 2.24 Abstand zwischen Parabel und waagerechter Gerade über den Scheitel beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.25 Aussagen über Funktions- und Ableitungswert nahe dem Tiefpunkt ohne Rechnung beurteilen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 2.26 Fehler finden (positives f'' als Hochpunkt gedeutet; Lösung x = 0 beim Ausklammern verloren; Extremstelle statt Extremwert angegeben; e-Faktor null gesetzt) → didaktischer Typ, kein Prüfungstyp
- 2.27 Begründen (warum f'(x₀) = 0 allein nicht reicht – Sattelstelle; warum am Rand eines Intervalls ein größter Wert ohne waagerechte Tangente liegen kann) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Krümmung und Wendepunkte** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 8 von 8 (Haupt 8).

- 3.1 Wendepunkte über zweite Ableitung (11) → wortgleich; GK 0 · LK 0 · FHR 7 (2019, 2020, 2021, 2022, 2023, 2024, 2026), Haupt 7
- 3.2 Wendepunkte über die zweite Ableitung berechnen (5) → wortgleich; GK 3 (2021, 2023, 2026), Haupt 3 · LK 0 · FHR 0
- 3.3 Krümmungsverhalten angeben (3) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2022, 2024, 2025, 2026), Haupt 3
- 3.4 Gerade durch die beiden Wendepunkte aufstellen und parallele Gerade mit genau einem gemeinsamen Punkt einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Wendepunkt an vorgegebener Stelle nachweisen und Wendetangente aufstellen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Existenz eines Wendepunkts aus Tiefpunkt und Grenzverhalten über eine Skizze begründen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.7 Punktprobe am Graphen (1; fhr 2023-C-1d: Punkt auf dem Graphen und Wendepunkt prüfen – Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2023, 2024, 2025, 2026), Haupt 4
- 3.8 Wendepunkt mit vorgegebenen Koordinaten über die zweite Ableitung nachweisen und den symmetrischen Wendepunkt angeben (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.9 Wendepunkt über den Vorzeichenwechsel der zweiten Ableitung aus der Kettenregel am Graphen nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.10 Wendestelle nachweisen und Winkel der Wendetangente mit der x-Achse über die Steigung −1 zeigen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.11 Wendestellen einer Sinusfunktion als ganzzahlig nachweisen und die beiden Wendetangentensteigungen zeigen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Zweite Ableitung nachweisen und Wendepunkt an vorgegebener Stelle zeigen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 3.13 Anzahl der Schnittpunkte von Geraden durch den Wendepunkt mit dem Graphen nach der Steigung unterscheiden (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.14 Fehler finden (Links- und Rechtskrümmung vertauscht; f''' vergessen; Wendestelle ohne Funktionswert; Sattelpunkt als bloßer Wendepunkt) → didaktischer Typ, kein Prüfungstyp
- 3.15 Begründen (warum f'' das Vorzeichen wechseln muss, damit ein Wendepunkt vorliegt; warum die Wendetangente den Graphen dort durchsetzt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Graph und Ableitungsgraph** – Abitur-Jahrgänge GK 7 von 9 (Haupt 6) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen (3) → wortgleich; GK 3 (2018, 2019, 2020), Haupt 2 · LK 0 · FHR 0
- 4.2 Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.3 Gemeinsamen Punkt zweier Graphen über gleiche Flächeninhalte indirekt begründen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.4 Logarithmus einer Exponentialfunktion als lineare Funktion nachweisen und Steigung und Achsenabschnitt angeben (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.5 Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.6 Aussagen über die Normale an der Wendestelle und den Wertebereich der Ableitung beurteilen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 4.7 Graphen skizzieren und Aussage über die Anzahl gemeinsamer Punkte von Tangente und Graph beurteilen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 4.8 Lage eines Punktes aus Bedingungen an Funktionswert und Ableitung am Graphen beschreiben (1) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 4.9 Lage zweier Graphen aus dem Graphen ihrer Differenzfunktion beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Wendepunkt mit negativer Steigung am Graphen markieren und begründen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.11 Werte für einen Ableitungswert und eine Wendestelle am Graphen ablesen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.12 Fehler finden (Graph von f' als Graph von f gelesen; an der Wendestelle ein Extrempunkt gezeichnet; Ableitungswert als Funktionswert abgelesen) → didaktischer Typ, kein Prüfungstyp
- 4.13 Begründen (warum die Nullstellen von f' unter den Hoch- und Tiefpunkten von f liegen; warum der Graph von f' einen Grad einfacher ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Kurvenuntersuchung im Sachzusammenhang** – Abitur-Jahrgänge GK 7 von 9 (Haupt 7) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 4 von 8 (Haupt 4).

- 5.1 Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen (4) → wortgleich; GK 2 (2018, 2019), Haupt 2 · LK 0 · FHR 0
- 5.2 Maximum einer ganzrationalen Funktion im Sachzusammenhang über die Ableitung berechnen (2) → wortgleich; GK 1 (2019), Haupt 0 · LK 0 · FHR 0
- 5.3 Passung eines Profils in einen Karton über Breite und Tiefe aus Nullstellen und Tiefpunkt prüfen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 5.4 Funktionswert im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2024, 2025), Haupt 2
- 5.5 Maße und Masse eines umschließenden Quaders eines Rotationskörpers aus Hochpunkt und Bereich mit Maßstab berechnen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 5.6 Maximale Höhe im Sachzusammenhang berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2023, 2024), Haupt 1
- 5.7 Maximalen Neigungswinkel über die Wendestelle berechnen und mit einer Schranke vergleichen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.8 Steilsten Anstieg über den Wendepunkt bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2021), Haupt 1
- 5.9 Volumen eines umschließenden Quaders aus den Achsenschnittpunkten mit Maßstab berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.10 Maximum eines Bestands an vorgegebener Stelle im Sachzusammenhang nachweisen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 5.11 Verlauf eines Graphen im Sachzusammenhang beschreiben (4) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 5.12 Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten (4) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 5.13 Gewinnbereich als Bereich zwischen den Schnittstellen von Erlösgerade und Kostengraph zeichnerisch bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.14 Ableitungswert an der Wendestelle als stärksten Anstieg der Rate im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.15 Aufgabenstellung zu Extremstellen und Wertedifferenz aus dem Lösungsweg formulieren und erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.16 Differenzfunktion und ihr Maximum aus einem Lösungsweg im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.17 Funktionswert an der Stelle stärkster Abnahme am Graphen ablesen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.18 Mittleren Wert einer periodisch schwankenden Größe am Graphen ablesen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.19 Fehler finden (Wendepunkt als Richtungswechsel oder als Beginn der Abnahme gedeutet; Nullstelle von f' statt f'' für die stärkste Abnahme; Maßstab vergessen; flacher Abschnitt als Abnahme gelesen) → didaktischer Typ, kein Prüfungstyp
- 5.20 Begründen (warum der größte Wert auf einem Bereich am Rand liegen kann; warum die Einheit von f' aus den Einheiten von f und x folgt) → didaktischer Typ, kein Prüfungstyp

### binomialverteilung

**Einheit 1 · Bernoulli-Experiment und Bernoulli-Kette** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 3 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen (3) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.2 Ungeeignetheit des Binomialmodells begründen (4) → wortgleich; GK 1 (2018), Haupt 1 · LK 1 (2017), Haupt 0 · FHR 0
- 1.3 Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen (3) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 1.4 Wahrscheinlichkeit für mindestens zwei Treffer bei drei Versuchen nachweisen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 1.5 Aussagen über Bernoulli-Experiment und Bernoulli-Kette im Sachzusammenhang beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Zufallsgröße mit gleicher Binomialverteilung in einem anderen Experiment angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Fehler finden (Binomialverteilung bejaht, weil es nur zwei Ausgänge gibt, obwohl ohne Zurücklegen aus einer kleinen Gesamtheit gezogen wird; bei zwei Versuchen nur einen Pfad gerechnet; die Unabhängigkeit nicht genannt) → didaktischer Typ, kein Prüfungstyp
- 1.8 Begründen (warum eine große Gesamtheit das Zurücklegen ersetzt; warum ein Spiel mit drei möglichen Ausgängen keine Bernoulli-Kette liefert) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Bernoulli-Formel** – Abitur-Jahrgänge GK 6 von 9 (Haupt 6) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln (12) → wortgleich; GK 2 (2018, 2022), Haupt 2 · LK 3 (2017, 2018, 2025), Haupt 3 · FHR 0
- 2.2 Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen (8; Ermessen, siehe Offene Punkte) → wortgleich; GK 3 (2019, 2020, 2021), Haupt 3 · LK 0 · FHR 0
- 2.3 Einzelwahrscheinlichkeit einer Binomialverteilung aus n und Erwartungswert berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Stichprobenumfang aus dem Erwartungswert berechnen und Einzelwahrscheinlichkeit ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben (7) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2026), Haupt 1 · FHR 0
- 2.6 Fehler finden (Binomialkoeffizient weggelassen, nur das Produkt der Einzelwahrscheinlichkeiten; Exponenten von p und 1 − p vertauscht; Trefferdefinition beim Zählen der Nieten nicht mitgewechselt; kumulierte statt Einzelwahrscheinlichkeit am Rechner) → didaktischer Typ, kein Prüfungstyp
- 2.7 Begründen (warum jeder Pfad mit k Treffern dieselbe Wahrscheinlichkeit hat; warum die Potenz für „alle Treffer“ keinen Binomialkoeffizienten braucht) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Kumulierte Wahrscheinlichkeiten** – Abitur-Jahrgänge GK 7 von 9 (Haupt 6) · LK 5 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln (22) → wortgleich; GK 3 (2018, 2022, 2026), Haupt 2 · LK 4 (2017, 2022, 2023, 2026), Haupt 3 · FHR 0
- 3.2 Fehlerwahrscheinlichkeit einer Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden (3) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.3 Bedingung an ein Anzahlverhältnis in eine Binomialwahrscheinlichkeit übersetzen (2) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 3.4 Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.5 Bedingte Restwahrscheinlichkeit nach bekannten Ergebnissen über die Binomialverteilung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Kumulierte Binomialwahrscheinlichkeit und Pfadwahrscheinlichkeit einer festen Anfangsfolge berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Wahrscheinlichkeit einer prozentualen Abweichung vom Erwartungswert nach beiden Seiten berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Wahrscheinlichkeit eines zweistufigen Prüfplans über Binomialwahrscheinlichkeiten berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.9 Wahrscheinlichkeit für Gewinn und Extrapreis über die Aufteilung einer Bernoulli-Kette in zwei Abschnitte berechnen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.10 Wahrscheinlichkeit für zwei unabhängige Spieler als Produkt binomialer Wahrscheinlichkeiten berechnen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.11 Summenbedingung bei wiederholtem Wurf in eine Binomialwahrscheinlichkeit übersetzen und nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Summenterme der Binomialverteilung auf ein vorgegebenes Mindestens-Ereignis prüfen und begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.13 Kumulierte Binomialsumme als Sachaussage formulieren (10) → wortgleich; GK 3 (2019, 2020, 2023), Haupt 3 · LK 0 · FHR 0
- 3.14 Sachaussage zu einer Ungleichung mit Binomialsumme formulieren (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.15 Aufgabenstellung zu einer Potenz der Gegenwahrscheinlichkeit formulieren und Ansatz erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.16 Fehler finden („mehr als k“ als X ≥ k gelesen; „weniger als k“ als P(X ≤ k); beim Intervall die falsche untere Grenze abgezogen; ein Prozentanteil als Anzahl genommen; im Summenterm Treffer und Niete vertauscht; die Summe als „genau k“ gedeutet) → didaktischer Typ, kein Prüfungstyp
- 3.17 Begründen (warum „mindestens k“ über das Gegenereignis „höchstens k − 1“ läuft; warum sich eine Anteilsbedingung erst in eine ganze Zahl übersetzen lässt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Umkehraufgaben** – Abitur-Jahrgänge GK 7 von 9 (Haupt 7) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen (6) → wortgleich; GK 5 (2019, 2020, 2021, 2022, 2023), Haupt 5 · LK 1 (2017), Haupt 1 · FHR 0
- 4.2 Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer bestimmen (4) → wortgleich; GK 2 (2018, 2022), Haupt 2 · LK 0 · FHR 0
- 4.3 Grenze k einer kumulierten Wahrscheinlichkeit gegen eine Schranke mit dem Rechner ermitteln (3) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 4.4 Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln (3) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.5 Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln (3) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 4.6 Kleinste Umgebungsbreite unterhalb des Erwartungswerts für eine Mindestwahrscheinlichkeit ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Mindestanzahl von Versuchen für mindestens drei Treffer mit vorgegebener Wahrscheinlichkeit durch Probieren ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.8 Parameter n und p aus einem Verhältnis zweier Einzelwahrscheinlichkeiten und dem Erwartungswert berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.9 Stichprobenumfang zu einer vorgegebenen Einzelwahrscheinlichkeit mit dem Rechner suchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Trefferwahrscheinlichkeit aus einer Gleichung zweier Einzelwahrscheinlichkeiten berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.11 Trefferwahrscheinlichkeit aus einer kumulierten Wahrscheinlichkeit auf ganze Prozent durch Probieren ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.12 Aussage über die Halbierung einer Potenzwahrscheinlichkeit bei doppeltem Umfang allgemein widerlegen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.13 Behauptung zur Monotonie einer Wahrscheinlichkeit an Beispielwerten prüfen (1) → wortgleich; GK 1 (2018), Haupt 1 · LK 0 · FHR 0
- 4.14 Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen (2) → wortgleich; GK 1 (2018), Haupt 1 · LK 0 · FHR 0
- 4.15 Wirkung eines kleineren Stichprobenumfangs auf eine Annahmewahrscheinlichkeit ohne Rechnung beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.16 Fehler finden (beim Teilen durch einen negativen Logarithmus das Ungleichheitszeichen nicht gedreht; abgerundet statt aufgerundet; die n-te Wurzel als Division durch n; die Grenze k ohne den zweiten Nachbarwert angegeben; n aus n · p = μ statt durch Probieren) → didaktischer Typ, kein Prüfungstyp
- 4.17 Begründen (warum (1 − p)^n mit wachsendem n fällt; warum ein Wert, der die Schranke gerade nicht erreicht, mit belegt werden muss) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Verteilung im Diagramm** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 3 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 5.1 Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen (3; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 5.2 Modalwert einer Binomialverteilung bestimmen (2) → wortgleich; GK 1 (2018), Haupt 1 · LK 1 (2017), Haupt 0 · FHR 0
- 5.3 Achsen eines Verteilungsdiagramms über Erwartungswert und größte Einzelwahrscheinlichkeit skalieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.4 Einzelwahrscheinlichkeit aus dem Diagramm kumulierter Wahrscheinlichkeiten ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.5 Obere Grenze einer im Diagramm markierten kumulierten Wahrscheinlichkeit über den Erwartungswert ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.6 Wahrscheinlichkeit eines symmetrischen Intervalls über die Symmetrie der Binomialverteilung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.7 Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen (5) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.8 Aussage über eine Summe von Wahrscheinlichkeiten am Säulendiagramm entscheiden (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.9 Binomialverteilung über den Widerspruch zwischen Symmetrie und einer Einzelwahrscheinlichkeit ausschließen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 5.10 Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen (4) → wortgleich; GK 2 (2020, 2025), Haupt 2 · LK 0 · FHR 0
- 5.11 Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern (4) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2026), Haupt 1 · FHR 0
- 5.12 Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 5.13 Aussagen über Verteilungen verschiedener Gruppen am Säulendiagramm beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.14 Aussagen über kumulierte Wahrscheinlichkeit und Trefferwahrscheinlichkeit aus dem Säulendiagramm einer Binomialverteilung beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.15 Bedingung an p für das Verhältnis zweier symmetrisch liegender Einzelwahrscheinlichkeiten angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.16 Verteilung der Gegenzufallsgröße im Diagramm darstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.17 Wahrscheinlichkeit eines Intervalls aus dem Säulendiagramm einer Verteilung ablesen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.18 Fehler finden (das Maximum bei n/2 statt bei n · p vermutet; ein Diagramm nur nach der Form beurteilt, ohne die Summe der Säulen zu prüfen; bei der Gegenzufallsgröße die Säule bei k statt bei n − k gelesen; die Symmetrieachse auf eine ganze Zahl statt auf die Mitte zweier Werte gelegt; Wertebereich mit n + 1 Werten als n gelesen) → didaktischer Typ, kein Prüfungstyp
- 5.19 Begründen (warum die Säulen sich zu eins addieren müssen; warum die Verteilung nur für p = 0,5 symmetrisch ist) → didaktischer Typ, kein Prüfungstyp

### ebenen

**Einheit 1 · Parameterform einer Ebene** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Eindeutigkeit einer Ebene durch vier Punkte über die Kollinearität dreier Punkte begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Parametergleichung einer Ebene aus Punkten angeben (3; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2022), Haupt 1 · LK 1 (2018), Haupt 1 · FHR 0
- 1.3 Fehler finden (zwei parallele Vektoren als Spannvektoren gewählt, etwa AB und DC; beim Nachweis eines Punktes die Parameter aus zwei Gleichungen bestimmt und die dritte Koordinate nicht geprüft; drei Punkte auf einer Geraden für ausreichend gehalten) → didaktischer Typ, kein Prüfungstyp
- 1.4 Begründen (warum eine Ebene unendlich viele Parametergleichungen hat; warum drei Punkte auf einer Geraden keine Ebene festlegen) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Normalenvektor und Koordinatengleichung** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 5 von 7 (Haupt 5) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen (20) → wortgleich; GK 5 (2018, 2020, 2021, 2024, 2025), Haupt 5 · LK 4 (2017, 2022, 2023, 2024), Haupt 3 · FHR 0
- 2.2 Normalenvektor als Ortsvektor eines Ebenenpunktes bestimmen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.3 Konstante einer Koordinatengleichung durch Einsetzen eines Punktes bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Normalenvektor einer Ebene aus zwei Richtungsvektoren über Skalarprodukte bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Normalenvektor aus der Orthogonalität zu Vielfachen der Spannvektoren begründen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 2.6 Koordinatengleichung einer Ebene aus Gerade und Punkt nachweisen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.7 Koordinatenform einer Ebene aus der Normalenform durch Ausmultiplizieren angeben (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 2.8 Fehler finden (Konstante aus dem Ursprung oder einem Punkt außerhalb der Ebene bestimmt; Komponenten des Normalenvektors vertauscht; Vorzeichen beim Eliminieren der Parameter; Normalenvektor aus den Achsenabschnitten geraten; den Normalenvektor selbst statt eines Vielfachen als Punkt eingesetzt) → didaktischer Typ, kein Prüfungstyp
- 2.9 Begründen (warum jedes Vielfache eines Normalenvektors wieder Normalenvektor ist; warum zwei Skalarprodukte für drei Unbekannte genügen; warum die ausmultiplizierte Normalenform die Koordinatengleichung ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Ebenen im Koordinatensystem** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Lage einer Ebene zu einer Koordinatenachse aus der Koordinatengleichung begründen (3) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.2 Lage einer Figur in einer Koordinatenebene aus Eckpunkt und orthogonaler Geraden begründen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 3.3 Komponente des Normalenvektors aus der Orthogonalität zur Koordinatenebene begründen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Vertikale Lage einer Fläche über einen Normalenvektor mit x₃-Komponente null nachweisen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Achsenparallele Ebene einer Bewegung aus der Parameterdarstellung angeben (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Darstellung einer Ebene im Schrägbild als Gerade beurteilen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Übereinstimmung einer Ebene mit einer Koordinatenebene beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Fehler finden („parallel zur Achse“ gesagt, obwohl der Ursprung in der Ebene liegt und die Ebene die Achse enthält; „enthält die Achse“ behauptet, obwohl der Ursprung nicht in der Ebene liegt; die achsenparallele Ebene als Koordinatenebene selbst bezeichnet; „vertikal“ mit einem Normalenvektor in Richtung der Hochachse verwechselt; die Ebene einer Bewegung mit dem Zeitparameter in Parameterform gesucht) → didaktischer Typ, kein Prüfungstyp
- 3.9 Begründen (warum eine fehlende Variable Parallelität zur Achse bedeutet; warum der Normalenvektor einer zur Koordinatenebene senkrechten Ebene in dieser Koordinatenebene liegt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Parallele Ebenen** – Abitur-Jahrgänge GK 4 von 9 (Haupt 3) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen (3) → wortgleich; GK 3 (2019, 2020, 2022), Haupt 2 · LK 0 · FHR 0
- 4.2 Parallele Ebene mit vorgegebenem Volumenverhältnis eines Prismas ermitteln (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Parallelität zweier Ebenen über die Normalenvektoren und eine Punktprobe begründen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 4.4 Fehler finden (den Punkt in die Ausgangsebene statt in die parallele Ebene eingesetzt; nur die Parallelität genannt und „identisch“ nicht ausgeschlossen; das Volumenverhältnis auf die halbe Höhe statt auf ein Drittel übersetzt) → didaktischer Typ, kein Prüfungstyp
- 4.5 Begründen (warum parallele Ebenen denselben Normalenvektor haben; warum eine Punktprobe zwischen parallel und identisch entscheidet) → didaktischer Typ, kein Prüfungstyp

### ableitung-und-aenderungsrate

**Einheit 1 · Mittlere Änderungsrate und Sekante** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen (4) → wortgleich; GK 1 (2025), Haupt 1 · LK 1 (2024), Haupt 1 · FHR 0
- 1.2 Mittlere Änderungsrate aus dem Funktionsterm im Sachzusammenhang berechnen (3) → wortgleich; GK 1 (2019), Haupt 1 · LK 1 (2025), Haupt 1 · FHR 0
- 1.3 Sekantengleichung durch zwei Punkte eines Graphen ermitteln (2) → wortgleich; GK 1 (2018), Haupt 1 · LK 1 (2024), Haupt 1 · FHR 0
- 1.4 Mittlere Änderungsrate über ein Intervall berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Mittlere Änderungsraten zweier Modelle vergleichen (1) → wortgleich; GK 1 (2018), Haupt 1 · LK 0 · FHR 0
- 1.6 Umlaufzeit aus der Gesamtlänge eines symmetrischen Streckenzugs mit Halbkreisen und der Durchschnittsgeschwindigkeit berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 1.7 Term für die mittlere Änderungsrate über Einheitsintervalle nachweisen und Zeitpunkt des Unterschreitens einer Schranke berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Differenz und Differenzenquotient im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.9 Gleichung für die mittlere Änderungsrate lösen und Lösung im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Aussage über die Zunahme der Zusatzkosten über Differenzen von Funktionswerten beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.11 Sekantenwinkel gegen eine Schranke am Graphen beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.12 Fehler finden (die Differenz der Funktionswerte ohne Division durch die Intervalllänge als Rate angegeben; durch die Anzahl der Tabellenzeilen statt durch die Zeitspanne geteilt; f(b)/b als Durchschnitt genommen; die Einheit weggelassen) → didaktischer Typ, kein Prüfungstyp
- 1.13 Begründen (warum die mittlere Änderungsrate die Steigung der Sekante ist; warum eine Differenz und ein Differenzenquotient verschiedene Einheiten haben) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Ableitung an einer Stelle** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Ableitungswert berechnen und als Tangentensteigung veranschaulichen (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 2.2 Stelle mit vorgegebener momentaner Änderungsrate über die Ableitung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Gleiche Ableitungswerte zweier Funktionen nachweisen und als parallele Tangenten deuten (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 2.4 Steigung einer Geraden am Graphen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Negativen Wert einer Änderungsrate im Sachzusammenhang deuten (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.6 Aussage über den Vergleich der Steigungen zweier Graphen auf einem Intervall mit Gegenbeispiel beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Aussage über die Steigung am Graphen beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Koordinaten eines Punktes des Ratengraphen im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Fehler finden (f'(x₀) als f(x₀) gelesen oder umgekehrt; die Konstante im Term mit abgeleitet; eine Sekante statt der Tangente eingezeichnet; die negative Rate als negativen Bestand gedeutet) → didaktischer Typ, kein Prüfungstyp
- 2.10 Begründen (warum die Ableitung einer Geraden überall ihre Steigung ist; warum ein Gegenbeispiel eine Allaussage widerlegt, eine bestätigte Stelle sie aber nicht beweist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Von der Sekante zur Tangente** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Stelle mit lokaler gleich mittlerer Änderungsrate bestimmen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.2 Mittlere und momentane Änderungsrate im Sachzusammenhang vergleichen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 3.3 Mittlere Steigung berechnen und Tangentensteigung im Wendepunkt grafisch bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Steigungen aller Sekanten durch einen Punkt des Graphen angeben (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.5 Aufgabenstellung zu einer Gleichung aus Differenzenquotient und Ableitung formulieren (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.6 Fehler finden (die Tangentensteigung zu den Sekantensteigungen gezählt, obwohl die Tangente den Graphen nur in P trifft; die Gleichung f'(x₀) = Differenzenquotient als Sekante selbst gedeutet; die Abweichung auf die mittlere statt auf die momentane Rate bezogen; der Betrag statt des Vorzeichens der Steigung) → didaktischer Typ, kein Prüfungstyp
- 3.7 Begründen (warum die Sekantensteigungen gegen die Tangentensteigung streben; warum es zwischen zwei Punkten eine Stelle mit Tangente parallel zur Sekante gibt – anschaulich, nicht als Satz) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Die Rate als Funktion** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion berechnen (4) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 4.2 Länge des Zeitraums mit Mindeständerungsrate über die Lösungen von f'(x) = c berechnen (3) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.3 Zeitpunkt der größten Rate aus der Ableitung angeben (3) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.4 Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen (2) → wortgleich; GK 1 (2018), Haupt 1 · LK 0 · FHR 0
- 4.5 Größte und kleinste Rate im Zeitraum über Ableitung und Randwerte berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.6 Größte Änderungsrate über das Maximum der Ableitung im Sachzusammenhang berechnen (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 4.7 Zeitpunkte größter Differenz zweier Änderungsraten über die Extremstellen der Differenzfunktion berechnen (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 4.8 Eignung eines Modells über das Vorzeichen der Änderungsrate nach einer Nullstelle beurteilen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 4.9 Proportionalität zwischen Bestand und Änderungsrate im Sachzusammenhang nachweisen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 4.10 Fehler finden (das Maximum des Bestands statt der Rate gesucht – f' = 0 statt f'' = 0; bei gegebener Ratenfunktion r'' = 0 statt r' = 0; die Randwerte nicht geprüft; eine Lösung außerhalb des Zeitraums nicht verworfen; die Stelle statt des Wertes der Rate angegeben; mit der falschen Nullstelle argumentiert) → didaktischer Typ, kein Prüfungstyp
- 4.11 Begründen (warum die größte Rate eines Bestands an seiner Wendestelle liegt; warum ein Modell für eine Anzahl unbrauchbar wird, sobald seine Rate negativ wird) → didaktischer Typ, kein Prüfungstyp

### ableitungsregeln

**Einheit 1 · Potenz-, Faktor- und Summenregel** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 8 von 8 (Haupt 6).

- 1.1 Ableitung ganzrationale Funktion (6) → wortgleich; GK 0 · LK 0 · FHR 6 (2021, 2022, 2023, 2024, 2025, 2026), Haupt 4
- 1.2 Ableitung mit Parameter in faktorisierter Form nachweisen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 1.3 Ableitung als Quadrat eines Produkts von Linearfaktoren nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Verhalten im Unendlichen bestimmen (2; Ermessen, siehe Offene Punkte – zwei fhr-Zeilen, deren Punkt-Schwerpunkt bei den drei Ableitungen liegt, der Typ gehört zu grenzwerte-und-verhalten-im-unendlichen.md) → wortgleich; GK 0 · LK 0 · FHR 8, Haupt 3
- 1.5 Ableitungsfunktion und Stammfunktion einer ganzrationalen Funktion angeben (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 1.6 Fehler finden (der Exponent nicht gesenkt; der Vorfaktor nicht mit dem Exponenten multipliziert; die Konstante beim Ableiten mitgeführt; der Parameter wie eine Variable abgeleitet; beim Aufleiten der Exponent nicht erhöht) → didaktischer Typ, kein Prüfungstyp
- 1.7 Begründen (warum die Konstante beim Ableiten wegfällt; warum ein Parameter beim Ableiten nach x eine Zahl ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Kettenregel** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Tangente an eine Verkettung aus zwei abgebildeten Graphen über die Kettenregel bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.2 Verschiebung zwischen Graph und hundertster Ableitung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Fehler finden (die innere Ableitung vergessen; die äußere Ableitung an x statt an der inneren Funktion gebildet; bei e^(kx) den Faktor k als Exponent behandelt; die wiederholte Ableitung von e^(2x) als Streckung statt als Verschiebung gedeutet) → didaktischer Typ, kein Prüfungstyp
- 2.4 Begründen (warum die Ableitung von e^(kx) den Faktor k trägt; warum der Graph von c · e^(2x) eine Verschiebung des Graphen von e^(2x) ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Produktregel** – Abitur-Jahrgänge GK 2 von 9 (Haupt 1) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden (2) → wortgleich; GK 1 (2018), Haupt 0 · LK 2 (2018, 2022), Haupt 1 · FHR 0
- 3.2 Ableitung eines Produkts aus Graphenwerten mit der Produktregel bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen (6) → wortgleich; GK 1 (2020), Haupt 1 · LK 3 (2018, 2022, 2024), Haupt 3 · FHR 0
- 3.4 Bedingung für eine waagerechte Tangente eines Produkts mit e^x nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Fehler finden (nur die Faktoren einzeln abgeleitet und multipliziert; die innere Ableitung des e-Terms vergessen; der Vorfaktor nur bei einem Summanden; nach dem Ausklammern nicht zusammengefasst und die vorgegebene Form nicht erreicht; am Extrempunkt f'(x₀) = 0 nicht erkannt) → didaktischer Typ, kein Prüfungstyp
- 3.6 Begründen (warum man den e-Term ausklammern kann und warum er die Nullstellen nicht ändert; warum g'(a) = 0 für g = f · e^x auf f'(a) = −f(a) führt) → didaktischer Typ, kein Prüfungstyp

### grenzwerte-und-verhalten-im-unendlichen

**Einheit 1 · Ganzrationale Funktionen** – Abitur-Jahrgänge GK 3 von 9 (Haupt 2) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 8 von 8 (Haupt 8).

- 1.1 Symmetrie am Funktionsterm beurteilen (3; Ermessen, siehe Offene Punkte – drei fhr-Zeilen, deren Punkt-Schwerpunkt beim Verhalten im Unendlichen liegt, der Typ gehört zum fhr-Thema „Symmetrie nachweisen“ bei funktionsklassen-und-eigenschaften.md) → wortgleich; GK 0 · LK 0 · FHR 8, Haupt 8
- 1.2 Grenzverhalten einer ganzrationalen Funktion angeben (3) → wortgleich; GK 3 (2020, 2022, 2026), Haupt 2 · LK 1 (2022), Haupt 1 · FHR 0
- 1.3 Verhalten im Unendlichen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 8, Haupt 3
- 1.4 Fehler finden (bei ungeradem Grad beide Seiten gleich angegeben; das Vorzeichen des Leitkoeffizienten übersehen; am Summanden 2x statt am Leitterm abgelesen; das Absolutglied als ungeraden Exponenten gewertet; das Verhalten von f statt von f' angegeben) → didaktischer Typ, kein Prüfungstyp
- 1.5 Begründen (warum nur der Leitterm zählt; warum ein negativer Leitkoeffizient bei geradem Grad beide Seiten nach unten schickt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Produkte aus Polynom und e-Funktion** – Abitur-Jahrgänge GK 7 von 9 (Haupt 7) · LK 3 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (5) → wortgleich; GK 4 (2019, 2020, 2021, 2023), Haupt 4 · LK 1 (2023), Haupt 1 · FHR 0
- 2.2 Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben (5) → wortgleich; GK 2 (2018, 2025), Haupt 2 · LK 2 (2017, 2018), Haupt 1 · FHR 0
- 2.3 Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben (3) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 2.4 Fehler finden (aus dem wachsenden Polynomfaktor auf +∞ geschlossen, obwohl der e-Faktor gegen null geht; das Vorzeichen des Polynomfaktors auf der Seite übersehen, auf der die e-Funktion wächst; „unbestimmt“ statt null, weil ein Faktor wächst und einer fällt; die Fallunterscheidung nach dem Parameter vergessen; den konstanten Summanden nicht als Grenzwert stehen gelassen) → didaktischer Typ, kein Prüfungstyp
- 2.5 Begründen (warum die e-Funktion gegen jedes Polynom gewinnt; warum e^x nie null ist und die Nullstellen allein aus dem Polynomfaktor kommen) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Waagerechte Asymptoten** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Monotonie, Nullstelle und Grenzwert einer e-Funktion am Term begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Nullstellenfreiheit und Grenzwerte eines Bruchs mit e-Funktion am Term begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Fehler finden (Grenzwert null statt der Verschiebung c; die beiden Grenzwerte des Bruchs vertauscht; den Nenner null gesetzt und eine Nullstelle gefunden; die Monotonie bei negativem Streckfaktor nicht umgedreht) → didaktischer Typ, kein Prüfungstyp
- 3.4 Begründen (warum die Verschiebung um c die Asymptote auf y = c legt; warum ein Bruch mit konstantem Zähler keine Nullstelle hat) → didaktischer Typ, kein Prüfungstyp

### gleichungen-loesen

**Einheit 1 · Ganzrationale Gleichungen** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 7 von 8 (Haupt 7).

- 1.1 Schnittpunkte zweier Funktionsgraphen berechnen (6) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2021, 2022, 2023, 2025), Haupt 5
- 1.2 Stelle zu gegebenem Funktionswert berechnen (3) → wortgleich; GK 0 · LK 0 · FHR 3 (2021, 2024, 2025), Haupt 3
- 1.3 Schnittpunkt zweier Graphen über eine biquadratische Gleichung berechnen (1) → wortgleich; GK 1 (2018), Haupt 1 · LK 0 · FHR 0
- 1.4 Schnittpunkte einer Geraden mit einer Hyperbel über eine quadratische Gleichung berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Stellen mit vorgegebenem Funktionswert durch Ausklammern berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Schnittstellen zweier Graphen durch Lösen einer quadratischen Gleichung nachweisen (3) → wortgleich; GK 2 (2019, 2021), Haupt 2 · LK 0 · FHR 0
- 1.7 Gemeinsame Punkte zweier Graphen als einzige durch Ausklammern nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Termgleichheit zweier Darstellungen einer ganzrationalen Funktion durch Ausmultiplizieren nachweisen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 1.9 Fehler finden (durch x geteilt und die Lösung null verloren; die negative Hilfslösung u zurücksubstituiert; aus x⁴ = c die Quadratwurzel gezogen; beim Wurzelziehen nur das positive Vorzeichen; beim Gleichsetzen ein Vorzeichen falsch übernommen; das „nur“ nicht begründet; die Lösung nicht am Sachzusammenhang geprüft) → didaktischer Typ, kein Prüfungstyp
- 1.10 Begründen (warum eine quadratische Gleichung höchstens zwei Lösungen hat; warum u = x² nicht negativ sein kann; warum eine bekannte Lösung die Polynomdivision erlaubt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Gleichungen mit e-Funktion und Logarithmus** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Nullstelle einer Exponentialfunktion durch Logarithmieren bestimmen (2) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.2 Anfangswert angeben und Stelle für einen vorgegebenen Wert einer Exponentialfunktion berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Anfangswert angeben und Zeitpunkt für einen Bestand bei logistischem Wachstum berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Exponentialgleichung für einen Funktionswert durch Logarithmieren lösen und als Abstand im Sachzusammenhang angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Nullstelle einer Logarithmusfunktion berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.6 Steigung im Schnittpunkt von Graph und Ableitungsgraph bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Schnittstellen zweier Graphen über den gemeinsamen Exponentialfaktor nachweisen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 2.8 Schnittstelle von Graph und Ableitungsgraph nachweisen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 1 (2025), Haupt 1 · FHR 0
- 2.9 Fehlenden Schnittpunkt zweier Graphen über eine unlösbare Gleichung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Fehler finden (den Vorfaktor beim Logarithmieren mitgezogen; den Faktor im Exponenten vergessen; den e-Faktor null gesetzt statt gekürzt; ln(1/4) mit falschem Vorzeichen; ln(x + 5) = −1 zu x + 5 = −e umgeformt; e^x = −1 numerisch lösen wollen; die Lösung statt des Abstands zur Bezugsstelle angegeben) → didaktischer Typ, kein Prüfungstyp
- 2.11 Begründen (warum man durch e^x teilen darf; warum ln nur auf positive Zahlen anwendbar ist und e^x = −1 keine Lösung hat) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Gleichungen aufstellen und grafisch oder numerisch lösen** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Gleichung aus Differenzenquotient und Ableitung lösen (2) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 3.2 Alle Zeitpunkte für einen Wert einer Sinusfunktion in einem Intervall berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Gleichung f(t) = f(t − c) für gleiche Werte im Abstand c mit dem Rechner lösen und im Graphen darstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Zeitpunkt für einen Anteil des Maximalwerts einer Sinusfunktion berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Funktionalgleichung mit Zeitverschiebung grafisch lösen und im Sachzusammenhang deuten (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 3.6 Achsenparallele Quadrate mit Eckpunkt auf dem Graphen skizzieren, Gleichungen für die Seitenlängen angeben und Umfangsverhältnis beschreiben (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.7 Gleichung für zwei Graphenpunkte mit festem horizontalem Abstand und Höhenunterschied aufstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Lösungen einer Differenzgleichung als Schnittstellen zweier Graphen grafisch beschreiben und angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.9 Fehler finden (a(x + 3) = a(x) + 1000 als a(3) = a(0) + 1000 gelesen; r(t) = r(5) statt r(t − 5) angesetzt; die Maße in Metern statt in Längeneinheiten in die Gleichung geschrieben; nur die Rechnerlösung der Sinusgleichung angegeben; 0,13 Stunden als 13 Minuten gelesen; beim Multiplizieren mit x einen Summanden vergessen) → didaktischer Typ, kein Prüfungstyp
- 3.10 Begründen (warum eine Sinusgleichung im Intervall mehrere Lösungen hat; warum die Differenz zweier Funktionen genau dort null ist, wo sich die Graphen schneiden) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Ungleichungen** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Lösungsmenge einer Ungleichung zwischen zwei Funktionstermen über die faktorisierte Differenz bestimmen (2) → wortgleich; GK 1 (2023), Haupt 1 · LK 1 (2022), Haupt 1 · FHR 0
- 4.2 Parameter einer Exponentialfunktion aus einer Ungleichung für einen Funktionswert im Sachzusammenhang ermitteln (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 4.3 Lösungsweg für den Gültigkeitsbereich einer Näherung über eine Betragsungleichung beschreiben (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 4.4 Fehler finden (die doppelte Nullstelle in die Lösungsmenge aufgenommen; die Ungleichung nur an Beispielwerten geprüft; „alle x“ geantwortet und die Gleichheitsstellen übersehen; den Betrag nicht aufgelöst; beim Auflösen nach k die Exponentialzahl auf die falsche Seite gebracht) → didaktischer Typ, kein Prüfungstyp
- 4.5 Begründen (warum ein Quadrat als Faktor das Vorzeichen nicht ändert; warum Beispielwerte eine Ungleichung nicht beweisen) → didaktischer Typ, kein Prüfungstyp

### umkehrfunktion

**Einheit 1 · Umkehrbarkeit, Bereiche und Term** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Definitionsbereich der Umkehrfunktion angeben und ihren Term nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Umkehrbarkeit auf einem Intervall begründen und Definitions- und Wertebereich der Umkehrfunktion angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Fehler finden (Definitionsbereich der Umkehrfunktion mit dem der Funktion verwechselt; einen Grenzwert, der nicht angenommen wird, in den Bereich aufgenommen; die Variablen nicht getauscht) → didaktischer Typ, kein Prüfungstyp
- 1.4 Begründen (warum eine Funktion mit Extrempunkt auf ℝ nicht umkehrbar ist; warum der Wertebereich von f der Definitionsbereich von g ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Spiegelung an der Winkelhalbierenden** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Flächeninhalt eines Vierecks aus Berührpunkten und Spiegelpunkten als Trapez begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.2 Tangente an Funktion und Umkehrfunktion über die Spiegelung an y = x begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Flächenbeziehung zwischen Funktion und Umkehrfunktion über die Spiegelung an y = x beurteilen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 2.4 Fehler finden (die Gerade y = x nicht als Symmetrieachse erkannt; die Tangente an die Umkehrfunktion neu berechnet statt gespiegelt; die Höhe des Trapezes als Abstand zweier Spiegelpunkte genommen) → didaktischer Typ, kein Prüfungstyp
- 2.5 Begründen (warum die Spiegelung an y = x die Koordinaten tauscht; warum eine Gerade mit Steigung −1 bei der Spiegelung in sich übergeht) → didaktischer Typ, kein Prüfungstyp

### ableitungsgraph-und-funktionsgraph

### tangente-normale-schnittwinkel

**Einheit 1 · Tangentengleichung im Punkt** – Abitur-Jahrgänge GK 6 von 9 (Haupt 6) · LK 6 von 7 (Haupt 6) · FHR-Jahrgänge 8 von 8 (Haupt 7).

- 1.1 Tangentengleichung in einem Punkt des Graphen aufstellen (11) → wortgleich; GK 4 (2019, 2022, 2025, 2026), Haupt 4 · LK 2 (2017, 2018), Haupt 1 · FHR 0
- 1.2 Berührpunkt der Tangente mit vorgegebener Steigung berechnen (3) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 1.3 Tangentengleichung im Punkt (3) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2021, 2022, 2024, 2025, 2026), Haupt 3
- 1.4 Anstieg des Graphen an einer Stelle berechnen (2) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2021, 2022, 2023, 2024), Haupt 2
- 1.5 Parallele Tangente über die Ableitung finden und skizzieren (2) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 1.6 Punktprobe am Graphen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2023, 2024, 2025, 2026), Haupt 4
- 1.7 Anstieg einer Strecke aus den Endpunkten angeben (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 1 (2021), Haupt 1
- 1.8 Stelle mit parallelen Tangenten an Graph und Ableitungsgraph über f' = f'' ermitteln (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 1.9 Stelle zu gegebenem Anstieg berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2019), Haupt 1
- 1.10 Tangente mit vorgegebener Steigung außerhalb eines Punktes angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.11 y-Achsenabschnitt der Tangente allgemein nachweisen (3) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.12 Tangentensteigung in einem Punkt über die Ableitung nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.13 Fehlende waagerechte Tangente über Vorzeichen am Graphen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.14 Nullstelle der Tangente an einen gestreckten Graphen als parameterunabhängig nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.15 Schranke für den Anstieg der Tangenten einer Schar begründen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 1.16 Stellen mit vorgegebenem Tangentenanstieg nachweisen (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 1.17 Tangente im Ursprung als Gerade durch zwei Punkte nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.18 Waagerechte Tangente an einer vorgegebenen Stelle nachweisen und Funktionswert berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 1.19 Tangentengleichung aus der Abbildung ablesen (3) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.20 Tangente am gespiegelten Punkt über die Achsensymmetrie angeben (2) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 1.21 Tangente mit gegebener Gleichung in die Abbildung einzeichnen (2) → wortgleich; GK 1 (2020), Haupt 0 · LK 1 (2025), Haupt 1 · FHR 0
- 1.22 Aussage über den größten y-Achsenabschnitt der Tangenten eines Graphen beurteilen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 1.23 Ergebnis eines Lösungswegs als y-Achsenabschnitt der parallelen Tangente deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.24 Stellen mit waagerechter Tangente aus der faktorisierten Ableitung angeben (1) → wortgleich; GK 0 · LK 2 (2023, 2024), Haupt 1 · FHR 0
- 1.25 Tangente in das Koordinatensystem einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 3 (2024, 2025, 2026), Haupt 1
- 1.26 Fehler finden (den Funktionswert statt des Ableitungswerts als Steigung genommen; n gleich dem Funktionswert gesetzt statt aus der Punktbedingung berechnet; die Funktionsgleichung statt der Ableitung gleich dem Anstieg gesetzt; die Steigung aus der Abbildung falsch abgelesen) → didaktischer Typ, kein Prüfungstyp
- 1.27 Begründen (warum die Tangente an der Stelle dieselbe Steigung wie der Graph hat; warum parallele Tangenten über f' gleich m gefunden werden) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Tangente als Berührung** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 3 von 7 (Haupt 2) · FHR-Jahrgänge 2 von 8 (Haupt 2).

- 2.1 Einsehbarkeit eines Kurvenstücks von einem Punkt aus über die Tangente durch diesen Punkt untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.2 Näherung durch die Tangente mit dem Funktionswert im Sachzusammenhang vergleichen (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 0 · FHR 0
- 2.3 Parameter einer Logarithmusfunktion aus einer gemeinsamen Tangente mit einer Scharkurve berechnen und Tangentengleichung angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Steigungen der Geraden durch den Wendepunkt mit genau einem gemeinsamen Punkt über die Wendetangente eingrenzen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Tangente aufstellen und weiteren gemeinsamen Punkt mit dem Graphen berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 2.6 Gemeinsame Tangente zweier Graphen im Schnittpunkt nachweisen und angeben (2) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 2.7 Gerade als Tangente in einem vorgegebenen Punkt über Funktionswert und Ableitung nachweisen (2) → wortgleich; GK 2 (2020, 2026), Haupt 2 · LK 0 · FHR 0
- 2.8 Tangenteneigenschaft einer Geraden nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 2 (2022, 2026), Haupt 2
- 2.9 Faktorisierung von f(x) − t(x) nachweisen und weiteren Schnittpunkt von Tangente und Graph begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Fehlen einer gemeinsamen Tangente zweier Graphen über die Vorzeichen der Steigungen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.11 Näherungsweise tangentiale Einmündung einer Geraden nachweisen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.12 Schnittpunkt zweier Tangenten nachweisen und Tangenten einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.13 Tangente durch einen entfernten Punkt über die Rationalität der Steigung ausschließen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.14 Weiteren Schnittpunkt von Tangente und Graph aus einer vorgegebenen Faktorisierung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.15 Gleichung als Tangentenbedingung geometrisch deuten (2) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 2.16 Rechenweg zur Tangente von einem Punkt an den Graphen erläutern und Aufgabenstellung formulieren (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.17 Relative Abweichung zwischen Tangente und Funktion als Ungleichung im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.18 Tangente durch einen vorgegebenen Punkt am Graphen einzeichnen und ihre Gleichung ablesen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.19 Tangenten durch einen Punkt der y-Achse an den Graphen skizzieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.20 Fehler finden (nur eine der beiden Berührbedingungen geprüft; die Berührstelle als weiteren Schnittpunkt gezählt; die Tangente als Sekante durch zwei Kurvenpunkte gezeichnet; den Parameter aus der Punktbedingung statt aus der Steigungsbedingung bestimmt) → didaktischer Typ, kein Prüfungstyp
- 2.21 Begründen (warum die Berührstelle doppelte Nullstelle der Differenz ist; warum eine Aussage über alle Tangenten nicht an einem Beispiel bewiesen werden kann) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Normale** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 2 von 7 (Haupt 1) · FHR-Jahrgänge 4 von 8 (Haupt 3).

- 3.1 Mittelpunkt eines den Graphen berührenden Kreises über die Normale im Berührpunkt bestimmen (3) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 3.2 Abstand des Ursprungs zu einer Geraden über das Lot berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Funktionswert an einer Stelle berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 2 (2019, 2022), Haupt 2
- 3.4 Gerade senkrecht zu einer gegebenen Tangente durch einen Punkt aufstellen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 0 · FHR 0
- 3.5 Länge der Normalen vom Graphenpunkt bis zur x-Achse berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Normalengleichung im Punkt (1) → wortgleich; GK 0 · LK 0 · FHR 3 (2022, 2023, 2025), Haupt 1
- 3.7 Abstand eines Punktes von einem Graphen über die Normalenbedingung deuten (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Lösungsweg für eine gemeinsame Normale zweier Kurven erläutern (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.9 Fehler finden (die Tangentensteigung für die Normale übernommen oder nur das Vorzeichen gedreht, ohne den Kehrwert zu bilden; den Abstand senkrecht zur Achse statt senkrecht zur Tangente gemessen; die Tangente statt der Normalen angesetzt) → didaktischer Typ, kein Prüfungstyp
- 3.10 Begründen (warum der kürzeste Abstand auf der Normalen liegt; warum der Mittelpunkt eines berührenden Kreises auf der Normalen im Berührpunkt liegt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Steigungswinkel und Schnittwinkel** – Abitur-Jahrgänge GK 7 von 9 (Haupt 7) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Parameter aus dem senkrechten Schnitt zweier Graphen bestimmen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 4.2 Schnittwinkel zweier Graphen im gemeinsamen Punkt über die Tangentensteigungen berechnen (2) → wortgleich; GK 2 (2022, 2023), Haupt 2 · LK 0 · FHR 0
- 4.3 Tangentengleichung und Schnittwinkel der Tangente mit der x-Achse bestimmen (2) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 4.4 Winkel zwischen Graph und senkrechter Kante über die Ableitung berechnen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.5 Auftreffwinkel einer Flugkurve über die Ableitung an der Nullstelle berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.6 Bereich der Stellen mit Mindeststeigungswinkel der Tangente über eine quadratische Ungleichung ermitteln (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.7 Öffnungswinkel an der Spitze eines Rotationskörpers über die Tangentensteigung prüfen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 4.8 Scharparameter für einen vorgegebenen Schnittwinkel des Graphen mit der y-Achse bestimmen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 4.9 Schnittwinkel eines Graphen mit einer waagerechten Geraden über die Ableitung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Schnittwinkel zwischen Tangente und Gerade über die Anstiege berechnen (1) → wortgleich; GK 2 (2018, 2021), Haupt 1 · LK 0 · FHR 0
- 4.11 Steigungswinkel des Graphen in einem Punkt über die Ableitung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.12 Steigungswinkel einer Tangente berechnen und Aussage über den Schnittwinkel mit einer Geraden prüfen (1) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 4.13 Steigungswinkel und y-Achsenabschnitt der Wendetangente berechnen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.14 Ursprungsgerade durch einen Graphenpunkt als Winkelhalbierende zwischen x-Achse und Tangente bestimmen (1) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 4.15 Rechenschritte zur Winkelbestimmung aus Höhen- und Horizontalabstand beurteilen und berichtigen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 4.16 Steigungswinkel und Nebenwinkel am Übergang zweier Profilstücke einzeichnen und im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.17 Fehler finden (die Anstiege statt der Steigungswinkel voneinander abgezogen; den Winkel gegen die falsche Bezugslinie angegeben; den Rechner im Bogenmaß gelassen; nur den halben Winkel mit der Vorgabe verglichen; den Winkel als Steigung angegeben) → didaktischer Typ, kein Prüfungstyp
- 4.18 Begründen (warum tan α = m die Steigung in einen Winkel übersetzt; warum senkrechter Schnitt das Produkt der Steigungen minus eins bedeutet) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Dreiecke und Figuren aus Tangente, Normale und Achsen** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 2 von 8 (Haupt 1).

- 5.1 Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen (3) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2018), Haupt 1 · FHR 0
- 5.2 Berührpunkt der Tangente mit gleichschenkligem Achsendreieck über die Steigung −1 berechnen (2) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 5.3 Flächeninhalt des Dreiecks aus Tangente, Gerade und x-Achse berechnen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 5.4 Umfang des Achsendreiecks einer Tangente berechnen und Umkreismittelpunkt angeben (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 5.5 Umfang des Dreiecks aus zwei Tangenten und der x-Achse berechnen (2) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.6 Aussage über den Bremsweg bei konstanter Abnahme über die Tangente und ein Dreieck untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.7 Dreiecksfläche aus Achsenabschnitten einer Geraden (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2024, 2026), Haupt 1
- 5.8 Flächeninhalt des von Tangente, Normale und y-Achse begrenzten Dreiecks berechnen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 1 (2017), Haupt 0 · FHR 0
- 5.9 Scharparameter für ein gleichseitiges Dreieck aus den Tangenten an Graph und Spiegelgraph und der y-Achse bestimmen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 5.10 Tangentengleichung im Ursprung aufstellen und Grenze einer Dreiecksfläche aus dem Flächeninhalt berechnen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 5.11 Gleichschenkligkeit des Dreiecks aus Tangente und Koordinatenachsen allgemein begründen (3) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 5.12 Flächeninhalt eines Rechtecks aus Nullstellen und Normale als parameterunabhängig nachweisen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 5.13 Tangentenabschnitt auf der x-Achse als Quotient f/f' am Graphen begründen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 5.14 Dreiecke aus Wendetangente, Normale und Koordinatenachsen einzeichnen und ihre Ähnlichkeit begründen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.15 Fehler finden (den negativen Achsenabschnitt ohne Betrag in die Flächenformel gesetzt; den Faktor ein halb vergessen; die Höhe als Schenkel genommen; den Flächeninhalt statt des Umfangs berechnet; den Schwerpunkt statt des Umkreismittelpunkts angegeben) → didaktischer Typ, kein Prüfungstyp
- 5.16 Begründen (warum das Achsendreieck im Ursprung rechtwinklig ist; warum Gleichschenkligkeit hier Steigung plus oder minus eins bedeutet) → didaktischer Typ, kein Prüfungstyp

### extremalprobleme

**Einheit 1 · Figur und Term** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 2 von 8 (Haupt 2).

- 1.1 Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 0 · FHR 0
- 1.2 Flächenterm eines einbeschriebenen Trapezes über die Mittelparallele geometrisch herleiten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Dreieck in das Koordinatensystem einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2023), Haupt 1
- 1.4 Dreieck zu Schnittpunkten mit einer Parallelen zur x-Achse einzeichnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 1.5 Einbeschriebenes Trapez zu einem Parameterwert in die Abbildung einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Rechteck in das Koordinatensystem einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2020), Haupt 1
- 1.7 Term für die Schenkellänge eines einbeschriebenen Trapezes aufstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Fehler finden (die Höhe als Stelle statt als Funktionswert genommen; nur eine Seite verdoppelt; die Schenkellänge mit der Differenz der parallelen Seiten verwechselt; eine Ecke falsch gelesen) → didaktischer Typ, kein Prüfungstyp
- 1.9 Begründen (warum die Seiten der Figur Koordinaten und Funktionswerte sind; warum die Trapezfläche Mittelparallele mal Höhe ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Zielfunktion aus Haupt- und Nebenbedingung** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 3 von 8 (Haupt 2).

- 2.1 Zielfunktion aus Haupt- und Nebenbedingung aufstellen (3) → wortgleich; GK 0 · LK 0 · FHR 3 (2020, 2023, 2025), Haupt 2
- 2.2 Flächeninhalt bei gegebener Nebenbedingung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2020, 2025), Haupt 1
- 2.3 Fehler finden (die Nebenbedingung nach der falschen Variablen umgestellt; den Umfang als einfache statt doppelte Summe angesetzt; das Material auf vier statt drei Seiten verteilt; den Faktor ein halb der Dreiecksfläche im Term verloren) → didaktischer Typ, kein Prüfungstyp
- 2.4 Begründen (warum die Zielfunktion nur noch eine Variable haben darf; warum der Definitionsbereich zur Figur gehört) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Maximum bestimmen und deuten** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 3 von 8 (Haupt 3).

- 3.1 Maximum der Zielfunktion bestimmen (3) → wortgleich; GK 0 · LK 0 · FHR 3 (2020, 2023, 2025), Haupt 3
- 3.2 Parameter für den größten Flächeninhalt über die Ableitung bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Achsenparalleles Rechteck maximaler Fläche zwischen Ursprung und Graphenpunkt bestimmen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.4 Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen (4) → wortgleich; GK 4 (2018, 2020, 2021, 2024), Haupt 4 · LK 0 · FHR 0
- 3.5 Ausschluss einer Stelle als Maximalstelle einer Rechtecksfläche über die notwendige Bedingung nachweisen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.6 Aufgabenstellung zu einer Extremwertaufgabe mit Dreiecksfläche aus dem Lösungsweg formulieren und Schritte erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Fehler finden (die Lösung außerhalb des Definitionsbereichs verwendet; die Extremstelle statt des Extremwerts angegeben; das Minimum der Differenz als Maximalstelle genommen; die hinreichende Bedingung vergessen; f' statt A' betrachtet) → didaktischer Typ, kein Prüfungstyp
- 3.8 Begründen (warum am Rand die Figur entartet und das größte Exemplar im Inneren liegt; warum der vertikale Abstand die Differenz der Funktionswerte ist) → didaktischer Typ, kein Prüfungstyp

### funktionsklassen-und-eigenschaften

**Einheit 1 · Funktionswert und Punkt** – Abitur-Jahrgänge GK 6 von 9 (Haupt 6) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 8 von 8 (Haupt 5).

- 1.1 Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen (12) → wortgleich; GK 2 (2019, 2026), Haupt 2 · LK 1 (2024), Haupt 1 · FHR 0
- 1.2 Nullstellen und Werte: Vertikalen Abstand zweier Punkte als Differenz von Funktionswerten berechnen (2) → wortgleich; GK 1 (2018), Haupt 1 · LK 1 (2023), Haupt 1 · FHR 0
- 1.3 Nullstellen und Werte: Zurückgelegten Weg aus Hin- und Rückbewegung über Funktionswerte berechnen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 1.4 Nullstellen und Werte: Anfangswert eines Bestands als Funktionswert an der Stelle null berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Nullstellen und Werte: Ausdehnung einer Figur in x-Richtung aus der Ausdehnung in y-Richtung über Funktionswerte ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Nullstellen und Werte: Bereich mit Funktionswerten über einer Schranke aus dem Graphen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Nullstellen und Werte: Funktionswert und Änderungsbeträge zweier Zeitabschnitte im Sachzusammenhang vergleichen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Nullstellen und Werte: Gleichheit zweier Sachgrößen als Bedingung an den Funktionswert übersetzen und Stelle am Graphen ablesen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.9 Nullstellen und Werte: Höhen an den Rändern einer Profillinie als Funktionswerte berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Nullstellen und Werte: Länge der Verbindungsstrecke zweier Graphenpunkte als Näherung der Bogenlänge berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.11 Nullstellen und Werte: Prozentuale Abweichung eines Modellwerts vom Messwert berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.12 Nullstellen und Werte: Wert einer Funktion berechnen und die zugehörige Stelle einer zweiten Funktion am Graphen ablesen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.13 Nullstellen und Werte: y-Achsenabschnitt einer Geraden durch einen festen Punkt als Term in der Steigung angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.14 Punktprobe am Graphen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2023, 2024, 2025, 2026), Haupt 4
- 1.15 Schnittpunkt mit der y-Achse berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 6 (2020, 2021, 2022, 2023, 2024, 2026), Haupt 1
- 1.16 Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen (8) → wortgleich; GK 2 (2021, 2025), Haupt 2 · LK 2 (2018, 2026), Haupt 2 · FHR 0
- 1.17 Nullstellen und Werte: Gleichheit zweier Funktionswerte durch Einsetzen im Sachzusammenhang nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.18 Nullstellen und Werte: Aussage über das Verhältnis zweier Funktionswerte durch Einsetzen widerlegen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.19 Nullstellen und Werte: Aussage über eine Rate aus dem Nullabschnitt einer abschnittsweise definierten Funktion begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.20 Nullstellen und Werte: Punktprobe an einer Geraden rechnerisch zeigen und Gerade einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.21 Nullstellen und Werte: Schnittpunkt mit der y-Achse und Steigung des Graphen dort angeben (2) → wortgleich; GK 1 (2018), Haupt 0 · LK 1 (2018), Haupt 1 · FHR 0
- 1.22 Nullstellen und Werte: Schnittstellen zweier Graphen im Sachzusammenhang ablesen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.23 Nullstellen und Werte: Stelle zu einem vorgegebenen Funktionswert am Graphen ablesen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.24 Nullstellen und Werte: Aussage zur Modellgüte über die Summe vorzeichenbehafteter Abweichungen beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.25 Nullstellen und Werte: Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.26 Nullstellen und Werte: Summe von Funktionswerten mit Maßstab als Gesamtlänge im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.27 Nullstellen und Werte: Tiefstelle und Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.28 Nullstellen und Werte: Ungleichung für einen Funktionswert im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.29 Fehler finden (den Wert am falschen Graphen abgelesen; die Achsen beim Ablesen vertauscht; die Einheit der Achse übersehen; den Maßstab vergessen; e als Variable behandelt und die Gleichung lösen wollen) → didaktischer Typ, kein Prüfungstyp
- 1.30 Begründen (warum ein Punkt auf dem Graphen „f von Stelle gleich Wert“ bedeutet; warum der Anfangswert der Funktionswert an der Stelle null ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Nullstellen** – Abitur-Jahrgänge GK 6 von 9 (Haupt 5) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 8 von 8 (Haupt 8).

- 2.1 Nullstellen über Substitution biquadratisch (5) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2021, 2022, 2023, 2026), Haupt 5
- 2.2 Nullstellen und Werte: Nullstelle und y-Achsenschnittpunkt eines Produkts mit e-Funktion angeben (3) → wortgleich; GK 3 (2020, 2021, 2024), Haupt 3 · LK 0 · FHR 0
- 2.3 Nullstellen durch Ausklammern (2) → wortgleich; GK 0 · LK 0 · FHR 5 (2019, 2023, 2024, 2025, 2026), Haupt 2
- 2.4 Nullstellen mit Polynomdivision (2) → wortgleich; GK 0 · LK 0 · FHR 7 (2019, 2021, 2022, 2023, 2024, 2025, 2026), Haupt 2
- 2.5 Nullstellen und Werte: Nullstellen einer ganzrationalen Funktion durch Ausklammern und Faktorisieren berechnen (2) → wortgleich; GK 3 (2021, 2022, 2025), Haupt 2 · LK 0 · FHR 0
- 2.6 Nullstellen einer quadratischen Funktion mit Lösungsformel (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2023, 2024), Haupt 1
- 2.7 Nullstellen einer quadratischen Funktion über Wurzelziehen (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2023, 2024), Haupt 1
- 2.8 Nullstellen und Werte: Gesamtlänge aus einer Nullstelle und der Achsensymmetrie im Sachzusammenhang berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Nullstellen und Werte: Nullstellen berechnen und Grenzverhalten einer ganzrationalen Funktion angeben (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Nullstellen und Werte: Schnittpunkte des Graphen mit beiden Koordinatenachsen berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 2.11 Nullstellen und Werte: y-Achsenschnittpunkt angeben und Anzahl der Nullstellen aus der faktorisierten Form ermitteln (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 2.12 Nullstelle durch Einsetzen nachweisen (3; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 3 (2023, 2024, 2025), Haupt 2
- 2.13 Nullstellen und Werte: Nullstellen aus Linearfaktoren im Sachzusammenhang nennen und ihre Vollständigkeit über die Faktorstruktur begründen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.14 Nullstellen und Werte: Durchmesser der Grundfläche eines Rotationskörpers aus der Nullstelle der Profilfunktion mit Maßstab nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.15 Nullstellen eines Produkts von Funktionen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2023), Haupt 1
- 2.16 Nullstellen und Werte: Nullstelle null am Term ohne konstanten Summanden begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.17 Nullstellen und Werte: Nullstelle über die Symmetrie begründen und übrige Nullstellen einer biquadratischen Funktion bestimmen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 2.18 Nullstellen aus der faktorisierten Form ablesen (2) → wortgleich; GK 0 · LK 0 · FHR 2 (2020, 2023), Haupt 2
- 2.19 Nullstellen und Werte: Nullstellen aus der faktorisierten Form angeben (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 2.20 Fehler finden (die Lösung null beim Ausklammern verloren; nach der Rücksubstitution nur die positiven Wurzeln angegeben; die negative Hilfslösung zurücksubstituiert; das Vorzeichen der Linearfaktoren übernommen; e hoch x gleich null angesetzt) → didaktischer Typ, kein Prüfungstyp
- 2.21 Begründen (warum ein Produkt genau dann null ist, wenn ein Faktor null ist; warum der e-Faktor keine Nullstelle beisteuert) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Definitionsbereich, Wertemenge und Schranken: den größtmöglichen Definitionsbereich einer Logarithmusfunktion aus der Bedingung Argument größer null, auch mit Parameter; Wertemengen am Term ablesen (e-Funktion positiv und nie null, Sinus zwischen minus eins und plus eins, Quadrat ab null), bei Verkettungen von innen nach außen; Schranken über das Vorzeichen des e-Terms begründen (der Grenzwert wird nicht angenommen); Werte und ihre Häufigkeit auf einer Periode; Abschätzungen gegen die x-Achse. (Q1, GK-Kern „Definitions- und Wertebereich“; LK-Zusatz ln als Funktionsklasse; FOS „Funktionsbegriff“ mit „Definitions- und Wertebereich“, ohne eigene fhr-Zeile; OHiMi 2.2 „Definitionsbereich, Wertebereich“) ← Eingabe „definitionsbereich“, „wertemenge“, „wertebereich“, „schranke“, „nie null“** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Nullstellen und Werte: Definitionsbereich einer Logarithmusfunktion angeben (2) → wortgleich; GK 0 · LK 2 (2017, 2023), Haupt 2 · FHR 0
- 3.2 Nullstellen und Werte: Nullstellenfreiheit und Wertemenge einer e-Funktion aus dem Term begründen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2017), Haupt 0 · FHR 0
- 3.3 Nullstellen und Werte: Einhalten einer Schranke über das Vorzeichen des e-Terms begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Nullstellen und Werte: Minimalwert einer verschobenen Sinusfunktion begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Nullstellen und Werte: Lage eines Graphen unterhalb der x-Achse über eine Logarithmus-Abschätzung beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Nullstellen und Werte: Wertemenge einer verketteten e-Funktion angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Nullstellen und Werte: Wertemenge und Häufigkeit der Werte einer Sinusfunktion auf einer Periode angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Fehler finden (den Grenzwert in die Wertemenge eingeschlossen; die Randpunkte des Definitionsbereichs mitgenommen; die Wertemenge der Verkettung wie die der äußeren Funktion angegeben) → didaktischer Typ, kein Prüfungstyp
- 3.9 Begründen (warum das Logarithmus-Argument positiv sein muss; warum ein stets positiver e-Term die Schranke unerreichbar macht) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Symmetrie** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 5 von 7 (Haupt 4) · FHR-Jahrgänge 8 von 8 (Haupt 8).

- 4.1 Symmetrie: Höhe einer waagerechten Sekante aus dem Abstand ihrer Schnittpunkte über die Symmetrie bestimmen (2) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 4.2 Symmetrie: Symmetrieart am Term über die Exponenten begründen (11) → wortgleich; GK 2 (2024, 2025), Haupt 2 · LK 4 (2017, 2018, 2022, 2024), Haupt 3 · FHR 0
- 4.3 Symmetrie am Funktionsterm beurteilen (7) → wortgleich; GK 0 · LK 0 · FHR 8, Haupt 8
- 4.4 Symmetrie: Fehlende Punktsymmetrie aus der Wertemenge begründen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 4.5 Symmetrie: Punktsymmetrie zum Wendepunkt über die Verschiebung einer ungeraden Funktion begründen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.6 Symmetrie: Punktsymmetrie über f(−x) = −f(x) nachweisen, eindeutige Nullstelle begründen und Grenzwert angeben (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.7 Symmetrie: Symmetrie eines Produkts symmetrischer Funktionen allgemein nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.8 Symmetrie: Weiteren Wendepunkt über die Punktsymmetrie ohne Rechnung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.9 Symmetrie: Weiteren Extrempunkt aus der Symmetrie des Graphen angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Fehler finden (das Absolutglied als ungeraden Summanden gewertet; einen Term mit gemischten Exponenten für symmetrisch erklärt; die Symmetrie nur am Bild abgelesen oder nur behauptet; f(−x) = −f(x) nur an einem Beispiel geprüft) → didaktischer Typ, kein Prüfungstyp
- 4.11 Begründen (warum das Absolutglied als gerader Exponent zählt; warum bei Punktsymmetrie mit jedem Wert auch sein Gegenwert angenommen wird) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Transformationen** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 5.1 Transformation: Periode einer Kosinusfunktion im Sachzusammenhang deuten und Stelle stärkster Zunahme am Graphen angeben (3) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 5.2 Transformation: Ableitungswert einer verschobenen Funktion über die Ausgangsfunktion berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.3 Transformation: An der x-Achse gespiegelte Funktion angeben und Durchmesser aus dem Funktionswert mit Maßstab berechnen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 5.4 Transformation: Funktionsterm nach Verschiebung in x-Richtung durch den Ursprung ermitteln (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 5.5 Transformation: Integrationsgrenzen und Faktor für ein Integral über den transformierten Graphen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.6 Transformation: Streckfaktor aus einer Flächenbedingung für den gestauchten Graphen bestimmen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 5.7 Transformation: Streckfaktor und Verschiebung aus zwei Termen durch Koeffizientenvergleich ermitteln und die Abbildung beschreiben (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.8 Transformation: Streckfaktoren aus der Zuordnung zweier Punkte deuten und berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.9 Transformation: Verschiebung einer Geraden aus dem Abstand der parallelen Geraden über das Steigungsdreieck ermitteln (1) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 5.10 Transformation: Graph eines in y-Richtung gestreckten Scharmitglieds begründen und skizzieren (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.11 Transformation: Verschiebung einer Exponentialfunktion als Streckung nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.12 Transformation: Wertemenge einer transformierten Funktion begründen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 5.13 Transformation: Anzahl verschiedener Ergebnisse bei vertauschter Reihenfolge von Spiegelung und Verschiebungen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.14 Transformation: Bild des Graphen unter Spiegelung, Streckung und Verschiebung als Ableitungsgraph nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.15 Transformation: Um 90° gedrehte Gerade und Bildpunkt einer Drehung um den Ursprung angeben (1) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 5.16 Transformation: Abbildung zwischen zwei Graphen angeben (8) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2026), Haupt 1 · FHR 0
- 5.17 Transformation: Aussage über eine Verschiebung zwischen zwei Graphen beurteilen (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 5.18 Transformation: Graphen einer periodischen Funktion mit vorgegebenem Maximum und Periode skizzieren (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 5.19 Transformation: Verschobenen Graphen in die Abbildung skizzieren (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.20 Transformation: Extrempunkt eines transformierten Graphen angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.21 Transformation: Funktionsterm nach Streckung in x-Richtung und Verschiebung angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.22 Transformation: Graph einer gestreckten und verschobenen Potenzfunktion skizzieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.23 Transformation: Streckfaktoren aus dem Term ablesen und Flächengleichheit der Bilddreiecke über das Produkt der Faktoren beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.24 Transformation: Term und Intervall des an der y-Achse gespiegelten Graphen angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.25 Transformation: Terme der an den Koordinatenachsen gespiegelten Randlinien angeben (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.26 Transformation: Verschiebung und Streckung der Grundhyperbel aus dem Term beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.27 Transformation: Wertebereich einer gestreckten und verschobenen Sinusfunktion angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.28 Fehler finden (die Verschiebung in die falsche Richtung gelesen; den Faktor im Argument nicht invertiert; die Reihenfolge von Spiegelung und Verschiebung vertauscht; die Verschiebung in x-Richtung auf die Wertemenge angewandt; die Intervallenden nach der Spiegelung nicht getauscht) → didaktischer Typ, kein Prüfungstyp
- 5.29 Begründen (warum Änderungen im Argument gegenläufig wirken; warum die Reihenfolge nur zwischen Spiegelung bzw. Streckung und y-Verschiebung zählt) → didaktischer Typ, kein Prüfungstyp

**Einheit 6 · Graph und Term** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 8 von 8 (Haupt 8).

- 6.1 Wertetabelle erstellen (3) → wortgleich; GK 0 · LK 0 · FHR 3 (2023, 2024, 2026), Haupt 3
- 6.2 Extrempunkte: Flächeninhalt eines Dreiecks aus Extrempunkten der Sinusfunktion berechnen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 6.3 Extrempunkte: Abstand von Extrempunkten einer gestreckten Sinusfunktion vergleichen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 6.4 Extrempunkte: Existenz eines Hochpunkts aus dem Grad und einem Tiefpunkt begründen und Koordinaten angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.5 Extrempunkte: Gerade durch die Hochpunkte einer Kosinusfunktion begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.6 Nullstellen und Werte: Geradengleichung aus der Abbildung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.7 Graph ganzrationaler Funktion im Intervall zeichnen (13) → wortgleich; GK 0 · LK 0 · FHR 8, Haupt 8
- 6.8 Nullstellen und Werte: Passenden Graphen zu einem Funktionsterm über Funktionswerte auswählen (3) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 6.9 Extrempunkte: Hochpunkt aus dem Graphen ablesen und im Sachzusammenhang deuten (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.10 Funktionswert am Graphen ablesen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 2 (2024, 2025), Haupt 2
- 6.11 Graph einer ganzrationalen Funktion zuordnen (2) → wortgleich; GK 0 · LK 0 · FHR 2 (2022, 2026), Haupt 2
- 6.12 Grad einer Funktion am Graphen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2024), Haupt 1
- 6.13 Koordinatenachsen in eine Abbildung einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2022, 2024), Haupt 1
- 6.14 Nullstellen und Werte: Aussage über die Achsenskalierung einer Abbildung beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.15 Nullstellen und Werte: Zeitliche Entwicklung eines Bestands über ein Intervall grafisch darstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.16 Fehler finden (beide Achsen gleich eingeteilt und den Graphen nicht aufs Blatt gebracht; die Randwerte nicht berechnet und den Graphen auslaufen lassen; beim Zuordnen nur die Form verglichen oder nur ein Merkmal geprüft; den Grad aus der Zahl der Nullstellen statt der Extrempunkte geschlossen; bei negativen Stellen das Vorzeichen der dritten Potenz verloren) → didaktischer Typ, kein Prüfungstyp
- 6.17 Begründen (warum eine Funktion mit drei Extrempunkten mindestens vierten Grades ist; warum ein einzelner berechneter Punkt die Achsenskalierung prüft) → didaktischer Typ, kein Prüfungstyp

### funktionsscharen-und-ortskurven

**Einheit 1 · Scharbegriff und Parameterwert** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 5 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Scharparameter aus einem Punkt des Graphen angeben (9) → wortgleich; GK 0 · LK 4 (2017, 2018, 2022, 2024), Haupt 2 · FHR 0
- 1.2 Parameter einer Schar aus einem vorgegebenen Punkt auf dem Graphen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Parameter einer Schar aus einer vorgegebenen Ausdehnung einer Figur bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Scharparameter aus Anfangswert und Grenzwert über das Vorzeichen des Exponenten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Scharparameter aus der Differenz zweier Scharfunktionswerte über eine Potenzgleichung bestimmen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 1.6 Scharparameter aus der Weite berechnen und Höhe des Hochpunkts angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen (4) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.8 Steigung und Achsenschnittpunkt des linearen Sonderfalls einer Schar angeben (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 1.9 Einfluss eines additiven Scharparameters auf den Graphen beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Einfluss eines multiplikativen Parameters auf den Graphen im Vergleich mit dem Ausgangsgraphen beschreiben (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 1.11 Gleichungen eines Bestimmungssystems für Scharparameter im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.12 Graph der Schar zu einem Parameterwert in die Abbildung skizzieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.13 Scharparameter den Graphen über Spiegelung und Extremstelle zuordnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.14 Scharparameter den Graphen über den y-Achsenabschnitt zuordnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.15 Scharparameter der Ausgangsfunktion angeben und Eignung zweier Scharfunktionen am Graphen beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.16 Fehler finden (den Parameter als Variable behandelt und nach x aufgelöst; das Vorzeichen im Exponenten beim Vergleich verloren; die Zuordnung an der Form statt an einem parameterabhängigen Merkmal festgemacht) → didaktischer Typ, kein Prüfungstyp
- 1.17 Begründen (warum ein Parameterwert genau einen Graphen liefert; warum der y-Achsenabschnitt die Kurven ordnet) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Eigenschaften aller Graphen am Term** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 7 von 7 (Haupt 6) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Gemeinsame Punkte aller Graphen einer Schar bestimmen (3) → wortgleich; GK 0 · LK 3 (2017, 2024, 2026), Haupt 1 · FHR 0
- 2.2 Nullstellen einer Funktionenschar mit Fallunterscheidung ermitteln (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.3 Anzahl der Nullstellen einer Schar in Abhängigkeit vom Parameter über die Diskriminante ermitteln (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.4 Genau zwei Nullstellen einer Schar aus der faktorisierten Form begründen und angeben (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 2.5 Grenzverhalten einer Potenzschar nach der Parität des Exponenten begründen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.6 Vorzeichen der Funktionswerte einer Schar begründen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.7 Gleiche Steigung aller Graphen einer Schar im Ursprung nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Gleichung zwischen Scharparameter und Nullstelle aus der Nullstellenbedingung herleiten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Grenzverhalten einer Schar angeben und parameterunabhängigen Funktionswert nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Nullstellen einer Schar am Term begründen und Tangentensteigungen dort nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.11 Nullstellen einer Schar angeben und Vorzeichen des y-Achsenabschnitts begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.12 Positivität, y-Achsenabschnitt und Steigung einer Schar begründen und berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.13 Punktsymmetrie aller Graphen einer Schar zum Ursprung nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.14 Punktsymmetrie aller Scharkurven und gemeinsame Tangente im Ursprung nachweisen (1) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 2.15 Symmetrieachse einer Scharkurve aus der Verschiebung einer geraden Funktion begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.16 Tangente im y-Achsenschnittpunkt aufstellen und als gemeinsame Tangente aller Scharkurven begründen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.17 Verschobene Scharfunktion als gerade Funktion nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.18 Vorzeichen aller Funktionswerte einer Schar am Term begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.19 Folgerungen aus gemeinsamen Eigenschaften einer Schar für den Verlauf der Graphen angeben (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.20 Grenzverhalten einer Schar für x → +∞ nach dem Parametervorzeichen angeben (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.21 Nullstellen einer Schar am faktorisierten Term angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.22 Fehler finden (den e-Faktor oder den Nenner als Nullstellenquelle behandelt; die Fallunterscheidung auf zwei Fälle verkürzt und den Sonderfall null vergessen; die Symmetrie nur für einen Parameterwert geprüft) → didaktischer Typ, kein Prüfungstyp
- 2.23 Begründen (warum an einem gemeinsamen Punkt der Parameter herausfällt; warum der Sonderfall Parameter null eigens zu prüfen ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Extrem- und Wendepunkte mit Parameter** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 7 von 7 (Haupt 7) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Abstand des Hochpunkts zu den Tiefpunkten einer Schar in Abhängigkeit vom Parameter berechnen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.2 Scharparameter aus einem Punkt bestimmen und Wendepunkt nachweisen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 3.3 Einzigen Extrempunkt einer Schar mit vorgegebener x-Koordinate nachweisen und y-Koordinate berechnen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.4 Extrempunkt einer Schar mit Art nach dem Parametervorzeichen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Hochpunkt einer Schar mit Parameterfaktor bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Hochpunkt im Ursprung über das Vorzeichen begründen und Tiefstelle einer Schar berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Lage und Art der Extrempunkte einer Schar bestimmen und Parameter für einen vorgegebenen Abstand der Extrempunkte berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Parameterwert für genau eine waagerechte Tangente bestimmen (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 3.9 Parameterwerte nach der Anzahl der Extrempunkte über die Lösbarkeit der Extremstellengleichung begründen (4) → wortgleich; GK 0 · LK 3 (2018, 2022, 2026), Haupt 3 · FHR 0
- 3.10 Gemeinsamen Extrempunkt einer Funktionenschar nachweisen (2) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 3.11 Hochpunkt einer Parabelschar mit Parameterkoordinaten nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Tiefpunkt einer Schar mit zwei Parametern nachweisen und Hochpunkt über die Punktsymmetrie begründen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 3.13 Ableitung einer Schar als Vielfaches der Ableitung eines Scharmitglieds nachweisen (1) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.14 Ableitung einer Schar nachweisen und zusammenhängenden Monotoniebereich ohne Rechnung begründen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.15 Einzigen Wendepunkt einer Schar nachweisen und angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.16 Extrempunkte aller Scharkurven aus dem Ableitungsgraphen eines Scharmitglieds ohne Rechnung begründen (1) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.17 Gemeinsamen und parameterabhängigen Wendepunkt einer Schar nachweisen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.18 Konstanten Abstand von Extrem- und Wendestelle einer Schar nachweisen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.19 Parameterwerte mit waagerechter Tangente über die Lösbarkeit der Ableitungsgleichung untersuchen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.20 Strenge Monotonie einer Schar über die Diskriminante der Ableitung für einen Parameterbereich nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.21 Tiefpunkt oder Sattelpunkt nach der Parität des Exponenten unterscheiden (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.22 Waagerechte Tangente aller Scharkurven in einem gemeinsamen Punkt nachweisen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.23 Wendepunkt einer Schar im Ursprung mit der x-Achse als Wendetangente nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.24 Eignung der Scharfunktionen über die Lage einer dritten Extremstelle beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.25 Nullstellenfreiheit aller Scharkurven aus dem gemeinsamen Tiefpunktwert beurteilen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 3.26 Scharparameter für genau eine Nullstelle über die Lage der Extrempunkte angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.27 Scharparameter für genau eine waagerechte Tangente aus dem Graphen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.28 Fehler finden (die hinreichende Bedingung weggelassen oder nur an einem Beispiel geführt; beim Ableiten den Parameterterm falsch behandelt; die Sattelstelle als Extremstelle mitgezählt) → didaktischer Typ, kein Prüfungstyp
- 3.29 Begründen (warum die Anzahl der Extrempunkte an der Lösbarkeit einer Gleichung hängt; warum eine parameterfreie Nullstelle der Ableitung allen Graphen gehört) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Parameter aus Bedingungen bestimmen** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen (4) → wortgleich; GK 0 · LK 2 (2023, 2024), Haupt 2 · FHR 0
- 4.2 Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen (3) → wortgleich; GK 0 · LK 2 (2017, 2024), Haupt 2 · FHR 0
- 4.3 Scharparameter aus der Flächengleichheit von Quadrat und Flächenstück bestimmen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.4 Scharparameter aus einem vorgegebenen Flächeninhalt zwischen Graph und x-Achse berechnen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.5 Scharparameter für eine vorgegebene Wendestelle berechnen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.6 Scharparameter für einen vorgegebenen Flächeninhalt eines Vierecks aus Hochpunkt und Achsenpunkten bestimmen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.7 Parameter einer Parabelschar aus dem knickfreien Übergang zu einem Graphen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.8 Parameter einer Schar aus gleichen Winkeln zweier Graphen mit einer Strecke bestimmen und Lage eines Punktes prüfen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.9 Parameter für genau zwei gemeinsame Punkte von Graph und Scharparabel über die Diskriminante bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Scharparameter aus der y-Koordinate der Tiefpunkte ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.11 Scharparameter aus einer Integralbedingung bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.12 Scharparameter für Hoch- und Tiefpunkt als Gegenecken eines achsenparallelen Quadrats bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.13 Scharparameter für den Mittelpunkt der Extrempunkte auf der x-Achse bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.14 Scharparameter für ein vorgegebenes Verhältnis zweier Radien einer Profilkurve berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.15 Scharparameter für einen Extrempunkt als Quadratecke bestimmen und Flächeninhalt berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.16 Scharparameter für einen Wendepunkt auf einer Geraden berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.17 Scharparameter für einen vorgegebenen Flächeninhalt zwischen Graph und x-Achse bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.18 Achsenschnittpunkte einer Schar bestimmen und Flächeninhalt des Achsendreiecks als Term im Parameter nachweisen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.19 Scharparameter für eine vorgegebene Tangente in einem Punkt untersuchen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.20 Vorzeichen der Stammfunktionen einer Schar durch Fallunterscheidung untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.21 Bedingungen für den sprungfreien Übergang von Funktionswert und Ableitung angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.22 Fehler finden (das Integral über einem Flächenstück unter der Achse positiv angesetzt; die Vorzeichenbedingung an den Parameter beim Sieben der Lösungen vergessen; die Parametergrenzen des Integrals als Zahlen behandelt) → didaktischer Typ, kein Prüfungstyp
- 4.23 Begründen (warum die Bedingung eine Gleichung im Parameter liefert; warum knickfrei mehr verlangt als sprungfrei) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Ortskurve und Kurvenvergleich** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 5.1 Ortskurve der Extrempunkte einer Schar durch Elimination des Parameters bestimmen (2) → wortgleich; GK 0 · LK 2 (2022, 2023), Haupt 2 · FHR 0
- 5.2 Abstand der Hochpunkte zweier benachbarter Scharparabeln berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.3 Abstand der y-Achsenabschnitte zweier benachbarter Scharkurven berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.4 Gemeinsamen Punkt von Scharkurve und ihrem Ableitungsgraphen in Abhängigkeit vom Parameter berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.5 Steigung der Ortsgeraden der Hochpunkte einer Schar aus zwei Hochpunkten berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.6 Gleichmäßige Streckung eines Scharfgraphen als Graph einer anderen Scharfunktion nachweisen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 5.7 Mittelpunkte der Strecken zum Ursprung auf einem gegebenen Graphen allgemein nachweisen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 5.8 Ortskurve der Extrempunkte einer Schar als Gerade über Sonderfall und Streckungseigenschaft begründen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 5.9 Spiegelung an der x-Achse als Scharmitglied nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.10 Trapez aus Funktions- und Ableitungswerten einer Schar begründen und Flächengleichheit für k und k + 1 nachweisen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 5.11 Existenz von Scharparametern mit beliebig vielen Schnittstellen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.12 Parameterunabhängigkeit der Fläche zwischen zwei Scharkurven nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.13 Punktsymmetrie zweier Scharkurven zueinander aus einer Identität nachweisen und deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.14 Schnittwinkel von Scharkurve und Ortskurve als nur von der Ortskurve abhängig begründen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 5.15 Aussage über den Ableitungsgraphen einer Schar als Tangente an den Scharfgraphen beurteilen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 5.16 Parameter des Extrempunkts mit kleinstem Abstand zum Ursprung an der Ortskurve näherungsweise erläutern und angeben (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 5.17 Fehler finden (beim Eliminieren den Parameter statt der Variablen eingesetzt; die Ortskurve für einen einzelnen Parameterwert bestätigt und für bewiesen gehalten; den Abstand benachbarter Kurven nur in einer Richtung genommen) → didaktischer Typ, kein Prüfungstyp
- 5.18 Begründen (warum die Elimination alle Extrempunkte zugleich erfasst; warum eine parameterfreie Differenz für alle Nachbarn gilt) → didaktischer Typ, kein Prüfungstyp

### rekonstruktion-von-funktionsgleichungen

**Einheit 1 · Ansatz und Punktbedingungen** – Abitur-Jahrgänge GK 2 von 9 (Haupt 1) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 7 von 8 (Haupt 7).

- 1.1 Funktionsgleichung mit Symmetriebedingung über LGS (4) → wortgleich; GK 0 · LK 0 · FHR 5 (2020, 2021, 2023, 2025, 2026), Haupt 4
- 1.2 Funktionsgleichung aus drei Punkten über LGS (3) → wortgleich; GK 0 · LK 0 · FHR 3 (2019, 2023, 2026), Haupt 3
- 1.3 Parameter einer Linearkombination aus Funktion und Gerade aus zwei Punkten bestimmen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 1.4 Ganzrationale Funktion dritten Grades aus drei Nullstellen und einem Punkt rekonstruieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Geradengleichung aus zwei Punkten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2022), Haupt 1
- 1.6 Parameter einer Exponentialfunktion aus zwei Punkten des Graphen bestimmen (1) → wortgleich; GK 1 (2018), Haupt 0 · LK 0 · FHR 0
- 1.7 Parameter einer Logarithmusfunktion aus Asymptote und Punkt ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Lineare Funktion durch zwei Punkte nachweisen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 1.9 Markante Punkte im Sachzusammenhang markieren und ablesen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2025), Haupt 1
- 1.10 Fehler finden (den vollen Ansatz gewählt, obwohl die Symmetrie ihn verkürzt; den y-Achsenabschnitt nicht direkt abgelesen; mit zwei Punkten ein unterbestimmtes System gebaut; den Punkt ungenau aus dem Bild abgelesen) → didaktischer Typ, kein Prüfungstyp
- 1.11 Begründen (warum die Symmetrie Koeffizienten streicht; warum jede Bedingung genau eine Gleichung liefert) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Bedingungen mit Ableitung** – Abitur-Jahrgänge GK 6 von 9 (Haupt 6) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 2 von 8 (Haupt 1).

- 2.1 Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren (3) → wortgleich; GK 2 (2019, 2023), Haupt 2 · LK 1 (2022), Haupt 1 · FHR 0
- 2.2 Quadratische Funktion aus Wert- und Steigungsbedingungen rekonstruieren (3) → wortgleich; GK 2 (2020, 2021), Haupt 2 · LK 0 · FHR 0
- 2.3 Funktionsgleichung aus knickfreiem Übergang und einer Wertbedingung rekonstruieren (2) → wortgleich; GK 2 (2018, 2022), Haupt 2 · LK 0 · FHR 0
- 2.4 Funktionsgleichung aus der Ableitung und einer Tangente über die Integrationskonstante rekonstruieren (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.5 Funktionsgleichung mit Extremalbedingung über LGS (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2021, 2025), Haupt 1
- 2.6 Ganzrationale Funktion aus Symmetrie und Randbedingungen rekonstruieren (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.7 Parameter einer Exponentialfunktion aus der Änderungsrate zum Anfangszeitpunkt bestimmen (1) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 2.8 Quadratische Funktion aus senkrechtem Schnitt mit einer Geraden und einer Extrempunktbedingung ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Fehler finden (den Hochpunkt nur als Punkt eingesetzt und die Ableitungsbedingung vergessen; knickfrei nur über den Funktionswert angesetzt; die Tangente falsch übersetzt; die Integrationskonstante vergessen; den Steigungswinkel ohne Tangens als Anstieg genommen) → didaktischer Typ, kein Prüfungstyp
- 2.10 Begründen (warum ein Wortpaar wie Hochpunkt zwei Gleichungen liefert; warum die Zahl der Bedingungen zur Zahl der Koeffizienten passen muss) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Sonderansätze und Modellkritik** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Maximum eines Parabelmodells aus einem Zeitraum ohne Durchschnittswachstum und einer Differenzbedingung ermitteln (1) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 3.2 Parameter einer Sinusfunktion aus Extremstelle und Funktionswert bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Parameter einer Sinusfunktion aus zwei aufeinanderfolgenden Extrempunkten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Sinusfunktion mit gleichen Nullstellen und gleichem Flächeninhalt wie ein Graph bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Steigung einer aus Periode und Extrempunkt rekonstruierten Kosinusfunktion allgemein bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Parabel ohne lineares Glied aus dem knickfreien Übergang begründen und Parameter aus einem Flächeninhalt berechnen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.7 Unmöglichkeit einer einzigen Parabel für ein knickfreies Profil mit zwei waagerechten Tangenten begründen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.8 Fehler finden (die halbe Periode als ganze genommen; die Amplitude als ganze Differenz der Extremwerte angesetzt; die Fläche nicht in Längeneinheiten des Modells umgerechnet; die Unmöglichkeit nur mit einem Punktargument begründet) → didaktischer Typ, kein Prüfungstyp
- 3.9 Begründen (warum der Abstand aufeinanderfolgender Extremstellen die halbe Periode ist; warum eine Parabel keinen Krümmungswechsel hat) → didaktischer Typ, kein Prüfungstyp

### stammfunktion-und-hauptsatz

**Einheit 1 · Stammfunktion** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Stammfunktion mit einer Wertebedingung bestimmen (3) → wortgleich; GK 1 (2020), Haupt 0 · LK 0 · FHR 0
- 1.2 Faktor für einen Stammfunktionsterm der Form r/x · f(x) bestimmen (1) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 1.3 Funktion aus einer gegebenen Stammfunktion durch Ableiten bestimmen (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 1.4 Stammfunktion aus einer vorgegebenen Integralgleichung ermitteln (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 1.5 Stammfunktion eines Polynomterms nach dem Ausmultiplizieren angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Stammfunktionen mit der x-Achse als Tangente über die Nullstellen der Funktion ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Stammfunktion durch Ableiten nachweisen (8) → wortgleich; GK 4 (2018, 2020, 2022, 2024), Haupt 4 · LK 1 (2023), Haupt 1 · FHR 0
- 1.8 Stammfunktionen mit vorgegebenem vertikalem Abstand zum Graphen einer Stammfunktion angeben (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 1.9 Fehler finden (aufgeleitet statt abgeleitet oder umgekehrt; die Integrationskonstante vergessen; beim Produktnachweis einen Faktor verloren; das Vorzeichen der inneren Ableitung verdreht) → didaktischer Typ, kein Prüfungstyp
- 1.10 Begründen (warum alle Stammfunktionen sich nur um eine Konstante unterscheiden; warum der Nachweis eine Ableitungsrechnung ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Hauptsatz** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 2 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Bestimmtes Integral einer ganzrationalen Funktion berechnen (4) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 2.2 Bestimmtes Integral mit vorgegebener Stammfunktion berechnen (4) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 2.3 Bestimmtes Integral einer trigonometrischen Funktion über eine Periode berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Integral der Ableitung als Differenz von Funktionswerten berechnen (1) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 2.5 Prozentuale Abweichung eines Näherungswerts vom exakten Wert berechnen (1) → wortgleich; GK 1 (2025), Haupt 0 · LK 1 (2024), Haupt 0 · FHR 0
- 2.6 Fehler finden (die Grenzen vertauscht; den Wert an der unteren Grenze mit falschem Vorzeichen abgezogen; einen Vorfaktor beim Integrieren vergessen; den Rechner im Gradmaß gelassen; die Abweichung auf den Näherungswert statt den exakten Wert bezogen) → didaktischer Typ, kein Prüfungstyp
- 2.7 Begründen (warum der Integralwert nicht von der Wahl der Stammfunktion abhängt; warum das Integral über eine volle Sinusperiode null ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Der Graphenblick** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Integral über f aus dem Graphen der Stammfunktion bestimmen (3) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.2 Funktionswert von f als Tangentensteigung am Graphen der Stammfunktion bestimmen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.3 Extremstelle aller Stammfunktionen über den Vorzeichenwechsel der gegebenen Ableitung begründen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2026), Haupt 1 · FHR 0
- 3.4 Höchstens eine positive Nullstelle jeder Stammfunktion über die Monotonie aus dem Vorzeichen des Integranden begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Maximumstelle aller Stammfunktionen über den Vorzeichenwechsel des Integranden begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Tiefpunkt aller Stammfunktionen auf der y-Achse über den Vorzeichenwechsel von f begründen und Stammfunktion mit Tiefpunkt im Ursprung bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Aussage über Extrempunkte einer Stammfunktion beurteilen (3) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2022), Haupt 1 · FHR 0
- 3.8 Graph einer Stammfunktion durch einen Punkt skizzieren (3) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 3.9 Aussage über den Krümmungswechsel der Stammfunktionen über das Vorzeichen von f am Graphen beurteilen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 3.10 Integrationsgrenzen mit Integral null über die zweite Ableitung am Graphen der Ableitung angeben (1) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.11 Fehler finden (Extremstellen von f als Extremstellen von F übernommen; einen Tiefpunkt von f als Tiefpunkt von F gezeichnet; den F-Wert statt der Steigung abgelesen; die Fläche unter dem Stammfunktionsgraphen bestimmt) → didaktischer Typ, kein Prüfungstyp
- 3.12 Begründen (warum eine Nullstelle von f ohne Vorzeichenwechsel keine Extremstelle von F liefert; warum die Aussage für jede Stammfunktion zugleich gilt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Integralfunktion** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Ganzzahlige Nullstellen einer Integralfunktion über gleiche Grenzen und Symmetrie begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.2 Höchstzahl der Nullstellen einer Integralfunktion über den Grad begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Maximum einer Integralfunktion über die Nullstelle des Integranden begründen und im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.4 Weitere Nullstelle einer Integralfunktion über die Flächenbilanz am Graphen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.5 Wendestelle einer Integralfunktion über die Ableitung des Integranden begründen und Funktionswert berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.6 Anzahl der Nullstellen einer Integralfunktion am Graphen beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Fehler finden (die Nullstellen des Integranden für Nullstellen der Integralfunktion gehalten; die untere Grenze als Nullstelle vergessen; die Flächenbilanz ohne Vorzeichen gerechnet) → didaktischer Typ, kein Prüfungstyp
- 4.8 Begründen (warum die untere Grenze immer Nullstelle ist; warum die Integralfunktion den Grad des Integranden um eins übertrifft) → didaktischer Typ, kein Prüfungstyp

### integrationsregeln

**Einheit 2 · Vorgegebene Regeln anwenden** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Integral über eine vorgegebene Regel für g' · e^g berechnen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.2 Fehler finden (das Vorzeichen der inneren Ableitung übersehen; g aus dem Exponenten falsch abgeschrieben; die Regel angewendet, ohne den Faktor anzupassen) → didaktischer Typ, kein Prüfungstyp
- 2.3 Begründen (warum die Regel nur für die Struktur g' · e^g gilt; warum das Anpassen des Vorzeichens ein Ausklammern von minus eins ist) → didaktischer Typ, kein Prüfungstyp

### flaecheninhalt-durch-integration

**Einheit 1 · Fläche zwischen Graph und x-Achse** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 2 von 7 (Haupt 1) · FHR-Jahrgänge 8 von 8 (Haupt 8).

- 1.1 Fläche zwischen Graph und x-Achse berechnen (10) → wortgleich; GK 0 · LK 0 · FHR 8, Haupt 7
- 1.2 Fläche: Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen (4) → wortgleich; GK 2 (2021, 2024), Haupt 2 · LK 0 · FHR 0
- 1.3 Fläche: Fläche zwischen Graph und Koordinatenachsen berechnen (2) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 1.4 Fläche: Fläche zwischen Graph, x-Achse und zwei senkrechten Geraden mit vorgegebener Stammfunktion berechnen (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 1.5 Fläche: Flächeninhalt einer Vorderansicht als Integral mit Maßstab und Abzug berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Fläche: Flächeninhalt zwischen Graph, x-Achse und senkrechter Gerade im Sachzusammenhang mit Maßstab berechnen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 0 · FHR 0
- 1.7 Ganzzahlige Nullstellen durch Probieren finden (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2022), Haupt 1
- 1.8 Gesamtfläche aus mehreren Teilflächen berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 2 (2019, 2021), Haupt 1
- 1.9 Fläche: Flächeninhalt zwischen Graph, x-Achse und senkrechter Gerade über das Integral nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Fläche: Flächeninhalt zwischen Graph und x-Achse am Bild mit einem berechneten Integralwert vergleichen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.11 Fehler finden (den negativen Integralwert ohne Betrag als Fläche angegeben; über eine Nullstelle hinweg in einem Zug integriert; nur eine Teilfläche berechnet; die untere Grenze am Zeichenintervall statt an der Nullstelle angesetzt) → didaktischer Typ, kein Prüfungstyp
- 1.12 Begründen (warum der Betrag nötig ist; warum die Nullstellen die Grenzen liefern) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Fläche zwischen zwei Graphen** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 7 von 8 (Haupt 6).

- 2.1 Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen (14) → wortgleich; GK 3 (2018, 2019, 2021), Haupt 3 · LK 3 (2018, 2023, 2026), Haupt 3 · FHR 0
- 2.2 Fläche zwischen zwei Graphen berechnen (6) → wortgleich; GK 0 · LK 0 · FHR 7 (2019, 2020, 2021, 2022, 2023, 2024, 2026), Haupt 6
- 2.3 Fläche: Fläche zwischen Graph und Hochpunktgerade über eine Periode berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Fläche: Fläche zwischen Graph und zwei Tangenten berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Fläche: Fläche zwischen zwei Graphen mit verschiedenen Grenzen als Differenz zweier Integrale berechnen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 2.6 Fläche: Flächeninhalt zwischen Graph und waagerechter Gerade als Term in der Grenze nachweisen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 2.7 Fläche: Aussage über den Flächeninhalt zwischen zwei Scharkurven als Parameterungleichung untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Fläche: Fläche zwischen Graph und waagerechter Gerade zwischen zwei nachgewiesenen Schnittstellen berechnen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 2.9 Fläche: Lösungsschritte zur Fläche zwischen zwei Scharkurven geometrisch deuten und Parameterungleichung untersuchen (1) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 2.10 Fehler finden (die Differenz in der falschen Reihenfolge gebildet und das Vorzeichen als Fläche gelassen; nur eine Randkurve integriert; beide Integrale über dieselben Grenzen gebildet, obwohl die Randkurven verschieden weit reichen) → didaktischer Typ, kein Prüfungstyp
- 2.11 Begründen (warum die Differenzfunktion die Fläche unabhängig von der Achsenlage liefert; warum ein Wechsel der oberen Funktion das Intervall teilt) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Zusammengesetzte Flächen, Maßstab und Volumen** – Abitur-Jahrgänge GK 6 von 9 (Haupt 6) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 3 von 8 (Haupt 2).

- 3.1 Fläche: Abschnittsweise begrenzte Fläche durch Integration berechnen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 3.2 Fläche: Differenz von Kreisfläche und Flügelflächen veranschaulichen und berechnen (1) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 3.3 Fläche: Eingeschlossene Fläche aus Integral, Symmetrie und Halbkreisen berechnen (1) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 3.4 Fläche: Fläche zwischen Graph, x-Achse und waagerechter Gerade aus Rechteck und Integral berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Fläche: Flächeninhalt aus einem vorgegebenen Term mit Stammfunktion berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Fläche: Flächeninhalt zwischen Graph, Achse und zwei Parallelen über Rechtecke und Integral berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Fläche: Querschnittsfläche eines Rotationskörpers als doppeltes Integral mit Maßstab berechnen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 3.8 Fläche: Querschnittsfläche zwischen Graph und Streckenzug als Integral minus Trapez und Dreieck berechnen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.9 Fläche: Querschnittsfläche zwischen Tangente und Graph als Dreieck minus Integral berechnen und mit der Breite zum Volumen umrechnen (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 3.10 Fläche: Radius eines flächengleichen Halbkreisprofils aus einem Integral bestimmen und Materialmasse berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.11 Fläche: Wasservolumen in einer Mulde aus Fläche zwischen Wasserlinie und Graph mal Breite berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Länge aus Volumen und Querschnittsfläche berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 1 (2025), Haupt 1
- 3.13 Volumen aus Querschnittsfläche und Länge (1) → wortgleich; GK 0 · LK 0 · FHR 3 (2021, 2025, 2026), Haupt 1
- 3.14 Fläche: An der Sehne gespiegelte Randlinien skizzieren und Lösungsweg für den Flächenzuwachs beschreiben (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 3.15 Fläche: Aufgabenstellung zu einem Volumen aus Fläche zwischen Graph und Gerade und Maßstab formulieren und erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.16 Fläche: Aufgabenstellung zu einer Summe zweier Integrale formulieren und die Integrale als Teilflächen im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.17 Fläche: Lösungsschritte zu einem Flächenverhältnis von Segment und Dreieck geometrisch deuten und Flächen einzeichnen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 3.18 Fläche: Änderung eines Flächeninhalts beim Ersetzen des Graphen durch die Sehne untersuchen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.19 Fehler finden (den Maßstab nur einfach statt quadriert angewandt; ein elementargeometrisches Teilstück vergessen oder mit falschem Vorzeichen; Fläche und Volumen multipliziert statt geteilt; die Volumeneinheit mit dem falschen Faktor umgerechnet) → didaktischer Typ, kein Prüfungstyp
- 3.20 Begründen (warum der Flächenmaßstab das Quadrat des Längenmaßstabs ist; warum die Zerlegung an der Additivität des Integrals hängt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Flächenbedingungen** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen Graph und Gerade bestimmen (3) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.2 Fläche: Senkrechte Gerade zur Halbierung einer Fläche über den Flächenterm bestimmen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 4.3 Fläche: Achsenschnittpunkt einer Geraden aus einer Flächenbedingung über Rechteck und Dreieck bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.4 Fläche: Gerade zur Halbierung der Fläche zwischen Scharkurve und Koordinatenachsen ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.5 Fläche: Parallele Gerade zur Halbierung einer Fläche über ein Achsendreieck bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.6 Fläche: Verschiebung für die Halbierung einer Fläche über ein Integral bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Integralwert: Eindeutige Lösung einer Flächengleichung über die Monotonie des Flächeninhalts begründen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.8 Fläche: Prozentuale Abweichung einer Dreiecksnäherung vom Flächeninhalt zwischen Scharkurve und Achsen als parameterunabhängig nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.9 Integralwert: Existenz einer Grenze mit Integralwert null über den Vorzeichenwechsel und die Stetigkeit am Graphen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Integralwert: Existenz einer oberen Grenze mit Integralwert null über den Flächenausgleich ohne Rechnung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.11 Integralwert: Existenz eines Flächenstücks mit vorgegebenem Inhalt über die Stammfunktion begründen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.12 Integralwert: Lösung einer Integralgleichung über die Punktsymmetrie und ein Rechteck am Graphen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.13 Fläche: Flächenstück zwischen zwei Scharkurven und der x-Achse markieren und Gleichung für den Parameter aus dem Flächeninhalt angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.14 Integralwert: Anzahl der Lösungen einer Integralgleichung über gleitende Streifen am Graphen untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.15 Fehler finden (die Halbierungsbedingung an die falsche Größe geknüpft; ein konkretes Beispiel ausgerechnet, wo eine Existenzbegründung verlangt war; nur die Existenz, nicht die Eindeutigkeit begründet) → didaktischer Typ, kein Prüfungstyp
- 4.16 Begründen (warum ein monoton wachsender Flächenterm jeden Zwischenwert genau einmal annimmt; warum die Halbierung eine Gleichung liefert) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Das Integral als Flächenbilanz** – Abitur-Jahrgänge GK 6 von 9 (Haupt 6) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 5.1 Integralwert: Integralwert grafisch durch Kästchenzählen bestimmen (3) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.2 Integralwert: Mittelwert einer Funktion als Integral geteilt durch die Intervalllänge berechnen und deuten (3) → wortgleich; GK 2 (2019, 2023), Haupt 2 · LK 1 (2026), Haupt 1 · FHR 0
- 5.3 Integralwert: Integral als Flächeninhalt zwischen Graph und x-Achse deuten und über die Stammfunktion berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.4 Integralwert: Integral mit Wert null am Graphen begründen (3) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 5.5 Integralwert: Integral über die Summe aus ungerader Funktion und Konstante ohne Stammfunktion begründen (3) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 5.6 Integralwert: Näherungswert eines Integrals als Vielecksfläche am Graphen begründen (3) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 5.7 Integralwert: Flächenterm einer an y = x gespiegelten Figur über Rechteck und Integral begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.8 Integralwert: Grenzen für ein positives Produkt zweier Integrale über die Vorzeichen der Hyperbeläste angeben und begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.9 Integralwert: Integral null über die Punktsymmetrie begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.10 Integralwert: Integral über die Punktsymmetrie zum Wendepunkt als Dreiecksfläche unter einer Sekante begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.11 Integralwert: Integral über eine Summe aus e-Funktion und linearem Term gegen eine Schranke nachweisen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 5.12 Integralwert: Integralwert über die Punktsymmetrie und ein Quadrat geometrisch begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.13 Integralwert: Ungleichung zweier Integrale über das Vorzeichen des Teilintegrals am Graphen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.14 Integralwert: Vorzeichen eines Differenzintegrals über Flächenvergleich am Graphen begründen und im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.15 Integralwert: Integral als Flächeninhalt für alle Scharkurven über das Vorzeichen des Terms beurteilen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 5.16 Integralwert: Integralabschätzung über ein Rechteck und Flächenvergleich am Graphen erläutern und im Sachzusammenhang deuten (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 5.17 Integralwert: Summe zweier Integrale als Flächeninhalt beurteilen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 5.18 Integralwert: Aussage über zwei Integrale über die Lage des Graphen zur x-Achse beurteilen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 5.19 Integralwert: Integral einer Differenzfunktion grafisch abschätzen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.20 Integralwert: Integrale der Ableitung über das Vorzeichen des Ableitungsgraphen vergleichen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 5.21 Integralwert: Negativen Integralwert als Differenz zweier Flächeninhalte am Graphen erläutern (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 5.22 Integralwert: Nullwert eines Integrals über eine Differenzfunktion mit drei Schnittstellen als Flächengleichheit deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.23 Integralwert: Vorgehen zur grafischen Bestimmung eines Integrals beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.24 Integralwert: Vorzeichen eines Integrals am Graphen beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.25 Fehler finden (Integralwert und Flächeninhalt gleichgesetzt; Flächeninhalte statt orientierter Integrale verglichen; Kästchen als Einheitsquadrate gezählt; das Flächenstück oberhalb der Achse mit demselben Vorzeichen wie das darunter) → didaktischer Typ, kein Prüfungstyp
- 5.26 Begründen (warum das Integral über eine ungerade Funktion auf symmetrischem Intervall null ist; warum der Mittelwert die Fläche zu einem Rechteck glättet) → didaktischer Typ, kein Prüfungstyp

### rekonstruktion-von-bestaenden

**Einheit 1 · Bestand aus Rate** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten (4) → wortgleich; GK 0 · LK 2 (2024, 2026), Haupt 2 · FHR 0
- 1.2 Zunahme eines Bestands als Differenz der Bestandsfunktion und mittlere Änderungsrate im Zeitraum berechnen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 1.3 Anfangsbestand aus Endbestand und Fläche unter dem Ableitungsgraphen ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Bestand nach einem Zeitraum aus Anfangsbestand und Integral der Änderungsrate berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Bestandsänderung grafisch als Fläche unter dem Ratengraphen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Zurückgelegte Strecke als Integral der Geschwindigkeit mit Umrechnung der Einheiten berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Zurückgelegte Strecke aus dem Integral der Geschwindigkeit und einer Phase konstanter Geschwindigkeit berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Term für einen Bestand aus einer Rate über ein Integral angeben (3) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 1.9 Gleichung für den Zeitpunkt eines Bestandswerts über ein Integral der Rate angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Fehler finden (den Anfangsbestand vergessen; die Grenzen als Uhrzeiten statt als Modellstunden eingesetzt; den Einheitenfaktor verloren; die Rate über ihren Geltungsbereich hinaus integriert) → didaktischer Typ, kein Prüfungstyp
- 1.11 Begründen (warum der neue Bestand alter Bestand plus Integral ist; warum die Einheit des Integrals Rate mal Zeit ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Rate und Bestand als Paar** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen (3) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.2 Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.3 Zunahme eines Bestands aus dem Vorzeichen der Rate begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Integralfunktion einer Rate und ihren Grenzwert als Bestand und Endwert im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Fehler finden (den Hochpunkt der Rate mit dem größten Bestand verwechselt; nur die Ableitung geprüft und den Anfangswert vergessen; die Rate als Bestand gelesen und ihre Monotonie untersucht) → didaktischer Typ, kein Prüfungstyp
- 2.6 Begründen (warum der Bestand am Vorzeichenwechsel der Rate kippt; warum eine Kandidatenfunktion zwei Prüfungen braucht) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Am Ratengraphen** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Integral der Differenz zweier Änderungsraten berechnen und als Bestandsdifferenz deuten (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 3.2 Zeitpunkt gleichen Bestands am Ratengraphen über gleich große Flächen markieren und begründen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.3 Gleichheit der Flächen unter Eingangs- und Ausgangsrate als gleiche Gesamtzahl im Sachzusammenhang erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Nullstelle eines Differenzintegrals als Zeitpunkt gleicher Strecke deuten und ihre Lage begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Fehler finden (den Zeitpunkt mit gleichem Ratenwert statt gleichem Bestand markiert; die Nullstelle des Differenzintegrals mit dem Schnittpunkt der Raten gleichgesetzt; Teilflächen verglichen, ohne den gemeinsamen Teil zu erwähnen) → didaktischer Typ, kein Prüfungstyp
- 3.6 Begründen (warum gleiche Bestände gleiche Flächen ober- und unterhalb bedeuten; warum die Streckengleichheit nach dem Geschwindigkeitsschnittpunkt liegt) → didaktischer Typ, kein Prüfungstyp

### rotationsvolumen

**Einheit 1 · Die Volumenformel** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 3 von 8 (Haupt 3).

- 1.1 Rotationsvolumen um die x-Achse berechnen (4) → wortgleich; GK 0 · LK 0 · FHR 3 (2019, 2020, 2024), Haupt 3
- 1.2 Gleichung für die Füllhöhe aus einem Rotationsvolumen zwischen variablen Grenzen aufstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Wasservolumen als Differenz aus Rotationsvolumen und Kugelvolumen nach unten abschätzen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Fehler finden (den Funktionsterm nicht oder gliedweise quadriert; das gemischte Glied vergessen; die Kreiszahl weggelassen; das Volumen in Volumeneinheiten stehen gelassen) → didaktischer Typ, kein Prüfungstyp
- 1.5 Begründen (warum quadriert wird – der Funktionswert ist der Radius der Kreisscheibe; warum der Volumenmaßstab die dritte Potenz trägt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Um den Körper herum** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Umbeschriebenes Prisma zu einem Rotationskörper bestimmen (2) → wortgleich; GK 0 · LK 2 (2017, 2018), Haupt 2 · FHR 0
- 2.2 Integranden als Querschnittsfläche über den Satz des Pythagoras deuten und Umrechnungsfaktor erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Rotationsvolumen über einbeschriebene Zylinder abschätzen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Aufgabenstellung zu einem Rotationsvolumen-Anteil aus dem Lösungsweg formulieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Fehlerhaftes Verfahren zur Volumenberechnung beurteilen und berichtigen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.6 Integralfunktion im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.7 Fehler finden (die Rotationsachse nicht geprüft und den x-Achsen-Ansatz übernommen; den Umkreis- statt des Inkreisradius genommen; den Zylinderterm als Kegel gedeutet; die Kugel in die Schicht eingerechnet) → didaktischer Typ, kein Prüfungstyp
- 2.8 Begründen (warum der Integrand eine Kreisfläche ist; warum einbeschriebene Zylinder eine untere Schranke liefern) → didaktischer Typ, kein Prüfungstyp

### uneigentliche-integrale

**Einheit 2 · Die Näherungsdeutung** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.2 Fehler finden (die Aussage als Gleichheit von Stammfunktionen gelesen; die Restfläche für null statt für vernachlässigbar erklärt) → didaktischer Typ, kein Prüfungstyp
- 2.3 Begründen (warum die Differenz zweier Stammfunktionswerte eine Fläche ist; warum ein gegen null laufender Graph die Restfläche klein hält) → didaktischer Typ, kein Prüfungstyp

### punkte-und-strecken-im-koordinatensystem

**Einheit 1 · Punkte darstellen und Lage lesen** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 1 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Punkt: Lage zweier Punkte zu einer Koordinatenebene begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Ebene Figur: Lage eines Dreiecks parallel zu einer Koordinatenebene und symmetrisch zu einer anderen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Ebene Figur: Viereck in ein Schrägbild einzeichnen (2) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 1.4 Ebene Figur: Dreieck in ein Schrägbild einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Ebene Figur: Projektion eines Parallelogramms in eine Koordinatenebene einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Ebene Figur: Symmetrisches Achteck in der Koordinatenebene vervollständigen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Körper: Körper in ein räumliches Koordinatensystem einzeichnen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 0 · FHR 0
- 1.8 Körper: Lage des Höhenfußpunkts einer Pyramide über die Projektion in die Grundflächenebene entscheiden (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.9 Körper: Netz einer Pyramide vervollständigen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 1.10 Fehler finden (Punkte auf die falschen Kanten gesetzt; das Vorzeichen negativer Koordinaten beim Eintragen verloren; die Symmetrie zur falschen Koordinatenebene behauptet; die Spitze statt ihrer Projektion betrachtet) → didaktischer Typ, kein Prüfungstyp
- 1.11 Begründen (warum eine Koordinate null den Punkt in die Koordinatenebene legt; warum die Projektion parallel zur Achse genau eine Koordinate löscht) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Streckenlängen, Mittelpunkt und Teilpunkte** – Abitur-Jahrgänge GK 5 von 9 (Haupt 3) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Punkt: Koordinaten eines Punktes auf einer Strecke in Abhängigkeit von seiner Höhe ermitteln (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.2 Körper: Gesamtlänge der Dachkanten einer Pyramide mit Zuschlag berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Körper: Geschwindigkeit entlang einer Kante aus Kantenlänge und Zeit berechnen (1) → wortgleich; GK 1 (2018), Haupt 0 · LK 0 · FHR 0
- 2.4 Körper: Länge eines Streckenzugs aus Kanten und Diagonalen eines Quaders im Sachzusammenhang berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Punkt: Begegnungspunkt zweier gleichzeitig startender Bewegungen auf einer Strecke aus den Geschwindigkeiten berechnen (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 2.6 Punkt: Lage eines bewegten Punktes gegenüber einer Mauer über Zeitpunkt und Höhe untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Punkt: Länge einer Strecke aus einer Vektorbeziehung der Ortsvektoren berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Punkt: Teilpunkte einer Strecke in drei gleiche Abschnitte berechnen (1) → wortgleich; GK 1 (2023), Haupt 0 · LK 0 · FHR 0
- 2.9 Punkt: Ursprüngliche Länge einer Strecke aus der Streckenlänge und einer prozentualen Verlängerung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Körper: Kantenlänge eines Würfels aus gegenüberliegenden Oktaederecken nachweisen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.11 Punkt: Mittelpunkt einer Kante nachweisen und symmetrischen Schnittpunkt angeben (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 2.12 Punkt: Zweiten Punkt auf einer Geraden mit gleichem Abstand zu einem Geradenpunkt über den Richtungsvektor angeben (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 2.13 Fehler finden (Koordinaten statt Koordinatendifferenzen quadriert; das Teilverhältnis mit dem Anteil verwechselt; den Zuschlag in der falschen Einheit addiert; den Prozentsatz abgezogen statt geteilt) → didaktischer Typ, kein Prüfungstyp
- 2.14 Begründen (warum die Längenformel der räumliche Pythagoras ist; warum der Mittelpunkt koordinatenweise der Mittelwert ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Dreiecke nachweisen** – Abitur-Jahrgänge GK 4 von 9 (Haupt 3) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Ebene Figur: Eckpunkt auf einer Achse aus dem Umfang eines Dreiecks bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Ebene Figur: Eckpunkt eines flächen- und umfangsgleichen Dreiecks über eine Parallelverschiebung angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Ebene Figur: Vierten Eckpunkt einer Raute zu einem gleichschenkligen Dreieck über die Punktspiegelung am Seitenmittelpunkt bestimmen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 3.4 Ebene Figur: Zwei Ecken eines gleichschenkligen Dreiecks mit gleichem Abstand zu einem Mittelpunkt angeben (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 3.5 Punkt: Mittelpunkt des Kreises durch drei Punkte der Ebene über Mittelsenkrechte und Abstandsgleichung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Ebene Figur: Gleichschenkligkeit eines Dreiecks mit Parameter über die Schenkellängen nachweisen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.7 Ebene Figur: Gleichschenkligkeit oder Gleichseitigkeit eines Dreiecks über die Seitenlängen prüfen (2) → wortgleich; GK 2 (2020, 2023), Haupt 1 · LK 0 · FHR 0
- 3.8 Ebene Figur: Gleichschenkligkeit über kongruente rechtwinklige Dreiecke begründen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.9 Ebene Figur: Rechtwinkliges gleichschenkliges Dreieck aus den Koordinaten begründen und Flächeninhalt angeben (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.10 Ebene Figur: Gleichschenkligkeit über Seitenlängen nachweisen und Parallelität einer Kante zur Grundfläche begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.11 Ebene Figur: Lage dreier Punkte auf einem Kreis über den Thaleskreis begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Fehler finden (die Basis als Schenkel geprüft; nur zwei Seiten berechnet und die dritte nicht geprüft; den rechten Winkel an der falschen Ecke vermutet; beim Quadrieren die Wurzel nicht isoliert) → didaktischer Typ, kein Prüfungstyp
- 3.13 Begründen (warum zwei gleiche Schenkellängen genügen und welche Seite die Basis ist; warum der Thaleskreis den rechten Winkel liefert) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Vierecke nachweisen** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Ebene Figur: Eckpunkt eines Quadrats in einer Ebene aus zwei benachbarten Ecken berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.2 Ebene Figur: Eckpunkte einer Raute mit einer Seite auf einer Geraden bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen (6) → wortgleich; GK 2 (2018, 2026), Haupt 2 · LK 0 · FHR 0
- 4.4 Ebene Figur: Benachbarte Ecke eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen (2) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 4.5 Ebene Figur: Parallelogramm als Rechteck über das Skalarprodukt nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.6 Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Ebene Figur: Raute über vier gleich lange Seiten nachweisen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.8 Ebene Figur: Trapez mit zwei gleich langen Seiten über Kollinearität und Seitenlängen nachweisen (2) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 4.9 Ebene Figur: Berührpunkt des Inkreises einer Raute über Lage auf der Seite und Orthogonalität zum Mittelpunkt begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Ebene Figur: Drachenviereck über zwei Paare gleich langer Seiten nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.11 Ebene Figur: Größeren Teil einer Wand über die Lage der Diagonalen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.12 Ebene Figur: Parallelität zweier Seiten und rechten Winkel eines Vierecks über Vektoren nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.13 Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen und Rechteck über das Skalarprodukt ausschließen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.14 Ebene Figur: Raute über gleiche Seitenvektoren nachweisen und Quadrat über das Skalarprodukt ausschließen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.15 Ebene Figur: Rechteck mit Parameter nachweisen und Seitenlänge in Abhängigkeit vom Parameter berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.16 Ebene Figur: Ansatz für einen rechten Innenwinkel eines Vierecks über das Skalarprodukt mit unbekannter Koordinate erläutern (2) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 4.17 Fehler finden (AB mit CD statt DC verglichen; nur vier gleiche Seiten gezeigt und das Parallelogramm weggelassen; die Parallelität aus gleich langen Vektoren statt aus dem Vielfachen geschlossen; nur zwei Seiten der Raute verglichen; gegenüberliegende statt benachbarter Seiten beim Drachenviereck) → didaktischer Typ, kein Prüfungstyp
- 4.18 Begründen (warum ein Gegenmerkmal zum Ausschließen genügt; warum im Raum vier gleiche Seiten allein die Raute nicht sichern) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Körper im Koordinatensystem und Drehungen** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 5.1 Körper: Anteil der Bodenfläche unter einer Mindesthöhe über den Strahlensatz am Dachquerschnitt berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.2 Körper: Kantenlänge eines Würfels mit einer Ecke auf einer Pyramidenkante berechnen und Lage im Inneren begründen (1) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 5.3 Punkt: Bildpunkt einer Drehung um eine Kante in eine Koordinatenebene über Lotfußpunkt und Abstand berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.4 Körper: Parallelität der Grundfläche einer Pyramide zu einer Koordinatenebene begründen und Höhe angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.5 Körper: Punkt auf dem Rand der Grundfläche eines Zylinders nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.6 Körper: Koordinaten eines Eckpunkts eines Prismas angeben (4) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 5.7 Körper: Eckenzahl der Schnittvielecke einer Ebenenschar mit einem Körper und Sonderfälle angeben (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.8 Körper: Koordinaten der Eckpunkte eines beschriebenen Körpers wählen (2) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 5.9 Körper: Eckpunkt mit vorgegebenen Vorzeichen nach einer Verschiebung angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.10 Punkt: Bildpunkte einer Drehung um eine Koordinatenachse mit vorgegebener Koordinate angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.11 Punkt: Lösungsweg für den Bildpunkt einer Drehung um eine Kante über Lotfußpunkt und Abstand beschreiben (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 5.12 Fehler finden (zwei Deckenecken verwechselt; die Ecke nach der größten Koordinate statt nach der Lage zum Mittelpunkt benannt; die Hypotenuse auf eine Achse gelegt; um den Ursprung statt um die Kante gedreht; die Vierteldrehung nicht erkannt) → didaktischer Typ, kein Prüfungstyp
- 5.13 Begründen (warum die Deckenecke eines geraden Prismas senkrecht über der Grundecke liegt; warum der gedrehte Punkt auf einem Kreis um den Lotfußpunkt läuft) → didaktischer Typ, kein Prüfungstyp

### vektoren-und-rechenoperationen

**Einheit 1 · Vektorbegriff, Betrag und Kollinearität** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Koordinate eines Vektors aus vorgegebener Länge bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Fehlende Koordinate eines Punktes aus der Parallelität zweier Kanten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Unterschiedliche Beträge von Vektoren mit fester Komponentensumme über ein Beispiel begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Blickrichtungsvektoren zu schematischen Ansichten angeben und eine weitere Ansicht zeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Verbindungsvektor zweier Würfelecken mit gleicher Länge wie eine Raumdiagonale und nicht kollinear angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Fehler finden (die Beträge komponentenweise addiert statt die Betragsformel zu nehmen; beide Vorzeichen behalten, obwohl eine Bedingung eines ausschließt; den Gegenvektor als „nicht kollinear“ angeboten) → didaktischer Typ, kein Prüfungstyp
- 1.7 Begründen (warum das Quadrieren der Betragsgleichung beide Vorzeichen liefert; warum gleiche Komponentensumme nichts über die Länge sagt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Vektorterme am Körper** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Verschobenen Punkt über den Diagonalenschnittpunkt bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.2 Vierten Eckpunkt eines Quadrats über eine Vektoraddition bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Vektorterm für einen Eckpunkt eines Pyramidenstumpfs begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Lage eines Punktes zu einem Vektorterm im Quader beschreiben (2) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.5 Punkt zu einem Vektorterm in das Schrägbild einzeichnen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.6 Verbindungsvektor zweier Kantenmittelpunkte als Linearkombination der Kantenvektoren angeben (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Ortsvektor eines gedrehten Punktes als Term aufstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Punkt aus einer Linearkombination von Kantenvektoren in das Schrägbild einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Vektorterm für einen Punkt aus Lotfußpunkt, Abstand und Richtungsvektor angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Fehler finden (eine ganze Kante abgetragen, wo der Faktor sie halbiert; das Vorzeichen eines Kettenglieds verdreht; den Richtungsvektor ohne Normierung mit dem Abstand multipliziert; den Diagonalenschnittpunkt aus einer Flächendiagonale berechnet) → didaktischer Typ, kein Prüfungstyp
- 2.11 Begründen (warum jeder Weg über die Ecken denselben Verbindungsvektor liefert; warum der Einheitsvektor die Länge eins hat und der Term deshalb den Abstand trifft) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Skalarprodukt im Sachzusammenhang** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Mengen aus einem Mischungsverhältnis und einem vorgegebenen Skalarprodukt berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Skalarprodukt zweier Sachvektoren als Gesamtpreis deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Fehler finden (das Skalarprodukt als Vektor gedeutet; die Gesamtsumme durch die Preissumme geteilt statt das Verhältnis anzusetzen) → didaktischer Typ, kein Prüfungstyp
- 3.4 Begründen (warum das Skalarprodukt eine Zahl ist; warum der Verhältnisansatz mit einem Faktor alle Komponenten zugleich trifft) → didaktischer Typ, kein Prüfungstyp

### linearkombination-und-lineare-abhaengigkeit

**Einheit 2 · Linearkombination mit Nebenbedingung** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.2 Fehler finden (die Behauptung an einem einzelnen Zahlenbeispiel geprüft statt allgemein umgeformt; die Intervallbedingung vergessen und die ganze Gerade erhalten) → didaktischer Typ, kein Prüfungstyp
- 2.3 Begründen (warum r = 1 − s die Kombination auf eine Parameterform bringt; warum die Grenzen des Parameters die Endpunkte der Strecke liefern) → didaktischer Typ, kein Prüfungstyp

### geraden

**Einheit 1 · Geradengleichung aufstellen und lesen** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Parallele Gerade durch einen Teilpunkt einer Strecke bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Parallelität einer Geraden zu einer Koordinatenachse über die Koordinaten begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Echt parallele und senkrecht schneidende Gerade zu einer gegebenen Geraden angeben (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 1.4 Gerade in einer Ebene durch einen Punkt parallel zu einer Koordinatenebene angeben (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 1.5 Geradengleichung durch zwei Punkte aufstellen (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 1.6 Parametergleichung einer Strecke im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Fehler finden (für die echt parallele Gerade einen Stützpunkt auf der Geraden selbst gewählt; einen Spannvektor der Ebene als Richtungsvektor genommen, der die Koordinatenebene schneidet; das Teilverhältnis als Bruchteil gelesen; die Streckengleichung als ganze Gerade gedeutet) → didaktischer Typ, kein Prüfungstyp
- 1.8 Begründen (warum die Punktprobe des Stützpunkts über echt parallel entscheidet; warum die Richtungskomponente null den Schnitt mit der Koordinatenebene verhindert) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Punktprobe und Punkte auf der Geraden** – Abitur-Jahrgänge GK 5 von 9 (Haupt 4) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen (2) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.2 Höhe eines Punktes auf einer Strecke aus der Entfernung vom Anfang berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Punkt auf einer Geraden mit vorgegebener Koordinate angeben (1) → wortgleich; GK 2 (2019, 2025), Haupt 0 · LK 0 · FHR 0
- 2.4 Punktprobe an einer Geraden durchführen (11) → wortgleich; GK 3 (2018, 2023, 2025), Haupt 3 · LK 1 (2025), Haupt 1 · FHR 0
- 2.5 Kollinearität dreier Punkte über die Verbindungsvektoren nachweisen (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 2.6 Fehler finden (nur eine oder zwei Koordinaten geprüft; den Abstand als Parameterwert genommen statt den Richtungsvektor zu normieren; die Entfernung direkt als Parameter eingesetzt; bei der Strecke den Parameterbereich nicht geprüft; Schar- und Geradenparameter als denselben Parameter behandelt) → didaktischer Typ, kein Prüfungstyp
- 2.7 Begründen (warum ein einziger Widerspruch die Punktprobe entscheidet; warum der Parameter bei der Strecke zwischen null und eins liegen muss) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Lage als Anhang** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Parallelität zweier Geraden über die Richtungsvektoren prüfen (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 3.2 Geradengleichung durch zwei Punkte aufstellen und windschiefe Lage begründen (3) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.3 Nichtidentität zweier Geraden über die Richtungsvektoren begründen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.4 Existenz eines Geradenschnittpunkts über die gemeinsame Ebene begründen (1) → wortgleich; GK 1 (2018), Haupt 1 · LK 0 · FHR 0
- 3.5 Nichtidentität zweier paralleler Geraden über den Verbindungsvektor begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Schnitt einer senkrecht schneidenden Geraden mit einer parallelen Geraden beurteilen (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 3.7 Fehler finden (wegen des gemeinsamen Stützpunkts Identität angenommen; gleiche Richtungsvektoren als Identität gelesen; die Windschiefe nur über die fehlende Parallelität begründet; nur „kein Schnittpunkt“ gezeigt und die Parallelität nicht ausgeschlossen) → didaktischer Typ, kein Prüfungstyp
- 3.8 Begründen (warum zwei nicht parallele Geraden einer Ebene sich schneiden müssen; warum senkrechtes Schneiden im Raum keinen Schnitt mit der Parallelen erzwingt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Sachgeraden** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Höhenunterschied zweier übereinanderliegender Punkte auf Seilgeraden bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.2 Neigung einer Strecke in Prozent aus Höhendifferenz und Horizontalabstand berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Lösungsweg zur Bestimmung eines Punktes auf einer Geraden beschreiben (2) → wortgleich; GK 1 (2018), Haupt 1 · LK 0 · FHR 0
- 4.4 Lösungsansatz für eine bewegte Gerade durch einen festen Punkt erläutern und im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.5 Fehler finden (den vertikalen Abstand als Abstand windschiefer Geraden gerechnet; die Seillänge statt des Horizontalabstands als Bezug der Neigung genommen; die Höhendifferenz als Lotfußpunkt-Abstand beschrieben; das Intervall des Streckenparameters nicht erläutert) → didaktischer Typ, kein Prüfungstyp
- 4.6 Begründen (warum „vertikal übereinander“ zwei Koordinatengleichungen liefert; warum die Neigung ein Quotient zweier Längen ist) → didaktischer Typ, kein Prüfungstyp

### lagebeziehungen

**Einheit 1 · Punktprobe und Seitenlage** – Abitur-Jahrgänge GK 7 von 9 (Haupt 6) · LK 1 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen (10) → wortgleich; GK 6 (2018, 2019, 2021, 2022, 2025, 2026), Haupt 5 · LK 1 (2026), Haupt 0 · FHR 0
- 1.2 Punkt und Ebene: Aussage über das Innere eines Dreiecks unter Koordinatentausch mit einem Gegenbeispiel widerlegen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Punkt und Ebene: Lage eines Punktes zwischen zwei parallelen Ebenen über Einsetzen in die Koordinatengleichungen begründen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 1.4 Punkt und Ebene: Verlauf zweier Ebenen durch das Innere eines Körpers über Punktproben und Vorzeichen untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Punkt und Ebene: Aufgabenstellung zu einer Punktprobe auf einer Kante aus dem Lösungsweg formulieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Fehler finden (nur den Stützpunkt eingesetzt; die dritte Gleichung der Parameterprobe nicht geprüft; eine fehlende Variable in der Gleichung als Fehler gedeutet; nur eine der beiden Ebenen geprüft) → didaktischer Typ, kein Prüfungstyp
- 1.7 Begründen (warum das Erfülltsein der Gleichung die Lage entscheidet; warum gleiche Vorzeichen beim Einsetzen dieselbe Seite bedeuten) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Parameter aus der Lagebedingung** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen (7) → wortgleich; GK 0 · LK 2 (2022, 2026), Haupt 2 · FHR 0
- 2.2 Punkt und Ebene: Punkt der Ebene mit drei gleichen Koordinaten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Fehler finden (den falschen Punkt eingesetzt; einen Punkt gewählt, an dem der Parameter herausfällt; beide freien Werte null gesetzt; den Parameter aus einem einzelnen Koeffizienten geraten) → didaktischer Typ, kein Prüfungstyp
- 2.4 Begründen (warum ein Punkt der Ebene eine Gleichung für den Parameter liefert; warum die triviale Lösung keine Ebenengleichung ergibt) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Gerade und Ebene** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Gerade und Ebene: Lage einer Geradenschar zu einer Ebene mit Fallunterscheidung nach dem Parameter untersuchen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 3.2 Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen (4) → wortgleich; GK 1 (2021), Haupt 1 · LK 1 (2023), Haupt 1 · FHR 0
- 3.3 Gerade und Ebene: Kreisbahn einer Drehung um eine Kante als Kreis in einer Ebene mit Mittelpunkt begründen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 3.4 Gerade und Ebene: Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 3.5 Gerade und Ebene: Existenz unendlich vieler Ebenen ohne Punkt mit drei gleichen Koordinaten begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Punkt und Ebene: Parameterwerte für gemeinsame Punkte einer Pyramidenschar mit einer Ebene untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Fehler finden (nur den Stützpunkt geprüft und „liegt in der Ebene“ geschlossen; den Fall Parameter fällt heraus als „parallel“ abgeschlossen, ohne die Punktprobe zu führen; bei der Schar nur die Spitze geprüft und die Grundfläche vergessen) → didaktischer Typ, kein Prüfungstyp
- 3.8 Begründen (warum das Herausfallen des Parameters über enthalten oder parallel entscheidet; warum das Skalarprodukt mit dem Normalenvektor die drei Fälle trennt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Lagebefunde im Sachzusammenhang** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Gerade und Ebene: Berühren einer Geraden mit einem Netz über die Höhe des Durchstoßpunkts in der Netzebene untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.2 Gerade und Ebene: Schattenpunkt auf einer Wand als Schnitt von Lichtstrahl und Ebene untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Punkt und Ebene: Auftreffpunkt einer Bahnkurve auf der Grundebene berechnen und Lage innerhalb des Spielfelds prüfen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.4 Gerade und Ebene: Spurpunkt einer Lichtgeraden als Schatten auf der Wand aus einem Lösungsweg erläutern (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.5 Fehler finden (nur den Schnittpunkt berechnet und die Wandmaße nicht geprüft; nur die Zeit berechnet und die Lage nicht geprüft; den Schatten an der falschen Kante beginnen lassen; den zweiten Lösungsschritt falsch gedeutet) → didaktischer Typ, kein Prüfungstyp
- 4.6 Begründen (warum der Schatten der Durchstoßpunkt der Lichtgeraden ist; warum nach der Rechnung immer der Bereich zu prüfen bleibt) → didaktischer Typ, kein Prüfungstyp

### schnittmengen

**Einheit 1 · Schnittpunkt von Gerade und Ebene** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Schnittpunkt von Gerade und Ebene berechnen (6) → wortgleich; GK 2 (2018, 2023), Haupt 1 · LK 3 (2017, 2018, 2026), Haupt 2 · FHR 0
- 1.2 Schattenpunkt bei paralleler Projektion bestimmen (2) → wortgleich; GK 1 (2018), Haupt 0 · LK 0 · FHR 0
- 1.3 Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen (2) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 1.4 Durchstoßpunkt einer achsenparallelen Geraden mit einer Ebene berechnen und Abstand im Sachzusammenhang angeben (1) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 1.5 Zeit bis zum Erreichen einer Ebene aus dem Geradenparameter bestimmen (1) → wortgleich; GK 1 (2018), Haupt 1 · LK 0 · FHR 0
- 1.6 Rechenweg für den Schnittpunkt einer Geraden mit einer Ebene durch drei Punkte beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Fehler finden (beim Einsetzen den Aufpunkt vergessen und nur den Richtungsvektor eingesetzt; ein Vorzeichen beim Ausmultiplizieren verloren; die Ebene aufwendig aus drei Punkten bestimmt, wo der gemeinsame Koordinatenwert sie liefert; den Lotfußpunkt gesucht, wo der Durchstoßpunkt gefragt ist) → didaktischer Typ, kein Prüfungstyp
- 1.8 Begründen (warum das Einsetzen der Geradenkoordinaten eine Gleichung im Parameter liefert; warum bei einer Ebene z gleich Konstante nur die dritte Koordinate zählt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Schnittpunkt zweier Geraden** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Parameter aus dem Schnitt zweier Geraden ermitteln (3) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 2.2 Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen (2) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 2.3 Höhe des Endpunkts einer Strecke auf einer senkrechten Geraden über den Schnitt mit einer Kante berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Gegebene Rechnung zum Geradenschnittpunkt erläutern (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.5 Fehler finden (für beide Geraden denselben Parameterbuchstaben verwendet; die dritte Gleichung nicht geprüft; eine Lösung außerhalb der Kante nicht verworfen; die Terme der vorgelegten Rechnung nicht als Kantengeraden benannt) → didaktischer Typ, kein Prüfungstyp
- 2.6 Begründen (warum zwei Parameter zwei Gleichungen brauchen und die dritte die Probe ist; warum der Kantenparameter zwischen null und eins liegen muss) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Spuren, Schnittgeraden und Schnittfiguren** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 2 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Endpunkt der Schnittstrecke eines Vierecks mit einer achsenparallelen Ebene bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Halbierung eines Quadrats durch gegebene Ebenen entscheiden und begründen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.3 Lage zweier Ebenen über die Normalenvektoren entscheiden und Schnittgerade berechnen (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 3.4 Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen (3) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.5 Koordinate eines Punktes aus der Schnittfigur zeichnerisch ermitteln und Vorgehen beschreiben (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Schnittfigur einer Ebene mit einem Würfel einzeichnen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.7 Spurpunkte einer Ebene auf den Koordinatenachsen bestimmen (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 1 (2017), Haupt 0 · FHR 0
- 3.8 Fehler finden (die Spurgerade in der falschen Koordinatenebene gezeichnet; den Achsenpunkt auf falscher Höhe eingetragen; die Schnittfigur an den Ecken statt an den Kantenmitten enden lassen; die Koeffizienten statt der Achsenabschnitte als Spurpunkte angegeben; beide Koordinatengleichungen gleichgesetzt statt die Parameterform einzusetzen) → didaktischer Typ, kein Prüfungstyp
- 3.9 Begründen (warum parallele Flächen parallele Schnittkanten liefern; warum das Nullsetzen zweier Koordinaten den Achsenpunkt gibt) → didaktischer Typ, kein Prüfungstyp

### skalarprodukt-und-winkel

**Einheit 1 · Das Skalarprodukt als Objekt** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Parameter für einen Winkel von mindestens 90° über das Skalarprodukt ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Abhängigkeit eines Skalarprodukts nur von der Seitenlänge allgemein begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Art des Ergebnisses von Ausdrücken mit Skalarprodukt ankreuzen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Aussagen über Winkel zwischen Vektoren mit fester Komponentensumme beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Winkelart aus dem Vorzeichen des Skalarprodukts beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Fehler finden (einen Ausdruck aus Vektor plus Zahl als Vektor angekreuzt; aus einem negativen Skalarprodukt auf einen rechten oder kleinen Winkel geschlossen; beim Ungleichungslösen das Zeichen umgedreht oder nur den Randwert angegeben; mit Koordinaten gerechnet, wo keine gegeben sind) → didaktischer Typ, kein Prüfungstyp
- 1.7 Begründen (warum das Skalarprodukt eine Zahl ist; warum sein Vorzeichen die Winkelart trägt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Winkel zwischen Vektoren, Kanten und Geraden** – Abitur-Jahrgänge GK 4 von 9 (Haupt 3) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Winkel zwischen zwei Kanten über das Skalarprodukt berechnen (6) → wortgleich; GK 1 (2026), Haupt 1 · LK 2 (2018, 2026), Haupt 2 · FHR 0
- 2.2 Innenwinkel eines Vierecks über das Skalarprodukt der Seitenvektoren berechnen (2) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 2.3 Innenwinkel eines Dreiecks über gleiche Seitenlängen als gleichseitig bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Rechten Winkel zwischen zwei Seiten einer Figur über das Skalarprodukt nachweisen (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 2.5 Schnittwinkel zweier Geraden über das Skalarprodukt berechnen (1) → wortgleich; GK 1 (2018), Haupt 0 · LK 1 (2018), Haupt 0 · FHR 0
- 2.6 Fehler finden (die Vektoren nicht von derselben Ecke aus angesetzt; einen Vektor in Gegenrichtung genommen und den Nebenwinkel erhalten; den Betrag im Zähler weggelassen und den stumpfen Winkel angegeben; das falsche Eckenpaar auf den rechten Winkel geprüft) → didaktischer Typ, kein Prüfungstyp
- 2.7 Begründen (warum beide Vektoren vom Scheitel weg zeigen müssen; warum der Betrag im Zähler den spitzen Winkel liefert) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Neigungswinkel von Ebenen** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen (17) → wortgleich; GK 5 (2018, 2021, 2023, 2024, 2025), Haupt 5 · LK 3 (2017, 2023, 2025), Haupt 3 · FHR 0
- 3.2 Innenwinkel zwischen Dachebene und vertikaler Wand über den Neigungswinkel berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Winkel zwischen einer Seitenfläche und der Horizontalen als Grenzwinkel im Sachzusammenhang bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Neigung einer Ebene in Prozent über den Winkel zur Koordinatenebene prüfen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Fehler finden (den Sinus statt des Kosinus genommen; das Komplement – den Winkel zwischen Normalenvektor und Ebene – angegeben; den Nebenwinkel statt des Innenwinkels gelassen; einen Betrag falsch berechnet; die Neigung in Prozent mit dem Gradmaß gleichgesetzt) → didaktischer Typ, kein Prüfungstyp
- 3.6 Begründen (warum der Winkel der Normalenvektoren der Winkel der Ebenen ist; warum der Tangens die Neigung in Prozent liefert) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Winkel von Geraden gegen Ebenen und Bogenmaße** – Abitur-Jahrgänge GK 1 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen (3) → wortgleich; GK 1 (2019), Haupt 0 · LK 1 (2017), Haupt 1 · FHR 0
- 4.2 Länge eines Kreisbogens durch drei Punkte über den Winkel am Mittelpunkt berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Neigungswinkel einer Strecke gegen die Horizontale über ihre Projektion berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.4 Fehler finden (den Kosinus statt des Sinus genommen und den Winkel zur Normalen erhalten; den Winkel zur Vertikalen statt zur Horizontalen angegeben; den Radius falsch angesetzt) → didaktischer Typ, kein Prüfungstyp
- 4.5 Begründen (warum zur Ebene der Sinus gehört – der Winkel zur Normalen ist das Komplement; warum die Projektion denselben Winkel liefert) → didaktischer Typ, kein Prüfungstyp

### orthogonalitaet

**Einheit 1 · Rechte Winkel an Dreiecken nachweisen** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen (5) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2026), Haupt 1 · FHR 0
- 1.2 Dreieck: Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen (3) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 1.3 Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen (2) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 1.4 Dreieck: Rechten Winkel aus der Lage zu den Koordinatenachsen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Fehler finden (den rechten Winkel an der falschen Ecke geprüft; das Skalarprodukt nur für ein Zahlenbeispiel des Parameters gerechnet; nur eine Ecke geprüft und aus einem Wert ungleich null auf das ganze Dreieck geschlossen; einen Schenkelvektor von der falschen Ecke aus gebildet) → didaktischer Typ, kein Prüfungstyp
- 1.6 Begründen (warum die Schenkelvektoren vom Scheitel ausgehen müssen; warum ein identisch verschwindendes Skalarprodukt für alle Parameterwerte trägt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Rechte Winkel rückwärts** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln (4) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 2.2 Dreieck: Koordinate eines Punktes auf einer Kante für einen rechten Winkel über das Skalarprodukt berechnen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.3 Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen oder Oberflächeninhalt berechnen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Geraden und Ebenen: Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 2.5 Dreieck: Eckpunkt eines gleichschenklig-rechtwinkligen Dreiecks mit Kathete in einer Koordinatenebene ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.6 Dreieck: Punkte auf einer Koordinatenachse mit rechtem Winkel zu zwei Punkten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Dreieck: Teilverhältnis eines Punktes auf einer Strecke aus einem rechten Winkel ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Fehler finden (die Vektoren vom falschen Punkt aus angesetzt; eine Lösung außerhalb des Kantenbereichs nicht ausgeschlossen; die negative Höhe nicht verworfen; nur eine von zwei Lösungen angegeben; den Streckenparameter als Teilverhältnis ausgegeben; die Länge des konstruierten Vektors nicht angepasst) → didaktischer Typ, kein Prüfungstyp
- 2.9 Begründen (warum die Bedingung eine Gleichung liefert; warum quadratische Bedingungen zwei Kandidaten geben, die der Bereich siebt) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Senkrecht zu Geraden und Ebenen** – Abitur-Jahrgänge GK 4 von 9 (Haupt 3) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Geraden und Ebenen: Orthogonalität zweier Geraden über das Skalarprodukt untersuchen (3) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 3.2 Geraden und Ebenen: Parameter für die Orthogonalität zweier Ebenen bestimmen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.3 Geraden und Ebenen: Mittelsenkrechte einer Strecke parallel zu einer Koordinatenebene bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen (6) → wortgleich; GK 2 (2025, 2026), Haupt 0 · LK 2 (2022, 2026), Haupt 2 · FHR 0
- 3.5 Geraden und Ebenen: Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen (3) → wortgleich; GK 2 (2022, 2025), Haupt 2 · LK 0 · FHR 0
- 3.6 Geraden und Ebenen: Ebene senkrecht zu zwei gegebenen Ebenen angeben (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.7 Fehler finden (für die Gerade senkrecht zur Ebene ein Skalarprodukt null mit dem Normalenvektor erwartet statt der Kollinearität; nur einen Spannvektor geprüft; die Normalenvektoren gleichgesetzt statt orthogonal angesetzt; den Normalenvektor aus den Koeffizienten falsch zugeordnet, wenn eine Variable fehlt; eine parallele statt einer senkrechten Ebene angegeben; die Mittelsenkrechte als Ebene aufgestellt) → didaktischer Typ, kein Prüfungstyp
- 3.8 Begründen (warum die Gerade senkrecht zur Ebene die Richtung des Normalenvektors hat; warum zwei Skalarprodukte für den Normalenvektor der Parameterform genügen) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Lot und Extremum** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Dreieck: Parameter für den maximalen Spitzenwinkel eines gleichschenkligen Dreiecks über die minimale Höhe und die Orthogonalität zur Geraden ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.2 Dreieck: Gleichung für den Parameter des flächenkleinsten gleichschenkligen Dreiecks über die Orthogonalität von Höhe und Gerade begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Dreieck: Streckenverhältnis am Lot im Quadrat über ähnliche Dreiecke begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.4 Fehler finden (die Fläche über den Abstand zu einem Endpunkt statt über die Höhe angesetzt; das Maximum mit dem Rechner gesucht, ohne den Weg zu erläutern; mit Koordinaten gerechnet, wo keine gegeben sind) → didaktischer Typ, kein Prüfungstyp
- 4.5 Begründen (warum die kleinste Verbindung das Lot ist; warum der Spitzenwinkel wächst, wenn die Höhe schrumpft) → didaktischer Typ, kein Prüfungstyp

### abstaende

**Einheit 1 · Abstand zweier Punkte** – Abitur-Jahrgänge GK 4 von 9 (Haupt 3) · LK 3 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen (6) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2026), Haupt 1 · FHR 0
- 1.2 Streckenlänge im Raum berechnen (5) → wortgleich; GK 3 (2018, 2019, 2020), Haupt 2 · LK 2 (2017, 2018), Haupt 0 · FHR 0
- 1.3 Erreichbarkeit der Grundfläche über den größten Abstand zu einem Punkt beurteilen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Nächsten und fernsten Punkt des Deckflächenrands eines Zylinders zu einem Randpunkt der Grundfläche bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Sprungweite als Abstand zweier Punkte einer Parameterkurve in der Grundebene berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Existenz eines Kreispunkts mit vorgegebener Koordinate über den Radius widerlegen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 1.7 Untere Schranke für den Abstand zweier Punkte mit einer unbekannten Koordinate nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Fehler finden (Koordinaten addiert statt subtrahiert; die Hypotenuse mit einer Kathete gleichgesetzt; Basis und Schenkel verwechselt; nur eine von zwei Lösungen angegeben; den Zuschlag als Gesamtlänge genommen; beim Umrechnen durch den Faktor geteilt statt multipliziert; die Koordinate frei gelassen und die Aussage für wahr gehalten) → didaktischer Typ, kein Prüfungstyp
- 1.9 Begründen (warum die Betragsformel der Satz des Pythagoras im Raum ist; warum Quadrieren vor dem Wurzelziehen die Gleichung vereinfacht und nichts verliert, solange beide Seiten nicht negativ sind) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Abstand Punkt–Ebene** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 5 von 7 (Haupt 5) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen (6) → wortgleich; GK 1 (2025), Haupt 1 · LK 2 (2024, 2026), Haupt 2 · FHR 0
- 2.2 Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen (3) → wortgleich; GK 1 (2020), Haupt 1 · LK 2 (2017, 2022), Haupt 1 · FHR 0
- 2.3 Punkt auf einer Strecke mit vorgegebenem Abstand zu einer Ebene bestimmen (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.4 Lotgerade von einem Punkt auf eine Ebene angeben (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.5 Aufgabenstellung zum Abstand eines Punktes von einer Scharebene aus dem Lösungsweg formulieren (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.6 Fehler finden (den Normalenvektor nicht normiert; den vollen statt den halben Spiegelbild-Abstand abgetragen; die volle Kantenlänge statt der halben; die Betragsgleichung nur mit einem Vorzeichen gelöst; die Einheit nicht in Längeneinheiten umgerechnet; einen Richtungsvektor der Ebene statt des Normalenvektors für die Lotgerade genommen) → didaktischer Typ, kein Prüfungstyp
- 2.7 Begründen (warum das Normieren den Abstand liefert; warum die Rückrichtung immer zwei Lösungen hat und der Sachzusammenhang eine auswählt) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Lotfußpunkt** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Gerade in einer Ebene parallel zu einer Geraden mit kleinstem Abstand bestimmen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.2 Lotfußpunkt auf einer Geraden über das Skalarprodukt mit dem Richtungsvektor berechnen (2) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 3.3 Punkt auf einer Geraden mit vorgegebenem Abstand zu einer zweiten Geraden über eine Skizze und den Sinus berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Gleichen Abstand eines Punktes zu einer Geradenschar über den Lotfußpunkt beurteilen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 3.5 Lotfußpunkt aus Geradengleichung und Orthogonalitätsbedingung im Gleichungspaar deuten (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 3.6 Lösungsweg für den Lotfußpunkt eines Punktes auf einer Geraden beschreiben (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.7 Rechenweg für die kürzeste Linie über eine Kante aus Lotfußpunkt und Symmetrie erläutern (2) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.8 Abstand eines Punktes von einer Geraden über Lotgerade und Schnittpunkt aus einem Lösungsweg erläutern (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 3.9 Aufgabenstellung zu einer Drehung um eine Kante aus Lotfußpunkt und Rechenweg formulieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.10 Lösungsweg für einen Punkt mit gleichem Abstand zu drei Strecken über Lotfußpunkt und Abstandsgleichheit erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.11 Fehler finden (den Mittelpunkt statt des Lotfußpunkts genommen; die Orthogonalität zum falschen Vektor gefordert; den Lotfußpunkt auf die falsche Kante bezogen; irgendeine parallele Gerade ohne den Lotfußpunkt angegeben; den Lotfußpunkt nur innerhalb der Strecke gesucht, obwohl er außerhalb liegt; Abstände für einzelne Parameterwerte berechnet und verallgemeinert) → didaktischer Typ, kein Prüfungstyp
- 3.12 Begründen (warum das Gleichungspaar aus Geradengleichung und Skalarprodukt null immer einen Lotfußpunkt beschreibt; warum das Lot von P auf die Ebene senkrecht auf jeder Geraden durch den Lotfußpunkt in der Ebene steht) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Abstand als Argument** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Punkt mit gleichem Abstand zu allen Seitenflächen über die Symmetrieachse bestimmen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 4.2 Punkte mit gleichem Abstand zu drei Eckpunkten eines rechtwinkligen Dreiecks über den Thaleskreis ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Strecke in einer geneigten Ebene über einen Höhenschnitt bestimmen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 4.4 Abstand zweier Punkte auf parallelen Ebenen mit dem Abstand der Ebenen vergleichen (2) → wortgleich; GK 2 (2020, 2023), Haupt 2 · LK 0 · FHR 0
- 4.5 Verhältnis zweier Abstände über den Strahlensatz an der Pyramidenspitze begründen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.6 Abstand einer vertikalen Fläche zu einer Achse über den Mittelpunkt der Oberkante begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Abstand eines Punktes zu einer Ebene über eine Schrägstrecke nach oben abschätzen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.8 Horizontalen Abstand zweier Punkte als kürzer als ihre Verbindungsstrecke begründen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 4.9 Lotfußpunkt außerhalb einer Figur als Grund für größere Abstände aller Figurpunkte zeichnerisch begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Lösungsweg für den Punkt gleichen Abstands zu allen Seitenflächen einer Pyramide erläutern (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 4.11 Fehler finden (die schräge Strecke als Abstand genommen; den Abstand zweier Ebenenpunkte mit dem Ebenenabstand gleichgesetzt; mit gerechneten Werten statt mit einer Begründung geantwortet; den Lotfußpunkt rechnerisch bestimmt, wo zeichnerisch zu begründen war; den Abstand einer Ecke statt des Kantenmittelpunkts zur Achse genommen; die Vordachlänge waagerecht statt in der geneigten Ebene gemessen; die Abstandsgleichung als Abstand zur Spitze gedeutet; drei Abstandsgleichungen angesetzt statt den Thaleskreis zu sehen) → didaktischer Typ, kein Prüfungstyp
- 4.12 Begründen (warum das Lot die kürzeste Verbindung ist; warum die Symmetrieachse die Punkte gleichen Abstands trägt) → didaktischer Typ, kein Prüfungstyp

### spiegelung

**Einheit 1 · Punkte spiegeln** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Spiegelpunkt an einem Punkt bestimmen (2) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 1.2 Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 1.3 Spiegelpunkt an einer Ebene über die Lotgerade bestimmen (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 1.4 Punkt auf der Spiegelachse mit vorgegebenem Abstandsverhältnis zur Spiegelebene bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Koordinaten gespiegelter Eckpunkte aus den Symmetrieebenen eines Körpers angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Fehler finden (den Verbindungsvektor am Ausgangspunkt statt am Spiegelzentrum abgetragen; beim Lotfußpunkt stehen geblieben statt den Parameter zu verdoppeln; den Lotfußpunkt neu berechnet, obwohl er gegeben ist; in die falsche Richtung abgetragen und den Ausgangspunkt erhalten; an der falschen Symmetrieebene gespiegelt; das Verhältnis vom Punkt statt vom Mittelpunkt aus angesetzt) → didaktischer Typ, kein Prüfungstyp
- 1.7 Begründen (warum das Spiegeln an einer Koordinatenebene genau ein Vorzeichen wechselt; warum der doppelte Lotparameter den Spiegelpunkt liefert) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Spiegelebene und Spiegelgerade bestimmen** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Spiegelebene aus Punkt und Spiegelpunkt bestimmen (3) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 2.2 Spiegelebene zweier sich schneidender Geraden bestimmen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.3 Spiegelgerade einer Geraden an einer Ebene aus Fixpunkt und bekanntem Spiegelpunkt angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Spiegelgerade zweier Geraden zeichnen und Punkt der Winkelhalbierenden als Vektorterm angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Fehler finden (den Mittelpunkt nicht in die Ebenengleichung eingesetzt, sondern den Punkt selbst; die Summe der Richtungsvektoren als Richtung der Ebene statt als Normalenvektor genommen; die Spiegelgerade durch Punkt und Spiegelpunkt gelegt – das ist die Lotgerade; die Summe der Ortsvektoren als Winkelhalbierenden-Term angegeben, ohne die Vektoren gleich lang zu machen) → didaktischer Typ, kein Prüfungstyp
- 2.6 Begründen (warum der Verbindungsvektor von Punkt und Spiegelpunkt Normalenvektor der Spiegelebene ist; warum die Rautendiagonale den Winkel halbiert und die Richtungsvektoren dafür gleich lang sein müssen) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Symmetrieebenen von Körpern** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Symmetrieebenen eines Körpers aus den Koordinaten begründen (3; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Symmetrie zweier Punkte bezüglich einer Koordinatenachse über die Koordinaten begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Symmetrieebene eines geraden Prismas über die Symmetrieachse der Grundfläche begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Symmetrieebene eines zusammengesetzten Körpers über verschiedene Höhen der Teilkörper ausschließen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen (5) → wortgleich; GK 1 (2022), Haupt 1 · LK 1 (2024), Haupt 1 · FHR 0
- 3.6 Symmetrieebene eines Körpers angeben und ihre Schnittfigur mit dem Körper einzeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Fehler finden (die waagerechte Ebene durch die Giebelspitzen gewählt; eine Ebene für symmetrisch gehalten, weil die Spitze in ihr liegt; die Diagonalebene mit der falschen Vorzeichenbedingung verwechselt; beim Rechteck eine Diagonalebene angegeben; die Mitte geschätzt statt den Mittelwert der Koordinaten zu bilden; die Symmetrie zur falschen Ebene behauptet; nur einzelne Punktepaare gespiegelt statt allgemein zu begründen; nur einen Parameterwert geprüft) → didaktischer Typ, kein Prüfungstyp
- 3.8 Begründen (warum eine einzige Punktprobe zum Ausschließen genügt; warum beim geraden Prisma die Ebene durch die Symmetrieachse der Grundfläche senkrecht auf ihr stehen muss) → didaktischer Typ, kein Prüfungstyp

### scharen-von-geraden-und-ebenen

**Einheit 1 · Die Schar als Familie** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Zugehörigkeit einer Ebene zu einer Schar prüfen (3) → wortgleich; GK 0 · LK 2 (2022, 2024), Haupt 2 · FHR 0
- 1.2 Gemeinsamen Punkt aller Ebenen einer Schar nachweisen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.3 Nichtparallelität verschiedener Ebenen einer Schar über die Normalenvektoren nachweisen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 1.4 Schnittwinkel einer Geraden mit allen Ebenen einer Schar als parameterunabhängig nachweisen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.5 Windschiefe Lage einer Geraden zu einer Geradenschar nachweisen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 1.6 Gemeinsame Gerade aller Ebenen einer Schar aus der Abbildung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Ortsvektor und Richtungsvektor der Geraden durch die Punkte einer Punktschar nachweisen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Parallelität aller Geraden einer Schar begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.9 Spurpunkt einer Scharebene auf einer Koordinatenachse nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Identität aller Geraden einer Schar beurteilen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 1.11 Koordinatenebene senkrecht zu allen Ebenen einer Schar angeben (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 1.12 Fehler finden (nur zwei konkrete Parameterwerte geprüft; wegen verschiedener Stützvektoren auf verschiedene Geraden geschlossen; mit den Stützvektoren statt den Richtungsvektoren argumentiert; nur einen Punkt oder einen Endpunkt geprüft; nur die rechte Seite der Gleichungen verglichen; die falsche Koordinatenebene benannt, weil eine Variable fehlt) → didaktischer Typ, kein Prüfungstyp
- 1.13 Begründen (warum ein herausfallender Parameter die Aussage für alle Mitglieder liefert; warum zwei Beispiele keine Schar-Aussage tragen) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Parameter aus Lagebedingungen** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Scharparameter für Parallelität von Ebene und Gerade ermitteln (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.2 Existenz eines Scharparameters für eine Gerade in der Ebene untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Ganzzahligen Scharparameter aus einer Bereichsbedingung an den Durchstoßpunkt bestimmen (1) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 2.4 Koordinatengleichung einer Ebene aufstellen und Parameter eines Scharpunkts in der Ebene bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Parameter einer Geradenschar aus einem vorgegebenen Durchstoßpunkt bestimmen (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.6 Scharparameter für Orthogonalität von Gerade und Ebene bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Scharparameter, für den eine Kante in der Scharebene liegt, nachweisen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.8 Nachbarschaft zweier Quadratecken auf einer Geradenschar durch Fallunterscheidung ausschließen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Fehler finden (für die Parallelität den Stützpunkt der Geraden in die Ebenengleichung eingesetzt; für die Orthogonalität das Skalarprodukt null gesetzt statt der Kollinearität; nur die Richtung geprüft und den Stützpunkt vergessen; nur einen von zwei Fällen geprüft; das Vorzeichen des Parameters nicht geprüft und einen Punkt außerhalb des Bereichs angegeben) → didaktischer Typ, kein Prüfungstyp
- 2.10 Begründen (warum „parallel“ das Skalarprodukt null und „senkrecht“ die Kollinearität verlangt – dieselbe Paarregel wie bei festen Objekten; warum eine Kante in der Ebene liegt, wenn beide Endpunkte denselben Parameterwert liefern) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Parameter aus Maßbedingungen** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Scharparameter für den minimalen Flächeninhalt eines Schnittdreiecks über die Orthogonalität zur Kante ermitteln (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.2 Scharparameter für einen vorgegebenen Schnittwinkel zwischen Achse und Ebene ermitteln (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.3 Scharparameter für einen vorgegebenen Winkel zwischen Ebene und Scharebene berechnen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Scharparameter für einen vorgegebenen Abstand eines Punktes zur Scharebene bestimmen (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.5 Fehler finden (den Kosinus statt des Sinus für den Winkel Gerade–Ebene angesetzt; den Betrag weggelassen und eine Lösung verloren; die negative Lösung vergessen; beim Abstand nur eine Seite angegeben; den Flächeninhalt als Funktion aufgestellt und abgeleitet statt die Lotbedingung zu nutzen) → didaktischer Typ, kein Prüfungstyp
- 3.6 Begründen (warum Betragsgleichungen zwei Lösungen liefern; warum die kleinste Höhe die Lotbedingung ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Scharen am Körper** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Geradenschar der Schnittgeraden einer Ebenenschar mit einer Koordinatenebene bestimmen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.2 Parameterbereich, in dem eine Ebenenschar dieselben Kanten eines Körpers schneidet, bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Punkte einer Geraden, für die eine Ebene durch eine Achse vier vorgegebene Kanten eines Körpers schneidet, ermitteln (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.4 Weiteren Eckpunkt des Schnittdreiecks einer Scharebene mit einem Körper ermitteln (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.5 Kleinsten Parameterwert, ab dem eine Ebenenschar einen Körper nicht mehr trifft, begründen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 4.6 Mögliche Lage des Achsendreiecks einer Ebenenschar über die Vorzeichen der Achsenabschnitte entscheiden und den Parameterbereich bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben (4) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.8 Lotfußpunkte vom Ursprung auf Spurgeraden von Scharebenen einzeichnen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 4.9 Scharebene für einen Parameterwert angeben und Schnittfigur mit der Pyramide einzeichnen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 4.10 Fehler finden (einen Übergangswert übersehen; den Sonderfall ausgelassen, in dem die Ebene die Grundfläche enthält und keine Schnittfigur liefert; Randfälle nicht geprüft; den falschen Bereich für den größten gehalten oder senkrechte Kanten mitgezählt; den größten Koordinatenwert statt des Ebenenwerts genommen; eine Kante ohne Schnittpunkt gewählt; den Scharpunkt auf der falschen Kante gesucht; die Lotfußpunkte auf die Ecken gelegt; die Koordinatenebene mit der falschen Gleichung eingesetzt und den Scharparameter im Ergebnis mitgeführt; die Ungleichung ohne Vorzeichenfall mit dem Parameter multipliziert) → didaktischer Typ, kein Prüfungstyp
- 4.11 Begründen (warum die Schnittfigur zwischen zwei Übergangswerten ihre Gestalt behält; warum jenseits des größten Ebenenwerts über den Ecken der Körper ganz auf einer Seite liegt) → didaktischer Typ, kein Prüfungstyp

### flaecheninhalt-und-volumen-im-raum

**Einheit 1 · Dreiecksflächen** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen (5) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 1.2 Ebene Figur: Parameter einer Ecke aus dem Flächeninhalt eines gleichschenkligen Dreiecks bestimmen (3) → wortgleich; GK 2 (2020, 2022), Haupt 2 · LK 0 · FHR 0
- 1.3 Ebene Figur: Flächeninhalt eines Dreiecks aus den Spurpunkten einer Ebene berechnen (2) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 1.4 Ebene Figur: Flächenverhältnis von Dreieck und Trapez über einen Vektorterm ermitteln (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 1.5 Ebene Figur: Parameter eines Punktes aus einer Flächengleichheit bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Ebene Figur: Schattendreieck in der Grundebene zeichnen und seinen Flächeninhalt berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Ebene Figur: Flächengleichheit zweier Dreiecke mit gemeinsamer Seite über gleiche Höhen an einer Skizze begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Ebene Figur: Flächeninhalt eines rechtwinkligen Dreiecks über die Kathetenlängen nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.9 Ebene Figur: Kongruenz aller Dreiecke aus Raumdiagonale, Flächendiagonale und Kante begründen und Flächeninhalt berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Ebene Figur: Flächenterm eines Dreiecks als Quadrat minus Randdreiecke in der Abbildung veranschaulichen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 1.11 Fehler finden (eine Schenkellänge oder einen Ortsvektorbetrag als Höhe genommen; die Spitze über eine Ecke statt über die Basismitte gesetzt; negative Achsenabschnitte als negative Längen eingesetzt; die Hypotenuse als Kathete genommen; eine Höhe angesetzt, die nicht senkrecht steht; den Zielpunkt am falschen Ende abgetragen; das Dreieck selbst statt der Restdreiecke beschriftet) → didaktischer Typ, kein Prüfungstyp
- 1.12 Begründen (warum die Höhe des gleichschenkligen Dreiecks durch die Basismitte geht; warum Dreiecke mit gemeinsamer Seite und gleichen Höhen flächengleich sind) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Vierecksflächen** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Ebene Figur: Flächeninhalt eines Trapezes im Raum über die Höhe zwischen den parallelen Seiten berechnen (2) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 2.2 Ebene Figur: Innenwinkel einer Raute und Gesamtfläche der Dachflächen berechnen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 2.3 Ebene Figur: Diagonalenschnittpunkt und Flächeninhalt eines Quadrats aus dem Spurpunkt einer Geraden bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Ebene Figur: Eckpunkte eines gleichschenkligen Trapezes aus einem Flächenverhältnis zum Quadrat bestimmen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 2.5 Ebene Figur: Flächeninhalt eines Rechtecks aus Kantenlängen berechnen und rechten Winkel zweier Flächen prüfen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.6 Ebene Figur: Flächeninhalt eines ebenen Vierecks mit zwei parallelen senkrechten Seiten aus Seitenlänge und Pfahlabstand berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Ebene Figur: Parameter aus Seitenlänge und Flächeninhalt eines Rechtecks bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Ebene Figur: Teilverhältnis auf einer Kante deuten und Teilfläche eines Rechtecks berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Ebene Figur: Trapezfläche zwischen einer geneigten Ebene und einer waagerechten Ebene in einem Quader berechnen (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 2.10 Ebene Figur: Zuschauerzahl aus dem Flächeninhalt eines Trapezes im Raum und dem Platzbedarf berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.11 Ebene Figur: Flächenformel einer Raute als halbes Diagonalenprodukt mit einer Skizze begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.12 Ebene Figur: Flächenverhältnis zweier Quadrate aus den Seitenlängen nachweisen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 2.13 Ebene Figur: Flächenterm eines Vierecks als Rechteck plus rechtwinkliges Dreieck erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.14 Fehler finden (eine Schenkellänge als Trapezhöhe genommen; die Rautenfläche als Seite mal Seite gerechnet; den halben Diagonalenabstand als Seitenlänge genommen; die Verschiebung nur auf einer Seite angesetzt; die Schnittgerade in der falschen Höhe bestimmt; das Netz mit der Seillänge statt dem Pfahlabstand gerechnet; die Formel nur zitiert statt am Rechteck zu begründen; nur eine Lösung der Wurzelgleichung ohne Begründung angegeben; den falschen Anteil der Fläche genommen) → didaktischer Typ, kein Prüfungstyp
- 2.15 Begründen (warum die Trapezhöhe senkrecht zwischen den parallelen Seiten gemessen wird; warum das halbe Diagonalenprodukt am umschließenden Rechteck sichtbar wird) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Volumen und Oberfläche von Pyramide und Prisma: Grundfläche mal Höhe, bei der Pyramide der Faktor ein Drittel; die Höhe als Abstand der Spitze zur Grundflächenebene (waagerechte Grundfläche: z-Differenz; senkrechte Kante über Skalarprodukte erkennen); die Grundfläche aus den Kästen eins und zwei (Drachen, Trapez, Raute, rechtwinkliges Dreieck); Oberflächen (Seitenhöhe über Pythagoras** – Abitur-Jahrgänge GK 4 von 9 (Haupt 3) · LK 5 von 7 (Haupt 5) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Körper: Kürzeste und längste Kante und Volumen einer Pyramide über einem Drachenviereck berechnen (4) → wortgleich; GK 1 (2025), Haupt 1 · LK 1 (2025), Haupt 1 · FHR 0
- 3.2 Körper: Höhe einer Pyramide aus dem Volumen bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen (2) → wortgleich; GK 1 (2021), Haupt 0 · LK 1 (2024), Haupt 1 · FHR 0
- 3.4 Körper: Pyramidenvolumen aus Grundfläche und Höhe berechnen (2) → wortgleich; GK 1 (2020), Haupt 1 · LK 1 (2018), Haupt 1 · FHR 0
- 3.5 Körper: Volumen aus Prisma und aufgesetzter Pyramide berechnen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 3.6 Körper: Höhe eines Prismas aus dem Mantelflächeninhalt bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Körper: Oberflächeninhalt eines Prismas über einem rechtwinkligen Dreieck berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Körper: Rechteck als Quadrat ausschließen und Volumen einer Pyramide über dem Rechteck berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.9 Körper: Volumen einer Pyramide über einem rechtwinkligen Dreieck mit Pythagoras berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.10 Körper: Volumen eines Hauses als Quader plus Dachprisma mit Trapezquerschnitt berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.11 Körper: Volumen eines Prismas mit Trapezquerschnitt im Sachzusammenhang berechnen und mit einer Vorgabe vergleichen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Körper: Volumen eines Prismas über einer Raute berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.13 Körper: Trapezgrundfläche nachweisen und Pyramidenvolumen berechnen (3) → wortgleich; GK 1 (2024), Haupt 1 · LK 1 (2026), Haupt 1 · FHR 0
- 3.14 Körper: Volumen eines geraden Prismas über einem Dreieck nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.15 Fehler finden (den Faktor ein Drittel der Pyramide vergessen oder ihn fälschlich beim Prisma gesetzt; die Drachen- oder Rautenfläche ohne den Faktor ein Halb; die Kantenlänge statt der Seitenhöhe für die Oberfläche; die Grundfläche als Rechteck statt als Dreieck; die Hypotenuse als Kathete; Mantelrechtecke oder Grundflächen vergessen; das Dachprisma als Dreiecksprisma angesetzt; die Prismenhöhe mit der Gebäudehöhe verwechselt) → didaktischer Typ, kein Prüfungstyp
- 3.16 Begründen (warum die Pyramide ein Drittel des Prismas über derselben Grundfläche füllt – Cavalieri und Zerlegung; warum die senkrechte Kante die Höhe ist, wenn zwei Skalarprodukte null sind) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Zusammengesetzte Körper, Verhältnisse und Parameter: Zerlegen und Ergänzen (Differenz zweier Pyramiden am abgeschnittenen Quader, Quader plus Dachprisma, Prisma plus Pyramide, vorgelegte Volumenterme Faktor für Faktor deuten), Volumenverhältnisse ohne Zahlenwerte (Formeln dividieren, Anteile am Quader begründen), Ähnlichkeit (der parallele Schnitt trennt eine ähnliche Teilpyramide ab** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Körper: Volumen eines Teilkörpers als Differenz zweier Pyramiden berechnen und erläutern (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.2 Körper: Volumen eines Teilkörpers eines Würfels berechnen (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 4.3 Körper: Volumenverhältnis zweier Körper über Formeln ohne Zahlenwerte ermitteln (2) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 4.4 Körper: Ebene parallel zu einer Koordinatenebene zur Halbierung eines Pyramidenvolumens über die Ähnlichkeit bestimmen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.5 Körper: Oberflächeninhalt des Rotationskegels eines rechtwinkligen Dreiecks berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.6 Körper: Parameter für das größte Volumen einer Pyramide bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Körper: Parameter für einen Volumenanteil zweier gegenläufiger Pyramiden im Quader bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.8 Körper: Passung eines Zylinders in ein Gefäß über die Höhe aus dem Volumen prüfen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.9 Körper: Volumen zweier Pyramiden vergleichen und prozentualen Mehrwert berechnen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 4.10 Körper: Volumenanteil einer Pyramide am Quader ohne Volumenberechnung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.11 Körper: Volumenterm eines Dachs als Pyramide minus Eckpyramiden begründen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 4.12 Körper: Rotationskörper einer Scharfläche als halben Kegel beschreiben und Volumen bestimmen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 4.13 Körper: Füllvolumen eines gedrehten Behälters am Graphen ergänzen und Grenzwinkel deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.14 Körper: Volumenansatz als Differenz zweier Pyramiden erläutern und Parameter bestimmen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 4.15 Körper: Volumenrechnung eines Prismas aus einem Lösungsweg erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.16 Körper: Volumenverlauf eines Restkörpers in Abhängigkeit vom Parameter als linear begründen und Graphen zuordnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.17 Fehler finden (den über den Quader hinausragenden Teil nicht abgezogen; den Restkörper direkt statt als Differenz angesetzt; den Teilkörper für den halben Würfel gehalten; das Verhältnis linear statt kubisch angesetzt; mit Zahlen gerechnet, wo allgemein verlangt war; den ganzen statt des halben Kegels angegeben; das Volumen für einzelne Parameterwerte ausprobiert statt den Term zu untersuchen; die Einheiten falsch umgerechnet; die Zahlen eines vorgelegten Terms falsch zugeordnet) → didaktischer Typ, kein Prüfungstyp
- 4.18 Begründen (warum beim parallelen Schnitt das Volumenverhältnis der Kubus des Streckfaktors ist; warum der Volumenverlauf linear ist, wenn nur eine Höhe linear vom Parameter abhängt) → didaktischer Typ, kein Prüfungstyp

### matrizen-und-uebergangsprozesse

**Einheit 1 · Matrizen als Rechenobjekte** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Matrizenalgebra: Matrix-Vektor-Produkt berechnen (4) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Matrizenalgebra: Inverse Matrix über A · B = E bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Matrizenalgebra: Einträge einer Faktormatrix aus dem Produkt mit einer bekannten Matrix bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Matrizenalgebra: Faktor aus M² als Vielfachem der Einheitsmatrix ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Matrizenalgebra: Fehlende Einträge einer Matrixpotenz über Zeile mal Spalte und Spaltensumme berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Matrizenalgebra: Ganzzahlige Einträge einer Matrix aus ihrem Quadrat bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Matrizenalgebra: Parameter aus der Gültigkeit der binomischen Formel für zwei Matrizen bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.9 Matrizenalgebra: Parameter für gleiche Spur von Matrix und Inverser bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Matrizenalgebra: Quadrat einer Matrix mit Parameter berechnen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.11 Matrizenalgebra: Hohe Potenz einer Vertauschungsmatrix über das Quadrat gleich Einheitsmatrix bestimmen (1; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.12 Matrizenalgebra: Quadrat einer Summe zweier Matrizen mit C · D = −D · C vereinfachen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.13 Matrizenalgebra: Aufbau von Vertauschungsmatrizen mit vorgegebener Wirkung beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.14 Matrizenalgebra: Inverse einer Vertauschungsmatrix angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.15 Matrizenalgebra: Mögliche Formate einer Matrix aus der Bildbarkeit eines Produkts beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.16 Matrizenalgebra: Wirkung einer Permutationsmatrix beschreiben und Einträge aus M · A · M = A bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.17 Fehler finden (elementweise quadriert; Zeile mit Zeile multipliziert; die binomische Formel für Matrizen als allgemeingültig angesehen; die Inverse als Kehrwert-Matrix oder die Spur der Inversen als Kehrwert der Spur angesetzt; nur die Zeilen statt Zeilen und Spalten umsortiert; das Format nur ausgeschlossen statt beschrieben) → didaktischer Typ, kein Prüfungstyp
- 1.18 Begründen (warum A · B und B · A verschieden sein können; warum M² = E hohe Potenzen auf M oder E zurückführt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Vektoren unter Matrizen** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen (4) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.2 Matrizenalgebra: Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Matrizenalgebra: Abbildungsmatrix aus einer geometrischen Bedingung an den Bildpunkt bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Matrizenalgebra: Alle Vektoren mit M · v = t · v durch Fallunterscheidung bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Matrizenalgebra: Gleichung mit inverser Matrix über die Eigenvektorbeziehung lösen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.6 Matrizenalgebra: Kollinearität von M · x − x mit einem Vektor untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Matrizenalgebra: Parameter einer Matrix aus der Orthogonalität von v und M · v bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Matrizenalgebra: Parameter einer Matrix aus einer Matrix-Vektor-Gleichung untersuchen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Matrizenalgebra: Parameterbereich für endliche Grenzwerte der Matrixpotenzen über eine Potenzfolge bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Matrizenalgebra: Erhalt der Spaltensumme unter einer stochastischen Matrix allgemein nachweisen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.11 Matrizenalgebra: Bedingung für eine selbstinverse Matrix mit Parametern herleiten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.12 Matrizenalgebra: Existenz mehrerer Lösungen von M · a = 0 begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.13 Matrizenalgebra: Konstanten Faktor der Komponentensumme von Q · u über die Spaltensummen nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.14 Matrizenalgebra: Orthogonalität einer Matrix über das Produkt mit der Transponierten nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.15 Matrizenalgebra: Unlösbarkeit einer Matrix-Vektor-Gleichung über eine Nullzeile begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.16 Matrizenalgebra: Abbildungsmatrix als Spiegelung an einer Koordinatenachse deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.17 Matrizenalgebra: Existenz von Matrizen mit vorgegebener Eigenschaft über ein Gleichungssystem beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.18 Matrizenalgebra: Matrix mit vorgegebener Eigenschaft angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.19 Fehler finden (nur eine Lösung oder nur den Nullvektor gefunden; die Fallunterscheidung nach der Nullkomponente ausgelassen; die überzählige Gleichung nicht geprüft oder als Widerspruch gelesen; mit einer Zahlenmatrix statt allgemein gerechnet; die Spaltensummen nicht eingesetzt; nur eine Vorzeichenlösung genommen) → didaktischer Typ, kein Prüfungstyp
- 2.20 Begründen (warum die Lösungen von M · v = t · v Vielfache bilden; warum die überzählige Gleichung die Probe ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Verflechtung** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix berechnen (4) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Verflechtung: Maximale Kostensteigerung eines Rohstoffs aus einer Kostenschranke bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Verflechtung: Maximale Produktionsmenge aus dem Rohstoffvorrat ermitteln (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Verflechtung: Produktionsmengen aus dem Rohstoffverbrauch über ein Gleichungssystem ermitteln (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Verflechtung: Rohstoffmenge aus den übrigen Rohstoffen über die Gesamtmatrix bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Verflechtung: Bedarf eines neuen Endprodukts an Zwischenprodukten aus der Produktgleichung der Matrizen ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Verflechtung: Höchstmenge aus einer Kostenschranke bei festem Mengenverhältnis ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Verflechtung: Matrixeintrag aus Mengenbedingungen ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.9 Verflechtung: Produktionsmenge aus einer Anteilsbedingung an den Rohstoffverbrauch bei festem Lagerverbrauch ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.10 Verflechtung: Unbekannte Bedarfe im Diagramm aus der Gesamtmatrix bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.11 Verflechtung: Verflechtungsmatrix aus Sachbedingungen und Matrixprodukt bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Verflechtung: Eintrag der Gesamtmatrix aus dem Diagramm bestätigen und Nulleintrag begründen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.13 Verflechtung: Format der Bedarfsmatrix aus der Anzahl der Stufenprodukte begründen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.14 Verflechtung: Gesamtmatrix im Sachzusammenhang deuten (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.15 Verflechtung: Fehlenden Eintrag des Diagramms aus der Bedarfsmatrix angeben und deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.16 Verflechtung: Kostengleichung mit Zeilenvektor, Matrix und Auftragsvektor erläutern und lösen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.17 Verflechtung: Matrix-Vektor-Gleichung mit konkreten Zahlen im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.18 Verflechtung: Nichtinvertierbarkeit der Gesamtmatrix im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.19 Verflechtung: Rohstoffbedarf in Abhängigkeit von einem Matrixparameter als Gerade darstellen und erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.20 Verflechtung: Verflechtungsdiagramm zu einer Matrix zeichnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.21 Verflechtung: Verflechtungsmatrix aus dem Diagramm angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.22 Fehler finden (mit der falschen Stufenmatrix oder mit einer Stufe allein gerechnet; einen Pfad mitgezählt, der nicht existiert; das Mengenverhältnis umgekehrt; den ersten statt des knappsten Rohstoffs genommen; den Preisanstieg linear statt exponentiell angesetzt; den Zeilenvektor als Mengen statt als Stückkosten gedeutet) → didaktischer Typ, kein Prüfungstyp
- 3.23 Begründen (warum die Gesamtmatrix das Produkt der Stufenmatrizen ist; warum ein Nulleintrag „kein Pfad“ heißt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Übergangsmodell** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Übergangsprozess: Spanne einer Komponente nach einem Schritt bei teilweise bekannter Verteilung ermitteln (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.2 Übergangsprozess: Verteilung nach einem Übergang berechnen und einen Anteil angeben (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.3 Übergangsprozess: Anteil nach zwei Übergängen aus dem Diagramm berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.4 Übergangsprozess: Bereich eines Anteils in Abhängigkeit vom Matrixparameter über die Randwerte ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.5 Übergangsprozess: Eintrag von M² berechnen und Zeile von M² im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.6 Übergangsprozess: Größtmögliche Anzahl im Vorquartal über die inverse Matrix und Nichtnegativität bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Übergangsprozess: Matrixeintrag aus einer Potenz der inversen Matrix bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.8 Übergangsprozess: Matrixparameter aus einer Komponente nach einem Schritt bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.9 Übergangsprozess: Matrixparameter aus einer Komponente nach zwei Schritten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Übergangsprozess: Mögliche Übergangsmatrix aus Ausgabe- und Rückgabezahlen zweier Stationen mit freiem Parameter ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.11 Übergangsprozess: Quadrat der Übergangsmatrix aus dem Diagramm berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.12 Übergangsprozess: Quadrat der Übergangsmatrix berechnen und M² · v als Zustand nach zwei Schritten deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.13 Übergangsprozess: Unbekannte Anzahl aus einer Bedingung an den Folgezustand berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.14 Übergangsprozess: Unbekannte Komponente der Ausgangsverteilung aus dem Ergebnisvektor über ein Gleichungssystem ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.15 Übergangsprozess: Verhältnis der Anfangsbestände aus einer Gleichverteilung nach einem Übergang bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.16 Übergangsprozess: Vorherige Verteilung über die inverse Matrix berechnen und prozentuale Abnahme einer Komponente angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.17 Übergangsprozess: Zustände nach einem und zwei Schritten aus einem Anfangszustand berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.18 Übergangsprozess: Fehler in einem Übergangsdiagramm gegen die Matrix begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.19 Übergangsprozess: Gleichung aus gleichen Komponentensummen von Ausgabe- und Rückgabevektor nachweisen und deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.20 Übergangsprozess: Unmöglichkeit einer Verteilung über eine negative Vorgängerkomponente begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.21 Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen (9) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.22 Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten (5) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.23 Übergangsprozess: Term mit Matrixpotenz und Zugang im Sachzusammenhang auswählen und deuten (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.24 Übergangsprozess: Aussage über eine Komponente nach einem Übergang bei gleicher Ausgangsverteilung beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.25 Übergangsprozess: Aussage über eine gleichbleibende Komponente aus einer Matrixzeile beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.26 Übergangsprozess: Aussagen über Anteile nach zwei Übergängen mit M² beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.27 Übergangsprozess: Diagramm der zeitlichen Entwicklung eines Zustands aus dem Übergangsdiagramm auswählen und begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.28 Übergangsprozess: Geänderte Übergangsmatrix aus zwei Vorschlägen nach dem beschriebenen Wechselverhalten auswählen und begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.29 Übergangsprozess: Gleichungssystem für die Verteilung vor einem Übergang aufstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.30 Übergangsprozess: Komponentensumme eines Produkts mit der diagonalfreien Matrix als Wechslerzahl deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.31 Übergangsprozess: Matrix bei geänderter Reihenfolge der Zustände angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.32 Übergangsprozess: Matrixeintrag und Spaltensumme eins im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.33 Übergangsprozess: Potenz der Übergangsmatrix als mehrschrittigen Übergang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.34 Übergangsprozess: Rückrechnung eines Verteilungsvektors über die Inverse von M² beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.35 Übergangsprozess: Spielregel zu den Übergangswahrscheinlichkeiten eines Feldes angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.36 Übergangsprozess: Term für die Verteilung mit zwischenzeitlichem Abgang über Diagonalmatrix und Matrixpotenzen angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.37 Übergangsprozess: Zeile der Übergangsmatrix aus dem Diagramm angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.38 Übergangsprozess: Zustand mit dem kleinsten Wechselanteil aus der Matrix ablesen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.39 Übergangsprozess: Übergangsdiagramm zur Matrix auswählen und fehlende Werte angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.40 Übergangsprozess: Übergangsgleichung mit Matrix aus dem Diagramm aufstellen und Variablen deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.41 Übergangsprozess: Übergangsmatrix aus dem Diagramm unter zwei Darstellungen auswählen und ergänzen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.42 Übergangsprozess: Übergangsmatrix aus dem Übergangsdiagramm aufstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.43 Fehler finden (Zeilen und Spalten vertauscht – das Kernfehlmuster des Themas; die Pfeilrichtung nach Zeilen statt Spalten; die Zugänge einer Zeile mit den Abgängen einer Spalte verwechselt; die Schrittzahl falsch gezählt oder den Zugang an die falsche Stelle des Terms gesetzt; vorwärts statt rückwärts gerechnet; die Summenbedingung der Gesamtheit vergessen) → didaktischer Typ, kein Prüfungstyp
- 4.44 Begründen (warum die Spalten die Ausgangszustände tragen und die Spaltensumme eins die Erhaltung; warum M² der Übergang über zwei Schritte ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Stationär und langfristig** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 5.1 Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen (3) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.2 Übergangsprozess: Stationäre Verteilung mit vorgegebener Gesamtzahl berechnen und einen Anteil beurteilen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.3 Übergangsprozess: Zeitpunkt für das Unterschreiten eines Anteils der Populationsgröße über einen konstanten Faktor bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.4 Übergangsprozess: Anteil zu entfernender Individuen für einen stationären Zustand berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.5 Übergangsprozess: Kleinsten Zeitpunkt für das Unterschreiten eines Anteils aus dem Matrixterm bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.6 Übergangsprozess: Parameter einer Übergangsmatrix aus einer Zykluslänge bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.7 Übergangsprozess: Wechselzahlen nach einem Übergang berechnen und Gleichgewicht deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.8 Übergangsprozess: Exponentielles Wachstum aus einem Eigenvektor begründen und Kurve zuordnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.9 Übergangsprozess: Konstante prozentuale Abnahme einer Gruppe ohne Zugänge aus der Matrix begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.10 Übergangsprozess: Monotone Entwicklung der Anteile aus der Übergangstabelle begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.11 Übergangsprozess: Unmöglichkeit eines konstanten Zustands über eine negative Lösung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.12 Übergangsprozess: Einträge der Grenzmatrix im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.13 Übergangsprozess: Entwicklung einer Population aus einer Potenz der inversen Matrix beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.14 Übergangsprozess: Langfristige Entwicklung aus M³ als Vielfachem der Einheitsmatrix durch Fallunterscheidung beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.15 Übergangsprozess: Langfristige Verteilung aus dem Übergangsdiagramm beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.16 Übergangsprozess: Potenz der Übergangsmatrix gleich Einheitsmatrix als Zyklus deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.17 Übergangsprozess: Stationäre Verteilung bei absorbierendem Zustand angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.18 Übergangsprozess: Übergangsverhalten einer parametrisierten Matrix nach Fällen im Sachzusammenhang beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.19 Fehler finden (den Fixvektor nur bis auf Vielfache bestimmt und die Gesamtzahl vergessen; alle drei Gleichungen aufgestellt und sich verloren; eine stationäre Verteilung mit lauter positiven Anteilen vermutet, obwohl ein Zustand absorbiert; den Zeitpunkt nicht aufgerundet oder um eins verfehlt; den Faktor rückwärts als Faktor vorwärts gelesen; nur den Faktor genannt, ohne die Fälle zu unterscheiden) → didaktischer Typ, kein Prüfungstyp
- 5.20 Begründen (warum die Gesamtzahl eine Gleichung des Fixvektorsystems ersetzt; warum ein konstanter Faktor je Schritt eine Exponentialentwicklung liefert) → didaktischer Typ, kein Prüfungstyp

### vierfeldertafel

**Einheit 1 · Die Tafel füllen: Aufbau (zwei Merkmale mit Gegenereignissen, vier Felder, Ränder, Summe eins bzw. Gesamtzahl), Füllregeln (Ränder zuerst, Felder als Differenzen der Ränder), der Kernschritt bei bedingten Angaben („Anteil innerhalb einer Gruppe“ ist bedingt** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Vierfeldertafel aus Anteilen vervollständigen (19) → wortgleich; GK 4 (2018, 2022, 2023, 2024), Haupt 4 · LK 2 (2017, 2018), Haupt 2 · FHR 0
- 1.2 Tabelle mit drei Spalten analog zur Vierfeldertafel aus Anteilen vervollständigen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Vierfeldertafel mit absoluten Häufigkeiten aus Gruppengrößen und bedingten Anteilen vervollständigen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Vierfeldertafel mit Parameter vervollständigen und einen Parameterwert ausschließen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Fehler finden (einen bedingten Anteil unmittelbar als Feld eingetragen, ohne mit dem Rand zu multiplizieren – das Kernfehlmuster des Themas; „weder–noch“ als Randwert gelesen; „entweder–oder“ als Vereinigung gelesen; einen Schnitt als Produkt der Ränder angesetzt und damit Unabhängigkeit unterstellt; einen Prozentwert auf die falsche Gesamtheit bezogen) → didaktischer Typ, kein Prüfungstyp
- 1.6 Begründen (warum ein Anteil „innerhalb einer Gruppe“ bedingt ist und erst die Multiplikation mit dem Rand das Feld liefert; warum die Felder einer Zeile sich zum Rand summieren) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Aus der Tafel rechnen: die Vereinigung „A oder B“ als eins minus Gegenfeld (oder über den Additionssatz), das ausschließende Entweder-oder als Summe der beiden gemischten Felder, fehlende absolute Häufigkeiten durch Subtraktion, Anteile aus Anteilen und bedingten Anteilen kombinieren. (Q2, GK-Kern; OHiMi 2.4 „Additionssatz“) ← Eingabe „a oder b tafel“, „entweder oder“, „vereinigung tafel“** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen (2) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 2.2 Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen (2) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 2.3 Anteil aus Anteilen und bedingten Anteilen über die Vierfeldertafel berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Fehler finden (die Ränder addiert, ohne den Schnitt abzuziehen; das einschließende statt des ausschließenden Oder gerechnet; die falsche Teilgruppe subtrahiert) → didaktischer Typ, kein Prüfungstyp
- 2.6 Begründen (warum „A oder B“ das Gegenfeld von „weder A noch B“ ist; warum das ausschließende Oder genau zwei Felder summiert) → didaktischer Typ, kein Prüfungstyp

### bedingte-wahrscheinlichkeit-und-bayes

**Einheit 1 · Der Quotient** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 2 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen (12) → wortgleich; GK 3 (2018, 2022, 2023), Haupt 3 · LK 2 (2017, 2018), Haupt 1 · FHR 0
- 1.2 Bedingte Anteile aus der Vierfeldertafel vergleichen (3) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Bedingte Wahrscheinlichkeit aus der Vierfeldertafel mit absoluten Häufigkeiten angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Fehler finden (die Bedingung vertauscht – durch den falschen Rand geteilt, das Kernfehlmuster des Themas; den Quotienten auf die Gesamtheit statt auf die Bedingungsgruppe bezogen; Schnittanteile direkt verglichen statt bedingte Anteile; absolute statt bedingte Anteile verglichen) → didaktischer Typ, kein Prüfungstyp
- 1.5 Begründen (warum der Nenner der Anteil der Bedingung ist; warum bedingte Anteile vergleichbar machen, was Schnittanteile nicht leisten) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Bayes** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen (8) → wortgleich; GK 1 (2020), Haupt 1 · LK 2 (2022, 2024), Haupt 2 · FHR 0
- 2.2 Bedingte Wahrscheinlichkeit aus dem Baumdiagramm mit einer Schranke vergleichen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Bayes-Term für drei Behälter nachweisen und Kugelzahl bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Bayes-Term im Sachzusammenhang deuten (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Fehler finden (die Richtung der Bedingung umgekehrt – P(B ¦ A) statt P(A ¦ B) angegeben, obwohl der Baum die erste Richtung liefert; den Nenner nur aus einem Ast gebildet; im Nenner zusammengehörige Pfade nicht zusammengefasst; eine Pfadwahrscheinlichkeit mit einer bedingten verwechselt) → didaktischer Typ, kein Prüfungstyp
- 2.6 Begründen (warum der Nenner die Summe aller Pfade zum eingetretenen Ereignis ist; warum sich die Richtung der Bedingung gegen die Baumrichtung dreht) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Mit Parameter** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Mindestwert einer Erkennungswahrscheinlichkeit aus einer Bedingung an eine bedingte Wahrscheinlichkeit bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Bayes-Term mit Parameter grafisch lösen und Parameter und Funktionswert im Sachzusammenhang deuten (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 3.3 Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen (6) → wortgleich; GK 1 (2026), Haupt 1 · LK 2 (2023, 2026), Haupt 2 · FHR 0
- 3.4 Graph einer bedingten Wahrscheinlichkeit in Abhängigkeit von einem Parameter über Randwerte ohne Rechnung zuordnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Term für eine bedingte Wahrscheinlichkeit mit Parameter aufstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Fehler finden (mit einem Zahlenbeispiel statt allgemein argumentiert; den Zähler für parameterabhängig gehalten, obwohl er konstant ist; die Deutung der Bedingung umgekehrt; den Graphen gewählt, ohne die Randwerte zu prüfen; die Bedingung im Term übersehen) → didaktischer Typ, kein Prüfungstyp
- 3.7 Begründen (warum ein Bruch mit konstantem Zähler wächst, wenn der Nenner fällt; warum die Randwerte des Parameterbereichs den Graphen festlegen) → didaktischer Typ, kein Prüfungstyp

### unabhaengigkeit

**Einheit 1 · Unabhängigkeit prüfen: die Produktregel P(A ∩ B) = P(A) · P(B) an Anteilen oder absoluten Häufigkeiten prüfen (Tafel oder Anzahlen erst beschaffen** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 4 von 8 (Haupt 4).

- 1.1 Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen (7) → wortgleich; GK 1 (2024), Haupt 1 · LK 1 (2022), Haupt 1 · FHR 0
- 1.2 Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen (3) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 1.3 Stochastische Unabhängigkeit prüfen (2; fhr) → wortgleich; GK 0 · LK 0 · FHR 4 (2023, 2024, 2025, 2026), Haupt 2
- 1.4 Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten (2) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 1.5 Vierfeldertafel vervollständigen (2; fhr) → wortgleich; GK 0 · LK 0 · FHR 3 (2023, 2024, 2026), Haupt 3
- 1.6 Fehler finden (Unabhängigkeit mit Unvereinbarkeit verwechselt – ein nichtleerer Schnitt ist kein Abhängigkeitsbeweis; die Richtung der bedingten Anteile vertauscht; einen bedingten Anteil auf die falsche Gesamtheit bezogen und damit die Tafel falsch gefüllt; P(A ∩ B) mit P_A(B) verwechselt; die Produktregel mit den falschen Werten geprüft) → didaktischer Typ, kein Prüfungstyp
- 1.7 Begründen (warum Produktregel und Anteilsvergleich dieselbe Prüfung sind; warum „abhängig“ nur „verschieden häufig“ heißt und keine Ursache behauptet) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Rückwärts** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen (3) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 2.2 Gleichung für p aus der Unabhängigkeit zweier Ereignisse im Baumdiagramm aufstellen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Parameter für die Unabhängigkeit zweier Ereignisse aus der Vierfeldertafel ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Wahrscheinlichkeit eines Fehlers aus der Vereinigung zweier unabhängiger Fehler berechnen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.5 Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.6 Fehler finden (P(A und nicht B) als Differenz oder Produkt der Randwahrscheinlichkeiten angesetzt; beim Additionssatz die Schnittmenge vergessen; die Nulllösung als Wahrscheinlichkeit angegeben; die falsche Zahl als unabhängigkeitsstiftenden Anteil gewählt; die Bedingung P(E ∩ G) mit P_E(G) verwechselt) → didaktischer Typ, kein Prüfungstyp
- 2.7 Begründen (warum Unabhängigkeit P(A ∩ ¬B) = P(A) · (1 − P(B)) liefert; warum der bedingte Anteil bei Unabhängigkeit gleich dem unbedingten ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Unabhängigkeit als Argument: die Ausgleichs-Fehlvorstellung widerlegen** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen (3) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 3.2 Fehler finden (das empirische Gesetz der großen Zahlen als Ausgleichspflicht der nächsten Versuche gelesen; mit der Seltenheit der langen Serie argumentiert statt mit der Konstanz der Einzelwahrscheinlichkeit) → didaktischer Typ, kein Prüfungstyp
- 3.3 Begründen (warum die Wahrscheinlichkeit des nächsten Versuchs nicht von den bisherigen abhängt; was das Gesetz der großen Zahlen tatsächlich sagt – Stabilisierung der relativen Häufigkeit, keine Kompensation) → didaktischer Typ, kein Prüfungstyp

### zufallsgroessen-und-verteilungen

**Einheit 1 · Verteilung aufstellen: die Werte der Zufallsgröße aus den Regeln gewinnen (alle Ergebnisfolgen durchrechnen), die Tabelle durch Abzählen füllen (günstige Paare je Wert), fehlende Wahrscheinlichkeiten über die Summe eins** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Wahrscheinlichkeitsverteilung der Augensumme in einer Tabelle vervollständigen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Wahrscheinlichkeitsverteilung über ein unmögliches Ergebnis vervollständigen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Mögliche Werte einer Auszahlung aus zweistufigen Spielregeln nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Wahrscheinlichkeit p aus der Summe 1 im Diagramm nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Fehler finden (spiegelbildliche Ergebnisfolgen als verschiedene Beträge erwartet; Paare nur einmal gezählt; fehlende Werte geraten statt über die Summe eins bestimmt; die Säulenhöhen als Auszahlungen gelesen) → didaktischer Typ, kein Prüfungstyp
- 1.6 Begründen (warum sich alle Wahrscheinlichkeiten zu eins summieren; warum ein unmöglicher Wert die Restverteilung festlegt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Verteilung lesen: die Symmetrie einer Verteilung nutzen (Restwahrscheinlichkeit gleich verteilen, kumulierte Werte daraus), beschriebene Zufallsgrößen den Säulendiagrammen zuordnen (Symmetrie, Verhältnisse einzelner Säulen). (Q2, GK-Kern „Verteilung in … Diagrammen“; OHiMi 2.4 Histogramme) ← Eingabe „verteilung zuordnen“, „symmetrische verteilung“, „säulendiagramm zufallsgröße“** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Wahrscheinlichkeit eines Ereignisses aus einer symmetrischen Verteilung und einem Einzelwert bestimmen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 2.2 Verteilungen zweier Zufallsgrößen den Säulendiagrammen zuordnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Fehler finden (den Einzelwert selbst als kumulierte Wahrscheinlichkeit angegeben; die Zuordnung nur nach der Form entschieden, ohne einzelne Säulenverhältnisse zu prüfen) → didaktischer Typ, kein Prüfungstyp
- 2.4 Begründen (warum die Symmetrie die Restwahrscheinlichkeit halbiert; warum ein Säulenverhältnis eine Verteilung identifiziert) → didaktischer Typ, kein Prüfungstyp

### hypergeometrische-verteilung

**Einheit 1 · Genau k Treffer ohne Zurücklegen: die Situation erkennen (feste kleine Gesamtheit, Ziehen ohne Zurücklegen** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 3 von 7 (Haupt 3) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen (3) → wortgleich; GK 1 (2022), Haupt 1 · LK 2 (2017, 2018), Haupt 2 · FHR 0
- 1.2 Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen (3; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 1.3 Fehler finden (binomial mit fester Trefferwahrscheinlichkeit gerechnet, obwohl ohne Zurücklegen gezogen wird – das Kernfehlmuster; mit Zurücklegen gerechnet; die Bruchkette mit gleichbleibendem Nenner) → didaktischer Typ, kein Prüfungstyp
- 1.4 Begründen (warum sich p von Zug zu Zug ändert; warum günstige durch mögliche Teilmengen dasselbe liefert wie die Bruchkette) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Kumulieren gegen eine Schranke: hypergeometrische Einzelwahrscheinlichkeiten aufsummieren und die größte (oder kleinste) Trefferzahl gegen eine Schranke bestimmen** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Größte Trefferzahl, bis zu der die kumulierte hypergeometrische Wahrscheinlichkeit unter einer Schranke bleibt, ermitteln (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.2 Fehler finden (mit der Binomialverteilung kumuliert; die Schranke am falschen Nachbarwert festgemacht) → didaktischer Typ, kein Prüfungstyp
- 2.3 Begründen (warum beide Nachbarwerte zu belegen sind) → didaktischer Typ, kein Prüfungstyp

### kenngroessen-von-verteilungen

**Einheit 1 · Erwartungswert berechnen und deuten: die Verteilung beschaffen (Tabelle, Sachtext, Baumpfade, Kosten je Ausgang; fehlende Wahrscheinlichkeit über die Summe 1), die gewichtete Summe bilden (bei Anzahlen n · p), das Ergebnis deuten** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 2 von 8 (Haupt 2).

- 1.1 Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen (5) → wortgleich; GK 3 (2018, 2019, 2021), Haupt 3 · LK 2 (2017, 2018), Haupt 2 · FHR 0
- 1.2 Erwartungswert berechnen (2; fhr) → wortgleich; GK 0 · LK 0 · FHR 2 (2019, 2021), Haupt 2
- 1.3 Prozentuale Abweichung einer Anzahl vom Erwartungswert berechnen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 1.4 Erwartungswert aus einer Verteilung mit fehlender Wahrscheinlichkeit berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Erwartungswert der Kosten pro Stück aus einer Wahrscheinlichkeitstabelle berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Erwartungswert eines Spielgewinns über die Pfade eines Baumdiagramms berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.7 Erwartungswert der Augensumme aus dem Erwartungswert der Trefferzahl berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.8 Erwartungswert einer weiteren Runde mit dem sicheren Betrag vergleichen und eine Empfehlung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.9 Erwartungswert der Auszahlung mit dem Einsatz vergleichen (3) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 1.10 Summand eines Erwartungswertterms im Sachzusammenhang deuten (2) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 1.11 Fehler finden (Auszahlung als Gewinn gedeutet, Einsatz nicht gegengerechnet; falsche Gewichte; fehlende Wahrscheinlichkeit nicht ergänzt; Selbstkosten mit entgangenem Gewinn verwechselt; Abweichung auf die falsche Bezugsgröße bezogen) → didaktischer Typ, kein Prüfungstyp
- 1.12 Begründen (warum der Erwartungswert kein möglicher Wert sein muss; warum „im Mittel gewinnbringend“ nichts über ein einzelnes Spiel sagt) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Rückwärts** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 6 von 7 (Haupt 6) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Unbekannte Größe aus einer Erwartungswertbedingung bestimmen (20) → wortgleich; GK 2 (2018, 2023), Haupt 2 · LK 5 (2017, 2022, 2023, 2025, 2026), Haupt 5 · FHR 0
- 2.2 Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten (3) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 2.3 Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen (2) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 2.4 Restwahrscheinlichkeit und Erwartungswert eines Teilgewinns aus dem Gesamterwartungswert bestimmen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 2.5 Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.6 Verhältnis zweier Auszahlungen aus dem Ausgleich der Erwartungswerte berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Kugelzahl für den größten Erwartungswert der Auszahlung ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Kugelbeschriftung aus dem Erwartungswert der Summe beim Ziehen ohne Zurücklegen berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Mindestanzahl aus einer Erwartungswertbedingung n · p > c ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Wertebereich des Erwartungswerts aus Ungleichungen für die Wahrscheinlichkeiten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.11 Untere Schranke für eine Kugelbeschriftung aus dem Erwartungswert der Summe ohne Rechnung begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.12 Aussage über gleiche Erwartungswerte aufeinanderfolgender Parameterwerte über eine Gleichung beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.13 Fehler finden (Fairness als Gewinnerwartung null statt Auszahlungserwartung gleich Einsatz angesetzt; Reihenfolgen-Faktor vergessen; mit statt ohne Zurücklegen gerechnet; unzulässige Lösung mitgenommen oder die verlangte negative übersehen; falsch auf- oder abgerundet) → didaktischer Typ, kein Prüfungstyp
- 2.14 Begründen (warum „Einsätze und Auszahlungen gleichen sich aus“ eine Gleichung liefert; warum die Summenbedingung die zweite Gleichung ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Varianz und Standardabweichung: die allgemeinen Formeln (gewichtete quadrierte Abweichung, Wurzel), die Binomialformeln μ = n · p und σ = √(n · p · (1 − p)) vorwärts und rückwärts (Parameter aus Kenngrößen, Symmetrie liefert p), Argumente über die Formel (Parabel in p, Symmetrie von p und Gegenwahrscheinlichkeit, Wachstum mit der Wurzel aus n). (BB Q2 GK-Kern, BE Q4 GK binomial bzw. LK allgemein; [IQB-VER 4] vorausgesetzt) ← Eingabe „standardabweichung“, „varianz“, „sigma“, „streuung“** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen (2) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 3.2 Standardabweichung einer Binomialverteilung aus n und Erwartungswert berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Parameter n aus Erwartungswert und Symmetrie einer Binomialverteilung ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Verhältnis der Varianzen zweier Binomialverteilungen aus dem Erwartungswert im Diagramm bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Stichprobenumfang für eine verdoppelte Standardabweichung der Binomialverteilung ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Standardabweichung über einen Summanden der Varianz abschätzen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Gleiche Standardabweichung zweier komplementärer Zufallsgrößen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.8 Monotonie der Varianz einer Binomialverteilung in p über die Parabel begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.9 Achsen des Graphen der Standardabweichung in Abhängigkeit von p skalieren und erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.10 Fehler finden (σ statt σ² in die Formel gesetzt; die Wurzel nur über einen Teil des Produkts gezogen; Varianz als Standardabweichung angegeben; n verdoppelt statt vervierfacht; mit gleichen Erwartungswerten statt mit der Symmetrie der Formel argumentiert) → didaktischer Typ, kein Prüfungstyp
- 3.11 Begründen (warum die Varianz in p eine Parabel ist und was ihr Scheitel bedeutet; warum ein einzelner Summand die Varianz nach unten abschätzt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Kenngrößen am Säulendiagramm: den ganzzahligen Erwartungswert an der höchsten Säule ablesen und daraus p, n oder Verhältnisse bestimmen, die Parität von n aus zwei gleich hohen Säulen begründen, ein Sigma-Intervall auf ganze Werte übertragen und die Wahrscheinlichkeit als Summe der Säulenhöhen ablesen. (GOST-Inhalt „Eigenschaften auf der Grundlage graphischer Darstellungen“; OHiMi 2.4 „Histogramme“; alle Zeilen Teil A, gehäuft seit 2024) ← Eingabe „höchste säule“, „diagramm erwartungswert“, „sigma-intervall“, „säulendiagramm binomial“** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.1 Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln (4) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 4.2 Wahrscheinlichkeit eines Sigma-Intervalls aus dem Säulendiagramm ermitteln (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 4.3 Parität von n aus zwei gleich hohen Säulen der Verteilung begründen (2) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 4.4 Fehler finden (p aus der Höhe statt aus der Lage der höchsten Säule abgelesen; Säulenhöhen statt Lage der Maxima verglichen; Intervallgrenzen gerundet statt die eingeschlossenen ganzen Werte bestimmt) → didaktischer Typ, kein Prüfungstyp
- 4.5 Begründen (warum der ganzzahlige Erwartungswert an der höchsten Säule liegt; warum ein Doppelmaximum den Erwartungswert zwischen die Säulen legt) → didaktischer Typ, kein Prüfungstyp

### normalverteilung-und-sigma-regeln

**Einheit 1 · Modell und Glockenkurve: die Dichtefunktion lesen und skizzieren (μ als Symmetrieachse und Maximumsstelle, σ als Breitenmaß** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 1.2 Eignung der Normalverteilung trotz negativer Werte im Definitionsbereich begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Dichtefunktion mit gleichem Erwartungswert und größerer Standardabweichung skizzieren (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Dichtefunktionen zu verschobenem Erwartungswert und kleinerer Standardabweichung skizzieren und Wirkung auf eine Wahrscheinlichkeit begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Wahrscheinlichkeit eines Einzelwerts einer stetigen Zufallsgröße angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.6 Fehler finden (den Dichtewert als Wahrscheinlichkeit gedeutet; die Glocke breiter, aber gleich hoch gezeichnet – die Fläche wäre größer als eins; bei kleinerem σ die Glocke niedriger statt höher gezeichnet; das Modell wegen einer positiven, aber verschwindend kleinen Wahrscheinlichkeit verworfen) → didaktischer Typ, kein Prüfungstyp
- 1.7 Begründen (warum die Fläche unter jeder Dichte eins ist; warum ein Einzelwert einer stetigen Zufallsgröße die Wahrscheinlichkeit null hat) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Wahrscheinlichkeiten berechnen: Intervall- und einseitige Wahrscheinlichkeiten mit dem Rechner, die Sigma-Regeln der Formelsammlung, Symmetrie und Gegenereignis (außerhalb wird halbiert), Sachbedingungen übersetzen („weicht um höchstens … ab“ als symmetrisches Intervall um den Sollwert, diskrete Anzahlen im stetigen Modell über halbe Schritte), Näherungen ohne Rechner (Rechteck unter der Dichte). (Q4 LK; FS-IQB Abschnitt „Sigma-Regeln“) ← Eingabe „normalverteilung wahrscheinlichkeit“, „sigma-regeln“, „intervall normalverteilung“** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen (4) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 2.2 Wahrscheinlichkeit außerhalb eines symmetrischen Intervalls über die Symmetrie der Normalverteilung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 2.4 Näherung einer Normalverteilungswahrscheinlichkeit über Rechteck und Symmetrie erläutern (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Fehler finden (einseitig statt zweiseitig gerechnet; die Sollwert-Abweichung ohne halbe Schritte übersetzt; außerhalb des symmetrischen Intervalls nicht halbiert; für eine diskrete Anzahl im stetigen Modell die Wahrscheinlichkeit null geantwortet) → didaktischer Typ, kein Prüfungstyp
- 2.6 Begründen (warum die halben Schritte nötig sind, wenn eine Anzahl stetig modelliert wird; warum die Symmetrie die Außenwahrscheinlichkeit halbiert) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Umkehraufgaben und Argumente: μ aus einer Wahrscheinlichkeitsvorgabe bei bekanntem σ, Grenzen und Quantile, μ und σ am Graphen der Verteilungsfunktion (die Stelle mit dem Wert ein Halb) und am Dichteterm ablesen ([IQB-VER 4] vorausgesetzt), Argumente über die Parameter (Monotonie in σ, das beste Intervall fester Länge liegt symmetrisch um μ). (Q4 LK; Prüfungshöhe des Pools in Teil B) ← Eingabe „umkehraufgabe normalverteilung“, „mu gesucht“, „quantil“, „parameter ablesen“** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Erwartungswert einer Normalverteilung aus einer Wahrscheinlichkeitsvorgabe ermitteln und weitere Wahrscheinlichkeit berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Parameter aus der Dichtefunktion ablesen und Bedingungen an Wahrscheinlichkeiten der Normalverteilung prüfen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Parameter einer Normalverteilung aus dem Graphen der Verteilungsfunktion ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Implikation zweier Wahrscheinlichkeitsbedingungen der Normalverteilung über eine Schranke für σ begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Quantil einer Normalverteilung bestimmen und Wahrscheinlichkeit dafür bei einer zweiten Verteilung beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Maximale Wahrscheinlichkeit eines Intervalls fester Länge über die Lage um den Erwartungswert begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Fehler finden (σ falsch aus dem Vorfaktor des Dichteterms gelesen; die Achsenskalierung des Verteilungsfunktions-Graphen übersehen; μ gleich der vorgegebenen Grenze gesetzt; die Monotonie in σ nicht benannt und nur einen Einzelfall gerechnet; die Aufgabe bei unbekanntem μ für unlösbar gehalten) → didaktischer Typ, kein Prüfungstyp
- 3.8 Begründen (warum die Stelle mit dem Verteilungsfunktionswert ein Halb der Erwartungswert ist; warum kleineres σ die Masse näher an μ zieht) → didaktischer Typ, kein Prüfungstyp

### hypothesentests

**Einheit 1 · Entscheidungsregel bestimmen: die Nullhypothese liefert p und die Binomialverteilung der Testgröße, die Alternative die Seite des Ablehnungsbereichs (rechtsseitig bei „mehr als“, linksseitig bei „weniger als“); die Grenze über kumulierte Wahrscheinlichkeiten so wählen, dass das Signifikanzniveau eingehalten wird** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Entscheidungsregel eines einseitigen Signifikanztests bestimmen (6) → wortgleich; GK 0 · LK 3 (2018, 2023, 2025), Haupt 3 · FHR 0
- 1.2 Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.3 Fehler finden (rechts- statt linksseitig getestet; die Grenze um eins verfehlt, weil das knapp überschrittene Niveau in Kauf genommen wurde; die Minimalität nicht oder in der falschen Richtung belegt) → didaktischer Typ, kein Prüfungstyp
- 1.4 Begründen (warum die Seite des Ablehnungsbereichs aus der Alternative folgt; warum der Nachbarwert zur Begründung der Grenze gehört) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Die Nullhypothese wählen: aus der Sicht des Entscheiders** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Wahl der Nullhypothese aus der Sicht des Entscheiders begründen (5) → wortgleich; GK 0 · LK 2 (2022, 2024), Haupt 2 · FHR 0
- 2.2 Fehler finden (den Fehler zweiter Art als kontrolliert angesehen oder als Grund der Wahl genannt; die Überlegung ohne Bezug zum begrenzten Risiko formuliert) → didaktischer Typ, kein Prüfungstyp
- 2.3 Begründen (warum nur der Fehler erster Art durch das Signifikanzniveau begrenzt ist; wem welcher Irrtum schadet) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Fehlerarten und Güte: den Fehler zweiter Art für selbst gewählte Anteile berechnen (p dort wählen, wo die Nullhypothese falsch ist), einordnen und im Sachzusammenhang beschreiben; Mindestanteile für eine Fehlerschranke; die Gütekurve lesen (Ablehnwahrscheinlichkeit in Abhängigkeit von p** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen (3) → wortgleich; GK 0 · LK 2 (2023, 2024), Haupt 2 · FHR 0
- 3.2 Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 3.3 Fehler zweiter Art aus dem Graphen der Ablehnwahrscheinlichkeit ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Stichprobenumfang eines Tests aus Ablehnungsgrenze und Fehler erster Art am Graphen ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.5 Untere Schranke für den Stichprobenumfang eines Tests über den Fehler erster Art am Graphen begründen (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.6 Nutzen eines größeren Stichprobenumfangs über den Fehler zweiter Art an den Gütekurven begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Fehler finden (p auf der Seite gewählt, wo die Nullhypothese wahr ist – dort gibt es keinen Fehler zweiter Art; den Fehler erster Art als zweiten gerechnet; das Komplement des Annahmebereichs verfehlt; am Graphen die falsche Stelle abgelesen; die Monotonie in n in der falschen Richtung) → didaktischer Typ, kein Prüfungstyp
- 3.8 Begründen (warum der Fehler zweiter Art vom gewählten p abhängt und nahe eins liegen kann; warum größeres n ihn verkleinert) → didaktischer Typ, kein Prüfungstyp

### konfidenzintervalle

**Einheit 1 · Das Intervall lesen und deuten: die Überdeckungsdeutung (verträglich heißt: der angenommene Anteil wird vom Intervall überdeckt** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.1 Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.2 Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Fehler finden (die Senkrechte beim vermuteten p statt der Waagerechten beim Stichprobenanteil geschnitten; die inneren statt der äußeren Grenzgraphen verwendet; einen Anteil gewählt, den alle Intervalle treffen; „genau k“ als „mindestens k“ gerechnet) → didaktischer Typ, kein Prüfungstyp
- 1.5 Begründen (warum die Überdeckungszahl binomialverteilt ist und was ihre Trefferwahrscheinlichkeit ist; warum „Sicherheit“ eine Aussage über viele Intervalle ist, nicht über das eine) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Mit der Näherungsformel rechnen: die Grenzgleichung nach p lösen (quadratisch** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 2.1 Grenzen eines Konfidenzintervalls aus dem Stichprobenergebnis über die Näherungsformel berechnen und im Diagramm zuordnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.2 Konfidenzintervall aus dem Diagramm identifizieren und Stichprobenergebnis aus der Grenze berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.3 Kleinsten Stichprobenumfang für die Unverträglichkeit eines Anteils mit einer Annahme über die Näherungsformel ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Fehler finden (die Gleichung in h statt in p gelöst – die bequeme Näherung liefert andere Grenzen; die Grenze mit dem Umfang multipliziert statt erst h aus der Grenzgleichung bestimmt; die Anzahl statt des Anteils in die Formel gesetzt) → didaktischer Typ, kein Prüfungstyp
- 2.5 Begründen (warum die Grenzgleichung zwei Lösungen hat und beide Grenzen sind; warum Unverträglichkeit eine Ungleichung in n ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Argumente über Formel und Verträglichkeit: die Länge des Intervalls bei doppeltem Umfang (Faktor eins durch Wurzel zwei** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Länge eines Konfidenzintervalls bei doppeltem Stichprobenumfang über den Faktor 1/√2 begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.2 Obere Grenze eines Konfidenzintervalls über den Stichprobenanteil begründen und Verträglichkeit einer Annahme beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Verträglichkeit zweier Annahmen mit demselben Stichprobenanteil über den Stichprobenumfang beurteilen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Fehler finden (die Länge als proportional zu eins durch n angenommen; die obere Grenze über eine vermeintliche Symmetrie rechnen wollen; die Richtung der Ungleichungen in n vertauscht) → didaktischer Typ, kein Prüfungstyp
- 3.5 Begründen (warum der Stichprobenanteil im Intervall liegt; warum wachsendes n das Intervall enger macht und eine Annahme herausfallen kann, während die andere drin bleibt) → didaktischer Typ, kein Prüfungstyp

### zufallsexperimente-und-pfadregeln

**Einheit 1 · Ereignisse als Mengen** – Abitur-Jahrgänge GK 3 von 9 (Haupt 3) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 3 von 8 (Haupt 3).

- 1.1 Anteil für genau eines von zwei Ereignissen aus Anteilen und Schnitt berechnen (4) → wortgleich; GK 2 (2022, 2024), Haupt 2 · LK 0 · FHR 0
- 1.2 Anteil eines Entweder-oder-Ereignisses aus einer Tafel berechnen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Wahrscheinlichkeit des Gegenereignisses einer Vereinigung nachweisen und als Ereignis angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.4 Wahrscheinlichkeit eines Schnitts aus einem Randanteil und dem Anteil ohne beide Mängel nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.5 Ergebnismenge eines Zufallsexperiments angeben (3; fhr) → wortgleich; GK 0 · LK 0 · FHR 3 (2021, 2022, 2023), Haupt 3
- 1.6 Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben (3) → wortgleich; GK 1 (2026), Haupt 1 · LK 0 · FHR 0
- 1.7 Term und Ereignis: Schnittwahrscheinlichkeit zweier Ereignisse im Sachzusammenhang deuten (3) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 1.8 Term und Ereignis: Bedingte Wahrscheinlichkeit und Schnittwahrscheinlichkeit im Sachzusammenhang deuten (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 1.9 Gegenereignis einer Vereinigung im Sachzusammenhang beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.10 Laplace-Experiment: Ergebnisse eines zusammengesetzten Experiments zu einem Zahlenwert aufzählen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.11 Term P(A) + P(B) − 2 · P(A ∩ B) als Wahrscheinlichkeit für genau eines der Ereignisse deuten (1) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 1.12 Fehler finden (das einschließende Oder gerechnet, wo „entweder – oder“ verlangt war; den Überstrich über einer Vereinigung übersehen und die Vereinigung selbst beschrieben; P(A ∩ B) als bedingte Wahrscheinlichkeit gelesen; in der Ergebnismenge die Reihenfolge vernachlässigt und Paare nur einmal gezählt; ein Ergebnis mit der falschen Rechenregel mitgezählt) → didaktischer Typ, kein Prüfungstyp
- 1.13 Begründen (warum der Schnitt beim Additionssatz einmal, beim „genau eines“ zweimal abgezogen wird; warum das Gegenereignis von „A oder B“ „weder A noch B“ ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Laplace-Experimente in der Oberstufe** – Abitur-Jahrgänge GK 2 von 9 (Haupt 2) · LK 3 von 7 (Haupt 2) · FHR-Jahrgänge 4 von 8 (Haupt 2).

- 2.1 Laplace-Wahrscheinlichkeit berechnen (3; fhr) → wortgleich; GK 0 · LK 0 · FHR 3 (2019, 2022, 2023), Haupt 2
- 2.2 Laplace-Experiment: Sektorenzahlen eines Glücksrads aus Wahrscheinlichkeiten ermitteln (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 2.3 Laplace-Experiment: Wahrscheinlichkeit durch Abzählen günstiger Ergebnisse berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen (6) → wortgleich; GK 1 (2019), Haupt 1 · LK 1 (2025), Haupt 1 · FHR 0
- 2.5 Laplace-Experiment: Wahrscheinlichkeit eines Vergleichsereignisses beim Wurf zweier Würfel über die Ergebnistabelle nachweisen (2) → wortgleich; GK 2 (2019, 2021), Haupt 2 · LK 0 · FHR 0
- 2.6 Laplace-Bedingung begründen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 4 (2019, 2021, 2022, 2023), Haupt 1
- 2.7 Laplace-Experiment: Kleinere Gesamtzahl von Kugeln aus gekürzten Anteilen begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.8 Laplace-Experiment: Wahrscheinlichkeit einer Augensumme beim Wurf zweier Würfel begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.9 Laplace-Experiment: Wahrscheinlichkeit eines sicheren Ereignisses beim Umlegen einer Kugel begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.10 Laplace-Experiment: Wahrscheinlichkeiten zweier Extremsummen über die Häufigkeit der Beschriftung vergleichen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.11 Laplace-Experiment: Wahrscheinlichkeitsterm nach Hinzufügen von Kugeln als Anteil begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.12 Laplace-Experiment: Zunahme einer Wahrscheinlichkeit nach Hinzufügen von Kugeln über eine Termdifferenz begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.13 Laplace-Experiment: Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben (3) → wortgleich; GK 1 (2019), Haupt 1 · LK 1 (2017), Haupt 0 · FHR 0
- 2.14 Laplace-Experiment: Urnenmodell zu einer vorgegebenen Verteilung beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.15 Fehler finden (doch gerechnet, wo eine Begründung über Anzahlen verlangt war; gleiche Augenzahlen beim Vergleich „kleiner als“ mitgezählt; (2; 6) und (6; 2) als ein Ergebnis genommen; die Grundmenge nicht angepasst – Leiterin nicht abgezogen, die Gesamtzahl der Sektoren nicht bestimmt; verschieden große Sektoren als gleich wahrscheinlich angesetzt; beim Term in n den Nenner um eins statt um die Zahl der hinzugefügten Kugeln erhöht) → didaktischer Typ, kein Prüfungstyp
- 2.16 Begründen (warum beim Vergleich zweier Laplace-Wahrscheinlichkeiten der Nenner wegbleiben darf; warum ein Glücksrad mit ungleichen Sektoren kein Laplace-Experiment ist, ein Würfel mit doppelt beschrifteten Seiten aber doch) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Pfadregeln bei unabhängigen Stufen** – Abitur-Jahrgänge GK 7 von 9 (Haupt 7) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 6 von 8 (Haupt 5).

- 3.1 Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen (7) → wortgleich; GK 1 (2021), Haupt 1 · LK 2 (2017, 2022), Haupt 2 · FHR 0
- 3.2 Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen (6) → wortgleich; GK 1 (2024), Haupt 1 · LK 1 (2025), Haupt 1 · FHR 0
- 3.3 Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen (3) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 3.4 Wahrscheinlichkeit einer vorgegebenen Augensumme bei zwei Würfen über Pfade berechnen (3) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 3.5 Wahrscheinlichkeit für mindestens oder höchstens einmal bei mehreren Stufen über das Gegenereignis berechnen (3) → wortgleich; GK 1 (2020), Haupt 0 · LK 1 (2022), Haupt 1 · FHR 0
- 3.6 Wahrscheinlichkeit einer ungeraden Summe über Pfade berechnen (2) → wortgleich; GK 1 (2025), Haupt 1 · LK 0 · FHR 0
- 3.7 Wahrscheinlichkeit eines Vergleichs zweier Zufallsgeräte über Pfade berechnen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 3.8 Pfadregel mehrstufig mit Zurücklegen anwenden (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 4 (2019, 2021, 2024, 2025), Haupt 1
- 3.9 Wahrscheinlichkeit eines Spielausgangs über Pfade mit Abbruch berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.10 Wahrscheinlichkeit für das Erreichen eines Feldes über die Pfadregel berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.11 Wahrscheinlichkeit für mehrere Wiederholungen ohne Abbruch als Potenz berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Wahrscheinlichkeit für mindestens einen von zwei unabhängigen Erfolgen über das Gegenereignis berechnen (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 3.13 Wahrscheinlichkeit für zwei gleichfarbige Kugeln beim Ziehen mit Zurücklegen als Summe zweier Pfade berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 3.14 Gewinnwahrscheinlichkeiten in einem Wechselspiel vergleichen (3) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 3.15 Behauptung über die größere Wahrscheinlichkeit einer Augensumme bei zwei Würfeln über die Pfade widerlegen (1) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 3.16 Wahrscheinlichkeit eines Gewinns über alle günstigen Summenpfade nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.17 Baumdiagramm zweistufig darstellen (4; fhr) → wortgleich; GK 0 · LK 0 · FHR 3 (2019, 2022, 2026), Haupt 3
- 3.18 Baumdiagramm mit Abbruchbedingung erstellen (2) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 3.19 Baumdiagramm mehrstufig mit Zurücklegen darstellen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 1 (2021), Haupt 1
- 3.20 Wahrscheinlichkeitsverteilung aufstellen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 1 (2022), Haupt 1
- 3.21 Fehler finden (Wahrscheinlichkeiten addiert oder vervielfacht statt multipliziert; einen Binomialkoeffizienten ergänzt, obwohl die Reihenfolge festliegt; die Potenz mit der Trefferwahrscheinlichkeit statt der Nietenwahrscheinlichkeit gebildet; nur einen von mehreren Pfaden gerechnet; beim Abbruch alle Pfade auf volle Länge gezeichnet; in einem Wechselspiel nur den ersten Zug des Zweiten berücksichtigt; „höchstens einmal“ als „genau einmal“ gelesen) → didaktischer Typ, kein Prüfungstyp
- 3.22 Begründen (warum die Äste auf jeder Stufe gleich bleiben, wenn zurückgelegt wird oder verschiedene Geräte gedreht werden; warum „mindestens einmal in n Versuchen“ über das Gegenereignis eine Potenz wird; warum beim Abbruch die Pfade verschieden lang sind und sich trotzdem zu eins ergänzen) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Ziehen ohne Zurücklegen und Umlegen** – Abitur-Jahrgänge GK 6 von 9 (Haupt 6) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 8 von 8 (Haupt 7).

- 4.1 Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen (9) → wortgleich; GK 4 (2018, 2019, 2020, 2025), Haupt 4 · LK 0 · FHR 0
- 4.2 Wahrscheinlichkeit bei zweistufigem Umlegen zwischen Urnen berechnen (2) → wortgleich; GK 0 · LK 1 (2017), Haupt 1 · FHR 0
- 4.3 Gegenereignis nutzen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2021, 2024, 2025, 2026), Haupt 1
- 4.4 Pfadregel mehrstufig ohne Zurücklegen anwenden (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 5 (2020, 2021, 2023, 2024, 2025), Haupt 1
- 4.5 Ziehen ohne Zurücklegen: Wahrscheinlichkeit für ausschließlich eine Sorte beim mehrfachen Ziehen als Produkt berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 4.6 Ziehen ohne Zurücklegen: Wahrscheinlichkeit für spätestens den dritten Zug über das Gegenereignis berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.7 Ziehen ohne Zurücklegen: Gleiche Chance verschiedener Ziehungspositionen beim Ziehen ohne Zurücklegen begründen (1) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 4.8 Baumdiagramm mehrstufig ohne Zurücklegen darstellen (10; fhr) → wortgleich; GK 0 · LK 0 · FHR 7 (2019, 2020, 2021, 2022, 2023, 2024, 2025), Haupt 7
- 4.9 Ziehen ohne Zurücklegen: Mögliche Anzahlen nach dem Umlegen zweier Kugeln angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.10 Fehler finden (mit Zurücklegen gerechnet – der Nenner bleibt stehen; die Kugelzahl nach dem Umlegen nicht angepasst; nur einen der beiden Pfade „verschiedene Farben“ genommen; zwei statt vier Ziehungen angesetzt, weil von zwei Personen die Rede war; angenommen, frühere Ziehungen senkten die Chance der späteren) → didaktischer Typ, kein Prüfungstyp
- 4.11 Begründen (warum die Astwahrscheinlichkeit der zweiten Stufe ein bedingter Anteil ist; warum die Ziehungsposition ohne Zurücklegen die Chance nicht ändert, das Wissen um frühere Züge aber schon) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Mammutbäume** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 2 von 7 (Haupt 2) · FHR-Jahrgänge 6 von 8 (Haupt 2).

- 5.1 Wahrscheinlichkeit einer Summe über alle Ergebnisfolgen mit Reihenfolgen berechnen (3) → wortgleich; GK 1 (2021), Haupt 1 · LK 0 · FHR 0
- 5.2 Term für die Wahrscheinlichkeit eines Produktereignisses bei n Würfen ermitteln (2) → wortgleich; GK 0 · LK 1 (2025), Haupt 1 · FHR 0
- 5.3 Wahrscheinlichkeit für k Treffer unmittelbar hintereinander unter n Versuchen berechnen (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 5.4 Wahrscheinlichkeit über mehrere Pfade summieren (2; fhr) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2021, 2022, 2023, 2024), Haupt 2
- 5.5 Ziehen ohne Zurücklegen: Wahrscheinlichkeit für höchstens k einer Sorte über Binomialkoeffizienten berechnen (2) → wortgleich; GK 2 (2019, 2023), Haupt 2 · LK 0 · FHR 0
- 5.6 Ziehen ohne Zurücklegen: Wahrscheinlichkeit für eine Mehrheit einer Sorte beim dreimaligen Ziehen ohne Zurücklegen berechnen (1) → wortgleich; GK 1 (2023), Haupt 1 · LK 0 · FHR 0
- 5.7 Ziehen ohne Zurücklegen: Wahrscheinlichkeit für genau drei aufeinanderfolgende gleichfarbige Kugeln beim Ziehen ohne Zurücklegen berechnen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 5.8 Ziehen ohne Zurücklegen: Wahrscheinlichkeit für genau k einer Sorte beim mehrfachen Ziehen über Pfade berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.9 Laplace-Experiment: Wahrscheinlichkeit für drei verschiedene Ergebnisse über Pfadprodukt und Reihenfolgen nachweisen (2) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 5.10 Ziehen ohne Zurücklegen: Kugelzahl für eine begrenzte Anzahl von Farbreihenfolgen beim Ziehen ohne Zurücklegen begründen (1) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 5.11 Fehler finden (den Faktor für die Reihenfolgen vergessen – der häufigste Fehler des Themas; einen Binomialkoeffizienten für einen Block genommen, der nur wenige Lagen hat; eine Zerlegung der Summe übersehen; „weniger als zwei“ als „höchstens zwei“ gelesen; beim Lotto-Bruch die Auswahl der einen Sorte im Zähler vergessen) → didaktischer Typ, kein Prüfungstyp
- 5.12 Begründen (warum alle Pfade mit denselben Sorten in anderer Reihenfolge dieselbe Wahrscheinlichkeit haben – auch ohne Zurücklegen; warum der Lotto-Bruch und der Pfadweg dasselbe Ergebnis liefern) → didaktischer Typ, kein Prüfungstyp

**Einheit 6 · Situationsbäume** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 7 von 7 (Haupt 6) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 6.1 Fehlende Wahrscheinlichkeiten im Baumdiagramm über die Pfadregel ermitteln (3) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 6.2 Anteil über die totale Wahrscheinlichkeit aus dem Baumdiagramm berechnen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.3 Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen (2) → wortgleich; GK 0 · LK 2 (2017, 2023), Haupt 1 · FHR 0
- 6.4 Totale Wahrscheinlichkeit über die Pfadregeln nachweisen (4) → wortgleich; GK 2 (2021, 2025), Haupt 2 · LK 0 · FHR 0
- 6.5 Absolute Anzahl aus einer Pfadwahrscheinlichkeit mit einer Schranke vergleichen (2) → wortgleich; GK 0 · LK 1 (2026), Haupt 1 · FHR 0
- 6.6 Anzahlvergleich zweier Teilgruppen über Pfadwahrscheinlichkeiten nachweisen (2) → wortgleich; GK 0 · LK 1 (2023), Haupt 1 · FHR 0
- 6.7 Baumdiagramm zu einer zweistufigen Situation erstellen (11) → wortgleich; GK 1 (2025), Haupt 1 · LK 5 (2017, 2018, 2023, 2024, 2025), Haupt 3 · FHR 0
- 6.8 Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen (5) → wortgleich; GK 1 (2026), Haupt 1 · LK 1 (2025), Haupt 1 · FHR 0
- 6.9 Baumdiagramm mit aus einer Pfadwahrscheinlichkeit erschlossener Einzelwahrscheinlichkeit erstellen (4) → wortgleich; GK 1 (2024), Haupt 1 · LK 1 (2022), Haupt 1 · FHR 0
- 6.10 Baumdiagramm eines Befragungsverfahrens mit unbekanntem Anteil vervollständigen (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 6.11 Astwahrscheinlichkeit im Baumdiagramm einer Befragung im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.12 Fehler finden (einen Anteil „unter den …“ als Anteil aller an die erste Stufe gesetzt; die Stufen vertauscht; einen Pfadanteil direkt an einen Ast geschrieben statt durch die erste Stufe zu teilen; nur einen der beiden Pfade zur Randwahrscheinlichkeit genommen; Anteile ungewichtet gemittelt; beim Vergleich zweier Gruppen die bedingten Anteile statt der Pfade verglichen; die Zufallsfrage unter beiden Ästen gleich beschriftet) → didaktischer Typ, kein Prüfungstyp
- 6.13 Begründen (warum die totale Wahrscheinlichkeit die Summe aller Pfade zum Merkmal ist; warum ein Anteil „aller“ ein Pfad oder ein Rand ist, nie ein Ast) → didaktischer Typ, kein Prüfungstyp

**Einheit 7 · Term und Ereignis** – Abitur-Jahrgänge GK 4 von 9 (Haupt 4) · LK 4 von 7 (Haupt 4) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 7.1 Term und Ereignis: Wahrscheinlichkeitsterm über das Gegenereignis gleicher Ergebnisse begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 7.2 Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben (21) → wortgleich; GK 3 (2021, 2024, 2025), Haupt 2 · LK 3 (2018, 2023, 2026), Haupt 3 · FHR 0
- 7.3 Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen (8) → wortgleich; GK 2 (2021, 2026), Haupt 2 · LK 2 (2022, 2026), Haupt 2 · FHR 0
- 7.4 Term und Ereignis: Produkt aus Potenz und Binomialterm als Ereignis mit festem Abschnitt deuten (2) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 7.5 Term für die Wahrscheinlichkeit eines mehrstufigen Pfads angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 7.6 Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitswert als Potenz angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 7.7 Term und Ereignis: Zufallsexperiment und Ereignis zu einer Potenz der Gegenwahrscheinlichkeit beschreiben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 7.8 Fehler finden (den Vorfaktor als Wahrscheinlichkeit einer weiteren Stufe gelesen; eine Basis der falschen Sorte zugeordnet, weil sie im Bild auffällt; „genau“ und „mindestens“ vertauscht; das Gegenereignis nur teilweise gebildet; einen Platzhalter mit der Trefferwahrscheinlichkeit gefüllt, wo die Niete steht; beim Term mit festem Abschnitt die Potenz als „irgendwo“ gedeutet) → didaktischer Typ, kein Prüfungstyp
- 7.9 Begründen (warum ein Term ohne Vorfaktor eine feste Reihenfolge beschreibt; warum die Exponenten zusammen die Zahl der Versuche ergeben müssen) → didaktischer Typ, kein Prüfungstyp

**Einheit 8 · Rückwärts** – Abitur-Jahrgänge GK 5 von 9 (Haupt 5) · LK 5 von 7 (Haupt 5) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 8.1 Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen (7) → wortgleich; GK 1 (2026), Haupt 1 · LK 3 (2017, 2023, 2026), Haupt 3 · FHR 0
- 8.2 Laplace-Experiment: Sektorwinkel eines Glücksrads aus einer Wahrscheinlichkeitsbedingung berechnen (3) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 8.3 Anteil aus dem Ergebnis eines Befragungsverfahrens berechnen (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 8.4 Anteil aus einem Verhältnis zweier Pfadwahrscheinlichkeiten berechnen (2) → wortgleich; GK 1 (2020), Haupt 1 · LK 0 · FHR 0
- 8.5 Anteil aus einer quadratischen Gleichung für ein zweistufiges Bestehen berechnen (2) → wortgleich; GK 1 (2019), Haupt 1 · LK 0 · FHR 0
- 8.6 Anteil in der Restgruppe über die totale Wahrscheinlichkeit einordnen (2) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 8.7 Ziehen ohne Zurücklegen: Kugelzahl aus einer Wahrscheinlichkeitsbedingung beim Umlegen einer Kugel bestimmen (2) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 8.8 Bedingte Wahrscheinlichkeit einer Teilgruppe aus totaler Wahrscheinlichkeit und der anderen Teilgruppe berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 8.9 Laplace-Experiment: Kugelzahl aus zwei Wahrscheinlichkeitsbedingungen vor und nach einem Austausch ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 8.10 Laplace-Experiment: Sektorwinkel eines Glücksrads aus der Maximierung einer Wahrscheinlichkeit ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 8.11 Ziehen ohne Zurücklegen: Anzahl einer Sorte aus der Wahrscheinlichkeit für zwei verschiedene Sorten bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 8.12 Ziehen ohne Zurücklegen: Entfernte Kugel aus einer Wahrscheinlichkeit für verschiedene Farben entscheiden (1) → wortgleich; GK 1 (2022), Haupt 1 · LK 0 · FHR 0
- 8.13 Ziehen ohne Zurücklegen: Kugelzahl aus dem Vergleich der zweiten Zugwahrscheinlichkeit mit und ohne Zurücklegen berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 8.14 Ziehen ohne Zurücklegen: Kugelzahlen aus zwei Astwahrscheinlichkeiten eines unvollständigen Baumdiagramms ermitteln (1) → wortgleich; GK 0 · LK 1 (2022), Haupt 1 · FHR 0
- 8.15 Ziehen ohne Zurücklegen: Mindestanzahl beim Ziehen ohne Zurücklegen über das Gegenereignis bestimmen (1) → wortgleich; GK 0 · LK 1 (2018), Haupt 1 · FHR 0
- 8.16 Anteil einer Eigenschaft aus einer Randomized-Response-Befragung über die totale Wahrscheinlichkeit nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 8.17 Fehler finden (den beobachteten Anteil direkt als gesuchten Anteil genommen; den Anteil des zweiten Versuchs auf alle statt auf die Durchgefallenen bezogen; das Verhältnis der bedingten Anteile statt der Pfade angesetzt; „zwei Prozent größer“ als plus statt als Faktor gelesen; die zweite Lösung nicht ausgeschlossen; die Kugelzahl nach dem Umlegen im Nenner nicht erhöht; binomial gerechnet, wo ohne Zurücklegen gezogen wird) → didaktischer Typ, kein Prüfungstyp
- 8.18 Begründen (warum eine Randwahrscheinlichkeit eine Gleichung liefert; warum von zwei Lösungen einer quadratischen Gleichung der Sachzusammenhang entscheidet) → didaktischer Typ, kein Prüfungstyp

### kombinatorik

**Einheit 1 · Zählprinzip und Anordnungen** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 7 von 8 (Haupt 4).

- 1.1 Permutation ohne Wiederholung berechnen (2; fhr) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2021, 2022, 2023, 2025), Haupt 2
- 1.2 Anzahl geordneter Auswahlen ohne Wiederholung berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.3 Anzahl über das Zählprinzip berechnen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 2 (2020, 2021), Haupt 1
- 1.4 Fehlende Anzahl aus der Gesamtzahl der Möglichkeiten bestimmen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 1 (2021), Haupt 1
- 1.5 Permutation mit Wiederholung berechnen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 1 (2026), Haupt 1
- 1.6 Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen (2; Operator „Zeigen Sie“, Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 1.7 Fehler finden (Fakultät statt Potenz, wo jede Kette mehrfach vergeben werden darf; nur die Fakultät der Gesamtzahl genommen und die gleichartigen Gruppen nicht herausdividiert; Produkt statt Potenz bei Zeichenfolgen mit Wiederholung; die Grundmenge falsch – alle Gäste statt der Kinder; durch die Summe statt durch das Produkt der bekannten Anzahlen geteilt; den Binomialkoeffizienten genommen, obwohl die Reihenfolge festgelegt wird) → didaktischer Typ, kein Prüfungstyp
- 1.8 Begründen (warum eine Anordnung jede Reihenfolge zählt und deshalb die Fakultät entsteht; warum bei Wiederholung die Zahl der Möglichkeiten je Platz gleich bleibt und eine Potenz entsteht) → didaktischer Typ, kein Prüfungstyp

**Einheit 2 · Auswahlen und Binomialkoeffizient** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 1 von 7 (Haupt 1) · FHR-Jahrgänge 8 von 8 (Haupt 8).

- 2.1 Kombination ohne Wiederholung berechnen (9; fhr) → wortgleich; GK 0 · LK 0 · FHR 7 (2019, 2020, 2021, 2022, 2023, 2024, 2025), Haupt 7
- 2.2 Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen (2) → wortgleich; GK 0 · LK 1 (2024), Haupt 1 · FHR 0
- 2.3 Anzahl der Kombinationen aus zwei getrennten Auswahlgruppen ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.4 Anzahl der Zahlenkombinationen mit einer vierfachen Ziffer aus drei Ziffern berechnen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.5 Kombination mit Wiederholung berechnen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 1 (2026), Haupt 1
- 2.6 Faktoren eines kombinatorischen Terms im Sachzusammenhang deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 2.7 Fehler finden (die Reihenfolge mitgezählt und eine Variation statt des Binomialkoeffizienten gerechnet – der häufigste Fehler des Themas; bei der Kombination mit Wiederholung die Potenz genommen; die Reihenfolge der beiden übrigen Ziffern vergessen; Wiederholung der Zusatzzeichen zugelassen oder die festen Buchstaben nicht ausgeschlossen; bei getrennten Gruppen die Fälle multipliziert statt addiert; einen Faktor des Terms als Restanzahl gedeutet) → didaktischer Typ, kein Prüfungstyp
- 2.8 Begründen (warum (n über k) gleich (n über n − k) ist – auswählen heißt liegen lassen; warum Auswahl mal Anordnung dasselbe ergibt wie die geordnete Auswahl) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Zählen mit Bedingungen und Wahrscheinlichkeitsterme** – Abitur-Jahrgänge GK 1 von 9 (Haupt 1) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.1 Anzahl der Sitzordnungen mit Abstandsbedingung berechnen (3) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 3.2 Anzahl der Zusammensetzungen mit Mengenbedingungen je Sorte bestimmen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.3 Kleinstes n, für das die Wahrscheinlichkeit lauter verschiedener Ergebnisse unter eine Schranke fällt, ermitteln (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.4 Auswahlen mit Abstandsbedingung aufzählen (2) → wortgleich; GK 1 (2024), Haupt 1 · LK 0 · FHR 0
- 3.5 Term für das Gegenereignis einer festen Häufigkeitsverteilung bei mehreren Würfen angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.6 Term für die Wahrscheinlichkeit aufstellen, dass jede Zahl mindestens einmal fällt (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.7 Fehler finden (eine Auswahl vergessen, weil immer mit dem ersten Platz begonnen wurde, oder eine benachbarte mitgezählt; die Muster gezählt und die Anordnungen der Personen oder Lieder vergessen; die Zuordnungen einer Zerlegung vergessen oder die Sorten als Potenz gezählt; die Anordnungen im Term weggelassen oder die Fakultät statt des Binomialkoeffizienten genommen; die Binomialverteilung für eine einzelne Zahl angesetzt, wo alle Zahlen zugleich verteilt sind; die Zahl der Folgen ohne Wiederholung als Potenz minus n geschrieben) → didaktischer Typ, kein Prüfungstyp
- 3.8 Begründen (warum die Muster erst aufgezählt und dann multipliziert werden; warum „jede Zahl mindestens einmal“ bei einem Wurf mehr als Zahlen genau eine Wiederholung heißt) → didaktischer Typ, kein Prüfungstyp

### einheiten (Sek-II-Teil eines Sek-I-Eintrags)

**Einheit 1 · Länge, Masse, Geld** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 7 von 8 (Haupt 5).

- 1.16 Streckenlänge im Koordinatensystem in Meter umrechnen (3; fhr – Abstände aus Schnittstellen und Extrempunkten mal Maßstab, in Zentimeter oder Meter) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2021, 2022, 2024, 2026), Haupt 3
- 1.17 Funktionswert im Sachzusammenhang deuten (2; fhr – die Stelle aus dem Sachtext, der Funktionswert als Höhe oder Länge in der Wirklichkeit) → wortgleich; GK 0 · LK 0 · FHR 2 (2024, 2025), Haupt 2
- 1.18 Funktionswert an einer Stelle berechnen (1; fhr – Radius verdoppeln, mit dem Maßstab in Zentimeter) → wortgleich; GK 0 · LK 0 · FHR 2 (2019, 2022), Haupt 2
- 1.19 Fehler finden (Längeneinheiten ohne Maßstab als Zentimeter übernommen; den Maßstab nicht angewendet; eine Höhe bis zur Achse statt bis zur unteren Begrenzung gemessen; die falsche Stelle eingesetzt) → didaktischer Typ, kein Prüfungstyp
- 1.20 Begründen (warum eine Längeneinheit des Koordinatensystems keine feste Einheit ist, sondern der Faktor im Text sie erst festlegt) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Flächen- und Volumeneinheiten** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 7 von 8 (Haupt 6).

- 3.15 Flächeninhalt einer zusammengesetzten Figur berechnen (1; fhr – Querschnitt in Flächeneinheiten und Volumen in Volumeneinheiten, beide mit dem Maßstab eins zu eins in Quadrat- und Kubikmeter) → wortgleich; GK 0 · LK 0 · FHR 1 (2021), Haupt 1
- 3.16 Fläche zwischen zwei Graphen berechnen (1; fhr – Operator „Weisen Sie nach“ für das Integral, dann Flächeneinheiten mit dem quadrierten Maßstab in Quadratzentimeter, verdoppelt für beide Seiten, in Quadratmeter) → wortgleich; GK 0 · LK 0 · FHR 7 (2019, 2020, 2021, 2022, 2023, 2024, 2026), Haupt 6
- 3.17 Fehler finden (den Maßstab beim Flächeninhalt nicht quadriert; beim Dreieck den Faktor ein halb vergessen) → didaktischer Typ, kein Prüfungstyp
- 3.18 Begründen (warum die Flächeneinheit mit dem Quadrat des Maßstabs umgerechnet wird – zwei Längen, wie bei der Umrechnungszahl hundert) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Mit Größen rechnen im Sachzusammenhang** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 1 von 8 (Haupt 1).

- 4.14 Gesamteinnahme aus Stückzahlen und Einzelpreisen berechnen (1; fhr – Stückzahlen je Preisstufe addieren, mit dem Preis multiplizieren, Teilbeträge summieren); dazu als Nebenleistungen der Sek-II-Zeilen anderer Einheiten die Druckkosten aus Fläche und Quadratmeterpreis und der Verschnitt als Anteil → wortgleich; GK 0 · LK 0 · FHR 1 (2020), Haupt 1
- 4.15 Fehler finden (die beiden Preise gemittelt und mit der Gesamtzahl multipliziert; den Verschnitt auf die Summe der Teile statt auf das Ausgangsstück bezogen) → didaktischer Typ, kein Prüfungstyp
- 4.16 Begründen (warum bei zwei Preisstufen nicht der Durchschnittspreis, sondern die gewichtete Summe zählt) → didaktischer Typ, kein Prüfungstyp

### lineare-gleichungssysteme (Sek-II-Teil eines Sek-I-Eintrags)

**Einheit 1 · Gleichungen mit zwei Variablen und grafisches Lösen** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 1.11 Eindeutigkeit der Lösung eines Gleichungssystems durch Einsetzen und Vergleich begründen (1; zwei nicht äquivalente Gleichungen, Teil A) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.12 Lösungsmenge eines Gleichungssystems mit zwei Variablen als Gerade zeichnen und eine Lösung angeben (1; identische Geraden, Teil A) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.13 Fehler finden (die Gerade mit dem falschen Vorzeichen der Steigung gezeichnet; nur eingesetzt und die Eindeutigkeit nicht begründet) → didaktischer Typ, kein Prüfungstyp
- 1.14 Begründen (warum zwei nicht äquivalente Gleichungen mit zwei Variablen höchstens eine gemeinsame Lösung haben) → didaktischer Typ, kein Prüfungstyp

**Einheit 3 · Additionsverfahren** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 3.11 Koeffizienten für ein unlösbares Gleichungssystem angeben und begründen (1; Vielfaches der linken Seite mit anderer rechter Seite, Widerspruch über den Additionsschritt, Teil A) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 3.12 Fehler finden (den Faktor mit falschem Vorzeichen gewählt, so dass das System eindeutig lösbar bleibt) → didaktischer Typ, kein Prüfungstyp
- 3.13 Begründen (warum eine falsche Aussage nach dem Addieren „keine Lösung“ heißt) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Sachaufgaben** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 4.14 Lineares Gleichungssystem im Sachzusammenhang interpretieren (1; Mischung dreier Säfte als Anteilssumme und Bilanz, Teil A) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.15 Fehler finden (die Variablen als Prozentzahlen der Zutaten statt als Anteile der Säfte gedeutet) → didaktischer Typ, kein Prüfungstyp
- 4.16 Begründen (warum die Summe der Anteile eins ergibt und die zweite Gleichung eine Bilanz ist) → didaktischer Typ, kein Prüfungstyp

**Einheit 5 · Drei Variablen und Lösungsvielfalt (Sek II)** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 0 von 8 (Haupt 0).

- 5.1 Gestaffeltes Gleichungssystem für einen Parameterwert lösen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.2 Lineares Gleichungssystem mit drei Variablen lösen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.3 Lösung eines unterbestimmten Gleichungssystems unter Zusatzbedingungen auswählen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.4 Lösungsanzahl eines gestaffelten Gleichungssystems mit Parameter durch Fallunterscheidung begründen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.5 Aussage über die Lösungsmenge eines Gleichungssystems mit Nichtnegativität nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.6 Lösung eines Gleichungssystems durch Einsetzen nachweisen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.7 Lösbarkeit eines Gleichungssystems mit Parameter beurteilen (2; Ermessen, siehe Offene Punkte) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.8 Lösungsanzahl eines erweiterten Gleichungssystems in Abhängigkeit vom Parameter angeben (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 5.9 Fehler finden (durch einen parameterabhängigen Koeffizienten geteilt, ohne den Fall null zu unterscheiden; nur den Sonderwert des Parameters geprüft und den allgemeinen Fall nicht ausgeführt; das System für eindeutig lösbar gehalten, obwohl eine Gleichung ein Vielfaches der anderen ist; die Ganzzahligkeit einer Variablen übersehen; für den passenden Parameterwert unendlich viele statt genau einer Lösung erwartet; ein Vorzeichen beim Rückwärtseinsetzen verfehlt; die Nichtnegativität der Variablen nicht herangezogen) → didaktischer Typ, kein Prüfungstyp
- 5.10 Begründen (warum ein Koeffizient null zwei verschiedene Fälle erzeugt; warum eine freie Variable eine ganze Schar von Lösungen liefert und Zusatzbedingungen daraus eine auswählen) → didaktischer Typ, kein Prüfungstyp

### daten (Sek-II-Teil eines Sek-I-Eintrags)

**Einheit 1 · Häufigkeiten** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 7 von 8 (Haupt 6).

- 1.16 Relative Häufigkeit berechnen (7; fhr – je Klasse oder Sorte, mit Häufigkeitsdiagramm als Nebentyp, Hochrechnung auf eine Gruppe) → wortgleich; GK 0 · LK 0 · FHR 6 (2019, 2020, 2022, 2024, 2025, 2026), Haupt 5
- 1.17 Relative Häufigkeit aus absoluten Häufigkeiten berechnen (1; aus der Restanzahl) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 1.18 Vierfeldertafel vervollständigen (1; fhr – absolute Anzahlen über Randsummen) → wortgleich; GK 0 · LK 0 · FHR 3 (2023, 2024, 2026), Haupt 3
- 1.19 Fehler finden (durch die Zahl der Werte statt durch die Gesamtzahl geteilt; beide Gruppen durch dieselbe Gesamtzahl; die Laplace-Wahrscheinlichkeit statt der beobachteten Häufigkeit) → didaktischer Typ, kein Prüfungstyp
- 1.20 Begründen (warum sich bei größerer Stichprobe die absoluten, nicht die relativen Häufigkeiten ändern) → didaktischer Typ, kein Prüfungstyp

**Einheit 4 · Kenngrößen** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 7 von 8 (Haupt 7).

- 4.16 Mittelwert aus Werteliste (5; fhr – stets mit der Standardabweichung als Nebentyp) → wortgleich; GK 0 · LK 0 · FHR 7 (2019, 2020, 2022, 2023, 2024, 2025, 2026), Haupt 4
- 4.17 Median aus Werteliste (3; fhr – mit Mittelwert und Standardabweichung, einmal mit Ausreißer-Deutung) → wortgleich; GK 0 · LK 0 · FHR 3 (2019, 2023, 2024), Haupt 3
- 4.18 Fehlenden Wert aus dem arithmetischen Mittel berechnen (1; Gesamtsumme minus Teilsumme, mit Zeiteinheiten) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 4.19 Fehler finden (den Median an der unsortierten Liste abgelesen; Minuten und Sekunden als Dezimalzahl gerechnet; die Standardabweichung mit dem falschen Nenner) → didaktischer Typ, kein Prüfungstyp
- 4.20 Begründen (warum ein Ausreißer den Mittelwert, nicht den Median verschiebt) → didaktischer Typ, kein Prüfungstyp

**Einheit 6 · Kenngrößen aus Häufigkeitstabellen und Klassen (Sek II)** – Abitur-Jahrgänge GK 0 von 9 (Haupt 0) · LK 0 von 7 (Haupt 0) · FHR-Jahrgänge 8 von 8 (Haupt 7).

- 6.1 Mittelwert aus Häufigkeitstabelle (7; fhr – mit Standardabweichung, Median oder Modalwert aus der Tabelle als Nebentypen, viermal aus Klassenmitten) → wortgleich; GK 0 · LK 0 · FHR 8, Haupt 7
- 6.2 Fehlenden Wert aus vorgegebenem Mittelwert bestimmen (2; fhr – unbekannter Preis, unbekannter Gruppenschnitt) → wortgleich; GK 0 · LK 0 · FHR 2 (2020, 2021), Haupt 2
- 6.3 Medianklasse aus klassierter Häufigkeitstabelle bestimmen (1; fhr) → wortgleich; GK 0 · LK 0 · FHR 3 (2019, 2020, 2024), Haupt 1
- 6.4 Medianklasse aus einem Säulendiagramm relativer Häufigkeiten begründen (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.5 Gewichtete Summe der Intervallgrenzen als Schranke des Mittelwerts deuten (1) → wortgleich; GK 0 · LK 0 · FHR 0 · nur Pool
- 6.6 Fehler finden (die Werte ungewichtet gemittelt; mit den Klassengrenzen statt den Klassenmitten gerechnet; die Klasse mit der größten Anzahl als Medianklasse genannt; die Abweichungen ohne Quadrat addiert; die Wurzel vergessen; beide Gruppen gleich gewichtet) → didaktischer Typ, kein Prüfungstyp
- 6.7 Begründen (warum die Klassenmitte alle Werte einer Klasse vertritt und der Mittelwert aus Klassen deshalb ein Näherungswert ist; warum bei klassierten Daten nur die Medianklasse bestimmbar ist) → didaktischer Typ, kein Prüfungstyp
