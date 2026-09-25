# Auftrag: Umzug 2026-09-25 (zweiter)

## Ausgangslage

Der Chat verbessereBlaetter() vom 25./26.09.2026 ist beendet;
die neue Übergabe liegt als Datei 2 bei. Der Testlauf
„auftrag-testlauf" ist durchgelaufen (Commits 93a5d70 bis
3bda4d4) und gepusht; `git status` muss sauber sein, sonst
diesen Auftrag nicht starten.

## Schritte

1. Die bisherige `uebergabe.md` (Kopf „Übergabe
   verbessereBlaetter – 2026-09-26") nach
   `archiv/uebergabe-2026-09-26.md` verschieben. Liegt dort schon
   eine Datei dieses Namens, die neue mit Suffix `-b` benennen.
2. Die neue `uebergabe.md` (Datei 2) in die Wurzel legen.
3. `faellig.md` § 2, je ein Posten (was · Auslöser · bei wem ·
   Fundstelle):
   - FHR-Wort an den acht Sek-I-Einheiten mit Sek-II-Zeilen
     (daten 1 und 4 u. a.) in die Marken-Zeile aufnehmen ·
     nächster Mechanik-Auftrag · Claude Code · bericht-marken.md
     Punkt 15.
   - `blattbau`: `.gitattributes` mit `* text=auto eol=lf`
     anlegen · nächster Auftrag in blattbau · Claude Code ·
     Bericht v4.3-Einspielung.
   - `werkzeuge/klassen-ermessen.py`: Zitat je Fall aus der
     eigenen Reihe statt aus der ersten · nächster Neubau ·
     Claude Code · katalog/_marken-entscheidungen.md Nebenbefund.
   - Testlauf: Blätter nacheinander statt gleichzeitig bauen
     (Sub-Agenten teilen sich den Ordner), Uhrzeiten nur aus
     `Get-Date`, Regelweg `claude -p` (jetzt angemeldet) ·
     nächster Testlauf · Chat (Auftrag ändern) · uebergabe.md § 5.
4. `README.md`: unter „Wo fange ich an" die Zeile zu
   `uebergabe.md` unverändert lassen; im Archiv-Absatz nichts
   ändern (das Archiv wird nicht einzeln gelistet).
5. Diesen Auftrag nach `archiv/auftrag-umzug-2026-09-25b.md`
   verschieben (nicht löschen). Commit mit Nachricht aus
   UTF-8-Datei über `commit -F`: „umzug: Übergabe 25.09. abends,
   vier Posten faellig".

## Bericht (im Chat)

Erste Zeile das Modell; dann: Archivname der alten Übergabe,
Zeilenzahl der neuen, die vier Posten wortgleich, Commit-Hash;
letzte Zeile „Push origin drücken".

## Regeln

- PowerShell 5.1: kein Heredoc, kein sed; Dateien schreiben mit
  `[System.IO.File]::WriteAllText(pfad, text, (New-Object
  System.Text.UTF8Encoding($false)))`; BOM und CR prüfen.
- git über die git.exe von GitHub Desktop mit `-c
  core.pager=cat`; Commit-Nachricht über `commit -F`.
- Nichts löschen; verschieben nach `archiv/`.
