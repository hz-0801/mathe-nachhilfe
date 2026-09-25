"""Sek-II-Ordnung nach Halbjahr und Kursart je Lerneinheit (v0.1, 26.09.2026).

Für die Oberstufe ordnen Halbjahr und Kursart statt der Klasse (ziel.md § 5). Schreibt
katalog/_sek2-ordnung-belege.md nach dem Muster von katalog/_klassen-belege.md: je Sek-II-Eintrag und
Lerneinheit die Stellen im Rahmenlehrplan (Kurshalbjahr, Grund- oder Leistungskurs) und in den
Lehrwerken (Band, Kapitelzeile wortgleich, Seite, Zeilennummer), die Zusammenfassung „Halbjahr: … · GK/LK: …“
und „nur LK: ja/nein“, Ermessen mit Grund; „keine Stelle“ ist ein Ergebnis. Ändert keinen Eintrag.

Aufruf aus der Repo-Wurzel: python werkzeuge/sek2-ordnung-belege.py  (--probe: bauen, vergleichen, nicht
schreiben). Bei einem Prüffehler (Zeilennummer, Quelle, Einheit) wird nichts geschrieben.

Eingaben und Lesart
- Einträge: Tabelle Sekundarstufe II in katalog/index.md (44), dazu die Sek-II-Einheiten der Sek-I-Einträge
  (Titel mit „(Sek II)“: daten Einheit 6, lineare-gleichungssysteme Einheit 5).
- Rahmenlehrplan GOST (quellen/quelle-rlp-gost-be-2022-mathematik.txt, …-bb-2022-…): die Stellen je Einheit
  übernimmt das Skript aus katalog/_kursart-belege.md (Auftrag Niveaustufen-Belege, 24.09.2026; dort an den
  Quelltexten geprüft, mit Block und Ermessen) und liest selbst am Quelltext nach: Berlin – das Kurshalbjahr
  in der Spalte „Khj“ am rechten Rand der Standardzeile (am Ende des Standards; „Q1/2“ = Q1 oder Q2), der Block
  „Grundkursfach und Leistungskursfach“ oder „Zusätzlich: Leistungskursfach“ darüber; Brandenburg – das
  Kurshalbjahr Q1–Q4 aus dem Abschnitt, in dem die Zeile steht, der Block „Grund- und Leistungskursfach“ oder
  „Zusätzlich im Leistungskursfach“ darüber. Für Einheiten ohne Stelle dort (Sek-II-Einheiten der
  Sek-I-Einträge) und für Ergänzungen: Daten R.
- FOS (quellen/quelle-rlp-fos-bb-2019-mathematik.txt): die Zitate hinter „FOS“ in der Zeile der Lerneinheit
  (Abschnitt „Lerneinheiten“ des Eintrags), am Quelltext gesucht; Ort = Themenfeld 1–8 (Pflicht- oder
  Wahlthema). Die Fachoberschule ist einjährig und kennt kein Kurshalbjahr und keine Kursart.
- Lehrwerke (Zuordnungsdaten werkzeuge/sek2-ordnung-belege-daten.py, L = Zeile, K = keine Stelle mit Grund):
  Bigalke/Köhler Brandenburg (Bände GK 11, LK 11, GK 12, LK 12; Reihenfolge-Quelle, keine Form-Quelle,
  Beschluss 25.09.2026), Fundamente Sek II Ausgabe B (nur Einführungsphase im Repo), Elemente Sek II
  (NRW, nur Gegenprobe), Neue Wege Sek II Berlin 2011 (nur Gegenprobe). Zitiert wird die Kapitelzeile
  wortgleich ohne Führungspunkte und Seitenzahl, davor die Kapitelüberschrift („…“ › „…“), S. = Seite laut
  Verzeichnis, Z. = Zeilennummer der Quelldatei.
- Zusammenfassung je Einheit: „Halbjahr:“ nennt die Kurshalbjahre beider Pläne (gleich: einmal) und die
  Bigalke/Köhler-Bände; „GK/LK:“ die Blöcke beider Pläne und die Bigalke/Köhler-Kursbände. „nur LK: ja“,
  wenn jede Planstelle der Einheit im Leistungskurszusatz steht (mindestens eine Stelle) oder wenn
  Bigalke/Köhler die Einheit nur in den LK-Bänden führt (in LK 11 oder LK 12, in keinem GK-Band).

Entstanden im Auftrag Nacht 2026-09-26, Teil 3.
"""
import os
import re
import subprocess
import sys
from collections import OrderedDict, defaultdict

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
DATEN = os.environ.get('SOB_DATEN') or os.path.join(HIER, 'sek2-ordnung-belege-daten.py')
AUSGABE = os.path.join(REPO, 'katalog', '_sek2-ordnung-belege.md')

Q = os.path.join(REPO, 'quellen')
PLAN_BE = os.path.join(Q, 'quelle-rlp-gost-be-2022-mathematik.txt')
PLAN_BB = os.path.join(Q, 'quelle-rlp-gost-bb-2022-mathematik.txt')
PLAN_FOS = os.path.join(Q, 'quelle-rlp-fos-bb-2019-mathematik.txt')
LEHRWERKE = OrderedDict([
    ('BK', dict(name='Bigalke/Köhler', datei='quelle-cornelsen-bigalkekoehler-sek2-bebb-inhalt.txt', rolle='Reihenfolge', keine='in keinem Band')),
    ('FDM', dict(name='Fundamente Sek II B', datei='quelle-cornelsen-fundamente-sek2-ausgabeb-inhalt.txt', rolle='BE/BB', keine='nicht in der Einführungsphase; die Bände der Qualifikationsphase sind nicht im Repo (quellen/lehrwerke-fundliste.md)')),
    ('EDM', dict(name='Elemente Sek II NRW', datei='quelle-westermann-elemente-der-mathematik-sek2-nrw-inhalt.txt', rolle='Gegenprobe')),
    ('NW', dict(name='Neue Wege Sek II Berlin 2011', datei='quelle-westermann-mathematikneuewege-sek2-berlin2011-inhalt.txt', rolle='Gegenprobe')),
])
BANDNAMEN = {
    'Band 11 Grundkurs': 'GK 11', 'Band 11 Leistungskurs': 'LK 11', 'Band 12 Grundkurs': 'GK 12',
    'Band 12 Leistungskurs': 'LK 12',
    'Aufgaben zur Abiturvorbereitung (Hilfsmittelfreie und komplexe Aufgaben)': 'Abiturvorbereitung',
    'Einfuehrungsphase': 'Einführungsphase', 'Qualifikationsphase Grundkurs': 'Q-Phase GK',
    'Qualifikationsphase Leistungskurs': 'Q-Phase LK', 'Analysis': 'Analysis',
    'Lineare Algebra, Analytische Geometrie': 'Lineare Algebra/Analytische Geometrie', 'Stochastik': 'Stochastik',
}
BB_HALBJAHRE = [(864, 'Q1'), (1030, 'Q2'), (1196, 'Q3'), (1313, 'Q4')]
FOS_FELDER = [(1024, '1 Elementare Funktionsuntersuchungen (Pflichtthema)'), (1079, '2 Differentialrechnung (Pflichtthema)'),
              (1123, '3 Integralrechnung (Pflichtthema)'), (1165, '4 Stochastik (Pflichtthema)'),
              (1198, '5 Analytische Geometrie (Wahlthema)'), (1226, '6 Zahlenfolgen (Wahlthema)'),
              (1245, '7 Anwendungen ökonomischer Funktionen (Wahlthema)'), (1263, '8 Freies Projekt (Wahlthema)')]
KHJ = re.compile(r'\s(Q[1-4](?:/[1-4])*)\s*$')


def lies_zeilen(pfad):
    with open(pfad, encoding='utf-8') as f:
        return f.read().split('\n')


def lies(*teile):
    with open(os.path.join(REPO, *teile), encoding='utf-8') as f:
        return f.read()


def norm(s):
    s = s.replace('­', '').replace('\f', ' ')
    s = re.sub(r'(?:\s*[.·]){2,}', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


# ---------------------------------------------------------------- Einträge

def sek2_eintraege():
    zeilen = lies('katalog', 'index.md').split('\n')
    bereich, liste, sek1 = None, [], []
    for z in zeilen:
        if z.startswith('## Sekundarstufe II'):
            bereich = 2
        elif z.startswith('## Sekundarstufe I'):
            bereich = 1
        elif z.startswith('## '):
            bereich = None
        m = re.match(r'^\| ([a-z0-9-]+)\.md \|', z)
        if m and bereich == 2:
            liste.append(m.group(1))
        elif m and bereich == 1:
            sek1.append(m.group(1))
    return liste, sek1


def lerneinheiten(name):
    zeilen = lies('katalog', name + '.md').split('\n')
    einheiten, drin = OrderedDict(), False
    for i, z in enumerate(zeilen, 1):
        if z.startswith('### Lerneinheiten'):
            drin = True
            continue
        if drin and z.startswith('### '):
            break
        m = re.match(r'^(\d+)\.\s+(.+?)(?:\s+–\s+|$)', z) if drin else None
        if m:
            einheiten[int(m.group(1))] = {'titel': m.group(2).strip(), 'zeile': i, 'text': z}
    return einheiten


# ---------------------------------------------------------------- Kursart-Belege (Planstellen)

def kursart_stellen():
    """{(eintrag, einheit): {'eintrag': (zeile, text) , 'BE': [...], 'BB': [...], 'erm': [...]}}."""
    zeilen = lies('katalog', '_kursart-belege.md').split('\n')
    d = defaultdict(lambda: {'marke': None, 'BE': [], 'BB': [], 'BE_keine': False, 'BB_keine': False, 'erm': []})
    eintrag, einheit, letzte = None, None, None
    for i, z in enumerate(zeilen):
        m = re.match(r'^### (\S+)$', z)
        if m:
            eintrag, einheit = m.group(1), None
            continue
        m = re.match(r'^  - (\d+)\. ', z)
        if m and eintrag:
            einheit = int(m.group(1))
            continue
        if z.startswith('- ') and not z.startswith('- Lerneinheiten'):
            einheit = None
        if not eintrag or einheit is None:
            continue
        e = d[(eintrag, einheit)]
        m = re.match(r'^    - Eintrag, Zeile (\d+): (.*)$', z)
        if m:
            e['marke'] = (int(m.group(1)), m.group(2))
            continue
        m = re.match(r'^    - GOST (Berlin|Brandenburg)(?: \[Zeilen? ([\d–und ]+)\])?: (.*)$', z)
        if m:
            land = 'BE' if m.group(1) == 'Berlin' else 'BB'
            if m.group(3).strip() == 'keine Stelle':
                e[land + '_keine'] = True
                continue
            nummern = [int(x) for x in re.findall(r'\d+', m.group(2) or '')]
            kontext = zeilen[i + 1].strip() if i + 1 < len(zeilen) and zeilen[i + 1].startswith('      ') else ''
            e[land].append({'zeilen': nummern, 'zitat': m.group(3), 'kontext': kontext})
            continue
        m = re.match(r'^    - Ermessen: (.*)$', z)
        if m:
            e['erm'].append(m.group(1))
    return d


def khj_berlin(plan, nummern):
    """Kurshalbjahr am Ende des Standards, der die zitierten Zeilen enthält; (khj, zeile)."""
    start = min(nummern)
    for i in range(start - 1, min(start + 8, len(plan))):
        z = plan[i]
        if i > start - 1 and z.lstrip().startswith('­'):
            break
        m = KHJ.search(z)
        if m:
            return m.group(1), i + 1
    return None, None


def block_oben(plan, zeile, muster):
    for i in range(zeile - 1, -1, -1):
        for name, rx in muster:
            if re.search(rx, plan[i]):
                return name, i + 1
    return None, None


BLOCK_BE = [('Leistungskurszusatz', r'^\s*Zusätzlich: Leistungskursfach'), ('Grund- und Leistungskurs', r'^\s*Grundkursfach und Leistungskursfach')]
BLOCK_BB = [('Leistungskurszusatz', r'^\s*Zusätzlich im Leistungskursfach'), ('Grund- und Leistungskurs', r'^\s*Grund- und Leistungskursfach\s*$')]


def halbjahr_bb(zeile):
    q = None
    for start, name in BB_HALBJAHRE:
        if zeile >= start:
            q = name
    return q


def fos_feld(zeile):
    f = None
    for start, name in FOS_FELDER:
        if zeile >= start:
            f = name
    return f


def fos_zitate(text):
    """Zitate hinter „FOS“ in der Lerneinheitszeile."""
    m = re.search(r'FOS\b(.*?)(?:;\s*(?:OHiMi|GOST|Q\d)|\)\s*(?:←|$))', text)
    if not m:
        return []
    return re.findall(r'„([^“]+)“', m.group(1))


def wortform(tok):
    return re.sub(r'[^\wäöüßÄÖÜ-]', '', tok).lower().strip('-')


_FOS_STROEME = {}


def fos_stroeme(fos):
    """Wortströme der Themenfeld-Tabellen, je Tabelle Spalte „Thema“ und „Inhaltliche Präzisierung“:
    [(wörter, zeilennummern)]; ein Trennstrich am Zeilenende verbindet mit dem nächsten Wort derselben Spalte."""
    if id(fos) in _FOS_STROEME:
        return _FOS_STROEME[id(fos)]
    kopf = [(i, z.index('Inhaltliche'), z.index('Leitideen')) for i, z in enumerate(fos)
            if re.match(r'^\s*Thema\s+Inhaltliche Präzisierung\s+Leitideen', z)]
    stroeme = []
    for t, (start, lm, lr) in enumerate(kopf):
        ende = kopf[t + 1][0] if t + 1 < len(kopf) else len(fos)
        for spalte in ('links', 'mitte'):
            woerter, nummern, offen = [], [], False
            for i in range(start + 1, ende):
                z = fos[i]
                teil = z[:lm - 1] if spalte == 'links' else z[lm - 1:lr - 1]
                toks = teil.split()
                if spalte == 'mitte' and toks and toks[0] == '-':
                    toks = toks[1:]
                for j, tok in enumerate(toks):
                    w = wortform(tok)
                    if not w:
                        continue
                    if offen and j == 0 and tok[:1].islower():
                        woerter[-1] = woerter[-1] + w
                    else:
                        woerter.append(w)
                        nummern.append(i + 1)
                    offen = False
                offen = bool(toks) and toks[-1].endswith('-') and not toks[-1].endswith('--')
            stroeme.append((woerter, nummern))
    _FOS_STROEME[id(fos)] = stroeme
    return stroeme


def suche_fos(fos, zitat):
    """Fundstelle (erste, letzte Zeile) eines Zitats; Stücke um „…“ in dieser Folge mit höchstens 12 Wörtern
    Abstand; zuerst in der Spalte „Inhaltliche Präzisierung“, dann in der Spalte „Thema“."""
    stuecke = [[w for w in (wortform(t) for t in s.split()) if w] for s in zitat.split('…')]
    stuecke = [s for s in stuecke if s]
    if not stuecke:
        return None
    stroeme = fos_stroeme(fos)
    for woerter, nummern in stroeme[1::2] + stroeme[0::2]:
        for i in range(len(woerter)):
            pos, ok = i, True
            for k, s in enumerate(stuecke):
                grenze = pos + (1 if k == 0 else 13)
                treffer = next((p for p in range(pos, min(grenze, len(woerter) - len(s) + 1))
                                if woerter[p:p + len(s)] == s), None)
                if treffer is None:
                    ok = False
                    break
                pos = treffer + len(s)
            if ok:
                return nummern[i], nummern[pos - 1]
    return None


# ---------------------------------------------------------------- Lehrwerke

def lehrwerk_zeilen():
    """{kürzel: {zeile: dict(band, kapitel, text, seite, kapzeile)}}."""
    alle = {}
    for k, w in LEHRWERKE.items():
        zeilen = lies_zeilen(os.path.join(Q, w['datei']))
        band, kapitel, kapzeile = None, None, None
        info = {}
        for i, z in enumerate(zeilen, 1):
            m = re.match(r'^== (.+) ==$', z)
            if m:
                band, kapitel = BANDNAMEN.get(m.group(1), m.group(1)), None
                continue
            if not band or not z.strip():
                continue
            text = norm(re.sub(r'\s*\(Seitenangabe im Rohtext unklar\)\s*$', '', z))
            seite = None
            m = re.search(r'\s(\d{1,3})\s*$', text)
            if m:
                seite = m.group(1)
                text = text[:m.start()].strip()
            text = re.sub(r'\s*\.+\s*$', '', text).strip()
            ist_kapitel = False
            if k == 'BK':
                ist_kapitel = bool(re.match(r'^[IVX]+\. ', z))
            elif k == 'FDM':
                ist_kapitel = bool(re.match(r'^\d+\s+[/I]\s', z))
            elif k == 'EDM':
                ist_kapitel = bool(re.match(r'^\d+ \S', z)) or z.startswith('Vorbereiten')
            elif k == 'NW':
                ist_kapitel = z.startswith('Kapitel ')
            if ist_kapitel:
                kapitel, kapzeile = text, i
                if k == 'NW':
                    kapitel = re.sub(r'^Kapitel (\d+)\s+', r'Kapitel \1 ', kapitel)
            info[i] = dict(band=band, kapitel=kapitel, kapzeile=kapzeile, text=text, seite=seite, ist_kapitel=ist_kapitel)
        alle[k] = info
    return alle


class Daten:
    def __init__(self):
        self.L = defaultdict(list)
        self.K = {}
        self.R = defaultdict(list)
        self.E = defaultdict(list)

    def lade(self):
        if os.path.exists(DATEN):
            with open(DATEN, encoding='utf-8') as f:
                exec(compile(f.read(), DATEN, 'exec'),
                     {'L': self.l, 'K': self.k, 'R': self.r, 'E': self.e})
        return self

    def l(self, eintrag, einheit, quelle, zeilen, erm=''):
        if isinstance(zeilen, int):
            zeilen = [zeilen]
        for i, z in enumerate(zeilen):
            self.L[(eintrag, einheit)].append((quelle, z, erm if i == 0 else ''))

    def k(self, eintrag, einheit, quelle, grund):
        self.K[(eintrag, einheit, quelle)] = grund

    def r(self, eintrag, einheit, plan, von, bis=None, zitat='', erm=''):
        self.R[(eintrag, einheit)].append((plan, von, bis or von, zitat, erm))

    def e(self, eintrag, einheit, text):
        self.E[(eintrag, einheit)].append(text)


# ---------------------------------------------------------------- Bau

def baue():
    fehler = []
    sek2, sek1 = sek2_eintraege()
    plan_be, plan_bb, fos = lies_zeilen(PLAN_BE), lies_zeilen(PLAN_BB), lies_zeilen(PLAN_FOS)
    ks = kursart_stellen()
    lw = lehrwerk_zeilen()
    daten = Daten().lade()
    eintraege = OrderedDict()
    for name in sek2:
        eintraege[name] = [(n, e) for n, e in lerneinheiten(name).items()]
    for name in sek1:
        s2 = [(n, e) for n, e in lerneinheiten(name).items() if 'Sek II' in e['titel']]
        if s2:
            eintraege[name] = s2

    gueltig = {(name, n) for name, liste in eintraege.items() for n, _ in liste}
    for key in list(daten.L) + list(daten.R) + list(daten.E) + [(a, b) for a, b, _ in daten.K]:
        if key not in gueltig:
            fehler.append(f'Daten: Einheit {key[0]} {key[1]} gibt es nicht (oder nicht Sek II)')

    ergebnis = OrderedDict()
    for name, liste in eintraege.items():
        einheiten = []
        for n, e in liste:
            k = ks.get((name, n), {'marke': None, 'BE': [], 'BB': [], 'BE_keine': True, 'BB_keine': True, 'erm': []})
            stellen = {'BE': [], 'BB': [], 'FOS': []}
            erm = list(k['erm'])
            for land, plan, bl in (('BE', plan_be, BLOCK_BE), ('BB', plan_bb, BLOCK_BB)):
                for s in k[land]:
                    zeile = min(s['zeilen'])
                    if land == 'BE':
                        khj, kz = khj_berlin(plan, s['zeilen'])
                    else:
                        khj, kz = halbjahr_bb(zeile), None
                    block, _ = block_oben(plan, zeile, bl)
                    stellen[land].append(dict(zeilen=s['zeilen'], zitat=s['zitat'], khj=khj, khj_zeile=kz, block=block))
            for plan_k, von, bis, zitat_d, e_text in daten.R.get((name, n), []):
                plan = {'BE': plan_be, 'BB': plan_bb, 'FOS': fos}.get(plan_k)
                if plan is None or not (1 <= von <= bis <= len(plan)):
                    fehler.append(f'R: {name} {n}: Plan {plan_k} Zeilen {von}–{bis} ungültig')
                    continue
                roh = ' '.join(norm(plan[i - 1]) for i in range(von, bis + 1))
                if zitat_d:
                    if norm(zitat_d) not in roh:
                        fehler.append(f'R: {name} {n}: Zitat „{zitat_d}“ steht nicht in {plan_k} Z. {von}–{bis}')
                        continue
                    zitat = f'„{zitat_d}“'
                else:
                    zitat = '„' + roh.lstrip('­–- ').strip() + '“'
                if plan_k == 'BE':
                    khj, kz = khj_berlin(plan, [von, bis])
                    block, _ = block_oben(plan, von, BLOCK_BE)
                    stellen['BE'].append(dict(zeilen=[von, bis] if bis != von else [von], zitat=zitat, khj=khj, khj_zeile=kz, block=block))
                elif plan_k == 'BB':
                    block, _ = block_oben(plan, von, BLOCK_BB)
                    stellen['BB'].append(dict(zeilen=[von, bis] if bis != von else [von], zitat=zitat, khj=halbjahr_bb(von), khj_zeile=None, block=block))
                else:
                    stellen['FOS'].append(dict(zeilen=[von, bis] if bis != von else [von], zitat=zitat, feld=fos_feld(von)))
                if e_text:
                    erm.append(e_text)
            fos_offen = []
            for zitat in fos_zitate(e['text']):
                treffer = suche_fos(fos, zitat)
                if treffer:
                    stellen['FOS'].append(dict(zeilen=[treffer[0], treffer[1]] if treffer[1] != treffer[0] else [treffer[0]],
                                               zitat=f'„{zitat}“', feld=fos_feld(treffer[0])))
                else:
                    fos_offen.append(zitat)
            buecher = []
            for quelle, zeile, e_text in daten.L.get((name, n), []):
                if quelle not in lw or zeile not in lw[quelle]:
                    fehler.append(f'L: {name} {n}: {quelle} Zeile {zeile} ist keine Verzeichniszeile')
                    continue
                buecher.append((quelle, zeile, lw[quelle][zeile], e_text))
                if e_text:
                    erm.append(f'{LEHRWERKE[quelle]["name"]}, Z. {zeile}: {e_text}')
            erm += daten.E.get((name, n), [])
            einheiten.append(dict(n=n, titel=e['titel'], zeile=e['zeile'], marke=k['marke'], stellen=stellen,
                                  be_keine=not stellen['BE'], bb_keine=not stellen['BB'], fos_offen=fos_offen,
                                  buecher=buecher, erm=erm,
                                  keine={q: daten.K.get((name, n, q)) for q in LEHRWERKE}))
        ergebnis[name] = einheiten
    return fehler, ergebnis


# ---------------------------------------------------------------- Zusammenfassung

def khj_menge(k):
    if not k:
        return set()
    m = re.match(r'Q(\d)((?:/\d)*)', k)
    return {f'Q{m.group(1)}'} | {f'Q{x}' for x in re.findall(r'\d', m.group(2))}


def zusammenfassung(u):
    be = sorted(set().union(*[khj_menge(s['khj']) for s in u['stellen']['BE']])) if u['stellen']['BE'] else []
    bb = sorted({s['khj'] for s in u['stellen']['BB'] if s['khj']})
    bk_baende = sorted({b[2]['band'] for b in u['buecher'] if b[0] == 'BK' and b[2]['band'] in ('GK 11', 'LK 11', 'GK 12', 'LK 12')},
                       key=lambda x: (x[3:], x[:2]))
    teile = []
    if be and be == bb:
        teile.append(f"{'/'.join(be)} (Berlin und Brandenburg)")
    else:
        if be:
            teile.append(f"Berlin {'/'.join(be)}")
        if bb:
            teile.append(f"Brandenburg {'/'.join(bb)}")
    if not be and not bb:
        teile.append('keine Planstelle')
    jahre = sorted({b[3:] for b in bk_baende})
    nur_abi = not bk_baende and any(b[0] == 'BK' and b[2]['band'] == 'Abiturvorbereitung' for b in u['buecher'])
    teile.append('Bigalke/Köhler ' + (f"Band {' und '.join(jahre)}" if jahre
                                      else ('nur im Band Abiturvorbereitung' if nur_abi else 'keine Stelle')))
    halbjahr = ' · '.join(teile)

    def kursart(stellen):
        bl = {s['block'] for s in stellen}
        if not bl:
            return None
        if 'Grund- und Leistungskurs' in bl:
            return 'GK und LK'
        return 'nur LK'
    kbe, kbb = kursart(u['stellen']['BE']), kursart(u['stellen']['BB'])
    k_teile = []
    if kbe and kbe == kbb:
        k_teile.append(f'{kbe} (Berlin und Brandenburg)')
    else:
        if kbe:
            k_teile.append(f'Berlin {kbe}')
        if kbb:
            k_teile.append(f'Brandenburg {kbb}')
    if not kbe and not kbb:
        k_teile.append('keine Planstelle')
    gk_band = any(b.startswith('GK') for b in bk_baende)
    lk_band = any(b.startswith('LK') for b in bk_baende)
    k_teile.append('Bigalke/Köhler ' + (', '.join(bk_baende) if bk_baende
                                        else ('nur Band Abiturvorbereitung' if nur_abi else 'keine Stelle')))
    gklk = ' · '.join(k_teile)
    plan_lk = [k for k in (kbe, kbb) if k]
    nur_lk_plan = bool(plan_lk) and all(k == 'nur LK' for k in plan_lk)
    nur_lk_bk = lk_band and not gk_band
    nur_lk = nur_lk_plan or nur_lk_bk
    grund = []
    if nur_lk_plan:
        grund.append('Plan')
    if nur_lk_bk:
        grund.append('Bigalke/Köhler nur LK-Band')
    laender = kbe and kbb and kbe != kbb
    return halbjahr, gklk, nur_lk, grund, laender, be, bb, bk_baende


def zitat_lehrwerk(quelle, zeile, info):
    w = LEHRWERKE[quelle]
    s = f"{w['name']} {info['band']}" + (f", S. {info['seite']}" if info['seite'] else '')
    if info['ist_kapitel'] or not info['kapitel']:
        return f"{s}: „{info['text']}“ (Z. {zeile})"
    return f"{s}: „{info['kapitel']}“ (Z. {info['kapzeile']}) › „{info['text']}“ (Z. {zeile})"


def stand():
    git = os.environ.get('GIT', 'git')
    eingaben = ['katalog', 'quellen/quelle-rlp-gost-be-2022-mathematik.txt', 'quellen/quelle-rlp-gost-bb-2022-mathematik.txt',
                'quellen/quelle-rlp-fos-bb-2019-mathematik.txt'] + [f'quellen/{w["datei"]}' for w in LEHRWERKE.values()]
    try:
        aus = subprocess.run([git, '-c', 'core.pager=cat', 'log', '-1', '--format=%h %ad', '--date=short', '--'] + eingaben,
                             cwd=REPO, capture_output=True, text=True).stdout.strip()
    except OSError:
        aus = ''
    return aus or 'unbekannt'


def schreibe(ergebnis):
    alle = [(name, u) for name, liste in ergebnis.items() for u in liste]
    z = ['# Sek-II-Ordnung nach Halbjahr und Kursart je Lerneinheit (Vorschlagsliste)',
         f'Eingaben auf Stand {stand()}. Erzeugt im Auftrag Nacht 2026-09-26 (Teil 3) von `werkzeuge/sek2-ordnung-belege.py` '
         'aus den Sek-II-Einträgen, `katalog/_kursart-belege.md` (Planstellen), den Rahmenlehrplantexten und den '
         'Sek-II-Verzeichnissen unter `quellen/` sowie den Zuordnungsdaten `werkzeuge/sek2-ordnung-belege-daten.py`; '
         'abgeleitet, nie von Hand ändern. Zweck: für die Oberstufe ordnen Halbjahr und Kursart statt der Klasse '
         '(`ziel.md` § 5). Kein Eintrag wird geändert, nichts wird entschieden; „keine Stelle“ ist ein Ergebnis.',
         '',
         'Quellen:',
         '- Rahmenlehrplan GOST Berlin (`quelle-rlp-gost-be-2022-mathematik.txt`): Kurshalbjahr in der Spalte „Khj“ am '
         'rechten Rand des Standards (Q1–Q4; „Q1/2“ heißt Q1 oder Q2), Block „Grundkursfach und Leistungskursfach“ oder '
         '„Zusätzlich: Leistungskursfach“.',
         '- Rahmenlehrplan GOST Brandenburg (`quelle-rlp-gost-bb-2022-mathematik.txt`): Kurshalbjahr = Abschnitt '
         '„Q1 1. Kurshalbjahr“ … „Q4“ (Zeilen 864, 1030, 1196, 1313), Block „Grund- und Leistungskursfach“ oder '
         '„Zusätzlich im Leistungskursfach“.',
         '- Rahmenlehrplan Fachoberschule (`quelle-rlp-fos-bb-2019-mathematik.txt`): Themenfeld 1–8; die FOS ist einjährig, '
         'ohne Kurshalbjahr und Kursart. Gesucht werden die FOS-Zitate der Lerneinheitszeile des Eintrags.',
         '- Die Planstellen je Einheit stammen aus `katalog/_kursart-belege.md` (dort am Quelltext geprüft, mit Ermessen); '
         'Halbjahr und Block liest dieses Skript am Quelltext nach.',
         '- Lehrwerke: Bigalke/Köhler Brandenburg 2019/2020, Bände GK 11, LK 11, GK 12, LK 12 '
         '(`quelle-cornelsen-bigalkekoehler-sek2-bebb-inhalt.txt`; Reihenfolge-Quelle, keine Form-Quelle, Beschluss '
         '25.09.2026); Fundamente der Mathematik Ausgabe B, nur Einführungsphase '
         '(`quelle-cornelsen-fundamente-sek2-ausgabeb-inhalt.txt`); Elemente der Mathematik SII NRW 2024/2025, nur '
         'Gegenprobe (`quelle-westermann-elemente-der-mathematik-sek2-nrw-inhalt.txt`); Mathematik Neue Wege SII Berlin '
         '2011, nur Gegenprobe (`quelle-westermann-mathematikneuewege-sek2-berlin2011-inhalt.txt`).',
         '',
         'Lesart:',
         '- Eine Lehrwerkszeile gehört zu einer Einheit, wenn sie ihren Inhalt nennt; maßgeblich ist der Inhalt, nicht der '
         'Wortlaut. Zitiert ist die Kapitelzeile wortgleich (ohne Führungspunkte und Seitenzahl), davor die '
         'Kapitelüberschrift; S. = Seite laut Verzeichnis, Z. = Zeilennummer der Quelldatei. Wiederholungs- und '
         'Übersichtskapitel (Abiturvorbereitung, Grundstrategien) zählen nicht in die Zusammenfassung.',
         '- „Halbjahr:“ nennt die Kurshalbjahre beider Pläne (gleich: einmal) und die Bigalke/Köhler-Bände (11 oder 12). '
         '„GK/LK:“ nennt die Blöcke beider Pläne („GK und LK“ = mindestens eine Stelle im gemeinsamen Block) und die '
         'Bigalke/Köhler-Kursbände. „nur LK: ja“, wenn jede Planstelle im Leistungskurszusatz steht (mindestens eine '
         'Stelle) oder Bigalke/Köhler die Einheit nur in LK-Bänden führt.',
         '- „Ermessen:“ steht an der Einheit, deren Zuordnung eine Auslegung verlangt (aus `_kursart-belege.md` '
         'übernommen oder neu).',
         '']
    # Zahlen
    zs = [(name, u, zusammenfassung(u)) for name, u in alle]
    nur_lk = [(name, u) for name, u, s in zs if s[2]]
    ohne_plan = [(name, u) for name, u, s in zs if not u['stellen']['BE'] and not u['stellen']['BB']]
    ohne_bk = [(name, u) for name, u, s in zs if not s[7]]
    laender = [(name, u) for name, u, s in zs if s[4]]
    halb = defaultdict(int)
    for name, u, s in zs:
        for q in sorted(set(s[5]) | set(s[6])):
            halb[q] += 1
    fos_mit = sum(1 for _, u in alle if u['stellen']['FOS'])
    fos_offen = [(name, u) for name, u in alle if u['fos_offen']]
    z += ['## Zahlen',
          f'Einträge: {len(ergebnis)} ({sum(1 for n in ergebnis if not any("Sek II" in u["titel"] for u in ergebnis[n]))} '
          f'Sek-II-Einträge der Tabelle Sekundarstufe II und {sum(1 for n in ergebnis if any("Sek II" in u["titel"] for u in ergebnis[n]))} '
          f'Sek-I-Einträge mit Sek-II-Einheit); Lerneinheiten: {len(alle)}.',
          f'Einheiten mit Planstelle Berlin: {sum(1 for _, u in alle if u["stellen"]["BE"])}, Brandenburg: '
          f'{sum(1 for _, u in alle if u["stellen"]["BB"])}, in keinem Plan: {len(ohne_plan)}'
          + (f' ({", ".join(f"{n} {u["n"]}" for n, u in ohne_plan)})' if ohne_plan else '') + '.',
          'Einheiten je Kurshalbjahr (Berlin oder Brandenburg; eine Einheit kann in mehreren stehen): '
          + ', '.join(f'{q} {halb[q]}' for q in sorted(halb)) + '.',
          f'Einheiten mit Länderunterschied in der Kursart: {len(laender)}'
          + (f' ({", ".join(f"{n} {u["n"]}" for n, u in laender)})' if laender else '') + '.',
          f'Einheiten „nur LK: ja“: {len(nur_lk)}'
          + (f' ({", ".join(f"{n} {u["n"]}" for n, u in nur_lk)})' if nur_lk else '') + '.',
          f'Einheiten mit Stelle bei Bigalke/Köhler (Bände 11/12): {len(alle) - len(ohne_bk)}; ohne: {len(ohne_bk)}.',
          f'Einheiten mit FOS-Stelle: {fos_mit}; FOS-Zitate des Eintrags ohne Fund im Plantext: '
          f'{sum(len(u["fos_offen"]) for _, u in alle)}.',
          '']
    # Übersicht je Eintrag
    z += ['## Übersicht je Eintrag', '', '| Eintrag | Halbjahr | GK/LK | nur LK |', '|---|---|---|---|']
    for name, liste in ergebnis.items():
        if not liste:
            z.append(f'| {name} | keine Lerneinheiten (Verweiseintrag) | – | – |')
            continue
        be = set(); bb = set(); bk = set(); nl = []
        kbe, kbb = set(), set()
        for u in liste:
            s = zusammenfassung(u)
            be |= set(s[5]); bb |= set(s[6]); bk |= {b[3:] for b in s[7]}
            kbe |= {x['block'] for x in u['stellen']['BE']}; kbb |= {x['block'] for x in u['stellen']['BB']}
            if s[2]:
                nl.append(str(u['n']))
        h = []
        if be and be == bb:
            h.append('/'.join(sorted(be)))
        else:
            if be: h.append('BE ' + '/'.join(sorted(be)))
            if bb: h.append('BB ' + '/'.join(sorted(bb)))
        if not be and not bb:
            h.append('keine Planstelle')
        h.append('B/K ' + ('/'.join(sorted(bk)) if bk else '–'))

        def ka(bl):
            if not bl:
                return '–'
            if bl == {'Leistungskurszusatz'}:
                return 'nur LK'
            if 'Leistungskurszusatz' in bl:
                return 'GK und LK, Teile nur LK'
            return 'GK und LK'
        k = f'BE {ka(kbe)} · BB {ka(kbb)}' if ka(kbe) != ka(kbb) else ka(kbe)
        z.append(f"| {name} | {' · '.join(h)} | {k} | {('Einheit ' + ', '.join(nl)) if nl else 'nein'} |")
    z.append('')
    # je Eintrag
    for name, liste in ergebnis.items():
        z.append(f'### {name}')
        if not liste:
            z.append('- Keine Lerneinheiten: Verweiseintrag, die didaktischen Abschnitte verweisen auf den tragenden '
                     'Eintrag (Halbjahr und Kursart dort).')
        for u in liste:
            z.append(f"- {u['n']}. {u['titel']}")
            if u['marke']:
                z.append(f"  - Eintrag, Zeile {u['marke'][0]}: {u['marke'][1]}")
            for land, lname in (('BE', 'Berlin'), ('BB', 'Brandenburg')):
                if not u['stellen'][land]:
                    z.append(f'  - Rahmenlehrplan {lname}: keine Stelle')
                for s in u['stellen'][land]:
                    zr = '–'.join(str(x) for x in (s['zeilen'][0], s['zeilen'][-1])) if len(s['zeilen']) > 1 and s['zeilen'][0] != s['zeilen'][-1] else str(s['zeilen'][0])
                    khj = s['khj'] or 'kein Halbjahr'
                    if land == 'BE' and s['khj_zeile']:
                        khj += f" (Khj, Z. {s['khj_zeile']})"
                    z.append(f"  - Rahmenlehrplan {lname}, Z. {zr}: {s['zitat']} – {khj}, {s['block'] or 'Block?'}")
            if u['stellen']['FOS']:
                for s in u['stellen']['FOS']:
                    zr = '–'.join(str(x) for x in (s['zeilen'][0], s['zeilen'][-1])) if s['zeilen'][0] != s['zeilen'][-1] else str(s['zeilen'][0])
                    z.append(f"  - FOS, Z. {zr}: {s['zitat']} – Themenfeld {s['feld']}")
            else:
                z.append('  - FOS: keine Stelle (die Zeile der Einheit nennt kein FOS-Zitat)')
            for zit in u['fos_offen']:
                z.append(f'  - FOS: Zitat „{zit}“ im Plantext nicht gefunden')
            for quelle, w in LEHRWERKE.items():
                eigene = [b for b in u['buecher'] if b[0] == quelle]
                for q, zeile, info, _ in eigene:
                    z.append(f"  - {zitat_lehrwerk(q, zeile, info)}" + (' (Gegenprobe)' if w['rolle'] == 'Gegenprobe' else ''))
                if not eigene:
                    grund = u['keine'].get(quelle) or w.get('keine')
                    z.append(f"  - {w['name']}: keine Stelle" + (f' – {grund}' if grund else ''))
            for e in u['erm']:
                z.append(f'  - Ermessen: {e}')
            s = zusammenfassung(u)
            z.append(f'  - Halbjahr: {s[0]} · GK/LK: {s[1]}')
            z.append(f"  - nur LK: {'ja (' + ', '.join(s[3]) + ')' if s[2] else 'nein'}")
        z.append('')
    return '\n'.join(z).rstrip('\n') + '\n'


def main():
    fehler, ergebnis = baue()
    if fehler:
        print(f'{len(fehler)} Prüffehler – nichts geschrieben:')
        for f in fehler[:100]:
            print('  ' + f)
        sys.exit(1)
    text = schreibe(ergebnis)
    if '--probe' in sys.argv:
        alt = open(AUSGABE, encoding='utf-8').read() if os.path.exists(AUSGABE) else ''
        print('unverändert' if alt == text else 'weicht ab')
        return
    with open(AUSGABE, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(f'{os.path.relpath(AUSGABE, REPO)} geschrieben.')


if __name__ == '__main__':
    main()
