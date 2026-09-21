# Auftrag: Dateiverweise nachtragen, zweiter Satz

## Ausgangslage

Der Lauf vom 21.09. („Blatt 0: Dateiverweise nachgetragen",
cfa4723) hat 112 Zeilen in 21 Einträgen erfasst – nämlich die, deren
Blatt-0-Abschnitt gar keinen Dateiverweis trug. Acht weitere
Einträge nennen ihre Themen teils als Verweis, teils in Wortform;
sie fielen deshalb durch die Messung. `_tragfaehigkeit.md` führt sie
nach dem Werkzeugpflege-Lauf unter „Einträge mit Dateiverweisen, die
daneben Themen in Wortform nennen": daten 5, einheiten 9,
kurvenuntersuchung 1, lineare-gleichungssysteme 7, potenzen-wurzeln
5, reelle-zahlen 6, trigonometrische-funktionen 10, zinsrechnung 8.

`ersetzungen-blatt0-2b.txt` enthält diese 50 Zeilen als fertige
Ersetzungen. Die Zuordnung Titel → Datei ist entschieden; du
ersetzt, du übersetzt nicht.

Voraussetzung: `werkzeuge/verweis-pruef.py` und
`werkzeuge/tragfaehigkeit.py` stehen auf v0.2 (Commit 9722afb).
Stehen sie auf v0.1, brich ab und melde es.

## Schritte

1. `ersetzungen-blatt0-2b.txt` einlesen. Vier Felder je Zeile,
   getrennt durch `|`: Dateiname, Zeilennummer, alter Text, neuer
   Text. Die Einträge liegen in `katalog/`.
2. Je Zeile: In `katalog/<Dateiname>` die angegebene Zeilennummer
   aufsuchen und dort den alten Text durch den neuen ersetzen.
   Drei Bedingungen, alle müssen gelten – sonst nichts ändern,
   Zeile überspringen und melden:
   – die Zeilennummer existiert,
   – der alte Text kommt in dieser Zeile genau einmal vor,
   – die Zeile liegt im Abschnitt „### Voraussetzungen (Blatt 0)"
     vor der Zwischenzeile „Erkennungsschritte…".
3. `werkzeuge/tragfaehigkeit.py`, `werkzeuge/verweis-pruef.py` und
   `werkzeuge/blatt0-belege.py` laufen lassen; die drei
   abgeleiteten Dateien werden mit committet.
4. In `faellig.md` § 2 den Posten zu den 54 Wortform-Zeilen der
   sieben Sek-I-Einträge streichen und mit dem heutigen Datum in
   § 4 eintragen; dabei vermerken, dass 50 Zeilen in acht Einträgen
   ersetzt wurden (kurvenuntersuchung war im Posten nicht genannt,
   gehört aber zur selben Form).
5. Auftrag und Ersetzungsliste nach `archiv/` verschieben
   (`archiv/auftrag-blatt0-verweise-2b-2026-09-21.md`,
   `archiv/ersetzungen-blatt0-2b-2026-09-21.txt`).
6. Committen mit der Nachricht
   „Blatt 0: Dateiverweise in acht weiteren Einträgen nachgetragen".

## Prüfungen

- 50 Ersetzungen ausgeführt, keine übersprungen. Jede übersprungene
  Zeile ist ein Abbruchgrund für Schritt 3: erst melden.
- `git diff --stat` nennt genau acht Dateien unter `katalog/` plus
  die drei abgeleiteten und `faellig.md`.
- `git diff` zeigt in jeder geänderten Zeile ausschließlich
  eingefügte Klammern der Form ` (name.md)`. Zwei Ausnahmen, beide
  so gewollt: `kurvenuntersuchung.md` Zeile 31 erhält
  ` (lineare-funktionen.md, Sek I, Einheit 3)`, `potenzen-wurzeln.md`
  Zeile 28 erhält ` (bruchrechnung.md, LS-AA Kl. 6 V 4)` – in beiden
  Fällen steht der Dateiname in einer vorhandenen Klammer vorn.
- Kennzahl 9 fällt von 93 auf 43. Kennzahl 7 bleibt 1 von 73.
  Kennzahl 8 Gruppe (c) bleibt 16.
- „Einträge mit Dateiverweisen, die daneben Themen in Wortform
  nennen" fällt in den Messlücken von `_tragfaehigkeit.md` von 8
  auf 0.
- Die Zahl der direkt zugeordneten Einheitenangaben in Prüfung 2
  steigt von 441; um wie viel, ist offen. Jede Einheitsnummer, die
  größer ist als die Zieldatei Einheiten hat, wird berichtet und
  nicht berichtigt. Bekannt und unverändert ist der eine Grenzfall
  in `lineare-gleichungssysteme.md` Zeile 117.
- `python katalog/_pruef_struktur.py` und
  `python werkzeuge/themen-pruef.py` laufen durch.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann Zahl der
ausgeführten und übersprungenen Ersetzungen, `git diff --stat`, das
Ergebnis der Prüfungen, die neuen Werte von Kennzahl 9 und Prüfung 2
sowie – falls Prüfung 2 jetzt zu große Einheitsnummern findet –
diese Fälle vollständig mit Eintrag, Zeile, Ziel und Nummer.
Abweichungen und Annahmen. Letzte Zeile: „Push origin drücken".

## Regeln

Nur die 50 genannten Stellen anfassen. Keinen Satz umformulieren,
keine Einheitsnummer ändern, keine Quellenklammer anfassen, keine
Zeile hinzufügen oder löschen. Passt eine Ersetzung nicht, melden
statt anpassen.

Modell: Sonnet (reine Mechanik, alle Lesarten sind entschieden).
