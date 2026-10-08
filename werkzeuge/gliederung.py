#!/usr/bin/env python3
"""gliederung.py – liest die Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026).

Je Prüfungskapitel eine Datei msa/gliederung/<kapitel>.md bzw. abitur/gliederung/<kapitel>.md
(Format: msa/gliederung/README.md). Die Gliederung ist das gepflegte Objekt; zuordnung-*.csv,
skript-zuschnitt-*.csv und handgriffe-p10.csv sind erzeugte Sichten (werkzeuge/zuordnung.py,
werkzeuge/gliederung-sichten.py). Nur Standardbibliothek.

    import gliederung
    G = gliederung.lies('msa/gliederung/prozent.md')
    alle = gliederung.alle(MN, 'msa')          # {kapitel: G}, Folge der Kopfzeile „Folge:“

Ein Kapitel G ist ein dict:
    datei, kapitel, pruefung ('msa' | 'abitur'), gebiet, name (Kapitelname im Zuschnitt), folge (int),
    skript (True, wenn Bank und Zuordnung – „Skript: nein“ nur Basisteil-Sammlungen),
    bank [Einträge], katalog [Verweise], stufen [Stufe], plaetze [Platz], fokus {name: Text}
Stufe: name, kern ('ja'|'nein'), kern_grund, originale [ids] (explizit oder aus den Zuschnitt-Zeilen),
    bank [(eintrag, sprosse, filter|None, 'inner'|'')]  – das Muster der Zuordnung,
    verwechselbar [(kapitel, stufe)], abschnitt (Zuschnitt), zeilen [(zeile, [ids], [neben])],
    felder {Schlüssel: Wert}  – alle Felder roh
Platz: id, hauptplatz [kap:stufe], ganz_auch [..], zwischenschritt [..], begruendung
"""
import glob
import os
import re

MN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDRE = r'\d{4}-[A-Za-z]+(?:-[a-z]+)*-[A-Z]\d+(?:\.\d+)?[a-z]?'
SPROSSE = re.compile(r'^([a-z0-9-]+?)-(e\d+-k\d+-s\d+)(?:\[([^\]]*)\])?(\(i\))?$')


def _felder(zeilen):
    """„- **Schlüssel:** Wert“ mit eingerückter Fortsetzung und Unterpunkten („  - …“) -> {Schlüssel: Wert}.
    Unterpunkte stehen als Liste unter Schlüssel + '/'."""
    f, key = {}, None
    for z in zeilen:
        m = re.match(r'- \*\*(.+?):\*\*\s*(.*)$', z)
        if m:
            key = re.sub(r'\s*\(.*\)\s*$', '', m.group(1)).strip()
            f[key] = m.group(2).strip()
            continue
        m = re.match(r'\s{2,}- (.*)$', z)
        if m and key:
            f.setdefault(key + '/', []).append(m.group(1).strip())
            continue
        m = re.match(r'\s{2,}(\S.*)$', z)
        if m and key:
            if f.get(key + '/'):
                f[key + '/'][-1] += ' ' + m.group(1).strip()
            else:
                f[key] = (f[key] + ' ' + m.group(1).strip()).strip()
            continue
        if z.strip():
            key = None
    return f


def muster(tokens):
    """Bank-Muster der Zuordnung -> [(eintrag, sprosse, filter, 'inner'|'')]."""
    out = []
    for t in (tokens or '').split():
        if t in ('–', '-'):
            continue
        m = SPROSSE.match(t)
        if not m:
            raise ValueError(f'Bank-Muster unlesbar: {t}')
        filt = [x for x in m.group(3).split(',') if x] if m.group(3) is not None else None
        out.append((m.group(1), m.group(2), filt, 'inner' if m.group(4) else ''))
    return out


def muster_text(maps):
    t = []
    for e, pre, orig, inner in maps:
        s = f'{e}-{pre}'
        if orig:
            s += '[' + ','.join(orig) + ']'
        if inner:
            s += '(i)'
        t.append(s)
    return ' '.join(t)


def _zeile(t):
    """„<Zeile> [ids] neben [ids]“ -> (zeile, [ids], [neben])."""
    m = re.match(r'^(.*?)\s*\[([^\]]*)\](?:\s*neben\s*\[([^\]]*)\])?\s*$', t)
    if not m:
        raise ValueError(f'Zuschnitt-Zeile unlesbar: {t}')
    return m.group(1).strip(), m.group(2).split(), (m.group(3) or '').split()


def lies(pfad):
    txt = open(pfad, encoding='utf-8').read()
    G = {'datei': pfad, 'kapitel': os.path.splitext(os.path.basename(pfad))[0], 'pruefung': 'msa',
         'gebiet': '', 'name': '', 'folge': 0, 'skript': True, 'bank': [], 'katalog': [],
         'stufen': [], 'plaetze': [], 'fokus': {}}
    teile = re.split(r'^(?=## )', txt, flags=re.M)
    for z in teile[0].splitlines():
        m = re.match(r'(Prüfung|Kapitel|Gebiet|Name|Folge|Bank|Katalog|Skript):\s*(.*)$', z)
        if not m:
            continue
        k, w = m.group(1), m.group(2).strip()
        if k == 'Prüfung':
            G['pruefung'] = w
        elif k == 'Kapitel':
            G['kapitel'] = w
        elif k == 'Gebiet':
            G['gebiet'] = w
        elif k == 'Name':
            G['name'] = w
        elif k == 'Folge':
            G['folge'] = int(w)
        elif k == 'Skript':
            G['skript'] = w.lower() != 'nein'
        else:
            G[k.lower()] = [x.strip() for x in w.split('|') if x.strip()]
    for t in teile[1:]:
        kopf = t.splitlines()[0][3:].strip()
        if kopf == 'Stufen':
            for b in re.split(r'^(?=### )', t, flags=re.M)[1:]:
                zl = b.splitlines()
                G['stufen'].append(_stufe(zl[0][4:].strip(), _felder(zl[1:]), G))
        elif kopf.startswith('Plätze'):
            for z in t.splitlines()[1:]:
                if not z.startswith('|') or re.match(r'^\|\s*-', z) or z.startswith('| id'):
                    continue
                c = [x.strip() for x in z.strip().strip('|').split('|')]
                c += [''] * (5 - len(c))
                def refs(s):
                    return [x if re.match(r'^[a-z-]+:', x) else f'{G["kapitel"]}:{x}' for x in
                            (y.strip() for y in s.split(';')) if x]
                G['plaetze'].append(dict(id=c[0], hauptplatz=refs(c[1]), ganz_auch=refs(c[2]),
                                         zwischenschritt=refs(c[3]), begruendung=c[4].replace('\\|', '|')))
        elif kopf.startswith('Fokus '):
            G['fokus'][kopf[6:].strip()] = t
    return G


def _stufe(name, f, G):
    kern, _, grund = (f.get('Kern') or '').partition(' – ')
    verw = []
    for x in (f.get('Verwechselbar') or '').split(' | '):
        x = x.strip()
        if x:
            verw.append(tuple(x.split(':', 1)) if re.match(r'^[a-z-]+:', x) else (G['kapitel'], x))
    zeilen = [_zeile(z) for z in f.get('Zuschnitt/', [])]
    orig = (f.get('Originale') or '').split()
    if not orig and zeilen:
        for _, ids, _ in zeilen:
            orig += [i for i in ids if i not in orig]
    return dict(name=name, kern=kern.strip(), kern_grund=grund.strip(), originale=orig,
                bank=muster(f.get('Bank', '')), verwechselbar=verw,
                abschnitt=(f.get('Zuschnitt') or '').strip(), zeilen=zeilen, felder=f)


def zuschnitt_zeilen(st):
    """Zeilen der Stufe für den Zuschnitt: explizit (Unterpunkte) oder eine Zeile mit dem Namen der Stufe
    und den Originalen ab 2022 ohne EBR (Reihenfolge der Originale), ohne Nebenplatz."""
    if st['zeilen']:
        return st['zeilen']
    ids = [i for i in st['originale'] if i[:4] >= '2022' and '-EBR-' not in i]
    return [(st['name'], ids, [])]


def alle(mn=MN, pruefung='msa'):
    ordner = {'msa': 'msa', 'abitur': 'abitur'}[pruefung]
    out = {}
    for p in sorted(glob.glob(os.path.join(mn, ordner, 'gliederung', '*.md'))):
        if os.path.basename(p).lower() == 'readme.md':
            continue
        G = lies(p)
        out[G['kapitel']] = G
    return dict(sorted(out.items(), key=lambda kv: (kv[1]['folge'], kv[0])))


def fokus_text(G, name):
    """Text des Fokus-Blocks „## Fokus <name>“ mit Überschriften eine Ebene hoch (### -> ##, #### -> ###),
    so dass er wie ein Steckbrief (aufgabenbank/werkzeuge/steckbrief.py) gelesen werden kann."""
    t = G['fokus'].get(name)
    if t is None:
        return None
    out = []
    for z in t.splitlines()[1:]:
        if z.startswith('#### '):
            z = z[1:]
        elif z.startswith('### '):
            z = z[1:]
        out.append(z)
    return '\n'.join(out) + '\n'
