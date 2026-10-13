# Gliederung Daten (P10)

Prüfung: msa
Kapitel: daten
Gebiet: Daten + Zufall
Name: Daten
Folge: 9
Bank: daten
Katalog: katalog/daten.md
Anzeigenamen: Kenngrößen = Kenngrößen | Diagramme = Kreis- und Säulendiagramme
Kennung: Kenngrößen = K9X
Kennung: Diagramme = DGH

Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,
didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die
Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py
und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026.

## Stufen

Zwei Blätter (Runde 8, Lehrer 13.10.; pruefung.md § 5 „Blatt = alle Originale der letzten fünf Jahre“):
Kenngrößen (K9X, 10 Originale 2022–2026) und Diagramme (DGH). Kreisdiagramm (3 Originale 2022–2026) und
Diagramm ergänzen und beurteilen (4) haben je höchstens vier junge Originale und werden ein Blatt mit fünf
Stufen (Grenze der Regel: zwei Seiten, endet mit der schwersten echten, 2026-FOR-K3e); Kennung 32A ist frei.
Stufen wie im Buch (msa/buchstufen-p10.csv) und nach dem Gesuchten: Spannweite · Median · Modalwert ·
Mittelwert · fehlender Wert · Aussagen zu Kenngrößen; Winkel im Kreisdiagramm · Kreisdiagramm zeichnen ·
Säule ergänzen · Aussage zum Diagramm · falscher Eindruck. Modalwert hat kein Original (nur Teilschritt in
2025-OS-K6a) und steht nur in der Handreichung; relative Häufigkeit, Boxplot, Histogramm, Wert ablesen sind
Buchstufen ohne eigenes Original. 2022-OS-K4a (Minimum, Maximum, dann Durchschnitt) steht bei dem, was sie
zuletzt sucht, unter Mittelwert (wie Lineare 12.10.); 2024-OS-K2b ohne Prozentteil (Zweitthema, Spalten
*_einheit; 2024-OS-K2b-Prozent bleibt Kapitel Prozent).
Einstiege nur, wo der Schüler vor dem Original stolpert: Median (erst ordnen), fehlender Wert (Formel
umstellen, Runde A 13.10.), Winkel (Anteil · 360°), Säule ergänzen (ein Schritt an der Achse ist wie viel wert?).
Häufigkeit (pruefung.md § 5, Lehrer 13.10.; P10-Hefte 2014–2026 ohne GYM, Hauptplatz, ganz auch und
Zwischenschritt): Spannweite 9 von 13 Jahren (Lücken 2015–2018), Mittelwert 9 (Lücken 2014, 2018, 2019,
2023), alle übrigen höchstens 4 – keine Stufe „fast immer“; der Setzer druckt die Jahre. Eine Datenaufgabe
mit Spannweite oder Mittelwert kam allerdings seit 2014 jedes Jahr außer 2018 – das gilt dem Kapitel, nicht
einer Stufe.

### Minimum, Maximum, Spannweite
- **Anzeigename:** Spannweite gesucht
- **Regine:** S. 42
- **Kern:** ja – 8 echte 2014–2026 (2022-OS-K4a seit 13.10. unter Mittelwert), fast jedes Jahr Einstieg der Datenaufgabe (Niveau I), Bank-Kette Kenngrößen mit Grundfall
- **Originale:** 2026-FOR-K3a 2024-OS-K2a 2023-OS-K6c 2021-OS-K5a 2020-OS-K2d 2019-OS-B1i 2014-OS-K4a 2014-OS-K4b
- **Bank:** daten-e4-k1-s1 daten-e4-k1-s2 daten-e4-k1-s9 daten-e4-k1-s8
- **Verwechselbar:** Median | Mittelwert
- **Zuschnitt:** Kenngrößen
  - Minimum, Maximum, Spannweite [2022-OS-K4a 2023-OS-K6c 2026-FOR-K3a 2024-OS-K2a 2025-OS-K6a]
- **Durchsicht 13.10.:** Runde A: Anzeigename nach dem Gesuchten („Spannweite gesucht“); keine Heranführung, das erste Original (größter minus kleinster Preis) ist der Einstieg.
- **Frage:** Kenngrößen in deiner Formelsammlung: Seite ___
- **Probe 14.10.:** Ebene 1 (Seitenfrage, einmal je Blatt, an der ersten Stufe): Regine S. 42 hat alle Kenngrößen des Blatts auf einer Seite (Spannweite R, Zentralwert, Mittelwert, Modalwert); Lösung „S. 42“ aus Feld Regine.

### Median
- **Anzeigename:** Median gesucht
- **Regine:** S. 42
- **Schülerfrage:** Zentralwert (Median): erst ordnen – die Mitte der ungeordneten Reihe ist es nicht.
- **Schülerfrage-Fälle:** 9; 4; 7; 2; 5 → 5 (nicht 7) | 8; 2; 6; 4 → 5 (nicht 4)
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** ungeordnet stünde 7 bzw. 2 und 6 in der Mitte; geordnet 2; 4; 5; 7; 9: der dritte, 5; geordnet 2; 4; 6; 8: zwischen 4 und 6, (4 + 6) : 2 = 5
- **Kern:** nein – 2 echte (Basisteil 2015, 2024), Sprosse der Kette Kenngrößen
- **Originale:** 2024-OS-B1h 2015-OS-B1f
- **Bank:** daten-e4-k1-s4 daten-e4-k1-s5
- **Verwechselbar:** Minimum, Maximum, Spannweite | Mittelwert
- **Zuschnitt:** Kenngrößen
- **Durchsicht 13.10.:** Runde A: zwei Fälle statt einem – ungerade Anzahl (ordnen, Mitte abzählen) und gerade Anzahl (Mitte zwischen zwei Werten), denn ’24 · B1h hat sechs Werte; Satz „Erster Schritt beim Median“ weg, die Frage steht für sich.
- **Probe 14.10.:** Ebene 2 (Eigenschaft abfragen): Wort wie Regine S. 42 („Zentralwert“, Duden S. 37 ebenso); Erkennen-Schritt gegen die Fehlvorstellung „Median ohne Sortieren“ – die Mitte der ungeordneten Liste ist der falsche Wert; gerader Fall bleibt (’24 · 1h hat sechs Werte).

### Modalwert
- **Anzeigename:** Modalwert gesucht
- **Regine:** S. 42
- **Kern:** nein – kein Original 2014–2026, nur als Teilschritt (2025-OS-K6a); Stufe aus dem Zuschnitt (Lehrer 10.10.), damit die Kette Kenngrößen vollständig ist
- **Originale:**
- **Bank:** –
- **Zuschnitt:** Kenngrößen

### Mittelwert
- **Anzeigename:** Mittelwert gesucht
- **Regine:** S. 42
- **Kern:** ja – 8 echte 2015–2026 (Niveau I/II; mit 2022-OS-K4a), Bank-Kette Kenngrößen
- **Originale:** 2026-FOR-K3b 2024-OS-K2b 2022-OS-K4a 2021-OS-B1f 2017-OS-B1h 2016-OS-B1a 2020-OS-K2c 2015-OS-K7a
- **Bank:** daten-e4-k1-s6 daten-e4-k1-s7 daten-e4-k1-s10 daten-e4-k1-s11 daten-e4-k1-s12 daten-e4-k4-s4 daten-e6-k2-s3
- **Verwechselbar:** Minimum, Maximum, Spannweite | Median
- **Zuschnitt:** Kenngrößen
  - Mittelwert [2026-FOR-K3b 2024-OS-K2b 2025-OS-K6c]
- **Durchsicht 13.10.:** Runde A: Anzeigename nach dem Gesuchten; keine Heranführung (Summe durch Anzahl ist der Handgriff selbst, kein Stolperstein davor).

### rückwärts: fehlender Wert
- **Anzeigename:** Fehlender Wert gesucht
- **Regine:** S. 42
- **Schülerfrage:** Stelle die Formel nach der gesuchten Größe um.
- **Schülerfrage-Fälle:** Durchschnitt zweier Zahlen: m = (a + x) : 2, gesucht ist x → x = 2 · m − a
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** rückwärts erst mal 2: a + x = 2 · m (aus dem Durchschnitt wird die Summe), dann a abziehen: x = 2 · m − a
- **Kern:** nein – 1 echte (Basisteil 2022)
- **Originale:** 2022-OS-B1d
- **Bank:** daten-e4-k1-s13 daten-e6-k2-s4
- **Zuschnitt:** Kenngrößen
- **Durchsicht 13.10.:** Runde A: Rückwärts-Regel – statt „Durchschnitt 6, Summe?“ mit Zahlen jetzt Umstellen ohne Zahlen am Durchschnitt zweier Zahlen (einfacher als die sieben Tage von ’22 · B1d); er trägt beide Schritte (Summe aus dem Schnitt, dann die Bekannten abziehen).

### Aussagen prüfen, Auswirkung erklären
- **Anzeigename:** Aussagen zu Kenngrößen prüfen
- **Regine:** S. 42
- **Kern:** nein – 2 echte, nur 2025 (Niveau II/III)
- **Originale:** 2025-OS-K6a 2025-OS-K6c
- **Bank:** daten-e4-k1-s14 daten-e4-k1-s15 daten-e4-k1-s16 daten-e4-k3-s1 daten-e4-k4-s2
- **Zuschnitt:** Kenngrößen
- **Durchsicht 13.10.:** Runde A: Name bleibt (sagt schon, was der Schüler tut); keine Heranführung, ’25 · 6a erklärt den Modalwert im Text.

### Winkel berechnen und beschriften
- **Anzeigename:** Winkel gesucht
- **Regine:** S. 43
- **Schülerfrage:** Ein Sektor im Kreisdiagramm steht für einen Anteil. Wie viel Grad hat er? Der ganze Kreis hat 360°.
- **Schülerfrage-Fälle:** 10 % → 36 | 30 von 120 Befragten → 90
- **Schülerfrage-Form:** linie:°
- **Schülerfrage-Weg:** Anteil · 360°: 0,10 · 360° = 36°; 30 : 120 = 0,25 und 0,25 · 360° = 90°
- **Kern:** ja – 4 echte (2017, 2021, 2022, 2024), Bank-Kette Anteile darstellen mit Grundfall
- **Originale:** 2022-OS-K4d 2024-OS-K2c 2017-OS-K2c 2021-OS-K5b
- **Bank:** daten-e3-k1-s5 daten-e3-k1-s6 daten-e3-k1-s8 daten-e3-k1-s9 daten-e3-k1-s10 daten-e3-k1-s4 daten-e3-k3-s4 daten-e3-k1-s12[2017-OS-K2c,2024-OS-K2c]
- **Zuschnitt:** Diagramme
- **Durchsicht 13.10.:** Runde A: Anzeigename nach dem Gesuchten; Anregung statt Reihe – zwei Fälle, je einer für die zwei folgenden Aufgaben (Anteil in Prozent ’22 · 4d, Anteil aus Anzahlen ’24 · 2c), „die Hälfte“ raus; die Frage sagt, wofür der Sektor steht.

### aus Prozent darstellen
- **Anzeigename:** Kreisdiagramm zeichnen
- **Regine:** S. 43
- **Kern:** nein – 2 echte (2018, 2025)
- **Originale:** 2025-OS-K6b 2018-OS-K3c
- **Bank:** daten-e3-k1-s2 daten-e3-k1-s3 daten-e3-k3-s3 daten-e3-k1-s12[2025-OS-K6b]
- **Zuschnitt:** Diagramme
  - aus Prozent darstellen (selten geprüft, auffüllen) [] neben [2025-OS-K6b]
- **Durchsicht 13.10.:** Runde A: Name bleibt; keine Heranführung, den Winkel aus dem Anteil übt der Abschnitt davor.

### ergänzen
- **Anzeigename:** Säule ergänzen
- **Frage:** Wie viel ist ein Schritt an der Achse wert, von einer Linie zur nächsten? Steht dort keine Zahl, hilft eine bekannte Säule: ihr Wert durch ihre Schritte.
- **Kern:** ja – 4 echte (2018, 2020, 2023, 2026), Bank-Kette Diagramme lesen mit Grundfall
- **Originale:** 2026-FOR-K3d 2023-OS-K6d 2020-OS-K2a 2018-OS-K3a
- **Bank:** daten-e2-k2-s7 daten-e2-k2-s8 daten-e2-k2-s9 daten-e2-k2-s12 daten-e2-k3-s1 daten-e2-k4-s3
- **Zuschnitt:** Diagramme
- **Durchsicht 13.10.:** Runde A: der kursive Hinweis begann mit „Erster Schritt“ und „eine Hilfslinie“ (welche?) – jetzt eine Frage, die für sich steht (ein Schritt an der Achse, ohne Zahlen aus einer bekannten Säule); als nummerierte Aufgabe mit zwei Fällen ging das Blatt auf 4 Seiten, darum kursiv geblieben.

### Aussage prüfen
- **Anzeigename:** Aussage prüfen
- **Kern:** ja – 3 echte (2018, 2019, 2022), Bank-Kette Beurteilen mit Grundfall (Aussage mit einem Wert prüfen)
- **Originale:** 2022-OS-K4c 2018-OS-K3d 2019-OS-K5c
- **Bank:** daten-e5-k1-s1 daten-e5-k1-s2 daten-e5-k1-s3 daten-e5-k1-s4 daten-e5-k1-s5 daten-e5-k1-s7 daten-e5-k1-s8 daten-e5-k4-s4 daten-e5-k1-s11[2018-OS-K3d,2019-OS-K5c]
- **Zuschnitt:** Diagramme
- **Durchsicht 13.10.:** Runde A: Anzeigename kürzer als Reihe mit „… ergänzen“, „… erklären“; keine Heranführung.

### falschen Eindruck erklären
- **Anzeigename:** Falschen Eindruck erklären
- **Kern:** nein – 2 echte (2014, 2026), Niveau III, eine Sprosse der Kette Beurteilen
- **Originale:** 2026-FOR-K3e 2014-OS-K3d
- **Bank:** daten-e5-k1-s6 daten-e5-k1-s9 daten-e5-k3-s1 daten-e5-k4-s1 daten-e5-k4-s2 daten-e5-k1-s11[2026-FOR-K3e]
- **Zuschnitt:** Diagramme
- **Durchsicht 13.10.:** Runde A: Anzeigename sagt, was der Schüler tut; keine Heranführung.

## Plätze der Originale

Jede Teilaufgabe 2014–2026 (OS, EBR, FOR, GYM) mit ihrem Hauptplatz (Stufe, deren Handgriff die
ganze Teilaufgabe ist), „ganz auch“ (die ganze Aufgabe ist dieser Handgriff, obwohl anders
etikettiert) und Zwischenschritt; Stufen anderer Kapitel mit „kapitel:“. Erzeugt daraus:
msa/handgriffe-p10.csv (werkzeuge/gliederung-sichten.py).

| id | Hauptplatz | Ganz auch | Zwischenschritt | Begründung |
|---|---|---|---|---|
| 2014-GYM-B1e | rückwärts: fehlender Wert |  |  | Hauptplatz nach typ „Fehlenden Wert aus Spannweite bestimmen“ |
| 2014-GYM-K3a | Mittelwert |  |  | Hauptplatz nach typ „Arithmetisches Mittel berechnen“ |
| 2014-OS-K3d | falschen Eindruck erklären |  |  | Hauptplatz nach typ „Verzerrung eines Diagramms erklären“ |
| 2014-OS-K4a | Minimum, Maximum, Spannweite |  |  | Hauptplatz nach typ „Minimum und Maximum ablesen“ |
| 2014-OS-K4b | Minimum, Maximum, Spannweite |  |  | Hauptplatz nach typ „Spannweite berechnen“ |
| 2015-GYM-B1f | Median |  |  | GYM-Zwilling von 2015-OS-B1f |
| 2015-GYM-K5d | Mittelwert |  | prozent:Erhöhung und Veränderung in Prozent | Hauptplatz nach typ „Arithmetisches Mittel berechnen“. Zwischenschritt aus typ_neben |
| 2015-OS-B1f | Median |  |  | Hauptplatz nach typ „Median bestimmen“ |
| 2015-OS-K7a | Mittelwert |  |  | Hauptplatz nach typ „Arithmetisches Mittel berechnen“ |
| 2016-GYM-B1a | Mittelwert |  |  | GYM-Zwilling von 2016-OS-B1a |
| 2016-GYM-K3c | Minimum, Maximum, Spannweite |  |  | Hauptplatz nach typ „Spannweite berechnen“ |
| 2016-GYM-K5a | Winkel berechnen und beschriften |  | prozent:Prozentsatz | Hauptplatz nach typ „Kreisdiagramm zeichnen“. Zwischenschritt aus typ_neben |
| 2016-OS-B1a | Mittelwert |  |  | Hauptplatz nach typ „Arithmetisches Mittel berechnen“ |
| 2017-GYM-B1h | Mittelwert |  |  | GYM-Zwilling von 2017-OS-B1h |
| 2017-OS-B1h | Mittelwert |  |  | Hauptplatz nach typ „Arithmetisches Mittel berechnen“ |
| 2017-OS-K2c | Winkel berechnen und beschriften |  |  | Hauptplatz nach typ „Kreisdiagramm zeichnen“ |
| 2018-GYM-K3d |  |  | Mittelwert | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2018-OS-K3a | ergänzen |  |  | Hauptplatz nach typ „Achsenskalierung aus Säule bestimmen“ |
| 2018-OS-K3c | aus Prozent darstellen |  |  | Hauptplatz nach typ „Streifendiagramm zeichnen“ |
| 2018-OS-K3d | Aussage prüfen |  | prozent:Prozent und Anteil umwandeln | Hauptplatz nach typ „Aussage zu Diagramm prüfen“. Zwischenschritt aus typ_neben |
| 2019-GYM-K5a | Winkel berechnen und beschriften |  |  | Hauptplatz nach typ „Kreisdiagramm zeichnen“ |
| 2019-OS-B1i | Minimum, Maximum, Spannweite |  |  | Hauptplatz nach typ „Spannweite berechnen“ |
| 2019-OS-K5c | Aussage prüfen |  | falschen Eindruck erklären | Hauptplatz nach typ „Aussage zu Diagramm prüfen“. Zwischenschritt aus typ_neben |
| 2020-GYM-K6c | Minimum, Maximum, Spannweite |  | Winkel berechnen und beschriften | Hauptplatz nach typ „Spannweite berechnen“. Zwischenschritt aus typ_neben |
| 2020-OS-K2a | ergänzen |  |  | Hauptplatz nach typ „Säulen- oder Balkendiagramm ergänzen“ |
| 2020-OS-K2c | Mittelwert |  |  | Hauptplatz nach typ „Arithmetisches Mittel berechnen“ |
| 2020-OS-K2d | Minimum, Maximum, Spannweite | prozent:Erhöhung und Veränderung in Prozent |  | Hauptplatz nach typ „Spannweite berechnen“. zwei Aussagen, Spannweite nach typ Hauptplatz |
| 2021-OS-B1f | Mittelwert |  |  | Hauptplatz nach typ „Arithmetisches Mittel berechnen“ |
| 2021-OS-K5a | Minimum, Maximum, Spannweite | prozent:Erhöhung und Veränderung in Prozent | Mittelwert | Hauptplatz nach typ „Spannweite berechnen“. drei Teile, Spannweite nach typ Hauptplatz |
| 2021-OS-K5b | Winkel berechnen und beschriften |  |  | Hauptplatz nach typ „Fehlenden Prozentanteil ergänzen“ |
| 2022-GYM-K6a | Winkel berechnen und beschriften |  |  | Hauptplatz nach typ „Kreisdiagramm zeichnen“ |
| 2022-GYM-K6b | Minimum, Maximum, Spannweite |  | Median | Hauptplatz nach typ „Spannweite berechnen“. Zwischenschritt aus typ_neben |
| 2022-GYM-K6c | Aussage prüfen |  | falschen Eindruck erklären; prozent:Erhöhung und Veränderung in Prozent | Hauptplatz nach typ „Aussage zu Diagramm prüfen“. Abnahme 50 %, Achse beginnt nicht bei 0 |
| 2022-OS-B1d | rückwärts: fehlender Wert |  |  | Hauptplatz nach typ „Fehlenden Wert aus Mittelwert bestimmen“ |
| 2022-OS-K4a | Mittelwert |  | Minimum, Maximum, Spannweite | steht bei dem, was sie zuletzt sucht (Durchschnitt; Runde 8, 13.10.); Minimum und Maximum als Zwischenschritt |
| 2022-OS-K4c | Aussage prüfen |  |  | Hauptplatz nach typ „Aussage zu Diagramm prüfen“ |
| 2022-OS-K4d | Winkel berechnen und beschriften |  |  | Hauptplatz nach typ „Sektor im Kreisdiagramm zuordnen“ |
| 2023-GYM-K5a | aus Prozent darstellen |  |  | Hauptplatz nach typ „Streifendiagramm zeichnen“ |
| 2023-GYM-K5c | Mittelwert |  |  | Hauptplatz nach typ „Arithmetisches Mittel berechnen“ |
| 2023-GYM-K5d | rückwärts: fehlender Wert |  |  | Hauptplatz nach typ „Fehlenden Wert aus Mittelwert bestimmen“ |
| 2023-OS-K6c | Minimum, Maximum, Spannweite |  |  | Hauptplatz nach typ „Spannweite berechnen“ |
| 2023-OS-K6d | ergänzen |  |  | Hauptplatz nach typ „Achsenskalierung aus Säule bestimmen“ |
| 2024-OS-B1h | Median |  |  | Hauptplatz nach typ „Median bestimmen“ |
| 2024-OS-K2a | Minimum, Maximum, Spannweite |  |  | Hauptplatz nach typ „Spannweite berechnen“ |
| 2024-OS-K2b | Mittelwert |  | prozent:Erhöhung und Veränderung in Prozent | Hauptplatz nach typ „Arithmetisches Mittel berechnen“. Zwischenschritt aus typ_neben |
| 2024-OS-K2c | Winkel berechnen und beschriften |  |  | Hauptplatz nach typ „Sektor im Kreisdiagramm zuordnen“ |
| 2025-OS-K6a | Aussagen prüfen, Auswirkung erklären |  | Minimum, Maximum, Spannweite | Hauptplatz nach typ „Kenngrößen einer Liste prüfen“. Spannweite und Modalwert prüfen |
| 2025-OS-K6b | aus Prozent darstellen |  | prozent:Prozentsatz; Winkel berechnen und beschriften | Hauptplatz nach Zuordnung. Zwischenschritt aus typ_neben |
| 2025-OS-K6c | Aussagen prüfen, Auswirkung erklären |  | Mittelwert | Hauptplatz nach Zuordnung. Zwischenschritt aus typ_neben |
| 2026-EBR-K4a | Minimum, Maximum, Spannweite |  |  | EBR-Zwilling von 2026-FOR-K3a |
| 2026-EBR-K4b | Mittelwert |  |  | EBR-Zwilling von 2026-FOR-K3b |
| 2026-EBR-K4d | ergänzen |  |  | EBR-Zwilling von 2026-FOR-K3d |
| 2026-FOR-K3a | Minimum, Maximum, Spannweite |  |  | Hauptplatz nach typ „Spannweite berechnen“ |
| 2026-FOR-K3b | Mittelwert |  |  | Hauptplatz nach typ „Arithmetisches Mittel berechnen“ |
| 2026-FOR-K3d | ergänzen |  |  | Hauptplatz nach typ „Säulen- oder Balkendiagramm ergänzen“ |
| 2026-FOR-K3e | falschen Eindruck erklären |  |  | Hauptplatz nach typ „Verzerrung eines Diagramms erklären“ |
