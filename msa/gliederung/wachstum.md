# Gliederung Wachstum (P10)

Prüfung: msa
Kapitel: wachstum
Gebiet: Funktionen
Name: Wachstum
Folge: 7
Bank: potenz-exponentialfunktionen
Katalog: katalog/potenz-exponentialfunktionen.md

Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,
didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die
Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py
und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026.

## Stufen

### Tabelle ergänzen
- **Kern:** ja – 5 echte 2016–2026, Einstieg fast jeder Wachstumsaufgabe (Niveau I), Bank-Kette Wachstumstabelle fortschreiben mit Grundfall
- **Originale:** 2026-FOR-K7a 2020-OS-K4a 2019-OS-K7a 2017-OS-K7a 2016-OS-K4a
- **Bank:** potenz-exponentialfunktionen-e2-k2-s1 potenz-exponentialfunktionen-e2-k2-s2 potenz-exponentialfunktionen-e2-k2-s3 potenz-exponentialfunktionen-e2-k2-s4 potenz-exponentialfunktionen-e2-k2-s5 potenz-exponentialfunktionen-e2-k2-s6 potenz-exponentialfunktionen-e2-k2-s7 potenz-exponentialfunktionen-e2-k2-s8 potenz-exponentialfunktionen-e2-k3-s3
- **Verwechselbar:** lineare:Endwert berechnen
- **Zuschnitt:** Exponentielles Wachstum

### Punkte darstellen
- **Kern:** ja – 4 echte (2016, 2017, 2021, 2025), Bank-Kette Wertepaare darstellen mit Grundfall
- **Originale:** 2025-OS-K7a 2017-OS-K7b 2016-OS-K4b 2021-OS-K6b
- **Bank:** potenz-exponentialfunktionen-e1-k3-s1 potenz-exponentialfunktionen-e1-k3-s2 potenz-exponentialfunktionen-e1-k3-s3 potenz-exponentialfunktionen-e1-k3-s4 potenz-exponentialfunktionen-e1-k3-s5 potenz-exponentialfunktionen-e1-k4-s3
- **Zuschnitt:** Exponentielles Wachstum

### Faktor bestimmen, Gleichung aufstellen
- **Kern:** ja – 8 echte 2016–2026 (mit Funktionswert aus der Gleichung), Bank-Ketten Wachstumsfaktor und Exponentialfunktion aufstellen mit Grundfall
- **Originale:** 2025-OS-K7b 2026-FOR-K7c 2018-OS-K2a 2017-OS-K7c 2019-OS-K7b 2020-OS-K4c 2017-OS-K7d 2016-OS-K4e
- **Bank:** potenz-exponentialfunktionen-e2-k1-s1 potenz-exponentialfunktionen-e2-k1-s2 potenz-exponentialfunktionen-e2-k1-s3 potenz-exponentialfunktionen-e2-k1-s4 potenz-exponentialfunktionen-e2-k1-s5 potenz-exponentialfunktionen-e2-k1-s6 potenz-exponentialfunktionen-e2-k1-s7 potenz-exponentialfunktionen-e3-k1-s2 potenz-exponentialfunktionen-e3-k1-s3 potenz-exponentialfunktionen-e3-k1-s4 potenz-exponentialfunktionen-e3-k1-s5 potenz-exponentialfunktionen-e3-k1-s7 potenz-exponentialfunktionen-e3-k2-s2 potenz-exponentialfunktionen-e3-k2-s3 potenz-exponentialfunktionen-e3-k2-s5 potenz-exponentialfunktionen-e3-k2-s8 potenz-exponentialfunktionen-e3-k3-s3
- **Verwechselbar:** lineare:Gleichung aufstellen und rückwärts rechnen
- **Zuschnitt:** Exponentielles Wachstum

### Graph zuordnen und begründen
- **Kern:** nein – 2 echte (2019, 2026), Niveau II/III
- **Originale:** 2026-FOR-K7b 2019-OS-K7c
- **Bank:** potenz-exponentialfunktionen-e1-k2-s3 potenz-exponentialfunktionen-e1-k2-s4 potenz-exponentialfunktionen-e1-k2-s5 potenz-exponentialfunktionen-e1-k2-s6 potenz-exponentialfunktionen-e1-k2-s7
- **Zuschnitt:** Exponentielles Wachstum

## Plätze der Originale

Jede Teilaufgabe 2014–2026 (OS, EBR, FOR, GYM) mit ihrem Hauptplatz (Stufe, deren Handgriff die
ganze Teilaufgabe ist), „ganz auch“ (die ganze Aufgabe ist dieser Handgriff, obwohl anders
etikettiert) und Zwischenschritt; Stufen anderer Kapitel mit „kapitel:“. Erzeugt daraus:
msa/handgriffe-p10.csv (werkzeuge/gliederung-sichten.py).

| id | Hauptplatz | Ganz auch | Zwischenschritt | Begründung |
|---|---|---|---|---|
| 2014-GYM-K4b |  |  | Faktor bestimmen, Gleichung aufstellen; Graph zuordnen und begründen | Hauptplatz außerhalb der P10-Stufen. Zwischenschritt aus typ_neben |
| 2016-GYM-K2a | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Parameter einer Exponentialfunktion bestimmen“ |
| 2016-GYM-K2b | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Wachstumsfaktor aus Tabelle bestimmen“ |
| 2016-OS-K4a | Tabelle ergänzen |  |  | Hauptplatz nach typ „Wachstumstabelle ergänzen“ |
| 2016-OS-K4b | Punkte darstellen |  |  | Hauptplatz nach typ „Achseneinteilung wählen“ |
| 2016-OS-K4d | Graph zuordnen und begründen |  |  | Hauptplatz nach typ „Wachstumsart begründen“. nicht in katalog_ids der Zuordnung |
| 2016-OS-K4e | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Funktionswert berechnen“ |
| 2017-OS-K7a | Tabelle ergänzen |  |  | Hauptplatz nach typ „Wachstumstabelle ergänzen“ |
| 2017-OS-K7b | Punkte darstellen |  |  | Hauptplatz nach typ „Achseneinteilung wählen“ |
| 2017-OS-K7c | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Exponentialfunktion aufstellen“ |
| 2017-OS-K7d | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Funktionswert berechnen“ |
| 2018-OS-K2a | Faktor bestimmen, Gleichung aufstellen |  | prozent:Erhöhung und Veränderung in Prozent | Hauptplatz nach typ „Wachstumsfaktor aus Tabelle bestimmen“. 600 000 € um 8 % erhöht |
| 2018-OS-K2b | Graph zuordnen und begründen |  |  | Hauptplatz nach typ „Wachstumsart begründen“. nicht in katalog_ids der Zuordnung |
| 2018-OS-K2c |  |  | Tabelle ergänzen | Hauptplatz außerhalb der P10-Stufen. Werte Jahr für Jahr mit 1,08 fortschreiben |
| 2019-OS-K7a | Tabelle ergänzen |  |  | Hauptplatz nach typ „Wachstumstabelle ergänzen“ |
| 2019-OS-K7b | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Gleichung im Sachzusammenhang deuten“ |
| 2019-OS-K7c | Graph zuordnen und begründen |  |  | Hauptplatz nach typ „Graph zu Wachstumsprozess zuordnen“ |
| 2020-OS-K4a | Tabelle ergänzen |  |  | Hauptplatz nach typ „Wachstumstabelle ergänzen“ |
| 2020-OS-K4c | Faktor bestimmen, Gleichung aufstellen | prozent:Erhöhung und Veränderung in Prozent |  | Hauptplatz nach typ „Funktionswert berechnen“. Funktionswert nach typ Hauptplatz, Studie 2 (+40 %) ganz in P5 |
| 2021-GYM-K3a | Punkte darstellen |  |  | Hauptplatz nach typ „Wertetabelle als Punkte darstellen“ |
| 2021-GYM-K3b | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Wachstumsfaktor aus Tabelle bestimmen“ |
| 2021-OS-K6b | Punkte darstellen |  |  | Hauptplatz nach typ „Wertetabelle als Punkte darstellen“ |
| 2024-GYM-K4a | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Funktionswert berechnen“ |
| 2024-GYM-K4b | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Funktionswert berechnen“ |
| 2024-GYM-K4d | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Parameter einer Exponentialfunktion bestimmen“ |
| 2025-GYM-K3a | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach Urteil. Punktprobe an einer Exponentialfunktion |
| 2025-GYM-K3e | Faktor bestimmen, Gleichung aufstellen |  | Punkte darstellen | Hauptplatz nach typ „Funktionswert berechnen“. Zwischenschritt aus typ_neben |
| 2025-OS-K7a | Punkte darstellen |  |  | Hauptplatz nach typ „Wertetabelle als Punkte darstellen“ |
| 2025-OS-K7b | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Wachstumsfaktor aus Tabelle bestimmen“ |
| 2026-EBR-K7a | Tabelle ergänzen |  |  | EBR-Zwilling von 2026-FOR-K7a |
| 2026-EBR-K7b | Graph zuordnen und begründen |  |  | EBR-Zwilling von 2026-FOR-K7b |
| 2026-FOR-K7a | Tabelle ergänzen |  |  | Hauptplatz nach typ „Wachstumstabelle ergänzen“ |
| 2026-FOR-K7b | Graph zuordnen und begründen |  |  | Hauptplatz nach typ „Graph zu Wachstumsprozess zuordnen“ |
| 2026-FOR-K7c | Faktor bestimmen, Gleichung aufstellen |  |  | Hauptplatz nach typ „Exponentialfunktion aufstellen“ |
