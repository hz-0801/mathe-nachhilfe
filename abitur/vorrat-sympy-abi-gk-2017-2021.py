#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rechenkontrolle für die Beitabelle abitur/vorrat-abi-gk-2017-2021.csv
(Muster: werkzeuge/vorrat-sympy-abi-gk.py).

Je rechenbarer Teilaufgabe eine Funktion unter ihrer id in PRUEF; sie gibt
"ok" oder "abw: <eigener Wert>" zurück und prüft die Zahlen aus kurz und
zwischen (Katalogwert als Kommentar). Teilaufgaben ohne rechnerisches
Ergebnis stehen in NICHT_RECHENBAR mit Grund.

Aufruf: python3 vorrat-sympy-abi-gk-2017-2021.py [id ...]
        python3 vorrat-sympy-abi-gk-2017-2021.py --eintragen <beitabelle.csv>
Ohne ids werden alle Funktionen ausgeführt, Ausgabe je Zeile "id;wert";
--eintragen schreibt die Werte in die Spalte sympy der Beitabelle.
"""
import csv
import io
import math
import sys
from sympy import (symbols, Rational as R, sqrt, exp, E, diff, solve, Matrix,
                   binomial, atan, asin, acos, pi, simplify, log, N, nsimplify,
                   integrate, Abs, sin, cos, tan, expand, factor)

x, y, z, t, s, a, b, c, k, n = symbols('x y z t s a b c k n', real=True)

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


def binom_p(n_, p, kmin, kmax):
    return sum(binomial(n_, i) * R(p)**i * (1 - R(p))**(n_ - i) for i in range(kmin, kmax + 1))


def grad(w):
    return float(w) * 180 / math.pi


def vec(*k_):
    return Matrix(k_)


# ================================ 2017-be-gk =================================
f17 = -R(1, 500) * x**3 + R(3, 50) * x**2 + 1


@pruef("2017-be-gk-B1.1a")
def _():
    # T(0 | 1), H(20 | 9); f″(0) = 0,12, f″(20) = −0,12
    f1, f2 = diff(f17, x), diff(f17, x, 2)
    st = solve(f1, x)
    w = (sorted(st), f17.subs(x, 0), f17.subs(x, 20), f2.subs(x, 0), f2.subs(x, 20))
    return ok(w == ([0, 20], 1, 9, R(3, 25), -R(3, 25)), w)


@pruef("2017-be-gk-B1.1b")
def _():
    # m = 0,4; x = 10 ± 10/√3 ≈ 4,23 / 15,77
    m = (f17.subs(x, 20) - f17.subs(x, 0)) / 20
    st = solve(diff(f17, x) - m, x)
    w = (m, [float(v) for v in sorted(st)])
    return ok(m == R(2, 5) and near(w[1][0], 4.226) and near(w[1][1], 15.774), w)


@pruef("2017-be-gk-B1.1c")
def _():
    # W(10 | 5), f′(10) = 0,6, α ≈ 30,96°
    xw = solve(diff(f17, x, 2), x)[0]
    m = diff(f17, x).subs(x, xw)
    w = (xw, f17.subs(x, xw), m, grad(atan(m)))
    return ok(xw == 10 and w[1] == 5 and m == R(3, 5) and near(w[3], 30.96, 0.01), w)


@pruef("2017-be-gk-B1.1d")
def _():
    # A = 100, V = 400
    A = integrate(f17, (x, 0, 20))
    return ok(A == 100 and 4 * A == 400, A)


@pruef("2017-be-gk-B1.1e")
def _():
    # f′(1,5) = 0,1665 → 9,45°; f′(8,5) = 0,5865 → 30,39°; Differenz 20,9°
    f1 = diff(f17, x)
    m1, m2 = f1.subs(x, R(3, 2)), f1.subs(x, R(17, 2))
    a1, a2 = grad(atan(m1)), grad(atan(m2))
    w = (m1, m2, a1, a2, a2 - a1)
    return ok(m1 == R(333, 2000) and m2 == R(1173, 2000) and near(a1, 9.453, 0.01)
              and near(a2, 30.392, 0.01) and near(a2 - a1, 20.94, 0.01), w)


@pruef("2017-be-gk-B1.1f")
def _():
    # a = −0,00128, b = 0,048, c = 1,5
    g = a * x**3 + b * x**2 + c
    loes = solve([g.subs(x, 0) - R(3, 2), diff(g, x).subs(x, 25), g.subs(x, 25) - R(23, 2)], [a, b, c])
    return ok(loes == {a: -R(4, 3125), b: R(6, 125), c: R(3, 2)}, loes)


f17b = (x**2 - 2 * x + 1) * exp(-x)


@pruef("2017-be-gk-B1.2a")
def _():
    # (0 | 1), (1 | 0); T(1 | 0), H(3 | 4e⁻³ ≈ 0,199); f″ = (x² − 6x + 7)e^(−x), f″(1) = 2/e, f″(3) = −2e⁻³
    f1, f2 = diff(f17b, x), diff(f17b, x, 2)
    st = sorted(solve(f1, x))
    w = (f17b.subs(x, 0), solve(f17b, x), st, simplify(f2 / exp(-x)), f2.subs(x, 1), f2.subs(x, 3), float(f17b.subs(x, 3)))
    return ok(w[0] == 1 and w[1] == [1] and st == [1, 3] and expand(w[3]) == x**2 - 6 * x + 7
              and w[4] == 2 / E and w[5] == -2 * exp(-3) and near(w[6], 0.199, 0.001), w)


@pruef("2017-be-gk-B1.2b")
def _():
    # f(0,5) ≈ 0,15, f(2) ≈ 0,14
    w = (float(f17b.subs(x, R(1, 2))), float(f17b.subs(x, 2)))
    return ok(near(w[0], 0.152) and near(w[1], 0.135), w)


@pruef("2017-be-gk-B1.2c")
def _():
    # x_P = 3 − √2 ≈ 1,586, f′(x_P) ≈ 0,170; 3 + √2 ≈ 4,41
    st = solve(diff(f17b, x, 2), x)
    xp = min(st)
    w = (st, float(xp), float(diff(f17b, x).subs(x, xp)), float(max(st)))
    return ok(simplify(xp - (3 - sqrt(2))) == 0 and near(w[2], 0.170, 0.001) and near(w[3], 4.414), w)


@pruef("2017-be-gk-B1.2d")
def _():
    # F′ = f; F(1) − F(0) = 1 − 2/e ≈ 0,2642 → 26,4 m²
    F = (-x**2 - 1) * exp(-x)
    A = F.subs(x, 1) - F.subs(x, 0)
    w = (simplify(diff(F, x) - f17b), A, float(A))
    return ok(w[0] == 0 and simplify(A - (1 - 2 / E)) == 0 and near(w[2], 0.2642, 1e-3)
              and near(100 * w[2], 26.4, 0.05), w)


@pruef("2017-be-gk-B1.2e")
def _():
    # t(x) = −3x + 1; Dreieck 1/6 FE ≈ 16,7 m²; Einsparung ≈ 9,8 m²
    m = diff(f17b, x).subs(x, 0)
    tang = m * x + 1
    n0 = solve(tang, x)[0]
    A = R(1, 2) * 1 * n0
    ein = (1 - 2 / E) - A
    w = (m, n0, A, float(100 * A), float(100 * ein))
    return ok(m == -3 and n0 == R(1, 3) and A == R(1, 6) and near(w[3], 16.67, 0.01) and near(w[4], 9.8, 0.05), w)


@pruef("2017-be-gk-B1.2f")
def _():
    # c = 1, b = −3, a = 2, p′(1) = 1
    p = a * x**2 + b * x + c
    loes = solve([p.subs(x, 0) - 1, diff(p, x).subs(x, 0) + 3, p.subs(x, 1)], [a, b, c])
    p1 = diff(p, x).subs(loes).subs(x, 1)
    return ok(loes == {a: 2, b: -3, c: 1} and p1 == 1, (loes, p1))


@pruef("2017-be-gk-B2.1a")
def _():
    # r = (60 | 11 | 30), |r| = √4621 ≈ 67,98 m, 244,7 km/h, α ≈ 26,2°
    r = vec(1200, 251, 30) - vec(1140, 240, 0)
    betrag = sqrt(r.dot(r))
    alpha = grad(asin(30 / betrag))
    w = (list(r), betrag, float(betrag), float(betrag) * 3.6, alpha)
    return ok(list(r) == [60, 11, 30] and betrag == sqrt(4621) and near(w[2], 67.98, 0.01)
              and near(w[3], 244.7, 0.05) and near(alpha, 26.2, 0.05), w)


@pruef("2017-be-gk-B2.1b")
def _():
    # |(60 | 11 | 0)| = 61; 7000/61 ≈ 114,75; R(8040 | 1505 | 0)
    d = vec(60, 11, 0)
    betrag = sqrt(d.dot(d))
    Rp = vec(1140, 240, 0) + 115 * d
    w = (betrag, float(7000 / betrag), list(Rp))
    return ok(betrag == 61 and near(w[1], 114.75, 0.01) and list(Rp) == [8040, 1505, 0], w)


@pruef("2017-be-gk-B2.1c")
def _():
    # s = 70, y = 1505, z = 615
    h = vec(1740, 350, 300) + s * vec(90, R(33, 2), R(9, 2))
    s0 = solve(h[0] - 8040, s)[0]
    w = (s0, list(h.subs(s, s0)))
    return ok(s0 == 70 and w[1] == [8040, 1505, 615], w)


@pruef("2017-be-gk-B2.1d")
def _():
    # r_neu · n = 0; 1740 − 6000 = −4260; z = 480
    nv = vec(1, 0, -20)
    sp = vec(90, R(33, 2), R(9, 2)).dot(nv)
    probe = 1740 - 20 * 300
    z0 = solve(8040 - 20 * z + 1560, z)[0]
    w = (sp, probe, z0)
    return ok(sp == 0 and probe == -4260 and z0 == 480, w)


nr("2017-be-gk-B2.2a", "Koordinaten aus der Körperbeschreibung abgelesen")


@pruef("2017-be-gk-B2.2b")
def _():
    # n = (60 | 0 | 10) → (6 | 0 | 1); 6x + z = 60 für A, E, F
    A, B, F_, E_ = vec(10, 0, 0), vec(10, 10, 0), vec(9, 9, 6), vec(9, 1, 6)
    nv = (B - A).cross(F_ - A)
    w = (list(nv), [6 * P[0] + P[2] for P in (A, B, F_, E_)])
    return ok(list(nv) == [60, 0, 10] and w[1] == [60, 60, 60, 60], w)


@pruef("2017-be-gk-B2.2c")
def _():
    # cos γ = 1/√37, γ ≈ 80,54°; |AC| = √200 ≈ 14,14; |DF| = √198 ≈ 14,07; |AS| = √131 ≈ 11,45
    n1, n2 = vec(6, 0, 1), vec(0, 0, 1)
    cg = Abs(n1.dot(n2)) / (sqrt(n1.dot(n1)) * sqrt(n2.dot(n2)))
    gam = grad(acos(cg))
    A, C, D, F_, S = vec(10, 0, 0), vec(0, 10, 0), vec(0, 0, 0), vec(9, 9, 6), vec(5, 5, 9)
    la = lambda P, Q: (Q - P).dot(Q - P)
    w = (cg, gam, la(A, C), la(D, F_), la(A, S))
    return ok(cg == 1 / sqrt(37) and near(gam, 80.54, 0.01) and w[2:] == (200, 198, 131), w)


@pruef("2017-be-gk-B2.2d")
def _():
    # Seitenhöhe 5, Mantel 80
    hs = sqrt(3**2 + 4**2)
    return ok(hs == 5 and 4 * R(1, 2) * 8 * hs == 80, hs)


@pruef("2017-be-gk-B2.2e")
def _():
    # P1(9,5 | 0,5 | 3); |P1D| = |P1B| = √99,5 ≈ 9,975; 8 · √99,5 ≈ 79,8
    A, E_, D, B = vec(10, 0, 0), vec(9, 1, 6), vec(0, 0, 0), vec(10, 10, 0)
    P1 = (A + E_) / 2
    d1, d2 = (D - P1).dot(D - P1), (B - P1).dot(B - P1)
    w = (list(P1), d1, d2, float(8 * sqrt(d1)))
    return ok(list(P1) == [R(19, 2), R(1, 2), 3] and d1 == d2 == R(199, 2) and near(w[3], 79.8, 0.05), w)


@pruef("2017-be-gk-B3.1a")
def _():
    return ok(binomial(6, 4) == 15, binomial(6, 4))


@pruef("2017-be-gk-B3.1b")
def _():
    # P(A) = 247/490 ≈ 0,504; P(B) ≈ 0,496
    pa = binomial(47, 10) / binomial(50, 10)
    return ok(pa == R(247, 490) and near(pa, 0.504, 5e-4) and near(1 - pa, 0.496, 5e-4), pa)


@pruef("2017-be-gk-B3.1c")
def _():
    pf = R(1, 10) * R(5, 100) + R(3, 10) * R(3, 100) + R(2, 10) * R(4, 100) + R(4, 10) * R(2, 100)
    return ok(pf == R(3, 100), pf)


@pruef("2017-be-gk-B3.1d")
def _():
    w = R(1, 10) * R(5, 100) / R(3, 100)
    return ok(w == R(1, 6), w)


@pruef("2017-be-gk-B3.1e")
def _():
    w = float(R(95, 100)**20)
    return ok(near(w, 0.358, 5e-4), w)


@pruef("2017-be-gk-B3.1f")
def _():
    # P(X ≤ 1) für n = 200, p = 0,02 ≈ 0,0894 = 200 · 0,02 · 0,98^199 + 0,98^200
    w = float(binom_p(200, R(2, 100), 0, 1))
    term = float(200 * R(98, 100)**199 * R(2, 100) + R(98, 100)**200)
    return ok(near(w, 0.0894, 5e-4) and near(term, w, 1e-9), (w, term))


@pruef("2017-be-gk-B3.1g")
def _():
    # n ≥ 73,4 → 74; 1 − 0,96^73 ≈ 0,9492, 1 − 0,96^74 ≈ 0,9512
    grenze = math.log(0.05) / math.log(0.96)
    w = (grenze, 1 - 0.96**73, 1 - 0.96**74)
    return ok(near(grenze, 73.4, 0.05) and near(w[1], 0.9492, 5e-4) and near(w[2], 0.9512, 5e-4) and w[1] < 0.95 <= w[2], w)


@pruef("2017-be-gk-B3.2a")
def _():
    pa1 = R(2, 3) * R(1, 2)
    pa2 = R(1, 3) * R(6, 10) + R(2, 3) * R(1, 2)
    return ok(pa1 == R(1, 3) and pa2 == R(8, 15), (pa1, pa2))


@pruef("2017-be-gk-B3.2b")
def _():
    w = {(1, "Rot"): R(1, 3) * R(1, 2), (2, "Blau"): R(2, 3) * R(1, 4), (2, "Schwarz"): R(2, 3) * R(1, 4),
         (1, "Blau"): R(1, 3) * R(1, 4), (2, "Rot"): R(2, 3) * R(1, 2)}
    gleich = [k_ for k_, v in w.items() if v == R(1, 6)]
    return ok(sorted(gleich) == [(1, "Rot"), (2, "Blau"), (2, "Schwarz")] and w[(1, "Blau")] == R(1, 12), w)


@pruef("2017-be-gk-B3.2c")
def _():
    # P(X = 4) ≈ 0,2508; P(X ≤ 4) = 0,6331; P(X ≤ 3) = 0,3823; P(C2) = 0,3669
    p4 = float(binom_p(10, R(2, 5), 4, 4))
    k4 = float(binom_p(10, R(2, 5), 0, 4))
    k3 = float(binom_p(10, R(2, 5), 0, 3))
    w = (p4, k4, k3, 1 - k4)
    return ok(near(p4, 0.2508, 5e-5) and near(k4, 0.6331, 5e-5) and near(k3, 0.3823, 5e-5) and near(1 - k4, 0.3669, 5e-5), w)


@pruef("2017-be-gk-B3.2d")
def _():
    # P(Y = 15) ≈ 0,048 < 0,05; (30 über 15) = 155 117 520
    p = 0.3669
    w = (binomial(30, 15), float(binomial(30, 15)) * p**15 * (1 - p)**15)
    return ok(w[0] == 155117520 and near(w[1], 0.048, 5e-4) and w[1] < 0.05, w)


@pruef("2017-be-gk-B3.2e")
def _():
    # P(X = 5) = 0,8338 − 0,6331 = 0,2007; Produkt ≈ 0,127
    k5 = float(binom_p(10, R(2, 5), 0, 5))
    k4 = float(binom_p(10, R(2, 5), 0, 4))
    p5 = k5 - k4
    w = (k5, k4, p5, p5 * k4)
    return ok(near(k5, 0.8338, 5e-5) and near(p5, 0.2007, 5e-5) and near(p5 * k4, 0.127, 5e-4), w)


# ================================ 2018-be-gk =================================
g18 = R(1, 1000) * (R(1, 2000) * x**4 - 10 * x**2 + 50000)
h18 = R(5, 100) * x**2 + 54
f18 = -R(8, 1000) * x**2 + 54


@pruef("2018-be-gk-B1.1a")
def _():
    # 4 m; h(−20) = 74; AB = 24
    w = (h18.subs(x, 0) - g18.subs(x, 0), h18.subs(x, -20), h18.subs(x, -20) - 50)
    return ok(w == (4, 74, 24), w)


@pruef("2018-be-gk-B1.1b")
def _():
    A = integrate(h18 - 50, (x, -20, 0))
    return ok(A == R(640, 3) and near(A, 213.3, 0.05), A)


@pruef("2018-be-gk-B1.1c")
def _():
    # x = −100, 0, 100; g″(0) = −0,02, g″(±100) = 0,04; g(0) = 50, g(±100) = 0
    g1, g2 = diff(g18, x), diff(g18, x, 2)
    st = sorted(solve(g1, x))
    w = (st, g2.subs(x, 0), g2.subs(x, 100), g2.subs(x, -100), g18.subs(x, 0), g18.subs(x, 100))
    return ok(w == ([-100, 0, 100], -R(1, 50), R(1, 25), R(1, 25), 50, 0), w)


@pruef("2018-be-gk-B1.1d")
def _():
    # x = 100/√3 ≈ 57,74; g = 200/9 ≈ 22,22; g′ ≈ −0,77
    st = [v for v in solve(diff(g18, x, 2), x) if v > 0][0]
    w = (st, float(st), g18.subs(x, st), float(g18.subs(x, st)), float(diff(g18, x).subs(x, st)))
    return ok(simplify(st - 100 / sqrt(3)) == 0 and near(w[1], 57.74, 0.01) and w[2] == R(200, 9)
              and near(w[3], 22.22, 0.01) and near(w[4], -0.77, 0.005), w)


@pruef("2018-be-gk-B1.1e")
def _():
    # c = 54, b = 0, g(60) = 20,48, f(60) = 25,2, a = −0,008
    f = a * x**2 + b * x + c
    g60 = g18.subs(x, 60)
    loes = solve([f.subs(x, 0) - 54, diff(f, x).subs(x, 0), f.subs(x, 60) - (g60 + R(472, 100))], [a, b, c])
    return ok(g60 == R(512, 25) and loes == {a: -R(1, 125), b: 0, c: 54} and g60 + R(472, 100) == R(126, 5), (g60, loes))


@pruef("2018-be-gk-B1.1f")
def _():
    # u = 2000 + 2000√3 ≈ 5464,1; x ≈ 73,92; y ≈ 10,29; f(40) = 41,2, f(60) = 25,2
    u = symbols('u', positive=True)
    gl = expand((g18 - f18) * 2000000)
    us = [v for v in solve(gl.subs(x**4, u**2).subs(x**2, u), u) if v > 0][0]
    xs = sqrt(us)
    w = (us, float(us), float(xs), float(g18.subs(x, xs)), f18.subs(x, 40), f18.subs(x, 60))
    return ok(expand(gl) == x**4 - 4000 * x**2 - 8000000 and simplify(us - (2000 + 2000 * sqrt(3))) == 0
              and near(w[1], 5464.1, 0.05) and near(w[2], 73.92, 0.01) and near(w[3], 10.29, 0.01)
              and w[4] == R(206, 5) and w[5] == R(126, 5), w)


@pruef("2018-be-gk-B1.1g")
def _():
    # x = 20√5 ≈ 44,72; d = 6; f = 38, g = 32
    d = f18 - g18
    st = [v for v in solve(diff(d, x), x) if v > 0][0]
    w = (st, float(st), d.subs(x, st), f18.subs(x, st), g18.subs(x, st))
    return ok(simplify(st - 20 * sqrt(5)) == 0 and near(w[1], 44.72, 0.01) and w[2:] == (6, 38, 32), w)


f18b = (x + 1) * exp(-R(1, 2) * x)


@pruef("2018-be-gk-B1.2a")
def _():
    from sympy import limit, oo
    return ok(limit(f18b, x, oo) == 0, limit(f18b, x, oo))


@pruef("2018-be-gk-B1.2b")
def _():
    # f′(0) = 0,5; tan φ = 1/3; φ ≈ 18,43°; arctan 0,5 ≈ 26,57°
    m = diff(f18b, x).subs(x, 0)
    tphi = Abs((1 - m) / (1 + m))
    w = (m, tphi, grad(atan(tphi)), grad(atan(m)), grad(atan(1)) - grad(atan(m)))
    return ok(m == R(1, 2) and tphi == R(1, 3) and near(w[2], 18.43, 0.01) and near(w[3], 26.57, 0.01)
              and near(w[4], 18.43, 0.01), w)


@pruef("2018-be-gk-B1.2c")
def _():
    # F′ = f; Nullstelle −1; A = 4√e − 6,5 ≈ 0,09; F(0) = −6, F(−1) = −4√e ≈ −6,595
    F = (-2 * x - 6) * exp(-R(1, 2) * x)
    A = integrate(f18b - (x + 1), (x, -1, 0))
    w = (simplify(diff(F, x) - f18b), solve(f18b, x), A, float(A), F.subs(x, 0), F.subs(x, -1), float(F.subs(x, -1)))
    return ok(w[0] == 0 and w[1] == [-1] and simplify(A - (4 * sqrt(E) - R(13, 2))) == 0 and near(w[3], 0.09, 0.005)
              and w[4] == -6 and near(w[6], -6.595, 0.001), w)


@pruef("2018-be-gk-B1.2d")
def _():
    st = solve(diff(f18b, x), x)
    w = (st, f18b.subs(x, 1), float(f18b.subs(x, 1)))
    return ok(st == [1] and w[1] == 2 * exp(-R(1, 2)) and near(w[2], 1.213, 0.001), w)


@pruef("2018-be-gk-B1.2e")
def _():
    # f(2) ≈ 1,1036, f(6) ≈ 0,3485, m ≈ −0,1888, y ≈ −0,189x + 1,481
    f2, f6 = float(f18b.subs(x, 2)), float(f18b.subs(x, 6))
    m = (f6 - f2) / 4
    n0 = f2 - 2 * m
    w = (f2, f6, m, n0)
    return ok(near(f2, 1.1036, 5e-5) and near(f6, 0.3485, 5e-5) and near(m, -0.1888, 5e-5) and near(n0, 1.481, 5e-4), w)


@pruef("2018-be-gk-B1.2f")
def _():
    # f″ = 0,25(x − 3)e^(−0,5x); f′(3) = −e^(−1,5) ≈ −0,2231
    f2 = diff(f18b, x, 2)
    st = solve(f2, x)
    w = (simplify(f2 - R(1, 4) * (x - 3) * exp(-R(1, 2) * x)), st, diff(f18b, x).subs(x, 3), float(diff(f18b, x).subs(x, 3)))
    return ok(w[0] == 0 and st == [3] and w[2] == -exp(-R(3, 2)) and near(w[3], -0.2231, 5e-5) and w[3] < -0.222, w)


@pruef("2018-be-gk-B1.2g")
def _():
    # m_f ≈ −0,109; m_h = −0,15; a = 1,2; b = −ln 24/6 ≈ −0,53
    mf = float((f18b.subs(x, 6) - f18b.subs(x, 0)) / 6)
    mh = (0.3 - 1.2) / 6
    bb = solve((6 + R(6, 5)) * exp(6 * b) - R(3, 10), b)[0]
    w = (mf, mh, bb, float(bb))
    return ok(near(mf, -0.109, 5e-4) and mh == -0.15 and abs(mh) > abs(mf) and simplify(bb + log(24) / 6) == 0
              and near(w[3], -0.53, 0.005), w)


A18, B18, C18, D18 = vec(0, 0, 5), vec(R(22, 5), 44, 5), vec(R(1, 5), 2, 7), vec(R(24, 5), 48, 9)


@pruef("2018-be-gk-B2.1a")
def _():
    nv = (B18 - A18).cross(C18 - A18)
    w = (list(nv), [-10 * P[0] + P[1] for P in (A18, B18, C18)])
    return ok(list(nv) == [88, -R(44, 5), 0] and w[1] == [0, 0, 0], w)


@pruef("2018-be-gk-B2.1b")
def _():
    w = (-10 * D18[0] + D18[1], vec(-10, 1, 0).dot(vec(0, 0, 1)))
    return ok(w == (0, 0), w)


@pruef("2018-be-gk-B2.1c")
def _():
    # u · v = 2044,24; |u| ≈ 44,22; |v| ≈ 46,27; cos ≈ 0,9991; φ ≈ 2,5°; Schnittpunkt (−4,4 | −44 | 5)
    u, v = B18 - A18, D18 - C18
    sp = u.dot(v)
    bu, bv = sqrt(u.dot(u)), sqrt(v.dot(v))
    cphi = sp / (bu * bv)
    phi = grad(acos(cphi))
    r_, s_ = symbols('r_ s_')
    loes = solve(list(A18 + r_ * u - (C18 + s_ * v)), [r_, s_])
    P = A18 + loes[r_] * u
    w = (sp, float(bu), float(bv), float(cphi), phi, list(P))
    return ok(sp == R(204424, 100) and near(w[1], 44.22, 0.005) and near(w[2], 46.27, 0.005)
              and near(w[3], 0.9991, 5e-5) and near(phi, 2.5, 0.05) and list(P) == [-R(22, 5), -44, 5], w)


@pruef("2018-be-gk-B2.1d")
def _():
    PQ = vec(42, 36, 0) - vec(82, 40, 0)
    l2 = PQ.dot(PQ)
    v_ = float(sqrt(l2)) / 1.5
    w = (list(PQ), l2, float(sqrt(l2)), v_, v_ * 3.6)
    return ok(list(PQ) == [-40, -4, 0] and l2 == 1616 and near(w[2], 40.2, 0.05) and near(v_, 26.8, 0.05) and near(w[4], 96.5, 0.05), w)


@pruef("2018-be-gk-B2.1e")
def _():
    r_ = symbols('r_')
    bahn = vec(42, 36, 0) + r_ * vec(-40, -4, 0)
    r0 = solve(-10 * bahn[0] + bahn[1], r_)[0]
    P = bahn.subs(r_, r0)
    w = (r0, [float(v) for v in P], R(3, 2) * r0, float(R(3, 2) * r0))
    return ok(r0 == R(32, 33) and near(w[1][0], 3.2, 0.05) and near(w[1][1], 32.1, 0.05) and w[2] == R(16, 11) and near(w[3], 1.45, 0.005), w)


A2, B2, E2, F2 = vec(3, 0, 2), vec(0, 3, 2), vec(6, 0, 0), vec(0, 6, 0)


@pruef("2018-be-gk-B2.2a")
def _():
    M1, M2 = (A2 + B2) / 2, (E2 + F2) / 2
    d = M2 - M1
    l_ = sqrt(d.dot(d))
    w = (list(M1), list(M2), list(d), d.dot(d), float(l_), float(1.2 * l_))
    return ok(list(M1) == [R(3, 2), R(3, 2), 2] and list(M2) == [3, 3, 0] and d.dot(d) == R(17, 2)
              and near(w[4], 2.92, 0.005) and near(w[5], 3.50, 0.005), w)


@pruef("2018-be-gk-B2.2b")
def _():
    AB, EF, AE, BF = B2 - A2, F2 - E2, E2 - A2, F2 - B2
    w = (list(AB), list(EF), list(AE), list(BF), AE.dot(AE), BF.dot(BF))
    return ok(EF == 2 * AB and w[4] == w[5] == 13 and near(sqrt(13), 3.61, 0.005), w)


@pruef("2018-be-gk-B2.2c")
def _():
    nL = vec(2, 2, 3)
    cphi = 3 / sqrt(nL.dot(nL))
    w = (cphi, float(cphi), grad(acos(cphi)))
    return ok(cphi == 3 / sqrt(17) and near(w[1], 0.7276, 5e-5) and near(w[2], 43.3, 0.05), w)


@pruef("2018-be-gk-B2.2d")
def _():
    # t = 5/6; Licht (−1 | −5 | −3); S′(7 | 8 | 0)
    Rp, Sp, Tp = vec(5, 7, 3), vec(8, 13, 3), vec(2, 10, 3)
    Rs, Ts = vec(4, 2, 0), vec(1, 5, 0)
    t0 = solve(list(E2 + t * (F2 - E2) - Ts), t)
    licht = Rs - Rp
    k0 = solve((Sp + k * licht)[2], k)[0]
    Ss = Sp + k0 * licht
    w = (t0, list(licht), k0, list(Ss), list(Tp + licht))
    return ok(t0 == {t: R(5, 6)} and list(licht) == [-1, -5, -3] and k0 == 1 and list(Ss) == [7, 8, 0] and list(Tp + licht) == list(Ts), w)


nr("2018-be-gk-B2.2e", "Beschreibung eines Lösungswegs, keine Zahl")


@pruef("2018-be-gk-B3.1a")
def _():
    w = (R(4, 6) * R(3, 5), binomial(4, 2) / binomial(6, 2))
    return ok(w == (R(2, 5), R(2, 5)), w)


@pruef("2018-be-gk-B3.1b")
def _():
    # P(A) ≈ 0,2508; P(höchstens 1 von 9) ≈ 0,0705; P(B) ≈ 0,0282
    pa = float(binom_p(10, R(2, 5), 4, 4))
    p9 = float(binom_p(9, R(2, 5), 0, 1))
    w = (pa, p9, 0.4 * p9)
    return ok(near(pa, 0.2508, 5e-5) and near(p9, 0.0705, 5e-5) and near(w[2], 0.0282, 5e-5), w)


@pruef("2018-be-gk-B3.1c")
def _():
    w = (1 - 0.6, 1 - 0.6**10, 0.6**10)
    return ok(near(w[1], 0.9940, 5e-5) and near(w[2], 0.0060, 5e-5), w)


@pruef("2018-be-gk-B3.1d")
def _():
    return ok(R(2, 5) * 2 == R(4, 5), R(2, 5) * 2)


@pruef("2018-be-gk-B3.1e")
def _():
    # q(2) = 35/57 ≈ 0,614; x = 4; q(4) = 1/2
    q = 15 / (17 + x) * 14 / (16 + x)
    st = solve(q - R(1, 2), x)
    w = (q.subs(x, 2), float(q.subs(x, 2)), sorted(st), q.subs(x, 4), expand((17 + x) * (16 + x) - 420))
    return ok(w[0] == R(35, 57) and near(w[1], 0.614, 5e-4) and sorted(st) == [-37, 4] and w[3] == R(1, 2)
              and w[4] == x**2 + 33 * x - 148, w)


@pruef("2018-be-gk-B3.2a")
def _():
    # 0,3073; 0,9393; 0,5836; 0,3557
    k8 = float(binom_p(50, R(1, 5), 0, 8))
    k14 = float(binom_p(50, R(1, 5), 0, 14))
    k10 = float(binom_p(50, R(1, 5), 0, 10))
    w = (k8, k14, k10, k14 - k10)
    return ok(near(k8, 0.3073, 5e-5) and near(k14, 0.9393, 5e-5) and near(k10, 0.5836, 5e-5) and near(k14 - k10, 0.3557, 5e-5), w)


@pruef("2018-be-gk-B3.2b")
def _():
    p50 = float(binom_p(250, R(1, 5), 50, 50))
    p49 = float(binom_p(250, R(1, 5), 49, 49))
    p51 = float(binom_p(250, R(1, 5), 51, 51))
    w = (p49, p50, p51)
    return ok(near(p50, 0.0630, 5e-5) and p50 > p49 and p50 > p51, w)


nr("2018-be-gk-B3.2c", "Begründung über den Faktor 0,8, keine Zahl")


@pruef("2018-be-gk-B3.2d")
def _():
    w = 0.1**(1 / 25)
    return ok(near(w, 0.91201, 5e-6) and near(1 - w, 0.088, 5e-4), (w, 1 - w))


@pruef("2018-be-gk-B3.2e")
def _():
    dh = R(1000, 10) - R(107, 10)
    nn = dh - R(873, 10)
    bb = R(30, 10) - nn
    nd = R(107, 10) - bb
    w = (dh, nn, bb, nd)
    return ok(w == (R(893, 10), 2, 1, R(97, 10)), w)


@pruef("2018-be-gk-B3.2f")
def _():
    w = float(R(10, 1000) / R(107, 1000))
    return ok(near(w, 0.0935, 5e-5), w)


nr("2018-be-gk-B3.2g", "Beurteilung der Modellvoraussetzungen")


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


def eintragen(pfad):
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    kopf, daten = rows[0], rows[1:]
    ix = kopf.index("sympy")
    werte = lauf([r[0] for r in daten])
    zaehl = {}
    for r in daten:
        r[ix] = werte[r[0]]
        zaehl[r[ix].split(":")[0]] = zaehl.get(r[ix].split(":")[0], 0) + 1
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", lineterminator="\n")
        w.writerow(kopf)
        w.writerows(daten)
    print(f"{pfad}: {len(daten)} Zeilen – " + ", ".join(f"{k_} {v}" for k_, v in sorted(zaehl.items())))
    for r in daten:
        if not r[ix].startswith("ok") and r[ix] != "nicht rechenbar":
            print(f"  {r[0]}: {r[ix]}")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--eintragen"]:
        eintragen(sys.argv[2])
    else:
        for i, w in lauf(sys.argv[1:] or None).items():
            print(f"{i};{w}")
