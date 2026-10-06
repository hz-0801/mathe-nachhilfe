# Fremdprüfungen Baden-Württemberg (Gruppe bw)

Stand 06.10.2026. Quellen: die zwölf Dateien `quellen/quelle-fremd-ni-bw-bw-{hs,rs,wrs}-{2021..2024}.txt` (Serlo-Fassung der BW-Abschlussprüfungen Hauptschule, Realschule, Werkrealschule; Lösungen sind Serlo-Lösungen, nicht amtlich). Marke „BW ’JJ“, herausgelöste „nach BW ’JJ“. Regeln: `aufgabenbank/bau/pruefheft/beschluesse-2026-10-06b.md` N1, N4.

## Zahlen

- Zeilen in `bw.csv`: 372 (228 ganz, 144 herausgelöst); Sätze in `bw-erkennen.csv`: 74.
- Mit sympy nachgerechnet: 350 Zeilen; 22 Zeilen ohne Rechenergebnis (Zuordnen, Ankreuzen, Zeichnen, Formel ergänzen) nur sachlich geprüft.
- Teilaufgaben ohne P10-Stufe (nicht geschrieben): 83.

| Kapitel | ganz | herausgelöst | erkennen |
|---|---|---|---|
| daten | 16 | 4 | 0 |
| dreiecke | 52 | 42 | 25 |
| flaechen | 15 | 5 | 0 |
| gleichungssysteme | 9 | 8 | 0 |
| koerper | 18 | 6 | 0 |
| lineare | 7 | 11 | 0 |
| prozent | 35 | 35 | 39 |
| quadratische | 44 | 25 | 0 |
| wahrscheinlichkeit | 32 | 8 | 10 |

Je Datei (ganz/herausgelöst):

- quelle-fremd-ni-bw-bw-hs-2021.txt: 13/8
- quelle-fremd-ni-bw-bw-hs-2022.txt: 16/5
- quelle-fremd-ni-bw-bw-hs-2023.txt: 14/5
- quelle-fremd-ni-bw-bw-hs-2024.txt: 10/2
- quelle-fremd-ni-bw-bw-rs-2021.txt: 18/22
- quelle-fremd-ni-bw-bw-rs-2022.txt: 21/21
- quelle-fremd-ni-bw-bw-rs-2023.txt: 20/16
- quelle-fremd-ni-bw-bw-rs-2024.txt: 18/14
- quelle-fremd-ni-bw-bw-wrs-2021.txt: 27/14
- quelle-fremd-ni-bw-bw-wrs-2022.txt: 24/17
- quelle-fremd-ni-bw-bw-wrs-2023.txt: 26/11
- quelle-fremd-ni-bw-bw-wrs-2024.txt: 21/9

## Entscheidungen

- id: `BW-<HS|RS|WRS>-<Jahr>-<Teil><Nr><Buchstabe>`; Pflichtteile als `A1-4`, `A2-3` (Nummer im Teil), Wahlteil als `B2a`. Wahlteilaufgaben ohne Buchstaben in der Quelle, die mehrere Unteraufgaben bündeln (WRS 2021–2023), bekommen fortlaufende Buchstaben; die Spalte quelle nennt den Teil (z. B. „Wahlteil B2 (Leuchtmittel)“).
- Doppelt gespeicherte Serlo-Aufgaben (gleiche Aufgabe als Sammel- und Einzelseite, z. B. WRS 2022 A1 Nr. 2/3, 4/5, 8/9) nur einmal erfasst.
- Teile einer Teilaufgabe ohne P10-Stufe (Erwartungswert, Strahlensatz, Oberfläche Kugel/Kegel, Konstruktion, Einheiten) sind weggelassen, wenn der Rest lösbar bleibt; vermerkt in bemerkung und unten als eigener Posten.
- Werte, die nur in Abbildungen standen, wurden aus der Serlo-Lösung erschlossen und stehen in abbildung; wo das unsicher ist, steht die Zeile unter „Unsichere Lösungen“.
- Wo die Serlo-Lösung mit gerundeten Zwischenwerten rechnet, steht in loesung der mit sympy ungerundet gerechnete Wert; die Serlo-Zahl steht in bemerkung.
- „Mitternachtsformel“, „pq-Formel“, „Zentralwert“, „Schaubild“ im Wortlaut durch Brandenburger Wörter ersetzt (Lösungsformel nicht genannt, „Median“, „Graph/Diagramm“). „Normalparabel“, „Scheitelpunkt“, „Steigung“ bleiben.
- Hauptplatz Gegenwahrscheinlichkeit/„mit Zurücklegen“: Erkennen-Sätze zu „mit Zurücklegen“ stehen unter der Stufe „ohne Zurücklegen“ (gesucht = „mit Zurücklegen“), weil es keine eigene Stufe gibt.
- Zuordnungen „Parabel spiegeln/verschieben“ stehen ersatzweise unter „Lage zweier Parabeln ohne Rechnung begründen“; Sinus über 90° (RS 2024 A1 Nr. 5) unter „Seitenverhältnis benennen“; Oberflächenterm (WRS 2023 A1 Nr. 9) unter „Volumen direkt“ (alles in bemerkung).
- Viele RS-Wahlteilaufgaben sind deutlich schwerer als P10 (Strahlensatz, Fünfeck, Kosinussatz, verschachtelte Figuren); sie stehen als ganz-Zeilen nur zur Vollständigkeit; brauchbar sind vor allem ihre herausgelösten Zeilen. Der Bau soll N1.2 (nie schwerer als die schwerste BB/BE-Aufgabe) anhand schritte/zahlart/woerter filtern.
- Wortlaut: Prüfung gegen die Quelle auf 9 gleiche Wörter in Folge; alle Treffer umformuliert.
- Bau-Skripte (Zeilen je Datei mit sympy-Prüfung) liegen nur im Scratchpad, weil der Schreibbereich auf drei Dateien begrenzt war.

## Unsichere Lösungen

- BW-HS-2022-A1-9: beschriftete Augenzahlen des Netzes nicht im Text, 2, 4, 1 angenommen (laut Lösung zwei gerade, eine ungerade)
- BW-HS-2022-A2-3: Netzform nicht im Text, Abbildung fehlt; Lösung nur Zeichnung (nicht mit sympy prüfbar)
- BW-HS-2023-A2-2: Grundriss aus der Lösung rekonstruiert, Lage der Teilflächen nicht gesichert
- BW-HS-2023-B4a: Körperform nicht im Text; Lösung nicht rechnerisch prüfbar
- BW-HS-2024-A2-3: Lage der Winkel δ, ε aus der Lösung rekonstruiert (Abbildung fehlt)
- BW-RS-2021-A1-1a: Abbildung (Netze) fehlt im Text; Lösung „Netz B“ ungeprüft übernommen
- BW-RS-2021-A1-4: Lage des leeren Feldes in der 2. Stufe aus Lösung erschlossen
- BW-RS-2021-A2-1: Figur nur aus der Lösung rekonstruiert; Strahlensatz nötig, für P10 eher zu schwer
- BW-RS-2021-A2-6: Boxplot-Aufgabe, Säulendiagramm 1 nicht im Text; Lösung übernommen, nur Quartilsplatz geprüft
- BW-RS-2021-B1a: Lage von D und F aus der Lösung rekonstruiert
- BW-RS-2021-B4b: Faltfigur aus der Lösung rekonstruiert (Bilder fehlen)
- BW-RS-2022-A1-8: Figur aus der Lösung rekonstruiert; rechte Winkel (C, E) angenommen
- BW-RS-2022-B2b: Kosinussatz nötig (keine P10-Stufe); nur als Quelle der herausgelösten Aufgabe sinnvoll
- BW-RS-2023-A1-2: Figur aus der Lösung rekonstruiert (Abbildung fehlt)
- BW-RS-2023-A1-4: Netze nicht im Text; Lösung „Netz C“ ungeprüft übernommen
- BW-RS-2023-A1-7: Ranglisten nicht im Text; nicht nachrechenbar
- BW-RS-2023-A2-5: Belegung der Kreiselfelder (Symbole, grau) aus der Lösung rekonstruiert
- BW-RS-2023-A2-6: Bannerwert 2020 nicht im Text, 895 Mio. € aus Serlo-Ergebnis 817 Mio. € rückgerechnet
- BW-RS-2023-B1a: Figur aus der Lösung rekonstruiert
- BW-RS-2023-B3a: Ziffern auf den Streifen nicht im Text; zwei 3, eine 6, eine 1 gesichert, fünfte Ziffer angenommen
- BW-RS-2023-B3b: Abstand über dem Schilfrohr hängt von der Rundung von a ab (exakt ≈ 26,6 cm, Serlo 27,4 cm)
- BW-RS-2023-B4b: Lage der Streckenzugpunkte aus der Lösung rekonstruiert; für P10 sehr schwer
- BW-RS-2024-A1-2: welcher Ast der 2. Stufe leer ist, aus der Lösung erschlossen (nach grün angenommen)
- BW-RS-2024-A1-5: Stufe nur ersatzweise (Sinus am Einheitskreis hat keine eigene P10-Stufe)
- BW-RS-2024-A2-1: Figur aus der Lösung rekonstruiert (Abbildung fehlt)
- BW-RS-2024-A2-6: Nutzerzahl 2020 nicht im Text, aus Serlo-Ergebnis 23,5 % auf 340 000 rückgerechnet
- BW-RS-2024-B1a: Lage der Punkte des Drachens unklar (Abbildung fehlt); Wortlaut vor Verwendung am Original prüfen
- BW-WRS-2021-B2b: Kostenangaben nur aus den Gleichungen der Lösung (y = 0,2x + 120; y = 1,2x + 80); Einheit angenommen
- BW-WRS-2021-B4a: Figur aus der Lösung rekonstruiert (Abbildung fehlt)
- BW-WRS-2022-A2-1: Belegung des 8. Glücksradfelds nicht im Text
- BW-WRS-2022-A2-5: Darlehenszins 1,44 % und Rate 430 € nur aus der Lösung; Ausgangszinssatz 1,5 % ebenso
- BW-WRS-2022-A2-6: Rundungsabhängig: exakt h_Z ≈ 2,38 m, Serlo 2,40 m
- BW-WRS-2022-B1b: Serlo-Lösung ≈ 10 % widerspricht „Reihenfolge egal“; eigene Lösung 676/3 364 ≈ 20,1 %
- BW-WRS-2022-B4b: Vierecksform aus der Lösung erschlossen (Abbildung fehlt)
- BW-WRS-2023-A1-2: Figur aus der Lösung rekonstruiert
- BW-WRS-2023-A1-9: Stufe nur ersatzweise (Oberfläche zusammengesetzter Körper)
- BW-WRS-2023-B1c: Serlo-Lösung (tan, 51,48 cm) widerspricht „Umkreis“; eigene Lösung mit sin: ≈ 49,7 cm
- BW-WRS-2023-B4b: Lage von I und Winkel α aus der Lösung rekonstruiert
- BW-WRS-2024-A1-5: Gewinnbedingungen (ungerade, Teiler von 12) nur aus der Lösung
- BW-WRS-2024-A2-2: Perlenketten nicht im Text; Merkmale aus der Lösung, Wortlaut am Original prüfen
- BW-WRS-2024-A2-3: Serlo-Korrektur x = −2/7 falsch; eigene Lösung x = 0, y = 1
- BW-WRS-2024-B1a: Figur nur über die Randmaße der Lösung bekannt
- BW-WRS-2024-B2a: Lage des Streckenzugs aus der Lösung rekonstruiert
- BW-WRS-2024-B3a: Serlo-Lösung (308,27 cm²) vertauscht sin/cos; eigene Lösung ≈ 143,8 cm²; Lage des 160°-Winkels nicht gesichert

## Teilaufgaben ohne P10-Stufe (gezählt, nicht geschrieben)

- quelle-fremd-ni-bw-bw-hs-2021.txt · A1 Nr. 1: Division mit Dezimalzahlen, Überschlag
- quelle-fremd-ni-bw-bw-hs-2021.txt · A1 Nr. 2: Brüche: Gläser zu 1/4 Liter
- quelle-fremd-ni-bw-bw-hs-2021.txt · A1 Nr. 3: Zehnerpotenz
- quelle-fremd-ni-bw-bw-hs-2021.txt · A1 Nr. 5: lineare Gleichung mit Klammer (keine P10-Stufe)
- quelle-fremd-ni-bw-bw-hs-2021.txt · A1 Nr. 6: Diagonalen ins Quadernetz zeichnen
- quelle-fremd-ni-bw-bw-hs-2021.txt · A1 Nr. 7: Flächengleichheit von Parallelogrammen begründen (nur Messen)
- quelle-fremd-ni-bw-bw-hs-2021.txt · A1 Nr. 10: proportionale Zuordnung, Tabelle ergänzen (keine P10-Stufe)
- quelle-fremd-ni-bw-bw-hs-2021.txt · A2 Nr. 2: Oberfläche Pyramide gleich Oberfläche Würfel (keine P10-Stufe für Oberfläche)
- quelle-fremd-ni-bw-bw-hs-2021.txt · B1b: Zaunlänge aus Plan mit Maßstab 1 : 500 und Kosten (keine P10-Stufe)
- quelle-fremd-ni-bw-bw-hs-2021.txt · B2a: größte Fläche aus Zaunteilen (Quadrat)
- quelle-fremd-ni-bw-bw-hs-2021.txt · B4b erster Teil: Dreieck aus WSW konstruieren
- quelle-fremd-ni-bw-bw-hs-2022.txt · A1 Nr. 1: Summe eines Einkaufs
- quelle-fremd-ni-bw-bw-hs-2022.txt · A1 Nr. 2: Bruch zwischen zwei Brüchen
- quelle-fremd-ni-bw-bw-hs-2022.txt · A1 Nr. 4: lineare Gleichung mit Klammer
- quelle-fremd-ni-bw-bw-hs-2022.txt · A1 Nr. 5: Flächengleichheit dreier Figuren begründen (Messen)
- quelle-fremd-ni-bw-bw-hs-2022.txt · A1 Nr. 7: Vierecksarten: jedes Rechteck ist ein Parallelogramm
- quelle-fremd-ni-bw-bw-hs-2022.txt · A2 Nr. 4: Maßstab 1 : 8 am Vogelbild messen
- quelle-fremd-ni-bw-bw-hs-2022.txt · B4a: Division und Zeiteinheiten umrechnen (Fitnessvideo)
- quelle-fremd-ni-bw-bw-hs-2023.txt · A1 Nr. 1: Term für „die Hälfte von 3“
- quelle-fremd-ni-bw-bw-hs-2023.txt · A1 Nr. 2: Zahlenrätsel, lineare Gleichung
- quelle-fremd-ni-bw-bw-hs-2023.txt · A1 Nr. 4: Restbetrag nach Verteilung (Grundrechnen)
- quelle-fremd-ni-bw-bw-hs-2023.txt · A1 Nr. 10: proportionale Zuordnung Farbe/Fläche, Tabelle und Graph
- quelle-fremd-ni-bw-bw-hs-2023.txt · A2 Nr. 3: Winkelhalbierende im stumpfwinkligen Dreieck zeichnen
- quelle-fremd-ni-bw-bw-hs-2023.txt · A2 Nr. 4: antiproportionale Zuordnung
- quelle-fremd-ni-bw-bw-hs-2023.txt · A2 Nr. 5: Ereignisse dem Wahrscheinlichkeitsstreifen zuordnen (qualitativ)
- quelle-fremd-ni-bw-bw-hs-2023.txt · B3: Aufgabe ohne Inhalt in der Quelle
- quelle-fremd-ni-bw-bw-hs-2023.txt · B4b: Maßstab aus Bild bestimmen (Statue)
- quelle-fremd-ni-bw-bw-hs-2023.txt · B5a: Tauchgang-Diagramm ablesen und ergänzen (keine P10-Stufe)
- quelle-fremd-ni-bw-bw-hs-2024.txt · A1 Nr. 1: Rechenkästchen, Abbildung fehlt
- quelle-fremd-ni-bw-bw-hs-2024.txt · A1 Nr. 3: Vorzeichen bei a · b = −2
- quelle-fremd-ni-bw-bw-hs-2024.txt · A1 Nr. 7: lineare Gleichung
- quelle-fremd-ni-bw-bw-hs-2024.txt · A1 Nr. 8: Graph zu einer Geschichte skizzieren (Schulweg)
- quelle-fremd-ni-bw-bw-hs-2024.txt · A1 Nr. 9: Punkte zeichnen und spiegeln
- quelle-fremd-ni-bw-bw-hs-2024.txt · A1 Nr. 10: Diagramm zur Tabelle ankreuzen (Abbildung fehlt)
- quelle-fremd-ni-bw-bw-hs-2024.txt · A2 Nr. 4: proportionale/antiproportionale Tabelle ergänzen
- quelle-fremd-ni-bw-bw-hs-2024.txt · A2 Nr. 5: Ablaufplan einer Umfrage
- quelle-fremd-ni-bw-bw-hs-2024.txt · B2b: Netz eines Prismas skizzieren und Bauklötze packen (Anzahl)
- quelle-fremd-ni-bw-bw-hs-2024.txt · B3a: Amortisation Solaranlage (Grundrechnen)
- quelle-fremd-ni-bw-bw-hs-2024.txt · B3b: Mehlpackungen auf Fußballfeldern (Einheiten, Division)
- quelle-fremd-ni-bw-bw-rs-2021.txt · A1 Nr. 8: Potenzen: Term nachweisen
- quelle-fremd-ni-bw-bw-rs-2021.txt · A1 Nr. 9: Muster mit Kärtchen (Folge)
- quelle-fremd-ni-bw-bw-rs-2021.txt · A1 Nr. 10: Kreisdiagramme Aussagen zuordnen (Abbildung fehlt)
- quelle-fremd-ni-bw-bw-rs-2021.txt · B3a: Erwartungswert eines Kartenspiels (keine P10-Stufe)
- quelle-fremd-ni-bw-bw-rs-2022.txt · A1 Nr. 3: Winkel α ohne Messen (Abbildung fehlt, keine Werte im Text)
- quelle-fremd-ni-bw-bw-rs-2022.txt · A1 Nr. 4: Winkel α ohne Messen (Abbildung fehlt, keine Werte im Text)
- quelle-fremd-ni-bw-bw-rs-2022.txt · A1 Nr. 5: Streckenzug im Würfelnetz
- quelle-fremd-ni-bw-bw-rs-2022.txt · A1 Nr. 6: Höhe eines Hauses (Abbildung fehlt, keine Werte im Text)
- quelle-fremd-ni-bw-bw-rs-2022.txt · A1 Nr. 7: Memory-Wahrscheinlichkeit (Kartenzahl nur in der Abbildung)
- quelle-fremd-ni-bw-bw-rs-2022.txt · A1 Nr. 12: Zehnerpotenzen addieren
- quelle-fremd-ni-bw-bw-rs-2022.txt · A1 Nr. 13: Kärtchenmuster, Term s = n²
- quelle-fremd-ni-bw-bw-rs-2022.txt · B3a Teil 2: Erwartungswert und Gewinnplan
- quelle-fremd-ni-bw-bw-rs-2023.txt · A1 Nr. 1: ohne Inhalt in der Quelle
- quelle-fremd-ni-bw-bw-rs-2023.txt · A1 Nr. 6: Wurzelgleichung mit Platzhalter
- quelle-fremd-ni-bw-bw-rs-2023.txt · A1 Nr. 9: Plättchenmuster und Term
- quelle-fremd-ni-bw-bw-rs-2023.txt · B2b: Mantelflächen Kegel und fünfseitige Pyramide (Kegelmantel, Fünfeck; keine P10-Stufe für die Hauptsache)
- quelle-fremd-ni-bw-bw-rs-2023.txt · B3a Teil 2: Erwartungswert und Änderung der Streifen
- quelle-fremd-ni-bw-bw-rs-2024.txt · A1 Nr. 3: Zehnerpotenzen vergleichen
- quelle-fremd-ni-bw-bw-rs-2024.txt · A1 Nr. 4a: Kärtchenmuster
- quelle-fremd-ni-bw-bw-rs-2024.txt · A1 Nr. 4b: Term zum Muster
- quelle-fremd-ni-bw-bw-rs-2024.txt · A1 Nr. 6a: Boxplot-Fehler finden (Rangliste nur in der Abbildung)
- quelle-fremd-ni-bw-bw-rs-2024.txt · B3a Teil 2: Erwartungswert und fairer Gewinn
- quelle-fremd-ni-bw-bw-wrs-2021.txt · A1 Nr. 4: Streckenzug auf Pyramidennetz übertragen
- quelle-fremd-ni-bw-bw-wrs-2021.txt · A1 Nr. 5: Dreieck konstruieren
- quelle-fremd-ni-bw-bw-wrs-2021.txt · A1 Nr. 7: Wurzel schätzen
- quelle-fremd-ni-bw-bw-wrs-2021.txt · A2 Nr. 2: Strahlensatz (Schatzkarte)
- quelle-fremd-ni-bw-bw-wrs-2021.txt · A2 Nr. 6 Teil 1: Durchschnittsgeschwindigkeit m/s in km/h
- quelle-fremd-ni-bw-bw-wrs-2021.txt · B1 Teil 1: Kugel: Oberfläche und Gewicht (keine P10-Stufe)
- quelle-fremd-ni-bw-bw-wrs-2022.txt · A1 Nr. 7: ohne Inhalt in der Quelle
- quelle-fremd-ni-bw-bw-wrs-2022.txt · A1 Nr. 12: Streckenzug im Würfelnetz
- quelle-fremd-ni-bw-bw-wrs-2022.txt · A1 Nr. 13: Höhe eines Hauses mit Strahlensatz
- quelle-fremd-ni-bw-bw-wrs-2022.txt · A2 Nr. 3 Teil 2: Umlaufbahnen: Tabelle mit Geschwindigkeit und Zeit
- quelle-fremd-ni-bw-bw-wrs-2022.txt · B2b Teil 1: hohle Wachskugel: Kugelvolumen und Gewicht
- quelle-fremd-ni-bw-bw-wrs-2023.txt · A1 Nr. 3: Zehnerpotenzen und Zahlwörter
- quelle-fremd-ni-bw-bw-wrs-2023.txt · A2 Nr. 1: Punktmuster und Term
- quelle-fremd-ni-bw-bw-wrs-2023.txt · A2 Nr. 6 Teil 1: Fahrradtour: Abfahrtszeit aus Strecke und Geschwindigkeit
- quelle-fremd-ni-bw-bw-wrs-2023.txt · B3a Teil 1: Anordnungen von vier Schleifen (Fakultät)
- quelle-fremd-ni-bw-bw-wrs-2023.txt · B4a: Ähnlichkeit und Strahlensatz (keine P10-Stufe)
- quelle-fremd-ni-bw-bw-wrs-2024.txt · A1 Nr. 2: Strahlensatz
- quelle-fremd-ni-bw-bw-wrs-2024.txt · A1 Nr. 4: Maßeinteilung eines Gefäßes (Füllgraph)
- quelle-fremd-ni-bw-bw-wrs-2024.txt · A2 Nr. 1: Streichholzmuster und Term
- quelle-fremd-ni-bw-bw-wrs-2024.txt · A2 Nr. 5: Mittelsenkrechte konstruieren
- quelle-fremd-ni-bw-bw-wrs-2024.txt · A2 Nr. 7: ohne Inhalt in der Quelle
- quelle-fremd-ni-bw-bw-wrs-2024.txt · B3b: Strahlensatz-Verhältnisgleichungen

## Offen

- keine Datei offen; alle zwölf gelesen.
