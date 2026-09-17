# NAMENSSCHEMA – Dateiarten, Kennungen, Erweiterbarkeit
Version 0.1 · 17.09.2026 · Vorschlag (Auftrag D „Namensschema, Erweiterbarkeit,
Begründungen", Teil 1); gilt für alle Profile. Über die Umbenennungen in § 4
entscheidet der Lehrer; bis dahin gelten die heutigen Namen (§ 1), und neue
Dateien folgen § 2 und § 3, wo das ohne Umbenennung möglich ist (erste
Anwendung: die Geltungsdateien `abi-<zielprüfung>-geltung.md`, Teil 2).

## 1 Bestand: Dateiarten und heutiges Benennungsmuster

Grundlage: `git ls-files` (54 Dateien) und die lokalen Ordner hefte/ und
hefte-md/ (Stand 17.09.2026, nach Abgleichlauf 23). Muster in spitzen
Klammern; `<kennung>` ist die Profil-Kennung (msa, fhr, abi, iqb).

| Dateiart | Heutiges Muster | Dateien | Befund |
|---|---|---|---|
| Kern (Erfassungsmethode) | `katalog-prompt.md` | 1 | ohne Präfix, gilt für alle Profile |
| Profil | `<kennung>.md` | msa.md, fhr.md, abi.md, iqb.md | Kennung = Prüfungsart (msa, fhr, abi) bzw. Quelle (iqb); das Land steckt nicht im Namen |
| Katalogdatei | `<kennung>-katalog.csv`; msa `katalog-basis.csv`, `katalog-kontext.csv` | fhr-katalog.csv, abi-katalog.csv, iqb-katalog.csv; msa zwei Dateien | msa ohne Präfix und im Zwei-Dateien-Modell (Entscheidung 14); die übrigen eine Datei mit Feld `block` |
| Typenliste | `<kennung>-typen.csv`; msa `typen.csv`; abi+iqb `abitur-typen.csv` | typen.csv, fhr-typen.csv, abitur-typen.csv | drei Muster: ohne Präfix, Profilpräfix, Familienname „abitur" für die geteilte Liste |
| Prüfungsliste (Hefte/Stapel, Befunde, Änderungslog) | `<kennung>-pruefungen.md`; msa `pruefungen.md` | pruefungen.md, fhr-pruefungen.md, abi-pruefungen.md, iqb-pruefungen.md | msa ohne Präfix |
| Quellenverzeichnis | `<kennung>-quellen.md`, dazu erzeugte `<kennung>-quellen.csv` mit Erzeuger `<kennung>-quellen.py` | abi-quellen.md; iqb-quellen.md, .csv, .py | msa: Quelle in pruefungen.md § 1; fhr: in fhr.md § 2 und fhr-pruefungen.md – kein eigenes Verzeichnis |
| Bau-Skript | `<kennung>-bau.py` | fhr-bau.py, abi-bau.py, iqb-bau.py | msa hat keines (Erfassung vor dem Skriptmodell); jedes Skript trägt die ZEILEN des letzten Hefts/Stapels |
| Abgleichskript | `abgleich.py` (bis Lauf 11 `iqb-abgleich.py`) | 1 | ohne Präfix, obwohl es nur die Familie abi/iqb betrifft |
| Erzeuger abgeleiteter Dateien | `<kennung>-<erzeugnis>.py` → `<kennung>-<erzeugnis>.md` | fhr-typenbibliothek.py/.md; iqb-quellen.py/.csv | Muster konsistent |
| Vorgabendatei (amtliche Vorgaben, Jahrescheck) | `<kennung>-vorgaben.md`; msa `vorgaben.md` | vorgaben.md (msa), abi-vorgaben.md (abi und iqb) | msa ohne Präfix; abi-vorgaben.md gilt für zwei Profile unter dem Präfix eines davon |
| Vokabular (Sachgebiete, Themen, Klassen) | `abitur-vokabular.md` (abi+iqb); msa und fhr im Profil § 5–6 | 1 | Familienname „abitur"; für msa und fhr keine eigene Datei |
| Geltung (Zielprüfung × Thema) | Tabelle in `abitur-vokabular.md` § 3 mit den Spalten be-gk, be-lk, bb-gk, bb-ea | – | keine Datei; fhr: Schwerpunktmarkierung (27)/(28) in fhr.md § 6; msa: keine Geltung |
| Quelltexte amtlicher Quellen | `quelle-<herausgeber>-<gegenstand>-<jahr>.txt`, Übersicht `quellen.md` | quelle-rlp-teil-c-mathematik-2023.txt, quelle-klett-fahrplan-ls-aa-berlin-2024.txt, quelle-lisum-planungshilfen-7bis10.txt | konsistent; gehören zum Themenkatalog (konzept.md § 3), nicht zu einem Profil |
| Heftdateien (lokal, nicht im Repo) | `hefte/<papier>.pdf` mit papier = `<jahr>-<land>-<niveau>[-cas]`; dazu `hefte/<papier>.txt`, abgeschriebene Verlagstexte `hefte/hinweise-<band>.md`, `hefte/stichwort-<band>.md` | 15 PDF, 4 TXT, 5 MD (nur abi) | msa und fhr halten keine lokalen Hefte (curl mit dem amtlichen Dateinamen, z. B. 25_P10_Ma_A.pdf, 26_FOS_Ma_LH_C.pdf); iqb-Cache `iqb-pdf/<Kennung>_Aufgabe.pdf` |
| Markdown-Korpus (lokal) | `hefte-md/<papier>.md`, Bilder `hefte-md/<papier>/abb-N.jpg` | 10 Hefte | konsistent mit den Heftdateien |
| Befund- und Bestandsdateien (einmalig) | uneinheitlich: `repo-bestand.md`, `abi-iqb-typen.md`, `abi-aufbau.md`, `abi-struktur.json`, `Testauswertung_…_JJJJ-MM-TT.md`, `Bewertung_Masterprompt_v3-34.md` | 6 | kein Muster; Werkstattdateien in CamelCase mit Unterstrich |
| Konzept, Landkarte, Anweisung | `konzept.md`, `blatt-konzept.md`, `README.md`, `CLAUDE.md`, `CHANGELOG.md` | 5 | ohne Präfix (repoweit) bzw. Konvention der Werkzeuge (CLAUDE.md, README.md) |
| Blattbau (Prompts, Vorlage) | `masterprompt.md`, `pruefungsprompt.md`, `mathblatt.sty`, `Anleitung_mathblatt.md`, `uebergabe.md`, `archiv-hinweis.md` | 6 | anderes Projekt (repo-bestand.md § 1: B); hier nicht geregelt |

Kennungen unterhalb der Dateiebene, die das Schema mitträgt, weil Dateinamen
aus ihnen gebildet werden:

| Kennung | Heute | Wo |
|---|---|---|
| Profil-Kennung | msa, fhr, abi, iqb | Dateipräfix, Kern § 1 („<kennung>.md") |
| Land | be, bb; bebb für gemeinsame Hefte | abi papier, Geltungstabelle, Zielprüfungen |
| Niveau | gk, lk (Berlin), ea (Brandenburg erhöht), gk (Brandenburg grundlegend in der Geltungstabelle), ga/ea (Pool), EBR/FOR (msa) | papier, Zielprüfungen, Stapel |
| Zielprüfung | be-gk, be-lk, bb-gk, bb-ea | Geltungstabelle, abi-bau.py ziele_von, Kennzahlen |
| papier (Heftkürzel) | abi `<jahr>-<land>-<niveau>[-cas]`; iqb `<jahr>-iqb-<niveau>[-mms]`; msa `OS`, `EBR`, `FOR`, `MUSTER-FOR`; fhr `A`, `B`, `C` | Katalogfeld, Dateinamen unter hefte/ und hefte-md/ (abi) |
| Stapel (iqb) | `<jahr>-<niveau>-<teil>[-<rechner>]`: 2026-ga-A, 2026-ga-B-wtr | iqb-quellen.csv, iqb-bau.py KONFIG |
| Rechnerfassung | unmarkiert = WTR; -cas, -mms | papier, Stapel, Dateinamen |

## 2 Vorgeschlagenes Schema

**Bausteine.** Alle Kennungen klein, ohne Umlaute, Bausteine mit Bindestrich
verbunden; Dateinamen aus Kennung, Dateiart und Endung: `<kennung>-<dateiart>.<endung>`.

| Baustein | Werte | Regel |
|---|---|---|
| Prüfungsart | msa, fhr, abi; künftig z. B. zk (zentrale Klassenarbeit), bbr | die gebräuchliche Kurzbezeichnung der Prüfung, zwei bis vier Buchstaben; sie ist der Familienname alles Geteilten (Typenliste, Vokabular, Abgleich) |
| Träger | Länderkürzel be, bb, ni, nw, by, bw, he, hh, hb, mv, rp, sl, sn, st, sh, th; länderübergreifend iqb, kmk; gemeinsame Hefte durch Aneinanderreihung in der Reihenfolge der amtlichen Kopfzeile (bebb) | wer die Prüfung stellt; der Pool ist ein Träger ohne Land |
| Schulform | os (Oberschule/Gesamtschule), gym, fos, bg | nur, wenn dieselbe Prüfungsart desselben Trägers je Schulform verschieden ist; sonst weggelassen |
| Niveau | wie der Träger es nennt: gk, lk, ga, ea, ebr, for | nur, wenn die Prüfungsart Niveaus kennt; das Kürzel des Trägers, nicht vereinheitlicht (Berlin „Grundkurs" = gk, Brandenburg „grundlegendes Anforderungsniveau" = ga; die Geltungstabelle schreibt heute bb-gk, § 5) |
| Jahrgang | JJJJ des Prüfungsjahrs; bsp für undatierte Beispielaufgaben | |
| Rechnerfassung | unmarkiert = Regelfall ohne MMS (WTR); -cas, -mms | Suffix am Ende |

**Kennungsstufen.** Aus den Bausteinen entstehen vier Kennungen, jede eindeutig:

| Stufe | Muster | Beispiele |
|---|---|---|
| Familie (Geteiltes) | `<prüfungsart>` | abi, msa, fhr |
| Profil | `<prüfungsart>-<träger>[-<schulform>]` | abi-bebb, abi-iqb, msa-bb, fhr-bb; neu: abi-ni, msa-bb-gym |
| Zielprüfung | `<prüfungsart>-<träger>[-<schulform>]-<niveau>` | abi-be-gk, abi-be-lk, abi-bb-gk, abi-bb-ea, msa-bb-for, fhr-bb; neu: abi-ni-ga |
| Heft (papier) | `<jahrgang>-<träger>[-<schulform>]-<niveau>[-<rechner>]` | 2025-bebb-gk, 2026-bb-ea, 2017-be-gk-cas; neu: 2028-ni-ga |

Die Profil-Kennung ersetzt die heutige Kurzkennung. Kurzkennungen bleiben
als Aliasse lesbar, solange nur ein Träger die Prüfungsart führt (msa =
msa-bb, fhr = fhr-bb, abi = abi-bebb, iqb = abi-iqb); mit dem ersten zweiten
Träger derselben Prüfungsart ist die Kurzform mehrdeutig (§ 5).

**Regel je Dateiart**, mit dem erfundenen Neufall „Niedersachsen, Abitur,
grundlegendes Niveau, Jahrgang 2028" (Profil abi-ni; die Typenliste teilt
es mit abi-bebb und abi-iqb, weil die Prüfungsart dieselbe ist):

| Dateiart | Muster | Heute (Bestand) | Neufall abi-ni |
|---|---|---|---|
| Kern | `katalog-prompt.md` | katalog-prompt.md | unverändert |
| Profil | `<profil>.md` | abi-bebb.md, abi-iqb.md, msa-bb.md, fhr-bb.md | abi-ni.md |
| Katalog | `<profil>-katalog.csv`; bei Zwei-Dateien-Modell `<profil>-katalog-<block>.csv` | abi-bebb-katalog.csv, abi-iqb-katalog.csv, msa-bb-katalog-basis.csv, msa-bb-katalog-kontext.csv, fhr-bb-katalog.csv | abi-ni-katalog.csv |
| Typenliste | `<familie>-typen.csv` | abi-typen.csv (abi-bebb, abi-iqb), msa-typen.csv, fhr-typen.csv | abi-typen.csv (geteilt; beispiel_id darf in abi-ni-katalog.csv zeigen) |
| Vokabular | `<familie>-vokabular.md`; ohne eigene Datei im Profil § 5–6 | abi-vokabular.md | abi-vokabular.md (geteilt; Sachgebiete und Themenliste sind die der Bildungsstandards, niedersächsische Ergänzungen als Themen mit Geltungszeile) |
| Geltung | `<zielprüfung>-geltung.md`, eine Datei je Zielprüfung; das Profil nennt seine Zielprüfungen | abi-be-gk-geltung.md, abi-be-lk-geltung.md, abi-bb-gk-geltung.md, abi-bb-ea-geltung.md (Teil 2); fhr-bb-geltung.md und msa-bb-for-geltung.md, sobald msa/fhr eine Geltung führen | abi-ni-ga-geltung.md, abi-ni-ea-geltung.md |
| Prüfungsliste | `<profil>-pruefungen.md` | abi-bebb-pruefungen.md, abi-iqb-pruefungen.md, msa-bb-pruefungen.md, fhr-bb-pruefungen.md | abi-ni-pruefungen.md |
| Quellenverzeichnis | `<profil>-quellen.md`; erzeugte Liste `<profil>-quellen.csv`, Erzeuger `<profil>-quellen.py` | abi-bebb-quellen.md, abi-iqb-quellen.md/.csv/.py | abi-ni-quellen.md |
| Bau-Skript | `<profil>-bau.py` | abi-bebb-bau.py, abi-iqb-bau.py, fhr-bb-bau.py | abi-ni-bau.py |
| Abgleichskript | `<familie>-abgleich.py` | abi-abgleich.py | abi-abgleich.py (zieht dann drei Kataloge mit) |
| Erzeuger abgeleiteter Dateien | `<profil>-<erzeugnis>.py` → `<profil>-<erzeugnis>.md` | fhr-bb-typenbibliothek.py/.md | abi-ni-typenbibliothek.py/.md |
| Vorgaben | `<familie>-vorgaben.md`, wenn die Vorgaben mehrere Profile betreffen, sonst `<profil>-vorgaben.md` | abi-vorgaben.md (Prüfungsschwerpunkte beider Länder, gelesen von abi-bebb und abi-iqb), msa-bb-vorgaben.md | abi-ni-vorgaben.md (eigene Landesvorgaben) oder Abschnitt in abi-vorgaben.md |
| Quelltexte amtlicher Quellen | `quelle-<herausgeber>-<gegenstand>-<jahr>.<endung>`, Übersicht `quellen.md` | unverändert | quelle-ni-kerncurriculum-2028.txt |
| Heftdateien (lokal) | `hefte/<profil>/<papier>.pdf` (Textauszug `.txt`, Verlagstexte `hinweise-<band>.md`, `stichwort-<band>.md` im selben Ordner) | hefte/abi-bebb/2025-bebb-gk.pdf, hefte/abi-bebb/hinweise-2027-bebb.md; iqb-Cache hefte/abi-iqb/<Kennung>_Aufgabe.pdf (heute iqb-pdf/) | hefte/abi-ni/2028-ni-ga.pdf |
| Markdown-Korpus (lokal) | `hefte-md/<profil>/<papier>.md`, Bilder `hefte-md/<profil>/<papier>/abb-N.jpg` | hefte-md/abi-bebb/2025-bebb-gk.md | hefte-md/abi-ni/2028-ni-ga.md |
| Befunde (einmalig, keine Regel) | `befund-<gegenstand>[-<datum>].md` | befund-repo-bestand.md, befund-abi-iqb-typen.md, befund-abi-aufbau-2017-2018.md (mit abi-struktur.json als befund-abi-struktur-2017-2018.json) | – |
| Konzept, Landkarte, Anweisung | ohne Präfix, wie heute | konzept.md, namensschema.md, README.md, CLAUDE.md | unverändert; CLAUDE.md § 1 nennt das neue Profil |
| Blattbau | außerhalb dieses Schemas | – | – (Vorschlag in repo-bestand.md § 2: Präfix blatt- oder eigenes Repo) |

Katalogwerte bleiben, wie sie sind: `papier` und `id` sind Fakten der Zeile
(Kern § 5, id-Muster im Profil), sie werden nicht nachträglich umgeschrieben.
Das Schema verlangt für **neue** Profile nur, dass papier das Heftmuster oben
erfüllt und die id mit papier beginnt (abi: `2018-bb-ea-B2.1c`); msa (`OS`,
`FOR`) und fhr (`A`, `B`, `C`) behalten ihre Muster, das Jahr steht dort in
der id vorn. Für lokale Heftdateien dieser Profile gilt dann
`hefte/<profil>/<jahr>-<papier>.pdf` (hefte/msa-bb/2025-os.pdf).

## 3 Prüfung: zwei Träger, dieselbe Prüfungsart

Fall: Niedersachsen führt das Abitur ein (Profil abi-ni) neben abi-bebb und
abi-iqb.

- Profile: abi-bebb, abi-iqb, abi-ni – verschieden.
- Zielprüfungen: abi-be-gk, abi-be-lk, abi-bb-gk, abi-bb-ea, abi-ni-ga,
  abi-ni-ea – verschieden; die Geltungsdateien kollidieren nicht.
- Kataloge: abi-bebb-katalog.csv, abi-iqb-katalog.csv, abi-ni-katalog.csv –
  verschieden.
- Geteilt: abi-typen.csv, abi-vokabular.md, abi-abgleich.py. Die
  Typenliste verlangt, dass jede beispiel_id in genau einem der Kataloge
  steht: die ids sind verschieden, weil papier den Träger trägt
  (2028-ni-ga-B2a gegen 2028-be-gk-B2a) und die Poolkennungen ihr eigenes
  Muster haben. Der Verweis „Dublette von: <id>" bleibt eindeutig.
- Hefte: hefte/abi-ni/2028-ni-ga.pdf gegen hefte/abi-bebb/2028-be-gk.pdf –
  verschieden auch ohne Ordner.
- Stapel gibt es nur im Pool; ein zweiter Pool (etwa ein Länderverbund)
  wäre ein eigener Träger (abi-<verbund>) mit eigenem Stapelmuster.

Grenzfälle: (1) Ein gemeinsames Heft zweier Länder heißt nach der Kopfzeile
(bebb); stellen dieselben Länder später getrennt, laufen be und bb daneben –
so wie 2026 schon. (2) Dieselbe Prüfungsart mit zwei Schulformen desselben
Trägers (msa-bb-os, msa-bb-gym): das Profil bekommt die Schulform; das
heutige msa (nur Oberschule, Entscheidung 18) bliebe msa-bb, bis eine zweite
Schulform hinzukommt, und würde dann msa-bb-os. (3) Ein Träger mit einer
Prüfungsart ohne Niveau (fhr-bb): Zielprüfung = Profil. (4) Kurzkennungen:
solange nur ein Träger die Prüfungsart führt, sind msa, fhr, abi, iqb als
Aliasse eindeutig; die Vollform macht die Namen länger, aber dauerhaft
eindeutig. Wer die Aliasse behält, muss beim ersten zweiten Träger derselben
Prüfungsart das ältere Profil umbenennen – dann mit größerem Bestand als
heute.

## 4 Umbenennungen, die das Schema kostet (Liste; nicht ausgeführt)

Zahlen: Verweise auf den Dateinamen als eigenes Wort in allen Repo-Dateien
außer den drei Quelltexten (Skript vom 17.09.2026), aufgeteilt nach Skripten
(Konstanten wie KAT, TYP, VOKABULAR, ANDERE_KATALOGE, Dateilisten der
Selbstprüfung), Regelwerk (CLAUDE.md, Kern, Profile, Vokabular, konzept.md,
README.md, Prompts) und Prüfungslisten/Befunden. Verweise in den Katalogen
selbst (bemerkung-Felder) sind eigens genannt: sie dürfen nur per
Abgleichlauf geändert werden.

**Variante A – Vollform durchgängig** (Profil = Prüfungsart-Träger, Familie
= Prüfungsart):

| Alt | Neu | Verweise | Skripte | Regelwerk | Sonstiges |
|---|---|---|---|---|---|
| msa.md | msa-bb.md | 7 | – | README 1, fhr.md 2, konzept 2 | abi-aufbau 1, repo-bestand 1 |
| typen.csv | msa-typen.csv | 26 | – | Kern 7, konzept 3, pruefungsprompt.md 6, README 1, abi.md 1 | katalog-basis/kontext je 1, pruefungen 1, blatt-konzept 1, abi-iqb-typen 1, abi-pruefungen 1, repo-bestand 2 |
| katalog-basis.csv | msa-bb-katalog-basis.csv | 7 | – | Kern 2, konzept 1, msa.md 1, pruefungsprompt.md 1, README 1 | repo-bestand 1 |
| katalog-kontext.csv | msa-bb-katalog-kontext.csv | 7 | – | Kern 2, konzept 1, msa.md 1, pruefungsprompt.md 1, README 1 | repo-bestand 1 |
| pruefungen.md | msa-bb-pruefungen.md | 12 | – | Kern 3, konzept 1, msa.md 2, README 1 | vorgaben 2, abi-aufbau 1, repo-bestand 2 |
| vorgaben.md | msa-bb-vorgaben.md | 23 | – | CLAUDE 1, konzept 4, msa.md 2, fhr.md 1, README 1 | pruefungen 6, abi-vorgaben 3, abi-pruefungen 1, fhr-pruefungen 1, repo-bestand 3 |
| fhr.md | fhr-bb.md | 31 | fhr-bau.py 2, fhr-typenbibliothek.py 5 | Kern 1, konzept 2, Vokabular 1, README 1 | **fhr-katalog.csv 12 (bemerkung)**, fhr-pruefungen 2, fhr-typenbibliothek.md 2, blatt-konzept 1, abi-pruefungen 1, repo-bestand 1 |
| fhr-bau.py, fhr-katalog.csv, fhr-pruefungen.md, fhr-typenbibliothek.md/.py | fhr-bb-… (die Typenliste fhr-typen.csv bleibt: Familienname) | 24 | fhr-bau.py 2, fhr-typenbibliothek.py 5 | fhr.md 7 | fhr-typenbibliothek.md 2, repo-bestand 6, abi-pruefungen 2 |
| abi.md | abi-bebb.md | 127 | abi-bau.py 11, iqb-bau.py 2 | CLAUDE 7, Vokabular 11, iqb.md 4, Kern 1, konzept 2, README 1 | abi-pruefungen 58, abi-quellen 8, abi-vorgaben 7, abi-iqb-typen 4, abi-aufbau 2, iqb-pruefungen 2, repo-bestand 7 |
| abi-bau.py | abi-bebb-bau.py | 81 | abgleich.py 5, iqb-bau.py 2 | CLAUDE 4, abi.md 17, Vokabular 2, iqb.md 1, konzept 1 | abi-pruefungen 41, abi-iqb-typen 4, iqb-pruefungen 2, repo-bestand 2 |
| abi-katalog.csv | abi-bebb-katalog.csv | 23 | abgleich.py 2, abi-bau.py 2, iqb-bau.py 4 | CLAUDE 2, abi.md 2, Vokabular 1, konzept 1 | abi-pruefungen 4, iqb-pruefungen 2, abi-iqb-typen 2, repo-bestand 1 |
| abi-pruefungen.md | abi-bebb-pruefungen.md | 60 | abgleich.py 6, abi-bau.py 2 | CLAUDE 7, abi.md 17, Vokabular 3, iqb.md 1, konzept 1 | abi-quellen 8, iqb-pruefungen 7, abi-iqb-typen 3, abi-vorgaben 2, repo-bestand 3 |
| abi-quellen.md | abi-bebb-quellen.md | 31 | – | CLAUDE 3, abi.md 11 | abi-pruefungen 13, abi-aufbau 2, abi-iqb-typen 1, repo-bestand 1 |
| abi-aufbau.md, abi-struktur.json | befund-abi-aufbau-2017-2018.md, befund-abi-struktur-2017-2018.json (nur 2017/2018, seit 12.09. unverändert, von keinem Skript gelesen) | 17 | – | CLAUDE 2, abi.md 5, Vokabular 1 | abi-pruefungen 2, repo-bestand 7 |
| abi-vorgaben.md | bleibt (Familie abi) | 0 | | | |
| iqb.md | abi-iqb.md | 169 | iqb-bau.py 18, abgleich.py 4, abi-bau.py 3, iqb-quellen.py 5 | CLAUDE 5, Vokabular 10, abi.md 5, konzept 3, Kern 1, README 1 | iqb-pruefungen 74, abi-pruefungen 19, abi-iqb-typen 8, abi-vorgaben 4, **iqb-katalog.csv 3 (bemerkung)**, iqb-quellen 3, abi-quellen 2, repo-bestand 1 |
| iqb-bau.py | abi-iqb-bau.py | 95 | abi-bau.py 3, abgleich.py 1 | CLAUDE 6, iqb.md 26, abi.md 3, Vokabular 2, konzept 1 | iqb-pruefungen 32, abi-pruefungen 12, abi-iqb-typen 5, **iqb-katalog.csv 1 (bemerkung)**, iqb-quellen 1, repo-bestand 2 |
| iqb-katalog.csv | abi-iqb-katalog.csv | 33 | abgleich.py 3, abi-bau.py 3, iqb-bau.py 2 | CLAUDE 3, iqb.md 3, abi.md 2, Vokabular 1, konzept 1 | abi-pruefungen 8, iqb-pruefungen 5, abi-iqb-typen 1, repo-bestand 1 |
| iqb-pruefungen.md | abi-iqb-pruefungen.md | 36 | iqb-bau.py 2, abgleich.py 1, abi-bau.py 1 | CLAUDE 5, iqb.md 19, Vokabular 2, abi.md 1 | abi-pruefungen 3, abi-iqb-typen 1, repo-bestand 1 |
| iqb-quellen.md, iqb-quellen.csv, iqb-quellen.py | abi-iqb-quellen.md/.csv/.py | 94 | iqb-bau.py 11, abgleich.py 3, iqb-quellen.py 4 | CLAUDE 6, iqb.md 22, abi.md 3, Kern 1, konzept 1 | iqb-pruefungen 27, abi-pruefungen 2, abi-vorgaben 2, abi-quellen 1, iqb-quellen 6, .gitignore 1, repo-bestand 4 |
| abitur-typen.csv | abi-typen.csv | 46 | abgleich.py 5, abi-bau.py 5, iqb-bau.py 5 | CLAUDE 7, abi.md 4, iqb.md 4, Vokabular 3, konzept 3, Kern 1, README 1 | abi-pruefungen 3, iqb-pruefungen 4, repo-bestand 1 |
| abitur-vokabular.md | abi-vokabular.md | 94 | abi-bau.py 15, iqb-bau.py 12, abgleich.py 1 | CLAUDE 7, abi.md 14, iqb.md 12, konzept 4, Kern 2, README 1 | abi-pruefungen 17, iqb-pruefungen 5, **abi-katalog.csv 2 (bemerkung)**, repo-bestand 2 |
| abgleich.py | abi-abgleich.py | 64 | abi-bau.py 5, iqb-bau.py 7 | CLAUDE 3, abi.md 3, iqb.md 5, Vokabular 3, konzept 5, README 1 | abi-pruefungen 19, iqb-pruefungen 10, abi-iqb-typen 1, repo-bestand 2 |
| abi-iqb-typen.md | befund-abi-iqb-typen.md (oder löschen: Messung vor Lauf 12, Dateien existieren nicht mehr) | 14 | abgleich.py 3 | konzept 1, iqb.md 1, Vokabular 1, README 1 | abi-pruefungen 2, iqb-pruefungen 1, repo-bestand 4 |
| repo-bestand.md | befund-repo-bestand.md | 1 | – | – | abi-pruefungen 1 |
| hefte/, hefte-md/ | hefte/abi-bebb/, hefte-md/abi-bebb/ (lokal; iqb-pdf/ → hefte/abi-iqb/) | 77 | abi-bau.py 1 (KONFIG datei) | CLAUDE 2, abi.md 13, konzept 1 | abi-pruefungen 43, abi-quellen 11, .gitignore 3, repo-bestand 4; dazu die Scratchpad-Werkzeuge (mdcheck, cropsrel) |

Summe Variante A: 31 Dateien im Repo (plus zwei lokale Ordner), rund 1 200
Verweise, davon in Skripten etwa 165 (Konstanten und Docstrings), im
Regelwerk etwa 400, in Prüfungslisten und Befunden etwa 630; 18 Verweise
stehen in Katalogzeilen (fhr-katalog.csv 12, iqb-katalog.csv 4,
abi-katalog.csv 2) und brauchen einen Abgleichlauf mit Feldkorrektur. Dazu
außerhalb des Repos: die Projektanweisungen (Kopien von pruefungsprompt.md
und masterprompt.md, konzept.md § 2), die den Basis-URL und die msa-Dateinamen
tragen, und die Scratchpad-Werkzeuge (selbst.py, mdcheck.py). Die
Skript-Konstanten sind je Skript eine Handvoll Zeilen; die Prüfungslisten
nennen die Namen in Befundtexten, wo ein historischer Name („abi-bau.py
v0.4") auch stehen bleiben könnte – dann sind es nur die Regelwerk- und
Skriptstellen, rund 570.

**Variante B – Aliasse behalten, nur das Präfixlose beheben:** msa bekommt
wie die anderen Profile ein Präfix (typen.csv → msa-typen.csv,
katalog-basis.csv → msa-katalog-basis.csv, katalog-kontext.csv →
msa-katalog-kontext.csv, pruefungen.md → msa-pruefungen.md, vorgaben.md →
msa-vorgaben.md; 75 Verweise, davon Kern 14, pruefungsprompt.md 8, keine
Skripte, keine Katalogzeilen), abgleich.py → abitur-abgleich.py (64 Verweise,
Familienname wie abitur-typen.csv), abi-iqb-typen.md und repo-bestand.md nach
befund-…; alles andere bleibt. Kurzkennungen msa, fhr, abi, iqb sind dann
Aliasse mit der Gleichsetzung in konzept.md; neue Profile tragen die
Vollform. Kosten rund 155 Verweise; Rest: die Mehrdeutigkeit aus § 3 (4).

**Variante C – nichts umbenennen:** Schema gilt nur für Neues (Geltungsdateien,
neue Profile). Kosten 0; Preis: drei Muster nebeneinander (§ 1).

## 5 Beobachtungen am Rand (keine Umbenennung, aber Entscheidung des Lehrers)

- Die Geltungstabelle schreibt für Brandenburg grundlegend `bb-gk`, das
  Kürzel des Profils für Brandenburg erhöht ist `ea` (nicht `lk`): das
  Niveau-Kürzel folgt einmal dem Berliner Wort (Grundkurs), einmal dem
  Brandenburger (erhöhtes Anforderungsniveau). Das Schema lässt das zu
  (Niveau = Kürzel des Trägers), eindeutig ist es; einheitlich wäre
  `bb-ga`/`bb-ea` – das hieße Umbenennen einer Spalte in der Geltung, in
  abi-bau.py (ziele_von) und in allen Kennzahlenzeilen.
- `abi-vorgaben.md` ist unter dem Profilpräfix abgelegt, gilt aber für abi
  und iqb; im Schema ist es die Familiendatei (`<familie>-vorgaben.md`) und
  behielte in Variante A zufällig seinen Namen.
- Der msa-Katalog liegt in zwei Dateien (Entscheidung 14), alle anderen in
  einer mit Feld `block` (abi.md § 2 begründet das). Das Schema trägt beides
  (`-katalog-<block>.csv`), entscheidet den Modellunterschied aber nicht.
- fhr und msa haben keine Geltungsdatei: fhr bindet seine Themen über eine
  Markierung (27)/(28) an Prüfungsjahrgänge, nicht an Land oder Schulform,
  und kein Skript liest sie; msa hat gar keine Geltung. Teil 2 sagt, warum
  beide nicht umgebaut werden.
