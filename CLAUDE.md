# CLAUDE.md – Abitur-Katalogarbeit (Profil abi)

Repo hz-0801/mathe-nachhilfe, alle Dateien flach in der Wurzel. Dieses Dokument
gilt für die Erfassung der Abiturhefte in den Katalog. Für MSA (Profil msa) und
FHR (Profil fhr) liegen eigene Dateien daneben; sie werden hier nicht angefasst.

## 1 Maßgebliche Dateien

Regelwerk (lesen, nicht ohne Anlass ändern):

| Datei | Rolle |
|---|---|
| `konzept.md` | Gesamtkonzept: Ziel, Bausteine, Entscheidungen 1–22, Verworfenes. Getroffene Entscheidungen werden ohne neuen Anlass nicht wieder aufgerollt. |
| `katalog-prompt.md` | Kern der Erfassungsmethode (v0.3, Schema-Version 2): Zeilenregel, 37 Felder mit Kopfzeile, Formvokabular, Prüfung, Ausgabe je Heft. Prüfungsunabhängig. |
| `abi.md` | Profil abi (v0.5): Prüfung, Basis-URL, Heftaufbau, Kürzel und id-Muster, Sachgebiete (`leitidee`), Themenliste, Besonderheiten beim Erfassen, Beispielzeilen, Offenes. **Bei Widerspruch zum Kern gilt das Profil.** |
| `abi-quellen.md` | Verzeichnis, Dateinamen, papier-Kürzel und Seitenzahlen der Hefte. |
| `abi-aufbau.md`, `abi-struktur.json` | Zeiten, Wahlstruktur, BE-Verteilung; Zwillingsnachweis Berlin/Brandenburg über BE-Vektoren. |

Arbeitsdateien (werden je Heft geschrieben):

| Datei | Rolle |
|---|---|
| `abi-bau.py` | Gerüst für ein Heft: `KONFIG`, `ZEILEN` (ein `row(...)` je Teilaufgabe), `NEUE_TYPEN`. Liest Kopfzeile und Formvokabular aus `katalog-prompt.md` § 5, Sachgebiete und Themen aus `abi.md` § 5–6; schreibt beide CSV-Dateien nur, wenn alle Prüfungen bestehen. Der Teil unter „QUELLEN UND PRÜFUNG, NICHT ÄNDERN" bleibt unverändert. |
| `abi-katalog.csv` | Der Katalog, eine Datei für Teil A und B (das Feld `block` trennt). Semikolon, alles gequotet, UTF-8, LF. Nie von Hand editieren – nur über das Skript. |
| `abi-typen.csv` | Typenliste `typ;leitidee;thema;definition;beispiel_id;status`. Wächst nur über `NEUE_TYPEN`. |
| `abi-pruefungen.md` | Heftliste mit Status, Befunde je Heft (§ 4), Änderungslog (§ 5). Nach jedem Heft fortschreiben. |

Nicht maßgeblich für die Erfassung: `vorgaben.md` (Fachbriefe, jährlicher Check, vom Katalog-Prompt nicht gelesen), `pruefungsprompt.md`/`masterprompt.md` (Blattbau, kommt später), die msa-/fhr-Dateien.

## 2 Wie ein Heft erfasst wird

Grundlage: `katalog-prompt.md` § 3–8, konkretisiert durch `abi.md` § 4 und § 7 und den Ablauf im Kopf von `abi-bau.py`.

1. **Heft wählen.** Der Lehrer nennt es („2017 be-gk", „weiter"); Zuordnung über `abi-pruefungen.md` § 2. Leitfassung je Jahr und Niveau: erhöht `bb-ea`, grundlegend `be-gk`. Wortgleiche Zwillinge des anderen Landes bekommen keine Zeile, nur einen Vermerk in `abi-pruefungen.md`; CAS-Hefte sind Nachtrag nach WTR. Vor dem Bau eine Zeile: Datei, Seitenzahl, Zahl der Typen in `abi-typen.csv`.
2. **Heft holen und lesen.** PDF nach `abi-quellen.md` mit curl holen, Seitenzahl prüfen, Text aller Seiten mit Layout extrahieren (`pdftotext -layout`), jede Aufgabenseite einmal rendern und ansehen. Bei Widerspruch gilt das Bild; Werte, die nur in Abbildungen stehen, gehören in `gegeben` und `skizze`.
3. **`abi-bau.py` füllen.** `KONFIG` (jahr, papier, datei, seiten, `soll` je Aufgabe aus den BE-Tabellen; `soll_teil1` nur bei bb-ea), dann `ZEILEN`: eine `row(...)` je Einheit mit eigener Punktangabe, Felder nach Kern § 5, Kürzel nach `abi.md` § 4 (id `papier-BlockAufgabeTeilaufgabe`, aufgabe zweistufig, Teilaufgabe ein Kleinbuchstabe, `stern` und `afb_amtlich` leer, `hilfsmittel` folgt aus `block`). Aufgabenstamm in jeder Zeile wiederholen; Kontrollangaben in `gegeben` der Teilaufgabe, in der sie stehen, und durch eigene Rechnung bestätigen. Mehrere Leistungen bleiben eine Zeile: `typ` die erste, `typ_neben` die weiteren. `NEUE_TYPEN` mit Definition und erster Fundstelle.
4. **Ergebnisse rechnen.** Jedes rechnerische Ergebnis mit einem Skript (sympy) nachrechnen; für 2017/2018 gibt es keine amtlichen Lösungen, jede Zeile trägt „Eigene Rechnung" in `bemerkung`. Unsicheres mit „?" und Grund in `bemerkung`.
5. **Skript laufen lassen.** `abi.md`, `katalog-prompt.md`, `abi-katalog.csv`, `abi-typen.csv` liegen neben dem Skript; `python abi-bau.py`. Es prüft Pflichtfelder, Vokabular, id-Muster, Punktsummen je Aufgabe, Typen gegen `abi-typen.csv`, `abhaengig_von`, ASCII-Minus und Umlaut-Umschrift; bei einem Fehler wird nichts geschrieben. Nach dem Schreiben liest es die Datei zurück und vergleicht. Ausgabe: Prüftabelle und Bericht.
6. **Selbstprüfung.** Das Skript mit leerem `ZEILEN` laufen lassen: prüft den Gesamtbestand beider CSV-Dateien gegen das Vokabular, jede Typenverwendung, jede `beispiel_id`, und dass kein Typ unbenutzt ist; schreibt nichts. Bisher üblich: der Lauf wird aus einer frischen Repo-Kopie wiederholt und muss byteidentisch sein.
7. **Nachführen.** `abi-pruefungen.md`: Status „erfasst JJJJ-MM-TT, n Zeilen", Befunde in § 4, Zeile im Änderungslog § 5. Themenlücken und Typenstand in `abi.md` § 6–7 ergänzen, wenn das Heft Neues gebracht hat; dann Versionszeile oben in `abi.md` anpassen.
8. **Bericht im Chat**, je Element eine Zeile: Punktprüfung Soll/Ist je Aufgabe, neue Typen mit Definition, Vorschläge zur Typenliste, unsichere Zeilen mit Grund, nicht lesbare Abbildungen, Themen, die nicht passten. Danach nichts weiter; das nächste Heft kommt auf „weiter".

## 3 Arbeitsregeln

- **Ein Heft je Lauf.** Ein Lauf erfasst genau ein Heft vollständig – alle Aufgaben, beide Wahlwege. Nicht zwei Hefte in einem Lauf, kein halbes Heft.
- **Keine Zwischenstände.** Katalog, Typenliste und Heftliste werden erst geschrieben, wenn das ganze Heft in `ZEILEN` steht und das Skript ohne Fehler durchläuft. Keine Teil-CSVs, keine vorläufigen Zeilen, keine handeditierten CSV-Dateien.
- **Etikettenfragen selbst entscheiden.** Ob ein vorhandener Typ passt oder ein neuer nötig ist, wie er heißt, welches Thema bei einer Lücke der Themenliste das nächstliegende ist – das wird im Lauf entschieden und nicht zurückgefragt. Maßstab: Kern § 6 (gleiche Fertigkeit → gleiches Etikett, anderer Lösungsweg → trennen; Gegenstand plus Handlung, keine Synonyme). Die Entscheidung steht in `bemerkung` der Zeile bzw. im Bericht; Umbenennungen bestehender Typen kommen ins Änderungslog von `abi-pruefungen.md`.
- **Commit erst nach bestandener Selbstprüfung.** Committet wird, wenn (a) der Heftlauf „Alle Prüfungen bestanden." gemeldet hat, (b) die Selbstprüfung über den Gesamtbestand fehlerfrei ist und (c) `abi-pruefungen.md` nachgeführt ist. Ein Commit je Heft.
- Fakten von Deutung trennen: Deutung nur in `niveau_geschaetzt`, `fehlerquelle`, `bemerkung`. Kein Volltext im Katalog; Wortlaut und Bild holt später nur der Blatt-Prompt.
- Häufigkeit eines Typs ist Auskunft, keine Priorität; ein einziges Vorkommen ist ein vollwertiger Typ.
- Sprache und Zeichen: Deutsch, echte Umlaute und ß in allen Textfeldern (nur `id`, `papier`, `abhaengig_von` sind umlautfrei), Unicode-Minus „−" statt Bindestrich vor Zahlen, Dezimalkomma wie im Heft.
