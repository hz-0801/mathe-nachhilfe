# Eigener Wortlaut Daten (P10)

Stand 2026-10-06. Datei: `msa/wortlaut-eigen-daten.csv`
(id;teil;wortlaut;abbildung;punkte;fundstelle;anmerkung;zwischenfragen).
Nur eigener Wortlaut; die Originaltexte liegen nicht im Repo.

## Auswahl (32 Teilaufgaben + 7 Vorspann-Zeilen = 39 Zeilen)

1. Alle ids der Spalte katalog_ids in `msa/zuordnung-daten.csv`
   (zehn Stufen), 36 ids.
2. Schon in `msa/wortlaut-eigen-prozent.csv` und hier nicht
   wiederholt (4): 2020-OS-K2d, 2021-OS-K5a, 2023-OS-K6c, 2023-OS-K6d.
   Bleiben 32 Teilaufgaben.
3. Prüfstein: 2026-FOR-K3 Benzinpreise (jüngste ganze
   Kontextaufgabe 2022–2026, die überwiegend Daten prüft). Alle
   Teilaufgaben a, b, d, e stehen hier; c (Preissteigerung in
   Prozent) steht in `wortlaut-eigen-prozent.csv`. EBR-Zwilling
   2026-EBR-K4 a–d ist wortgleich (b: „stimmt“ statt „richtig“;
   e fehlt in EBR) und nicht eigens geschrieben; Hinweis in
   anmerkung.

Vorspann-Zeilen: 2014-OS-K4 (Kraftstoff-Tabelle), 2018-OS-K3
(Säulendiagramm Fleisch), 2020-OS-K2 (Schwimmbad), 2022-OS-K4
(Bücher), 2024-OS-K2 (Niederschlag), 2025-OS-K6 (Alter der
Erziehenden), 2026-FOR-K3 (Benzinpreise). 2018-OS-K3a, 2017-OS-K2c,
2021-OS-K5b, 2024-OS-K2c und 2025-OS-K6a holen ihre Tabelle in den
Aufgabentext, weil keine zweite gewählte Teilaufgabe sie braucht.

## Prüfungen

- Kurzlösung: alle 32 Werte mit den Zahlen des neuen Wortlauts
  nachgerechnet (Python): Summe Niederschlag 581,7 mm, Mittel
  48,475 ≈ 48,5; Bücher 2255 : 5 = 451; Schwimmbad 1400 : 7 = 200;
  Benzin Mo–Fr 8,95 : 5 = 1,79; Kita 528 : 11 = 48, ohne 66 und 30
  432 : 9 = 48; 5 : 11 · 360° ≈ 163,6°; Wasser 12 : 508 · 360° ≈ 8,5°.
  Keine Abweichung zur Katalog-Lösung.
- Jede Zeile allein lösbar: Teilaufgaben mit Vorspann verweisen im
  Feld abbildung darauf („aus dem Vorspann“); 2026-FOR-K3e verweist
  auf das Diagramm aus 3d.
- Wortgleiche Folgen: Neun-Wort-Fenster gegen den Text der gelesenen
  Heftseiten (Skript nicht committet). Treffer nur in reinen
  Datenreihen (2017-OS-B1h, 2019-OS-B1i, innermathematisch).
- CSV: 39 + Kopf = 40 Zeilen, je 8 Felder, Trenner `;`, LF.

## Abbildungen

Säulen- und Balkendiagramme im Muster „Säulendiagramm (Achse beginnt
bei …), Größe: Kategorie: Wert, …“; „leer“ heißt: Säule fehlt und
wird vom Schüler gezeichnet. Ein Balkendiagramm ist ein liegendes
Säulendiagramm (Balken waagerecht, Kategorien senkrecht von unten
nach oben in der Reihenfolge der Liste).

Neue Typen:

- **Balkendiagramm** wie Säulendiagramm, waagerecht.
  Sonderfall „(Achse ohne Einteilung), Länge in Kästchen: A: 5,5,
  …“ (2018-OS-K3a): Balkenlängen in Kästchen, Achse ohne Zahlen.
- **Kreisdiagramm**: „Kreisdiagramm: Sektoren im Uhrzeigersinn ab
  12 Uhr: <Beschriftung> <Winkel>°, …“. Beschriftung `[leer]` heißt:
  Sektor ohne Text, mit Schreiblinie; ein Zusatz in der Klammer
  nennt Füllung (grau, gepunktet, schraffiert, dunkel). Richtung und
  Startpunkt können abweichen („gegen den Uhrzeigersinn ab 9 Uhr“,
  2017-OS-K2c, nur ein Sektor eingezeichnet). Winkelsumme 360°.
- **leerer Streifen**: „leerer Streifen: <Länge> lang, <Höhe> hoch,
  auf Karopapier“ (Streifendiagramm zum Selbstzeichnen).
- **leerer Kreis** wie bei Prozent, hier mit Durchmesser (2025-OS-K6b).

## Abgelesene Werte

- 2014-OS-K3d: Säulen bei 70 dpi abgelesen: 1064, 1067, 1069,5
  (Achse 1060–1070, Gitter 1 €). Das Katalogfeld skizze nennt
  1062,5 / 1065 / 1067,5. Für die Aufgabe gleichgültig (Begründung
  ist die abgeschnittene Achse); Befund für den Katalog.
- 2024-OS-K2c: Sektorfolge im Bild ab 12 Uhr im Uhrzeigersinn:
  Körperpflege (181,4°), Sonstiges, Wäsche, Gartenpflege, Toilette,
  Trinken (oben links am Ende). Das Katalogfeld skizze sagt „in
  dieser Reihenfolge“ (Tabellenreihenfolge) – stimmt nicht mit dem
  Bild überein; Befund für den Katalog. Die Lage von „Wäsche
  waschen“ (links unten vor Gartenpflege) stimmt mit der
  Katalog-Lösung überein.
- 2019-OS-K5c: Säulen 44, 42, 40, 39, 36 % wie im Katalog.

## Entscheidungen

- Namen teils geändert (Paul → Jonas, Paolo → Ben, Fabio → Timo,
  Schulz → Becker), Gegenstände und Zahlen nicht.
- 2014-OS-K4 Vorspann: nur die zehn Wochenpreise; die Taxi-Teile c–e
  gehören nicht zum Kapitel.
- Zwischenfragen nur dort, wo die Katalog-Lösung ein Zwischenergebnis
  hat und mehr als ein Handgriff nötig ist.
