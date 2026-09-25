# Auftrag: Marken in die Katalogeinträge

## Ausgangslage

Drei Belegdateien liegen vor, keine ist in einen Eintrag geflossen:
- `katalog/_klassen-belege.md` – Klasse je Lerneinheit und Typ aus
  den Lehrwerken (Sek I), mit Verlagsmarken und Ermessensliste je
  Eintrag; Lesart im Kopf der Datei.
- `katalog/_pruefungswort-belege.md` – P10-Jahrgänge je Sek-I-Einheit
  und Typ; Abitur-GK-, LK- und FHR-Jahrgänge je Sek-II-Einheit.
- `katalog/_sek2-ordnung-belege.md` – Halbjahr (Berlin, Brandenburg)
  und Kursart je Sek-II-Einheit.
Dazu `katalog/_marken-entscheidungen.md` (Datei 2): die Urteile des
Chats über die Ermessensfälle und zwei Regeln, die für alle Stellen
gelten. Und `katalog/_marken-neue-einheiten.md` (Datei 3): drei
Ergänzungen an Einträgen, die vor dem Markenlauf eingefügt werden.

Ziel: Jede Lerneinheit jedes Eintrags trägt eine erzeugte Zeile
`Marken:` direkt unter ihrer Nummernzeile; Typen, für die ein
Verzeichnis eine eigene Stelle nennt, tragen ihre Klasse in eckigen
Klammern. Die Zeile wird von einem Skript gebaut, das im Repo bleibt
und bei geänderten Belegen neu läuft.

## Form der Marken

Sek-I-Einheit (Zeile unter der Nummernzeile, zwei Leerzeichen
eingerückt, eine Zeile, kein Umbruch):

    Marken: OS Kl. 9–10 (Sekundo 10, Mathematik 2023 9, Schnittpunkt 9, Mathematik heute 10) · GYM Kl. 9 · P10 oft · nicht für alle: Sekundo 8 LVL, Fundamente 5 Streifzug

- „OS Kl. n" bzw. „GYM Kl. n", wenn alle Reihen der Schulform in
  derselben Klasse einführen; sonst die Spanne mit der Reihenliste
  in Klammern. Reihenliste nur bei Spanne.
- Ohne Stelle in einer Schulform: „OS –" bzw. „GYM –".
- Prüfungswort aus `_pruefungswort-belege.md`, Zählung Haupt oder
  Neben (Spalte jahre_gesamt der Einheit): 7 oder mehr von 13
  Jahrgängen → „P10 oft"; 1 bis 6 → „P10"; 0 → „keine P10-Aufgabe".
- „nicht für alle:" nur, wenn es Stellen mit Verlagsmarke gibt
  (Regel B in Datei 2); sonst entfällt der Teil.
- Typ: hinter dem Typnamen in „Typen je Lerneinheit" die Klasse in
  eckigen Klammern, wenn `_klassen-belege.md` eine Typzeile für ihn
  führt oder Datei 2 eine Stelle zur Typzeile macht:
  `Kreis mit gegebenem Radius oder Durchmesser zeichnen [OS 5, GYM 6]`.
  Mehrere Reihen einer Schulform in verschiedenen Klassen: Spanne.
  Typen ohne Klammer erben die Zeile der Einheit.

Sek-II-Einheit (Sek-II-Einträge und die Sek-II-Einheiten der drei
Sek-I-Einträge mit Sek-II-Teil):

    Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR

- Halbjahr je Land aus `_sek2-ordnung-belege.md`; „BE Q1/2", wenn
  der Plan zwei Halbjahre nennt; „BE –", wenn keines belegt ist.
- Kursart: „GK" (Grund- und Leistungskurs), „nur LK", „FOS".
- Prüfungswort aus `_pruefungswort-belege.md`: „Abitur GK", wenn
  GK-Jahrgänge ≥ 1; „Abitur LK", wenn LK-Jahrgänge ≥ 1; „FHR", wenn
  FHR-Jahrgänge ≥ 1; alle drei null → „keine Prüfungsaufgabe".

Die Klammer „(Kl. n)" am Ende einer Nummernzeile fällt weg, wenn sie
nur eine Klassenangabe enthält (Muster „(Kl. 7)", „(Kl. 7/8)",
„(Kl. 5–7)"). Enthält die Klammer mehr („(Kl. 5 im Lehrwerk;
RLP B/C/D)", „(Q1, GK-Kern; FOS …)"), bleibt sie stehen; der Bericht
listet diese Zeilen. Der Text „← Eingabe …" bleibt unverändert.

## Schritte

1. Datei 3 einarbeiten: die drei Ergänzungen wortgleich an die
   genannten Stellen von `katalog/potenz-exponentialfunktionen.md`
   und `katalog/daten.md` setzen. Den Vorrat-Typ „Potenzfunktion
   y = a · xᵏ vom exponentiellen Term unterscheiden" aus Einheit 1
   von potenz-exponentialfunktionen entfernen (er wandert in die
   neue Einheit 5). `themen.csv` prüfen: braucht die neue Einheit
   ein Stichwort, trage es ein wie die anderen Zeilen des Themas.
2. Skript `werkzeuge/marken-bau.py` bauen. Es liest die drei
   Belegdateien und Datei 2 und schreibt je Eintrag die Marken-
   Zeilen und Typklammern. Es ist wiederholbar: ein zweiter Lauf
   ersetzt vorhandene Marken-Zeilen und Klammern, statt sie zu
   verdoppeln. Python über
   `%LocalAppData%\Programs\Python\Python312\python.exe`.
3. Regeln A und B aus Datei 2 im Skript umsetzen. Regel A verlangt
   je Stelle eine Lesart (Vorstufe oder Kern): Nimm die Stellen aus
   der Liste in Datei 2 und dazu alle Stellen in
   `_klassen-belege.md`, deren Ermessenstext „Vorstufe", „Einstieg",
   „Wiederaufnahme", „Zeichnen" oder „Benennen" enthält, und
   entscheide sie einzeln; jede Entscheidung außerhalb von Datei 2
   steht im Bericht mit Grund. Die Stellenliste, die das Skript
   dafür liest, liegt als `werkzeuge/marken-bau-stellen.txt` im
   Repo.
4. Skript laufen lassen über alle 29 Sek-I-Einträge und alle
   Sek-II-Einträge (Liste aus `katalog/index.md`).
5. Gegenprobe mit bekannten Werten; Abweichung ist ein Befund im
   Bericht, kein Grund, das Skript zu ändern:
   - lineare-funktionen Einheit 4: OS Kl. 8, GYM Kl. 8, P10 oft.
   - quadratische-gleichungen Einheit 2: OS Kl. 10, GYM Kl. 9.
   - prozentrechnung Einheit 1: GYM Kl. 5.
   - kreis Einheit 1: weder OS noch GYM nennt Klasse 5 oder 6;
     der Typ „Kreis mit gegebenem Radius oder Durchmesser zeichnen"
     trägt „[OS 5, GYM 6]".
   - potenz-exponentialfunktionen Einheit 5: OS Kl. 10, GYM Kl. 9,
     keine P10-Aufgabe.
   - daten Einheit 7: keine P10-Aufgabe.
   - kurvenuntersuchung Einheit 1: BE Q1 · BB Q1 · GK.
   - Zahl der Marken-Zeilen = Zahl der Lerneinheiten aller
     Einträge (114 Sek I + 2 neue + 162 Sek II laut Zahlenblock
     von `_pruefungswort-belege.md`; weicht deine Zählung ab,
     nenne beide Zahlen).
6. `python werkzeuge/themen-pruef.py` und
   `python werkzeuge/verweis-pruef.py` laufen lassen; Befunde in
   den Bericht.
7. `README.md`: `werkzeuge/marken-bau.py`, `marken-bau-stellen.txt`,
   `katalog/_marken-entscheidungen.md` und
   `katalog/_marken-neue-einheiten.md` eintragen; im Katalog-Absatz
   einen Satz zur Marken-Zeile. `katalog/index.md`: bei daten und
   potenz-exponentialfunktionen die Einheitenzahl anpassen, wenn
   sie dort steht.
8. `faellig.md` § 2: Posten „Marken neu bauen, wenn eine Belegdatei
   sich ändert · Auslöser: Commit an _klassen-belege, _pruefungswort-
   belege oder _sek2-ordnung-belege · bei wem: Claude Code" eintragen.
9. Diesen Auftrag nach `archiv/auftrag-marken-2026-09-26.md`
   verschieben (nicht löschen). Bericht als `bericht-marken.md` in
   die Wurzel. Committen mit Nachricht aus UTF-8-Datei über
   `commit -F`: „katalog: Marken-Zeilen je Lerneinheit, drei
   Einheiten ergänzt, marken-bau.py".

## Bericht (bericht-marken.md)

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann:
- Zahlen: Einträge geändert, Marken-Zeilen, Typklammern, Klammern
  „(Kl. n)" entfernt, Klammern stehen geblieben (mit Zeilen).
- Ergebnis der sieben Gegenproben, je eine Zeile, mit Ist-Wert.
- Regel A: jede Stelle außerhalb von Datei 2, die du als Vorstufe
  gelesen hast, mit Eintrag, Einheit, Reihe, Zitat, Grund.
- Regel B: Zahl der Zeilen „nicht für alle", drei Beispiele.
- Einheiten mit „OS –" oder „GYM –" (Liste).
- Was Datei 2 oder dieser Auftrag nicht regelte und wie du
  entschieden hast.
- Befunde von themen-pruef.py und verweis-pruef.py.
- Letzte Zeile: „Push origin drücken".

## Regeln

- Shell ist PowerShell 5.1: kein Heredoc, kein sed. Dateien
  schreiben mit `[System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false)))`; nach dem
  Schreiben prüfen, dass keine BOM und kein CR entstanden sind.
- Commit-Nachricht in eine UTF-8-Datei, `commit -F`; git über die
  git.exe von GitHub Desktop mit `-c core.pager=cat`.
- Nichts löschen; verschieben nach `archiv/`.
- Kein Eintragstext außer den genannten Stellen wird geändert:
  keine Umformulierung, keine Sortierung, kein Zusammenfassen.
- Skript und alle Daten, die es liest, kommen ins Repo.
- Gegenprobe erklärt, Skript bleibt.
