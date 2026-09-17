# CLAUDE.md – Abitur-Katalogarbeit (Profile abi und iqb)

Repo hz-0801/mathe-nachhilfe, alle Dateien flach in der Wurzel. Dieses Dokument
gilt für die Erfassung der Abiturhefte (Profil abi) und des IQB-Aufgabenpools
(Profil iqb) in den Katalog. Für MSA (Profil msa) und FHR (Profil fhr) liegen
eigene Dateien daneben; sie werden hier nicht angefasst. § 1–3 beschreiben abi;
§ 4 nennt, was für iqb anders ist – alles Übrige gilt dort gleich.

Werkzeuge auf dem Rechner des Lehrers (Windows, nichts im PATH): git aus GitHub
Desktop (`%LOCALAPPDATA%\GitHubDesktop\app-*\resources\app\git\cmd\git.exe`),
Python aus LibreOffice (`C:\Program Files\LibreOffice\program\python.exe`),
sympy und pypdf per `pip install --target` in den Scratchpad, dann `PYTHONPATH`
setzen. Kein pdftotext: Text mit pypdf, Seiten mit dem Read-Tool ansehen.

## 1 Maßgebliche Dateien

Regelwerk (lesen, nicht ohne Anlass ändern):

| Datei | Rolle |
|---|---|
| `konzept.md` | Gesamtkonzept: Ziel, Bausteine, Entscheidungen 1–26, Verworfenes. Getroffene Entscheidungen werden ohne neuen Anlass nicht wieder aufgerollt. |
| `katalog-prompt.md` | Kern der Erfassungsmethode (v0.6, Schema-Version 2): Zeilenregel, 37 Felder mit Kopfzeile, Formvokabular, Handlung je format (§ 5), Vorrang des Amtlichen für niveau_geschaetzt (§ 5), Markierungen in bemerkung („Dublette von:", Vorstufe „Poolaufgabe (nicht erfasst):" als Übergangszustand, „Abgewandelt von:", „Traegerbindung: Kontext"), Prüfung, Ausgabe je Heft. Prüfungsunabhängig; Etikettenänderungen nur im Abgleichlauf (§ 6, § 9). |
| `abi.md` | Profil abi (v0.16): Prüfung, Basis-URL, Heftaufbau, Kürzel und id-Muster, Sachgebiete (`leitidee`), Verweis auf das Vokabular, Besonderheiten beim Erfassen, Beispielzeilen, Offenes. **Bei Widerspruch zum Kern gilt das Profil.** |
| `abi-quellen.md` | Verzeichnis, Dateinamen, papier-Kürzel und Seitenzahlen der Hefte. |
| `abitur-vokabular.md` | Gemeinsames Vokabular der Profile abi und iqb (Entscheidung 25): Sachgebiete, Themenliste, Geltungstabelle, Gegenstandsklassen mit der Regel **Zeilenthema = Typthema** (§ 4), Regeln der gemeinsamen Typenliste. Beide Bau-Skripte lesen es; abi.md und iqb.md verweisen darauf. |
| `abi-aufbau.md`, `abi-struktur.json` | Zeiten, Wahlstruktur, BE-Verteilung; Zwillingsnachweis Berlin/Brandenburg über BE-Vektoren. |

Arbeitsdateien (werden je Heft geschrieben):

| Datei | Rolle |
|---|---|
| `abi-bau.py` | Gerüst für ein Heft: `KONFIG`, `ZEILEN` (ein `row(...)` je Teilaufgabe), `NEUE_TYPEN`. Liest Kopfzeile, Formvokabular und Handlung je format aus `katalog-prompt.md` § 5, Sachgebiete, Themen, Geltung und Klassen aus `abitur-vokabular.md`; prüft wie `iqb-bau.py` (Präfixregel, Zeilenthema = Typthema, Schwellen, Eichung, Vollständigkeit, Dublettenverweis) und schreibt beide CSV-Dateien nur, wenn alle Prüfungen bestehen. Der Teil unter „QUELLEN UND PRÜFUNG, NICHT ÄNDERN" bleibt unverändert. |
| `abi-katalog.csv` | Der Katalog, eine Datei für Teil A und B (das Feld `block` trennt). Semikolon, alles gequotet, UTF-8, LF. Nie von Hand editieren – nur über das Skript. |
| `abitur-typen.csv` | Gemeinsame Typenliste der Profile abi und iqb, `typ;leitidee;thema;definition;beispiel_id;status`; `beispiel_id` zeigt in einen der beiden Kataloge. Wächst nur über `NEUE_TYPEN` der Bau-Skripte; Umbenennungen und Zusammenziehungen nur über `abgleich.py` (beide Kataloge). |
| `abi-pruefungen.md` | Heftliste mit Status, Befunde je Heft (§ 4), Änderungslog (§ 5). Nach jedem Heft fortschreiben. |

Nicht maßgeblich für die Erfassung: `vorgaben.md` und `abi-vorgaben.md` (Fachbriefe, Prüfungsschwerpunkte, jährlicher Check, vom Katalog-Prompt nicht gelesen), `pruefungsprompt.md`/`masterprompt.md` (Blattbau, kommt später), die msa-/fhr-Dateien.

## 2 Wie ein Heft erfasst wird

Grundlage: `katalog-prompt.md` § 3–8, konkretisiert durch `abi.md` § 4 und § 7 und den Ablauf im Kopf von `abi-bau.py`.

1. **Heft wählen.** Der Lehrer nennt es („2017 be-gk", „weiter"); Zuordnung über `abi-pruefungen.md` § 2. Leitfassung je Jahr und Niveau: erhöht `bb-ea`, grundlegend `be-gk`. Wortgleiche Zwillinge des anderen Landes bekommen keine Zeile, nur einen Vermerk in `abi-pruefungen.md`; CAS-Hefte sind Nachtrag nach WTR. Hefte ab 2019 liegen als Scans unter `hefte/` (nicht im Repo), gemeinsame Hefte Berlin/Brandenburg tragen `bebb`. Vor dem Bau eine Zeile: Datei, Seitenzahl, Zahl der Typen in `abitur-typen.csv`.
2. **Heft holen und lesen.** PDF nach `abi-quellen.md` mit curl holen, Seitenzahl prüfen, Text aller Seiten mit Layout extrahieren (`pdftotext -layout`), jede Aufgabenseite einmal rendern und ansehen. Bei Widerspruch gilt das Bild; Werte, die nur in Abbildungen stehen, gehören in `gegeben` und `skizze`.
3. **`abi-bau.py` füllen.** `KONFIG` (jahr, papier, datei, seiten, `soll` je Aufgabe aus den BE-Tabellen – alle Aufgaben des Hefts, sonst ist es unvollständig; `soll_teil1` nur bei bb-ea; `probe` für einen Probelauf), dann `ZEILEN`: eine `row(...)` je Einheit mit eigener Punktangabe, Felder nach Kern § 5, Kürzel nach `abi.md` § 4 (id `papier-BlockAufgabeTeilaufgabe`, aufgabe wie im Heft, Teilaufgabe ein Kleinbuchstabe, `stern` leer, `afb_amtlich` nur bei amtlich ausgewiesenem Bereich, `hilfsmittel` folgt aus `block`). Aufgabenstamm in jeder Zeile wiederholen; Kontrollangaben in `gegeben` der Teilaufgabe, in der sie stehen, und durch eigene Rechnung bestätigen. Mehrere Leistungen bleiben eine Zeile: `typ` die erste, `typ_neben` die weiteren; `leitidee` und `thema` der Zeile sind die des `typ` (das Skript erzwingt es – passt das Thema nicht, ist der Typ falsch oder gehört in den Abgleichlauf). `NEUE_TYPEN` mit Definition und erster Fundstelle; Typname in Themen mit Gegenstandsklassen mit Präfix „Klasse: " (`abitur-vokabular.md` § 4). Pool-Teilaufgaben in einem Landesheft bekommen eine eigene Zeile mit dem typ der iqb-Zeile und „Dublette von: <iqb-id>." am Anfang von bemerkung; ist der Poolstapel noch nicht erfasst, stattdessen „Poolaufgabe (nicht erfasst): <voraussichtliche iqb-id>." – ein Übergangszustand, der als offener Posten in den Prüfungslisten steht, bis der Stapel erfasst ist und `abgleich.py` den Vermerk auf „Dublette von:" (wortgleich) oder „Abgewandelt von: <iqb-id>; <Unterschied>." (abgewandelt) umstellt (`abi.md` § 7). Vor dem Bau die Aufgaben gegen den Pool halten (Textvergleich, Poolquote je Heft ist Kennzahl).
4. **Ergebnisse rechnen.** Jedes rechnerische Ergebnis mit einem Skript (sympy) nachrechnen; für 2017/2018 gibt es keine amtlichen Lösungen, jede Zeile trägt „Eigene Rechnung" in `bemerkung`. Unsicheres mit „?" und Grund in `bemerkung`.
5. **Skript laufen lassen.** `abitur-vokabular.md`, `katalog-prompt.md`, `abi-katalog.csv`, `iqb-katalog.csv`, `abitur-typen.csv` liegen neben dem Skript; `python abi-bau.py`. Es prüft Pflichtfelder, Vokabular, id-Muster, Punktsummen und Vollständigkeit je Aufgabe, Typen gegen `abitur-typen.csv` samt Präfix, `abhaengig_von`, Dublettenverweise gegen `iqb-katalog.csv`, die Schwellen („?", ersatzweise, Eichung) sowie ASCII-Minus und Umlaut-Umschrift; bei einem Fehler wird nichts geschrieben. Nach dem Schreiben liest es die Datei zurück und vergleicht. Ausgabe: Prüftabelle und Bericht.
6. **Selbstprüfung.** Das Skript mit leerem `ZEILEN` laufen lassen: prüft den Gesamtbestand gegen das Vokabular, jede Typenverwendung, jede `beispiel_id` (in einem der beiden Kataloge), und dass kein Typ der gemeinsamen Liste in beiden Katalogen unbenutzt ist; schreibt nichts. Nach einem Abgleichlauf beide Bau-Skripte so laufen lassen. Bisher üblich: der Lauf wird aus einer frischen Repo-Kopie wiederholt und muss byteidentisch sein.
7. **Nachführen.** `abi-pruefungen.md`: Status „erfasst JJJJ-MM-TT, n Zeilen", Kennzahlenzeile in § 2, Befunde in § 4, Zeile im Änderungslog § 5. Themenlücken in `abi.md` § 6 ergänzen, wenn das Heft Neues gebracht hat; Änderungen an Themenliste oder Klassen nur in `abitur-vokabular.md` (gilt für beide Profile); dann Versionszeile anpassen.
8. **Bericht im Chat**, je Element eine Zeile: Punktprüfung Soll/Ist je Aufgabe, neue Typen mit Definition, Vorschläge zur Typenliste, unsichere Zeilen mit Grund, nicht lesbare Abbildungen, Themen, die nicht passten. Danach nichts weiter; das nächste Heft kommt auf „weiter".

## 3 Arbeitsregeln

- **Ein Heft je Lauf.** Ein Lauf erfasst genau ein Heft vollständig – alle Aufgaben, beide Wahlwege. Nicht zwei Hefte in einem Lauf, kein halbes Heft.
- **Keine Zwischenstände.** Katalog, Typenliste und Heftliste werden erst geschrieben, wenn das ganze Heft in `ZEILEN` steht und das Skript ohne Fehler durchläuft. Keine Teil-CSVs, keine vorläufigen Zeilen, keine handeditierten CSV-Dateien.
- **Etikettenfragen selbst entscheiden.** Ob ein vorhandener Typ passt oder ein neuer nötig ist, wie er heißt, welches Thema bei einer Lücke der Themenliste das nächstliegende ist – das wird im Lauf entschieden und nicht zurückgefragt. Maßstab: Kern § 6 (gleiche Fertigkeit → gleiches Etikett, anderer Lösungsweg → trennen; Gegenstand plus Handlung, keine Synonyme). Die Entscheidung steht in `bemerkung` der Zeile bzw. im Bericht; Umbenennungen bestehender Typen kommen ins Änderungslog von `abi-pruefungen.md`.
- **Commit erst nach bestandener Selbstprüfung.** Committet wird, wenn (a) der Heftlauf „Alle Prüfungen bestanden." gemeldet hat, (b) die Selbstprüfung über den Gesamtbestand fehlerfrei ist und (c) `abi-pruefungen.md` nachgeführt ist. Ein Commit je Heft.
- Fakten von Deutung trennen: Deutung nur in `niveau_geschaetzt`, `fehlerquelle`, `bemerkung`. Kein Volltext im Katalog; Wortlaut und Bild holt später nur der Blatt-Prompt.
- Häufigkeit eines Typs ist Auskunft, keine Priorität; ein einziges Vorkommen ist ein vollwertiger Typ.
- Sprache und Zeichen: Deutsch, echte Umlaute und ß in allen Textfeldern (nur `id`, `papier`, `abhaengig_von` sind umlautfrei), Unicode-Minus „−" statt Bindestrich vor Zahlen, Dezimalkomma wie im Heft.

## 4 Profil iqb – was anders ist

Regelwerk: `iqb.md` (Profil, bei Widerspruch zum Kern gilt es), `abitur-vokabular.md` (gemeinsam mit abi), `iqb-quellen.md` und `iqb-quellen.csv` (alle 624 Kennungen mit Zerlegung, papier, Stapel, Seitenzahl und Dublettenverweis; erzeugt von `iqb-quellen.py`, `iqb-bau.py` liest die CSV). Arbeitsdateien: `iqb-bau.py`, `iqb-katalog.csv`, `abitur-typen.csv` (gemeinsam mit abi, bis 15.09.2026 `iqb-typen.csv`), `iqb-pruefungen.md` (Stapelliste, Befunde, Änderungslog). Entscheidungen: `konzept.md` Nr. 23–25.

- **Ein Stapel je Lauf statt ein Heft.** Eine Poolaufgabe ist kein Heft; die Einheit ist der Stapel = Prüfungsteil eines Pooljahrs auf einem Niveau (Spalte `stapel`, z. B. `2026-ga-A`, 10–20 Dateien, 25–50 Zeilen). Der Lehrer nennt ihn („2026 ga", „weiter" = nächster in `iqb-pruefungen.md` § 2). Reihenfolge: Teil A vollständig, jüngstes Jahr zuerst, grundlegend vor erhöht, Beispielaufgaben zuletzt; Teil B liegt.
- **Holen und lesen.** Je Datei `curl` nach `iqb-quellen.md` § 4, zwei Seiten in Teil A. Die Datei enthält Aufgabe, Erwartungshorizont, Standardbezug und Bewertungshinweise. Formeln sind Bilder: jede Seite rendern. Reihenfolge je Aufgabe: Aufgabe lesen und `niveau_geschaetzt` festlegen, erst dann Erwartungshorizont und Standardbezug lesen (`iqb.md` § 7).
- **`iqb-bau.py` füllen.** `KONFIG` (`stapel`, `soll` je Kennung aus der BE-Summe, `probe`), dann `row(kennung, teilaufgabe, ...)`: id, jahr, papier, block, aufgabe, titel, stern und hilfsmittel leitet das Skript aus der Kennung ab (`iqb.md` § 4), nicht übergeben. Aufgaben ohne Buchstaben: `row(kennung, ...)` ohne teilaufgabe, eine Zeile, id gleich Kennung. Dateien mit `dublette_von` (wortgleich unter beiden AG/LA-Alternativen) bekommen keine Zeile und kein Soll – `dublette_von` ist nur eine Spalte von `iqb-quellen.csv` (Datei zeigt auf Datei), kein Katalogfeld; der Zeilenverweis „Dublette von: <id>." in `bemerkung` ist etwas anderes (Kern § 5, abi.md § 7). `afb_amtlich` aus dem Standardbezug mit allen vorkommenden Bereichen (`I|II`), die Matrixzeile nach `bemerkung` („Standardbezug: K1 I, K2 II, K5 II"). `ergebnis` amtlich aus dem Erwartungshorizont mit „(amtlich)", eigene Rechnung mit sympy als Kontrolle. Kein passendes Thema: nächstliegendes wählen und „ersatzweise" in `bemerkung`. Die Typenliste ist mit abi geteilt; ein Etikett gilt für beide Profile.
- **Qualitätsschranke im Skript.** `SCHWELLEN` in `iqb-bau.py` (`iqb.md` § 7): Zeilen mit „?", Anteil neuer Typen, Zeilen ohne passendes Thema. Reißt eine Schranke, werden Etiketten und Rechnungen geprüft und der Lauf wiederholt; erst wenn das nicht hilft, wird der Wert im Skript geändert und in `iqb-pruefungen.md` § 5 begründet. Die Eichschwelle gilt für jeden Stapel gleich (die Überschreibung je Stapel aus iqb-bau.py v1.4 ist mit v1.5 zurückgebaut); eine aus einer Landeszeile übernommene Schätzung, die vom Standardbezug abweicht, wird korrigiert, nicht die Schwelle (Vorrang des Amtlichen, Kern § 5). `probe: True` prüft alles und schreibt nichts; damit wird eine einzelne Aufgabe ausprobiert, ohne einen Zwischenstand zu erzeugen.
- **Stapel vollständig.** Das Skript vergleicht die Dateien in `ZEILEN` mit `iqb-quellen.csv` und schreibt nur, wenn jede Datei des Stapels da ist und jede Punktsumme stimmt. Die Selbstprüfung (leeres `ZEILEN`) prüft zusätzlich, dass jeder angefangene Stapel im Bestand vollständig ist, und gibt die Eichung über den Bestand aus.
- **Typname mit Gegenstandsklasse** (Entscheidung 24, `abitur-vokabular.md` § 4; seit Entscheidung 25 auch für abi): Bei Themen mit Klassenliste beginnt der Typname mit der Klasse und Doppelpunkt („Matrizenalgebra: Alle Fixvektoren einer Matrix ermitteln"), bei allen anderen ohne Präfix; maßgeblich ist das Thema des Typs in `abitur-typen.csv`. Beide Skripte prüfen das. Der Schnitt Thema × Klasse × Handlung (Thema des Typs, Handlung aus dem ersten `format`-Wert nach Kern § 5) ist die Einheit für den Blattbau; der Typ nach Kern § 6 bleibt Feinetikett.
- **Abgleichlauf nach jedem Stapel** (Kern § 9): Etiketten des Stapels gegen `abitur-typen.csv` vereinheitlichen; Umbenennungen und Zusammenziehungen nur über `abgleich.py` (Regeln im Skript, zieht beide Kataloge mit, danach Selbstprüfung beider Bau-Skripte), Liste alt → neu in `iqb-pruefungen.md` bzw. `abi-pruefungen.md` § 5. Commit je Stapel nach bestandener Selbstprüfung; Nachführen wie bei abi, dazu die Eichungsquote in `iqb-pruefungen.md` § 4.
