#!/usr/bin/env python3
# Rechnet die Ergebnisse von Blatt 0 unabhaengig nach und vergleicht mit den
# Werten aus blatt0_l.tex (Blattwerte von Hand eingetragen).
from fractions import Fraction as F
import math, sympy as sp

x = sp.Symbol('x')
zeilen = []
abw = 0

def pruef(nr, skript, blatt):
    global abw
    ok = str(skript).replace(' ', '') == str(blatt).replace(' ', '')
    if not ok:
        abw += 1
    zeilen.append(f"{nr:<8} Skript: {str(skript):<28} Blatt: {str(blatt):<28} "
                  f"{'OK' if ok else 'ABWEICHUNG'}")

# 1 Quadratzahlen
pruef("1a", 6**2, 36)
pruef("1b", 9**2, 81)
pruef("1c", float(F(4,10)**2), 0.16)
pruef("1d", (-7)**2, 49)
pruef("1e", -(7**2), -49)
pruef("1f", 3*4**2, 48)

# 2 Fehler finden
pruef("2-Fehler", (-9)**2, 81)
pruef("2a-1", (-12)**2, 144)
pruef("2a-2", -(12**2), -144)

# 3 Wurzeln
pruef("3a", int(math.isqrt(36)), 6)
pruef("3b", int(math.isqrt(81)), 9)
pruef("3c", int(math.isqrt(169)), 13)
pruef("3d", round(math.sqrt(7), 2), 2.65)
pruef("3e", round(math.sqrt(30), 2), 5.48)
pruef("3f", "keine", "keine")
pruef("3g", int(math.isqrt(0)), 0)

# 4 Gleichungen
for nr, gl, soll in [("4a", sp.Eq(x+7, 15), 8), ("4b", sp.Eq(x-5, 11), 16),
                     ("4c", sp.Eq(4*x, 28), 7), ("4d", sp.Eq(-x, 12), -12),
                     ("4e", sp.Eq(6*x, -42), -7), ("4f", sp.Eq(x+14, 5), -9)]:
    pruef(nr, sp.solve(gl, x)[0], soll)

# 5 Einsetzen pruefen
def wahr(links, rechts, wert):
    return sp.simplify(links.subs(x, wert) - rechts.subs(x, wert)) == 0
pruef("5a", wahr(3*x-5, sp.Integer(7), 4), True)
pruef("5b", wahr(x+9, sp.Integer(14), 6), False)
pruef("5c", wahr(x+11, sp.Integer(9), -3), False)
pruef("5d", wahr(x**2, sp.Integer(25), -5), True)
pruef("5e", wahr(x**2+3*x, sp.Integer(10), -2), False)
pruef("5f", wahr(x*(x+9), sp.Integer(-20), -4), True)

# 6 Scheitelpunktform: Scheitel und Oeffnung aus dem Term selbst bestimmt
def scheitel(term):
    t = sp.expand(term)
    a = sp.Poly(t, x).coeff_monomial(x**2)
    d = sp.nsimplify(-sp.Poly(t, x).coeff_monomial(x)/(2*a))
    e = sp.simplify(t.subs(x, d))
    return (d, e, "oben" if a > 0 else "unten")
pruef("6a", scheitel((x-3)**2+2), (3, 2, "oben"))
pruef("6b", scheitel((x-6)**2+1), (6, 1, "oben"))
pruef("6c", scheitel((x-2)**2-7), (2, -7, "oben"))
pruef("6d", scheitel((x+5)**2+3), (-5, 3, "oben"))
pruef("6e", scheitel(-(x-4)**2+6), (4, 6, "unten"))
pruef("6f", scheitel(x**2-12), (0, -12, "oben"))

# 7 Klammern
pruef("7a", 5*(3+4), 35)
pruef("7b", (-6)*(2+5), -42)
pruef("7c", (-4)*(-4+9), -20)
pruef("7d", (-3)*(-3-5), 24)
pruef("7e", 7*(7-12), -35)
pruef("7f", (-8)*(-8+8), 0)

# 8 Ausmultiplizieren / Ausklammern
pruef("8a", sp.expand(x*(x+6)), sp.expand(x**2+6*x))
pruef("8b", sp.expand(x*(x-9)), sp.expand(x**2-9*x))
pruef("8c", sp.expand((x+5)**2), sp.expand(x**2+10*x+25))
pruef("8d", sp.expand((x-7)**2), sp.expand(x**2-14*x+49))
pruef("8e", sp.expand((x+3)*(x-8)), sp.expand(x**2-5*x-24))
pruef("8f", sp.factor(x**2+11*x), sp.factor(x*(x+11)))
pruef("8g", sp.factor(x**2-6*x), sp.factor(x*(x-6)))

# 9 Terme ordnen
pruef("9a", sp.expand(x**2+4*x+9*x), sp.expand(x**2+13*x))
pruef("9b", sp.expand(3*x+x**2-8), sp.expand(x**2+3*x-8))
pruef("9c", sp.expand(x**2-7+5*x+12), sp.expand(x**2+5*x+5))
pruef("9d", sp.expand(2*x-x**2+9*x), sp.expand(-x**2+11*x))
pruef("9e", sp.expand(x**2+6*x-4-10*x), sp.expand(x**2-4*x-4))
pruef("9f", sp.expand(x**2-9*x+2*x-6), sp.expand(x**2-7*x-6))

# 10 Punkte (Grafikwerte aus dem Quelltext)
pruef("10a", (3, 5), (3, 5))
pruef("10b", (2, -4), (2, -4))
pruef("10c", (-6, 0), (-6, 0))
pruef("10d", (-4, 3), (-4, 3))
pruef("10e", (3, -2), (3, -2))
pruef("10f", (-2, -4), (-2, -4))

# 11 Geraden
pruef("11a", (2*x+1).subs(x, 3), 7)
pruef("11b", (-x+8).subs(x, 5), 3)
pruef("11c", (3*x-4).subs(x, -2), -10)
pruef("11d", sp.solve(sp.Eq(2*x+1, x+6), x)[0], 5)
pruef("11e", sp.solve(sp.Eq(3*x-5, -x+11), x)[0], 4)
xf = sp.solve(sp.Eq(-2*x+1, 4*x-17), x)[0]
pruef("11f", xf, 3)
pruef("11g", (xf, (4*xf-17)), (3, -5))

with open("pruef_out_blatt0.txt", "w") as f:
    f.write("\n".join(zeilen) + f"\nAbweichungen: {abw}\n")
print("\n".join(zeilen))
print(f"Abweichungen: {abw}")
