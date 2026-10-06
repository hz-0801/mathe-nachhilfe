# Eigener Wortlaut Kurvenuntersuchung (Abitur GK) – Probe

Stand 2026-10-06 (Lauf B1). Datei:
`abitur/wortlaut-eigen-kurvenuntersuchung.csv`, Trenner `;`, UTF-8.
Nur eigener Wortlaut, gebaut aus den Katalogfeldern von
`abitur/abi-katalog.csv` (gegeben, gesucht, operator, skizze, kontext,
punkte, abhaengig_von, kurzloesung, zwischenergebnis); die Hefte lagen
nicht vor.

## Felder

| Feld | Inhalt |
|---|---|
| id | Katalog-id; Vorspann: Aufgaben-id ohne Buchstaben (bei zwei Aufgabenteilen `-T1`/`-T2`) |
| teil | Buchstabe oder `vorspann` |
| wortlaut | Aufgabentext in Du-Form, Formeln als LaTeX |
| abbildung | Typ am Anfang (Graph, Skizze, Diagramm), dann Beschreibung nach Katalog-Feld skizze; „Graph aus dem Vorspann“ verweist |
| punkte | BE aus dem Katalog; Vorspann leer |
| fundstelle | „Abi GK <Jahr> · <Block><Nr> <Teil>“ |
| platz | haupt (Spalte ids im Zuschnitt) oder haupt+neben |
| stufe | Abschnitt – Stufe aus `skript-zuschnitt-abi-gk.csv` |
| sicher | ja / nein (Katalogfelder reichen nicht für eine eindeutige Aufgabe) |
| anmerkung | Abweichungen, übernommene Zwischenergebnisse |
| zwischenfragen | Hilfsfragen aus zwischenergebnis, Trenner „ ; “ |

## Auswahl (84 Zeilen = 68 Teilaufgaben + 16 Vorspann)

Kapitel Kurvenuntersuchung im Zuschnitt: 68 ids als Hauptplatz, 2 als
Nebenplatz (2022-B2.1a, 2024-B2.1g); beide Nebenplätze sind zugleich
Hauptplätze einer anderen Stufe, also 68 verschiedene Teilaufgaben.
Vorspann je Aufgabe, wenn zwei oder mehr gewählte Teilaufgaben
dieselbe Funktion oder denselben Sachkontext brauchen; sonst steht
alles in der Teilaufgabe.

10 Teilaufgaben brauchen ein Ergebnis einer früheren Teilaufgabe; das
steht als „Gegeben: …“ im Wortlaut (Anmerkung nennt es): 2022-B2.1c,
B2.1k; 2023-B2.1d, B2.1e, B2.2e; 2024-A1.4b, B2.1h, B2.2b, B2.2h;
2026-B2.1e (Gerade t aus 2.1d).

## sicher = nein (8 Zeilen, davon 6 Teilaufgaben)

- 2022-A1.2 (Vorspann, a, b): Graph ohne Term, Werte nur „etwa“;
  Wendestellen nur aus der Beschreibung erschließbar.
- 2023-B2.2h: Ablesewert aus einem nur beschriebenen Diagramm.
- 2023-B2.1k: siehe Befund 1 (Satz ergänzt; bleibt markiert, weil die
  Ergänzung nicht aus dem Katalog stammt).
- 2025-B2.2 Aufgabenteil 2 (Vorspann, e, g): Term von a(x) nicht im
  Katalog; grafische Lösung hängt an der Zeichnung.

## Prüfung

sympy hat alle 68 Teilaufgaben mit den Zahlen des neuen Wortlauts
nachgerechnet (Skript im Scratchpad, nicht committet, weil es keine
Datei baut); alle Ergebnisse stimmen mit kurzloesung überein, auch die
Rundungen (z. B. f(−1 + √5) ≈ −4,25; W1(−4,45 | 0,09); 1040,6 m;
114,4 g; 18,4 m / 5,25 min). Bei 2022-A1.2, 2023-B2.2h und 2025-B2.2e/g
gibt es nichts zu rechnen (Ablesen, Deuten). CSV parst mit 11 Feldern
je Zeile.

## Befunde

1. 2023-B2.1k (Karton): Die vier Spitzen bilden ein Quadrat mit der
   Seite 2·√2 LE ≈ 42,4 cm; die Ränder sind nach innen gewölbt. Ein
   um 45° gedrehter Karton mit dieser Grundfläche reicht also
   (42,4² · 50 cm³ = 90 l). Die Kurzlösung 180 l (60 cm × 60 cm × 50 cm)
   gilt nur für Kanten parallel zu den Achsen.
   Im Wortlaut ergänzt: „Die Kanten der Grundfläche verlaufen parallel
   zu den Koordinatenachsen.“ Ob das Heft das so sagt, ist offen.
2. 2023-B2.2k: Bedingung III „H(5 | 220) ist Hochpunkt“ ist mit
   k(0) = 20, k′(0) = 130 nicht erfüllbar; die Lösung
   k(x) = 2x³ − 28x² + 130x + 20 hat bei 5 einen Tiefpunkt
   (k″(5) = 4 > 0, schon im Katalog vermerkt). Im Wortlaut steht
   „waagerechte Tangente in (5 | 220)“; damit ist die Aufgabe
   eindeutig und richtig (sicher = ja).
3. 2022-B2.2k: Der Katalog sagt nicht, wie der Rand bei (5 | 5)
   weitergeht; für die Teilaufgabe nötig sind nur k(2) = 1,
   k′(2) = 1,5 und k′(0) = 0 („waagerecht im Ursprung“, aus der
   Kurzlösung erschlossen).
4. 2023-B2.1i: Welche der Funktionen g, h, k zu welchem Quadranten
   gehört, legt der Katalog nicht fest; im Wortlaut werden keine
   Buchstaben vergeben, der Schüler nennt den Quadranten.
5. 2022-B2.1c: Katalog-Skizze nennt den Tiefpunkt von f′ „rechts der
   y-Achse“; nachgerechnet liegt er bei (0 | −1) (f″(x) = x·e^(−x)).
   In der Abbildungsbeschreibung berichtigt.

## Entscheidungen

- Operatoren in Du-Form nach dem Katalog (Berechne, Bestimme, Gib an,
  Weise nach, Zeige, Begründe, Ermittle, Beschreibe, Beurteile,
  Untersuche, Entscheide, Skizziere, Markiere, Deute).
- Funktionsterme und Bereiche wörtlich aus gegeben; Sachtexte neu
  formuliert, Zahlen unverändert.
- Abbildungen, die zum Lösen nicht nötig sind, tragen den Vermerk
  „zum Lösen nicht nötig“ (2022-B2.2g, 2025-A1.4a, 2026-B2.2).
