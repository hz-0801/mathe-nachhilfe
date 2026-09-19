# Auftrag: Rohdateien für alle Themen

## Ausgangslage

`werkzeuge/rohdatei-bau.py` (Commit 16e5c1f) baut Rohdateien mit
den Teilen A, B und C. Der Probelauf hat gezeigt, dass Teil C
(Fehlerquellen und Stichwörter gezählt) nichts trägt: fast jeder
Wert kommt genau einmal vor. Teil C wird gestrichen, dann werden
alle kanonischen Themen mit Katalogzeilen gebaut.

## Schritte

1. Teil C aus `werkzeuge/rohdatei-bau.py` entfernen: Code und
   Überschrift `## C Sammlung`. Teil A und Teil B unverändert
   lassen, auch die Zeilenform und die Sortierung. Den Docstring
   des Skripts anpassen, falls er Teil C nennt.

2. `rohdaten/` leeren (die zwei Dateien des Probelaufs per git rm),
   dann `python werkzeuge/rohdatei-bau.py` ohne Argument: alle
   kanonischen Themen mit mindestens einer Katalogzeile.

3. README: im Abschnitt `## rohdaten/` die Beschreibung auf Teil A
   und B anpassen und die Zahl der Dateien nennen. Sonst nichts
   ändern.

4. Diese Auftragsdatei nach `archiv/auftrag-rohdatei-voll-2026-09-19.md`
   verschieben (git mv).

5. Ein Commit: „Rohdateien für alle Themen, Teil C gestrichen".

## Prüfungen

- Zahl der Dateien in `rohdaten/` gleich der Zahl der kanonischen
  Themen mit Zeilen (erwartet 66).
- Summe aller Teil-B-Zeilen über alle Dateien gleich der Summe der
  Spalte `zeilen` in `themen.csv`.
- Jede Katalogzeile in höchstens einer Rohdatei.
- Kein „Teil C" und keine Überschrift `## C` in irgendeiner Datei
  unter `rohdaten/`.
- `python werkzeuge/themen-pruef.py` mit Rückgabewert 0.
- Keine Datei außerhalb von `rohdaten/`, `werkzeuge/`, `README.md`,
  `archiv/` geändert.

## Bericht (zurück in den Chat)

- Zahl der Dateien, Summe der Teil-B-Zeilen, Gesamtgröße von
  `rohdaten/` in KB.
- Die fünf größten Dateien (Zeilen, Typen in Teil A) und die fünf
  kleinsten.
- Alle Typen ohne Definition, mit Thema und Typenliste, falls es
  welche gibt.
- Über alle Dateien: Zahl der Typen gesamt und Zahl der Typen mit
  genau einer Zeile, je Profil (msa, fhr, abi+iqb).
- Abweichungen oder Annahmen.
- Commit-Hash.
- Letzte Zeile: „Push origin drücken".

## Regeln

- Nichts löschen außer den zwei Probelauf-Dateien in Schritt 2.
- Kataloge, `themen.csv`, Typenlisten nicht ändern.
- Bei Unklarheit die einfachste Lesart wählen und im Bericht
  nennen, nicht rückfragen.
