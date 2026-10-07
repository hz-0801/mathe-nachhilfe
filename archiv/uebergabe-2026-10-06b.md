# Übergabe verbessereBlaetter – 2026-10-06b (Chat 06.10., Opus)

Vorherige Übergabe: archiv/uebergabe-2026-10-06.md.

## 1 Ziel

Am Stundenanfang in wenigen Minuten ein gutes Blatt – Prüfungsmaterial
(P10, Abitur GK) oder allgemeines Blatt. Weg: Daten je Teilaufgabe und je
Handgriff vollständig, ein Bauprogramm setzt auf Bestellung. Jetzt: Plan
„P10 fertig“ (faellig.md § 0).

## 2 Arbeitsgrundlage

- Beschlüsse: aufgabenbank `bau/pruefheft/beschluesse-2026-10-06.md`
  (Punkte 1–29) und `beschluesse-2026-10-06b.md` (N1–N6, Punkt 30) –
  maßgeblich, bei Widerspruch gilt 06b.
- Steckbriefe (neu): mathe-nachhilfe `katalog/steckbrief/prozent-grundwert.md`,
  `pythagoras-seite.md` – Teil 1 Verständnis (aus `katalog/<eintrag>.md`:
  Erkennungsschritte, Merkkasten, Typische Fehler, Leiter), Teil 2 Raster,
  Teil 3 Formulierungen (kurz/lang), aus den echten Aufgaben.
- Bauprogramm: aufgabenbank `werkzeuge/pruefheft.py` v0.3+ (N1–N5),
  `werkzeuge/abbildung.py`, Anleitung `pruefheft.md`, Standdatei
  `bau/pruefheft/stand-2026-10-06.md`; Vorlage blattbau `mathblatt.sty`
  2026-10-06c; Hefte unter `bau/pruefheft/*-2026-10-06/`.
- Daten P10 (mathe-nachhilfe `msa/`): `wortlaut-eigen-<kapitel>.csv` (alle
  zehn Kapitel), `handgriffe-p10.csv`, `herausgeloest-p10.csv` (140),
  `rueckblick-p10.csv`, `erkennen-p10.csv`, `zuordnung-*.csv` (Spalten
  jahre_letzte5, nebenplaetze, verwechselbar), `fremd/<gruppe>.csv`
  (1 502 ganz, 206 herausgelöst) und `fremd/*-erkennen.csv` (374).
- Bank: Feld `"ruht": "kopie von <id>"` (15 Zeilen), Vielfalt-Messung
  `werkzeuge/vielfalt.py`, `bau/vielfalt-p10-2026-10-06.md`.
- Regeln: `ziel.md`, `bank.md`, `bau/layout-befunde.md` Stand N1–N4;
  `bankblatt.md` v5.7 im Repo (nicht im Betrieb).

## 3 Arbeitsstand

Erledigt 06.10.: Nachzug 05./06.10.; eigener Wortlaut aller P10-Kapitel;
exakt vor ≈ im Katalog; Abbildungen aus Daten; alle P10-Hefte und Probeheft
Abitur Kurvenuntersuchung gebaut; Lauf „P10 in einem Rutsch“ (Handgriffe,
Herauslösen, Rückblick-/Erkennen-Daten, sieben Fremdgruppen, Bank-Vielfalt);
Endbau mit N5 (Prozent 15 S., Dreiecke 42, Flächen 13, Körper 14, Lineare
16, Quadratische 16, GLS 4, Wachstum 9, Daten 18, Wahrscheinlichkeit 16;
Fokus Grundwert 2 S.); Steckbrief-Entwürfe Grundwert und Pythagoras.

Nicht nachgezogen: N5, N6 und Punkt 30 stehen nur in beschluesse-06b,
noch nicht in ziel.md, bankblatt.md und im Bauprogramm (N6, Punkt 30).
Das Bauprogramm liest weder Katalog-Einträge noch Steckbriefe.

Messwerte: Lauf 06.10. (zehn Agenten ≈ 3,5 Mio Token) → Woche 9 → 16 %;
Neubau N5 0,17 Mio. Bestätigt ≈ 0,5 Mio Token je Wochenpunkt (Opus).

## 4 Verbindliche Entscheidungen und Rahmenbedingungen

- Alles in beschluesse-06/06b; Kern von heute: echte Aufgaben zuerst
  (BB/BE → andere Länder, nie schwerer als BB/BE → eigene nur für Lücken,
  Raster ≥ 2 Merkmale); Herauslösen („nach P10 ’15“); Fokusblatt mit allen
  Originalen; Zählung B; Auffüllen B (Zielzahl nur Vorrat); Punkte nur
  Prüfstein; Anhang „Mehr zum Üben“ bei kurzem Kernteil; Erkennen nicht im
  Fokus; Rückblick vereinheitlicht (Name „Rückblick“, Regel Punkt 29,
  Behalten in „Zum Schluss“, Verständnis als erste Sprosse); Grundwert-
  Leiter nach Katalog (glatte Sätze vor 1 %); Fundstelle nur Jahr;
  Bezeichnungen N4.18; Prüfstein mit Fuß.
- Einrücken statt Rahmen für gleichartige BB/BE-Originale (Plan 2).
- Steckbrief je Handgriff, gemeinsam für alle Blattarten, drei Teile.
- global.md Stand 2026-10-06: sparsamster gleich guter Weg ungefragt.

## 5 Offene Punkte und Verworfenes

- Offen: Anhang-Untergrenze 2 oder 4; Steckbrief maschinenlesbar machen
  (feste Schlüssel je Teil) – im nächsten Lauf entscheiden und begründen;
  Erkennen-Sätze teils falsch etikettiert (Steckbrief Grundwert § 4);
  182 aktive Bank-Kopien; 107 fremde Prozent-Aufgaben ohne zeichenbare
  Abbildung; Abitur ohne neue Daten; Bauskripte der K- und F-Agenten nur im
  Scratchpad (CSV ist Quelle); bankblatt v5.7 an den Lehrer erst nach N5/N6.
- Verworfen: Zielzahl 12/6 als Blattlänge; Erkennen-Aufgabe im Fokusblatt;
  Punkte an allen Aufgaben; Rahmen um Dubletten (→ Einrücken); Streifen als
  Schmuck neben einer Tabelle; „0,1 · 70“-artige Lückenfüller im Rückblick.

## 6 Nächster Arbeitsschritt

Plan § 0 Schritt 1+2 als ein Lauf (frischer Opus-Agent, liest nur die
betroffenen Stellen): Bauprogramm liest die zwei Steckbriefe (Format dafür
festlegen), setzt N6/Punkt 29–30 und die Satzänderungen aus Schritt 2 um,
zieht N5/N6/30 in ziel.md und bankblatt.md nach, baut Fokus Grundwert und
Fokus Pythagoras. Danach zeigt der Chat dem Lehrer beide Blätter (rendern,
rechts). Vorher die Anhang-Untergrenze fragen. Modell: Opus im Chat und für
Agenten.
