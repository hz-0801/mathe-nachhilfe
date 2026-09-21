# Belege der Blatt-0-Fertigkeiten ohne Ziel
Stand 2026-09-21, Katalog auf Commit cfa4723.
Erzeugt von `werkzeuge/blatt0-belege.py` (v0.1) aus den Blatt-0-Abschnitten der Einträge, `msa/msa-typen.csv`, `msa/msa-katalog-basis.csv`, `msa/msa-katalog-kontext.csv`, `themen.csv`, `quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt`, `quellen/quelle-rlp-teil-c-mathematik-2023.txt` und der Registerzeile [MSK] in `katalog/_quellen.md`; abgeleitet, nie von Hand ändern. Vorschlagsliste für die Fertigkeitszeilen, die keinen Dateiverweis tragen: was ihre Quellenklammer hergibt, wenn man sie gegen die Register im Repo hält. Kein Eintrag wird geändert, nichts wird entschieden; eine Zeile, deren Klammer kein Register auflöst, bleibt ohne Vorschlag – das ist ein Ergebnis, kein Mangel.

Gemessen: 73 Einträge (`katalog/*.md` ohne `_*` und `index.md`). Lesarten wie in `werkzeuge/tragfaehigkeit.py` (v0.1), importiert: Blatt-0-Abschnitt = „### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, Verweis = `<name>.md`. Fertigkeitszeile = Zeile des Abschnitts, die mit „- “ beginnt und vor der Zwischenzeile „Erkennungsschritte…“ steht (die Erkennungsschritte gehören dem Thema selbst). Ziel = Verweis ohne Pfad auf einen anderen vorhandenen Katalogeintrag, irgendwo in der Zeile; Selbstverweise zählen nicht. Klammer = die letzte eckige Klammer der Zeile (vermerkt, wenn sie nicht am Zeilenende steht). Bestandteile = Klammer an „;“ und „,“ zerlegt, nicht in „…“ und nicht in runden Klammern; ein Teil, der mit einer P10-Aufgabenkennung beginnt, setzt den vorigen fort, ein bloßer MSK-Code einen MSK-Teil. Sechs Sorten je Bestandteil: P10-Typ (enthält „P10“ und einen Typnamen in „…“ oder eine Aufgabenkennung), LS-AA-Kapitel („LS-AA Kl. 8 II 1“), RLP mit Zitat, RLP ohne Zitat (auch mit Zusatz ohne Anführungszeichen), MSK-Code, sonstiges oder keine Klammer. Zeilennummern zählen ab 1 in der Datei.

Auflösung, soweit ein Register es hergibt: P10-Typ – Typname gegen die Spalte `typ` von `msa/msa-typen.csv`, Kennung gegen `beispiel_id`; je Treffer das Thema und über `themen.csv` (profil msa) das kanonische Thema; Kennungen zusätzlich gegen die `id`-Spalte der beiden msa-Kataloge (Thema, Typ, Nebentypen der Katalogzeile), weil die Typenliste je Typ nur eine beispiel_id führt. LS-AA-Kapitel – Fahrplan Teil 1 (Gliederung je Klasse, zweispaltig): Kapiteltitel und Titel der Lerneinheit; Teil 2 (RLP-Inhalte mit „Zu finden in Studyly“): die RLP-Blöcke (Niveaustufe, Jahrgang, Themenbereich, Bereich), unter denen das Kapitel mit dieser Lerneinheit genannt ist. RLP mit Zitat – das Zitat wird in den Spalten des RLP-Texts gesucht (mehrspaltig gesetzt; ein Block sind die Zeilen zwischen zwei Leerzeilen, darin wird jede Zelle an die Zelle der Zeile davor gehängt, mit der sie sich am weitesten überlappt – je Zelle höchstens eine Fortsetzung –, Silbentrennung wird zusammengezogen, „…“ im Zitat erlaubt eine Lücke); Fundstelle mit Zeilen des Treffers, Block, Niveaustufenbuchstabe(n) am Block (der Buchstabe steht einmal je Stufe am linken Rand, in der Mitte seiner Zeilen) und Seitenkopf – zuerst genau, sonst ohne Groß-/Kleinschreibung. Steht das Zitat nicht im Text, wird noch der längste Wortanfang gesucht (mindestens 3 Wörter und mindestens die Hälfte; nicht bei Zitaten mit Lücke) und als Teiltreffer genannt, ohne als Auflösung zu zählen. RLP ohne Zitat, MSK-Code und sonstiges werden nach Auftrag nicht aufgelöst („nicht aufzulösen“; „nicht aufgelöst“ heißt dagegen: das Register gab nichts her); beim MSK-Code steht der Bausteintitel aus `katalog/_quellen.md` dabei, soweit er dort genannt ist. Zusätzlich je Zeile: welche kanonischen Namen aus `themen.csv` der Wortlaut der Zeile ohne ihre Quellenklammer wörtlich nennt (der Name selbst mit Bindestrich als Leerzeichen und ohne Rücksicht auf Groß-/Kleinschreibung, ein `thema`-Wert seiner Zeilen oder die H1-Überschrift seiner Katalogdatei, jeweils als ganzes Wort, mit dem Umfeld des Treffers; der eigene Eintrag zählt nicht) – keine Ähnlichkeitssuche, kein Raten; ob das Wort in der Zeile das Thema meint, steht nicht hier.

## Zahlen
Teil 1, die 22 Sek-I-Einträge des Auftrags Blatt-0-Dateiverweise (21 Dateien aus `archiv/ersetzungen-blatt0-2026-09-21.txt` und `terme.md`; dieselbe Menge wie `_verweise.md` § 5 auf Commit c05e6f0): 147 Fertigkeitszeilen, 112 mit Ziel, 35 ohne. Gegenprobe des Auftrags 147/112/35: bestanden.
Teil 2, die übrigen 51 Einträge: 316 Fertigkeitszeilen, 258 mit Ziel, 58 ohne – berichtet, nicht geprüft. Darunter sieben Einträge mit Stufe Sek I oder Sek I + II in der Statuszeile (potenzen-wurzeln, reelle-zahlen, trigonometrische-funktionen, zinsrechnung, daten, einheiten, lineare-gleichungssysteme); sie stehen in Teil 2 vorn.
Bestandteile der Klammern in Teil 1 nach Sorte (Bestandteile · davon aufgelöst): P10-Typ 2 · 2; LS-AA-Kapitel 5 · 5; RLP mit Zitat 5 · 4; RLP ohne Zitat 23 · 0; MSK-Code 13 · 0; sonstiges oder keine Klammer 3 · 0. MSK-Codes mit Bausteintitel aus _quellen.md: 4.
Bestandteile der Klammern in Teil 2 nach Sorte (Bestandteile · davon aufgelöst): P10-Typ 26 · 26; LS-AA-Kapitel 5 · 5; RLP mit Zitat 18 · 13; RLP ohne Zitat 30 · 0; MSK-Code 2 · 0; sonstiges oder keine Klammer 13 · 0. MSK-Codes mit Bausteintitel aus _quellen.md: 2.
Einträge ohne Blatt-0-Abschnitt: keine. Einträge ohne Zwischenzeile „Erkennungsschritte…“ (der ganze Abschnitt gilt als Fertigkeitenteil): ableitungsgraph-und-funktionsgraph.

## 1 Die 22 Sek-I-Einträge des Auftrags Blatt-0-Dateiverweise
Reihenfolge wie in der Ersetzungsdatei (alphabetisch). Je Eintrag die Fertigkeitszeilen ohne Ziel mit Zeilennummer, Wortlaut, Klammer, Bestandteilen, Sorte, dem, was die Register hergeben, und den wörtlichen themen.csv-Treffern.

### binomische-formeln – Stufe Sek I; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### bruchrechnung – Stufe Sek I; 6 Fertigkeitszeilen, 2 mit Ziel, 4 ohne
- Zeile 28:
  > - Kürzen und Erweitern; gleichwertige Brüche (zwei Drittel gleich vier Sechstel) – Einheit 1 und 3. [RLP D, MSK B2B]
  - Klammer: `RLP D, MSK B2B` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `MSK B2B` – MSK-Code, nicht aufzulösen:
      - B2B: Bausteintitel in _quellen.md nicht genannt
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 29:
  > - Vielfache und Teiler (kgV von vier und sechs, ggT von zwölf und achtzehn) – Einheit 1 (Hauptnenner) und Einheit 3 (Kürzen). [RLP D, LS-AA Kl. 5 III 5]
  - Klammer: `RLP D, LS-AA Kl. 5 III 5` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `LS-AA Kl. 5 III 5` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 5 III 5“ → Klasse 5, Kapitel III „Rechnen“, Lerneinheit 5 „Teilbarkeit“; Fahrplan-Zuordnung (Teil 2): RLP D, Jg. 5/6, Themenbereich „Zahlen und Operationen“ – Zahlvorstellungen
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 30:
  > - Stellenwerte der Dezimalzahlen (Zehntel, Hundertstel; 0,7 = 0,70) – Einheit 2 und 4. [MSK D1A, RLP D]
  - Klammer: `MSK D1A, RLP D` – 2 Bestandteile:
    - `MSK D1A` – MSK-Code, nicht aufzulösen:
      - D1A: Bausteintitel in _quellen.md nicht genannt
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 31:
  > - Schriftliches Rechnen mit natürlichen Zahlen, Einmaleins – Einheit 2 und 4. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### brueche-dezimalzahlen – Stufe Sek I; 7 Fertigkeitszeilen, 3 mit Ziel, 4 ohne
- Zeile 27:
  > - Teilen und Vervielfachen im Kopf (vierundzwanzig geteilt durch sechs, drei mal neun), Einmaleins – Einheit 1 bis 3 (Anteil nehmen, Erweitern, Kürzen). [RLP D, LS-AA Kl. 5 III]
  - Klammer: `RLP D, LS-AA Kl. 5 III` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `LS-AA Kl. 5 III` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 5 III“ → Klasse 5, Kapitel III „Rechnen“ (Lerneinheiten: 1 Terme · 2 Rechenvorteile beim Addieren und Multiplizieren · 3 Ausklammern und Ausmultiplizieren · 4 Potenzieren · 5 Teilbarkeit · 6 Primzahlen und Primfaktorzerlegung · 7 Schriftliches Addieren und Subtrahieren · 8 Schriftliches Multiplizieren · 9 Schriftliches Dividieren · 10 Sachaufgaben systematisch lösen); Fahrplan-Zuordnung (Teil 2): RLP D, Jg. 5/6, Themenbereich „Zahlen und Operationen“ – Zahlvorstellungen; RLP D, Jg. 5/6, Themenbereich „Zahlen und Operationen“ – Operationsvorstellungen und Rechenstrategien
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 28:
  > - Teiler und Vielfache einer Zahl angeben (Teiler von zwölf; Vielfache von vier) – Einheit 2 und 3 (Kürzen, Hauptnenner). [RLP D „Angeben gemeinsamer Teiler und Vielfache zweier natürlicher Zahlen“, LS-AA Kl. 5 III 5]
  - Klammer: `RLP D „Angeben gemeinsamer Teiler und Vielfache zweier natürlicher Zahlen“, LS-AA Kl. 5 III 5` – 2 Bestandteile:
    - `RLP D „Angeben gemeinsamer Teiler und Vielfache zweier natürlicher Zahlen“` – RLP mit Zitat, aufgelöst:
      - „Angeben gemeinsamer Teiler und Vielfache zweier natürlicher Zahlen“ (Klammer nennt D): Zeilen 1823–1825 (Block 1812–1836), Niveaustufe am Block: D (Zeile 1826); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen D, E
    - `LS-AA Kl. 5 III 5` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 5 III 5“ → Klasse 5, Kapitel III „Rechnen“, Lerneinheit 5 „Teilbarkeit“; Fahrplan-Zuordnung (Teil 2): RLP D, Jg. 5/6, Themenbereich „Zahlen und Operationen“ – Zahlvorstellungen
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 29:
  > - Stellenwerte natürlicher Zahlen und Zahlenstrahl mit natürlichen Zahlen (Skala ablesen) – Einheit 3 und 4. [RLP C/D, MSK N2]
  - Klammer: `RLP C/D, MSK N2` – 2 Bestandteile:
    - `RLP C/D` – RLP ohne Zitat, nicht aufzulösen.
    - `MSK N2` – MSK-Code, nicht aufzulösen:
      - N2: Bausteintitel in _quellen.md nicht genannt
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 31:
  > - Schriftlich oder mit Taschenrechner dividieren (drei geteilt durch acht) – Einheit 4 (Division). [RLP D „schriftliche Rechenverfahren … Division“]
  - Klammer: `RLP D „schriftliche Rechenverfahren … Division“` – 1 Bestandteil:
    - `RLP D „schriftliche Rechenverfahren … Division“` – RLP mit Zitat, nicht aufgelöst:
      - „schriftliche Rechenverfahren … Division“ (Klammer nennt D): im RLP-Text nicht gefunden
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### flaechen – Stufe Sek I; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### koerper – Stufe Sek I; 6 Fertigkeitszeilen, 5 mit Ziel, 1 ohne
- Zeile 32:
  > - Räumliches Vorstellen: Würfelnetze falten, Ansichten von Würfelbauten – Einheit 1. [RLP C/D; MO]
  - Klammer: `RLP C/D; MO` – 2 Bestandteile:
    - `RLP C/D` – RLP ohne Zitat, nicht aufzulösen.
    - `MO` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### kreis – Stufe Sek I; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### lineare-funktionen – Stufe Sek I; 6 Fertigkeitszeilen, 1 mit Ziel, 5 ohne
- Zeile 24:
  > - Koordinaten lesen und eintragen, 4 Quadranten, (x|y)-Reihenfolge. [RLP E, MSK S4]
  - Klammer: `RLP E, MSK S4` – 2 Bestandteile:
    - `RLP E` – RLP ohne Zitat, nicht aufzulösen.
    - `MSK S4` – MSK-Code, nicht aufzulösen:
      - S4: Bausteintitel in _quellen.md „Diagramme“
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 25:
  > - Proportionale Zuordnung erkennen und hochrechnen (Dreisatz). [MSK S5, RLP D/E] – für Einheit 1 und 5.
  - Klammer: `MSK S5, RLP D/E` (nicht am Zeilenende) – 2 Bestandteile:
    - `MSK S5` – MSK-Code, nicht aufzulösen:
      - S5: Bausteintitel in _quellen.md nicht genannt
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 26:
  > - Negative Zahlen multiplizieren und dividieren – Steigung, Funktionswerte. [MSK N]
  - Klammer: `MSK N` – 1 Bestandteil:
    - `MSK N` – MSK-Code, nicht aufzulösen:
      - N: Bausteintitel in _quellen.md nicht genannt
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 27:
  > - Brüche als Steigung (½, −¾), Bruch mal ganze Zahl. [MSK B] – ab Einheit 2.
  - Klammer: `MSK B` (nicht am Zeilenende) – 1 Bestandteil:
    - `MSK B` – MSK-Code, nicht aufzulösen:
      - B: Bausteintitel in _quellen.md nicht genannt
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 29:
  > - Terme zusammenfassen. – für Einheit 4 (Gleichsetzen).
  - Klammer: keine – Sorte sonstiges oder keine Klammer.
  - themen.csv wörtlich im Wortlaut: **terme** (Name „Terme“ in „- Terme zusammenfassen. – für Einheit…“).

### lineare-gleichungen – Stufe Sek I; 5 Fertigkeitszeilen, 2 mit Ziel, 3 ohne
- Zeile 22:
  > - Negative Zahlen addieren, subtrahieren, dividieren (12 : (−3)) – Lösungen und Umformungen. [MSK N, RLP D]
  - Klammer: `MSK N, RLP D` – 2 Bestandteile:
    - `MSK N` – MSK-Code, nicht aufzulösen:
      - N: Bausteintitel in _quellen.md nicht genannt
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 24:
  > - Punkt vor Strich (3 · 4 − 5) – Probe und Einsetzen. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 26:
  > - Brüche: Hauptnenner, Bruch mal Zahl – nur Einheit 3. [MSK B]
  - Klammer: `MSK B` – 1 Bestandteil:
    - `MSK B` – MSK-Code, nicht aufzulösen:
      - B: Bausteintitel in _quellen.md nicht genannt
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### potenz-exponentialfunktionen – Stufe Sek I; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### prozentrechnung – Stufe Sek I; 6 Fertigkeitszeilen, 2 mit Ziel, 4 ohne
- Zeile 28:
  > - Bruch ↔ Dezimalzahl (ein Viertel, drei Fünftel) – Einheit 1, Einheit 3 (Operator). [RLP D/E]
  - Klammer: `RLP D/E` – 1 Bestandteil:
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 29:
  > - Bruchteil einer Größe (zwei Drittel von 60 €) – Einheit 3. [RLP D „Operator“]
  - Klammer: `RLP D „Operator“` – 1 Bestandteil:
    - `RLP D „Operator“` – RLP mit Zitat, aufgelöst:
      - „Operator“ (Klammer nennt D): Zeile 1890 (Block 1871–1894), Niveaustufe am Block: D (Zeile 1885); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen D, E | Zeile 1916 (Block 1897–1916), Niveaustufe am Block: E (Zeile 1907); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen D, E | Zeile 2660 (Block 2656–2672), Niveaustufe am Block: C (Zeile 2664); Seitenkopf: Themenbereich „Gleichungen und Funktionen“ – Niveaustufen A, B, C
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 30:
  > - Durch hundert teilen, mit Dezimalzahlen multiplizieren (Kommaverschiebung) – Einheit 2 bis 4. [RLP D, LS-AA Kl. 6 V 4]
  - Klammer: `RLP D, LS-AA Kl. 6 V 4` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `LS-AA Kl. 6 V 4` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 6 V 4“ → Klasse 6, Kapitel V „Zahlen multiplizieren und dividieren“, Lerneinheit 4 „Kommaverschiebung“; Fahrplan-Zuordnung (Teil 2): RLP D, Jg. 5/6, Themenbereich „Zahlen und Operationen“ – Operationsvorstellungen und Rechenstrategien
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 32:
  > - Runden auf eine Dezimalstelle – Einheit 2 und 5. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### pyramide-kegel-kugel – Stufe Sek I; 9 Fertigkeitszeilen, 9 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### pythagoras – Stufe Sek I; 9 Fertigkeitszeilen, 9 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### quadratische-funktionen – Stufe Sek I; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### quadratische-gleichungen – Stufe Sek I; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### rationale-zahlen – Stufe Sek I; 5 Fertigkeitszeilen, 2 mit Ziel, 3 ohne
- Zeile 25:
  > - Natürliche Zahlen addieren, subtrahieren, multiplizieren, dividieren im Kopf (Einmaleins) – alle Einheiten. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **einheiten** (Name „Einheiten“ in „…n im Kopf (Einmaleins) – alle Einheiten.“).
- Zeile 26:
  > - Zahlenstrahl: Zahlen eintragen und ablesen, auch Dezimalzahlen und Brüche – Einheit 1. [RLP D, MSK D2A]
  - Klammer: `RLP D, MSK D2A` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `MSK D2A` – MSK-Code, nicht aufzulösen:
      - D2A: Bausteintitel in _quellen.md „Nachbarzahlen und Zählen in Schritten“
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 28:
  > - Punkt vor Strich und Klammern mit natürlichen Zahlen – Einheit 3 und 4. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### strahlensaetze – Stufe Sek I; 9 Fertigkeitszeilen, 9 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### symmetrie-abbildungen – Stufe Sek I; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### terme – Stufe Sek I; 4 Fertigkeitszeilen, 0 mit Ziel, 4 ohne
- Zeile 24:
  > - Addieren und Subtrahieren negativer Zahlen (3 − 7, −2 − 5) – für Vorzahlen und Vorzeichen in jeder Einheit. [MSK N, RLP D]
  - Klammer: `MSK N, RLP D` – 2 Bestandteile:
    - `MSK N` – MSK-Code, nicht aufzulösen:
      - N: Bausteintitel in _quellen.md nicht genannt
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 25:
  > - Multiplizieren mit Vorzeichen ((−2) · (−3), 3 · (−4)) – für Malnehmen und Minusklammer. [RLP D/E]
  - Klammer: `RLP D/E` – 1 Bestandteil:
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 26:
  > - Dezimalzahlen und einfache Brüche als Vorzahlen (2,5x, ½x) – nur, wenn die Einheit sie braucht. [MSK D, DB]
  - Klammer: `MSK D, DB` – 1 Bestandteil:
    - `MSK D, DB` – MSK-Code, nicht aufzulösen:
      - D: Bausteintitel in _quellen.md nicht genannt
      - DB: Bausteintitel in _quellen.md „Zusammenhang von Dezimalzahlen und Brüchen“
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 27:
  > - Punkt vor Strich mit Zahlen (Zahl minus Produkt) – ab Einheit 2 (Produkt mit Vorzahl plus gleichartiges Glied) und Einheit 3. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### trigonometrie – Stufe Sek I; 9 Fertigkeitszeilen, 8 mit Ziel, 1 ohne
- Zeile 28:
  > - Taschenrechner: Grad-Modus (DEG) prüfen, Tasten sin, cos, tan mit dem Winkel dahinter, Umkehrtaste über SHIFT, Bruch in Klammern, Ergebnis erst am Ende runden – alle Einheiten. Kein eigenes Thema. [P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“; 2019-OS-K3b, 2025-OS-K4a „Umkehrfunktion am Taschenrechner“; Hilfsmittel immer ja]
  - Klammer: `P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“; 2019-OS-K3b, 2025-OS-K4a „Umkehrfunktion am Taschenrechner“; Hilfsmittel immer ja` – 2 Bestandteile:
    - `P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“; 2019-OS-K3b, 2025-OS-K4a „Umkehrfunktion am Taschenrechner“` – P10-Typ, aufgelöst:
      - „Taschenrechner in Bogenmaß“: kein Typname in msa/msa-typen.csv
      - „Umkehrfunktion am Taschenrechner“: kein Typname in msa/msa-typen.csv
      - Kennung 2021-OS-K3a: Katalogzeile (msa-katalog-kontext.csv): Thema „Trigonometrie im rechtwinkligen Dreieck“, Typ „Seite im rechtwinkligen Dreieck berechnen“ → themen.csv: trigonometrie
      - Kennung 2019-OS-K3b: Katalogzeile (msa-katalog-kontext.csv): Thema „Trigonometrie im rechtwinkligen Dreieck“, Typ „Winkel im rechtwinkligen Dreieck berechnen“ → themen.csv: trigonometrie
      - Kennung 2025-OS-K4a: beispiel_id des Typs „Winkel im rechtwinkligen Dreieck berechnen“ in msa/msa-typen.csv, Thema „Trigonometrie im rechtwinkligen Dreieck“ → themen.csv: trigonometrie; Katalogzeile (msa-katalog-kontext.csv): Thema „Satz des Pythagoras“, Typ „Pythagoras Hypotenuse“, Nebentypen „Winkel im rechtwinkligen Dreieck berechnen“ → themen.csv: pythagoras
    - `Hilfsmittel immer ja` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **einheiten** (Name „Einheiten“ in „…is erst am Ende runden – alle Einheiten. Kein eigenes Thema.“).

### wahrscheinlichkeit – Stufe Sek I; 5 Fertigkeitszeilen, 4 mit Ziel, 1 ohne
- Zeile 29:
  > - Anzahl der Zahlen in einem Bereich (101 bis 900 sind 800 Lose; Endziffer 6 in 106 bis 896 sind 80) – Einheit 2. [P10 2016-OS-K5c, 2016-OS-K5d]
  - Klammer: `P10 2016-OS-K5c, 2016-OS-K5d` – 1 Bestandteil:
    - `P10 2016-OS-K5c, 2016-OS-K5d` – P10-Typ, aufgelöst:
      - Kennung 2016-OS-K5c: Katalogzeile (msa-katalog-kontext.csv): Thema „Wahrscheinlichkeit einstufig“, Typ „Wahrscheinlichkeit einstufig“, Nebentypen „Behauptung prüfen“ → themen.csv: wahrscheinlichkeit
      - Kennung 2016-OS-K5d: Katalogzeile (msa-katalog-kontext.csv): Thema „Wahrscheinlichkeit einstufig“, Typ „Wahrscheinlichkeit einstufig“, Nebentypen „Behauptung prüfen“ → themen.csv: wahrscheinlichkeit
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### winkel-dreiecke – Stufe Sek I; 5 Fertigkeitszeilen, 3 mit Ziel, 2 ohne
- Zeile 27:
  > - Mit Lineal und Geodreieck zeichnen: Strecken messen, Senkrechte und Parallele zeichnen, rechten Winkel erkennen – Einheit 1, 4, 5. [RLP C/D „Zeichnen … mithilfe von Zeichengeräten“]
  - Klammer: `RLP C/D „Zeichnen … mithilfe von Zeichengeräten“` – 1 Bestandteil:
    - `RLP C/D „Zeichnen … mithilfe von Zeichengeräten“` – RLP mit Zitat, aufgelöst:
      - „Zeichnen … mithilfe von Zeichengeräten“ (Klammer nennt C/D): Zeilen 2441–2446 (Block 2434–2485), Niveaustufe am Block: D (Zeile 2448), E (Zeile 2470); Seitenkopf: Themenbereich „Raum und Form“ – Niveaustufen D, E
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 30:
  > - Vierecksarten kennen: Rechteck, Quadrat, Parallelogramm, Raute, Trapez, Drachen; parallele und gleich lange Seiten in der Figur erkennen – Einheit 2 und 3. [RLP C „Beschreiben der Beziehungen zwischen Vierecken“; LS-AA Kl. 5 II 5]
  - Klammer: `RLP C „Beschreiben der Beziehungen zwischen Vierecken“; LS-AA Kl. 5 II 5` – 2 Bestandteile:
    - `RLP C „Beschreiben der Beziehungen zwischen Vierecken“` – RLP mit Zitat, aufgelöst:
      - „Beschreiben der Beziehungen zwischen Vierecken“ (Klammer nennt C): Zeilen 2370–2371 (Block 2306–2375), Niveaustufe am Block: A (Zeile 2314), B (Zeile 2330), C (Zeile 2357); Seitenkopf: Themenbereich „Raum und Form“ – Niveaustufen A, B, C
    - `LS-AA Kl. 5 II 5` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 5 II 5“ → Klasse 5, Kapitel II „Symmetrie“, Lerneinheit 5 „Eigenschaften von Vielecken“; Fahrplan-Zuordnung (Teil 2): RLP D, Jg. 5/6, Themenbereich „Raum und Form“ – Geometrische Objekte
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### zuordnungen – Stufe Sek I; 5 Fertigkeitszeilen, 2 mit Ziel, 3 ohne
- Zeile 25:
  > - Multiplizieren und Dividieren mit Dezimalzahlen (Preis geteilt durch Stückzahl, Preis mal Stückzahl) – Einheit 2 bis 4. [MSK S5A Diagnose, RLP D]
  - Klammer: `MSK S5A Diagnose, RLP D` – 2 Bestandteile:
    - `MSK S5A Diagnose` – MSK-Code, nicht aufzulösen:
      - S5A: Bausteintitel in _quellen.md „Proportionale Zusammenhänge“
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 26:
  > - Vielfache und Teiler erkennen (zwölf ist das Dreifache von vier) – Einheit 2 und 3. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 28:
  > - Bruchteil einer Größe (die Hälfte, ein Viertel von 12 €) – Einheit 2. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

## 2 Die übrigen Einträge
Zuerst die Einträge mit Stufe Sek I und Sek I + II in der Statuszeile, dann die Sek-II-Einträge, je alphabetisch. Gleicher Aufbau wie Teil 1; die Zahlen sind nicht gegengeprüft.

### potenzen-wurzeln – Stufe Sek I; 9 Fertigkeitszeilen, 1 mit Ziel, 8 ohne
- Zeile 23:
  > - Kleines Einmaleins und Malnehmen mehrstelliger Zahlen im Kopf oder halbschriftlich, Malketten mit gleichen Faktoren – Einheit 1. Kein eigenes Thema (Grundschule; LS-AA Kl. 5 I 4). [RLP C/D; P10 2020-OS-B1h Verfahren als Malkette]
  - Klammer: `RLP C/D; P10 2020-OS-B1h Verfahren als Malkette` – 2 Bestandteile:
    - `RLP C/D` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2020-OS-B1h Verfahren als Malkette` – P10-Typ, aufgelöst:
      - Kennung 2020-OS-B1h: Katalogzeile (msa-katalog-basis.csv): Thema „Potenzen und Wurzeln“, Typ „Exponent einer Potenz bestimmen“ → themen.csv: potenzen-wurzeln
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 24:
  > - Quadratzahlen bis 100 aus dem Kopf, Kubikzahlen zwei hoch drei, drei hoch drei, zehn hoch drei – Einheit 1 und 3. Kein eigenes Thema (Grundschule). [RLP C „Nennen und Erkennen von Quadratzahlen (bis 100)“]
  - Klammer: `RLP C „Nennen und Erkennen von Quadratzahlen (bis 100)“` – 1 Bestandteil:
    - `RLP C „Nennen und Erkennen von Quadratzahlen (bis 100)“` – RLP mit Zitat, aufgelöst:
      - „Nennen und Erkennen von Quadratzahlen (bis 100)“ (Klammer nennt C): Zeilen 1727–1728 (Block 1717–1731), Niveaustufe am Block: C (Zeile 1727); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen A, B, C
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 25:
  > - Vorzeichenregel beim Malnehmen (minus mal minus gibt plus), Anzahl der Minuszeichen zählen, Quadrat einer negativen Zahl mit und ohne Klammer – Einheit 1 und 3. Thema Rationale Zahlen, Einheit 3. [RLP E; P10 2014-OS-K7a Voraussetzung „Potenz mit negativer Basis“, 2015-OS-B1j „negative Basis“]
  - Klammer: `RLP E; P10 2014-OS-K7a Voraussetzung „Potenz mit negativer Basis“, 2015-OS-B1j „negative Basis“` – 2 Bestandteile:
    - `RLP E` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2014-OS-K7a Voraussetzung „Potenz mit negativer Basis“, 2015-OS-B1j „negative Basis“` – P10-Typ, aufgelöst:
      - „Potenz mit negativer Basis“: kein Typname in msa/msa-typen.csv
      - „negative Basis“: kein Typname in msa/msa-typen.csv
      - Kennung 2014-OS-K7a: Katalogzeile (msa-katalog-kontext.csv): Thema „Quadratische Funktionen“, Typ „Punktprobe durchführen“ → themen.csv: quadratische-funktionen
      - Kennung 2015-OS-B1j: beispiel_id des Typs „Wurzel eines Quadrats berechnen“ in msa/msa-typen.csv, Thema „Potenzen und Wurzeln“ → themen.csv: potenzen-wurzeln; Katalogzeile (msa-katalog-basis.csv): Thema „Potenzen und Wurzeln“, Typ „Wurzel eines Quadrats berechnen“ → themen.csv: potenzen-wurzeln
  - themen.csv wörtlich im Wortlaut: **rationale-zahlen** (Name „Rationale Zahlen“ in „…mmer – Einheit 1 und 3. Thema Rationale Zahlen, Einheit 3.“).
- Zeile 26:
  > - Dezimalzahlen multiplizieren (Kommastellen zählen), Brüche multiplizieren – Einheit 1 und 3. Thema Bruchrechnung. [RLP D; P10 2023-OS-B1f Fehlerquelle Quadrat einer Dezimalzahl als Verdopplung]
  - Klammer: `RLP D; P10 2023-OS-B1f Fehlerquelle Quadrat einer Dezimalzahl als Verdopplung` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2023-OS-B1f Fehlerquelle Quadrat einer Dezimalzahl als Verdopplung` – P10-Typ, aufgelöst:
      - Kennung 2023-OS-B1f: beispiel_id des Typs „Zahlen in verschiedenen Darstellungen vergleichen“ in msa/msa-typen.csv, Thema „Brüche und Dezimalzahlen“ → themen.csv: brueche-dezimalzahlen; Katalogzeile (msa-katalog-basis.csv): Thema „Brüche und Dezimalzahlen“, Typ „Zahlen in verschiedenen Darstellungen vergleichen“ → themen.csv: brueche-dezimalzahlen
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…eren – Einheit 1 und 3. Thema Bruchrechnung.“).
- Zeile 27:
  > - Große Zahlen lesen und schreiben (Dreiergruppen, Zahlwörter bis Billion), Stellenwerttafel, mal zehn, hundert und tausend durch Nullen anhängen – Einheit 2. Kein eigenes Thema (Grundschule; LS-AA Kl. 5 I 3); Struktur: MSK D4A (Multiplizieren und Dividieren mit Zehnerzahlen). [RLP C „Zahldarstellungen natürlicher Zahlen bis eine Million“; P10 2015-OS-K3a Fehlerquelle „Nullen falsch zählen“]
  - Klammer: `RLP C „Zahldarstellungen natürlicher Zahlen bis eine Million“; P10 2015-OS-K3a Fehlerquelle „Nullen falsch zählen“` – 2 Bestandteile:
    - `RLP C „Zahldarstellungen natürlicher Zahlen bis eine Million“` – RLP mit Zitat, nicht aufgelöst:
      - „Zahldarstellungen natürlicher Zahlen bis eine Million“ (Klammer nennt C): im RLP-Text nicht gefunden; Teiltreffer – der Wortanfang „Zahldarstellungen natürlicher Zahlen bis“ (4 von 6 Wörtern) steht in: Zeilen 1702–1703 (Block 1686–1712), Niveaustufe am Block: A (Zeile 1692), B (Zeile 1707); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen A, B, C | Zeilen 1722–1723 (Block 1717–1731), Niveaustufe am Block: C (Zeile 1727); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen A, B, C
    - `P10 2015-OS-K3a Fehlerquelle „Nullen falsch zählen“` – P10-Typ, aufgelöst:
      - „Nullen falsch zählen“: kein Typname in msa/msa-typen.csv
      - Kennung 2015-OS-K3a: beispiel_id des Typs „Große Zahl mit Zehnerpotenz multiplizieren“ in msa/msa-typen.csv, Thema „Zehnerpotenzen und Näherungswerte“ → themen.csv: potenzen-wurzeln; Katalogzeile (msa-katalog-kontext.csv): Thema „Zehnerpotenzen und Näherungswerte“, Typ „Große Zahl mit Zehnerpotenz multiplizieren“ → themen.csv: potenzen-wurzeln
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 28:
  > - Kommaverschiebung: Dezimalzahl mal zehn, hundert, tausend – Komma nach rechts; geteilt – Komma nach links; Nullen auffüllen – Einheit 2. Thema Brüche und Dezimalzahlen, Einheit 4; Bruchrechnung (LS-AA Kl. 6 V 4). [RLP D; P10 2016-OS-B1h, 2019-OS-B1j Verfahren „Komma verschieben“]
  - Klammer: `RLP D; P10 2016-OS-B1h, 2019-OS-B1j Verfahren „Komma verschieben“` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2016-OS-B1h, 2019-OS-B1j Verfahren „Komma verschieben“` – P10-Typ, aufgelöst:
      - „Komma verschieben“: kein Typname in msa/msa-typen.csv
      - Kennung 2016-OS-B1h: Katalogzeile (msa-katalog-basis.csv): Thema „Zehnerpotenzen und Näherungswerte“, Typ „Zehnerpotenzschreibweise umwandeln“ → themen.csv: potenzen-wurzeln
      - Kennung 2019-OS-B1j: Katalogzeile (msa-katalog-basis.csv): Thema „Zehnerpotenzen und Näherungswerte“, Typ „Zehnerpotenzschreibweise umwandeln“ → themen.csv: potenzen-wurzeln
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…und Dezimalzahlen, Einheit 4; Bruchrechnung (LS-AA Kl. 6 V 4).“); **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…auffüllen – Einheit 2. Thema Brüche und Dezimalzahlen, Einheit 4; Bruchrechnung (LS…“).
- Zeile 29:
  > - Dezimalzahlen und Brüche vergleichen und ordnen, Bruch in Dezimalzahl umwandeln, Prozent in Dezimalzahl, negative Zahlen auf der Zahlengerade ordnen – Einheit 1 bis 3 (Vergleichs-Originale). Thema Brüche und Dezimalzahlen, Einheit 4 und 5; Rationale Zahlen, Einheit 1. [RLP D/E; P10 2017-OS-B1e, 2022-OS-B1j, 2015-OS-B1c, 2014-OS-B1h]
  - Klammer: `RLP D/E; P10 2017-OS-B1e, 2022-OS-B1j, 2015-OS-B1c, 2014-OS-B1h` – 2 Bestandteile:
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2017-OS-B1e, 2022-OS-B1j, 2015-OS-B1c, 2014-OS-B1h` – P10-Typ, aufgelöst:
      - Kennung 2017-OS-B1e: Katalogzeile (msa-katalog-basis.csv): Thema „Potenzen und Wurzeln“, Typ „Zahlen in verschiedenen Darstellungen vergleichen“ → themen.csv: potenzen-wurzeln
      - Kennung 2022-OS-B1j: Katalogzeile (msa-katalog-basis.csv): Thema „Potenzen und Wurzeln“, Typ „Zahlen in verschiedenen Darstellungen vergleichen“ → themen.csv: potenzen-wurzeln
      - Kennung 2015-OS-B1c: Katalogzeile (msa-katalog-basis.csv): Thema „Brüche und Dezimalzahlen“, Typ „Zahlen in verschiedenen Darstellungen vergleichen“ → themen.csv: brueche-dezimalzahlen
      - Kennung 2014-OS-B1h: Katalogzeile (msa-katalog-basis.csv): Thema „Brüche und Dezimalzahlen“, Typ „Zahlen in verschiedenen Darstellungen vergleichen“ → themen.csv: brueche-dezimalzahlen
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…(Vergleichs-Originale). Thema Brüche und Dezimalzahlen, Einheit 4 und 5; Rationale Z…“); **rationale-zahlen** (Name „Rationale Zahlen“ in „…zimalzahlen, Einheit 4 und 5; Rationale Zahlen, Einheit 1.“).
- Zeile 30:
  > - Runden von Dezimalzahlen auf eine und zwei Stellen, Näherungswert mit ≈ schreiben – Einheit 2 und 3. Thema Brüche und Dezimalzahlen, Einheit 5. [RLP D/E „sinnvolle Genauigkeit“; RLP G „sachgerechtes Runden von reellen Zahlen“]
  - Klammer: `RLP D/E „sinnvolle Genauigkeit“; RLP G „sachgerechtes Runden von reellen Zahlen“` – 2 Bestandteile:
    - `RLP D/E „sinnvolle Genauigkeit“` – RLP mit Zitat, nicht aufgelöst:
      - „sinnvolle Genauigkeit“ (Klammer nennt D/E): im RLP-Text nicht gefunden
    - `RLP G „sachgerechtes Runden von reellen Zahlen“` – RLP mit Zitat, aufgelöst:
      - „sachgerechtes Runden von reellen Zahlen“ (Klammer nennt G): Zeilen 1943–1944 (Block 1940–1947), Niveaustufe am Block: G (Zeile 1947); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen F, G, H
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…iben – Einheit 2 und 3. Thema Brüche und Dezimalzahlen, Einheit 5.“).

### reelle-zahlen – Stufe Sek I; 7 Fertigkeitszeilen, 1 mit Ziel, 6 ohne
- Zeile 23:
  > - Potenz als Malkette mit Basis und Exponent, Potenz ausrechnen (auch negative Basis), a hoch null gleich eins und negative Hochzahl als Bruch – Einheit 2 und 3. Thema Potenzen und Wurzeln, Einheit 1. [RLP F „fortgesetzte Multiplikation“, RLP G negative Exponenten; P10 2022-OS-B1j]
  - Klammer: `RLP F „fortgesetzte Multiplikation“, RLP G negative Exponenten; P10 2022-OS-B1j` – 3 Bestandteile:
    - `RLP F „fortgesetzte Multiplikation“` – RLP mit Zitat, aufgelöst:
      - „fortgesetzte Multiplikation“ (Klammer nennt F): Zeilen 1975–1976 (Block 1971–1999), Niveaustufe am Block: F (Zeile 1978), G (Zeile 1992); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen F, G, H
    - `RLP G negative Exponenten` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2022-OS-B1j` – P10-Typ, aufgelöst:
      - Kennung 2022-OS-B1j: Katalogzeile (msa-katalog-basis.csv): Thema „Potenzen und Wurzeln“, Typ „Zahlen in verschiedenen Darstellungen vergleichen“ → themen.csv: potenzen-wurzeln
  - themen.csv wörtlich im Wortlaut: **potenzen-wurzeln** (thema „Potenzen und Wurzeln“ in „…ruch – Einheit 2 und 3. Thema Potenzen und Wurzeln, Einheit 1.“).
- Zeile 24:
  > - Quadratwurzel als Umkehrung des Quadrierens, Quadratzahlen bis zwanzig hoch zwei, Wurzel mit dem Taschenrechner und Näherungswert, Wurzel zwischen zwei Nachbar-Quadratzahlen abschätzen, keine Wurzel aus negativer Zahl – Einheit 1 und 3. Thema Potenzen und Wurzeln, Einheit 3. [RLP F/G; P10 2015-OS-B1c, 2015-OS-B1j]
  - Klammer: `RLP F/G; P10 2015-OS-B1c, 2015-OS-B1j` – 2 Bestandteile:
    - `RLP F/G` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2015-OS-B1c, 2015-OS-B1j` – P10-Typ, aufgelöst:
      - Kennung 2015-OS-B1c: Katalogzeile (msa-katalog-basis.csv): Thema „Brüche und Dezimalzahlen“, Typ „Zahlen in verschiedenen Darstellungen vergleichen“ → themen.csv: brueche-dezimalzahlen
      - Kennung 2015-OS-B1j: beispiel_id des Typs „Wurzel eines Quadrats berechnen“ in msa/msa-typen.csv, Thema „Potenzen und Wurzeln“ → themen.csv: potenzen-wurzeln; Katalogzeile (msa-katalog-basis.csv): Thema „Potenzen und Wurzeln“, Typ „Wurzel eines Quadrats berechnen“ → themen.csv: potenzen-wurzeln
  - themen.csv wörtlich im Wortlaut: **potenzen-wurzeln** (thema „Potenzen und Wurzeln“ in „…Zahl – Einheit 1 und 3. Thema Potenzen und Wurzeln, Einheit 3.“).
- Zeile 25:
  > - Bruch in Dezimalzahl umwandeln (Division), abbrechende und periodische Dezimalzahlen erkennen und mit Periodenstrich schreiben, Dezimalzahl in Bruch – Einheit 1. Thema Brüche und Dezimalzahlen, Einheit 4. [RLP E „auch periodische Dezimalzahlen“; LS-AA Kl. 6 II 3]
  - Klammer: `RLP E „auch periodische Dezimalzahlen“; LS-AA Kl. 6 II 3` – 2 Bestandteile:
    - `RLP E „auch periodische Dezimalzahlen“` – RLP mit Zitat, aufgelöst:
      - „auch periodische Dezimalzahlen“ (Klammer nennt E): Zeilen 1856–1857 (Block 1838–1860), Niveaustufe am Block: E (Zeile 1850); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen D, E
    - `LS-AA Kl. 6 II 3` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 6 II 3“ → Klasse 6, Kapitel II „Brüche in Dezimalschreibweise“, Lerneinheit 3 „Abbrechende und periodische Dezimalzahlen“; Fahrplan-Zuordnung (Teil 2): RLP D, Jg. 5/6, Themenbereich „Zahlen und Operationen“ – Zahlvorstellungen
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…l in Bruch – Einheit 1. Thema Brüche und Dezimalzahlen, Einheit 4.“).
- Zeile 26:
  > - Zahlengerade mit negativen Zahlen, Brüche und Dezimalzahlen eintragen, Zahlen vergleichen und ordnen – Einheit 1. Thema Rationale Zahlen, Einheit 1; Brüche und Dezimalzahlen, Einheit 5. [RLP E]
  - Klammer: `RLP E` – 1 Bestandteil:
    - `RLP E` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…ngerade mit negativen Zahlen, Brüche und Dezimalzahlen eintragen, Zahlen vergleichen…“); **rationale-zahlen** (Name „Rationale Zahlen“ in „…und ordnen – Einheit 1. Thema Rationale Zahlen, Einheit 1; Brüche und Dezima…“).
- Zeile 27:
  > - Terme zusammenfassen: gleichartige Glieder, Vorzahl und Variable, Faktoren vertauschen – Einheit 2 und 3. Thema Terme, Einheit 2. [RLP E; LS-AA Kl. 7 IV 2]
  - Klammer: `RLP E; LS-AA Kl. 7 IV 2` – 2 Bestandteile:
    - `RLP E` – RLP ohne Zitat, nicht aufzulösen.
    - `LS-AA Kl. 7 IV 2` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 7 IV 2“ → Klasse 7, Kapitel IV „Terme und Gleichungen“, Lerneinheit 2 „Terme mit einer Variablen umformen“; Fahrplan-Zuordnung (Teil 2): RLP E, Jg. 7, Themenbereich „Gleichungen und Funktionen“ – Terme und Gleichungen
  - themen.csv wörtlich im Wortlaut: **terme** (Name „Terme“ in „- Terme zusammenfassen: gleichartige…“).
- Zeile 28:
  > - Brüche als Exponenten lesen und mit Brüchen rechnen: ein halb plus ein halb, ein Drittel, Kehrwert – Einheit 3. Thema Bruchrechnung, Einheit 1 und 3. [RLP D/E]
  - Klammer: `RLP D/E` – 1 Bestandteil:
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…, Kehrwert – Einheit 3. Thema Bruchrechnung, Einheit 1 und 3.“).

### trigonometrische-funktionen – Stufe Sek I; 11 Fertigkeitszeilen, 0 mit Ziel, 11 ohne
- Zeile 25:
  > - Sinus, Kosinus und Tangens als Seitenverhältnisse im rechtwinkligen Dreieck, Wert zu einem Winkel mit dem Taschenrechner im Grad-Modus – Einheit 1 und 2. Thema Trigonometrie, Einheit 1 und 2. [RLP F; LISUM-PH Wiederholungsblock „Berechnungen in Dreiecken“]
  - Klammer: `RLP F; LISUM-PH Wiederholungsblock „Berechnungen in Dreiecken“` – 2 Bestandteile:
    - `RLP F` – RLP ohne Zitat, nicht aufzulösen.
    - `LISUM-PH Wiederholungsblock „Berechnungen in Dreiecken“` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **trigonometrie** (Name „Trigonometrie“ in „…odus – Einheit 1 und 2. Thema Trigonometrie, Einheit 1 und 2.“).
- Zeile 26:
  > - Taschenrechner: Modus DEG und RAD unterscheiden und umstellen, Tasten sin und cos mit dem Winkel dahinter, Umkehrtaste, Wert erst am Ende runden – Einheit 1 bis 3. Kein eigenes Thema. [LISUM-PH „Taschenrechnereinsatz“; P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“]
  - Klammer: `LISUM-PH „Taschenrechnereinsatz“; P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“` – 2 Bestandteile:
    - `LISUM-PH „Taschenrechnereinsatz“` – sonstiges oder keine Klammer, nicht aufzulösen.
    - `P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“` – P10-Typ, aufgelöst:
      - „Taschenrechner in Bogenmaß“: kein Typname in msa/msa-typen.csv
      - Kennung 2021-OS-K3a: Katalogzeile (msa-katalog-kontext.csv): Thema „Trigonometrie im rechtwinkligen Dreieck“, Typ „Seite im rechtwinkligen Dreieck berechnen“ → themen.csv: trigonometrie
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 27:
  > - Koordinatensystem mit vier Quadranten, Punkte eintragen und ablesen, Achsen benennen und einteilen – Einheit 1 bis 4. Thema Symmetrie und Abbildungen, Einheit 1; Zuordnungen, Einheit 3. [RLP E „Zeichnen von Figuren im Koordinatensystem (vier Quadranten)“]
  - Klammer: `RLP E „Zeichnen von Figuren im Koordinatensystem (vier Quadranten)“` – 1 Bestandteil:
    - `RLP E „Zeichnen von Figuren im Koordinatensystem (vier Quadranten)“` – RLP mit Zitat, nicht aufgelöst:
      - „Zeichnen von Figuren im Koordinatensystem (vier Quadranten)“ (Klammer nennt E): im RLP-Text nicht gefunden; Teiltreffer – der Wortanfang „Zeichnen von Figuren im Koordinatensystem (vier“ (6 von 7 Wörtern) steht in: Zeilen 2462–2463 (Block 2434–2485), Niveaustufe am Block: D (Zeile 2448), E (Zeile 2470); Seitenkopf: Themenbereich „Raum und Form“ – Niveaustufen D, E
  - themen.csv wörtlich im Wortlaut: **symmetrie-abbildungen** (thema „Symmetrie und Abbildungen“ in „…ilen – Einheit 1 bis 4. Thema Symmetrie und Abbildungen, Einheit 1; Zuordnungen, Einh…“); **zuordnungen** (Name „Zuordnungen“ in „…e und Abbildungen, Einheit 1; Zuordnungen, Einheit 3.“).
- Zeile 28:
  > - Kreis mit Mittelpunkt und Radius zeichnen, Umfang mit Pi berechnen, Mittelpunktswinkel und Kreisbogen als Anteil des Vollkreises – Einheit 1. Thema Kreis, Einheit 1 und 3. [RLP E; hier Grundlage des Bogenmaßes]
  - Klammer: `RLP E; hier Grundlage des Bogenmaßes` – 2 Bestandteile:
    - `RLP E` – RLP ohne Zitat, nicht aufzulösen.
    - `hier Grundlage des Bogenmaßes` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **kreis** (Name „Kreis“ in „- Kreis mit Mittelpunkt und Radius ze…“).
- Zeile 29:
  > - Winkel messen, zeichnen und benennen, Vollwinkel, gestreckter und rechter Winkel, Winkel über neunzig Grad als stumpfe Winkel – Einheit 1. Thema Winkel und Dreiecke, Einheit 1. [RLP D „Messen von Winkeln“]
  - Klammer: `RLP D „Messen von Winkeln“` – 1 Bestandteil:
    - `RLP D „Messen von Winkeln“` – RLP mit Zitat, nicht aufgelöst:
      - „Messen von Winkeln“ (Klammer nennt D): im RLP-Text nicht gefunden
  - themen.csv wörtlich im Wortlaut: **winkel-dreiecke** (H1 „Winkel und Dreiecke“ in „…pfe Winkel – Einheit 1. Thema Winkel und Dreiecke, Einheit 1.“).
- Zeile 30:
  > - Wertetabelle anlegen, Wertepaare als Punkte eintragen, den Graphen als durchgehende Linie zeichnen, Funktionswert und Argument ablesen, Punktprobe – Einheit 2 bis 4. Thema Quadratische Funktionen, Einheit 1; Lineare Funktionen; Zuordnungen, Einheit 3. [RLP E/F/G]
  - Klammer: `RLP E/F/G` – 1 Bestandteil:
    - `RLP E/F/G` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **lineare-funktionen** (Name „Lineare Funktionen“ in „…tische Funktionen, Einheit 1; Lineare Funktionen; Zuordnungen, Einheit 3.“); **quadratische-funktionen** (Name „Quadratische Funktionen“ in „…robe – Einheit 2 bis 4. Thema Quadratische Funktionen, Einheit 1; Lineare Funktione…“); **zuordnungen** (Name „Zuordnungen“ in „…inheit 1; Lineare Funktionen; Zuordnungen, Einheit 3.“).
- Zeile 31:
  > - Achseneinteilung wählen, wenn beide Achsen verschiedene Einheiten und Schrittweiten haben – Einheit 2 und 4. Thema Zuordnungen, Einheit 3 (Typ „Achseneinteilung wählen“). [RLP G „auch bei verschiedenen Einheiten und Einteilungen der Koordinatenachsen“]
  - Klammer: `RLP G „auch bei verschiedenen Einheiten und Einteilungen der Koordinatenachsen“` – 1 Bestandteil:
    - `RLP G „auch bei verschiedenen Einheiten und Einteilungen der Koordinatenachsen“` – RLP mit Zitat, aufgelöst:
      - „auch bei verschiedenen Einheiten und Einteilungen der Koordinatenachsen“ (Klammer nennt G): Zeilen 2900–2903 (Block 2891–2918), Niveaustufe am Block: G (Zeile 2907); Seitenkopf: Themenbereich „Gleichungen und Funktionen“ – Niveaustufen G, H
  - themen.csv wörtlich im Wortlaut: **einheiten** (Name „Einheiten“ in „…enn beide Achsen verschiedene Einheiten und Schrittweiten haben – Ein…“); **zuordnungen** (Name „Zuordnungen“ in „…aben – Einheit 2 und 4. Thema Zuordnungen, Einheit 3 (Typ „Achseneintei…“).
- Zeile 32:
  > - Parameter in einer Funktionsgleichung erkennen und ihre Wirkung auf den Graphen beschreiben (Streckung, Stauchung, Verschiebung), Graph zu Gleichung zuordnen – Einheit 3. Thema Quadratische Funktionen, Einheit 1 und 2. [RLP G; LS-AA Kl. 9 I 2–3]
  - Klammer: `RLP G; LS-AA Kl. 9 I 2–3` – 2 Bestandteile:
    - `RLP G` – RLP ohne Zitat, nicht aufzulösen.
    - `LS-AA Kl. 9 I 2–3` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 9 I 2–3“ → Klasse 9, Kapitel I „Quadratische Funktionen“, Lerneinheit 2 „Quadratische Funktionen vom Typ f(x) = ax²“, 3 „Scheitelpunktform quadratischer Funktionen“; Fahrplan-Zuordnung (Teil 2): RLP G, Jg. 9, Themenbereich „Gleichungen und Funktionen“ – Terme und Gleichungen; RLP G, Jg. 9, Themenbereich „Gleichungen und Funktionen“ – Zuordnungen und Funktionen; RLP H, Jg. 10, Themenbereich „Gleichungen und Funktionen“ – Terme und Gleichungen; RLP H, Jg. 10, Themenbereich „Gleichungen und Funktionen“ – Zuordnungen und Funktionen; RLP H, Jg. 10, Themenbereich „Daten und Zufall“ – Zählstrategien und Wahrscheinlichkeiten
  - themen.csv wörtlich im Wortlaut: **quadratische-funktionen** (Name „Quadratische Funktionen“ in „…g zuordnen – Einheit 3. Thema Quadratische Funktionen, Einheit 1 und 2.“).
- Zeile 33:
  > - Achsensymmetrisch und punktsymmetrisch als Wörter, Symmetrieachse und Symmetriezentrum am Graphen – Einheit 2. Thema Symmetrie und Abbildungen, Einheit 2 und 3. [RLP C/D; LISUM-PH Begriff „Symmetrieachse“]
  - Klammer: `RLP C/D; LISUM-PH Begriff „Symmetrieachse“` – 2 Bestandteile:
    - `RLP C/D` – RLP ohne Zitat, nicht aufzulösen.
    - `LISUM-PH Begriff „Symmetrieachse“` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **symmetrie-abbildungen** (thema „Symmetrie und Abbildungen“ in „…am Graphen – Einheit 2. Thema Symmetrie und Abbildungen, Einheit 2 und 3.“).
- Zeile 34:
  > - Größtwert, Kleinstwert und Spannweite einer Tabelle entnehmen, Mittelwert bilden – Einheit 4. Thema Daten, Einheit 3. [RLP E; Grundlage von Mittellinie und Amplitude]
  - Klammer: `RLP E; Grundlage von Mittellinie und Amplitude` – 2 Bestandteile:
    - `RLP E` – RLP ohne Zitat, nicht aufzulösen.
    - `Grundlage von Mittellinie und Amplitude` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **daten** (Name „Daten“ in „…ert bilden – Einheit 4. Thema Daten, Einheit 3.“).
- Zeile 35:
  > - Bruchteile eines Vollkreises als Bruch und als Dezimalzahl (halb, viertel, drittel) – Einheit 1. Thema Bruchrechnung, Einheit 1; Kreis, Einheit 3. [RLP C „Nutzen von gebräuchlichen Bruchzahlen bei Größenangaben“]
  - Klammer: `RLP C „Nutzen von gebräuchlichen Bruchzahlen bei Größenangaben“` – 1 Bestandteil:
    - `RLP C „Nutzen von gebräuchlichen Bruchzahlen bei Größenangaben“` – RLP mit Zitat, nicht aufgelöst:
      - „Nutzen von gebräuchlichen Bruchzahlen bei Größenangaben“ (Klammer nennt C): im RLP-Text nicht gefunden; Teiltreffer – der Wortanfang „Nutzen von gebräuchlichen Bruchzahlen“ (4 von 6 Wörtern) steht in: Zeile 2061 (Block 2018–2066), Niveaustufe am Block: A (Zeile 2022), B (Zeile 2033), C (Zeile 2056); Seitenkopf: Themenbereich „Größen und Messen“ – Niveaustufen A, B, C
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…, drittel) – Einheit 1. Thema Bruchrechnung, Einheit 1; Kreis, Einheit 3.…“); **kreis** (Name „Kreis“ in „…ema Bruchrechnung, Einheit 1; Kreis, Einheit 3.“).

### zinsrechnung – Stufe Sek I; 8 Fertigkeitszeilen, 1 mit Ziel, 7 ohne
- Zeile 21:
  > - Prozentwert berechnen: Prozentsatz als Dezimalzahl mal Grundwert oder Ein-Prozent-Weg (ein Prozent = Grundwert geteilt durch hundert, dann mal p) – Einheit 1 und 2. Thema Prozentrechnung, Einheit 3. [RLP E „Nutzen von Prozentsätzen als Operatoren“; P10 2015-OS-B1e Verfahren „Kapital mal Zinssatz als Dezimalzahl“]
  - Klammer: `RLP E „Nutzen von Prozentsätzen als Operatoren“; P10 2015-OS-B1e Verfahren „Kapital mal Zinssatz als Dezimalzahl“` – 2 Bestandteile:
    - `RLP E „Nutzen von Prozentsätzen als Operatoren“` – RLP mit Zitat, aufgelöst:
      - „Nutzen von Prozentsätzen als Operatoren“ (Klammer nennt E): Zeile 1916 (Block 1897–1916), Niveaustufe am Block: E (Zeile 1907); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen D, E
    - `P10 2015-OS-B1e Verfahren „Kapital mal Zinssatz als Dezimalzahl“` – P10-Typ, aufgelöst:
      - „Kapital mal Zinssatz als Dezimalzahl“: kein Typname in msa/msa-typen.csv
      - Kennung 2015-OS-B1e: Katalogzeile (msa-katalog-basis.csv): Thema „Zinsrechnung“, Typ „Prozentwert berechnen“ → themen.csv: zinsrechnung
  - themen.csv wörtlich im Wortlaut: **prozentrechnung** (Name „Prozentrechnung“ in „…l p) – Einheit 1 und 2. Thema Prozentrechnung, Einheit 3.“).
- Zeile 22:
  > - Prozentsatz berechnen: Teil geteilt durch Ganzes, Dezimalzahl in Prozent schreiben (Komma zwei Stellen nach rechts) – Einheit 1. Thema Prozentrechnung, Einheit 2; Einheit 1 (Dezimalzahl ↔ Prozent). [RLP E; P10 2014-OS-B1e Fehlerquelle „Komma verschoben“]
  - Klammer: `RLP E; P10 2014-OS-B1e Fehlerquelle „Komma verschoben“` – 2 Bestandteile:
    - `RLP E` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2014-OS-B1e Fehlerquelle „Komma verschoben“` – P10-Typ, aufgelöst:
      - „Komma verschoben“: kein Typname in msa/msa-typen.csv
      - Kennung 2014-OS-B1e: Katalogzeile (msa-katalog-basis.csv): Thema „Zinsrechnung“, Typ „Prozentsatz berechnen“ → themen.csv: zinsrechnung
  - themen.csv wörtlich im Wortlaut: **prozentrechnung** (Name „Prozentrechnung“ in „…ch rechts) – Einheit 1. Thema Prozentrechnung, Einheit 2; Einheit 1 (Dezima…“).
- Zeile 23:
  > - Grundwert berechnen: Prozentwert geteilt durch p, mal hundert – Einheit 1 (Kapital aus Zinsen). Thema Prozentrechnung, Einheit 4. [RLP E „Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“]
  - Klammer: `RLP E „Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“` – 1 Bestandteil:
    - `RLP E „Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“` – RLP mit Zitat, aufgelöst:
      - „Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ (Klammer nennt E): Zeilen 1838–1840 (Block 1838–1860), Niveaustufe am Block: E (Zeile 1850); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen D, E
  - themen.csv wörtlich im Wortlaut: **prozentrechnung** (Name „Prozentrechnung“ in „…1 (Kapital aus Zinsen). Thema Prozentrechnung, Einheit 4.“).
- Zeile 24:
  > - Erhöhung um p % als Wachstumsfaktor: neuer Wert = alter Wert mal (eins plus p Hundertstel) – Einheit 2. Thema Prozentrechnung, Einheit 5. [RLP F; P10 2018-OS-K2c Muster „mal 1,08 je Jahr“; LISUM-PH Hinweis Operatormethode → Wachstumsfaktor]
  - Klammer: `RLP F; P10 2018-OS-K2c Muster „mal 1,08 je Jahr“; LISUM-PH Hinweis Operatormethode → Wachstumsfaktor` – 3 Bestandteile:
    - `RLP F` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2018-OS-K2c Muster „mal 1,08 je Jahr“` – P10-Typ, aufgelöst:
      - „mal 1,08 je Jahr“: kein Typname in msa/msa-typen.csv
      - Kennung 2018-OS-K2c: beispiel_id des Typs „Zeitpunkt für Schwellenwert bei Wachstum bestimmen“ in msa/msa-typen.csv, Thema „Exponentialfunktionen und Wachstum“ → themen.csv: potenz-exponentialfunktionen; Katalogzeile (msa-katalog-kontext.csv): Thema „Exponentialfunktionen und Wachstum“, Typ „Zeitpunkt für Schwellenwert bei Wachstum bestimmen“ → themen.csv: potenz-exponentialfunktionen
    - `LISUM-PH Hinweis Operatormethode → Wachstumsfaktor` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **prozentrechnung** (Name „Prozentrechnung“ in „…ndertstel) – Einheit 2. Thema Prozentrechnung, Einheit 5.“).
- Zeile 25:
  > - Dezimalzahlen addieren und multiplizieren, Euro-Beträge auf Cent runden (zwei Dezimalen), Ergebnis mit ≈ – Einheit 1 und 2. Thema Bruchrechnung, Einheit 2 und 4; Brüche und Dezimalzahlen, Einheit 5. [RLP D/E; P10 2014-OS-K3b Cent-Beträge in der Tabelle]
  - Klammer: `RLP D/E; P10 2014-OS-K3b Cent-Beträge in der Tabelle` – 2 Bestandteile:
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2014-OS-K3b Cent-Beträge in der Tabelle` – P10-Typ, aufgelöst:
      - Kennung 2014-OS-K3b: beispiel_id des Typs „Guthabentabelle mit Zinsen ergänzen“ in msa/msa-typen.csv, Thema „Zinsrechnung“ → themen.csv: zinsrechnung; Katalogzeile (msa-katalog-kontext.csv): Thema „Zinsrechnung“, Typ „Guthabentabelle mit Zinsen ergänzen“, Nebentypen „Prozentwert berechnen“ → themen.csv: zinsrechnung
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…it ≈ – Einheit 1 und 2. Thema Bruchrechnung, Einheit 2 und 4; Brüche und…“); **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…uchrechnung, Einheit 2 und 4; Brüche und Dezimalzahlen, Einheit 5.“).
- Zeile 26:
  > - Dreisatz und fester Faktor („pro Monat“, „pro Tag“) – Einheit 1 (Monats- und Tageszinsen). Thema Zuordnungen, Einheit 2. [RLP D/E; MSK S5A]
  - Klammer: `RLP D/E; MSK S5A` – 2 Bestandteile:
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
    - `MSK S5A` – MSK-Code, nicht aufzulösen:
      - S5A: Bausteintitel in _quellen.md „Proportionale Zusammenhänge“
  - themen.csv wörtlich im Wortlaut: **zuordnungen** (Name „Zuordnungen“ in „…nats- und Tageszinsen). Thema Zuordnungen, Einheit 2.“).
- Zeile 28:
  > - Tabelle lesen und fortschreiben: Zeilen und Spalten, Feld aus Zeile und Spalte, „von der Vorzeile zur nächsten“ – Einheit 2. Thema Daten, Einheit 1. [RLP D; P10 2014-OS-K3a, 2014-OS-K3b Material Tabelle]
  - Klammer: `RLP D; P10 2014-OS-K3a, 2014-OS-K3b Material Tabelle` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2014-OS-K3a, 2014-OS-K3b Material Tabelle` – P10-Typ, aufgelöst:
      - Kennung 2014-OS-K3a: Katalogzeile (msa-katalog-kontext.csv): Thema „Zinsrechnung“, Typ „Prozentwert berechnen“ → themen.csv: zinsrechnung
      - Kennung 2014-OS-K3b: beispiel_id des Typs „Guthabentabelle mit Zinsen ergänzen“ in msa/msa-typen.csv, Thema „Zinsrechnung“ → themen.csv: zinsrechnung; Katalogzeile (msa-katalog-kontext.csv): Thema „Zinsrechnung“, Typ „Guthabentabelle mit Zinsen ergänzen“, Nebentypen „Prozentwert berechnen“ → themen.csv: zinsrechnung
  - themen.csv wörtlich im Wortlaut: **daten** (Name „Daten“ in „…nächsten“ – Einheit 2. Thema Daten, Einheit 1.“).

### daten – Stufe Sek I + II; 9 Fertigkeitszeilen, 3 mit Ziel, 6 ohne
- Zeile 33:
  > - Zahlen ordnen, auch Dezimalzahlen (9,5 < 9,6 < 9,7), und Skalen ablesen – Einheit 2 und 4. Thema Brüche und Dezimalzahlen, Einheit 4 und 5. [RLP D; P10 2024-OS-B1h, 2019-OS-B1i]
  - Klammer: `RLP D; P10 2024-OS-B1h, 2019-OS-B1i` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2024-OS-B1h, 2019-OS-B1i` – P10-Typ, aufgelöst:
      - Kennung 2024-OS-B1h: beispiel_id des Typs „Median bestimmen“ in msa/msa-typen.csv, Thema „Kenngrößen“ → themen.csv: daten; Katalogzeile (msa-katalog-basis.csv): Thema „Kenngrößen“, Typ „Median bestimmen“ → themen.csv: daten
      - Kennung 2019-OS-B1i: Katalogzeile (msa-katalog-basis.csv): Thema „Kenngrößen“, Typ „Spannweite berechnen“ → themen.csv: daten
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…esen – Einheit 2 und 4. Thema Brüche und Dezimalzahlen, Einheit 4 und 5.“).
- Zeile 34:
  > - Addieren und Dividieren mit Dezimalzahlen (Taschenrechner) und Runden – Einheit 4. Thema Bruchrechnung, Einheit 4; Brüche und Dezimalzahlen, Einheit 5. [P10 2021-OS-B1f, 2015-OS-K7a]
  - Klammer: `P10 2021-OS-B1f, 2015-OS-K7a` – 1 Bestandteil:
    - `P10 2021-OS-B1f, 2015-OS-K7a` – P10-Typ, aufgelöst:
      - Kennung 2021-OS-B1f: Katalogzeile (msa-katalog-basis.csv): Thema „Kenngrößen“, Typ „Arithmetisches Mittel berechnen“ → themen.csv: daten
      - Kennung 2015-OS-K7a: Katalogzeile (msa-katalog-kontext.csv): Thema „Kenngrößen“, Typ „Arithmetisches Mittel berechnen“ → themen.csv: daten
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…und Runden – Einheit 4. Thema Bruchrechnung, Einheit 4; Brüche und Dezima…“); **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…ema Bruchrechnung, Einheit 4; Brüche und Dezimalzahlen, Einheit 5.“).
- Zeile 35:
  > - Prozentsatz berechnen (Teil geteilt durch Ganzes), Prozent ↔ Dezimalzahl, Rest zu hundert Prozent – Einheit 1, 3 und 5. Thema Prozentrechnung, Einheit 1 und 2. [RLP E; P10 2025-OS-K6b, 2021-OS-K5b]
  - Klammer: `RLP E; P10 2025-OS-K6b, 2021-OS-K5b` – 2 Bestandteile:
    - `RLP E` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2025-OS-K6b, 2021-OS-K5b` – P10-Typ, aufgelöst:
      - Kennung 2025-OS-K6b: beispiel_id des Typs „Kreisdiagramm zeichnen“ in msa/msa-typen.csv, Thema „Daten darstellen“ → themen.csv: daten; Katalogzeile (msa-katalog-kontext.csv): Thema „Daten darstellen“, Typ „Prozentsatz berechnen“, Nebentypen „Kreisdiagramm zeichnen“ → themen.csv: daten
      - Kennung 2021-OS-K5b: beispiel_id des Typs „Fehlenden Prozentanteil ergänzen“ in msa/msa-typen.csv, Thema „Prozentrechnung“ → themen.csv: prozentrechnung; Katalogzeile (msa-katalog-kontext.csv): Thema „Diagramme lesen und beurteilen“, Typ „Fehlenden Prozentanteil ergänzen“, Nebentypen „Sektor im Kreisdiagramm zuordnen“ → themen.csv: daten
  - themen.csv wörtlich im Wortlaut: **prozentrechnung** (Name „Prozentrechnung“ in „…t – Einheit 1, 3 und 5. Thema Prozentrechnung, Einheit 1 und 2.“).
- Zeile 36:
  > - Winkel mit dem Geodreieck zeichnen; Winkel als Anteil vom Vollkreis (90° ist ein Viertel) – Einheit 3. Thema Winkel und Dreiecke, Einheit 1; Kreis, Einheit 3. [RLP D/E]
  - Klammer: `RLP D/E` – 1 Bestandteil:
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **kreis** (Name „Kreis“ in „…nkel und Dreiecke, Einheit 1; Kreis, Einheit 3.“); **winkel-dreiecke** (H1 „Winkel und Dreiecke“ in „…n Viertel) – Einheit 3. Thema Winkel und Dreiecke, Einheit 1; Kreis, Einheit 3.…“).
- Zeile 37:
  > - Längen in Zentimetern und Millimetern abtragen – Einheit 3 (Streifen). [P10 2018-OS-K3c]
  - Klammer: `P10 2018-OS-K3c` – 1 Bestandteil:
    - `P10 2018-OS-K3c` – P10-Typ, aufgelöst:
      - Kennung 2018-OS-K3c: beispiel_id des Typs „Streifendiagramm zeichnen“ in msa/msa-typen.csv, Thema „Daten darstellen“ → themen.csv: daten; Katalogzeile (msa-katalog-kontext.csv): Thema „Daten darstellen“, Typ „Streifendiagramm zeichnen“ → themen.csv: daten
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.
- Zeile 38:
  > - Bruchteil und Vielfaches einer Zahl („ein Drittel mehr“, „doppelt so viel“) – Einheit 5. Thema Brüche und Dezimalzahlen, Einheit 1. [P10 2020-OS-K2d]
  - Klammer: `P10 2020-OS-K2d` – 1 Bestandteil:
    - `P10 2020-OS-K2d` – P10-Typ, aufgelöst:
      - Kennung 2020-OS-K2d: Katalogzeile (msa-katalog-kontext.csv): Thema „Kenngrößen“, Typ „Spannweite berechnen“, Nebentypen „Prozentuale Veränderung berechnen|Behauptung prüfen“ → themen.csv: daten
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…so viel“) – Einheit 5. Thema Brüche und Dezimalzahlen, Einheit 1.“).

### einheiten – Stufe Sek I + II; 11 Fertigkeitszeilen, 2 mit Ziel, 9 ohne
- Zeile 28:
  > - Multiplizieren und Dividieren mit zehn, hundert und tausend als Kommaverschiebung, auch bei Dezimalzahlen – Einheit 1 bis 4. Thema Bruchrechnung, Einheit 5; Brüche und Dezimalzahlen, Einheit 4. [RLP D „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln“; P10 2019-OS-B1b, 2022-OS-B1h Fehlerquellen]
  - Klammer: `RLP D „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln“; P10 2019-OS-B1b, 2022-OS-B1h Fehlerquellen` – 2 Bestandteile:
    - `RLP D „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln“` – RLP mit Zitat, aufgelöst:
      - „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln“ (Klammer nennt D): Zeilen 2138–2139 (Block 2119–2159), Niveaustufe am Block: D (Zeile 2133), E (Zeile 2155); Seitenkopf: Themenbereich „Größen und Messen“ – Niveaustufen D, E
    - `P10 2019-OS-B1b, 2022-OS-B1h Fehlerquellen` – P10-Typ, aufgelöst:
      - Kennung 2019-OS-B1b: Katalogzeile (msa-katalog-basis.csv): Thema „Einheiten umrechnen“, Typ „Größen vergleichen“ → themen.csv: einheiten
      - Kennung 2022-OS-B1h: beispiel_id des Typs „Portionen aus Gesamtmenge berechnen“ in msa/msa-typen.csv, Thema „Einheiten umrechnen“ → themen.csv: einheiten; Katalogzeile (msa-katalog-basis.csv): Thema „Einheiten umrechnen“, Typ „Portionen aus Gesamtmenge berechnen“ → themen.csv: einheiten
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…hlen – Einheit 1 bis 4. Thema Bruchrechnung, Einheit 5; Brüche und Dezima…“); **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…ema Bruchrechnung, Einheit 5; Brüche und Dezimalzahlen, Einheit 4.“).
- Zeile 29:
  > - Stellenwerttafel lesen und schreiben, Nullen an der richtigen Stelle ergänzen (null Komma null sechs Meter; eintausendfünfhundert Milliliter) – Einheit 1 und Einheit 3. Thema Brüche und Dezimalzahlen, Einheit 4. [RLP D; MSK D2B]
  - Klammer: `RLP D; MSK D2B` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `MSK D2B` – MSK-Code, nicht aufzulösen:
      - D2B: Bausteintitel in _quellen.md „Dezimalzahlen vergleichen und ordnen“
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…inheit 1 und Einheit 3. Thema Brüche und Dezimalzahlen, Einheit 4.“).
- Zeile 30:
  > - Dezimalzahlen mit einer Zahl malnehmen und durch eine Zahl teilen, auch schriftlich oder mit dem Taschenrechner – Einheit 1, Einheit 2 und Einheit 4. Thema Bruchrechnung, Einheit 4 und 5. [P10 2016-OS-K3a, 2016-OS-K3d Verfahren]
  - Klammer: `P10 2016-OS-K3a, 2016-OS-K3d Verfahren` – 1 Bestandteil:
    - `P10 2016-OS-K3a, 2016-OS-K3d Verfahren` – P10-Typ, aufgelöst:
      - Kennung 2016-OS-K3a: beispiel_id des Typs „Längeneinheit mit Faktor umrechnen“ in msa/msa-typen.csv, Thema „Einheiten umrechnen“ → themen.csv: einheiten; Katalogzeile (msa-katalog-kontext.csv): Thema „Einheiten umrechnen“, Typ „Längeneinheit mit Faktor umrechnen“, Nebentypen „Behauptung prüfen“ → themen.csv: einheiten
      - Kennung 2016-OS-K3d: beispiel_id des Typs „Volumen aus Masse und Dichte berechnen“ in msa/msa-typen.csv, Thema „Einheiten umrechnen“ → themen.csv: einheiten; Katalogzeile (msa-katalog-kontext.csv): Thema „Einheiten umrechnen“, Typ „Volumen aus Masse und Dichte berechnen“ → themen.csv: einheiten
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…inheit 2 und Einheit 4. Thema Bruchrechnung, Einheit 4 und 5.“).
- Zeile 31:
  > - Dezimalzahlen vergleichen und ordnen (stellenweise, Nullen anhängen) – Einheit 1 und 3. Thema Brüche und Dezimalzahlen, Einheit 5. [RLP D; P10 2019-OS-B1b]
  - Klammer: `RLP D; P10 2019-OS-B1b` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `P10 2019-OS-B1b` – P10-Typ, aufgelöst:
      - Kennung 2019-OS-B1b: Katalogzeile (msa-katalog-basis.csv): Thema „Einheiten umrechnen“, Typ „Größen vergleichen“ → themen.csv: einheiten
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…gen) – Einheit 1 und 3. Thema Brüche und Dezimalzahlen, Einheit 5.“).
- Zeile 32:
  > - Bruchteil einer Größe bilden (ein Viertel von einem Kilogramm; die Hälfte einer Stunde) – Einheit 2 und 4. Thema Brüche und Dezimalzahlen, Einheit 1. [RLP D „Erfassen und Bilden von Bruchteilen von Größen“]
  - Klammer: `RLP D „Erfassen und Bilden von Bruchteilen von Größen“` – 1 Bestandteil:
    - `RLP D „Erfassen und Bilden von Bruchteilen von Größen“` – RLP mit Zitat, aufgelöst:
      - „Erfassen und Bilden von Bruchteilen von Größen“ (Klammer nennt D): Zeile 2136 (Block 2119–2159), Niveaustufe am Block: D (Zeile 2133), E (Zeile 2155); Seitenkopf: Themenbereich „Größen und Messen“ – Niveaustufen D, E
  - themen.csv wörtlich im Wortlaut: **brueche-dezimalzahlen** (thema „Brüche und Dezimalzahlen“ in „…nde) – Einheit 2 und 4. Thema Brüche und Dezimalzahlen, Einheit 1.“).
- Zeile 33:
  > - Prozentwert einer Größe berechnen (zehn Prozent eines Volumens) – Einheit 4. Thema Prozentrechnung, Einheit 3. [P10 2019-OS-K4c Voraussetzung „Prozentwert berechnen“]
  - Klammer: `P10 2019-OS-K4c Voraussetzung „Prozentwert berechnen“` – 1 Bestandteil:
    - `P10 2019-OS-K4c Voraussetzung „Prozentwert berechnen“` – P10-Typ, aufgelöst:
      - Typ „Prozentwert berechnen“ in msa/msa-typen.csv: Thema „Prozentrechnung“ (Leitidee Zahlen und Operationen) → themen.csv: prozentrechnung
      - Kennung 2019-OS-K4c: beispiel_id des Typs „Masse aus Volumen und Dichte berechnen“ in msa/msa-typen.csv, Thema „Einheiten umrechnen“ → themen.csv: einheiten; beispiel_id des Typs „Flächeninhalt Dreieck berechnen“ in msa/msa-typen.csv, Thema „Flächeninhalt und Umfang“ → themen.csv: flaechen; beispiel_id des Typs „Volumen Prisma berechnen“ in msa/msa-typen.csv, Thema „Volumen und Oberfläche“ → themen.csv: koerper; Katalogzeile (msa-katalog-kontext.csv): Thema „Volumen und Oberfläche“, Typ „Flächeninhalt Dreieck berechnen“, Nebentypen „Volumen Prisma berechnen|Masse aus Volumen und Dichte berechnen“ → themen.csv: koerper
  - themen.csv wörtlich im Wortlaut: **prozentrechnung** (Name „Prozentrechnung“ in „…Volumens) – Einheit 4. Thema Prozentrechnung, Einheit 3.“).
- Zeile 34:
  > - Formel nach einer Größe umstellen (aus einer Verhältnisgleichung die gesuchte Größe isolieren) – Einheit 4 (Dichte). Thema Lineare Gleichungen, Einheit 2. [RLP E „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“; P10 2016-OS-K3d Voraussetzung „Dichteformel umstellen“]
  - Klammer: `RLP E „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“; P10 2016-OS-K3d Voraussetzung „Dichteformel umstellen“` – 2 Bestandteile:
    - `RLP E „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“` – RLP mit Zitat, aufgelöst:
      - „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“ (Klammer nennt E): Zeilen 2747–2748 (Block 2739–2754), Niveaustufe am Block: E (Zeile 2746); Seitenkopf: Themenbereich „Gleichungen und Funktionen“ – Niveaustufen D, E, F
    - `P10 2016-OS-K3d Voraussetzung „Dichteformel umstellen“` – P10-Typ, aufgelöst:
      - „Dichteformel umstellen“: kein Typname in msa/msa-typen.csv
      - Kennung 2016-OS-K3d: beispiel_id des Typs „Volumen aus Masse und Dichte berechnen“ in msa/msa-typen.csv, Thema „Einheiten umrechnen“ → themen.csv: einheiten; Katalogzeile (msa-katalog-kontext.csv): Thema „Einheiten umrechnen“, Typ „Volumen aus Masse und Dichte berechnen“ → themen.csv: einheiten
  - themen.csv wörtlich im Wortlaut: **lineare-gleichungen** (Name „Lineare Gleichungen“ in „…) – Einheit 4 (Dichte). Thema Lineare Gleichungen, Einheit 2.“).
- Zeile 35:
  > - Fläche eines Rechtecks und eines Dreiecks berechnen (für den Materialbedarf) – Einheit 4. Thema Flächen, Einheit 1 und 3. [P10 2015-OS-K6d, 2019-OS-K4c]
  - Klammer: `P10 2015-OS-K6d, 2019-OS-K4c` – 1 Bestandteil:
    - `P10 2015-OS-K6d, 2019-OS-K4c` – P10-Typ, aufgelöst:
      - Kennung 2015-OS-K6d: beispiel_id des Typs „Materialbedarf aus Fläche berechnen“ in msa/msa-typen.csv, Thema „Einheiten umrechnen“ → themen.csv: einheiten; Katalogzeile (msa-katalog-kontext.csv): Thema „Einheiten umrechnen“, Typ „Materialbedarf aus Fläche berechnen“, Nebentypen „Behauptung prüfen“ → themen.csv: einheiten
      - Kennung 2019-OS-K4c: beispiel_id des Typs „Masse aus Volumen und Dichte berechnen“ in msa/msa-typen.csv, Thema „Einheiten umrechnen“ → themen.csv: einheiten; beispiel_id des Typs „Flächeninhalt Dreieck berechnen“ in msa/msa-typen.csv, Thema „Flächeninhalt und Umfang“ → themen.csv: flaechen; beispiel_id des Typs „Volumen Prisma berechnen“ in msa/msa-typen.csv, Thema „Volumen und Oberfläche“ → themen.csv: koerper; Katalogzeile (msa-katalog-kontext.csv): Thema „Volumen und Oberfläche“, Typ „Flächeninhalt Dreieck berechnen“, Nebentypen „Volumen Prisma berechnen|Masse aus Volumen und Dichte berechnen“ → themen.csv: koerper
  - themen.csv wörtlich im Wortlaut: **flaechen** (H1 „Flächen“ in „…ialbedarf) – Einheit 4. Thema Flächen, Einheit 1 und 3.“).
- Zeile 36:
  > - Skala am Lineal und an der Uhr lesen (Untereinheiten) – Einheit 1 und 2. Thema Winkel und Dreiecke, Einheit 1 (Skala am Geodreieck). [RLP C „Erklären von Einheiten und Untereinheiten zur Beschreibung einer entsprechenden Skala“]
  - Klammer: `RLP C „Erklären von Einheiten und Untereinheiten zur Beschreibung einer entsprechenden Skala“` – 1 Bestandteil:
    - `RLP C „Erklären von Einheiten und Untereinheiten zur Beschreibung einer entsprechenden Skala“` – RLP mit Zitat, aufgelöst:
      - „Erklären von Einheiten und Untereinheiten zur Beschreibung einer entsprechenden Skala“ (Klammer nennt C): Zeilen 2060–2062 (Block 2018–2066), Niveaustufe am Block: A (Zeile 2022), B (Zeile 2033), C (Zeile 2056); Seitenkopf: Themenbereich „Größen und Messen“ – Niveaustufen A, B, C
  - themen.csv wörtlich im Wortlaut: **winkel-dreiecke** (H1 „Winkel und Dreiecke“ in „…ten) – Einheit 1 und 2. Thema Winkel und Dreiecke, Einheit 1 (Skala am Geodreie…“).

### lineare-gleichungssysteme – Stufe Sek I + II; 10 Fertigkeitszeilen, 3 mit Ziel, 7 ohne
- Zeile 31:
  > - Lineare Gleichung mit Klammern, Dezimalzahlen und x auf beiden Seiten lösen, Schreibform mit Strich – Einheit 2 bis 4. Thema Lineare Gleichungen, Einheit 2 und 3. [RLP E/F; LS-AA Kl. 7 IV 5]
  - Klammer: `RLP E/F; LS-AA Kl. 7 IV 5` – 2 Bestandteile:
    - `RLP E/F` – RLP ohne Zitat, nicht aufzulösen.
    - `LS-AA Kl. 7 IV 5` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 7 IV 5“ → Klasse 7, Kapitel IV „Terme und Gleichungen“, Lerneinheit 5 „Gleichungen mit Äquivalenzumformungen lösen“; Fahrplan-Zuordnung (Teil 2): RLP E, Jg. 7, Themenbereich „Gleichungen und Funktionen“ – Terme und Gleichungen; RLP H, Jg. 10, Themenbereich „Gleichungen und Funktionen“ – Terme und Gleichungen
  - themen.csv wörtlich im Wortlaut: **lineare-gleichungen** (Name „Lineare Gleichungen“ in „…rich – Einheit 2 bis 4. Thema Lineare Gleichungen, Einheit 2 und 3.“).
- Zeile 32:
  > - Lösung durch Einsetzen prüfen, Ergebnis mit (wA)/(fA) – alle Einheiten. Thema Lineare Gleichungen, Einheit 1. [RLP E „Prüfen einer Lösung“]
  - Klammer: `RLP E „Prüfen einer Lösung“` – 1 Bestandteil:
    - `RLP E „Prüfen einer Lösung“` – RLP mit Zitat, aufgelöst:
      - „Prüfen einer Lösung“ (Klammer nennt E): Zeile 2750 (Block 2739–2754), Niveaustufe am Block: E (Zeile 2746); Seitenkopf: Themenbereich „Gleichungen und Funktionen“ – Niveaustufen D, E, F
  - themen.csv wörtlich im Wortlaut: **einheiten** (Name „Einheiten“ in „…Ergebnis mit (wA)/(fA) – alle Einheiten. Thema Lineare Gleichungen, E…“); **lineare-gleichungen** (Name „Lineare Gleichungen“ in „…/(fA) – alle Einheiten. Thema Lineare Gleichungen, Einheit 1.“).
- Zeile 33:
  > - Gleichung nach einer Variablen umstellen (Formel umstellen: ax + by = c nach y) – Einheit 1 und 2. Thema Lineare Gleichungen, Einheit 4. [RLP E „Umstellen von Formeln“]
  - Klammer: `RLP E „Umstellen von Formeln“` – 1 Bestandteil:
    - `RLP E „Umstellen von Formeln“` – RLP mit Zitat, aufgelöst:
      - „Umstellen von Formeln“ (Klammer nennt E): Zeile 2748 (Block 2739–2754), Niveaustufe am Block: E (Zeile 2746); Seitenkopf: Themenbereich „Gleichungen und Funktionen“ – Niveaustufen D, E, F
  - themen.csv wörtlich im Wortlaut: **lineare-gleichungen** (Name „Lineare Gleichungen“ in „…h y) – Einheit 1 und 2. Thema Lineare Gleichungen, Einheit 4.“).
- Zeile 34:
  > - Gerade aus der Gleichung zeichnen (n und Steigungsdreieck), Punkt ablesen, Lage zweier Geraden (parallel bei gleicher Steigung) – Einheit 1. Thema Lineare Funktionen, Einheit 2 und 4. [RLP F]
  - Klammer: `RLP F` – 1 Bestandteil:
    - `RLP F` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **lineare-funktionen** (Name „Lineare Funktionen“ in „…Steigung) – Einheit 1. Thema Lineare Funktionen, Einheit 2 und 4.“); **geraden** (Name „Geraden“ in „…), Punkt ablesen, Lage zweier Geraden (parallel bei gleicher Steigu…“).
- Zeile 35:
  > - Klammer ausmultiplizieren (Zahl mal Klammer, Minus vor der Klammer), Terme mit zwei Variablen zusammenfassen – Einheit 2 und 3. Thema Terme. [RLP E/F Distributivgesetz; LS-AA Kl. 8 II]
  - Klammer: `RLP E/F Distributivgesetz; LS-AA Kl. 8 II` – 2 Bestandteile:
    - `RLP E/F Distributivgesetz` – RLP ohne Zitat, nicht aufzulösen.
    - `LS-AA Kl. 8 II` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 8 II“ → Klasse 8, Kapitel II „Terme mit mehreren Variablen“ (Lerneinheiten: 1 Wiederholung: Terme mit einer Variablen · 2 Terme mit mehreren Variablen · 3 Multiplizieren von Summen · 4 Binomische Formeln); Fahrplan-Zuordnung (Teil 2): RLP F, Jg. 8, Themenbereich „Gleichungen und Funktionen“ – Terme und Gleichungen
  - themen.csv wörtlich im Wortlaut: **terme** (Name „Terme“ in „…mmer, Minus vor der Klammer), Terme mit zwei Variablen zusammenfa…“).
- Zeile 36:
  > - Rechnen mit Dezimalzahlen (Geld) und negativen Zahlen, Division mit dem Taschenrechner – Einheit 2 bis 4. Thema Bruchrechnung Einheit 4, Rationale Zahlen. [RLP D/E]
  - Klammer: `RLP D/E` – 1 Bestandteil:
    - `RLP D/E` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **bruchrechnung** (Name „Bruchrechnung“ in „…hner – Einheit 2 bis 4. Thema Bruchrechnung Einheit 4, Rationale Zahlen.…“); **rationale-zahlen** (Name „Rationale Zahlen“ in „…hema Bruchrechnung Einheit 4, Rationale Zahlen.“).
- Zeile 37:
  > - Gleichung mit einer Variablen aus einem Sachverhalt aufstellen (Preis · Anzahl, „zusammen“) – Einheit 4. Thema Lineare Gleichungen, Einheit 4. [P10 „Lineare Gleichung aus Sachverhalt aufstellen“]
  - Klammer: `P10 „Lineare Gleichung aus Sachverhalt aufstellen“` – 1 Bestandteil:
    - `P10 „Lineare Gleichung aus Sachverhalt aufstellen“` – P10-Typ, aufgelöst:
      - Typ „Lineare Gleichung aus Sachverhalt aufstellen“ in msa/msa-typen.csv: Thema „Lineare Gleichungen“ (Leitidee Gleichungen und Funktionen) → themen.csv: lineare-gleichungen
  - themen.csv wörtlich im Wortlaut: **lineare-gleichungen** (Name „Lineare Gleichungen“ in „…zusammen“) – Einheit 4. Thema Lineare Gleichungen, Einheit 4.“).

### ableitung-und-aenderungsrate – Stufe Sek II; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### ableitungsgraph-und-funktionsgraph – Stufe Sek II; 0 Fertigkeitszeilen, 0 mit Ziel, 0 ohne
Keine Fertigkeitszeile.

### ableitungsregeln – Stufe Sek II; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### abstaende – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### bedingte-wahrscheinlichkeit-und-bayes – Stufe Sek II; 5 Fertigkeitszeilen, 5 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### binomialverteilung – Stufe Sek II; 8 Fertigkeitszeilen, 7 mit Ziel, 1 ohne
- Zeile 36:
  > - Rechnerfunktionen für die Binomialverteilung (Einzelwahrscheinlichkeit und kumulierte Wahrscheinlichkeit, je nach Gerät binompdf und binomcdf) bedienen oder die Tabelle der summierten Binomialverteilung lesen (Spalte p, Zeile k; bei p über ein Halb Treffer und Niete tauschen) – Werkzeug für Einheit 2 bis 5, Prüfungsteil B. **Ermessen:** keine amtliche Eingangsvoraussetzung nennt die Rechnerbedienung; gesetzt, weil vierunddreißig Zeilen der Rohdatei den Rechner voraussetzen (Typen „… mit dem Rechner ermitteln“) und Berlin vom Taschenrechner verlangt, dass „Werte der Binomialverteilungen ermittelt werden können“ (abitur-vokabular.md, Abschnitt Geltung, Anmerkung). [Ermessen; Rohdatei; abitur-vokabular.md Abschnitt Geltung]
  - Klammer: `Ermessen; Rohdatei; abitur-vokabular.md Abschnitt Geltung` – 3 Bestandteile:
    - `Ermessen` – sonstiges oder keine Klammer, nicht aufzulösen.
    - `Rohdatei` – sonstiges oder keine Klammer, nicht aufzulösen.
    - `abitur-vokabular.md Abschnitt Geltung` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **wahrscheinlichkeit** (Name „Wahrscheinlichkeit“ in „…scheinlichkeit und kumulierte Wahrscheinlichkeit, je nach Gerät binompdf und b…“).

### ebenen – Stufe Sek II; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### extremalprobleme – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### flaecheninhalt-durch-integration – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### flaecheninhalt-und-volumen-im-raum – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### funktionsklassen-und-eigenschaften – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### funktionsscharen-und-ortskurven – Stufe Sek II; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### geraden – Stufe Sek II; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### gleichungen-loesen – Stufe Sek II; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### grenzwerte-und-verhalten-im-unendlichen – Stufe Sek II; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### hypergeometrische-verteilung – Stufe Sek II; 4 Fertigkeitszeilen, 4 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### hypothesentests – Stufe Sek II; 5 Fertigkeitszeilen, 4 mit Ziel, 1 ohne
- Zeile 29:
  > - Den Rechner für kumulierte Verteilungswahrscheinlichkeiten einsetzen – alle Zeilen liegen in Teil B (Werkzeugwissen; die Befehle stehen in keiner Formelsammlung). [IQB-STR 1: Teil B mit WTR]
  - Klammer: `IQB-STR 1: Teil B mit WTR` – 1 Bestandteil:
    - `IQB-STR 1: Teil B mit WTR` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### integrationsregeln – Stufe Sek II; 3 Fertigkeitszeilen, 3 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### kenngroessen-von-verteilungen – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### kombinatorik – Stufe Sek II; 5 Fertigkeitszeilen, 5 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### konfidenzintervalle – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### kurvenuntersuchung – Stufe Sek II; 6 Fertigkeitszeilen, 5 mit Ziel, 1 ohne
- Zeile 31:
  > - Funktionswerte berechnen und Punktprobe – Koordinaten der gefundenen Punkte, Nachweis vorgegebener Punkte, Einheit 2, 3 und 5. Thema Lineare Funktionen (Sek I, Einheit 3); der fhr-Typ „Punktprobe am Graphen“ ist hier Einheit 3 zugeordnet. [GOST Eingangsvoraussetzung L4; FOS Pflichtthema 1 „Funktionsdarstellungen (Wertetabelle, Funktionsgleichung, Graph)“]
  - Klammer: `GOST Eingangsvoraussetzung L4; FOS Pflichtthema 1 „Funktionsdarstellungen (Wertetabelle, Funktionsgleichung, Graph)“` – 2 Bestandteile:
    - `GOST Eingangsvoraussetzung L4` – sonstiges oder keine Klammer, nicht aufzulösen.
    - `FOS Pflichtthema 1 „Funktionsdarstellungen (Wertetabelle, Funktionsgleichung, Graph)“` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **lineare-funktionen** (Name „Lineare Funktionen“ in „…te, Einheit 2, 3 und 5. Thema Lineare Funktionen (Sek I, Einheit 3); der fhr-T…“).

### lagebeziehungen – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### linearkombination-und-lineare-abhaengigkeit – Stufe Sek II; 4 Fertigkeitszeilen, 4 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### matrizen-und-uebergangsprozesse – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### normalverteilung-und-sigma-regeln – Stufe Sek II; 5 Fertigkeitszeilen, 4 mit Ziel, 1 ohne
- Zeile 29:
  > - Den Rechner für Verteilungswahrscheinlichkeiten einsetzen – die Teil-B-Rechnungen der Einheiten 2 und 3 (Werkzeugwissen; die Befehle stehen in keiner Formelsammlung). [IQB-STR 1: Teil B mit WTR]
  - Klammer: `IQB-STR 1: Teil B mit WTR` – 1 Bestandteil:
    - `IQB-STR 1: Teil B mit WTR` – sonstiges oder keine Klammer, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **einheiten** (Name „Einheiten“ in „…n – die Teil-B-Rechnungen der Einheiten 2 und 3 (Werkzeugwissen; die…“).

### orthogonalitaet – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### punkte-und-strecken-im-koordinatensystem – Stufe Sek II; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### rekonstruktion-von-bestaenden – Stufe Sek II; 5 Fertigkeitszeilen, 5 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### rekonstruktion-von-funktionsgleichungen – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### rotationsvolumen – Stufe Sek II; 5 Fertigkeitszeilen, 5 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### scharen-von-geraden-und-ebenen – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### schnittmengen – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### skalarprodukt-und-winkel – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### spiegelung – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### stammfunktion-und-hauptsatz – Stufe Sek II; 5 Fertigkeitszeilen, 5 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### tangente-normale-schnittwinkel – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### umkehrfunktion – Stufe Sek II; 5 Fertigkeitszeilen, 5 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### unabhaengigkeit – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### uneigentliche-integrale – Stufe Sek II; 3 Fertigkeitszeilen, 3 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### vektoren-und-rechenoperationen – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### vierfeldertafel – Stufe Sek II; 5 Fertigkeitszeilen, 5 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### zufallsexperimente-und-pfadregeln – Stufe Sek II; 9 Fertigkeitszeilen, 9 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### zufallsgroessen-und-verteilungen – Stufe Sek II; 3 Fertigkeitszeilen, 3 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

## Schwäche der Messung
Die Zerlegung sieht Zeichenketten, keine Bedeutung. Ob eine Zeile ein Ziel hat, entscheidet allein die Form `<name>.md`; eine Zeile, die ihr Thema in Wortform nennt („Thema Prozentrechnung, Einheit 3“), gilt als ohne Ziel und landet hier – der themen.csv-Treffer zeigt solche Fälle, ohne sie zu deuten. Die Sorten hängen an Signalwörtern („P10“, „LS-AA Kl.“, „RLP“ mit Buchstabe, „MSK“); eine Klammer in anderer Schreibweise fällt unter sonstiges. Die Zerlegung an Komma und Semikolon kann eine Aufzählung innerhalb eines Belegs trennen, wo weder Anführungszeichen noch Kennung noch MSK-Code den Zusammenhang zeigen. Beim P10-Typ sagt ein gefundener Typ nur, welches Thema die Typenliste ihm gibt, nicht, ob die Fertigkeit der Zeile dort gelehrt wird; die Katalogzeile einer Kennung nennt Thema und Typ der Aufgabe, nicht der Fertigkeit. Beim LS-AA-Fahrplan hängt die Lesung an der zweispaltigen Textfassung (Spaltengrenze bei Zeichen 100); Teil 2 nennt nur die Blöcke, unter denen das Kapitel mit der Lerneinheit steht, nicht die RLP-Zeile daneben. Beim RLP-Text werden Spalten nach der Überlappung der Zellen verkettet; ein Zitat, das über eine Seite hinweg umbricht oder im Katalog gekürzt wurde, wird nicht gefunden – „nicht gefunden“ heißt hier nur: nicht in dieser Textfassung, in dieser Schreibweise. Der Niveaustufenbuchstabe steht im RLP-Text einmal je Block in der Mitte; fehlt er am Block, ist die Stufe nur über den Seitenkopf und die Nachbarblöcke zu lesen; ein Teiltreffer über den Wortanfang zeigt nur, wo der Anfang des Zitats steht, nicht, was der Katalog daraus gemacht hat. Der themen.csv-Abgleich meldet jedes ganze Wort, auch wenn es in der Zeile etwas anderes meint („Einheiten“ in „alle Einheiten“ sind Lerneinheiten, „Geraden“ kann eine Sek-I-Gerade sein); das Umfeld steht dabei, die Deutung nicht – er ist ein Hinweis, kein Vorschlag.
