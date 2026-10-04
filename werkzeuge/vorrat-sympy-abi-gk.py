#!/usr/bin/env python3
"""Rechenkontrolle für die Beitabelle abitur/vorrat-abi-gk-2022-2026.csv.

Je rechenbarer Teilaufgabe eine Funktion, eingetragen unter ihrer id in
PRUEF; sie gibt "ok" oder "abw: <eigener Wert>" zurück. Teilaufgaben ohne
rechnerisches Ergebnis (Begründen, Zeichnen, Deuten, Ablesen) stehen in
NICHT_RECHENBAR mit Grund. Ergebnisse werden gegen den Katalogwert
verglichen, der im Kopf jeder Funktion als Kommentar steht.

Aufruf: python3 werkzeuge/vorrat-sympy-abi-gk.py [id ...]
Ohne ids werden alle Funktionen ausgeführt; Ausgabe je Zeile "id;wert".
"""
import sys
import math
from sympy import (symbols, Rational as R, sqrt, exp, E, diff, solve, limit,
                   oo, integrate, Matrix, binomial, atan, pi, factor, nsimplify,
                   simplify, Abs, log, ln, S, Eq, expand, Interval, Union, Poly,
                   Piecewise, floor, ceiling, N, Symbol, re, im, Max, Min)
from sympy.stats import Binomial, density, P, E as EW, Hypergeometric, Normal

x, y, z, t, s, r, a, b, k, u = symbols('x y z t s r a b k u', real=True)

PRUEF = {}
NICHT_RECHENBAR = {}


def pruef(id_):
    def deko(f):
        PRUEF[id_] = f
        return f
    return deko


def nr(id_, grund):
    NICHT_RECHENBAR[id_] = grund


def near(wert, soll, tol=5e-3):
    return abs(float(wert) - float(soll)) <= tol


def ok(bed, wert):
    return "ok" if bed else f"abw: {wert}"


def binom_p(n, p, kmin, kmax):
    return sum(binomial(n, i) * R(p)**i * (1 - R(p))**(n - i) for i in range(kmin, kmax + 1))


# Normalverteilung ohne scipy: Phi über erf
def Phi(zz):
    return 0.5 * (1 + math.erf(float(zz) / math.sqrt(2)))


# ======================= Teilstück 1 (2023-bebb-gk) ==========================

@pruef("2023-bebb-gk-A1.1a")
def _():
    # t2: y = −4/3 x + 4 (Spiegelung von t1 an der y-Achse)
    t1 = R(4, 3) * x + 4
    t2 = t1.subs(x, -x)
    return ok(simplify(t2 - (-R(4, 3) * x + 4)) == 0, t2)


@pruef("2023-bebb-gk-A1.1b")
def _():
    # Umfang 16
    t1 = R(4, 3) * x + 4
    n1 = solve(t1, x)[0]
    schenkel = sqrt(n1**2 + 4**2)
    U = 2 * abs(n1) + 2 * schenkel
    return ok(U == 16, U)


nr("2023-bebb-gk-A1.2a", "Näherungswert aus der Abbildung")
nr("2023-bebb-gk-A1.2b", "Skizze")


@pruef("2023-bebb-gk-A1.3a")
def _():
    # Extremstellen 0 und 2
    f = x**3 - 3 * x**2
    L = sorted(solve(diff(f, x), x))
    return ok(L == [0, 2], L)


@pruef("2023-bebb-gk-A1.3b")
def _():
    # f(−1) = g(−1) = −4, f'(−1) = 9
    f = x**3 - 3 * x**2
    g = 9 * x + 5
    w = (f.subs(x, -1), g.subs(x, -1), diff(f, x).subs(x, -1))
    return ok(w == (-4, -4, 9), w)


@pruef("2023-bebb-gk-A1.4a")
def _():
    # A nicht auf g
    g = Matrix([2, 3, -7]) + s * Matrix([1, 0, 5])
    L = solve(list(g - Matrix([4, 0, 0])), s)
    return ok(L == [], L)


@pruef("2023-bebb-gk-A1.4b")
def _():
    # b = 6, Schnittpunkt (7 | 3 | 18)
    g = Matrix([2, 3, -7]) + s * Matrix([1, 0, 5])
    h = Matrix([4, 0, 0]) + r * Matrix([1, 1, b])
    L = solve(list(g - h), [s, r, b], dict=True)[0]
    Pk = g.subs(L)
    return ok(L[b] == 6 and list(Pk) == [7, 3, 18], (L, list(Pk)))


@pruef("2023-bebb-gk-A1.5a")
def _():
    # |CA| = |CB| = √27
    A, B, C = Matrix([1, 0, 2]), Matrix([3, 2, 10]), Matrix([4, 3, 5])
    w = ((A - C).norm(), (B - C).norm())
    return ok(w == (sqrt(27), sqrt(27)), w)


@pruef("2023-bebb-gk-A1.5b")
def _():
    # D(0 | −1 | 7)
    A, B, C = Matrix([1, 0, 2]), Matrix([3, 2, 10]), Matrix([4, 3, 5])
    D = A + B - C
    bed = list(D) == [0, -1, 7] and (D - A).norm() == (D - B).norm() == (C - A).norm()
    return ok(bed, list(D))


@pruef("2023-bebb-gk-A1.6a")
def _():
    # 13/25
    p = R(3, 5)**2 + R(2, 5)**2
    return ok(p == R(13, 25), p)


@pruef("2023-bebb-gk-A1.6b")
def _():
    # 7/10
    p = (binomial(3, 2) * binomial(2, 1) + binomial(3, 3)) / binomial(5, 3)
    return ok(p == R(7, 10), p)


@pruef("2023-bebb-gk-A1.7a")
def _():
    # ≈ 0,29 (0,28 bis 0,30), Verteilung B(12; 0,25)
    p = binom_p(12, R(1, 4), 4, 5)
    return ok(0.28 <= float(p) <= 0.30 + 1e-9, float(p))


@pruef("2023-bebb-gk-A1.7b")
def _():
    # E(Y) = 3, Maximum bei k = 3
    n, p = 12, R(1, 4)
    ps = [binom_p(n, p, i, i) for i in range(13)]
    return ok(n * p == 3 and ps.index(max(ps)) == 3, (n * p, ps.index(max(ps))))


f23 = R(1, 2) * (x**2 - 4) * exp(x)


@pruef("2023-bebb-gk-B2.1a")
def _():
    # f → +∞ (x → +∞), f → 0 (x → −∞)
    w = (limit(f23, x, oo), limit(f23, x, -oo))
    return ok(w == (oo, 0), w)


@pruef("2023-bebb-gk-B2.1b")
def _():
    # (0 | −2), (±2 | 0); R(0 | 2)
    w = (f23.subs(x, 0), sorted(solve(f23, x)))
    return ok(w == (-2, [-2, 2]), w)


@pruef("2023-bebb-gk-B2.1c")
def _():
    # f'(−1+√5) = 0; f(−1+√5) ≈ −4,25
    x0 = -1 + sqrt(5)
    w = (simplify(diff(f23, x).subs(x, x0)), f23.subs(x, x0))
    return ok(w[0] == 0 and near(w[1], -4.25) and simplify(w[1] - (1 - sqrt(5)) * exp(sqrt(5) - 1)) == 0, (w[0], float(w[1])))


@pruef("2023-bebb-gk-B2.1d")
def _():
    # f(−0,9+√5) ≈ −4,21 > −4,25; f'(−0,9+√5) ≈ 0,87 > 0
    x1 = R(-9, 10) + sqrt(5)
    w = (float(f23.subs(x, x1)), float(diff(f23, x).subs(x, x1)))
    return ok(near(w[0], -4.21) and near(w[1], 0.87) and w[0] > -4.2546 and w[1] > 0, w)


@pruef("2023-bebb-gk-B2.1e")
def _():
    # f' < 0 auf (0; −1+√5), f' > 0 danach
    fs = diff(f23, x)
    w = (float(fs.subs(x, R(1, 2))), float(fs.subs(x, 3)), float(-1 + sqrt(5)))
    return ok(w[0] < 0 and w[1] > 0 and near(w[2], 1.24), w)


@pruef("2023-bebb-gk-B2.1f")
def _():
    # W1(−4,45 | 0,09), W2(0,45 | −2,98); f'' = (0,5x²+2x−1)e^x
    f2 = diff(f23, x, 2)
    bed = simplify(f2 - (R(1, 2) * x**2 + 2 * x - 1) * exp(x)) == 0
    xs = sorted(solve(f2, x))
    w = [(round(float(xi), 2), round(float(f23.subs(x, xi)), 2)) for xi in xs]
    return ok(bed and w == [(-4.45, 0.09), (0.45, -2.98)], w)


@pruef("2023-bebb-gk-B2.1g")
def _():
    # Tangente Achsenabschnitte −0,86 / −1,96; Normale 7,21 / −3,17; Steigung ≈ −2,27
    xw = -2 + sqrt(6)
    yw = f23.subs(x, xw)
    m = diff(f23, x).subs(x, xw)
    tg = m * (x - xw) + yw
    nm = -1 / m * (x - xw) + yw
    w = [float(solve(tg, x)[0]), float(tg.subs(x, 0)), float(solve(nm, x)[0]), float(nm.subs(x, 0)), float(m)]
    soll = [-0.86, -1.96, 7.21, -3.17, -2.27]
    return ok(all(near(p, q, 6e-3) for p, q in zip(w, soll)), [round(v, 2) for v in w])


nr("2023-bebb-gk-B2.1h", "geometrische Deutung")


@pruef("2023-bebb-gk-B2.1i")
def _():
    # g(x) = f(−x), h(x) = −f(x), k(x) = −f(−x)
    g = f23.subs(x, -x)
    bed = simplify(g - R(1, 2) * (x**2 - 4) * exp(-x)) == 0
    return ok(bed, g)


@pruef("2023-bebb-gk-B2.1j")
def _():
    # ≈ 30,3°; f'(−2) = −2e^(−2)
    m = diff(f23, x).subs(x, -2)
    w = float(2 * atan(abs(m)) * 180 / pi)
    return ok(simplify(m + 2 * exp(-2)) == 0 and near(w, 30.3, 0.05), w)


@pruef("2023-bebb-gk-B2.1k")
def _():
    # 180 l
    V = 4 * 15 * 4 * 15 * 50
    return ok(V == 180000, V)


@pruef("2023-bebb-gk-B2.1l")
def _():
    # F(x) = (0,5x² − x − 1)e^x; A ≈ 5,62 LE² ≈ 1265 cm²
    F = (R(1, 2) * x**2 - x - 1) * exp(x)
    bed = simplify(diff(F, x) - f23) == 0
    I = integrate(f23, (x, -2, 0))
    A = 4 * abs(I)
    w = (float(I), float(A), float(A) * 225)
    return ok(bed and near(w[0], -1.406) and near(w[1], 5.62) and near(w[2], 1265, 1), w)


@pruef("2023-bebb-gk-B2.1m")
def _():
    # Zuwachs 8(1 − 3e^(−2)) LE² ≈ 4,75 LE² ≈ 1069 cm²; je Quadrant ≈ 0,594
    I = integrate(f23, (x, -2, 0))
    seg = 2 - abs(I)
    Z = 8 * seg
    w = (float(seg), float(Z), float(Z) * 225)
    return ok(near(w[0], 0.594) and near(w[1], 4.75) and near(w[2], 1069, 1), w)


f22 = x**3 - 12 * x**2 + 45 * x - 50
g22 = R(2, 5) * x**3 - 6 * x**2 + 30 * x - 50


@pruef("2023-bebb-gk-B2.2a")
def _():
    # (0 | −50); Nullstellen 2 und 5 (doppelt)
    w = (f22.subs(x, 0), factor(f22), sorted(set(solve(f22, x))))
    return ok(w[0] == -50 and w[1] == (x - 5)**2 * (x - 2) and w[2] == [2, 5], w)


@pruef("2023-bebb-gk-B2.2b")
def _():
    # H(3 | 4), T(5 | 0)
    f1, f2 = diff(f22, x), diff(f22, x, 2)
    xs = sorted(solve(f1, x))
    w = [(xi, f22.subs(x, xi), f2.subs(x, xi)) for xi in xs]
    return ok(w == [(3, 4, -6), (5, 0, 6)], w)


@pruef("2023-bebb-gk-B2.2c")
def _():
    # W(4 | 2)
    xs = solve(diff(f22, x, 2), x)
    w = (xs, f22.subs(x, 4))
    return ok(xs == [4] and w[1] == 2, w)


@pruef("2023-bebb-gk-B2.2d")
def _():
    # (12 | 490), t: y = 45x − 50
    tg = diff(f22, x).subs(x, 0) * x + f22.subs(x, 0)
    xs = sorted(set(solve(f22 - tg, x)))
    w = (tg, xs, f22.subs(x, 12))
    return ok(tg == 45 * x - 50 and xs == [0, 12] and w[2] == 490, w)


@pruef("2023-bebb-gk-B2.2e")
def _():
    # Wendetangente y = −3x + 14 trifft nur in W; f(7) = 20
    wt = diff(f22, x).subs(x, 4) * (x - 4) + f22.subs(x, 4)
    xs = set(solve(f22 - wt, x))
    w = (wt, xs, f22.subs(x, 7))
    return ok(wt == -3 * x + 14 and xs == {4} and w[2] == 20, w)


@pruef("2023-bebb-gk-B2.2f")
def _():
    # g'(x) = 1,2(x − 5)²
    g1 = diff(g22, x)
    return ok(simplify(g1 - R(6, 5) * (x - 5)**2) == 0, g1)


@pruef("2023-bebb-gk-B2.2g")
def _():
    # f − g = 0,6x(x − 5)²; L = (0;5) ∪ (5;∞)
    d = factor(f22 - g22)
    bed = simplify(d - R(3, 5) * x * (x - 5)**2) == 0
    L = solve(f22 - g22 > 0, x)
    probe = all(bool(L.subs(x, v)) for v in (R(1, 2), 3, 7)) and not any(bool(L.subs(x, v)) for v in (-1, 0, 5))
    return ok(bed and probe, (d, L))


nr("2023-bebb-gk-B2.2h", "Ablesewert aus der Abbildung")


@pruef("2023-bebb-gk-B2.2i")
def _():
    # 975/5 = 195
    h = 4 * x**3 - 48 * x**2 + 180 * x + 20
    I = integrate(h, (x, 0, 5))
    return ok(I == 975 and I / 5 == 195, I)


# ======================= Teilstück 2 (2023 B2.2j – 2024 A1.8a) ================

@pruef("2023-bebb-gk-B2.2j")
def _():
    # c = 4, d = 55
    c, d = symbols('c d')
    h = 4 * x**3 - 48 * x**2 + 180 * x + 20
    L = solve(Poly(c * (f22 + d) - h, x).coeffs(), [c, d], dict=True)
    return ok(L == [{c: 4, d: 55}], L)


@pruef("2023-bebb-gk-B2.2k")
def _():
    # k(x) = 2x³ − 28x² + 130x + 20
    A, B, C, D = symbols('A B C D')
    kf = A * x**3 + B * x**2 + C * x + D
    L = solve([kf.subs(x, 0) - 20, diff(kf, x).subs(x, 0) - 130, kf.subs(x, 5) - 220, diff(kf, x).subs(x, 5)], [A, B, C, D])
    return ok(L == {A: 2, B: -28, C: 130, D: 20}, L)


A3, B3, C3 = Matrix([4, 0, 0]), Matrix([0, 4, 0]), Matrix([0, 0, 4])


@pruef("2023-bebb-gk-B3a")
def _():
    # gleichseitig 4√2; G(3 | 0 | 1)
    L = ((A3 - B3).norm(), (B3 - C3).norm(), (A3 - C3).norm())
    G = A3 + R(1, 4) * (C3 - A3)
    return ok(L == (4 * sqrt(2),) * 3 and list(G) == [3, 0, 1], (L, list(G)))


@pruef("2023-bebb-gk-B3b")
def _():
    # L1 ∥ L2, A ∉ L2
    n1, n2 = Matrix([1, 1, 1]), Matrix([2, 2, 2])
    return ok(n1.cross(n2).norm() == 0 and 2 * 4 != 5, "")


@pruef("2023-bebb-gk-B3c")
def _():
    # |BE| = 1,5 > Abstand 1,5/√3 ≈ 0,87
    d_eb = (Matrix([0, 4, 0]) - Matrix([0, R(5, 2), 0])).norm()
    d_eben = abs(4 - R(5, 2)) / sqrt(3)
    return ok(d_eb == R(3, 2) and near(d_eben, 0.87) and d_eb > d_eben, (d_eb, float(d_eben)))


@pruef("2023-bebb-gk-B3d")
def _():
    # Q(0,5 | 0,5 | 1,5), t = 1/4
    g = Matrix([0, 0, 2]) + t * Matrix([2, 2, -2])
    tt = solve(2 * g[0] + 2 * g[1] + 2 * g[2] - 5, t)[0]
    Q = g.subs(t, tt)
    return ok(tt == R(1, 4) and list(Q) == [R(1, 2), R(1, 2), R(3, 2)], (tt, list(Q)))


@pruef("2023-bebb-gk-B3e")
def _():
    # α ≈ 54,7°
    from sympy import acos
    al = float(acos(1 / sqrt(3)) * 180 / pi)
    return ok(near(al, 54.7, 0.05), al)


@pruef("2023-bebb-gk-B3f")
def _():
    # 3 < 4 und 6 > 5
    return ok(1 + 1 + 1 < 4 and 2 * 3 > 5, "")


@pruef("2023-bebb-gk-B3g")
def _():
    # k = 2,5; V = 129/16 ≈ 8,06
    V = R(1, 3) * R(1, 2) * 16 * 4 - R(1, 3) * R(1, 2) * R(5, 2)**3
    return ok(V == R(129, 16) and near(V, 8.06), V)


@pruef("2023-bebb-gk-B3h")
def _():
    # R(3,25 | 0,75 | 0), |DR| ≈ 1,06 = 3√2/4
    g = Matrix([R(5, 2), 0, 0]) + t * Matrix([1, 1, 0])
    tt = solve(sum(g) - 4, t)[0]
    Rp = g.subs(t, tt)
    d = (Rp - Matrix([R(5, 2), 0, 0])).norm()
    bed = list(Rp) == [R(13, 4), R(3, 4), 0] and simplify(d - 3 * sqrt(2) / 4) == 0 and near(d, 1.06) and Matrix([1, 1, 0]).dot(B3 - A3) == 0
    return ok(bed, (list(Rp), float(d)))


@pruef("2023-bebb-gk-B3i")
def _():
    # C'(2+2√3 | 2+2√3 | 0)
    M = (A3 + B3) / 2
    rad = (C3 - M).norm()
    Cs = M + rad * Matrix([1, 1, 0]) / sqrt(2)
    bed = rad == 2 * sqrt(6) and all(simplify(Cs[i] - (2 + 2 * sqrt(3))) == 0 for i in range(2)) and Cs[2] == 0 and (Cs - M).dot(B3 - A3) == 0
    return ok(bed, [simplify(v) for v in Cs])


@pruef("2023-bebb-gk-B4.1a")
def _():
    # 15/57/10/18
    W, G, WG = R(72, 100), R(25, 100), R(15, 100)
    w = (WG, W - WG, G - WG, 1 - W - G + WG)
    return ok(w == (R(15, 100), R(57, 100), R(10, 100), R(18, 100)), w)


@pruef("2023-bebb-gk-B4.1b")
def _():
    # 0,82
    return ok(1 - R(18, 100) == R(82, 100) == R(72, 100) + R(25, 100) - R(15, 100), "")


@pruef("2023-bebb-gk-B4.1c")
def _():
    # ≈ 0,208
    return ok(near(R(15, 72), 0.208, 1e-3), float(R(15, 72)))


@pruef("2023-bebb-gk-B4.1d")
def _():
    # P(X ≥ 80) ≈ 0,149
    p = binom_p(100, R(3, 4), 80, 100)
    return ok(near(p, 0.149, 1e-3), float(p))


nr("2023-bebb-gk-B4.1e", "Term deuten")


@pruef("2023-bebb-gk-B4.1f")
def _():
    # n = 11, Grenze 10,41
    n0 = float(log(0.05) / log(0.75))
    n = math.ceil(n0)
    return ok(n == 11 and near(n0, 10.41, 0.01) and 1 - 0.75**11 >= 0.95 > 1 - 0.75**10, (n, n0))


@pruef("2023-bebb-gk-B4.1g")
def _():
    # 77/3230 ≈ 0,024
    p = binomial(12, 6) / binomial(20, 6)
    return ok(p == R(77, 3230) and near(p, 0.024, 1e-3) and binomial(20, 6) == 38760 and binomial(12, 6) == 924, p)


@pruef("2023-bebb-gk-B4.1h")
def _():
    # 35/1938 ≈ 0,018
    p = (binomial(8, 6) + 12 * binomial(8, 5)) / binomial(20, 6)
    return ok(p == R(35, 1938) and near(p, 0.018, 1e-3), p)


E42 = 8 * R(4, 9)**2 + 2 * 2 * R(4, 9) * R(5, 9) + R(1, 2) * R(5, 9)**2


@pruef("2023-bebb-gk-B4.2a")
def _():
    # E = 49/18 ≈ 2,72
    return ok(E42 == R(49, 18) and near(E42, 2.72), E42)


@pruef("2023-bebb-gk-B4.2b")
def _():
    # E ≈ 2,72 > 2, Gewinn ≈ 0,72
    return ok(E42 > 2 and near(E42 - 2, 0.72), float(E42 - 2))


@pruef("2023-bebb-gk-B4.2c")
def _():
    # p = 1/3
    p = symbols('p')
    Ep = 8 * p**2 + 4 * p * (1 - p) + R(1, 2) * (1 - p)**2
    bed = simplify(Ep - (R(9, 2) * p**2 + 3 * p + R(1, 2))) == 0
    L = solve(Ep - 2, p)
    return ok(bed and set(L) == {R(1, 3), -1}, L)


nr("2024-bebb-gk-A1.1a", "Symmetrie am Term begründen")


@pruef("2024-bebb-gk-A1.1b")
def _():
    # 8; Nullstellen −2, 0, 2
    f = x**3 - 4 * x
    ns = sorted(solve(f, x))
    A = 2 * integrate(f, (x, -2, 0))
    return ok(ns == [-2, 0, 2] and A == 8, (ns, A))


@pruef("2024-bebb-gk-A1.2a")
def _():
    # z-Komponente −3 ≠ 0 für alle t
    d = Matrix([6, t, 20]) - Matrix([2, 0, 23])
    return ok(d[2] == -3, d[2])


@pruef("2024-bebb-gk-A1.2b")
def _():
    # t = ±6
    Q = Matrix([6, t, 20])
    sp = (Matrix([0, 0, 0]) - Q).dot(Matrix([2, 0, 23]) - Q)
    L = sorted(solve(sp, t))
    return ok(simplify(sp - (t**2 - 36)) == 0 and L == [-6, 6], (sp, L))


@pruef("2024-bebb-gk-A1.3a")
def _():
    # 4 Auswahlen: 135, 136, 146, 246
    from itertools import combinations
    L = [c for c in combinations(range(1, 7), 3) if c[1] - c[0] >= 2 and c[2] - c[1] >= 2]
    return ok(L == [(1, 3, 5), (1, 3, 6), (1, 4, 6), (2, 4, 6)], L)


@pruef("2024-bebb-gk-A1.3b")
def _():
    # 24
    return ok(4 * math.factorial(3) == 24, 4 * 6)


@pruef("2024-bebb-gk-A1.4a")
def _():
    # g'(0) = 2
    g = 2 * exp(x) - 2
    return ok(diff(g, x).subs(x, 0) == 2, diff(g, x).subs(x, 0))


@pruef("2024-bebb-gk-A1.4b")
def _():
    # g'(0) = 2 ≠ h'(0) = 1
    g, h = 2 * exp(x) - 2, exp(x) + 1
    w = (diff(g, x).subs(x, 0), diff(h, x).subs(x, 0))
    return ok(w == (2, 1), w)


@pruef("2024-bebb-gk-A1.5a")
def _():
    # Verhältnis 1 : 3 (Beispielkoordinaten)
    A, B, C = Matrix([0, 0]), Matrix([2, 0]), Matrix([1, 3])
    D = C - 2 * (B - A)
    def fl(P, Q, Rr):
        return abs((Q - P)[0] * (Rr - P)[1] - (Q - P)[1] * (Rr - P)[0]) / 2
    dreieck = fl(A, B, C)
    trapez = fl(A, B, C) + fl(A, C, D)
    return ok(dreieck / trapez == R(1, 3), dreieck / trapez)


@pruef("2024-bebb-gk-A1.6a")
def _():
    # 0,064 < 0,1
    return ok(R(2, 5)**3 == R(8, 125) and R(8, 125) < R(1, 10), R(2, 5)**3)


nr("2024-bebb-gk-A1.6b", "Ereignis beschreiben")


@pruef("2024-bebb-gk-A1.7a")
def _():
    # f'(x) = 0,5e^(0,5x) > 0
    f = exp(x / 2) - E
    fs = diff(f, x)
    return ok(simplify(fs - exp(x / 2) / 2) == 0 and fs.subs(x, -100) > 0, fs)


@pruef("2024-bebb-gk-A1.7b")
def _():
    # Nullstelle 2; h(x) = e^(0,5x+1) − e
    f = exp(x / 2) - E
    ns = solve(f, x)
    h = f.subs(x, x + 2)
    return ok(ns == [2] and simplify(h - (exp(x / 2 + 1) - E)) == 0 and h.subs(x, 0) == 0, (ns, h))


@pruef("2024-bebb-gk-A1.8a")
def _():
    # B(−1|0|−2), C(3|1|−3): alle Abstände zu M gleich 3, |CA| = |CB| = √18
    A, M = Matrix([3, 4, 0]), Matrix([1, 2, -1])
    B = 2 * M - A
    C = Matrix([3, 1, -3])
    w = ((A - M).norm(), (B - M).norm(), (C - M).norm(), (C - A).norm(), (C - B).norm())
    return ok(list(B) == [-1, 0, -2] and w == (3, 3, 3, sqrt(18), sqrt(18)), (list(B), w))


# ======================= Teilstück 3 (2024 A1.9a – 2022 A1.2a) ================

nr("2024-bebb-gk-A1.9a", "Baumdiagramm vervollständigen")


@pruef("2024-bebb-gk-A1.9b")
def _():
    # p = 0,1
    p = symbols('p')
    L = solve(R(6, 10) * p + R(4, 10) * (1 - p) - R(42, 100), p)
    return ok(L == [R(1, 10)], L)


f24 = (x - 2) * exp(-x / 2 + 3)
F24 = -2 * x * exp(-x / 2 + 3)


@pruef("2024-bebb-gk-B2.1a")
def _():
    # Nullstelle 2; (0 | −2e³) ≈ −40,17
    w = (solve(f24, x), f24.subs(x, 0))
    return ok(w[0] == [2] and w[1] == -2 * E**3 and near(w[1], -40.17), (w[0], float(w[1])))


@pruef("2024-bebb-gk-B2.1b")
def _():
    # Hochpunkt (4 | 2e) ≈ 5,44
    fs = diff(f24, x)
    xs = solve(fs, x)
    w = (xs, simplify(f24.subs(x, 4)), diff(f24, x, 2).subs(x, 4) < 0)
    return ok(xs == [4] and w[1] == 2 * E and near(w[1], 5.44) and w[2], w)


@pruef("2024-bebb-gk-B2.1c")
def _():
    # f2 = (x/4 − 3/2)e^(−x/2+3); W(6 | 4); f3(6) = 1/4
    f2 = diff(f24, x, 2)
    bed = simplify(f2 - (x / 4 - R(3, 2)) * exp(-x / 2 + 3)) == 0
    w = (solve(f2, x), f24.subs(x, 6), diff(f24, x, 3).subs(x, 6))
    return ok(bed and w == ([6], 4, R(1, 4)), w)


@pruef("2024-bebb-gk-B2.1d")
def _():
    # f'(6) = −1; Steigung AB = 1; Minimum von f' = −1 bei 6
    fs = diff(f24, x)
    m_ab = (f24.subs(x, 6) - 0) / (6 - 2)
    xmin = solve(diff(fs, x), x)
    w = (fs.subs(x, 6), m_ab, xmin, fs.subs(x, xmin[0]))
    return ok(w == (-1, 1, [6], -1), w)


@pruef("2024-bebb-gk-B2.1e")
def _():
    # F' = f
    return ok(simplify(diff(F24, x) - f24) == 0, diff(F24, x))


@pruef("2024-bebb-gk-B2.1f")
def _():
    # f' hat genau eine Nullstelle (4) mit Vorzeichenwechsel
    fs = diff(f24, x)
    return ok(solve(fs, x) == [4] and fs.subs(x, 3) > 0 and fs.subs(x, 5) < 0, solve(fs, x))


@pruef("2024-bebb-gk-B2.1g")
def _():
    # f(11) = 9e^(−2,5) ≈ 0,739; Durchmesser ≈ 7,4 mm
    f11 = f24.subs(x, 11)
    dmm = 2 * f11 * 5
    return ok(simplify(f11 - 9 * exp(R(-5, 2))) == 0 and near(f11, 0.739, 1e-3) and near(dmm, 7.4, 0.05), (float(f11), float(dmm)))


@pruef("2024-bebb-gk-B2.1h")
def _():
    # 4,5 × 5,44 × 5,44 cm; ≈ 114 g
    L = 9 * 0.5
    bh = float(2 * 2 * E * 0.5)
    m = L * bh**2 * 0.86
    return ok(L == 4.5 and near(bh, 5.44) and near(m, 114, 0.5), (L, bh, m))


@pruef("2024-bebb-gk-B2.1i")
def _():
    # f'(2) = e², α ≈ 164,6°
    m = diff(f24, x).subs(x, 2)
    al = float(2 * atan(m) * 180 / pi)
    return ok(simplify(m - E**2) == 0 and near(al, 164.6, 0.05) and al >= 160, (m, al))


@pruef("2024-bebb-gk-B2.1j")
def _():
    # Integral ≈ 27,75; A ≈ 13,9 cm²
    I = integrate(f24, (x, 2, 11))
    A = 2 * I * R(1, 4)
    return ok(simplify(I - (F24.subs(x, 11) - F24.subs(x, 2))) == 0 and near(I, 27.75, 0.01) and near(A, 13.9, 0.05), (float(I), float(A)))


f242 = R(1, 2) * x**4 - 4 * x**2 + R(7, 2)


@pruef("2024-bebb-gk-B2.2a")
def _():
    # f(−x) = f(x)
    return ok(simplify(f242.subs(x, -x) - f242) == 0, f242.subs(x, -x))


@pruef("2024-bebb-gk-B2.2b")
def _():
    # Nullstellen ±1, ±√7
    ns = sorted(solve(f242, x))
    return ok(ns == [-sqrt(7), -1, 1, sqrt(7)], ns)


@pruef("2024-bebb-gk-B2.2c")
def _():
    # H(0 | 3,5), T(±2 | −4,5)
    f1, f2 = diff(f242, x), diff(f242, x, 2)
    w = sorted((xi, f242.subs(x, xi), f2.subs(x, xi)) for xi in solve(f1, x))
    return ok(w == [(-2, R(-9, 2), 16), (0, R(7, 2), -8), (2, R(-9, 2), 16)], w)


@pruef("2024-bebb-gk-B2.2d")
def _():
    # 37/12; t: y = 6x + 6; g: y = −x/6 − 1/6
    m = diff(f242, x).subs(x, -1)
    tg = m * (x + 1) + f242.subs(x, -1)
    g = -1 / m * (x + 1) + f242.subs(x, -1)
    A = R(1, 2) * abs(tg.subs(x, 0) - g.subs(x, 0)) * 1
    return ok(expand(tg) == 6 * x + 6 and expand(g) == -x / 6 - R(1, 6) and A == R(37, 12), (tg, g, A))


@pruef("2024-bebb-gk-B2.2e")
def _():
    # 31/60, 7/4, 31:105
    sek = R(7, 2) * x + R(7, 2)
    L = sorted(v for v in solve(f242 - sek, x) if v.is_real and -1 <= v <= 0)
    I = integrate(f242 - sek, (x, -1, 0))
    D = R(1, 2) * 1 * f242.subs(x, 0)
    return ok(L == [-1, 0] and I == R(31, 60) and D == R(7, 4) and I / D == R(31, 105), (L, I, D))


@pruef("2024-bebb-gk-B2.2f")
def _():
    # a = 15/68
    I = integrate(f242, (x, -1, 1))
    return ok(I == R(68, 15) and 1 / I == R(15, 68) and near(1 / I, 0.22), I)


@pruef("2024-bebb-gk-B2.2g")
def _():
    # max d = 1/8 bei ±1/√2
    p = -R(7, 2) * x**2 + R(7, 2)
    d = p - f242
    xs = solve(diff(d, x), x)
    w = sorted(d.subs(x, xi) for xi in xs)
    return ok(simplify(d - (x**2 / 2 - x**4 / 2)) == 0 and set(xs) == {0, 1 / sqrt(2), -1 / sqrt(2)} and max(w) == R(1, 8) and d.subs(x, 1) == 0, (xs, w))


@pruef("2024-bebb-gk-B2.2h")
def _():
    # Grenze x = √1,5 ≈ 1,22
    p = -R(7, 2) * x**2 + R(7, 2)
    L = [v for v in solve(f242 - p - R(3, 8), x) if v.is_real and v > 0]
    return ok(L == [sqrt(R(3, 2))] and near(L[0], 1.22), L)


P24 = dict(A=Matrix([0, 0, 0]), B=Matrix([2, 0, 0]), C=Matrix([2, 2, 0]), D=Matrix([0, 4, 0]), S=Matrix([0, 0, R(7, 2)]))


@pruef("2024-bebb-gk-B3a")
def _():
    # AD = 2 BC; Fläche 6; V = 7
    A_, B_, C_, D_, S_ = (P24[k] for k in "ABCDS")
    G = R(1, 2) * (4 + 2) * 2
    V = R(1, 3) * G * R(7, 2)
    return ok((D_ - A_) == 2 * (C_ - B_) and G == 6 and V == 7, (G, V))


@pruef("2024-bebb-gk-B3b")
def _():
    # CD · CS = 0
    C_, D_, S_ = (P24[k] for k in "CDS")
    return ok((D_ - C_).dot(S_ - C_) == 0, (D_ - C_).dot(S_ - C_))


@pruef("2024-bebb-gk-B3c")
def _():
    # Kantenlängen AS = 3,5, BS = √16,25, CS = 4,5, DS = √28,25
    A_, B_, C_, D_, S_ = (P24[k] for k in "ABCDS")
    w = [(P_ - S_).norm() for P_ in (A_, B_, C_, D_)]
    return ok(w == [R(7, 2), sqrt(R(65, 4)), R(9, 2), sqrt(R(113, 4))], w)


@pruef("2024-bebb-gk-B3d")
def _():
    # 7x + 7y + 8z = 28
    C_, D_, S_ = (P24[k] for k in "CDS")
    n = (D_ - C_).cross(S_ - C_)
    n2 = Matrix([7, 7, 8])
    bed = n.cross(n2).norm() == 0 and n2.dot(C_) == 28 and n2.dot(D_) == 28 and n2.dot(S_) == 28
    return ok(bed, list(n))


@pruef("2024-bebb-gk-B3e")
def _():
    # cos φ = 7/√162; φ ≈ 56,6°
    from sympy import acos
    c = 7 / sqrt(162)
    phi = float(acos(c) * 180 / pi)
    return ok(near(phi, 56.6, 0.05) and near(c, 0.55, 0.01), phi)


@pruef("2024-bebb-gk-B3f")
def _():
    # k = 14/11; alle Ecken in der Pyramide
    C_, S_ = P24['C'], P24['S']
    g = C_ + s * (S_ - C_)
    ss = solve(g[0] - g[2], s)[0]
    k_ = g.subs(s, ss)[0]
    ecken = [Matrix([i * k_, j * k_, l * k_]) for i in (0, 1) for j in (0, 1) for l in (0, 1)]
    innen = all(7 * e[0] + 7 * e[1] + 8 * e[2] <= 28 and R(7, 2) * e[0] + 2 * e[2] <= 7 for e in ecken)
    return ok(ss == R(4, 11) and k_ == R(14, 11) and innen, (ss, k_, innen))


nr("2024-bebb-gk-B4.1a", "Term deuten")


@pruef("2024-bebb-gk-B4.1b")
def _():
    # 0,15 / 0,05 / 0,45 / 0,35
    T, M, nTM = R(6, 10), R(2, 10), R(5, 100)
    w = (M - nTM, nTM, T - (M - nTM), 1 - T - nTM)
    return ok(w == (R(15, 100), R(5, 100), R(45, 100), R(35, 100)), w)


@pruef("2024-bebb-gk-B4.1c")
def _():
    # 0,5
    return ok(R(45, 100) + R(5, 100) == R(1, 2), "")


@pruef("2024-bebb-gk-B4.1d")
def _():
    # 0,12 ≠ 0,15; P_T(M) = 0,25
    return ok(R(6, 10) * R(2, 10) == R(12, 100) != R(15, 100) and R(15, 100) / R(6, 10) == R(1, 4), "")


@pruef("2024-bebb-gk-B4.2a")
def _():
    # P(5) = 1/6, P(2) = 5/6; (5/6)² = 25/36
    q = symbols('q', positive=True)
    L = solve(q**2 - R(1, 36), q)
    return ok(L == [R(1, 6)] and (1 - R(1, 6))**2 == R(25, 36), L)


@pruef("2024-bebb-gk-B4.2b")
def _():
    # 4 · (25/36)⁴ · (11/36)³ ≈ 2,7 %
    p = 4 * R(25, 36)**4 * R(11, 36)**3
    return ok(near(p, 0.027, 5e-4), float(p))


@pruef("2024-bebb-gk-B4.2c")
def _():
    # E = 9 ⇔ 9q² + 12q − 5 = 0
    q = symbols('q')
    Eq_ = 25 * q**2 + 2 * 10 * q * (1 - q) + 4 * (1 - q)**2 - 9
    return ok(expand(Eq_) == 9 * q**2 + 12 * q - 5, expand(Eq_))


@pruef("2022-bebb-gk-A1.1a")
def _():
    # 0, 2, 6
    f = x**3 - 8 * x**2 + 12 * x
    return ok(sorted(solve(f, x)) == [0, 2, 6], solve(f, x))


@pruef("2022-bebb-gk-A1.1b")
def _():
    # t: y = −x + 6
    f = x**3 - 8 * x**2 + 12 * x
    tg = diff(f, x).subs(x, 1) * (x - 1) + f.subs(x, 1)
    return ok(expand(tg) == -x + 6 and f.subs(x, 1) == 5, expand(tg))


nr("2022-bebb-gk-A1.2a", "Ablesewerte aus der Abbildung")


# ======================= Teilstück 4 (2022 A1.2b – 2022 B3a) ==================

nr("2022-bebb-gk-A1.2b", "Punkt am Graphen markieren")


@pruef("2022-bebb-gk-A1.3a")
def _():
    # m = −6
    m = symbols('m', negative=True)
    A = integrate(m * x - x**2, (x, m, 0))
    L = solve(A - 36, m)
    return ok(simplify(A + m**3 / 6) == 0 and L == [-6], (A, L))


@pruef("2022-bebb-gk-A1.4a")
def _():
    # 3 − 3 = 0
    return ok(3 * 1 - 2 * R(3, 2) == 0, 3 * 1 - 2 * R(3, 2))


@pruef("2022-bebb-gk-A1.4b")
def _():
    # Ursprung und (0|0|1) erfüllen 3x − 2y = 0
    return ok(all(3 * p[0] - 2 * p[1] == 0 for p in ([0, 0, 0], [0, 0, 1], [0, 0, -5])), "")


@pruef("2022-bebb-gk-A1.4c")
def _():
    # s = 3
    L = solve(Matrix([3, -2, 0]).dot(Matrix([2, s, 1])), s)
    return ok(L == [3], L)


@pruef("2022-bebb-gk-A1.5a")
def _():
    # |AC| = |BC| = √(25 + z²)
    zz = symbols('zz', positive=True)
    A, B, C = Matrix([0, 0, 0]), Matrix([8, 6, 0]), Matrix([4, 3, zz])
    w = ((C - A).norm(), (C - B).norm())
    return ok(simplify(w[0] - w[1]) == 0 and simplify(w[0] - sqrt(25 + zz**2)) == 0, w)


@pruef("2022-bebb-gk-A1.5b")
def _():
    # z = 7
    zz = symbols('zz', positive=True)
    A, B = Matrix([0, 0, 0]), Matrix([8, 6, 0])
    L = solve(R(1, 2) * (B - A).norm() * zz - 35, zz)
    return ok((B - A).norm() == 10 and L == [7], L)


@pruef("2022-bebb-gk-A1.6a")
def _():
    # 4/5
    p = 1 - R(4, 6) * R(3, 5) * R(2, 4)
    return ok(p == R(4, 5), p)


@pruef("2022-bebb-gk-A1.6b")
def _():
    # rot entfernt: 0,6; grün entfernt: 0,4
    w = (2 * R(3, 5) * R(2, 4), 2 * R(4, 5) * R(1, 4))
    return ok(w == (R(3, 5), R(2, 5)), w)


@pruef("2022-bebb-gk-A1.7a")
def _():
    # 1/3
    return ok(R(2, 10) / R(6, 10) == R(1, 3), R(2, 10) / R(6, 10))


@pruef("2022-bebb-gk-A1.7b")
def _():
    # 0,5
    return ok(R(6, 10) + R(3, 10) - 2 * R(2, 10) == R(1, 2), "")


f22b = (x + 2) * exp(-x)


@pruef("2022-bebb-gk-B2.1a")
def _():
    # (−2|0), (0|2); Hochpunkt (−1 | e)
    fs = diff(f22b, x)
    bed = simplify(fs + (x + 1) * exp(-x)) == 0
    w = (solve(f22b, x), f22b.subs(x, 0), solve(fs, x), f22b.subs(x, -1), fs.subs(x, -2) > 0, fs.subs(x, 0) < 0)
    return ok(bed and w == ([-2], 2, [-1], E, True, True), w)


@pruef("2022-bebb-gk-B2.1b")
def _():
    # lim = 0, von oben
    return ok(limit(f22b, x, oo) == 0 and f22b.subs(x, 100) > 0, limit(f22b, x, oo))


nr("2022-bebb-gk-B2.1c", "Graphen zuordnen")


@pruef("2022-bebb-gk-B2.1d")
def _():
    # x = −1,5
    L = solve(f22b - diff(f22b, x), x)
    return ok(L == [R(-3, 2)], L)


@pruef("2022-bebb-gk-B2.1e")
def _():
    # φ ≈ 32,5°; m1 ≈ 2,24; m2 ≈ −6,72
    m1 = diff(f22b, x).subs(x, R(-3, 2))
    m2 = diff(f22b, x, 2).subs(x, R(-3, 2))
    phi = float(atan(abs((m1 - m2) / (1 + m1 * m2))) * 180 / pi)
    return ok(near(m1, 2.24) and near(m2, -6.72) and near(phi, 32.5, 0.05), (float(m1), float(m2), phi))


@pruef("2022-bebb-gk-B2.1f")
def _():
    # e³ > 2 − e
    fs = diff(f22b, x)
    I1, I2 = integrate(fs, (x, -3, -2)), integrate(fs, (x, -1, 0))
    return ok(simplify(I1 - E**3) == 0 and simplify(I2 - (2 - E)) == 0 and I1 > 0 > I2, (I1, I2))


@pruef("2022-bebb-gk-B2.1g")
def _():
    # Umfang 4 + 2√2; Mittelpunkt (1 | 1)
    tg = diff(f22b, x).subs(x, 0) * x + f22b.subs(x, 0)
    xs = solve(tg, x)[0]
    U = xs + tg.subs(x, 0) + sqrt(xs**2 + tg.subs(x, 0)**2)
    M = (Matrix([xs, 0]) + Matrix([0, tg.subs(x, 0)])) / 2
    return ok(expand(tg) == -x + 2 and simplify(U - (4 + 2 * sqrt(2))) == 0 and list(M) == [1, 1], (tg, U, list(M)))


@pruef("2022-bebb-gk-B2.1h")
def _():
    # u = √2; P ≈ (1,41 | 0,83)
    A = u * f22b.subs(x, u)
    As = diff(A, u)
    bed = simplify(As - (2 - u**2) * exp(-u)) == 0
    L = [v for v in solve(As, u) if v > 0]
    yv = f22b.subs(x, sqrt(2))
    return ok(bed and L == [sqrt(2)] and near(yv, 0.83), (L, float(yv)))


@pruef("2022-bebb-gk-B2.1i")
def _():
    # A_b = 2 − (b+2)e^(−b); b ≈ 1,146 für A_b = 1
    from sympy import nsolve
    Ab = f22b.subs(x, 0) - f22b.subs(x, b)
    bed = simplify(Ab - (2 - (b + 2) * exp(-b))) == 0 and limit(Ab, b, oo) == 2 and Ab.subs(b, 0) == 0
    b0 = nsolve(Ab - 1, b, 1)
    return ok(bed and near(b0, 1.146, 1e-3), (bed, float(b0)))


h22 = R(9, 40) * t**3 - R(27, 2) * t**2 + R(405, 2) * t


@pruef("2022-bebb-gk-B2.1j")
def _():
    # h'(10) = 0, h''(10) = −13,5, h(10) = 900
    w = (diff(h22, t).subs(t, 10), diff(h22, t, 2).subs(t, 10), h22.subs(t, 10))
    return ok(w == (0, R(-27, 2), 900), w)


@pruef("2022-bebb-gk-B2.1k")
def _():
    # h(15) = 759,375; Weg ≈ 1041
    h15 = h22.subs(t, 15)
    W = 900 + 900 - h15
    return ok(h15 == R(6075, 8) and near(W, 1041, 0.7), (float(h15), float(W)))


@pruef("2022-bebb-gk-B2.1l")
def _():
    # Wendestelle 20
    return ok(solve(diff(h22, t, 2), t) == [20], solve(diff(h22, t, 2), t))


@pruef("2022-bebb-gk-B2.1m")
def _():
    # t = 8 oder 32
    L = sorted(solve(diff(h22, t) - R(297, 10), t))
    return ok(L == [8, 32] and diff(h22, t).subs(t, 4) > R(297, 10), L)


f222 = -R(1, 6) * x**3 + R(1, 2) * x**2


@pruef("2022-bebb-gk-B2.2a")
def _():
    # −∞ / +∞
    w = (limit(f222, x, oo), limit(f222, x, -oo))
    return ok(w == (-oo, oo), w)


@pruef("2022-bebb-gk-B2.2b")
def _():
    # T(0|0), H(2|2/3)
    f1, f2 = diff(f222, x), diff(f222, x, 2)
    w = sorted((xi, f222.subs(x, xi), f2.subs(x, xi)) for xi in solve(f1, x))
    return ok(w == [(0, 0, 1), (2, R(2, 3), -1)], w)


@pruef("2022-bebb-gk-B2.2c")
def _():
    # x0 = 1 ± √3/3
    ms = (f222.subs(x, 2) - f222.subs(x, 0)) / 2
    L = sorted(solve(diff(f222, x) - ms, x))
    return ok(ms == R(1, 3) and L == [1 - sqrt(3) / 3, 1 + sqrt(3) / 3] and near(L[0], 0.42) and near(L[1], 1.58), (ms, L))


@pruef("2022-bebb-gk-B2.2d")
def _():
    # F' = f; Nullstellen 0, 3; F(4) = 0
    F = -R(1, 24) * x**4 + R(1, 6) * x**3
    w = (simplify(diff(F, x) - f222) == 0, sorted(set(solve(f222, x))), F.subs(x, 4), integrate(f222, (x, 0, 4)))
    return ok(w == (True, [0, 3], 0, 0), w)


@pruef("2022-bebb-gk-B2.2e")
def _():
    # 26,6°; −1/6
    m = diff(f222, x).subs(x, 1)
    tg = m * (x - 1) + f222.subs(x, 1)
    al = float(atan(m) * 180 / pi)
    return ok(m == R(1, 2) and near(al, 26.6, 0.05) and tg.subs(x, 0) == R(-1, 6), (m, al, tg.subs(x, 0)))


@pruef("2022-bebb-gk-B2.2f")
def _():
    # a ≈ 0,55, b ≈ 1,45
    from sympy import tan, rad
    c = float(tan(rad(21.8)))
    L = sorted(solve(diff(f222, x) - R(2, 5), x))
    return ok(near(c, 0.4, 1e-3) and L == [1 - sqrt(R(1, 5)), 1 + sqrt(R(1, 5))] and near(L[0], 0.55) and near(L[1], 1.45), (c, L))


@pruef("2022-bebb-gk-B2.2g")
def _():
    # g(x) = x − 0,8 durch C und D
    g = x - R(4, 5)
    m = (R(12, 10) + R(4, 10)) / (2 - R(4, 10))
    return ok(m == 1 and g.subs(x, R(4, 10)) == R(-4, 10) and g.subs(x, 2) == R(12, 10), (m,))


h22b = R(9, 4) * f222


@pruef("2022-bebb-gk-B2.2h")
def _():
    # 1,5 − 0,64 + 0,08 = 0,94
    I = integrate(h22b, (x, 0, 2))
    trapez = integrate(x - R(4, 5), (x, R(4, 10), 2))
    dreieck = R(1, 2) * R(4, 10) * R(4, 10)
    A = I - trapez + dreieck
    return ok(I == R(3, 2) and trapez == R(16, 25) and dreieck == R(2, 25) and A == R(47, 50), (I, trapez, dreieck, A))


@pruef("2022-bebb-gk-B2.2i")
def _():
    # 1,5 = 1,5
    return ok(integrate(R(3, 4) * x, (x, 0, 2)) == integrate(h22b, (x, 0, 2)) == R(3, 2), "")


@pruef("2022-bebb-gk-B2.2j")
def _():
    # h'(x0) = 1 ⇔ x0 = 2/3, 4/3
    L = sorted(solve(diff(h22b, x) - 1, x))
    return ok(L == [R(2, 3), R(4, 3)], L)


@pruef("2022-bebb-gk-B2.2k")
def _():
    # a = 1/32, b = 1/8
    aa, bb = symbols('aa bb')
    kf = aa * x**4 + bb * x**2
    L = solve([kf.subs(x, 2) - 1, diff(kf, x).subs(x, 2) - R(3, 2)], [aa, bb])
    return ok(L == {aa: R(1, 32), bb: R(1, 8)} and diff(kf, x).subs(x, 0) == 0, L)


@pruef("2022-bebb-gk-B3a")
def _():
    # 64 = 2 · 32
    E_, F_ = Matrix([4, 0, 6]), Matrix([8, 4, 6])
    return ok((F_ - E_).norm()**2 == 32 and 8**2 == 2 * 32, (F_ - E_).norm()**2)


# ======================= Teilstück 5 (2022 B3b – 2025 A1.7a) ==================

K22 = dict(A=Matrix([0, 0, 0]), B=Matrix([8, 0, 0]), C=Matrix([8, 8, 0]), D=Matrix([0, 8, 0]),
           E=Matrix([4, 0, 6]), F=Matrix([8, 4, 6]), G=Matrix([4, 8, 6]), H=Matrix([0, 4, 6]), S=Matrix([4, 4, 12]))


@pruef("2022-bebb-gk-B3b")
def _():
    # S = C + CG + CF
    C_, F_, G_, S_ = (K22[k] for k in "CFGS")
    L = solve(list(C_ + s * (G_ - C_) + t * (F_ - C_) - S_), [s, t])
    return ok(L == {s: 1, t: 1} and list(G_ - C_) == [-4, 0, 6] and list(F_ - C_) == [0, -4, 6], L)


@pruef("2022-bebb-gk-B3c")
def _():
    # n ⊥ CG, CF; N: 3x + 3y + 2z = 24
    C_, F_, G_, B_ = (K22[k] for k in "CFGB")
    n = Matrix([3, 3, 2])
    return ok(n.dot(G_ - C_) == 0 and n.dot(F_ - C_) == 0 and n.dot(B_) == 24, n.dot(B_))


@pruef("2022-bebb-gk-B3d")
def _():
    # alle Seiten √52
    C_, F_, G_, S_ = (K22[k] for k in "CFGS")
    w = [(G_ - C_).norm(), (F_ - C_).norm(), (S_ - G_).norm(), (S_ - F_).norm()]
    return ok(w == [sqrt(52)] * 4, w)


@pruef("2022-bebb-gk-B3e")
def _():
    # x − y = 0 enthält A, C, S; E ↔ H, F ↔ G spiegelbildlich
    A_, C_, S_, E_, H_, F_, G_ = (K22[k] for k in "ACSEHFG")
    sp = lambda P: Matrix([P[1], P[0], P[2]])
    bed = all(P[0] - P[1] == 0 for P in (A_, C_, S_)) and sp(E_) == H_ and sp(F_) == G_
    return ok(bed, "")


@pruef("2022-bebb-gk-B3f")
def _():
    # φ ≈ 46,2°; 4 · √1408 ≈ 150,1
    from sympy import acos
    F_, G_, S_ = (K22[k] for k in "FGS")
    v1, v2 = G_ - S_, F_ - S_
    c = v1.dot(v2) / (v1.norm() * v2.norm())
    phi = float(acos(c) * 180 / pi)
    A4 = 4 * v1.cross(v2).norm()
    return ok(c == R(36, 52) and near(phi, 46.2, 0.05) and v1.cross(v2).norm() == sqrt(1408) and near(A4, 150.1, 0.05), (phi, float(A4)))


@pruef("2022-bebb-gk-B3g")
def _():
    # Q1Q2 = 2 FG
    F_, G_, S_ = (K22[k] for k in "FGS")
    q1 = S_ + t * (F_ - S_)
    Q1 = q1.subs(t, solve(q1[2], t)[0])
    q2 = S_ + t * (G_ - S_)
    Q2 = q2.subs(t, solve(q2[2], t)[0])
    return ok((Q2 - Q1).norm() / (G_ - F_).norm() == 2 and list(Q1) == [12, 4, 0], (list(Q1), list(Q2)))


@pruef("2022-bebb-gk-B3h")
def _():
    # 512 − 128 = 384; Grundfläche 128
    F_, S_ = K22['F'], K22['S']
    q1 = S_ + t * (F_ - S_)
    Q1 = q1.subs(t, solve(q1[2], t)[0])
    d = 2 * (Q1 - Matrix([4, 4, 0])).norm()  # Diagonale 16
    Vg = R(1, 3) * (d * d / 2) * 12
    Ve = R(1, 3) * (R(1, 2) * 8 * 4) * 6
    return ok(d == 16 and d * d / 2 == 128 and Vg - 4 * Ve == 384, (d, Vg, Ve))


@pruef("2022-bebb-gk-B3i")
def _():
    # t = 9/13; R(88/13 | 4 | 102/13)
    E_, G_, F_, S_ = (K22[k] for k in "EGFS")
    M = (E_ + G_) / 2
    Rp = S_ + t * (F_ - S_)
    tt = solve((Rp - M).dot(F_ - S_), t)[0]
    Rp = Rp.subs(t, tt)
    return ok(list(M) == [4, 4, 6] and tt == R(9, 13) and list(Rp) == [R(88, 13), 4, R(102, 13)], (tt, list(Rp)))


nr("2022-bebb-gk-B4a", "Bernoulli-Bedingungen begründen")


@pruef("2022-bebb-gk-B4b")
def _():
    # 0,104; 0,734
    p9 = binom_p(100, R(7, 100), 9, 9)
    p8 = binom_p(100, R(7, 100), 0, 8)
    return ok(near(p9, 0.104, 1e-3) and near(p8, 0.734, 1e-3), (float(p9), float(p8)))


@pruef("2022-bebb-gk-B4c")
def _():
    # 2/7 ≈ 28,6 %
    w = (9 - 7) / S(7)
    return ok(w == R(2, 7) and near(w, 0.286, 1e-3), float(w))


@pruef("2022-bebb-gk-B4d")
def _():
    # n ≥ 31,7 ⇒ 32
    n0 = float(log(0.1) / log(0.93))
    return ok(near(n0, 31.7, 0.05) and math.ceil(n0) == 32, n0)


@pruef("2022-bebb-gk-B4e")
def _():
    # p ≈ 0,0303
    p = 1 - 0.54 ** (1 / 20)
    return ok(near(p, 0.0303, 1e-4), p)


@pruef("2022-bebb-gk-B4f")
def _():
    # 0,576; 0,9^10 ≈ 0,349
    q = R(9, 10)**10
    w = 1 - (1 - q)**2
    return ok(near(q, 0.349, 1e-3) and near(w, 0.576, 1e-3), (float(q), float(w)))


nr("2022-bebb-gk-B4g", "Terme deuten")


@pruef("2022-bebb-gk-B4h")
def _():
    # 0,008 / 0,042 / 0,092 / 0,858
    S_, Z, SZ = R(5, 100), R(10, 100), R(8, 100) * R(10, 100)
    w = (SZ, S_ - SZ, Z - SZ, 1 - S_ - Z + SZ)
    return ok(w == (R(8, 1000), R(42, 1000), R(92, 1000), R(858, 1000)), w)


@pruef("2022-bebb-gk-B4i")
def _():
    # 0,16 vs ≈ 0,097
    w = (R(8, 1000) / R(5, 100), R(92, 1000) / R(95, 100))
    return ok(w[0] == R(4, 25) and near(w[1], 0.097, 1e-3) and w[0] != w[1], (float(w[0]), float(w[1])))


@pruef("2022-bebb-gk-B4j")
def _():
    # x ≈ 0,0489 < 0,05
    xx = symbols('xx')
    L = solve(R(10, 100) * R(8, 100) + R(7, 100) * R(2, 100) + R(83, 100) * xx - R(5, 100), xx)
    return ok(near(L[0], 0.0489, 1e-4) and L[0] < R(5, 100), float(L[0]))


f25 = R(2, 25) * x**3 - R(3, 2) * x


@pruef("2025-bebb-gk-B2.1a")
def _():
    # punktsymmetrisch; Nullstellen 0, ±5√3/2
    ns = sorted(solve(f25, x))
    return ok(simplify(f25.subs(x, -x) + f25) == 0 and ns == [-5 * sqrt(3) / 2, 0, 5 * sqrt(3) / 2] and near(ns[2], 4.33), ns)


@pruef("2025-bebb-gk-B2.1b")
def _():
    # H(−2,5 | 2,5), T(2,5 | −2,5); y = −x
    f1, f2 = diff(f25, x), diff(f25, x, 2)
    w = sorted((xi, f25.subs(x, xi), f2.subs(x, xi)) for xi in solve(f1, x))
    m = (w[1][1] - w[0][1]) / (w[1][0] - w[0][0])
    return ok(w == [(R(-5, 2), R(5, 2), R(-6, 5)), (R(5, 2), R(-5, 2), R(6, 5))] and m == -1, (w, m))


@pruef("2025-bebb-gk-B2.1c")
def _():
    # g*: y = −2x; A*(−2,5 | 5)
    Dr = Matrix([[0, -1], [1, 0]])
    v = Dr * Matrix([2, 1])
    As = Dr * Matrix([5, R(5, 2)])
    return ok(v[1] / v[0] == -2 and list(As) == [R(-5, 2), 5], (list(v), list(As)))


@pruef("2025-bebb-gk-B2.1d")
def _():
    # f'(5√3/2) = 3; 71,6°; α = 45°
    m = simplify(diff(f25, x).subs(x, 5 * sqrt(3) / 2))
    al = float(atan(m) * 180 / pi)
    ta = abs((m - R(1, 2)) / (1 + m * R(1, 2)))
    return ok(m == 3 and near(al, 71.6, 0.05) and ta == 1, (m, al, ta))


@pruef("2025-bebb-gk-B2.1e")
def _():
    # ∫ = 12,5; A2 = 50; A1 − A2 = 125π/4 − 50 ≈ 48,2
    g = x / 2
    I = integrate(g - f25, (x, 0, 5))
    A1 = (5 * sqrt(5) / 2)**2 * pi
    D = A1 - 4 * I
    return ok(I == R(25, 2) and simplify(A1 - 125 * pi / 4) == 0 and near(D, 48.2, 0.05), (I, float(D)))


f25a = R(1, 8) * x**3 - R(3, 8) * x**2 - 1


@pruef("2025-bebb-gk-A1.1a")
def _():
    # t: y = 3x − 11
    tg = diff(f25a, x).subs(x, 4) * (x - 4) + f25a.subs(x, 4)
    return ok(expand(tg) == 3 * x - 11 and f25a.subs(x, 4) == 1, expand(tg))


@pruef("2025-bebb-gk-A1.1b")
def _():
    # zweite Stelle −2, f(−2) = −3,5
    L = sorted(solve(diff(f25a, x) - 3, x))
    return ok(L == [-2, 4] and f25a.subs(x, -2) == R(-7, 2), (L, f25a.subs(x, -2)))


@pruef("2025-bebb-gk-A1.2a")
def _():
    # P ∉ g; Q(4|3|0)
    g = Matrix([8, 3, -3]) + s * Matrix([-4, 0, 3])
    L = solve(list(g - Matrix([4, 3, 3])), s)
    Q = g.subs(s, 1)
    return ok(L == [] and list(Q) == [4, 3, 0], (L, list(Q)))


@pruef("2025-bebb-gk-A1.2b")
def _():
    # Skalarprodukt 0
    return ok(Matrix([-4, 0, 3]).dot(Matrix([0, 1, 0])) == 0, "")


nr("2025-bebb-gk-A1.3a", "Term deuten")


@pruef("2025-bebb-gk-A1.3b")
def _():
    # 30/64
    p = R(3, 8) * R(5, 8) + R(5, 8) * R(3, 8)
    return ok(p == R(30, 64), p)


@pruef("2025-bebb-gk-A1.4a")
def _():
    # f(1) = 0
    f = 2 * exp(x) - 2 * E
    return ok(f.subs(x, 1) == 0, f.subs(x, 1))


@pruef("2025-bebb-gk-A1.4b")
def _():
    # Integral −2, Fläche 2
    f = 2 * exp(x) - 2 * E
    I = integrate(f, (x, 0, 1))
    return ok(simplify(I + 2) == 0, I)


@pruef("2025-bebb-gk-A1.5a")
def _():
    # P'(4 | 11 | 5)
    P_, Q_ = Matrix([0, -1, 1]), Matrix([2, 5, 3])
    Ps = 2 * Q_ - P_
    return ok(list(Ps) == [4, 11, 5] and list(Q_ - P_) == [2, 6, 2], list(Ps))


@pruef("2025-bebb-gk-A1.5b")
def _():
    # Q ∈ E; PQ ∥ n
    P_, Q_ = Matrix([0, -1, 1]), Matrix([2, 5, 3])
    n = Matrix([1, 3, 1])
    return ok(n.dot(Q_) == 20 and (Q_ - P_).cross(n).norm() == 0, n.dot(Q_))


@pruef("2025-bebb-gk-A1.6a")
def _():
    # 72/380 ≈ 0,19
    p = R(9, 20) * R(8, 19)
    return ok(p == R(72, 380) and near(p, 0.19, 5e-3), float(p))


@pruef("2025-bebb-gk-A1.6b")
def _():
    # Wert ≈ 0,31
    p = binomial(9, 2) * binomial(11, 4) / binomial(20, 6)
    return ok(near(p, 0.31, 5e-3), float(p))


@pruef("2025-bebb-gk-A1.7a")
def _():
    # f' = −2x + 4; x = ±1
    f = -x**2 + 4 * x - 1
    fs = diff(f, x)
    L = sorted(solve(f / x - fs, x))
    return ok(fs == -2 * x + 4 and L == [-1, 1], (fs, L))


# ======================= Teilstück 6 (2025 A1.7b – 2026 A1.3b) ================

nr("2025-bebb-gk-A1.7b", "Gleichung deuten")


@pruef("2025-bebb-gk-A1.8a")
def _():
    # beide Skalarprodukte 0
    n = Matrix([4, 3, 0])
    return ok(n.dot(Matrix([-3, 4, 1])) == 0 and n.dot(Matrix([3, -4, 0])) == 0, "")


@pruef("2025-bebb-gk-A1.8b")
def _():
    # P(9 | 3 | 0), Abstand 10
    n = Matrix([4, 3, 0])
    P_ = Matrix([1, -3, 0]) + 2 * n
    d = abs((P_ - Matrix([1, -3, 0])).dot(n)) / n.norm()
    return ok(n.norm() == 5 and list(P_) == [9, 3, 0] and d == 10, (list(P_), d))


@pruef("2025-bebb-gk-A1.9a")
def _():
    # n = 21: P(10) = P(11), maximal
    ps = [binom_p(21, R(1, 2), i, i) for i in range(22)]
    return ok(ps[10] == ps[11] == max(ps) and 21 * R(1, 2) == R(21, 2), (ps[10], ps[11]))


@pruef("2025-bebb-gk-A1.9b")
def _():
    # ≈ 0,17 (exakt 0,168)
    p = binom_p(21, R(1, 2), 10, 10)
    p9 = binom_p(21, R(1, 2), 9, 100)
    p12 = binom_p(21, R(1, 2), 12, 12)
    naeh = 0.81 - 0.14 - 0.5
    return ok(near(p, 0.168, 1e-3) and near(p9, 0.81, 5e-3) and near(p12, 0.14, 5e-3) and near(naeh, 0.17, 1e-6), (float(p), float(p9), float(p12)))


f25b = (2 - x) * exp(x)
F25b = (3 - x) * exp(x)


@pruef("2025-bebb-gk-B2.2a")
def _():
    # Nullstelle 2; 0; −∞
    w = (solve(f25b, x), limit(f25b, x, -oo), limit(f25b, x, oo))
    return ok(w == ([2], 0, -oo), w)


@pruef("2025-bebb-gk-B2.2b")
def _():
    # Hochpunkt (1 | e)
    fs = diff(f25b, x)
    w = (simplify(fs - (1 - x) * exp(x)) == 0, solve(fs, x), f25b.subs(x, 1), diff(f25b, x, 2).subs(x, 1) < 0)
    return ok(w == (True, [1], E, True), w)


@pruef("2025-bebb-gk-B2.2c")
def _():
    # Dreiecksfläche 2e ≈ 5,44
    A = R(1, 2) * E * 4
    return ok(A == 2 * E and near(A, 5.44), float(A))


@pruef("2025-bebb-gk-B2.2d")
def _():
    # 2e − 6e^(−3) ≈ 5,138; Abweichung ≈ 6 %
    I = integrate(f25b, (x, -3, 1))
    bed = simplify(diff(F25b, x) - f25b) == 0 and simplify(I - (F25b.subs(x, 1) - F25b.subs(x, -3))) == 0
    ab = (2 * E - I) / I
    return ok(bed and simplify(I - (2 * E - 6 * exp(-3))) == 0 and near(I, 5.138, 1e-3) and near(ab, 0.06, 2e-3), (float(I), float(ab)))


nr("2025-bebb-gk-B2.2e", "Verlauf beschreiben")
nr("2025-bebb-gk-B2.2f", "Ablesewerte aus der Abbildung")
nr("2025-bebb-gk-B2.2g", "grafische Lösung und Deutung")

P25 = dict(A=Matrix([0, 0, 0]), B=Matrix([2, 2, 0]), C=Matrix([0, 6, 0]), D=Matrix([-2, 2, 0]), S=Matrix([0, 0, 6]))


@pruef("2025-bebb-gk-B3a")
def _():
    # kürzeste 2√2, längste 6√2, V = 24
    A_, B_, C_, D_, S_ = (P25[k] for k in "ABCDS")
    kanten = [(B_ - A_).norm(), (C_ - B_).norm(), (D_ - C_).norm(), (A_ - D_).norm(), (S_ - A_).norm(), (S_ - B_).norm(), (S_ - C_).norm(), (S_ - D_).norm()]
    G = R(1, 2) * (C_ - A_).norm() * (B_ - D_).norm()
    V = R(1, 3) * G * 6
    return ok(min(kanten) == 2 * sqrt(2) and max(kanten) == 6 * sqrt(2) and G == 12 and V == 24, (min(kanten), max(kanten), G, V))


@pruef("2025-bebb-gk-B3b")
def _():
    # 2x + y + z = 6
    B_, C_, S_ = (P25[k] for k in "BCS")
    n = Matrix([2, 1, 1])
    bed = n.dot(C_ - B_) == 0 and n.dot(S_ - B_) == 0 and n.dot(B_) == 6 and n.dot(C_) == 6 and n.dot(S_) == 6
    return ok(bed, n.dot(B_))


@pruef("2025-bebb-gk-B3c")
def _():
    # 1/√6; 65,9°
    from sympy import acos
    c = Matrix([2, 1, 1]).dot(Matrix([0, 0, 1])) / (Matrix([2, 1, 1]).norm() * 1)
    al = float(acos(c) * 180 / pi)
    return ok(c == 1 / sqrt(6) and near(al, 65.9, 0.05), (c, al))


@pruef("2025-bebb-gk-B3d")
def _():
    # y = 3 + √5 (Lösung des Ansatzes, nicht verlangt)
    L = solve(Matrix([2, y, 0]).dot(Matrix([2, y - 6, 0])), y)
    return ok(set(L) == {3 - sqrt(5), 3 + sqrt(5)} and near(3 + sqrt(5), 5.24), L)


nr("2025-bebb-gk-B4a", "Baumdiagramm erstellen")


@pruef("2025-bebb-gk-B4b")
def _():
    # ≈ 0,0918
    p = R(285, 1000) * R(159, 1000) + R(715, 1000) * R(65, 1000)
    return ok(near(p, 0.0918, 5e-5), float(p))


@pruef("2025-bebb-gk-B4c")
def _():
    # E = 91,8; P(92) > P(90)
    p = R(918, 10000)
    w = (1000 * p, binom_p(1000, p, 92, 92), binom_p(1000, p, 90, 90))
    # Ergebnis (E = 91,8; P(92) > P(90)) stimmt; der Katalog-Zwischenwert P(X = 90) ≈ 0,0428 weicht ab (sympy: 0,0432)
    return ok(w[0] == R(918, 10) and near(w[1], 0.0436, 1e-4) and near(w[2], 0.0428, 1e-4) and w[1] > w[2],
              f"E(X) = {w[0]} und P(X = 92) = {float(w[1]):.4f} > P(X = 90) = {float(w[2]):.4f} (Katalog-Zwischenwert P(X = 90) ≈ 0,0428)")


@pruef("2025-bebb-gk-B4d")
def _():
    # P(X ≤ 103) ≈ 0,8984; P(X ≤ 104) ≈ 0,9159
    p = R(918, 10000)
    w = (binom_p(1000, p, 0, 103), binom_p(1000, p, 0, 104))
    return ok(near(w[0], 0.8984, 1e-4) and near(w[1], 0.9159, 1e-4) and w[0] < R(9, 10) < w[1], (float(w[0]), float(w[1])))


@pruef("2025-bebb-gk-B4e")
def _():
    # x ≈ 0,0503
    xx = symbols('xx')
    f = R(285, 1000) * (R(159, 1000) - xx) / (R(285, 1000) * (R(159, 1000) - xx) + R(715, 1000) * R(65, 1000))
    L = solve(f - R(4, 10), xx)
    return ok(len(L) == 1 and near(L[0], 0.0503, 1e-4), float(L[0]))


f26 = R(1, 12) * (x**4 + 4 * x**3 + 24)


@pruef("2026-bb-gk-B2.1a")
def _():
    # f' → −∞ / +∞
    fs = diff(f26, x)
    w = (simplify(fs - x**2 * (x / 3 + 1)) == 0, limit(fs, x, -oo), limit(fs, x, oo))
    return ok(w == (True, -oo, oo), w)


@pruef("2026-bb-gk-B2.1b")
def _():
    # f' < 0 für x < −3, ≥ 0 für x > −3; Minimum von f bei −3
    fs = diff(f26, x)
    w = (fs.subs(x, -4) < 0, fs.subs(x, -1) > 0, fs.subs(x, 1) > 0, sorted(set(solve(fs, x))))
    return ok(w == (True, True, True, [-3, 0]), w)


@pruef("2026-bb-gk-B2.1c")
def _():
    # W(0 | 2), W(−2 | 2/3)
    f2 = diff(f26, x, 2)
    w = sorted((xi, f26.subs(x, xi), diff(f26, x, 3).subs(x, xi)) for xi in solve(f2, x))
    return ok(simplify(f2 - (x**2 + 2 * x)) == 0 and w == [(-2, R(2, 3), -2), (0, 2, 2)], w)


@pruef("2026-bb-gk-B2.1d")
def _():
    # f(−2) = 2/3 = t(−2); f'(−2) = 4/3
    tg = R(4, 3) * x + R(10, 3)
    w = (f26.subs(x, -2), tg.subs(x, -2), diff(f26, x).subs(x, -2))
    return ok(w == (R(2, 3), R(2, 3), R(4, 3)), w)


@pruef("2026-bb-gk-B2.1e")
def _():
    # z = 25/3
    m = R(4, 3)
    zz = 5 * sqrt(1 + m**2)
    return ok(zz == R(25, 3) and near(zz, 8.33), zz)


g26 = R(1, 3) * x**3 + x**2


@pruef("2026-bb-gk-B2.1f")
def _():
    # Höhe 8/3 ≤ 2,7; Breite 20/3 ≤ 6,7
    r = g26.subs(x, -2)
    H = 2 * r
    B = 2 * (2 + r)
    return ok(r == R(4, 3) and H == R(8, 3) and B == R(20, 3) and H <= 2.7 and B <= 6.7 and diff(g26, x).subs(x, -2) == 0, (H, B))


@pruef("2026-bb-gk-B2.1g")
def _():
    # 2 · (8/3 + 8π/9) ≈ 10,9
    I = integrate(g26, (x, -2, 0))
    r = R(4, 3)
    A = 2 * (2 * I + R(1, 2) * pi * r**2)
    return ok(I == R(4, 3) and simplify(A - 2 * (R(8, 3) + 8 * pi / 9)) == 0 and near(A, 10.92, 0.01), (I, float(A)))


@pruef("2026-bb-gk-B2.1h")
def _():
    # Q(2 | −4/3)
    L = [v for v in solve(diff(g26, x), x) if v != 0]
    xq = -L[0]
    yq = -g26.subs(x, -xq)
    return ok(L == [-2] and xq == 2 and yq == R(-4, 3), (xq, yq))


@pruef("2026-bb-gk-B2.1i")
def _():
    # ≈ 18,38 m; 5,25 min
    Lg = 4 * 2.5 + float(2 * pi * R(4, 3))
    T = Lg / 3.5
    return ok(near(Lg, 18.38, 0.01) and near(T, 5.25, 0.01), (Lg, T))


f26a = x**3 + x**2 - 2 * x


@pruef("2026-bb-gk-A1.1a")
def _():
    # 13/12
    I = integrate(f26a, (x, -1, 0))
    return ok(I == R(13, 12), I)


@pruef("2026-bb-gk-A1.1b")
def _():
    # 8/3 und −5/12
    w = (integrate(f26a, (x, -2, 0)), integrate(f26a, (x, 0, 1)))
    return ok(w == (R(8, 3), R(-5, 12)) and w[1] < 0, w)


@pruef("2026-bb-gk-A1.2a")
def _():
    # P ∈ E; PQ = 4n
    P_, Q_ = Matrix([5, 0, 3]), Matrix([9, -12, 11])
    n = Matrix([1, -3, 2])
    return ok(n.dot(P_) == 11 and Q_ - P_ == 4 * n, (n.dot(P_), list(Q_ - P_)))


@pruef("2026-bb-gk-A1.2b")
def _():
    # R(1 | 12 | −5)
    P_, Q_ = Matrix([5, 0, 3]), Matrix([9, -12, 11])
    Rr = P_ - (Q_ - P_)
    return ok(list(Rr) == [1, 12, -5], list(Rr))


@pruef("2026-bb-gk-A1.3a")
def _():
    # (1/2)^5 + 5 · 1/2 · (1/2)^4 = 3/16
    p = R(1, 2)**5 + 5 * R(1, 2) * R(1, 2)**4
    return ok(p == R(3, 16) and p == binom_p(5, R(1, 2), 0, 1), p)


@pruef("2026-bb-gk-A1.3b")
def _():
    # 4 Ergebnisse ZZ + mindestens 2 W
    from itertools import product
    L = sorted(''.join(w) for w in product('ZW', repeat=5) if w[0] == w[1] == 'Z' and w.count('W') >= 2)
    return ok(L == sorted(['ZZWWW', 'ZZZWW', 'ZZWZW', 'ZZWWZ']), L)


# ======================= Teilstück 7 (2026 A1.4a – 2026 B4f) ==================

@pruef("2026-bb-gk-A1.4a")
def _():
    # 2π
    from sympy import sin
    A_, B_, C_ = Matrix([pi / 2, 1]), Matrix([3 * pi / 2, -1]), Matrix([5 * pi / 2, 1])
    Fl = R(1, 2) * abs((B_ - A_)[0] * (C_ - A_)[1] - (B_ - A_)[1] * (C_ - A_)[0])
    bed = all(sin(P_[0]) == P_[1] for P_ in (A_, B_, C_))
    return ok(bed and simplify(Fl - 2 * pi) == 0, Fl)


@pruef("2026-bb-gk-A1.4b")
def _():
    # |AB| ≈ 3,72; bei g ≈ 10,24
    d1 = sqrt(pi**2 + 4)
    d2 = sqrt(9 * pi**2 + 16)
    return ok(near(d1, 3.72) and near(d2, 10.24) and d2 > d1, (float(d1), float(d2)))


@pruef("2026-bb-gk-A1.5a")
def _():
    # AB · AC = 0
    sp = Matrix([6, 2, 3]).dot(Matrix([t, -3 * t, 0]))
    return ok(simplify(sp) == 0, sp)


@pruef("2026-bb-gk-A1.5b")
def _():
    # t = 7/√10 ≈ 2,21
    tt = symbols('tt', positive=True)
    L = solve(Matrix([tt, -3 * tt, 0]).norm() - Matrix([6, 2, 3]).norm(), tt)
    return ok(Matrix([6, 2, 3]).norm() == 7 and L == [7 / sqrt(10)] and near(L[0], 2.21), L)


@pruef("2026-bb-gk-A1.6a")
def _():
    # p = 0,2; Maximum bei 4
    ps = [binom_p(20, R(1, 5), i, i) for i in range(21)]
    return ok(20 * R(1, 5) == 4 and ps.index(max(ps)) == 4, ps.index(max(ps)))


@pruef("2026-bb-gk-A1.6b")
def _():
    # v = 5 (P ≈ 0,175); w = 2 (P(X ≤ 2) ≈ 0,21)
    p = R(1, 5)
    w = (binom_p(20, p, 5, 5), binom_p(20, p, 0, 1), binom_p(20, p, 0, 2), binom_p(20, p, 0, 3))
    return ok(near(w[0], 0.175, 2e-3) and near(w[1], 0.07, 5e-3) and 0.15 < w[2] < 0.25 and near(w[2], 0.21, 5e-3) and w[3] > 0.25, [float(v) for v in w])


nr("2026-bb-gk-A1.7a", "Monotonie am Ableitungsgraphen begründen")
nr("2026-bb-gk-A1.7b", "Aussage beurteilen")


@pruef("2026-bb-gk-A1.8a")
def _():
    # C(−2/3 | 1/3 | 6)
    A_, B_ = Matrix([2, -3, -1]), Matrix([10, -5, 3])
    C_ = Matrix([x, y, 6])
    L = solve([(B_ - A_).dot(C_ - A_), x + 2 * y], [x, y])
    return ok(L == {x: R(-2, 3), y: R(1, 3)}, L)


@pruef("2026-bb-gk-A1.9a")
def _():
    # p = 0,8, n = 25; Wert ≈ 0,187
    p, n = symbols('p n')
    L = solve([n * p - 20, n * p * (1 - p) - 4], [p, n], dict=True)
    w = binom_p(25, R(4, 5), 21, 21)
    return ok(L == [{p: R(4, 5), n: 25}] and near(w, 0.187, 1e-3), (L, float(w)))


f26b = 3 * exp(x) + 1


@pruef("2026-bb-gk-B2.2a")
def _():
    # f > 1; Wertemenge ]1; ∞[
    return ok(limit(f26b, x, -oo) == 1 and solve(f26b, x) == [] and f26b.subs(x, -50) > 1, limit(f26b, x, -oo))


@pruef("2026-bb-gk-B2.2b")
def _():
    # y = 3x + 4
    tg = diff(f26b, x).subs(x, 0) * x + f26b.subs(x, 0)
    return ok(expand(tg) == 3 * x + 4, tg)


@pruef("2026-bb-gk-B2.2c")
def _():
    # 16/3 + 4/3 √10 ≈ 9,55
    tg = 3 * x + 4
    xs = solve(tg, x)[0]
    U = abs(xs) + 4 + sqrt(xs**2 + 16)
    return ok(xs == R(-4, 3) and simplify(U - (R(16, 3) + R(4, 3) * sqrt(10))) == 0 and near(U, 9.55), float(U))


@pruef("2026-bb-gk-B2.2d")
def _():
    # 3 − 3e^u
    I = integrate(f26b - 1, (x, u, 0))
    return ok(simplify(I - (3 - 3 * exp(u))) == 0, I)


@pruef("2026-bb-gk-B2.2e")
def _():
    # a = ln(3/5) ≈ −0,51
    ges = 3 - 3 * exp(-log(5))
    L = solve(3 - 3 * exp(a) - ges / 2, a)
    return ok(ges == R(12, 5) and L == [log(R(3, 5))] and near(L[0], -0.51), (ges, L))


nr("2026-bb-gk-B2.2f", "Transformation beschreiben")

k26 = 60 * exp(-x / 400) + 20


@pruef("2026-bb-gk-B2.2g")
def _():
    # 80
    return ok(k26.subs(x, 0) == 80, k26.subs(x, 0))


@pruef("2026-bb-gk-B2.2h")
def _():
    # mittlere ≈ −0,139; k'(60) ≈ −0,129; Abweichung ≈ 0,08
    mr = (k26.subs(x, 60) - k26.subs(x, 0)) / 60
    kr = diff(k26, x).subs(x, 60)
    ab = (mr - kr) / kr
    return ok(near(mr, -0.139, 1e-3) and near(kr, -0.129, 1e-3) and near(ab, 0.08, 5e-3) and ab < 0.1, (float(mr), float(kr), float(ab)))


@pruef("2026-bb-gk-B2.2i")
def _():
    # k − 20 = −400 k'
    return ok(simplify((k26 - 20) + 400 * diff(k26, x)) == 0, "")


P26 = dict(A=Matrix([0, -2, 0]), B=Matrix([5, -1, 0]), C=Matrix([5, 1, 0]), D=Matrix([0, 2, 0]), S=Matrix([2, 0, 4]))


@pruef("2026-bb-gk-B3a")
def _():
    # AD = 2 BC; Fläche 15
    A_, B_, C_, D_ = (P26[k] for k in "ABCD")
    Fl = R(1, 2) * ((D_ - A_).norm() + (C_ - B_).norm()) * 5
    return ok(D_ - A_ == 2 * (C_ - B_) and Fl == 15, Fl)


@pruef("2026-bb-gk-B3b")
def _():
    # cos α = 7/13; 57,4°
    from sympy import acos
    C_, D_, S_ = (P26[k] for k in "CDS")
    v1, v2 = D_ - C_, S_ - C_
    c = v1.dot(v2) / (v1.norm() * v2.norm())
    al = float(acos(c) * 180 / pi)
    return ok(c == R(7, 13) and near(al, 57.4, 0.05), (c, al))


@pruef("2026-bb-gk-B3c")
def _():
    # t = 7/26
    C_, D_, S_ = (P26[k] for k in "CDS")
    Pp = C_ + t * (S_ - C_)
    tt = solve((Pp - D_).dot(S_ - C_), t)[0]
    # Katalog-Zwischenwert t = 7/26; sympy: DP · CS = −14 + 26t = 0 ⇒ t = 7/13 (Deutung des Ergebnisses unberührt)
    return ok(tt == R(7, 26), f"t = {tt} (Katalog-Zwischenwert t = 7/26)")


@pruef("2026-bb-gk-B3d")
def _():
    # W = (1|1|2); T(1|−1|2)
    D_, S_ = P26['D'], P26['S']
    W = (D_ + S_) / 2
    T_ = Matrix([W[0], -W[1], W[2]])
    return ok(list(W) == [1, 1, 2] and list(T_) == [1, -1, 2], (list(W), list(T_)))


@pruef("2026-bb-gk-B3e")
def _():
    # −4x + 2z = −10
    C_, W_, U_ = P26['C'], Matrix([1, 1, 2]), Matrix([R(7, 2), R(-1, 2), 2])
    n = W_ - C_
    d = n.dot(U_)
    M = (C_ + W_) / 2
    return ok(list(n) == [-4, 0, 2] and d == -10 and n.dot(M) == -10, (list(n), d))


@pruef("2026-bb-gk-B4a")
def _():
    # P(X = 3) ≈ 0,0031 für B(10; 0,75)
    p = binom_p(10, R(3, 4), 3, 3)
    return ok(p == binomial(10, 3) * R(3, 4)**3 * R(1, 4)**7 and near(p, 0.0031, 1e-4), float(p))


@pruef("2026-bb-gk-B4b")
def _():
    # ≈ 0,474
    p = binom_p(10, R(3, 4), 0, 7)
    return ok(near(p, 0.474, 1e-3), float(p))


@pruef("2026-bb-gk-B4c")
def _():
    # P(X = 6) = P(Y = 4) ≈ 0,146
    w = (binom_p(10, R(3, 4), 6, 6), binom_p(10, R(1, 4), 4, 4))
    return ok(w[0] == w[1] and near(w[0], 0.146, 1e-3), float(w[0]))


@pruef("2026-bb-gk-B4d")
def _():
    # 0,6 = 6 · 0,1
    return ok(R(3, 4) * R(4, 5) == 6 * R(1, 4) * R(2, 5), "")


@pruef("2026-bb-gk-B4e")
def _():
    # a = 0,4
    L = solve(R(3, 4) * R(1, 5) + R(1, 4) * (1 - a) - R(3, 10), a)
    return ok(L == [R(2, 5)], L)


@pruef("2026-bb-gk-B4f")
def _():
    # Term steigt in a; a = 0,4: 0,5; a = 0,6: 0,6
    term = R(3, 4) * R(1, 5) / (R(3, 4) * R(1, 5) + R(1, 4) * (1 - a))
    w = (term.subs(a, R(2, 5)), term.subs(a, R(3, 5)), diff(term, a).subs(a, R(1, 2)) > 0)
    return ok(w == (R(1, 2), R(3, 5), True), w)


# ================================ Lauf =======================================

def lauf(ids=None):
    ids = ids or list(PRUEF) + [i for i in NICHT_RECHENBAR if i not in PRUEF]
    out = {}
    for i in ids:
        if i in PRUEF:
            try:
                out[i] = PRUEF[i]()
            except Exception as ex:  # Skriptfehler je Zeile festhalten
                out[i] = f"offen: Skriptfehler {type(ex).__name__}: {ex}"
        elif i in NICHT_RECHENBAR:
            out[i] = "nicht rechenbar"
        else:
            out[i] = "offen: keine Prüffunktion"
    return out


if __name__ == "__main__":
    for i, w in lauf(sys.argv[1:] or None).items():
        print(f"{i};{w}")
