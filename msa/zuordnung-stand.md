# Stand: Zuordnung P10-Kapitel ↔ Aufgabenbank und Auffüllen

Auftrag 2026-10-05 (Muster Prozent). Skript `werkzeuge/zuordnung.py
KAPITEL` (Prozent-Ausgabe byteidentisch mit
`werkzeuge/prozent-zuordnung.py`). Je Kapitel: `msa/zuordnung-<kapitel>.csv`,
Zusatz ohne Bank-Sprosse in `msa/<kapitel>-zusatz.jsonl`.
Grenze des Laufs: 400 neue Aufgaben. Ein Neustart macht beim ersten
Kapitel ohne „fertig“ weiter.

| Kapitel | Stand | Stufen (Kern) | fehlen vorher | fehlen nachher | neu | Commit Bank | Commit hier |
|---|---|---|--:|--:|--:|---|---|
| Lineare | fertig | 10 (5) | 1 | 0 | 1 | 05d8c03 | siehe git log |
| Quadratische | fertig | 10 (4) | 0 | 0 | 0 | – | siehe git log |
| Dreiecke | fertig | 13 (9) | 0 | 0 | 0 | – | siehe git log |
| Daten | fertig | 10 (5) | 0 | 0 | 0 | – | siehe git log |
| Wahrscheinlichk. | fertig | 7 (5) | 1 | 0 | 1 | d2f673d | siehe git log |
| Körper | fertig | 8 (2) | 0 | 0 | 0 | – | siehe git log |
| Flächen | offen | | | | | | |
| Wachstum | offen | | | | | | |
| Gleichungssysteme | offen | | | | | | |

Summe neu bisher: 2.

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
