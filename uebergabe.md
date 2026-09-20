# Übergabe 2026-09-20a

## 1 Ziel

Sek-II-Serie ist abgeschlossen (42 Sek-II-Einträge, 71 gesamt,
alle Sek-II-Themen der themen.csv gedeckt). Jetzt: Gegenlese,
Protokoll-Auswertung blattbau, danach Promptumbau und
Geltungsrecherche. Testlauf mit einem gebauten Blatt bleibt
verschoben (19b), sinnvoll nach der Gegenlese.

## 2 Arbeitsgrundlage

- GitHub hz-0801/mathe-nachhilfe, Commit e6f1df8 (gepusht,
  20.09.2026). Maßgeblich: konzept.md § 4, Entscheidungen 1–36
  samt Zusätzen (neu: Eintragsart Verweiseintrag, c13cc58);
  katalog/ mit 71 Einträgen; themen.csv; faellig.md.
- Prüfskripte Sek-II-fähig samt Serien-Erweiterungen
  (Verweiseintrag 164c741, Malpunkt-Parser c4d1fc8). Kennzahl 5
  = 345 (nur noch Sek-I-Restposten, Serie deckt alles).
- hz-0801/blattbau unverändert (0e1ec2d): Prompts, Vorlage,
  zwei Testauswertungs-Raster. hz-0801/anweisungen: kandidaten.md
  7472eb6.
- Claude Code im Code-Tab. Aufträge als Textblock nach
  kandidaten.md „Delegationsform". Bewährt in elf Bündeln und
  in die Aufträge übernommen: Kontext-Stopp-Regel (laufenden
  Eintrag beenden, nach Komprimierung nichts Neues beginnen),
  Kennzahl-5-Sollwertkette als Stoppsignal, Vorabprüfung der
  ids, Prüfungen und Commit je Eintrag, Mehrbündel-Aufträge mit
  bewusstem Überpacken. Neu: nie ids ungebauter Themen im Text
  nennen (bloße Erwähnung zählt als verbaut; Befund 511/512).
- Modell: Fable hat die Serie getragen (Bündel 2–11) und ist
  erste Wahl für Katalog-/Prosaarbeit; Wochenlimit war am
  20.09. zu 99 % verbraucht (Reset Mo 18:00), Nutzungsguthaben
  0 €. Mechanik: Sonnet. Lehrer prüft die Ausgabenlimit-
  Einstellung (20,43 € von 1 € angezeigt, Neuladen aus).

## 3 Arbeitsstand

Seit 19d: Bündelplan erstellt und abgearbeitet – elf Bündel in
sechs Serienaufträgen (B1 Opus, B2–11 Fable), 39 Themen, alle
Sollwerte exakt, alle Prüfungen grün. Nebenarbeiten in den
Läufen: Seitenzahlkorrekturen [GOST] (66961ca, 8d66679),
Befundkorrekturen [FS-IQB 1.1] Figurenmaße (d2b39ee) und [FS]
Signifikanztest (99af310), Wendetangenten-Vermerk aufgelöst,
faellig-Posten Zuruf-Deutung (8ceac4e) und Erwartungshorizonte
(6cfa150), Geltungsrecherche als faellig-Posten. Vorentscheidung
Verweiseintrag abgelegt und gebaut
(ableitungsgraph-und-funktionsgraph).

Vorfall Bündel 8–11-Lauf: Komprimierung während Bündel 10,
Bündel 11 wurde danach regelwidrig neu begonnen; der Lauf hat
sich sichtbar neu geerdet (Rohdateien neu gelesen), alle
Prüfungen grün – Konsequenz: Gegenlese-Vorrang für die vier
Bündel-11-Einträge.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Entscheidungen 1–36 samt Zusätzen: konzept.md § 4; nicht neu
  aufrollen. Formbefunde stehen in den Einträgen.
- Matrizen und Konfidenzintervalle sind gebaut, obwohl Geltung
  offen: Katalog dient auch Unterrichtsblättern; Geltungsfragen
  füllen nur Vermerke, sie entscheiden nicht über Einträge.
- blattbau-Konzepte (19.09., Umsetzung beim Promptumbau;
  Vollform): Blatt 0 = Hinführung zum Stundenthema,
  Standardbestandteil ohne Bestellparameter; Bauprinzip
  Überspringbarkeit; Kurzkästen und Kurzergebnisse am
  Blattende; Scheiternsregel (Herkunftsthema wird Stundenthema);
  Kurztest als fester Schlussabschnitt (10 Minuten, 3 Aufgaben,
  Etiketten, Ankreuzfußzeile), Befund per Foto in den Chat;
  Stundenanker = Kompositionsregel des Prompts, kein
  Katalogobjekt. Betriebsmodell: Projekt „Unterricht", ein Chat
  je Schüler, Pseudonyme ab der ersten Nachricht. Präzisierung
  (20.09.): Schülerakte als kompakte Datei im Projektwissen
  (Stand, Lücken, Kurztest-Befunde, nächstes Thema); Chat liest
  sie am Start aufs Pseudonym hin und gibt am Stundenende die
  aktualisierte Akte als Codeblock aus, Lehrer kopiert sie
  zurück; Chat-Suche als Sicherheitsnetz; keine Schülerdaten in
  Repos.

## 5 Offene Punkte und verworfene Ansätze

Lehrer: (a) Gegenlese aller 42 Sek-II-Einträge, Vorrang
Bündel 11 (kenngroessen, normalverteilung, hypothesentests,
konfidenzintervalle), danach Bündelberichte-Punkte: schwächste
Auswendig-Zeile gleichungen-loesen Kasten 4, Planzeilen-
Einheiten ohne amtliche Deckung, BE-Angabe binomialverteilung
(L4 S. 27, L2 S. 25); (b) dabei entscheiden: Kastenbeispiele
einheitlich (B1–3 eigene Zahlen, ab B4 wörtlich aus
Prüfungszeilen – beides als Ermessen markiert); (c)
stehengebliebene Offene-Punkte-Zeile im Piloten
(kurvenuntersuchung, Verweis-Entscheidung) abräumen; (d)
Ausgabenlimit-Einstellung prüfen; (e) Ort, Format und Anzahl
der Protokoll-Archive nennen (für den Auswertungs-Block).

Werkstatt, nach Gegenlese/parallel: Protokoll-Auswertung
blattbau (eigener Block, Ordner blattbau, nach dem
Testauswertungs-Raster im Repo, aggregierter Befundbericht als
Datei; speist den Promptumbau). Promptumbau-Vormerkungen:
Kriterienabgleich der Blattregeln gegen Büchter/Leuders
(Mathematikaufgaben selbst entwickeln, Cornelsen 2023) mit
Kandidat „operative Variation als Blattelement"; Zuruf-Deutung
über Konkordanz (faellig). Einheitenschnitt-Verbesserungen:
Ausreißer-Flag im Prüfskript (Mini-Einheiten ohne Vermerk),
Gliederungsregel Sek II als E36-Zusatz, Validierung über
Testlauf und Kurztest-Befunde. Gebündelte Geltungsrecherche
(faellig-Posten; Matrizen ab 2030, Konfidenzintervalle,
Sinus-Ableitung GK, Scharen/Rotationsvolumen-Niveau,
hypergeometrisch BB/BE, Transformationen „Anlage ja, Plan
nein", Normalverteilung; amtliche Quellen, Stand angeben).
Fortgeführt: Erwartungshorizonte-Beschaffung (faellig);
Sek-I-Restposten (345 Zeilen: sieben Themen ohne Rohdatei,
funktionen-allgemein, kombinatorik, zwei nur typ_neben);
[FS]-Abgleich am PDF, COSH-Beschaffung, [BASICS], MaCo-Lizenz;
Kastenzahlen-Lauf nichtdeterministisch (kosmetisch).

Verworfen (neu): Register-/Inhaltsverzeichnisanalyse von
Lehrbüchern als eigener Lauf (für den Prüfungszweck den
Hauptquellen unterlegen; Lehrwerk bleibt nachrangige Stütze);
paralleler Zweitblock während Abwesenheit (kein Nutzervorteil,
Ein-Block-Prinzip); Modell-Doppelläufe zum Gliederungsvergleich
(teuer, Abweichung ≠ Fehler); Schülerakten im GitHub-Repo
(Schülerdaten). Fortgeführt verworfen (19d): Formerweiterung
„typischer Fehler → verletzte Voraussetzung"; Zurufparameter
„reduziert"/„Spickzeile"; Stundenanker als Katalogobjekt.

## 6 Nächster Arbeitsschritt

Der neue Chat erfragt Ort, Format und Anzahl der
Protokoll-Archive und schreibt dann den Block für die
Protokoll-Auswertung (Ordner blattbau, Modell Opus oder Sonnet
– Fable-Limit beachten). Parallel läuft die Gegenlese des
Lehrers; ihre Befunde werden im neuen Chat gesammelt und als
Nachbesserungs-Block gebündelt.
