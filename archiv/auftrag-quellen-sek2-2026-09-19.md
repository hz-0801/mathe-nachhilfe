# Auftrag: Quellentexte Sekundarstufe II

## Ausgangslage

`quellen/` enthält die drei Quellentexte der Sek-I-Einträge. Für
die Sek-II-Einträge fehlen Rahmenlehrpläne, FOS-Plan und die
IQB-Dokumente. Die Werkstatt hat am 19.09.2026 die amtlichen
Adressen ermittelt und die Umwandlung geprüft. Dieser Auftrag holt
die acht PDF, wandelt sie mit `pdftotext -layout` um, legt sie
nach dem Muster von `quellen/` ab und trägt sie in
`quellen/quellen.md` und `README.md` ein.

## Schritte

1. Im Ordner `quellen/` die acht PDF laden und umwandeln. Je Zeile:
   Zieldatei, Adresse, erwartete Zeilenzahl der Textfassung
   (Abweichung bis 5 % ist in Ordnung, darüber im Bericht nennen).

   quelle-rlp-gost-bb-2022-mathematik.txt · 1371
   https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/rahmenlehrplaene/gymnasiale_oberstufe/curricula/2022/Teil_C_RLP_GOST_2022_Mathematik.pdf

   quelle-rlp-gost-be-2022-mathematik.txt · 1793
   https://www.berlin.de/sen/bildung/unterricht/faecher-rahmenlehrplaene/rahmenlehrplaene/rahmenlehrplan-mathematik_go-teil-c.pdf?ts=1684146742

   quelle-rlp-gost-2022-mathematik-anlage-ohimi.txt · 288
   https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/rahmenlehrplaene/gymnasiale_oberstufe/curricula/2022/Teil_C_RLP_GOST_2022_Mathematik_Anlage_OHiMi.pdf

   quelle-rlp-fos-bb-2019-mathematik.txt · 1283
   https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/rahmenlehrplaene/berufliche_bildung/bb/Mathematik-RLP_FOS_2019_Brandenburg.pdf

   quelle-iqb-formelsammlung-2024-mathematik.txt · 445 (siehe 2)
   https://www.iqb.hu-berlin.de/media/documents/N_Mathematisch-naturwissenschaftliche_Formelsammlung.pdf

   quelle-iqb-operatoren-2019.txt · 51
   https://www.iqb.hu-berlin.de/media/documents/M_Grundstock_von_Operatoren.pdf

   quelle-iqb-vereinbarungen-2022.txt · 157
   https://www.iqb.hu-berlin.de/media/documents/M_Inhaltliche_Vereinbarungen_zur_Gestaltung_der_Aufgaben.pdf

   quelle-iqb-struktur-2024.txt · 143
   https://www.iqb.hu-berlin.de/media/documents/M_Beschreibung_der_Struktur_der_Aufgaben.pdf

   Befehl je Datei: `pdftotext -layout <pdf> <txt>`. Die PDF nach
   der Umwandlung nicht ins Repo legen (löschen ist hier erlaubt,
   weil sie nie eingecheckt waren).

2. Von der Formelsammlung nur Teil 1 Mathematik behalten: die
   Textfassung endet vor der Zeile, die im Fließtext (nicht im
   Inhaltsverzeichnis) mit „2" beginnt und „Chemie" enthält. Das
   sind etwa 445 Zeilen; die gesamte Umwandlung hat etwa 4408.

3. In `quellen/quellen.md` nach dem Abschnitt
   `## quelle-lisum-planungshilfen-7bis10.txt` und vor
   `## Noch nicht abgelegt` die folgenden Abschnitte einfügen,
   wortgleich:

   ## Sekundarstufe II (abgelegt 19.09.2026)

   Erzeugt am 19.09.2026 mit `pdftotext -layout`. Berlin und
   Brandenburg führen seit 2022 verschiedene Fachteile C für
   Mathematik: Berlin den Plan von 2014, Brandenburg den von 2018,
   jeweils mit den neuen Teilen A und B von 2021/2022. Nur der
   Brandenburger Plan hat Lineare Algebra (Q1).

   ## quelle-rlp-gost-bb-2022-mathematik.txt  [RLP-GOST-BB]

   Rahmenlehrplan für die gymnasiale Oberstufe, Teil C Mathematik,
   Land Brandenburg. Herausgeber MBJS 2022; Inhalt des Plans vom
   01.08.2018; gültig ab 2022/23 (Einführungsphase) und 2023/24
   (Qualifikationsphase). 32 Seiten. Kurshalbjahre: Q1 Analysis
   und Lineare Algebra, Q2 Analysis und Stochastik, Q3 Analytische
   Geometrie, Q4 Analysis, Stochastik, komplexe Aufgaben.
   Lizenz CC BY-ND 4.0.

   Quelle: https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/rahmenlehrplaene/gymnasiale_oberstufe/curricula/2022/Teil_C_RLP_GOST_2022_Mathematik.pdf

   ## quelle-rlp-gost-be-2022-mathematik.txt  [RLP-GOST-BE]

   Rahmenlehrplan für die gymnasiale Oberstufe, Teil C Mathematik,
   Berlin. Herausgeber SenBJF 2022; Inhalt des Plans „gültig ab
   1. August 2014"; Teile A und B 2021. Kurshalbjahre: Q1
   Differentialrechnung, Q2 Integralrechnung, Q3 Analytische
   Geometrie, Q4 Analysis. Lizenz CC BY-ND 4.0.

   Quelle: https://www.berlin.de/sen/bildung/unterricht/faecher-rahmenlehrplaene/rahmenlehrplaene/rahmenlehrplan-mathematik_go-teil-c.pdf?ts=1684146742

   ## quelle-rlp-gost-2022-mathematik-anlage-ohimi.txt  [RLP-GOST-OHIMI]

   Anlage zum Rahmenlehrplan GOST Teil C Mathematik: Inhalte, die
   ohne Hilfsmittel beherrscht werden müssen (Algebra, Analysis,
   Analytische Geometrie, Stochastik). 12 Seiten, 2022, CC BY-ND
   4.0. Grundlage für Prüfungsteil A.

   Quelle: https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/rahmenlehrplaene/gymnasiale_oberstufe/curricula/2022/Teil_C_RLP_GOST_2022_Mathematik_Anlage_OHiMi.pdf

   ## quelle-rlp-fos-bb-2019-mathematik.txt  [RLP-FOS]

   Rahmenlehrplan Fachoberschule Mathematik, Land Brandenburg,
   MBJS, gültig ab 1. August 2019. Kapitel 4 Themen und Inhalte:
   je vier Pflicht- und Wahlthemenfelder. Lizenz CC BY-ND 4.0.

   Quelle: https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/rahmenlehrplaene/berufliche_bildung/bb/Mathematik-RLP_FOS_2019_Brandenburg.pdf

   ## quelle-iqb-formelsammlung-2024-mathematik.txt  [FS-IQB]

   IQB, Mathematisch-naturwissenschaftliche Formelsammlung, Stand
   14.02.2024, nur Teil 1 Mathematik (Abschnitte 1.1 Grundlagen,
   1.2 Analysis, 1.3 Analytische Geometrie/Lineare Algebra,
   1.4 Stochastik). Ab Abitur 2025 in Berlin und Brandenburg das
   einzige zugelassene Formeldokument (nicht in Prüfungsteil A).
   © IQB – Gliederung und Formelnamen als Beleg. Achtung: Die
   Textfassung gibt Formeln nur bruchstückhaft wieder (Brüche,
   Wurzeln, Indizes fehlen); für den Wortlaut einer Formel das
   PDF lesen. Löst [FS] für Sek II: Abschnittsverweise im
   Merkkasten sind hier prüfbar.

   Quelle: https://www.iqb.hu-berlin.de/media/documents/N_Mathematisch-naturwissenschaftliche_Formelsammlung.pdf

   ## quelle-iqb-operatoren-2019.txt  [IQB-OP]

   IQB, Grundstock von Operatoren, Mathematik, Stand 28.02.2019.
   Gilt unverändert; die überarbeitete Fassung ab 2027 betrifft
   nur Englisch und Französisch. Maßgeblich für die Spalte
   `operator` und für Aufgabentexte der Prüfungsblätter.

   Quelle: https://www.iqb.hu-berlin.de/media/documents/M_Grundstock_von_Operatoren.pdf

   ## quelle-iqb-vereinbarungen-2022.txt  [IQB-VER]

   IQB, Inhaltliche Vereinbarungen zur Gestaltung der Aufgaben,
   Mathematik, Stand 17.01.2022.

   Quelle: https://www.iqb.hu-berlin.de/media/documents/M_Inhaltliche_Vereinbarungen_zur_Gestaltung_der_Aufgaben.pdf

   ## quelle-iqb-struktur-2024.txt  [IQB-STR]

   IQB, Beschreibung der Struktur der Aufgaben, Mathematik, Stand
   19.06.2024: Prüfungsteil A und B, Aufgabengruppen, Umfang.

   Quelle: https://www.iqb.hu-berlin.de/media/documents/M_Beschreibung_der_Struktur_der_Aufgaben.pdf

4. In `quellen/quellen.md` unter `## Noch nicht abgelegt` den
   Punkt `[FS]` so ändern, dass nur der Sek-I-Teil bleibt:
   „[FS] Formelsammlung Sek I: Das P10-Formelblatt ist nicht
   öffentlich. Sek II: siehe [FS-IQB]."
   Den ersten Absatz der Datei („Textfassungen der drei Quellen
   …") so anpassen, dass er von den Quellen für Sek I und Sek II
   spricht; der Grund (Erreichbarkeit, LISUM aufgelöst) bleibt.

5. `README.md`, Abschnitt `## quellen/ – Quellentexte`: nach den
   drei vorhandenen Zeilen acht Zeilen im selben Stil ergänzen,
   je Datei Name und ein Halbsatz; Lizenz nur, wo sie nicht CC
   BY-ND ist (IQB: © IQB).

6. Diese Auftragsdatei nach
   `archiv/auftrag-quellen-sek2-2026-09-19.md` verschieben
   (git mv).

7. Ein Commit: „Quellentexte Sek II: RLP GOST BE/BB, FOS, IQB".

## Prüfungen

- Acht neue Dateien unter `quellen/`, alle UTF-8, alle mit LF.
- Zeilenzahlen wie in Schritt 1 (bis 5 % Abweichung).
- `grep -c "Chemie" quellen/quelle-iqb-formelsammlung-2024-mathematik.txt`
  liefert höchstens die Treffer aus Titel und Inhaltsverzeichnis
  (erwartet 3 oder weniger).
- Keine PDF im Repo.
- Außer `quellen/`, `README.md`, `archiv/` nichts geändert.

## Bericht (zurück in den Chat)

- Je Datei die Zeilenzahl der Textfassung und die Abweichung von
  der Erwartung.
- Ob eine Adresse nicht erreichbar war (dann Datei auslassen und
  melden, nicht ersetzen).
- Die eingefügten README-Zeilen wörtlich.
- Commit-Hash.
- Letzte Zeile: „Push origin drücken".

## Regeln

- Textfassungen nicht nachbearbeiten außer dem Zuschnitt in
  Schritt 2.
- Vorhandene Quellentexte und ihre Abschnitte in `quellen.md`
  nicht ändern, außer den zwei Stellen aus Schritt 4.
- Bei Unklarheit die einfachste Lesart wählen und im Bericht
  nennen, nicht rückfragen.
