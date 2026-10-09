# Plan – Blätter aus Katalog und Bank

Stand 09.10.2026, vom Lehrer beschlossen („plan gilt“). Entstanden aus dem
Prüfstand 09.10. (pruefstand-2026-10-09/: vier Leserberichte, Gegenlese).
Ersetzt archiv/plan-2026-10-08.md, ziel.md § 1–4 und faellig.md.

## 0 Wie dieser Plan gilt

- Er ist die einzige Stelle für Ziel, Linien und den nächsten Schritt
  (§ 7 „Jetzt“). Übergaben verweisen hierher und nennen keinen eigenen
  Schritt.
- Ändern darf ihn nur der Lehrer, mit Eintrag in § 10.
- Vorrang bei Widerspruch: plan.md → aufgabenbank bau/bauregeln.md
  (Handwerk) → aufgabenbank bau/bauauftrag.md (Didaktik des Baus) →
  aufgabenbank bank.md (Zeilenform) → begriffe.md (Wörter). Alles andere
  ist Beleg oder Archiv.

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

## 3 Linien (gelten bis zum Ende von M3)

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
4. Sorten aus demselben Bestand: Lernblatt = Lernweg einer Lerneinheit,
   Originale nur, wo sie die beste Aufgabe sind. Prüfungsblatt = die Stufen
   der Prüfungsgliederung in Katalogfolge, je Stufe die passenden Schritte
   (Feld schritt), am Ende ein echtes Original ganz. Fokus = ein Schritt.
   Prüfungsheft = die Prüfungsblätter eines Kapitels. Original und Original
   neu bleiben bei pruefheft.py. Den Wortlaut der Originale liest der Setzer
   aus aufgabenbank-privat.
5. Eine Datei je Frage: Ziel und Plan in plan.md; Handwerk in
   bauregeln.md; Didaktik im Bauauftrag (bau/bauauftrag.md); Wörter in
   begriffe.md; Zeilenform in bank.md. Regeln werden mit Namen zitiert,
   nicht mit Nummern.
6. Der Lehrer urteilt an Stichproben (etwa jede zehnte Einheit) und am
   Prüfstein; Kritiker und Prüfskripte prüfen jede. Das ersetzt die Pflicht
   vom 01.10., dass der Lehrer Vollständigkeit und Reihenfolge je Eintrag
   vorher bestätigt.
7. Jeder Lauf: Schätzung vorher, Ablesen nachher; Zeit je Einheit wird
   gemessen.
8. Gegen das Kreisdrehen: Der nächste Schritt steht nur in plan.md (§ 7,
   Meilenstein und Abnahmestand); die Übergabe nennt keinen eigenen.
   Befunde aus Blättern gehen in eine Befundliste je Meilenstein
   (befunde-M<n>.md); bauauftrag.md und bauregeln.md ändern sich nur am Ende
   eines Meilensteins, gesammelt. Ausnahme: Handwerksfehler (falsche Zahl,
   Satzfehler) sofort. Nebenfragen kommen in § 9 „Später“, nicht in eine
   Regel.

## 4 Was sich an Bank und Katalog ändert

- Katalog, je Lerneinheit neues Feld **Lernweg**: Schritt · was der Schüler
  begreift · Stolperstelle · Bank-ids (2–3 gleichwertige je Schritt für
  „neue Zahlen“).
- Bank, je Zeile neue Felder (in M1 nur in bank.md definiert; gefüllt wird
  je gebauter Einheit, nicht global): **schritt** (Lernweg-Schritt, neben sprosse),
  **sache**, **darstellung** (skizze-fertig / bild / karte / text / tabelle /
  graph / term; Werte in bank.md), **frage** (Länge, Unterschied, Entscheidung,
  Begründung …), **antwortform** (rechnen, ankreuzen, zuordnen, begründen),
  **status** (gut / schwach mit Grund und besserer id / ruht). Gelöscht wird
  nichts; schwach und ruht werden nicht gesetzt.
- Prüfkennung „(P10 2023 OS)“ wandert aus dem Aufgabentext ins Feld (2 523
  Zeilen, Skript).
- bank-pruef.py: Altlasten (≈ 160 Meldungen je Eintrag) einmal bereinigen,
  damit „0 Abweichungen“ wieder prüfbar ist; duplikate.py hineinnehmen.

## 5 Werkzeuge

- **Setzer** (neu, klein): liest Lernweg + Bankzeilen, schreibt LaTeX mit
  mathblatt.sty, drei PDFs (Übersicht nach bauregeln „Übersicht und
  Serie“). Ziel: unter 30 s. Die Kennung eines Blatts steht im Register mit
  der Liste der gesetzten Bank-ids; damit setzt er ein Blatt wieder und
  bedient „hängt bei Nr.“, ohne dass ein Blatt abgelegt wird. Graphen und
  Aufgabenbilder (Feld bild, heute leer) braucht er erst vor M5.
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
  Lernweg Bauauftrag; Schülerliste bleibt privat. Die alten Prompts
  unterrichtsblatt.md und pruefungsblatt.md bleiben als Steinbruch liegen
  und werden nach M3 archiviert.

## 6 Aufräumen (M1: die ersten drei Punkte; der Rest nach M2)

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

M0 Prüfstein K4W „Hypotenuse berechnen“: Lehrer 09.10. „besser“ als
   Durchgang 1 – erfüllt; die Linie trägt so weit.
M1 Grundlagen, klein – plan.md, CLAUDE.md/README-Einstieg, bauauftrag.md,
   Felder in bank.md definiert, Lernweg-Feld im Katalog definiert.
   Abnahme: ein frischer Agent findet über CLAUDE.md alles Nötige.
M2 Prüfstein Bau – „Kathete berechnen“ nach Bauauftrag gebaut, zerlegt
   zurückgelegt, mit einem Setzer-Rohling gesetzt; K4W nachträglich in
   dieselbe Form gebracht. Gemessen: Bauzeit, Token, Setzzeit. Abnahme:
   Kritiker ohne schweren Befund, Lehrer „gut“, Setzen ≤ 3 min. Gelingt es
   nicht: Umbau beenden, Blätter auf Bestellung frei bauen wie das
   Geradenheft. Danach: Rest von § 6, Prüfkennung ins Feld, bank-pruef
   bereinigen.
M3 P10 – Reihenfolge: Einheiten mit „P10 oft“ (45), dann Kern mit P10 (54
   zusammen), dann der Rest; Runden zu etwa zehn, Agenten parallel,
   Ablesen zwischen den Runden; erste Runde ein Kapitel, Lehrer sieht eine
   Einheit. Abnahme: jede Einheit hat Lernweg, Prüfskripte ohne Meldung,
   Stichproben gut.
M4 Bestellung – bankblatt.md kurz, ruft Setzer. Abnahme: drei echte
   Bestellungen ≤ 3 min (für Einheiten mit Lernweg).
M5 Abitur GK – Setzer mit Graphen; dann wie M3, so weit das Kontingent
   reicht.

Jetzt: M3 Runde 1 (M2 erfüllt 09.10.: Bau T6B 41 min, 0,23 Mio Token +
Kritiker, Lehrer „insgesamt gut“; setzer.py setzt T6B in 3,7 s). Runde 1:
zwei Agenten nach bau/bauauftrag.md – Pythagoras ganz (Hypotenuse neu,
Umkehrung, Das Dreieck erst finden, Thema-Weg) und Prozentrechnung;
Schätzung 2–3 Mio Token; Ablesen vorher und nachher; Lehrer sieht eine
Stichprobe. In der ersten Setzerrunde: Originalliste auf Lernblättern weg,
Feld satz gegen aufgabe/loesung bereinigen. Token sparen vom Ende her
(uebergabe.md § 4).

## 8 Modelle und Kosten

Bau-Agenten Opus; Kritiker und Leser Fable (Fable-Kontingent nutzen).
Messwert: enge Agenten ≈ 0,5–0,7 Mio Token je Wochenpunkt. Bau einer
Einheit geschätzt 0,3–1,5 Mio Token (Geradenheft 0,6 Mio ohne Bank-Lesen)
→ die 54 P10-Kerneinheiten ≈ 0,3–1,6 Wochen Kontingent. M2 misst den Wert;
M3 wird danach budgetiert.

## 9 Später

Folgebaum der Kennung · Durchgänge · Einstieg unten/oben · Serie mit
Wiederkehr · Musterbeispiel · Boden unter Klasse 8 · FHR, LK · mündliche
Prüfung.
Zu M4: Bestelloptionen (Wiederholung, Ausblick) und Prüfungsprofile aus
archiv/ziel-2026-10-09.md § 3–4 übernehmen.

## 10 Änderungen

- 09.10.2026: Plan neu aus dem Prüfstand; Linie „Lernweg führt, Bank
  liefert“, Setzer ohne Modell, Mechanik gegen Kreisdrehen (Linie 8),
  Meilensteine M0–M5. Ersetzt Plan vom 08.10. (große Linien 1, 3, 8, W1–W4,
  M1–M6) und die Pflicht vom 01.10. „Lehrer bestätigt Vollständigkeit je
  Eintrag vorher“. Messwert Prüfstand: fünf Fable-Leser + Kritiker ≈ 1,4 Mio
  Token → Woche 37 → 41 %, Fable 12 → 18 %.
- 09.10.2026 (b): Selbstlernheft als mögliche Sorte (Bauregeln 2.6, Wahl
  offen); Bau legt je Schritt Formel, Beispiel, leichtere und gleichwertige
  Aufgaben an; Thema-Weg je Thema; „Für wen du baust“ im Bauauftrag (Lehrer
  09.10.). Messwert M2: Kathete-Bau + Setzer ≈ 0,4 Mio Token → Woche 41 →
  42 %, Fable 18 → 18 %.
