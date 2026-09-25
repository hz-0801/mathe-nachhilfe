# Vorschläge für das Urteil im Chat (2026-09-27)

Zweck: vier Posten aus faellig.md § 2, deren Urteil im Chat mit einem ausgearbeiteten Vorschlag schneller fällt – (1) der Ausbau der neuen Einheiten potenz-exponentialfunktionen 5 und daten 7 (katalog/_marken-neue-einheiten.md), (2) die zwei G-Inhalte aus befund-geltung-2026-09-21.md § 3, (3) das Nebentyp-Etikett von 2025-GYM-K5d, (4) die Namensabweichungen aus katalog/_verweise.md Prüfung 3 (b).
Stand: Katalog auf Commit b9683ed (Auftrag Nacht 2026-09-27, Teil 7). Abschnitt 1 und 2 von Hilfsagenten (Opus) entworfen und in der Auftragssitzung durchgesehen, Abschnitt 3 und 4 in der Auftragssitzung geschrieben. Zeilennummern der Einträge beziehen sich auf diesen Stand.

**Vorschlag, nicht entschieden.** Kein Katalogeintrag, kein Katalog und keine Belegdatei ist geändert. Übernommen wird nur, was der Chat entscheidet; Marken-Zeilen bleiben Sache von werkzeuge/marken-bau.py.

## 1 Ausbau der neuen Einheiten

### 1a potenz-exponentialfunktionen.md, Einheit 5

**1. Merkkasten**

Einfügen in: „### Merkkasten“, nach dem Kasten „Einheit 4 (Verdopplungs- und Halbwertszeit):“ und seiner Quelle-Zeile (Zeile 76), mit einer Leerzeile davor.

```
Einheit 5 (Potenzfunktionen mit natürlichem Exponenten):
    Potenzfunktion: y = a · xⁿ mit einer natürlichen Zahl n im Exponenten – die Variable steht in der Basis. n = 1 ergibt eine Gerade, n = 2 eine Parabel, n = 3 eine kubische Parabel. Steht die Variable im Exponenten, wie bei y = 2ˣ, ist es eine Exponentialfunktion.
    Gerader Exponent: Der Graph ist achsensymmetrisch zur y-Achse und liegt bei positivem a nie unter der x-Achse – (−3)⁴ = 81 wie 3⁴ = 81. Ungerader Exponent: Der Graph ist punktsymmetrisch zum Ursprung und läuft bei positivem a von links unten nach rechts oben – (−3)³ = −27.
    Faktor a: Ist a größer als 1, wird der Graph schmaler, liegt a zwischen 0 und 1, wird er breiter; ein negatives a spiegelt ihn an der x-Achse. Jeder Graph geht durch O(0 | 0) und P(1 | a).
    Rückwärts: zum Funktionswert das Argument mit der Wurzel – x³ = 64 hat genau eine Lösung, x = 4 (dritte Wurzel mit dem Taschenrechner); x⁴ = 81 hat zwei, x = 3 und x = −3.
    Formelsammlung: Funktionen – Potenzfunktionen [FS]
Quelle: [Serlo 51910] „Potenzfunktionen mit natürlichen Exponenten“ (de.serlo.org/mathe/51910, CC BY-SA 4.0; am 2026-09-25 abgerufen, nur als Zusammenfassung des Abrufs gelesen, nicht im Wortlaut), sinngemäß: f(x) = a · xⁿ mit natürlichem n, gerade Potenzfunktionen achsensymmetrisch zur y-Achse, ungerade punktsymmetrisch zum Ursprung, alle Graphen durch den Punkt (1 | a); [RLP H] „Potenzfunktionen der Form y = a xᵏ + b“ (S. 61) und [RLP F] „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ (S. 43); [LISUM-PH] Reihe „Potenz- und Wurzelfunktionen“: „Potenzfunktionen auf Basis von Wertetabellen zeichnen, ähnliche Graphen kategorisieren (z. B. gemeinsame Quadranten)“, „Punktprobe“, Begriffe „symmetrisch zum Ursprung, Achsensymmetrie (zur y-Achse)“ (Zeilen 2428–2430 und 2474, CC BY-SA, sinngemäß); [LS-AA Kl. 9 III 7]; die Zahlenbeispiele sind eigen.
```

Fünf Kastenzeilen (vier Regeln, eine Formelsammlung-Zeile) wie die Nachbarkästen, die alle eine „Formelsammlung:“-Zeile mit [FS] tragen.

**2. Sprossen je Verfahrenstyp**

Einfügen in: „### Für schwache Schüler“, „Sprossen je Verfahrenstyp“, nach der Zeile „- Verdopplungs- und Halbwertszeit (Einheit 4): …“ (Zeile 106). Gleichzeitig die Zeile „- Potenzfunktion einordnen (Einheit 1, Vorrat): …“ (Zeile 101) streichen – ihr Inhalt geht in die dritte Kette unten auf.

```
- Wertetabelle und Graph (Einheit 5): „Welches Vorzeichen?“ und „Wohin zeigen die Enden?“ ankreuzen (Vorstufe) → Potenzen negativer Zahlen mit Klammer ausrechnen (4×) → Wertetabelle zu x hoch drei mit negativen und positiven x ausfüllen → Wertetabelle zu x hoch vier → Punkte eintragen und die Achseneinteilung wählen, weil die Werte schnell groß werden → die Punkte zu einer glatten Kurve verbinden, flach am Ursprung → die Graphen zu den Exponenten eins bis vier in ein Koordinatensystem zeichnen und die gemeinsamen Punkte markieren → Symmetrie am Exponenten ablesen und begründen (gerade: senkrechte Achse; ungerade: Ursprung) → Faktor vor der Potenz: schmaler, breiter, gespiegelt → Gleichung einem von vier Graphen zuordnen und zu einer Gleichung den Graphen ankreuzen → begründen, warum der Graph mit Exponent vier nie unter die waagerechte Achse kommt und warum der mit Exponent drei durch den dritten Quadranten geht → Prüfungshöhe: kein P10-Original; Zielmarke nach RLP H („Bestimmen und Beschreiben von Merkmalen … Potenzfunktionen“) und LISUM-PH („Potenzfunktionen auf Basis von Wertetabellen zeichnen, ähnliche Graphen kategorisieren“): zu einer Potenzfunktion mit Faktor die Wertetabelle mit negativen x aufstellen, den Graphen zeichnen, Symmetrie und Quadranten begründen und die Gleichung einem von vier Graphen zuordnen [LS-AA Kl. 9 III 7; Fundamente Kl. 9, S. 204; Schnittpunkt Kl. 10, S. 134; LISUM-PH Zeilen 2427–2429].
- Funktionswert, Punktprobe und Argument (Einheit 5): „Welches Vorzeichen?“ ankreuzen (Vorstufe) → Funktionswert für eine positive Zahl berechnen (4×) → für eine negative Zahl mit Klammer → mit Faktor vor der Potenz, erst potenzieren, dann malnehmen → Punktprobe: einsetzen und vergleichen, nicht am Graphen schätzen → Argument zu einem Wert beim Exponenten zwei, beide Lösungen → beim Exponenten drei mit der dritten Wurzel am Taschenrechner, genau eine Lösung, auch zu einem negativen Wert → beim Exponenten vier, zwei Lösungen oder keine → Sachaufgabe Würfel: Volumen aus der Kante, Kante aus dem Volumen → Fehler finden (Minus vor der Potenz gegen Minus in der Klammer; x hoch drei als drei mal x) → Prüfungshöhe: kein P10-Original; Zielmarke nach RLP F („Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“) und LISUM-PH („Punktprobe“): zu einer Potenzfunktion einen Punkt rechnerisch prüfen und zu einem gegebenen Funktionswert alle Argumente angeben, im Sachkontext die Würfelkante aus dem Volumen [LS-AA Kl. 9 III 7; Mathematik 2023 Kl. 10, S. 19 „Potenzfunktionen untersuchen“; LISUM-PH Zeile 2430].
- Potenzfunktion vom exponentiellen Term unterscheiden (Einheit 5): „Basis oder Exponent?“ ankreuzen (Vorstufe) → zu einem Term angeben, ob die Variable in der Basis oder im Exponenten steht (4×) → Wertetabellen zu x hoch zwei und zu zwei hoch x nebeneinander ausfüllen, auch für negative x → beide Graphen in ein Koordinatensystem zeichnen: die Potenzfunktion geht durch den Ursprung, die Exponentialfunktion schneidet die senkrechte Achse bei eins und bleibt über der waagerechten Achse → für große x entscheiden, welcher Term schneller wächst → zu einem Sachverhalt die passende Gleichung wählen (Würfelvolumen gegen Verdopplung) → Prüfungshöhe: kein P10-Original; Zielmarke nach RLP H („Gegenüberstellen einander entsprechender Eigenschaften der bekannten Funktionsklassen“) und LISUM-PH Gym-Reihe (sinngemäß: Verlauf der Exponentialfunktion gegen den Verlauf der Potenzfunktionen vergleichen): zu zwei Termen mit denselben Zahlen in Basis und Exponent entscheiden und begründen, welcher eine Potenzfunktion ist, und die Graphen unterscheiden [LISUM-PH Zeile 2630; LS-AA Kl. 9 III 7 und Kl. 10 II 2]; Nebenmarke: die Gleichung mit der Variablen in der Basis als Distraktor ausschließen (P10-Form 2017-OS-K7c, Stern, Niveau I – Typ „Exponentialfunktion aufstellen“, Einheit 3; setzt Einheit 3 voraus, siehe Offen).
```

**3. Zielmarke**

Einfügen in: „### Prüfungsform (P10)“, Liste unter „Zielmarke (Haupt-, Neben- und Basismarke je Einheit; …):“, nach der Zeile „Einheit 4 – …“ (Zeile 119).

```
Einheit 5 – keine aus der P10: kein Typ, kein Original, keine Haupt- oder Basismarke (Prüfungswort „keine P10-Aufgabe“); das ist hier kein Befund, sondern die Lage der Einheit. Zielmarke nach Lehrwerk und RLP H (S. 61): Wertetabelle mit negativen x, Graph, Symmetrie begründen, Gleichung einem von vier Graphen zuordnen, Punktprobe und Argument zum Wert (LS Kl. 9 III 7, Fundamente Kl. 9 6.2, Elemente Kl. 9 5.4.1, mathe.delta Kl. 9 6.1, Schnittpunkt Kl. 10 6.2, Mathematik 2023 Kl. 10 S. 18–19, Sekundo Kl. 10 S. 92; LISUM-PH Reihe „Potenz- und Wurzelfunktionen“, Block „Potenzfunktionen entdecken“, Zeilen 2427–2430 – dort nur Gymnasium und H). Nebenmarke: die Auswahl der passenden Gleichung in 2017-OS-K7c (Stern, Niveau I, Einheit 3), deren Distraktor y = x^1,13 eine Potenzfunktion ist – die Unterscheidung wird dort mitgeprüft, nicht verlangt; die Fehlerquelle des Originals nennt nur 1,13 statt 0,87 und die lineare Gleichung. Außerhalb der P10 (Gymnasium): 2020-GYM-K3b, die Umkehrfunktion von y = ³√x im ersten Quadranten ist y = x³ (Niveau III, Thema Funktionen allgemein; zählt nach der Themenregel nicht).
```

**4. Typische Fehler**

Einfügen in: „### Typische Fehler“, nach der letzten Zeile „- Zwischenwerte zu früh gerundet …“ (Zeile 92).

```
- Potenz als Produkt aus Basis und Exponent: x³ als 3 · x gelesen, für x = 2 also 6 statt 8. [P10 2020-OS-B1h, 2024-OS-B1g Fehlerquellen „4³ = 12“ – dort an Zahlen, potenzen-wurzeln.md; FD Malle, Potenz als „mal“ gelesen]
- Vorzeichen bei negativem x: (−2)³ positiv gerechnet oder (−2)⁴ negativ; −x² mit (−x)² verwechselt, sodass die Wertetabelle zu y = x⁴ links negative Werte bekommt. [P10 2014-OS-K7a, 2018-OS-K5a, 2024-OS-K3c Fehlerquellen „negative Zahl quadriert“ – quadratische-funktionen.md; potenzen-wurzeln.md Fehlerzeile „Vorzeichen bei negativer Basis“]
- Gerader und ungerader Exponent nicht unterschieden: den Graphen von y = x³ links wie eine Parabel nach oben gebogen oder nur im ersten Quadranten gezeichnet. [FD, aus dem Gedächtnis]
- Punkte mit dem Lineal verbunden oder am Ursprung eine Spitze gezeichnet; y = x⁴ am Ursprung so spitz wie y = x² statt flacher. [FD; quadratische-funktionen.md Fehlerzeile „Punkte mit dem Lineal verbunden“ (FD)]
- Punktprobe am Graphen geschätzt statt gerechnet. [P10 2020-OS-K3b Fehlerquelle – dort an der Parabel, quadratische-funktionen.md]
- Argument zum Wert: bei x⁴ = 16 nur x = 2 angegeben; bei x³ = −8 „keine Lösung“, weil man aus einer negativen Zahl keine Wurzel ziehen könne (das gilt nur für gerade Exponenten); die dritte Wurzel mit der Quadratwurzeltaste gerechnet. [FD; potenzen-wurzeln.md Einheit 3 „keine Wurzel aus einer negativen Zahl“ als Quelle der Übergeneralisierung]
- Faktor a als Verschiebung gelesen (y = −x³ „nach unten geschoben“) oder großes a als „breiter“. [FD; quadratische-funktionen.md Fehlerzeile „Streckung und Verschiebung verwechselt“ (FD)]
- Potenzfunktion und Exponentialfunktion verwechselt: x² und 2ˣ gleichgesetzt, die Wertetabelle zu 2ˣ wie zu x² ausgefüllt. [FD Malle; P10 2017-OS-K7c: der Distraktor y = x^1,13 setzt diese Verwechslung voraus, die Fehlerquelle des Originals nennt sie nicht]
- Würfelkante aus dem Volumen durch drei geteilt statt mit der dritten Wurzel. [FD; koerper.md Typ „Würfelkante aus V (Kubikzahlen)“, Fehler „3 · 3 statt 3 · 3 · 3“]
```

**5. Voraussetzungen (Blatt 0)**

Einfügen in: „### Voraussetzungen (Blatt 0)“, Fertigkeiten nach der Zeile „- Division zweier Tabellenwerte …“ (Zeile 38); Erkennungsschritte nach „- „Was wird verdoppelt?“ …“ (Zeile 45).

```
- Potenzen mit natürlichem Exponenten als wiederholte Multiplikation, auch mit negativer Basis: Klammer setzen, bei gerader Hochzahl positiv, bei ungerader negativ – Einheit 5. Thema Potenzen und Wurzeln (potenzen-wurzeln.md), Einheit 1; Rationale Zahlen (rationale-zahlen.md), Einheit 3. [RLP F „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte Multiplikation“ (S. 43); P10 2014-OS-K7a, 2025-OS-B1h Fehlerquellen „Vorzeichen bei negativer Basis“]
- Normalparabel: Wertetabelle mit negativen x, Punkte eintragen, Parabel als Bogen zeichnen, symmetrisch zur senkrechten Achse, bei negativem Faktor nach unten geöffnet, schmaler oder breiter – Einheit 5 (der Fall Exponent zwei). Thema Quadratische Funktionen (quadratische-funktionen.md), Einheit 1. [RLP G; LS-AA Kl. 9 I 2; Schnittpunkt Kl. 10, S. 132 „Lineare und quadratische Funktionen“ unmittelbar vor den Potenzfunktionen]
- Proportionale Funktion: Gerade durch den Ursprung, Faktor als Steigung – Einheit 5 (der Fall Exponent eins). Thema Lineare Funktionen (lineare-funktionen.md), Einheit 1. [RLP F]
- Koordinatensystem mit vier Quadranten, Achseneinteilung wählen, wenn die Werte schnell groß werden – Einheit 5. Thema Symmetrie und Abbildungen (symmetrie-abbildungen.md), Einheit 1; Zuordnungen (zuordnungen.md), Einheit 1. [RLP E „vier Quadranten“; RLP G „auch bei verschiedenen Einheiten und Einteilungen der Koordinatenachsen“]
- Achsensymmetrie und Punktsymmetrie an einer Figur erkennen (Faltkante, halbe Drehung um einen Punkt) – Einheit 5. Thema Symmetrie und Abbildungen (symmetrie-abbildungen.md), Einheit 2 und 3. [RLP C/D; LISUM-PH Begriffe „symmetrisch zum Ursprung, Achsensymmetrie (zur y-Achse)“]
- Quadratwurzel und Kubikwurzel als Umkehrung des Potenzierens, Kubikwurzel mit dem Taschenrechner, aus einer negativen Zahl keine Quadratwurzel – Einheit 5. Thema Potenzen und Wurzeln (potenzen-wurzeln.md), Einheit 3; Reelle Zahlen (reelle-zahlen.md), Einheit 3. [RLP F „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ (S. 43); LS-AA Kl. 9 III 6 unmittelbar vor III 7]
- Würfelvolumen als Kante hoch drei, Kante aus dem Volumen über Kubikzahlen – Einheit 5 (Sachaufgabe). Thema Körper (koerper.md), Einheit 2. [RLP D; koerper.md Typ „Würfelkante aus V (Kubikzahlen)“]
Erkennungsschritte (hinter die vorhandenen sechs):
- „Basis oder Exponent?“ – zu Termen wie x hoch drei, drei hoch x und drei mal x ankreuzen, ob die Variable in der Basis, im Exponenten oder in einem Produkt steht; nichts rechnen. Vor Einheit 5. [bisher Vorstufe der Vorrat-Sprosse „Potenzfunktion einordnen“ in Einheit 1; LISUM-PH Gym-Reihe Zeile 2630; P10 2017-OS-K7c Auswahl mit einer Potenz als Distraktor]
- „Welches Vorzeichen?“ – zu Potenzen negativer Zahlen mit und ohne Klammer ankreuzen, ob das Ergebnis positiv oder negativ ist (Klammer? gerade oder ungerade Hochzahl?); nichts ausrechnen. Vor Einheit 5. [potenzen-wurzeln.md Erkennungsschritt „Plus oder minus?“; P10 2014-OS-K7a Fehlerquelle]
- „Wohin zeigen die Enden?“ – zu Graphskizzen ankreuzen, ob beide Enden nach oben zeigen (gerader Exponent) oder eines nach unten und eines nach oben (ungerader Exponent) und ob der Graph gespiegelt ist; nichts rechnen. Vor Einheit 5. [LISUM-PH „ähnliche Graphen kategorisieren (z. B. gemeinsame Quadranten)“, Zeilen 2428–2429; Serlo 51910 gerade und ungerade Potenzfunktionen]
```

Die Unterscheidung von der Exponentialfunktion braucht Einheit 3 dieses Eintrags; sie steht deshalb nicht als Blatt-0-Zeile da (Selbstverweis), sondern als Voraussetzung der dritten Sprossenkette (siehe 7).

**6. Verortung**

Einfügen in: „### Verortung“, erster Absatz (Zeile 5), nach dem Satz „Auf H kommen y = a · bˣ + c, die Potenzfunktion y = a · xᵏ + b, Umkehrfunktionen und die Exponentialgleichung mit Logarithmus dazu.“:

„Die Potenzfunktion mit natürlichem Exponenten (Einheit 5) führt der RLP nur als Teil der H-Zeile y = a · xᵏ + b; ihre Bausteine stehen tiefer – Potenzen mit natürlichem Exponenten als fortgesetzte Multiplikation und Quadrat- und Kubikwurzel als Umkehrung auf F (Zahlen und Operationen, S. 43), die Parabel auf G. Die Lehrwerke führen sie am Gymnasium in Kl. 9, an der Oberschule in Kl. 10, sieben von acht Regelreihen (katalog/_klassen-belege.md); die Einheit folgt deshalb dem Lehrwerk, nicht der Stufe.“

Am Ende derselben Zeile, in der Verweisliste nach „Potenzgesetze und rationale Exponenten → reelle-zahlen.md Einheit 2 und 3.“ anfügen:

„Potenzen mit negativer Basis → potenzen-wurzeln.md Einheit 1 (hier Blatt 0 für Einheit 5); Normalparabel als Fall Exponent zwei → quadratische-funktionen.md Einheit 1; Kubikwurzel → potenzen-wurzeln.md Einheit 3 und reelle-zahlen.md Einheit 3; Würfelvolumen → koerper.md Einheit 2; Potenzfunktionen mit ganzzahligem und rationalem Exponenten, Summand b, Wurzelfunktion als Umkehrfunktion (übrige LISUM-Reihe „Potenz- und Wurzelfunktionen“) → nicht geführt.“

In der [RLP]-Zeile (Zeile 6) nach „Zahlen und Operationen E (S. 40–41): „Nutzen von Prozentsätzen als Operatoren““ anfügen:

„; F (S. 43, Textfassung Zeilen 1974–1979): „Darstellen und Beschreiben von Potenzen mit natürlichem Exponenten als fortgesetzte Multiplikation“, „Beschreiben von Quadrat- und Kubikwurzel als Umkehrung der Potenzschreibweise“ – die Bausteine der Einheit 5“

[LS-AA] (Zeile 7) und [LISUM-PH] (Zeile 8) tragen die Einheit schon („Einheit 5 = Kl. 9 III 7“; „Seit 26.09.2026 steht die Potenzfunktion …“) – keine Änderung.

**7. Offen/Hinweise**

- Urteil zu Typ 5.14 (Vorschlag): nicht zuordnen – 2017-OS-K7c verlangt die Auswahl der Exponentialgleichung, der Potenz-Distraktor y = x^1,13 hat keinen natürlichen Exponenten und ist nicht Fehlerquelle des Originals; mit Zuordnung hätte Einheit 5 über „Exponentialfunktion aufstellen“ vier P10-Jahrgänge (2016, 2017, 2025, 2026, davon Haupt zwei; katalog/_pruefungswort-belege.md) und hieße „P10“, obwohl kein Original eine Potenzfunktion zeichnen, auswerten oder deuten lässt. Stattdessen Nebenmarke in Zielmarke und dritter Sprossenkette (oben).
- Reihenfolge: Die Unterscheidungskette setzt Einheit 3 voraus. Am Gymnasium steht die Potenzfunktion vor der Exponentialfunktion (LS Kl. 9 III 7 vor Kl. 10 II), an der Oberschule meist danach (Schnittpunkt Kl. 10: Kapitel 4 „Exponentialrechnung“ mit exponentiellem Wachstum, S. 88, vor Kapitel 6.2, S. 134). Vorschlag: die dritte Kette als Vorrat markieren, solange Einheit 3 nicht behandelt ist.
- Folgeänderungen im Eintrag, nicht Teil der Blöcke: Mindeststoff-Zeile (Zeile 95) „Vorrat: Potenzfunktion (H, kein Original; eigene LISUM-Reihe 2417, nur Gymnasium)“ ist überholt – Vorschlag „Einheit 5: kein Mindeststoff (RLP H), Vorrat; Bausteine auf F“; die Blatt-0-Zeilen 31 und 37 sagen „alle Einheiten“ (Prozentfaktor, Dezimalzahlen multiplizieren) und gelten nicht für Einheit 5 – „Einheit 1 bis 4“; Kopfzeile (Zeile 2) nennt für das Gymnasium nur Kl. 9–10 nach Wachstum, Einheit 5 liegt dort in Kl. 9, an der Oberschule in Kl. 10; die Kastenzahlen-Zeile (Zeile 139) um Kasten 5 ergänzen; Posten in faellig.md § 2 streichen, wenn der Ausbau übernommen wird.
- Nicht belegt: alle [FD]-Fehler aus dem Gedächtnis; Serlo 51910 nur als Zusammenfassung des Abrufs gelesen; [FS] Abschnitt „Potenzfunktionen“ ungeprüft; die Lehrwerksinhalte hinter den Kapitelzeilen (welche Exponenten, ob die Würfel-Sachaufgabe) sind nicht eingesehen – nur Verzeichniszeilen.
- 2020-GYM-K3b (msa-katalog-gym.csv) berührt Einheit 5 als Graph von x³; nach der Themenregel ohne Folge für das Prüfungswort.
- Prüfskript: `_pruef_katalog.py` ordnet eine Blatt-0-Zeile jeder genannten Einheitsnummer zu, auch den Einheiten fremder Dateien („Einheit 5. Thema Potenzen … Einheit 1“ wird auch gegen Kasten 1 dieses Eintrags geprüft). Die Zeilen oben sind ziffernfrei außerhalb der Belegklammern und bestehen deshalb gegen alle fünf Kästen.

Kastenzahlen: Kasten 5 (n = 1, 2, 3; y = 2ˣ; (−3)⁴ = 81, 3⁴ = 81; (−3)³ = −27; a größer als 1, zwischen 0 und 1; O(0 | 0), P(1 | a); x³ = 64, x = 4; x⁴ = 81, x = 3, x = −3) sperrt 0, 1, 2, 3, 4, 27, 64, 81 – in Sprossen/Blatt 0 nicht verwendet (Sprossen und Blatt-0-Zeilen oben tragen außerhalb der Belegklammern keine Ziffer; Zahlen stehen in Worten).

### 1b daten.md, Einheit 7

**1. Merkkasten**

Einfügen in: „### Merkkasten“, nach dem Kasten „Einheit 6 (Kenngrößen aus Häufigkeitstabellen und Klassen, Sek II):“ und seiner Quelle-Zeile (Zeile 123), mit einer Leerzeile davor.

```
Einheit 7 (Vierfeldertafel, Sek I):
    Vierfeldertafel: zwei Merkmale mit je zwei Ausprägungen; die vier inneren Felder zählen die Kombinationen, am Rand stehen die Zeilen- und Spaltensummen, unten rechts die Gesamtzahl.      Mädchen 12 mit Brille, 18 ohne → 30; Jungen 7 mit, 13 ohne → 20; zusammen 19 mit, 31 ohne, 50 Kinder
    Fehlendes Feld: Randsumme minus das bekannte Feld; zur Kontrolle muss jede Zeile, jede Spalte und die Gesamtzahl aufgehen.      30 − 12 = 18
    Anteil an allen: Feld durch die Gesamtzahl. Anteil innerhalb einer Zeile oder Spalte: Feld durch diese Randsumme – „von den Mädchen …“ heißt: durch die Zahl der Mädchen teilen.      12 : 50 = 24 % aller Kinder; 12 : 30 = 40 % der Mädchen; 12 : 19 ≈ 63 % der Brillenträger
    Die Anteile innerhalb einer Zeile ergeben zusammen 1 (100 %).      40 % + 60 % = 100 %
    Formelsammlung: Stochastik – Vierfeldertafel [FS]
Quelle: eigene Formulierung nach [RLP G] „Ermitteln von (auch bedingten) Wahrscheinlichkeiten … unter Nutzung von Baumdiagrammen, Pfadregeln, Vierfeldertafeln …“ (S. 65) und [RLP E] „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ (S. 64); [LISUM-PH] Jg. 9/10 „Nutzen von Baumdiagrammen und Vierfeldertafeln insbesondere bzw. auch mit absoluten Häufigkeiten“ (Zeilen 2301–2302, CC BY-SA, sinngemäß); [LS-AA Kl. 9 VII 2] „Vierfeldertafel – mit Anteilen argumentieren“; [Serlo 66166] „Vierfeldertafel mit Häufigkeiten“ (de.serlo.org/mathe/66166, CC BY-SA 4.0; am 2026-09-25 abgerufen, nur als Zusammenfassung gelesen), sinngemäß: der letzte Wert einer Zeile oder Spalte ist die Summe der beiden davor, relative Häufigkeiten ergeben zusammen eins; Zahlenbeispiel eigen.
```

Form wie die Sek-I-Kästen 2, 3 und 5 des Eintrags: Regel mit eingerücktem Beispiel in derselben Zeile, „Formelsammlung:“-Zeile mit [FS]; keine „Auswendig (Teil A):“-Zeile, weil die Einheit keine Sek-II-Zeile trägt (bei Variante B unter 6 wäre sie nötig). Rechnung geprüft: 12 + 18 = 30, 7 + 13 = 20, 12 + 7 = 19, 18 + 13 = 31, 19 + 31 = 30 + 20 = 50; 12 : 50 = 0,24; 12 : 30 = 0,4; 12 : 19 ≈ 0,632; 18 : 30 = 0,6.

**2. Sprossen je Verfahrenstyp**

Einfügen in: „### Für schwache Schüler“, „Sprossen je Verfahrenstyp“, nach der letzten Zeile „- Kenngrößen aus Tabellen und Klassen (Einheit 6): …“ (Zeile 156) – in der Reihenfolge der Lerneinheiten, die Einheit 7 hinter die Sek-II-Einheit 6 stellen.

```
- Vierfeldertafel füllen (Einheit 7): „Welche zwei Merkmale?“ und „Feld oder Rand?“ ankreuzen (Vorstufe) → an einer vollständig gefüllten Tafel die Zeilen- und Spaltensummen bilden und die Gesamtzahl auf beiden Wegen prüfen (4×) → ein fehlendes inneres Feld aus einer Zeilensumme → ein fehlendes Feld aus einer Spaltensumme → zwei fehlende Felder, erst den Rand, dann das Feld → nur die Ränder und ein inneres Feld gegeben, die übrigen drei Felder erschließen → die Tafel aus einem Text aufstellen: Merkmale benennen, Zahlen einordnen, „der Rest“ als Differenz → Prüfungshöhe: kein P10-Original; Zielmarke nach Lehrwerk und LISUM-PH („Vierfeldertafeln … auch mit absoluten Häufigkeiten“): aus einem Sachtext mit Gesamtzahl, zwei Randangaben und einem Feld die vollständige Tafel aufstellen [LS-AA Kl. 9 VII 2; Schnittpunkt Kl. 9, S. 138; LISUM-PH Zeilen 2301–2308]; Nebenmarke außerhalb der P10: dieselbe Leistung in zwei Punkten (fhr 2023-A-3a, Niveau II – Sek-II-Zeile der Einheit 1).
- Anteile unterscheiden (Einheit 7): „Durch wen teilen?“ ankreuzen (Vorstufe) → Anteil eines Feldes an allen als Bruch (4×) → derselbe Anteil gekürzt, als Dezimalzahl und in Prozent → Anteil innerhalb einer Zeile („von den Mädchen …“) → Anteil innerhalb einer Spalte („von den Brillenträgern …“) → zu derselben Zelle beide Anteile nebeneinander und begründen, warum sie verschieden sind → prüfen, dass die Anteile einer Zeile zusammen eins ergeben → eine Aussage mit der richtigen Bezugsgröße prüfen („mehr als die Hälfte der …“) → zwei Gruppen verschiedener Größe über die Anteile innerhalb ihrer Zeilen vergleichen → Fehler finden (falsche Bezugsgröße) → Prüfungshöhe: kein P10-Original; Zielmarke nach Lehrwerk („mit Anteilen argumentieren“) und LISUM-PH (Anteilsbild: der Anteil in der einen Gruppe ist kleiner als in der anderen): eine Aussage über den Anteil in zwei Gruppen an einer Tafel mit absoluten Zahlen prüfen und mit beiden Anteilen begründen [LS-AA Kl. 9 VII 2; LISUM-PH Zeilen 2344–2360]; nächstliegende P10-Leistung: relative Häufigkeit mit der Gesamtzahl als Ganzem (2015-OS-K7b, Niveau I – Einheit 1, Typ „Relative Häufigkeit angeben“).
```

**3. Zielmarke**

Einfügen in: „### Prüfungsform (P10)“, Absatz „Zielmarke:“ (Zeile 161), am Ende nach „… (2018-OS-K3d, Niveau II, Stern).“ anfügen:

```
 Einheit 7 – keine aus der P10: msa-typen.csv führt keinen Vierfeldertafel-Typ, kein Original (Prüfungswort „keine P10-Aufgabe“). Zielmarke nach Lehrwerk und RLP G (S. 65) mit LISUM-PH Jg. 9/10 (Zeilen 2301–2308, „auch mit absoluten Häufigkeiten“): eine Tafel aus einem Text aufstellen, fehlende Felder über die Randsummen ergänzen und eine Aussage mit dem Anteil innerhalb einer Zeile oder Spalte prüfen (LS Kl. 9 VII 2, Schnittpunkt Kl. 9 6.1 und Kl. 10 5.5, Fundamente Kl. 10 5.6, mathe.delta Kl. 10 2.3). Nebenmarke außerhalb der P10: fhr 2023-A-3a, Tafel mit absoluten Anzahlen über Randsummen – 30 Erwachsene, 50 Kinder, 60 mit Sauna, davon 35 Kinder → 5 und 15 ohne, 25 und 35 mit Sauna (zwei Punkte, Niveau II; Sek-II-Zeile der Einheit 1); die Anteilsfrage in derselben Aufgabe, 2023-A-3e (Niveau III, unabhaengigkeit.md), mit der Fehlerquelle „auf die 60 Saunagäste beziehen“.
```

**4. Typische Fehler**

Einfügen in: „### Typische Fehler“, nach der letzten Sek-I-Zeile „- Boxplot: …“ (Zeile 139), vor den Sek-II-Zeilen.

```
- Falsche Bezugsgröße: den Anteil innerhalb einer Zeile durch die Gesamtzahl geteilt („von den Mädchen“ als „von allen“) oder umgekehrt; Zeilen- und Spaltenanteil derselben Zelle verwechselt. [fhr 2023-A-3e Fehlerquelle „P(C und D) auf die 60 Saunagäste beziehen und 25/60 ansetzen“ – Sek II, unabhaengigkeit.md; vierfeldertafel.md Fehlerzeile „einen Prozentwert auf die falsche Gesamtheit bezogen“; FD]
- Fehlendes Feld von der falschen Randsumme abgezogen (die Kinder mit Sauna von den Erwachsenen statt von den Kindern). [fhr 2023-A-3a Fehlerquelle; daten.md Sek-II-Fehlerzeile „in der Vierfeldertafel von der falschen Randsumme abgezogen“]
- Randsumme in ein inneres Feld eingetragen oder die Gesamtzahl als Feld gelesen; „der Rest“ nicht als Differenz erkannt. [FD; vierfeldertafel.md Fehlerzeile „weder–noch als Randwert gelesen“ (Sek II)]
- Keine Kontrolle über beide Richtungen: Zeilensummen und Spaltensummen ergeben verschiedene Gesamtzahlen, ohne dass es auffällt. [FD]
- Anteil als absolute Zahl angegeben oder durch die Zahl der anderen statt durch die ganze Gruppe geteilt. [P10 2015-OS-K7b Fehlerquelle „22 statt 22/34; 22 : 12 statt 22 : 34“ – Einheit 1]
- Zwei Gruppen verschiedener Größe über die absoluten Zahlen verglichen („mehr Mädchen tragen eine Brille, also ist der Anteil größer“). [FD; daten.md Einheit 1 Typ „zwei Gruppen verschiedener Größe über relative Häufigkeiten vergleichen“; LISUM-PH Anteilsbild „Der Anteil derjenigen, die ein Auto besitzen, ist unter den Frauen kleiner als unter den Männern“]
```

**5. Voraussetzungen (Blatt 0)**

Einfügen in: „### Voraussetzungen (Blatt 0)“, Fertigkeiten nach der letzten Sek-I-Zeile „- Bruchteil und Vielfaches einer Zahl …“ (Zeile 47), vor den Sek-II-Zeilen; Erkennungsschritte nach „- „Sortiert?“ …“ (Zeile 57), vor den Sek-II-Schritten.

```
- Summe aus zwei Teilen bilden und den fehlenden Teil zur Summe ergänzen („der Rest“) – Einheit 7. Thema Brüche und Dezimalzahlen (brueche-dezimalzahlen.md), Einheit 1 („Rest zum Ganzen“); Prozentrechnung (prozentrechnung.md), Einheit 1 („Rest zu hundert Prozent“ als Anteil). [RLP C/D; fhr 2023-A-3a Fehlerquelle „von der falschen Randsumme abgezogen“]
- Anteil einer Menge als Bruch („drei von zwölf Kindern“), kürzen, als Dezimalzahl und in Prozent – Einheit 7. Thema Brüche und Dezimalzahlen (brueche-dezimalzahlen.md), Einheit 1 und 2; Prozentrechnung (prozentrechnung.md), Einheit 1 und 2. [RLP D/E; P10 2015-OS-K7b]
- Relative Häufigkeit als Anteil an der Gesamtzahl, Häufigkeitstabelle mit Summenzeile lesen, Summe der relativen Häufigkeiten eins – Einheit 7. Thema Daten (daten.md), Einheit 1. [RLP E „Ermitteln und Vergleichen von absoluter und relativer Häufigkeit (auch in Prozent)“ (S. 64); P10 2015-OS-K7b]
- „Welche zwei Merkmale?“ – zu einem kurzen Text die beiden Merkmale und ihre je zwei Ausprägungen in Kopfzeile und Kopfspalte einer leeren Tafel schreiben; keine Zahl eintragen. Vor Einheit 7. [RLP C „Ordnen von gesammelten Daten nach vorgegebenen Merkmalen (z. B. Junge/Mädchen)“ (S. 62); LS-AA Kl. 9 VII 2]
- „Feld oder Rand?“ – zu den Zahlenangaben eines Textes ankreuzen, ob sie in ein inneres Feld gehören oder an den Rand (Zeilensumme, Spaltensumme, Gesamtzahl); nichts rechnen. Vor Einheit 7. [vierfeldertafel.md Einheit 1 Füllregel „Ränder zuerst, Felder als Differenzen der Ränder“; vierfeldertafel.md Fehlerzeile „weder–noch als Randwert gelesen“; FD]
- „Durch wen teilen?“ – zu Fragen „wie viel Prozent aller …“, „wie viel Prozent der Mädchen …“, „wie viel Prozent der Brillenträger …“ ankreuzen, durch welche Zahl geteilt wird (Gesamtzahl, Zeilensumme, Spaltensumme); nichts rechnen. Vor Einheit 7. [LS-AA Kl. 9 VII 2 „mit Anteilen argumentieren“; LISUM-PH Anteilsbild, Zeilen 2344–2360; fhr 2023-A-3e Fehlerquelle; daten.md Erkennungsschritt „Was ist das Ganze?“]
```

Die ersten drei Zeilen sind Fertigkeiten, die letzten drei Erkennungsschritte (getrennt einzufügen wie oben). Die dritte Fertigkeit verweist auf Einheit 1 desselben Eintrags (Selbstverweis, siehe 7).

**6. Verortung**

(a) Satzvorschlag, einzufügen in „### Verortung“, Zeile 5, nach „Streumaße interpretieren: H (nicht hier).“:

„Vierfeldertafel mit absoluten Anzahlen – zwei Merkmale mit je zwei Ausprägungen, Zeilen- und Spaltensummen, Anteil an allen gegen Anteil innerhalb einer Zeile oder Spalte: Einheit 7 (Sek I, Kl. 9/10); der RLP nennt die Tafel nur auf G unter „Wahrscheinlichkeiten von Ereignissen bestimmen“ (S. 65), die LISUM-Reihe Jg. 9/10 im Block „Bedingte Wahrscheinlichkeiten“ ausdrücklich „auch mit absoluten Häufigkeiten“, die Lehrwerke als eigenes Kapitel am Übergang von Daten zu Wahrscheinlichkeit (LS Kl. 9 VII 2, Schnittpunkt Kl. 9 und 10, Fundamente Kl. 10, mathe.delta Kl. 10). Fortsetzung mit Wahrscheinlichkeiten, bedingten Anteilen und Unabhängigkeit → vierfeldertafel.md, bedingte-wahrscheinlichkeit-und-bayes.md, unabhaengigkeit.md.“

(b) Stellen, die die Vierfeldertafel noch anders verorten, wörtlich:

Zeile 5 (Sek-II-Teil der Verortung): „die Vierfeldertafel mit absoluten Anzahlen als Häufigkeitstabelle mit Randsummen in Einheit 1 (das Wahrscheinlichkeitswerkzeug liegt in vierfeldertafel.md und unabhaengigkeit.md).“

Ersetzung (Variante A, empfohlen – der fhr-Typ bleibt in Einheit 1, Zählzeile und Sek-II-Kästen unverändert): „die Vierfeldertafel mit absoluten Anzahlen über Randsummen (fhr, ein Typ) als Sek-II-Zeile in Einheit 1 – das Verfahren selbst lehrt seit dem 26.09.2026 die Sek-I-Einheit 7, das Wahrscheinlichkeitswerkzeug liegt in vierfeldertafel.md und unabhaengigkeit.md.“

Ersetzung (Variante B – der fhr-Typ zieht nach Einheit 7): „die Vierfeldertafel mit absoluten Anzahlen über Randsummen (fhr, ein Typ) in Einheit 7, wo die Sek-I-Einheit dasselbe Verfahren lehrt (das Wahrscheinlichkeitswerkzeug liegt in vierfeldertafel.md und unabhaengigkeit.md).“ Folgen von B: Typenzeile Einheit 1 (Zeile 31) verliert „— Deutung: Vierfeldertafel vervollständigen (1; fhr – absolute Anzahlen über Randsummen)“, Einheit 7 bekommt „— Sek II (fhr): Vierfeldertafel vervollständigen (1; fhr – absolute Anzahlen über Randsummen)“; Zählzeile (Zeile 38) „2 + 0 + 0 + 3 + 0 + 5 + 1 = 11 Haupttypen, 8 + 0 + 0 + 9 + 0 + 12 + 1 = 30 Zeilen“; Kasten 7 braucht eine „Auswendig (Teil A):“-Zeile (Prüfliste, letzter Punkt) und hätte dann sechs Zeilen; Marke der Einheit 7 bekommt „FHR“; die Sek-II-Sprosse der Einheit 1 (Zeile 154) verliert den Schritt „→ eine Vierfeldertafel mit absoluten Anzahlen über die Randsummen füllen (fhr 2023-A-3a)“; Punkt (2) der Ermessensstellen (Zeile 184) ist umzuschreiben.

Zeile 31 (Typen je Lerneinheit, nicht Verortung, der Vollständigkeit halber): „— Deutung: Vierfeldertafel vervollständigen (1; fhr – absolute Anzahlen über Randsummen).“ – bei Variante A unverändert; anzumerken bleibt, dass die Rechnung über Randsummen eher ein Berechnungs- als ein Deutungstyp ist (Ermessen der Rohdatei, hier nicht entschieden).

Zeile 7 ([LS-AA]): „Klasse 9, Kapitel VI „Daten“ (wie Kl. 7 VII, Wiederholung und Vertiefung) und Kapitel VII 1 „Statistiken beurteilen“ (2–4 Vierfeldertafel, bedingte Wahrscheinlichkeit, Unabhängigkeit → nicht im Katalog).“

Ersetzung: „Klasse 9, Kapitel VI „Daten“ (wie Kl. 7 VII, Wiederholung und Vertiefung), Kapitel VII 1 „Statistiken beurteilen“ und VII 2 „Vierfeldertafel – mit Anteilen argumentieren“ (= Einheit 7); VII 3–4 bedingte Wahrscheinlichkeit und Unabhängigkeit → nicht hier (Sek-II-Einträge bedingte-wahrscheinlichkeit-und-bayes.md und unabhaengigkeit.md).“

Zeile 8 ([LISUM-PH]): „Die übrigen Blöcke dieser Reihe (bedingte Wahrscheinlichkeit, Vierfeldertafel, Konfidenz- und Prognoseintervalle) → wahrscheinlichkeit.md und nicht im Katalog.“

Ersetzung: „Die übrigen Blöcke dieser Reihe (bedingte Wahrscheinlichkeit, Konfidenz- und Prognoseintervalle) → wahrscheinlichkeit.md und nicht im Katalog; aus dem Block „Bedingte Wahrscheinlichkeiten“ (Zeilen 2300–2313) trägt Einheit 7 die Vierfeldertafel mit absoluten Häufigkeiten und das Anteilsbild (Zeilen 2344–2360), ohne den Begriff der bedingten Wahrscheinlichkeit.“

**7. Offen/Hinweise**

- Urteil zu Typ 7.4 (Vorschlag): nicht zuordnen – „Relative Häufigkeit angeben“ hat ein Original (2015-OS-K7b), und das steht mit derselben Rechnung schon in Einheit 1; mit Zuordnung hieße Einheit 7 „P10“ wie Einheit 1 (ein Jahrgang, 2015, Haupt eins), obwohl die P10 nie eine Tafel vorlegt. Die Aufgabe steht stattdessen als „nächstliegende P10-Leistung“ in der zweiten Sprossenkette.
- Belegbreite: Die Marken-Datei begründet die Einheit mit „alle oder fast alle Lehrwerke“; für die Vierfeldertafel trifft das nur zur Hälfte zu – vier von acht Regelreihen (LS, Fundamente, mathe.delta, Schnittpunkt), an der Oberschule allein Schnittpunkt (Sekundo, Mathematik 2023, Mathematik heute, Elemente: keine Stelle; katalog/_klassen-belege.md Zeilen 4369–4382). Der RLP führt die Tafel nur auf G und nur unter Wahrscheinlichkeiten. Damit ist Einheit 7 Vorrat im Sinn der Mindeststoff-Zeile (Zeile 146 wäre um „Einheit 7 (G) Vorrat“ zu ergänzen).
- Selbstverweis: Die Blatt-0-Zeile zur relativen Häufigkeit verweist auf daten.md Einheit 1. Ob die Blatt-0-Werkzeuge (`blatt0-belege.py`, Klammerform) einen Verweis auf den eigenen Eintrag annehmen, ist nicht geprüft; sonst nur die Verweise auf brueche-dezimalzahlen.md und prozentrechnung.md stehen lassen.
- Nicht belegt: die [FD]-Fehler aus dem Gedächtnis; Serlo 66166 nur als Zusammenfassung des Abrufs; [FS] Abschnitt „Vierfeldertafel“ ungeprüft (die Formelsammlung führt ihn vermutlich nur für Wahrscheinlichkeiten); Lehrwerksinhalte hinter den Kapitelzeilen nicht eingesehen. Eine eigene Grundvorstellungs-Aufgabe für Einheit 7 ist nicht gebaut – die vorhandene (Säule als gestapelte Einzelne, Mittelwert als Ausgleich) trägt sie nicht; Vorschlag für später: „Tafel aus Kärtchen legen“ (jedes Kind eine Karte in eines der vier Felder).
- Prüfskript-Eigenheit, gesehen beim Prüfen: `_pruef_katalog.py` liest „Einheit 1, 3 und 5“ nur als Einheit 1 und 3 (das „und 5“ nach einer Kommaliste fällt heraus, Zeilen 44 und 52 von daten.md). Die neuen Zeilen nennen deshalb je nur „Einheit 7“.
- Die Kastenzahlen-Prüfung zählt die Grundvorstellungs-Zeile gegen alle Kästen; sie ist in daten.md ziffernfrei, Kasten 7 kollidiert nicht.

Kastenzahlen: Kasten 7 (12, 18, 30; 7, 13, 20; 19, 31, 50; 30 − 12 = 18; 12 : 50 = 24 %; 12 : 30 = 40 %; 12 : 19 ≈ 63 %; 1 und 100 %; 40 % + 60 % = 100 %) sperrt 1, 7, 12, 13, 18, 19, 20, 24, 30, 31, 40, 50, 60, 63, 100 – in Sprossen/Blatt 0 nicht verwendet (Sprossen und Blatt-0-Zeilen oben tragen außerhalb der Belegklammern keine Ziffer; „drei von zwölf“, „eins“ in Worten). daten.md hat bisher keinen Kastenzahlen-Absatz unter „Offene Punkte“; diese Zeile wäre der erste.

## 2 Niveaustufe G (befund-geltung-2026-09-21.md § 3)

Zeilennummern der Einträge: Stand HEAD 2f52c77. `_niveaustufen-belege.md` steht auf 72325d0; seit 7613213 (Marken-Zeilen) liegen die Eintragszeilen ab „### Typen je Lerneinheit“ dort um 4 tiefer („Zeile 24“ dort = Zeile 28 hier). Lesart des Befunds: „neu auf Niveaustufe G“ heißt nicht, dass die Stufe sich ändert – beide Inhalte stehen im RLP (Fassung 14.08.2023) schon auf G. Neu ist, dass sie auf der Liste der G-Inhalte stehen, die auch das EBR-Heft prüft: `msa/msa-vorgaben.md` Z. 35 „Inhalte der Niveaustufe G, die für das EBR-Niveau prüfungsrelevant sind (Stand FB 10; für FOR gilt die ganze Niveaustufe G)“, Z. 39 „neu: Sinussatz“, Z. 41 „neu: Lösbarkeit und Lösungsvielfalt quadratischer Gleichungen ax²+n=b und ax²+bx+n=0 mit Begründung“; Z. 30 (Zeile „ab 2028 | FB 10 (08/2026)“): „EBR-Liste mit zwei neuen Punkten (Sinussatz; Lösbarkeit quadratischer Gleichungen)“.

### 2a Sinussatz in beliebigen Dreiecken (trigonometrie.md)

**Führt der Eintrag es schon?** Ja, als Einheit 4 auf G – ohne jedes Wort zum EBR-Niveau.
- Z. 2 (Kopf): „Sinussatz G „in Teilen“; FOR- und MSA-Gang, in der P10 seit 2016 jährlich, Sinussatz 2014–2025 in neun Jahrgängen mit Stern“.
- Z. 5 (Verortung): „Sinussatz für Seiten und Winkel und Kosinussatz für Seiten: G (Gymnasium Kl. 9, Oberschule 9–10 „in Teilen“)“.
- Z. 6 ([RLP]): „G (S. 49): „Nutzen des Sinussatzes, um in beliebigen Dreiecken Winkelgrößen und Seitenlängen zu bestimmen““; Befund dort: „für die Oberschule nur „in Teilen“, die P10 prüft den Sinussatz trotzdem jährlich“.
- Z. 17 (Lerneinheit): „4. Sinussatz – … Winkel mit dem Sinussatz – beide ohne P10-Original, Marke aus RLP und LISUM-PH … (Kl. 10; RLP G)“; Z. 18: „Marken: OS Kl. 10 · GYM Kl. 9–10 (LS 10, Fundamente 9, Elemente 9, mathe.delta 9) · P10 oft · nicht für alle: Sekundo 10 Zusatzstoff“.
- Z. 24 (Typen): „Winkel mit dem Sinussatz (kein P10-Original, RLP G)“; Z. 105 (Sprossen): „Winkel mit dem Sinussatz aus vollständigem Paar und zweiter Seite (kein P10-Original; Marke nach RLP Stufe G und LISUM-PH)“.
- Z. 99 (Mindeststoff der Prüfungsvorbereitung, „(P10, FOR)“): „Einheit 4 Sinussatz (neun Originale 2014–2025, alle mit Stern – Niveau II und III; Bedeutung des Sterns für den FOR-Gang beim Prüfungsblatt-Prompt festlegen)“.
- Z. 109 (Prüfungsform): „(kein Original 2016, 2022, 2023, 2026)“; Z. 112 (Zielmarke): Hauptmarke 2019-OS-K3c, „keine Basismarke“; Z. 122: „in der Einheit 4 verschärft um den Stern“.
- Nicht aufgelöst: Stern heißt „nur FOR“ (`msa-vorgaben.md` Z. 16 „Sternchen = nur FOR“); die Lücke 2022/2023 ist Vorgabe, nicht Zufall (Z. 24 „Nicht Prüfungsinhalt: Sinus- und Kosinussatz“, Z. 25 „identisch mit 2022, letztmalig“).

**RLP.** `quellen/quelle-rlp-teil-c-mathematik-2023.txt` Z. 2290–2291: „Nutzen des Sinussatzes, um in beliebigen Dreiecken Winkelgrößen und Seitenlängen zu bestimmen“ – Seitenkopf Z. 2215 „Themenbereich „Größen und Messen“ – Niveaustufen F, G, H“, Seite 49, Block 2278–2295, Randbuchstabe G in Z. 2285 (das H in Z. 2295 gehört nur zur Kosinussatz-Winkel-Zeile Z. 2295) → **G**, einspaltig gesetzt, kein Spaltenartefakt. Gegenprobe `katalog/_niveaustufen-belege.md` Z. 3202–3204: „4. Sinussatz – G/H“, „G [Zeile 2290] … Grundfall“; Z. 3321: Sprosse 13 Winkel mit dem Sinussatz „→ G [Zeile 2290]“ – deckt sich. Der Kosinussatz (Z. 2292, G) steht nicht auf der EBR-Liste und bleibt FOR-Stoff. Nebenbefund: `msa-vorgaben.md` Z. 39 führt „Trigonometrie im rechtwinkligen Dreieck; beliebige Dreiecke durch Zerlegung in rechtwinklige“ ebenfalls als G-Inhalt – das stützt die Abweichung in `_niveaustufen-belege.md` Z. 3335 (rechtwinklige Trigonometrie im G-Block, nicht F wie Eintrag Z. 5).

**Vorschlag.** Einheit, Typen, Sprossen und Zielmarke bleiben – der Inhalt samt Winkel-Sprosse ist da. Zu ändern ist die Geltung:
- alt (Z. 2): „(F; Sinussatz G „in Teilen“; FOR- und MSA-Gang, …“ → neu: „(F; Sinussatz G „in Teilen“, seit Fachbrief 10 auch auf EBR-Niveau prüfungsrelevant, Kosinussatz nur FOR; FOR- und MSA-Gang, …“.
- alt (Z. 5): „Sinussatz für Seiten und Winkel und Kosinussatz für Seiten: G (Gymnasium Kl. 9, Oberschule 9–10 „in Teilen“)“ → neu: „… G (Gymnasium Kl. 9, Oberschule 9–10 „in Teilen“ – der Sinussatz für Seiten und Winkel gehört seit Fachbrief 10 zu den G-Inhalten, die auch das EBR-Heft prüft, der Kosinussatz nicht; msa-vorgaben.md § 3)“.
- alt (Z. 6): „für die Oberschule nur „in Teilen“, die P10 prüft den Sinussatz trotzdem jährlich.“ → neu: „für die Oberschule nur „in Teilen“; die P10 prüfte den Sinussatz 2014–2025 als Sternaufgabe (Stern = nur FOR), 2022 und 2023 war er durch Vorgabe ausgeschlossen (Fachbrief 5 und 6), seit Fachbrief 10 steht er auf der EBR-Liste der G-Inhalte (msa-vorgaben.md § 2 und 3).“ – „jährlich“ stimmt auch nach Z. 109 nicht (neun von zwölf Jahrgängen).
- alt (Z. 99): „Bedeutung des Sterns für den FOR-Gang beim Prüfungsblatt-Prompt festlegen)“ → neu: „der Stern hieß „nur FOR“ und entfällt ab 2026 mit den getrennten Heften; seit Fachbrief 10 gehören Seite und Winkel mit dem Sinussatz auch zum EBR-Stoff, der Kosinussatz für die Seite nur zum FOR-Stoff)“; in derselben Zeile hinter „Winkel mit dem Sinussatz (RLP G – …)“ einfügen: „, seit Fachbrief 10 auch EBR“.
- alt (Z. 109): „(kein Original 2016, 2022, 2023, 2026)“ → neu: „(kein Original 2016, 2022, 2023, 2026; 2022 und 2023 durch Vorgabe ausgeschlossen, Fachbrief 5 und 6)“.
- Einfügung am Ende von Z. 122: „Mit dem Wegfall des Sterns und der EBR-Liste (Fachbrief 10) trifft die fehlende Basismarke der Einheit 4 ab 2028 auch EBR-Schüler.“
- Marke (Z. 18): nicht betroffen, nichts nachzuziehen. „OS Kl. 10“ kommt aus den Lehrwerksstellen (`_klassen-belege.md` Z. 2048–2084), „P10 oft“ aus `_pruefungswort-belege.md` (Jahrgänge bleiben), „nicht für alle: Sekundo 10 Zusatzstoff“ hängt am Kosinussatz (`_klassen-belege.md` Z. 2083 „Zusatzstoff laut Stoffverteilungsplan [SEKUNDO-BB] Z. 2538 („*“) bei „Kosinussatz““), nicht am Sinussatz. Ein Markenwort für „EBR“ kennt `marken-bau.py` nicht; das wäre eine neue Regel in `_marken-entscheidungen.md`, hier nicht vorgeschlagen.
- P10 (`msa/msa-typen.csv`): Z. 64 „Sinussatz Seite berechnen“, beispiel_id 2025-OS-K4c; Z. 201 „Sinussatz Winkel berechnen“, beispiel_id 2015-GYM-K5b (dazu 2025-GYM-K4b, `msa-katalog-gym.csv` Z. 241). Die Aussage „kein P10-Original“ (Z. 24, 99, 105, 112) gilt damit nur für OS/FOR/EBR, nicht für die GYM-Hefte. Kein EBR-Original: `ebr-vergleich.md` Z. 124 führt „Sinussatz Seite berechnen“ unter „nur B (FOR/OS)“. Das Thema heißt in `msa-typen.csv` inzwischen „Sinus- und Kosinussatz“ (`msa.md` Z. 3), Z. 109 schreibt noch „Thema „Sinussatz““.

**Grund.** Die Stufe G ist richtig und bleibt; falsch wird mit Fachbrief 10 die stillschweigende Gleichung „Sinussatz = Sternstoff = nur FOR“, auf der Z. 2, 6, 99 und 122 stehen.

### 2b Lösbarkeit und Lösungsvielfalt quadratischer Gleichungen (quadratische-gleichungen.md)

**Führt der Eintrag es schon?** Ja, auf G – aber die Form ax² + n = b ist ausdrücklich als GYM und „für EBR und FOR nicht verlangt“ markiert.
- Z. 2 (Kopf): „Oberschule/Gesamtschule Kl. 9–10 (F „in Teilen G“, für den MSA nötig; …)“.
- Z. 5 (Verortung): „Lösbarkeit und Lösungsvielfalt (zwei, eine, keine Lösung); … Stufe G (Gymnasium Kl. 9; Oberschule 9–10 „in Teilen G“, für den MSA nötig)“.
- Z. 6 ([RLP]): „„Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen““ – das Zitat endet vor „und Formulierung diesbezüglicher Aussagen und Begründungen“.
- Z. 9 (Befund 11h): „**Nur Gymnasium und ohne P10-Original:** … die Form Faktor mal Quadrat plus Zahl gleich Zahl (Gymnasium Zeile 1950, in der EBR/FOR-Reihe nicht vorhanden)“.
- Z. 14 (Lerneinheit 1 „Wurzelziehen und Lösbarkeit“): „die allgemeinere Form a·x² + b = c mit Fallbetrachtung (GYM, LISUM-PH Gymnasium Zeile 1950)“; Z. 15: „Marken: OS Kl. 9–10 (Sekundo 10, Schnittpunkt 10, Mathematik heute 9) · GYM Kl. 8–9 (…) · P10 · nicht für alle: Mathematik heute 9 Im Blickpunkt, Mathematik heute 10 Im Blickpunkt“.
- Z. 24 (Typen Einheit 1): „a·x² + b = c mit beliebiger rechter Seite und Fallbetrachtung (GYM)“, „Zahl der Lösungen an c begründen (positiv, null, negativ)“.
- Z. 18 und 26 (Einheit 3): „Diskriminante (zwei, eine, keine Lösung)“; „Zahl der Lösungen am Wert unter der Wurzel beurteilen (der Begriff „Diskriminante“ dafür: GYM …)“; Normieren der allgemeinen Form schon „Niveaumarke überschrieben (GYM-Regel, 2020-OS-K3e)“ (Z. 108).
- Z. 103: „Mindeststoff der Prüfungsvorbereitung (P10, FOR)“ und „GYM-Sprossen …: … die Form a·x² + b = c in Einheit 1“.
- Z. 106 (Sprossen Einheit 1): „rechte Seite beliebig, a·x² + b = c mit Fallbetrachtung (GYM, LISUM-PH Gymnasium Zeile 1950; für EBR und FOR nicht verlangt)“.
- Z. 108 (Sprossen Einheit 3): nach „Wert unter der Wurzel negativ: keine Lösung“ keine Sprosse, die die Zahl der Lösungen an ax² + bx + c = 0 ohne Ausrechnen entscheidet und begründet.

**RLP.** `quelle-rlp-teil-c-mathematik-2023.txt` Z. 2852–2855 (rechte Spalte „Gleichungen und Gleichungssysteme lösen“): „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen und Formulierung diesbezüglicher Aussagen und Begründungen“ – Seitenkopf Z. 2834 „Themenbereich „Gleichungen und Funktionen“ – Niveaustufen G, H“, Block 2836–2855, Randbuchstabe G in Z. 2851 → **G**. Die Form dazu Z. 2842–2844: „Lösen von Gleichungen (auch quadratische Gleichungen der Form d = ax² + bx + c )“, derselbe Block, G. Zweispaltig: die linke Spalte desselben Blocks (Z. 2839–2845, „Übersetzungen zwischen verschiedenen Darstellungen …“) läuft daneben und gehört nicht ins Zitat. Gegenprobe `_niveaustufen-belege.md` Z. 2453–2454: „G [Zeilen 2852–2853]: „Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen“ – Block 2836–2855, Niveaustufe am Block: G (Z2851); zwei, eine oder keine Lösung“; Z. 2485 Sprosse 8 „a·x² + b = c mit Fallbetrachtung (GYM …) → G [Zeilen 2842–2843]; Eintrag: GYM“; Z. 2535–2538 Sprossen 7 und 8 der Einheit 3 → G [Zeilen 2852–2853] – deckt sich. Die GYM-Marke der Form stammt also nicht aus dem RLP, sondern allein aus der LISUM-Gymnasialreihe (Z. 1950).

**Vorschlag.** Befund-Formen zu den Einheiten: ax² + n = b ist a·x² + b = c (Einheit 1), ax² + bx + n = 0 ist die allgemeine Form (Einheit 3, über Normieren und den Wert unter der Wurzel). Die GYM-Marke der Form a·x² + b = c wird nach dem Muster Z. 9/106 überschrieben (P10-Vorgabe vor Planungshilfe):
- alt (Z. 14): „die allgemeinere Form a·x² + b = c mit Fallbetrachtung (GYM, LISUM-PH Gymnasium Zeile 1950)“ → neu: „die allgemeinere Form a·x² + b = c mit Fallbetrachtung (amtlich nur Gymnasialreihe, LISUM-PH Zeile 1950; seit Fachbrief 10 auch EBR-Stoff)“.
- alt (Z. 24): „a·x² + b = c mit beliebiger rechter Seite und Fallbetrachtung (GYM)“ → neu: „a·x² + b = c mit beliebiger rechter Seite und Fallbetrachtung“ (Typklammer, falls `marken-bau.py` eine setzt, bleibt dessen Sache).
- alt (Z. 106): „rechte Seite beliebig, a·x² + b = c mit Fallbetrachtung (GYM, LISUM-PH Gymnasium Zeile 1950; für EBR und FOR nicht verlangt)“ → neu: „rechte Seite beliebig, a·x² + b = c mit Fallbetrachtung und Begründung – amtlich nur in der Gymnasialreihe (Zeile 1950), von der P10-Vorgabe aber für EBR und FOR verlangt (Fachbrief 10: „ax² + n = b“), Niveaumarke überschrieben (GYM-Regel)“.
- Einfügung Z. 108 nach „Wert unter der Wurzel negativ: keine Lösung“: „→ Zahl der Lösungen einer Gleichung a·x² + bx + c = 0 nur am Wert unter der Wurzel entscheiden und begründen, ohne die Lösungen auszurechnen (kein P10-Original; P10-Vorgabe Fachbrief 10 „ax² + bx + n = 0 mit Begründung“, RLP G „Formulierung diesbezüglicher Aussagen und Begründungen“)“. Der Begriff „Diskriminante“ bleibt GYM – die EBR-Liste nennt ihn nicht.
- alt (Z. 103): „Mindeststoff der Prüfungsvorbereitung (P10, FOR) [P10]:“ → neu: „Mindeststoff der Prüfungsvorbereitung (P10, FOR; Lösbarkeit und Lösungsvielfalt seit Fachbrief 10 auch EBR) [P10]:“; aus der Liste „GYM-Sprossen …“ „die Form a·x² + b = c in Einheit 1,“ streichen und in die Liste „Nicht GYM, obwohl amtlich nur in der Gymnasialreihe“ aufnehmen: „der Nullfall der quadrierten Klammer (Einheit 1), das Normieren der allgemeinen Form (Einheit 3) und seit Fachbrief 10 die Form a·x² + b = c (Einheit 1)“.
- Einfügung am Ende von Z. 9: „Nachtrag (Fachbrief 10, msa-vorgaben.md § 3): Die Form Faktor mal Quadrat plus Zahl gleich Zahl ist für EBR und FOR prüfungsrelevant und wechselt in die zweite Gruppe; damit überschreibt die P10 drei der sechs Unterschiede.“ – bisher nennt Z. 9 „drei“, führt aber nur zwei auf (Nullfall, Normieren); die Zahl stimmt erst mit diesem Nachtrag.
- alt (Z. 6): „„Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen““ → neu: „„Untersuchen von Fragen der Lösbarkeit und der Lösungsvielfalt von quadratischen Gleichungen und Formulierung diesbezüglicher Aussagen und Begründungen““ (RLP Z. 2852–2855; die Begründung ist genau der Teil, den die EBR-Zeile betont).
- alt (Z. 2): „(F „in Teilen G“, für den MSA nötig; …“ → neu: „(F „in Teilen G“, für den MSA nötig; Lösbarkeit und Lösungsvielfalt seit Fachbrief 10 auch auf EBR-Niveau prüfungsrelevant; …“.
- Marke (Z. 15, Z. 19): nicht betroffen – Lehrwerksstellen und P10-Jahrgänge ändern sich nicht. Die neue Sprosse in Einheit 3 verschiebt die Sprossenzählung; `_niveaustufen-belege.md` (und jede andere aus den Sprossen abgeleitete Datei) ist danach neu zu bauen, nicht von Hand. Zielmarken bleiben unverändert.
- P10 (`msa/msa-typen.csv`): Z. 154 „Lösbarkeit quadratischer Gleichung beurteilen“, beispiel_id 2021-OS-K7c, Definition „… einer quadratischen Gleichung in Scheitelpunktform prüfen und eine Gleichung ohne Lösung angeben“ – enger als die EBR-Zeile (keine Form ax² + n = b, keine allgemeine Form); zweites Original im GYM-Heft 2017-GYM-K2a (`msa-katalog-gym.csv` Z. 82, CSV-Thema Quadratische Funktionen, f(x) = (x − 3)² + 1,5 hat keine Nullstellen), im Eintrag nicht genannt. Z. 136 „Lösung durch Einsetzen prüfen“, beispiel_id 2025-OS-B1h (Einheit 2). Kein EBR-Original: `ebr-vergleich.md` Z. 84 führt den Typ unter „nur B (FOR/OS)“.

**Grund.** Der Eintrag schließt mit „für EBR und FOR nicht verlangt“ (Z. 106) genau die Form aus, die Fachbrief 10 für EBR neu verlangt; nach der eigenen GYM-Regel des Eintrags geht die Prüfungsvorgabe der Planungshilfe vor.

## 3 msa/msa-katalog-gym.csv, Zeile 2025-GYM-K5d: Nebentyp „Mantellinie Kegel bestimmen“

**Wortlaut der Aufgabe** (Heft `hefte/msa/sonstiges/25_P10_Ma_Gym_A2.pdf`, S. 6–7, Textfassung mit `pdftotext -layout`; das Heft liegt lokal, nicht im Repo): Aufgabe 5 „Verpackung“ (13 Punkte). Stamm: „Diese Verpackung hat die Form eines 10 cm hohen geraden Prismas. Die Grundfläche ist ein gleichschenkliges Trapez. Die zueinander parallel verlaufenden Seiten dieses Trapezes sind 6 cm und 12 cm lang. […] Ihr Abstand beträgt 6 cm.“ Teilaufgabe d) (4 P): „Die Abbildung 2 zeigt ein Netz dieser Verpackung. Zwei Flächen werden vollständig mit einer Folie, auf der Blumenmotive abgebildet sind, beklebt. Berechnen Sie, wie viel Quadratzentimeter Folie benötigt werden.“

**Zeile heute:** typ „Mantelfläche Prisma berechnen“, typ_neben „Mantellinie Kegel bestimmen“; verfahren „Schenkellänge über Pythagoras: √(((12−6):2)² + 6²) = √(3² + 6²) = √45 = 3√5 cm; jede Schenkelfläche (Rechteck) hat die Fläche Schenkellänge · 10 cm; zwei Flächen zusammen“, ergebnis „3√5 cm ≈ 6,71 cm; Folie insgesamt ≈ 134,2 cm²“.

**Befund:** In der Aufgabe kommt kein Kegel vor. Der Nebenschritt ist die Hypotenuse des Stützdreiecks im gleichschenkligen Trapez aus halber Seitendifferenz (3 cm) und Höhe (6 cm). „Mantellinie Kegel bestimmen“ (Thema Satz des Pythagoras, Definition „Mantellinie eines Kegels aus Radius und Höhe über den Satz des Pythagoras berechnen“, beispiel_id 2018-OS-K6d) benennt denselben Rechenschritt an einem anderen Gegenstand; der Katalog führt ihn sonst nur an Kegeln (2018-OS-K6d Haupttyp, 2021-GYM-K5b Nebentyp am Messbecher-Kegel).

**Vorschlag:** typ_neben „Mantellinie Kegel bestimmen“ → „Pythagoras Hypotenuse“ (msa-typen.csv: „Hypotenuse eines rechtwinkligen Dreiecks aus beiden Katheten berechnen“, beispiel_id 2025-OS-K2a, Thema Satz des Pythagoras). Grund nach Kern § 6 (katalog-prompt.md): ein Typ ist Gegenstand plus Handlung; der Gegenstand hier ist ein Dreieck im Trapez, nicht ein Kegel – das vorhandene Etikett, das die Fertigkeit trifft, ist die Hypotenuse aus zwei Katheten; ein neuer Typ ist nicht nötig. Nicht „Umfang Trapez berechnen“: der Typ verlangt den Umfang, hier ist nur der Schenkel Zwischenschritt einer Mantelflächenrechnung. Ausführen im msa-Abgleich über `werkzeuge/typen-abgleich.py` ist nicht möglich (das Skript benennt Typen um oder zieht sie zusammen, es ändert kein einzelnes typ_neben); die Änderung gehört in einen Heftlauf-Nachtrag über `msa/msa-bau.py` für 2025-GYM oder in eine Erweiterung des Abgleich-Skripts um Einzelzeilen – das entscheidet der Chat.

## 4 Namensabweichungen (katalog/_verweise.md, Prüfung 3 (b))

Stand der Fundstelle nach dem Neubau im Auftrag Nacht 2026-09-27 (Teil 4): **28 Einträge** mit Abweichung (bis Teil 4 waren es 27; neu ist strahlensaetze.md, seit themen.csv den Maßstab dort führt). Sorte „fhr-Titel systematisch“: H1 gleich den abi/iqb-Themen, nur die fhr-Themen weichen ab; „msa-Titel“: eine Übereinstimmung, nur msa weicht ab; „ohne Übereinstimmung“: kein thema-Wert gleicht der H1. Die thema-Werte sind das Vokabular der Prüfungskataloge (fhr.md, msa.md, abitur-vokabular.md) und werden dort von den Bau-Skripten geprüft; sie zu ändern hieße, Katalogzeilen umzuetikettieren – deshalb schlägt keine Zeile „thema-Wert ändern“ vor.

| Eintrag | H1 | thema-Werte (abweichend) | Sorte | Vorschlag | Grund |
|---|---|---|---|---|---|
| ableitungsregeln.md | Ableitungsregeln | fhr „Ableitungen bilden“ | fhr-Titel systematisch | Sammelthema, so lassen | fhr benennt die Handlung, der Eintrag das Sachgebiet; themen.csv bildet es ab. |
| daten.md | Daten | msa „Kenngrößen“, „Diagramme lesen und beurteilen“, „Daten darstellen“; fhr „Statistische Kenngrößen“, „Daten darstellen und aufbereiten“; iqb „Lage- und Streumaße einer Stichprobe“ | ohne Übereinstimmung | Sammelthema, so lassen | Sechs Prüfungsthemen aus drei Profilen in sieben Einheiten; kein einzelnes Thema passt als Titel. |
| einheiten.md | Größen und Einheiten | msa „Einheiten umrechnen“ | msa-Titel | Sammelthema, so lassen | Der Eintrag führt auch Schätzen und Rechnen mit Größen; die H1 gleicht dem fhr-Thema. |
| extremalprobleme.md | Extremalprobleme | fhr „Extremwertaufgaben“ | fhr-Titel systematisch | Sammelthema, so lassen | Synonym aus der fhr-Themenliste; der Eintrag folgt dem abitur-Vokabular. |
| flaechen.md | Flächen | msa „Flächeninhalt und Umfang“ | ohne Übereinstimmung | Sammelthema, so lassen | Das msa-Thema umfasst auch die Kreistypen, die kreis.md führt; „Flächen“ ist der Teil ohne Kreis. |
| flaecheninhalt-durch-integration.md | Flächeninhalt durch Integration | fhr „Fläche zwischen Graph und x-Achse“, „Fläche zwischen zwei Graphen“, „Körpervolumen aus Grundfläche und Länge“ | fhr-Titel systematisch | Sammelthema, so lassen | Drei feinere fhr-Themen in einem Eintrag. |
| funktionsklassen-und-eigenschaften.md | Funktionsklassen und Eigenschaften | fhr „Graph zeichnen und zuordnen“, „Nullstellen ganzrationaler Funktionen“, „Symmetrie nachweisen“ | fhr-Titel systematisch | Sammelthema, so lassen | Drei feinere fhr-Themen in einem Eintrag. |
| gleichungen-loesen.md | Gleichungen lösen | fhr „Schnittpunkte von Funktionsgraphen“ | fhr-Titel systematisch | Sammelthema, so lassen | fhr prüft das Gleichungslösen als Schnittpunktsuche; dazu offen (d): fhr-typen.csv kennt „Gleichungen lösen“ ohne themen.csv-Zeile (Posten in faellig.md § 2). |
| grenzwerte-und-verhalten-im-unendlichen.md | Grenzwerte und Verhalten im Unendlichen | fhr „Verhalten im Unendlichen“ | fhr-Titel systematisch | Sammelthema, so lassen | Teilmenge des Titels; nichts zu tun. |
| kenngroessen-von-verteilungen.md | Kenngrößen von Verteilungen | fhr „Erwartungswert“ | fhr-Titel systematisch | Sammelthema, so lassen | fhr prüft nur den Erwartungswert. |
| koerper.md | Körper | msa „Volumen und Oberfläche“, „Körper, Netze, Schrägbilder“ | ohne Übereinstimmung | Sammelthema, so lassen | Zwei msa-Themen in einem Eintrag. |
| kombinatorik.md | Kombinatorik | fhr „Kombinatorische Abzählverfahren“ | fhr-Titel systematisch | Sammelthema, so lassen | Synonym aus der fhr-Themenliste. |
| kurvenuntersuchung.md | Kurvenuntersuchung | fhr „Extrem- und Sattelpunkte“, „Wendepunkte“, „Monotonie und Krümmung“ | fhr-Titel systematisch | Sammelthema, so lassen | Drei feinere fhr-Themen in einem Eintrag. |
| potenz-exponentialfunktionen.md | Potenz- und Exponentialfunktionen, Wachstum und Zerfall | msa „Exponentialfunktionen und Wachstum“ | ohne Übereinstimmung | Sammelthema, so lassen | Seit Einheit 5 führt der Eintrag auch die Potenzfunktionen, die das msa-Thema nicht hat; die H1 trifft jetzt genau. |
| potenzen-wurzeln.md | Potenzen, Zehnerpotenzen und Quadratwurzeln | msa „Potenzen und Wurzeln“, „Zehnerpotenzen und Näherungswerte“ | ohne Übereinstimmung | Sammelthema, so lassen | Zwei msa-Themen in einem Eintrag. |
| rationale-zahlen.md | Rationale Zahlen | msa „Rationale Zahlen rechnen“ | ohne Übereinstimmung | Sammelthema, so lassen | Der Eintrag führt auch Ordnen und Zahlengerade; das msa-Thema nur das Rechnen. |
| rekonstruktion-von-funktionsgleichungen.md | Rekonstruktion von Funktionsgleichungen | fhr „Funktionsgleichung bestimmen“ | fhr-Titel systematisch | Sammelthema, so lassen | Synonym aus der fhr-Themenliste. |
| rotationsvolumen.md | Rotationsvolumen | fhr „Rotationsvolumen um die x-Achse“ | fhr-Titel systematisch | Sammelthema, so lassen | Teilmenge des Titels. |
| strahlensaetze.md | Maßstab, Ähnlichkeit und Strahlensätze | msa „Maßstab“ | ohne Übereinstimmung | Sammelthema, so lassen | Neu seit Teil 4; dazu prüfen, ob msa „Ähnlichkeit und Strahlensätze“ (msa-typen.csv, Prüfung 3 (d): ohne themen.csv-Zeile, weil nur GYM-Zeilen) eine themen.csv-Zeile bei strahlensaetze bekommt. |
| symmetrie-abbildungen.md | Symmetrie, Abbildungen und Koordinatensystem | msa „Symmetrie und Abbildungen“ | ohne Übereinstimmung | Sammelthema, so lassen | Der Eintrag führt zusätzlich das Koordinatensystem (Einheit 1). |
| tangente-normale-schnittwinkel.md | Tangente, Normale, Schnittwinkel | fhr „Anstieg und Tangente“, „Normale“ | fhr-Titel systematisch | Sammelthema, so lassen | Zwei feinere fhr-Themen. |
| terme.md | Terme | msa „Terme umformen“, fhr „Terme umformen“ | ohne Übereinstimmung | Sammelthema, so lassen | Der Eintrag führt auch das Aufstellen (Einheit 1); die H1 ist weiter als das Prüfungsthema. |
| trigonometrie.md | Trigonometrie | msa „Trigonometrie im rechtwinkligen Dreieck“, „Sinus- und Kosinussatz“ | ohne Übereinstimmung | Sammelthema, so lassen | Zwei msa-Themen in einem Eintrag; dazu offen Kennzahl 6 „Sinus- und Kosinussatz“ ohne Zuordnung in index.md. |
| unabhaengigkeit.md | Unabhängigkeit | fhr „Unabhängigkeit von Ereignissen“ | fhr-Titel systematisch | Sammelthema, so lassen | Synonym aus der fhr-Themenliste. |
| wahrscheinlichkeit.md | Wahrscheinlichkeit | msa „Wahrscheinlichkeit mehrstufig“, „Wahrscheinlichkeit einstufig“, „Zählen und Kombinatorik“ | ohne Übereinstimmung | Sammelthema, so lassen | Drei msa-Themen in einem Eintrag. |
| winkel-dreiecke.md | Winkel und Dreiecke | msa „Ebene Figuren und Winkel“ | ohne Übereinstimmung | Sammelthema, so lassen | Das msa-Thema umfasst auch Vierecke, die der Eintrag nur als Einheit 3 führt; ein Umbenennen der H1 in „Ebene Figuren und Winkel“ wäre möglich, trüge aber Flächen- und Kreisstoff mit, der anderswo liegt. |
| zufallsexperimente-und-pfadregeln.md | Zufallsexperimente und Pfadregeln | fhr „Mehrstufige Zufallsexperimente“, „Laplace-Wahrscheinlichkeit“, „Baumdiagramm und Pfadregeln“; abi und iqb „Baumdiagramm und Pfadregeln“, „Zufallsexperimente und Urnenmodelle“, „Ereignisse und Mengenoperationen“ | ohne Übereinstimmung | Sammelthema, so lassen | Trägerthema nach Entscheidung 37 unter eigenem kanonischem Namen; neun Profilthemen. |
| zuordnungen.md | Zuordnungen | msa „Zuordnungen proportional und antiproportional“ | ohne Übereinstimmung | Sammelthema, so lassen | Einheit 1 (Darstellen, Zuordnungen allgemein) liegt außerhalb des Prüfungsthemas. |

Zusammen: 13 fhr-Titel systematisch, 1 msa-Titel, 14 ohne Übereinstimmung. Ergebnis der Durchsicht: keine Abweichung ist ein Versehen; die H1 folgt dem didaktischen Zuschnitt des Eintrags, die thema-Werte dem Vokabular der Prüfungskataloge, themen.csv verbindet beide. Vorschlag für den Posten in faellig.md § 2: als „Absicht (Sammelthemen), kein Handlungsbedarf“ schließen; die Prüfung 3 (b) von `werkzeuge/verweis-pruef.py` könnte die Sorten künftig selbst ausweisen.
