#!/usr/bin/env python3
r"""testlauf-messen.py – Kennzahlen eines Testlaufs des Unterrichtsblatt-Prompts (v0.1, 25.09.2026)

Auftrag: archiv/auftrag-testlauf-<datum>.md, Teil 3. Baut
blaetter/testlauf-<datum>/kennzahlen.md in zwei Teilen:
  1. die Ausgabe von werkzeuge/blatt-pruef.py --testlauf <ordner> --ausgabe <datei>
     (Gesamt- und Fokus-PDFs aller Eingaben; blaetter/kennzahlen.md bleibt unberührt),
  2. die Zusatzzählung aus der Textextraktion (pdftotext -layout) je Gesamt-/Fokus-PDF
     und die drei Gegenproben des Auftrags.

Aufruf (aus der Repo-Wurzel oder beliebig):
  python werkzeuge/testlauf-messen.py blaetter/testlauf-<datum> [--probe]
--probe gibt Teil 2 auf der Konsole aus und schreibt nichts.

Lesarten der Zusatzzählung (je Seite des pdftotext-Texts, Seitentrennung Seitenvorschub):
 Abhakseite   die erste Seite ab 2 mit einer Zeile, die mit „Das kann ich“ beginnt, und alle
              Seiten danach (die Abhakseite ist nach unterrichtsblatt.md 4.1 der Schluss und
              kann zwei Seiten lang sein). Diese Seiten zählen für Köpfe, Zweigzeilen und
              Hauptnummern nicht mit (sie wiederholen die Titel).
 Einheitenkopf  Zeile mit „Einheit <n> von <m>“ (davor ggf. „Ausblick“).
 Zweigzeile   Zeile mit „Hier lernst du“, oder – wenn keine solche folgt – die erste
              nichtleere Zeile nach einem Einheitenkopf mit mindestens zwei „·“. Der Text der
              Zweigzeile reicht bis zur nächsten Leerzeile, Hauptnummer oder zum nächsten Kopf.
 Hauptnummer  Zeile „<n>. <Text>“ oder „Z<n>. <Text>“ (Zone mit eigener Zählung) mit
              höchstens sechs Leerzeichen Einzug, deren Nummer die vorige derselben Zählung um
              eins fortsetzt oder 1 ist (Zone und Blatt dürfen neu zählen). Titel =
              Text bis zum ersten Satzende. Ich-Titel = Titel beginnt mit „Ich kann“,
              „Ich erkenne“ oder „Ich finde“.
 Blatt 0      jedes Vorkommen von „Blatt 0“ (auch „Blatt0“) im ganzen PDF-Text.
"""

import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import importlib.util
_spec = importlib.util.spec_from_file_location('blatt_pruef', Path(__file__).parent / 'blatt-pruef.py')
BP = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(BP)

KOPF = re.compile(r'(Ausblick\s*)?Einheit\s+(\d+)\s+von\s+(\d+)\s*·?\s*(.*)')
HN = re.compile(r'^\s{0,6}(Z?)(\d{1,3})\.\s+(\S.*)$')
ICH = ('Ich kann', 'Ich erkenne', 'Ich finde')


def satz(text):
    m = re.search(r'[.?!](?=\s|$)', text)
    return (text[:m.end()] if m else text).strip()


def zerlege_text(seiten):
    erste = next((i for i, s in enumerate(seiten)
                  if i > 0 and re.search(r'(?m)^\s*Das kann ich\b', s)), None)
    abhak = list(range(erste, len(seiten))) if erste is not None else []
    koepfe, zweig, hns = [], [], []
    letzte = {}
    for i, s in enumerate(seiten):
        if i in abhak:
            continue
        zeilen = s.split('\n')
        j = 0
        while j < len(zeilen):
            z = zeilen[j]
            m = KOPF.search(z)
            if m and not re.search(r'Seiten?\s+\d', z):
                kopf = {'seite': i + 1, 'ausblick': bool(m.group(1)), 'nr': int(m.group(2)),
                        'von': int(m.group(3)), 'titel': m.group(4).strip(), 'zweig': None}
                koepfe.append(kopf)
                # Zweigzeile suchen: nächste nichtleere Zeilen
                k = j + 1
                while k < len(zeilen) and not zeilen[k].strip():
                    k += 1
                if k < len(zeilen):
                    erste = zeilen[k]
                    if 'Hier lernst du' in erste or erste.count('·') >= 2:
                        teile = [erste.strip()]
                        k2 = k + 1
                        while (k2 < len(zeilen) and zeilen[k2].strip() and not HN.match(zeilen[k2])
                               and not KOPF.search(zeilen[k2])):
                            teile.append(zeilen[k2].strip())
                            k2 += 1
                        kopf['zweig'] = ' '.join(teile)
                        zweig.append((i + 1, kopf['zweig']))
                        j = k2
                        continue
                j += 1
                continue
            if 'Hier lernst du' in z and not any(z.strip() in t for _, t in zweig):
                teile = [z.strip()]
                k2 = j + 1
                while k2 < len(zeilen) and zeilen[k2].strip() and not HN.match(zeilen[k2]):
                    teile.append(zeilen[k2].strip())
                    k2 += 1
                zweig.append((i + 1, ' '.join(teile)))
                j = k2
                continue
            m = HN.match(z)
            if m:
                vor, n = m.group(1), int(m.group(2))
                if n == letzte.get(vor, 0) + 1 or n == 1:
                    hns.append({'nr': f'{vor}{n}', 'seite': i + 1, 'titel': satz(m.group(3).strip())})
                    letzte[vor] = n
            j += 1
    return abhak, koepfe, zweig, hns


def blatt0(text):
    return len(re.findall(r'Blatt\s?0\b', text))


def messe(pdf):
    seiten = BP.pdf_text(pdf)
    abhak, koepfe, zweig, hns = zerlege_text(seiten)
    ich = [h for h in hns if h['titel'].startswith(ICH)]
    return {'pdf': pdf, 'seiten': len(seiten), 'abhak': [a + 1 for a in abhak], 'koepfe': koepfe,
            'zweig': zweig, 'hns': hns, 'ich': ich, 'blatt0': blatt0('\n'.join(seiten))}


def zeitmarke(kopf):
    """(Zeitmarke, Prüfungswort) aus der Zweigzeile: die zwei Teile vor „baut auf:“ (Trenner „ · “;
    Malpunkte in Formeln stören nicht, weil von hinten gezählt wird)."""
    if not kopf or not kopf.get('zweig'):
        return ('?', '?')
    teile = [t.strip() for t in kopf['zweig'].split(' · ')]
    idx = next((i for i, t in enumerate(teile) if t.startswith('baut auf')), len(teile))
    if idx < 3:
        return ('?', '?')
    return (teile[idx - 2], teile[idx - 1])


def zeile_md(text):
    return text.replace('|', '/')


def gegenproben(ordner, mess):
    z = ['## Gegenproben (Teil 3.3)', '']

    def blatt(prefix):
        for (o, pdf), m in mess.items():
            if o.name.startswith(prefix) and 'gesamt' in pdf.name.lower():
                return m
        for (o, pdf), m in mess.items():
            if o.name.startswith(prefix):
                return m
        return None

    # 1: Eingabe 1 und 2
    m1, m2 = blatt('1-'), blatt('2-')
    z.append('1. Eingabe 1 und 2 – dieselben Zweige, verschiedene Zeitmarken (Marken-Zeile '
             'quadratische-gleichungen Einheit 2 „Satz vom Nullprodukt“: OS Kl. 10, GYM Kl. 8–9). '
             'Verglichen nach Zweigtitel, weil die Stelle des Zweigs mit der Bestellung wechseln darf.')
    z.append('')
    if m1 and m2:
        t1 = {k['titel']: k for k in m1['koepfe']}
        t2 = {k['titel']: k for k in m2['koepfe']}
        z.append(f"   - Zweige (nach Titel) Eingabe 1: {len(t1)}; Eingabe 2: {len(t2)}; "
                 f"dieselben Zweige: {'ja' if set(t1) == set(t2) else 'nein'}"
                 + (f" (nur in 1: {', '.join(sorted(set(t1) - set(t2))) or '–'}; "
                    f"nur in 2: {', '.join(sorted(set(t2) - set(t1))) or '–'})" if set(t1) != set(t2) else '')
                 + '.')
        z.append('')
        z.append('   | Zweig | Eingabe 1: Stelle · Zeitmarke · Prüfungswort | Eingabe 2: Stelle · Zeitmarke · Prüfungswort | Zeitmarke verschieden |')
        z.append('   |---|---|---|---|')
        for titel in [k['titel'] for k in m2['koepfe']] + [t for t in t1 if t not in t2]:
            a, b = t1.get(titel), t2.get(titel)
            za, zb = zeitmarke(a), zeitmarke(b)

            def zelle(k, zm):
                if not k:
                    return '–'
                stelle = f"{'Ausblick ' if k['ausblick'] else ''}E{k['nr']}"
                return f"{stelle} · {zeile_md(zm[0])} · {zeile_md(zm[1])}"
            z.append(f"   | {zeile_md(titel)} | {zelle(a, za)} | {zelle(b, zb)} | "
                     f"{('ja' if za[0] != zb[0] else 'nein') if a and b else '–'} |")
    else:
        z.append('   - nicht messbar: ' + ', '.join(n for n, m in (('Eingabe 1', m1), ('Eingabe 2', m2)) if not m)
                 + ' ohne Gesamt-PDF.')
    z.append('')

    # 2: Eingabe 8
    m8 = blatt('8-')
    z.append('2. Eingabe 8 – ein Zweig mit „Potenzfunktion“ und dem Prüfungswort „keine P10-Aufgabe“.')
    z.append('')
    if m8:
        treffer = [k for k in m8['koepfe']
                   if 'Potenzfunktion' in (k['titel'] + ' ' + (k['zweig'] or ''))]
        if not treffer:
            z.append('   - kein Einheitenkopf und keine Zweigzeile mit „Potenzfunktion“.')
        for k in treffer:
            z.append(f"   - {'Ausblick ' if k['ausblick'] else ''}Einheit {k['nr']} von {k['von']} · "
                     f"{zeile_md(k['titel'])}: „keine P10-Aufgabe“ in der Zweigzeile: "
                     f"{'ja' if k['zweig'] and 'keine P10-Aufgabe' in k['zweig'] else 'nein'} – "
                     f"„{zeile_md(k['zweig'] or '– keine –')}“")
    else:
        z.append('   - nicht messbar: Eingabe 8 ohne Gesamt-PDF.')
    z.append('')

    # 3: Eingabe 4
    o4 = next((o for o in sorted(ordner.iterdir()) if o.is_dir() and o.name.startswith('4-')), None)
    z.append('3. Eingabe 4 – kein PDF „KennstDuSchon“.')
    z.append('')
    if o4:
        kds = sorted(p.name for p in o4.rglob('*.pdf') if 'kennstduschon' in p.name.lower())
        z.append(f"   - PDFs im Ordner: {', '.join(sorted(p.name for p in o4.glob('*.pdf'))) or '–'}; "
                 f"„KennstDuSchon“: {', '.join(kds) if kds else 'keins'}.")
    else:
        z.append('   - Ordner der Eingabe 4 fehlt.')
    z.append('')
    return z


def zusatz(ordner):
    tripel = BP.testlauf_blaetter(ordner)
    mess = {}
    for pdf, o, _ in tripel:
        mess[(o, pdf)] = messe(pdf)
    z = ['', '# Zusatzzählung aus der Textextraktion (werkzeuge/testlauf-messen.py)', '',
         'Lesarten im Kopf von `werkzeuge/testlauf-messen.py`. „Hauptnummern (tex)“ ist die Zahl aus '
         'Teil 1 (Quelltext), „Hauptnummern (Text)“ die aus der Textextraktion.', '',
         '| Eingabe | Datei | Seiten | Einheitenköpfe | Zweigzeilen | Hauptnummern (Text) | '
         'Hauptnummern (tex) | Ich-Titel | Seite „Das kann ich“ | „Blatt 0“ |',
         '|---|---|---|---|---|---|---|---|---|---|']
    for pdf, o, t in tripel:
        m = mess[(o, pdf)]
        k = BP.messe(pdf, o, None, t)
        hn_tex = len(k.get('hauptnummern', [])) if not k.get('fehlt_tex') else '–'
        z.append(f"| {o.name} | {pdf.name} | {m['seiten']} | {len(m['koepfe'])} | {len(m['zweig'])} | "
                 f"{len(m['hns'])} | {hn_tex} | {len(m['ich'])} von {len(m['hns'])} | "
                 f"{('ja, S. ' + ', '.join(map(str, m['abhak']))) if m['abhak'] else 'nein'} | {m['blatt0']} |")
    z += ['', '## Je Blatt: Köpfe, Zweigzeilen, Titel ohne Ich-Form', '']
    for pdf, o, _ in tripel:
        m = mess[(o, pdf)]
        z.append(f'### {o.name} · {pdf.name}')
        z.append('')
        if m['koepfe']:
            for k in m['koepfe']:
                z.append(f"- S. {k['seite']} {'Ausblick ' if k['ausblick'] else ''}Einheit {k['nr']} von {k['von']}"
                         f" · {zeile_md(k['titel'])} – Zweigzeile: "
                         f"{('„' + zeile_md(k['zweig']) + '“') if k['zweig'] else 'fehlt'}")
        else:
            z.append('- kein Einheitenkopf „Einheit n von m“ gefunden.')
        lose = [t for s, t in m['zweig'] if not any(k['zweig'] == t for k in m['koepfe'])]
        for t in lose:
            z.append(f'- Zweigzeile ohne erkannten Kopf: „{zeile_md(t)}“')
        ohne = [h for h in m['hns'] if not h['titel'].startswith(ICH)]
        if ohne:
            z.append('- Titel ohne Ich-Form: ' + '; '.join(f"Nr. {h['nr']} (S. {h['seite']}) „{zeile_md(h['titel'])}“"
                                                         for h in ohne))
        else:
            z.append('- Titel ohne Ich-Form: keiner.')
        if m['blatt0']:
            z.append(f"- „Blatt 0“ kommt {m['blatt0']}-mal vor.")
        z.append('')
    z += gegenproben(ordner, mess)
    return '\n'.join(z).rstrip('\n') + '\n'


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    probe = '--probe' in sys.argv
    if not args:
        sys.exit(__doc__)
    ordner = Path(args[0]).resolve()
    teil2 = zusatz(ordner)
    if probe:
        print(teil2)
        return
    ziel = ordner / 'kennzahlen.md'
    subprocess.run([sys.executable, str(Path(__file__).parent / 'blatt-pruef.py'),
                    '--testlauf', str(ordner), '--ausgabe', str(ziel)], check=True)
    text = ziel.read_text(encoding='utf-8')
    with open(ziel, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text.rstrip('\n') + '\n' + teil2)
    print(f'{ziel} geschrieben (blatt-pruef.py + Zusatzzählung).')


if __name__ == '__main__':
    main()
