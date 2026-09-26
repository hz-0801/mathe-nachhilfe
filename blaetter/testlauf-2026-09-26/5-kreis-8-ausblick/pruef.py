# pruef.py – rechnet die Lösungen einer Einheit unabhängig nach (Kreis, Kl. 8)
# Aufruf: python pruef.py zone|e1|e2|e3  -> schreibt pruef_out_<datei>.txt
# BLATT: Werte wortgleich aus dem Lösungsquelltext (<datei>_l.tex) übertragen.
import sys, math
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as Fr

PI = math.pi

def rnd(x, n):
    q = Decimal(1).scaleb(-n)
    return float(Decimal(repr(x)).quantize(q, rounding=ROUND_HALF_UP))

def dez(s):
    """Blattwert '11,4' -> (11.4, Stellen)"""
    s = s.strip()
    if '/' in s:
        a, b = s.split('/')
        return Fr(int(a), int(b)), None
    n = len(s.split(',')[1]) if ',' in s else 0
    return float(s.replace(',', '.')), n

# ---------- Skriptwerte (unabhängig gerechnet) ----------
def zone():
    S = {}
    S['1a'] = 0.5*8; S['1b'] = 2.5*4; S['1c'] = 3.2*1.5; S['1d'] = 4.37*2.6
    S['1e'] = 25/3.2; S['1f'] = 3.96*5.05; S['1g'] = 6.35*1.5*4
    S['1g-zwischenrunden'] = rnd(6.35*1.5, 1)*4
    S['2a-u'] = 2*(3+5); S['2a-A'] = 3*5; S['2b-u'] = 4*4; S['2b-A'] = 4*4
    S['2c-u'] = 2*(2.5+4); S['2c-A'] = 2.5*4; S['2d-u'] = 2*(0.5+2); S['2d-A'] = 0.5*2
    S['3d'] = 18.4/4; S['3e'] = 60/(5*4)
    S['4a'] = 6**2; S['4b'] = math.sqrt(49); S['4c'] = 1.5**2; S['4d'] = 0.5**2
    S['4e'] = math.sqrt(12.25); S['4f'] = math.sqrt(30); S['4g'] = math.sqrt(36); S['4h'] = math.sqrt(2.56)
    S['5a'] = 3.5**2; S['5b'] = math.sqrt(64)
    S['6a1'] = 4**2; S['6a2'] = 2*4; S['6b1'] = 2.5**2; S['6b2'] = 2*2.5
    S['6c1'] = math.sqrt(36); S['6c2'] = 36/2; S['6d1'] = 0.3**2; S['6d2'] = 2*0.3
    S['7a'] = 360; S['7b'] = 90; S['7c'] = 180; S['7d'] = 65  # Zeichnung \winkel[4]{65}
    S['7e'] = 360-130; S['7f'] = 360-275
    S['9a'] = Fr(5, 20); S['9a%'] = 5/20*100; S['9b'] = Fr(30, 60); S['9b%'] = 30/60*100
    S['9c'] = Fr(42, 120); S['9c%'] = 42/120*100; S['9d'] = Fr(50, 360); S['9d%'] = 50/360*100
    S['9e'] = Fr(80-20, 80); S['9e%'] = (80-20)/80*100
    return S

def strecke(w1, w2=None):
    """Strecke im Kreis: Radius (von M), sonst Abstand der Sehnenmitte von M"""
    if w2 is None:
        return 'Radius'
    d = abs(math.cos(math.radians((w2 - w1) / 2)))
    return 'Durchmesser' if d < 1e-9 else 'keins'

RAND = {'Borte': 'Umfang', 'Rasen': 'Fläche', 'Soße': 'Fläche', 'Abrollen': 'Umfang', 'Zaun': 'Umfang',
        'Tischdecke': 'Fläche', 'Tellerkante': 'Umfang', 'Teppich': 'Fläche', 'Lichterkette': 'Umfang', 'Farbe': 'Fläche'}

def e1():
    S = {}
    S['10a'] = strecke(40); S['10b'] = strecke(150, 330); S['10c'] = strecke(200, 280)
    S['10d'] = 'Durchmesser'  # von Rand zu Rand durch die Mitte
    S['10e'] = 'Radius'       # Zirkelöffnung = Abstand Mitte–Rand
    for k, w in zip('abcde', ['Borte', 'Rasen', 'Soße', 'Abrollen', 'Zaun']):
        S['11' + k] = RAND[w]
    S['12a'] = 2*3; S['12b'] = 2*6; S['12c'] = 2*3.5; S['12d'] = 10/2; S['12e'] = 14/2
    S['12f'] = 9/2; S['12g'] = 9.6/2; S['12h'] = 1.2/2*100
    S['14b'] = 3/2; S['14c'] = 4.6/2
    for k, (d, u) in {'15Dose': (7.4, 23.2), '15Teller': (24.0, 75.5), '15Münze': (2.3, 7.2), '15Eimer': (30.0, 94.0)}.items():
        S[k] = u/d
    S['15a'] = PI*50
    S['16a'] = PI*3; S['16b'] = PI*6; S['16c'] = PI*9; S['16d'] = PI*20; S['16e'] = 2*PI*4; S['16f'] = 2*PI*1.8
    S['17a'] = 47.1/PI; S['17b'] = 88/PI; S['17c'] = 37.7/(2*PI); S['17d'] = 100/(2*PI)
    S['18a'] = PI*12/2; S['18b'] = PI*7; S['18c'] = PI*12/2 + 12; S['18d'] = 2*PI*3.8
    S['19a-falsch'] = PI*7; S['19a'] = PI*14; S['19b-falsch'] = PI*36; S['19b'] = 2*PI*6
    S['21a'] = PI*70; S['21b'] = 500*PI*0.7; S['21c'] = 5000/(PI*0.7); S['21c-ganz'] = math.ceil(5000/(PI*0.7))
    return S

def e2():
    S = {}
    A = lambda r: PI*r*r
    for k, w in zip('abcde', ['Tischdecke', 'Tellerkante', 'Teppich', 'Lichterkette', 'Farbe']):
        S['22' + k] = RAND[w]
    S['23a'] = A(1); S['23b'] = A(6); S['23c'] = A(7); S['23d'] = A(10); S['23e'] = A(18/2); S['23f'] = A(5.4/2)
    S['24a'] = A(6)/2; S['24b'] = A(12)/4; S['24c'] = A(14/2)/2; S['24d'] = A(4)*3/4
    # 25: Figur -> Term (Anteil aus dem grauen Sektor, Radius aus der Beschriftung)
    S['25a'] = f'{Fr(90,360)}·π·{3}²'; S['25b'] = f'{Fr(180,360)}·π·{8//2}²'; S['25c'] = f'{Fr(270,360)}·π·{2}²'
    S['26a'] = 'Halbkreis r=5'; S['26b'] = 'Viertelkreis r=6'
    for k, r in {'27K1': 6, '27K2': 9/2, '27K3': 2.4/2, '27K4': 22.0/(2*PI)}.items():
        S[k+'r'] = r; S[k+'d'] = 2*r; S[k+'u'] = 2*PI*r; S[k+'A'] = A(r)
    S['28a'] = math.sqrt(154/PI); S['28b'] = math.sqrt(314/PI); S['28c-r'] = math.sqrt(20/PI); S['28c'] = 2*math.sqrt(20/PI)
    S['28d'] = A(3.46/2)
    S['29a-falsch'] = A(12); S['29a'] = A(6); S['29b-falsch'] = 2*PI*9; S['29b'] = A(9); S['29c-falsch'] = PI*14; S['29c'] = A(7)
    S['31a'] = A(0.6); S['31b'] = PI*1.2; S['31c'] = 2*PI*3.5; S['31d'] = A(3.5)
    S['32a-gross'] = A(15); S['32a-klein'] = 2*A(10)
    S['32b-gross'] = 8/(A(15)/100); S['32b-klein'] = 9/(2*A(10)/100)
    S['32c'] = 'groß' if S['32b-gross'] < S['32b-klein'] else 'klein'
    return S

TEIL = {Fr(1, 2): 'Halbkreis', Fr(1, 4): 'Viertelkreis', Fr(3, 4): 'Dreiviertelkreis', Fr(1, 8): 'Achtelkreis', Fr(1, 3): 'Drittelkreis'}

def e3():
    S = {}
    anteil = lambda a: Fr(a, 360)
    bogen = lambda a, r: a/360*2*PI*r
    aus = lambda a, r: a/360*PI*r*r
    for k, (w1, w2) in zip(['33-1', '33-2', '33-3', '33-4', '33-5'], [(0, 180), (90, 180), (0, 270), (0, 45), (90, 210)]):
        S[k] = TEIL[anteil(w2 - w1)]
    S['34a'] = anteil(90); S['34b'] = anteil(180); S['34c'] = anteil(60); S['34d'] = anteil(120)
    S['34e'] = 36/360*100; S['34f'] = 100/360*100; S['34g'] = (360-125)/360*100
    S['35a'] = 360/4; S['35b'] = 360*2/3; S['35c'] = 0.30*360
    S['36a'] = bogen(90, 4); S['36b'] = bogen(60, 9); S['36c'] = bogen(135, 8); S['36d'] = bogen(250, 2.5)
    S['37a'] = aus(90, 4); S['37b'] = aus(120, 6); S['37c'] = aus(200, 7.5); S['37d'] = aus(300, 4.5)
    S['38a'] = bogen(90, 4)+8; S['38b'] = bogen(60, 12)+24; S['38c'] = bogen(150, 5)+10
    S['39a'] = PI*(6**2-4**2); S['39b'] = PI*(15**2-10**2); S['39c'] = PI*(9**2-(9-3)**2)
    S['40a'] = anteil(40); S['40a-falsch'] = Fr(40, 180); S['40b-falsch'] = bogen(90, 6); S['40b'] = bogen(90, 6)+12
    S['40c-falsch'] = 110/360*100; S['40c'] = (360-110)/360*100
    S['42a'] = aus(150, 7); S['42b'] = bogen(150, 7); S['42c'] = 80/(PI*49)*360
    S['43a-Rad'] = 18/40*100; S['43a-Bus'] = 12/40*100; S['43a-Fuss'] = 10/40*100
    S['43b-Rad'] = 18/40*360; S['43b-Bus'] = 12/40*360; S['43b-Fuss'] = 10/40*360
    return S

BLATT = {
 'e3': {
  '33-1':'Halbkreis','33-2':'Viertelkreis','33-3':'Dreiviertelkreis','33-4':'Achtelkreis','33-5':'Drittelkreis',
  '34a':'1/4','34b':'1/2','34c':'1/6','34d':'1/3','34e':'10','34f':'27,8','34g':'65,3',
  '35a':'90','35b':'240','35c':'108',
  '36a':'6,3','36b':'9,4','36c':'18,8','36d':'10,9',
  '37a':'12,6','37b':'37,7','37c':'98,2','37d':'53,0',
  '38a':'14,3','38b':'36,6','38c':'23,1',
  '39a':'62,8','39b':'392,7','39c':'141,4',
  '40a':'1/9','40a-falsch':'2/9','40b-falsch':'9,4','40b':'21,4','40c-falsch':'30,6','40c':'69,4',
  '42a':'64,1','42b':'18,3','42c':'187',
  '43a-Rad':'45','43a-Bus':'30','43a-Fuss':'25','43b-Rad':'162','43b-Bus':'108','43b-Fuss':'90',
 },
 'e2': {
  '22a':'Fläche','22b':'Umfang','22c':'Fläche','22d':'Umfang','22e':'Fläche',
  '23a':'3,1','23b':'113,1','23c':'153,9','23d':'314,2','23e':'254,5','23f':'22,9',
  '24a':'56,5','24b':'113,1','24c':'77,0','24d':'37,7',
  '25a':'1/4·π·3²','25b':'1/2·π·4²','25c':'3/4·π·2²','26a':'Halbkreis r=5','26b':'Viertelkreis r=6',
  '27K1r':'6','27K1d':'12','27K1u':'37,7','27K1A':'113,1',
  '27K2r':'4,5','27K2d':'9','27K2u':'28,3','27K2A':'63,6',
  '27K3r':'1,2','27K3d':'2,4','27K3u':'7,5','27K3A':'4,5',
  '27K4r':'3,5','27K4d':'7,0','27K4u':'22,0','27K4A':'38,5',
  '28a':'7,0','28b':'10,0','28c-r':'2,52','28c':'5,0','28d':'9,40',
  '29a-falsch':'452,4','29a':'113,1','29b-falsch':'56,5','29b':'254,5','29c-falsch':'44,0','29c':'153,9',
  '31a':'1,1','31b':'3,8','31c':'22,0','31d':'38,5',
  '32a-gross':'706,9','32a-klein':'628,3','32b-gross':'1,13','32b-klein':'1,43','32c':'groß',
 },
 'e1': {
  '10a':'Radius','10b':'Durchmesser','10c':'keins','10d':'Durchmesser','10e':'Radius',
  '11a':'Umfang','11b':'Fläche','11c':'Fläche','11d':'Umfang','11e':'Umfang',
  '12a':'6','12b':'12','12c':'7','12d':'5','12e':'7','12f':'4,5','12g':'4,8','12h':'60',
  '14b':'1,5','14c':'2,3',
  '15Dose':'3,14','15Teller':'3,15','15Münze':'3,13','15Eimer':'3,13','15a':'157',
  '16a':'9,4','16b':'18,8','16c':'28,3','16d':'62,8','16e':'25,1','16f':'11,3',
  '17a':'15,0','17b':'28,0','17c':'6,0','17d':'15,9',
  '18a':'18,8','18b':'22,0','18c':'30,8','18d':'23,9',
  '19a-falsch':'22,0','19a':'44,0','19b-falsch':'113,1','19b':'37,7',
  '21a':'219,9','21b':'1099,6','21c':'2273,6','21c-ganz':'2274',
 },
 'zone': {
  '1a':'4','1b':'10','1c':'4,8','1d':'11,4','1e':'7,8','1f':'20,0','1g':'38,1','1g-zwischenrunden':'38,0',
  '2a-u':'16','2a-A':'15','2b-u':'16','2b-A':'16','2c-u':'13','2c-A':'10','2d-u':'5','2d-A':'1',
  '3d':'4,6','3e':'3',
  '4a':'36','4b':'7','4c':'2,25','4d':'0,25','4e':'3,5','4f':'5,5','4g':'6','4h':'1,6',
  '5a':'12,25','5b':'8',
  '6a1':'16','6a2':'8','6b1':'6,25','6b2':'5','6c1':'6','6c2':'18','6d1':'0,09','6d2':'0,6',
  '7a':'360','7b':'90','7c':'180','7d':'65','7e':'230','7f':'85',
  '9a':'1/4','9a%':'25','9b':'1/2','9b%':'50','9c':'7/20','9c%':'35','9d':'5/36','9d%':'13,9',
  '9e':'3/4','9e%':'75',
 },
}

FUNKS = {'zone': zone, 'e1': e1, 'e2': e2, 'e3': e3}

def main():
    teil = sys.argv[1]
    S = FUNKS[teil]()
    B = BLATT[teil]
    zeilen, abw = [], 0
    for k, bs in B.items():
        if k not in S:
            zeilen.append(f'{k}: kein Skriptwert  Blatt {bs}  ABWEICHUNG'); abw += 1; continue
        sv = S[k]
        if isinstance(sv, str):
            ok = sv == bs
            if not ok: abw += 1
            zeilen.append(f'{k}: Skript {sv}  Blatt {bs}  {"OK" if ok else "ABWEICHUNG"}')
            continue
        bv, n = dez(bs)
        if isinstance(bv, Fr):
            ok = Fr(sv).limit_denominator(1000) == bv
            svs = str(Fr(sv).limit_denominator(1000))
        else:
            svr = rnd(float(sv), n)
            ok = abs(svr - bv) < 1e-9
            svs = f'{float(sv):.6g} -> {svr}'
        if not ok: abw += 1
        zeilen.append(f'{k}: Skript {svs}  Blatt {bs}  {"OK" if ok else "ABWEICHUNG"}')
    fehlt = [k for k in S if k not in B]
    for k in fehlt:
        zeilen.append(f'{k}: Skriptwert ohne Blattwert  ABWEICHUNG'); abw += 1
    zeilen.append(f'Abweichungen: {abw}')
    txt = '\n'.join(zeilen)
    with open(f'pruef_out_{teil}.txt', 'w', encoding='utf-8') as f:
        f.write(txt + '\n')
    print(txt)

if __name__ == '__main__':
    main()
