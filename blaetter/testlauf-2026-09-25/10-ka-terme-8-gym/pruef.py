# -*- coding: utf-8 -*-
# pruef.py – ein Prüfskript für den ganzen Bau (Terme und binomische Formeln).
# Aufruf: python pruef.py zone | e1 | e2 | e3 | e4 | e5
# Skriptwert: aus der Aufgabe mit sympy gerechnet. Blattwert: aus dem Lösungsquelltext abgeschrieben.
# Verglichen werden Werte (Termgleichheit bzw. Zahlenwert); bei Ausmultiplizieren zusätzlich,
# dass der Blattwert ausmultipliziert ist, bei Faktorisieren, dass er ein Produkt ist.
# Dazu je Einheit: Kasten-/Beispiel-/Originalterme des Eintrags im Aufgabenquelltext (Treffer von Hand werten)
# und doppelte Aufgabenterme.
import sys, re, io
import sympy as sp
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                        implicit_multiplication_application, convert_xor)

x, y, z, m, n, u, v, p, k, s, q, w, a, b = sp.symbols('x y z m n u v p k s q w a b')
LOC = dict(x=x, y=y, z=z, m=m, n=n, u=u, v=v, p=p, k=k, s=s, q=q, w=w, a=a, b=b)
TR = standard_transformations + (implicit_multiplication_application, convert_xor)

def P(t, ev=True):
    t = (t.replace('−', '-').replace('·', '*').replace('²', '^2').replace('³', '^3')
          .replace(',', '.'))
    return parse_expr(t, local_dict=LOC, transformations=TR, evaluate=ev)

zeilen = []
abw = 0

def aus(nr, sk, bl, ok):
    global abw
    if not ok:
        abw += 1
    zeilen.append(f"{nr} | Skript: {sk} | Blatt: {bl} | {'OK' if ok else 'ABWEICHUNG'}")

def hat_add_in_produkt(e):
    for t in sp.preorder_traversal(e):
        if isinstance(t, sp.Pow) and isinstance(t.base, sp.Add):
            return True
        if isinstance(t, sp.Mul) and any(isinstance(f, sp.Add) for f in t.args):
            return True
    return False

def ist_produkt(e):
    if isinstance(e, sp.Pow) and isinstance(e.base, sp.Add):
        return True
    if isinstance(e, sp.Mul):
        return any(isinstance(f, sp.Add) or (isinstance(f, sp.Pow) and isinstance(f.base, sp.Add)) for f in e.args)
    return False

def zahl(nr, skript, blatt):
    sk = sp.nsimplify(skript)
    bl = P(blatt)
    aus(nr, sk, blatt, abs(float(sk) - float(bl)) < 1e-9)

def term(nr, skript, blatt, form=None):
    bl = P(blatt)
    ok = sp.expand(sp.expand(skript) - sp.expand(bl)) == 0
    roh = P(blatt, False)
    if form == 'summe':
        ok = ok and not hat_add_in_produkt(roh)
    if form == 'produkt':
        ok = ok and ist_produkt(roh)
    sk = sp.factor(skript) if form == 'produkt' else sp.expand(skript)
    aus(nr, sk, blatt, ok)

def text(nr, skript, blatt):
    aus(nr, skript, blatt, str(skript) == str(blatt))

def ggt(t):
    glieder = sp.Add.make_args(sp.expand(t))
    g = glieder[0]
    for gl_ in glieder[1:]:
        g = sp.gcd(g, gl_)
    return g

def gleichwertig(t1, t2):
    return 'ja' if sp.expand(P(t1) - P(t2)) == 0 else 'nein'

# ---------------------------------------------------------------------------
def zone():
    # 1 negative Zahlen
    zahl('1a', 9 - 4, '5'); zahl('1b', -2 + 6, '4'); zahl('1c', sp.Rational(3, 2) - 4, '-2,5')
    zahl('1d', 3 - 8, '-5'); zahl('1e', -4 - 6, '-10'); zahl('1f', 6 - 10 + 3, '-1')
    # 2 Vorzeichen, Punkt vor Strich
    zahl('2a', 5 * (-3), '-15'); zahl('2b', (-4) * (-5), '20'); zahl('2c', sp.Rational(-1, 2) * 8, '-4')
    zahl('2d', (-8) ** 2, '64'); zahl('2e', 10 - 2 * 7, '-4')
    # 3 Termwert
    zahl('3a', (2 * x + 1).subs(x, 3), '7'); zahl('3b', (5 * x - 4).subs(x, 3), '11')
    zahl('3c', (3 * x + 4).subs(x, -2), '-2'); zahl('3d', (x**2 + 1).subs(x, -2), '5')
    zahl('3e', (7 - 2 * x).subs(x, -2), '11')
    # 4 zusammenfassen
    term('4a', 4*x + 3*x, '7x', 'summe'); term('4b', 9*y - 5*y, '4y', 'summe')
    term('4c', 2*m + 5 + 6*m, '8m + 5', 'summe'); term('4d', z + 4*z, '5z', 'summe')
    term('4e', 3*n - 7*n, '-4n', 'summe'); term('4f', 2*x**2 + 5*x + 3*x**2, '5x² + 5x', 'summe')
    term('4g', 5*m + 2*n - 3*m + 4*n, '2m + 6n', 'summe')
    # 5 Fehler finden
    term('5a', 5*x + 2*x**2 + 3*x, '2x² + 8x', 'summe'); term('5b', 6*y + y**2 + 2*y, 'y² + 8y', 'summe')
    # 6 malnehmen
    term('6a', 4*5*x, '20x'); term('6b', 5*2*m, '10m'); term('6c', (-4)*2*x, '-8x')
    term('6d', y*y, 'y²'); term('6e', 4*z*2*z, '8z²'); term('6f', 5*x*2*y, '10xy')
    term('6g', 2*x*9, '18x'); term('6h', (-x)*3*y, '-3xy')
    # 7 Quadratzahlen
    zahl('7a', 6**2, '36'); zahl('7b', 9**2, '81'); zahl('7c', sp.Rational(3, 10)**2, '0,09')
    zahl('7d', sp.sqrt(144), '12'); zahl('7e', sp.sqrt(196), '14'); term('7f', (4*x)**2, '16x²')

def e1():
    # 8, 9: Vorstufen ohne Rechnung – Glieder und Zeichen vor der Klammer
    text('8a', [str(t) for t in sp.Add.make_args(5*x - 2*y + 7)].__len__(), 3)
    text('9d', 'negative Zahl', 'negative Zahl')
    # 10 Plusklammer (Beispiel 6 + (x − 1) = x + 5)
    term('10B', 6 + (x - 1), 'x + 5', 'summe')
    term('10a', 3 + (x + 4), 'x + 7', 'summe'); term('10b', 2*x + (5 + x), '3x + 5', 'summe')
    term('10c', 10 + (x - 6), 'x + 4', 'summe'); term('10d', 4*m + (2 - m), '3m + 2', 'summe')
    # 11 Zahl mal Klammer (Beispiel 4·(x + 2) = 4x + 8)
    term('11B', 4*(x + 2), '4x + 8', 'summe')
    term('11a', 2*(x + 3), '2x + 6', 'summe'); term('11b', 5*(m + 4), '5m + 20', 'summe')
    term('11c', 6*(y + 1), '6y + 6', 'summe'); term('11d', 7*(2 + x), '14 + 7x', 'summe')
    term('11e', 4*(x - 5), '4x - 20', 'summe'); term('11f', (x + 9)*2, '2x + 18', 'summe')
    term('11g', x*(x + 4), 'x² + 4x', 'summe')
    # 12 Minusklammer (Beispiel 9 − (x − 2) = 11 − x)
    term('12B', 9 - (x - 2), '11 - x', 'summe')
    term('12a', -(x + 6), '-x - 6', 'summe'); term('12b', 10 - (x + 2), '8 - x', 'summe')
    term('12c', 7 - (x - 5), '12 - x', 'summe'); term('12d', 5*x - (2*x - 1), '3x + 1', 'summe')
    term('12e', 4*m - (m - 2*n + 3), '3m + 2n - 3', 'summe'); term('12f', -3*(x - 4), '-3x + 12', 'summe')
    term('12g', 4*x - 2*(x + 3), '2x - 6', 'summe'); term('12h', 2*(3*x + 5) - 4*(x - 2), '2x + 18', 'summe')
    # 13 Fehler finden: richtige Rechnung und Selbstrechnen
    term('13a', 12 - (x - 5), '17 - x', 'summe'); term('13b', 9 - (2*x - 4), '13 - 2x', 'summe')
    term('13c', 5 - 2*(x + 1), '3 - 2x', 'summe'); term('13d', 8 - 3*(x + 2), '2 - 3x', 'summe')
    # 14 Begründen: gleichwertig?
    text('14a', gleichwertig('3*(x-2)', '3x-2'), 'nein'); text('14b', gleichwertig('6-(x+2)', '4-x'), 'ja')
    text('14c', gleichwertig('2*(x+1)', 'x+3'), 'nein')
    zahl('14c-Probe x=0', (2*(x + 1)).subs(x, 0) - (x + 3).subs(x, 0), '2 - 3')
    # 15 Anwendung Wechselgeld
    term('15b', 20 - 3*(p + 2), '14 - 3p', 'summe')
    zahl('15c', (20 - 3*(p + 2)).subs(p, sp.Rational(3, 2)), '9,50')
    zahl('15d', (20 - 3*(p + 2)).subs(p, 5), '-1')

def e2():
    # 16 Ausklammern (Beispiel 4x + 20 = 4·(x + 5))
    term('16B', 4*x + 20, '4·(x + 5)', 'produkt')
    term('16a', 3*x + 12, '3·(x + 4)', 'produkt'); term('16b', 5*m + 10, '5·(m + 2)', 'produkt')
    term('16c', 7*y + 21, '7·(y + 3)', 'produkt'); term('16d', 2*x - 16, '2·(x - 8)', 'produkt')
    term('16e', x**2 + 9*x, 'x·(x + 9)', 'produkt'); term('16f', 4*x**2 + 12*x, '4x·(x + 3)', 'produkt')
    term('16g', 5*x**2 + 5*x, '5x·(x + 1)', 'produkt'); term('16h', 6*x**2 + 3*x - 9, '3·(2x² + x - 3)', 'produkt')
    term('16i', 10*x**2 - 15*x, '5x·(2x - 3)', 'produkt'); term('16j', 12*m**2 + 8*m*n - 4*m, '4m·(3m + 2n - 1)', 'produkt')
    # größter gemeinsamer Faktor jeweils vollständig ausgeklammert?
    for nr, t, f in [('16a', 3*x + 12, 3), ('16b', 5*m + 10, 5), ('16c', 7*y + 21, 7), ('16d', 2*x - 16, 2),
                     ('16e', x**2 + 9*x, x), ('16f', 4*x**2 + 12*x, 4*x), ('16g', 5*x**2 + 5*x, 5*x),
                     ('16h', 6*x**2 + 3*x - 9, 3), ('16i', 10*x**2 - 15*x, 5*x), ('16j', 12*m**2 + 8*m*n - 4*m, 4*m)]:
        text(nr + ' ggT', ggt(t), f)
    # 17 Fehler finden
    term('17a', 6*x + 18, '6·(x + 3)', 'produkt'); term('17b', 8*m - 24, '8·(m - 3)', 'produkt')
    term('17c', 7*y**2 + 7*y, '7y·(y + 1)', 'produkt'); term('17d', 9*x**2 - 9*x, '9x·(x - 1)', 'produkt')
    # 18 Entscheiden: größter gemeinsamer Faktor (1 = nein)
    text('18a', ggt(10*x + 4), 2); text('18b', ggt(4*x + 9), 1); text('18c', ggt(x**2 + 5), 1)
    text('18d', ggt(8*m**2 + 12*m), 4*m); text('18e', ggt(12*x + 8), 4)
    term('18e', 12*x + 8, '4·(3x + 2)', 'produkt')
    # 19 Anwendung Rechteck
    term('19a', (6*k + 15) / 3, '2k + 5', 'summe'); term('19b', sp.cancel((k**2 + 8*k) / k), 'k + 8', 'summe')
    zahl('19c', ((6*k + 15) / 3).subs(k, 4), '13'); zahl('19c Probe', 3 * 13 - (6*4 + 15), '0')

def e3():
    # 20 Vorstufe: vier Produkte je Aufgabe
    for nr, t1, t2 in [('20a', x + 1, x + 9), ('20b', m + 3, n + 4), ('20c', x - 5, x + 1), ('20d', 2*y + 1, y - 7)]:
        text(nr + ' Produkte', len(sp.Add.make_args(t1)) * len(sp.Add.make_args(t2)), 4)
    # 21 Termwert mit zwei Variablen (Beispiel m = 2, n = 5: 3m + n = 11)
    zahl('21B', (3*m + n).subs({m: 2, n: 5}), '11')
    W1 = {m: 4, n: 1}; W2 = {m: -3, n: 2}
    zahl('21a', (m + n).subs(W1), '5'); zahl('21b', (2*m - n).subs(W1), '7'); zahl('21c', (m*n).subs(W1), '4')
    zahl('21d', (3*m + 5*n).subs(W1), '17'); zahl('21e', (m + 2*n).subs(W2), '1'); zahl('21f', (m**2 + n).subs(W2), '11')
    zahl('21g', (2*m*n).subs(W2), '-12'); zahl('21h', (m**2 - m*n + n**2).subs(W2), '19')
    # 22 zusammenfassen mit zwei Variablen (Beispiel 4x + 3y + 2x = 6x + 3y)
    term('22B', 4*x + 3*y + 2*x, '6x + 3y', 'summe')
    term('22a', 3*x + 2*y + 4*x, '7x + 2y', 'summe'); term('22b', 5*m + 4*n + 2*n, '5m + 6n', 'summe')
    term('22c', 2*m + 3*n + 6*m + 4*n, '8m + 7n', 'summe'); term('22d', 4*u + 5*v + 3*u + 2*v, '7u + 7v', 'summe')
    term('22e', 8*x - 3*y - x + 6*y, '7x + 3y', 'summe'); term('22f', x**2 + 3*x*y + 2*x**2 - x*y + x, '3x² + 2xy + x', 'summe')
    term('22g', 5*m*n - 2*n*m + 4*m, '3mn + 4m', 'summe'); term('22h', 3*(2*x + y) + 4*x, '10x + 3y', 'summe')
    # 23 Klammer mal Klammer (Beispiel (x + 6)·(x + 2) = x² + 8x + 12)
    term('23B', (x + 6)*(x + 2), 'x² + 8x + 12', 'summe')
    term('23a', (x + 1)*(x + 4), 'x² + 4x + x + 4', 'summe'); term('23b', (m + 2)*(m + 7), 'm² + 7m + 2m + 14', 'summe')
    term('23c', (y + 3)*(y + 1), 'y² + y + 3y + 3', 'summe'); term('23d', (u + 4)*(v + 3), 'uv + 3u + 4v + 12', 'summe')
    term('23e', (x + 2)*(x + 9), 'x² + 11x + 18', 'summe')
    # 24 weiter
    term('24a', (x - 6)*(x + 2), 'x² - 4x - 12', 'summe'); term('24b', (x - 3)*(x - 7), 'x² - 10x + 21', 'summe')
    term('24c', (2*x + 1)*(x + 5), '2x² + 11x + 5', 'summe'); term('24d', (m + 2*n)*(3*m + n), '3m² + 7mn + 2n²', 'summe')
    term('24e', (4*x - 3)*(2*x - 5), '8x² - 26x + 15', 'summe')
    # 25 Fehler finden
    term('25a', (x + 6)*(x + 4), 'x² + 10x + 24', 'summe'); term('25b', (x + 7)*(x + 2), 'x² + 9x + 14', 'summe')
    term('25c', (x - 5)*(x - 1), 'x² - 6x + 5', 'summe'); term('25d', (x - 2)*(x - 8), 'x² - 10x + 16', 'summe')
    term('25e', (x + 2)*(x + 4), 'x² + 6x + 8', 'summe'); term('25f', (y + 6)*(y + 3), 'y² + 9y + 18', 'summe')
    # 26 Flächenbild: Teilflächen und Summe
    term('26a', x*x + x*4 + 1*x + 1*4, 'x² + 4x + x + 4', 'summe'); term('26c', (x + 4)*(x + 1), 'x² + 5x + 4', 'summe')
    term('26c fehlt', (x + 4)*(x + 1) - (x**2 + 4), '5x', 'summe')
    # 27 Anwendung Beet
    term('27a', (s + 4)*(s - 2), 's² + 2s - 8', 'summe')
    zahl('27b alt', (s**2).subs(s, 6), '36'); zahl('27b neu', ((s + 4)*(s - 2)).subs(s, 6), '40')
    term('27c Unterschied', (s + 4)*(s - 2) - s**2, '2s - 8', 'summe')
    zahl('27c Grenze', sp.solve(sp.Eq(2*s - 8, 0), s)[0], '4')

def formel(t):
    e = P(t, False)
    if isinstance(e, sp.Pow) and e.exp == 2 and isinstance(e.base, sp.Add) and len(e.base.args) == 2:
        return 'zweite' if any(g.could_extract_minus_sign() for g in e.base.args) else 'erste'
    if isinstance(e, sp.Mul):
        f = [g for g in e.args if isinstance(g, sp.Add)]
        if len(f) == 2 and all(len(g.args) == 2 for g in f) and len(sp.Add.make_args(sp.expand(P(t)))) == 2:
            return 'dritte'
    return 'keine'

def e4():
    # 28 Vorstufe: Quadrat einer Klammer?
    text('28a', 'ja' if sp.expand((x + 8)**2 - (x + 8)*(x + 8)) == 0 else 'nein', 'ja')
    text('28b', formel('(x+4)*(x-4)') in ('erste', 'zweite'), False)
    text('28c', 'ja', 'ja'); term('28c', (m - 6)**2, '(m - 6)·(m - 6)', 'produkt')
    text('28d', sp.expand((y + 2)*(2 + y) - (y + 2)**2) == 0, True)
    text('28e', sp.expand((2*x + 1)*(x + 1) - (x + 1)**2) == 0 or sp.expand((2*x + 1)*(x + 1) - (2*x + 1)**2) == 0, False)
    # 29 a und b
    for nr, t, aa, bb in [('29a', '(x+9)^2', x, 9), ('29b', '(y-4)^2', y, 4), ('29c', '(4x+1)^2', 4*x, 1),
                          ('29d', '(3m-2n)^2', 3*m, 2*n), ('29e', '(6+z)^2', 6, z)]:
        e = P(t); ok = sp.expand(e - (aa + bb)**2) == 0 or sp.expand(e - (aa - bb)**2) == 0
        text(nr, ok, True)
    # 30 welche Formel
    text('30a', formel('(x+12)^2'), 'erste'); text('30b', formel('(m+7)*(m-7)'), 'dritte')
    text('30c', formel('(y-5)*(y+6)'), 'keine'); text('30d', formel('(z-10)^2'), 'zweite')
    text('30e', formel('(u+2)*(u+3)'), 'keine')
    # 31 Verfahren (Beispiel (x + 6)² = x² + 12x + 36)
    term('31B', (x + 6)**2, 'x² + 12x + 36', 'summe')
    term('31a', (x + 1)**2, 'x² + 2x + 1', 'summe'); term('31b', (x + 4)**2, 'x² + 8x + 16', 'summe')
    term('31c', (m + 2)**2, 'm² + 4m + 4', 'summe'); term('31d', (y + 10)**2, 'y² + 20y + 100', 'summe')
    term('31e', (x - 9)**2, 'x² - 18x + 81', 'summe'); term('31f', (x + 8)*(x - 8), 'x² - 64', 'summe')
    # 32 weiter
    text('32a Formel', formel('(4-z)*(4+z)'), 'dritte'); term('32a', (4 - z)*(4 + z), '16 - z²', 'summe')
    text('32b Formel', formel('(x+6)*(x-1)'), 'keine'); term('32b', (x + 6)*(x - 1), 'x² + 5x - 6', 'summe')
    term('32c', (3*x + 2)**2, '9x² + 12x + 4', 'summe'); term('32d', (2*m - n)**2, '4m² - 4mn + n²', 'summe')
    # 33 weiter, Prüfungshöhe
    term('33a', 4*(x - 1)**2, '4x² - 8x + 4', 'summe'); term('33b', -(x - 7)**2, '-x² + 14x - 49', 'summe')
    term('33c', (x + 2)**2 - 4*x, 'x² + 4', 'summe'); term('33d', (x - 6)**2 - 11, 'x² - 12x + 25', 'summe')
    # 34 Kopfrechnen (Beispiel 41² = 1681)
    zahl('34B', 41**2, '1681'); zahl('34a', 31**2, '961'); zahl('34b', 19**2, '361')
    zahl('34c', 52 * 48, '2496'); zahl('34d', 99**2, '9801')
    # 35, 36 Fehler finden
    term('35a', (x + 11)**2, 'x² + 22x + 121', 'summe'); term('35b', (m + 13)**2, 'm² + 26m + 169', 'summe')
    term('35c', (x - 10)**2, 'x² - 20x + 100', 'summe'); term('35d', (y - 8)**2, 'y² - 16y + 64', 'summe')
    term('36a', (5*x + 2)**2, '25x² + 20x + 4', 'summe'); term('36b', (4*y + 3)**2, '16y² + 24y + 9', 'summe')
    term('36c', -(x + 6)**2, '-x² - 12x - 36', 'summe'); term('36d', 20 - (x + 4)**2, '-x² - 8x + 4', 'summe')
    # 37 Begründen
    zahl('37a links', (6 + 4)**2, '100'); zahl('37a rechts', 6**2 + 4**2, '52'); zahl('37a fehlt', 2*6*4, '48')
    term('37b', x*x + 2*x + 2*x + 2*2, 'x² + 4x + 4', 'summe'); term('37b Formel', (x + 2)**2, 'x² + 4x + 4', 'summe')
    text('37c', sp.solve(sp.Eq(sp.expand((a + b)**2), a**2 + b**2), a), [0])
    # 38 Anwendung Rahmen
    term('38a', (q + 4)**2, 'q² + 8q + 16', 'summe'); term('38b', (q + 4)**2 - q**2, '8q + 16', 'summe')
    zahl('38c', ((q + 4)**2 - q**2).subs(q, 10), '96')

def mittelglied_passt(t):
    # erstes und letztes Glied Quadrate; passt das Mittelglied zu (r ± s)²?
    return 'ja' if len(sp.factor_list(sp.expand(P(t)))[1]) == 1 and sp.factor_list(sp.expand(P(t)))[1][0][1] == 2 else 'nein'

def e5():
    # 39 Quadrat? (ja/nein und wovon)
    def quadrat_von(t):
        pos = {g: sp.Symbol(str(g), positive=True) for g in (x, y, z, m)}
        r = sp.sqrt(sp.sympify(t).subs(pos)).subs({v_: k_ for k_, v_ in pos.items()})
        if not r.is_polynomial(x, y, z, m):
            return 'nein'
        return r if all(c.is_integer for c in sp.Poly(r, x, y, z, m).coeffs()) else 'nein'
    for nr, t, r in [('39 81', 81, '9'), ('39 z²', z**2, 'z'), ('39 25m²', 25*m**2, '5*m'), ('39 8x', 8*x, 'nein'),
                     ('39 12', 12, 'nein'), ('39 100y²', 100*y**2, '10*y'), ('39 2x²', 2*x**2, 'nein')]:
        text(nr, quadrat_von(t), r)
    # 40 Mittelglied
    for nr, t, bl in [('40a', 'x^2+4x+4', 'ja'), ('40b', 'x^2+8x+64', 'nein'), ('40c', 'y^2-20y+100', 'ja'),
                      ('40d', 'm^2+9m+81', 'nein'), ('40e', '9x^2+6x+1', 'ja'), ('40f', 'z^2+10z+36', 'nein')]:
        text(nr, mittelglied_passt(t), bl)
    # 41 Verfahren (Beispiel x² − 36 = (x + 6)·(x − 6))
    term('41B', x**2 - 36, '(x + 6)·(x - 6)', 'produkt')
    term('41a', x**2 - 16, '(x + 4)·(x - 4)', 'produkt'); term('41b', x**2 - 81, '(x + 9)·(x - 9)', 'produkt')
    term('41c', m**2 - 1, '(m + 1)·(m - 1)', 'produkt'); term('41d', y**2 - 100, '(y + 10)·(y - 10)', 'produkt')
    term('41e', x**2 + 16*x + 64, '(x + 8)²', 'produkt'); term('41f', z**2 - 18*z + 81, '(z - 9)²', 'produkt')
    # 42 weiter
    term('42a', 16*y**2 + 40*y + 25, '(4y + 5)²', 'produkt'); term('42b', 7*x**2 - 28, '7·(x + 2)·(x - 2)', 'produkt')
    text('42c', mittelglied_passt('x^2+6x+16'), 'nein'); zahl('42c Mittelglied', 2*4, '8')
    term('42d', 16*x**2 - 1, '(4x + 1)·(4x - 1)', 'produkt')
    # 43 weiter: Produkt null, quadratische Ergänzung, Prüfungshöhe
    text('43a', sorted(sp.solve(x**2 - 144, x)), sorted([-12, 12]))
    zahl('43b', sp.expand(x**2 + 8*x + 20 - (x + 4)**2), '4')
    term('43c', 2*x**2 - 24*x + 72, '2·(x - 6)²', 'produkt')
    # 44 Fehler finden
    text('44a', len(sp.factor_list(x**2 + 16)[1]) == 1 and sp.factor_list(x**2 + 16)[1][0][1] == 1, True)
    text('44b geht nicht', sp.factor(m**2 + 64) == m**2 + 64, True)
    text('44c', mittelglied_passt('x^2+10x+16'), 'nein'); term('44d', x**2 + 20*x + 100, '(x + 10)²', 'produkt')
    term('44e', x**2 - 8*x + 16, '(x - 4)²', 'produkt'); term('44f', y**2 - 22*y + 121, '(y - 11)²', 'produkt')
    # 45 Begründen
    text('45a', sp.factor(z**2 + 36) == z**2 + 36, True); term('45b', 9 - y**2, '(3 + y)·(3 - y)', 'produkt')
    # 46 Anwendung Grundstück
    wp = sp.Symbol('w', positive=True)   # Seitenlänge: w positiv, sonst zieht sympy die Wurzel nicht
    term('46a', sp.sqrt(sp.factor((w**2 + 24*w + 144).subs(w, wp))).subs(wp, w), 'w + 12', 'summe')
    zahl('46b Seite', (w + 12).subs(w, 8), '20'); zahl('46b Fläche', (w**2 + 24*w + 144).subs(w, 8), '400')
    term('46c', sp.cancel((w**2 - 16) / (w + 4)), 'w - 4', 'summe')

def doppelt():
    # doppelte Aufgabenterme über alle Aufgabendateien (\gl-Argumente und Terme in teilezwei/geruest)
    alle = {}
    for d in ['zone_a.tex', 'e1_a.tex', 'e2_a.tex', 'e3_a.tex', 'e4_a.tex', 'e5_a.tex']:
        src = io.open(d, encoding='utf-8').read()
        for t in re.findall(r'\\gl(?:\[\d\])?\{((?:[^{}]|\{[^{}]*\})*)\}', src) + re.findall(r'\\gz\{\w\}\{\$([^$]*)\$\}', src):
            alle.setdefault(norm(t), []).append(d)
    return {t: ds for t, ds in alle.items() if len(ds) > 1}

EINHEITEN = {'zone': zone, 'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'e5': e5}

# Kasten-, Beispiel- und Originalterme beider Einträge (normalisiert: ohne Leerzeichen, * für Malpunkt)
VERBOTEN = [
 '(x+3)*(x+5)', 'x^2+8x+15', '(x-4)*(x+2)', 'x^2-2x-8', '(x+3)^2', 'x^2+6x+9', '(x-3)^2', 'x^2-6x+9',
 '(x+3)*(x-3)', 'x^2-9', '(2+3)^2', '(2x+3)^2', '4x^2+12x+9', 'x^2+10x+25', '(x+5)^2', 'x^2-10x+25',
 '(x-5)^2', 'x^2-25', '3x^2-75', 'x^2+7x+25', '3x+5x', '7a-2a+4', 'x^2+3x', '3*4x', '2x*3x', '3a*2b',
 '3*(x+4)', '6x+9', '4a^2+2a', 'x^2+6x+7', '(x-2)^2-4', 'x^2-4x', '-2x+3', '(2+2)^2', '(x+1)*(x+3)',
 '7*(x+6)', '-(x-6)', '6x+12', 'x^2+7x', '(-6)*(-7)', '11-6*7', 'x^2-7', '(x-7)^2+11', '3-7', '-2-5',
 '(-2)*(-3)', '3*(-4)', '(x+7)^2', '(x+7)*(x-11)', '(7x+11)^2', '49x^2', 'x^2+14x+49', '4x-3y+2',
 'x^2+9', '(3+4)^2', '(x-4)*(x-2)', 'x^2+8x=', '(3x)^2', '-(x-1)^2', '3*(x+2)^2', 'x^2+5x+9',
 '2x^2-18', '2x+3x^2', 'x+6x', '5a-3b+2a', '-(x-4)', '2+3*x', '(-2)*3x',
]

def norm(t):
    t = t.replace('\\cdot', '*').replace('{', '').replace('}', '').replace(' ', '').replace('\\left', '').replace('\\right', '')
    return t

def kastenpruefung(datei):
    try:
        src = io.open(datei, encoding='utf-8').read()
    except OSError:
        return []
    mathe = ' | '.join(re.findall(r'\$([^$]*)\$', src) + re.findall(r'\\gl(?:\[\d\])?\{([^}]*(?:\{[^}]*\}[^}]*)*)\}', src)
                     + re.findall(r'\\(?:rechnung|beispiel)\{(.*)\}', src))
    nm = norm(mathe)
    return [v for v in VERBOTEN if v in nm]

if __name__ == '__main__':
    teil = sys.argv[1]
    EINHEITEN[teil]()
    treffer = kastenpruefung(f'{teil}_a.tex')
    with io.open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8') as f:
        for zl in zeilen:
            f.write(zl + '\n')
        f.write(f"Kastenprüfung {teil}_a.tex: {', '.join(treffer) if treffer else 'keine Treffer'}\n")
        if teil == 'e5':
            dd = doppelt()
            f.write("Doppelte Aufgabenterme (alle Aufgabendateien): "
                    + ('; '.join(f"{t} in {', '.join(ds)}" for t, ds in dd.items()) if dd else 'keine') + "\n")
        f.write(f"Abweichungen: {abw}\n")
    print(io.open(f'pruef_out_{teil}.txt', encoding='utf-8').read())
