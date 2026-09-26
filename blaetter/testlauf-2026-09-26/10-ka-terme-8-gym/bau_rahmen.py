# bau_rahmen.py – liest die Aufgabenquelltexte und schreibt daraus
# abhaken.tex (Handform, wortgleiche Titel), lernblatt.tex, gesamt.tex, loesungen.tex.
# Nummernbereiche der Verzeichniszeile kommen aus den Quelltexten.
import re

THEMA = 'Terme und binomische Formeln'
TEILE = ['zone', 'e1', 'e2', 'e3', 'e4', 'e5']

VORSPANN = r'''\documentclass[11pt]{article}
\usepackage{mathblatt}
% im Vorspann definierter Baustein (fehlt in der Anleitung): Flächenbild eines Rechtecks
% mit geteilten Seiten #1+#2 (oben) und #3+#4 (links), Innenfelder #5..#8
\newcommand{\flaechenbild}[8]{%
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[thick] (0,0) rectangle (4.5,-4.5);
\draw (3,0) -- (3,-4.5);
\draw (0,-3) -- (4.5,-3);
\node at (1.5,0.3) {$#1$};
\node at (3.75,0.3) {$#2$};
\node at (-0.4,-1.5) {$#3$};
\node at (-0.4,-3.75) {$#4$};
\node at (1.5,-1.5) {$#5$};
\node at (3.75,-1.5) {$#6$};
\node at (1.5,-3.75) {$#7$};
\node at (3.75,-3.75) {$#8$};
\end{tikzpicture}}
'''

def lies(teil):
    src = open(f'{teil}_a.tex', encoding='utf-8').read()
    kopf = re.search(r'\\einheitenkopf\[(\w+)\]\[([^\]]*)\]\{([^}]*)\}', src)
    ziel, kurz, lang = kopf.groups()
    n = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', src).group(1))
    eintraege = []  # ('verfahren', text) | ('aufgabe', nr, titel)
    for m in re.finditer(r'\\verfahren\{([^}]*)\}|\\begin\{aufgabe\}\{((?:[^{}]|\{[^{}]*\})*)\}', src):
        if m.group(1) is not None:
            eintraege.append(('verfahren', m.group(1)))
        else:
            n += 1
            eintraege.append(('aufgabe', n, m.group(2)))
    nrs = [e[1] for e in eintraege if e[0] == 'aufgabe']
    return dict(teil=teil, ziel=ziel, kurz=kurz, lang=lang, eintraege=eintraege, von=min(nrs), bis=max(nrs))

daten = [lies(t) for t in TEILE]

# fortlaufende Nummern prüfen
alle = [e[1] for d in daten for e in d['eintraege'] if e[0] == 'aufgabe']
assert alle == list(range(1, len(alle) + 1)), alle

def gruppenname(d):
    if d['teil'] == 'zone':
        return 'Kennst du schon'
    m = re.match(r'Einheit (\d+) von \d+ · (.*)', d['lang'])
    return f'Einheit {m.group(1)} · {m.group(2)}'

zeilen = [r'\begin{abhakseite}']
for d in daten:
    block = [r'\abhakgruppe{' + gruppenname(d) + '}']
    for e in d['eintraege']:
        if e[0] == 'verfahren':
            block.append(r'\abhakgruppe{\normalfont\itshape ' + e[1] + '}')
        else:
            block.append(r'\abhak{' + str(e[1]) + '}{' + e[2] + '}')
    if d['teil'] == 'zone':
        zeilen.append(r'\ifmitzone')
        zeilen += block
        zeilen.append(r'\fi')
    else:
        zeilen += block
zeilen.append(r'\end{abhakseite}')
open('abhaken.tex', 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n')

def verz(d):
    if d['teil'] == 'zone':
        text = f"Kennst du schon (Nr. {d['von']}–{d['bis']})"
    else:
        text = f"{d['kurz']} (Nr. {d['von']}–{d['bis']})"
    return r'\verz{' + d['ziel'] + '}{' + text + '}'

def rahmen(blatt, mit_zone):
    teile = daten if mit_zone else daten[1:]
    vz = r' \verztrenn '.join([verz(d) for d in teile] + [r'\verz{abhaken}{Das kann ich}'])
    out = [VORSPANN, r'\newif\ifmitzone', r'\mitzone' + ('true' if mit_zone else 'false'),
           r'\begin{document}', r'\blattkopf{' + THEMA + '}{' + blatt + '}', r'\weit',
           r'\verzeichniszeile{' + vz + '}', '']
    for i, d in enumerate(teile):
        if i > 0:
            out.append(r'\clearpage')
        out.append(r'\input{' + d['teil'] + '_a}')
    out += [r'\input{abhaken}', r'\end{document}', '']
    return '\n'.join(out), vz

lb, vz_lb = rahmen('Lernblatt', False)
ge, vz_ge = rahmen('Gesamt', True)
open('lernblatt.tex', 'w', encoding='utf-8').write(lb)
open('gesamt.tex', 'w', encoding='utf-8').write(ge)

lo = [r'\documentclass[11pt]{article}', r'\usepackage{mathblatt}', r'\begin{document}',
      r'\blattkopf{' + THEMA + '}{Lösungen}']
for d in daten:
    lo.append(r'\input{' + d['teil'] + '_l}')
lo += [r'\end{document}', '']
open('loesungen.tex', 'w', encoding='utf-8').write('\n'.join(lo))

for d in daten:
    print(d['teil'], d['von'], '-', d['bis'], d['lang'])
print('Verzeichnis Lernblatt:', vz_lb)
print('Verzeichnis Gesamt:', vz_ge)
print('Hauptnummern gesamt:', len(alle))
