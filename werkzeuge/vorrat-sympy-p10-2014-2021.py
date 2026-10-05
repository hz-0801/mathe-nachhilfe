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
