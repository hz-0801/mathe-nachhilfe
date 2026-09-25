# pruef.py – rechnet die Lösungen einer Einheit (oder der Zone) unabhängig nach.
# Aufruf: python pruef.py zone|e1|e2|e3|e4   -> Ausgabe auch in pruef_out_<teil>.txt
# Blattwerte (B=...) sind aus dem Lösungsquelltext (zone_l.tex, e<n>_l.tex) abgeschrieben.
import sys
import sympy as sp
import sympy.parsing.sympy_parser

x = sp.symbols('x')
ZEILEN = []
FEHLER = 0


def P(s):
    """'lhs = rhs' oder Term als String -> sympy"""
    s = s.replace('−', '-').replace('^', '**').replace('·', '*')
    tr = (sp.parsing.sympy_parser.standard_transformations +
          (sp.parsing.sympy_parser.implicit_multiplication_application,))
    if '=' in s:
        l, r = s.split('=')
        return sp.parse_expr(l, transformations=tr, local_dict={'x': x}) - \
            sp.parse_expr(r, transformations=tr, local_dict={'x': x})
    return sp.parse_expr(s, transformations=tr, local_dict={'x': x})


def loes(glg):
    """reelle Lösungen, aufsteigend"""
    e = P(glg)
    return sorted([s for s in sp.solve(sp.Eq(e, 0), x) if s.is_real], key=lambda v: float(v))


def zahl(v):
    return float(sp.N(v))


def gleich(a, b, tol=0.006):
    if a is None or b is None:
        return a is None and b is None
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, str) or isinstance(b, str):
        return str(a) == str(b)
    if isinstance(a, (list, tuple)) or isinstance(b, (list, tuple)):
        a = list(a) if isinstance(a, (list, tuple)) else [a]
        b = list(b) if isinstance(b, (list, tuple)) else [b]
        if len(a) != len(b):
            return False
        return all(gleich(u, v, tol) for u, v in zip(sorted(a, key=zahl_sort), sorted(b, key=zahl_sort)))
    if isinstance(a, sp.Basic) and a.free_symbols or isinstance(b, sp.Basic) and b.free_symbols:
        return sp.simplify(sp.expand(a) - sp.expand(b)) == 0
    return abs(zahl(a) - zahl(b)) <= tol


def zahl_sort(v):
    try:
        return zahl(v)
    except Exception:
        return 0


def c(nr, skript, blatt, tol=0.006):
    global FEHLER
    ok = gleich(skript, blatt, tol)
    if not ok:
        FEHLER += 1
    ZEILEN.append(f"{nr:8} Skript: {fmt(skript):32} Blatt: {fmt(blatt):32} {'OK' if ok else 'ABWEICHUNG'}")


def fmt(v):
    if isinstance(v, (list, tuple)):
        return '[' + ', '.join(fmt(u) for u in v) + ']'
    if isinstance(v, sp.Basic) and not v.free_symbols:
        f = zahl(v)
        return str(v) if len(str(v)) < 14 else f"{f:.4f}"
    return str(v)


def expr(s):
    return sp.expand(P(s))


def wahr(xw, glg):
    e = P(glg)
    return sp.simplify(e.subs(x, xw)) == 0


def rund(v, n=2):
    return round(zahl(v) + 1e-12, n)


# ---- Zahlen aus Kasten, Beispiel, Original und Fehlerliste des Eintrags (2.1, 3.6) ----
# x^2 = 0 (Kasten 1) fehlt bewusst: der Nullfall ist in jeder Form zu x^2 = 0 proportional;
# auf dem Blatt steht er nur als 5x^2 = 0 und 3x^2 + 5 = 5, nie wortgleich.
VERBOTEN_GLG = ['x^2 = 36', 'x^2 = -36', '(x+4)^2 = 36', '(x+4)^2 = 0', 'x^2 - 7x = 0',
                '(x+3)(x-9) = 0', 'x(x+8) = 20', '3x^2 + 24x - 60 = 0', 'x^2 + 8x - 20 = 0',
                'x^2 + 8x + 16 = 0', 'x^2 + 8x + 20 = 0', '(x+7)^2 = 0', '(x+8)^2 = 16', 'x^2 + 1 = 0',
                'x(x+5) = -6', '2x^2 + 8x + 6 = 0', 'x^2 - 6x + 7 = 0', '-x^2 - 2x + 5 = -10',
                'x^2 - x - 2 = 0', '(x-2)^2 - 4 = -2x + 3', 'x^2 + 2x - 1 = 3x + 1', 'x^2 = 49',
                'x^2 = -25', 'x^2 = 7x', '(x+3)^2 = x^2 + 9', 'x^2 = 9', 'x^2 + 4x + 3 = 0',
                'x^2 + 2x - 15 = 0', 'x^2 + 8x = 20', 'x + 5 = 12', '-x = 5', '5x = 15', 'x + 17 = 12']
VERBOTEN_LSG = [[-6, 6], [-10, 2], [-4], [0, 7], [-3, 9], [-12, -4], [-3, -2], [-3, -1],
                [3 - sp.sqrt(2), 3 + sp.sqrt(2)], [-5, 3], [-3 - sp.sqrt(2), -3 + sp.sqrt(2)],
                [-1, 2], [-7, 7], [-3, 3], [-5], [7]]


def verboten(nr, glg):
    """prüft eine Aufgabengleichung gegen Kasten-, Beispiel- und Originalgleichungen"""
    global FEHLER
    e = sp.Poly(sp.expand(P(glg)), x)
    treffer = []
    for v in VERBOTEN_GLG:
        f = sp.Poly(sp.expand(P(v)), x)
        if e.degree() == f.degree() and e.degree() > 0:
            q = sp.simplify(e.as_expr() / f.as_expr())
            if q.is_number:
                treffer.append('Gleichung ' + v)
    try:
        L = loes(glg)
    except Exception:
        L = None
    if L and e.degree() == 2:
        for v in VERBOTEN_LSG:
            if len(v) == len(L) and all(abs(zahl(a) - zahl(b)) < 1e-9 for a, b in zip(L, sorted(v, key=zahl))):
                treffer.append('Lösungen ' + str(v))
    if treffer:
        FEHLER += 1
    ZEILEN.append(f"{nr:8} Kasten/Original: {glg:40} {'ABWEICHUNG ' + '; '.join(treffer) if treffer else 'OK'}")


# =============================== Zone ===============================
def zone():
    for nr, t, b in [('Z1a', '5^2', 25), ('Z1b', '9^2', 81), ('Z1c', '(-8)^2', 64), ('Z1d', '0.4^2', 0.16),
                     ('Z1e', '2.5^2', 6.25), ('Z1f', '3*(-2)^2', 12), ('Z1g', '10-4^2', -6),
                     ('Z2a', '3*(2+4)', 18), ('Z2b', '(7-5)*6', 12), ('Z2c', '(-3)*(-3+8)', -15),
                     ('Z2d', '(-4)*(-4-2)', 24), ('Z2e', '(-1-3)*(-1+2)', -4), ('Z2f', '(-3)^2+5*(-3)+6', 0)]:
        c(nr, P(t), b)
    for nr, g, b in [('Z3a', 'x-6=3', 9), ('Z3b', '4x=28', 7), ('Z3c', '-x=8', -8), ('Z3d', 'x+2=-5', -7),
                     ('Z3e', '2x+7=-3', -5), ('Z3f', '5x-3=2x+9', 4)]:
        c(nr, loes(g), b)
    for nr, xw, g, b in [('Z4a', 3, '2x+1=7', True), ('Z4b', 5, 'x-2=4', False), ('Z4c', -2, '3x+10=4', True),
                         ('Z4d', -3, '4-2x=10', True), ('Z4e', -1, '5x+2=3x-4', False)]:
        c(nr, wahr(xw, g), b)
    for nr, r, b in [('Z5a', 81, 9), ('Z5b', 144, 12), ('Z5c', sp.Rational(1, 4), 0.5), ('Z5d', 7, 2.65),
                     ('Z5e', 0, 0)]:
        c(nr, rund(sp.sqrt(r)), b)
    c('Z5f', None if sp.sqrt(-16).is_real is False else 4, None)
    # Scheitel, Öffnung, Zahl der Nullstellen
    for nr, t, b in [('Z6a', '(x-2)^2+1', (2, 1, 'oben', 0)), ('Z6b', '(x-4)^2-3', (4, -3, 'oben', 2)),
                     ('Z6c', '(x+1)^2-2', (-1, -2, 'oben', 2)), ('Z6d', '-(x-3)^2+4', (3, 4, 'unten', 2)),
                     ('Z6e', '(x+2)^2', (-2, 0, 'oben', 1)), ('Z6f', '-(x+1)^2-5', (-1, -5, 'unten', 0))]:
        f = P(t)
        xs = sp.solve(sp.diff(f, x), x)[0]
        a = sp.Poly(f, x).LC()
        n = len([s for s in sp.solve(f, x) if s.is_real])
        c(nr + ' S', [xs, f.subs(x, xs)], [b[0], b[1]])
        c(nr + ' Öff', 'oben' if a > 0 else 'unten', b[2])
        c(nr + ' Anz', n, b[3])
    for nr, t, b in [('Z7a', '3x+x^2+2', 'x^2+3x+2'), ('Z7b', '5+x^2-4x', 'x^2-4x+5'),
                     ('Z7c', 'x^2+2x-7+3x', 'x^2+5x-7'), ('Z7d', '2x^2-3+x-x^2+8', 'x^2+x+5'),
                     ('Z7e', '4-3x-x^2+5x', '-x^2+2x+4'),
                     ('Z8a', 'x*(x+4)', 'x^2+4x'), ('Z8b', '(x+2)*(x+5)', 'x^2+7x+10'),
                     ('Z8c', '(x-3)*(x+6)', 'x^2+3x-18'), ('Z8d', '(x+5)^2', 'x^2+10x+25'),
                     ('Z8e', '(x-3)^2', 'x^2-6x+9'), ('Z8f', 'x^2+9x', 'x*(x+9)'), ('Z8g', 'x^2-2x', 'x*(x-2)'),
                     ('Z9a', '(x+9)^2', 'x^2+18x+81'), ('Z9b', '(x-8)^2', 'x^2-16x+64')]:
        c(nr, expr(t), expr(b))
    c('Z9a Feh', sp.expand(P('(x+9)^2') - P('x^2+81')), expr('18x'))


# =============================== Einheit 1 ===============================
def e1():
    for nr, g, b in [('1a', 'x^2+3=12', 'quadratisch'), ('1b', '4x-1=7', 'linear'), ('1c', '(x-2)^2=5', 'quadratisch'),
                     ('1d', '3*(x+1)=9', 'linear'), ('1e', '2x=x^2', 'quadratisch')]:
        c(nr, 'quadratisch' if sp.Poly(sp.expand(P(g)), x).degree() == 2 else 'linear', b)
    for nr, r, b in [('2a', 17, 'positiv'), ('2b', -8, 'negativ'), ('2c', 0, 'null'), ('2d', 2.25, 'positiv'),
                     ('2e', -0.5, 'negativ')]:
        c(nr, 'positiv' if r > 0 else ('null' if r == 0 else 'negativ'), b)
    c('3 Bsp', loes('x^2=25'), [5, -5])
    for nr, g, b in [('3a', 'x^2=4', [2, -2]), ('3b', 'x^2=81', [9, -9]), ('3c', 'x^2=1', [1, -1]),
                     ('3d', 'x^2=100', [10, -10]), ('3f', 'x^2=11', [3.32, -3.32]), ('3g', 'x^2=-9', []),
                     ('4 Bsp', '2x^2-32=0', [4, -4]), ('4a', '3x^2=75', [5, -5]), ('4b', 'x^2-12=52', [8, -8]),
                     ('4c', '3x^2-7=5', [2, -2]), ('4d', '19-x^2=3', [4, -4]), ('4f', '2x^2+9=1', []),
                     ('4g', '3x^2+5=5', [0]),
                     ('5 Bsp', '(x-3)^2=25', [8, -2]), ('5a', '(x-1)^2=9', [4, -2]), ('5b', '(x-2)^2=16', [6, -2]),
                     ('5c', '(x-5)^2=1', [6, 4]), ('5d', '(x+2)^2=9', [1, -5]), ('5e', '(x-4)^2=0', [4]),
                     ('9a', '3x^2=48', [4, -4]), ('9b', '2x^2=162', [9, -9]), ('9c', '(x+6)^2=4', [-4, -8]),
                     ('9d', '(x+5)^2=4', [-3, -7])]:
        c(nr, [rund(v) for v in loes(g)], b)
        verboten(nr, g)
    c('3e', sp.sqrt(64), 8)
    c('4e r^2', rund(sp.Rational(1000, 12) / sp.pi), 26.53)
    c('4e r', rund(sp.sqrt(sp.Rational(1000, 12) / sp.pi)), 5.15)
    c('6 Bsp', wahr(-2, 'x^2+5=9'), True)
    for nr, xw, g, b in [('6a', 1, 'x^2+3=4', True), ('6b', 3, 'x^2-1=10', False), ('6c', 4, '2x^2=32', True),
                         ('6d', 5, '30-x^2=5', True), ('6e', -3, '2x^2=16', False), ('6f', -1, '(x-2)^2=1', False),
                         ('6g', -7, '(x+3)^2=16', True)]:
        c(nr, wahr(xw, g), b)
        verboten(nr, g)
    # Nr. 7: Parabel y=(x-1)^2-2 mit waagerechten Geraden
    for nr, cc, b in [('7 Bsp', 2, [-1, 3]), ('7a', -1, [0, 2]), ('7b', -2, [1]), ('7c', -3, [])]:
        c(nr, loes(f'(x-1)^2-2={cc}'), b)
    for nr, g, b in [('7d', '(x+2)^2+1=0', 0), ('7e', '-(x-1)^2+3=-2', 2), ('7f', '(x-3)^2-5=-5', 1)]:
        c(nr, len(loes(g)), b)
        verboten(nr, g)
    c('8a', len(loes('x^2=-2')), 0)
    c('8b', len(loes('x^2+7=7')), 1)
    c('8c A1', len(loes('(x-6)^2=0')) == 1, True)
    c('8c A2', wahr(2, '(x+5)^2=9') and wahr(8, '(x+5)^2=9'), False)
    c('8c A2 L', loes('(x+5)^2=9'), [-8, -2])
    c('8c Bsp', len(loes('x^2+4=0')), 0)
    for nr, g in [('8a', 'x^2=-2'), ('8b', 'x^2+7=7'), ('8c', '(x-6)^2=0'), ('8c', '(x+5)^2=9'), ('8c', 'x^2+4=0'),
                  ('10a', 'x^2=30'), ('10b', 'x^2=-30'), ('10c', '(x-2)^2=0')]:
        verboten(nr, g)
    c('10a', len(loes('x^2=30')), 2)
    c('10b', len(loes('x^2=-30')), 0)
    c('10c', loes('(x-2)^2=0'), [2])


# =============================== Einheit 2 (p-q-Formel) ===============================
def normal(glg):
    """Normalform-Koeffizienten p, q aus beliebiger quadratischer Gleichung"""
    a, b, cc = sp.Poly(sp.expand(P(glg)), x).all_coeffs()
    return sp.nsimplify(b / a), sp.nsimplify(cc / a)


def e2():
    for nr, g, b in [('11a', 'x^2-5x+4=0', 'Formel'), ('11b', 'x^2=13', 'Wurzel'), ('11c', '(x+2)^2=11', 'Rueckwaerts'),
                     ('11d', '3x^2-12=0', 'Wurzel'), ('11e', '2x^2+3x-1=0', 'Formel')]:
        s = sp.Poly(sp.expand(P(g)), x).all_coeffs()
        art = 'Rueckwaerts' if '(' in g else ('Wurzel' if s[1] == 0 else 'Formel')
        c(nr, art, b)
    for nr, g, b in [('12a', 'x^2+7x+10=0', (7, 10)), ('12b', 'x^2-3x+2=0', (-3, 2)), ('12c', 'x^2+4x-7=0', (4, -7)),
                     ('12d', 'x^2-x-12=0', (-1, -12)), ('12e', 'x^2-11x=0', (-11, 0))]:
        c(nr, list(normal(g)), list(b))
    for nr, g, b in [('13a', 'x^2+3x-4=0', 1), ('13b', '2x^2+6x-8=0', 2), ('13c', '5x^2-10x+5=0', 5),
                     ('13d', '-x^2+4x+5=0', -1), ('13e', '0.5x^2+x-3=0', 0.5)]:
        c(nr, sp.Poly(sp.expand(P(g)), x).LC(), b)
    # p-q-Formel: -p/2 und Wert unter der Wurzel, dann Lösungen
    for nr, g, b_m, b_d, b in [('14 Bsp', 'x^2+2x-8=0', -1, 9, [2, -4]),
                               ('14a', 'x^2+6x+8=0', -3, 1, [-2, -4]), ('14b', 'x^2+10x+9=0', -5, 16, [-1, -9]),
                               ('14c', 'x^2+6x+5=0', -3, 4, [-1, -5]), ('14d', 'x^2+10x+16=0', -5, 9, [-2, -8]),
                               ('14e', 'x^2-6x+8=0', 3, 1, [4, 2]), ('14f', 'x^2+2x-24=0', -1, 25, [4, -6]),
                               ('15 Bsp', '2x^2+12x=32', -3, 25, [2, -8]),
                               ('15a', 'x^2-4x=5', 2, 9, [5, -1]), ('15b', 'x^2+5x=x+12', -2, 16, [2, -6]),
                               ('15c', '5x^2-20x+15=0', 2, 1, [3, 1]), ('15d', '-x^2+8x-12=0', 4, 4, [6, 2]),
                               ('16a', 'x^2+3x-10=0', -1.5, 12.25, [2, -5]), ('16b', 'x^2-10x+25=0', 5, 0, [5]),
                               ('16c', 'x^2+4x+7=0', -2, -3, []), ('16d', 'x^2+5x+3=0', -2.5, 3.25, None),
                               ('16e', 'x^2-4x+1=0', 2, 3, [3.73, 0.27]), ('16f', 'x^2+2x-35=0', -1, 36, [5, -7]),
                               ('17a', '(x+1)^2=3x+7', 0.5, 6.25, [3, -2]), ('17b', 'x*(x+4)=21', -2, 25, [3, -7]),
                               ('17e', '2x^2-12x+10=0', 3, 4, [5, 1]),
                               ('18b', 'x^2-5=-x+1', -0.5, 6.25, [2, -3]), ('18c', '(x-1)^2-3=x+2', 1.5, 6.25, [4, -1]),
                               ('19a', '2x^2-10x+12=0', 2.5, 0.25, [3, 2]), ('19b', '5x^2+10x-15=0', -1, 4, [1, -3]),
                               ('19c', 'x^2-10x+16=0', 5, 9, [8, 2]), ('19d', 'x^2-14x+40=0', 7, 9, [10, 4])]:
        p, q = normal(g)
        c(nr + ' -p/2', -p / 2, b_m)
        c(nr + ' D', (p / 2) ** 2 - q, b_d)
        if b is not None:
            c(nr, [rund(v) for v in loes(g)], b)
        verboten(nr, g)
    c('16d Anz', len(loes('x^2+5x+3=0')), 2)
    c('16f Probe', P('x^2+2x-35').subs(x, 5), 0)
    for nr, g, b in [('17c', '2x^2-50=0', [5, -5]), ('17d', '(x-1)^2=16', [5, -3])]:
        c(nr, loes(g), b)
        verboten(nr, g)
    c('17e normiert', list(normal('2x^2-12x+10=0')), [-6, 5])
    # Nr. 18: Schnittpunkte
    c('18a/b y', [P('-x+1').subs(x, v) for v in loes('x^2-5=-x+1')], [4, -1])
    c('18c y', [P('x+2').subs(x, v) for v in loes('(x-1)^2-3=x+2')], [1, 6])
    c('18c f=g', [P('(x-1)^2-3').subs(x, v) for v in loes('(x-1)^2-3=x+2')], [1, 6])
    c('19a falsch', rund(5 + sp.sqrt(13)), rund(P('5+sqrt(13)')))
    c('20a D', (sp.Rational(2, 2)) ** 2 - 5, -4)
    c('20b normiert', list(normal('4x^2+8x-4=0')), [2, -1])
    c('20c D', 9 - 9, 0)
    c('20c L', loes('x^2-6x+9=0'), [3])
    for nr, g in [('20a', 'x^2+2x+5=0'), ('20b', '4x^2+8x-4=0'), ('20c', 'x^2-6x+9=0'), ('11a', 'x^2-5x+4=0'),
                  ('11c', '(x+2)^2=11'), ('11e', '2x^2+3x-1=0'), ('12a', 'x^2+7x+10=0'), ('12b', 'x^2-3x+2=0'),
                  ('12d', 'x^2-x-12=0'), ('13a', 'x^2+3x-4=0'), ('13b', '2x^2+6x-8=0'), ('13d', '-x^2+4x+5=0'),
                  ('13e', '0.5x^2+x-3=0')]:
        verboten(nr, g)
    # Nr. 21: Anhalteweg
    v = sp.symbols('v')
    L = sorted(sp.solve(sp.Rational(3, 10) * v + sp.Rational(1, 100) * v ** 2 - 40, v))
    c('21a', sp.expand(100 * (sp.Rational(3, 10) * v + sp.Rational(1, 100) * v ** 2 - 40)), v ** 2 + 30 * v - 4000)
    c('21b', L, [-80, 50])
    c('21c', max(L) - 30, 20)


# =============================== Einheit 3 (Sachaufgaben) ===============================
def e3():
    # Nr. 22: passende Lösung – Länge, Anzahl, Zeit nicht negativ; Zahl und Temperatur beliebig
    for nr, art, l, b in [('22a', 'Laenge', [7, -3], 'x1'), ('22b', 'Anzahl', [-12, 9], 'x2'),
                          ('22c', 'Zahl', [4, -4], 'beide'), ('22d', 'Zeit', [2.5, -1.2], 'x1'),
                          ('22e', 'Temperatur', [-5, 3], 'beide')]:
        if art in ('Zahl', 'Temperatur'):
            s = 'beide'
        else:
            s = 'x1' if l[0] >= 0 else 'x2'
        c(nr, s, b)
    for nr, g, b in [('23 Bsp', 'x^2=144', [12, -12]), ('23a', 'x^2=225', [15, -15]), ('23b', 'x^2=900', [30, -30]),
                     ('23c', '2x^2=50', [5, -5]), ('23d', 'x^2+7=71', [8, -8]), ('23e', 'x^2-19=81', [10, -10]),
                     ('23f', 'x*(x+1)=72', [8, -9]),
                     ('24 Bsp', 'x*(x+3)=40', [5, -8]), ('24b', 'x*(x+2)=48', [6, -8]),
                     ('25a', '(x+6)^2=625', [19, -31]), ('25b', '(x+1)*(x+6)=84', [6, -13]),
                     ('26a', 'x*(x+4)=45', [5, -9]), ('26b', 'x*(x+5)=14', [2, -7]), ('26c', 'x*(x+3)=54', [6, -9]),
                     ('26d', 'x*(x+1)=30', [5, -6]), ('27', 'x^2+4x=32', [4, -8])]:
        c(nr, loes(g), b)
        verboten(nr, g)
    c('23f Nachfolger', sorted([v + 1 for v in loes('x*(x+1)=72')], key=zahl), [-8, 9])
    # Seiten: Breite = positive Lösung, Länge = Breite + d (d aus dem Aufgabentext)
    for nr, g, d, b in [('24 Bsp', 'x*(x+3)=40', 3, (5, 8)), ('24d', 'x*(x+2)=48', 2, (6, 8)),
                        ('25b', '(x+1)*(x+6)=84', 5, (6, 11)), ('26a', 'x*(x+4)=45', 4, (5, 9)),
                        ('26b', 'x*(x+5)=14', 5, (2, 7)), ('26c', 'x*(x+3)=54', 3, (6, 9)),
                        ('26d', 'x*(x+1)=30', 1, (5, 6)), ('27b', 'x*(x+4)=32', 4, (4, 8))]:
        br = max(loes(g), key=zahl)
        c(nr + ' Seiten', [br, br + d], list(b))
    c('24 Bsp -p/2 D', [-sp.Rational(3, 2), sp.Rational(9, 4) + 40], [-1.5, 42.25])
    c('24e Probe', 6 * 8, 48)
    c('25a', max(loes('(x+6)^2=625'), key=zahl), 19)
    c('25b -p/2 D', [-sp.Rational(7, 2), sp.Rational(49, 4) + 78], [-3.5, 90.25])
    c('26c Umfang falsch', loes('2x+2*(x+3)=54'), [12])
    c('27a', [wahr(4, 'x^2+4x=32'), wahr(-8, 'x^2+4x=32')], [True, True])


# =============================== Einheit 4 (Ausblick Nullprodukt) ===============================
def e4():
    for nr, g, b in [('28a', 'x*(x+4)=0', 'null'), ('28b', '(x-2)*(x+5)=12', 'andere'), ('28c', '(x+1)*(x-6)=0', 'null'),
                     ('28d', 'x*(x-3)=10', 'andere'), ('28e', '3x*(x+2)=0', 'null')]:
        c(nr, 'null' if P(g.split('=')[1]) == 0 else 'andere', b)
        verboten(nr, g)
    for nr, g, b in [('29 Bsp', '(x-2)*(x-5)=0', [2, 5]), ('29a', '(x-1)*(x-4)=0', [1, 4]), ('29b', '(x-3)*(x-6)=0', [3, 6]),
                     ('29c', '(x-2)*(x-7)=0', [2, 7]), ('29d', '(x-5)*(x-8)=0', [5, 8]), ('29e', '(x+3)*(x-1)=0', [-3, 1]),
                     ('29f', 'x*(x+6)=0', [0, -6]), ('29g', '(x+2)*(x+2)=0', [-2]),
                     ('30 Bsp', 'x^2-5x=0', [0, 5]), ('30a', 'x^2+3x=0', [0, -3]), ('30b', 'x^2-6x=0', [0, 6]),
                     ('30c', '2x^2+10x=0', [0, -5]), ('30d', 'x*(x+3)=28', [4, -7]), ('30e', 'x^2-9x+20=0', [4, 5]),
                     ('31a', 'x^2=4x', [0, 4]), ('31b', 'x^2=9x', [0, 9]), ('31c', 'x*(x-4)=12', [6, -2]),
                     ('31d', 'x*(x-3)=18', [6, -3]), ('32b', 'x^2=11x', [0, 11])]:
        c(nr, loes(g), b)
        verboten(nr, g)
    c('29h', wahr(-3, '(x+5)*(x-2)=-10'), True)
    c('29h Wert', P('(x+5)*(x-2)').subs(x, -3), -10)
    c('30d -p/2 D', [-sp.Rational(3, 2), sp.Rational(9, 4) + 28], [-1.5, 30.25])
    c('30e Faktor', expr('(x-4)*(x-5)'), expr('x^2-9x+20'))
    # Prüfungshöhe (P10 2025): genau eine der vier Optionen erfüllt die Gleichung
    opt = [3, 4, -3, -12]
    c('30f', [o for o in opt if wahr(o, 'x*(x+7)=-12')], [-3])
    verboten('30f', 'x*(x+7)=-12')
    c('31c falsch', [12, 16], [12, 12 + 4])
    c('31c -p/2 D', [2, 4 + 12], [2, 16])
    c('31d -p/2 D', [sp.Rational(3, 2), sp.Rational(9, 4) + 18], [1.5, 20.25])
    c('32a', P('(x-9)*(x+4)').subs(x, 9), 0)
    t = sp.symbols('t')
    Lt = sorted(sp.solve(15 * t - 5 * t ** 2, t))
    c('33b', Lt, [0, 3])
    c('33b Faktor', sp.expand(5 * t * (3 - t)), sp.expand(15 * t - 5 * t ** 2))


TEILE = {'zone': zone, 'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4}

if __name__ == '__main__':
    teil = sys.argv[1]
    TEILE[teil]()
    ZEILEN.append(f"Abweichungen: {FEHLER}")
    out = '\n'.join(ZEILEN)
    print(out)
    with open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8') as fh:
        fh.write(out + '\n')
