# Auftrag Umzug 2026-09-26

Modell: Sonnet (reine Mechanik). Voraussetzung: der Auftrag Nacht
2026-09-28 ist beendet (archiv/auftrag-nacht-2026-09-28.md liegt
vor, nacht-stand-2026-09-28.md nicht mehr in der Wurzel). Ist er
noch nicht beendet, brich ab und melde es.

Regeln: PowerShell; Dateien schreiben mit
[System.IO.File]::WriteAllText(pfad, text,
(New-Object System.Text.UTF8Encoding($false))), nach dem Schreiben
prüfen (keine BOM, kein CR); git über die git.exe von GitHub
Desktop mit -c core.pager=cat, Commit-Nachricht über commit -F aus
einer UTF-8-Datei; nichts löschen, verschieben mit git mv; kein
Push.

1. Vor dem Anlegen dieser Dateien lag die alte uebergabe.md
   (Kopfzeile „2026-09-25 (abends …)") in der Wurzel; sie ist
   jetzt überschrieben. Hol sie aus git (git show HEAD:uebergabe.md)
   und leg sie als archiv/uebergabe-2026-09-25-abends.md ab (bei
   Namensgleichheit „b" anhängen).
2. faellig.md § 2, neue Posten (je Zeile: was · Auslöser · bei
   wem · Fundstelle):
   - blattbau, Vorlage Stufe 7: \einheitenkopf allein am
     Seitenende (Lösung wie \verfahren); Achsenstriche im ksys
     gegen den Zahlenstrahl-Befund prüfen; Probeblatt ist voll
     (12 von 12 Seiten) – Grenze anheben oder kürzen · nächster
     Vorlagen-Auftrag · Claude (Auftrag), Lehrer (blattbau) ·
     blattbau/bericht-vorlage-stufe6-2026-09-28.md
   - Blatt-Chat je Prompt-Version nach dem Testlauf:
     „quadratische gleichungen 9 oberschule" im Projekt
     erzeugeUnterrichtsblatt() (Opus); Protokoll-Archiv über
     einsortieren.py · Testlauf mit v4.4 liegt vor · Lehrer (Chat),
     Chat (Auswertung) · uebergabe.md § 6
   - Live-Fassung des Prompts nachziehen, sobald v4.4 im Repo
     liegt (Projektanweisung erzeugeUnterrichtsblatt()) · Commit
     v4.4 in blattbau · Lehrer · uebergabe.md § 6
3. README.md: Zeile zu uebergabe.md prüfen (Stand 2026-09-26),
   archivierte Übergabe im archiv-Block nennen.
4. Commit „umzug: Übergabe 2026-09-26, drei Posten faellig".

Bericht im Chat: Modell, Commit, Name der archivierten Datei,
letzte Zeile „Push origin drücken".
