#!/usr/bin/env python3
"""Fortschrittstafel (plan.md, Meilenstein M1).

Zählt aus den Repos, wie weit jede P10-Stufe und jeder Bankeintrag ist,
und schreibt tafel.md in die Wurzel. Nichts wird geschätzt: jede Spalte
kommt aus einer Datei; was keine Datei belegt, steht als „–“.

Aufruf (aus der Wurzel von mathe-nachhilfe):
  python3 werkzeuge/tafel.py [--bank ../aufgabenbank]

Quellen:
  msa/zuordnung-<kapitel>.csv   Stufen, Kern, echte Aufgaben, Bankaufgaben,
                                Ziel, fehlen (Stand des Zuordnungslaufs)
  katalog/steckbrief/*.md       Kopfzeilen „Kapitel:“ und „Stufen:“
  aufgabenbank bau/pruefheft/   gebaute Hefte <kapitel>-normal-<datum>,
                                Fokusblätter fokus-*/<kapitel>-normal-fokus-*
  katalog/index.md              Status je Katalogeintrag
  aufgabenbank bank/<eintrag>/  Zeilen; werkzeuge/bank-pruef.py <eintrag>
  abnahme.csv                   Abnahmen des Lehrers (ebene;name;datum;urteil;anmerkung)
                                ebene = stufe (kapitel:stufe) | heft (kapitel)
                                | katalog (eintrag)
v1.0 2026-10-08
"""
import argparse, csv, datetime, glob, os, re, subprocess, sys
from collections import OrderedDict

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAPITEL = OrderedDict([
    ('prozent', 'Prozent'), ('dreiecke', 'Dreiecke'), ('flaechen', 'Flächen'),
    ('koerper', 'Körper'), ('lineare', 'Lineare'),
    ('quadratische', 'Quadratische'), ('gleichungssysteme', 'Gleichungssysteme'),
    ('wachstum', 'Wachstum'), ('daten', 'Daten'),
    ('wahrscheinlichkeit', 'Wahrscheinlichkeit')])
REGELSTAND = '2026-10-07'  # jüngster Stand von bau/bauregeln.md (plan.md W3)


def lies_csv(pfad):
    with open(pfad, encoding='utf-8') as f:
        kopf = f.readline()
        f.seek(0)
        return list(csv.DictReader(f, delimiter=';' if ';' in kopf else ','))


def steckbriefe():
    """kapitel -> {stufe: dateiname}"""
    erg = {}
    for p in sorted(glob.glob(os.path.join(WURZEL, 'katalog/steckbrief/*.md'))):
        if p.endswith('README.md'):
            continue
        kap, stufen = None, []
        for z in open(p, encoding='utf-8'):
            if z.startswith('Kapitel:'):
                kap = z.split(':', 1)[1].strip()
            elif z.startswith('Stufen:'):
                stufen = [s.strip() for s in z.split(':', 1)[1].split('|')]
        for s in stufen:
            erg.setdefault(kap, {})[s] = os.path.basename(p)
    return erg


def hefte(bank):
    """kapitel -> (datum, ordner) des jüngsten Normal-Hefts; Fokus je kapitel."""
    heft, fokus = {}, {}
    for d in glob.glob(os.path.join(bank, 'bau/pruefheft/*-normal-20*')):
        m = re.match(r'([a-z]+)-normal-(\d{4}-\d{2}-\d{2})$', os.path.basename(d))
        if m and m.group(1) in KAPITEL and not os.path.basename(d).count('fokus'):
            if m.group(1) not in heft or m.group(2) > heft[m.group(1)][0]:
                heft[m.group(1)] = (m.group(2), os.path.relpath(d, bank))
    for d in glob.glob(os.path.join(bank, 'bau/pruefheft/fokus-*/*-normal-fokus-*')):
        m = re.match(r'([a-z]+)-normal-fokus-(.+)$', os.path.basename(d))
        dat = re.search(r'fokus-(\d{4}-\d{2}-\d{2})', d)
        if m and dat:
            fokus.setdefault(m.group(1), {})
            alt = fokus[m.group(1)].get(m.group(2))
            if not alt or dat.group(1) > alt:
                fokus[m.group(1)][m.group(2)] = dat.group(1)
    return heft, fokus


def abnahmen():
    p = os.path.join(WURZEL, 'abnahme.csv')
    erg = {}
    if os.path.exists(p):
        for r in lies_csv(p):
            erg[(r['ebene'], r['name'])] = f"{r['urteil']} {r['datum']}"
    return erg


def katalog_status():
    erg = {}
    for z in open(os.path.join(WURZEL, 'katalog/index.md'), encoding='utf-8'):
        if z.startswith('| ') and '.md' in z.split('|')[1]:
            t = [x.strip() for x in z.strip().strip('|').split('|')]
            erg[t[0][:-3]] = t[-1]
    return erg


def bankpruef(bank, eintrag):
    pf = os.path.join(bank, 'werkzeuge/bank-pruef.py')
    try:
        out = subprocess.run([sys.executable, pf, eintrag], capture_output=True,
                             text=True, timeout=120).stdout
    except Exception as e:
        return '–'
    m = re.search(r'^Abweichungen: (\d+), Warnungen: (\d+)', out, re.M)
    return f'{m.group(1)} / {m.group(2)}' if m else '–'


def zeilen(bank, eintrag):
    n = 0
    for p in glob.glob(os.path.join(bank, 'bank', eintrag, '*.jsonl')):
        n += sum(1 for z in open(p, encoding='utf-8') if z.strip())
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bank', default=os.path.join(os.path.dirname(WURZEL), 'aufgabenbank'))
    ap.add_argument('--aus', default=os.path.join(WURZEL, 'tafel.md'))
    a = ap.parse_args()
    sb, ab, kst = steckbriefe(), abnahmen(), katalog_status()
    heft, fokus = hefte(a.bank)
    git = subprocess.run(['git', '-C', a.bank, 'log', '-1', '--format=%h %cs'],
                         capture_output=True, text=True).stdout.strip()

    L = []
    w = L.append
    w('# Fortschrittstafel')
    w('')
    w(f'Gebaut {datetime.date.today().isoformat()} von `werkzeuge/tafel.py` '
      f'(Aufgabenbank {git}). Nie von Hand ändern; Abnahmen in `abnahme.csv`.')
    w('Plan: `plan.md`. Regelstand der Bauregeln: ' + REGELSTAND + '.')
    w('')

    # Kopfzahlen
    alle, eintraege = [], OrderedDict()
    for k, name in KAPITEL.items():
        p = os.path.join(WURZEL, f'msa/zuordnung-{k}.csv')
        for r in lies_csv(p):
            r['_k'] = k
            alle.append(r)
            for s in r.get('bank_sprossen', '').split():
                e = re.match(r'([a-z0-9-]+?)-(e\d+|zone)', s)
                if e:
                    eintraege.setdefault(e.group(1), set()).add(k)
    n_sb = sum(1 for r in alle if r['stufe'] in sb.get(r['_k'], {}))
    n_fehlt = sum(1 for r in alle if (r.get('fehlen') or '0').strip() not in ('', '0'))
    n_ab = sum(1 for r in alle if ('stufe', f"{r['_k']}:{r['stufe']}") in ab)
    akt = sum(1 for k in KAPITEL if k in heft and heft[k][0] >= REGELSTAND)
    w('## Auf einen Blick (P10, Meilenstein M2)')
    w('')
    w('| Maß | Stand |')
    w('|---|---|')
    w(f'| Stufen in den Zuordnungen | {len(alle)} in {len(KAPITEL)} Kapiteln |')
    w(f'| Stufen mit Steckbrief | {n_sb} von {len(alle)} |')
    w(f'| Stufen, denen Bankaufgaben fehlen | {n_fehlt} |')
    w(f'| Kapitel-Hefte gebaut | {len(heft)} von {len(KAPITEL)}, davon auf Regelstand {REGELSTAND}: {akt} |')
    w(f'| Stufen vom Lehrer abgenommen | {n_ab} von {len(alle)} |')
    w('')

    w('## Kapitel')
    w('')
    w('| Kapitel | Stufen (Kern) | mit Steckbrief | Heft gebaut | Fokusblätter | Heft abgenommen |')
    w('|---|---|---|---|---|---|')
    for k, name in KAPITEL.items():
        rs = [r for r in alle if r['_k'] == k]
        kern = sum(1 for r in rs if r.get('kern') == 'ja')
        msb = sum(1 for r in rs if r['stufe'] in sb.get(k, {}))
        h = heft.get(k)
        hs = '–' if not h else (h[0] + ('' if h[0] >= REGELSTAND else ' (alter Regelstand)'))
        fk = ', '.join(f'{f} {d}' for f, d in sorted(fokus.get(k, {}).items())) or '–'
        w(f'| {name} | {len(rs)} ({kern}) | {msb} | {hs} | {fk} | {ab.get(("heft", k), "–")} |')
    w('')

    w('## Stufen')
    w('')
    w('Echt = Prüfungsaufgaben der Stufe; Bank = zugeordnete Bankaufgaben; '
      'fehlen = bis zum Ziel des Zuordnungslaufs (Stand msa/zuordnung-stand.md).')
    w('')
    w('| Kapitel | Stufe | Kern | echt | Bank | Ziel | fehlen | letzte 5 Jahre | Steckbrief | abgenommen |')
    w('|---|---|---|--:|--:|--:|--:|---|---|---|')
    for r in alle:
        k = r['_k']
        w(f"| {KAPITEL[k]} | {r['stufe']} | {r.get('kern') or '–'} | {r.get('anzahl_echt') or '–'} | "
          f"{r.get('anzahl_bank') or '–'} | {r.get('ziel') or '–'} | {r.get('fehlen') or '–'} | "
          f"{(r.get('jahre_letzte5') or '–').split(' ')[0]} | {sb.get(k, {}).get(r['stufe'], '–')} | "
          f"{ab.get(('stufe', k + ':' + r['stufe']), '–')} |")
    w('')

    w('## Bankeinträge, die P10 braucht (Meilenstein M4)')
    w('')
    w('Status = Spalte im Katalog-Index; Prüfung = bank-pruef.py Abweichungen / Warnungen; '
      'Vollständigkeit bestätigt = Abnahme „katalog“ in abnahme.csv.')
    w('')
    w('| Eintrag | gebraucht von | Katalog-Status | Zeilen | Prüfung | Vollständigkeit bestätigt |')
    w('|---|---|---|--:|---|---|')
    for e in sorted(eintraege):
        w(f"| {e} | {', '.join(KAPITEL[k] for k in KAPITEL if k in eintraege[e])} | "
          f"{kst.get(e, '–')} | {zeilen(a.bank, e)} | {bankpruef(a.bank, e)} | "
          f"{ab.get(('katalog', e), '–')} |")
    w('')

    p = os.path.join(WURZEL, 'abitur/skript-zuschnitt-abi-gk.csv')
    if os.path.exists(p):
        rs = lies_csv(p)
        ka = [c for c in rs[0] if 'abschnitt' in c.lower()]
        n = len(set(r[ka[0]] for r in rs)) if ka else len(rs)
        w('## Abitur Grundkurs (Meilenstein M5)')
        w('')
        w(f'Zuschnitt (Entwurf): {n} Abschnitte in `abitur/skript-zuschnitt-abi-gk.csv`; '
          'Zuordnungen und Steckbriefe noch keine.')
        w('')

    open(a.aus, 'w', encoding='utf-8').write('\n'.join(L))
    print(f'geschrieben: {a.aus} ({len(alle)} Stufen, {len(eintraege)} Bankeinträge)')


if __name__ == '__main__':
    main()
