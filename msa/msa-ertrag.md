# Ertrag je Typ – Profil msa
Stand 2026-09-23, Katalog auf Commit b699744.

Gezählt werden die Zeilen aus msa-katalog-basis.csv und msa-katalog-kontext.csv. Hauptzeilen sind Zeilen, deren Feld typ dem Typ entspricht; Nebenzeilen sind Zeilen, in deren Pipe-getrenntem Feld typ_neben der Typ vorkommt, unabhängig vom Haupttyp der Zeile. Jede Zeile hat genau einen Haupttyp, aber keine, eine oder mehrere Nebentypen; punkte_haupt, basis/kontext und niveau_I/II/III zählen nur Hauptzeilen.

Gesamt: 393 Zeilen, 780 Punkte, 175 Typen mit Hauptzeile, 10 Typen nur als Nebentyp, 108 Typen ohne Vorkommen.

Erzeugt von `werkzeuge/ertrag.py` (v0.1) aus den msa-Katalogen und msa-typen.csv; abgeleitet, nie von Hand ändern.

## A Alle Typen nach Ertrag
Absteigend nach ertrag (punkte_haupt, bei Gleichstand jahre_gesamt, dann zeilen_haupt); bei vollständigem Gleichstand alphabetisch nach Typ. Typen mit Status „nicht in typen.csv“ haben kein Thema und keine Leitidee.

| Rang | Typ | punkte_haupt | punkte_anteil | zeilen_haupt | zeilen_neben | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | niveau_I | niveau_II | niveau_III | schritte_mittel | schritte_fehlt | thema | leitidee | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sinussatz Seite berechnen | 29 | 3,7 % | 9 | 0 | 9 | 9 | 2014 | 2025 | 0 | 9 | 0 | 6 | 3 | 3,2 | 0 | Sinussatz | Größen und Messen | gültig |
| 2 | Seite im rechtwinkligen Dreieck berechnen | 23 | 2,9 % | 8 | 6 | 7 | 9 | 2014 | 2026 | 0 | 8 | 3 | 4 | 1 | 2,4 | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 3 | Baumdiagramm ergänzen | 21 | 2,7 % | 6 | 0 | 6 | 6 | 2014 | 2026 | 0 | 6 | 1 | 4 | 1 | 2,7 | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 4 | Wahrscheinlichkeit einstufig | 18 | 2,3 % | 12 | 3 | 8 | 9 | 2014 | 2026 | 4 | 8 | 10 | 1 | 1 | 1,2 | 0 | Wahrscheinlichkeit einstufig | Daten und Zufall | gültig |
| 5 | Spannweite berechnen | 16 | 2,1 % | 7 | 0 | 7 | 7 | 2014 | 2026 | 1 | 6 | 6 | 1 | 0 | 1,7 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 6 | Arithmetisches Mittel berechnen | 15 | 1,9 % | 8 | 2 | 8 | 9 | 2015 | 2026 | 3 | 5 | 6 | 1 | 1 | 1,9 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 7 | Gerade aus Gleichung zeichnen | 14 | 1,8 % | 5 | 0 | 5 | 5 | 2021 | 2026 | 0 | 5 | 4 | 1 | 0 | 1,4 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 8 | Flächeninhalt Dreieck berechnen | 14 | 1,8 % | 4 | 0 | 3 | 3 | 2015 | 2022 | 0 | 4 | 0 | 3 | 1 | 2,8 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 9 | Pythagoras Kathete | 13 | 1,7 % | 6 | 0 | 5 | 5 | 2016 | 2026 | 0 | 6 | 4 | 2 | 0 | 2,2 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 10 | Gleichung im Sachzusammenhang deuten | 12 | 1,5 % | 4 | 1 | 4 | 5 | 2018 | 2024 | 0 | 4 | 1 | 3 | 0 | 1,0 | 0 | Lineare Gleichungssysteme | Gleichungen und Funktionen | gültig |
| 11 | Schnittpunkte Gerade und Parabel berechnen | 12 | 1,5 % | 3 | 0 | 3 | 3 | 2021 | 2024 | 0 | 3 | 0 | 3 | 0 | 4,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 12 | Winkel im rechtwinkligen Dreieck berechnen | 11 | 1,4 % | 5 | 2 | 5 | 6 | 2019 | 2026 | 0 | 5 | 3 | 2 | 0 | 2,2 | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 13 | Prozentsatz berechnen | 11 | 1,4 % | 5 | 2 | 5 | 5 | 2014 | 2025 | 1 | 4 | 3 | 2 | 0 | 1,8 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 14 | Wachstumstabelle ergänzen | 11 | 1,4 % | 5 | 0 | 5 | 5 | 2016 | 2026 | 0 | 5 | 3 | 2 | 0 | 2,2 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 15 | Dauer aus Menge und Rate berechnen | 11 | 1,4 % | 4 | 0 | 4 | 4 | 2014 | 2024 | 0 | 4 | 2 | 2 | 0 | 2,5 | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 16 | Bruchteil einer Fläche bestimmen | 10 | 1,3 % | 9 | 0 | 9 | 9 | 2014 | 2026 | 9 | 0 | 8 | 1 | 0 | 1,3 | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | gültig |
| 17 | Scheitelpunkt ablesen | 10 | 1,3 % | 8 | 1 | 8 | 9 | 2017 | 2026 | 1 | 7 | 7 | 1 | 0 | 0,5 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 18 | Punktprobe durchführen | 10 | 1,3 % | 5 | 2 | 5 | 7 | 2014 | 2026 | 1 | 4 | 4 | 1 | 0 | 1,8 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 19 | Funktionswert berechnen | 10 | 1,3 % | 5 | 2 | 3 | 5 | 2016 | 2026 | 0 | 5 | 2 | 3 | 0 | 1,8 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 20 | Wahrscheinlichkeit mehrstufig unabhängig | 10 | 1,3 % | 4 | 5 | 3 | 5 | 2014 | 2026 | 0 | 4 | 0 | 4 | 0 | 2,8 | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 21 | Lineares Gleichungssystem aufstellen | 10 | 1,3 % | 3 | 0 | 3 | 3 | 2016 | 2024 | 0 | 3 | 1 | 2 | 0 | 3,3 | 0 | Lineare Gleichungssysteme | Gleichungen und Funktionen | gültig |
| 22 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen | 9 | 1,2 % | 3 | 3 | 3 | 5 | 2015 | 2024 | 0 | 3 | 0 | 1 | 2 | 2,7 | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 23 | Pythagoras Hypotenuse | 9 | 1,2 % | 3 | 2 | 3 | 4 | 2015 | 2025 | 0 | 3 | 1 | 2 | 0 | 2,7 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 24 | Prozentwert berechnen | 8 | 1,0 % | 7 | 2 | 6 | 6 | 2014 | 2026 | 5 | 2 | 7 | 0 | 0 | 1,3 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 25 | Volumen Zylinder berechnen | 8 | 1,0 % | 4 | 1 | 4 | 5 | 2021 | 2026 | 0 | 4 | 4 | 0 | 0 | 1,8 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 26 | Aussage zu Diagramm prüfen | 8 | 1,0 % | 3 | 0 | 3 | 3 | 2018 | 2022 | 0 | 3 | 0 | 2 | 1 | 1,3 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 27 | Netz eines Prismas vervollständigen | 8 | 1,0 % | 3 | 0 | 3 | 3 | 2014 | 2020 | 0 | 3 | 0 | 3 | 0 | 0,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 28 | Achseneinteilung wählen | 8 | 1,0 % | 2 | 1 | 2 | 3 | 2016 | 2021 | 0 | 2 | 0 | 2 | 0 | 2,0 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 29 | Tarife vergleichen | 8 | 1,0 % | 2 | 0 | 2 | 2 | 2016 | 2023 | 0 | 2 | 0 | 2 | 0 | 4,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 30 | Zahlen in verschiedenen Darstellungen vergleichen | 7 | 0,9 % | 7 | 0 | 7 | 7 | 2014 | 2023 | 7 | 0 | 7 | 0 | 0 | 1,4 | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | gültig |
| 31 | Term zu Sachtext angeben | 7 | 0,9 % | 5 | 0 | 5 | 5 | 2015 | 2023 | 4 | 1 | 4 | 1 | 0 | 0,4 | 0 | Terme umformen | Zahlen und Operationen | gültig |
| 32 | Nullstellen quadratische Funktion berechnen | 7 | 0,9 % | 2 | 1 | 2 | 3 | 2017 | 2025 | 0 | 2 | 0 | 2 | 0 | 3,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 33 | Gerade durch zwei Punkte zeichnen | 7 | 0,9 % | 2 | 0 | 2 | 2 | 2017 | 2025 | 0 | 2 | 0 | 2 | 0 | 3,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 34 | Prozentuale Veränderung berechnen | 6 | 0,8 % | 3 | 3 | 3 | 6 | 2016 | 2026 | 0 | 3 | 1 | 2 | 0 | 2,0 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 35 | Zufallsgerät zu Wahrscheinlichkeit entwerfen | 6 | 0,8 % | 4 | 0 | 4 | 4 | 2018 | 2026 | 2 | 2 | 1 | 1 | 2 | 2,0 | 0 | Wahrscheinlichkeit einstufig | Daten und Zufall | gültig |
| 36 | Sektor im Kreisdiagramm zuordnen | 6 | 0,8 % | 2 | 2 | 2 | 4 | 2017 | 2024 | 0 | 2 | 0 | 2 | 0 | 2,0 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 37 | Anteilsaussage prüfen und korrigieren | 6 | 0,8 % | 3 | 0 | 3 | 3 | 2017 | 2023 | 0 | 3 | 0 | 3 | 0 | 1,3 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 38 | Symmetrieachsen bestimmen | 6 | 0,8 % | 3 | 0 | 3 | 3 | 2021 | 2025 | 2 | 1 | 2 | 1 | 0 | 1,0 | 0 | Symmetrie und Abbildungen | Raum und Form | gültig |
| 39 | Lineare Funktion aus Sachverhalt aufstellen | 6 | 0,8 % | 2 | 1 | 2 | 3 | 2016 | 2023 | 0 | 2 | 0 | 2 | 0 | 2,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 40 | Anzahl der Anordnungen bestimmen | 6 | 0,8 % | 2 | 0 | 2 | 2 | 2016 | 2017 | 0 | 2 | 0 | 1 | 1 | 2,5 | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 41 | Graph zu Wachstumsprozess zuordnen | 6 | 0,8 % | 2 | 0 | 2 | 2 | 2019 | 2026 | 0 | 2 | 0 | 0 | 2 | 0,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 42 | Wachstumsfaktor aus Tabelle bestimmen | 6 | 0,8 % | 2 | 0 | 2 | 2 | 2018 | 2025 | 0 | 2 | 1 | 1 | 0 | 2,5 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 43 | Winkelsumme im Dreieck anwenden | 5 | 0,6 % | 4 | 5 | 4 | 9 | 2015 | 2023 | 0 | 4 | 3 | 1 | 0 | 1,2 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 44 | Eigenschaften eines Graphen beurteilen | 5 | 0,6 % | 2 | 4 | 2 | 6 | 2018 | 2026 | 0 | 2 | 1 | 1 | 0 | 2,0 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 45 | Term zu Figur angeben | 5 | 0,6 % | 5 | 0 | 5 | 5 | 2014 | 2025 | 5 | 0 | 5 | 0 | 0 | 0,2 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 46 | Winkelfunktion Seitenverhältnis angeben | 5 | 0,6 % | 5 | 0 | 5 | 5 | 2017 | 2025 | 5 | 0 | 5 | 0 | 0 | 0,2 | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 47 | Zehnerpotenzschreibweise umwandeln | 5 | 0,6 % | 5 | 0 | 5 | 5 | 2015 | 2025 | 4 | 1 | 5 | 0 | 0 | 1,0 | 0 | Zehnerpotenzen und Näherungswerte | Zahlen und Operationen | gültig |
| 48 | Ergebnismenge aufzählen | 5 | 0,6 % | 3 | 1 | 3 | 4 | 2017 | 2025 | 1 | 2 | 3 | 0 | 0 | 1,3 | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 49 | Wertetabelle als Punkte darstellen | 5 | 0,6 % | 2 | 2 | 2 | 4 | 2016 | 2025 | 0 | 2 | 1 | 1 | 0 | 1,5 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 50 | Achsenskalierung aus Säule bestimmen | 5 | 0,6 % | 2 | 0 | 2 | 2 | 2018 | 2023 | 0 | 2 | 0 | 2 | 0 | 2,5 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 51 | Lineare Gleichung aus Sachverhalt aufstellen | 5 | 0,6 % | 2 | 0 | 2 | 2 | 2018 | 2020 | 0 | 2 | 0 | 2 | 0 | 3,0 | 0 | Lineare Gleichungen | Gleichungen und Funktionen | gültig |
| 52 | Minimum und Maximum ablesen | 5 | 0,6 % | 2 | 0 | 2 | 2 | 2014 | 2022 | 0 | 2 | 2 | 0 | 0 | 1,0 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 53 | Draufsicht maßstabsgerecht zeichnen | 5 | 0,6 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Maßstab | Größen und Messen | gültig |
| 54 | Strecke aus Teilstrecken berechnen | 4 | 0,5 % | 3 | 6 | 3 | 6 | 2014 | 2026 | 1 | 2 | 3 | 0 | 0 | 1,7 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 55 | Kreisfläche berechnen | 4 | 0,5 % | 2 | 3 | 2 | 5 | 2016 | 2024 | 0 | 2 | 2 | 0 | 0 | 1,5 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 56 | Pythagoras Gleichung zuordnen | 4 | 0,5 % | 4 | 0 | 4 | 4 | 2017 | 2026 | 4 | 0 | 4 | 0 | 0 | 0,0 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 57 | Exponentialfunktion aufstellen | 4 | 0,5 % | 2 | 2 | 2 | 4 | 2016 | 2026 | 0 | 2 | 1 | 1 | 0 | 1,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 58 | Kosten aus Menge und Preis berechnen | 4 | 0,5 % | 3 | 1 | 2 | 3 | 2014 | 2026 | 0 | 3 | 1 | 2 | 0 | 1,7 | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 59 | Graph zu Tarif zuordnen | 4 | 0,5 % | 2 | 0 | 2 | 2 | 2016 | 2023 | 0 | 2 | 1 | 1 | 0 | 0,0 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 60 | Länge im Maßstab umrechnen | 4 | 0,5 % | 2 | 0 | 2 | 2 | 2015 | 2018 | 0 | 2 | 2 | 0 | 0 | 1,5 | 0 | Maßstab | Größen und Messen | gültig |
| 61 | Verdopplungs- oder Halbwertszeit bestimmen | 4 | 0,5 % | 2 | 0 | 2 | 2 | 2016 | 2020 | 0 | 2 | 1 | 1 | 0 | 1,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 62 | Wachstumsart begründen | 4 | 0,5 % | 2 | 0 | 2 | 2 | 2016 | 2018 | 0 | 2 | 0 | 2 | 0 | 0,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 63 | Fehler in Rechnung erklären und korrigieren | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 0 | 1 | 2,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 64 | Körper in Schrägbild skizzieren | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2024 | 2024 | 0 | 1 | 0 | 1 | 0 | 1,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 65 | Parabel zu Eigenschaften angeben | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 0 | 1 | 2,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 66 | Scheitelpunktform in Normalform umformen | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 0 | 0 | 1 | 4,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 67 | Streckenlänge aus Koordinaten berechnen | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2019 | 2019 | 0 | 1 | 0 | 1 | 0 | 4,0 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 68 | Verschnitt in Prozent berechnen | 4 | 0,5 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 0 | 0 | 1 | 4,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 69 | Lineare Gleichung lösen | 3 | 0,4 % | 3 | 3 | 3 | 5 | 2018 | 2024 | 3 | 0 | 3 | 0 | 0 | 1,7 | 0 | Lineare Gleichungen | Gleichungen und Funktionen | gültig |
| 70 | Scheitelpunktform aufstellen | 3 | 0,4 % | 2 | 3 | 2 | 5 | 2016 | 2025 | 1 | 1 | 1 | 1 | 0 | 0,5 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 71 | Zeiteinheiten umrechnen | 3 | 0,4 % | 3 | 2 | 3 | 4 | 2015 | 2025 | 3 | 0 | 3 | 0 | 0 | 1,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 72 | Lineares Gleichungssystem lösen | 3 | 0,4 % | 1 | 3 | 1 | 4 | 2016 | 2024 | 0 | 1 | 0 | 1 | 0 | 4,0 | 0 | Lineare Gleichungssysteme | Gleichungen und Funktionen | gültig |
| 73 | Lösung durch Einsetzen prüfen | 3 | 0,4 % | 3 | 0 | 3 | 3 | 2018 | 2025 | 3 | 0 | 3 | 0 | 0 | 1,0 | 0 | Lineare Gleichungen | Gleichungen und Funktionen | gültig |
| 74 | Proportionale Zuordnung Dreisatz | 3 | 0,4 % | 3 | 0 | 3 | 3 | 2016 | 2023 | 3 | 0 | 3 | 0 | 0 | 1,7 | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 75 | Termwert berechnen | 3 | 0,4 % | 3 | 0 | 3 | 3 | 2016 | 2026 | 3 | 0 | 3 | 0 | 0 | 2,0 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 76 | Winkel im Viereck berechnen | 3 | 0,4 % | 3 | 0 | 3 | 3 | 2021 | 2026 | 2 | 1 | 3 | 0 | 0 | 1,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 77 | Verzerrung eines Diagramms erklären | 3 | 0,4 % | 2 | 1 | 2 | 3 | 2014 | 2026 | 0 | 2 | 0 | 0 | 2 | 0,0 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 78 | Wert nach prozentualer Erhöhung berechnen | 3 | 0,4 % | 2 | 1 | 2 | 3 | 2015 | 2024 | 1 | 1 | 1 | 1 | 0 | 1,5 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 79 | Geradengleichung aus zwei Punkten | 3 | 0,4 % | 1 | 2 | 1 | 3 | 2015 | 2025 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 80 | Kreisdiagramm zeichnen | 3 | 0,4 % | 1 | 2 | 1 | 3 | 2015 | 2025 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Daten darstellen | Daten und Zufall | gültig |
| 81 | Endwert linearer Veränderung berechnen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2021 | 2022 | 0 | 2 | 2 | 0 | 0 | 2,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 82 | Graph nach Eigenschaft auswählen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2016 | 2019 | 1 | 1 | 2 | 0 | 0 | 0,5 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 83 | Median bestimmen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2015 | 2024 | 2 | 0 | 2 | 0 | 0 | 1,5 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 84 | Parabel verschieben | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2015 | 2017 | 1 | 1 | 1 | 1 | 0 | 1,5 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 85 | Rechteckseite aus Fläche berechnen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2014 | 2023 | 1 | 1 | 1 | 1 | 0 | 1,5 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 86 | Wert aus Diagramm ablesen | 3 | 0,4 % | 2 | 0 | 2 | 2 | 2015 | 2016 | 0 | 2 | 2 | 0 | 0 | 0,5 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 87 | Mantelfläche Zylinder als Netz skizzieren | 3 | 0,4 % | 1 | 1 | 1 | 2 | 2022 | 2023 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 88 | Gleichschenkliges Dreieck erkennen | 3 | 0,4 % | 2 | 0 | 1 | 1 | 2023 | 2023 | 1 | 1 | 1 | 1 | 0 | 1,5 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 89 | Argument zu Funktionswert berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 90 | Flächeninhalt zusammengesetzter Figur berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 91 | Geradengleichung zu Graph zuordnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2019 | 2019 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 92 | Höhe eines Zylinders aus Volumen berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 93 | Lage zweier Parabeln begründen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 0 | 1 | 0 | 0 | 1 | 0,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 94 | Lösbarkeit quadratischer Gleichung beurteilen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 0 | 0 | 1 | 3,0 | 0 | Quadratische Gleichungen | Gleichungen und Funktionen | gültig |
| 95 | Mantelfläche Kegel berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 96 | Materialbedarf aus Fläche berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 97 | Netz eines Zylinders erkennen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 98 | Parabel an der y-Achse spiegeln | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 0 | 1 | 0 | 1 | 0 | 1,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 99 | Parabelgleichung zu Graph zuordnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 0 | 1 | 0 | 1,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 100 | Radius eines Zylinders aus Volumen berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 101 | Restfläche berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 102 | Restvolumen berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2024 | 2024 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 103 | Steigung in Prozent deuten | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 104 | Term zu Körper angeben | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 0 | 1 | 0 | 0,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 105 | Trapezhöhe aus Fläche berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 106 | Umfang Trapez berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 107 | Volumen Kegel und Zylinder vergleichen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 0 | 1 | 0 | 0 | 1 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 108 | Volumen Kugel berechnen | 3 | 0,4 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 109 | Prozent und Anteil umwandeln | 2 | 0,3 % | 2 | 4 | 2 | 5 | 2014 | 2022 | 2 | 0 | 2 | 0 | 0 | 0,5 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 110 | Säulen- oder Balkendiagramm ergänzen | 2 | 0,3 % | 2 | 1 | 2 | 3 | 2020 | 2026 | 0 | 2 | 2 | 0 | 0 | 0,5 | 0 | Daten darstellen | Daten und Zufall | gültig |
| 111 | Bruchteil einer Größe berechnen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2015 | 2018 | 2 | 0 | 2 | 0 | 0 | 1,5 | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | gültig |
| 112 | Eigenschaft einer Figur zuordnen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2016 | 2026 | 2 | 0 | 2 | 0 | 0 | 0,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 113 | Exponent einer Potenz bestimmen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2020 | 2024 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Potenzen und Wurzeln | Zahlen und Operationen | gültig |
| 114 | Grundwert berechnen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2023 | 2025 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 115 | Größen vergleichen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2019 | 2026 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 116 | Körper aus Netz oder Schrägbild benennen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2017 | 2018 | 2 | 0 | 2 | 0 | 0 | 0,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 117 | Werte im Diagramm nach Bedingung auswählen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2016 | 2020 | 0 | 2 | 2 | 0 | 0 | 0,0 | 0 | Diagramme lesen und beurteilen | Daten und Zufall | gültig |
| 118 | Winkel an geschnittenen Parallelen bestimmen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2015 | 2020 | 2 | 0 | 2 | 0 | 0 | 0,5 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 119 | Winkel über Scheitel- oder Nebenwinkel bestimmen | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2014 | 2019 | 2 | 0 | 2 | 0 | 0 | 1,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 120 | Zahl zu Bedingung angeben | 2 | 0,3 % | 2 | 0 | 2 | 2 | 2014 | 2015 | 2 | 0 | 2 | 0 | 0 | 0,5 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 121 | Nullstelle lineare Funktion berechnen | 2 | 0,3 % | 1 | 1 | 1 | 2 | 2021 | 2022 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 122 | Volumen Prisma berechnen | 2 | 0,3 % | 1 | 1 | 1 | 2 | 2014 | 2019 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 123 | Fehlenden Prozentanteil ergänzen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 124 | Figur in Teilflächen zerlegen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 125 | Flächeninhalt Drachenviereck berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 126 | Flächeninhalt Trapez berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2023 | 2023 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 127 | Gerade ohne gemeinsamen Punkt mit Parabel angeben | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 1 | 0 | 0,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 128 | Geschwindigkeit aus Weg und Zeit berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | gültig |
| 129 | Gleichung zu Tarif zuordnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 130 | Grundseite aus Dreiecksfläche berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 131 | Guthabentabelle mit Zinsen ergänzen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Zinsrechnung | Zahlen und Operationen | gültig |
| 132 | Günstigste Preiskombination bestimmen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 0 | 0 | 1 | 4,0 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 133 | Kenngrößen einer Liste prüfen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 134 | Kreissektor Anteil berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 135 | Körperskizze beschriften | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 136 | Mantelfläche Prisma berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2019 | 2019 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 137 | Mantelfläche Zylinder berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 1 | 0 | 0 | 2,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 138 | Mantellinie Kegel bestimmen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 139 | Packungsanzahl in Quader bestimmen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 0 | 1 | 0 | 0 | 1 | 3,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 140 | Parabel aus Gleichung skizzieren | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2024 | 2024 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 141 | Rechten Winkel begründen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 142 | Streifendiagramm zeichnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Daten darstellen | Daten und Zufall | gültig |
| 143 | Volumen aus Masse und Dichte berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 144 | Volumenänderung bei doppeltem Radius begründen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2021 | 2021 | 0 | 1 | 0 | 1 | 0 | 1,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 145 | Wahrscheinlichkeit über Gegenereignis berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 146 | Zeitpunkt für Schwellenwert bei Wachstum bestimmen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 0 | 1 | 0 | 1 | 0 | 3,0 | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | gültig |
| 147 | Zinseszins Endkapital berechnen | 2 | 0,3 % | 1 | 0 | 1 | 1 | 2014 | 2014 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Zinsrechnung | Zahlen und Operationen | gültig |
| 148 | Winkel aus Teilwinkeln berechnen | 1 | 0,1 % | 1 | 2 | 1 | 3 | 2014 | 2018 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 149 | Nullstelle am Graphen ablesen | 1 | 0,1 % | 1 | 1 | 1 | 2 | 2015 | 2019 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 150 | Uhrzeit aus Startzeit und Dauer berechnen | 1 | 0,1 % | 1 | 1 | 1 | 2 | 2014 | 2021 | 1 | 0 | 1 | 0 | 0 | 2,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 151 | Anzahl der Dreiecke aus Punkten bestimmen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 0 | 1 | 0 | 2,0 | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 152 | Ausgangswert aus Differenz berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2017 | 2017 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 153 | Dreiecksungleichung anwenden | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Ebene Figuren und Winkel | Raum und Form | gültig |
| 154 | Fehlenden Wert aus Mittelwert bestimmen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 1 | 0 | 0 | 1 | 0 | 2,0 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 155 | Figur nach Spiegelung benennen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Symmetrie und Abbildungen | Raum und Form | gültig |
| 156 | Gegenfläche im Würfelnetz bestimmen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 157 | Graph einer linearen Funktion erkennen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2025 | 2025 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 158 | Große Zahl mit Zehnerpotenz multiplizieren | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Zehnerpotenzen und Näherungswerte | Zahlen und Operationen | gültig |
| 159 | Größte Zahl aus Ziffern bilden | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 1 | 0 | 0 | 0,0 | 0 | Zählen und Kombinatorik | Daten und Zufall | gültig |
| 160 | Kantenzahl eines Körpers angeben | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2019 | 2019 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 161 | Lage eines Punktes zu den Achsen erkennen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Koordinaten und Zeichnen | Raum und Form | gültig |
| 162 | Längeneinheit mit Faktor umrechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2016 | 2016 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 163 | Mitte zweier Zahlen bestimmen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | gültig |
| 164 | Portionen aus Gesamtmenge berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 1 | 0 | 1 | 0 | 0 | 2,0 | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 165 | Quadratseite aus Fläche berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 166 | Rechteckseite aus Umfang berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2018 | 2018 | 1 | 0 | 1 | 0 | 0 | 2,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 167 | Relative Häufigkeit angeben | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 0 | 1 | 1 | 0 | 0 | 1,0 | 0 | Kenngrößen | Daten und Zufall | gültig |
| 168 | Satz des Pythagoras formulieren | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2022 | 2022 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Satz des Pythagoras | Größen und Messen | gültig |
| 169 | Trigonometrische Gleichung nach Seite umstellen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2020 | 2020 | 1 | 0 | 1 | 0 | 0 | 2,0 | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | gültig |
| 170 | Umfang Rechteck berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 171 | Volumen Würfel berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 172 | Vorzeichenregel anwenden | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 1 | 0 | 1 | 0 | 0 | 0,0 | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | gültig |
| 173 | Wertetabelle einer Funktion zuordnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2026 | 2026 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Funktionen allgemein | Gleichungen und Funktionen | gültig |
| 174 | Wurzel eines Quadrats berechnen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2015 | 2015 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Potenzen und Wurzeln | Zahlen und Operationen | gültig |
| 175 | y-Achsenabschnitt ablesen | 1 | 0,1 % | 1 | 0 | 1 | 1 | 2024 | 2024 | 1 | 0 | 1 | 0 | 0 | 1,0 | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 176 | Behauptung prüfen | 0 | 0,0 % | 0 | 36 | 0 | 12 | 2014 | 2026 | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | gültig |
| 177 | Mittelpunktswinkel berechnen | 0 | 0,0 % | 0 | 4 | 0 | 4 | 2015 | 2024 | 0 | 0 | 0 | 0 | 0 | – | 0 | Daten darstellen | Daten und Zufall | gültig |
| 178 | Flächeninhalt Rechteck berechnen | 0 | 0,0 % | 0 | 3 | 0 | 2 | 2017 | 2018 | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | gültig |
| 179 | Parabel an der x-Achse spiegeln | 0 | 0,0 % | 0 | 2 | 0 | 2 | 2017 | 2018 | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | gültig |
| 180 | Masse aus Volumen und Dichte berechnen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2019 | 2019 | 0 | 0 | 0 | 0 | 0 | – | 0 | Einheiten umrechnen | Größen und Messen | gültig |
| 181 | Schnittpunkt am Graphen ablesen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2023 | 2023 | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | gültig |
| 182 | Steigung in Prozent berechnen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2025 | 2025 | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | gültig |
| 183 | Verpackungsmaße aus Körpermaßen bestimmen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2024 | 2024 | 0 | 0 | 0 | 0 | 0 | – | 0 | Körper, Netze, Schrägbilder | Raum und Form | gültig |
| 184 | Veränderung des Mittelwerts begründen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2025 | 2025 | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | gültig |
| 185 | Volumen Kegel berechnen | 0 | 0,0 % | 0 | 1 | 0 | 1 | 2024 | 2024 | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | gültig |
| 186 | Anstieg einer linearen Funktion aus Punkt und y-Achsenabschnitt berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | neu |
| 187 | Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | neu |
| 188 | Anteil einer unterteilten Kreisfläche bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Brüche und Dezimalzahlen | Zahlen und Operationen | neu |
| 189 | Antiproportionale Zuordnung Dreisatz | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Zuordnungen proportional und antiproportional | Gleichungen und Funktionen | neu |
| 190 | Anzahl Kombinationen nach dem Zählprinzip bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Zählen und Kombinatorik | Daten und Zufall | neu |
| 191 | Anzahl Objekte aus Masse und Tragfähigkeit berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 192 | Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Zählen und Kombinatorik | Daten und Zufall | neu |
| 193 | Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | neu |
| 194 | Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | neu |
| 195 | Aussage über eine mehrfach gebrochene Streckenteilung prüfen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Rationale Zahlen rechnen | Zahlen und Operationen | neu |
| 196 | Aussage über einen Logarithmusterm als Abstand zur y-Achse prüfen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 197 | Binomische Formel anwenden | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Terme umformen | Zahlen und Operationen | neu |
| 198 | Datenreihen anhand von Kenngrößen vergleichen und begründen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | neu |
| 199 | Dreieck aus Koordinaten als gleichschenklig-rechtwinklig nachweisen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 200 | Durchmesser einer Halbkugel aus der Oberfläche berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 201 | Eigenschaften trigonometrischer Funktionen vergleichen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrische Funktionen | Gleichungen und Funktionen | neu |
| 202 | Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 203 | Ereignis zu Wahrscheinlichkeitsterm beschreiben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | neu |
| 204 | Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit einstufig | Daten und Zufall | neu |
| 205 | Exponentialfunktion vertikal verschieben und Schnittpunkt mit der y-Achse angeben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 206 | Farbmenge aus Fläche und Ergiebigkeit berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Einheiten umrechnen | Größen und Messen | neu |
| 207 | Fehlende Schnittpunkte zweier Funktionen über Wertebereiche begründen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 208 | Fehlenden Wert aus Spannweite bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | neu |
| 209 | Fläche zweier Mantelflächen eines Prismas mit trapezförmiger Grundfläche berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 210 | Flächenberechnung eines Vielecks anhand einer vorgegebenen Gleichung erläutern | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 211 | Flächeninhalt eines Drachenvierecks aus Diagonalen berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | neu |
| 212 | Flächeninhalt eines Dreiecks aus Koordinaten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 213 | Flächeninhalt eines Dreiecks aus drei Seiten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 214 | Flächeninhalt eines Vierecks aus den Achsenschnittpunkten zweier Funktionsgraphen berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 215 | Flächeninhalt eines aus vier kongruenten rechtwinkligen Dreiecken zusammengesetzten Vierecks berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | neu |
| 216 | Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | neu |
| 217 | Formel für die Tiefe eines Kegels aus Durchmesser und Öffnungswinkel herleiten | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | neu |
| 218 | Funktionswerte einer Parabel im Sachkontext berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 219 | Gerade an der x-Achse spiegeln | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | neu |
| 220 | Gerade an der y-Achse spiegeln | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | neu |
| 221 | Geradengleichung aus Steigung und Punkt bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | neu |
| 222 | Geradengleichung einer Parallelen durch einen Punkt bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | neu |
| 223 | Gesamtmenge aus Pro-Kopf-Angabe, Anteil und Einwohnerzahl berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | neu |
| 224 | Gleich große oder doppelt so große Winkel in einer aus kongruenten Dreiecken zusammengesetzten Figur kennzeichnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 225 | Gleichung einer Senkrechten aufstellen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | neu |
| 226 | Gleichverteilung der Trefferwahrscheinlichkeit begründen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | neu |
| 227 | Graph einer Exponentialfunktion an der y-Achse spiegeln | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 228 | Graph einer trigonometrischen Funktion durch Streckung und Verschiebung beschreiben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrische Funktionen | Gleichungen und Funktionen | neu |
| 229 | Graph eines exponentiellen Vorgangs zeichnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 230 | Grundfläche eines Prismas im Körpernetz kennzeichnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Körper, Netze, Schrägbilder | Raum und Form | neu |
| 231 | Grundstücksbreiten aus einem in Teilflächen zerlegten Trapez bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ähnlichkeit und Strahlensätze | Raum und Form | neu |
| 232 | Höhe eines Drachenvierecks aus geteiltem Winkel und Diagonalen berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | neu |
| 233 | Innendurchmesser eines Kreisrings aus Flächeninhalt und Außendurchmesser berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | neu |
| 234 | Kantenlänge einer quadratischen Grundfläche aus Volumen berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 235 | Kantensumme eines Quaders mit Seitenlängen in Abhängigkeit von der Höhe berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 236 | Kegelhöhe aus Mantellinie und Radius berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Satz des Pythagoras | Größen und Messen | neu |
| 237 | Kreisumfang berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | neu |
| 238 | Kugeldurchmesser aus Anzahl nebeneinanderliegender Kugeln bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 239 | Kugeloberfläche berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 240 | Körper im Schrägbild darstellen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Körper, Netze, Schrägbilder | Raum und Form | neu |
| 241 | Lage zweier Geraden bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | neu |
| 242 | Lineare Funktion aus Steigung und Schnittbedingung bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Lineare Funktionen | Gleichungen und Funktionen | neu |
| 243 | Länge auf der Mantellinie eines Kegels bei Teilfüllung über Ähnlichkeit bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ähnlichkeit und Strahlensätze | Raum und Form | neu |
| 244 | Mantelfläche einer Pyramide berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 245 | Masse eines zusammengesetzten Körpers berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 246 | Materialbedarf aus Längen berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Einheiten umrechnen | Größen und Messen | neu |
| 247 | Maximale Anzahl rechteckiger Objekte auf einer Fläche bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Flächeninhalt und Umfang | Größen und Messen | neu |
| 248 | Maximale ganzzahlige Menge aus Grenzwert berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Runden und Überschlag | Zahlen und Operationen | neu |
| 249 | Maße eines Körpers aus einem bemaßten Netz im Maßstab ablesen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Körper, Netze, Schrägbilder | Raum und Form | neu |
| 250 | Mehrere Kenngrößen zweier Datenreihen vergleichend bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | neu |
| 251 | Modalwert bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kenngrößen | Daten und Zufall | neu |
| 252 | Neigungswinkel einer Geraden berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | neu |
| 253 | Parabelgleichung aus Scheitel und Punkt bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 254 | Parabelgleichung aus Spannweite und Höhe eines Bogens bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 255 | Parabelgleichung aus zwei Nullstellen aufstellen und Nullstellen bestätigen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 256 | Parabeltransformation gegenüber der Normalparabel beschreiben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 257 | Parameter einer Exponentialfunktion aus Graph bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 258 | Parameter einer Exponentialfunktion aus einer Wertetabelle bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 259 | Parameter einer Parabel aus Graph bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 260 | Parameter einer Wurzelfunktion aus einem Punkt bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Funktionen allgemein | Gleichungen und Funktionen | neu |
| 261 | Prozentanteil einer Rasterfläche markieren | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | neu |
| 262 | Prozentuale Abweichung einer Modellfläche von der tatsächlichen Fläche berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | neu |
| 263 | Prozentuale Abweichung eines Werts von einem Vergleichswert berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | neu |
| 264 | Prozentualen Zuwachs aus Anfangs- und Endwert berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Prozentrechnung | Zahlen und Operationen | neu |
| 265 | Sachaufgabe zu einer Gleichungskette formulieren | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 266 | Scheitelpunkt einer Parabel rechnerisch nachweisen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 267 | Schnittpunktanzahl von Graphen begründen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 268 | Schnittpunktgleichung zweier Parabeln herleiten | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |
| 269 | Seite im allgemeinen Dreieck über Kosinussatz berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Sinussatz | Größen und Messen | neu |
| 270 | Seite im rechtwinkligen Dreieck aus Winkel und Kathete berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | neu |
| 271 | Sinussatz Winkel berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Sinussatz | Größen und Messen | neu |
| 272 | Streckenlänge über ein konstruiertes Parallelogramm im Vieleck begründen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kongruenz und Konstruktion | Raum und Form | neu |
| 273 | Symmetrie einer geraden Funktion zur Bestimmung eines Funktionswertes ohne Rechnung nutzen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Funktionen allgemein | Gleichungen und Funktionen | neu |
| 274 | Term durch Zusammenfassen gleichartiger Glieder vereinfachen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Terme umformen | Zahlen und Operationen | neu |
| 275 | Term mit Klammern und Potenzen vereinfachen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Terme umformen | Zahlen und Operationen | neu |
| 276 | Transportanzahl aus Volumen und Masse berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 277 | Trapezfläche im Koordinatensystem aus Funktionsgraph und Geraden berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 278 | Trapezhöhe über den aus einem angrenzenden Dreieck übertragenen Winkel berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ähnlichkeit und Strahlensätze | Raum und Form | neu |
| 279 | Trigonometrische Funktionsgleichung zu Graph zuordnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrische Funktionen | Gleichungen und Funktionen | neu |
| 280 | Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 281 | Umfang eines Dreiecks aus Koordinaten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 282 | Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Funktionen allgemein | Gleichungen und Funktionen | neu |
| 283 | Vieleck aus Seiten und Winkeln im Maßstab konstruieren | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Kongruenz und Konstruktion | Raum und Form | neu |
| 284 | Volumen eines aus Kegel und Halbkugel zusammengesetzten Körpers mit Nebenbedingung berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Volumen und Oberfläche | Größen und Messen | neu |
| 285 | Wahrscheinlichkeit für die Position des ersten Treffers berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Wahrscheinlichkeit mehrstufig | Daten und Zufall | neu |
| 286 | Wertebereich einer Funktion angeben | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 287 | Wertetabelle auf Exponentialfunktion prüfen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 288 | Winkel als Differenz zweier Teilwinkel in einem zusammengesetzten rechtwinkligen Dreieck nachweisen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Ebene Figuren und Winkel | Raum und Form | neu |
| 289 | Winkel eines Drachenvierecks aus Diagonalenabschnitten berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Trigonometrie im rechtwinkligen Dreieck | Größen und Messen | neu |
| 290 | Winkel im allgemeinen Dreieck über Kosinussatz berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Sinussatz | Größen und Messen | neu |
| 291 | Winkel im allgemeinen Dreieck über Sinussatz berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Sinussatz | Größen und Messen | neu |
| 292 | Zeit aus Exponentialgleichung berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Exponentialfunktionen und Wachstum | Gleichungen und Funktionen | neu |
| 293 | x-Werte einer quadratischen Funktion zu gegebenem Funktionswert berechnen | 0 | 0,0 % | 0 | 0 | 0 | 0 | – | – | 0 | 0 | 0 | 0 | 0 | – | 0 | Quadratische Funktionen | Gleichungen und Funktionen | neu |

## B Typen je Thema
Themen nach Punktsumme (punkte_haupt ihrer Typen) absteigend; die Typen je Thema in Ertragsfolge.

### Quadratische Funktionen – 59 Punkte, 26 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Schnittpunkte Gerade und Parabel berechnen | 12 | 3 | 3 |
| 2 | Scheitelpunkt ablesen | 10 | 8 | 9 |
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
| 15 | Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen | 0 | 0 | 0 |
| 16 | Fehlende Schnittpunkte zweier Funktionen über Wertebereiche begründen | 0 | 0 | 0 |
| 17 | Funktionswerte einer Parabel im Sachkontext berechnen | 0 | 0 | 0 |
| 18 | Parabelgleichung aus Scheitel und Punkt bestimmen | 0 | 0 | 0 |
| 19 | Parabelgleichung aus Spannweite und Höhe eines Bogens bestimmen | 0 | 0 | 0 |
| 20 | Parabelgleichung aus zwei Nullstellen aufstellen und Nullstellen bestätigen | 0 | 0 | 0 |
| 21 | Parabeltransformation gegenüber der Normalparabel beschreiben | 0 | 0 | 0 |
| 22 | Parameter einer Parabel aus Graph bestimmen | 0 | 0 | 0 |
| 23 | Scheitelpunkt einer Parabel rechnerisch nachweisen | 0 | 0 | 0 |
| 24 | Schnittpunktanzahl von Graphen begründen | 0 | 0 | 0 |
| 25 | Schnittpunktgleichung zweier Parabeln herleiten | 0 | 0 | 0 |
| 26 | x-Werte einer quadratischen Funktion zu gegebenem Funktionswert berechnen | 0 | 0 | 0 |

### Flächeninhalt und Umfang – 55 Punkte, 24 Typen

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
| 10 | Figur in Teilflächen zerlegen | 2 | 1 | 1 |
| 11 | Flächeninhalt Drachenviereck berechnen | 2 | 1 | 1 |
| 12 | Flächeninhalt Trapez berechnen | 2 | 1 | 1 |
| 13 | Grundseite aus Dreiecksfläche berechnen | 2 | 1 | 1 |
| 14 | Kreissektor Anteil berechnen | 2 | 1 | 1 |
| 15 | Quadratseite aus Fläche berechnen | 1 | 1 | 1 |
| 16 | Rechteckseite aus Umfang berechnen | 1 | 1 | 1 |
| 17 | Umfang Rechteck berechnen | 1 | 1 | 1 |
| 18 | Flächeninhalt Rechteck berechnen | 0 | 0 | 2 |
| 19 | Flächeninhalt eines Drachenvierecks aus Diagonalen berechnen | 0 | 0 | 0 |
| 20 | Flächeninhalt eines aus vier kongruenten rechtwinkligen Dreiecken zusammengesetzten Vierecks berechnen | 0 | 0 | 0 |
| 21 | Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen | 0 | 0 | 0 |
| 22 | Innendurchmesser eines Kreisrings aus Flächeninhalt und Außendurchmesser berechnen | 0 | 0 | 0 |
| 23 | Kreisumfang berechnen | 0 | 0 | 0 |
| 24 | Maximale Anzahl rechteckiger Objekte auf einer Fläche bestimmen | 0 | 0 | 0 |

### Lineare Funktionen – 54 Punkte, 22 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Gerade aus Gleichung zeichnen | 14 | 5 | 5 |
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
| 15 | Anstieg einer linearen Funktion aus Punkt und y-Achsenabschnitt berechnen | 0 | 0 | 0 |
| 16 | Gerade an der x-Achse spiegeln | 0 | 0 | 0 |
| 17 | Gerade an der y-Achse spiegeln | 0 | 0 | 0 |
| 18 | Geradengleichung aus Steigung und Punkt bestimmen | 0 | 0 | 0 |
| 19 | Geradengleichung einer Parallelen durch einen Punkt bestimmen | 0 | 0 | 0 |
| 20 | Gleichung einer Senkrechten aufstellen | 0 | 0 | 0 |
| 21 | Lage zweier Geraden bestimmen | 0 | 0 | 0 |
| 22 | Lineare Funktion aus Steigung und Schnittbedingung bestimmen | 0 | 0 | 0 |

### Funktionen allgemein – 43 Punkte, 10 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Punktprobe durchführen | 10 | 5 | 7 |
| 2 | Funktionswert berechnen | 10 | 5 | 5 |
| 3 | Achseneinteilung wählen | 8 | 2 | 3 |
| 4 | Eigenschaften eines Graphen beurteilen | 5 | 2 | 6 |
| 5 | Wertetabelle als Punkte darstellen | 5 | 2 | 4 |
| 6 | Graph zu Tarif zuordnen | 4 | 2 | 2 |
| 7 | Wertetabelle einer Funktion zuordnen | 1 | 1 | 1 |
| 8 | Parameter einer Wurzelfunktion aus einem Punkt bestimmen | 0 | 0 | 0 |
| 9 | Symmetrie einer geraden Funktion zur Bestimmung eines Funktionswertes ohne Rechnung nutzen | 0 | 0 | 0 |
| 10 | Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen | 0 | 0 | 0 |

### Kenngrößen – 43 Punkte, 12 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Spannweite berechnen | 16 | 7 | 7 |
| 2 | Arithmetisches Mittel berechnen | 15 | 8 | 9 |
| 3 | Minimum und Maximum ablesen | 5 | 2 | 2 |
| 4 | Median bestimmen | 3 | 2 | 2 |
| 5 | Kenngrößen einer Liste prüfen | 2 | 1 | 1 |
| 6 | Fehlenden Wert aus Mittelwert bestimmen | 1 | 1 | 1 |
| 7 | Relative Häufigkeit angeben | 1 | 1 | 1 |
| 8 | Veränderung des Mittelwerts begründen | 0 | 0 | 1 |
| 9 | Datenreihen anhand von Kenngrößen vergleichen und begründen | 0 | 0 | 0 |
| 10 | Fehlenden Wert aus Spannweite bestimmen | 0 | 0 | 0 |
| 11 | Mehrere Kenngrößen zweier Datenreihen vergleichend bestimmen | 0 | 0 | 0 |
| 12 | Modalwert bestimmen | 0 | 0 | 0 |

### Prozentrechnung – 43 Punkte, 15 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Prozentsatz berechnen | 11 | 5 | 5 |
| 2 | Prozentwert berechnen | 8 | 7 | 6 |
| 3 | Prozentuale Veränderung berechnen | 6 | 3 | 6 |
| 4 | Anteilsaussage prüfen und korrigieren | 6 | 3 | 3 |
| 5 | Wert nach prozentualer Erhöhung berechnen | 3 | 2 | 3 |
| 6 | Steigung in Prozent deuten | 3 | 1 | 1 |
| 7 | Prozent und Anteil umwandeln | 2 | 2 | 5 |
| 8 | Grundwert berechnen | 2 | 2 | 2 |
| 9 | Fehlenden Prozentanteil ergänzen | 2 | 1 | 1 |
| 10 | Steigung in Prozent berechnen | 0 | 0 | 1 |
| 11 | Gesamtmenge aus Pro-Kopf-Angabe, Anteil und Einwohnerzahl berechnen | 0 | 0 | 0 |
| 12 | Prozentanteil einer Rasterfläche markieren | 0 | 0 | 0 |
| 13 | Prozentuale Abweichung einer Modellfläche von der tatsächlichen Fläche berechnen | 0 | 0 | 0 |
| 14 | Prozentuale Abweichung eines Werts von einem Vergleichswert berechnen | 0 | 0 | 0 |
| 15 | Prozentualen Zuwachs aus Anfangs- und Endwert berechnen | 0 | 0 | 0 |

### Wahrscheinlichkeit mehrstufig – 42 Punkte, 10 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Baumdiagramm ergänzen | 21 | 6 | 6 |
| 2 | Wahrscheinlichkeit mehrstufig unabhängig | 10 | 4 | 5 |
| 3 | Wahrscheinlichkeit mehrstufig ohne Zurücklegen | 9 | 3 | 5 |
| 4 | Wahrscheinlichkeit über Gegenereignis berechnen | 2 | 1 | 1 |
| 5 | Behauptung prüfen | 0 | 0 | 12 |
| 6 | Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen | 0 | 0 | 0 |
| 7 | Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen | 0 | 0 | 0 |
| 8 | Ereignis zu Wahrscheinlichkeitsterm beschreiben | 0 | 0 | 0 |
| 9 | Gleichverteilung der Trefferwahrscheinlichkeit begründen | 0 | 0 | 0 |
| 10 | Wahrscheinlichkeit für die Position des ersten Treffers berechnen | 0 | 0 | 0 |

### Trigonometrie im rechtwinkligen Dreieck – 40 Punkte, 10 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Seite im rechtwinkligen Dreieck berechnen | 23 | 8 | 9 |
| 2 | Winkel im rechtwinkligen Dreieck berechnen | 11 | 5 | 6 |
| 3 | Winkelfunktion Seitenverhältnis angeben | 5 | 5 | 5 |
| 4 | Trigonometrische Gleichung nach Seite umstellen | 1 | 1 | 1 |
| 5 | Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen | 0 | 0 | 0 |
| 6 | Formel für die Tiefe eines Kegels aus Durchmesser und Öffnungswinkel herleiten | 0 | 0 | 0 |
| 7 | Höhe eines Drachenvierecks aus geteiltem Winkel und Diagonalen berechnen | 0 | 0 | 0 |
| 8 | Neigungswinkel einer Geraden berechnen | 0 | 0 | 0 |
| 9 | Seite im rechtwinkligen Dreieck aus Winkel und Kathete berechnen | 0 | 0 | 0 |
| 10 | Winkel eines Drachenvierecks aus Diagonalenabschnitten berechnen | 0 | 0 | 0 |

### Volumen und Oberfläche – 38 Punkte, 25 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Volumen Zylinder berechnen | 8 | 4 | 5 |
| 2 | Höhe eines Zylinders aus Volumen berechnen | 3 | 1 | 1 |
| 3 | Mantelfläche Kegel berechnen | 3 | 1 | 1 |
| 4 | Radius eines Zylinders aus Volumen berechnen | 3 | 1 | 1 |
| 5 | Restvolumen berechnen | 3 | 1 | 1 |
| 6 | Term zu Körper angeben | 3 | 1 | 1 |
| 7 | Volumen Kegel und Zylinder vergleichen | 3 | 1 | 1 |
| 8 | Volumen Kugel berechnen | 3 | 1 | 1 |
| 9 | Volumen Prisma berechnen | 2 | 1 | 2 |
| 10 | Mantelfläche Prisma berechnen | 2 | 1 | 1 |
| 11 | Mantelfläche Zylinder berechnen | 2 | 1 | 1 |
| 12 | Volumenänderung bei doppeltem Radius begründen | 2 | 1 | 1 |
| 13 | Volumen Würfel berechnen | 1 | 1 | 1 |
| 14 | Volumen Kegel berechnen | 0 | 0 | 1 |
| 15 | Anzahl Objekte aus Masse und Tragfähigkeit berechnen | 0 | 0 | 0 |
| 16 | Durchmesser einer Halbkugel aus der Oberfläche berechnen | 0 | 0 | 0 |
| 17 | Fläche zweier Mantelflächen eines Prismas mit trapezförmiger Grundfläche berechnen | 0 | 0 | 0 |
| 18 | Kantenlänge einer quadratischen Grundfläche aus Volumen berechnen | 0 | 0 | 0 |
| 19 | Kantensumme eines Quaders mit Seitenlängen in Abhängigkeit von der Höhe berechnen | 0 | 0 | 0 |
| 20 | Kugeldurchmesser aus Anzahl nebeneinanderliegender Kugeln bestimmen | 0 | 0 | 0 |
| 21 | Kugeloberfläche berechnen | 0 | 0 | 0 |
| 22 | Mantelfläche einer Pyramide berechnen | 0 | 0 | 0 |
| 23 | Masse eines zusammengesetzten Körpers berechnen | 0 | 0 | 0 |
| 24 | Transportanzahl aus Volumen und Masse berechnen | 0 | 0 | 0 |
| 25 | Volumen eines aus Kegel und Halbkugel zusammengesetzten Körpers mit Nebenbedingung berechnen | 0 | 0 | 0 |

### Exponentialfunktionen und Wachstum – 37 Punkte, 17 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Wachstumstabelle ergänzen | 11 | 5 | 5 |
| 2 | Graph zu Wachstumsprozess zuordnen | 6 | 2 | 2 |
| 3 | Wachstumsfaktor aus Tabelle bestimmen | 6 | 2 | 2 |
| 4 | Exponentialfunktion aufstellen | 4 | 2 | 4 |
| 5 | Verdopplungs- oder Halbwertszeit bestimmen | 4 | 2 | 2 |
| 6 | Wachstumsart begründen | 4 | 2 | 2 |
| 7 | Zeitpunkt für Schwellenwert bei Wachstum bestimmen | 2 | 1 | 1 |
| 8 | Aussage über einen Logarithmusterm als Abstand zur y-Achse prüfen | 0 | 0 | 0 |
| 9 | Exponentialfunktion vertikal verschieben und Schnittpunkt mit der y-Achse angeben | 0 | 0 | 0 |
| 10 | Graph einer Exponentialfunktion an der y-Achse spiegeln | 0 | 0 | 0 |
| 11 | Graph eines exponentiellen Vorgangs zeichnen | 0 | 0 | 0 |
| 12 | Parameter einer Exponentialfunktion aus Graph bestimmen | 0 | 0 | 0 |
| 13 | Parameter einer Exponentialfunktion aus einer Wertetabelle bestimmen | 0 | 0 | 0 |
| 14 | Sachaufgabe zu einer Gleichungskette formulieren | 0 | 0 | 0 |
| 15 | Wertebereich einer Funktion angeben | 0 | 0 | 0 |
| 16 | Wertetabelle auf Exponentialfunktion prüfen | 0 | 0 | 0 |
| 17 | Zeit aus Exponentialgleichung berechnen | 0 | 0 | 0 |

### Satz des Pythagoras – 33 Punkte, 7 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Pythagoras Kathete | 13 | 6 | 5 |
| 2 | Pythagoras Hypotenuse | 9 | 3 | 4 |
| 3 | Pythagoras Gleichung zuordnen | 4 | 4 | 4 |
| 4 | Streckenlänge aus Koordinaten berechnen | 4 | 1 | 1 |
| 5 | Mantellinie Kegel bestimmen | 2 | 1 | 1 |
| 6 | Satz des Pythagoras formulieren | 1 | 1 | 1 |
| 7 | Kegelhöhe aus Mantellinie und Radius berechnen | 0 | 0 | 0 |

### Sinussatz – 29 Punkte, 5 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Sinussatz Seite berechnen | 29 | 9 | 9 |
| 2 | Seite im allgemeinen Dreieck über Kosinussatz berechnen | 0 | 0 | 0 |
| 3 | Sinussatz Winkel berechnen | 0 | 0 | 0 |
| 4 | Winkel im allgemeinen Dreieck über Kosinussatz berechnen | 0 | 0 | 0 |
| 5 | Winkel im allgemeinen Dreieck über Sinussatz berechnen | 0 | 0 | 0 |

### Diagramme lesen und beurteilen – 27 Punkte, 6 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Aussage zu Diagramm prüfen | 8 | 3 | 3 |
| 2 | Sektor im Kreisdiagramm zuordnen | 6 | 2 | 4 |
| 3 | Achsenskalierung aus Säule bestimmen | 5 | 2 | 2 |
| 4 | Verzerrung eines Diagramms erklären | 3 | 2 | 3 |
| 5 | Wert aus Diagramm ablesen | 3 | 2 | 2 |
| 6 | Werte im Diagramm nach Bedingung auswählen | 2 | 2 | 2 |

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
| 11 | Grundfläche eines Prismas im Körpernetz kennzeichnen | 0 | 0 | 0 |
| 12 | Körper im Schrägbild darstellen | 0 | 0 | 0 |
| 13 | Maße eines Körpers aus einem bemaßten Netz im Maßstab ablesen | 0 | 0 | 0 |

### Ebene Figuren und Winkel – 25 Punkte, 20 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Winkelsumme im Dreieck anwenden | 5 | 4 | 9 |
| 2 | Strecke aus Teilstrecken berechnen | 4 | 3 | 6 |
| 3 | Winkel im Viereck berechnen | 3 | 3 | 3 |
| 4 | Gleichschenkliges Dreieck erkennen | 3 | 2 | 1 |
| 5 | Eigenschaft einer Figur zuordnen | 2 | 2 | 2 |
| 6 | Winkel an geschnittenen Parallelen bestimmen | 2 | 2 | 2 |
| 7 | Winkel über Scheitel- oder Nebenwinkel bestimmen | 2 | 2 | 2 |
| 8 | Rechten Winkel begründen | 2 | 1 | 1 |
| 9 | Winkel aus Teilwinkeln berechnen | 1 | 1 | 3 |
| 10 | Dreiecksungleichung anwenden | 1 | 1 | 1 |
| 11 | Dreieck aus Koordinaten als gleichschenklig-rechtwinklig nachweisen | 0 | 0 | 0 |
| 12 | Flächenberechnung eines Vielecks anhand einer vorgegebenen Gleichung erläutern | 0 | 0 | 0 |
| 13 | Flächeninhalt eines Dreiecks aus Koordinaten berechnen | 0 | 0 | 0 |
| 14 | Flächeninhalt eines Dreiecks aus drei Seiten berechnen | 0 | 0 | 0 |
| 15 | Flächeninhalt eines Vierecks aus den Achsenschnittpunkten zweier Funktionsgraphen berechnen | 0 | 0 | 0 |
| 16 | Gleich große oder doppelt so große Winkel in einer aus kongruenten Dreiecken zusammengesetzten Figur kennzeichnen | 0 | 0 | 0 |
| 17 | Trapezfläche im Koordinatensystem aus Funktionsgraph und Geraden berechnen | 0 | 0 | 0 |
| 18 | Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen | 0 | 0 | 0 |
| 19 | Umfang eines Dreiecks aus Koordinaten berechnen | 0 | 0 | 0 |
| 20 | Winkel als Differenz zweier Teilwinkel in einem zusammengesetzten rechtwinkligen Dreieck nachweisen | 0 | 0 | 0 |

### Lineare Gleichungssysteme – 25 Punkte, 3 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Gleichung im Sachzusammenhang deuten | 12 | 4 | 5 |
| 2 | Lineares Gleichungssystem aufstellen | 10 | 3 | 3 |
| 3 | Lineares Gleichungssystem lösen | 3 | 1 | 4 |

### Wahrscheinlichkeit einstufig – 24 Punkte, 3 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Wahrscheinlichkeit einstufig | 18 | 12 | 9 |
| 2 | Zufallsgerät zu Wahrscheinlichkeit entwerfen | 6 | 4 | 4 |
| 3 | Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen | 0 | 0 | 0 |

### Brüche und Dezimalzahlen – 20 Punkte, 5 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Bruchteil einer Fläche bestimmen | 10 | 9 | 9 |
| 2 | Zahlen in verschiedenen Darstellungen vergleichen | 7 | 7 | 7 |
| 3 | Bruchteil einer Größe berechnen | 2 | 2 | 2 |
| 4 | Mitte zweier Zahlen bestimmen | 1 | 1 | 1 |
| 5 | Anteil einer unterteilten Kreisfläche bestimmen | 0 | 0 | 0 |

### Zuordnungen proportional und antiproportional – 20 Punkte, 5 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Dauer aus Menge und Rate berechnen | 11 | 4 | 4 |
| 2 | Kosten aus Menge und Preis berechnen | 4 | 3 | 3 |
| 3 | Proportionale Zuordnung Dreisatz | 3 | 3 | 3 |
| 4 | Geschwindigkeit aus Weg und Zeit berechnen | 2 | 1 | 1 |
| 5 | Antiproportionale Zuordnung Dreisatz | 0 | 0 | 0 |

### Einheiten umrechnen – 17 Punkte, 11 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Fehler in Rechnung erklären und korrigieren | 4 | 1 | 1 |
| 2 | Zeiteinheiten umrechnen | 3 | 3 | 4 |
| 3 | Materialbedarf aus Fläche berechnen | 3 | 1 | 1 |
| 4 | Größen vergleichen | 2 | 2 | 2 |
| 5 | Volumen aus Masse und Dichte berechnen | 2 | 1 | 1 |
| 6 | Uhrzeit aus Startzeit und Dauer berechnen | 1 | 1 | 2 |
| 7 | Längeneinheit mit Faktor umrechnen | 1 | 1 | 1 |
| 8 | Portionen aus Gesamtmenge berechnen | 1 | 1 | 1 |
| 9 | Masse aus Volumen und Dichte berechnen | 0 | 0 | 1 |
| 10 | Farbmenge aus Fläche und Ergiebigkeit berechnen | 0 | 0 | 0 |
| 11 | Materialbedarf aus Längen berechnen | 0 | 0 | 0 |

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

### Maßstab – 9 Punkte, 2 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Draufsicht maßstabsgerecht zeichnen | 5 | 1 | 1 |
| 2 | Länge im Maßstab umrechnen | 4 | 2 | 2 |

### Rationale Zahlen rechnen – 9 Punkte, 6 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Termwert berechnen | 3 | 3 | 3 |
| 2 | Zahl zu Bedingung angeben | 2 | 2 | 2 |
| 3 | Günstigste Preiskombination bestimmen | 2 | 1 | 1 |
| 4 | Ausgangswert aus Differenz berechnen | 1 | 1 | 1 |
| 5 | Vorzeichenregel anwenden | 1 | 1 | 1 |
| 6 | Aussage über eine mehrfach gebrochene Streckenteilung prüfen | 0 | 0 | 0 |

### Daten darstellen – 7 Punkte, 4 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Kreisdiagramm zeichnen | 3 | 1 | 3 |
| 2 | Säulen- oder Balkendiagramm ergänzen | 2 | 2 | 3 |
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
| 1 | Streckenlänge über ein konstruiertes Parallelogramm im Vieleck begründen | 0 | 0 | 0 |
| 2 | Vieleck aus Seiten und Winkeln im Maßstab konstruieren | 0 | 0 | 0 |

### Runden und Überschlag – 0 Punkte, 1 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Maximale ganzzahlige Menge aus Grenzwert berechnen | 0 | 0 | 0 |

### Trigonometrische Funktionen – 0 Punkte, 3 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Eigenschaften trigonometrischer Funktionen vergleichen | 0 | 0 | 0 |
| 2 | Graph einer trigonometrischen Funktion durch Streckung und Verschiebung beschreiben | 0 | 0 | 0 |
| 3 | Trigonometrische Funktionsgleichung zu Graph zuordnen | 0 | 0 | 0 |

### Ähnlichkeit und Strahlensätze – 0 Punkte, 3 Typen

| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |
|---|---|---|---|---|
| 1 | Grundstücksbreiten aus einem in Teilflächen zerlegten Trapez bestimmen | 0 | 0 | 0 |
| 2 | Länge auf der Mantellinie eines Kegels bei Teilfüllung über Ähnlichkeit bestimmen | 0 | 0 | 0 |
| 3 | Trapezhöhe über den aus einem angrenzenden Dreieck übertragenen Winkel berechnen | 0 | 0 | 0 |

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

### Ohne Vorkommen (108)
- Anstieg einer linearen Funktion aus Punkt und y-Achsenabschnitt berechnen – Lineare Funktionen
- Anteil aus der Wahrscheinlichkeit mehrerer unabhängiger Ereignisse zurückrechnen – Wahrscheinlichkeit mehrstufig
- Anteil einer unterteilten Kreisfläche bestimmen – Brüche und Dezimalzahlen
- Antiproportionale Zuordnung Dreisatz – Zuordnungen proportional und antiproportional
- Anzahl Kombinationen nach dem Zählprinzip bestimmen – Zählen und Kombinatorik
- Anzahl Objekte aus Masse und Tragfähigkeit berechnen – Volumen und Oberfläche
- Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen – Zählen und Kombinatorik
- Anzahl der Pfade zu einem Ereignis im Baumdiagramm zählen – Wahrscheinlichkeit mehrstufig
- Aussage zu einer Winkelfunktion im rechtwinkligen Dreieck prüfen – Trigonometrie im rechtwinkligen Dreieck
- Aussage über eine mehrfach gebrochene Streckenteilung prüfen – Rationale Zahlen rechnen
- Aussage über einen Logarithmusterm als Abstand zur y-Achse prüfen – Exponentialfunktionen und Wachstum
- Binomische Formel anwenden – Terme umformen
- Datenreihen anhand von Kenngrößen vergleichen und begründen – Kenngrößen
- Dreieck aus Koordinaten als gleichschenklig-rechtwinklig nachweisen – Ebene Figuren und Winkel
- Durchmesser einer Halbkugel aus der Oberfläche berechnen – Volumen und Oberfläche
- Eigenschaften trigonometrischer Funktionen vergleichen – Trigonometrische Funktionen
- Eignung einer Funktionsgleichung für einen Sachverhalt beurteilen – Quadratische Funktionen
- Ereignis zu Wahrscheinlichkeitsterm beschreiben – Wahrscheinlichkeit mehrstufig
- Erwartete Anzahl aus Wahrscheinlichkeit und Stichprobengröße berechnen – Wahrscheinlichkeit einstufig
- Exponentialfunktion vertikal verschieben und Schnittpunkt mit der y-Achse angeben – Exponentialfunktionen und Wachstum
- Farbmenge aus Fläche und Ergiebigkeit berechnen – Einheiten umrechnen
- Fehlende Schnittpunkte zweier Funktionen über Wertebereiche begründen – Quadratische Funktionen
- Fehlenden Wert aus Spannweite bestimmen – Kenngrößen
- Fläche zweier Mantelflächen eines Prismas mit trapezförmiger Grundfläche berechnen – Volumen und Oberfläche
- Flächenberechnung eines Vielecks anhand einer vorgegebenen Gleichung erläutern – Ebene Figuren und Winkel
- Flächeninhalt eines Drachenvierecks aus Diagonalen berechnen – Flächeninhalt und Umfang
- Flächeninhalt eines Dreiecks aus Koordinaten berechnen – Ebene Figuren und Winkel
- Flächeninhalt eines Dreiecks aus drei Seiten berechnen – Ebene Figuren und Winkel
- Flächeninhalt eines Vierecks aus den Achsenschnittpunkten zweier Funktionsgraphen berechnen – Ebene Figuren und Winkel
- Flächeninhalt eines aus vier kongruenten rechtwinkligen Dreiecken zusammengesetzten Vierecks berechnen – Flächeninhalt und Umfang
- Flächeninhalt eines gleichseitigen Dreiecks aus Umfang berechnen – Flächeninhalt und Umfang
- Formel für die Tiefe eines Kegels aus Durchmesser und Öffnungswinkel herleiten – Trigonometrie im rechtwinkligen Dreieck
- Funktionswerte einer Parabel im Sachkontext berechnen – Quadratische Funktionen
- Gerade an der x-Achse spiegeln – Lineare Funktionen
- Gerade an der y-Achse spiegeln – Lineare Funktionen
- Geradengleichung aus Steigung und Punkt bestimmen – Lineare Funktionen
- Geradengleichung einer Parallelen durch einen Punkt bestimmen – Lineare Funktionen
- Gesamtmenge aus Pro-Kopf-Angabe, Anteil und Einwohnerzahl berechnen – Prozentrechnung
- Gleich große oder doppelt so große Winkel in einer aus kongruenten Dreiecken zusammengesetzten Figur kennzeichnen – Ebene Figuren und Winkel
- Gleichung einer Senkrechten aufstellen – Lineare Funktionen
- Gleichverteilung der Trefferwahrscheinlichkeit begründen – Wahrscheinlichkeit mehrstufig
- Graph einer Exponentialfunktion an der y-Achse spiegeln – Exponentialfunktionen und Wachstum
- Graph einer trigonometrischen Funktion durch Streckung und Verschiebung beschreiben – Trigonometrische Funktionen
- Graph eines exponentiellen Vorgangs zeichnen – Exponentialfunktionen und Wachstum
- Grundfläche eines Prismas im Körpernetz kennzeichnen – Körper, Netze, Schrägbilder
- Grundstücksbreiten aus einem in Teilflächen zerlegten Trapez bestimmen – Ähnlichkeit und Strahlensätze
- Höhe eines Drachenvierecks aus geteiltem Winkel und Diagonalen berechnen – Trigonometrie im rechtwinkligen Dreieck
- Innendurchmesser eines Kreisrings aus Flächeninhalt und Außendurchmesser berechnen – Flächeninhalt und Umfang
- Kantenlänge einer quadratischen Grundfläche aus Volumen berechnen – Volumen und Oberfläche
- Kantensumme eines Quaders mit Seitenlängen in Abhängigkeit von der Höhe berechnen – Volumen und Oberfläche
- Kegelhöhe aus Mantellinie und Radius berechnen – Satz des Pythagoras
- Kreisumfang berechnen – Flächeninhalt und Umfang
- Kugeldurchmesser aus Anzahl nebeneinanderliegender Kugeln bestimmen – Volumen und Oberfläche
- Kugeloberfläche berechnen – Volumen und Oberfläche
- Körper im Schrägbild darstellen – Körper, Netze, Schrägbilder
- Lage zweier Geraden bestimmen – Lineare Funktionen
- Lineare Funktion aus Steigung und Schnittbedingung bestimmen – Lineare Funktionen
- Länge auf der Mantellinie eines Kegels bei Teilfüllung über Ähnlichkeit bestimmen – Ähnlichkeit und Strahlensätze
- Mantelfläche einer Pyramide berechnen – Volumen und Oberfläche
- Masse eines zusammengesetzten Körpers berechnen – Volumen und Oberfläche
- Materialbedarf aus Längen berechnen – Einheiten umrechnen
- Maximale Anzahl rechteckiger Objekte auf einer Fläche bestimmen – Flächeninhalt und Umfang
- Maximale ganzzahlige Menge aus Grenzwert berechnen – Runden und Überschlag
- Maße eines Körpers aus einem bemaßten Netz im Maßstab ablesen – Körper, Netze, Schrägbilder
- Mehrere Kenngrößen zweier Datenreihen vergleichend bestimmen – Kenngrößen
- Modalwert bestimmen – Kenngrößen
- Neigungswinkel einer Geraden berechnen – Trigonometrie im rechtwinkligen Dreieck
- Parabelgleichung aus Scheitel und Punkt bestimmen – Quadratische Funktionen
- Parabelgleichung aus Spannweite und Höhe eines Bogens bestimmen – Quadratische Funktionen
- Parabelgleichung aus zwei Nullstellen aufstellen und Nullstellen bestätigen – Quadratische Funktionen
- Parabeltransformation gegenüber der Normalparabel beschreiben – Quadratische Funktionen
- Parameter einer Exponentialfunktion aus Graph bestimmen – Exponentialfunktionen und Wachstum
- Parameter einer Exponentialfunktion aus einer Wertetabelle bestimmen – Exponentialfunktionen und Wachstum
- Parameter einer Parabel aus Graph bestimmen – Quadratische Funktionen
- Parameter einer Wurzelfunktion aus einem Punkt bestimmen – Funktionen allgemein
- Prozentanteil einer Rasterfläche markieren – Prozentrechnung
- Prozentuale Abweichung einer Modellfläche von der tatsächlichen Fläche berechnen – Prozentrechnung
- Prozentuale Abweichung eines Werts von einem Vergleichswert berechnen – Prozentrechnung
- Prozentualen Zuwachs aus Anfangs- und Endwert berechnen – Prozentrechnung
- Sachaufgabe zu einer Gleichungskette formulieren – Exponentialfunktionen und Wachstum
- Scheitelpunkt einer Parabel rechnerisch nachweisen – Quadratische Funktionen
- Schnittpunktanzahl von Graphen begründen – Quadratische Funktionen
- Schnittpunktgleichung zweier Parabeln herleiten – Quadratische Funktionen
- Seite im allgemeinen Dreieck über Kosinussatz berechnen – Sinussatz
- Seite im rechtwinkligen Dreieck aus Winkel und Kathete berechnen – Trigonometrie im rechtwinkligen Dreieck
- Sinussatz Winkel berechnen – Sinussatz
- Streckenlänge über ein konstruiertes Parallelogramm im Vieleck begründen – Kongruenz und Konstruktion
- Symmetrie einer geraden Funktion zur Bestimmung eines Funktionswertes ohne Rechnung nutzen – Funktionen allgemein
- Term durch Zusammenfassen gleichartiger Glieder vereinfachen – Terme umformen
- Term mit Klammern und Potenzen vereinfachen – Terme umformen
- Transportanzahl aus Volumen und Masse berechnen – Volumen und Oberfläche
- Trapezfläche im Koordinatensystem aus Funktionsgraph und Geraden berechnen – Ebene Figuren und Winkel
- Trapezhöhe über den aus einem angrenzenden Dreieck übertragenen Winkel berechnen – Ähnlichkeit und Strahlensätze
- Trigonometrische Funktionsgleichung zu Graph zuordnen – Trigonometrische Funktionen
- Umfang eines Drachenvierecks aus Diagonalenabschnitten berechnen – Ebene Figuren und Winkel
- Umfang eines Dreiecks aus Koordinaten berechnen – Ebene Figuren und Winkel
- Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen – Funktionen allgemein
- Vieleck aus Seiten und Winkeln im Maßstab konstruieren – Kongruenz und Konstruktion
- Volumen eines aus Kegel und Halbkugel zusammengesetzten Körpers mit Nebenbedingung berechnen – Volumen und Oberfläche
- Wahrscheinlichkeit für die Position des ersten Treffers berechnen – Wahrscheinlichkeit mehrstufig
- Wertebereich einer Funktion angeben – Exponentialfunktionen und Wachstum
- Wertetabelle auf Exponentialfunktion prüfen – Exponentialfunktionen und Wachstum
- Winkel als Differenz zweier Teilwinkel in einem zusammengesetzten rechtwinkligen Dreieck nachweisen – Ebene Figuren und Winkel
- Winkel eines Drachenvierecks aus Diagonalenabschnitten berechnen – Trigonometrie im rechtwinkligen Dreieck
- Winkel im allgemeinen Dreieck über Kosinussatz berechnen – Sinussatz
- Winkel im allgemeinen Dreieck über Sinussatz berechnen – Sinussatz
- Zeit aus Exponentialgleichung berechnen – Exponentialfunktionen und Wachstum
- x-Werte einer quadratischen Funktion zu gegebenem Funktionswert berechnen – Quadratische Funktionen
