# Fremdprüfungen VERA 8 (IQB-Aufgabenpool) – Erschließung 06.10.2026

Gruppe vera8, Marke „VERA ’JJ“ mit dem Einsatzjahr aus den Metadaten der IQB-Seite (herausgelöst „nach VERA ’JJ“). Dateien: `vera8.csv` (Aufgaben), `vera8-erkennen.csv` (Sätze für Erkennen-Aufgaben). Quellen: `quellen/quelle-fremd-iqb-vera8-pool-l1.txt` bis `-l5.txt` (Leitideen Zahl, Messen, Raum und Form, Funktionaler Zusammenhang, Daten und Zufall; Jahrgänge 2011–2017). Regeln: aufgabenbank `bau/pruefheft/beschluesse-2026-10-06b.md` (N1, N4). Gebaut mit einem Skript im Scratchpad (nicht im Repo; die CSV ist die Quelle). Modell: Claude Opus 5.5.

VERA 8 ist ein Test für Klasse 8: Die Aufgaben sind kurz (meist ein Schritt, Kopfrechnen) und passen vor allem unten in die Leitern. Aufgaben, die in zwei Leitideen-Archiven liegen, stehen nur unter ihrer ersten Leitidee und sind nur dort gezählt.

## Zahlen

- Zeilen art=ganz: 148; art=herausgeloest: 4; Erkennen-Sätze: 27.
- Lösungen mit sympy nachgerechnet: 127 von 152. Die übrigen 25 haben kein Rechenergebnis (Gleichung aufstellen, Symmetrieachsen zählen, Ablesen, Begründen ohne Zahl, P = 1/6 u. ä.); dort wurde der Kern von Hand gegen die amtliche Auswertung geprüft.
- Teilaufgaben ohne P10-Stufe (nur gezählt): 361 von 509.

| Kapitel | ganz | herausgelöst | erkennen |
|---|---|---|---|
| prozent | 27 | 3 | 16 |
| dreiecke | 10 | 0 | 1 |
| flaechen | 11 | 0 | 0 |
| koerper | 9 | 0 | 0 |
| lineare | 19 | 0 | 3 |
| quadratische | 0 | 0 | 0 |
| gleichungssysteme | 2 | 0 | 0 |
| wachstum | 2 | 1 | 2 |
| daten | 26 | 0 | 0 |
| wahrscheinlichkeit | 42 | 0 | 5 |

## Je Datei

| Datei | Teilaufgaben | Zeilen ganz | ohne Stufe |
|---|---|---|---|
| quelle-fremd-iqb-vera8-pool-l1.txt | 146 | 35 | 111 |
| quelle-fremd-iqb-vera8-pool-l2.txt | 69 | 22 | 47 |
| quelle-fremd-iqb-vera8-pool-l3.txt | 70 | 6 | 64 |
| quelle-fremd-iqb-vera8-pool-l4.txt | 109 | 24 | 85 |
| quelle-fremd-iqb-vera8-pool-l5.txt | 115 | 61 | 54 |

Was ohne Stufe blieb: Zahlbereich und Rechnen (Stellenwert, Runden, negative Zahlen, Brüche, Teilbarkeit, Zahlenmauern, Terme), Größen und Einheiten, Maßstab, Konstruieren und Zeichnen, Koordinaten ohne Funktion, Netze und Ansichten von Würfeln und Quadern (Stufe „Netz erkennen“ meint Prisma/Zylinder/Pyramide der P10; die VERA-Würfelnetze sind Klasse-5-Niveau), proportionale/antiproportionale Zuordnung (Dreisatz), Weg-Zeit-Graphen zuordnen, Diagramme nur ablesen, Muster und Folgen, Begründungen ohne Rechnung.

## Entscheidungen

- Hauptplatz = Handgriff, mit dem die Teilaufgabe anfängt oder den sie prüft. Ankreuzaufgaben behalten die Wahlantworten im Wortlaut.
- Oberfläche (Quader, Würfel aus Würfeln) unter „Mantelfläche mit Kosten“: die Stufe ist die einzige mit Oberfläche als Handgriff; Kosten fehlen.
- Zählaufgaben (Kombinationen, Türme, Zahlen aus Ziffern) unter „Ergebnisse aufzählen“.
- „Würfelsumme ≤ 4“ u. ä. unter „Wahrscheinlichkeit angeben“ mit „Ergebnisse aufzählen“ als zweitem Handgriff.
- Erkennen: zusätzlich zu W/G/p, Zinsen/Zinseszins, mit/ohne Zurücklegen, linear/exponentiell ein Satz zur Winkelfunktion (Gefälle 100 % ⇒ 45°); Pythagoras/Sinussatz kommen in VERA 8 nicht vor.
- Fachwörter umformuliert: „Urne“ → „Beutel“, „Dezimalbruch“ → „Dezimalzahl“, „Rhombus“ weggelassen.
- Marke: Einsatzjahr laut IQB-Metadaten (bei zwei Jahren das jüngere, Thermometer 2017/2015 – ohne Zeile).

## Unsichere Stellen (Textfassung aus Bildern zerlegt)

- VERA-L1-3a/3b: Form der Figuren nicht lesbar; Einteilung (1/3, 2/5) aus der amtlichen Lösung.
- VERA-L1-44a: Aufteilung der Frauen 60/20 auf „zu klein“/„zu groß“ nicht sicher; Lösung (165 von 200) amtlich bestätigt.
- VERA-L1-67b: Zuordnung der Prozentsäulen zu den Parteien aus der amtlichen Lösung (A ≈ 33,4 %).
- VERA-L4-4, L4-43a, L4-48, L4-50, L1-28b: Gleichungen aus zerlegten Formelbildern erschlossen und gegen die amtliche Lösung geprüft.
- VERA-L4-33: Vorzeichen der y-Achsenabschnitte (±3) nicht sicher; Lösung „parallel“ hängt nicht davon ab.
- VERA-L5-11a: Juni-Wert 3 845 aus Gesamtzahl und amtlicher Lösung 5 306 rückgerechnet.
- VERA-L5-30c: Monatszuordnung der Niederschlagswerte nicht lesbar; Spannweite unabhängig davon.
- VERA-L5-38b: Einzelhöhen der drei Säulen nicht lesbar; Mittel 6 cm amtlich.
- VERA-L5-8a: Zuordnung der Tagesstrecken zu den Tagen aus der Textfassung übernommen; Mittelwert 50 km amtlich.

Gelesene Lösungsabschnitte (einzeln per grep): anteileingeometrischenobjekten, kreisefaerben, passendeschuhe, schokoladenfiguren, wahl, steilestrasse, dreieckimquadrat, quader, flaechengleichodernicht, flaecheninhalt, rollrasen, wuerfelkoerper, lagevonzweigeraden, schnittpunktvongraphen, verlaufdesgraphen, punkteaufgeraden, geradenimkoordinatensystem, wosinddiepunkte, rolltreppe, joggen, sauerkraut, linearundproportional, tabelle, heizkosten, computerspielsucht, osterhase, adventskalender, fahrradtour, rotgelbgruen, temperaturen, rubbellose, hausaufgaben, freibad, niederschlaege, saeulenhoehe, schulkleidung, internetauktion, wettkampfwaehlen, prozentanteilschaetzen, rabattaktion, fahrtrichtunggeradeaus, schneekristalle; Kommentierung nur für passendeschuhe, anteileingeometrischenobjekten und vier Aufgaben aus L4 (Gleichungen).
