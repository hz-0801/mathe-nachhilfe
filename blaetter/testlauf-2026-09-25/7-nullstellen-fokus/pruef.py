# pruef.py – Mindestprüfung 5.1 a) für den Fokus Nullstellen (quadratische-funktionen.md, Einheit 4)
# Aufruf: python pruef.py zone | e4   → schreibt pruef_out_<datei>.txt
# Skriptwerte werden mit sympy unabhängig gerechnet; Blattwerte sind aus dem Lösungsquelltext abgetippt.
import sys
import sympy as sp

x = sp.symbols('x', real=True)
zeilen = []
abw = 0


def fmt(v):
    if isinstance(v, (list, tuple, set)):
        return '{' + ', '.join(fmt(e) for e in sorted(v, key=lambda t: float(t))) + '}'
    return str(sp.nsimplify(v)) if not isinstance(v, float) else f'{v:.4f}'


def gleich(a, b, tol=0.006):
    """Zahlenvergleich: Mengen elementweise, gerundete Blattwerte mit Toleranz."""
    if isinstance(a, (list, tuple, set)) or isinstance(b, (list, tuple, set)):
        a = sorted([float(t) for t in a]); b = sorted([float(t) for t in b])
        return len(a) == len(b) and all(abs(p - q) <= tol for p, q in zip(a, b))
    if isinstance(a, bool) or isinstance(b, bool):
        return a == b
    if isinstance(a, sp.Basic) and not a.is_number:
        return sp.simplify(sp.expand(a) - sp.expand(b)) == 0
    return abs(float(a) - float(b)) <= tol


def pruefe(nr, skript, blatt):
    global abw
    ok = gleich(skript, blatt)
    if not ok:
        abw += 1
    s = str(skript) if isinstance(skript, (bool, str)) else fmt(skript)
    b = str(blatt) if isinstance(blatt, (bool, str)) else fmt(blatt)
    zeilen.append(f'{nr:8s} Skript: {s:40s} Blatt: {b:40s} {"OK" if ok else "ABWEICHUNG"}')


def nst(term):
    """reelle Nullstellen eines Terms in x"""
    return sorted(sp.solve(sp.Eq(term, 0), x), key=lambda t: float(t))


def anzahl(term):
    return len(nst(term))


def zone():
    pruefe('1a', sp.Integer(-5)**2, 25)
    pruefe('1b', sp.Rational(3, 2)**2, 2.25)
    pruefe('2a', nst(2*x - 8), [4])
    pruefe('2b', nst(-3*x - 6), [-2])
    pruefe('3a', sp.expand((x + 5)**2), x**2 + 10*x + 25)
    pruefe('3b', sp.expand((x - 3)**2 - 5), x**2 - 6*x + 4)
    pruefe('4a', round(float(sp.sqrt(7)), 2), 2.65)
    pruefe('4b', bool(sp.sqrt(-4).is_real), False)
    pruefe('5a', nst(x**2 - 64), [8, -8])
    pruefe('5b', nst(x**2 + 4*x - 12), [2, -6])


def gerundet(term):
    return [round(float(t), 2) for t in nst(term)]


def pq_radikand(p, q):
    return sp.Rational(p, 1)**2 / 4 - q if isinstance(p, int) else (p / 2)**2 - q


def e4():
    # 6 Vorstufe: Gleichung f(x) = 0 bzw. f(x) = g(x) – Vergleich der Differenzterme
    pruefe('6d', sp.expand((x**2 - 1) - (x + 5)), x**2 - x - 6)
    pruefe('6e', sp.expand((x + 1)**2 - (-x + 3)), x**2 + 3*x - 2)
    # Beispiel 7
    pruefe('7 Bsp', nst((x - 1)**2 - 9), [4, -2])
    pruefe('7a', nst(x**2 - 25), [5, -5])
    pruefe('7b', nst((x - 4)**2 - 1), [5, 3])
    pruefe('7c', nst((x - 6)**2 - 4), [8, 4])
    pruefe('7d', nst((x - 3)**2 - 25), [8, -2])
    pruefe('8a', nst((x + 2)**2 - 9), [1, -5])
    pruefe('8b', nst((x + 5)**2 - 4), [-3, -7])
    pruefe('8c', nst((x - 7)**2), [7])
    pruefe('8d', nst((x + 1)**2 + 4), [])
    # 9 Anzahl ohne Rechnung (Skript rechnet trotzdem)
    pruefe('9a', anzahl((x - 3)**2 - 2), 2)
    pruefe('9b', anzahl((x + 4)**2 + 1), 0)
    pruefe('9c', anzahl((x + 6)**2), 1)
    pruefe('9d', anzahl(-(x - 2)**2 + 5), 2)
    pruefe('9e', anzahl(-(x + 1)**2 - 3), 0)
    pruefe('9g', anzahl(-(x - 4)**2 - 1), 0)
    # 10 p-q-Formel; Zwischenwerte Radikand
    pruefe('10a Rad', pq_radikand(-2, -15), 16)
    pruefe('10a', nst(x**2 - 2*x - 15), [5, -3])
    pruefe('10b Rad', pq_radikand(-8, 12), 4)
    pruefe('10b', nst(x**2 - 8*x + 12), [6, 2])
    pruefe('10c Rad', pq_radikand(4, -21), 25)
    pruefe('10c', nst(x**2 + 4*x - 21), [3, -7])
    pruefe('10d Rad', pq_radikand(10, 16), 9)
    pruefe('10d', nst(x**2 + 10*x + 16), [-2, -8])
    pruefe('11a Rad', pq_radikand(-5, 6), 0.25)
    pruefe('11a', nst(x**2 - 5*x + 6), [3, 2])
    pruefe('11b Rad', pq_radikand(3, -10), 12.25)
    pruefe('11b', nst(x**2 + 3*x - 10), [2, -5])
    pruefe('11c', nst(x**2 - 10*x + 25), [5])
    pruefe('11d Rad', pq_radikand(4, 7), -3)
    pruefe('11d', nst(x**2 + 4*x + 7), [])
    # 12 Wurzel bleibt stehen
    pruefe('12a exakt', nst((x - 1)**2 - 3), [1 + sp.sqrt(3), 1 - sp.sqrt(3)])
    pruefe('12a gerund.', gerundet((x - 1)**2 - 3), [2.73, -0.73])
    pruefe('12b exakt', nst((x + 3)**2 - 7), [-3 + sp.sqrt(7), -3 - sp.sqrt(7)])
    pruefe('12b gerund.', gerundet((x + 3)**2 - 7), [-0.35, -5.65])
    pruefe('12c Rad', pq_radikand(-4, -2), 6)
    pruefe('12c gerund.', gerundet(x**2 - 4*x - 2), [4.45, -0.45])
    # 13/14 Streckfaktor
    pruefe('13a normiert', sp.expand((2*x**2 + 4*x - 16) / 2), x**2 + 2*x - 8)
    pruefe('13a', nst(2*x**2 + 4*x - 16), [2, -4])
    pruefe('13b normiert', sp.expand((3*x**2 - 21*x + 30) / 3), x**2 - 7*x + 10)
    pruefe('13b Rad', pq_radikand(-7, 10), 2.25)
    pruefe('13b', nst(3*x**2 - 21*x + 30), [5, 2])
    pruefe('13c normiert', sp.expand((-x**2 + 4*x + 5) / -1), x**2 - 4*x - 5)
    pruefe('13c', nst(-x**2 + 4*x + 5), [5, -1])
    pruefe('14a', nst(2*(x - 3)**2 - 18), [6, 0])
    pruefe('14b', nst(-(x + 4)**2 + 1), [-3, -5])
    # 15 Prüfungshöhe (verfremdete Originale)
    pruefe('15a normiert', sp.expand((2*x**2 - 2*x - 24) / 2), x**2 - x - 12)
    pruefe('15a', nst(2*x**2 - 2*x - 24), [4, -3])
    pruefe('15b exakt', nst(x**2 + 4*x - 1), [-2 + sp.sqrt(5), -2 - sp.sqrt(5)])
    pruefe('15b gerund.', gerundet(x**2 + 4*x - 1), [0.24, -4.24])
    pruefe('15c Nachweis', sp.expand((x - 4)**2 - 7), x**2 - 8*x + 9)
    pruefe('15c exakt', nst(x**2 - 8*x + 9), [4 + sp.sqrt(7), 4 - sp.sqrt(7)])
    pruefe('15c gerund.', gerundet(x**2 - 8*x + 9), [6.65, 1.35])
    # 16/17 Fehler finden: richtige Rechnung und die vorgegebene falsche
    pruefe('16a', nst((x + 1)**2 - 49), [6, -8])
    pruefe('16b', nst((x - 5)**2 - 36), [11, -1])
    pruefe('17a Ben', [round(-6 + float(sp.sqrt(26)), 2), round(-6 - float(sp.sqrt(26)), 2)], [-0.90, -11.10])
    pruefe('17a', nst(2*x**2 + 12*x + 10), [-1, -5])
    pruefe('17b', nst(3*x**2 - 12*x - 36), [6, -2])
    # 18 Anwendung
    h = -sp.Rational(1, 10)*(x - 4)**2 + sp.Rational(36, 10)
    pruefe('18a', h.subs(x, 0), 2)
    pruefe('18b', nst(h), [10, -2])
    pruefe('18b Lösung', max(nst(h)), 10)


if __name__ == '__main__':
    datei = sys.argv[1]
    {'zone': zone, 'e4': e4}[datei]()
    zeilen.append(f'Abweichungen: {abw}')
    text = '\n'.join(zeilen)
    print(text)
    with open(f'pruef_out_{datei}.txt', 'w', encoding='utf-8') as f:
        f.write(text + '\n')
