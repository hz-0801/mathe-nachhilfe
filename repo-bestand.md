# Bestandsaufnahme des Repos – Zuordnung der Dateien

Stand 17.09.2026 (Auftrag C „Eichschwelle setzen, Markdown-Korpus
fertigstellen, offene Posten schließen, Katalog gegen Stark prüfen, Repo
sichten", Teil 5). Nur Liste und Bewertung; nichts verschoben, umbenannt oder
gelöscht. Über Ordner, Umbenennungen und eine Trennung der beiden Projekte
entscheidet der Lehrer anhand dieser Liste. Diese Datei ist selbst ein
Kandidat zum Löschen, sobald die Entscheidung gefallen ist.

Grundlage: `git ls-files` (53 Dateien, 6,2 MB), Kopfzeilen und
Versionsvermerke, `git log` je Datei (Anlage, letzte Änderung, Zahl der
Commits). Werkzeuge außerhalb des Repos (Scratchpad) stehen in § 3.

Zuordnung: **K** Katalog-Projekt (Erfassung der Prüfungen in die Kataloge,
Profile msa, fhr, abi, iqb), **B** Blattbau-Projekt (Masterprompt,
Prüfungsprompt, LaTeX-Vorlage, Blatt-Konzept, Testauswertungen), **K+B**
beide, **X** nicht mehr in Gebrauch.

## 1 Dateien

| Datei | Projekt | Zweck (eine Zeile) | Stand | Angelegt | Letzte Änderung | Commits |
|---|---|---|---|---|---|---|
| `.gitattributes` | K+B | `* -text`: Git normalisiert keine Zeilenenden (LF der Skripte und CSV bleibt) | 1 Zeile | 13.09. | 13.09. | 1 |
| `.gitignore` | K | Schließt iqb-pdf/, hefte/, hefte-md/, __pycache__/ aus | aktuell | 13.09. | 17.09. | 3 |
| `README.md` | K+B | Landkarte des Repos (Dateien und Rollen) | veraltet (nennt abi als 2017/2018 mit Scans ab 2019, sagt Testauswertungen lägen nicht hier) | 05.09. | 16.09. | 8 |
| `konzept.md` | K (§ 3 Themenkatalog K+B) | Gesamtkonzept des Katalogs, Entscheidungen 1–26, Verworfenes; § 2 zweite Dateiliste | Stand 12.09., Dateiliste teils veraltet (pdf/ „noch nicht angelegt", msa-Typenbibliothek) | 05.09. | 16.09. | 15 |
| `CLAUDE.md` | K | Arbeitsanweisung für die Erfassung abi und iqb | aktuell in der Sache; § 1 nennt abi.md v0.18 und Kern v0.6 (jetzt v0.21, v0.7) | 13.09. | 17.09. | 16 |
| `CHANGELOG.md` | B | Änderungshistorie der Prompts und der Vorlage (bis v3.34 / v0.14 / 07d) | letzter Eintrag 08.09. | 07.09. | 08.09. | 8 |
| `katalog-prompt.md` | K | Kern der Erfassungsmethode (alle Profile) | v0.7, 17.09. | 05.09. | 17.09. | 8 |
| `msa.md` | K (Profil msa) | Profil P10 Brandenburg (FOR/EBR) | v0.3, gilt mit Kern v0.3; seit 07.09. unverändert | 05.09. | 07.09. | 3 |
| `typen.csv` | K (msa) | Typenliste msa, 185 Typen | 05.09., ruhend | 05.09. | 05.09. | 17 |
| `katalog-basis.csv` | K (msa) | Katalog msa, Basisaufgaben, 126 Zeilen (Zwei-Dateien-Modell) | 05.09., ruhend | 05.09. | 05.09. | 17 |
| `katalog-kontext.csv` | K (msa) | Katalog msa, Kontextaufgaben, 267 Zeilen | 05.09., ruhend | 05.09. | 05.09. | 17 |
| `pruefungen.md` | K (msa) | Heftliste msa mit Erfassungsstatus (2014–2025, 2026 FOR) | 05.09., ruhend | 05.09. | 05.09. | 18 |
| `vorgaben.md` | K (msa) | Amtliche Vorgaben P10 (Fachbriefe) mit Jahrescheck | 05.09., ruhend | 05.09. | 05.09. | 2 |
| `fhr.md` | K (Profil fhr) | Profil Fachhochschulreife Brandenburg | v1.6, 13.09.; gilt mit Kern v0.3 | 12.09. | 13.09. | 10 |
| `fhr-bau.py` | K (fhr) | Bau-Skript fhr (Gerüst je Heft, enthält die ZEILEN des letzten Hefts) | v0.2, 12.09.; Katalog vollständig, Skript ruhend | 12.09. | 12.09. | 9 |
| `fhr-katalog.csv` | K (fhr) | Katalog fhr, 253 Zeilen, 16 Hefte 2019–2026 (vollständig erfasst) | 12.09., abgeschlossen | 12.09. | 12.09. | 10 |
| `fhr-typen.csv` | K (fhr) | Typenliste fhr, 135 Typen | 12.09. | 12.09. | 12.09. | 10 |
| `fhr-pruefungen.md` | K (fhr) | Heftliste fhr mit Befunden | 12.09. | 12.09. | 12.09. | 10 |
| `fhr-typenbibliothek.py` | K+B (fhr) | Erzeugt die Typenbibliothek aus dem Katalog (Vorstufe für den Blattbau, blatt-konzept § 3) | v0.1, 12.09. | 12.09. | 12.09. | 1 |
| `fhr-typenbibliothek.md` | K+B (fhr) | Abgeleitete Typenbibliothek fhr (nie von Hand geändert) | erzeugt 12.09., zum Katalogstand passend | 12.09. | 12.09. | 1 |
| `abi.md` | K (Profil abi) | Profil Zentralabitur BE/BB: Prüfung, Quellen, Aufbau, Kürzel, Besonderheiten, Offenes, Prüfungsgeschichte (§ 10), Struktur und Bewertung (§ 11) | v0.21, 17.09. | 12.09. | 17.09. | 24 |
| `abi-quellen.md` | K (abi) | Verzeichnis, Dateinamen, Verlagsbände, lokaler Heftordner, Markdown-Korpus | v0.5, 17.09. | 12.09. | 17.09. | 5 |
| `abi-aufbau.md` | K (abi) | Befundaufnahme Aufbau 2017/2018 (Zeiten, Wahlstruktur, BE, Zwillingsnachweis) | v0.1, 12.09.; nur 2017/2018, seitdem nicht fortgeschrieben (Aufbau ab 2019 steht in abi.md § 11) | 12.09. | 12.09. | 1 |
| `abi-struktur.json` | K (abi) | BE-Vektoren der zwölf Hefte 2017/2018 (WTR und CAS) für den Zwillingsnachweis | 12.09.; nur 2017/2018, keine Verwendung durch ein Skript | 12.09. | 12.09. | 1 |
| `abi-vorgaben.md` | K (abi, iqb) | Amtliche Vorgaben Abitur (Fachbriefe, Prüfungsschwerpunkte) mit Jahrescheck | Stand 13.09., Prüfungsschwerpunkte 2027 eingetragen 15.09. | 13.09. | 15.09. | 3 |
| `abi-bau.py` | K (abi) | Bau-Skript abi (Gerüst je Heft; enthält die 46 ZEILEN von 2025-bebb-lk: 1030 der 1810 Quelltextzeilen) | v0.9, 17.09. | 12.09. | 17.09. | 27 |
| `abi-katalog.csv` | K (abi) | Katalog abi, 794 Zeilen, 16 Hefte 2017–2026 | 17.09. (Lauf 22) | 12.09. | 17.09. | 29 |
| `abi-pruefungen.md` | K (abi) | Heftliste abi, Kennzahlen, Befunde je Heft und Lauf (§ 4, 195 KB), Änderungslog (§ 5) | 17.09. | 12.09. | 17.09. | 41 |
| `iqb.md` | K (Profil iqb) | Profil IQB-Aufgabenpool | v1.9, 17.09. | 13.09. | 17.09. | 34 |
| `iqb-quellen.md` | K (iqb) | Beschreibung der Quelle, Kennungsschema, Dubletten | v0.4, 15.09. | 13.09. | 15.09. | 6 |
| `iqb-quellen.csv` | K (iqb) | Alle 624 Kennungen mit Zerlegung, Stapel, Seiten, Dublettenverweis (erzeugt) | 15.09. | 13.09. | 15.09. | 6 |
| `iqb-quellen.py` | K (iqb) | Erzeugt iqb-quellen.csv aus der IQB-Übersicht (Scan, Dublettenprüfung) | v0.4, 15.09. | 13.09. | 15.09. | 5 |
| `iqb-bau.py` | K (iqb) | Bau-Skript iqb (Gerüst je Stapel; enthält die ZEILEN des letzten Stapels) | v1.5, 17.09. | 13.09. | 17.09. | 44 |
| `iqb-katalog.csv` | K (iqb) | Katalog iqb, 1258 Zeilen, 33 Stapel | 17.09. | 13.09. | 17.09. | 49 |
| `iqb-pruefungen.md` | K (iqb) | Stapelliste, Befunde (252 KB, größte Textdatei), Änderungslog | 17.09. | 13.09. | 17.09. | 77 |
| `abitur-vokabular.md` | K (abi, iqb) | Gemeinsames Vokabular: Sachgebiete, Themen, Geltungstabelle, Ausschlussliste, Gegenstandsklassen | v1.4, 17.09. | 15.09. | 17.09. | 5 |
| `abitur-typen.csv` | K (abi, iqb) | Gemeinsame Typenliste, 1211 Typen | 17.09. | 15.09. | 17.09. | 22 |
| `abgleich.py` | K (abi, iqb) | Abgleichläufe 1–23 über Typenliste und beide Kataloge (jeder Lauf einmalig, als Code archiviert; 108 KB) | v0.23, 17.09. | 15.09. | 17.09. | 11 |
| `abi-iqb-typen.md` | X (K, erledigt) | Vergleich der Typenlisten abi/iqb als Entscheidungsgrundlage für Entscheidung 25 (15.09.) | historisch; die verglichenen Listen existieren nicht mehr | 15.09. | 15.09. | 2 |
| `blatt-konzept.md` | B | Konzept der Nachhilfehefte aus dem Katalog (Heft-Phase), Baumaschine Prüfungsprompt | v0.8, 12.09. | 05.09. | 12.09. | 8 |
| `masterprompt.md` | B | Masterprompt (Blätter ohne Katalog), Masterfassung | v3.34, 08.09. | 07.09. | 08.09. | 7 |
| `pruefungsprompt.md` | B | Prüfungsprompt (Hefte mit Katalog, heute Profil msa), Masterfassung | v0.14, 08.09. | 07.09. | 08.09. | 7 |
| `mathblatt.sty` | B | LaTeX-Vorlage für die Arbeitsblätter | 2026-09-07d | 07.09. | 07.09. | 5 |
| `Anleitung_mathblatt.md` | B | Anleitung zur Vorlage (Stufe 3), von den Prompts beim Bau geholt | zu 07d, 08.09. | 07.09. | 08.09. | 7 |
| `Testauswertung_Masterprompt_Mathe_2026-09-07.md` | X (B, überholt) | Auswertungsvorschrift für Protokoll-Archive, Fassung vom 07.09. | durch die Fassung vom 08.09. ersetzt | 07.09. | 07.09. | 3 |
| `Testauswertung_Masterprompt_Mathe_2026-09-08.md` | B | Auswertungsvorschrift für Protokoll-Archive, gültige Fassung | 08.09. | 08.09. | 08.09. | 1 |
| `Bewertung_Masterprompt_v3-34.md` | B | Bewertung des Masterprompts v3.34 (Kernbefund, Werkstatt) | 08.09., einmalig | 09.09. | 09.09. | 1 |
| `uebergabe.md` | X (B, Werkstatt-Prozess) | Übergabezettel der Werkstatt-Lieferung 08.09. („Zuerst dieses Zip hochladen"), Arbeitsstand und Entscheidungen des Blattbaus | 08.09.; Chat-Übergabe, kein Repo-Baustein | 07.09. | 08.09. | 4 |
| `archiv-hinweis.md` | X (B, Werkstatt-Prozess) | Inhaltszettel des Werkstatt-Archivs 09.09. („Nicht für Katalog-Chats") | 09.09.; Chat-Übergabe | 09.09. | 09.09. | 1 |
| `quellen.md` | K+B (Themenkatalog, konzept § 3) | Übersicht der drei Quellentexte (RLP, Klett-Fahrplan, LISUM-Planungshilfen) | 12.09.; verweist auf `katalog/_suche_quelle.py`, das es hier nicht gibt; kein Verweis aus einer anderen Datei | 13.09. | 13.09. | 1 |
| `quelle-rlp-teil-c-mathematik-2023.txt` | K+B (Themenkatalog) | Textfassung Rahmenlehrplan 1–10 Teil C Mathematik 2023 (180 KB) | 12.09. | 13.09. | 13.09. | 1 |
| `quelle-klett-fahrplan-ls-aa-berlin-2024.txt` | K+B (Themenkatalog) | Textfassung Klett-Fahrplan Lambacher Schweizer Berlin 2024 (219 KB, © Klett, nur Gliederung) | 12.09. | 13.09. | 13.09. | 1 |
| `quelle-lisum-planungshilfen-7bis10.txt` | K+B (Themenkatalog) | Textfassung LISUM-Planungshilfen 7–10 (260 KB, CC BY-SA) | 12.09. | 13.09. | 13.09. | 1 |

Zählung: K 32 (msa 6, fhr 5, abi 8, iqb 7, abi+iqb 3, alle Profile 3:
Kern, CLAUDE.md, .gitignore), B 8 (darunter als Grenzfall
Bewertung_Masterprompt, das nur der Archivzettel nennt), K+B 9 (README,
konzept, .gitattributes, zwei fhr-Typenbibliothek-Dateien, quellen.md mit
drei Quellentexten), X 4 (abi-iqb-typen.md, Testauswertung 07.09.,
uebergabe.md, archiv-hinweis.md).

## 2 Auffälligkeiten

**Skripte, die dasselbe tun.**

- Die drei Bau-Skripte (`abi-bau.py` 136 KB, `iqb-bau.py` 51 KB, `fhr-bau.py`
  38 KB) tragen denselben Kern – Laden und Schreiben der CSV im festen Format,
  Zeilenprüfung (Pflichtfelder, Vokabular, Umlaut-Umschrift, ASCII-Minus),
  Typenprüfung, Selbstprüfung über den Bestand, Kennzahlen – in drei Kopien,
  die nacheinander weiterentwickelt wurden (fhr auf Kern v0.3, iqb v1.5, abi
  v0.9). Eine Änderung am Kern (zuletzt: Maßstab der Schätzung) muss je
  Skript nachgezogen werden; fhr ist seit dem 12.09. nicht mitgezogen.
- Jedes Bau-Skript im Repo enthält die ZEILEN des zuletzt erfassten Hefts
  bzw. Stapels (abi: 2025-bebb-lk, 1030 der 1810 Zeilen). Der versionierte
  Stand eines Skripts ist damit immer „Gerüst + letztes Heft"; das Gerüst
  allein ist nirgends abgelegt, die Heftdaten nach dem Lauf tot.
- `abgleich.py` archiviert 22 einmalige Läufe als Code (102 KB); jeder Lauf
  ist nach dem Fahren nur noch Beleg. Das Skript wächst mit jedem Lauf, die
  gemeinsame Maschinerie (Umbenennen, Zusammenziehen, Feldkorrektur,
  Prüfungen) macht davon etwa 150 Zeilen aus.
- Die Prüfwerkzeuge, die die Arbeitsregeln in CLAUDE.md verlangen (Selbstprüfung
  beider Skripte in einer Arbeitskopie, byteidentischer HEAD-Rerun je Heft,
  Stapel und Abgleichlauf, Messung neuer Schnittwerte, Erzeugen der
  Dubletten-Zeilen aus Poolzeilen), liegen **nicht im Repo**, sondern im
  Scratchpad der Sitzung (§ 3): `selbst.py`, `pruefe.py`/`pruefe2.py` (zwei
  ältere Fassungen desselben, Selbstprüfung plus HEAD-Rerun), `heftrerun.py`,
  `stapelrerun.py`, `abgleichrerun.py`, `heftmass.py`/`stapelmass.py`/
  `teilamass.py`, `dubletten.py`, `bau_heft.py`. Sie verschwinden mit der
  Sitzung und werden bei Bedarf neu geschrieben; die Regel „Lauf aus HEAD
  byteidentisch" ist im Repo nur als Text, nicht als Werkzeug vorhanden.

**Dateien ohne Verweis aus CLAUDE.md oder einem Profil.**

- `quellen.md` und die drei `quelle-*.txt` (660 KB, ein Zehntel des Repos):
  kein Verweis aus irgendeiner anderen Datei; Zweck ist der Themenkatalog aus
  konzept.md § 3, der nicht angelegt ist; `quellen.md` nennt ein Werkzeug
  `katalog/_suche_quelle.py` aus einer anderen Ablage.
- `archiv-hinweis.md`, `uebergabe.md`, `Bewertung_Masterprompt_v3-34.md`,
  beide `Testauswertung_*.md`: Verweise nur untereinander und aus
  blatt-konzept.md; README.md behauptet, Testauswertung und Protokoll-Archive
  lägen im Werkstatt-Projekt und nicht hier.
- `abi-iqb-typen.md`: nur als historischer Verweis (Entscheidung 25) genannt.
- `abi-struktur.json`: aus CLAUDE.md § 1 genannt, von keinem Skript gelesen.
- Nicht aus CLAUDE.md, aber aus konzept.md/README.md: `blatt-konzept.md`,
  `mathblatt.sty`, `Anleitung_mathblatt.md`, `CHANGELOG.md`, die
  fhr-Typenbibliothek, die msa-Dateien (CLAUDE.md nennt sie nur als „liegen
  daneben, werden hier nicht angefasst").

**Doppelstände.**

- Zwei Landkarten des Repos: README.md (Tabelle) und konzept.md § 2
  (Liste), beide teilweise veraltet und nicht deckungsgleich (README kennt
  keine quelle-Dateien, konzept nennt `pdf/` als noch nicht angelegt).
- Aufbau der Abiturprüfung an drei Stellen: `abi-aufbau.md` und
  `abi-struktur.json` (nur 2017/2018, Stand 12.09.) neben abi.md § 3, § 10,
  § 11 (alle Jahrgänge, laufend fortgeschrieben). Die beiden älteren Dateien
  sind seit ihrer Anlage unverändert.
- Zwei Testauswertungen (07.09., 08.09.) mit gleichem Aufbau; der
  Archivzettel erklärt die vom 08.09. für gültig.
- Zwei Vorgaben-Dateien (`vorgaben.md` msa, `abi-vorgaben.md` abi/iqb) mit
  gleichem Zuschnitt, dazu abi.md § 10/§ 11 mit teils denselben Inhalten
  (Prüfungsschwerpunkte 2027 stehen in abi-vorgaben.md § 2, abi.md § 3 und
  abitur-vokabular.md § 3).
- Zwei Änderungslog-Systeme: CHANGELOG.md für Prompts und Vorlage;
  `*-pruefungen.md` § 5 für die Kataloge, dazu die Versionsvermerke im Kopf
  jeder md-Datei und jedes Skripts.
- Versionsangaben in CLAUDE.md § 1 hinken (abi.md v0.18 statt v0.21, Kern
  v0.6 statt v0.7).
- msa führt Basis- und Kontextaufgaben in zwei Katalogdateien
  (katalog-basis/katalog-kontext); abi hat dieses Modell verworfen (eine
  Datei, Feld block). Beide Modelle liegen nebeneinander, das Profil msa ist
  auf Kern v0.3 stehen geblieben.

**Reste aus verworfenen oder abgeschlossenen Ansätzen.**

- `abi-iqb-typen.md`: Messung vor der Zusammenführung der Typenlisten; die
  gemessenen Dateien (abi-typen.csv, iqb-typen.csv) sind seit Lauf 12
  gelöscht.
- `uebergabe.md`, `archiv-hinweis.md`: Zettel eines Zip-Übergabeprozesses
  zwischen Chats („Zuerst dieses Zip hochladen", „Nicht für Katalog-Chats");
  im Repo ohne Funktion, seit dem 08./09.09. unverändert.
- `Testauswertung_…_2026-09-07.md`: überholte Fassung.
- `abi-aufbau.md` § 5 und `abi-struktur.json`: der CAS-Nachtrag für 2017/2018
  ist bis heute nicht erfolgt (abi-pruefungen.md § 2 „zurückgestellt");
  die Vorarbeit liegt seit dem 12.09. brach.
- `konzept.md` § 2 nennt `pdf/` (Archiv der Hefte, nie angelegt) und
  `<kennung>-typenbibliothek` „für msa noch nicht" – der Ansatz Typenbibliothek
  ist nur für fhr ausgeführt und seit dem 12.09. nicht weitergegangen.

**Sonstiges, für die Entscheidung über Ordner und Trennung.**

- Größen: die vier Katalog-CSV (abi 1,1 MB, iqb 1,6 MB, abitur-typen 0,4 MB,
  fhr 0,4 MB) und die zwei Befund-Dateien (iqb-pruefungen 252 KB,
  abi-pruefungen 195 KB) machen 4 MB der 6,2 MB aus; die Blattbau-Dateien
  zusammen 0,35 MB.
- Namensschema: msa ohne Präfix (typen.csv, katalog-*.csv, pruefungen.md,
  vorgaben.md), fhr/abi/iqb mit Präfix, Gemeinsames unter `abitur-*`,
  Quellentexte unter `quelle-*.txt` neben `*-quellen.md`, Werkstattdateien in
  CamelCase mit Datum. Bei einer Trennung nach Projekten wären die
  K+B-Dateien (README, konzept § 3, Typenbibliothek, quellen) die Schnittstelle.
- Alles, was das Katalog-Projekt außerhalb des Repos hält (hefte/, hefte-md/,
  iqb-pdf/), ist in .gitignore erfasst; Scratchpad-Werkzeuge sind es nicht
  (§ 3).

## 3 Werkzeuge außerhalb des Repos (Scratchpad der Sitzung, nicht versioniert)

Stand 17.09.2026, rund 290 Python-Dateien; die meisten sind Einmalskripte
je Heft, Stapel oder Lauf (`zeilen-*.py`, `block_*.py`, `map_*.py`,
`typen_*.py`, `rechne*.py`, `nach_*.py`, `patch*.py`). Wiederverwendet und
für die Arbeitsregeln nötig:

| Skript | Zweck |
|---|---|
| `selbst.py` | Selbstprüfung beider Bau-Skripte mit geleertem ZEILEN in einer Arbeitskopie |
| `pruefe.py`, `pruefe2.py` | ältere Fassungen desselben, dazu HEAD-Rerun (Lauf 12) |
| `heftrerun.py`, `stapelrerun.py`, `abgleichrerun.py` | HEAD-Rerun je Heftlauf, Stapellauf, Abgleichlauf; Bytevergleich mit dem Arbeitsbaum |
| `heftmass.py`, `stapelmass.py`, `teilamass.py` | neue Schnittwerte eines Hefts/Stapels gegen den Bestand |
| `dubletten.py`, `bau_heft.py`, `splice_abi.py`, `splice.py` | Heft-Pipeline: Dubletten-Zeilen aus Poolzeilen erzeugen, Blöcke zusammensetzen, in das Bau-Skript einsetzen |
| `fixquotes.py` | typografische Anführungszeichen in Python-Strings |
| `aehnlich.py` | Ähnlichkeitssuche über neue Typen vor einem Abgleichlauf |
| `check_md25gk.py`, `crops25gk.py`, `crop.py`, `pdftxt.py`, `pdfrender.py` | Markdown-Korpus: Prüfung gegen den Katalog, Bildausschnitte, Text und Seitenbilder aus PDF |
| `casdelta.py`, `eichquote.py`, `afb_stat*.py`, `geltung_check*.py` | Messskripte der Aufträge A–C |

Diese Werkzeuge sind im Repo nur beschrieben (CLAUDE.md § 2 Schritt 6,
abi-pruefungen.md § 4), nicht abgelegt.
