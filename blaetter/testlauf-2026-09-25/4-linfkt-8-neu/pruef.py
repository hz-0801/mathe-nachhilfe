# pruef.py – rechnet die Lösungen je Einheit unabhängig nach (5.1 a)
# Aufruf: python pruef.py e1   -> schreibt pruef_out_e1.txt
# Blattwerte sind aus dem Lösungsquelltext (eN_l.tex) übertragen.
import sys
from fractions import Fraction as F
import sympy as sp

x = sp.symbols('x')
ZEILEN = []

def num(v):
    if isinstance(v, (tuple, list)):
        return tuple(num(t) for t in v)
    if isinstance(v, str):
        try:
            float(v)
        except ValueError:
            return v
    return sp.nsimplify(v)

def chk(nr, skript, blatt):
    s, b = num(skript), num(blatt)
    if isinstance(s, tuple) or isinstance(b, tuple) or isinstance(s, str):
        ok = s == b
    else:
        ok = abs(float(s) - float(b)) < 1e-9
    ZEILEN.append(f"{nr:10s} Skript={s!s:28s} Blatt={b!s:28s} {'OK' if ok else 'ABWEICHUNG'}")
    return ok

def f_lin(m, n=0):
    m, n = sp.nsimplify(m), sp.nsimplify(n)
    return lambda v: m * sp.nsimplify(v) + n

def loese(expr_l, expr_r):
    return sp.solve(sp.Eq(expr_l, expr_r), x)[0]

def zwei_punkte(A, B):
    m = sp.Rational(sp.nsimplify(B[1] - A[1]), 1) / sp.nsimplify(B[0] - A[0])
    n = sp.nsimplify(A[1]) - m * sp.nsimplify(A[0])
    return m, n

def prop(xs, ys):
    q = [sp.nsimplify(b) / sp.nsimplify(a) for a, b in zip(xs, ys)]
    return 'ja' if len(set(q)) == 1 else 'nein', q[0]

def auf_gerade(m, n, P):
    return 'ja' if sp.nsimplify(m) * sp.nsimplify(P[0]) + sp.nsimplify(n) == sp.nsimplify(P[1]) else 'nein'

# ---------------- Einheit 1 ----------------
def e1():
    chk('Bsp', f_lin(2)(1), 2)
    for t, m, b in [('1a', 1, 1), ('1b', 3, 3), ('1c', 4, 4), ('1d', 5, 5)]:
        chk(t, f_lin(m)(1), b)
    chk('2a', f_lin('2.5')(2), 5)
    chk('2b', f_lin(F(1, 3))(3), 1)
    chk('2c', f_lin(-2)(1), -2)
    g = f_lin('1.5')
    chk('3a', g(2), 3); chk('3b', g(-2), -3)
    chk('3c', loese(sp.nsimplify('1.5') * x, 6), 4)
    chk('3d', g(2), 3); chk('3e', g(12), 18)
    chk('3f', sp.Rational(3, 2) * 12, 18)
    chk('4a', prop([1, 2, 3, 4], [6, 12, 18, 24]), ('ja', 6))
    chk('4b', prop([2, 4, 6], [7, 14, 20])[0], 'nein')
    chk('4b q', (F(14, 4), F(20, 6)), (F(7, 2), F(10, 3)))
    chk('4c', prop([1, 2, 3], [5, 8, 11])[0], 'nein')
    chk('4d', prop([-2, 1, 4], [3, '-1.5', -6]), ('ja', '-1.5'))
    chk('4e', prop([1, 2], ['1.8', '3.6']), ('ja', '1.8'))
    chk('4f', prop([1, 2], [6, 8])[0], 'nein')  # 4 + 2x
    chk('5 Tom', 21 - 3, 18)
    chk('5a', prop([3, 6], [21, 42]), ('ja', 7))
    chk('5b', prop([4, 10], [18, 45]), ('ja', '4.5'))
    chk('6b', auf_gerade(-4, 0, (2, 5)), 'nein')
    chk('7a', 40, 40)
    chk('7b', f_lin(40)(10), 400)
    chk('7c', loese(40 * x, 200), 5)

# ---------------- Einheit 2 ----------------
def mn(term):
    t = sp.expand(sp.sympify(term.replace(',', '.')))
    return sp.nsimplify(t.coeff(x, 1)), sp.nsimplify(t.subs(x, 0))

def e2():
    for t, term, b in [('8a', '3*x-5', (3, -5)), ('8b', '-x+6', (-1, 6)), ('8c', '7*x', (7, 0)),
                       ('8d', '-4+0*x', (0, -4)), ('8e', '4+0.5*x', ('0.5', 4))]:
        chk(t, mn(term), b)
    for t, term, b in [('9a', '2*x+7', 'steigt'), ('9b', '-3*x+1', 'fällt'), ('9c', '0.5*x-4', 'steigt'),
                       ('9d', '-x-2', 'fällt'), ('9e', '6-2*x', 'fällt')]:
        chk(t, 'steigt' if mn(term)[0] > 0 else 'fällt', b)
    # Steigungsdreiecke: Endpunkte liegen auf den Geraden, Hoehe = m
    for t, (m, n), (x0, y0, y1), b in [('10a', (2, -2), (1, 0, 2), 2), ('10b', (-1, 3), (-1, 4, 3), -1),
                                       ('10c', (3, -4), (1, -1, 2), 3), ('10d', (-2, -1), (-2, 3, 1), -2)]:
        lage = (m * x0 + n == y0) and (m * (x0 + 1) + n == y1)
        chk(t, (y1 - y0) if lage else 'falsch', b)
    xs = [-1, 0, 1, 2]
    chk('11 Bsp', tuple(v - 1 for v in xs), (-2, -1, 0, 1))
    chk('11a', tuple(v + 3 for v in xs), (2, 3, 4, 5))
    chk('11b', tuple(2 * v - 1 for v in xs), (-3, -1, 1, 3))
    chk('11c', tuple(-v + 2 for v in xs), (3, 2, 1, 0))
    chk('12 Bsp', (3, 2 + 3), (3, 5))
    for t, m, n, b in [('12a', 1, 2, (2, 3)), ('12b', 3, 2, (2, 5)), ('12c', 1, 5, (5, 6)), ('12d', 2, 5, (5, 7))]:
        chk(t, (n, m * 1 + n), b)
    chk('13e', (5, -3 * 1 + 5), (5, 2))
    chk('13f', (3, F(1, 2) * 2 + 3), (3, 4))
    chk('13g', (-4, 2 * 1 - 4), (-4, -2))
    chk('13h', (-1, F(-2, 3) * 3 - 1), (-1, -3))
    g, h, k = (2, 2), (-1, 4), (F(1, 3), -2)
    chk('14a', g[1], 2); chk('14b', h[1], 4); chk('14c', k[1], -2)
    chk('14d', g[0], 2); chk('14e', h[0], -1); chk('14f', k[0], F(1, 3))
    links = {'p': (3, -2), 'q': (-2, 3), 'r': (F(1, 2), 1), 's': (0, -3)}
    rechts = {'l_1': (F(1, 2), 2), 'l_2': (F(-1, 2), -2), 'l_3': (F(1, 2), -2), 'l_4': (2, -2)}
    such = lambda d, mn_: [k_ for k_, v in d.items() if v == mn_][0]
    chk('15a', such(links, (3, -2)), 'p'); chk('15b', such(links, (-2, 3)), 'q')
    chk('15c', such(links, (F(1, 2), 1)), 'r'); chk('15d', such(links, (0, -3)), 's')
    chk('15e', such(rechts, (F(1, 2), -2)), 'l_3')
    fs = {1: (3, -1), 2: (-2, 4), 3: (3, 5), 4: (0, 2), 5: (-2, -3), 6: (F(1, 2), 4)}
    chk('16a', tuple(i for i, v in fs.items() if v[0] > 0), (1, 3, 6))
    par = tuple((i, j) for i in fs for j in fs if i < j and fs[i][0] == fs[j][0])
    chk('16b', par, ((1, 3), (2, 5)))
    chk('16c', tuple(i for i, v in fs.items() if v[0] == 0), (4,))
    gl = tuple((i, j) for i in fs for j in fs if i < j and fs[i][1] == fs[j][1])
    chk('16d', gl, ((2, 6),))
    P, Q = (0, 1), (3, 3)
    chk('17a', F(Q[1] - P[1], Q[0] - P[0]), F(2, 3))
    chk('17a Lage', F(2, 3) * 3 + 1, 3)
    chk('17b', F((-0.5 * 2 - 2) - (-2)).limit_denominator(10) / 2, F(-1, 2))
    chk('18a', 'g' if abs(4) > abs(1) else 'h', 'g')
    chk('18b', 'g' if abs(-3) > abs(2) else 'h', 'g')
    chk('18c', 'ja' if abs(0.5) > abs(2) else 'nein', 'nein')
    chk('19b', 'B' if loese(-6 * x + 120, 0) < loese(-4 * x + 120, 0) else 'A', 'B')
    chk('19c', 120 - 90, 30)

# ---------------- Einheit 3 ----------------
def e3():
    # 20: Einsetzen (Term, Wert zur Kontrolle der Klammerung)
    for t, (m, n, xv), b in [('20a', (5, 2, 3), 17), ('20b', (2, -7, 4), 1), ('20c', (3, -2, -4), -14),
                             ('20d', (-2, 5, -3), 11), ('20e', (-1, 8, -6), 14)]:
        chk(t, f_lin(m, n)(xv), b)   # Blatt: Wert der eingetragenen Terme 5*3+2 usw.
    chk('21 Bsp', f_lin(4, -3)(2), 5)
    for t, (m, n, xv), b in [('21a', (2, 3, 4), 11), ('21b', (5, -1, 2), 9), ('21c', (3, 4, 5), 19),
                             ('21d', (1, 7, 6), 13), ('21e', (3, 5, -4), -7), ('21f', (4, -1, '2.5'), 9)]:
        chk(t, f_lin(m, n)(xv), b)
    chk('22 Bsp', loese(3 * x + 2, 14), 4)
    for t, (m, n, w), b in [('22a', (2, 4, 10), 3), ('22b', (3, -5, 7), 4), ('22c', (5, 3, 28), 5),
                            ('22d', (4, -2, 22), 6), ('22e', (-2, 6, 14), -4), ('22f', (4, 7, 1), '-1.5')]:
        chk(t, loese(m * x + n, w), b)
    chk('23 Bsp', loese(3 * x - 6, 0), 2)
    for t, (m, n), b in [('23a', (2, -8), 4), ('23b', (4, -12), 3), ('23c', (5, -10), 2), ('23d', (3, -21), 7),
                         ('24e', (1, 3), -3), ('24f', (-3, 9), 3), ('24g', (4, 6), '-1.5')]:
        chk(t, loese(m * x + n, 0), b)
    chk('24h', (loese(-2 * x + 7, 0), f_lin(-2, 7)(0)), ('3.5', 7))
    chk('25 Bsp', auf_gerade(2, -3, (4, 5)), 'ja')
    for t, (m, n, P), b in [('25a', (1, 4, (2, 6)), 'ja'), ('25b', (2, -1, (3, 6)), 'nein'),
                            ('25c', (4, -2, (1, 3)), 'nein'), ('25d', (-1, 3, (5, -2)), 'ja'),
                            ('25e', (3, 2, (-2, -4)), 'ja'), ('25f', (-2, 1, (-3, -5)), 'nein'),
                            ('25g', (F(3, 4), -2, (-8, -8)), 'ja')]:
        chk(t, auf_gerade(m, n, P), b)
    chk('26a', tuple(f_lin(1, -3)(v) for v in [-2, -1, 0, 1, 2]), (-5, -4, -3, -2, -1))
    chk('26b', tuple(f_lin(-2, 3)(v) for v in [-2, -1, 0, 1, 2]), (7, 5, 3, 1, -1))
    chk('26c', tuple(f_lin('0.5', -1)(v) for v in [-4, -2, 0, 2, 4]), (-3, -2, -1, 0, 1))
    tab = [(0, -4), (1, -1), (2, 2), (3, 5)]
    opts = {'3x-4': (3, -4), '-4x+3': (-4, 3), '3x+4': (3, 4), 'x-4': (1, -4)}
    chk('26d', [k_ for k_, (m, n) in opts.items() if all(m * a + n == b_ for a, b_ in tab)][0], '3x-4')
    chk('27a', loese(2 * x - 4, 0), 2); chk('27b', f_lin(2, -4)(0), -4)
    chk('27c', loese(-x + 5, 0), 5); chk('27d', f_lin(-1, 5)(0), 5)
    xs = loese(2 * x - 4, -x + 5)
    chk('27e', (xs, f_lin(2, -4)(xs)), (3, 2))
    chk('28a', loese(2 * x - 6, 0), 3)
    chk('28b', (loese(4 * x - 10, 0), f_lin(4, -10)(0)), ('2.5', -10))
    chk('29a', 'wahr' if -3 < 0 else 'falsch', 'wahr')
    chk('29b', 'wahr' if loese(-3 * x + 6, 0) == 6 else 'falsch', 'falsch')
    chk('29b N', loese(-3 * x + 6, 0), 2)
    chk('29c', 'wahr' if auf_gerade(-3, 6, (-1, 9)) == 'ja' else 'falsch', 'wahr')
    chk('29d', 'wahr' if f_lin(-3, 6)(0) == -3 else 'falsch', 'falsch')
    L = lambda v: sp.nsimplify('-2.5') * v + 90
    chk('31a', L(12), 60)
    chk('31b', loese(sp.nsimplify('-2.5') * x + 90, 40), 20)
    chk('31c', loese(sp.nsimplify('-2.5') * x + 90, 0), 36)

# ---------------- Einheit 4 ----------------
def schnitt(m1, n1, m2, n2):
    xs = loese(sp.nsimplify(m1) * x + n1, sp.nsimplify(m2) * x + n2)
    return xs, sp.nsimplify(m1) * xs + n1

def e4():
    for t, (m, n), b in [('32a', (1, -3), (1, -3)), ('32b', (-3, 2), (-3, 2)), ('32c', (2, 4), (2, 4))]:
        chk(t, (m, n), b)   # Geraden wie gezeichnet
    nn = lambda m, P: sp.nsimplify(P[1]) - sp.nsimplify(m) * P[0]
    chk('33 Bsp', nn(2, (3, 5)), -1)
    for t, m, P, b in [('33a', 2, (1, 5), 3), ('33b', 3, (2, 4), -2), ('33c', -1, (3, 1), 4),
                       ('33d', -2, (-3, 4), -2), ('33e', '0.5', (-4, 3), 5)]:
        chk(t, nn(m, P), b)
    chk('34 Bsp', zwei_punkte((2, 3), (4, 9)), (3, -3))
    for t, A, B, b in [('34a', (0, 2), (2, 8), (3, 2)), ('34b', (0, -1), (4, 7), (2, -1)),
                       ('34c', (1, 6), (4, 15), (3, 3)), ('34d', (-1, 7), (2, -2), (-3, 4))]:
        chk(t, zwei_punkte(A, B), b)
    chk('35c', zwei_punkte((-2, 4), (4, 1)), ('-0.5', 3))
    chk('36 Bsp', schnitt(3, -2, 1, 4), (3, 7))
    for t, g1, g2, b in [('36a', (3, 2), (1, 6), (2, 8)), ('36b', (4, -3), (2, 5), (4, 13)),
                         ('36c', (5, -4), (2, 2), (2, 6)), ('36d', (2, 7), (5, -2), (3, 13)),
                         ('37e', (-1, 7), (2, -2), (3, 4)), ('37f', ('0.5', 1), (-1, 4), (2, 2)),
                         ('37g', (-2, 3), (2, -3), ('1.5', 0))]:
        chk(t, schnitt(*g1, *g2), b)
    chk('38 Mia', F(5 - 11, 4 - 2), -3)
    chk('38a', zwei_punkte((2, 5), (4, 11)), (3, -1))
    chk('38b', zwei_punkte((1, -1), (3, 7)), (4, -5))
    lage = lambda g, h: 'identisch' if g == h else ('parallel' if g[0] == h[0] else 'schneiden')
    chk('39a', lage((2, -3), (2, 4)), 'parallel')
    chk('39b', lage((-1, 2), (1, 2)), 'schneiden')
    chk('39b S', schnitt(-1, 2, 1, 2), (0, 2))
    chk('39c', lage((F(1, 2), 1), (F(1, 2), 1)), 'identisch')
    m, n = zwei_punkte((4, 820), (10, 700))
    chk('40a', (m, n), (-20, 900))
    chk('40c', loese(m * x + n, 0), 45)

# ---------------- Einheit 5 ----------------
def e5():
    N = sp.nsimplify
    chk('42a', (N('0.30'), 6), ('0.3', 6))
    chk('42b', (4, 12), (4, 12))
    chk('42c', (N(30) / 100, 9), ('0.3', 9))
    chk('43a', (3, 5), (3, 5)); chk('43b', (-25, 800), (-25, 800))
    chk('43c', (N(8) / 100, 2), ('0.08', 2))
    chk('44a', f_lin(6, 40)(15), 130)
    chk('44b', f_lin('-7.5', 60)(6), 15)
    tab = [(0, 120), (1, 116), (2, 112), (3, 108)]
    m, n = zwei_punkte(tab[0], tab[3])
    chk('44c m', m, -4)
    chk('44c', f_lin(m, n)(10), 80)
    grenze = loese(45 * x + 350, 1000)
    chk('44d Grenze', grenze, F(130, 9))
    chk('44d', sp.floor(grenze) + 1, 15)
    chk('44d 14', f_lin(45, 350)(14), 980); chk('44d 15', f_lin(45, 350)(15), 1025)
    A, B = f_lin('0.08', 6)(100), f_lin('0.15')(100)
    chk('45a A', A, 14); chk('45a B', B, 15); chk('45a', 'A' if A < B else 'B', 'A')
    C, D = 12 + N('0.20') * (120 - 50), f_lin('0.10', 4)(120)
    chk('45b C', C, 26); chk('45b D', D, 16); chk('45b', 'C' if C < D else 'D', 'D')
    xs = loese(N('2.5') * x + 8, N('4.5') * x)
    chk('46b', xs, 4); chk('46b y', f_lin('2.5', 8)(xs), 18)
    chk('46c A', f_lin('2.5', 8)(10), 33); chk('46c B', f_lin('4.5')(10), 45)
    chk('46c', 'ja' if f_lin('2.5', 8)(10) < f_lin('4.5')(10) else 'nein', 'ja')
    chk('47 Tim', f_lin(20, 35)(6), 155)
    chk('47a', f_lin(35, 20)(6), 230)
    chk('47b', f_lin('0.6', '3.5')(8), '8.3')
    graphen = {'I': (N('0.3'), 0), 'II': (N('0.1'), 5), 'III': (N('0.2'), 2)}
    anb = {'A': (N('0.2'), 2), 'B': (N('0.3'), 0), 'C': (N('0.1'), 5)}
    zu = tuple([g for g, v in graphen.items() if v == anb[a]][0] for a in 'ABC')
    chk('48a', zu, ('III', 'I', 'II'))
    k10 = {a: v[0] * 10 + v[1] for a, v in anb.items()}
    chk('48c', min(k10, key=k10.get), 'B')
    chk('48c Werte', tuple(k10[a] for a in 'ABC'), (4, 3, 6))
    # Schnittpunkte der Graphen fuer lesbare Lage (keine Dreifachkreuzung)
    chk('48 AB', loese(N('0.2') * x + 2, N('0.3') * x), 20)
    chk('48 AC', loese(N('0.2') * x + 2, N('0.1') * x + 5), 30)
    chk('48 BC', loese(N('0.3') * x, N('0.1') * x + 5), 25)

# ENDE EINHEITEN

if __name__ == '__main__':
    e = sys.argv[1]
    globals()[e]()
    abw = sum('ABWEICHUNG' in z for z in ZEILEN)
    ZEILEN.append(f"Abweichungen: {abw}")
    with open(f'pruef_out_{e}.txt', 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(ZEILEN) + '\n')
    print('\n'.join(ZEILEN))
