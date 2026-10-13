# Gliederung Gleichungssysteme (P10)

Prüfung: msa
Kapitel: gleichungssysteme
Gebiet: Funktionen
Name: Gleichungssysteme
Folge: 6
Bank: lineare-gleichungssysteme
Katalog: katalog/lineare-gleichungssysteme.md
Kennung: Gleichungssystem im Sachzusammenhang = 93F

Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,
didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die
Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py
und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026.

## Stufen

Drei Stufen (Runde 13.10. Schritt B, pruefung.md § 5 „Stufen heißen nach dem Gesuchten“):
Gleichungen aufstellen · x und y gesucht · Bedeutung gesucht. Folge wie in der Prüfung: erst aus
dem Text die Gleichungen, dann lösen, dann deuten. „Variablen deuten“ (2022-OS-K7a) und „Gleichung in
Worte fassen und lösen“ (2024-OS-K7b) sind eine Stufe: beide fragen zuerst, was eine Variable oder
Gleichung in der Sache bedeutet (eigener erster Schritt; je ein Original wäre keine Stufe). Die Stufe
steht zuletzt, weil ’24 · 7b danach noch lösen lässt und die schwerste Aufgabe ist (4 BE).
Blatt = alle Originale 2022–2026 (4); ältere (2021-OS-K7b, 2016-OS-K6d) im Mehr-Block. Keine zwei
Originale unterscheiden sich nur in den Zahlen; kein Bündel. Einziger Anstoß: vor „x und y gesucht“
der erste Schritt des Einsetzens (umstellen, einsetzen mit Klammer) an einem einfacheren System ohne
die Zahlen der Prüfung.

Häufigkeit (pruefung.md § 5, Lehrer 13.10.; P10-Hefte 2014–2026 ohne GYM): Gleichungssysteme kamen
2016, 2021, 2022 und 2024 – keine Zeile „Häufigkeit“; der Setzer druckt die Jahre.

### aufstellen
- **Anzeigename:** Gleichungen aufstellen
- **Kern:** ja – 3 echte (2016, 2021, 2024), Hauptleistung jeder Gleichungssystem-Aufgabe, Bank-Kette Sachaufgaben mit Grundfall
- **Originale:** 2024-OS-K7a 2021-OS-K7b 2016-OS-K6d
- **Bank:** lineare-gleichungssysteme-e4-k1-s1 lineare-gleichungssysteme-e4-k1-s2 lineare-gleichungssysteme-e4-k1-s3 lineare-gleichungssysteme-e4-k1-s4 lineare-gleichungssysteme-e4-k1-s7 lineare-gleichungssysteme-e4-k1-s9[2024-OS-K7a,2021-OS-K7b] lineare-gleichungssysteme-e1-k1-s13[2016-OS-K6d]
- **Zuschnitt:** Gleichungssystem im Sachzusammenhang

### lösen
- **Anzeigename:** x und y gesucht
- **Regine:** S. 20 · 21
- **Schülerfrage:** Beim Einsetzen stellst du eine Gleichung um und setzt sie in die andere ein. Fang so an:
- **Schülerfrage-Fälle:** Stelle x + y = 10 nach y um → y = 10 − x | Setze y = 10 − x in 3x + 2y = 24 ein → 3x + 2 · (10 − x) = 24
- **Schülerfrage-Form:** linie
- **Schülerfrage-Weg:** a) x auf die andere Seite: y = 10 − x; b) statt y die ganze Klammer (10 − x); ausgerechnet x = 4, y = 6
- **Kern:** ja – 1 echte (2022), aber in 2016, 2021, 2024 als Nebenleistung (typ_neben lösen), Bank-Ketten Einsetzen und Addition mit Grundfall
- **Originale:** 2022-OS-K7b
- **Bank:** lineare-gleichungssysteme-e2-k1-s1(i) lineare-gleichungssysteme-e2-k1-s2(i) lineare-gleichungssysteme-e2-k1-s3(i) lineare-gleichungssysteme-e2-k1-s4(i) lineare-gleichungssysteme-e2-k1-s5(i) lineare-gleichungssysteme-e2-k1-s7(i) lineare-gleichungssysteme-e2-k1-s8(i) lineare-gleichungssysteme-e3-k1-s1(i) lineare-gleichungssysteme-e3-k1-s2(i) lineare-gleichungssysteme-e3-k1-s3(i) lineare-gleichungssysteme-e3-k1-s4(i) lineare-gleichungssysteme-e3-k1-s5(i) lineare-gleichungssysteme-e2-k1-s6 lineare-gleichungssysteme-e2-k1-s12
- **Zuschnitt:** Gleichungssystem im Sachzusammenhang

### deuten
- **Anzeigename:** Bedeutung gesucht
- **Kern:** nein – 2 echte (2022, 2024): was x, y oder eine Gleichung in der Sache bedeutet; 2024 danach lösen
- **Originale:** 2022-OS-K7a 2024-OS-K7b
- **Bank:** lineare-gleichungssysteme-e4-k1-s5 lineare-gleichungssysteme-e4-k5-s1 lineare-gleichungssysteme-e4-k1-s6 lineare-gleichungssysteme-e4-k1-s9[2022-OS-K7a,2024-OS-K7b]
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
| 2022-OS-K7a | deuten |  |  | Hauptplatz nach typ „Gleichung im Sachzusammenhang deuten“ |
| 2022-OS-K7b | lösen |  |  | Hauptplatz nach typ „Lineares Gleichungssystem lösen“ |
| 2024-OS-K7a | aufstellen |  |  | Hauptplatz nach typ „Lineares Gleichungssystem aufstellen“ |
| 2024-OS-K7b | deuten |  | lösen | Hauptplatz nach typ „Gleichung im Sachzusammenhang deuten“ (beginnt mit dem Satz zu Gleichung II). Zwischenschritt aus typ_neben |
