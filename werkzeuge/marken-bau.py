"""Marken je Lerneinheit – baut in den Katalogeinträgen die Zeile „Marken:“ unter jeder Nummernzeile und die
Klassenklammer hinter den Typen, die ein Verzeichnis einzeln nennt.

Liest:
- katalog/index.md – die Sek-I- und Sek-II-Einträge (Tabellen „Sekundarstufe I“ und „Sekundarstufe II“),
- katalog/_klassen-belege.md – Stellen, Typzeilen und Verlagsmarken je Sek-I-Einheit (Lesart im Kopf dort),
- katalog/_pruefungswort-belege.md – P10-Jahrgänge (Haupt oder Neben) je Sek-I-Einheit, Abitur-GK-, LK- und
  FHR-Jahrgänge je Sek-II-Einheit,
- katalog/_sek2-ordnung-belege.md – Halbjahr (Berlin, Brandenburg) und Kursart je Sek-II-Einheit,
- katalog/_marken-entscheidungen.md – Regel A und B, die Schwelle „P10 oft“ und die 38 Fälle (Gegenprobe der
  Stellenliste),
- werkzeuge/marken-bau-stellen.txt – die Lesart einzelner Stellen (Regel A, Stoff in einer anderen Einheit).

Schreibt in jeden Eintrag mit Lerneinheiten:
- unter jede Nummernzeile, zwei Leerzeichen eingerückt, eine Zeile
  Sek I:  „Marken: OS Kl. 9–10 (Sekundo 10, …) · GYM Kl. 9 · P10 oft · nicht für alle: Sekundo 8 LVL, …“
  Sek II: „Marken: BE Q1 · BB Q1 · GK · Abitur GK · Abitur LK · FHR“;
- hinter jeden Sek-I-Typ mit Typzeile die Klasse in eckigen Klammern („[OS 5, GYM 6]“);
- entfernt am Ende der Nummernzeile eine Klammer, die nur eine Klassenangabe enthält („(Kl. 7/8)“).
Wiederholbar: ein zweiter Lauf ersetzt vorhandene Marken-Zeilen und Klammern, statt sie zu verdoppeln.

Lesart (Auftrag Marken, archiv/auftrag-marken-2026-09-26.md; Entscheidungen im Bericht bericht-marken.md):
- Einführungsklasse einer Reihe = kleinste Klasse unter ihren zählenden Stellen. Es zählen nicht: Stellen, die
  die Stellenliste als Vorstufe liest (Regel A), Stellen mit Verlagsmarke (Regel B), die Nebenquelle
  Fundamente 2017 und die Förderhefte. Sekundo und mathe.delta beginnen in Klasse 7: ihre 7 zählt nicht, wenn
  eine andere Reihe derselben Schulform früher einführt (wie in _klassen-belege.md).
- „OS Kl. n“, wenn alle zählenden Reihen der Schulform in Klasse n einführen, sonst die Spanne mit der Liste
  der zählenden Reihen und ihrer Einführungsklasse; „OS –“ ohne zählende Stelle.
- Verlagsmarke (Regel B) = die Markenwörter aus Datei 2 und die übrigen Markenwörter der Lesart von
  _klassen-belege.md, dazu Zusatzstoff „*“, „(fakultativ)“ und das Zeichen „für Sonderseiten“. Keine Marke:
  Wiederholung (Datei 2), unerklärte Symbolzeichen und „Sonderfälle“ (siehe NICHT_MARKE).
- Typklammer: je Schulform die Einführungsklasse jeder Reihe mit Typzeile (gleiche 7er-Regel), eine Klasse
  oder die Spanne; Typzeilen mit Verlagsmarke zählen mit.
- Prüfungswort Sek I: P10-Jahrgänge ab der Schwelle aus Datei 2 „P10 oft“, ab 1 „P10“, sonst „keine
  P10-Aufgabe“. Sek II: „Abitur GK“, „Abitur LK“, „FHR“ je nach Jahrgängen, sonst „keine Prüfungsaufgabe“.
- Sek II: „BE Q1/2“ bei zwei Halbjahren, „BE –“ ohne Planstelle; Kursart „GK“ (Grund- und Leistungskurs, bei
  Länderunterschied „GK (BE nur LK)“), „nur LK“, „FOS“ (nur FOS-Stelle), „Kursart –“ (keine Stelle).

Aufruf aus der Repo-Wurzel: python werkzeuge/marken-bau.py – mit --probe wird gebaut und verglichen, nichts
geschrieben. Entstanden im Auftrag Marken (26.09.2026).
"""
import os, re, sys
from collections import OrderedDict, defaultdict

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
KAT = os.path.join(REPO, 'katalog')
STELLENLISTE = os.path.join(HIER, 'marken-bau-stellen.txt')
DATEI2 = os.path.join(KAT, '_marken-entscheidungen.md')

# Reihen wie in werkzeuge/klassen-belege.py: Schulform und erste Klasse des ersten Bands.
REIHEN = OrderedDict([
    ('Sekundo', ('OS', 7)), ('Mathematik 2023', ('OS', 5)), ('Schnittpunkt', ('OS', 5)),
    ('Mathematik heute', ('OS', 5)), ('LS', ('GYM', 5)), ('Fundamente', ('GYM', 5)),
    ('Fundamente 2017', ('NEBEN', 7)), ('Elemente', ('GYM', 5)), ('mathe.delta', ('GYM', 7))])
REIHE_RE = '|'.join(re.escape(r) for r in sorted(REIHEN, key=len, reverse=True))
KL_RE = r'Kl\. \d+(?: \(Ausgabe \d{4}\))?'

# Regel A: Stellen, deren Ermessenstext eines dieser Wörter enthält, brauchen eine Zeile in der Stellenliste.
REGEL_A_WOERTER = ['Vorstufe', 'Einstieg', 'Wiederaufnahme', 'Zeichnen', 'Benennen']

# Keine Verlagsmarke im Sinn von Regel B (Entscheidungen im Lauf, Bericht):
NICHT_MARKE = {
    'Wiederholung': 'Datei 2, Regel B: Wiederholungskapitel sind spätere Stellen',
    'Symbolzeichen': 'Zeichen, das das Verzeichnis nicht erklärt – kein Markenwort, Bedeutung unbekannt',
    'Sonderfälle': 'Wortanfang eines Inhaltstitels („Sonderfälle quadratischer Gleichungen“), keine Seitenart',
}

# Einheiten, die der Auftrag vor dem Lauf eingefügt hat (katalog/_marken-neue-einheiten.md) und die in den
# Belegdateien noch fehlen; Prüfungswort bis zum nächsten Bau von _pruefungswort-belege.md aus Datei 3.
NEUE_EINHEITEN = {('potenz-exponentialfunktionen', 5): 'keine P10-Aufgabe', ('daten', 7): 'keine P10-Aufgabe'}

# Gegenprobe des Auftrags (bekannte Werte); Abweichung wird gemeldet, nichts wird angepasst.
GEGENPROBE = [
    ('lineare-funktionen', 4, 'Marken', ['OS Kl. 8', 'GYM Kl. 8', 'P10 oft']),
    ('quadratische-gleichungen', 2, 'Marken', ['OS Kl. 10', 'GYM Kl. 9']),
    ('prozentrechnung', 1, 'Marken', ['GYM Kl. 5']),
    ('kreis', 1, 'ohne Kl. 5/6', []),
    ('kreis', 1, 'Typ', ['Kreis mit gegebenem Radius oder Durchmesser zeichnen', '[OS 5, GYM 6]']),
    ('potenz-exponentialfunktionen', 5, 'Marken', ['OS Kl. 10', 'GYM Kl. 9', 'keine P10-Aufgabe']),
    ('daten', 7, 'Marken', ['keine P10-Aufgabe']),
    ('kurvenuntersuchung', 1, 'Marken', ['BE Q1 · BB Q1 · GK']),
]

FEHLER = []
LOG = defaultdict(list)


def lies(pfad):
    with open(pfad, encoding='utf-8') as f:
        return f.read()


def abschnitt_bereich(zeilen, titel):
    """(erste, letzte+1) Zeilenindex des Abschnitts „### titel“ ohne Überschrift."""
    start = None
    for i, l in enumerate(zeilen):
        if start is None and l.strip() == '### ' + titel:
            start = i + 1
        elif start is not None and (l.startswith('### ') or l.startswith('## ')):
            return start, i
    return (start, len(zeilen)) if start is not None else (None, None)


# ---------------------------------------------------------------- Einträge
def eintraege():
    sek1, sek2, teil = [], [], None
    for l in lies(os.path.join(KAT, 'index.md')).splitlines():
        if l.startswith('## '):
            teil = {'## Sekundarstufe I': 1, '## Sekundarstufe II': 2}.get(l.strip())
            continue
        m = re.match(r'^\| ([a-z0-9-]+)\.md \|', l)
        if m and teil:
            (sek1 if teil == 1 else sek2).append(m.group(1))
    return sek1, sek2


# ---------------------------------------------------------------- Regel B: Markenwörter
def markenwoerter():
    """Markenwörter der Lesart von _klassen-belege.md und aus Datei 2."""
    kopf = lies(os.path.join(KAT, '_klassen-belege.md')).split('\n## Zahlen', 1)[0]
    m = re.search(r'^- Marken: jede zitierte Zeile, die mit einem Markenwort beginnt \(([^)]*)\) oder (.*?) enthält;',
                  kopf, re.M)
    if not m:
        sys.exit('_klassen-belege.md: Lesart der Marken nicht gefunden')
    lesart = [w.strip() for w in m.group(1).split(',')]
    lesart += re.findall(r'„([^“]+)“', m.group(2))              # Zum Selbstlernen, Wiederholung
    d2 = re.sub(r'\s+', ' ', lies(DATEI2))
    m2 = re.search(r'Stellen mit Verlagsmarke \((.*?)\) setzen', d2)
    if not m2 or 'übrigen Markenwörter der Lesart' not in m2.group(1):
        sys.exit('Datei 2: Liste der Verlagsmarken (Regel B) nicht gefunden')
    datei2 = []
    for w in re.split(r', | und ', m2.group(1)):
        w = w.strip()
        if w.startswith('Zusatzstoff'):
            datei2.append('Zusatzstoff')
        elif 'fakultativ' in w:
            datei2.append('fakultativ')
        elif not w.startswith('die übrigen'):
            datei2.append(w)
    if 'Wiederholungskapitel' not in d2 or 'keine Marke im Sinn dieser Regel' not in d2:
        sys.exit('Datei 2: Ausnahme Wiederholung nicht gefunden')
    alle = list(OrderedDict.fromkeys(datei2 + lesart + ['Sonderseite']))
    regel_b = [w for w in alle if w not in NICHT_MARKE]
    return lesart, regel_b


def schwelle():
    m = re.search(r'Schwelle (\d+) von (\d+) P10-Jahrgängen', re.sub(r'\s+', ' ', lies(DATEI2)))
    if not m:
        sys.exit('Datei 2: Schwelle „P10 oft“ nicht gefunden')
    return int(m.group(1)), int(m.group(2))


# ---------------------------------------------------------------- _klassen-belege.md
def klasse(kl):
    return int(re.match(r'Kl\. (\d+)', kl).group(1))


def lies_klassenbelege(lesart):
    """{eintrag: {nr: dict(titel, stellen, typzeilen, os, gym)}}"""
    daten = OrderedDict()
    e = u = None
    letzte = None
    stelle_re = re.compile(rf'^  - (?P<reihe>{REIHE_RE}) (?P<kl>{KL_RE})(?:, S\. (?P<s>[^:]*?))?: (?P<rest>„.*)$')
    rest_re = re.compile(r'^(?:„(?P<kap>.*?)“ \(Z\. [\d, ]+\) › )?„(?P<z>.*?)“ \(Z\. [\d, ]+\)(?P<zus>(?: – .*)?)$')
    typ_re = re.compile(rf'^  - Typ: (?P<typ>.*) – (?P<reihe>{REIHE_RE}) (?P<kl>{KL_RE})(?:, S\. [^:]*?)?: „(?P<z>.*)“$')
    item_re = re.compile(rf'^(?P<reihe>{REIHE_RE}) (?P<kl>{KL_RE}): (?P<rest>.*)$')
    for nr_z, l in enumerate(lies(os.path.join(KAT, '_klassen-belege.md')).splitlines(), 1):
        m = re.match(r'^### (\S+) – ', l)
        if m:
            e = m.group(1); daten[e] = OrderedDict(); u = None; continue
        if e is None:
            continue
        m = re.match(r'^- (\d+)\. (.*)$', l)
        if m:
            u = int(m.group(1))
            daten[e][u] = dict(titel=m.group(2), stellen=[], typzeilen=[], os='', gym='')
            letzte = None
            continue
        if re.match(r'^- (Spanne|Boden|Ermessen \(|Verortung)', l):
            u = None; continue
        if u is None:
            continue
        einheit = daten[e][u]
        if l.startswith('    Ermessen: '):
            if letzte is not None:
                letzte['erm'].append(l[len('    Ermessen: '):])
            continue
        m = stelle_re.match(l)
        if m:
            mr = rest_re.match(m.group('rest'))
            if not mr:
                FEHLER.append(f'_klassen-belege.md Z. {nr_z}: Stelle nicht lesbar: {l}'); continue
            letzte = dict(eintrag=e, nr=u, reihe=m.group('reihe'), kl=m.group('kl'), klasse=klasse(m.group('kl')),
                          zitat=mr.group('z'), zeile=nr_z, erm=[], marken=[], nachgetragen=[])
            einheit['stellen'].append(letzte)
            continue
        letzte = None                                   # „    Ermessen:“ hinter Förderheft- und anderen Zeilen
        m = typ_re.match(l)
        if m:
            # der letzte Typ einer Zeile steht in der Belegdatei mit dem Satzpunkt; die Klammer gehört davor
            einheit['typzeilen'].append(dict(typ=m.group('typ').rstrip('.'), reihe=m.group('reihe'), kl=m.group('kl'),
                                             zitat=m.group('z'), zeile=nr_z))
            continue
        if l.startswith('  - Marken: '):
            inhalt = l[len('  - Marken: '):]
            if inhalt == 'keine':
                continue
            for item in re.split(rf'; (?=(?:{REIHE_RE}) Kl\. \d)', inhalt):
                mi = item_re.match(item)
                if not mi:
                    FEHLER.append(f'_klassen-belege.md Z. {nr_z}: Marke nicht lesbar: {item}'); continue
                rest = mi.group('rest')
                if ' bei „' in rest:
                    text, _, z = rest.rpartition(' bei „')
                    z = z[:-1]
                    if 'Wiederholung' in text:
                        lab = 'Wiederholung'
                    elif text.startswith('Zusatzstoff'):
                        lab = 'Zusatzstoff'
                    elif 'fakultativ' in text:
                        lab = 'fakultativ'
                    elif 'Symbol des Originals für Sonderseiten' in text:
                        lab = 'Sonderseite'
                    elif 'im Verzeichnis nicht erklärt' in text:
                        lab = 'Symbolzeichen'
                    else:
                        FEHLER.append(f'_klassen-belege.md Z. {nr_z}: Marke unbekannter Art: {item}'); continue
                    labs = [lab]
                else:
                    z = rest[1:-1]
                    enthalten = {'Zum Selbstlernen': r'Zum Se.bstlernen', 'Wiederholung': r'\(Wiederholung\)|Wiederholung:'}
                    labs = [w for w in lesart if (re.search(enthalten[w], z) if w in enthalten else z.startswith(w))]
                    if not labs:
                        FEHLER.append(f'_klassen-belege.md Z. {nr_z}: kein Markenwort in {item}'); continue
                treffer = [s for s in einheit['stellen'] if (s['reihe'], s['kl'], s['zitat']) == (mi.group('reihe'), mi.group('kl'), z)]
                if len(treffer) != 1:
                    FEHLER.append(f'_klassen-belege.md Z. {nr_z}: Marke ohne eindeutige Stelle: {item}'); continue
                for lab in labs:
                    if lab not in treffer[0]['marken']:
                        treffer[0]['marken'].append(lab)
            continue
        m = re.match(r'^  - (OS|GYM): (.*)$', l)
        if m:
            einheit['os' if m.group(1) == 'OS' else 'gym'] = m.group(2)
    return daten


def marken_nachtragen(belege, regel_b):
    """Verlagsmarke am Zeilenanfang, die die Marken-Zeile der Belegdatei nicht führt (etwa „Im Blickpunkt;“
    mit Strichpunkt oder „Q LVL:“ hinter einem verstümmelten Zeichen)."""
    woerter = [w for w in regel_b if w not in ('Zusatzstoff', 'fakultativ', 'Sonderseite', 'Zum Selbstlernen')]
    muster = re.compile(r'^(?:\S{1,3} )?(' + '|'.join(re.escape(w) for w in woerter) + r')\s*[:;]')
    for e, einheiten in belege.items():
        for u, d in einheiten.items():
            for s in d['stellen']:
                if REIHEN[s['reihe']][0] == 'NEBEN':
                    continue
                neu = []
                m = muster.match(s['zitat'])
                if m and m.group(1) not in s['marken']:
                    neu.append(m.group(1))
                if re.search(r'Zum Se.bstlernen', s['zitat']) and 'Zum Selbstlernen' not in s['marken']:
                    neu.append('Zum Selbstlernen')
                for w in neu:
                    s['marken'].append(w); s['nachgetragen'].append(w)
                    LOG['marke nachgetragen'].append(f'{e} {u}, {s["reihe"]} {s["kl"]}: „{s["zitat"]}“ – {w}')


# ---------------------------------------------------------------- Stellenliste
def lies_stellenliste():
    liste = []
    for nr_z, l in enumerate(lies(STELLENLISTE).splitlines(), 1):
        if not l.strip() or l.startswith('#'):
            continue
        teile = l.split(' | ')
        if len(teile) < 7:
            FEHLER.append(f'marken-bau-stellen.txt Z. {nr_z}: weniger als sieben Felder'); continue
        e, u, rk, z = teile[:4]
        quelle, grund = teile[-2], teile[-1]
        wirkung = ' | '.join(teile[4:-2])
        m = re.match(rf'^({REIHE_RE}) ({KL_RE})$', rk)
        if not m or not u.isdigit() or quelle not in ('Datei 2', 'eigen'):
            FEHLER.append(f'marken-bau-stellen.txt Z. {nr_z}: Feld nicht lesbar: {l}'); continue
        w = dict(zeile=nr_z, eintrag=e, nr=int(u), reihe=m.group(1), kl=m.group(2), zitat=z, quelle=quelle, grund=grund)
        mt = re.match(r'^Typ ([a-z0-9-]+) (\d+): (.+)$', wirkung)
        me = re.match(r'^Einheit (\d+)$', wirkung)
        if wirkung in ('gilt', 'ohne Klasse'):
            w['art'] = wirkung
        elif me:
            w['art'], w['ziel'] = 'Einheit', int(me.group(1))
        elif mt:
            w['art'], w['ziel_eintrag'], w['ziel'], w['typ'] = 'Typ', mt.group(1), int(mt.group(2)), mt.group(3)
        else:
            FEHLER.append(f'marken-bau-stellen.txt Z. {nr_z}: Wirkung unbekannt: {wirkung}'); continue
        liste.append(w)
    return liste


def pruefe_datei2(liste):
    """Jeder der 38 Fälle aus Datei 2 hat mindestens eine Zeile mit Quelle „Datei 2“ und umgekehrt."""
    faelle = []
    zahlwort = {'zwei': 2, 'drei': 3, 'vier': 4, 'fünf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9}
    anzahl = 0
    for l in lies(DATEI2).splitlines():
        m = re.match(r'^\| ([a-z0-9-]+) \| (\d+) \| (.*?) \| (.*?) \| (.*?) \|$', l)
        if m:
            faelle.append((m.group(1), int(m.group(2)), m.group(3)))
            anzahl += zahlwort.get(m.group(3).split()[0], 1)      # „sieben Stellen …“ sind sieben Fälle

    def passt(w, fall):
        e, u, text = fall
        k = klasse(w['kl'])
        return (w['eintrag'], w['nr']) == (e, u) and (f'{w["reihe"]} {k}' in text or f'{w["reihe"]} Kl. {k}' in text)

    d2 = [w for w in liste if w['quelle'] == 'Datei 2']
    for fall in faelle:
        stellen = {(w['reihe'], w['kl'], w['zitat']) for w in d2 if passt(w, fall)}
        soll = zahlwort.get(fall[2].split()[0], 1)
        if len(stellen) < soll:
            FEHLER.append(f'Datei 2: Fall mit {len(stellen)} statt {soll} Stellen in der Stellenliste: {fall[0]} {fall[1]} {fall[2]}')
    for w in d2:
        if not any(passt(w, fall) for fall in faelle):
            FEHLER.append(f'marken-bau-stellen.txt Z. {w["zeile"]}: Quelle „Datei 2“, aber kein Fall dort')
    return len(faelle), anzahl


# ---------------------------------------------------------------- _pruefungswort-belege.md
def lies_pruefungswort():
    sek1, sek2 = {}, {}
    teil = e = None
    for l in lies(os.path.join(KAT, '_pruefungswort-belege.md')).splitlines():
        if l.startswith('## '):
            teil = {'## Sek I je Eintrag': 1, '## Sek II je Eintrag': 2}.get(l.strip()); e = None; continue
        m = re.match(r'^### ([a-z0-9-]+)', l)
        if m:
            e = m.group(1); continue
        if teil == 1 and e:
            m = re.match(r'^\*\*Einheit (\d+) · .*?\*\* – P10-Jahrgänge (\d+) von (\d+)', l)
            if m:
                sek1[(e, int(m.group(1)))] = int(m.group(2))
        elif teil == 2 and e:
            m = re.match(r'^\*\*Einheit (\d+) · .*?\*\* – Abitur-Jahrgänge GK (\d+) von \d+ \(Haupt \d+\) · '
                         r'LK (\d+) von \d+ \(Haupt \d+\) · FHR-Jahrgänge (\d+) von \d+', l)
            if m:
                sek2[(e, int(m.group(1)))] = tuple(int(m.group(i)) for i in (2, 3, 4))
    return sek1, sek2


# ---------------------------------------------------------------- _sek2-ordnung-belege.md
def lies_sek2_ordnung():
    daten = {}
    e = u = None
    for l in lies(os.path.join(KAT, '_sek2-ordnung-belege.md')).splitlines():
        m = re.match(r'^### ([a-z0-9-]+)$', l)
        if m:
            e, u = m.group(1), None; continue
        m = re.match(r'^- (\d+)\. ', l)
        if m and e:
            u = int(m.group(1)); daten[(e, u)] = dict(fos=False); continue
        if u is None:
            continue
        d = daten[(e, u)]
        if l.startswith('  - FOS, Z.'):
            d['fos'] = True
        elif l.startswith('  - Halbjahr: '):
            m = re.match(r'^  - Halbjahr: (.*?) · Bigalke/Köhler.*? · GK/LK: (.*) · Bigalke/Köhler', l)
            if not m:
                FEHLER.append(f'_sek2-ordnung-belege.md {e} {u}: Halbjahr nicht lesbar'); continue
            d['halbjahr'], d['gklk'] = m.group(1), m.group(2)
        elif l.startswith('  - nur LK: '):
            d['nur_lk'] = l[len('  - nur LK: '):].startswith('ja')
    return daten


def laender(text):
    """„Q3 (Berlin und Brandenburg)“, „Berlin Q4 · Brandenburg Q2“, „Berlin Q3“, „keine Planstelle“ ->
    {'BE': …, 'BB': …} (None ohne Stelle)."""
    if text == 'keine Planstelle':
        return {'BE': None, 'BB': None}
    m = re.match(r'^(.*) \(Berlin und Brandenburg\)$', text)
    if m:
        return {'BE': m.group(1), 'BB': m.group(1)}
    out = {'BE': None, 'BB': None}
    for teil in text.split(' · '):
        m = re.match(r'^(Berlin|Brandenburg) (.*)$', teil)
        if not m:
            raise ValueError(text)
        out['BE' if m.group(1) == 'Berlin' else 'BB'] = m.group(2)
    return out


def halbjahr(q):
    return '–' if not q else re.sub(r'/Q', '/', q)       # Q1/Q2 -> Q1/2


def sek2_marken(e, u, ordnung, pruef, kein_typ=False):
    d = ordnung.get((e, u))
    if d is None or 'halbjahr' not in d:
        FEHLER.append(f'{e} {u}: keine Halbjahreszeile in _sek2-ordnung-belege.md'); return None
    try:
        hj, kurs = laender(d['halbjahr']), laender(d['gklk'])
    except ValueError as x:
        FEHLER.append(f'{e} {u}: Halbjahr oder GK/LK nicht lesbar: {x}'); return None
    werte = {k: v for k, v in kurs.items() if v}
    if werte and set(werte.values()) == {'nur LK'}:
        kursart = 'nur LK'
    elif 'GK und LK' in werte.values():
        kursart = 'GK' + ''.join(f' ({k} nur LK)' for k, v in werte.items() if v == 'nur LK')
    elif not werte:
        kursart = 'FOS' if d['fos'] else 'Kursart –'
    else:
        FEHLER.append(f'{e} {u}: Kursart unbekannt: {d["gklk"]}'); return None
    if (kursart == 'nur LK') != d.get('nur_lk', False):
        FEHLER.append(f'{e} {u}: „nur LK“ widerspricht der GK/LK-Angabe')
    if (e, u) in pruef:
        gk, lk, fhr = pruef[(e, u)]
    elif kein_typ:
        # Typzeile „Einheit n: kein Typ – …“: die Belegdatei führt die Einheit nicht, weil sie keinen Typ hat
        gk = lk = fhr = 0
        LOG['Sek II ohne Typ (keine Prüfungsaufgabe)'].append(f'{e} {u}')
    else:
        FEHLER.append(f'{e} {u}: keine Sek-II-Zeile in _pruefungswort-belege.md'); return None
    worte = [w for w, n in (('Abitur GK', gk), ('Abitur LK', lk), ('FHR', fhr)) if n >= 1] or ['keine Prüfungsaufgabe']
    return ' · '.join([f'BE {halbjahr(hj["BE"])}', f'BB {halbjahr(hj["BB"])}', kursart] + worte)


# ---------------------------------------------------------------- Sek I: Stellen zuordnen
def einfuehrung(klassen):
    """{reihe: [Klassen]} einer Schulform -> ({reihe: Einführungsklasse} der zählenden Reihen)."""
    e = {r: min(k) for r, k in klassen.items() if k}
    zens = [r for r, v in e.items() if REIHEN[r][1] >= 7 and v == REIHEN[r][1] and any(w < v for o, w in e.items() if o != r)]
    return {r: v for r, v in e.items() if r not in zens}


def schulform_text(form, klassen, mit_liste=True):
    eff = einfuehrung(klassen)
    if not eff:
        return f'{form} –'
    lo, hi = min(eff.values()), max(eff.values())
    if lo == hi:
        return f'{form} Kl. {lo}' if mit_liste else f'{form} {lo}'
    if not mit_liste:
        return f'{form} {lo}–{hi}'
    liste = ', '.join(f'{r} {eff[r]}' for r in REIHEN if r in eff)
    return f'{form} Kl. {lo}–{hi} ({liste})'


def sek1_zuordnen(belege, stellenliste, sek1):
    """Wendet die Stellenliste an. Ergebnis je (eintrag, nr): zaehlt, nfa (Stellen mit Marke), typzeilen."""
    einheit = defaultdict(lambda: dict(zaehlt=[], nfa=[], typzeilen=[]))
    wirkung = defaultdict(list)
    for w in stellenliste:
        d = belege.get(w['eintrag'], {}).get(w['nr'])
        treffer = [s for s in (d['stellen'] if d else []) if (s['reihe'], s['kl'], s['zitat']) == (w['reihe'], w['kl'], w['zitat'])]
        if len(treffer) != 1:
            FEHLER.append(f'marken-bau-stellen.txt Z. {w["zeile"]}: {len(treffer)} Stellen in _klassen-belege.md'); continue
        wirkung[id(treffer[0])].append(w)
        w['stelle'] = treffer[0]
    # Regel A: jede Stelle mit Stichwort im Ermessenstext steht in der Stellenliste
    for e in sek1:
        for u, d in belege.get(e, {}).items():
            for s in d['stellen']:
                if any(re.search(x, t, re.I) for x in REGEL_A_WOERTER for t in s['erm']) and id(s) not in wirkung:
                    FEHLER.append(f'Regel A: {e} {u}, {s["reihe"]} {s["kl"]} „{s["zitat"]}“ fehlt in der Stellenliste')
    for e in sek1:
        for u, d in belege.get(e, {}).items():
            typ_von = defaultdict(list)
            for t in d['typzeilen']:
                typ_von[(t['reihe'], t['kl'], t['zitat'])].append(t)
            schluessel = {(s['reihe'], s['kl'], s['zitat']) for s in d['stellen']}
            for k, ts in typ_von.items():
                if k not in schluessel:
                    FEHLER.append(f'_klassen-belege.md Z. {ts[0]["zeile"]}: Typzeile ohne Stelle in {e} {u}')
            for s in d['stellen']:
                if REIHEN[s['reihe']][0] == 'NEBEN':
                    continue
                ws = wirkung.get(id(s), [])
                arten = {w['art'] for w in ws}
                ziele = [w['ziel'] for w in ws if w['art'] == 'Einheit']
                if not ws or 'gilt' in arten:
                    ziele.append(u)
                for z in ziele:
                    (einheit[(e, z)]['nfa'] if set(s['marken']) & REGEL_B else einheit[(e, z)]['zaehlt']).append(s)
                eigene = typ_von.get((s['reihe'], s['kl'], s['zitat']), [])
                if u in ziele or 'ohne Klasse' in arten or 'Typ' in arten:
                    for t in eigene:
                        einheit[(e, u)]['typzeilen'].append((t['typ'], s))
                elif eigene:
                    for t in eigene:
                        LOG['Typzeile entfällt'].append(f'{e} {u}: „{t["typ"]}“ – {s["reihe"]} {s["kl"]} „{s["zitat"]}“ '
                                                        f'(Stelle gilt jetzt für Einheit {", ".join(map(str, ziele))})')
                for w in ws:
                    if w['art'] == 'Typ':
                        ziel = einheit[(w['ziel_eintrag'], w['ziel'])]
                        ziel['typzeilen'].append((w['typ'], s))
                        if set(s['marken']) & REGEL_B and s not in ziel['nfa']:
                            ziel['nfa'].append(s)
    return einheit


def nfa_text(stellen):
    teile = []
    for form in ('OS', 'GYM'):
        for r in REIHEN:
            if REIHEN[r][0] != form:
                continue
            for s in sorted((s for s in stellen if s['reihe'] == r), key=lambda s: (s['klasse'], s['zeile'])):
                for m in s['marken']:
                    if m in REGEL_B:
                        teile.append(f'{r} {s["klasse"]} {m}')
    return ', '.join(OrderedDict.fromkeys(teile))


def typklammer(zeilen):
    """[(typ, stelle)] eines Typs -> „OS 5, GYM 5–6“."""
    teile = []
    for form in ('OS', 'GYM'):
        klassen = defaultdict(list)
        for _, s in zeilen:
            if REIHEN[s['reihe']][0] == form:
                klassen[s['reihe']].append(s['klasse'])
        if klassen:
            teile.append(schulform_text(form, klassen, mit_liste=False))
    return ', '.join(teile)


# ---------------------------------------------------------------- Einträge umschreiben
KLASSENKLAMMER = re.compile(r' \(Kl\. \d+(?:[/–-]\d+)?\)$')
TYPKLAMMER = re.compile(r' \[(?:OS|GYM) [^\]]*\]')


def endklammer(text):
    """Letzte Klammer am Ende von text (ohne Leerzeichen davor) oder None."""
    if not text.endswith(')'):
        return None
    tiefe = 0
    for i in range(len(text) - 1, -1, -1):
        if text[i] == ')':
            tiefe += 1
        elif text[i] == '(':
            tiefe -= 1
            if tiefe == 0:
                return text[i:]
    return None


def typ_einsetzen(zeile, typ, klammer):
    kopf = re.match(r'^\s*[-*]?\s*Einheit \d+:\s*', zeile).end()
    stellen = []
    start = 0
    while True:
        p = zeile.find(typ, start)
        if p < 0:
            break
        start = p + 1
        vor, nach = zeile[:p], zeile[p + len(typ):]
        if not (p == kopf or vor.endswith(' · ')):
            continue
        if not (nach == '' or nach.startswith(' · ') or nach.startswith(' —') or re.match(r'^\.(\s|$)', nach)):
            continue
        stellen.append(p)
    if len(stellen) != 1:
        return None
    p = stellen[0] + len(typ)
    return zeile[:p] + f' [{klammer}]' + zeile[p:]


def eintrag_bauen(e, text, marken, klammern, zahlen):
    zeilen = text.split('\n')
    a, b = abschnitt_bereich(zeilen, 'Lerneinheiten')
    if a is None:
        return text, []
    einheiten_im_eintrag = []
    neu = zeilen[:a]
    i = a
    while i < b:
        l = zeilen[i]
        i += 1
        if l.startswith('  Marken: '):
            continue                                    # alte Marken-Zeile, wird neu gebaut
        m = re.match(r'^(\d+)\.\s', l)
        if not m:
            neu.append(l); continue
        u = int(m.group(1))
        einheiten_im_eintrag.append(u)
        vor, sep, eingabe = l.partition(' ← Eingabe')
        vor_r = vor.rstrip()
        if KLASSENKLAMMER.search(vor_r):
            zahlen['entfernt'].append(f'{e} {u}: {KLASSENKLAMMER.search(vor_r).group(0).strip()}')
            vor_r = KLASSENKLAMMER.sub('', vor_r)
            l = vor_r + sep + eingabe
        else:
            k = endklammer(vor_r)
            if k and re.search(r'Kl\.|Klasse|\bQ[1-4]\b|Q[1-4][ ,;/)]', k):
                zahlen['geblieben'].append(f'{e} {u}: {k}')
            elif k:
                zahlen['andere Klammer'].append(f'{e} {u}: {k}')
        neu.append(l)
        if (e, u) not in marken:
            FEHLER.append(f'{e} {u}: keine Marken gebaut'); continue
        neu.append('  Marken: ' + marken[(e, u)])
    neu += zeilen[b:]
    # Typen je Lerneinheit
    a, b = abschnitt_bereich(neu, 'Typen je Lerneinheit')
    if a is not None:
        for j in range(a, b):
            m = re.match(r'^\s*[-*]?\s*Einheit (\d+):', neu[j])
            if not m:
                continue
            u = int(m.group(1))
            z = TYPKLAMMER.sub('', neu[j])
            for typ, kl in sorted(klammern.get((e, u), {}).items(), key=lambda x: -len(x[0])):
                z2 = typ_einsetzen(z, typ, kl)
                if z2 is None:
                    FEHLER.append(f'{e} {u}: Typ „{typ}“ nicht eindeutig in der Typzeile'); continue
                z = z2
                zahlen['typklammern'] += 1
            neu[j] = z
    return '\n'.join(neu), einheiten_im_eintrag


# ---------------------------------------------------------------- Hauptteil
def main(probe=False):
    global REGEL_B
    sek1, sek2 = eintraege()
    lesart, regel_b = markenwoerter()
    REGEL_B = set(regel_b)
    oft, von = schwelle()
    belege = lies_klassenbelege(lesart)
    marken_nachtragen(belege, regel_b)
    stellenliste = lies_stellenliste()
    faelle = pruefe_datei2(stellenliste)
    pw1, pw2 = lies_pruefungswort()
    ordnung = lies_sek2_ordnung()
    if sorted(belege) != sorted(sek1):
        FEHLER.append(f'_klassen-belege.md: Einträge weichen von index.md ab: {set(belege) ^ set(sek1)}')
    zuordnung = sek1_zuordnen(belege, stellenliste, sek1)
    if FEHLER:
        return FEHLER

    marken, klammern = {}, defaultdict(dict)
    zahlen = dict(entfernt=[], geblieben=[], typklammern=0, **{'andere Klammer': []})
    sek2_einheiten = {k for k in ordnung if k[0] in sek1}
    geaendert, einheiten_gesamt = [], defaultdict(int)
    ergebnisse = OrderedDict()
    for e in sek1 + sek2:
        pfad = os.path.join(KAT, e + '.md')
        text = lies(pfad)
        zeilen = text.split('\n')
        a, b = abschnitt_bereich(zeilen, 'Lerneinheiten')
        nummern = [int(m.group(1)) for l in (zeilen[a:b] if a is not None else []) for m in [re.match(r'^(\d+)\.\s', l)] if m]
        for u in nummern:
            if e in sek2 or (e, u) in sek2_einheiten:
                t = sek2_marken(e, u, ordnung, pw2, kein_typ=bool(re.search(rf'^Einheit {u}: kein Typ\b', text, re.M)))
                if t is not None:
                    marken[(e, u)] = t
                einheiten_gesamt['Sek II'] += 1
                continue
            einheiten_gesamt['Sek I'] += 1
            z = zuordnung.get((e, u), dict(zaehlt=[], nfa=[], typzeilen=[]))
            if u not in belege.get(e, {}) and (e, u) not in NEUE_EINHEITEN:
                FEHLER.append(f'{e} {u}: Einheit fehlt in _klassen-belege.md'); continue
            teile = []
            for form in ('OS', 'GYM'):
                klassen = defaultdict(list)
                for s in z['zaehlt']:
                    if REIHEN[s['reihe']][0] == form:
                        klassen[s['reihe']].append(s['klasse'])
                teile.append(schulform_text(form, klassen))
            if (e, u) in pw1:
                n = pw1[(e, u)]
                teile.append('P10 oft' if n >= oft else 'P10' if n >= 1 else 'keine P10-Aufgabe')
            elif (e, u) in NEUE_EINHEITEN:
                teile.append(NEUE_EINHEITEN[(e, u)])
                LOG['Prüfungswort aus Datei 3'].append(f'{e} {u}: {NEUE_EINHEITEN[(e, u)]} (Einheit fehlt in _pruefungswort-belege.md)')
            else:
                FEHLER.append(f'{e} {u}: keine P10-Zeile in _pruefungswort-belege.md'); continue
            nfa = nfa_text(z['nfa'])
            if nfa:
                teile.append('nicht für alle: ' + nfa)
            marken[(e, u)] = ' · '.join(teile)
            je_typ = defaultdict(list)
            for typ, s in z['typzeilen']:
                if REIHEN[s['reihe']][0] in ('OS', 'GYM') and (typ, s) not in je_typ[typ]:
                    je_typ[typ].append((typ, s))
            for typ, liste in je_typ.items():
                klammern[(e, u)][typ] = typklammer(liste)
        neu, _ = eintrag_bauen(e, text, marken, klammern, zahlen)
        ergebnisse[e] = (pfad, text, neu)
    # Typzeilen an Einheiten ohne Nummernzeile oder an fremden Einträgen ohne Treffer
    for (e, u), d in zuordnung.items():
        if d['typzeilen'] and (e, u) not in marken:
            FEHLER.append(f'{e} {u}: Typzeilen an einer Einheit ohne Marken')
    if FEHLER:
        return FEHLER

    for e, (pfad, alt, neu) in ergebnisse.items():
        if neu != alt:
            geaendert.append(e)
            if not probe:
                with open(pfad, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(neu)
                roh = open(pfad, 'rb').read()
                assert not roh.startswith(b'\xef\xbb\xbf') and b'\r' not in roh, pfad
                assert roh.decode('utf-8') == neu, pfad

    # ---------------- Ausgabe
    print(f'Datei 2: {faelle[1]} Fälle in {faelle[0]} Tabellenzeilen, alle in der Stellenliste; Schwelle „P10 oft“: {oft} von {von}.')
    print(f'Regel B, Verlagsmarken: {", ".join(regel_b)}; keine Marke: {", ".join(NICHT_MARKE)}.')
    print(f'Einträge: {len(sek1)} Sek I, {len(sek2)} Sek II; {"zu ändern" if probe else "geändert"}: {len(geaendert)}.')
    print(f'Marken-Zeilen: {len(marken)} (Sek-I-Einheiten {einheiten_gesamt["Sek I"]}, Sek-II-Einheiten {einheiten_gesamt["Sek II"]}); '
          f'Typklammern: {zahlen["typklammern"]}; Klammern „(Kl. n)“ entfernt: {len(zahlen["entfernt"])}; '
          f'Klassenklammern mit mehr Inhalt geblieben: {len(zahlen["geblieben"])}; andere Endklammern: {len(zahlen["andere Klammer"])}.')
    nfa = [(k, v) for k, v in marken.items() if 'nicht für alle:' in v]
    print(f'Zeilen mit „nicht für alle“: {len(nfa)}.')
    print('Gegenprobe (bekannte Werte des Auftrags; Abweichung ist ein Befund):')
    for e, u, art, soll in GEGENPROBE:
        ist = marken.get((e, u), '–')
        if art == 'Marken':
            # Schulformangaben müssen als ganzer Teil stimmen („OS Kl. 8“ ≠ „OS Kl. 7–8 (…)“), der Rest als Text
            ok = all(x in ist.split(' · ') if x.startswith(('OS ', 'GYM ')) else x in ist for x in soll)
            print(f'  {"stimmt" if ok else "ABWEICHUNG"}: {e} {u} – Soll {" · ".join(soll)} – Ist {ist}')
        elif art == 'ohne Kl. 5/6':
            teile = [t for t in ist.split(' · ') if t.startswith(('OS', 'GYM'))]
            ok = not any(re.search(r'\b[56]\b', t) for t in teile)
            print(f'  {"stimmt" if ok else "ABWEICHUNG"}: {e} {u} – Soll: weder OS noch GYM nennt Kl. 5 oder 6 – Ist {" · ".join(teile)}')
        else:
            k = klammern.get((e, u), {}).get(soll[0], '–')
            print(f'  {"stimmt" if "[" + k + "]" == soll[1] else "ABWEICHUNG"}: {e} {u} Typ „{soll[0]}“ – Soll {soll[1]} – Ist [{k}]')
    for titel, liste in (('Klammern „(Kl. n)“ entfernt', zahlen['entfernt']),
                         ('Klassenklammern mit mehr Inhalt geblieben', zahlen['geblieben']),
                         ('andere Endklammern (keine Klassenangabe, unberührt)', zahlen['andere Klammer'])):
        print(f'{titel} ({len(liste)}):')
        for x in liste:
            print('  ' + x)
    for titel, liste in LOG.items():
        print(f'{titel} ({len(liste)}):')
        for x in liste:
            print('  ' + x)
    print('Einheiten mit „OS –“ oder „GYM –“:')
    for (e, u), v in marken.items():
        if v.startswith('OS –') or ' · GYM – ' in v or v.endswith(' · GYM –'):
            print(f'  {e} {u}: {v}')
    print('Marken-Zeilen:')
    for (e, u), v in marken.items():
        print(f'  {e} {u}: {v}')
    print('Typklammern:')
    for (e, u), d in klammern.items():
        for typ, k in d.items():
            print(f'  {e} {u}: {typ} [{k}]')
    if probe:
        print('Probe: ' + ('nichts zu ändern' if not geaendert else f'{len(geaendert)} Einträge würden sich ändern: '
                           + ', '.join(geaendert)) + ' – nichts geschrieben')
    return []


REGEL_B = set()

if __name__ == '__main__':
    fehler = main(probe='--probe' in sys.argv[1:])
    if fehler:
        print('FEHLER – nichts geschrieben:')
        for f in fehler:
            print('  ' + f)
        sys.exit(1)
