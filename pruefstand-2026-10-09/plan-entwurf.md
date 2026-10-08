# Plan – Entwurf aus dem Prüfstand 09.10.2026

Grundlage: r1-september.md, r2-oktober.md, r3-regeln.md, r4-werkzeuge.md
(dieser Ordner). Gilt erst nach Zustimmung des Lehrers; dann ersetzt er
plan.md, ziel.md § 1–4 und faellig.md.

## 1 Ziel

Der Lehrer bestellt mit wenigen Wörtern ein Lernblatt oder ein
Prüfungsblatt (mit echten Prüfungsaufgaben) und bekommt in höchstens
3 Minuten drei PDFs (Übersicht, Blatt, Lösungen), die ein guter Didaktiker
so bauen würde – zuerst alle P10-Themen, dann Abitur Grundkurs. Aufgebaut
wird mit dem großen Abo; danach soll es mit einem Skript oder einem kleinen
Abo laufen.

## 2 Befund in fünf Sätzen

1. Wir drehen uns, weil Entscheidungen in Schichten liegen (15 Übergaben in
   8 Tagen, der nächste Schritt wechselte 13-mal, fünf Dateien beanspruchen
   Vorrang, Regelnummern zweimal neu) und nie aufgeräumt wurde.
2. Schnell (Programm aus der Bank, 58 s) war nicht gut; gut (freier Bau mit
   Lernweg, Geradenheft) war nicht schnell (21 min, 0,6 Mio Token).
3. Die Bank ist reich (16 743 Zeilen, Originale, Fehlerquellen, geprüfte
   Lösungen), aber ihre Ketten tragen keinen Lernweg und ihre Aufgaben keine
   Formmerkmale; darum ergibt Auswahl von unten gleichförmige Blätter.
4. Im Unterricht lief nur der Bank-Prompt (sechs Blätter, 01.–06.10.); jedes
   Blatt baute eigene Satzmakros nach, 40 % der Erfindungen waren Dubletten.
5. Die Werkstatt selbst ist zu schwer: 83 Skripte (68 000 Zeilen, 27 einmalig),
   eine Projektanweisung von 3 100 Wörtern, davon 1 100 über tote Wege.

## 3 Linien (gelten bis zum Ende von M3, ändern nur aus einem Messwert)

1. Drei gepflegte Objekte, sonst nichts: **Katalog** (je Lerneinheit der
   Lernweg), **Bank** (Aufgaben), **Prüfungsgliederung** (Originale,
   Häufigkeit). Alles andere ist Werkzeug, Beleg oder Archiv.
2. **Der Lernweg führt, die Bank liefert.** Je Lerneinheit wird einmal
   gebaut: Lernweg in 5–7 Schritten, je Schritt die beste Aufgabe aus der
   Bank oder neu geschrieben, Kritiker ohne Regeln, Prüfskripte. Das
   Ergebnis wird zerlegt zurückgelegt (Lernweg ins Katalogfeld, Aufgaben als
   Bankzeilen); kein ganzes Blatt wird abgelegt.
3. **Die Bestellung setzt** aus Lernweg und Bankzeilen; ein Setzer ohne
   Modell macht daraus die drei PDFs. Fehlt der Lernweg, wird die Einheit
   erst gebaut (Ausnahme, ~20 min) und dann gesetzt.
4. Prüfungsblatt: der Lernweg endet mit einem echten Original, ganz.
   Lernblatt: Originale nur, wo sie die beste Aufgabe sind.
5. Eine Datei je Frage: Ziel und Plan in plan.md; Handwerk in
   bauregeln.md; Didaktik im Bauauftrag (bau/bauauftrag.md); Wörter in
   begriffe.md; Zeilenform in bank.md. Regeln werden mit Namen zitiert,
   nicht mit Nummern.
6. Der Lehrer urteilt an Stichproben (etwa jede zehnte Einheit) und am
   Prüfstein; Kritiker und Prüfskripte prüfen jede.
7. Jeder Lauf: Schätzung vorher, Ablesen nachher; Zeit je Einheit wird
   gemessen.

## 4 Was sich an Bank und Katalog ändert

- Katalog, je Lerneinheit neues Feld **Lernweg**: Schritt · was der Schüler
  begreift · Stolperstelle · Bank-ids (2–3 gleichwertige je Schritt für
  „neue Zahlen“).
- Bank, je Zeile neue Felder: **schritt** (Lernweg-Schritt, neben sprosse),
  **sache**, **darstellung** (Skizze mit Dreieck / Bild ohne / Karte / nur
  Text / Tabelle / Graph), **frage** (Länge, Unterschied, Entscheidung,
  Begründung …), **antwortform** (rechnen, ankreuzen, zuordnen, begründen),
  **status** (gut / schwach mit Grund und besserer id / ruht). Gelöscht wird
  nichts; schwach und ruht werden nicht gesetzt.
- Prüfkennung „(P10 2023 OS)“ wandert aus dem Aufgabentext ins Feld (2 523
  Zeilen, Skript).
- bank-pruef.py: Altlasten (≈ 160 Meldungen je Eintrag) einmal bereinigen,
  damit „0 Abweichungen“ wieder prüfbar ist; duplikate.py hineinnehmen.

## 5 Werkzeuge

- **Setzer** (neu, klein): liest Lernweg + Bankzeilen, schreibt LaTeX mit
  mathblatt.sty, drei PDFs. Ziel: unter 30 s.
- **mathblatt.sty**: die Formen aufnehmen, die die Blatt-Chats selbst
  nachbauten (Rechenkaro, Kreuzzeile, zweispaltig Skizze/Rechnung, graues
  a), Antwortfeld).
- **Bauauftrag** (bau/bauauftrag.md): Zweck, Lernweg zuerst, die Prinzipien
  aus den alten Prompts (ein Merkmal je Stufe, rückwärts von der Decke,
  jede Nummer beim einfachsten Fall, verfremdetes Original behält die Falle,
  Runden zuletzt, Sache trägt die Mathematik, nie zwei Sachaufgaben mit
  demselben Modell, Antwortform wechseln), Kritiker zählt Sachen und
  Darstellungen über die Einheit, Ausgaben (Katalogfeld, Bankzeilen, Beleg).
- **pruefheft.py** bleibt für Original und Original neu; zusammenbau.py,
  regal.py, Testlauf-Kette, einmalig/ und gelaufene Katalogskripte ins
  Archiv (Liste r4 § 3.6).
- **bankblatt.md** wird kurz: Bestellung deuten → Setzer → bei fehlendem
  Lernweg Bauauftrag. Die alten Prompts unterrichtsblatt.md und
  pruefungsblatt.md werden archiviert (Steinbruch bleibt im Archiv).

## 6 Aufräumen (vor M2, ein Gang)

- plan.md neu (dieser Entwurf); ziel.md § 1–4 geht darin auf, Rest
  archiviert; faellig.md archiviert, Gültiges als Zeile in § 7.
- blatt-konzept.md, layout-befunde.md, bauregeln-streichliste.md,
  Beschluss-Stubs, weg-vorschlag.md, uebersicht-vorschlag.md,
  merkzettel-abend.md, Testlauf-Ordner → archiv; konzept.md auf die
  Erfassung zurückgeschnitten.
- Verweise auf Regelnummern in bank.md, bankblatt.md, pruefheft.py auf
  Namen umstellen; Blattregeln aus bank.md nach bauregeln.md oder gestrichen.
- begriffe.md als einzige Wortliste (Kette, Sprosse, Lernweg, Schritt,
  Lerneinheit; „Einstieg unten“ = „schwach“).
- CLAUDE.md und README-Einstieg zeigen auf fünf Dateien: plan.md,
  bauregeln.md, bau/bauauftrag.md, begriffe.md, bank.md.
- Projektanweisung auf Rolle, Chatstart (plan.md, uebergabe.md), Umgang,
  Modell, Umzug kürzen; Rechner- und Code-Tab-Wege nach anweisungen/wege.md.

## 7 Meilensteine

M1 Aufräumen und Grundlagen – § 6, Bankfelder (§ 4), Setzer v1, Vorlage,
   Bauauftrag. Abnahme: Setzer setzt K4W aus Lernweg + Bankzeilen in unter
   30 s; ein neuer Agent findet über CLAUDE.md alle Grundlagen.
M2 Prüfstein – Lerneinheit „Kathete berechnen“ nach Bauauftrag gebaut und
   gesetzt. Gemessen: Bauzeit, Token, Setzzeit. Abnahme: Kritiker ohne
   schweren Befund, Lehrer „gut“, Setzen ≤ 3 min. Gelingt es nicht: Umbau
   beenden, Blätter auf Bestellung frei bauen wie das Geradenheft.
M3 P10 – alle P10-Lerneinheiten (119 mit P10-Bezug) in Runden zu etwa zehn,
   mehrere Agenten parallel, Ablesen zwischen den Runden; erste Runde ein
   Kapitel, Lehrer sieht eine Einheit. Abnahme: jede Einheit hat Lernweg,
   Prüfskripte ohne Meldung, Stichproben gut.
M4 Bestellung – bankblatt.md kurz, ruft Setzer. Abnahme: drei echte
   Bestellungen im Unterricht ≤ 3 min.
M5 Abitur GK – wie M3, so weit das Kontingent reicht.

## 8 Modelle und Kosten

Bau-Agenten Opus; Kritiker Fable (Fable-Kontingent nutzen). Messwert
09.10.: enge Agenten ≈ 0,5–0,7 Mio Token je Wochenpunkt; Bau einer Einheit
nach Geradenheft ≈ 0,6 Mio Token → P10 ≈ 1–1,5 Wochen Kontingent
(Schätzung, M2 misst sie).
