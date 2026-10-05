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


# ================================ 2019-be-gk =================================
f19 = -5 * x**4 - 3 * x**2 + x


@pruef("2019-be-gk-A1.1a")
def _():
    F = -x**5 - x**3 + R(1, 2) * x**2
    w = (diff(f19, x), simplify(diff(F, x) - f19))
    return ok(w[0] == -20 * x**3 - 6 * x + 1 and w[1] == 0, w)


@pruef("2019-be-gk-A1.1b")
def _():
    # f′(0) = 1, f′(1) = −25, x_Max ≈ 0,154
    f1 = diff(f19, x)
    from sympy import nsolve
    xm = nsolve(f1, x, 0.2)
    w = (f1.subs(x, 0), f1.subs(x, 1), float(xm))
    return ok(w[0] == 1 and w[1] == -25 and near(w[2], 0.154, 5e-4), w)


g19, h19 = x**2 - 3, -x**2 + 2 * x + 1


@pruef("2019-be-gk-A1.2a")
def _():
    w = (sorted(solve(g19 - h19, x)), g19.subs(x, -1), h19.subs(x, -1), g19.subs(x, 2), h19.subs(x, 2), expand(g19 - h19))
    return ok(w[0] == [-1, 2] and w[1] == w[2] == -2 and w[3] == w[4] == 1 and w[5] == 2 * x**2 - 2 * x - 4, w)


@pruef("2019-be-gk-A1.2b")
def _():
    A = integrate(h19 - g19, (x, -1, 2))
    return ok(A == 9, A)


@pruef("2019-be-gk-A1.3a")
def _():
    rg = vec(2, -5, -1)
    w = (rg.dot(vec(1, 0, 2)), solve(list(vec(5, 3, 6) + t * rg - vec(5, 4, 6)), t))
    return ok(w[0] == 0 and w[1] == [], w)


nr("2019-be-gk-A1.3b", "Lagebegründung ohne Zahl")
nr("2019-be-gk-A1.4a", "Anteil 11/20 direkt abgelesen")
nr("2019-be-gk-A1.4b", "Begründung ohne Rechnung")


@pruef("2019-be-gk-A1.4c")
def _():
    w = (2 * R(11, 20) * R(9, 19), R(11 * 9, 1) / binomial(20, 2))
    return ok(w[0] == w[1] == R(99, 190) and near(w[0], 0.52, 5e-3), w)


hA = -R(1, 10) * t**4 + 20 * t**2
gB = -2 * t**3 + 30 * t**2


@pruef("2019-be-gk-B2.1a")
def _():
    h1, h2 = diff(hA, t), diff(hA, t, 2)
    w = (hA.subs(t, 2), hA.subs(t, 8), sorted(solve(h1, t)), h2.subs(t, 10), hA.subs(t, 10))
    return ok(w == (R(392, 5), R(4352, 5), [-10, 0, 10], -80, 1000), w)


@pruef("2019-be-gk-B2.1b")
def _():
    tm = [v for v in solve(diff(hA, t, 2), t) if v > 0][0]
    w = (tm, float(tm), diff(hA, t).subs(t, tm), float(diff(hA, t).subs(t, tm)))
    return ok(simplify(tm - 10 / sqrt(3)) == 0 and near(w[1], 5.77, 0.005) and simplify(w[2] - 800 * sqrt(3) / 9) == 0 and near(w[3], 154, 0.5), w)


@pruef("2019-be-gk-B2.1c")
def _():
    g = a * t**3 + b * t**2
    loes = solve([g.subs(t, 5) - 500, diff(g, t).subs(t, 5) - 150], [a, b])
    return ok(loes == {a: -2, b: 30}, loes)


@pruef("2019-be-gk-B2.1d")
def _():
    st = sorted(solve(diff(hA, t) - diff(gB, t), t))
    w = (hA.subs(t, 0), gB.subs(t, 0), st, diff(gB, t))
    return ok(w[0] == 0 and w[1] == 0 and st == [0, 5, 10] and w[3] == -6 * t**2 + 60 * t, w)


@pruef("2019-be-gk-B2.1e")
def _():
    d = diff(gB, t) - diff(hA, t)
    st = sorted(solve(diff(d, t), t))
    w = (expand(d), expand(diff(d, t)), st, [float(v) for v in st])
    return ok(w[0] == R(2, 5) * t**3 - 6 * t**2 + 20 * t and w[1] == R(6, 5) * t**2 - 12 * t + 20
              and simplify(st[0] - (5 - 5 / sqrt(3))) == 0 and near(w[3][0], 2.1, 0.05) and near(w[3][1], 7.9, 0.05), w)


@pruef("2019-be-gk-B2.1f")
def _():
    g1 = diff(gB, t)
    w = [g1.subs(t, v) for v in (0, 2, 4, 5, 6, 8, 10)]
    return ok(w == [0, 96, 144, 150, 144, 96, 0], w)


@pruef("2019-be-gk-B2.1g")
def _():
    A = integrate(diff(gB, t) - diff(hA, t), (t, 0, 5))
    return ok(A == R(125, 2), A)


h19b = 8 * t * exp(-R(4, 100) * t) + 50


@pruef("2019-be-gk-B2.2a")
def _():
    from sympy import limit, oo
    return ok(limit(h19b, t, oo) == 50, limit(h19b, t, oo))


@pruef("2019-be-gk-B2.2b")
def _():
    h1 = diff(h19b, t)
    st = solve(h1, t)
    w = (simplify(h1 - (8 - R(32, 100) * t) * exp(-R(4, 100) * t)), st, h19b.subs(t, 25), float(h19b.subs(t, 25)))
    return ok(w[0] == 0 and st == [25] and w[2] == 200 / E + 50 and near(w[3], 123.6, 0.05), w)


@pruef("2019-be-gk-B2.2c")
def _():
    h2 = diff(h19b, t, 2)
    st = solve(h2, t)
    w = (simplify(h2 - (-R(64, 100) + R(128, 10000) * t) * exp(-R(4, 100) * t)), st, float(h19b.subs(t, 50)), float(diff(h19b, t).subs(t, 50)))
    return ok(w[0] == 0 and st == [50] and near(w[2], 104.1, 0.05) and near(w[3], -1.08, 0.005), w)


@pruef("2019-be-gk-B2.2d")
def _():
    h7 = float(h19b.subs(t, 7))
    w = (h7, (h7 - 50) / 7)
    return ok(near(h7, 92.32, 0.005) and near(w[1], 6.0, 0.05), w)


@pruef("2019-be-gk-B2.2e")
def _():
    H = (-200 * t - 5000) * exp(-R(4, 100) * t) + 50 * t
    w = (simplify(diff(H, t) - h19b), float(H.subs(t, 70)), H.subs(t, 0), float((H.subs(t, 70) - H.subs(t, 0)) / 70))
    return ok(w[0] == 0 and near(w[1], 2344.6, 0.1) and w[2] == -5000 and near(w[3], 104.9, 0.05) and w[3] > 100, w)


@pruef("2019-be-gk-B2.2f")
def _():
    m = diff(h19b, t).subs(t, 70)
    h70 = h19b.subs(t, 70)
    n0 = h70 - 70 * m
    t1 = solve(-R(88, 100) * t + R(1457, 10) - 50, t)[0]
    t2 = solve(m * t + n0 - 50, t)[0]
    w = (float(m), float(h70), float(n0), float(t1), float(t2))
    return ok(simplify(m + R(144, 10) * exp(-R(28, 10))) == 0 and near(w[0], -0.876, 5e-4) and near(w[1], 84.05, 0.005)
              and near(w[2], 145.35, 0.005) and near(w[3], 108.75, 0.005) and near(w[4], 108.9, 0.05), w)


@pruef("2019-be-gk-B2.2g")
def _():
    kk = solve(k * 70 * exp(-R(28, 10)) + 50 - 100, k)[0]
    return ok(simplify(kk - 50 * exp(R(28, 10)) / 70) == 0 and near(kk, 11.75, 0.005), (kk, float(kk)))


@pruef("2019-be-gk-B2.2h")
def _():
    hk = k * t * exp(-R(4, 100) * t) + 50
    st = solve(diff(hk, t), t)
    w = (st, float(hk.subs({k: 10, t: 25})), hk.subs(t, 0))
    return ok(st == [25] and near(w[1], 142, 0.5) and w[2] == 50, w)


S19, N19 = vec(0, 40, 6), vec(30, 65, 7)


@pruef("2019-be-gk-B3.1a")
def _():
    u = N19 - S19
    l2 = u.dot(u)
    sa = 1 / sqrt(l2)
    w = (list(u), l2, float(sqrt(l2)), grad(asin(sa)))
    return ok(list(u) == [30, 25, 1] and l2 == 1526 and near(w[2], 39.06, 0.005) and near(w[3], 1.5, 0.05), w)


@pruef("2019-be-gk-B3.1b")
def _():
    P = vec(15, R(105, 2), R(13, 2)) + t * vec(0, 0, 1)
    t0 = solve(10 * P[0] + 5 * P[1] + 7 * P[2] - R(951, 2), t)[0]
    w = (t0, list(P.subs(t, t0)), 100 * t0 + 2)
    return ok(t0 == R(5, 2) and w[1] == [15, R(105, 2), 9] and w[2] == 252, w)


A19, B19 = vec(20, 60, R(13, 2)), vec(60, 65, 6)


@pruef("2019-be-gk-B3.1c")
def _():
    u = B19 - A19
    kol = solve(list(u - k * vec(30, 25, 1)), k)
    t0 = solve((A19 + t * u)[2] - R(64, 10), t)[0]
    P = A19 + t0 * u
    w = (list(u), kol, t0, list(P))
    return ok(list(u) == [40, 5, -R(1, 2)] and kol == [] and t0 == R(1, 5) and list(P) == [28, 61, R(32, 5)], w)


@pruef("2019-be-gk-B3.1d")
def _():
    u = B19 - A19
    L = float(sqrt(u.dot(u))) * 100
    s0 = L * 100 / 180
    w = (u.dot(u), L, s0)
    return ok(u.dot(u) == R(6501, 4) and near(L, 4031, 0.5) and near(s0, 2240, 0.5), w)


nr("2019-be-gk-B3.2a", "Zeichnung")
I19, J19, K19, L19 = vec(5, 0, 1), vec(2, 5, 0), vec(0, 5, 2), vec(1, 0, 5)


@pruef("2019-be-gk-B3.2b")
def _():
    IL, JK, IJ, KL = L19 - I19, K19 - J19, J19 - I19, L19 - K19
    w = (list(IL), list(JK), list(IJ), list(KL), IJ.dot(IJ), KL.dot(KL), IL.dot(IL), JK.dot(JK))
    return ok(IL == 2 * JK and list(IL) == [-4, 0, 4] and w[4] == w[5] == 35 and w[6] == 32 and w[7] == 8, w)


@pruef("2019-be-gk-B3.2c")
def _():
    IL, IJ = L19 - I19, J19 - I19
    sp = IL.dot(IJ)
    c_ = sp / (sqrt(IL.dot(IL)) * sqrt(IJ.dot(IJ)))
    w = (sp, float(c_), grad(acos(c_)), 180 - grad(acos(c_)))
    return ok(sp == 8 and near(w[1], 0.239, 5e-4) and near(w[2], 76.2, 0.05) and near(w[3], 103.8, 0.05), w)


@pruef("2019-be-gk-B3.2d")
def _():
    M1, M2 = (I19 + L19) / 2, (J19 + K19) / 2
    d = M2 - M1
    A = R(1, 2) * (sqrt(32) + sqrt(8)) * sqrt(d.dot(d))
    w = (list(M1), list(M2), d.dot(d), simplify(A), float(A))
    return ok(list(M1) == [3, 0, 3] and list(M2) == [1, 5, 1] and d.dot(d) == 33 and simplify(A - 3 * sqrt(66)) == 0 and near(w[4], 24.37, 0.005), w)


@pruef("2019-be-gk-B3.2e")
def _():
    nv = vec(5, 4, 5)
    w = (nv.dot(K19), nv.dot(L19))
    return ok(w == (30, 30), w)


@pruef("2019-be-gk-B3.2f")
def _():
    u, w_, r = symbols('u w_ r', real=True)
    g = vec(4 - r, 0, r**2 + 1) + u * vec(4, -5, 0)
    gh = vec(5, 5, 5) + w_ * vec(-5, 0, 0)
    loes = solve(list(g - gh), [u, w_, r], dict=True)
    ws = sorted((d[r], d[w_]) for d in loes)
    S = gh.subs(w_, R(3, 5))
    w = (ws, list(S), (vec(5, 5, 5) - S).norm(), (S - vec(0, 5, 5)).norm())
    return ok(ws == [(-2, R(3, 5)), (2, R(7, 5))] and list(S) == [2, 5, 5] and w[2] == 3 and w[3] == 2, w)


@pruef("2019-be-gk-B4.1a")
def _():
    p80 = float(binom_p(100, R(4, 5), 80, 80))
    k75 = float(binom_p(100, R(4, 5), 0, 75))
    y24 = float(binom_p(100, R(1, 5), 0, 24))
    w = (p80, k75, y24, 1 - y24)
    return ok(near(p80, 0.099, 5e-4) and near(k75, 0.131, 5e-4) and near(y24, 0.8686, 5e-5), w)


@pruef("2019-be-gk-B4.1b")
def _():
    g_ = math.log(0.01) / math.log(0.8)
    w = (g_, 0.8**20, 0.8**21)
    return ok(near(g_, 20.6, 0.05) and w[1] > 0.01 >= w[2], w)


@pruef("2019-be-gk-B4.1c")
def _():
    w = (13879 - 2482, 13879 - 2482 - 8870)
    return ok(w == (11397, 2527), w)


@pruef("2019-be-gk-B4.1d")
def _():
    w = (11104 - 8870, float(R(11104 - 8870, 2482)), float(R(11104, 13879)))
    return ok(w[0] == 2234 and near(w[1], 0.900, 5e-4) and near(w[2], 0.800, 5e-4), w)


@pruef("2019-be-gk-B4.1e")
def _():
    q = symbols('q')
    gl = q + (1 - q) * q / 2 - R(9, 10)
    st = sorted(solve(gl, q))
    w = (expand(-2 * gl), [float(v) for v in st])
    return ok(w[0] == q**2 - 3 * q + R(9, 5) and near(w[1][0], 0.829, 5e-4) and near(w[1][1], 2.17, 5e-3)
              and simplify(st[0] - (3 - sqrt(R(18, 10))) / 2) == 0, w)


@pruef("2019-be-gk-B4.2a")
def _():
    return ok(R(1, 6) * R(2, 6) == R(1, 18), R(1, 6) * R(2, 6))


@pruef("2019-be-gk-B4.2b")
def _():
    n_ = sum(1 for i in range(1, 7) for j in range(1, 7) if i < j)
    return ok(n_ == 15 and R(n_, 36) == R(5, 12), n_)


@pruef("2019-be-gk-B4.2c")
def _():
    return ok(30 * R(5, 12) == R(25, 2), 30 * R(5, 12))


@pruef("2019-be-gk-B4.2d")
def _():
    p12 = float(binom_p(30, R(5, 12), 12, 12))
    w = (p12, float(1 - R(5, 12)**30))
    return ok(near(p12, 0.145, 5e-4) and near(w[1], 1, 1e-9), w)


@pruef("2019-be-gk-B4.2e")
def _():
    w = float(binom_p(30, R(5, 12), 10, 12))
    return ok(near(w, 0.372, 5e-4), w)


@pruef("2019-be-gk-B4.2f")
def _():
    w = (binomial(10, 7), binomial(5, 2) * binomial(5, 5), binomial(5, 3) * binomial(5, 4))
    p = (w[1] + w[2]) / w[0]
    return ok(w == (120, 10, 50) and p == R(1, 2), (w, p))


# ================================ 2020-be-gk =================================
@pruef("2020-be-gk-A1.1a")
def _():
    return ok(diff(2 * x**4 - x + 1, x) == 8 * x**3 - 1, diff(2 * x**4 - x + 1, x))


nr("2020-be-gk-A1.1b", "Konstante aus der Verschiebung abgelesen (C = 4, −2)")


@pruef("2020-be-gk-A1.2a")
def _():
    f = a * x**2 + b * x + c
    loes = solve([f.subs(x, 0), f.subs(x, 2) - 6, diff(f, x).subs(x, 2) - 4], [a, b, c])
    return ok(loes == {a: R(1, 2), b: 2, c: 0}, loes)


@pruef("2020-be-gk-A1.3a")
def _():
    A, B, C = vec(3, 4, -1), vec(4, 6, 0), vec(1, 0, -3)
    w = (list(B - A), list(C - A))
    return ok(C - A == -2 * (B - A) and w[0] == [1, 2, 1], w)


@pruef("2020-be-gk-A1.3b")
def _():
    A, B = vec(3, 4, -1), vec(4, 6, 0)
    D = A - (B - A)
    return ok(list(D) == [2, 2, -2] and (D - A).norm() == (B - A).norm(), list(D))


@pruef("2020-be-gk-A1.4a")
def _():
    d = vec(4, 1, 5) - vec(7, -3, 5)
    return ok(list(d) == [-3, 4, 0] and d.norm() == 5, list(d))


@pruef("2020-be-gk-A1.4b")
def _():
    A, B = vec(7, -3, 5), vec(4, 1, 5)
    h = 2 * 10 / (B - A).norm()
    M = (A + B) / 2
    C = M + vec(0, 0, h)
    w = (h, list(M), list(C), (C - A).norm() == (C - B).norm(), R(1, 2) * 5 * h)
    return ok(h == 4 and list(M) == [R(11, 2), -1, 5] and list(C) == [R(11, 2), -1, 9] and w[3] and w[4] == 10, w)


@pruef("2020-be-gk-A1.5a")
def _():
    w = R(3, 5) * R(2, 4) + R(2, 5) * R(3, 4)
    return ok(w == R(3, 5), w)


@pruef("2020-be-gk-A1.5b")
def _():
    w = R(2, 5) + R(3, 5) * R(2, 4) * R(2, 3)
    return ok(w == R(3, 5) and w > R(1, 2), w)


f20 = (6 * x - 3) * exp(-x)


@pruef("2020-be-gk-B2.1a")
def _():
    w = (solve(f20, x), f20.subs(x, 0))
    return ok(w == ([R(1, 2)], -3), w)


@pruef("2020-be-gk-B2.1b")
def _():
    from sympy import limit, oo
    w = (limit(f20, x, oo), limit(f20, x, -oo))
    return ok(w == (0, -oo), w)


@pruef("2020-be-gk-B2.1c")
def _():
    f1 = diff(f20, x)
    st = solve(f1, x)
    w = (simplify(f1 - (-6 * x + 9) * exp(-x)), st, f20.subs(x, R(3, 2)), float(f20.subs(x, R(3, 2))))
    return ok(w[0] == 0 and st == [R(3, 2)] and w[2] == 6 * exp(-R(3, 2)) and near(w[3], 1.34, 0.005), w)


nr("2020-be-gk-B2.1d", "Begründung aus der Skizze")
nr("2020-be-gk-B2.1e", "Skizze")


@pruef("2020-be-gk-B2.1f")
def _():
    m = diff(f20, x).subs(x, 1)
    f1v = f20.subs(x, 1)
    n0 = f1v - m * 1
    w = (m, f1v, n0, float(m), grad(atan(m)))
    return ok(m == 3 / E and f1v == 3 / E and n0 == 0 and near(w[3], 1.104, 5e-4) and near(w[4], 47.8, 0.05), w)


@pruef("2020-be-gk-B2.1g")
def _():
    d = f20 - diff(f20, x)
    st = solve(diff(d, x), x)
    w = (simplify(d - (12 * x - 12) * exp(-x)), simplify(diff(d, x) - (24 - 12 * x) * exp(-x)), st, d.subs(x, 2), float(d.subs(x, 2)))
    return ok(w[0] == 0 and w[1] == 0 and st == [2] and w[3] == 12 * exp(-2) and near(w[4], 1.62, 0.005), w)


@pruef("2020-be-gk-B2.1h")
def _():
    F = (-6 * x - 3) * exp(-x)
    w = (simplify(diff(F, x) - f20), F.subs(x, 0), 17 - F.subs(x, 0))
    return ok(w == (0, -3, 20), w)


@pruef("2020-be-gk-B2.1i")
def _():
    F = (-6 * x - 3) * exp(-x)
    A = F.subs(x, 5) - F.subs(x, 1)
    w = (simplify(A - (-33 * exp(-5) + 9 * exp(-1))), float(A), float(F.subs(x, 5)), float(F.subs(x, 1)))
    return ok(w[0] == 0 and near(w[1], 3.09, 0.005) and near(w[2], -0.222, 5e-4) and near(w[3], -3.311, 5e-4), w)


@pruef("2020-be-gk-B2.1j")
def _():
    f1, f2 = diff(f20, x), diff(f20, x, 2)
    st = solve(f1 - f2, x)
    return ok(simplify(f2 - (6 * x - 15) * exp(-x)) == 0 and st == [2], st)


f20b = -R(1, 100) * (x - 8) * (x + 1)**2


@pruef("2020-be-gk-B2.2a")
def _():
    from sympy import roots
    return ok(roots(f20b, x) == {8: 1, -1: 2}, roots(f20b, x))


@pruef("2020-be-gk-B2.2b")
def _():
    from sympy import limit, oo
    w = (expand(f20b), limit(f20b, x, oo), limit(f20b, x, -oo))
    return ok(w[0] == -R(1, 100) * x**3 + R(3, 50) * x**2 + R(3, 20) * x + R(2, 25) and w[1] == -oo and w[2] == oo, w)


@pruef("2020-be-gk-B2.2c")
def _():
    f1, f2 = diff(f20b, x), diff(f20b, x, 2)
    st = sorted(solve(f1, x))
    w = (expand(f1), st, f2.subs(x, -1), f2.subs(x, 5), f20b.subs(x, -1), f20b.subs(x, 5))
    return ok(w[0] == -R(3, 100) * x**2 + R(3, 25) * x + R(3, 20) and st == [-1, 5] and w[2] == R(9, 50) and w[3] == -R(9, 50)
              and w[4] == 0 and w[5] == R(27, 25), w)


@pruef("2020-be-gk-B2.2d")
def _():
    w = (f20b.subs(x, -2), diff(f20b, x).subs(x, 2), solve(diff(f20b, x, 2), x))
    return ok(w == (R(1, 10), R(27, 100), [2]), w)


nr("2020-be-gk-B2.2e", "Begründung über f″, keine Zahl")


@pruef("2020-be-gk-B2.2f")
def _():
    m = diff(f20b, x).subs(x, 6)
    y6 = f20b.subs(x, 6)
    n0 = y6 - 6 * m
    x0 = solve(m * x + n0, x)[0]
    w = (m, y6, n0, x0, float(x0))
    return ok(m == -R(21, 100) and y6 == R(49, 50) and n0 == R(224, 100) and x0 == R(32, 3) and near(w[4], 10.67, 0.005), w)


@pruef("2020-be-gk-B2.2g")
def _():
    tri = R(1, 2) * (R(32, 3) - 6) * R(49, 50)
    integ = integrate(f20b, (x, 6, 8))
    q = tri - integ
    w = (float(tri), float(integ), float(q), float(5 * q))
    return ok(near(w[0], 2.29, 0.005) and near(w[1], 1.18, 0.005) and near(w[2], 1.107, 0.001) and near(w[3], 5.53, 0.005), w)


@pruef("2020-be-gk-B2.2h")
def _():
    st = sorted(solve(diff(f20b, x) + R(27, 100), x))
    w = (st, [float(v) for v in st], diff(f20b, x).subs(x, 2))
    return ok(simplify(st[1] - (2 + sqrt(18))) == 0 and near(w[1][1], 6.24, 0.005) and near(w[1][0], -2.24, 0.005) and w[2] == R(27, 100), w)


@pruef("2020-be-gk-B3.1a")
def _():
    nv = vec(-3, 9, 0).cross(vec(-3, 0, 4))
    w = (list(nv), vec(12, 4, 9).dot(vec(3, 0, 0)))
    return ok(list(nv) == [36, 12, 27] and w[1] == 36, w)


@pruef("2020-be-gk-B3.1b")
def _():
    w = (R(36, 12), R(36, 4), R(36, 9))
    return ok(w == (3, 9, 4), w)


@pruef("2020-be-gk-B3.1c")
def _():
    d = 36 / sqrt(144 + 16 + 81)
    return ok(d == 36 / sqrt(241) and near(d, 2.32, 0.005), float(d))


@pruef("2020-be-gk-B3.1d")
def _():
    r_, s_ = symbols('r_ s_')
    P = vec(3, 0, 0) + r_ * vec(-3, 9, 0) + s_ * vec(-3, 0, 4)
    gl = 6 * P[0] + 2 * P[1] + 9 * P[2] - 18
    kol = solve(list(vec(12, 4, 9) - k * vec(6, 2, 9)), k)
    w = (expand(gl), solve(gl, s_), kol)
    return ok(expand(gl) == 18 * s_ and w[1] == [0] and kol == [], w)


@pruef("2020-be-gk-B3.1e")
def _():
    w = (R(1, 2) * 3 * 9, R(1, 3) * R(27, 2) * 4)
    return ok(w == (R(27, 2), 18), w)


@pruef("2020-be-gk-B3.1f")
def _():
    r_ = symbols('r_')
    P = vec(3, 0, 0) + r_ * vec(-3, 9, 0)
    PC = vec(0, 0, 4) - P
    r0 = solve(PC.dot(vec(-3, 9, 0)), r_)[0]
    w = (list(PC), expand(PC.dot(vec(-3, 9, 0))), r0, list(P.subs(r_, r0)))
    return ok(r0 == R(1, 10) and list(P.subs(r_, r0)) == [R(27, 10), R(9, 10), 0], w)


E20, K20, L20 = vec(0, 0, 6), vec(2, 10, 6), vec(10, 0, 4)


@pruef("2020-be-gk-B3.2a")
def _():
    EK, EL, KL = K20 - E20, L20 - E20, L20 - K20
    w = (EK.dot(EK), EL.dot(EL), KL.dot(KL), float(sqrt(104)), float(sqrt(168)))
    return ok(w[0] == w[1] == 104 and w[2] == 168 and near(w[3], 10.2, 0.05) and near(w[4], 13.0, 0.05), w)


@pruef("2020-be-gk-B3.2b")
def _():
    LE, LK = E20 - L20, K20 - L20
    nv = LE.cross(LK)
    w = (list(LE), list(LK), list(nv), [vec(5, -1, 25).dot(P) for P in (E20, K20, L20)])
    return ok(list(LE) == [-10, 0, 2] and list(LK) == [-8, 10, 2] and list(nv) == [-20, 4, -100] and w[3] == [150, 150, 150], w)


@pruef("2020-be-gk-B3.2c")
def _():
    nv = vec(5, -1, 25)
    z0 = solve(nv.dot(vec(0, 10, z)) - 50, z)[0]
    w = (nv.dot(vec(10, 0, 0)), z0)
    return ok(w == (50, R(12, 5)), w)


@pruef("2020-be-gk-B3.2d")
def _():
    nv = vec(5, -1, 25)
    d = Abs(150 - 50) / sqrt(nv.dot(nv))
    w = (nv.dot(nv), float(d), (vec(10, 0, 0) - L20).norm())
    return ok(nv.dot(nv) == 651 and near(w[1], 3.92, 0.005) and w[2] == 4 and w[1] < 4, w)


@pruef("2020-be-gk-B3.2e")
def _():
    x1 = solve(5 * x - 0 + 25 * R(8, 10) - 50, x)[0]
    x2 = solve(5 * x - 10 + 25 * R(8, 10) - 50, x)[0]
    A = (10 - x1 + 10 - x2) / 2 * 10
    return ok(x1 == 6 and x2 == 8 and A == 30, (x1, x2, A))


@pruef("2020-be-gk-B4.1a")
def _():
    w = (float(binom_p(10, R(1, 3), 4, 4)), float(R(2, 3)**10))
    return ok(near(w[0], 0.228, 5e-4) and near(w[1], 0.017, 5e-4), w)


@pruef("2020-be-gk-B4.1b")
def _():
    w = (R(1, 3) + R(2, 3) * R(1, 3) + R(2, 3)**2 * R(1, 3), 1 - R(2, 3)**3)
    return ok(w[0] == w[1] == R(19, 27) and near(w[0], 0.704, 5e-4), w)


@pruef("2020-be-gk-B4.1c")
def _():
    g_ = math.log(0.05) / math.log(2 / 3)
    return ok(near(g_, 7.39, 0.005) and (2 / 3)**7 > 0.05 >= (2 / 3)**8, g_)


@pruef("2020-be-gk-B4.1d")
def _():
    w = R(1, 3) * R(1, 3) + R(1, 6) * R(1, 6)
    return ok(w == R(5, 36) and near(w, 0.139, 5e-4), w)


@pruef("2020-be-gk-B4.1e")
def _():
    w = (6 * R(1, 6) * R(1, 3) * R(1, 6), R(1, 3)**3)
    return ok(w == (R(1, 18), R(1, 27)) and w[0] + w[1] == R(5, 54), w)


@pruef("2020-be-gk-B4.1f")
def _():
    w = (6 * R(1, 6) * R(1, 6) * R(1, 3), R(1, 6)**3)
    return ok(w == (R(1, 18), R(1, 216)) and w[0] + w[1] == R(13, 216) and R(5, 54) == R(20, 216), w)


@pruef("2020-be-gk-B4.2a")
def _():
    k16 = float(binom_p(50, R(1, 3), 0, 16))
    return ok(near(k16, 0.4868, 5e-5) and near(1 - k16, 0.513, 5e-4), (k16, 1 - k16))


@pruef("2020-be-gk-B4.2b")
def _():
    w = float(binom_p(50, R(1, 3), 13, 14))
    return ok(near(w, 0.158, 5e-4), w)


@pruef("2020-be-gk-B4.2c")
def _():
    w = (solve(a + 4 * a - 50, a), float(binom_p(50, R(1, 3), 10, 10)))
    return ok(w[0] == [10] and near(w[1], 0.016, 5e-4), w)


@pruef("2020-be-gk-B4.2d")
def _():
    w = (50 * R(1, 3), float(binom_p(50, R(1, 3), 16, 16)), float(binom_p(50, R(1, 3), 17, 17)), float(binom_p(50, R(1, 3), 15, 15)))
    return ok(w[0] == R(50, 3) and max(w[1], w[2]) > w[3], w)


@pruef("2020-be-gk-B4.2e")
def _():
    w = (1 - R(105, 1000), float(R(1, 3) * R(35, 1000)))
    return ok(w[0] == R(895, 1000) and near(w[1], 0.0117, 5e-5), w)


@pruef("2020-be-gk-B4.2f")
def _():
    pu = R(1, 3) * R(35, 1000) + R(2, 3) * R(105, 1000)
    pnu = R(2, 3) * R(105, 1000)
    w = (float(pu), pnu, float(pnu / pu))
    return ok(near(w[0], 0.0817, 5e-5) and pnu == R(7, 100) and near(w[2], 0.857, 5e-4), w)


@pruef("2020-be-gk-B4.2g")
def _():
    w = solve(5 * a * R(4, 100) - (1 - a) * R(1, 10), a)
    return ok(w == [R(1, 3)], w)


# ================================ 2021-be-gk =================================
f21a = x**3 - x


@pruef("2021-be-gk-A1.1a")
def _():
    w = (f21a.subs(x, R(1, 2)), sorted(solve(f21a, x)))
    return ok(w == (-R(3, 8), [-1, 0, 1]), w)


@pruef("2021-be-gk-A1.1b")
def _():
    A = 2 * integrate(f21a, (x, -1, 0))
    return ok(A == R(1, 2), A)


nr("2021-be-gk-A1.2a", "Ablesen aus dem Graphen")
nr("2021-be-gk-A1.2b", "Vorzeichen aus dem Graphen")
f21b = x**3 - 3 * x**2 + 4


@pruef("2021-be-gk-A1.3a")
def _():
    w = (diff(f21b, x).subs(x, 2), diff(f21b, x, 2).subs(x, 2))
    return ok(w == (0, 6), w)


@pruef("2021-be-gk-A1.3b")
def _():
    from sympy import nsolve
    A = x * f21b
    A1 = diff(A, x)
    xm = nsolve(A1, x, 0.8)
    w = (expand(A), expand(A1), A1.subs(x, 1), float(xm))
    return ok(w[0] == x**4 - 3 * x**3 + 4 * x and w[1] == 4 * x**3 - 9 * x**2 + 4 and w[2] == -1 and near(w[3], 0.84, 0.005), w)


@pruef("2021-be-gk-A1.4a")
def _():
    return ok(vec(-5, 2, 8).dot(vec(1, 8, 3)) == 35, vec(-5, 2, 8).dot(vec(1, 8, 3)))


@pruef("2021-be-gk-A1.4b")
def _():
    r_ = symbols('r_')
    P = vec(1, -4, 2) + r_ * vec(0, 8, -2)
    w = simplify(2 * P[0] + P[1] + 4 * P[2] - 6)
    return ok(w == 0, w)


@pruef("2021-be-gk-A1.4c")
def _():
    nH = vec(0, 4, -1)
    w = (nH.dot(vec(2, 1, 4)), nH.dot(vec(-5, 2, 8)), vec(2, 1, 4).cross(vec(-5, 2, 8)))
    return ok(w[0] == 0 and w[1] == 0 and list(w[2]) == [0, -36, 9], w)


@pruef("2021-be-gk-A1.5a")
def _():
    loes = solve(list(vec(1, 2, 3) + t * vec(0, 2, 1) + s * vec(3, 0, -1) - vec(4, 6, 4)), [t, s])
    return ok(loes == {t: 2, s: 1}, loes)


@pruef("2021-be-gk-A1.5b")
def _():
    rv = 1 * vec(0, 2, 1) + 1 * vec(3, 0, -1)
    return ok(list(rv) == [3, 2, 0], list(rv))


@pruef("2021-be-gk-A1.6a")
def _():
    n_ = sum(1 for r_ in range(1, 7) for b_ in range(1, 7) if b_ > r_)
    return ok(n_ == 15, n_)


@pruef("2021-be-gk-A1.6b")
def _():
    w = 0 * R(15, 36) + 1 * R(6, 36) + 2 * R(15, 36)
    return ok(w == 1, w)


@pruef("2021-be-gk-A1.7a")
def _():
    w = R(6, 10) * R(5, 9) + R(4, 10) * R(6, 9)
    return ok(w == R(3, 5), w)


@pruef("2021-be-gk-A1.7b")
def _():
    w = R(6, 10) * R(5, 9) * R(4, 8) + 2 * R(6, 10) * R(4, 9) * R(5, 8) + R(4, 10) * R(3, 9) * R(6, 8)
    return ok(w == R(3, 5), w)


f21 = R(1, 12) * x**3 - x**2 + 3 * x
p21 = -x**2 + R(38, 10) * x - R(136, 100)


@pruef("2021-be-gk-B2.1a")
def _():
    w = (p21.subs(x, R(4, 10)), p21.subs(x, R(34, 10)))
    return ok(w == (0, 0), w)


@pruef("2021-be-gk-B2.1b")
def _():
    from sympy import roots
    return ok(roots(f21, x) == {0: 1, 6: 2} and factor(f21) == x * (x - 6)**2 / 12, roots(f21, x))


@pruef("2021-be-gk-B2.1c")
def _():
    w = (diff(f21, x).subs(x, 2), diff(f21, x, 2).subs(x, 2), f21.subs(x, 2))
    return ok(w == (0, -1, R(8, 3)), w)


@pruef("2021-be-gk-B2.1d")
def _():
    w = (solve(diff(f21, x, 2), x), diff(f21, x, 3), f21.subs(x, 4))
    return ok(w == ([4], R(1, 2), R(4, 3)), w)


@pruef("2021-be-gk-B2.1e")
def _():
    w = (f21.subs(x, 2), f21.subs(x, 8), integrate(R(8, 3) - f21, (x, 2, 8)))
    return ok(w == (R(8, 3), R(8, 3), 9), w)


@pruef("2021-be-gk-B2.1f")
def _():
    xs = solve(diff(p21, x), x)[0]
    S = (xs, p21.subs(x, xs))
    d = sqrt((2 - xs)**2 + (R(8, 3) - S[1])**2)
    w = (S, d, float(d), float(R(5, 12)))
    return ok(S == (R(19, 10), R(9, 4)) and simplify(d - sqrt(661) / 60) == 0 and near(w[2], 0.4285, 5e-5) and w[2] > w[3], w)


@pruef("2021-be-gk-B2.1g")
def _():
    d = f21 - p21
    xs = [v for v in solve(diff(d, x), x) if v > 0][0]
    w = (expand(d), xs, float(xs), float(d.subs(x, xs)), float(d.subs(x, R(4, 10))), float(d.subs(x, R(34, 10))))
    return ok(w[0] == R(1, 12) * x**3 - R(4, 5) * x + R(34, 25) and simplify(xs - sqrt(R(32, 10))) == 0 and near(w[2], 1.79, 0.005)
              and near(w[3], 0.406, 5e-4) and near(w[4], 1.045, 5e-4) and near(w[5], 1.915, 5e-4), w)


@pruef("2021-be-gk-B2.1h")
def _():
    i1 = integrate(f21, (x, 0, R(9, 2)))
    i2 = integrate(p21, (x, R(4, 10), R(34, 10)))
    w = (float(i1), i2, float(i1 - i2), float(100 * (i1 - i2)))
    return ok(near(w[0], 8.54, 0.005) and i2 == R(9, 2) and near(w[2], 4.04, 0.005) and near(w[3], 404, 0.5), w)


@pruef("2021-be-gk-B2.1i")
def _():
    w = (diff(p21, x).subs(x, R(4, 10)), diff(f21, x).subs(x, 0))
    return ok(w == (3, 3), w)


@pruef("2021-be-gk-B2.1j")
def _():
    h = R(4, 3) * x - R(7, 4)
    w = (f21.subs(x, 3), h.subs(x, 3), diff(f21, x).subs(x, 3), diff(f21, x).subs(x, 3) * R(4, 3))
    return ok(w == (R(9, 4), R(9, 4), -R(3, 4), -1), w)


@pruef("2021-be-gk-B2.1k")
def _():
    q = a * x**2 + b * x
    loes = solve([q.subs(x, 2) - R(22, 10), diff(q, x).subs(x, 2)], [a, b])
    return ok(loes == {a: -R(11, 20), b: R(11, 5)}, loes)


f21c = (-R(1, 10) * x**2 + 2 * x) * exp(-R(1, 10) * x)
h21 = -R(3, 4) * x * exp(-R(1, 10) * x)


@pruef("2021-be-gk-B2.2a")
def _():
    w = (sorted(solve(f21c, x)), f21c.subs(x, 0))
    return ok(w == ([0, 20], 0), w)


@pruef("2021-be-gk-B2.2b")
def _():
    from sympy import limit, oo
    w = (limit(f21c, x, oo), limit(f21c, x, -oo))
    return ok(w == (0, -oo), w)


@pruef("2021-be-gk-B2.2c")
def _():
    w = (f21c.subs(x, 0), h21.subs(x, 0))
    return ok(w == (0, 0), w)


@pruef("2021-be-gk-B2.2d")
def _():
    f1, f2 = diff(f21c, x), diff(f21c, x, 2)
    st = sorted(solve(f1, x))
    w = (simplify(f1 / exp(-R(1, 10) * x)), st, [float(v) for v in st], [float(f21c.subs(x, v)) for v in st],
         [float(f2.subs(x, v)) for v in st], simplify(f2 / exp(-R(1, 10) * x)))
    return ok(expand(w[0]) == R(1, 100) * x**2 - R(2, 5) * x + 2 and simplify(st[0] - (20 - 10 * sqrt(2))) == 0
              and near(w[2][0], 5.86, 0.005) and near(w[2][1], 34.14, 0.005) and near(w[3][0], 4.61, 0.005) and near(w[3][1], -1.59, 0.005)
              and w[4][0] < 0 < w[4][1] and expand(w[5]) == -R(1, 1000) * x**2 + R(3, 50) * x - R(3, 5), w)


@pruef("2021-be-gk-B2.2e")
def _():
    h1 = diff(h21, x)
    w = (solve(h1, x), float(h21.subs(x, 10)), solve(diff(h21, x, 2), x))
    return ok(w[0] == [10] and near(w[1], -2.76, 0.005) and w[2] == [20], w)


@pruef("2021-be-gk-B2.2f")
def _():
    m = diff(h21, x).subs(x, 0)
    bb = [v for v in solve(R(1, 2) * b * Abs(m * b) - R(75, 2), b) if v > 0]
    return ok(m == -R(3, 4) and bb == [10], (m, bb))


@pruef("2021-be-gk-B2.2g")
def _():
    st = sorted(solve(f21c - h21, x))
    w = (st, float(f21c.subs(x, R(55, 2))))
    return ok(st == [0, R(55, 2)] and near(w[1], -1.32, 0.005), w)


nr("2021-be-gk-B2.2h", "Begründung über Pythagoras, keine Zahl")


@pruef("2021-be-gk-B2.2i")
def _():
    d = f21c - h21
    d1 = diff(d, x)
    st = sorted(solve(d1, x))
    w = (simplify(d / exp(-R(1, 10) * x)), expand(simplify(d1 / exp(-R(1, 10) * x))), [float(v) for v in st], float(d.subs(x, st[0])))
    return ok(expand(w[0]) == -R(1, 10) * x**2 + R(11, 4) * x and w[1] == R(1, 100) * x**2 - R(19, 40) * x + R(11, 4)
              and near(w[2][0], 6.75, 0.005) and near(w[2][1], 40.75, 0.005) and near(w[3], 7.13, 0.005) and w[3] < 7.15, w)


@pruef("2021-be-gk-B2.2j")
def _():
    D = (x**2 - R(15, 2) * x - 75) * exp(-R(1, 10) * x)
    d = f21c - h21
    A = D.subs(x, R(55, 2)) - D.subs(x, 0)
    w = (simplify(diff(D, x) - d), float(D.subs(x, R(55, 2))), D.subs(x, 0), float(A))
    return ok(w[0] == 0 and near(w[1], 30.4, 0.05) and w[2] == -75 and near(w[3], 105.4, 0.05), w)


@pruef("2021-be-gk-B2.2k")
def _():
    y_ = 1.32
    w = (grad(asin(y_ / math.sqrt(27.5**2 + y_**2))), grad(atan(y_ / 27.5)))
    return ok(near(w[0], 2.75, 0.005) and near(w[1], 2.75, 0.005), w)


@pruef("2021-be-gk-B2.2l")
def _():
    f2 = diff(f21c, x, 2)
    st = sorted(solve(f2, x))
    xr = st[0]
    yr = f21c.subs(x, xr)
    beta = grad(atan(yr / xr))
    w = (st, float(xr), float(yr), beta, 2.75 + beta)
    return ok(simplify(xr - (30 - 10 * sqrt(3))) == 0 and near(w[1], 12.68, 0.005) and near(w[2], 2.61, 0.005)
              and near(beta, 11.6, 0.05) and near(w[4], 14.4, 0.05) and w[4] < 18, w)


A21, B21, C21, D21, E21 = vec(0, 0, 0), vec(10, 0, 0), vec(10, 10, 0), vec(0, 10, 0), vec(0, 10, 6)


@pruef("2021-be-gk-B3a")
def _():
    BC, CE = C21 - B21, E21 - C21
    O = 100 + 2 * R(1, 2) * 10 * sqrt(CE.dot(CE)) + 2 * R(1, 2) * 10 * 6
    w = (BC.dot(CE), CE.dot(CE), simplify(O), float(O))
    return ok(w[0] == 0 and w[1] == 136 and simplify(O - (160 + 20 * sqrt(34))) == 0 and near(w[3], 276.6, 0.05), w)


nr("2021-be-gk-B3b", "Lagebegründung, Geradengleichung abgelesen")


@pruef("2021-be-gk-B3c")
def _():
    nv = (C21 - B21).cross(E21 - C21)
    w = (list(nv), [3 * P[0] + 5 * P[2] for P in (B21, C21, E21)])
    return ok(list(nv) == [60, 0, 100] and w[1] == [30, 30, 30], w)


@pruef("2021-be-gk-B3d")
def _():
    c_ = 5 / sqrt(34)
    return ok(near(grad(acos(c_)), 31.0, 0.05), grad(acos(c_)))


nr("2021-be-gk-B3e", "Lagebegründung")


@pruef("2021-be-gk-B3f")
def _():
    lam = symbols('lam')
    w = solve(R(1, 2) * (10 + 10 - 2 * lam) * 10 - 80, lam)
    return ok(w == [2], w)


@pruef("2021-be-gk-B3g")
def _():
    P = vec(10 - 10 * t, 10 * t, 6 * t)
    PC, PB = C21 - P, B21 - P
    t0 = solve(PC.dot(PB), t)
    t0 = [v for v in t0 if v != 0][0]
    l_ = float(2 * (C21 - P.subs(t, t0)).norm())
    return ok(t0 == R(25, 59) and near(l_, 15.2, 0.05), (t0, l_))


@pruef("2021-be-gk-B3h")
def _():
    return ok(solve(5 * z - 30, z) == [6], solve(5 * z - 30, z))


@pruef("2021-be-gk-B3i")
def _():
    return ok(R(1, 2) / R(1, 3) == R(3, 2), R(1, 2) / R(1, 3))


@pruef("2021-be-gk-B4a")
def _():
    k6 = float(binom_p(10, R(2, 5), 0, 6))
    k8 = float(binom_p(10, R(2, 5), 0, 8))
    k4 = float(binom_p(10, R(2, 5), 0, 4))
    w = (k6, k8, k4, 1 - k6, k8 - k4)
    return ok(near(k6, 0.9452, 5e-5) and near(k8, 0.9983, 5e-5) and near(k4, 0.6331, 5e-5) and near(1 - k6, 0.055, 5e-4) and near(k8 - k4, 0.365, 5e-4), w)


@pruef("2021-be-gk-B4b")
def _():
    p = 1 - float(binom_p(10, R(2, 5), 0, 4))
    return ok(near(p, 0.3669, 5e-5) and near(p**2, 0.135, 5e-4), (p, p**2))


nr("2021-be-gk-B4c", "Beurteilung der Unabhängigkeit")


@pruef("2021-be-gk-B4d")
def _():
    p5 = float(binom_p(10, R(2, 5), 5, 5))
    w = (p5, 6 * p5**2 * (1 - p5)**2)
    return ok(near(p5, 0.2007, 5e-5) and near(w[1], 0.154, 5e-4), w)


@pruef("2021-be-gk-B4e")
def _():
    g_ = math.log(0.05) / math.log(0.6)
    return ok(near(g_, 5.86, 0.005) and 0.6**5 > 0.05 >= 0.6**6, g_)


@pruef("2021-be-gk-B4f")
def _():
    w = (1 - (0.6**10 + 10 * 0.4 * 0.6**9), float(binom_p(10, R(2, 5), 2, 10)))
    return ok(near(w[0], 0.954, 5e-4) and near(w[0], w[1], 1e-9), w)


@pruef("2021-be-gk-B4g")
def _():
    w = R(1, 10) * R(4, 10) * R(5, 10)
    return ok(w == R(2, 100), w)


@pruef("2021-be-gk-B4h")
def _():
    w = 4 * R(1, 10) * R(5, 10)**3 + R(4, 10)**4
    return ok(w == R(756, 10000), w)


@pruef("2021-be-gk-B4i")
def _():
    w = solve(10 * x + 20 * (R(9, 10) - x) + 5 - 15, x)
    return ok(w == [R(4, 5)] and R(9, 10) - w[0] == R(1, 10), w)


# ============================ 2017-be-gk-cas =================================
@pruef("2017-be-gk-cas-B1.1a")
def _():
    return PRUEF["2017-be-gk-B1.1a"]()


@pruef("2017-be-gk-cas-B1.1b")
def _():
    return PRUEF["2017-be-gk-B1.1b"]()


@pruef("2017-be-gk-cas-B1.1c")
def _():
    return PRUEF["2017-be-gk-B1.1c"]()


@pruef("2017-be-gk-cas-B1.1e")
def _():
    gu, go = R(45, 100) * x - 2, R(45, 100) * x + 1
    d = f17 - gu
    d1 = diff(d, x)
    w = (factor(go - f17), expand(d), factor(d1), sorted(solve(d1, x)), d.subs(x, 5), d.subs(x, 15), d.subs(x, 0), d.subs(x, 20))
    return ok(w[0] == x * (x - 15)**2 / 500 and w[1] == -x**3 / 500 + R(3, 50) * x**2 - R(9, 20) * x + 3
              and w[3] == [5, 15] and w[4:] == (2, 3, 3, 2), w)


@pruef("2017-be-gk-cas-B1.1f")
def _():
    gu = R(45, 100) * x - 2
    n0 = solve(gu, x)[0]
    i2 = integrate(gu, (x, n0, 17))
    A = integrate(f17, (x, 0, 20)) - i2
    w = (n0, i2, float(i2), A, float(A), 4 * A, float(4 * A), gu.subs(x, 17))
    return ok(n0 == R(40, 9) and i2 == R(12769, 360) and near(w[2], 35.47, 0.005) and A == R(23231, 360) and near(w[4], 64.53, 0.005)
              and 4 * A == R(23231, 90) and near(w[6], 258.1, 0.05) and w[7] == R(565, 100), w)


@pruef("2017-be-gk-cas-B1.2a")
def _():
    w = (f17b.subs(x, 0), solve(f17b, x), float(f17b.subs(x, R(1, 2))), float(f17b.subs(x, R(3, 2))), float(f17b.subs(x, 2)))
    return ok(w[0] == 1 and w[1] == [1] and near(w[2], 0.152, 5e-4) and near(w[3], 0.056, 5e-4) and near(w[4], 0.135, 5e-4), w)


@pruef("2017-be-gk-cas-B1.2b")
def _():
    f1, f2, f3 = diff(f17b, x), diff(f17b, x, 2), diff(f17b, x, 3)
    ws = sorted(solve(f2, x))
    w = (simplify(f1 - (-x**2 + 4 * x - 3) * exp(-x)), sorted(solve(f1, x)), ws, [float(f17b.subs(x, v)) for v in ws],
         simplify(f3 + (x**2 - 8 * x + 13) * exp(-x)), [f3.subs(x, v) != 0 for v in ws])
    return ok(w[0] == 0 and w[1] == [1, 3] and simplify(ws[0] - (3 - sqrt(2))) == 0 and near(w[3][0], 0.070, 5e-4)
              and near(w[3][1], 0.141, 5e-4) and w[4] == 0 and all(w[5]), w)


@pruef("2017-be-gk-cas-B1.2d")
def _():
    A = integrate(f17b, (x, 0, 1))
    return ok(simplify(A - (1 - 2 / E)) == 0 and near(A, 0.2642, 1e-3), float(A))


@pruef("2017-be-gk-cas-B1.2e")
def _():
    return PRUEF["2017-be-gk-B1.2e"]()


@pruef("2017-be-gk-cas-B1.2f")
def _():
    from sympy import nsolve
    xq = nsolve(diff(f17b, x) + 1, x, 0.4)
    w = (float(xq), float(f17b.subs(x, xq)))
    return ok(near(w[0], 0.4145, 5e-5) and near(w[1], 0.2264, 5e-5), w)


@pruef("2017-be-gk-cas-B2.2c")
def _():
    E_, F_, S = vec(9, 1, 6), vec(9, 9, 6), vec(5, 5, 9)
    nv = (F_ - E_).cross(S - E_)
    n1 = vec(3, 0, 4)
    cphi = Abs(n1.dot(vec(6, 0, 1))) / (sqrt(n1.dot(n1)) * sqrt(37))
    phi = grad(acos(cphi))
    w = (list(nv), n1.dot(E_), cphi, float(cphi), phi, 180 - phi)
    return ok(list(nv) == [24, 0, 32] and w[1] == 51 and cphi == 22 / (5 * sqrt(37)) and near(w[3], 0.7234, 5e-5)
              and near(phi, 43.67, 0.01) and near(w[5], 136.33, 0.01), w)


@pruef("2017-be-gk-cas-B2.2d")
def _():
    return PRUEF["2017-be-gk-B2.2d"]()


@pruef("2017-be-gk-cas-B3.1e")
def _():
    p12 = float(binom_p(250, R(5, 100), 12, 12))
    p13 = float(binom_p(250, R(5, 100), 13, 13))
    return ok(near(p12, 0.1160, 5e-5) and near(p13, 0.1117, 5e-5) and p12 > p13, (p12, p13))


@pruef("2017-be-gk-cas-B3.1g")
def _():
    w = [float(binom_p(n_, R(96, 100), 500, n_)) for n_ in (525, 526, 527)]
    return ok(near(w[0], 0.842, 5e-4) and near(w[1], 0.885, 5e-4) and near(w[2], 0.919, 5e-4) and w[1] < 0.9 <= w[2], w)


@pruef("2017-be-gk-cas-B3.2c")
def _():
    return PRUEF["2017-be-gk-B3.2c"]()


@pruef("2017-be-gk-cas-B3.2d")
def _():
    p = 0.3669
    pi_ = {i: float(binomial(30, i)) * p**i * (1 - p)**(30 - i) for i in range(31)}
    gross = [i for i in range(31) if pi_[i] > 0.1]
    w = (30 * p, gross, [round(pi_[i], 3) for i in (8, 9, 10, 11, 12, 13, 14)])
    return ok(gross == [9, 10, 11, 12, 13] and near(pi_[8], 0.0824, 5e-4) and near(pi_[14], 0.0776, 5e-4)
              and near(pi_[11], 0.150, 5e-4), w)


# ============================ 2018-be-gk-cas =================================
@pruef("2018-be-gk-cas-B1.1b")
def _():
    return PRUEF["2018-be-gk-B1.1b"]()


@pruef("2018-be-gk-cas-B1.1c")
def _():
    base = PRUEF["2018-be-gk-B1.1c"]()
    m = (g18.subs(x, 100) - g18.subs(x, 0)) / 100
    return ok(base == "ok" and m == -R(1, 2), (base, m))


@pruef("2018-be-gk-cas-B1.1d")
def _():
    return PRUEF["2018-be-gk-B1.1d"]()


@pruef("2018-be-gk-cas-B1.1e")
def _():
    y0, m = g18.subs(x, 110), diff(g18, x).subs(x, 110)
    tg = expand(m * (x - 110) + y0)
    return ok(y0 == R(441, 200) and m == R(231, 500) and tg == R(462, 1000) * x - R(48615, 1000), (y0, m, tg))


@pruef("2018-be-gk-cas-B1.1f")
def _():
    base = PRUEF["2018-be-gk-B1.1f"]()
    xl = 20 * sqrt(5 + 5 * sqrt(3))
    mf, mg = diff(f18, x).subs(x, xl), diff(g18, x).subs(x, xl)
    a1, a2 = grad(atan(mf)), grad(atan(mg))
    w = (base, float(xl), float(g18.subs(x, xl)), float(mf), float(mg), a1, a2, a1 - a2)
    return ok(base == "ok" and near(w[1], 73.920, 5e-4) and near(w[2], 10.287, 5e-4) and near(w[3], -1.183, 5e-4)
              and near(w[4], -0.671, 5e-4) and near(a1, -49.79, 0.01) and near(a2, -33.85, 0.01) and near(a2 - a1, 15.9, 0.05), w)


@pruef("2018-be-gk-cas-B1.1g")
def _():
    d = f18 - g18
    st = sorted(v for v in solve(d - 5, x) if v > 0)
    w = (expand(d), [float(v) for v in st], simplify(st[0] - 10 * sqrt(20 - 10 * sqrt(2))), d.subs(x, 20 * sqrt(5)), diff(d, x, 2).subs(x, 20 * sqrt(5)) < 0)
    return ok(w[0] == -x**4 / 2000000 + x**2 / 500 + 4 and near(w[1][0], 24.20, 0.005) and near(w[1][1], 58.43, 0.005)
              and w[2] == 0 and w[3] == 6 and w[4], w)


@pruef("2018-be-gk-cas-B1.2a")
def _():
    from sympy import limit, oo
    w = (limit(f18b, x, oo), limit(f18b, x, -oo))
    return ok(w == (0, -oo), w)


@pruef("2018-be-gk-cas-B1.2b")
def _():
    st = sorted(solve(f18b - (x + 1), x))
    base = PRUEF["2018-be-gk-B1.2b"]()
    return ok(st == [-1, 0] and base == "ok", (st, base))


@pruef("2018-be-gk-cas-B1.2c")
def _():
    i1 = integrate(f18b, (x, -1, 0))
    i2 = integrate(x + 1, (x, -1, 0))
    A = i1 - i2
    w = (simplify(i1 - (4 * sqrt(E) - 6)), float(i1), i2, float(A))
    return ok(w[0] == 0 and near(w[1], 0.5949, 5e-5) and i2 == R(1, 2) and near(w[3], 0.0949, 5e-5) and w[3] < 0.1, w)


@pruef("2018-be-gk-cas-B1.2d")
def _():
    base = PRUEF["2018-be-gk-B1.2d"]()
    f2 = diff(f18b, x, 2).subs(x, 1)
    return ok(base == "ok" and f2 == -R(1, 2) * exp(-R(1, 2)), (base, f2))


@pruef("2018-be-gk-cas-B1.2e")
def _():
    from sympy import nsolve
    f1 = diff(f18b, x)
    x1, x2 = nsolve(f1 + R(2, 10), x, 2.2), nsolve(f1 + R(2, 10), x, 4.1)
    w = (float(f1.subs(x, 3)), float(f1.subs(x, 6)), float(x1), float(x2))
    return ok(near(w[0], -0.2231, 5e-5) and near(w[1], -0.1245, 5e-5) and near(w[2], 2.20418, 5e-6) and near(w[3], 4.08695, 5e-6), w)


@pruef("2018-be-gk-cas-B1.2f")
def _():
    return PRUEF["2018-be-gk-B1.2e"]()


@pruef("2018-be-gk-cas-B1.2g")
def _():
    from sympy import nsolve
    f2v, f6v = f18b.subs(x, 2), f18b.subs(x, 6)
    m = (f6v - f2v) / 4
    sek = m * (x - 2) + f2v
    d = sek - f18b
    xm = nsolve(diff(d, x), x, 4.4)
    sr = -R(19, 100) * x + R(148, 100)
    xr = nsolve(diff(sr - f18b, x), x, 4.4)
    w = (float(xm), float(d.subs(x, xm)), float(xr), float((sr - f18b).subs(x, xr)))
    return ok(near(w[0], 4.389, 5e-4) and near(w[1], 0.0522, 5e-5) and near(w[2], 4.358, 5e-4) and near(w[3], 0.0457, 5e-4), w)


@pruef("2018-be-gk-cas-B1.2h")
def _():
    from sympy import nsolve
    base = PRUEF["2018-be-gk-B1.2g"]()
    bb = -log(24) / 6
    hW = (x + R(6, 5)) * exp(bb * x)
    xs = nsolve(diff(f18b, x) - diff(hW, x), x, 4.7)
    w = (base, float(xs), float(diff(f18b, x).subs(x, xs)))
    return ok(base == "ok" and near(w[1], 4.6833, 5e-5) and near(w[2], -0.1771, 5e-5), w)


@pruef("2018-be-gk-cas-B3.1b")
def _():
    pa = float(binom_p(10, R(2, 5), 4, 4))
    p9 = 1 - float(binom_p(9, R(2, 5), 0, 3))
    w = (pa, p9, 0.4 * p9)
    return ok(near(pa, 0.2508, 5e-5) and near(p9, 0.5174, 5e-5) and near(w[2], 0.2070, 5e-5), w)


@pruef("2018-be-gk-cas-B3.2a")
def _():
    k8 = float(binom_p(50, R(1, 5), 0, 8))
    kb = float(binom_p(200, R(1, 5), 31, 49))
    return ok(near(k8, 0.3073, 5e-5) and near(kb, 0.9076, 5e-5), (k8, kb))


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
