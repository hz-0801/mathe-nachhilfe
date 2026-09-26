# Stand Testlauf 2026-09-26

Datum: 2026-09-26 (Start 19:23 Uhr, aus Get-Date)
Prompt-Version: v4.4 – hz-0801/blattbau main 36b7b12, Zeile 1 „# UNTERRICHTSBLATT v4.4 – PROMPT FÜR LERNBLATT UND FOKUS", Kopie `unterrichtsblatt-v4.4.md` (79429 Byte, SHA-256 B215E6E0…F386D, byteidentisch mit ../blattbau/unterrichtsblatt.md)
Bauweise: Ersatzweg – je Eingabe ein Sub-Agent (Typ general-purpose, model opus), Nachricht nach `werkzeuge/testlauf-umgebung.md` (Teil 1 Verweis auf die Promptkopie, Teil 2 Umgebung, Teil 3 Eingabezeile mit Antworten aus der CSV); Blätter nacheinander, nie gleichzeitig. Grund: Der Regelweg ist seit dem 25.09. technisch da – Beigabe `%LocalAppData%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code\2.1.281\claude.exe` (Version 2.1.281), Probeaufruf `claude -p "Antworte mit OK" --model opus` antwortet „OK" (Exitcode 0), `--append-system-prompt[-file]`, `--dangerously-skip-permissions`, `--model`, `--output-format stream-json` bekannt –, aber das Startskript für die Blattsitzungen mit `--dangerously-skip-permissions` hat der Berechtigungsklassifikator der Auftragssitzung abgelehnt („Create Unsafe Agents"); ohne Freigabe des Lehrers kein Umgehungsversuch, also gilt der Regelweg als nicht verfügbar.
Modell: Auftragssitzung Claude Opus 5.5 (claude-opus-5-5); Blattsitzungen Sub-Agent mit model opus
Werkzeuge: xelatex (MiKTeX-XeTeX 4.16, MiKTeX 25.12), pdftotext, pdfinfo, pdftoppm unter %LocalAppData%\Programs\MiKTeX\miktex\bin\x64; Python 3.12.10 unter %LocalAppData%\Programs\Python\Python312 (sympy 1.14.0, pypdf 6.19.0 per pip --target im Scratchpad); curl 8.21.0
Katalog: live von raw.githubusercontent.com (origin/main 68a6401; lokal ein Commit voraus, ohne Änderung an katalog/ und blaetter/index.md)

## Eingaben

1 quadgl-9-os · wartet · Anläufe 0
2 quadgl-9-gym · wartet · Anläufe 0
3 prozent-7-schwach · wartet · Anläufe 0
4 linfkt-8-neu · wartet · Anläufe 0
5 kreis-8-ausblick · wartet · Anläufe 0
6 daten-7 · wartet · Anläufe 0
7 nullstellen-fokus · wartet · Anläufe 0
8 potenz-10 · wartet · Anläufe 0
9 kurven-12-be · wartet · Anläufe 0
10 ka-terme-8-gym · wartet · Anläufe 0
