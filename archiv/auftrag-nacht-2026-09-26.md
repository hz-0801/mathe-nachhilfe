# Auftrag Nacht 2026-09-26: Prüfskript für Blätter,
# Auftrag Nacht 2026-09-26: Prüfskript für Blätter,
# Prüfungswort-Belege, Sek-II-Ordnung, Ermessensfälle gruppieren

Modell: Opus (Zuordnungen mit Lesart in Teil 2 und 3). Läuft
ohne den Lehrer: keine Rückfrage, Standdatei, Commit je Teil,
Fehlerregel je Teil.

## Ausgangslage

ziel.md (Stand 25.09.2026). Die Nacht vom 25.09. hat
katalog/_klassen-belege.md (Klasse je Lerneinheit aus den
Lehrwerken) und die fremden Aufgabensammlungen geliefert; das
Bauskript liegt unter werkzeuge/klassen-belege.py. Dieser
Auftrag baut vier Dinge, die alle ohne Urteil gehen:

- Teil 1: ein Prüfskript, das je Blatt Kennzahlen misst (ziel.md
  § 5 und Übergabe: „Prüfskript, dann Nachtbau").
- Teil 2: Belege für das Prüfungswort je Lerneinheit und Typ
  (ziel.md § 2 „Überschriften": „P10 oft", „P10", „keine
  P10-Aufgabe"; Sek II „Abitur GK/LK", „FHR"; Quelle: Ertrag je
  Typ aus dem Prüfungskatalog).
- Teil 3: die Ordnung der Sek-II-Einträge nach Halbjahr und
  Kursart (ziel.md § 5, letzter Punkt).
- Teil 4: die 250 Ermessensfälle aus _klassen-belege.md nach
  Sorte gruppiert, damit das Urteil im Chat gebündelt fallen kann.

Du änderst keinen Katalogeintrag und keinen Prompt.

## Regeln

- Shell PowerShell: kein Heredoc, kein sed. Dateien schreiben mit
  [System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false))); Zeilenenden
  LF; nach dem Schreiben prüfen (keine BOM, kein CR).
- Python nur %LocalAppData%\Programs\Python\Python312\python.exe;
  git über die git.exe von GitHub Desktop, mit -c core.pager=cat,
  commit -m; kein Push.
- pdftotext und pdfinfo liegen im MiKTeX-Ordner
  (%LocalAppData%\Programs\MiKTeX\miktex\bin\x64).
- Nichts löschen; verschieben nur mit git mv. Keine Handedits an
  CSV; abgeleitete Dateien tragen die Zeile „Abgeleitet von
  <skript>, nie von Hand ändern".
- Grenzen sind Zählgrenzen, nie Zeit. Fehlerregel überall: ein
  Schritt, der zweimal scheitert, wird als „offen" mit Grund in
  Standdatei und Bericht eingetragen; der nächste Punkt folgt.
- Standdatei nacht-stand-2026-09-26.md in der Wurzel: je Teil
  eine Zeile „offen / läuft / erledigt" mit dem letzten fertigen
  Punkt; ein Neustart liest sie zuerst.
- README.md ist die Landkarte: jede neue Datei bekommt dort
  einen Satz, im selben Commit.
- Skripte gehören mit allen Daten, die sie brauchen, ins Repo;
  nichts bleibt im Scratchpad.

## Teil 1: Prüfskript werkzeuge/blatt-pruef.py

Zweck: Was die Befunde vom 24.09. (befund-schwach-blatt-
2026-09-24.md) von Hand gezählt haben, misst das Skript für
jedes Blatt unter blaetter/. Ergebnis ist eine Tabelle, mit der
zwei Läufe desselben Themas verglichen werden.

Eingabe: alle Ordner blaetter/<thema>/<datum>/ mit src/*.tex
und pdf/*.pdf. Die LaTeX-Makros der Vorlage stehen in
../blattbau/ (Ordner neben diesem Repo; Vorlage und Anleitung
dort lesen); fehlt der Ordner, leite die Makronamen aus den
tex-Dateien selbst ab und schreib das in den Bericht.

Je Blatt (je PDF-Datei mit zugehöriger tex-Datei) diese
Kennzahlen:
1. Seiten (pdfinfo).
2. Hauptnummern gesamt; Teilaufgaben gesamt.
3. Hauptnummern je Seite und Teilaufgaben je Seite (pdftotext
   -layout mit Seitentrennung; eine Hauptnummer zählt auf der
   Seite, auf der sie beginnt).
4. Titel je Hauptnummer, wortgleich, und die Form: „Kurzname –
   Formwort" (Muster der Version 4.2), „Ich kann …", anderes.
5. Darstellungen je Hauptnummer (Streifen, Tabelle, Skizze,
   Koordinatensystem, Balken – nach den Makros der Vorlage
   gezählt) und die letzte Hauptnummer, die eine Darstellung
   trägt.
6. Antwortform je Hauptnummer: Raster mit Zeilen (wie viele),
   Antwortlinie, Kasten, nichts.
7. Merkkästen (Zahl und Position: vor oder nach den Aufgaben).
8. Fachwörter: die fett gesetzten Begriffe des Abschnitts
   „Merkkasten" im Katalogeintrag des Themas (Register
   blaetter/index.md nennt den Eintrag; fehlen fette Begriffe,
   die Begriffe vor einem Doppelpunkt) und die Hauptnummer
   ihres ersten Auftretens im Blatt.
9. Sprossenabgleich: Für jeden Typ des Katalogeintrags („Typen je
   Lerneinheit") ob ein Titel oder Aufgabentext des Blatts ihn
   nennt (Wortstamm genügt, Lesart im Skriptkopf dokumentiert);
   Liste der Typen ohne Treffer.

Ausgabe: blaetter/kennzahlen.md (abgeleitet), je Blatt ein
Abschnitt mit den Kennzahlen 1–9 und oben eine Vergleichstabelle
über alle Blätter mit den Spalten Thema, Datum, Prompt-Version
(aus index.md), Datei, Seiten, Hauptnummern, Teilaufgaben,
Hauptnummern je Seite, Teilaufgaben je Seite, Titelform, letzte
Darstellung, Typen ohne Treffer. Aufruf ohne Argumente baut
alles neu; mit Pfad nur ein Blatt.

Gegenprobe Teil 1 (bekannte Werte aus dem Befund vom 24.09.;
Abweichung ist ein Befund, kein Grund, das Skript anzupassen):
blaetter/prozentrechnung/2026-09-24/pdf/fokus_a.pdf hat 4 Seiten,
16 Hauptnummern, 52 Teilaufgaben, 16 Hauptnummern mit Titel der
Form „Kurzname – Formwort"; der Streifen erscheint bis
Hauptnummer 8, danach nicht mehr; der Merkkasten steht oben.

Abschluss: README-Zeilen (werkzeuge/, blaetter/); Commit
„werkzeuge: blatt-pruef.py, Kennzahlen je Blatt".

## Teil 2: Prüfungswort-Belege

Schreibe katalog/_pruefungswort-belege.md, gebaut von
werkzeuge/pruefungswort-belege.py (Skript und Daten ins Repo).

Sek I (29 Einträge): Je Lerneinheit und je Typ des Eintrags die
P10-Typen aus msa/msa-typen.csv, die ihn prüfen (Zuordnung nach
Inhalt; themen.csv gibt die Thema-Ebene vor, die Typ-Ebene ist
deine Zuordnung mit Grund, wo sie nicht wortgleich ist). Je
zugeordnetem P10-Typ aus msa/msa-ertrag.csv: ertrag,
jahre_haupt, jahre_gesamt, erster, letzter, basis, kontext.
Je Lerneinheit die Summe: P10-Jahrgänge, in denen mindestens ein
Typ der Einheit vorkam (von 13); Zahl der P10-Typen; Summe
ertrag. Einheiten ohne P10-Typ: „keine P10-Aufgabe" mit dem
Vermerk aus themen.csv, wenn dort einer steht.

Verteilung für die Schwelle „oft" (der Lehrer setzt sie): Tabelle
über alle Sek-I-Einheiten, sortiert nach P10-Jahrgängen; dazu
die Zahl der Einheiten je Wert (13, 12, …, 0). Dasselbe je Typ.

Sek II (die übrigen Einträge, Tabelle Sek II in katalog/index.md):
dieselbe Zuordnung gegen abitur/abi-katalog.csv (Spalten GK/LK
und Jahr, wie dort geführt) und, wenn fhr/ einen Katalog hat,
gegen ihn. Je Einheit: Abitur-Jahrgänge GK, LK, FHR-Jahrgänge.

Gegenprobe Teil 2: prozentrechnung, Einheit „Prozentsatz" muss
P10-Typen aus dem Thema „Prozentrechnung" der themen.csv
bekommen; trigonometrie, Typ mit dem Sinussatz: msa-ertrag.csv
führt „Sinussatz Seite berechnen" mit jahre_haupt 9, erster 2014,
letzter 2025 – diese Zahlen müssen in der Belegdatei wortgleich
stehen. Abweichung ist ein Befund.

Abschluss: README-Zeilen; Commit „katalog: Prüfungswort-Belege
je Lerneinheit und Typ".

## Teil 3: Sek-II-Ordnung

Schreibe katalog/_sek2-ordnung-belege.md, gebaut von
werkzeuge/sek2-ordnung-belege.py (Skript und Daten ins Repo).
Zweck: Für die Oberstufe ordnen Halbjahr und Kursart statt der
Klasse (ziel.md § 5).

Je Sek-II-Eintrag und Lerneinheit, nach dem Muster von
_klassen-belege.md:
- Rahmenlehrplan Sek II (quellen/quelle-rlp-gost-be-2022-
  mathematik.txt und quelle-rlp-gost-bb-2022-mathematik.txt;
  für FHR quelle-rlp-fos-bb-2019-mathematik.txt): Kurshalbjahr
  (ma-1 bis ma-4 oder wie dort benannt), Grund- oder
  Leistungskurs, mit Zitat und Zeilennummer.
- Lehrwerke mit Verzeichnis im Repo: Bigalke/Köhler Brandenburg
  (GK 11, LK 11, GK 12, LK 12), Fundamente Sek II Ausgabe B,
  Elemente Sek II (NRW, nur Gegenprobe), Neue Wege Sek II Berlin
  2011 (nur Gegenprobe): Band, Kapitelzeile wortgleich, Seite,
  Zeilennummer. Bigalke/Köhler ist Reihenfolge-Quelle, keine
  Form-Quelle (Beschluss 25.09.).
- Zusammenfassung je Einheit: „Halbjahr: … · GK/LK: …" und
  „nur LK: ja/nein" (ja, wenn RLP oder beide LK-Bände die Einheit
  nur im LK führen).
- Ermessen mit Grund, „keine Stelle" ist ein Ergebnis.

Gegenprobe Teil 3: Die Einheit zur Ableitung (Differenzial-
rechnung) liegt in Bigalke/Köhler GK 11 und LK 11 und im RLP im
ersten Kurshalbjahr; die Stochastik-Einheiten liegen in Band 12.
Abweichung ist ein Befund.

Abschluss: README-Zeilen; Commit „katalog: Sek-II-Ordnung nach
Halbjahr und Kursart (Vorschlagsliste)".

## Teil 4: Ermessensfälle gruppieren

Lies katalog/_klassen-belege.md und schreibe
katalog/_klassen-ermessen.md (abgeleitet, Skript
werkzeuge/klassen-ermessen.py): alle Zeilen „Ermessen:" mit
Eintrag, Einheit, Reihe, Zitat und Grund, gruppiert nach der
Sorte des Grundes (Sorten aus dem Wortlaut ableiten, etwa
„Verzeichnis zu grob", „Inhalt verteilt auf zwei Kapitel",
„Wortlaut weicht ab", „Wiederholungskapitel", „Förderheft nach
Blocktitel"); je Sorte die Zahl und die Fälle. Oben die Sorten
mit Zahl, sortiert. Keine Bewertung.

Gegenprobe Teil 4: Die Summe aller Fälle ist 250 (Zahlenblock
von _klassen-belege.md); Abweichung ist ein Befund.

Abschluss: README-Zeile; Commit „katalog: Ermessensfälle der
Klassenbelege gruppiert".

## Abschluss

- nacht-stand-2026-09-26.md und diesen Auftrag nach archiv/
  verschieben (git mv; bei Namensgleichheit „b" anhängen).
- Bericht nacht-bericht-2026-09-26.md in der Wurzel, README-
  Zeile. Commit „archiv: auftrag-nacht-2026-09-26, Bericht".

## Bericht

nacht-bericht-2026-09-26.md und im Chat. Erste Zeile das Modell.
Teil 1: die Vergleichstabelle aus kennzahlen.md vollständig; die
Gegenprobe im Wortlaut. Teil 2: die Verteilungstabelle der
Einheiten nach P10-Jahrgängen; die Zahl der Einheiten ohne
P10-Typ; die Gegenprobe im Wortlaut. Teil 3: je Sek-II-Eintrag
eine Zeile Halbjahr/Kursart; die Zahl der Einheiten „nur LK";
die Gegenprobe. Teil 4: die Sorten mit Zahl. Je Teil: offene
Punkte mit Grund, eigene Entscheidungen. Letzte Zeile: „Push
origin drücken".
