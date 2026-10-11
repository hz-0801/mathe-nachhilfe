#!/usr/bin/env python3
"""Prüft msa/mehr-p10.csv (Mehr-Block, alle Kapitel).

1. Jede pruef-Zeile wird mit eval (nur math) gerechnet und mit der Zahl in
   loesung verglichen (Rundung auf die Stellen der Lösung). Mehrere
   Teilergebnisse stehen in loesung und pruef durch " | " getrennt; verglichen
   wird je Teilergebnis die letzte Zahl der loesung.
2. Jede id aus zuordnung-<kapitel>.csv (Kapitel, die in der Datei vorkommen)
   kommt genau einmal in der Datei vor (eltern_id), in dem Kapitel, in dem sie
   zuerst Hauptplatz ist; ein Nebenplatz zählt dort, wo er Hauptplatz ist.
   Ausnahmen: 2026-EBR-Zwillinge (stehen mit ihrem FOR-Zwilling) und ids ohne
   Wortlaut in allen wortlaut-eigen-*.csv (keine Vorlage, keine Zeile).
3. Ohne bemerkung "keine Zahlen"/"offen" muss sich die Zahlenmenge des
   Wortlauts vom Original (wortlaut-eigen-*.csv, Vorspann + Teil) unterscheiden.
4. Kein ASCII-Minus vor Zahlen in wortlaut/loesung.
Aufruf: python3 msa/mehr-pruef.py [--teil]   (--teil: Vollständigkeit auslassen)
Ohne Meldung = alles in Ordnung."""
import csv, math, os, re, sys
D = os.path.dirname(os.path.abspath(__file__))
ZWILLING = {'2026-EBR-K3a': '2026-FOR-K4a', '2026-EBR-K3b': '2026-FOR-K4b'}
KOPF = 'id;marke;quelle;kapitel;einheit;stufe;art;eltern_id;auf_blatt;wortlaut;abbildung;loesung;pruef;zahlart;schwere;rang;bemerkung'.split(';')
ZAHL = re.compile(r'[−-]?\d+(?:,\d+)?')

def lies(name):
    with open(os.path.join(D, name), encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))

def zahl(txt):
    m = ZAHL.findall(txt)
    return m[-1] if m else None

def num(s):
    return float(s.replace('−', '-').replace(',', '.'))

def zahlen(txt):
    return sorted(ZAHL.findall(txt))

KAPITEL = ['dreiecke', 'prozent', 'lineare', 'quadratische', 'flaechen', 'koerper', 'daten',
           'wahrscheinlichkeit', 'gleichungssysteme', 'wachstum']
MINUS = re.compile(r'(?<![\w−–])-\d')

def vorlagen():
    """id -> Liste (teil, wortlaut) aus allen wortlaut-eigen-*.csv."""
    o = {}
    for k in KAPITEL:
        fn = f'wortlaut-eigen-{k}.csv'
        if os.path.exists(os.path.join(D, fn)):
            for r in lies(fn):
                o.setdefault(r['id'], []).append(r)
    return o

def voll(o, i):
    """Vorspann + Teil der Aufgabe i (Text, Teil allein) oder None."""
    if i not in o:
        return None
    teil = ' '.join(r['wortlaut'] + ' ' + r['abbildung'] for r in o[i])
    m = re.match(r'(.*[BK]\d+)[a-z]$', i)
    vor = ' '.join(r['wortlaut'] + ' ' + r['abbildung'] for r in o.get(m.group(1), [])) if m else ''
    return (vor + ' ' + teil).strip(), teil

def main():
    teil = '--teil' in sys.argv
    fehler = []
    with open(os.path.join(D, 'mehr-p10.csv'), encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f, delimiter=';')
        if rd.fieldnames not in (KOPF, KOPF + ['grafik', 'form']):   # grafik, form: Setzer-Felder (12.10.)
            fehler.append('Kopfzeile weicht ab')
        rows = list(rd)
    orig = vorlagen()
    gesehen = {}
    for r in rows:
        i = r['id']
        gesehen[r['eltern_id']] = gesehen.get(r['eltern_id'], 0) + 1
        if i != r['eltern_id'] + '-m1' or r['art'] != 'mehr':
            fehler.append(f'{i}: id/art')
        if r['kapitel'] not in KAPITEL:
            fehler.append(f'{i}: kapitel')
        if r['auf_blatt'] not in ('ja', 'nein') or r['schwere'] not in ('I', 'II', 'III'):
            fehler.append(f'{i}: auf_blatt/schwere')
        if r['zahlart'] not in ('ganz', 'dezimal', 'bruch', 'prozent'):
            fehler.append(f'{i}: zahlart')
        for feld in ('wortlaut', 'loesung'):
            if MINUS.search(re.sub(r'\$[^$]*\$', '', r[feld])):
                fehler.append(f'{i}: ASCII-Minus in {feld}')
        pr = r['pruef'].strip()
        if pr:
            ps = [x.strip() for x in pr.split(' | ')]
            ls = [x.strip() for x in r['loesung'].split(' | ')]
            if len(ps) != len(ls):
                fehler.append(f'{i}: Teilergebnisse {len(ps)} pruef / {len(ls)} loesung')
            else:
                for p, l in zip(ps, ls):
                    z = zahl(l)
                    if z is None:
                        fehler.append(f'{i}: keine Zahl in "{l}"'); continue
                    try:
                        v = eval(p, {'__builtins__': {}, 'math': math}, {})
                    except Exception as e:
                        fehler.append(f'{i}: pruef "{p}": {e}'); continue
                    st = len(z.split(',')[1]) if ',' in z else 0
                    if abs(v - num(z)) > 0.5 * 10 ** -st + 1e-9:
                        fehler.append(f'{i}: pruef {p} = {v:.6f}, loesung {z}')
        vl = voll(orig, r['eltern_id'])
        if vl and 'keine Zahlen' not in r['bemerkung'] and not r['bemerkung'].startswith('offen'):
            zo = zahlen(vl[0]); zt = zahlen(vl[1]); zn = zahlen(r['wortlaut'] + ' ' + r['abbildung'])
            if zo and (zo == zn or (zt and zt == zn)):
                fehler.append(f'{i}: Zahlen wie im Original')
        if r['bemerkung'].startswith('offen') and vl and r['wortlaut'] not in vl[0] and r['wortlaut'] not in vl[1]:
            fehler.append(f'{i}: offen, aber Wortlaut geändert')
    for i, n in gesehen.items():
        if n != 1:
            fehler.append(f'{i}: {n}-mal')
    if not teil:
        kap = {r['kapitel'] for r in rows}
        haupt = {}
        for k in KAPITEL:
            if os.path.exists(os.path.join(D, f'zuordnung-{k}.csv')):
                for z in lies(f'zuordnung-{k}.csv'):
                    for i in z['katalog_ids'].split():
                        haupt.setdefault(i, set()).add(k)
        soll = set()
        for k in KAPITEL:
            if k not in kap:
                continue
            for z in lies(f'zuordnung-{k}.csv'):
                hi = z['katalog_ids'].split()
                for i in hi + z['nebenplaetze'].split():
                    if i in haupt and k not in haupt[i] and not (haupt[i] & kap):
                        continue
                    soll.add(i)
        for i in sorted(soll):
            if i in ZWILLING:
                if ZWILLING[i] not in gesehen:
                    fehler.append(f'{i}: Zwilling {ZWILLING[i]} fehlt')
            elif i not in gesehen and i in orig:
                fehler.append(f'{i}: fehlt')
        for i in gesehen:
            if i not in soll:
                fehler.append(f'{i}: in keiner Zuordnung der geprüften Kapitel')
    for m in fehler:
        print(m)
    sys.exit(1 if fehler else 0)

main()
