# Übergabe verbessereBlaetter – 2026-10-03 (Chat 02./03.10.)

Vorherige Übergabe: archiv/uebergabe-2026-10-01c.md.

## 1 Ziel

Schnell gute Blätter für die Stunde. Schwerpunkt jetzt:
Prüfungsblätter P10 2027, zuerst Aufgabe 1 (Basis) – ein Zettel
je Unterrichtstermin, aus dem Skript, nicht im Chat erzeugt.
Abitur später (2027 schreibt nur ein Schüler sicher Mathe).

## 2 Arbeitsgrundlage

- aufgabenbank: Basisvorrat `bank/_basis/` (64 Typen, 640
  Aufgaben; typen.py, vorrat.py, stand.md); Skript
  `werkzeuge/zusammenbau.py` v1.4 (Rezept Zettel v0.7, Serie
  BAS-S, hoehen.csv, Schalter ist_original); maßgebliche
  Zettelform: `bau/zettel/vorlage-2026-10-03/vorlage.tex` (+pdf;
  Basis 1, 2, 3-schwach); bank.md siebte Fassung;
  `eingang/gebaut.csv` (Blätter je Schülernummer).
- mathe-nachhilfe: 16 Einträge nach Duden-Abgleich und
  Leiterregeln umgesetzt (`katalog/_abgleich-duden9-kap1..10.md`,
  `katalog/_gewicht/`); konzept.md Entscheidungen 38–40;
  `msa/handreichung-p10-2027.tex/.pdf`; faellig.md.
- blattbau: `bankblatt.md` v5.4 = Projektanweisung in
  erzeugeBlatt(Bank) (ersetzt 03.10.).
- Privat, nie im Repo: `Schuelerliste-privat.md` (18 Schüler,
  Nummern S01–S18) als Projektdatei in erzeugeBlatt(Bank); der
  Duden-PDF; Wortlaut der Prüfungsoriginale.

## 3 Arbeitsstand

Erledigt 02./03.10.: Duden WÜT 9 Kap. 1–10 gegen den Katalog,
Umsetzung in 16 Einträgen samt Bank (Opus-Agenten); Leiterregeln
(Rückwärts- und Mischsprosse je Kette, krumme Zahlen sparsam);
Gewicht Kern/Rand mit Halbsatz; Basisvorrat 640; Zettelvorlage
nach vielen Runden vom Lehrer gutgeheißen (ein Blatt, keine zwei
Spalten, Kopf nur „Basis n“, Streifen rechts, Buchstabe vor dem
Kästchen, U groß, Jahreszahl links vor der Nummer, leichter
Einstieg, Hilfsmittel nicht auf dem Zettel); Handreichung eine
Seite mit QR-Code zu den alten Prüfungen; Schülerliste mit
Nummern; v5.4 (Name → Nummer, gebaut.csv automatisch).
Messwerte: Woche 80 %, Fable 80 % (02.10.); Reset Montag 18:00.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter, soweit hier nichts anderes steht.

- P10 2027: EBR (Grundkurs) und FOR (Erweiterungskurs), beide
  135 min; Aufgabe 1 Basis in beiden gleich, mit Taschenrechner
  und Formelsammlung; ab 2028 hilfsmittelfreier Teil.
- Zettel: jeder steht für sich, keine Rückmeldung des Lehrers,
  keine Serie mit Fortschritt; Nummer nur gegen Wiederholung;
  mindestens drei Originale je Zettel (verfremdet, Jahr links);
  Vorstufen immer; „schwach“ = 7 Aufgaben Kerntypen. Abgelegt
  wird erst, was der Lehrer gutheißt.
- Schülerdaten: im Repo nur Nummern; Namen nur in der privaten
  Projektdatei. Kein Ergebnisblatt zu alten Prüfungen.
- Kernentscheidungen kommen nach einer Weile zur Wiedervorlage
  (konzept.md § 4); Fünf-Minuten-Test am 16.10.
- Modellwahl: Opus im Chat und für Agenten; Großes erst nach dem
  Reset Montag 18:00.

## 5 Offene Punkte und Verworfenes

- Ablage der unveränderten Originale (Wortlaut): privates Repo?
  Mit dem Lehrer klären (faellig.md).
- Kern-Schärfung offen: Kern = in mind. 30 % der Jahre seit 2020;
  sortiert, filtert nicht; bei „schwach“ nur Kern.
- Themenhefte P10: zehn Hefte nach Punkteanteil (Lineare
  Funktionen, Quadratische Funktionen, Mittelwert/Median/
  Spannweite, Wahrscheinlichkeit, Flächen, Volumen, Pythagoras,
  Trigonometrie, Wachstum, Prozent) – Liste nicht bestätigt.
- Offen in der Schülerliste: Mathekurs S02, S03, S04; Klasse S03;
  Bildungsgang S17; Abschluss S18.
- bankblatt v5.5: Bank vor Erfinden, krumme Zahlen sparsam, Kern
  zuerst, Basiszettel auf Zuruf, EBR/FOR-Filter.
- Aus 01.10. weiter offen: schwach-Länge (23 Seiten), Lage der
  Prüfungssprosse, Eingang terme-01c ohne Übernahme, Abgleich der
  übrigen Einträge gegen weitere Bände.
- Verworfen: Ergebnisblatt alter Prüfungen; Zeilen zum Abtippen
  für den Lehrer; zweispaltige Zettel; Lösungswort; Serie mit
  Rückmeldung.

## 6 Nächster Arbeitsschritt

Schritt 1: Basiszettel ins Skript nach der Vorlage vom 03.10.
(zusammenbau.py → v1.5, Rezept Zettel v0.8) und Vorrat ergänzen:
Vorstufen-Varianten für die Kerntypen, Tipps, Stufe der
Verfremdung je Original, Prüfungsverb vorn, Ankreuzen A–D, U
statt u; Regeln: leichter Einstieg, verschiedene Themen, mind.
drei Originale, schwach = 7 Aufgaben Kerntypen. Opus-Agent nach
Montag 18:00; vorher Größe nennen. Ergebnis: zwei Probezettel
dem Lehrer zeigen, nicht ablegen.
