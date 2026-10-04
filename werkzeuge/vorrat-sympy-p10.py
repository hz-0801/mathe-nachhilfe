#!/usr/bin/env python3
"""Sympy-Kontrolle der P10-Teilaufgaben 2022–2026 (Vorratslauf Block 1, 04.10.2026).

Je rechnerische Teilaufgabe eine Funktion, die den Katalogwert (ergebnis,
ggf. zwischenergebnis) nachrechnet und "ok" oder "abw: <eigener Wert>"
zurückgibt. Teilaufgaben ohne Funktion gelten als "nicht rechenbar"
(Begründen, Zeichnen, Ankreuzen ohne Rechenkern, Ablesen).

Aufruf: python3 werkzeuge/vorrat-sympy-p10.py [id ...]
Ohne Argument werden alle Funktionen ausgeführt und als "id;wert" ausgegeben.
Die Funktion ist nach der id benannt (Bindestriche als Unterstrich, Präfix p_).
"""
import sys
from sympy import (Rational as R, sqrt, symbols, solve, Eq, nsimplify, pi, sin,
                   cos, tan, asin, acos, atan, deg, rad, N, Abs, log, floor,
                   ceiling, binomial, factorial, Matrix, simplify, expand, S)

x, y, z, a, b, c, t = symbols("x y z a b c t")


def naeh(wert, soll, einheit="", tol=R(1, 20)):
    """Vergleich mit Toleranz (Rundung im Heft); Rückgabe ok/abw."""
    w = N(wert, 12)
    if Abs(w - soll) <= tol:
        return "ok"
    return "abw: " + str(round(float(w), 4)) + einheit


def genau(wert, soll, einheit=""):
    if simplify(nsimplify(wert) - nsimplify(soll)) == 0:
        return "ok"
    return "abw: " + str(nsimplify(wert)) + einheit


def grad(w):
    """Bogenmaß → Grad als Zahl."""
    return N(w * 180 / pi, 12)


# ---------- Teilstück 1/4 (Basis: 2025-OS-B1, 2026-FOR-B1, 2024-OS-B1, 2023-OS-B1)

def p_2025_OS_B1a():
    return genau(6 / R(20, 100), 30, " €")

def p_2025_OS_B1b():
    return genau(R(3, 2) * 60, 90, " min")

def p_2025_OS_B1d():
    return genau(log(850000 / R(85, 10), 10), 5)

def p_2025_OS_B1e():
    return naeh(R(145, 360) * 100, R(403, 10), " %")

def p_2025_OS_B1h():
    l = solve(Eq(x * (x + 5), -6), x)
    return "ok" if -2 in l and set(l) & {2, 3, -6} == set() else "abw: " + str(l)

def p_2026_FOR_B1a():
    return genau(R(30, 100) * 70, 21, " €")

def p_2026_FOR_B1b():
    return genau(R(120, 360), R(1, 3))

def p_2026_FOR_B1d():
    return "ok" if R(35, 10) * 100 > 35 else "abw: <="

def p_2026_FOR_B1e():
    w = [3 * k**2 for k in range(-2, 3)]
    return "ok" if w == [12, 3, 0, 3, 12] else "abw: " + str(w)

def p_2026_FOR_B1f():
    return genau(3**3, 27, " cm³")

def p_2026_FOR_B1g():
    return genau((5 * (x - 3)).subs(x, -2), -25)

def p_2026_FOR_B1h():
    return genau(2 * (R(35, 10) + R(15, 10)), 10, " cm")

def p_2026_FOR_B1i():
    return genau(180 - 75, 105, "°")

def p_2024_OS_B1a():
    return genau(R(325, 100) * 60, 195, " min")

def p_2024_OS_B1b():
    # Quadrat aus den Seitenmitten eines 4×4-Gitters: Diagonalen 4 und 4
    return genau(R(4 * 4, 2) / 16, R(1, 2))

def p_2024_OS_B1d():
    l = solve(Eq(2 * (x - R(65, 10)), 0), x)
    return genau(l[0], R(65, 10))

def p_2024_OS_B1e():
    return genau(R(350, 100) * R(12, 10), R(420, 100), " €")

def p_2024_OS_B1g():
    return genau(solve(Eq(4**x, 256), x)[0], 4)

def p_2024_OS_B1h():
    d = sorted([20, 17, 21, 18, 21, 11])
    return genau(R(d[2] + d[3], 2), 19, " °C")

def p_2024_OS_B1i():
    return genau((R(1, 2) * x - 1).subs(x, 0), -1)

def p_2023_OS_B1a():
    r = genau(R(25, 4), R(625, 100))
    return r if r != "ok" else genau(R(25, 4) * 6, R(375, 10), " min")

def p_2023_OS_B1b():
    return genau(200 / R(25, 100), 800, " €")

def p_2023_OS_B1c():
    return genau(R(42000, 400), 105, " mm")

def p_2023_OS_B1d():
    return genau(R(25, 100) * 24, 6)

def p_2023_OS_B1e():
    return genau(solve(Eq(3 * (x - 8) + 2, 2), x)[0], 8)

def p_2023_OS_B1f():
    w = {"4,4": R(44, 10), "0,44": R(44, 100), "0,4²": R(4, 10)**2, "44 %": R(44, 100)}
    k = min(w, key=w.get)
    return "ok" if k == "0,4²" and w[k] == R(16, 100) else "abw: " + k

def p_2023_OS_B1g():
    return genau(180 - 2 * 70, 40, "°")

def p_2023_OS_B1i():
    f = -7 * x + 3
    w = [f.subs(x, -1), f.subs(x, 3), f.subs(x, -4)]
    return "ok" if w == [10, -18, 31] else "abw: " + str(w)


# ---------- Ausführung

def alle():
    g = globals()
    return {k[2:].replace("_", "-"): g[k] for k in sorted(g) if k.startswith("p_")}


if __name__ == "__main__":
    fn = alle()
    ids = sys.argv[1:] or list(fn)
    for i in ids:
        if i in fn:
            try:
                print(i + ";" + fn[i]())
            except Exception as e:  # noqa: BLE001
                print(i + ";offen: " + type(e).__name__ + " " + str(e))
        else:
            print(i + ";nicht rechenbar")
