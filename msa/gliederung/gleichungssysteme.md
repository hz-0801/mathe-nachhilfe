# Gliederung Gleichungssysteme (P10)

Prüfung: msa
Kapitel: gleichungssysteme
Gebiet: Funktionen
Name: Gleichungssysteme
Folge: 6
Bank: lineare-gleichungssysteme
Katalog: katalog/lineare-gleichungssysteme.md

Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,
didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die
Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py
und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026.

## Stufen

### Variablen deuten
- **Kern:** nein – 1 echte (2022)
- **Originale:** 2022-OS-K7a
- **Bank:** lineare-gleichungssysteme-e4-k1-s5 lineare-gleichungssysteme-e4-k5-s1 lineare-gleichungssysteme-e4-k1-s9[2022-OS-K7a]
- **Zuschnitt:** Gleichungssystem im Sachzusammenhang

### aufstellen
- **Kern:** ja – 3 echte (2016, 2021, 2024), Hauptleistung jeder Gleichungssystem-Aufgabe, Bank-Kette Sachaufgaben mit Grundfall
- **Originale:** 2024-OS-K7a 2021-OS-K7b 2016-OS-K6d
- **Bank:** lineare-gleichungssysteme-e4-k1-s1 lineare-gleichungssysteme-e4-k1-s2 lineare-gleichungssysteme-e4-k1-s3 lineare-gleichungssysteme-e4-k1-s4 lineare-gleichungssysteme-e4-k1-s7 lineare-gleichungssysteme-e4-k1-s9[2024-OS-K7a,2021-OS-K7b] lineare-gleichungssysteme-e1-k1-s13[2016-OS-K6d]
- **Zuschnitt:** Gleichungssystem im Sachzusammenhang

### lösen
- **Kern:** ja – 1 echte (2022), aber in 2016, 2021, 2024 als Nebenleistung (typ_neben lösen), Bank-Ketten Einsetzen und Addition mit Grundfall
- **Originale:** 2022-OS-K7b
- **Bank:** lineare-gleichungssysteme-e2-k1-s1(i) lineare-gleichungssysteme-e2-k1-s2(i) lineare-gleichungssysteme-e2-k1-s3(i) lineare-gleichungssysteme-e2-k1-s4(i) lineare-gleichungssysteme-e2-k1-s5(i) lineare-gleichungssysteme-e2-k1-s7(i) lineare-gleichungssysteme-e2-k1-s8(i) lineare-gleichungssysteme-e3-k1-s1(i) lineare-gleichungssysteme-e3-k1-s2(i) lineare-gleichungssysteme-e3-k1-s3(i) lineare-gleichungssysteme-e3-k1-s4(i) lineare-gleichungssysteme-e3-k1-s5(i) lineare-gleichungssysteme-e2-k1-s6 lineare-gleichungssysteme-e2-k1-s12
- **Zuschnitt:** Gleichungssystem im Sachzusammenhang

### Gleichung in Worte fassen und lösen
- **Kern:** nein – 1 echte (2024)
- **Originale:** 2024-OS-K7b
- **Bank:** lineare-gleichungssysteme-e4-k1-s6 lineare-gleichungssysteme-e4-k1-s9[2024-OS-K7b]
- **Zuschnitt:** Gleichungssystem im Sachzusammenhang

## Plätze der Originale

Jede Teilaufgabe 2014–2026 (OS, EBR, FOR, GYM) mit ihrem Hauptplatz (Stufe, deren Handgriff die
ganze Teilaufgabe ist), „ganz auch“ (die ganze Aufgabe ist dieser Handgriff, obwohl anders
etikettiert) und Zwischenschritt; Stufen anderer Kapitel mit „kapitel:“. Erzeugt daraus:
msa/handgriffe-p10.csv (werkzeuge/gliederung-sichten.py).

| id | Hauptplatz | Ganz auch | Zwischenschritt | Begründung |
|---|---|---|---|---|
| 2015-GYM-K3b | lösen |  | aufstellen | Hauptplatz nach typ „Lineares Gleichungssystem lösen“. Zwischenschritt aus typ_neben |
| 2016-OS-K6d | aufstellen |  | lösen | Hauptplatz nach typ „Lineares Gleichungssystem aufstellen“. Zwischenschritt aus typ_neben |
| 2021-OS-K7b | aufstellen |  | lösen | Hauptplatz nach typ „Lineares Gleichungssystem aufstellen“. Zwischenschritt aus typ_neben |
| 2022-OS-K7a | Variablen deuten |  |  | Hauptplatz nach typ „Gleichung im Sachzusammenhang deuten“ |
| 2022-OS-K7b | lösen |  |  | Hauptplatz nach typ „Lineares Gleichungssystem lösen“ |
| 2024-OS-K7a | aufstellen |  |  | Hauptplatz nach typ „Lineares Gleichungssystem aufstellen“ |
| 2024-OS-K7b | Gleichung in Worte fassen und lösen |  | lösen | Hauptplatz nach Zuordnung. Zwischenschritt aus typ_neben |
