# Eigener Wortlaut Wachstum (P10)

Stand 2026-10-06. Datei: `msa/wortlaut-eigen-wachstum.csv`
(id;teil;wortlaut;abbildung;punkte;fundstelle;anmerkung;zwischenfragen).
Nur eigener Wortlaut; die Originaltexte liegen nicht im Repo.

## Auswahl (18 Teilaufgaben + 5 Vorspann-Zeilen = 23 Zeilen)

1. ids in `msa/zuordnung-wachstum.csv`: 19. Davon steht 2020-OS-K4c
   (Wasserverbrauch 2033, zwei Studien) schon in
   `msa/wortlaut-eigen-prozent.csv` und ist hier nicht wiederholt.
   Bleiben 18.
2. Prüfstein: 2026-FOR-K7 „Mietkosten“ (7a Tabelle, 7b Graph wählen,
   7c Gleichung und Miete 2040); alle drei Teile schon unter den ids.

Vorspann-Zeilen: 2016-OS-K4 (Technetium), 2017-OS-K7 (Luftdruck),
2019-OS-K7 (Ferkel), 2025-OS-K7 (Bakterien), 2026-FOR-K7 (Miete).

Nicht zugeordnet und daher nicht geschrieben: 2016-OS-K4c/d,
2018-OS-K2b, 2020-OS-K4b. 2021-OS-K6b (Kerze, lineare Abnahme
zeichnen) ist Wachstum zugeordnet; 6a/6c/6d stehen in
`wortlaut-eigen-lineare.csv`.

## 2026: EBR und FOR

7a und 7b wortgleich mit 2026-EBR-K7a/b; 7c nur FOR.

## Prüfungen

- sympy gegen Katalog: 4,45 mg und 4 h; 0,31 mg (genau 0,305);
  757 und 328 hPa; $1000 \cdot 0{,}87^4 \approx 573$; 648 000 €;
  10 / 10,816 / ≈ 12,167 kg; 54 und 59,0; Quotienten 1,40/1,40/1,40/1,40
  und $80 \cdot 1{,}4^{24} \approx 257\,136$; 650,00 € / 687,76 € und
  $650 \cdot 1{,}019^{14} \approx 845{,}96$ €. Keine Abweichung.
- Wortgleiche Folgen: höchstens 7 Wörter (2019-OS-K7c, 2026-FOR-K7b).
  2016-OS-K4e (10) und 7b-Begründungssatz (8) umformuliert.
- CSV parst; 23 Zeilen = 18 ids + 5 Vorspann.

## Abbildungen

Tabellen als „Tabelle: Kopf | …; Zeile | …“, Lücken als „leer“.
Zeichenaufgaben mit selbst gewählter Skala (2016-OS-K4b, 2017-OS-K7b,
2021-OS-K6b) als neuer Typ „Achsenkreuz ohne Einteilung“ mit
Kästchenzahl; die Werte der Tabelle stehen als „Gegeben: …“ im Text,
damit die Zeile ohne die Vorgänger-Teilaufgabe lösbar ist.
2019-OS-K7c und 2026-FOR-K7b als „Graphauswahl“ (Form der Kurven in
Worten, keine Zahlen). Typenliste in `wortlaut-eigen-lineare.md`.

## Entscheidungen

- 2016-OS-K4a: Die zweite Lücke steht im Tabellenkopf (Zeit zu
  3,14 mg); im Wortlaut ausdrücklich genannt.
- 2017-OS-K7d: Bergsteiger → Bergsteigerin.
- 2026-FOR-K7c: $t = 0$ für 2026 (wie Tabelle und Katalog), 2040 also
  $t = 14$.
