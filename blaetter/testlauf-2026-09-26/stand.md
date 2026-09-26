# Stand Testlauf 2026-09-26

Datum: 2026-09-26 (Start 19:23 Uhr, aus Get-Date)
Prompt-Version: v4.4 – hz-0801/blattbau main 36b7b12, Zeile 1 „# UNTERRICHTSBLATT v4.4 – PROMPT FÜR LERNBLATT UND FOKUS", Kopie `unterrichtsblatt-v4.4.md` (79429 Byte, SHA-256 B215E6E0…F386D, byteidentisch mit ../blattbau/unterrichtsblatt.md)
Bauweise: Ersatzweg – je Eingabe ein Sub-Agent (Typ general-purpose, model opus), Nachricht nach `werkzeuge/testlauf-umgebung.md` (Teil 1 Verweis auf die Promptkopie, Teil 2 Umgebung, Teil 3 Eingabezeile mit Antworten aus der CSV); Blätter nacheinander, nie gleichzeitig. Grund: Der Regelweg ist seit dem 25.09. technisch da – Beigabe `%LocalAppData%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code\2.1.281\claude.exe` (Version 2.1.281), Probeaufruf `claude -p "Antworte mit OK" --model opus` antwortet „OK" (Exitcode 0), `--append-system-prompt[-file]`, `--dangerously-skip-permissions`, `--model`, `--output-format stream-json` bekannt –, aber das Startskript für die Blattsitzungen mit `--dangerously-skip-permissions` hat der Berechtigungsklassifikator der Auftragssitzung abgelehnt („Create Unsafe Agents"); ohne Freigabe des Lehrers kein Umgehungsversuch, also gilt der Regelweg als nicht verfügbar.
Modell: Auftragssitzung Claude Opus 5.5 (claude-opus-5-5); Blattsitzungen Sub-Agent mit model opus
Werkzeuge: xelatex (MiKTeX-XeTeX 4.16, MiKTeX 25.12), pdftotext, pdfinfo, pdftoppm unter %LocalAppData%\Programs\MiKTeX\miktex\bin\x64; Python 3.12.10 unter %LocalAppData%\Programs\Python\Python312 (sympy 1.14.0, pypdf 6.19.0 per pip --target im Scratchpad); curl 8.21.0
Katalog: live von raw.githubusercontent.com (origin/main 68a6401; lokal ein Commit voraus, ohne Änderung an katalog/ und blaetter/index.md)

## Eingaben

1 quadgl-9-os · fertig · Anläufe 1 · Start 19:30 · Ende 20:00 · Aufrufe laut protokoll.txt 78, Umgebung 80
2 quadgl-9-gym · fertig · Anläufe 1 · Start 20:00 · Ende 20:30 · Aufrufe laut protokoll.txt 76, Umgebung 77
3 prozent-7-schwach · fertig · Anläufe 1 · Start 20:30 · Ende 20:57 · Aufrufe laut protokoll.txt 107, Umgebung 109
4 linfkt-8-neu · fertig · Anläufe 1 · Start 20:57 · Ende 21:27 · Aufrufe laut protokoll.txt 119, Umgebung 120
5 kreis-8-ausblick · fertig · Anläufe 1 · Start 21:27 · Ende 21:54 · Aufrufe laut protokoll.txt 95, Umgebung 97 · Sitzung legte zwei leere Dateien in der Repo-Wurzel an (Kreis_KennstDuSchon.tex, zone_a.tex, 21:39:58) – in den Scratchpad verschoben
6 daten-7 · fertig · Anläufe 1 · Start 21:54 · Ende 22:17 · Aufrufe laut protokoll.txt 55, Umgebung 58
7 nullstellen-fokus · fertig · Anläufe 1 · Start 22:17 · Ende 22:29 · Aufrufe laut protokoll.txt 37, Umgebung 39
8 potenz-10 · fertig · Anläufe 1 · Start 22:29 · Ende 22:59 · Aufrufe laut protokoll.txt 87, Umgebung 88
9 kurven-12-be · fertig · Anläufe 1 · Start 22:59 · Ende 23:33 · Aufrufe laut protokoll.txt 80, Umgebung 82
10 ka-terme-8-gym · fertig · Anläufe 1 · Start 23:33 · Ende 00:00 (27.09.) · Aufrufe laut protokoll.txt 80, Umgebung 81
