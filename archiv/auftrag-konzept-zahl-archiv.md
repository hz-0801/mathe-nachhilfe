# Auftrag: Zahl in konzept.md korrigieren, Projektarchiv ablegen

Zwei Sachen, ein Commit.

## A Korrektur in konzept.md

Zwei Zeilen führen für fhr die Zahl „49 von 135 Typen genau einmal". Nachgezählt aus
`fhr/fhr-katalog.csv` (19.09.2026): 37 Typen sind genau einmal Haupttyp, 49 mehrfach,
49 nie Haupttyp. Die 49 ist die falsche Menge. `fhr.md` § 9 führt die Zahl nicht mehr;
Quelle ist `fhr/fhr-typenbibliothek.md` (Kopfabsatz nach der Kennzahlentabelle).

1. Zeile 83 (Entscheidung 4, Kippt bei), ersetzen:
   `(zu wenige Originale je Typ: fhr 49 von 135 Typen mit genau einem Vorkommen, fhr.md § 9)`
   durch
   `(zu wenige Originale je Typ: fhr 37 von 135 Typen mit genau einem Vorkommen, 49 nie Haupttyp; fhr-typenbibliothek.md)`

2. Zeile 97 (Entscheidung 9, Zahl), ersetzen:
   `Zahl: fhr 49 von 135 Typen genau einmal, 27 zweimal (fhr.md § 9);`
   durch
   `Zahl: fhr 37 von 135 Typen genau einmal, 49 mehrfach, 49 nie Haupttyp (fhr-typenbibliothek.md; korrigiert 19.09.2026, vorher stand hier 49 einmal);`

3. Die 27 (zweimal) nicht neu setzen – sie ist nicht nachgezählt und fällt mit der Umformulierung weg.

4. Änderungslog § 10, neuer Eintrag oben:
   `- 2026-09-19: Entscheidung 4 und 9 – fhr-Zahl korrigiert (37 statt 49 Typen mit genau einem Vorkommen; Zählung aus fhr-katalog.csv, Fund des Projektarchivs Katalog). Verweis fhr.md § 9 durch fhr-typenbibliothek.md ersetzt, weil § 9 die Zahl nicht mehr führt.`

Vorher prüfen: Die zwei alten Textstücke müssen genau einmal in konzept.md vorkommen.
Sonst abbrechen und melden.

## B Archivdatei ablegen

Im Repo-Ordner liegt eine Datei `projekt-*-2026-09-19.md` (zweites Projektarchiv). Nach
`archiv/` verschieben.

## C Abschluss

Diese Auftragsdatei nach `archiv/`. Commit: `konzept.md: fhr-Zahl in Entscheidung 4 und 9
korrigiert; Projektarchiv abgelegt`. Push versuchen. Bericht: Commit-Hash, welche Datei
unter B abgelegt wurde, und „Push origin drücken", falls nötig.
