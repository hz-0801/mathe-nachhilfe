#!/usr/bin/env python3
"""gliederung-extrakt.py – einmaliger Lauf (08.10.2026, Entscheidung A): zieht die Stufendaten aus
werkzeuge/zuordnung.py (Stand vor v2, Daten im Skript), den Zuschnitt-CSVs, msa/handgriffe-p10.csv und den
Steckbriefen katalog/steckbrief/*.md heraus und schreibt je Kapitel eine Gliederungsdatei
(msa/gliederung/<kapitel>.md, abitur/gliederung/<kapitel>.md; Format msa/gliederung/README.md).

Aufruf aus der Repo-Wurzel, mit der alten zuordnung.py als Argument (git show a1c9fd3:werkzeuge/zuordnung.py):
    python3 werkzeuge/gliederung-extrakt.py /pfad/zur/alten/zuordnung.py
Bleibt im Repo als Beleg, wie die Dateien entstanden sind; ein zweiter Lauf überschreibt sie.
"""
import collections
import csv
import importlib.util
import os
import re
import sys

MN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(MN, 'werkzeuge'))
import gliederung as GL

alt = sys.argv[1]
spec = importlib.util.spec_from_file_location('zalt', alt)
Z = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Z)

KN = {'Dreiecke': 'dreiecke', 'Flächen': 'flaechen', 'Körper': 'koerper', 'Lineare': 'lineare',
      'Quadratische': 'quadratische', 'Gleichungssysteme': 'gleichungssysteme', 'Wachstum': 'wachstum',
      'Prozent': 'prozent', 'Daten': 'daten', 'Wahrscheinlichk.': 'wahrscheinlichkeit',
      'Kurvenuntersuchung': 'kurvenuntersuchung', 'Ableitung + Tangente': 'ableitung-tangente',
      'Integral': 'integral', 'Punkte, Flächen, Körper': 'punkte-flaechen-koerper',
      'Winkel + Abstände': 'winkel-abstaende', 'Geraden + Ebenen': 'geraden-ebenen',
      'Baumdiagramm + bedingte Wahrscheinlichkeit': 'baum-bedingte-wahrscheinlichkeit',
      'Binomialverteilung': 'binomialverteilung', 'Erwartungswert': 'erwartungswert'}
# Zuschnitt-Zeilen, deren Name nicht die Stufe ist (Arten des Steckbriefs Pythagoras, 07.10.)
ZEILE_ZU_STUFE = {('dreiecke', 'Hypotenuse gesucht'): 'Kathete oder Hypotenuse direkt',
                  ('dreiecke', 'Kathete gesucht'): 'Kathete oder Hypotenuse direkt',
                  ('dreiecke', 'Dreieck versteckt'): 'Dreieck erst in Figur oder Körper finden',
                  ('dreiecke', 'Seite im allgemeinen Dreieck (Sinussatz)/Seite berechnen'): 'Seite berechnen (Sinussatz)'}
TITEL = {'msa': 'P10', 'abitur': 'Abitur GK'}


def zuschnitt(pfad):
    rows = list(csv.DictReader(open(pfad, encoding='utf-8'), delimiter=';'))
    je = collections.OrderedDict()
    for r in rows:
        je.setdefault(r['kapitel'], []).append(r)
    return je


def stufen_block(kap, K, zrows, pruefung):
    out = []
    zrows = list(zrows)
    # Zeilen den Stufen zuordnen
    je_stufe = collections.OrderedDict((n, []) for n, _, _ in K['stufen'])
    for r in zrows:
        n = r['stufe']
        key = ZEILE_ZU_STUFE.get((kap, r['abschnitt'] + '/' + n)) or ZEILE_ZU_STUFE.get((kap, n))
        if key is None:
            if pruefung == 'abitur':
                key = r['abschnitt']
            elif n in je_stufe and not je_stufe[n]:
                key = n
            else:
                sys.exit(f'{kap}: Zuschnitt-Zeile {r["abschnitt"]}/{n} ohne Stufe')
        je_stufe[key].append(r)
    for name, echt, maps in K['stufen']:
        k, g = K['kern'][name]
        out.append(f'### {name}')
        out.append(f'- **Kern:** {k} – {g}')
        rows = je_stufe[name]
        abschnitt = rows[0]['abschnitt'] if rows else ''
        maps4 = [(m[0], m[1], m[2], 'inner' if len(m) > 3 and m[3] == 'inner' else '') for m in maps]
        explizit = pruefung == 'abitur' or not rows or len(rows) != 1 or rows[0]['stufe'] != name or \
            rows[0]['neben'] or rows[0]['ids'].split() != [i for i in echt if i[:4] >= '2022' and '-EBR-' not in i]
        if pruefung == 'abitur':
            # Originale = ids der Zuschnitt-Zeilen (wie _zuschnitt_ids); Kontrolle
            ids = []
            for r in rows:
                ids += [i for i in r['ids'].split() if i not in ids]
            assert ids == echt, (kap, name, ids, echt)
        else:
            out.append(f'- **Originale:** {" ".join(echt)}')
        out.append(f'- **Bank:** {GL.muster_text(maps4) or "–"}')
        verw = Z.VERWECHSELBAR.get((kap, name), [])
        if verw:
            out.append('- **Verwechselbar:** ' + ' | '.join(f'{kk}:{s}' if kk != kap else s for kk, s in verw))
        if abschnitt:
            out.append(f'- **Zuschnitt:** {abschnitt}')
            if explizit:
                for r in rows:
                    assert r['abschnitt'] == abschnitt, (kap, name)
                    z = f'  - {r["stufe"]} [{r["ids"]}]'
                    if r['neben']:
                        z += f' neben [{r["neben"]}]'
                    out.append(z)
        out.append('')
    return out


def plaetze_block(kap, H):
    out = ['## Plätze der Originale', '',
           'Jede Teilaufgabe 2014–2026 (OS, EBR, FOR, GYM) mit ihrem Hauptplatz (Stufe, deren Handgriff die',
           'ganze Teilaufgabe ist), „ganz auch“ (die ganze Aufgabe ist dieser Handgriff, obwohl anders',
           'etikettiert) und Zwischenschritt; Stufen anderer Kapitel mit „kapitel:“. Erzeugt daraus:',
           'msa/handgriffe-p10.csv (werkzeuge/gliederung-sichten.py).', '',
           '| id | Hauptplatz | Ganz auch | Zwischenschritt | Begründung |', '|---|---|---|---|---|']
    def kurz(refs):
        return '; '.join(x[len(kap) + 1:] if x.startswith(kap + ':') else x for x in refs)
    for d in H:
        out.append(f'| {d["id"]} | {kurz(d["hauptplatz"])} | {kurz(d["ganz_auch"])} | {kurz(d["zwischenschritt"])} '
                   f'| {d["begruendung"].replace("|", chr(92) + "|")} |')
    out.append('')
    return out


def fokus_block(pfad, name):
    """Steckbrief -> Fokus-Block: Überschriften eine Ebene tiefer, Titel als Kopfzeile, Teil 1 „Typische
    Fehler“ und „Leiter“ als Verweis auf den Katalog (W2: Fehler stehen nur im Katalog)."""
    txt = open(pfad, encoding='utf-8').read()
    out = [f'## Fokus {name}', '']
    zl = txt.splitlines()
    titel = zl[0][2:].strip()
    out.append(f'Titel: {titel}')
    zl = zl[1:]
    # Typische Fehler -> Verweis (Auswahl nach Anfang des Katalog-Satzes), Leiter -> Verweis
    katalog = {'grundwert': ('katalog/prozentrechnung.md', 'Einheit 4',
                             ['Grundwert gesucht', 'Grundwert und Prozentwert vertauscht', 'Falsches Ganzes', '„um“ und „auf“ verwechselt']),
               'pythagoras-seite': ('katalog/pythagoras.md', 'Einheiten 1–3',
                                    ['Quadrate addiert', 'Falsche Seite als Hypotenuse', 'Wurzel vergessen', 'Satz als Längenformel',
                                     'Wurzel aus jedem Summanden', 'Ganze statt halbe Seite', 'Radius und Durchmesser', 'Schräge als Höhe',
                                     'Buchstabenfixierung'])}[name]
    res, i = [], 0
    while i < len(zl):
        z = zl[i]
        if re.match(r'- \*\*Typische Fehler:\*\*', z):
            res.append(f'- **Typische Fehler:** → {katalog[0]}, Typische Fehler: ' + ' | '.join(katalog[2]))
            i += 1
            while i < len(zl) and (zl[i].startswith('  ') or not zl[i].strip()) and not re.match(r'- \*\*', zl[i]):
                if not zl[i].strip():
                    break
                i += 1
            continue
        if re.match(r'- \*\*Leiter( \(.*\))?:\*\*', z):
            res.append(f'- **Leiter:** → {katalog[0]}, Lerneinheiten und Merkkasten {katalog[1]} (Sprossen in der Bank)')
            i += 1
            while i < len(zl) and zl[i].startswith('  '):
                i += 1
            continue
        res.append(z)
        i += 1
    for z in res:
        if z.startswith('#### '):
            z = '#' + z
        elif z.startswith('### '):
            z = '#' + z
        elif z.startswith('## '):
            z = '#' + z
        out.append(z)
    out.append('')
    return out


def schreibe(pruefung, kap, K, zrows, gebiet, name, folge, H, fokus):
    ordner = os.path.join(MN, pruefung, 'gliederung')
    os.makedirs(ordner, exist_ok=True)
    eintraege = K.get('eintraege', [])
    out = [f'# Gliederung {name} ({TITEL[pruefung]})', '',
           f'Prüfung: {pruefung}', f'Kapitel: {kap}', f'Gebiet: {gebiet}', f'Name: {name}', f'Folge: {folge}']
    if eintraege:
        out.append('Bank: ' + ' | '.join(eintraege))
        kat = [f'katalog/{e}.md' for e in eintraege if os.path.exists(os.path.join(MN, 'katalog', e + '.md'))]
        if kat:
            out.append('Katalog: ' + ' | '.join(kat))
    else:
        out.append('Skript: nein')
    out += ['',
            'Prüfungsgliederung (Entscheidung A, plan.md 08.10.2026): Kapitel → Stufe → Bankaufgaben, Originale,',
            'didaktische Felder. Erzeugt daraus: zuordnung-<kapitel>.csv (werkzeuge/zuordnung.py), die',
            'Zuschnitt-CSV und handgriffe-p10.csv (werkzeuge/gliederung-sichten.py). Stand der Daten: zuordnung.py',
            'und Zuschnitt vom 08.10.2026, Steckbriefe vom 07.10.2026.', '',
            '## Stufen', '']
    out += stufen_block(kap, K, zrows, pruefung)
    if H:
        out += plaetze_block(kap, H)
    for n, p in fokus:
        out += fokus_block(p, n)
    txt = '\n'.join(out).rstrip('\n') + '\n'
    open(os.path.join(ordner, kap + '.md'), 'w', encoding='utf-8', newline='\n').write(txt)


def basis(pruefung, kap, rows, gebiet, folge, titel):
    ordner = os.path.join(MN, pruefung, 'gliederung')
    out = [f'# Gliederung {titel} ({TITEL[pruefung]})', '', f'Prüfung: {pruefung}', f'Kapitel: {kap}',
           f'Gebiet: {gebiet}', 'Name: –', f'Folge: {folge}', 'Skript: nein', '',
           'Teilaufgaben ohne Skript-Kapitel (nur Zuschnitt). Keine Bank, keine Zuordnung.', '', '## Stufen', '']
    for r in rows:
        out += [f'### {r["abschnitt"]}: {r["stufe"]}', f'- **Zuschnitt:** {r["abschnitt"]}',
                f'  - {r["stufe"]} [{r["ids"]}]' + (f' neben [{r["neben"]}]' if r['neben'] else ''), '']
    open(os.path.join(ordner, kap + '.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out).rstrip('\n') + '\n')


def main():
    H = Z.lade_handgriffe()
    je_kap = collections.defaultdict(list)
    for d in H:
        ref = (d['hauptplatz'] or d['ganz_auch'] or d['zwischenschritt'])[0]
        je_kap[ref.split(':')[0]].append(d)
    sbs = {'prozent': [('grundwert', os.path.join(MN, 'katalog', 'steckbrief', 'prozent-grundwert.md'))],
           'dreiecke': [('pythagoras-seite', os.path.join(MN, 'katalog', 'steckbrief', 'pythagoras-seite.md'))]}
    for pruefung, datei in (('msa', 'msa/skript-zuschnitt-p10.csv'), ('abitur', 'abitur/skript-zuschnitt-abi-gk.csv')):
        je = zuschnitt(os.path.join(MN, datei))
        for folge, (kname, rows) in enumerate(je.items(), 1):
            kap = KN.get(kname)
            if kap is None:
                basis(pruefung, '_basisteil' if pruefung == 'msa' else '_hilfsmittelfrei', rows, rows[0]['gebiet'],
                      folge, 'Basisteil' if pruefung == 'msa' else 'Hilfsmittelfrei ohne Kapitel')
                continue
            K = Z.KAPITEL[kap]
            assert K.get('pruefung', 'msa') == pruefung
            schreibe(pruefung, kap, K, rows, rows[0]['gebiet'], kname, folge,
                     je_kap.get(kap, []) if pruefung == 'msa' else [], sbs.get(kap, []))
            print(pruefung, kap, len(K['stufen']), 'Stufen,', len(rows), 'Zuschnitt-Zeilen,', len(je_kap.get(kap, [])), 'Plätze')


if __name__ == '__main__':
    main()
