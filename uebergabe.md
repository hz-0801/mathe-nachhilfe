# Übergabe 2026-09-20

## 1 Ziel

Der Themenkatalog beschreibt den Stoff so, dass daraus Unterrichts-
und Prüfungsblätter gebaut werden können. Die Sek-II-Einträge nach
Entscheidung 36 stehen; der nächste Zweck ist der Umbau der beiden
Prompte im Repo blattbau und der erste Testlauf eines Blatts aus einem
Katalogeintrag.

## 2 Arbeitsgrundlage

- GitHub hz-0801/mathe-nachhilfe, Commit e6f1df8 (19./20.09.2026).
  Maßgeblich: konzept.md § 4 (Entscheidungen 1–36 samt Zusätzen),
  README.md als Landkarte, faellig.md § 2 für die offenen Handlungen.
- katalog/ – alle Sek-I- und Sek-II-Themen der themen.csv haben einen
  Eintrag; Status durchgehend Entwurf, gegengelesen: nein.
- Prüfskripte katalog/_pruef_struktur.py und katalog/_pruef_katalog.py
  (Sek-II-Modus, Einheiten E1–E9, Eintragsart Verweiseintrag).
- hz-0801/blattbau (0e1ec2d, unverändert): unterrichtsblatt.md,
  pruefungsblatt.md, LaTeX-Vorlage – Gegenstand des nächsten Schritts.
- hz-0801/anweisungen: kandidaten.md, darin die Delegationsform.
- Claude Code im Code-Tab, Aufträge als Textblock nach der
  Delegationsform (/clear-Regel, Modell in der Holger-Zeile).
  Katalog- und Prompttexte: Opus; reine Mechanik: Sonnet.

## 3 Arbeitsstand

Seit 19d abgeschlossen und committet (Push durch den Lehrer): die
gesamte Sek-II-Serie in elf Bündeln, Analysis → Integral → Analytische
Geometrie → Stochastik, jeweils mit nachgezogenem README-Katalogstand.
Darin der erste Verweiseintrag (ableitungsgraph-und-funktionsgraph,
E36-Zusatz „Eintragsart Verweiseintrag"), das größte Einzelthema
(matrizen-und-uebergangsprozesse, 154 Katalogzeilen) und zwei reine
Poolthemen ohne Planinhalt (Matrizen, Konfidenzintervalle). Werkstatt:
BB-Seitenzahlen in katalog/_quellen.md korrigiert (Fußzeilen-Regel),
Prüfskript um Verweiseintrag und Typnamen mit Malpunkt erweitert, zwei
Befundkorrekturen ([FS-IQB 1.1] Figurenmaße in
flaecheninhalt-durch-integration, [FS] Signifikanztest in
hypothesentests), index.md nachgezogen.

Nicht begonnen: der Umbau der blattbau-Prompte; kein Blatt ist bisher
aus einem Katalogeintrag gebaut worden.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Entscheidungen 1–36 samt Zusätzen: konzept.md § 4; nicht neu
  aufrollen. Formbefunde stehen in den Einträgen selbst unter „Offene
  Punkte".
- Die Sek-II-Eintragsform (E36) hat in Analysis, Geometrie und
  Stochastik getragen; die Kastenform mit Auswendig-Zeile gilt für
  jeden Sek-II-Merkkasten.
- blattbau-Konzepte (Diskussionsstand 19.09.2026, Umsetzung steht aus;
  faellig.md § 2 trägt die Kurzposten): Blatt 0 = Hinführung zum
  Stundenthema (Erinnerung, Test, Heranführung), Standardbestandteil,
  vollständiges Blatt ohne Bestellparameter; Bauprinzip
  Überspringbarkeit (unabhängige Aufgaben, beschriftete
  Fertigkeitsgruppen, Wichtigstes je Gruppe zuerst); Kurzkästen der
  Herkunftsthemen und Kurzergebnisse gesammelt am Blattende;
  Scheiternsregel: Herkunftsthema wird Stundenthema. Kurztest = fester
  Schlussabschnitt jedes Blatts (10 Minuten, 3 Aufgaben, je ein
  Einheiten-/Fertigkeitsetikett, Ankreuzfußzeile sicher/mit
  Hilfe/nicht); Befund geht per Foto in den Chat und speist die
  nächste Stunde. Stundenanker = Kompositionsregel des
  Unterrichtsblatt-Prompts (Kästen der gewählten Einheiten in Kurzform
  an den Blattanfang), kein Katalogobjekt. Zuruf-Deutung über die
  Konkordanz: ein Themen-Zuruf wird über themen.csv auf das kanonische
  Thema aufgelöst, enger nur bei ausdrücklichem Fokus-Zuruf.
  Betriebsmodell: eigenes Projekt „Unterricht", ein Chat je Schüler,
  Pseudonyme von Anfang an, Schüler-Umzugsregel mit Kurzübergabe.

## 5 Offene Punkte und verworfene Ansätze

Lehrer: fachliche Gegenlese der Sek-II-Einträge (Kästen, Sprossen,
Auswendig-Zeilen); Mechanik-Punkte Sek I (A4 breit/eng, Prüflisten,
Prüflistenzeilen 10 und 11).

Werkstatt, mit Posten in faellig.md § 2: gebündelte Geltungsrecherche
zu Matrizen und Konfidenzintervallen (Auslöser mit dem Serienende
eingetreten); Quellenausbau Erwartungshorizonte (löst die
BE-Angaben-Lücke, Befund binomialverteilung); Anker-Kompositionsregel
und Skizzenbedarf der Kästen beim Promptumbau; Zuruf-Deutung über die
Konkordanz beim Promptumbau. Ohne Posten: [FS]-Abgleich am PDF der
Formelsammlung, COSH-Beschaffung und [BASICS] am Text, MaCo-Lizenz vor
der ersten MaCo-Formulierung; zwei nicht eindeutige gost-Verweise im
Quellenprotokoll (kein Blocker); sieben fein geschnittene Sek-I-Themen
ohne eigene Rohdatei; funktionen-allgemein und kombinatorik ohne
Katalogdatei; zwei Themen nur in typ_neben. Kosmetisch:
Kastenzahlen-Lauf sortiert wertgleiche Zahlen (0,05/0,050)
nichtdeterministisch.

Verworfen (Stand 19d, nur soweit es sonst wiederkäme): Formerweiterung
„typischer Fehler → verletzte Voraussetzung" (entfiel mit der
Hinführungslesart von Blatt 0); Zurufparameter
„reduziert"/„Spickzeile" (Anpassung durch Weglassen am Tisch);
Stundenanker als Katalogobjekt (dupliziert Kästen fremder Themen).

## 6 Nächster Arbeitsschritt

Zwei Stränge, in dieser Reihenfolge:

1. Gebündelte Geltungsrecherche (faellig.md § 2): Prüfungsrelevanz von
   Matrizen/Übergangsprozessen und Konfidenzintervallen für künftige
   Jahrgänge ab Abitur 2030 klären – künftige Prüfungsschwerpunkte
   beider Länder und die KMK/IQB-Dokumente prüfen, Ergebnis in die vier
   Geltungsdateien und in die Vermerke der beiden Katalogeinträge.
   Recherche im Chat, Ablage per Auftrag.
2. Umbau der beiden Prompte im Repo blattbau nach den Konzepten aus
   § 4, danach der verschobene Testlauf: ein Unterrichtsblatt aus einem
   fertigen Sek-II-Eintrag bauen und am Ergebnis prüfen, ob der Eintrag
   trägt. Das ist der erste Belastungstest des Katalogs überhaupt.
