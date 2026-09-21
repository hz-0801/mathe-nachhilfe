# Auftrag: Umzug 2026-09-21b

## Ausgangslage

Der Chat vom 21.09.2026 ist zu Ende. Die neue Übergabe liegt als
uebergabe.md in der Wurzel. Die bisherige Übergabe (Stand
2026-09-21, Commit ae3d874) muss ins Archiv.

## Schritte

1. Prüfen, dass uebergabe.md in der Wurzel liegt und mit
   „# Übergabe 2026-09-21b" beginnt.
2. Die bisherige Übergabe aus der Git-Historie sichern:
   `git show HEAD:uebergabe.md > archiv/uebergabe-2026-09-21.md`
   (die Arbeitskopie ist bereits überschrieben).
3. Diesen Auftrag nach archiv/auftrag-umzug-2026-09-21b.md
   verschieben.
4. Committen mit der Nachricht „Umzug 2026-09-21b".

## Prüfungen

- `git status` ist nach dem Commit sauber.
- archiv/uebergabe-2026-09-21.md beginnt mit „# Übergabe
  2026-09-21" und ist nicht leer.
- `python katalog/_pruef_struktur.py` (aus katalog/ gestartet) und
  `python werkzeuge/themen-pruef.py` laufen unverändert durch;
  Kennzahl 7 = 0 von 73, Kennzahl 8 Gruppe (c) = 16, Kennzahl 9 =
  24 von 463.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Danach je eine
Zeile zu den vier Schritten, das Ergebnis der Prüfungen,
Abweichungen und Annahmen. Letzte Zeile: „Push origin drücken".

## Regeln

Keine Datei löschen. Keinen Katalogeintrag, kein Prüfskript, keine
Konkordanz und keine abgeleitete Datei anfassen.
