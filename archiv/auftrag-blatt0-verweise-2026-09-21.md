# Auftrag: Dateiverweise in den Blatt-0-Abschnitten nachtragen

## Ausgangslage

`katalog/_verweise.md` § 5 zeigt: 22 Einträge nennen ihre Blatt-0-
Voraussetzungen nur in Wortform („Thema Lineare Gleichungen,
Einheit 4."), ohne Dateiverweis. Ein Prompt kann Blatt 0 dort nicht
auflösen. `ersetzungen-blatt0.txt` enthält 112 fertige Ersetzungen:
Der Titel bleibt stehen, der Dateiname kommt in Klammern dazu.

Die Zuordnung Titel → Datei ist entschieden und steht in der
Datei. Du übersetzt nicht und entscheidest nicht, du ersetzt.

## Schritte

1. `ersetzungen-blatt0.txt` einlesen. Vier Felder je Zeile, getrennt
   durch `|`: Dateiname, Zeilennummer, alter Text, neuer Text. Die
   Datei liegt in der Wurzel, die Einträge in `katalog/`.
2. Je Zeile: In `katalog/<Dateiname>` die angegebene Zeilennummer
   aufsuchen und dort den alten Text durch den neuen ersetzen.
   Bedingungen, alle drei müssen gelten – sonst nichts ändern, Zeile
   überspringen und melden:
   – die Zeilennummer existiert,
   – der alte Text kommt in dieser Zeile genau einmal vor,
   – die Zeile liegt im Abschnitt „### Voraussetzungen (Blatt 0)".
3. `python werkzeuge/tragfaehigkeit.py` und
   `python werkzeuge/verweis-pruef.py` neu laufen lassen;
   `katalog/_tragfaehigkeit.md` und `katalog/_verweise.md` sind
   abgeleitet und werden mit committet.
4. Diesen Auftrag und `ersetzungen-blatt0.txt` nach `archiv/`
   verschieben (`archiv/auftrag-blatt0-verweise-2026-09-21.md`,
   `archiv/ersetzungen-blatt0-2026-09-21.txt`).
5. Committen mit der Nachricht
   „Blatt 0: Dateiverweise in 21 Sek-I-Einträgen nachgetragen".

## Prüfungen

- 112 Ersetzungen ausgeführt, keine übersprungen. Jede
  übersprungene Zeile ist ein Abbruchgrund für Schritt 3: erst
  melden, dann entscheidet der Lehrer.
- `git diff --stat` nennt genau 21 Dateien unter `katalog/` plus
  die zwei abgeleiteten. `terme.md` ist nicht dabei – der Eintrag
  hat keine Nennung und bleibt unverändert.
- `git diff` zeigt in jeder geänderten Zeile ausschließlich
  eingefügte Klammern der Form ` (name.md)` bzw. bei
  `quadratische-funktionen.md` Zeile 26 und `pythagoras.md`
  Zeile 28 ` (lineare-funktionen.md, Blatt 0)`. Einzige Ausnahme:
  `prozentrechnung.md` Zeile 27, dort wird „Thema Brüche." durch
  zwei benannte Themen ersetzt – so gewollt.
- Nach dem Lauf steht in `_verweise.md` § 5 nur noch `terme.md`
  (1 von 73 statt 22 von 73), und in den Messlücken von
  `_tragfaehigkeit.md` ebenso.
- `_verweise.md` Prüfung 1 Gruppe (c) bleibt bei 16 Verweisen auf
  fehlende Dateien; Prüfung 2 bleibt bei 0 zu großen
  Einheitsnummern. Steigt eine der beiden Zahlen, ist eine
  Ersetzung falsch gelandet.
- `python katalog/_pruef_struktur.py` und
  `python werkzeuge/themen-pruef.py` laufen durch.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann: Zahl der
ausgeführten und der übersprungenen Ersetzungen, `git diff --stat`,
das Ergebnis der sechs Prüfungen. Dazu die Nachfragezahlen aus
`_tragfaehigkeit.md` Tabelle A vor und nach dem Lauf für die zehn
Themen an der Spitze – die Zahlen steigen, und um wie viel, ist der
eigentliche Ertrag. Letzte Zeile: „Push origin drücken".

## Regeln

Nur die 112 genannten Stellen anfassen. Keinen Satz umformulieren,
keine Einheitsnummer ändern, keine Quellenklammer anfassen, keine
Zeile hinzufügen oder löschen. Passt eine Ersetzung nicht, melden
statt anpassen.

Modell: Sonnet (reine Mechanik, alle Lesarten sind entschieden).
