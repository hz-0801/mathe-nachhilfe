# Auftrag: Umzug 2026-09-26

## Ausgangslage

Der Chat verbessereBlaetter zieht um. Die neue Übergabe liegt als
uebergabe.md neben diesem Auftrag; die alte (Stand 24.09.2026)
liegt noch als uebergabe.md im Repo, bis Schritt 1 sie sichert.

## Schritte

1. git mv uebergabe.md archiv/uebergabe-2026-09-24.md (liegt dort
   schon eine Datei dieses Namens, hänge „b" an). Erst danach die
   neue uebergabe.md aus diesem Block anlegen.
2. Prüfe die neue uebergabe.md: erste Zeile „# Übergabe
   verbessereBlaetter – 2026-09-26 (nach zwei Nächten)",
   Abschnitte „## 1 Ziel" bis „## 6 Nächster Arbeitsschritt",
   keine Zeile länger als 72 Zeichen.
3. ziel.md, Abschnitt „## 5 Offen", zweiter Punkt: ersetze
   „Sprossen ohne Prüfungsoriginal (22 Prüfungshöhen im Sek-I-
   Katalog)" durch „Sprossen ohne Prüfungsoriginal (22 Sprossen
   im Sek-I-Katalog, 15 davon Prüfungshöhen)"; Umbruch bei 72
   Zeichen anpassen. Sonst nichts an ziel.md.
4. faellig.md, Abschnitt 2, neue Posten je eine Zeile nach dem
   Muster „was · Auslöser oder Termin · bei wem · Fundstelle":
   - Fotos der Inhaltsverzeichnisse aus den Büchern der Schüler
     und zwei Aufgabenseiten eines Themas im Chat lesen, je Buch
     eine Zeile eintragen · Fotos liegen vor (etwa 10.10.2026) ·
     Lehrer, dann Chat · uebergabe.md § 5.
   - Prüfstein-Befund neben die gekauften Förderhefte legen
     (Sekundo 8 BE/BB, Schnittpunkt 8 diff.) · Heft liegt vor ·
     Chat · befund-schwach-blatt-2026-09-24.md.
   - flaechen.md: Original-ids zu „Term zu Figur angeben" prüfen
     und tauschen · nächster Katalogauftrag · Claude Code ·
     nacht-bericht-2026-09-26.md Teil 2.
   - zuordnungen.md und terme.md um die neueren GYM-Typen
     ergänzen · nächster Katalogauftrag · Claude Code ·
     nacht-bericht-2026-09-26.md Teil 2.
   - themen.csv: Maßstab von zuordnungen nach strahlensaetze ·
     nächster Katalogauftrag · Claude Code ·
     nacht-bericht-2026-09-26.md Teil 2.
   - 2025-GYM-K5d Nebentyp-Etikett prüfen · nächster
     msa-Abgleich · Chat · nacht-bericht-2026-09-26.md Teil 2.
   - Fundamente B Qualifikationsphase in der DNB nachsehen ·
     nächster Sek-II-Quellenlauf · Claude Code ·
     nacht-bericht-2026-09-26.md Teil 3.
   Stand-Zeile von faellig.md um „26.09.2026: sieben Posten aus
   dem Umzug in § 2" ergänzen.
5. git mv auftrag-umzug.md archiv/auftrag-umzug-2026-09-26.md.
6. Commit mit Nachricht aus einer UTF-8-Datei (-F): „umzug:
   Übergabe 2026-09-26, Posten faellig, ziel § 5 Zahl".

## Prüfungen

- git diff HEAD~1 --stat zeigt genau: archiv/uebergabe-2026-09-24.md
  (umbenannt), uebergabe.md (neu), ziel.md (1 Stelle), faellig.md
  (7 Zeilen plus Stand), archiv/auftrag-umzug-2026-09-26.md.
- git status sauber.

## Bericht

Erste Zeile das Modell; dann je Schritt eine Zeile; die beiden
Prüfungen; Abweichungen und eigene Entscheidungen. Letzte Zeile
„Push origin drücken".

## Regeln

- Shell PowerShell: kein Heredoc, kein sed. Dateien schreiben mit
  [System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false))); Zeilenenden
  LF; danach prüfen (keine BOM, kein CR).
- git über die git.exe von GitHub Desktop, mit -c core.pager=cat;
  Commit-Nachricht über -F aus einer UTF-8-Datei. Kein Push.
- Nichts löschen; verschieben nur mit git mv.
