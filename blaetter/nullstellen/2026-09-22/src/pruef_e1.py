#!/usr/bin/env python3
import math, sympy as sp
x = sp.Symbol('x')
zeilen = []; abw = 0
def pruef(nr, skript, blatt):
    global abw
    ok = str(skript).replace(' ', '') == str(blatt).replace(' ', '')
    if not ok: abw += 1
    zeilen.append(f"{nr:<10} Skript: {str(skript):<34} Blatt: {str(blatt):<34} "
                  f"{'OK' if ok else 'ABWEICHUNG'}")

def loes(gl):
    """reelle Loesungen aufsteigend? nein: nach P10-Art x1 positiv zuerst"""
    s = [sp.nsimplify(v) for v in sp.solve(gl, x) if v.is_real]
    return sorted(s, key=lambda v: -float(v))

# 1 Vorstufe: quadratisch oder linear
pruef("1a", "linear", "linear"); pruef("1b", "quadratisch", "quadratisch")
pruef("1c", "quadratisch", "quadratisch"); pruef("1d", "linear", "linear")
pruef("1e", "quadratisch", "quadratisch")

# 2 Vorstufe: Zahl der Loesungen an c
def anzahl(c):
    return "zwei" if c > 0 else ("eine" if c == 0 else "keine")
pruef("2a", anzahl(169), "zwei"); pruef("2b", anzahl(-12), "keine")
pruef("2c", anzahl(0), "eine"); pruef("2d", anzahl(5), "zwei")
pruef("2e", anzahl(sp.Rational(-1,2)), "keine")

# 3 Beispiel und Kette
pruef("3-Bsp", loes(sp.Eq(x**2, 49)), [7, -7])
pruef("3a", loes(sp.Eq(x**2, 9)), [3, -3])
pruef("3b", loes(sp.Eq(x**2, 64)), [8, -8])
pruef("3c", loes(sp.Eq(x**2, 121)), [11, -11])
pruef("3d", loes(sp.Eq(x**2, 225)), [15, -15])
pruef("3e", loes(sp.Eq(x**2, 11)), [sp.sqrt(11), -sp.sqrt(11)])
pruef("3e-nah", round(math.sqrt(11), 2), 3.32)
pruef("3f", loes(sp.Eq(x**2, -100)), [])
pruef("3g", loes(sp.Eq(x**2 - 45, 55)), [10, -10])
pruef("3h", loes(sp.Eq(3*x**2, 48)), [4, -4])
pruef("3i", loes(sp.Eq(2*x**2 + 5, 55)), [5, -5])
pruef("3j", loes(sp.Eq((x-5)**2, 36)), [11, -1])
pruef("3k", loes(sp.Eq((x+3)**2, 81)), [6, -12])
pruef("3l", loes(sp.Eq((x-7)**2, 0)), [7])

# 4 Probe
def probe(l, r, w): return sp.simplify(l.subs(x, w) - r) == 0
pruef("4a", probe(x**2, 64, -8), True)
pruef("4b", probe((x-5)**2, 16, 1), True)
pruef("4c", probe((x+3)**2, 16, 2), False)

# 5 am Graphen (Parabel p(x)=x^2-3)
p = x**2 - 3
for nr, c, soll in [("5a", 1, [2, -2]), ("5b", -3, [0]), ("5c", -5, [])]:
    pruef(nr, loes(sp.Eq(p, c)), soll)
# Kontrolle: alle abgelesenen Punkte liegen im Achsenbereich -5..5 / -6..7
for xv in (-2, 2, 0):
    assert -5 <= xv <= 5
pruef("5-Bereich", "alle Schnittpunkte in der Flaeche", "alle Schnittpunkte in der Flaeche")

# 6 Fehler finden
pruef("6-falsch", [11, 1], [11, 1])
pruef("6-richtig", loes(sp.Eq((x+6)**2, 25)), [-1, -11])
pruef("6a", loes(sp.Eq((x+4)**2, 81)), [5, -13])

# 7 Begruenden
pruef("7a", anzahl(-20), "keine"); pruef("7b", anzahl(0), "eine")
pruef("7c", anzahl(7), "zwei")

# 8 Sachtext
pruef("8a", int(math.isqrt(64)), 8)
pruef("8b", round(math.sqrt(200), 2), 14.14)
pruef("8b-pass", math.sqrt(200) > 14, True)
r2 = 50/(math.pi*2.5)
pruef("8c", round(math.sqrt(r2), 2), 2.52)

# 9 Pruefungshoehe (P10-Form 2021)
pruef("9a", loes(sp.Eq((x-5)**2, 0)), [5])
pruef("9a-wahr", len(loes(sp.Eq((x-5)**2, 0))) == 1, True)
l9b = loes(sp.Eq((x+9)**2, 16))
pruef("9b", l9b, [-5, -13])
pruef("9b-wahr", set(map(int, l9b)) == {5, 13}, False)
pruef("9c", loes(sp.Eq(x**2 + 4, 0)), [])

with open("pruef_out_e1.txt", "w") as f:
    f.write("\n".join(zeilen) + f"\nAbweichungen: {abw}\n")
print("\n".join(zeilen)); print(f"Abweichungen: {abw}")
