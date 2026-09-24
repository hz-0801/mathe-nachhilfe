# Auftrag: Übergabe ablegen

Ordner mathe-nachhilfe. Modell Sonnet. Keine Rückfragen.

Regeln: Python nur über %LocalAppData%\Programs\Python\
Python312\python.exe; git über die git.exe von GitHub Desktop;
PowerShell; git mit -c core.pager=cat, commit -m; nicht pushen.
Nichts löschen.

1. Die bisherige uebergabe.md liegt nicht mehr in der Wurzel
   (überschrieben). Ihre letzte committete Fassung wiederherstellen
   und nach archiv/uebergabe-2026-09-23.md legen:
   git show HEAD:uebergabe.md > archiv/uebergabe-2026-09-23.md
   (UTF-8 ohne BOM; in PowerShell mit
   [System.IO.File]::WriteAllText oder python schreiben, nicht
   mit > allein, das erzeugt UTF-16).
2. Prüfen: archiv/uebergabe-2026-09-23.md beginnt mit
   „# Übergabe 2026-09-23"; uebergabe.md in der Wurzel beginnt
   mit „# Übergabe 2026-09-25".
3. README.md: Zeile zu uebergabe.md unverändert lassen; falls
   archiv/ dort mit Beispielen genannt ist, nichts ergänzen.
4. Commit „Umzug 2026-09-25: Übergabe, alte nach archiv/".
5. Diesen Auftrag nach archiv/ verschieben (git mv), Commit
   „archiv: auftrag-umzug 2026-09-25".

Bericht: erste Zeile das Modell; die beiden Kopfzeilen aus
Schritt 2; letzte Zeile „Push origin drücken".
