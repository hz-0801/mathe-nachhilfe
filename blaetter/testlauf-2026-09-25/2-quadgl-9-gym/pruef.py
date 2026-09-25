# pruef.py – rechnet die Lösungen einer Einheit unabhängig nach (5.1 a)
# Aufruf: python pruef.py zone|e1|e2|e3|e4   → pruef_out_<teil>.txt
# Blattwerte sind aus dem Lösungsquelltext (<teil>_l.tex) abgeschrieben.
import sys, re, math
from sympy import symbols, solve, sqrt, Rational as R, expand, factor, simplify, sympify, pi, nsimplify, S

x = symbols('x')
zeilen = []
abw = 0

def zahlen(blatt):
    """'5; -5' → [5.0, -5.0]; 'keine' → []; Dezimalkomma und Unicode-Minus erlaubt."""
    b = blatt.replace('−', '-').strip()
    if b in ('keine', ''):
        return []
    return [float(t.strip().replace(',', '.')) for t in b.split(';')]

def tol_fuer(blatt):
    dez = [len(m) for m in re.findall(r',(\d+)', blatt)]
    return 0.5 * 10 ** (-max(dez)) + 1e-9 if dez else 1e-9

def reell(loes):
    out = []
    for l in loes:
        v = complex(l.evalf())
        if abs(v.imag) < 1e-12:
            out.append(v.real)
    return sorted(out)

def chk(nr, skript, blatt):
    """skript: Liste von Zahlen (Lösungsmenge) oder Zahl; blatt: Text aus dem Lösungsquelltext."""
    global abw
    if not isinstance(skript, (list, tuple)):
        skript = [skript]
    s = sorted(float(v) for v in skript)
    b = sorted(zahlen(blatt))
    t = tol_fuer(blatt)
    ok = len(s) == len(b) and all(abs(p - q) <= t for p, q in zip(s, b))
    if not ok:
        abw += 1
    zeilen.append(f"{nr:6} | Skript: {', '.join(f'{v:.6g}' for v in s) or 'keine'} | Blatt: {blatt} | {'OK' if ok else 'ABWEICHUNG'}")

def chk_bool(nr, skript, blatt):
    global abw
    ok = (skript and blatt == 'wA') or ((not skript) and blatt == 'fA')
    if not ok:
        abw += 1
    zeilen.append(f"{nr:6} | Skript: {'wA' if skript else 'fA'} | Blatt: {blatt} | {'OK' if ok else 'ABWEICHUNG'}")

def chk_term(nr, skript, blatt):
    """Termvergleich: skript und blatt als sympy-Ausdrücke in x (Blatt aus dem Lösungsquelltext)."""
    global abw
    ok = simplify(sympify(skript) - sympify(blatt)) == 0
    if not ok:
        abw += 1
    zeilen.append(f"{nr:6} | Skript: {expand(sympify(skript))} | Blatt: {blatt} | {'OK' if ok else 'ABWEICHUNG'}")

def chk_text(nr, skript, blatt):
    global abw
    ok = skript == blatt
    if not ok:
        abw += 1
    zeilen.append(f"{nr:6} | Skript: {skript} | Blatt: {blatt} | {'OK' if ok else 'ABWEICHUNG'}")

def L(gl):
    """Lösungen einer Gleichung 'links = rechts' als sortierte reelle Liste."""
    l, r = gl.split('=')
    return reell(solve(sympify(l) - sympify(r), x))

def anzahl(n):
    return {0: 'keine', 1: 'eine', 2: 'zwei'}[n]

def wert(ausdr, xv):
    return sympify(ausdr).subs(x, xv)

# --- Sperrliste (2.1, 3.6): Zahlen und Gleichungen aus Kasten, Beispielen, Originalen des Eintrags ---
SPERRZAHLEN = ['13', '15', '16', '17', '20', '26', '36', '60', '121', '169', '1{,}5', '2{,}25', '2{,}24', '1{,}59', '4{,}41']
SPERRGL = ['(x+7)^2=0', '(x+8)^2=16', 'x^2+1=0', 'x\\cdot(x+5)=-6', '2x^2+8x+6', 'x^2+4x+3', 'x^2-6x+7',
           '-x^2-2x+5=-10', 'x^2+2x-15', 'x^2-x-2', '(x-2)^2-4', 'x^2=36', '(x+4)^2=36', 'x^2-7x=0',
           '(x+3)\\cdot(x-9)', 'x^2+8x-20', '3x^2+24x-60', 'x^2+8x+16', 'x^2+8x+20', 'x\\cdot(x+8)=20',
           'x^2=9', 'x^2=49', 'x^2=-25', 'x^2=7x', '(x+13)^2', 'x+17=12', 'x+5=12', '5x=15', '(x-5)^2-11']

def sperre(datei):
    global abw
    txt = open(datei, encoding='utf-8').read()
    txt = re.sub(r'%.*', '', txt)
    txt = re.sub(r'\\(setcounter|hypertarget|gl|sgl)\{?\[?[^\]}]*[\]}]', ' ', txt)
    kompakt = re.sub(r'\s|\\,|\\;|\\ ', '', txt)
    treffer = []
    for z in SPERRZAHLEN:
        for m in re.finditer(r'(?<![\d{,.])' + re.escape(z) + r'(?![\d}]|\{,\})', txt):
            ctx = txt[max(0, m.start() - 4):m.end() + 4]
            if re.search(r'(19|20)\d\d', ctx) and len(z) == 2:
                continue  # Jahreszahl (P10 2020 …)
            treffer.append(z)
    for g in SPERRGL:
        if re.search(re.escape(g) + r'(?![\d{])', kompakt):
            treffer.append(g)
    ok = not treffer
    if not ok:
        abw += 1
    zeilen.append(f"Sperre | {datei}: {', '.join(sorted(set(treffer))) or 'keine Sperrzahl, keine Sperrgleichung'} | {'OK' if ok else 'ABWEICHUNG'}")

# ------------------------------------------------------------------------------------------------
def zone():
    chk('1a', 5**2, '25'); chk('1b', 9**2, '81'); chk('1c', (-2.5)**2, '6,25'); chk('1d', (-7)**2, '49')
    chk('1e', (-3)**2, '9'); chk('1f', -3**2, '-9'); chk('1g', 2*(-4)**2, '32')
    chk('2a', 4*(1+2), '12'); chk('2b', 3+2*5, '13'); chk('2c', (-4)*(-4+9), '-20'); chk('2d', (-3)*(-3-5), '24')
    chk('2e', (-6)**2+5*(-6), '6'); chk('2f', 2*(-1)**2-3*(-1)-5, '0')
    chk('3a', L('x+4=9'), '5'); chk('3b', L('3*x=21'), '7'); chk('3c', L('x-2.5=-4'), '-1,5')
    chk('3d', L('-x=6'), '-6'); chk('3e', L('5*x+3=2*x-9'), '-4'); chk('3f', L('x+7=0'), '-7')
    chk_bool('4a', 2*3+1 == 7, 'wA'); chk_bool('4b', 4-1 == 5, 'fA'); chk_bool('4c', 3*(-2)+10 == 4, 'wA')
    chk_bool('4d', -2*(-5)-3 == 7, 'wA'); chk_bool('4e', 4*0.5-1 == 3, 'fA')
    chk('4a-l', 2*3+1, '7'); chk('4b-l', 4-1, '3'); chk('4c-l', 3*(-2)+10, '4'); chk('4d-l', -2*(-5)-3, '7'); chk('4e-l', 4*0.5-1, '1')
    chk('5a', math.sqrt(25), '5'); chk('5b', math.sqrt(81), '9'); chk('5c', math.sqrt(0.49), '0,7')
    chk('5d', math.sqrt(19), '4,36'); chk('5e', [], 'keine'); chk('5f', 0, '0'); chk('5g', math.sqrt(25+144), '13')
    # 6: Scheitel (d|e) aus a(x-d)^2+e, Öffnung aus a, Zahl der Nullstellen
    def sp(a, d, e):
        n = len(L(f'{a}*(x-({d}))**2+({e})=0'))
        return d, e, ('oben' if a > 0 else 'unten'), anzahl(n)
    for nr, (a, d, e), blatt in [('6a', (1, 1, 2), (1, 2, 'oben')), ('6b', (1, -3, -1), (-3, -1, 'oben')),
                                 ('6c', (-1, 2, 5), (2, 5, 'unten')), ('6d', (1, 0, -4), (0, -4, 'oben'))]:
        d_, e_, o_, _ = sp(a, d, e)
        chk(nr + '-S', [d_, e_], f'{blatt[0]}; {blatt[1]}'); chk_text(nr + '-Öffn.', o_, blatt[2])
    chk_text('6e', sp(1, 1, 2)[3], 'keine'); chk_text('6f', sp(-1, 2, 5)[3], 'zwei'); chk_text('6g', sp(1, 4, 0)[3], 'eine')
    chk_term('7a', 'x*(x+2)', 'x**2+2*x'); chk_term('7b', '-x*(x-4)', '-x**2+4*x'); chk_term('7c', '(x+1)**2', 'x**2+2*x+1')
    chk_term('7d', '(x-3)**2', 'x**2-6*x+9'); chk_term('7e', '(x+5)*(x-2)', 'x**2+3*x-10')
    chk_term('7f', 'x**2+6*x', 'x*(x+6)'); chk_term('7g', '3*x**2-12*x', '3*x*(x-4)')
    chk_term('8a', '3+x**2+2*x', 'x**2+2*x+3'); chk_term('8b', '5*x-1+x**2', 'x**2+5*x-1')
    chk_term('8c', 'x**2+4*x-7+2*x+9', 'x**2+6*x+2'); chk_term('8d', '7-x**2+3*x', '-x**2+3*x+7')
    chk_term('8e', '2*x**2-x+4-x**2-5*x+1', 'x**2-6*x+5')
    chk('9a', (-8)**2+3*(-8), '40'); chk('9b', (-5)**2+4*(-5), '5')
    sperre('zone_a.tex')

def grad(gl):
    l, r = gl.split('=')
    from sympy import Poly
    return Poly(expand(sympify(l) - sympify(r)), x).degree()

def e1():
    # Beispiele
    chk('12-Bsp', L('x**2=81'), '9; -9'); chk('13-Bsp', L('x**2-7=57'), '8; -8'); chk('14-Bsp', L('(x-3)**2=25'), '8; -2')
    # 10 quadratisch/linear
    for nr, gl, b in [('10a', 'x**2=50', 'quadratisch'), ('10b', '4*x-1=19', 'linear'), ('10c', '(x-1)**2=25', 'quadratisch'),
                      ('10d', '3*(x+2)=18', 'linear'), ('10e', 'x*x=14', 'quadratisch')]:
        chk_text(nr, 'quadratisch' if grad(gl) == 2 else 'linear', b)
    # 11 Vorzeichen der rechten Seite und Zahl der Lösungen
    for nr, c, b in [('11a', 30, 'positiv, zwei'), ('11b', -1, 'negativ, keine'), ('11c', 0, 'null, eine'),
                     ('11d', 0.1, 'positiv, zwei'), ('11e', -100, 'negativ, keine')]:
        vz = 'positiv' if c > 0 else ('null' if c == 0 else 'negativ')
        chk_text(nr, f"{vz}, {anzahl(len(L(f'x**2={c}')))}", b)
    chk('12a', L('x**2=25'), '5; -5'); chk('12b', L('x**2=100'), '10; -10'); chk('12c', L('x**2=144'), '12; -12')
    chk('12d', L('x**2=1'), '1; -1'); chk('12e', [v for v in L('x**2=225') if v > 0], '15')
    chk('12f', L('x**2=14'), '3,74; -3,74'); chk('12g', L('x**2=-64'), 'keine')
    chk('13a', L('x**2+5=30'), '5; -5'); chk('13b', L('2*x**2=98'), '7; -7'); chk('13c', L('2*x**2-3=29'), '4; -4')
    r2 = 850 / (math.pi * 12)
    chk('13d-r2', r2, '22,55'); chk('13d', math.sqrt(r2), '4,7')
    chk('13e', L('4*x**2+9=9'), '0'); chk('13f', L('2*x**2+11=3'), 'keine')
    chk('14a', L('(x-1)**2=9'), '4; -2'); chk('14b', L('(x-5)**2=4'), '7; 3'); chk('14c', L('(x+2)**2=49'), '5; -9')
    chk('14d', L('(x+6)**2=0'), '-6'); chk_bool('14e', (-5 + 2)**2 == 9, 'wA')
    f15 = '(x-1)**2-3'
    chk('15a', L(f'{f15}=1'), '-1; 3'); chk('15b', L(f'{f15}=-3'), '1'); chk('15c', L(f'{f15}=-4'), 'keine')
    chk('15d', L(f'{f15}=-5'), 'keine')  # Beispielwert c = -5; Scheitel bei y = -3
    chk_text('16a-1', anzahl(len(L('(x+5)**2=0'))), 'eine')
    chk_text('16a-2', 'wahr' if sorted(L('(x+6)**2=9')) == [3, 9] else 'falsch', 'falsch'); chk('16a-2L', L('(x+6)**2=9'), '-3; -9')
    chk('16b', L('x**2+3=0'), 'keine')
    chk('17a', L('(x+1)**2=81'), '8; -10'); chk('17b', L('(x+3)**2=64'), '5; -11')
    chk_text('18a', anzahl(len(L('x**2=40'))), 'zwei'); chk_text('18b', anzahl(len(L('x**2=-40'))), 'keine'); chk_text('18c', anzahl(len(L('x**2=0'))), 'eine')
    sperre('e1_a.tex')

def e2():
    chk('20-Bsp', L('(x-2)*(x-5)=0'), '2; 5'); chk('21-Bsp', L('x**2+3*x=0'), '0; -3')
    for nr, gl, b in [('19a', '(x-1)*(x-5)=0', 'gilt'), ('19b', 'x*(x+4)=21', 'gilt nicht'), ('19c', '(x+2)*(x-7)=0', 'gilt'),
                      ('19d', '(x-3)*x=-2', 'gilt nicht'), ('19e', '0=x*(x-1)', 'gilt')]:
        l, r = gl.split('=')
        chk_text(nr, 'gilt' if sympify(l) == 0 or sympify(r) == 0 else 'gilt nicht', b)
    chk('20a', L('(x-1)*(x-4)=0'), '1; 4'); chk('20b', L('(x-3)*(x-6)=0'), '3; 6'); chk('20c', L('(x-8)*(x-2)=0'), '8; 2')
    chk('20d', L('(x-5)*(x-7)=0'), '5; 7'); chk('20e', L('(x+4)*(x-1)=0'), '-4; 1'); chk('20f', L('x*(x+6)=0'), '0; -6')
    chk('20g', L('(x+3)*(x+3)=0'), '-3'); chk('20h-Wert', wert('(x-3)*(x+1)', -2), '5'); chk_bool('20h', wert('(x-3)*(x+1)', -2) == 0, 'fA')
    chk('21a', L('x**2+4*x=0'), '0; -4'); chk('21b', L('x**2+9*x=0'), '0; -9'); chk('21c', L('x**2-8*x=0'), '0; 8')
    chk('21d', L('2*x**2+10*x=0'), '0; -5'); chk_term('21e', 'x*(x+1)-30', 'x**2+x-30')
    chk_term('21f-Faktor', '2*x**2-2*x-24', '2*(x-4)*(x+3)'); chk('21f', L('2*x**2-2*x-24=0'), '4; -3')
    opts = [3, 4, -3, -12]
    chk('21g', [o for o in opts if wert('x*(x+7)', o) == -12], '-3')
    chk('22a', L('x**2=6*x'), '0; 6'); chk('22b', L('4*x**2=28*x'), '0; 7')
    chk('23a', L('(x-4)*(x+1)=0'), '4; -1'); chk('23b-Probe', wert('x*(x-1)', 6), '30'); chk('23b', L('x*(x-1)=6'), '3; -2')
    chk('24a', L('-0.05*x*(x-48)=0'), '0; 48'); chk('24b', wert('-0.05*x*(x-48)', 24), '28,8')
    sperre('e2_a.tex')

def pq(p, q):
    """p-q-Formel unabhängig von solve: (Diskriminante, Lösungen)."""
    D = (p / 2) ** 2 - q
    if D < 0:
        return D, []
    if D == 0:
        return D, [-p / 2]
    return D, [-p / 2 + math.sqrt(D), -p / 2 - math.sqrt(D)]

def e3():
    chk('28-Bsp', pq(6, 8)[1], '-2; -4'); chk('28-Bsp-L', L('x**2+6*x+8=0'), '-2; -4')
    formen = {'a': ('x**2=70', 'ohne x-Glied, Wurzelziehen'), 'b': ('(x-2)*(x+9)=0', 'Produkt = 0, Nullprodukt'),
              'c': ('(x+1)**2=7', 'Klammer^2 = Zahl, Rückwärtsrechnen'), 'd': ('x**2-3*x+1=0', 'Normalform, Formel'),
              'e': ('3*x**2-27=0', 'ohne x-Glied, Wurzelziehen')}
    for k, (gl, b) in formen.items():
        l, r = gl.split('=')
        if '*(' in l and r == '0':
            f = 'Produkt = 0, Nullprodukt'
        elif ')**2' in l:
            f = 'Klammer^2 = Zahl, Rückwärtsrechnen'
        else:
            from sympy import Poly
            P = Poly(expand(sympify(l) - sympify(r)), x)
            f = 'ohne x-Glied, Wurzelziehen' if P.coeff_monomial(x) == 0 else 'Normalform, Formel'
        chk_text('25' + k, f, b)
    for nr, gl, b in [('26a', 'x**2+5*x+4', '5; 4'), ('26b', 'x**2-3*x+2', '-3; 2'), ('26c', 'x**2+x-12', '1; -12'),
                      ('26d', 'x**2-11*x', '-11; 0'), ('26e', 'x**2-2', '0; -2')]:
        from sympy import Poly
        P = Poly(sympify(gl), x)
        pb, qb = zahlen(b)
        chk(nr + '-p', float(P.coeff_monomial(x)), str(pb).replace('.0', '')); chk(nr + '-q', float(P.coeff_monomial(1)), str(qb).replace('.0', ''))
    for nr, a, b in [('27a', 2, '2'), ('27b', 1, 'nicht'), ('27c', -1, '-1'), ('27d', 0.5, '0,5'), ('27e', 5, '5')]:
        if b == 'nicht':
            chk_text(nr, 'nicht teilen' if a == 1 else 'teilen', 'nicht teilen')
        else:
            chk(nr, a, b)
    chk('28a', pq(6, 5)[1], '-1; -5'); chk('28b', pq(10, 21)[1], '-3; -7'); chk('28c', pq(12, 35)[1], '-5; -7')
    chk('28d', pq(14, 40)[1], '-4; -10'); chk('28e', pq(-4, -5)[1], '5; -1')
    chk('29a', L('x**2=2*x+24'), '6; -4'); chk('29b', L('-2*x**2+12*x-10=0'), '5; 1'); chk('29c', pq(-5, 6)[1], '3; 2')
    chk('29d', pq(-10, 25)[1], '5'); chk('29e', pq(2, 7)[1], 'keine'); chk('29f-D', pq(7, 11)[0], '1,25'); chk_text('29f', anzahl(len(pq(7, 11)[1])), 'zwei')
    chk('30a', L('x**2-4*x+1=0'), '3,73; 0,27'); chk_bool('30b', wert('x**2+5*x-14', -7) == 0, 'wA'); chk('30c', L('(x+3)**2=2*x+14'), '1; -5')
    chk('31a', L('4*x**2=100'), '5; -5'); chk('31b', L('(x-6)*(x+1)=0'), '6; -1'); chk('31c', L('x**2-9*x=0'), '0; 9')
    chk('31d', L('(x-4)**2=1'), '5; 3'); chk('31e', L('x**2+x-6=0'), '2; -3'); chk('31f', L('2*x**2+4*x-4=0'), '0,73; -2,73')
    xs = L('x**2-3=2*x+5'); chk('32a-x', xs, '4; -2'); chk('32a-y', [wert('x**2-3', v) for v in xs], '13; 1')
    chk('32a-y-Gerade', [wert('2*x+5', v) for v in xs], '13; 1')
    xs = L('(x-3)**2-2=-x+3'); chk('32b-x', xs, '4; 1'); chk('32b-y', [wert('(x-3)**2-2', v) for v in xs], '-1; 2')
    chk('32b-y-Gerade', [wert('-x+3', v) for v in xs], '-1; 2')
    chk('33a', L('x**2-14*x+45=0'), '9; 5'); chk('33b', L('x**2-8*x+7=0'), '7; 1')
    chk('34a', L('3*x**2-6*x-9=0'), '3; -1')  # Kontrolle: normiert x^2-2x-3=0
    xs = L('-0.1*x**2+0.6*x+1.6=0'); chk('35a', xs, '8; -2'); chk('35a-Antwort', [v for v in xs if v >= 0], '8')
    chk('35b', L('-0.1*x**2+0.6*x+1.6=2'), '0,76; 5,24')
    sperre('e3_a.tex')

def e4():
    chk('37-Bsp', L('x**2=625'), '25; -25'); chk('38-Bsp', L('x*(x+4)=45'), '5; -9')
    # 36: sinnvolle Lösungen je Kontext (Länge, Anzahl, Zeit nicht negativ; Zahl beliebig)
    def passend(werte, nichtneg):
        return [w for w in werte if (w >= 0 or not nichtneg)]
    chk('36a', passend([4, -9], True), '4'); chk('36b', passend([8, -9], True), '8'); chk('36c', passend(L('x**2=49'), False), '7; -7')
    chk('36d', passend([-0.5, 2.5], True), '2,5'); chk('36e', passend(L('x*(x+1)=30'), False), '5; -6')
    chk('37a', L('x**2=400'), '20; -20'); chk('37b', L('x**2=900'), '30; -30'); chk('37c', L('x**2=0.25'), '0,5; -0,5')
    chk('37d', L('x**2=2500'), '50; -50'); chk('37e', L('x**2+19=100'), '9; -9'); chk('37f', L('x*(x+1)=56'), '7; -8')
    xs = L('x*(x+5)=84'); chk('38a', xs, '7; -12'); chk('38c', [v for v in xs if v > 0] + [v + 5 for v in xs if v > 0], '7; 12')
    chk('38d', 7 * 12, '84'); xs = L('(x+2)*(x+5)=88'); chk('38e', xs, '6; -13'); chk('38e-Antwort', [v for v in xs if v > 0], '6')
    chk('39a', [v for v in L('(x+2)**2=144') if v > 0], '10'); chk('39b', L('(x+6)**2=400'), '14; -26'); chk('39b-Antwort', [v for v in L('(x+6)**2=400') if v > 0], '14')
    chk('40a', L('x**2=196'), '14; -14')
    sperre('e4_a.tex')

TEILE = {'zone': zone, 'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4}

if __name__ == '__main__':
    teil = sys.argv[1]
    TEILE[teil]()
    zeilen.append(f"Abweichungen: {abw}")
    txt = '\n'.join(zeilen)
    open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8').write(txt + '\n')
    print(txt)
