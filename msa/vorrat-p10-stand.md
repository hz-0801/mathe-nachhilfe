# Vorrat P10 2022–2026 – Stand

Beitabelle: `archiv/vorrat-p10-2022-2026-2026-10-05.csv` (bis 05.10.2026
`msa/vorrat-p10-2022-2026.csv`); am 05.10.2026 über `msa-bau.py --korrektur`
in die Katalogfelder kurzloesung, zwischenergebnis, stichwoerter, neben,
abhaengig_von übernommen (`msa/uebernahme-stand.md`).

Beginn: 2026-10-04 14:30 UTC. Teilstücke: 4 à 37 Zeilen (146 Zeilen, basis dann kontext).

- Teilstück 1/4: 37 Zeilen (2025-OS-B1a … 2023-OS-B1i), gebaut 14:32 UTC; sympy ok 28, nicht rechenbar 9.
- Teilstück 2/4: 37 Zeilen (2022-OS-B1a … 2026-FOR-K3e), gebaut 14:34 UTC; sympy ok 31, nicht rechenbar 6. Festlegung: kein Semikolon in Feldern (CSV-Trenner); mehrere Teilantworten in kurz durch „ | “, Begründungen mit Komma statt Semikolon.
- Teilstück 3/4: 37 Zeilen (2026-FOR-K4a … 2023-OS-K2c), gebaut 14:36 UTC; sympy ok 33, nicht rechenbar 4.
- Teilstück 4/4: 35 Zeilen (2023-OS-K3a … 2022-OS-K7b), gebaut 14:38 UTC; sympy ok 33, nicht rechenbar 2.

## Bericht (Agent, Fable 5.1, 2026-10-04 14:38 UTC)

- Zeilen gesamt: 146 (OS 2022–2025: 113, FOR 2026: 33), davon sympy ok 125, abw 0, nicht rechenbar 21, offen 0.
- Gegenprobe (bemerkung enthält „amtlich“ oder „sympy“): Soll 0, Ist 0 – keine Zeile der 146 trägt eines der Wörter; die Gegenprobe läuft deshalb ins Leere. Ersatz: alle 125 rechnerischen Ergebnisse sind mit dem Katalogwert verglichen, keine Abweichung.
- Abweichungen: keine. Katalogwerte, Zwischenwerte und Rundungen stimmen überall (Toleranz ±0,05 in der letzten Heftstelle, bei Geldbeträgen ±0,005 €).
- abhaengig_von: 6 vorhandene Werte übernommen (2026-FOR-K4c, 2026-FOR-K6c, 2023-OS-K7b, 2022-OS-K5c, 2022-OS-K5e, 2022-OS-K7b), 0 ergänzt. Grenzfälle, bewusst nicht ergänzt: 2026-FOR-K4b, 2024-OS-K6b (über cos unabhängig von a), 2024-OS-K2c, 2026-FOR-K3e (nur Deutung, keine Rechenabhängigkeit). Zwei übernommene Werte sind keine echte Rechenabhängigkeit (2022-OS-K7b ← K7a: Bedeutung der Variablen; 2022-OS-K5e ← K5d: DB kommt über tan, nicht über a) – übernommen, weil der Auftrag „vorhandene Werte übernehmen“ sagt; Entscheidung im Chat.
- typ_neben leer, aber Nebenthema nötig: 43 Zeilen (von 81 Zeilen mit Nebenthema). Häufigste Fälle: Prozentrechnung in Anteils- und Diagrammaufgaben, Koordinaten und Zeichnen bei Zeichenaufträgen, Rationale Zahlen rechnen bei Punktproben mit negativen Zahlen, Quadratische Gleichungen bei Schnittpunkt- und Nullstellenaufgaben.
- Prüfung: werkzeuge/vorrat-pruef.py (nimmt nur einen Katalog; beide Kataloge im Scratchpad zu einer Datei zusammengefügt) – „Prüfung bestanden: 146 Zeilen.“ Zusätzlich im Bau-Skript: jede id genau einmal in Katalogreihenfolge, kurz nie leer, neben nur gültige Themen, abh nur gültige ids, kein Semikolon in Feldern.
- Festlegungen: (1) Kein Semikolon in Feldern (CSV-Trenner); Teilantworten in kurz durch „ | “ wie im Katalogfeld ergebnis, Begründungen mit Komma („wahr, …“, „falsch, …“). (2) Ankreuz- und Zuordnungsaufgaben mit Rechenkern (120° : 360° = 1/3, Wertetabelle zu y = 3x²) sind nachgerechnet und tragen „ok“; nur reine Erkennungs-, Zeichen- und Begründungsaufgaben tragen „nicht rechenbar“. (3) Bei Zeichenaufgaben ohne Zwischenwert steht in zwischen der Konstruktionsgedanke (Steigungsdreieck, Skala). (4) Sympy-Skript: eine Funktion je rechnerischer Teilaufgabe, Toleranzen in der Funktion.
- Beispielzeilen (wörtlich):
  2024-OS-K6a;FA ≈ 287,1 m;FA² = 384² − 255² = 82 431;Satz des Pythagoras|Kathete|Höhenunterschied;;;ok
  2023-OS-K3b;Angebot 1: 178,20 € | Angebot 2: 162,30 € | Angebot 2 günstiger | K(x) = 0,09x + 120;120 Mehrkilometer · 0,36 € = 43,20 € | 5 · 27 = 135 €;Gesamtkosten|Tarifvergleich|Freikilometer|lineare Funktion|Funktionsgleichung aufstellen;Rationale Zahlen rechnen;;ok
  2023-OS-K7a;Winkel bei A und B im Dreieck ABF je 45° ⇒ gleichschenklig mit Basis AB (BF = AF);Winkelsumme: 180° − 90° − 45° = 45°;gleichschenkliges Dreieck|Basiswinkel|rechter Winkel|Winkelsumme|Begründen;;;ok
- Gelesen: vier Teilstücke (74 KB, ≈ 30 000 Token) je einmal; Gesamtverbrauch der Sitzung ≈ 200 000 Token.
- Letzter Commit: siehe git log (Teilstück 4/4).
