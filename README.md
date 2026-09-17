# mathe-nachhilfe

Ein Repo für die Mathe-Nachhilfe: Prüfungskataloge, die Prompts, die LaTeX-Vorlage. Alles liegt flach in der Wurzel; jedes Profil trägt sein Präfix (msa-, fhr-, abi-, iqb-; msa seit 17.09.2026), Gemeinsames von abi und iqb `abitur-`, Befunde `befund-` (namensschema.md).

| Datei | Rolle |
|---|---|
| `masterprompt.md` | Masterprompt – baut alles ohne Katalog (Unterricht Kl. 8–13, Klassenarbeiten, Prüfungen ohne Katalog). Projektanweisung im Masterprompt-Projekt ist eine Kopie. |
| `pruefungsprompt.md` | Prüfungsprompt – baut Prüfungen mit Katalog, heute Profil msa. Projektanweisung im Aufgaben-Projekt ist eine Kopie. |
| `mathblatt.sty`, `Anleitung_mathblatt.md` | LaTeX-Vorlage und ihre Anleitung; die Prompts holen beide beim Bau. Version in Zeile 2. |
| `katalog-prompt.md`, `msa.md` | Erfassung: Kern (Methode) und Profil msa (P10 Brandenburg, FOR). |
| `msa-typen.csv`, `msa-katalog-basis.csv`, `msa-katalog-kontext.csv`, `msa-bau.py` | Katalog msa: Typenliste, Basis- und Kontextaufgaben, Bau-Skript mit Selbstprüfung. |
| `fhr.md`, `fhr-*` | Profil fhr (Fachhochschulreife Brandenburg): Profil, Heftliste, Typenliste, Katalog, Bau-Skript, Typenbibliothek, Vorgaben. |
| `abi.md`, `abi-*` | Profil abi (Zentralabitur Berlin/Brandenburg 2017/2018, Verlagsscans ab 2019): Profil, Quellen, Aufbau, Heftliste, Katalog, Bau-Skript, Vorgaben. Arbeitsanweisung in `CLAUDE.md`. |
| `iqb.md`, `iqb-*` | Profil iqb (IQB-Aufgabenpool, 624 Aufgaben mit Erwartungshorizont): Profil, Quellen (md und csv), Stapelliste, Katalog, Bau-Skript. Arbeitsanweisung in `CLAUDE.md` § 4. |
| `abitur-vokabular.md`, `abitur-typen.csv`, `abitur-abgleich.py`, `befund-abi-iqb-typen.md` | Gemeinsam für abi und iqb (Entscheidung 25): Vokabular (Sachgebiete, Themen, Geltung, Gegenstandsklassen; Handlung je format seit Kern v0.4 im Kern), eine Typenliste, Abgleich-Skript über beide Kataloge, Messung und Zuordnung der Typenlisten vor der Zusammenführung. |
| `konzept.md`, `blatt-konzept.md` | Entscheidungen: Katalog bzw. Hefte. Bei Widerspruch in der Heft-Phase gilt blatt-konzept. |
| `msa-pruefungen.md`, `msa-vorgaben.md` | Heftliste mit Erfassungsstatus; amtliche Vorgaben mit Jahrescheck. |
| `CHANGELOG.md` | Änderungshistorie der Prompts und der Vorlage. |

Aufteilung der Prompts nach Quelle: Katalog vorhanden → Prüfungsprompt, sonst Masterprompt (blatt-konzept §5). Gemeinsame Abschnitte 3–6 werden in beiden gepflegt. Testauswertung und Protokoll-Archive liegen im Werkstatt-Projekt, nicht hier.
