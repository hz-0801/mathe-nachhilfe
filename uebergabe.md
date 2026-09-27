# Übergabe verbessereBlaetter – 2026-09-27 (Chat vom 26./27.09.)

Vorherige Übergabe: archiv/uebergabe-2026-09-26.md.

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, damit
erzeugeUnterrichtsblatt() und erzeugePrüfungsblatt() aus wenigen
Wörtern druckfertige Blätter bauen. Maßstab ist ziel.md
(Stand 25.09.2026). Neue Linie seit 26.09. (§ 4): Blätter
entstehen künftig durch Auswahl aus einer Aufgabenbank, nicht
durch Erzeugung im Chat; der Chat wird vom Bauplatz zum Schalter.
ziel.md ist darauf noch nicht nachgezogen (§ 6).

## 2 Arbeitsgrundlage

- ziel.md (25.09.2026), unverändert; Nachzug offen.
- hz-0801/aufgabenbank (neu, 26.09.): bank.md (Form und Regeln,
  Stand nach zwei Prüfsteinen), werkzeuge/bank-pruef.py v0.2
  (Ergebnisstelle, Ankreuzen, Bausteine, Grafik, Sperre; Mengen
  als Warnung), werkzeuge/mappe.py und mappen/<eintrag>.md (acht
  Mappen, dazu mappen/_bausteine.md), auftrag-eintrag.md
  (Vorlage je Eintrag). Gefüllt: prozentrechnung (275 Zeilen),
  quadratische-funktionen (257 Zeilen), beide mit stand.md und
  Entscheidungen; im Lauf seit 27.09. 07:10: lineare-funktionen,
  quadratische-gleichungen, lineare-gleichungen, terme,
  bruchrechnung, pythagoras (sechs Web-Sitzungen parallel).
- blattbau: unterrichtsblatt.md v4.4 (Commit 36b7b12, 1447
  Zeilen; Projektanweisung in erzeugeUnterrichtsblatt() ist v4.4
  seit 26.09. 19:18); CHANGELOG-Zeile v4.4; mathblatt.sty Stufe 6
  (cad91ae) mit Anleitung und Probeblatt.
- mathe-nachhilfe: Nacht 29.09. (Datei nacht-bericht-2026-09-29.md,
  gelaufen am 26.09. 14–17 Uhr) vollständig: beschluss-2026-09-26.md
  (Urteile Übersicht, Eichung, CAS Berlin, kreis, Vorschläge),
  Deutungsliste (f), 2018-ea-B CAS erfasst mit Unterschreitung
  69/85, Berliner CAS-Hefte nachgetragen (Typen 1421), 2017-ga-B
  CAS erfasst, marken-bau kreis 1, Merkkasten 0 = p(x),
  katalog/_vorschlaege-sprossen-2026-09-29.md,
  katalog/_vorschlaege-2026-09-29.md (Befund 3–8).
- Testlauf v4.4 läuft seit 26.09. abends im Code-Tab
  (auftrag-testlauf.md, Ordner blaetter/testlauf-<datum>/);
  Bericht bericht-testlauf-<datum>.md noch nicht gelesen. Dieser
  Auftrag zieht auch werkzeuge/testlauf-eingaben.csv (Eingabe 5
  und 6) und die Testlauf-Vorlage nach und legt zwei Posten an
  (v4.5 straffen; Aufträge mit Get-Date datieren).
- Weiter gültig: befund-testlauf-2026-09-25.md (Quelle von v4.4),
  katalog/_vorschlaege-2026-09-27.md (vier Abschnitte,
  entschieden am 26.09., siehe § 4), Belegdateien, blatt-pruef.py
  v0.4, testlauf-auftrag.md.

## 3 Arbeitsstand

Abgeschlossen: Urteile Übersichtsblatt (vertagt), Eichung 2017,
CAS Berlin, kreis 1; Nachtauftrag 29.09.; v4.4 gebaut und
eingespielt (Repo und Projektanweisung); Testlauf v4.4 gestartet;
Katalog-Urteile zu _vorschlaege-2026-09-27.md (alle vier
Abschnitte) und _vorschlaege-sprossen-2026-09-29.md (sechs
Vorschläge); Linie Regal/Bank beschlossen; Repo aufgabenbank mit
zwei Prüfsteinen und Vorbereitung; Modellregel und Web-Sitzungen
in der Projektanweisung (Stand 27.09.c).

Läuft: sechs Bank-Sitzungen (seit 07:10); Testlauf v4.4 am PC.

Nicht begonnen: Katalogauftrag aus den Urteilen (§ 6 Punkt 2);
Nachbesserung der zwei Prüfstein-Einträge gegen bank-pruef v0.2
(83 Abweichungen, Schreibweisen); Runde 3 der Bank (19 Mappen,
19 Sitzungen; Aufträge liegen beim Lehrer als Dateien
auftrag-bank-mappen-3.txt und auftrag-bank-<eintrag>.txt);
Zusammenbau-Skript (Bank → Blatt); Nachzug ziel.md und
Projektbeschreibung; Lückenlauf Lehrwerke gegen Einheiten.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Aus früheren Übergaben gelten weiter: Marken, Zweigzeile,
Ich-kann-Titel, schwach als Form, Bestellung, Regel A/B, Testlauf
je Version, ein Schreiber je Ordner, Beschlüsse vom 26.09.
(beschluss-2026-09-26.md).

Neu 26./27.09.:
- Linie: Weg 1 Regal (Blätter über Nacht vorproduziert) sofort,
  Weg 2 Aufgabenbank als Richtung – begonnen wurde direkt mit der
  Bank, weil Aufgaben schreiben nur Repo und Netz braucht. Der
  Chat in erzeugeUnterrichtsblatt() wird zum Schalter: Bestellung
  lesen, aus der Bank zusammensetzen, kompilieren; Erzeugung nur
  für Ausnahmen (Klassenarbeit mit Schulaufgaben, personalisiert).
  Ein Gleis, mehrere Rezepte (Lernblatt, Fokus, Prüfungsheft);
  ohne Abo bleibt die Bank per Skript nutzbar.
- Bank-Form: JSONL je Einheit, Felder nach bank.md; pruef trägt
  nur Ergebniszahlen (keine Zwischenwerte, keine Distraktoren);
  Erkennungsschritt 4, Grundfall 5, Sprosse 3, Prüfungshöhe 2 je
  Original, Typ ohne Kette 3, Pflicht je 3, Zone-Paar; Reihenfolge
  Erkennungsschritt → Kette → Typen ohne Kette → Pflicht; Sperre
  mit Ausnahme für den Gegenstand der Kette; Opus schreibt,
  Prüfskript bis null Abweichungen vor jedem Commit.
- Web-Sitzungen: vom Cloud-Guthaben, parallel in getrennten
  Ordnern, nur Mappe lesen; der Lehrer hat das Guthaben
  freigegeben („kann verbrannt werden"), Ziel schnellstmöglich
  großer Datenbestand ohne Qualitätsverlust.
- Katalog-Urteile: _vorschlaege-2026-09-27.md alle vier
  Abschnitte übernehmen; dabei Typ 5.14 und 7.4 nicht zuordnen,
  dritte Kette potenz 5 als Sprosse mit „baut auf: Einheit 3"
  (kein Vorrat), daten 7 Variante A, Sinussatz/Lösbarkeit EBR
  nach Fachbrief 10 (ab 2028), 2025-GYM-K5d Nebentyp „Pythagoras
  Hypotenuse", Namensabweichungen schließen ohne Änderung.
  _vorschlaege-sprossen-2026-09-29.md: alle sechs übernehmen,
  einschließlich Einheitentausch quadratische-gleichungen
  (p-q-Formel vor Nullprodukt); Zehn-Prozent-Schritte in
  prozentrechnung E3 als Vorform vor den Ein-Prozent-Weg.
- Prüfungsheft-Prompt: kein Umbau mehr nach v4.4-Muster; er wird
  zum zweiten Auswahlrezept der Bank.
- v4.5 (Straffung) erst nach dem Testlauf v4.4; Kandidaten 4.4,
  4.6 in die Anleitung, Muster 2.3, 6.3.
- Modellregel: Opus 5.5 Regelfall auch für Urteilsarbeit; Fable
  nur auf Wahl des Lehrers. Prognosen nur als Schätzung mit
  Grundlage (global.md, Vorschlag § 6).
- Übersichtsblatt vertagt; „mit übersicht" nicht in v4.4.
- Katalogbefund neu: Vorstufe prozentrechnung E4 verlangt Zahl
  (stand.md prozentrechnung); Grafiken der Bank nie kompiliert.

## 5 Offene Punkte und verworfene Ansätze

Offen:
- Testlauf-Bericht v4.4 lesen (Montag nach 18:00), dann
  Blatt-Chat „quadratische gleichungen 9 oberschule" – oder, nach
  der neuen Linie, stattdessen der Zusammenbau aus der Bank.
- Zusammenbau-Skript: aus bank/<eintrag>/ nach Bestellung
  (Einheiten, Zone, Fokus) Quelltexte mit den Bausteinen der
  Vorlage bauen, kompilieren; Zone, Zweigzeile, Kopfzeile,
  Abhakseite, Nummern deterministisch. Erster Prüfstein
  prozentrechnung gegen die drei vorhandenen Blätter. Braucht
  LaTeX → Code-Tab, ab Montag.
- Kurzer Prompt für erzeugeUnterrichtsblatt() als Schalter, nach
  dem Zusammenbau-Skript.
- potenz-exponentialfunktionen und daten in der Bank erst nach dem
  Katalogauftrag (Einheit 5 und 7 haben noch keine Sprossen).
- quadratische-gleichungen in der Bank wird mit der alten
  Einheitenfolge gebaut; nach dem Katalogauftrag e2/e3 umbenennen.
- Nachbesserung prozentrechnung und quadratische-funktionen gegen
  bank-pruef v0.2 (Sonnet-Web-Sitzung, nach den sechs).
- Lückenlauf: alle Kapitel der Lehrwerks-Inhaltsverzeichnisse
  gegen die Einheiten des Katalogs (Kandidaten: Bruchterme und
  Bruchgleichungen, lineare Ungleichungen, Boden Kl. 5/6).
- Aufräumen mathe-nachhilfe (Wurzel auf fünf Dateien, Belege in
  katalog/belege/, README als Landkarte plus Inventar aus Skript)
  – nach dem Testlauf, Sonnet, mit Verweisprüfung.
- Schülerbücher: kapitelweise als Fotos in den Chat, wenn ein
  Thema dran ist (Schreibform, Kettenfolge, Kapiteltest); nichts
  ins Repo. Welche Reihen, ist noch nicht genannt.
- global.md: Absatz „Prognosen" (Wortlaut in der Kandidatendatei
  dieses Umzugs); der Lehrer hat „später" gesagt.
- ziel.md und Projektbeschreibung auf die Linie nachziehen.
- Aus der Übergabe vom 26.09. weiter offen: Vorlage Stufe 7,
  Fundamente B, Förderhefte, Fotos Inhaltsverzeichnisse, Berlin
  2026 be-gk/lk, einsortieren.py Sorte uebersicht (ruht).

Verworfen (mit Grund):
- Übersichtsblatt aus Merkkästen: zu dicht; nur Abbildung und
  Tabelle, neuer Prüfstein irgendwann.
- Prompt straffen vor dem Testlauf: zwei Änderungen auf einmal
  sind nicht messbar.
- 29 Bank-Sitzungen in der ersten Nacht: Form war ungeprüft;
  Prüfstein zuerst hat vier Formfehler vor der Breite gefunden.
- Alle 74 Blätter über Nacht bauen (Weg 1 pur): durch die Bank
  ersetzt, die dasselbe liefert und Korrekturen behält.
- Aufräumen als Kosmetik: nur mit Verweisprüfung und Landkarte,
  sonst nicht.

## 6 Nächster Arbeitsschritt

Modell: Opus 5.5.

1. Berichte der sechs Bank-Sitzungen lesen (Zeilen, Abweichungen,
   Befunde in stand.md); Guthaben ablesen. Bei brauchbarer Form:
   auftrag-bank-mappen-3.txt (Sonnet) starten, danach die 19
   Eintragsaufträge parallel; Nachbesserungs-Sitzung für die zwei
   Prüfsteine.
2. Katalogauftrag für den Code-Tab (ab Montag, nach dem Testlauf)
   aus § 4: Einträge potenz 5 und daten 7 ausbauen, Niveaustufe G
   (Sinussatz, Lösbarkeit), GYM-K5d, Namensabweichungen
   schließen, Sprossenvorschläge umsetzen mit Einheitentausch,
   Katalogbefund 3–8 nach _vorschlaege-2026-09-29.md, Vorstufe
   prozentrechnung E4, Lückenlauf als Vorschlagsdatei; Marken neu
   bauen; danach Mappen für potenz und daten.
3. Testlauf-Bericht lesen; dann Zusammenbau-Skript als Prüfstein
   an prozentrechnung (Code-Tab, LaTeX).
4. ziel.md, Projektbeschreibung nachziehen; global.md-Absatz
   „Prognosen" vorlegen.
