# Übergabe verbessereBlaetter – 2026-09-28 (Chat vom 27./28.09.)

Vorherige Übergabe: archiv/uebergabe-2026-09-27.md.

## 1 Ziel

Der bestmögliche Themenkatalog, die Aufgabenbank und die Prompts,
damit aus wenigen Wörtern druckfertige Blätter entstehen – für den
Unterricht und für MSA/P10 und Abitur GK. Maßstab ist ziel.md
(Stand 25.09.) mit den Beschlüssen vom 28.09. (§ 4), die dort
noch nicht nachgezogen sind. Leitbild bleibt: **ein Blatt für
alle Schüler** (Leiter je Fertigkeit, der Schüler steigt, so hoch
er kommt; der Lehrer streicht am Tisch) – jetzt kleiner
geschnitten und aus der Bank zusammengesetzt statt im Chat
erzeugt. Die Prompts müssen auch ohne Abo nutzbar bleiben.

## 2 Arbeitsgrundlage

- mathe-nachhilfe: ziel.md (25.09.), katalog/ (mit
  _ichkann.csv, _kuerzel.csv, _fremd-konkordanz-*.md),
  quellen/altlehrwerke-formen.md, -pflichtformen.md,
  -formen-sek2.md (DDR-Bände, ausgewertet, **nicht eingebunden**),
  quellen/blattarten-literatur.md und
  quellen/nachhilfe-situationen.md (Literatur, 28.09.),
  quellen/register-fundliste.md (Suche lief 28.09. 18:16).
- aufgabenbank: 72 Einträge und bank/_basis/ (410 Zeilen);
  bank.md Stand 27b; werkzeuge/bank-pruef.py v0.6,
  zusammenbau.py v0.8; bau/layout-befunde.md (Befunde 1–54,
  maßgeblich für jedes Layout); bau/sprachlauf/regeln.md
  (Sprachregeln); bank/_strittig.md (1 123 Zeilen, ungesichtet);
  bank/_punkte.csv.
- blattbau: unterrichtsblatt.md v4.4, pruefungsblatt.md,
  mathblatt.sty; Testlauf v4.4 (blaetter/testlauf-2026-09-26/),
  Bericht ungelesen.
- Muster „schwach“: zwei von Hand gebaute Blätter Terme plus,
  minus, mal, geteilt (TER-S1, TER-S2, je 5 Seiten + Lösungen)
  liegen nur im Chat als PDF, nicht im Repo.

## 3 Arbeitsstand

Abgeschlossen 27./28.09.:
- Bank Sek I und Sek II vollständig (72 Einträge, rund 13 500
  Zeilen); Zweitleser blind für 72 Einträge (gegenlese2.md);
  Bank-Korrektur nach Doppelbefund 28.09. 12:44, strittige Zeilen
  in bank/_strittig.md.
- Renderlauf aller Einträge, 144 Bankzeilen behoben.
- Sprachlauf über alle 29 MSA-Einträge: 6 536 von 7 728
  Aufgabentexten in ganze, einfache Sätze mit Bezug umgeschrieben;
  Gegenprobe im Chat: Lösungen, Schritte, Merkmale unverändert;
  146 Texte mit geänderter Zahlenfolge geprüft (Aufgabe wird vor
  der fremden Rechnung genannt – kein Fehler). Sek II nicht.
- zusammenbau v0.8 mit Rezept K (Durchgang: je Schritt eine
  Aufgabe, Prüfungshöhen) und Layoutbefunden 37/40/49/52/53;
  fünf Durchgänge gebaut (LIN, QGL, PRZ, POT, TRI; PRZ-K1 nach
  Sprachlauf neu).
- Lehrer hat LIN-K1, QGL-K1, PRZ-K1 gelesen: Befunde 35–54.
- Literatur: Blattarten/Übungsformen, Nachhilfe-Situationen.

Nicht erledigt: Urteilsliste 28.09. (Auftrag lieferte keine
Datei); Testlauf-Bericht v4.4; ziel.md-Nachzug; Prompts.

## 4 Verbindliche Entscheidungen (neu 28.09.)

Aus früheren Übergaben gelten weiter (siehe archiv/).

- **Ein Blatt für alle bleibt.** Kein Dialog über die Lage des
  Schülers; der Dialog fragt nach dem **Teil des Themas**
  (Planfrage 1.3). Ein Blatt ist so lang wie nötig, aber nie
  30 Seiten: ein Teil = 1–3 Fertigkeiten.
- **Blattarten:** Lernblatt, Fokus, Prüfungsheft; Schalter
  „schwach“ (Form, nicht Stoff). Namen bleiben. Das
  „Kompetenzblatt“ ist keine Blattart, sondern Durchgang/Baustein
  (gut als Überblick, nicht zum Einüben). Einteilung wird mit
  der Literatur weiter geschärft (§ 5).
- **Stern entfällt;** Niveau wird bestellt (FOR zuerst, EBR
  später). **Punkte** nur im Prüfungsheft, dort immer. Je
  Original höchstens eine Aufgabe; Prüfungshöhen aus den
  jüngsten fünf Jahrgängen.
- **Sprache:** ganze, kurze Sätze; erst die Lage, dann eine
  Aufforderung; die Frage nennt ihren Bezug; keine Begriffe, die
  das Blatt nicht einführt; Division als Bruchstrich;
  Endergebnis als Lösungsmenge; „Zutatenzeile“ (Größen vor der
  Formel notieren: p, q; m, n; G, W, p %).
- **Merkkasten** (Befund 54, Umsetzung zurückgestellt): wie eine
  Formelsammlung – Formel und Voraussetzung, dazu ein bis zwei
  häufige Fehler, keine erklärenden Sätze.
- **Altlehrwerke** sind Steinbruch für Katalog, Bank und Prompt
  (Sprossen, Reihenfolge, Aufgaben, Sprache), **keine neue
  Blattart**. Dichte nicht übernehmen (Literatur: mehr gleiche
  Aufgaben am Stück bringt kaum etwas; öfter, verteilt, gemischt
  wirkt).
- Taschenrechner: Zeichen nur, wo verboten oder nötig; ohne TR
  kopfrechenbare Zahlen.

## 5 Offene Punkte

Zu entscheiden (Lehrer):
- Musterbeispiel: bei „schwach“ Standard, obwohl v4.4 es
  abgeschafft hat? (Literatur: Musterbeispiel mit Ausblenden hilft
  Anfängern und Schwachen; TER-S1/S2 sind so gebaut.)
- Vorschlag Speicherform: Bank speichert Aufgaben und Bausteine
  (Musterbeispiel, gemeinsame Anweisung, Merkkasten,
  Kopfrechenblock); Blätter nur als Bestellung (bau.json),
  PDFs nur als Zwischenspeicher und Notvorrat ohne Abo.
- Ein Prompt mit Prüfungsmodus statt zwei?
- Literaturbefunde: gemischter Schlussblock „Prüfe dich“ im
  Lernblatt; Zone als Diagnose mit Verweis („hängst du hier →
  Nr. 3“) statt Schalter „wie lange her“; Wachhalten über
  Basisheft (vorhanden) statt neuer Blattart.
- Pflichtelemente 1–10 aus quellen/altlehrwerke-pflichtformen.md
  (u. a. fehlerfreie Vorlage „Hat Lea richtig gerechnet?“,
  Aussagenserie wahr/falsch, Personenaussage, Kontrolle als
  Schlusszeile).

Konsistenz (Abgleich 28.09. abends):
- K1 Quellen der letzten Tage nirgends eingebunden (liegen nur in
  quellen/ und katalog/_fremd-*): DDR-Bände, Literatur,
  Fremdoriginale. Einbinden heißt in allen Dimensionen, je mit
  Ort, an dem es wirkt:
  · Sprossen – Zahl und Folge je Kette, Vorstufen-Serie („erst
    benennen“), Kontrolle als Schlussprosse → Katalog, Bank;
  · Formulierungen – Operatoren, Anweisung über dem Päckchen,
    Personenaussagen („Hat Karin recht?“), Schrittnamen in der
    Musterlösung → Sprachregeln, bank.md, Prompt;
  · Layout – Merkmal über dem Päckchen, Seitenaufbau, Stellung
    von Beispiel und Merkkasten → layout-befunde, zusammenbau;
  · Dichte – Aufgaben je Seite und je Schritt (DDR 40–120 Posten,
    heute 2–4; Literatur: öfter und gemischt statt länger) →
    Regel für Lernblatt, Fokus, schwach;
  · Schwerpunkte – welches Thema, welcher Schritt wie viel Raum
    bekommt, Reihenfolge der Themen je Klasse (DDR, Lehrwerke,
    P10-Häufigkeit) → Katalog-Marken, Planfrage;
  dazu die Pflichtelemente-Vorschläge 1–10 (Entscheidung oben).
- K2 bank.md kannte die Sprachregeln nicht (neue Zeilen wären
  wieder Stichwortsprache) – vorläufiger Verweis am 28.09.
  eingetragen, Abnahme durch den Lehrer offen.
- K3 Sek II ohne Sprachlauf – Bank sprachlich uneinheitlich.
- K4 ziel.md widerspricht den Beschlüssen in drei Punkten:
  „kein Kasten auf dem Blatt“ (vs. Befund 54), „voller statt
  kürzer“ (vs. „nie 30 Seiten“), v4.4 „kein Beispiel“ (vs.
  Literatur); dazu fehlt die Bank-Linie. Revision vorlegen.
- K5 Katalog-Lücke: „Term durch Zahl teilen“ fehlt (Katalog und
  Bank); Register-Abgleich als Lückenprüfung.
- K6 Rezept S (schwach) im Zusammenbau veraltet (leere Seiten,
  55 TODO bei terme); Rezept K ist Durchgang, nicht Fokus.
- K7 bank/_strittig.md: 1 123 Zeilen ungesichtet.
- K8 bau/regal/, bau/kompetenz/, bau/hefte/ stammen aus der
  überholten Linie „Kompetenzblatt als Grundeinheit“ – bleiben
  als Material, sind kein Regal im Betrieb.
- Geprüft und in Ordnung: vier Grafikänderungen in pythagoras,
  symmetrie-abbildungen, terme stammen aus der Gegenlese-
  Korrektur, nicht aus dem Sprachlauf.

Verworfen (mit Grund):
- Dialog nach der Lage des Schülers („neu, unsicher, Prüfung“):
  widerspricht „ein Blatt für alle“.
- Neue Blattarten Kompetenzblatt/Themenblatt/Übungsblatt:
  Drift; die alten Namen tragen.
- Päckchen-Fokus „im DDR-Stil“ mit 40–120 Aufgaben je Seite:
  Dichte bringt laut Literatur wenig.
- Alle 424 Durchgänge bauen: vor dem Layout-Durchgang und der
  Einteilung verfrüht.

## 6 Nächster Arbeitsschritt

Modell: Opus 5.5 (Fable auf Wahl des Lehrers).

1. Einbindungslauf K1/K2 als Vorschlagsdatei: alle Quellen der
   letzten Tage in den fünf Dimensionen (Sprossen,
   Formulierungen, Layout, Dichte, Schwerpunkte) gegen Katalog,
   bank.md, auftrag-eintrag.md, zusammenbau und Prompt halten;
   je Fund Ort, Wortlaut, Vorschlag. Urteil im Chat, dann
   Umsetzung.
2. Testlauf-Bericht v4.4 lesen (bau/merkzettel-abend.md Punkt 1).
3. ziel.md nachziehen mit den Revisionen aus K4 (Lehrer
   entscheidet) – danach erst der Prompt (Schalter,
   Lernblatt/Fokus/Prüfungsheft, Ausnahmeweg ohne Abo).
