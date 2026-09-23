# Auftrag umzug – Übergabe ablegen

## Ausgangslage

Ordner mathe-nachhilfe. In der Wurzel liegt die bisherige
uebergabe.md (2026-09-22d) und die neue als uebergabe-neu.md
(2026-09-23).

git über die git.exe von GitHub Desktop:
C:\Users\holge\AppData\Local\GitHubDesktop\app-3.6.5\resources\app\git\cmd\git.exe
Python nur über den vollen Pfad
%LocalAppData%\Programs\Python\Python312\python.exe.
Die Shell ist PowerShell: kein Heredoc, kein sed.

## Schritte

1. git mv uebergabe.md archiv/uebergabe-2026-09-22d.md.
2. Benenne uebergabe-neu.md in uebergabe.md um und nimm sie auf
   (git add).
3. git mv auftrag-umzug.md archiv/auftrag-umzug-2026-09-23.md.
4. Committe alles mit der Nachricht „Umzug 2026-09-23".
   Nicht pushen.

## Prüfungen

- archiv/uebergabe-2026-09-22d.md existiert, die Wurzel enthält
  genau eine uebergabe.md, ihre erste Zeile nennt 2026-09-23,
  eine uebergabe-neu.md gibt es nicht mehr.
- git status zeigt keine weiteren Änderungen.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief.
Dann in drei Zeilen: was verschoben, was angelegt, was
committet wurde, plus Abweichungen.
Letzte Zeile: Push origin drücken.

## Regeln

- Lösche nichts; verschieben statt löschen.
- Ändere keine andere Datei.
- Trifft ein Name im Archiv auf eine vorhandene Datei, hänge
  „b" an und melde es.
- Berichte, was war, auch wenn es scheiterte.
