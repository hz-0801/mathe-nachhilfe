#!/usr/bin/env python3
"""anzeigenamen-pruef.py – Abschnitts- und Stufennamen der P10-Gliederung gegen pruefung.md § 2.

Anlass (plan.md § 10, 13.10.2026 g): Stufen stehen nur in der Gliederung (msa/gliederung/*.md);
ein Agent, der aus den Daten baut, verliert eine Festlegung, die nur in pruefung.md steht (P4Z2 hat
Hypotenuse und Kathete wieder zusammengelegt). Das Skript vergleicht, ändert nichts.
Soll sind seit 14.10.2026 (plan.md § 7 Schritt 2) die Namen der Gliederung: eine Meldung heißt
„pruefung.md § 2 auf die Gliederung nachziehen“ – außer der Lehrer hat in § 2 neu entschieden, dann
umgekehrt.

Gelesen aus pruefung.md § 2 („Hauptteil … Einheiten“ bis „Basisteil“):
  - je Kapitelzeile „- <Kapitel>: A (n · m) · B (…) …“ die Abschnitte (Einheiten = Blätter);
  - „Blattnamen und Stufen (…): <Blatt> – <Stufe> · <Stufe> …; <Blatt> – …“ (bisher nur Dreiecke);
  - „Stufen X, Y, Z – …“ in der Klammer eines Abschnitts (Prozent), „Stufe X ohne Original“ (Daten).
Gelesen aus der Gliederung: Zuschnitt der Stufen (Abschnitt), „Anzeigenamen: <Zuschnitt> = <Blatt>“,
„- **Anzeigename:**“ der Stufe (sonst ihr Name).

Meldungen:
  fehlt          Abschnitt oder Stufe aus § 2 kommt in der Gliederung nicht vor
  zusammengelegt eine Stufe der Gliederung trägt die Kennwörter zweier Stufen aus § 2 („… oder …“)
  umbenannt/neu  Abschnitt oder Stufe der Gliederung steht nicht in § 2
  Folge          die Stufen eines Blatts stehen in anderer Reihenfolge als in § 2
Vergleich ohne Groß-/Kleinschreibung, Satzzeichen und Klammern („Sinussatz, …“ = „(Sinussatz)“).
Aufruf aus der Wurzel: python3 werkzeuge/anzeigenamen-pruef.py   – ohne Meldung Rückgabe 0, sonst 1.
"""
import os
import re
import sys

MN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(MN, 'werkzeuge'))
import gliederung as GL  # noqa: E402

FUELL = {'und', 'oder', 'mit', 'im', 'in', 'der', 'die', 'das', 'den', 'dem', 'ein', 'eine', 'zwei',
         'gesucht', 'erst', 'dann', 'auf', 'aus', 'von', 'zu', 'nach', 'am', 'an', 'als'}


def norm(s):
    return re.sub(r'\s+', ' ', re.sub(r'[^\wäöüß ]', ' ', (s or '').lower())).strip()


def woerter(s):
    return {w for w in norm(s).split() if w not in FUELL and len(w) > 2}


def oben(s, sep):
    """s an sep teilen, aber nicht in Klammern."""
    out, tief, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        tief += c in '(„' and 1 or 0
        tief -= c in ')“' and 1 or 0
        if tief == 0 and s.startswith(sep, i):
            out.append(cur)
            cur, i = '', i + len(sep)
            continue
        cur += c
        i += 1
    return out + [cur]


def lies_pruefung():
    t = open(os.path.join(MN, 'pruefung.md'), encoding='utf-8').read()
    a = t.index('## 2 P10')
    t = t[a:t.index('\n## ', a + 5)]
    t = t[t.index('Hauptteil'):t.index('Basisteil (')]
    # Kapitelzeilen „  - Name: …“ mit Fortsetzung
    zeilen, cur = [], None
    for z in t.splitlines():
        m = re.match(r'^  - (\S[^:]*):\s*(.*)$', z)
        if m:
            cur = [m.group(1).strip(), m.group(2)]
            zeilen.append(cur)
        elif cur and re.match(r'^\s{4,}\S', z):
            cur[1] += ' ' + z.strip()
        elif not z.strip().startswith('-'):
            cur = None if not z.strip() else cur
    kap = {}
    for name, rest in zeilen:
        teile = re.split(r'\.\s+(?=Blattnamen|Gruppen)', rest)
        abschn, stufen = [], {}
        for x in oben(teile[0].rstrip('.'), ' · '):
            m = re.match(r'^(.*?)\s*\((.*)\)\s*$', x.strip())
            n, klammer = (m.group(1), m.group(2)) if m else (x.strip(), '')
            abschn.append(n)
            s = re.search(r'Stufen\s+(.*?)\s+–', klammer)
            if s:
                stufen[n] = [y.strip() for y in s.group(1).split(',')]
            s = re.search(r'Stufe\s+(\S+)\s+ohne Original', klammer)
            if s:
                stufen.setdefault(n, []).append(s.group(1))
        blatt = {}
        for tl in teile[1:]:
            if not tl.startswith('Blattnamen'):
                continue
            tl = tl[tl.index('):') + 2:] if '):' in tl else tl.split(':', 1)[1]
            for b in oben(tl.strip().rstrip('.'), '; '):
                if ' – ' in b:
                    bn, st = b.split(' – ', 1)
                    blatt[bn.strip()] = [y.strip() for y in oben(st, ' · ')]
                else:
                    blatt[re.sub(r'\s*\(.*$', '', b).strip()] = None
        kap[norm(name)] = dict(name=name, abschnitte=abschn, stufen=stufen, blatt=blatt)
    return kap


def lies_gliederung():
    out = {}
    for k, G in GL.alle(MN, 'msa').items():
        if not G['skript']:
            continue
        roh = open(G['datei'], encoding='utf-8').read()
        anz = {}
        for z in roh.split('\n## ')[0].splitlines():
            m = re.match(r'^Anzeigenamen:\s*(.*)$', z)
            if m:
                for teil in m.group(1).split('|'):
                    if '=' in teil:
                        a, b = teil.split('=', 1)
                        anz[a.strip()] = b.strip()
        ab = {}
        for st in G['stufen']:
            if not st['abschnitt'] or st['abschnitt'].startswith('Weitere'):
                continue
            x = ab.setdefault(st['abschnitt'], dict(anzeige=anz.get(st['abschnitt'], st['abschnitt']), stufen=[]))
            x['stufen'].append((st['name'], st['felder'].get('Anzeigename') or st['name']))
        ab = {a: x for a, x in ab.items()}
        out[norm(G['name'])] = dict(name=G['name'], datei=os.path.relpath(G['datei'], MN), abschnitte=ab)
    return out


def gleich(a, b):
    return norm(a) == norm(b)


def pruefe():
    P, G = lies_pruefung(), lies_gliederung()
    meld = []
    for kk, p in P.items():
        g = G.get(kk) or next((v for k2, v in G.items() if k2 and kk.startswith(k2)), None)
        if not g:
            meld.append(f'{p["name"]}: Kapitel fehlt in msa/gliederung/')
            continue
        ab_g = g['abschnitte']
        def finde(n):
            return next((a for a, x in ab_g.items() if gleich(a, n) or gleich(x['anzeige'], n)), None)
        bekannt = set()
        for n in p['abschnitte'] + list(p['blatt']):
            a = finde(n)
            if a:
                bekannt.add(a)
            elif n in p['abschnitte'] and not any(gleich(n, b) for b in p['blatt']):
                meld.append(f'{g["datei"]}: Abschnitt „{n}“ (pruefung.md § 2) fehlt in der Gliederung – § 2 nachziehen?')
        for a in ab_g:
            if a not in bekannt:
                meld.append(f'{g["datei"]}: Abschnitt „{a}“ steht nicht in pruefung.md § 2 (umbenannt/neu)')
        # Stufen je Blatt (Blattnamen und Stufen)
        for bn, soll in p['blatt'].items():
            a = finde(bn)
            if not a or not soll:
                continue
            ist = [x for _, x in ab_g[a]['stufen']]
            for s in soll:
                if any(gleich(s, i) for i in ist):
                    continue
                w = woerter(s)
                zus = [i for i in ist if w and w <= woerter(i)
                       and any(o != s and woerter(o) and woerter(o) <= woerter(i) for o in soll)]
                if zus:
                    meld.append(f'{g["datei"]}: {bn} – Stufe „{s}“ zusammengelegt in „{zus[0]}“')
                else:
                    meld.append(f'{g["datei"]}: {bn} – Stufe „{s}“ (pruefung.md § 2) fehlt in der Gliederung – § 2 nachziehen?')
            for i in ist:
                if not any(gleich(s, i) for s in soll):
                    meld.append(f'{g["datei"]}: {bn} – Stufe „{i}“ steht nicht in pruefung.md § 2 (umbenannt/neu)')
            gem = [i for i in ist if any(gleich(s, i) for s in soll)]
            folge = [s for s in soll if any(gleich(s, i) for i in ist)]
            if [norm(x) for x in gem] != [norm(x) for x in folge]:
                meld.append(f'{g["datei"]}: {bn} – Folge der Stufen {gem} statt {folge}')
        # Stufen aus der Klammer eines Abschnitts (Wort genügt: „Prozentwert“ in „Prozentwert gesucht“)
        alle = [(n2, x) for v in ab_g.values() for n2, x in v['stufen']]
        for n, soll in p['stufen'].items():
            for s in soll:
                w = woerter(re.sub(r'\bmit\b.*$', '', s))
                if any(w and w <= woerter(x) for _, x in alle):
                    continue
                um = next((x for n2, x in alle if w and w <= woerter(n2)), None)
                if um:
                    meld.append(f'{g["datei"]}: Stufe „{s}“ ({n}, pruefung.md § 2) umbenannt in „{um}“')
                else:
                    meld.append(f'{g["datei"]}: Stufe „{s}“ ({n}, pruefung.md § 2) fehlt')
    for kk, g in G.items():
        if not any(k2.startswith(kk) for k2 in P):
            meld.append(f'{g["datei"]}: Kapitel „{g["name"]}“ steht nicht in pruefung.md § 2')
    return meld


if __name__ == '__main__':
    m = pruefe()
    for x in m:
        print(x)
    sys.exit(1 if m else 0)
