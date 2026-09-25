# Umgebung für eine Blattsitzung im Testlauf (Ersatzweg)

Zweiter Teil der Anweisung an jeden Sub-Agenten des Testlaufs
(`archiv/auftrag-testlauf-<datum>.md`, Teil 1 Schritt 3, Ersatzweg).
Der erste Teil ist der Prompt, der dritte die Eingabe. Dieser Teil
ersetzt nur, was im Claude-Projekt die Oberfläche und die Sandbox
liefern; am Prompt ändert er nichts. `{ARBEIT}`, `{PROMPT}` und
`{PYLIB}` setzt die Auftragssitzung ein.

Die Nachricht an den Sub-Agenten besteht aus den drei Blöcken unter
dem Strich; `{EINGABE}` ist die Spalte `eingabe` der CSV, `{ANTWORTEN}`
die Spalte `antworten`.

---

TEIL 1 – SYSTEMANWEISUNG

Die Anleitung für diese Aufgabe steht in `{PROMPT}`. Lies sie zuerst
vollständig mit dem Read-Tool (sie ist länger als eine Leseseite;
lies in Abschnitten bis zur letzten Zeile) und arbeite dann genau
nach ihr.

TEIL 2 – UMGEBUNG (vom Testlauf gesetzt, nicht Teil des Prompts)

Du läufst nicht im Claude-Projekt mit Chat und Dateikarten, sondern
unbeaufsichtigt auf einem Windows-Rechner. Der Prompt bleibt, wie er
ist; nur diese Punkte ersetzen die Oberfläche und die Linux-Sandbox:

- Kein Gegenüber. Niemand antwortet auf eine Frage und niemand
  schreibt „weiter". Die Eingabe unten enthält die Antworten auf
  Planfrage und Zone; nimm sie als Freitext nach 1.1 und baue ohne
  Halt bis zum Ausgabeblock durch. Keine Rückfrage.
- Arbeitsverzeichnis: `{ARBEIT}`. Alle Dateien (Quelltexte, PDFs,
  Logs, pruef.py, zeiten.txt, Archiv) entstehen dort. „Übergeben"
  heißt: das PDF liegt fertig in diesem Verzeichnis. Außerhalb
  schreibst du nichts. Das lokale Repo
  `C:\Users\holge\mathe\mathe-nachhilfe` liest und änderst du nicht;
  Katalog, Register, Vorlage und Anleitung holst du per curl von
  raw.githubusercontent.com, wie der Prompt es sagt.
- Shell: PowerShell 5.1, kein bash. `curl` ist dort ein Alias –
  schreibe `curl.exe`. Kein `&&` (statt dessen `;` oder
  `if ($?) { … }`). Zeitstempel statt `echo "t0 $(date +%s)" >>
  zeiten.txt`: `Add-Content -Encoding ascii zeiten.txt ("t0 " +
  [DateTimeOffset]::UtcNow.ToUnixTimeSeconds())` – mit dem Stempelwort
  des Prompts an Stelle von „t0".
- Werkzeuge (nicht im PATH; setze zu Beginn jedes Aufrufs, der sie
  braucht, `$env:PATH = "$env:LOCALAPPDATA\Programs\MiKTeX\miktex\bin\x64;" + $env:PATH`):
  `xelatex`, `pdftotext` (`-layout -enc UTF-8`), `pdfinfo`,
  `pdftoppm` (Seiten als PNG rendern, `-png -r 60`). Python:
  `& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"`,
  sympy und pypdf mit `$env:PYTHONPATH = "{PYLIB}"`. xelatex mit
  `-interaction=nonstopmode`. Gerenderte Seiten siehst du mit dem
  Read-Tool an (PNG oder direkt das PDF mit Seitenangabe).
- Dateien schreibst du mit dem Write-Tool (UTF-8 ohne BOM); gezielte
  Korrekturen mit dem Edit-Tool.
- Protokoll-Archiv: zippen mit Python (`zipfile`) oder
  `Compress-Archive`.
- Keine Sub-Agenten starten.
- Deine letzte Nachricht zeigt, was der Lehrer im Chat zu sehen
  bekäme (2.7, 6.1): Deutungszeile, Plan, gegebenenfalls die
  Planfrage mit der Antwort aus der Eingabe, die Zeile nach der
  Zone, die Namen der fertigen Dateien und den Ausgabeblock (6.3).

TEIL 3 – EINGABE DES LEHRERS (erste Nutzerzeile des Chats)

{EINGABE} – Antworten auf Planfrage und Zone: {ANTWORTEN}; baue ohne Halt bis zum Ausgabeblock durch
