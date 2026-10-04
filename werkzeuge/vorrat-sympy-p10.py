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


# ---------- Teilstück 2/4 (Basis: 2022-OS-B1; Kontext: 2025-OS-K2…K7, 2026-FOR-K2, K3)

def p_2022_OS_B1a():
    return genau(R(20, 100) * 15, 3)

def p_2022_OS_B1b():
    r = genau(R(480, 100) / 3, R(160, 100))
    return r if r != "ok" else genau(R(480, 100) / 3 * 5, 8, " €")

def p_2022_OS_B1c():
    return genau(solve(Eq(5 - 2 * x, 3 * x - 25), x)[0], 6)

def p_2022_OS_B1d():
    w = [21, 20, 19, 22, 20, 20]
    r = genau(sum(w), 122)
    return r if r != "ok" else genau(7 * 20 - sum(w), 18, " °C")

def p_2022_OS_B1f():
    return genau(R(1, 5) * 100, 20, " %")

def p_2022_OS_B1h():
    return genau(floor(R(1500, 300)), 5)

def p_2022_OS_B1j():
    r = genau(R(2)**-5, R(3125, 100000))
    return r if r != "ok" else ("ok" if R(2)**-5 < R(25, 100) else "abw: >=")

def p_2025_OS_K2a():
    bf = 80 - 25
    ab2 = 25**2 + bf**2
    r = genau(bf, 55, " cm")
    if r != "ok": return r
    r = genau(ab2, 3650)
    return r if r != "ok" else naeh(sqrt(ab2), R(604, 10), " cm")

def p_2025_OS_K2b():
    return genau(R(50 * 80, 2), 2000, " cm²")

def p_2025_OS_K2c():
    # Umkehrung Pythagoras: AD² + DC² = AC²; Basiswinkel im gleichschenklig-rechtwinkligen Dreieck
    ad2 = 25**2 + 25**2
    r = genau(ad2 + ad2, 50**2)
    if r != "ok": return r
    r = naeh(sqrt(ad2), R(354, 10), " cm")
    return r if r != "ok" else genau(2 * grad(atan(R(25, 25))), 90, "°")

def p_2025_OS_K3a():
    m = sorted({f"{l}{r}" for l in (1, 2, 1, 3) for r in (2, 3, 2, 1)})
    return "ok" if m == ["11", "12", "13", "21", "22", "23", "31", "32", "33"] else "abw: " + str(m)

def p_2025_OS_K3b():
    li, re = (1, 2, 1, 3), (2, 3, 2, 1)
    p = lambda a, b: R(li.count(a), 4) * R(re.count(b), 4)
    r = genau(p(3, 3), R(1, 16))
    return r if r != "ok" else genau(p(2, 2), R(1, 8))

def p_2025_OS_K3c():
    li, re = (1, 2, 1, 3), (2, 3, 2, 1)
    p = lambda a, b: R(li.count(a), 4) * R(re.count(b), 4)
    r = genau(p(1, 2) + p(2, 1), R(5, 16))
    return r if r != "ok" else genau(R(5, 16) * 100, R(3125, 100), " %")

def p_2025_OS_K3d():
    return genau(R(2, 4) * R(2, 4), R(1, 4))

def p_2025_OS_K4a():
    r = genau(170**2 + 16**2, 29156)
    if r != "ok": return r
    r = naeh(sqrt(29156), R(1708, 10), " cm")
    return r if r != "ok" else naeh(grad(atan(R(16, 170))), R(54, 10), "°")

def p_2025_OS_K4b():
    r = naeh(R(16, 170) * 100, R(94, 10), " %")
    return r if r != "ok" else ("ok" if R(16, 170) > R(6, 100) else "abw: nicht zu steil")

def p_2025_OS_K4c():
    g = 180 - 5 - 141
    r = genau(g, 34, "°")
    return r if r != "ok" else naeh(160 * sin(rad(141)) / sin(rad(34)), R(1801, 10), " cm")

def p_2025_OS_K5a():
    m = (R(-15, 10) - 6) / (3 - (-2))
    n = 6 - m * (-2)
    r = genau(m, R(-15, 10))
    if r != "ok": return r
    r = genau(n, 3)
    return r if r != "ok" else ("ok" if m < 0 else "abw: steigend")

def p_2025_OS_K5b():
    p = x**2 - 6 * x + 7
    r = genau(expand((x - 3)**2 - 2) - p, 0)
    return r if r != "ok" else genau(p.subs(x, 3), -2)

def p_2025_OS_K5c():
    l = sorted(solve(Eq(x**2 - 6 * x + 7, 0), x))
    if l != [3 - sqrt(2), 3 + sqrt(2)]: return "abw: " + str(l)
    r = naeh(l[0], R(159, 100))
    return r if r != "ok" else naeh(l[1], R(441, 100))

def p_2025_OS_K6a():
    d = [5, 2, 1, 4, 2, 4, 2, 4, 2, 2]
    r = genau(max(d) - min(d), 4)
    if r != "ok": return r
    modal = max(set(d), key=d.count)
    return "ok" if modal == 2 and d.count(2) == 5 and d.count(4) == 3 else "abw: Modalwert " + str(modal)

def p_2025_OS_K6b():
    d = [52, 57, 33, 44, 31, 30, 66, 58, 61, 41, 55]
    k = sum(1 for v in d if v < 50)
    r = genau(k, 5)
    if r != "ok": return r
    r = naeh(R(k, 11) * 100, R(455, 10), " %")
    return r if r != "ok" else naeh(R(k, 11) * 360, R(1636, 10), "°")

def p_2025_OS_K6c():
    d = [52, 57, 33, 44, 31, 30, 66, 58, 61, 41, 55]
    r = genau(sum(d), 528)
    if r != "ok": return r
    r = genau(R(sum(d), 11), 48, " Jahre")
    return r if r != "ok" else genau(R(sum(d) - 66 - 30, 9), 48, " Jahre")

def p_2025_OS_K7b():
    w = [80, 112, 157, 220, 308]
    r = genau(R(112, 80), R(14, 10))
    if r != "ok": return r
    q = [N(R(w[i + 1], w[i]), 3) for i in range(4)]
    if any(Abs(v - R(14, 10)) > R(1, 50) for v in q): return "abw: Quotienten " + str(q)
    r = naeh(R(14, 10)**24, R(32142, 10), " ", tol=R(1, 10))
    return r if r != "ok" else naeh(80 * R(14, 10)**24, 257136, "", tol=R(1, 2))

def p_2026_FOR_K2a():
    return naeh(pi * R(47, 10)**2 * 25, R(17349, 10), " m³")

def p_2026_FOR_K2b():
    m = pi * R(47, 10) * R(86, 10)
    r = naeh(m, R(12698, 100), " m²", tol=R(1, 100))
    return r if r != "ok" else naeh(m * 20, R(253966, 100), " €", tol=R(1, 100))

def p_2026_FOR_K2c():
    h = sqrt(R(86, 10)**2 - R(47, 10)**2)
    r = genau(R(86, 10)**2 - R(47, 10)**2, R(5187, 100))
    if r != "ok": return r
    r = naeh(h, R(720, 100), " m", tol=R(1, 100))
    return r if r != "ok" else naeh(25 + h, R(322, 10), " m")

def p_2026_FOR_K2d():
    r_, h_ = symbols("r h", positive=True)
    vk = R(1, 3) * pi * (3 * r_)**2 * h_
    vz = pi * r_**2 * h_
    return genau(simplify(vk / vz), 3)

def p_2026_FOR_K3a():
    return genau(R(185, 100) - R(177, 100), R(8, 100), " €/l")

def p_2026_FOR_K3b():
    s = R(177 + 178 + 177 + 179 + 184, 100)
    r = genau(s, R(895, 100))
    return r if r != "ok" else genau(s / 5, R(179, 100), " €")

def p_2026_FOR_K3c():
    return naeh((R(184, 100) - R(179, 100)) / R(179, 100) * 100, R(28, 10), " %")


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
