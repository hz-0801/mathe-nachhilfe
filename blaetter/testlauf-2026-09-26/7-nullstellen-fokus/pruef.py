# pruef.py – Mindestprüfung 5.1 a für den Fokus Nullstellen (quadratische-funktionen)
# Aufruf: python pruef.py zone | e4   → schreibt pruef_out_<teil>.txt
# Skriptwert: sympy rechnet aus der Aufgabe; Blattwert: aus zone_l.tex / e4_l.tex abgetippt.
import sys
from sympy import symbols, sympify, solve, sqrt, Rational, S, simplify, N

x = symbols('x', real=True)

def reelle_nullstellen(term):
    return sorted([float(N(r)) for r in solve(sympify(term, locals={'x': x}), x) if r.is_real], reverse=True)

def gerundet(liste, st=2):
    return [round(v, st) for v in liste]

# Art: 'ns' exakte Nullstellen (Liste, leer = keine), 'nsr' gerundete Nullstellen,
#      'wert' Zahlenwert, 'gl' Gleichung 0 = Term (Term gleich f), 'anz' Zahl der Nullstellen
TEIL = {
 'zone': [
  ('1a', 'ns', '2*x-8', [4]),
  ('1b', 'ns', '-3*x+6', [2]),
  ('2a', 'wert', '(-6)**2', 36),
  ('2b', 'wert', '(-1.5)**2', 2.25),
  ('3a', 'wert', 'sqrt(81)', 9),
  ('3b', 'wertr', 'sqrt(13)', 3.61),
  ('4a', 'ns', 'x**2-64', [8, -8]),
  ('4b', 'ns', 'x**2+9', []),
  ('5a', 'ns', 'x**2+8*x+15', [-3, -5]),
  ('5b', 'ns', 'x**2-2*x-24', [6, -4]),
 ],
 'e4': [
  ('6a', 'gl', '(x-5)**2-4', '(x-5)**2-4'),
  ('6b', 'gl', 'x**2+3*x-10', 'x**2+3*x-10'),
  ('6c', 'gl', '-(x+1)**2+9', '-(x+1)**2+9'),
  ('6d', 'gl', 'x**2-36', 'x**2-36'),
  ('6e', 'gl', '3*x**2-12*x+9', '3*x**2-12*x+9'),
  ('7a', 'ns', '(x-1)**2-4', [3, -1]),
  ('7b', 'ns', '(x-4)**2-1', [5, 3]),
  ('7c', 'ns', '(x-2)**2-9', [5, -1]),
  ('7d', 'ns', '(x-5)**2-16', [9, 1]),
  ('8a', 'ns', '(x+2)**2-1', [-1, -3]),
  ('8b', 'ns', '(x+4)**2-25', [1, -9]),
  ('8c', 'ns', '-(x-1)**2+16', [5, -3]),
  ('8d', 'ns', '-(x+3)**2+4', [-1, -5]),
  ('9a', 'ns', '2*(x-3)**2-8', [5, 1]),
  ('9b', 'ns', '-3*(x+1)**2+27', [2, -4]),
  ('9c', 'ns', 'Rational(1,2)*(x+3)**2-8', [1, -7]),
  ('10a', 'nsr', '(x-3)**2-6', [5.45, 0.55]),
  ('10b', 'nsr', '(x+1)**2-7', [1.65, -3.65]),
  ('10c', 'nsr', '(x+4)**2-3', [-2.27, -5.73]),
  ('10c Form', 'gl', 'x**2+8*x+13', '(x+4)**2-3'),
  ('11a', 'ns', '(x-3)**2-25', [8, -2]),
  ('11b', 'ns', '(x+2)**2-9', [1, -5]),
  ('12a', 'anz', '(x-4)**2+3', 0),
  ('12b', 'anz', '(x+2)**2-5', 2),
  ('12c', 'anz', '(x-6)**2', 1),
  ('12d', 'anz', '-(x-1)**2+2', 2),
  ('12e', 'anz', '-(x+3)**2-4', 0),
  ('13a', 'ns', 'x**2-6*x+8', [4, 2]),
  ('13b', 'ns', 'x**2+4*x+3', [-1, -3]),
  ('13c', 'ns', 'x**2-8*x+12', [6, 2]),
  ('13d', 'ns', 'x**2+10*x+9', [-1, -9]),
  ('14a', 'ns', 'x**2-2*x-8', [4, -2]),
  ('14b', 'ns', 'x**2+6*x-7', [1, -7]),
  ('14c', 'ns', 'x**2+x-6', [2, -3]),
  ('14d', 'ns', 'x**2-3*x-10', [5, -2]),
  ('15a', 'ns', 'x**2-10*x+25', [5]),
  ('15b', 'ns', 'x**2+8*x+16', [-4]),
  ('16a', 'ns', 'x**2+2*x+5', []),
  ('16b', 'ns', 'x**2-4*x+7', []),
  ('17a', 'ns', '2*x**2+4*x-30', [3, -5]),
  ('17b', 'ns', '-x**2-4*x+12', [2, -6]),
  ('17c', 'ns', 'Rational(1,2)*x**2+x-4', [2, -4]),
  ('17d', 'ns', '3*x**2+9*x+6', [-1, -2]),
  ('18a', 'nsr', 'x**2-4*x+1', [3.73, 0.27]),
  ('18b', 'nsr', 'x**2+2*x-4', [1.24, -3.24]),
  ('18c', 'nsr', 'x**2-10*x+14', [8.32, 1.68]),
  ('19a', 'ns', 'x**2-8*x+7', [7, 1]),
  ('19b', 'ns', '2*x**2+12*x+10', [-1, -5]),
  ('19c', 'ns', 'x**2+4*x-21', [3, -7]),
 ],
}

# Gegenprobe Fehler-finden: die Vorgaberechnung muss wirklich falsch sein
FALSCH = [
  ('11a Vorgabe', '(x-3)**2-25', [8]),
  ('11b Vorgabe', '(x+2)**2-9', [5, -1]),
  ('19a Vorgabe', 'x**2-8*x+7', [-1, -7]),
  ('19b Vorgabe', '2*x**2+12*x+10', [-0.90, -11.10]),
  ('19c Vorgabe', 'x**2+4*x-21', []),
]

teil = sys.argv[1]
zeilen, abw = [], 0
for nr, art, term, blatt in TEIL[teil]:
    if art == 'ns':
        s = reelle_nullstellen(term); ok = gerundet(s, 9) == gerundet(sorted(blatt, reverse=True), 9)
    elif art == 'nsr':
        s = gerundet(reelle_nullstellen(term)); ok = s == sorted(blatt, reverse=True)
    elif art == 'wert':
        s = float(N(sympify(term))); ok = abs(s - blatt) < 1e-9
    elif art == 'wertr':
        s = round(float(N(sympify(term))), 2); ok = abs(s - blatt) < 1e-9
    elif art == 'gl':
        s = str(sympify(term, locals={'x': x}).expand()); ok = simplify(sympify(term, locals={'x': x}) - sympify(blatt, locals={'x': x})) == 0
    elif art == 'anz':
        s = len(set(solve(sympify(term, locals={'x': x}), x))); ok = s == blatt
    if not ok: abw += 1
    zeilen.append(f"{nr}\tSkript: {s}\tBlatt: {blatt}\t{'OK' if ok else 'ABWEICHUNG'}")
if teil == 'e4':
    for nr, term, vorgabe in FALSCH:
        s = gerundet(reelle_nullstellen(term))
        falsch = s != sorted(vorgabe, reverse=True)
        if not falsch: abw += 1
        zeilen.append(f"{nr}\tSkript: {s}\tVorgabe: {vorgabe}\t{'OK (Vorgabe falsch)' if falsch else 'ABWEICHUNG (Vorgabe stimmt)'}")
zeilen.append(f"Abweichungen: {abw}")
out = '\n'.join(zeilen)
print(out)
open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8').write(out + '\n')
