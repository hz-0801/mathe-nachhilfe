# Eigener Wortlaut Prozent (P10) – Probe

Stand 2026-10-05. Datei: `msa/wortlaut-eigen-prozent.csv`
(id;teil;wortlaut;abbildung;punkte;fundstelle;anmerkung).
Nur eigener Wortlaut; die Originaltexte liegen nicht im Repo.

## Auswahl (31 Teilaufgaben + 3 Vorspann-Zeilen = 34 Zeilen)

1. Kapitel Prozent in `msa/skript-zuschnitt-p10.csv` (Spalte ids und
   neben), 11: 2022-OS-B1f, 2026-FOR-B1a, 2023-OS-K6a, 2023-OS-B1b,
   2025-OS-B1a, 2024-OS-B1e, 2022-OS-K4b, 2026-FOR-K3c, 2023-OS-K6b,
   2025-OS-K4b, 2023-OS-K5c (neben).
2. 2014–2021 aus `msa-katalog-basis.csv`/`-kontext.csv`, Kriterium:
   thema, typ, typ_neben oder stichwoerter enthält Prozentrechnung,
   Zinsrechnung, Prozentwert, Prozentsatz, Grundwert, Rabatt, Zins oder
   „prozentual“; 20: 2014-OS-B1a, B1e, K3a, K3b, K3c; 2015-OS-B1e, K2a,
   K2b, K7c; 2016-OS-K2c; 2017-OS-B1b, K2b; 2018-OS-K7a; 2019-OS-K5a,
   K5b; 2020-OS-B1a, K2d, K4c; 2021-OS-B1c, K5a.
   Nicht gewählt (nur „Prozent“/„Anteil umwandeln“ als Nebensache,
   Wahrscheinlichkeit, Diagramme): 2014-OS-B1i, 2014-OS-K6a,
   2016-OS-B1f, 2017-OS-K6a, 2018-OS-B1d, 2018-OS-K3c/K3d,
   2019-OS-K4c, 2021-OS-K5b.
   Grenzfälle drin, weil das Kriterium sie trifft: 2020-OS-K2d
   („ein Drittel mehr“), 2020-OS-K4c (Wachstum), 2021-OS-K5a
   (Prozent nur Teilleistung von 5 P).

Vorspann-Zeilen: 2014-OS-K3 (Sparbuch-Tabelle), 2015-OS-K2
(Eintrittspreise, Rabatt), 2023-OS-K6 (Weltbevölkerung).

## Prüfungen

- Kurzlösung: alle 31 Werte des Katalogs (kurzloesung,
  zwischenergebnis) mit den Zahlen des neuen Wortlauts nachgerechnet;
  alle stimmen (z. B. 12 : 83 ≈ 14,5 %, 54 · 1,03¹⁴ ≈ 81,7,
  Abfall 24,6 %).
- Wortgleiche Folgen (Skript nicht committet): Prosa ohne Zahlen und
  Formeln höchstens 9 Wörter in Folge (2016-OS-K2c „Berechnen Sie, um
  wie viel Prozent die Besucherzahl von …“). Mit Zahlen gezählt
  über 12 nur zwei Fälle, beide reine Daten/Terme: 2015-OS-K2a (die
  drei Rabatt-Terme, 27 Zeichenfolgen-Wörter) und 2026-FOR-K3c (Preis-
  tabelle Mo–So, 19). Das ist innermathematisch bzw. Zahlenmaterial.

## Abbildungen

8 Zeilen beschreiben eine Abbildung, die zum Lösen nötig ist:
2014-OS-K3 (Tabelle), 2015-OS-K7c (leerer Kreis), 2016-OS-K2c,
2020-OS-K2d, 2021-OS-K5a, 2022-OS-K4b (Säulendiagramme mit Werten),
2025-OS-K4b (Rampendreieck 170 cm/16 cm), 2015-OS-K2a (Ankreuztabelle).
Turmzeichnung 2015 und Dose 2023 sind für die Prozentteile nicht nötig.

## Wo eigener Wortlaut schwer war

- Ankreuzoptionen und Aussagen (2020-OS-B1a, 2019-OS-K5b,
  2023-OS-K6b, 2020-OS-K2d): Inhalt ist festgelegt, nur der Satzbau
  lässt sich drehen.
- Operator-Sätze („Berechnen Sie, um wie viel Prozent …“) sind
  formelhaft; Nähe bleibt bei 8–9 Wörtern.
- 2023-OS-B1b: Ein Zusatz „ein Viertel“ hätte die Aufgabe leichter
  gemacht; gestrichen.

## Entscheidungen

- Fundstelle für FOR: „P10 2026 FOR · 1a“, sonst „P10 <Jahr> · <Nr><Teil>“.
- Namen teils geändert (Tom → Lena, Tim → Mia), Gegenstände nicht.
- Vorspann nur, wenn mehrere gewählte Teilaufgaben ihn brauchen;
  sonst steht der nötige Kontext in der Teilaufgabe.
- punkte der Vorspann-Zeilen leer; Formeln als LaTeX wie im Korpus.

## Auffüllen Prozent (Auftrag 2026-10-05, Beschluss „schwach“ fest)

Ziel 12 Aufgaben je Kern-Stufe, 6 je übriger Stufe; gezählt: echte
Teilaufgaben + zugeordnete Bank-Aufgaben + Zusatz. Zuordnung in
`msa/zuordnung-prozent.csv` (Spalte anzahl_bank zählt Bank und Zusatz).

Zählweise: Eine Bank-Sprosse zählt zur Stufe, wenn sie denselben
Handgriff ohne Gerüst verlangt (kein Streifen, keine Vorform, kein
vorgegebener Teilschritt, keine „gemischt“-Sprosse). Innermathematische
Aufgaben zählen je Zeile; eine Sachaufgabe zählt nicht, wenn ihr Text
ohne Zahlen zu mindestens 70 % mit einer schon gezählten Aufgabe der
Stufe übereinstimmt (difflib; „nur andere Zahlen im selben Text“).

| Stufe | Kern | echt | Bank+Zusatz vorher | nachher | Ziel |
|---|---|---|---|---|---|
| Prozent und Anteil umwandeln | ja | 2 | 9 | 11 | 12 |
| Prozentwert | ja | 6 | 16 | 16 | 12 |
| Prozentsatz | ja | 3 | 18 | 18 | 12 |
| Grundwert | ja | 2 | 11 | 11 | 12 |
| Erhöhung und Veränderung in Prozent | ja | 8 | 20 | 20 | 12 |
| Aussagen prüfen | nein | 4 | 12 | 12 | 6 |
| Prozent aus einer berechneten Fläche | nein | 1 | 0 | 5 | 6 |
| Zinsen und Zinssatz | nein | 3 | 9 | 9 | 6 |
| Zinseszins und Guthabentabelle | nein | 2 | 9 | 9 | 6 |

Neu: 7 Aufgaben. Bank `prozentrechnung` e1-k1-s6 v4 (Struktur: Nenner
geht nicht in hundert auf) und v5 (Struktur: Richtung umgekehrt,
„jeder …“ aus Prozent); Zusatz `msa/prozent-zusatz.jsonl` 5 zur Stufe
Fläche ohne Bank-Sprosse (Kontext Kork/Quadratraster, Struktur
Begründen π/4, Darstellung Kreisring, Struktur rückwärts Prozentwert,
Kontext Holz mit Durchmesser und nicht eingehaltener Vorgabe). Feld
herkunft „eigene Aufgabe 2026-10-05 (Auffüllen Prozent); anders: …“ –
was anders ist, steht dort, weil merkmal nach bank.md je Sprosse
einheitlich sein muss (sonst Abweichung im Prüfskript).

Zwischenfragen: Spalte `zwischenfragen` in `msa/wortlaut-eigen-prozent.csv`
für alle 21 Teilaufgaben mit Katalogfeld zwischenergebnis, je Eintrag
eine Frage, Trenner „ ; “.

Gegenprobe: bank-pruef.py prozentrechnung 0 Abweichungen (Warnung neu:
e1-k1-s6 hat 5 statt 3 Zeilen), zinsrechnung unverändert 0; Zusatz im
Probeordner als eigener Eintrag 0 Abweichungen (ohne Mappe keine
Sperrprobe); sympy alle 7 Werte nachgerechnet; duplikate.py: keine
neue Aufgabe in Liste A oder B.
