# gen_abhak.py – erzeugt die Abhakseiten wortgleich aus den Quelltexten
# und gibt die Nummernbereiche je Datei aus (für die Verzeichniszeile).
import re

def arg(s, i):
    """liest das {...}-Argument ab Position i (s[i] == '{')."""
    tiefe = 0
    for j in range(i, len(s)):
        if s[j] == '{': tiefe += 1
        elif s[j] == '}':
            tiefe -= 1
            if tiefe == 0: return s[i+1:j], j + 1
    raise ValueError('Klammer offen')

def lies(datei):
    s = open(datei, encoding='utf-8').read()
    s = '\n'.join(l for l in s.split('\n') if not l.lstrip().startswith('%'))
    ev = []
    for m in re.finditer(r'\\einheitenkopf(\[[^\]]*\])?(\[[^\]]*\])?\{|\\verfahren\{|\\begin\{aufgabe\}\{', s):
        a, _ = arg(s, m.end() - 1)
        if m.group(0).startswith('\\einheitenkopf'): ev.append(('kopf', a))
        elif m.group(0).startswith('\\verfahren'): ev.append(('verf', a))
        else: ev.append(('aufg', a))
    return ev

def seite(dateien):
    nr = 0; zeilen = ['\\begin{abhakseite}']; bereiche = []
    for d in dateien:
        erste = nr + 1
        for art, a in lies(d):
            if art == 'kopf':
                g = 'Kennst du schon' if 'kennst du schon' in a.lower() else a.replace(' von 5', '')
                zeilen.append('\\abhakgruppe{%s}' % g)
            elif art == 'verf':
                zeilen.append('\\abhakgruppe{\\normalfont\\itshape %s}' % a)
            else:
                nr += 1; zeilen.append('\\abhak{%d}{%s}' % (nr, a))
        bereiche.append((d, erste, nr))
    zeilen.append('\\end{abhakseite}')
    return '\n'.join(zeilen) + '\n', bereiche

einh = ['e1_a.tex', 'e2_a.tex', 'e3_a.tex', 'e4_a.tex', 'e5_a.tex']
g, b = seite(['zone_a.tex'] + einh)
open('abhaken.tex', 'w', encoding='utf-8').write(g)
# Lernblatt ohne Zone: Nummern laufen trotzdem ab 9 weiter
lb, _ = seite(['zone_a.tex'] + einh)
lb = re.sub(r'\\abhakgruppe\{Kennst du schon\}\n(\\abhak\{\d+\}\{.*\}\n)+', '', lb)
open('abhaken_lernblatt.tex', 'w', encoding='utf-8').write(lb)
for d, a, e in b: print(d, a, e)
