# Rohdatei wahrscheinlichkeit

Stufe: I

- msa: Wahrscheinlichkeit mehrstufig (18 Zeilen)
- msa: Wahrscheinlichkeit einstufig (15 Zeilen)
- msa: Zählen und Kombinatorik (6 Zeilen)

Stand: 2026-09-25, Commit 25322c5

## A Typenprofil

**Wahrscheinlichkeit einstufig** · 13 Zeilen · msa 13 · Jahre 2014–2026
msa/msa-typen.csv (gültig): Laplace-Wahrscheinlichkeit eines Ergebnisses als günstige durch mögliche Fälle angeben.

**Baumdiagramm ergänzen** · 7 Zeilen · msa 7 · Jahre 2014–2026
msa/msa-typen.csv (gültig): Fehlende Wahrscheinlichkeiten in einem Baumdiagramm eintragen (Knotensumme 1, Astwahrscheinlichkeiten aus dem Sachverhalt).

**Wahrscheinlichkeit mehrstufig unabhängig** · 4 Zeilen · msa 4 · Jahre 2014–2025
msa/msa-typen.csv (gültig): Wahrscheinlichkeit eines Ergebnisses oder Ereignisses in einem zwei- oder dreistufigen Versuch mit unabhängigen Stufen (mehrere Geräte, mit Zurücklegen) mit Pfad- und Summenregel berechnen; Stufenzahl steht in gegeben und schritte.

**Zufallsgerät zu Wahrscheinlichkeit entwerfen** · 4 Zeilen · msa 4 · Jahre 2018–2026
msa/msa-typen.csv (gültig): Ein Zufallsgerät (Scheibe, Urne) so belegen, dass eine vorgegebene Wahrscheinlichkeit entsteht, ein- oder mehrstufig: Belegung einzeichnen oder die Anzahl der Felder bzw. Kugeln berechnen, mit Rechnung als Nachweis; die Leistung steht in format.

**Ergebnismenge aufzählen** · 3 Zeilen · msa 3 · Jahre 2017–2025
msa/msa-typen.csv (gültig): Alle möglichen Ergebnisse eines mehrstufigen Zufallsversuchs auflisten.

**Wahrscheinlichkeit mehrstufig ohne Zurücklegen** · 3 Zeilen · msa 3 · Jahre 2018–2024
msa/msa-typen.csv (gültig): Wahrscheinlichkeit in einem zwei- oder dreistufigen Versuch ohne Zurücklegen berechnen; jede Stufe hängt von der vorigen ab (verkleinerte Grundmenge); Stufenzahl steht in gegeben und schritte.

**Anzahl der Anordnungen bestimmen** · 2 Zeilen · msa 2 · Jahre 2016–2017
msa/msa-typen.csv (gültig): Anzahl der Reihenfolgen (Permutationen) einer kleinen Menge verschiedener Elemente durch Auflisten oder Zählprinzip bestimmen.

**Anzahl der Dreiecke aus Punkten bestimmen** · 1 Zeile · msa 1 · Jahre 2015
msa/msa-typen.csv (gültig): Anzahl der Dreiecke mit Ecken aus einer kleinen Punktmenge einer Figur bestimmen; Punkte auf einer Geraden ergeben kein Dreieck.

**Größte Zahl aus Ziffern bilden** · 1 Zeile · msa 1 · Jahre 2016
msa/msa-typen.csv (gültig): Aus gegebenen Ziffern durch Anordnen die größte (oder kleinste) Zahl bilden.

**Wahrscheinlichkeit über Gegenereignis berechnen** · 1 Zeile · msa 1 · Jahre 2026
msa/msa-typen.csv (gültig): Wahrscheinlichkeit eines mit „nicht“ oder „mindestens“ formulierten Ereignisses über 1 − P(Gegenereignis) berechnen.

**Nebentypen:** Behauptung prüfen (6) · Wahrscheinlichkeit mehrstufig unabhängig (6) · Wahrscheinlichkeit einstufig (3) · Wahrscheinlichkeit mehrstufig ohne Zurücklegen (3) · Prozent und Anteil umwandeln (2) · Ergebnismenge aufzählen (1) · Gleichung im Sachzusammenhang deuten (1)

## B Zeilenliste

## msa

2016-OS-K5b | 2 | ja | Kurzantwort¦Kurzantwort · Geben Sie an¦Geben Sie an | Ziffern 2, 3, 6 nacheinander gezogen → alle dreistelligen Gewinnzahlen¦P(Gewinnzahl gerade) | 236, 263, 326, 362, 623, 632; gerade = Endziffer 2 oder 6: 4 von 6
2017-OS-K6b | 4 | ja | Kurzantwort¦Kurzantwort¦Rechnung · Geben Sie an¦Geben Sie an¦Ermitteln Sie | Ziffern 5, 7, 9, jede genau einmal; eine Nummer richtig; Versuche ohne Wiederholung → Anzahl der möglichen Nummern¦P(richtig beim ersten Versuch)¦P(richtig spätestens beim zweiten Versuch) | 3 · 2 · 1 = 6 (579, 597, 759, 795, 957, 975); 1/6; 1/6 + 5/6 · 1/5 = 2/6
2015-OS-K5a | 1 | ja | Ankreuzen · Kreuzen Sie an | fünf Punkte A, B, C, D, E; E liegt auf AC und auf BD; Auswahl 6, 8, 10, 12 → Anzahl verschiedener Dreiecke mit drei dieser Punkte als Ecken | 10 Dreierauswahlen aus 5 Punkten, davon 2 auf einer Geraden (A, E, C und B, E, D) → 8
2014-OS-K6b | 2 | ja | Eintragen · Ergänzen Sie | Glücksrad 4 × A, 3 × B, 1 × C; Baum für zwei Drehungen, nur P(C) = 1/8 in der ersten Stufe eingetragen → alle fehlenden Wahrscheinlichkeiten | P(A) = 4/8 = 1/2, P(B) = 3/8, P(C) = 1/8 auf beiden Stufen (unabhängig)
2015-OS-K7d | 4 | ja | Eintragen¦Rechnung · Vervollständigen Sie¦Tragen Sie ein¦Berechnen Sie | 11 Spieler, jeder höchstens einmal, Reihenfolge zufällig; Ereignis: Ronny unter den ersten drei Schützen; Baum mit R/nR je Stufe, nur nR verzweigt weiter; vorgegeben 1/11 (1. Stufe R) und 9/10 (2. Stufe nR) → vier fehlende Wahrscheinlichkeiten¦P(Ronny unter den ersten drei) | 1. Stufe nR = 10/11; 2. Stufe R = 1/10; 3. Stufe R = 1/9, nR = 8/9; P = 1/11 + 10/11 · 1/10 + 10/11 · 9/10 · 1/9 = 3/11 (oder 1 − 10/11 · 9/10 · 8/9)
2019-OS-K6b | 5 | ja | Eintragen¦Ankreuzen · Ergänzen Sie¦Entscheiden Sie¦Kreuzen Sie an | Kiste mit 20 Buntstiften: 7 grün, 4 rot, 3 gelb, 6 blau; drei Stifte nacheinander ohne Zurücklegen; Baum rot/nicht rot mit 4/20, 3/19 und 2/18 am fetten Pfad rot–rot–rot; zwei Felder leer: Stufe 1 nicht rot; Stufe 3 rot nach nicht rot → rot; Aussagen zum fetten Pfad: 1 Marie greift drei unterschiedlich farbige Stifte; 2 Marie legt den Stift nach jedem Ziehen zurück; 3 die Wahrscheinlichkeit des Pfades ist kleiner als 1 % → zwei fehlende Wahrscheinlichkeiten¦wahr/falsch je Aussage | nicht rot = 16/20; nach nicht rot und rot bleiben 18 Stifte mit 3 roten: 3/18; fetter Pfad = dreimal rot ohne Zurücklegen, P = 4/20 · 3/19 · 2/18
2020-OS-K6c | 3 | ja | Eintragen¦Rechnung · Vervollständigen Sie¦Berechnen Sie | drei Würfe; Max zahlt, wenn Lisa mindestens zweimal eine 6 würfelt; Baumdiagramm ohne Wahrscheinlichkeiten → Astwahrscheinlichkeiten¦P(mindestens zwei Sechsen) | jeder Ast 1/6 bzw. 5/6; Pfade mit genau zwei Sechsen 3 · (1/6)² · 5/6 = 15/216, drei Sechsen 1/216, addieren
2024-OS-K5b | 3 | ja | Eintragen¦Rechnung · Ergänzen Sie¦Weisen Sie nach | fünf Zettel: Müll rausbringen, Spülmaschine ausräumen, Staubsaugen, Einkaufen, Joker; jedes der 5 Kinder zieht am Wochenanfang genau einen Zettel; Benjamin zieht jede Woche als Erster (jede Woche alle fünf Zettel); Behauptung: P(Joker in beiden Wochen) = 1/25 → fehlende Wahrscheinlichkeiten¦Nachweis von 1/25 | 1. Woche kein Joker 4/5, Joker 1/5; 2. Woche ebenso an beiden Ästen; Pfad Joker–Joker 1/5 · 1/5
2026-EBR-K6b | 4 | ja | Eintragen¦Rechnung · Ergänzen Sie¦Ermitteln Sie | Würfel A mit den Zahlen 1, 1, 2, 2, 4, 5; Würfel B mit 1, 1, 2, 3, 3, 3; erst A, dann B geworfen; betrachtet wird gerade/ungerade; im Baum vorgegeben P(A gerade) = 3/6 und P(B gerade ¦ A gerade) = 1/6 → fehlende Wahrscheinlichkeiten im Baum¦P(beide ungerade) | A ungerade 3/6; bei B gerade 1/6 und ungerade 5/6 auf beiden Ästen; Pfadregel 3/6 · 5/6
2026-FOR-K6b | 4 | ja | Eintragen¦Rechnung · Ergänzen Sie¦Ermitteln Sie | Würfel A mit den Zahlen 1, 1, 2, 2, 4, 5; Würfel B mit 1, 1, 2, 3, 3, 3; erst A, dann B geworfen; betrachtet wird gerade/ungerade; im Baum vorgegeben P(A gerade) = 3/6 und P(B gerade ¦ A gerade) = 1/6 → fehlende Wahrscheinlichkeiten im Baum¦P(beide ungerade) | A ungerade 3/6; bei B gerade 1/6 und ungerade 5/6 auf beiden Ästen; Pfadregel 3/6 · 5/6
2017-OS-B1f | 1 | ja | Kurzantwort · Geben Sie an | zwei gleiche Münzen gleichzeitig; Ergebnisse Z oder W → Anzahl der möglichen Ergebnisse | ZZ, ZW, WZ, WW
2020-OS-K6a | 3 | ja | Kurzantwort¦Rechnung · Notieren Sie¦Ermitteln Sie¦Geben Sie an | Würfel zweimal geworfen, 36 Augenpaare, (2,1) und (1,2) verschieden → alle Paare mit zweiter Augenzahl 2¦P(zweiter Wurf 2) in Prozent | (1,2), (2,2), …, (6,2) aufzählen; 6 von 36
2025-OS-K3a | 1 | ja | Kurzantwort · Notieren Sie | zwei Scheiben mit je vier gleich großen Sektoren, links 1, 2, 1, 3, rechts 2, 3, 2, 1; beide werden gleichzeitig gedreht, gelesen wird erst die linke, dann die rechte Ziffer (Beispiel 12) → alle möglichen zweistelligen Zahlen | jede linke Ziffer 1, 2, 3 mit jeder rechten Ziffer 1, 2, 3 kombinieren
2016-OS-K5a | 1 | ja | Kurzantwort · Geben Sie an | Ziffern 2, 3, 6, jede einmal → größte dreistellige Zahl | Ziffern absteigend ordnen
2014-OS-B1b | 1 | ja | Kurzantwort · Geben Sie an | Lostrommel mit 80 Nieten und 20 Gewinnlosen → P(Gewinn) | 20 : (80 + 20)
2014-OS-B1d | 1 | ja | Kurzantwort · Geben Sie an | ein Wurf mit einem Spielwürfel; Ereignis: weder 1 noch 6 → P(weder 1 noch 6) | günstig 2, 3, 4, 5 → 4/6 (oder 1 − 2/6)
2014-OS-K6a | 2 | ja | Kurzantwort¦Kurzantwort · Ermitteln Sie¦Notieren Sie | Glücksrad mit 8 gleich großen Feldern: 4 × A, 3 × B, 1 × C → P(B) als Bruch¦P(B) in Prozent | 3 : 8 = 0,375
2015-OS-B1a | 1 | ja | Ankreuzen · Kreuzen Sie an | drei Töpfe mit je 6 Kugeln: links 4 weiße/2 graue, Mitte 2 weiße/4 graue, rechts 3 weiße/3 graue; P(weiß) soll 50 % sein → der Topf mit P(weiß) = 50 % | Anteil weißer Kugeln je Topf: 4/6, 2/6, 3/6; 50 % = die Hälfte
2016-OS-B1f | 1 | ja | Kurzantwort · Geben Sie an | 100 Lampen, 5 kaputt; eine wird entnommen → P(kaputt) | 5 von 100
2016-OS-K5c | 2 | ja | Begründung · Begründen Sie | Lose 101 bis 900; ein Hauptgewinn 326; Behauptung P = 1/800 → Begründung | 900 − 101 + 1 = 800 Lose, eines gewinnt
2016-OS-K5d | 3 | ja | Begründung · Begründen Sie | Lose 101–900; Trostpreis bei Endung 26 außer 326; Anne sieht Endziffer 6; Behauptung P = 7/80 → Entscheidung mit Begründung | Lose mit Endziffer 6: 106, 116, …, 896 = 80; davon Endung 26: 126, 226, …, 826 = 8, ohne 326 bleiben 7
2017-OS-K6a | 2 | ja | Kurzantwort · Geben Sie an | dritter Ring mit Ziffern 0 bis 9, eine richtig → P(richtige Ziffer beim ersten Versuch) als Bruch und in Prozent | 1 günstige von 10 möglichen
2018-OS-K7b | 2 | ja | Begründung · Entscheiden Sie¦Begründen Sie | 16 Pfannkuchen (14 Marmelade, 2 Senf); Tom hat zwei mit Marmelade genommen; Pia: P(Senf) = 2/16 → Entscheidung mit Begründung | nur noch 14 Pfannkuchen, davon 2 mit Senf: 2/14
2019-OS-K6a | 1 | ja | Kurzantwort · Geben Sie an | Kiste mit 20 Buntstiften: 7 grün, 4 rot, 3 gelb, 6 blau; ein Stift wird gegriffen und zurückgelegt → P(gelb) | günstige durch mögliche: 3/20
2024-OS-K5a | 1 | ja | Kurzantwort · Geben Sie an | fünf Zettel: Müll rausbringen, Spülmaschine ausräumen, Staubsaugen, Einkaufen, Joker; jedes der 5 Kinder zieht am Wochenanfang genau einen Zettel → P(erstes Kind zieht Staubsaugen) | ein günstiger von fünf Zetteln
2026-EBR-K6a | 1 | ja | Kurzantwort · Geben Sie an | Würfel A mit den Zahlen 1, 1, 2, 2, 4, 5; Würfel B mit 1, 1, 2, 3, 3, 3; Würfel A wird einmal geworfen → P(2) bei Würfel A | zwei von sechs Flächen zeigen 2
2026-FOR-K6a | 1 | ja | Kurzantwort · Geben Sie an | Würfel A mit den Zahlen 1, 1, 2, 2, 4, 5; Würfel B mit 1, 1, 2, 3, 3, 3; Würfel A wird einmal geworfen → P(2) bei Würfel A | zwei von sechs Flächen zeigen 2
2018-OS-K7c | 4 | ja | Kurzantwort¦Rechnung¦Kurzantwort · Nennen Sie¦Ermitteln Sie¦Formulieren Sie | 16 Pfannkuchen (14 Marmelade M, 2 Senf S); zwei nacheinander zufällig ohne Zurücklegen; Rechnung P(E) = 2/16 · 1/15 + 14/16 · 13/15 → alle Ergebnisse mit mindestens einem Senf-Pfannkuchen¦P(beide Marmelade)¦Ereignis E zur Rechnung in Worten | Ergebnisse (S;M), (M;S), (S;S); P(M;M) = 14/16 · 13/15; E: beide gleich (beide Senf oder beide Marmelade)
2019-OS-K6c | 3 | ja | Rechnung¦Begründung · Begründen Sie rechnerisch | Kiste mit 20 Buntstiften: 7 grün, 4 rot, 3 gelb, 6 blau; drei Stifte nacheinander ohne Zurücklegen; Behauptung: P(3 blau) ist doppelt so hoch wie P(3 gelb) → Widerlegung mit Rechnung | P(3 blau) = 6/20 · 5/19 · 4/18; P(3 gelb) = 3/20 · 2/19 · 1/18; Quotient bilden
2024-OS-K5c | 2 | ja | Rechnung · Ermitteln Sie | fünf Zettel: Müll rausbringen, Spülmaschine ausräumen, Staubsaugen, Einkaufen, Joker; jedes der 5 Kinder zieht am Wochenanfang genau einen Zettel; Benjamin zieht als Erster, Klara als Zweite (aus den verbleibenden vier Zetteln) → P(Klara zieht in Woche 1 den Joker) | Benjamin kein Joker 4/5, dann Klara Joker aus 4 Zetteln 1/4: 4/5 · 1/4
2014-OS-K6c | 2 | ja | Rechnung · Berechnen Sie | Glücksrad 4 × A, 3 × B, 1 × C, zweimal gedreht; Ereignis: zweimal derselbe Buchstabe → P(AA oder BB oder CC) | (1/2)² + (3/8)² + (1/8)² = 16/64 + 9/64 + 1/64
2020-OS-K6b | 3 | ja | Ankreuzen¦Begründung · Entscheiden Sie¦Begründen Sie | zwei Würfe; Behauptung: P(zwei gleiche Augenzahlen) > P(zuerst eine 6); Ankreuzfelder „Max hat Recht“ / „Max hat nicht Recht“ → Entscheidung¦Begründung mit Wahrscheinlichkeiten | P(gleich) = 6/36 = 1/6; P(erst 6) = 1/6 (zweiter Wurf beliebig); gleich groß
2025-OS-K3b | 3 | ja | Rechnung¦Begründung · Berechnen Sie¦Entscheiden Sie¦Begründen Sie | zwei Scheiben mit je vier gleich großen Sektoren, links 1, 2, 1, 3, rechts 2, 3, 2, 1; beide werden gleichzeitig gedreht, gelesen wird erst die linke, dann die rechte Ziffer (Beispiel 12); Behauptung von Esra: P(22) ist gleich P(33) → P(33)¦Entscheidung zur Behauptung mit Begründung | P(3 links) = 1/4, P(3 rechts) = 1/4, Pfadregel multiplizieren; für 22 ist P = 1/4 · 2/4
2025-OS-K3c | 2 | ja | Rechnung · Bestimmen Sie | zwei Scheiben mit je vier gleich großen Sektoren, links 1, 2, 1, 3, rechts 2, 3, 2, 1; beide werden gleichzeitig gedreht, gelesen wird erst die linke, dann die rechte Ziffer (Beispiel 12) → P(12 oder 21) | P(12) = 2/4 · 2/4 = 4/16, P(21) = 1/4 · 1/4 = 1/16, addieren
2026-FOR-K6c | 2 | ja | Rechnung · Bestimmen Sie | Würfel A mit den Zahlen 1, 1, 2, 2, 4, 5; Würfel B mit 1, 1, 2, 3, 3, 3; erst A, dann B; E: „Es wird nicht zweimal eine gerade Zahl gewürfelt.“ → P(E) | Gegenereignis zweimal gerade: 3/6 · 1/6 = 3/36; P(E) = 1 − 3/36
2018-OS-B1j | 1 | ja | Kurzantwort · Geben Sie an | 5 gleich große Felder (rot, grün, weiß); P(rot) = 40 % → Anzahl der roten Felder | 40 % von 5 = 2
2019-OS-B1g | 1 | ja | Zeichnen · Zeichnen Sie ein | Gefäß mit 4 schwarzen Kugeln (gezeichnet) und unbekannt vielen weißen; Baumdiagramm: P(schwarz) = 2/3, P(weiß) = 1/3 → fehlende weiße Kugeln einzeichnen | 4 schwarze sind 2/3, also 6 Kugeln insgesamt, 2 weiße
2025-OS-K3d | 2 | ja | Eintragen¦Rechnung · Tragen Sie ein¦Begründen Sie durch eine Rechnung | zwei leere Scheiben mit je vier gleich großen Sektoren; gelesen wird erst links, dann rechts; Zielwert P(13) = 25 % → Ziffern je Sektor¦Rechnung, die P(13) = 1/4 zeigt | 1/4 als Produkt zweier Sektoranteile schreiben, z. B. 2/4 · 2/4, 1 · 1/4 oder 1/4 · 1, und die Scheiben entsprechend belegen
2026-FOR-K6d | 2 | ja | Eintragen¦Rechnung · Beschriften Sie¦Zeigen Sie durch eine Rechnung | Würfel A mit den Zahlen 1, 1, 2, 2, 4, 5; Würfel B mit 1, 1, 2, 3, 3, 3; bei Würfel B wird genau eine Zahl geändert; erst A, dann B; Ziel: P(Summe = 2) = 1/6 → Beschriftung von Würfel B neu¦Rechnung, die P = 1/6 zeigt | Summe 2 nur bei 1 + 1; P(A = 1) = 2/6, also muss P(B = 1) = 1/2 sein, d. h. drei Einsen auf B: die 2 oder eine 3 durch 1 ersetzen; Probe 2/6 · 3/6 = 6/36
