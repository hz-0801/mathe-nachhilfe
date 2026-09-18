# mathe-nachhilfe

Im Repo liegen zwei Arbeiten nebeneinander: die **Erfassung** – vergangene Prüfungen werden Zeile für Zeile in Prüfungskataloge geschrieben, je Prüfung ein Profil – und der **Blattbau** – Prompts und LaTeX-Vorlage, die daraus (oder ohne Katalog) Arbeitsblätter bauen. Wer nur eine davon macht, braucht die andere Hälfte nicht. Alle Dateien liegen flach in der Wurzel; die Ordnung kommt aus den Namen: Präfix je Profil (`msa-`, `fhr-`, `abi-`, `iqb-`), `abitur-` für das, was abi und iqb teilen, `befund-` für Eingefrorenes (Regeln in `namensschema.md`). Die Ordner `hefte/`, `hefte-md/`, `baende/` und `iqb-pdf/` liegen daneben, nicht im Repo (`.gitignore`): Verlagsmaterial, Sammelbände und Cache.

## Wo fange ich an

- `CLAUDE.md` – öffnen, wenn im Repo erfasst wird: Werkzeuge auf dem Rechner, Ablauf je Heft und Stapel, Arbeitsregeln (Selbstprüfung, Rerun, Commit).
- `konzept.md` – öffnen, wenn man wissen will, warum etwas so ist: Entscheidungen mit Zahl und Kippbedingung (§ 4), was offen ist und worauf es wartet (§ 6), die Jahresroutine (§ 7), wie eine neue Prüfung aufgenommen wird (§ 8).
- `faellig.md` – öffnen am Anfang eines Auftrags und wenn ein Fachbrief, ein Jahrgang oder ein Band erscheint: Handlungen mit Termin oder Auslöser und bei wem sie liegen (jährlich, einmalig, beim Lehrer, erledigt). Angelegt am 18.09.2026, weil Termine und Auslöser bis dahin über Prüfungslisten, Vorgaben-Dateien und Berichte verstreut waren.

## Profil msa (P10 Mathematik, Brandenburg, Oberschule/Gesamtschule, Niveau FOR)

- `msa.md` – öffnen, bevor ein P10-Heft erfasst wird: Kürzel, Leitideen, Themenliste, Besonderheiten; bei Widerspruch zum Kern gilt es.
- `msa-pruefungen.md` – öffnen, um zu sehen, welches Heft als Nächstes dran ist, wo die Hefte liegen und was je Heft geschah.
- `msa-quellen.md` – öffnen, wenn ein Heft geholt wird oder eine Datei zuzuordnen ist: Jahresseite, Serverdateien je papier-Kürzel, Heftordner `hefte/msa/` (lokal) mit Erfassungsstand, Dateien ohne Katalogeintrag.
- `msa-typen.csv` – öffnen, wenn ein Typ gesucht, verglichen oder neu angelegt wird; wächst nur über das Bau-Skript.
- `msa-katalog-basis.csv`, `msa-katalog-kontext.csv` – der Katalog in zwei Dateien (Basisaufgaben, Kontextaufgaben); öffnen zum Lesen, nie von Hand ändern.
- `msa-bau.py` – ausführen, um ein Heft zu erfassen oder den Bestand zu prüfen (leeres ZEILEN = Selbstprüfung); Feldkorrekturen an der Typenliste laufen hier.
- `msa-vorgaben.md` – öffnen beim jährlichen Vorgabencheck und wenn ein Formatwechsel (2028) ansteht.

## Profil fhr (Fachhochschulreife Mathematik, Brandenburg)

- `fhr.md` – öffnen, bevor ein FHR-Heft erfasst wird: Kürzel, Themenliste mit Schwerpunktmarkierung, Regel Punkt-Schwerpunkt, Besonderheiten.
- `fhr-pruefungen.md` – öffnen für Heftliste, Quelle, Umfang und Änderungslog; alle sechzehn Hefte 2019–2026 sind erfasst.
- `fhr-quellen.md` – öffnen, wenn ein Heft geholt wird oder eine Datei zuzuordnen ist: Übersichtsseite, Serverdateien je papier-Kürzel, Heftordner `hefte/fhr/` (lokal) mit Erfassungsstand, Dateien ohne Katalogeintrag.
- `fhr-typen.csv` – öffnen, wenn ein Typ gesucht oder neu angelegt wird.
- `fhr-katalog.csv` – der Katalog; öffnen zum Lesen, nie von Hand ändern.
- `fhr-bau.py` – ausführen, um ein Heft zu erfassen oder den Bestand zu prüfen (leeres ZEILEN = Selbstprüfung).
- `fhr-vorgaben.md` – öffnen beim jährlichen Vorgabencheck; der erste Check löst den Vorbehalt im Kopf auf.
- `fhr-typenbibliothek.py`, `fhr-typenbibliothek.md` – das Skript nach jeder Katalogänderung ausführen; die erzeugte Bibliothek öffnen, wenn ein Blatt zu einem fhr-Typ geplant wird.

## Profil abi (Zentralabitur Mathematik, Berlin/Brandenburg)

- `abi.md` – öffnen, bevor ein Landesheft erfasst wird: Kürzel je Jahrgang, Zielprüfungen, Dubletten und Vormerkungen, Prüfungsgeschichte und Struktur (§ 10–11); bei Widerspruch zum Kern gilt es.
- `abi-quellen.md` – öffnen, wenn ein Heft beschafft oder geholt wird: amtliche Dateien 2017/2018, Verlagsbände ab 2019, Heftordner `hefte/abi/` (lokal), Markdown-Korpus `hefte-md/` (lokal).
- `abi-pruefungen.md` – öffnen, um zu sehen, welches Heft als Nächstes dran ist, die Kennzahlen je Heft, die Befunde je Heft und Lauf, das Änderungslog.
- `abi-katalog.csv` – der Katalog (eine Datei, Feld block trennt die Teile); öffnen zum Lesen, nie von Hand ändern.
- `abi-bau.py` – ausführen, um ein Heft zu erfassen oder den Bestand zu prüfen (leeres ZEILEN = Selbstprüfung); enthält die Zeilen des zuletzt erfassten Hefts.
- `abi-vorgaben.md` – öffnen beim jährlichen Vorgabencheck (Prüfungsschwerpunkte beider Länder; gilt auch für iqb, soweit es den Pool betrifft).
- `abi-aufbau.md`, `abi-struktur.json` – öffnen nur für die Jahrgänge 2017/2018: Wahlstruktur, BE-Vektoren, Zwillingsnachweis der Länder.

## Profil iqb (Gemeinsame Abituraufgabenpools der Länder, IQB)

- `iqb.md` – öffnen, bevor ein Stapel erfasst wird: Kennung und id, Stapel als Laufeinheit, Schätzung vor dem Erwartungshorizont, Schwellen, Abbruchkriterium; bei Widerspruch zum Kern gilt es.
- `iqb-quellen.md`, `iqb-quellen.csv`, `iqb-quellen.py` – öffnen, wenn ein Pooljahrgang neu ist oder eine Kennung zu deuten ist; das Skript ausführen, um die Dateiliste zu erneuern (Cache `iqb-pdf/`, lokal).
- `iqb-pruefungen.md` – öffnen, um zu sehen, welcher Stapel als Nächstes dran ist, welche Reserve sind, die Kennzahlen und Befunde je Stapel, das Änderungslog.
- `iqb-katalog.csv` – der Katalog; öffnen zum Lesen, nie von Hand ändern.
- `iqb-bau.py` – ausführen, um einen Stapel zu erfassen oder den Bestand zu prüfen (leeres ZEILEN = Selbstprüfung); enthält die Zeilen des zuletzt erfassten Stapels.

## Gemeinsam für abi und iqb

- `abitur-vokabular.md` – öffnen, wenn ein Thema, eine Gegenstandsklasse oder die Regel Zeilenthema = Typthema gebraucht wird; Änderungen an Themen und Klassen nur hier.
- `abitur-typen.csv` – die gemeinsame Typenliste; öffnen, wenn ein Typ gesucht oder neu angelegt wird; Umbenennen und Zusammenziehen nur über das Abgleich-Skript.
- `abi-be-gk-geltung.md`, `abi-be-lk-geltung.md`, `abi-bb-gk-geltung.md`, `abi-bb-ea-geltung.md` – öffnen beim Vorgabencheck und wenn eine Zeile außerhalb der Geltung liegt: je Zielprüfung Thema ja/nein, ausgeschlossene Aufgabenformen, Rechnerfassung.
- `abitur-abgleich.py` – ausführen nach jedem Heft und Stapel (`python abitur-abgleich.py N`): stellt Typenliste und beide Kataloge zugleich um; jeder Lauf bleibt als Code stehen.

## Gilt für alle Profile

- `katalog-prompt.md` – der Kern: öffnen, wenn eine Frage zur Methode nicht im Profil beantwortet ist (Zeilenregel, 37 Felder, Vokabular, Prüfung, Abgleichlauf).
- `namensschema.md` – öffnen, wenn eine Datei, ein Profil oder eine Kennung neu benannt wird.

## Blattbau – anderes Projekt

Baut Arbeitsblätter, liest den Katalog nur als Quelle und ändert ihn nie: `masterprompt.md` (ohne Katalog), `pruefungsprompt.md` (mit Katalog, heute Profil msa), `mathblatt.sty` und `Anleitung_mathblatt.md` (Vorlage), `blatt-konzept.md`, `CHANGELOG.md`. Die Projektanweisungen in den Claude-Projekten sind Kopien der beiden Prompts.

## Sammelbände – anderes Projekt

Baut je Prüfungsart einen PDF-Band aus den Originalseiten der Hefte mit Inhalt, Register aus dem Katalog und Bandseitenzahlen; liest Katalog und Hefte nur als Quelle und ändert sie nie. Bisher fhr; Ausgabe unter `baende/` (lokal, nicht im Repo). Familienname `band-` (namensschema.md).

- `band-anleitung.md` – öffnen, bevor ein Band gebaut oder ein Heft angehängt wird: Laufumgebung, Schritte, Spalten der Strukturliste, Seitenreserve, Regel „erst erfassen, dann bauen".
- `band-bau.py` – ausführen (`python band-bau.py fhr`), um den Band und die Einzelhefte neu zu bauen; öffnen, wenn Vorspann, Aufdruck oder Titeltexte eines Profils zu ändern sind (KONFIG).
- `fhr-band-struktur.py` – ausführen vor jedem Bau, damit die Strukturliste zum Katalog und zu den Heften passt; öffnen, wenn ein Profil einen eigenen Erzeuger braucht (Muster).
- `fhr-band.csv` – die Strukturliste (Jahrgänge, Hefte, Abschnitte mit Heftseiten); öffnen, um Reihenfolge, Titel oder Hinweiszeile eines Hefts zu ändern – Abschnittszeilen nie von Hand.

## Eingefroren oder nicht mehr in Arbeit

- `befund-*.md` – datierte Befunde (`befund-repo-bestand.md`, `befund-typenlisten.md`, `befund-lesbarkeit.md`, `befund-abi-iqb-typen.md`, Stichtagsbefund `befund-stichtag-2026-09-17.md`); sie beschreiben den Stand ihres Datums und werden nicht fortgeschrieben.
- Werkstattdateien des Blattbaus (`Testauswertung_*`, `Bewertung_*`, `uebergabe.md`, `archiv-hinweis.md`) – Zettel und Auswertungsvorschriften aus dem Werkstatt-Prozess vom September 2026; die Protokoll-Archive selbst liegen nicht hier.
- Quellentexte des Themenkatalogs (`quellen.md`, `quelle-*.txt`) – für den Themenkatalog aus konzept.md § 3, der nicht begonnen ist.

---

Regel: Die Landkarte – welche Datei wofür da ist – steht in dieser Datei und nur hier. `konzept.md` § 2 behält die Begründung der Bausteine, `befund-`Dateien bleiben eingefroren.

**Landkarte pflegen.** Wer eine Datei anlegt, umbenennt oder aus dem Repo nimmt, trägt das im selben Commit in die Landkarte ein: README im Block des Profils oder Projekts mit einem Satz zum Anlass des Öffnens; CLAUDE.md § 1, wenn die Erfassung die Datei liest oder schreibt; konzept.md § 2 mit Grund, wenn sie ein neuer Baustein ist; namensschema.md, wenn ein neues Muster oder ein neuer Familienname entsteht. Ein Commit, der eine Datei hinzufügt, ohne die Landkarte zu ändern, ist unvollständig – wie ein Heft ohne Zeile in der Prüfungsliste.
