#!/usr/bin/env python3
"""Prüft eine Beitabelle (Vorrat) gegen den Katalog.

Aufruf: python3 werkzeuge/vorrat-pruef.py <vorrat.csv> <katalog.csv>

Prüfungen: Kopfzeile id;kurz;zwischen;stich;neben;abh;sympy; jede id der
Beitabelle genau einmal und im Katalog vorhanden; Reihenfolge wie im Katalog;
kurz nie leer; neben nur Themen, die im Katalog als thema vorkommen, und nicht
das Hauptthema der Zeile; abh nur ids desselben Papiers, die im Katalog stehen,
nicht die eigene id – oder, beim CAS-Nachtrag, ids des WTR-Papiers desselben
Hefts (papier „…-cas“ → „…“, wie im Katalog; seit 05.10.2026); sympy aus {ok, abw: …, nicht rechenbar, offen: …};
ASCII-Minus vor Ziffern in kurz/zwischen; Datei UTF-8 ohne BOM mit LF.
Rückgabe 0 bei fehlerfreiem Lauf, sonst 1 mit Fehlerliste.
"""
import csv
import re
import sys

KOPF = ['id', 'kurz', 'zwischen', 'stich', 'neben', 'abh', 'sympy']


def lies(pfad):
    with open(pfad, 'rb') as fh:
        roh = fh.read()
    fehler = []
    if roh.startswith(b'\xef\xbb\xbf'):
        fehler.append('BOM am Dateianfang')
    if b'\r\n' in roh:
        fehler.append('CRLF-Zeilenenden')
    text = roh.decode('utf-8')
    zeilen = list(csv.reader(text.splitlines(), delimiter=';'))
    return zeilen, fehler


def main(vorrat, katalog):
    zeilen, fehler = lies(vorrat)
    kat = list(csv.DictReader(open(katalog, encoding='utf-8'), delimiter=';'))
    themen = {r['thema'] for r in kat}
    kat_ids = [r['id'] for r in kat]
    kat_by = {r['id']: r for r in kat}
    if not zeilen or zeilen[0] != KOPF:
        fehler.append(f'Kopfzeile falsch: {zeilen[0] if zeilen else "leer"}')
        return melde(fehler)
    gesehen = set()
    reihenfolge = []
    for nr, z in enumerate(zeilen[1:], start=2):
        if len(z) != len(KOPF):
            fehler.append(f'Zeile {nr}: {len(z)} Felder statt {len(KOPF)}')
            continue
        d = dict(zip(KOPF, z))
        i = d['id']
        if i in gesehen:
            fehler.append(f'Zeile {nr}: id {i} doppelt')
        gesehen.add(i)
        if i not in kat_by:
            fehler.append(f'Zeile {nr}: id {i} nicht im Katalog')
            continue
        reihenfolge.append(i)
        if not d['kurz'].strip():
            fehler.append(f'{i}: kurz leer')
        for th in filter(None, d['neben'].split('|')):
            if th not in themen:
                fehler.append(f'{i}: neben enthält unbekanntes Thema „{th}“')
            elif th == kat_by[i]['thema']:
                fehler.append(f'{i}: neben wiederholt das Hauptthema „{th}“')
        papier = kat_by[i]['papier']
        for a in filter(None, d['abh'].split('|')):
            if a not in kat_by:
                fehler.append(f'{i}: abh verweist auf unbekannte id {a}')
            elif kat_by[a]['papier'] != papier and papier != kat_by[a]['papier'] + '-cas':
                fehler.append(f'{i}: abh {a} liegt in anderem Papier')
            elif a == i:
                fehler.append(f'{i}: abh verweist auf sich selbst')
        sy = d['sympy']
        if not (sy in ('ok', 'nicht rechenbar') or sy.startswith('abw: ') or sy.startswith('offen: ')):
            fehler.append(f'{i}: sympy-Wert „{sy}“ unzulässig')
        for feld in ('kurz', 'zwischen'):
            if re.search(r'(^|[\s(=|;])-\d', d[feld]):
                fehler.append(f'{i}: ASCII-Minus vor Ziffer in {feld}')
    # Reihenfolge wie im Katalog
    pos = {i: n for n, i in enumerate(kat_ids)}
    if reihenfolge != sorted(reihenfolge, key=pos.get):
        fehler.append('Reihenfolge weicht vom Katalog ab')
    return melde(fehler, len(reihenfolge))


def melde(fehler, n=0):
    if fehler:
        print('FEHLER:')
        for f in fehler:
            print(' -', f)
        return 1
    print(f'Prüfung bestanden: {n} Zeilen.')
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
