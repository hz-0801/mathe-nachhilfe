#!/usr/bin/env python3
"""Baut sa-seiten.md aus sa-zuordnung.csv, sa-seiten.csv, sa-roh.csv und dem Katalogindex."""
import csv, re, collections, statistics as st

KURZ = 'Am meisten Raum bekommen in Klasse 7–10 lineare Funktionen, Körper und Wahrscheinlichkeit (je rund 7 % der Seiten), dann Daten (6 %); Wahrscheinlichkeit, lineare Funktionen, Körper und lineare Gleichungen haben 1,5- bis 2-mal so viel Raum, wie ihr Anteil an den Lerneinheiten des Katalogs erwarten lässt. Auffällig wenig Raum, gemessen am Katalog, bekommen Terme (2,6 % der Seiten bei 5 % der Einheiten; ein Teil der Termseiten steckt in Kapiteln „Terme und Gleichungen“ und fällt über den Titel den Gleichungen zu), lineare Gleichungssysteme (2,4 gegen 4,2 %), quadratische Gleichungen (1,5 gegen 3,3 %), binomische Formeln und Symmetrie/Abbildungen (je 0,8 gegen 2,5 %). Brüche, Bruchrechnung und Einheiten haben in den Bänden 7–10 praktisch keine Seiten (Stoff der Klassen 5/6, nur Sekundo 7 wiederholt ihn), obwohl sie 15 Einheiten des Sek-I-Katalogs stellen – hier misst der Seitenanteil nicht das Gewicht, sondern zeigt Voraussetzungsstoff. Die Schulformen setzen verschieden: Gymnasialreihen geben Potenz- und Exponentialfunktionen (7,1 gegen 3,7 %), trigonometrischen Funktionen (4,0 gegen 1,4 %) und reellen Zahlen mehr Raum, Oberschul-/ISS-Reihen Körpern (8,2 gegen 5,9 %), Zuordnungen (5,5 gegen 3,6 %), Prozentrechnung (4,2 gegen 2,2 %), Flächen und Pythagoras. Gut 3 % der Seiten haben keinen Katalogeintrag, vor allem Sek-II-Vorgriff in Klasse 10 der Gymnasialreihen (ganzrationale Funktionen, Änderungsrate, Ableitung) und Werkzeugseiten (Tabellenkalkulation, Geometriesoftware, Methoden).'
GYM = ['mathedelta', 'fundamente17', 'fundamente24', 'elemente']
OS = ['schnittpunkt', 'mathematik23', 'mheute', 'sekundo']
VOLL = GYM + OS  # fundamente17: nur Kl. 9-10 mit Seitenzahlen, getrennt
ALLE = VOLL
NAME = {'mathedelta': 'mathe.delta (Gym)', 'fundamente24': 'Fundamente 2024 (Gym)', 'elemente': 'Elemente 2016 (Gym)',
        'schnittpunkt': 'Schnittpunkt diff. 2017', 'mathematik23': 'Mathematik 2023 (OS)', 'mheute': 'Mathematik heute',
        'sekundo': 'Sekundo 2017', 'fundamente17': 'Fundamente 2017 (Gym)'}

Z = list(csv.DictReader(open('sa-zuordnung.csv', encoding='utf-8'), delimiter=';'))
S = list(csv.DictReader(open('sa-seiten.csv', encoding='utf-8'), delimiter=';'))
R = list(csv.DictReader(open('sa-roh.csv', encoding='utf-8'), delimiter=';'))

# Katalog
kat = {}
idx = open('mathe-nachhilfe/katalog/index.md', encoding='utf-8').read().split('## Sekundarstufe II')[0]
for line in idx.splitlines():
    m = re.match(r'\| ([\w-]+)\.md \|', line)
    if not m: continue
    f = m.group(1); t = open(f'mathe-nachhilfe/katalog/{f}.md', encoding='utf-8').read()
    le = re.search(r'### Lerneinheiten\n(.*?)\n###', t, re.S)
    units = {}
    if le:
        for l in le.group(1).splitlines():
            mm = re.match(r'(\d+)\. (.*)', l)
            if mm: units[mm.group(1)] = re.split(r' – | \(|: ', mm.group(2))[0][:50]
    cells = [c.strip() for c in line.split('|')]
    kat[f] = dict(titel=t.splitlines()[0].lstrip('# '), units=units, klasse=cells[5] if len(cells) > 5 else '', p10=cells[6] if len(cells) > 6 else '')

# Bandsummen (Inhaltsteil: ohne Kapitelzeilen und Anhang)
band = collections.Counter(); bandk = collections.Counter()
for r in Z:
    if r['art'] in ('kapitel', 'anhang') or r['plausibel'] != 'ja': continue
    band[r['reihe']] += int(r['seiten']); bandk[(r['reihe'], r['klasse'])] += int(r['seiten'])

ein = collections.defaultdict(lambda: collections.Counter())    # eintrag -> reihe -> seiten mit rahmen
eind = collections.defaultdict(lambda: collections.Counter())   # direkt
einh = collections.defaultdict(lambda: collections.Counter())   # (eintrag, einheit) -> reihe -> seiten (Titeltreffer)
for s in S:
    ein[s['eintrag']][s['reihe']] += int(s['seiten_mit_rahmen'])
    eind[s['eintrag']][s['reihe']] += int(s['seiten'])
    if s['einheit']:
        einh[(s['eintrag'], s['einheit'])][s['reihe']] += int(s['seiten'])

def anteil(e, r, src=ein):
    return 100 * src[e][r] / band[r] if band[r] else 0

rows = []
for e in kat:
    a_all = [anteil(e, r) for r in VOLL]
    rows.append(dict(e=e, mittel=st.mean(a_all), gym=st.mean([anteil(e, r) for r in GYM]), os=st.mean([anteil(e, r) for r in OS]),
                     seiten=st.mean([ein[e][r] for r in VOLL]), direkt=st.mean([eind[e][r] for r in VOLL]),
                     nunits=len(kat[e]['units']), min=min(a_all), max=max(a_all)))
rows.sort(key=lambda x: -x['mittel'])
tot_units = sum(x['nunits'] for x in rows)
for x in rows:
    x['soll'] = 100 * x['nunits'] / tot_units  # Anteil an den Lerneinheiten des Sek-I-Katalogs
    x['verh'] = x['mittel'] / x['soll'] if x['soll'] else 0
kein_e = [e for e in ein if e.startswith('kein')]
kein_anteil = st.mean([sum(ein[e][r] for e in kein_e) * 100 / band[r] for r in VOLL])

out = []
P = out.append
P('# Seitenanteil in Lehrwerken je Katalogeintrag (Sek I, Klasse 7–10)')
P('')
P('Stand ' + __import__('subprocess').run(['date', '+%Y-%m-%d'], capture_output=True, text=True).stdout.strip() +
  '. Gewichtsmaß „Unterrichtszeit“: Seiten, die ein Lehrwerk einem Unterkapitel gibt (Startseite des nächsten Eintrags minus eigene Startseite, aus den DNB-Inhaltsverzeichnissen in `quellen/`). Skripte: `sa_parse.py` → `sa-roh.csv`, `sa_zuordnung.py` (Zuordnungsregeln als Python-Liste) → `sa-zuordnung.csv`, `sa-seiten.csv`, `sa_bericht.py` → diese Datei.')
P('')
P('## Kurzfassung')
P('')
P('@@KURZ@@')
P('')
P('## Lesart')
P('')
P('- **Seiten direkt**: Unterkapitel, deren Titel (oder Kapitel) zum Eintrag passt, und thematische Streifzüge. **Mit Rahmen**: zusätzlich Kapitelöffner, Vermischtes, Zusammenfassung, Tests und Streifzüge ohne Titeltreffer, je dem benachbarten Unterkapitel zugeschlagen (Öffner dem folgenden, sonst dem vorangehenden). Anteile beziehen sich auf „mit Rahmen“.')
P('- **Anteil** = Seiten des Eintrags / Seiten des Inhaltsteils der Bände 7–10 einer Reihe (ohne Anhang, Lösungen, Register). Mittel über alle acht Reihen (jede Reihe gleich gewichtet, Anteile statt Seiten, damit dicke Bände nicht mehr zählen); Gym = mathe.delta, Fundamente 2017, Fundamente 2024, Elemente 2016; OS/ISS = Schnittpunkt, Mathematik 2023, Mathematik heute, Sekundo. mathe.delta Kl. 8: das Verzeichnis endet nach Kapitel 4 (Kapitel 5–6 nur im Stoffverteilungsplan, ohne Seiten), der Band zählt daher nur 130 Seiten.')
P('- **Katalogstellung** = Anteil des Eintrags an allen Lerneinheiten der Sek-I-Einträge (%d Einheiten). **Faktor** = Seitenanteil / Katalogstellung: > 1,5 viel Raum im Lehrwerk, < 0,67 wenig Raum, gemessen am Gewicht im Katalog.' % tot_units)
P('- Grenzen: OCR-Fehler und zweispaltige Verzeichnisse; Kapitelöffner ohne eigene Seitenzahl (Mathematik 2023) fallen dem vorigen Eintrag zu; Mathematik 2023 hat Einzelseiten je Unterkapitel, andere Reihen Doppelseiten; das ändert die Feinheit, nicht die Anteile. Werte sind Größenordnungen, keine Stundenzahlen.')
P('')
P('## Rangliste der Einträge nach mittlerem Seitenanteil')
P('')
P('| Rang | Eintrag | Klasse (Gym / OS) | Einheiten | Seiten Ø (direkt / mit Rahmen) | Anteil Ø | Gym | OS/ISS | Spanne | Katalogstellung | Faktor |')
P('|---:|---|---|---:|---|---:|---:|---:|---|---:|---:|')
for i, x in enumerate(rows, 1):
    P(f"| {i} | {x['e']} | {kat[x['e']]['klasse'][:28]} | {x['nunits']} | {x['direkt']:.0f} / {x['seiten']:.0f} | {x['mittel']:.1f} % | {x['gym']:.1f} % | {x['os']:.1f} % | {x['min']:.1f}–{x['max']:.1f} % | {x['soll']:.1f} % | {x['verh']:.2f} |")
P(f"| – | kein Katalogeintrag (Werkzeug, Problemlösen, Sek-II-Stoff, unlesbare Titel) | | | | {kein_anteil:.1f} % | | | | | |")
P('')
P('## Seiten je Eintrag und Reihe (Klasse 7–10, mit Rahmen; in Klammern Anteil am Inhaltsteil)')
P('')
P('| Eintrag | ' + ' | '.join(NAME[r] for r in ALLE) + ' |')
P('|---|' + '---:|' * len(ALLE))
for x in rows:
    P(f"| {x['e']} | " + ' | '.join(f"{ein[x['e']][r]} ({anteil(x['e'], r):.1f})" for r in ALLE) + ' |')
P('| **Inhaltsteil gesamt** | ' + ' | '.join(str(band[r]) for r in ALLE) + ' |')
P('')
P('Inhaltsteil je Band (Seiten): ' + '; '.join(f"{NAME[r]}: " + ', '.join(f"{k} = {bandk[(r, str(k))]}" for k in (7, 8, 9, 10)) for r in ALLE) + '.')
P('')
P('## Seiten je Lerneinheit (direkt, nur Titeltreffer; Ø über acht Reihen)')
P('')
P('Nur Unterkapitel, deren Titel eine Einheit erkennen lässt; Kapitelrahmen und Unterkapitel ohne Einheitsbezug fehlen hier, die Summe je Eintrag ist daher kleiner als oben.')
P('')
for x in rows:
    e = x['e']; parts = []
    for u, name in kat[e]['units'].items():
        v = st.mean([einh[(e, u)][r] for r in VOLL])
        parts.append(f"E{u} {name}: {v:.1f}")
    P(f"- **{e}** – " + ' · '.join(parts))
P('')
P('## Einträge ohne oder mit sehr wenig Lehrwerksseiten (Kl. 7–10)')
P('')
wenig = [x for x in rows if x['seiten'] < 5]
for x in wenig:
    P(f"- {x['e']}: Ø {x['seiten']:.1f} Seiten (Klasse laut Katalog {kat[x['e']]['klasse'][:40]}) – " + ', '.join(f"{NAME[r]} {ein[x['e']][r]}" for r in VOLL if ein[x['e']][r]))
leer_einh = []
for x in rows:
    for u, name in kat[x['e']]['units'].items():
        if all(einh[(x['e'], u)][r] == 0 for r in ALLE):
            leer_einh.append(f"{x['e']} E{u} {name}")
P('')
P('Lerneinheiten ohne einen einzigen Titeltreffer in Kl. 7–10: ' + ('; '.join(leer_einh) if leer_einh else 'keine') + '.')
P('')
P('## Unterkapitel ohne Katalogeintrag (Kandidaten für Lücken)')
P('')
P('Titel so, wie das Inhaltsverzeichnis sie liefert (OCR-Fehler belassen); Seiten in Klammern. „Nachbar“: Unterkapitel ohne Titeltreffer, dem vorangehenden Eintrag zugeschlagen – bitte prüfen.')
P('')
grp = collections.defaultdict(list)
for r in Z:
    if r['art'] in ('uk', 'streifzug') and (r['eintrag'].startswith('kein') or r['weg'] == 'nachbar'):
        lab = r['eintrag'] if r['weg'] != 'nachbar' else 'nachbar → ' + r['eintrag']
        grp[lab].append(f"{r['titel'][:60]} ({NAME[r['reihe']].split(' (')[0]} {r['klasse']}, {r['seiten'] or '?'})")
for lab in sorted(grp):
    P(f"- **{lab}** ({len(grp[lab])}): " + '; '.join(grp[lab]))
P('')
P('## Kapitelumfang')
P('')
P('Kapitel mit erkannter Überschrift und Seitenzahl (Mathematik 2023: Kapitel = Abschnitt bis zum „Ausgangstest“; Mathematik heute Kl. 8: Kapitel 2–5 fehlen im Verzeichnis, Kapitel 1 enthält daher deren Seiten).')
P('')
for r0 in ALLE:
    ks = [r for r in R if r['reihe'] == r0 and r['art'] == 'kapitel' and r['seiten']]
    P(f"- **{NAME[r0]}**: " + '; '.join(f"{k['klasse']}/{k['nr']} {k['titel'][:30]} {k['seiten']}" for k in ks))
P('')
P('## Gegenprobe')
P('')
P('@@GEGEN@@')

# Gegenprobe: Summe der Seiten gegen letzte Seitenzahl
geg = []
for r0, kl in (('schnittpunkt', '8'), ('mathematik23', '8'), ('sekundo', '9')):
    B = [r for r in R if r['reihe'] == r0 and r['klasse'] == kl and r['art'] != 'kapitel' and r['start']]
    first = min(int(r['start']) for r in B); last = max(int(r['start']) for r in B)
    summe = sum(int(r['seiten']) for r in B if r['seiten'] and r['plausibel'] == 'ja')
    nein = sum(int(r['seiten']) for r in B if r['seiten'] and r['plausibel'] == 'nein')
    inh = sum(int(r['seiten']) for r in B if r['seiten'] and r['plausibel'] == 'ja' and r['art'] != 'anhang')
    anh0 = min([int(r['start']) for r in B if r['art'] == 'anhang' and int(r['start']) > 0.6 * last] or [last])
    inh = sum(int(r['seiten']) for r in B if r['seiten'] and r['plausibel'] == 'ja' and int(r['start']) < anh0)
    geg.append(f"- {NAME[r0]} Kl. {kl}: erste Seitenzahl {first}, letzte Seitenzahl (Beginn des letzten Eintrags) {last}; Summe aller plausiblen Seitenumfänge {summe} (+ {nein} unplausibel) = letzte − erste ({last - first}) {'stimmt' if summe + nein == last - first else 'weicht ab'}; Inhaltsteil {inh} Seiten = Anhangbeginn {anh0} − {first} ({anh0 - first}) {'stimmt' if inh == anh0 - first else 'weicht ab'}.")
txt = '\n'.join(out).replace('@@KURZ@@', KURZ).replace('@@GEGEN@@', '\n'.join(geg) + '\n\nDie Summe ist durch die Bauart (Differenzen aufeinanderfolgender Startseiten) gleich der Spanne erste–letzte Seite, solange kein Eintrag als unplausibel fällt; die Probe prüft also Lücken und Ausreißer, nicht die Seitenzahlen selbst. Fehlende Unterkapitel (OCR ohne Seitenzahl) verschieben Seiten auf den vorangehenden Eintrag, ändern die Summe aber nicht.')
open('sa-seiten.md', 'w', encoding='utf-8').write(txt)
for x in rows:
    print(f"{x['e'][:26]:26} {x['mittel']:5.1f} gym {x['gym']:5.1f} os {x['os']:5.1f} soll {x['soll']:4.1f} f {x['verh']:.2f} S {x['seiten']:.0f}")
print('kein', round(kein_anteil, 1), 'band', dict(band))
print('\n'.join(geg))
print('leere Einheiten:', leer_einh)
