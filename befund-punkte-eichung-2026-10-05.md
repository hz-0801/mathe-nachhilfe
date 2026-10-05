# Befund Punkte-Eichung (2026-10-05)

Frage: Taugt die Faustregel „Zwischenergebnisse auf dem Lösungsblatt =
Bewertungsstellen mit Ergebnis; BE ist Obergrenze (höchstens BE − 1 neben
dem Endergebnis)“, und deckt sie sich mit der Handgriff-Regel (je Handgriff
ein Zwischenergebnis; Handgriff = eigene Fertigkeit, ein Kopf-Schritt)?

Daten: `werkzeuge/punkte-eichung.csv` (46 Teilaufgaben), Auswertung
`werkzeuge/punkte-eichung.py`.

## Stichprobe

| Quelle | Stufe | Teilaufgaben |
|---|---|---|
| SH MSA 2023–2026, Korrekturanweisung (`quellen/quelle-fremd-hh-sh-sh-msa-*-loesungen.txt`) | I | 24 |
| BB FHR 2024 B und 2026 C, Lehrerheft mit Gutachtenbogen (Bildungsserver, nicht in `quellen/`) | II | 22 |

Nach Antwortart: Zahl 17, Nachweis 11, Begründen 6, Term 6, Beurteilen 3,
Grafik 3. BE 1–8, 36 Teilaufgaben mit BE ≤ 4.

Nicht verwendbar, weil ohne Punkte je Schritt: NI-Erwartungshorizonte
(Punkte nur je Teilaufgabe), HH-MSA-Beispiele, NRW ZP10 (Serlo-Fassung ohne
Punkte), IQB-Abiturpool (`abitur/iqb.md` § 2: „keine Punkteaufteilung“),
P10-Musteraufgaben 2028 (Text nur in `hefte/`, nicht im Repo).

Zählweise: Stelle = kleinste sichtbare Punkteinheit (SH: Marke „(1)“;
FHR: BE der Gutachtenzeile, nach Erwartungshorizont auf Ergebnisse
verteilt). Mehrere Punkte am selben Ergebnis zählen einmal „mit Ergebnis“,
der Rest als Teilkriterium. `erg_ewh` = alle Ergebnisse, die der
Erwartungshorizont hinschreibt, auch unbepunktete. Handgriffe = eigenes
Urteil; ein Handgriff, der zweimal läuft (Punktprobe für zwei Punkte),
zählt einmal.

## Quoten

| Prüfung | alle | Sek I | Sek II | BE ≤ 4 | BE ≥ 5 |
|---|---|---|---|---|---|
| (a) Stellen mit Ergebnis ≤ BE | 100 % | 100 % | 100 % | 100 % | 100 % |
| (a2) Ergebnisse im EWH ≤ BE | 93 % | 100 % | 86 % | 100 % | 70 % |
| (b) Stellen mit Ergebnis = Handgriffe | 63 % | 79 % | 45 % | 72 % | 30 % |
| (c) dieselbe ± 1 | 87 % | 100 % | 73 % | 100 % | 40 % |

Je Antwortart (b / c): Zahl 53 / 88 %, Nachweis 55 / 82 %, Term 67 / 67 %,
Begründen 83 / 100 %, Beurteilen 100 / 100 %, Grafik 67 / 100 %.

Punkte ohne Ergebnis: 27 von 149 BE (18 %): Ansatz/Formel 11,
Darstellungskriterien einer Grafik 10, Teilkriterium eines Terms oder einer
Beschreibung 2, Begründungsform 2, Verfahrensschritt ohne Wert 2.

## Urteil

1. Die Obergrenze hält: In keiner Teilaufgabe gibt es mehr bepunktete
   Ergebnisse als BE. Nur drei FHR-Teilaufgaben mit 5–8 BE schreiben im
   Erwartungshorizont mehr Ergebnisse hin, als es BE gibt (Wendepunkte,
   Extrempunkte, Achsenschnitte) – dort bündelt eine BE mehrere gleichartige
   Werte.
2. Gleichheit mit der Handgriff-Regel liegt unter 70 % (63 %), mit ± 1 bei
   87 %. Bis BE 4 ist die Übereinstimmung gut (72 % genau, 100 % ± 1); ab
   BE 5 kippt sie (30 % / 40 %). Grund ist fast immer derselbe: die
   Prüfung gibt je Wiederholung desselben Handgriffs einen Punkt (drei
   Ableitungen, drei Wendepunkte, zwei Punktproben), die Handgriff-Regel
   zählt den Handgriff einmal. Umgekehrt (weniger Punkte als Handgriffe,
   3 Fälle) steht ein Handgriff ohne eigenen Punkt: Gleichung aus der
   Sachlage aufstellen, Daten ordnen, Maßstab im Netz.
3. Beide Regeln sind also nicht dasselbe, aber verträglich: Die
   Handgriff-Regel liefert die Mindestzahl der Zeilen, die BE die
   Höchstzahl. Wo ein Handgriff mehrfach läuft, zeigt das Lösungsblatt
   jedes Ergebnis (wie der Erwartungshorizont), nicht nur das erste.
4. Wofür es Punkte ohne Ergebnis gibt: vor allem für den Ansatz (Formel,
   Gleichung, Modellwahl) und für die Darstellungsqualität von Grafiken.
   Antwortsatz und Einheit sind in beiden Quellen keine eigenen Stellen,
   sondern Abzüge (NI: je ½ P., höchstens 3).

## Formulierung für die Lösungsblatt-Regeln

> Zwischenergebnisse: je Handgriff, den die Teilaufgabe durchläuft, ein
> Zwischenergebnis; läuft derselbe Handgriff mehrmals (mehrere Punkte,
> Stellen, Ableitungen), steht jedes Ergebnis. Die BE der Teilaufgabe sind
> die Obergrenze: höchstens BE Zeilen mit Ergebnis, das Endergebnis
> eingeschlossen. Ein Ansatz (Formel, Gleichung, Modell) steht als eigene
> Zeile, wenn er aus der Sachlage aufgestellt wird; eine bloß eingesetzte
> Formel steht nicht eigens. Bei Grafiken nennt das Lösungsblatt die
> Merkmale, auf die es ankommt (Maßstab, Achsen, markante Punkte), statt
> Zwischenergebnisse.

Grenzen: Handgriffzählung ist Urteil (eine Lesart je Zeile); SH-Formeln
sind im Textauszug teils verloren (Marken lesbar, B1-Zeilen nach Marken
gezählt); FHR-Gutachtenzeilen mit mehreren BE wurden nach dem
Erwartungshorizont auf Ergebnisse verteilt.
