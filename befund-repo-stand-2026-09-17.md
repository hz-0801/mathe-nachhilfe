# Stand des Repos am 17.09.2026 – Stichtagsbefund
Befund, einmalig und eingefroren (namensschema.md § 2: befund-<gegenstand>-<datum>): so sah das Repo am 17.09.2026 nach Abschluss der Aufträge D bis G aus. Ab dem nächsten Commit veraltet; wird nicht fortgeschrieben. Kein Verlauf: Geschichte steht in den Änderungslogs der Dateien.

## 0 Geltung dieses Befunds

Diese Datei ist kein Einstieg und keine Anweisung. Einstieg für jede Arbeit im Repo sind `CLAUDE.md` (Arbeitsanweisung, Werkzeuge, Arbeitsregeln) und `konzept.md` (Entscheidungen § 4, Offenes § 6); was der Kern und die Profile regeln, steht in `katalog-prompt.md` und in `msa.md`, `fhr.md`, `abi.md`, `iqb.md` selbst und gilt in der jeweils geltenden Fassung, nicht in der hier festgehaltenen. Was diese Datei leistet: den Zustand eines Tages nachweisbar festhalten – welche Dateien es gab und welche Rolle sie hatten (§ 1), was Kern und Profile an diesem Tag regelten (§ 2–3), die Bestandszahlen der Selbstprüfung (§ 4). Wer wissen will, was heute gilt, liest die Dateien; wer wissen will, was am 17.09.2026 galt, liest hier.

Befund zu den Werkzeugen: Die Prüfwerkzeuge der Arbeitsregeln – Selbstprüfung aller Bau-Skripte in einer Arbeitskopie mit geleertem `ZEILEN`, byteidentischer Rerun eines Laufs aus dem HEAD-Stand, BOM/CRLF-Prüfung – lagen am 17.09.2026 nicht im Repo, sondern im Scratchpad der Sitzung (befund-repo-bestand.md § 3).

## 1 Dateien und Rollen

Alle Dateien flach in der Wurzel; Präfix je Profil (`msa-`, `fhr-`, `abi-`, `iqb-`), Gemeinsames der Familie abi unter `abitur-`, Befunde unter `befund-` (§ 6).

**Regelwerk (alle Profile)**

| Datei | Rolle |
|---|---|
| `konzept.md` | Gesamtkonzept: Ziel, Bausteine (§ 2), Themenkatalog (§ 3), Entscheidungen 1–33 (§ 4), Verworfenes (§ 5), Offenes (§ 6), Ablauf (§ 7), Eine neue Prüfung aufnehmen (§ 8), Andere Zielprüfung bei gleichem Bestand (§ 9), Änderungen (§ 10). |
| `katalog-prompt.md` | Kern (v0.9, Schema-Version 2): Methode der Erfassung, prüfungsunabhängig. |
| `CLAUDE.md` | Arbeitsanweisung für die Erfassung abi und iqb im Repo; Arbeitsregeln (§ 3) gelten sinngemäß für alle Profile. |
| `namensschema.md` | Bausteine und Kennungsstufen der Dateinamen (v0.2); § 4 Umbenennungsliste mit Varianten A/B/C. |
| `README.md` | Landkarte des Repos. |
| `.gitignore` | Schließt `hefte/`, `hefte-md/`, `iqb-pdf/`, `__pycache__/` aus – Verlagsmaterial und Cache bleiben lokal. |

**Profil msa** (P10 Brandenburg, Oberschule/Gesamtschule, Niveau FOR; Alias von msa-bb)

| Datei | Rolle |
|---|---|
| `msa.md` | Profil (v0.6): Prüfung, Basis-URL, Heftaufbau, Kürzel (papier OS/EBR/FOR/MUSTER-…, id `Jahr-papier-B1a` bzw. `-K3b`), Leitideen (§ 5), Themenliste (§ 6), Besonderheiten, Beispielzeilen. |
| `msa-katalog-basis.csv`, `msa-katalog-kontext.csv` | Katalog in zwei Dateien (block Basis / Kontext, Entscheidung 14), gleiches Schema. |
| `msa-typen.csv` | Typenliste msa (`typ;leitidee;thema;definition;beispiel_id;status`). |
| `msa-pruefungen.md` | Heftliste mit Erfassungsstatus, Änderungslog. |
| `msa-vorgaben.md` | Amtliche Vorgaben P10 (Fachbriefe) mit Jahrescheck; vom Katalog nicht gelesen. |
| `msa-bau.py` | Bau-Skript (v0.2): Gerüst je Heft, Selbstprüfung des Bestands, Feldkorrektur an der Typenliste (`TYPEN_KORREKTUR`); liest Kern § 5 und msa.md § 5–6. |

**Profil fhr** (Fachhochschulreife Brandenburg; Alias von fhr-bb)

| Datei | Rolle |
|---|---|
| `fhr.md` | Profil (v1.9): Prüfung, Quellen, Aufbau, Kürzel (papier A/B/C, id `Jahr-papier-1a`), Leitideen, Themenliste mit Schwerpunktmarkierung 27/28 (§ 6), Besonderheiten (§ 7, darunter die Regel Punkt-Schwerpunkt), Beispielzeilen, Offenes. |
| `fhr-katalog.csv`, `fhr-typen.csv` | Katalog (eine Datei, block leer) und Typenliste. |
| `fhr-pruefungen.md` | Heftliste, Umfang, Änderungslog. |
| `fhr-vorgaben.md` | Amtliche Vorgaben FHR mit Jahrescheck – **Vorbehalt im Kopf: aus fhr.md zusammengetragen, Papiere nicht gelesen.** |
| `fhr-bau.py` | Bau-Skript (v0.4) mit Selbstprüfung; Themenliste als Code (`THEMEN`). |
| `fhr-typenbibliothek.py`, `fhr-typenbibliothek.md` | Erzeuger und erzeugte Typenbibliothek (Vorstufe für den Blattbau); die .md wird nie von Hand geändert. |

**Profil abi** (Zentralabitur Berlin/Brandenburg; Alias von abi-bebb) und **Profil iqb** (IQB-Aufgabenpool; Alias von abi-iqb)

| Datei | Rolle |
|---|---|
| `abi.md` | Profil abi (v0.26): Prüfung, Basis-URL, Heftaufbau, Kürzel (papier `Jahr-Land-Niveau[-cas]`, Land be/bb/bebb nach Jahrgang; id `papier-BlockAufgabeTeilaufgabe`), Zeile „Zielprüfungen:", Besonderheiten (§ 7: Dubletten, Vormerkung, Eichung ausgesetzt), Prüfungsgeschichte (§ 10), Struktur und Bewertung (§ 11). |
| `abi-quellen.md` | Verzeichnis der Hefte, Dateinamen, Seitenzahlen; § 8 lokaler Heftordner `hefte/` mit Erfassungsstand. |
| `abi-aufbau.md`, `abi-struktur.json` | Aufbau 2017/2018 (Zeiten, Wahlstruktur, BE-Vektoren, Zwillingsnachweis); nur diese Jahrgänge. |
| `abi-bau.py` | Bau-Skript abi (v0.12): `KONFIG`, `ZEILEN`, `NEUE_TYPEN`; prüft Präfixregel, Zeilenthema = Typthema, Schwellen, Eichung, Vollständigkeit, Dublettenverweise, Geltung; enthält die `ZEILEN` des zuletzt erfassten Hefts. |
| `abi-katalog.csv` | Katalog abi (eine Datei, Feld block trennt Prüfungsteile). |
| `abi-pruefungen.md` | Heftliste (§ 2 mit Kennzahlen je Heft), Befunde je Heft und Lauf (§ 4), Änderungslog (§ 5). |
| `iqb.md` | Profil iqb (v1.13): Pool als Quelle, Kennung und id (§ 4: Kennung = Dateiname ohne `_Aufgabe.pdf`, id `Kennung-Teilaufgabe`, papier `Jahr-iqb-Niveau[-mms]`), Stapel als Laufeinheit, § 6 Zielprüfungen und Schnitt, § 7 Eichung und Schwellen, Deutungsliste für die Schätzung. |
| `iqb-quellen.md`, `iqb-quellen.csv`, `iqb-quellen.py` | Quelle, Kennungsschema, alle 624 Kennungen mit Stapel, Seiten und Spalte `dateidublette_von` (erzeugt). |
| `iqb-bau.py` | Bau-Skript iqb (v1.9): `row(kennung, teilaufgabe, …)`, `SCHWELLEN` (darunter Eichung 85 %), Stapelvollständigkeit, Landesverwendung. |
| `iqb-katalog.csv` | Katalog iqb. |
| `iqb-pruefungen.md` | Stapelliste (§ 2 mit Kennzahlen je Stapel), Befunde (§ 4), Änderungslog (§ 5). |
| `abitur-vokabular.md` | Gemeinsames Vokabular abi/iqb (v1.6): Sachgebiete (§ 1), Themenliste (§ 2), Geltungsregeln (§ 3), Gegenstandsklassen und Regel Zeilenthema = Typthema (§ 4), Regeln der gemeinsamen Typenliste (§ 6). |
| `abi-be-gk-geltung.md`, `abi-be-lk-geltung.md`, `abi-bb-gk-geltung.md`, `abi-bb-ea-geltung.md` | Geltung je Zielprüfung: § 1 Thema ja/nein, § 2 ausgeschlossene Aufgabenformen, § 3 Rechnerfassung; beide Bau-Skripte lesen sie. |
| `abitur-typen.csv` | Gemeinsame Typenliste abi/iqb; `beispiel_id` zeigt in einen der beiden Kataloge. |
| `abitur-abgleich.py` | Abgleichläufe 1–23 als Code (`LAEUFE`): Umbenennen, Zusammenziehen, Feldkorrekturen über Typenliste und beide Kataloge; `python abitur-abgleich.py N`. |
| `abi-vorgaben.md` | Amtliche Vorgaben Abitur beider Länder (Prüfungsschwerpunkte 2027) mit Jahrescheck. |

**Befunde** (datiert, werden nicht fortgeschrieben): `befund-repo-bestand.md` (alle Dateien mit Zweck, Stand, git-Daten; § 2 Auffälligkeiten, § 3 Scratchpad-Werkzeuge), `befund-typenlisten.md` (die drei Typenlisten nebeneinander, Vorschläge), `befund-lesbarkeit.md` (Stellen mit Vorwissen in Kern und Profilen), `befund-abi-iqb-typen.md` (Vergleich vor der Zusammenführung der Typenlisten), diese Datei.

**Blattbau** (anderes Projekt, im selben Repo): `masterprompt.md` (v3.35, Blätter ohne Katalog), `pruefungsprompt.md` (v0.15, Hefte aus dem Katalog, heute Profil msa; holt `msa-typen.csv`, `msa-katalog-basis.csv`, `msa-katalog-kontext.csv` von der Basis-URL), `blatt-konzept.md`, `mathblatt.sty` und `Anleitung_mathblatt.md` (LaTeX-Vorlage), `CHANGELOG.md`; die Projektanweisungen in den Claude-Projekten sind Kopien der beiden Prompts. Werkstattdateien (`Testauswertung_*`, `Bewertung_*`, `uebergabe.md`, `archiv-hinweis.md`) und die Quellentexte des Themenkatalogs (`quellen.md`, `quelle-*.txt`) liegen daneben.

**Lokal, nicht im Repo:** `hefte/` (Verlagsscans abi ab 2019, Textauszüge, Verlagshinweise; urheberrechtlich geschützt), `hefte-md/` (Markdown-Korpus der Hefte mit Abbildungen), `iqb-pdf/` (Cache der Pooldateien). Alle drei in `.gitignore`; sie bleiben dort.

## 2 Was der Kern regelt (katalog-prompt.md v0.9)

- **Ziel und Maßstab (§ 0):** je Teilaufgabe eine Katalogzeile; Erfolgskriterium ist der Nachbau-Test – aus der Zeile allein muss sich eine strukturgleiche Aufgabe bauen lassen. Fakten und Deutung getrennt; Deutung nur in `niveau_geschaetzt`, `fehlerquelle`, `bemerkung`.
- **Arbeitsgrundlage und Ablauf (§ 1–3):** Katalogdateien von der Basis-URL des Profils; ein Heft je Antwort; Text extrahieren, jede Aufgabenseite rendern, bei Widerspruch gilt das Bild; jedes rechnerische Ergebnis per Skript nachrechnen, amtliche Lösung geht vor.
- **Zeilenregel (§ 4):** kleinste Einheit mit eigener Punktangabe; mehrere Leistungen bleiben eine Zeile (`typ` = Haupttyp, `typ_neben` = Nebentypen); Aufgabenstamm in jeder Zeile wiederholen; Abhängigkeiten in `abhaengig_von`.
- **Felder (§ 5, Schema-Version 2):** 37 Felder mit fester Kopfzeile, Semikolon, alles gequotet, UTF-8; Formvokabular für format, antwort, material, zahlenraum, textumfang; Handlung je format (Tabelle) für den Schnitt; Vorrang des Amtlichen und Maßstab der Schätzung (`afb_amtlich` leer = Schätzung ohne Maßstab; Eichung ist Kennzahl in Profilen mit amtlichen Anforderungsbereichen, sonst entfällt sie; ob Schranke, entscheidet das Profil); Markierungen in `bemerkung`: „Dublette von:", Vormerkung „Poolaufgabe (nicht erfasst):" als Übergangszustand, „Abgewandelt von:", „Traegerbindung: Kontext"; Dateidublette ist Eigenschaft der Datei, nicht der Zeile.
- **Vokabular (§ 6):** Leitidee und Thema fest im Profil oder in der Vokabulardatei; Zeilenthema = Typthema als Regel, ein Profil kann eine eigene festlegen; Typ = Fertigkeit als Gegenstand plus Handlung, Etikett = Name des Typs; gleiche Fertigkeit → gleiches Etikett, anderer Lösungsweg → trennen; Änderungen an bestehenden Etiketten nur im Abgleichlauf.
- **Prüfung, Ausgabe, Abgleichlauf (§ 7–9):** Zeilenzahl, Punktsummen, Nachbau-Test, eindeutige Kennung, Typ in der Liste; Selbstprüfung mit leerer Zeilenliste über den ganzen Bestand – ein Profil ohne sie gilt als unvollständig; Ausgabe nur geänderte Dateien, Prüftabelle, Bericht; Abgleichlauf über ein Skript, das Typenliste und alle Kataloge derselben Liste zugleich umstellt.

## 3 Was die Profile regeln

Jedes Profil nennt Prüfung und Träger, Basis-URL und Quellen, Heftaufbau, Kürzel und id-Muster, Leitideen und Themenliste (oder die Vokabulardatei), Besonderheiten beim Erfassen, Beispielzeilen aus dem Katalog, Offenes; im Kopf die Kernbindung (welche Kernänderungen durchgesehen sind, welche eigene Regel gilt).

- **msa:** zwei Katalogdateien Basis/Kontext; Zeilenthema = Thema der Aufgabenstellung (eigene Regel, entschieden; 42 von 393 Zeilen weichen vom Typthema ab); amtliche Bereiche nur bei den Musteraufgaben 2028 (nicht erfasst), Eichung entfällt bis dahin; keine Geltungsdatei (Themenliste gilt ganz); Koordinaten mit „|" wie im Heft.
- **fhr:** ein Niveau, keine Anforderungsbereiche (Eichung entfällt), amtlicher Erwartungshorizont (ergebnis „amtlich"); Zeilenthema nach Punkt-Schwerpunkt bei mehrleistigen Zeilen (eigene Regel); Schwerpunktstand über Markierung 27/28 in der Themenliste statt Geltungsdatei; Decke einer Kette nach blatt-konzept.md § 3, Vorgabenstand nur Information.
- **abi:** Leitfassung je Jahr und Niveau (erhöht bb-ea, grundlegend be-gk), Zwillinge des anderen Landes nur als Vermerk, CAS-Hefte Nachtrag; Pool-Teilaufgaben als eigene Zeile mit „Dublette von: <iqb-id>" und dem Typ der Poolzeile, sonst Vormerkung (überlebt keinen Auftrag); `afb_amtlich` genau bei Dubletten aus der Poolzeile; Eichschwelle ausgesetzt, Kennzahl bleibt; Geltung über die vier Zielprüfungen, gemeinsame Hefte bebb gegen beide Spalten; Poolquote je Heft ist Kennzahl.
- **iqb:** Stapel (Prüfungsteil eines Pooljahrs auf einem Niveau) als Laufeinheit, Teil A vor Teil B; id aus der Kennung, `afb_amtlich` aus dem Standardbezug; Schätzung vor dem Lesen des Erwartungshorizonts; `SCHWELLEN` im Skript (Eichung mindestens 85 % je Stapel, „?", neue Typen, „ersatzweise"); Dateidubletten bekommen keine Zeile; MMS/CAS als Delta zur WTR-Fassung; Abbruchkriterium: unter fünf neue Schnittwerte in der Geltung heißt ausgereizt, Reserve nur für Landesheftverweise.
- **Gemeinsam abi/iqb:** eine Typenliste, ein Vokabular; Typname in Themen mit Gegenstandsklassen mit Präfix „Klasse: "; Zeilenthema = Typthema erzwungen; Schnitt Thema × Klasse × Handlung als Einheit für den Blattbau, der Typ bleibt Feinetikett; Abgleichlauf nach jedem Stapel über abitur-abgleich.py, danach Selbstprüfung beider Skripte.

## 4 Bestandszahlen (Selbstprüfung 17.09.2026) und wo sie stehen

| Profil | Bestand | Zeilen | Typen | Weitere Kennzahlen |
|---|---|---|---|---|
| msa | 13 Hefte (2014–2026: 12 Oberschulhefte, 2026 FOR) | 393 (126 Basis, 267 Kontext) | 185 | Musteraufgaben 2028 nicht erfasst; 42 Zeilen mit Zeilenthema ≠ Typthema |
| fhr | 16 Hefte 2019–2026, vollständig | 253 | 135 | 3,61 Vorkommen je Typ; 49 Typen genau einmal; Eichung entfällt |
| abi | 16 Hefte 2017–2026 (2017/2018 amtlich, ab 2019 Verlagsscans) | 794 | 1323 gemeinsam (267 nur abi) | Eichung 323 von 344 (93 %), 450 Zeilen ohne Maßstab; 344 Dubletten, 24 abgewandelte, 0 Vormerkungen; außerhalb der Geltung be-gk 101, be-lk 5, bb-gk 96, bb-ea 0; Schnitt 144 Werte |
| iqb | 37 Stapel, alle vollständig (Teil A ausgereizt, Teil B grundlegend und erhöht mit Reserve, MMS-Deltas) | 1443 | 1323 gemeinsam (708 nur iqb, 348 in beiden) | Eichung 1357 von 1442 (94 %); außerhalb der Geltung be-gk 316, be-lk 168, bb-gk 314, bb-ea 166 |

Summe 2883 Katalogzeilen in fünf Katalogdateien, 1643 Typen in drei Typenlisten.

Wo die Zahlen stehen: je Heft und Stapel in `*-pruefungen.md` § 2 (Status, Zeilen, Kennzahlen), Befunde in § 4, Änderungen in § 5; über den Bestand in der Ausgabe der Selbstprüfung jedes Bau-Skripts (leeres `ZEILEN`); tragende Zahlen je Entscheidung in konzept.md § 4 („Zahl:"); Poolquote je Heft in abi-pruefungen.md § 2, Eichung je Stapel in iqb-pruefungen.md § 4; Materiallage fhr in fhr.md § 1.

## 5 Arbeitsregeln in Kürze

- Ein Heft oder ein Stapel je Lauf, vollständig; keine Zwischenstände; CSV nie von Hand, nur über die Skripte (Feldkorrekturen über Abgleichlauf oder `TYPEN_KORREKTUR`).
- Etikettenfragen im Lauf selbst entscheiden und im Bericht nennen; Umbenennungen bestehender Typen nur im Abgleichlauf.
- Commit erst nach bestandener Selbstprüfung aller betroffenen Bau-Skripte und byteidentischem Rerun aus dem HEAD-Stand; ein Commit je Heft, Stapel, Lauf oder Auftragspunkt; Push beim Lehrer.
- Änderungslogs und Versionszeilen bei jeder Änderung nachführen (Kopfzeile jeder md- und py-Datei, § 5 bzw. § 10 der Listen).
- `hefte/`, `hefte-md/`, `iqb-pdf/` nie ins Repo.
- Eine Vormerkung überlebt keinen Auftrag; ein Profil ohne Selbstprüfung ist unvollständig.

## 6 Namen und Aliasse (Entscheidung 32)

Kurzkennungen msa = msa-bb, fhr = fhr-bb, abi = abi-bebb, iqb = abi-iqb bleiben als Aliasse; Familienname `abitur-` für das Geteilte der Familie abi; neue Dateien und neue Profile tragen die Vollform nach namensschema.md § 2 (Beispiel abi-ni, abi-ni-ga-geltung.md). Variante A (Vollform durchgängig) ist aufgeschoben.

## 7 Offenes

Stand am 17.09.2026 in konzept.md § 6 – je Punkt eine Zeile mit dem Grund des Wartens – und nur dort; hier nicht wiederholt, damit der Befund nicht mit dem geltenden Stand verwechselt wird.
