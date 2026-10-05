# Vorrat Abitur GK 2022–2026 – Standdatei

Auftrag: Vorratslauf Block 1 (Agent 04.10.2026). Beitabelle
`abitur/vorrat-abi-gk-2022-2026.csv` (id;kurz;zwischen;stich;neben;abh;sympy;
seit 05.10.2026 in `archiv/vorrat-abi-gk-2022-2026-2026-10-05.csv`, nach der
Übernahme in `abitur/abi-katalog.csv` über `abitur/vorrat-uebernahme.py`,
Stand in `abitur/uebernahme-stand.md`),
246 Teilaufgaben in 7 Teilstücken (6 × 36, 1 × 30), Katalogreihenfolge.
Ein Neustart beginnt beim ersten Teilstück, das unten nicht als „fertig“ steht.

## Stand

- Start: 2026-10-04T14:30Z
- Teilstück 1/7 fertig: 36 Zeilen, 2026-10-04T14:34Z
- Teilstück 2/7 fertig: 36 Zeilen, 2026-10-04T14:36Z
- Teilstück 3/7 fertig: 36 Zeilen, 2026-10-04T14:39Z
- Teilstück 4/7 fertig: 36 Zeilen, 2026-10-04T14:41Z
- Teilstück 5/7 fertig: 36 Zeilen, 2026-10-04T14:43Z
- Teilstück 6/7 fertig: 36 Zeilen, 2026-10-04T14:45Z
- Teilstück 7/7 fertig: 30 Zeilen, 2026-10-04T14:48Z

Alle sieben Teilstücke fertig; `python3 werkzeuge/vorrat-pruef.py archiv/vorrat-abi-gk-2022-2026-2026-10-05.csv abitur/abi-katalog.csv` meldet „Prüfung bestanden: 246 Zeilen.“

## Bericht (Agent 04.10.2026, Fable 5.1)

- Zeilen gesamt: 246; sympy ok 221, abw 2, nicht rechenbar 23, offen 0.
- Gegenprobe (bemerkung enthält „mit sympy bestätigt“ oder „(amtlich)“): Soll 127, Ist 127 ok. „(amtlich)“ kommt in den 246 Zeilen nicht vor (Poolzeilen im abi-Katalog tragen „Ergebnis aus der Poolzeile übernommen“), alle 127 sind „mit sympy bestätigt“.
- Abweichungen (beide im Feld `zwischenergebnis`, das Ergebnis der Zeile stimmt jeweils):
  - 2025-bebb-gk-B4c: Katalog „P(X = 90) ≈ 0,0428“; sympy 0,0432 (B(1000; 0,0918)); P(X = 92) ≈ 0,0436 und E(X) = 91,8 stimmen.
  - 2026-bb-gk-B3c: Katalog „t = 7/26“; sympy t = 7/13 (DP · CS = −14 + 26t = 0); die Deutung „P ist Lotfußpunkt von D auf CS“ ist unberührt.
- abhaengig_von: 53 Katalogzeilen hatten einen Wert, alle übernommen; bei 11 Zeilen ergänzt (2023-bebb-gk-B4.2c ← B4.2a; 2024-bebb-gk-B3f ← B3d; 2022-bebb-gk-A1.2b ← A1.2a; 2022-bebb-gk-B4h ← B4g; 2025-bebb-gk-A1.5b ← A1.5a; 2025-bebb-gk-B4e ← B4a; 2026-bb-gk-B2.1e ← B2.1d; 2026-bb-gk-A1.3b ← A1.3a; 2026-bb-gk-B3e ← B3d; 2026-bb-gk-B4e ← B4d; 2026-bb-gk-B4f ← B4e). Beitabelle: 64 Zeilen mit abh.
- typ_neben leer, aber Nebenthema nötig: 198 von 232 Zeilen ohne typ_neben haben in der Beitabelle ein Nebenthema (211 Zeilen mit neben insgesamt). Das Feld `neben` zählt jede mitbenutzte Fertigkeit (Ableitungsregeln, Gleichungen lösen, Vektoren und Rechenoperationen), `typ_neben` nur eine zweite bepunktete Leistung – die beiden Felder messen Verschiedenes.
- Beispielzeilen (wörtlich aus der Beitabelle):
  - Rechentyp: `2023-bebb-gk-B2.1f;W1(−4,45 | 0,09), W2(0,45 | −2,98);f''(x) = (0,5x² + 2x − 1) · e^x|x = −2 ± √6;Wendepunkt|zweite Ableitung|Produktregel|quadratische Gleichung;Ableitungsregeln|Gleichungen lösen;;ok`
  - Begründen: `2023-bebb-gk-B2.2f;"genau eine Nullstelle von g' (x = 5) ⇒ genau eine waagerechte Tangente; g' ≥ 0 ohne Vorzeichenwechsel ⇒ kein Extrempunkt (Sattelpunkt)";g'(x) = 1,2(x − 5)²;Ableitungsgraph|Sattelpunkt|Berührnullstelle|Vorzeichenwechsel|waagerechte Tangente;Kurvenuntersuchung;;ok`
  - Sachzusammenhang: `2023-bebb-gk-B2.2i;"195; mittlere Temperatur in der Startphase (0 bis 5 min) ist 195 °C";∫ von 0 bis 5 h(x) dx = 975;Mittelwert einer Funktion|Integral|Stammfunktion|Sachzusammenhang;Stammfunktion und Hauptsatz;;ok`
- Eigene Entscheidungen: (1) `sympy` = „nicht rechenbar“ bei Ablesewerten aus Abbildungen, Skizzen, Termdeutungen und Baumdiagrammen; Näherungswerte mit Toleranzangabe im Katalog (A1.2a 2023, A1.7a 2023) gelten als „ok“, wenn der sympy-Wert in der angegebenen Spanne liegt. (2) Wo das Ergebnis eine Begründung ist, prüft sympy die tragenden Zahlen (Vorzeichen, Nullstellen, Skalarprodukte) und meldet „ok“. (3) `abh` nur bei echter Rechenabhängigkeit ergänzt; vorhandene Werte unverändert übernommen, auch wo sie eher „gleiche Funktion“ als Rechenabhängigkeit sind (z. B. 2023-bebb-gk-A1.4b ← A1.4a). (4) `neben` nennt nur Themen aus der Themenliste des Katalogs, nie das Hauptthema; wo ein Begriff keinem Thema zuzuordnen war (Trapez, Strahlensatz, Kreisfläche), steht er nur in `stich`. (5) Zeichen: Vektoren in `kurz`/`zwischen` mit „|“-Trennung in Klammern wie im Katalog („(2 | 6 | 2)“); `stich` enthält keine Rechenschritte, nur Begriffe. (6) Die Prüfung „ASCII-Minus vor Ziffer“ in `vorrat-pruef.py` ist eine Zusatzprüfung über den Auftrag hinaus.
- Letzter Commit des Laufs: c84c471 (Teilstück 7/7); Nachtrag mit diesem Bericht als eigener Commit.
- Grob gelesene Token: etwa 75 000 für die sieben Teilstücke (241 KB Text), insgesamt mit Skripten und Ausgaben etwa 150 000.
