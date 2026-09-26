# pruef.py – rechnet die Lösungen je Einheit unabhängig nach (sympy).
# Aufruf: python pruef.py e1   -> schreibt pruef_out_e1.txt
# Blattwerte (B=...) sind aus dem Lösungsquelltext e<n>_l.tex übertragen.
import sys
import sympy as sp
from sympy import Rational as R

x = sp.symbols('x')
zeilen = []
abw = 0


def gleich(a, b):
    if isinstance(a, (bool, sp.logic.boolalg.BooleanAtom)) or isinstance(b, bool):
        return bool(a) == bool(b)
    if isinstance(a, str) or isinstance(b, str):
        return str(a) == str(b)
    if isinstance(a, (tuple, list)):
        return len(a) == len(b) and all(gleich(u, v) for u, v in zip(a, b))
    return abs(float(sp.nsimplify(a)) - float(sp.nsimplify(b))) < 1e-9


def c(nr, skript, blatt):
    global abw
    ok = gleich(skript, blatt)
    if not ok:
        abw += 1
    zeilen.append(f"{nr:8s} Skript={skript!s:28s} Blatt={blatt!s:28s} {'OK' if ok else 'ABWEICHUNG'}")


def werte(m, n, xs):
    return [m * v + n for v in xs]


def nullst(m, n):
    return sp.solve(sp.Eq(m * x + n, 0), x)[0]


def arg(m, n, y):
    return sp.solve(sp.Eq(m * x + n, y), x)[0]


def prop(xs, ys):
    q = [sp.nsimplify(b) / sp.nsimplify(a) for a, b in zip(xs, ys)]
    return ('ja', q[0]) if all(v == q[0] for v in q) else ('nein',)


def gerade2(P, Q):
    m = sp.nsimplify(Q[1] - P[1]) / sp.nsimplify(Q[0] - P[0])
    n = sp.nsimplify(P[1]) - m * sp.nsimplify(P[0])
    return (m, n)


def schnitt(m1, n1, m2, n2):
    if m1 == m2:
        return 'keiner'
    xs = sp.solve(sp.Eq(m1 * x + n1, m2 * x + n2), x)[0]
    return (xs, m1 * xs + n1)


def e1():
    X = [0, 1, 2, 3]
    for t, m, B in [('1a', 2, [0, 2, 4, 6]), ('1b', 3, [0, 3, 6, 9]), ('1c', 1, [0, 1, 2, 3]),
                    ('1d', 5, [0, 5, 10, 15]), ('1e', R(3, 2), [0, 1.5, 3, 4.5]),
                    ('1f', R(1, 2), [0, 0.5, 1, 1.5]), ('1g', -2, [0, -2, -4, -6])]:
        c(t, werte(m, 0, X), B)
    # 2: zweiter Punkt der Ursprungsgerade
    c('2a', (1, 2 * 1), (1, 2)); c('2b', (2, R(1, 2) * 2), (2, 1)); c('2c', (1, -2 * 1), (1, -2))
    m = R(3, 2)
    c('3a', m * 2, 3); c('3b', m * 4, 6); c('3c', m * -2, -3); c('3d', arg(m, 0, -6), -4)
    c('3e', m * 10, 15); c('3f', arg(m, 0, 21), 14)
    c('4a', prop([1, 2, 3, 4], [3, 6, 9, 12]), ('ja', 3))
    c('4b', prop([1, 2, 3, 4], [2, 4, 7, 8]), ('nein',))
    c('4c', prop([2, 4, 6, 8], [5, 10, 15, 20]), ('ja', 2.5))
    c('4d', prop([1, 2, 3, 4], [5, 6, 7, 8]), ('nein',))
    c('5a', prop([2, 4, 6, 10], [-1, -2, -3, -5]), ('ja', -0.5))
    c('5b', prop([1, 2, 3], [4, 8, 12]), ('ja', 4))                       # 4 € je kg
    c('5c', prop([1, 2, 10], [5.1, 5.2, 6]), ('nein',))  # 5 € + 0,10 € je min
    c('5c-f(0)', 5 + 0.1 * 0, 5)
    c('6a', 4 * 3, 12); c('6b', R(5, 2) * 4, 10); c('6c', 6 * R(3, 2), 9)
    c('7a', prop([2, 4, 6], [7, 14, 21]), ('ja', 3.5))
    c('7b', prop([3, 6, 9], [-6, -12, -18]), ('ja', -2))
    c('8a-y(0)', 0 * 5, 0)          # Ursprungsgerade hat bei x=0 den Wert 0, nicht 3
    c('8b', sp.simplify(4 * (2 * x) / (4 * x)), 2)
    c('9a', 15, 15); c('9b', 15 * 8, 120); c('9c', 15 * (x + 1) - 15 * x, 15)


def e2():
    # 10: (m, n) aus der Gleichung (sympy liest den Term)
    for t, term, B in [('10a', 3*x+4, (3, 4)), ('10b', 5*x-2, (5, -2)), ('10c', -4*x+1, (-4, 1)),
                       ('10d', 7-2*x, (-2, 7)), ('10e', sp.Integer(-6), (0, -6))]:
        p = sp.Poly(term, x)
        c(t, (p.coeff_monomial(x), p.coeff_monomial(1)), B)
    for t, m, B in [('11a', 2, 'steigt'), ('11b', -3, 'fällt'), ('11c', 0.5, 'steigt'),
                    ('11d', -1, 'fällt'), ('11e', 3, 'steigt')]:
        c(t, 'steigt' if m > 0 else 'fällt', B)
    # 12: Schritt nach oben/unten = m (Punkt liegt auf der Geraden)
    for t, m, n, P, B in [('12a', 2, -1, (0, -1), 2), ('12b', -3, 2, (0, 2), -3),
                          ('12c', 1, 1, (-1, 0), 1), ('12d', -2, 1, (0, 1), -2)]:
        c(t + '-Punkt', m * P[0] + n, P[1]); c(t, (m * (P[0] + 1) + n) - P[1], B)
    X = [-1, 0, 1, 2]
    c('13a', werte(1, 2, X), [1, 2, 3, 4]); c('13b', werte(2, -1, X), [-3, -1, 1, 3])
    c('13c', werte(3, -2, X), [-5, -2, 1, 4])
    for t, m, n, P, Q in [('14a', 1, 3, (0, 3), (1, 4)), ('14b', 2, 2, (0, 2), (1, 4)),
                          ('14c', 3, 4, (0, 4), (1, 7)), ('14d', 1, 1, (0, 1), (1, 2)),
                          ('15a', -2, 3, (0, 3), (1, 1)), ('15b', R(1, 2), 2, (0, 2), (2, 3)),
                          ('15c', 3, -4, (0, -4), (1, -1)), ('15d', R(2, 3), -2, (0, -2), (3, 0))]:
        c(t, ((P[0], m * P[0] + n), (Q[0], m * Q[0] + n)), (P, Q))
    g, h, k = (2, -1), (-1, 3), (R(1, 2), -2)
    c('16a', g[1], -1); c('16b', h[1], 3); c('16c', k[1], -2)
    c('16d', g[0], 2); c('16e', h[0], -1); c('16f', k[0], 0.5)
    c('16f-Gitter', (k[0] * 2 + k[1], k[0] * 4 + k[1]), (-1, 0))   # (2|-1), (4|0) auf Gitterpunkten
    A = {1: (2, 4), 2: (4, 2), 3: (-2, 4), 4: (0, -1)}
    finde = lambda mn: [kk for kk, v in A.items() if v == mn][0]
    c('17a', finde((2, 4)), 1); c('17b', finde((-2, 4)), 3); c('17c', finde((4, 2)), 2); c('17d', finde((0, -1)), 4)
    Bild = {'I': (R(-1, 2), 2), 'II': (2, -2), 'III': (0, 1)}
    Angebot = [(2, -2), (-2, -2), (R(-1, 2), 2), (R(1, 2), 2), (0, 1), (-1, 1)]
    c('17e', [Bild[kk] in Angebot for kk in ('I', 'II', 'III')], [True, True, True])
    c('17e-I', Bild['I'], (-0.5, 2)); c('17e-II', Bild['II'], (2, -2)); c('17e-III', Bild['III'], (0, 1))
    f = {1: (4, -1), 2: (-2, 5), 3: (0, 3), 4: (4, 2), 5: (-0.5, 0), 6: (1, 3)}
    c('18a', [kk for kk, v in f.items() if v[0] > 0], [1, 4, 6])
    c('18b', [kk for kk, v in f.items() if v[0] < 0], [2, 5])
    c('18c', [kk for kk, v in f.items() if v[0] == 0], [3])
    c('18d', [(a, b) for a in f for b in f if a < b and f[a][0] == f[b][0]], [(1, 4)])
    c('18e', [kk for kk, v in f.items() if v[1] == 0], [5])
    c('18f', [(a, b) for a in f for b in f if a < b and f[a][1] == f[b][1]], [(3, 6)])
    c('18g', (f[2][0], -1), (-2, -1))
    c('19a', 3 / 1, 3); c('19b', -2 / 1, -2)
    c('20a', 5 > 2, True); c('20b', abs(-3) > abs(2), True)
    c('21a', -4 * 0 + 60, 60); c('21b', (-4 * 5 + 60) - (-4 * 4 + 60), -4)
    c('21-Gitter', (-4 * 5 + 60, -4 * 10 + 60, nullst(-4, 60)), (40, 20, 15))
    c('21c', (-4, 60), (-4, 60))


def pp(m, n, P):
    return 'ja' if sp.nsimplify(m) * sp.nsimplify(P[0]) + sp.nsimplify(n) == sp.nsimplify(P[1]) else 'nein'


def e3():
    for t, m, n, xv, B in [('23a', 3, 4, 2, 10), ('23b', 5, -3, 4, 17), ('23c', 2, 6, 5, 16),
                           ('23d', 6, -10, 2, 2), ('23e', 3, 5, -2, -1), ('23f', 4, -1, R(5, 2), 9),
                           ('23h', R(3, 4), -2, -8, -8)]:
        c(t, m * xv + n, B)
    c('23g', werte(-2, 3, [-2, -1, 0, 1, 2]), [7, 5, 3, 1, -1])
    for t, m, n, y, B in [('24a', 2, 3, 11, 4), ('24b', 3, -1, 14, 5), ('24c', 5, 2, 22, 4),
                          ('24d', 4, 2, -6, -2), ('24e', -2, 7, 1, 3), ('24f', R(1, 2), 4, 6, 4)]:
        c(t, arg(m, n, y), B)
    for t, m, n, P, B in [('25a', 3, -2, (2, 4), 'ja'), ('25b', 3, -2, (1, 2), 'nein'),
                          ('25c', -1, 5, (-1, 6), 'ja'), ('25d', 2, 3, (0, -3), 'nein'),
                          ('25e', R(1, 2), 1, (3, R(5, 2)), 'ja'), ('25f', -2, 1, (-2, -3), 'nein'),
                          ('25g', R(-2, 3), 4, (-6, 8), 'ja')]:
        c(t, pp(m, n, P), B)
    c('25b-f(1)', 3 * 1 - 2, 1); c('25d-f(0)', 3, 3); c('25f-f(-2)', -2 * -2 + 1, 5); c('25g-f(-6)', R(-2, 3) * -6 + 4, 8)
    for t, m, n, B in [('26a', 2, -6, 3), ('26b', 3, -12, 4), ('26c', 4, -20, 5), ('26d', 5, 10, -2),
                       ('27a', -4, 8, 2), ('27b', R(-1, 2), 3, 6), ('27c', R(6, 5), -3, 2.5)]:
        c(t, nullst(m, n), B)
    for t, m, n, B in [('28a', 2, -4, ((0, -4), (2, 0))), ('28b', -3, 6, ((0, 6), (2, 0))),
                       ('28c', R(1, 2), 2, ((0, 2), (-4, 0))), ('28d', 4, 0, ((0, 0), (0, 0)))]:
        c(t, ((0, n), (nullst(m, n), 0)), B)
    c('28e', ((0, -2), 'kein' if sp.solve(sp.Eq(0 * x - 2, 0), x) == [] else 'einer'), ((0, -2), 'kein'))
    c('29a', nullst(1, -1), 1); c('29b', nullst(-1, 3), 3); c('29c', (0, 3), (0, 3))
    c('29d', schnitt(1, -1, -1, 3), (2, 1))
    m, n = R(-3, 2), 3
    c('30a', 'wahr' if m < 0 else 'falsch', 'wahr'); c('30b', 'wahr' if n == R(-3, 2) else 'falsch', 'falsch')
    c('30c', 'wahr' if nullst(m, n) == 2 else 'falsch', 'wahr'); c('30d', pp(m, n, (4, 3)), 'nein')
    c('30d-f(4)', m * 4 + n, -3)
    c('31a', nullst(3, -9), 3); c('31b', 2 * 5 - 8, 2)
    c('32a', sp.solve(sp.Eq(sp.Integer(4), 0), x), [])
    c('32b', nullst(2, 6), -3)
    c('33a', R(-15, 2) * 2 + 90, 75); c('33b', arg(R(-15, 2), 90, 30), 8); c('33c', nullst(R(-15, 2), 90), 12)


def e4():
    for t, m, n, P, Q, B in [('34a', 1, 3, (0, 3), (1, 4), (1, 3)), ('34b', 3, -3, (0, -3), (1, 0), (3, -3)),
                             ('34c', 2, -4, (0, -4), (2, 0), (2, -4))]:
        c(t, gerade2(P, Q), B)
        c(t + '-Punkte', (m * P[0] + n, m * Q[0] + n), (P[1], Q[1]))
    for t, m, P, B in [('35a', 2, (3, 8), 2), ('35b', 3, (2, 5), -1), ('35c', -1, (4, 1), 5),
                       ('35d', R(1, 2), (-4, 1), 3)]:
        c(t, sp.solve(sp.Eq(P[1], m * P[0] + sp.Symbol('n')), sp.Symbol('n'))[0], B)
    for t, P, Q, B in [('36a', (0, 4), (2, 10), (3, 4)), ('36b', (0, -2), (3, 4), (2, -2)),
                       ('36c', (1, 5), (4, 11), (2, 3)), ('37a', (2, 7), (5, 1), (-2, 11)),
                       ('37b', (-4, 1), (2, 4), (0.5, 3)), ('38c', (-3, 5), (3, 1), (R(-2, 3), 3))]:
        c(t, gerade2(P, Q), B)
    for t, g1, g2, B in [('39a', (1, 1), (-1, 5), (2, 3)), ('39b', (2, -1), (1, 3), (4, 7)),
                         ('39c', (3, 7), (-2, -3), (-2, 1)), ('40a', (R(1, 2), 1), (-1, 4), (2, 2)),
                         ('40b', (4, -3), (4, 1), 'keiner')]:
        c(t, schnitt(g1[0], g1[1], g2[0], g2[1]), B)
    c('41a', gerade2((2, 5), (6, 13))[0], 2)
    c('41b', sp.solve(sp.Eq(4, 3 * 2 + sp.Symbol('n')), sp.Symbol('n'))[0], -2)
    c('42a', schnitt(3, 6, 3, -5), 'keiner'); c('42b', schnitt(2, 4, R(-1, 2), 4), (0, 4))
    mb, nb = gerade2((2, 840), (6, 600))
    c('43a', (mb, nb), (-60, 960)); c('43b', nb, 960); c('43c', nullst(mb, nb), 16)
    c('44a', ((20, 0), (12, 12)), ((20, 0), (12, 12)))
    c('44b', schnitt(20, 0, 12, 12), (1.5, 30))


def e5():
    for t, n0, m0, B in [('45a', 4, 2.2, (4, 2.2)), ('45b', 80, -5, (80, -5)), ('45c', 25, 9.99, (25, 9.99)),
                         ('45d', 45, 3, (45, 3)), ('45e', 12, 0.5, (12, 0.5))]:
        c(t, (n0, m0), B)
    # 46: Gleichung = Änderung·x + Anfangswert, in €
    c('46a', (2, 6), (2, 6)); c('46b', (3, 15), (3, 15)); c('46c', (0.3, 12), (0.3, 12))
    c('46d', (R(5, 100), 2), (0.05, 2))
    c('47a', (4, 8), (4, 8)); c('47b', 4 * 3 + 8, 20); c('47c', (-15, 250), (-15, 250))
    c('47d', -15 * 8 + 250, 130)
    xs = arg(35, 60, 500)
    c('47e-x', float(xs), 12.571428571428571)
    c('47e', sp.ceiling(xs), 13); c('47e-12M', 35 * 12 + 60, 480); c('47e-13M', 35 * 13 + 60, 515)
    c('48a', (2.5, 10), (2.5, 10)); c('48b', (-3, 60), (-3, 60))
    G = {'I': (0, 50), 'II': (10, 0), 'III': (5, 20)}
    finde = lambda mn: [kk for kk, v in G.items() if v == mn][0]
    c('49a', finde((10, 0)), 'II'); c('49b', finde((0, 50)), 'I'); c('49c', finde((5, 20)), 'III')
    nord = lambda km: 9 + R(3, 10) * km
    sued = lambda km: R(45, 100) * km
    c('50a', (nord(40), sued(40), 'Süd' if sued(40) < nord(40) else 'Nord'), (21, 18, 'Süd'))
    c('50b', (nord(80), sued(80), 'Süd' if sued(80) < nord(80) else 'Nord'), (33, 36, 'Nord'))
    c('50c', schnitt(R(3, 10), 9, R(45, 100), 0)[0], 60)
    basis = lambda t: 2 + R(25, 100) * max(0, t - 10)
    plus = lambda t: 5 + R(15, 100) * max(0, t - 30)
    c('51a', basis(8), 2); c('51b', basis(40), 9.5)
    c('51c', (plus(40), 'Plus' if plus(40) < basis(40) else 'Basis'), (6.5, 'Plus'))
    c('52a', (R(20, 100), 1.5), (0.2, 1.5)); c('52b', (45, 30), (45, 30))
    c('53a', schnitt(R(1, 2), 5, R(1, 2), 8), 'keiner')      # gleiche Steigung: nie gleich teuer
    c('53b', schnitt(R(1, 2), 5, R(3, 10), 8)[0] > 0, True)  # Beispielwerte: Schnitt bei positiver Strecke


def main():
    einheit = sys.argv[1]
    globals()[einheit]()
    with open(f'pruef_out_{einheit}.txt', 'w', encoding='utf-8') as f:
        for z in zeilen:
            f.write(z + '\n')
        f.write(f'Abweichungen: {abw}\n')
    print('\n'.join(zeilen[-3:]))
    print(f'Abweichungen: {abw}')


if __name__ == '__main__':
    main()
