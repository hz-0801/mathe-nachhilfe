# Übergabe 2026-09-23 – Werkstatt verbessereBlaetter

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, die aus
ihm Blätter bauen. Maßgeblich ist ziel.md in der Wurzel; jede
Entscheidung dient dem Blatt, das ein Schüler im ersten Lauf
bearbeiten kann.

## 2 Arbeitsgrundlage

- ziel.md – das Ziel; gilt vor jeder anderen Datei.
- blattbau/unterrichtsblatt.md v4.2 – läuft seit 23.09. als
  Projektanweisung in erzeugeUnterrichtsblatt(); Repo und
  Betrieb stimmen überein (CHANGELOG-Eintrag v4.2). Noch kein
  Lauf mit v4.2.
- blattbau/mathblatt.sty 2026-09-22h (Stufe 4) und
  Anleitung_mathblatt.md, Kopf auf Stufe 4 berichtigt.
- blattbau/pruefungsblatt.md v0.15 – unverändert.
- katalog/_niveaustufen-belege.md – je Sek-I-Eintrag, Lern-
  einheit und Sprosse die Stufe A–H aus Rahmenlehrplan und
  LISUM, mit Zitat; Vorschlag, entscheidet nicht.
- katalog/_kursart-belege.md – je Sek-II-Eintrag und Einheit
  Grund- oder Leistungskurs aus Geltungstabellen und GOST;
  Vorschlag, entscheidet nicht.
- blaetter/ – drei Blätter (daten, nullstellen, prozentrechnung),
  Register blaetter/index.md. nullstellen/2026-09-22 ist Lauf 4.
- befund-lauf3-2026-09-22.md, befund-testlauf-2026-09-22.md –
  Befunde der Läufe 1–3.
- katalog/ (73 Einträge), README.md als Landkarte.

## 3 Arbeitsstand

Abgeschlossen:
- Prompt v4.2 (auf Opus gebaut, nicht auf Fable): Planfrage vor
  dem Bau (1.3), Stufenschnitt und Kursart (1.5), Halbseitenmaß
  je Hauptnummer mit Teilung an Kettenstellen (2.3 g),
  Bereitstellung in drei Antworten (2.7), Vorlage Stufe 4 ohne
  eigene.sty (4.5), Vorstufe ohne Ergebnis, gemeinte Grafik wird
  gezeichnet, Zählregel Lösungsdatei.
- Lauf 4 abgelegt, nicht ausgewertet: Eingabe „nullstellen
  10.klasse, test vorbereitung", v4.1, zwei Einträge
  (quadratische-gleichungen, quadratische-funktionen Einheit 4),
  5 Einheiten, Gesamt 22 Seiten plus Lösungen 3, über alle PDFs
  mehr als 30 Seiten, über 20 Minuten. Gebraucht hätten pq-Formel
  und Diskriminante. Anlass der Planfrage.
- Belegdateien Niveaustufe und Kursart (Commit 3a420af). Kern:
  Sek I trägt – 115 von 116 Lerneinheiten und 1126 von 1352
  Sprossen haben eine Stelle im Rahmenlehrplan. Die Zeile
  „Spanne" der Sek-I-Datei folgt einer falschen Regel aus dem
  Auftrag (G/H und F zugleich); richtig ist Stoff auf H (siehe
  § 4). Sek II: 37 von 44 Einträgen haben Stoff beider
  Kursarten, 5 nur LK, 2 kein Planinhalt.
- Nebenbefunde der Belege: trigonometrie liegt auf G (Eintrag
  und index.md sagen F); lineare-funktionen Einheit 4 auf G
  (sagen F); wahrscheinlichkeit: Baumdiagramm und Pfadregel auf
  G (index.md D–E). Dazu 171 Ermessensfälle, je einer an seinem
  Ort in den Dateien.

Läuft nicht: nichts.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Neu am 23.09.:
- Rückfragen im Blattbau nur, wo der Katalogeintrag eine Spanne
  trägt, die die Eingabe nicht auflöst. v4.2: Umfang (nacktes
  Thema, vier oder mehr Einheiten), Stufe (Eintrag „Sek I + II"
  ohne Klasse), Bildungsgang (ab Kl. 11 ohne Schulwort). Alles in
  einer Antwort mit dem Plan, sonst keine Frage.
- Schulform bis Klasse 10: Der Unterschied ist real (Oberschule
  bis F, in Teilen G; Gymnasium Kl. 10 auf H). Gefragt wird in
  v4.3, und nur, wenn der Eintrag Stoff auf H trägt – nicht nach
  der Regel „G/H und F zugleich" aus dem Belegauftrag.
- Sek II: berufliches Gymnasium am OSZ = Zentralabitur, kein
  Vorgabenunterschied; FOS = eigener Plan (schon 1.5). Ohne
  Zuruf Grundkurs, LK-Stoff nur auf „lk".
- Hauptnummern höchstens etwa eine halbe Seite; geteilt wird an
  Kettenstellen, nie an jeder Sprosse; keine feste eigene Nummer
  für die letzten Teilaufgaben.
- Beispiel je Hauptnummer bleibt: eigene Zahlen, nie aus dem
  Merkkasten.
- Umgang mit dem Lehrer: Jede Antwort beginnt mit einem Satz,
  wo wir stehen und warum wir den nächsten Schritt tun; dann ein
  Punkt, eine Frage. Einfache Worte, Fachwort nur, wenn es im
  Repo so heißt, dann mit Erklärung. Kein Bericht über den
  eigenen Weg. Nur den nächsten Handgriff nennen, keine Vorschau
  auf die übernächsten. Auch Prompt-Regeln werden hinterfragt,
  nicht zitiert.

Beschlüsse vom 22.09. gelten weiter (archiv/uebergabe-
2026-09-22d.md § 4, befund-lauf3-2026-09-22.md § 2–3).

Rahmen:
- Oberfläche: Dateikarten erscheinen am Ende einer Antwort; je
  Antwort etwa 20 Werkzeugaufrufe.
- Claude-Code-Shell ist PowerShell: kein Heredoc, kein sed. Git
  über die git.exe von GitHub Desktop, Python über den vollen
  Pfad %LocalAppData%\Programs\Python\Python312\python.exe,
  MiKTeX unter %LocalAppData%\Programs\MiKTeX\miktex\bin\x64.
- Die Sitzung startet nicht immer auf dem gewünschten Modell
  (v4.2-Auftrag lief auf Opus statt Sonnet, der Belegauftrag auf
  Opus 5); vor jedem Auftrag den Modellwähler prüfen.
- Das Modell dieses Chats nachsehen, nicht nennen: Der Umbau
  v4.2 lief auf Opus 5.5, obwohl Fable geplant war.
- Modellwahl nächste Phase: Fable für die Katalogentscheidung
  (§ 6) und für die Auswertung von Lauf 4 und 5; Opus für
  Aufträge und Berichte; Blatt-Chats Opus.

## 5 Offene Punkte und verworfene Ansätze

Offen, in dieser Reihenfolge:
1. Katalogentscheidung aus den Belegdateien (Fable): Sek-I-Marke
   je Einheit und Sprosse (Stufe, Auslöser H); Sek II: bleibt es
   bei GK ohne Frage (Empfehlung, weil eine Kursartfrage bei 37
   von 44 Einträgen käme); die drei Stufenfehler aus § 3; die
   sieben Sek-II-Befunde. Danach ein Auftrag, der die Marken in
   die Einträge schreibt.
2. Lauf 5 mit v4.2 im Blatt-Projekt, Vorschlag Eingabe
   „nullstellen kl. 10" – misst die Planfrage an ihrem Anlass.
   Archiv ablegen (Muster archiv/auftrag-lauf4-ablage.md), dann
   auswerten.
3. v4.3: Planfrage auch bei Test-Richtung (2.6), wenn die Themen
   nicht einzeln aufgezählt sind und keine Übungsaufgaben
   vorliegen – Lücke in v4.2, Lauf 4 wäre wieder ohne Frage
   durchgelaufen; Schulformfrage mit H-Marke; Kursartregel nach
   Punkt 1.
4. Lauf 4 gegen ziel.md auswerten (Fable).
5. v4.2 von Fable gegenlesen lassen, weil auf Opus gebaut – vor
   oder mit v4.3.
6. schwach: Lückenbeispiele auch im Lernblatt – nach dem ersten
   Lauf mit der Option.
7. ziel.md § 5: „Beispiel je Typ" als entschieden streichen;
   „Kursart ohne Zuruf" nach Punkt 1.
8. Befunde-Skript (blaetter/befunde.md) ab dem fünften Lauf.
9. Sonnet-Vergleichslauf.
10. Prompt kürzen um etwa ein Drittel – nach v4.3.
11. Prüfungsblatt-Prompt auf ziel.md umbauen.
12. Katalog: Gegenlese Sek II, Kategorien je Prüfungsart, Boden
    unter Klasse 8; katalog/_vorlage.md Zeile 20; befund-geltung-
    und befund-inkonsistenzen-2026-09-21.md fehlen in README.md;
    leerer Kasten zum Selbstausfüllen; Band aller Themen;
    \liniendia Overfull 5,7 pt in halber Spalte.

Verworfen:
- Seitenschätzung als Auslöser der Umfangsfrage – vor dem Bau
  nicht messbar; die Zahl der Einheiten ist das ehrliche Maß.
- Jede Sprosse eine eigene Hauptnummer – zerstört die Leiter.
- Feste eigene Nummer für die letzten Teilaufgaben (für Starke)
  – legt den Schnitt fürs Blatt fest und wirkt wie eine
  Niveauüberschrift; „blatt 0 kurz" und „ab d)" leisten es.
- Verworfenes der Übergaben 2026-09-22b bis d gilt weiter.

## 6 Nächster Arbeitsschritt

Katalogentscheidung Niveaustufe und Kursart (Fable): die Zahlen
und Ermessensfälle aus katalog/_niveaustufen-belege.md und
katalog/_kursart-belege.md lesen und dem Lehrer die Entscheidungen
einzeln vorlegen – zuerst, ob der Auslöser „Stoff auf H" für die
Sek-I-Schulformfrage gilt. Liegt vorher ein Lauf-5-Archiv vor,
zuerst ablegen und auswerten.
