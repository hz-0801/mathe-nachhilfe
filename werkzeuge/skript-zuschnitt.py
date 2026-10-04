"""Skript-Zuschnitt P10: prüft die Zuordnung und baut die Übersicht.

Liest msa/skript-zuschnitt-p10.csv (gebiet; kapitel; abschnitt;
stufe; ids; neben) und die P10-Katalogzeilen 2022-2026 (ohne EBR).
Regeln (Lehrer 04.10.):
- ids = Hauptplatz; jede Teilaufgabe hat genau einen.
- neben = Nebenplatz; nur wo der Schritt dort eine eigene Stufe
  bildet; nie im eigenen Abschnitt; nur im bestätigten Zuschnitt.
- Gezählt („kommt das dran?“) werden nur Hauptplätze.
- Gemeldet wird jeder Abschnitt mit mehr Neben- als Hauptplätzen.
Schreibt msa/skript-zuschnitt-p10.md. Aufruf aus der Repo-Wurzel:
python3 werkzeuge/skript-zuschnitt.py
"""
import csv, collections, sys

KAT = ['msa/msa-katalog-basis.csv', 'msa/msa-katalog-kontext.csv']
ZU = 'msa/skript-zuschnitt-p10.csv'
OUT = 'msa/skript-zuschnitt-p10.md'

rows = {}
for f in KAT:
    for x in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
        if x['jahr'] >= '2022' and x['papier'] != 'EBR':
            rows[x['id']] = x

zu = list(csv.DictReader(open(ZU, encoding='utf-8'), delimiter=';'))
haupt = {}
seen = collections.Counter()
for z in zu:
    for i in z['ids'].split():
        seen[i] += 1
        haupt[i] = z['abschnitt']
fehler = [i for i in rows if seen[i] == 0]
doppelt = [i for i, n in seen.items() if n > 1]
fremd = [i for i in seen if i not in rows]
neben_fehler = []
for z in zu:
    for i in z['neben'].split():
        if i not in rows:
            neben_fehler.append(f'{i} unbekannt')
        elif haupt.get(i) == z['abschnitt']:
            neben_fehler.append(f'{i} Nebenplatz im eigenen Abschnitt')
if fehler or doppelt or fremd or neben_fehler:
    print('ohne Hauptplatz:', fehler)
    print('doppelt:', doppelt)
    print('unbekannt:', fremd)
    print('Nebenplatz:', neben_fehler)
    sys.exit(1)

H = collections.defaultdict(list)
N = collections.defaultdict(list)
for z in zu:
    H[(z['gebiet'], z['abschnitt'])] += z['ids'].split()
    N[(z['gebiet'], z['abschnitt'])] += z['neben'].split()

out = ['# Skript-Zuschnitt P10 – Vorschlag',
       '',
       'Abgeleitet von `werkzeuge/skript-zuschnitt.py` aus '
       '`msa/skript-zuschnitt-p10.csv`; nie von Hand ändern. Grundlage: '
       f'{len(rows)} Teilaufgaben 2022–2026 (OS, ab 2026 FOR). Je Abschnitt: '
       'Teilaufgaben · Jahrgänge · zuletzt · BE, gezählt nur Hauptplätze; '
       'Nebenplätze getrennt („dazu n aus anderen Abschnitten“). Stufen in '
       'Leiterfolge. Basisaufgaben (B1…) in den Gebieten stehen zusätzlich '
       'als unterste Stufe; der Basisteil bleibt ganz und gemischt '
       '(Original, Antwortbogen), ohne Skript (Lehrer 04.10.).',
       '']
warn = []
geb = kap = ab = None
for z in zu:
    k = (z['gebiet'], z['abschnitt'])
    if z['gebiet'] != geb:
        geb = z['gebiet']
        n = sum(len(v) for kk, v in H.items() if kk[0] == geb)
        out += ['', f'## {geb} ({n} Teilaufgaben)']
        kap = None
    if z['kapitel'] != kap:
        kap = z['kapitel']
        if kap != '–':
            out += ['', f'### Kapitel {kap}']
    if z['abschnitt'] != ab:
        ab = z['abschnitt']
        ids, nb = H[k], N[k]
        if ids:
            js = sorted({rows[i]['jahr'] for i in ids})
            be = sum(int(rows[i]['punkte'] or 0) for i in ids)
            kopf = f'{len(ids)} · {len(js)} J · zuletzt {js[-1]} · {be} BE'
        else:
            kopf = 'keine eigenen Teilaufgaben'
        if nb:
            kopf += f' · dazu {len(nb)} aus anderen Abschnitten'
        if len(nb) > len(ids):
            warn.append(ab)
        out += ['', f'#### {ab} – {kopf}']
    teile = [f'{i} ({rows[i]["typ"]})' for i in z['ids'].split()]
    teile += [f'{i} ({rows[i]["typ"]}; kennst du aus „{haupt[i]}“)'
              for i in z['neben'].split()]
    out.append(f'- neu: {z["stufe"]} – ' + ', '.join(teile))
if warn:
    out += ['', 'Mehr Neben- als Hauptplätze: ' + '; '.join(warn) + '.']
open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print(f'{len(rows)} Teilaufgaben, jede mit genau einem Hauptplatz; '
      f'{sum(len(v) for v in N.values())} Nebenplätze; {len(H)} Abschnitte '
      f'nach {OUT}')
for w in warn:
    print('Meldung: mehr Neben- als Hauptplätze in', w)
