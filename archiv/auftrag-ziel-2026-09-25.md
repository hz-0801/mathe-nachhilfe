# Auftrag: ziel.md auf Stand 25.09.2026

## Ausgangslage

ziel.md in der Wurzel trägt den Stand 22.09.2026. Der Chat
verbessereBlaetter hat am 25.09.2026 eine neue Fassung
beschlossen (Zeitachse statt Filter, Baum je Thema, Zone „kennst
du schon" statt Blatt 0, „schwach" als Form, Zweigzeile und
Ich-kann-Titel). Die neue Fassung liegt als ziel.md schon neben
diesem Auftrag; die alte Fassung ist noch im Git-Verlauf.

## Schritte

1. Alte Fassung sichern: Hole den Stand von ziel.md aus dem
   letzten Commit (git show HEAD:ziel.md) und schreibe ihn nach
   archiv/ziel-2026-09-22.md (UTF-8, LF). Liegt dort schon eine
   Datei dieses Namens, nimm archiv/ziel-2026-09-22b.md.
2. Prüfe die neue ziel.md: erste Zeile „# Ziel – Blätter aus
   Prüfungen und Lehrplan", dritte Zeile beginnt mit „Stand
   25.09.2026", 222 Zeilen, keine Zeile länger als 72 Zeichen,
   Abschnitte „## 1 Ziel" bis „## 5 Offen" vorhanden.
3. Prüfe die gesicherte alte Fassung: erste Zeile gleich, Stand
   22.09.2026, 150 Zeilen.
4. Verschiebe auftrag-ziel.md nach archiv/auftrag-ziel-2026-09-25.md
   (git mv; liegt dort schon eine Datei dieses Namens, hänge „b"
   an).
5. Commit mit der Nachricht „ziel: Stand 2026-09-25 (Zeitachse,
   Baum, Zone kennst du schon)".

## Prüfungen

- Gegenprobe: git diff HEAD~1 -- ziel.md zeigt Änderungen in
  Abschnitt 1 (Bauprinzip), 2 (Zone, Anpassung, Überschriften,
  Kennzeichnung), 3 (Bestellung, Stoff und Höhe) und 5 (Offen);
  Abschnitt 4 unverändert bis auf den Satz zur Heftsorte
  „Vorbereitung". Weicht das ab, ist das ein Befund für den
  Bericht, kein Grund, etwas zu ändern.
- git status nach dem Commit sauber.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann je
Zeile: Ergebnis von Schritt 1 bis 5, Ergebnis der beiden
Prüfungen, Abweichungen und eigene Entscheidungen. Letzte Zeile:
„Push origin drücken".

## Regeln

- Shell ist PowerShell: kein Heredoc, kein sed. Dateien mit
  Set-Content -Encoding UTF8 schreiben; danach prüfen, dass kein
  BOM und keine CRLF entstanden sind (Zeilenenden LF).
- git über die git.exe von GitHub Desktop
  (%LOCALAPPDATA%\GitHubDesktop\app-*\resources\app\git\cmd\git.exe),
  immer mit -c core.pager=cat, Commit mit commit -m.
- Nichts löschen; verschieben nur mit git mv.
- Kein Push.
