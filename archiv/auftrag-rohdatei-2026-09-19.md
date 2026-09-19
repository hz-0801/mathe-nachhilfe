# Auftrag: Rohdatei je Thema (Probelauf)

## Ausgangslage

`themen.csv` ordnet jedem Katalogthema (Spalten `profil`, `thema`)
ein kanonisches Thema zu (Spalte `kanonisch`). Die fünf Kataloge
`msa/msa-katalog-basis.csv`, `msa/msa-katalog-kontext.csv`,
`fhr/fhr-katalog.csv`, `abitur/abi-katalog.csv`,
`abitur/iqb-katalog.csv` haben dieselben 37 Spalten. Die Typenlisten
`msa/msa-typen.csv`, `fhr/fhr-typen.csv`, `abitur/abitur-typen.csv`
(gilt für abi und iqb) haben die Spalten typ, leitidee, thema,
definition, beispiel_id, status. Trennzeichen aller CSV: Semikolon,
Felder in Anführungszeichen. Listenfelder (`stichwoerter`,
`fehlerquelle`, `typ_neben`): Trennzeichen laut `katalog-prompt.md`
nachschlagen, nicht raten.

Eine Rohdatei ist der Lesestoff, aus dem ein Chat später den
Themenkatalog-Eintrag schreibt. Sie zeigt, was zu einem kanonischen
Thema tatsächlich geprüft wird.

## Schritte

1. Schreibe `werkzeuge/rohdatei-bau.py`. Aufruf aus der Repo-Wurzel:
   `python werkzeuge/rohdatei-bau.py [thema ...]`. Ohne Argument alle
   kanonischen Themen mit mindestens einer Katalogzeile; mit
   Argumenten nur die genannten. Ausgabe: je Thema
   `rohdaten/<kanonisch>.md`, überschreibt vorhandene Dateien.
   Das Skript liest nur, ändert keine Kataloge.

2. Aufbau jeder Rohdatei, genau in dieser Reihenfolge:

   Kopf: `# Rohdatei <kanonisch>`, dann Stufe, dann eine Zeile je
   Profilthema aus `themen.csv` in der Form
   `- msa: Wahrscheinlichkeit mehrstufig (17 Zeilen)`, dann
   Stand (Datum, kurzer Hash des HEAD-Commits).

   Teil A – Typenprofil. Alle Werte von `typ` der zugehörigen Zeilen,
   absteigend nach Zeilenzahl. Je Typ ein Absatz:
   Typname, Zeilenzahl, Profile (mit Zeilenzahl je Profil),
   Jahre (kleinstes–größtes), Status und Definition aus der
   Typenliste des Profils. Kommt derselbe Typname in mehreren
   Typenlisten vor, alle Definitionen nennen, je mit Profil.
   Fehlt eine Definition, `(keine Definition in <liste>)` schreiben.
   Danach ein Absatz „Nebentypen": alle Werte aus `typ_neben` mit
   Zeilenzahl, ohne Definition.

   Teil B – Zeilenliste. Eine Zeile je Katalogzeile, sortiert nach
   Profil in der Reihenfolge msa, fhr, abi, iqb, dann typ, dann jahr,
   dann id. Vor jedem Profilwechsel eine Zwischenüberschrift
   `## msa` usw. Zeilenform:
   `id | punkte | hilfsmittel | format · operator | gegeben → gesucht | verfahren`
   Senkrechte Striche im Inhalt durch `¦` ersetzen. Zeilenumbrüche
   im Inhalt durch Leerzeichen ersetzen. Keine Zeile kürzen.

   Teil C – Sammlung. Zwei Listen, jeweils alle Einzelwerte aus den
   Listenfeldern der zugehörigen Zeilen, getrimmt, exakt entdoppelt,
   absteigend nach Häufigkeit, Häufigkeit in Klammern:
   `## Fehlerquellen` aus `fehlerquelle`,
   `## Stichwörter` aus `stichwoerter`.

3. Lauf: `python werkzeuge/rohdatei-bau.py brueche-dezimalzahlen
   wahrscheinlichkeit`. Nur diese zwei; kein Vollausbau.

4. README: Abschnitt `## rohdaten/ – Rohdateien je Thema` nach
   `katalog/` einfügen: Zweck (Lesestoff für Katalogeinträge),
   abgeleitet aus `themen.csv` und den Katalogen, nie von Hand
   ändern, neu bauen mit dem Skript. Unter `werkzeuge/` eine Zeile
   für `rohdatei-bau.py`. Sonst nichts an der README ändern.

5. Diese Auftragsdatei nach `archiv/auftrag-rohdatei-2026-09-19.md`
   verschieben (git mv).

6. Ein Commit: „Rohdatei-Skript, Probelauf zwei Themen".

## Prüfungen

- Zeilenzahl je Rohdatei (Teil B) gleich der Summe der Spalte
  `zeilen` aller Profilthemen des kanonischen Themas in
  `themen.csv`. Bei Abweichung abbrechen und melden.
- Jede Katalogzeile landet in höchstens einer Rohdatei (über
  Profil und Thema eindeutig).
- `python werkzeuge/themen-pruef.py` läuft danach unverändert mit
  Rückgabewert 0.
- Keine Datei außerhalb von `rohdaten/`, `werkzeuge/`, `README.md`,
  `archiv/` geändert.

## Bericht (zurück in den Chat)

- Je Rohdatei: Zeilen in Teil B, Zahl der Typen in Teil A, davon
  ohne Definition, Zahl der Einträge in Teil C je Liste und die
  drei häufigsten Fehlerquellen mit Häufigkeit.
- Trennzeichen der Listenfelder laut `katalog-prompt.md`.
- Die kanonischen Themen ohne Katalogzeilen (Anzahl und Namen).
- Dateigröße der beiden Rohdateien in Zeilen und KB.
- Abweichungen oder Annahmen, falls etwas nicht wie beschrieben
  ging.
- Commit-Hash.
- Letzte Zeile: „Push origin drücken".

## Regeln

- Nichts löschen; verschieben nur wie in Schritt 5.
- Kataloge, `themen.csv`, Typenlisten nicht ändern.
- Keine weiteren Themen bauen als die zwei genannten.
- Bei Unklarheit die einfachste Lesart wählen und im Bericht
  nennen, nicht rückfragen.
