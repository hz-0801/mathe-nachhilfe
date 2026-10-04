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
                   simplify, Abs, log, ln, S, Eq, Interval, Union, Poly,
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
