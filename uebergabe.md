# Übergabe verbessereBlaetter – 2026-09-30b (Chat 30.09. 08:40 bis abends)

Vorherige Übergabe: archiv/uebergabe-2026-09-30.md (Nacht 29./30.09.
mit Nachträgen des Tages; dort § 3 die Einzelheiten des 30.09.).

## 1 Ziel

Der bestmögliche Themenkatalog, die Aufgabenbank und die Prompts,
damit aus wenigen Wörtern druckfertige Blätter entstehen. Maßstab
ist ziel.md (28.09.); Leitbild: ein Blatt für alle Schüler, aus der
Bank zusammengesetzt, Chat als Schalter.

## 2 Arbeitsgrundlage

- mathe-nachhilfe: ziel.md (28.09., unverändert); katalog/ auf
  db8d2a3 (Katalogauftrag 30.09.: 23 Vorschläge aus katalog/
  _vorschlaege-2026-09-30.md, Marke „(kein P10-Stoff)“ in
  _vorlage.md; 17 Einträge mit Kopfzeile „Änderungen 2026-09-30“);
  faellig.md (Stand 30.09. abends).
- aufgabenbank auf 546d722: bank.md 2026-09-30b (Regel R.1 zu
  Erkennungsschritten und Vorstufen; „(4×)“ ist Blattzahl, Bank hält
  fünf; Deutungstypen in Sek II tragen Darstellung/Anwendung;
  Original über zwei Einheiten an der späteren Prüfungssprosse;
  „(kein P10-Stoff)“ steuert nur den Zusammenbau); werkzeuge/
  mappe.py nimmt Kennungen aus den Ketten auf, 72 Mappen auf
  Katalog db8d2a3; bank-pruef.py v0.12; auftrag-eintrag.md 29e;
  bank/<eintrag>/stand.md mit Abschnitt „Nachzug 30.09.“ in 16
  Einträgen. Bank 15 351 Zeilen; _punkte.csv 2 851 Urteile,
  Gegenprobe bestanden.
- blattbau unverändert: unterrichtsblatt.md v4.4, pruefungsblatt.md
  v0.15; werkzeuge/zusammenbau.py kennt „(kein P10-Stoff)“ nicht.
- anweisungen: projekt-verbessereBlaetter.md 2026-09-30 (neu:
  Alltagssprache, Revisionen, Kontingent-Messwert), kandidaten.md
  2026-09-30b.
- TER-S1, TER-S2 weiter nur im alten Chat (Lehrer).

## 3 Arbeitsstand

Erledigt 30.09. (Einzelheiten in archiv/uebergabe-2026-09-30.md
§ 3):
- Nachbesserungen in der Bank (antwort-Gerüst „__“ in 455 Zeilen,
  drei Einzelzeilen, „ohne genau zu rechnen“ in acht Einheiten).
- Katalogauftrag aus den 66 Katalogbefunden der stand.md-Dateien:
  Vorschlagsdatei, Urteil im Chat (Lehrer), Umsetzung in Katalog,
  bank.md, mappe.py; Revision: dritte binomische Formel ist
  regulärer Stoff mit Marke „(kein P10-Stoff)“ statt Vorrat.
- Bank-Nachtrag in 16 Einträgen (terme, lineare-gleichungen,
  binomische-formeln, bruchrechnung, brueche-dezimalzahlen,
  prozentrechnung, tangente, binomialverteilung, flaecheninhalt-
  durch-integration, skalarprodukt, kurvenuntersuchung, rationale-
  zahlen, ableitung-und-aenderungsrate, abstaende, ebenen,
  zufallsexperimente), alle 0/0 mit --katalog; Erkennungsschritte
  nach R.1; Prüfungssprossen der Sek-II-Einträge mit den Originalen,
  die die Mappe vorher nicht kannte; 63 neue Urteile.
- Befund: Die 48 nicht nachgezogenen Einträge standen bisher gegen
  Mappen vom 25.09.; gegen die neuen Mappen zeigt --katalog dort
  rund 5 000 Abweichungen (fast alles „sprosse_text nicht
  wortgleich“, Katalogstand 27./29.09.). Das ist der ausstehende
  Nachzug, kein neuer Schaden.

Nicht erledigt: Schalter-Prompt; Nachzug der 48; Gegenlese;
pruefungsblatt.md 1.1; K2–K7; Bausteine (§ 5).

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Frühere Übergaben gelten weiter (archiv/); die vom 30.09. früh
(Vorstufen 0/−1/−2, eine Prüfungssprosse je Kette, Musterbeispiel
je Kette, Sperre mit Körperregel, Pooldublette = ein Original,
Agenten je in eigenem Klon) bleiben.

- Reihenfolge seit 30.09. mittags (Lehrer, „zweiter Weg“): erst
  Katalog und Schalter, Gegenlese je Eintrag erst, wenn der
  Schalter daraus ein Blatt baut.
- Marke „(kein P10-Stoff)“ (Lehrer): regulärer Schulstoff, nicht
  Teil der P10-Vorbereitung; das Prüfungsheft lässt die Sprosse
  aus, das Unterrichtsblatt führt sie; Bankzeilen wie überall. Die
  Marke „(Vorrat)“ bleibt für Nicht-Mindeststoff. „Kein P10-
  Original“ ist eine Beobachtung, keine Marke.
- Regel R.1 (bank.md): ein Erkennungsschritt wird einmal angelegt,
  in der ersten Einheit seines Bereichs ohne Vorstufe desselben
  Handgriffs; derselbe Handgriff = dieselbe Entscheidung an
  derselben Vorlage; zwei Ketten mit gleicher Vorstufe: Zeilen einmal
  bei der ersten.
- Alltagssprache und Revisionen (Lehrer, kandidaten.md 30b): Befunde
  und Vorschläge im Chat wie am Tisch einem Kollegen, Nummern und
  Kennungen bleiben in der Datei; eine frühere Festlegung, die
  nicht mehr optimal scheint, als eigene Entscheidung mit Optionen
  und Folgen vorlegen.
- Kontingent (Messwerte 30.09.): Woche 41 % (08:40) → 42 % (13:00,
  ein Opus-Agent 0,16 Mio) → 53 % (abends); Fable 21 → 24 → 46 %.
  Dazwischen 3,3 Mio Token Fable-Agenten und dieser Chat:
  Fable-Agenten zahlen Woche und Fable zugleich (rund 3 % Woche und
  6–7 % Fable je Mio). Lehrer: nicht alles auf einmal – Runden mit
  Ablesen dazwischen; heute keine Agenten mehr. Die Hochrechnung
  der Anzeige („morgen Nacht“) rechnet mit dem Nachmittagstempo.
- Modellwahl für die nächste Phase: Schalter-Prompt im Chat, Opus
  (Fable auf Wahl des Lehrers); Nachzug der 48 ab Montag 18:00 mit
  Opus-Agenten, sechs je Runde, Nutzungsanzeige vor jeder Runde
  (Messwert 29.09.: 1–1,5 % Woche je Eintrag).
- Nach jedem Mappenbau läuft das Prüfskript über die ganze Bank
  (mehr Originale kippen Bestandszeilen über die Sperre).

## 5 Offene Punkte und Verworfenes

- Zusammenbau (zusammenbau.py, pruefungsblatt.md): Sprossen mit
  „(kein P10-Stoff)“ im Prüfungsheft auslassen; Vorrat-Originale an
  einer Prüfungssprosse sind je Zeile nicht kennzeichenbar
  (brueche-dezimalzahlen), Regel nötig.
- blattbau-Bausteine, die neue Bankzeilen brauchen: Pfeile über
  einem Term und zerlegtes Quadrat (binomische-formeln), Prozent-
  streifen über 100 % (prozentrechnung), Pfeil an der Zahlengeraden
  (rationale-zahlen), Figur aus zwei Rechtecken (terme). Bis dahin
  form text ohne Grafik.
- Prüfskript v0.13: Uhrzeiten „15:00“ nicht als Term sperren; Kette
  gegen die Sprossenliste der Mappe abgleichen (fehlende Sprosse);
  „2 je Original“ prüfen; Nein-Antwort ohne Zahl ohne pruef;
  Formprobe: Wechsel Bruch/Dezimal/Prozent als eigene Richtung;
  \int in STANDARD. punkte-nachziehen.py: bei Kettenverschiebung
  wortgleiche Zeile unter neuer id finden statt entfernen; nur die
  genannten Einträge anfassen.
- Katalog klein: terme Z. 21 „das Doppelte von x plus zwei“
  zweideutig; binomialverteilung E5-Vorstufe = Erkennungsschritt
  Z. 43 (eine streichen?); skalarprodukt 2019-be-gk-B3.2c an
  Sprosse und Prüfungshöhe derselben Kette; kurvenuntersuchung:
  R.1 legt den Erkennungsschritt in E3 an, wo er wenig nützt
  (Regel oder Bereich prüfen); marken-bau.py scheitert an
  quadratische-gleichungen (Bestand); Einsetz-Skript des
  Katalogauftrags liegt nicht im Repo (Regel verletzt).
- Gegenlese je Eintrag (ohne Mappe, nur neue und umgeschriebene
  Zeilen; gegenlese.md in den Ordnern zeigt auf alte ids);
  Urteilsbalance (P2 immer „Richtig“, P6 fast immer Nein) offen.
- funktionsklassen: 30 CAS-Originale 2017/2018 an keiner Sprosse –
  eigener Katalogauftrag „Ketten um den CAS-Nachtrag“.
- Ein Agent (kurvenuntersuchung) hat seine 16 Urteile selbst
  gefällt statt ein zweiter; bei der Gegenlese prüfen.
- Alte Posten: K2–K7 (faellig.md), winkel-dreiecke.md Z. 125.

Verworfen: Vorschlag 2.3 (Vorrat ans Kettenende) – ersetzt durch die
Marke; Fable-Agenten als Weg, die Woche zu schonen (Messwert);
Gegenlese aller 24 vor dem Schalter (zweiter Weg).

## 6 Nächster Arbeitsschritt

1. Schalter-Prompt nach ziel.md, im Chat: zuerst ziel.md,
   bank.md, werkzeuge/zusammenbau.md und zusammenbau.py (Aufruf,
   Eingaben) lesen, dann den Prompt bauen (Vorgehen „Vorgehen bei
   jedem neuen Prompt“ der Projektanweisung); die Regel „kein
   P10-Stoff“ gehört hinein; pruefungsblatt.md 1.1 im selben Zug.
   Erst Exemplar, dann Regel: ein Blatt aus einem nachgezogenen
   Eintrag (terme oder bruchrechnung) ist der erste Test.
2. Ab Montag 18:00: Nachzug der 48 übrigen Einträge in Runden.
3. Gegenlese je Eintrag, sobald der Schalter daraus ein Blatt baut.
