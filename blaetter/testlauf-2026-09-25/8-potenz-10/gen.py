# gen.py – erzeugt die Abhakseite (wortgleich aus den Aufgabenquelltexten) und die
# Verzeichnisse von Lernblatt und Gesamt aus der Textextraktion des Kompilats.
#   python gen.py abhaken
#   python gen.py toc <lernblatt|gesamt> <pdf>
import sys, re, subprocess

TEILE = [('zone', 'Kennst du schon'), ('e1', None), ('e2', None), ('e3', None), ('e4', None), ('e5', None)]

def aufgaben(teil):
    t = open(f'{teil}_a.tex', encoding='utf-8').read()
    start = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', t).group(1))
    titel = re.search(r'\\einheitenkopf\*\{([^}]*)\}', t).group(1)
    saetze = []
    for m in re.finditer(r'\\begin\{aufgabe\}\{', t):
        i, tiefe = m.end(), 1
        j = i
        while tiefe:
            if t[j] == '{': tiefe += 1
            elif t[j] == '}': tiefe -= 1
            j += 1
        arg = t[i:j - 1]
        # erster Satz: bis zum ersten Punkt außerhalb von $...$
        inmath, k = False, 0
        while k < len(arg):
            c = arg[k]
            if c == '$': inmath = not inmath
            if c == '.' and not inmath and (k + 1 == len(arg) or arg[k + 1] in ' \n'):
                break
            k += 1
        saetze.append(arg[:k + 1].strip())
    return start + 1, titel, saetze

def abhaken():
    z = [r'\hypertarget{abhaken}{}\einheitenkopf*{Das kann ich}',
         r'\zweigzeile{Hake am Ende ab, was du kannst.}', r'{\small']
    for teil, name in TEILE:
        n0, titel, saetze = aufgaben(teil)
        z.append(r'\par\medskip\noindent\textbf{' + (name or titel) + r'}\par\smallskip')
        for i, s in enumerate(saetze):
            z.append(r'\abhak{' + str(n0 + i) + '}{' + s + '}')
    z.append('}')
    open('abhaken.tex', 'w', encoding='utf-8').write('\n'.join(z) + '\n')
    print('abhaken.tex:', sum(len(aufgaben(t)[2]) for t, _ in TEILE), 'Hauptnummern')

def seitentexte(pdf):
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    n = int(re.search(r'Pages:\s+(\d+)', info).group(1))
    return [subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', str(s), '-l', str(s), pdf, '-'],
                           capture_output=True, text=True, encoding='utf-8').stdout for s in range(1, n + 1)]

def toc(art, pdf):
    seiten = seitentexte(pdf)
    teile = TEILE if art == 'gesamt' else TEILE[1:]
    marken = []
    for teil, name in teile:
        n0, titel, saetze = aufgaben(teil)
        suche = 'Kennst du schon' if teil == 'zone' else titel.split(' · ')[0]
        erste = next(i + 1 for i, s in enumerate(seiten) if i > 0 and suche in s)
        marken.append((teil, name, titel, n0, n0 + len(saetze) - 1, erste))
    abh = next(i + 1 for i, s in enumerate(seiten) if i > 0 and 'Das kann ich' in s)
    zeilen = []
    for k, (teil, name, titel, a, b, erste) in enumerate(marken):
        letzte = (marken[k + 1][5] if k + 1 < len(marken) else abh) - 1
        s = f'Seite {erste}' if erste == letzte else f'Seiten {erste}–{letzte}'
        text = (name if teil == 'zone' else re.sub(r' von \d+', '', titel)) + f' (Nr. {a}–{b}) · {s}'
        zeilen.append((teil, text))
    s = f'Seite {abh}' if abh == len(seiten) else f'Seiten {abh}–{len(seiten)}'
    zeilen.append(('abhaken', f'Das kann ich · {s}'))
    tex = [r'\hyperlink{' + t + '}{' + x + r'}\par\smallskip' for t, x in zeilen]
    open(f'{art}_toc.tex', 'w', encoding='utf-8').write('\n'.join(tex) + '\n')
    for t, x in zeilen: print(x)

if __name__ == '__main__':
    if sys.argv[1] == 'abhaken': abhaken()
    else: toc(sys.argv[2], sys.argv[3])
