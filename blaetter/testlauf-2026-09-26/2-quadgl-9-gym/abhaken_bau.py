# -*- coding: utf-8 -*-
# Baut abhaken.tex aus den Aufgabentiteln und \verfahren-Zeilen der Quelltexte (wortgleich)
# und gibt die Nummernbereiche je Datei aus (für die Verzeichniszeile, nicht geschätzt).
import io, re

teile = [('zone_a.tex', 'Kennst du schon'), ('e1_a.tex', 'Einheit 1 · Wurzelziehen und Lösbarkeit'),
         ('e2_a.tex', 'Einheit 2 · Satz vom Nullprodukt'), ('e3_a.tex', 'Einheit 3 · Normalform und p-q-Formel'),
         ('e4_a.tex', 'Einheit 4 · Sachaufgaben')]
aus = ['% Abhakseite „Das kann ich" – erzeugt von abhaken_bau.py aus den Quelltexten', '\\begin{abhakseite}']
nr = 0
for datei, gruppe in teile:
    t = io.open(datei, encoding='utf-8').read()
    start = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', t).group(1))
    assert start == nr, (datei, start, nr)
    aus.append('\\abhakgruppe{%s}' % gruppe)
    erste = nr + 1
    for m in re.finditer(r'\\verfahren\{((?:[^{}]|\{[^{}]*\})*)\}|\\begin\{aufgabe\}\{((?:[^{}]|\{[^{}]*\})*)\}', t):
        if m.group(1) is not None:
            aus.append('\\abhakgruppe{– %s}' % m.group(1))
        else:
            nr += 1
            aus.append('\\abhak{%d}{%s}' % (nr, m.group(2)))
    print('%s: Nr. %d–%d' % (datei, erste, nr))
aus.append('\\end{abhakseite}')
io.open('abhaken.tex', 'w', encoding='utf-8').write('\n'.join(aus) + '\n')
print('Titel gesamt:', nr)
