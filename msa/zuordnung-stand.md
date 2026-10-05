# Stand: Zuordnung P10-Kapitel ↔ Aufgabenbank und Auffüllen

Auftrag 2026-10-05 (Muster Prozent). Skript `werkzeuge/zuordnung.py
KAPITEL` (Prozent-Ausgabe byteidentisch mit
`werkzeuge/prozent-zuordnung.py`). Je Kapitel: `msa/zuordnung-<kapitel>.csv`,
Zusatz ohne Bank-Sprosse in `msa/<kapitel>-zusatz.jsonl`.
Grenze des Laufs: 400 neue Aufgaben. Ein Neustart macht beim ersten
Kapitel ohne „fertig“ weiter. Lauf abgeschlossen 2026-10-05: alle neun
Kapitel fertig, 4 neue Aufgaben (Grenze 400 nicht berührt).

| Kapitel | Stand | Stufen (Kern) | fehlen vorher | fehlen nachher | neu | Commit Bank | Commit hier |
|---|---|---|--:|--:|--:|---|---|
| Lineare | fertig | 10 (5) | 1 | 0 | 1 | 05d8c03 | 89203e4 |
| Quadratische | fertig | 10 (4) | 0 | 0 | 0 | – | 77cb4cc |
| Dreiecke | fertig | 13 (9) | 0 | 0 | 0 | – | 548de90 |
| Daten | fertig | 10 (5) | 0 | 0 | 0 | – | cb0a4ac |
| Wahrscheinlichk. | fertig | 7 (5) | 1 | 0 | 1 | d2f673d | 38ceb45 |
| Körper | fertig | 8 (2) | 0 | 0 | 0 | – | 67fa104 |
| Flächen | fertig | 5 (4) | 2 | 0 | 2 | e2035eb | eae258a |
| Wachstum | fertig | 4 (3) | 0 | 0 | 0 | – | 73bfbf8 |
| Gleichungssysteme | fertig | 4 (2) | 0 | 0 | 0 | – | 392cc47 |

Summe neu bisher: 4.

## Notizen je Kapitel

- Lineare: neu 1 (Darstellung: Ankreuzen unter drei Punkten,
  lineare-funktionen e3-k2-s5-v4). Innermathematische Sprossen mit
  Zahlen in Term oder Grafik als „(i)“ markiert (jede Zeile zählt);
  e2-k4-s4 nicht gezählt (Teilschritte vorgegeben). 2021-OS-K6b
  (Wertetabelle als Punkte) keiner Stufe zugeordnet.
- Quadratische: alle Stufen schon voll, keine neue Aufgabe. Verschieben,
  Spiegeln, Parabel zu Eigenschaften (2015–2020) zur Stufe
  Scheitelpunktform angeben; 2015-OS-K4b (Gleichung zu Graph) zu
  Wertetabelle zuordnen; 2014-OS-K7b (Gerade ohne gemeinsamen Punkt) zu
  Lage zweier Parabeln; 2021-OS-K7c (Lösbarkeit) keiner Stufe.
- Dreiecke: alle Stufen schon voll, keine neue Aufgabe. Zweite Stufe
  „Seite berechnen“ (Sinussatz) heißt hier „Seite berechnen (Sinussatz)“.
  Keiner Stufe zugeordnet (kein Zuschnitt-Handgriff): Winkel an
  Parallelen, Scheitel- und Nebenwinkel (2014-OS-B1f, 2015-OS-B1d,
  2019-OS-B1a, 2020-OS-B1g), Teilwinkel (2016-OS-K7a, 2018-OS-K4a),
  Dreiecksungleichung (2020-OS-B1i), Figur nach Spiegelung (2018-OS-B1h).
- Daten: alle Stufen schon voll, keine neue Aufgabe. Keiner Stufe
  zugeordnet: Wert ablesen und Werte nach Bedingung (2016-OS-K2a/b,
  2020-OS-K2b), relative Häufigkeit (2015-OS-K7b).
- Wahrscheinlichk.: neu 1 (Kontext und Struktur: Freiwurf mit
  Trefferwahrscheinlichkeit 0,7, wahrscheinlichkeit e3-k3-s6-v4) für
  Gegenereignis. Nur Eintrag wahrscheinlichkeit (Sek I);
  zufallsexperimente-und-pfadregeln ist Sek II. Keiner Stufe zugeordnet:
  Anzahl der Anordnungen und Ziffern (2015-OS-K5a, 2016-OS-K5a/b,
  2017-OS-K6b).
- Körper: alle Stufen schon voll, keine neue Aufgabe. Keiner Stufe
  zugeordnet: Kantenzahl (2019-OS-B1f), Packungsanzahl (2020-OS-K5c),
  Term zu Körper (2017-OS-K3c); 2019-OS-K4c (Dreiecksfläche als
  Grundfläche) unter Flächen.
- Flächen: neu 2 für Anteil in Prozent (Verschnitt) in flaechen
  e5-k3-s1 (v4 Kontext Glas, Struktur Trapez; v5 Kontext Fotopapier,
  Struktur Rand). Die 5 Zusatzaufgaben aus msa/prozent-zusatz.jsonl
  (dieselbe Stufe unter Prozent) zählen hier nicht mit. 19-OS-K4b
  (Mantelfläche Prisma) keiner Stufe zugeordnet.
- Wachstum: alle Stufen schon voll, keine neue Aufgabe. Funktionswert
  aus der Gleichung (2016-OS-K4e, 2017-OS-K7d, 2020-OS-K4c) zur Stufe
  Faktor bestimmen, Gleichung aufstellen; 2021-OS-K6b (linear,
  Wertetabelle als Punkte) zu Punkte darstellen. Keiner Stufe
  zugeordnet: Wachstumsart begründen (2016-OS-K4d, 2018-OS-K2b),
  Schwellenwert (2018-OS-K2c), Verdopplungszeit (2016-OS-K4c,
  2020-OS-K4b).
- Gleichungssysteme: alle Stufen schon voll, keine neue Aufgabe. Stufe
  lösen trotz einer echten als Kern (Nebenleistung 2016, 2021, 2024).

## Entscheidungen und Befunde des Laufs

- Spaltenfolge wie `msa/zuordnung-prozent.csv` (kern_grund am Ende),
  damit die Prozent-Ausgabe byteidentisch bleibt.
- Echte Teilaufgaben: Zuschnitt 2022–2026 (ids und neben) plus
  Katalogzeilen 2014–2021 (basis, kontext), deren typ denselben
  Handgriff nennt; typ_neben nur, wenn keine Stufe den typ trägt.
- Kern: mindestens zwei echte und eine Bank-Kette mit Grundfall für den
  Handgriff, oder Basisteil fast jedes Jahr (Begründung je Zeile).
- Innermathematisch: Die Prozent-Regel (Text ohne Zahlen unter 40
  Zeichen) hält Aufgaben mit Zahlen in Grafik oder Term („Lies n ab“,
  „Zeichne f(x) = …“, „Ein Zylinder hat r = … und h = …“) für eine
  Sachaufgabe und zählt alle Varianten einmal. Solche Sprossen sind in
  den Daten als innermathematisch markiert („(i)“), jede Zeile zählt.
- Die Bank trägt fast alle Stufen schon über das Ziel; der Engpass sind
  Stufen mit genau einer Sprosse (Punkt ankreuzen, Gegenereignis,
  Verschnitt). Die Zuordnung ist großzügig (Sprossen desselben
  Handgriffs aus mehreren Ketten); wer strenger zählt, findet eher
  Lücken bei Stufen mit einer Sprosse.
- bank-pruef.py: keine neue Abweichung; je neu gefüllter Sprosse die
  Mengenwarnung (4 oder 5 statt 3 Zeilen), wie bei Prozent. Vorher schon
  2 Abweichungen in lineare-funktionen (Sperre f(x) = 3x − 7 gegen
  2014-GYM-B1i, e2-k7-s2-v1 und e4-k4-s2-v1), nicht angefasst.
- stand.md der Bank-Einträge nicht fortgeschrieben (außerhalb des
  Schreibbereichs); die Zeilen tragen herkunft.
