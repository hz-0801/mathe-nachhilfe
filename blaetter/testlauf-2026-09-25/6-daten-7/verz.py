# verz.py – Abhakseite aus den Quelltexten erzeugen (wortgleiche Titel) und Verzeichnisse aus der
# Textextraktion des Kompilats setzen. Aufruf: python verz.py abhaken | python verz.py <pdf> <ziel.tex> <modus>
import re, sys, subprocess

TEILE = [('zone_a.tex', 'Kennst du schon'),
         ('e1_a.tex', 'Einheit 1 · Streifen- und Kreisdiagramm'),
         ('e2_a.tex', 'Einheit 2 · Diagramme beurteilen und Boxplot')]

def titel(datei):
    t = open(datei, encoding='utf-8').read()
    start = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', t).group(1))
    tit = re.findall(r'\\begin\{aufgabe\}\{\\textbf\{([^{}]*)\}', t)
    return [(start + i + 1, s) for i, s in enumerate(tit)]

if sys.argv[1] == 'abhaken':
    z = [r'\eng', r'\hypertarget{abhaken}{}\einheitenkopf{Das kann ich}', r'\begingroup\setlength{\parskip}{3pt}', r'\noindent Hake ab, was du kannst.\par\medskip']
    for datei, name in TEILE:
        z.append(r'\par\medskip\noindent\textbf{%s}\par\smallskip' % name)
        for nr, s in titel(datei):
            z.append(r'\noindent\hangindent=2.2em\hangafter=1 $\square$\quad %d. %s\par' % (nr, s))
    z.append(r'\endgroup')
    open('abhaken.tex', 'w', encoding='utf-8').write('% Abhakseite „Das kann ich“ (erzeugt von verz.py)\n' + '\n'.join(z) + '\n')
    for datei, name in TEILE:
        tt = titel(datei); print(name, tt[0][0], '–', tt[-1][0], len(tt))
    sys.exit()

pdf, ziel, modus = sys.argv[1], sys.argv[2], sys.argv[3]
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
seiten = []
for p in range(1, n + 1):
    seiten.append(subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', str(p), '-l', str(p), pdf, '-'],
                                 capture_output=True, text=True, encoding='utf-8').stdout)

def erste(marke):
    for i, s in enumerate(seiten):
        if i > 0 and marke in s:  # Seite 1 ist das Verzeichnis
            return i + 1
    raise SystemExit('Marke nicht gefunden: ' + marke)

marken = []
if modus == 'gesamt':
    marken.append(('zone', 'Kennst du schon', 'Das kennst du schon', 1, 11))
marken += [('e1', 'Einheit 1 · Streifen- und Kreisdiagramm', 'Einheit 1 von 2', 12, 23),
           ('e2', 'Einheit 2 · Diagramme beurteilen und Boxplot', 'Einheit 2 von 2', 24, 34)]
anf = [erste(m[2]) for m in marken]
abh = erste('Das kann ich')
zeilen = []
for k, (ziel_id, name, marke, a, b) in enumerate(marken):
    ende = (anf[k + 1] if k + 1 < len(anf) else abh) - 1
    zeilen.append((ziel_id, f'{name} (Nr. {a}–{b}) · Seiten {anf[k]}–{ende}'))
zeilen.append(('abhaken', (f'Das kann ich (Nr. 1–34) · Seite {abh}' if abh == n else f'Das kann ich (Nr. 1–34) · Seiten {abh}–{n}')))
tex = '\n'.join(r'\noindent\hyperlink{%s}{%s}\par\smallskip' % z for z in zeilen)
open(ziel, 'w', encoding='utf-8').write(tex + '\n')
for z in zeilen:
    print(z[1])
