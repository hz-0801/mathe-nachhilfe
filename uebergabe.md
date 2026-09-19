# Übergabe 2026-09-19d

## 1 Ziel

Sek-II-Themenkatalog in Serie: 39 verbleibende Einträge nach
konzept.md § 4 Entscheidung 36 bauen. Vorlauf abgeschlossen
(Werkzeuge Sek-II-fähig, drei Formproben bestanden, Kastenform
entschieden). Testlauf mit einem gebauten Blatt bleibt
verschoben (19b).

## 2 Arbeitsgrundlage

- GitHub hz-0801/mathe-nachhilfe, Commit 955bca2 (gepusht,
  19.09.2026). Maßgeblich: konzept.md § 4, Entscheidungen 35
  und 36 samt Zusätzen (Straffung, Kurzform (Ek), Kastenform
  mit Auswendig-Zeile, Klarstellung Geometrie); Muster:
  katalog/kurvenuntersuchung.md, katalog/binomialverteilung.md,
  katalog/ebenen.md (alle Status Entwurf, gegengelesen: nein);
  rohdaten/<kanonisch>.md je Thema; themen.csv.
- Prüfskripte katalog/_pruef_struktur.py und
  katalog/_pruef_katalog.py (Sek-II-fähig, Einheiten E1–E9);
  Kennzahl 5 ist der Serienzähler: 2157 von 2883, sinkt mit
  jedem Eintrag um dessen Zeilenzahl.
- hz-0801/blattbau unverändert (0e1ec2d). hz-0801/anweisungen:
  kandidaten.md Commit 7472eb6 (Delegationsform ergänzt).
- Claude Code im Code-Tab, Ordner mathe-nachhilfe. Aufträge als
  Textblock nach kandidaten.md „Delegationsform" (samt
  /clear-Regel und Modell in der Holger-Zeile). Katalogeinträge:
  Opus; reine Mechanik: Sonnet.

## 3 Arbeitsstand

Seit 19c, alles gepusht: Straffungsregel und Kurzform (Ek)
abgelegt, Pilot gestrafft (a4d4a8b, f47a051). Werkzeuge
Sek-II-fähig mit bestandenem Fehlertest, index.md und README
nachgezogen, gost-Verweise geprüft (0ff8f98). Formproben
binomialverteilung (796b4b6) und ebenen (df23cc1) bestanden –
E36 trägt in Analysis, Stochastik und Geometrie. Kastenform
entschieden und abgelegt, Auswendig-Zeilen in allen drei
Einträgen, Prüfskript E1–E9, faellig.md-Posten blattbau,
.gitattributes (660335c). Seitenzahlen der ersten zwei Einträge
korrigiert, E36-Klarstellung Geometrie abgelegt (955bca2).

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Entscheidungen 1–36 samt Zusätzen: konzept.md § 4; nicht neu
  aufrollen. Die Formbefunde der Proben stehen in den Einträgen
  selbst (Offene Punkte).
- Vorentscheidung ableitungsgraph-und-funktionsgraph (Chat
  19.09., noch nicht abgelegt): Verweiseintrag – Kopf,
  Verortung (kompetenzgleich mit kurvenuntersuchung Einheit 4)
  und Prüfungsform der eigenen 21 Zeilen; Lerneinheiten,
  Kästen, Blatt 0, Fehler, Sprossen verweisen auf
  kurvenuntersuchung.md Einheit 4. Mit dem Serienauftrag des
  Themas als Eintragsart „Verweiseintrag" in E36 ablegen.
- blattbau-Konzepte (Diskussionsergebnisse 19.09., Umsetzung
  beim Promptumbau; faellig.md trägt den Kurzposten, dieser
  Absatz die Vollform): Blatt 0 = Hinführung zum Stundenthema
  (Erinnerung, Test, Heranführung), Standardbestandteil, ein
  vollständiges Blatt ohne Bestellparameter; Bauprinzip
  Überspringbarkeit (unabhängige Aufgaben, beschriftete
  Fertigkeitsgruppen, Wichtigstes je Gruppe zuerst); Kurzkästen
  der Herkunftsthemen und Kurzergebnisse gesammelt am
  Blattende; Scheiternsregel: Herkunftsthema wird Stundenthema.
  Kurztest = fester Schlussabschnitt jedes Blatts (10 Minuten,
  3 Aufgaben, je ein Einheiten-/Fertigkeitsetikett,
  Ankreuzfußzeile sicher/mit Hilfe/nicht); Befund geht per Foto
  in den Chat und speist die nächste Stunde. Stundenanker =
  Kompositionsregel des Unterrichtsblatt-Prompts (Kästen der
  gewählten Einheiten in Kurzform an den Blattanfang), kein
  Katalogobjekt. Betriebsmodell: eigenes Projekt „Unterricht",
  ein Chat je Schüler, Pseudonyme von Anfang an,
  Schüler-Umzugsregel mit Kurzübergabe.

## 5 Offene Punkte und verworfene Ansätze

Lehrer: fachliche Gegenlese der drei Sek-II-Einträge (Kästen,
Sprossen, Auswendig-Zeilen); Mechanik-Punkte Sek I.

Werkstatt: katalog/_quellen.md Z. 39 trägt BB-Seitenangaben um
eins zu niedrig (Fußzeilen-Regel; erster Serienauftrag,
Schritt 1). BE-Angabe in binomialverteilung.md deckt nur L5
(L4 liegt auf S. 27, L2 auf S. 25 – Gegenlese).
Wendetangenten-Auswendigmarkierung beim Bau von
tangente-normale-schnittwinkel.md setzen (Vermerk in
kurvenuntersuchung Kasten 3). Zwei nicht eindeutige
gost-Verweise im Quellenprotokoll (Sammelthemen von vor der
Konkordanz, kein Blocker). [FS]-Abgleich am PDF der
Formelsammlung; COSH-Beschaffung, [BASICS] am Text prüfen;
MaCo-Lizenz (faellig.md). Fortgeführt aus 19b: sieben fein
geschnittene Sek-I-Themen ohne eigene Rohdatei;
funktionen-allgemein und kombinatorik ohne Katalogdatei; zwei
Themen nur in typ_neben. Kosmetisch: Kastenzahlen-Lauf sortiert
wertgleiche Zahlen (0,05/0,050) nichtdeterministisch.

Verworfen (neu): Formerweiterung „typischer Fehler → verletzte
Voraussetzung" (entfiel mit der Fundament-/Hinführungslesart
von Blatt 0); Zurufparameter „reduziert"/„Spickzeile"
(Anpassung durch Weglassen am Tisch statt Konfiguration);
Stundenanker als Katalogobjekt (dupliziert Kästen fremder
Themen).

## 6 Nächster Arbeitsschritt

Serie der 39 Restthemen in Umfangsbündeln: ~150–200 Rohzeilen
je Auftrag, fachlich benachbarte Themen zusammen (ergibt etwa
12–14 Aufträge), Reihenfolge Analysis-Differenzialrechnung →
Integral → Analytische Geometrie → Stochastik; Zielmodell Opus.
Der erste Serienauftrag beginnt mit der Seitenzahlkorrektur in
katalog/_quellen.md (Schritt 1), dann die ersten Einträge. Vor
matrizen-und-uebergangsprozesse (Geltungsfrage Abitur 2030) und
ableitungsgraph-und-funktionsgraph (Vorentscheidung B ablegen)
je eine kurze Chat-Klärung. Der neue Chat erstellt zuerst den
konkreten Bündelplan aus themen.csv und legt ihn dem Lehrer
vor; dann Serienstart.
