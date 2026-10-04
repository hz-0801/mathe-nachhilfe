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


# ---------- Teilstück 3/4 (Kontext: 2026-FOR-K4…K7, 2024-OS-K2…K7, 2023-OS-K2)

def p_2026_FOR_K4a():
    r = genau(32**2 - 13**2, 855)
    return r if r != "ok" else naeh(sqrt(855), R(292, 10), " cm")

def p_2026_FOR_K4b():
    return naeh(grad(acos(R(13, 32))), R(660, 10), "°")

def p_2026_FOR_K4c():
    h = sqrt(855)
    ac = h / sin(rad(22))
    r = naeh(ac, R(781, 10), " cm")
    return r if r != "ok" else naeh(h / tan(rad(22)), R(724, 10), " cm")

def p_2026_FOR_K5b():
    return genau((-2 * x + 2).subs(x, -4), 10)

def p_2026_FOR_K5c():
    p = (x - 2)**2 - 2
    return "ok" if p.subs(x, 2) == -2 and solve(p.diff(x), x) == [2] else "abw"

def p_2026_FOR_K5d():
    l = solve(Eq((x - 2)**2 - 2, -(x - 2)**2 - 2), x)
    return "ok" if l == [2] else "abw: " + str(l)

def p_2026_FOR_K6a():
    return genau(R((1, 1, 2, 2, 4, 5).count(2), 6), R(1, 3))

def p_2026_FOR_K6b():
    A, B = (1, 1, 2, 2, 4, 5), (1, 1, 2, 3, 3, 3)
    pa = R(sum(1 for v in A if v % 2 == 0), 6)
    pb = R(sum(1 for v in B if v % 2 == 0), 6)
    r = genau(pa, R(1, 2))
    if r != "ok": return r
    r = genau(pb, R(1, 6))
    return r if r != "ok" else genau((1 - pa) * (1 - pb), R(5, 12))

def p_2026_FOR_K6c():
    return genau(1 - R(3, 6) * R(1, 6), R(11, 12))

def p_2026_FOR_K6d():
    A, B = (1, 1, 2, 2, 4, 5), (1, 1, 1, 3, 3, 3)
    p = sum(R(1, 36) for u in A for v in B if u + v == 2)
    return genau(p, R(1, 6))

def p_2026_FOR_K7a():
    q = R(1019, 1000)
    r = naeh(650 * q, R(66235, 100), " €", tol=R(1, 200))
    if r != "ok": return r
    r = naeh(650 * q**2, R(67493, 100), " €", tol=R(1, 200))
    return r if r != "ok" else naeh(650 * q**3, R(68776, 100), " €", tol=R(1, 200))

def p_2026_FOR_K7c():
    q = R(1019, 1000)
    r = naeh(q**14, R(13015, 10000), "", tol=R(1, 20000))
    return r if r != "ok" else naeh(650 * q**14, R(84596, 100), " €", tol=R(1, 200))

def p_2024_OS_K2a():
    d = [R(v, 10) for v in (522, 396, 353, 192, 493, 851, 361, 824, 217, 546, 641, 421)]
    return genau(max(d) - min(d), R(659, 10), " mm")

def p_2024_OS_K2b():
    d = [R(v, 10) for v in (522, 396, 353, 192, 493, 851, 361, 824, 217, 546, 641, 421)]
    r = genau(sum(d), R(5817, 10))
    if r != "ok": return r
    m = sum(d) / 12
    r = naeh(m, R(485, 10), " mm")
    if r != "ok": return r
    r = naeh(R(485, 10) - R(192, 10), R(293, 10), " mm")
    return r if r != "ok" else naeh((R(485, 10) - R(192, 10)) / R(485, 10) * 100, R(604, 10), " %")

def p_2024_OS_K2c():
    r = naeh(R(60, 508) * 360, R(425, 10), "°", tol=R(1, 2))
    if r != "ok": return r
    r = naeh(R(12, 508), R(236, 10000), "", tol=R(1, 10000))
    return r if r != "ok" else naeh(R(12, 508) * 360, R(85, 10), "°")

def p_2024_OS_K2d():
    return genau(16 * R(14, 100), R(224, 100), " ct")

def p_2024_OS_K3b():
    p = x**2 - 4
    r = "ok" if sorted(solve(p, x)) == [-2, 2] and p.subs(x, 0) == -4 and p.subs(x, 3) == 5 else "abw"
    return r

def p_2024_OS_K3c():
    return genau((x**2 - 4).subs(x, -5), 21)

def p_2024_OS_K3d():
    l = sorted(solve(Eq(4 * x + 1, x**2 - 4), x))
    if l != [-1, 5]: return "abw: " + str(l)
    ys = [(4 * x + 1).subs(x, v) for v in l]
    return "ok" if ys == [-3, 21] else "abw: y " + str(ys)

def p_2024_OS_K4a():
    return naeh(pi * 30**2, R(28274, 10), " cm²")

def p_2024_OS_K4c():
    vz = pi * R(305, 10)**2 * 81
    vk = R(1, 3) * pi * 30**2 * 80
    r = naeh(vz, R(2367198, 10), " cm³", tol=R(1, 10))
    if r != "ok": return r
    r = naeh(vk, R(753982, 10), " cm³", tol=R(1, 10))
    return r if r != "ok" else naeh(vz - vk, 161322, " cm³", tol=R(1, 2))

def p_2024_OS_K5a():
    return genau(R(1, 5) * 100, 20, " %")

def p_2024_OS_K5b():
    return genau(R(1, 5) * R(1, 5), R(1, 25))

def p_2024_OS_K5c():
    return genau(R(4, 5) * R(1, 4), R(1, 5))

def p_2024_OS_K6a():
    r = genau(384**2 - 255**2, 82431)
    return r if r != "ok" else naeh(sqrt(82431), R(2871, 10), " m")

def p_2024_OS_K6b():
    return naeh(grad(acos(R(255, 384))), R(484, 10), "°")

def p_2024_OS_K6c():
    r = genau(384 / R(32, 10), 120, " s")
    return r if r != "ok" else genau(R(120, 60), 2, " min")

def p_2024_OS_K6d():
    g = 180 - 38 - 108
    r = genau(g, 34, "°")
    return r if r != "ok" else naeh(384 * sin(rad(38)) / sin(rad(g)), R(4228, 10), " m")

def p_2024_OS_K7a():
    l = solve([Eq(x + y, R(380, 100)), Eq(6 * x + 5 * y, R(2120, 100))], [x, y])
    return "ok" if l == {x: R(220, 100), y: R(160, 100)} else "abw: " + str(l)

def p_2024_OS_K7b():
    r_, t_ = symbols("r t")
    l = solve([Eq(R(230, 100) * r_ + R(170, 100) * t_, R(2690, 100)), Eq(r_ + t_, 13)], [r_, t_])
    return "ok" if l == {r_: 8, t_: 5} else "abw: " + str(l)

def p_2023_OS_K2a():
    return genau(180 - 56, 124, "°")

def p_2023_OS_K2b():
    r = genau((R(258, 10) + 15) / 2, R(204, 10), " m")
    return r if r != "ok" else genau((R(258, 10) + 15) / 2 * 8, R(1632, 10), " m²")

def p_2023_OS_K2c():
    s1 = 8 / sin(rad(56))
    s2 = sqrt(R(54, 10)**2 + 64)
    r = naeh(s1, R(965, 100), " m", tol=R(1, 100))
    if r != "ok": return r
    r = naeh(s2, R(965, 100), " m", tol=R(1, 100))
    return r if r != "ok" else naeh(15 + R(258, 10) + 2 * s1, R(601, 10), " m")


# ---------- Teilstück 4/4 (Kontext: 2023-OS-K3…K7, 2022-OS-K2…K7)

def p_2023_OS_K3b():
    a1 = 5 * 27 + (470 - 350) * R(36, 100)
    a2 = 120 + 470 * R(9, 100)
    r = genau(a1, R(17820, 100), " €")
    if r != "ok": return r
    r = genau(a2, R(16230, 100), " €")
    return r if r != "ok" else ("ok" if a2 < a1 else "abw: Angebot 1 günstiger")

def p_2023_OS_K4a():
    f = 4 * x - 2
    p = -(x + 1)**2 + 6
    l = sorted(solve(Eq(f, p), x))
    if l != [-7, 1]: return "abw: " + str(l)
    ys = [f.subs(x, v) for v in l]
    return "ok" if ys == [-30, 2] and f.subs(x, 0) == -2 else "abw: y " + str(ys)

def p_2023_OS_K4b():
    p = -(x + 1)**2 + 6
    return "ok" if p.subs(x, -1) == 6 and solve(p.diff(x), x) == [-1] else "abw"

def p_2023_OS_K4c():
    l = sorted(solve(Eq(-x**2 - 2 * x + 5, -10), x))
    r = "ok" if l == [-5, 3] else "abw: " + str(l)
    if r != "ok": return r
    return "ok" if expand(-(-x**2 - 2 * x + 5 + 10)) == x**2 + 2 * x - 15 else "abw: Normalform"

def p_2023_OS_K5a():
    return naeh(2 * pi * 4, R(251, 10), " cm")

def p_2023_OS_K5b():
    r = naeh(pi * 16, R(503, 10), " cm²")
    return r if r != "ok" else naeh(pi * 16 * 8, R(4021, 10), " cm³")

def p_2023_OS_K5c():
    n = floor(R(100, 8))
    r = genau(n, 12)
    if r != "ok": return r
    d = n * pi * 16
    r = naeh(d, R(6032, 10), " cm²")
    if r != "ok": return r
    ab = 800 - d
    r = naeh(ab, R(1968, 10), " cm²")
    if r != "ok": return r
    r = naeh(ab / 800 * 100, R(246, 10), " %")
    return r if r != "ok" else ("ok" if ab / 800 <= R(25, 100) else "abw: > 25 %")

def p_2023_OS_K5d():
    r = naeh(pi * 16, R(503, 10), " cm²")
    return r if r != "ok" else naeh(1000 / (pi * 16), R(199, 10), " cm")

def p_2023_OS_K6a():
    return naeh(R(125, 780) * 100, R(160, 10), " %")

def p_2023_OS_K6b():
    r = genau(R(39, 78), R(1, 2))
    return r if r != "ok" else genau(R(195, 780), R(1, 4))

def p_2023_OS_K6c():
    d = {"Arabisch": 290, "Chinesisch": 1300, "Englisch": 500, "Hindi": 525, "Spanisch": 389}
    if min(d, key=d.get) != "Arabisch" or max(d, key=d.get) != "Chinesisch": return "abw: Min/Max"
    return genau(max(d.values()) - min(d.values()), 1010, " Mio.")

def p_2023_OS_K6d():
    k = R(389, R(78, 10))
    r = naeh(k, 50, " Mio./Kästchen", tol=R(1, 2))
    if r != "ok": return r
    r = naeh(R(105, 10) * 50, 525, "", tol=R(1, 2))
    return r if r != "ok" else naeh(R(290, 50), R(58, 10), " Kästchen")

def p_2023_OS_K7a():
    return genau(180 - 90 - 45, 45, "°")

def p_2023_OS_K7b():
    bf = R(1315, 10) * sin(rad(45))
    af = R(1315, 10) * cos(rad(45))
    r = naeh(bf, R(930, 10), " cm")
    if r != "ok": return r
    r = naeh(af, R(930, 10), " cm")
    if r != "ok": return r
    r = naeh(cos(rad(65)), R(4226, 10000), "", tol=R(1, 10000))
    return r if r != "ok" else naeh(bf / cos(rad(65)), R(2200, 10), " cm")

def p_2022_OS_K2a():
    return naeh(2 * pi * R(32, 10), R(201, 10), " cm")

def p_2022_OS_K2b():
    r = naeh(pi * R(32, 10)**2, R(322, 10), " cm²")
    if r != "ok": return r
    v = pi * R(32, 10)**2 * 7
    r = naeh(v, R(2252, 10), " cm³")
    return r if r != "ok" else ("ok" if v > 200 else "abw: < 200")

def p_2022_OS_K2c():
    d = sqrt(7**2 + R(64, 10)**2)
    r = naeh(d, R(95, 10), " cm")
    return r if r != "ok" else naeh(d + 2, R(115, 10), " cm")

def p_2022_OS_K2d():
    r2 = 425 / (pi * 7)
    r = naeh(r2, R(1933, 100), "", tol=R(1, 100))
    return r if r != "ok" else naeh(sqrt(r2), R(440, 100), " cm", tol=R(1, 100))

def p_2022_OS_K3a():
    f = -2 * x + 3
    r = genau(solve(f, x)[0], R(3, 2))
    return r if r != "ok" else ("ok" if f.subs(x, 0) == 3 and f.subs(x, 1) == 1 else "abw: Punkte")

def p_2022_OS_K3b():
    p = (x - 2)**2 - 4
    return "ok" if p.subs(x, 2) == -4 and solve(p.diff(x), x) == [2] else "abw"

def p_2022_OS_K3c():
    f = -2 * x + 3
    l = sorted(solve(Eq((x - 2)**2 - 4, f), x))
    if l != [-1, 3]: return "abw: " + str(l)
    ys = [f.subs(x, v) for v in l]
    return "ok" if ys == [5, -3] else "abw: y " + str(ys)

def p_2022_OS_K4a():
    d = {2017: 468, 2018: 432, 2019: 485, 2020: 470, 2021: 400}
    if min(d, key=d.get) != 2021 or max(d, key=d.get) != 2019: return "abw: Min/Max"
    r = genau(sum(d.values()), 2255)
    return r if r != "ok" else genau(R(sum(d.values()), 5), 451)

def p_2022_OS_K4b():
    return naeh(R(470 - 400, 470) * 100, R(149, 10), " %")

def p_2022_OS_K4c():
    r = "ok" if 485 > 432 else "abw: kein Anstieg"
    if r != "ok": return r
    r = genau(432 - 400, 32)
    if r != "ok": return r
    r = naeh(R(32, 432) * 100, R(74, 10), " %")
    return r if r != "ok" else ("ok" if R(400, 432) > R(1, 2) else "abw: mehr als Hälfte")

def p_2022_OS_K4d():
    return genau(R(16, 100) * 360, R(576, 10), "°")

def p_2022_OS_K5a():
    q = R(141, 10)**2 - R(74, 10)**2
    r = genau(q, R(14405, 100))
    return r if r != "ok" else naeh(sqrt(q), R(120, 10), " m")

def p_2022_OS_K5b():
    r = naeh(R(74, 141), R(525, 1000), "", tol=R(1, 1000))
    return r if r != "ok" else naeh(grad(asin(R(74, 141))), R(317, 10), "°")

def p_2022_OS_K5c():
    return naeh(90 - grad(asin(R(74, 141))), R(583, 10), "°")

def p_2022_OS_K5d():
    r = naeh(sin(rad(52)), R(788, 1000), "", tol=R(1, 1000))
    return r if r != "ok" else naeh(R(74, 10) / sin(rad(52)), R(94, 10), " m")

def p_2022_OS_K5e():
    db = R(74, 10) / tan(rad(52))
    ad = sqrt(R(141, 10)**2 - R(74, 10)**2)
    r = naeh(db, R(58, 10), " m")
    if r != "ok": return r
    c = ad + db
    r = naeh(c, R(178, 10), " m")
    return r if r != "ok" else naeh(c * R(74, 10) / 2, R(658, 10), " m²")

def p_2022_OS_K6a():
    r = genau(12 * 22, 264)
    if r != "ok": return r
    r = genau(1472 + 264, 1736, " €")
    return r if r != "ok" else genau(990 + 12 * 55, 1650, " €")

def p_2022_OS_K6b():
    g = solve(Eq(55 * x + 990, 2000), x)[0]
    r = naeh(g, R(1836, 100), "", tol=R(1, 100))
    return r if r != "ok" else genau(ceiling(g), 19, " Monate")

def p_2022_OS_K7b():
    l = solve([Eq(x + y, 63), Eq(9 * x + 3 * y, R(35220, 100))], [x, y])
    r = "ok" if l == {x: R(2720, 100), y: R(3580, 100)} else "abw: " + str(l)
    return r if r != "ok" else genau(R(35220, 100) - 189, R(16320, 100))


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
