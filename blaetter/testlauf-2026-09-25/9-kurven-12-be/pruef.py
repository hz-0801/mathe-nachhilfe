# pruef.py – rechnet die Lösungen je Einheit unabhängig nach (5.1 a)
# Aufruf: python pruef.py zone|e1|e2|e3|e4|e5  -> pruef_out_<datei>.txt
# Blattwerte sind aus dem Lösungsquelltext (<datei>_l.tex) übertragen.
import sys, math
import sympy as sp

x, t = sp.symbols('x t', real=True)
E = sp.E
ZEILEN = []

def _num(v):
    return float(sp.N(v))

def _flat(v):
    if isinstance(v, (list, tuple, set, sp.FiniteSet)):
        out = []
        for w in v:
            out += _flat(w)
        return out
    return [_num(v)]

def chk(nr, skript, blatt, tol=1e-9):
    """Zahlen, Punkte oder Mengen vergleichen (Mengen sortiert)."""
    if isinstance(skript, (set, sp.FiniteSet)) or isinstance(blatt, set):
        s = sorted(_flat(list(skript))); b = sorted(_flat(list(blatt)))
    else:
        s = _flat(skript); b = _flat(blatt)
    ok = len(s) == len(b) and all(abs(p - q) <= tol + 1e-9 for p, q in zip(s, b))
    ZEILEN.append((nr, s, b, ok))

def chk_expr(nr, skript, blatt):
    L = {'x': x, 't': t, 'e': E}
    s = sp.sympify(skript, locals=L); b = sp.sympify(blatt, locals=L)
    ok = sp.simplify(s - b) == 0
    ZEILEN.append((nr, str(s), str(b), ok))

def chk_txt(nr, skript, blatt):
    ZEILEN.append((nr, skript, blatt, skript == blatt))

def nst(expr, var=x):
    return set(sp.solveset(sp.Eq(expr, 0), var, domain=sp.S.Reals))

def extrema(f, var=x):
    """Liste (Stelle, Wert, Art) aller lokalen Extrema über Vorzeichenwechsel von f'."""
    d = sp.diff(f, var)
    out = []
    for s in sorted(nst(d, var), key=lambda q: float(q)):
        l = d.subs(var, s - sp.Rational(1, 1000)); r = d.subs(var, s + sp.Rational(1, 1000))
        l, r = float(l), float(r)
        if l > 0 and r < 0: out.append((s, sp.simplify(f.subs(var, s)), 'H'))
        elif l < 0 and r > 0: out.append((s, sp.simplify(f.subs(var, s)), 'T'))
        else: out.append((s, sp.simplify(f.subs(var, s)), 'S'))
    return out

def wende(f, var=x):
    """Wendestellen über Vorzeichenwechsel von f''."""
    d2 = sp.diff(f, var, 2)
    out = []
    for s in sorted(nst(d2, var), key=lambda q: float(q)):
        l = float(d2.subs(var, s - sp.Rational(1, 1000))); r = float(d2.subs(var, s + sp.Rational(1, 1000)))
        if l * r < 0: out.append((s, sp.simplify(f.subs(var, s))))
    return out

def rand_ext(f, a, b, var=x):
    kand = [a, b] + [s for s in nst(sp.diff(f, var), var) if a <= s <= b]
    werte = [(sp.simplify(f.subs(var, k)), k) for k in kand]
    return max(werte, key=lambda w: float(w[0])), min(werte, key=lambda w: float(w[0]))

def ende(f):
    lo = sp.limit(f, x, -sp.oo); hi = sp.limit(f, x, sp.oo)
    w = lambda L: 'oben' if L == sp.oo else 'unten'
    return w(lo) + ', ' + w(hi)

def sym(f):
    if sp.simplify(f.subs(x, -x) - f) == 0: return 'y'
    if sp.simplify(f.subs(x, -x) + f) == 0: return 'U'
    return 'k'

def vz(v):
    v = float(v)
    return '+' if v > 1e-12 else ('-' if v < -1e-12 else '0')

# ---------------------------------------------------------------- Zone
def zone():
    f = x**3 - 6*x**2 + 9*x
    chk('1a', nst(f), {0, 3})
    chk('1b', f.subs(x, 2), 2)
    ex = extrema(f)
    chk('1c', [(s, v) for s, v, a in ex if a == 'H'], [(1, 4)])
    chk('1d', [(s, v) for s, v, a in ex if a == 'T'], [(3, 0)])
    chk('1e', nst(f - 4), {1, 4})
    mx, mn = rand_ext(f, 0, 3)
    chk('1f', mx[0], 4)
    chk('2 Beispiel', nst(x**2 - 6*x + 8), {4, 2})
    chk('2a', nst(2*x - 8), {4})
    chk('2b', nst(x**2 - 49), {7, -7})
    chk('2c', nst(x**2 - 2*x - 8), {4, -2})
    chk('2d', nst(x**3 - 9*x), {0, 3, -3})
    chk('2e', nst(x**4 + 3*x**3 - 10*x**2), {0, 2, -5})
    chk('2f', nst((x - 3)*sp.exp(x)), {3})
    chk('2g', nst(x**3 - 2*x**2 - 5*x + 6), {1, 3, -2})
    chk('2g Lösung 1', (x**3 - 2*x**2 - 5*x + 6).subs(x, 1), 0)
    chk('3a', nst(x**3 - 36*x), {0, 6, -6})
    chk('3b', nst(2*x**3 - 32*x), {0, 4, -4})
    for nr, fx, bl in [('4a', x**5, '5*x**4'), ('4b', 3*x**2 + 7*x, '6*x+7'),
                       ('4c', -sp.Rational(1, 2)*x**4 + 2*x**3 - x + 9, '-2*x**3+6*x**2-1'),
                       ('4d', x**3/3 - x**2/2, 'x**2-x'),
                       ('4f', sp.exp(-2*x), '-2*exp(-2*x)'), ('4g', (x + 3)*sp.exp(x), '(x+4)*exp(x)'),
                       ('4h', x**2*sp.exp(-x), '(2*x-x**2)*exp(-x)')]:
        chk_expr(nr, sp.diff(fx, x), bl)
    fe = x**4 - 5*x**3 + x
    chk_expr("4e f'", sp.diff(fe, x), '4*x**3-15*x**2+1')
    chk_expr("4e f''", sp.diff(fe, x, 2), '12*x**2-30*x')
    chk_expr("4e f'''", sp.diff(fe, x, 3), '24*x-30')
    chk('5a', (x**2 + 1).subs(x, 3), 10)
    chk('5b', (x**3 - x).subs(x, 2), 6)
    chk('5c', (sp.Rational(1, 2)*x**4 - x**2).subs(x, -2), 4)
    chk('5d', (-x**2 + 4*x).subs(x, -3), -21)
    chk('5e', (x**3 + 2*x**2).subs(x, -3), -9)
    chk('5f', ((x + 1)*sp.exp(x)).subs(x, 0), 1)
    g5 = x**3 - 5*x + 2
    chk_txt('5g', 'ja' if g5.subs(x, 2) == 0 else 'nein', 'ja'); chk('5g Wert', g5.subs(x, 2), 0)
    chk_txt('5h', 'ja' if g5.subs(x, -1) == 4 else 'nein', 'nein'); chk('5h Wert', g5.subs(x, -1), 6)
    r5 = ((x + 1)*sp.exp(x)).subs(x, 1)
    chk_txt('5i', 'ja' if sp.simplify(r5 - 2*E) == 0 else 'nein', 'ja')
    for nr, fx, bl in [('6a', x**2 - 3, 'oben, oben'), ('6b', x**3, 'unten, oben'), ('6c', -2*x**2 + x, 'unten, unten'),
                       ('6d', -x**3 + 5*x**2, 'oben, unten'), ('6e', x**4 - 10*x**3, 'oben, oben')]:
        chk_txt(nr, ende(fx), bl)
    chk_txt('6f', sym(x**4 - 3*x**2), 'y'); chk_txt('6g', sym(x**3 - 7*x), 'U'); chk_txt('6h', sym(x**3 + x**2), 'k')
    g = (x**3 - 12*x)/8; dg = sp.diff(g, x)
    chk_txt('7a (A, x=-3)', vz(dg.subs(x, -3)), '+')
    chk_txt('7b (C, x=0)', vz(dg.subs(x, 0)), '-')
    chk_txt('7c (B, x=-2)', vz(dg.subs(x, -2)), '0')
    chk('7d', dg.subs(x, 0), -1.5)
    chk_txt('7e', ('B' if g.subs(x, -2) > g.subs(x, 0) else 'C') + ' höher, ' +
            ('C' if abs(dg.subs(x, 0)) > abs(dg.subs(x, -2)) else 'B') + ' steiler', 'B höher, C steiler')
    chk('7 Punkte A,B,D,E', [g.subs(x, -3), g.subs(x, -2), g.subs(x, 2), g.subs(x, 3)], [1.125, 2, -2, -1.125])

def mono(f, var=x, a=None, b=None):
    """Grenzen (Nullstellen von f' mit Vorzeichenwechsel oder Randpunkte) und Vorzeichenfolge von f'."""
    d = sp.diff(f, var)
    z = sorted([s for s in nst(d, var) if (a is None or a < s) and (b is None or s < b)], key=float)
    lo = (z[0] - 1 if z else -1) if a is None else a
    hi = (z[-1] + 1 if z else 1) if b is None else b
    pts = [lo] + z + [hi]
    sg = ''.join(vz(d.subs(var, (sp.nsimplify(pts[i]) + sp.nsimplify(pts[i + 1])) / 2)) for i in range(len(pts) - 1))
    return z, sg

def vz_intervall(d, a, b, var=x):
    """Vorzeichen von d auf [a;b] (Minimum/Maximum über Rand und kritische Stellen)."""
    kand = [a, b] + [s for s in nst(sp.diff(d, var), var) if a < s < b]
    w = [float(d.subs(var, k)) for k in kand]
    return '+' if min(w) > 0 else ('-' if max(w) < 0 else '±')

# ---------------------------------------------------------------- Einheit 1
def e1():
    chk_txt('8 Beispiel', vz_intervall(5*x - 10, 3, 6), '+')
    for nr, d, a, b, bl in [('8a', 2*x - 6, 4, 7, '+'), ('8b', -x + 5, 6, 9, '-'),
                            ('8c', x**2 + 1, -2, 2, '+'), ('8d', x**2 - 9, -2, 2, '-')]:
        chk_txt(nr, vz_intervall(d, a, b), bl)
    z, s = mono(x**2 + 2*x); chk('9 Beispiel Grenzen', z, [-1]); chk_txt('9 Beispiel VZ', s, '-+')
    z, s = mono(x**3/3 - 9*x); chk('9a Grenzen', z, [-3, 3]); chk_txt('9a VZ', s, '+-+')
    f9b = -x**3 + 3*x**2 + 9*x
    z, s = mono(f9b); chk('9b Grenzen', z, [-1, 3]); chk_txt('9b VZ', s, '-+-'); chk('9b Probe f\'(0)', sp.diff(f9b, x).subs(x, 0), 9)
    z, s = mono(x**4 - 8*x**2); chk('9c Extremstellen', z, [-2, 0, 2]); chk_txt('9c VZ', s, '-+-+')
    # 9d: H(-1|5), T(3|-4), Grad 3 -> Probe mit f'(x) = k(x+1)(x-3), k>0
    z, s = mono(sp.integrate((x + 1)*(x - 3), x)); chk('9d Grenzen', z, [-1, 3]); chk_txt('9d VZ', s, '+-+')
    z, s = mono((x - 2)*sp.exp(x)); chk('9e Grenzen', z, [1]); chk_txt('9e VZ', s, '-+')
    chk_expr('9e f\'', sp.diff((x - 2)*sp.exp(x), x), '(x-1)*exp(x)')
    R = sp.Rational
    f = -R(1, 10)*t**3 + R(12, 10)*t**2 + 50; g = -R(3, 10)*t**2 + R(27, 10)*t + 50; d = f - g
    chk_expr('9f d(t)', d, '-0.1*t**3+1.5*t**2-2.7*t'.replace('0.1', '1/10').replace('1.5', '3/2').replace('2.7', '27/10'))
    z, s = mono(d, t, 0, 10); chk('9f Grenzen', z, [1, 9]); chk_txt('9f VZ', s, '-+-')
    chk('9f d(0),d(1),d(9),d(10)', [d.subs(t, v) for v in (0, 1, 9, 10)], [0, -1.3, 24.3, 23])
    mx, mn = rand_ext(d, 0, 10, t); chk('9f Wertebereich', [mn[0], mx[0]], [-1.3, 24.3])
    for nr, fx, bl in [('10 Beispiel', 2*x**3 + x, 1), ('10a', x**3 + 5*x - 7, 5), ('10c', -x**3 - 2*x + 1, -2)]:
        dd = sp.diff(fx, x)
        ext = [dd.subs(x, s) for s in nst(sp.diff(dd, x))]  # Extremwert der Ableitung (Parabel)
        chk(nr + ' Schranke von f\'', ext, [bl])
        chk_txt(nr + ' kein VZW/keine NS', str(len(nst(dd))), '0')
    chk_txt('10b f\'=1+e^x>0', str(len(nst(sp.diff(x + sp.exp(x), x)))), '0')
    chk_expr('10e f\'', sp.diff((x**2 + 1)*sp.exp(x), x), '(x+1)**2*exp(x)')
    z, s = mono((x**2 + 1)*sp.exp(x)); chk_txt('10e VZ (nie negativ)', s.replace('0', ''), '++')
    f11 = x**3 - 6*x**2
    z, s = mono(f11); chk('11a Grenzen', z, [0, 4]); chk_txt('11a VZ', s, '+-+')
    chk('11a Probestellen f\'(-1), f\'(1), f\'(5)', [sp.diff(f11, x).subs(x, v) for v in (-1, 1, 5)], [15, -9, 15])
    chk('11 Mias Rechnung f\'\'(0), f\'\'(3)', [sp.diff(f11, x, 2).subs(x, v) for v in (0, 3)], [-12, 6])
    z, s = mono(x**3 + 3*x**2); chk('11b Grenzen', z, [-2, 0]); chk_txt('11b VZ', s, '+-+')
    chk('12a Minimum von 4x^2+7', (4*x**2 + 7).subs(x, 0), 7)
    z, s = mono(x**5); chk_txt('12b VZ von f\' (nie negativ)', s, '++')
    A = -R(2, 100)*t**3 + R(3, 10)*t**2 + 15; B = -R(1, 10)*t**2 + R(16, 10)*t + 14
    z, s = mono(A, t, 0, 14); chk('13a A Grenze', z, [10]); chk_txt('13a A VZ', s, '+-')
    z, s = mono(B, t, 0, 14); chk('13a B Grenze', z, [8]); chk_txt('13a B VZ', s, '+-')
    chk('13b Differenz der Steigzeiten', 10 - 8, 2)

# ---------------------------------------------------------------- Einheit 2
def pts(ex, art):
    return [(s, v) for s, v, a in ex if a == art]

def e2():
    R = sp.Rational
    chk('16 Beispiel', nst(sp.diff(x**3 - 6*x**2 + 9*x, x)), {3, 1})
    for nr, fx, bl in [('16a', x**3/3 - 4*x, {2, -2}), ('16b', x**3/3 - x**2 - 3*x, {3, -1}),
                       ('16c', 2*x**3 + 3*x**2 - 12*x, {1, -2}), ('16d', -x**3/3 + 2*x**2 + 5*x, {5, -1})]:
        chk(nr, nst(sp.diff(fx, x)), bl)
    ex = extrema(x**3 + 3*x**2 - 9*x); chk('17a H', pts(ex, 'H'), [(-3, 27)]); chk('17a T', pts(ex, 'T'), [(1, -5)])
    ex = extrema(x**4 - 4*x**3 + 4*x**2); chk('17b T', pts(ex, 'T'), [(0, 0), (2, 0)]); chk('17b H', pts(ex, 'H'), [(1, 1)])
    f = 3*x**4 - 4*x**3; ex = extrema(f)
    chk('17c T', pts(ex, 'T'), [(1, -1)]); chk('17c S', pts(ex, 'S'), [(0, 0)])
    chk("17c f''(0), f'''(0)", [sp.diff(f, x, 2).subs(x, 0), sp.diff(f, x, 3).subs(x, 0)], [0, -24])
    f = R(1, 4)*x**4 - R(7, 2)*x**2 + 6*x; ex = extrema(f)
    chk('17d Stelle 1 ist NS von f\'', sp.diff(f, x).subs(x, 1), 0)
    chk('17d H-Stellen', [s for s, v, a in ex if a == 'H'], [1]); chk('17d T-Stellen', [s for s, v, a in ex if a == 'T'], [-3, 2])
    ex = extrema((x**2 - 3)*sp.exp(x)); chk('17e H', pts(ex, 'H'), [(-3, 0.30)], tol=0.005); chk('17e T', pts(ex, 'T'), [(1, -5.44)], tol=0.005)
    chk('17e exakt', [pts(ex, 'H')[0][1], pts(ex, 'T')[0][1]], [6*sp.exp(-3), -2*E])
    a = 5*t*sp.exp(-R(1, 5)*t); ex = extrema(a, t); chk('17f', pts(ex, 'H'), [(5, 9.2)], tol=0.01)
    mx, mn = rand_ext(-x**3 + 6*x**2, -3, 5)
    chk('17g max (Wert, Stelle)', [mx[0], mx[1]], [81, -3]); chk('17g min (Wert, Stelle)', [mn[0], mn[1]], [0, 0])
    chk('17g Randwert g(5), H', [(-x**3 + 6*x**2).subs(x, 5), pts(extrema(-x**3 + 6*x**2), 'H')], [25, (4, 32)])
    f = x**4 - 2*x**2 + 3; ex = extrema(f); chk('17h T', pts(ex, 'T'), [(-1, 2), (1, 2)]); chk('17h H', pts(ex, 'H'), [(0, 3)])
    chk_txt('17h Grenzverhalten', ende(f), 'oben, oben')
    f = x**2*sp.exp(-R(1, 2)*x); ex = extrema(f)
    chk('17i T', pts(ex, 'T'), [(0, 0)]); chk('17i H', pts(ex, 'H'), [(4, 2.17)], tol=0.005)
    chk_expr('17i f\'', sp.diff(f, x), '0.5*x*(4-x)*exp(-x/2)'.replace('0.5', '1/2'))
    chk('18 Beispiel', sp.diff(x**3 - 6*x**2 + 5, x).subs(x, 4), 0)
    for nr, fx, x0 in [('18a', x**2 - 10*x, 5), ('18b', x**3 - 27*x, 3), ('18c', 2*x**3 + 3*x**2 - 36*x, 2), ('18d', x**4 - 18*x**2, -3)]:
        chk(nr, sp.diff(fx, x).subs(x, x0), 0)
    f = -x**3 + 3*x**2 + 24*x; chk("18e f'(4), f''(4)", [sp.diff(f, x).subs(x, 4), sp.diff(f, x, 2).subs(x, 4)], [0, -18])
    f = x**4 + 4*x - 4; chk("18f f'(-1), f''(-1), f(-1)", [sp.diff(f, x).subs(x, -1), sp.diff(f, x, 2).subs(x, -1), f.subs(x, -1)], [0, 12, -7])
    f = (x + 2)**4 - 1; chk_txt('18g Art', extrema(f)[0][2], 'T'); chk('18g Punkt', extrema(f)[0][:2], (-2, -1)); chk("18g f''(-2)", sp.diff(f, x, 2).subs(x, -2), 0)
    f = -x**3 + 3*x**2 - 3*x + 4; ex = extrema(f); chk_txt('18i Art', ex[0][2], 'S'); chk('18i Punkt', ex[0][:2], (1, 3))
    f = x**3 + x**2 - 3*x; d = sp.diff(f, x)
    chk("18j f'(0), f'(1)", [d.subs(x, 0), d.subs(x, 1)], [-3, 2]); chk('18j Tiefstelle', [s for s, v, a2 in extrema(f) if a2 == 'T'], [0.72], tol=0.005)
    f = 3*x**4 - 8*x**3 + 2; ex = extrema(f)
    chk('18k T', pts(ex, 'T'), [(2, -14)]); chk("18k f''(2)", sp.diff(f, x, 2).subs(x, 2), 48); chk_txt('18k Art bei 0', [a2 for s, v, a2 in ex if s == 0][0], 'S')
    chk('19a Nullstellen', nst(x**2 - 6*x + 5), {1, 5}); chk('19a Extremstelle', nst(sp.diff(x**2 - 6*x + 5, x)), {3})
    q = x**2 - 4*x + 7; T = pts(extrema(q), 'T')[0]; chk('19b Abstand', T[1] - 1, 2)
    f = (x**2 - 4)*sp.exp(-x); chk('19c Nullstellen', nst(f), {-2, 2})
    chk('19c Tiefstelle', [s for s, v, a2 in extrema(f) if a2 == 'T'], [1 - sp.sqrt(5)]); chk('19c gerundet', 1 - sp.sqrt(5), -1.24, tol=0.005)
    f = R(1, 4)*x**3 - 3*x; ex = extrema(f); chk('19d T', pts(ex, 'T'), [(2, -4)]); chk('19d H', pts(ex, 'H'), [(-2, 4)])
    chk('19d Abstand', sp.sqrt(4**2 + 8**2), 8.94, tol=0.005)
    f = -R(1, 2)*x**3 + R(3, 2)*x; ex = extrema(f); chk('19e H', pts(ex, 'H'), [(1, 1)]); chk('19e T', pts(ex, 'T'), [(-1, -1)])
    f = x**3 - 3*x**2 - 9*x + 2; ex = extrema(f); chk('20a H', pts(ex, 'H'), [(-1, 7)]); chk('20a T', pts(ex, 'T'), [(3, -25)])
    chk("20 Jonas f''(-1), f''(3)", [sp.diff(f, x, 2).subs(x, -1), sp.diff(f, x, 2).subs(x, 3)], [-12, 12])
    ex = extrema(x**3 + 3*x**2 - 1); chk('20b H', pts(ex, 'H'), [(-2, 3)]); chk('20b T', pts(ex, 'T'), [(0, -1)])
    ex = extrema(x**5); chk_txt('21a x^5 bei 0', ex[0][2], 'S')
    # 21c: kubische Funktion mit zwei verschiedenen Nullstellen von f' -> H und T (Stichprobe)
    chk_txt('21c Stichprobe', ''.join(sorted(a2 for s, v, a2 in extrema(x**3 - 2*x**2 - 4*x + 1))), 'HT')
    f = x**3 - 3*x**2; chk('22a Achsenschnitt', nst(f), {0, 3}); chk_expr("22a f'", sp.diff(f, x), '3*x*(x-2)')
    chk("22a f'(-1), f'(1)", [sp.diff(f, x).subs(x, -1), sp.diff(f, x).subs(x, 1)], [9, -3]); chk('22a H', pts(extrema(f), 'H'), [(0, 0)])
    ex = extrema(sp.exp(x) - x); chk('22c', [(s, v, a2) for s, v, a2 in ex if a2 == 'T'][0][:2], (0, 1)); chk_txt('22c Anzahl Extrema', str(len(ex)), '1')
    f = sp.exp(-x**2); ex = extrema(f); chk('22d H', pts(ex, 'H'), [(0, 1)]); chk_txt('22d Symmetrie', sym(f), 'y')
    chk('22d Grenzwert', sp.limit(f, x, sp.oo), 0)
    f = -R(1, 2)*x**2 + 2*x + 1; g = -R(1, 4)*x**3 + R(15, 4)*x**2 - 18*x + 29
    chk('23 Stetigkeit f(4)=g(4)', f.subs(x, 4), g.subs(x, 4))
    H1 = pts(extrema(f), 'H')[0]; H2 = [p for p in pts(extrema(g), 'H') if 4 <= p[0] <= 7][0]
    chk('23a Gipfel A', H1, (2, 3)); chk('23a Gipfel B', H2, (6, 2)); chk("23a g''(6)", sp.diff(g, x, 2).subs(x, 6), -1.5)
    dist = 100*sp.sqrt((H2[0] - H1[0])**2 + (H2[1] - H1[1])**2); chk('23b Länge in m', dist, 412, tol=0.5)
    chk_txt('23b möglich', 'ja' if dist <= 450 else 'nein', 'ja')

# ---------------------------------------------------------------- Einheit 3
def kruemm(f, var=x):
    """Wendestellen und Vorzeichenfolge von f''."""
    return mono(sp.diff(f, var), var)

def e3():
    R = sp.Rational
    fb = x**4 - 2*x**3 + x
    chk_expr("24 Beispiel f''", sp.diff(fb, x, 2), '12*x**2-12*x'); chk_expr("24 Beispiel f'''", sp.diff(fb, x, 3), '24*x-12')
    for nr, fx, b2, b3 in [('24a', x**3 + 2*x**2, '6*x+4', '6'), ('24b', x**4 - x**2, '12*x**2-2', '24*x'),
                           ('24c', -2*x**3 + 5*x - 1, '-12*x', '-12'), ('24d', R(1, 2)*x**4 + x**3, '6*x**2+6*x', '12*x+6')]:
        chk_expr(nr + " f''", sp.diff(fx, x, 2), b2); chk_expr(nr + " f'''", sp.diff(fx, x, 3), b3)
    chk('25 Beispiel', wende(x**3 + 3*x**2 - 2), [(-1, 0)])
    chk('25a', wende(2*x**3 - 6*x**2 + 5*x), [(1, 1)])
    f = x**4 - 6*x**2 + 1; chk('25b', wende(f), [(-1, -4), (1, -4)])
    z, s = kruemm(f); chk('25c Grenzen', z, [-1, 1]); chk_txt('25c VZ f\'\' (+ = links)', s, '+-+')
    f = x**3 - 6*x**2 + 11*x - 5; W = wende(f); chk('25d W', W, [(2, 1)])
    m = sp.diff(f, x).subs(x, 2); chk('25d Tangente m, n', [m, W[0][1] - m*2], [-1, 3])
    f = -x**3 + 3*x**2 + 1; chk("25e f''(1), f'''(1), f(1)", [sp.diff(f, x, 2).subs(x, 1), sp.diff(f, x, 3).subs(x, 1), f.subs(x, 1)], [0, -6, 3])
    f = 3*x**4 + 4*x**3 + 1
    chk("25f f'(0), f''(0), f'''(0), f(0)", [sp.diff(f, x).subs(x, 0), sp.diff(f, x, 2).subs(x, 0), sp.diff(f, x, 3).subs(x, 0), f.subs(x, 0)], [0, 0, 24, 1])
    f = x*sp.exp(x); chk_expr("26a f''", sp.diff(f, x, 2), '(x+2)*exp(x)')
    W = wende(f); chk('26a W exakt', W, [(-2, -2*sp.exp(-2))]); chk('26a W gerundet', W[0][1], -0.27, tol=0.005)
    g = 3/E*(x - 2)*sp.exp(x)   # Lösungsskizze
    chk('26b Skizze: T', pts(extrema(g), 'T'), [(1, -3)]); chk('26b Skizze: Grenzwert links', sp.limit(g, x, -sp.oo), 0)
    chk('26b Skizze: W links von T', [w[0] for w in wende(g)], [0])
    chk('27a Winkel', sp.deg(sp.atan(1)), 45)
    f = x**4 - 2*x**3; W = wende(f); chk('27b W', W, [(0, 0), (1, -1)])
    mW = (W[1][1] - W[0][1]) / (W[1][0] - W[0][0]); chk('27b Gerade m, n', [mW, W[0][1]], [-1, 0])
    d = f + x
    grenz_lo = d.subs(x, -1); grenz_hi = d.subs(x, R(22, 10))
    chk('27c zulässige c (2 < c <= 4,33)', [grenz_lo, grenz_hi], [2, 4.33], tol=0.005)
    loes = [s for s in sp.Poly(d - 3, x).nroots() if s.is_real and -1 <= s <= 2.2]
    chk('27c Schnittstelle bei c = 3 (genau eine)', loes, [2.1], tol=0.02)
    f = -x**3 + 6*x**2; z, s = kruemm(f); chk('28a Grenze', z, [2]); chk_txt('28a VZ (links, rechts)', s, '+-')
    chk("28 Leas f''(0), f''(3)", [sp.diff(f, x, 2).subs(x, 0), sp.diff(f, x, 2).subs(x, 3)], [12, -6])
    z, s = kruemm(x**3 + 3*x**2 - x); chk('28b Grenze', z, [-1]); chk_txt('28b VZ', s, '-+')
    chk_txt('29a x^4 ohne Wendepunkt', str(len(wende(x**4))), '0')
    mm = sp.symbols('m', real=True)
    for mv, anz in [(2, 3), (1, 1), (0, 1), (-3, 1)]:
        chk(f'29c m = {mv}: Anzahl', len(nst(x**3 + x - mv*x)), anz)
    chk('29c W', wende(x**3 + x), [(0, 0)])
    f = R(1, 10)*x**3 - R(6, 10)*x**2 + 2; W = wende(f); chk('30a W', W, [(2, 0.4)])
    z, s = kruemm(f); chk_txt('30 VZ (rechts, links)', s, '-+')

# ---------------------------------------------------------------- Einheit 4
def e4():
    R = sp.Rational
    fb = sp.integrate((x + 1)*(x - 2), x); z, s = mono(fb); chk('31 Beispiel', z, [-1, 2]); chk_txt('31 Beispiel VZ', s, '+-+')
    f1 = R(1, 4)*x**4 - 2*x**2 + 1; z, s = mono(f1); chk('31a', z, [-2, 0, 2]); chk_txt('31b', s, '-+-+')
    chk('31 f1 im Bild (y-Bereich)', [f1.subs(x, 3), pts(extrema(f1), 'T')[0][1]], [3.25, -3])
    f2 = R(1, 2)*x**3 - R(3, 2)*x**2 + 2; z, s = mono(f2); chk('31c', z, [0, 2])
    chk_txt('31d', ''.join(vz(sp.diff(f2, x).subs(x, v)) for v in (-1, 1, 3)), '+-+')
    chk('31e W', wende(f2), [(1, 1)]); chk("31e f2'(1)", sp.diff(f2, x).subs(x, 1), -1.5)
    p = R(3, 2); chk_txt('31f Punkt x=1,5: f>0, f\'<0, f\'\'>0', vz(f2.subs(x, p)) + vz(sp.diff(f2, x).subs(x, p)) + vz(sp.diff(f2, x, 2).subs(x, p)), '+-+')
    f = x**3/3 - x**2; d = sp.diff(f, x)
    chk_expr("32a f'", d, 'x**2-2*x'); chk('32a Tabelle', [d.subs(x, v) for v in (-1, 0, 1, 2, 3)], [3, 0, -1, 0, 3])
    chk('32c H, T', [pts(extrema(f), 'H'), pts(extrema(f), 'T')], [(0, 0), (2, -R(4, 3))])
    fs = R(5, 32)*x**3 - R(15, 8)*x - R(1, 2)   # Lösungsskizze 33
    chk('33 Skizze H', pts(extrema(fs), 'H'), [(-2, 2)]); chk('33 Skizze T', pts(extrema(fs), 'T'), [(2, -3)])
    chk('33 Skizze W-Stelle', [w[0] for w in wende(fs)], [0]); chk("33 f'-Skizze Nullstellen", nst(sp.diff(fs, x)), {-2, 2})
    chk('33c Mindestgrad (Beispiel x^4-2x^2: 2 T, 1 H)', [len(pts(extrema(x**4 - 2*x**2), 'T')), len(pts(extrema(x**4 - 2*x**2), 'H')), sp.degree(x**4 - 2*x**2, x)], [2, 1, 4])
    dd = -R(1, 2)*x**2 + x + R(3, 2)
    chk('34b', nst(dd), {-1, 3}); chk_txt('34a VZ zwischen', vz(dd.subs(x, 1)), '+')
    chk('34c', pts(extrema(dd), 'H'), [(1, 2)])
    f = -R(1, 2)*x**3 + R(3, 2)*x**2 + 1; W = wende(f); chk('35a W', W, [(1, 2)])
    m = sp.diff(f, x).subs(x, 1); chk('35a Normale Steigung', -1/m, -R(2, 3))
    chk("35a max f'", pts(extrema(sp.diff(f, x)), 'H'), [(1, 1.5)])
    chk_txt('35a (2) f\' nimmt 3 an?', 'ja' if nst(sp.diff(f, x) - 3) else 'nein', 'nein')
    chk_expr('35b f - Wendetangente', f - (m*x + (W[0][1] - m)), '-(x-1)**3/2')
    tang = sp.diff(f, x).subs(x, 0)*x + f.subs(x, 0)
    chk('35b Tangente bei x=0: Anzahl gemeinsamer Punkte', len(nst(f - tang)), 2)
    fp = x**2 - 2*x - 3; F = sp.integrate(fp, x)
    chk('36 Tiefpunkt von f\'', pts(extrema(fp), 'T'), [(1, -4)]); chk('36a Wendestelle von f', [w[0] for w in wende(F)], [1])
    chk('36b H-Stelle', [s for s, v, a2 in extrema(F) if a2 == 'H'], [-1]); chk('36b T-Stelle', [s for s, v, a2 in extrema(F) if a2 == 'T'], [3])
    chk('37a Grad', [sp.degree(sp.diff(x**5 - 3*x**2, x), x)], [4])
    w = -R(1, 4)*t**2 + 3*t - 5
    chk('38a/b', nst(w, t), {2, 10}); chk_txt('38a VZ', ''.join(vz(w.subs(t, v)) for v in (1, 6, 11)), '-+-')
    chk('38c', pts(extrema(w, t), 'H'), [(6, 4)])
    chk('38 Bild: w\'(0), w\'(12)', [w.subs(t, 0), w.subs(t, 12)], [-5, -5])

# ---------------------------------------------------------------- Einheit 5
def verlauf(f, a, b, var=t):
    m = (sp.nsimplify(a) + sp.nsimplify(b)) / 2
    d1 = vz(sp.diff(f, var).subs(var, m)); d2 = vz(sp.diff(f, var, 2).subs(var, m))
    z = 'nimmt zu' if d1 == '+' else 'nimmt ab'
    s = 'immer schneller' if (d1 == d2) else 'immer langsamer'
    return z + ', ' + s

def e5():
    R = sp.Rational
    W = R(1, 4)*t**3 - 3*t**2 + 9*t + 2
    for nr, a, b, bl in [('40a', 0, 2, 'nimmt zu, immer langsamer'), ('40b', 2, 4, 'nimmt ab, immer schneller'),
                         ('40c', 4, 6, 'nimmt ab, immer langsamer'), ('40d', 6, 8, 'nimmt zu, immer schneller')]:
        chk_txt(nr, verlauf(W, a, b), bl)
    chk('40 Abschnittsgrenzen (H, T)', [pts(extrema(W, t), 'H'), pts(extrema(W, t), 'T')], [(2, 10), (6, 2)])
    Wp = wende(W, t); chk('40e Wendestelle', [Wp[0][0]], [4]); chk_txt('40e Abnahme', vz(sp.diff(W, t).subs(t, 4)), '-')
    chk('40f in m³', 100*W.subs(t, 4), 600)
    chk('40 Bild: W(0), W(8)', [W.subs(t, 0), W.subs(t, 8)], [2, 10])
    hb = -5*t**2 + 20*t; chk('41 Beispiel', pts(extrema(hb, t), 'H'), [(2, 20)])
    h = -R(1, 2)*t**3 + 3*t**2; mx, mn = rand_ext(h, 0, 6, t); chk('41a (Wert, Stelle)', [mx[0], mx[1]], [16, 4])
    N = -R(1, 10)*t**3 + R(3, 2)*t**2 + 20
    chk("41b N'(10), N''(10)", [sp.diff(N, t).subs(t, 10), sp.diff(N, t, 2).subs(t, 10)], [0, -3])
    chk('41b N(10), N(0), N(14)', [N.subs(t, v) for v in (10, 0, 14)], [70, 20, 39.6])
    mx, mn = rand_ext(N, 0, 14, t); chk('41b global max', [mx[0], mx[1]], [70, 10])
    K = 50*t*sp.exp(-t/2); Kp = sp.diff(K, t)
    chk('41c Wendestelle', [w[0] for w in wende(K, t)], [4]); chk_txt('41c Minimum von K\'', pts(extrema(Kp, t), 'T') and 'T bei 4' , 'T bei 4')
    chk("41c K'(4)", Kp.subs(t, 4), -6.77, tol=0.005); chk("41c K'(4) exakt", Kp.subs(t, 4), -50*sp.exp(-2))
    f = R(1, 2)*t**3 - 6*t**2 + 18*t + 20
    chk('41d Nullstellen von f\'', nst(sp.diff(f, t), t), {2, 6})
    mx, mn = rand_ext(f, 0, 5, t); chk('41d max (Wert, Stelle)', [mx[0], mx[1]], [36, 2]); chk('41d min (Wert, Stelle)', [mn[0], mn[1]], [20, 0])
    chk('41d f(5)', f.subs(t, 5), 22.5)
    s = R(1, 10)*x**3 - R(6, 10)*x**2
    chk('42a Nullstellen', nst(s), {0, 6}); chk('42a T', pts(extrema(s), 'T'), [(4, -3.2)])
    chk('42a Breite, Tiefe in cm', [6*5, 3.2*5], [30, 16]); chk_txt('42a passt', 'ja' if 30 <= 32 and 16 <= 15 else 'nein', 'nein')
    r = -R(1, 5)*t**3 + 3*t**2; chk('42b Wendestelle', [w[0] for w in wende(r, t)], [5]); chk("42b r'(5)", sp.diff(r, t).subs(t, 5), 15)
    fA = -R(5, 100)*t**3 + R(13, 10)*t**2 + t + 5; gB = R(4, 10)*t**2 + 4*t + 5; d = fA - gB
    chk_expr('42c d(t)', d, '-t**3/20+9*t**2/10-3*t')
    chk('42c Nullstellen d\'', nst(sp.diff(d, t), t), {2, 10}); chk("42c d''(10)", sp.diff(d, t, 2).subs(t, 10), -1.2)
    chk('42c d(10), d(0), d(12)', [d.subs(t, v) for v in (10, 0, 12)], [10, 0, 7.2])
    mx, mn = rand_ext(d, 0, 12, t); chk('42c globaler Vorsprung', [mx[0], mx[1]], [10, 10])
    T = -R(1, 10)*t**3 + R(9, 10)*t**2 + 15
    chk("43 Pauls Nullstellen T'", nst(sp.diff(T, t), t), {0, 6}); chk('43 Pauls Stelle ist H', pts(extrema(T, t), 'H')[0][0], 6)
    Tp = sp.diff(T, t); mx, mn = rand_ext(Tp, 0, 8, t); chk("43a max T' (Wert, Stelle)", [mx[0], mx[1]], [2.7, 3])
    Z = -R(1, 5)*t**3 + R(9, 5)*t**2 + 50; Zp = sp.diff(Z, t); mx, mn = rand_ext(Zp, 0, 9, t)
    chk("43b max Z' (Wert, Stelle)", [mx[0], mx[1]], [5.4, 3]); chk('43b Besucher pro Stunde', 100*mx[0], 540)
    z = -R(1, 2)*x**2 + 2; chk('45a Nullstellen', nst(z), {-2, 2}); chk('45a Volumen', 4*z.subs(x, 0)*3, 24)
    rr = R(1, 10)*x**3 - R(9, 10)*x**2 + R(12, 5)*x + 1; ex = extrema(rr)
    chk('45b H, T', [pts(ex, 'H'), pts(ex, 'T')], [(2, 3), (4, 2.6)]); chk('45b Ränder', [rr.subs(x, 0), rr.subs(x, 6)], [1, 4.6])
    mx, mn = rand_ext(rr, 0, 6); rmax = mx[0]; chk('45b größter Radius', rmax, 4.6)
    V = 6*(2*rmax)**2; chk('45b Volumen', V, 507.84); chk('45b Masse', R(7, 10)*V, 355.5, tol=0.02)
    h = -R(2, 100000)*x**3 + R(3, 1000)*x**2
    chk('46a Wendestelle', [w[0] for w in wende(h)], [50]); chk("46a h'(50)", sp.diff(h, x).subs(x, 50), 0.15)
    chk("46a h' an den Rändern", [sp.diff(h, x).subs(x, 0), sp.diff(h, x).subs(x, 100)], [0, 0])
    chk('46b Winkel', sp.deg(sp.atan(sp.Rational(15, 100))), 8.5, tol=0.05); chk_txt('46b eingehalten', 'ja' if float(sp.deg(sp.atan(0.15))) <= 10 else 'nein', 'ja')
    K2 = R(1, 10)*x**3 - R(1, 2)*x**2 + R(8, 5)*x + 8; E2 = 5*x
    chk('47a Schnittstellen im Bild', sorted(s2 for s2 in nst(K2 - E2) if 0 <= s2 <= 9), [2, 8]); chk_txt('47a Gewinn zwischen', vz((E2 - K2).subs(x, 5)), '+')
    chk('47b K(0)', K2.subs(x, 0), 8)
    chk('47 Bild: K(9) <= 60', [K2.subs(x, 9)], [54.8])
    p = 3 + 2*sp.sin(sp.pi*t/6); chk('47c Mittelwert (Max+Min)/2', (sp.maximum(p, t, sp.Interval(0, 24)) + sp.minimum(p, t, sp.Interval(0, 24)))/2, 3)

EINHEITEN = {'zone': zone, 'e1': e1, 'e2': e2, 'e3': e3, 'e4': e4, 'e5': e5}

if __name__ == '__main__':
    datei = sys.argv[1]
    EINHEITEN[datei]()
    zeilen = []
    for nr, s, b, ok in ZEILEN:
        zeilen.append(f"{nr} | Skript: {s} | Blatt: {b} | {'OK' if ok else 'ABWEICHUNG'}")
    n = sum(1 for z in ZEILEN if not z[3])
    zeilen.append(f"Abweichungen: {n}")
    txt = '\n'.join(zeilen)
    open(f'pruef_out_{datei}.txt', 'w', encoding='utf-8').write(txt + '\n')
    print(txt)
