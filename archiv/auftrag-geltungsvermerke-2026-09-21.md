# Auftrag: Geltungsvermerke der beiden Vorratsthemen schließen

## Ausgangslage

`befund-geltung-2026-09-21.md` beantwortet die Frage, die in
`matrizen-und-uebergangsprozesse.md` und `konfidenzintervalle.md`
an sechs Stellen als offen vermerkt ist: Beide Themen sind in
Berlin und Brandenburg nicht prüfungsrelevant, und für 2030 ist
inhaltlich nichts angekündigt. Die Vermerke sagen noch, eine
gebündelte Recherche stehe aus. Dieser Auftrag ersetzt sie durch
das Ergebnis.

Die Zeilen in den vier `abitur/abi-*-geltung.md` führen beide
Themen bereits mit „nein" und bleiben unverändert.

`ersetzungen-geltung.txt` enthält die sechs Ersetzungen. Die
Blockform ist dieselbe wie zuletzt: `DATEI`, `ZEILE`, `ALT`, `NEU`,
getrennt durch `----`; der Text läuft jeweils bis zum Zeilenende und
kann Klammern, Anführungszeichen und senkrechte Striche enthalten.
`ALT` ist hier nicht die ganze Zeile, sondern ein Ausschnitt daraus.

## Schritte

1. `ersetzungen-geltung.txt` einlesen.
2. Je Block: In `katalog/<DATEI>` in Zeile `<ZEILE>` den Text `ALT`
   durch `NEU` ersetzen. Zwei Bedingungen, beide müssen gelten –
   sonst nichts ändern, Block überspringen und melden:
   – die Zeilennummer existiert,
   – `ALT` kommt in dieser Zeile genau einmal vor.
3. `werkzeuge/tragfaehigkeit.py`, `werkzeuge/verweis-pruef.py` und
   `werkzeuge/blatt0-belege.py` laufen lassen; die drei abgeleiteten
   Dateien werden mit committet, falls sie sich ändern.
4. In `faellig.md` § 2 den Rest des Geltungspostens streichen
   (Vermerke nachtragen) und in § 4 vermerken, dass er mit diesem
   Lauf erledigt ist.
5. `katalog/index.md` Zeile 232 auf den heutigen Stand bringen: Sie
   nennt noch die Gegenprobe 147/112/35 und Kennzahl 9 = 93. Richtig
   sind 147/131/16 und Kennzahl 9 = 24 von 463. Findest du dort eine
   andere Zahl als beschrieben, melde es und lass die Zeile stehen.
6. Auftrag und Ersetzungsliste nach `archiv/` verschieben
   (`archiv/auftrag-geltungsvermerke-2026-09-21.md`,
   `archiv/ersetzungen-geltung-2026-09-21.txt`).
7. Committen mit der Nachricht
   „Geltung: Vermerke der beiden Vorratsthemen geschlossen".

## Prüfungen

- 6 Ersetzungen ausgeführt, keine übersprungen.
- Nach dem Lauf findet eine Suche nach „ungeklärt" und
  „gebündelte" in beiden Einträgen keinen Treffer mehr.
- `git diff --stat` nennt `katalog/matrizen-und-uebergangsprozesse.md`,
  `katalog/konfidenzintervalle.md`, `katalog/index.md` und
  `faellig.md`, dazu die abgeleiteten Dateien, soweit sie sich
  ändern. Kein anderer Katalogeintrag, keine Zeile in `themen.csv`,
  keine der vier `abi-*-geltung.md`.
- Kennzahl 7 bleibt 0 von 73, Kennzahl 8 Gruppe (c) bleibt 16,
  Kennzahl 9 bleibt 24 von 463, Prüfung 2 bleibt bei 516 direkt
  zugeordneten Angaben. Ändert sich eine dieser Zahlen, hat eine
  Ersetzung mehr getroffen als gewollt – melden, nicht anpassen.
- `python katalog/_pruef_struktur.py` und
  `python werkzeuge/themen-pruef.py` laufen durch.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann Zahl der
ausgeführten und übersprungenen Ersetzungen, das Ergebnis der
Suche nach „ungeklärt" und „gebündelte", `git diff --stat`, die
vier Kennzahlen, der neue Wortlaut von `index.md` Zeile 232.
Abweichungen und Annahmen. Letzte Zeile: „Push origin drücken".

## Regeln

Nur die sechs genannten Stellen und `index.md` Zeile 232 anfassen.
Keinen weiteren Satz umformulieren, keine Quellenklammer anfassen,
keine Zeile hinzufügen oder löschen. An
`befund-geltung-2026-09-21.md` nichts ändern. Passt eine Ersetzung
nicht, melden statt anpassen.
