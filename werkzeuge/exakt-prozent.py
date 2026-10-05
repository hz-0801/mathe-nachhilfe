# exakt-prozent.py – Lauf A 06.10.2026: ergänzt in msa-katalog-basis/kontext die Prozent-Zeilen
# um exakte Werte vor gerundeten (Beschluss 24, Arbeitsliste aufgabenbank bau/pruefheft/
# beschluesse-2026-10-06.md); Gegenprobe mit sympy; wiederholbar (bereits ergänzte Felder bleiben).
import csv, io, sys
from sympy import Rational as R, pi, N, Float
# Gegenprobe an bekannten Werten
assert R(30,100)*70 == 21 and R(6)/R(20,100) == 30 and R(200)/R(25,100) == 800
chk = {  # exakter Wert -> gerundeter Wert im Katalog
 'K3c': (R(5,179)*100, 2.8, 1), 'K6a': (R(25,156)*100, 16.0, 1), 'K4b': (R(7,47)*100, 14.9, 1),
 'K5a': (R(11,79)*100, 13.9, 1), 'K4b25': (R(8,85)*100, 9.4, 1), 'K7c': (R(12,83)*100, 14.5, 1),
 'K5c': (800-192*pi, 196.8, 1), 'K5cD': (192*pi, 603.2, 1), 'K3c14': (1000*R(103,100)**5, 1159.27, 2),
 'K5a19': (R(23,100)*1200, 276, 0), 'K2b15': (R(4350,100)*R(8,10), 34.80, 2)}
for k,(e,g,st) in chk.items():
    assert round(float(N(e)),st) == g, (k, N(e), g)
E = {
 '2020-OS-K4c': {'kurzloesung': ('Studie 1 ≈ 81,7', 'Studie 1 54 · 1,03¹⁴ ≈ 81,7')},
 '2015-OS-K7c': {'zwischenergebnis': ('0,145 · 360° ≈ 52°', '12/83 · 360° = 4320/83° ≈ 52°')},
 '2025-OS-B1a': {'zwischenergebnis': ('G = W : p', 'G = W : p = 6 € : 0,2 = 30 €')},
 '2026-FOR-B1a': {'zwischenergebnis': ('W = G · p', 'W = G · p = 70 € · 0,3 = 21 €')},
 '2023-OS-B1b': {'zwischenergebnis': ('G = W : p', 'G = W : p = 200 € : 0,25 = 800 €')},
 '2026-FOR-K3c': {'kurzloesung': ('≈ 2,8 %', '5/179 ≈ 2,8 %'),
                  'zwischenergebnis': ('0,05 : 1,79 ≈ 0,0279', '0,05 : 1,79 = 5/179 ≈ 0,0279')},
 '2023-OS-K5c': {'kurzloesung': ('Abfall ≈ 196,8 cm²', 'Abfall 800 − 192π ≈ 196,8 cm²'),
                 'zwischenergebnis': ('12 · π · 16 ≈ 603,2 cm²', '12 · π · 16 = 192π ≈ 603,2 cm²')},
 '2023-OS-K6a': {'kurzloesung': ('≈ 16,0 %', '25/156 ≈ 16,0 %'),
                 'zwischenergebnis': ('1,25 : 7,8 ≈ 0,160', '1,25 : 7,8 = 25/156 ≈ 0,160')},
 '2022-OS-K4b': {'kurzloesung': ('≈ 14,9 %', '7/47 ≈ 14,9 %'),
                 'zwischenergebnis': ('70 : 470 ≈ 0,149', '70 : 470 = 7/47 ≈ 0,149')},
 '2021-OS-K5a': {'kurzloesung': ('≈ 13,9 %', '11/79 ≈ 13,9 %')},
 '2025-OS-K4b': {'kurzloesung': ('16 : 170 ≈ 9,4 %', '16 : 170 = 8/85 ≈ 9,4 %'),
                 'zwischenergebnis': ('16 : 170 ≈ 0,0941', '16 : 170 = 8/85 ≈ 0,0941')},
 '2019-OS-K5a': {'zwischenergebnis': ('23 % von 1200', '23 % von 1200 = 276')},

 '2015-OS-K2b': {'zwischenergebnis': ('43,50 € · 0,8', '43,50 € · 0,8 = 34,80 €')},
 '2014-OS-K3c': {'kurzloesung': ('≈ 1159,27 €', '1000 € · 1,03⁵ ≈ 1159,27 €')},
}
n = 0
for p in ('msa/msa-katalog-basis.csv', 'msa/msa-katalog-kontext.csv'):
    raw = open(p, encoding='utf-8', newline='').read()
    rows = list(csv.reader(io.StringIO(raw), delimiter=';'))
    out = io.StringIO(); w = csv.writer(out, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\n')
    w.writerows(rows)
    if out.getvalue() != raw: sys.exit('Rundreise ändert ' + p)
    kopf = rows[0]
    for r in rows[1:]:
        d = E.get(r[0])
        if not d: continue
        for feld, (alt, neu) in d.items():
            i = kopf.index(feld)
            if neu in r[i]: continue
            if r[i].count(alt) != 1: sys.exit(f'{r[0]} {feld}: „{alt}“ nicht genau einmal in „{r[i]}“')
            r[i] = r[i].replace(alt, neu); n += 1
    out = io.StringIO(); w = csv.writer(out, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\n')
    w.writerows(rows); open(p, 'w', encoding='utf-8', newline='').write(out.getvalue())
print('geändert:', n, 'Felder')
