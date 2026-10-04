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
