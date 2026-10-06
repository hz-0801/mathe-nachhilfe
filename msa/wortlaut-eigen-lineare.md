# Eigener Wortlaut Lineare Funktionen (P10)

Stand 2026-10-06. Datei: `msa/wortlaut-eigen-lineare.csv`
(id;teil;wortlaut;abbildung;punkte;fundstelle;anmerkung;zwischenfragen).
Nur eigener Wortlaut; die Originaltexte liegen nicht im Repo.

## Auswahl (29 Teilaufgaben + 6 Vorspann-Zeilen = 35 Zeilen)

1. Alle ids der Spalte katalog_ids in `msa/zuordnung-lineare.csv`
   (30 ids). Eine davon, 2024-OS-K3c (Punktprobe an der Parabel
   $p(x) = x^2 - 4$), steht auch in `zuordnung-quadratische.csv` und ist
   nur dort geschrieben (`msa/wortlaut-eigen-quadratische.csv`).
2. Prüfstein: 2023-OS-K3 „Umzug“ (Mietwagen-Tarife, 3a Diagramm
   zuordnen, 3b Kosten und Gleichung). Jüngste ganze Kontextaufgabe
   2022–2026, die überwiegend Lineare prüft; beide Teilaufgaben waren
   schon unter den ids. 2026-FOR-K5 und 2025-OS-K5 („Funktionen“) sind
   zur Hälfte bzw. überwiegend Parabel und deshalb nicht Prüfstein hier.

Vorspann-Zeilen: 2016-OS-K6 (Busfirmen, Tabelle und Graphen),
2019-OS-K2 (drei Geraden), 2021-OS-K2 ($y = 3x + 1$), 2021-OS-K6
(Kerze, Tabelle), 2022-OS-K6 (Sparen für den Führerschein),
2023-OS-K3 (Umzug).

Teilaufgaben derselben Aufgabe in anderen Dateien:
2015-OS-K4b, 2017-OS-K5c–e, 2021-OS-K2c, 2022-OS-K3b/c, 2023-OS-K4b/c,
2024-OS-K3b–d, 2025-OS-K5b/c, 2026-FOR-K5c/d →
`wortlaut-eigen-quadratische.csv`; 2016-OS-K6d, 2021-OS-K7b →
`wortlaut-eigen-gleichungssysteme.csv`; 2021-OS-K6b →
`wortlaut-eigen-wachstum.csv`; 2019-OS-K2d → Dreiecke.

## 2026: EBR und FOR

2026-FOR-K5a/b einmal geschrieben. 5b ist mit 2026-EBR-K5b wortgleich.
5a ist in der Rechnung gleich, aber das EBR-Heft gibt ein leeres
Kästchenraster ohne Parabel; das steht in der anmerkung. Der Vorspann
„$f(x) = -2x + 2$“ steht in 5a und 5b selbst, weil die Vorspann-Zeile
2026-FOR-K5 schon in der Quadratik-Datei die Parabel trägt.

## Prüfungen

- Ergebnisse mit sympy gegen kurzloesung des Katalogs: alle 29 stimmen
  (z. B. $h(t) = -5t + 1300$; Reiselust 700 € gegen 725 €, bei 450 km
  875 € gegen 900 €; 19 Monate aus $x \ge 18{,}36$; 178,20 € und
  162,30 €; Schnittpunkt $(1\,|\,2)$, zweiter bei $(-7\,|\,-30)$;
  $f(x) = -1{,}5x + 3$). Keine Abweichung.
- Wortgleiche Folgen (Skript im Scratchpad, nicht committet): Prosa ohne
  Formeln gegen die Heftseite, längste Folge 7 Wörter
  (2021-OS-K7b/2020-OS-K3b in den Nachbardateien); in dieser Datei
  höchstens 6. 2024-OS-B1i hatte 9 und wurde umformuliert.
- CSV parst mit 8 Feldern je Zeile; 35 Zeilen = 29 ids + 6 Vorspann.

## Abbildungen

Typ „Graph:“ mit Term, wo der Term bekannt oder eindeutig ablesbar ist:
2015-OS-K4d (stückweise Parabel/Gerade), 2016-OS-K6 (zwei Tarifgeraden),
2016-OS-B1c (Terme $-1{,}5x + 0{,}5$ und $0{,}5x - 1{,}5$ aus der
Zeichnung des Originals erschlossen), 2019-OS-K2, 2023-OS-K4a
(Parabel $-(x+1)^2 + 6$), 2026-FOR-K5a (Parabel, in die die Gerade
gezeichnet wird). Mehrere Abbildungen in einem Feld trennt „ // “.

Neue Typen (in dieser Datei und den drei Nachbardateien gleich):

| Typ | Form | Bedeutung |
|---|---|---|
| Koordinatensystem | `Koordinatensystem: x a..b; y c..d; Gitter ja; Achsen X \| Y` | leeres System zum Zeichnen; Achsennamen nur, wenn das Original sie trägt |
| Graphauswahl | `Graphauswahl: n Achsenkreuze A–… ohne Einteilung (…): A …; B …` | kleine Skizzen ohne Zahlen zum Ankreuzen; Form je Kurve in Worten |
| Tabellenauswahl | `Tabellenauswahl: …` | mehrere Wertetabellen zum Ankreuzen (nur Quadratik) |
| Achsenkreuz ohne Einteilung | `Achsenkreuz ohne Einteilung: Karoraster …` | Schüler wählt die Skala selbst (nur Wachstum) |
| leeres Karoraster | `leeres Karoraster ohne Achsen (…)` | Schüler zeichnet auch die Achsen (2017-OS-K5a) |

„Graph aus dem Vorspann“ und „Tabelle aus dem Vorspann“ verweisen.
2021-OS-K7a: Im Original verbindet man Kästen mit Linien; hier als
Ankreuztabelle (Sachverhalt × Gleichung), weil das Bauprogramm das zeichnen kann.

## Entscheidungen

- Fundstelle wie Prozent: „P10 <Jahr> · <Nr><Teil>“, FOR mit „FOR“.
- Sternchenaufgaben in anmerkung, wie im Muster.
- Namen: Tom → Lena (2015); Herr Mert, Maxi, Paula, Can, Filip,
  Daniel, Frau Bauer, Wilma übernommen.
- „Anstieg“ (2019) durch „Steigung“ ersetzt.
- zwischenfragen nur bei echten Mehrschritt-Aufgaben; bei
  Einschrittaufgaben (Punktprobe, Zuordnen, Ablesen) leer.
