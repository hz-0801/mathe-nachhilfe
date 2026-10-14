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
Kennung neu: Lineare Funktionen = PA10

Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,
didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die
Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py
und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026; Stufen wie im Buch und nach dem Gesuchten
12.10.2026 (TAL2).

## Stufen

Ein Blatt „Lineare Funktionen“ (TAL), Stufen wie im Buch und nach dem Gesuchten (pruefung.md § 5,
Lehrer 12.10.): Gerade zeichnen · Gleichung aus Graph · Gleichung aus zwei Punkten · Nullstelle ·
Punktprobe · Gleichung aus Text; „Schnittpunkt zweier Geraden“ ist Buchstufe ohne Original
(msa/buchstufen-p10.csv, nur Handreichung). Eine Teilaufgabe steht bei dem, was sie zuletzt sucht
(wie Quadratische 12.10.): 2022-OS-K3a (zeichnen, dann Nullstelle) bei Nullstelle, 2025-OS-K5a
(zeichnen, dann Gleichung) bei Gleichung aus zwei Punkten. Die drei Buchstufen des Sachzusammenhangs
(Gleichung aus Text, Wert berechnen, Angebote vergleichen) sind eine Stufe: erster Schritt jedes Originals
ist, Anfangswert und Änderung aus dem Text zu holen (Schülerfrage). Einstieg Geraden = Erkennen (Lehrer
12.10.): vier Funktionen, die linearen ankreuzen, an einer m und n benennen; danach 2025-OS-B1f (Graphen).

TAL3 (Lehrer 13.10.): „Gleichung ablesen oder aus Punkten aufstellen“ ist geteilt in „Gleichung aus
Graph“ (erster Schritt: n am Graphen ablesen, dann Steigungsdreieck) und „Gleichung aus zwei Punkten“
(erster Schritt: m = Δy : Δx, dann n) – verschiedene erste Schritte. „Gleichung aus Graph“ hat nur
Originale von 2019 und entfällt deshalb auf dem Blatt (Mehr-Block); 2024-OS-B1i bleibt bei „Gerade
zeichnen“ (n wird aus der Gleichung gelesen und eingezeichnet, gesucht ist ein Punkt im Bild). Die
Parabel-Punktprobe 2024-OS-K3c und die quadratische Gleichung 2025-OS-B1h stehen nicht mehr auf dem
Geraden-Blatt, sondern ungekürzt auf dem Gemischt-Blatt Gerade und Parabel (mehr-p10.csv, Einheit
„Gemischt: Gerade und Parabel“; pruefung.md „Zweitthema ausblenden“). Koordinatensysteme breiter (Karo
0,45 cm, Gerade über mehrere Einheiten mit Platz für ein Steigungsdreieck), Lösungen mit Ansatz.

Runde 8 (Lehrer 13.10.): Fenster wie im Original, wo der fremde Teil nicht ausgeblendet ist (Fenster
verrät die Lösung nicht); 2026-FOR-K5a eigenes Fenster ohne Parabel nicht mehr nötig, die Teilaufgabe
steht ungekürzt im Abschnitt „Gemischt: Gerade und Parabel“ (am Ende, auch auf Quadratische), ebenso
2023-OS-K4a; das Bündel 2024-3a/2026-5a ist aufgelöst. „Gleichung aus Graph“ wird mit den Originalen
2019-OS-K2b/K2c gefüllt (Setzer v0.11, ältere füllen eine leere Stufe), Graphen f, g, h als grafik.

Häufigkeit (pruefung.md § 5, Lehrer 13.10.; P10-Hefte 2014–2026 ohne GYM, Hauptplatz, ganz auch und
Zwischenschritt aus msa/handgriffe-p10.csv): keine Stufe kam fast jedes Jahr. Gerade zeichnen 7 von 13
Jahren (2016, 2021–2026), Punktprobe 9 (Lücken 2015, 2016, 2019, 2020), Gleichung aus Text 4, aus zwei
Punkten 3, aus Graph 1, Nullstelle 3; das ganze Kapitel fehlt 2014, 2018 und 2020. Darum keine Zeile
„Häufigkeit“; der Setzer druckt die Jahre.

### Gerade zeichnen
- **Anzeigename:** Gerade zeichnen
- **Regine:** S. 31
- **Frage:** Wo steht die Gleichung der linearen Funktion mit m und n? Formelsammlung, Seite ___
- **Heranführung:** Lehrer 13.10. (TAL3 Nr. 1 „besser mit Formelsammlung: allgemeine Gleichung, m und n“); der Stups zur Steigungsformel bei „Gleichung aus zwei Punkten“ entfällt (ein Formelsammlungs-Stups je Blatt).
- **Schülerfrage:** Welche Funktionen sind linear? Kreuze an. Wähl eine lineare aus und gib ihr m und n an: $m = \underline{\hspace{10mm}}$, $n = \underline{\hspace{10mm}}$.
- **Schülerfrage-Fälle:** $f(x) = 3 - 2x$ → ja | $f(x) = x^2 + 1$ → nein | $f(x) = 0{,}5x$ → ja
- **Schülerfrage-Form:** kreuz:linear
- **Schülerfrage-Weg:** linear sind a) und c): a) m = −2, n = 3 (die Zahl vor x ist m, auch hinten); c) m = 0,5, n = 0; x² gibt keine Gerade
- **Kern:** ja – Graph erkennen, y-Achsenabschnitt einzeichnen, Gerade aus der Gleichung zeichnen, Eigenschaften prüfen (Basisteil 2016, 2024, 2025; Niveau I–II); Bank-Kette Graph zeichnen mit Grundfall
- **Originale:** 2025-OS-B1f 2024-OS-B1i 2024-OS-K3a 2026-FOR-K5a 2023-OS-K4a 2016-OS-B1c 2021-OS-K2a 2021-OS-K2b
- **Bank:** lineare-funktionen-e2-k4-s5(i) lineare-funktionen-e2-k4-s6(i) lineare-funktionen-e2-k4-s7(i) lineare-funktionen-e2-k4-s8(i) lineare-funktionen-e2-k6-s1(i) lineare-funktionen-e2-k7-s2(i) lineare-funktionen-e4-k4-s2(i) lineare-funktionen-e3-k2-s7[2023-OS-K4a,2021-OS-K2b]
- **Zuschnitt:** Lineare Funktionen
- **Durchsicht 13.10.:** Runde A: Anstoß steht für sich; drei statt vier Fälle (4 : x gestrichen – x² trägt schon „keine Gerade“), jeder trägt einen Gedanken: m hinten, keine Gerade, n = 0.

### Gleichung aus Graph
- **Anzeigename:** Gleichung ablesen
- **Regine:** S. 31
- **Kern:** ja – erster Schritt: n am Schnitt mit der y-Achse ablesen, dann m mit einem Steigungsdreieck (Graph nach Steigung auswählen, Gleichung zum Graphen zuordnen 2019; Niveau I–II); Bank-Kette Ablesen mit Grundfall. Kein Original 2022–2026: die Stufe entfällt auf dem Blatt, die Originale stehen im Mehr-Block (Lehrer 13.10.: geteilt, weil der erste Schritt ein anderer ist als bei zwei Punkten). 2024-OS-B1i bleibt bei „Gerade zeichnen“: dort wird n aus der Gleichung gelesen und eingezeichnet, gesucht ist ein Punkt im Bild, nicht die Gleichung
- **Originale:** 2019-OS-K2b 2019-OS-K2c
- **Bank:** lineare-funktionen-e2-k5-s1(i) lineare-funktionen-e2-k5-s2(i) lineare-funktionen-e2-k5-s3(i) lineare-funktionen-e2-k5-s4(i) lineare-funktionen-e2-k5-s5(i) lineare-funktionen-e2-k5-s6(i)
- **Zuschnitt:** Lineare Funktionen
- **Durchsicht 13.10.:** Runde A: unverändert; Name in der Reihe „Gleichung aus …“, kein Anstoß nötig.

### Gleichung aus zwei Punkten
- **Anzeigename:** Gleichung aus zwei Punkten
- **Regine:** S. 31
- **Kern:** ja – erster Schritt: m = Δy : Δx aus den Koordinaten, dann n durch Einsetzen eines Punktes (2015, 2017, 2025; Niveau I–II); Bank-Ketten Gerade durch zwei Punkte zeichnen und Gleichung bestimmen mit Grundfall. 2025-OS-K5a zeichnet erst und sucht zuletzt die Gleichung
- **Originale:** 2025-OS-K5a 2017-OS-K5a 2015-OS-K4d
- **Bank:** lineare-funktionen-e4-k2-s1(i) lineare-funktionen-e4-k1-s3(i) lineare-funktionen-e4-k1-s4(i) lineare-funktionen-e4-k1-s5(i) lineare-funktionen-e4-k1-s6[v1,v2,v5,v6](i) lineare-funktionen-e4-k1-s6[v3,v4] lineare-funktionen-e4-k4-s4
- **Zuschnitt:** Lineare Funktionen
- **Durchsicht 13.10.:** Runde A: unverändert; der Anstoß ist der einzige Hinweis auf die Formelsammlung und steht für sich.

### Nullstelle
- **Anzeigename:** Nullstelle gesucht
- **Regine:** S. 31
- **Kern:** nein – 2 echte (2019 ablesen, 2022 nach dem Zeichnen angeben), Niveau I; Bank Funktionswert null
- **Originale:** 2022-OS-K3a 2019-OS-K2a
- **Bank:** lineare-funktionen-e3-k2-s6(i) lineare-funktionen-e3-k5-s4(i)
- **Zuschnitt:** Lineare Funktionen
- **Durchsicht 13.10.:** Runde A: Name „Nullstelle gesucht“ (Reihe … gesucht); kein Anstoß – ein Anstoß (beide Achsenpunkte einer anderen Geraden) kostete eine Seite, im Bericht gemeldet.

### Punktprobe
- **Anzeigename:** Punktprobe
- **Regine:** S. 31
- **Kern:** ja – einsetzen und vergleichen an einer Geraden (2017, 2023, 2026; Befund Funktionen 10.10., Lehrer 10.10.: Einsetzen ist ein Handgriff); Bank-Kette Funktionswert mit Grundfall. Die Punktprobe an der Parabel (2024-OS-K3c) und die quadratische Gleichung durch Einsetzen (2025-OS-B1h) stehen nicht auf dem Geraden-Blatt (Lehrer 13.10., „Zweitthema ausblenden“): der Schüler soll hier die lineare Punktprobe üben, nicht quadrieren; beide ungekürzt fürs Gemischt-Blatt Gerade und Parabel (msa/mehr-p10.csv, Einheit „Gemischt: Gerade und Parabel“), hier nur „ganz auch“
- **Originale:** 2023-OS-B1i 2026-FOR-K5b 2017-OS-K5b
- **Bank:** lineare-funktionen-e3-k2-s5(i) lineare-funktionen-e3-k2-s7[2023-OS-B1i,2026-FOR-K5b,2017-OS-K5b,2019-OS-K2a,2021-OS-K6d,2022-OS-K3a] quadratische-funktionen-e1-k1-s4 quadratische-funktionen-e3-k1-s2 quadratische-funktionen-e4-k1-s14 quadratische-gleichungen-e1-k2-s12(i) quadratische-gleichungen-e2-k1-s5(i) quadratische-gleichungen-e3-k3-s13(i)
- **Zuschnitt:** Lineare Funktionen
- **Durchsicht 13.10.:** Runde A: Name nach dem, was der Schüler tut, wie auf dem Parabel-Blatt („Punkt auf der Parabel prüfen“); kein Anstoß nötig.

### Gleichung aus Text
- **Anzeigename:** Gleichung aus Text
- **Regine:** S. 31
- **Schülerfrage:** Welche Zahl ist m, welche n? Rechne nicht.
- **Heranführung:** TAL3 Nr. 10, Lehrer 13.10.: „Gedanke gut, Fassung zu lang“ – gekürzt.
- **Schülerfrage-Fälle:** Handytarif: 8 € im Monat und 0,09 € je Minute = 8 ist n, 0,09 ist m | Kerze: 25 cm hoch, brennt je Stunde 2 cm ab = 25 ist n, −2 ist m
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** n steht am Anfang (x = 0), m ist das, was je Monat, Minute oder Stunde dazukommt oder weggeht
- **Kern:** ja – Wert berechnen, Gleichung aufstellen und deuten, rückwärts rechnen, Graph zum Tarif zuordnen, Angebote vergleichen (2016, 2021, 2022, 2023; Niveau I–II); Bank-Kette Anwendung mit Grundfall
- **Originale:** 2022-OS-K6a 2022-OS-K6b 2023-OS-K3a 2023-OS-K3b 2021-OS-K6a 2021-OS-K6c 2021-OS-K6d 2021-OS-K7a 2016-OS-K6a 2016-OS-K6b 2016-OS-K6c
- **Bank:** lineare-funktionen-e5-k1-s3 lineare-funktionen-e5-k4-s4 lineare-funktionen-e5-k1-s1 lineare-funktionen-e5-k1-s2 lineare-funktionen-e5-k3-s1 lineare-funktionen-e5-k4-s1 lineare-funktionen-e1-k1-s8 lineare-funktionen-e5-k2-s1 lineare-funktionen-e5-k1-s4 lineare-funktionen-e5-k4-s2 lineare-funktionen-e5-k1-s5[2022-OS-K6a,2021-OS-K6a,2022-OS-K6b,2016-OS-K6c,2021-OS-K7a,2023-OS-K3a,2016-OS-K6a,2023-OS-K3b,2016-OS-K6b]
- **Gleichungssysteme:** geprüft 13.10. (Lehrer: geht es um Gleichungen aus Text, bleibt es bei Lineare): keine Sachaufgabe dieser Stufe braucht zwei Gleichungen – 2022-OS-K6a/b und 2016-OS-K6c eine Gleichung, 2023-OS-K3a/b und 2016-OS-K6a/b vergleichen zwei Angebote durch Einsetzen (kein System), 2021-OS-K7a ordnet zu. Die Aufgaben mit zwei Gleichungen (2016-OS-K6d, 2021-OS-K7b, 2024-OS-K7a) stehen schon im Kapitel gleichungssysteme (Stufe „aufstellen“); nichts auszublenden
- **Verwechselbar:** wachstum:Tabelle ergänzen | wachstum:Faktor bestimmen, Gleichung aufstellen
- **Zuschnitt:** Lineare Funktionen
- **Durchsicht 13.10.:** Runde A: unverändert; Anstoß steht für sich, zwei Fälle, je ein Gedanke (m und n trennen, m negativ beim Abnehmen).

### Gemischt: Gerade und Parabel
- **Anzeigename:** Gerade und Parabel
- **Regine:** S. 21 · 31
- **Zuschnitt:** Lineare Funktionen
- **Kern:** nein – Abschnitt am Ende (pruefung.md § 5 „Gemischt als letzter Abschnitt“, Lehrer 13.10., Weg C): die Teilaufgaben, die Gerade und Parabel zugleich brauchen, ungekürzt – 2025-OS-B1h, 2026-FOR-K5a (Gerade ins System mit der Parabel), 2024-OS-K3c/3d, 2023-OS-K4a (Schnittpunkt ablesen), 2022-OS-K3c (gleichsetzen); Zeilen einmal in mehr-p10 (einheit „Gemischt: Gerade und Parabel“), auf Lineare und Quadratische gleich gesetzt
- **Originale:** 2025-OS-B1h 2026-FOR-K5a 2024-OS-K3c 2024-OS-K3d 2023-OS-K4a 2022-OS-K3c
- **Durchsicht 13.10.:** Runde A: unverändert, gleich auf Lineare und Quadratische.

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
| 2015-OS-K4d | Gleichung aus zwei Punkten |  |  | Hauptplatz nach typ „Geradengleichung aus zwei Punkten“ (bis 12.10.: durch zwei Punkte, Gleichung ablesen) |
| 2016-GYM-B1c | Gerade zeichnen |  |  | GYM-Zwilling von 2016-OS-B1c (bis 12.10.: erkennen und ablesen) |
| 2016-GYM-K2c |  |  | Gerade zeichnen | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2016-OS-B1c | Gerade zeichnen |  |  | Hauptplatz nach typ „Graph nach Eigenschaft auswählen“ (bis 12.10.: erkennen und ablesen) |
| 2016-OS-K6a | Gleichung aus Text |  |  | Hauptplatz nach typ „Graph zu Tarif zuordnen“ (bis 12.10.: Graph zum Tarif zuordnen) |
| 2016-OS-K6b | Gleichung aus Text |  |  | Hauptplatz nach typ „Tarife vergleichen“ (bis 12.10.: Tarife vergleichen) |
| 2016-OS-K6c | Gleichung aus Text |  |  | Hauptplatz nach typ „Lineare Funktion aus Sachverhalt aufstellen“ (bis 12.10.: Gleichung aufstellen und rückwärts rechnen) |
| 2017-GYM-K5b | Gleichung aus Text |  | prozent:Erhöhung und Veränderung in Prozent | Hauptplatz nach typ „Tarife vergleichen“. Nettopreis um 19 % erhöht (bis 12.10.: Tarife vergleichen) |
| 2017-OS-K5a | Gleichung aus zwei Punkten |  |  | Hauptplatz nach typ „Gerade durch zwei Punkte zeichnen“ (bis 12.10.: durch zwei Punkte, Gleichung ablesen) |
| 2017-OS-K5b | Punktprobe |  |  | Hauptplatz nach typ „Funktionswert berechnen“ (bis 12.10.: rechnerisch an Gerade und Parabel) |
| 2018-GYM-K2d |  |  | Gerade zeichnen; dreiecke:Winkel berechnen | Hauptplatz außerhalb der P10-Stufen. Neigungswinkel über tan |
| 2019-OS-K2a | Nullstelle |  |  | Hauptplatz nach typ „Nullstelle am Graphen ablesen“ (bis 12.10.: erkennen und ablesen) |
| 2019-OS-K2b | Gleichung aus Graph |  |  | Hauptplatz nach typ „Graph nach Eigenschaft auswählen“ (bis 12.10.: erkennen und ablesen) |
| 2019-OS-K2c | Gleichung aus Graph |  |  | Hauptplatz nach typ „Geradengleichung zu Graph zuordnen“ (bis 12.10.: erkennen und ablesen) |
| 2020-GYM-K3c |  |  | Nullstelle | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2021-GYM-K3c | Gleichung aus zwei Punkten |  | flaechen:Fläche gesucht | Hauptplatz nach typ „Geradengleichung aus zwei Punkten“. Trapezfläche unter der Geraden (bis 12.10.: durch zwei Punkte, Gleichung ablesen) |
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
| 2024-GYM-B1b |  |  | Gleichung aus zwei Punkten | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2024-OS-B1i | Gerade zeichnen |  |  | Hauptplatz nach typ „y-Achsenabschnitt ablesen“ (bis 12.10.: erkennen und ablesen) |
| 2024-OS-K3a | Gerade zeichnen |  |  | Hauptplatz nach typ „Gerade aus Gleichung zeichnen“ (bis 12.10.: aus Gleichung zeichnen) |
| 2025-OS-B1f | Gerade zeichnen |  |  | Hauptplatz nach typ „Graph einer linearen Funktion erkennen“ (bis 12.10.: erkennen und ablesen) |
| 2025-OS-K5a | Gleichung aus zwei Punkten |  |  | Hauptplatz nach typ „Gerade durch zwei Punkte zeichnen“. Zwischenschritt aus typ_neben (bis 12.10.: durch zwei Punkte, Gleichung ablesen) |
| 2026-EBR-K5a | Gerade zeichnen |  |  | EBR-Zwilling von 2026-FOR-K5a (bis 12.10.: aus Gleichung zeichnen) |
| 2026-EBR-K5b | Punktprobe |  |  | EBR-Zwilling von 2026-FOR-K5b (bis 12.10.: rechnerisch an Gerade und Parabel) |
| 2026-FOR-K5a | Gerade zeichnen |  |  | Hauptplatz nach typ „Gerade aus Gleichung zeichnen“ (bis 12.10.: aus Gleichung zeichnen) |
| 2026-FOR-K5b | Punktprobe |  |  | Hauptplatz nach typ „Punktprobe durchführen“ (bis 12.10.: rechnerisch an Gerade und Parabel) |
