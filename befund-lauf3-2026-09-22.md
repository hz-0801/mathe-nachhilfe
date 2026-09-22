# Befund Lauf 3 – Lernblatt Daten, Prompt v4.1

Stand 22.09.2026. Auswertung im Werkstattchat verbessereBlätter()
gegen ziel.md. Lauf im Projekt erzeugeUnterrichtsblatt(), Modell
Opus, Eingabe „daten", keine Rückfrage. Ergebnis abgelegt unter
blaetter/daten/2026-09-22/.

## 1 Ergebnis

Lernblatt mit 21 Seiten, 40 Hauptnummern, 208 Teilaufgaben,
18 Grafiken; fünf Einheiten (1–5 des Eintrags), je Einheit ein
Original mit Jahr; Blatt 0 aus sechs Fertigkeiten plus einer
Fehler-finden-Aufgabe; Verzeichnis mit Seitenbereichen; Lösungen
als eigene Datei (3 Seiten, Ergebnis mit Zwischenergebnissen).
Stichproben der Lösungen (Nr. 10, 19, 32 j, 37 b) richtig; keine
Vollprüfung aller Teilaufgaben.

Gegen ziel.md § 1–3 trägt das Blatt: Leiter je Typ, Vorstufen an
der ersten Einheit ihres Bereichs, Verfremdung mit Jahr, keine
Typnamen des Katalogs, kein Kasten, keine Sterne.

Zeiten (zeiten.txt, Sekunden seit t0): Blatt 0 284, Einheit 1
475, Einheit 2 653, Einheit 3 757, Einheit 4 977, Einheit 5 1079,
Gesamt und Lösungen 1127. Erste Bauzeitmessung überhaupt.
24 Werkzeugschritte, davon 7 Korrekturen und 3 für eigene.sty.
Werkzeuggrenze der Oberfläche nach 20 Aufrufen erreicht
(Zwischenmeldung in Einheit 4), Fortsetzung auf „Weiter".

## 2 Befunde nach Gewicht

### 2.1 Bereitstellung gebrochen

Blatt 0 stand nach 4:44 min, das Gesamt nach 18:47 min. Alle
Dateien erschienen erst am Ende. Ursache (Annahme, hohe
Sicherheit): Dateikarten einer Antwort werden in claude.ai erst
gezeigt, wenn die Antwort endet; eine laufende Antwort kann keine
Datei früh zeigen. Regel 2.7 des Prompts („Blatt 0 als PDF, sobald
es steht, der Bau läuft weiter") ist in dieser Oberfläche nicht
erfüllbar.

Beschluss 22.09.2026 (Revision des Beschlusses „Bau in Reihe,
Blatt 0 und Einheit 1 früh als PDF"): Blatt 0 beendet die erste
Antwort – Karte plus Zeile „Weiter baut Einheit 1 bis 5, Gesamt
und Lösungen". Nach „Weiter" läuft der Rest ohne Rückfrage und
liefert drei Dateien plus Archiv: Lernblatt ohne Blatt 0, Gesamt
mit Blatt 0, Lösungen. Einheit 1 als eigenes frühes PDF entfällt.
Grund: Der Klick nach Blatt 0 fällt mit dem Drucken zusammen; der
Lehrer ist dann ohnehin am Rechner.

### 2.2 Werkzeuggrenze

Ein zweiter Klick zu unvorhersehbarer Zeit (Werkzeuggrenze mitten
im Bau) ist das eigentliche Problem: Der Lehrer sitzt beim Schüler
und verpasst ihn; alles kommt dann viel später. Ziel: Der Rest nach
Blatt 0 passt in einen Durchgang. Rechnung: 24 Schritte heute,
minus Vorbereitung und Blatt 0, minus 5 Schritte für eigene.sty
und ihre Korrekturen, ergibt etwa 17 – unter der Grenze, wenn 2.7
schlank baut. Schlank heißt: Aufrufe derselben Einheit bündeln
(kompilieren, rechnen, rendern in einem Aufruf statt in dreien),
ein Prüfskript für alle Einheiten statt je Einheit eines. Nicht
gebündelt wird die Prüfung über Einheiten hinweg: Jede Einheit
wird direkt nach dem Schreiben geprüft, sonst zeigt sich ein
Fehler in Einheit 1 erst nach Einheit 5. Keine Prüfung entfällt.

Das spart Aufrufe, kaum Zeit: Die Bauzeit ist überwiegend
Schreibzeit des Modells (100–220 s je Einheit), nicht Kompilat.
Auffanglösung bleibt: An der Grenze sagt Claude, was fertig ist,
liefert nichts Halbes, und läuft nach „Weiter" ohne weitere
Frage zu Ende.

Beschluss 22.09.2026: Vorlage Stufe 4 vor der Prompt-Kürzung;
2.7 wird beim Umbau nach Stufe 4 schlank gemacht, mit denselben
Prüfungen. Bedingung des Lehrers: Druckqualität und Inhalt
unverändert.

### 2.3 Stufenschnitt bei Einträgen „Sek I + II"

Vorhersage vor dem Lauf: v4.1 baut alle sechs Einheiten und
liefert einem Siebtklässler Standardabweichung mit. Widerlegt:
Der Prompt ließ Einheit 6, die Sek-II-Zeilen der Einheiten 1 und
4 und die beiden Sek-II-Vorstufen weg und sagte es in der
Deutungszeile („Kl. 7 (Katalog) · Einheit 6 (Sek II) weggelassen
(Stoffstand Sek I)"). Richtig gehandelt, aber aus Auslegung von
1.5, nicht aus einer Regel.

Offen, Vorschlag: Ein Satz in 1.5 – Eintrag der Stufe „Sek I + II"
ohne Klassenangabe → Sek-I-Stoff, Deutungszeile nennt den Schnitt;
der Sek-II-Teil kommt nur mit „fos", „gymnasium" oder Klasse ab 11.

### 2.4 Vorlage: fehlende Bausteine und Layoutfehler

Der Prompt hat sich acht Bausteine in eigene.sty gebaut, weil
mathblatt.sty (2026-09-07d) sie nicht hat:
- \saeulenab – Säulendiagramm ohne Wertebeschriftung, feine
  Hilfslinien, Optionen ohnezahlen und ymin (Achse ab ymin für
  die abgeschnittene Achse)
- \balkenab – Balkendiagramm waagerecht
- \liniendia – Liniendiagramm
- \streifenleer, \streifenvoll – Streifendiagramm, Rahmen 10 cm
- \kreisleer – leerer Kreis mit Mittelpunkt und Startradius
- \einheitenkopf – „Einheit n von m · Titel"
- \strichliste – Strichliste
Dazu aus Lauf 2 (blaetter/prozentrechnung/2026-09-22/eigene.sty):
Streifen, Dreisatz-Schema, Einheitenkopf. Beide eigene.sty sind
die Bauvorlage für Stufe 4.

Layoutfehler der Vorlage, am Blatt gesehen:
- teilezwei kippt bei ungerader Zahl von Teilaufgaben: die letzte
  steht allein, die folgenden rutschen mit anderem Einzug darunter
  (Blatt 0 Nr. 5 e–g und Nr. 6 e–f, Gesamt Nr. 24 e–i).
- Strahl für den Winkel: Pfeil zeigt nach links, Scheitel S liegt
  links; der Strahl muss von S nach rechts gehen (Blatt 0 Nr. 3 g).
- Halbe Seiten leer, weil Grafiken nicht umbrechen (Gesamt S. 4,
  S. 13).
- Strichliste ohne Fünferbündel (Querstrich durch vier Striche).
- Beschriftungen an der x-Achse laufen bei langen Wörtern
  ineinander (Korrektur im Lauf, Einheit 1).

### 2.5 Beispiel je Typ

Der Prompt setzt vor Verfahrenstypen eine Beispielzeile
(„Beispiel: 30 % → 3 cm"), selbst erfunden, nicht aus dem
Merkkasten. Offener Punkt aus ziel.md § 5 ist damit entscheidbar;
noch nicht entschieden. Beobachtung: Es hilft beim Einstieg und
ist kein Kasten.

### 2.6 Kleines

- Vorstufe Nr. 8 e fragt nach dem Anteil, obwohl die Anweisung
  „Rechne noch nicht" lautet.
- Nr. 23 g beschreibt einen Streifen, statt ihn zu zeigen.
- Die Protokollzählung meldet für die Lösungsdatei „0 Haupt-
  nummern", weil die Zählregel das Lösungsformat nicht kennt.
- Der Lauf begann mit der falschen Projektanweisung (Werkstatt
  statt v4.1), weil beim letzten Umzug die Werkstatt-Anweisung
  ins Projekt erzeugeUnterrichtsblatt() gewandert war; v4.1 wurde
  vor dem Lauf eingesetzt.

## 3 Beschlüsse dieses Laufs

- Blatt 0 beendet die erste Antwort; der Rest nach „Weiter"
  (2.1).
- Vorlage Stufe 4 vor der Prompt-Kürzung; 2.7 schlank mit
  Prüfung je Einheit (2.2).

## 4 Offen

- Regel 1.5 für Einträge „Sek I + II" (2.3).
- Beispiel je Typ (2.5).
- Kleines aus 2.6 beim nächsten Umbau des Prompts.
