# Auftrag Nacht 2026-09-28: Befund ablegen, Abitur-Reste
# schließen, Sek-II-Einträge nachziehen, Prüfskript, Übersichts-
# Prüfstein

Modell: Opus. Läuft ohne den Lehrer: keine Rückfrage, Standdatei,
Commit je Teil, Fehlerregel je Teil. Ordner: mathe-nachhilfe.
Die Vorlage Stufe 6 in ../blattbau ist fertig (Commit cad91ae);
du liest dort, schreibst dort nichts.

## Ausgangslage

Die Nacht vom 27.09. (nacht-bericht-2026-09-27.md) hat vier Posten
offen gelassen (faellig.md § 2, Einträge vom 27.09.); der
Vorlagen-Auftrag in blattbau hat einen Zuruf an blatt-pruef.py;
der Lehrer hat am 26.09. zwei Testlauf-Blätter gelesen, und seine
Befunde liegen in Datei 2 dieses Auftrags. Dieser Auftrag legt
den Befund ab (Teil 1), schließt die Abitur-Reste nach den Regeln
des Profils (Teil 2–3), zieht die Sek-II-Einträge nach (Teil 4),
stellt das Prüfskript um (Teil 5), bereitet die Eichungsfrage für
den Chat vor (Teil 6) und baut einen Prüfstein für das
Übersichtsblatt (Teil 7). Du änderst
keinen Prompt und nichts
unter blaetter/testlauf-*/.

## Regeln

- Shell PowerShell: kein Heredoc, kein sed. Dateien schreiben mit
  [System.IO.File]::WriteAllText(pfad, text,
  (New-Object System.Text.UTF8Encoding($false))); Zeilenenden LF;
  nach dem Schreiben prüfen (keine BOM, kein CR).
- Python nur %LocalAppData%\Programs\Python\Python312\python.exe;
  git über die git.exe von GitHub Desktop, mit -c core.pager=cat;
  Commit-Nachrichten mit Umlaut über commit -F aus einer
  UTF-8-Datei, nie -m; kein Push.
- xelatex, pdftotext, pdfinfo, pdftoppm unter
  %LocalAppData%\Programs\MiKTeX\miktex\bin\x64.
- Nichts löschen; verschieben nur mit git mv. Keine Handedits an
  CSV, die ein Bauskript schreibt.
- Grenzen sind Zählgrenzen, nie Zeit. Fehlerregel überall: ein
  Schritt, der zweimal scheitert, wird als „offen" mit Grund in
  Standdatei und Bericht eingetragen; der nächste Punkt folgt.
- Standdatei nacht-stand-2026-09-28.md in der Wurzel: je Teil eine
  Zeile „offen / läuft / erledigt" mit dem letzten fertigen Punkt
  und dem Commit; Uhrzeiten nur aus Get-Date; ein Neustart liest
  sie zuerst.
- Gegenproben: Der bekannte Wert steht mit seiner Belegdatei
  dabei. Weicht die Gegenprobe ab, schreib die Abweichung mit
  Erklärung in den Bericht und ändere das Skript nicht.
- README.md ist die Landkarte: jede neue Datei bekommt dort einen
  Satz, im selben Commit. faellig.md: erledigte Posten im selben
  Commit in § 2 streichen und mit Datum in § 4 eintragen; neue
  Posten eintragen statt sie im Bericht zu lassen.
- Skripte gehören mit allen Daten ins Repo. Hilfsagenten, die
  dieselben Dateien anfassen, laufen nacheinander.

## Teil 1: Befund ablegen

Datei 2 dieses Auftrags ist befund-testlauf-2026-09-25.md; sie
liegt schon in der Wurzel. README-Zeile (Block Wurzel, neben
bericht-testlauf-2026-09-25.md); in faellig.md § 2 je Zeile des
Abschnitts „Katalog" und „Werkzeug" der Befunddatei einen Posten,
Fundstelle die Befunddatei; die Abschnitte „Prompt", „Vorlage"
und „Beschluss" bekommen keine Posten (sie gehen in v4.4 und
Stufe 6). Commit „befund: Testlauf 2026-09-25, Lesebefunde".

## Teil 2: Delta-Stapel CAS und Vormerkungen

faellig.md § 2 Posten „Pool-Vormerkungen des CAS-Nachtrags
schließen"; abi.md § 7, iqb.md § 7 (MMS/CAS als Delta zum
WTR-Zweig: wortgleiche Dateien sind Dateidubletten, nur die nicht
wortgleichen bilden den Delta-Stapel; Muster 2026-ea-B-mms in
iqb-pruefungen.md § 2), CLAUDE.md § 4.

1. Stapel 2017-ea-B (WTR) erfassen: Reserve geöffnet wegen
   Landesheftverweisen (2017-bb-ea-cas B3.1), Abbruchkriterium
   unberührt – wie 2017-ga-B in der Nacht vom 27.09. Commit.
2. Delta-Stapel 2017-ea-B-cas: iqb-quellen.csv sagt je CAS-Datei,
   ob sie Dateidublette der WTR-Datei ist; fehlt die Spalte für
   2017, misst du die Wortgleichheit wie iqb-quellen.py es für
   2026 tut, und trägst sie ein (Skriptlauf, kein Handedit). Nur
   die nicht wortgleichen Dateien werden erfasst. Commit.
3. Delta-Stapel 2018-ea-B-cas ebenso (WTR-Stapel 2018-ea-B ist
   erfasst). Commit.
4. Vormerkungen umstellen: 2017-bb-ea-cas B3.1 c, e, f und
   2018-bb-ea-cas B3.1 f auf „Dublette von:" bzw. „Abgewandelt
   von:" mit der jetzt erfassten Pool-id; ist die CAS-Datei
   Dateidublette der WTR-Datei, zeigt der Verweis auf die
   WTR-Zeile. Dazu die fehlenden Poolvermerke der WTR-Zeilen
   2017-bb-ea-B3.1 a–f (Posten nennt sie). Abgleichlauf
   abitur-abgleich.py, Selbstprüfung beider Bauskripte. Commit.

Scheitert Punkt 1 nach zwei Anläufen, entfallen 2 und 4 für
2017; Punkt 3 und der 2018-Teil von 4 laufen trotzdem.

Gegenprobe Teil 2 (iqb-pruefungen.md § 2, abi-pruefungen.md § 2):
2017-ea-B (WTR) 14 Dateien; nach Punkt 4 steht in keinem
abi-Katalogeintrag mehr „Poolaufgabe (nicht erfasst)" (grep über
abitur/abi-katalog.csv: 0 Treffer).

## Teil 3: Berliner CAS-Hefte – Abgrenzung messen, nicht erfassen

abi.md § 9 lässt offen, welche Teilaufgaben der Berliner CAS-Hefte
2017/2018 eine eigene Zeile bekommen (kein „CAS:"-Präfix). Miss
für 2017-be-gk-cas, 2017-be-lk-cas, 2018-be-gk-cas, 2018-be-lk-cas
(hefte/abi/, Dateinamen nach abi-quellen.md § 8) je Teilaufgabe die
Wortgleichheit mit der WTR-Fassung (Text über pdftotext -layout,
Vergleich je Teilaufgabe wie beim Pool-Abgleich) und schreib
abitur/befund-cas-berlin-2026-09-28.md: je Heft eine Tabelle
Teilaufgabe · wortgleich / abweichend · Art der Abweichung
(Zahl, Werkzeug, ganze Aufgabe). Kein Katalogeintrag; das Urteil
fällt im Chat. Fehlt eine Datei: offen mit Grund.

Gegenprobe Teil 3 (abi-pruefungen.md § 2): Seiten je Heft 8, 9,
10, 9; die Zahl der abweichenden Teilaufgaben je Heft in den
Bericht.

Commit „abitur: Befund Berliner CAS-Hefte 2017/2018".

## Teil 4: Sek-II-Einträge mit den Katalogzeilen vom 27.09. nachziehen

faellig.md § 2 Posten „katalog: Sek-II-Einträge … nachziehen"
(120 Zeilen: CAS-Nachträge 28, Stapel 2017 59, Heft 33; dazu die
Zeilen aus Teil 2). Vorgehen wie der Serienbau (archiv, Aufträge
„Serienbau Bündel"): je Zeile über themen.csv (profil abi/iqb,
Spalte thema) zum Eintrag, dort zur Lerneinheit nach dem Typ;
Typen, die der Eintrag noch nicht führt, in die Typenzeile der
passenden Einheit, Originale in „Prüfungsform" mit id. Neue
Einheit nur, wenn kein vorhandener Titel den Typ trägt – dann
Vorschlag in katalog/_vorschlaege-2026-09-28.md, nicht im
Eintrag. Danach katalog/_pruef_katalog.py: „Zeilensumme ≠
themen.csv" muss bei 0 Einträgen stehen, Kennzahl 5 wieder auf
dem Wert vor dem 27.09. (48) oder darunter.

Gegenprobe Teil 4 (nacht-bericht-2026-09-27.md Teil 10): Kennzahl
5 vor diesem Teil 168; 31 Einträge mit Zeilensumme-Abweichung.

Commit „katalog: Sek-II-Einträge auf die Katalogzeilen vom 27.09.".

## Teil 5: Prüfskript und Marken-Gegenprobe

1. werkzeuge/blatt-pruef.py: \swz und \swa in TEILZAEHLER
   aufnehmen (bericht-vorlage-stufe5-2026-09-27.md in blattbau,
   offener Punkt); Kennzahl 2 für Eingabe 3 des Testlaufs muss
   danach alle Teilaufgaben zählen, nicht 34. Dazu die Bausteine
   der Stufe 6 aus ../blattbau/Anleitung_mathblatt.md (\verfahren,
   \anweisung, \rechenplatz, Umgebung beispiel, \streifenleer[0]):
   je Baustein eine Kennzahl (Zahl je Blatt).
2. werkzeuge/marken-bau.py: die fest eingebaute GEGENPROBE trägt
   Sollwerte vom 26.09., die als falsch belegt sind
   (nacht-bericht-2026-09-27.md Teil 1). Sollwerte auf die
   Belegwerte stellen: lineare-funktionen 4 „P10" (3 von 13),
   quadratische-gleichungen 2 „GYM Kl. 8–9"; Quelle je Wert im
   Skriptkopf nennen. Das ist die Entscheidung des Chats vom
   26.09. („beide Belegwerte gelten").
3. blaetter/kennzahlen.md und blaetter/testlauf-2026-09-25/
   kennzahlen.md nicht neu bauen (die Testlauf-Datei ist
   eingefroren); für den Nachweis ein Lauf in den Scratchpad und
   die Zahl für Eingabe 3 in den Bericht.

Gegenprobe Teil 5 (bericht-testlauf-2026-09-25.md): Eingabe 3
Teilaufgaben bisher 34; Quelltext zählen (\teil, \swz, \swa,
\swfrage, \gl) und beide Zahlen in den Bericht.

Commit „werkzeuge: blatt-pruef.py Schwach-Zähler, marken-bau
Gegenprobe".

## Teil 6: Eichungsfrage 2017-ga-B für den Chat

faellig.md § 2 Posten „Eichung Pool 2017 grundlegend prüfen".
Schreib abitur/befund-eichung-2017-2026-09-28.md: die sechzehn
abweichenden Zeilen von 2017-ga-B (WTR) mit id, erster Schätzung,
amtlichem Bereich, Grund der Korrektur (aus bemerkung) und der
Regel der engen Fassung, die griff; dazu dieselbe Tabelle für
2017-ga-A (drei Abweichungen, zwei korrigiert). Darunter die
Eichung je Pooljahr über den Bestand (aus der Selbstprüfung von
iqb-bau.py), als Tabelle Jahr · Niveau · Eichung erster Lauf, wo
die Änderungslogs ihn nennen · Eichung heute. Kein Urteil.

Gegenprobe Teil 6 (iqb-pruefungen.md § 2): 2017-ga-B 34 von 39,
erster Lauf 23 von 39; 2017-ga-A 17 von 20, erster Lauf 15.

Commit „abitur: Befund Eichung Pool 2017".

## Teil 7: Prüfstein Übersichtsblatt quadratische Funktionen

Beschluss des Lehrers vom 26.09. (befund-testlauf-2026-09-25.md,
Abschnitt Beschluss): je Thema eine Übersicht für den Lehrer, aus
den Merkkästen des Eintrags, einmal gebaut. Dieser Teil baut den
Prüfstein, an dem der Chat die Form entscheidet.

1. Quelle: katalog/quadratische-funktionen.md, Abschnitt
   „Merkkasten" (alle Einheiten), dazu aus quadratische-
   gleichungen.md der Kasten zum Lösen (Wurzelziehen, Satz vom
   Nullprodukt, p-q-Formel, Lösbarkeit). Nichts erfinden: jede
   Zeile der Übersicht ist eine Regelzeile eines Kastens,
   wortgleich oder gekürzt.
2. Form: eine Seite A4, Vorlage ../blattbau/mathblatt.sty
   (Stand zur Laufzeit), Blattkopf „Quadratische Funktionen ·
   Übersicht"; Blöcke je Kasten in der Reihenfolge der
   Einheiten; ein Koordinatensystem mit Normalparabel und einer
   verschobenen Parabel (Bausteine der Vorlage: ksys, funktion),
   daneben die Formen (Normalparabel, Scheitelpunktform,
   Normalform, allgemeine Form) und die Verfahren zur Nullstelle
   nebeneinander in einer Tabelle „Form · Verfahren · wann".
   Keine Aufgaben, kein Kästchen, keine Zweigzeile.
3. Ablage: blaetter/uebersicht/quadratische-funktionen/
   2026-09-28/ mit src/uebersicht.tex, pdf/uebersicht.pdf,
   protokoll.txt (Quelle je Block: Eintrag, Einheit, Kasten).
   blaetter/index.md nicht anfassen (einsortieren.py kennt die
   Sorte nicht; Posten in faellig.md: „einsortieren.py um Sorte
   uebersicht erweitern").
4. Zweiter Prüfstein, nur wenn der erste in höchstens drei
   Kompilierläufen steht: prozentrechnung (Verfahrensthema) nach
   derselben Regel, damit der Chat beide Sorten nebeneinander
   sieht.

Gegenprobe Teil 7 (katalog/quadratische-funktionen.md): die Zahl
der Kästen im Eintrag und die Zahl der Blöcke auf der Seite
müssen gleich sein; pdfinfo: 1 Seite.

Commit „blaetter: Prüfstein Übersichtsblatt quadratische
Funktionen (und Prozentrechnung)".

## Abschluss

- faellig.md nachführen (Teil 1 Posten anlegen; Teil 2, 4, 5
  Posten erledigt; Teil 3 und 6 „Befund liegt vor, Urteil im
  Chat" als Zusatz am Posten; Teil 7 neuer Posten
  einsortieren.py).
- nacht-stand-2026-09-28.md und diesen Auftrag nach archiv/
  verschieben (git mv; bei Namensgleichheit „b" anhängen).
- Bericht nacht-bericht-2026-09-28.md in der Wurzel, README-
  Zeile. Commit „archiv: auftrag-nacht-2026-09-28, Bericht".

## Bericht

nacht-bericht-2026-09-28.md und im Chat. Erste Zeile das Modell.
Je Teil: was geändert ist (Dateien, Zahlen), die Gegenprobe im
Wortlaut mit Belegdatei, eigene Entscheidungen, offene Punkte mit
Grund. Teil 2: je Stapel Zeilen, neue Typen, Poolquote, „?"-
Zeilen, Zahl der Dateidubletten. Teil 3: je Heft die Zahl
abweichender Teilaufgaben. Teil 4: Kennzahl 5 vorher/nachher,
Zahl der neuen Typen je Eintrag, Vorschläge neue Einheiten.
Teil 7: Seitenbild als PNG (pdftoppm, 100 dpi) neben das PDF.
Letzte Zeile: „Push origin drücken".
