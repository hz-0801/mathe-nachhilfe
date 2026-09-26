# pruef.py – rechnet die Lösungen je Einheit unabhängig nach (sympy).
# Aufruf: python pruef.py zone | e1 | e2 | e3 | e4 | e5  -> pruef_out_<teil>.txt
# Blattwerte sind aus dem Lösungsquelltext (<teil>_l.tex) übertragen.
import sys
from sympy import symbols, expand, sqrt, Integer, solve, Eq, factor, simplify
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
    implicit_multiplication_application, convert_xor)

x, y, z, u, v = symbols('x y z u v')
TR = standard_transformations + (implicit_multiplication_application, convert_xor)
LOC = {'x': x, 'y': y, 'z': z, 'u': u, 'v': v, 'sqrt': sqrt}

def P(s):
    s = s.replace('−', '-').replace('·', '*')
    return parse_expr(s, local_dict=LOC, transformations=TR)

zeilen = []

def gleich(nr, aufgabe, blatt, subs=None):
    """Term- oder Zahlvergleich: Skriptwert = expand(aufgabe) (ggf. eingesetzt)."""
    a = P(aufgabe)
    if subs:
        a = a.subs(subs)
    sw = expand(a)
    bw = P(blatt)
    ok = simplify(expand(bw) - sw) == 0
    zeilen.append((nr, str(sw), blatt, ok))

def produkt(nr, aufgabe, blatt):
    """Faktorisieren/Ausklammern: Blattwert muss ein Produkt sein und ausmultipliziert gleich."""
    a = expand(P(aufgabe))
    bw = P(blatt)
    roh = parse_expr(blatt.replace('−', '-'), local_dict=LOC, transformations=TR, evaluate=False)
    ok = (simplify(expand(bw) - a) == 0) and (roh.is_Mul or roh.is_Pow)
    zeilen.append((nr, str(factor(a)), blatt, ok))

def loesung(nr, gleichung, blatt):
    l, r = gleichung.split('=')
    sw = sorted(solve(Eq(P(l), P(r)), x))
    bw = sorted([P(t) for t in blatt.split(';')])
    zeilen.append((nr, str(sw), str(bw), sw == bw))

def wahr(nr, aussage_skript, blatt):
    zeilen.append((nr, str(aussage_skript), str(blatt), bool(aussage_skript) == blatt))

def zahl(nr, wert, blatt):
    zeilen.append((nr, str(wert), str(blatt), simplify(wert - P(str(blatt))) == 0))

def zone():
    # 1 negative Zahlen
    for t, (a, b) in zip('abcde', [('4-9', '-5'), ('-3-6', '-9'), ('-14+8', '-6'), ('-5-(-12)', '7'), ('9-15+4', '-2')]):
        gleich('1' + t, a, b)
    for t, (a, b) in zip('abcde', [('3*(-5)', '-15'), ('(-4)*(-2)', '8'), ('(-12)*(-3)', '36'), ('(-1)*(-9)', '9'), ('(-8)^2', '64')]):
        gleich('2' + t, a, b)
    for t, (a, b) in zip('abcde', [('2+3*4', '14'), ('20-2*5', '10'), ('7-4*3', '-5'), ('5-2*(-3)', '11'), ('3*2-4*5', '-14')]):
        gleich('3' + t, a, b)
    for t, (a, s, b) in zip('abcde', [('3x+2', 4, '14'), ('5-x', 2, '3'), ('2x-7', -3, '-13'), ('x^2-3', -4, '13'), ('4-2x', -5, '14')]):
        gleich('4' + t, a, b, {x: s})
    for t, (a, b) in zip('abcdef', [('4x+5x', '9x'), ('9y-3y', '6y'), ('2x+7+5x', '7x+7'), ('x+4x', '5x'), ('2y-9y', '-7y'), ('-3x+5x', '2x')]):
        gleich('5' + t, a, b)
    for t, (a, b) in zip('abcdef', [('3*5x', '15x'), ('4y*2', '8y'), ('x*x', 'x^2'), ('2x*4x', '8x^2'), ('(-3)*6x', '-18x'), ('4x*5y', '20xy')]):
        gleich('6' + t, a, b)
    # 7 Fehler finden: korrigierte Rechnung; zusätzlich: Vorgabe ist falsch
    gleich('7a', '3x^2+5x+2x', '3x^2+7x')
    wahr('7a Vorgabe falsch', expand(P('3x^2+5x+2x') - P('10x^2')) != 0, True)
    gleich('7b', '4+3*x', '4+3x')
    wahr('7b Vorgabe falsch', expand(P('4+3*x') - P('7x')) != 0, True)
    for t, (a, b) in zip('abcde', [('5x^2+2x+3x', '5x^2+5x'), ('x^2+4x+2x^2', '3x^2+4x'), ('6x-2x^2+x', '-2x^2+7x'), ('3x^2+7-x^2', '2x^2+7'), ('5+2*x+3', '2x+8')]):
        gleich('8' + t, a, b)
    for t, (a, b) in zip('abcdef', [('6^2', '36'), ('9^2', '81'), ('sqrt(64)', '8'), ('sqrt(169)', '13'), ('(-11)^2', '121'), ('(4x)^2', '16x^2')]):
        gleich('9' + t, a, b)
    gleich('9g', '36', '6^2')
    gleich('9h', '9x^2', '(3x)^2')

def e1():
    # 10 Glieder mit Vorzeichen: Summe der Glieder = Term
    for t, (a, b) in zip('abcde', [('6x+2y-5', '6x+2y-5'), ('3x-4+y', '3x-4+y'), ('-x+7y-2', '-x+7y-2'), ('8-3x-y', '8-3x-y'), ('-2x-5y+9', '-2x-5y+9')]):
        gleich('10' + t, a, b)
    # 11 Zeichen vor der Klammer (Zuordnung, Faktor vor der Klammer): Plus=+1, Minus=-1, Zahl=Wert
    for t, (skript, blatt) in zip('abcde', [(1, 1), (-1, -1), (3, 3), (-4, -4), (-1, -1)]):
        zahl('11' + t, Integer(skript), blatt)
    L12 = [('x+(y+4)', 'x+y+4'), ('3x+(y-2)', '3x+y-2'), ('5+(2x-y)', '5+2x-y'), ('3*(x+5)', '3x+15'),
           ('2*(y+6)', '2y+12'), ('5*(x+2)', '5x+10'), ('4*(y+7)', '4y+28'), ('4x-(y+2)', '4x-y-2'),
           ('x-(3y-z+4)', 'x-3y+z-4'), ('-3*(x-4)', '-3x+12'), ('x*(x+6)', 'x^2+6x')]
    for t, (a, b) in zip('abcdefghijk', L12):
        gleich('12' + t, a, b)
    L13 = [('3x+(2x+4)', '5x+4'), ('6+2*(x+1)', '2x+8'), ('5y+3*(y-2)', '8y-6'), ('7y-(2y+5)', '5y-5'),
           ('10-2*(x-4)', '18-2x'), ('2*(x+3)+4*(x-1)', '6x+2'), ('3x*(x-2)-2*(x^2-4x+5)', 'x^2+2x-10')]
    for t, (a, b) in zip('abcdefg', L13):
        gleich('13' + t, a, b)
    gleich('13f Zwischen', '2*(x+3)+4*(x-1)', '2x+6+4x-4')
    gleich('13g Zwischen', '3x*(x-2)-2*(x^2-4x+5)', '3x^2-6x-2x^2+8x-10')
    gleich('14a', '9x-(4x-6)', '5x+6'); wahr('14a Vorgabe falsch', expand(P('9x-(4x-6)') - P('5x-6')) != 0, True)
    gleich('14b', '12-3*(x-2)', '18-3x'); wahr('14b Vorgabe falsch', expand(P('12-3*(x-2)') - P('6-3x')) != 0, True)
    wahr('15a gleichwertig?', expand(P('2*(x+5)') - P('2x+5')) == 0, False)
    gleich('15a Probe x=1', '2*(x+5)', '12', {x: 1}); gleich('15a Probe x=1 rechts', '2x+5', '7', {x: 1})
    wahr('15b gleichwertig?', expand(P('10-(x-3)') - P('13-x')) == 0, True)
    wahr('15c gleichwertig?', expand(P('-(4-x)') - P('x-4')) == 0, True)
    gleich('16a', '2*(x+6)+2*x-3', '4x+9')
    gleich('16b', '2*(x+6)+2*x-3', '41', {x: 8})

def e2():
    L17 = [('3x+12', '3*(x+4)'), ('5y+35', '5*(y+7)'), ('2x-10', '2*(x-5)'), ('7y+21', '7*(y+3)'),
           ('x^2+9x', 'x*(x+9)'), ('6x^2+15x', '3x*(2x+5)'), ('6x+6', '6*(x+1)'), ('4x^2+8x+12', '4*(x^2+2x+3)'),
           ('10x^2-4x', '2x*(5x-2)'), ('12x^3+8x^2-4x', '4x*(3x^2+2x-1)')]
    for t, (a, b) in zip('abcdefghij', L17):
        produkt('17' + t, a, b)
    gleich('17i Probe', '2x*(5x-2)', '10x^2-4x'); gleich('17j Probe', '4x*(3x^2+2x-1)', '12x^3+8x^2-4x')
    produkt('18a', '6x+15', '3*(2x+5)'); wahr('18a Vorgabe falsch', expand(P('3*(2x+15)') - P('6x+15')) != 0, True)
    produkt('18b', '7x^2+7x', '7x*(x+1)'); wahr('18b Vorgabe falsch', expand(P('7x*x') - P('7x^2+7x')) != 0, True)
    from sympy import gcd, Poly
    def gf(term):  # gemeinsamer Faktor außer 1 (Zahl oder Variable)?
        t = expand(P(term)); g = gcd(t.args[0], t.args[1])
        return g != 1 and g != -1
    for t, (a, b) in zip('abcdef', [('4x+9', False), ('6x+10', True), ('x^2+3', False), ('5x^2+2x', True), ('3x+7y', False), ('14y-21', True)]):
        wahr('19' + t, gf(a), b)
    produkt('20a', '8x^2+20x', '4x*(2x+5)')
    gleich('20b Länge', '2x+5', '25', {x: 10}); gleich('20b Breite', '4x', '40', {x: 10})
    gleich('20b Fläche', '8x^2+20x', '1000', {x: 10}); gleich('20b Probe', '40*25', '1000')

def e3():
    # 21 Vorstufe: vier Produkte je Aufgabe (Zahl der Pfeile)
    for t, a in zip('abcde', ['(x+2)*(y+5)', '(u+4)*(v-1)', '(x-3)*(x+8)', '(2x+1)*(x-6)', '(y+7)*(z+3)']):
        l, r = a.split('*')
        zahl('21' + t + ' Pfeile', Integer(len(P(l).args) * len(P(r).args)), 4)
    L22 = [('2x+y', 3, 4, '10'), ('x+3y', 2, 5, '17'), ('4x-y', 2, 9, '-1'), ('xy+1', 3, 4, '13'),
           ('3x-2y', -2, 5, '-16'), ('x^2+xy', -3, 2, '3'), ('2x^2-xy+y^2', -1, 4, '22')]
    for t, (a, sx, sy, b) in zip('abcdefg', L22):
        gleich('22' + t, a, b, {x: sx, y: sy})
    L23 = [('3x+2y+4x', '7x+2y'), ('5u+v+2v', '5u+3v'), ('2x+6y+3x+4y', '5x+10y'), ('4u+3v+2u+5v', '6u+8v'),
           ('6x-y-2x+4y', '4x+3y'), ('x^2+3xy+2x^2-xy+5x', '3x^2+2xy+5x'), ('4xy-2x^2+3yx-x^2+6y', '7xy-3x^2+6y')]
    for t, (a, b) in zip('abcdefg', L23):
        gleich('23' + t, a, b)
    L24 = [('3*(x+2y)', '3x+6y'), ('4*(2x-y)', '8x-4y'), ('5*(u+v)', '5u+5v'), ('2*(3x+4y)', '6x+8y'),
           ('x*(y+3)', 'xy+3x'), ('-(2x-5y)', '-2x+5y'), ('2x*(x+3y)', '2x^2+6xy'), ('4*(x+2y)-3*(x-y)', 'x+11y')]
    for t, (a, b) in zip('abcdefgh', L24):
        gleich('24' + t, a, b)
    L25 = [('(x+2)*(y+4)', 'xy+4x+2y+8'), ('(x+5)*(y+1)', 'xy+x+5y+5'), ('(u+3)*(v+6)', 'uv+6u+3v+18'),
           ('(x+7)*(y+2)', 'xy+2x+7y+14'), ('(x+2)*(x+6)', 'x^2+8x+12'), ('(x-4)*(x+9)', 'x^2+5x-36'),
           ('(x-3)*(x-8)', 'x^2-11x+24'), ('(2x+1)*(x+7)', '2x^2+15x+7'), ('(x+2y)*(3x+y)', '3x^2+7xy+2y^2'),
           ('(3x-2)*(2x-5)', '6x^2-19x+10')]
    for t, (a, b) in zip('abcdefghij', L25):
        gleich('25' + t, a, b)
    for t, (a, b) in zip('efghij', [('(x+2)*(x+6)', 'x^2+6x+2x+12'), ('(x-4)*(x+9)', 'x^2+9x-4x-36'),
            ('(x-3)*(x-8)', 'x^2-8x-3x+24'), ('(2x+1)*(x+7)', '2x^2+14x+x+7'), ('(x+2y)*(3x+y)', '3x^2+xy+6xy+2y^2'),
            ('(3x-2)*(2x-5)', '6x^2-15x-4x+10')]):
        gleich('25' + t + ' Zwischen', a, b)
    gleich('26a', '(x+4)*(x+6)', 'x^2+10x+24'); wahr('26a Vorgabe falsch', expand(P('(x+4)*(x+6)') - P('x^2+24')) != 0, True)
    gleich('26b', '(x-5)*(x-2)', 'x^2-7x+10'); wahr('26b Vorgabe falsch', expand(P('(x-5)*(x-2)') - P('x^2-7x-10')) != 0, True)
    gleich('26c', '(x+7)*(x+1)', 'x^2+8x+7'); wahr('26c Vorgabe falsch', expand(P('(x+7)*(x+1)') - P('x^2+15x')) != 0, True)
    gleich('27a Summe Teilflächen', '(x+3)*(x+2)', 'x*x+3*x+x*2+3*2')
    gleich('27b richtig', '(x+3)*(x+2)', 'x^2+5x+6')
    gleich('28a', '(x+3)*(x-2)', 'x^2+x-6')
    gleich('28b', '(x+3)*(x-2)-x^2', 'x-6')
    gleich('28c x=4', '(x+3)*(x-2)-x^2', '-2', {x: 4}); gleich('28c x=10', '(x+3)*(x-2)-x^2', '4', {x: 10})

def ist_quadrat(ausdruck):
    """(A)*(A) oder (A)^2 bzw. A*B mit A == B"""
    roh = parse_expr(ausdruck, local_dict=LOC, transformations=TR, evaluate=False)
    if roh.is_Pow and roh.exp == 2:
        return True
    if roh.is_Mul and len(roh.args) == 2:
        return expand(P(str(roh.args[0])) - P(str(roh.args[1]))) == 0
    return False

def formel(ausdruck):
    """welche binomische Formel: erste/zweite/dritte/keine (Klammern mit x-Glied und Zahl)"""
    roh = parse_expr(ausdruck, local_dict=LOC, transformations=TR, evaluate=False)
    if roh.is_Pow:
        A = B = roh.base
    else:
        A, B = roh.args
    A, B = expand(A), expand(B)
    if expand(A - B) == 0:
        # gleiches Vorzeichen der Glieder -> erste, verschiedenes -> zweite
        c = A.as_ordered_terms()
        return 'erste' if all(t.could_extract_minus_sign() == c[0].could_extract_minus_sign() for t in c) else 'zweite'
    if len(expand(A * B).as_ordered_terms()) == 2:  # Mittelglied fällt weg
        return 'dritte'
    return 'keine'

def e4():
    for t, (a, b) in zip('abcde', [('(x+6)^2', True), ('(x+6)*(x-6)', False), ('(y-2)*(y-2)', True), ('(z+5)*(5+z)', True), ('(2x+1)*(x+2)', False)]):
        wahr('29' + t, ist_quadrat(a), b)
    for t, (a, b) in zip('abcde', [('(x+8)^2', 'erste'), ('(y-9)^2', 'zweite'), ('(x+4)*(x-4)', 'dritte'), ('(x+2)*(x+7)', 'keine'), ('(z-1)*(z-1)', 'zweite')]):
        f = formel(a); zeilen.append(('30' + t, f, b, f == b))
    # 31: a und b so, dass (a+b)^2 bzw. (a-b)^2 den Term ergibt
    for t, (term, a, b, vz) in zip('abcde', [('(x+9)^2', 'x', '9', 1), ('(y-4)^2', 'y', '4', -1), ('(3x+1)^2', '3x', '1', 1), ('(5+2y)^2', '5', '2y', 1), ('(4x-7y)^2', '4x', '7y', -1)]):
        wahr('31' + t, expand(P(term) - (P(a) + vz * P(b))**2) == 0, True)
    L32 = [('(x+4)^2', 'x^2+8x+16'), ('(x+1)^2', 'x^2+2x+1'), ('(y+6)^2', 'y^2+12y+36'), ('(x+10)^2', 'x^2+20x+100'),
           ('(x-9)^2', 'x^2-18x+81'), ('(x+11)*(x-11)', 'x^2-121'), ('(x+3)*(x-8)', 'x^2-5x-24')]
    for t, (a, b) in zip('abcdefg', L32):
        gleich('32' + t, a, b)
    gleich('32g Zwischen', '(x+3)*(x-8)', 'x^2-8x+3x-24')
    L33 = [('(3x+4)^2', '9x^2+24x+16'), ('(x-5y)^2', 'x^2-10xy+25y^2'), ('2*(x+6)^2', '2x^2+24x+72'),
           ('-(x-8)^2', '-x^2+16x-64'), ('(y-4)^2-10', 'y^2-8y+6'), ('(x-6)^2-2*(3x-4)+7x', 'x^2-11x+44')]
    for t, (a, b) in zip('abcdef', L33):
        gleich('33' + t, a, b)
    gleich('33f Zwischen', '(x-6)^2-2*(3x-4)+7x', 'x^2-12x+36-6x+8+7x')
    for t, (a, b) in zip('abcd', [('(x+2)^2-1', 'x^2+4x+3'), ('(x+1)^2+7', 'x^2+2x+8'), ('(x-4)^2+2', 'x^2-8x+18'), ('(x+6)^2-11', 'x^2+12x+25')]):
        gleich('34' + t, a, b)
    for t, (a, b) in zip('abcdef', [('21^2', '441'), ('51^2', '2601'), ('19^2', '361'), ('98^2', '9604'), ('32*28', '896'), ('45*55', '2475')]):
        gleich('35' + t, a, b)
    for t, (a, b) in zip('abcdef', [('(20+1)^2', '400+40+1'), ('(50+1)^2', '2500+100+1'), ('(20-1)^2', '400-40+1'), ('(100-2)^2', '10000-400+4'), ('(30+2)*(30-2)', '900-4'), ('(50-5)*(50+5)', '2500-25')]):
        gleich('35' + t + ' Weg', a, b)
    gleich('36a', '(x+6)^2', 'x^2+12x+36'); wahr('36a Vorgabe falsch', expand(P('(x+6)^2') - P('x^2+36')) != 0, True)
    gleich('36b', '(3x-2)^2', '9x^2-12x+4'); wahr('36b Vorgabe falsch', expand(P('(3x-2)^2') - P('3x^2-12x+4')) != 0, True)
    gleich('36c', '-(x+9)^2', '-x^2-18x-81'); wahr('36c Vorgabe falsch', expand(P('-(x+9)^2') - P('-x^2+18x+81')) != 0, True)
    # 37: genau eine Option gleichwertig, und zwar die angekreuzte
    for t, (term, opts, blatt) in zip('abc', [('(y+9)^2', ['y^2+81', 'y^2+18y+81', 'y^2+9y+81', 'y^2+18y+18'], 'y^2+18y+81'),
            ('(x-10)*(x+10)', ['x^2-20x-100', 'x^2-100', 'x^2+100', 'x^2-20x+100'], 'x^2-100'),
            ('(4-3y)^2', ['16-9y^2', '16-24y+9y^2', '16-12y+9y^2', '16-24y-9y^2'], '16-24y+9y^2')]):
        richtige = [o for o in opts if expand(P(term) - P(o)) == 0]
        zeilen.append(('37' + t, ' | '.join(richtige), blatt, richtige == [blatt]))
    gleich('38a links', '(6+2)^2', '64'); gleich('38a rechts', '6^2+2^2', '40'); gleich('38a Mittelglied', '2*6*2', '24')
    gleich('38b', '(x+2)^2', 'x^2+4x+4')
    gleich('39a', '(x+12)^2', 'x^2+24x+144'); gleich('39b', '(x+12)^2-x^2', '24x+144')
    gleich('39c', '(x+12)^2-x^2', '624', {x: 20})

def binom_faktorisierbar(term):
    """lässt sich mit einer binomischen Formel faktorisieren: Faktorisierung ist Quadrat oder (A+B)(A-B)"""
    f = factor(P(term))
    if f.is_Pow and f.exp == 2:
        return True
    if f.is_Mul:
        fs = [a for a in f.args if not a.is_number]
        if len(fs) == 2 and expand(fs[0] * fs[1]).is_Add and len(expand(fs[0] * fs[1]).args) == 2:
            return True
    return False

def e5():
    from sympy import integer_nthroot
    def quadrat(term):
        # Quadrat = Quadratzahl mal (1 oder Variable hoch gerader Zahl)
        c, rest = P(term).as_coeff_Mul()
        if not (c.is_integer and c > 0 and integer_nthroot(int(c), 2)[1]):
            return False
        if rest == 1:
            return True
        return rest.is_Pow and rest.exp.is_integer and rest.exp % 2 == 0
    for t, (a, b) in zip('abcdefg', [('y^2', True), ('64', True), ('25x^2', True), ('12x', False), ('18', False), ('3x^2', False), ('100y^2', True)]):
        wahr('40' + t, quadrat(a), b)
    # 41 Quadrate und Mittelglied: Mittelglied = +-2*sqrt(Q1)*sqrt(Q2), Summe = Term
    for t, (term, q1, q2, m) in zip('abcde', [('y^2+16y+64', 'y^2', '64', '16y'), ('36+12x+x^2', '36', 'x^2', '12x'),
            ('9x^2-24x+16', '9x^2', '16', '-24x'), ('49-14y+y^2', '49', 'y^2', '-14y'), ('81x^2+18x+1', '81x^2', '1', '18x')]):
        wahr('41' + t, expand(P(q1) + P(q2) + P(m) - P(term)) == 0, True)
    L42 = [('x^2-16', '(x+4)*(x-4)'), ('x^2-36', '(x+6)*(x-6)'), ('y^2-100', '(y+10)*(y-10)'), ('x^2-1', '(x+1)*(x-1)'),
           ('x^2+12x+36', '(x+6)^2'), ('x^2-16x+64', '(x-8)^2'), ('9x^2+30x+25', '(3x+5)^2'), ('2x^2-72', '2*(x+6)*(x-6)'),
           ('x^2-20x+100', '(x-10)^2'), ('5x^3-40x^2+80x', '5x*(x-4)^2')]
    for t, (a, b) in zip('abcdefghij', L42):
        produkt('42' + t, a, b)
    gleich('42h Zwischen', '2x^2-72', '2*(x^2-36)'); gleich('42j Zwischen', '5x^3-40x^2+80x', '5x*(x^2-8x+16)')
    for t, (g, b) in zip('abcd', [('x^2-81=0', '-9;9'), ('x^2-144=0', '-12;12'), ('x^2-18x+81=0', '9'), ('3x^2-48=0', '-4;4')]):
        loesung('43' + t, g, b)
    L44 = [('x^2+4x+7', '(x+2)^2+3'), ('x^2+8x+20', '(x+4)^2+4'), ('x^2-12x+40', '(x-6)^2+4'), ('x^2+16x+50', '(x+8)^2-14')]
    for t, (a, b) in zip('abcd', L44):
        gleich('44' + t, a, b)
    wahr('45a Vorgabe falsch', expand(P('(x+8)*(x-8)') - P('x^2+64')) != 0, True)
    wahr('45a nicht faktorisierbar', binom_faktorisierbar('x^2+64'), False)
    wahr('45b Vorgabe falsch', expand(P('(x+4)^2') - P('x^2+9x+16')) != 0, True)
    wahr('45b nicht binomisch', binom_faktorisierbar('x^2+9x+16'), False)
    wahr('45c Vorgabe falsch', expand(P('2*(x^2-32)') - P('2x^2-32')) != 0, True)
    produkt('45c', '2x^2-32', '2*(x+4)*(x-4)')
    for t, (a, b) in zip('abcdef', [('x^2+22x+121', True), ('x^2+36', False), ('y^2-169', True), ('x^2+5x+4', False), ('4x^2-20x+25', True), ('x^2-8x-16', False)]):
        wahr('46' + t, binom_faktorisierbar(a), b)
    produkt('46a Form', 'x^2+22x+121', '(x+11)^2'); produkt('46c Form', 'y^2-169', '(y+13)*(y-13)'); produkt('46e Form', '4x^2-20x+25', '(2x-5)^2')
    produkt('47a', 'x^2-100', '(x+10)*(x-10)'); wahr('47a x^2+100', binom_faktorisierbar('x^2+100'), False)
    gleich('47b Mittelglied müsste', '2*x*6', '12x'); wahr('47b', binom_faktorisierbar('x^2+10x+36'), False)
    produkt('48a', 'x^2+18x+81', '(x+9)^2'); gleich('48b', '4*(x+9)', '4x+36')
    gleich('48c Seite', 'x+9', '12', {x: 3}); gleich('48c Fläche', 'x^2+18x+81', '144', {x: 3})

TEILE = {'zone': zone, 'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'e5': e5}

if __name__ == '__main__':
    teil = sys.argv[1]
    TEILE[teil]()
    ab = sum(1 for z_ in zeilen if not z_[3])
    with open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8') as f:
        for nr, sw, bw, ok in zeilen:
            f.write(f'{nr}\tSkript: {sw}\tBlatt: {bw}\t{"OK" if ok else "ABWEICHUNG"}\n')
        f.write(f'Abweichungen: {ab}\n')
    print(f'{teil}: {len(zeilen)} Werte, Abweichungen: {ab}')
    for nr, sw, bw, ok in zeilen:
        if not ok:
            print('ABWEICHUNG', nr, sw, bw)
