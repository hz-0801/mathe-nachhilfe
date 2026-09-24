# Auftrag: Förderformen aus freien Quellen sichern

Stand 2026-09-24. Ordner mathe-nachhilfe. Modell Sonnet.
Läuft unbeaufsichtigt; nichts wartet auf den Lehrer.

## Ausgangslage

Die Formenliste quellen/foerderhefte-formen.md hat fünf Zeilen
aus zwei Schulbuchreihen (Klick!, Kohl). Für Klasse 7–10 und
Sek II gibt es keine Seite, weil Schulbuchverlage keine
Vorschauen zeigen. Dieser Auftrag sucht dort, wo ganze Seiten
frei liegen: Förderkonzepte der Fachdidaktik, Lernhilfe-Verlage
mit Leseproben als PDF, Grundwissen-Blätter, Brückenkurse. Das
Bundesland ist unwichtig; die Form zählt.

Zweck: Vorbild für die Option „schwach“ des Unterrichtsblatts
(Takt Beispiel → Lücke → frei, Dichte, Text vor der ersten
Aufgabe) und für Themen unter Klasse 8 (Boden). Befund und
Revision stehen in befund-foerderhefte-2026-09-24.md (Datei 2,
Teil 0); nichts daraus ist entschieden.

## Regeln

- Python nur über %LocalAppData%\Programs\Python\Python312\
  python.exe; git über die git.exe von GitHub Desktop; PowerShell
  (kein Heredoc, kein sed). git mit -c core.pager=cat, commit -m,
  nicht pushen. CQL an dnb-sru.py mit --% und verdoppelten
  Anführungszeichen.
- Nichts löschen. Kein Login, keine Registrierung, kein
  Warenkorb, kein Formular. Lesen und frei angebotene Dateien
  laden ist erlaubt, auch bei Händlern (Amazon „Blick ins Buch“,
  Google Books), Einkauf nicht.
- Keine Rückfragen; eigene Entscheidungen in den Bericht.
- Zählgrenzen: je Quelle höchstens 15 Seitenaufrufe und 8
  gesicherte Dateien; je Datei höchstens 12 Seiten angesehen.
  Grenze erreicht → Stand eintragen, nächste Quelle.
- Standdatei quellen/foerderformen-stand-2026-09-24.md
  (Datei 3): nach jeder Quelle fortschreiben; Neustart macht beim
  ersten offenen Punkt weiter.
- Ein Commit je Teil (0 bis 7), einer für Register und Bericht.
  git status vor jedem Commit; hefte/ nie im Commit.
- Fehlerfall: nach zwei Anläufen „nicht gefunden“ mit Grund,
  weiter.
- Urheberrecht: PDFs und Seitenbilder nur lokal unter
  hefte/foerderformen/<quelle>/ (.gitignore). Freie Lizenzen
  (CC BY, CC BY-SA, CC BY-NC-SA, OER) dürfen als Text unter
  quellen/ committet werden – dann mit Lizenzzeile im Kopf. Aus
  allem anderen kommt ins Repo nur: Titel, Adresse, Klasse,
  Thema, die Formenzeile. Kein Aufgabentext, kein Bild.

## Teil 0 – Befunddatei

befund-foerderhefte-2026-09-24.md liegt in der Wurzel (Datei 2).
README.md, Abschnitt „Wo fange ich an“: ein Satz nach dem Muster
der anderen Befunddateien. Commit „befund: Förderhefte
2026-09-24“.

## Teil 1 – Mathe sicher können (DZLM)

mathe-sicher-koennen.dzlm.de (und die Seiten der Uni Dortmund /
DZLM dazu): Diagnose- und Förderbausteine, Handreichungen,
Schülermaterial, soweit frei als PDF. Alle Bausteine laden
(Natürliche Zahlen, Brüche/Dezimalzahlen/Prozente, Sachrechnen,
weitere). Lizenz im Kopf jeder Datei nachsehen. Je Baustein:
Fundzeile und Formenzeile (unten). Ist die Lizenz frei, die
Gliederung (Bausteine, Titel, Seiten) als Text nach quellen/
quelle-dzlm-mathe-sicher-koennen-inhalt.txt. Commit „quellen:
Mathe sicher können (DZLM)“.

## Teil 2 – Stark Verlag

stark-verlag.de: Training Mathematik Hauptschule/Mittelschule
und Realschule je Klasse 5–10, Abitur-Training Analysis/
Geometrie/Stochastik, Grundwissen-Titel. Leseproben als PDF
laden, wo angeboten. Je Titel Fund- und Formenzeile. Commit
„quellen: Stark Leseproben“.

## Teil 3 – Persen und Auer

persen.de, auer-verlag.de: Mathematik Förderschule, Inklusion,
„Mathe an Stationen“, Rechnen im Zahlenraum bis …, Klasse 5–10.
Leseproben als PDF laden. Höchstens 8 Titel je Verlag, bevorzugt
Klasse 7–10 und Grundvorstellungen. Commit „quellen: Persen und
Auer Leseproben“.

## Teil 4 – Grundwissen-Blätter Bayern

Suche: „Grundwissen Mathematik Jahrgangsstufe 7 Gymnasium pdf“
(ebenso 5, 6, 8, 9, 10, 11, 12) sowie ISB Bayern Grundwissen
Mathematik. Je Jahrgangsstufe ein bis zwei Schulen, deren
Blätter vollständig als PDF vorliegen; dazu die ISB-Fassung,
wenn es sie gibt. Fundzeile; Formenzeile nur, wenn Aufgaben
enthalten sind. Commit „quellen: Grundwissen Bayern“.

## Teil 5 – Brückenkurse Sek II

OMB+ (Online Mathematik Brückenkurs), Vorkurs-Skripte deutscher
Hochschulen (Suche „Vorkurs Mathematik Skript pdf“), Mindest-
anforderungskatalog cosh liegt schon in quellen/. Höchstens 5
Skripte; Fund- und Formenzeile. Commit „quellen: Brückenkurse“.

## Teil 6 – Händlervorschauen

Für die Reihen ohne Verlagsvorschau: Sekundo Förderheft,
Schnittpunkt Förderheft, Mathematik 2023 Förderheft, Duden
Basiswissen Schule Mathematik, Klett Lerntraining Mathematik.
Amazon „Blick ins Buch“ oder Google Books öffnen; sind Seiten
sichtbar, wie bei einem Betrachter ansehen (höchstens 12) und
Formenzeile; Seitenbilder nur lokal. Commit „quellen:
Händlervorschauen Förderhefte“.

## Teil 7 – Rechenschwäche Sek I

Suche: „Rechenschwäche Sekundarstufe Fördermaterial pdf“,
„Dyskalkulie Klasse 7 Material“, Landesbildungsserver
(Diagnose Stellenwert, Zahlenstrahl, Grundvorstellungen).
Höchstens 6 Dokumente, frei als PDF. Fund- und Formenzeile.
Commit „quellen: Rechenschwäche Sek I“.

## Fund- und Formenzeile

quellen/foerderformen-fundliste.md, je Teil eine Tabelle:
Quelle, Titel, Klasse/Stufe, Adresse, Datei lokal (ja/nein),
Lizenz, Seiten angesehen, Thema (Titel des Abschnitts), Formen
als Kürzel aus dieser festen Liste und nur aus ihr:
  B  vorgerechnetes Beispiel
  L  dieselbe Aufgabe mit Lücken zum Ausfüllen
  F  freie Aufgabe ohne Vorgabe
  M  Merkkasten oder Regelkasten
  R  Rechenraster (ein Schritt je Zeile, Kästchen für Zahlen)
  Z  Zahlenstrahl, Bild oder Tabelle als Hilfe
  S  Selbsttest oder Kontrollkästchen
  Lö Lösungen im Heft
  W  Wortschatz- oder Lesehilfe
  D  Diagnoseaufgabe vor der Förderung
dazu drei Zahlen: Aufgaben je Seite, Zeilen Text vor der ersten
Aufgabe, Teilaufgaben je Beispiel (Mittel, gerundet). Am Ende
je Teil: Dateien gesichert, Grenze erreicht ja/nein,
Suchbegriffe ohne Treffer.

## Register

quellen/quellen.md (neue Textdateien), README.md Abschnitt
quellen/ (Fundliste, Standdatei, Bericht, Textdateien je ein
Satz). Commit „quellen: Register Förderformen“. Auftrag nach
archiv/ verschieben, Commit „archiv: auftrag-foerderformen“.

## Prüfungen

1. Fundliste: jede Zeile hat Adresse und Lizenzangabe; Formen
   nur aus der Liste; kein Aufgabentext.
2. Jede Textdatei unter quellen/ trägt eine Lizenzzeile, die
   das Committen erlaubt.
3. git status vor jedem Commit: kein Pfad unter hefte/.
4. Standdatei: alle Punkte tragen einen Stand.

## Bericht

Als quellen/foerderformen-bericht-2026-09.md und im Chat. Erste
Zeile: das Modell. Je Teil: Dateien gesichert, Formenzeilen,
„nicht gefunden“ mit Grund, Grenze erreicht. Ergebnis der
Prüfungen 1–4. Eigene Entscheidungen, je ein Satz mit Grund.
Letzte Zeile: „Push origin drücken“.
