# mathe-nachhilfe

Prüfungskataloge und Themenkatalog für Mathematik-Nachhilfe, Berlin/Brandenburg.
Vergangene Prüfungen werden Zeile für Zeile in Prüfungskataloge geschrieben, je
Prüfungsart ein Profil. Der Themenkatalog beschreibt den Stoff, aus dem Blätter
gebaut werden. Die Prompts und die LaTeX-Vorlage, die daraus Blätter machen, liegen
im eigenen Repo `blattbau` (siehe unten).

Diese Datei ist die einzige Landkarte. Wer eine Datei anlegt, umbenennt oder
entfernt, trägt das hier ein – sonst nirgends.

Umbau 19.09.2026: Ordner statt Präfixe. Dateinamen sind unverändert geblieben, damit
Querverweise in Texten und Skripten weiter stimmen; nur der Ort hat sich geändert.
Die Bau-Skripte laufen im Ordner ihres Profils (`cd abitur && python abi-bau.py`).

## Wo fange ich an

- `uebergabe.md` – Stand und nächster Arbeitsschritt der Prompt-Werkstatt; ein neuer Chat liest sie zuerst. Wird bei jedem Umzug ersetzt.
- `CLAUDE.md` – wenn im Repo erfasst wird: Ablauf je Heft, Arbeitsregeln, Commit-Regel.
- `katalog-prompt.md` – der Kern: Zeilenregel, die 37 Felder, Vokabular, Prüfung, Abgleichlauf. Gilt für alle Profile.
- `konzept.md` – warum etwas so ist: Bausteine (§ 2), Themenkatalog (§ 3), Entscheidungen mit Kippbedingung (§ 4), Offenes (§ 6), Jahresroutine (§ 7), neue Prüfung aufnehmen (§ 8), Änderungen (§ 10).
- `blatt-konzept.md` – die Heft-Phase: Sprossen, Decke, Merkmalsfrage (§ 7). Bei Widerspruch zum Prüfungsblatt-Prompt gilt es. Liegt hier, weil beide Repos es brauchen.
- `faellig.md` – am Anfang eines Auftrags: Handlungen mit Termin oder Auslöser und bei wem sie liegen.
- `themen.csv` – Themenkonkordanz: kanonisches Thema je Katalogthema, alle vier Profile; nach jeder Katalogänderung `python werkzeuge/themen-pruef.py`.

## msa/ – P10 Mathematik, Brandenburg, Oberschule/Gesamtschule, Niveau FOR

- `msa.md` – vor dem Erfassen: Kürzel, Leitideen, Themenliste, Besonderheiten; bei Widerspruch zum Kern gilt es.
- `msa-pruefungen.md` – welches Heft als Nächstes dran ist, wo die Hefte liegen, was je Heft geschah.
- `msa-quellen.md` – Jahresseite, Serverdateien je papier-Kürzel, Heftordner `hefte/msa/` (lokal), Dateien ohne Katalogeintrag.
- `msa-typen.csv` – Typen suchen, vergleichen, anlegen; wächst nur über das Bau-Skript.
- `msa-katalog-basis.csv`, `msa-katalog-kontext.csv` – der Katalog (Basisaufgaben, Kontextaufgaben); nie von Hand ändern.
- `msa-bau.py` – Heft erfassen oder Bestand prüfen (leeres ZEILEN = Selbstprüfung).
- `msa-vorgaben.md` – jährlicher Vorgabencheck, Formatwechsel 2028.

## fhr/ – Fachhochschulreife Mathematik, Brandenburg

- `fhr.md` – vor dem Erfassen: Kürzel, Themenliste mit Schwerpunktmarkierung, Regel Punkt-Schwerpunkt.
- `fhr-pruefungen.md` – Heftliste, Quelle, Umfang, Änderungslog; alle sechzehn Hefte 2019–2026 erfasst.
- `fhr-quellen.md` – Übersichtsseite, Serverdateien, Heftordner `hefte/fhr/` (lokal).
- `fhr-typen.csv` – Typen suchen oder anlegen.
- `fhr-katalog.csv` – der Katalog; nie von Hand ändern.
- `fhr-bau.py` – Heft erfassen oder Bestand prüfen.
- `fhr-vorgaben.md` – jährlicher Vorgabencheck.
- `fhr-typenbibliothek.py`, `fhr-typenbibliothek.md` – Skript nach jeder Katalogänderung ausführen; die Bibliothek öffnen, wenn ein Blatt zu einem fhr-Typ geplant wird.

## abitur/ – Zentralabitur Berlin/Brandenburg (abi) und IQB-Aufgabenpool (iqb)

Beide Profile in einem Ordner, weil sie sich gegenseitig lesen (Dubletten, gemeinsame
Typenliste, Abgleich).

Profil abi:
- `abi.md` – vor dem Erfassen: Kürzel je Jahrgang, Zielprüfungen, Dubletten und Vormerkungen, Prüfungsgeschichte (§ 10–11); bei Widerspruch zum Kern gilt es.
- `abi-quellen.md` – amtliche Dateien 2011–2018 (44 Dateien, Serverpfade je Jahrgang), Verlagsbände ab 2019, Heftordner `hefte/abi/` (lokal), Markdown-Korpus `hefte-md/` (lokal).
- `abi-pruefungen.md` – nächstes Heft, Kennzahlen, Befunde je Heft und Lauf, Änderungslog.
- `abi-katalog.csv` – der Katalog (Feld block trennt die Teile); nie von Hand ändern.
- `abi-bau.py` – Heft erfassen oder Bestand prüfen; enthält die Zeilen des zuletzt erfassten Hefts.
- `abi-vorgaben.md` – jährlicher Vorgabencheck (Prüfungsschwerpunkte beider Länder; gilt auch für iqb).
- `abi-aufbau.md`, `abi-struktur.json` – nur für 2017/2018: Wahlstruktur, BE-Vektoren, Zwillingsnachweis.
- `abi-be-gk-geltung.md`, `abi-be-lk-geltung.md`, `abi-bb-gk-geltung.md`, `abi-bb-ea-geltung.md` – je Zielprüfung Thema ja/nein, ausgeschlossene Aufgabenformen, Rechnerfassung.

Profil iqb:
- `iqb.md` – vor dem Erfassen eines Stapels: Kennung und id, Stapel als Laufeinheit, Schätzung vor dem Erwartungshorizont, Schwellen, Abbruchkriterium.
- `iqb-quellen.md`, `iqb-quellen.csv`, `iqb-quellen.py` – Pooljahrgänge, Kennungen deuten, Dateiliste erneuern (Cache `iqb-pdf/`, lokal).
- `iqb-pruefungen.md` – nächster Stapel, Reserven, Kennzahlen, Befunde, Änderungslog.
- `iqb-katalog.csv` – der Katalog; nie von Hand ändern.
- `iqb-bau.py` – Stapel erfassen oder Bestand prüfen.

Gemeinsam:
- `abitur-vokabular.md` – Themen, Gegenstandsklassen, Regel Zeilenthema = Typthema; Änderungen an Themen und Klassen nur hier.
- `abitur-typen.csv` – gemeinsame Typenliste; Umbenennen und Zusammenziehen nur über das Abgleich-Skript.
- `abitur-abgleich.py` – nach jedem Heft und Stapel (`python abitur-abgleich.py N`); jeder Lauf bleibt als Code stehen.

## katalog/ – Themenkatalog

41 Einträge, Stand 2026-09-20: 29 Sek-I-Einträge (Stand 2026-09-11j, gegengelesen
bis auf den Punkt [FS]) und zwölf Sek-II-Einträge in der Eintragsform nach `konzept.md`
§ 4 Entscheidung 36 (alle Entwurf, nicht gegengelesen): die drei Formproben
`kurvenuntersuchung.md` (Pilot, Analysis, fhr/abi/iqb), `binomialverteilung.md`
(Stochastik, abi/iqb) und `ebenen.md` (Analytische Geometrie, abi/iqb), die fünf
Einträge des Serienbaus Bündel 1 „Ableitung Grundlagen“ (149 Katalogzeilen):
`ableitung-und-aenderungsrate.md`, `ableitungsregeln.md`,
`grenzwerte-und-verhalten-im-unendlichen.md`, `gleichungen-loesen.md` und
`umkehrfunktion.md` (Kurzform), sowie die drei Einträge des Bündels 2 „Ableitung
Anwendung“ (171 Katalogzeilen): `tangente-normale-schnittwinkel.md`,
`extremalprobleme.md` und `ableitungsgraph-und-funktionsgraph.md` – Letzterer der
erste Verweiseintrag (Eintragsart nach dem E36-Zusatz vom 19.09.2026: eigener Kopf,
eigene Verortung und Prüfungsform, die didaktischen Abschnitte je eine Verweiszeile
auf den tragenden Eintrag, hier `kurvenuntersuchung.md` Einheit 4), sowie der eine
Eintrag des Bündels 3 (200 Katalogzeilen, das größte Einzelthema der Serie):
`funktionsklassen-und-eigenschaften.md`. Zweck und
Arbeitsteilung mit den
Prüfungskatalogen: `konzept.md` § 3. Bis zum Umbau lag der Themenkatalog nur in Lieferzips
der Prompt-Werkstatt, nicht im Repo.

- je Thema eine Datei (`bruchrechnung.md`, `prozentrechnung.md` …): Lerneinheiten, Voraussetzungen, Grundvorstellung, Sprossen, Merkkasten, Fehlerquellen, Zielmarke; Sek-II-Einträge mit Prüfungsform je Profil (fhr / abi / iqb) aus der Rohdatei `rohdaten/<kanonisch>.md`, Zahl der Lerneinheiten frei (funktionsklassen-und-eigenschaften sechs, kurvenuntersuchung, binomialverteilung und tangente-normale-schnittwinkel fünf, ebenen, ableitung-und-aenderungsrate und gleichungen-loesen vier, ableitungsregeln, grenzwerte-und-verhalten-im-unendlichen und extremalprobleme drei, umkehrfunktion zwei; der Verweiseintrag ableitungsgraph-und-funktionsgraph ohne eigene Einheiten). Jeder Merkkasten eines Sek-II-Eintrags trägt seit dem 19.09.2026 eine Zeile „Auswendig (Teil A):" (Entscheidung 36, Kastenform), die nennt, welche Kastenteile laut Anlage ohne Hilfsmittel ohne Rechner und Formelsammlung sitzen müssen.
- `index.md` – Tabelle je Sek-I-Thema (Leitidee, Stufe, Klasse, P10, Status) mit Gegenlese-Verlauf und CSV-Themen-Zuordnung für Kennzahl 6 (`_pruef_struktur.py`); seit dem Sek-II-Piloten auch eine Sek-II-Tabelle (Profile, Zeilen/Typen aus `themen.csv`).
- `_quellen.md` – Zweck, Aufbau, Notation je Thema, Quellenregister mit Kürzeln (seit 19.09.2026 auch [GOST], [FOS], [BASICS], [COSH], [FS-IQB], [IQB-VER], [IQB-STR]).
- `_quellenprotokoll.md` – was aus welcher Quelle gelesen wurde.
- `_formelsammlung.md` – Prüfliste [FS]; steht zur Streichung (Abschnittsverweis nicht haltbar, Adresse der Formelsammlung nicht feststellbar).
- `_pruef_katalog.py`, `_pruef_struktur.py` – Prüfskripte (Sek-II-Modus: Zählzeile und Profillisten gegen `themen.csv`, Einheitsnummern E1–E9); `_suche_quelle.py` – Suche in den zweispaltigen Quellentexten.

Kastenform entschieden (19.09.2026, Entscheidung 36 „Kastenform"): Arbeitskästen je Lerneinheit mit Auswendig-Zeile; der themenweite Stundenanker ist Kompositionsregel des Unterrichtsblatt-Prompts (Posten in `faellig.md` § 2). Offen: [FS]-Abschnittsverweis am PDF, Mechanik-Punkte (A4 breit/eng, Prüflisten, Prüflistenzeilen 10 und 11). Kein Blatt ist bisher aus einem Eintrag gebaut worden.

## rohdaten/ – Rohdateien je Thema

Lesestoff für Katalogeinträge: je kanonischem Thema aus `themen.csv` eine Datei
`<kanonisch>.md` mit Teil A Typenprofil (jeder Haupttyp mit Zeilenzahl, Profilen, Jahren
und Definition aus der Typenliste, dazu die Nebentypen) und Teil B Zeilenliste (eine Zeile
je Katalogzeile, nach Profil, Typ, Jahr, id). Abgeleitet aus `themen.csv` und den fünf
Katalogen, nie von Hand ändern; neu bauen mit `python werkzeuge/rohdatei-bau.py [thema ...]`.
66 Dateien – alle kanonischen Themen mit Katalogzeilen; die 7 ohne Zeilen haben keine Datei.

## quellen/ – Quellentexte

Textfassungen der Quellen, die alle Katalogeinträge brauchen, damit sie nicht in jedem
Chat neu geholt werden. Herkunft, Stand, Lizenz und Suchfallstricke in `quellen/quellen.md`.

- `quelle-rlp-teil-c-mathematik-2023.txt` – Rahmenlehrplan 1–10, Teil C Mathematik, gültig ab 2025/26.
- `quelle-lisum-planungshilfen-7bis10.txt` – LISUM-Planungshilfen 7–10, Gesamtdatei 2024, CC BY-SA 4.0.
- `quelle-klett-fahrplan-ls-aa-berlin-2024.txt` – Lambacher Schweizer, Fahrplan Berlin 2024.
- `quelle-rlp-gost-bb-2022-mathematik.txt` – Rahmenlehrplan GOST Brandenburg, Teil C Mathematik, gültig ab 2022/23.
- `quelle-rlp-gost-be-2022-mathematik.txt` – Rahmenlehrplan GOST Berlin, Teil C Mathematik, gültig ab 2014.
- `quelle-rlp-gost-2022-mathematik-anlage-ohimi.txt` – Anlage zum RLP GOST: Inhalte ohne Hilfsmittel, Grundlage für Prüfungsteil A.
- `quelle-rlp-fos-bb-2019-mathematik.txt` – Rahmenlehrplan Fachoberschule Mathematik, Brandenburg, gültig ab 2019.
- `quelle-iqb-formelsammlung-2024-mathematik.txt` – IQB-Formelsammlung, nur Teil 1 Mathematik, Stand 2024, © IQB.
- `quelle-iqb-operatoren-2019.txt` – IQB, Grundstock von Operatoren, Stand 2019, © IQB.
- `quelle-iqb-vereinbarungen-2022.txt` – IQB, Inhaltliche Vereinbarungen zur Gestaltung der Aufgaben, Stand 2022, © IQB.
- `quelle-iqb-struktur-2024.txt` – IQB, Beschreibung der Struktur der Aufgaben, Stand 2024, © IQB.

Das LISUM wurde zum 31.12.2024 aufgelöst; die Texte werden nicht mehr fortgeschrieben
und ihre Adressen sind nicht gesichert. Deshalb liegen sie hier.

## werkzeuge/ – Bände und Korpus

Lesen die Kataloge, ändern nichts. Ausgabeordner `baende/` und `korpus/` sind lokal (`.gitignore`).

- `band-anleitung.md`, `band-bau.py`, `fhr-band-struktur.py`, `fhr-band.csv` – Sammelbände aus den Originalseiten.
- `korpus-bau.py`, `korpus-protokoll.md` – Markdown-Korpus und OCR der Prüfungshefte.
- `themen-inventar.py`, `themen-inventar.md` – Themennamen aller vier Prüfungskataloge gezählt; Vorstufe der Themenkonkordanz.
- `themen-pruef.py` – prüft `themen.csv` gegen Kataloge, `katalog/` und Vokabular; nach jeder Katalogänderung ausführen, Rückgabewert 0 nur bei bestandener Prüfung.
- `rohdatei-bau.py` – schreibt je kanonischem Thema `rohdaten/<kanonisch>.md` aus `themen.csv` und den Katalogen; ohne Argument alle Themen mit Katalogzeilen.

## archiv/ – eingefroren

Datierte Befunde und Werkstattzettel. Beschreiben den Stand ihres Datums, werden nicht
fortgeschrieben, kein Chat muss sie lesen. `namensschema.md` liegt hier, weil der Umbau
auf Ordner es überholt hat.

## Nicht im Repo (lokal, `.gitignore`)

`hefte/` gescannte Prüfungshefte (urheberrechtlich geschützt), `hefte-md/` Markdown-Korpus
der Verlagsbände, `korpus/` maschineller Korpus, `baende/` Sammelbände, `iqb-pdf/` Cache.

## Repo blattbau – anderes Projekt

`unterrichtsblatt.md`, `pruefungsblatt.md`, `mathblatt.sty`, `Anleitung_mathblatt.md`,
`CHANGELOG.md` und die Testauswertungen liegen seit dem Umbau im eigenen Repo. Der
Prüfungsblatt-Prompt lädt die Kataloge per Abruf aus diesem Repo; nach dem Umbau müssen die
Pfade dort auf die Profilordner zeigen (`msa/msa-typen.csv` statt `msa-typen.csv`).
