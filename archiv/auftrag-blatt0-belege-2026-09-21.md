# Auftrag: Belege der Blatt-0-Fertigkeiten ohne Ziel sammeln

## Ausgangslage

Nach dem Auftrag „Blatt 0: Dateiverweise nachgetragen" tragen 112
Fertigkeitszeilen der Sek-I-Einträge einen Dateiverweis. 35 tragen
keinen – nicht weil der Verweis fehlt, sondern weil offen ist, ob
es überhaupt ein Katalogthema dazu gibt. Beispiele: „Schriftliches
Rechnen mit natürlichen Zahlen, Einmaleins", „Vielfache und
Teiler", „Vierecksarten kennen".

Jede dieser Zeilen trägt aber eine Quellenklammer. Dieser Auftrag
löst die Klammern gegen die Register auf, die im Repo liegen, und
legt das Ergebnis als Vorschlagsliste vor. Er ändert keinen
Eintrag und entscheidet nichts.

Voraussetzung: Der Auftrag zu den 112 Ersetzungen ist gelaufen und
committet. Ist er das nicht, brich ab und melde es.

## Schritte

1. `werkzeuge/blatt0-belege.py` (v0.1) bauen. Es liest alle
   `katalog/*.md` ohne `_*` und ohne `index.md`.
2. Je Eintrag den Abschnitt „### Voraussetzungen (Blatt 0)" nehmen
   und dort nur die Zeilen vor der Zwischenzeile
   „Erkennungsschritte…" – das sind die Fertigkeiten. Die
   Erkennungsschritte gehören dem Thema selbst und bleiben außen
   vor.
3. Eine Fertigkeitszeile hat ein Ziel, wenn sie einen Verweis der
   Form `<name>.md` auf eine vorhandene Katalogdatei enthält.
   Gesammelt werden die Zeilen ohne Ziel.
4. Aus jeder gesammelten Zeile den Inhalt der eckigen Klammer am
   Zeilenende nehmen und in Bestandteile zerlegen. Sechs Sorten,
   je Bestandteil eine:
   – **P10-Typ** (Text enthält „P10" und einen Typnamen oder eine
     Aufgabenkennung wie 2018-OS-K6d),
   – **LS-AA-Kapitel** (Form „LS-AA Kl. 8 II 1"),
   – **RLP mit Zitat** (Niveaustufe und ein Zitat in
     Anführungszeichen),
   – **RLP ohne Zitat** (nur Niveaustufe, etwa „RLP D"),
   – **MSK-Code** (Form „MSK B2B", „MSK S5A", „MSK N"),
   – **sonstiges oder keine Klammer**.
5. Auflösen, soweit ein Register es hergibt:
   – P10-Typ gegen `msa/msa-typen.csv`: der Typ steht dort mit
     seinem Thema. Findest du die Typ- und die Themenspalte nicht
     eindeutig über die Kopfzeile, melde es und lass die Sorte aus.
   – LS-AA-Kapitel gegen
     `quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt`: die
     Kapitelangabe suchen und den Abschnitt ausgeben, in dem sie
     steht.
   – RLP mit Zitat gegen
     `quellen/quelle-rlp-teil-c-mathematik-2023.txt`: das Zitat
     suchen und die Fundstelle mit Niveaustufe ausgeben.
   – RLP ohne Zitat, MSK-Code und sonstiges: nicht auflösen. Beim
     MSK-Code den Bausteintitel aus `katalog/_quellen.md`
     beilegen, soweit er dort genannt ist.
6. Für jede gesammelte Zeile zusätzlich angeben, ob ihr Wortlaut
   einen kanonischen Namen aus `themen.csv` nahelegt: Treffer nur
   melden, wenn der Themenname oder sein Thementitel wörtlich in
   der Zeile vorkommt. Keine Ähnlichkeitssuche, kein Raten.
7. `katalog/_blatt0-belege.md` schreiben, Kopf nach dem Muster von
   `_verweise.md` (Stand, Commit, Skript, „abgeleitet, nie von
   Hand ändern", Messweise, Schwäche der Messung). Aufbau: erst
   die Sek-I-Einträge, dann die übrigen; je Eintrag die Zeilen mit
   Zeilennummer, vollem Wortlaut, Klammerinhalt, Sorte und dem,
   was die Register hergeben.
8. Die Datei dort anmelden, wo `_verweise.md` angemeldet ist
   (`katalog/index.md`, `README.md`); in `_pruef_struktur.py` neue
   Kennzahl nur, wenn es sich ohne Umbau einfügt – sonst melden.
9. Auftrag nach `archiv/auftrag-blatt0-belege-2026-09-21.md`
   verschieben, committen mit der Nachricht
   „Blatt 0: Belege der Fertigkeiten ohne Ziel".

## Prüfungen

- Gegenprobe: In den 22 Sek-I-Einträgen zählt das Skript
  147 Fertigkeitszeilen, davon 112 mit Ziel und 35 ohne. Weicht
  eine der drei Zahlen ab, stimmt die Abschnitts- oder
  Zeilenerkennung nicht – dann das Skript korrigieren, nicht die
  Zahl.
- Für die übrigen 51 Einträge ist die Zahl unbekannt; sie wird
  berichtet, nicht geprüft.
- Kein Eintrag, keine Konkordanzzeile und keine der beiden
  abgeleiteten Dateien `_tragfaehigkeit.md` und `_verweise.md`
  ändert sich.
- `python katalog/_pruef_struktur.py` und
  `python werkzeuge/themen-pruef.py` laufen durch.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Dann die drei
Zahlen der Gegenprobe, die entsprechenden Zahlen der übrigen 51
Einträge, und eine Aufschlüsselung der gesammelten Zeilen nach den
sechs Klammersorten mit der Zahl der aufgelösten Fälle je Sorte.
Keine Einzelzeilen im Bericht – die stehen in der Datei.
Abweichungen und Annahmen. Letzte Zeile: „Push origin drücken".

## Regeln

Nichts entscheiden. Eine Zeile, deren Klammer kein Register
auflöst, bleibt ohne Vorschlag – das ist ein Ergebnis, kein
Mangel. Keine Ähnlichkeitssuche, keine geratene Zuordnung, keine
Ergänzung aus eigenem Fachwissen.

Modell: Opus (das Skript legt Lesarten fest).
