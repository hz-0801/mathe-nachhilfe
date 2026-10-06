# Eigener Wortlaut Wahrscheinlichkeit (P10)

Stand 2026-10-06. Datei: `msa/wortlaut-eigen-wahrscheinlichkeit.csv`
(id;teil;wortlaut;abbildung;punkte;fundstelle;anmerkung;zwischenfragen).
Nur eigener Wortlaut; die Originaltexte liegen nicht im Repo.

## Auswahl (33 Teilaufgaben + 7 Vorspann-Zeilen = 40 Zeilen)

1. Alle ids der Spalte katalog_ids in
   `msa/zuordnung-wahrscheinlichkeit.csv` (sieben Stufen), 33 ids.
   Keine davon steht in einer anderen wortlaut-eigen-*.csv.
2. Prüfstein: 2026-FOR-K6 Würfel (jüngste ganze Kontextaufgabe
   2022–2026, die überwiegend Wahrscheinlichkeit prüft), Teilaufgaben
   a–d, alle schon über die Zuordnung gewählt. EBR-Zwilling
   2026-EBR-K6 a und b ist wortgleich und nicht eigens geschrieben;
   Hinweis in anmerkung.

Vorspann-Zeilen: 2014-OS-K6 (Glücksrad), 2016-OS-K5 (Lose 101–900),
2019-OS-K6 (Buntstifte), 2020-OS-K6 (zwei Würfe), 2024-OS-K5
(Hausarbeit-Zettel), 2025-OS-K3 (Zahlenscheiben), 2026-FOR-K6
(Würfelnetze). 2018-OS-K7b und K7c holen den Kontext in den Text
(K7a ist Prozent und steht in `wortlaut-eigen-prozent.csv`).

## Prüfungen

- Kurzlösung: alle Werte mit Brüchen nachgerechnet (Python
  fractions): 13/32; 3/11; 91/120; 4/20 · 3/19 · 2/18 ≈ 0,35 %;
  1/57 gegen 1/1140; 16/216 = 2/27; 1 − 3/36 = 11/12; 15/36 = 5/12;
  1/5 (Klara); 5/16. Keine Abweichung zur Katalog-Lösung.
- Wortgleiche Folgen: Neun-Wort-Fenster gegen den Text der gelesenen
  Heftseiten; ein Treffer (2024-OS-K5c) umformuliert, danach keiner.
- CSV: 40 + Kopf = 41 Zeilen, je 8 Felder, Trenner `;`, LF.

## Neue Abbildungstypen

- **Glücksrad**: „Glücksrad: <n> gleich große Felder, im
  Uhrzeigersinn ab 12 Uhr: A, B, …; Zeiger oben“. Bei ungleichen
  Feldern Winkel je Feld angeben („A 90°“).
- **Baumdiagramm**: „Baumdiagramm (Stufen: <Name 1> | <Name 2> | …;
  Äste <a>, <b>): <Pfad>: <Wert>; …“. Ein Pfad ist die Folge der
  Astnamen mit `>` (z. B. `nR>nR>R`); Wert ist ein Bruch, `leer`
  (Eintragfeld) oder fehlt („übrige Äste ohne Eintrag“ = Ast
  gezeichnet, kein Feld). „nur X verzweigt weiter“ heißt: andere
  Äste enden. „Pfad fett“ markiert einen hervorgehobenen Pfad.
  „alle 14 Äste leer“: voller Baum, jeder Ast mit Eintragfeld.
- **Zahlenscheiben**: zwei Kreisscheiben mit je n gleich großen
  Sektoren, Pfeil oben, Ziffern im Uhrzeigersinn ab 12 Uhr; „alle
  Sektoren leer (Eintragfeld)“ für die Entwurfsaufgabe.
- **Würfelnetze**: Kreuznetz (Reihe aus vier Feldern, je ein Feld
  über und unter dem zweiten Feld); je Würfel „oben x; Reihe a, b,
  c, d; unten y“; mehrere Würfel mit „|“ getrennt; „alle Felder
  leer“ für ein Netz zum Beschriften.
- **Gefäße** (2015-OS-B1a, 2019-OS-B1g): Töpfe mit Kugelzahl je
  Farbe; der Inhalt steht zusätzlich im Text, damit die Zeile auch
  ohne Bild lösbar ist.
- **Gewinnplan-Kasten** (2016-OS-K5): einfacher Textkasten.

Ankreuztabelle wie bei Prozent (2019-OS-K6b, Spalten wahr | falsch).

## Entscheidungen

- Bilder, die nur Schmuck sind (Würfel 2014, Münzen 2017, Zahlenschloss
  2017, Zettel 2024, kleines Glücksrad 2018), nicht beschrieben.
- 2016-OS-K5 Vorspann: nur der Gewinnplan; 5a und 5b (Ziffernkapseln,
  Abzählen) gehören nicht zur Zuordnung.
- 2019-OS-K6b: Der Baum im Original zeigt nur die nötigen Felder; die
  Beschreibung nennt die beiden leeren Stellen (Stufe 1 „nicht rot“,
  Pfad nicht rot > rot > rot) und den fetten Pfad rot > rot > rot.
- 2026-FOR-K6c: Ereignis E umformuliert („Nicht beide Würfel zeigen
  eine gerade Zahl“), gleichwertig zu „nicht zweimal gerade“.
- Namen der Kontexte belassen (Spielfiguren der Aufgabe); Terme wörtlich.
