# Auftrag: Umzug 2026-09-22b

Modell: Sonnet (Mechanik).

## Schritte

1. Die alte uebergabe.md liegt jetzt in
   archiv/uebergabe-2026-09-22a.md, die neue (Datei 1) in der
   Wurzel. Prüfe beides; die neue beginnt mit
   „# Übergabe 2026-09-22b".
2. werkzeuge/einsortieren.py: Die Spalte „Vorlage" im Index nimmt
   bisher die letzte Zeile des Protokolls, die mit „Vorlage:"
   beginnt („Vorlage: fehlende Bausteine …"); sie soll die erste
   nehmen (die Versionszeile). Ändern, Werkzeug laufen lassen
   (py -3 oder voller Python-Pfad), blaetter/index.md wird neu
   geschrieben; die Indexzeile zeigt in „Vorlage" jetzt die
   Version der .sty. Zeile im Bericht.
3. Verschiebe auftrag-umzug.md nach archiv/.
4. Commit „Umzug 2026-09-22b; Index: Vorlage-Spalte".

## Bericht

Erste Zeile: das Modell. Dann: Kopfzeile der neuen Übergabe,
Pfad der alten, die neue Indexzeile, Commit-Kennung,
Abweichungen. Letzte Zeile: „Push origin drücken".

## Regeln

Keine Rückfragen. Nichts löschen. Außer den genannten Dateien
nichts ändern. UTF-8, LF. git über die git.exe von GitHub
Desktop.
