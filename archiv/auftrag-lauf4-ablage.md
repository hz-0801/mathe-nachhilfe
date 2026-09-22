# Auftrag: Lauf 4 ablegen (Nullstellen, 2026-09-22)

## Ausgangslage

Am 22.09.2026 lief im Projekt erzeugeUnterrichtsblatt() ein
Lernblatt mit dem Unterrichtsblatt-Prompt v4.1, Eingabe etwa
„nullstellen, 10. klasse" (der genaue Wortlaut steht in chat.txt
des Archivs). Ergebnis über 30 Seiten; das ist der Lauf, der die
Planfrage in v4.2 ausgelöst hat, und er wird als Lauf 4
ausgewertet. Der Lehrer hat am 23.09.2026 das Protokoll-Archiv
heruntergeladen; es heißt vermutlich
Nullstellen_2026-09-22_protokoll.zip und liegt in Downloads.
werkzeuge/einsortieren.py verarbeitet es; welches Katalogthema
das Blatt trägt, liest das Skript aus der Katalog-Zeile von
protokoll.txt.

## Schritte

1. Archiv finden. Suche in %USERPROFILE%\Downloads,
   %USERPROFILE%\OneDrive\Downloads und
   %USERPROFILE%\OneDrive\blatt-eingang nach einer Datei
   *Nullstellen*protokoll*.zip. Liegt sie dort nicht, suche in
   denselben Ordnern nach files.zip oder einem Archiv, das eine
   Datei *protokoll*.zip enthält; entpacke nur diese eine Datei
   nach %USERPROFILE%\Downloads. Ändere nichts anderes in den
   Ordnern des Lehrers. Notiere im Bericht, wo das Archiv lag
   und wie es genau heißt.
2. Einsortieren: python werkzeuge/einsortieren.py über den vollen
   Python-Pfad (Regeln). Erwartet wird ein neuer Ordner
   blaetter/<thema>/2026-09-22/ und eine neue Zeile in
   blaetter/index.md; <thema> ergibt sich aus protokoll.txt.
3. Auftrag archivieren: git mv auftrag-lauf4-ablage.md
   archiv/auftrag-lauf4-ablage.md.
4. Commit mit der Meldung
   „Blattablage: Nullstellen 2026-09-22 (Lauf 4)". Nicht pushen.

## Prüfungen

- blaetter/<thema>/2026-09-22/ enthält die PDFs und die Quelltexte,
  wie einsortieren.py sie anlegt.
- blaetter/index.md hat eine neue Zeile für <thema> / 2026-09-22;
  die zwei alten Zeilen (daten, prozentrechnung) sind unverändert.
- Aus src/protokoll.txt des neuen Blatts: Zeile „Prompt:", Zeile
  „Katalog:", die Zählung des Gesamts (Hauptnummern, Teilaufgaben,
  Seiten) und das Verzeichnis – wortgleich in den Bericht. Aus
  src/chat.txt die Eingabe des Lehrers und die Deutungszeile.
- git status ist nach dem Commit sauber (keine ungetrackten
  Dateien im Repo außer den in .gitignore genannten).

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann:
- Fundort und Name des Archivs, ob ein Entpacken nötig war.
- Ausgabe von einsortieren.py wortgleich.
- Die neuen Pfade unter blaetter/.
- Ergebnis jeder Prüfung, mit den verlangten Zeilen aus
  protokoll.txt und chat.txt.
- Abweichungen und Annahmen.
Letzte Zeile: „Push origin drücken".

## Regeln

- Python 3.12 liegt nicht im PATH der Claude-Code-Shell, py -3
  gibt es nicht: nur der volle Pfad
  %LocalAppData%\Programs\Python\Python312\python.exe.
- git über die git.exe von GitHub Desktop.
- Nichts löschen. Dateien werden nur angelegt, geändert oder mit
  git mv verschoben.
- Findet einsortieren.py nichts oder meldet es einen vorhandenen
  Zielordner, ist das ein Befund: melden und anhalten, nicht das
  Skript ändern.
- Keine Änderung an den Dateien des Blatts; sie werden abgelegt,
  wie sie sind.
