"""Skript-Zuschnitt: prüft die Zuordnung und baut die Übersicht.

Liest je Profil die Zuschnitt-CSV (gebiet; kapitel; abschnitt; stufe;
ids; neben) und die Katalogzeilen der Grundlage.
Regeln (Lehrer 04.10.):
- ids = Hauptplatz; jede Teilaufgabe hat genau einen.
- neben = Nebenplatz; nur wo der Schritt dort eine eigene Stufe
  bildet; nie im eigenen Abschnitt; nur im bestätigten Zuschnitt.
- Gezählt („kommt das dran?“) werden nur Hauptplätze.
- Gemeldet wird jeder Abschnitt mit mehr Neben- als Hauptplätzen.
Profile (Argument, Standard p10):
  p10    msa/skript-zuschnitt-p10.csv, P10-Katalog 2022-2026 ohne EBR,
         schreibt msa/skript-zuschnitt-p10.md
  abi-gk abitur/skript-zuschnitt-abi-gk.csv, abi-katalog.csv mit papier
         2022-bebb-gk … 2025-bebb-gk, 2026-bb-gk,
         schreibt abitur/skript-zuschnitt-abi-gk.md
Aufruf aus der Repo-Wurzel: python3 werkzeuge/skript-zuschnitt.py [p10|abi-gk]
"""
import csv, collections, sys

PROFIL = {
    'p10': dict(
        kat=['msa/msa-katalog-basis.csv', 'msa/msa-katalog-kontext.csv'],
        filt=lambda x: x['jahr'] >= '2022' and x['papier'] != 'EBR',
        zu='msa/skript-zuschnitt-p10.csv',
        out='msa/skript-zuschnitt-p10.md',
        titel='Skript-Zuschnitt P10 – Vorschlag',
        grund='{n} Teilaufgaben 2022–2026 (OS, ab 2026 FOR)',
        basis='Basisaufgaben (B1…) in den Gebieten stehen zusätzlich '
              'als unterste Stufe; der Basisteil bleibt ganz und gemischt '
              '(Original, Antwortbogen), ohne Skript (Lehrer 04.10.).'),
    'abi-gk': dict(
        kat=['abitur/abi-katalog.csv'],
        filt=lambda x: x['papier'] in {'2022-bebb-gk', '2023-bebb-gk',
                                       '2024-bebb-gk', '2025-bebb-gk',
                                       '2026-bb-gk'},
        zu='abitur/skript-zuschnitt-abi-gk.csv',
        out='abitur/skript-zuschnitt-abi-gk.md',
        titel='Skript-Zuschnitt Abitur GK – Entwurf',
        grund='{n} Teilaufgaben 2022–2026 (Brandenburg GK: 2022–2025 '
              'gemeinsame Hefte Berlin/Brandenburg, 2026 bb-gk)',
        basis='Hilfsmittelfreie Teilaufgaben (A1…) in den Gebieten stehen '
              'zusätzlich als unterste Stufe; der hilfsmittelfreie Teil '
              'bleibt ganz und gemischt, ohne Skript (Regel wie P10, '
              '04.10.).'),
}
name = sys.argv[1] if len(sys.argv) > 1 else 'p10'
if name not in PROFIL:
    sys.exit(f'unbekanntes Profil {name}; bekannt: {", ".join(PROFIL)}')
P = PROFIL[name]
KAT, ZU, OUT = P['kat'], P['zu'], P['out']

rows = {}
for f in KAT:
    for x in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
        if P['filt'](x):
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

out = [f'# {P["titel"]}',
       '',
       'Abgeleitet von `werkzeuge/skript-zuschnitt.py` aus '
       f'`{ZU}`; nie von Hand ändern. Grundlage: '
       f'{P["grund"].format(n=len(rows))}. Je Abschnitt: '
       'Teilaufgaben · Jahrgänge · zuletzt · BE, gezählt nur Hauptplätze; '
       'Nebenplätze getrennt („dazu n aus anderen Abschnitten“). Stufen in '
       'Leiterfolge. ' + P['basis'],
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
