# Auftrag: Lauf 3 ablegen (Daten, 2026-09-22)

## Ausgangslage

Am 22.09.2026 lief im Projekt erzeugeUnterrichtsblatt() der dritte
Testlauf des Unterrichtsblatt-Prompts v4.1 mit der Eingabe „daten".
Ergebnis: fünf Dateien (Daten_Blatt0.pdf, Daten_E1.pdf,
Daten_Gesamt.pdf, Daten_Loesungen.pdf, Daten_2026-09-22_protokoll.zip).
Der Lehrer hat sie als ein Archiv heruntergeladen; es heißt
vermutlich files.zip und liegt in Downloads. Darin liegt das
Protokoll-Archiv Daten_2026-09-22_protokoll.zip, das
werkzeuge/einsortieren.py verarbeitet.

Die Befunde der Auswertung liegen in befund-lauf3-2026-09-22.md
(Datei 2 dieses Blocks). Sie gehören ins Repo und in die README.

## Schritte

1. Archiv finden. Suche in %USERPROFILE%\Downloads,
   %USERPROFILE%\OneDrive\Downloads und
   %USERPROFILE%\OneDrive\blatt-eingang nach
   Daten_2026-09-22_protokoll.zip. Liegt es dort nicht, suche in
   denselben Ordnern nach files.zip oder einem Archiv, das eine
   Datei *protokoll*.zip enthält; entpacke nur diese eine Datei
   nach %USERPROFILE%\Downloads. Ändere nichts anderes in den
   Ordnern des Lehrers. Notiere im Bericht, wo das Archiv lag.
2. Einsortieren: py -3 werkzeuge/einsortieren.py (oder der volle
   Python-Pfad, siehe Regeln). Erwartet wird ein neuer Ordner
   blaetter/daten/2026-09-22/ und eine neue Zeile in
   blaetter/index.md.
3. README.md: Im Abschnitt „Wo fange ich an" unmittelbar nach der
   Zeile zu befund-testlauf-2026-09-22.md diese Zeile einfügen:
   - `befund-lauf3-2026-09-22.md` – Befund des dritten Testlaufs
     (Lernblatt Daten, v4.1): Bereitstellung, Stufenschnitt,
     Werkzeuggrenze, Bausteinliste für Vorlage Stufe 4.
   Sonst nichts in README.md ändern.
4. Auftrag archivieren: git mv auftrag-lauf3-ablage.md
   archiv/auftrag-lauf3-ablage.md.
5. Commit mit der Meldung
   „Blattablage: Daten 2026-09-22 (Lauf 3); Befund Lauf 3".
   Nicht pushen.

## Prüfungen

- blaetter/daten/2026-09-22/ enthält die vier PDFs und den Ordner
  oder die Dateien der Quelltexte, wie einsortieren.py sie anlegt.
- blaetter/index.md hat eine Zeile für daten / 2026-09-22.
- befund-lauf3-2026-09-22.md liegt in der Wurzel, beginnt mit
  „# Befund Lauf 3" und hat mehr als 100 Zeilen.
- README.md enthält die neue Zeile genau einmal.
- git status ist nach dem Commit sauber (keine ungetrackten
  Dateien im Repo außer den in .gitignore genannten).

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann:
- Fundort des Archivs und ob ein Entpacken aus files.zip nötig war.
- Ausgabe von einsortieren.py wortgleich.
- Die neuen Pfade unter blaetter/.
- Ergebnis jeder Prüfung.
- Abweichungen und Annahmen.
Letzte Zeile: „Push origin drücken".

## Regeln

- Python 3.12 liegt nicht im PATH der Claude-Code-Shell: py -3
  oder %LocalAppData%\Programs\Python\Python312\python.exe.
- git über die git.exe von GitHub Desktop.
- Nichts löschen. Dateien werden nur angelegt, geändert oder mit
  git mv verschoben.
- Findet einsortieren.py nichts, ist das ein Befund: melden und
  anhalten, nicht das Skript ändern.
- Keine Änderung an befund-lauf3-2026-09-22.md; sie wird wortgleich
  abgelegt.
