"""Wie stark filtert das Skript? (v0.1, 04.10.2026)

Zählt je Katalogeintrag (katalog/*.md ohne _* und index.md) die
Lerneinheiten und ihre Prüfungsmarken (Zeile „Marken:“ unter jeder
Einheit) und je Einheit die Aufgaben der Bank (aufgabenbank/bank/
<eintrag>/e<n>.jsonl). Daraus: welcher Anteil der Einheiten und der
Bankaufgaben in P10, Abitur GK, Abitur LK und FHR geprüft wird – also
wie weit sich das Skript (Blatt mit Prüfungsfilter) vom allgemeinen
Blatt unterscheidet.

Marken: P10 = „P10“ oder „P10 oft“ (nicht „keine P10-Aufgabe“);
GK = „Abitur GK“; LK = „Abitur LK“; FHR = „FHR“.
Schreibt katalog/_skript-filter.md. Abgeleitet, nie von Hand ändern.
Aufruf aus der Wurzel: python werkzeuge/skript-filter-mass.py
(Bank neben dem Repo oder BANK=<ordner>).
"""
import glob, json, os, re

W = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
BANK = os.environ.get('BANK', os.path.join(W, '..', 'aufgabenbank', 'bank'))
PRUEF = ['P10', 'GK', 'LK', 'FHR']


def marken(zeile):
    m = {t.strip() for t in zeile.split(':', 1)[1].split('·')}
    return {'P10': bool(m & {'P10', 'P10 oft'}), 'GK': 'Abitur GK' in m,
            'LK': 'Abitur LK' in m, 'FHR': 'FHR' in m}


def main():
    zeilen = []
    for f in sorted(glob.glob(os.path.join(W, 'katalog', '*.md'))):
        name = os.path.basename(f)[:-3]
        if name.startswith('_') or name == 'index':
            continue
        s = open(f, encoding='utf-8').read()
        m = re.search(r'### Lerneinheiten\n(.*?)\n###', s, re.S)
        if not m:
            continue
        einh = {}
        nr = None
        for l in m.group(1).split('\n'):
            k = re.match(r'(\d+)\. ', l)
            if k:
                nr = int(k.group(1)); einh[nr] = {p: False for p in PRUEF}
            elif nr and l.strip().startswith('Marken:'):
                einh[nr] = marken(l)
        bank = {}
        for e in einh:
            p = os.path.join(BANK, name, f'e{e}.jsonl')
            bank[e] = sum(1 for _ in open(p, encoding='utf-8')) if os.path.exists(p) else 0
        zeilen.append((name, einh, bank))
    o = ['# Skript-Filter – Anteil geprüfter Einheiten und Bankaufgaben je Katalogeintrag', '',
         'Abgeleitet von `werkzeuge/skript-filter-mass.py` (v0.1); nie von Hand ändern. '
         'Je Prüfung: Einheiten mit Marke / alle Einheiten, dahinter Anteil der Bankaufgaben in diesen Einheiten. '
         '„–“ = keine Einheit geprüft.', '',
         '| Eintrag | Einheiten | Bank | P10 | Abitur GK | Abitur LK | FHR |', '|---|---|---|---|---|---|---|']
    summe = {p: [0, 0] for p in PRUEF}
    for name, einh, bank in zeilen:
        nb = sum(bank.values())
        zellen = []
        for p in PRUEF:
            g = [e for e in einh if einh[e][p]]
            if not g:
                zellen.append('–'); continue
            b = sum(bank[e] for e in g)
            summe[p][0] += b; summe[p][1] += nb
            zellen.append(f'{len(g)}/{len(einh)}' + (f' · {100*b/nb:.0f} %' if nb else ''))
        o.append(f'| {name} | {len(einh)} | {nb} | ' + ' | '.join(zellen) + ' |')
    o += ['', 'Über alle Einträge mit mindestens einer geprüften Einheit: Anteil der Bankaufgaben, die ins Skript kämen – '
          + ' · '.join(f'{p} {100*a/b:.0f} %' for p, (a, b) in summe.items() if b) + '.']
    open(os.path.join(W, 'katalog', '_skript-filter.md'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
    print('\n'.join(o))


if __name__ == '__main__':
    main()
