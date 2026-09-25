# rahmen.py – Abhakseite aus den Titeln bauen (wortgleich) und Seitenbereiche aus der Textextraktion eintragen
# Aufruf: python rahmen.py abhaken            -> abhaken.tex, titel.txt
#         python rahmen.py seiten <Rahmen.tex> -> trägt \def\Se..{a--b} aus <Rahmen>.pdf ein
import re, sys, subprocess, os

TEILE = [('zone', 'Kennst du schon'),
         ('e1', 'Einheit 1 · Monotonie und erste Ableitung'),
         ('e2', 'Einheit 2 · Extrempunkte'),
         ('e3', 'Einheit 3 · Krümmung und Wendepunkte'),
         ('e4', 'Einheit 4 · Graph und Ableitungsgraph'),
         ('e5', 'Einheit 5 · Kurvenuntersuchung im Sachzusammenhang')]

def titel(datei):
    src = open(datei + '_a.tex', encoding='utf-8').read()
    start = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', src).group(1))
    out = []
    for i, m in enumerate(re.finditer(r'\\begin\{aufgabe\}\{', src)):
        rest = src[m.end():]
        # Titel = erster Satz bis ". " oder "." am Ende des Arguments
        t = re.match(r'(.*?\.)(\s|\})', rest, re.S).group(1)
        out.append((start + i + 1, t.strip()))
    return out

def abhaken():
    zeilen = ['% Abhakseite „Das kann ich“ – erzeugt von rahmen.py aus den Titeln der Quelltexte',
              '\\clearpage', '\\hypertarget{abhaken}{}\\einheitenkopf{Das kann ich}', '{\\small\\setlength{\\parskip}{0pt}']
    txt = []
    for datei, name in TEILE:
        zeilen.append('\\abhakgruppe{%s}' % name)
        txt.append(name)
        for nr, t in titel(datei):
            zeilen.append('\\abhak{%d}{%s}' % (nr, t))
            txt.append('%d. %s' % (nr, t))
    zeilen.append('}')
    open('abhaken.tex', 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n')
    open('titel.txt', 'w', encoding='utf-8').write('\n'.join(txt) + '\n')
    print('\n'.join(txt))

def seiten(rahmen):
    pdf = rahmen.replace('.tex', '.pdf')
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    seitentext = []
    for p in range(1, n + 1):
        r = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', str(p), '-l', str(p), pdf, '-'], capture_output=True)
        seitentext.append(r.stdout.decode('utf-8'))
    marken = [('Zone', 'Das kennst du schon'), ('Ea', 'Einheit 1 von 5'), ('Eb', 'Einheit 2 von 5'), ('Ec', 'Einheit 3 von 5'),
              ('Ed', 'Einheit 4 von 5'), ('Ee', 'Einheit 5 von 5'), ('Abh', 'Das kann ich')]
    erste = {}
    for key, muster in marken:
        for p in range(2, n + 1):   # Seite 1 ist das Verzeichnis
            if muster in seitentext[p - 1]:
                erste[key] = p; break
    keys = [k for k, _ in marken if k in erste]
    src = open(rahmen, encoding='utf-8').read()
    ber = {}
    for i, k in enumerate(keys):
        a = erste[k]; b = (erste[keys[i + 1]] - 1) if i + 1 < len(keys) else n
        ber[k] = (a, b)
        wert = str(a) if a == b else '%d–%d' % (a, b)
        src = re.sub(r'(\\def\\Se%s\{)[^}]*(\})' % k, lambda m: m.group(1) + wert + m.group(2), src)
    open(rahmen, 'w', encoding='utf-8').write(src)
    print(rahmen, n, 'Seiten', ber)

if __name__ == '__main__':
    if sys.argv[1] == 'abhaken': abhaken()
    else: seiten(sys.argv[2])
