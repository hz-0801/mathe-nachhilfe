"""Skript-Zuschnitt P10: prüft die Zuordnung und baut die Übersicht.

Liest msa/skript-zuschnitt-p10.csv (Gebiet; Abschnitt; Stufe; ids) und
die P10-Katalogzeilen 2022-2026 (ohne EBR). Prüft: jede Teilaufgabe
genau einmal zugeordnet. Schreibt msa/skript-zuschnitt-p10.md mit
Zählung je Abschnitt (Teilaufgaben, Jahrgänge, zuletzt, BE).
Aufruf aus der Repo-Wurzel: python3 werkzeuge/skript-zuschnitt.py
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
seen = collections.Counter(i for z in zu for i in z['ids'].split())
fehler = [i for i in rows if seen[i] == 0]
doppelt = [i for i, n in seen.items() if n > 1]
fremd = [i for i in seen if i not in rows]
if fehler or doppelt or fremd:
    print('nicht zugeordnet:', fehler)
    print('doppelt:', doppelt)
    print('unbekannt:', fremd)
    sys.exit(1)

out = ['# Skript-Zuschnitt P10 – Vorschlag',
       '',
       'Abgeleitet von `werkzeuge/skript-zuschnitt.py` aus '
       '`msa/skript-zuschnitt-p10.csv`; nie von Hand ändern. Grundlage: '
       f'{len(rows)} Teilaufgaben 2022–2026 (OS, ab 2026 FOR). Je Abschnitt: '
       'Teilaufgaben · Jahrgänge · zuletzt · BE. Stufen in Leiterfolge.',
       '']
geb = None
ab = None
stat = collections.defaultdict(list)
for z in zu:
    stat[(z['gebiet'], z['abschnitt'])] += z['ids'].split()
for z in zu:
    if z['gebiet'] != geb:
        geb = z['gebiet']
        n = sum(len(v) for k, v in stat.items() if k[0] == geb)
        out += ['', f'## {geb} ({n} Teilaufgaben)']
    if z['abschnitt'] != ab:
        ab = z['abschnitt']
        ids = stat[(geb, ab)]
        js = sorted({rows[i]['jahr'] for i in ids})
        be = sum(int(rows[i]['punkte'] or 0) for i in ids)
        out += ['', f'### {ab} – {len(ids)} · {len(js)} J · zuletzt {js[-1]} · {be} BE']
    ids = z['ids'].split()
    out.append(f'- neu: {z["stufe"]} – ' + ', '.join(
        f'{i} ({rows[i]["typ"]})' for i in ids))
open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print(f'{len(rows)} Teilaufgaben, alle genau einmal; '
      f'{len(stat)} Abschnitte geschrieben nach {OUT}')
