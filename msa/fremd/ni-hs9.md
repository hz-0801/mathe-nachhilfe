# Fremdprüfungen ni-hs9 – Niedersachsen Hauptschulabschluss Kl. 9 (E- und G-Kurs) 2022–2026

Auftrag Fremdprüfungen 06.10.2026. Marke „NI ’JJ“, herausgelöst „nach NI ’JJ“. Niveau unter P10 (Hauptschule Kl. 9): eher für untere Sprossen.

## Gelesen

Zehn Aufgabendateien je einmal: `quellen/quelle-fremd-ni-bw-ni-hs9e-2022…2026.txt`, `quelle-fremd-ni-bw-ni-hs9g-2022…2026.txt`. Lösungsdateien nur abschnittsweise (Erwartungshorizont Hauptteil 2/Wahlteil per grep/sed), um Maße zu erschließen, die nur in Abbildungen stehen, und eigene Ergebnisse gegenzuprüfen.

## Ergebnis

- `ni-hs9.csv`: 225 Zeilen, davon 218 ganz, 7 herausgelöst.
- `ni-hs9-erkennen.csv`: 46 Sätze.

| Kapitel | ganz | herausgelöst | erkennen |
|---|---|---|---|
| daten | 28 | 0 | 0 |
| dreiecke | 11 | 0 | 10 |
| flaechen | 30 | 1 | 0 |
| koerper | 18 | 2 | 0 |
| lineare | 38 | 0 | 3 |
| prozent | 39 | 4 | 24 |
| wahrscheinlichkeit | 54 | 0 | 9 |

Keine Zeilen in quadratische, gleichungssysteme, wachstum: Die Hefte haben dazu keine Aufgaben.

## Prüfung

- CSV parst mit 17 Feldern je Zeile; keine id doppelt; jede stufe und jeder handgriff steht in der Zuordnungsdatei des Kapitels; jede eltern_id existiert.
- Lösungen: 209 mit sympy nachgerechnet (exakte Rechnung oder Rundung auf 0,005 gegen den Lösungswert); 16 ohne Rechnung (reine Ablese- oder Begründungsaufgaben, etwa Baum ergänzen, Säule ergänzen). Alle Werte zusätzlich gegen den amtlichen Erwartungshorizont gehalten.
- Ein eigener Fehler fiel dabei auf und ist behoben: G-2022 W4b Durchschnittsnote 2,65 (nicht 2,55).

## Entscheidungen

- Hauptteil 1 ist in jedem Jahr für E- und G-Kurs wortgleich; erfasst nur unter E. Gleiche Teilaufgaben in Hauptteil 2/Wahlteil (z. B. Dose 2026, Gutscheine 2025) nur einmal; abweichende Zahlen im G-Kurs bekommen eine eigene Zeile.
- Maße, die nur im Bild stehen, aus dem Erwartungshorizont erschlossen und in `bemerkung` vermerkt (NI-HS9E-2022-H2A6a, NI-HS9E-2022-W1c, NI-HS9E-2022-W2a, NI-HS9G-2022-H2A1a, NI-HS9G-2022-H2A6a, NI-HS9G-2022-W2a, NI-HS9E-2023-H2A2b, NI-HS9E-2023-H2A4a, NI-HS9E-2023-W1d, NI-HS9G-2023-W1c, NI-HS9G-2023-W2b, NI-HS9G-2023-W3d, NI-HS9E-2024-H2A1a, NI-HS9E-2024-H2A3a, NI-HS9E-2024-W3b, NI-HS9G-2024-H2A3a, NI-HS9G-2024-W1b, NI-HS9G-2024-W3b, NI-HS9E-2025-H2A5a, NI-HS9E-2025-W1a, NI-HS9E-2025-W3a, NI-HS9E-2025-W4b, NI-HS9G-2025-W1a, NI-HS9E-2026-H2A1d, NI-HS9E-2026-W4a).
- Stufen nächstliegend gewählt und vermerkt: Schnittpunkt zweier Sachgeraden → lineare „Tarife vergleichen“; Kreisradius aus Umfang → flaechen „rückwärts: Seite aus Fläche“; Oberfläche Zylinder/Quader → koerper „Mantelfläche mit Kosten“; Differenz zweier Werte → daten „Minimum, Maximum, Spannweite“; Wertetabelle einer Sachgeraden → lineare „aus Gleichung zeichnen“ bzw. „Endwert berechnen“.
- Lineare Einzelgleichungen (Waage, Fehler finden) passen zu keiner P10-Stufe (gleichungssysteme meint Systeme) und sind nicht erfasst.
- Fachwörter: „arithmetisches Mittel“ → Durchschnitt; „absolute Häufigkeit“ → Anzahl; „Dodekaeder“ → Würfel mit 12 Flächen; Ziehen als „Tüte“/„Box“ beibehalten.
- Herausgelöst nur dort, wo ein P10-Handgriff als echter Zwischenschritt in einer längeren Aufgabe steckt (7 Fälle); bei den meist kurzen NI-Aufgaben ist der Handgriff fast immer schon die ganze Aufgabe.

## Unsichere Zeilen

- NI-HS9E-2022-H2A1a: Welche Säulen im Original fehlen, ist aus dem Text nicht sicher; Werte April/Juni aus der Lösung
- NI-HS9G-2024-W3c: Lösung nennt zwei Lücken mit 3/8; Lage im Baum unsicher
- NI-HS9G-2025-W1a: Zuordnung der Zahlen zu den Spalten aus Lösung 1a/1b erschlossen; Hinweis „genauso beliebt“ ergänzt, weil die Spaltenzuordnung im Text unsicher ist
- NI-HS9E-2026-W2b: welche zwei Felder leer sind, aus dem Text nicht sicher
- NI-HS9E-2026-W3b: Grundgebühr im Original nur über die Parallele zum Graphen; Lage der Lücken unsicher
- NI-HS9E-2024-H2A3a/3c: Becher im Original vermutlich kegelstumpfförmig gezeichnet; hier als Rechteck im Schnitt (7 cm × 3 cm) vereinfacht, Ergebnisse 7,62 cm und 8,49 cm stimmen mit dem Erwartungshorizont.
- NI-HS9G-2024-W4b: amtlich 53,41 Randsteine ohne Aufrunden; hier 54.

## Teilaufgaben ohne P10-Stufe (nicht geschrieben)

Gezählt nach der Liste unten: 293 Teilaufgaben nicht geschrieben – 172 ohne passende P10-Stufe oder mit unlesbarer Abbildung (Grundrechnen, Einheiten, Runden, Fahrpläne, Rezepte, Preise, Zuordnungen, sicher/möglich/unmöglich, Netze und Karofiguren nur als Bild) und 121 in Zeilen mit Dubletten zwischen E- und G-Kurs (davon 85 aus den wortgleichen Hauptteilen 1; einige Zeilen mischen Dublette und keine Stufe).

| Datei | Teilaufgaben | Grund |
|---|---|---|
| hs9e-2022.txt | H1 1a–c, 2a–c, 3a–b | schriftlich rechnen, Zahlenfolgen, Überschlag – keine P10-Stufe |
| hs9e-2022.txt | H1 4a–b | Prisma Ecken/Kanten, Aussagen – keine P10-Stufe |
| hs9e-2022.txt | H1 5a–b | Würfelgebäude zählen – Abbildung nicht als Text lesbar, keine P10-Stufe |
| hs9e-2022.txt | H1 6a–d, 7a–b, 8a–b | Fahrplan, Einheiten, Proportionalität – keine P10-Stufe |
| hs9e-2022.txt | H2 2a, 5a | Preisvergleich, Materialkosten – keine P10-Stufe |
| hs9e-2022.txt | H2 4a, 4b, 4d | Weg-Zeit-Graph nur als Bild, Abschnitte nicht lesbar |
| hs9e-2022.txt | W2d–f | Skizze der Tonne; Graph Tonne A/B nicht lesbar |
| hs9e-2022.txt | W4c | Diagramm der Kritikpunkte nicht lesbar |
| hs9g-2022.txt | H1 1–8 (13 Teilaufgaben) | wortgleich mit E-Kurs, Dublette |
| hs9g-2022.txt | H2 2a, 3a, 4a–d, 5b | Skizze, Preisvergleich, Weg-Zeit-Graph, Materialkosten – keine P10-Stufe oder Bild nicht lesbar |
| hs9g-2022.txt | H2 5c, W3c, W3d | gleich wie E-Kurs H2 5c, W3a, W3b – Dublette |
| hs9g-2022.txt | W1a, W1d, W1e, W2e–g, W3a, W4c, W4d | Skizze/Maß eintragen, Figuren auf Fläche, Graphen nicht lesbar, sicher/möglich/unmöglich – keine P10-Stufe |
| hs9e-2023.txt | H1 1a–c, 2a–c, 3, 4a–c, 5a–b | Zahlenstrahl, Ergänzen, Temperaturen, schriftlich rechnen, Größen – keine P10-Stufe |
| hs9e-2023.txt | H1 6a–c | lineare Gleichung (Waage, Fehler finden) – keine P10-Stufe (gleichungssysteme meint Systeme) |
| hs9e-2023.txt | H1 7a–c | Kanten markieren, Netz ankreuzen, Prisma-Aussagen – Netze nur als Bild, nicht lesbar |
| hs9e-2023.txt | H2 1a–c | Preise Kletterpark – keine P10-Stufe |
| hs9e-2023.txt | H2 4c | Umrechnung in Zoll – keine P10-Stufe |
| hs9e-2023.txt | H2 6b, 6c | abschnittsweiser Füllgraph, Gefäße zuordnen – keine P10-Stufe bzw. Bild nicht lesbar |
| hs9e-2023.txt | W1a, W1b | Rezept hochrechnen, Verkaufspreis – keine P10-Stufe |
| hs9e-2023.txt | W4a, W4d | sicher/möglich/unmöglich, Erklärung – keine P10-Stufe |
| hs9g-2023.txt | H1 1–7 (18 Teilaufgaben) | wortgleich mit E-Kurs, Dublette |
| hs9g-2023.txt | H2 1a–c, 4b | Preise Kletterpark, abschnittsweiser Füllgraph – keine P10-Stufe |
| hs9g-2023.txt | W1a, W1b, W2e, W3c, W4a, W4e | Rezept, Gewinn, Begründung ohne Rechnung, Jahreslohn, sicher/möglich – keine P10-Stufe |
| hs9e-2024.txt | H1 1a–b, 2a–b, 3a–b, 4, 6, 8 | Rechentafeln, schriftlich rechnen, Einheiten, Zahlenreihen, Gleichung ankreuzen, Fehler finden – keine P10-Stufe |
| hs9e-2024.txt | H1 7a–c | Viereck auf Karos – Figur nur als Bild, Maße nicht lesbar |
| hs9e-2024.txt | H2 1b, 2a–c, 4a, 4c, 5c | Eimer runden, Bausteinturm, Einwohner ausschreiben, Dichte, Funktionstyp – keine P10-Stufe |
| hs9e-2024.txt | W1d, W3a | Plausibilität Blutspende, Glücksrad-Aussagen ohne lesbares Bild – keine P10-Stufe bzw. Bild nicht lesbar |
| hs9g-2024.txt | H1 1–8 (15 Teilaufgaben) | wortgleich mit E-Kurs, Dublette (nur H1 5 einmal unter E erfasst) |
| hs9g-2024.txt | H2 1b, 1c, 2a–c, 3b, 4a, 4c | Eimer, Kosten, Bausteine, Körper ankreuzen, Netz skizzieren, Einwohner – keine P10-Stufe |
| hs9g-2024.txt | H2 5b, W2c, W4c, W4d | gleich wie E-Kurs (Gleichung, Zylindervolumen, Grillecke, Bruce) – Dublette |
| hs9g-2024.txt | W1e, W3a | Schaubild ohne Werte, sicher/möglich/unmöglich – keine P10-Stufe |
| hs9e-2025.txt | H1 1a–b, 2a–d, 3a–d, 4a–c, 5a–b, 6a–b, 7a–b | schriftlich rechnen, Einheiten, Vergleichen, Runden, Einkauf, Winkel messen/Nebenwinkel, Schrägbild – keine P10-Stufe |
| hs9e-2025.txt | H2 3a–c | Werkstück aus Würfel und Zylinder – Maße nur im Bild, nicht lesbar; Dichte keine P10-Stufe |
| hs9e-2025.txt | H2 4a–c, 6a–c | Eintrittspreise, Einkauf/Milchshakes – keine P10-Stufe |
| hs9e-2025.txt | W2c, W4a, W4d | Pfad markieren, Grundfläche begründen, Oberfläche Prisma – keine passende Stufe |
| hs9g-2025.txt | H1 1–7 (21 Teilaufgaben) | wortgleich mit E-Kurs, Dublette |
| hs9g-2025.txt | H2 1b, 3a–c, 4a–c, W2a–d, W3b–c | gleich wie E-Kurs bzw. Maße nicht lesbar – Dublette |
| hs9g-2025.txt | H2 6a–b, W3a, W4a–d | Rezept, Einkauf, Achsen beschriften, Zelt (Maße nicht vollständig lesbar) – keine P10-Stufe |
| hs9e-2026.txt | H1 1a–d, 2, 3, 4a–b, 6a–c, 8a–c | Kopfrechnen, Einheiten, Überschlag, Rezept, Busfahrplan, Tische/Stühle-Term – keine P10-Stufe |
| hs9e-2026.txt | H1 7a–b | Dreieck auf Karos – Maße nur im Bild, nicht lesbar |
| hs9e-2026.txt | H2 1b, 5c | Name ablesen, 330 mℓ passen – zu klein bzw. keine eigene Stufe |
| hs9e-2026.txt | W2d, W4d | Term aus Bild nicht lesbar; Kartonbild nicht lesbar |
| hs9g-2026.txt | H1 1–8 (18 Teilaufgaben) | wortgleich mit E-Kurs, Dublette (nur H1 5 einmal unter E erfasst) |
| hs9g-2026.txt | H2 1b, 1c, 2b, 2c, 4a, 4c, 5a, 5b, 5d, W1a, W1b, W3d | gleich wie E-Kurs, Begriffe zuordnen, Grundfläche markieren, Variablen deuten – Dublette oder keine P10-Stufe |
| hs9g-2026.txt | W4a, W4c, W4d, W4e | Körperform ankreuzen, Netz ergänzen, Pappe (gleich E-Kurs), Stapel aus Bild – keine P10-Stufe bzw. Dublette |

