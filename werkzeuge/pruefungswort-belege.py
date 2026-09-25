"""Prüfungswort-Belege je Lerneinheit und Typ (v0.1, 26.09.2026).

Liefert die Zahlen für das Prüfungswort der Zweigzeile (ziel.md § 2 „Überschriften“: „P10 oft“,
„P10“, „keine P10-Aufgabe“; Sek II „Abitur GK/LK“, „FHR“). Schreibt katalog/_pruefungswort-belege.md
und die Typenliste werkzeuge/pruefungswort-belege-typen.txt; ändert keinen Katalogeintrag.

Aufruf aus der Repo-Wurzel:
  python werkzeuge/pruefungswort-belege.py            baut beide Dateien
  python werkzeuge/pruefungswort-belege.py --typen    schreibt nur die Typenliste (zum Zuordnen)
  python werkzeuge/pruefungswort-belege.py --probe    baut und vergleicht mit den vorhandenen Dateien,
                                                      schreibt nichts
Bei einem Prüffehler (Name, Nummer, Wortlaut, fehlender Grund) wird nichts geschrieben.

Eingaben: katalog/index.md (Tabellen Sekundarstufe I und II), die Einträge (Lerneinheiten, Typen je
Lerneinheit, Prüfungsform), themen.csv, msa/msa-typen.csv, msa/msa-ertrag.csv, msa/msa-katalog-basis.csv
und msa/msa-katalog-kontext.csv (wie werkzeuge/ertrag.py; msa-katalog-gym.csv nur für den Vermerk „nur GYM“),
abitur/abitur-typen.csv, abitur/abi-katalog.csv, abitur/iqb-katalog.csv (nur für den Vermerk „nur Pool“),
fhr/fhr-typen.csv, fhr/fhr-katalog.csv und die Zuordnungsdaten werkzeuge/pruefungswort-belege-daten.py.

Lesarten
- Typen je Lerneinheit: Sek-I-Teile werden an „·“, „—“ und am Satzende außerhalb von Klammern getrennt;
  ein Vorspann mit Doppelpunkt („Dazu:“) wird abgelöst. Sek-II-Teile (Sek-II-Einträge und alles hinter
  „— Sek II“ in einem Sek-I-Eintrag) tragen je Haupttyp eine Zeilenzahl in Klammern; getrennt wird dort nur
  hinter einer schließenden Klammer (ein „·“ im Typnamen, etwa A · B, trennt nicht), die Marken
  „Nachweis:“, „Deutung:“, „kein …typ“ fallen weg, hinter „Dazu:“ folgen die didaktischen Typen.
- Sek I, Einheit: die P10-Typen der Einheit sind die der Zuordnungszeile im Abschnitt „Prüfungsform (P10)“
  des Eintrags (Daten U, jeder Name muss dort wörtlich stehen) und die, die eine Typzuordnung (Daten T)
  der Einheit nennt. themen.csv gibt die Thema-Ebene vor: P10-Typen der Themen des Eintrags, die keiner
  Einheit zugeordnet sind, werden genannt.
- Sek I, Typ: ein P10-Typ prüft einen Katalogtyp, wenn die Fertigkeit des Katalogtyps Teil der Leistung
  ist, die der P10-Typ verlangt – nach seiner Definition in msa-typen.csv oder nach einem Original
  (Haupt- oder Nebentyp); Vorstufen desselben Verfahrens zählen mit, Fehler-finden-, Begründungs- und
  Darstellungstypen nur, wenn ein P10-Typ genau diese Leistung verlangt. Nicht wortgleiche Zuordnungen
  tragen einen Grund (Daten T); ohne Zuordnung: „kein P10-Typ“.
- Themenregel: themen.csv gibt die Thema-Ebene vor. Gezählt werden nur P10-Typen der msa-Themen, die
  themen.csv dem Eintrag zuweist, und der Themen der P10-Typen, die der Eintrag selbst in seiner
  Zuordnungszeile führt (Daten U; so zählen bei kreis.md auch neuere GYM-Typen des Themas „Flächeninhalt und
  Umfang“, dessen Kreistypen die Zuordnungszeile nennt);
  ein P10-Typ anderer Themen, den die Daten nennen, steht als Hinweis „außerhalb der Themen des Eintrags
  (zählt nicht)“ da. So bleibt „keine P10-Aufgabe“ mit dem Vermerk aus themen.csv stehen, wo das Thema
  kein Prüfungsthema ist, auch wenn eine Fertigkeit als Schritt in fremden Aufgaben vorkommt.
  „Behauptung prüfen“ ist themenübergreifend (nur Nebentyp, Thema nach der ersten Fundstelle) und zählt nie.
- Verfahrensgeber (Daten V): Sagt die Zuordnungszeile, eine Einheit ohne eigenen Typ sei das „Verfahren für“
  einen namentlich genannten P10-Typ einer anderen Datei (quadratische-gleichungen Einheit 3 für die Nullstellen
  in quadratische-funktionen.md), zählt dieser Typ für die Einheit wie ein eigener; „liefert … für“ und
  „Voraussetzung für“ sind Nebenleistung und zählen nicht.
- P10-Jahrgänge: Jahre 2014–2026 (13) der Zeilen in msa-katalog-basis.csv und msa-katalog-kontext.csv, in
  denen ein P10-Typ als typ (Hauptleistung) oder in typ_neben (Nebenleistung) steht; gezählt wird
  „Haupt oder Neben“ (der Typ kam vor), daneben „Haupt“. Die Kennzahlen je P10-Typ (ertrag, jahre_haupt,
  jahre_gesamt, erster, letzter, basis, kontext) stehen wortgleich wie in msa/msa-ertrag.csv.
- Sek II: der Katalogtyp ist ein Prüfungstyp, wenn sein Name (ohne Zeilenzahl) wortgleich in
  abitur/abitur-typen.csv oder fhr/fhr-typen.csv steht, auch mit einer Gegenstandsklasse davor
  („Punkt und Ebene: …“, Grund „Präfix“); sonst entscheiden die Daten S mit Grund. Abitur-Jahrgänge aus
  abi-katalog.csv: papier „…-gk“ = Grundkurs, „…-lk“ und „bb-ea“ (erhöhtes Anforderungsniveau) =
  Leistungskurs; erfasst sind GK 2018–2026 (9 Jahrgänge), LK 2017, 2018, 2022–2026 (7). FHR-Jahrgänge aus
  fhr-katalog.csv, 2019–2026 (8). Gezählt Haupt oder Neben, daneben Haupt. Der IQB-Pool zählt nicht
  (Auftrag: Abitur und FHR); ein Typ nur im Pool trägt den Vermerk „nur Pool“.

Entstanden im Auftrag Nacht 2026-09-26, Teil 2 (auftrag-nacht-2026-09-26.md).
"""
import csv
import os
import re
import subprocess
import sys
from collections import OrderedDict, defaultdict

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
KAT = os.path.join(REPO, 'katalog')
DATEN = os.environ.get('PWB_DATEN') or os.path.join(HIER, 'pruefungswort-belege-daten.py')
TYPENLISTE = os.path.join(HIER, 'pruefungswort-belege-typen.txt')
AUSGABE = os.path.join(KAT, '_pruefungswort-belege.md')

JAHRE_P10 = list(range(2014, 2027))
GK_JAHRE = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
LK_JAHRE = [2017, 2018, 2022, 2023, 2024, 2025, 2026]
FHR_JAHRE = list(range(2019, 2027))
ABKUERZUNGEN = ['z. B.', 'd. h.', 'u. a.', 'Nr.', 'S.', 'ca.', 'bzw.', 'vgl.', 'evtl.', 'geg.', 'ges.']
ERTRAG_SPALTEN = ['ertrag', 'jahre_haupt', 'jahre_gesamt', 'erster', 'letzter', 'basis', 'kontext']
THEMENUEBERGREIFEND = {'Behauptung prüfen'}


def pfad(*teile):
    return os.path.join(REPO, *teile)


def lies_csv(*teile):
    with open(pfad(*teile), encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))


def lies(*teile):
    with open(pfad(*teile), encoding='utf-8') as f:
        return f.read()


# ---------------------------------------------------------------- Einträge

def index_listen():
    zeilen = lies('katalog', 'index.md').split('\n')
    sek1, sek2, bereich = [], [], None
    for z in zeilen:
        if z.startswith('## Sekundarstufe I') and not z.startswith('## Sekundarstufe II'):
            bereich = 1
        elif z.startswith('## Sekundarstufe II'):
            bereich = 2
        elif z.startswith('## '):
            bereich = None
        m = re.match(r'^\| ([a-z0-9-]+)\.md \|', z)
        if m and bereich == 1:
            sek1.append(m.group(1))
        elif m and bereich == 2:
            sek2.append(m.group(1))
    return sek1, sek2


def abschnitt(text, kopf):
    m = re.search(r'^### ' + re.escape(kopf) + r'[^\n]*\n(.*?)(?=^### |^## |\Z)', text, re.S | re.M)
    return m.group(1) if m else ''


def abschnitt_zeilen(text, kopf):
    """(erste Zeilennummer des Abschnittsinhalts, Inhalt)."""
    m = re.search(r'^### ' + re.escape(kopf) + r'[^\n]*\n', text, re.M)
    if not m:
        return None, ''
    start = text[:m.end()].count('\n') + 1
    return start, abschnitt(text, kopf)


def lerneinheiten(text):
    teil = abschnitt(text, 'Lerneinheiten')
    einheiten = OrderedDict()
    for m in re.finditer(r'^(\d+)\.\s+(.+?)(?:\s+–\s+|$)', teil, re.M):
        einheiten[int(m.group(1))] = m.group(2).strip()
    return einheiten


def auf_ebene_null(text, trenner):
    """Trennt text an trenner (Liste regulärer Ausdrücke) außerhalb von Klammern."""
    stuecke, tiefe, start, i = [], 0, 0, 0
    muster = re.compile('|'.join(trenner))
    while i < len(text):
        c = text[i]
        if c in '([':
            tiefe += 1
        elif c in ')]':
            tiefe = max(0, tiefe - 1)
        if tiefe == 0:
            m = muster.match(text, i)
            if m and m.end() > i:
                stuecke.append(text[start:i])
                start = i = m.end()
                continue
        i += 1
    stuecke.append(text[start:])
    return stuecke


def schuetze(text):
    for i, abk in enumerate(ABKUERZUNGEN):
        text = text.replace(abk, f'\x00{i}\x00')
    return text


def entschuetze(text):
    for i, abk in enumerate(ABKUERZUNGEN):
        text = text.replace(f'\x00{i}\x00', abk)
    return text


MARKE_SEK2 = re.compile(r'^(Sek II\b[^:]*|Haupttypen[^:]*|Nachweis|Deutung|Dazu)\s*:\s*')
FORMELTOKEN = re.compile(r'^„?(?:[0-9]+(?:[,/][0-9]+)?°?|[a-zA-Zπα](?:_[a-z]+)?[²³ᵏˣⁿ⁻⁰¹²³⁴⁵⁶⁷⁸⁹]*|α/360°|10(?:\^\S|[ⁿ⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+))“?$')
NEUER_TYP = {'aus', 'oder', 'als'}
PLATZHALTER = re.compile(r'^kein (?:Typ\b|\S*typ\b|Berechnungs- und kein)')  # „kein Deutungstyp“ u. ä.


def malpunkte_schuetzen(text):
    """Ersetzt „ · “ zwischen zwei Formelzeichen (V = π · r² · h, a · 10ⁿ, 6 · a²) durch einen geschützten
    Punkt, damit nur die Typtrenner trennen. Ein Formelpunkt: das Wort davor und danach sind Formelzeichen
    (Zahl, Bruch, einzelner Buchstabe mit Hoch- oder Tiefzeichen, π, α/360°), das Wort davor ist nicht „0“
    (rechte Seite einer Gleichung „… = 0“), und das Wort nach dem zweiten Zeichen ist nicht „aus“, „oder“,
    „als“ (dann beginnt dort ein neuer Typ: „h aus V · r aus V“)."""
    teile = text.split(' · ')
    if len(teile) == 1:
        return text
    aus = teile[0]
    for rest in teile[1:]:
        vor = aus.split()[-1] if aus.split() else ''
        woerter = rest.split()
        nach = woerter[0] if woerter else ''
        danach = woerter[1] if len(woerter) > 1 else ''
        tiefe = aus.count('(') - aus.count(')')
        if (tiefe == 0 and vor != '0' and FORMELTOKEN.match(vor) and FORMELTOKEN.match(nach)
                and danach not in NEUER_TYP):
            aus += ' \x01 ' + rest
        else:
            aus += ' · ' + rest
    return aus


def sek1_typen(teil):
    liste = []
    teil = malpunkte_schuetzen(teil)
    for stueck in auf_ebene_null(schuetze(teil), [r' · ', r' — ', r'\. (?=\S)']):
        stueck = stueck.replace('\x01', '·')
        s = entschuetze(stueck).strip().lstrip('—').strip().rstrip('.').strip()
        s = re.sub(r'^Dazu:\s*', '', s)
        if not s or PLATZHALTER.match(s):
            continue
        liste.append(s)
    return liste


def sek2_typen(teil):
    """Sek-II-Teil einer Typenzeile: [(Typ, didaktisch ja/nein)]."""
    teil = schuetze(teil)
    haupt, didakt = teil, ''
    for m in re.finditer(r'Dazu:\s*', teil):
        vorher = teil[:m.start()].rstrip()
        if not vorher or vorher[-1] in '.)—':
            haupt, didakt = vorher.rstrip('—').rstrip(), teil[m.end():]
            break
    liste = []
    for stueck in auf_ebene_null(haupt, [r'(?<=\))\s*[·—]\s+', r'(?<=\))\.\s+', r'\s+—\s+']):
        s = entschuetze(stueck).strip().lstrip('—').strip()
        while True:
            m = MARKE_SEK2.match(s)
            if not m:
                break
            s = s[m.end():].strip()
        s = s.rstrip('.').strip()
        if not s or PLATZHALTER.match(s):
            continue
        liste.append((s, False))
    for s in sek1_typen(entschuetze(didakt)):
        liste.append((s, True))
    return liste


def typen_des_eintrags(text, sek2_eintrag):
    """{Einheit: [dict(nr, text, sek2, didakt)]}."""
    teil = abschnitt(text, 'Typen je Lerneinheit')
    sek2_einheiten = {n for n, t in lerneinheiten(text).items() if 'Sek II' in t}
    ergebnis = OrderedDict()
    for m in re.finditer(r'^Einheit (\d+):\s*(.+)$', teil, re.M):
        n = int(m.group(1))
        zeile = m.group(2)
        liste = []
        if sek2_eintrag or n in sek2_einheiten:
            for s, d in sek2_typen(zeile):
                liste.append({'text': s, 'sek2': True, 'didakt': d})
        else:
            m2 = re.search(r'(?:^|\.\s*|\s)—\s*Sek II\b', zeile)
            vorn, hinten = (zeile[:m2.start()], zeile[m2.start():]) if m2 else (zeile, '')
            for s in sek1_typen(vorn):
                liste.append({'text': s, 'sek2': False, 'didakt': False})
            if hinten:
                hinten = re.sub(r'^[.\s—]*Sek II\b[^:]*:\s*', '', hinten)
                for s, d in sek2_typen(hinten):
                    liste.append({'text': s, 'sek2': True, 'didakt': d})
        for i, t in enumerate(liste, 1):
            t['nr'] = f'{n}.{i}'
        ergebnis[n] = liste
    return ergebnis


def ohne_zeilenzahl(s):
    """Typname ohne die Zeilenzahl-Klammer „(n)“ bzw. „(n; …)“ und ohne alles dahinter."""
    m = re.search(r'\s*\(\d+(\)|;)', s)
    return s[:m.start()].strip() if m else s.strip()


def kern(s):
    alt = None
    while alt != s:
        alt = s
        s = re.sub(r'\([^()]*\)', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


# ---------------------------------------------------------------- Prüfungskataloge

def p10_jahre():
    haupt, neben = defaultdict(set), defaultdict(set)
    for datei in ('msa-katalog-basis.csv', 'msa-katalog-kontext.csv'):
        for z in lies_csv('msa', datei):
            j = int(z['jahr'])
            haupt[z['typ']].add(j)
            for n in z['typ_neben'].split('|'):
                if n.strip():
                    neben[n.strip()].add(j)
    return haupt, neben


def gym_typen():
    s = set()
    for z in lies_csv('msa', 'msa-katalog-gym.csv'):
        s.add(z['typ'])
        s.update(n.strip() for n in z['typ_neben'].split('|') if n.strip())
    return s


def abi_jahre():
    """typ → {'GK': (haupt, alle), 'LK': (haupt, alle)}."""
    d = defaultdict(lambda: {'GK': (set(), set()), 'LK': (set(), set())})
    for z in lies_csv('abitur', 'abi-katalog.csv'):
        kurs = 'GK' if z['papier'].endswith('-gk') else 'LK'
        j = int(z['jahr'])
        d[z['typ']][kurs][0].add(j)
        d[z['typ']][kurs][1].add(j)
        for n in z['typ_neben'].split('|'):
            if n.strip():
                d[n.strip()][kurs][1].add(j)
    return d


def fhr_jahre():
    d = defaultdict(lambda: (set(), set()))
    for z in lies_csv('fhr', 'fhr-katalog.csv'):
        j = int(z['jahr'])
        d[z['typ']][0].add(j)
        d[z['typ']][1].add(j)
        for n in z['typ_neben'].split('|'):
            if n.strip():
                d[n.strip()][1].add(j)
    return d


def pool_typen():
    s = set()
    for z in lies_csv('abitur', 'iqb-katalog.csv'):
        s.add(z['typ'])
        s.update(n.strip() for n in z['typ_neben'].split('|') if n.strip())
    return s


# ---------------------------------------------------------------- Daten

class Daten:
    def __init__(self):
        self.U = defaultdict(list)       # (eintrag, einheit) -> [p10]
        self.V = defaultdict(list)       # (eintrag, einheit) -> [p10] – „Verfahren für“ laut Zuordnungszeile
        self.T = {}                      # (eintrag, nr) -> (text, [p10], grund)
        self.S = {}                      # (eintrag, nr) -> (text, [abi], [fhr], grund)
        self.fehler = []

    def lade(self):
        if not os.path.exists(DATEN):
            return self
        umgebung = {'U': self.u, 'V': self.v, 'T': self.t, 'S': self.s}
        with open(DATEN, encoding='utf-8') as f:
            exec(compile(f.read(), DATEN, 'exec'), umgebung)
        return self

    def u(self, eintrag, einheit, typen):
        if (eintrag, einheit) in self.U:
            self.fehler.append(f'U doppelt: {eintrag} Einheit {einheit}')
        self.U[(eintrag, einheit)] = list(typen)

    def v(self, eintrag, einheit, typen):
        self.V[(eintrag, einheit)] += list(typen)

    def t(self, eintrag, nr, text, typen, grund=''):
        if (eintrag, nr) in self.T:
            self.fehler.append(f'T doppelt: {eintrag} {nr}')
        self.T[(eintrag, nr)] = (text, list(typen), grund)

    def s(self, eintrag, nr, text, abi=(), fhr=(), grund=''):
        if (eintrag, nr) in self.S:
            self.fehler.append(f'S doppelt: {eintrag} {nr}')
        self.S[(eintrag, nr)] = (text, list(abi), list(fhr), grund)


# ---------------------------------------------------------------- Zusammenbau

def jahrtext(menge, alle):
    return f'{len(menge)}' + (f' ({", ".join(str(j) for j in sorted(menge))})' if menge and len(menge) < len(alle) else '')


def baue():
    fehler = []
    sek1, sek2 = index_listen()
    daten = Daten().lade()
    fehler += daten.fehler
    themen = lies_csv('themen.csv')
    msa_typen = {z['typ']: z for z in lies_csv('msa', 'msa-typen.csv')}
    ertrag = {z['typ']: z for z in lies_csv('msa', 'msa-ertrag.csv')}
    p10_h, p10_n = p10_jahre()
    gym = gym_typen()
    abi_typen = {z['typ'] for z in lies_csv('abitur', 'abitur-typen.csv')}
    fhr_typen = {z['typ'] for z in lies_csv('fhr', 'fhr-typen.csv')}
    abi_j = abi_jahre()
    fhr_j = fhr_jahre()
    pool = pool_typen()
    ohne_praefix = defaultdict(list)
    for t in abi_typen:
        if ': ' in t:
            ohne_praefix[t.split(': ', 1)[1]].append(t)

    eintraege = OrderedDict()
    for name in sek1 + sek2:
        text = lies('katalog', name + '.md')
        eintraege[name] = {'text': text, 'sek2': name in sek2, 'einheiten': lerneinheiten(text),
                           'typen': typen_des_eintrags(text, name in sek2)}

    # ---- Typenliste
    tl = ['# Typenliste zu werkzeuge/pruefungswort-belege.py',
          'Abgeleitet von werkzeuge/pruefungswort-belege.py, nie von Hand ändern.',
          'Je Eintrag und Einheit die Typen aus „Typen je Lerneinheit“ mit Nummer (Einheit.Lfd); Sek II mit',
          'dem Prüfungstyp, den das Skript wortgleich findet (= Name, P = mit Gegenstandsklasse, ? = keiner).', '']
    for name, e in eintraege.items():
        th = [z['thema'] for z in themen if z['kanonisch'] == name and z['profil'] == 'msa']
        tl.append(f"## {name} ({'Sek II' if e['sek2'] else 'Sek I'})" + (f" – themen.csv: {', '.join(th)}" if th else ''))
        for n, liste in e['typen'].items():
            tl.append(f"Einheit {n} · {e['einheiten'].get(n, '?')}")
            for t in liste:
                marke = ''
                if t['sek2'] and not t['didakt']:
                    nm = ohne_zeilenzahl(t['text'])
                    marke = ' [=]' if (nm in abi_typen or nm in fhr_typen) else (' [P]' if nm in ohne_praefix else ' [?]')
                elif t['sek2']:
                    marke = ' [didaktisch]'
                tl.append(f"  {t['nr']}  {t['text']}{marke}")
        tl.append('')
    typenliste = '\n'.join(tl).rstrip('\n') + '\n'

    # ---- Prüfen der Daten
    for (name, nr), (text, typen, grund) in daten.T.items():
        e = eintraege.get(name)
        if not e:
            fehler.append(f'T: Eintrag {name} unbekannt')
            continue
        n = int(nr.split('.')[0])
        t = next((x for x in e['typen'].get(n, []) if x['nr'] == nr), None)
        if not t:
            fehler.append(f'T: {name} {nr} gibt es nicht')
            continue
        if t['text'] != text:
            fehler.append(f'T: {name} {nr} Wortlaut weicht ab: „{text}“ statt „{t["text"]}“')
        for p in typen:
            if p not in msa_typen:
                fehler.append(f'T: {name} {nr}: P10-Typ „{p}“ nicht in msa-typen.csv')
        wortgleich = len(typen) == 1 and kern(text).lower() == typen[0].lower()
        if typen and not wortgleich and not grund.strip():
            fehler.append(f'T: {name} {nr}: Grund fehlt')
    for (name, n), typen in list(daten.U.items()) + list(daten.V.items()):
        e = eintraege.get(name)
        if not e:
            fehler.append(f'U: Eintrag {name} unbekannt')
            continue
        if n not in e['einheiten']:
            fehler.append(f'U: {name} Einheit {n} gibt es nicht')
        pf = abschnitt(e['text'], 'Prüfungsform (P10)')
        for p in typen:
            if p not in msa_typen:
                fehler.append(f'U: {name} Einheit {n}: „{p}“ nicht in msa-typen.csv')
            elif p not in pf:
                fehler.append(f'U: {name} Einheit {n}: „{p}“ steht nicht in der Prüfungsform des Eintrags')
    for (name, nr), (text, abi, fhr, grund) in daten.S.items():
        e = eintraege.get(name)
        n = int(nr.split('.')[0])
        t = next((x for x in e['typen'].get(n, []) if x['nr'] == nr), None) if e else None
        if not t:
            fehler.append(f'S: {name} {nr} gibt es nicht')
            continue
        if t['text'] != text:
            fehler.append(f'S: {name} {nr} Wortlaut weicht ab: „{text}“ statt „{t["text"]}“')
        for a in abi:
            if a not in abi_typen:
                fehler.append(f'S: {name} {nr}: „{a}“ nicht in abitur-typen.csv')
        for a in fhr:
            if a not in fhr_typen:
                fehler.append(f'S: {name} {nr}: „{a}“ nicht in fhr-typen.csv')
        if not grund.strip():
            fehler.append(f'S: {name} {nr}: Grund fehlt')

    # ---- Sek I messen
    def p10_zeile(p):
        z = ertrag.get(p)
        werte = [z[s] if z else '–' for s in ERTRAG_SPALTEN]
        vermerk = ''
        if z and z['jahre_gesamt'] == '0':
            vermerk = 'nur GYM' if p in gym else 'keine Zeile'
        return werte, vermerk

    sek1_mess = OrderedDict()
    for name in sek1:
        e = eintraege[name]
        th = [z for z in themen if z['kanonisch'] == name]
        themen_msa = [z['thema'] for z in th if z['profil'] == 'msa']
        vermerk = '; '.join(z['bemerkung'] for z in th if z['bemerkung'])
        u_typen = {p for (en, _), liste in daten.U.items() if en == name for p in liste}
        u_themen = {msa_typen[p]['thema'] for p in u_typen if p in msa_typen}
        eigen = {p for p, z in msa_typen.items() if z['thema'] in set(themen_msa) | u_themen} | u_typen
        eigen |= {p for (en, _), liste in daten.V.items() if en == name for p in liste}
        eigen -= THEMENUEBERGREIFEND
        einheiten = OrderedDict()
        alle_p10 = set()
        for n, titel in e['einheiten'].items():
            if 'Sek II' in titel:
                continue
            u = daten.U.get((name, n), [])
            typen = []
            for t in e['typen'].get(n, []):
                if t['sek2']:
                    continue
                zu = daten.T.get((name, t['nr']))
                alle = zu[1] if zu else []
                p10 = [p for p in alle if p in eigen]
                fremd = [p for p in alle if p not in eigen]
                grund = zu[2] if zu else ''
                ja = set()
                for p in p10:
                    ja |= p10_h.get(p, set()) | p10_n.get(p, set())
                jh = set()
                for p in p10:
                    jh |= p10_h.get(p, set())
                typen.append({'nr': t['nr'], 'text': t['text'], 'p10': p10, 'fremd': fremd, 'grund': grund,
                              'jahre': ja, 'jahre_h': jh})
            vf = daten.V.get((name, n), [])
            menge = list(u) + list(vf) + [p for t in typen for p in t['p10'] if p not in u]
            menge = list(OrderedDict.fromkeys(menge))
            alle_p10 |= set(menge)
            ja, jh = set(), set()
            for p in menge:
                ja |= p10_h.get(p, set()) | p10_n.get(p, set())
                jh |= p10_h.get(p, set())
            summe = sum(int(ertrag[p]['ertrag']) for p in menge if p in ertrag)
            ohne_typ = [p for p in list(u) + list(vf) if not any(p in t['p10'] for t in typen)]
            ausser = [p for p in menge if p not in u and p not in vf]
            einheiten[n] = {'titel': titel, 'p10': menge, 'jahre': ja, 'jahre_h': jh, 'summe': summe,
                            'typen': typen, 'ohne_typ': ohne_typ, 'ausser': ausser, 'verfahren': list(vf)}
        thema_typen = [p for p, z in msa_typen.items() if z['thema'] in themen_msa and p not in THEMENUEBERGREIFEND]
        frei = [p for p in thema_typen if p not in alle_p10]
        sek1_mess[name] = {'themen': themen_msa, 'vermerk': vermerk, 'einheiten': einheiten, 'frei': frei}

    # ---- Sek II messen
    sek2_mess = OrderedDict()
    for name in sek2 + [x for x in sek1 if any(t['sek2'] for l in eintraege[x]['typen'].values() for t in l)]:
        e = eintraege[name]
        einheiten = OrderedDict()
        for n, liste in e['typen'].items():
            typen = []
            for t in liste:
                if not t['sek2']:
                    continue
                zu = daten.S.get((name, t['nr']))
                if t['didakt'] and not zu:
                    typen.append({'nr': t['nr'], 'text': t['text'], 'abi': [], 'fhr': [], 'grund': '', 'art': 'didaktisch'})
                    continue
                if zu:
                    abi, fhr, grund, art = zu[1], zu[2], zu[3], 'Daten'
                else:
                    nm = ohne_zeilenzahl(t['text'])
                    abi = [nm] if nm in abi_typen else []
                    fhr = [nm] if nm in fhr_typen else []
                    grund, art = '', 'wortgleich'
                    if not abi and not fhr and len(ohne_praefix.get(nm, [])) == 1:
                        abi = ohne_praefix[nm]
                        grund, art = f'Präfix: abitur-typen.csv führt „{abi[0]}“', 'Präfix'
                    elif not abi and not fhr:
                        art = 'offen'
                        fehler.append(f'Sek II ohne Prüfungstyp: {name} {t["nr"]} „{t["text"]}“')
                typen.append({'nr': t['nr'], 'text': t['text'], 'abi': abi, 'fhr': fhr, 'grund': grund, 'art': art})
            if not typen:
                continue
            for t in typen:
                t['gk'] = (set().union(*[abi_j[a]['GK'][0] for a in t['abi']]) if t['abi'] else set(),
                           set().union(*[abi_j[a]['GK'][1] for a in t['abi']]) if t['abi'] else set())
                t['lk'] = (set().union(*[abi_j[a]['LK'][0] for a in t['abi']]) if t['abi'] else set(),
                           set().union(*[abi_j[a]['LK'][1] for a in t['abi']]) if t['abi'] else set())
                t['fh'] = (set().union(*[fhr_j[a][0] for a in t['fhr']]) if t['fhr'] else set(),
                           set().union(*[fhr_j[a][1] for a in t['fhr']]) if t['fhr'] else set())
                t['pool'] = bool(t['abi']) and all(a in pool for a in t['abi']) and not (t['gk'][1] or t['lk'][1])
            einheit = {'titel': e['einheiten'].get(n, '?'), 'typen': typen}
            for k in ('gk', 'lk', 'fh'):
                einheit[k] = (set().union(*[t[k][0] for t in typen]), set().union(*[t[k][1] for t in typen]))
            einheiten[n] = einheit
        sek2_mess[name] = einheiten

    return fehler, typenliste, sek1_mess, sek2_mess, (msa_typen, ertrag, p10_zeile, gym)


# ---------------------------------------------------------------- Ausgabe

def stand():
    eingaben = ['katalog', 'themen.csv', 'msa/msa-typen.csv', 'msa/msa-ertrag.csv', 'msa/msa-katalog-basis.csv',
                'msa/msa-katalog-kontext.csv', 'abitur/abitur-typen.csv', 'abitur/abi-katalog.csv',
                'fhr/fhr-typen.csv', 'fhr/fhr-katalog.csv']
    git = os.environ.get('GIT', 'git')
    try:
        aus = subprocess.run([git, '-c', 'core.pager=cat', 'log', '-1', '--format=%h %ad', '--date=short', '--']
                             + eingaben, cwd=REPO, capture_output=True, text=True).stdout.strip()
    except OSError:
        aus = ''
    return aus or 'unbekannt'


def schreibe_md(sek1_mess, sek2_mess, hilfen):
    msa_typen, ertrag, p10_zeile, gym = hilfen
    z = ['# Prüfungswort-Belege je Lerneinheit und Typ',
         'Abgeleitet von `werkzeuge/pruefungswort-belege.py` aus den Einträgen, `themen.csv`, den msa-, abi- und '
         'fhr-Katalogen und den Zuordnungsdaten `werkzeuge/pruefungswort-belege-daten.py`, nie von Hand ändern.',
         f'Eingaben auf Stand {stand()}. Die Datei schlägt vor, sie entscheidet nicht: die Schwelle „oft“ setzt der Lehrer.',
         '',
         'Lesart (Einzelheiten im Skriptkopf): Die P10-Typen einer Einheit sind die der Zuordnungszeile des Eintrags '
         'und die, die eine Typzuordnung nennt; ein P10-Typ prüft einen Katalogtyp, wenn dessen Fertigkeit Teil der '
         'Leistung ist, die der P10-Typ verlangt (Definition oder Original, Vorstufen desselben Verfahrens '
         'eingeschlossen); nicht wortgleiche Zuordnungen tragen einen Grund. Gezählt werden nur P10-Typen der Themen, '
         'die `themen.csv` dem Eintrag zuweist, und der Themen, aus denen seine Zuordnungszeile Typen führt; P10-Typen fremder Themen stehen als '
         'Hinweis da und zählen nicht, „Behauptung prüfen“ (themenübergreifend) zählt nie. „P10-Jahrgänge“ = Jahre 2014–2026, in '
         'denen ein P10-Typ der Einheit als Haupt- oder Nebenleistung vorkam (msa-katalog-basis/-kontext wie '
         '`ertrag.py`, ohne GYM); „davon Haupt“ nur als Hauptleistung.',
         '']

    # Zahlenblock
    einheiten = [(name, n, e) for name, m in sek1_mess.items() for n, e in m['einheiten'].items()]
    typen = [(name, n, t) for name, n, e in einheiten for t in e['typen']]
    ohne = [(name, n, e) for name, n, e in einheiten if not e['p10']]
    z += ['## Zahlenblock', '',
          f'- Sek I: {len(sek1_mess)} Einträge, {len(einheiten)} Lerneinheiten (ohne Sek-II-Einheiten), '
          f'{len(typen)} Typen; Einheiten mit P10-Typ {len(einheiten) - len(ohne)}, ohne P10-Typ {len(ohne)}; '
          f'Typen mit P10-Typ {sum(1 for _, _, t in typen if t["p10"])}, ohne {sum(1 for _, _, t in typen if not t["p10"])} '
          f'(davon {sum(1 for _, _, t in typen if not t["p10"] and t["fremd"])} nur mit P10-Typen fremder Themen, zählen nicht).',
          f'- Sek II: {len(sek2_mess)} Einträge mit Sek-II-Typen (davon '
          f'{sum(1 for x in sek2_mess if x in sek1_mess)} Sek-I-Einträge mit Sek-II-Teil), '
          f'{sum(len(e) for e in sek2_mess.values())} Einheiten.', '']

    # Verteilung Einheiten
    z += ['## Verteilung für die Schwelle „oft“ – Sek-I-Einheiten', '',
          'Sortiert nach P10-Jahrgängen (Haupt oder Neben), dann nach Summe ertrag.', '',
          '| Eintrag | Einheit | P10-Jahrgänge (von 13) | davon Haupt | P10-Typen | Summe ertrag |',
          '|---|---|---|---|---|---|']
    for name, n, e in sorted(einheiten, key=lambda x: (-len(x[2]['jahre']), -x[2]['summe'], x[0], x[1])):
        z.append(f"| {name} | {n} · {e['titel']} | {len(e['jahre'])} | {len(e['jahre_h'])} | {len(e['p10'])} | {e['summe']} |")
    z += ['', 'Zahl der Einheiten je Wert:', '', '| P10-Jahrgänge | Einheiten (Haupt oder Neben) | Einheiten (nur Haupt) |',
          '|---|---|---|']
    for w in range(13, -1, -1):
        z.append(f"| {w} | {sum(1 for _, _, e in einheiten if len(e['jahre']) == w)} "
                 f"| {sum(1 for _, _, e in einheiten if len(e['jahre_h']) == w)} |")
    z.append('')

    # Verteilung Typen
    mit = [(name, n, t) for name, n, t in typen if t['p10']]
    z += ['## Verteilung für die Schwelle „oft“ – Sek-I-Typen', '',
          f'Sortiert nach P10-Jahrgängen; aufgeführt die {len(mit)} Typen mit P10-Typ, die übrigen '
          f'{len(typen) - len(mit)} zählen unten unter 0.', '',
          '| Eintrag | Typ | P10-Jahrgänge | davon Haupt | P10-Typen |', '|---|---|---|---|---|']
    for name, n, t in sorted(mit, key=lambda x: (-len(x[2]['jahre']), -len(x[2]['jahre_h']), x[0], x[2]['nr'])):
        z.append(f"| {name} | {t['nr']} {t['text']} | {len(t['jahre'])} | {len(t['jahre_h'])} | {' · '.join(t['p10'])} |")
    z += ['', 'Zahl der Typen je Wert:', '', '| P10-Jahrgänge | Typen (Haupt oder Neben) | Typen (nur Haupt) |', '|---|---|---|']
    for w in range(13, -1, -1):
        z.append(f"| {w} | {sum(1 for _, _, t in typen if len(t['jahre']) == w)} "
                 f"| {sum(1 for _, _, t in typen if len(t['jahre_h']) == w)} |")
    z.append('')

    # Einheiten ohne P10
    z += ['## Sek-I-Einheiten ohne P10-Typ („keine P10-Aufgabe“)', '']
    for name, n, e in ohne:
        v = sek1_mess[name]['vermerk']
        z.append(f"- {name}, Einheit {n} · {e['titel']}" + (f" – themen.csv: „{v}“" if v else ''))
    z.append('')

    # Je Eintrag Sek I
    z += ['## Sek I je Eintrag', '']
    for name, m in sek1_mess.items():
        z.append(f'### {name}')
        z.append('')
        z.append('themen.csv: ' + (', '.join(f'„{t}“' for t in m['themen']) if m['themen'] else 'kein msa-Thema')
                 + (f" – Vermerk: „{m['vermerk']}“" if m['vermerk'] else '') + '.')
        if m['frei']:
            z.append('P10-Typen der Themen ohne Einheit in diesem Eintrag: ' + '; '.join(f'„{p}“' for p in m['frei']) + '.')
        z.append('')
        for n, e in m['einheiten'].items():
            z.append(f"**Einheit {n} · {e['titel']}** – P10-Jahrgänge {len(e['jahre'])} von 13 "
                     f"(davon Haupt {len(e['jahre_h'])}); P10-Typen {len(e['p10'])}; Summe ertrag {e['summe']}"
                     + ('' if e['p10'] else ' – keine P10-Aufgabe') + '.')
            z.append('')
            if e['p10']:
                z.append('| P10-Typ | ertrag | jahre_haupt | jahre_gesamt | erster | letzter | basis | kontext | Vermerk |')
                z.append('|---|---|---|---|---|---|---|---|---|')
                for p in e['p10']:
                    werte, vermerk = p10_zeile(p)
                    extra = []
                    if p in e['verfahren']:
                        extra.append('Verfahren für diesen Typ laut Zuordnungszeile (Typ in einer anderen Datei)')
                    if p in e['ausser']:
                        extra.append('nicht in der Zuordnungszeile der Einheit')
                    if p in e['ohne_typ']:
                        extra.append('kein Katalogtyp zugeordnet')
                    if vermerk:
                        extra.append(vermerk)
                    z.append(f"| {p} | " + ' | '.join(werte) + f" | {'; '.join(extra)} |")
                z.append('')
            for t in e['typen']:
                fremd = (' Außerhalb der Themen des Eintrags (zählt nicht): '
                         + ' · '.join(f'„{p}“' for p in t['fremd']) + '.') if t['fremd'] else ''
                if t['p10']:
                    z.append(f"- {t['nr']} {t['text']} → " + ' · '.join(f'„{p}“' for p in t['p10'])
                             + f" – P10-Jahrgänge {len(t['jahre'])} (Haupt {len(t['jahre_h'])})."
                             + fremd + (f" Grund: {t['grund']}" if t['grund'] else ' (wortgleich)'))
                elif t['fremd']:
                    z.append(f"- {t['nr']} {t['text']} → kein P10-Typ der eigenen Themen.{fremd} Grund: {t['grund']}")
                else:
                    z.append(f"- {t['nr']} {t['text']} → kein P10-Typ")
            z.append('')

    # Sek II
    z += ['## Sek II je Eintrag', '',
          'Abitur-Jahrgänge aus abi-katalog.csv (GK: 9 erfasste Jahrgänge 2018–2026; LK: 7, 2017, 2018, 2022–2026), '
          'FHR-Jahrgänge aus fhr-katalog.csv (8, 2019–2026); gezählt „Haupt oder Neben“, dazu „Haupt“ (nur als Hauptleistung); '
          'die Jahre stehen in Klammern, wenn es nicht alle sind. '
          'Der IQB-Pool zählt nicht; „nur Pool“ = der Typ hat nur Poolzeilen.', '']
    for name, einheiten2 in sek2_mess.items():
        z.append(f'### {name}' + (' (Sek-II-Teil eines Sek-I-Eintrags)' if name in sek1_mess else ''))
        z.append('')
        for n, e in einheiten2.items():
            z.append(f"**Einheit {n} · {e['titel']}** – Abitur-Jahrgänge GK {len(e['gk'][1])} von 9 (Haupt {len(e['gk'][0])}) · "
                     f"LK {len(e['lk'][1])} von 7 (Haupt {len(e['lk'][0])}) · FHR-Jahrgänge {len(e['fh'][1])} von 8 "
                     f"(Haupt {len(e['fh'][0])}).")
            z.append('')
            for t in e['typen']:
                if t['art'] == 'didaktisch':
                    z.append(f"- {t['nr']} {t['text']} → didaktischer Typ, kein Prüfungstyp")
                    continue
                if t['art'] == 'offen':
                    z.append(f"- {t['nr']} {t['text']} → offen: kein Prüfungstyp gefunden")
                    continue
                ziel = ' · '.join(f'„{a}“' for a in t['abi'] + [f for f in t['fhr'] if f not in t['abi']])
                def kurs(name, paar, alle):
                    if not paar[1]:
                        return f'{name} 0'
                    return f'{name} {jahrtext(paar[1], alle)}, Haupt {len(paar[0])}'
                werte = ' · '.join([kurs('GK', t['gk'], GK_JAHRE), kurs('LK', t['lk'], LK_JAHRE),
                                    kurs('FHR', t['fh'], FHR_JAHRE)])
                zusatz = ' · nur Pool' if t['pool'] else ''
                if not t['abi'] and not t['fhr']:
                    z.append(f"- {t['nr']} {t['text']} → kein Prüfungstyp. Grund: {t['grund']}")
                elif t['art'] == 'wortgleich':
                    z.append(f"- {t['nr']} {t['text']} → wortgleich; {werte}{zusatz}")
                else:
                    z.append(f"- {t['nr']} {t['text']} → {ziel}; {werte}{zusatz}. Grund: {t['grund']}")
            z.append('')
    return '\n'.join(z).rstrip('\n') + '\n'


def main():
    probe = '--probe' in sys.argv
    nur_typen = '--typen' in sys.argv
    fehler, typenliste, sek1_mess, sek2_mess, hilfen = baue()
    if nur_typen:
        with open(TYPENLISTE, 'w', encoding='utf-8', newline='\n') as f:
            f.write(typenliste)
        print(f'{os.path.relpath(TYPENLISTE, REPO)} geschrieben.')
        return
    if fehler:
        print(f'{len(fehler)} Prüffehler – nichts geschrieben:')
        for f in fehler[:200]:
            print('  ' + f)
        sys.exit(1)
    md = schreibe_md(sek1_mess, sek2_mess, hilfen)
    if probe:
        for p, inhalt in ((AUSGABE, md), (TYPENLISTE, typenliste)):
            alt = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
            print(f'{os.path.relpath(p, REPO)}: ' + ('unverändert' if alt == inhalt else 'weicht ab'))
        return
    for p, inhalt in ((AUSGABE, md), (TYPENLISTE, typenliste)):
        with open(p, 'w', encoding='utf-8', newline='\n') as f:
            f.write(inhalt)
    print(f'{os.path.relpath(AUSGABE, REPO)} und {os.path.relpath(TYPENLISTE, REPO)} geschrieben.')


if __name__ == '__main__':
    main()
