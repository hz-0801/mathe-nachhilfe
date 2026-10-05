#!/usr/bin/env python3
"""Sympy-Kontrolle der P10-Teilaufgaben 2014–2021 (Übernahme Teil 5, 05.10.2026).

Wie werkzeuge/vorrat-sympy-p10.py: je rechnerische Teilaufgabe eine
Funktion, die den Katalogwert (ergebnis, kurzloesung, ggf. Zwischenwerte)
aus den Angaben in gegeben nachrechnet und "ok" oder "abw: <eigener Wert>"
zurückgibt. Teilaufgaben ohne Funktion gelten als "nicht rechenbar"
(Begründen, Zeichnen, Ablesen, Ankreuzen ohne Rechenkern).

Aufruf: python3 werkzeuge/vorrat-sympy-p10-2014-2021.py [id ...]
        python3 werkzeuge/vorrat-sympy-p10-2014-2021.py --spalte TABELLE
Ohne Argument werden alle Funktionen ausgeführt und als "id;wert"
ausgegeben. Mit --spalte wird die Spalte sympy der Korrekturtabelle
(Kopf id;kurz;zwischen;stich;neben;abh;sympy) neu gefüllt und eine
Zählung je Jahrgang ausgegeben.
Die Funktion ist nach der id benannt (Bindestriche als Unterstrich, Präfix p_).
"""
import csv, io, sys
from collections import Counter
from sympy import (Rational as R, sqrt, symbols, solve, Eq, nsimplify, pi, sin,
                   cos, tan, asin, acos, atan, N, Abs, log, floor, ceiling,
                   binomial, factorial, simplify, expand, S, real_roots, Poly)

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


def kette(*erg):
    """Erstes Ergebnis, das nicht ok ist, sonst ok."""
    for e in erg:
        if e != "ok":
            return e
    return "ok"


def wahr(bed, wert=""):
    return "ok" if bed else "abw: " + str(wert)


def gr(w):
    """Grad → Bogenmaß für sin/cos/tan."""
    return w * pi / 180


def grad(w):
    """Bogenmaß → Grad als Zahl."""
    return N(w * 180 / pi, 12)

# ---------- 2014 (OS)

def p_2014_OS_B1a():
    return genau(50 * R(13, 100), R(65, 10), " €")

def p_2014_OS_B1b():
    return genau(R(20, 80 + 20), R(1, 5))

def p_2014_OS_B1c():
    return wahr(R(1, 2) < R(6, 10) < R(4, 5))

def p_2014_OS_B1d():
    return genau(R(4, 6), R(2, 3))

def p_2014_OS_B1e():
    return genau(R(230, 10000) * 100, R(23, 10), " %")

def p_2014_OS_B1f():
    return genau(50 - 30, 20, "°")

def p_2014_OS_B1g():
    return genau(2 * (5 + 3), 16)

def p_2014_OS_B1h():
    w = [-R(1, 2), R(14, 10), -R(512, 1000), sqrt(2)]
    return wahr(sorted(w, key=lambda v: N(v)) == [-R(512, 1000), -R(1, 2), R(14, 10), sqrt(2)], w)

def p_2014_OS_B1i():
    return kette(genau(R(9, 15), R(3, 5)), genau(R(9, 15) * 100, 60, " %"))

def p_2014_OS_K2a():
    return genau(R(2800, 1000) + R(15, 10), R(43, 10), " km")

def p_2014_OS_K2b():
    jr = 2800 * sin(gr(60)) / sin(gr(50))
    return kette(naeh(jr, 3165, " m", tol=1), naeh(jr + 2500, 5665, " m", tol=1))

def p_2014_OS_K2c():
    gehzeit = R(25, 10) / 5 * 60
    ankunft = 11 * 60 + 30 + 45 + gehzeit
    return kette(genau(gehzeit, 30, " min"), genau(ankunft, 12 * 60 + 45, " min"))

def p_2014_OS_K3a():
    return genau(200 * R(2, 100), 4, " €")

def p_2014_OS_K3b():
    g14 = R(61208, 100) + R(1224, 100) + 200
    return kette(genau(g14, R(82432, 100), " €"), naeh(g14 * R(2, 100), R(1649, 100), " €", tol=R(1, 200)),
                 genau(g14 + R(1649, 100) + 200, R(104081, 100), " €"))

def p_2014_OS_K3c():
    return naeh(1000 * R(103, 100)**5, R(115927, 100), " €", tol=R(1, 100))

def p_2014_OS_K4b():
    return genau(R(1540, 10) - R(1396, 10), R(144, 10), " ct")

def p_2014_OS_K4c():
    return genau(R(100000, 100) * 9 * R(1455, 1000), 13095, " €")

def p_2014_OS_K4d():
    return kette(genau(9000 * R(152, 100), 13680, " €"), genau(13680 - 13095, 585, " €"))

def p_2014_OS_K4e():
    return kette(genau(585 * 100, 58500, " ct"), naeh(R(58500, 100000), R(6, 10), " ct", tol=R(2, 100)))

def p_2014_OS_K5a():
    return genau(5225 * 165, 862125, " cm³")

def p_2014_OS_K5c():
    h = solve(Eq((110 + 80) / S(2) * x, 5225), x)[0]
    return kette(genau(h, 55, " cm"), naeh(sqrt(57**2 - 15**2), 55, " cm", tol=R(6, 10)), wahr(h > 50))

def p_2014_OS_K5d():
    return kette(genau(R(18, 10) / R(12, 10), R(15, 10), " m"), wahr(R(15, 10) < R(165, 100)),
                 genau(R(110, 100) * R(165, 100), R(1815, 1000), " m²"))

def p_2014_OS_K6a():
    return kette(genau(R(3, 8), R(3, 8)), genau(R(3, 8) * 100, R(375, 10), " %"))

def p_2014_OS_K6b():
    return genau(R(4, 8) + R(3, 8) + R(1, 8), 1)

def p_2014_OS_K6c():
    return kette(genau(R(1, 2)**2 + R(3, 8)**2 + R(1, 8)**2, R(13, 32)), naeh(R(13, 32), R(41, 100), tol=R(1, 100)))

def p_2014_OS_K7a():
    p, g = -x**2, 2 * x - 3
    return kette(genau(p.subs(x, -3), -9), genau(g.subs(x, -3), -9),
                 wahr(set(solve(Eq(p, g), x)) == {-3, 1}))

def p_2014_OS_K7b():
    return wahr(real_roots(Poly(-x**2 - 1, x)) == [])


# ---------- 2015 (OS)

def p_2015_OS_B1a():
    w = {"links": R(4, 6), "Mitte": R(2, 6), "rechts": R(3, 6)}
    return wahr([k for k in w if w[k] == R(1, 2)] == ["rechts"], w)

def p_2015_OS_B1b():
    return wahr(0 > -150)

def p_2015_OS_B1c():
    return wahr(not (R(15, 10) < R(3, 2)) and R(8, 5) > R(3, 2) and not (sqrt(2) > R(3, 2)))

def p_2015_OS_B1d():
    return genau(180 - 53, 127, "°")

def p_2015_OS_B1e():
    return genau(400 * R(2, 100), 8, " €")

def p_2015_OS_B1f():
    return genau(sorted([5, 7, 3, 8, 1, 8, 5])[3], 5, " °C")

def p_2015_OS_B1g():
    return wahr(3 * (-2) < 0)

def p_2015_OS_B1h():
    return genau(600 - R(2, 3) * 600, 200, " l")

def p_2015_OS_B1i():
    return genau(solve(Eq((x - 2)**2, 0), x)[0], 2)

def p_2015_OS_B1j():
    return genau(sqrt((-4)**2), 4)

def p_2015_OS_K2a():
    voll = 3 * 12 + R(75, 10)
    t1 = (2 * 12 + 2 * R(75, 10)) * R(20, 100)
    t2 = R(1, 5) * (36 + R(75, 10))
    t3 = 20 * (12 + 12 + 12 + R(75, 10)) / 100
    return kette(genau(voll * R(20, 100), R(87, 10), " €"), wahr(t1 != t2 and t2 == t3 == R(87, 10), (t1, t2, t3)))

def p_2015_OS_K2b():
    return genau((3 * 12 + R(75, 10)) * R(8, 10), R(348, 10), " €")

def p_2015_OS_K3a():
    return genau(9460000000000 * 100, R(946, 100) * 10**14, " km")

def p_2015_OS_K3b():
    return genau(R(946, 100) * 10**12, 9460000000000)

def p_2015_OS_K3c():
    ts = R(403, 100) * 10**15 / (3 * 10**5)
    return kette(naeh(ts / 10**10, R(134, 100), tol=R(1, 200)), genau(365 * 24 * 3600, 31536000, " s"),
                 naeh(ts / 31536000, 426, " Jahre", tol=1))

def p_2015_OS_K4b():
    h = -3 * t**2 + 2400
    return kette(genau(h.subs(t, 0), 2400), genau(h.subs(t, 20), 1200))

def p_2015_OS_K4c():
    return kette(genau(R(1200 - 700, 100), 5, " m/s"), genau(5 * R(36, 10), 18, " km/h"))

def p_2015_OS_K4d():
    m = R(700 - 1200, 120 - 20)
    n = solve(Eq(1200, m * 20 + x), x)[0]
    return kette(genau(m, -5), genau(n, 1300), genau((m * t + n).subs(t, 260), 0))

def p_2015_OS_K5a():
    return genau(binomial(5, 3) - 2, 8)

def p_2015_OS_K5b():
    return genau(180 - 123 - 36, 21, "°")

def p_2015_OS_K5c():
    bd = R(41, 10) * sin(gr(123)) / sin(gr(36))
    de, ae = R(41, 10) * cos(gr(21)), R(41, 10) * sin(gr(21))
    return kette(naeh(bd, R(585, 100), " cm", tol=R(1, 100)), naeh(de + ae / tan(gr(36)), R(585, 100), " cm", tol=R(1, 100)))

def p_2015_OS_K5d():
    ae, de = R(41, 10) * sin(gr(21)), R(41, 10) * cos(gr(21))
    return kette(naeh(ae, R(147, 100), " cm", tol=R(1, 100)), naeh(de, R(383, 100), " cm", tol=R(1, 100)),
                 naeh(ae * de / 2, R(281, 100), " cm²", tol=R(1, 100)))

def p_2015_OS_K6a():
    return kette(genau(R(68, 100) * 10, R(68, 10), " m"), genau(R(80, 100) * 10, 8, " m"))

def p_2015_OS_K6c():
    hs = sqrt(R(68, 100)**2 + R(40, 100)**2)
    return kette(naeh(hs, R(789, 1000), " m", tol=R(1, 1000)), naeh(R(80, 100) * hs / 2, R(32, 100), " m²", tol=R(5, 1000)))

def p_2015_OS_K6d():
    f = 4 * R(32, 100) * 2
    return kette(genau(f, R(256, 100), " m²"), genau(f / 10 * 1000, 256, " ml"), wahr(256 < 375))

def p_2015_OS_K7a():
    return kette(naeh(R(680353, 17), R(400208, 10), tol=R(1, 10)), genau(round(R(680353, 17)), 40021))

def p_2015_OS_K7b():
    return kette(genau(R(22, 34), R(11, 17)), naeh(R(11, 17) * 100, R(647, 10), " %"))

def p_2015_OS_K7c():
    q = R(83 - 71, 83)
    return kette(naeh(q * 100, R(145, 10), " %"), naeh(q * 360, 52, "°", tol=R(6, 10)))

def p_2015_OS_K7d():
    p = R(1, 11) + R(10, 11) * R(1, 10) + R(10, 11) * R(9, 10) * R(1, 9)
    return kette(genau(p, R(3, 11)), genau(1 - R(10, 11) * R(9, 10) * R(8, 9), R(3, 11)),
                 genau(R(1, 10) + R(9, 10), 1), genau(R(1, 9) + R(8, 9), 1))


# ---------- 2016 (OS)

def p_2016_OS_B1a():
    return genau(R(8 + 40 + 60, 3), 36)

def p_2016_OS_B1b():
    return genau(solve(Eq(8 * x - 12, 36), x)[0], 6)

def p_2016_OS_B1d():
    return genau(R(30, 100) * 20, 6, " g")

def p_2016_OS_B1f():
    return kette(genau(R(5, 100), R(1, 20)), genau(R(5, 100) * 100, 5, " %"))

def p_2016_OS_B1g():
    f = (x - 1)**2 + 3
    return kette(genau(solve(f.diff(x), x)[0], 1), genau(f.subs(x, 1), 3))

def p_2016_OS_B1h():
    return genau(R(85, 10) * 10**5, 850000)

def p_2016_OS_B1i():
    return genau((2 + (-4)) / S(-2), 1)

def p_2016_OS_K2c():
    return genau(R(400 - 320, 320) * 100, 25, " %")

def p_2016_OS_K2d():
    w = {"Oma-Opa + Eltern einzeln": 34 + 2 * 21, "Familie + Oma-Opa": 60 + 34,
         "Familie + 2 einzeln": 60 + 2 * 21, "einzeln": 112}
    return kette(genau(min(w.values()), 76, " €"), wahr(min(w, key=w.get) == "Oma-Opa + Eltern einzeln"))

def p_2016_OS_K3a():
    return kette(genau(7 * R(305, 1000), R(2135, 1000), " m"), naeh(R(2135, 1000), R(214, 100), tol=R(1, 200)))

def p_2016_OS_K3b():
    return naeh(pi * R(107, 100)**2, R(360, 100), " m²", tol=R(1, 100))

def p_2016_OS_K3c():
    return naeh(R(4, 3) * pi * 6**3, R(9048, 10), " cm³")

def p_2016_OS_K3d():
    return naeh(4000 / R(78, 10), R(5128, 10), " cm³")

def p_2016_OS_K4a():
    w = [5 * R(89, 100)**k for k in range(9)]
    return kette(naeh(w[1], R(445, 100), tol=R(1, 200)), naeh(w[2], R(396, 100), tol=R(1, 200)),
                 naeh(w[4], R(314, 100), tol=R(1, 200)), naeh(w[5], R(279, 100), tol=R(1, 200)))

def p_2016_OS_K4c():
    th = log(R(1, 2)) / log(R(89, 100))
    return naeh(th, 6, " h", tol=R(1, 10))

def p_2016_OS_K4d():
    d = [5 * R(89, 100)**k - 5 * R(89, 100)**(k + 1) for k in range(2)]
    return kette(naeh(d[0], R(55, 100), tol=R(1, 200)), naeh(d[1], R(49, 100), tol=R(1, 100)), wahr(d[0] != d[1]))

def p_2016_OS_K4e():
    return naeh(5 * R(89, 100)**24, R(31, 100), " mg", tol=R(1, 200))

def p_2016_OS_K5a():
    return genau(int("".join(sorted("236", reverse=True))), 632)

def p_2016_OS_K5b():
    from itertools import permutations
    zahlen = sorted(int("".join(p)) for p in permutations("236"))
    return kette(wahr(zahlen == [236, 263, 326, 362, 623, 632], zahlen),
                 genau(R(sum(1 for n in zahlen if n % 2 == 0), len(zahlen)), R(2, 3)))

def p_2016_OS_K5c():
    return genau(R(1, len(range(101, 901))), R(1, 800))

def p_2016_OS_K5d():
    sechs = [n for n in range(101, 901) if n % 10 == 6]
    trost = [n for n in sechs if n % 100 == 26 and n != 326]
    return kette(genau(len(sechs), 80), genau(R(len(trost), len(sechs)), R(7, 80)))

def p_2016_OS_K6b():
    s, r = lambda k: 200 + R(3, 2) * k, lambda k: 2 * k
    return kette(genau(s(350), 725, " €"), genau(r(350), 700, " €"), genau(s(450), 875, " €"),
                 genau(r(450), 900, " €"), genau(solve(Eq(s(x), r(x)), x)[0], 400, " km"))

def p_2016_OS_K6d():
    l = solve([Eq(x + y, 16), Eq(3 * x + 5 * y, 66)], [x, y])
    return wahr(l == {x: 7, y: 9}, l)

def p_2016_OS_K7a():
    return genau(920 + 541, 1461, " m")

def p_2016_OS_K7b():
    return kette(naeh(sqrt(920**2 - 541**2), 744, " m", tol=1), naeh(920 * sin(gr(54)), 744, " m", tol=1))

def p_2016_OS_K7c():
    return naeh(744 * tan(gr(70 - 36)), 502, " m", tol=1)


# ---------- 2017 (OS)

def p_2017_OS_B1a():
    return genau(R(28, 7) * 6, 24)

def p_2017_OS_B1b():
    return genau(120 * R(20, 100), 24, " €")

def p_2017_OS_B1e():
    w = [-R(1, 100), -10**3, -10**2, -R(1, 10)]
    return genau(min(w), -1000)

def p_2017_OS_B1f():
    return genau(2 * 2, 4)

def p_2017_OS_B1g():
    return genau(log(100000, 10), 5)

def p_2017_OS_B1h():
    return genau((R(18, 10) + R(17, 10) + R(16, 10) + R(17, 10)) / 4, R(17, 10), " m")

def p_2017_OS_K2a():
    return genau(682069 - 8512, 673557)

def p_2017_OS_K2b():
    return kette(genau(R(344, 10) + R(112, 10) + 5, R(506, 10), " %"), genau(100 - R(494, 10), R(506, 10), " %"))

def p_2017_OS_K2c():
    return kette(genau(R(5, 100) * 360, 18, "°"), naeh(R(112, 1000) * 360, R(403, 10), "°"))

def p_2017_OS_K3b():
    return kette(genau(10 * 5, 50), naeh(pi * R(25, 10)**2, R(1963, 100), tol=R(1, 100)),
                 naeh(50 + pi * R(25, 10)**2, R(6963, 100), " m²", tol=R(1, 100)))

def p_2017_OS_K3d():
    return genau(R(140000, 17500), 8, " h")

def p_2017_OS_K4a():
    return genau(180 - R(628, 10) - R(349, 10), R(823, 10), "°")

def p_2017_OS_K4b():
    return naeh(R(12, 10) / tan(gr(R(349, 10))), R(172, 100), " m", tol=R(1, 100))

def p_2017_OS_K4c():
    bc = R(45, 10) * sin(gr(R(628, 10))) / sin(gr(R(349, 10)))
    return kette(naeh(bc, 7, " m", tol=R(1, 100)), naeh((R(45, 10) + bc) * 8, 92, " m²", tol=R(1, 10)))

def p_2017_OS_K5a():
    m = R(2 - (-1), 2 - (-4))
    n = solve(Eq(2, m * 2 + x), x)[0]
    return kette(genau(m, R(1, 2)), genau(n, 1), genau(m * (-4) + n, -1))

def p_2017_OS_K5b():
    return genau(R(1, 2) * (-10) + 1, -4)

def p_2017_OS_K5c():
    f = (x + 3)**2 - 2
    xs = solve(f.diff(x), x)[0]
    return kette(genau(xs, -3), genau(f.subs(x, xs), -2))

def p_2017_OS_K5d():
    f = (x + 3)**2 - 2
    l = sorted(solve(f, x), key=lambda v: N(v))
    return kette(genau(expand(f) - (x**2 + 6 * x + 7), 0), naeh(l[1], R(-159, 100), tol=R(1, 100)),
                 naeh(l[0], R(-441, 100), tol=R(1, 100)))

def p_2017_OS_K5e():
    q = -(((x + 3)**2 - 2) + 2)
    return genau(q - (-(x + 3)**2), 0)

def p_2017_OS_K6a():
    return kette(genau(R(1, 10), R(1, 10)), genau(R(1, 10) * 100, 10, " %"))

def p_2017_OS_K6b():
    return kette(genau(factorial(3), 6), genau(R(1, 6) + R(5, 6) * R(1, 5), R(1, 3)))

def p_2017_OS_K7a():
    return kette(naeh(870 * R(87, 100), 757, " hPa", tol=R(6, 10)), naeh(1000 * R(87, 100)**8, 328, " hPa", tol=R(6, 10)),
                 naeh(498 * R(87, 100)**3, 328, " hPa", tol=R(6, 10)))

def p_2017_OS_K7c():
    return kette(naeh(1000 * R(87, 100)**3, 659, tol=R(6, 10)), naeh(1000 * R(87, 100)**10, 248, tol=R(6, 10)))

def p_2017_OS_K7d():
    return naeh(1000 * R(87, 100)**4, 573, " hPa", tol=R(6, 10))


# ---------- 2018 (OS)

def p_2018_OS_B1a():
    return genau(R(3, 4) * R(12, 10), R(9, 10), " kg")

def p_2018_OS_B1b():
    return genau(500 - 5 * 30, 350, " cm")

def p_2018_OS_B1c():
    g = [4 * x - 8, 2 * x + 10 - 2, 5 * x + 12 - 2, -2 * x + 4]
    return wahr([e.subs(x, -2) == 0 for e in g] == [False, False, True, False])

def p_2018_OS_B1d():
    return wahr(R(5, 100) < R(5, 10))

def p_2018_OS_B1e():
    return genau(R(35, 10) * 60, 210, " min")

def p_2018_OS_B1f():
    return genau(solve(Eq(2 * 8 + 2 * x, 26), x)[0], 5, " cm")

def p_2018_OS_B1j():
    return genau(R(40, 100) * 5, 2)

def p_2018_OS_K2a():
    return kette(genau(600000 * R(108, 100), 648000, " €"), genau(R(48000, 600000) * 100, 8, " %"))

def p_2018_OS_K2b():
    return kette(genau(648000 - 600000, 48000), genau(648000 * R(108, 100) - 648000, 51840))

def p_2018_OS_K2c():
    u = [816293 * R(108, 100)**k for k in range(4)]
    erstes = 2017 + min(k for k in range(4) if u[k] > 10**6)
    return kette(genau(erstes, 2020), naeh(u[2], 952124, " €", tol=1), naeh(u[3], 1028294, " €", tol=1))

def p_2018_OS_K3a():
    return kette(genau(R(160, 8), 20), genau(1000 - (80 + 90 + 160 + 160 + 110), 400))

def p_2018_OS_K3b():
    s = solve(Eq(x + 3 * x, 1000 - (80 + 90 + 160 + 160 + 110)), x)[0]
    return kette(genau(s, 100), genau(3 * s, 300))

def p_2018_OS_K3c():
    return wahr([R(p, 10) for p in (10, 15, 55, 20)] == [1, R(3, 2), R(11, 2), 2] and 10 + 15 + 55 + 20 == 100)

def p_2018_OS_K3d():
    return kette(wahr(55 > 50), naeh(R(100, 15), R(67, 10), " %"))

def p_2018_OS_K4a():
    return genau(35 - 30, 5, "°")

def p_2018_OS_K4b():
    return kette(genau(180 - (180 - (180 - 90 - 30)) - 5, 55, "°"), genau(90 - 35, 55, "°"))

def p_2018_OS_K4c():
    return naeh(12 * sin(gr(55)) / sin(gr(5)), R(1128, 10), " m")

def p_2018_OS_K4d():
    cb = R(1128, 10) * sin(gr(30))
    return kette(genau(cb, R(564, 10), " m"), genau(cb + R(15, 10), R(579, 10), " m"), genau(cb + R(15, 10) + 12, R(699, 10), " m"))

def p_2018_OS_K5a():
    p = x**2 - 4 * x + 2
    return kette(genau(p.subs(x, -1), 7), genau(expand((x - 2)**2 - 2) - p, 0), genau(p.subs(x, 0), 2))

def p_2018_OS_K5b():
    p = x**2 - 4 * x + 2
    xs = solve(p.diff(x), x)[0]
    return kette(genau(xs, 2), genau(p.subs(x, xs), -2))

def p_2018_OS_K5c():
    return genau(expand((x - 2)**2 - 2) - (x**2 - 4 * x + 2), 0)

def p_2018_OS_K5d():
    return kette(wahr(real_roots(Poly(x**2 + 1, x)) == []), genau(-(x**2 + 1) - (-x**2 - 1), 0))

def p_2018_OS_K6a():
    k = pi * R(32, 10)**2
    return kette(naeh(k, R(3217, 100), tol=R(1, 100)), naeh(240 - k, R(20783, 100), " m²", tol=R(1, 100)))

def p_2018_OS_K6b():
    return naeh(pi * R(64, 10) * R(217, 10), R(4363, 10), " m²")

def p_2018_OS_K6c():
    return kette(genau(R(30, 50) * 100, 60, " cm"), genau(R(64, 10) / 50 * 100, R(128, 10), " cm"))

def p_2018_OS_K7a():
    return genau(R(2, 16) * 100, R(125, 10), " %")

def p_2018_OS_K7b():
    return kette(genau(R(2, 14), R(1, 7)), naeh(R(100, 7), R(143, 10), " %"))

def p_2018_OS_K7c():
    from itertools import permutations
    kugeln = ["M"] * 14 + ["S"] * 2
    paare = list(permutations(range(16), 2))
    mm = sum(1 for i, j in paare if kugeln[i] == kugeln[j] == "M")
    gleich = sum(1 for i, j in paare if kugeln[i] == kugeln[j])
    return kette(genau(R(14, 16) * R(13, 15), R(91, 120)), genau(R(mm, len(paare)), R(91, 120)),
                 genau(R(gleich, len(paare)), R(2, 16) * R(1, 15) + R(14, 16) * R(13, 15)))


# ---------- Ausführung

def alle():
    g = globals()
    return {k[2:].replace("_", "-"): g[k] for k in sorted(g) if k.startswith("p_")}


def rechne(i, fn):
    if i not in fn:
        return "nicht rechenbar"
    try:
        return fn[i]()
    except Exception as e:  # noqa: BLE001
        return "offen: " + type(e).__name__ + " " + str(e)


def spalte(pfad):
    fn = alle()
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        zeilen = list(csv.reader(fh, delimiter=";"))
    kopf, rest = zeilen[0], zeilen[1:]
    j = kopf.index("sympy")
    zaehl = {}
    for r in rest:
        r[j] = rechne(r[0], fn)
        jahr = r[0][:4]
        art = "abw" if r[j].startswith("abw") else ("offen" if r[j].startswith("offen") else r[j])
        zaehl.setdefault(jahr, Counter())[art] += 1
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", lineterminator="\n")
        w.writerow(kopf)
        w.writerows(rest)
    for jahr in sorted(zaehl):
        print(jahr, dict(zaehl[jahr]))
    for r in rest:
        if r[j].startswith(("abw", "offen")):
            print(" ", r[0], r[j])
    unbenutzt = set(fn) - {r[0] for r in rest}
    if unbenutzt:
        print("Funktionen ohne Tabellenzeile:", sorted(unbenutzt))


if __name__ == "__main__":
    if sys.argv[1:2] == ["--spalte"]:
        spalte(sys.argv[2])
    else:
        fn = alle()
        for i in sys.argv[1:] or list(fn):
            print(i + ";" + rechne(i, fn))
