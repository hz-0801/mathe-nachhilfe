"""Zuschnitt aus Steckbriefen (Beschluss A4, 07.10.2026): erzeugt bzw. ersetzt
in msa/skript-zuschnitt-p10.csv die Zeilen der Handgriffe, die einen
Steckbrief mit Teil 5 „Arten“ haben (katalog/steckbrief/*.md, Format in
katalog/steckbrief/README.md). Übrige Zeilen bleiben byteidentisch.

Regeln:
- Ersetzt werden die Zeilen, deren stufe in der Kopfzeile „Stufen:“ des
  Steckbriefs oder im Feld „Zuschnitt“ einer Art steht (ein zweiter Lauf
  ändert nichts) und deren abschnitt zum Kapitel des Steckbriefs gehört
  (der Abschnitt der ersten solchen Zeile; gebiet, kapitel, abschnitt
  werden übernommen). Sie werden an der Stelle der ersten ersetzten Zeile
  eingefügt, eine Zeile je Art, Reihenfolge der Arten im Steckbrief.
- stufe = Feld „Zuschnitt“ der Art.
- ids = Aufgaben der Art aus der Grundlage des Zuschnitts (P10 2022–2026,
  ohne EBR, wie werkzeuge/skript-zuschnitt.py), deren bisheriger
  Hauptplatz in einer ersetzten Zeile lag; liegt der Hauptplatz anderswo
  (anderer Abschnitt), steht die Aufgabe unter neben.
- Bisherige Nebenplätze der ersetzten Zeilen bleiben Nebenplätze, wenn
  die Aufgabe in keiner Art steht (Befund).
- Jede bisherige Hauptplatz-Aufgabe der ersetzten Zeilen muss in genau
  einer Art stehen, sonst wird nichts geschrieben.

Aufruf aus der Repo-Wurzel: python3 werkzeuge/zuschnitt-aus-steckbrief.py
Danach: python3 werkzeuge/skript-zuschnitt.py (prüft und baut die .md).
Gegenprobe (im Skript): alle Zeilen ohne Steckbrief byteidentisch.
"""
import csv, glob, io, os, re, sys

ZU = 'msa/skript-zuschnitt-p10.csv'
KAT = ['msa/msa-katalog-basis.csv', 'msa/msa-katalog-kontext.csv']


def arten(pfad):
    """Kopf (Stufen) und Arten (Zuschnitt, Aufgaben) eines Steckbriefs; [] ohne Teil 5."""
    txt = open(pfad, encoding='utf-8').read()
    m = re.search(r'^Stufen:\s*(.*)$', txt, re.M)
    stufen = [s.strip() for s in (m.group(1) if m else '').split('|') if s.strip()]
    m = re.search(r'^## 5 Arten\s*$', txt, re.M)
    if not m:
        return stufen, []
    out = []
    for block in re.split(r'^### ', txt[m.end():], flags=re.M)[1:]:
        name = block.splitlines()[0].strip()
        felder = {}
        key = None
        for z in block.splitlines()[1:]:
            mm = re.match(r'- \*\*(.+?):\*\*\s*(.*)$', z)
            if mm:
                key = mm.group(1)
                felder[key] = mm.group(2).strip()
            elif key and re.match(r'\s{2,}\S', z):
                felder[key] += ' ' + z.strip()
        out.append((name, felder.get('Zuschnitt', name),
                    re.findall(r'\d{4}-[A-Z]+-[A-Z]\d+[a-z]', felder.get('Aufgaben', ''))))
    return stufen, out


def main():
    roh = open(ZU, encoding='utf-8').read()
    zeilen = roh.splitlines()
    kopf, daten = zeilen[0], zeilen[1:]
    rows = [dict(zip(kopf.split(';'), z.split(';'))) for z in daten]
    grund = set()
    for f in KAT:
        for x in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
            if x['jahr'] >= '2022' and x['papier'] != 'EBR':
                grund.add(x['id'])
    haupt = {i: k for k, r in enumerate(rows) for i in r['ids'].split()}
    ersetzt = {}   # Zeilenindex -> neue Zeilen (nur am ersten Index), sonst []
    befunde = []
    for sb in sorted(glob.glob('katalog/steckbrief/*.md')):
        if os.path.basename(sb).lower().startswith('readme'):
            continue
        stufen, ar = arten(sb)
        if not ar:
            continue
        namen = set(stufen) | {st for _, st, _ in ar}   # auch schon erzeugte Zeilen (zweiter Lauf gleich)
        idx = [k for k, r in enumerate(rows) if r['stufe'] in namen]
        if not idx:
            befunde.append(f'{sb}: keine Zuschnittzeile mit den Stufen {stufen}')
            continue
        ab = rows[idx[0]]['abschnitt']
        idx = [k for k in idx if rows[k]['abschnitt'] == ab]
        alt_haupt = [i for k in idx for i in rows[k]['ids'].split()]
        alt_neben = [i for k in idx for i in rows[k]['neben'].split()]
        neu, gesehen = [], set()
        for name, st, ids in ar:
            h = [i for i in ids if i in grund and haupt.get(i) in idx]
            n = [i for i in ids if i in grund and i in haupt and haupt[i] not in idx]
            gesehen |= set(h)
            neu.append((st, h, n))
        fehlt = [i for i in alt_haupt if i not in gesehen]
        if fehlt:
            sys.exit(f'{sb}: Hauptplätze ohne Art: {fehlt} – nichts geschrieben')
        rest_neben = [i for i in alt_neben if not any(i in n for _, _, n in neu)]
        if rest_neben:
            befunde.append(f'{sb}: Nebenplätze ohne Art bleiben bei der ersten Art: {rest_neben}')
            neu[0] = (neu[0][0], neu[0][1], neu[0][2] + rest_neben)
        r0 = rows[idx[0]]
        ersetzt[idx[0]] = [';'.join([r0['gebiet'], r0['kapitel'], r0['abschnitt'], st, ' '.join(h), ' '.join(n)])
                           for st, h, n in neu]
        for k in idx[1:]:
            ersetzt[k] = []
        print(f'{sb}: {len(idx)} Zeilen ersetzt durch {len(neu)} ({", ".join(s for s, _, _ in neu)})')
    out = [kopf]
    for k, z in enumerate(daten):
        out += ersetzt.get(k, [z]) if k in ersetzt else [z]
    # Gegenprobe: Zeilen ohne Steckbrief byteidentisch und in derselben Folge
    alt_rest = [z for k, z in enumerate(daten) if k not in ersetzt]
    neu_set = {z for v in ersetzt.values() for z in v}
    neu_rest = [z for z in out[1:] if z not in neu_set]
    if alt_rest != neu_rest:
        sys.exit('Gegenprobe: Zeilen ohne Steckbrief verändert – nichts geschrieben')
    txt = '\n'.join(out) + ('\n' if roh.endswith('\n') else '')
    open(ZU, 'w', encoding='utf-8', newline='\n').write(txt)
    print(f'Gegenprobe: {len(alt_rest)} Zeilen ohne Steckbrief byteidentisch')
    for b in befunde:
        print('Befund:', b)


if __name__ == '__main__':
    main()
