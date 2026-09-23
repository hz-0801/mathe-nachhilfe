# Auftrag: Gymnasialhefte P10 2014–2025 erfassen (Profil msa,
papier GYM)

Stand 2026-09-23. Ordner mathe-nachhilfe. Modell Opus.

## Ausgangslage

Auf dem Bildungsserver liegen 19 Gymnasialhefte der P10 Mathematik
Brandenburg 2014–2025 (ab 2019 zwei Dateien je Jahrgang); sie sind
lokal unter hefte/msa/sonstiges/ gesichert (msa/msa-quellen.md
§ 5, Tabelle „sonstiges/") und nicht erfasst. konzept.md
Entscheidung 18 nimmt sie vom Bestand aus, nennt aber als
Kippbedingung „einen Gymnasialschüler mit zentraler
Klassenarbeit". Nach msa/msa-vorgaben.md (FB 10) schreibt das
Gymnasium seit 2025/26 statt der P10 eine zentrale Klassenarbeit
in Klasse 10 (90 min, 35 BE, 10 BE hilfsmittelfrei). Die
Bedingung ist erfüllt; der Lehrer hat am 23.09.2026 entschieden,
die Hefte zu erfassen.

Zweck: (1) Prüfungsart für Gymnasiasten der Klasse 10; (2) echte
Prüfungsaufgaben als Decke der Gymnasialketten im Themenkatalog;
(3) Vergleich Oberschule/Gymnasium je Typ, damit „in Teilen G"
aus dem Rahmenlehrplan messbar wird.

Form: kein neues Profil, sondern das Profil msa mit dem neuen
papier-Wert GYM. Grund: dieselbe Themenliste (msa.md § 6),
dieselbe Typenliste (msa-typen.csv) – nur mit einer gemeinsamen
Typenliste lässt sich je Typ zählen, ob er in OS-, FOR- oder
GYM-Heften vorkommt (wie abi und iqb, konzept.md). Die GYM-Zeilen
kommen in eine eigene Katalogdatei msa/msa-katalog-gym.csv (beide
Blöcke, Feld block trennt sie), damit werkzeuge/ertrag.py und
alles andere, was die FOR-Kataloge liest, unverändert bleibt.

Der Lehrer ist längere Zeit nicht am Rechner. Der Auftrag muss
ohne Eingreifen durchlaufen. Deshalb: keine Rückfrage, kein
Warten auf Bestätigung, jeder Fehlerfall hat unten eine Regel,
und der Stand steht nach jedem Heft in msa/gym-stand.md, damit
ein Neustart dort weitermacht.

## Regeln

- Python nur über den vollen Pfad
  %LocalAppData%\Programs\Python\Python312\python.exe; git über
  die git.exe von GitHub Desktop; Shell ist PowerShell (kein
  Heredoc, kein sed). Jeden git-Aufruf mit
  -c core.pager=cat und ohne Editor (commit -m). Nicht pushen.
- Nichts löschen. Dateien, die dieser Auftrag anlegt, stehen in
  README.md (Block msa/), im selben Commit.
- Erfassung nach CLAUDE.md § 2 und § 3, katalog-prompt.md § 3–8
  und msa/msa.md; bei Widerspruch gilt msa.md. Ein Heft je Lauf,
  ein Commit je Heft, kein Zwischenstand in den CSV-Dateien, keine
  Handedits an CSV.
- Text der Hefte mit pdftotext -layout; jede Aufgabenseite einmal
  rendern und ansehen. Fehlt pdftotext oder das Rendern: Text
  über Python (pypdf oder PyMuPDF), Rendern über PyMuPDF; ist
  auch das nicht möglich, Text allein und in bemerkung jeder
  betroffenen Zeile „Bild nicht gesehen". Vor dem ersten Heft die
  Textextraktion an 2025-os.pdf gegen eine bekannte Zeile prüfen
  (Aufgabe 1, Basisaufgaben, 10 Punkte muss im Text stehen);
  weicht sie ab, Werkzeug wechseln, nicht die Zeile.
- Gegenprobe je Heft: Summe punkte aller Zeilen = BE laut
  Deckblatt des Hefts; Seitenzahl = Tabelle in msa-quellen.md § 5.
  Eine Abweichung ist ein Befund im Bericht und in gym-stand.md,
  kein Grund, das Skript anzupassen.
- Ergebnisse mit sympy nachrechnen; „?" mit Grund in bemerkung.
- Stand fortschreiben: Nach jedem Heft die Zeile des Hefts in
  msa/gym-stand.md auf „erfasst <Datum>, n Zeilen" setzen, dazu
  Befunde des Hefts in einem Satz; Datei im Commit des Hefts.
  Nach einem Abbruch beginnt der nächste Lauf beim ersten Heft
  ohne „erfasst".
- Zeitbudget: Kommt ein Heft nach zwei Anläufen nicht durch das
  Skript, Zeile in gym-stand.md auf „offen: <Grund>" setzen, das
  Heft nicht committen und mit dem nächsten Heft weitermachen.
  Nichts wartet auf den Lehrer.

## Schritte

1. Stand lesen. msa/gym-stand.md öffnen. Trägt jedes Heft
   „erfasst", weiter bei Schritt 7. Sonst beim ersten Heft ohne
   „erfasst" weiter, Schritt 2 nur beim ersten Durchlauf (Stand
   „Skript: offen").

2. Skript und Profil erweitern (nur einmal, Stand „Skript:
   offen"). Vorher Referenz: msa-bau.py mit leerem ZEILEN laufen
   lassen, Ausgabe und die drei CSV-Dateien sichern (Zeilenzahl,
   Hash). Dann:
   a) msa-bau.py: papier-Muster um GYM erweitern; KONFIG bekommt
      „dateien" (Liste, weil ab 2019 zwei PDF je Heft) statt nur
      „datei", Altwert bleibt gültig; Zeilen mit papier GYM werden
      nach msa-katalog-gym.csv geschrieben (beide Blöcke in einer
      Datei, Feld block), OS/EBR/FOR/MUSTER wie bisher; die
      Selbstprüfung liest alle drei Katalogdateien; die
      Versionszeile im Kopf anpassen (0.3, Anlass dieser Auftrag).
   b) msa.md: § 1 Absatz Gymnasium (Bestand, Grund, seit 2025/26
      zentrale Klassenarbeit); § 3 Aufbau der Gymnasialhefte, wie
      im ersten gelesenen Heft je Format vorgefunden (2014–2018
      ein Heft; ab 2019 Teil 1 ohne Hilfsmittel und Teil 2 mit
      Hilfsmitteln – am Heft prüfen, nicht annehmen); § 4 papier
      GYM, id 2019-GYM-K3b, hilfsmittel nein im hilfsmittelfreien
      Teil, block Basis für den hilfsmittelfreien Teil bzw. für
      Aufgabe 1 „Basisaufgaben" (wie 2028), Kontext für den Rest;
      stern leer; Versionszeile.
   c) konzept.md Entscheidung 18 neu fassen: Bestand um GYM
      2014–2025 erweitert am 23.09.2026, Grund die zentrale
      Klassenarbeit; Zahl und Kippbedingung neu (kippt, wenn die
      Klassenarbeit veröffentlicht wird und ein anderes Format
      hat – dann eigene papier-Kennung prüfen).
   d) Gegenprobe: Selbstprüfung erneut, Ergebnis für OS/EBR/FOR
      byteidentisch mit der Referenz (393 Zeilen, 185 Typen,
      gleiche Hashes). Weicht etwas ab: Änderung zurücknehmen, in
      gym-stand.md „Skript: offen – <Abweichung>" eintragen,
      Auftrag beenden (Schritt 8). Stimmt es: „Skript: erledigt",
      Commit „msa: papier GYM, Katalogdatei gym, Entscheidung 18".

3. Zentrale Klassenarbeit 2026 suchen (einmal, im Lauf des ersten
   Hefts): Jahresseite und Verzeichnis aus msa-quellen.md § 1
   nach einer Datei des Gymnasiums 2026 absuchen (curl, Liste der
   Links). Gefunden: nach hefte/msa/sonstiges/ sichern, Zeile in
   gym-stand.md „2026 GYM: gesichert, Format <Seiten, BE,
   Hilfsmittel>", nicht erfassen (Format ist neu, Kürzel offen).
   Nicht gefunden: „2026 GYM: nicht veröffentlicht (Stand
   <Datum>)". Danach weiter.

4. Heft erfassen, das erste ohne „erfasst" in gym-stand.md,
   chronologisch. Dateien aus hefte/msa/sonstiges/ (Namen in der
   Tabelle msa-quellen.md § 5); fehlt eine Datei lokal, mit curl
   vom Verzeichnis (§ 1) holen; scheitert das, Heft „offen: Datei
   fehlt" und weiter. Ablauf CLAUDE.md § 2 Schritt 2–6 mit
   msa-bau.py. Typen: erst die vorhandene Liste, neue nur nach
   Kern § 6; Typen, die nur in GYM-Heften vorkommen, brauchen
   keine Marke, das zählt später der Vergleich. Zeilenthema nach
   msa.md § 6 (Thema der Aufgabenstellung). Stern leer, hilfsmittel
   nach Heftteil.

5. Nachführen im selben Commit: msa-pruefungen.md § 2 bekommt
   eine Tabelle „Hefte Gymnasium" (Jahr, Dateien, Papier, Seiten,
   Zeit, BE, Status) und die Zeile im Änderungslog; msa-quellen.md
   § 3 und § 5 (sonstiges/ wird Bestand, Status je Datei);
   gym-stand.md (Regeln). Commit „msa: Heft <Jahr> GYM erfasst,
   n Zeilen".

6. Nächstes Heft: zurück zu Schritt 4, bis alle 12 Jahrgänge
   „erfasst" oder „offen" tragen.

7. Abschluss (einmal, wenn kein Heft mehr ohne Status ist):
   a) Selbstprüfung über den Gesamtbestand; werkzeuge/
      themen-pruef.py laufen lassen (Rückgabe 0 verlangt; bei
      Fehler nichts reparieren, Befund notieren).
   b) werkzeuge/ertrag.py laufen lassen und prüfen, dass
      msa-ertrag.csv unverändert ist (Gegenprobe: das Skript liest
      die gym-Datei nicht; ändert sich etwas, ist das ein Befund).
   c) Vergleich schreiben, msa/gym-vergleich.md, abgeleitet, aus
      den drei Katalogen: je Typ der Typenliste die Zahl der
      Hauptzeilen und Jahrgänge in OS/EBR/FOR und in GYM, dazu
      drei Listen: nur GYM, nur OS/FOR, beide. Je Thema (msa.md
      § 6) dieselben Zahlen. Datei mit Kopf (Stand, Skript,
      Quelle), das erzeugende Skript werkzeuge/gym-vergleich.py.
   d) README.md: msa-katalog-gym.csv, gym-stand.md,
      gym-vergleich.md, gym-vergleich.py, je ein Satz; ziel.md § 5
      nicht anfassen; faellig.md: Posten „zentrale Klassenarbeit
      Gymnasium 2026 suchen" nach Schritt 3 eintragen oder
      streichen.
   e) Commit „msa: Abschluss GYM-Erfassung, Vergleich".

8. Auftrag nach archiv/ verschieben (git mv; trifft er dort auf
   eine gleichnamige Datei, den neuen Namen datieren), Commit
   „archiv: auftrag-gym-erfassung". gym-stand.md bleibt in msa/.

## Prüfungen

- Je Heft: Punktsumme = BE laut Deckblatt; alle Aufgaben und
  Teilaufgaben mit Zeile; Seitenzahl = msa-quellen.md § 5;
  Selbstprüfung „Alle Prüfungen bestanden".
- Referenz Schritt 2 d: 393 Zeilen, 185 Typen, Hashes gleich.
- Abschluss: themen-pruef.py Rückgabe 0; msa-ertrag.csv
  unverändert; jede neue Datei in README.md.

## Bericht

Am Ende, als msa/gym-bericht-2026-09.md (im Abschluss-Commit) und
im Chat: erste Zeile das Modell, mit dem der Auftrag lief. Dann
je Heft eine Zeile (Jahr, Zeilen Basis/Kontext, BE Soll/Ist, neue
Typen mit Definition, „?"-Zeilen, Befunde), Hefte „offen" mit
Grund, Abweichungen der Gegenproben, Ergebnis Schritt 3, die
drei Listen aus dem Vergleich in Zahlen (nur GYM / nur OS-FOR /
beide), Entscheidungen, die du selbst getroffen hast. Letzte
Zeile: „Push origin drücken".
