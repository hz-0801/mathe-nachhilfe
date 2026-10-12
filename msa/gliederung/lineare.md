# Gliederung Lineare (P10)

Prüfung: msa
Kapitel: lineare
Gebiet: Funktionen
Name: Lineare
Folge: 4
Bank: lineare-funktionen | quadratische-funktionen | quadratische-gleichungen
Katalog: katalog/lineare-funktionen.md | katalog/quadratische-funktionen.md | katalog/quadratische-gleichungen.md
Anzeigenamen: Lineare Funktionen = Lineare Funktionen
Kennung: Lineare Funktionen = TAL

Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,
didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die
Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py
und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026; Stufen wie im Buch und nach dem Gesuchten
12.10.2026 (TAL2).

## Stufen

Ein Blatt „Lineare Funktionen“ (TAL), Stufen wie im Buch und nach dem Gesuchten (pruefung.md § 5,
Lehrer 12.10.): Gerade zeichnen · Gleichung ablesen oder aus Punkten aufstellen · Nullstelle ·
Punktprobe · Gleichung aus Text; „Schnittpunkt zweier Geraden“ ist Buchstufe ohne Original
(msa/buchstufen-p10.csv, nur Handreichung). Eine Teilaufgabe steht bei dem, was sie zuletzt sucht
(wie Quadratische 12.10.): 2022-OS-K3a (zeichnen, dann Nullstelle) bei Nullstelle, 2025-OS-K5a
(zeichnen, dann Gleichung) bei Gleichung aus Punkten. Die drei Buchstufen des Sachzusammenhangs (Gleichung
aus Text, Wert berechnen, Angebote vergleichen) sind eine Stufe: erster Schritt jedes Originals ist,
Anfangswert und Änderung aus dem Text zu holen (Schülerfrage). Einstieg Geraden = Erkennen (Lehrer
12.10.): vier Funktionen, die linearen ankreuzen, an einer m und n benennen; danach 2025-OS-B1f (Graphen).

### Gerade zeichnen
- **Anzeigename:** Gerade zeichnen
- **Schülerfrage:** Welche Funktionen sind linear? Kreuze an. Wähl eine lineare aus und gib ihr m und n an: $m = \underline{\hspace{10mm}}$, $n = \underline{\hspace{10mm}}$.
- **Schülerfrage-Fälle:** $f(x) = 3 - 2x$ → ja | $f(x) = x^2 + 1$ → nein | $f(x) = 0{,}5x$ → ja | $f(x) = \frac{4}{x}$ → nein
- **Schülerfrage-Form:** kreuz:linear
- **Schülerfrage-Weg:** linear sind a) und c): a) m = −2, n = 3 (die Zahl vor x ist m, auch hinten); c) m = 0,5, n = 0; x² und 4 : x geben keine Gerade
- **Kern:** ja – Graph erkennen, y-Achsenabschnitt einzeichnen, Gerade aus der Gleichung zeichnen, Eigenschaften prüfen (Basisteil 2016, 2024, 2025; Niveau I–II); Bank-Kette Graph zeichnen mit Grundfall
- **Originale:** 2025-OS-B1f 2024-OS-B1i 2024-OS-K3a 2026-FOR-K5a 2023-OS-K4a 2016-OS-B1c 2021-OS-K2a 2021-OS-K2b
- **Bank:** lineare-funktionen-e2-k4-s5(i) lineare-funktionen-e2-k4-s6(i) lineare-funktionen-e2-k4-s7(i) lineare-funktionen-e2-k4-s8(i) lineare-funktionen-e2-k6-s1(i) lineare-funktionen-e2-k7-s2(i) lineare-funktionen-e4-k4-s2(i) lineare-funktionen-e3-k2-s7[2023-OS-K4a,2021-OS-K2b]
- **Zuschnitt:** Lineare Funktionen

### Gleichung ablesen oder aus Punkten aufstellen
- **Anzeigename:** Gleichung ablesen oder aus Punkten aufstellen
- **Frage:** Die Steigung aus zwei Punkten: Wo steht die Formel? Formelsammlung, Seite ___
- **Kern:** ja – m und n am Graphen ablesen, Gleichung zuordnen, Gerade durch zwei Punkte und ihre Gleichung (2015–2025, Niveau I–II); Bank-Ketten Ablesen und Gleichung bestimmen mit Grundfall
- **Originale:** 2025-OS-K5a 2019-OS-K2b 2019-OS-K2c 2017-OS-K5a 2015-OS-K4d
- **Bank:** lineare-funktionen-e2-k5-s1(i) lineare-funktionen-e2-k5-s2(i) lineare-funktionen-e2-k5-s3(i) lineare-funktionen-e2-k5-s4(i) lineare-funktionen-e2-k5-s5(i) lineare-funktionen-e2-k5-s6(i) lineare-funktionen-e4-k2-s1(i) lineare-funktionen-e4-k1-s3(i) lineare-funktionen-e4-k1-s4(i) lineare-funktionen-e4-k1-s5(i) lineare-funktionen-e4-k1-s6[v1,v2,v5,v6](i) lineare-funktionen-e4-k1-s6[v3,v4] lineare-funktionen-e4-k4-s4
- **Zuschnitt:** Lineare Funktionen

### Nullstelle
- **Anzeigename:** Nullstelle
- **Kern:** nein – 2 echte (2019 ablesen, 2022 nach dem Zeichnen angeben), Niveau I; Bank Funktionswert null
- **Originale:** 2022-OS-K3a 2019-OS-K2a
- **Bank:** lineare-funktionen-e3-k2-s6(i) lineare-funktionen-e3-k5-s4(i)
- **Zuschnitt:** Lineare Funktionen

### Punktprobe
- **Anzeigename:** Punktprobe
- **Kern:** ja – einsetzen und vergleichen, an Gerade, Parabel oder Gleichung (2017, 2023–2026; Befund Funktionen 10.10., Lehrer 10.10.: Einsetzen ist ein Handgriff); Bank-Kette Funktionswert mit Grundfall. 2025-OS-B1h (Lösung einer Gleichung durch Einsetzen prüfen) ist derselbe Handgriff und steht als Basisaufgabe am Platz der Stufe (pruefung.md § 5 „Basis am Platz ihrer Stufe“)
- **Originale:** 2023-OS-B1i 2026-FOR-K5b 2024-OS-K3c 2017-OS-K5b 2025-OS-B1h
- **Bank:** lineare-funktionen-e3-k2-s5(i) lineare-funktionen-e3-k2-s7[2023-OS-B1i,2026-FOR-K5b,2017-OS-K5b,2019-OS-K2a,2021-OS-K6d,2022-OS-K3a] quadratische-funktionen-e1-k1-s4 quadratische-funktionen-e3-k1-s2 quadratische-funktionen-e4-k1-s14 quadratische-gleichungen-e1-k2-s12(i) quadratische-gleichungen-e2-k1-s5(i) quadratische-gleichungen-e3-k3-s13(i) quadratische-gleichungen-e2-k1-s12[2025-OS-B1h]
- **Zuschnitt:** Lineare Funktionen

### Gleichung aus Text
- **Anzeigename:** Gleichung aus Text
- **Schülerfrage:** Anfangswert oder Änderung je Schritt? Schreib zu jeder Zahl, was sie in der Gleichung y = m · x + n ist (m oder n). Rechne nicht.
- **Schülerfrage-Fälle:** Handytarif: 8 € im Monat und 0,09 € je Minute = 8 ist n, 0,09 ist m | Kerze: 25 cm hoch, brennt je Stunde 2 cm ab = 25 ist n, −2 ist m
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** n steht am Anfang (x = 0), m ist das, was je Monat, Minute oder Stunde dazukommt oder weggeht
- **Kern:** ja – Wert berechnen, Gleichung aufstellen und deuten, rückwärts rechnen, Graph zum Tarif zuordnen, Angebote vergleichen (2016, 2021, 2022, 2023; Niveau I–II); Bank-Kette Anwendung mit Grundfall
- **Originale:** 2022-OS-K6a 2022-OS-K6b 2023-OS-K3a 2023-OS-K3b 2021-OS-K6a 2021-OS-K6c 2021-OS-K6d 2021-OS-K7a 2016-OS-K6a 2016-OS-K6b 2016-OS-K6c
- **Bank:** lineare-funktionen-e5-k1-s3 lineare-funktionen-e5-k4-s4 lineare-funktionen-e5-k1-s1 lineare-funktionen-e5-k1-s2 lineare-funktionen-e5-k3-s1 lineare-funktionen-e5-k4-s1 lineare-funktionen-e1-k1-s8 lineare-funktionen-e5-k2-s1 lineare-funktionen-e5-k1-s4 lineare-funktionen-e5-k4-s2 lineare-funktionen-e5-k1-s5[2022-OS-K6a,2021-OS-K6a,2022-OS-K6b,2016-OS-K6c,2021-OS-K7a,2023-OS-K3a,2016-OS-K6a,2023-OS-K3b,2016-OS-K6b]
- **Verwechselbar:** wachstum:Tabelle ergänzen | wachstum:Faktor bestimmen, Gleichung aufstellen
- **Zuschnitt:** Lineare Funktionen

## Plätze der Originale

Jede Teilaufgabe 2014–2026 (OS, EBR, FOR, GYM) mit ihrem Hauptplatz (Stufe, deren Handgriff die
ganze Teilaufgabe ist), „ganz auch“ (die ganze Aufgabe ist dieser Handgriff, obwohl anders
etikettiert) und Zwischenschritt; Stufen anderer Kapitel mit „kapitel:“. Erzeugt daraus:
msa/handgriffe-p10.csv (werkzeuge/gliederung-sichten.py).

| id | Hauptplatz | Ganz auch | Zwischenschritt | Begründung |
|---|---|---|---|---|
| 2014-GYM-K2a | Gerade zeichnen |  |  | Hauptplatz nach typ „Eigenschaften eines Graphen beurteilen“ (bis 12.10.: zeichnen und Aussagen prüfen) |
| 2015-GYM-K3a | Gleichung aus Text |  |  | Hauptplatz nach typ „Graph zu Tarif zuordnen“. Angebote für 350 km vergleichen (bis 12.10.: Graph zum Tarif zuordnen) |
| 2015-OS-K4a |  |  | Nullstelle | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2015-OS-K4d | Gleichung ablesen oder aus Punkten aufstellen |  |  | Hauptplatz nach typ „Geradengleichung aus zwei Punkten“ (bis 12.10.: durch zwei Punkte, Gleichung ablesen) |
| 2016-GYM-B1c | Gerade zeichnen |  |  | GYM-Zwilling von 2016-OS-B1c (bis 12.10.: erkennen und ablesen) |
| 2016-GYM-K2c |  |  | Gerade zeichnen | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2016-OS-B1c | Gerade zeichnen |  |  | Hauptplatz nach typ „Graph nach Eigenschaft auswählen“ (bis 12.10.: erkennen und ablesen) |
| 2016-OS-K6a | Gleichung aus Text |  |  | Hauptplatz nach typ „Graph zu Tarif zuordnen“ (bis 12.10.: Graph zum Tarif zuordnen) |
| 2016-OS-K6b | Gleichung aus Text |  |  | Hauptplatz nach typ „Tarife vergleichen“ (bis 12.10.: Tarife vergleichen) |
| 2016-OS-K6c | Gleichung aus Text |  |  | Hauptplatz nach typ „Lineare Funktion aus Sachverhalt aufstellen“ (bis 12.10.: Gleichung aufstellen und rückwärts rechnen) |
| 2017-GYM-K5b | Gleichung aus Text |  | prozent:Erhöhung und Veränderung in Prozent | Hauptplatz nach typ „Tarife vergleichen“. Nettopreis um 19 % erhöht (bis 12.10.: Tarife vergleichen) |
| 2017-OS-K5a | Gleichung ablesen oder aus Punkten aufstellen |  |  | Hauptplatz nach typ „Gerade durch zwei Punkte zeichnen“ (bis 12.10.: durch zwei Punkte, Gleichung ablesen) |
| 2017-OS-K5b | Punktprobe |  |  | Hauptplatz nach typ „Funktionswert berechnen“ (bis 12.10.: rechnerisch an Gerade und Parabel) |
| 2018-GYM-K2d |  |  | Gerade zeichnen; dreiecke:Winkel berechnen | Hauptplatz außerhalb der P10-Stufen. Neigungswinkel über tan |
| 2019-OS-K2a | Nullstelle |  |  | Hauptplatz nach typ „Nullstelle am Graphen ablesen“ (bis 12.10.: erkennen und ablesen) |
| 2019-OS-K2b | Gleichung ablesen oder aus Punkten aufstellen |  |  | Hauptplatz nach typ „Graph nach Eigenschaft auswählen“ (bis 12.10.: erkennen und ablesen) |
| 2019-OS-K2c | Gleichung ablesen oder aus Punkten aufstellen |  |  | Hauptplatz nach typ „Geradengleichung zu Graph zuordnen“ (bis 12.10.: erkennen und ablesen) |
| 2020-GYM-K3c |  |  | Nullstelle | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2021-GYM-K3c | Gleichung ablesen oder aus Punkten aufstellen |  | flaechen:Fläche gesucht | Hauptplatz nach typ „Geradengleichung aus zwei Punkten“. Trapezfläche unter der Geraden (bis 12.10.: durch zwei Punkte, Gleichung ablesen) |
| 2021-OS-K2a | Gerade zeichnen |  |  | Hauptplatz nach typ „Gerade aus Gleichung zeichnen“ (bis 12.10.: aus Gleichung zeichnen) |
| 2021-OS-K2b | Gerade zeichnen |  | Punktprobe | Hauptplatz nach typ „Eigenschaften eines Graphen beurteilen“. Zwischenschritt aus typ_neben (bis 12.10.: zeichnen und Aussagen prüfen) |
| 2021-OS-K6a | Gleichung aus Text |  |  | Hauptplatz nach typ „Endwert linearer Veränderung berechnen“ (bis 12.10.: Endwert berechnen) |
| 2021-OS-K6c | Gleichung aus Text |  |  | Hauptplatz nach typ „Gleichung im Sachzusammenhang deuten“ (bis 12.10.: Gleichung aufstellen und rückwärts rechnen) |
| 2021-OS-K6d | Gleichung aus Text |  |  | Hauptplatz nach typ „Nullstelle lineare Funktion berechnen“ (bis 12.10.: Gleichung aufstellen und rückwärts rechnen) |
| 2021-OS-K7a | Gleichung aus Text |  |  | Hauptplatz nach typ „Gleichung zu Tarif zuordnen“ (bis 12.10.: Gleichung aufstellen und rückwärts rechnen) |
| 2022-OS-K3a | Nullstelle |  | Gerade zeichnen | Hauptplatz nach typ „Gerade aus Gleichung zeichnen“. Zwischenschritt aus typ_neben (bis 12.10.: aus Gleichung zeichnen) |
| 2022-OS-K6a | Gleichung aus Text |  |  | Hauptplatz nach typ „Endwert linearer Veränderung berechnen“ (bis 12.10.: Endwert berechnen) |
| 2022-OS-K6b | Gleichung aus Text |  |  | Hauptplatz nach typ „Lineare Funktion aus Sachverhalt aufstellen“ (bis 12.10.: Gleichung aufstellen und rückwärts rechnen) |
| 2023-GYM-B1a | Nullstelle |  |  | Hauptplatz nach typ „Nullstelle lineare Funktion berechnen“ (bis 12.10.: Gleichung aufstellen und rückwärts rechnen) |
| 2023-OS-B1i | Punktprobe |  |  | Hauptplatz nach Zuordnung. Punktprobe ist der ganze Handgriff, L5 nur die Ankreuzform (bis 12.10.: ankreuzen) |
| 2023-OS-K3a | Gleichung aus Text |  |  | Hauptplatz nach typ „Graph zu Tarif zuordnen“ (bis 12.10.: Graph zum Tarif zuordnen) |
| 2023-OS-K3b | Gleichung aus Text |  |  | Hauptplatz nach typ „Tarife vergleichen“. Zwischenschritt aus typ_neben (bis 12.10.: Tarife vergleichen) |
| 2023-OS-K4a | Gerade zeichnen |  |  | Hauptplatz nach Zuordnung. Zwischenschritt aus typ_neben (bis 12.10.: zeichnen und Aussagen prüfen) |
| 2024-GYM-B1b |  |  | Gleichung ablesen oder aus Punkten aufstellen | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2024-OS-B1i | Gerade zeichnen |  |  | Hauptplatz nach typ „y-Achsenabschnitt ablesen“ (bis 12.10.: erkennen und ablesen) |
| 2024-OS-K3a | Gerade zeichnen |  |  | Hauptplatz nach typ „Gerade aus Gleichung zeichnen“ (bis 12.10.: aus Gleichung zeichnen) |
| 2025-OS-B1f | Gerade zeichnen |  |  | Hauptplatz nach typ „Graph einer linearen Funktion erkennen“ (bis 12.10.: erkennen und ablesen) |
| 2025-OS-K5a | Gleichung ablesen oder aus Punkten aufstellen |  |  | Hauptplatz nach typ „Gerade durch zwei Punkte zeichnen“. Zwischenschritt aus typ_neben (bis 12.10.: durch zwei Punkte, Gleichung ablesen) |
| 2026-EBR-K5a | Gerade zeichnen |  |  | EBR-Zwilling von 2026-FOR-K5a (bis 12.10.: aus Gleichung zeichnen) |
| 2026-EBR-K5b | Punktprobe |  |  | EBR-Zwilling von 2026-FOR-K5b (bis 12.10.: rechnerisch an Gerade und Parabel) |
| 2026-FOR-K5a | Gerade zeichnen |  |  | Hauptplatz nach typ „Gerade aus Gleichung zeichnen“ (bis 12.10.: aus Gleichung zeichnen) |
| 2026-FOR-K5b | Punktprobe |  |  | Hauptplatz nach typ „Punktprobe durchführen“ (bis 12.10.: rechnerisch an Gerade und Parabel) |
