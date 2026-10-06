# Eigener Wortlaut Dreiecke (P10)

Stand 2026-10-06. Datei: `msa/wortlaut-eigen-dreiecke.csv`
(id;teil;wortlaut;abbildung;punkte;fundstelle;anmerkung;zwischenfragen).
Nur eigener Wortlaut; die Originaltexte liegen nicht im Repo.

## Auswahl (59 Teilaufgaben + 11 Vorspann-Zeilen = 70 Zeilen)

1. Alle ids aus Spalte katalog_ids von `msa/zuordnung-dreiecke.csv`
   (Haupt- und Nebenplätze): 66 Nennungen, 59 verschiedene ids.
2. Prüfstein: 2026-FOR-K4 (Viereck/Parallelogramm, Höhe h, ε, AC) –
   jüngste ganze Kontextaufgabe, alle drei Teile Dreiecke; 4a–4c
   stehen schon in der Zuordnung, keine zusätzlichen Zeilen.
3. EBR-Zwillinge einmal geschrieben (anmerkung „EBR-Zwilling …“):
   2026-EBR-B1c, B1i, B1j, K3a, K3b.
4. Vorspann-Zeilen: 2015-OS-K5, 2016-OS-K7, 2017-OS-K4, 2018-OS-K4,
   2019-OS-K3, 2021-OS-K3, 2022-OS-K5, 2023-OS-K7, 2024-OS-K6,
   2025-OS-K2, 2026-FOR-K4.

Nicht gewählte Nachbarteile (nicht in der Zuordnung): 2014-OS-K2a,
2016-OS-K7a, 2018-OS-K4a, 2024-OS-K6c. Teile anderer Kapitel derselben
Aufgabe stehen dort: 2015-OS-K5d, 2020-OS-K7b, 2022-OS-K5e, 2023-OS-K2b/c,
2025-OS-K2b in `wortlaut-eigen-flaechen.csv`; 2022-OS-K2a/b/d,
2026-FOR-K2a/b/d, 2020-OS-K5a in `wortlaut-eigen-koerper.csv`;
2025-OS-K4b in `wortlaut-eigen-prozent.csv`.

## Prüfungen

- Ergebnisse: alle Katalogwerte (ergebnis, kurzloesung) mit den Zahlen
  des neuen Wortlauts nachgerechnet; alle stimmen (z. B. JR ≈ 3165 m,
  Weg ≈ 5665 m; BD = 4,1 · sin 123° : sin 36° ≈ 5,85 cm; BD ≈ 502 m;
  AC ≈ 112,8 m; BC ≈ 1805,5 m; DP ≈ 3,2 m; BC ≈ 422,8 m; y ≈ 180,1 cm;
  Turm ≈ 32,2 m; AC ≈ 78,1 cm). Keine Abweichung zur Katalog-Lösung.
- Allein lösbar: Teilaufgaben, die ein Ergebnis eines früheren Teils
  brauchen, nennen es als „Gegeben: …“ (2016-OS-K7c, 2018-OS-K4b–d,
  2022-OS-K5c, 2026-FOR-K4c); 2017-OS-K4c rechnet BC selbst.
- Wortgleiche Folgen (Prosa ohne Zahlen/Formeln): höchstens 8 Wörter.
  Längere Folgen nur in Formel-Auswahlen (2017-OS-B1d, 2018-OS-B1g,
  2021-OS-B1h, 2024-OS-B1f, 2026-FOR-B1j) – innermathematisch.
- CSV parst mit `csv` (Trenner ;), 8 Felder je Zeile.

## Befund

- 2015-OS-K5c: Katalogfeld zwischenergebnis schreibt
  „BD : sin 123° = 4,1 : sin 21°“; richtig ist sin 36° (AD liegt dem
  Winkel bei B gegenüber). Mit sin 21° käme 9,6 cm heraus; das
  Katalogergebnis 5,85 cm stimmt.

## Abbildungen

Neue Typen (das Bauprogramm muss sie frei zeichnen oder als Text
setzen): „Dreieck: …“ (allgemeines Dreieck mit Ecken, Seiten,
Winkeln), „Viereck (<Art>): …“ (Trapez, Parallelogramm, Drachen,
Quadrat), „Lageskizze: …“ (Sachskizze mit Punkten, Strecken,
Winkeln), „Schrägbild: …“ (Körper), „Koordinatensystem: x a..b;
y c..d; Gitter …; Punkte …“ (wie „Graph“, aber nur Punkte/Strecken).
„… aus dem Vorspann“ verweist auf die Abbildung der Vorspann-Zeile.

## Entscheidungen

- 2019-OS-K2d: Geraden f, g, h des Koordinatensystems weggelassen,
  nur A, B, C gezeichnet (für 2d genügt das).
- Namen geändert (Tim → Lea bei 2018-OS-K4), Orte und Gegenstände
  nicht.
- Symmetrie- und Eigenschafts-Ankreuzaufgaben (2016-OS-B1e,
  2021-OS-B1j, 2022-OS-B1i, 2026-FOR-B1c) als Frage bzw. Aussagen
  umformuliert; Inhalt der Optionen festgelegt.
- 2023-OS-K2a ohne Vorspann (Trapez im Text), weil der Vorspann
  2023-OS-K2 in `wortlaut-eigen-flaechen.csv` steht.
