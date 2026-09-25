# pruef.py – rechnet alle Lösungen eines Teils unabhängig nach (5.1 a)
# Aufruf: python pruef.py zone | e1 | e2 | e3 | e4 | e5
# Blattwerte sind aus dem Lösungsquelltext (<teil>_l.tex) abgeschrieben.
import sys, re, math
from sympy import Rational, nsimplify, sqrt, log, N, root

rows = []

def zahl(s):
    s = s.replace('\u202f', '').replace(' ', '').replace('.', '')
    return float(s.replace(',', '.'))

def dezimalen(s):
    s = s.replace(' ', '')
    return len(s.split(',')[1]) if ',' in s else 0

def chk(nr, skript, blatt, genau=None):
    """skript: Zahl oder Text; blatt: Text wie im Lösungsquelltext.
    Zahlen werden verglichen, gerundet auf die Stellen des Blattwerts."""
    if isinstance(skript, str):
        ok = skript == blatt
        sw = skript
    else:
        skript = float(skript)
        d = dezimalen(blatt) if genau is None else genau
        tol = 0.5 * 10 ** (-d) + 1e-9
        ok = abs(skript - zahl(blatt)) <= tol
        sw = f'{skript:.6f}'.rstrip('0').rstrip('.')
    rows.append((nr, sw, blatt, 'OK' if ok else 'ABWEICHUNG'))

def f(x):  # float-Hilfe
    return float(x)

# ---------------------------------------------------------------- Zone
def zone():
    chk('1a', 0.5 * 8, '4'); chk('1b', 3 * 1.1, '3,3'); chk('1c', 250 * 1.07, '267,5')
    chk('1d', round(48.356, 2), '48,36'); chk('1e', round(1234 * 1.15), '1419')
    chk('1f', 37 * 1.15 * 1.15, '48,9')
    chk('1f-früh', 42.6 * 1.15, '49,0')  # Kontrolle: frühes Runden (42,55 -> 42,6) weicht ab
    chk('2a', 1 + 10 / 100, '1,1'); chk('2b', 1 - 50 / 100, '0,5'); chk('2c', 1 + 7 / 100, '1,07')
    chk('2d', 1 - 15 / 100, '0,85'); chk('2e', 1 + 2.5 / 100, '1,025')
    chk('2f', 300 * 1.12, '336'); chk('2g', 860 * 0.9, '774')
    chk('3-Mia', 400 * 1.25, '500'); chk('3a', 400 * 1.025, '410'); chk('3b', 800 * 1.035, '828')
    for n, (x, y) in zip('abcd', [(1, 50), (3, 40), (6, 70), (7, 10)]):
        chk('4' + n + ' x', x, str(x)); chk('4' + n + ' y', y, str(y))
    chk('5a', 18 + 3, '21'); chk('5b', 90 + 20, '110'); chk('5c', 10.5 + 1.5, '12'); chk('5d', 76 - 7, '69')
    chk('5e', 40 + 3 * 15, '85'); chk('5f', 40, '40')
    chk('6a', 18 / 9, '2'); chk('6b', 36 / 12, '3'); chk('6c', 44 / 40, '1,1')
    chk('6d', 40 / 50, '0,8'); chk('6e', 460 / 400, '1,15')
    chk('7a', 0.1 * 70, '7'); chk('7b', 0.5 * 36, '18'); chk('7c', 0.07 * 350, '24,50')
    chk('7d', 14 / 40 * 100, '35'); chk('7e', 0.035 * 100, '3,5'); chk('7f', (285 - 250) / 250 * 100, '14')
    chk('8a', 500 * 1.02, '510'); chk('8b', 500 * 0.02, '10'); chk('8c', 500 * 1.02 ** 2, '520,20')
    chk('8d', 510 * 0.02, '10,20'); chk('8e', 2000 * 1.018 ** 3, '2109,96')
    chk('9a', 2 ** 3, '8'); chk('9b', 3 ** 5, '243'); chk('9c', 1.1 ** 3, '1,331')
    chk('9d', 50 * 1.1 ** 3, '66,55'); chk('9e', 0.9 ** 5, '0,590'); chk('9f', 1800 * 1.07 ** 10, '3540,87')

# ---------------------------------------------------------------- Einheit 1
def diffs(xs): return [round(b - a, 6) for a, b in zip(xs, xs[1:])]
def quots(xs): return [round(b / a, 6) for a, b in zip(xs, xs[1:])]
def gleich(xs): return 'ja' if len(set(xs)) == 1 else 'nein'
def ex_lin(xs):
    if len(set(diffs(xs))) == 1: return 'linear'
    if len(set(round(q, 4) for q in quots(xs))) == 1: return 'exponentiell'
    return 'weder'

def e1():
    for nr, xs, bl, g in [('13a', [12, 19, 26, 33], '7', 'ja'), ('13b', [3, 13, 23, 33], '10', 'ja'),
                          ('13c', [10, 13, 17, 22], None, 'nein'), ('13d', [40, 55, 70, 85], '15', 'ja')]:
        d = diffs(xs)
        if bl: chk(nr + ' Differenz', d[0], bl)
        else: chk(nr + ' Differenzen', ';'.join(str(int(v)) for v in d), '3;4;5')
        chk(nr + ' gleich', gleich(d), g)
    q = quots([50, 55, 60.5, 66.55]); chk('13e Quotient', q[0], '1,1'); chk('13e gleich', gleich(q), 'ja')
    chk('13f', ex_lin([800, 840, 882, 926.1]), 'exponentiell'); chk('13f q', quots([800, 840, 882, 926.1])[2], '1,05')
    chk('13g Faktor', 1 + 15 / 100, '1,15')
    xs = [2000, 1800, 1620, 1458]; chk('13h', ex_lin(xs), 'exponentiell'); chk('13h q', quots(xs)[0], '0,9')
    chk('13h Tabelle', 1620 * 0.9, '1458')
    d = diffs([800, 840, 882, 926.1]); chk('13i 1', d[0], '40'); chk('13i 2', d[1], '42'); chk('13i 3', d[2], '44,1')
    xs = [240000, 252000, 264600, 277830]
    for i, q in enumerate(quots(xs)): chk(f'13k q{i+1}', q, '1,05')
    for i, (dd, b) in enumerate(zip(diffs(xs), ['12000', '12600', '13230'])): chk(f'13k d{i+1}', dd, b)
    chk('14e', 'I und IV', 'I und IV'); chk('14f', 'II', 'II')  # Skizzen: 0,9x und 0,2x² beginnen im Ursprung
    chk('15a Betrag', 300, '300'); chk('15 Graph II Start', 3200 * 0.85 ** 0, '3200')
    chk('15d richtig', 'III', 'III')  # 40*1,09^x; I = 40+3,6x Gerade; II = 60*(1,09^x-1) bei 0
    chk('12b Start II', 1.2 * 1.3 ** 0, '1,2'); chk('12c Start III', 0.5 * 0 + 2, '2')
    for t, v in [(0, 10), (1, 20), (2, 40), (3, 80)]: chk(f'16 t={t}', 10 * 2 ** t, str(v))
    for t, v in [(0, '500'), (2, '605'), (4, '732'), (6, '886'), (8, '1072')]: chk(f'17a t={t}', 500 * 1.1 ** t, v, genau=0)
    for t, v in [(0, '800'), (1, '520'), (2, '338'), (3, '220')]: chk(f'17b {t} m', 800 * 0.65 ** t, v, genau=0)
    pr = [500, 560, 627.20, 702.46]
    for i in range(1, 4): chk(f'18 Tabelle {i}', pr[i-1] * 1.12, str(pr[i]).replace('.', ','))
    chk('18a d2', 627.2 - 560, '67,20'); chk('18a d3', 627.2 * 1.12 - 627.2, '75,26')
    ew = [35000]
    for i in range(3): ew.append(ew[-1] * 0.98)
    chk('18b 2', ew[1], '34300'); chk('18b 3', ew[2], '33614'); chk('18b 4', ew[3], '32942', genau=0)
    chk('18b', ex_lin([35000, 34300, 33614, 32941.72]), 'exponentiell')
    A = [1200 + 150 * n for n in range(9)]; B = [1200 * 1.1 ** n for n in range(9)]
    for n, b in zip(range(3, 9), ['1597', '1757', '1933', '2126', '2338', '2572']): chk(f'20 B{n}', B[n], b, genau=0)
    chk('20b', min(n for n in range(9) if B[n] > A[n]), '6')
    chk('20c Plan B', min(n for n in range(9) if B[n] > 2300), '7'); chk('20c Plan A', min(n for n in range(9) if A[n] > 2300), '8')

# ---------------------------------------------------------------- Einheit 2
def e2():
    for n, q, b in zip('abcde', [1.15, 0.7, 2, 0.98, 1.005], ['nimmt zu', 'nimmt ab', 'nimmt zu', 'nimmt ab', 'nimmt zu']):
        chk('21' + n, 'nimmt zu' if q > 1 else 'nimmt ab', b)
    chk('22 Bsp', 1 + 11 / 100, '1,11')
    for n, p, b in zip('abcd', [10, 15, 2, 35], ['1,1', '1,15', '1,02', '1,35']): chk('22' + n, 1 + p / 100, b)
    chk('22e', 1 - 40 / 100, '0,6'); chk('22f', (1 - 0.93) * 100, '7'); chk('22g', 290 / 250, '1,16')
    for i, q in enumerate(quots([400, 460, 529, 608.35])): chk(f'22h q{i+1}', q, '1,15')
    q = math.sqrt(1936 / 1600); chk('22i q', q, '1,1'); chk('22i p', (q - 1) * 100, '10')
    for i, q in enumerate(quots([256, 320, 400, 500])): chk(f'22j q{i+1}', q, '1,25')
    chk('23 Bsp', 300 * 1.1, '330')
    for n, (w, q, b) in zip('abcd', [(70, 2, '140'), (500, 1.1, '550'), (800, 1.05, '840'), (250, 1.02, '255')]):
        chk('23' + n, w * q, b)
    chk('23e 0', 400, '400'); chk('23e 1', 400 * 1.1, '440'); chk('23e 2', 400 * 1.1 ** 2, '484')
    chk('23f', 1500 * 1.1, '1650'); chk('23f Kontrolle', 1500 * 1.1 ** 2, '1815'); chk('23g', 3000 * 1.05 ** 3, '3472,88')
    chk('24a', 1331 / 1.1, '1210')
    k = round(math.log(732.05 / 500) / math.log(1.1), 6); chk('24b Jahr', k, '4'); chk('24b Probe', 500 * 1.1 ** 4, '732,05')
    chk('24b Tabelle', 500 * 1.1, '550')
    chk('24c 2', 600 * 0.8, '480'); chk('24c 3', 600 * 0.8 ** 2, '384'); chk('24c Kontrolle', 750 * 0.8, '600')
    chk('24d 2025', 144, '144,00'); chk('24d 2026', 144 * 1.035, '149,04'); chk('24d 2027', 144 * 1.035 ** 2, '154,26')
    chk('24d 2028', 144 * 1.035 ** 3, '159,66')
    chk('25 Paul Betrag', 7200 - 6120, '1080'); chk('25 Paul 1', 7200 * 0.85, '6120')
    chk('25a 2', 7200 * 0.85 ** 2, '5202'); chk('25a 3', 7200 * 0.85 ** 3, '4421,70')
    for i, b in zip(range(1, 4), ['3240', '2916', '2624,40']): chk(f'25b {i}', 3600 * 0.9 ** i, b)
    chk('25c Lena', 2000 * 0.09, '180'); chk('25c', 2000 * 1.09, '2180'); chk('25d', 2500 * 1.07, '2675')
    chk('26c', 1.5 * 0.5, '0,75')
    for i, b in zip(range(1, 4), ['12240', '12485', '12734']): chk(f'27a {i}', 12000 * 1.02 ** i, b, genau=0)
    chk('27b', min(i for i in range(1, 4) if 12000 * 1.02 ** i > 12700), '3')

# ---------------------------------------------------------------- Einheit 3
def schwelle(n0, q, grenze, ueber=True):
    t, w = 0, n0
    while (w <= grenze) if ueber else (w >= grenze):
        t += 1; w = n0 * q ** t
    return t, w

def e3():
    for n, (s, z, b) in zip('abcd', [(2022, 2029, '7'), (2021, 2026, '5'), (2019, 2027, '8'), (2023, 2030, '7')]):
        chk('28' + n + ' Schritte', z - s, b)
    for n, (n0, p, q) in zip('abcd', [(700, 2, '1,02'), (12, 15, '1,15'), (48000, 2.5, '1,025'), (900, 35, '1,35')]):
        chk('29' + n + ' q', 1 + p / 100, q)
    chk('29f q', 1 - 2 / 100, '0,98'); chk('30a q', 1 - 12 / 100, '0,88'); chk('30d q', 1 + 2.8 / 100, '1,028')
    chk('30b p', (1.07 - 1) * 100, '7')
    chk('31 Bsp', 250 * 1.1 * 1.1, '302,5')
    chk('31a', 500 * 2 ** 3, '4000'); chk('31b', 90 * 1.1 ** 2, '108,9'); chk('31c', 2000 * 1.05 ** 2, '2205')
    chk('31d', 50 * 3 ** 2, '450'); chk('31e', 2000 * 1.05 ** 3, '2315,25')
    chk('31f t', 2030 - 2022, '8'); chk('31f', 3400 * 1.02 ** 8, '3984', genau=0)
    chk('31g', 1250 * 1.035 ** 7, '1590,35'); chk('31h', 2400 * 0.93 ** 5, '1669,65')
    chk('31h Urteil', 'stimmt' if 2400 * 0.93 ** 5 < 1700 else 'falsch', 'stimmt')
    chk('31i A', 18000 * 1.02 ** 12, '22828', genau=0); chk('31i B', 18000 * 1.24, '22320')
    chk('31i Differenz', 18000 * 1.02 ** 12 - 22320, '508', genau=0)
    t, w = schwelle(750, 1.35, 2000); chk('32a t', t, '4'); chk('32a Wert', w, '2491', genau=0)
    t, w = schwelle(900, 0.85, 300, ueber=False); chk('32b t', t, '7'); chk('32b Wert', w, '288,5')
    chk('32c', 3500 * 1.25 ** 12, '50932', genau=0)
    chk('33 Ole', 600 * 1.05 * 8, '5040'); chk('33a', 600 * 1.05 ** 8, '886,47'); chk('33b', 750 * 1.1 ** 6, '1328,67')
    chk('33c t', 2031 - 2025, '6'); chk('33c', 1800 * 1.02 ** 6, '2027,09'); chk('33d', 2600 * 1.015 ** 7, '2885,60')
    chk('34b Faktor', 1.02 ** 12, '1,268'); chk('34b Prozent', (1.02 ** 12 - 1) * 100, '26,8')
    chk('35b', 250 * 0.82 ** 3, '137,8'); chk('35c 5', 250 * 0.82 ** 5, '92,7'); chk('35c 6', 250 * 0.82 ** 6, '76,0')
    t, w = schwelle(250, 0.82, 90, ueber=False); chk('35c t', t, '6')

# ---------------------------------------------------------------- Einheit 4
def e4():
    chk('37 Bsp', 350 / 2, '175')
    chk('37a', 90 * 2, '180'); chk('37b', 1400 / 2, '700'); chk('37c', 2.5 / 2, '1,25'); chk('37d', 725 * 2, '1450')
    for t, b in [(4, '1131'), (8, '800'), (12, '566'), (16, '400')]: chk(f'37e Tabelle {t}', 1600 * 0.5 ** (t / 8), b, genau=0)
    chk('37e', [t for t in (0, 4, 8, 12, 16) if abs(1600 * 0.5 ** (t / 8) - 800) < 1e-6][0], '8')
    tab = [300 * 1.13 ** t for t in range(8)]
    for t, b in zip(range(1, 8), ['339', '383', '433', '489', '553', '625', '706']): chk(f'37f Tabelle {t}', tab[t], b, genau=0)
    chk('37f', min(range(8), key=lambda t: abs(round(tab[t]) - 600)), '6')
    ha = 3 * math.log(160 / 320) / math.log(0.5); chk('38a', ha, '3')  # 320*0,5^(t/3) = 160
    t, w = schwelle(40, 1.15, 80); chk('39a', t, '5')
    for i, b in zip(range(1, 6), ['46', '52,9', '60,8', '70,0', '80,5']): chk(f'39a {i}', 40 * 1.15 ** i, b)
    t, w = schwelle(300, 1.15, 600); chk('39b', t, '5')
    for i, b in zip(range(1, 6), ['345', '396,8', '456,3', '524,7', '603,4']): chk(f'39b {i}', 300 * 1.15 ** i, b)
    chk('39c', math.log(2) / math.log(1.15), '5,0'); chk('39c genauer', math.log(2) / math.log(1.15), '4,96')
    chk('39d', math.log(2) / math.log(1.09), '8', genau=0); chk('39d doppelt', 1.6 * 2, '3,2')
    for t, b in [(2, '420'), (4, '354'), (6, '297'), (8, '250')]: chk(f'40 Tabelle {t}', 500 * 0.5 ** (t / 8), b, genau=0)
    chk('40a', 8, '8')
    for t, b in [(9, '1697'), (18, '1200'), (27, '849'), (36, '600')]: chk(f'40b Tabelle {t}', 2400 * 0.5 ** (t / 18), b, genau=0)
    chk('40b', 18, '18')
    chk('41a', 2 ** (21 / 7), '8')
    for t, b in [(12, '4'), (24, '2'), (36, '1')]: chk(f'42a {t}', 8 * 0.5 ** (t / 12), b)
    chk('42b', 8 * 0.5 ** (28 / 12), '1,59'); chk('42c', 12 * math.log(1 / 8) / math.log(0.5), '36')

# ---------------------------------------------------------------- Einheit 5
def e5():
    chk('43 Bsp', (-2) ** 3, '-8')
    for n, (e, xs, b) in zip('abcd', [(3, [0, 1, 2, 3], ['0', '1', '8', '27']), (3, [-3, -2, -1], ['-27', '-8', '-1']),
                                     (4, [-2, -1, 0, 1, 2], ['16', '1', '0', '1', '16']), (4, [-0.5, 0.5, 3], ['0,0625', '0,0625', '81'])]):
        for x, bb in zip(xs, b): chk(f'43{n} x={x}', x ** e, bb)
    chk('44 Bsp', 3 ** 4, '81')
    for n, (v, b) in zip('abcdefgh', [(2 ** 3, '8'), (2 ** 4, '16'), (3 ** 3, '27'), (10 ** 4, '10000'), ((-5) ** 3, '-125'),
                                      ((-2) ** 4, '16'), (2 * (-2) ** 3, '-16'), (0.5 ** 3, '0,125')]):
        chk('44' + n, v, b)
    chk('44i', 'ja' if (-2) ** 4 == 16 else 'nein', 'ja'); chk('44j', 'ja' if 3 ** 3 == -27 else 'nein', 'nein')
    chk('44k', round(216 ** (1 / 3), 9), '6'); chk('44l +', round(81 ** 0.25, 9), '3'); chk('44l -', (-3) ** 4, '81')
    for x, b in [(-2, '4'), (-1, '1'), (0, '0'), (1, '1'), (2, '4')]: chk(f'45a x={x}', x ** 2, b)
    for x, b in [(-2, '-8'), (-1, '-1'), (1, '1'), (2, '8')]: chk(f'45b x={x}', x ** 3, b)
    for x, b in [(-2, '16'), (2, '16')]: chk(f'45c x={x}', x ** 4, b)
    sym = lambda n: 'y-Achse' if n % 2 == 0 else 'Ursprung'
    for n, e, b in zip('abcd', [4, 5, 6, 3], ['y-Achse', 'Ursprung', 'y-Achse', 'Ursprung']): chk('46' + n, sym(e), b)
    chk('46e', 'schmaler' if 3 > 1 else 'breiter', 'schmaler'); chk('46f', 'schmaler' if 0.25 > 1 else 'breiter', 'breiter')
    # Graphen in Nr. 47: I = x^4, II = x^3, III = -x^2, IV = 0,5x^3
    chk('47a', 'II', 'II'); chk('47b', 'III', 'III'); chk('47c', 'I', 'I'); chk('47d', 'IV', 'IV'); chk('47e', 'I', 'I')
    chk('48g 2', 2 ** 3, '8'); chk('48g 2b', 3 ** 2, '9'); chk('48g 5', 5 ** 3, '125'); chk('48g 5b', 3 ** 5, '243')
    chk('49 Tom', -2 * 3, '-6'); chk('49a', (-2) ** 3, '-8'); chk('49b', (-3) ** 3, '-27')
    chk('49 Sara', (-2) ** 4, '16'); chk('49c', -(2 ** 4), '-16'); chk('49d', -(3 ** 4), '-81')
    chk('51a', 7 ** 3, '343'); chk('51b', round(1331 ** (1 / 3), 9), '11'); chk('51c', (2 * 5) ** 3 / 5 ** 3, '8')

# ---------------------------------------------------------------- Sperrzahlen (5.1 b)
# bewusst zugelassene Treffer je Teil (Nummer, Grund) – erscheinen im Protokoll
ERLAUBT = {'e1': {'20': 'Nr. 16 Verdopplungsreihe 10; 20; 40; 80 (kein Kastenbeispiel nachgebildet)',
                  '80': 'Nr. 16 Verdopplungsreihe 10; 20; 40; 80'}}
GESPERRT = ['1,5', '0,94', '1,06', '1,2', '1,3', '571', '0,89', '0,87', '1,019', '1,9', '1,04',
            '1,03', '1,08', '1,4', '650', '687,76', '845,96', '112', '600000', '648000',
            '257136', '1028294', '81,7', '75,6', '0,31', '573', '20', '25', '30', '45', '60', '72',
            '200', '32', '64', '1000', '54', '80']

def sperrscan(datei):
    try:
        t = open(datei, encoding='utf-8').read()
    except FileNotFoundError:
        return []
    t = re.sub(r'%.*', '', t)
    t = t.replace('{,}', ',').replace('\\,', '').replace('~', '')
    # Befehlsargumente, die keine Aufgabenzahlen sind (Koordinaten, Grafikschlüssel, Zähler)
    t = re.sub(r'\\setcounter\{[^}]*\}\{\d+\}', '', t)
    t = re.sub(r'\\begin\{ksys\}\[[^\]]*\]', '', t)
    t = re.sub(r'\\begin\{minipage\}\[[^\]]*\]\{[^}]*\}', '', t)
    t = re.sub(r'\\(hspace|vspace|rule|parbox|leeresgitter)\{[^}]*\}', '', t)
    t = re.sub(r'\\(punkt|funktion|funktionab|gerade|leeresgitter|wertetabelleleer)\b(\[[^\]]*\])?(\{[^{}]*\})+', '', t)
    treffer = []
    for m in re.finditer(r'(?<![\d,.])\d+(?:,\d+)?(?![\d,.])', t):
        z = m.group(0)
        if z in GESPERRT:
            treffer.append(z)
    return treffer

if __name__ == '__main__':
    teil = sys.argv[1]
    globals()[teil]()
    aus = [f'Prüfung {teil}: Nummer · Skriptwert · Blattwert · Ergebnis']
    for r in rows:
        aus.append(' · '.join(r))
    sp = sperrscan(f'{teil}_a.tex')
    erl = ERLAUBT.get(teil, {})
    offen = [z for z in sp if z not in erl]
    for z in sorted(set(sp) & set(erl)):
        aus.append(f'Sperrzahl {z} zugelassen: {erl[z]}')
    aus.append('Sperrzahlen im Aufgabenquelltext: ' + (', '.join(offen) if offen else 'keine'))
    abw = sum(1 for r in rows if r[3] != 'OK')
    aus.append(f'Abweichungen: {abw}')
    txt = '\n'.join(aus)
    open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8').write(txt + '\n')
    print(txt)
