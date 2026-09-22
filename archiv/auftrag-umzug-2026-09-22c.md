# Auftrag: Umzug 2026-09-22c

## Ausgangslage

Der Werkstattchat verbessereBlätter() zieht um. Die neue Übergabe
liegt als uebergabe.md in diesem Block; die bestehende
uebergabe.md (Übergabe 2026-09-22b) wandert ins Archiv.

## Schritte

1. git mv uebergabe.md archiv/uebergabe-2026-09-22b.md
2. Die uebergabe.md aus diesem Block in die Wurzel legen.
3. Den Auftrag verschieben: auftrag-umzug.md nach
   archiv/auftrag-umzug-2026-09-22c.md (Dateisystem-Verschiebung,
   die Datei ist noch nicht getrackt).
4. Commit mit der Meldung „Umzug 2026-09-22c". Nicht pushen.

## Prüfungen

- archiv/uebergabe-2026-09-22b.md beginnt mit
  „# Übergabe 2026-09-22b".
- uebergabe.md in der Wurzel beginnt mit „# Übergabe 2026-09-22c".
- archiv/auftrag-umzug-2026-09-22c.md liegt vor; in der Wurzel
  liegt kein auftrag-*.md mehr.
- git status nach dem Commit sauber.

## Bericht

Erste Zeile das Modell. Dann Ergebnis jeder Prüfung, Abweichungen
und Annahmen. Letzte Zeile: „Push origin drücken".

## Regeln

- Python wird nicht gebraucht. Falls doch: nur der volle Pfad
  %LocalAppData%\Programs\Python\Python312\python.exe (py -3 gibt
  es in dieser Shell nicht).
- git über die git.exe von GitHub Desktop.
- Nichts löschen; verschieben nur mit git mv oder, bei
  ungetrackten Dateien, per Dateisystem.
