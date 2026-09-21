# Auftrag: Verweis- und Namensprüfung des Katalogs

## Ausgangslage

Der Themenkatalog (`katalog/`, 73 Einträge) ist fertig, aber noch
nie maschinell auf innere Stimmigkeit geprüft worden. Vor dem Umbau
der beiden Blatt-Prompte soll feststehen, ob die Verweise, die
Namen und die Konkordanz tragen. Dieser Auftrag ändert keinen
einzigen Katalogeintrag – er baut ein Prüfwerkzeug und berichtet.

Vorbild für Bau und Form ist `werkzeuge/tragfaehigkeit.py` (v0.1)
mit seiner Ausgabedatei `katalog/_tragfaehigkeit.md`. Lies das
Skript, bevor du anfängst, und übernimm seine Lesart für den
Abschnitt „### Voraussetzungen (Blatt 0)" und für die Verweisform
`<name>.md` unverändert. Zwei Werkzeuge, die verschieden zählen,
sind schlimmer als keins.

## Schritte

1. `werkzeuge/tragfaehigkeit.py` lesen und die dortige
   Abschnitts- und Verweiserkennung übernehmen.
2. `werkzeuge/verweis-pruef.py` (v0.1) bauen. Es liest alle
   `katalog/*.md` ohne `_*` und ohne `index.md`, dazu `themen.csv`,
   `abitur/abitur-vokabular.md`, die vier
   `abitur/abi-*-geltung.md` und die Typenkataloge der Profile. Es
   schreibt `katalog/_verweise.md` und gibt eine Kurzfassung auf
   stdout aus. Fünf Prüfungen:

   **1 Dateiverweise.** Jeden Verweis der Form `<name>.md` in
   jedem Abschnitt jedes Eintrags sammeln, nicht nur in Blatt 0.
   Drei Gruppen: (a) Ziel liegt in `katalog/`, (b) Ziel liegt
   anderswo im Repo, (c) Ziel gibt es nicht. Gruppe (b) und (c)
   vollständig auflisten, je mit Quelldatei und Abschnitt.

   **2 Einheitennummern.** Wo hinter einem Verweis eine
   Einheitenangabe steht („Einheit 4", „Einheit 6 und 8",
   „Einheiten 2 bis 4"), prüfen, ob die Zieldatei so viele
   Lerneinheiten hat. Maßgeblich ist die Zahl der Zeilen, die im
   Abschnitt „### Lerneinheiten" mit `<n>. ` beginnen. Melden:
   Nummer größer als vorhanden, und getrennt davon jede
   Einheitenangabe, die du nicht eindeutig einem Verweis zuordnen
   konntest. Nicht raten.

   **3 Namensgleichheit.** Vier Abgleiche:
   – jede `katalog/<x>.md` hat mindestens eine Zeile in
     `themen.csv` mit `kanonisch` = x, und umgekehrt hat jeder
     kanonische Name mit `stufe` = II eine Katalogdatei;
   – die H1-Überschrift jedes Eintrags gegen die Werte der Spalte
     `thema` seiner Zeilen (Abweichungen melden, nicht bewerten);
   – jeder `thema`-Wert der Zeilen mit `profil` = abi oder iqb
     gegen die Themenliste in `abitur-vokabular.md` § 2 und gegen
     die Themenspalte der vier `abi-*-geltung.md` § 1, in beide
     Richtungen;
   – jeder `thema`-Wert der Zeilen mit `profil` = msa oder fhr
     gegen die Themenspalte des jeweiligen Typenkatalogs, in beide
     Richtungen.
   Findest du die Themenspalte einer Datei nicht eindeutig über
   ihre Kopfzeile, brich diese Teilprüfung ab und melde es, statt
   eine Spalte zu wählen.

   **4 Gegenrichtung.** Wenn Eintrag A im Blatt-0-Abschnitt auf B
   verweist, B aber A in keinem seiner Abschnitte erwähnt, ist das
   ein Paar für die Liste. Nur auflisten, nicht bewerten.

   **5 Formlücke.** Die Einträge, deren Blatt-0-Abschnitt keinen
   einzigen Verweis der Form `<name>.md` enthält. Je Eintrag: die
   Zahl der Nennungen in Wortform und – das ist der Zweck – jede
   dieser Nennungen als wörtliches Zitat der Zeile, in der sie
   steht. Diese Zitate gehören vollständig in
   `katalog/_verweise.md`, nicht in den Bericht.

3. `katalog/_verweise.md` mit Kopf nach dem Muster von
   `_tragfaehigkeit.md`: Stand, Commit, erzeugendes Skript,
   Hinweis „abgeleitet, nie von Hand ändern", Messweise, und am
   Ende ein Abschnitt „Schwäche der Messung", der sagt, was die
   Prüfungen nicht sehen.
4. Die neue Datei dort anmelden, wo `_tragfaehigkeit.md`
   angemeldet ist: `katalog/_pruef_struktur.py`, `katalog/index.md`
   und `README.md`. Sieh nach, wie es dort für `_tragfaehigkeit.md`
   gemacht wurde, und mach es genauso.
5. Diesen Auftrag nach `archiv/auftrag-verweise-2026-09-21.md`
   verschieben und alles committen mit der Nachricht
   „Verweis- und Namensprüfung: Werkzeug und _verweise.md".

## Prüfungen

- Gegenprobe zu Prüfung 1: Für `binomialverteilung.md` muss
  Gruppe (b) den Verweis auf `abitur-vokabular.md` enthalten.
  Fehlt er, stimmt die Verweiserkennung nicht.
- Gegenprobe zu Prüfung 5: Deine Liste muss dieselben 22 Einträge
  nennen wie der Abschnitt „Messlücken" in
  `katalog/_tragfaehigkeit.md`. Weicht sie ab, ist die
  Abschnittserkennung nicht die des Vorbilds – dann korrigier das
  Skript, nicht die Liste.
- `python katalog/_pruef_struktur.py`,
  `python katalog/_pruef_katalog.py` und
  `python werkzeuge/themen-pruef.py` laufen nach der Änderung
  unverändert durch.
- `python werkzeuge/tragfaehigkeit.py` erzeugt ein
  `_tragfaehigkeit.md`, das sich nicht geändert hat.
- `git status` ist nach dem Commit sauber.

## Bericht

Erste Zeile: das Modell, mit dem der Auftrag lief. Danach je
Prüfung eine Zahl und die Abweichungen – höchstens vierzig Zeilen
je Prüfung, der Rest steht in `katalog/_verweise.md`. Bei Prüfung 5
nur die Namen der Einträge mit ihrer Nennungszahl, keine Zitate.
Dann Abweichungen vom Auftrag und Annahmen, die du treffen
musstest. Letzte Zeile: „Push origin drücken".

## Regeln

Keinen Katalogeintrag ändern, keine Zeile in `themen.csv` ändern,
keine Datei löschen. Wo eine Prüfung nicht eindeutig entscheidbar
ist, meldest du den Fall, statt ihn zu entscheiden. Keine neue
Lesart erfinden, wo `tragfaehigkeit.py` schon eine hat.

Modell: Opus (das Skript legt Lesarten fest).
