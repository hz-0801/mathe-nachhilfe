# Nachauftrag: Formenliste der Förderhefte, Bigalke/Köhler,
Lücken der Sorte 1

Stand 2026-09-24. Ordner mathe-nachhilfe. Modell Sonnet.
Läuft unbeaufsichtigt; nichts wartet auf den Lehrer.

## Ausgangslage

Der Auftrag vom 24.09. (archiv/auftrag-lehrwerke-sek2-foerder.md,
Bericht quellen/lehrwerke-sek2-foerder-bericht-2026-09.md) hat
Inhaltsverzeichnisse gesichert, aber keine Formenliste: Die Regel
„nur Betrachter → nichts sichern“ war falsch. Die Formenliste
braucht keine Datei, sie braucht das Ansehen der Seiten – und
das geht im Betrachter. Dieser Auftrag holt das nach, sucht
Bigalke/Köhler über das Personenfeld und schließt die Lücken der
Sorte 1.

Zweck der Formenliste: Vorbild für die Option „schwach“ des
Unterrichtsblatts – wie eine Seite aussieht, die ein schwacher
Schüler bearbeiten kann. Es zählt die Form, nicht der Inhalt.

## Regeln

- Python nur über %LocalAppData%\Programs\Python\Python312\
  python.exe; git über die git.exe von GitHub Desktop; PowerShell
  (kein Heredoc, kein sed). git mit -c core.pager=cat, commit -m,
  nicht pushen.
- CQL-Abfragen mit Anführungszeichen an dnb-sru.py über den
  Stop-Parsing-Operator übergeben, wie im Bericht vom 24.09.
  beschrieben (--% und verdoppelte Anführungszeichen); das Skript
  bleibt unverändert.
- Nichts löschen. Kein Login, keine Registrierung, kein Warenkorb.
  Verlagsseiten nur lesen.
- Keine Rückfragen. Was der Auftrag nicht regelt, entscheidest du
  und schreibst es unter „Eigene Entscheidungen“.
- Zählgrenzen statt Zeit (Zeitgrenzen sind nicht messbar): je
  Betrachter höchstens 12 Seiten ansehen; je Reihe höchstens 10
  DNB-Abfragen oder Seitenaufrufe; Teil 3 höchstens 12 neue Bände.
  Ist eine Grenze erreicht: Stand eintragen, weiter.
- Standdatei quellen/lehrwerke-stand-2026-09-24b.md (Datei 2):
  nach jedem Teil fortschreiben; ein Neustart macht beim ersten
  offenen Punkt weiter.
- Ein Commit je Teil, einer für Register und Bericht. Vor jedem
  Commit git status lesen; hefte/ darf nie im Commit sein.
- Fehlerfall: nach zwei Anläufen „nicht gefunden“ mit Grund,
  nächster Punkt.
- Seitenbilder aus Betrachtern werden nur lokal unter hefte/
  lehrwerke/probeseiten/ abgelegt (.gitignore). Ins Repo kommt
  aus einer Seite nichts als die Kürzel und Zahlen der
  Formenliste – kein Aufgabentext, kein Bild, keine
  Beschreibung darüber hinaus.

## Teil 1 – Formenliste aus den Betrachtern

Für jede der folgenden Quellen den Betrachter öffnen. Ein
Betrachter lädt seine Seiten als Bilddateien; die Adressen der
Bilder stehen im Quelltext oder in den Netzwerkaufrufen der
Seite (index.html, dazu meist eine Konfigurationsdatei mit der
Seitenliste). Die Bilder mit Invoke-WebRequest laden und mit dem
Lesewerkzeug ansehen; höchstens 12 Seiten je Betrachter, bevorzugt
Seiten mit Aufgaben, nicht Umschlag oder Inhaltsverzeichnis.

Quellen:
a) Cornelsen, Klick! – Mathematik, Ausgabe ab 2024, Kl. 5, 6, 7:
   Produktseite (z. B. cornelsen.de/produkte/klick-schulbuch-5-
   schuljahr-9783060013050), „Blick ins Buch“
   (static.cornelsen.de/…/index.html). Je Klasse ein Betrachter.
b) Kohl Verlag, Grundwissen Mathematik, Klasse 5 bis 10 (die
   Linie mit je einem Band je Klasse, nicht „Freiarbeit“):
   kohlverlag.de, Produktseite je Band, „Leseprobe“
   (leseprobe.kohlverlag.de/html5/…/index.html). Zusätzlich für
   diese Linie ISBN und IDN ermitteln, DNB num=<ISBN>, TOC nach
   dem Muster der vorhandenen Dateien nach quellen/
   quelle-kohlverlag-grundwissenmathematik-foerder-5bis10-
   inhalt.txt sichern (Kl. 5–10, soweit vorhanden).
c) Westermann, Sekundo – Förderheft und Mathematik Ausgabe 2023 –
   Förderheft: kapiert.de nach Probeseiten oder Musterseiten
   dieser Hefte durchsuchen (Pfad /fileadmin/redakteure/
   Lehrwerke/Mathematik/…); sonst westermann.de „Blick ins Buch“.
   Fehlt beides, „keine Vorschau“.
d) Klett, Schnittpunkt Mathematik – Förderheft: klett.de
   Produktseite, „Blick ins Buch“ oder „Probeseiten“; sonst
   „keine Vorschau“.

Ergebnis in quellen/foerderhefte-formen.md: Tabelle je Betrachter
eine Zeile – Reihe, Klasse, Seiten angesehen (Zahl), Thema der
Seiten (nur Kapiteltitel), Formen als Kürzel aus dieser festen
Liste und nur aus ihr, Aufgaben je Seite (Mittel, gerundet):
  B  vorgerechnetes Beispiel
  L  dieselbe Aufgabe mit Lücken zum Ausfüllen
  F  freie Aufgabe ohne Vorgabe
  M  Merkkasten oder Regelkasten
  R  Rechenraster (ein Schritt je Zeile, Kästchen für Zahlen)
  Z  Zahlenstrahl, Bild oder Tabelle als Hilfe
  S  Selbsttest oder Kontrollkästchen
  Lö Lösungen im Heft
  W  Wortschatz- oder Lesehilfe (Fachwort erklärt, Text kurz)
Dazu je Zeile zwei Zahlen: wie viele Zeilen Text stehen auf der
Seite vor der ersten Aufgabe (0 bis n), und wie viele Teilaufgaben
folgen auf ein Beispiel, bevor ein neues Beispiel kommt (Mittel).
Die Prosa-Begründungen der leeren Fassung bleiben unter der
Tabelle als „Stand 24.09. vormittags“ stehen; darunter „Stand
24.09. Nachauftrag“ mit dem Ergebnis je Quelle (Betrachter
gefunden ja/nein, Seiten angesehen, Grenze erreicht).

Commit: „quellen: Formenliste Förderhefte aus Betrachtern“.

## Teil 2 – Bigalke/Köhler über das Personenfeld

DNB-Abfragen: per="Bigalke" and tit="Mathematik" and jhr>2013;
dazu per="Köhler" and tit="Mathematik" and tit="Berlin". Gesucht
sind die Cornelsen-Bände für Berlin und Brandenburg
(Grundkurs/Leistungskurs, Einführungs- und Qualifikationsphase;
Titel wie „Mathematik Berlin – Grundkurs ma-1“ o. ä.). Treffer
mit TOC:ja sichern nach quellen/quelle-cornelsen-bigalkekoehler-
sek2-bebb-inhalt.txt (Muster: die Sek-II-Dateien vom 24.09.);
Bundeslandzuordnung über den Titel oder die Reihenangabe der
DNB, sonst „nicht belegt“ im Kopf. Fehlt jeder Treffer mit TOC,
die Trefferliste (IDN, Jahr, Titel) in den Bericht.

Commit: „quellen: Inhaltsverzeichnisse Bigalke/Köhler (DNB)“.

## Teil 3 – Lücken der Sorte 1 und 3

Höchstens 12 neue Bände, in dieser Reihenfolge:
1. Sekundo – Förderheft Kl. 6, 8, 10 (DNB tit="Sekundo" and
   tit="Förderheft", Jahrgang passend zur Ausgabe 2017/2018).
2. Schnittpunkt Mathematik – Förderheft Kl. 8, 10, dann 5, 6
   (DNB tit="Schnittpunkt" and tit="Förderheft", Differenzierende
   Ausgabe ab 2017).
3. Mathematik heute – „Diagnose und Fördern“ Kl. 7–10, je Klasse
   der jüngste Band (DNB tit="Mathematik heute" and tit="Diagnose
   und Fördern").
4. Klick! – Mathematik, Vorgängerausgabe, Kl. 8, 9, 10 (DNB
   tit="Klick" and tit="Mathematik", Jahr 2008–2018).
Ablage und Fundliste wie beim Auftrag vom 24.09.: Text in die
bestehende Datei der Reihe (neue „== Klasse n ==“-Abschnitte;
für Diagnose und Fördern und für Klick! Vorgänger je eine neue
Datei), Zeilen in quellen/foerderhefte-fundliste.md ergänzen,
„nicht gesichert (Zeitgrenze)“ dort durch das Ergebnis ersetzen.

Commit: „quellen: Förderhefte Sorte 1 und 3 ergänzt (DNB)“.

## Register

- quellen/quellen.md: neue Textdateien nach dem Muster.
- quellen/lehrwerke-fundliste.md: Bigalke/Köhler in der Tabelle
  „Sek II“ eintragen.
- README.md, Abschnitt quellen/: je neue Datei ein Satz; die
  Standdatei und der Bericht.
- Commit: „quellen: Register Nachauftrag Lehrwerke“.
- Auftrag nach archiv/ verschieben, Commit „archiv:
  auftrag-lehrwerke-nach“.

## Prüfungen

1. foerderhefte-formen.md: jede Tabellenzeile trägt nur Kürzel
   aus der Liste, drei Zahlen und einen Kapiteltitel; keine
   Zeile enthält Aufgabentext.
2. Jede neue oder ergänzte Textdatei: je Band Kapitel erster
   Ebene mit Seitenzahl, Kopf mit ISBN, IDN, Adresse, Datum.
3. Fundlisten und Textdateien stimmen überein (jede Fundzeile
   „DNB“ hat einen Abschnitt, jeder Abschnitt eine Zeile).
4. git status vor jedem Commit: kein Pfad unter hefte/.
5. Standdatei: alle Punkte tragen einen Stand.

## Bericht

Als quellen/lehrwerke-nach-bericht-2026-09.md (im Register-
Commit) und im Chat. Erste Zeile: das Modell. Teil 1: je Quelle
Betrachter gefunden ja/nein, Seiten angesehen, wie die Bilder
geladen wurden (eine Zeile). Teil 2: Treffer, gesichert ja/nein.
Teil 3: Bände gesichert, „nicht gefunden“ mit Grund. Ergebnis
der Prüfungen 1–5. Eigene Entscheidungen, je ein Satz mit Grund.
Letzte Zeile: „Push origin drücken“.
