"""Daten für die Lernreihenfolge der P10-Handreichung (v0.1, 03.10.2026).

Liest msa/msa-katalog-basis.csv, msa/msa-katalog-kontext.csv und die
Katalogeinträge (Abschnitt „Voraussetzungen (Blatt 0)“) und schreibt
msa/handreichung-reihenfolge.md: je Thema der Handreichung Punkteanteil
2020–2026, Jahre (nur Jahre, in denen das Thema geprüft werden durfte),
Anteil leichter Punkte (Niveau I), Anteil in der Basis und die
Voraussetzungen unter den Themen der Liste.

Zählregeln: 2026 nur das FOR-Heft (EBR und FOR sind getrennte Hefte;
sonst zählte 2026 doppelt). Ausschlüsse nach msa/msa-vorgaben.md § 2:
2021 Exponentialfunktionen und Wahrscheinlichkeit, 2022 und 2023
Exponentialfunktionen, Wahrscheinlichkeit (Niveau E), Sinus-/Kosinussatz.
Abgeleitet, nie von Hand ändern. Aufruf aus der Wurzel:
python werkzeuge/handreichung-reihenfolge.py
"""
import csv, os, re, collections

W = os.path.join(os.path.dirname(__file__), '..')
JAHRE = [str(j) for j in range(2020, 2027)]

# Thema der Handreichung -> (msa-Themen, Katalogeinträge, ausgeschlossene Jahre)
THEMEN = {
    'Prozentrechnung': (['Prozentrechnung'], ['prozentrechnung', 'zinsrechnung'], []),
    'Mittelwert, Median, Spannweite': (['Kenngrößen'], ['daten'], []),
    'Lineare Funktionen': (['Lineare Funktionen'], ['lineare-funktionen'], []),
    'Quadratische Funktionen': (['Quadratische Funktionen'], ['quadratische-funktionen'], []),
    'Satz des Pythagoras': (['Satz des Pythagoras'], ['pythagoras'], []),
    'Trigonometrie': (['Trigonometrie im rechtwinkligen Dreieck'], ['trigonometrie'], []),
    'Flächen und Umfang': (['Flächeninhalt und Umfang'], ['flaechen'], []),
    'Volumen und Oberfläche': (['Volumen und Oberfläche'], ['koerper', 'pyramide-kegel-kugel'], []),
    'Wahrscheinlichkeit': (['Wahrscheinlichkeit einstufig', 'Wahrscheinlichkeit mehrstufig'],
                           ['wahrscheinlichkeit'], ['2021', '2022', '2023']),
    'Wachstum': (['Exponentialfunktionen und Wachstum'], ['potenz-exponentialfunktionen'],
                 ['2021', '2022', '2023']),
}


def lies():
    zeilen = []
    for f, quelle in [('msa-katalog-basis.csv', 'basis'), ('msa-katalog-kontext.csv', 'kontext')]:
        for x in csv.DictReader(open(os.path.join(W, 'msa', f), encoding='utf-8'), delimiter=';'):
            if x['jahr'] in JAHRE and (x['jahr'] != '2026' or x['papier'] == 'FOR'):
                x['_quelle'] = quelle
                zeilen.append(x)
    return zeilen


def blatt0(eintrag):
    p = os.path.join(W, 'katalog', eintrag + '.md')
    s = open(p, encoding='utf-8').read()
    m = re.search(r'### Voraussetzungen \(Blatt 0\)(.*?)\n###', s, re.S)
    return set(re.findall(r'([a-z0-9-]+)\.md', m.group(1))) if m else set()


def main():
    z = lies()
    gesamt = sum(float(x['punkte'] or 0) for x in z)
    eintrag_zu = {e: t for t, (_, es, _) in THEMEN.items() for e in es}
    zeilen = []
    for t, (ms, es, aus) in THEMEN.items():
        r = [x for x in z if x['thema'] in ms]
        p = sum(float(x['punkte'] or 0) for x in r)
        erlaubt = [j for j in JAHRE if j not in aus]
        mit = sorted({x['jahr'] for x in r if x['jahr'] in erlaubt})
        leicht = sum(float(x['punkte'] or 0) for x in r if x['niveau_geschaetzt'].startswith('I') and not x['niveau_geschaetzt'].startswith('II'))
        basis = sum(float(x['punkte'] or 0) for x in r if x['_quelle'] == 'basis')
        vor = set()
        for e in es:
            vor |= {eintrag_zu[v] for v in blatt0(e) if v in eintrag_zu and eintrag_zu[v] != t}
        zeilen.append((t, p, len(mit), len(erlaubt), leicht, basis, sorted(vor)))
    zeilen.sort(key=lambda r: -r[1])
    o = ['# Lernreihenfolge P10 – Daten für die Handreichung', '',
         'Abgeleitet von `werkzeuge/handreichung-reihenfolge.py` (v0.1); nie von Hand ändern.',
         f'Punkte 2020–2026, 2026 nur FOR: {gesamt:g}. Jahre = Jahre mit Punkten von den Jahren, '
         'in denen das Thema geprüft werden durfte (msa-vorgaben.md § 2).', '',
         '| Thema | Anteil | Jahre | leicht (Niveau I) | in der Basis | setzt voraus |',
         '|---|---|---|---|---|---|']
    for t, p, m, e, l, b, v in zeilen:
        o.append(f'| {t} | {100*p/gesamt:.0f} % | {m} von {e} | {100*l/p:.0f} % | {100*b/p:.0f} % | {", ".join(v) or "–"} |')
    # Gegenprobe: Summe der Anteile der zehn Themen
    o += ['', f'Gegenprobe: die zehn Themen tragen zusammen {100*sum(r[1] for r in zeilen)/gesamt:.0f} % der Punkte.']
    open(os.path.join(W, 'msa', 'handreichung-reihenfolge.md'), 'w', encoding='utf-8').write('\n'.join(o) + '\n')
    print('\n'.join(o))


if __name__ == '__main__':
    main()
