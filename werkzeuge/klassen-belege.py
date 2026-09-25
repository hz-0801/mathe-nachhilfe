"""Klassenbelege je Lerneinheit (Sek I) aus den Inhaltsverzeichnissen der Lehrwerke.

Liest die 29 Sek-I-Einträge aus katalog/ (Tabelle Sekundarstufe I in index.md, Verortung, Lerneinheiten,
Typen je Lerneinheit), die Verzeichnisdateien unter quellen/ und die Zuordnungen in
werkzeuge/klassen-belege-daten.py, prüft jedes Zitat an der Quelldatei und jeden Typnamen am Eintrag und schreibt
katalog/_klassen-belege.md sowie die Typenliste werkzeuge/klassen-belege-typen.txt.
Aufruf aus der Repo-Wurzel: python werkzeuge/klassen-belege.py – mit --probe wird nur gebaut und mit der
vorhandenen katalog/_klassen-belege.md verglichen, nichts geschrieben.

Die Stand-Zeile nennt Datum und Kurzhash des letzten Commits, der eine Eingabe geändert hat (index.md, die 29
Einträge, die Verzeichnisdateien); ein Lauf ohne geänderte Eingaben erzeugt deshalb dieselbe Datei.
Entstanden im Auftrag Nacht 2026-09-25, Teil 2 (archiv/auftrag-nacht-2026-09-25.md).
"""
import os, re, sys, glob, subprocess
from collections import OrderedDict, Counter, defaultdict

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
DATEN = os.path.join(HIER, 'klassen-belege-daten.py')
TYPENLISTE = os.path.join(HIER, 'klassen-belege-typen.txt')
Q = os.path.join(REPO, 'quellen')
KAT = os.path.join(REPO, 'katalog')

# ---------- Reihen ----------
REIHEN = OrderedDict([
    ('SEK', dict(name='Sekundo', form='OS', dateien=['quelle-westermann-sekundo-bb-2017-inhalt.txt'])),
    ('M23', dict(name='Mathematik 2023', form='OS', dateien=['quelle-westermann-mathematik2023-bebbstth-inhalt.txt', 'quelle-westermann-mathematik2022-bebbstth-kl5-6-inhalt.txt'])),
    ('SP', dict(name='Schnittpunkt', form='OS', dateien=['quelle-klett-schnittpunkt-mathematik-diff2017-inhalt.txt', 'quelle-klett-schnittpunkt-mathematik-diff2017-kl5-6-inhalt.txt'])),
    ('MH', dict(name='Mathematik heute', form='OS', dateien=['quelle-westermann-mathematikheute-bebb-inhalt.txt', 'quelle-westermann-mathematikheute-bebb-kl5-6-inhalt.txt'])),
    ('LS', dict(name='LS', form='GYM', dateien=['quelle-klett-fahrplan-ls-aa-berlin-2024.txt'])),
    ('FDM', dict(name='Fundamente', form='GYM', dateien=['quelle-cornelsen-fundamente-bb-ausgabeb2024-inhalt.txt', 'quelle-cornelsen-fundamente-bb-ausgabeb2024-kl5-6-inhalt.txt'])),
    ('FDM17', dict(name='Fundamente 2017', form='GYM', dateien=['quelle-cornelsen-fundamente-bb-ausgabeb2017-inhalt.txt'], neben=True)),
    ('EDM', dict(name='Elemente', form='GYM', dateien=['quelle-westermann-elemente-der-mathematik-bb-2016u2025-inhalt.txt'])),
    ('MD', dict(name='mathe.delta', form='GYM', dateien=['quelle-buchner-mathedelta-bb-2016-inhalt.txt'])),
    ('SEKF', dict(name='Sekundo-Förderheft', form='F', dateien=['quelle-westermann-sekundo-foerder-be_bb2017-inhalt.txt'])),
    ('M23F', dict(name='Mathematik-2023-Förderheft', form='F', dateien=['quelle-westermann-mathematik2023-foerder-bebbstth-inhalt.txt'])),
    ('SPF', dict(name='Schnittpunkt-Förderheft', form='F', dateien=['quelle-klett-schnittpunkt-foerder-diff2017-inhalt.txt'])),
    ('MHF', dict(name='Mathematik heute „Diagnose und Fördern“', form='F', dateien=['quelle-westermann-mathematikheute-diagnoseundfoerdern-inhalt.txt'])),
])
OS = [k for k, v in REIHEN.items() if v['form'] == 'OS']
GYM = [k for k, v in REIHEN.items() if v['form'] == 'GYM']
GYM_HAUPT = [k for k in GYM if not REIHEN[k].get('neben')]
FOERDER = [k for k, v in REIHEN.items() if v['form'] == 'F']
# LS-Fahrplan: Abschnitte Klasse 5-10 als Zeilenbereiche (Kapitelübersicht vor der Synopse)
LS_ABSCHNITTE = [(21, 78, 5), (79, 113, 6), (114, 144, 7), (145, 177, 8), (178, 213, 9), (214, 244, 10)]

MARKEN_PRAEFIXE = ['LVL:', 'Vertiefen:', 'Üben:', 'EXTRA:', 'Streifzug:', 'Exkursion', 'Themenseite:', 'Werkzeug:',
                   'Mathematisch arbeiten:', 'Mit Medien arbeiten:', 'Arbeiten mit dem Computer:', 'Im Blickpunkt:',
                   'Projekt:', 'Wissen kompakt', 'Bleib fit', 'Diagnosetest', 'Training', 'Vertiefung', 'Sonderfälle']
MARKEN_ENTHALTEN = [('Zum Selbstlernen', 'Zum Selbstlernen'), ('Zum Se.bstlernen', 'Zum Selbstlernen'),
                    ('(Wiederholung)', 'Wiederholung'), ('Wiederholung:', 'Wiederholung')]

def norm(s):
    s = s.replace('\f', ' ').replace('\u00ad', '')
    s = s.replace('…', ' ')
    s = re.sub(r'(?:\s*[.·]){2,}', ' ', s)
    s = re.sub(r'_{2,}', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

# ---------- Quelldateien lesen ----------
DATEIEN = {}
def lade(datei):
    if datei in DATEIEN:
        return DATEIEN[datei]
    zeilen = open(os.path.join(Q, datei), encoding='utf-8').read().split('\n')
    abschn = []  # (von, bis, klassenkey)
    if 'fahrplan-ls' in datei:
        abschn = [(a, b, k) for a, b, k in LS_ABSCHNITTE]
    else:
        start = None; key = None
        for i, l in enumerate(zeilen, 1):
            m = re.match(r'^== (?:Ausgabe (\d{4}), )?Klasse (\d+)', l)
            if m:
                if start is not None:
                    abschn.append((start, i - 1, key))
                key = f'{m.group(1)}-{m.group(2)}' if m.group(1) else int(m.group(2))
                start = i + 1
        if start is not None:
            abschn.append((start, len(zeilen), key))
    DATEIEN[datei] = (zeilen, abschn)
    return DATEIEN[datei]

def klassenzahl(key):
    return int(str(key).split('-')[-1])

FEHLER = []

def finde(reihe, klasse, seg, zhinweis=None):
    """liefert (datei, zeilennummer) für ein Segment in der Klasse der Reihe"""
    ns = norm(seg)
    treffer = []
    for d in REIHEN[reihe]['dateien']:
        zeilen, abschn = lade(d)
        for a, b, k in abschn:
            if str(k) != str(klasse):
                continue
            for i in range(a, b + 1):
                if ns and ns in norm(zeilen[i - 1]):
                    treffer.append((d, i))
    if zhinweis:
        treffer = [t for t in treffer if t[1] in zhinweis]
    if len(treffer) != 1:
        FEHLER.append(f'{reihe} Kl. {klasse}: Segment „{seg}“ – {len(treffer)} Treffer {treffer[:4]}')
        return (None, None)
    return treffer[0]

# ---------- Katalog ----------
def lies_katalog():
    """Die Sek-I-Einträge aus katalog/index.md mit Lerneinheiten und Typzeilen (Zeilennummern ab 1)."""
    idx = open(os.path.join(KAT, 'index.md'), encoding='utf-8').read().splitlines()
    eintraege, in_sek1 = [], False
    for l in idx:
        if l.strip() == '## Sekundarstufe I':
            in_sek1 = True; continue
        if l.startswith('## ') and in_sek1:
            break
        if in_sek1 and l.startswith('| ') and l.endswith('|') and '.md' in l.split('|')[1]:
            eintraege.append(l.split('|')[1].strip())

    def abschnitt(lines, titel):
        out, drin = [], False
        for i, l in enumerate(lines, 1):
            if l.startswith('### '):
                if drin: break
                if l.strip() == '### ' + titel: drin = True; continue
            if drin: out.append((i, l))
        return out

    daten = {}
    for e in eintraege:
        lines = open(os.path.join(KAT, e), encoding='utf-8').read().splitlines()
        einheiten = []
        for i, l in abschnitt(lines, 'Lerneinheiten'):
            m = re.match(r'^(\d+)\.\s+(.*)$', l)
            if m:
                einheiten.append({'nr': int(m.group(1)), 'zeile': i, 'text': m.group(2)})
        daten[e] = {'einheiten': einheiten, 'typen': [(i, l) for i, l in abschnitt(lines, 'Typen je Lerneinheit') if l.strip()]}
    return {'eintraege': eintraege, 'daten': daten}

KATALOG = lies_katalog()
EINTRAEGE = [e[:-3] for e in KATALOG['eintraege']]
KURZ = {}  # Kürzel -> (eintrag, nr)
KUERZEL_EINTRAG = {
    'bd': 'brueche-dezimalzahlen', 'br': 'bruchrechnung', 'rz': 'rationale-zahlen', 'pr': 'prozentrechnung',
    'zi': 'zinsrechnung', 'pw': 'potenzen-wurzeln', 're': 'reelle-zahlen', 'ei': 'einheiten', 'fl': 'flaechen',
    'kr': 'kreis', 'ko': 'koerper', 'pk': 'pyramide-kegel-kugel', 'py': 'pythagoras', 'tr': 'trigonometrie',
    'wd': 'winkel-dreiecke', 'sy': 'symmetrie-abbildungen', 'st': 'strahlensaetze', 'zu': 'zuordnungen',
    'te': 'terme', 'lg': 'lineare-gleichungen', 'lf': 'lineare-funktionen', 'lgs': 'lineare-gleichungssysteme',
    'bi': 'binomische-formeln', 'qf': 'quadratische-funktionen', 'qg': 'quadratische-gleichungen',
    'pe': 'potenz-exponentialfunktionen', 'tf': 'trigonometrische-funktionen', 'da': 'daten', 'wa': 'wahrscheinlichkeit'}
assert sorted(KUERZEL_EINTRAG.values()) == sorted(EINTRAEGE), set(EINTRAEGE) ^ set(KUERZEL_EINTRAG.values())
EINTRAG_KUERZEL = {v: k for k, v in KUERZEL_EINTRAG.items()}

def einheiten(e):
    return KATALOG['daten'][e + '.md']['einheiten']

def typzeile(e, nr):
    for zi, l in KATALOG['daten'][e + '.md']['typen']:
        if re.match(rf'^\s*[-*]?\s*Einheit {nr}:', l):
            return zi, l
    return None, ''

def pruefe_typ(e, nr, typ):
    zi, l = typzeile(e, nr)
    if not l:
        FEHLER.append(f'{e} E{nr}: keine Typzeile'); return None
    m = re.match(r'^\s*[-*]?\s*Einheit \d+:\s*', l)
    rest = ' · ' + l[m.end():]
    if (' · ' + typ) not in rest:
        FEHLER.append(f'{e} E{nr}: Typ „{typ}“ steht nicht wortgleich als Typ im Eintrag')
        return None
    return zi

def klassensatz(e):
    lines = open(os.path.join(KAT, e + '.md'), encoding='utf-8').read().split('\n')
    drin = False
    for i, l in enumerate(lines, 1):
        if l.strip() == '### Verortung':
            drin = True; continue
        if drin and l.strip():
            return i, saetze(l)
    return None, []

ABK = {'Kl', 'S', 'z', 'B', 'bzw', 'ggf', 'u', 'a', 'vgl', 'Nr', 'ca', 'd', 'h', 'etc', 'Jg', 'Abs', 'max', 'min', 'o', 'v', 's'}
def saetze(t):
    out, tiefe, start = [], 0, 0
    i = 0
    while i < len(t):
        c = t[i]
        if c in '([': tiefe += 1
        elif c in ')]': tiefe = max(0, tiefe - 1)
        elif c == '.' and tiefe == 0 and (i + 1 == len(t) or t[i + 1] == ' '):
            wort = re.findall(r'(\w+)$', t[start:i])
            if not (wort and (wort[0] in ABK or len(wort[0]) == 1 or wort[0].isdigit())):
                out.append(t[start:i + 1].strip()); start = i + 1
        i += 1
    if t[start:].strip():
        out.append(t[start:].strip())
    return out

# ---------- Daten ----------
REFS = []
KEINE = {}      # (kuerzel, reihe) -> Grund
UNIT_ERM = defaultdict(list)   # kuerzel -> [Text]
def R(unit, reihe, klasse, segs, seite=None, typ=None, marke=None, erm=None, z=None, kap=None, zus=None):
    if isinstance(segs, str): segs = [segs]
    if isinstance(typ, str): typ = [typ]
    if isinstance(marke, str): marke = [marke]
    REFS.append(dict(unit=unit, reihe=reihe, klasse=klasse, segs=segs, seite=seite, typ=typ or [], marke=marke or [],
                     erm=erm, z=z, kap=kap, zus=zus))
def K(unit, reihe, grund):
    KEINE[(unit, reihe)] = grund
def E(unit, text):
    UNIT_ERM[unit].append(text)

# Die Datendatei besteht aus Abschnitten „# ==== Abschnitt: <name> ====“ (je Reihe bzw. Förderhefte); jeder
# Abschnitt läuft in einem eigenen Namensraum, weil die Abschnitte gleiche Hilfsnamen verschieden belegen.
def lade_daten():
    text = open(DATEN, encoding='utf-8').read()
    teile = re.split(r'^# ==== Abschnitt: (\S+) ====$', text, flags=re.M)
    assert len(teile) > 1, 'keine Abschnitte in der Datendatei'
    for name, code in zip(teile[1::2], teile[2::2]):
        exec(compile(code, f'{DATEN}:{name}', 'exec'), dict(R=R, K=K, E=E))
lade_daten()

# ---------- auflösen ----------
def unit_split(u):
    m = re.match(r'^([a-z]+)(\d+)$', u)
    return KUERZEL_EINTRAG[m.group(1)], int(m.group(2))

for r in REFS:
    e, nr = unit_split(r['unit'])
    if nr > len(einheiten(e)):
        FEHLER.append(f'{r["unit"]}: Einheit {nr} gibt es nicht')
    r['eintrag'], r['nr'] = e, nr
    zs = []
    zl = r['z'] or [None] * len(r['segs'])
    for s, zh in zip(r['segs'], zl):
        d, zi = finde(r['reihe'], r['klasse'], s, [zh] if zh else None)
        zs.append(zi); r['datei'] = d
    r['zeilen'] = zs
    if r['kap']:
        d, zi = finde(r['reihe'], r['klasse'], r['kap'])
        r['kapzeile'] = zi
    r['typzeilen'] = [pruefe_typ(e, nr, t) for t in r['typ']]
    # Marken aus dem Text
    auto = []
    for s in r['segs']:
        for p in MARKEN_PRAEFIXE:
            if norm(s).startswith(p):
                auto.append(p.rstrip(':'))
        for p, lab in MARKEN_ENTHALTEN:
            if p in norm(s) and lab not in auto:
                auto.append(lab)
    r['automarken'] = auto

if FEHLER:
    print('FEHLER:')
    for f in FEHLER: print(' ', f)
    sys.exit(1)

# ---------- Ausgabe ----------
def zitat(r):
    t = ' '.join(norm(s) for s in r['segs'])
    return t

def zeilentext(r):
    zs = [z for z in r['zeilen'] if z]
    return 'Z. ' + ', '.join(str(z) for z in zs)

def kl_text(k):
    k = str(k)
    if '-' in k:
        a, b = k.split('-')
        return f'Kl. {b} (Ausgabe {a})'
    return f'Kl. {k}'

def beleg(r):
    kopf = kl_text(r['klasse'])
    s = f'S. {r["seite"]}' if r['seite'] else None
    txt = f'„{zitat(r)}“ ({zeilentext(r)})'
    if r['kap']:
        txt = f'„{norm(r["kap"])}“ (Z. {r["kapzeile"]}) › {txt}'
    return f'{kopf}{", " + s if s else ""}: {txt}'

def main():
    out = []
    nach_unit = defaultdict(list)
    for r in REFS:
        nach_unit[r['unit']].append(r)
    stat = Counter()
    marken_zahl = Counter()
    typzeilen_gesamt = 0
    erm_gesamt = 0
    spanne_ja, boden_ja = [], []
    abschnitte = []
    foerder_zeilen = 0; foerder_einheiten = 0; spanne_einheiten = []; ohne = []; getrennt_ja = []; ohne_gym = []
    erm_je = OrderedDict()
    for e in EINTRAEGE:
        kz = EINTRAG_KUERZEL[e]
        vz, ks = klassensatz(e)
        satz = next((s for s in ks if re.search(r'Klasse|Kl\. ?\d', s)), ks[0] if ks else '')
        a = [f'### {e} – {satz}', f'- Verortung (Zeile {vz}), Klassensatz wortgleich.']
        eintrag_spanne = False; eintrag_boden = False; eintrag_erm = []; foerder_erm = OrderedDict(); sp_det = []
        for u in einheiten(e):
            key = f'{kz}{u["nr"]}'
            titel = re.split(r' – |: ', u['text'], 1)[0]
            a.append(f'- {u["nr"]}. {titel}')
            refs = nach_unit.get(key, [])
            einf = {}   # reihe -> Liste Klassen
            for rk in list(REIHEN):
                rr = [r for r in refs if r['reihe'] == rk]
                if rr and REIHEN[rk]['form'] != 'F':
                    einf[rk] = sorted({klassenzahl(r['klasse']) for r in rr})
            fruehest = min((k for rk, v in einf.items() if rk != 'FDM17' for k in v), default=None)
            for rk in list(REIHEN):
                if REIHEN[rk]['form'] == 'F':
                    continue
                rr = [r for r in refs if r['reihe'] == rk]
                name = REIHEN[rk]['name']
                if rr:
                    for r in sorted(rr, key=lambda r: (klassenzahl(r['klasse']), r['zeilen'][0] or 0)):
                        zus = f' – {r["zus"]}' if r['zus'] else ''
                        a.append(f'  - {name} {beleg(r)}{zus}')
                        if r['erm']:
                            a.append(f'    Ermessen: {r["erm"]}')
                            eintrag_erm.append(f'Einheit {u["nr"]}, {name} {kl_text(r["klasse"])}: {r["erm"]}')
                else:
                    grund = KEINE.get((key, rk)) or standardgrund(key, rk, fruehest)
                    a.append(f'  - {name}: keine Stelle – {grund}')
            # Typzeilen
            for r in refs:
                if REIHEN[r['reihe']]['form'] == 'F':
                    continue
                for t in r['typ']:
                    s = f', S. {r["seite"]}' if r['seite'] else ''
                    a.append(f'  - Typ: {t} – {REIHEN[r["reihe"]]["name"]} {kl_text(r["klasse"])}{s}: „{zitat(r)}“')
                    typzeilen_gesamt += 1
            # Marken
            mk = []
            for r in refs:
                if REIHEN[r['reihe']]['form'] == 'F':
                    continue
                for m in r['automarken']:
                    mk.append(f'{REIHEN[r["reihe"]]["name"]} {kl_text(r["klasse"])}: „{zitat(r)}“')
                    marken_zahl[m] += 1
                for m in r['marke']:
                    lab, _, txt = m.partition('|')
                    mk.append(f'{REIHEN[r["reihe"]]["name"]} {kl_text(r["klasse"])}: {txt or lab} bei „{zitat(r)}“')
                    marken_zahl[lab] += 1
            a.append('  - Marken: ' + ('; '.join(dict.fromkeys(mk)) if mk else 'keine'))
            # Förderhefte
            fr = [r for r in refs if REIHEN[r['reihe']]['form'] == 'F']
            if fr:
                for r in sorted(fr, key=lambda r: (list(REIHEN).index(r['reihe']), klassenzahl(r['klasse']), r['zeilen'][0] or 0)):
                    a.append(f'  - Förderheft: {REIHEN[r["reihe"]]["name"]} {beleg(r)}')
                    foerder_zeilen += 1
                    if r['erm']:
                        kurz = 'Themenblock ohne Unterkapitel, dem Blocktitel nach zugeordnet (Grund unter „Ermessen“ des Eintrags).' \
                            if r['reihe'] == 'MHF' else r['erm']
                        a.append(f'    Ermessen: {kurz}')
                        fk = (REIHEN[r['reihe']]['name'], kl_text(r['klasse']), zitat(r), r['erm'])
                        foerder_erm.setdefault(fk, []).append(u['nr'])
                foerder_einheiten += 1
            else:
                a.append('  - Förderheft: keine Stelle')
            for t in UNIT_ERM.get(key, []):
                a.append(f'  - Ermessen: {t}')
                eintrag_erm.append(f'Einheit {u["nr"]}: {t}')
            # Zusammenfassung
            os_e = {rk: min(v) for rk, v in einf.items() if rk in OS}
            gy_e = {rk: min(v) for rk, v in einf.items() if rk in GYM_HAUPT}
            a.append('  - ' + zusammenfassung('OS', OS, einf, os_e))
            a.append('  - ' + zusammenfassung('GYM', GYM_HAUPT, einf, gy_e))
            osw = spanne(wirksam(os_e)[0]); gyw = spanne(wirksam(gy_e)[0])
            if os_e and gy_e and osw != gyw:
                eintrag_spanne = True
                spanne_einheiten.append((e, u['nr'], titel, osw, gyw))
                sp_det.append((u['nr'], osw, gyw, getrennt(osw, gyw)))
            alle = [k for v in einf.values() for k in v]
            if any(k <= 6 for rk, v in einf.items() if rk not in ('FDM17',) for k in v):
                eintrag_boden = True
            stat['einheiten'] += 1
            if os_e: stat['os'] += 1
            if gy_e: stat['gym'] += 1
            if os_e and gy_e: stat['beide'] += 1
            if os_e and not gy_e: ohne_gym.append(f'{e} {u["nr"]}. {titel}')
            if not os_e and not gy_e:
                stat['keine'] += 1; ohne.append(f'{e} {u["nr"]}. {titel}')
        for (fn, fkl, fz, ferm), nrs in foerder_erm.items():
            eintrag_erm.append(f'Einheit{"en" if len(nrs) > 1 else ""} {", ".join(str(n) for n in nrs)}, Förderheft {fn} {fkl} „{fz}“: {ferm}')
        if eintrag_spanne:
            det = '; '.join(f'Einheit {n}: OS {o}, GYM {g}' for n, o, g, _ in sp_det)
            getr = [str(n) for n, _, _, t in sp_det if t]
            if getr:
                det += f'; ohne gemeinsame Klasse: Einheit{"en" if len(getr) > 1 else ""} {", ".join(getr)}'
                getrennt_ja.append(e)
            a.append(f'- Spanne OS/GYM: ja ({det})')
        else:
            a.append('- Spanne OS/GYM: nein')
        a.append(f'- Boden: {"ja" if eintrag_boden else "nein"}')
        a.append(f'- Ermessen ({len(eintrag_erm)}):' + ('' if eintrag_erm else ' keine'))
        for t in eintrag_erm:
            a.append(f'  - {t}')
        erm_gesamt += len(eintrag_erm)
        erm_je[e] = len(eintrag_erm)
        if eintrag_spanne: spanne_ja.append(e)
        if eintrag_boden: boden_ja.append(e)
        abschnitte.append('\n'.join(a))
    return dict(abschnitte=abschnitte, stat=stat, spanne_ja=spanne_ja, boden_ja=boden_ja, typzeilen=typzeilen_gesamt,
                ermessen=erm_gesamt, marken=marken_zahl, foerder_zeilen=foerder_zeilen,
                foerder_einheiten=foerder_einheiten, spanne_einheiten=spanne_einheiten, ohne=ohne, erm_je=erm_je,
                getrennt_ja=getrennt_ja, ohne_gym=ohne_gym)

def getrennt(a, b):
    def rng(s):
        t = s.replace('Kl. ', '').split('–')
        return int(t[0]), int(t[-1])
    (a1, a2), (b1, b2) = rng(a), rng(b)
    return a2 < b1 or b2 < a1

START = {rk: min(klassenzahl(k) for d in v['dateien'] for (_, _, k) in lade(d)[1]) for rk, v in REIHEN.items()}

def wirksam(e):
    """Einführungsklassen ohne die Reihen, die erst in Klasse 7 beginnen, wenn eine andere Reihe derselben
    Schulform früher einführt (ihre 7 ist dann der erste Band, keine spätere Einführung)."""
    zens = [rk for rk, v in e.items() if START[rk] >= 7 and v == START[rk] and any(w < START[rk] for o, w in e.items() if o != rk)]
    return {rk: v for rk, v in e.items() if rk not in zens}, zens

def spanne(d):
    if not d: return None
    lo, hi = min(d.values()), max(d.values())
    return f'Kl. {lo}' if lo == hi else f'Kl. {lo}–{hi}'

def zusammenfassung(label, reihen, einf, e):
    teile = []
    for rk in reihen:
        n = REIHEN[rk]['name']
        if rk in einf:
            teile.append(f'{n} {", ".join(str(k) for k in einf[rk])}')
        else:
            teile.append(f'{n} –')
    eff, zens = wirksam(e)
    s = spanne(eff)
    if not s:
        return f'{label}: keine Stelle ({", ".join(teile)})'
    txt = f'{label}: {s} ({", ".join(teile)})'
    if '–' in s:
        lo = min(eff.values())
        spaeter = [f'{REIHEN[rk]["name"]} {v}' for rk, v in eff.items() if v != lo]
        txt += f'; Streuung der Einführung: {", ".join(spaeter)} später als Kl. {lo}'
    if zens:
        txt += '; nicht in die Spanne gerechnet: ' + ', '.join(f'{REIHEN[rk]["name"]} {e[rk]}' for rk in zens) + \
               ' (Reihe beginnt in Klasse 7, Bände 5/6 für BE/BB nicht erschienen)'
    return txt

def standardgrund(key, rk, fruehest=None):
    e, nr = unit_split(key)
    u = einheiten(e)[nr - 1]
    if 'Sek II' in u['text'][:120]:
        return 'Sek-II-Einheit; die Verzeichnisse reichen bis Klasse 10'
    klassen = sorted({klassenzahl(k) for d in REIHEN[rk]['dateien'] for (_, _, k) in lade(d)[1]})
    if fruehest is not None and fruehest < klassen[0]:
        if rk == 'FDM17':
            return (f'Thema liegt vor dem ersten Band der Nebenquelle (Datei Kl. {klassen[0]}–{klassen[-1]}); '
                    f'andere Reihen führen es ab Kl. {fruehest}')
        return (f'Thema liegt vor dem ersten Band: die Reihe beginnt in Klasse {klassen[0]} (Bände 5/6 für BE/BB '
                f'nicht erschienen); andere Reihen führen es ab Kl. {fruehest}')
    return (f'Reihe führt das Thema in keinem Band als Kapitel- oder Unterkapitelzeile '
            f'(Verzeichnisse Kl. {klassen[0]}–{klassen[-1]})')

KOPF = '''# Klassenbelege je Lerneinheit aus den Lehrwerken (Sekundarstufe I)
Stand {datum}, Katalog auf Commit {head} (letzte Änderung an den 29 Einträgen: {kat}).
Erzeugt im Auftrag `archiv/auftrag-nacht-2026-09-25.md` (Teil 2) aus den 29 Sek-I-Einträgen (`katalog/index.md`, Tabelle Sekundarstufe I) und den Inhaltsverzeichnissen der Regelreihen und Förderhefte unter `quellen/`; abgeleitet, nie von Hand ändern. Vorschlagsliste für die Zeitachse (`ziel.md` § 1): in welcher Klasse die Lehrwerke der Oberschule und die des Gymnasiums eine Lerneinheit führen – am Typ, wo ein Verzeichnis ihn nennt, sonst an der Einheit –, samt Verlagsmarken für „nicht für alle“ und den Förderheften. Kein Eintrag wird geändert, nichts wird entschieden; „keine Stelle“ ist ein Ergebnis, kein Mangel.

Verzeichnisse (Dateien unter `quellen/`, Klassenumfang):
- Oberschule (OS):
  - Sekundo (Westermann, Ausgabe 2017 Berlin/Brandenburg): `quelle-westermann-sekundo-bb-2017-inhalt.txt`, Kl. 7–10. Bände 5/6 sind für BE/BB nicht erschienen (`quellen/lehrwerke-fundliste.md` Teil 3).
  - Mathematik 2023 (Westermann, BE/BB/ST/TH): `quelle-westermann-mathematik2023-bebbstth-inhalt.txt`, Kl. 7–10, und `quelle-westermann-mathematik2022-bebbstth-kl5-6-inhalt.txt`, Kl. 5–6 (Ausgabe 2022 derselben Reihe).
  - Schnittpunkt Mathematik (Klett, Differenzierende Ausgabe ab 2017): `quelle-klett-schnittpunkt-mathematik-diff2017-inhalt.txt`, Kl. 7–10, und `quelle-klett-schnittpunkt-mathematik-diff2017-kl5-6-inhalt.txt`, Kl. 5–6.
  - Mathematik heute (Westermann, BE/BB): `quelle-westermann-mathematikheute-bebb-inhalt.txt`, Kl. 7–10, und `quelle-westermann-mathematikheute-bebb-kl5-6-inhalt.txt`, Kl. 5–6 (Ausgabe 2014 für die Grundschule; Kl. 5 aus dem Lösungsband, die Seiten sind die des Lösungsbands).
- Gymnasium (GYM):
  - Lambacher Schweizer (Klett): `quelle-klett-fahrplan-ls-aa-berlin-2024.txt`, Kl. 5–10, Kapitel und Lerneinheiten ohne Seiten (Kapitelübersicht Zeilen 21–244; Klasse 5: 21–78, 6: 79–113, 7: 114–144, 8: 145–177, 9: 178–213, 10: 214–244). Eine Landesausgabe BE/BB mit Inhaltsverzeichnis gibt es in der DNB nicht (Teil 1 des Auftrags); der Fahrplan gilt als Verzeichnis.
  - Fundamente der Mathematik (Cornelsen, Ausgabe B 2024): `quelle-cornelsen-fundamente-bb-ausgabeb2024-inhalt.txt`, Kl. 7–10, und `quelle-cornelsen-fundamente-bb-ausgabeb2024-kl5-6-inhalt.txt`, Kl. 5–6.
  - Fundamente der Mathematik, Ausgabe B 2017 (Vorgängerausgabe): `quelle-cornelsen-fundamente-bb-ausgabeb2017-inhalt.txt`, Kl. 7–10 – Nebenquelle: ihre Zeilen stehen da, sie zählt nicht in Zusammenfassung, Spanne, Boden und Zahlenblock.
  - Elemente der Mathematik (Westermann, Brandenburg): `quelle-westermann-elemente-der-mathematik-bb-2016u2025-inhalt.txt`, Ausgabe 2016 Kl. 7–10 und Ausgabe 2025 Kl. 5–7 (Klasse 7 aus beiden Ausgaben).
  - mathe.delta (C.C. Buchner, Berlin/Brandenburg ab 2016): `quelle-buchner-mathedelta-bb-2016-inhalt.txt`, Kl. 7–10; Bände 5/6 nicht erschienen. Kl. 8 Kapitel 5–6 nur aus dem Stoffverteilungsplan des Verlags (ohne Seiten; das DNB-Verzeichnis endet mit Kapitel 4). Die Reihe fehlt in der Aufzählung des Auftrags und ist als vierte Gymnasialreihe aufgenommen (Teil 1).
- Förderhefte (Sorte „Förderheft“ in `quellen/foerderhefte-fundliste.md`): Sekundo `quelle-westermann-sekundo-foerder-be_bb2017-inhalt.txt`, Kl. 5–9; Schnittpunkt `quelle-klett-schnittpunkt-foerder-diff2017-inhalt.txt`, Kl. 5–10; Mathematik 2023 `quelle-westermann-mathematik2023-foerder-bebbstth-inhalt.txt`, Kl. 7–9; Mathematik heute „Diagnose und Fördern“ `quelle-westermann-mathematikheute-diagnoseundfoerdern-inhalt.txt`, Kl. 7–10 (nur Themenblöcke des Schülerbands).
- Stoffverteilungsplan als Gegenprobe: `quelle-westermann-sekundo-bb-2017.txt` [SEKUNDO-BB] für das Zusatzstoff-Kennzeichen „*“ (Zeilen 14, 643, 1310, 2064: „Zusatzstoff … gekennzeichnet (*)“).

Lesart:
- Eine Lerneinheit ist einer Reihe zugeordnet, wenn eine Kapitel- oder Unterkapitelzeile eines Verzeichnisses ihren Inhalt nennt; maßgeblich ist der Inhalt, nicht der Wortlaut. Das Zitat ist die Verzeichniszeile wortgleich aus der Quelldatei, auch mit deren Trennfugen und Erkennungsfehlern (etwa „Thaies“ für „Thales“); nur Führungspunkte, Seitenzahl und Leerraum sind herausgenommen, eine umbrochene Zeile ist zusammengesetzt. „S.“ ist die Seite laut Verzeichnis, „Z.“ die Zeilennummer der Quelldatei (zwei Nummern bei umbrochener Zeile). Beim Lambacher Schweizer steht die Kapitelzeile vor der Lerneinheit: „Kapitel …“ (Z.) › „Lerneinheit“ (Z.).
- Führt eine Reihe den Inhalt in mehreren Klassen (Einführung, Erweiterung, Wiederaufnahme, wortgleiches Kapitel in zwei Bänden), stehen alle Stellen da.
- Typzeile „Typ: <Typname> – <Reihe> Kl. n, S. x: „<Zeile>““, wenn die Zeile einen einzelnen Typ der Einheit nennt; der Typname ist wortgleich aus „Typen je Lerneinheit“ des Eintrags und wurde beim Bau dort nachgeschlagen.
- Marken: jede zitierte Zeile, die mit einem Markenwort beginnt (LVL, Vertiefen, Üben, EXTRA, Streifzug, Exkursion, Themenseite, Werkzeug, Mathematisch arbeiten, Mit Medien arbeiten, Arbeiten mit dem Computer, Im Blickpunkt, Projekt, Wissen kompakt, Bleib fit, Diagnosetest, Training, Vertiefung, Sonderfälle) oder „Zum Selbstlernen“ bzw. „Wiederholung“ enthält; dazu Kennzeichen außerhalb der Zeile: ein Kapitel, das sich als Wiederholung ausweist; Zeichen vor der Zeile, die das Verzeichnis nicht erklärt („Symbolzeichen“, Sekundo und Elemente); das Zusatzstoff-Kennzeichen „*“ aus [SEKUNDO-BB] mit Zeile; „(fakultativ)“ im Stoffverteilungsplan von mathe.delta.
- „keine Stelle“ mit Grund: Sek-II-Einheit; Thema liegt vor dem ersten Band (Reihe beginnt in Klasse 7, andere Reihen führen es früher); sonst führt die Reihe das Thema in keinem Band als Kapitel- oder Unterkapitelzeile. Kein Verzeichnis war für eine Klasse als Ganzes unlesbar, „nicht lesbar“ kommt deshalb nicht vor; verstümmelte Einzelzeilen (Texterkennung) sind wortgleich zitiert und mit „Ermessen:“ gelesen.
- Förderheft: je Stelle eine Zeile mit der Seite des Förderhefts; „Förderheft: keine Stelle“, wenn keines der vier Hefte die Einheit nennt. Mathematik heute „Diagnose und Fördern“ gliedert nur nach Themenblöcken; ein Block ist den Einheiten zugeordnet, die sein Titel nennt (deckt der Titel das ganze Thema des Eintrags, allen Sek-I-Einheiten), das ist Ermessen und steht je Block einmal in der Ermessensliste des Eintrags. Der Block „Ebene Geometrie (Schülerband Seite 72 bis 113)“ (Kl. 8, Z. 46) nennt keinen Inhalt einer Einheit und ist nicht zugeordnet.
- Zusammenfassung je Einheit: Einführungsklasse einer Reihe ist die kleinste Klasse mit Stelle. „OS: Kl. n“ bzw. „GYM: Kl. n“, wenn alle Reihen der Schulform in derselben Klasse einführen, sonst die Spanne („Kl. 9–10“) mit dem Grund (welche Reihen später einführen); in Klammern alle Klassen je Reihe, „–“ ohne Stelle. Sekundo und mathe.delta beginnen in Klasse 7: ihre 7 zählt nicht in die Spanne, wenn eine andere Reihe derselben Schulform früher einführt (erster Band, keine spätere Einführung), und steht dann als „nicht in die Spanne gerechnet“.
- Spanne OS/GYM je Eintrag: ja, wenn für mindestens eine Einheit die Angabe „OS: Kl. …“ und die Angabe „GYM: Kl. …“ verschieden sind (Einheiten mit Stelle nur in einer Schulform zählen nicht); in Klammern die Einheiten, „ohne gemeinsame Klasse“ markiert die, bei denen sich OS- und GYM-Angabe nicht überschneiden.
- Boden je Eintrag: ja, wenn eine Einheit in einer Regelreihe schon in Klasse 5 oder 6 steht.
- „Ermessen:“ steht an der Zeile, deren Zuordnung eine Auslegung verlangt, und gesammelt am Schluss des Eintrags; Einträge ohne Einzelstelle („Ermessen:“ direkt unter der Einheit) betreffen die ganze Einheit.
- Reihenfolge der Abschnitte wie die Tabelle Sekundarstufe I in `katalog/index.md`; Verortung = erster Satz des Abschnitts „### Verortung“, der eine Klasse nennt.
'''

def git(*args):
    """git aus dem PATH, sonst das git von GitHub Desktop; ohne git: None."""
    for g in ['git'] + sorted(glob.glob(os.path.expandvars(r'%LOCALAPPDATA%\GitHubDesktop\app-*\resources\app\git\cmd\git.exe'))):
        try:
            return subprocess.run([g, '-C', REPO, '-c', 'core.pager=cat'] + list(args), capture_output=True, text=True,
                                  encoding='utf-8', check=True).stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            continue
    return None

def eingaben():
    pfade = ['katalog/index.md'] + [f'katalog/{e}.md' for e in EINTRAEGE]
    pfade += sorted({f'quellen/{d}' for v in REIHEN.values() for d in v['dateien']})
    return pfade

def typenliste():
    zeilen = ['# Typenliste zu werkzeuge/klassen-belege-daten.py – abgeleitet von werkzeuge/klassen-belege.py aus dem Abschnitt',
              '# „Typen je Lerneinheit“ der 29 Sek-I-Einträge; nie von Hand ändern. Je Einheit die Typzeile wortgleich mit',
              '# Zeilennummer im Eintrag; ein typ=… in den Daten muss wortgleich am Zeilenanfang oder hinter „ · “ stehen',
              '# („ · “ trennt die Typen, kommt aber auch als Malpunkt vor – maßgeblich ist der Wortlaut).', '']
    for e in EINTRAEGE:
        zeilen.append(f'## {e}')
        for zi, l in KATALOG['daten'][e + '.md']['typen']:
            m = re.match(r'^\s*[-*]?\s*Einheit (\d+):\s*(.*)$', l)
            if m:
                zeilen.append(f'E{m.group(1)} (Z. {zi}): {m.group(2).strip()}')
        zeilen.append('')
    return '\n'.join(zeilen).rstrip('\n') + '\n'

def schreibe(E_, probe=False):
    stat = E_['stat']
    ne = len(EINTRAEGE)
    alle = EINTRAEGE
    sp = E_['spanne_ja']; bo = E_['boden_ja']; gt = E_['getrennt_ja']
    nein = [e for e in alle if e not in sp]
    bnein = [e for e in alle if e not in bo]
    zit = sum(len([z for z in r['zeilen'] if z]) + (1 if r['kap'] else 0) for r in REFS)
    typen = sum(len(r['typ']) for r in REFS)
    haupt = [r for r in REFS if REIHEN[r['reihe']]['form'] != 'F']
    foerder = [r for r in REFS if REIHEN[r['reihe']]['form'] == 'F']
    z = ['## Zahlen',
         f'Einträge gesamt: {ne} (die {ne} Sek-I-Einträge aus `katalog/index.md`, Tabelle Sekundarstufe I).',
         f'Lerneinheiten gesamt: {stat["einheiten"]}; mit mindestens einer Stelle in einer OS-Reihe: {stat["os"]}, '
         f'in einer GYM-Reihe: {stat["gym"]}, in beiden: {stat["beide"]}, in keiner: {stat.get("keine", 0)}'
         + (f' ({", ".join(E_["ohne"])})' if E_['ohne'] else '') + '.'
         + (f' Ohne GYM-Stelle: {", ".join(E_["ohne_gym"])}.' if E_.get('ohne_gym') else ''),
         f'Einträge mit Spanne OS/GYM ja: {len(sp)} ({", ".join(sp)}); davon mit mindestens einer Einheit ohne gemeinsame Klasse: {len(gt)} ({", ".join(gt)}).',
         f'Einträge mit Spanne OS/GYM nein: {len(nein)} ({", ".join(nein)}).',
         f'Einheiten mit verschiedener OS- und GYM-Angabe: {len(E_["spanne_einheiten"])}.',
         f'Einträge mit Boden ja: {len(bo)} ({", ".join(bo)}).',
         f'Einträge mit Boden nein: {len(bnein)} ({", ".join(bnein)}).',
         f'Typzeilen gesamt: {E_["typzeilen"]}.',
         f'Ermessensfälle gesamt: {E_["ermessen"]} in {sum(1 for v in E_["erm_je"].values() if v)} Einträgen ('
         + ', '.join(f'{e} {v}' for e, v in E_['erm_je'].items()) + ').',
         f'Förderheftzeilen gesamt: {E_["foerder_zeilen"]}; Einheiten mit mindestens einer Förderheftstelle: {E_["foerder_einheiten"]} von {stat["einheiten"]}.',
         'Verlagsmarken (Nennungen): ' + ', '.join(f'{m} {n}' for m, n in E_['marken'].most_common()) + '.',
         f'Geprüfte Zitate beim Bau: {zit} Verzeichniszeilen in {len(haupt)} Regelreihen- und {len(foerder)} Förderheftzuordnungen, {typen} Typnamen.',
         '']
    stand = git('log', '-1', '--format=%cs %h', '--', *eingaben())
    kat = git('log', '-1', '--format=%h vom %ad', '--date=short', '--', *[f'katalog/{e}.md' for e in EINTRAEGE])
    if not stand or not kat:
        sys.exit('git nicht gefunden oder Eingaben ohne Commit – Stand-Zeile nicht bestimmbar, nichts geschrieben')
    datum, head = stand.split()
    text = KOPF.format(datum=datum, head=head, kat=kat) + '\n' + '\n'.join(z) + '\n' + '\n\n'.join(E_['abschnitte']) + '\n'
    assert '\r' not in text
    ziel = os.path.join(KAT, '_klassen-belege.md')
    if probe:
        alt = open(ziel, encoding='utf-8').read() if os.path.exists(ziel) else ''
        print('Probe:', 'gleich der vorhandenen Datei' if alt == text else 'weicht von der vorhandenen Datei ab', '– nichts geschrieben')
        return
    for pfad, inhalt in ((ziel, text), (TYPENLISTE, typenliste())):
        with open(pfad, 'w', encoding='utf-8', newline='\n') as f:
            f.write(inhalt)
        roh = open(pfad, 'rb').read()
        assert not roh.startswith(b'\xef\xbb\xbf') and b'\r' not in roh
        print('geschrieben', os.path.relpath(pfad, REPO), len(roh), 'Bytes', inhalt.count('\n'), 'Zeilen')

if __name__ == '__main__':
    E_ = main()
    stat = E_['stat']
    print('Einheiten', stat['einheiten'], 'OS', stat['os'], 'GYM', stat['gym'], 'beide', stat['beide'],
          '| Spanne ja', len(E_['spanne_ja']), 'Boden ja', len(E_['boden_ja']), '| Typzeilen', E_['typzeilen'],
          'Ermessen', E_['ermessen'], 'Förderheftzeilen', E_['foerder_zeilen'])
    schreibe(E_, probe='--probe' in sys.argv[1:])
