# Auftrag Nacht 2026-09-27: offene Mechanik aufräumen,
# Vorschläge für das Urteil, Abitur 2017 nachziehen

Modell: Opus (Teil 1, 4, 5, 7, 9 und 10 lesen je Stelle). Läuft
ohne den Lehrer: keine Rückfrage, Standdatei, Commit je Teil,
Fehlerregel je Teil.

## Ausgangslage

ziel.md (Stand 25.09.2026), uebergabe.md (25.09. abends) und
faellig.md § 2 führen Posten, die ohne Urteil gehen oder deren
Urteil im Chat mit einem Vorschlag schneller fällt als ohne. Der
Testlauf vom 25.09. (bericht-testlauf-2026-09-25.md) ist gebaut
und wird im Chat ausgewertet; dieser Auftrag fasst ihn nicht an.
Zwei Arten von Teilen:

- Mechanik (Teil 1–6, 8): das Ergebnis steht danach im Repo.
- Vorschlag (Teil 7): du schreibst in eine Vorschlagsdatei, nie in
  den Katalogeintrag; der Chat entscheidet.
- Erfassung (Teil 9, 10): Abiturhefte nach CLAUDE.md und abi.md,
  ein Heft oder Stapel je Lauf.

Du änderst keinen Prompt und nichts unter blaetter/testlauf-*/.
Parallel läuft im Ordner blattbau ein zweiter Auftrag (Vorlage
Stufe 5); du liest ../blattbau, schreibst dort nichts.

## Regeln

- Shell PowerShell: kein Heredoc, kein sed. Dateien schreiben mit
  [System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false))); Zeilenenden LF;
  nach dem Schreiben prüfen (keine BOM, kein CR).
- Python nur %LocalAppData%\Programs\Python\Python312\python.exe;
  git über die git.exe von GitHub Desktop, mit -c core.pager=cat;
  Commit-Nachrichten mit Umlaut über commit -F aus einer
  UTF-8-Datei, nie -m; kein Push.
- pdftotext, pdfinfo, pdftoppm liegen unter
  %LocalAppData%\Programs\MiKTeX\miktex\bin\x64. CQL-Abfragen mit
  Anführungszeichen an werkzeuge/dnb-sru.py über --% und
  verdoppelte Anführungszeichen.
- Nichts löschen; verschieben nur mit git mv. Keine Handedits an
  CSV, die ein Bauskript schreibt; abgeleitete Dateien tragen die
  Zeile „Abgeleitet von <skript>, nie von Hand ändern".
- Grenzen sind Zählgrenzen, nie Zeit. Fehlerregel überall: ein
  Schritt, der zweimal scheitert, wird als „offen" mit Grund in
  Standdatei und Bericht eingetragen; der nächste Punkt folgt.
- Standdatei nacht-stand-2026-09-27.md in der Wurzel: je Teil eine
  Zeile „offen / läuft / erledigt" mit dem letzten fertigen Punkt
  und dem Commit; Uhrzeiten nur aus Get-Date, nie aus dem Text;
  ein Neustart liest sie zuerst und macht beim ersten nicht
  erledigten Teil weiter.
- Gegenproben: Der bekannte Wert steht mit seiner Belegdatei
  dabei. Weicht die Gegenprobe ab, schreib die Abweichung mit
  Erklärung in den Bericht und ändere das Skript nicht.
- README.md ist die Landkarte: jede neue Datei bekommt dort einen
  Satz, im selben Commit. faellig.md: einen erledigten Posten im
  selben Commit in § 2 streichen und mit Datum in § 4 eintragen;
  einen neuen Posten eintragen statt ihn im Bericht zu lassen.
- Skripte gehören mit allen Daten, die sie brauchen, ins Repo;
  nichts bleibt im Scratchpad. Sub-Agenten, die dieselben Dateien
  anfassen, laufen nacheinander.

## Teil 1: Belegskripte auf die drei neuen Katalogstellen, Marken neu

Grundlage: katalog/_marken-neue-einheiten.md, bericht-marken.md,
werkzeuge/marken-bau-stellen.txt, faellig.md § 2 (Posten
„Zuordnungsdaten der Belegskripte").

1. werkzeuge/klassen-belege-daten.py: die acht Potenzfunktionen-
   Stellen von potenz-exponentialfunktionen Einheit 1 nach
   Einheit 5 (ohne den entfernten Vorrat-Typ); die fünf
   Vierfeldertafel-Stellen von daten Einheit 1 nach Einheit 7;
   die Klasseneinteilungs-Stellen als Typzeilen an die vier
   Klassen-Typen von daten Einheit 1 (Lesart wie
   marken-bau-stellen.txt).
2. werkzeuge/pruefungswort-belege-daten.py: potenz-
   exponentialfunktionen Einheit 1 ab 1.11 und daten Einheit 1
   über den Wortlaut umnummerieren; die neuen Einheiten und Typen
   zuordnen.
3. werkzeuge/marken-bau-stellen.txt: betroffene Zeilen auf die
   neue Einheit stellen.
4. python werkzeuge/klassen-belege.py und
   werkzeuge/pruefungswort-belege.py laufen lassen – beide müssen
   ohne die bisherigen Abbrüche (sieben Fehler Vorrat-Typ, zwei
   Prüffehler) durchlaufen. Dann python werkzeuge/marken-bau.py
   --probe, dann ohne --probe.

Gegenprobe Teil 1 (bericht-marken.md, katalog/_klassen-belege.md,
katalog/_pruefungswort-belege.md): git diff über katalog/*.md
zeigt geänderte Marken-Zeilen und Typklammern nur in
potenz-exponentialfunktionen.md und daten.md; lineare-funktionen
Einheit 4 trägt weiter „P10" (3 von 13), quadratische-gleichungen
Einheit 2 weiter „GYM Kl. 8–9". Zahl der Marken-Zeilen 273,
Typklammern 262 (bericht-marken.md), plus das, was die drei
Stellen dazubringen – die neue Zahl in den Bericht.

Commit „katalog: Belegskripte auf die neuen Einheiten, Marken neu
gebaut".

## Teil 2: FHR-Wort an den acht Sek-I-Einheiten mit Sek-II-Zeilen

bericht-marken.md Punkt 15: einheiten 1, 3, 4;
lineare-gleichungssysteme 1, 3, 4; daten 1, 4 tragen nur die
Sek-I-Form. Erweitere werkzeuge/marken-bau.py so, dass eine
Sek-I-Einheit mit FHR-Jahrgängen in _pruefungswort-belege.md das
Prüfungswort „FHR" anhängt, in derselben Form wie bei den
Sek-II-Einträgen (Wortlaut dort nachsehen und übernehmen);
Schwelle: mindestens ein FHR-Jahrgang. Neu bauen wie in Teil 1.

Gegenprobe Teil 2 (bericht-marken.md Punkt 15): daten 1 und daten 4
tragen danach „FHR"; außer den acht Einheiten ändert sich keine
Marken-Zeile.

Commit „katalog: FHR-Wort an Sek-I-Einheiten mit Sek-II-Zeilen".

## Teil 3: potenz-exponentialfunktionen.md an Einheit 5 angleichen

faellig.md § 2, Posten „potenz-exponentialfunktionen.md an die
neue Einheit 5 angleichen". In der Nummernzeile von Einheit 1 die
Lesart „Potenzfunktion als zweiter Funktionstyp mit Potenz im
Term (Vorrat, H)" und das Eingabewort „potenzfunktion" entfernen
(es steht bei Einheit 5); Verortung und „Offene Punkte" auf
Einheit 5 umschreiben; die Zeile in katalog/index.md
(„Potenzfunktion als Vorrat, H/GYM") auf den neuen Stand. Nur
diese Stellen; Sprossen und Kasten für Einheit 5 sind Teil 7.
Prüfung: python werkzeuge/themen-pruef.py und
werkzeuge/verweis-pruef.py laufen ohne neuen Fehler.

Commit „katalog: potenz-exponentialfunktionen Einheit 1 ohne
Vorrat-Lesart".

## Teil 4: Kleinposten aus Nacht 26.09. und Werkzeugpflege

Quelle: nacht-bericht-2026-09-26.md Teil 2, faellig.md § 2.

1. flaechen.md, Prüfungsform „Term zu Figur angeben": die
   Original-ids nach msa/msa-katalog-*.csv richtig zuordnen
   (2014-OS-B1g Kreuz aus Quadraten, 2022-OS-B1e rechtwinkliges
   Dreieck, 2025-OS-B1i geteiltes Rechteck – vor dem Tausch in der
   CSV nachsehen, die CSV gilt).
2. zuordnungen.md und terme.md um die GYM-Typen aus
   msa/msa-typen.csv ergänzen, die ihr Thema tragen und im Eintrag
   fehlen: je Typ in die Typenzeile der passenden Lerneinheit,
   Zuordnung nach Inhalt, Grund im Bericht; den Satz „hat keinen
   eigenen Typ" bzw. „hat einen Typ" berichtigen.
3. themen.csv: „Maßstab" von zuordnungen nach strahlensaetze
   (katalog/index.md führt es so); themen-pruef.py danach ohne
   neuen Fehler.
4. werkzeuge/klassen-ermessen.py: Zitat je Fall aus der eigenen
   Reihe statt aus der ersten (Nebenbefund in
   katalog/_marken-entscheidungen.md); katalog/_klassen-ermessen.md
   neu bauen.
5. katalog/index.md Zeile 232 (Absatz „Belege der Blatt-0-
   Fertigkeiten ohne Ziel") auf 147/131/16, Kennzahl 9 = 24 von
   463 und 316/308/8 (Freigabe des Lehrers vom 25.09.; Werte aus
   katalog/_blatt0-belege.md § Zahlen).

Gegenprobe Teil 4: msa/msa-typen.csv zählt zum Thema
„Zuordnungen" den Typ „Antiproportionale Zuordnung Dreisatz"
(nacht-bericht-2026-09-26.md); er steht danach in zuordnungen.md.

Commit „katalog: flaechen-ids, GYM-Typen zuordnungen und terme,
Maßstab, klassen-ermessen, index Zeile 232".

## Teil 5: Vorrat-Verweise auf gost-*/fos-* umstellen

faellig.md § 2, Posten „Vorrat-Verweise der Sek-I-Einträge auf
die alten Gliederungsentwürfe". Im Katalog stehen 43 Verweise auf
zwölf Dateien gost-*.md und fos-*.md, die es nicht gibt, in
zwölf Einträgen (gezählt am 25.09. mit grep; 14 davon auf
gost-funktionen-grundlagen.md). Jeden Verweis auf den
kanonischen Sek-II-Eintrag umstellen, der den Stoff führt
(Tabelle Sek II in katalog/index.md, themen.csv); wo eine Datei
auf zwei Einträge zerfällt, den nach dem Wortlaut der Stelle
wählen und die Wahl im Bericht nennen. Danach die beiden
Gliederungsentwürfe in katalog/index.md gegen themen.csv prüfen
und den Absatz vor „Gymnasiale Oberstufe" richtigstellen.

Gegenprobe Teil 5: grep über katalog/*.md findet danach kein
„gost-" und kein „fos-" mehr; werkzeuge/verweis-pruef.py zählt in
Gruppe „Ziel fehlt" 43 weniger.

Commit „katalog: Vorrat-Verweise auf die Sek-II-Einträge".

## Teil 6: Netz und Pfade

1. cosh-Mindestanforderungskatalog: suchen (cosh Mindest-
   anforderungskatalog Mathematik, Version 3.0 oder neuer),
   PDF nach quellen/ sichern, Textfassung mit pdftotext -layout,
   Zeile in quellen/quellen.md; danach den Verweis in konzept.md
   § 4 Entscheidung 36 auf die Datei richten. Ist die Datei nicht
   frei erreichbar: Verweis auf „nicht im Repo, Fundort <URL>"
   umstellen.
2. Fundamente Mathematik Ausgabe B, Qualifikationsphase
   (Cornelsen): über werkzeuge/dnb-sru.py suchen (tit und jhr;
   höchstens zehn Abfragen), Inhaltsverzeichnis d-nb.info/<IDN>/04
   sichern wie die übrigen Lehrwerke unter quellen/, Textfassung,
   Zeile in quellen/quellen.md und in der Lehrwerksliste, die die
   Sek-II-Ordnung nennt (katalog/_sek2-ordnung-belege.md Kopf).
   Nicht auswerten.
3. abitur/iqb-quellen.py: Standard-Cache von iqb-pdf/ auf
   hefte/iqb/ (faellig.md § 2); README.md Zeile 89 und 376,
   konzept.md § 2, .gitignore, werkzeuge/tragfaehigkeit.py Zeile
   188 nachziehen. Kein Lauf des Skripts.

Gegenprobe Teil 6: python abitur/iqb-quellen.py --help oder ein
Aufruf ohne Argument darf nichts holen und muss hefte/iqb als
Standard nennen; falls das Skript ohne Argument sofort lädt, nur
den Quelltext prüfen.

Commit „quellen: cosh, Fundamente B Q-Phase; iqb-Cache-Pfad".

## Teil 7: Vorschläge für das Urteil im Chat

Schreibe katalog/_vorschlaege-2026-09-27.md (Kopf: Zweck, Stand,
„Vorschlag, nicht entschieden"). Vier Abschnitte. Du änderst hier
keinen Eintrag.

1. Ausbau der neuen Einheiten (katalog/_marken-neue-einheiten.md):
   für potenz-exponentialfunktionen Einheit 5 und daten Einheit 7
   je einen vollständigen Vorschlag in der Form des Eintrags:
   Merkkasten (höchstens fünf Zeilen), Sprossen je Verfahrenstyp
   (Kette von Grundfall bis Zielmarke; Zielmarke nach Lehrwerk-
   Konvention, weil kein P10-Original – so sagt es die Marke),
   Typische Fehler, Voraussetzungen (Blatt 0) mit Dateiverweisen
   in Klammerform, Verortung. Muster: die Nachbareinheiten
   desselben Eintrags und ein Eintrag mit gleicher Marke.
   Belege: die Lehrwerksstellen aus katalog/_klassen-belege.md
   und die Textfassungen unter quellen/. Für daten 7 dazu die
   Verortungszeile in daten.md, die die Vierfeldertafel noch als
   Teil von Einheit 1 nennt, als Ersetzungsvorschlag.
2. Niveaustufe G (befund-geltung-2026-09-21.md § 3): Sinussatz in
   beliebigen Dreiecken (trigonometrie.md) sowie Lösbarkeit und
   Lösungsvielfalt quadratischer Gleichungen der Typen ax²+n=b und
   ax²+bx+n=0 (quadratische-gleichungen.md): je ein Vorschlag, wo
   im Eintrag es steht (Einheit, Typ, Sprosse, Marke) und was sich
   ändert, mit RLP-Zitat und Zeilennummer aus dem RLP-Text unter
   quellen/. Prüfe zuerst, ob der Eintrag es schon führt.
3. msa/msa-katalog-gym.csv, Zeile 2025-GYM-K5d: Nebentyp
   „Mantellinie Kegel bestimmen" prüfen; Vorschlag mit dem
   Wortlaut der Aufgabe (Textfassung unter quellen/ oder
   hefte-md/) und dem Etikett, das nach Kern § 6 passt.
4. 28 Namensabweichungen (katalog/_verweise.md Prüfung 3 (b)):
   je Zeile H1-Überschrift, thema-Werte, Sorte (fhr-Titel
   systematisch / ohne Übereinstimmung) und ein Vorschlag:
   „Sammelthema, so lassen" oder „H1 auf … ändern" oder
   „thema-Wert auf … ändern", mit einem Satz Grund.

Gegenprobe Teil 7: Abschnitt 4 hat so viele Zeilen, wie
_verweise.md Prüfung 3 (b) Einträge nennt (dort nachzählen und
die Zahl in den Bericht; die Fundstelle nennt 27 Einträge, die
Überschrift 28).

Commit „katalog: Vorschläge neue Einheiten, Niveaustufe G,
GYM-K5d, Namensabweichungen".

## Teil 8: Prüfskript, Kennzahlen, Testlauf-Auftragsvorlage

1. werkzeuge/blatt-pruef.py (Messgrenzen aus
   bericht-testlauf-2026-09-25.md): Zweigzeile, Abhakseite,
   Verzeichniszeile und Schwach-Bausteine erkennen. Die Namen der
   Vorlage Stufe 5 (../blattbau/mathblatt.sty, wenn der Ordner
   den heutigen Stand trägt; sonst aus dieser Liste):
   \zweigzeile{...} als zweite Zeile unter \einheitenkopf;
   Umgebung abhakseite mit \abhak{nr}{titel}; \verzeichniszeile
   mit \verz{label}{text}; \swfrage (Teilaufgabe mit Raster und
   Darstellung daneben) als Teilaufgabenzähler. Kennzahlen dazu:
   Zweigzeilen je Einheitenkopf (Zahl · Zahl), Abhakseite ja/nein
   mit Zahl der Zeilen, Verzeichniszeile ja/nein. Die Zuordnung
   Blattnummer → Katalog-Einheit nicht mehr über die Nummer,
   sondern über den Titel im Einheitenkopf gegen die Titel der
   Lerneinheiten des Eintrags (Wortstamm, Lesart im Skriptkopf);
   ohne Treffer alle Einheiten, mit Vermerk. Alter Modus bleibt
   byteidentisch, wo kein neuer Baustein vorkommt.
2. blaetter/kennzahlen.md neu bauen (Freigabe des Lehrers vom
   25.09.); blaetter/testlauf-2026-09-25/kennzahlen.md nicht
   anfassen.
3. werkzeuge/testlauf-auftrag.md: Kopie von
   archiv/auftrag-testlauf-2026-09-25.md mit drei Änderungen –
   Blätter nacheinander statt gleichzeitig (ein Sub-Agent nach dem
   anderen, oder Regelweg claude -p, der jetzt angemeldet ist;
   den Regelweg zuerst versuchen, Ersatzweg als zweite Stufe),
   Uhrzeiten in stand.md nur aus Get-Date, Ordnername
   blaetter/testlauf-<datum>/ und Berichtsname mit dem Datum des
   Laufs. Kopfzeile: „Vorlage; für einen Lauf in die Wurzel als
   auftrag-testlauf.md kopieren, Datum eintragen." Der Testlauf
   selbst läuft nicht.

Gegenprobe Teil 8 (nacht-bericht-2026-09-26.md Teil 1,
bericht-testlauf-2026-09-25.md Nebenbefund):
blaetter/prozentrechnung/2026-09-24/pdf/fokus_a.pdf: 4 Seiten,
16 Hauptnummern, 54 Teilaufgaben; Daten_E1.pdf (2026-09-22)
„Typen ohne Treffer" 7 von 15 mit dem heutigen Katalog.

Commit „werkzeuge: blatt-pruef.py Stufe 5, Kennzahlen neu,
Testlauf-Vorlage".

## Teil 9: CAS-Nachtrag Brandenburg 2017 und 2018

abitur/abi.md § 7 (Regel für den Nachtrag: papier mit Zusatz
-cas; eigene Zeile nur für Teilaufgaben, die von der WTR-Fassung
abweichen, kenntlich am Präfix „CAS:" im Aufgabentitel;
CAS-Delta nach abi-pruefungen.md § 4), CLAUDE.md § 2 und § 3,
abi-quellen.md § 8 (Dateien unter hefte/abi/). Zwei Läufe, je ein
Heft, je ein Commit: 2017-bb-ea-cas, dann 2018-bb-ea-cas. Die
Berliner CAS-Hefte bleiben zurückgestellt (abi.md § 9, Abgrenzung
offen). Jeder Lauf: Heft lesen, abi-bau.py füllen, Skript ohne
Fehler, Selbstprüfung, abi-pruefungen.md nachführen (Status,
Kennzahlen, § 4, § 5). Fehlt die Datei unter hefte/abi/: Teil
offen mit Grund.

Gegenprobe Teil 9 (abi-pruefungen.md § 2): Seiten 10 bzw. 12,
BE 100 je Heft; die Zahl der „CAS:"-Aufgaben je Heft in den
Bericht.

Commits „abitur: 2017-bb-ea-cas erfasst", „abitur: 2018-bb-ea-cas
erfasst".

## Teil 10: 2017-be-gk erfassen, Reserve-Stapel dazu

abi-pruefungen.md § 2: 2017-be-gk (BE, grundlegend, WTR, 8 Seiten,
80 BE, „nicht erfasst"), Datei hefte/abi/2017-be-gk.pdf. Regel
„Eine Vormerkung überlebt keinen Auftrag" (CLAUDE.md § 2 Schritt
3, abi.md § 7): Poolaufgaben des Hefts liegen in den Reserve-
Stapeln 2017-ga-A (10 Dateien) und 2017-ga-B (WTR, 5 Dateien)
(iqb-pruefungen.md § 2). Reihenfolge:

1. Stapel 2017-ga-A erfassen (CLAUDE.md § 4, iqb-bau.py), Commit.
2. Stapel 2017-ga-B erfassen, Commit.
3. Heft 2017-be-gk erfassen; Poolaufgaben mit „Dublette von:"
   bzw. „Abgewandelt von:", keine Vormerkung; Commit.
4. Abgleichlauf abitur-abgleich.py und die Selbstprüfung beider
   Bauskripte mit leerem ZEILEN; Commit, falls etwas geändert.

Scheitert Punkt 1 oder 2 nach zwei Anläufen, entfällt Punkt 3
(sonst entstünde eine Vormerkung, die den Auftrag überlebt);
Grund in Standdatei und Bericht.

Gegenprobe Teil 10 (abi-pruefungen.md § 2, iqb-pruefungen.md
§ 2): 2017-be-gk 80 BE über alle Aufgaben; jeder Stapel
vollständig laut iqb-quellen.csv (Skript prüft es).

## Abschluss

- faellig.md: erledigte Posten aus § 2 streichen und in § 4
  eintragen (Teil 1–6, 8; Teil 9 und 10 als Erfassung; Teil 7 als
  „Vorschlag liegt vor, Entscheidung im Chat" – der Posten bleibt
  in § 2 mit diesem Zusatz). Den Posten „270 Paare ohne
  Gegenrichtung" (Prüfung 4) als „erledigt, kein Bedarf –
  Entscheidung des Lehrers 25.09.2026: v4.3 löst die Zone nur
  rückwärts auf, die Vorwärtsrichtung braucht kein Prompt" nach
  § 4. Neue Posten aus dem Lauf eintragen.
- nacht-stand-2026-09-27.md und diesen Auftrag nach archiv/
  verschieben (git mv; bei Namensgleichheit „b" anhängen).
- Bericht nacht-bericht-2026-09-27.md in der Wurzel, README-
  Zeile. Commit „archiv: auftrag-nacht-2026-09-27, Bericht".

## Bericht

nacht-bericht-2026-09-27.md und im Chat. Erste Zeile das Modell.
Je Teil: was geändert ist (Dateien, Zahlen), die Gegenprobe im
Wortlaut mit Belegdatei, eigene Entscheidungen, offene Punkte mit
Grund. Teil 1: neue Zahl der Marken-Zeilen und Typklammern. Teil
5: die Zuordnung alte Datei → Eintrag als Tabelle. Teil 7: nur
die Zeilenzahl je Abschnitt (der Chat liest die Datei). Teil 9
und 10: je Heft und Stapel Zeilen, neue Typen, Poolquote, „?"-
Zeilen. Letzte Zeile: „Push origin drücken".
