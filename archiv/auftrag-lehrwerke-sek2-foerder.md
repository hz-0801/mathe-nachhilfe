# Auftrag: Lehrwerke Sek II und Förderhefte über die Deutsche
Nationalbibliothek sichern

Stand 2026-09-24. Ordner mathe-nachhilfe. Modell Sonnet.
Läuft unbeaufsichtigt; nichts wartet auf den Lehrer.

## Ausgangslage

Die Deutsche Nationalbibliothek führt zu fast jedem Schulbuch das
Inhaltsverzeichnis als PDF: Katalogsatz https://d-nb.info/<IDN>,
Inhaltsverzeichnis https://d-nb.info/<IDN>/04. Suche über
werkzeuge/dnb-sru.py (CQL-Abfrage als Argument, Ausgabe je Treffer
IDN | Jahr | ISBN | Titel | TOC:ja/-). Der Auftrag vom 24.09.
(archiv/auftrag-lehrwerke-inhalt.md) hat damit die Landesausgaben
BE/BB Kl. 7–10 gesichert; Muster für Dateiform und Fundliste sind
quellen/quelle-cornelsen-fundamente-bb-ausgabeb2024-inhalt.txt und
quellen/lehrwerke-fundliste.md. Weitere CQL-Felder: tit (Titel),
num (ISBN), jhr (Jahr), sw (Schlagwort), per (Person).

Zweck, damit du Zweifelsfälle entscheiden kannst:
- Teil A (Sek II): Kapitelfolge der Oberstufenbände für die
  Verortung der Sek-II-Themen und die Decke der Klasse 10.
- Teil B und C (Förderhefte): Vorbild für die Option „schwach“ des
  Unterrichtsblatts und für Themen unter Klasse 8. Aus B kommt,
  welchen Stoff ein Förderheft weglässt; aus C, wie eine Seite
  aussieht, die ein schwacher Schüler bearbeiten kann. Das
  Bundesland ist hier unwichtig, die Breite zählt.

## Regeln

- Python nur über %LocalAppData%\Programs\Python\Python312\
  python.exe; git über die git.exe von GitHub Desktop; PowerShell
  (kein Heredoc, kein sed). git mit -c core.pager=cat, commit -m,
  nicht pushen.
- Nichts löschen. Kein Login, keine Registrierung, kein Warenkorb.
  Verlagsseiten nur lesen (Filter anklicken erlaubt).
- Keine Rückfragen. Was der Auftrag nicht regelt, entscheidest du
  und schreibst es in den Bericht unter „Eigene Entscheidungen“.
- Standdatei quellen/lehrwerke-stand-2026-09-24.md (Datei 2):
  nach jedem abgeschlossenen Teil und innerhalb von Teil B nach
  jeder Sorte fortschreiben (offen → erledigt, mit Zahl der
  gesicherten Bände). Ein Neustart liest sie und macht beim
  ersten offenen Punkt weiter.
- Ein Commit je Teil (A, B, C), dazu einer für Register und
  Bericht. Vor jedem Commit git status lesen; hefte/ darf nie
  im Commit sein.
- Fehlerfall: Liefert eine Abfrage, ein Download oder pdftotext
  nach zwei Anläufen nichts, wird der Band als „nicht gefunden“
  mit Grund eingetragen und der nächste genommen. Bricht ein Teil
  ab, wird der Teil in der Standdatei als „abgebrochen: <Grund>“
  vermerkt und der nächste Teil begonnen.
- Zeitgrenzen: Teil A je Reihe höchstens 20 Minuten; Teil B je
  Sorte höchstens 90 Minuten; Teil C je Reihe höchstens 10
  Minuten. Danach Stand eintragen, weiter. Keine Bandgrenze.
- Dateien unter hefte/ sind lokal (.gitignore); Textfassungen
  unter quellen/ werden committet. Aus einem Buch wird nur das
  Inhaltsverzeichnis als Text übernommen (Kapitelnummer, Titel,
  Seite), sonst nichts – auch nicht aus Probeseiten.
- Keine Bewertung, keine Zuordnung zum Katalog. Das Urteil fällt
  im Chat.

## Schritt 0 – Gegenprobe

python werkzeuge/dnb-sru.py 'num=9783060428175' muss den Satz
1338042475 mit TOC:ja zeigen. Sonst Skript reparieren (Endpunkt
services.dnb.de/sru/dnb, MARC21-xml), nicht die Aufgabe.
pdftotext muss aufrufbar sein; sonst Pfad suchen (MiKTeX unter
%LocalAppData%\Programs\MiKTeX\miktex\bin\x64 oder Poppler), im
Bericht nennen.

## Teil A – Sek II, Landesausgaben Berlin/Brandenburg

Gesucht: Schulbücher der gymnasialen Oberstufe mit Ausgabe für
Berlin und/oder Brandenburg, Einführungsphase und
Qualifikationsphase (Grundkurs und Leistungskurs, ggf. ein Band
für beide), Erscheinungsjahr ab 2014 (Berliner GOST-Plan gilt
seit 2014). Reihen, mit denen die Suche beginnt; weitere, die
die Verlagsseiten unter „Berlin“ oder „Brandenburg“ und
„Oberstufe“ zeigen, kommen dazu:

- Klett: Lambacher Schweizer, Ausgabe Berlin/Brandenburg
- Cornelsen: Fundamente der Mathematik, Ausgabe Berlin/Brandenburg
- Cornelsen: Bigalke/Köhler Mathematik, Ausgabe Berlin/Brandenburg
- Westermann: Elemente der Mathematik SII, Ausgabe Berlin/
  Brandenburg
- Westermann: Mathematik Neue Wege SII (Ausgabe 2011 für Berlin
  u. a. und jede jüngere Ausgabe, die Berlin oder Brandenburg
  nennt)

Vorgehen je Reihe: ISBNs der Schülerbände über die Verlagsseite
(Reihe, Bundesland-Filter), dann DNB num=<ISBN>; fehlt der
Bundesland-Filter, DNB-Titelsuche mit tit="<Reihe>" and
tit="Berlin" bzw. tit="Brandenburg" und Jahr. Gibt es keine
Landesausgabe, die Allgemeine Ausgabe der Reihe als Gegenprobe
sichern und so kennzeichnen. Fehlt der TOC-Link, Verlagsseite
(Inhaltsverzeichnis als PDF) prüfen, sonst „nicht gefunden“.

Ablage: PDF nach hefte/lehrwerke/<verlag>-<reihe>-<ausgabe>-
<band>-inhalt.pdf (lokal); Text mit pdftotext -layout; je Reihe
eine Datei quellen/quelle-<verlag>-<reihe>-sek2-<ausgabe>-
inhalt.txt nach dem Muster der Sek-I-Dateien: Kopf (Werk,
Ausgabe, Schulform laut Verlag, je Band Titel, ISBN, IDN, Adresse
d-nb.info/<IDN>/04, Datum), dann je Band „== <Band> ==“ (z. B.
„== Einführungsphase ==“, „== Qualifikationsphase Leistungskurs
==“) und das Inhaltsverzeichnis.

Dazu die zwei offenen Bestätigungen aus dem Auftrag vom 24.09.:
- Fundamente der Mathematik, Ausgabe B ab 2017, Kl. 7, 8 und 10:
  auf cornelsen.de die Reihe öffnen, Bundesland Berlin oder
  Brandenburg, ISBN je Klasse ablesen, DNB num=<ISBN>, TOC
  sichern und in quelle-cornelsen-fundamente-bb-ausgabeb2017-
  inhalt.txt ergänzen; die dort notierten Kandidaten als
  bestätigt oder verworfen kennzeichnen.
- Mathematik heute: auf westermann.de prüfen, ob die ISBNs
  9783507812604/-2673/-2741/-2819 zur Ausgabe für Berlin und
  Brandenburg gehören; Ergebnis in den Kopf von
  quelle-westermann-mathematikheute-bebb-inhalt.txt eintragen
  (bestätigt / nicht bestätigt, mit Fundstelle).

Commit: „quellen: Inhaltsverzeichnisse Sek II BE/BB (DNB)“.

## Teil B – Förderhefte, bundesweit, Klasse 5–10

Gesucht sind drei Sorten; je Sorte 90 Minuten, alle drei werden
begonnen, auch wenn eine unvollständig bleibt:

Sorte 1 – Förder- und Basishefte zu Regelreihen: die Hefte zu
den Reihen, die schon im Repo liegen (Sekundo, Schnittpunkt
Mathematik, Mathematik Ausgabe 2023, Fundamente der Mathematik,
Elemente der Mathematik, Mathematik heute, Lambacher Schweizer),
mit Titelbestandteilen wie Förderheft, Basisheft, Basistraining,
Arbeitsheft Basisniveau, Fördermaterial. Verlagsseite der Reihe
öffnen, alle Hefttitel notieren, ISBNs, DNB num=<ISBN>.

Sorte 2 – eigenständige Basis- und Grundwissenreihen, ohne
Bindung an ein Schulbuch: DNB-Suchen wie
tit="Grundwissen" and tit="Mathematik" and jhr>2009,
tit="Basiswissen" and tit="Mathematik",
tit="Fördern" and tit="Mathematik",
tit="Training" and tit="Mathematik" and tit="Grundlagen".
Nur Treffer mit TOC:ja, Jahr ab 2010, Klasse 5–10 im Titel
oder in der Reihe; Nachschlagewerke und Prüfungstrainer (Abitur,
MSA) gehören nicht dazu. Reihen zuerst vollständig (alle Bände),
dann die nächste Reihe.

Sorte 3 – Hefte für den Förderschwerpunkt Lernen und für die
Hauptschule/Oberschule mit Grundniveau: DNB-Suchen wie
sw="Förderschule" and tit="Mathematik" and jhr>2009,
sw="Lernbehinderung" and tit="Mathematik",
tit="Klick" and tit="Mathematik" (Cornelsen),
tit="Stark in Mathematik" (Westermann),
tit="Lernstufen Mathematik" (Cornelsen),
tit="Maßstab" and tit="Mathematik" (Westermann).
Die genannten Titel sind Startpunkte: prüfen, ob es sie gibt,
nicht voraussetzen. Regel wie Sorte 2.

Ablage: wie Teil A, Dateiname quellen/quelle-<verlag>-<reihe>-
foerder-<ausgabe>-inhalt.txt, je Klasse „== Klasse n ==“. Der
Kopf nennt die Sorte (1, 2 oder 3) und die Schulform laut Verlag.

Fundliste: quellen/foerderhefte-fundliste.md, Tabelle je Band:
Sorte, Verlag, Reihe, Ausgabe, Klasse, ISBN, IDN, Fund (DNB /
Verlag / nicht gefunden), Vollständigkeit. Am Ende je Sorte eine
Zeile: Bände gesichert, Zeitgrenze erreicht ja/nein, Suchbegriffe,
die nichts brachten.

Commit: „quellen: Inhaltsverzeichnisse Förderhefte (DNB)“.

## Teil C – Probeseiten der Förderhefte

Zu jeder Reihe aus Teil B, in der Reihenfolge der Fundliste:
Auf der Verlagsseite des Hefts nach frei zugänglichen Probeseiten
suchen („Blick ins Buch“, „Leseprobe“, „Probeseiten“,
„Musterseiten“; auch kapiert.de für Westermann). Ohne Login, ohne
Formular. Jede frei angebotene Probe als PDF (oder Bildseiten)
nach hefte/lehrwerke/probeseiten/<verlag>-<reihe>-<klasse>-
probe.<ext> (lokal). Zeigt der Verlag die Probe nur als
Bildbetrachter im Browser ohne Download, wird nichts gesichert
und „nur Betrachter“ eingetragen.

Ins Repo kommt quellen/foerderhefte-formen.md: je gesicherter
Probe eine Tabellenzeile mit Reihe, Klasse, Seitenzahl der Probe,
Thema der Probeseiten (nur der Kapiteltitel) und den
Aufgabenformen, die auf den Seiten vorkommen, angekreuzt aus
dieser festen Liste und nur aus ihr:
  B  vorgerechnetes Beispiel
  L  dieselbe Aufgabe mit Lücken zum Ausfüllen
  F  freie Aufgabe ohne Vorgabe
  M  Merkkasten oder Regelkasten
  R  Rechenraster (ein Schritt je Zeile, Kästchen für Zahlen)
  Z  Zahlenstrahl, Bild oder Tabelle als Hilfe
  S  Selbsttest oder Kontrollkästchen
  Lö Lösungen im Heft
  W  Wortschatz- oder Lesehilfe (Fachwort erklärt, Text kurz)
Dazu eine Zahl: wie viele Aufgaben stehen auf einer Seite (Mittel
über die Probe, gerundet). Kein Aufgabentext, kein Urteil, keine
Beschreibung darüber hinaus.

Commit: „quellen: Probeseiten Förderhefte, Formenliste“.

## Register

- quellen/quellen.md: die neuen Textdateien nach dem Muster der
  vorhandenen Einträge.
- quellen/lehrwerke-fundliste.md: dritte Tabelle „Sek II“ (Verlag,
  Reihe, Ausgabe, Band, ISBN, IDN, Fund, Vollständigkeit) und die
  beiden Bestätigungen als je eine Zeile in der zweiten Tabelle.
- README.md, Abschnitt quellen/: je neue Datei ein Satz
  (Textdateien, foerderhefte-fundliste.md, foerderhefte-formen.md,
  lehrwerke-stand-2026-09-24.md, der Bericht).
- Commit: „quellen: Register Sek II und Förderhefte“.
- Auftrag nach archiv/ verschieben, Commit „archiv:
  auftrag-lehrwerke-sek2-foerder“.

## Prüfungen

1. Schritt 0 bestanden (Satz 1338042475, TOC:ja).
2. Jede Textdatei: je Band mindestens die Kapitel erster Ebene
   mit Seitenzahl; Kopf vollständig (ISBN, IDN, Adresse, Datum).
3. Fundlisten: jede Zeile mit Fund „DNB“ oder „Verlag“ hat eine
   Textdatei mit passendem Abschnitt; jede Textdatei hat ihre
   Zeilen in der Fundliste.
4. foerderhefte-formen.md: nur Kürzel aus der festen Liste;
   jede Zeile hat eine lokale Datei unter hefte/lehrwerke/
   probeseiten/.
5. git status vor jedem Commit: kein Pfad unter hefte/.
6. Standdatei: alle Punkte tragen einen Stand.

## Bericht

Als quellen/lehrwerke-sek2-foerder-bericht-2026-09.md (im
Register-Commit) und im Chat. Erste Zeile: das Modell, mit dem
der Auftrag lief. Dann je Teil: Zahl der gesicherten Bände, Zahl
„nicht gefunden“ mit Gründen, Zeitgrenze erreicht ja/nein, je
Reihe eine Zeile (Bände, Fund, Vollständigkeit). Teil C: Zahl der
Reihen mit Probe, ohne Probe, nur Betrachter. Ergebnis der
Prüfungen 1–6. Eigene Entscheidungen, jede in einem Satz mit
Grund. Was ein späterer Auftrag noch holen könnte (Reihen, die
in der Zeitgrenze liegen blieben). Letzte Zeile:
„Push origin drücken“.
