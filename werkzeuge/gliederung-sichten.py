#!/usr/bin/env python3
"""gliederung-sichten.py – erzeugt die Sichten aus der Prüfungsgliederung (Entscheidung A, 08.10.2026):

    msa/skript-zuschnitt-p10.csv        aus msa/gliederung/*.md    (gebiet;kapitel;abschnitt;stufe;ids;neben)
    abitur/skript-zuschnitt-abi-gk.csv  aus abitur/gliederung/*.md
    msa/handgriffe-p10.csv              aus den Tabellen „Plätze der Originale“ (id;hauptplatz;ganz_auch;
                                        zwischenschritt;begruendung, nach id sortiert)

Aufruf aus der Repo-Wurzel:
    python3 werkzeuge/gliederung-sichten.py            schreibt die drei Dateien
    python3 werkzeuge/gliederung-sichten.py --pruefe   schreibt nichts, vergleicht mit dem Bestand
                                                       (Zahl der abweichenden Zeilen, Beispiele)
Danach wie bisher: python3 werkzeuge/skript-zuschnitt.py [p10|abi-gk] (Prüfung und Übersicht .md);
werkzeuge/zuordnung.py <kapitel> für die Zuordnungs-CSVs. Ersetzt zuschnitt-aus-steckbrief.py
(archiv/) – Zeilen je Art stehen jetzt als Zuschnitt-Unterpunkte der Stufe in der Gliederung.
"""
import argparse
import difflib
import os
import re
import sys

MN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(MN, 'werkzeuge'))
import gliederung as GL

ZUSCHNITT = {'msa': 'msa/skript-zuschnitt-p10.csv', 'abitur': 'abitur/skript-zuschnitt-abi-gk.csv'}
HANDGRIFFE = 'msa/handgriffe-p10.csv'


def zuschnitt(pruefung):
    out = ['gebiet;kapitel;abschnitt;stufe;ids;neben']
    for kap, G in GL.alle(MN, pruefung).items():
        if any('stufen' in e for e in G.get('einheiten', {}).values()):
            out += _zuschnitt_einheiten(G)
            continue
        for st in G['stufen']:
            if not st['abschnitt']:
                continue
            for zeile, ids, neben in GL.zuschnitt_zeilen(st):
                out.append(';'.join([G['gebiet'], G['name'], st['abschnitt'], zeile, ' '.join(ids), ' '.join(neben)]))
    return '\n'.join(out) + '\n'


def _zuschnitt_einheiten(G):
    """Abitur (15.10.2026): je Einheit (Kopf „Stufen: <Einheit> = …“, Folge der Kennung) eine Zeile je Stufe,
    ids aller Zuschnitt-Zeilen gleichen Namens über die Blöcke zusammengefasst."""
    out = []
    platz = lambda e: int(re.sub(r'\D', '', G['einheiten'][e].get('kennung', '999')) or 999)
    for ein in sorted(G['einheiten'], key=platz):
        st_namen = G['einheiten'][ein].get('stufen', [])
        ids, neben = {s: [] for s in st_namen}, {s: [] for s in st_namen}
        for st in G['stufen']:
            if st['abschnitt'] != ein:
                continue
            for zeile, i, n in GL.zuschnitt_zeilen(st):
                if zeile not in ids:
                    raise SystemExit(f'{G["kapitel"]}: Zeile „{zeile}“ fehlt im Kopf „Stufen: {ein} = …“')
                ids[zeile] += i
                neben[zeile] += n
        for s in st_namen:
            out.append(';'.join([G['gebiet'], G['name'], ein, s, ' '.join(ids[s]), ' '.join(neben[s])]))
    return out


def handgriffe():
    rows = [p for G in GL.alle(MN, 'msa').values() for p in G['plaetze']]
    rows.sort(key=lambda d: d['id'])
    out = ['id;hauptplatz;ganz_auch;zwischenschritt;begruendung']
    for d in rows:
        out.append(';'.join([d['id'], ' | '.join(d['hauptplatz']), ' | '.join(d['ganz_auch']),
                             ' | '.join(d['zwischenschritt']), d['begruendung']]))
    return '\n'.join(out) + '\n'


def vergleich(name, neu):
    p = os.path.join(MN, name)
    alt = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    if alt == neu:
        print(f'{name}: byteidentisch ({neu.count(chr(10))} Zeilen)')
        return 0
    a, n = alt.splitlines(), neu.splitlines()
    diff = [z for z in difflib.unified_diff(a, n, lineterm='', n=0) if z[:1] in '+-' and z[:3] not in ('+++', '---')]
    print(f'{name}: {len(diff)} abweichende Zeilen (− Bestand, + erzeugt); Beispiele:')
    for z in diff[:6]:
        print('   ', z[:160])
    return len(diff)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pruefe', action='store_true')
    a = ap.parse_args()
    sichten = [(ZUSCHNITT['msa'], zuschnitt('msa')), (ZUSCHNITT['abitur'], zuschnitt('abitur')),
               (HANDGRIFFE, handgriffe())]
    n = sum(vergleich(name, txt) for name, txt in sichten)
    if a.pruefe:
        return
    for name, txt in sichten:
        open(os.path.join(MN, name), 'w', encoding='utf-8', newline='\n').write(txt)
    print('geschrieben:', ', '.join(name for name, _ in sichten))


if __name__ == '__main__':
    main()
