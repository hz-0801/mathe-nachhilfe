#!/usr/bin/env python3
"""Prüft msa/mehr-p10.csv (Mehr-Block Dreiecke).

1. Jede pruef-Zeile wird mit eval (nur math) gerechnet und mit der Zahl in
   loesung verglichen (Rundung auf die Stellen der Lösung). Mehrere
   Teilergebnisse stehen in loesung und pruef durch " | " getrennt; verglichen
   wird je Teilergebnis die letzte Zahl der loesung.
2. Jede id aus zuordnung-dreiecke.csv kommt genau einmal vor (eltern_id).
   Ausnahme: 2026-EBR-Zwillinge (Nebenplätze) stehen mit ihrem FOR-Zwilling.
3. Ohne bemerkung "keine Zahlen"/"offen" muss sich die Zahlenmenge des
   Wortlauts vom Original (wortlaut-eigen-dreiecke.csv) unterscheiden.
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

def main():
    teil = '--teil' in sys.argv
    fehler = []
    with open(os.path.join(D, 'mehr-p10.csv'), encoding='utf-8', newline='') as f:
        rd = csv.DictReader(f, delimiter=';')
        if rd.fieldnames != KOPF:
            fehler.append('Kopfzeile weicht ab')
        rows = list(rd)
    orig = {r['id']: r for r in lies('wortlaut-eigen-dreiecke.csv')}
    gesehen = {}
    for r in rows:
        i = r['id']
        gesehen[r['eltern_id']] = gesehen.get(r['eltern_id'], 0) + 1
        if i != r['eltern_id'] + '-m1' or r['art'] != 'mehr':
            fehler.append(f'{i}: id/art')
        if r['auf_blatt'] not in ('ja', 'nein') or r['schwere'] not in ('I', 'II', 'III'):
            fehler.append(f'{i}: auf_blatt/schwere')
        if r['zahlart'] not in ('ganz', 'dezimal', 'bruch', 'prozent'):
            fehler.append(f'{i}: zahlart')
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
        o = orig.get(r['eltern_id'])
        if o and 'keine Zahlen' not in r['bemerkung'] and not r['bemerkung'].startswith('offen'):
            zo = zahlen(o['wortlaut'])
            if zo and zo == zahlen(r['wortlaut']):
                fehler.append(f'{i}: Zahlen wie im Original')
        if r['bemerkung'].startswith('offen') and o and r['wortlaut'] != o['wortlaut']:
            fehler.append(f'{i}: offen, aber Wortlaut geändert')
    for i, n in gesehen.items():
        if n != 1:
            fehler.append(f'{i}: {n}-mal')
    if not teil:
        soll = set()
        for z in lies('zuordnung-dreiecke.csv'):
            soll.update(z['katalog_ids'].split()); soll.update(z['nebenplaetze'].split())
        for i in sorted(soll):
            if i in ZWILLING:
                if ZWILLING[i] not in gesehen:
                    fehler.append(f'{i}: Zwilling {ZWILLING[i]} fehlt')
            elif i not in gesehen:
                fehler.append(f'{i}: fehlt')
        for i in gesehen:
            if i not in soll:
                fehler.append(f'{i}: nicht in zuordnung-dreiecke.csv')
    for m in fehler:
        print(m)
    sys.exit(1 if fehler else 0)

main()
