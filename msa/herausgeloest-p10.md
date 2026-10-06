# Herausgelöste Aufgaben P10

Stand 2026-10-06 (Auftrag K Schritt 3). Datei: `msa/herausgeloest-p10.csv`
(id;marke;quelle;kapitel;stufe;handgriffe;art;eltern_id;wortlaut;
abbildung;loesung;schritte;zahlart;fragerichtung;darstellung;woerter;
bemerkung). Regel: Beschluss N1.4 (`aufgabenbank/bau/pruefheft/
beschluesse-2026-10-06b.md`), Muster `beispiel-zwischenschritt.html`.

## Inhalt

- 140 Aufgaben, je eine für einen Zwischenschritt aus
  `msa/handgriffe-p10.csv` (157 Zwischenschritte ohne EBR- und
  GYM-Zwillinge; 17 ohne herausgelöste Aufgabe, Liste unten). 87 aus
  OS/FOR, 53 aus GYM.
- id `<eltern-id>-h1`, `-h2` …; `marke` „nach P10 ’15“ (auch bei GYM, die
  Marke nennt nur das Jahr, N4.17); `quelle` wie in den
  Wortlaut-Dateien („P10 2015 · 2b“, „P10 2026 FOR · 3c“, „P10 2017 GYM ·
  4c“); `art` immer `herausgeloest`.
- `kapitel`/`stufe` wie in `msa/zuordnung-*.csv`; `handgriffe` die Stufe
  (`kapitel:stufe`), bei Pythagoras im Körper auch „Kathete oder
  Hypotenuse direkt“.
- `wortlaut` eigener Wortlaut, Du-Form, echte Sache und echte Zahlen der
  Elternaufgabe; das Nebensächliche (Ablesen, andere Teilaufgaben,
  Sachrahmen ohne Zahl) fällt weg. Wo ein Wert in der Elternaufgabe erst
  berechnet wird, steht er als gegeben da (z. B. 43,50 € in 2015-OS-K2b).
- `loesung` exakt zuerst, dann gerundet (Beschluss 24); Bezeichnungen
  nach N4.18 (Punkte mit Buchstaben, x₁, x₂, Variablen nach der Sache).
- `schritte`, `zahlart` (ganz, dezimal, bruch, krumm),
  `fragerichtung` (vorwärts, rückwärts, vergleichen, Aussage prüfen),
  `darstellung` (Text, Tabelle, Bild, Diagramm), `woerter` (Wörter des
  Wortlauts) für die Sortierung der Leiter (Beschlüsse 2, 3, N1.3).
- Jede Lösung ist mit sympy nachgerechnet (0 Abweichungen).

## Nicht herausgelöst (17)

Skizze, die schon die ganze Teilaufgabe ist (2014-GYM-K2c, 2016-GYM-K2d,
2017-GYM-K2a, 2019-GYM-K2a, 2025-GYM-K3e); Daten nur im Bild oder
unvollständig (2014-GYM-K5a, 2015-GYM-K5d, 2020-GYM-K5b, 2020-GYM-K6c,
2024-GYM-K6a); Sinussatz nach einem Winkel umgestellt, passt nicht auf
„Seite berechnen (Sinussatz)“ (2015-GYM-K5b, 2025-GYM-K4b); Formel
außerhalb P10 (2016-GYM-K5b gleichseitiges Dreieck aus Umfang,
2022-GYM-K4d Kugel mit unbekanntem r); echte Aufgabe gleicher Art
vorhanden (2016-GYM-K2c Gerade zeichnen); Handgriff schon Hauptplatz
(2021-GYM-K6a); Scheitel dort berechnet statt abgelesen (2021-GYM-K6b).

## Offen

- Bauskript und Prüfrechnung liegen nicht im Repo (Schreibbereich des
  Auftrags); die CSV ist die Quelle, Änderungen von Hand.
