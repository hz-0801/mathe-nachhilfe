# -*- coding: utf-8 -*-
# pruef.py – Mindestprüfung 5.1 a) für das Lernblatt Quadratische Gleichungen, Kl. 9 Gymnasium.
# Aufruf: python pruef.py zone|e1|e2|e3|e4
# Skriptwerte werden mit sympy unabhängig gerechnet; die Blattwerte sind aus dem
# Lösungsquelltext (<teil>_l.tex) abgeschrieben. Dazu die Sperrliste (2.1): keine ganze
# Gleichung aus Kasten, Beispiel, Typischen Fehlern oder Original des Eintrags in <teil>_a.tex.
import sys, re, io
from sympy import symbols, Eq, solve, sympify, N, expand, Poly, pi, sqrt, Mul, Pow

x = symbols('x')
teil = sys.argv[1]
zeilen = []
abw = 0


def P(s):
    s = s.replace('−', '-').replace(' ', '')
    s = re.sub(r'(\d)x', r'\1*x', s)
    s = re.sub(r'(\d|x)\(', r'\1*(', s)
    s = re.sub(r'\)(\(|x|\d)', r')*\1', s)
    s = s.replace('^', '**')
    return sympify(s)


def loes(eq):
    l, r = eq.split('=')
    sols = solve(Eq(P(l), P(r)), x)
    return sorted(float(N(s)) for s in sols if s.is_real)


def anzahl(eq):
    return len(loes(eq))


def val(expr, xv=None):
    e = P(expr)
    if xv is not None:
        e = e.subs(x, xv)
    return float(N(e))


def probe(eq, xv):
    l, r = eq.split('=')
    return abs(val(l, xv) - val(r, xv)) < 1e-9


def ausm(expr):
    return str(expand(P(expr)))


def normal(eq):  # linke Seite nach dem Ordnen (rechts 0), nicht normiert
    l, r = eq.split('=')
    return str(expand(P(l) - P(r)))


def normiert(eq):
    l, r = eq.split('=')
    p = Poly(expand(P(l) - P(r)), x)
    a = p.LC()
    return str(expand(p.as_expr() / a))


def pq(eq):
    l, r = eq.split('=')
    p = Poly(expand(P(l) - P(r)), x)
    c = p.all_coeffs()
    return (float(c[1] / c[0]), float(c[2] / c[0]))


def disk(eq):
    pp, qq = pq(eq)
    return (pp / 2) ** 2 - qq


def grad(eq):
    l, r = eq.split('=')
    return Poly(expand(P(l) - P(r)), x).degree()


def produkt_null(eq):
    l, r = eq.split('=')
    return isinstance(P(l), Mul) and P(r) == 0 and any(a.has(x) for a in P(l).args) \
        and sum(1 for a in P(l).args if a.has(x)) >= 2 or \
        (isinstance(P(l), Pow) and P(r) == 0)


def weg(eq):
    l, r = eq.split('=')
    L, R = P(l), P(r)
    if isinstance(L, Mul) and R == 0:
        return 'Nullprodukt'
    if isinstance(L, Pow) and L.base != x:
        return 'rückwärts'
    p = Poly(expand(L - R), x)
    if p.coeff_monomial(x) == 0:
        return 'Wurzel'
    return 'Formel'


def scheitel(expr):
    p = Poly(expand(P(expr)), x)
    a, b, c = [float(v) for v in p.all_coeffs()]
    xs = -b / (2 * a)
    ys = val(expr, xs)
    return (round(xs, 6), round(ys, 6), 'oben' if a > 0 else 'unten')


def fmt(v):
    if isinstance(v, float):
        return ('%.4f' % v).rstrip('0').rstrip('.')
    if isinstance(v, (list, tuple)):
        return '[' + '; '.join(fmt(e) for e in v) + ']'
    return str(v)


def gleich(a, b, tol):
    if isinstance(a, (list, tuple)):
        if not isinstance(b, (list, tuple)) or len(a) != len(b):
            return False
        if all(isinstance(e, (int, float)) for e in list(a) + list(b)):
            return all(abs(p - q) <= tol for p, q in zip(sorted(a), sorted(b)))
        return all(gleich(p, q, tol) for p, q in zip(a, b))
    if isinstance(a, (bool, str)) or isinstance(b, (bool, str)):
        return a == b
    return abs(a - b) <= tol


def c(nr, skript, blatt, tol=0.0051):
    global abw
    ok = gleich(skript, blatt, tol)
    if not ok:
        abw += 1
    zeilen.append('%s\t%s\t%s\t%s' % (nr, fmt(skript), fmt(blatt), 'OK' if ok else 'ABWEICHUNG'))


WA = lambda b: '(wA)' if b else '(fA)'

if teil == 'zone':
    for nr, e, b in [('1a', '7^2', 49), ('1b', '12^2', 144), ('1c', '(-9)^2', 81), ('1d', '0.6^2', 0.36),
                     ('1e', '3*(-2)^2', 12), ('2a', '4*(2+3)', 20), ('2b', '18-3*4', 6),
                     ('2c', '(-2)*(-2+6)', -8), ('2d', '(-4)*(-4-3)', 28), ('2e', '2*(-3)^2-7', 11)]:
        c(nr, val(e), b)
    for nr, eq, xv, b in [('3a', '2x+1=7', 3, '(wA)'), ('3b', 'x-2=4', 5, '(fA)'), ('3c', '3x+10=4', -2, '(wA)'),
                          ('3d', 'x(x+6)=-8', -2, '(wA)'), ('3e', '4-2x=2', -1, '(fA)'),
                          ('4', 'x^2+3x=10', -5, '(wA)'), ('5a', 'x^2+2x=8', -4, '(wA)'),
                          ('5b', 'x^2-3x=4', -2, '(fA)')]:
        c(nr, WA(probe(eq, xv)), b)
    c('4 linke Seite', val('(-5)^2+3*(-5)'), 10)
    c('5a linke Seite', val('(-4)^2+2*(-4)'), 8)
    c('5b linke Seite', val('(-2)^2-3*(-2)'), 10)
    for nr, eq, b in [('6a', 'x+6=11', [5]), ('6b', '4x=28', [7]), ('6c', 'x+8=0', [-8]), ('6d', '-x=7', [-7]),
                      ('6e', '2x-7=0', [3.5]), ('6f', '3x+4=x-6', [-5])]:
        c(nr, loes(eq), b)
    for nr, r, b in [('7a', 49, 7), ('7b', 100, 10), ('7c', 169, 13), ('7d', 0.25, 0.5), ('7f', 36 - 11, 5),
                     ('7g', 7, 2.65), ('7h', 13.5, 3.67)]:
        c(nr, float(N(sqrt(r))), b)
    c('7e', 'gibt es nicht' if -16 < 0 else 'x', 'gibt es nicht')
    for nr, e, b in [('8a', '(x-2)^2+1', (2, 1, 'oben')), ('8b', '(x-3)^2', (3, 0, 'oben')),
                     ('8c', 'x^2-4', (0, -4, 'oben')), ('8d', '(x+1)^2-5', (-1, -5, 'oben')),
                     ('8e', '-(x-2)^2+3', (2, 3, 'unten'))]:
        c(nr, scheitel(e), b)
    for nr, e, b in [('9a', 'x(x+4)', 'x^2+4x'), ('9b', '3x(x-2)', '3x^2-6x'), ('9c', '(x+5)^2', 'x^2+10x+25'),
                     ('9d', '(x-3)^2', 'x^2-6x+9'), ('9e', '(x+2)(x-6)', 'x^2-4x-12'),
                     ('10a', 'x^2+9x', 'x(x+9)'), ('10b', 'x^2-4x', 'x(x-4)'), ('10c', '3x^2+12x', 'x(3x+12)'),
                     ('10d', 'x^2-x', 'x(x-1)'),
                     ('11a', '3+x^2+2x', 'x^2+2x+3'), ('11b', '5x-1+x^2', 'x^2+5x-1'),
                     ('11c', 'x^2+4x-3x+7', 'x^2+x+7'), ('11d', '6-2x+x^2-9', 'x^2-2x-3'),
                     ('11e', '2x^2-6+x-x^2', 'x^2+x-6'), ('11f', 'x^2+2x-(3x+4)', 'x^2-x-4')]:
        c(nr, ausm(e), ausm(b))

elif teil == 'e1':
    for nr, eq, b in [('12a', '3x+4=10', 'linear'), ('12b', 'x^2=50', 'quadratisch'),
                      ('12c', '(x-1)^2=9', 'quadratisch'), ('12d', '2(x+3)=8', 'linear'),
                      ('12e', '5x=x^2', 'quadratisch')]:
        c(nr, 'quadratisch' if grad(eq) == 2 else 'linear', b)
    for nr, eq, b in [('13a', 'x^2=16', 2), ('13b', 'x^2=-9', 0), ('13c', 'x^2=2', 2), ('13d', '5x^2=0', 1),
                      ('13e', 'x^2=-0.5', 0)]:
        c(nr, anzahl(eq), b)
    for nr, eq, b in [('14a', 'x^2=25', [5, -5]), ('14b', 'x^2=81', [9, -9]), ('14c', 'x^2=4', [2, -2]),
                      ('14d', 'x^2=144', [12, -12]), ('14e', 'x^2=11', [3.32, -3.32]), ('14f', 'x^2=-16', []),
                      ('15a', 'x^2+3=19', [4, -4]), ('15b', 'x^2-20=5', [5, -5]), ('15c', '5x^2=45', [3, -3]),
                      ('15d', '3x^2+5=32', [3, -3]), ('15e', '4x^2-9=-9', [0]), ('15f', '2x^2+11=3', []),
                      ('15g', '3x^2-4=17', [2.65, -2.65]),
                      ('16a', '(x-2)^2=9', [5, -1]), ('16b', '(x-1)^2=16', [5, -3]), ('16c', '(x-5)^2=4', [7, 3]),
                      ('16d', '(x-3)^2=25', [8, -2]), ('16e', '(x+3)^2=49', [4, -10]), ('16f', '(x+6)^2=0', [-6]),
                      ('16g', '(x-2)^2=5', [4.24, -0.24])]:
        c(nr, loes(eq), b)
    for nr, eq, xv, b in [('17a', 'x^2-16=0', 4, '(wA)'), ('17b', 'x^2+16=0', -4, '(fA)'),
                          ('17c', '(x-3)^2=36', -3, '(wA)'), ('17d', '(x+5)^2=4', 3, '(fA)'),
                          ('17e', '2x^2+1=9', -2, '(wA)'), ('17f', '(x-1)^2=-4', -1, '(fA)')]:
        c(nr, WA(probe(eq, xv)), b)
    for nr, eq, b in [('18a', '(x-1)^2-2=2', 2), ('18b', '(x-1)^2-2=-2', 1), ('18c', '(x-1)^2-2=-3', 0),
                      ('18d', '(x-1)^2-2=0', 2)]:
        c(nr, anzahl(eq), b)
    c('18e', loes('(x-1)^2-2=2'), [-1, 3])
    for nr, eq in [('19a', 'x^2=-1'), ('19b', '(x-1)^2=-4'), ('19c', '2x^2+5=1')]:
        c(nr + ' (Beispiel)', anzahl(eq), 0)
    c('20a', 'wahr' if anzahl('(x-5)^2=0') == 1 else 'falsch', 'wahr')
    c('20b', 'wahr' if loes('(x+6)^2=16') == [2, 10] else 'falsch', 'falsch')
    c('20b Lösungen', loes('(x+6)^2=16'), [-10, -2])
    c('20c (Beispiel)', anzahl('(x+6)^2=-1'), 0)
    c('21a', loes('2x^2=162'), [9, -9])
    c('21b', loes('(x+2)^2=49'), [5, -9])
    c('21c', loes('x^2+21=12'), [])
    c('22a', anzahl('x^2=20'), 2)
    c('22b', anzahl('x^2=-20'), 0)
    c('22c', loes('(x-4)^2=0'), [4])
    c('23a', float(N(sqrt(64))), 8)
    c('23b', float(N(sqrt(300000 / (pi * 90)))), 32.6, tol=0.051)

elif teil == 'e2':
    for nr, eq, b in [('24a', '(x-2)(x-9)=0', 'ja'), ('24b', 'x(x+4)=12', 'nein'), ('24c', '(x+1)(x-6)=0', 'ja'),
                      ('24d', '(x-3)(x+3)=7', 'nein'), ('24e', 'x(x+4)-12=0', 'nein'), ('24f', 'x(x-5)=0', 'ja')]:
        c(nr, 'ja' if produkt_null(eq) else 'nein', b)
    for nr, eq, b in [('25a', '(x-2)(x-5)=0', [2, 5]), ('25b', '(x-1)(x-4)=0', [1, 4]),
                      ('25c', '(x-6)(x-3)=0', [6, 3]), ('25d', '(x-7)(x-2)=0', [7, 2]),
                      ('25e', '(x+4)(x-1)=0', [-4, 1]), ('25f', 'x(x+6)=0', [0, -6]), ('25g', '(x-3)(x-3)=0', [3])]:
        c(nr, loes(eq), b)
    for nr, eq, xv, b in [('26a', '(x-3)(x+8)=0', 3, '(wA)'), ('26b', '(x-2)(x+5)=0', -2, '(fA)'),
                          ('26c', 'x(x+9)=-14', -7, '(wA)'), ('26d', 'x(x-3)=-4', -1, '(fA)'),
                          ('26e', '(x+2)(x+3)=12', -6, '(wA)')]:
        c(nr, WA(probe(eq, xv)), b)
    c('26f', [v for v in [2, 5, -2, -10] if probe('x(x+7)=-10', v)], [-2])
    for nr, eq, b in [('27a', 'x^2+4x=0', [0, -4]), ('27b', 'x^2+5x=0', [0, -5]), ('27c', 'x^2+2x=0', [0, -2]),
                      ('27d', 'x^2-6x=0', [0, 6]), ('27e', '5x^2-15x=0', [0, 3])]:
        c(nr, loes(eq), b)
    for nr, eq, b in [('28a', 'x(x+3)=10', 'x^2+3x-10'), ('28b', 'x(x-4)=-3', 'x^2-4x+3'),
                      ('28c', '(x+1)(x-2)=4', 'x^2-x-6')]:
        c(nr, normal(eq), ausm(b))
    for nr, prod, summe, b in [('29a', '(x+2)(x+3)', 'x^2+5x+6', [-2, -3]), ('29b', '(x-4)(x+2)', 'x^2-2x-8', [4, -2]),
                               ('29c', '4(x-3)(x+2)', '4x^2-4x-24', [3, -2])]:
        c(nr + ' Produktform', ausm(prod), ausm(summe))
        c(nr, loes(summe + '=0'), b)
    c('30a', loes('x^2=6x'), [0, 6])
    c('30b', loes('(x+5)(x-2)=0'), [-5, 2])
    c('30c Normalform', normal('x(x+1)=12'), ausm('x^2+x-12'))
    c('30c', loes('x(x+1)=12'), [3, -4])
    c('31b', loes('x^2=3x'), [0, 3])

elif teil == 'e3':
    for nr, eq, b in [('32a', '3x^2=27', 'Wurzel'), ('32b', '(x-4)(x+1)=0', 'Nullprodukt'),
                      ('32c', '(x+2)^2=11', 'rückwärts'), ('32d', 'x^2+5x-14=0', 'Formel'),
                      ('32e', 'x^2-7x+6=0', 'Formel')]:
        c(nr, weg(eq), b)
    for nr, eq, b in [('33a', 'x^2+9x+4=0', (9, 4)), ('33b', 'x^2-5x+2=0', (-5, 2)), ('33c', 'x^2+2x-8=0', (2, -8)),
                      ('33d', 'x^2-x-20=0', (-1, -20)), ('33e', 'x^2-7x=0', (-7, 0))]:
        c(nr, pq(eq), b)
    for nr, eq, b in [('34a', 'x^2+4x-5=0', 'nein'), ('34b', '2x^2-6x+4=0', '2'), ('34c', '-x^2+3x+10=0', '-1'),
                      ('34d', '5x^2+10x-15=0', '5'), ('34e', 'x^2-3x=0', 'nein')]:
        l, r = eq.split('=')
        a = Poly(expand(P(l) - P(r)), x).LC()
        c(nr, 'nein' if a == 1 else str(a), b)
    for nr, eq, b in [('35a', 'x^2+6x+8=0', [-2, -4]), ('35b', 'x^2+10x+21=0', [-3, -7]),
                      ('35c', 'x^2+12x+20=0', [-2, -10]), ('35d', 'x^2+6x+5=0', [-1, -5]),
                      ('35e', 'x^2-2x-8=0', [4, -2])]:
        c(nr, loes(eq), b)
    for nr, eq, nf, b in [('36a', 'x^2+5=6x', 'x^2-6x+5', [1, 5]), ('36b', 'x^2=2x+3', 'x^2-2x-3', [3, -1]),
                          ('36c', '2x^2+4x-16=0', 'x^2+2x-8', [2, -4]), ('36d', '-x^2+6x-8=0', 'x^2-6x+8', [2, 4]),
                          ('36e', '2x^2+2x-12=0', 'x^2+x-6', [2, -3])]:
        c(nr + ' Normalform', normiert(eq), ausm(nf))
        c(nr, loes(eq), b)
    c('37a', loes('x^2-6x+9=0'), [3])
    c('37b', loes('x^2-2x+5=0'), [])
    for nr, eq, d, n in [('37c', 'x^2-3x+2=0', 0.25, 2), ('37d', 'x^2+5x+7=0', -0.75, 0),
                         ('37e', 'x^2-7x+12.25=0', 0, 1)]:
        c(nr + ' Diskriminante', disk(eq), d)
        c(nr + ' Anzahl', anzahl(eq), n)
    for nr, eq, b in [('38a', 'x^2-4x+1=0', [3.73, 0.27]), ('38b', 'x^2+x-1=0', [0.62, -1.62]),
                      ('38c', '3x^2-6x-3=0', [2.41, -0.41]),
                      ('39a', 'x^2-2x-24=0', [6, -4]), ('39b', '3x^2-12x-15=0', [5, -1]),
                      ('40a', 'x(x+3)=18', [3, -6]), ('40b', '(x+1)^2=3x+7', [3, -2]),
                      ('40c', '(x-2)(x+4)=3x+4', [4, -3]),
                      ('41a', '4x^2=100', [5, -5]), ('41b', 'x^2+7x=0', [0, -7]), ('41c', '(x-4)^2=1', [5, 3]),
                      ('41d', 'x^2-3x-4=0', [4, -1]), ('41e', '-x^2+4x+9=-3', [6, -2]),
                      ('42a', '3x^2+6x-9=0', [1, -3]), ('42b', 'x^2-8x+12=0', [6, 2]),
                      ('42c', 'x^2-10x+16=0', [8, 2]), ('43b', '2x^2-10x+12=0', [3, 2])]:
        c(nr, loes(eq), b)
    c('38a exakt', [float(N(2 + sqrt(3))), float(N(2 - sqrt(3)))], [3.7320508, 0.2679492])
    c('39a Probe', val('6^2-2*6-24'), 0)
    c('39b Probe', val('3*(-1)^2-12*(-1)-15'), 0)
    c('40a Normalform', normal('x(x+3)=18'), ausm('x^2+3x-18'))
    c('40b Normalform', normal('(x+1)^2=3x+7'), ausm('x^2-x-6'))
    c('40c Normalform', normal('(x-2)(x+4)=3x+4'), ausm('x^2-x-12'))
    c('41e Normalform', normiert('-x^2+4x+9=-3'), ausm('x^2-4x-12'))
    c('42a Normalform', normiert('3x^2+6x-9=0'), ausm('x^2+2x-3'))
    s = loes('x^2-2=-2x+1')
    c('44a', [(v, val('-2x+1', v)) for v in s], [(-3, 7), (1, -1)])
    c('44a Kontrolle f', [val('x^2-2', v) for v in s], [7, -1])
    s = loes('(x-1)^2-4=3x+3')
    c('44c', [(v, val('3x+3', v)) for v in s], [(-1, 0), (6, 21)])
    c('44c Kontrolle f', [val('(x-1)^2-4', v) for v in s], [0, 21])
    c('44c Normalform', normal('(x-1)^2-4=3x+3'), ausm('x^2-5x-6'))

elif teil == 'e4':
    def passt(lsg, art):
        return 'beide' if art == 'Zahl' else ('x1' if lsg[0] >= 0 else 'x2')
    for nr, lsg, art, b in [('45a', (6, -6), 'Länge', 'x1'), ('45b', (-12, 4), 'Länge', 'x2'),
                            ('45c', (9, -14), 'Anzahl', 'x1'), ('45d', (12, -12), 'Zahl', 'beide'),
                            ('45e', (-3, 11), 'Alter', 'x2')]:
        c(nr, passt(lsg, art), b)
    for nr, eq, b in [('46a', 'x^2=100', [10, -10]), ('46b', 'x^2=121', [11, -11]), ('46c', '2x^2=72', [6, -6]),
                      ('46d', 'x^2-10=71', [9, -9]), ('46e', 'x^2+20=84', [8, -8]), ('46f', 'x(x+1)=56', [7, -8]),
                      ('47b', 'x(x+3)=40', [5, -8]), ('47f', '(x+2)(x+6)=96', [6, -14]),
                      ('48a', 'x(x+2)=48', [6, -8]), ('48b falsch', '2x+2(x+5)=24', [3.5]),
                      ('48b richtig', 'x(x+5)=24', [3, -8])]:
        c(nr, loes(eq), b)
    c('46f Nachfolger', [(v, v + 1) for v in loes('x(x+1)=56')], [(-8, -7), (7, 8)])
    c('47b Normalform', normal('x(x+3)=40'), ausm('x^2+3x-40'))
    c('47d Länge', 5 + 3, 8)
    c('47e Probe', 5 * 8, 40)
    c('47f Normalform', normal('(x+2)(x+6)=96'), ausm('x^2+8x-84'))
    c('47f Länge', 6 + 4, 10)
    c('47f Probe', (6 + 2) * (10 + 2), 96)
    c('48b Länge', 3 + 5, 8)

# Sperrliste (2.1): ganze Gleichungen und Terme aus Kasten, Beispielen, Typischen Fehlern, Originalen
SPERRE = ['x^2=36', 'x^2=0', 'x^2=-36', '(x+4)^2=36', '(x+4)^2=0', 'x^2-7x=0', 'x*(x-7)=0',
          '(x+3)*(x-9)=0', 'x*(x+8)=20', 'x^2+8x-20=0', '3x^2+24x-60=0', 'x^2+8x+16=0', 'x^2+8x+20=0',
          '(x+7)^2=0', '(x+8)^2=16', 'x^2+1=0', 'x*(x+5)=-6', '2x^2+8x+6=0', 'x^2+4x+3=0', 'x^2-6x+7=0',
          '-x^2-2x+5=-10', 'x^2+2x-15=0', 'x^2-x-2=0', '(x-2)^2-4=-2x+3', 'x^2=9', 'x^2=49', 'x^2=-25',
          'x^2=7x', 'x^2+2x-1=3x+1', 'x^2+8x=20', 'x+5=12', '-x=5', '5x=15', 'x+17=12', '(x+13)^2',
          '(x-5)^2-11', 'x^2-12x+5', '(-11)^2', '1,5^2', '(-5)*(-5+17)', 'x*(x+5)', '(x+3)^2=x^2+9',
          'x^2-5+12x+17']


def norm(t):
    t = re.sub(r'%.*', '', t)
    for a, b in [('\\cdot', '*'), ('·', '*'), ('−', '-'), ('\\left', ''), ('\\right', ''), ('\\,', ''),
                 ('{,}', ','), ('$', ''), ('{', ''), ('}', ''), (' ', ''), ('\n', '')]:
        t = t.replace(a, b)
    return t


try:
    quelle = norm(io.open(teil + '_a.tex', encoding='utf-8').read())
    treffer = []
    for s in SPERRE:
        pat = (r'(?<![0-9a-z)^.,])' if s[0] in 'x-' else '') + re.escape(s) + r'(?![0-9,.])'
        if re.search(pat, quelle):
            treffer.append(s)
    for t in treffer:
        abw += 1
        zeilen.append('Sperrliste\t%s\t%s_a.tex\tABWEICHUNG' % (t, teil))
    zeilen.append('Sperrliste\t%d Einträge geprüft\t%d Treffer\t%s' % (len(SPERRE), len(treffer),
                                                                       'OK' if not treffer else 'ABWEICHUNG'))
except IOError:
    zeilen.append('Sperrliste\t%s_a.tex fehlt\t-\tABWEICHUNG' % teil)
    abw += 1

zeilen.append('Abweichungen: %d' % abw)
text = 'Nummer\tSkriptwert\tBlattwert\tErgebnis\n' + '\n'.join(zeilen) + '\n'
io.open('pruef_out_%s.txt' % teil, 'w', encoding='utf-8').write(text)
print(text)
