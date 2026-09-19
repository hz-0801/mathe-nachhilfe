# Auftrag: Quellentexte Sek II neu umwandeln

## Ausgangslage

Commit fa866ee hat acht Quellentexte mit pypdf umgewandelt. pypdf
zerlegt Wörter („Fertigk eiten", „Unt erricht"); in vier der acht
Dateien ist ein Fünftel der Wörter betroffen. Die Werkstatt hat die
PDF mit `pdftotext -layout` (poppler) umgewandelt und die Wortzahlen
festgehalten. Die acht Dateien werden mit poppler oder, wenn das
nicht geht, mit PyMuPDF neu erzeugt. `quellen.md` und `README.md`
bleiben, bis auf die Werkzeugangabe.

## Schritte

1. poppler beschaffen. Reihenfolge, beim ersten Erfolg aufhören:
   a) `pdftotext -v` – falls doch vorhanden.
   b) `winget install --id oschwartz10612.Poppler -e` und danach
      den Ordner `Library\bin` des installierten Pakets in den PATH
      der Sitzung nehmen.
   c) `pip install pymupdf` und Umwandlung mit
      `page.get_text("text")` je Seite, Seiten durch `\f` getrennt.
   Im Bericht nennen, welcher Weg lief.

2. Die acht PDF aus `archiv/auftrag-quellen-sek2-2026-09-19.md`
   (Schritt 1 dort) erneut laden und umwandeln; die Berliner Datei
   ist passwortlos AES-verschlüsselt (pdftotext liest sie direkt;
   bei PyMuPDF `doc.authenticate("")`). Zieldateinamen wie dort.
   Die Formelsammlung wie dort auf Teil 1 Mathematik zuschneiden.
   Die acht vorhandenen Dateien überschreiben. PDF danach löschen.

3. Wortzahlen prüfen (Wörter = durch Leerraum getrennte Zeichen-
   folgen, `len(text.split())`). Erwartung aus der Werkstatt:

   quelle-rlp-gost-bb-2022-mathematik.txt · 7182
   quelle-rlp-gost-be-2022-mathematik.txt · 11204
   quelle-rlp-gost-2022-mathematik-anlage-ohimi.txt · 1033
   quelle-rlp-fos-bb-2019-mathematik.txt · 7016
   quelle-iqb-formelsammlung-2024-mathematik.txt · 1789
   quelle-iqb-operatoren-2019.txt · 352
   quelle-iqb-vereinbarungen-2022.txt · 736
   quelle-iqb-struktur-2024.txt · 688

   Bei pdftotext Abweichung bis 2 %, bei PyMuPDF bis 5 %.

4. Wortzerlegung prüfen: In keiner der acht Dateien darf eines
   dieser Bruchstücke vorkommen: „k eiten", „Unt erricht",
   „Herau sgeber", „Inhalts verzeichnis", „creativecomm ons".

5. In `quellen/quellen.md` die Zeile „Erzeugt am 19.09.2026 mit
   `pdftotext -layout`." im Abschnitt Sekundarstufe II auf das
   tatsächliche Werkzeug setzen (bei PyMuPDF: „mit PyMuPDF
   (Wörter unzerlegt; Spaltenlayout kann von den Sek-I-Texten
   abweichen)").

6. `fhr/fhr.md` § 9: nach dem Satz, der „[IQB-Pool]" enthält, als
   eigene Zeile anfügen:
   „[IQB-Pool]: IQB, Abituraufgabenpools,
   https://www.iqb.hu-berlin.de/de/schule/sekundarstufe-ii/abituraufgabenpools/"

7. Falls `CLAUDE.md` eine Werkzeugregel für PDF-Umwandlung enthält,
   dort ergänzen: „Quellentexte für `quellen/` mit pdftotext
   -layout (poppler) erzeugen; pypdf zerlegt Wörter und ist dafür
   nicht geeignet." Enthält `CLAUDE.md` keine solche Regel, nichts
   ändern und im Bericht sagen, wo die pypdf-Konvention steht.

8. Diese Auftragsdatei nach
   `archiv/auftrag-quellen-sek2-neu-2026-09-19.md` verschieben
   (git mv).

9. Ein Commit: „Quellentexte Sek II neu umgewandelt (poppler)".

## Prüfungen

- Schritte 3 und 4 bestanden; sonst abbrechen und melden, ohne
  zu committen.
- Acht Dateien UTF-8, LF, kein BOM. Keine PDF im Repo.
- Außer `quellen/`, `fhr/fhr.md`, `CLAUDE.md`, `archiv/` nichts
  geändert.

## Bericht (zurück in den Chat)

- Welcher Weg aus Schritt 1 lief.
- Je Datei Wortzahl und Abweichung; Ergebnis der Bruchstückprüfung.
- Ob und wo `CLAUDE.md` geändert wurde.
- Commit-Hash.
- Letzte Zeile: „Push origin drücken".

## Regeln

- Textfassungen nicht nachbearbeiten außer dem Zuschnitt der
  Formelsammlung.
- Bei Unklarheit die einfachste Lesart wählen und im Bericht
  nennen, nicht rückfragen.
