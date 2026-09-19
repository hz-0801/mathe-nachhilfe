# Übergabe 2026-09-19a

Zuerst dieses Zip hochladen.

## 1 Ziel

Ein geprüfter Themenkatalog, aus dem Masterprompt und Prüfungsprompt Arbeitsblätter bauen, statt je Thema selbst zu planen. Sek I liegt vor; Sek II folgt über die Prüfungskataloge fhr, abi und iqb. Der Lehrer hat gerade Zeit und ein Max-Abo und will das Zeitintensive jetzt erledigen; ob der Katalog trägt, wird der Testlauf zeigen, den er bewusst verschiebt.

## 2 Arbeitsgrundlage

- GitHub `hz-0801/mathe-nachhilfe`, Commit 24d4412 (19.09.2026). Seit dem Umbau in Ordnern: `msa/`, `fhr/`, `abitur/` (abi und iqb zusammen), `katalog/` (Themenkatalog Sek I, 29 Einträge, Stand 11j), `quellen/` (RLP, LISUM-Planungshilfen, Klett-Fahrplan als Text), `werkzeuge/`, `archiv/`. Wurzel: `README.md` (einzige Landkarte), `CLAUDE.md` (Erfassungsregeln), `katalog-prompt.md`, `konzept.md` (§ 3 Themenkatalog neu), `blatt-konzept.md`, `faellig.md`. Ein Chat mit Shell klont es; ein Chat ohne Shell holt Dateien per Raw-URL `https://raw.githubusercontent.com/hz-0801/mathe-nachhilfe/main/<ordner>/<datei>` – die Adresse muss dafür als Text in der Nachricht stehen.
- GitHub `hz-0801/blattbau`, Commit 007981b: `masterprompt.md` v3.35, `pruefungsprompt.md` v0.15, `mathblatt.sty` 07d, `Anleitung_mathblatt.md`, `CHANGELOG.md`, Testauswertungen. Abruf-URLs in beiden Prompts zeigen bereits auf die neuen Orte.
- Das Lieferzip enthält nur diese Übergabe. Der Themenkatalog liegt im Repo, nicht mehr im Zip.
- Prüfungskataloge (Zeilen / Themen): msa 393 / 25, fhr 253 / 28, abi 794 / 43, iqb 1443 / 47. Alle vier Bau-Skripte bestehen die Selbstprüfung.
- Claude Code läuft auf dem Rechner des Lehrers im lokalen Clone; GitHub Desktop für Push. Aufträge an Claude Code als md-Datei ins Repo legen, Modell Opus.

## 3 Arbeitsstand

Umbau des Repos am 19.09.2026 durch Claude Code eingespielt: 59 Dateien verschoben mit erhaltener Geschichte, Themenkatalog erstmals im Repo, Blattbau ausgelagert, Befunde und `namensschema.md` archiviert. Drei Pfade in `katalog/_pruef_*.py` korrigiert. Am Themenkatalog selbst ist seit 11j nichts geändert; Kennzahl 1 steht auf 0 von 29, weil [FS] offen ist.

Neu seit 12a: `konzept.md` § 3 hält Zweck und Arbeitsteilung des Themenkatalogs fest (Stoffbeschreibung, beide Prompts lesen ihn, Decke kommt vom Prüfungskatalog, ein Eintrag je Thema über alle Prüfungsarten). Die drei Quellentexte liegen im Repo. Globale Anweisung des Lehrers überarbeitet (Rangfolge, kein Prozessbericht, Recherche ohne Rückfrage).

Befund am Rand: Die Bau-Skripte `fhr-bau.py`, `abi-bau.py`, `iqb-bau.py` tragen im Repo noch die `row()`-Zeilen ihres letzten Hefts; die Selbstprüfung läuft nur mit geleertem ZEILEN. War vor dem Umbau so, kein Umbau-Fehler.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Reihenfolge des Lehrers vom 19.09.: Jetzt entsteht, was viel Modellzeit kostet und formunabhängig ist – Prüfungskataloge, Themenkonkordanz, Rohdateien je Thema. Formabhängige Arbeit (fertige Sek-II-Einträge, Kastenform) später. Der Testlauf mit einem gebauten Blatt ist bewusst verschoben; nicht wieder darauf drängen.
- Themenkatalog ist Stoffbeschreibung, kein Bauplan (`konzept.md` § 3). Ein Eintrag je Thema, prüfungsartübergreifend; die Decke je Prüfungsart liefert der Prüfungskatalog.
- Die vier Prüfungskataloge benennen denselben Stoff verschieden (fhr/abi: 1 von 28 Themen namensgleich). Ohne Konkordanz kann kein Skript Originale eines Themas zusammenführen.
- Repo-Struktur: Ordner je Profil, Dateinamen mit Präfix unverändert, README einzige Landkarte, Landkarte-Regel nur noch auf README (CLAUDE.md § 3). Ausgabeordner `hefte/`, `hefte-md/`, `korpus/`, `baende/`, `iqb-pdf/` bleiben lokal.
- Formelsammlung: P10-Formelblatt nicht öffentlich; ab Abitur 2025 in Berlin nur die IQB-Formelsammlung (Fachbrief Nr. 8; für Brandenburg plausibel, nicht in einer Brandenburger Vorschrift belegt; FHR ungeklärt). IQB-Notation weicht im Sek-I-Teil von der Katalognotation ab (Katheten u, v, w; Winkel φ; Mantellinie m); die Analysis-Notation ist Standard, dort nichts zu entscheiden.
- Kastenkriterium (erarbeitet, noch in keiner Datei): Formel, wenn alle Buchstaben gleichrangig sind oder ihre Stellung die Rolle erklärt, und wenn sie kürzer zu lesen ist als ein Beispiel. Drei Kastensorten: Merkformel, Musterformel, Variationsfeld (vollständiger Satz, nicht kürzbar, Reihenfolge trägt). Reihenfolgebedingung nach Padberg und Marton: das geschlossene System gehört ans Ende einer Themenfolge, nicht auf das Blatt der ersten Einheit.
- LISUM zum 31.12.2024 aufgelöst; Nachfolger LIBRA (BB) und BLiQ (BE); Abituraufgaben seit 2026 getrennt. Der Lehrer hat Schüler aus beiden Ländern.
- Modelle: Fable für Urteilsarbeit im Chat (Konkordanz, Kastenform, Sparring), Opus für Claude Code. Aufwand Mittel.
- Kommerzielle Nutzung: Werkzeug für die eigene Arbeit; ein Produkt scheitert vorerst an Rechten (Verlagsscans, LISUM CC BY-SA ShareAlike) und Reichweite.

## 5 Offene Punkte und verworfene Ansätze

Offen, Lehrer:
1. Kastenform: Abschnittsverweis streichen? Zahlenbeispiele im Kasten oder als Musterbeispiel in Aufgabe 1? Nachschlagewerk (Masterprompt 3.1) oder Merkhilfe (Katalog)? Fällt der Verweis, sind `_formelsammlung.md` und der [FS]-Punkt in 29 Einträgen zu streichen – als Rücknahme kennzeichnen.
2. Mechanik-Punkte Sek I: A4 breit oder eng; zehn fehlende Prüflisten nachtragen oder Prüfliste streichen; Prüflistenzeilen 10 und 11.
3. IQB-Regel für Brandenburg und FHR belegen (vor dem Sek-II-Schritt).

Offen, Werkstatt:
4. MzDuF-Download (LISUM, CC BY-SA 4.0, je Leitidee eine große PDF) nicht gefunden.
5. Rohdatei-Skript je Thema (nach der Konkordanz).
6. `katalog/_quellen.md` nennt die Planungshilfen noch unter dem alten Namen ohne `quelle-`; Cornelsen-Angabe unter [FS] für Sek II hinfällig, für Sek I unbelegt.

Verworfen:
- P10-Formelblatt beschaffen – nicht öffentlich.
- Weitere Erklärquellen neben Serlo – Notation läuft ohnehin gegen Serlo; echte Lücke bei Sprossen/Grundvorstellungen, aber kein Anlass vor dem Test.
- Kasten nur bei vergessbarer Formel – zu eng (Bruchregeln, Distributivgesetz).
- Bruchaddition und -multiplikation im Kasten trennen – Befund betrifft die Sequenz, nicht die Gegenüberstellung.
- Eigener Themenkatalog je Prüfungsart – ein Eintrag über alle (konzept.md § 3).
- Shell-Skript zum Einspielen – ersetzt durch md-Auftrag an Claude Code, der auch prüft und repariert.

## 6 Nächster Arbeitsschritt

Themenkonkordanz (Stufe 0). Ein Skript zieht alle Themennamen aus `msa/msa-typen.csv`, `fhr/fhr-typen.csv` und `abitur/abitur-typen.csv` (deckt abi und iqb) samt Typenzahl und schlägt Zusammenführungen vor; der Lehrer bestätigt per Auswahl. Ergebnis `themen.csv` in der Repo-Wurzel: kanonischer Name, Alias je Profil, Typenzahl je Profil. Sek-I-Themen aus `katalog/` sind die Referenz für Namen. Vorher nichts anderes anfangen. Danach Stufe 1, das Rohdatei-Skript.
