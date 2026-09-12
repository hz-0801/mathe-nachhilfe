# FHR – Typenbibliothek

Erzeugt am 2026-09-12 von `fhr-typenbibliothek.py v0.1` aus `fhr-katalog.csv` (253 Zeilen, 16 Hefte, Punktsumme 1120) und `fhr-typen.csv` (135 Typen).

**Diese Datei wird abgeleitet und nie von Hand geändert** (konzept.md § 2). Nach jeder Katalogänderung mit dem Skript neu erzeugen; Korrekturen gehören in den Katalog, nicht hierher.

Gliederung nach Leitidee, Thema und Typ wie in fhr.md § 6. Je Typ stehen die Definition aus `fhr-typen.csv`, die **Originale** (Zeilen, in denen der Typ das Feld `typ` stellt) und die **Nebenvorkommen** (Zeilen, in denen er nur in `typ_neben` steht). Für eine Heftkette zählt die erste Gruppe: Die Hauptnummer eines Hefts ist ein Typ, und nur eine Zeile, die ihn selbst verlangt, taugt als deren Decke.

Zu jeder Zeile steht `P` für die Punkte und `M` für die Merkmalszahlen Leistungen / Typen / Schritte. **Der Deckenkandidat ist eine vorläufige Rechnung, keine Regel.** blatt-konzept.md § 3 nennt als Decke das Original mit den meisten Merkmalen (bei Gleichstand Punkte, dann jüngeres Jahr); was ein Merkmal ist, ist bewusst offen (blatt-konzept.md § 7). Das Skript rechnet ersatzweise nach M, dann Punkte, dann Jahr. Zeilen mit `!` sind Aussagenlisten: Sie stehen in `gesucht` als eine Leistung, verlangen aber mehrere Begründungen, und werden von dieser Rechnung unterschätzt. Beim Bau entscheidet der Prompt, das Protokoll weist die Wahl aus.

## Überblick

| Leitidee | Thema | Typen | Originale | Typen mit nur einem Original |
|---|---|---|---|---|
| Differentialrechnung | Ableitungen bilden | 1 | 6 | 0 |
| Differentialrechnung | Nullstellen ganzrationaler Funktionen | 12 | 19 | 5 |
| Differentialrechnung | Extrem- und Sattelpunkte | 7 | 22 | 1 |
| Differentialrechnung | Monotonie und Krümmung | 6 | 3 | 0 |
| Differentialrechnung | Wendepunkte | 4 | 12 | 1 |
| Differentialrechnung | Symmetrie nachweisen | 1 | 10 | 0 |
| Differentialrechnung | Verhalten im Unendlichen | 1 | 3 | 0 |
| Differentialrechnung | Graph zeichnen und zuordnen | 11 | 25 | 5 |
| Differentialrechnung | Anstieg und Tangente | 8 | 15 | 4 |
| Differentialrechnung | Normale | 3 | 1 | 1 |
| Differentialrechnung | Schnittpunkte von Funktionsgraphen | 3 | 11 | 0 |
| Differentialrechnung | Funktionsgleichung bestimmen | 4 | 9 | 2 |
| Differentialrechnung | Extremwertaufgaben | 4 | 7 | 1 |
| Integralrechnung | Stammfunktion bilden – | 0 | 0 | 0 |
| Integralrechnung | Bestimmtes Integral berechnen – | 0 | 0 | 0 |
| Integralrechnung | Fläche zwischen Graph und x-Achse | 4 | 11 | 1 |
| Integralrechnung | Fläche zwischen zwei Graphen | 2 | 7 | 0 |
| Integralrechnung | Rotationsvolumen um die x-Achse | 1 | 4 | 0 |
| Integralrechnung | Körpervolumen aus Grundfläche und Länge | 2 | 2 | 2 |
| Stochastik | Daten darstellen und aufbereiten | 7 | 7 | 0 |
| Stochastik | Statistische Kenngrößen | 11 | 18 | 1 |
| Stochastik | Mehrstufige Zufallsexperimente | 5 | 15 | 3 |
| Stochastik | Baumdiagramm und Pfadregeln | 6 | 6 | 2 |
| Stochastik | Unabhängigkeit von Ereignissen | 2 | 5 | 0 |
| Stochastik | Erwartungswert | 2 | 2 | 0 |
| Stochastik | Kombinatorische Abzählverfahren | 7 | 15 | 4 |
| Stochastik | Laplace-Wahrscheinlichkeit | 4 | 7 | 1 |
| Grundlagen | Prozentrechnung | 4 | 1 | 1 |
| Grundlagen | Gleichungen lösen – | 1 | 0 | 0 |
| Grundlagen | Größen und Einheiten | 10 | 8 | 2 |
| Grundlagen | Terme umformen | 2 | 2 | 0 |

Themen mit „–": Sie stellen in keiner Katalogzeile das Feld `thema`, ihre Typen kommen nur innerhalb anderer Aufgaben vor. Aus ihnen lässt sich kein eigenes Heft bauen (fhr.md § 6): Stammfunktion bilden, Bestimmtes Integral berechnen, Gleichungen lösen.

Von 135 Typen stellen 86 mindestens einmal das Feld `typ`; bei 49 davon stehen mehrere Originale zur Wahl, dort ist der Deckenkandidat ausgewiesen. 37 Typen haben genau ein Original.

## Differentialrechnung

### Ableitungen bilden

*1 Typen, 6 Originale*

**Ableitung ganzrationale Funktion**  
Erste bis dritte Ableitung einer ganzrationalen Funktion mit Potenz-, Faktor- und Summenregel bilden.  
Originale: `2024-B-1d` P5 M3/3/5 ← · `2023-C-1b` P5 M2/2/5 · `2024-C-1c` P4 M2/2/4 · `2026-C-1c` P3 M1/1/3 · `2026-B-1c` P3 M1/1/3 · `2025-C-1c` P3 M1/1/3  
Deckenkandidat: `2024-B-1d` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2021-A-1a`, `2022-B-1a`, `2023-A-1b`, `2023-A-1f`, `2023-A-2e`, `2024-B-2b`  

### Nullstellen ganzrationaler Funktionen

*12 Typen, 19 Originale*

**Nullstellen über Substitution biquadratisch**  
Eine biquadratische Gleichung mit z = x^2 auf eine quadratische zurückführen, lösen und rücksubstituieren.  
Originale: `2020-C-1b` P5 M2/2/4 ← · `2026-B-1b` P6 M1/2/4 · `2021-B-1b` P6 M1/2/4 · `2022-C-1b` P5 M1/2/4 · `2019-C-1b` P4 M1/1/4  
Deckenkandidat: `2020-C-1b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2022-B-2a`, `2023-A-1f`  

**Nullstelle durch Einsetzen nachweisen**  
Eine behauptete Nullstelle durch Einsetzen in den Funktionsterm bestätigen.  
Originale: `2024-C-1b` P4 M2/2/4 ← · `2025-C-1b` P3 M2/2/3 · `2025-C-2a` P3 M1/2/3  
Deckenkandidat: `2024-C-1b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2023-C-1a`, `2025-A-1d`  

**Nullstellen aus der faktorisierten Form ablesen**  
Aus einem als Produkt von Linearfaktoren gegebenen Funktionsterm die Nullstellen ohne Rechnung ablesen.  
Originale: `2023-C-1a` P6 M3/4/4 ← · `2020-A-1b` P2 M1/2/2  
Deckenkandidat: `2023-C-1a` (vorläufig, siehe Kopf)  

**Nullstellen durch Ausklammern**  
Die Variable ausklammern und die Nullstellen über den Satz vom Nullprodukt bestimmen.  
Originale: `2026-B-2b` P5 M2/2/4 ← · `2019-A-1b` P3 M1/1/3  
Deckenkandidat: `2026-B-2b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2023-A-1b`, `2023-C-1c`, `2024-B-1c`, `2025-C-1d`  

**Nullstellen mit Polynomdivision**  
Eine gegebene oder durch Probieren gefundene Nullstelle abspalten und die restliche Gleichung niedrigeren Grades lösen.  
Originale: `2022-B-1b` P5 M2/2/4 ← · `2021-A-1b` P4 M2/2/3  
Deckenkandidat: `2022-B-1b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-C-2c`, `2022-C-2d`, `2023-C-1c`, `2024-C-1b`, `2025-A-1d`, `2026-C-1f`  

**Ganzzahlige Nullstellen durch Probieren finden**  
Bei gegebener Anzahl ganzzahliger Nullstellen diese über eine Wertetabelle oder durch systematisches Einsetzen ganzer Zahlen auffinden, ohne Polynomdivision oder Lösungsformel.  
Originale: `2022-C-2c` P5 M2/2/4  

**Nullstellen einer quadratischen Funktion mit Lösungsformel**  
Eine quadratische Funktion gleich Null setzen, die Gleichung auf die Normalform bringen und mit der Lösungsformel lösen.  
Originale: `2024-C-2e` P3 M1/1/3  
Nebenvorkommen: `2023-C-1c`, `2024-B-1c`  

**Nullstellen einer quadratischen Funktion über Wurzelziehen**  
Eine reinquadratische Funktion gleich Null setzen, das quadratische Glied isolieren und beide Nullstellen durch Wurzelziehen angeben.  
Originale: `2024-C-2a` P3 M1/1/3  
Nebenvorkommen: `2023-A-2b`  

**Nullstellen eines Produkts von Funktionen begründen**  
Über den Satz vom Nullprodukt begründen, welche Nullstellen ein als Produkt gegebener Funktionsterm besitzt, und ausschließen, dass weitere hinzukommen.  
Originale: `2023-A-2d` P2 M1/1/2  

**Schnittpunkt mit der y-Achse berechnen**  
Den Funktionswert an der Stelle null berechnen und als Achsenschnittpunkt angeben.  
Originale: `2024-B-1c` P5 M1/3/4  
Nebenvorkommen: `2020-A-1b`, `2020-C-1b`, `2021-B-1b`, `2022-B-1b`, `2022-C-1b`, `2023-C-1a`, `2026-B-1b`  

**Nullstellen und y-Achsenschnitt unterscheiden**  
Eine Aussage über die Lage von Achsenschnittpunkten prüfen, ohne zu rechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-C-1a`, `2026-C-1b`  

**Weitere Nullstellen über Symmetrie angeben**  
Aus einer bekannten Nullstelle und der Symmetrie des Graphen die übrigen Nullstellen ohne Rechnung angeben.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-C-1b`  

### Extrem- und Sattelpunkte

*7 Typen, 22 Originale*

**Extrem- und Sattelpunkte über zweite Ableitung**  
An Stellen mit f'(x) = 0 über das Vorzeichen von f'' und nötigenfalls f''' die Art des Punktes bestimmen und die Koordinaten angeben.  
Originale: `2025-C-1d` P11 M3/3/6 ← · `2026-C-1e` P8 M3/2/9 · `2020-A-1c` P11 M3/2/6 · `2023-C-1c` P9 M2/4/7 · `2021-A-1c` P8 M2/2/5 · `2024-C-1d` P7 M2/2/5 · `2022-B-1c` P7 M2/2/5 · `2026-B-2c` P5 M2/2/4 · `2019-C-1c` P7 M2/1/4 · `2019-A-1d` P5 M2/1/4 · `2023-A-1b` P8 M1/3/6 · `2024-B-2b` P8 M1/2/6 · `2020-A-2b` P7 M1/2/5 · `2019-C-2b` P6 M1/2/5 · `2022-C-1c` P8 M1/1/5 · `2025-A-1e` P7 M1/1/5 · `2026-B-1d` P3 M1/1/3  
Deckenkandidat: `2025-C-1d` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2021-B-1c`  

**Aussagen zu Stellen mit waagerechter Tangente beurteilen**  
Zu mehreren vorgelegten Aussagen über Stellen mit erster Ableitung null entscheiden, ob sie wahr oder falsch sind, und die Entscheidung begründen – allgemein über Sattelstelle, Tangentenlage und den notwendigen Wechsel zwischen Hoch- und Tiefpunkten oder rechnerisch über die Ableitungswerte an einer konkreten Stelle.  
Originale: `2020-C-1c`! P9 M2/2/5 ← · `2019-A-1c`! P7 M1/2/4  
Deckenkandidat: `2020-C-1c` (vorläufig, siehe Kopf)  

**Gegebene Stelle als Extremstelle nachweisen**  
Für eine vorgegebene Stelle oder einen vorgegebenen Punkt über notwendige und hinreichende Bedingung nachweisen, dass dort ein Extrempunkt vorliegt, ohne die Stelle selbst zu berechnen.  
Originale: `2021-B-1c` P8 M3/2/5 ← · `2021-B-2c` P8 M1/2/6  
Deckenkandidat: `2021-B-1c` (vorläufig, siehe Kopf)  

**Maximale Höhe im Sachzusammenhang berechnen**  
Die Stelle mit erster Ableitung Null berechnen und den zugehörigen Funktionswert als größten Wert im Sachzusammenhang deuten; bei einer Wurfparabel ohne Nachweis über die zweite Ableitung.  
Originale: `2023-C-2a` P3 M2/1/3  
Nebenvorkommen: `2024-C-2d`  

**Extrempunkt über notwendige Bedingung ausschließen**  
Über f'(x) ungleich null zeigen, dass ein gegebener Punkt des Graphen kein Extrempunkt sein kann.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2024-B-1d`  

**Punkte mit waagerechtem Anstieg berechnen**  
Alle Stellen mit erster Ableitung null bestimmen und mit den zugehörigen Funktionswerten als Punktkoordinaten angeben, ohne die Art der Punkte über die zweite Ableitung zu prüfen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2020-C-1c`  

**Sattelpunkt an einer Wendestelle nachweisen**  
An einer bereits bestimmten Wendestelle zusätzlich f'(x) = 0 zeigen und den Wendepunkt damit als Sattelpunkt ausweisen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-A-1c`, `2021-B-2c`, `2024-B-1e`  

### Monotonie und Krümmung

*6 Typen, 3 Originale*

**Krümmungsverhalten angeben**  
Die Intervalle der Links- und Rechtskrümmung aus den Wendestellen und dem Vorzeichen von f'' angeben.  
Originale: `2025-A-1c` P3 M2/2/3 ← · `2019-A-1e` P7 M2/1/5 · `2024-B-1f` P2 M1/1/2  
Deckenkandidat: `2025-A-1c` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2020-C-1d`, `2022-B-1d`, `2022-C-1d`, `2026-B-1e`  

**Krümmungsbereiche am Graphen markieren**  
Die links- oder rechtsgekrümmten Abschnitte eines vorgegebenen Graphen im Koordinatensystem kennzeichnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-A-1c`  

**Monotonieverhalten angeben**  
Die Intervalle monotonen Steigens und Fallens aus den Extremstellen und dem Vorzeichen von f' angeben.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2021-A-1c`, `2022-B-1c`, `2024-C-1d`, `2025-C-1d`, `2026-C-1e`  

**Vorzeichen der ersten Ableitung am Graphen beurteilen**  
Aus dem Steigen oder Fallen eines vorgegebenen Graphen an einer Stelle auf das Vorzeichen der ersten Ableitung schließen und die Antwort begründen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2024-B-1b`, `2025-A-1b`  

**Vorzeichen der zweiten Ableitung am Graphen beurteilen**  
Aus der Links- oder Rechtskrümmung eines vorgegebenen Graphen an einer Stelle auf das Vorzeichen der zweiten Ableitung schließen und die Antwort begründen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2024-B-1b`  

**Zahl der Krümmungs- und Monotoniewechsel vergleichen**  
Aus dem Verlauf oder dem Grad der Funktion die Anzahl der Monotonie- und Krümmungswechsel gegenüberstellen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2026-C-1b`  

### Wendepunkte

*4 Typen, 12 Originale*

**Wendepunkte über zweite Ableitung**  
Nullstellen von f'' bestimmen, mit f''' ungleich Null bestätigen und die Koordinaten der Wendepunkte angeben.  
Originale: `2020-C-1d` P9 M3/2/6 ← · `2024-B-1e` P7 M3/2/6 · `2026-B-1e` P6 M3/2/4 · `2022-C-1d` P7 M2/2/5 · `2021-B-1d` P7 M2/2/5 · `2022-B-1d` P5 M2/2/4 · `2024-C-1e` P3 M2/1/3 · `2026-C-1f` P7 M1/2/8 · `2023-A-2e` P6 M1/2/5 · `2019-C-1d` P5 M1/1/4 · `2021-A-1d` P3 M1/1/3  
Deckenkandidat: `2020-C-1d` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2020-A-1c`  

**Steilsten Anstieg über den Wendepunkt bestimmen**  
Erkennen, dass der Anstieg eines Graphen im Wendepunkt am größten ist, die Wendestelle bestimmen und dort den Wert der ersten Ableitung berechnen.  
Originale: `2021-B-2d` P4 M1/1/4  

**Wendepunkt über notwendige Bedingung ausschließen**  
Über f''(x) ungleich null zeigen, dass ein gegebener Punkt des Graphen kein Wendepunkt sein kann.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2023-C-1d`  

**Wendepunkte am Graphen markieren**  
Die Stellen des Krümmungswechsels in einem vorgegebenen Graphen abschätzen und die Wendepunkte dort einzeichnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2024-B-1a`  

### Symmetrie nachweisen

*1 Typen, 10 Originale*

**Symmetrie am Funktionsterm beurteilen**  
Über die Exponenten des Funktionsterms oder über f(−x) entscheiden und begründen, ob der Graph achsensymmetrisch zur y-Achse oder punktsymmetrisch zum Ursprung ist.  
Originale: `2025-C-1a` P4 M2/2/2 ← · `2022-C-1a` P4 M2/2/2 · `2026-B-1a` P3 M2/2/2 · `2024-B-2a` P3 M2/2/2 · `2023-A-1a` P3 M2/2/2 · `2021-B-1a` P3 M2/2/2 · `2020-C-1a` P3 M2/2/2 · `2019-C-1a`! P8 M1/4/4 · `2026-C-1b`! P3 M1/3/3 · `2019-A-1a` P2 M1/1/1  
Deckenkandidat: `2025-C-1a` (vorläufig, siehe Kopf)  

### Verhalten im Unendlichen

*1 Typen, 3 Originale*

**Verhalten im Unendlichen bestimmen**  
Aus Grad und Vorzeichen des Leitkoeffizienten das Verhalten von f für x gegen plus und minus unendlich angeben.  
Originale: `2022-B-1a` P5 M2/2/4 ← · `2021-A-1a` P5 M2/2/4 · `2024-C-1a` P2 M1/1/1  
Deckenkandidat: `2022-B-1a` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-C-1a`, `2020-C-1a`, `2021-B-1a`, `2022-C-1a`, `2022-C-2a`, `2023-A-1a`, `2025-C-1a`, `2026-B-1a`, `2026-C-1a`  

### Graph zeichnen und zuordnen

*11 Typen, 25 Originale*

**Graph ganzrationaler Funktion im Intervall zeichnen**  
Den Graphen über einem vorgegebenen Intervall in ein selbst angelegtes Koordinatensystem zeichnen, ohne vorgedruckte Wertetabelle.  
Originale: `2026-B-1f` P3 M1/1/2 ← · `2025-C-1e` P3 M1/1/2 · `2025-A-1g` P3 M1/1/2 · `2024-C-1f` P3 M1/1/2 · `2023-C-1e` P3 M1/1/2 · `2022-C-1f` P3 M1/1/2 · `2022-B-1e` P3 M1/1/2 · `2021-B-1e` P3 M1/1/2 · `2021-A-1f` P3 M1/1/2 · `2020-A-1e` P3 M1/1/2 · `2020-C-1e` P3 M1/1/2 · `2019-A-1f` P3 M1/1/2 · `2019-C-1e` P3 M1/1/2  
Deckenkandidat: `2026-B-1f` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2023-A-1d`  

**Wertetabelle erstellen**  
Zu vorgegebenen oder selbst gewählten x-Werten die Funktionswerte berechnen und in eine vorgedruckte oder selbst angelegte Wertetabelle eintragen.  
Originale: `2026-C-2a` P4 M2/2/10 ← · `2024-B-1g` P4 M2/2/3 · `2023-A-1d` P4 M2/2/3  
Deckenkandidat: `2026-C-2a` (vorläufig, siehe Kopf)  

**Funktionswert am Graphen ablesen**  
Zu einer gegebenen Stelle den Funktionswert aus einem vorgegebenen Graphen ablesen und angeben.  
Originale: `2025-A-1b` P2 M2/2/2 ← · `2024-B-1b` P4 M1/3/4  
Deckenkandidat: `2025-A-1b` (vorläufig, siehe Kopf)  

**Graph einer ganzrationalen Funktion zuordnen**  
Aus mehreren vorgegebenen Graphen den passenden auswählen und die Wahl über Nullstellen, Symmetrie oder Verhalten im Unendlichen begründen.  
Originale: `2026-C-1a` P3 M2/2/2 ← · `2022-C-2a` P2 M1/2/2  
Deckenkandidat: `2026-C-1a` (vorläufig, siehe Kopf)  

**Dreieck in das Koordinatensystem einzeichnen**  
Ein durch seine Eckpunkte gegebenes Dreieck in ein vorhandenes oder selbst angelegtes Koordinatensystem eintragen.  
Originale: `2023-A-1e` P5 M3/3/4  

**Grad einer Funktion am Graphen bestimmen**  
Aus der Zahl der Extrempunkte eines vorgegebenen Graphen auf den Grad der ganzrationalen Funktion schließen und die Wahl begründen.  
Originale: `2024-B-1a` P3 M2/2/2  

**Koordinatenachsen in eine Abbildung einzeichnen**  
In eine maßstäbliche Abbildung ohne Koordinatensystem die Lage von x- und y-Achse so einzeichnen, dass sie zum gegebenen Funktionsterm passt.  
Originale: `2022-B-2c` P2 M1/1/2  
Nebenvorkommen: `2024-B-2a`  

**Markante Punkte im Sachzusammenhang markieren und ablesen**  
In einer vorgegebenen Abbildung die kennzeichnenden Punkte eintragen und ihre Koordinaten aus den Sachangaben notieren.  
Originale: `2025-C-2d` P4 M2/2/4  

**Rechteck in das Koordinatensystem einzeichnen**  
Ein durch seine Eckpunkte gegebenes Rechteck in ein vorhandenes oder selbst angelegtes Koordinatensystem eintragen.  
Originale: `2020-C-2c` P4 M2/2/3  

**Graph nach Wertetabelle skizzieren**  
Den Graphen anhand einer Wertetabelle in ein selbst angelegtes Koordinatensystem eintragen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2024-B-1g`, `2026-C-2a`  

**Punkte und Parabel einzeichnen**  
Gegebene Punkte eintragen und den Verlauf einer quadratischen Funktion zwischen ihnen skizzieren.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2026-C-2d`  

### Anstieg und Tangente

*8 Typen, 15 Originale*

**Punktprobe am Graphen**  
Durch Einsetzen entscheiden, ob ein gegebener Punkt auf dem Graphen liegt.  
Originale: `2025-A-1d` P5 M3/3/5 ← · `2026-C-1d` P3 M2/2/4 · `2023-C-1d` P2 M2/2/2 · `2020-A-1d` P2 M2/2/2  
Deckenkandidat: `2025-A-1d` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-C-1a`, `2024-B-1d`  

**Tangentengleichung im Punkt**  
Aus Anstieg f'(x0) und einem Punkt des Graphen die Gleichung der Tangente bestimmen.  
Originale: `2025-C-1f` P6 M4/3/5 ← · `2024-C-1g` P7 M3/3/6 · `2019-C-1f` P3 M1/1/3  
Deckenkandidat: `2025-C-1f` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2021-B-1d`, `2022-C-1e`, `2026-C-1d`  

**Anstieg des Graphen an einer Stelle berechnen**  
Den Anstieg des Graphen an einer gegebenen Stelle als Wert der ersten Ableitung dort berechnen, ohne eine Tangentengleichung aufzustellen.  
Originale: `2023-A-1c` P4 M2/2/4 ← · `2019-A-2b` P2 M1/1/2  
Deckenkandidat: `2023-A-1c` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2020-A-1d`, `2021-A-1b`, `2022-B-1f`, `2023-C-1b`, `2024-C-1c`  

**Tangenteneigenschaft einer Geraden nachweisen**  
Für eine gegebene Gerade nachweisen, dass sie an einer Stelle Funktionswert und Anstieg mit dem Graphen teilt und damit Tangente ist.  
Originale: `2026-B-1g` P3 M2/2/3 ← · `2022-C-1e` P3 M2/2/3  
Deckenkandidat: `2026-B-1g` (vorläufig, siehe Kopf)  

**Anstieg einer Strecke aus den Endpunkten angeben**  
Den Anstieg einer geradlinigen Strecke als Quotient aus Höhenunterschied und waagerechter Entfernung angeben, ohne eine Funktionsgleichung aufzustellen.  
Originale: `2021-B-2a` P3 M2/2/3  

**Dreiecksfläche aus Achsenabschnitten einer Geraden**  
Aus Nullstelle und y-Achsenabschnitt einer Geraden die Katheten des eingeschlossenen Dreiecks bilden und dessen Flächeninhalt berechnen.  
Originale: `2026-B-1h` P3 M1/1/2  
Nebenvorkommen: `2024-C-1g`  

**Stelle zu gegebenem Anstieg berechnen**  
Die erste Ableitung gleich einem vorgegebenen Anstieg setzen, die entstehende Gleichung lösen und alle passenden Stellen angeben.  
Originale: `2019-A-1g` P3 M1/1/3  

**Tangente in das Koordinatensystem einzeichnen**  
Eine durch ihre Gleichung gegebene Tangente in ein vorhandenes Koordinatensystem eintragen.  
Originale: `2025-A-1a` P2 M2/2/2  
Nebenvorkommen: `2024-C-1g`, `2025-C-1f`, `2026-B-1g`  

### Normale

*3 Typen, 1 Originale*

**Normalengleichung im Punkt**  
Den Anstieg der Normale als negativen Kehrwert der Ableitung an der Stelle bilden und mit dem Funktionswert das absolute Glied der Geradengleichung berechnen.  
Originale: `2025-A-1h` P5 M2/2/4  
Nebenvorkommen: `2022-B-1f`, `2023-A-1c`  

**Anstieg einer senkrechten Geraden angeben**  
Zu einer Geraden mit bekanntem Anstieg den Anstieg einer dazu senkrechten Geraden als negativen Kehrwert angeben, ohne eine vollständige Geradengleichung aufzustellen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2022-C-2b`  

**Normale in das Koordinatensystem einzeichnen**  
Eine durch ihre Gleichung gegebene Normale in ein vorhandenes Koordinatensystem eintragen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-A-1h`  

### Schnittpunkte von Funktionsgraphen

*3 Typen, 11 Originale*

**Schnittpunkte zweier Funktionsgraphen berechnen**  
Zwei Funktionsterme gleichsetzen, die Gleichung lösen und die Schnittpunkte mit beiden Koordinaten angeben.  
Originale: `2023-C-2c` P6 M3/3/5 ← · `2019-C-2c` P8 M2/4/6 · `2020-A-2a` P4 M2/2/3 · `2022-B-2a` P7 M1/2/5 · `2022-C-2d` P6 M1/2/5 · `2021-A-2b` P4 M1/1/4  
Deckenkandidat: `2023-C-2c` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2025-C-1f`  

**Stelle zu gegebenem Funktionswert berechnen**  
Den Funktionsterm einem vorgegebenen Wert gleichsetzen, die Gleichung lösen und alle im Sachzusammenhang sinnvollen Lösungen angeben.  
Originale: `2021-A-1e` P4 M1/1/3 ← · `2025-A-2c` P3 M1/1/3 · `2024-C-2f` P3 M1/1/3  
Deckenkandidat: `2021-A-1e` (vorläufig, siehe Kopf)  

**Funktionswert an einer Stelle berechnen**  
Eine gegebene Stelle in den Funktionsterm einsetzen und den zugehörigen Funktionswert berechnen; Umkehrung zu Stelle zu gegebenem Funktionswert berechnen.  
Originale: `2022-B-1f` P5 M3/3/4 ← · `2019-A-2a` P2 M1/2/2  
Deckenkandidat: `2022-B-1f` (vorläufig, siehe Kopf)  

### Funktionsgleichung bestimmen

*4 Typen, 9 Originale*

**Funktionsgleichung mit Symmetriebedingung über LGS**  
Aus einer Symmetrieeigenschaft den verkürzten Ansatz aufstellen, gegebene Punkte einsetzen und das LGS lösen.  
Originale: `2021-A-2a` P7 M1/2/5 ← · `2023-A-2a` P5 M1/1/4 · `2026-B-2a` P5 M1/1/3 · `2020-C-2a` P4 M1/1/3  
Deckenkandidat: `2021-A-2a` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2025-C-2d`  

**Funktionsgleichung aus drei Punkten über LGS**  
Allgemeinen Ansatz aufstellen, gegebene Punkte einsetzen und das lineare Gleichungssystem lösen.  
Originale: `2026-C-2c` P6 M1/1/5 ← · `2023-C-2b` P7 M1/1/4 · `2019-C-2a` P6 M1/1/4  
Deckenkandidat: `2026-C-2c` (vorläufig, siehe Kopf)  

**Funktionsgleichung mit Extremalbedingung über LGS**  
Allgemeinen Ansatz aufstellen, gegebene Punkte einsetzen und die Bedingung erste Ableitung gleich Null an der Extremstelle ergänzen, dann das LGS lösen.  
Originale: `2025-A-2a` P6 M1/1/4  
Nebenvorkommen: `2021-A-2a`  

**Geradengleichung aus zwei Punkten bestimmen**  
Aus zwei gegebenen Punkten den Anstieg als Quotient der Koordinatendifferenzen und den y-Achsenabschnitt bestimmen und die Gleichung der linearen Funktion notieren.  
Originale: `2022-C-2b` P4 M2/2/3  

### Extremwertaufgaben

*4 Typen, 7 Originale*

**Maximum der Zielfunktion bestimmen**  
Die Zielfunktion ableiten, die Extremstelle berechnen und daraus den größten Wert samt den zugehörigen Größen angeben.  
Originale: `2023-A-1f` P6 M2/3/6 ← · `2025-A-2f` P4 M2/1/4 · `2020-C-2e` P5 M1/1/4  
Deckenkandidat: `2023-A-1f` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2020-A-1f`  

**Zielfunktion aus Haupt- und Nebenbedingung aufstellen**  
Hauptbedingung und Nebenbedingung notieren, die Nebenbedingung nach einer Variablen umstellen und einsetzen, um eine Zielfunktion in einer Variablen zu erhalten.  
Originale: `2020-A-1f` P8 M2/2/5 ← · `2025-A-2e` P3 M1/1/3 · `2020-C-2d` P3 M1/1/2  
Deckenkandidat: `2020-A-1f` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2023-A-1e`  

**Flächeninhalt bei gegebener Nebenbedingung berechnen**  
Aus der Nebenbedingung die fehlende Seite bestimmen und den Flächeninhalt für vorgegebene Seitenlängen berechnen.  
Originale: `2025-A-2d` P3 M2/1/4  
Nebenvorkommen: `2020-C-2c`  

**Dreiecksfläche aus Punktkoordinaten berechnen**  
Aus den Koordinaten der Eckpunkte Grundseite und Höhe eines rechtwinkligen Dreiecks bestimmen und dessen Flächeninhalt berechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2023-A-1e`  


## Integralrechnung

### Stammfunktion bilden

*0 Typen, 0 Originale  ·  kein eigenes Heft baubar*

### Bestimmtes Integral berechnen

*0 Typen, 0 Originale  ·  kein eigenes Heft baubar*

### Fläche zwischen Graph und x-Achse

*4 Typen, 11 Originale*

**Fläche zwischen Graph und x-Achse berechnen**  
Nullstellen als Grenzen nutzen, das bestimmte Integral bilden und den Betrag als Flächeninhalt angeben.  
Originale: `2026-B-2d` P5 M3/3/4 ← · `2025-C-2c` P5 M3/3/4 · `2026-C-2b` P4 M2/2/4 · `2019-A-2c` P6 M1/3/5 · `2023-A-2b` P5 M1/2/4 · `2020-A-2d` P5 M1/2/3 · `2023-C-1f` P5 M1/1/4 · `2024-C-2b` P3 M1/1/4 · `2025-A-1f` P3 M1/1/3 · `2021-A-1g` P3 M1/1/2  
Deckenkandidat: `2026-B-2d` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2021-B-1f`, `2022-C-2c`  

**Gesamtfläche aus mehreren Teilflächen berechnen**  
Bei mehreren Nullstellen die von Graph und x-Achse eingeschlossene Fläche in Teilflächen zerlegen, jede betragsmäßig berechnen und die Beträge addieren.  
Originale: `2021-B-1f` P5 M1/2/4  
Nebenvorkommen: `2019-A-2c`  

**Fläche zwischen Graph und Koordinatenachsen markieren**  
Die von einem vorgegebenen Graphen und den beiden Koordinatenachsen begrenzte Fläche im Koordinatensystem kennzeichnen, ohne sie zu berechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-A-1a`  

**Flächengleichheit mit Punktsymmetrie begründen**  
Aus der Punktsymmetrie des Graphen auf gleich große Flächen schließen, ohne beide zu berechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2026-C-2b`  

### Fläche zwischen zwei Graphen

*2 Typen, 7 Originale*

**Fläche zwischen zwei Graphen berechnen**  
Differenzfunktion bilden und über dem gegebenen Intervall integrieren.  
Originale: `2022-B-2d` P7 M3/3/6 ← · `2026-C-2d` P7 M3/3/5 · `2024-B-2d` P6 M2/4/5 · `2021-A-2d` P6 M2/3/5 · `2020-A-2c` P5 M1/2/4 · `2023-C-2d` P4 M1/2/4 · `2022-C-2e` P3 M1/1/3  
Deckenkandidat: `2022-B-2d` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-C-2c`  

**Differenzfunktion aufstellen**  
Aus zwei Funktionstermen die Differenz bilden und zusammenfassen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2023-C-2d`, `2024-B-2d`, `2026-C-2d`  

### Rotationsvolumen um die x-Achse

*1 Typen, 4 Originale*

**Rotationsvolumen um die x-Achse berechnen**  
Das Volumen eines Rotationskörpers als Produkt der Kreiszahl mit dem Integral über das Quadrat des Funktionsterms zwischen den Grenzen berechnen.  
Originale: `2019-A-2d` P5 M2/2/4 ← · `2020-C-2b` P5 M1/1/4 · `2024-C-2c` P4 M1/1/4 · `2019-A-2e` P5 M1/1/3  
Deckenkandidat: `2019-A-2d` (vorläufig, siehe Kopf)  

### Körpervolumen aus Grundfläche und Länge

*2 Typen, 2 Originale*

**Länge aus Volumen und Querschnittsfläche berechnen**  
Bei gegebenem Volumen und gegebener Querschnittsfläche die Länge eines prismatischen Körpers bestimmen.  
Originale: `2025-C-2e` P2 M1/1/1  

**Volumen aus Querschnittsfläche und Länge**  
Eine berechnete Querschnittsfläche mit einer Länge multiplizieren und das Ergebnis in eine andere Volumeneinheit umrechnen.  
Originale: `2026-C-2e` P2 M1/2/3  
Nebenvorkommen: `2021-A-2d`, `2021-B-2b`, `2025-C-2c`, `2026-B-2d`  


## Stochastik

### Daten darstellen und aufbereiten

*7 Typen, 7 Originale*

**Relative Häufigkeit berechnen**  
Absolute Häufigkeiten durch den Gesamtumfang teilen und als Dezimalzahl oder Prozentwert angeben.  
Originale: `2019-A-3b` P5 M3/4/5 ← · `2024-C-3b` P3 M3/3/5 · `2025-C-3b` P5 M2/3/4 · `2026-C-3c` P4 M2/2/4 · `2020-C-3b` P3 M2/2/3 · `2026-B-3b` P4 M2/2/2 · `2020-A-3a` P3 M2/2/2  
Deckenkandidat: `2019-A-3b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2022-C-3d`, `2025-A-3d`  

**Anzahl aus relativer Häufigkeit hochrechnen**  
Aus relativen Häufigkeiten einer Stichprobe die zu erwartenden Anzahlen für eine größere Gruppe berechnen und auf ganze Stücke aufrunden.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-A-3c`, `2024-C-3b`  

**Bedarf im ungünstigsten Fall angeben**  
Ohne Kenntnis der konkreten Verteilung die Menge angeben, die in jedem Fall ausreicht, weil jede Gruppengröße vollständig bedient werden muss.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2024-C-3b`  

**Häufigkeitsdiagramm zeichnen**  
Häufigkeiten in einem selbst gewählten Diagramm mit beschrifteten Achsen darstellen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-A-3b`, `2020-A-3a`, `2021-A-3a`, `2022-C-3d`, `2026-B-3b`, `2026-C-3c`  

**Urliste zu einer Häufigkeitsverteilung ordnen**  
Eine ungeordnete Liste von Einzelwerten auszählen und als Häufigkeitsverteilung darstellen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-C-3b`  

**Zwei Häufigkeitsverteilungen gemeinsam darstellen**  
Zwei Verteilungen mit verschiedenen Gesamtzahlen in einem Diagramm gruppiert und mit Legende darstellen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-C-3b`  

**Änderung der Häufigkeiten bei größerer Stichprobe begründen**  
Begründen, wie sich absolute und relative Häufigkeiten verhalten, wenn der Stichprobenumfang bei gleichem Verhalten der Grundgesamtheit vervielfacht wird.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2022-C-3d`  

### Statistische Kenngrößen

*11 Typen, 18 Originale*

**Mittelwert aus Häufigkeitstabelle**  
Arithmetisches Mittel aus Werten mit zugehörigen absoluten Häufigkeiten berechnen.  
Originale: `2022-C-3d` P8 M4/4/6 ← · `2025-C-3a` P5 M4/4/4 · `2021-A-3a` P6 M3/3/5 · `2020-C-3c` P6 M3/3/5 · `2026-C-3a` P4 M3/3/4 · `2024-B-3b` P5 M2/2/5 · `2023-A-3b` P4 M2/2/4  
Deckenkandidat: `2022-C-3d` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-A-3b`  

**Mittelwert aus Werteliste**  
Arithmetisches Mittel einer ungewichteten Liste von Einzelwerten als Summe durch Anzahl berechnen.  
Originale: `2025-A-3b` P3 M2/2/4 ← · `2022-B-3c` P4 M2/2/3 · `2026-B-3a` P3 M2/2/3 · `2022-C-3b` P3 M2/2/3 · `2020-C-3a` P3 M2/2/3  
Deckenkandidat: `2025-A-3b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-A-3a`, `2023-C-3a`, `2024-C-3a`  

**Median aus Werteliste**  
Den Median einer ungeordneten Werteliste durch Ordnen bestimmen und bei gerader Anzahl aus den beiden mittleren Werten mitteln.  
Originale: `2023-C-3a` P6 M4/4/6 ← · `2019-A-3a` P6 M3/4/5 · `2024-C-3a` P4 M3/3/5  
Deckenkandidat: `2023-C-3a` (vorläufig, siehe Kopf)  

**Fehlenden Wert aus vorgegebenem Mittelwert bestimmen**  
Bei bekannten Häufigkeiten und bekanntem Zielmittelwert den einen unbekannten Einzelwert über eine Gleichung bestimmen; Umkehrung der Mittelwertberechnung.  
Originale: `2021-A-3b` P2 M1/1/2 ← · `2020-C-3e` P2 M1/1/2  
Deckenkandidat: `2021-A-3b` (vorläufig, siehe Kopf)  

**Medianklasse aus klassierter Häufigkeitstabelle bestimmen**  
Über die kumulierten Häufigkeiten die Klasse angeben, in der der Median klassierter Daten liegt, und die Wahl mit der Position des Medians begründen.  
Originale: `2024-B-3a` P2 M1/1/3  
Nebenvorkommen: `2019-A-3b`, `2020-C-3b`  

**Median aus Häufigkeitstabelle**  
Den Median aus der geordneten Liste aller Einzelwerte einer Häufigkeitstabelle bestimmen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-C-3a`, `2026-C-3a`  

**Median und Mittelwert bei Ausreißern vergleichen**  
Die Abweichung zwischen Median und arithmetischem Mittel auf einzelne Ausreißer zurückführen und begründen, welche Kenngröße die Daten besser beschreibt.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-A-3a`  

**Modalwert aus Häufigkeitstabelle**  
Den häufigsten Wert einer Häufigkeitstabelle ablesen und angeben.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-C-3a`  

**Standardabweichung aus Häufigkeitstabelle**  
Standardabweichung aus den mit den Häufigkeiten gewichteten quadratischen Abweichungen vom Mittelwert berechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2020-C-3c`, `2021-A-3a`, `2023-A-3b`, `2024-B-3b`, `2025-C-3a`, `2026-C-3a`  

**Standardabweichung aus Werteliste**  
Standardabweichung einer ungewichteten Werteliste über die mittlere quadratische Abweichung vom Mittelwert berechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-A-3a`, `2020-C-3a`, `2022-B-3c`, `2022-C-3b`, `2023-C-3a`, `2024-C-3a`, `2025-A-3b`, `2026-B-3a`  

**Streuung zweier Verteilungen vergleichen**  
Aus zwei Standardabweichungen bei gleichem Mittelwert auf die unterschiedlich breite Streuung der Daten schließen und den Unterschied im Sachzusammenhang deuten.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2020-C-3c`  

### Mehrstufige Zufallsexperimente

*5 Typen, 15 Originale*

**Baumdiagramm mehrstufig ohne Zurücklegen darstellen**  
Ein Ziehen ohne Zurücklegen über zwei oder mehr Stufen mit allen Pfaden und den von Stufe zu Stufe sinkenden Nennern zeichnen.  
Originale: `2025-A-3c` P8 M4/4/5 ← · `2021-A-3d` P8 M4/4/5 · `2023-A-3d` P7 M3/3/5 · `2019-C-3e` P7 M3/3/5 · `2024-C-3d` P6 M3/3/5 · `2025-C-3c` P7 M3/3/4 · `2023-C-3c` P7 M3/3/4 · `2020-A-3c` P7 M2/4/5 · `2020-C-3d` P6 M2/3/4 · `2022-C-3c` P5 M2/2/4  
Deckenkandidat: `2025-A-3c` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2024-B-3d`  

**Wahrscheinlichkeit über mehrere Pfade summieren**  
Ein Ereignis, das mehrere Pfade des Baumdiagramms umfasst, über die Summe aller zugehörigen Pfadwahrscheinlichkeiten berechnen und dabei die Zahl der Reihenfolgen beachten.  
Originale: `2024-C-3c` P7 M3/4/6 ← · `2022-B-3f` P2 M1/1/2  
Deckenkandidat: `2024-C-3c` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-A-3c`, `2019-C-3e`, `2020-A-3c`, `2020-C-3d`, `2021-A-3d`, `2022-B-3e`, `2022-C-3c`, `2023-A-3d`, `2023-C-3c`, `2024-C-3d`  

**Baumdiagramm mehrstufig mit Zurücklegen darstellen**  
Ein Zufallsexperiment mit drei oder mehr Stufen, bei dem sich die Wahrscheinlichkeiten von Stufe zu Stufe nicht ändern, mit allen Ästen und Wahrscheinlichkeiten zeichnen.  
Originale: `2021-B-3d` P6 M4/3/5  

**Pfadregel mehrstufig mit Zurücklegen anwenden**  
Die Wahrscheinlichkeit mehrerer gleichartiger unabhängiger Versuche als Potenz der Einzelwahrscheinlichkeit berechnen.  
Originale: `2025-A-3e` P2 M1/1/1  
Nebenvorkommen: `2019-C-3c`, `2021-B-3d`, `2024-C-3c`  

**Pfadregel mehrstufig ohne Zurücklegen anwenden**  
Bei einem Versuch mit zwei oder mehr Stufen ohne Zurücklegen die Wahrscheinlichkeit eines Pfades als Produkt der Ästewahrscheinlichkeiten berechnen, deren Nenner von Stufe zu Stufe kleiner werden.  
Originale: `2021-A-3e` P2 M1/1/2  
Nebenvorkommen: `2020-A-3c`, `2020-C-3d`, `2021-A-3d`, `2023-A-3d`, `2023-C-3c`, `2024-B-3d`, `2024-C-3d`, `2025-A-3c`, `2025-C-3c`  

### Baumdiagramm und Pfadregeln

*6 Typen, 6 Originale*

**Baumdiagramm zweistufig darstellen**  
Ein zweistufiges Zufallsexperiment mit allen Ästen und Wahrscheinlichkeiten zeichnen.  
Originale: `2026-B-3c` P9 M4/3/5 ← · `2019-A-3c` P6 M3/4/4 · `2026-C-3d` P6 M3/3/5 · `2022-B-3d` P5 M3/3/4  
Deckenkandidat: `2026-B-3c` (vorläufig, siehe Kopf)  

**Gegenereignis nutzen**  
Eine Wahrscheinlichkeit als 1 minus der Wahrscheinlichkeit des Gegenereignisses berechnen.  
Originale: `2024-B-3d` P6 M2/3/4  
Nebenvorkommen: `2019-C-3c`, `2020-A-3c`, `2021-A-3d`, `2021-B-3d`, `2024-C-3c`, `2025-A-3c`, `2025-C-3c`, `2026-B-3c`, `2026-C-3d`  

**Wahrscheinlichkeitsverteilung aufstellen**  
Zu einem mehrstufigen Versuch alle möglichen Werte der Zufallsgröße bilden, gleiche Werte durch Addition ihrer Pfadwahrscheinlichkeiten zusammenfassen und die Verteilung als Tabelle angeben.  
Originale: `2022-B-3e` P3 M2/2/4  

**Gegenereignis in Worten formulieren**  
Zu einem in Worten gegebenen Ereignis das Gegenereignis sprachlich richtig beschreiben.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2022-B-3b`, `2024-C-3c`, `2025-A-3c`  

**Pfadregel zweistufig anwenden**  
Die Wahrscheinlichkeit eines Ergebnisses als Produkt entlang eines Pfades berechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-A-3c`, `2022-B-3d`, `2026-B-3c`, `2026-C-3d`  

**Vertauschung der Reihenfolge bei unabhängigen Stufen begründen**  
Begründen, dass die Wahrscheinlichkeit eines Pfades sich nicht ändert, wenn die Reihenfolge voneinander unabhängiger Stufen vertauscht wird, weil nur die Faktoren die Plätze tauschen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2022-B-3d`  

### Unabhängigkeit von Ereignissen

*2 Typen, 5 Originale*

**Vierfeldertafel vervollständigen**  
Fehlende Felder und Randsummen einer Vierfeldertafel aus gegebenen Anzahlen ergänzen.  
Originale: `2026-C-3e` P4 M2/2/5 ← · `2024-B-3e` P5 M2/2/4 · `2023-A-3a` P2 M1/1/3  
Deckenkandidat: `2026-C-3e` (vorläufig, siehe Kopf)  

**Stochastische Unabhängigkeit prüfen**  
Prüfen, ob das Produkt der Einzelwahrscheinlichkeiten gleich der Wahrscheinlichkeit des Schnittereignisses ist.  
Originale: `2025-A-3d` P5 M1/2/4 ← · `2023-A-3e` P3 M1/1/4  
Deckenkandidat: `2025-A-3d` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2024-B-3e`, `2026-C-3e`  

### Erwartungswert

*2 Typen, 2 Originale*

**Erwartungswert berechnen**  
Die Werte einer Zufallsgröße mit ihren Wahrscheinlichkeiten gewichten und aufsummieren, um den auf Dauer zu erwartenden Durchschnittswert zu erhalten.  
Originale: `2021-B-3e` P4 M2/2/4 ← · `2019-C-3d` P3 M2/2/3  
Deckenkandidat: `2021-B-3e` (vorläufig, siehe Kopf)  

**Überschuss aus Einsatz und durchschnittlicher Auszahlung berechnen**  
Aus dem Einsatz je Spiel, der durchschnittlichen Auszahlung und der Zahl der Spiele den zu erwartenden Überschuss des Anbieters bestimmen oder umgekehrt aus einem Zielüberschuss den nötigen Mindesteinsatz.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-C-3d`, `2019-C-3e`  

### Kombinatorische Abzählverfahren

*7 Typen, 15 Originale*

**Kombination ohne Wiederholung berechnen**  
Die Zahl der Auswahlen von k aus n ohne Beachtung der Reihenfolge über den Binomialkoeffizienten bestimmen.  
Originale: `2022-C-3a` P4 M2/2/2 ← · `2025-C-3d` P3 M2/2/2 · `2023-C-3d` P3 M2/2/2 · `2019-A-3d` P3 M2/2/2 · `2020-A-3d` P3 M1/1/3 · `2025-A-3a` P2 M1/1/1 · `2024-B-3c` P2 M1/1/1 · `2023-A-3c` P2 M1/1/1 · `2021-A-3c` P2 M1/1/1  
Deckenkandidat: `2022-C-3a` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2021-B-3a`  

**Permutation ohne Wiederholung berechnen**  
Die Zahl der Anordnungen unterscheidbarer Elemente als Fakultät ihrer Anzahl bestimmen.  
Originale: `2020-A-3e` P6 M1/3/3 ← · `2023-A-3f` P2 M1/1/2  
Deckenkandidat: `2020-A-3e` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-A-3d`, `2021-B-3a`, `2022-C-3a`, `2023-C-3d`, `2025-C-3d`  

**Anzahl über das Zählprinzip berechnen**  
Die Zahl der Möglichkeiten einer mehrteiligen Zusammenstellung als Produkt der Wahlmöglichkeiten je Teil berechnen.  
Originale: `2021-B-3a` P5 M3/3/3  
Nebenvorkommen: `2020-A-3e`  

**Fehlende Anzahl aus der Gesamtzahl der Möglichkeiten bestimmen**  
Aus der bekannten Gesamtzahl der Möglichkeiten und den bekannten Faktoren die fehlende Anzahl durch Division bestimmen; Umkehrung des Zählprinzips.  
Originale: `2021-B-3b` P2 M1/1/1  

**Kombination mit Wiederholung berechnen**  
Die Zahl der Auswahlen ohne Beachtung der Reihenfolge und mit Wiederholung über den Binomialkoeffizienten von n + k − 1 über k bestimmen.  
Originale: `2026-B-3d` P2 M1/1/1  

**Permutation mit Wiederholung berechnen**  
Die Zahl der Anordnungen mehrerer gleichartiger Gruppen als Fakultät der Gesamtzahl geteilt durch das Produkt der Gruppenfakultäten bestimmen.  
Originale: `2026-B-3e` P2 M1/1/1  

**Variation ohne Wiederholung berechnen**  
Die Zahl der geordneten Auswahlen von k aus n unterscheidbaren Elementen ohne Wiederholung als Fakultät von n geteilt durch die Fakultät von n minus k bestimmen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2020-A-3e`  

### Laplace-Wahrscheinlichkeit

*4 Typen, 7 Originale*

**Ergebnismenge eines Zufallsexperiments angeben**  
Alle möglichen Ergebnisse eines einstufigen Zufallsexperiments als Menge notieren.  
Originale: `2023-C-3b` P4 M3/3/4 ← · `2022-B-3a` P3 M2/2/2 · `2021-B-3c` P3 M2/2/2  
Deckenkandidat: `2023-C-3b` (vorläufig, siehe Kopf)  

**Laplace-Wahrscheinlichkeit berechnen**  
Die Wahrscheinlichkeit eines Ereignisses im ein- oder mehrstufigen Laplace-Versuch als Anteil der günstigen an allen gleich wahrscheinlichen Ergebnissen berechnen.  
Originale: `2022-B-3b` P3 M3/2/3 ← · `2019-C-3c` P3 M1/3/3 · `2019-C-3b` P4 M1/1/4  
Deckenkandidat: `2022-B-3b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2023-C-3b`  

**Laplace-Bedingung begründen**  
Anhand der Versuchsbedingungen begründen, dass alle Ergebnisse gleich wahrscheinlich sind und damit ein Laplace-Experiment vorliegt.  
Originale: `2019-C-3a` P3 M2/2/2  
Nebenvorkommen: `2021-B-3c`, `2022-B-3a`, `2023-C-3b`  

**Beispiele für Laplace-Experimente nennen**  
Eigene Zufallsversuche mit lauter gleich wahrscheinlichen Ergebnissen angeben, etwa Münzwurf oder Lottoziehung.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-C-3a`  


## Grundlagen

### Prozentrechnung

*4 Typen, 1 Originale*

**Grundwert aus Prozentwert berechnen**  
Aus einem verminderten oder vermehrten Wert und dem Prozentsatz den Grundwert bestimmen.  
Originale: `2026-C-3b` P2 M2/2/4  

**Differenzbetrag aus Stückzahlen berechnen**  
Preisdifferenzen mit Stückzahlen multiplizieren und zu einem Gesamtbetrag summieren.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2026-C-3b`  

**Prozentsatz aus Anteil berechnen**  
Aus Prozentwert und Grundwert den Prozentsatz als Quotienten bestimmen und in Prozent angeben.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2020-A-2d`, `2022-B-2b`  

**Prozentualen Mehrpreis berechnen**  
Zwei Preise ins Verhältnis setzen, den Prozentsatz bezogen auf den günstigeren als Grundwert bestimmen und die Differenz zu 100 Prozent als Mehrpreis angeben.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2023-C-3a`  

### Gleichungen lösen

*1 Typen, 0 Originale  ·  kein eigenes Heft baubar*

**Gleichung vierten Grades über Substitution lösen**  
Eine Gleichung der Form f(x) = c auf Normalform bringen, mit z = x^2 substituieren, lösen und rücksubstituieren.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2025-C-2b`  

### Größen und Einheiten

*10 Typen, 8 Originale*

**Funktionswert im Sachzusammenhang deuten**  
Eine Stelle aus dem Sachzusammenhang bestimmen, den Funktionswert berechnen und als Länge oder Höhe in der Wirklichkeit deuten.  
Originale: `2025-C-2b` P6 M2/2/5 ← · `2024-C-2d` P4 M2/2/3 · `2025-A-2b` P1 M1/1/1  
Deckenkandidat: `2025-C-2b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2025-C-2a`  

**Streckenlänge im Koordinatensystem in Meter umrechnen**  
Eine in Längeneinheiten gemessene Strecke über den angegebenen Maßstab in eine wirkliche Länge umrechnen.  
Originale: `2022-B-2b` P4 M3/2/4 ← · `2024-B-2c` P3 M3/1/3 · `2021-A-2c` P3 M2/1/3  
Deckenkandidat: `2022-B-2b` (vorläufig, siehe Kopf)  
Nebenvorkommen: `2019-A-2a`, `2019-C-2b`, `2020-A-2a`, `2020-A-2b`, `2026-B-2b`, `2026-B-2c`  

**Flächeninhalt einer zusammengesetzten Figur berechnen**  
Eine aus Rechtecken und Dreiecken zusammengesetzte Figur zerlegen, die Teilflächen einzeln berechnen und addieren.  
Originale: `2021-B-2b` P3 M2/2/3  

**Gesamteinnahme aus Stückzahlen und Einzelpreisen berechnen**  
Aus einer Häufigkeitstabelle und den zugehörigen Einzelpreisen die Gesamteinnahme als Summe der Produkte aus Stückzahl und Preis berechnen.  
Originale: `2020-A-3b` P2 M1/1/3  

**Flächeninhalt im Koordinatensystem in Quadratmeter umrechnen**  
Eine Maßzahl in Flächeneinheiten mit dem quadrierten Maßstab in einen wirklichen Flächeninhalt umrechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-A-2c`, `2019-C-2c`, `2020-A-2c`, `2021-A-2d`, `2022-B-2d`, `2024-B-2d`, `2026-B-2d`  

**Masse aus Volumen und Dichte**  
Aus Volumen und Masse je Volumeneinheit die Gesamtmasse berechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2019-A-2d`, `2025-C-2c`, `2026-C-2e`  

**Mindestmaße eines umschließenden Rechtecks bestimmen**  
Aus berechneten Punkten die Breite und Höhe des kleinsten Rechtecks angeben, das eine Fläche im Sachzusammenhang vollständig aufnimmt.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2023-C-2c`  

**Preis aus Fläche und Quadratmeterpreis berechnen**  
Einen Flächeninhalt in Quadratmetern mit dem Preis je Quadratmeter multiplizieren.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2022-B-2d`, `2023-C-2c`  

**Streckenlänge über den Satz des Pythagoras berechnen**  
Die Länge einer schrägen Strecke aus waagerechtem und senkrechtem Abstand ihrer Endpunkte mit dem Satz des Pythagoras berechnen.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2021-B-2a`  

**Stückzahl aus Gesamtmenge und Verbrauch je Stück berechnen**  
Eine verfügbare Gesamtmenge durch den Verbrauch je Stück teilen und auf die ganze Stückzahl abrunden.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2021-B-3e`, `2024-B-2d`  

### Terme umformen

*2 Typen, 2 Originale*

**Produkt zweier Funktionsterme ausmultiplizieren**  
Zwei gegebene Funktionsterme multiplizieren, ordnen und zusammenfassen, um eine vorgegebene Darstellung nachzuweisen.  
Originale: `2023-A-2c` P2 M1/1/2 ← · `2020-A-1a` P2 M1/1/2  
Deckenkandidat: `2023-A-2c` (vorläufig, siehe Kopf)  

**Ungleichheit zweier Funktionsterme nachweisen**  
Zeigen, dass zwei Funktionsterme nicht dieselbe Funktion beschreiben, etwa durch eine Punktprobe an einer Stelle mit verschiedenen Funktionswerten.  
Originale: keine – kommt nur als Nebentyp vor  
Nebenvorkommen: `2023-C-1a`  


