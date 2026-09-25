# rahmen.py – Abhakseite, Verzeichnisse und Rahmendateien für Lernblatt, Gesamt, Lösungen
# Aufruf: python rahmen.py abhaken            → abhaken.tex (Titel wortgleich aus den Aufgabendateien)
#         python rahmen.py verz <pdf-txt> <art> → verz_<art>.tex aus der Textextraktion des Kompilats
#         python rahmen.py pruef <pdf-txt>       → Nummernfolge, Titel auf der Abhakseite, Seitenbereiche
import re, sys

TEILE = [('zone', 'Kennst du schon', 'zone_a.tex'),
         ('e1', 'Einheit 1 · Wurzelziehen und Lösbarkeit', 'e1_a.tex'),
         ('e2', 'Einheit 2 · Satz vom Nullprodukt', 'e2_a.tex'),
         ('e3', 'Einheit 3 · Normalform und p-q-Formel', 'e3_a.tex'),
         ('e4', 'Einheit 4 · Sachaufgaben', 'e4_a.tex')]
KOPF = {'zone': 'Das kennst du schon', 'e1': 'Einheit 1 von 4', 'e2': 'Einheit 2 von 4', 'e3': 'Einheit 3 von 4',
        'e4': 'Einheit 4 von 4', 'abhaken': 'Das kann ich'}

def titel(datei):
    txt = open(datei, encoding='utf-8').read()
    start = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', txt).group(1))
    out = []
    for i, m in enumerate(re.finditer(r'\\begin\{aufgabe\}\{(.*)\}\s*$', txt, re.M)):
        arg = m.group(1)
        t = re.match(r'(.*?[.?])(\s|$)', arg).group(1)
        out.append((start + i + 1, t))
    return out

def abhaken():
    z = ['% Abhakseite „Das kann ich“ – erzeugt von rahmen.py aus den Titeln der Aufgabendateien',
         '\\clearpage', '\\hypertarget{abhaken}{}\\einheitenkopf{Das kann ich}',
         '\\zweigzeile{Hake ab, was du kannst. Die Nummern sind die Aufgaben auf dem Blatt.}', '{\\small\\setlength{\\parskip}{1.5pt}']
    for kurz, name, datei in TEILE:
        z.append(f'\\abhakgruppe{{{name}}}')
        for nr, t in titel(datei):
            z.append(f'\\abhakzeile{{{nr}}}{{{t}}}')
    z.append('}')
    open('abhaken.tex', 'w', encoding='utf-8').write('\n'.join(z) + '\n')
    print('\n'.join(z))

def seiten(txtdatei):
    seiten = open(txtdatei, encoding='utf-8').read().split('\f')
    erste = {}
    for i, s in enumerate(seiten, 1):
        for k, kopf in KOPF.items():
            ende = r'\s*$' if k in ('zone', 'abhaken') else r'(\s|$)'
            if k not in erste and re.search(r'^\s*' + re.escape(kopf) + ende, s, re.M):
                erste[k] = i
    n = len([s for s in seiten if s.strip()])
    return erste, n

def verz(txtdatei, art):
    erste, n = seiten(txtdatei)
    folge = [k for k in ['zone', 'e1', 'e2', 'e3', 'e4', 'abhaken'] if k in erste]
    z = [f'% Verzeichnis {art} – Seitenbereiche aus der Textextraktion des Kompilats']
    for j, k in enumerate(folge):
        von = erste[k]
        bis = (erste[folge[j + 1]] - 1) if j + 1 < len(folge) else n
        if k == 'abhaken':
            seite = f'Seite {von}' if von == bis else f'Seiten {von}–{bis}'
            z.append(f'\\verzzeile{{abhaken}}{{Das kann ich · {seite}}}')
            continue
        name = dict((a, b) for a, b, c in TEILE)[k]
        nrn = [nr for nr, t in titel(dict((a, c) for a, b, c in TEILE)[k])]
        seite = f'Seite {von}' if von == bis else f'Seiten {von}–{bis}'
        z.append(f'\\verzzeile{{{k}}}{{{name} (Nr. {nrn[0]}–{nrn[-1]}) · {seite}}}')
    open(f'verz_{art}.tex', 'w', encoding='utf-8').write('\n'.join(z) + '\n')
    print('\n'.join(z))

def pruef(txtdatei):
    txt = open(txtdatei, encoding='utf-8').read()
    nummern = [int(m.group(1)) for m in re.finditer(r'^\s{0,3}(\d{1,2})\. \S', txt, re.M)]
    print('Nummern im Kompilat:', nummern)
    erste, n = seiten(txtdatei)
    print('Erste Seiten:', erste, 'Seiten gesamt:', n)

if __name__ == '__main__':
    {'abhaken': lambda: abhaken(), 'verz': lambda: verz(sys.argv[2], sys.argv[3]), 'pruef': lambda: pruef(sys.argv[2])}[sys.argv[1]]()
