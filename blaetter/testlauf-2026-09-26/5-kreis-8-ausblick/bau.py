# bau.py – Abhakseite und Verzeichniszeilen aus den Quelltexten (Nummern nie geschätzt)
import re

TEILE = [('zone_a.tex', 'Kennst du schon', 'zone'),
         ('e1_a.tex', 'Einheit 1 · Kreisumfang', 'e1'),
         ('e2_a.tex', 'Einheit 2 · Kreisfläche', 'e2'),
         ('e3_a.tex', 'Einheit 3 · Kreisteile', 'e3')]
KURZ = {'zone': 'Kennst du schon', 'e1': '1 Kreisumfang', 'e2': '2 Kreisfläche', 'e3': '3 Kreisteile'}

def titel_arg(s, i):
    """liest das Argument in geschweiften Klammern ab Position i (auf '{')"""
    tiefe, j = 0, i
    while True:
        if s[j] == '{': tiefe += 1
        elif s[j] == '}':
            tiefe -= 1
            if tiefe == 0: return s[i+1:j]
        j += 1

abh, bereiche = [], {}
for datei, gruppe, ziel in TEILE:
    s = open(datei, encoding='utf-8').read()
    start = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', s).group(1))
    nr = start
    abh.append(f'\\abhakgruppe{{{gruppe}}}')
    erste = None
    for m in re.finditer(r'\\(verfahren|begin\{aufgabe\})\{', s):
        arg = titel_arg(s, m.end() - 1)
        if m.group(1) == 'verfahren':
            abh.append(f'\\abhakgruppe{{\\hspace*{{1em}}\\mdseries\\itshape {arg}}}')
        else:
            nr += 1
            erste = erste or nr
            abh.append(f'\\abhak{{{nr}}}{{{arg}}}')
    bereiche[ziel] = (erste, nr)

with open('abhaken.tex', 'w', encoding='utf-8') as f:
    f.write('% erzeugt von bau.py aus zone_a, e1_a, e2_a, e3_a\n\\begin{abhakseite}\n' + '\n'.join(abh) + '\n\\end{abhakseite}\n')

def verz(mit_zone):
    teile = []
    for _, _, ziel in TEILE:
        if ziel == 'zone' and not mit_zone: continue
        a, b = bereiche[ziel]
        teile.append(f'\\verz{{{ziel}}}{{{KURZ[ziel]} (Nr.~{a}–{b})}}')
    teile.append('\\verz{abhaken}{Das kann ich}')
    return '\\verzeichniszeile{' + ' \\verztrenn '.join(teile) + '}\n'

open('verz_lernblatt.tex', 'w', encoding='utf-8').write(verz(False))
open('verz_gesamt.tex', 'w', encoding='utf-8').write(verz(True))
print(bereiche)
