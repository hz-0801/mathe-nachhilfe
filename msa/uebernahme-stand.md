# Übernahme Vorrat P10 in die msa-Kataloge – Stand

Auftrag vom 2026-10-05 (Agent im Chat verbessereBlätter(), Opus 5.5).
Neustart: am ersten Teil weitermachen, der nicht „erledigt“ trägt.

- Teil 1 – erledigt 2026-10-05 15:33 UTC. msa-bau.py 0.4: neue Felder
  neben (nach typ_neben) und kurzloesung (nach ergebnis); Aufruf
  `python3 msa-bau.py --korrektur vorrat-p10-2022-2026.csv` (im Ordner msa/).
  Geändert: kurzloesung 146, zwischenergebnis 134 (davon 57 mit anderem
  Katalogwert, Liste unten), stichwoerter 131, neben 81, abhaengig_von 0
  (alle 6 Werte gleich). GYM nur Kopfzeile. Selbstprüfung aller 666 Zeilen
  bestanden.
- Teil 2 – offen
- Teil 3 – offen
- Teil 4 – offen
- Teil 5 – offen

## zwischenergebnis: Katalogwert → Beitabelle (57)

  2025-OS-B1e: '145/360' → '145 : 360 = 0,4028'
  2025-OS-B1h: '2 · 7 = 14; 3 · 8 = 24; (−6) · (−1) = 6' → '(−2) · 3 = −6'
  2026-FOR-B1e: 'Tabelle 2 gehört zu y = 3x, Tabelle 3 zu y = x²' → '3 · 2² = 12'
  2024-OS-B1h: 'sortierte Reihe 11, 17, 18, 20, 21, 21' → 'sortiert 11, 17, 18, 20, 21, 21 | Mitte zwischen 18 und 20'
  2022-OS-B1a: '15 Kästchen' → '15 Kästchen | 20 % = 1/5'
  2022-OS-B1c: 'beide Seiten −7' → '30 = 5x'
  2022-OS-B1d: 'Summe der sechs Werte 122' → 'Summe der sechs Werte 122 | 7 · 20 = 140'
  2022-OS-B1j: '2⁻⁵ = 0,03125' → '2⁻⁵ = 1/32 = 0,03125'
  2025-OS-K2a: 'AF = 25 cm; AB² = 3650 cm²' → 'AF = 25 cm | AB² = 25² + 55² = 3650 cm²'
  2025-OS-K2c: 'AD = DC = √1250 ≈ 35,4 cm' → 'AF = FC = DF = 25 cm | Basiswinkel 45°'
  2025-OS-K3b: 'P(22) = 2/16' → 'P(3 links) = 1/4 | P(2 rechts) = 2/4'
  2025-OS-K3c: 'P(12) = 1/4; P(21) = 1/16' → 'P(12) = 4/16 | P(21) = 1/16'
  2025-OS-K4a: 'x² = 29 156 cm²; tan α ≈ 0,0941' → 'x² = 170² + 16² = 29 156 | tan α = 16 : 170 ≈ 0,0941'
  2025-OS-K4c: 'Winkel gegenüber 160 cm: 34°' → 'dritter Winkel 34° gegenüber 160 cm | y = 160 · sin 141° : sin 34°'
  2025-OS-K5a: 'm = −1,5' → 'm = (−1,5 − 6) : (3 + 2) = −1,5 | n = 3'
  2025-OS-K5c: 'Diskriminante 9 − 7 = 2' → 'Diskriminante 9 − 7 = 2 | √2 ≈ 1,41'
  2025-OS-K6a: 'Häufigkeiten 1: 1, 2: 5, 4: 3, 5: 1' → 'Häufigkeiten: 1 ×1, 2 ×5, 4 ×3, 5 ×1'
  2025-OS-K6b: '5 Personen (33, 44, 31, 30, 41); 163,6°' → '5 von 11 Personen | 5/11 · 360° ≈ 163,6°'
  2025-OS-K6c: 'Summe 528; neue Summe 432 bei 9 Personen' → 'Summe 528 : 11 | neue Summe 432 : 9'
  2026-FOR-K2b: 'M ≈ 126,98 m²' → 'M = π · r · s ≈ 126,98 m²'
  2026-FOR-K2c: 'Kegelhöhe ≈ 7,20 m (√51,87)' → 'Kegelhöhe = √(8,6² − 4,7²) = √51,87 ≈ 7,20 m'
  2026-FOR-K3c: 'Differenz 0,05 €' → 'Differenz 0,05 € | 0,05 : 1,79 ≈ 0,0279'
  2026-FOR-K4a: 'h² = 1024 − 169 = 855' → 'h² = 32² − 13² = 855'
  2026-FOR-K4c: 'AF ≈ 72,4 cm' → 'sin 22° = h : AC | AF ≈ 72,4 cm'
  2026-FOR-K6c: 'P(gerade, gerade) = 1/12' → 'P(gerade, gerade) = 3/6 · 1/6 = 3/36'
  2026-FOR-K7c: '1,019^14 ≈ 1,3015' → 't = 2040 − 2026 = 14 | 1,019^14 ≈ 1,3015'
  2024-OS-K2b: 'Differenz 29,3 mm' → 'Differenz 48,5 − 19,2 = 29,3 mm | 29,3 : 48,5 ≈ 0,604'
  2024-OS-K2c: '12 : 508 ≈ 0,0236' → '60 : 508 · 360° ≈ 42,5° | 12 : 508 ≈ 0,0236'
  2024-OS-K3d: 'x² − 4x − 5 = 0; x = 5 und x = −1' → 'x² − 4x − 5 = 0 | x = 2 ± 3'
  2024-OS-K4c: 'V_Zyl ≈ 236 719,8 cm³; V_Kegel ≈ 75 398,2 cm³' → 'V_Zylinder = π · 30,5² · 81 ≈ 236 719,8 cm³ | V_Kegel = 1/3 · π · 30² · 80 ≈ 75 398,2 cm³'
  2024-OS-K6a: 'FA² = 147 456 − 65 025 = 82 431' → 'FA² = 384² − 255² = 82 431'
  2024-OS-K6c: '120 s' → 't = 384 : 3,2 = 120 s'
  2024-OS-K6d: 'γ = 34°' → 'γ = 180° − 38° − 108° = 34° | BC = 384 · sin 38° : sin 34°'
  2024-OS-K7b: '0,6t = 3' → 'r = 13 − t | 29,9 − 0,6t = 26,9 ⇒ 0,6t = 3'
  2023-OS-K2b: 'Mittellinie 20,4 m' → 'Mittellinie (25,8 + 15) : 2 = 20,4 m'
  2023-OS-K2c: 's ≈ 9,65 m' → 'Schenkel s = 8 : sin 56° ≈ 9,65 m (oder √(5,4² + 8²)) | Überstand (25,8 − 15) : 2 = 5,4 m'
  2023-OS-K3b: '120 Mehrkilometer, 43,20 €' → '120 Mehrkilometer · 0,36 € = 43,20 € | 5 · 27 = 135 €'
  2023-OS-K4a: 'zweiter Schnittpunkt (−7|−30) außerhalb des Bildes' → 'Steigung 4, y-Achsenabschnitt −2 | zweiter Schnittpunkt (−7|−30) außerhalb'
  2023-OS-K4c: 'x² + 2x − 15 = 0' → 'x² + 2x − 15 = 0 | x = −1 ± 4'
  2023-OS-K5b: 'Grundfläche ≈ 50,3 cm²' → 'Grundfläche ≈ 50,3 cm² | 1 cm³ = 1 ml'
  2023-OS-K5c: 'Deckelfläche ≈ 603,2 cm²' → '100 : 8 = 12,5 ⇒ 12 Deckel | Deckelfläche 12 · π · 16 ≈ 603,2 cm² | Blech 800 cm²'
  2023-OS-K5d: 'Grundfläche ≈ 50,3 cm²' → '1 l = 1000 cm³ | h = V : (π · r²) | Grundfläche ≈ 50,3 cm²'
  2023-OS-K6b: 'mittleres Alter 50 %, Kinder 25 %' → 'mittleres Alter 3,9 : 7,8 = 50 % | Kinder 25 %'
  2023-OS-K6d: 'Verhältnis der Säulen ≈ 1,35 entspricht 525 : 389' → '389 Mio. ≙ 7,8 Kästchen ⇒ 50 Mio. je Kästchen | 10,5 · 50 = 525'
  2023-OS-K7b: 'cos 65° ≈ 0,4226' → 'sin 45° ≈ 0,7071 | cos 65° ≈ 0,4226'
  2022-OS-K2b: 'Grundfläche ≈ 32,2 cm²' → 'Grundfläche ≈ 32,2 cm² | 1 cm³ = 1 ml'
  2022-OS-K2c: 'Diagonale ≈ 9,5 cm' → 'Diagonale √(7² + 6,4²) ≈ 9,5 cm | Durchmesser 6,4 cm'
  2022-OS-K2d: 'r² ≈ 19,33' → 'r² = 425 : (π · 7) ≈ 19,33'
  2022-OS-K3c: 'x² − 2x − 3 = 0' → 'x² − 2x − 3 = 0 | x = 1 ± 2'
  2022-OS-K4a: 'Summe 2 255' → 'Summe 2255 : 5'
  2022-OS-K4b: 'Differenz 70' → 'Differenz 70 | 70 : 470 ≈ 0,149'
  2022-OS-K5b: 'sin α ≈ 0,525' → 'sin α = 7,4 : 14,1 ≈ 0,525'
  2022-OS-K5d: 'sin 52° ≈ 0,788' → 'sin 52° ≈ 0,788 | a = 7,4 : sin 52°'
  2022-OS-K5e: 'DB ≈ 5,8 m, c ≈ 17,8 m' → 'DB = 7,4 : tan 52° ≈ 5,8 m | c = 12,0 + 5,8 ≈ 17,8 m'
  2022-OS-K6a: '12 · 22 = 264' → '12 · 22 = 264 €'
  2022-OS-K6b: 'x ≥ 18,36' → '55x + 990 ≥ 2000 ⇒ x ≥ 18,36 | aufrunden'
  2022-OS-K7b: '6x = 163,20' → 'y = 63 − x | 6x = 163,20'
