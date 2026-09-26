# Übergabe verbessereBlaetter – 2026-09-25 (abends; Chat vom 25./26.09.)

Vorherige Übergabe: archiv/uebergabe-2026-09-26.md.

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, damit
erzeugeUnterrichtsblatt() und erzeugePrüfungsblatt() aus wenigen
Wörtern druckfertige Blätter bauen. Maßstab ist ziel.md
(Stand 25.09.2026).

## 2 Arbeitsgrundlage

- ziel.md (25.09.2026), unverändert.
- Katalogeinträge mit Marken (Commit 7613213): je Lerneinheit
  die Zeile „Marken: OS Kl. n · GYM Kl. n · Prüfungswort · nicht
  für alle: …" (Sek II: „BE Qn · BB Qn · Kursart · Prüfungswort"),
  Typklammern „[OS 5, GYM 6]" an Typen mit eigener Stelle.
  Quelle der Zeile: werkzeuge/marken-bau.py aus den drei
  Belegdateien, katalog/_marken-entscheidungen.md (Regeln A und
  B, die 38 Fälle) und werkzeuge/marken-bau-stellen.txt.
  bericht-marken.md: Zahlen, Gegenproben, eigene Entscheidungen
  (19 Punkte), Listen (173 stehengebliebene Klammern, 20
  verschobene Einführungsklassen).
- Drei neue Katalogstellen (katalog/_marken-neue-einheiten.md):
  potenz-exponentialfunktionen Einheit 5 (Potenzfunktionen),
  daten Einheit 7 (Vierfeldertafel Sek I, Nummer hinter der
  Sek-II-Einheit 6), daten Einheit 1 mit Klassen-Typen. Nur
  Nummernzeile und Typen; Merkkasten, Sprossen, Blatt-0-Zeilen
  fehlen (faellig).
- blattbau/unterrichtsblatt.md v4.3 (Commit 512ae78),
  CHANGELOG-Zeile dort nennt jede Änderung; Projektanweisung in
  erzeugeUnterrichtsblatt() ist v4.3.
- Testlauf: werkzeuge/testlauf-eingaben.csv (zehn Eingaben mit
  Antworten und Prüfhinweisen), blaetter/testlauf-2026-09-25/
  (je Eingabe PDFs, Protokoll, sitzung.txt; stand.md;
  kennzahlen.md; lesezettel.md), bericht-testlauf-2026-09-25.md
  in der Wurzel. Auftrag: archiv/auftrag-testlauf-2026-09-25.md.
- Weiter gültig: katalog/_klassen-belege.md,
  _pruefungswort-belege.md, _sek2-ordnung-belege.md,
  _klassen-ermessen.md; werkzeuge/blatt-pruef.py;
  nacht-bericht-2026-09-25.md und -26.md.

## 3 Arbeitsstand

Abgeschlossen: 38 Ermessensfälle entschieden; Marken in allen
Einträgen (273 Zeilen, 262 Typklammern); v4.3 gebaut, im Repo
und in der Projektanweisung; Nachtauftrag Testlauf gestartet
(25.09. nachmittags, alle zehn parallel), Ergebnis nicht ausgewertet. Remote Control
für Claude Code eingerichtet (Projektanweisung „Handy").

Befunde, noch ohne Folge:
- Gegenproben der Übergabe vom 26.09. waren zweimal falsch:
  lineare-funktionen 4 hat „P10" (3 von 13), nicht „P10 oft";
  quadratische-gleichungen 2 hat GYM Kl. 8–9 (Elemente 8), nicht
  Kl. 9. Beide Belegwerte gelten.
- kreis 1 stand vor Regel A bei „OS Kl. 5–8, GYM 5–6"; jetzt
  „OS 7–8, GYM 7–8", Zeichnen-Typ „[OS 5–8, GYM 5–6]".
- Zwanzig Einführungsklassen haben sich durch Regel A und B
  verschoben (Liste in bericht-marken.md).
- Testlauf (Bericht bericht-testlauf-2026-09-25.md): alle
  zehn fertig im ersten Anlauf, Ersatzweg Sub-Agenten (claude.exe
  „Not logged in" für -p – inzwischen angemeldet), alle zehn
  parallel; sieben Blätter mit 74–124 Werkzeugaufrufen (Chat:
  zwanzig); Vorlage ohne Zweigzeile, Abhakseite,
  Verzeichniszeile, gleichungsraster-Umbruchfehler; Zonen von
  Nr. 1 und 5 mit eigener Nummerierung (Nummern doppelt);
  Nr. 9 (Kl. 12): alle Zweige vor der Eingabeklasse, 1.5 regelt
  es nicht; drei Sitzungen lasen die Vorlage; „mit Ausblick" bei
  kreis ohne Ausblick-Zweig, weil alle Marken bis Kl. 8 reichen
  (CSV-Erwartung war falsch); protokoll.txt zählt Aufrufe zu
  niedrig; blaetter/kennzahlen.md passt nicht mehr zum Katalog.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

Aus der Übergabe vom 26.09. gelten weiter: Marke = Klasse je
Schulform aus den Lehrwerken, nicht der RLP-Buchstabe; Klasse und
Schulform ordnen, filtern nicht; Zweigzeile Fertigkeit ·
Zeitmarke · Prüfungswort; Prüfungswort-Schwelle 7 von 13 (Haupt
oder Neben); Ich-kann-Titel; schwach ändert die Form; Bestellung
„nur das Neue / mit Wiederholung / mit Ausblick"; Bigalke/Köhler
nur Reihenfolge-Quelle; Kaufen nur zwei Förderhefte; fremde
Sammlungen nur für die 22 Sprossen; Cloud-Sitzungen nur für
Repo-und-Netz-Aufträge.

Neu (25./26.09.):
- Regel A: Eine Vorstufe setzt keine Einführungsklasse; sie wird
  Typzeile am genannten Typ, sonst Zeile ohne Klassenwirkung. Nur
  der Kern der Einheit (Nummernzeile) setzt die Klasse.
- Regel B: Verlagsmarken (LVL, Streifzug, Üben, …) setzen keine
  Klasse; sie stehen unter „nicht für alle". „Sonderfälle" und
  unerklärte Symbolzeichen sind keine Marke.
- Marken-Form im Eintrag: erzeugte Zeile unter der Nummernzeile,
  Typklammer am Typ, reine „(Kl. n)"-Klammern entfernt; Klammern
  mit mehr Inhalt bleiben als Herkunft. Nur die Marken-Zeile ist
  Zeitquelle für den Prompt (v4.3, 1.5).
- Sek-I-Lücken werden nachgezogen, wenn alle Lehrwerke den Stoff
  führen (Potenzfunktionen, Vierfeldertafel, Klasseneinteilung);
  Prüfungswort sagt dann „keine P10-Aufgabe".
- v4.3-Festlegungen (in CHANGELOG): Standpunkt Oberschule ohne
  Schulform, Spanne „je nach Buch", Eintragsfrage bei doppeltem
  Stichwort, Zone „kennst du schon" mit Dateiname KennstDuSchon,
  Abhakseite „Das kann ich", Sek-II-Zeitmarke mit Halbjahr je
  Land, LK aus der Marke „nur LK".
- Testlauf ist der Regeltest je Prompt-Version (zehn Eingaben,
  feste Liste); ein Blatt-Chat je Version prüft danach den Weg,
  den Code nicht geht. Ergebnisse zweier Läufe werden nebeneinander
  gelegt, nicht einzeln beurteilt.
- Aufträge, die schwer zurücknehmbare Dateien schreiben (Marken,
  Prompt), laufen auf Opus, wenn sie je Stelle lesen müssen;
  Sonnet nur, wenn nichts zu lesen bleibt.
- Zwei Sitzungen im selben Ordner: nur eine schreibt.

## 5 Offene Punkte und verworfene Ansätze

Offen (Posten in faellig.md, soweit dort):
- Auswertung des Testlaufs (nächster Schritt).
- FHR-Wort an den acht Sek-I-Einheiten mit Sek-II-Zeilen.
- Belegskripte (klassen-belege.py, pruefungswort-belege.py) auf
  die drei neuen Katalogstellen umstellen; bis dahin bricht
  klassen-belege.py beim Neubau ab.
- potenz-exponentialfunktionen: alte Lesart in Einheit 1
  („Potenzfunktion als zweiter Funktionstyp … Vorrat") und
  doppeltes Eingabewort „potenzfunktion" bereinigen; Merkkasten,
  Sprossen, Blatt-0-Zeilen für Einheit 5 und daten 7.
- 173 Klammern mit Klassenangaben neben den Marken (zweimal
  Wahrheit); erst bereinigen, wenn die Verortung umgebaut wird.
- blattbau: core.autocrlf ohne .gitattributes.
- klassen-ermessen.py: Zitatfehler bei Mehrfachfällen.
- Testlauf-Auftrag: Reihenfolge statt Gleichzeitigkeit, Zeiten
  aus Get-Date, Regelweg claude -p jetzt möglich (angemeldet);
  nach der Auswertung ändern.
- Vorlage Stufe 5: Zweigzeile, Abhakseite, Verzeichniszeile,
  gleichungsraster-Umbruch (faellig, aus dem Testlauf).
- Prüfskript: Lesart Merkkasten; Typen ohne Treffer von Hand
  gegenlesen; vier neue Klassen-Typen als „ohne Treffer".
- Einträge (Nacht 26.09.): flaechen.md Original-ids vertauscht;
  zuordnungen.md und terme.md ohne neuere GYM-Typen; themen.csv
  Maßstab bei zuordnungen statt strahlensaetze; 2025-GYM-K5d
  Nebentyp prüfen; koerper 5 nennt keine Pyramide/Kegel/Kugel
  als Teilkörper.
- Fundamente B Qualifikationsphase nicht im Repo.
- In etwa zwei Wochen: Fotos der Inhaltsverzeichnisse der
  Schülerbücher; im Chat lesen, je Buch eine Zeile.
- Förderhefte, wenn gekauft: Prüfstein-Befund.
- Prüfungsheft: Umbau nach v4.3-Muster, Schwelle „selten".
- Verschmelzung der Prompte: prüfen, sobald der Prüfungsprompt
  Abschnitt 0–2 nachgezogen hat.

Verworfen (mit Grund):
- Blatt-Chat als erster Prüfstein von v4.3: zehn Blätter in
  Code sind billiger und vergleichbar; der Chat prüft nur die
  Interaktion, dafür einer je Version.
- marken.csv als eigene Datei statt Zeile im Eintrag: ein
  Abruf mehr je Blatt bei enger Werkzeuggrenze.
- Vierfeldertafel als Einheit 6 mit Umnummerierung: „Einheit 6"
  sitzt in Belegen, Niveaustufung und Verweisen fest.
- Umzug in der Cloud-Sitzung parallel zum Nachtlauf: zwei
  Schreiber im selben Repo.

## 6 Nächster Arbeitsschritt

Modell: Fable (Auswertung eines Laufs gegen ziel.md).

1. bericht-testlauf-2026-09-25.md, blaetter/testlauf-2026-09-25/
   lesezettel.md und kennzahlen.md lesen; der Lehrer liest die
   PDFs nach dem Lesezettel und meldet, was ihm auffällt.
2. Je Eingabe gegen ziel.md § 1–3 und den Prompt v4.3 urteilen:
   Zweigzeile, Zeitmarke (Nr. 1 gegen 2), schwach als Form
   (Nr. 3), Zone/keine Zone (Nr. 4), Typklammer (Nr. 5),
   Stufenschnitt (Nr. 6), Eintragsfrage (Nr. 7), neue Einheit
   (Nr. 8), Sek II (Nr. 9), Klassenarbeit (Nr. 10). Befunde
   trennen: Prompt (→ v4.4), Katalog (→ Eintrag), Werkzeug
   (→ Testlauf-Auftrag, Prüfskript), Vorlage (→ Stufe 5).
3. Erst dann ein Blatt-Chat mit „quadratische gleichungen 9
   oberschule" im Projekt (Opus) für Planfrage, drei Antworten,
   Werkzeuggrenze und Dateikarten; Protokoll-Archiv über
   einsortieren.py ablegen.
4. Nach den Befunden: Testlauf-Auftrag nachziehen (Reihenfolge,
   Zeiten) und v4.4 nur aus Befunden, keine Regel aus Vermutung.
