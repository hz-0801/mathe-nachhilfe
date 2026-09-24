# Ertrag je Typ – Profil msa
Stand 2026-09-24, Katalog auf Commit 875c5d8.

Gezählt werden die Zeilen aus msa-katalog-basis.csv und msa-katalog-kontext.csv. Hauptzeilen sind Zeilen, deren Feld typ dem Typ entspricht; Nebenzeilen sind Zeilen, in deren Pipe-getrenntem Feld typ_neben der Typ vorkommt, unabhängig vom Haupttyp der Zeile. Jede Zeile hat genau einen Haupttyp, aber keine, eine oder mehrere Nebentypen; punkte_haupt, basis/kontext und niveau_I/II/III zählen nur Hauptzeilen.

Gesamt: 418 Zeilen, 820 Punkte, 175 Typen mit Hauptzeile, 10 Typen nur als Nebentyp, 79 Typen ohne Vorkommen.

Erzeugt von `werkzeuge/ertrag.py` (v0.1) aus den msa-Katalogen und msa-typen.csv; abgeleitet, nie von Hand ändern.

## A Alle Typen nach Ertrag
Absteigend nach ertrag (punkte_haupt, bei Gleichstand jahre_gesamt, dann zeilen_haupt); bei vollständigem Gleichstand alphabetisch nach Typ. Typen mit Status „nicht in typen.csv“ haben kein Thema und keine Leitidee.

| Rang | Typ | punkte_haupt | punkte_anteil | zeilen_haupt | zeilen_neben | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | niveau_I | niveau_II | niveau_III | schritte_mittel | schritte_fehlt | thema | leitidee | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sinussatz Seite berechnen | 29 | 3,5 % | 9 | 0 | 9 | 9 | 2014 | 2025 | 0 | 9 | 0 | 6 | 3 | 3,2 | 0 | Sinus- und Kosinussatz | Größen und Messen | gültig |
| 2 | Baumdiagramm ergänzen | 25 | 3,0 % | 7 | 0 | 6 | 6 | 2014 | 2026 | 0 | 7 | 1 | 5 | 1 | 2,7 | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 3 | Seite im rechtwinkligen Dreieck berechnen | 23 | 2,8 % | 8 | 6 | 7 | 9 | 2014 | 2026 | 0 | 8 | 3 | 4 | 1 | 2,4 | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 4 | Wahrscheinlichkeit einstufig | 19 | 2,3 % | 13 | 3 | 8 | 9 | 2014 | 2026 | 4 | 9 | 11 | 1 | 1 | 1,2 | 0 | Wahrscheinlichkeit einstufig | Daten und Zufall | gültig |
| 5 | Arithmetisches Mittel berechnen | 17 | 2,1 % | 9 | 2 | 8 | 9 | 2015 | 2026 | 3 | 6 | 7 | 1 | 1 | 1,9 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 6 | Spannweite berechnen | 17 | 2,1 % | 8 | 0 | 7 | 7 | 2014 | 2026 | 1 | 7 | 7 | 1 | 0 | 1,6 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 7 | Gerade aus Gleichung zeichnen | 16 | 2,0 % | 6 | 0 | 5 | 5 | 2021 | 2026 | 0 | 6 | 5 | 1 | 0 | 1,3 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 8 | Pythagoras Kathete | 15 | 1,8 % | 7 | 0 | 5 | 5 | 2016 | 2026 | 0 | 7 | 5 | 2 | 0 | 2,1 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 9 | Flächeninhalt Dreieck berechnen | 14 | 1,7 % | 4 | 0 | 3 | 3 | 2015 | 2022 | 0 | 4 | 0 | 3 | 1 | 2,8 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 10 | Winkel im rechtwinkligen Dreieck berechnen | 13 | 1,6 % | 6 | 2 | 5 | 6 | 2019 | 2026 | 0 | 6 | 4 | 2 | 0 | 2,2 | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 11 | Wachstumstabelle ergänzen | 13 | 1,6 % | 6 | 0 | 5 | 5 | 2016 | 2026 | 0 | 6 | 4 | 2 | 0 | 2,2 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 12 | Punktprobe durchführen | 12 | 1,5 % | 6 | 2 | 5 | 7 | 2014 | 2026 | 1 | 5 | 5 | 1 | 0 | 1,7 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 13 | Gleichung im Sachzusammenhang deuten | 12 | 1,5 % | 4 | 1 | 4 | 5 | 2018 | 2024 | 0 | 4 | 1 | 3 | 0 | 1,0 | 0 | Lineare Gleichungssysteme | Gleichungen und Funktionen | gültig |
| 14 | Schnittpunkte Gerade und Parabel berechnen | 12 | 1,5 % | 3 | 0 | 3 | 3 | 2021 | 2024 | 0 | 3 | 0 | 3 | 0 | 4,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 15 | Bruchteil einer Fläche bestimmen | 11 | 1,3 % | 10 | 0 | 9 | 9 | 2014 | 2026 | 10 | 0 | 9 | 1 | 0 | 1,3 | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | gültig |
| 16 | Scheitelpunkt ablesen | 11 | 1,3 % | 9 | 1 | 8 | 9 | 2017 | 2026 | 1 | 8 | 8 | 1 | 0 | 0,6 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 17 | Prozentsatz berechnen | 11 | 1,3 % | 5 | 2 | 5 | 5 | 2014 | 2025 | 1 | 4 | 3 | 2 | 0 | 1,8 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 18 | Dauer aus Menge und Rate berechnen | 11 | 1,3 % | 4 | 0 | 4 | 4 | 2014 | 2024 | 0 | 4 | 2 | 2 | 0 | 2,5 | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 19 | Funktionswert berechnen | 10 | 1,2 % | 5 | 2 | 3 | 5 | 2016 | 2026 | 0 | 5 | 2 | 3 | 0 | 1,8 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 20 | Volumen Zylinder berechnen | 10 | 1,2 % | 5 | 1 | 4 | 5 | 2021 | 2026 | 0 | 5 | 5 | 0 | 0 | 1,6 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 21 | Wahrscheinlichkeit mehrstufig unabhängig | 10 | 1,2 % | 4 | 6 | 3 | 5 | 2014 | 2026 | 0 | 4 | 0 | 4 | 0 | 2,8 | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 22 | Lineares Gleichungssystem aufstellen | 10 | 1,2 % | 3 | 0 | 3 | 3 | 2016 | 2024 | 0 | 3 | 1 | 2 | 0 | 3,3 | 0 | Lineare Gleichungssysteme | Gleichungen und Funktionen | gültig |
| 23 | Prozentwert berechnen | 9 | 1,1 % | 8 | 2 | 6 | 6 | 2014 | 2026 | 6 | 2 | 8 | 0 | 0 | 1,2 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 24 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen | 9 | 1,1 % | 3 | 3 | 3 | 5 | 2015 | 2024 | 0 | 3 | 0 | 1 | 2 | 2,7 | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 25 | Pythagoras Hypotenuse | 9 | 1,1 % | 3 | 2 | 3 | 4 | 2015 | 2025 | 0 | 3 | 1 | 2 | 0 | 2,7 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 26 | Graph zu Wachstumsprozess zuordnen | 9 | 1,1 % | 3 | 0 | 2 | 2 | 2019 | 2026 | 0 | 3 | 0 | 0 | 3 | 0,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 27 | Prozentuale Veränderung berechnen | 8 | 1,0 % | 4 | 3 | 3 | 6 | 2016 | 2026 | 0 | 4 | 1 | 3 | 0 | 2,0 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 28 | Aussage zu Diagramm prüfen | 8 | 1,0 % | 3 | 0 | 3 | 3 | 2018 | 2022 | 0 | 3 | 0 | 2 | 1 | 1,3 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 29 | Netz eines Prismas vervollständigen | 8 | 1,0 % | 3 | 0 | 3 | 3 | 2014 | 2020 | 0 | 3 | 0 | 3 | 0 | 0,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 30 | Achseneinteilung wählen | 8 | 1,0 % | 2 | 1 | 2 | 3 | 2016 | 2021 | 0 | 2 | 0 | 2 | 0 | 2,0 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 31 | Tarife vergleichen | 8 | 1,0 % | 2 | 0 | 2 | 2 | 2016 | 2023 | 0 | 2 | 0 | 2 | 0 | 4,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 32 | Zahlen in verschiedenen Darstellungen vergleichen | 7 | 0,9 % | 7 | 0 | 7 | 7 | 2014 | 2023 | 7 | 0 | 7 | 0 | 0 | 1,4 | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | gültig |
| 33 | Term zu Sachtext angeben | 7 | 0,9 % | 5 | 0 | 5 | 5 | 2015 | 2023 | 4 | 1 | 4 | 1 | 0 | 0,4 | 0 | Terme umformen | Zahlen und Operationen | gültig |
| 34 | Nullstellen quadratische Funktion berechnen | 7 | 0,9 % | 2 | 1 | 2 | 3 | 2017 | 2025 | 0 | 2 | 0 | 2 | 0 | 3,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 35 | Gerade durch zwei Punkte zeichnen | 7 | 0,9 % | 2 | 0 | 2 | 2 | 2017 | 2025 | 0 | 2 | 0 | 2 | 0 | 3,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 36 | Zufallsgerät zu Wahrscheinlichkeit entwerfen | 6 | 0,7 % | 4 | 0 | 4 | 4 | 2018 | 2026 | 2 | 2 | 1 | 1 | 2 | 2,0 | 0 | Wahrscheinlichkeit einstufig | Daten und Zufall | gültig |
| 37 | Sektor im Kreisdiagramm zuordnen | 6 | 0,7 % | 2 | 2 | 2 | 4 | 2017 | 2024 | 0 | 2 | 0 | 2 | 0 | 2,0 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 38 | Anteilsaussage prüfen und korrigieren | 6 | 0,7 % | 3 | 0 | 3 | 3 | 2017 | 2023 | 0 | 3 | 0 | 3 | 0 | 1,3 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 39 | Symmetrieachsen bestimmen | 6 | 0,7 % | 3 | 0 | 3 | 3 | 2021 | 2025 | 2 | 1 | 2 | 1 | 0 | 1,0 | 0 | Symmetrie und Abbildungen | Raum und Form | gültig |
| 40 | Lineare Funktion aus Sachverhalt aufstellen | 6 | 0,7 % | 2 | 1 | 2 | 3 | 2016 | 2023 | 0 | 2 | 0 | 2 | 0 | 2,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 41 | Anzahl der Anordnungen bestimmen | 6 | 0,7 % | 2 | 0 | 2 | 2 | 2016 | 2017 | 0 | 2 | 0 | 1 | 1 | 2,5 | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 42 | Wachstumsfaktor aus Tabelle bestimmen | 6 | 0,7 % | 2 | 0 | 2 | 2 | 2018 | 2025 | 0 | 2 | 1 | 1 | 0 | 2,5 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 43 | Mantelfläche Kegel berechnen | 6 | 0,7 % | 2 | 0 | 1 | 1 | 2026 | 2026 | 0 | 2 | 0 | 2 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 44 | Winkelsumme im Dreieck anwenden | 5 | 0,6 % | 4 | 5 | 4 | 9 | 2015 | 2023 | 0 | 4 | 3 | 1 | 0 | 1,2 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 45 | Eigenschaften eines Graphen beurteilen | 5 | 0,6 % | 2 | 5 | 2 | 6 | 2018 | 2026 | 0 | 2 | 1 | 1 | 0 | 2,0 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 46 | Term zu Figur angeben | 5 | 0,6 % | 5 | 0 | 5 | 5 | 2014 | 2025 | 5 | 0 | 5 | 0 | 0 | 0,2 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 47 | Winkelfunktion Seitenverhältnis angeben | 5 | 0,6 % | 5 | 0 | 5 | 5 | 2017 | 2025 | 5 | 0 | 5 | 0 | 0 | 0,2 | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 48 | Zehnerpotenzschreibweise umwandeln | 5 | 0,6 % | 5 | 0 | 5 | 5 | 2015 | 2025 | 4 | 1 | 5 | 0 | 0 | 1,0 | 0 | Zehnerpotenzen und Näherungswerte | Zahlen und Operationen | gültig |
| 49 | Pythagoras Gleichung zuordnen | 5 | 0,6 % | 5 | 0 | 4 | 4 | 2017 | 2026 | 5 | 0 | 5 | 0 | 0 | 0,0 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 50 | Ergebnismenge aufzählen | 5 | 0,6 % | 3 | 1 | 3 | 4 | 2017 | 2025 | 1 | 2 | 3 | 0 | 0 | 1,3 | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 51 | Wertetabelle als Punkte darstellen | 5 | 0,6 % | 2 | 2 | 2 | 4 | 2016 | 2025 | 0 | 2 | 1 | 1 | 0 | 1,5 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 52 | Achsenskalierung aus Säule bestimmen | 5 | 0,6 % | 2 | 0 | 2 | 2 | 2018 | 2023 | 0 | 2 | 0 | 2 | 0 | 2,5 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 53 | Lineare Gleichung aus Sachverhalt aufstellen | 5 | 0,6 % | 2 | 0 | 2 | 2 | 2018 | 2020 | 0 | 2 | 0 | 2 | 0 | 3,0 | 0 | Lineare Gleichungen | Gleichungen und Funktionen | gültig |
| 54 | Minimum und Maximum ablesen | 5 | 0,6 % | 2 | 0 | 2 | 2 | 2014 | 2022 | 0 | 2 | 2 | 0 | 0 | 1,0 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 55 | Draufsicht maßstabsgerecht zeichnen | 5 | 0,6 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Maßstab | Größen und Messen | gültig |
| 56 | Strecke aus Teilstrecken berechnen | 4 | 0,5 % | 3 | 6 | 3 | 6 | 2014 | 2026 | 1 | 2 | 3 | 0 | 0 | 1,7 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 57 | Kreisfläche berechnen | 4 | 0,5 % | 2 | 3 | 2 | 5 | 2016 | 2024 | 0 | 2 | 2 | 0 | 0 | 1,5 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 58 | Exponentialfunktion aufstellen | 4 | 0,5 % | 2 | 2 | 2 | 4 | 2016 | 2026 | 0 | 2 | 1 | 1 | 0 | 1,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 59 | Termwert berechnen | 4 | 0,5 % | 4 | 0 | 3 | 3 | 2016 | 2026 | 4 | 0 | 4 | 0 | 0 | 2,0 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 60 | Winkel im Viereck berechnen | 4 | 0,5 % | 4 | 0 | 3 | 3 | 2021 | 2026 | 3 | 1 | 4 | 0 | 0 | 1,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 61 | Kosten aus Menge und Preis berechnen | 4 | 0,5 % | 3 | 2 | 2 | 3 | 2014 | 2026 | 0 | 3 | 1 | 2 | 0 | 1,7 | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 62 | Graph zu Tarif zuordnen | 4 | 0,5 % | 2 | 0 | 2 | 2 | 2016 | 2023 | 0 | 2 | 1 | 1 | 0 | 0,0 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 63 | Länge im Maßstab umrechnen | 4 | 0,5 % | 2 | 0 | 2 | 2 | 2015 | 2018 | 0 | 2 | 2 | 0 | 0 | 1,5 | 0 | Maßstab | Größen und Messen | gültig |
| 64 | Verdopplungs- oder Halbwertszeit bestimmen | 4 | 0,5 % | 2 | 0 | 2 | 2 | 2016 | 2020 | 0 | 2 | 1 | 1 | 0 | 1,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 65 | Wachstumsart begründen | 4 | 0,5 % | 2 | 0 | 2 | 2 | 2016 | 2018 | 0 | 2 | 0 | 2 | 0 | 0,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 66 | Fehler in Rechnung erklären und korrigieren | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 0 | 1 | 2,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 67 | Körper in Schrägbild skizzieren | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2024 | 2024 | 0 | 1 | 0 | 1 | 0 | 1,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 68 | Parabel zu Eigenschaften angeben | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 0 | 1 | 2,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 69 | Scheitelpunktform in Normalform umformen | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 0 | 0 | 1 | 4,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 70 | Streckenlänge aus Koordinaten berechnen | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2019 | 2019 | 0 | 1 | 0 | 1 | 0 | 4,0 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 71 | Verschnitt in Prozent berechnen | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 0 | 0 | 1 | 4,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 72 | Lineare Gleichung lösen | 3 | 0,4 % | 3 | 3 | 3 | 5 | 2018 | 2024 | 3 | 0 | 3 | 0 | 0 | 1,7 | 0 | Lineare Gleichungen | Gleichungen und Funktionen | gültig |
| 73 | Scheitelpunktform aufstellen | 3 | 0,4 % | 2 | 3 | 2 | 5 | 2016 | 2025 | 1 | 1 | 1 | 1 | 0 | 0,5 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 74 | Zeiteinheiten umrechnen | 3 | 0,4 % | 3 | 2 | 3 | 4 | 2015 | 2025 | 3 | 0 | 3 | 0 | 0 | 1,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 75 | Lineares Gleichungssystem lösen | 3 | 0,4 % | 1 | 3 | 1 | 4 | 2016 | 2024 | 0 | 1 | 0 | 1 | 0 | 4,0 | 0 | Lineare Gleichungssysteme | Gleichungen und Funktionen | gültig |
| 76 | Lösung durch Einsetzen prüfen | 3 | 0,4 % | 3 | 0 | 3 | 3 | 2018 | 2025 | 3 | 0 | 3 | 0 | 0 | 1,0 | 0 | Lineare Gleichungen | Gleichungen und Funktionen | gültig |
| 77 | Proportionale Zuordnung Dreisatz | 3 | 0,4 % | 3 | 0 | 3 | 3 | 2016 | 2023 | 3 | 0 | 3 | 0 | 0 | 1,7 | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 78 | Säulen- oder Balkendiagramm ergänzen | 3 | 0,4 % | 3 | 1 | 2 | 3 | 2020 | 2026 | 0 | 3 | 3 | 0 | 0 | 0,7 | 0 | Daten darstellen | Daten und Zufall | gültig |
| 79 | Verzerrung eines Diagramms erklären | 3 | 0,4 % | 2 | 1 | 2 | 3 | 2014 | 2026 | 0 | 2 | 0 | 0 | 2 | 0,0 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 80 | Wert nach prozentualer Erhöhung berechnen | 3 | 0,4 % | 2 | 1 | 2 | 3 | 2015 | 2024 | 1 | 1 | 1 | 1 | 0 | 1,5 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 81 | Geradengleichung aus zwei Punkten | 3 | 0,4 % | 1 | 2 | 1 | 3 | 2015 | 2025 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 82 | Kreisdiagramm zeichnen | 3 | 0,4 % | 1 | 2 | 1 | 3 | 2015 | 2025 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Daten darstellen | Daten und Zufall | gültig |
| 83 | Eigenschaft einer Figur zuordnen | 3 | 0,4 % | 3 | 0 | 2 | 2 | 2016 | 2026 | 3 | 0 | 3 | 0 | 0 | 0,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 84 | Größen vergleichen | 3 | 0,4 % | 3 | 0 | 2 | 2 | 2019 | 2026 | 3 | 0 | 3 | 0 | 0 | 1,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 85 | Endwert linearer Veränderung berechnen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2021 | 2022 | 0 | 2 | 2 | 0 | 0 | 2,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 86 | Graph nach Eigenschaft auswählen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2016 | 2019 | 1 | 1 | 2 | 0 | 0 | 0,5 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 87 | Median bestimmen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2015 | 2024 | 2 | 0 | 2 | 0 | 0 | 1,5 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 88 | Parabel verschieben | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2015 | 2017 | 1 | 1 | 1 | 1 | 0 | 1,5 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 89 | Rechteckseite aus Fläche berechnen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2014 | 2023 | 1 | 1 | 1 | 1 | 0 | 1,5 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 90 | Wert aus Diagramm ablesen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2015 | 2016 | 0 | 2 | 2 | 0 | 0 | 0,5 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 91 | Mantelfläche Zylinder als Netz skizzieren | 3 | 0,4 % | 1 | 1 | 1 | 2 | 2022 | 2023 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 92 | Gleichschenkliges Dreieck erkennen | 3 | 0,4 % | 2 | 0 | 1 | 1 | 2023 | 2023 | 1 | 1 | 1 | 1 | 0 | 1,5 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 93 | Argument zu Funktionswert berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 94 | Flächeninhalt zusammengesetzter Figur berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 95 | Geradengleichung zu Graph zuordnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2019 | 2019 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 96 | Höhe eines Zylinders aus Volumen berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 97 | Lage zweier Parabeln begründen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 0 | 1 | 0 | 0 | 1 | 0,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 98 | Lösbarkeit quadratischer Gleichung beurteilen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 0 | 0 | 1 | 3,0 | 0 | Quadratische Gleichungen | Gleichungen und Funktionen | gültig |
| 99 | Materialbedarf aus Fläche berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 100 | Netz eines Zylinders erkennen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 101 | Parabel an der y-Achse spiegeln | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 0 | 1 | 0 | 1 | 0 | 1,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 102 | Parabelgleichung zu Graph zuordnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 0 | 1 | 0 | 1,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 103 | Radius eines Zylinders aus Volumen berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 104 | Restfläche berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 105 | Restvolumen berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2024 | 2024 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 106 | Steigung in Prozent deuten | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 107 | Term zu Körper angeben | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 0 | 1 | 0 | 0,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 108 | Trapezhöhe aus Fläche berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 109 | Umfang Trapez berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 110 | Volumen Kegel und Zylinder vergleichen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 0 | 1 | 0 | 0 | 1 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 111 | Volumen Kugel berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 112 | Prozent und Anteil umwandeln | 2 | 0,2 % | 2 | 4 | 2 | 5 | 2014 | 2022 | 2 | 0 | 2 | 0 | 0 | 0,5 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 113 | Bruchteil einer Größe berechnen | 2 | 0,2 % | 2 | 0 | 2 | 2 | 2015 | 2018 | 2 | 0 | 2 | 0 | 0 | 1,5 | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | gültig |
| 114 | Exponent einer Potenz bestimmen | 2 | 0,2 % | 2 | 0 | 2 | 2 | 2020 | 2024 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Potenzen und Wurzeln | Zahlen und Operationen | gültig |
| 115 | Grundwert berechnen | 2 | 0,2 % | 2 | 0 | 2 | 2 | 2023 | 2025 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 116 | Körper aus Netz oder Schrägbild benennen | 2 | 0,2 % | 2 | 0 | 2 | 2 | 2017 | 2018 | 2 | 0 | 2 | 0 | 0 | 0,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 117 | Werte im Diagramm nach Bedingung auswählen | 2 | 0,2 % | 2 | 0 | 2 | 2 | 2016 | 2020 | 0 | 2 | 2 | 0 | 0 | 0,0 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 118 | Winkel an geschnittenen Parallelen bestimmen | 2 | 0,2 % | 2 | 0 | 2 | 2 | 2015 | 2020 | 2 | 0 | 2 | 0 | 0 | 0,5 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 119 | Winkel über Scheitel- oder Nebenwinkel bestimmen | 2 | 0,2 % | 2 | 0 | 2 | 2 | 2014 | 2019 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 120 | Zahl zu Bedingung angeben | 2 | 0,2 % | 2 | 0 | 2 | 2 | 2014 | 2015 | 2 | 0 | 2 | 0 | 0 | 0,5 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 121 | Nullstelle lineare Funktion berechnen | 2 | 0,2 % | 1 | 1 | 1 | 2 | 2021 | 2022 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 122 | Volumen Prisma berechnen | 2 | 0,2 % | 1 | 1 | 1 | 2 | 2014 | 2019 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 123 | Umfang Rechteck berechnen | 2 | 0,2 % | 2 | 0 | 1 | 1 | 2026 | 2026 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 124 | Volumen Würfel berechnen | 2 | 0,2 % | 2 | 0 | 1 | 1 | 2026 | 2026 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 125 | Wertetabelle einer Funktion zuordnen | 2 | 0,2 % | 2 | 0 | 1 | 1 | 2026 | 2026 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 126 | Fehlenden Prozentanteil ergänzen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 127 | Figur in Teilflächen zerlegen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 128 | Flächeninhalt Drachenviereck berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 129 | Flächeninhalt Trapez berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 130 | Gerade ohne gemeinsamen Punkt mit Parabel angeben | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 1 | 0 | 0,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 131 | Geschwindigkeit aus Weg und Zeit berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 132 | Gleichung zu Tarif zuordnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 133 | Grundseite aus Dreiecksfläche berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 134 | Guthabentabelle mit Zinsen ergänzen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Zinsrechnung | Zahlen und Operationen | gültig |
| 135 | Günstigste Preiskombination bestimmen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 0 | 0 | 1 | 4,0 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 136 | Kenngrößen einer Liste prüfen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 137 | Kreissektor Anteil berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 138 | Körperskizze beschriften | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 139 | Mantelfläche Prisma berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2019 | 2019 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 140 | Mantelfläche Zylinder berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 141 | Mantellinie Kegel bestimmen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 142 | Packungsanzahl in Quader bestimmen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 0 | 1 | 0 | 0 | 1 | 3,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 143 | Parabel aus Gleichung skizzieren | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2024 | 2024 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 144 | Rechten Winkel begründen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 145 | Streifendiagramm zeichnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Daten darstellen | Daten und Zufall | gültig |
| 146 | Volumen aus Masse und Dichte berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 147 | Volumenänderung bei doppeltem Radius begründen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 0 | 1 | 0 | 1,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 148 | Wahrscheinlichkeit über Gegenereignis berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 149 | Zeitpunkt für Schwellenwert bei Wachstum bestimmen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 150 | Zinseszins Endkapital berechnen | 2 | 0,2 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Zinsrechnung | Zahlen und Operationen | gültig |
| 151 | Winkel aus Teilwinkeln berechnen | 1 | 0,1 % | 1 | 2 | 1 | 3 | 2014 | 2018 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 152 | Nullstelle am Graphen ablesen | 1 | 0,1 % | 1 | 1 | 1 | 2 | 2015 | 2019 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 153 | Uhrzeit aus Startzeit und Dauer berechnen | 1 | 0,1 % | 1 | 1 | 1 | 2 | 2014 | 2021 | 1 | 0 | 1 | 0 | 0 | 2,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 154 | Anzahl der Dreiecke aus Punkten bestimmen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 155 | Ausgangswert aus Differenz berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 156 | Dreiecksungleichung anwenden | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 157 | Fehlenden Wert aus Mittelwert bestimmen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 1 | 0 | 0 | 1 | 0 | 2,0 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 158 | Figur nach Spiegelung benennen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Symmetrie und Abbildungen | Raum und Form | gültig |
| 159 | Gegenfläche im Würfelnetz bestimmen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 160 | Graph einer linearen Funktion erkennen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 161 | Große Zahl mit Zehnerpotenz multiplizieren | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Zehnerpotenzen und Näherungswerte | Zahlen und Operationen | gültig |
| 162 | Größte Zahl aus Ziffern bilden | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 163 | Kantenzahl eines Körpers angeben | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2019 | 2019 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 164 | Lage eines Punktes zu den Achsen erkennen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Koordinaten und Zeichnen | Raum und Form | gültig |
| 165 | Längeneinheit mit Faktor umrechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 166 | Mitte zweier Zahlen bestimmen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | gültig |
| 167 | Portionen aus Gesamtmenge berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 1 | 0 | 1 | 0 | 0 | 2,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 168 | Quadratseite aus Fläche berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 169 | Rechteckseite aus Umfang berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 1 | 0 | 1 | 0 | 0 | 2,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 170 | Relative Häufigkeit angeben | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 171 | Satz des Pythagoras formulieren | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 172 | Trigonometrische Gleichung nach Seite umstellen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 2,0 | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 173 | Vorzeichenregel anwenden | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 174 | Wurzel eines Quadrats berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Potenzen und Wurzeln | Zahlen und Operationen | gültig |
| 175 | y-Achsenabschnitt ablesen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2024 | 2024 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 176 | Behauptung prüfen | 0 | 0,0 % | 0 | 37 | 0 | 12 | 2014 | 2026 | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 177 | Mittelpunktswinkel berechnen | 0 | 0,0 % | 0 | 4 | 0 | 4 | 2015 | 2024 | 0 | 0 | 0 | 0 | 0 | – | 0 | Daten darstellen | Daten und Zufall | gültig |
| 178 | Flächeninhalt Rechteck berechnen | 0 | 0,0 % | 0 | 3 | 0 | 2 | 2017 | 2018 | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 179 | Parabel an der x-Achse spiegeln | 0 | 0,0 % | 0 | 2 | 0 | 2 | 2017 | 2018 | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 180 | Masse aus Volumen und Dichte berechnen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2019 | 2019 | 0 | 0 | 0 | 0 | 0 | – | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 181 | Schnittpunkt am Graphen ablesen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2023 | 2023 | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 182 | Steigung in Prozent berechnen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2025 | 2025 | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 183 | Verpackungsmaße aus Körpermaßen bestimmen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2024 | 2024 | 0 | 0 | 0 | 0 | 0 | – | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 184 | Veränderung des Mittelwerts begründen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2025 | 2025 | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | gültig |
| 185 | Volumen Kegel berechnen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2024 | 2024 | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 186 | Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 187 | Antiproportionale Zuordnung Dreisatz | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 188 | Anzahl Kombinationen nach dem Zählprinzip bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 189 | Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 190 | Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 191 | Anzahl gemeinsamer Punkte zweier Graphen begründen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 192 | Anzahl gleicher Rechtecke auf Fläche bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 193 | Aussage zu Logarithmusterm prüfen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 194 | Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 195 | Aussage über Bruchteile einer Größe prüfen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 196 | Binomische Formel anwenden | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Terme umformen | Zahlen und Operationen | gültig |
| 197 | Datenreihen anhand von Kenngrößen vergleichen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | gültig |
| 198 | Diagonale eines Drachenvierecks über Winkelfunktion berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 199 | Dreiecksart aus Koordinaten nachweisen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 200 | Eigenschaften trigonometrischer Funktionen vergleichen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrische Funktionen | Gleichungen und Funktionen | gültig |
| 201 | Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 202 | Ereignis zu Wahrscheinlichkeitsterm beschreiben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 203 | Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit einstufig | Daten und Zufall | gültig |
| 204 | Exponentialfunktion verschieben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 205 | Fehlenden Wert aus Spannweite bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | gültig |
| 206 | Flächeninhalt einer von Graphen begrenzten Figur berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 207 | Flächeninhalt eines Dreiecks aus Koordinaten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 208 | Flächeninhalt eines Dreiecks aus drei Seiten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 209 | Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 210 | Formel über Winkelfunktion herleiten | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 211 | Funktionswert über Symmetrie bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 212 | Ganzzahlige Anzahl aus Grenzwert bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Runden und Überschlag | Zahlen und Operationen | gültig |
| 213 | Gerade an der x-Achse spiegeln | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 214 | Gerade an der y-Achse spiegeln | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 215 | Geradengleichung aus Punkt und einem Parameter bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 216 | Geradengleichung einer Parallelen durch einen Punkt bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 217 | Gesamtmenge aus Pro-Kopf-Angabe berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 218 | Gleichung einer Senkrechten aufstellen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 219 | Gleichung zu Figur erläutern | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 220 | Gleichungskette im Sachzusammenhang erläutern | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 221 | Gleichverteilung der Trefferwahrscheinlichkeit begründen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 222 | Graph einer Exponentialfunktion an der y-Achse spiegeln | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 223 | Graph eines exponentiellen Vorgangs zeichnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 224 | Grundfläche im Netz kennzeichnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 225 | Grundkante aus Volumen berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 226 | Kegelhöhe aus Mantellinie und Radius berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 227 | Kosinussatz Seite berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Sinus- und Kosinussatz | Größen und Messen | gültig |
| 228 | Kosinussatz Winkel berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Sinus- und Kosinussatz | Größen und Messen | gültig |
| 229 | Kreisringmaß aus Fläche berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 230 | Kreisumfang berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 231 | Kugeldurchmesser aus Anordnung bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 232 | Kugelmaß aus Oberfläche berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 233 | Kugeloberfläche berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 234 | Körper im Schrägbild darstellen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 235 | Lage zweier Geraden bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 236 | Mantelfläche einer Pyramide berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 237 | Materialbedarf aus Längen berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 238 | Maße aus Netz im Maßstab ablesen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 239 | Modalwert bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | gültig |
| 240 | Neigungswinkel einer Geraden berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 241 | Parabelgleichung aus Nullstellen aufstellen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 242 | Parabelgleichung aus Scheitel und Punkt bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 243 | Parabeltransformation gegenüber der Normalparabel beschreiben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 244 | Parameter einer Exponentialfunktion bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 245 | Parameter einer Parabel aus Graph bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 246 | Parameter einer Wurzelfunktion aus einem Punkt bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 247 | Prozentanteil einer Rasterfläche markieren | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 248 | Scheitelpunkt einer Parabel rechnerisch nachweisen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 249 | Schnittpunkte zweier Parabeln berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 250 | Sinussatz Winkel berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Sinus- und Kosinussatz | Größen und Messen | gültig |
| 251 | Streckenlänge im Vieleck begründen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kongruenz und Konstruktion | Raum und Form | gültig |
| 252 | Streckenlänge über Ähnlichkeit berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ähnlichkeit und Strahlensätze | Raum und Form | gültig |
| 253 | Term durch Zusammenfassen gleichartiger Glieder vereinfachen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Terme umformen | Zahlen und Operationen | gültig |
| 254 | Term mit Klammern und Potenzen vereinfachen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Terme umformen | Zahlen und Operationen | gültig |
| 255 | Transformation einer trigonometrischen Funktion beschreiben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrische Funktionen | Gleichungen und Funktionen | gültig |
| 256 | Trigonometrische Funktionsgleichung zu Graph zuordnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrische Funktionen | Gleichungen und Funktionen | gültig |
| 257 | Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 258 | Umfang eines Dreiecks aus Koordinaten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 259 | Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 260 | Vieleck aus Seiten und Winkeln im Maßstab konstruieren | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kongruenz und Konstruktion | Raum und Form | gültig |
| 261 | Volumen zusammengesetzter Körper berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 262 | Wertebereich einer Funktion angeben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 263 | Winkel in zusammengesetzter Figur kennzeichnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 264 | Zeit aus Exponentialgleichung berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |

## B Typen je Thema
Themen nach Punktsumme (punkte_haupt ihrer Typen) absteigend; die Typen je Thema in Ertragsfolge.

### Quadratische Funktionen – 60 Punkte, 22 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Schnittpunkte Gerade und Parabel berechnen | 12 | 3 | 3 |
| 2 | Scheitelpunkt ablesen | 11 | 9 | 9 |
| 3 | Nullstellen quadratische Funktion berechnen | 7 | 2 | 3 |
| 4 | Parabel zu Eigenschaften angeben | 4 | 1 | 1 |
| 5 | Scheitelpunktform in Normalform umformen | 4 | 1 | 1 |
| 6 | Scheitelpunktform aufstellen | 3 | 2 | 5 |
| 7 | Parabel verschieben | 3 | 2 | 2 |
| 8 | Argument zu Funktionswert berechnen | 3 | 1 | 1 |
| 9 | Lage zweier Parabeln begründen | 3 | 1 | 1 |
| 10 | Parabel an der y-Achse spiegeln | 3 | 1 | 1 |
| 11 | Parabelgleichung zu Graph zuordnen | 3 | 1 | 1 |
| 12 | Gerade ohne gemeinsamen Punkt mit Parabel angeben | 2 | 1 | 1 |
| 13 | Parabel aus Gleichung skizzieren | 2 | 1 | 1 |
| 14 | Parabel an der x-Achse spiegeln | 0 | 0 | 2 |
| 15 | Anzahl gemeinsamer Punkte zweier Graphen begründen | 0 | 0 | 0 |
| 16 | Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen | 0 | 0 | 0 |
| 17 | Parabelgleichung aus Nullstellen aufstellen | 0 | 0 | 0 |
| 18 | Parabelgleichung aus Scheitel und Punkt bestimmen | 0 | 0 | 0 |
| 19 | Parabeltransformation gegenüber der Normalparabel beschreiben | 0 | 0 | 0 |
| 20 | Parameter einer Parabel aus Graph bestimmen | 0 | 0 | 0 |
| 21 | Scheitelpunkt einer Parabel rechnerisch nachweisen | 0 | 0 | 0 |
| 22 | Schnittpunkte zweier Parabeln berechnen | 0 | 0 | 0 |

### Flächeninhalt und Umfang – 56 Punkte, 22 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Flächeninhalt Dreieck berechnen | 14 | 4 | 3 |
| 2 | Term zu Figur angeben | 5 | 5 | 5 |
| 3 | Kreisfläche berechnen | 4 | 2 | 5 |
| 4 | Verschnitt in Prozent berechnen | 4 | 1 | 1 |
| 5 | Rechteckseite aus Fläche berechnen | 3 | 2 | 2 |
| 6 | Flächeninhalt zusammengesetzter Figur berechnen | 3 | 1 | 1 |
| 7 | Restfläche berechnen | 3 | 1 | 1 |
| 8 | Trapezhöhe aus Fläche berechnen | 3 | 1 | 1 |
| 9 | Umfang Trapez berechnen | 3 | 1 | 1 |
| 10 | Umfang Rechteck berechnen | 2 | 2 | 1 |
| 11 | Figur in Teilflächen zerlegen | 2 | 1 | 1 |
| 12 | Flächeninhalt Drachenviereck berechnen | 2 | 1 | 1 |
| 13 | Flächeninhalt Trapez berechnen | 2 | 1 | 1 |
| 14 | Grundseite aus Dreiecksfläche berechnen | 2 | 1 | 1 |
| 15 | Kreissektor Anteil berechnen | 2 | 1 | 1 |
| 16 | Quadratseite aus Fläche berechnen | 1 | 1 | 1 |
| 17 | Rechteckseite aus Umfang berechnen | 1 | 1 | 1 |
| 18 | Flächeninhalt Rechteck berechnen | 0 | 0 | 2 |
| 19 | Anzahl gleicher Rechtecke auf Fläche bestimmen | 0 | 0 | 0 |
| 20 | Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen | 0 | 0 | 0 |
| 21 | Kreisringmaß aus Fläche berechnen | 0 | 0 | 0 |
| 22 | Kreisumfang berechnen | 0 | 0 | 0 |

### Lineare Funktionen – 56 Punkte, 20 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Gerade aus Gleichung zeichnen | 16 | 6 | 5 |
| 2 | Tarife vergleichen | 8 | 2 | 2 |
| 3 | Gerade durch zwei Punkte zeichnen | 7 | 2 | 2 |
| 4 | Lineare Funktion aus Sachverhalt aufstellen | 6 | 2 | 3 |
| 5 | Geradengleichung aus zwei Punkten | 3 | 1 | 3 |
| 6 | Endwert linearer Veränderung berechnen | 3 | 2 | 2 |
| 7 | Graph nach Eigenschaft auswählen | 3 | 2 | 2 |
| 8 | Geradengleichung zu Graph zuordnen | 3 | 1 | 1 |
| 9 | Nullstelle lineare Funktion berechnen | 2 | 1 | 2 |
| 10 | Gleichung zu Tarif zuordnen | 2 | 1 | 1 |
| 11 | Nullstelle am Graphen ablesen | 1 | 1 | 2 |
| 12 | Graph einer linearen Funktion erkennen | 1 | 1 | 1 |
| 13 | y-Achsenabschnitt ablesen | 1 | 1 | 1 |
| 14 | Schnittpunkt am Graphen ablesen | 0 | 0 | 1 |
| 15 | Gerade an der x-Achse spiegeln | 0 | 0 | 0 |
| 16 | Gerade an der y-Achse spiegeln | 0 | 0 | 0 |
| 17 | Geradengleichung aus Punkt und einem Parameter bestimmen | 0 | 0 | 0 |
| 18 | Geradengleichung einer Parallelen durch einen Punkt bestimmen | 0 | 0 | 0 |
| 19 | Gleichung einer Senkrechten aufstellen | 0 | 0 | 0 |
| 20 | Lage zweier Geraden bestimmen | 0 | 0 | 0 |

### Funktionen allgemein – 46 Punkte, 10 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Punktprobe durchführen | 12 | 6 | 7 |
| 2 | Funktionswert berechnen | 10 | 5 | 5 |
| 3 | Achseneinteilung wählen | 8 | 2 | 3 |
| 4 | Eigenschaften eines Graphen beurteilen | 5 | 2 | 6 |
| 5 | Wertetabelle als Punkte darstellen | 5 | 2 | 4 |
| 6 | Graph zu Tarif zuordnen | 4 | 2 | 2 |
| 7 | Wertetabelle einer Funktion zuordnen | 2 | 2 | 1 |
| 8 | Funktionswert über Symmetrie bestimmen | 0 | 0 | 0 |
| 9 | Parameter einer Wurzelfunktion aus einem Punkt bestimmen | 0 | 0 | 0 |
| 10 | Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen | 0 | 0 | 0 |

### Kenngrößen – 46 Punkte, 11 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Arithmetisches Mittel berechnen | 17 | 9 | 9 |
| 2 | Spannweite berechnen | 17 | 8 | 7 |
| 3 | Minimum und Maximum ablesen | 5 | 2 | 2 |
| 4 | Median bestimmen | 3 | 2 | 2 |
| 5 | Kenngrößen einer Liste prüfen | 2 | 1 | 1 |
| 6 | Fehlenden Wert aus Mittelwert bestimmen | 1 | 1 | 1 |
| 7 | Relative Häufigkeit angeben | 1 | 1 | 1 |
| 8 | Veränderung des Mittelwerts begründen | 0 | 0 | 1 |
| 9 | Datenreihen anhand von Kenngrößen vergleichen | 0 | 0 | 0 |
| 10 | Fehlenden Wert aus Spannweite bestimmen | 0 | 0 | 0 |
| 11 | Modalwert bestimmen | 0 | 0 | 0 |

### Prozentrechnung – 46 Punkte, 12 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Prozentsatz berechnen | 11 | 5 | 5 |
| 2 | Prozentwert berechnen | 9 | 8 | 6 |
| 3 | Prozentuale Veränderung berechnen | 8 | 4 | 6 |
| 4 | Anteilsaussage prüfen und korrigieren | 6 | 3 | 3 |
| 5 | Wert nach prozentualer Erhöhung berechnen | 3 | 2 | 3 |
| 6 | Steigung in Prozent deuten | 3 | 1 | 1 |
| 7 | Prozent und Anteil umwandeln | 2 | 2 | 5 |
| 8 | Grundwert berechnen | 2 | 2 | 2 |
| 9 | Fehlenden Prozentanteil ergänzen | 2 | 1 | 1 |
| 10 | Steigung in Prozent berechnen | 0 | 0 | 1 |
| 11 | Gesamtmenge aus Pro-Kopf-Angabe berechnen | 0 | 0 | 0 |
| 12 | Prozentanteil einer Rasterfläche markieren | 0 | 0 | 0 |

### Wahrscheinlichkeit mehrstufig – 46 Punkte, 9 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Baumdiagramm ergänzen | 25 | 7 | 6 |
| 2 | Wahrscheinlichkeit mehrstufig unabhängig | 10 | 4 | 5 |
| 3 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen | 9 | 3 | 5 |
| 4 | Wahrscheinlichkeit über Gegenereignis berechnen | 2 | 1 | 1 |
| 5 | Behauptung prüfen | 0 | 0 | 12 |
| 6 | Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen | 0 | 0 | 0 |
| 7 | Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen | 0 | 0 | 0 |
| 8 | Ereignis zu Wahrscheinlichkeitsterm beschreiben | 0 | 0 | 0 |
| 9 | Gleichverteilung der Trefferwahrscheinlichkeit begründen | 0 | 0 | 0 |

### Volumen und Oberfläche – 44 Punkte, 20 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Volumen Zylinder berechnen | 10 | 5 | 5 |
| 2 | Mantelfläche Kegel berechnen | 6 | 2 | 1 |
| 3 | Höhe eines Zylinders aus Volumen berechnen | 3 | 1 | 1 |
| 4 | Radius eines Zylinders aus Volumen berechnen | 3 | 1 | 1 |
| 5 | Restvolumen berechnen | 3 | 1 | 1 |
| 6 | Term zu Körper angeben | 3 | 1 | 1 |
| 7 | Volumen Kegel und Zylinder vergleichen | 3 | 1 | 1 |
| 8 | Volumen Kugel berechnen | 3 | 1 | 1 |
| 9 | Volumen Prisma berechnen | 2 | 1 | 2 |
| 10 | Volumen Würfel berechnen | 2 | 2 | 1 |
| 11 | Mantelfläche Prisma berechnen | 2 | 1 | 1 |
| 12 | Mantelfläche Zylinder berechnen | 2 | 1 | 1 |
| 13 | Volumenänderung bei doppeltem Radius begründen | 2 | 1 | 1 |
| 14 | Volumen Kegel berechnen | 0 | 0 | 1 |
| 15 | Grundkante aus Volumen berechnen | 0 | 0 | 0 |
| 16 | Kugeldurchmesser aus Anordnung bestimmen | 0 | 0 | 0 |
| 17 | Kugelmaß aus Oberfläche berechnen | 0 | 0 | 0 |
| 18 | Kugeloberfläche berechnen | 0 | 0 | 0 |
| 19 | Mantelfläche einer Pyramide berechnen | 0 | 0 | 0 |
| 20 | Volumen zusammengesetzter Körper berechnen | 0 | 0 | 0 |

### Exponentialfunktionen und Wachstum – 42 Punkte, 15 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Wachstumstabelle ergänzen | 13 | 6 | 5 |
| 2 | Graph zu Wachstumsprozess zuordnen | 9 | 3 | 2 |
| 3 | Wachstumsfaktor aus Tabelle bestimmen | 6 | 2 | 2 |
| 4 | Exponentialfunktion aufstellen | 4 | 2 | 4 |
| 5 | Verdopplungs- oder Halbwertszeit bestimmen | 4 | 2 | 2 |
| 6 | Wachstumsart begründen | 4 | 2 | 2 |
| 7 | Zeitpunkt für Schwellenwert bei Wachstum bestimmen | 2 | 1 | 1 |
| 8 | Aussage zu Logarithmusterm prüfen | 0 | 0 | 0 |
| 9 | Exponentialfunktion verschieben | 0 | 0 | 0 |
| 10 | Gleichungskette im Sachzusammenhang erläutern | 0 | 0 | 0 |
| 11 | Graph einer Exponentialfunktion an der y-Achse spiegeln | 0 | 0 | 0 |
| 12 | Graph eines exponentiellen Vorgangs zeichnen | 0 | 0 | 0 |
| 13 | Parameter einer Exponentialfunktion bestimmen | 0 | 0 | 0 |
| 14 | Wertebereich einer Funktion angeben | 0 | 0 | 0 |
| 15 | Zeit aus Exponentialgleichung berechnen | 0 | 0 | 0 |

### Trigonometrie im rechtwinkligen Dreieck – 42 Punkte, 8 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Seite im rechtwinkligen Dreieck berechnen | 23 | 8 | 9 |
| 2 | Winkel im rechtwinkligen Dreieck berechnen | 13 | 6 | 6 |
| 3 | Winkelfunktion Seitenverhältnis angeben | 5 | 5 | 5 |
| 4 | Trigonometrische Gleichung nach Seite umstellen | 1 | 1 | 1 |
| 5 | Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen | 0 | 0 | 0 |
| 6 | Diagonale eines Drachenvierecks über Winkelfunktion berechnen | 0 | 0 | 0 |
| 7 | Formel über Winkelfunktion herleiten | 0 | 0 | 0 |
| 8 | Neigungswinkel einer Geraden berechnen | 0 | 0 | 0 |

### Satz des Pythagoras – 36 Punkte, 7 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Pythagoras Kathete | 15 | 7 | 5 |
| 2 | Pythagoras Hypotenuse | 9 | 3 | 4 |
| 3 | Pythagoras Gleichung zuordnen | 5 | 5 | 4 |
| 4 | Streckenlänge aus Koordinaten berechnen | 4 | 1 | 1 |
| 5 | Mantellinie Kegel bestimmen | 2 | 1 | 1 |
| 6 | Satz des Pythagoras formulieren | 1 | 1 | 1 |
| 7 | Kegelhöhe aus Mantellinie und Radius berechnen | 0 | 0 | 0 |

### Sinus- und Kosinussatz – 29 Punkte, 4 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Sinussatz Seite berechnen | 29 | 9 | 9 |
| 2 | Kosinussatz Seite berechnen | 0 | 0 | 0 |
| 3 | Kosinussatz Winkel berechnen | 0 | 0 | 0 |
| 4 | Sinussatz Winkel berechnen | 0 | 0 | 0 |

### Diagramme lesen und beurteilen – 27 Punkte, 6 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Aussage zu Diagramm prüfen | 8 | 3 | 3 |
| 2 | Sektor im Kreisdiagramm zuordnen | 6 | 2 | 4 |
| 3 | Achsenskalierung aus Säule bestimmen | 5 | 2 | 2 |
| 4 | Verzerrung eines Diagramms erklären | 3 | 2 | 3 |
| 5 | Wert aus Diagramm ablesen | 3 | 2 | 2 |
| 6 | Werte im Diagramm nach Bedingung auswählen | 2 | 2 | 2 |

### Ebene Figuren und Winkel – 27 Punkte, 18 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Winkelsumme im Dreieck anwenden | 5 | 4 | 9 |
| 2 | Strecke aus Teilstrecken berechnen | 4 | 3 | 6 |
| 3 | Winkel im Viereck berechnen | 4 | 4 | 3 |
| 4 | Eigenschaft einer Figur zuordnen | 3 | 3 | 2 |
| 5 | Gleichschenkliges Dreieck erkennen | 3 | 2 | 1 |
| 6 | Winkel an geschnittenen Parallelen bestimmen | 2 | 2 | 2 |
| 7 | Winkel über Scheitel- oder Nebenwinkel bestimmen | 2 | 2 | 2 |
| 8 | Rechten Winkel begründen | 2 | 1 | 1 |
| 9 | Winkel aus Teilwinkeln berechnen | 1 | 1 | 3 |
| 10 | Dreiecksungleichung anwenden | 1 | 1 | 1 |
| 11 | Dreiecksart aus Koordinaten nachweisen | 0 | 0 | 0 |
| 12 | Flächeninhalt einer von Graphen begrenzten Figur berechnen | 0 | 0 | 0 |
| 13 | Flächeninhalt eines Dreiecks aus Koordinaten berechnen | 0 | 0 | 0 |
| 14 | Flächeninhalt eines Dreiecks aus drei Seiten berechnen | 0 | 0 | 0 |
| 15 | Gleichung zu Figur erläutern | 0 | 0 | 0 |
| 16 | Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen | 0 | 0 | 0 |
| 17 | Umfang eines Dreiecks aus Koordinaten berechnen | 0 | 0 | 0 |
| 18 | Winkel in zusammengesetzter Figur kennzeichnen | 0 | 0 | 0 |

### Körper, Netze, Schrägbilder – 26 Punkte, 13 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Netz eines Prismas vervollständigen | 8 | 3 | 3 |
| 2 | Körper in Schrägbild skizzieren | 4 | 1 | 1 |
| 3 | Mantelfläche Zylinder als Netz skizzieren | 3 | 1 | 2 |
| 4 | Netz eines Zylinders erkennen | 3 | 1 | 1 |
| 5 | Körper aus Netz oder Schrägbild benennen | 2 | 2 | 2 |
| 6 | Körperskizze beschriften | 2 | 1 | 1 |
| 7 | Packungsanzahl in Quader bestimmen | 2 | 1 | 1 |
| 8 | Gegenfläche im Würfelnetz bestimmen | 1 | 1 | 1 |
| 9 | Kantenzahl eines Körpers angeben | 1 | 1 | 1 |
| 10 | Verpackungsmaße aus Körpermaßen bestimmen | 0 | 0 | 1 |
| 11 | Grundfläche im Netz kennzeichnen | 0 | 0 | 0 |
| 12 | Körper im Schrägbild darstellen | 0 | 0 | 0 |
| 13 | Maße aus Netz im Maßstab ablesen | 0 | 0 | 0 |

### Lineare Gleichungssysteme – 25 Punkte, 3 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Gleichung im Sachzusammenhang deuten | 12 | 4 | 5 |
| 2 | Lineares Gleichungssystem aufstellen | 10 | 3 | 3 |
| 3 | Lineares Gleichungssystem lösen | 3 | 1 | 4 |

### Wahrscheinlichkeit einstufig – 25 Punkte, 3 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Wahrscheinlichkeit einstufig | 19 | 13 | 9 |
| 2 | Zufallsgerät zu Wahrscheinlichkeit entwerfen | 6 | 4 | 4 |
| 3 | Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen | 0 | 0 | 0 |

### Brüche und Dezimalzahlen – 21 Punkte, 4 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Bruchteil einer Fläche bestimmen | 11 | 10 | 9 |
| 2 | Zahlen in verschiedenen Darstellungen vergleichen | 7 | 7 | 7 |
| 3 | Bruchteil einer Größe berechnen | 2 | 2 | 2 |
| 4 | Mitte zweier Zahlen bestimmen | 1 | 1 | 1 |

### Zuordnungen proportional und antiproportional – 20 Punkte, 5 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Dauer aus Menge und Rate berechnen | 11 | 4 | 4 |
| 2 | Kosten aus Menge und Preis berechnen | 4 | 3 | 3 |
| 3 | Proportionale Zuordnung Dreisatz | 3 | 3 | 3 |
| 4 | Geschwindigkeit aus Weg und Zeit berechnen | 2 | 1 | 1 |
| 5 | Antiproportionale Zuordnung Dreisatz | 0 | 0 | 0 |

### Einheiten umrechnen – 18 Punkte, 10 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Fehler in Rechnung erklären und korrigieren | 4 | 1 | 1 |
| 2 | Zeiteinheiten umrechnen | 3 | 3 | 4 |
| 3 | Größen vergleichen | 3 | 3 | 2 |
| 4 | Materialbedarf aus Fläche berechnen | 3 | 1 | 1 |
| 5 | Volumen aus Masse und Dichte berechnen | 2 | 1 | 1 |
| 6 | Uhrzeit aus Startzeit und Dauer berechnen | 1 | 1 | 2 |
| 7 | Längeneinheit mit Faktor umrechnen | 1 | 1 | 1 |
| 8 | Portionen aus Gesamtmenge berechnen | 1 | 1 | 1 |
| 9 | Masse aus Volumen und Dichte berechnen | 0 | 0 | 1 |
| 10 | Materialbedarf aus Längen berechnen | 0 | 0 | 0 |

### Zählen und Kombinatorik – 13 Punkte, 6 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Anzahl der Anordnungen bestimmen | 6 | 2 | 2 |
| 2 | Ergebnismenge aufzählen | 5 | 3 | 4 |
| 3 | Anzahl der Dreiecke aus Punkten bestimmen | 1 | 1 | 1 |
| 4 | Größte Zahl aus Ziffern bilden | 1 | 1 | 1 |
| 5 | Anzahl Kombinationen nach dem Zählprinzip bestimmen | 0 | 0 | 0 |
| 6 | Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen | 0 | 0 | 0 |

### Lineare Gleichungen – 11 Punkte, 3 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Lineare Gleichung aus Sachverhalt aufstellen | 5 | 2 | 2 |
| 2 | Lineare Gleichung lösen | 3 | 3 | 5 |
| 3 | Lösung durch Einsetzen prüfen | 3 | 3 | 3 |

### Rationale Zahlen rechnen – 10 Punkte, 6 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Termwert berechnen | 4 | 4 | 3 |
| 2 | Zahl zu Bedingung angeben | 2 | 2 | 2 |
| 3 | Günstigste Preiskombination bestimmen | 2 | 1 | 1 |
| 4 | Ausgangswert aus Differenz berechnen | 1 | 1 | 1 |
| 5 | Vorzeichenregel anwenden | 1 | 1 | 1 |
| 6 | Aussage über Bruchteile einer Größe prüfen | 0 | 0 | 0 |

### Maßstab – 9 Punkte, 2 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Draufsicht maßstabsgerecht zeichnen | 5 | 1 | 1 |
| 2 | Länge im Maßstab umrechnen | 4 | 2 | 2 |

### Daten darstellen – 8 Punkte, 4 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Säulen- oder Balkendiagramm ergänzen | 3 | 3 | 3 |
| 2 | Kreisdiagramm zeichnen | 3 | 1 | 3 |
| 3 | Streifendiagramm zeichnen | 2 | 1 | 1 |
| 4 | Mittelpunktswinkel berechnen | 0 | 0 | 4 |

### Symmetrie und Abbildungen – 7 Punkte, 2 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Symmetrieachsen bestimmen | 6 | 3 | 3 |
| 2 | Figur nach Spiegelung benennen | 1 | 1 | 1 |

### Terme umformen – 7 Punkte, 4 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Term zu Sachtext angeben | 7 | 5 | 5 |
| 2 | Binomische Formel anwenden | 0 | 0 | 0 |
| 3 | Term durch Zusammenfassen gleichartiger Glieder vereinfachen | 0 | 0 | 0 |
| 4 | Term mit Klammern und Potenzen vereinfachen | 0 | 0 | 0 |

### Zehnerpotenzen und Näherungswerte – 6 Punkte, 2 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Zehnerpotenzschreibweise umwandeln | 5 | 5 | 5 |
| 2 | Große Zahl mit Zehnerpotenz multiplizieren | 1 | 1 | 1 |

### Zinsrechnung – 4 Punkte, 2 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Guthabentabelle mit Zinsen ergänzen | 2 | 1 | 1 |
| 2 | Zinseszins Endkapital berechnen | 2 | 1 | 1 |

### Potenzen und Wurzeln – 3 Punkte, 2 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Exponent einer Potenz bestimmen | 2 | 2 | 2 |
| 2 | Wurzel eines Quadrats berechnen | 1 | 1 | 1 |

### Quadratische Gleichungen – 3 Punkte, 1 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Lösbarkeit quadratischer Gleichung beurteilen | 3 | 1 | 1 |

### Koordinaten und Zeichnen – 1 Punkte, 1 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Lage eines Punktes zu den Achsen erkennen | 1 | 1 | 1 |

### Kongruenz und Konstruktion – 0 Punkte, 2 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Streckenlänge im Vieleck begründen | 0 | 0 | 0 |
| 2 | Vieleck aus Seiten und Winkeln im Maßstab konstruieren | 0 | 0 | 0 |

### Runden und Überschlag – 0 Punkte, 1 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Ganzzahlige Anzahl aus Grenzwert bestimmen | 0 | 0 | 0 |

### Trigonometrische Funktionen – 0 Punkte, 3 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Eigenschaften trigonometrischer Funktionen vergleichen | 0 | 0 | 0 |
| 2 | Transformation einer trigonometrischen Funktion beschreiben | 0 | 0 | 0 |
| 3 | Trigonometrische Funktionsgleichung zu Graph zuordnen | 0 | 0 | 0 |

### Ähnlichkeit und Strahlensätze – 0 Punkte, 1 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Streckenlänge über Ähnlichkeit berechnen | 0 | 0 | 0 |

## C Verteilung (Hilfe für die Schwelle „selten“)
Nur Typen mit Hauptzeile (175). Perzentil im Rang-Sinn: sortierte Werte aufsteigend, Index floor(p/100 · n) – der Wert, unter dem rund p % der Typen liegen.

| Kennzahl | 10 % | 25 % | 50 % |
|---|---|---|---|
| punkte_haupt | 1 | 2 | 3 |
| jahre_gesamt | 1 | 1 | 2 |
| zeilen_haupt | 1 | 1 | 2 |

Typen mit Hauptzeile und jahre_gesamt ≤ 2: 111 von 175.

## D Typen ohne Hauptzeile
### Nur Nebentyp (10)
- Behauptung prüfen – Wahrscheinlichkeit mehrstufig
- Mittelpunktswinkel berechnen – Daten darstellen
- Flächeninhalt Rechteck berechnen – Flächeninhalt und Umfang
- Parabel an der x-Achse spiegeln – Quadratische Funktionen
- Masse aus Volumen und Dichte berechnen – Einheiten umrechnen
- Schnittpunkt am Graphen ablesen – Lineare Funktionen
- Steigung in Prozent berechnen – Prozentrechnung
- Verpackungsmaße aus Körpermaßen bestimmen – Körper, Netze, Schrägbilder
- Veränderung des Mittelwerts begründen – Kenngrößen
- Volumen Kegel berechnen – Volumen und Oberfläche

### Ohne Vorkommen (79)
- Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen – Wahrscheinlichkeit mehrstufig
- Antiproportionale Zuordnung Dreisatz – Zuordnungen proportional und antiproportional
- Anzahl Kombinationen nach dem Zählprinzip bestimmen – Zählen und Kombinatorik
- Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen – Zählen und Kombinatorik
- Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen – Wahrscheinlichkeit mehrstufig
- Anzahl gemeinsamer Punkte zweier Graphen begründen – Quadratische Funktionen
- Anzahl gleicher Rechtecke auf Fläche bestimmen – Flächeninhalt und Umfang
- Aussage zu Logarithmusterm prüfen – Exponentialfunktionen und Wachstum
- Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen – Trigonometrie im rechtwinkligen Dreieck
- Aussage über Bruchteile einer Größe prüfen – Rationale Zahlen rechnen
- Binomische Formel anwenden – Terme umformen
- Datenreihen anhand von Kenngrößen vergleichen – Kenngrößen
- Diagonale eines Drachenvierecks über Winkelfunktion berechnen – Trigonometrie im rechtwinkligen Dreieck
- Dreiecksart aus Koordinaten nachweisen – Ebene Figuren und Winkel
- Eigenschaften trigonometrischer Funktionen vergleichen – Trigonometrische Funktionen
- Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen – Quadratische Funktionen
- Ereignis zu Wahrscheinlichkeitsterm beschreiben – Wahrscheinlichkeit mehrstufig
- Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen – Wahrscheinlichkeit einstufig
- Exponentialfunktion verschieben – Exponentialfunktionen und Wachstum
- Fehlenden Wert aus Spannweite bestimmen – Kenngrößen
- Flächeninhalt einer von Graphen begrenzten Figur berechnen – Ebene Figuren und Winkel
- Flächeninhalt eines Dreiecks aus Koordinaten berechnen – Ebene Figuren und Winkel
- Flächeninhalt eines Dreiecks aus drei Seiten berechnen – Ebene Figuren und Winkel
- Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen – Flächeninhalt und Umfang
- Formel über Winkelfunktion herleiten – Trigonometrie im rechtwinkligen Dreieck
- Funktionswert über Symmetrie bestimmen – Funktionen allgemein
- Ganzzahlige Anzahl aus Grenzwert bestimmen – Runden und Überschlag
- Gerade an der x-Achse spiegeln – Lineare Funktionen
- Gerade an der y-Achse spiegeln – Lineare Funktionen
- Geradengleichung aus Punkt und einem Parameter bestimmen – Lineare Funktionen
- Geradengleichung einer Parallelen durch einen Punkt bestimmen – Lineare Funktionen
- Gesamtmenge aus Pro-Kopf-Angabe berechnen – Prozentrechnung
- Gleichung einer Senkrechten aufstellen – Lineare Funktionen
- Gleichung zu Figur erläutern – Ebene Figuren und Winkel
- Gleichungskette im Sachzusammenhang erläutern – Exponentialfunktionen und Wachstum
- Gleichverteilung der Trefferwahrscheinlichkeit begründen – Wahrscheinlichkeit mehrstufig
- Graph einer Exponentialfunktion an der y-Achse spiegeln – Exponentialfunktionen und Wachstum
- Graph eines exponentiellen Vorgangs zeichnen – Exponentialfunktionen und Wachstum
- Grundfläche im Netz kennzeichnen – Körper, Netze, Schrägbilder
- Grundkante aus Volumen berechnen – Volumen und Oberfläche
- Kegelhöhe aus Mantellinie und Radius berechnen – Satz des Pythagoras
- Kosinussatz Seite berechnen – Sinus- und Kosinussatz
- Kosinussatz Winkel berechnen – Sinus- und Kosinussatz
- Kreisringmaß aus Fläche berechnen – Flächeninhalt und Umfang
- Kreisumfang berechnen – Flächeninhalt und Umfang
- Kugeldurchmesser aus Anordnung bestimmen – Volumen und Oberfläche
- Kugelmaß aus Oberfläche berechnen – Volumen und Oberfläche
- Kugeloberfläche berechnen – Volumen und Oberfläche
- Körper im Schrägbild darstellen – Körper, Netze, Schrägbilder
- Lage zweier Geraden bestimmen – Lineare Funktionen
- Mantelfläche einer Pyramide berechnen – Volumen und Oberfläche
- Materialbedarf aus Längen berechnen – Einheiten umrechnen
- Maße aus Netz im Maßstab ablesen – Körper, Netze, Schrägbilder
- Modalwert bestimmen – Kenngrößen
- Neigungswinkel einer Geraden berechnen – Trigonometrie im rechtwinkligen Dreieck
- Parabelgleichung aus Nullstellen aufstellen – Quadratische Funktionen
- Parabelgleichung aus Scheitel und Punkt bestimmen – Quadratische Funktionen
- Parabeltransformation gegenüber der Normalparabel beschreiben – Quadratische Funktionen
- Parameter einer Exponentialfunktion bestimmen – Exponentialfunktionen und Wachstum
- Parameter einer Parabel aus Graph bestimmen – Quadratische Funktionen
- Parameter einer Wurzelfunktion aus einem Punkt bestimmen – Funktionen allgemein
- Prozentanteil einer Rasterfläche markieren – Prozentrechnung
- Scheitelpunkt einer Parabel rechnerisch nachweisen – Quadratische Funktionen
- Schnittpunkte zweier Parabeln berechnen – Quadratische Funktionen
- Sinussatz Winkel berechnen – Sinus- und Kosinussatz
- Streckenlänge im Vieleck begründen – Kongruenz und Konstruktion
- Streckenlänge über Ähnlichkeit berechnen – Ähnlichkeit und Strahlensätze
- Term durch Zusammenfassen gleichartiger Glieder vereinfachen – Terme umformen
- Term mit Klammern und Potenzen vereinfachen – Terme umformen
- Transformation einer trigonometrischen Funktion beschreiben – Trigonometrische Funktionen
- Trigonometrische Funktionsgleichung zu Graph zuordnen – Trigonometrische Funktionen
- Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen – Ebene Figuren und Winkel
- Umfang eines Dreiecks aus Koordinaten berechnen – Ebene Figuren und Winkel
- Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen – Funktionen allgemein
- Vieleck aus Seiten und Winkeln im Maßstab konstruieren – Kongruenz und Konstruktion
- Volumen zusammengesetzter Körper berechnen – Volumen und Oberfläche
- Wertebereich einer Funktion angeben – Exponentialfunktionen und Wachstum
- Winkel in zusammengesetzter Figur kennzeichnen – Ebene Figuren und Winkel
- Zeit aus Exponentialgleichung berechnen – Exponentialfunktionen und Wachstum
