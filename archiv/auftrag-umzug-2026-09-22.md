# Auftrag: Umzug 2026-09-22

Ausgangslage: Die alte Übergabe (2026-09-21b) liegt in HEAD als
uebergabe.md; die neue ist bereits als uebergabe.md in der Wurzel
angelegt und hat sie in der Arbeitskopie überschrieben.

Schritte:
1. Prüfen: uebergabe.md in der Wurzel beginnt mit
   „# Übergabe 2026-09-22".
2. Alte Übergabe aus HEAD sichern:
   git show HEAD:uebergabe.md > archiv/uebergabe-2026-09-21b.md
   (byte-treu, LF; unter PowerShell über cmd /c umleiten). Blob-
   Hash der Archivdatei muss dem HEAD-Blob von uebergabe.md
   entsprechen.
3. auftrag-umzug.md nach archiv/auftrag-umzug-2026-09-22.md
   verschieben.
4. Commit „Umzug 2026-09-22".

Prüfungen: Archivdatei beginnt mit „# Übergabe 2026-09-21b" und
ist byteidentisch mit HEAD:uebergabe.md; git status nach Commit
sauber; genau drei Dateien im Commit (uebergabe.md geändert, zwei
neu in archiv/); python werkzeuge/themen-pruef.py bestanden.

Bericht: erste Zeile das Modell, je Schritt ein Satz,
Prüfergebnisse, Abweichungen. Letzte Zeile: „Push origin drücken".

Regeln: nichts löschen, keine andere Datei anfassen, README nicht
ändern (archiv-Block listet keine Einzeldateien).
