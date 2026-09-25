# verzeichnis.py – Hilfsskript des Baus (Prozentrechnung Kl. 7 schwach)
#   python verzeichnis.py abhaken             -> schreibt abhaken.tex aus den Titeln der Aufgabendateien (wortgleich)
#   python verzeichnis.py seiten <rahmen>     -> liest <rahmen>.pdf per pdftotext, setzt die Seitenbereiche
#                                                in <rahmen>.tex (Platzhalter @zone@, @e1@ … @abhaken@) und gibt sie aus
import re, sys, subprocess

DATEIEN = [('zone', 'zone_a.tex', 'Das kennst du schon'),
           ('e1', 'e1_a.tex', 'Einheit 1 von 4 · Prozentsatz berechnen'),
           ('e2', 'e2_a.tex', 'Einheit 2 von 4 · Prozentwert berechnen'),
           ('e3', 'e3_a.tex', 'Einheit 3 von 4 · Grundwert berechnen'),
           ('e4', 'e4_a.tex', 'Einheit 4 von 4 · Prozentuale Veränderung')]

def titel(datei):
    text = open(datei, encoding='utf-8').read()
    start = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', text).group(1))
    out = []
    for i, m in enumerate(re.finditer(r'\\begin\{aufgabe\}\{(.*)', text)):
        arg = m.group(1)
        # erster Satz: bis zum ersten Punkt, dem ein Leerzeichen oder das Argumentende folgt
        satz = re.match(r'(.*?\.)(\s|\}$)', arg).group(1)
        out.append((start + i + 1, satz))
    return out

def abhaken():
    z = ['% Abhakseite „Das kann ich“ – erzeugt von verzeichnis.py aus den Aufgabendateien',
         '\\clearpage', '\\hypertarget{abhaken}{}', '\\einheitenkopf*{Das kann ich}',
         '{\\small Hake ab, was du kannst.\\par}', '\\medskip', '{\\small']
    for kurz, datei, kopf in DATEIEN:
        z.append('\\par\\smallskip\\noindent\\textbf{%s}\\par' % kopf)
        for nr, satz in titel(datei):
            z.append('\\noindent$\\square$\\quad %d.\\ %s\\par' % (nr, satz))
    z.append('}')
    open('abhaken.tex', 'w', encoding='utf-8').write('\n'.join(z) + '\n')
    print('abhaken.tex:', sum(len(titel(d)) for _, d, _ in DATEIEN), 'Hauptnummern')

def seiten(rahmen):
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', rahmen + '.pdf'], capture_output=True, text=True).stdout).group(1))
    erste = {}
    for s in range(2, n + 1):
        t = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', str(s), '-l', str(s), rahmen + '.pdf', '-'],
                           capture_output=True, encoding='utf-8').stdout
        t = re.sub(r'\s+', ' ', t)
        for kurz, _, kopf in DATEIEN:
            if kopf in t and kurz not in erste:
                erste[kurz] = s
        if 'Das kann ich' in t and 'abhaken' not in erste:
            erste['abhaken'] = s
    folge = sorted(erste.items(), key=lambda kv: kv[1])
    bereiche = {}
    for i, (kurz, s) in enumerate(folge):
        ende = folge[i + 1][1] - 1 if i + 1 < len(folge) else n
        bereiche[kurz] = f'{s}' if s == ende else f'{s}–{ende}'
    tex = open(rahmen + '.tex', encoding='utf-8').read()
    for kurz, b in bereiche.items():
        wort = 'Seiten ' if '–' in b else 'Seite '
        tex = re.sub(r'(%% @%s@\n[^\n]*?· )Seiten? [^}\n]*\}' % kurz, lambda m: m.group(1) + wort + b + '}', tex)
    open(rahmen + '.tex', 'w', encoding='utf-8').write(tex)
    print(rahmen, n, 'Seiten:', bereiche)

if __name__ == '__main__':
    if sys.argv[1] == 'abhaken':
        abhaken()
    else:
        seiten(sys.argv[2])
