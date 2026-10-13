#!/usr/bin/env python3
"""Zieht in msa/mehr-p10/*.csv die Zahlen der Spalte abbildung auf die des
wortlauts nach (Mehr-Block: wortlaut und loesung tragen neue Zahlen, die
Skizzenbeschreibung oft noch alte).

Verfahren je Zeile mit Zahlen in abbildung:
1. Eine Skizzenzahl, die in wortlaut oder loesung vorkommt, bleibt.
2. Sonst wird sie, wenn eine Einheit folgt (cm, m, °, % …), über Bezeichner
   in der Nähe (Seitenname, Winkelname, Wort wie „Grundseite"; näher zählt
   mehr) einer Zahl des wortlauts mit derselben Einheit zugeordnet, die noch
   nicht in der Skizze steht; gibt es genau einen besten Kandidaten, wird sie
   ersetzt. Zahlen ohne Einheit (Achsen, Tabellen) bleiben und werden gemeldet.
3. Gemeldet wird je Zeile, was offen bleibt: Zahlen ohne eindeutigen
   Kandidaten, und Skizzen, deren Zahlen noch denen des Originals
   (wortlaut-eigen-<kapitel>.csv) gleichen, obwohl der Wortlaut neue hat.
   Diese Fälle werden von Hand bearbeitet.
Aufruf: python3 msa/mehr-abbildung.py [--probe]   (--probe: nur melden)
"""
import csv, glob, io, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
ZAHL = re.compile(r'[−-]?\d+(?:[,.]\d+)?')
TOK = re.compile(r'[−-]?\d+(?:[,.]\d+)?|\$[^$]+\$|\w+|\S')
EINHEIT = {'cm', 'm', 'km', 'mm', 'dm', '°', '%', '€', 'kg', 'g', 'l', 'ml', 'h', 'min', 's', 'Kästchen', 'cm²', 'm²', 'cm³', 'm³'}
STOP = {'bei', 'und', 'von', 'nach', 'auf', 'zwischen', 'oben', 'unten', 'links', 'rechts', 'der', 'die', 'das',
        'ist', 'lang', 'hoch', 'breit', 'groß', 'etwa', 'in', 'mit', 'ein', 'eine', 'einen', 'dem', 'den', 'des',
        'nicht', 'maßstabsgerecht', 'gestrichelt', 'zu', 'bis', 'am', 'im', 'über', 'unter', 'vom', 'zum', 'zur'}
KAPITEL = ['dreiecke', 'prozent', 'lineare', 'quadratische', 'flaechen', 'koerper', 'daten',
           'wahrscheinlichkeit', 'gleichungssysteme', 'wachstum']
FENSTER = 12

def lies(name):
    with open(os.path.join(D, name), encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))

def tokens(txt):
    return [m.group() for m in TOK.finditer(txt)]

def istzahl(t):
    return bool(ZAHL.fullmatch(t))

def bezeichner(toks, j, weite=3):
    """Bezeichner um Position j -> kleinster Abstand: Wörter, keine Zahlen,
    Einheiten, Stoppwörter, Satzzeichen."""
    b = {}
    if j >= 2 and toks[j - 1] == '=':
        return {toks[j - 2]: 1}
    for k in range(max(0, j - weite), min(len(toks), j + weite + 1)):
        t = toks[k]
        if k == j or istzahl(t) or t in EINHEIT or t in STOP or not re.search(r'\w', t):
            continue
        b[t] = min(b.get(t, 99), abs(k - j))
    return b

def einheit(toks, j):
    return toks[j + 1] if j + 1 < len(toks) and toks[j + 1] in EINHEIT else None

def vorlagen():
    o = {}
    for k in KAPITEL:
        fn = f'wortlaut-eigen-{k}.csv'
        if os.path.exists(os.path.join(D, fn)):
            for r in lies(fn):
                o.setdefault(r['id'], []).append(r)
    return o

def main():
    probe = '--probe' in sys.argv
    dateien = sorted(glob.glob(os.path.join(D, 'mehr-p10', '*.csv')))
    kopf, rows, teile = None, [], []
    for pfad in dateien:
        with open(pfad, encoding='utf-8', newline='') as f:
            zeilen = list(csv.reader(io.StringIO(f.read()), delimiter=';'))
        kopf = kopf or zeilen[0]
        assert zeilen[0] == kopf, f'{pfad}: Kopfzeile weicht ab'
        teile.append((pfad, zeilen[1:]))
        rows += zeilen[1:]
    IA, IW, IL, IE, IB = (kopf.index(x) for x in ('abbildung', 'wortlaut', 'loesung', 'eltern_id', 'bemerkung'))
    orig = vorlagen()
    geaendert, meldungen = 0, []
    for r in rows:
        i, abb = r[0], r[IA]
        if not ZAHL.search(abb):
            continue
        tw = tokens(r[IW])
        neu = set(ZAHL.findall(r[IW] + ' ' + r[IL]))
        kand = [(j, einheit(tw, j), bezeichner(tw, j, FENSTER)) for j, t in enumerate(tw) if istzahl(t)]
        ta = tokens(abb)
        in_skizze = set(ZAHL.findall(abb))
        offen, ersatz = [], {}
        benutzt = set()
        for j, t in enumerate(ta):
            if not istzahl(t) or t in neu:
                continue
            e, bz = einheit(ta, j), bezeichner(ta, j)
            treffer = []
            for jw, ew, bw in kand:
                if e is None or e != ew or tw[jw] in in_skizze or jw in benutzt:
                    continue
                s = sum(1 / bw[x] for x in bz if x in bw)
                if s:
                    treffer.append((s, jw))
            if treffer:
                treffer.sort(reverse=True)
                if len(treffer) == 1 or treffer[0][0] > treffer[1][0]:
                    ersatz[j] = tw[treffer[0][1]]
                    benutzt.add(treffer[0][1])
                    continue
            offen.append(t + (' ' + e if e else ''))
        if ersatz:
            text, k = '', 0
            for j, mt in enumerate(TOK.finditer(abb)):
                text += abb[k:mt.start()] + ersatz.get(j, mt.group())
                k = mt.end()
            text += abb[k:]
            print(f'{i}: {abb}\n  -> {text}')
            r[IA] = text
            geaendert += len(ersatz)
        if offen:
            meldungen.append(f'{i}: offen {", ".join(offen)}')
        # Skizze noch wie im Original?
        e = r[IE]
        m = re.match(r'(.*[BK]\d+)[a-z]$', e)
        alt = [x['abbildung'] for x in orig.get(e, []) + (orig.get(m.group(1), []) if m else [])]
        za = sorted(ZAHL.findall(r[IA]))
        if za and any(sorted(ZAHL.findall(a)) == za for a in alt) and 'keine Zahlen' not in r[IB]:
            meldungen.append(f'{i}: Skizzenzahlen wie im Original')
    for m in meldungen:
        print('MELDUNG', m)
    print(f'{geaendert} Zahlen ersetzt, {len(meldungen)} Meldungen')
    if not probe:
        for pfad, zl in teile:   # zl enthält dieselben Zeilenobjekte wie rows, in der Datei des Kapitels
            out = io.StringIO()
            csv.writer(out, delimiter=';', lineterminator='\n').writerows([kopf] + zl)
            with open(pfad, 'w', encoding='utf-8', newline='') as f:
                f.write(out.getvalue())

main()
