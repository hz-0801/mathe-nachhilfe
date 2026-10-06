# Fremdprüfungen Bayern (BY)

Stand 06.10.2026. Erschlossen aus 30 Aufgabendateien `quellen/quelle-fremd-bayern-*.txt` (ohne Lösungen): Realschul-Abschlussprüfung Mathematik I und II (rsap-mi, rsap-mii), BMT 10 und BMT 8 (Gymnasium), Jahrgangsstufentest 6 und 8 (Realschule), je 2021–2025. Marke „BY ’JJ“, herausgelöste „nach BY ’JJ“. Regeln: `aufgabenbank/bau/pruefheft/beschluesse-2026-10-06b.md` N1, N4.

## Dateien

- `msa/fremd/bayern.csv` – Aufgaben (art ganz/herausgeloest), Kopf nach Auftrag.
- `msa/fremd/bayern-erkennen.csv` – auf die Frage gekürzte Sätze für Erkennen-Aufgaben (N4.19).

## Zahlen

| Kapitel | ganz | herausgelöst | erkennen |
|---|---|---|---|
| daten | 14 | 0 | 0 |
| dreiecke | 23 | 3 | 19 |
| flaechen | 15 | 0 | 0 |
| gleichungssysteme | 7 | 0 | 0 |
| koerper | 8 | 4 | 0 |
| lineare | 12 | 0 | 0 |
| prozent | 29 | 3 | 28 |
| quadratische | 18 | 0 | 0 |
| wachstum | 6 | 1 | 4 |
| wahrscheinlichkeit | 27 | 0 | 4 |
| **Summe** | 159 | 11 | 55 |

Mit sympy nachgerechnet: 170 von 170 Zeilen (jede Lösung mit mindestens einem Zahlwert gegen die Rechnung geprüft; Begründungs- und Ankreuzaufgaben über den tragenden Zahlwert).

## Je Datei: geschrieben / ohne P10-Stufe

Gezählt sind Teilaufgaben (Nummern mit Punktangabe). „ohne Stufe“ = nicht geschrieben, weil keine P10-Stufe passt.

| Datei | ganz | herausgelöst | ohne Stufe | was ohne Stufe blieb |
|---|---|---|---|---|
| rsap-mi-2021 | 2 | 1 | 18 | A 1.2 Umkehrfunktion; A 2.1–2.4 Trapezschar; A 3.1–3.3 Pyramidenschar im Würfel; B 1.1–1.6 Logarithmusfunktionen; B 2.2–2.5 Dreiecks- und Pyramidenschar |
| rsap-mii-2021 | 5 | 1 | 12 | B 1.2 Kosinussatz und Flächenformel mit Sinus; A 1.1 Bogenlänge, A 1.2 Kreisfigur, A 2.2–2.5 Kreisschar, A 3 Rotationskörper (Kegelstumpf), B 1.4–1.5 Vierecke/Sektor, B 2.1/2.3–2.6 Schrägbild und Pyramidenschar |
| rsap-mi-2022 | 3 | 0 | 15 | A 2.2–2.4 Pyramidenschar; A 3.1–3.3 Pfeile mit Parameter; B 1.1–1.6 Logarithmus; B 2.1–2.5 Rautenschar und Trägergraph |
| rsap-mii-2022 | 6 | 2 | 15 | A 1.1–1.2 Rotationskörper/Masse; A 2.2 Viereck aus zwei Dreiecken mit Sinusformel; A 2.3–2.4 Kreisbogen; A 3.3 Verhältnis; B 1.2–1.6 Drachenschar; B 2.2–2.4, 2.6 Pyramidenschar |
| rsap-mi-2023 | 5 | 1 | 17 | A 1 Parallelogramm mit Pfeilen; A 2.1–2.2 Exponentialfunktion Nullstelle/Asymptote; A 4.1–4.2 Pfeile mit Parameter; B 1.1–1.2 Dreiecksschar; B 3.1–3.6 Exponentialfunktionen; B 4.2–4.5 Pyramidenschar |
| rsap-mii-2023 | 10 | 3 | 14 | A 2.2 Wertemenge; B 1.1 Zeichnen; B 2 Rotationskörper; B 3.2–3.6 Dreiecksschar; B 4.2–4.5 Pyramidenschar |
| rsap-mi-2024 | 4 | 2 | 16 | A 1.1–1.2 Schrägbild/Verzerrung; A 3.1–3.3 Hyperbel; B 1.1–1.2 Logarithmus/Dreiecksschar; B 2.1–2.2 Dreiecksschar im Trapez; B 3.1–3.5 Rechteckschar; B 4.2–4.5 Pyramidenschar |
| rsap-mii-2024 | 8 | 0 | 14 | A 1.1 Scheitelpunktform aus Zeichnung (Bild nicht lesbar); A 1.2 Gerade ohne Schnitt; A 2.1–2.2 Pyramidenschar/Term; B 2.1–2.2 Rotationskörper/Oberfläche; B 3.2–3.6 Dreiecksschar; B 4.1 Zeichnen; B 4.3–4.4 Kreisbogen/Sektor |
| rsap-mi-2025 | 7 | 0 | 17 | A 2.1–2.4 Dreiecks-/Rotationskörperschar; A 3.1 Schwerpunkt; B 2.1–2.3 Prismenschar mit tan; B 3.1–3.6 Exponentialfunktionen/Trapezschar; B 4.1–4.5 Parallelogrammschar |
| rsap-mii-2025 | 16 | 1 | 11 | A 4 Raute begründen; B 3.1 Zeichnen/Winkel begründen; B 3.4–3.6 Kreissektorschar; B 4.2–4.5 Pyramidenschar |
| bmt10-2021 | 9 | 0 | 7 | 1a Exponentialgleichung; 2b, 2c Parabelschar; 3c Maßstab; 4a Skala; 4c Kegelmantel; 5a Laplace-Text |
| bmt10-2022 | 7 | 0 | 8 | 1b Potenzgleichung; 2a–2b Hyperbel; 3b Term begründen; 4a–4b Ereignisalgebra; 5d Proportionalität begründen; 6b Spiegelung; 7 Halbkreise (Pythagoras-Beweis) |
| bmt10-2023 | 5 | 0 | 10 | 2a–2c Vierfeldertafel/Ereignisalgebra; 3a–3c Wertemenge/Wurzel/Potenzfunktion; 4a–4b Bruchterm; 5a Einheiten; 6a sin aus Abbildung; 7 DIN-Format |
| bmt10-2024 | 8 | 0 | 9 | 1a–1b Wurzel/Potenzen; 2b Verschiebung/Wertemenge; 3a–3b Ereignisalgebra; 5b quadratischer Zusammenhang Bremsweg; 7a–7c Hyperbel |
| bmt10-2025 | 7 | 0 | 10 | 1b Term ohne Nullstelle; 2a Laplace; 3a–3c Hyperbel; 4b Einheitskreis; 6a–6c Parabel/Strahlensatz |
| bmt8-2021 | 5 | 0 | 10 | 1a–1b Potenzen; 2a–2b Term; 3 lineare Gleichung; 4b–4c Hohlwürfel deuten; 6b Größenabschätzung; 8a–8b Thales-Beweis |
| bmt8-2022 | 2 | 0 | 15 | 1a–1c Konstruktion; 2 Bruchgleichung; 3 Tabellenkalkulation; 4a–4b Terme; 5b–5d offen: Zuordnung der Prozentwerte zu den Noten im Text nicht lesbar, keine Lösungsdatei; 6a–6b Einheiten; 7a offen: Lage von β nur im Bild; 7c Formel begründen |
| bmt8-2023 | 7 | 0 | 11 | 1a–1c Terme; 2a (in 2b); 3a–3b Raute; 4a–4b Schätzen/Einheiten; 5c Mittelwert-Änderung (s. u.); 7b Höhe zeichnen; 7c Thaleskreis |
| bmt8-2024 | 3 | 0 | 11 | 1a–1b, 2 Gleichung/Term; 3a Säule ergänzen; 4a–4b Maßstab/Konstruktion; 5b Fläche begründen; 6a–6c Zahlen/Tabellenkalkulation; 7a–7b Binom |
| bmt8-2025 | 6 | 0 | 11 | 1a–1b, 3, 4 Terme/Gleichungen; 2a Volumen zusammengesetzt (Maße nur im Bild, offen); 5 Tabellenkalkulation; 7a, 7c Koordinaten (Bild); 8a–8b Kreiswinkel |
| jst6-2021 | 4 | 0 | 15 | 1, 2, 4, 5, 9, 10 Zahlen; 7 Maßstab; 8 Geraden; 11 Würfelnetz; 12 Winkel zeichnen; 14 Dreisatz; 15 Körper; 17 Umfang (Bild); 18 Rechteck ergänzen; 19 Familienkarte |
| jst6-2022 | 2 | 0 | 17 | 1–5, 7, 9 Zahlen; 8 Winkel an Geraden (Bild); 10 Dreisatz; 11, 12 Zeichnen; 14 Vielfaches; 15 Schätzen; 16 Balken ergänzen (Werte nur im Bild); 17 Pyramide Ecken; 18 Maßstab; 19 Flächenfehler (Bild) |
| jst6-2023 | 1 | 0 | 18 | 1–6, 9 Zahlen; 7, 15 Vielfache/Dreisatz; 8 Schätzen; 10, 12, 13, 17 Zeichnen; 11 Körper; 14 Einheiten; 16 Maßstab; 19 Säule ergänzen (Werte nur im Bild) |
| jst6-2024 | 1 | 0 | 18 | 1–8 Zahlen; 9 Quadernetz (Maße im Bild); 10–11 Zeichnen; 12 Würfel; 13 Einheiten; 14 Teiler; 15 Rundung Geld; 16 Dreisatz; 17 Fläche schätzen; 19 Diagramm (Werte nur im Bild) |
| jst6-2025 | 2 | 0 | 17 | 1–8 Zahlen; 10–12 Winkel/Zeichnen (Bild); 13 Pyramide; 14 Massen; 15 Schätzen; 16 Dreisatz; 17 Fläche (Bild); 19 Diagramm ergänzen |
| jst8-2021 | 4 | 0 | 15 | 1, 8 Potenzen; 2, 9 Determinante; 3, 4, 10 Vektoren; 6 Winkel (Bild); 11 Mittelpunkt; 13, 16, 17 Konstruktion; 15 Terme; 18, 19 Ungleichungen; 20 Proportionalität |
| jst8-2022 | 7 | 0 | 12 | 1–3, 13, 16 Terme/Potenzen/Determinante; 4, 8 Winkel (Bild); 5, 9 Ungleichung; 6 Pfeil; 11, 12 Konstruktion; 17 Proportionalität |
| jst8-2023 | 3 | 0 | 17 | 1–3, 12, 18 Terme/Potenzen; 4, 5 Mittelpunkt/Pfeil; 6, 7 Winkel (Bild); 8–10 Konstruktion; 11 Umfangsterm (Bild); 13, 15 Lösungsmenge/Ungleichung; 17 Dreisatz; 20 Diagramm (Werte nur im Bild) |
| jst8-2024 | 7 | 0 | 11 | 1, 2, 13, 14, 16 Terme/Potenzen; 3 Pfeil; 4–6 Winkel (Bild); 8, 9 Konstruktion; 10 Dreisatz (antiproportional); 20 Diagramm (Werte nur im Bild) |
| jst8-2025 | 3 | 0 | 14 | 7 Mittelpunkt; 1–3, 14–16 Terme/Potenzen; 4, 8 Vektoren; 5, 6 Winkel (Bild); 9, 10 Konstruktion; 11 Ungleichung; 12 Gleichung (Vorzeichen nicht lesbar); 13 Weide (Bild); 18 indirekte Proportionalität |

Teilaufgaben ohne P10-Stufe insgesamt: 405. Schwerpunkte: Abbildungsscharen mit Parameter (Punkte P_n, Pyramiden- und Dreiecksscharen, Trägergraph) in rsap-mi/mii, Logarithmus- und Exponentialfunktionen mit Verschiebung, Hyperbeln, Vektoren/Determinanten, Konstruktionen, Terme und Potenzen, Zahlbereich Klasse 6.

## Entscheidungen

- Zeichenaufträge (Schrägbild, Graph zeichnen), die in einer Teilaufgabe neben einer Rechnung stehen, sind weggelassen; die Rechnung trägt die Zeile.
- Teilaufgaben, die selbst nur eine Schar mit Parameter behandeln, aber einen P10-Handgriff als Zwischenschritt brauchen (Pyramidenvolumen, „um 80 % kleiner“, Prozentsatz zweier Volumina), bekommen nur herausgelöste Zeilen; deren `eltern_id` zeigt auf die Original-Teilaufgabe, die keine eigene Zeile hat (in `bemerkung` vermerkt).
- Sie-Form in Du-Form; bayerische Fachwörter umformuliert: Wahlpflichtfächergruppe → Schwerpunkt, Staatsverschuldung → Schulden eines Landes, ausgelastet → besetzt, landwirtschaftliche Betriebe → Bauernhöfe, Gemüsegarten → Gemüsebeet; „Zeige“ in „Berechne“, wo der Zielwert sonst die Aufgabe verrät (rsap-mii-2021 B 1.3).
- Kosinussatz und Flächenformel mit Sinus (rsap-mii-2021 B 1.2, rsap-mii-2022 A 2.2) sind in BB nicht geprüft: ohne Zeile. Sinussatz-Aufgaben stehen unter „Seite berechnen (Sinussatz)“, auch wenn ein Winkel gesucht ist.
- Nächstliegende Stufe ersatzweise: Zählprinzip → „Ergebnisse aufzählen“; Funktionswerte einer Exponentialfunktion → wachstum „Tabelle ergänzen“; Umfang rückwärts → „rückwärts: Seite aus Fläche“; relative Häufigkeit → „Prozentwert“; einfache lineare Gleichungen (jst8) → gleichungssysteme „lösen“ (untere Sprosse, mit „?“ markiert, ob sie dort gewollt sind).
- jst6, jst8 und bmt8 sind Klasse 6/8: Zeilen tragen „Klasse 6“ bzw. „Klasse 8“ in `bemerkung` und sind nur für die unteren Sprossen gedacht.
- Taschenrechnerfreie Teile (rsap ab 2023, Aufgabengruppe A) sind in `bemerkung` als „ohne Taschenrechner“ markiert.
- Werte, die nur in Abbildungen stehen, wurden aus der amtlichen Lösung erschlossen (Lösungsdatei nur abschnittsweise per grep); wo das nicht ging, keine Zeile (z. B. bmt8-2022 5b–5d, bmt8-2025 2a, Diagrammaufgaben jst6/jst8).

## Unsichere Zeilen

- BY-RSAP1-2025-B1a: Ankreuzterme aus zerlegtem Text rekonstruiert (?), Kern: Summe 100 %
- BY-RSAP2-2025-A2c: Vorzeichen der Ankreuzgleichungen aus Text rekonstruiert (?); ohne Taschenrechner
- BY-RSAP2-2025-A3: Vorzeichen von 4x im Text nicht lesbar (?); y_S = 6 und Wertemenge gelten für beide Vorzeichen (amtlich y_S = 6); ohne Taschenrechner
- BY-BMT10-2024-4b: Ankreuzterme aus zerlegtem Text rekonstruiert (?); amtlich „erster Term“
- BY-BMT8-2021-6c: Klasse 8; Prozentpunkte vs. Prozent; Ankreuzbrüche aus zerlegtem Text rekonstruiert (?)
- BY-BMT8-2021-6a: Klasse 8; Art der Darstellung aus Text erschlossen (Tütenbilder) – ?
- BY-JST6-2025-9: Klasse 6; Minuszeichen vor 18 aus Sachzusammenhang (Gefrierschrank) – ?
- BY-JST8-2021-12: Klasse 8; eine Gleichung mit einer Variablen – nur untere Sprosse (?)
- BY-JST8-2022-18: Klasse 8; untere Sprosse (?)
- BY-JST8-2023-14: Klasse 8; untere Sprosse (?)
- BY-JST8-2024-17: Klasse 8; untere Sprosse (?)

## Offen

- keine Datei offen; alle 30 gelesen.
