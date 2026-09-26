# pruef.py – rechnet die Lösungen je Datei unabhängig nach (5.1 a)
# Aufruf: python pruef.py zone|e1|e2|e3|e4  -> schreibt pruef_out_<datei>.txt
# Blattwerte sind aus dem Lösungsquelltext (<datei>_l.tex) übertragen.
import sys
import sympy as sp
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations,
                                        implicit_multiplication_application,
                                        convert_xor)

x, t = sp.symbols('x t')
TR = standard_transformations + (implicit_multiplication_application, convert_xor)
LOC = {'x': x, 't': t, 'pi': sp.pi, 'sqrt': sp.sqrt}


def P(s):
    return parse_expr(s, transformations=TR, local_dict=LOC)


zeilen = []
fehler = 0
eigene_gleichungen = []   # für die Sperrprüfung (2.1)


def aus(nr, skript, blatt, ok):
    global fehler
    if not ok:
        fehler += 1
    zeilen.append(f"{nr:8s} | Skript: {skript} | Blatt: {blatt} | {'OK' if ok else 'ABWEICHUNG'}")


def fmt(v):
    v = sp.nsimplify(v) if isinstance(v, (int, float)) else v
    try:
        f = float(v)
        return str(sp.nsimplify(v)) if abs(f - round(f)) < 1e-12 else f"{f:.4f}"
    except TypeError:
        return str(v)


def num(nr, ausdruck, blatt, tol=None):
    """Zahlenwert eines Terms gegen den Blattwert; tol aus Rundung des Blattwerts."""
    v = P(ausdruck) if isinstance(ausdruck, str) else ausdruck
    v = float(sp.N(v))
    if tol is None:
        s = str(blatt)
        tol = 0.5 * 10 ** (-(len(s.split('.')[1]))) + 1e-9 if '.' in s else 1e-9
    aus(nr, f"{v:.4f}".rstrip('0').rstrip('.'), blatt, abs(v - blatt) <= tol)


def loese(nr, gleichung, blatt, var=x, tol=None, sperr=True):
    """reelle Lösungen einer Gleichung 'links = rechts' gegen die Blattliste ([] = keine Lösung)."""
    l, r = gleichung.split('=')
    ex = sp.expand(P(l) - P(r))
    if sperr:
        eigene_gleichungen.append((nr, gleichung, ex))
    sol = sorted(float(s) for s in sp.solve(sp.Eq(ex, 0), var) if s.is_real)
    bl = sorted(blatt)
    if tol is None:
        tol = max([0.5 * 10 ** (-len(str(b).split('.')[1])) if '.' in str(b) else 1e-9 for b in bl] + [1e-9]) + 1e-9
    ok = len(sol) == len(bl) and all(abs(a - b) <= tol for a, b in zip(sol, bl))
    aus(nr, [round(s, 4) for s in sol] if sol else 'keine', bl if bl else 'keine', ok)
    return sol


def einsetzen(nr, gleichung, wert, blatt):
    """wA/fA durch Einsetzen."""
    l, r = gleichung.split('=')
    L = P(l).subs(x, wert)
    R = P(r).subs(x, wert)
    s = 'wA' if sp.simplify(L - R) == 0 else 'fA'
    aus(nr, f"{s} ({L} / {R})", blatt, s == blatt)


def term(nr, links, blatt):
    """Termumformung: links und Blattterm müssen gleich sein."""
    ok = sp.expand(P(links) - P(blatt)) == 0
    aus(nr, str(sp.expand(P(links))), blatt, ok)


def faktor(nr, links, blatt):
    """Ausklammern/Faktorisieren: gleich und Blattform ist ein Produkt."""
    b = parse_expr(blatt, transformations=TR, local_dict=LOC, evaluate=False)
    ok = sp.expand(P(links) - b) == 0 and isinstance(b, sp.Mul)
    aus(nr, str(sp.factor(P(links))), blatt, ok)


def diskr(nr, gleichung, wert_blatt, anzahl_blatt):
    """Wert unter der Wurzel (p/2)^2 - q der normierten Gleichung und Zahl der Lösungen."""
    l, r = gleichung.split('=')
    ex = sp.Poly(sp.expand(P(l) - P(r)), x)
    a, b, c = [ex.coeff_monomial(x ** k) for k in (2, 1, 0)]
    p, q = b / a, c / a
    D = (p / 2) ** 2 - q
    n = 2 if D > 0 else (1 if D == 0 else 0)
    eigene_gleichungen.append((nr, gleichung, sp.expand(P(l) - P(r))))
    aus(nr, f"D = {float(D):g}, {n} Lösung(en)", f"D = {wert_blatt}, {anzahl_blatt}",
        abs(float(D) - wert_blatt) < 1e-9 and n == anzahl_blatt)


# Sperrliste (2.1): ganze Gleichungen aus Kasten, Beispiel, Original und Grundvorstellung des Eintrags
SPERR = ["x^2=36", "x^2=0", "x^2=-36", "(x+4)^2=36", "(x+4)^2=0", "x^2-7x=0",
         "(x+3)(x-9)=0", "x(x+8)=20", "3x^2+24x-60=0", "x^2+8x-20=0", "x^2+8x+16=0",
         "x^2+8x+20=0", "(x+7)^2=0", "(x+8)^2=16", "x^2+1=0", "x(x+5)=-6",
         "2x^2+8x+6=0", "x^2+4x+3=0", "x^2-6x+7=0", "-x^2-2x+5=-10", "x^2+2x-15=0",
         "x^2-x-2=0", "(x-2)^2-4=-2x+3", "x^2=9", "x^2=49", "x^2=-25", "x^2=7x",
         "x(x+5)=-6", "x^2+2x-1=3x+1", "x^2=36", "x+5=12", "x+17=12", "5x=15", "-x=5"]
SP = []
for g in SPERR:
    l, r = g.split('=')
    SP.append((g, sp.expand(P(l) - P(r))))


def sperrpruefung():
    global fehler
    treffer = 0
    for nr, g, ex in eigene_gleichungen:
        for sg, sex in SP:
            if sp.expand(ex - sex) == 0 or sp.expand(ex + sex) == 0:
                treffer += 1
                zeilen.append(f"{nr:8s} | Sperre: {g} ist {sg} aus dem Eintrag | ABWEICHUNG")
    fehler += treffer
    zeilen.append(f"Sperrprüfung: {len(eigene_gleichungen)} Gleichungen gegen {len(SP)} gesperrte, Treffer {treffer}")


def zone():
    # 1 Quadrieren
    for n, e, b in [('1a', '6^2', 36), ('1b', '10^2', 100), ('1c', '(-8)^2', 64),
                    ('1d', '2.5^2', 6.25), ('1e', '(-0.5)^2', 0.25)]:
        num(n, e, b)
    # 2 Klammer, Punkt vor Strich
    for n, e, b in [('2a', '3*(2+4)', 18), ('2b', '20-4*3', 8), ('2c', '(-2)*6', -12),
                    ('2d', '(-4)*(-4+9)', -20), ('2e', '2*(-3)^2-10', 8)]:
        num(n, e, b)
    # 3 lineare Gleichungen
    for n, g, b in [('3a', 'x+4=10', [6]), ('3b', '3x=12', [4]), ('3c', 'x-2.5=4', [6.5]),
                    ('3d', 'x+6=0', [-6]), ('3e', '2x-5=11', [8]), ('3f', '-x=7', [-7])]:
        loese(n, g, b)
    # 4 Einsetzen
    for n, g, w, b in [('4a', 'x+5=8', 3, 'wA'), ('4b', '4x=10', 2, 'fA'),
                       ('4c', '4x+1=3', sp.Rational(1, 2), 'wA'), ('4d', '5-x=3', -2, 'fA'),
                       ('4e', '2x-1=-7', -3, 'wA')]:
        einsetzen(n, g, w, b)
    # 5 Wurzeln
    for n, e, b in [('5a', 'sqrt(49)', 7), ('5b', 'sqrt(100)', 10), ('5c', 'sqrt(0.64)', 0.8),
                    ('5d', 'sqrt(196)', 14), ('5f', 'sqrt(7)', 2.65)]:
        num(n, e, b)
    aus('5e', 'sqrt(-9) nicht reell' if not P('sqrt(-9)').is_real else 'reell', 'gibt es nicht',
        not P('sqrt(-9)').is_real)
    # 6 Scheitel: y = (x-d)^2+e -> Minimum der Parabel
    for n, e, b in [('6a', '(x-2)^2+1', (2, 1)), ('6b', '(x-4)^2', (4, 0)),
                    ('6c', 'x^2-5', (0, -5)), ('6d', '(x+3)^2-2', (-3, -2))]:
        f = P(e)
        xs = sp.solve(sp.diff(f, x), x)[0]
        s = (xs, f.subs(x, xs))
        aus(n, f"S{s}", f"S{b}", s == b)
    # 7 Ausmultiplizieren
    for n, e, b in [('7a', '2*(x+5)', '2x+10'), ('7b', 'x*(x+3)', 'x^2+3x'),
                    ('7c', 'x*(x-6)', 'x^2-6x'), ('7d', '(x+6)^2', 'x^2+12x+36'),
                    ('7e', '(x-9)^2', 'x^2-18x+81')]:
        term(n, e, b)
    # 8 Ausklammern
    for n, e, b in [('8a', '4x+8', '4*(x+2)'), ('8b', 'x^2+3x', 'x*(x+3)'),
                    ('8c', 'x^2-9x', 'x*(x-9)'), ('8d', '2x^2+6x', '2*x*(x+3)'),
                    ('8e', 'x^2-x', 'x*(x-1)')]:
        faktor(n, e, b)
    # 9 Ordnen
    for n, e, b in [('9a', '3+x^2+2x', 'x^2+2x+3'), ('9b', 'x^2+4x+3x+1', 'x^2+7x+1'),
                    ('9c', '5x-2+x^2-6', 'x^2+5x-8'), ('9d', '2x-x^2+4', '-x^2+2x+4'),
                    ('9e', 'x^2-3x+10-12+x', 'x^2-2x-2')]:
        term(n, e, b)
    # 10 Fehler finden, 11 selbst rechnen
    term('10', '(x+5)^2-30', 'x^2+10x-5')
    aus('10 Vorgabe', str(sp.expand(P('(x+5)^2-30'))), 'x^2-5 (Vorgabe falsch)',
        sp.expand(P('(x+5)^2-30') - P('x^2-5')) != 0)
    for n, e, b in [('11a', '(x+2)^2-7', 'x^2+4x-3'), ('11b', '(x-3)^2+4x', 'x^2-2x+9'),
                    ('11c', '(x-1)^2-2x+5', 'x^2-4x+6')]:
        term(n, e, b)


def e1():
    r10 = 10 ** 0.5
    for n, g, b in [('14a', 'x^2=16', [4, -4]), ('14b', 'x^2=81', [9, -9]), ('14c', 'x^2=4', [2, -2]),
                    ('14d', 'x^2=144', [12, -12]), ('14e', 'x^2=10', [3.16, -3.16]), ('14f', 'x^2=-16', []),
                    ('15a', 'x^2-4=12', [4, -4]), ('15b', 'x^2+3=67', [8, -8]), ('15c', '2x^2=50', [5, -5]),
                    ('15d', '3x^2+1=13', [2, -2]), ('15e', '2x^2+9=1', []), ('15f', '4x^2+3=3', [0]),
                    ('16a', '(x-2)^2=9', [5, -1]), ('16b', '(x-1)^2=25', [6, -4]), ('16c', '(x-5)^2=4', [7, 3]),
                    ('16d', '(x-3)^2=1', [4, 2]), ('16e', '(x+2)^2=25', [3, -7]), ('16f', '(x+5)^2=0', [-5]),
                    ('18a', '(x+1)^2=4', [1, -3]), ('18b', '(x+1)^2=1', [0, -2]), ('18c', '(x+1)^2=0', [-1]),
                    ('18d', '(x+1)^2=-2', []),
                    ('20 A1', '(x-6)^2=0', [6]), ('20 A2', '(x+6)^2=16', [-2, -10]),
                    ('21a', 'x^2=64', [8, -8]), ('21b', '(x+9)^2=4', [-7, -11]), ('21c', 'x^2=-81', []),
                    ('22c', '(x-9)^2=0', [9])]:
        loese(n, g, b)
    num('14e Wurzel', 'sqrt(10)', 3.16)
    aus('20 A2 Vorgabe', '2 und 10 keine Lösungen', 'falsch', all(P('(x+6)^2-16').subs(x, v) != 0 for v in (2, 10)))
    # 17 Einsetzen
    for n, g, w, b in [('17a', 'x^2+1=50', 7, 'wA'), ('17b', 'x^2+1=50', -7, 'wA'), ('17c', '(x-1)^2=9', 3, 'fA'),
                       ('17d', '(x+5)^2=9', -2, 'wA'), ('17e', '3x^2-5=-8', -1, 'fA')]:
        einsetzen(n, g, w, b)
    # 18 Graph: Anzahl der Schnittpunkte der Parabel mit y=c = Zahl der Lösungen (oben geprüft)
    # 19 Beispielwerte: Zahl der Lösungen
    for n, g, anz in [('19a', '(x-3)^2=0', 1), ('19b', '(x+2)^2=9', 2), ('19c', 'x^2+5=1', 0),
                      ('19d', '3x^2=-3', 0), ('19e', '(x-1)^2=-4', 0), ('20b', 'x^2=-4', 0)]:
        l, r = g.split('=')
        s = [v for v in sp.solve(sp.Eq(P(l), P(r)), x) if v.is_real]
        aus(n, f"{len(s)} Lösung(en)", f"{anz}", len(s) == anz)
    # 21 Vorgaben sind falsch
    aus('21a Vorgabe', 'x=8 allein unvollständig', 'Fehler', len(sp.solve(P('x^2-64'), x)) == 2)
    aus('21b Vorgabe', str(sp.solve(P('(x+9)^2-4'), x)), '11, 7 falsch', 11 not in sp.solve(P('(x+9)^2-4'), x))
    # 23 Anwendung
    loese('23a', 'x^2=121', [11, -11])
    aus('23a Länge', 'positive Lösung 11', 11, True)
    num('23b', 'sqrt(1.44)', 1.2)
    num('23c r^2', '500/(10*pi)', 15.92)
    num('23c r', 'sqrt(500/(10*pi))', 3.99)


def e2():
    # 25 p und q (Vorstufe, Lösungsblatt)
    for n, g, pb, qb in [('25a', 'x^2+7x+2', 7, 2), ('25b', 'x^2-2x+9', -2, 9), ('25c', 'x^2+5x-1', 5, -1),
                         ('25d', 'x^2-x-20', -1, -20), ('25e', 'x^2-11', 0, -11)]:
        po = sp.Poly(P(g), x)
        aus(n, f"p={po.coeff_monomial(x)}, q={po.coeff_monomial(1)}", f"p={pb}, q={qb}",
            po.coeff_monomial(x) == pb and po.coeff_monomial(1) == qb)
    # 26 Vorzahl
    for n, g, b in [('26a', 'x^2+5x-3', 1), ('26b', '2x^2+4x-7', 2), ('26c', '-x^2+3x+4', -1),
                    ('26d', '0.5x^2-x+2', 0.5), ('26e', 'x^2-9x+1', 1)]:
        a = sp.Poly(P(g), x).coeff_monomial(x ** 2)
        aus(n, f"Vorzahl {a}", f"{'nicht teilen' if b == 1 else 'teilen durch ' + str(b)}", abs(float(a) - b) < 1e-12)
    # 24 Lösungsweg: kein x-Glied -> Wurzel; quadrierte Klammer -> rückwärts; sonst Formel
    for n, g, b in [('24a', 'x^2-7x+10=0', 'Formel'), ('24b', 'x^2=30', 'Wurzel'), ('24c', '(x-4)^2=5', 'rückwärts'),
                    ('24d', '3x^2-12=0', 'Wurzel'), ('24e', 'x^2+x=6', 'Formel')]:
        l, r = g.split('=')
        ex = sp.expand(P(l) - P(r))
        weg = 'rückwärts' if '(' in l else ('Wurzel' if sp.Poly(ex, x).coeff_monomial(x) == 0 else 'Formel')
        aus(n, weg, b, weg == b)
    for n, g, b in [('27a', 'x^2+6x+8=0', [-2, -4]), ('27b', 'x^2+10x+16=0', [-2, -8]),
                    ('27c', 'x^2+6x+5=0', [-1, -5]), ('27d', 'x^2+10x+21=0', [-3, -7]),
                    ('28a', 'x^2-4x-12=0', [6, -2]), ('28b', 'x^2+3x-10=0', [2, -5]),
                    ('28c', 'x^2-4x+1=0', [3.73, 0.27]), ('28d', 'x^2+x-3=0', [1.30, -2.30]),
                    ('28e', 'x^2-8x+14=0', [5.41, 2.59]),
                    ('29a', 'x^2+2x=8', [2, -4]), ('29b', 'x^2=6x-5', [5, 1]), ('29c', 'x^2+4=5x', [4, 1]),
                    ('29d', 'x^2+9x-5=3x+11', [2, -8]),
                    ('30a', '2x^2-4x-6=0', [3, -1]), ('30b', '3x^2+9x-12=0', [1, -4]),
                    ('30c', '-x^2+6x-8=0', [4, 2]), ('30d', '0.5x^2-x-4=0', [4, -2]),
                    ('30e', '3x^2-3x-36=0', [4, -3]),
                    ('31a', 'x*(x+4)=12', [2, -6]), ('31b', '(x+1)^2=3x+7', [3, -2]),
                    ('31c', '(x-3)^2-1=-2x+8', [4, 0]), ('31d', '-x^2+6x-1=-8', [7, -1]),
                    ('32a', 'x^2+6x+9=0', [-3]), ('32b', 'x^2-10x+25=0', [5]), ('32c', 'x^2-x+0.25=0', [0.5]),
                    ('32d', '4x^2+12x+9=0', [-1.5]),
                    ('33a', 'x^2+2x+5=0', []), ('33b', 'x^2-6x+10=0', []), ('33c', 'x^2+x+1=0', []),
                    ('33d', '2x^2+4x+7=0', []),
                    ('36a', 'x^2-20=5', [5, -5]), ('36b', 'x^2+2x-24=0', [4, -6]), ('36c', '(x+3)^2=16', [1, -7]),
                    ('36d', 'x^2-6x=16', [8, -2]),
                    ('37a', '2x^2+16x+14=0', [-1, -7]), ('37b', 'x^2-10x+9=0', [9, 1]), ('37c', 'x^2-8x+12=0', [6, 2]),
                    ('38a', '2x^2+6x-8=0', [1, -4]),
                    ('39a', 'x^2-2x-1=x+3', [4, -1])]:
        loese(n, g, b)
    # Zwischenwerte (Wert unter der Wurzel) aus den Lösungen
    for n, g, w in [('28b D', 'x^2+3x-10=0', 12.25), ('28d D', 'x^2+x-3=0', 3.25), ('33d D', '2x^2+4x+7=0', -2.5),
                    ('33c D', 'x^2+x+1=0', -0.75)]:
        l, r = g.split('=')
        po = sp.Poly(sp.expand(P(l) - P(r)), x)
        a, b, c = [po.coeff_monomial(x ** k) for k in (2, 1, 0)]
        D = (b / a / 2) ** 2 - c / a
        aus(n, float(D), w, abs(float(D) - w) < 1e-9)
    for n, g, w, k in [('34a', 'x^2+4x+1=0', 3, 2), ('34b', 'x^2-12x+36=0', 0, 1), ('34c', 'x^2+2x+4=0', -3, 0),
                       ('34d', 'x^2-3x+1=0', 1.25, 2), ('34e', 'x^2+5x+7=0', -0.75, 0), ('34f', 'x^2-2x-1=0', 2, 2)]:
        diskr(n, g, w, k)
    for n, g, w, b in [('35a', 'x^2+2x-8=0', 2, 'wA'), ('35b', 'x^2-5x+4=0', -1, 'fA'), ('35c', 'x^2-2x-3=0', -1, 'wA'),
                       ('35d', 'x^2+x-6=0', 3, 'fA'), ('35e', 'x^2+3x-4=0', -4, 'wA')]:
        einsetzen(n, g, w, b)
    # 37 Vorgaben sind falsch
    aus('37b Vorgabe', 'x=-1 in x^2-10x+9', '≠ 0', P('x^2-10x+9').subs(x, -1) != 0)
    aus('37c Vorgabe', '4±sqrt(28) keine Lösung', 'falsch', P('x^2-8x+12').subs(x, 4 + sp.sqrt(28)) != 0)
    # 39 y-Werte
    for xv, yb in [(4, 7), (-1, 2)]:
        aus(f'39b x={xv}', P('x+3').subs(x, xv), yb, P('x+3').subs(x, xv) == yb and P('x^2-2x-1').subs(x, xv) == yb)
    # Parabel im Graphen: y=(x-1)^2-2 ist y=x^2-2x-1
    term('39 Graph', '(x-1)^2-2', 'x^2-2x-1')


def e3():
    # 40 Auswahl im Kontext: Länge/Anzahl/natürliche Zahl -> positiv; Zahl -> beide
    for n, sol, art, b in [('40a', [9, -9], 'Länge', '9'), ('40b', [4, -4], 'Zahl', 'beide'),
                           ('40c', [6, -10], 'Länge', '6'), ('40d', [-15, 12], 'Anzahl', '12'),
                           ('40e', [7, -8], 'natürlich', '7')]:
        s = 'beide' if art == 'Zahl' else str([v for v in sol if v > 0][0])
        aus(n, s, b, s == b)
    for n, g, b in [('41a', 'x^2=169', [13, -13]), ('41b', 'x^2=400', [20, -20]), ('41c', '2x^2=128', [8, -8]),
                    ('41d', 'x^2-10=90', [10, -10]), ('42a', 'x^2+15=96', [9, -9]), ('42b', '3x^2=75', [5, -5]),
                    ('42c', 'x*(x+1)=56', [7, -8]), ('42d', 'x*(x+1)=132', [11, -12]),
                    ('43b', 'x*(x+3)=40', [5, -8]), ('44a', '(x+4)^2=196', [10, -18]),
                    ('44b', '(x+4)*(x-2)=55', [7, -9]), ('45a', 'x*(x+5)=24', [3, -8]),
                    ('45b', 'x*(x+2)=48', [6, -8])]:
        loese(n, g, b)
    num('43b D', '1.5^2+40', 42.25)
    num('43d Probe', '5*8', 40)
    num('44b Probe', '(7+4)*(7-2)', 55)
    num('45a Länge', '3+5', 8)
    num('45b Länge', '6+2', 8)
    loese('45b Vorgabe Mia', '2x+2*(x+2)=48', [11], sperr=False)
    aus('45b Vorgabe', '11*13=143', '≠ 48', 11 * 13 != 48)
    for n, a, b in [('42c Paare', (7 * 8, -8 * -7), 56), ('42d Paar', (11 * 12,), 132)]:
        aus(n, a, b, all(v == b for v in a))
    aus('46b', '15^2 = (-15)^2 = 225', 225, 15 ** 2 == 225 and (-15) ** 2 == 225)


def e4():
    # 47 rechts null?
    for n, g, b in [('47a', '(x-3)*(x+1)=0', 'gilt'), ('47b', 'x*(x+2)=8', 'gilt nicht'), ('47c', '(x+4)*(x-4)=0', 'gilt'),
                    ('47d', 'x*(x-5)=-4', 'gilt nicht'), ('47e', '2x*(x-1)=0', 'gilt')]:
        s = 'gilt' if P(g.split('=')[1]) == 0 else 'gilt nicht'
        aus(n, s, b, s == b)
    for n, g, b in [('48a', '(x-2)*(x-5)=0', [2, 5]), ('48b', '(x-1)*(x-6)=0', [1, 6]), ('48c', '(x-3)*(x-4)=0', [3, 4]),
                    ('48d', '(x-7)*(x-2)=0', [7, 2]), ('48e', '(x+5)*(x-1)=0', [-5, 1]), ('48f', 'x*(x+6)=0', [0, -6]),
                    ('48g', '(x-8)*(x-8)=0', [8]),
                    ('50a', 'x^2+4x=0', [0, -4]), ('50b', 'x^2+9x=0', [0, -9]), ('50c', 'x^2-x=0', [0, 1]),
                    ('50d', '3x^2-12x=0', [0, 4]), ('50e', 'x^2=5x', [0, 5]),
                    ('51a', 'x*(x+2)=35', [5, -7]), ('51b', '(x-2)*(x+3)=14', [4, -5]), ('51c', 'x*(x-3)=10', [5, -2]),
                    ('52a', 'x^2+8x+15=0', [-3, -5]), ('52b', 'x^2-7x+12=0', [3, 4]), ('52c', 'x^2+2x-3=0', [-3, 1]),
                    ('52d', '2x^2+14x+20=0', [-2, -5]),
                    ('53a', 'x^2=3x', [0, 3]), ('53b', '(x+2)*(x-6)=0', [-2, 6]), ('53c', 'x*(x+1)=12', [3, -4]),
                    ('54b', 'x^2=6x', [0, 6])]:
        loese(n, g, b)
    for n, e, b in [('52a', 'x^2+8x+15', '(x+3)*(x+5)'), ('52b', 'x^2-7x+12', '(x-3)*(x-4)'),
                    ('52c', 'x^2+2x-3', '(x+3)*(x-1)'), ('52d', '2x^2+14x+20', '2*(x+2)*(x+5)'),
                    ('50a', 'x^2+4x', 'x*(x+4)'), ('50d', '3x^2-12x', '3*x*(x-4)')]:
        faktor(n + ' Faktoren', e, b)
    for n, g, w, b in [('49a', '(x-3)*(x+2)=0', 3, 'wA'), ('49b', 'x*(x+4)=-4', -2, 'wA'), ('49c', 'x*(x+4)=-4', 2, 'fA'),
                       ('49d', '(x+3)*(x-2)=-6', -1, 'wA'), ('49e', '(x-4)*(x+2)=9', 1, 'fA')]:
        einsetzen(n, g, w, b)
    opt = {w: P('x*(x+7)').subs(x, w) for w in (2, 5, -2, -10)}
    richtig = [w for w, v in opt.items() if v == -10]
    aus('49f', f"erfüllt: {richtig} (Werte {opt})", [-2], richtig == [-2])
    loese('49f Gl.', 'x*(x+7)=-10', [-2, -5])
    # 55 Ball
    t_ = sp.symbols('t')
    h = 15 * t_ - 5 * t_ ** 2
    aus('55a', str(sp.factor(h)), '5t*(3-t)', sp.expand(h - 5 * t_ * (3 - t_)) == 0)
    s = sorted(sp.solve(h, t_))
    aus('55b', s, [0, 3], s == [0, 3])


if __name__ == '__main__':
    teil = sys.argv[1]
    globals()[teil]()
    sperrpruefung()
    zeilen.append(f"Abweichungen: {fehler}")
    text = "\n".join(zeilen)
    with open(f"pruef_out_{teil}.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)
