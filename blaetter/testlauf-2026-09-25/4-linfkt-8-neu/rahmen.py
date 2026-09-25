# rahmen.py – erzeugt abhaken.tex (Titel wortgleich aus eN_a.tex) und das Verzeichnis
# Aufruf: python rahmen.py abhaken | python rahmen.py inhalt <name> [pdftotext-Datei]
import re, sys

EINHEITEN = [('e1', 'Proportionale Funktion'),
             ('e2', r'Lineare Funktion $f(x) = m \cdot x + n$'),
             ('e3', 'Punkte und Werte'),
             ('e4', 'Gleichung bestimmen'),
             ('e5', 'Anwendungen')]

def titel(datei):
    src = open(datei, encoding='utf-8').read()
    return re.findall(r'\\begin\{aufgabe\}\{\\textbf\{(.+?)\}(?= )', src)

def nummern():
    out, nr = [], 0
    for e, t in EINHEITEN:
        ts = titel(f'{e}_a.tex')
        out.append((e, t, list(range(nr + 1, nr + len(ts) + 1)), ts))
        nr += len(ts)
    return out

def abhaken():
    z = [r'\clearpage', r'\hypertarget{abhaken}{}\einheitenkopf{Das kann ich}',
         r'\zweigzeile{Hake ab, was du kannst.}']
    for i, (e, t, nrs, ts) in enumerate(nummern(), 1):
        z.append(r'\par\medskip\noindent\begin{minipage}{\linewidth}')
        z.append(r'\textbf{Einheit %d · %s}\par\smallskip' % (i, t))
        z.append(r'\noindent\begin{tabular}{@{}p{7mm} p{14cm} c@{}}')
        for n, s in zip(nrs, ts):
            z.append(r'\hfill %d. & %s & $\square$ \\' % (n, s))
        z.append(r'\end{tabular}')
        z.append(r'\end{minipage}')
    open('abhaken.tex', 'w', encoding='utf-8').write('\n'.join(z) + '\n')
    print('abhaken.tex:', sum(len(x[2]) for x in nummern()), 'Nummern')

def inhalt(name, txt=None):
    seiten = None
    if txt:
        roh = open(txt, encoding='utf-8').read().split('\f')
        start = []
        for i, (e, t, nrs, ts) in enumerate(nummern(), 1):
            start.append(next(p for p in range(1, len(roh)) if f'Einheit {i} von 5' in roh[p]) + 1)
        ab = next(p for p in range(1, len(roh)) if 'Hake ab, was du kannst' in roh[p]) + 1
        letzte = len([s for s in roh if s.strip()])
        grenzen = start + [ab]
        seiten = [(grenzen[k], grenzen[k + 1] - 1) for k in range(5)] + [(ab, letzte)]
    z = [r'\hypertarget{inhalt}{}\einheitenkopf{Inhalt}', r'\medskip']
    for k, (e, t, nrs, ts) in enumerate(nummern()):
        s = f'Seiten {seiten[k][0]}–{seiten[k][1]}' if seiten else 'Seiten ?–?'
        z.append(r'\noindent\hyperlink{%s}{Einheit %d · %s (Nr. %d–%d) · %s}\par\smallskip'
                 % (e, k + 1, t, nrs[0], nrs[-1], s))
    s = (f'Seite {seiten[5][0]}' if seiten[5][0] == seiten[5][1] else f'Seiten {seiten[5][0]}–{seiten[5][1]}') if seiten else 'Seite ?'
    z.append(r'\noindent\hyperlink{abhaken}{Das kann ich (Nr. 1–%d) · %s}\par' % (nummern()[-1][2][-1], s))
    open(f'inhalt_{name}.tex', 'w', encoding='utf-8').write('\n'.join(z) + '\n')
    print('\n'.join(z))

if __name__ == '__main__':
    if sys.argv[1] == 'abhaken':
        abhaken()
    else:
        inhalt(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
