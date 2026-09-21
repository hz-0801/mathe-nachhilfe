# Auftrag: Befundbericht nachträglich ablegen

## Ausgangslage

`befund-inkonsistenzen-2026-09-21.md` wird von der Übergabe
2026-09-21b als zentraler Text genannt und ist nie im Repo
angekommen: Der Umzugsblock vom 21.09. enthielt ihn, Commit
ae3d874 hat aber nur die Übergabe abgelegt. Der Text liegt diesem
Auftrag als zweite Datei bei.

## Schritte

1. Prüfen, dass `befund-inkonsistenzen-2026-09-21.md` in der Wurzel
   liegt und mit „# BEFUND – Inkonsistenzen vor dem Promptumbau"
   beginnt.
2. Diesen Auftrag nach `archiv/auftrag-befund-ablage-2026-09-21.md`
   verschieben.
3. Committen mit der Nachricht
   „Befund Inkonsistenzen nachträglich abgelegt".

## Prüfungen

- `git status` ist nach dem Commit sauber.
- `git diff --stat` nennt genau zwei Dateien: die Befunddatei und
  den verschobenen Auftrag. Kein Katalogeintrag, keine abgeleitete
  Datei, keine Zeile in `themen.csv` oder `faellig.md`.
- `python katalog/_pruef_struktur.py` (aus `katalog/` gestartet)
  und `python werkzeuge/themen-pruef.py` laufen durch.

## Bericht

Erste Zeile: das Modell. Danach je eine Zeile zu den drei
Schritten, das Ergebnis der Prüfungen, Abweichungen. Letzte Zeile:
„Push origin drücken".

## Regeln

An der Befunddatei nichts ändern – sie wird abgelegt, nicht
bearbeitet. Keine Datei löschen.
