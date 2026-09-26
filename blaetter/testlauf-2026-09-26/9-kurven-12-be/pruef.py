# pruef.py – rechnet die Lösungen je Einheit unabhängig nach (sympy)
# Aufruf: python pruef.py zone | e1 | e2 | e3 | e4 | e5
# Blattwerte sind aus den Lösungsquelltexten (*_l.tex) abgetragen.
import sys, math
import sympy as sp

x, t = sp.symbols('x t', real=True)
E = sp.E
ZEILEN = []

def num(v):
    return [float(sp.N(a)) for a in (v if isinstance(v, (list, tuple)) else [v])]

def chk(nr, skript, blatt, tol=1e-2, ordnung=False):
    s = num(skript); b = num(blatt)
    if not ordnung: s = sorted(s); b = sorted(b)
    ok = len(s) == len(b) and all(abs(p - q) <= tol * max(1, abs(q)) for p, q in zip(s, b))
    ZEILEN.append((nr, s, b, 'OK' if ok else 'ABWEICHUNG'))

def loes(expr, var=x, dom=None):
    r = [v for v in sp.solve(sp.Eq(expr, 0), var) if v.is_real]
    if dom: r = [v for v in r if dom[0] - 1e-9 <= float(v) <= dom[1] + 1e-9]
    return sorted(set(r), key=float)

def extrema(f, var=x):
    """Liste (Stelle, Wert, Art) aller lokalen Extrema; Art per f'' bzw. VZW."""
    d1 = sp.diff(f, var); d2 = sp.diff(d1, var); out = []
    for s in loes(d1, var):
        v2 = d2.subs(var, s)
        if abs(float(v2)) > 1e-12:
            out.append((s, sp.simplify(f.subs(var, s)), 'H' if v2 < 0 else 'T'))
        else:
            l = d1.subs(var, s - sp.Rational(1, 1000)); r = d1.subs(var, s + sp.Rational(1, 1000))
            if l * r < 0:
                out.append((s, sp.simplify(f.subs(var, s)), 'H' if l > 0 else 'T'))
            else:
                out.append((s, sp.simplify(f.subs(var, s)), 'S'))
    return out

def wende(f, var=x):
    d2 = sp.diff(f, var, 2); d3 = sp.diff(f, var, 3); out = []
    for s in loes(d2, var):
        if abs(float(d3.subs(var, s))) > 1e-12:
            out.append((s, sp.simplify(f.subs(var, s))))
    return out

def zone():
    f1 = sp.Rational(1, 8) * x**3 - sp.Rational(3, 2) * x + 2
    chk('1a y-Achse', f1.subs(x, 0), 2)
    ex = extrema(f1)
    chk('1b H x,y', [ (e[0], e[1]) for e in ex if e[2] == 'H'][0], [-2, 4])
    chk('1c T x,y', [ (e[0], e[1]) for e in ex if e[2] == 'T'][0], [2, 0])
    chk('1d Nullstellen', loes(f1), [-4, 2])
    chk('1e Berührstelle', [s for s in loes(f1) if sp.diff(f1, x).subs(x, s) == 0], [2])
    for nr, g, b in [('2a', 4*x-12, [3]), ('2b', x*(x-5), [0, 5]), ('2c', x**2-6*x+5, [1, 5]),
                     ('2d', x**2-36, [-6, 6]), ('2e', 6*x**2+6*x-36, [-3, 2]), ('2f', x**3-4*x, [-2, 0, 2]),
                     ('2g', x**4-5*x**2, [-math.sqrt(5), 0, math.sqrt(5)]), ('2h', (x-2)*sp.exp(x), [2]),
                     ('3', x**3-16*x, [0, -4, 4]), ('4a', 2*x**3-18*x, [-3, 0, 3]), ('4b', x**4-7*x**3, [0, 7])]:
        chk(nr, loes(g), b)
    # 5: Ableitungen, verglichen an Probestellen x = -1, 0.5, 2
    P = [-1, sp.Rational(1, 2), 2]
    def abl(nr, f, blatt, k=1):
        d = sp.diff(f, x, k)
        chk(nr, [d.subs(x, p) for p in P], [blatt.subs(x, p) for p in P])
    abl('5a', x**4, 4*x**3); abl('5b', 5*x**2, 10*x); abl('5c', 2*x**3-6*x**2+7, 6*x**2-12*x)
    abl('5d', -x**4/4+2*x, -x**3+2); abl('5e', sp.exp(2*x), 2*sp.exp(2*x))
    abl('5f', x*sp.exp(x), (x+1)*sp.exp(x)); abl('5g', (x-3)*sp.exp(-x), (4-x)*sp.exp(-x))
    abl("5h f'", x**4-2*x**3, 4*x**3-6*x**2); abl("5h f''", x**4-2*x**3, 12*x**2-12*x, 2)
    abl("5i f'", x*sp.exp(2*x), (1+2*x)*sp.exp(2*x)); abl("5i f''", x*sp.exp(2*x), (4+4*x)*sp.exp(2*x), 2)
    f6 = x**3 - 2*x**2 + 1; g6 = (x+1)*sp.exp(x)
    chk('6a', f6.subs(x, 0), 1); chk('6b', f6.subs(x, 2), 1); chk('6c', f6.subs(x, -1), -2)
    chk('6d', f6.subs(x, sp.Rational(1, 2)), 0.625); chk('6e', g6.subs(x, 0), 1); chk('6f', g6.subs(x, -1), 0)
    chk('6g P(2|1) ja=1', 1 if f6.subs(x, 2) == 1 else 0, 1)
    chk('6h f(-2)', f6.subs(x, -2), -15)
    chk('7a Nullst.', loes((x-2)*(x+1)), [-1, 2]); chk('7a Scheitel', [sp.Rational(1, 2), ((x-2)*(x+1)).subs(x, sp.Rational(1, 2))], [0.5, -2.25])
    chk('7b Nullst.', loes(-x**2+4), [-2, 2]); chk('7c Nullst.', loes(-x**3+4*x), [-2, 0, 2])
    q = x**2/2 - 2*x + 1; dq = sp.diff(q, x)
    chk("8a q'(0)<0", dq.subs(x, 0), -2); chk("8b q'(2)", dq.subs(x, 2), 0); chk("8c q'(4)>0", dq.subs(x, 4), 2)
    chk('8d Tangentensteigung A', dq.subs(x, 0), -2); chk('8 C auf q', q.subs(x, 4), 1)
    chk('8e q(0)=q(4)', [q.subs(x, 0), q.subs(x, 4)], [1, 1])

def vorz(d, a, b, var=x):
    """Vorzeichen von d in der Mitte von [a;b] (+1/-1), unbeschränkte Ränder als +-100."""
    m = (a + b) / 2
    return 1 if float(d.subs(var, m)) > 0 else -1

def mono(f, var=x, dom=(-100, 100)):
    """Grenzen und Vorzeichenfolge von f' – Grenzen = Nullstellen mit VZW im Bereich."""
    d = sp.diff(f, var)
    z = [float(s) for s in loes(d, var, dom) if dom[0] < float(s) < dom[1]]
    g = [dom[0]] + z + [dom[1]]
    return z, [vorz(d, g[i], g[i+1], var) for i in range(len(g) - 1)]

def e1():
    for nr, d, iv, b in [('9a', x-1, (2, 5), 1), ('9b', x-1, (-3, 0), -1), ('9c', -2*x+8, (5, 9), -1),
                         ('9d', (x-1)*(x-5), (2, 4), -1)]:
        # Vorzeichen muss im ganzen Intervall gleich sein
        z = [s for s in loes(d) if iv[0] < float(s) < iv[1]]
        chk(nr + ' Vorz.', vorz(d, *iv) if not z else 0, b)
    z, s = mono(x**3 - 12*x + 1); chk('10a Grenzen', z, [-2, 2]); chk('10a +-+', s, [1, -1, 1], ordnung=True)
    z, s = mono(-x**3 + 3*x**2 + 9*x); chk('10b Grenzen', z, [-1, 3]); chk('10b -+-', s, [-1, 1, -1], ordnung=True)
    # 10c: kubisch mit H(-1|5), T(3|-1): Ansatz f' = a(x+1)(x-3), a>0 wegen H links
    a, c = sp.symbols('a c'); F = sp.integrate(a*(x+1)*(x-3), x) + c
    sol = sp.solve([F.subs(x, -1) - 5, F.subs(x, 3) + 1], [a, c], dict=True)[0]
    chk('10c a>0 (steigt-fällt-steigt)', 1 if sol[a] > 0 else -1, 1)
    f = x**3 - 5*x**2 + 9*x + 1; g = x**2 + 1; dd = sp.expand(f - g)
    z, s = mono(dd, dom=(0, 5)); chk('10d Grenzen', z, [1, 3]); chk('10d +-+', s, [1, -1, 1], ordnung=True)
    werte = [dd.subs(x, v) for v in [0, 1, 3, 5]]
    chk('10d Wertebereich', [min(werte), max(werte)], [0, 20])
    # 11: f' > 0 überall: Minimum von f' numerisch bzw. keine reelle Nullstelle
    for nr, f in [('11a', 2*x**3 + x), ('11b', 4 + sp.exp(2*x)), ('11c', x + sp.exp(x)), ('11d', 5 - sp.exp(-x)),
                  ('11e', x**3 + x**2 + x), ('11f', x**5 + 2*x), ('11g', (x**2 + 3)*sp.exp(x))]:
        d = sp.diff(f, x)
        mini = min(float(d.subs(x, v)) for v in [i/10 for i in range(-200, 201)])
        chk(nr + " f'>0", 1 if (mini > 0 and not loes(d)) else 0, 1)
    chk('11e Diskriminante', 2**2 - 4*3*1, -8)
    z, s = mono(x**3 - 6*x**2 + 5); chk('12a Grenzen', z, [0, 4]); chk('12a +-+', s, [1, -1, 1], ordnung=True)
    z, s = mono(x**2 - 6*x + 1); chk('12b Grenze', z, [3])
    chk('13b f streng steigend (f(1)>f(0)>f(-1))', 1 if (x**3+2).subs(x, 1) > (x**3+2).subs(x, 0) > (x**3+2).subs(x, -1) else 0, 1)
    A = -sp.Rational(1, 10)*t**3 + sp.Rational(6, 5)*t**2 + 12; B = 12 + 6*t*sp.exp(-t/5)
    z, s = mono(A, t, (0, 10)); chk('14a A steigt bis', z, [8]); chk('14a A +-', s, [1, -1], ordnung=True)
    z, s = mono(B, t, (0, 10)); chk('14a B steigt bis', z, [5]); chk('14a B +-', s, [1, -1], ordnung=True)
    chk('14b Differenz', 8 - 5, 3)

def expkt(nr, f, blatt, var=x):
    """blatt: Liste (Art, x, y); verglichen werden Stellen, Werte und Art-Code H=1, T=-1, S=0."""
    code = {'H': 1, 'T': -1, 'S': 0}
    ex = extrema(f, var)
    chk(nr + ' Stellen', [e[0] for e in ex], [b[1] for b in blatt])
    chk(nr + ' Werte', [e[1] for e in sorted(ex, key=lambda e: float(e[0]))], [b[2] for b in sorted(blatt, key=lambda b: float(b[1]))], ordnung=True)
    chk(nr + ' Art', [code[e[2]] for e in sorted(ex, key=lambda e: float(e[0]))], [code[b[0]] for b in sorted(blatt, key=lambda b: float(b[1]))], ordnung=True)

def e2():
    chk('16b f\'\'(0)=0 -> VZW noetig', 0, 0)
    for nr, f, b in [('17a', x**3-27*x, [-3, 3]), ('17b', x**3+3*x**2-9*x, [-3, 1]), ('17c', 2*x**3-9*x**2+12*x, [1, 2]),
                     ('17d', -x**3+6*x**2-9*x, [1, 3])]:
        chk(nr, loes(sp.diff(f, x)), b)
    expkt('17e', x**3-3*x**2-9*x+2, [('H', -1, 7), ('T', 3, -25)])
    expkt('17f', 3*x**4-4*x**3-12*x**2, [('T', -1, -5), ('H', 0, 0), ('T', 2, -32)])
    expkt('17g', 3*x**4+4*x**3, [('T', -1, -1), ('S', 0, 0)])
    f = x**4-4*x**3-2*x**2+12*x; chk('17h x=3 ist Nullst. von f\'', sp.diff(f, x).subs(x, 3), 0)
    expkt('17h', f, [('T', -1, -9), ('H', 1, 7), ('T', 3, -9)])
    expkt('18a', x*sp.exp(-x), [('H', 1, sp.exp(-1))])
    expkt('18b', 8*t*sp.exp(-t/2), [('H', 2, 5.89)], t)
    f = 2*x**3-3*x**2-12*x; kand = [-2, 4] + [s for s in loes(sp.diff(f, x)) if -2 <= s <= 4]
    chk('18c groesster Wert', max(f.subs(x, k) for k in kand), 32)
    chk('18c Stelle', [k for k in kand if f.subs(x, k) == max(f.subs(x, kk) for kk in kand)], [4])
    f = x**4-32*x; chk('18d Minimum (global)', min(f.subs(x, s) for s in loes(sp.diff(f, x))), -48)
    expkt('18e', (x**2-3)*sp.exp(-x), [('T', -1, -2*E), ('H', 3, 6*sp.exp(-3))])
    for nr, f, x0 in [('19a', x**3-48*x, 4), ('19b', x**2-10*x+3, 5), ('19c', x**4-4*x, 1), ('19d', -2*x**3+6*x, -1)]:
        chk(nr + " f'(x0)", sp.diff(f, x).subs(x, x0), 0)
    f = x**3+3*x**2-2; chk("19e f'(-2), f''(-2), f(-2)", [sp.diff(f, x).subs(x, -2), sp.diff(f, x, 2).subs(x, -2), f.subs(x, -2)], [0, -6, 2], ordnung=True)
    expkt('19f', x**4-5, [('T', 0, -5)])
    f = -x**3+12*x+3; chk("19g f'(2), f''(2), f(2)", [sp.diff(f, x).subs(x, 2), sp.diff(f, x, 2).subs(x, 2), f.subs(x, 2)], [0, -12, 19], ordnung=True)
    expkt('19i', x**3-3*x**2+3*x, [('S', 1, 1)])
    f = -x**3+3*x**2+1; chk("19k f'(2), f''(2), f(2)", [sp.diff(f, x).subs(x, 2), sp.diff(f, x, 2).subs(x, 2), f.subs(x, 2)], [0, -6, 5], ordnung=True)
    expkt('20a', 2*x**3-6*x+1, [('H', -1, 5), ('T', 1, -3)])
    expkt('20b', (x-2)*sp.exp(x), [('T', 1, -E)])
    h = -sp.Rational(1, 20)*x**4 + sp.Rational(4, 5)*x**3 - sp.Rational(39, 10)*x**2 + sp.Rational(28, 5)*x + 2
    expkt('22a', h, [('H', 1, 4.45), ('T', 4, 0.4), ('H', 7, 4.45)])
    chk('22a Randwerte h(0), h(8)', [h.subs(x, 0), h.subs(x, 8)], [2, 2])
    chk('22b Abstand in m', (7-1)*10, 60)

def kruemm(f, var=x):
    d2 = sp.diff(f, var, 2)
    z = [float(s) for s in loes(d2, var)]
    g = [-100] + z + [100]
    return z, [vorz(d2, g[i], g[i+1], var) for i in range(len(g) - 1)]

def e3():
    P = [-1, sp.Rational(1, 2), 2]
    for nr, f, b2, b3 in [('23a', x**3-9*x**2, 6*x-18, 6+0*x), ('23b', -2*x**3+5*x**2, -12*x+10, -12+0*x),
                          ('23c', -x**4+3*x**2, -12*x**2+6, -24*x), ('23d', x**4/4-x**3, 3*x**2-6*x, 6*x-6)]:
        chk(nr + " f''", [sp.diff(f, x, 2).subs(x, p) for p in P], [b2.subs(x, p) for p in P], ordnung=True)
        chk(nr + " f'''", [sp.diff(f, x, 3).subs(x, p) for p in P], [b3.subs(x, p) for p in P], ordnung=True)
    chk('23e W', [c for w in wende(x**3-6*x**2+8*x) for c in w], [2, 0], ordnung=True)
    chk('23f W', [c for w in wende(x**4-2*x**3+1) for c in w], [0, 1, 1, 0], ordnung=True)
    chk('23g W', [c for w in wende((x+1)*sp.exp(-x)) for c in w], [1, 2*sp.exp(-1)], ordnung=True)
    for nr, f, zb, sb in [('24a', x**3+3*x**2-4, [-1], [-1, 1]), ('24b', -x**3+6*x**2, [2], [1, -1]),
                          ('24c', x**4-6*x**2, [-1, 1], [1, -1, 1])]:
        z, s = kruemm(f); chk(nr + ' Grenzen', z, zb); chk(nr + ' Kruemmung (+1 links)', s, sb, ordnung=True)
    for nr, f, x0 in [('25a', x**3+6*x**2-2, -2), ('25b', -x**3+9*x, 0)]:
        chk(nr + " f''(x0)=0, f'''!=0", [sp.diff(f, x, 2).subs(x, x0), 1 if sp.diff(f, x, 3).subs(x, x0) != 0 else 0], [0, 1], ordnung=True)
    f = x**4/2-3*x**2+2; chk("25c f''(1), f'''(1), f(1)", [sp.diff(f, x, 2).subs(x, 1), sp.diff(f, x, 3).subs(x, 1), f.subs(x, 1)], [0, 12, -0.5], ordnung=True)
    f = x**3-3*x**2+4*x; w = wende(f)[0]; m = sp.diff(f, x).subs(x, w[0])
    chk('25d W', [w[0], w[1]], [1, 2], ordnung=True); chk('25d Tangente m, n', [m, w[1] - m*w[0]], [1, 1], ordnung=True)
    f = x**4+2*x**3+5; chk("25e f'(0), f''(0), f'''(0), f(0)", [sp.diff(f, x, k).subs(x, 0) for k in (1, 2, 3)] + [f.subs(x, 0)], [0, 0, 12, 5], ordnung=True)
    f = (x-3)*sp.exp(x); expkt('25f T', f, [('T', 2, -E**2)])
    chk('25f W (Kontrolle)', [c for w in wende(f) for c in w], [1, -2*E], ordnung=True)
    chk('25f f->0 fuer x->-inf', sp.limit(f, x, -sp.oo), 0)
    z, s = kruemm(-x**3+3*x**2); chk('26a Grenze', z, [1]); chk('26a links dann rechts', s, [1, -1], ordnung=True)
    chk('26b W', [c for w in wende(x**3+3*x**2) for c in w], [-1, 2], ordnung=True)
    z, s = kruemm(x**4+1); chk('27a kein VZW von f\'\' (Anzahl Wechsel)', sum(s[i] != s[i+1] for i in range(len(s)-1)), 0)
    f = -sp.Rational(1, 10)*x**3 + sp.Rational(3, 5)*x**2
    chk('28a W', [c for w in wende(f) for c in w], [2, 1.6], ordnung=True)
    z, s = kruemm(f); chk('28a links dann rechts', s, [1, -1], ordnung=True)

def e4():
    f = x**4/4 - 2*x**2 + 1
    chk("29a f'=0", loes(sp.diff(f, x)), [-2, 0, 2])
    z, s = mono(f, dom=(-3, 3)); chk('29b/c Vorzeichen auf [-3;3]', s, [-1, 1, -1, 1], ordnung=True)
    chk("29d f'(1)", sp.diff(f, x).subs(x, 1), -3)
    w = [v for v in wende(f) if v[0] > 0][0]
    chk('29e W rechts', [w[0], w[1]], [1.15, -1.22], ordnung=True)
    chk("29e f'(W)<0", sp.diff(f, x).subs(x, w[0]), -3.08)
    fs = x**2/2 - x - sp.Rational(3, 2)
    chk("30a f'(1)", fs.subs(x, 1), -2)
    chk('30b Wendestelle = Extremstelle von f\'', loes(sp.diff(fs, x)), [1])
    z, s = mono(sp.integrate(fs, x)); chk('30c Extremstellen', z, [-1, 3]); chk('30c/d +-+ (H bei -1, T bei 3)', s, [1, -1, 1], ordnung=True)
    f = x**3/2 - sp.Rational(3, 2)*x**2
    chk('31a f', [f.subs(x, v) for v in [-1, 0, 1, 2, 3]], [-2, 0, -1, -2, 0], ordnung=True)
    chk("31a f'", [sp.diff(f, x).subs(x, v) for v in [-1, 0, 1, 2, 3]], [4.5, 0, -1.5, 0, 4.5], ordnung=True)
    expkt('31c', f, [('H', 0, 0), ('T', 2, -2)])
    fa = sp.Rational(10, 27)*x**3 - sp.Rational(5, 9)*x**2 - sp.Rational(20, 9)*x + sp.Rational(46, 27)
    expkt('32a Loesungsskizze', fa, [('H', -1, 3), ('T', 2, -2)])
    fb = sp.Rational(9, 16)*x**4 - sp.Rational(3, 2)*x**3 + 2
    expkt('32b Loesungsskizze', fb, [('S', 0, 2), ('T', 2, -1)])
    chk('32c Mindestgrad', sp.degree(fb, x), 4)
    d = -x**2 + 5*x - 4
    chk('33a d>0 auf ]1;4[ (Nullstellen)', loes(d), [1, 4]); chk('33a d(2.5)>0', d.subs(x, 2.5), 2.25)
    chk("33b d'(2.5)", sp.diff(d, x).subs(x, sp.Rational(5, 2)), 0)
    f = x**3 - 6*x**2 + 10*x; w = wende(f)[0]; m = sp.diff(f, x).subs(x, w[0]); mn = -1/m
    chk('33c W', [w[0], w[1]], [2, 4], ordnung=True); chk('33c Normale y-Achsenabschnitt', w[1] - mn*w[0], 3)
    chk("33c min f'", min(sp.diff(f, x).subs(x, s) for s in loes(sp.diff(f, x, 2))), -2)
    chk("33c Steigung -3 moeglich? (0=nein)", len(loes(sp.diff(f, x) + 3)), 0)
    r = -t**2/2 + 4*t - sp.Rational(7, 2)
    chk('36a Nullstellen r', loes(r, t), [1, 7])
    V = sp.integrate(r, (t, 0, t))
    chk('36b V(7)-V(0)>0 und V(7)>V(8)', [1 if V.subs(t, 7) > 0 else 0, 1 if V.subs(t, 7) > V.subs(t, 8) else 0], [1, 1], ordnung=True)
    chk('36c max Rate bei', loes(sp.diff(r, t), t), [4]); chk('36c Rate', r.subs(t, 4), 4.5)

def globmax(f, var, a, b, mini=False):
    kand = [a, b] + [s for s in loes(sp.diff(f, var), var) if a <= float(s) <= b]
    w = [(float(f.subs(var, k)), k) for k in kand]
    return (min(w) if mini else max(w))

def e5():
    h = t**3/16 - sp.Rational(3, 2)*t**2 + 9*t + 2
    chk('38 h(0),h(4),h(8),h(12)', [h.subs(t, v) for v in [0, 4, 8, 12]], [2, 18, 10, 2], ordnung=True)
    z, s = mono(h, t, (0, 12)); chk('38a-c steigt bis 4, dann faellt', s, [1, -1], ordnung=True)
    chk("38d h'=0", loes(sp.diff(h, t), t), [4, 12])
    chk('38e staerkstes Sinken (min h\')', globmax(sp.diff(h, t), t, 0, 12, mini=True)[1], 8)
    chk('38f h(8)', h.subs(t, 8), 10)
    zt = -t**3 + 6*t**2 + 15*t; m = globmax(zt, t, 0, 7)
    chk('39a groesste Hoehe, Zeit', [m[0], m[1]], [100, 5], ordnung=True); chk('39a z(7)', zt.subs(t, 7), 56)
    n = -4*t**3 + 36*t**2 + 60; m = globmax(n, t, 0, 9)
    chk('39b Max bei t=6, Wert', [m[1], m[0]], [6, 492], ordnung=True); chk("39b n''(6)", sp.diff(n, t, 2).subs(t, 6), -72)
    th = sp.Rational(1, 10)*t**3 - sp.Rational(6, 5)*t**2 + sp.Rational(18, 5)*t + 12; m = globmax(th, t, 0, 10)
    chk('39c hoechste Temp., Zeit', [m[0], m[1]], [28, 10], ordnung=True)
    expkt('39c lokale Extrema', th, [('H', 2, 15.2), ('T', 6, 12)], t)
    G = 40*x - (sp.Rational(1, 100)*x**3 - sp.Rational(3, 10)*x**2 + 31*x + 100)
    chk("39d G'=0", loes(sp.diff(G, x)), [-10, 30]); chk("39d G''(30)", sp.diff(G, x, 2).subs(x, 30), -1.2)
    m = globmax(G, x, 0, 50); chk('39d Max G, Stelle', [m[0], m[1]], [170, 30], ordnung=True)
    chk('39d G(0), G(50)', [G.subs(x, 0), G.subs(x, 50)], [-100, -150], ordnung=True)
    w = sp.Rational(1, 2)*t**3 - 6*t**2 + 18*t + 200; m = globmax(sp.diff(w, t), t, 0, 8, mini=True)
    chk("40a min w', Zeit", [m[0], m[1]], [-6, 4], ordnung=True); chk('40a w(4)', w.subs(t, 4), 208)
    p = 30*t*sp.exp(-t/3); m = globmax(sp.diff(p, t), t, 0, 14, mini=True)
    chk("40b min p', Zeit", [m[0], m[1]], [-4.06, 6], ordnung=True)
    f = -sp.Rational(5, 10000)*x**3 + sp.Rational(3, 100)*x**2; m = globmax(sp.diff(f, x), x, 0, 40)
    chk("40c max f', Stelle", [m[0], m[1]], [0.6, 20], ordnung=True)
    chk('40c Winkel in Grad', math.degrees(math.atan(m[0])), 31.0)
    g = x**2/4 - x
    chk('41a Breite cm, Tiefe cm', [(max(loes(g)) - min(loes(g)))*5, -globmax(g, x, 0, 4, mini=True)[0]*5], [20, 5], ordnung=True)
    mm = sp.Rational(1, 20)*x**3 - sp.Rational(3, 10)*x**2
    chk('41b Breite cm, Tiefe cm', [(max(loes(mm)) - min(loes(mm)))*5, -globmax(mm, x, 0, 6, mini=True)[0]*5], [30, 8], ordnung=True)
    V = t**3 - 15*t**2 + 63*t + 10; m = globmax(sp.diff(V, t), t, 0, 8, mini=True)
    chk("42a min V', Zeit", [m[0], m[1]], [-12, 5], ordnung=True)
    chk("42a V'(0), V'(8)", [sp.diff(V, t).subs(t, 0), sp.diff(V, t).subs(t, 8)], [63, 15], ordnung=True)
    chk('42b Breite cm', 5*20, 100)
    N = -sp.Rational(1, 10)*t**3 + sp.Rational(3, 2)*t**2; m = globmax(sp.diff(N, t), t, 0, 10)
    chk("44a max N', Tag", [m[1], m[0]], [5, 7.5], ordnung=True)
    chk("44c N'>0 auf ]0;10[ (min N' innen)", min(float(sp.diff(N, t).subs(t, v/10)) for v in range(1, 100)) > 0 and 1 or 0, 1)

TEILE = {'zone': zone, 'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'e5': e5}

if __name__ == '__main__':
    teil = sys.argv[1]
    TEILE[teil]()
    ab = 0
    with open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8') as fh:
        for nr, s, b, st in ZEILEN:
            ab += st != 'OK'
            z = f'{nr:24s} Skript {[round(v, 4) for v in s]}  Blatt {[round(v, 4) for v in b]}  {st}'
            print(z); fh.write(z + '\n')
        z = f'Abweichungen: {ab}'
        print(z); fh.write(z + '\n')
