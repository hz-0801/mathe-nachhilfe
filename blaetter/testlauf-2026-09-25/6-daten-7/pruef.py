# pruef.py – rechnet die Lösungen je Einheit unabhängig nach (Aufruf: python pruef.py zone|e1|e2)
import sys
from fractions import Fraction as F
from statistics import median, mean

teil = sys.argv[1]
zeilen = []

def chk(nr, skript, blatt, tol=None):
    s = float(skript); b = float(blatt)
    if tol is None:
        # Toleranz aus der Rundung des Blattwerts
        txt = str(blatt)
        dec = len(txt.split('.')[1]) if '.' in txt else 0
        tol = 0.5 * 10 ** (-dec) + 1e-9
    ok = abs(s - b) <= tol
    zeilen.append(f"{nr:<10} Skript {s:<14.6g} Blatt {b:<12} {'OK' if ok else 'ABWEICHUNG'}")
    return ok

def chkbool(nr, skript, blatt):
    ok = (skript == blatt)
    zeilen.append(f"{nr:<10} Skript {str(skript):<14} Blatt {str(blatt):<12} {'OK' if ok else 'ABWEICHUNG'}")

def chkseq(nr, skript, blatt):
    ok = list(skript) == list(blatt)
    zeilen.append(f"{nr:<10} Skript {skript} Blatt {blatt} {'OK' if ok else 'ABWEICHUNG'}")

def pct(t, g): return 100 * F(t, 1) / g
def winkel(p): return F(p) / 100 * 360

if teil == 'zone':
    obst = {'Apfel': 7, 'Banane': 5, 'Erdbeere': 9, 'Kiwi': 3}
    n = sum(obst.values())
    chk('1a', obst['Apfel'], 7)
    chkbool('1b', max(obst, key=obst.get), 'Erdbeere')
    chk('1c', n, 24)
    chk('1d Bruch', F(9, n), 3/8); chk('1d %', pct(9, n), 37.5)
    chk('1e Bruch', F(3, n), 1/8); chk('1e %', pct(3, n), 12.5)
    chk('2a', pct(50, 100), 50); chk('2b', pct(3, 10), 30); chk('2c', pct(18, 40), 45)
    chk('2d', F(5, 100), 0.05); chk('2e', 100 - 45 - 30, 25); chk('2f', pct(14, 20), 70)
    mus = {'Januar': 40, 'Februar': 25, 'März': 35, 'April': 50, 'Mai': 45}
    chk('3a', mus['Januar'], 40); chk('3b', mus['April'], 50); chk('3c', mus['Februar'], 25)
    chk('3d', mus['März'] * 1000, 35000)
    chkseq('4a', sorted([7, 3, 9, 5]), [3, 5, 7, 9])
    chkseq('4b', sorted([21, 12, 18, 15]), [12, 15, 18, 21])
    chkseq('4c', sorted([1.7, 1.65, 1.8, 1.72]), [1.65, 1.7, 1.72, 1.8])
    chk('4d', 1.5 + 3 * 0.05, 1.65); chk('4e', 1.5 + 7 * 0.05, 1.85)
    chk('5a', 3 * 10, 30); chk('5b', 60 / 10, 6); chk('5c', 4.5 * 10, 45); chk('5d', 8 / 10, 0.8); chk('5e', 7.5 * 10, 75)
    chk('6a', F(180, 360), 0.5); chk('6b', F(90, 360), 0.25); chk('6c', 360 / 3, 120); chk('6d', 360 / 6, 60)
    chk('8a', 2.5 + 1.5, 4); chk('8b', 8.4 / 2, 4.2); chk('8c', 0.4 * 250, 100)
    chk('8d', round(8.46, 1), 8.5); chk('8e', round(17.96, 1), 18.0); chk('8f', 23 / 7, 3.3)
    L = [14, 9, 17, 11, 20]
    chk('9a', min(L), 9); chk('9b', max(L), 20); chk('9c', max(L) - min(L), 11)
    chk('9d', mean(L), 14.2); chk('9e', median(L), 14)
    chk('10a', 80 / 2, 40); chk('10b', 35 * 2, 70); chk('10c', F(240, 3), 80)
    chk('10d', 150 * F(4, 3), 200); chk('10e', 120 * F(3, 4), 90)
    chk('11a', pct(10, 25), 40); chk('11b', pct(9, 30), 30)

elif teil == 'e1':
    chk('14 Bsp', 30 / 10, 3)
    for nr, p, b in [('14a', 40, 4), ('14b', 70, 7), ('14c', 20, 2), ('14d', 90, 9), ('15e', 65, 6.5)]:
        chk(nr, p / 10, b)
    for nr, p, b in [('15f Rad', 45, 4.5), ('15f Bus', 40, 4), ('15f Fuß', 15, 1.5)]:
        chk(nr, p / 10, b)
    chk('15f Summe', 45 + 40 + 15, 100)
    rest = 100 - 50 - 20
    chk('15g Rest', rest, 30); chk('15g cm', rest / 10, 3)
    for nr, p, b in [('15h Brötchen', 40, 4), ('15h Getränke', 30, 3), ('15h Müsli', 25, 2.5), ('15h Kekse', 5, 0.5)]:
        chk(nr, p / 10, b)
    chk('15h Summe', 40 + 30 + 25 + 5, 100)
    chk('16 Bsp', winkel(20), 72)
    for nr, p, b in [('16a', 50, 180), ('16b', 25, 90), ('16c', 10, 36), ('16d', 75, 270), ('16e', 15, 54), ('16f', 5, 18), ('16g', F(25, 2), 45)]:
        chk(nr, winkel(p), b)
    chk('16h', F(3, 8) * 360, 135)
    chk('16i', F(13, 40) * 360, 117)
    chk('16j', F(4, 13) * 360, 111, tol=0.5)
    chk('17 Bsp', winkel(25), 90)
    chk('17a', winkel(40), 144)
    for nr, p, b in [('17b Tee', 50, 180), ('17b Kakao', 45, 162), ('17b Milch', 5, 18)]:
        chk(nr, winkel(p), b)
    rest = 100 - F(85, 2) - F(55, 2) - F(37, 2)
    chk('18c Rest', rest, 11.5)
    w = [winkel(F(85, 2)), winkel(F(55, 2)), winkel(F(37, 2)), winkel(rest)]
    for nr, x, b in zip(['18c Sport', '18c Musik', '18c Lesen', '18c Sonst'], w, [153, 99, 67, 41]):
        chk(nr, x, b, tol=0.5)
    chk('18c Summe gerundet', sum(round(float(x)) for x in w), 360)
    chk('18c exakt Lesen', winkel(F(37, 2)), 66.6); chk('18c exakt Sonst', winkel(rest), 41.4)
    chk('19a', 50, 50); chk('19b', 25, 25); chk('19c', 100 / 3, 33, tol=0.5); chk('19d', 100 / 6, 17, tol=0.5)
    chk('20a Summe', 55 + 25 + 20, 100)
    sonst = 100 - 34 - 10 - 24 - 18
    chk('20b Sonstiges', sonst, 14)
    chk('20b Winkel', F(72, 3200) * 360, 8.1)
    for nr, p, b in [('21a Rad', 40, 144), ('21a Bus', 45, 162), ('21a Fuß', 15, 54), ('21b Kakao', 55, 198), ('21b Tee', 20, 72), ('21b Wasser', 25, 90)]:
        chk(nr, winkel(p), b)
    chk('21c %', pct(12, 300), 4); chk('21c Winkel', F(12, 300) * 360, 14.4); chk('21c falsch', F(12, 100) * 360, 43.2)
    chk('21d %', pct(9, 450), 2); chk('21d Winkel', F(9, 450) * 360, 7.2)
    chk('22a', F(360, 100), 3.6)
    for nr, a, b in [('23 Fußball', 36, 45), ('23 Schwimmen', 24, 30), ('23 Rad', 32, 40), ('23 Tanzen', 16, 20)]:
        chk(nr, pct(a, 80), b)
    chk('23 Summe', pct(36 + 24 + 32 + 16, 80), 135)

elif teil == 'e2':
    # 24 Vorstufe: Startwerte
    chk('24b', 80, 80); chk('24c', 1.5, 1.5)
    fb = {'Mai': 18, 'Juni': 34, 'Juli': 46, 'August': 41, 'September': 12}
    chkbool('25a', max(fb, key=fb.get) == 'Juli', True)
    chkbool('25b', fb['Mai'] * 1000 == 18000, True)
    chkbool('25c', fb['September'] * 1000 > 15000, False)
    chkbool('25d', fb['August'] * 1000 == 4100, False)
    chkbool('25e', fb['Juni'] < fb['Juli'] < fb['August'], False)
    chkbool('25f', (fb['Juli'] - fb['Juni']) * 1000 == 12000, True)
    u = {'Freunde': 32, 'Gaming': 20, 'Sport': 24, 'Musik': 15, 'Lesen': 9}
    chk('26 Summe', sum(u.values()), 100)
    chkbool('26g', u['Freunde'] + u['Gaming'] > 50, True)
    chkbool('26h', F(u['Musik']) * F(4, 3) == u['Gaming'], True)
    chkbool('26i', abs(100 / 15 - u['Musik']) < 1e-9, False); chk('26i 1/15', 100 / 15, 6.7)
    lesen_anz = F(u['Lesen'], 100) * 600
    chk('26j Lesen Anzahl', lesen_anz, 54)
    chkbool('26j', (u['Sport'] > u['Gaming']) and (lesen_anz > 60), False)
    chkbool('26k1', u['Freunde'] + u['Lesen'] < 50, True); chk('26k1 %', u['Freunde'] + u['Lesen'], 41)
    chkbool('26k2', 100 / 5 == u['Sport'], False)
    chk('27a', 400, 400)
    chk('27b Differenz', 440 - 420, 20)
    chk('27b Säulen scheinbar', F(440 - 400, 420 - 400), 2)
    chk('27c', pct(20, 420), 4.8)
    ap = [2.40, 2.45, 2.50, 2.55, 2.60]
    chk('27e Säulenverhältnis', (ap[-1] - 2.30) / (ap[0] - 2.30), 3)
    chk('27e Anstieg %', (ap[-1] - ap[0]) / ap[0] * 100, 8.3)
    ki = {2019: 120, 2020: 105, 2021: 95, 2022: 100, 2023: 80, 2024: 70, 2025: 60}
    jahre = sorted(ki)
    chkbool('28b', all(ki[a] > ki[b] for a, b in zip(jahre, jahre[1:])), False)
    chk('28b Anstieg 2022', ki[2022] - ki[2021], 5)
    rate = (ki[2019] - ki[2025]) / (2025 - 2019)
    chk('28c Rückgang je Jahr', rate, 10); chk('28c Jahr 0', 2025 + ki[2025] / rate, 2031)
    bib = {2021: 42, 2022: 40, 2023: 41, 2024: 37, 2025: 35}
    for j, b in bib.items():
        chk(f'29a {j}', bib[j], b)
    jb = sorted(bib)
    chkbool('29d jedes Jahr', all(bib[a] > bib[b] for a, b in zip(jb, jb[1:])), False)
    chk('29d Rückgang %', (bib[2021] - bib[2025]) / bib[2021] * 100, 16.7)
    chk('29d Verhältnis', bib[2025] / bib[2021], 0.83)
    chk('29d Säulen scheinbar', (bib[2025] - 30) / (bib[2021] - 30), 0.42)
    a7 = [6, 10, 13, 16, 22]; b7 = [9, 12, 14, 15, 19]
    chk('30a', a7[2], 13); chk('30b min', a7[0], 6); chk('30b max', a7[4], 22)
    chk('30c Q1', a7[1], 10); chk('30c Q3', a7[3], 16); chk('30d', a7[4] - a7[0], 16)
    chk('30e von', b7[1], 12); chk('30e bis', b7[3], 15)
    chk('30f Median 7b', b7[2], 14); chk('30f Spannw 7b', b7[4] - b7[0], 10)
    chk('30f Box 7a', a7[3] - a7[1], 6); chk('30f Box 7b', b7[3] - b7[1], 3)
    chk('30 Bsp Spannw', 15 - 2, 13)
    liste = [9, 4, 13, 5, 7, 11, 2, 9, 5, 8, 6]
    s = sorted(liste); n = len(s)
    med = median(s); unten = s[:n // 2]; oben = s[(n + 1) // 2:]
    q1 = median(unten); q3 = median(oben)
    # Gegenprobe: Konvention mit Median in beiden Hälften
    q1b = median(s[:(n + 1) // 2]); q3b = median(s[n // 2:])
    chkbool('31c Konventionen gleich', (q1 == q1b) and (q3 == q3b), True)
    for nr, x, b in [('31c min', s[0], 2), ('31c Q1', q1, 5), ('31c Median', med, 7), ('31c Q3', q3, 9), ('31c max', s[-1], 13)]:
        chk(nr, x, b)
    chk('32a Differenz', 320 - 260, 60); chk('32a %', pct(60, 260), 23, tol=0.5)
    chk('32a scheinbar', F(320 - 200, 260 - 200), 2)
    chk('32b scheinbar', F(65 - 50, 55 - 50), 3); chk('32b %', pct(10, 55), 18.2)
    plaetze = 5 * 20; fehl = 125 - plaetze
    chk('34a fehlen', fehl, 25); chk('34a Ständer', -(-fehl // 20), 2)
    chk('34b', (125 - 84) / 84 * 100, 48.8)

abw = sum(1 for z in zeilen if z.endswith('ABWEICHUNG'))
out = '\n'.join(zeilen) + f"\nAbweichungen: {abw}\n"
print(out)
open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8').write(out)
