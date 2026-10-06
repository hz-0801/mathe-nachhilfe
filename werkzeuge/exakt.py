# exakt.py – Lauf 06.10.2026: Beschluss „Ergebnisse exakt zuerst, dann ≈ gerundet“ für alle
# P10-Kapitel außer Prozent (Prozent: werkzeuge/exakt-prozent.py, Lauf A, bleibt unverändert).
# Ändert in msa/msa-katalog-{basis,gym,kontext}.csv nur die Felder kurzloesung und zwischenergebnis.
# Jede Ersetzung trägt ihre Gegenprobe: (exakter Ausdruck in sympy, gerundeter Wert wie im Feld);
# der gerundete Wert muss aus dem exakten Wert durch Runden auf dieselbe Stellenzahl entstehen.
# Wiederholbar: Felder, die den neuen Text schon enthalten, bleiben. Prüft Zeilenzahl, Rundreise,
# dass nur die zwei Felder geändert sind und dass kein neues „ ; “ (Trenner) entsteht.
import csv, io, sys, re
from sympy import Rational as R, pi, sqrt, sin, cos, tan, asin, acos, atan, N

def g(x):  # Grad -> Bogenmaß
    return x * pi / 180
def deg(x):  # Bogenmaß -> Grad
    return x * 180 / pi
def zahl(s):  # „1 734,9“ -> (1734.9, 1)
    s = s.replace(' ', '').replace(' ', '').replace('−', '-')
    st = len(s.split(',')[1]) if ',' in s else 0
    return float(s.replace(',', '.')), st
def stimmt(expr, gerundet):
    v, st = zahl(gerundet)
    w = float(N(expr, 30))
    return abs(round(w, st) - v) < 10 ** (-st) / 2 + 1e-12

# Gegenprobe an bekannten Werten (Pythagoras, Kreis, Volumen, Trigonometrie)
for e, w in [(sqrt(3**2 + 4**2), '5'), (5 * sqrt(146), '60,4'), (10 * sqrt(13), '36,1'),
             (sqrt(65), '8,06'), (900 * pi, '2827,4'), (288 * pi, '904,8'),
             (R(4, 3) * pi * 6**3, '904,8'), (25 * sqrt(2), '35,4'), (deg(atan(2)), '63,4'),
             (1 - pi / 4, '0,215')]:
    assert stimmt(e, w), (e, w)

S = sqrt(R(553719))
# id -> feld -> [(alt, neu, [(ausdruck, gerundet), ...])]
E = {
 # basis
 '2025-OS-B1e': {'kurzloesung': [('≈ 40,3 %', '29/72 ≈ 40,3 %', [(R(29, 72) * 100, '40,3')])],
                 'zwischenergebnis': [('145 : 360 = 0,4028', '145 : 360 = 29/72 ≈ 0,4028', [(R(29, 72), '0,4028')])]},
 '2026-FOR-B1f': {'zwischenergebnis': [('V = a³', 'V = a³ = (3 cm)³ = 27 cm³', [])]},
 '2023-OS-B1c': {'zwischenergebnis': [('A = a · b', 'A = a · b ⇒ b = 42 000 mm² : 400 mm = 105 mm', [])]},
 # gym
 '2014-GYM-K5a': {'zwischenergebnis': [('Halbkreisfläche ≈ 37 253 m²', 'Halbkreisfläche 11 858π ≈ 37 253 m²', [(11858 * pi, '37 253')])]},
 '2014-GYM-K5c': {'zwischenergebnis': [('h ≈ 116,33 m', 'h = √13 533 ≈ 116,33 m', [(sqrt(13533), '116,33')])]},
 '2015-GYM-K4b': {'zwischenergebnis': [('Mantelfläche Rumpf ≈ 65,22 cm²', 'Mantelfläche Rumpf 20,76π ≈ 65,22 cm²', [(R(2076, 100) * pi, '65,22')])]},
 '2016-GYM-K3b': {'zwischenergebnis': [('V ≈ 167,55 cm³; Masse ≈ 1 306,9 g', 'V = 160π/3 ≈ 167,55 cm³; Masse = 416π ≈ 1 306,9 g',
                                        [(R(160, 3) * pi, '167,55'), (416 * pi, '1 306,9')])]},
 '2016-GYM-K4c': {'zwischenergebnis': [('Nullstelle bei x ≈ 37,57 m', 'Nullstelle bei x = √(12 : 0,0085) = 40√255/17 ≈ 37,57 m',
                                        [(40 * sqrt(255) / 17, '37,57'), (sqrt(12 / R(85, 10000)), '37,57')])]},
 '2016-GYM-K5a': {'zwischenergebnis': [('Anteil ≈ 20,86 %', 'Anteil 73/350 ≈ 20,86 %', [(R(73, 350) * 100, '20,86'), (R(1460, 7000), '0,2086')])]},
 '2016-GYM-K5b': {'zwischenergebnis': [('Seite a ≈ 1123,33 m', 'Seite a = 3370/3 ≈ 1123,33 m', [(R(3370, 3), '1123,33')])]},
 '2017-GYM-K3b': {'zwischenergebnis': [('rechte Seite ≈ 11,34 m, linke Seite ≈ 22,77 m', 'rechte Seite √128,5 ≈ 11,34 m, linke Seite √518,5 ≈ 22,77 m',
                                        [(sqrt(R(1285, 10)), '11,34'), (sqrt(R(5185, 10)), '22,77')])]},
 '2018-GYM-K3c': {'zwischenergebnis': [('V ≈ 647,64 cm³', 'V = 3 598 mm² · 180 mm = 647,64 cm³', [])]},
 '2019-GYM-K3b': {'zwischenergebnis': [('Pythagoras-Strecke ≈ 2,92 m', 'Pythagoras-Strecke √8,5 ≈ 2,92 m', [(sqrt(R(85, 10)), '2,92')])]},
 '2019-GYM-K4b': {'zwischenergebnis': [('Seitenhöhe ≈ 3,61 m', 'Seitenhöhe √13 ≈ 3,61 m', [(sqrt(13), '3,61')])]},
 '2019-GYM-K4c': {'zwischenergebnis': [('Fensterfläche ≈ 7,07 m²', 'Fensterfläche 2,25π ≈ 7,07 m²', [(R(9, 4) * pi, '7,07')])]},
 # kontext
 '2025-OS-K2a': {'kurzloesung': [('AB ≈ 60,4 cm', 'AB = 5√146 ≈ 60,4 cm', [(5 * sqrt(146), '60,4'), (sqrt(25**2 + 55**2), '60,4')])]},
 '2025-OS-K4a': {'kurzloesung': [('x ≈ 170,8 cm | α ≈ 5,4°', 'x = 2√7289 ≈ 170,8 cm | α = tan⁻¹(8/85) ≈ 5,4°',
                                  [(2 * sqrt(7289), '170,8'), (sqrt(170**2 + 16**2), '170,8'), (deg(atan(R(8, 85))), '5,4')])],
                 'zwischenergebnis': [('tan α = 16 : 170 ≈ 0,0941', 'tan α = 16 : 170 = 8/85 ≈ 0,0941', [(R(8, 85), '0,0941')])]},
 '2025-OS-K4c': {'kurzloesung': [('y ≈ 180,1 cm', 'y = 160 · sin 141° : sin 34° ≈ 180,1 cm', [(160 * sin(g(141)) / sin(g(34)), '180,1')])]},
 '2025-OS-K6b': {'kurzloesung': [('≈ 45,5 % | Sektor ≈ 164° (Rest ≈ 196°)', '5/11 ≈ 45,5 % | Sektor 1800/11° ≈ 164° (Rest 2160/11° ≈ 196°)',
                                  [(R(500, 11), '45,5'), (R(1800, 11), '164'), (R(2160, 11), '196')])],
                 'zwischenergebnis': [('5/11 · 360° ≈ 163,6°', '5/11 · 360° = 1800/11° ≈ 163,6°', [(R(1800, 11), '163,6')])]},
 '2026-FOR-K2a': {'kurzloesung': [('≈ 1734,9 m³', '552,25π ≈ 1734,9 m³', [(R(55225, 100) * pi, '1734,9')])],
                  'zwischenergebnis': [('V = π · r² · h', 'V = π · r² · h = π · 4,7² · 25 = 552,25π m³', [])]},
 '2026-FOR-K2b': {'zwischenergebnis': [('M = π · r · s ≈ 126,98 m²', 'M = π · r · s = 40,42π ≈ 126,98 m²', [(R(4042, 100) * pi, '126,98')])]},
 '2026-EBR-K2b': {'zwischenergebnis': [('M ≈ 126,98 m²', 'M = 40,42π ≈ 126,98 m²', [(R(4042, 100) * pi, '126,98')])]},
 '2026-FOR-K2c': {'kurzloesung': [('≈ 32,2 m', '25 + √51,87 ≈ 32,2 m', [(25 + sqrt(R(5187, 100)), '32,2')])]},
 '2026-FOR-K4a': {'kurzloesung': [('h ≈ 29,2 cm', 'h = 3√95 ≈ 29,2 cm', [(3 * sqrt(95), '29,2')])]},
 '2026-FOR-K4b': {'kurzloesung': [('ε ≈ 66,0°', 'ε = cos⁻¹(13/32) ≈ 66,0°', [(deg(acos(R(13, 32))), '66,0')])],
                  'zwischenergebnis': [('cos ε = 13 : 32 ≈ 0,406', 'cos ε = 13 : 32 = 13/32 ≈ 0,406', [(R(13, 32), '0,406')])]},
 '2026-FOR-K4c': {'kurzloesung': [('AC ≈ 78,1 cm', 'AC = 3√95 : sin 22° ≈ 78,1 cm', [(3 * sqrt(95) / sin(g(22)), '78,1')])],
                  'zwischenergebnis': [('AF ≈ 72,4 cm', 'AF = 3√95 : tan 22° ≈ 72,4 cm', [(3 * sqrt(95) / tan(g(22)), '72,4')])]},
 '2026-FOR-K5c': {'zwischenergebnis': [('Scheitelpunktform p(x) = (x − d)² + e', 'Scheitelpunktform p(x) = (x − d)² + e mit d = 2, e = −2', [])]},
 '2022-OS-K3b': {'zwischenergebnis': [('Scheitelpunktform p(x) = (x − d)² + e', 'Scheitelpunktform p(x) = (x − d)² + e mit d = 2, e = −4', [])]},
 '2024-OS-K2b': {'kurzloesung': [('581,7 : 12 ≈ 48,5 mm | April liegt ≈ 60,4 %', '581,7 : 12 = 48,475 ≈ 48,5 mm | April liegt 293/485 ≈ 60,4 %',
                                  [(R(5817, 120), '48,5'), (R(29300, 485), '60,4')])],
                 'zwischenergebnis': [('29,3 : 48,5 ≈ 0,604', '29,3 : 48,5 = 293/485 ≈ 0,604', [(R(293, 485), '0,604')])]},
 '2024-OS-K2c': {'kurzloesung': [('beschriften | ≈ 8,5°', 'beschriften | 1080/127° ≈ 8,5°', [(R(1080, 127), '8,5'), (R(5400, 127), '43')])],
                 'zwischenergebnis': [('60 : 508 · 360° ≈ 42,5°', '60 : 508 · 360° = 5400/127° ≈ 42,5°', [(R(5400, 127), '42,5')]),
                                      ('12 : 508 ≈ 0,0236', '12 : 508 = 3/127 ≈ 0,0236', [(R(3, 127), '0,0236')])]},
 '2024-OS-K4a': {'kurzloesung': [('≈ 2827,4 cm²', '900π ≈ 2827,4 cm²', [(900 * pi, '2827,4')])],
                 'zwischenergebnis': [('G = π · r² ;', 'G = π · r² = π · 30² = 900π cm² ;', [])]},
 '2024-OS-K4c': {'kurzloesung': [('≈ 161 322 cm³', '51 350,25π ≈ 161 322 cm³', [(R(5135025, 100) * pi, '161 322')])],
                 'zwischenergebnis': [('π · 30,5² · 81 ≈ 236 719,8', 'π · 30,5² · 81 = 75 350,25π ≈ 236 719,8', [(R(7535025, 100) * pi, '236 719,8')]),
                                      ('1/3 · π · 30² · 80 ≈ 75 398,2', '1/3 · π · 30² · 80 = 24 000π ≈ 75 398,2', [(24000 * pi, '75 398,2')])]},
 '2024-OS-K6a': {'kurzloesung': [('FA ≈ 287,1 m', 'FA = 3√9159 ≈ 287,1 m', [(3 * sqrt(9159), '287,1'), (sqrt(384**2 - 255**2), '287,1')])]},
 '2024-OS-K6b': {'kurzloesung': [('β1 ≈ 48,4°', 'β1 = cos⁻¹(85/128) ≈ 48,4°', [(deg(acos(R(85, 128))), '48,4')])],
                 'zwischenergebnis': [('cos β1 = 255 : 384 ≈ 0,664', 'cos β1 = 255 : 384 = 85/128 ≈ 0,664', [(R(85, 128), '0,664')])]},
 '2024-OS-K6d': {'kurzloesung': [('BC ≈ 422,8 m', 'BC = 384 · sin 38° : sin 34° ≈ 422,8 m', [(384 * sin(g(38)) / sin(g(34)), '422,8')])]},
 '2023-OS-K2c': {'kurzloesung': [('U ≈ 60,1 m', 'U = 40,8 + 16 : sin 56° ≈ 60,1 m', [(R(408, 10) + 16 / sin(g(56)), '60,1'), (R(408, 10) + 2 * sqrt(R(9316, 100)), '60,1')])]},
 '2023-OS-K5a': {'kurzloesung': [('a ≈ 25,1 cm', 'a = 8π ≈ 25,1 cm', [(8 * pi, '25,1')])]},
 '2023-OS-K5b': {'kurzloesung': [('V = π · 4² · 8 ≈ 402,1', 'V = π · 4² · 8 = 128π ≈ 402,1', [(128 * pi, '402,1')])],
                 'zwischenergebnis': [('Grundfläche ≈ 50,3 cm²', 'Grundfläche 16π ≈ 50,3 cm²', [(16 * pi, '50,3')])]},
 '2023-OS-K5d': {'kurzloesung': [('h ≈ 19,9 cm', 'h = 125/(2π) ≈ 19,9 cm', [(R(125, 2) / pi, '19,9'), (1000 / (16 * pi), '19,9')])],
                 'zwischenergebnis': [('h = V : (π · r²)', 'h = V : (π · r²) = 1000 : (16π)', []),
                                      ('Grundfläche ≈ 50,3 cm²', 'Grundfläche 16π ≈ 50,3 cm²', [(16 * pi, '50,3')])]},
 '2023-OS-K6d': {'kurzloesung': [('Säule Arabisch ≈ 5,8 Kästchen', 'Säule Arabisch 290 : 50 = 5,8 Kästchen', [])]},
 '2023-OS-K7b': {'kurzloesung': [('BF = 131,5 · sin 45° ≈ 93,0 cm', 'BF = 131,5 · sin 45° = 65,75√2 ≈ 93,0 cm', [(R(6575, 100) * sqrt(2), '93,0')]),
                                  ('BC = BF : cos 65° ≈ 220,0 cm', 'BC = 65,75√2 : cos 65° ≈ 220,0 cm', [(R(6575, 100) * sqrt(2) / cos(g(65)), '220,0')])],
                 'zwischenergebnis': [('sin 45° ≈ 0,7071', 'sin 45° = √2/2 ≈ 0,7071', [(sqrt(2) / 2, '0,7071')])]},
 '2022-OS-K2a': {'kurzloesung': [('Länge ≈ 20,1 cm', 'Länge 6,4π ≈ 20,1 cm', [(R(64, 10) * pi, '20,1')])],
                 'zwischenergebnis': [('Breite = h', 'Breite = h = 7 cm', [])]},
 '2022-OS-K2b': {'kurzloesung': [('V = π · 3,2² · 7 ≈ 225,2', 'V = π · 3,2² · 7 = 71,68π ≈ 225,2', [(R(7168, 100) * pi, '225,2')])],
                 'zwischenergebnis': [('Grundfläche ≈ 32,2 cm²', 'Grundfläche 10,24π ≈ 32,2 cm²', [(R(1024, 100) * pi, '32,2')])]},
 '2022-OS-K2c': {'kurzloesung': [('≈ 11,5 cm', '√89,96 + 2 ≈ 11,5 cm', [(sqrt(R(8996, 100)) + 2, '11,5')])],
                 'zwischenergebnis': [('√(7² + 6,4²) ≈ 9,5 cm', '√(7² + 6,4²) = √89,96 ≈ 9,5 cm', [(sqrt(R(8996, 100)), '9,5')])]},
 '2022-OS-K2d': {'kurzloesung': [('r ≈ 4,40 cm', 'r = √(425/(7π)) ≈ 4,40 cm', [(sqrt(R(425, 7) / pi), '4,40')])],
                 'zwischenergebnis': [('r² = 425 : (π · 7) ≈ 19,33', 'r² = 425 : (π · 7) = 425/(7π) ≈ 19,33', [(R(425, 7) / pi, '19,33')])]},
 '2022-OS-K4c': {'kurzloesung': [('(≈ 7,4 %)', '(2/27 ≈ 7,4 %)', [(R(3200, 432), '7,4')])]},
 '2022-OS-K5b': {'kurzloesung': [('α ≈ 31,7°', 'α = sin⁻¹(74/141) ≈ 31,7°', [(deg(asin(R(74, 141))), '31,7')])],
                 'zwischenergebnis': [('sin α = 7,4 : 14,1 ≈ 0,525', 'sin α = 7,4 : 14,1 = 74/141 ≈ 0,525', [(R(74, 141), '0,525')])]},
 '2022-OS-K5c': {'kurzloesung': [('γ₁ ≈ 58,3°', 'γ₁ = cos⁻¹(74/141) ≈ 58,3°', [(deg(acos(R(74, 141))), '58,3'), (90 - deg(asin(R(74, 141))), '58,3')])]},
 '2022-OS-K5d': {'kurzloesung': [('a ≈ 9,4 m', 'a = 7,4 : sin 52° ≈ 9,4 m', [(R(74, 10) / sin(g(52)), '9,4')])]},
 '2022-OS-K5e': {'kurzloesung': [('A ≈ 65,8 m²', 'A = 3,7 · (√144,05 + 7,4 : tan 52°) ≈ 65,8 m²',
                                  [(R(37, 10) * (sqrt(R(14405, 100)) + R(74, 10) / tan(g(52))), '65,8')])]},
 '2021-OS-K3b': {'kurzloesung': [('AD ≈ 860,4 m', 'AD = 1500 · cos 55° ≈ 860,4 m', [(1500 * cos(g(55)), '860,4')])]},
 '2021-OS-K3c': {'kurzloesung': [('BC ≈ 1805,5 m', 'BC = 2004 · sin 60° : sin 74° ≈ 1805,5 m', [(2004 * sin(g(60)) / sin(g(74)), '1805,5')])]},
 '2021-OS-K4b': {'kurzloesung': [('(≈ 1004 l)', '(319,58π l ≈ 1004 l)', [(R(31958, 100) * pi, '1004'), (pi * 58**2 * 95 / 1000, '1004')])]},
 '2020-OS-K4a': {'kurzloesung': [('2022: ≈ 59,0', '2022: 57,3 · 1,03 = 59,019 ≈ 59,0', [(R(573, 10) * R(103, 100), '59,0')])],
                 'zwischenergebnis': [('57,3 · 1,03 ≈ 59,0', '57,3 · 1,03 = 59,019 ≈ 59,0', [(R(573, 10) * R(103, 100), '59,0')])]},
 '2020-OS-K5b': {'kurzloesung': [('α ≈ 57,3°', 'α = tan⁻¹(14/9) ≈ 57,3°', [(deg(atan(R(14, 9))), '57,3')])]},
 '2020-OS-K7a': {'kurzloesung': [('AB ≈ 36,1 m', 'AB = 10√13 ≈ 36,1 m', [(10 * sqrt(13), '36,1')])]},
 '2020-OS-K7c': {'kurzloesung': [('DP ≈ 3,2 m', 'DP = 11 · sin 115° : sin 49° − 10 ≈ 3,2 m', [(11 * sin(g(115)) / sin(g(49)) - 10, '3,2')])]},
 '2019-OS-K2d': {'kurzloesung': [('β ≈ 63,4°', 'β = tan⁻¹(2) ≈ 63,4°', [(deg(atan(2)), '63,4'), (sqrt(20), '4,47')])]},
 '2019-OS-K3a': {'kurzloesung': [('BC ≈ 8,06 m', 'BC = √65 ≈ 8,06 m', [(sqrt(65), '8,06')])]},
 '2019-OS-K3b': {'zwischenergebnis': [('cos α ≈ 0,444', 'cos α = 4/9 ≈ 0,444', [(R(4, 9), '0,444'), (deg(acos(R(4, 9))), '63,6')])]},
 '2019-OS-K3c': {'kurzloesung': [('AD ≈ 7,9 m', 'AD = 9 · sin 60° : sin 80° ≈ 7,9 m', [(9 * sin(g(60)) / sin(g(80)), '7,9')])]},
 '2019-OS-K4c': {'kurzloesung': [('V = 0,975 · 1,2 ≈ 1,17 m³ ≈ 1,2 m³', 'V = 0,975 · 1,2 = 1,17 m³ ≈ 1,2 m³', [(R(975, 1000) * R(12, 10), '1,2')])]},
 '2019-OS-K6b': {'zwischenergebnis': [('4/20 · 3/19 · 2/18 ≈ 0,35 %', '4/20 · 3/19 · 2/18 = 1/285 ≈ 0,35 %', [(R(100, 285), '0,35'), (R(4 * 3 * 2, 20 * 19 * 18) * 100, '0,35')])]},
 '2018-OS-K3d': {'kurzloesung': [('jede 15. ≈ 6,7 %', 'jede 15. = 1/15 ≈ 6,7 %', [(R(100, 15), '6,7')])]},
 '2018-OS-K6a': {'kurzloesung': [('≈ 207,83 m²', '240 − 10,24π ≈ 207,83 m²', [(240 - R(1024, 100) * pi, '207,83')])],
                 'zwischenergebnis': [('Kreis π · 3,2² ≈ 32,17 m²', 'Kreis π · 3,2² = 10,24π ≈ 32,17 m²', [(R(1024, 100) * pi, '32,17')])]},
 '2018-OS-K6b': {'kurzloesung': [('≈ 436,3 m²', '138,88π ≈ 436,3 m²', [(R(13888, 100) * pi, '436,3')])],
                 'zwischenergebnis': [('M = π · d · h', 'M = π · d · h = π · 6,4 · 21,7 = 138,88π m²', [])]},
 '2017-OS-K2c': {'kurzloesung': [('| ≈ 40° |', '| 40,32° ≈ 40° |', [(R(112, 1000) * 360, '40')])],
                 'zwischenergebnis': [('0,112 · 360° ≈ 40,3°', '0,112 · 360° = 40,32° ≈ 40,3°', [(R(112, 1000) * 360, '40,3')])]},
 '2017-OS-K3b': {'kurzloesung': [('≈ 69,63 m²', '50 + 6,25π ≈ 69,63 m²', [(50 + R(625, 100) * pi, '69,63')])],
                 'zwischenergebnis': [('Kreis ≈ 19,63 m²', 'Kreis 6,25π ≈ 19,63 m²', [(R(625, 100) * pi, '19,63')])]},
 '2017-OS-K4b': {'kurzloesung': [('PB ≈ 1,72 m', 'PB = 1,20 : tan 34,9° ≈ 1,72 m', [(R(12, 10) / tan(g(R(349, 10))), '1,72')])]},
 '2017-OS-K4c': {'kurzloesung': [('BC ≈ 7,00 m | ≈ 92 m²', 'BC = 4,5 · sin 62,8° : sin 34,9° ≈ 7,00 m | 8 · (4,5 + BC) ≈ 92 m²',
                                  [(R(45, 10) * sin(g(R(628, 10))) / sin(g(R(349, 10))), '7,00'),
                                   (8 * (R(45, 10) + R(45, 10) * sin(g(R(628, 10))) / sin(g(R(349, 10)))), '92')])]},
 '2017-OS-K7a': {'kurzloesung': [('≈ 757 hPa |', '756,9 ≈ 757 hPa |', [(870 * R(87, 100), '757')])],
                 'zwischenergebnis': [('870 · 0,87 ≈ 757', '870 · 0,87 = 756,9 ≈ 757', [(870 * R(87, 100), '757')])]},
 '2016-OS-K3b': {'kurzloesung': [('≈ 3,60 m²', '1,1449π ≈ 3,60 m²', [(R(11449, 10000) * pi, '3,60')])]},
 '2016-OS-K3c': {'kurzloesung': [('≈ 904,8 cm³', '288π ≈ 904,8 cm³', [(288 * pi, '904,8')])]},
 '2016-OS-K3d': {'kurzloesung': [('≈ 512,8 cm³', '20 000/39 ≈ 512,8 cm³', [(R(20000, 39), '512,8')])],
                 'zwischenergebnis': [('V = m : ϱ', 'V = m : ϱ = 4000 : 7,8 = 20 000/39', [])]},
 '2016-OS-K6a': {'zwischenergebnis': [('Grundpreis = y-Achsenabschnitt', 'Grundpreis = y-Achsenabschnitt = 200 €', [])]},
 '2016-OS-K7b': {'kurzloesung': [('AD ≈ 744 m', 'AD = √553 719 ≈ 744 m', [(S, '744'), (sqrt(920**2 - 541**2), '744')])]},
 '2016-OS-K7c': {'kurzloesung': [('BD ≈ 502 m', 'BD = √553 719 · tan 34° ≈ 502 m', [(S * tan(g(34)), '502'), (744 * tan(g(34)), '502')])]},
 '2015-OS-K5c': {'kurzloesung': [('BD ≈ 5,85 cm', 'BD = 4,1 · sin 123° : sin 36° ≈ 5,85 cm', [(R(41, 10) * sin(g(123)) / sin(g(36)), '5,85')])]},
 '2015-OS-K5d': {'zwischenergebnis': [('AE ≈ 1,47 cm ; DE ≈ 3,83 cm', 'AE = 4,1 · sin 21° ≈ 1,47 cm ; DE = 4,1 · cos 21° ≈ 3,83 cm',
                                        [(R(41, 10) * sin(g(21)), '1,47'), (R(41, 10) * cos(g(21)), '3,83')])]},
 '2015-OS-K6c': {'kurzloesung': [('√(0,68² + 0,40²) ≈ 0,789 m ⇒ A = ½ · 0,80 · 0,789 ≈ 0,32 m²',
                                  '√(0,68² + 0,40²) = √0,6224 ≈ 0,789 m ⇒ A = 0,4 · √0,6224 ≈ 0,32 m²',
                                  [(sqrt(R(6224, 10000)), '0,789'), (R(4, 10) * sqrt(R(6224, 10000)), '0,32')])],
                 'zwischenergebnis': [('h_s ≈ 0,789 m ; A ≈ 0,316 m²', 'h_s = √0,6224 ≈ 0,789 m ; A = 0,4 · √0,6224 ≈ 0,316 m²',
                                        [(sqrt(R(6224, 10000)), '0,789'), (R(4, 10) * sqrt(R(6224, 10000)), '0,316')])]},
 '2015-OS-K7a': {'kurzloesung': [('≈ 40 000 Zuschauer (40 021)', '680 353/17 ≈ 40 000 Zuschauer (40 021)',
                                  [(R(680353, 17), '40 021'), (R(680353, 17) / 1000, '40')])]},
 '2014-OS-K2b': {'kurzloesung': [('≈ 5665 m (≈ 5,67 km)', '2800 · sin 60° : sin 50° + 2500 ≈ 5665 m (≈ 5,67 km)',
                                  [(2800 * sin(g(60)) / sin(g(50)) + 2500, '5665'), ((2800 * sin(g(60)) / sin(g(50)) + 2500) / 1000, '5,67')])],
                 'zwischenergebnis': [('JR ≈ 3165 m', 'JR = 2800 · sin 60° : sin 50° ≈ 3165 m', [(2800 * sin(g(60)) / sin(g(50)), '3165')])]},
 '2014-OS-K4e': {'kurzloesung': [('100 000 ≈ 0,6 ct', '100 000 = 0,585 ct ≈ 0,6 ct', [(R(58500, 100000), '0,6')])]},
 '2014-OS-K5a': {'zwischenergebnis': [('V = G · h', 'V = G · h = 5 225 cm² · 165 cm', [])]},
}

# Gegenprobe aller Ersetzungen: gerundeter Teil entsteht aus dem exakten Wert
fehler = [(k, a, w) for k, d in E.items() for fe, L in d.items() for (_, _, P) in L for (a, w) in P if not stimmt(a, w)]
if fehler:
    sys.exit('Gegenprobe kippt: ' + repr(fehler))
for k, d in E.items():
    for fe, L in d.items():
        for alt, neu, _ in L:
            if neu.count(' ; ') != alt.count(' ; '):
                sys.exit(f'{k}: Trenner „ ; “ würde neu entstehen')

def lies(p):
    raw = open(p, encoding='utf-8', newline='').read()
    rows = list(csv.reader(io.StringIO(raw), delimiter=';'))
    return raw, rows
def schreib(rows):
    out = io.StringIO(); w = csv.writer(out, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\n')
    w.writerows(rows); return out.getvalue()

n = 0; gesehen = set()
for p in ('msa/msa-katalog-basis.csv', 'msa/msa-katalog-gym.csv', 'msa/msa-katalog-kontext.csv'):
    raw, rows = lies(p)
    if schreib(rows) != raw: sys.exit('Rundreise ändert ' + p)
    alt_rows = [list(r) for r in rows]
    kopf = rows[0]
    for r in rows[1:]:
        d = E.get(r[0])
        if not d: continue
        gesehen.add(r[0])
        for feld, L in d.items():
            i = kopf.index(feld)
            for alt, neu, _ in L:
                if neu in r[i]: continue
                if r[i].count(alt) != 1: sys.exit(f'{r[0]} {feld}: „{alt}“ nicht genau einmal in „{r[i]}“')
                r[i] = r[i].replace(alt, neu); n += 1
    erlaubt = {kopf.index('kurzloesung'), kopf.index('zwischenergebnis')}
    assert len(rows) == len(alt_rows)
    for a, b in zip(alt_rows, rows):
        assert len(a) == len(b)
        for j, (x, y) in enumerate(zip(a, b)):
            if x != y:
                assert j in erlaubt, (p, a[0], kopf[j])
                assert y.count(' ; ') == x.count(' ; '), (p, a[0])
    open(p, 'w', encoding='utf-8', newline='').write(schreib(rows))
fehlt = set(E) - gesehen
if fehlt: sys.exit('ids nicht gefunden: ' + repr(fehlt))
print('Zeilen mit Tabelle:', len(E), '– geändert:', n, 'Ersetzungen')
