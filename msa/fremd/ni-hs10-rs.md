# Fremdprüfungen ni-hs10-rs (Niedersachsen, Kl. 10)

Stand 06.10.2026. Gruppe: Niedersachsen Hauptschule Kl. 10 E-Kurs
(2022–2024), Hauptschule Kl. 10 G-Kurs (2022–2026), Realschule
(2022–2024) bzw. Sjg. 10 E-Kurs/RS gemeinsam (2025–2026). Marke „NI ’JJ“.
Regeln: `aufgabenbank/bau/pruefheft/beschluesse-2026-10-06b.md` (N1, N4).

## Gelesen

13 Aufgabendateien, je einmal (`quellen/quelle-fremd-ni-bw-ni-{rs,hs10e,hs10g}-JJJJ.txt`).
Lösungsdateien nur abschnittsweise per grep, für Werte, die nur in den
Abbildungen der Aufgabe stehen (Radius, Höhe, Prozentwert im Diagramm)
und für Kontrollwerte.

## Zählung Teilaufgaben

| | Zahl |
|---|---|
| Teilaufgaben in 13 Heften | 730 |
| wortgleich in einem anderen Heft der Gruppe (Hauptteil 1 ist in RS/HS E/HS G meist gleich) | 137 |
| eigenständig | 593 |
| aufgenommen (art=ganz) | 159 |
| nicht aufgenommen, Rechenauftrag, aber Maße nur in der Abbildung oder inhaltsgleich mit aufgenommener Variante (andere Zahl) | 173 |
| nicht aufgenommen, ohne P10-Stufe (Kopfrechnen, Einheiten, Runden, Zeichnen/Konstruieren, Spiegeln, Symmetrie, Muster/Terme, Würfelnetze, Begründen ohne Rechnung, Zuordnung proportional, Ankreuzen von Graphen u. ä.) | 261 |

Zusätzlich 12 herausgelöste Zeilen und 54 Erkennen-Sätze.

## Zeilen je Kapitel

| Kapitel | ganz | herausgelöst | erkennen |
|---|---|---|---|
| prozent | 25 | 6 | 21 |
| dreiecke | 12 | 0 | 10 |
| flaechen | 15 | 1 | 0 |
| koerper | 25 | 0 | 0 |
| lineare | 28 | 1 | 3 |
| quadratische | 15 | 1 | 0 |
| gleichungssysteme | 1 | 0 | 0 |
| wachstum | 10 | 0 | 7 |
| daten | 3 | 0 | 0 |
| wahrscheinlichkeit | 25 | 3 | 13 |
| zusammen | 159 | 12 | 54 |

## Prüfung

- CSV parst (17 Felder, 171 Zeilen; Erkennen 5 Felder, 54 Zeilen), keine id doppelt,
  jede stufe und jeder Handgriff steht wörtlich in einer `msa/zuordnung-*.csv`.
- Mit sympy geprüft: 171 von 171 Lösungen (Kontrolle gegen den amtlichen
  Erwartungshorizont, wo er lesbar war); 0 Abweichungen.

## Entscheidungen

- Maße, die nur in der Abbildung stehen, wurden aus dem amtlichen
  Erwartungshorizont erschlossen und in `bemerkung` vermerkt („erschlossen“),
  z. B. Hocker r = 60 cm (RS 2023 A2), Pyramide Spreewald a = 35 m, h = 13 m
  (HS E 2022 W1), Fahrschule 672 € + 68 €/h (RS 2023 A5). Wo das nicht
  eindeutig ging (Lenkdrachen, Strommast, Carport, Fliesen, Praline,
  Papierflieger, Spielhaus), keine Zeile.
- Wortgleiche Aufgaben in mehreren Heften: eine Zeile, Zweitfundstelle in
  `bemerkung` („auch …“). Inhaltsgleiche Varianten mit anderen Zahlen
  (z. B. HS G neben HS E) nur, wenn sie leichter sind oder eine andere
  Fragerichtung haben.
- Zeichnen-Anteile (Säule, Balken, Graph einzeichnen) aus Rechenaufgaben
  weggelassen; reine Zeichenaufgaben nur bei passender Stufe
  („aus Gleichung zeichnen“, „Punkte darstellen“, „Parabel skizzieren“).
- Sinngemäß zugeordnet: Radius aus Kreisumfang → flaechen „rückwärts: Seite
  aus Fläche“; Punktprobe an einer Geraden → lineare „rechnerisch an Gerade
  und Parabel“; Steigung in % → Winkel → dreiecke „Winkel berechnen“;
  Mantelfläche ohne Kosten → koerper „Mantelfläche mit Kosten“.
- Fachwörter: „Funktionsgleichung“, „Körperhöhe hK“ und „Baumdiagramm“
  bleiben (in BB üblich); „Urne“, „Wertepaare“ nur wo nötig.
- Erkennen: linear/exponentiell-Sätze stehen bei der Stufe ihres
  Hauptplatzes (lineare bzw. wachstum); mit/ohne Zurücklegen auch
  Glücksrad-/Elfmeter-Sätze als „mit Zurücklegen“.

## Unsicher

- NI-HS10E-2023-W2c: Starttemperatur 80 °C nicht im Text, erschlossen aus
  den amtlichen Ablesewerten (12:45 Uhr ≈ 72 °C; um 15:30 Uhr 35 °C
  gefallen) – passt, ist aber nicht belegt.
- NI-RS-2023-A5a/b: Kostenaufbau der Fahrschule aus y = 68x + 672
  erschlossen; im Original stehen evtl. mehrere Posten (Grundgebühr,
  Prüfungen).
- NI-RS-2024-A5c: α als ganzer Öffnungswinkel gedeutet (amtlich 18,06°
  bei hK = 75,51 cm passt nur so).
- NI-RS-2023-A2c: Auswahlterme teils eigen, weil die Brüche im Quelltext
  verloren sind.
- NI-HS10G-2025-A4b: amtliche Lösung nicht lesbar, nur eigene Rechnung
  (≈ 336 Kugeln).
