# Stand Testlauf 2026-09-25

Datum: 2026-09-25 (Start 12:10 Uhr)
Prompt-Version: v4.3 – hz-0801/blattbau main 512ae78, Zeile 1 „# UNTERRICHTSBLATT v4.3 – PROMPT FÜR LERNBLATT UND FOKUS", Kopie `unterrichtsblatt-v4.3.md` (71520 Byte, SHA-256 F20BC282…C47B)
Bauweise: Ersatzweg – je Eingabe ein Sub-Agent (Typ general-purpose, model opus); Teil 1 Verweis auf die Promptkopie mit der Anweisung, sie ganz zu lesen und als Systemanweisung zu nehmen, Teil 2 `werkzeuge/testlauf-umgebung.md`, Teil 3 die Eingabezeile mit Antworten aus der CSV. Grund: `claude` fehlt im PATH; die Desktop-Beigabe `%APPDATA%\Claude\claude-code\2.1.280\claude.exe` kennt `-p`, `--append-system-prompt-file`, `--dangerously-skip-permissions`, `--model`, meldet aber „Not logged in · Please run /login" (Anmeldung liefert der Desktop-Host, nicht die CLI).
Modell: Auftragssitzung Claude Opus 5.5 (claude-opus-5-5); Blattsitzungen Sub-Agent mit model opus
Werkzeuge: xelatex (MiKTeX-XeTeX 4.16, MiKTeX 25.12), pdftotext, pdfinfo, pdftoppm unter %LocalAppData%\Programs\MiKTeX\miktex\bin\x64; Python 3.12.10 unter %LocalAppData%\Programs\Python\Python312 (sympy 1.14.0, pypdf 6.19.0 per pip --target im Scratchpad); curl 8.21.0
Katalog: live von raw.githubusercontent.com (main = lokaler Stand 7613213, origin gleich)

## Eingaben
