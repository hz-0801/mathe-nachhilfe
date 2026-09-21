# Belege der Blatt-0-Fertigkeiten ohne Ziel
Stand 2026-09-21, Katalog auf Commit f6e5fc5.
Erzeugt von `werkzeuge/blatt0-belege.py` (v0.2) aus den Blatt-0-Abschnitten der Einträge, `msa/msa-typen.csv`, `msa/msa-katalog-basis.csv`, `msa/msa-katalog-kontext.csv`, `themen.csv`, `quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt`, `quellen/quelle-rlp-teil-c-mathematik-2023.txt` und der Registerzeile [MSK] in `katalog/_quellen.md`; abgeleitet, nie von Hand ändern. Vorschlagsliste für die Fertigkeitszeilen, die keinen Dateiverweis tragen: was ihre Quellenklammer hergibt, wenn man sie gegen die Register im Repo hält. Kein Eintrag wird geändert, nichts wird entschieden; eine Zeile, deren Klammer kein Register auflöst, bleibt ohne Vorschlag – das ist ein Ergebnis, kein Mangel.

Gemessen: 73 Einträge (`katalog/*.md` ohne `_*` und `index.md`). Lesarten wie in `werkzeuge/tragfaehigkeit.py` (v0.1), importiert: Blatt-0-Abschnitt = „### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, Verweis = `<name>.md`. Fertigkeitszeile = Zeile des Abschnitts, die mit „- “ beginnt und vor der Zwischenzeile „Erkennungsschritte…“ steht (die Erkennungsschritte gehören dem Thema selbst). Ziel = Verweis ohne Pfad auf einen anderen vorhandenen Katalogeintrag, irgendwo in der Zeile; Selbstverweise zählen nicht. Klammer = die letzte eckige Klammer der Zeile (vermerkt, wenn sie nicht am Zeilenende steht). Bestandteile = Klammer an „;“ und „,“ zerlegt, nicht in „…“ und nicht in runden Klammern; ein Teil, der mit einer P10-Aufgabenkennung beginnt, setzt den vorigen fort, ein bloßer MSK-Code einen MSK-Teil. Sechs Sorten je Bestandteil: P10-Typ (enthält „P10“ und einen Typnamen in „…“ oder eine Aufgabenkennung), LS-AA-Kapitel („LS-AA Kl. 8 II 1“), RLP mit Zitat, RLP ohne Zitat (auch mit Zusatz ohne Anführungszeichen), MSK-Code, sonstiges oder keine Klammer. Zeilennummern zählen ab 1 in der Datei.

Auflösung, soweit ein Register es hergibt: P10-Typ – Typname gegen die Spalte `typ` von `msa/msa-typen.csv`, Kennung gegen `beispiel_id`; je Treffer das Thema und über `themen.csv` (profil msa) das kanonische Thema; Kennungen zusätzlich gegen die `id`-Spalte der beiden msa-Kataloge (Thema, Typ, Nebentypen der Katalogzeile), weil die Typenliste je Typ nur eine beispiel_id führt. LS-AA-Kapitel – Fahrplan Teil 1 (Gliederung je Klasse, zweispaltig): Kapiteltitel und Titel der Lerneinheit; Teil 2 (RLP-Inhalte mit „Zu finden in Studyly“): die RLP-Blöcke (Niveaustufe, Jahrgang, Themenbereich, Bereich), unter denen das Kapitel mit dieser Lerneinheit genannt ist. RLP mit Zitat – das Zitat wird in den Spalten des RLP-Texts gesucht (mehrspaltig gesetzt; ein Block sind die Zeilen zwischen zwei Leerzeilen, darin wird jede Zelle an die Zelle der Zeile davor gehängt, mit der sie sich am weitesten überlappt – je Zelle höchstens eine Fortsetzung –, Silbentrennung wird zusammengezogen, „…“ im Zitat erlaubt eine Lücke); Fundstelle mit Zeilen des Treffers, Block, Niveaustufenbuchstabe(n) am Block (der Buchstabe steht einmal je Stufe am linken Rand, in der Mitte seiner Zeilen) und Seitenkopf – zuerst genau, sonst ohne Groß-/Kleinschreibung. Steht das Zitat nicht im Text, wird noch der längste Wortanfang gesucht (mindestens 3 Wörter und mindestens die Hälfte; nicht bei Zitaten mit Lücke) und als Teiltreffer genannt, ohne als Auflösung zu zählen. RLP ohne Zitat, MSK-Code und sonstiges werden nach Auftrag nicht aufgelöst („nicht aufzulösen“; „nicht aufgelöst“ heißt dagegen: das Register gab nichts her); beim MSK-Code steht der Bausteintitel aus `katalog/_quellen.md` dabei, soweit er dort genannt ist. Zusätzlich je Zeile: welche kanonischen Namen aus `themen.csv` der Wortlaut der Zeile ohne ihre Quellenklammer wörtlich nennt (der Name selbst mit Bindestrich als Leerzeichen und ohne Rücksicht auf Groß-/Kleinschreibung, ein `thema`-Wert seiner Zeilen oder die H1-Überschrift seiner Katalogdatei, jeweils als ganzes Wort, mit dem Umfeld des Treffers; der eigene Eintrag zählt nicht) – keine Ähnlichkeitssuche, kein Raten; ob das Wort in der Zeile das Thema meint, steht nicht hier.

## Zahlen
Teil 1, die 22 Sek-I-Einträge des Auftrags Blatt-0-Dateiverweise (21 Dateien aus `archiv/ersetzungen-blatt0-2026-09-21.txt` und `terme.md`; dieselbe Menge wie `_verweise.md` § 5 auf Commit c05e6f0): 147 Fertigkeitszeilen, 131 mit Ziel, 16 ohne. Gegenprobe des Auftrags 147/131/16: bestanden.
Teil 2, die übrigen 51 Einträge: 316 Fertigkeitszeilen, 308 mit Ziel, 8 ohne – berichtet, nicht geprüft. Darunter sieben Einträge mit Stufe Sek I oder Sek I + II in der Statuszeile (potenzen-wurzeln, reelle-zahlen, trigonometrische-funktionen, zinsrechnung, daten, einheiten, lineare-gleichungssysteme); sie stehen in Teil 2 vorn.
Bestandteile der Klammern in Teil 1 nach Sorte (Bestandteile · davon aufgelöst): P10-Typ 2 · 2; LS-AA-Kapitel 4 · 4; RLP mit Zitat 4 · 3; RLP ohne Zitat 10 · 0; MSK-Code 1 · 0; sonstiges oder keine Klammer 2 · 0. MSK-Codes mit Bausteintitel aus _quellen.md: 0.
Bestandteile der Klammern in Teil 2 nach Sorte (Bestandteile · davon aufgelöst): P10-Typ 4 · 4; LS-AA-Kapitel 0 · 0; RLP mit Zitat 2 · 1; RLP ohne Zitat 1 · 0; MSK-Code 0 · 0; sonstiges oder keine Klammer 6 · 0. MSK-Codes mit Bausteintitel aus _quellen.md: 0.
Einträge ohne Blatt-0-Abschnitt: keine. Einträge ohne Zwischenzeile „Erkennungsschritte…“ (der ganze Abschnitt gilt als Fertigkeitenteil): ableitungsgraph-und-funktionsgraph.

## 1 Die 22 Sek-I-Einträge des Auftrags Blatt-0-Dateiverweise
Reihenfolge wie in der Ersetzungsdatei (alphabetisch). Je Eintrag die Fertigkeitszeilen ohne Ziel mit Zeilennummer, Wortlaut, Klammer, Bestandteilen, Sorte, dem, was die Register hergeben, und den wörtlichen themen.csv-Treffern.

### binomische-formeln – Stufe Sek I; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### bruchrechnung – Stufe Sek I; 6 Fertigkeitszeilen, 4 mit Ziel, 2 ohne
- Zeile 29:
  > - Vielfache und Teiler (kgV von vier und sechs, ggT von zwölf und achtzehn) – Einheit 1 (Hauptnenner) und Einheit 3 (Kürzen). [RLP D, LS-AA Kl. 5 III 5]
  - Klammer: `RLP D, LS-AA Kl. 5 III 5` – 2 Bestandteile:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
    - `LS-AA Kl. 5 III 5` – LS-AA-Kapitel, aufgelöst:
      - „LS-AA Kl. 5 III 5“ → Klasse 5, Kapitel III „Rechnen“, Lerneinheit 5 „Teilbarkeit“; Fahrplan-Zuordnung (Teil 2): RLP D, Jg. 5/6, Themenbereich „Zahlen und Operationen“ – Zahlvorstellungen
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

### lineare-funktionen – Stufe Sek I; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### lineare-gleichungen – Stufe Sek I; 5 Fertigkeitszeilen, 4 mit Ziel, 1 ohne
- Zeile 24:
  > - Punkt vor Strich (3 · 4 − 5) – Probe und Einsetzen. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### potenz-exponentialfunktionen – Stufe Sek I; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### prozentrechnung – Stufe Sek I; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### pyramide-kegel-kugel – Stufe Sek I; 9 Fertigkeitszeilen, 9 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### pythagoras – Stufe Sek I; 9 Fertigkeitszeilen, 9 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### quadratische-funktionen – Stufe Sek I; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### quadratische-gleichungen – Stufe Sek I; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### rationale-zahlen – Stufe Sek I; 5 Fertigkeitszeilen, 3 mit Ziel, 2 ohne
- Zeile 25:
  > - Natürliche Zahlen addieren, subtrahieren, multiplizieren, dividieren im Kopf (Einmaleins) – alle Einheiten. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv wörtlich im Wortlaut: **einheiten** (Name „Einheiten“ in „…n im Kopf (Einmaleins) – alle Einheiten.“).
- Zeile 28:
  > - Punkt vor Strich und Klammern mit natürlichen Zahlen – Einheit 3 und 4. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### strahlensaetze – Stufe Sek I; 9 Fertigkeitszeilen, 9 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### symmetrie-abbildungen – Stufe Sek I; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### terme – Stufe Sek I; 4 Fertigkeitszeilen, 3 mit Ziel, 1 ohne
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

### zuordnungen – Stufe Sek I; 5 Fertigkeitszeilen, 4 mit Ziel, 1 ohne
- Zeile 26:
  > - Vielfache und Teiler erkennen (zwölf ist das Dreifache von vier) – Einheit 2 und 3. [RLP D]
  - Klammer: `RLP D` – 1 Bestandteil:
    - `RLP D` – RLP ohne Zitat, nicht aufzulösen.
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

## 2 Die übrigen Einträge
Zuerst die Einträge mit Stufe Sek I und Sek I + II in der Statuszeile, dann die Sek-II-Einträge, je alphabetisch. Gleicher Aufbau wie Teil 1; die Zahlen sind nicht gegengeprüft.

### potenzen-wurzeln – Stufe Sek I; 9 Fertigkeitszeilen, 6 mit Ziel, 3 ohne
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
- Zeile 27:
  > - Große Zahlen lesen und schreiben (Dreiergruppen, Zahlwörter bis Billion), Stellenwerttafel, mal zehn, hundert und tausend durch Nullen anhängen – Einheit 2. Kein eigenes Thema (Grundschule; LS-AA Kl. 5 I 3); Struktur: MSK D4A (Multiplizieren und Dividieren mit Zehnerzahlen). [RLP C „Zahldarstellungen natürlicher Zahlen bis eine Million“; P10 2015-OS-K3a Fehlerquelle „Nullen falsch zählen“]
  - Klammer: `RLP C „Zahldarstellungen natürlicher Zahlen bis eine Million“; P10 2015-OS-K3a Fehlerquelle „Nullen falsch zählen“` – 2 Bestandteile:
    - `RLP C „Zahldarstellungen natürlicher Zahlen bis eine Million“` – RLP mit Zitat, nicht aufgelöst:
      - „Zahldarstellungen natürlicher Zahlen bis eine Million“ (Klammer nennt C): im RLP-Text nicht gefunden; Teiltreffer – der Wortanfang „Zahldarstellungen natürlicher Zahlen bis“ (4 von 6 Wörtern) steht in: Zeilen 1702–1703 (Block 1686–1712), Niveaustufe am Block: A (Zeile 1692), B (Zeile 1707); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen A, B, C | Zeilen 1722–1723 (Block 1717–1731), Niveaustufe am Block: C (Zeile 1727); Seitenkopf: Themenbereich „Zahlen und Operationen“ – Niveaustufen A, B, C
    - `P10 2015-OS-K3a Fehlerquelle „Nullen falsch zählen“` – P10-Typ, aufgelöst:
      - „Nullen falsch zählen“: kein Typname in msa/msa-typen.csv
      - Kennung 2015-OS-K3a: beispiel_id des Typs „Große Zahl mit Zehnerpotenz multiplizieren“ in msa/msa-typen.csv, Thema „Zehnerpotenzen und Näherungswerte“ → themen.csv: potenzen-wurzeln; Katalogzeile (msa-katalog-kontext.csv): Thema „Zehnerpotenzen und Näherungswerte“, Typ „Große Zahl mit Zehnerpotenz multiplizieren“ → themen.csv: potenzen-wurzeln
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### reelle-zahlen – Stufe Sek I; 7 Fertigkeitszeilen, 7 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### trigonometrische-funktionen – Stufe Sek I; 11 Fertigkeitszeilen, 10 mit Ziel, 1 ohne
- Zeile 26:
  > - Taschenrechner: Modus DEG und RAD unterscheiden und umstellen, Tasten sin und cos mit dem Winkel dahinter, Umkehrtaste, Wert erst am Ende runden – Einheit 1 bis 3. Kein eigenes Thema. [LISUM-PH „Taschenrechnereinsatz“; P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“]
  - Klammer: `LISUM-PH „Taschenrechnereinsatz“; P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“` – 2 Bestandteile:
    - `LISUM-PH „Taschenrechnereinsatz“` – sonstiges oder keine Klammer, nicht aufzulösen.
    - `P10 2021-OS-K3a Fehlerquelle „Taschenrechner in Bogenmaß“` – P10-Typ, aufgelöst:
      - „Taschenrechner in Bogenmaß“: kein Typname in msa/msa-typen.csv
      - Kennung 2021-OS-K3a: Katalogzeile (msa-katalog-kontext.csv): Thema „Trigonometrie im rechtwinkligen Dreieck“, Typ „Seite im rechtwinkligen Dreieck berechnen“ → themen.csv: trigonometrie
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### zinsrechnung – Stufe Sek I; 8 Fertigkeitszeilen, 8 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### daten – Stufe Sek I + II; 9 Fertigkeitszeilen, 8 mit Ziel, 1 ohne
- Zeile 37:
  > - Längen in Zentimetern und Millimetern abtragen – Einheit 3 (Streifen). [P10 2018-OS-K3c]
  - Klammer: `P10 2018-OS-K3c` – 1 Bestandteil:
    - `P10 2018-OS-K3c` – P10-Typ, aufgelöst:
      - Kennung 2018-OS-K3c: beispiel_id des Typs „Streifendiagramm zeichnen“ in msa/msa-typen.csv, Thema „Daten darstellen“ → themen.csv: daten; Katalogzeile (msa-katalog-kontext.csv): Thema „Daten darstellen“, Typ „Streifendiagramm zeichnen“ → themen.csv: daten
  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.

### einheiten – Stufe Sek I + II; 11 Fertigkeitszeilen, 11 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

### lineare-gleichungssysteme – Stufe Sek I + II; 10 Fertigkeitszeilen, 10 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

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

### kurvenuntersuchung – Stufe Sek II; 6 Fertigkeitszeilen, 6 mit Ziel, 0 ohne
Alle Fertigkeitszeilen tragen ein Ziel.

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
