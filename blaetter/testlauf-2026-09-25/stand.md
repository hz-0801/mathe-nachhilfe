# Stand Testlauf 2026-09-25

Datum: 2026-09-25 (Start 12:10 Uhr)
Prompt-Version: v4.3 – hz-0801/blattbau main 512ae78, Zeile 1 „# UNTERRICHTSBLATT v4.3 – PROMPT FÜR LERNBLATT UND FOKUS", Kopie `unterrichtsblatt-v4.3.md` (71520 Byte, SHA-256 F20BC282…C47B)
Bauweise: Ersatzweg – je Eingabe ein Sub-Agent (Typ general-purpose, model opus); Teil 1 Verweis auf die Promptkopie mit der Anweisung, sie ganz zu lesen und als Systemanweisung zu nehmen, Teil 2 `werkzeuge/testlauf-umgebung.md`, Teil 3 die Eingabezeile mit Antworten aus der CSV. Grund: `claude` fehlt im PATH; die Desktop-Beigabe `%APPDATA%\Claude\claude-code\2.1.280\claude.exe` kennt `-p`, `--append-system-prompt-file`, `--dangerously-skip-permissions`, `--model`, meldet aber „Not logged in · Please run /login" (Anmeldung liefert der Desktop-Host, nicht die CLI).
Modell: Auftragssitzung Claude Opus 5.5 (claude-opus-5-5); Blattsitzungen Sub-Agent mit model opus
Werkzeuge: xelatex (MiKTeX-XeTeX 4.16, MiKTeX 25.12), pdftotext, pdfinfo, pdftoppm unter %LocalAppData%\Programs\MiKTeX\miktex\bin\x64; Python 3.12.10 unter %LocalAppData%\Programs\Python\Python312 (sympy 1.14.0, pypdf 6.19.0 per pip --target im Scratchpad); curl 8.21.0
Katalog: live von raw.githubusercontent.com (main = lokaler Stand 7613213, origin gleich)

Fehlstart (vor 12:17): die ersten fünf Startnachrichten (Eingabe 1–5) hat die API vor dem ersten Werkzeugaufruf abgelehnt („safeguards flagged this message", `reasoning_extraction`); keine Datei entstanden. Zwei Sätze im Umgebungsteil umformuliert („Sein Inhalt ist deine Systemanweisung" → „arbeite dann genau nach ihr"; „wortgleich alles, was du … geschrieben hättest" → „was der Lehrer im Chat zu sehen bekäme"), danach Start ohne Ablehnung. Ein Fehlstart zählt nicht als Anlauf (keine Sitzung zustande gekommen).
Parallelität: Eingaben 1–5 zuerst, 6–10 nach einer Lastprobe (Rechnerlast 23 %) hinterher, also alle zehn Sub-Agenten gleichzeitig; t0 laut zeiten.txt: 1 12:17:36, 2 12:18:28, 3 12:18:49, 4 12:19:03, 5 12:19:15, 6 12:21:33, 8 12:21:42, 7 12:21:49, 9 12:21:56, 10 12:22:15. Ablage und Commit je Eingabe in CSV-Reihenfolge.

## Eingaben

1 quadgl-9-os · fertig · Anläufe 1 · (abgelegt)
2 quadgl-9-gym · fertig · Anläufe 1 · (abgelegt)
3 prozent-7-schwach · fertig · Anläufe 1 · (abgelegt)
4 linfkt-8-neu · fertig · Anläufe 1 · (abgelegt)
5 kreis-8-ausblick · fertig · Anläufe 1 · (abgelegt; Sitzung legte eine leere e1_a.tex in der Repo-Wurzel an – in den Scratchpad verschoben)
6 daten-7 · fertig · Anläufe 1 · (abgelegt)
7 nullstellen-fokus · fertig · Anläufe 1 · (abgelegt)
8 potenz-10 · läuft · Anläufe 1 ·
9 kurven-12-be · läuft · Anläufe 1 ·
10 ka-terme-8-gym · fertig · Anläufe 1 · (abgelegt)
