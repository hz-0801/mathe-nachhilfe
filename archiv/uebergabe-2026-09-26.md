# Übergabe verbessereBlaetter – 2026-09-26 (nach zwei Nächten)

Vorherige Übergabe: archiv/uebergabe-2026-09-24.md.

## 1 Ziel

Der bestmögliche Themenkatalog und die beiden Prompts, damit
erzeugeUnterrichtsblatt() und erzeugePrüfungsblatt() aus wenigen
Wörtern druckfertige Blätter bauen. Maßstab ist ziel.md
(Stand 25.09.2026).

## 2 Arbeitsgrundlage

- ziel.md (25.09.2026): drei Bilder – Leiter je Typ, Baum je
  Thema, Zeitachse je Schüler; Zone „kennst du schon" statt
  Blatt 0; „schwach" als Form; Zweigzeile und Ich-kann-Titel;
  Klasse und Schulform ordnen, filtern nicht.
- katalog/_klassen-belege.md (Nacht 25.09.): Klasse je
  Lerneinheit aus 9 Regelreihen und 4 Förderheften, Typzeilen,
  Verlagsmarken; Bauskript werkzeuge/klassen-belege.py mit
  Daten. Zahlen: 29 Einträge, 116 Einheiten, 649 Typzeilen,
  401 Förderheftzeilen, 250 Ermessensfälle.
- katalog/_klassen-ermessen.md (Nacht 26.09.): die 250 Fälle
  nach Sorte; Urteil brauchen nur „Katalog verortet den Stoff
  anders" (23) und „Frühe Stelle als Grundstufe gelesen" (15).
- katalog/_pruefungswort-belege.md (Nacht 26.09.): P10-Jahrgänge
  je Sek-I-Einheit und Typ (114 Einheiten, 1308 Typen), Sek II
  gegen Abitur GK/LK und FHR; Skript werkzeuge/pruefungswort-
  belege.py.
- katalog/_sek2-ordnung-belege.md (Nacht 26.09.): Halbjahr und
  Kursart je Sek-II-Einheit (157) aus RLP GOST BE und BB, FOS,
  Bigalke/Köhler; Skript werkzeuge/sek2-ordnung-belege.py.
- werkzeuge/blatt-pruef.py und blaetter/kennzahlen.md (Nacht
  26.09.): Kennzahlen je abgelegtem Blatt (Seiten, Nummern und
  Teilaufgaben je Seite, Titelform, letzte Darstellung,
  Antwortform, Fachwörter, Typen ohne Treffer).
- quellen/: Inhaltsverzeichnisse jetzt für Sekundo, Mathematik
  2022/2023, Schnittpunkt, Mathematik heute (OS, Kl. 5–10),
  Fundamente B, Elemente, mathe.delta, LS-Fahrplan (GYM,
  Kl. 5–10); vier Förderhefte; fremde Aufgabensammlungen
  (Bayern Gymnasium 8/10, Realschule 6/8, Realschulabschluss;
  IQB VERA-8) lokal unter hefte/fremd/, Fundliste quellen/
  fremdsammlungen-fundliste.md, Fundstellen katalog/
  _fremdoriginale-belege.md (18 von 22 Sprossen, meist
  Teilleistung).
- blattbau/unterrichtsblatt.md v4.2 (unverändert seit 24.09.);
  Befund befund-schwach-blatt-2026-09-24.md.
- Nachtberichte nacht-bericht-2026-09-25.md und
  nacht-bericht-2026-09-26.md (Lesarten, Befunde, Entscheidungen
  der Läufe).

## 3 Arbeitsstand

Abgeschlossen: Grundlage (ziel.md) neu beschlossen; alle
Belegdateien für Klasse, Prüfungswort und Sek-II-Ordnung liegen
mit Skripten vor; Prüfskript misst die vier abgelegten Blätter.
Nichts davon ist in einen Katalogeintrag oder Prompt
eingeflossen.

Wesentliche Befunde der Nächte:
- Spanne OS/GYM ohne gemeinsame Klasse nur bei 6 Themen
  (zinsrechnung, lineare-gleichungssysteme, quadratische-
  funktionen, quadratische-gleichungen, potenz-
  exponentialfunktionen, daten); bei 17 Themen liegt eine
  Einheit schon in Klasse 5 oder 6 („Boden").
- Prozentrechnung Einheit 1 am Gymnasium schon Klasse 5.
- Blätter v4.0–4.2 lassen laut Prüfskript viele Katalogtypen
  aus (Prozent-Gesamtblatt 14 von 44, Nullstellen 33 von 61;
  Wortstamm-Heuristik, aber deutlich).
- Sek II: 22 Einheiten „nur LK"; Berlin und Brandenburg legen
  Einheiten in verschiedene Halbjahre (Binomialverteilung Q4
  gegen Q2) – die Sek-II-Zeitachse braucht das Land.
- Bigalke/Köhler führt fast alle Stochastik in Band 11.
- Kein Katalog-Merkkasten hat fette Begriffe; das Prüfskript
  nimmt Begriffe vor Doppelpunkt.
- Prüfskript kennt als Merkkasten nur \uebersichtskasten und
  findet keinen; der Befund vom 24.09. sah oben einen Kasten –
  Lesart klären.
- Nicht frei: Quali Mittelschule Bayern, Kompetenztests Sachsen.

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Die Marke im Katalog ist die Klasse je Schulform aus den
  Lehrwerken, so fein wie das Verzeichnis (Typ oder Einheit),
  nicht der RLP-Buchstabe (25.09.; Grund: Buchstabe G an
  „Gleichung aus zwei Punkten" hätte Kl. 8 Oberschule falsch
  geschnitten, Sekundo 8 S. 128 lehrt es).
- Klasse und Schulform filtern nicht; sie ordnen (Zeitachse).
  Einzige feste Grenze: unter Klasse 11 keine Sek-II-Einheit.
- Zweigzeile: Fertigkeit · Zeitmarke · Prüfungswort. Zeitmarke
  relativ zur Eingabeklasse („kennst du wahrscheinlich seit
  Klasse 7", „neu in diesem Jahr", „kommt nächstes Jahr", „am
  Gymnasium schon jetzt"), ohne Klasse absolut („ab Kl. 7").
- Prüfungswort (26.09.): Schwelle 7 von 13 P10-Jahrgängen,
  Zählung „Haupt oder Neben"; Wörter „P10 oft", „P10", „keine
  P10-Aufgabe"; gilt für beide Prompts; im Prüfungsheft bleibt
  „selten" daneben, Schwelle dafür beim Umbau des
  Prüfungsprompts. Sek II: „Abitur GK", „Abitur LK", „FHR".
  Ergibt 44 / 47 / 23 Sek-I-Einheiten.
- Hauptnummern-Titel als Fertigkeit in Schülersprache („Ich kann
  …"); bei gemischten Aufgaben ist die Fertigkeit das
  Unterscheiden.
- „schwach" ändert die Form (Förderheft-Form, ziel.md § 2),
  nicht den Stoff; das Blatt darf länger werden.
- Bestellung: „nur das Neue / mit Wiederholung / mit Ausblick";
  ohne Angabe mit Wiederholung, und mit Ausblick nur beim ersten
  Bau eines Themas (Annahme, kippbar).
- Bigalke/Köhler ist Reihenfolge-Quelle, keine Form-Quelle.
- Reihenfolge der Bauphase: v4.3 → Prüfskript (liegt schon) →
  wiederkehrender Nachtauftrag „auftrag-testlauf" mit fester
  Eingabeliste, der bei jeder Prompt-Version dieselben Blätter
  baut (Claude Code, MiKTeX lokal).
- Kaufen nur zwei Förderhefte (Sekundo 8 BE/BB 978-3-14-124264-5,
  Schnittpunkt 8 diff. 978-3-12-744588-6); keine Schulbücher.
- Fremde Aufgabensammlungen nur für die 22 Sprossen ohne
  P10-Original auswerten (15 davon Prüfungshöhen).
- Nachtaufträge: Skripte samt Daten ins Repo, nichts im
  Scratchpad; Dateien mit WriteAllText ohne BOM; Commit-
  Nachrichten mit Umlaut über -F.
- Bonusguthaben 250 $ für Cloud-Sitzungen (Claude Code im Web):
  cloudfähig sind Aufträge, die nur Repo und Netz brauchen
  (Verzeichnisse, Belege); nicht cloudfähig: hefte/, MiKTeX.

## 5 Offene Punkte und verworfene Ansätze

Offen:
- 38 Ermessensfälle (Sorten „Katalog verortet anders", „Frühe
  Stelle als Grundstufe") entscheiden; die übrigen 212 gelten
  als Vorschlag übernommen.
- Format der Marken im Eintrag festlegen (je Lerneinheit: OS-
  Klasse, GYM-Klasse, Prüfungswort; Sek II: Halbjahr BE/BB,
  Kursart) und per Auftrag mechanisch eintragen.
- v4.3: Abschnitt 0–2 umbauen (Zeitachse, Zone, Bestellung,
  Zweigzeile, Ich-kann-Titel, schwach als Form); Vorschlag:
  „Stichwort in zwei Einträgen: begleitendes Wort entscheidet,
  sonst Rückfrage" (nullstellen 22.09. holte beide Einträge).
- Prüfskript: Lesart Merkkasten prüfen; „Typen ohne Treffer"
  an einem Blatt von Hand gegenlesen, um die Fehlerquote der
  Heuristik zu kennen.
- Befunde in Einträgen (Nacht 26.09.): flaechen.md Original-ids
  zu „Term zu Figur angeben" vertauscht; zuordnungen.md und
  terme.md kennen neuere GYM-Typen nicht; themen.csv führt den
  Maßstab bei zuordnungen statt strahlensaetze; 2025-GYM-K5d
  Nebentyp-Etikett prüfen.
- ziel.md § 5: „22 Prüfungshöhen" → „22 Sprossen, 15 davon
  Prüfungshöhen" (erledigt der Umzugsauftrag).
- Fundamente B Qualifikationsphase liegt nicht im Repo.
- In etwa zwei Wochen: Fotos der Inhaltsverzeichnisse aus den
  Büchern der Schüler, dazu zwei Aufgabenseiten eines Themas;
  im Chat lesen, je Buch eine Zeile eintragen.
- Förderhefte, wenn gekauft: Prüfstein-Befund daneben legen.
- Prüfungsheft: Schwelle „selten" beim Umbau setzen.

Verworfen:
- RLP-Niveaustufe (D–H) als Filtermarke: schneidet falsch,
  weil die Lehrwerke früher lehren als der Plan stuft
  (_niveaustufen-belege.md bleibt als Beleg liegen).
- Klasse und Schulform als Filter überhaupt: widerspricht „ein
  Blatt für alle"; ersetzt durch Zeitachse.
- Bildschirm mit drei Leiterstellungen (unten/oben/ganz):
  aufgegangen in der Bestellung „neu / mit Wiederholung / mit
  Ausblick".
- Sprossen bundesweit aus Lehrplänen recherchieren: Pläne sind
  keine Aufgaben; stattdessen freie Testaufgaben (gesichert).
- Lineare Funktionen als Prüfstein für Spanne: keine Spanne
  (alle Reihen Kl. 8).

## 6 Nächster Arbeitsschritt

Modell: Fable (Urteil mit Folgen).

1. katalog/_klassen-ermessen.md öffnen, die 38 Fälle der zwei
   Sorten im Chat entscheiden, Ergebnis als Liste (Eintrag,
   Einheit, Entscheidung, Grund).
2. Format der Markenzeilen im Eintrag festlegen; Auftrag
   (Sonnet, Mechanik) schreiben, der aus den drei Belegdateien
   und der Entscheidungsliste die Zeilen in alle Einträge
   einträgt, mit Gegenprobe (lineare-funktionen Einheit 4: OS 8,
   GYM 8, P10 oft; quadratische-gleichungen Einheit 2: OS 10,
   GYM 9; prozentrechnung Einheit 1: GYM 5).
3. Danach v4.3 (Fable), Prüfstein „quadratische gleichungen 9
   oberschule" und „9 gymnasium" sowie „prozentrechnung 7
   schwach" im Blatt-Chat, dann Prüfskript darüber.
