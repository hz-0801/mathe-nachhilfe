# Eigener Wortlaut Quadratische Funktionen (P10)

Stand 2026-10-06. Datei: `msa/wortlaut-eigen-quadratische.csv`
(id;teil;wortlaut;abbildung;punkte;fundstelle;anmerkung;zwischenfragen).
Nur eigener Wortlaut; die Originaltexte liegen nicht im Repo.

## Auswahl (32 Teilaufgaben + 8 Vorspann-Zeilen = 40 Zeilen)

1. Alle ids der Spalte katalog_ids in `msa/zuordnung-quadratische.csv`
   (32 ids), darunter 2024-OS-K3c, die auch Lineare zugeordnet ist
   (hier einmal geschrieben).
2. Prüfstein: 2025-OS-K5 „Funktionen“ (5b Scheitel und
   Scheitelpunktform, 5c Nullstellen; 6 von 10 Punkten Parabel). Die
   jüngere 2026-FOR-K5 ist zur Hälfte Gerade (4 von 8 Punkten), daher
   nicht „überwiegend“. Alle Teilaufgaben von 2025-OS-K5 sind
   geschrieben: 5b/5c hier, 5a (Gerade) in
   `wortlaut-eigen-lineare.csv`.

Vorspann-Zeilen: 2014-OS-K7, 2017-OS-K5, 2018-OS-K5, 2020-OS-K3,
2022-OS-K3, 2024-OS-K3, 2025-OS-K5, 2026-FOR-K5.

Teilaufgaben derselben Aufgabe in anderen Dateien: 2015-OS-K4d,
2017-OS-K5a/b, 2021-OS-K2a/b, 2022-OS-K3a, 2023-OS-K4a, 2024-OS-K3a,
2025-OS-K5a, 2026-FOR-K5a/b → `wortlaut-eigen-lineare.csv`.

## 2026: EBR und FOR

2026-FOR-B1e und 2026-FOR-K5c sind mit EBR-B1e und EBR-K5c wortgleich
(anmerkung „EBR-Zwilling …“). 5d gibt es nur im FOR-Heft.

## Prüfungen

- sympy gegen kurzloesung: alle 32 stimmen (z. B. $x = -3 \pm \sqrt2$;
  $q: y = -(x+3)^2$; D ist der Punkt außerhalb, $f(-1{,}5) = -3{,}75$;
  $p$ gespiegelt $y = (x-2)^2 - 4$; Schnittpunkte $(-1|-2), (2|7)$;
  $(-1|5), (3|-3)$; $(-1|-3), (5|21)$; $x = -5$ und $3$;
  $3 \pm \sqrt2 \approx 1{,}59; 4{,}41$; $p$ und $q$ nur $x = 2$
  gemeinsam). Keine Abweichung.
- Wortgleiche Folgen: höchstens 7 Wörter ohne Formeln (2020-OS-K3b:
  „… liegt nicht auf dem Graphen von $f$“). 2015-OS-K4b und der
  Vorspann 2020-OS-K3 hatten 8 und wurden umformuliert.
- CSV parst; 40 Zeilen = 32 ids + 8 Vorspann.

## Abbildungen

„Graph:“ mit Term bei allen gezeichneten Parabeln: $-x^2$ mit
$2x - 3$ (2014), $x^2$ (2015-B1i), Fallschirm stückweise (2015-K4b),
$(x+3)^2 - 2$, $x^2 - 4x + 2$, $(x+2)^2 - 4$, $(x+2)^2 - 1$,
$-(x+1)^2 + 6$, $x^2 - 6x + 7$, $(x-2)^2 - 2$. Leere Systeme als
„Koordinatensystem: …“ (2018-OS-K5d, 2024-OS-K3b). 2026-FOR-B1e als
neuer Typ „Tabellenauswahl“ (drei Wertetabellen zum Ankreuzen). Liste der
neuen Typen in `wortlaut-eigen-lineare.md`.

## Entscheidungen

- Antwortfelder „S( | )“ als $S(\ \ |\ \ )$ im Text.
- $q'$ als $q^{\prime}$ (kein Apostroph im CSV-Feld).
- 2024-OS-K3b: Im Original dasselbe System wie die Gerade 3a; hier
  eigenes leeres System, damit die Zeile allein lösbar ist.
- 2015-OS-K4b: Name Tom → Lena wie in 4d.
