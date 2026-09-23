# Belege der Niveaustufe je Lerneinheit und Sprosse (Sekundarstufe I)
Stand 2026-09-24, Katalog auf Commit 72325d0.
Erzeugt im Auftrag `archiv/auftrag-niveaustufen-belege.md` aus den 29 Sek-I-Einträgen (`katalog/index.md`, Tabelle Sekundarstufe I), `quellen/quelle-rlp-teil-c-mathematik-2023.txt` und `quellen/quelle-lisum-planungshilfen-7bis10.txt`; abgeleitet, nie von Hand ändern. Vorschlagsliste für die Marke, die der Unterrichtsblatt-Prompt ab v4.3 für die Schulformfrage braucht: was der Rahmenlehrplan je Lerneinheit und je Sprosse hergibt, wenn man den Inhalt der Einheit gegen die Standardtabellen hält. Kein Eintrag wird geändert, nichts wird entschieden; eine Einheit, für die der Plantext keine Stelle hergibt, bleibt ohne Stufe – das ist ein Ergebnis, kein Mangel.

Quellen und ihre Lesart:
- `quellen/quelle-rlp-teil-c-mathematik-2023.txt` – Rahmenlehrplan 1–10 Berlin-Brandenburg, Teil C Mathematik, Fassung 14.08.2023 (Registerzeile [RLP] in `katalog/_quellen.md` Zeile 23). Kapitel 3 ist mehrspaltig gesetzt. Gelesen wird er mit den Lesarten von `werkzeuge/blatt0-belege.py` (v0.2), importiert: ein Block sind die Zeilen zwischen zwei Leerzeilen, darin wird jede Zelle an die Zelle der Zeile davor gehängt, mit der sie sich am weitesten überlappt (je Zelle höchstens eine Fortsetzung), Silbentrennung wird zusammengezogen, „…“ im Zitat erlaubt eine Lücke. Die Fundstelle nennt die Zeilen des Treffers, den Block, den Niveaustufenbuchstaben am Block (er steht einmal je Stufe am linken Rand, in der Mitte seiner Zeilen) und den Seitenkopf mit Themenbereich und Niveaustufen.
- Die Zuordnung Bildungsgang → Niveaustufe steht im selben Text, Zeilen 572–591: Integrierte Sekundarschule, grundlegendes Niveau „Jahrgangsstufen 7 – 8      Niveaustufen D – E, in Teilen F“ [Zeile 574] und „Jahrgangsstufen 9 – 10     Niveaustufe F, in Teilen G“ [Zeile 575]; erweitertes Niveau „Jahrgangsstufen 7 – 8      Niveaustufe E, in Teilen F“ [Zeile 577] und „Jahrgangsstufen 9 – 10     Niveaustufen F – G“ [Zeile 578]; Gymnasium „Jahrgangsstufe 7        Niveaustufe E“ [Zeile 588], „Jahrgangsstufe 8        Niveaustufe F“ [Zeile 589], „Jahrgangsstufe 9        Niveaustufe G“ [Zeile 590], „Jahrgangsstufe 10       Niveaustufe H“ [Zeile 591]. Daraus die Lesart der Spanne: G und H sind Gymnasialstoff der Klassen 9 und 10, F und darunter erreicht auch der Bildungsgang zum MSA.
- `quellen/quelle-lisum-planungshilfen-7bis10.txt` – die LISUM-Planungshilfen. Je Thema wird genannt, ob die Planungshilfe getrennte Unterrichtsreihen für EBR/FOR und für GYM führt oder nur den Differenzierungshinweis; die Fundstelle ist die Zeilennummer im Text.
- `katalog/<eintrag>.md` – Zeilennummern zählen ab 1 in der Datei. Verortung = Abschnitt „### Verortung“, Lerneinheiten = Abschnitt „### Lerneinheiten“ (Nummer und Titel bis zum ersten Gedankenstrich bzw. Doppelpunkt), Sprossen = die Liste „Sprossen je Verfahrenstyp“ im Abschnitt „### Für schwache Schüler“, an „→“ zerlegt (Pfeile innerhalb einer offenen Klammer gehören zur Sprosse).

Lesart der Zuordnung: Die Stufe einer Einheit ist die Stufe des Blocks, in dem der Standard steht, der den Inhalt der Einheit nennt – nicht die Stufe, die dem Eintrag insgesamt zugeschrieben ist. Passt der Inhalt zu mehreren Stufen (Grundfall auf der einen, Sonderfall auf der nächsten), stehen beide da, je mit eigenem Zitat. Wo der Plantext den Inhalt nicht nennt, steht „keine Stelle“ mit dem Grund; wo die Zuordnung eine Auslegung verlangt, steht „Ermessen:“ mit der Begründung. Die Datei nennt Stufen; sie setzt keine Marke im Katalog und formuliert keine Prompt-Regel.

Spanne (Zeile e je Eintrag): ja, wenn mindestens eine Einheit oder Sprosse auf G oder H liegt und mindestens eine auf F oder darunter; sonst nein. Gerechnet wird über alle Stufen, die dieser Datei zufolge im Eintrag vorkommen.

## Zahlen
Einträge gesamt: 29 (die 29 Sek-I-Einträge aus `katalog/index.md`, Tabelle Sekundarstufe I).
Lerneinheiten gesamt: 116, davon mit Stelle im RLP-Text: 115, davon ohne: 1 (strahlensaetze 3. Strahlensätze).
Sprossen gesamt: 1352, davon mit Stelle im RLP-Text: 1126, davon ohne: 226.
Einträge mit Spanne ja: 19 (binomische-formeln, daten, einheiten, lineare-funktionen, lineare-gleichungssysteme, potenz-exponentialfunktionen, potenzen-wurzeln, pyramide-kegel-kugel, pythagoras, quadratische-gleichungen, reelle-zahlen, strahlensaetze, terme, trigonometrie, trigonometrische-funktionen, wahrscheinlichkeit, winkel-dreiecke, zinsrechnung, zuordnungen).
Einträge mit Spanne nein: 10 (bruchrechnung, brueche-dezimalzahlen, flaechen, koerper, kreis, lineare-gleichungen, prozentrechnung, quadratische-funktionen, rationale-zahlen, symmetrie-abbildungen).
Einträge ohne jede Stelle: keine.
Ermessensfälle gesamt: 126 in 29 Einträgen (binomische-formeln 4, bruchrechnung 4, brueche-dezimalzahlen 4, daten 6, einheiten 5, flaechen 4, koerper 5, kreis 4, lineare-funktionen 4, lineare-gleichungen 4, lineare-gleichungssysteme 4, potenz-exponentialfunktionen 4, potenzen-wurzeln 5, prozentrechnung 4, pyramide-kegel-kugel 5, pythagoras 4, quadratische-funktionen 4, quadratische-gleichungen 5, rationale-zahlen 3, reelle-zahlen 4, strahlensaetze 4, symmetrie-abbildungen 4, terme 4, trigonometrie 5, trigonometrische-funktionen 5, wahrscheinlichkeit 5, winkel-dreiecke 5, zinsrechnung 4, zuordnungen 4).
Geprüfte Zitate beim Bau: 1357 RLP-Zitate, 390 Eintragszitate, 28 LISUM-Zitate.

### binomische-formeln – Stufe F (Summe mal Summe) – G (binomische Formeln); quadratische Ergänzung H
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Terme und Gleichungen E (S. 58): „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen“; F (S. 58): „Distributivgesetz zum Ausmultiplizieren von Summen““
  - Zeile 6 (Verortung): „Befund: Die binomischen Formeln stehen im RLP erst auf G (Gymnasium Kl. 9), das Lehrwerk bringt sie in Kl. 8 II 4“
  - Zeile 6 (Verortung): „Summe mal Summe wird im RLP nicht eigens genannt, „Ausmultiplizieren von Summen“ (F) deckt es (Annahme).“
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[RLP E; LS-AA Kl. 8 II 1 Wiederholung]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP F; LS-AA Kl. 7 IV 3]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP F; LS-AA Kl. 7 IV 3]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP F; P10 2020-OS-K3c Fehlerquelle Quadrat einer Zahlensumme; 2026-FOR-B1e Vorzahl mit quadriert]“
  - Zeile 28 (Merkkasten): „[RLP G]“
  - Zeile 44 (Merkkasten): „[RLP F]“
  - Zeile 81 (Für schwache Schüler): „[RLP F/G, MO]“
- Lerneinheiten:
  - 1. Summe mal Summe – F
    - F [Zeilen 2757–2758]: „Distributivgesetz zum Ausmultiplizieren von Summen)“
      Block 2756–2769, Niveaustufe am Block: F (Z2763); der RLP nennt „Summe mal Summe“ nicht eigens; der Eintrag hält die Zuordnung selbst für eine Annahme
  - 2. Binomische Formeln – G
    - G [Zeilen 2839–2840]: „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); die einzige Stelle, die die binomischen Formeln nennt – auf G
  - 3. Faktorisieren – G/H
    - G [Zeilen 2839–2840]: „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); der RLP nennt die binomischen Formeln, nicht die Richtung
    - H [Zeilen 2864–2865]: „− auch Umformen quadratischer Terme in vollständige Quadrate mithilfe quadratischer“
      Block 2860–2880, Niveaustufe am Block: H (Z2875); die quadratische Ergänzung erst auf H; im Eintrag als Vorrat
- Sprossen je Verfahrenstyp:
  - Summe mal Summe (Einheit 1)
    - Sprosse 1 · Pfeile „jedes mit jedem“ zeichnen (Vorstufe) → F [Zeilen 2757–2758]; Eintrag: Vorstufe
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 2 · zwei Variablen zusammenfassen, lauter Plus (4×) → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · mit Minus und Vorzahl eins → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · Potenzen und Produkte getrennt halten (x², xy, x) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 5 · Zahl mal Klammer mit zwei Variablen → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 6 · Klammer mal Klammer mit lauter Plus, vier Produkte hinschreiben → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 7 · zusammenfassen zum dreigliedrigen Term → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 8 · ein Minus in einer Klammer → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 9 · Minus in beiden Klammern → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 10 · Vorzahl vor x → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 11 · zwei Variablen in beiden Klammern → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 12 · Prüfungshöhe: Klammer mal Klammer mit Minus und Vorzahl (kein P10-Original) … → F [Zeilen 2757–2758]; Eintrag: Prüfungshöhe, Zielmarke
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
  - Binomische Formeln (Einheit 2)
    - Sprosse 1 · Formel erkennen und a, b einkreisen (Vorstufe) → G [Zeilen 2839–2840]; Eintrag: Vorstufe
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 2 · erste Formel mit x und Zahl (4×) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 3 · zweite Formel, Minus im Mittelglied → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 4 · dritte Formel, Mittelglied fällt weg (Vorrat: kein P10-Original) → G [Zeilen 2839–2840]; Eintrag: Vorrat
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 5 · gemischt: Formel wählen, auch „keine“ → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 6 · Vorzahl vor x (Vorzahl mit quadrieren) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 7 · zwei Variablen (Vorrat) → G [Zeilen 2839–2840]; Eintrag: Vorrat
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 8 · Vorfaktor vor der Klammer → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 9 · Minus vor der Klammer (alle drei Vorzeichen drehen) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 10 · Klammer auflösen und mit dem Rest zusammenfassen → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 11 · Prüfungshöhe: Scheitelpunktform als vorgegebene Normalform nachweisen … → G [Zeilen 2839–2840]; Eintrag: Prüfungshöhe
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
  - Faktorisieren (Einheit 3)
    - Sprosse 1 · „Ist das ein Quadrat?“ und „Passt das Mittelglied?“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · dritte Formel rückwärts, x² minus Quadratzahl (4×) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 3 · erste Formel rückwärts mit geprüftem Mittelglied → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 4 · zweite Formel rückwärts, Minus im Mittelglied → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 5 · Vorzahl vor x², Quadrat von zwei x → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 6 · erst gemeinsamen Faktor ausklammern, dann Formel → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 7 · kein Binom erkennen und begründen → keine Stelle; Das Begründen, dass keine binomische Formel passt, nennt der RLP nicht.
    - Sprosse 8 · Probe durch Ausmultiplizieren → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 9 · Anwendung: Produktform gleich null lösen → G [Zeilen 2842–2843]
      „Lösen von Gleichungen (auch quadratische Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 10 · quadratische Ergänzung (Vorrat) → H [Zeilen 2864–2865]; Eintrag: Vorrat
      „− auch Umformen quadratischer Terme in vollständige Quadrate mithilfe quadratischer“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 11 · Prüfungshöhe: Term vollständig faktorisieren und die Probe führen (kein P10-Original) … → G [Zeilen 2839–2840]; Eintrag: Prüfungshöhe, Zielmarke
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 8, Mathematik: Terme und Gleichungen“ [Zeile 850]
  - Beleg [Zeile 851]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: ja  – Einheit 1 liegt auf E und F, Einheit 2 ganz auf G, Einheit 3 auf G und H (quadratische Ergänzung). Damit stehen Einheiten auf G und H und Einheiten auf F und darunter – das deckt sich mit der Stufenangabe „F – G; quadratische Ergänzung H“ in index.md.
- Ermessen (4):
  - Einheit 1: „Summe mal Summe“ nennt der RLP nicht eigens; der Eintrag hält die Zuordnung zu „Ausmultiplizieren von Summen“ (F) selbst für eine Annahme. Diese Datei übernimmt sie.
  - Einheit 3: der RLP nennt die binomischen Formeln nur einmal (G), ohne Richtung. Faktorisieren und Ausmultiplizieren hängen deshalb an derselben Stelle.
  - Sprossen mit zwei Variablen oder Potenzen im Term liegen auf G, während der Rest der Kette „Summe mal Summe“ auf E und F steht.
  - Sprosse „kein Binom erkennen und begründen“: keine Stelle; das Begründen einer Nicht-Anwendbarkeit steht nicht im Plan.

### bruchrechnung – Stufe D
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] D: „Zuordnen der Vorstellungen der Anteilbildung zur Multiplikation und der des Aufteilens zur Division im Bereich der gebrochenen Zahlen““
  - Zeile 6 (Verortung): „E: „Darstellen des Ergebnisses einer Division als gebrochene Zahl und als Dezimalzahl (auch periodische Dezimalzahlen)““
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP D, MSK B1A]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D, MSK B2B]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP D, LS-AA Kl. 5 III 5]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[MSK D1A, RLP D]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 35 (Merkkasten): „[RLP D „Operator“; FD]“
  - Zeile 37 (Merkkasten): „[RLP D]“
  - Zeile 73 (Typische Fehler): „[RLP D]“
  - Zeile 87 (Für schwache Schüler): „[RLP D]“
- Lerneinheiten:
  - 1. Brüche addieren und subtrahieren – D
    - D [Zeilen 1874–1875]: „Prüfen und Übertragen der operativen Strategien und der schriftlichen Rechenverfahren für Addition,“
      Block 1871–1894, Niveaustufe am Block: D (Z1885); Grundfall; Strom „Rechenverfahren und -strategien anwenden“
    - D [Zeilen 1887–1889]: „Darstellen, Ausführen und Beschreiben des Rechnens mit gemeinen Brüchen, z. B. mithilfe des Bruchstreifens“
      Block 1871–1894, Niveaustufe am Block: D (Z1885); die anschauliche Fassung, auf die der Eintrag die Vorstufe stützt
  - 2. Dezimalzahlen addieren und subtrahieren – D
    - D [Zeilen 1874–1875]: „Prüfen und Übertragen der operativen Strategien und der schriftlichen Rechenverfahren für Addition,“
      Block 1871–1894, Niveaustufe am Block: D (Z1885); Dezimalzahlen sind im RLP gebrochene Zahlen; eine eigene Zeile zum Kommarechnen gibt es nicht
    - D [Zeile 2138]: „Erklären von Größenangaben mit Dezimalzahlen“
      Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155); Themenbereich Größen und Messen, für die Größen mit Komma
      Ermessen: Der RLP nennt kein „Komma unter Komma“; die Einheit ist über das Übertragen der schriftlichen Verfahren auf gebrochene Zahlen zugeordnet.
  - 3. Brüche multiplizieren und dividieren – D/E
    - D [Zeilen 1874–1877]: „Zuordnen der Vorstellungen der Anteilbildung zur Multiplikation und der des Aufteilens zur Division im Bereich der gebrochenen Zahlen“
      Block 1871–1894, Niveaustufe am Block: D (Z1885); Grundfall
    - E [Zeilen 1910–1911]: „Division als Multiplikation mit dem Kehrwert der rationalen Zahl“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Sonderfall Kehrbruch; im Eintrag als Vorrat geführt
  - 4. Dezimalzahlen multiplizieren und dividieren – D
    - D [Zeilen 1874–1875]: „Prüfen und Übertragen der operativen Strategien und der schriftlichen Rechenverfahren für Addition,“
      Block 1871–1894, Niveaustufe am Block: D (Z1885); keine eigene Zeile zur Kommaverschiebung
      Ermessen: Kommaverschiebung bei 10, 100, 1000 und das Zählen der Kommastellen stehen im RLP nicht; zugeordnet über das Übertragen der Rechenverfahren auf gebrochene Zahlen.
  - 5. Rechengesetze und Punkt vor Strich – C/D
    - C [Zeile 1782]: „Klammerregeln im Bereich der natürlichen Zahlen“
      Block 1774–1802, Niveaustufe am Block: C (Z1785); Grundfall mit natürlichen Zahlen
    - D [Zeile 1882]: „Klammerregeln im Zahlenbereich der gebrochenen“
      Block 1871–1894, Niveaustufe am Block: D (Z1885); die Stufe der Einheit: dieselbe Regel im Bereich der gebrochenen Zahlen
- Sprossen je Verfahrenstyp:
  - Addieren/Subtrahieren (Einheit 1)
    - Sprosse 1 · am Streifen zusammenfügen (Vorstufe) → D [Zeilen 1888–1889]; Eintrag: Vorstufe
      „Rechnens mit gemeinen Brüchen, z. B. mithilfe des Bruchstreifens“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 2 · gleichnamig (4×) → D [Zeilen 1874–1875]
      „Prüfen und Übertragen der operativen Strategien und der schriftlichen Rechenverfahren für Addition,“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 3 · Ergebnis kürzen → D [Zeilen 1886–1887]
      „Unterscheiden zwischen Erweitern und Vervielfachen bzw. Kürzen und Dividieren“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 4 · über ein Ganzes (gemischte Zahl) → D [Zeilen 1827–1828]
      „Verwenden gemischter Zahlen nur in Alltagszusammenhängen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 5 · ein Nenner Vielfaches des anderen (4×) → D [Zeilen 1820–1821]
      „gleichnamig Machen und am Zahlenstrahl“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 6 · beide erweitern (Hauptnenner) → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 7 · gemischte Zahlen → D [Zeilen 1827–1828]
      „Verwenden gemischter Zahlen nur in Alltagszusammenhängen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 8 · Prüfungshöhe: drei Pfadwahrscheinlichkeiten mit verschiedenen Nennern addieren und kürzen … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Dezimal addieren/subtrahieren (Einheit 2)
    - Sprosse 1 · Stellenwerttafel (Vorstufe) → D [Zeilen 1823–1824]; Eintrag: Vorstufe
      „Erweitern der Stellenwerttafel (nach rechts)“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 2 · gleich viele Stellen (4×) → D [Zeilen 1874–1875]
      „Prüfen und Übertragen der operativen Strategien und der schriftlichen Rechenverfahren für Addition,“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 3 · Nullen anhängen → keine Stelle; Schreibhilfe beim Untereinanderschreiben; der RLP nennt sie nicht.
    - Sprosse 4 · Übertrag → D [Zeilen 1884–1885]
      „Ausführen der schriftlichen Rechenverfahren für natürliche Zahlen“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 5 · Größen mit Komma → D [Zeile 2138]
      „Erklären von Größenangaben mit Dezimalzahlen“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 6 · Prüfungshöhe: Differenz zweier Geldbeträge mit Komma als Nebenleistung … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Multiplizieren (Einheit 3)
    - Sprosse 1 · „von“ markieren (Vorstufe) → D [Zeilen 1889–1890]; Eintrag: Vorstufe
      „Verwenden von gebrochenen Zahlen als Operator“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 2 · Bruch mal Zahl (4×) → D [Zeilen 1874–1875]
      „Zuordnen der Vorstellungen der Anteilbildung zur Multiplikation“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 3 · Bruch mal Bruch → D [Zeilen 1874–1875]
      „Zuordnen der Vorstellungen der Anteilbildung zur Multiplikation“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 4 · vorher kürzen → D [Zeilen 1886–1887]
      „Unterscheiden zwischen Erweitern und Vervielfachen bzw. Kürzen und Dividieren“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 5 · gemischte Zahl → D [Zeilen 1827–1828]
      „Verwenden gemischter Zahlen nur in Alltagszusammenhängen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 6 · Prüfungshöhe: drei Brüche nach der Pfadregel multiplizieren und kürzen … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Dividieren (Einheit 3)
    - Sprosse 1 · Bruch geteilt durch Zahl (4×) → D [Zeilen 1876–1877]
      „Aufteilens zur Division im Bereich der gebrochenen Zahlen“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 2 · Zahl geteilt durch Stammbruch („wie oft passt ein Drittel in fünf?“) → D [Zeilen 1876–1877]
      „Aufteilens zur Division im Bereich der gebrochenen Zahlen“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 3 · Bruch geteilt durch Bruch mit Kehrbruch (Vorrat) → E [Zeilen 1910–1911]; Eintrag: Vorrat
      „Division als Multiplikation mit dem Kehrwert der rationalen Zahl“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · kürzen → D [Zeilen 1886–1887]
      „Unterscheiden zwischen Erweitern und Vervielfachen bzw. Kürzen und Dividieren“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 5 · Prüfungshöhe: Sachaufgabe „wie viele Flaschen zu zwei Fünftel Liter aus sechs Liter“ … → keine Stelle; Lehrwerksmaßstab ohne P10-Original; der RLP nennt die Sachform nicht.; Eintrag: Prüfungshöhe
  - Dezimal multiplizieren/dividieren (Einheit 4)
    - Sprosse 1 · Kommaverschiebung mal zehn, mal hundert (4×) → keine Stelle; Die Kommaverschiebung steht im RLP nicht; sie ist Rechentechnik innerhalb des Übertragens der Verfahren.
    - Sprosse 2 · geteilt durch zehn, durch hundert → keine Stelle; wie Sprosse 1: keine eigene Stelle.
    - Sprosse 3 · Dezimalzahl mal natürliche Zahl → D [Zeilen 1874–1875]
      „Prüfen und Übertragen der operativen Strategien und der schriftlichen Rechenverfahren für Addition,“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 4 · Kommastellen zählen (mal Dezimalzahl) → keine Stelle; Rechentechnik; der RLP nennt sie nicht.
    - Sprosse 5 · Ergebnis mit führenden Nullen → keine Stelle; Schreibweise; keine eigene Stelle im RLP.
    - Sprosse 6 · geteilt durch natürliche Zahl → D [Zeilen 1884–1885]
      „Ausführen der schriftlichen Rechenverfahren für natürliche Zahlen (auch der Division mit“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 7 · geteilt durch Dezimalzahl → keine Stelle; Das Verschieben beider Kommas steht im RLP nicht.
    - Sprosse 8 · Prüfungshöhe: Menge mal Literpreis mit Wechsel zwischen Cent und Euro … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Punkt vor Strich (Einheit 5)
    - Sprosse 1 · Rechnung einkreisen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Punkt vor Strich mit natürlichen Zahlen (4×) → C [Zeile 1782]
      „Klammerregeln im Bereich der natürlichen Zahlen“ – Block 1774–1802, Niveaustufe am Block: C (Z1785)
    - Sprosse 3 · mit Dezimalzahlen → D [Zeile 1882]
      „Klammerregeln im Zahlenbereich der gebrochenen“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 4 · mit Brüchen → D [Zeile 1882]
      „Klammerregeln im Zahlenbereich der gebrochenen“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 5 · Klammer → D [Zeile 1882]
      „Klammerregeln im Zahlenbereich der gebrochenen“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 6 · Rechenvorteil → D [Zeilen 1878–1879]
      „situationsangemessenes Verwenden der Kopfrechenstrategien und der Rechenverfahren“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 7 · Prüfungshöhe: Bruchterm mit Klammer auswerten, erst die Klammer, dann die Division … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7, Mathematik: Rationale Zahlen“ [Zeile 477]
  - Beleg [Zeile 478]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
  - Keine eigene Reihe: die Planungshilfen setzen mit Jahrgangsstufe 7 ein, das Rechnen mit Brüchen liegt in Klasse 6/7. Die Reihe „Rationale Zahlen“ (Zeilen 477–729) führt das Rechnen mit rationalen Zahlen für EBR, FOR und GYM gemeinsam.
- Spanne: nein  – Alle Einheiten und alle belegten Sprossen liegen auf C, D oder E; keine Stelle führt auf G oder H. Das deckt sich mit der Stufenangabe „D“ in index.md.
- Ermessen (4):
  - Einheit 2 und 4: der RLP hat keine Zeile zum Rechnen mit dem Komma. Beide Einheiten sind über „Prüfen und Übertragen der operativen Strategien und der schriftlichen Rechenverfahren … auf das Rechnen mit gebrochenen Zahlen“ (D) zugeordnet – eine Zuordnung nach Sinn.
  - Sprossen zur Kommaverschiebung (Einheit 4, Sprossen 1, 2, 4, 5, 7): keine Stelle. Der RLP beschreibt das Rechnen mit gebrochenen Zahlen, nicht die Stellenschreibweise beim Multiplizieren und Dividieren.
  - Sprosse „Bruch geteilt durch Bruch mit Kehrbruch“: der RLP nennt den Kehrwert erst auf E im Bereich der rationalen Zahlen (Zeile 1910–1911), der Eintrag führt sie als Vorrat – beides stimmt überein.
  - Sprosse „Punkt vor Strich mit natürlichen Zahlen“ liegt auf C, die übrigen derselben Kette auf D; die Kette überschreitet also eine Stufengrenze innerhalb eines Verfahrenstyps.

### brueche-dezimalzahlen – Stufe D–E (Vergleichen mit Potenzen F)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] D (Zahlvorstellungen): „Beschreiben der Anteile von Ganzen als gemeine Brüche und Abgrenzen von Verhältnissen““
  - Zeile 6 (Verortung): „E: „Darstellen des Ergebnisses einer Division als gebrochene Zahl und als Dezimalzahl (auch periodische Dezimalzahlen)““
  - Zeile 6 (Verortung): „F: „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen Exponenten)““
  - Zeile 6 (Verortung): „G: „Vergleichen und Ordnen von reellen Zahlen über Näherungswerte““
  - Zeile 6 (Verortung): „H: „situationsangemessenes Darstellen von Zahlen als Brüche, Dezimalzahlen, Prozentzahlen und in Zehnerpotenzschreibweise““
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP D, LS-AA Kl. 5 III]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D „Angeben gemeinsamer Teiler und Vielfache zweier natürlicher Zahlen“, LS-AA Kl. 5 III 5]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP C/D, MSK N2]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln“]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP D „schriftliche Rechenverfahren … Division“]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP E]“
  - Zeile 50 (Merkkasten): „[RLP D]“
  - Zeile 66 (Merkkasten): „[RLP D]“
  - Zeile 93 (Typische Fehler): „[MSK B3B 3.3; RLP D Dichtheit]“
- Lerneinheiten:
  - 1. Bruch als Anteil – D
    - D [Zeilen 1815–1816]: „Beschreiben der Anteile von Ganzen als gemeine Brüche“
      Block 1812–1836, Niveaustufe am Block: D (Z1826); Grundfall; Strom „Zahlen auffassen und darstellen“
    - D [Zeile 2136]: „Erfassen und Bilden von Bruchteilen von Größen“
      Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155); für den Bruchteil einer Größe; der Block trägt D (Zeile 2133) und E (Zeile 2155), die Stelle liegt im D-Teil – so auch der Eintrag in Zeile 6
  - 2. Kürzen und Erweitern – D
    - D [Zeilen 1825–1826]: „Kürzen und Erweitern von Brüchen“
      Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - D [Zeilen 1886–1887]: „Unterscheiden zwischen Erweitern und Vervielfachen“
      Block 1871–1894, Niveaustufe am Block: D (Z1885); Operationsvorstellungen, Block 1871–1894 mit D (Zeile 1885)
  - 3. Brüche vergleichen – D
    - D [Zeilen 1817–1819]: „Vergleichen und Ordnen von gemeinen Brüchen durch direktes Vergleichen,“
      Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - D [Zeilen 1815–1816]: „Anordnen von gebrochenen Zahlen am Zahlenstrahl“
      Block 1812–1836, Niveaustufe am Block: D (Z1826); für das Eintragen am Zahlenstrahl
  - 4. Dezimalzahlen – D/E
    - D [Zeilen 1823–1824]: „Erweitern der Stellenwerttafel (nach rechts)“
      Block 1812–1836, Niveaustufe am Block: D (Z1826); Grundfall Stellenwerte
    - E [Zeilen 1854–1857]: „Darstellen des Ergebnisses einer Division als gebrochene Zahl und als Dezimalzahl (auch periodische Dezimalzahlen)“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); Sonderfall Division und periodische Dezimalzahl; Block 1838–1860 mit E (Zeile 1850)
  - 5. Vergleichen, Ordnen, Runden – D/E/F
    - D [Zeilen 1822–1825]: „Vergleichen und Ordnen von Dezimalzahlen stellenweise und am Zahlenstrahl“
      Block 1812–1836, Niveaustufe am Block: D (Z1826); Grundfall
    - E [Zeilen 1838–1840]: „Beschreiben von Prozenten als weitere Darstellungsform für gebrochene Zahlen“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); für den Vergleich Bruch gegen Prozent
    - F [Zeilen 1930–1933]: „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen Exponenten)“
      Block 1927–1937, Niveaustufe am Block: F (Z1934); Erweiterung: gemischte Darstellungen mit Potenzen; deckt sich mit der Stufenangabe der index.md-Zeile „D–E (Vergleichen mit Potenzen F)“
- Sprossen je Verfahrenstyp:
  - Anteil bestimmen (Einheit 1)
    - Sprosse 1 · gleich große Teile prüfen (Vorstufe) → keine Stelle; Vorstufe des Bruchbegriffs; der RLP nennt das Prüfen auf gleich große Teile nicht als eigene Handlung.; Eintrag: Vorstufe
    - Sprosse 2 · Anteil an gleich geteilter Figur ablesen (4×) → D [Zeilen 1815–1816]
      „Beschreiben der Anteile von Ganzen als gemeine Brüche“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 3 · Anteil einzeichnen → D [Zeilen 1819–1822]
      „Übersetzen von gebrochenen Zahlen (gemeine Brüche und Dezimalzahlen) zwischen Bild, Wort und Symbol“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 4 · ungleiche Teile gleich groß machen (halbe Kästchen, Sektoren) → keine Stelle; Zwischenschritt beim Ablesen; der RLP nennt das Gleichmachen ungleicher Teile nicht.
    - Sprosse 5 · Figur mit gegebenem Anteil auswählen → D [Zeilen 1819–1822]
      „Übersetzen von gebrochenen Zahlen (gemeine Brüche und Dezimalzahlen) zwischen Bild, Wort und Symbol“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 6 · Anteil an einer Menge (Kinder, Plättchen) → D [Zeilen 1815–1816]
      „Beschreiben der Anteile von Ganzen als gemeine Brüche“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 7 · Prüfungshöhe: markierten Anteil eines ungleich geteilten Kreises als Bruch ankreuzen … → keine Stelle; beschreibt eine P10-Aufgabenform, keinen RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Bruchteil einer Größe (Einheit 1)
    - Sprosse 1 · „Was ist das Ganze?“ (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Stammbruch von glatter Zahl (4×) → D [Zeilen 1889–1890]
      „Verwenden von gebrochenen Zahlen als Operator (z. B. zwei Drittel von 60 Euro)“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 3 · Zähler größer als eins (Ganzes : Nenner · Zähler) → D [Zeilen 1889–1890]
      „Verwenden von gebrochenen Zahlen als Operator (z. B. zwei Drittel von 60 Euro)“ – Block 1871–1894, Niveaustufe am Block: D (Z1885)
    - Sprosse 4 · Größe mit Einheit → D [Zeile 2136]
      „Erfassen und Bilden von Bruchteilen von Größen“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 5 · Rest zum Ganzen → keine Stelle; der RLP nennt den Rest zum Ganzen nicht; er folgt aus dem Operator, ist aber keine eigene Zeile.
    - Sprosse 6 · Ganzes mit Komma (kg, l) → D [Zeilen 2136–2137]
      „Erfassen und Bilden von Bruchteilen von Größen (in gemeinen Brüchen und Dezimalzahlen)“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 7 · Prüfungshöhe: Rest zum Ganzen bei einer zu zwei Dritteln gefüllten Tonne … → keine Stelle; P10-Aufgabenform.; Eintrag: Prüfungshöhe
  - Kürzen und Erweitern (Einheit 2)
    - Sprosse 1 · Faktor benennen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · erweitern mit gegebener Zahl (4×) → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 3 · kürzen mit gegebener Zahl → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 4 · vollständig kürzen → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 5 · auf gegebenen Nenner erweitern → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 6 · gleichnamig machen, ein Nenner Vielfaches → D [Zeilen 1820–1821]
      „gleichnamig Machen und am Zahlenstrahl“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 7 · beide erweitern → D [Zeilen 1820–1821]
      „gleichnamig Machen und am Zahlenstrahl“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 8 · gemischte Zahl ↔ unechter Bruch → D [Zeilen 1827–1828]
      „Verwenden gemischter Zahlen nur in Alltagszusammenhängen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 9 · Prüfungshöhe: abgelesenen Anteil vollständig kürzen und als Prozentsatz angeben … → keine Stelle; P10-Aufgabenform.; Eintrag: Prüfungshöhe
  - Vergleichen (Einheit 3)
    - Sprosse 1 · Vergleichsweg ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · gleicher Nenner (4×) → D [Zeilen 1817–1819]
      „Vergleichen und Ordnen von gemeinen Brüchen durch direktes Vergleichen,“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 3 · gleicher Zähler → D [Zeilen 1817–1819]
      „Vergleichen und Ordnen von gemeinen Brüchen durch direktes Vergleichen,“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 4 · mit einem Halben und mit eins → D [Zeilen 1817–1819]
      „Vergleichen und Ordnen von gemeinen Brüchen durch direktes Vergleichen,“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 5 · gleichnamig machen → D [Zeilen 1820–1821]
      „gleichnamig Machen und am Zahlenstrahl“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 6 · am Zahlenstrahl eintragen → D [Zeilen 1815–1816]
      „Anordnen von gebrochenen Zahlen am Zahlenstrahl“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 7 · drei bis vier Brüche ordnen → D [Zeilen 1817–1819]
      „Vergleichen und Ordnen von gemeinen Brüchen durch direktes Vergleichen,“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 8 · Prüfungshöhe: eine Zahl angeben, die zwischen zwei gegebenen Brüchen liegt … → D [Zeilen 1827–1829]; Eintrag: Prüfungshöhe
      „Erklären der Dichtheit der gebrochenen Zahlen auch am Zahlenstrahl“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
  - Umwandeln (Einheit 4)
    - Sprosse 1 · Nachkommastellen zählen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Zehnerbruch ↔ Dezimalzahl (4×) → D [Zeilen 1823–1824]
      „Erweitern der Stellenwerttafel (nach rechts)“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 3 · mit Nullen (Hundertstel, Tausendstel) → D [Zeilen 1823–1824]
      „Erweitern der Stellenwerttafel (nach rechts)“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 4 · am Zahlenstrahl eintragen → D [Zeilen 1822–1825]
      „Vergleichen und Ordnen von Dezimalzahlen stellenweise und am Zahlenstrahl“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 5 · erweitern auf Zehntel oder Hundertstel (Halbe, Viertel, Fünftel, Zwanzigstel) → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 6 · Dezimalzahl → D [Zeilen 1819–1822]
      „Übersetzen von gebrochenen Zahlen (gemeine Brüche und Dezimalzahlen) zwischen Bild, Wort und Symbol“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 7 · Bruch und kürzen → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 8 · Division (Achtel, Taschenrechner) → E [Zeilen 1854–1856]
      „Darstellen des Ergebnisses einer Division als gebrochene Zahl und als Dezimalzahl“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 9 · periodisch (Vorrat) → E [Zeilen 1856–1857]; Eintrag: Vorrat
      „als Dezimalzahl (auch periodische Dezimalzahlen)“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 10 · Prüfungshöhe: Bruch und Prozentangabe in dieselbe Form bringen … → keine Stelle; P10-Aufgabenform; die Handlung selbst steht in Einheit 5.; Eintrag: Prüfungshöhe
  - Vergleichen und Ordnen (Einheit 5)
    - Sprosse 1 · Nullen anhängen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · zwei Dezimalzahlen mit gleich vielen Stellen (4×) → D [Zeilen 1822–1824]
      „Vergleichen und Ordnen von Dezimalzahlen stellenweise“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 3 · verschieden viele Stellen → D [Zeilen 1822–1824]
      „Vergleichen und Ordnen von Dezimalzahlen stellenweise“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 4 · vier Zahlen ordnen → D [Zeilen 1822–1824]
      „Vergleichen und Ordnen von Dezimalzahlen stellenweise“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 5 · runden → D [Zeile 1826]
      „Runden von Dezimalzahlen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 6 · Mitte zweier Zahlen → D [Zeilen 1827–1829]
      „Erklären der Dichtheit der gebrochenen Zahlen auch am Zahlenstrahl“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 7 · Bruch gegen Dezimalzahl → D [Zeilen 1819–1822]
      „Übersetzen von gebrochenen Zahlen (gemeine Brüche und Dezimalzahlen) zwischen Bild, Wort und Symbol“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 8 · Prozent gegen Dezimalzahl → E [Zeilen 1838–1840]
      „Beschreiben von Prozenten als weitere Darstellungsform für gebrochene Zahlen“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 9 · Potenz einer Dezimalzahl → F [Zeilen 1930–1933]
      „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen Exponenten)“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 10 · Prüfungshöhe: aus vier Zahlen in vier Darstellungen die kleinste bestimmen … → F [Zeilen 1930–1933]; Eintrag: Prüfungshöhe
      „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen Exponenten)“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7, Mathematik: Rationale Zahlen“ [Zeile 477]
  - Beleg [Zeile 478]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
  - Keine eigene Reihe: die Planungshilfen setzen mit Jahrgangsstufe 7 ein, Brüche und Dezimalzahlen liegen in Klasse 5/6. Nur die Teile Vergleichen und Ordnen rationaler Zahlen und die Dezimalzahl aus der Division stehen in der Reihe „Rationale Zahlen“ (Zeilen 477–729), und die führt EBR, FOR und GYM gemeinsam.
- Spanne: nein  – Der Kern liegt auf D und E, der Vergleich gemischter Darstellungen mit Potenzen aber auf F; eine Stelle auf G oder H liefert keine Einheit und keine Sprosse – die Verortung nennt G und H nur als Ausblick.
- Ermessen (4):
  - Einheit 1 und Sprosse „Größe mit Einheit“/„Ganzes mit Komma“: die Stelle steht in einem Block von Größen und Messen, der D (Zeile 2133) und E (Zeile 2155) trägt; die Zuordnung zu D folgt der [RLP]-Zeile 6 des Eintrags, nicht einer eigenen Buchstabenmarke am Absatz.
  - Sprosse „Anteil einzeichnen“ und „Figur mit gegebenem Anteil auswählen“: der RLP nennt kein Einzeichnen; zugeordnet über das Übersetzen zwischen Bild, Wort und Symbol (Zeile 1819–1822).
  - Sprosse „ungleiche Teile gleich groß machen“ und „Rest zum Ganzen“: keine Stelle – beides sind Zwischenschritte der P10-Aufgabenformen, die der RLP nicht eigens nennt.
  - Sprosse „Dezimalzahl“ und „Bruch und kürzen“ (Einheit 4) sind zwei Stufen derselben Umwandlungskette; sie über das Übersetzen bzw. das Kürzen zu belegen ist eine Zuordnung nach Sinn, keine wörtliche Übereinstimmung.

### daten – Stufe C/D–F (Beurteilen G); Sek I + II (FOS „Beschreibende Statistik“, GOST Q2 „Lage- und Streumaße“)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Daten und Zufall, Daten. C: „Darstellen von Datenmengen (auch in Balkendiagrammen)“, „Wechsel von Darstellungsformen (Tabelle, Diagramm, Text)“, „Ablesen, Vergleichen und in Beziehung setzen einzelner Werte einer Darstellung““
  - Zeile 6 (Verortung): „D: „Erfassen und Strukturieren von selbst erhobenen Messwerten (auch Dezimalzahlen)“, „Darstellen von Messwerten in Tabellen und Diagrammen““
  - Zeile 6 (Verortung): „E: „Planen und Durchführen von statistischen Erhebungen nach vorgegebenen Fragestellungen, Merkmalen, Stichproben“, „Darstellen von Daten (auch prozentuale Angaben) in Diagrammen (auch Kreisdiagramme)““
  - Zeile 6 (Verortung): „F: „Darstellen von Daten (auch in Klassen eingeteilt) in Diagrammen (auch Boxplots und Histogramme), auch unter Verwendung digitaler Mathematikwerkzeuge““
  - Zeile 6 (Verortung): „G: „Diagramme verändern, um vorliegende Manipulationen einer Aussage zu verstehen“, „Auswerten, Interpretieren und Beurteilen der Ergebnisse statistischer Erhebungen, z. B. Erkennen von Trends““
  - Zeile 6 (Verortung): „H: „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und Streumaßen (z. B. Spannweite und Breite der Box bei Boxplots)“.“
  - Zeile 33 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2024-OS-B1h, 2019-OS-B1i]“
  - Zeile 35 (Voraussetzungen (Blatt 0)): „[RLP E; P10 2025-OS-K6b, 2021-OS-K5b]“
  - Zeile 36 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 47 (Merkkasten): „[RLP E; P10 2025-OS-K6a]“
  - Zeile 60 (Merkkasten): „[RLP E]“
  - Zeile 69 (Merkkasten): „[RLP C/D]“
  - Zeile 78 (Merkkasten): „[RLP E]“
  - Zeile 88 (Merkkasten): „[RLP D/E]“
  - Zeile 98 (Merkkasten): „[RLP F/G]“
  - Zeile 138 (Für schwache Schüler): „[RLP C/D, MO]“
- Lerneinheiten:
  - 1. Häufigkeiten – C/E
    - E [Zeilen 3072–3074]: „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“
      Block 3064–3074, Niveaustufe am Block: kein Buchstabe; Grundfall; der Block 3064–3074 trägt keinen Buchstaben, der Buchstabe E steht im folgenden Block (Zeile 3076)
    - C [Zeilen 2985–2987]: „Nennen von seltenstem und häufigstem Wert bei Häufigkeitsverteilungen“
      Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990); häufigster und seltenster Wert stehen schon auf C
  - 2. Säulen-, Balken- und Liniendiagramme – C/D/F
    - C [Zeilen 2982–2984]: „Ablesen, Vergleichen und in Beziehung setzen einzelner Werte einer Darstellung“
      Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990); das Lesen steht schon auf C
    - D [Zeilen 2998–2999]: „Darstellen von Messwerten in Tabellen und Diagrammen“
      Block 2998–3002, Niveaustufe am Block: D (Z3001); das Zeichnen auf D
    - F [Zeilen 3081–3083]: „Lesen, Verstehen und Beschreiben von Darstellungen statistischer Erhebungen aus dem“
      Block 3081–3093, Niveaustufe am Block: F (Z3086); Alltagsdarstellungen auf F
  - 3. Streifen- und Kreisdiagramm – E
    - E [Zeilen 3067–3069]: „Darstellen von Daten (auch prozentuale Angaben) in Diagrammen (auch“
      Block 3064–3074, Niveaustufe am Block: kein Buchstabe; das Kreisdiagramm steht ausdrücklich auf E
      Ermessen: Den Mittelpunktswinkel und das Streifendiagramm nennt der Teil C nicht; sie sind über die proportionale Zuordnung (E) und das Berechnen von Winkelgrößen (D) belegt.
  - 4. Kenngrößen – D/E
    - D [Zeilen 2998–3000]: „Ermitteln und Vergleichen von Kennwerten (auch Minimum, Maximum und Spannweite)“
      Block 2998–3002, Niveaustufe am Block: D (Z3001); Minimum, Maximum und Spannweite stehen auf D
    - E [Zeilen 3067–3069]: „Ermitteln und Vergleichen von arithmetischem Mittel, Modalwert (häufigster Wert) und Median“
      Block 3064–3074, Niveaustufe am Block: kein Buchstabe; Mittelwert, Modalwert und Median auf E
  - 5. Diagramme beurteilen und Boxplot – F/G
    - G [Zeilen 3102–3104]: „Erkennen von typischen Fehlern und Manipulationen bei grafischen Darstellungen“
      Block 3095–3107, Niveaustufe am Block: G (Z3102); das Beurteilen steht auf G
    - F [Zeilen 3091–3093]: „Vergleichen verschiedener Darstellungsformen (auch Boxplots)“
      Block 3081–3093, Niveaustufe am Block: F (Z3086); der Boxplot auf F
  - 6. Kenngrößen aus Häufigkeitstabellen und Klassen (Sek II) – H
    - H [Zeilen 3110–3112]: „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und“
      Block 3110–3115, Niveaustufe am Block: H (Z3113); die Streumaße sind der Sek-I-Vorläufer der Standardabweichung; die Einheit selbst ist eine Sek-II-Einheit (FOS Pflichtthema 4, GOST Q2)
      Ermessen: „Standardabweichung“, „gewichtetes Mittel“, „Klassenmitte“ und „Medianklasse“ kommen im Teil C nicht vor; nur die Streumaße (H) sind ein Vorläufer.
- Sprossen je Verfahrenstyp:
  - Häufigkeiten (Einheit 1)
    - Sprosse 1 · Ganzes unterstreichen (Vorstufe) → E [Zeilen 3072–3074]; Eintrag: Vorstufe
      „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 2 · Strichliste auszählen (4×) → C [Zeilen 2973–2974]
      „Lesen von Strichlisten und Tabellen (mit einer“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 3 · Häufigkeitstabelle aus einer Urliste → D [Zeilen 2998–3000]
      „Erfassen und Strukturieren von selbst erhobenen Messwerten“ – Block 2998–3002, Niveaustufe am Block: D (Z3001)
    - Sprosse 4 · relative Häufigkeit als Bruch → E [Zeilen 3072–3074]
      „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 5 · kürzen → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 6 · als Dezimalzahl mit Taschenrechner → E [Zeilen 3072–3074]
      „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 7 · in Prozent, runden → E [Zeilen 3072–3074]
      „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 8 · Summe der Anteile prüfen → keine Stelle; Die Probe „Summe gleich eins“ nennt der Teil C nicht.
    - Sprosse 9 · aus einem Diagramm (Anzahl und Gesamtzahl ablesen) → C [Zeilen 2982–2984]
      „Ablesen, Vergleichen und in Beziehung setzen einzelner Werte einer Darstellung“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 10 · Anzahl aus Anteil und Gesamtzahl → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 11 · zwei Gruppen vergleichen → E [Zeilen 3072–3074]
      „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 12 · Prüfungshöhe: relative Häufigkeit eines Siegs als Bruch und in Prozent … → E [Zeilen 3072–3074]; Eintrag: Prüfungshöhe
      „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
  - Diagramme lesen (Einheit 2)
    - Sprosse 1 · Kästchenwert angeben (Vorstufe) → G [Zeilen 2902–2903]; Eintrag: Vorstufe
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · Säule an beschrifteter Linie ablesen (4×) → C [Zeilen 2982–2984]
      „Ablesen, Vergleichen und in Beziehung setzen einzelner Werte einer Darstellung“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 3 · zwischen zwei Linien (Hilfslinien zählen) → C [Zeilen 2982–2984]
      „Ablesen, Vergleichen und in Beziehung setzen einzelner Werte einer Darstellung“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 4 · Achse „in Tausend“ → keine Stelle; Die Einheit an der Achse nennt der Teil C nicht.
    - Sprosse 5 · Werte über oder unter einer Schwelle (Grenzwert) → C [Zeilen 2982–2984]
      „Ablesen, Vergleichen und in Beziehung setzen einzelner Werte einer Darstellung“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 6 · größte, kleinste, Differenz → C [Zeilen 2985–2987]
      „Nennen von seltenstem und häufigstem Wert bei Häufigkeitsverteilungen“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 7 · Balken statt Säulen → C [Zeilen 2982–2983]
      „Darstellen von Datenmengen (auch in Balkendiagrammen)“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 8 · Säule mit gegebenem Wert ergänzen → D [Zeilen 2998–2999]
      „Darstellen von Messwerten in Tabellen und Diagrammen“ – Block 2998–3002, Niveaustufe am Block: D (Z3001)
    - Sprosse 9 · Achseneinteilung aus einer bekannten Säule → G [Zeilen 2902–2903]
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 10 · unbeschriftete Säule zuordnen und weitere zeichnen → D [Zeilen 2998–2999]
      „Darstellen von Messwerten in Tabellen und Diagrammen“ – Block 2998–3002, Niveaustufe am Block: D (Z3001)
    - Sprosse 11 · Liniendiagramm lesen → C [Zeilen 2982–2984]
      „Ablesen, Vergleichen und in Beziehung setzen einzelner Werte einer Darstellung“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 12 · Prüfungshöhe: Skala aus einer Säule erschließen, Säulen zuordnen und ergänzen … → G [Zeilen 2902–2903]; Eintrag: Prüfungshöhe
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Anteile darstellen (Einheit 3)
    - Sprosse 1 · Prozent oder Grad ankreuzen (Vorstufe) → E [Zeilen 3067–3069]; Eintrag: Vorstufe
      „Darstellen von Daten (auch prozentuale Angaben) in Diagrammen (auch“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 2 · Prozent → E [Zeilen 1838–1839]
      „Beschreiben von Prozenten als weitere Darstellungsform für“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 3 · Streifenabschnitt (4×) → E [Zeilen 3067–3069]
      „Darstellen von Daten (auch prozentuale Angaben) in Diagrammen (auch“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 4 · Streifen mit mehreren Abschnitten zeichnen → E [Zeilen 3067–3069]
      „Darstellen von Daten (auch prozentuale Angaben) in Diagrammen (auch“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 5 · Rest zu hundert Prozent → keine Stelle; Der Rest zum Ganzen wird im Teil C nicht eigens genannt.
    - Sprosse 6 · Prozent → E [Zeilen 1838–1839]
      „Beschreiben von Prozenten als weitere Darstellungsform für“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 7 · Winkel mit glatten Zahlen (Viertel als rechter Winkel, Hälfte als gestreckter Winkel) → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 8 · beliebiger Prozentsatz (Anteil mal Vollwinkel) → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 9 · Anteil als „von“ (kleine Anzahl aus großer Grundmenge) → E [Zeilen 3072–3074]
      „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 10 · Sektor ab dem Radius zeichnen → D [Zeilen 2444–2446]
      „Zeichnen von Winkeln und ebenen Figuren mithilfe von Zeichengeräten (Lineal,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 11 · Kreisdiagramm mit drei Sektoren → E [Zeilen 3067–3069]
      „Darstellen von Daten (auch prozentuale Angaben) in Diagrammen (auch“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 12 · Sektoren nach Größe zuordnen → C [Zeilen 2982–2984]
      „Ablesen, Vergleichen und in Beziehung setzen einzelner Werte einer Darstellung“ – Block 2966–2993, Niveaustufe am Block: A (Z2970), B (Z2977), C (Z2990)
    - Sprosse 13 · Prüfungshöhe: Sektoren zuordnen und den Mittelpunktswinkel berechnen … → E [Zeilen 3067–3069]; Eintrag: Prüfungshöhe
      „Darstellen von Daten (auch prozentuale Angaben) in Diagrammen (auch“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
  - Kenngrößen (Einheit 4)
    - Sprosse 1 · Kenngröße ankreuzen (Vorstufe) → D [Zeilen 2998–3000]; Eintrag: Vorstufe
      „Ermitteln und Vergleichen von Kennwerten (auch Minimum, Maximum und Spannweite)“ – Block 2998–3002, Niveaustufe am Block: D (Z3001)
    - Sprosse 2 · Minimum und Maximum aus einer Liste (4×) → D [Zeilen 2998–3000]
      „Ermitteln und Vergleichen von Kennwerten (auch Minimum, Maximum und Spannweite)“ – Block 2998–3002, Niveaustufe am Block: D (Z3001)
    - Sprosse 3 · Spannweite → D [Zeilen 2998–3000]
      „Ermitteln und Vergleichen von Kennwerten (auch Minimum, Maximum und Spannweite)“ – Block 2998–3002, Niveaustufe am Block: D (Z3001)
    - Sprosse 4 · Modalwert → E [Zeilen 3067–3069]
      „Ermitteln und Vergleichen von arithmetischem Mittel, Modalwert (häufigster Wert) und Median“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 5 · Median bei ungerader Anzahl (sortieren) → E [Zeilen 3067–3069]
      „Ermitteln und Vergleichen von arithmetischem Mittel, Modalwert (häufigster Wert) und Median“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 6 · Median bei gerader Anzahl → E [Zeilen 3067–3069]
      „Ermitteln und Vergleichen von arithmetischem Mittel, Modalwert (häufigster Wert) und Median“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 7 · Mittelwert aus kurzer Liste → E [Zeilen 3067–3069]
      „Ermitteln und Vergleichen von arithmetischem Mittel, Modalwert (häufigster Wert) und Median“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 8 · Dezimalzahlen mit Taschenrechner → E [Zeilen 1901–1902]
      „Prüfen und Übertragen der bekannten operativen Strategien, Gesetze und Verfahren auf das Rechnen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 9 · aus Tabelle oder Diagramm → E [Zeilen 3067–3069]
      „Ermitteln und Vergleichen von arithmetischem Mittel, Modalwert (häufigster Wert) und Median“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 10 · sinnvoll runden → E [Zeilen 1909–1910]
      „Angeben von Ergebnissen mit sinnvoller Genauigkeit (auch beim Rechnen mit rationalen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 11 · Mittel aus Summe und Anzahl → E [Zeilen 3067–3069]
      „Ermitteln und Vergleichen von arithmetischem Mittel, Modalwert (häufigster Wert) und Median“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 12 · fehlender Wert aus dem Mittel → keine Stelle; Das Rückwärtsrechnen aus dem Mittelwert nennt der Teil C nicht.
    - Sprosse 13 · Aussagen prüfen und korrigieren → G [Zeilen 3095–3097]
      „Auswerten, Interpretieren und Beurteilen der Ergebnisse statistischer Erhebungen, z. B.“ – Block 3095–3107, Niveaustufe am Block: G (Z3102)
    - Sprosse 14 · Mittelwert nach einer Änderung begründen → H [Zeilen 3110–3112]
      „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und“ – Block 3110–3115, Niveaustufe am Block: H (Z3113)
    - Sprosse 15 · Prüfungshöhe: Durchschnittsalter und Begründung, warum es sich nicht ändert … → H [Zeilen 3110–3112]; Eintrag: Prüfungshöhe
      „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und“ – Block 3110–3115, Niveaustufe am Block: H (Z3113)
  - Beurteilen (Einheit 5)
    - Sprosse 1 · Achsenanfang ankreuzen (Vorstufe) → G [Zeilen 3102–3104]; Eintrag: Vorstufe
      „Erkennen von typischen Fehlern und Manipulationen bei grafischen Darstellungen“ – Block 3095–3107, Niveaustufe am Block: G (Z3102)
    - Sprosse 2 · Aussage mit einem Wert prüfen (4×) → F [Zeilen 3081–3083]
      „Lesen, Verstehen und Beschreiben von Darstellungen statistischer Erhebungen aus dem“ – Block 3081–3093, Niveaustufe am Block: F (Z3086)
    - Sprosse 3 · Aussage mit Vergleich zweier Werte (Anstieg, Rückgang) → F [Zeilen 3081–3083]
      „Lesen, Verstehen und Beschreiben von Darstellungen statistischer Erhebungen aus dem“ – Block 3081–3093, Niveaustufe am Block: F (Z3086)
    - Sprosse 4 · „mehr als die Hälfte“, „um ein Drittel“ nachrechnen → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 5 · „jede 15.“ umrechnen → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 6 · zwei Teilaussagen getrennt prüfen → G [Zeilen 3095–3097]
      „Auswerten, Interpretieren und Beurteilen der Ergebnisse statistischer Erhebungen, z. B.“ – Block 3095–3107, Niveaustufe am Block: G (Z3102)
    - Sprosse 7 · abgeschnittene Achse erklären → G [Zeilen 3102–3104]
      „Erkennen von typischen Fehlern und Manipulationen bei grafischen Darstellungen“ – Block 3095–3107, Niveaustufe am Block: G (Z3102)
    - Sprosse 8 · Verdopplung der Säule gegen Veränderung des Werts → G [Zeilen 3102–3104]
      „Erkennen von typischen Fehlern und Manipulationen bei grafischen Darstellungen“ – Block 3095–3107, Niveaustufe am Block: G (Z3102)
    - Sprosse 9 · Trend und Fortschreibung → G [Zeilen 3095–3097]
      „Auswerten, Interpretieren und Beurteilen der Ergebnisse statistischer Erhebungen, z. B.“ – Block 3095–3107, Niveaustufe am Block: G (Z3102)
    - Sprosse 10 · Diagramm mit Achse ab null skizzieren → G [Zeilen 3100–3102]
      „Diagramme verändern, um vorliegende Manipulationen einer Aussage zu verstehen“ – Block 3095–3107, Niveaustufe am Block: G (Z3102)
    - Sprosse 11 · Boxplot lesen (Vorrat) → F [Zeilen 3091–3093]; Eintrag: Vorrat
      „Vergleichen verschiedener Darstellungsformen (auch Boxplots)“ – Block 3081–3093, Niveaustufe am Block: F (Z3086)
    - Sprosse 12 · Prüfungshöhe: Aussage prüfen und die abgeschnittene Achse als Grund der Verzerrung benennen … → G [Zeilen 3102–3104]; Eintrag: Prüfungshöhe
      „Erkennen von typischen Fehlern und Manipulationen bei grafischen Darstellungen“ – Block 3095–3107, Niveaustufe am Block: G (Z3102)
  - Häufigkeiten, Sek II (Einheit 1)
    - Sprosse 1 · Ganzes unterstreichen (Vorstufe) → keine Stelle; Sek-II-Zeile (fhr/iqb); für sie gelten RLP FOS und GOST.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · relative Häufigkeiten aller Sorten einer Tabelle, Summe prüfen (Grundfall) → E [Zeilen 3072–3074]; Eintrag: Sek II
      „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 3 · relative Häufigkeiten je Klasse aus einer Klasseneinteilung → F [Zeilen 3081–3083]; Eintrag: Sek II
      „Darstellen von Daten (auch in Klassen eingeteilt) in Diagrammen (auch“ – Block 3081–3093, Niveaustufe am Block: F (Z3086)
    - Sprosse 4 · die Anteile in einem Häufigkeitsdiagramm darstellen, zwei Gruppen als gruppierte Säulen → E [Zeilen 3067–3069]; Eintrag: Sek II
      „Darstellen von Daten (auch prozentuale Angaben) in Diagrammen (auch“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 5 · die relative Häufigkeit aus der Restanzahl → keine Stelle; Sek-II-Zeile (iqb); keine Stelle im RLP 1–10.; Eintrag: Sek II
    - Sprosse 6 · eine Vierfeldertafel mit absoluten Anzahlen über die Randsummen füllen → keine Stelle; Sek-II-Zeile (fhr); die Vierfeldertafel steht im Teil C unter Zählstrategien (G), nicht unter Daten.; Eintrag: Sek II
    - Sprosse 7 · begründen, wie sich Häufigkeiten bei größerer Stichprobe ändern → keine Stelle; Sek-II-Zeile (fhr); keine Stelle im RLP 1–10.; Eintrag: Sek II
    - Sprosse 8 · Prüfungshöhe: Anteile hochrechnen, aufrunden, Menge für absolute Sicherheit angeben … → keine Stelle; Sek-II-Zeile (fhr); keine Stelle im RLP 1–10.; Eintrag: Prüfungshöhe, Sek II
  - Kenngrößen aus Listen, Sek II (Einheit 4)
    - Sprosse 1 · Sortiert? (Vorstufe) → keine Stelle; Sek-II-Zeile (fhr); keine Stelle im RLP 1–10.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · Mittelwert und Standardabweichung einer Liste mit dem Rechner (Grundfall) → H [Zeilen 3110–3112]; Eintrag: Sek II
      „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und“ – Block 3110–3115, Niveaustufe am Block: H (Z3113)
    - Sprosse 3 · Median, Mittelwert und Standardabweichung in einer Teilaufgabe → H [Zeilen 3110–3112]; Eintrag: Sek II
      „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und“ – Block 3110–3115, Niveaustufe am Block: H (Z3113)
    - Sprosse 4 · den fehlenden Wert aus dem Mittel in Zeiteinheiten → keine Stelle; Sek-II-Zeile (iqb); das Rückwärtsrechnen aus dem Mittelwert nennt der Teil C nicht.; Eintrag: Sek II
    - Sprosse 5 · Prüfungshöhe: Median und Mittelwert an einem Ausreißer vergleichen … → H [Zeilen 3110–3112]; Eintrag: Prüfungshöhe, Sek II
      „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und“ – Block 3110–3115, Niveaustufe am Block: H (Z3113)
  - Kenngrößen aus Tabellen und Klassen (Einheit 6)
    - Sprosse 1 · „Gewichtet oder ungewichtet?“ und „Wert oder Klasse?“ ankreuzen (Vorstufe) → keine Stelle; Sek-II-Zeile; „gewichtetes Mittel“ kommt im Teil C nicht vor.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · gewichtetes Mittel aus einer kleinen Häufigkeitstabelle (Grundfall) → keine Stelle; wie Sprosse 1: keine Stelle.; Eintrag: Sek II
    - Sprosse 3 · Median und Modalwert aus der Tabelle → E [Zeilen 3067–3069]; Eintrag: Sek II
      „Ermitteln und Vergleichen von arithmetischem Mittel, Modalwert (häufigster Wert) und Median“ – Block 3064–3074, Niveaustufe am Block: kein Buchstabe
    - Sprosse 4 · die Standardabweichung aus der Tabelle mit gewichteten Abweichungsquadraten → H [Zeilen 3110–3112]; Eintrag: Sek II
      „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und“ – Block 3110–3115, Niveaustufe am Block: H (Z3113)
    - Sprosse 5 · Klassenmitten bilden und Mittelwert und Standardabweichung aus Klassen → F [Zeilen 3081–3083]; Eintrag: Sek II
      „Darstellen von Daten (auch in Klassen eingeteilt) in Diagrammen (auch“ – Block 3081–3093, Niveaustufe am Block: F (Z3086)
    - Sprosse 6 · die Medianklasse über kumulierte Häufigkeiten und am Säulendiagramm → keine Stelle; „Medianklasse“ und kumulierte Häufigkeiten kommen im Teil C nicht vor.; Eintrag: Sek II
    - Sprosse 7 · den unbekannten Wert aus dem Zielmittelwert und den Gruppenschnitt bestimmen → keine Stelle; Sek-II-Zeile (fhr); keine Stelle im RLP 1–10.; Eintrag: Sek II
    - Sprosse 8 · zwei Jahrgänge über Mittelwert und Standardabweichung vergleichen → H [Zeilen 3110–3112]; Eintrag: Sek II
      „Analysieren, Interpretieren von Mittelwerten (arithmetisches Mittel, Median, Modalwerte) und“ – Block 3110–3115, Niveaustufe am Block: H (Z3113)
    - Sprosse 9 · Prüfungshöhe: gewichtete Summe von Intervallgrenzen als untere Schranke des Mittelwerts deuten … → keine Stelle; Anforderungsbereich III der Oberstufe; keine Stelle im RLP 1–10.; Eintrag: Prüfungshöhe, Sek II
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Daten und Zufall“ [Zeile 1454]; „Jahrgangsstufe 9/10, Mathematik: Daten und Zufall“ [Zeile 2246]
  - Beleg [Zeile 1455]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung“
  - Beide Reihen führen EBR, FOR und GYM gemeinsam und tragen den Differenzierungshinweis (Zeilen 1455 und 2248). Die Reihe 7/8 hat Blöcke auf E (Zeile 1461) und F (Zeile 1530), die Reihe 9/10 auf G (Zeile 2254) und H (Zeile 2318).
- Spanne: ja  – Die Stufen reichen von C (Ablesen, Balkendiagramm) über D (Kennwerte), E (Mittelwerte, Kreisdiagramm) und F (Boxplot, Klassen) bis G (Beurteilen) und H (Mittelwerte und Streumaße analysieren). Damit stehen Einheiten auf G und H und mehrere auf F und darunter.
- Ermessen (6):
  - Die E-Zeilen zu Daten stehen in einem Block ohne Buchstaben am Rand (Zeilen 3064–3074); der Buchstabe E steht im folgenden Block (Zeile 3076). Die Zuordnung folgt der Verortung des Eintrags.
  - Einheit 3: „Mittelpunktswinkel“ und „Streifendiagramm“ kommen im Teil C nicht vor. Der Winkel ist über die proportionale Zuordnung (E) und das Berechnen von Winkelgrößen (D) belegt.
  - Einheit 6 im Ganzen: „Standardabweichung“, „gewichtetes Mittel“, „Klassenmitte“ und „Medianklasse“ fehlen im Teil C; nur „Streumaße“ (H) ist ein Vorläufer. Fünf der neun Sprossen tragen „keine Stelle“.
  - Sprossen „fehlender Wert aus dem Mittel“ (Einheit 4 und Sek-II-Kette): keine Stelle; das Rückwärtsrechnen aus dem Mittelwert nennt der Teil C nicht, obwohl es ein P10-Typ ist.
  - Sprossen „Summe der Anteile prüfen“, „Achse in Tausend“, „Rest zu hundert Prozent“: keine Stelle; alle drei sind Aufgabenformen.
  - Die drei Sek-II-Ketten sind gemischt belegt: wo der RLP 1–10 dieselbe Handlung kennt (relative Häufigkeit E, Klassen F, Mittelwerte und Streumaße H), steht eine Stelle; Vierfeldertafel, Medianklasse und Rückwärtsrechnungen tragen „keine Stelle“.

### einheiten – Stufe D–E (Vorsätze F, Systematisierung G); Sek I + II
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Größen und Messen D (S. 46, Größenvorstellungen und Messen): „Unterscheiden verschiedener Größen (auch Flächeninhalt, Volumen und Winkel)““
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP D „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln“; P10 2019-OS-B1b, 2022-OS-B1h Fehlerquellen]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D; MSK D2B]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2019-OS-B1b]“
  - Zeile 32 (Voraussetzungen (Blatt 0)): „[RLP D „Erfassen und Bilden von Bruchteilen von Größen“]“
  - Zeile 34 (Voraussetzungen (Blatt 0)): „[RLP E „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“; P10 2016-OS-K3d Voraussetzung „Dichteformel umstellen“]“
  - Zeile 36 (Voraussetzungen (Blatt 0)): „[RLP C „Erklären von Einheiten und Untereinheiten zur Beschreibung einer entsprechenden Skala“]“
  - Zeile 43 (Merkkasten): „[RLP D „Zuordnen von Größenangaben zu vertrauten Objekten“; LISUM-PH „Kennen von Repräsentanten“]“
  - Zeile 44 (Merkkasten): „[RLP B „Unterscheiden zwischen Zeitpunkt und Zeitspanne“]“
  - Zeile 60 (Merkkasten): „[RLP D/E]“
  - Zeile 67 (Typische Fehler): „[RLP B]“
  - Zeile 77 (Typische Fehler): „[RLP D/E/F]“
  - Zeile 87 (Typische Fehler): „[RLP E]“
  - Zeile 109 (Für schwache Schüler): „[RLP D, LISUM-PH, MO]“
- Lerneinheiten:
  - 1. Länge, Masse, Geld – C/D/E
    - D [Zeilen 2132–2134]: „Umwandeln und Ordnen von Einheiten bekannter Größen und Darstellen in unterschiedlichen Schreibweisen (unter Anwendung der“
      Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155); Grundfall
    - C [Zeilen 2034–2036]: „Umwandeln und Ordnen von Größenangaben mit den oben genannten Einheiten und Darstellen in unterschiedlichen Schreibweisen“
      Block 2018–2066, Niveaustufe am Block: A (Z2022), B (Z2033), C (Z2056); die Einheiten selbst stehen schon auf C
    - E [Zeilen 2152–2153]: „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“
      Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155); das systematische Umrechnen über die Zusammenhänge aller Größenarten
  - 2. Zeit – B/C/E
    - B [Zeile 2039]: „Unterscheiden zwischen Zeitpunkt und Zeitspanne“
      Block 2018–2066, Niveaustufe am Block: A (Z2022), B (Z2033), C (Z2056); die Grundunterscheidung steht schon auf B
    - C [Zeilen 2060–2062]: „Erklären von Einheiten und Untereinheiten zur Beschreibung einer entsprechenden Skala (z. B. am Lineal und an der Uhr)“
      Block 2018–2066, Niveaustufe am Block: A (Z2022), B (Z2033), C (Z2056); die Uhr als Skala
    - E [Zeilen 2152–2153]: „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“
      Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155); das Umrechnen der Zeiteinheiten; der Spiegelstrich „− der Zeit“ steht in derselben Liste
      Ermessen: Die Dezimalstunde (1,5 h = 90 min) nennt der RLP nicht; sie ist im Eintrag der häufigste P10-Typ der Einheit.
  - 3. Flächen- und Volumeneinheiten – D/F/G
    - D [Zeilen 2129–2130]: „Angeben von Flächeninhalten und Volumina in dezimalen Einheiten“
      Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155); Grundfall
    - F [Zeilen 2221–2223]: „auch unter Nutzung der Zehnerpotenzen zur Beschreibung von Einheitenvorsätzen von Milli bis Kilo“
      Block 2217–2244, Niveaustufe am Block: F (Z2226), G (Z2240); Einheitenvorsätze Milli bis Kilo
    - G [Zeilen 2236–2238]: „Erweiterung der Nutzung der Zehnerpotenzen zur Beschreibung von Einheitenvorsätzen von Nano bis Tera im Anwendungsbezug“
      Block 2217–2244, Niveaustufe am Block: F (Z2226), G (Z2240); Vorsätze Nano bis Tera; im Eintrag als Vorrat geführt
  - 4. Mit Größen rechnen im Sachzusammenhang – D/E/F
    - E [Zeile 2189]: „Verwenden von Größenangaben in Rechnungen (auch Geschwindigkeiten, Dichten)“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); die Dichte steht ausdrücklich auf E
    - D [Zeilen 2173–2174]: „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und auch in Dezimalschreibweise), insbesondere in Sachkontexten“
      Block 2170–2184, Niveaustufe am Block: D (Z2184); Grundfall Sachkontext
    - F [Zeile 2266]: „Vertiefen der Kompetenzen zum Rechnen mit Größen im Zusammenhang mit berufsorientierten“
      Block 2263–2276, Niveaustufe am Block: F (Z2271); Materialbedarf und Gebindegrößen als berufsorientierter Kontext
- Sprossen je Verfahrenstyp:
  - Länge, Masse und Geld umrechnen (Einheit 1)
    - Sprosse 1 · „größer oder kleiner“ und „mal oder geteilt“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · in die Nachbareinheit, große in kleine Einheit, glatte Zahlen (4×) → D [Zeilen 2132–2134]
      „Umwandeln und Ordnen von Einheiten bekannter Größen und Darstellen in unterschiedlichen Schreibweisen (unter Anwendung der“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 3 · Nachbareinheit, kleine in große Einheit → D [Zeilen 2132–2134]
      „Umwandeln und Ordnen von Einheiten bekannter Größen und Darstellen in unterschiedlichen Schreibweisen (unter Anwendung der“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 4 · über zwei Stufen (Millimeter in Meter) → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 5 · Kilometer und Meter → C [Zeilen 2034–2036]
      „Umwandeln und Ordnen von Größenangaben mit den oben genannten Einheiten und Darstellen in unterschiedlichen Schreibweisen“ – Block 2018–2066, Niveaustufe am Block: A (Z2022), B (Z2033), C (Z2056)
    - Sprosse 6 · Massen von Gramm bis Tonne → C [Zeilen 2034–2036]
      „Umwandeln und Ordnen von Größenangaben mit den oben genannten Einheiten und Darstellen in unterschiedlichen Schreibweisen“ – Block 2018–2066, Niveaustufe am Block: A (Z2022), B (Z2033), C (Z2056)
    - Sprosse 7 · Geld: Euro und Cent → C [Zeilen 2034–2036]
      „Umwandeln und Ordnen von Größenangaben mit den oben genannten Einheiten und Darstellen in unterschiedlichen Schreibweisen“ – Block 2018–2066, Niveaustufe am Block: A (Z2022), B (Z2033), C (Z2056)
    - Sprosse 8 · gemischte Angabe in eine Einheit bringen und zurück → D [Zeilen 2138–2139]
      „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln sowie“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 9 · Angaben mit Komma (Stellenwerttafel) → D [Zeilen 2138–2139]
      „Erklären von Größenangaben mit Dezimalzahlen mithilfe der erweiterten Stellenwerttafeln sowie“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 10 · Prüfungshöhe: zwei Größen verschiedener Einheit vergleichen; Länge mit gegebenem Faktor … → D [Zeilen 2132–2134]; Eintrag: Prüfungshöhe
      „Umwandeln und Ordnen von Einheiten bekannter Größen und Darstellen in unterschiedlichen Schreibweisen (unter Anwendung der“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
  - Zeit umrechnen und Zeitspannen berechnen (Einheit 2)
    - Sprosse 1 · „Zeitpunkt oder Zeitspanne“ und „Komma oder Doppelpunkt“ ankreuzen (Vorstufe) → B [Zeile 2039]; Eintrag: Vorstufe
      „Unterscheiden zwischen Zeitpunkt und Zeitspanne“ – Block 2018–2066, Niveaustufe am Block: A (Z2022), B (Z2033), C (Z2056)
    - Sprosse 2 · Minuten in Sekunden und Stunden in Minuten, glatte Zahlen (4×) → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 3 · Sekunden in Minuten, Minuten in Stunden → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 4 · halbe und viertel Stunden in Minuten → C [Zeilen 2061–2062]
      „Nutzen von gebräuchlichen Bruchzahlen (halb, viertel, drei viertel) bei Größenangaben“ – Block 2018–2066, Niveaustufe am Block: A (Z2022), B (Z2033), C (Z2056)
    - Sprosse 5 · Dezimalstunde in Minuten → keine Stelle; Die Dezimalstunde nennt der RLP nicht; er kennt nur das Umwandeln zwischen den Zeiteinheiten.
    - Sprosse 6 · Minuten als Dezimalstunde → keine Stelle; wie Sprosse 5: keine Stelle.
    - Sprosse 7 · Zeitspanne zwischen zwei Uhrzeiten ohne Übertrag → B [Zeile 2085]
      „Berechnen von Zeitspannen als Differenz von zwei Zeitpunkten innerhalb“ – Block 2083–2087, Niveaustufe am Block: kein Buchstabe
    - Sprosse 8 · mit Übertrag → B [Zeile 2085]
      „Berechnen von Zeitspannen als Differenz von zwei Zeitpunkten innerhalb“ – Block 2083–2087, Niveaustufe am Block: kein Buchstabe
    - Sprosse 9 · Dauer mit Pause in zwei Abschnitten → B [Zeile 2085]
      „Berechnen von Zeitspannen als Differenz von zwei Zeitpunkten innerhalb“ – Block 2083–2087, Niveaustufe am Block: kein Buchstabe
    - Sprosse 10 · Prüfungshöhe: Dezimalstunde in Minuten; Ankunftszeit mit Übertrag … → B [Zeile 2085]; Eintrag: Prüfungshöhe
      „Berechnen von Zeitspannen als Differenz von zwei Zeitpunkten innerhalb“ – Block 2083–2087, Niveaustufe am Block: kein Buchstabe
  - Flächen- und Volumeneinheiten umrechnen (Einheit 3)
    - Sprosse 1 · „welche Umrechnungszahl“ und „passt die Angabe“ ankreuzen (Vorstufe) → keine Stelle; Der RLP nennt das Wort „Umrechnungszahl“ nicht.; Eintrag: Vorstufe
    - Sprosse 2 · Flächeneinheiten der Größe nach ordnen → D [Zeilen 2129–2130]
      „Angeben von Flächeninhalten und Volumina in dezimalen Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 3 · Flächeneinheit in die Nachbareinheit (4×) → D [Zeilen 2132–2134]
      „Umwandeln und Ordnen von Einheiten bekannter Größen und Darstellen in unterschiedlichen Schreibweisen (unter Anwendung der“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 4 · über zwei Stufen → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 5 · a und ha einordnen → E [Zeilen 2145–2146]
      „situationsangemessenes Verwenden von Größen und ihren Einheiten (auch a, ha, km²)“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 6 · Volumeneinheiten ordnen → D [Zeilen 2129–2130]
      „Angeben von Flächeninhalten und Volumina in dezimalen Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 7 · Volumeneinheit in die Nachbareinheit → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 8 · Liter und Kubikdezimeter, Milliliter und Kubikzentimeter gleichsetzen → keine Stelle; Die Gleichsetzung von Hohlmaß und Kubikmaß nennt der RLP nicht; er führt Liter und Kubikeinheiten nur nebeneinander auf.
    - Sprosse 9 · Liter in Milliliter und Kubikmeter in Liter → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 10 · Vorsätze als Namen lesen (Vorrat: Nano bis Tera) → G [Zeilen 2236–2238]; Eintrag: Vorrat
      „Erweiterung der Nutzung der Zehnerpotenzen zur Beschreibung von Einheitenvorsätzen von Nano bis Tera im Anwendungsbezug“ – Block 2217–2244, Niveaustufe am Block: F (Z2226), G (Z2240)
    - Sprosse 11 · Prüfungshöhe: Portionen aus einer Gesamtmenge; Dauer aus Menge und Durchsatz … → E [Zeilen 2152–2153]; Eintrag: Prüfungshöhe
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
  - Mit Größen rechnen im Sachzusammenhang (Einheit 4)
    - Sprosse 1 · „gleiche Einheit“ und „gegeben, gesucht“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · zwei Angaben verschiedener Einheit angleichen und addieren (4×) → D [Zeilen 2173–2174]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und auch in Dezimalschreibweise), insbesondere in Sachkontexten“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 3 · Ergebnis in eine handlichere Einheit umrechnen → E [Zeilen 2154–2155]
      „Angeben von Größen mit sinnvoller Genauigkeit“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 4 · Masse aus Volumen und Dichte → E [Zeile 2189]
      „Verwenden von Größenangaben in Rechnungen (auch Geschwindigkeiten, Dichten)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · Volumen aus Masse und Dichte (Formel umstellen) → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 6 · Masse eines Anteils in Prozent, Leermasse addieren → D [Zeile 2136]
      „Erfassen und Bilden von Bruchteilen von Größen“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 7 · Materialbedarf aus einer Fläche und der Ergiebigkeit → F [Zeile 2266]
      „Vertiefen der Kompetenzen zum Rechnen mit Größen im Zusammenhang mit berufsorientierten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 8 · mehrere Flächen und zweiter Anstrich → F [Zeile 2266]
      „Vertiefen der Kompetenzen zum Rechnen mit Größen im Zusammenhang mit berufsorientierten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 9 · Bedarf mit Gebindegrößen vergleichen und entscheiden → F [Zeile 2275]
      „kritisches Bewerten von Rechenergebnissen sowie Angabe von Rechenergebnissen mit sinnvoller“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 10 · eine fremde Rechnung nachrechnen und den Einheitenfehler benennen → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 11 · Prüfungshöhe: Volumen aus Masse und Dichte; Gebindegröße begründen; Einheitenfehler … → E [Zeile 2200]; Eintrag: Prüfungshöhe
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Maßstab im Koordinatensystem, Sek II (Einheit 1)
    - Sprosse 1 · „Länge, Fläche oder Volumen?“ ankreuzen und den Maßstabssatz unterstreichen (Vorstufe) → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · abgelesene Länge in Längeneinheiten mit dem Faktor in Zentimeter umrechnen (Grundfall) → E [Zeile 2190]; Eintrag: Sek II
      „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · Höhe und Breite aus Koordinatendifferenzen zweier Punkte, dann umrechnen → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Sek II
    - Sprosse 4 · einen Funktionswert als Höhe in der Wirklichkeit deuten, die Stelle aus dem Sachtext → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Sek II
    - Sprosse 5 · den Funktionswert als Radius verdoppeln und umrechnen → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Sek II
    - Sprosse 6 · Prüfungshöhe: Stangenlängen eines Gitters aus Funktionswerten, in Meter … → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Prüfungshöhe, Sek II
  - Flächen- und Volumeneinheiten im Koordinatensystem, Sek II (Einheit 3)
    - Sprosse 1 · „Länge, Fläche oder Volumen?“ ankreuzen (Vorstufe) → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · eine Flächeneinheit mit dem quadrierten Faktor in Quadratzentimeter umrechnen (Grundfall) → keine Stelle; Sek-II-Zeile (fhr); der quadrierte Maßstabsfaktor steht auch im RLP 1–10 nicht.; Eintrag: Sek II
    - Sprosse 3 · Querschnitt und Volumen mit dem Maßstab eins zu eins in Quadrat- und Kubikmeter → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Sek II
    - Sprosse 4 · Prüfungshöhe: Fläche zwischen zwei Graphen mit quadriertem Maßstab umrechnen … → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Prüfungshöhe, Sek II
  - Kosten und Einnahmen, Sek II (Einheit 4)
    - Sprosse 1 · „Gleiche Einheit?“ ankreuzen (Vorstufe) → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · Stückzahlen je Preisstufe addieren und mit dem Preis multiplizieren (Grundfall) → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Sek II
    - Sprosse 3 · Teilbeträge summieren → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Sek II
    - Sprosse 4 · Kosten aus einer Fläche in Quadratmeter und dem Quadratmeterpreis → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Sek II
    - Sprosse 5 · Prüfungshöhe: Verschnitt zweier Leisten als Anteil in Prozent … → keine Stelle; Sek-II-Zeile (fhr); der RLP 1–10 gilt dafür nicht.; Eintrag: Prüfungshöhe, Sek II
- LISUM: keine reihe
  - Die Planungshilfen haben keine Reihe zu Größen und Einheiten; das Umrechnen liegt in Klasse 5/6 und damit unter dem Bereich der Jahrgangsstufen 7 bis 10. Die Einheiten kommen in den Reihen nur als Begleitinhalt vor (z. B. Einheitenvorsätze in der Reihe „Potenzen und Wurzeln“, Zeile 779, dort mit dem Zusatz „nur GYM“ für Mikro, Nano, Mega, Giga und Tera).
- Spanne: ja  – Der Kern liegt auf B, C, D und E; die Einheitenvorsätze mit Zehnerpotenzen stehen auf F, ihre Erweiterung von Nano bis Tera und die Systematisierung auf G. Damit liegt mindestens eine Einheit (Einheit 3) auf G und mehrere auf F oder darunter.
- Ermessen (5):
  - Sprosse „Zeitspanne zwischen zwei Uhrzeiten“ (Einheit 2, Sprossen 7 bis 10): die Stelle steht in einem Block ohne Buchstaben am Rand (Zeilen 2083–2087). Die Stufe B folgt der Zuordnung des Eintrags (S. 45), nicht einer Buchstabenmarke am Absatz.
  - Sprossen „Dezimalstunde in Minuten“ und „Minuten als Dezimalstunde“: keine Stelle, obwohl sie nach dem Eintrag der häufigste P10-Typ der Einheit sind.
  - Sprosse „Liter und Kubikdezimeter gleichsetzen“: keine Stelle; der RLP führt Hohlmaße und Kubikeinheiten nebeneinander, ohne sie gleichzusetzen.
  - Vorstufe von Einheit 3: das Wort „Umrechnungszahl“ kommt im Teil C nicht vor; der Eintrag stellt das in der Verortung selbst fest (auch „Einheitentabelle“ und die Faktoren zehn, hundert, tausend fehlen).
  - Die drei Sek-II-Ketten (Maßstab im Koordinatensystem, Flächen- und Volumeneinheiten im Koordinatensystem, Kosten und Einnahmen) tragen durchweg „keine Stelle“: sie gehören zum Profil fhr, für das der RLP FOS 2019 gilt, nicht der RLP 1–10. Nur der Grundfall des Maßstabs ist über die E-Zeile zum Rechnen mit Maßstäben belegt.

### flaechen – Stufe D–F
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] D: „Unterscheiden zwischen Fläche und Umfang von Figuren““
  - Zeile 6 (Verortung): „E: „Berechnen des Umfangs von beliebigen geradlinig begrenzten Figuren, Kreisen und Kreisteilen““
  - Zeile 6 (Verortung): „F: „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten ebenen Figuren auf der Basis von Zerlegungen und Ergänzungen (auch mithilfe von Formelsammlungen)““
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP D, MSK S1A]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D, MSK S1B]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP E „Umstellen von Formeln“]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 34 (Merkkasten): „[RLP D „Unterscheiden zwischen Fläche und Umfang“; P10 Fehlerquellen]“
  - Zeile 36 (Merkkasten): „[RLP E „auch mithilfe von Formelsammlungen“]“
  - Zeile 38 (Merkkasten): „[RLP E „Umstellen von Formeln“]“
  - Zeile 47 (Merkkasten): „[RLP D]“
  - Zeile 54 (Merkkasten): „[RLP E]“
  - Zeile 76 (Typische Fehler): „[RLP E, F]“
  - Zeile 93 (Für schwache Schüler): „[RLP D, MO]“
- Lerneinheiten:
  - 1. Rechteck, Quadrat, Umfang – D
    - D [Zeile 2179]: „Nutzen und Begründen eines Rechenverfahrens zur Bestimmung des Flächeninhalts von“
      Block 2170–2184, Niveaustufe am Block: D (Z2184); Grundfall Rechteck
    - D [Zeile 2176]: „Berechnen des Umfangs von Vielecken durch Addition der Seitenlängen“
      Block 2170–2184, Niveaustufe am Block: D (Z2184); Umfang
  - 2. Parallelogramm – E
    - E [Zeile 2196]: „Begründen der Flächeninhaltsformeln für Parallelogramme und Dreiecke nach dem Prinzip“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); der RLP nennt Parallelogramm und Dreieck in einer Zeile
  - 3. Dreieck – E
    - E [Zeile 2194]: „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); Grundfall
    - E [Zeile 2196]: „Begründen der Flächeninhaltsformeln für Parallelogramme und Dreiecke nach dem Prinzip“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); Begründung der Formel
  - 4. Trapez, Drachenviereck, Raute – E
    - E [Zeile 2194]: „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); der RLP nennt nur „Vierecke“, nicht Trapez, Drachen oder Raute einzeln
      Ermessen: Trapez, Drachenviereck und Raute kommen im Teil C nicht mit Namen vor; zugeordnet über „Vierecke“ in der E-Zeile.
  - 5. Zusammengesetzte Figuren – D/F
    - D [Zeile 2177]: „Berechnen des Flächeninhalts von aus Rechtecken zusammengesetzten Flächen durch Addition“
      Block 2170–2184, Niveaustufe am Block: D (Z2184); Grundfall: nur Rechtecke
    - F [Zeile 2268]: „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten“
      Block 2263–2276, Niveaustufe am Block: F (Z2271); Erweiterung: Dreiecke, Vierecke und Kreise erst auf F
- Sprossen je Verfahrenstyp:
  - Rechteck (Einheit 1)
    - Sprosse 1 · Fläche oder Umfang ankreuzen (Vorstufe) → D [Zeile 2141]; Eintrag: Vorstufe
      „Unterscheiden zwischen Fläche und Umfang von“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 2 · A und u aus ganzen Zahlen (4×) → D [Zeile 2179]
      „Nutzen und Begründen eines Rechenverfahrens zur Bestimmung des Flächeninhalts von“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 3 · Dezimalzahlen → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 4 · Quadrat → D [Zeile 2179]
      „Nutzen und Begründen eines Rechenverfahrens zur Bestimmung des Flächeninhalts von“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 5 · Umfang Vieleck → D [Zeile 2176]
      „Berechnen des Umfangs von Vielecken durch Addition der Seitenlängen“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 6 · Seite aus A → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · Seite aus u → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 8 · Quadratseite als Wurzel → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 9 · Term zu Figur → E [Zeilen 2740–2741]
      „(auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 10 · Prüfungshöhe: Seite aus Umfang mit Halbieren (P10-Form). → E [Zeile 2747]; Eintrag: Prüfungshöhe
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
  - Parallelogramm (Einheit 2)
    - Sprosse 1 · Höhe einzeichnen (Vorstufe) → E [Zeilen 2470–2472]; Eintrag: Vorstufe
      „Beschreiben besonderer Linien in Dreiecken und Körpern (z. B. Höhe,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · A aus g und h (4×) → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · schräge Seite als Falle → keine Stelle; Fehlerquelle des Unterrichts; der RLP nennt sie nicht.
    - Sprosse 4 · Dezimalzahlen → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 5 · andere Grundseite, gleiche Fläche → E [Zeile 2196]
      „Begründen der Flächeninhaltsformeln für Parallelogramme und Dreiecke nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · h aus A → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP E und LISUM-PH … → E [Zeile 2196]; Eintrag: Prüfungshöhe, Zielmarke
      „Begründen der Flächeninhaltsformeln für Parallelogramme und Dreiecke nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Dreieck (Einheit 3)
    - Sprosse 1 · Höhe zur markierten Grundseite einzeichnen (Vorstufe) → E [Zeilen 2470–2472]; Eintrag: Vorstufe
      „Beschreiben besonderer Linien in Dreiecken und Körpern (z. B. Höhe,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · A aus g und h (4×) → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · rechtwinklig mit Katheten → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 4 · stumpfwinklig → keine Stelle; Die Höhe außerhalb des Dreiecks nennt der RLP nicht eigens.
    - Sprosse 5 · Dezimalzahlen → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 6 · g aus A → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · Term zu Figur → E [Zeilen 2740–2741]
      „(auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 8 · Prüfungshöhe: Grundseite aus Fläche und Höhe mit dem Faktor zwei (P10-Form). → E [Zeile 2747]; Eintrag: Prüfungshöhe
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
  - Trapez (Einheit 4)
    - Sprosse 1 · Formel ankreuzen (Vorstufe) → E [Zeilen 2194–2195]; Eintrag: Vorstufe
      „Kreisen auf der Basis von Zerlegungen und Ergänzungen (auch mithilfe von Formelsammlungen)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 2 · A aus a, c, h (4×) → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · Dezimalzahlen → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 4 · h aus A → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · Drachen aus e und f → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · Umfang mit gegebenen Schenkeln → E [Zeile 2192]
      „Berechnen des Umfangs von beliebigen geradlinig begrenzten Figuren, Kreisen und“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 7 · Prüfungshöhe: Höhe aus Fläche und Nachweis „reicht die Tiefe“ (P10-Form). → E [Zeile 2747]; Eintrag: Prüfungshöhe
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
  - Zusammengesetzte Figuren (Einheit 5)
    - Sprosse 1 · Teilflächen benennen (Vorstufe) → D [Zeile 2177]; Eintrag: Vorstufe
      „Berechnen des Flächeninhalts von aus Rechtecken zusammengesetzten Flächen durch Addition“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 2 · zwei Rechtecke (4×) → D [Zeile 2177]
      „Berechnen des Flächeninhalts von aus Rechtecken zusammengesetzten Flächen durch Addition“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 3 · Rechteck und Dreieck → F [Zeile 2268]
      „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 4 · Ergänzen statt Zerlegen → F [Zeile 2268]
      „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 5 · Restfläche mit Quadrat → F [Zeile 2268]
      „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 6 · Restfläche mit Kreis → F [Zeile 2268]
      „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 7 · Umfang der Figur → E [Zeile 2192]
      „Berechnen des Umfangs von beliebigen geradlinig begrenzten Figuren, Kreisen und“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Prüfungshöhe: Rechteck mit zwei Halbkreisen (P10-Form). → F [Zeile 2268]; Eintrag: Prüfungshöhe
      „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Geometrie“ [Zeile 1120]
  - Beleg [Zeile 1121]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: nein  – Die Stufen reichen von D über E bis F; keine Einheit und keine Sprosse liegt auf G oder H. Das deckt sich mit der Stufenangabe „D–F“ in index.md.
- Ermessen (4):
  - Einheit 4: Trapez, Drachenviereck und Raute kommen im Teil C nicht mit Namen vor; zugeordnet über „Vierecke“ in der E-Zeile.
  - Sprossen „Seite aus A“, „h aus A“, „g aus A“: der RLP nennt kein Umstellen einer Flächenformel; zugeordnet über „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“ (E, Themenbereich Gleichungen und Funktionen) – so auch der Eintrag in den Zeilen 29 und 38.
  - Sprossen „stumpfwinklig“ und „schräge Seite als Falle“: keine Stelle; beides sind Fehlerquellen des Unterrichts.
  - Sprossen „Term zu Figur“: zugeordnet über das Darstellen von Sachverhalten durch Terme (E), nicht über eine Zeile zu Größen und Messen.

### koerper – Stufe D–E (zusammengesetzt F)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Größen und Messen D: „Unterscheiden zwischen Oberflächeninhalt und Volumen von Körpern““
  - Zeile 6 (Verortung): „F: „Berechnen von Volumen und Oberflächeninhalt von Körpern (auch von geraden quadratischen Pyramiden …)“, „Berechnen des Volumens zusammengesetzter Körper unter Verwendung des Zerlegungs- und Ergänzungsprinzips“. G: Kegel, Kugel; H: Cavalieri.“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2021-OS-K4a]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP D/F]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP E „Umstellen von Formeln“]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP C/D; MO]“
  - Zeile 33 (Merkkasten): „[P10 2017-OS-B1c; RLP D]“
  - Zeile 34 (Merkkasten): „[RLP D „Unterscheiden zwischen Oberflächeninhalt und Volumen“; P10 2026-FOR-B1f, 2018-OS-K6b]“
  - Zeile 38 (Merkkasten): „[P10 2017-OS-K3c; RLP F]“
  - Zeile 47 (Merkkasten): „[RLP D]“
  - Zeile 56 (Merkkasten): „[RLP D]“
  - Zeile 64 (Merkkasten): „[RLP E]“
  - Zeile 72 (Merkkasten): „[RLP E]“
  - Zeile 81 (Typische Fehler): „[RLP F]“
  - Zeile 102 (Für schwache Schüler): „[RLP D, MO]“
- Lerneinheiten:
  - 1. Körper erkennen, Netze, Schrägbilder – D/E
    - D [Zeilen 2438–2441]: „Erkennen, Benennen und Beschreiben gerader geometrischer Körper (auch Zylinder, Prismen, Kegel,“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Grundfall, Themenbereich Raum und Form
    - D [Zeilen 2449–2451]: „Skizzieren der Schrägbilder von Würfeln und Quadern auf Rasterpapier“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Schrägbilder von Würfel und Quader
    - E [Zeilen 2466–2467]: „Zeichnen von Netzen und Schrägbildern gerader Prismen“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Netze und Schrägbilder von Prismen erst auf E
  - 2. Quader und Würfel – D
    - D [Zeile 2183]: „Nutzen und Begründen eines Rechenverfahrens zur Bestimmung des Volumens von Quadern“
      Block 2170–2184, Niveaustufe am Block: D (Z2184); Grundfall Volumen
    - D [Zeile 2178]: „(auch Oberflächeninhalt von Quadern)“
      Block 2170–2184, Niveaustufe am Block: D (Z2184); Oberfläche des Quaders
  - 3. Prisma – E
    - E [Zeile 2198]: „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); Grundfall
    - E [Zeilen 2466–2469]: „Beschreiben von Eigenschaften (auch Größenangaben) von geraden Prismen und Zylindern“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Themenbereich Raum und Form
  - 4. Zylinder – E
    - E [Zeile 2198]: „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); der RLP nennt Prisma und Kreiszylinder in einer Zeile
    - E [Zeilen 2470–2471]: „Skizzieren von Netzen und Schrägbildern von Kreiszylindern“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Netz des Zylinders
  - 5. Zusammengesetzte Körper und Anwendungen – D/F
    - D [Zeile 2181]: „Berechnen des Volumens von aus Quadern zusammengesetzten Körpern durch Addition der“
      Block 2170–2184, Niveaustufe am Block: D (Z2184); Grundfall: nur Quader
    - F [Zeile 2273]: „Berechnen des Volumens zusammengesetzter Körper unter Verwendung des Zerlegungs- und“
      Block 2263–2276, Niveaustufe am Block: F (Z2271); beliebige Teilkörper erst auf F
- Sprossen je Verfahrenstyp:
  - Körper und Netze (Einheit 1)
    - Sprosse 1 · Körper ankreuzen (Vorstufe) → D [Zeilen 2438–2441]; Eintrag: Vorstufe
      „Erkennen, Benennen und Beschreiben gerader geometrischer Körper (auch Zylinder, Prismen, Kegel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · Körper aus Schrägbild benennen (4×) → D [Zeilen 2438–2441]
      „Erkennen, Benennen und Beschreiben gerader geometrischer Körper (auch Zylinder, Prismen, Kegel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 3 · Ecken, Kanten, Flächen zählen → keine Stelle; Das Zählen von Ecken, Kanten und Flächen nennt der RLP nicht eigens.
    - Sprosse 4 · Würfelnetz gültig oder ungültig → D [Zeilen 2448–2450]
      „Beschreiben von Lage- und Größenbeziehungen ebener Figuren an räumlichen Objekten“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 5 · Gegenfläche im Würfelnetz → D [Zeilen 2448–2450]
      „Beschreiben von Lage- und Größenbeziehungen ebener Figuren an räumlichen Objekten“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 6 · Quadernetz mit Maßen zeichnen → E [Zeilen 2466–2467]
      „Zeichnen von Netzen und Schrägbildern gerader Prismen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 7 · Schrägbild eines Quaders zeichnen → D [Zeilen 2449–2451]
      „Skizzieren der Schrägbilder von Würfeln und Quadern auf Rasterpapier“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 8 · Schrägbild beschriften (Höhe einzeichnen) → keine Stelle; Das Beschriften eines Schrägbilds nennt der RLP nicht.
    - Sprosse 9 · Prüfungshöhe: Gegenfläche im Würfelnetz markieren; Kantenzahl einer Pyramide … → D [Zeilen 2448–2450]; Eintrag: Prüfungshöhe
      „Beschreiben von Lage- und Größenbeziehungen ebener Figuren an räumlichen Objekten“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
  - Quader (Einheit 2)
    - Sprosse 1 · Volumen oder Oberfläche ankreuzen (Vorstufe) → D [Zeilen 2143–2144]; Eintrag: Vorstufe
      „Unterscheiden zwischen Oberflächeninhalt und Volumen von Körpern“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 2 · V aus a, b, c mit ganzen Zahlen (4×) → D [Zeile 2183]
      „Nutzen und Begründen eines Rechenverfahrens zur Bestimmung des Volumens von Quadern“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 3 · Würfel a³ → D [Zeile 2183]
      „Nutzen und Begründen eines Rechenverfahrens zur Bestimmung des Volumens von Quadern“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 4 · Einheiten cm³ ↔ l → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 5 · O als sechs Rechtecke → D [Zeile 2178]
      „(auch Oberflächeninhalt von Quadern)“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 6 · Würfel als sechs gleiche Quadrate → D [Zeile 2178]
      „(auch Oberflächeninhalt von Quadern)“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 7 · Kante aus V → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 8 · zusammengesetzt aus zwei Quadern → D [Zeile 2181]
      „Berechnen des Volumens von aus Quadern zusammengesetzten Körpern durch Addition der“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 9 · Prüfungshöhe: Würfelvolumen aus der Kante mit der Oberfläche als Falle; Aquarium in Litern … → D [Zeile 2183]; Eintrag: Prüfungshöhe
      „Nutzen und Begründen eines Rechenverfahrens zur Bestimmung des Volumens von Quadern“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
  - Prisma (Einheit 3)
    - Sprosse 1 · Grundfläche und Höhe markieren (Vorstufe) → E [Zeilen 2466–2469]; Eintrag: Vorstufe
      „Beschreiben von Eigenschaften (auch Größenangaben) von geraden Prismen und Zylindern“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · V = G · h mit gegebener Grundfläche (4×) → E [Zeile 2198]
      „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · Rechteckgrundfläche → E [Zeile 2198]
      „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 4 · Dreiecksgrundfläche → E [Zeile 2198]
      „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · Trapezgrundfläche → E [Zeile 2198]
      „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · liegendes Prisma → keine Stelle; Die Lage des Prismas nennt der RLP nicht; sie ist Aufgabenform.
    - Sprosse 7 · Mantel als Rechtecke → E [Zeile 2199]
      „und des Oberflächeninhalts nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Oberfläche → E [Zeile 2199]
      „und des Oberflächeninhalts nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 9 · Netz vervollständigen → E [Zeilen 2466–2467]
      „Zeichnen von Netzen und Schrägbildern gerader Prismen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 10 · h aus V → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 11 · Prüfungshöhe: Dreiecksprisma, Deckfläche und Volumennachweis … → E [Zeile 2198]; Eintrag: Prüfungshöhe
      „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Zylinder (Einheit 4)
    - Sprosse 1 · Radius oder Durchmesser benennen (Vorstufe) → keine Stelle; Die Begriffe Radius und Durchmesser nennt der Teil C nicht.; Eintrag: Vorstufe
    - Sprosse 2 · V aus r und h mit ganzen Zahlen (4×) → E [Zeile 2198]
      „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · aus d → E [Zeile 2198]
      „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 4 · Dezimalzahlen mit Runden → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · in Liter → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 6 · Mantel → E [Zeile 2199]
      „und des Oberflächeninhalts nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 7 · Oberfläche mit und ohne Deckel → E [Zeile 2199]
      „und des Oberflächeninhalts nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Netz auswählen (Rechtecklänge = Umfang) → E [Zeilen 2470–2471]
      „Skizzieren von Netzen und Schrägbildern von Kreiszylindern“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 9 · h aus V → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 10 · r aus V → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 11 · Behauptung prüfen → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 12 · doppelter Radius begründen → keine Stelle; Die Wirkung einer Maßänderung auf das Volumen nennt der Teil C nicht.
    - Sprosse 13 · Prüfungshöhe: Höhe einer 1-Liter-Dose aus r = 4 cm (P10-Form, Stern). → E [Zeile 2198]; Eintrag: Prüfungshöhe
      „Berechnen des Volumens von geraden Prismen und Kreiszylindern nach dem Prinzip“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Zusammengesetzt (Einheit 5)
    - Sprosse 1 · Teilkörper benennen (Vorstufe) → F [Zeilen 2544–2546]; Eintrag: Vorstufe
      „Teilkörper und -flächen in zusammengesetzten Körpern“ – Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565)
    - Sprosse 2 · zwei Quader (4×) → D [Zeile 2181]
      „Berechnen des Volumens von aus Quadern zusammengesetzten Körpern durch Addition der“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 3 · Quader und Dreiecksprisma → F [Zeile 2273]
      „Berechnen des Volumens zusammengesetzter Körper unter Verwendung des Zerlegungs- und“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 4 · Quader und Halbzylinder → F [Zeile 2273]
      „Berechnen des Volumens zusammengesetzter Körper unter Verwendung des Zerlegungs- und“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 5 · Term zum Volumen prüfen → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · Restvolumen → F [Zeile 2273]
      „Berechnen des Volumens zusammengesetzter Körper unter Verwendung des Zerlegungs- und“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 7 · Verpackungsmaße (Durchmesser) → E [Zeilen 2145–2146]
      „Entnehmen von Maßen an Körpern aus verschiedenen Darstellungen, z. B. Skizzen“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 8 · Packungsanzahl durch Anordnen → keine Stelle; Das Anordnen von Packungen in einem Karton nennt der RLP nicht.
    - Sprosse 9 · Masse aus Volumen → E [Zeile 2189]
      „Verwenden von Größenangaben in Rechnungen (auch Geschwindigkeiten, Dichten)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 10 · Prüfungshöhe: Restvolumen Zylinderverpackung minus Kegel (P10-Form, Stern). → F [Zeile 2273]; Eintrag: Prüfungshöhe
      „Berechnen des Volumens zusammengesetzter Körper unter Verwendung des Zerlegungs- und“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Geometrie“ [Zeile 1120]; „Jahrgangsstufe 9/10, Mathematik: Körper“ [Zeile 2101]
  - Beleg [Zeile 2102]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und die Menge“
  - Beide Reihen führen EBR, FOR und GYM gemeinsam und tragen den Differenzierungshinweis (Zeilen 1121 und 2102).
- Spanne: nein  – Die Einheiten liegen auf D, E und F; keine Einheit und keine Sprosse liegt auf G oder H. Die G- und H-Stoffe der Verortung (Kegel, Kugel, Cavalieri) gehören zu pyramide-kegel-kugel.md.
- Ermessen (5):
  - Sprossen „Ecken, Kanten, Flächen zählen“ und „Schrägbild beschriften“: keine Stelle; der RLP beschreibt das Erkennen und Zeichnen, nicht das Zählen oder Beschriften.
  - Sprosse „liegendes Prisma“ und „doppelter Radius begründen“: keine Stelle; beides sind Aufgabenformen, keine Planinhalte.
  - Sprosse „Packungsanzahl durch Anordnen“: keine Stelle; das Anordnen von Packungen steht nicht im Plan.
  - Sprossen „h aus V“, „r aus V“, „Kante aus V“: über das Umstellen von Formeln (E) bzw. die Kubikwurzel (F) belegt – nicht über eine Zeile zu Körpern.
  - Sprosse „Quadernetz mit Maßen zeichnen“ ist über die E-Zeile zu Netzen gerader Prismen belegt; der RLP nennt für D nur das Skizzieren der Schrägbilder, nicht das maßgetreue Netz.

### kreis – Stufe E
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] D: „Zeichnen von Winkeln und ebenen Figuren mithilfe von Zeichengeräten (Lineal, Geodreieck, Zirkel …)““
  - Zeile 6 (Verortung): „E: „Berechnen des Umfangs von beliebigen geradlinig begrenzten Figuren, Kreisen und Kreisteilen (auch unter Verwendung von Pi)““
  - Zeile 6 (Verortung): „F: „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten ebenen Figuren“.“
  - Zeile 6 (Verortung): „G: „Nennen von Pi und einiger Quadratwurzeln natürlicher Zahlen als Beispiele für irrationale Zahlen“.“
  - Zeile 6 (Verortung): „H: „Beschreiben des Zusammenhangs zwischen Bogen- und Gradmaß am Einheitskreis““
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[RLP D/E „sinnvolle Genauigkeit“]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP F; P10 2022-OS-K2d]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP E „Umstellen von Formeln“]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 30 (Merkkasten): „[RLP D „Unterscheiden zwischen Fläche und Umfang“; P10 2024-OS-K4a]“
  - Zeile 31 (Merkkasten): „[RLP E „auch mithilfe von Formelsammlungen“]“
  - Zeile 40 (Merkkasten): „[RLP E]“
  - Zeile 48 (Merkkasten): „[RLP E]“
  - Zeile 66 (Typische Fehler): „[RLP E „sinnvolle Genauigkeit“; FD]“
  - Zeile 72 (Für schwache Schüler): „[RLP D, MO]“
- Lerneinheiten:
  - 1. Kreisumfang – D/E
    - E [Zeile 2192]: „Berechnen des Umfangs von beliebigen geradlinig begrenzten Figuren, Kreisen und“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); Grundfall; die Zeile nennt Kreise und Kreisteile ausdrücklich
    - D [Zeilen 2444–2446]: „Zeichnen von Winkeln und ebenen Figuren mithilfe von Zeichengeräten (Lineal,“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); der Zirkel und damit das Zeichnen des Kreises stehen auf D
  - 2. Kreisfläche – E
    - E [Zeile 2194]: „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); Grundfall
  - 3. Kreisteile – E
    - E [Zeilen 2192–2193]: „Kreisen und Kreisteilen (auch unter Verwendung von Pi)“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); Kreisteile stehen ausdrücklich auf E
    - E [Zeilen 2795–2797]: „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“
      Block 2795–2806, Niveaustufe am Block: E (Z2803); der Anteil aus dem Mittelpunktswinkel als proportionale Zuordnung
      Ermessen: Die Wörter „Kreisausschnitt“, „Mittelpunktswinkel“, „Bogenlänge“ und „Kreisring“ kommen im Teil C nicht vor; der RLP sagt nur „Kreisteile“.
- Sprossen je Verfahrenstyp:
  - Umfang (Einheit 1)
    - Sprosse 1 · Radius oder Durchmesser benennen (Vorstufe) → keine Stelle; Die Begriffe Radius und Durchmesser nennt der Teil C nicht.; Eintrag: Vorstufe
    - Sprosse 2 · u aus d mit ganzen Zahlen (4×) → E [Zeile 2192]
      „Berechnen des Umfangs von beliebigen geradlinig begrenzten Figuren, Kreisen und“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · u aus r → E [Zeile 2192]
      „Berechnen des Umfangs von beliebigen geradlinig begrenzten Figuren, Kreisen und“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 4 · Dezimalzahlen mit Runden → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · d aus u → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 6 · r aus u → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · Halbkreisbogen → E [Zeilen 2192–2193]
      „Kreisen und Kreisteilen (auch unter Verwendung von Pi)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Sachaufgabe (Rad, Umdrehungen) → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 9 · Prüfungshöhe: kein eigenes P10-Original; Marke nach dem Mantelrechteck eines Zylinders … → E [Zeile 2192]; Eintrag: Prüfungshöhe, Zielmarke
      „Berechnen des Umfangs von beliebigen geradlinig begrenzten Figuren, Kreisen und“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Fläche (Einheit 2)
    - Sprosse 1 · Formel ankreuzen (Vorstufe) → E [Zeilen 2194–2195]; Eintrag: Vorstufe
      „Kreisen auf der Basis von Zerlegungen und Ergänzungen (auch mithilfe von Formelsammlungen)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 2 · A aus r mit ganzen Zahlen (4×) → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · A aus d → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 4 · Dezimalzahlen mit Runden → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · Halbkreis, Viertelkreis → E [Zeilen 2192–2193]
      „Kreisen und Kreisteilen (auch unter Verwendung von Pi)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · Tabelle r, d, u, A → keine Stelle; Die Tabellenform ist Übungsform; der RLP nennt sie nicht.
    - Sprosse 7 · r aus A → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 8 · Prüfungshöhe: Kreisfläche aus dem Durchmesser, erst halbieren, dann quadrieren … → E [Zeile 2194]; Eintrag: Prüfungshöhe
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Kreisteile (Einheit 3)
    - Sprosse 1 · Anteil zum Ausschnitt ankreuzen (Vorstufe) → keine Stelle; Der Kreisausschnitt kommt als Begriff im Teil C nicht vor.; Eintrag: Vorstufe
    - Sprosse 2 · Anteil aus rechtem Winkel, gestrecktem Winkel und Sechstelkreis als Bruch (4×) → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 3 · beliebiger Winkel als Prozent mit Runden → E [Zeilen 2801–2802]
      „auch Maßstab und Prozentrechnung“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 4 · Winkel aus Anteil → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 5 · Bogenlänge → E [Zeilen 2192–2193]
      „Kreisen und Kreisteilen (auch unter Verwendung von Pi)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · Ausschnittsfläche → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 7 · Umfang des Ausschnitts → E [Zeilen 2192–2193]
      „Kreisen und Kreisteilen (auch unter Verwendung von Pi)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Kreisring → F [Zeile 2268]
      „Berechnen des Flächeninhaltes von aus Dreiecken, Vierecken und Kreisen zusammengesetzten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 9 · Prüfungshöhe: Anteil eines gegebenen Ausschnitts in Prozent, mit dem Restwinkel als Falle … → E [Zeilen 2801–2802]; Eintrag: Prüfungshöhe
      „auch Maßstab und Prozentrechnung“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Geometrie“ [Zeile 1120]
  - Beleg [Zeile 1121]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: nein  – Alle Einheiten liegen auf E, einzelne Sprossen auf D und der Kreisring auf F. Keine Einheit und keine Sprosse liegt auf G oder H; die Verortung nennt G (Pi als irrationale Zahl) und H (Bogenmaß) nur als Ausblick.
- Ermessen (4):
  - Einheit 3 im Ganzen: „Kreisausschnitt“, „Mittelpunktswinkel“, „Bogenlänge“ und „Kreisring“ kommen im Teil C nicht vor; der RLP sagt nur „Kreisteile“. Der Anteil aus dem Winkel ist über die proportionalen Zuordnungen (E) belegt.
  - Sprosse „Radius oder Durchmesser benennen“ (Einheit 1) und „Anteil zum Ausschnitt ankreuzen“ (Einheit 3): keine Stelle; die Begriffe selbst stehen nicht im Plan.
  - Sprossen „d aus u“, „r aus u“, „r aus A“: zugeordnet über „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“ (E, Gleichungen und Funktionen), nicht über eine Zeile zu Größen und Messen.
  - Sprosse „Tabelle r, d, u, A“: keine Stelle; die Tabellenform ist Übungsform.

### lineare-funktionen – Stufe F
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 5 (Verortung): „[RLP] Niveaustufe F: „Bestimmen und Beschreiben von Merkmalen linearer Funktionen (Steigung, Änderungsrate, Nullstelle, y-Achsenabschnitt, Einfluss der Parameter)", „Übersetzen zwischen sprachlicher, tabellarischer und grafischer Form sowie Funktionsgleichung", „Ermitteln und Nutzen von ausgewählten Punkten".“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP E, MSK S4]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[MSK S5, RLP D/E]“
  - Zeile 69 (Typische Fehler): „[RLP F Parametereinfluss]“
  - Zeile 74 (Für schwache Schüler): „Mindeststoff (D/E) [RLP]: Einheit 1 ganz (proportional ist D/E); Einheit 2 Graph zeichnen und m, n ablesen bei ganzzahligem m; Einheit 3 Funktionswert und Wertetabelle; Einheit 5 Tarif mit Anfangswert und Preis je Einheit.“
- Lerneinheiten:
  - 1. Proportionale Funktion – D/F
    - D [Zeilen 2783–2784]: „Darstellen von Zuordnungen, insbesondere direkt“
      Block 2780–2791, Niveaustufe am Block: D (Z2788); die proportionale Zuordnung steht schon auf D
    - F [Zeilen 2816–2818]: „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“
      Block 2811–2825, Niveaustufe am Block: F (Z2818); als lineare Funktion mit n = 0 erst auf F
  - 2. Lineare Funktion f(x) = m·x + n – F
    - F [Zeilen 2816–2818]: „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“
      Block 2811–2825, Niveaustufe am Block: F (Z2818); Grundfall; der RLP schreibt y = ax + b
    - F [Zeilen 2811–2813]: „Darstellen von Zuordnungen und linearen Funktionen im Koordinatensystem“
      Block 2811–2825, Niveaustufe am Block: F (Z2818); Graph zeichnen
  - 3. Punkte und Werte – F
    - F [Zeilen 2811–2813]: „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“
      Block 2811–2825, Niveaustufe am Block: F (Z2818); Grundfall
  - 4. Gleichung bestimmen – G
    - G [Zeilen 2912–2915]: „Ermitteln der Funktionsgleichung einer linearen Funktion aus zwei gegebenen Punkten“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); die Gleichung aus zwei Punkten steht erst auf G
    - G [Zeilen 2914–2916]: „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); der Schnittpunkt zweier Geraden ebenfalls erst auf G
      Ermessen: Der Eintrag und index.md führen das Thema als F; die beiden Verfahren dieser Einheit finden ihre Stelle im Teil C aber erst auf G.
  - 5. Anwendungen – F
    - F [Zeilen 2811–2814]: „Beschreiben, Analysieren, Interpretieren und Vergleichen von linearen Zusammenhängen und“
      Block 2811–2825, Niveaustufe am Block: F (Z2818); Tarife als lineare Zusammenhänge in Alltagssituationen
- Sprossen je Verfahrenstyp:
  - Proportionale Funktion (Einheit 1)
    - Sprosse 1 · aus einer Wertetabelle den festen Faktor bestimmen (Vorstufe, Blatt 0) → D [Zeilen 2787–2788]; Eintrag: Vorstufe, Blatt 0
      „(inhaltlich und durch Rechnen mit Dreisatz)“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 2 · Wertepaare zu y = m · x berechnen und die Ursprungsgerade zeichnen (4×) → F [Zeilen 2811–2813]
      „Darstellen von Zuordnungen und linearen Funktionen im Koordinatensystem“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 3 · Wert am Graphen ablesen und mit der Rechnung vergleichen → F [Zeilen 2814–2816]
      „Übersetzen zwischen sprachlicher, tabellarischer und grafischer Form sowie“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 4 · Faktor als Dezimalzahl → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 5 · Faktor als Bruch → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 6 · Faktor negativ, Gerade fällt → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 7 · aus einer Tabelle über die Quotientengleichheit entscheiden und die Gleichung angeben → D [Zeilen 2783–2785]
      „Beschreiben der Eigenschaften direkt proportionaler Zusammenhänge und“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 8 · Fehler finden: für den Faktor die Differenz statt des Quotienten genommen → keine Stelle; Fehlerquelle des Unterrichts; der RLP nennt sie nicht.
    - Sprosse 9 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP F und LISUM-PH … → F [Zeilen 2816–2818]; Eintrag: Prüfungshöhe, Zielmarke
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
  - Graph zeichnen (Einheit 2)
    - Sprosse 1 · Wertetabelle aus Gleichung (3×) → F [Zeilen 2814–2816]
      „Übersetzen zwischen sprachlicher, tabellarischer und grafischer Form sowie“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 2 · Punkte eintragen → F [Zeilen 2811–2813]
      „Darstellen von Zuordnungen und linearen Funktionen im Koordinatensystem“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 3 · Gerade durch Punkte → F [Zeilen 2811–2813]
      „Darstellen von Zuordnungen und linearen Funktionen im Koordinatensystem“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 4 · n markieren und Steigungsdreieck einen Schritt nach rechts, m nach oben (4×) → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 5 · m negativ → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 6 · m als Bruch (zwei nach rechts, einen nach oben) → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 7 · n negativ → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 8 · Prüfungshöhe: m Bruch und n negativ (P10 „Gerade aus Gleichung zeichnen“). → F [Zeilen 2816–2818]; Eintrag: Prüfungshöhe
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
  - Ablesen (Einheit 2)
    - Sprosse 1 · n ablesen (3×) → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 2 · m ablesen ganzzahlig → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 3 · m negativ → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 4 · m Bruch → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 5 · Gleichung zu Graph zuordnen (Ankreuzen, P10) → F [Zeilen 2814–2816]
      „Übersetzen zwischen sprachlicher, tabellarischer und grafischer Form sowie“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 6 · Prüfungshöhe: unter vier Geraden die richtige. → F [Zeilen 2814–2816]; Eintrag: Prüfungshöhe
      „Übersetzen zwischen sprachlicher, tabellarischer und grafischer Form sowie“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
  - Funktionswert (Einheit 3)
    - Sprosse 1 · x positiv ganz (4×) → F [Zeilen 2811–2813]
      „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 2 · x negativ → F [Zeilen 2811–2813]
      „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 3 · x Dezimal → F [Zeilen 2811–2813]
      „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 4 · Argument zum Wert (Gleichung lösen) → E [Zeile 2745]
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · Punktprobe ja/nein gemischt → F [Zeilen 2811–2813]
      „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 6 · Nullstelle (Funktionswert null) → F [Zeilen 2816–2818]
      „Bestimmen und Beschreiben von Merkmalen linearer Funktionen der Form“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 7 · Prüfungshöhe: Punktprobe mit Bruch-m. → F [Zeilen 2811–2813]; Eintrag: Prüfungshöhe
      „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
  - Gleichung bestimmen (Einheit 4)
    - Sprosse 1 · aus Graph mit n und ganzzahligem m (3×) → F [Zeilen 2814–2816]
      „Übersetzen zwischen sprachlicher, tabellarischer und grafischer Form sowie“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 2 · aus m und einem Punkt → G [Zeilen 2912–2915]
      „Ermitteln der Funktionsgleichung einer linearen Funktion aus zwei gegebenen Punkten“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · aus zwei Punkten, einer auf der y-Achse → G [Zeilen 2912–2915]
      „Ermitteln der Funktionsgleichung einer linearen Funktion aus zwei gegebenen Punkten“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · zwei beliebige Punkte → G [Zeilen 2912–2915]
      „Ermitteln der Funktionsgleichung einer linearen Funktion aus zwei gegebenen Punkten“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · negative Steigung → G [Zeilen 2912–2915]
      „Ermitteln der Funktionsgleichung einer linearen Funktion aus zwei gegebenen Punkten“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · Prüfungshöhe: zwei Punkte mit Bruch-m (P10 „Geradengleichung aus zwei Punkten“). → G [Zeilen 2912–2915]; Eintrag: Prüfungshöhe
      „Ermitteln der Funktionsgleichung einer linearen Funktion aus zwei gegebenen Punkten“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Anwendung (Einheit 5)
    - Sprosse 1 · Anfangswert und Änderung im Text markieren (Vorstufe) → F [Zeilen 2811–2814]; Eintrag: Vorstufe
      „Beschreiben, Analysieren, Interpretieren und Vergleichen von linearen Zusammenhängen und“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 2 · Gleichung ankreuzen (3×, P10 „Gleichung zu Tarif zuordnen“) → F [Zeilen 2814–2816]
      „Übersetzen zwischen sprachlicher, tabellarischer und grafischer Form sowie“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 3 · Gleichung aufstellen → F [Zeilen 2814–2816]
      „Übersetzen zwischen sprachlicher, tabellarischer und grafischer Form sowie“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 4 · Endwert berechnen → F [Zeilen 2811–2813]
      „Ermitteln und Nutzen von ausgewählten Punkten linearer Funktionen“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 5 · zwei Tarife für eine Nutzung vergleichen → F [Zeilen 2811–2814]
      „Beschreiben, Analysieren, Interpretieren und Vergleichen von linearen Zusammenhängen und“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 6 · Prüfungshöhe: ab wann günstiger (Schnittpunkt im Kontext). → G [Zeilen 2914–2916]; Eintrag: Prüfungshöhe
      „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 8, Mathematik: Lineare Funktionen“ [Zeile 1024]
  - Beleg [Zeile 1025]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: ja  – Die Einheiten 1 bis 3 und 5 liegen auf D bis F, Einheit 4 (Gleichung aus zwei Punkten, Schnittpunkt zweier Geraden) dagegen auf G. Damit steht eine Einheit auf G und mehrere auf F und darunter – obwohl index.md das Thema als reines F führt.
- Ermessen (4):
  - **Einheit 4 auf G:** Der Eintrag und index.md führen das Thema als F. Im Teil C stehen „Ermitteln der Funktionsgleichung einer linearen Funktion aus zwei gegebenen Punkten“ und „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von Schnittpunkten von Funktionsgraphen“ aber im G-Block der Leitidee Gleichungen und Funktionen (Zeilen 2912–2918). Diese eine Einheit entscheidet die Spanne.
  - Der RLP schreibt die lineare Funktion als y = ax + b, der Katalog als f(x) = m·x + n – gleiche Sache, andere Buchstaben.
  - Sprosse „Argument zum Wert“ ist über das Lösen linearer Gleichungen (E) belegt, nicht über eine Zeile zu Funktionen.
  - Sprosse „Fehler finden: Differenz statt Quotient“: keine Stelle; Fehlerquelle des Unterrichts.

### lineare-gleichungen – Stufe E–F
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 5 (Verortung): „[RLP] „Lösen linearer Gleichungen durch systematisches Probieren, grafisch und durch Äquivalenzumformungen", „Prüfen einer Lösung durch Einsetzen", „Untersuchen von Fragen der Lösbarkeit und Lösungsvielfalt" (E); „Lösen von linearen Gleichungen (auch mit Klammern)" (F).“
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[MSK N, RLP D]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP E]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP F]“
  - Zeile 63 (Typische Fehler): „[RLP E „Prüfen einer Lösung"]“
  - Zeile 70 (Für schwache Schüler): „Mindeststoff (D/E) [RLP]: Einheit 1 ganz; Einheit 2 ganz (Äquivalenzumformungen sind E, Probe ist E); Einheit 3 nur x beidseitig und Zusammenfassen; Klammern, Brüche, Sonderfälle sind F“
- Lerneinheiten:
  - 1. Gleichungen verstehen – E
    - E [Zeile 2750]: „Prüfen einer Lösung (auch durch Einsetzen in“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); die Probe steht auf E
    - E [Zeilen 2743–2744]: „Lösen linearer Gleichungen durch systematisches Probieren, grafisch und“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); das Probieren steht in derselben Zeile wie die Äquivalenzumformung
  - 2. Äquivalenzumformungen – E
    - E [Zeile 2745]: „durch Äquivalenzumformungen (auch mithilfe von“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); Grundfall
    - E [Zeile 2742]: „Begründen von Gleichungsumformungen“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); das Begründen der Umformung, ebenfalls E
  - 3. Gleichungen mit x auf beiden Seiten, Klammern, Brüchen und Dezimalzahlen – E/F
    - F [Zeile 2759]: „Lösen von linearen Gleichungen (auch mit“
      Block 2756–2769, Niveaustufe am Block: F (Z2763); die Klammer steht auf F; so auch der Eintrag
    - E [Zeile 2752]: „Untersuchen von Fragen der Lösbarkeit und der“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); die Sonderfälle keine/alle Lösungen stehen auf E
  - 4. Gleichungen aufstellen – E
    - E [Zeilen 2739–2741]: „Darstellen von außer- und innermathematischen Sachverhalten (auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); Gleichung aus Sachtext
    - E [Zeile 2747]: „Lösen von Verhältnisgleichungen“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); das Umstellen von Formeln steht in derselben Zeile
- Sprossen je Verfahrenstyp:
  - Lösung prüfen (Einheit 1)
    - Sprosse 1 · Zahl einsetzen, eine Rechenoperation (4×) → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 2 · zweischrittig → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · wA/fA entscheiden gemischt → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · x beidseitig → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · Prüfungshöhe: mit negativer Zahl. → E [Zeile 2750]; Eintrag: Prüfungshöhe
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
  - Durch Probieren lösen (Einheit 1)
    - Sprosse 1 · Tabelle mit vorgegebenen Kandidaten (3×) → E [Zeilen 2743–2744]
      „Lösen linearer Gleichungen durch systematisches Probieren, grafisch und“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 2 · eigene Kandidaten wählen und eingrenzen → E [Zeilen 2743–2744]
      „Lösen linearer Gleichungen durch systematisches Probieren, grafisch und“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · Umkehroperation ohne Strich („welche Zahl plus fünf ergibt neun?“) → D [Zeilen 2734–2735]
      „Lösen und Begründen der Lösungen von Gleichungen (auch mit gebrochenen Zahlen) mit“ – Block 2724–2737, Niveaustufe am Block: D (Z2732)
    - Sprosse 4 · die Lösung als die Zahl benennen, die die Aussage wahr macht → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP E und LISUM-PH … → E [Zeilen 2743–2744]; Eintrag: Prüfungshöhe, Zielmarke
      „Lösen linearer Gleichungen durch systematisches Probieren, grafisch und“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
  - Umformen (Einheit 2)
    - Sprosse 1 · Umformung nur anschreiben (Vorstufe, Blatt 0) → E [Zeile 2742]; Eintrag: Vorstufe, Blatt 0
      „Begründen von Gleichungsumformungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 2 · einschrittig plus/minus (4×) → E [Zeile 2745]
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · einschrittig mal/geteilt → E [Zeile 2745]
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · negative Lösung → E [Zeile 2745]
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · zweischrittig erst Strich dann Punkt (4×, mit Probe) → E [Zeile 2745]
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 6 · negative Vorzahl → E [Zeile 2745]
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · Vorzahl als Bruch → F [Zeile 2759]; Eintrag: F-Stoff (Eintrag)
      „Lösen von linearen Gleichungen (auch mit“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 8 · Umkehrung: Gleichung zu gegebener Lösung → keine Stelle; Das Erfinden einer Gleichung zu einer Lösung nennt der RLP nicht.
    - Sprosse 9 · Prüfungshöhe: zweischrittig mit negativer Lösung und Probe. → E [Zeile 2745]; Eintrag: Prüfungshöhe
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
  - x beidseitig (Einheit 3)
    - Sprosse 1 · erst Seite mit weniger x finden (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · x nur rechts wegnehmen (4×) → E [Zeile 2745]
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · x beidseitig mit Zahlen beidseitig → E [Zeile 2745]
      „durch Äquivalenzumformungen (auch mithilfe von“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · vorher zusammenfassen → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · Klammer → F [Zeile 2759]; Eintrag: F-Stoff (Eintrag)
      „Lösen von linearen Gleichungen (auch mit“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 6 · Bruch → F [Zeile 2759]; Eintrag: F-Stoff (Eintrag)
      „Lösen von linearen Gleichungen (auch mit“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 7 · Sonderfälle → E [Zeile 2752]; Eintrag: F-Stoff (Eintrag)
      „Untersuchen von Fragen der Lösbarkeit und der“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 8 · Prüfungshöhe: Klammer und x beidseitig. → F [Zeile 2759]; Eintrag: Prüfungshöhe
      „Lösen von linearen Gleichungen (auch mit“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
  - Aufstellen (Einheit 4)
    - Sprosse 1 · passende Gleichung ankreuzen (3×) → E [Zeilen 2746–2747]
      „Angeben von passenden Situationen und grafischen Darstellungen zu vorgegeben“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 2 · Zahlenrätsel einschrittig → E [Zeilen 2739–2741]
      „Darstellen von außer- und innermathematischen Sachverhalten (auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · zweischrittig → E [Zeilen 2739–2741]
      „Darstellen von außer- und innermathematischen Sachverhalten (auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · Alter/Geld → E [Zeilen 2739–2741]
      „Darstellen von außer- und innermathematischen Sachverhalten (auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · Geometrie mit Formel (geg./ges./F./R.) → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 6 · Prüfungshöhe: Sachverhalt mit Klammer (P10-Form). → F [Zeile 2759]; Eintrag: Prüfungshöhe
      „Lösen von linearen Gleichungen (auch mit“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7, Mathematik: Terme und Gleichungen“ [Zeile 344]; „Jahrgangsstufe 8, Mathematik: Terme und Gleichungen“ [Zeile 850]
  - Beleg [Zeile 345]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: nein  – Die Einheiten liegen auf D, E und F; keine Einheit und keine Sprosse liegt auf G oder H. Das deckt sich mit der Stufenangabe „E–F“ in index.md.
- Ermessen (4):
  - Sprosse „Sonderfälle“ (Einheit 3): der Eintrag führt sie als F-Stoff, der RLP nennt „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von linearen Gleichungen“ aber schon auf E. Die Marke des Eintrags und die Stufe des Plans sagen Verschiedenes.
  - Sprossen „Vorzahl als Bruch“, „Klammer“, „Bruch“: der RLP nennt auf F nur „auch mit Klammern“; Brüche in der Gleichung stehen dort nicht ausdrücklich. Die Zuordnung zu F folgt der Marke des Eintrags.
  - Sprosse „Umkehrung: Gleichung zu gegebener Lösung“: keine Stelle; der RLP kennt nur den Weg von der Gleichung zur Lösung.
  - Sprosse „Umkehroperation ohne Strich“ ist über die D-Zeile belegt („Lösen und Begründen der Lösungen von Gleichungen … mit einer Rechenoperation und einem Platzhalter“), die übrige Kette über E.

### lineare-gleichungssysteme – Stufe F (grafisch) – G (rechnerisch; Addition H); Sek I + II (drei Variablen H, GOST Q1/Q3)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Gleichungen und Funktionen E (S. 58): „Prüfen einer Lösung (auch durch Einsetzen in die Ausgangsgleichung)“.“
  - Zeile 6 (Verortung): „Der RLP nennt das Einsetzungs- und Gleichsetzungsverfahren nicht beim Namen („auch rechnerisch“, G); das Additionsverfahren steht erst auf H.“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP E/F; LS-AA Kl. 7 IV 5]“
  - Zeile 32 (Voraussetzungen (Blatt 0)): „[RLP E „Prüfen einer Lösung“]“
  - Zeile 33 (Voraussetzungen (Blatt 0)): „[RLP E „Umstellen von Formeln“]“
  - Zeile 34 (Voraussetzungen (Blatt 0)): „[RLP F]“
  - Zeile 35 (Voraussetzungen (Blatt 0)): „[RLP E/F Distributivgesetz; LS-AA Kl. 8 II]“
  - Zeile 36 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 42 (Merkkasten): „[RLP E „Prüfen einer Lösung“; LS-AA Kl. 8 III 1]“
  - Zeile 43 (Merkkasten): „[RLP F „Lösbarkeit und Lösungsvielfalt“]“
  - Zeile 60 (Merkkasten): „[RLP F]“
  - Zeile 77 (Merkkasten): „[RLP H]“
  - Zeile 87 (Typische Fehler): „[RLP F]“
  - Zeile 111 (Für schwache Schüler): „[FD, aus dem Gedächtnis; RLP F Lösbarkeit]“
  - Zeile 118 (Für schwache Schüler): „[RLP F, MO]“
- Lerneinheiten:
  - 1. Gleichungen mit zwei Variablen und grafisches Lösen – F
    - F [Zeile 2761]: „Lösen linearer Gleichungssysteme mit zwei“
      Block 2756–2769, Niveaustufe am Block: F (Z2763); Grundfall: grafisch und durch systematisches Probieren
    - F [Zeile 2765]: „Untersuchen der Lösbarkeit und der“
      Block 2756–2769, Niveaustufe am Block: F (Z2763); Sonderfälle parallel und identisch
  - 2. Einsetzungsverfahren – G
    - G [Zeilen 2847–2848]: „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); der RLP sagt nur „auch rechnerisch“ und nennt das Einsetzungsverfahren nicht beim Namen
  - 3. Additionsverfahren – H
    - H [Zeile 2878]: „− auch Nutzen des Additionsverfahrens“
      Block 2860–2880, Niveaustufe am Block: H (Z2875); das Additionsverfahren wird nur hier genannt, auf H
  - 4. Sachaufgaben – F
    - F [Zeile 2757]: „Sachverhalten durch Terme, Gleichungen und“
      Block 2756–2769, Niveaustufe am Block: F (Z2763); Gleichungssystem aus einem Sachverhalt
    - F [Zeile 2759]: „Variablen verwenden (auch verschiedene“
      Block 2756–2769, Niveaustufe am Block: F (Z2763); verschiedene Variablen in linearen Gleichungssystemen
  - 5. Drei Variablen und Lösungsvielfalt (Sek II) – H
    - H [Zeile 2876]: „− auch lineare Gleichungssysteme mit drei“
      Block 2860–2880, Niveaustufe am Block: H (Z2875); die drei Variablen stehen im RLP 1–10 auf H; die Einheit selbst ist eine Sek-II-Einheit nach GOST Q1/Q3
      Ermessen: Parameter, Lösungsscharen und Fallunterscheidungen gehören zur gymnasialen Oberstufe; der RLP 1–10 nennt auf H nur die drei Variablen und das Additionsverfahren.
- Sprossen je Verfahrenstyp:
  - Grafisch (Einheit 1)
    - Sprosse 1 · Zahlenpaar prüfen – Lösung von I, II, beiden (Vorstufe) → E [Zeile 2750]; Eintrag: Vorstufe
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 2 · Lösungspaare einer Gleichung in eine Tabelle (4×) → F [Zeile 2761]
      „Lösen linearer Gleichungssysteme mit zwei“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 3 · Gleichung nach y umstellen → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · Gerade zeichnen → F [Zeilen 2761–2763]
      „Angeben von passenden Situationen und grafischen Darstellungen zu vorgegeben Termen, Gleichungen und linearen“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 5 · zwei Geraden zeichnen und Schnittpunkt ablesen → F [Zeile 2761]
      „Lösen linearer Gleichungssysteme mit zwei“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 6 · Probe in beiden Gleichungen → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · Lösung an einem gegebenen Bild ablesen → F [Zeilen 2761–2763]
      „Angeben von passenden Situationen und grafischen Darstellungen zu vorgegeben Termen, Gleichungen und linearen“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 8 · Sonderfälle parallel und identisch → F [Zeile 2765]
      „Untersuchen der Lösbarkeit und der“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 9 · systematisches Probieren mit Tabelle → F [Zeile 2761]
      „Lösen linearer Gleichungssysteme mit zwei“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 10 · Prüfungshöhe: Zimmer und Betten durch Probieren oder grafisch lösen und begründen … → F [Zeile 2765]; Eintrag: Prüfungshöhe
      „Untersuchen der Lösbarkeit und der“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
  - Einsetzen (Einheit 2; LISUM-PH führt es in der Jahrgangsstufe acht als „nur Gym“ – hier für alle Bildungsgänge, weil die P10 es verlangt)
    - Sprosse 1 · Gleichung mit Vorzahl 1 ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · I ist nach y aufgelöst, in II einsetzen (4×) → G [Zeilen 2847–2848]
      „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 3 · I nach y umstellen (Vorzahl 1) → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · nach x umstellen → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · Klammer mit Zahl davor → F [Zeilen 2756–2757]
      „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 6 · Minus vor der Klammer → F [Zeilen 2756–2757]
      „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 7 · Dezimalzahlen (Geld) → G [Zeilen 2847–2848]
      „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 8 · negative Lösung → G [Zeilen 2847–2848]
      „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 9 · Gleichsetzen bei zwei Gleichungen y = … → G [Zeilen 2847–2848]
      „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 10 · Probe in beiden Gleichungen und Zahlenpaar angeben → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 11 · Prüfungshöhe: Preise aus einem System mit Dezimalzahlen durch Einsetzen … → G [Zeilen 2847–2848]; Eintrag: Prüfungshöhe
      „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
  - Addition (Einheit 3, GYM)
    - Sprosse 1 · gleiche Vorzahl oder Gegenzahl ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe, GYM
    - Sprosse 2 · Gegenzahlen, addieren (4×) → H [Zeile 2878]; Eintrag: GYM
      „− auch Nutzen des Additionsverfahrens“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 3 · gleiche Vorzahlen, subtrahieren → H [Zeile 2878]; Eintrag: GYM
      „− auch Nutzen des Additionsverfahrens“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 4 · eine Gleichung vervielfachen → H [Zeile 2878]; Eintrag: GYM
      „− auch Nutzen des Additionsverfahrens“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 5 · beide vervielfachen → H [Zeile 2878]; Eintrag: GYM
      „− auch Nutzen des Additionsverfahrens“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 6 · negative Zahlen → H [Zeile 2878]; Eintrag: GYM
      „− auch Nutzen des Additionsverfahrens“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 7 · Dezimalzahlen (Vorrat) → H [Zeile 2878]; Eintrag: Vorrat, GYM
      „− auch Nutzen des Additionsverfahrens“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 8 · Sonderfall keine oder unendlich viele Lösungen (Vorrat) → F [Zeile 2765]; Eintrag: Vorrat, GYM
      „Untersuchen der Lösbarkeit und der“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 9 · Verfahren wählen und begründen → G [Zeile 2849]; Eintrag: GYM
      „Vergleichen der Effektivität verschiedener“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 10 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP H und LISUM-PH Jg. 9 (Gymnasium) … → H [Zeile 2878]; Eintrag: Prüfungshöhe, Zielmarke, GYM
      „− auch Nutzen des Additionsverfahrens“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
  - Sachaufgaben (Einheit 4)
    - Sprosse 1 · Unbekannte benennen, Anzahlen und Beträge markieren (Vorstufe) → F [Zeile 2759]; Eintrag: Vorstufe
      „Variablen verwenden (auch verschiedene“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 2 · aus zwei Sätzen „zusammen …“ die Gleichungen aufstellen, nicht lösen (4×) → F [Zeile 2757]
      „Sachverhalten durch Terme, Gleichungen und“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 3 · Anzahl-und-Preis mit Dezimalzahlen → F [Zeile 2757]
      „Sachverhalten durch Terme, Gleichungen und“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 4 · Anzahl-und-Bestand (Zimmer, Räder) → F [Zeile 2757]
      „Sachverhalten durch Terme, Gleichungen und“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 5 · Zahlenrätsel mit Summe und Differenz → F [Zeile 2757]
      „Sachverhalten durch Terme, Gleichungen und“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 6 · Variablen einer gegebenen Gleichung benennen → F [Zeile 2759]
      „Variablen verwenden (auch verschiedene“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 7 · Gleichung als Satz formulieren → G [Zeile 2839]
      „Übersetzungen zwischen verschiedenen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 8 · aufstellen, lösen, zuordnen, Antwortsatz → G [Zeilen 2847–2848]
      „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 9 · Prüfungshöhe: Rosen und Tulpen – System aufstellen, deuten und lösen … → G [Zeilen 2847–2848]; Eintrag: Prüfungshöhe
      „Lösen von linearen Gleichungssystemen mit zwei Variablen (auch rechnerisch)“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
  - Grafisch, Sek II (Einheit 1)
    - Sprosse 1 · Schnittpunkt oder keiner? ankreuzen (Vorstufe) → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · Lösungsmenge eines Systems mit Vielfachen als Gerade zeichnen (Grundfall) → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Sek II
    - Sprosse 3 · Prüfungshöhe: vorgegebene Lösung bestätigen und begründen, dass es keine weitere gibt … → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Prüfungshöhe, Sek II
  - Addition, Sek II (Einheit 3)
    - Sprosse 1 · Gleiche Vorzahl oder Gegenzahl? ankreuzen (Vorstufe) → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · Gleichungen mit Gegenzahlen addieren und die Sonderfälle erkennen (Grundfall) → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Sek II
    - Sprosse 3 · eine Gleichung als Vielfaches einer anderen ergänzen (unendlich viele Lösungen) → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Sek II
    - Sprosse 4 · Prüfungshöhe: Koeffizienten so wählen, dass das System keine Lösung hat … → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Prüfungshöhe, Sek II
  - Sachaufgaben, Sek II (Einheit 4)
    - Sprosse 1 · Was ist unbekannt? ankreuzen (Vorstufe) → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · die Gleichungen eines Systems mit zwei Variablen als Sätze lesen (Grundfall) → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Sek II
    - Sprosse 3 · ein System mit drei Variablen als Summe der Anteile und Bilanz einer Zutat lesen → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Sek II
    - Sprosse 4 · Prüfungshöhe: Mischungssystem dreier Säfte im Sachzusammenhang deuten … → keine Stelle; Sek-II-Zeile (iqb); für sie gilt die GOST, nicht der RLP 1–10.; Eintrag: Prüfungshöhe, Sek II
  - Drei Variablen und Lösungsvielfalt (Einheit 5)
    - Sprosse 1 · „Wie viele Lösungen?“ und „Parameter im Koeffizienten?“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe einer Sek-II-Einheit; keine Stelle im RLP 1–10.; Eintrag: Vorstufe, Sek II
    - Sprosse 2 · eine vorgegebene Lösung in alle Gleichungen einsetzen und die Gültigkeit zeigen (Grundfall) → E [Zeile 2750]; Eintrag: Sek II
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · ein gestaffeltes System durch Rückwärtseinsetzen lösen → H [Zeile 2876]; Eintrag: Sek II
      „− auch lineare Gleichungssysteme mit drei“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 4 · ein System mit drei Variablen durch Subtrahieren und Einsetzen lösen → H [Zeile 2876]; Eintrag: Sek II
      „− auch lineare Gleichungssysteme mit drei“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 5 · die drei Fälle der Lösbarkeit rechnerisch erkennen → H [Zeile 2875]; Eintrag: Sek II
      „Lösen von Gleichungssystemen“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 6 · unendlich viele Lösungen als Schar mit Parameter schreiben → keine Stelle; Lösungsscharen mit Parameter nennt der RLP 1–10 nicht; das ist GOST-Stoff.; Eintrag: Sek II
    - Sprosse 7 · ein erweitertes System: die dritte Gleichung mit Parameter prüfen → keine Stelle; wie Sprosse 6: keine Stelle im RLP 1–10.; Eintrag: Sek II
    - Sprosse 8 · Fallunterscheidung am parameterabhängigen Koeffizienten → keine Stelle; wie Sprosse 6: keine Stelle im RLP 1–10.; Eintrag: Sek II
    - Sprosse 9 · Prüfungshöhe: Aussage über die Lösungsschar über eine Ungleichung im Parameter … → keine Stelle; Anforderungsbereich III der Oberstufe; keine Stelle im RLP 1–10.; Eintrag: Prüfungshöhe, Sek II
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 8, Mathematik: Terme und Gleichungen“ [Zeile 850]
  - Beleg [Zeile 851]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
  - Eine Reihe für alle Bildungsgänge mit dem Differenzierungshinweis (Zeile 851); sie trägt zusätzlich einen Block „Niveaustufe H (nur Gym)“ (Zeile 928). Der Eintrag vermerkt, dass die Planungshilfe das Einsetzungsverfahren in der Jahrgangsstufe acht als „nur Gym“ führt, der Katalog es aber für alle Bildungsgänge setzt, weil die P10 es verlangt.
- Spanne: ja  – Einheit 1 und 4 liegen auf F, Einheit 2 auf G, Einheit 3 und 5 auf H. Damit stehen Einheiten auf G und H und Einheiten auf F und darunter.
- Ermessen (4):
  - Einheit 2: der RLP nennt das Einsetzungs- und das Gleichsetzungsverfahren nicht beim Namen, sondern nur „auch rechnerisch“ (G). Der Eintrag stellt das selbst fest.
  - Einheit 3: das Additionsverfahren steht im Teil C nur auf H. Die ganze Kette trägt im Eintrag deshalb die GYM-Marke – hier stimmen Marke und Plan überein.
  - Sprosse „Sonderfall keine oder unendlich viele Lösungen“ (Einheit 3) liegt auf F, während der Rest der Kette auf H steht.
  - Die drei Sek-II-Ketten (Grafisch, Addition, Sachaufgaben) tragen durchweg „keine Stelle“: für sie gilt die GOST, nicht der RLP 1–10. Einheit 5 ist teilweise über die H-Zeile zu drei Variablen belegt; Parameter und Lösungsscharen sind es nicht.

### potenz-exponentialfunktionen – Stufe G (Exponentialfunktion y = a · bˣ, Modellieren von Wachstum und Zerfall) – H (y = a · bˣ + c, Potenzfunktionen y = a · xᵏ + b, Umkehrfunktion, Logarithmus)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Gleichungen und Funktionen G (S. 61, Zeilen aus dem Protokollabschnitt 08h): „Bestimmen und Beschreiben von Merkmalen (Definitionsbereich, Wertebereich, Form des Graphen, Schnittpunkte mit den Koordinatenachsen, Einfluss der Parameter auf den Verlauf des Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt, Periodizität) folgender Funktionstypen … Exponentialfunktionen der Form y = a · bˣ (b > 0, x ∈ ℕ)““
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP F; LISUM-PH „Prozentsatz als Operator (Wachstumsfaktor)“; P10 2018-OS-K2a Verfahren]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP E; P10 2018-OS-K2a Nebenweg]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP D/E; P10 2025-OS-K7a, 2016-OS-K4b, 2017-OS-K7b]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP F; LISUM-PH „Addition einer konstanten Zahl“]“
  - Zeile 61 (Typische Fehler): „[RLP G]“
- Lerneinheiten:
  - 1. Lineares und exponentielles Wachstum unterscheiden – F/G/H
    - G [Zeilen 2894–2896]: „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); Grundfall: lineare gegen exponentielle Funktion
    - F [Zeilen 2811–2814]: „Beschreiben, Analysieren, Interpretieren und Vergleichen von linearen Zusammenhängen und“
      Block 2811–2825, Niveaustufe am Block: F (Z2818); die lineare Seite des Vergleichs steht schon auf F
    - H [Zeile 2933]: „y = a xk + b (k∈Z und k∈Q+)“
      Block 2920–2957, Niveaustufe am Block: H (Z2934); die Potenzfunktion erst auf H; im Eintrag als Vorrat
  - 2. Wachstumsfaktor und Wachstumstabelle – E/G
    - E [Zeile 1916]: „Nutzen von Prozentsätzen als Operatoren“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); der Wachstumsfaktor als Operator steht schon auf E
    - G [Zeilen 2908–2910]: „bei Wachstums- und Zerfallsprozessen“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); das Modellieren von Wachstum und Zerfall auf G
      Ermessen: Das Wort „Wachstumsfaktor“ kommt im Teil C nicht vor; die Einheit ist über den Prozentsatz als Operator (E) und das Modellieren (G) belegt.
  - 3. Exponentialfunktion aufstellen und auswerten – G
    - G [Zeilen 2916–2918]: „− Exponentialfunktionen der Form y = a bx (b>0, x∈N)“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); die Form y = a · bˣ steht ausdrücklich auf G
    - G [Zeilen 2909–2911]: „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); Übersetzen zwischen Sachtext, Tabelle, Graph und Gleichung
  - 4. Verdopplungs- und Halbwertszeit – G/H
    - G [Zeilen 2908–2910]: „bei Wachstums- und Zerfallsprozessen“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); Ablesen und Probieren innerhalb des Modellierens
    - H [Zeilen 2005–2006]: „Umformen von Potenzen in Logarithmen und umgekehrt“
      Block 2001–2007, Niveaustufe am Block: H (Z2006); der genaue Zeitpunkt über den Logarithmus erst auf H; im Eintrag als Vorrat
      Ermessen: „Verdopplungszeit“ und „Halbwertszeit“ kommen im Teil C nicht vor; die Einheit hängt am Modellieren von Wachstums- und Zerfallsprozessen (G).
- Sprossen je Verfahrenstyp:
  - Wachstumsart erkennen und begründen (Einheit 1)
    - Sprosse 1 · „gleicher Betrag oder gleicher Prozentsatz“ ankreuzen (Vorstufe) → G [Zeilen 2894–2896]; Eintrag: Vorstufe
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · in einer kurzen Tabelle die Differenzen bilden und entscheiden (4×) → F [Zeilen 2811–2814]
      „Beschreiben, Analysieren, Interpretieren und Vergleichen von linearen Zusammenhängen und“ – Block 2811–2825, Niveaustufe am Block: F (Z2818)
    - Sprosse 3 · in derselben Tabelle die Quotienten bilden und entscheiden → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · zu einer Tabelle die Wachstumsart ankreuzen und in einem Satz begründen → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · dieselbe Entscheidung aus einem Text ohne Tabelle → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · Abnahme statt Zunahme → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · begründen, warum die Zuwächse in Euro größer werden, obwohl der Prozentsatz gleich bleibt → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · Grenzen des Modells nennen → keine Stelle; Die Grenzen eines Modells nennt der Teil C nicht; sie stehen in der Planungshilfe.
    - Sprosse 9 · Prüfungshöhe: Wachstumsart mit Begründung aus einer Umsatz- und einer Zerfallstabelle … → G [Zeilen 2894–2896]; Eintrag: Prüfungshöhe
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Graph zu einem Wachstumsprozess auswählen (Einheit 1)
    - Sprosse 1 · „wo beginnt der Graph“ ankreuzen (Vorstufe) → G [Zeile 2899]; Eintrag: Vorstufe
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · zu drei Skizzen notieren, welche Gerade und welche Kurve ist (4×) → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · den Startwert an der senkrechten Achse markieren und den Graphen im Ursprung ausschließen → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · den passenden Graphen ankreuzen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · in einem Satz begründen, warum die Gerade nicht passt → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · für jeden der drei Graphen eine eigene Begründung schreiben → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · fallender Graph bei Abnahme → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · Prüfungshöhe: passenden Graphen auswählen und die anderen begründet ausschließen … → G [Zeilen 2894–2896]; Eintrag: Prüfungshöhe
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Wertepaare darstellen (Einheit 1)
    - Sprosse 1 · Skala mit größeren Schritten lesen (Vorstufe) → G [Zeilen 2902–2903]; Eintrag: Vorstufe
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · Punkte aus einer gegebenen Tabelle eintragen (4×) → G [Zeilen 2894–2896]
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · Zwischenwerte auf einer Skala mit größeren Schritten genau abtragen → G [Zeilen 2902–2903]
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Punkte zur Kurve verbinden → G [Zeilen 2894–2896]
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · Achseneinteilung für gegebene Werte selbst wählen und beschriften → G [Zeilen 2902–2903]
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · Prüfungshöhe: Wertetabelle als Punkte darstellen; Achseneinteilung wählen … → G [Zeilen 2894–2896]; Eintrag: Prüfungshöhe
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Potenzfunktion einordnen (Einheit 1, Vorrat)
    - Sprosse 1 · ankreuzen, ob die Variable in der Basis oder im Exponenten steht (Vorstufe) → H [Zeile 2933]; Eintrag: Vorstufe, Vorrat
      „y = a xk + b (k∈Z und k∈Q+)“ – Block 2920–2957, Niveaustufe am Block: H (Z2934)
    - Sprosse 2 · Wertetabelle zu einer Potenzfunktion ausfüllen (4×) → H [Zeile 2933]; Eintrag: Vorrat
      „y = a xk + b (k∈Z und k∈Q+)“ – Block 2920–2957, Niveaustufe am Block: H (Z2934)
    - Sprosse 3 · Graph einer Potenzfunktion zeichnen → H [Zeile 2933]; Eintrag: Vorrat
      „y = a xk + b (k∈Z und k∈Q+)“ – Block 2920–2957, Niveaustufe am Block: H (Z2934)
    - Sprosse 4 · Graphen von Potenz- und Exponentialfunktion nebeneinander vergleichen → H [Zeilen 2920–2922]; Eintrag: Vorrat
      „Gegenüberstellen einander entsprechender Eigenschaften der bekannten Funktionsklassen“ – Block 2920–2957, Niveaustufe am Block: H (Z2934)
    - Sprosse 5 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP H, Lehrwerk und LISUM-PH (Gym) … → H [Zeile 2933]; Eintrag: Prüfungshöhe, Zielmarke, Vorrat
      „y = a xk + b (k∈Z und k∈Q+)“ – Block 2920–2957, Niveaustufe am Block: H (Z2934)
  - Wachstumsfaktor bestimmen (Einheit 2)
    - Sprosse 1 · „mehr oder weniger“ ankreuzen (Vorstufe) → E [Zeile 1916]; Eintrag: Vorstufe
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 2 · Prozentsatz einer Zunahme in den Faktor umrechnen (4×) → E [Zeile 1916]
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 3 · Prozentsatz einer Abnahme in den Faktor → E [Zeile 1916]
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · Faktor zurück in den Prozentsatz → E [Zeile 1916]
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 5 · Faktor als Quotient zweier Tabellenwerte berechnen → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · mehrere Quotienten bilden und vergleichen, Ergebnis in einem Satz → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · Wachstumsrate aus zwei Werten, die nicht nebeneinander stehen → keine Stelle; Das Zurückrechnen der Rate über mehrere Schritte nennt der Teil C nicht.
    - Sprosse 8 · Prüfungshöhe: Faktor an einer Bakterientabelle nachweisen; Prozentsatz an einer Umsatztabelle … → E [Zeile 1916]; Eintrag: Prüfungshöhe
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
  - Wachstumstabelle fortschreiben (Einheit 2)
    - Sprosse 1 · „Differenz oder Quotient“ ankreuzen (Vorstufe) → G [Zeilen 2894–2896]; Eintrag: Vorstufe
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · nächsten Wert berechnen (Wert mal Faktor) (4×) → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · Anfangswert in den Schritt null eintragen → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Lücke mitten in der Tabelle füllen → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · mehrere Schritte auf einmal mit der Potenz des Faktors → G [Zeilen 2916–2918]
      „− Exponentialfunktionen der Form y = a bx (b>0, x∈N)“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · einen Schritt zurückrechnen → keine Stelle; Das Zurückrechnen eines Schritts nennt der Teil C nicht.
    - Sprosse 7 · fehlende Zeitangabe im Tabellenkopf bestimmen und mit dem Faktor prüfen → keine Stelle; Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 8 · Tabelle eines Zerfalls mit Faktor kleiner eins → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · Prüfungshöhe: zwei Felder einer Tabelle ergänzen; Wert und fehlende Zeitangabe … → G [Zeilen 2908–2910]; Eintrag: Prüfungshöhe
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Exponentialfunktion aufstellen und deuten (Einheit 3)
    - Sprosse 1 · „welcher Schritt ist null“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Anfangswert und Faktor in einem Text unterstreichen (4×) → G [Zeilen 2916–2918]
      „− Exponentialfunktionen der Form y = a bx (b>0, x∈N)“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · Gleichung aus beiden aufstellen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Gleichung für eine Abnahme aufstellen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · unter vier Gleichungen die passende ankreuzen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · zu einer gegebenen Gleichung die Bedeutung der Bestandteile eintragen → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · Faktor als „hundert Prozent plus Zuwachs“ erklären → E [Zeile 1916]
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 8 · Prüfungshöhe: Gleichung zu einer Mietsteigerung aufstellen; Bedeutung der Bestandteile … → G [Zeilen 2909–2911]; Eintrag: Prüfungshöhe
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Wert und Schwellenwert berechnen (Einheit 3)
    - Sprosse 1 · Potenz mit dem Taschenrechner tippen (Vorstufe) → keine Stelle; Der RLP nennt den Taschenrechner nur bei Logarithmen (H).; Eintrag: Vorstufe
    - Sprosse 2 · Wert nach wenigen Schritten Schritt für Schritt (4×) → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · denselben Wert mit einer Potenz in einem Zug → G [Zeilen 2916–2918]
      „− Exponentialfunktionen der Form y = a bx (b>0, x∈N)“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Schritte aus Jahreszahlen zählen und einsetzen → keine Stelle; Das Zählen der Zeitschritte nennt der Teil C nicht.
    - Sprosse 5 · Ergebnis runden und mit Einheit angeben → E [Zeilen 1909–1910]
      „Angeben von Ergebnissen mit sinnvoller Genauigkeit (auch beim Rechnen mit rationalen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 6 · eine Behauptung prüfen: Wert berechnen, vergleichen, entscheiden, begründen → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · zwei Vorhersagen vergleichen (exponentiell gegen einen Gesamtprozentsatz) → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · schrittweise multiplizieren, bis eine Schwelle überschritten ist → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · Prüfungshöhe: Wert nach vielen Schritten mit der Potenz; erstes Jahr über einer Million … → G [Zeilen 2908–2910]; Eintrag: Prüfungshöhe
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Verdopplungs- und Halbwertszeit (Einheit 4)
    - Sprosse 1 · „was wird verdoppelt“ ankreuzen (Vorstufe) → keine Stelle; „Verdopplungszeit“ und „Halbwertszeit“ kommen im Teil C nicht vor.; Eintrag: Vorstufe
    - Sprosse 2 · Zielwert bilden: Anfangswert verdoppeln oder halbieren (4×) → keine Stelle; wie Sprosse 1: keine Stelle.
    - Sprosse 3 · Zielwert in einer Tabelle suchen und die Zeit ablesen → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Zielwert zwischen zwei Tabellenwerten, nächstliegende Zeit angeben → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · Zielwert am Graphen ablesen (waagerecht, senkrecht) → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · das Vorgehen in zwei Sätzen beschreiben → keine Stelle; Das Beschreiben des Ablesevorgangs nennt der Teil C nicht.
    - Sprosse 7 · durch Probieren mit dem Faktor rechnen und die Schritte zählen → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · prüfen, dass die Zeit vom Startwert unabhängig ist → keine Stelle; keine Stelle; die Eigenschaft nennt der Teil C nicht.
    - Sprosse 9 · Logarithmus für den genauen Zeitpunkt (Vorrat) → H [Zeilen 2005–2006]; Eintrag: Vorrat
      „Umformen von Potenzen in Logarithmen und umgekehrt“ – Block 2001–2007, Niveaustufe am Block: H (Z2006)
    - Sprosse 10 · Prüfungshöhe: Verdopplungszeit am Graphen ablesen; Halbwertszeit aus einer Zerfallstabelle … → G [Zeilen 2908–2910]; Eintrag: Prüfungshöhe
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
- LISUM: getrennte Reihen EBR/FOR und GYM; Reihen: „Jahrgangsstufe 10 (EBR und FOR), Mathematik: Exponentielles Wachstum und Exponentialfunktionen“ [Zeile 2487]; „Jahrgangsstufe 10 (Gymnasium), Mathematik: Exponentielles Wachstum und Exponentialfunktionen“ [Zeile 2566]
  - Beleg [Zeile 2488]: „Hinweis: Die Differenzierung zwischen EBR- und FOR-Klassen erfolgt über Tiefgründigkeit der Bearbeitung“
  - Zwei getrennte Reihen: EBR/FOR ab Zeile 2487, Gymnasium ab Zeile 2566. Der Hinweis der EBR/FOR-Reihe nennt nur EBR und FOR (Zeile 2488), die Gymnasialreihe trägt stattdessen den Hinweis „An Gesamtschulen sollte diese Thematik in Jahrgangsstufe 11 bearbeitet werden“ (Zeile 2567). Die EBR/FOR-Reihe hat Blöcke auf E (Zeile 2494) und G (Zeile 2500); die Gymnasialreihe zusätzlich zwei Blöcke auf H (Zeilen 2615 und 2649).
- Spanne: ja  – Die Einheiten 1 bis 4 liegen auf G, der Wachstumsfaktor auf E, der Vergleich mit dem linearen Wachstum auf F; Potenzfunktion und Logarithmus liegen auf H. Damit stehen Einheiten und Sprossen auf G und H und mehrere auf F und darunter.
- Ermessen (4):
  - Einheit 2: „Wachstumsfaktor“ kommt im Teil C nicht vor; die Einheit ist über den Prozentsatz als Operator (E) und das Modellieren von Wachstums- und Zerfallsprozessen (G) belegt.
  - Einheit 4: „Verdopplungszeit“ und „Halbwertszeit“ stehen nicht im Teil C. Die ersten beiden Sprossen der Kette tragen deshalb „keine Stelle“; die übrigen hängen am Modellieren (G).
  - Sprossen „einen Schritt zurückrechnen“, „fehlende Zeitangabe bestimmen“, „Wachstumsrate aus zwei nicht benachbarten Werten“, „Schritte aus Jahreszahlen zählen“: keine Stelle; alle vier sind Aufgabenformen der P10.
  - Sprosse „Grenzen des Modells nennen“: keine Stelle im Teil C; die Planungshilfe nennt sie (Zeile 2599).

### potenzen-wurzeln – Stufe F (negative Exponenten, Näherungswerte G; Zehnerpotenzschreibweise situationsangemessen H; Quadratzahlen bis 100 C)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Zahlen und Operationen F (S. 42, Zahlvorstellungen): „Darstellen von Potenzen, insbesondere Zehnerpotenzen mit natürlichem Exponenten““
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[RLP C/D; P10 2020-OS-B1h Verfahren als Malkette]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP C „Nennen und Erkennen von Quadratzahlen (bis 100)“]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP E; P10 2014-OS-K7a Voraussetzung „Potenz mit negativer Basis“, 2015-OS-B1j „negative Basis“]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2023-OS-B1f Fehlerquelle Quadrat einer Dezimalzahl als Verdopplung]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP C „Zahldarstellungen natürlicher Zahlen bis eine Million“; P10 2015-OS-K3a Fehlerquelle „Nullen falsch zählen“]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2016-OS-B1h, 2019-OS-B1j Verfahren „Komma verschieben“]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP D/E; P10 2017-OS-B1e, 2022-OS-B1j, 2015-OS-B1c, 2014-OS-B1h]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D/E „sinnvolle Genauigkeit“; RLP G „sachgerechtes Runden von reellen Zahlen“]“
  - Zeile 35 (Merkkasten): „[P10 2022-OS-B1j Fehlerquelle negative Potenz als negative Zahl; RLP G a⁻ⁿ als Kehrwert]“
  - Zeile 39 (Merkkasten): „[P10 2015-OS-B1c, 2014-OS-B1h Voraussetzung „Wurzel abschätzen“; RLP G Näherungswerte]“
  - Zeile 49 (Merkkasten): „[RLP F]“
  - Zeile 49 (Merkkasten): „[RLP G]“
  - Zeile 57 (Merkkasten): „[RLP F]“
  - Zeile 65 (Merkkasten): „[RLP F]“
  - Zeile 65 (Merkkasten): „[RLP G]“
  - Zeile 83 (Typische Fehler): „[RLP G „sachgerechtes Runden“; P10 2025-OS-K5c Näherungswert; FD]“
  - Zeile 88 (Für schwache Schüler): „[RLP F, MO]“
- Lerneinheiten:
  - 1. Potenzen – C/F/G
    - F [Zeilen 1974–1975]: „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); Grundfall: natürliche Exponenten
    - G [Zeilen 1990–1991]: „Potenzen mit negativen Exponenten auf bekannte Strukturen zurückzuführen“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); Sonderfall: negative Exponenten erst auf G
    - C [Zeilen 1727–1728]: „Nennen und Erkennen von Quadratzahlen (bis 100)“
      Block 1717–1731, Niveaustufe am Block: C (Z1727); die Quadratzahlen selbst stehen schon auf C
  - 2. Zehnerpotenzen – F/G/H
    - F [Zeilen 1930–1932]: „Darstellen von Potenzen, insbesondere Zehnerpotenzen mit natürlichem Exponenten“
      Block 1927–1937, Niveaustufe am Block: F (Z1934); Grundfall
    - G [Zeilen 1990–1991]: „Potenzen mit negativen Exponenten auf bekannte Strukturen zurückzuführen“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); kleine Zahlen mit negativer Hochzahl
    - H [Zeilen 1956–1958]: „situationsangemessenes Darstellen von Zahlen als Brüche, Dezimalzahlen,“
      Block 1952–1960, Niveaustufe am Block: H (Z1956); die situationsangemessene Wahl der Zehnerpotenzschreibweise erst auf H
      Ermessen: Der RLP nennt die Schreibweise a · 10ⁿ nicht mit diesem Namen und auch nicht die Wörter „Basis“ und „Exponent“; die Zuordnung erfolgt über das Darstellen rationaler Zahlen mithilfe von Zehnerpotenzen.
  - 3. Quadratwurzeln – F/G
    - F [Zeilen 1977–1979]: „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); Grundfall
    - G [Zeilen 1944–1945]: „Angeben von Näherungswerten für reelle Zahlen“
      Block 1940–1947, Niveaustufe am Block: G (Z1947); Näherungswert und Abschätzen erst auf G
- Sprossen je Verfahrenstyp:
  - Potenzen (Einheit 1)
    - Sprosse 1 · „hoch oder mal“ ankreuzen, Basis und Exponent beschriften (Vorstufe) → keine Stelle; Der RLP nennt weder „Basis“ noch „Exponent“ als Begriffe.; Eintrag: Vorstufe
    - Sprosse 2 · Potenz als Malkette schreiben und ausrechnen, Malkette als Potenz (4×) → F [Zeilen 1974–1975]
      „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 3 · Potenz und Produkt nebeneinander ausrechnen → F [Zeilen 1974–1975]
      „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 4 · Quadratzahlen bis zwanzig hoch zwei, Kubikzahlen bis zehn hoch drei → C [Zeilen 1727–1728]
      „Nennen und Erkennen von Quadratzahlen (bis 100)“ – Block 1717–1731, Niveaustufe am Block: C (Z1727)
    - Sprosse 5 · Potenzwert mit dem Taschenrechner (Tasten x² und ^) → keine Stelle; Der RLP nennt den Taschenrechner für Potenzen nicht; nur für Logarithmen (H).
    - Sprosse 6 · negative Basis mit Klammer, gerade und ungerade Hochzahl → keine Stelle; Die negative Basis kommt im Teil C nicht vor; der RLP F kennt nur natürliche Exponenten bei rationalen Zahlen.
    - Sprosse 7 · Minus vor der Potenz ohne Klammer → keine Stelle; wie Sprosse 6: keine Stelle.
    - Sprosse 8 · Potenz einer Dezimalzahl → F [Zeilen 1974–1975]
      „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 9 · zwei Potenzen vergleichen (beide ausrechnen) → F [Zeilen 1930–1932]
      „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 10 · drei Potenzen ordnen und die größte unterstreichen (P10-Form) → F [Zeilen 1930–1932]
      „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 11 · Exponent durch wiederholtes Malnehmen bestimmen (P10-Form) → F [Zeilen 1974–1975]
      „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 12 · Exponent durch Zerlegen des Werts → F [Zeilen 1974–1975]
      „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 13 · Exponent mit Basis zehn → F [Zeilen 1930–1932]
      „Darstellen von Potenzen, insbesondere Zehnerpotenzen mit natürlichem Exponenten“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 14 · negative Hochzahl als Bruch, dann als Dezimalzahl (LISUM: „nur GYM“ in der Jg.-8-Reihe) → G [Zeilen 1990–1991]; Eintrag: LISUM „nur GYM“, Marke überschrieben
      „Potenzen mit negativen Exponenten auf bekannte Strukturen zurückzuführen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 15 · Potenz mit negativer Hochzahl gegen Dezimalzahl vergleichen (P10-Form) → G [Zeilen 1990–1991]
      „Potenzen mit negativen Exponenten auf bekannte Strukturen zurückzuführen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 16 · Prüfungshöhe: Exponent angeben; größte von drei Potenzen; Vergleichszeichen … → F [Zeilen 1930–1932]; Eintrag: Prüfungshöhe
      „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
  - Zehnerpotenzen (Einheit 2)
    - Sprosse 1 · „groß oder klein“ und „Stellen oder Nullen“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Zehnerpotenz ausschreiben und Zahl als Zehnerpotenz schreiben (4×) → F [Zeilen 1930–1932]
      „Darstellen von Potenzen, insbesondere Zehnerpotenzen mit natürlichem Exponenten“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 3 · Zahlwörter zuordnen → C [Zeilen 1721–1723]
      „Wechsel zwischen den Zahldarstellungen natürlicher Zahlen bis 1 Mio.“ – Block 1717–1731, Niveaustufe am Block: C (Z1727)
    - Sprosse 4 · ganze Zahl mal zehn, hundert, tausend durch Nullen anhängen → keine Stelle; Rechentechnik; der RLP nennt das Anhängen von Nullen nicht.
    - Sprosse 5 · ganze Zahl mal Zehnerpotenz mit Hochzahl → F [Zeilen 1933–1936]
      „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 6 · Dezimalzahl mal Zehnerpotenz: Komma nach rechts, Nullen auffüllen → F [Zeilen 1933–1936]
      „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 7 · Zehnerpotenzschreibweise ausschreiben (P10-Form) → F [Zeilen 1933–1936]
      „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 8 · Zahl in Zehnerpotenzschreibweise schreiben: Komma nach der ersten Ziffer, Stellen zählen → F [Zeilen 1933–1936]
      „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 9 · fehlende Hochzahl eintragen (P10-Form) → F [Zeilen 1933–1936]
      „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 10 · passende ausgeschriebene Zahl unter drei Angeboten ankreuzen (P10-Form) → F [Zeilen 1933–1936]
      „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 11 · negative Hochzahl: Komma nach links, Nullen vorn (P10-Form; LISUM „nur GYM“) → G [Zeilen 1990–1991]; Eintrag: LISUM „nur GYM“, Marke überschrieben
      „Potenzen mit negativen Exponenten auf bekannte Strukturen zurückzuführen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 12 · Zahl kleiner als eins in Zehnerpotenzschreibweise → G [Zeilen 1990–1991]
      „Potenzen mit negativen Exponenten auf bekannte Strukturen zurückzuführen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 13 · Zahlen in Zehnerpotenzschreibweise ordnen, auch negative (P10-Form) → F [Zeilen 1930–1932]
      „Vergleichen und Ordnen von rationalen Zahlen (auch Potenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 14 · Taschenrechner-Anzeige mit E lesen und Zahl mit der EXP-Taste eingeben → keine Stelle; Die Anzeige des Taschenrechners nennt der RLP nicht.
    - Sprosse 15 · gerundeter Wert in Zehnerpotenzschreibweise mit Einheit → F [Zeilen 1935–1936]
      „Runden von rationalen Zahlen (auch in Potenzschreibweise)“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
    - Sprosse 16 · Sachaufgabe aus Astronomie oder Mikrowelt → H [Zeilen 1956–1958]
      „situationsangemessenes Darstellen von Zahlen als Brüche, Dezimalzahlen,“ – Block 1952–1960, Niveaustufe am Block: H (Z1956)
    - Sprosse 17 · Zehnerpotenzen multiplizieren und dividieren (Vorrat) → G [Zeilen 1993–1994]; Eintrag: Vorrat
      „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 18 · Prüfungshöhe: Hochzahl eintragen; negative Hochzahl ausschreiben; Lichtjahre … → F [Zeilen 1933–1936]; Eintrag: Prüfungshöhe
      „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen mit natürlichen“ – Block 1927–1937, Niveaustufe am Block: F (Z1934)
  - Quadratwurzeln (Einheit 3)
    - Sprosse 1 · „Quadratzahl oder nicht“ und „zwischen welchen Quadratzahlen“ ankreuzen (Vorstufe) → C [Zeilen 1727–1728]; Eintrag: Vorstufe
      „Nennen und Erkennen von Quadratzahlen (bis 100)“ – Block 1717–1731, Niveaustufe am Block: C (Z1727)
    - Sprosse 2 · Wurzel aus einer Quadratzahl im Kopf, mit der Probe „mal sich selbst“ (4×) → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 3 · Wurzel mit dem Taschenrechner, Anzeige ablesen, auf zwei Dezimalen runden → G [Zeilen 1943–1944]
      „sachgerechtes Runden von reellen Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 4 · Wurzel zwischen zwei Nachbar-Quadratzahlen abschätzen, dann vergleichen → G [Zeilen 1944–1945]
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 5 · Wurzel gegen Dezimalzahl und Bruch vergleichen → G [Zeilen 1940–1941]
      „Vergleichen und Ordnen von reellen Zahlen über“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 6 · Zahlen mit Wurzel aufsteigend ordnen → G [Zeilen 1940–1941]
      „Vergleichen und Ordnen von reellen Zahlen über“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 7 · Quadrat einer Wurzel → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 8 · Wurzel eines Quadrats mit negativer Basis: erst das Quadrat → keine Stelle; Die negative Basis unter der Wurzel kommt im Teil C nicht vor.
    - Sprosse 9 · Wurzel aus einer negativen Zahl: kein Wert, gegen Minus vor der Wurzel → keine Stelle; keine Stelle; der RLP äußert sich nicht zum Definitionsbereich der Wurzel.
    - Sprosse 10 · Wurzel aus Dezimalzahl und Bruch → keine Stelle; keine Stelle; der RLP nennt die Wurzel nur als Umkehrung der Potenzschreibweise.
    - Sprosse 11 · Quadratseite aus dem Flächeninhalt → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 12 · Wurzel als letzter Schritt einer Formel: Term unter der Wurzel erst ausrechnen → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 13 · Kubikwurzel (Vorrat) → F [Zeilen 1977–1979]; Eintrag: Vorrat
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 14 · Prüfungshöhe: Aussagen über die Wurzel aus dem Quadrat; Zahlen mit Wurzel ordnen … → G [Zeilen 1940–1941]; Eintrag: Prüfungshöhe
      „Vergleichen und Ordnen von reellen Zahlen über“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 8, Mathematik: Potenzen und Wurzeln“ [Zeile 730]; „Jahrgangsstufe 9, Mathematik: Terme und Gleichungen mit Potenzen bzw. Wurzeln“ [Zeile 1644]
  - Beleg [Zeile 750]: „(nur GYM: auch Zehnerpotenzen mit negativen ganzzahligen Exponenten)“
  - Keine getrennten Reihen: beide Reihen führen EBR, FOR und GYM gemeinsam und tragen den Differenzierungshinweis (Zeilen 731 und 1645). Die Trennung steht innerhalb der Reihe als Klammerzusatz „nur GYM“ – in der Jahrgangsstufe 8 für Zehnerpotenzen mit negativen Exponenten (Zeile 750) und für die n-te Wurzel (Zeile 792), in der Jahrgangsstufe 9 für das Umformen von Termen mit Wurzeln (Zeile 1669).
- Spanne: ja  – Grundfälle liegen auf C und F, negative Exponenten und Näherungswerte auf G, die situationsangemessene Zehnerpotenzschreibweise auf H. Damit stehen Einheiten und Sprossen sowohl auf G/H als auch auf F und darunter.
- Ermessen (5):
  - Einheit 2 im Ganzen: die Schreibweise a · 10ⁿ und die Wörter „Basis“ und „Exponent“ kommen im Teil C nicht vor; zugeordnet über „Darstellen von rationalen Zahlen (auch mithilfe von Zehnerpotenzen …)“ (F).
  - Sprossen zur negativen Basis (Einheit 1, Sprossen 6 und 7) und zur Wurzel aus negativen Zahlen (Einheit 3, Sprossen 8 bis 10): keine Stelle. Der RLP F kennt bei rationalen Zahlen nur natürliche Exponenten.
  - Sprossen zum Taschenrechner (Einheit 1 Sprosse 5, Einheit 2 Sprosse 14): keine Stelle; der RLP nennt den Taschenrechner nur bei Logarithmen (H).
  - Sprosse „Wurzel als letzter Schritt einer Formel“: zugeordnet über das Umstellen von Formeln unter Gleichungen und Funktionen (E), nicht über eine Zeile zu Zahlen und Operationen.
  - Sprossen 14 (Einheit 1) und 11 (Einheit 2): der Eintrag vermerkt, dass die LISUM-Marke „nur GYM“ von der P10 überschrieben wird. Die RLP-Stufe G bleibt davon unberührt – die Marke des Eintrags und die Stufe des Plans sagen Verschiedenes.

### prozentrechnung – Stufe E–F
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] D: „Verwenden von gebrochenen Zahlen als Operator (z. B. zwei Drittel von 60 Euro)“.“
  - Zeile 6 (Verortung): „E: „Beschreiben von Prozenten als weitere Darstellungsform für gebrochene Zahlen““
  - Zeile 6 (Verortung): „F: „… bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe von digitalen Mathematikwerkzeugen)““
  - Zeile 6 (Verortung): „H: „situationsangemessenes Darstellen von Zahlen als Brüche, Dezimalzahlen, Prozentzahlen“.“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[MSK B1B/B2C, RLP D]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP D „Operator“]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D, LS-AA Kl. 6 V 4]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 46 (Merkkasten): „[RLP E]“
- Lerneinheiten:
  - 1. Prozente als Anteile – D/E
    - E [Zeilen 1838–1839]: „Beschreiben von Prozenten als weitere Darstellungsform für“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); Grundfall
    - E [Zeilen 1838–1839]: „Vergleichen und Ordnen von − Prozentangaben“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); Prozentangaben vergleichen
    - D [Zeilen 1889–1890]: „Verwenden von gebrochenen Zahlen als Operator“
      Block 1871–1894, Niveaustufe am Block: D (Z1885); die Vorstufe „Anteil von“ liegt schon auf D
  - 2. Prozentsatz berechnen – E
    - E [Zeilen 1838–1840]: „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); Grundfall
    - E [Zeilen 1897–1898]: „Nutzen, Darstellen und Beschreiben von Strategien und Gesetzen bei der Prozentrechnung, z. B. mithilfe“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Prozentstreifen, Dreisatz, Verhältnisgleichung
  - 3. Prozentwert berechnen – E
    - E [Zeile 1916]: „Nutzen von Prozentsätzen als Operatoren“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Grundfall: p % von G
    - E [Zeilen 1838–1840]: „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“
      Block 1838–1860, Niveaustufe am Block: E (Z1850)
  - 4. Grundwert berechnen – E
    - E [Zeilen 1838–1840]: „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); der RLP nennt die drei Größen gemeinsam, nicht je eine eigene Aufgabenart
    - E [Zeile 1899]: „auch Dreisatz und“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Rückrechnen über den Dreisatz
  - 5. Prozentuale Veränderung – F
    - F [Zeilen 1975–1976]: „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); Rabatt und Zinsen stehen erst auf F
    - F [Zeilen 1981–1982]: „Zahlen (auch im Zusammenhang mit der Prozentrechnung)“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); Überschlagen und Überprüfen im Zusammenhang mit der Prozentrechnung, ebenfalls F
- Sprossen je Verfahrenstyp:
  - Umwandeln (Einheit 1)
    - Sprosse 1 · grobe Anteile am Streifen ablesen (4×) → E [Zeilen 1898–1899]
      „mithilfe des Prozentstreifens“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 2 · Bruch mit dem Nenner hundert → E [Zeilen 1838–1839]
      „Beschreiben von Prozenten als weitere Darstellungsform für“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 3 · Nenner, der in hundert aufgeht, erweitern → D [Zeilen 1825–1826]
      „Kürzen und Erweitern von Brüchen“ – Block 1812–1836, Niveaustufe am Block: D (Z1826)
    - Sprosse 4 · Dezimalzahl ↔ Prozent → E [Zeilen 1838–1839]
      „Beschreiben von Prozenten als weitere Darstellungsform für“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 5 · Anteilsformulierung („jeder fünfte“) → keine Stelle; Sprachliche Anteilsform; der RLP nennt sie nicht.
    - Sprosse 6 · Rest zum Ganzen → keine Stelle; keine eigene Stelle; folgt aus der Beziehung der drei Größen, wird aber nicht genannt.
    - Sprosse 7 · Prüfungshöhe: zur Prozentangabe die passende Anteilsaussage ankreuzen … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Prozentsatz (Einheit 2)
    - Sprosse 1 · Anteil am Streifen ablesen (Vorstufe) → E [Zeilen 1898–1899]; Eintrag: Vorstufe
      „mithilfe des Prozentstreifens“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 2 · Teil von 100 (4×) → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 3 · Teil von 50, 25, 20, 10 → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 4 · Teil : Ganzes als Dezimalzahl mit Taschenrechner → E [Zeile 1903]
      „mit rationalen Zahlen (auch unter Verwendung eines“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 5 · runden → E [Zeilen 1909–1910]
      „Angeben von Ergebnissen mit sinnvoller Genauigkeit (auch beim Rechnen mit rationalen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 6 · aus Sachtext, Ganzes zuerst finden → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 7 · Rabatt in Prozent aus altem und neuem Preis → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 8 · Prüfungshöhe: Anteil aus zwei Zahlen eines Sachtextes, gerundet … → E [Zeilen 1909–1910]; Eintrag: Prüfungshöhe
      „Angeben von Ergebnissen mit sinnvoller Genauigkeit (auch beim Rechnen mit rationalen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
  - Prozentwert (Einheit 3)
    - Sprosse 1 · 50 %, 25 %, 10 % vom Ganzen am Streifen (4×) → E [Zeilen 1898–1899]
      „mithilfe des Prozentstreifens“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 2 · Ein-Prozent-Weg mit glatten Zahlen → E [Zeile 1899]
      „auch Dreisatz und“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 3 · Zehn-Prozent-Schritte (dreißig, fünfzehn, fünf Prozent) → E [Zeile 1905]
      „Durchführen von einfachen Rechnungen und“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · Dezimalzahl mal Grundwert → E [Zeile 1916]
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 5 · Grundwert mit Komma → E [Zeilen 1901–1902]
      „Prüfen und Übertragen der bekannten operativen Strategien, Gesetze und Verfahren auf das Rechnen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 6 · Ersparnis oder neuer Preis (Frage genau lesen) → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 7 · über das Ganze hinaus → keine Stelle; Prozentsätze über hundert nennt der RLP nicht.
    - Sprosse 8 · Prüfungshöhe: Rabatt in Euro als Ankreuzaufgabe, mit dem Restpreis als Falle … → F [Zeilen 1975–1976]; Eintrag: Prüfungshöhe
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
  - Grundwert (Einheit 4)
    - Sprosse 1 · Streifen: zwanzig Prozent sind vier Kästchen, wie viel ist das Ganze? (Vorstufe) → E [Zeilen 1898–1899]; Eintrag: Vorstufe
      „mithilfe des Prozentstreifens“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 2 · glatte Sätze mal zwei, vier, fünf, zehn (4×) → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 3 · Ein-Prozent-Weg → E [Zeile 1899]
      „auch Dreisatz und“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · beliebiger Satz mit Taschenrechner → E [Zeile 1903]
      „mit rationalen Zahlen (auch unter Verwendung eines“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 5 · Sachtext („das sind 60 %“) → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 6 · gemischt: erst zuordnen, dann rechnen → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 7 · Prüfungshöhe: Grundwert aus Rabattangabe, alter Preis gesucht … → F [Zeilen 1975–1976]; Eintrag: Prüfungshöhe
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
  - Veränderung (Einheit 5)
    - Sprosse 1 · „um oder auf“ (Vorstufe) → keine Stelle; Sprachliche Unterscheidung; der RLP nennt sie nicht.; Eintrag: Vorstufe
    - Sprosse 2 · Prozentwert berechnen und dazu oder weg (4×) → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 3 · Faktor 1,2 und 0,8 → E [Zeile 1916]
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · Veränderung in Prozent aus zwei Werten → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 5 · alter Wert aus neuem Wert (auf 80 %: neu : 0,8) → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 6 · Brutto/Netto → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 7 · Prozentpunkte → keine Stelle; Der Begriff Prozentpunkt kommt im RLP nicht vor.
    - Sprosse 8 · Steigung in Prozent → keine Stelle; Die Steigung in Prozent nennt der RLP weder unter Zahlen und Operationen noch unter Gleichungen und Funktionen.
    - Sprosse 9 · Prüfungshöhe: prozentuale Veränderung zweier Preise, auf den alten Wert bezogen … → F [Zeilen 1981–1982]; Eintrag: Prüfungshöhe
      „Zahlen (auch im Zusammenhang mit der Prozentrechnung)“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7, Mathematik: Prozentrechnung“ [Zeile 224]
  - Beleg [Zeile 225]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge bzw.“
- Spanne: nein  – Die höchste belegte Stufe ist F (Veränderung, Rabatt und Zinsen); keine Einheit und keine Sprosse liegt auf G oder H. Nach der Regel des Auftrags (G oder H gegen F oder darunter) ist die Spanne damit „nein“. Die Gegenprobe des Auftrags erwartete D/E für Grundwert, Prozentwert und Prozentsatz und F für Veränderung und Zinsen – das trifft zu, mit der Einschränkung, dass der Prozentwert-Grundfall auf E liegt und nur der Operatorbegriff auf D.
- Ermessen (4):
  - Einheiten 2, 3 und 4: der RLP kennt keine drei getrennten Aufgabenarten, sondern nur „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ (E). Alle drei Einheiten hängen deshalb an derselben Stelle; die Trennung ist didaktisch, nicht amtlich.
  - Sprosse „Prozentpunkte“ und „Steigung in Prozent“ (Einheit 5): keine Stelle – beide Begriffe kommen im Teil C nicht vor. Der Eintrag selbst führt „Steigung in Prozent berechnen“ als Typ ohne Hauptoriginal.
  - Sprosse „über das Ganze hinaus“ (Einheit 3): keine Stelle; Prozentsätze über hundert nennt der RLP nicht.
  - Sprosse „Rest zum Ganzen“ und „Anteilsformulierung“ (Einheit 1): keine Stelle; beides sind Sprachformen der Aufgabenstellung.

### pyramide-kegel-kugel – Stufe F (Pyramide) – G (Kegel, Kugel); die Begründungszeilen des LISUM-Blocks „Kegel und Kugel“ sind H, ohne GYM-Marke
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Größen und Messen F (S. 49): „Berechnen von Volumen und Oberflächeninhalt von Körpern (auch von geraden quadratischen Pyramiden, auch mithilfe von digitalen Mathematikwerkzeugen)““
  - Zeile 6 (Verortung): „G: „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und von Kugeln)““
  - Zeile 6 (Verortung): „H: „Berechnen des Volumens schiefer Prismen, Zylinder und Pyramiden unter Nutzung des Satzes von Cavalieri“.“
  - Zeile 6 (Verortung): „Netze nennt der RLP auf F–H nur für quadratische Pyramiden (F); Kegelnetz, Stümpfe und Kugelteile stehen nicht im RLP“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP D/E; P10 2024-OS-K4a]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP E; LS-AA Kl. 8 VII; P10 2026-FOR-K2a]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP E/F; LS-AA Kl. 9 V 2 „in Figuren und Körpern“; LISUM-PH „Nutzen des Satzes des Pythagoras für Berechnungen an Pyramiden“; P10 2018-OS-K6d, 2026-FOR-K2c]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP F]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP E „Umstellen von Formeln“; P10 2026-FOR-K2a, 2016-OS-K3c „Formel aus der Formelsammlung entnehmen“]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2016-OS-K3d]“
  - Zeile 34 (Merkkasten): „[RLP D „Erkennen, Benennen und Beschreiben gerader geometrischer Körper“; LISUM-PH Wiederholungsblock „Benennen der verschiedenen Körper“; LS-AA Kl. 10 I]“
  - Zeile 38 (Merkkasten): „[RLP D „Unterscheiden zwischen Oberflächeninhalt und Volumen“; P10 2026-FOR-K2b Dachziegel, 2015-OS-K6d Lack]“
  - Zeile 39 (Merkkasten): „[P10 2026-FOR-K2a, 2016-OS-K3c „Formel aus der Formelsammlung entnehmen“; RLP G „auch unter Nutzung von Formelsammlungen“]“
  - Zeile 49 (Merkkasten): „[RLP F]“
  - Zeile 58 (Merkkasten): „[RLP G]“
  - Zeile 67 (Merkkasten): „[RLP G]“
  - Zeile 80 (Typische Fehler): „[RLP F „sinnvolle Genauigkeit“; LISUM-PH „geeignetes Runden der Größen“; P10 2015-OS-K6c, 2026-FOR-K2b Zwischenergebnisse; FD]“
  - Zeile 85 (Für schwache Schüler): „[RLP F/G, LISUM-PH, MO]“
- Lerneinheiten:
  - 1. Pyramide – F/G
    - F [Zeile 2271]: „Berechnen von Volumen und Oberflächeninhalt von Körpern (auch von geraden“
      Block 2263–2276, Niveaustufe am Block: F (Z2271); Grundfall: gerade quadratische Pyramiden
    - F [Zeilen 2544–2546]: „Zeichnen von Netzen und Schrägbildern geometrischer Körper (auch von geraden“
      Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565); Netz und Schrägbild, Themenbereich Raum und Form
    - G [Zeile 2282]: „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); Sonderfall: beliebige gerade Pyramiden (auch rechteckige Grundfläche) erst auf G
  - 2. Kegel – G
    - G [Zeile 2282]: „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); Grundfall
    - G [Zeilen 2558–2560]: „Skizzieren von Schrägbildern (auch von geraden Kreiskegeln und -zylindern, Pyramiden,“
      Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565); Schrägbild, Themenbereich Raum und Form
      Ermessen: Das Kegelnetz (Kreisausschnitt mit dem Radius s) kommt im Teil C nicht vor; der Eintrag stellt das in der Verortung selbst fest.
  - 3. Kugel – G
    - G [Zeile 2282]: „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); Grundfall Volumen
    - G [Zeile 2284]: „Berechnen des Oberflächeninhalts von Körpern (auch gerade Pyramiden, gerade Kegel und“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); Oberfläche
      Ermessen: Die Halbkugel und die Teile einer Kugel nennt der RLP nicht; sie sind über die zusammengesetzten Körper (G) belegt.
- Sprossen je Verfahrenstyp:
  - Pyramide (Einheit 1)
    - Sprosse 1 · Höhe, Seitenhöhe oder Seitenkante benennen (Vorstufe) → F [Zeilen 2553–2556]; Eintrag: Vorstufe
      „geometrischer Flächen und Körper und deren Zusammensetzungen (auch gerade quadratische“ – Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565)
    - Sprosse 2 · V aus gegebener Grundfläche und Höhe mit ganzen Zahlen (4×) → F [Zeile 2271]
      „Berechnen von Volumen und Oberflächeninhalt von Körpern (auch von geraden“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 3 · quadratische Grundfläche aus a → F [Zeile 2271]
      „Berechnen von Volumen und Oberflächeninhalt von Körpern (auch von geraden“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 4 · rechteckige Grundfläche → G [Zeile 2282]
      „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 5 · Dezimalzahlen mit Runden → F [Zeile 2275]
      „kritisches Bewerten von Rechenergebnissen sowie Angabe von Rechenergebnissen mit sinnvoller“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 6 · Seitenhöhe aus h und halber Grundkante (Stützdreieck, Wurzel) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 7 · eine Seitenfläche als Dreieck → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Mantel als vier Dreiecke → F [Zeile 2271]
      „Berechnen von Volumen und Oberflächeninhalt von Körpern (auch von geraden“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 9 · Oberfläche → F [Zeile 2271]
      „Berechnen von Volumen und Oberflächeninhalt von Körpern (auch von geraden“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 10 · Seitenkante aus h und der halben Diagonale der Grundfläche (Stützdreieck) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 11 · Netz der quadratischen Pyramide mit Maßen vervollständigen → F [Zeilen 2544–2546]
      „Zeichnen von Netzen und Schrägbildern geometrischer Körper (auch von geraden“ – Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565)
    - Sprosse 12 · Schrägbild zeichnen und Höhe einzeichnen → F [Zeilen 2544–2546]
      „Zeichnen von Netzen und Schrägbildern geometrischer Körper (auch von geraden“ – Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565)
    - Sprosse 13 · h aus V und G (GYM, LISUM-PH „nur Gym“, kein P10-Original) → E [Zeile 2747]; Eintrag: GYM, LISUM „nur Gym“
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 14 · Sachaufgabe (Zeltdach: Stoffbedarf; Glaspyramide: Volumen und Glasfläche) → F [Zeile 2266]
      „Vertiefen der Kompetenzen zum Rechnen mit Größen im Zusammenhang mit berufsorientierten“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 15 · Prüfungshöhe: Modellpyramide, Höhe im Schrägbild und Seitenfläche nachweisen … → F [Zeile 2271]; Eintrag: Prüfungshöhe
      „Berechnen von Volumen und Oberflächeninhalt von Körpern (auch von geraden“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
  - Kegel (Einheit 2)
    - Sprosse 1 · Höhe, Mantellinie oder Radius benennen (Vorstufe) → G [Zeilen 2565–2568]; Eintrag: Vorstufe
      „Beschreiben von Eigenschaften geometrischer Flächen und Körper und deren“ – Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565)
    - Sprosse 2 · V aus r und h mit ganzen Zahlen (4×) → G [Zeile 2282]
      „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 3 · aus d → G [Zeile 2282]
      „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 4 · Dezimalzahlen mit Runden → F [Zeile 2275]
      „kritisches Bewerten von Rechenergebnissen sowie Angabe von Rechenergebnissen mit sinnvoller“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 5 · in Liter oder Milliliter → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 6 · Mantellinie aus r und h (Stützdreieck, Wurzel) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 7 · Kegelhöhe aus s und r → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Mantel aus r und s → G [Zeile 2284]
      „Berechnen des Oberflächeninhalts von Körpern (auch gerade Pyramiden, gerade Kegel und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 9 · Oberfläche → G [Zeile 2284]
      „Berechnen des Oberflächeninhalts von Körpern (auch gerade Pyramiden, gerade Kegel und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 10 · Schrägbild skizzieren → G [Zeilen 2558–2560]
      „Skizzieren von Schrägbildern (auch von geraden Kreiskegeln und -zylindern, Pyramiden,“ – Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565)
    - Sprosse 11 · Netz erkennen und beschriften: Grundkreis und Kreisausschnitt mit dem Radius s → keine Stelle; Das Kegelnetz steht nicht im Teil C; Netze werden auf F–H nur für quadratische Pyramiden genannt.
    - Sprosse 12 · h aus V und r → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 13 · Kegeldach auf einem Zylinder: Dachfläche, Ziegelkosten, Gesamthöhe → G [Zeile 2287]
      „Berechnen des Volumens und des Oberflächeninhaltes zusammengesetzter Körper mithilfe des“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 14 · Kegel gegen Zylinder mit gleichem r und h: ein Drittel, begründen → keine Stelle; Der Vergleich der Volumenformeln von Kegel und Zylinder steht nicht im Teil C.
    - Sprosse 15 · Prüfungshöhe: Aussage über dreifachen Radius rechnerisch prüfen (Niveau III) … → G [Zeile 2282]; Eintrag: Prüfungshöhe
      „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
  - Kugel (Einheit 3)
    - Sprosse 1 · Radius oder Durchmesser benennen (Vorstufe) → keine Stelle; Die Begriffe Radius und Durchmesser nennt der Teil C nicht.; Eintrag: Vorstufe
    - Sprosse 2 · V aus r mit ganzen Zahlen (4×) → G [Zeile 2282]
      „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 3 · aus d → G [Zeile 2282]
      „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 4 · Dezimalzahlen mit Runden → F [Zeile 2275]
      „kritisches Bewerten von Rechenergebnissen sowie Angabe von Rechenergebnissen mit sinnvoller“ – Block 2263–2276, Niveaustufe am Block: F (Z2271)
    - Sprosse 5 · in Liter oder Milliliter → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 6 · Oberfläche aus r → G [Zeile 2284]
      „Berechnen des Oberflächeninhalts von Körpern (auch gerade Pyramiden, gerade Kegel und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 7 · Kugel skizzieren (Kreis mit Äquatorellipse, Radius gestrichelt) → G [Zeilen 2565–2568]
      „Beschreiben von Eigenschaften geometrischer Flächen und Körper und deren“ – Block 2536–2571, Niveaustufe am Block: F (Z2548), G (Z2565)
    - Sprosse 8 · Halbkugel: Volumen, dann Oberfläche mit Schnittkreis → G [Zeile 2287]
      „Berechnen des Volumens und des Oberflächeninhaltes zusammengesetzter Körper mithilfe des“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 9 · Masse aus Volumen und Dichte → E [Zeile 2189]
      „Verwenden von Größenangaben in Rechnungen (auch Geschwindigkeiten, Dichten)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 10 · r aus O (Wurzel) → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 11 · Kugel in der Würfelschachtel: Kante gleich Durchmesser, Restvolumen → G [Zeile 2287]
      „Berechnen des Volumens und des Oberflächeninhaltes zusammengesetzter Körper mithilfe des“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 12 · Sachaufgabe (Silo mit Halbkugeldach; Eiskugel in der Tüte) → G [Zeile 2287]
      „Berechnen des Volumens und des Oberflächeninhaltes zusammengesetzter Körper mithilfe des“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 13 · doppelter Radius: achtfaches Volumen begründen → keine Stelle; Die Wirkung einer Maßänderung auf das Volumen nennt der Teil C nicht.
    - Sprosse 14 · Prüfungshöhe: Kugelvolumen mit der Formelsammlung, dann Volumen über die Dichte … → G [Zeile 2282]; Eintrag: Prüfungshöhe
      „Berechnen des Volumens von Körpern (auch von geraden Pyramiden, geraden Kreiskegeln und“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 9/10, Mathematik: Körper“ [Zeile 2101]
  - Beleg [Zeile 2102]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und die Menge“
  - Eine Reihe für alle Bildungsgänge mit dem Differenzierungshinweis (Zeile 2102). Die Reihe hat je zwei Blöcke auf Niveaustufe G (Zeilen 2106 und 2182) und auf Niveaustufe H (Zeilen 2160 und 2230); die H-Blöcke tragen keine GYM-Marke.
- Spanne: ja  – Die Pyramide liegt auf F, Kegel und Kugel auf G; einzelne Sprossen greifen auf E zurück (Pythagoras, Einheiten, Formelumstellen). Damit stehen Einheiten auf G und Einheiten und Sprossen auf F und darunter.
- Ermessen (5):
  - Sprosse „Netz erkennen und beschriften“ (Kegel): keine Stelle. Netze nennt der RLP auf F–H nur für quadratische Pyramiden; der Eintrag stellt das in der Verortung selbst fest.
  - Sprossen „Kegel gegen Zylinder: ein Drittel begründen“ und „doppelter Radius: achtfaches Volumen“: keine Stelle; Vergleiche von Formeln und die Wirkung von Maßänderungen stehen nicht im Teil C.
  - Die Stützdreieck-Sprossen (Seitenhöhe, Seitenkante, Mantellinie, Kegelhöhe) sind über die E-Zeile zum Satz des Pythagoras belegt, nicht über eine Zeile zu Pyramide oder Kegel.
  - Einheit 3: die Halbkugel nennt der RLP nicht; sie ist über die zusammengesetzten Körper (G) belegt.
  - Sprosse „rechteckige Grundfläche“ (Pyramide) liegt auf G, obwohl die übrige Kette auf F steht – der RLP kennt auf F nur gerade quadratische Pyramiden.

### pythagoras – Stufe E (Satz und Umkehrung; Konstruieren G, Begründen H; Wurzel F/G)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Größen und Messen E (S. 47, Rechnen mit Größen): „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen Dreiecken (auch an Körpern und mithilfe von digitalen Mathematikwerkzeugen)““
  - Zeile 6 (Verortung): „Befund: Satz und Umkehrung stehen auf E, also im Mindeststoff; der RLP nennt weder „Hypotenuse“ noch „Kathete“ noch die Formel“
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[RLP F „Beschreiben von Quadrat- und Kubikwurzel“; LS-AA Kl. 8 IV 1]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP F/G; P10 „Wurzel ziehen“ als Voraussetzung in 2024-OS-K6a, 2025-OS-K2a, 2026-FOR-K2c, 2026-FOR-K4a]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP D „Systematisieren von Dreiecken“; P10 2022-OS-K5a „nicht rechtwinklig“]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP E „Umstellen von Formeln“]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP D/E „sinnvolle Genauigkeit“; P10 Ergebnisse in m und cm]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP E „vier Quadranten“; P10 2019-OS-K2d „Koordinaten stehen nur im Bild“]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D/E; P10 2025-OS-K2a, 2023-OS-K2c]“
  - Zeile 56 (Merkkasten): „[RLP E]“
  - Zeile 64 (Merkkasten): „[RLP E]“
  - Zeile 79 (Typische Fehler): „[RLP E „sinnvolle Genauigkeit“; P10 2026-FOR-K2c Zwischenergebnis; FD]“
  - Zeile 83 (Für schwache Schüler): „[RLP E]“
  - Zeile 84 (Für schwache Schüler): „[RLP E, MO]“
- Lerneinheiten:
  - 1. Satz und Hypotenuse – E/F
    - E [Zeile 2203]: „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); Grundfall; die Stufe E macht den Satz zum Mindeststoff
    - F [Zeilen 1977–1979]: „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); die Wurzel als Operation steht eine Stufe später als der Satz
      Ermessen: Der RLP nennt weder „Hypotenuse“ noch „Kathete“ noch die Gleichung a² + b² = c²; der Eintrag stellt das in der Verortung selbst fest.
  - 2. Kathete und Umkehrung – E
    - E [Zeile 2205]: „Verwenden der Umkehrung des Satzes des Pythagoras zur Identifizierung von rechtwinkligen“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); die Umkehrung steht auf derselben Stufe wie der Satz
    - E [Zeile 2747]: „Lösen von Verhältnisgleichungen“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); das Umstellen nach einer Kathete, Themenbereich Gleichungen und Funktionen
  - 3. Pythagoras in Figuren und Körpern – E
    - E [Zeile 2204]: „(auch an Körpern und mithilfe von digitalen Mathematikwerkzeugen)“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); „auch an Körpern“ deckt die Stützdreiecke ab
    - E [Zeilen 2464–2467]: „Beschreiben von Lage- und Größenbeziehungen geometrischer Objekte (auch unter Nutzung des Satzes von“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Themenbereich Raum und Form
- Sprossen je Verfahrenstyp:
  - Hypotenuse (Einheit 1)
    - Sprosse 1 · Rechtwinkelmarke einkreisen, Hypotenuse mit H beschriften (Vorstufe) → keine Stelle; Die Begriffe Hypotenuse und Kathete nennt der Teil C nicht.; Eintrag: Vorstufe
    - Sprosse 2 · Hypotenuse aus zwei Katheten mit aufgehender Wurzel, Rechnung in drei Zeilen (4×) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · Dreieck in anderer Lage (rechter Winkel oben oder rechts) → keine Stelle; Die Lage des Dreiecks ist Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 4 · Wurzel geht nicht auf: Näherungswert auf eine Dezimale → G [Zeilen 1944–1945]
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 5 · Katheten als Dezimalzahlen → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · Einheit beim Ergebnis, Meter und Zentimeter vorher angleichen → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 7 · Gleichung zum Dreieck mit anderen Buchstaben aufstellen → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Satz in Worten unter drei Aussagen ankreuzen → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 9 · Gleichung unter vier Optionen ankreuzen (P10-Form) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 10 · Diagonale im Rechteck → E [Zeilen 2464–2467]
      „Beschreiben von Lage- und Größenbeziehungen geometrischer Objekte (auch unter Nutzung des Satzes von“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 11 · Sachaufgabe mit gegebener Skizze (Leiter, Abkürzung, Rampe) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 12 · Überstand zum Ergebnis addieren → keine Stelle; Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 13 · Prüfungshöhe: Hypotenuse in Meter mit Näherungswert; Rampenlänge … → E [Zeile 2203]; Eintrag: Prüfungshöhe
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Kathete (Einheit 2)
    - Sprosse 1 · „lange oder kurze Seite gesucht“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Gleichung nach der gesuchten Kathete umstellen, dann Kathete (4×) → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · Wurzel geht nicht auf: Zwischenergebnis, Näherungswert → G [Zeilen 1944–1945]
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 4 · Dezimalzahlen → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · Ergebnis prüfen: kürzer als die Hypotenuse → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · Kathetengleichung unter vier Optionen ankreuzen (P10-Form) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 7 · Nachweis mit vorgegebenem Ergebnis in Nachweis-Form → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Kathete im Sachzusammenhang mit Skizze (Höhenunterschied, Abstand) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 9 · Umkehrung: drei Seiten, längste als c, a² + b² mit c² vergleichen → E [Zeile 2205]
      „Verwenden der Umkehrung des Satzes des Pythagoras zur Identifizierung von rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 10 · rechten Winkel mit der Umkehrung begründen, Antwort als Text → H [Zeilen 2573–2575]
      „Begründen der Eigenschaften von geometrischen Objekten mithilfe von Symmetrie,“ – Block 2573–2581, Niveaustufe am Block: H (Z2577)
    - Sprosse 11 · Prüfungshöhe: Höhenunterschied der Seilbahn; Nachweis im stumpfwinkligen Dreieck … → E [Zeile 2203]; Eintrag: Prüfungshöhe
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Figuren und Körper (Einheit 3)
    - Sprosse 1 · Teildreieck nachfahren und Seiten benennen (Vorstufe) → keine Stelle; Das Herauslösen eines Teildreiecks nennt der RLP nicht als eigene Handlung.; Eintrag: Vorstufe
    - Sprosse 2 · Höhe im gleichschenkligen Dreieck aus Schenkel und halber Grundseite (4×) → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · Schenkel aus Höhe und halber Grundseite → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 4 · gleichschenkliges Trapez: Überstand als halbe Differenz, dann Schenkel oder Höhe → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · Parallelogramm: Höhe mit Fußpunkt auf der Verlängerung → keine Stelle; Der Fußpunkt außerhalb der Figur ist Aufgabenform; der RLP nennt ihn nicht.
    - Sprosse 6 · stumpfwinkliges Dreieck mit Höhe: Teilstrecke der Grundseite → keine Stelle; wie Sprosse 5: keine Stelle.
    - Sprosse 7 · Diagonale im Rechteck, Raute aus den halben Diagonalen → E [Zeilen 2464–2467]
      „Beschreiben von Lage- und Größenbeziehungen geometrischer Objekte (auch unter Nutzung des Satzes von“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 8 · Strecke aus Koordinaten mit positiven Koordinaten → E [Zeilen 2462–2463]
      „Zeichnen von Figuren im Koordinatensystem (vier“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 9 · mit negativen Koordinaten (Differenz über die Achse hinweg) → E [Zeilen 2462–2463]
      „Zeichnen von Figuren im Koordinatensystem (vier“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 10 · Seitenhöhe der Pyramide aus Höhe und halber Grundkante → E [Zeile 2204]
      „(auch an Körpern und mithilfe von digitalen Mathematikwerkzeugen)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 11 · Mantellinie des Kegels aus Radius und Höhe → E [Zeile 2204]
      „(auch an Körpern und mithilfe von digitalen Mathematikwerkzeugen)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 12 · Kegelhöhe aus Mantellinie und Radius → E [Zeile 2204]
      „(auch an Körpern und mithilfe von digitalen Mathematikwerkzeugen)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 13 · Rechenweg ohne Zahlen als Text beschreiben → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 14 · zusammengesetzt: Gesamthöhe des Turms; Stab schräg im Becher mit Überstand → E [Zeile 2204]
      „(auch an Körpern und mithilfe von digitalen Mathematikwerkzeugen)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 15 · Raumdiagonale im Quader in zwei Schritten (seit 11e Mindeststoff) → E [Zeile 2204]; Eintrag: Mindeststoff
      „(auch an Körpern und mithilfe von digitalen Mathematikwerkzeugen)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 16 · Prüfungshöhe: Rechenweg für die Mantellinie; Gesamthöhe des Turms; Stablänge … → E [Zeile 2204]; Eintrag: Prüfungshöhe
      „(auch an Körpern und mithilfe von digitalen Mathematikwerkzeugen)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Geometrie“ [Zeile 1120]
  - Beleg [Zeile 1320]: „nur Gym: Nachvollziehen des (formalen) Beweises“
  - Eine Reihe für alle Bildungsgänge mit dem Differenzierungshinweis (Zeile 1121). Der Satz des Pythagoras steht darin ab Zeile 1300; als „nur Gym“ ist allein das Nachvollziehen des formalen Beweises gekennzeichnet (Zeile 1320). Das Modellieren räumlicher Situationen einschließlich der Raumdiagonale eines Quaders steht ohne GYM-Marke (Zeile 1316).
- Spanne: ja  – Satz und Umkehrung liegen auf E, der Näherungswert der Wurzel auf G und das Begründen eines rechten Winkels auf H. Damit stehen Sprossen auf G und H und Einheiten auf E und F.
- Ermessen (4):
  - Einheit 1: der RLP nennt weder „Hypotenuse“ noch „Kathete“ noch die Gleichung; die ganze Einheit hängt an der einen E-Zeile zum Satz.
  - Sprossen „Dreieck in anderer Lage“, „Überstand addieren“, „Fußpunkt auf der Verlängerung“, „stumpfwinkliges Dreieck mit Höhe“: keine Stelle; alle vier sind Aufgabenformen.
  - Sprosse „rechten Winkel mit der Umkehrung begründen“ liegt auf H, während die Umkehrung selbst auf E steht – der RLP trennt das Verwenden (E) vom Begründen (H).
  - Sprossen zum Näherungswert liegen auf G (Zahlen und Operationen), nicht auf der Stufe des Satzes.

### quadratische-funktionen – Stufe G einschließlich Normalform x² + px + q und Streckfaktor (berichtigt 11g; H bleiben allgemeine Form, Linearfaktoren, quadratische Ergänzung, Rekonstruktion)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Zuordnungen und Funktionen G (S. 61): Bestimmen und Beschreiben von Merkmalen – „Definitionsbereich, Wertebereich, Form des Graphen, Schnittpunkte mit den Koordinatenachsen“, Einfluss der Parameter „(Streckung, Stauchung, Verschiebung)“, „Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt“ – für „quadratische Funktionen der Form y = a (x + d)² + e““
  - Zeile 6 (Verortung): „Befund, berichtigt 11g: Der RLP nennt auf G die Scheitelpunktform mit Streckfaktor y = a (x + d)² + e und das Lösen von Gleichungen der Form d = ax² + bx + c; die Normalform y = x² + px + q nennt er an keiner Stelle ausdrücklich, auf H steht die allgemeine Form y = a x² + b x + c.“
  - Zeile 6 (Verortung): „Wo der RLP schweigt, entscheidet die Planungshilfe, und die führt die Normalform in beiden Reihen unter Niveaustufe G. Auf H bleiben allein die allgemeine Form mit a, die Linearfaktoren, die quadratische Ergänzung als Lösungsverfahren und die Rekonstruktion.“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP E/F; P10 Fehlerquellen 2014-OS-K7a, 2018-OS-K5a, 2024-OS-K3c]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP E; P10 2021-OS-B1d Fehlerquelle „Koordinaten vertauschen“]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP F; LS-AA Kl. 9 I 1 Wiederholung]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP G „auch unter Nutzung der binomischen Formeln“; LS-AA Kl. 8 II 4]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP F/G; LS-AA Kl. 8 IV 1]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP G „Lösen von Gleichungen (auch quadratische …)“; LS-AA Kl. 9 II 3 und II 5]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP E]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP G S. 61 Schnittpunkte von Funktionsgraphen]“
  - Zeile 47 (Merkkasten): „[RLP G]“
  - Zeile 74 (Typische Fehler): „[RLP G]“
  - Zeile 94 (Für schwache Schüler): „[RLP G, MO]“
- Lerneinheiten:
  - 1. Normalparabel und Streckfaktor – G
    - G [Zeilen 2910–2912]: „− quadratische Funktionen der Form y = a (x + d)² + e“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); die einzige Formangabe des RLP für quadratische Funktionen auf G – sie enthält den Streckfaktor a
    - G [Zeilen 2904–2906]: „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); Öffnung, Streckung und Stauchung stehen ausdrücklich auf G
  - 2. Scheitelpunktform – G
    - G [Zeilen 2910–2912]: „− quadratische Funktionen der Form y = a (x + d)² + e“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); der RLP schreibt (x + d)², P10 und typen.csv (x − d)²
    - G [Zeilen 2904–2906]: „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); Verschiebung und Scheitelpunkt
  - 3. Normalform – G/H
    - G [Zeilen 2839–2840]: „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); das Ausmultiplizieren der Scheitelpunktform mit der binomischen Formel; die Normalform y = x² + px + q nennt der RLP nirgends
    - H [Zeilen 2864–2865]: „− auch Umformen quadratischer Terme in vollständige Quadrate mithilfe quadratischer“
      Block 2860–2880, Niveaustufe am Block: H (Z2875); quadratische Ergänzung; im Eintrag als Vorrat (H)
      Ermessen: Die Normalform y = x² + px + q steht an keiner Stelle des Teils C. Der Eintrag ordnet sie nach der Planungshilfe der Stufe G zu; diese Datei folgt dem und belegt die Einheit über das Umformen von Termen (G).
  - 4. Nullstellen und Schnittpunkte berechnen – G
    - G [Zeilen 2842–2843]: „Lösen von Gleichungen (auch quadratische Gleichungen“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); der RLP nennt die Form d = ax² + bx + c auf G
    - G [Zeilen 2914–2916]: „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); Schnittpunkte von Funktionsgraphen
- Sprossen je Verfahrenstyp:
  - Normalparabel und Streckfaktor (Einheit 1)
    - Sprosse 1 · Gerade oder Parabel ankreuzen (Vorstufe) → G [Zeilen 2910–2912]; Eintrag: Vorstufe
      „− quadratische Funktionen der Form y = a (x + d)² + e“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · Wertetabelle zu x² ausfüllen, auch negative x (4×) → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · Punkte eintragen und Parabel als Bogen zeichnen → G [Zeilen 2894–2896]
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Eigenschaften nennen (Scheitel, Symmetrieachse, Öffnung, kleinster Wert) → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · Funktionswert und Punktprobe mit negativem x → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · Wertetabelle zu a·x² ausfüllen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · Öffnung und Breite an a erkennen (nach unten, schmaler, breiter) → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · Wertetabelle zu a·x² unter mehreren zuordnen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · Parabel zu a·x² zeichnen (ohne Original; Zielmarke nach RLP und LISUM-PH) → G [Zeilen 2894–2896]; Eintrag: Zielmarke
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 10 · Parabelgleichung zu einem Graphen zuordnen (Öffnung, Startwert) → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 11 · Prüfungshöhe: Wertetabelle zu y = 3x² ankreuzen; Gleichung zum Fallschirmsprung … → G [Zeilen 2909–2911]; Eintrag: Prüfungshöhe
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Scheitelpunktform (Einheit 2)
    - Sprosse 1 · Scheitel in der Gleichung markieren und Vorzeichen umdrehen (Vorstufe) → G [Zeilen 2910–2912]; Eintrag: Vorstufe
      „− quadratische Funktionen der Form y = a (x + d)² + e“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · Scheitel aus der Scheitelpunktform ablesen, d und e positiv (4×) → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · d oder e negativ → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Scheitel am Graphen ablesen und als S(d | e) schreiben → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · Parabel aus der Gleichung skizzieren (Scheitel setzen, Punkte wie bei der Normalparabel) → G [Zeilen 2894–2896]
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · Gleichung aus dem Scheitel aufstellen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · Gleichung aus dem Graphen aufstellen (Scheitel ablesen, Öffnung prüfen) → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · verschieben, erst nach oben/unten, dann rechts/links, dann beides → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · an der x-Achse spiegeln → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 10 · an der y-Achse spiegeln → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 11 · Parabel zu Eigenschaften angeben (Scheitel auf einer Achse, keine Nullstellen) → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 12 · Lage zweier Parabeln begründen → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 13 · Merkmale einer gestreckten oder gestauchten Parabel bestimmen (ohne Original; Zielmarke) → G [Zeilen 2904–2906]; Eintrag: Zielmarke
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 14 · Prüfungshöhe: verschieben und spiegeln, Gleichung angeben … → G [Zeilen 2904–2906]; Eintrag: Prüfungshöhe
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Normalform (Einheit 3)
    - Sprosse 1 · Scheitelpunktform oder Normalform ankreuzen (Vorstufe) → keine Stelle; Die Normalform y = x² + px + q nennt der Teil C an keiner Stelle.; Eintrag: Vorstufe
    - Sprosse 2 · y-Achsenabschnitt q ablesen (4×) → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · Funktionswert und Punktprobe in der Normalform mit negativem x → keine Stelle; keine Stelle: der RLP nennt für quadratische Funktionen weder Funktionswert noch Punktprobe.
    - Sprosse 4 · Scheitelpunktform ausmultiplizieren, d und e positiv → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 5 · d negativ (Plus in der Klammer) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 6 · Normalform als Behauptung nachweisen → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 7 · Scheitel einer Normalform-Parabel am Graphen ablesen → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · Scheitelpunktform aus dem abgelesenen Scheitel aufstellen, Probe mit q → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · Aussagen zur Parabel als wahr oder falsch beurteilen → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 10 · Prüfungshöhe: Scheitel und Scheitelpunktform zur gegebenen Normalform … → G [Zeilen 2839–2840]; Eintrag: Prüfungshöhe
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
  - Nullstellen und Schnittpunkte (Einheit 4)
    - Sprosse 1 · gleichzusetzende Terme markieren (Vorstufe) → G [Zeilen 2842–2843]; Eintrag: Vorstufe
      „Lösen von Gleichungen (auch quadratische Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 2 · Nullstellen aus der Scheitelpunktform durch Wurzelziehen, ganzzahlig (4×) → G [Zeilen 2842–2843]
      „Lösen von Gleichungen (auch quadratische Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 3 · Zahl der Nullstellen am Scheitel begründen → G [Zeilen 2852–2853]
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 4 · Nullstellen aus der Normalform mit der p-q-Formel, ganzzahlig → G [Zeilen 2842–2843]
      „Lösen von Gleichungen (auch quadratische Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 5 · Wurzel bleibt stehen, Näherungswert → G [Zeilen 1944–1945]
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 6 · vorher durch den Streckfaktor teilen → G [Zeilen 2842–2843]
      „Lösen von Gleichungen (auch quadratische Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 7 · Argument zu gegebenem Funktionswert → G [Zeilen 2842–2843]
      „Lösen von Gleichungen (auch quadratische Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 8 · Schnittpunkte Gerade und Parabel in Normalform, ganzzahlig → G [Zeilen 2914–2916]
      „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · Parabel in Scheitelpunktform (Klammer auflösen) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 10 · y-Werte über die Gerade und Punkte angeben → G [Zeilen 2914–2916]
      „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 11 · Punktprobe als Schnittpunkt-Nachweis in beiden Funktionen → keine Stelle; Die Punktprobe nennt der RLP für quadratische Funktionen nicht.
    - Sprosse 12 · Gerade ohne gemeinsamen Punkt angeben (waagerecht jenseits des Scheitels) → G [Zeilen 2852–2853]
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 13 · Schnittpunkte zweier Parabeln berechnen (ohne Original; Zielmarke, EBR/FOR-Reihe) → G [Zeilen 2914–2916]; Eintrag: Zielmarke
      „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 14 · Prüfungshöhe: Schnittpunkte Gerade–Parabel; Nullstellen mit Wurzel; x-Werte zu y … → G [Zeilen 2914–2916]; Eintrag: Prüfungshöhe
      „Nutzen von Lösungsprinzipien für lineare Gleichungssysteme zur Berechnung von“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
- LISUM: getrennte Reihen EBR/FOR und GYM; Reihen: „Jahrgangsstufe 9 (EBR und FOR), Mathematik: Quadratische Funktionen und Gleichungen“ [Zeile 1773]; „Jahrgangsstufe 9 (Gymnasium), Mathematik: Quadratische Funktionen und Gleichungen“ [Zeile 1869]
  - Beleg [Zeile 1870]: „Hinweis: Eine Differenzierung erfolgt über Tiefgründigkeit der Bearbeitung“
  - Die Planungshilfe führt zwei getrennte Reihen: eine für EBR und FOR (Zeilen 1773–1868) und eine für das Gymnasium (Zeilen 1869–2006). Beide beginnen mit einem Block Niveaustufe G (Zeilen 1778 und 1874); nur die Gymnasialreihe hat zusätzlich einen Block Niveaustufe H (Zeile 1963), in dem die Effektivität verschiedener Lösungsverfahren verglichen wird. Der Hinweis der EBR/FOR-Reihe spricht von der Differenzierung zwischen den Schulformen (Zeile 1774), der der Gymnasialreihe von der Differenzierung innerhalb der Lerngruppe (Zeile 1870).
- Spanne: nein  – Alle vier Einheiten liegen auf G; die quadratische Ergänzung als Verfahren (Einheit 3) findet ihre Stelle auf H. Auf F oder darunter liegt in diesem Eintrag nichts, deshalb ergibt die Regel aus Schritt 2e „nein“. Der Auftrag erwartet in der Gegenprobe „ja“ – der Widerspruch steht unter Ermessen.
- Ermessen (4):
  - **Gegenprobe des Auftrags:** Die Einheiten mit Scheitelpunktform (1 und 2) liegen auf G – das trifft zu. Sprossen zu Linearfaktoren und zur quadratischen Ergänzung gibt es in diesem Eintrag jedoch nicht: beide stehen nur in „Typen je Lerneinheit“ (Einheit 3) als Vorrat mit der Marke H, nicht in den Sprossenketten. Die H-Belege dieser Datei hängen deshalb an der Einheit 3, nicht an einer Sprosse.
  - **Spanne nach der Regel des Auftrags:** Die Regel lautet „mindestens eine Einheit oder Sprosse auf G oder H und mindestens eine auf F oder darunter“. In diesem Eintrag liegt nichts auf F oder darunter – alles liegt auf G, nur die quadratische Ergänzung auf H. Streng nach der Regel ist die Spanne damit „nein“; nach der Sache (G gegen H) wäre sie „ja“, und so erwartet es die Gegenprobe des Auftrags. Diese Datei folgt der Regel und schreibt „nein“; die Abweichung ist ein Befund, keine Änderung der Datei.
  - Einheit 3 im Ganzen: die Normalform y = x² + px + q steht an keiner Stelle des Teils C. Der Eintrag ordnet sie nach der Planungshilfe G zu (berichtigt 11g); diese Datei folgt dem.
  - Sprossen „Funktionswert und Punktprobe“ (Einheit 3, Sprosse 3) und „Punktprobe als Schnittpunkt-Nachweis“ (Einheit 4, Sprosse 11): keine Stelle; der RLP nennt für quadratische Funktionen weder Funktionswert noch Punktprobe.

### quadratische-gleichungen – Stufe G; GYM nach LISUM-PH (nur Gymnasialreihe, ohne P10-Original) sind das Ausklammern von x, die Form a·x² + b = c und der Begriff Diskriminante; quadratische Ergänzung, höhere Grade und Wurzelgleichungen H (Stufung 11h)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Terme und Gleichungen G (S. 60): „Lösen von Gleichungen (auch quadratische Gleichungen der Form d = ax² + bx + c) durch systematisches Probieren, rechnerisch und grafisch“; „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen““
  - Zeile 6 (Verortung): „Befund: Der RLP nennt kein Lösungsverfahren beim Namen – weder Wurzelziehen noch Nullprodukt noch p-q-Formel; „rechnerisch“ auf G deckt alle drei.“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP E/F; P10 Fehlerquelle 2025-OS-B1h „Vorzeichen beim Einsetzen negativer Werte“]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP F/G; LS-AA Kl. 8 IV 1–2; P10 2025-OS-K5c Ergebnis mit Wurzel und Näherungswert]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP E/F; LS-AA Kl. 7 IV 5]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP E „Prüfen einer Lösung durch Einsetzen“; P10 2018-OS-B1c, 2022-OS-B1c, 2025-OS-B1h]“
  - Zeile 32 (Voraussetzungen (Blatt 0)): „[RLP F/G „auch unter Nutzung der binomischen Formeln“; LS-AA Kl. 8 II 3–4; P10 2022-OS-K3c, 2017-OS-K5d Fehlerquelle „Mittelglied fehlt“]“
  - Zeile 33 (Voraussetzungen (Blatt 0)): „[RLP E]“
  - Zeile 34 (Voraussetzungen (Blatt 0)): „[RLP G; P10 2021-OS-K7c Stichwort „Scheitelpunktform“]“
  - Zeile 36 (Merkkasten): „[LS-AA Kl. 9 II 1; RLP G]“
  - Zeile 77 (Typische Fehler): „[RLP G]“
  - Zeile 100 (Für schwache Schüler): „[RLP G, MO]“
- Lerneinheiten:
  - 1. Wurzelziehen und Lösbarkeit – F/G
    - G [Zeilen 2842–2843]: „Lösen von Gleichungen (auch quadratische Gleichungen“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); Grundfall; der RLP nennt die Form d = ax² + bx + c
    - G [Zeilen 2852–2853]: „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); zwei, eine oder keine Lösung
    - F [Zeilen 1977–1979]: „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); das Wurzelziehen als Operation steht eine Stufe tiefer
  - 2. Satz vom Nullprodukt – G
    - G [Zeilen 2845–2846]: „durch systematisches Probieren, rechnerisch und grafisch“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); „rechnerisch“ deckt das Verfahren; den Satz vom Nullprodukt nennt der RLP nicht
      Ermessen: Der RLP nennt kein Lösungsverfahren beim Namen. Der Satz vom Nullprodukt ist über „rechnerisch“ (G) zugeordnet – so auch der Befund des Eintrags.
  - 3. Normalform und p-q-Formel – G
    - G [Zeilen 2845–2846]: „durch systematisches Probieren, rechnerisch und grafisch“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); die p-q-Formel nennt der RLP nicht beim Namen
    - G [Zeilen 2852–2853]: „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); die Zahl der Lösungen am Wert unter der Wurzel
  - 4. Sachaufgaben – G
    - G [Zeilen 2839–2840]: „Übersetzungen zwischen verschiedenen Darstellungen (symbolisch, grafisch,“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); „auch für quadratische Zusammenhänge“ steht in derselben Zeile
- Sprossen je Verfahrenstyp:
  - Wurzelziehen und Lösbarkeit (Einheit 1)
    - Sprosse 1 · rechte Seite ansehen und „zwei, eine, keine“ ankreuzen (Vorstufe) → G [Zeilen 2852–2853]; Eintrag: Vorstufe
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 2 · x² = c mit Quadratzahl, beide Lösungen (4×) → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 3 · Einstieg im Sachzusammenhang: Seitenlänge eines Quadrats aus seinem Flächeninhalt → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 4 · c keine Quadratzahl: Wurzel stehen lassen, Näherungswert → G [Zeilen 1944–1945]
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 5 · c negativ: keine Lösung mit Begründung → G [Zeilen 2852–2853]
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 6 · x² freistellen, wenn eine Vorzahl vor x² steht oder eine Zahl dazukommt → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · dasselbe an einer umgestellten Formel: Radius aus Volumen und Höhe → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 8 · a·x² + b = c mit Fallbetrachtung (GYM, LISUM-PH Gymnasium Zeile 1950) → G [Zeilen 2842–2843]; Eintrag: GYM
      „Lösen von Gleichungen (auch quadratische Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 9 · quadrierte Klammer (x − d)² = c rückwärts rechnen, d positiv → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 10 · d negativ (Plus in der Klammer) → F [Zeilen 1977–1979]
      „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 11 · (x − d)² = null: genau eine Lösung (amtlich nur Gymnasialreihe, Marke überschrieben) → G [Zeilen 2852–2853]; Eintrag: GYM, Marke überschrieben
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 12 · Lösung durch Einsetzen prüfen, negativ → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 13 · Zahl der Lösungen am Graphen ablesen → G [Zeilen 2845–2846]
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 14 · Gleichung ohne Lösung selbst angeben → G [Zeilen 2852–2853]
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 15 · Prüfungshöhe: Aussagen zu (x + a)² = b beurteilen und Gleichung ohne Lösung angeben … → G [Zeilen 2852–2853]; Eintrag: Prüfungshöhe
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
  - Nullprodukt (Einheit 2)
    - Sprosse 1 · „Steht rechts eine Null?“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; den Satz vom Nullprodukt nennt der RLP nicht.; Eintrag: Vorstufe
    - Sprosse 2 · Produktform mit zwei Klammern, jeden Faktor null setzen (4×) → G [Zeilen 2845–2846]
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 3 · gemischte Vorzeichen → G [Zeilen 2845–2846]
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 4 · x·(x + a) = null → G [Zeilen 2845–2846]
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 5 · gleiche Faktoren: eine Lösung → G [Zeilen 2852–2853]
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 6 · Lösung durch Einsetzen bei Produktform prüfen, negativ → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · x² + px = null mit x ausklammern, beide Lösungen (GYM) → G [Zeilen 2839–2840]; Eintrag: GYM
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 8 · Minus vor dem x-Glied (GYM) → G [Zeilen 2839–2840]; Eintrag: GYM
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 9 · Vorzahl vor x² (GYM) → G [Zeilen 2839–2840]; Eintrag: GYM
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 10 · Produkt gleich einer Zahl ungleich null: ausmultiplizieren und ordnen → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 11 · Prüfungshöhe: unter vier Werten den ankreuzen, der x·(x + a) = c erfüllt … → G [Zeilen 2845–2846]; Eintrag: Prüfungshöhe
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
  - p-q-Formel (Einheit 3; ohne Basismarke – in dreizehn Jahrgängen kein Original auf Niveau I und keines ohne Stern, die Einstiegsaufgaben des Themas liegen in Einheit 1 und 2)
    - Sprosse 1 · Form erkennen, p und q mit Vorzeichen einkreisen (Vorstufe) → keine Stelle; Die Normalform x² + px + q und die p-q-Formel nennt der Teil C nicht.; Eintrag: Vorstufe
    - Sprosse 2 · Normalform mit p und q positiv, Lösungen ganzzahlig (4×) → G [Zeilen 2845–2846]
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 3 · p oder q negativ → G [Zeilen 2845–2846]
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 4 · Gleichung ordnen: alles auf eine Seite, Reihenfolge x², x, Zahl → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 5 · Normieren: durch die Vorzahl von x² teilen (amtlich nur Gymnasialreihe, Marke überschrieben) → G [Zeilen 2839–2840]; Eintrag: GYM, Marke überschrieben
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 6 · p ungerade: Dezimalzahl unter der Wurzel → G [Zeilen 2845–2846]
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 7 · Wert unter der Wurzel null: eine Lösung → G [Zeilen 2852–2853]
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 8 · Wert unter der Wurzel negativ: keine Lösung → G [Zeilen 2852–2853]
      „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 9 · denselben Wert „Diskriminante“ nennen (GYM, LISUM-PH Gymnasium Zeile 1965) → keine Stelle; Das Wort „Diskriminante“ kommt im Teil C nicht vor; es steht nur in der Gymnasialreihe der Planungshilfe.; Eintrag: GYM
    - Sprosse 10 · Lösungen mit Wurzel, Näherungswert auf zwei Stellen → G [Zeilen 1944–1945]
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 11 · Probe mit einer Lösung → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 12 · Klammer oder Produkt zuerst auflösen (binomische Formel), dann ordnen → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 13 · Lösungsweg wählen: Wurzelziehen, Nullprodukt oder Formel → G [Zeile 2849]
      „Vergleichen der Effektivität verschiedener“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 14 · Prüfungshöhe: Nullstellen nach dem Normieren; irrationales Ergebnis; x-Werte zu y … → G [Zeilen 2845–2846]; Eintrag: Prüfungshöhe
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
  - Sachaufgaben (Einheit 4)
    - Sprosse 1 · passende Lösung zur Frage ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Zahlenrätsel mit dem Quadrat einer Zahl, Gleichung vorgegeben (4×) → G [Zeilen 2839–2840]
      „Übersetzungen zwischen verschiedenen Darstellungen (symbolisch, grafisch,“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 3 · Zahlenrätsel selbst aufstellen → G [Zeilen 2839–2840]
      „Übersetzungen zwischen verschiedenen Darstellungen (symbolisch, grafisch,“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 4 · Produkt einer Zahl mit ihrem Nachfolger (Nullprodukt oder Formel) → G [Zeilen 2845–2846]
      „durch systematisches Probieren, rechnerisch und grafisch“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 5 · Rechteck mit Seitenbeziehung und Fläche → G [Zeilen 2839–2840]
      „Übersetzungen zwischen verschiedenen Darstellungen (symbolisch, grafisch,“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 6 · negative Lösung im Kontext ausschließen und begründen → keine Stelle; Das Ausschließen einer Lösung im Sachkontext nennt der RLP nicht.
    - Sprosse 7 · Antwortsatz mit Einheit → keine Stelle; Darstellungsform der Lösung; keine eigene Stelle.
    - Sprosse 8 · Probe im Sachzusammenhang → E [Zeile 2750]
      „Prüfen einer Lösung (auch durch Einsetzen in“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 9 · Prüfungshöhe: Rechteck-Aufgabe mit Klammer, Ordnen, Formel (kein P10-Original) … → G [Zeilen 2839–2840]; Eintrag: Prüfungshöhe, Zielmarke
      „Übersetzungen zwischen verschiedenen Darstellungen (symbolisch, grafisch,“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
- LISUM: getrennte Reihen EBR/FOR und GYM; Reihen: „Jahrgangsstufe 9 (EBR und FOR), Mathematik: Quadratische Funktionen und Gleichungen“ [Zeile 1773]; „Jahrgangsstufe 9 (Gymnasium), Mathematik: Quadratische Funktionen und Gleichungen“ [Zeile 1869]
  - Beleg [Zeile 1870]: „Hinweis: Eine Differenzierung erfolgt über Tiefgründigkeit der Bearbeitung“
  - Zwei getrennte Reihen (EBR/FOR ab Zeile 1773, Gymnasium ab Zeile 1869). Nur die Gymnasialreihe hat einen Block Niveaustufe H (Zeile 1963) mit dem Vergleich der Lösungsverfahren; der Eintrag stützt darauf seine GYM-Marken für das Ausklammern von x, die Form a·x² + b = c, das Normieren und den Begriff Diskriminante.
- Spanne: ja  – Die Einheiten liegen auf G; einzelne Sprossen greifen auf F (Wurzelziehen) und E (Umstellen, Probe) zurück. Damit stehen Einheiten auf G und Sprossen auf F und darunter.
- Ermessen (5):
  - **Kein Verfahren beim Namen:** Der RLP nennt weder Wurzelziehen noch Satz vom Nullprodukt noch p-q-Formel. Alle drei Einheiten hängen an der einen G-Zeile „durch systematisches Probieren, rechnerisch und grafisch“. Der Eintrag stellt das selbst fest.
  - Sprosse „Diskriminante“ (Einheit 3): keine Stelle; das Wort kommt im Teil C nicht vor, nur in der Gymnasialreihe der Planungshilfe.
  - Vorstufe der Einheit 3: keine Stelle; die Normalform x² + px + q wird im Teil C nicht genannt (dieselbe Lücke wie bei quadratische-funktionen.md).
  - Sprossen „negative Lösung im Kontext ausschließen“ und „Antwortsatz mit Einheit“: keine Stelle; beides sind Darstellungsformen der Lösung.
  - Die GYM-Marken des Eintrags (Ausklammern von x, a·x² + b = c, Normieren, Diskriminante) stammen aus der Gymnasialreihe der Planungshilfe, nicht aus dem RLP; der RLP stuft alle vier auf G ein bzw. nennt sie gar nicht.

### rationale-zahlen – Stufe E
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] E: „Identifizieren von negativen Zahlen (negative ganze Zahlen und negative gebrochene Zahlen) und Verknüpfen mit Alltagssituationen““
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D, MSK D2A]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 30 (Merkkasten): „[RLP E; LS-AA Kl. 7 I 3]“
  - Zeile 31 (Merkkasten): „[RLP E „Änderung eines Zustandes“]“
  - Zeile 34 (Merkkasten): „[RLP E]“
  - Zeile 41 (Merkkasten): „[RLP E]“
  - Zeile 49 (Merkkasten): „[RLP E]“
  - Zeile 64 (Typische Fehler): „[RLP E]“
  - Zeile 76 (Für schwache Schüler): „[RLP E; FD]“
  - Zeile 81 (Für schwache Schüler): „[RLP E, MO]“
- Lerneinheiten:
  - 1. Negative Zahlen kennen und ordnen – E
    - E [Zeilen 1841–1842]: „Identifizieren von negativen Zahlen (negative ganze Zahlen“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); Grundfall
    - E [Zeilen 1848–1849]: „Darstellen von rationalen Zahlen mit Ziffern und an der“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); Zahlengerade
    - E [Zeilen 1838–1840]: „Vergleichen und Ordnen von − Prozentangaben − rationalen Zahlen“
      Block 1838–1860, Niveaustufe am Block: E (Z1850); Vergleichen und Ordnen; im Strom stehen Prozentangaben und rationale Zahlen als Spiegelstriche untereinander
  - 2. Addieren und Subtrahieren – E
    - E [Zeilen 1900–1901]: „Addition und Subtraktion als Änderung eines Zustandes“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Grundvorstellung
    - E [Zeile 1904]: „Subtraktion als Unterschied“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); zweite Grundvorstellung der Einheit
  - 3. Multiplizieren und Dividieren – E/F
    - E [Zeilen 1908–1909]: „als Inversion (Spiegelung am Nullpunkt)“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Vorzeichenregel der Multiplikation
    - E [Zeilen 1910–1911]: „Division als Multiplikation mit dem Kehrwert der rationalen Zahl“
      Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - F [Zeilen 1974–1975]: „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); Sonderfall: Potenzen mit negativer Basis stehen erst auf F
  - 4. Terme und Sachaufgaben – E
    - E [Zeilen 1901–1902]: „Prüfen und Übertragen der bekannten operativen Strategien, Gesetze und Verfahren auf das Rechnen“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Rechengesetze und Rechenvorteile
    - E [Zeilen 1902–1903]: „Addition als Zusammenfassung von mehreren Änderungen“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Sachaufgaben mit mehreren Buchungen
- Sprossen je Verfahrenstyp:
  - Ordnen (Einheit 1)
    - Sprosse 1 · Zahlengerade beschriften (Vorstufe) → E [Zeilen 1848–1849]; Eintrag: Vorstufe
      „Darstellen von rationalen Zahlen mit Ziffern und an der“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 2 · ganze Zahlen eintragen (4×) → E [Zeilen 1848–1849]
      „Darstellen von rationalen Zahlen mit Ziffern und an der“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 3 · Gegenzahl und Betrag → E [Zeilen 1841–1842]
      „Verwenden von Betrag und Gegenzahl“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 4 · zwei negative vergleichen → E [Zeilen 1838–1840]
      „Vergleichen und Ordnen von − Prozentangaben − rationalen Zahlen“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 5 · Dezimalzahlen und Brüche eintragen → E [Zeilen 1848–1849]
      „Darstellen von rationalen Zahlen mit Ziffern und an der“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 6 · gemischt ordnen → E [Zeilen 1838–1840]
      „Vergleichen und Ordnen von − Prozentangaben − rationalen Zahlen“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 7 · Prüfungshöhe: eine Zahl angeben, die eine Bedingung mit negativer Grenze erfüllt … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Addieren/Subtrahieren (Einheit 2)
    - Sprosse 1 · Pfeil an der Zahlengeraden (Vorstufe) → E [Zeilen 1900–1901]; Eintrag: Vorstufe
      „Addition und Subtraktion als Änderung eines Zustandes“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 2 · positive Zahl dazu oder weg, Start negativ (4×) → E [Zeilen 1900–1901]
      „Addition und Subtraktion als Änderung eines Zustandes“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 3 · negative Zahl addieren mit Klammer → E [Zeilen 1902–1903]
      „Addition als Zusammenfassung von mehreren Änderungen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · negative Zahl subtrahieren → E [Zeile 1906]
      „Subtraktion als Addition der Gegenzahl“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 5 · Zeichen zusammenfassen gemischt (4×) → E [Zeilen 1858–1860]
      „Unterscheiden von Vorzeichen bei rationalen Zahlen und Rechenzeichen“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 6 · Unterschied zweier Zahlen → E [Zeile 1904]
      „Subtraktion als Unterschied“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 7 · Dezimalzahlen → E [Zeilen 1901–1902]
      „Prüfen und Übertragen der bekannten operativen Strategien, Gesetze und Verfahren auf das Rechnen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 8 · mehrere Summanden → E [Zeilen 1902–1903]
      „Addition als Zusammenfassung von mehreren Änderungen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 9 · Prüfungshöhe: Rechnung in der Klammer eines Termwert-Originals … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Multiplizieren/Dividieren (Einheit 3)
    - Sprosse 1 · Vorzeichen ankreuzen ohne Rechnung (Vorstufe) → keine Stelle; Vorstufe; der RLP nennt das Bestimmen des Vorzeichens ohne Rechnung nicht.; Eintrag: Vorstufe
    - Sprosse 2 · plus mal minus (4×) → E [Zeilen 1908–1909]
      „als Inversion (Spiegelung am Nullpunkt)“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 3 · minus mal minus → E [Zeilen 1908–1909]
      „als Inversion (Spiegelung am Nullpunkt)“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · dividieren → E [Zeilen 1910–1911]
      „Division als Multiplikation mit dem Kehrwert der rationalen Zahl“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 5 · drei Faktoren → E [Zeilen 1901–1902]
      „Prüfen und Übertragen der bekannten operativen Strategien, Gesetze und Verfahren auf das Rechnen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 6 · Potenz mit Klammer und ohne → F [Zeilen 1974–1975]
      „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 7 · Punkt vor Strich → E [Zeilen 1901–1902]
      „Prüfen und Übertragen der bekannten operativen Strategien, Gesetze und Verfahren auf das Rechnen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 8 · Prüfungshöhe: Termwert eines Bruchterms mit zwei negativen Einsetzungen ohne Taschenrechner … → E [Zeile 1905]; Eintrag: Prüfungshöhe
      „Durchführen von einfachen Rechnungen und“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
  - Terme und Sachaufgaben (Einheit 4)
    - Sprosse 1 · Startwert und Änderung markieren (Vorstufe) → E [Zeilen 1900–1901]; Eintrag: Vorstufe
      „Addition und Subtraktion als Änderung eines Zustandes“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 2 · Kontostand nach einer Buchung (4×) → E [Zeilen 1900–1901]
      „Addition und Subtraktion als Änderung eines Zustandes“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 3 · mehrere Buchungen → E [Zeilen 1902–1903]
      „Addition als Zusammenfassung von mehreren Änderungen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · Unterschied zweier Zustände (Temperatur, Höhe) → E [Zeile 1904]
      „Subtraktion als Unterschied“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 5 · Minusklammer → keine Stelle; Das Auflösen einer Klammer mit vorangehendem Minus nennt der RLP nicht eigens; das Distributivgesetz steht erst unter Terme und Gleichungen (F).
    - Sprosse 6 · Termwert mit Klammer → E [Zeilen 1901–1902]
      „Prüfen und Übertragen der bekannten operativen Strategien, Gesetze und Verfahren auf das Rechnen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 7 · Prüfungshöhe: günstigste Kombination aus einer Preisliste ermitteln und abwägen … → keine Stelle; P10-Aufgabenform (Niveau III), kein RLP-Inhalt.; Eintrag: Prüfungshöhe, Vorrat
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7, Mathematik: Rationale Zahlen“ [Zeile 477]
  - Beleg [Zeile 478]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: nein  – Alle Einheiten und fast alle Sprossen liegen auf E; nur die Potenz mit negativer Basis führt auf F. Keine Stelle auf G oder H.
- Ermessen (3):
  - Sprosse „Potenz mit Klammer und ohne“ (Einheit 3): die Potenz mit negativer Basis kommt im RLP nicht vor; zugeordnet über die Potenz als fortgesetzte Multiplikation (F), die im Katalog bei potenzen-wurzeln.md liegt – die Kette überschreitet damit die Stufengrenze E → F.
  - Sprosse „Minusklammer“ (Einheit 4): keine Stelle. Das Distributivgesetz steht unter Terme und Gleichungen auf F, nicht unter Zahlen und Operationen auf E.
  - Sprosse „Punkt vor Strich“ und „drei Faktoren“: der RLP nennt für rationale Zahlen keine eigene Klammerregel; zugeordnet über das Übertragen der bekannten Gesetze auf das Rechnen mit rationalen Zahlen (E).

### reelle-zahlen – Stufe G (irrational, Näherungswerte, Zahlbereiche, Potenzgesetze) – H (Einschachtelung, Wurzelgesetze, rationale Exponenten, Logarithmen; LISUM-PH „nur GYM“)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Zahlen und Operationen G (S. 42, Zahlvorstellungen): „Nennen von Pi und einiger Quadratwurzeln natürlicher Zahlen als Beispiele für irrationale Zahlen““
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[RLP F „fortgesetzte Multiplikation“, RLP G negative Exponenten; P10 2022-OS-B1j]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP F/G; P10 2015-OS-B1c, 2015-OS-B1j]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP E „auch periodische Dezimalzahlen“; LS-AA Kl. 6 II 3]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP E]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP E; LS-AA Kl. 7 IV 2]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 30 (Merkkasten): „[RLP G „Quadratwurzeln natürlicher Zahlen als Beispiele für irrationale Zahlen“; LISUM-PH „Irrationalität der Wurzel aus zwei beschreiben“]“
  - Zeile 31 (Merkkasten): „[RLP G „Teilmengenbeziehungen“; FD periodisch gegen irrational]“
  - Zeile 43 (Merkkasten): „[RLP G]“
  - Zeile 51 (Merkkasten): „[RLP G]“
  - Zeile 58 (Merkkasten): „[RLP H]“
  - Zeile 61 (Typische Fehler): „[FD; RLP G „Näherungswerte“; P10 2017-OS-K5d Bemerkung „Graph gibt nur Näherung“]“
  - Zeile 62 (Typische Fehler): „[FD; RLP G Teilmengenbeziehungen]“
  - Zeile 75 (Für schwache Schüler): „[RLP G, LISUM-PH, MO]“
- Lerneinheiten:
  - 1. Irrationale Zahlen und Zahlbereiche – G/H
    - G [Zeilen 1940–1943]: „Nennen von Pi und einiger Quadratwurzeln natürlicher Zahlen als Beispiele für irrationale“
      Block 1940–1947, Niveaustufe am Block: G (Z1947); Grundfall
    - G [Zeilen 1940–1942]: „Untersuchen und Beschreiben der Teilmengenbeziehungen aller bisher bekannten“
      Block 1940–1947, Niveaustufe am Block: G (Z1947); Zahlbereiche
    - H [Zeilen 1952–1955]: „Beschreiben und Reflektieren eines Verfahrens zur Einschachtelung von Quadratwurzeln oder Pi“
      Block 1952–1960, Niveaustufe am Block: H (Z1956); Sonderfall Einschachtelung; im Eintrag als Vorrat geführt
  - 2. Potenzgesetze – G
    - G [Zeilen 1993–1994]: „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); Grundfall
    - G [Zeilen 2839–2840]: „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); Terme mit Variablen, Themenbereich Gleichungen und Funktionen
  - 3. Wurzelgesetze und rationale Exponenten – H
    - H [Zeilen 2001–2002]: „Zusammenfassen von Termen mit Wurzeln unter Nutzung der Potenzgesetze“
      Block 2001–2007, Niveaustufe am Block: H (Z2006); Grundfall
    - H [Zeilen 2004–2005]: „Begründen der Wurzelgesetze mithilfe der Potenzgesetze“
      Block 2001–2007, Niveaustufe am Block: H (Z2006)
    - H [Zeilen 2860–2861]: „äquivalentes Umformen von Termen (auch Potenzen mit rationalen Exponenten)“
      Block 2860–2880, Niveaustufe am Block: H (Z2875); rationale Exponenten, Themenbereich Gleichungen und Funktionen
      Ermessen: Das „teilweise Wurzelziehen“ nennt der RLP nicht; der Eintrag stellt das in der Verortung selbst fest.
- Sprossen je Verfahrenstyp:
  - Zahlbereiche und irrationale Zahlen (Einheit 1)
    - Sprosse 1 · „geht die Wurzel auf“ und „Bruch oder nicht“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Bruch in Dezimalzahl umwandeln: abbrechend oder periodisch, beides rational (4×) → E [Zeilen 1856–1857]
      „als Dezimalzahl (auch periodische Dezimalzahlen)“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 3 · Wurzel aus Quadratzahl gegen Wurzel aus Nicht-Quadratzahl: rational oder irrational → G [Zeilen 1940–1943]
      „Nennen von Pi und einiger Quadratwurzeln natürlicher Zahlen als Beispiele für irrationale“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 4 · irrationale Zahlen mit dem Taschenrechner als Näherungswert, Anzeige als Näherung lesen → G [Zeilen 1944–1945]
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 5 · Zahlen in die vier Zahlbereiche einordnen (Tabelle, dann Venn-Diagramm) → G [Zeilen 1940–1942]
      „Untersuchen und Beschreiben der Teilmengenbeziehungen aller bisher bekannten“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 6 · irrationale Zahl auf der Zahlengeraden zwischen zwei Zehntel einordnen → G [Zeilen 1944–1945]
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 7 · reelle Zahlen über Näherungswerte ordnen → G [Zeilen 1940–1941]
      „Vergleichen und Ordnen von reellen Zahlen über“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 8 · exakt und gerundet nebeneinander (Wurzel stehen lassen, Näherungswert mit ≈) → G [Zeilen 1943–1944]
      „sachgerechtes Runden von reellen Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
    - Sprosse 9 · Rechnen mit Wurzeln, das rational wird (Wurzel mal sich selbst, Wurzel minus Wurzel) → G [Zeilen 1983–1984]
      „Prüfen und Übertragen der bekannten operativen Strategien und Verfahren auf das Rechnen mit“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 10 · Einschachtelung von Wurzel zwei mit Tabelle (Vorrat, H, GYM) → H [Zeilen 1952–1955]; Eintrag: Vorrat, H, GYM
      „Beschreiben und Reflektieren eines Verfahrens zur Einschachtelung von Quadratwurzeln oder Pi“ – Block 1952–1960, Niveaustufe am Block: H (Z1956)
    - Sprosse 11 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP G und LISUM-PH … → G [Zeilen 1944–1945]; Eintrag: Prüfungshöhe, Zielmarke
      „Angeben von Näherungswerten für reelle Zahlen“ – Block 1940–1947, Niveaustufe am Block: G (Z1947)
  - Potenzgesetze (Einheit 2)
    - Sprosse 1 · „gleiche Basis oder gleicher Exponent“ und „mal oder plus“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Produkt gleicher Basen als Malkette schreiben, Faktoren zählen, als Potenz (4×) → F [Zeilen 1974–1975]
      „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 3 · Produkt gleicher Basen mit dem Gesetz: Exponenten addieren → G [Zeilen 1993–1994]
      „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 4 · Quotient gleicher Basen: Exponenten subtrahieren, auch hoch null und negativ → G [Zeilen 1993–1994]
      „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 5 · Potenz einer Potenz: Exponenten multiplizieren → G [Zeilen 1993–1994]
      „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 6 · gleicher Exponent: Basen multiplizieren oder dividieren → G [Zeilen 1993–1994]
      „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 7 · Gesetz erkennen oder ausrechnen (gemischte Aufgaben) → G [Zeilen 1993–1994]
      „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 8 · gemischte Terme mit Zahlen: erst das Gesetz, dann ausrechnen → G [Zeilen 1996–1997]
      „Ausführen von Rechnungen und Überschlagsrechnungen im Kopf unter Nutzung von“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 9 · Terme mit einer Variablen → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 10 · Vorzahlen getrennt von den Variablen → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 11 · Potenzen addieren: nur gleiche Potenzen zusammenfassen → keine Stelle; Das Zusammenfassen gleicher Potenzen nennt der RLP nicht; die Potenzgesetze betreffen Produkt und Quotient.
    - Sprosse 12 · Terme mit zwei Variablen und Klammern (Vorrat) → G [Zeilen 2839–2840]; Eintrag: Vorrat
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 13 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP G und LISUM-PH … → G [Zeilen 1993–1994]; Eintrag: Prüfungshöhe, Zielmarke
      „Nutzen, Darstellen und Beschreiben der Potenzgesetze für Potenzen mit ganzzahligen“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
  - Wurzelgesetze und rationale Exponenten (Einheit 3)
    - Sprosse 1 · „Produkt oder Summe unter der Wurzel“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Wurzel aus dem Produkt zweier Quadratzahlen: beide Wege rechnen und vergleichen (4×) → H [Zeilen 2001–2002]
      „Zusammenfassen von Termen mit Wurzeln unter Nutzung der Potenzgesetze“ – Block 2001–2007, Niveaustufe am Block: H (Z2006)
    - Sprosse 3 · Wurzel aus einem Quotienten → H [Zeilen 2001–2002]
      „Zusammenfassen von Termen mit Wurzeln unter Nutzung der Potenzgesetze“ – Block 2001–2007, Niveaustufe am Block: H (Z2006)
    - Sprosse 4 · teilweises Wurzelziehen: Quadratzahl als Faktor abspalten → keine Stelle; Der Ausdruck „teilweises Wurzelziehen“ und die Handlung dazu kommen im Teil C nicht vor; der Eintrag stellt das selbst fest.
    - Sprosse 5 · Wurzeln mit gleichem Radikanden zusammenfassen → H [Zeilen 2001–2002]
      „Zusammenfassen von Termen mit Wurzeln unter Nutzung der Potenzgesetze“ – Block 2001–2007, Niveaustufe am Block: H (Z2006)
    - Sprosse 6 · Summe unter der Wurzel erst ausrechnen (Pythagoras-Form) → keine Stelle; keine Stelle; der RLP äußert sich nicht zur Reihenfolge unter der Wurzel.
    - Sprosse 7 · Wurzel als Potenz mit dem Exponenten ein halb, Taschenrechner mit Klammer → H [Zeilen 2860–2861]
      „äquivalentes Umformen von Termen (auch Potenzen mit rationalen Exponenten)“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 8 · n-te Wurzel als Potenz mit dem Exponenten eins durch n, Kubikwurzel → H [Zeilen 2860–2861]
      „äquivalentes Umformen von Termen (auch Potenzen mit rationalen Exponenten)“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 9 · Potenzgesetze auf Wurzeln übertragen → H [Zeilen 2004–2005]
      „Begründen der Wurzelgesetze mithilfe der Potenzgesetze“ – Block 2001–2007, Niveaustufe am Block: H (Z2006)
    - Sprosse 10 · Nenner rational machen (Vorrat) → keine Stelle; Das Rationalmachen des Nenners kommt im Teil C nicht vor.; Eintrag: Vorrat
    - Sprosse 11 · Wurzelgesetz mit den Potenzgesetzen begründen (Vorrat, H, GYM) → H [Zeilen 2004–2005]; Eintrag: Vorrat, H, GYM
      „Begründen der Wurzelgesetze mithilfe der Potenzgesetze“ – Block 2001–2007, Niveaustufe am Block: H (Z2006)
    - Sprosse 12 · einfache Gleichung mit Potenz oder Wurzel (Vorrat; x² = c → quadratische-gleichungen.md) → H [Zeilen 2872–2874]; Eintrag: Vorrat
      „mit höheren Potenzen (z. B. durch Faktorisieren, Substituieren oder Polynomdivision) und mit Wurzeln“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 13 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP H und LISUM-PH („nur GYM“) … → H [Zeilen 2001–2002]; Eintrag: Prüfungshöhe, Zielmarke
      „Zusammenfassen von Termen mit Wurzeln unter Nutzung der Potenzgesetze“ – Block 2001–2007, Niveaustufe am Block: H (Z2006)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 9, Mathematik: Terme und Gleichungen mit Potenzen bzw. Wurzeln“ [Zeile 1644]
  - Beleg [Zeile 1669]: „Umformen von Termen mit Wurzeln mithilfe der Potenz- bzw. Wurzelgesetze (nur GYM)“
  - Eine Reihe für alle Bildungsgänge mit dem Differenzierungshinweis (Zeile 1645); die Gymnasialmarke steht als Klammerzusatz „nur GYM“ an einzelnen Inhalten – beim Umformen von Wurzeltermen (Zeile 1669) und beim Beschreiben und Reflektieren eines Einschachtelungsverfahrens (Zeile 1692).
- Spanne: ja  – Einheit 1 und 2 liegen auf G, Einheit 3 ganz auf H; einzelne Sprossen greifen auf E und F zurück. Damit stehen Einheiten auf G und H und Sprossen auf F und darunter.
- Ermessen (4):
  - Sprosse „teilweises Wurzelziehen“ (Einheit 3): keine Stelle. Der RLP nennt weder den Ausdruck noch die Handlung; der Eintrag stellt das in der Verortung selbst fest.
  - Sprosse „Summe unter der Wurzel erst ausrechnen“: keine Stelle, obwohl sie nach dem Eintrag der am häufigsten geprüfte Stoff ist (siebzehn Originale als Nebenleistung). Der Plan hat dafür keine Zeile.
  - Sprosse „Nenner rational machen“ und „Potenzen addieren“: keine Stelle; beide Umformungen stehen nicht im Teil C.
  - Einheit 2, Sprossen 9, 10 und 12: Terme mit Variablen sind über den Themenbereich Gleichungen und Funktionen (G) belegt, nicht über Zahlen und Operationen – der Eintrag liegt also in zwei Themenbereichen.

### strahlensaetze – Stufe E (Maßstab, Ähnlichkeit; Rasterpapier C; Modellbau und technische Zeichnungen G; Begründen H) – Strahlensätze und zentrische Streckung stehen in keiner RLP-Stufe (nur Lehrwerk)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Größen und Messen E (S. 47, Rechnen mit Größen): „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen Objekten, um Maße zu ermitteln (z. B. Rechnen mit Maßstäben)““
  - Zeile 6 (Verortung): „Befund: Maßstab und Ähnlichkeit sind E-Stoff (Mindeststoff für alle Bildungsgänge); „Strahlensatz“, „zentrische Streckung“, „Streckfaktor“ und „Ähnlichkeitssätze“ kommen im RLP 1–10 Teil C (S. 38–65) nicht vor“
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2018-OS-K6c Verfahren „Meter durch fünfzig, dann in Zentimeter“]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP D/E „Umwandeln von Einheiten der Länge“; P10 2018-OS-K6c Voraussetzung „m in cm umrechnen“]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP D; MSK S5A]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D/E „auch Maßstab und Prozentrechnung“]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP E „Verhältnisgleichungen“; Lernhelfer]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP E „Lösen von Verhältnisgleichungen (auch Umstellen von Formeln)“]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP D „Zeichnen von ebenen Figuren mithilfe von Zeichengeräten“; P10 2021-OS-K4c Voraussetzungen „Durchmesser aus Radius; Kreis mit Zirkel“]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP D „Herstellen von Würfelbauten nach Ansichten“; P10 2021-OS-K4c „Draufsicht = Kreis und Rechteck“]“
  - Zeile 36 (Merkkasten): „[RLP E „ähnliche Objekte anhand ihrer Eigenschaften erkennen“; FD Alltagswort „ähnlich“ gegen Fachbegriff]“
  - Zeile 47 (Merkkasten): „[RLP E]“
  - Zeile 54 (Merkkasten): „[RLP E]“
  - Zeile 71 (Typische Fehler): „[MSK S5A Diagnose „additiv statt multiplikativ“; RLP C „Vergrößern auf Rasterpapier“; FD]“
  - Zeile 74 (Typische Fehler): „[FD Alltagsbedeutung gegen Fachbegriff; RLP E]“
  - Zeile 82 (Für schwache Schüler): „[RLP C, MSK S5A, MO]“
- Lerneinheiten:
  - 1. Maßstab – C/E/G
    - E [Zeile 2190]: „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“
      Block 2189–2206, Niveaustufe am Block: E (Z2198); Grundfall; Mindeststoff für alle Bildungsgänge
    - C [Zeilen 2419–2420]: „Vergrößern und Verkleinern von ebenen Figuren auf Rasterpapier“
      Block 2412–2423, Niveaustufe am Block: C (Z2422); das Rasterpapier steht schon auf C
    - G [Zeilen 2608–2609]: „Zeichnen von maßstäblich vergrößerten oder verkleinerten geometrischen Körpern und deren“
      Block 2608–2611, Niveaustufe am Block: kein Buchstabe; Modellbau erst auf G; Block 2608–2611 ohne Buchstaben, der Buchstabe G steht im folgenden Block (Zeile 2615)
  - 2. Zentrische Streckung und Ähnlichkeit – E
    - E [Zeilen 2515–2516]: „Erkennen und Benennen kongruenter und ähnlicher ebener geometrischer Objekte anhand“
      Block 2515–2520, Niveaustufe am Block: kein Buchstabe; die Ähnlichkeit steht auf E; Block 2515–2520 ohne Buchstaben, der Buchstabe E steht im folgenden Block (Zeile 2525)
    - E [Zeilen 2518–2519]: „Beschreiben der Eigenschaften (auch Längenverhältnisse) von Kongruenz- und“
      Block 2515–2520, Niveaustufe am Block: kein Buchstabe; die Längenverhältnisse der Ähnlichkeitsabbildung
      Ermessen: Die zentrische Streckung, das Streckzentrum und der Streckfaktor k kommen im Teil C nicht vor; die Einheit ist über die Ähnlichkeitsabbildung (E) belegt.
  - 3. Strahlensätze – keine Stelle; „Strahlensatz“ kommt im RLP 1–10 Teil C nicht vor – weder in Raum und Form noch in Größen und Messen. Der Eintrag stellt das in der Verortung selbst fest; das Thema ist Lehrwerksstoff (Kl. 9 IV 3) ohne RLP-Zeile.
- Sprossen je Verfahrenstyp:
  - Maßstab umrechnen (Einheit 1)
    - Sprosse 1 · „kleiner oder größer“ und „mal oder geteilt“ ankreuzen (Vorstufe) → C [Zeilen 2418–2419]; Eintrag: Vorstufe
      „Erkennen und Begründen von vergrößerten und verkleinerten Figuren“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 2 · Maßstab lesen und in Worten sagen (4×) → E [Zeile 2190]
      „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 3 · von der Wirklichkeit in die Zeichnung: geteilt (4×) → E [Zeile 2190]
      „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 4 · von der Zeichnung in die Wirklichkeit: mal, Ergebnis in Meter → E [Zeile 2190]
      „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · mit Einheitenwechsel: Meter erst in Zentimeter, dann teilen → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 6 · zwei Größen in einer Aufgabe (Höhe und Breite) → E [Zeile 2190]
      „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 7 · Vergrößerungsmaßstab n zu eins (Käfer, Bauteil) → E [Zeile 2190]
      „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Maßstab aus zwei Längen bestimmen und auf eine Eins vorn kürzen → E [Zeilen 2801–2802]
      „auch Maßstab und Prozentrechnung“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 9 · Landkarte mit großer Zahl hinten (Kilometer aus Kartenzentimetern) → E [Zeile 2190]
      „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 10 · Prüfungshöhe: Modellhöhe und Modelldurchmesser eines Turms; Originalhöhe aus Modellmaßen … → E [Zeile 2190]; Eintrag: Prüfungshöhe
      „Nutzen von Beziehungen zwischen maßstäblich veränderten ebenen geometrischen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
  - Maßstabsgerecht zeichnen (Einheit 1)
    - Sprosse 1 · „passt es ins Feld“ ankreuzen (Vorstufe) → keine Stelle; Das Abschätzen des Zeichenfelds nennt der RLP nicht.; Eintrag: Vorstufe
    - Sprosse 2 · Kästchenmaßstab lesen und Strecke im Raster abtragen (4×) → C [Zeilen 2419–2420]
      „Vergrößern und Verkleinern von ebenen Figuren auf Rasterpapier“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 3 · Figur auf Karo vergrößern und verkleinern (jede Seite mit dem Faktor) → C [Zeilen 2419–2420]
      „Vergrößern und Verkleinern von ebenen Figuren auf Rasterpapier“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 4 · Rechteck im gegebenen Maßstab zeichnen und beschriften → E [Zeilen 2515–2516]
      „Zeichnen von kongruenten sowie maßstäblich vergrößerten und verkleinerten ebenen Figuren“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
    - Sprosse 5 · Kreis im Maßstab: Durchmesser umrechnen, Radius mit dem Zirkel → D [Zeilen 2444–2446]
      „Zeichnen von Winkeln und ebenen Figuren mithilfe von Zeichengeräten (Lineal,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 6 · Draufsicht eines Körpers als Figur erkennen → C [Zeile 2412]
      „Herstellen von Würfelbauten nach Vorgaben“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 7 · zwei Figuren in einer Zeichnung mit ihrer Lage zueinander → D [Zeilen 2438–2440]
      „Beschreiben von Lagebeziehungen (auch mithilfe von Gitternetzen und Koordinaten)“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 8 · Maßstab selbst wählen, angeben und beschriften → keine Stelle; Das eigene Wählen eines Maßstabs nennt der RLP nicht.
    - Sprosse 9 · an der Zeichnung entscheiden (Überstand, passt oder passt nicht) → keine Stelle; Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 10 · Prüfungshöhe: Draufsicht einer Tonne im selbst gewählten Maßstab, mit Entscheidung … → E [Zeilen 2515–2516]; Eintrag: Prüfungshöhe
      „Zeichnen von kongruenten sowie maßstäblich vergrößerten und verkleinerten ebenen Figuren“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
  - Zentrische Streckung und Ähnlichkeit (Einheit 2)
    - Sprosse 1 · „gleiche Form“ und „welche Seite gehört zu welcher“ ankreuzen (Vorstufe) → E [Zeilen 2515–2516]; Eintrag: Vorstufe
      „Erkennen und Benennen kongruenter und ähnlicher ebener geometrischer Objekte anhand“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
    - Sprosse 2 · Figur auf Karo mit ganzzahligem Streckfaktor strecken (4×) → C [Zeilen 2419–2420]
      „Vergrößern und Verkleinern von ebenen Figuren auf Rasterpapier“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 3 · Zentrum außerhalb: Strahlen zeichnen, Abstände vom Zentrum vervielfachen → keine Stelle; Die zentrische Streckung mit Streckzentrum kommt im Teil C nicht vor.
    - Sprosse 4 · Verkleinern mit einem Faktor kleiner als eins → C [Zeilen 2419–2420]
      „Vergrößern und Verkleinern von ebenen Figuren auf Rasterpapier“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 5 · Streckfaktor aus Original- und Bildstrecke berechnen → keine Stelle; Den Streckfaktor k nennt der Teil C nicht.
    - Sprosse 6 · Eigenschaften prüfen: parallel, gleiche Winkel, gleiche Verhältnisse → E [Zeilen 2518–2519]
      „Beschreiben der Eigenschaften (auch Längenverhältnisse) von Kongruenz- und“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
    - Sprosse 7 · ähnliche Dreiecke an zwei gleichen Winkeln erkennen → E [Zeilen 2515–2516]
      „Erkennen und Benennen kongruenter und ähnlicher ebener geometrischer Objekte anhand“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
    - Sprosse 8 · entsprechende Seiten paaren und das Verhältnis prüfen → E [Zeilen 2518–2519]
      „Beschreiben der Eigenschaften (auch Längenverhältnisse) von Kongruenz- und“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
    - Sprosse 9 · fehlende Seite über die Verhältnisgleichung → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 10 · zwei ähnliche rechtwinklige Dreiecke messen und Verhältnisse vergleichen → E [Zeilen 2518–2519]
      „Beschreiben der Eigenschaften (auch Längenverhältnisse) von Kongruenz- und“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
    - Sprosse 11 · Fläche mal k² (Vorrat) → keine Stelle; Die Wirkung des Streckfaktors auf den Flächeninhalt steht nicht im Teil C.; Eintrag: Vorrat
    - Sprosse 12 · Modellbau: Körper maßstäblich vergrößern (Vorrat, RLP G) → G [Zeilen 2608–2609]; Eintrag: Vorrat
      „Zeichnen von maßstäblich vergrößerten oder verkleinerten geometrischen Körpern und deren“ – Block 2608–2611, Niveaustufe am Block: kein Buchstabe
    - Sprosse 13 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP E … → E [Zeilen 2515–2516]; Eintrag: Prüfungshöhe, Zielmarke
      „Erkennen und Benennen kongruenter und ähnlicher ebener geometrischer Objekte anhand“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
  - Strahlensätze (Einheit 3)
    - Sprosse 1 · „V oder X“ und „vom Zentrum aus“ ankreuzen (Vorstufe) → keine Stelle; Der Strahlensatz kommt im Teil C nicht vor.; Eintrag: Vorstufe
    - Sprosse 2 · erster Strahlensatz in der V-Figur mit ganzzahligem Faktor (4×) → keine Stelle; Der Strahlensatz kommt im Teil C nicht vor.
    - Sprosse 3 · zweiter Strahlensatz: Parallelen aus den Abschnitten → keine Stelle; Der Strahlensatz kommt im Teil C nicht vor.
    - Sprosse 4 · X-Figur → keine Stelle; Der Strahlensatz kommt im Teil C nicht vor.
    - Sprosse 5 · Verhältnisgleichung nach der gesuchten Strecke umstellen, auch Dezimalzahlen → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 6 · Abschnitt gesucht, Gesamtstrecke gegeben (Teilstrecke berechnen) → keine Stelle; Der Strahlensatz kommt im Teil C nicht vor.
    - Sprosse 7 · Sachaufgabe mit fertiger Skizze: Baumhöhe aus Schatten und Stab → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 8 · Sachaufgabe mit selbst gezeichneter Skizze: Flussbreite, Försterdreieck, Lochkamera → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 9 · Umkehrung des ersten Strahlensatzes (Vorrat) → keine Stelle; Der Strahlensatz kommt im Teil C nicht vor.; Eintrag: Vorrat
    - Sprosse 10 · Prüfungshöhe: kein P10-Original; Zielmarke nach dem Lehrwerk (Kl. 9 IV 3) … → keine Stelle; Lehrwerksmarke ohne RLP-Zeile.; Eintrag: Prüfungshöhe, Zielmarke
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Geometrie“ [Zeile 1120]
  - Beleg [Zeile 1270]: „Beschreiben und Vergleichen der Eigenschaften von Kongruenz- und Ähnlichkeitsabbildungen“
  - Eine Reihe für alle Bildungsgänge mit dem Differenzierungshinweis (Zeile 1121). Der Maßstab wird dorthin verwiesen (Zeile 333: „bzgl. Maßstab siehe ‚Jahrgangsstufe 7/8, Mathematik: Geometrie‘“), die Ähnlichkeit steht im Block ab Zeile 1269. Den Strahlensatz nennen die Planungshilfen an keiner Stelle – wie der RLP.
- Spanne: ja  – Maßstab und Ähnlichkeit liegen auf C und E, der Modellbau mit Körpern auf G. Damit steht mindestens eine Stelle auf G und mehrere auf F oder darunter. Die Einheit 3 (Strahlensätze) hat gar keine Stelle.
- Ermessen (4):
  - **Einheit 3 ganz ohne Stelle:** „Strahlensatz“ kommt weder im RLP Teil C noch in den LISUM-Planungshilfen vor. Alle zehn Sprossen außer zwei (Verhältnisgleichung, proportionale Sachaufgabe) tragen „keine Stelle“.
  - Einheit 2: zentrische Streckung, Streckzentrum und Streckfaktor k fehlen im Plan; die Einheit ist über die Ähnlichkeitsabbildung (E) belegt. Die Sprossen 3, 5 und 11 tragen deshalb „keine Stelle“.
  - Die Stellen aus dem Abschnitt „Geometrische Abbildungen“ (Zeilen 2515–2520 und 2608–2611) stehen in Blöcken ohne Buchstaben am Rand; die Stufen E bzw. G folgen der Zuordnung des Eintrags und der Stellung der Buchstaben in den Nachbarblöcken.
  - Abweichung zur Stufenangabe: index.md nennt für dieses Thema E (Modellbau G, Begründen H); die Belege bestätigen das. Der Eintrag vermerkt selbst, dass der Index das Thema früher als F–G führte.

### symmetrie-abbildungen – Stufe C–D (vier Quadranten und Symmetrie der Dreiecksarten E)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Raum und Form D (S. 52, Geometrische Objekte und ihre Eigenschaften beschreiben): „Erkennen und Beschreiben von Symmetrien (auch in Modellen von geometrischen Körpern)““
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[RLP C „Zeichnen von Spiegelbildern auf Rasterpapier“]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP D „Zeichnen von Senkrechten und Parallelen mithilfe des Geodreiecks“; LS-AA Kl. 5 II 1]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP E „vier Quadranten“; LS-AA Kl. 6 IV 1]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP C „Haus der Vierecke“, D „Systematisieren von Dreiecken“; P10 2022-OS-B1i, 2021-OS-B1j, 2018-OS-B1h Voraussetzungen]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D; LISUM-PH „Länge, Winkel, Drehung, Verschiebung“]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP C „Erzeugen von Spiegelbildern“]“
  - Zeile 30 (Merkkasten): „[RLP D „Zeichnen von ebenen Figuren im Koordinatensystem“; P10 2020-OS-B1b Fehlerquelle „erste und zweite Koordinate verwechselt“]“
  - Zeile 32 (Merkkasten): „[Serlo 35620 „Symmetrieachse als Faltkante“; RLP C „Legen und Falten“]“
  - Zeile 34 (Merkkasten): „[RLP C „Beschreiben ausgewählter Eigenschaften von Spiegelungen an Geraden“]“
  - Zeile 35 (Merkkasten): „[RLP C „Erkennen und Benennen gespiegelter, verschobener und gedrehter ebener Figuren“; LISUM-PH „Länge, Winkel, Drehung, Verschiebung“]“
  - Zeile 36 (Merkkasten): „[RLP D „Längen- und Winkeltreue bei Kongruenzabbildungen“]“
  - Zeile 44 (Merkkasten): „[RLP D]“
  - Zeile 44 (Merkkasten): „[RLP E]“
  - Zeile 51 (Typische Fehler): „[RLP C/D]“
  - Zeile 58 (Typische Fehler): „[RLP C/D]“
  - Zeile 63 (Typische Fehler): „[RLP C; FD]“
  - Zeile 66 (Typische Fehler): „[FD; RLP C]“
  - Zeile 73 (Für schwache Schüler): „[RLP C, LISUM-PH, MO]“
- Lerneinheiten:
  - 1. Koordinatensystem – D/E
    - D [Zeilen 2441–2442]: „Zeichnen von ebenen Figuren im Koordinatensystem“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Grundfall: erster Quadrant
    - E [Zeilen 2462–2463]: „Zeichnen von Figuren im Koordinatensystem (vier“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); vier Quadranten erst auf E
    - D [Zeilen 2438–2440]: „Beschreiben von Lagebeziehungen (auch mithilfe von Gitternetzen und Koordinaten)“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); das Ablesen und Beschreiben der Lage
  - 2. Achsensymmetrie und Spiegeln – C/D/E
    - C [Zeilen 2370–2372]: „symmetrischen Figuren (auch dreh- und verschiebesymmetrische Figuren)“
      Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357); die Grundlage steht schon auf C (Grundschule)
    - D [Zeilen 2449–2451]: „Erkennen und Beschreiben von Symmetrien (auch in Modellen von geometrischen“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Grundfall der Sekundarstufe
    - E [Zeilen 2462–2464]: „Beschreiben weiterer Eigenschaften der Dreiecksarten“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); die Symmetrie der Dreiecksarten erst auf E
  - 3. Punktsymmetrie, Drehung, Verschiebung – C/D
    - C [Zeilen 2412–2413]: „Erkennen und Benennen gespiegelter, verschobener und gedrehter ebener Figuren“
      Block 2412–2423, Niveaustufe am Block: C (Z2422); Grundlage auf C
    - D [Zeilen 2503–2504]: „Original- und Bildfigur (Längen- und Winkeltreue) bei Kongruenzabbildungen“
      Block 2500–2505, Niveaustufe am Block: kein Buchstabe; Block 2500–2505 ohne Buchstaben am Rand; der Buchstabe D steht im folgenden Block (Zeile 2510), der Eintrag ordnet die Stelle D zu
      Ermessen: „Punktsymmetrie“, „Symmetriezentrum“ und „Drehwinkel“ kommen im Teil C nicht vor; der RLP schreibt „drehsymmetrisch“ (C) und „Drehungen“ als Kongruenzabbildung (D).
- Sprossen je Verfahrenstyp:
  - Punkte und Figuren im Koordinatensystem (Einheit 1)
    - Sprosse 1 · „erst rechts, dann hoch“ und „welche Koordinate ist null“ ankreuzen (Vorstufe) → D [Zeilen 2438–2440]; Eintrag: Vorstufe
      „Beschreiben von Lagebeziehungen (auch mithilfe von Gitternetzen und Koordinaten)“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · Punkt im ersten Quadranten eintragen, ganze Zahlen (4×) → D [Zeilen 2441–2442]
      „Zeichnen von ebenen Figuren im Koordinatensystem“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 3 · Koordinaten eines eingezeichneten Punktes ablesen → D [Zeilen 2438–2440]
      „Beschreiben von Lagebeziehungen (auch mithilfe von Gitternetzen und Koordinaten)“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 4 · Punkte mit negativen Koordinaten, vier Quadranten → E [Zeilen 2462–2463]
      „Zeichnen von Figuren im Koordinatensystem (vier“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 5 · Quadrant angeben → keine Stelle; Das Benennen des Quadranten nennt der RLP nicht; er spricht nur von „vier Quadranten“.
    - Sprosse 6 · Punkt auf einer Achse eintragen und beschreiben → D [Zeilen 2438–2440]
      „Beschreiben von Lagebeziehungen (auch mithilfe von Gitternetzen und Koordinaten)“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 7 · Figur nach gegebenen Koordinaten zeichnen und benennen → D [Zeilen 2441–2442]
      „Zeichnen von ebenen Figuren im Koordinatensystem“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 8 · fehlende Ecke eines Rechtecks ergänzen → keine Stelle; Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 9 · Prüfungshöhe: unter vier Punkten den ankreuzen, der auf der Rechtsachse liegt … → D [Zeilen 2438–2440]; Eintrag: Prüfungshöhe
      „Beschreiben von Lagebeziehungen (auch mithilfe von Gitternetzen und Koordinaten)“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
  - Symmetrieachsen bestimmen (Einheit 2)
    - Sprosse 1 · „passt die Faltung“ und „wie viele Achsen“ ankreuzen (Vorstufe) → C [Zeilen 2421–2422]; Eintrag: Vorstufe
      „Gedankliches Operieren mit geometrischen Objekten, z. B. Kippen, Aufklappen, Spiegeln und“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 2 · eine Achse in eine offensichtlich symmetrische Figur einzeichnen (4×) → C [Zeilen 2370–2372]
      „symmetrischen Figuren (auch dreh- und verschiebesymmetrische Figuren)“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 3 · Achsen zählen bei Figuren mit einer Achse → C [Zeilen 2370–2372]
      „symmetrischen Figuren (auch dreh- und verschiebesymmetrische Figuren)“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 4 · bei Figuren mit mehreren Achsen (Diagonalen mitzählen) → C [Zeilen 2370–2372]
      „symmetrischen Figuren (auch dreh- und verschiebesymmetrische Figuren)“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 5 · Figuren ohne Achse erkennen → C [Zeilen 2370–2372]
      „symmetrischen Figuren (auch dreh- und verschiebesymmetrische Figuren)“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 6 · Vierecksarten der Reihe nach prüfen → C [Zeilen 2370–2371]
      „Beschreiben der Beziehungen zwischen Vierecken“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 7 · Dreiecksarten prüfen → E [Zeilen 2462–2464]
      „Beschreiben weiterer Eigenschaften der Dreiecksarten“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 8 · Buchstaben und Verkehrszeichen → C [Zeilen 2370–2372]
      „symmetrischen Figuren (auch dreh- und verschiebesymmetrische Figuren)“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 9 · Symmetrieachse als Diagonale nutzen (Übergabe an pythagoras.md) → D [Zeilen 2449–2451]
      „Erkennen und Beschreiben von Symmetrien (auch in Modellen von geometrischen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 10 · Prüfungshöhe: Zahl der Symmetrieachsen eines Trapezes oder Quadrats ankreuzen … → C [Zeilen 2370–2372]; Eintrag: Prüfungshöhe
      „symmetrischen Figuren (auch dreh- und verschiebesymmetrische Figuren)“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
  - Spiegeln und Spiegelbild benennen (Einheit 2)
    - Sprosse 1 · „senkrecht zur Achse“ ankreuzen (Vorstufe) → C [Zeilen 2414–2415]; Eintrag: Vorstufe
      „Beschreiben ausgewählter Eigenschaften von Spiegelungen an Geraden“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 2 · Punkt an einer senkrechten Achse spiegeln, Kästchen abzählen (4×) → C [Zeile 2418]
      „Zeichnen von Spiegelbildern auf Rasterpapier“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 3 · Figur an einer senkrechten Achse spiegeln → C [Zeile 2418]
      „Zeichnen von Spiegelbildern auf Rasterpapier“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 4 · an einer waagerechten Achse → C [Zeile 2418]
      „Zeichnen von Spiegelbildern auf Rasterpapier“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 5 · an einer Koordinatenachse, Bildkoordinaten angeben → D [Zeilen 2502–2503]
      „Zeichnen von Spiegelungen und Verschiebungen (auch mithilfe von dynamischer“ – Block 2500–2505, Niveaustufe am Block: kein Buchstabe
    - Sprosse 6 · halbe Figur zur symmetrischen ergänzen → C [Zeilen 2374–2375]
      „symmetrischen Figuren (z. B. Zeichnen auf Rasterpapier)“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 7 · Figur an einer schrägen Achse (Vorrat) → keine Stelle; Die schräge Spiegelachse nennt der RLP nicht; er spricht von Rasterpapier.; Eintrag: Vorrat
    - Sprosse 8 · die entstandene Gesamtfigur benennen → keine Stelle; Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 9 · Prüfungshöhe: welches Viereck aus Dreieck und Spiegelbild entsteht … → keine Stelle; P10-Aufgabenform, kein RLP-Inhalt.; Eintrag: Prüfungshöhe
  - Drehen, Verschieben, Punktsymmetrie (Einheit 3)
    - Sprosse 1 · „welche Abbildung“ und „gleich groß“ ankreuzen (Vorstufe) → C [Zeilen 2412–2413]; Eintrag: Vorstufe
      „Erkennen und Benennen gespiegelter, verschobener und gedrehter ebener Figuren“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 2 · Figur mit einem Pfeil verschieben, Kästchen abzählen (4×) → D [Zeilen 2502–2503]
      „Zeichnen von Spiegelungen und Verschiebungen (auch mithilfe von dynamischer“ – Block 2500–2505, Niveaustufe am Block: kein Buchstabe
    - Sprosse 3 · Verschiebung in Worten beschreiben → C [Zeilen 2412–2413]
      „Erkennen und Benennen gespiegelter, verschobener und gedrehter ebener Figuren“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 4 · Figur um einen Punkt drehen, halbe Drehung → D [Zeilen 2503–2504]
      „Original- und Bildfigur (Längen- und Winkeltreue) bei Kongruenzabbildungen“ – Block 2500–2505, Niveaustufe am Block: kein Buchstabe
    - Sprosse 5 · Vierteldrehung → D [Zeilen 2503–2504]
      „Original- und Bildfigur (Längen- und Winkeltreue) bei Kongruenzabbildungen“ – Block 2500–2505, Niveaustufe am Block: kein Buchstabe
    - Sprosse 6 · Punkt am Zentrum spiegeln → keine Stelle; Die Punktspiegelung am Zentrum nennt der Teil C nicht.
    - Sprosse 7 · Figur am Zentrum spiegeln → keine Stelle; wie Sprosse 6: keine Stelle.
    - Sprosse 8 · prüfen, ob eine Figur punktsymmetrisch ist → C [Zeilen 2370–2372]
      „symmetrischen Figuren (auch dreh- und verschiebesymmetrische Figuren)“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 9 · Bandornament fortsetzen und die Abbildung benennen → C [Zeile 2416]
      „Herstellen von schubsymmetrischen Figuren“ – Block 2412–2423, Niveaustufe am Block: C (Z2422)
    - Sprosse 10 · Parkett aus einer Figur legen → D [Zeilen 2500–2501]
      „Herstellen von Parketten durch Zeichnen und Legen von Figuren“ – Block 2500–2505, Niveaustufe am Block: kein Buchstabe
    - Sprosse 11 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP D und Lehrwerk … → D [Zeilen 2503–2504]; Eintrag: Prüfungshöhe, Zielmarke
      „Original- und Bildfigur (Längen- und Winkeltreue) bei Kongruenzabbildungen“ – Block 2500–2505, Niveaustufe am Block: kein Buchstabe
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Geometrie“ [Zeile 1120]
  - Beleg [Zeile 1121]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
  - Keine eigene Reihe: Symmetrie und Abbildungen liegen in Klasse 5/6 und damit unter dem Bereich der Planungshilfen. Die Reihe „Geometrie“ (Jahrgangsstufe 7/8) nimmt sie nur als Wiederholung auf.
- Spanne: nein  – Die Stufen reichen von C über D bis E; keine Einheit und keine Sprosse liegt auf G oder H. Das deckt sich mit der Stufenangabe „C–D (vier Quadranten und Symmetrie der Dreiecksarten E)“ in index.md.
- Ermessen (4):
  - Einheit 3 im Ganzen: „Punktsymmetrie“, „Symmetriezentrum“ und „Drehwinkel“ kommen im Teil C nicht vor. Die Zuordnung erfolgt über „drehsymmetrisch“ (C) und „Drehungen“ als Kongruenzabbildung (D).
  - Die Stellen aus dem Abschnitt „Geometrische Abbildungen“ (Zeilen 2500–2505 und 2515–2520) stehen in Blöcken ohne Buchstaben am Rand; die Stufen D bzw. E folgen der Zuordnung des Eintrags und der Stellung der Buchstaben in den Nachbarblöcken (D in Zeile 2510, E in Zeile 2525).
  - Sprossen „Punkt am Zentrum spiegeln“ und „Figur am Zentrum spiegeln“: keine Stelle; die Punktspiegelung fehlt im Plan.
  - Sprossen „Quadrant angeben“, „fehlende Ecke ergänzen“, „schräge Achse“, „Gesamtfigur benennen“: keine Stelle; alle vier sind Aufgabenformen.

### terme – Stufe E–F
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 5 (Verortung): „[RLP] Leitidee Gleichungen und Funktionen: „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen" (E), „Distributivgesetz zum Ausmultiplizieren von Summen" (F).“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[MSK N, RLP D]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 61 (Typische Fehler): „[RLP D Fertigkeit]“
  - Zeile 65 (Für schwache Schüler): „Mindeststoff (D/E) [RLP]: Einheit 1 (Termwert, Term zu Situation) und Einheit 2 ohne Potenzen; Einheit 3 nur Plus- und Zahl-mal-Klammer; Minusklammer und Einheit 4 sind F.“
- Lerneinheiten:
  - 1. Terme aufstellen und berechnen – D/E
    - D [Zeilen 2731–2732]: „Nutzen von Variablen im Sinne eines Platzhalters (auch bei gebrochenen Zahlen)“
      Block 2724–2737, Niveaustufe am Block: D (Z2732); die Variable als Platzhalter steht schon auf D
    - E [Zeilen 2739–2741]: „Darstellen von außer- und innermathematischen Sachverhalten (auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); Term aus Sachtext und Figur
  - 2. Terme zusammenfassen – E
    - E [Zeilen 2739–2740]: „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“
      Block 2739–2754, Niveaustufe am Block: E (Z2746); Grundfall; so auch die Verortung des Eintrags
  - 3. Klammern auflösen – F
    - F [Zeilen 2756–2757]: „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“
      Block 2756–2769, Niveaustufe am Block: F (Z2763); das Distributivgesetz steht auf F; der Eintrag nennt die Minusklammer selbst F-Stoff
  - 4. Ausklammern – F/G
    - F [Zeilen 2757–2758]: „Distributivgesetz zum Ausmultiplizieren von Summen)“
      Block 2756–2769, Niveaustufe am Block: F (Z2763); der RLP nennt nur das Ausmultiplizieren, nicht das Ausklammern
    - G [Zeilen 2839–2840]: „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“
      Block 2836–2855, Niveaustufe am Block: G (Z2851); Terme mit Potenzen erst auf G
      Ermessen: Das Wort „Ausklammern“ kommt im Teil C nicht vor; die Einheit ist über das Distributivgesetz (F) belegt, das der RLP nur in der Richtung „Ausmultiplizieren“ nennt.
- Sprossen je Verfahrenstyp:
  - Zusammenfassen (Einheit 2)
    - Sprosse 1 · Grundfall zwei gleichartige Glieder mit Plus (4×) → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 2 · Minus (5y − 2y) → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · drei Glieder → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · ein ungleichartiges Glied bleibt stehen → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · zwei Variablen sortieren (5a + 2b + 3a) → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 6 · Vorzahl 1 (x + 6x) → keine Stelle; Die unsichtbare Vorzahl 1 ist Schreibweise; der RLP nennt sie nicht.
    - Sprosse 7 · negatives Ergebnis (3y − 8y) → E [Zeile 2741]
      „im Zahlbereich der rationalen Zahlen)“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 8 · negatives erstes Glied (−2x + 7x) → E [Zeile 2741]
      „im Zahlbereich der rationalen Zahlen)“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 9 · Potenz bleibt getrennt (5x² + 3x + 2x²) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 10 · Dezimalzahl als Vorzahl → E [Zeile 2741]
      „im Zahlbereich der rationalen Zahlen)“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 11 · Prüfungshöhe: langer Term mit allem. → E [Zeilen 2739–2740]; Eintrag: Prüfungshöhe
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
  - Malnehmen (Einheit 2)
    - Sprosse 1 · Zahl · Term (4×) → F [Zeilen 2756–2757]
      „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 2 · Term · Zahl → F [Zeilen 2756–2757]
      „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 3 · Term · Term (x · x = x²) → G [Zeilen 2839–2840]
      „Umformen von Termen (auch Potenzen mit ganzzahligem Exponenten und auch unter“ – Block 2836–2855, Niveaustufe am Block: G (Z2851)
    - Sprosse 4 · mit Vorzeichen ((−2) · 3x) → E [Zeile 2741]
      „im Zahlbereich der rationalen Zahlen)“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 5 · zwei Variablen (3a · 2b) → keine Stelle; Terme mit mehreren Variablen nennt der Teil C erst bei den linearen Gleichungssystemen (F); für das Produkt zweier Variablen gibt es keine Zeile.
    - Sprosse 6 · drei Faktoren → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · Prüfungshöhe: Vorzeichen und zwei Variablen. → F [Zeilen 2756–2757]; Eintrag: Prüfungshöhe
      „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
  - Klammern (Einheit 3)
    - Sprosse 1 · Plusklammer weglassen (3×) → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 2 · Zahl · Klammer (4×, Tabelle als Bild) → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 3 · Minusklammer zwei Glieder → F [Zeilen 2757–2758]; Eintrag: F-Stoff (Eintrag)
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 4 · Minusklammer drei Glieder → F [Zeilen 2757–2758]; Eintrag: F-Stoff (Eintrag)
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 5 · negative Zahl · Klammer → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 6 · auflösen und zusammenfassen → F [Zeilen 2756–2757]
      „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 7 · Prüfungshöhe: zwei Klammern. → F [Zeilen 2756–2757]; Eintrag: Prüfungshöhe
      „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
  - Term aufstellen (Einheit 1)
    - Sprosse 1 · passenden Term ankreuzen (3×) → D [Zeilen 2733–2734]
      „Angeben von passenden außer- und innermathematischen Sachverhalten zu vorgegeben“ – Block 2724–2737, Niveaustufe am Block: D (Z2732)
    - Sprosse 2 · Term aus Wörtern (Doppeltes, um vier mehr) → E [Zeilen 2739–2741]
      „Darstellen von außer- und innermathematischen Sachverhalten (auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 3 · aus Figur → E [Zeilen 2739–2741]
      „Darstellen von außer- und innermathematischen Sachverhalten (auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 4 · aus Situation mit zwei Variablen → F [Zeile 2757]
      „Sachverhalten durch Terme, Gleichungen und“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 5 · zusammenfassen → E [Zeilen 2739–2740]
      „Nutzen von Kommutativ- und Assoziativgesetz zum äquivalenten Umformen von Termen (auch“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 6 · Kette aus drei Anweisungen, bei der die Klammer nötig wird → E [Zeilen 2739–2741]
      „Darstellen von außer- und innermathematischen Sachverhalten (auch im Zahlenbereich der rationalen Zahlen) durch Terme, lineare“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 7 · Prüfungshöhe: unter vier Termen den passenden zu einem Sachtext ankreuzen … → D [Zeilen 2733–2734]; Eintrag: Prüfungshöhe
      „Angeben von passenden außer- und innermathematischen Sachverhalten zu vorgegeben“ – Block 2724–2737, Niveaustufe am Block: D (Z2732)
  - Ausklammern (Einheit 4)
    - Sprosse 1 · gemeinsamen Zahlfaktor bei zwei Gliedern (4×) → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 2 · gemeinsame Variable → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 3 · Zahl und Variable zusammen → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 4 · ein Glied ist selbst der Faktor, in der Klammer bleibt die Eins → keine Stelle; Sonderfall der Schreibweise; der RLP nennt ihn nicht.
    - Sprosse 5 · drei Glieder → F [Zeilen 2757–2758]
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 6 · Probe durch Ausmultiplizieren → F [Zeilen 2756–2757]
      „Nutzen von Rechengesetzen zum äquivalenten Umformen von Termen (auch Distributivgesetz“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
    - Sprosse 7 · Fehler finden: Faktor nur aus einem Glied gezogen → keine Stelle; Fehlerquelle des Unterrichts; der RLP nennt sie nicht.
    - Sprosse 8 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP F und LISUM-PH … → F [Zeilen 2757–2758]; Eintrag: Prüfungshöhe, Zielmarke
      „Distributivgesetz zum Ausmultiplizieren von Summen)“ – Block 2756–2769, Niveaustufe am Block: F (Z2763)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7, Mathematik: Terme und Gleichungen“ [Zeile 344]; „Jahrgangsstufe 8, Mathematik: Terme und Gleichungen“ [Zeile 850]
  - Beleg [Zeile 345]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
  - Beide Reihen führen EBR, FOR und GYM gemeinsam und tragen den Differenzierungshinweis (Zeilen 345 und 851). Die Reihe der Jahrgangsstufe 8 hat zusätzlich einen Block „Niveaustufe H (nur Gym)“ (Zeile 928), der aber die Zuordnungen und nicht die Terme betrifft.
- Spanne: ja  – Die Einheiten liegen auf D, E und F; Terme mit Potenzen (Sprosse 9 der Kette Zusammenfassen und Sprosse 3 der Kette Malnehmen) finden ihre Stelle erst auf G. Damit stehen Sprossen auf G und Einheiten auf F und darunter.
- Ermessen (4):
  - Einheit 4: das Wort „Ausklammern“ kommt im Teil C nicht vor. Der RLP nennt das Distributivgesetz nur in der Richtung „Ausmultiplizieren von Summen“ (F); die Rückrichtung ist eine Zuordnung nach Sinn.
  - Sprossen mit Potenzen im Term („Potenz bleibt getrennt“, „Term · Term“): zugeordnet auf G, weil der RLP Terme mit Potenzen erst dort nennt. Der Eintrag rechnet sie zu den E/F-Einheiten.
  - Sprosse „zwei Variablen (3a · 2b)“: keine Stelle; der Teil C nennt mehrere Variablen erst bei linearen Gleichungssystemen.
  - Sprossen „Vorzahl 1“, „in der Klammer bleibt die Eins“, „Fehler finden“: keine Stelle; Schreibweisen und Fehlerquellen.

### trigonometrie – Stufe F (rechtwinklig) – G (Sinussatz, Kosinussatz Seiten; Winkel H)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Größen und Messen F (S. 49, Rechnen mit Größen): „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von Sinus, Kosinus und Tangens (auch mithilfe von digitalen Mathematikwerkzeugen)““
  - Zeile 6 (Verortung): „Befund: das rechtwinklige Dreieck steht auf F, also nicht im Mindeststoff D/E; der RLP nennt weder Gegenkathete noch Ankathete noch die Umkehrfunktionen“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP D „Systematisieren von Dreiecken“; P10 2018-OS-K4c Fehlerquelle „Dreieck als rechtwinklig behandeln“]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D „Messen von Winkeln“; P10 Beschriftungen 2024-OS-K6b, 2026-FOR-K4b]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP E „Umstellen von Formeln“; P10 2020-OS-B1j, 2022-OS-K5d, 2026-FOR-K4c „Gleichung nach der Hypotenuse umstellen“]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2019-OS-K3b Zwischenergebnis „cos α = 0,444“]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP E; P10 2016-OS-K7b, 2021-OS-K3b, 2023-OS-K2c „Trigonometrie oder Pythagoras“]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP E „sinnvolle Genauigkeit“; P10 2014-OS-K2b Meter und Kilometer gemischt]“
  - Zeile 32 (Voraussetzungen (Blatt 0)): „[RLP D/E; P10 2020-OS-K5b, 2023-OS-K2c, 2026-FOR-K4b, 2015-OS-K5c]“
  - Zeile 68 (Merkkasten): „[RLP F]“
  - Zeile 90 (Typische Fehler): „[RLP E „sinnvolle Genauigkeit“; P10 2019-OS-K3c Bemerkung zur Rundung; FD]“
  - Zeile 96 (Für schwache Schüler): „[RLP F, MO]“
- Lerneinheiten:
  - 1. Seite berechnen mit Sinus, Kosinus und Tangens – G
    - G [Zeile 2278]: „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); Befund: die Zeile steht in der G-Zeile des Blocks 2278–2295 (Buchstabe G in Zeile 2285), nicht in der F-Zeile (Block 2263–2276, Buchstabe F in Zeile 2271). Eintrag und index.md nennen F.
      Ermessen: Der RLP nennt weder „Gegenkathete“ noch „Ankathete“ noch die Umkehrfunktionen; die Einheit hängt an der einen Zeile zum rechtwinkligen Dreieck.
  - 2. Winkel berechnen – G
    - G [Zeile 2278]: „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); der RLP nennt Winkelgrößen und Seitenlängen in einer Zeile; eine eigene Zeile zum Winkel gibt es nicht
  - 3. Rechtwinklige Teildreiecke in Figuren und Vermessung – G
    - G [Zeile 2280]: „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); „Zerlegung in rechtwinklige Teildreiecke“ deckt die Einheit ab
    - G [Zeile 2285]: „Kugeln, auch unter Nutzung trigonometrischer Beziehungen und mithilfe von digitalen“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); das Stützdreieck am Körper mit Neigungswinkel
  - 4. Sinussatz – G/H
    - G [Zeile 2290]: „Nutzen des Sinussatzes, um in beliebigen Dreiecken Winkelgrößen und Seitenlängen zu“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); Grundfall
    - G [Zeile 2292]: „Nutzen des Kosinussatzes, um in beliebigen Dreiecken Seitenlängen zu bestimmen“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); Kosinussatz für Seiten
    - H [Zeile 2295]: „Nutzen des Kosinussatzes, um in beliebigen Dreiecken auch Winkelgrößen zu bestimmen“
      Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295); Kosinussatz für Winkel erst auf H; im Eintrag als Vorrat mit GYM-Marke
- Sprossen je Verfahrenstyp:
  - Seite berechnen (Einheit 1)
    - Sprosse 1 · Seiten vom Winkel aus mit H, G, A beschriften (Vorstufe) → keine Stelle; Gegenkathete, Ankathete und Hypotenuse nennt der Teil C nicht.; Eintrag: Vorstufe
    - Sprosse 2 · sin, cos und tan zum beschrifteten Dreieck als Bruch eintragen → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 3 · dieselbe Aufgabe als Ankreuzen unter drei Gleichungen (P10-Form) → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 4 · Werte am Taschenrechner, Grad-Modus → G [Zeile 2279]
      „Sinus, Kosinus und Tangens (auch mithilfe von digitalen Mathematikwerkzeugen)“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 5 · Gegenkathete aus Hypotenuse und Winkel mit dem Sinus, drei Zeilen (4×) → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 6 · Ankathete mit dem Kosinus → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 7 · Dreieck in anderer Lage, anderer Winkel markiert → keine Stelle; Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 8 · Hypotenuse gesucht: geteilt durch den Sinus → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 9 · geteilt durch den Kosinus → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 10 · Gegenkathete mit dem Tangens → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 11 · Ankathete gesucht: geteilt durch den Tangens → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 12 · Funktion selbst wählen → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 13 · Gleichung ohne Figur nach der Seite im Nenner umstellen (P10-Form) → E [Zeile 2747]
      „Lösen von Verhältnisgleichungen“ – Block 2739–2754, Niveaustufe am Block: E (Z2746)
    - Sprosse 14 · Winkel als Dezimalgrad, Seiten als Dezimalzahlen mit Einheit → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 15 · Nachweis mit vorgegebenem Ergebnis → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 16 · Sachaufgabe mit gegebener Skizze (Leiter, Dachwand, Rampe, Viereck) → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 17 · Prüfungshöhe: Nachweis der Seite AB im Viereck; Abstand an der Dachwand … → G [Zeile 2278]; Eintrag: Prüfungshöhe
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
  - Winkel berechnen (Einheit 2)
    - Sprosse 1 · „Seite oder Winkel gesucht“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Winkel aus Gegenkathete und Hypotenuse mit sin⁻¹ (4×) → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 3 · aus Ankathete und Hypotenuse mit cos⁻¹ → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 4 · aus beiden Katheten mit tan⁻¹ → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 5 · Dreieck in anderer Lage, Winkel an anderer Ecke → keine Stelle; Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 6 · zweiter spitzer Winkel als Ergänzung, Kontrolle mit der zweiten Funktion → D [Zeilen 2459–2461]
      „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 7 · Dezimalzahlen als Seiten, Runden auf eine Dezimale → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Steigungswinkel einer Rampe oder Seilbahn aus Höhe und Seillänge → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 9 · Winkel im Dreieck im Koordinatensystem aus abgelesenen Katheten → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 10 · Winkel im Teildreieck mit gezeichneter Höhe → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 11 · Nachweis mit vorgegebenem Winkel als Text „also rund …“ → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 12 · Prüfungshöhe: Steigungswinkel der Seilbahn mit cos⁻¹; Winkel im Parallelogramm … → G [Zeile 2278]; Eintrag: Prüfungshöhe
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
  - Teildreiecke und Vermessung (Einheit 3)
    - Sprosse 1 · Teildreieck nachfahren, Seiten vom Winkel aus beschriften (Vorstufe) → keine Stelle; Das Herauslösen eines Teildreiecks nennt der RLP nicht als eigene Handlung.; Eintrag: Vorstufe
    - Sprosse 2 · Höhe im gleichschenkligen Dreieck aus Schenkel und Basiswinkel (4×) → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 3 · Trapez: Schenkel aus Höhe und Basiswinkel → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 4 · Trapez: Höhe oder Überstand aus Schenkel und Winkel → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 5 · rechtwinkliges Trapez: Hilfsdreieck mit der Differenz der Höhen als Kathete → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 6 · Parallelogramm: Höhe mit Fußpunkt auf der Verlängerung, Winkel dort → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 7 · Diagonale des Parallelogramms aus Höhe und Winkel an der Diagonalen → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 8 · Drachen: halbe Diagonale aus Seite und Winkel → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 9 · Vermessung: Höhe über dem Gerät aus Abstand und Höhenwinkel → G [Zeile 2278]
      „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 10 · Gerätehöhe addieren → keine Stelle; Aufgabenform der Vermessung; der RLP nennt sie nicht.
    - Sprosse 11 · Plattform oder Aufbau addieren → keine Stelle; wie Sprosse 10: keine Stelle.
    - Sprosse 12 · Teilwinkel als Differenz zweier Winkel, dann Seite → D [Zeilen 2459–2461]
      „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 13 · zwei Teildreiecke nacheinander an derselben Höhe → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 14 · Rechenweg als Lösungsplan ohne Zahlen → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 15 · zweiter Weg mit Pythagoras und Vergleich → E [Zeile 2203]
      „Verwenden des Satzes von Pythagoras zur Berechnung von Streckenlängen in rechtwinkligen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 16 · Höhe für die Fläche oder Schenkel für den Umfang weitergeben → E [Zeile 2194]
      „Berechnen des Flächeninhalts von Dreiecken, Vierecken, Kreisen auf der Basis von Zerlegungen“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 17 · Stützdreieck in Pyramide oder Kegel mit Neigungswinkel (kein P10-Original) → G [Zeile 2285]; Eintrag: Zielmarke
      „Kugeln, auch unter Nutzung trigonometrischer Beziehungen und mithilfe von digitalen“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 18 · Prüfungshöhe: Berghöhe mit Gerätehöhe und Plattform; Winkel im Trapez … → G [Zeile 2280]; Eintrag: Prüfungshöhe
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
  - Sinussatz (Einheit 4)
    - Sprosse 1 · „rechtwinklig oder nicht“ und Paare markieren (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Seite aus vollständigem Paar und Gegenwinkel, drei Zeilen (4×) → G [Zeile 2290]
      „Nutzen des Sinussatzes, um in beliebigen Dreiecken Winkelgrößen und Seitenlängen zu“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 3 · Dreieck in anderer Lage, andere Buchstaben → keine Stelle; Aufgabenform; der RLP nennt sie nicht.
    - Sprosse 4 · dritter Winkel aus der Winkelsumme zuerst → D [Zeilen 2459–2461]
      „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 5 · stumpfer Winkel im Paar → keine Stelle; Der Sinus stumpfer Winkel steht nicht im Teil C; er gehört zu den trigonometrischen Funktionen (H).
    - Sprosse 6 · stumpfer Winkel in der Winkelsumme → keine Stelle; wie Sprosse 5: keine Stelle.
    - Sprosse 7 · Dezimalzahlen und Einheiten, Ergebnis auf eine Dezimale → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 8 · Nachweis mit vorgegebenem Ergebnis → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 9 · Aussage über zwei Seiten prüfen → E [Zeile 2200]
      „Durchführen von Berechnungen und Bewerten der Ergebnisse sowie des gewählten Weges in“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 10 · Sinussatz im Viereck mit Diagonale nach Teilwinkeln → G [Zeile 2290]
      „Nutzen des Sinussatzes, um in beliebigen Dreiecken Winkelgrößen und Seitenlängen zu“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 11 · Seite als Teil einer Weglänge oder als Differenz zur Teilstrecke → G [Zeile 2290]
      „Nutzen des Sinussatzes, um in beliebigen Dreiecken Winkelgrößen und Seitenlängen zu“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 12 · zweiter Weg über zwei rechtwinklige Teildreiecke (Vergleich) → G [Zeile 2280]
      „Berechnen von Winkelgrößen und Seitenlängen in beliebigen Dreiecken durch Zerlegung“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 13 · Winkel mit dem Sinussatz aus vollständigem Paar und zweiter Seite (kein P10-Original) → G [Zeile 2290]; Eintrag: Zielmarke
      „Nutzen des Sinussatzes, um in beliebigen Dreiecken Winkelgrößen und Seitenlängen zu“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 14 · Kosinussatz für die dritte Seite aus zwei Seiten und dem eingeschlossenen Winkel → G [Zeile 2292]; Eintrag: Zielmarke
      „Nutzen des Kosinussatzes, um in beliebigen Dreiecken Seitenlängen zu bestimmen“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 15 · Kosinussatz nach dem Winkel umgestellt (Vorrat, GYM) → H [Zeile 2295]; Eintrag: Vorrat, GYM
      „Nutzen des Kosinussatzes, um in beliebigen Dreiecken auch Winkelgrößen zu bestimmen“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 16 · Herleitung des Sinussatzes über die Höhe nachvollziehen (Vorrat, GYM) → keine Stelle; Die Herleitung des Sinussatzes nennt der Teil C nicht; der LISUM-Block markiert sie „nur Gym“.; Eintrag: Vorrat, GYM
    - Sprosse 17 · Prüfungshöhe: Seilbahnstrecke nach dem dritten Winkel; Rampenlänge mit stumpfem Winkel … → G [Zeile 2290]; Eintrag: Prüfungshöhe
      „Nutzen des Sinussatzes, um in beliebigen Dreiecken Winkelgrößen und Seitenlängen zu“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 9/10, Mathematik: Trigonometrie“ [Zeile 2007]
  - Beleg [Zeile 2069]: „Berechnen von Winkeln durch Umstellen des Kosinussatzes (nur“
  - Eine Reihe für alle Bildungsgänge mit dem Differenzierungshinweis (Zeile 2008); sie hat Blöcke auf Niveaustufe G (Zeilen 2013 und 2036) und auf H (Zeilen 2056 und 2062). Die Gymnasialmarke steht innerhalb der Reihe am Umstellen des Kosinussatzes nach dem Winkel (Zeile 2069).
- Spanne: ja  – Alle vier Einheiten liegen auf G, der Kosinussatz für Winkel auf H; Sprossen zum Umstellen, Runden und zur Winkelsumme greifen auf D und E zurück. Damit stehen Einheiten auf G und H und Sprossen auf F und darunter.
- Ermessen (5):
  - **Abweichung vom Eintrag:** Der Eintrag und die Zeile in index.md nennen für die rechtwinklige Trigonometrie die Stufe F. Im Quelltext steht „Berechnen von Winkelgrößen und Seitenlängen in rechtwinkligen Dreiecken mithilfe von Sinus, Kosinus und Tangens“ (Zeilen 2278–2279) jedoch im Block 2278–2295, dessen Buchstabe am Rand G ist (Zeile 2285); der F-Block endet mit Zeile 2276. Nach dem Buchstaben am Rand ist die rechtwinklige Trigonometrie G-Stoff, nicht F.
  - Einheit 1 und 2: der RLP nennt weder Gegenkathete noch Ankathete noch die Umkehrfunktionen sin⁻¹, cos⁻¹, tan⁻¹; beide Einheiten hängen an derselben Zeile.
  - Sprossen „Dreieck in anderer Lage“ (dreimal), „Gerätehöhe addieren“, „Plattform addieren“: keine Stelle; alle sind Aufgabenformen.
  - Sprossen „stumpfer Winkel im Paar“ und „in der Winkelsumme“: keine Stelle. Der Sinus stumpfer Winkel gehört zu den trigonometrischen Funktionen (H) und wird im Katalog von trigonometrische-funktionen.md geführt.
  - Sprosse „Herleitung des Sinussatzes“: keine Stelle; die Planungshilfe markiert sie „nur Gym“, der RLP nennt sie nicht.

### trigonometrische-funktionen – Stufe G (y = a sin(b x) mit allen Merkmalen) – H (y = a sin(b x + c) + d, y = a cos(b x); Bogenmaß am Einheitskreis unter Größen und Messen)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Gleichungen und Funktionen G (S. 61, Zuordnungen und Funktionen untersuchen): „Bestimmen und Beschreiben von Merkmalen (Definitionsbereich, Wertebereich, Form des Graphen, Schnittpunkte mit den Koordinatenachsen, Einfluss der Parameter auf den Verlauf des Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt, Periodizität) folgender Funktionstypen (auch mithilfe von digitalen Mathematikwerkzeugen): … − trigonometrische Funktionen der Form y = a sin(b x) …““
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP F; LISUM-PH Wiederholungsblock „Berechnungen in Dreiecken“]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP E „Zeichnen von Figuren im Koordinatensystem (vier Quadranten)“]“
  - Zeile 28 (Voraussetzungen (Blatt 0)): „[RLP E; hier Grundlage des Bogenmaßes]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP D „Messen von Winkeln“]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP E/F/G]“
  - Zeile 31 (Voraussetzungen (Blatt 0)): „[RLP G „auch bei verschiedenen Einheiten und Einteilungen der Koordinatenachsen“]“
  - Zeile 32 (Voraussetzungen (Blatt 0)): „[RLP G; LS-AA Kl. 9 I 2–3]“
  - Zeile 33 (Voraussetzungen (Blatt 0)): „[RLP C/D; LISUM-PH Begriff „Symmetrieachse“]“
  - Zeile 34 (Voraussetzungen (Blatt 0)): „[RLP E; Grundlage von Mittellinie und Amplitude]“
  - Zeile 35 (Voraussetzungen (Blatt 0)): „[RLP C „Nutzen von gebräuchlichen Bruchzahlen bei Größenangaben“]“
  - Zeile 37 (Merkkasten): „[RLP H „Zusammenhang zwischen Bogen- und Gradmaß“; LISUM-PH „Taschenrechnereinsatz“; P10 2021-OS-K3a Fehlerquelle]“
  - Zeile 41 (Merkkasten): „[RLP G „Einfluss der Parameter … (Streckung, Stauchung, Verschiebung)“; LISUM-PH „Untersuchen und Beschreiben des Einflusses der Parameter“]“
  - Zeile 42 (Merkkasten): „[RLP G „periodische Vorgänge wie Schwingungen“; LISUM-PH Sachkontexte]“
  - Zeile 43 (Merkkasten): „[RLP G „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“; potenz-exponentialfunktionen.md Einheit 1]“
  - Zeile 55 (Merkkasten): „[RLP H]“
  - Zeile 64 (Merkkasten): „[RLP G]“
  - Zeile 75 (Merkkasten): „[RLP G]“
  - Zeile 75 (Merkkasten): „[RLP H]“
  - Zeile 84 (Typische Fehler): „[RLP G]“
  - Zeile 91 (Typische Fehler): „[RLP H; FD]“
  - Zeile 95 (Typische Fehler): „[FD; RLP G Parametereinfluss]“
  - Zeile 98 (Typische Fehler): „[FD; RLP G „verschiedene Einheiten und Einteilungen der Koordinatenachsen“]“
  - Zeile 102 (Für schwache Schüler): „[RLP G/H, LISUM-PH, MO]“
- Lerneinheiten:
  - 1. Einheitskreis und Bogenmaß – H
    - H [Zeilen 2249–2250]: „Beschreiben des Zusammenhangs zwischen Bogen- und Gradmaß am Einheitskreis“
      Block 2249–2252, Niveaustufe am Block: H (Z2251); Themenbereich Größen und Messen; die einzige Stelle, die den Einheitskreis nennt
    - H [Zeilen 2251–2252]: „Umrechnen von Winkeln im Gradmaß ins Bogenmaß und umgekehrt“
      Block 2249–2252, Niveaustufe am Block: H (Z2251)
      Ermessen: Das Ablesen von Sinus- und Kosinuswerten am Einheitskreis nennt der Teil C nicht; nur der Zusammenhang von Bogen- und Gradmaß (H) ist belegt.
  - 2. Sinus- und Kosinusfunktion und ihre Merkmale – G
    - G [Zeilen 2913–2915]: „− trigonometrische Funktionen der Form y = a sin(b x)“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); die Grundform steht auf G; der RLP schreibt sie ohne Malpunkt
    - G [Zeilen 2894–2896]: „Darstellen von Zuordnungen und Funktionen (auch quadratische,“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); Darstellen im Koordinatensystem
  - 3. Parameter und Transformationen – G/H
    - G [Zeilen 2904–2906]: „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); Parameter a und b, Streckung und Stauchung
    - H [Zeilen 2927–2930]: „− trigonometrische Funktionen der Form y = a sin(b x + c) + d und y = a cos(b x)“
      Block 2920–2957, Niveaustufe am Block: H (Z2934); Parameter c und d sowie die Kosinusform erst auf H; im Eintrag als Vorrat
  - 4. Periodische Vorgänge modellieren – G
    - G [Zeilen 2910–2911]: „bei periodischen Vorgängen wie Schwingungen)“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); das Modellieren periodischer Vorgänge steht ausdrücklich auf G
    - G [Zeilen 2894–2896]: „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); die vier Funktionstypen gegenüberstellen
- Sprossen je Verfahrenstyp:
  - Einheitskreis und Bogenmaß (Einheit 1)
    - Sprosse 1 · „Grad oder Bogenmaß“, „welcher Quadrant“ und „hoch oder rüber“ ankreuzen (Vorstufe) → H [Zeilen 2249–2250]; Eintrag: Vorstufe
      „Beschreiben des Zusammenhangs zwischen Bogen- und Gradmaß am Einheitskreis“ – Block 2249–2252, Niveaustufe am Block: H (Z2251)
    - Sprosse 2 · zu einem gegebenen Winkel den Punkt auf dem Einheitskreis einzeichnen (Grundfall) → E [Zeilen 2462–2463]
      „Zeichnen von Figuren im Koordinatensystem (vier“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 3 · zu einem eingezeichneten Punkt den Winkel angeben → E [Zeilen 2462–2463]
      „Zeichnen von Figuren im Koordinatensystem (vier“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 4 · Sinuswert als Höhe und Kosinuswert als Rechtsstrecke ablesen → keine Stelle; Das Ablesen der Werte am Einheitskreis nennt der Teil C nicht; es steht nur in der Planungshilfe.
    - Sprosse 5 · Werte der vier Achsenwinkel angeben → keine Stelle; wie Sprosse 4: keine Stelle.
    - Sprosse 6 · abgelesenen Wert mit dem Taschenrechner im Grad-Modus prüfen → G [Zeile 2279]
      „Sinus, Kosinus und Tangens (auch mithilfe von digitalen Mathematikwerkzeugen)“ – Block 2278–2295, Niveaustufe am Block: G (Z2285), H (Z2295)
    - Sprosse 7 · Vorzeichen beider Werte im angegebenen Quadranten bestimmen → keine Stelle; Die Vorzeichen in den Quadranten nennt der Teil C nicht.
    - Sprosse 8 · zu einem gegebenen Sinuswert beide Winkel im Vollkreis finden → keine Stelle; keine Stelle; der Teil C nennt keine Umkehraufgabe am Einheitskreis.
    - Sprosse 9 · Bogenmaß eines Winkels über den Anteil am Kreisumfang begründen → H [Zeilen 2249–2250]
      „Beschreiben des Zusammenhangs zwischen Bogen- und Gradmaß am Einheitskreis“ – Block 2249–2252, Niveaustufe am Block: H (Z2251)
    - Sprosse 10 · Winkel vom Gradmaß ins Bogenmaß umrechnen → H [Zeilen 2251–2252]
      „Umrechnen von Winkeln im Gradmaß ins Bogenmaß und umgekehrt“ – Block 2249–2252, Niveaustufe am Block: H (Z2251)
    - Sprosse 11 · Winkel vom Bogenmaß ins Gradmaß umrechnen → H [Zeilen 2251–2252]
      „Umrechnen von Winkeln im Gradmaß ins Bogenmaß und umgekehrt“ – Block 2249–2252, Niveaustufe am Block: H (Z2251)
    - Sprosse 12 · geläufige Winkel als Vielfache von Pi zuordnen → H [Zeilen 2251–2252]
      „Umrechnen von Winkeln im Gradmaß ins Bogenmaß und umgekehrt“ – Block 2249–2252, Niveaustufe am Block: H (Z2251)
    - Sprosse 13 · Taschenrechner-Modus erkennen und wechseln → keine Stelle; Die Modi DEG und RAD nennt der Teil C nicht; sie stehen in der Planungshilfe.
    - Sprosse 14 · den Sinus eines stumpfen Winkels bilden und am Einheitskreis zeigen, warum es ihn gibt → keine Stelle; keine Stelle; der Teil C beschränkt Sinus und Kosinus auf das rechtwinklige Dreieck und die Funktion y = a sin(b x).; Eintrag: P10-Nebenleistung
    - Sprosse 15 · Prüfungshöhe: kein eigenes P10-Original; Zielmarke nach RLP H und LISUM-PH … → H [Zeilen 2251–2252]; Eintrag: Prüfungshöhe, Zielmarke
      „Umrechnen von Winkeln im Gradmaß ins Bogenmaß und umgekehrt“ – Block 2249–2252, Niveaustufe am Block: H (Z2251)
  - Sinus- und Kosinusfunktion (Einheit 2)
    - Sprosse 1 · „wo ist die Welle zu Ende“ ankreuzen (Vorstufe) → G [Zeilen 2913–2915]; Eintrag: Vorstufe
      „− trigonometrische Funktionen der Form y = a sin(b x)“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · Wertetabelle in gleichen Winkelschritten ausfüllen (Grundfall, viermal) → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · Punkte eintragen und die Welle zeichnen → G [Zeilen 2894–2896]
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Achseneinteilung wählen und beschriften → G [Zeilen 2902–2903]
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · Funktionswert zu einem Winkel ablesen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · Winkel zu einem Funktionswert ablesen, beide Lösungen im Vollkreis → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · Funktionswert berechnen und Punktprobe → keine Stelle; Die Punktprobe nennt der RLP für trigonometrische Funktionen nicht.
    - Sprosse 8 · Wertebereich angeben → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · Nullstellen angeben und die Regelmäßigkeit beschreiben → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 10 · Hoch- und Tiefpunkte angeben → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 11 · kleinste Periode angeben → G [Zeile 2907]
      „Periodizität) folgender“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 12 · Monotonie in einem Abschnitt beschreiben → keine Stelle; Die Monotonie nennt der Teil C in der Merkmalsliste nicht.
    - Sprosse 13 · Symmetrie der Sinus- und der Kosinuskurve beschreiben → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 14 · beide Graphen vergleichen und die Verschiebung angeben → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 15 · Graph und Gleichung einander zuordnen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 16 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP G und LISUM-PH … → G [Zeile 2899]; Eintrag: Prüfungshöhe, Zielmarke
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Parameter und Transformationen (Einheit 3)
    - Sprosse 1 · „höher oder schmaler“ ankreuzen (Vorstufe) → G [Zeilen 2904–2906]; Eintrag: Vorstufe
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · Amplitude aus einer Gleichung ablesen (Grundfall, viermal) → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · Wertebereich zu gegebener Amplitude angeben → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Amplitude an einem Graphen ablesen → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · Spiegelung an der waagerechten Achse bei negativem Vorzeichen erkennen → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · Periode aus dem Faktor berechnen → G [Zeile 2907]
      „Periodizität) folgender“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · Faktor aus der abgelesenen Periode berechnen → G [Zeile 2907]
      „Periodizität) folgender“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · Graph zu einer gegebenen Gleichung skizzieren → G [Zeilen 2894–2896]
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · Gleichung aus einem Graphen aufstellen (erst Amplitude, dann Periode, dann Faktor) → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 10 · Graphen und Gleichungen einander zuordnen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 11 · die Wirkung eines Parameters in Worten beschreiben → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 12 · Verschiebung nach oben und unten und zur Seite (Vorrat, H, GYM) → H [Zeilen 2927–2930]; Eintrag: Vorrat, H; LISUM „nur GYM“ nur für d (Zeile 2689)
      „− trigonometrische Funktionen der Form y = a sin(b x + c) + d und y = a cos(b x)“ – Block 2920–2957, Niveaustufe am Block: H (Z2934)
    - Sprosse 13 · Kosinusfunktion als verschobene Sinusfunktion (Vorrat, H, GYM) → H [Zeilen 2927–2930]; Eintrag: Vorrat, H, GYM (LISUM Zeile 2685)
      „− trigonometrische Funktionen der Form y = a sin(b x + c) + d und y = a cos(b x)“ – Block 2920–2957, Niveaustufe am Block: H (Z2934)
    - Sprosse 14 · Lage der Nullstellen und Extremstellen mit Parameter und Periode (Vorrat, H, GYM) → H [Zeilen 2920–2921]; Eintrag: Vorrat, H, GYM (LISUM Zeile 2687)
      „Bestimmen und Beschreiben von Merkmalen von Funktionen,“ – Block 2920–2957, Niveaustufe am Block: H (Z2934)
    - Sprosse 15 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP G und LISUM-PH (EBR/FOR-Fassung) … → G [Zeilen 2909–2911]; Eintrag: Prüfungshöhe, Zielmarke
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Periodische Vorgänge modellieren (Einheit 4)
    - Sprosse 1 · „wiederholt sich das“ und „welcher Funktionstyp“ ankreuzen (Vorstufe) → G [Zeilen 2894–2896]; Eintrag: Vorstufe
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 2 · einen Vorgang als periodisch oder nicht einordnen und begründen (Grundfall, viermal) → G [Zeilen 2910–2911]
      „bei periodischen Vorgängen wie Schwingungen)“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · die Periode aus Beschreibung oder Diagramm angeben → G [Zeile 2907]
      „Periodizität) folgender“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Größt- und Kleinstwert einer Tabelle entnehmen → G [Zeile 2899]
      „Merkmalen (Definitionsbereich,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · Mittellinie und Amplitude daraus bestimmen → keine Stelle; „Amplitude“ und „Mittellinie“ kommen im Teil C nicht vor.
    - Sprosse 6 · aus Mittellinie, Amplitude und Periode die Gleichung aufstellen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 7 · Sachkontext, Gleichung und Graph einander zuordnen → G [Zeilen 2909–2911]
      „grafischer Form sowie Funktionsgleichung der bekannten Funktionen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · einen Funktionswert im Sachzusammenhang deuten → G [Zeilen 2910–2911]
      „bei periodischen Vorgängen wie Schwingungen)“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 9 · den Zeitpunkt des Größt- oder Kleinstwerts angeben → G [Zeilen 2904–2906]
      „Graphen (Streckung, Stauchung, Verschiebung), Symmetrie, ggf. Öffnungsrichtung, Scheitelpunkt,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 10 · eine Frage am Graphen mit Hilfslinien beantworten → G [Zeilen 2894–2896]
      „Darstellen von Zuordnungen und Funktionen (auch quadratische,“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 11 · beurteilen, wie gut das Modell passt, und die Grenzen benennen → keine Stelle; Die Grenzen eines Modells nennt der Teil C nicht.
    - Sprosse 12 · die vier Funktionstypen gegenüberstellen und den passenden auswählen → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 13 · unter drei Graphen den passenden ankreuzen und die anderen begründet ausschließen → G [Zeilen 2894–2896]
      „Gegenüberstellen der entsprechenden Eigenschaften der bekannten Funktionstypen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 14 · Prüfungshöhe: kein eigenes P10-Original; Zielmarke nach RLP G und LISUM-PH … → G [Zeilen 2910–2911]; Eintrag: Prüfungshöhe, Zielmarke
      „bei periodischen Vorgängen wie Schwingungen)“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 10, Mathematik: Trigonometrische Funktionen“ [Zeile 2664]
  - Beleg [Zeile 2665]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung“
  - Eine Reihe für alle Bildungsgänge mit dem Differenzierungshinweis (Zeile 2665); sie hat Blöcke auf G (Zeile 2670) und H (Zeile 2721). Die Gymnasialmarke steht innerhalb der Reihe an drei einzelnen Inhalten – Kosinusfunktion als verschobene Sinusfunktion (Zeile 2685), formelle Schreibweise der Null- und Extremstellen (Zeile 2687) und Einfluss des Parameters d (Zeile 2689). Für den Parameter c allein steht keine GYM-Marke; der Eintrag hat diese Unterscheidung am 11h berichtigt.
- Spanne: ja  – Die Einheiten 2, 3 und 4 liegen auf G, Einheit 1 (Bogenmaß) und die Vorratssprossen zu c, d und zur Kosinusform auf H; einzelne Sprossen greifen auf E zurück. Damit stehen Einheiten auf G und H und Sprossen auf F und darunter.
- Ermessen (5):
  - Einheit 1: der RLP nennt den Einheitskreis nur in der Bogenmaß-Zeile (H). Das Ablesen von Sinus- und Kosinuswerten am Kreis, die Vorzeichen in den Quadranten und die Umkehraufgabe haben keine Stelle – fünf der fünfzehn Sprossen tragen deshalb „keine Stelle“.
  - Die Wörter „Amplitude“, „Periodenlänge“, „Frequenz“ und „Sinuskurve“ kommen im Teil C nicht vor; die Sprossen dazu sind über „Einfluss der Parameter“ und „Periodizität“ (G) zugeordnet. Die Sprosse „Mittellinie und Amplitude bestimmen“ trägt „keine Stelle“.
  - Sprosse „Monotonie in einem Abschnitt beschreiben“: keine Stelle; die Merkmalsliste des RLP nennt die Monotonie nicht.
  - Sprosse „Sinus eines stumpfen Winkels“: keine Stelle, obwohl sie in drei P10-Originalen als Nebenleistung vorkommt (geführt in trigonometrie.md).
  - Die GYM-Marken des Eintrags für c und d stammen aus der Planungshilfe, nicht aus dem RLP; der RLP stuft beide gemeinsam auf H ein.

### wahrscheinlichkeit – Stufe D–E (Baumdiagramm und Pfadregeln G)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Daten und Zufall, Zählstrategien und Wahrscheinlichkeiten. C: „systematisches Durcharbeiten von Möglichkeiten und entsprechende Auswertung zu kombinatorischen Fragestellungen““
  - Zeile 6 (Verortung): „D: „systematisches Durcharbeiten und Begründen der Vollständigkeit einer Lösung bei kombinatorischen Fragestellungen (z. B. durch systematisches Aufzählen der Möglichkeiten)““
  - Zeile 6 (Verortung): „E: „… kombinatorischen Fragestellungen (auch mithilfe von Baumdiagrammen)“, „Angeben der Ergebnismenge““
  - Zeile 6 (Verortung): „G: „Nutzen von kombinatorischen Überlegungen zur Bestimmung der Art und Anzahl von Möglichkeiten in verschiedenen Kontexten zur Berechnung von Wahrscheinlichkeiten (mit und ohne Zurücklegen)““
  - Zeile 6 (Verortung): „H: „Bestimmen von Anzahlen mithilfe von Fakultäten und Binomialkoeffizienten““
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2019-OS-K6b]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D/E]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP E/G]“
  - Zeile 32 (Merkkasten): „[P10 2025-OS-K3b, 2026-FOR-K6a Fehlerquellen; RLP E „Begründen der Annahme der Gleichwahrscheinlichkeit“]“
  - Zeile 33 (Merkkasten): „[P10 2024-OS-K5b, 2014-OS-K6b, 2019-OS-K6b Fehlerquellen; RLP G]“
  - Zeile 44 (Merkkasten): „[RLP D]“
  - Zeile 54 (Merkkasten): „[RLP E]“
  - Zeile 62 (Merkkasten): „[RLP G]“
  - Zeile 70 (Merkkasten): „[RLP G]“
  - Zeile 85 (Typische Fehler): „[FD; RLP E „Begründen der Annahme der Gleichwahrscheinlichkeit“]“
  - Zeile 89 (Für schwache Schüler): „[RLP B/C, MO]“
- Lerneinheiten:
  - 1. Zählen und Ergebnismengen – C/D/E
    - C [Zeilen 3031–3032]: „systematisches Durcharbeiten von Möglichkeiten und entsprechende Auswertung“
      Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050); das Aufzählen steht schon auf C (Grundschule)
    - D [Zeilen 3047–3048]: „systematisches Durcharbeiten und Begründen der Vollständigkeit einer Lösung bei“
      Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050); die Begründung der Vollständigkeit auf D
    - E [Zeile 3128]: „Angeben der Ergebnismenge“
      Block 3125–3146, Niveaustufe am Block: E (Z3138); die Ergebnismenge auf E
  - 2. Wahrscheinlichkeit einstufig – E
    - E [Zeile 3138]: „Begründen der Annahme der Gleichwahrscheinlichkeit von“
      Block 3125–3146, Niveaustufe am Block: E (Z3138); die Regel von Laplace steht in derselben Zeile
    - E [Zeilen 3141–3142]: „Berechnen von Wahrscheinlichkeiten von Ereignissen mit der Summenregel“
      Block 3125–3146, Niveaustufe am Block: E (Z3138); die Summenregel auf E
  - 3. Baumdiagramm und Pfadregeln – G
    - G [Zeilen 3160–3161]: „unter Nutzung von Baumdiagrammen, Pfadregeln, Vierfeldertafeln,“
      Block 3158–3168, Niveaustufe am Block: G (Z3165); Baumdiagramm und Pfadregel stehen erst auf G; das deckt sich mit der Stufenangabe in index.md
  - 4. Ohne Zurücklegen – G
    - G [Zeilen 3158–3159]: „Nutzen von kombinatorischen Überlegungen zur Bestimmung der“
      Block 3158–3168, Niveaustufe am Block: G (Z3165); „mit und ohne Zurücklegen“ steht in derselben Zeile
    - G [Zeilen 3158–3159]: „Ermitteln von (auch bedingten) Wahrscheinlichkeiten (auch bei mehrstufigen Zufallsexperimenten,“
      Block 3158–3168, Niveaustufe am Block: G (Z3165); die bedingte Wahrscheinlichkeit als Kern des Ziehens ohne Zurücklegen
- Sprossen je Verfahrenstyp:
  - Zählen (Einheit 1)
    - Sprosse 1 · Möglichkeiten in Ordnung auflisten (Vorstufe) → C [Zeilen 3031–3032]; Eintrag: Vorstufe
      „systematisches Durcharbeiten von Möglichkeiten und entsprechende Auswertung“ – Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050)
    - Sprosse 2 · zweistufige Kombinationen zählen (4×) → C [Zeilen 3031–3032]
      „systematisches Durcharbeiten von Möglichkeiten und entsprechende Auswertung“ – Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050)
    - Sprosse 3 · Zählprinzip als Produkt → G [Zeilen 3158–3159]
      „Nutzen von kombinatorischen Überlegungen zur Bestimmung der“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 4 · Anordnungen von drei Dingen auflisten → D [Zeilen 3047–3048]
      „systematisches Durcharbeiten und Begründen der Vollständigkeit einer Lösung bei“ – Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050)
    - Sprosse 5 · Produkt der absteigenden Anzahlen → G [Zeilen 3158–3159]
      „Nutzen von kombinatorischen Überlegungen zur Bestimmung der“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 6 · größte und kleinste Zahl aus Ziffern → D [Zeilen 3047–3048]
      „systematisches Durcharbeiten und Begründen der Vollständigkeit einer Lösung bei“ – Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050)
    - Sprosse 7 · Ergebnismenge zweier Münzen oder Scheiben als geordnete Paare → E [Zeile 3128]
      „Angeben der Ergebnismenge“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 8 · Paare beim zweifachen Würfeln mit Bedingung → E [Zeile 3129]
      „Zusammenfassen von Ergebnissen bei Zufalls“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 9 · Dreiecke aus Punkten (Punkte auf einer Geraden streichen) → keine Stelle; Die geometrische Auswahlaufgabe nennt der Teil C nicht.
    - Sprosse 10 · Prüfungshöhe: Zahl der dreistelligen Nummern aus drei verschiedenen Ziffern … → G [Zeilen 3158–3159]; Eintrag: Prüfungshöhe
      „Nutzen von kombinatorischen Überlegungen zur Bestimmung der“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
  - Einstufig (Einheit 2)
    - Sprosse 1 · möglich und günstig unterstreichen (Vorstufe) → E [Zeile 3138]; Eintrag: Vorstufe
      „Begründen der Annahme der Gleichwahrscheinlichkeit von“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 2 · Würfel, ein Ergebnis (4×) → E [Zeile 3138]
      „Begründen der Annahme der Gleichwahrscheinlichkeit von“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 3 · Glücksrad mit gleich großen Feldern → E [Zeile 3129]
      „Zusammenfassen von Ergebnissen bei Zufalls“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 4 · Urne mit Anzahlen → E [Zeile 3138]
      „Begründen der Annahme der Gleichwahrscheinlichkeit von“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 5 · Ereignis mit mehreren günstigen Ergebnissen → E [Zeilen 3141–3142]
      „Berechnen von Wahrscheinlichkeiten von Ereignissen mit der Summenregel“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 6 · als Dezimalzahl und Prozent → E [Zeilen 1838–1839]
      „Beschreiben von Prozenten als weitere Darstellungsform für“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 7 · Gesamtzahl aus dem Text (Nieten plus Gewinne; Lose von … bis …) → keine Stelle; Das Erschließen der Grundmenge aus dem Text nennt der Teil C nicht.
    - Sprosse 8 · Gegenereignis („weder … noch“) → G [Zeile 3162]
      „Gegenwahrscheinlichkeiten und dem Urnenmodell“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 9 · Anzahl aus P und Gesamtzahl (Umkehrung) → H [Zeile 3177]
      „Nutzen von Wahrscheinlichkeiten zum Vorhersagen von“ – Block 3173–3178, Niveaustufe am Block: H (Z3176)
    - Sprosse 10 · Zufallsgerät entwerfen (Kugeln einzeichnen) → D [Zeile 3047]
      „zielgerichtetes Verändern von Bedingungen bei“ – Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050)
    - Sprosse 11 · veränderte Grundmenge → D [Zeile 3047]
      „zielgerichtetes Verändern von Bedingungen bei“ – Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050)
    - Sprosse 12 · relative Häufigkeit einer Versuchsreihe mit P vergleichen → E [Zeilen 3145–3146]
      „Vergleichen von theoretisch ermittelten Wahrscheinlichkeiten mit empirischen Beobachtungen“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 13 · Behauptung prüfen → E [Zeilen 3145–3146]
      „Vergleichen von theoretisch ermittelten Wahrscheinlichkeiten mit empirischen Beobachtungen“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 14 · Prüfungshöhe: Lose mit fester Endziffer als eingeschränkte Grundmenge … → E [Zeile 3138]; Eintrag: Prüfungshöhe
      „Begründen der Annahme der Gleichwahrscheinlichkeit von“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
  - Mit Zurücklegen (Einheit 3)
    - Sprosse 1 · mit oder ohne Zurücklegen ankreuzen (Vorstufe) → G [Zeilen 3160–3161]; Eintrag: Vorstufe
      „unter Nutzung von Baumdiagrammen, Pfadregeln, Vierfeldertafeln,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 2 · Baum für zwei Münzwürfe oder zwei Drehungen zeichnen (4×) → E [Zeile 3131]
      „Fragestellungen (auch mithilfe von“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 3 · Astwahrscheinlichkeiten ergänzen (Summe an jedem Punkt eins) → G [Zeilen 3160–3161]
      „unter Nutzung von Baumdiagrammen, Pfadregeln, Vierfeldertafeln,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 4 · Pfadregel für ein Ergebnis → G [Zeilen 3160–3161]
      „unter Nutzung von Baumdiagrammen, Pfadregeln, Vierfeldertafeln,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 5 · Summenregel für zwei Pfade → E [Zeilen 3141–3142]
      „Berechnen von Wahrscheinlichkeiten von Ereignissen mit der Summenregel“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 6 · „beide gleich“ (drei Pfade) → G [Zeilen 3160–3161]
      „unter Nutzung von Baumdiagrammen, Pfadregeln, Vierfeldertafeln,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 7 · „mindestens einmal“ über das Gegenereignis → G [Zeile 3162]
      „Gegenwahrscheinlichkeiten und dem Urnenmodell“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 8 · „nicht zweimal“ → G [Zeile 3162]
      „Gegenwahrscheinlichkeiten und dem Urnenmodell“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 9 · dreistufig → G [Zeilen 3158–3159]
      „Ermitteln von (auch bedingten) Wahrscheinlichkeiten (auch bei mehrstufigen Zufallsexperimenten,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 10 · Behauptung prüfen (P(22) = P(33)?) → E [Zeilen 3145–3146]
      „Vergleichen von theoretisch ermittelten Wahrscheinlichkeiten mit empirischen Beobachtungen“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 11 · Zufallsgerät zu vorgegebener Wahrscheinlichkeit belegen → D [Zeile 3047]
      „zielgerichtetes Verändern von Bedingungen bei“ – Block 3031–3053, Niveaustufe am Block: C (Z3039), D (Z3050)
    - Sprosse 12 · Prüfungshöhe: dreistufigen Baum beschriften und mindestens zwei Sechsen berechnen … → G [Zeilen 3158–3159]; Eintrag: Prüfungshöhe
      „Ermitteln von (auch bedingten) Wahrscheinlichkeiten (auch bei mehrstufigen Zufallsexperimenten,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
  - Ohne Zurücklegen (Einheit 4)
    - Sprosse 1 · Grundmenge nach dem ersten Zug angeben (Vorstufe) → G [Zeile 3162]; Eintrag: Vorstufe
      „Gegenwahrscheinlichkeiten und dem Urnenmodell“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 2 · zweimal Ziehen, ein Pfad (4×) → G [Zeilen 3158–3159]
      „Nutzen von kombinatorischen Überlegungen zur Bestimmung der“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 3 · Baum mit veränderten Ästen ergänzen → G [Zeilen 3160–3161]
      „unter Nutzung von Baumdiagrammen, Pfadregeln, Vierfeldertafeln,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 4 · zwei gleiche Farben (Summenregel) → E [Zeilen 3141–3142]
      „Berechnen von Wahrscheinlichkeiten von Ereignissen mit der Summenregel“ – Block 3125–3146, Niveaustufe am Block: E (Z3138)
    - Sprosse 5 · zweite Person zieht (erste Stufe mitrechnen) → G [Zeilen 3158–3159]
      „Ermitteln von (auch bedingten) Wahrscheinlichkeiten (auch bei mehrstufigen Zufallsexperimenten,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 6 · dreistufig, ein Pfad → G [Zeilen 3158–3159]
      „Ermitteln von (auch bedingten) Wahrscheinlichkeiten (auch bei mehrstufigen Zufallsexperimenten,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 7 · dreistufig, Baum mit leeren Feldern → G [Zeilen 3160–3161]
      „unter Nutzung von Baumdiagrammen, Pfadregeln, Vierfeldertafeln,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 8 · „unter den ersten drei“ (Summe oder Gegenereignis) → G [Zeile 3162]
      „Gegenwahrscheinlichkeiten und dem Urnenmodell“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 9 · Vergleich mit Zurücklegen → G [Zeilen 3158–3159]
      „Nutzen von kombinatorischen Überlegungen zur Bestimmung der“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 10 · Behauptung prüfen („doppelt so hoch“?) → G [Zeile 3163]
      „Interpretieren von Wahrscheinlichkeitsaussagen aus dem“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
    - Sprosse 11 · Prüfungshöhe: Ergebnisse aufzählen, zwei gleiche Füllungen berechnen, Ereignis in Worten … → G [Zeilen 3158–3159]; Eintrag: Prüfungshöhe
      „Ermitteln von (auch bedingten) Wahrscheinlichkeiten (auch bei mehrstufigen Zufallsexperimenten,“ – Block 3158–3168, Niveaustufe am Block: G (Z3165)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Daten und Zufall“ [Zeile 1454]; „Jahrgangsstufe 9/10, Mathematik: Daten und Zufall“ [Zeile 2246]
  - Beleg [Zeile 1455]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung“
  - Beide Reihen führen EBR, FOR und GYM gemeinsam und tragen den Differenzierungshinweis (Zeilen 1455 und 2248). Die Reihe 7/8 deckt die einstufigen Experimente ab, die Reihe 9/10 die mehrstufigen (Blöcke auf G, Zeile 2254, und H, Zeile 2318).
- Spanne: ja  – Das Zählen und die einstufige Wahrscheinlichkeit liegen auf C, D und E; Baumdiagramm, Pfadregeln, Gegenwahrscheinlichkeit und das Ziehen ohne Zurücklegen erst auf G, die Umkehrung aus der Wahrscheinlichkeit auf H. Damit stehen Einheiten auf G und Sprossen auf H und auf F und darunter.
- Ermessen (5):
  - Einheit 3 und 4 im Ganzen: Baumdiagramm, Pfadregel und das Ziehen ohne Zurücklegen stehen im Teil C erst auf G, obwohl die P10 sie in jedem Jahrgang prüft und index.md das Thema als D–E führt (mit dem Zusatz „Baumdiagramm und Pfadregeln G“).
  - Sprosse „Dreiecke aus Punkten“ (Einheit 1): keine Stelle; die geometrische Auswahlaufgabe nennt der Teil C nicht.
  - Sprosse „Gesamtzahl aus dem Text“ (Einheit 2): keine Stelle; das Erschließen der Grundmenge aus einem Sachtext steht nicht im Plan.
  - Sprosse „Anzahl aus P und Gesamtzahl“ liegt auf H („Nutzen von Wahrscheinlichkeiten zum Vorhersagen von relativen und absoluten Häufigkeiten“), während die übrige Kette auf E steht.
  - Die Wörter „Pfadregel“ und „Gegenereignis“ kommen im Teil C nur in der G-Zeile vor; der Katalog verwendet sie schon in Einheit 2.

### winkel-dreiecke – Stufe D–E
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Größen und Messen D: „Unterscheiden verschiedener Größen (auch Flächeninhalt, Volumen und Winkel)““
  - Zeile 6 (Verortung): „E: „Beschreiben weiterer Eigenschaften der Dreiecksarten (z. B. Symmetrie)“, „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren (auch Innenwinkelsumme von Vielecken)““
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP C/D „Zeichnen … mithilfe von Zeichengeräten“]“
  - Zeile 29 (Voraussetzungen (Blatt 0)): „[RLP C „Beschreiben der Beziehungen zwischen Vierecken“; LS-AA Kl. 5 II 5]“
  - Zeile 30 (Voraussetzungen (Blatt 0)): „[RLP D „Zeichnen ebener Figuren … Zirkel“]“
  - Zeile 32 (Merkkasten): „[RLP D „Systematisieren von Winkeln“]“
  - Zeile 33 (Merkkasten): „[RLP D „Erklären und Nutzen verschiedener Skalen“]“
  - Zeile 34 (Merkkasten): „[RLP D; P10 2020-OS-B1g, 2015-OS-B1d]“
  - Zeile 36 (Merkkasten): „[RLP D „Systematisieren von Dreiecken“; P10 2023-OS-B1g]“
  - Zeile 38 (Merkkasten): „[RLP E; LS-AA Kl. 7 V 3]“
  - Zeile 39 (Merkkasten): „[RLP E „Beschreiben besonderer Linien“]“
  - Zeile 49 (Merkkasten): „[RLP D]“
  - Zeile 58 (Merkkasten): „[RLP D]“
  - Zeile 67 (Typische Fehler): „[RLP D/E]“
  - Zeile 76 (Typische Fehler): „[RLP E]“
  - Zeile 85 (Typische Fehler): „[RLP E]“
  - Zeile 106 (Für schwache Schüler): „[RLP D, MO]“
- Lerneinheiten:
  - 1. Winkel messen und zeichnen – D
    - D [Zeilen 2126–2127]: „Messen von Größen (auch von Volumina sowie von spitzen, gestreckten und stumpfen“
      Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155); Grundfall, Themenbereich Größen und Messen
    - D [Zeilen 2444–2446]: „Zeichnen von Winkeln und ebenen Figuren mithilfe von Zeichengeräten (Lineal,“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Zeichnen, Themenbereich Raum und Form
  - 2. Winkel an Geradenkreuzungen und Parallelen – D
    - D [Zeilen 2441–2444]: „Beschreiben von Winkelbeziehungen an geschnittenen Geraden bzw. Parallelen sowie in Dreiecken (Scheitelwinkel,“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); der RLP nennt Scheitel-, Neben-, Stufen- und Innenwinkel, nicht den Wechselwinkel
  - 3. Winkelsummen, Dreiecke und Vierecke – D/E
    - E [Zeilen 2459–2461]: „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); mit dem Zusatz „auch Innenwinkelsumme von Vielecken“
    - D [Zeilen 2456–2458]: „Systematisieren von Winkeln bzw. von Dreiecken nach Winkelgrößen und Seitenlängen“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); die Dreiecksarten stehen schon auf D
  - 4. Dreiecke konstruieren – E
    - E [Zeilen 2484–2485]: „Konstruieren von Dreiecken nach den Kongruenzsätzen“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Grundfall
    - E [Zeilen 2470–2472]: „Nutzen von Lage- und Größenbeziehungen zum Formulieren von Aussagen zur“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Lösbarkeit der Konstruktion, Dreiecksungleichung
  - 5. Besondere Linien im Dreieck und Satz des Thales – E
    - E [Zeilen 2481–2483]: „Konstruieren von Mittelsenkrechten, Höhen und Seitenhalbierenden in Dreiecken“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Grundfall; Winkelhalbierende, Umkreis und Inkreis nennt der RLP nicht
    - E [Zeilen 2464–2467]: „Beschreiben von Lage- und Größenbeziehungen geometrischer Objekte (auch unter Nutzung des Satzes von“
      Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470); Satz des Thales
- Sprossen je Verfahrenstyp:
  - Winkel messen (Einheit 1)
    - Sprosse 1 · Winkelart ankreuzen (Vorstufe) → D [Zeilen 2456–2458]; Eintrag: Vorstufe
      „Systematisieren von Winkeln bzw. von Dreiecken nach Winkelgrößen und Seitenlängen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · spitze Winkel messen (4×) → D [Zeilen 2126–2127]
      „Messen von Größen (auch von Volumina sowie von spitzen, gestreckten und stumpfen“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 3 · stumpfe Winkel (große Skala) → D [Zeile 2132]
      „Erklären und Nutzen verschiedener Skalen“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 4 · Winkel mit gegebener Größe zeichnen → D [Zeilen 2444–2446]
      „Zeichnen von Winkeln und ebenen Figuren mithilfe von Zeichengeräten (Lineal,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 5 · über den gestreckten Winkel hinaus (Rest zum Vollwinkel) → D [Zeilen 2126–2127]
      „Messen von Größen (auch von Volumina sowie von spitzen, gestreckten und stumpfen“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 6 · Winkel benennen (∠ASB, α) → keine Stelle; Die Schreibweise ∠ASB und die griechischen Buchstaben nennt der Teil C nicht.
    - Sprosse 7 · Teilwinkel addieren → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 8 · Teilwinkel abziehen → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 9 · Teilstrecken addieren und abziehen (Einheiten) → D [Zeile 2173]
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
    - Sprosse 10 · Prüfungshöhe: Winkel zwischen zwei Sichtlinien als Differenz; Weg aus zwei Teilstrecken … → D [Zeile 2173]; Eintrag: Prüfungshöhe
      „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln und“ – Block 2170–2184, Niveaustufe am Block: D (Z2184)
  - Winkel an Geraden (Einheit 2)
    - Sprosse 1 · Winkelpaar benennen (Vorstufe) → D [Zeilen 2441–2444]; Eintrag: Vorstufe
      „Beschreiben von Winkelbeziehungen an geschnittenen Geraden bzw. Parallelen sowie in Dreiecken (Scheitelwinkel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · Scheitelwinkel angeben (4×) → D [Zeilen 2441–2444]
      „Beschreiben von Winkelbeziehungen an geschnittenen Geraden bzw. Parallelen sowie in Dreiecken (Scheitelwinkel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 3 · Nebenwinkel (Rest zum gestreckten Winkel) → D [Zeile 2445]
      „Nebenwinkel, Stufenwinkel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 4 · alle vier Winkel einer Kreuzung aus einem → D [Zeilen 2441–2444]
      „Beschreiben von Winkelbeziehungen an geschnittenen Geraden bzw. Parallelen sowie in Dreiecken (Scheitelwinkel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 5 · Teilwinkel an der Kreuzung (Scheitelwinkel minus Teil) → D [Zeilen 2441–2444]
      „Beschreiben von Winkelbeziehungen an geschnittenen Geraden bzw. Parallelen sowie in Dreiecken (Scheitelwinkel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 6 · Stufenwinkel an Parallelen → D [Zeile 2445]
      „Nebenwinkel, Stufenwinkel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 7 · Wechselwinkel → keine Stelle; Den Wechselwinkel nennt der RLP nicht; die Aufzählung endet mit Scheitel-, Neben-, Stufen- und Innenwinkel.
    - Sprosse 8 · Nebenwinkel des Stufenwinkels → D [Zeile 2445]
      „Nebenwinkel, Stufenwinkel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 9 · Winkel an verlängerten Seiten mit überflüssiger Angabe → keine Stelle; Aufgabenform mit Distraktor; der RLP nennt sie nicht.
    - Sprosse 10 · Parallelogramm und Trapez → E [Zeilen 2459–2461]
      „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 11 · Prüfungshöhe: Winkel an zwei geschnittenen Parallelen; Nachbarwinkel im Parallelogramm … → D [Zeilen 2441–2444]; Eintrag: Prüfungshöhe
      „Beschreiben von Winkelbeziehungen an geschnittenen Geraden bzw. Parallelen sowie in Dreiecken (Scheitelwinkel,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
  - Winkelsumme (Einheit 3)
    - Sprosse 1 · Dreiecksart markieren (Vorstufe) → D [Zeilen 2456–2458]; Eintrag: Vorstufe
      „Systematisieren von Winkeln bzw. von Dreiecken nach Winkelgrößen und Seitenlängen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · dritter Winkel mit ganzen Graden (4×) → E [Zeilen 2459–2461]
      „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 3 · Dezimalgrade → E [Zeile 2202]
      „Angeben von Rechenergebnissen in sinnvoller Genauigkeit“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 4 · gleichschenklig aus dem Basiswinkel → E [Zeilen 2462–2464]
      „Beschreiben weiterer Eigenschaften der Dreiecksarten“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 5 · gleichseitig → E [Zeilen 2462–2464]
      „Beschreiben weiterer Eigenschaften der Dreiecksarten“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 6 · rechtwinklig (zwei spitze Winkel) → E [Zeilen 2459–2461]
      „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 7 · Viereck mit Winkelsumme Vollwinkel → E [Zeile 2462]
      „(auch Innenwinkelsumme von“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 8 · Winkel im Teildreieck (Höhe, Diagonale) → E [Zeilen 2459–2461]
      „Untersuchen und Beschreiben der Größenbeziehungen in ebenen geometrischen Figuren“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 9 · gleichschenklig erkennen und Seite angeben → E [Zeilen 2462–2464]
      „Beschreiben weiterer Eigenschaften der Dreiecksarten“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 10 · rechten Winkel begründen (zwei Basiswinkel 45°) → H [Zeilen 2573–2575]
      „Begründen der Eigenschaften von geometrischen Objekten mithilfe von Symmetrie,“ – Block 2573–2581, Niveaustufe am Block: H (Z2577)
    - Sprosse 11 · Vierecks-Eigenschaft ankreuzen → C [Zeilen 2370–2371]
      „Beschreiben der Beziehungen zwischen Vierecken“ – Block 2306–2375, Niveaustufe am Block: A (Z2314), B (Z2330), C (Z2357)
    - Sprosse 12 · Prüfungshöhe: Dreieck mit zwei gleichen Basiswinkeln; Begründung im Drachenviereck … → H [Zeilen 2573–2575]; Eintrag: Prüfungshöhe
      „Begründen der Eigenschaften von geometrischen Objekten mithilfe von Symmetrie,“ – Block 2573–2581, Niveaustufe am Block: H (Z2577)
  - Konstruieren (Einheit 4)
    - Sprosse 1 · Kongruenzsatz ankreuzen (Vorstufe) → E [Zeilen 2484–2485]; Eintrag: Vorstufe
      „Konstruieren von Dreiecken nach den Kongruenzsätzen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · SSS mit ganzen Zentimetern (4×) → E [Zeilen 2484–2485]
      „Konstruieren von Dreiecken nach den Kongruenzsätzen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 3 · SWS → E [Zeilen 2484–2485]
      „Konstruieren von Dreiecken nach den Kongruenzsätzen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 4 · WSW → E [Zeilen 2484–2485]
      „Konstruieren von Dreiecken nach den Kongruenzsätzen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 5 · SsW → E [Zeilen 2484–2485]
      „Konstruieren von Dreiecken nach den Kongruenzsätzen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 6 · gleichschenkliges Dreieck aus Basis und Schenkel → E [Zeilen 2484–2485]
      „Konstruieren von Dreiecken nach den Kongruenzsätzen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 7 · rechtwinkliges Dreieck aus den Katheten → E [Zeilen 2484–2485]
      „Konstruieren von Dreiecken nach den Kongruenzsätzen“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 8 · Konstruktionsbeschreibung → keine Stelle; Die Konstruktionsbeschreibung als Textform nennt der Teil C nicht.
    - Sprosse 9 · konstruierbar oder nicht (Dreiecksungleichung) → E [Zeilen 2470–2472]
      „Nutzen von Lage- und Größenbeziehungen zum Formulieren von Aussagen zur“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 10 · kongruente Figuren zuordnen → E [Zeilen 2515–2516]
      „Erkennen und Benennen kongruenter und ähnlicher ebener geometrischer Objekte anhand“ – Block 2515–2520, Niveaustufe am Block: kein Buchstabe
    - Sprosse 11 · Prüfungshöhe: Dreiecksungleichung als Ankreuzaufgabe; Konstruktion nach WSW … → E [Zeilen 2470–2472]; Eintrag: Prüfungshöhe
      „Nutzen von Lage- und Größenbeziehungen zum Formulieren von Aussagen zur“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
  - Besondere Linien (Einheit 5)
    - Sprosse 1 · Linie ankreuzen (Vorstufe) → E [Zeilen 2470–2472]; Eintrag: Vorstufe
      „Beschreiben besonderer Linien in Dreiecken und Körpern (z. B. Höhe,“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 2 · Mittelsenkrechte einer Strecke (4×) → E [Zeilen 2481–2483]
      „Konstruieren von Mittelsenkrechten, Höhen und Seitenhalbierenden in Dreiecken“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 3 · Umkreis eines spitzwinkligen Dreiecks → keine Stelle; Den Umkreis nennt der Teil C nicht.
    - Sprosse 4 · Winkelhalbierende → keine Stelle; Die Winkelhalbierende fehlt in der Aufzählung der besonderen Linien (Höhe, Seitenhalbierende, Mittelsenkrechte).
    - Sprosse 5 · Inkreis → keine Stelle; Den Inkreis nennt der Teil C nicht.
    - Sprosse 6 · Höhe im spitzwinkligen, dann im stumpfwinkligen Dreieck → E [Zeilen 2481–2483]
      „Konstruieren von Mittelsenkrechten, Höhen und Seitenhalbierenden in Dreiecken“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 7 · Seitenhalbierende und Schwerpunkt → E [Zeilen 2481–2483]
      „Konstruieren von Mittelsenkrechten, Höhen und Seitenhalbierenden in Dreiecken“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 8 · Thaleskreis zeichnen und rechtwinkliges Dreieck einzeichnen → E [Zeilen 2464–2467]
      „Beschreiben von Lage- und Größenbeziehungen geometrischer Objekte (auch unter Nutzung des Satzes von“ – Block 2434–2485, Niveaustufe am Block: D (Z2448), E (Z2470)
    - Sprosse 9 · rechten Winkel mit Thales begründen → H [Zeilen 2573–2575]
      „Begründen der Eigenschaften von geometrischen Objekten mithilfe von Symmetrie,“ – Block 2573–2581, Niveaustufe am Block: H (Z2577)
    - Sprosse 10 · Prüfungshöhe: Begründen, dass ein Winkel 90° ist, über Thales oder Teildreiecke … → H [Zeilen 2573–2575]; Eintrag: Prüfungshöhe
      „Begründen der Eigenschaften von geometrischen Objekten mithilfe von Symmetrie,“ – Block 2573–2581, Niveaustufe am Block: H (Z2577)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7/8, Mathematik: Geometrie“ [Zeile 1120]
  - Beleg [Zeile 1121]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: ja  – Die Einheiten liegen auf C, D und E; das Begründen von Eigenschaften über Winkelsätze und den Satz des Thales steht dagegen auf H (Sprossen 10 und 12 der Einheit 3, Sprossen 9 und 10 der Einheit 5). Damit liegen Sprossen auf H und Einheiten auf F und darunter.
- Ermessen (5):
  - Sprosse „Wechselwinkel“ (Einheit 2): keine Stelle. Die Aufzählung des RLP endet mit Scheitel-, Neben-, Stufen- und Innenwinkel.
  - Sprossen „Umkreis“, „Winkelhalbierende“ und „Inkreis“ (Einheit 5): keine Stelle. Der RLP zählt als besondere Linien nur Höhe, Seitenhalbierende und Mittelsenkrechte auf.
  - Sprossen „Winkel benennen (∠ASB, α)“, „Konstruktionsbeschreibung“, „Winkel an verlängerten Seiten mit überflüssiger Angabe“: keine Stelle; alle drei sind Schreib- oder Aufgabenformen.
  - Die Begründungssprossen liegen auf H, während das Verwenden derselben Sätze auf D und E steht – der RLP trennt Verwenden und Begründen um mehrere Stufen. Das ist der Grund für die Spanne dieses Eintrags.
  - Kleine Abweichung: der Eintrag ordnet „Berechnen von Größenangaben (auch von Flächeninhalten, Volumina und Winkeln …)“ der Stufe E zu; im Quelltext steht die Zeile im Block 2170–2184, dessen Buchstabe am Rand D ist (Zeile 2184).

### zinsrechnung – Stufe F (Zinsen in der Prozentrechnungs-Zeile); Zinseszins in keiner RLP-Stufe (nur Lehrwerk Kl. 7 III 6 und LISUM-Planungshilfe Kl. 8)
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] Zahlen und Operationen F (S. 43, Rechenverfahren): „Nutzen, Darstellen und Beschreiben von Strategien und Gesetzen bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe von digitalen Mathematikwerkzeugen)““
  - Zeile 20 (Voraussetzungen (Blatt 0)): „[RLP E „Nutzen von Prozentsätzen als Operatoren“; P10 2015-OS-B1e Verfahren „Kapital mal Zinssatz als Dezimalzahl“]“
  - Zeile 21 (Voraussetzungen (Blatt 0)): „[RLP E; P10 2014-OS-B1e Fehlerquelle „Komma verschoben“]“
  - Zeile 22 (Voraussetzungen (Blatt 0)): „[RLP E „Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“]“
  - Zeile 23 (Voraussetzungen (Blatt 0)): „[RLP F; P10 2018-OS-K2c Muster „mal 1,08 je Jahr“; LISUM-PH Hinweis Operatormethode → Wachstumsfaktor]“
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[RLP D/E; P10 2014-OS-K3b Cent-Beträge in der Tabelle]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D/E; MSK S5A]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D; P10 2014-OS-K3a, 2014-OS-K3b Material Tabelle]“
  - Zeile 42 (Merkkasten): „[RLP F]“
- Lerneinheiten:
  - 1. Jahreszins, Monats- und Tageszins – E/F
    - F [Zeilen 1975–1976]: „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“
      Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992); die einzige Stelle des Teils C, die das Wort „Zinsen“ nennt
    - E [Zeile 1916]: „Nutzen von Prozentsätzen als Operatoren“
      Block 1897–1916, Niveaustufe am Block: E (Z1907); Grundfall: Zinsen als Prozentwert des Kapitals
  - 2. Zinseszins und Guthabentabelle – G/H
    - G [Zeilen 2908–2910]: „bei Wachstums- und Zerfallsprozessen“
      Block 2891–2918, Niveaustufe am Block: G (Z2907); der Zinseszins als Wachstumsprozess; das Wort „Zinseszins“ kommt im Teil C nicht vor
    - H [Zeile 2865]: „Prozentdarstellungen, Potenzen, Wurzeln,“
      Block 2860–2880, Niveaustufe am Block: H (Z2875); Terme mit Prozentdarstellungen und Potenzen – die Form K · qⁿ und das Rückwärtsrechnen über den Logarithmus
      Ermessen: Der RLP hat keine Zeile zum Zinseszins. Beide Stellen sind Zuordnungen nach Inhalt: das Modellieren von Wachstumsprozessen (G) und die Terme mit Prozentdarstellungen, Potenzen und Logarithmen (H). Der Eintrag selbst stellt in der Verortung fest, dass der Zinseszins Lehrwerks- und Planungshilfen-Stoff ohne RLP-Zeile ist.
- Sprossen je Verfahrenstyp:
  - Zinsen berechnen (Einheit 1)
    - Sprosse 1 · „was ist was“ und „Zinsen oder Guthaben“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Jahreszinsen aus Kapital und glattem Zinssatz: Prozentsatz als Dezimalzahl mal Kapital (4×) → E [Zeile 1916]
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 3 · Jahreszinsen mit dem 1 %-Weg (ein Prozent, dann mal p) → E [Zeile 1899]
      „auch Dreisatz und“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 4 · Guthaben nach einem Jahr: Kapital plus Zinsen → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 5 · Zinssatz aus Zinsen und Kapital, Ergebnis als Prozent mit Komma → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 6 · Zinssatz mit Dezimalstelle (zwei Komma drei Prozent) → E [Zeilen 1909–1910]
      „Angeben von Ergebnissen mit sinnvoller Genauigkeit (auch beim Rechnen mit rationalen“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 7 · Kapital aus Zinsen und Zinssatz (1 %-Weg rückwärts) → E [Zeilen 1838–1840]
      „Beschreiben der Beziehung zwischen Prozentsatz, Prozentwert und Grundwert“ – Block 1838–1860, Niveaustufe am Block: E (Z1850)
    - Sprosse 8 · Nachweis: stimmt der Zinssatz in der Tabelle → F [Zeilen 1981–1982]
      „Zahlen (auch im Zusammenhang mit der Prozentrechnung)“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 9 · Zinsen für mehrere Jahre ohne Zinseszins (Jahreszins mal Jahre) → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 10 · Kredit: Zinsen als Kosten, Rückzahlung → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 11 · zwei Angebote vergleichen → keine Stelle; Das Abwägen zweier Angebote nennt der RLP im Teil C nicht als eigene Handlung.
    - Sprosse 12 · Prüfungshöhe: Jahreszinsen, Zinssatz und Tabellennachweis als Kurzantworten … → F [Zeilen 1975–1976]; Eintrag: Prüfungshöhe
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
  - Monats- und Tageszinsen (Einheit 1)
    - Sprosse 1 · „ein Jahr oder kürzer“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Jahreszinsen zuerst, dann durch zwölf, mal Anzahl der Monate (4×) → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 3 · Tageszinsen: durch dreihundertsechzig, mal Anzahl der Tage → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 4 · Laufzeit aus zwei Daten zählen (Monat mit dreißig Tagen) → keine Stelle; Das Bankjahr mit 360 Tagen ist eine Konvention der Zinsrechnung; der RLP nennt sie nicht.
    - Sprosse 5 · Zinssatz oder Kapital bei gegebenen Monatszinsen (Vorrat) → F [Zeilen 1975–1976]; Eintrag: Vorrat
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 6 · Prüfungshöhe: kein P10-Original; Zielmarke nach RLP F und LISUM-PH Block ② … → F [Zeilen 1975–1976]; Eintrag: Prüfungshöhe, Zielmarke
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
  - Zinseszins (Einheit 2)
    - Sprosse 1 · „vom Start oder vom neuen Guthaben“ und „plus oder mal“ ankreuzen (Vorstufe) → keine Stelle; Vorstufe; keine eigene Handlung im RLP.; Eintrag: Vorstufe
    - Sprosse 2 · Zinsen ans Guthaben anhängen, neues Guthaben nach einem Jahr (4×) → F [Zeilen 1975–1976]
      „bei der Prozentrechnung (auch im Zusammenhang mit Rabatt und Zinsen, auch mithilfe“ – Block 1971–1999, Niveaustufe am Block: F (Z1978), G (Z1992)
    - Sprosse 3 · Zinsen im zweiten Jahr vom neuen Guthaben, zwei Jahre Schritt für Schritt → keine Stelle; Der Zinseszins hat im Teil C keine Zeile; das wiederholte Verzinsen wird nicht genannt.
    - Sprosse 4 · Guthabentabelle mit den Spalten Zinsen, Einzahlung, Guthaben um eine Zeile fortschreiben → keine Stelle; keine Stelle: die Guthabentabelle ist Lehrwerks- und Planungshilfenform.
    - Sprosse 5 · zwei fehlende Felder in einer gegebenen Tabelle, Kontrolle über die nächste Zeile → keine Stelle; wie Sprosse 4: keine Stelle.
    - Sprosse 6 · Wachstumsfaktor: mal q in einem Schritt statt plus p % → E [Zeile 1916]
      „Nutzen von Prozentsätzen als Operatoren“ – Block 1897–1916, Niveaustufe am Block: E (Z1907)
    - Sprosse 7 · Endkapital nach n Jahren mit q hoch n und dem Taschenrechner → G [Zeilen 2908–2910]
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 8 · einfache Zinsen und Zinseszins nebeneinander, Unterschied in Euro → keine Stelle; keine Stelle; der Vergleich beider Verzinsungsarten steht im Teil C nicht.
    - Sprosse 9 · Zinsen insgesamt: Endkapital minus Startkapital → keine Stelle; keine Stelle.
    - Sprosse 10 · Startkapital oder Laufzeit rückwärts (Vorrat) → H [Zeile 2865]; Eintrag: Vorrat
      „Prozentdarstellungen, Potenzen, Wurzeln,“ – Block 2860–2880, Niveaustufe am Block: H (Z2875)
    - Sprosse 11 · Prüfungshöhe: Guthabentabelle ergänzen; Endkapital mit K · qⁿ … → G [Zeilen 2908–2910]; Eintrag: Prüfungshöhe
      „bei Wachstums- und Zerfallsprozessen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 8, Mathematik: Zinsrechnung“ [Zeile 980]
  - Beleg [Zeile 981]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: ja  – Einheit 1 liegt auf E und F, Einheit 2 auf G (Wachstumsprozesse) und H (Terme mit Potenzen und Logarithmen). Damit steht mindestens eine Einheit auf G oder H und mindestens eine auf F oder darunter.
- Ermessen (4):
  - Einheit 2 im Ganzen: „Zinseszins“, „Kapital“ und „Zinssatz“ kommen im Teil C nicht vor. Die Stufen G und H sind über den Inhalt zugeordnet (Modellieren von Wachstumsprozessen; Terme mit Prozentdarstellungen, Potenzen und Logarithmen), nicht über eine wörtliche Tabellenzeile.
  - Sprossen 3, 4, 5, 8 und 9 der Kette Zinseszins: keine Stelle. Das schrittweise Fortschreiben einer Guthabentabelle ist Lehrwerks- und Planungshilfenform ohne RLP-Zeile.
  - Sprosse „Laufzeit aus zwei Daten zählen“: keine Stelle; das Bankjahr mit 360 Tagen ist eine Konvention der Zinsrechnung.
  - Sprosse „zwei Angebote vergleichen“: keine Stelle; das Abwägen zweier Angebote steht als Handlung nicht im Teil C.

### zuordnungen – Stufe D–E
- Verortung, [RLP]-Klammern mit Niveaustufe: 
  - Zeile 6 (Verortung): „[RLP] D: „Beschreiben der Eigenschaften direkt proportionaler Zusammenhänge und Abgrenzung von Eigenschaften anderer Zuordnungen (auch in Alltagssituationen)““
  - Zeile 6 (Verortung): „E: „Beschreiben, Analysieren, Interpretieren und Vergleichen von Eigenschaften von Zuordnungen und Unterscheidung zwischen direkt und indirekt proportionalen Zuordnungen (auch in Alltagssituationen)““
  - Zeile 24 (Voraussetzungen (Blatt 0)): „[MSK S5A Diagnose, RLP D]“
  - Zeile 25 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 26 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 27 (Voraussetzungen (Blatt 0)): „[RLP D]“
  - Zeile 41 (Merkkasten): „[RLP D]“
  - Zeile 59 (Typische Fehler): „[RLP E]“
- Lerneinheiten:
  - 1. Zuordnungen darstellen – D/E
    - D [Zeilen 2783–2784]: „Darstellen von Zuordnungen, insbesondere direkt“
      Block 2780–2791, Niveaustufe am Block: D (Z2788); Grundfall: erster Quadrant
    - E [Zeilen 2795–2797]: „Darstellen von Zuordnungen im Koordinatensystem (auch 4 Quadranten)“
      Block 2795–2806, Niveaustufe am Block: E (Z2803); vier Quadranten erst auf E
    - D [Zeilen 2789–2791]: „Wechsel zwischen verschiedenen Darstellungen von Zuordnungen“
      Block 2780–2791, Niveaustufe am Block: D (Z2788); Wechsel zwischen Tabelle, Graph, Wort und Formel
  - 2. Proportionale Zuordnungen und Dreisatz – D
    - D [Zeilen 2783–2786]: „Ermitteln von Größen in anwendungsbezogenen, direkt proportionalen Zusammenhängen“
      Block 2780–2791, Niveaustufe am Block: D (Z2788); Grundfall
    - D [Zeilen 2787–2788]: „(inhaltlich und durch Rechnen mit Dreisatz)“
      Block 2780–2791, Niveaustufe am Block: D (Z2788); der Dreisatz wird ausdrücklich genannt
  - 3. Antiproportionale Zuordnungen – E
    - E [Zeilen 2799–2800]: „Unterscheidung zwischen direkt und indirekt proportionalen“
      Block 2795–2806, Niveaustufe am Block: E (Z2803); der RLP schreibt „indirekt proportional“, der Katalog „antiproportional“
  - 4. Zuordnungstypen erkennen und anwenden – E
    - E [Zeilen 2795–2798]: „Beschreiben, Analysieren, Interpretieren und Vergleichen von Eigenschaften von Zuordnungen und“
      Block 2795–2806, Niveaustufe am Block: E (Z2803); Grundfall
    - E [Zeilen 2795–2797]: „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“
      Block 2795–2806, Niveaustufe am Block: E (Z2803); Sachaufgaben mit Rate
- Sprossen je Verfahrenstyp:
  - Darstellen (Einheit 1)
    - Sprosse 1 · Wertepaare aus einem Satz in eine leere Wertetabelle eintragen (Vorstufe, Blatt 0) → D [Zeilen 2789–2791]; Eintrag: Vorstufe, Blatt 0
      „Wechsel zwischen verschiedenen Darstellungen von Zuordnungen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 2 · Punkte einer fertigen Tabelle in ein vorgegebenes Koordinatensystem eintragen (4×) → D [Zeilen 2783–2784]
      „Darstellen von Zuordnungen, insbesondere direkt“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 3 · Werte aus einem fertigen Graphen ablesen → D [Zeilen 2789–2791]
      „Wechsel zwischen verschiedenen Darstellungen von Zuordnungen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 4 · Punkte auf einer gröberen Skala eintragen → G [Zeilen 2902–2903]
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 5 · entscheiden und begründen, ob die Punkte verbunden werden dürfen → keine Stelle; Die Frage, ob Punkte verbunden werden dürfen, steht in der Planungshilfe, nicht im Teil C.; Eintrag: LISUM-PH Jg. 7
    - Sprosse 6 · Zuordnung in Worten beschreiben und zu einer Situation den passenden Graphen wählen → D [Zeilen 2789–2791]
      „Wechsel zwischen verschiedenen Darstellungen von Zuordnungen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 7 · Fehler finden: Achsen vertauscht, Punkt auf der falschen Achse abgetragen → keine Stelle; Fehlerquelle des Unterrichts; der RLP nennt sie nicht.
    - Sprosse 8 · Prüfungshöhe: Wertetabelle in ein Koordinatensystem mit grober Skala eintragen … → D [Zeilen 2783–2784]; Eintrag: Prüfungshöhe
      „Darstellen von Zuordnungen, insbesondere direkt“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
  - Achseneinteilung (Einheit 1)
    - Sprosse 1 · an einem fertigen Koordinatensystem ablesen, wie viel ein Kästchen wert ist (Vorstufe) → keine Stelle; Das Ablesen der Skaleneinheit nennt der Teil C nicht.; Eintrag: Vorstufe, Blatt 0
    - Sprosse 2 · unter zwei angebotenen Einteilungen die passende ankreuzen (4×) → G [Zeilen 2902–2903]
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 3 · für eine Tabelle mit kleinen Werten selbst eine Einteilung wählen und beschriften → G [Zeilen 2902–2903]
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 4 · Kästchen abzählen und prüfen, ob der größte Tabellenwert noch ins Raster passt → keine Stelle; Zeichentechnik; der RLP nennt sie nicht.
    - Sprosse 5 · Einteilung für eine Achse mit großen Werten wählen → G [Zeilen 2902–2903]
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
    - Sprosse 6 · beide Achsen mit Größe und Einheit beschriften → keine Stelle; Die Achsenbeschriftung steht in der Planungshilfe, nicht im Teil C.; Eintrag: LISUM-PH Jg. 7
    - Sprosse 7 · Prüfungshöhe: ein Koordinatensystem ohne Skala selbst einteilen und beschriften … → G [Zeilen 2902–2903]; Eintrag: Prüfungshöhe
      „Einteilungen der Koordinatenachsen“ – Block 2891–2918, Niveaustufe am Block: G (Z2907)
  - Dreisatz proportional (Einheit 2)
    - Sprosse 1 · Tabelle mit Einerschritten weiterführen (Vorstufe) → D [Zeilen 2787–2788]; Eintrag: Vorstufe
      „(inhaltlich und durch Rechnen mit Dreisatz)“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 2 · verdoppeln und halbieren (4×) → D [Zeilen 2783–2786]
      „Ermitteln von Größen in anwendungsbezogenen, direkt proportionalen Zusammenhängen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 3 · hochrechnen mal 3, mal 10 → D [Zeilen 2783–2786]
      „Ermitteln von Größen in anwendungsbezogenen, direkt proportionalen Zusammenhängen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 4 · runterrechnen → D [Zeilen 2783–2786]
      „Ermitteln von Größen in anwendungsbezogenen, direkt proportionalen Zusammenhängen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 5 · auf eine Portion, dann hochrechnen (4×, Minitabelle) → D [Zeilen 2787–2788]
      „(inhaltlich und durch Rechnen mit Dreisatz)“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 6 · Preis mit Komma → D [Zeilen 2787–2788]
      „(inhaltlich und durch Rechnen mit Dreisatz)“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 7 · Preisvergleich über gleiche Portion → D [Zeilen 2783–2785]
      „Beschreiben der Eigenschaften direkt proportionaler Zusammenhänge und“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 8 · Prüfungshöhe: fehlender vierter Wert mit nicht ganzzahligem Wert je Portion (P10-Form). → D [Zeilen 2787–2788]; Eintrag: Prüfungshöhe
      „(inhaltlich und durch Rechnen mit Dreisatz)“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
  - Antiproportional (Einheit 3)
    - Sprosse 1 · „je mehr, desto weniger“ ankreuzen (Vorstufe) → E [Zeilen 2799–2800]; Eintrag: Vorstufe
      „Unterscheidung zwischen direkt und indirekt proportionalen“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 2 · doppelt → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 3 · halb (4×) → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 4 · dreifach → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 5 · Drittel → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 6 · auf eine Einheit hochrechnen, dann runter → E [Zeilen 2798–2799]
      „Verwendung von Verhältnisgleichungen)“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 7 · Produkt als Probe → keine Stelle; Die Produktprobe nennt der Teil C nicht.
    - Sprosse 8 · Sachtext → E [Zeilen 2795–2797]
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 9 · Prüfungshöhe: Dreisatz umgekehrt mit Zwischenschritt auf eine Einheit. → E [Zeilen 2795–2797]; Eintrag: Prüfungshöhe
      „Berechnen von Größen in direkt und indirekt proportionalen Zuordnungen (auch unter“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
  - Erkennen (Einheit 4)
    - Sprosse 1 · je-desto-Satz (Vorstufe) → E [Zeilen 2799–2800]; Eintrag: Vorstufe
      „Unterscheidung zwischen direkt und indirekt proportionalen“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 2 · Tabelle mit Quotient prüfen (4×) → D [Zeilen 2783–2785]
      „Beschreiben der Eigenschaften direkt proportionaler Zusammenhänge und“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 3 · Produkt prüfen → E [Zeilen 2799–2800]
      „Unterscheidung zwischen direkt und indirekt proportionalen“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 4 · Nullwert und Grundgebühr → D [Zeilen 2786–2787]
      „Abgrenzung von Eigenschaften anderer Zuordnungen (auch in“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 5 · Graph zuordnen → E [Zeilen 2798–2800]
      „Übersetzen zwischen symbolischer, sprachlicher, tabellarischer und grafischer“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 6 · gemischte Tabellen (proportional, antiproportional, keins) → E [Zeilen 2795–2798]
      „Beschreiben, Analysieren, Interpretieren und Vergleichen von Eigenschaften von Zuordnungen und“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
    - Sprosse 7 · Prüfungshöhe: Entscheidung mit Begründung. → E [Zeilen 2795–2798]; Eintrag: Prüfungshöhe
      „Beschreiben, Analysieren, Interpretieren und Vergleichen von Eigenschaften von Zuordnungen und“ – Block 2795–2806, Niveaustufe am Block: E (Z2803)
  - Rate (Einheit 4)
    - Sprosse 1 · Rate ablesen („je Liter“, „je Stunde“) (Vorstufe) → D [Zeilen 2783–2786]; Eintrag: Vorstufe
      „Ermitteln von Größen in anwendungsbezogenen, direkt proportionalen Zusammenhängen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 2 · Kosten aus Menge mal Preis (4×) → D [Zeilen 2783–2786]
      „Ermitteln von Größen in anwendungsbezogenen, direkt proportionalen Zusammenhängen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 3 · Menge aus Kosten geteilt durch Preis → D [Zeilen 2783–2786]
      „Ermitteln von Größen in anwendungsbezogenen, direkt proportionalen Zusammenhängen“ – Block 2780–2791, Niveaustufe am Block: D (Z2788)
    - Sprosse 4 · Geschwindigkeit aus Weg : Zeit → E [Zeile 2189]
      „Verwenden von Größenangaben in Rechnungen (auch Geschwindigkeiten, Dichten)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 5 · Dauer aus Weg : Geschwindigkeit → E [Zeile 2189]
      „Verwenden von Größenangaben in Rechnungen (auch Geschwindigkeiten, Dichten)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
    - Sprosse 6 · Einheit umrechnen (s → min, ct → €) → E [Zeilen 2152–2153]
      „Nutzung der Zusammenhänge zum Umrechnen von Einheiten“ – Block 2119–2159, Niveaustufe am Block: D (Z2133), E (Z2155)
    - Sprosse 7 · Prüfungshöhe: Dauer aus Strecke und Geschwindigkeit in der verlangten Zeiteinheit (P10-Form). → E [Zeile 2189]; Eintrag: Prüfungshöhe
      „Verwenden von Größenangaben in Rechnungen (auch Geschwindigkeiten, Dichten)“ – Block 2189–2206, Niveaustufe am Block: E (Z2198)
- LISUM: Differenzierungshinweis, keine getrennten Reihen; Reihen: „Jahrgangsstufe 7, Mathematik: Zuordnungen“ [Zeile 89]
  - Beleg [Zeile 90]: „Hinweis: Die Differenzierung zwischen EBR-, FOR- und GYM-Klassen erfolgt über Tiefgründigkeit der Bearbeitung, das Eingehen auf Details und Menge“
- Spanne: ja  – Die Einheiten liegen auf D und E; die Achseneinteilung ist im Teil C aber erst auf G belegt („auch bei verschiedenen Einheiten und Einteilungen der Koordinatenachsen“). Damit liegen Sprossen auf G und Einheiten auf F und darunter. Ohne diesen Verfahrenstyp wäre die Spanne „nein“.
- Ermessen (4):
  - **Achseneinteilung auf G:** Der ganze Verfahrenstyp „Achseneinteilung“ (Einheit 1) findet im Teil C nur eine Stelle, und die steht im G-Block der Leitidee Gleichungen und Funktionen („auch bei verschiedenen Einheiten und Einteilungen der Koordinatenachsen“, Zeilen 2900–2903). Der Eintrag verankert ihn stattdessen über die LISUM-Planungshilfe. Diese eine Zuordnung entscheidet die Spanne des Eintrags.
  - Sprossen „ob Punkte verbunden werden dürfen“ und „beide Achsen beschriften“: keine Stelle; beides steht in der Planungshilfe, nicht im Teil C. Der Eintrag sagt das selbst.
  - Sprossen „Kästchen abzählen“, „Fehler finden: Achsen vertauscht“, „Produkt als Probe“: keine Stelle; Zeichentechnik bzw. Fehlerquellen des Unterrichts.
  - Der RLP schreibt „indirekt proportional“, der Katalog „antiproportional“ – gleiche Sache, anderes Wort.
