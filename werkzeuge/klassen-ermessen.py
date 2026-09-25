"""Ermessensfälle der Klassenbelege, nach Sorte des Grundes gruppiert (v0.2, 27.09.2026; v0.1 26.09.2026).

v0.2 (Auftrag Nacht 2026-09-27, Teil 4): steht derselbe Grund an mehreren Stellen eines Eintrags, kommt das Zitat
aus der Stelle der eigenen Reihe (Präfix „Einheit n, <Reihe> Kl. k:“) und Einheit, nicht mehr aus der ersten
(Nebenbefund in katalog/_marken-entscheidungen.md: fünfmal das Zitat von Mathematik 2023 bei den Potenzfunktionen).

Liest katalog/_klassen-belege.md und schreibt katalog/_klassen-ermessen.md: alle Ermessensfälle mit Eintrag,
Einheit, Reihe, Zitat und Grund, gruppiert nach der Sorte des Grundes; oben die Sorten mit Zahl. Keine Bewertung,
keine Änderung an der Quelle. Aufruf aus der Repo-Wurzel: python werkzeuge/klassen-ermessen.py
(--probe: nur bauen und mit der vorhandenen Datei vergleichen).

Lesart
- Ein Fall ist ein Punkt der Liste „- Ermessen (n):“ am Schluss eines Eintrags (dort gezählt, Zahlenblock
  „Ermessensfälle gesamt“). Präfix „Einheit n, <Reihe>:“ bzw. „Einheiten …, <Reihe>:“ oder nur „Einheit n:“.
- Zitat: die Verzeichniszeile, unter der derselbe Grund im Eintrag als „Ermessen:“ steht (Zitat in „…“ mit
  Zeilennummer „Z.“ der Quelldatei); bei Förderheft-Blöcken die Förderheftzeile mit dem Blocktitel; „–“, wenn
  der Grund für die ganze Einheit gilt und an keiner Zeile steht. Reihe: aus dem Präfix, sonst der Name der
  Reihe am Anfang des Grundes.
- Sorte: die erste Regel aus SORTEN, deren Muster im Grund vorkommt (Reihenfolge wie dort); die Muster sind aus dem
  Wortlaut der 250 Gründe abgeleitet. Die letzte Sorte nimmt alles Übrige.
- Gegenprobe: Summe der Fälle gegen die Zahl im Zahlenblock (Abweichung wird gemeldet, nicht angepasst).

Entstanden im Auftrag Nacht 2026-09-26, Teil 4.
"""
import os
import re
import sys
from collections import OrderedDict

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
QUELLE = os.path.join(REPO, 'katalog', '_klassen-belege.md')
AUSGABE = os.path.join(REPO, 'katalog', '_klassen-ermessen.md')

REIHEN = ['Mathematik heute', 'Mathematik 2023', 'Sekundo', 'Schnittpunkt', 'LS', 'Fundamente', 'Elemente',
          'mathe.delta']

# (Sorte, Muster, Erklärung) – Reihenfolge = Vorrang
SORTEN = [
    ('Förderheft nach Blocktitel', r'Themenblock ohne Unterkapitel',
     'Förderheft gliedert nur nach Blöcken des Schülerbands; Zuordnung nach dem Blocktitel'),
    ('Kapitel in zwei Bänden', r'in (Band|Kl\.) \d+ \(Kap\.[^)]*\) und (Band|Kl\.) \d+|wortgleich in Band',
     'dasselbe Kapitel steht in zwei Bänden oder Klassen; beide Stellen stehen da'),
    ('Zeile unlesbar oder abgeschnitten', r'verstümmelt|Texterkennung|Seitenbild|abgeschnitten|nicht lesbar',
     'Erkennungsfehler, Seitenbild oder abgeschnittener Titel; Lesart nach dem Bild oder dem Sinn'),
    ('Ersatzverzeichnis', r'Lösungsband|Stoffverteilungsplan|Synopse',
     'die Stelle stammt aus Lösungsband, Stoffverteilungsplan oder Synopse statt aus dem Schulbuchverzeichnis'),
    ('Katalog verortet den Stoff anders', r'im Katalog|Sek-II|nur Vorrat|von koerper|von terme|von binomische-formeln|von einheiten',
     'der Katalog führt den Inhalt als Sek-II-Einheit, Vorrat oder in einem anderen Eintrag'),
    ('Zeile deckt mehrere Einheiten oder Typen',
     r'Einheiten \d+ (und|bis) \d+|Einheit \d+ und \d+|beiden zugeordnet|auch Einheit|auch Typ|auch der Typ|gleichfalls gedeckt|umfasst|wie Einheit \d',
     'eine Verzeichniszeile nennt Stoff mehrerer Einheiten oder Typen; mehrfach zugeordnet'),
    ('Verzeichnis zu grob', r'ohne Unterkapitel|ohne nähere Angabe|ohne Zusatz|Berechnungen allgemein|nicht feiner',
     'die Zeile nennt nur das Thema, keinen Inhalt einer Einheit'),
    ('Frühe Stelle als Grundstufe gelesen', r'Wiederaufnahme|Vorstufe|Einstieg|Einführung|erste Begegnung|folgt (erst )?(Kl\.|S\.)|schon (in )?Kl\.',
     'Stelle in einer früheren Klasse oder vor dem eigentlichen Kapitel als Vorstufe, Einstieg oder Wiederaufnahme gelesen'),
    ('Wortlaut weicht ab', r'.',
     'die Zeile nennt den Inhalt mit anderen Worten; Lesart „… als … gelesen“'),
]


def lies():
    with open(QUELLE, encoding='utf-8') as f:
        return f.read().split('\n')


def baue():
    zeilen = lies()
    zahlenblock = None
    faelle = []
    inline = []           # (eintrag, grund, zitatzeile)
    eintrag, sammel, letzte_stelle, einheit = None, False, None, None
    stellen = []          # (eintrag, zeile)
    for z in zeilen:
        m = re.match(r'^Ermessensfälle gesamt: (\d+)', z)
        if m:
            zahlenblock = int(m.group(1))
        m = re.match(r'^### (\S+) –', z)
        if m:
            eintrag, sammel, letzte_stelle = m.group(1), False, None
            continue
        if eintrag is None:
            continue
        if re.match(r'^- Ermessen \(\d+\):', z):
            sammel = True
            continue
        if sammel:
            m = re.match(r'^  - (.*)$', z)
            if m:
                faelle.append({'eintrag': eintrag, 'roh': m.group(1)})
                continue
            sammel = False
        m = re.match(r'^- (\d+)\. ', z)
        if m:
            einheit, letzte_stelle = int(m.group(1)), None
            continue
        m = re.match(r'^    Ermessen: (.*)$', z)
        if m:
            inline.append((eintrag, einheit, m.group(1).strip(), letzte_stelle))
            continue
        m = re.match(r'^  - (.*„.*“.*)$', z)
        if m and not m.group(1).startswith('Ermessen'):
            letzte_stelle = m.group(1)
            stellen.append((eintrag, m.group(1)))
    for f in faelle:
        roh = f['roh']
        m = re.match(r'^(Einheit(?:en)? [\d, ]+?)(?:, (.+?))?: (.*)$', roh)
        if not m:
            f.update(einheit='–', reihe='–', grund=roh, zitat='–')
            continue
        f['einheit'] = m.group(1).replace('Einheiten ', '').replace('Einheit ', '')
        reihe = m.group(2)
        grund = m.group(3)
        if reihe and 'Förderheft' in reihe and '„' in reihe:
            block = reihe[reihe.rfind('„'):]
            reihe_name = reihe[:reihe.rfind('„')].strip()
            # Förderheftzeile mit dem Blocktitel suchen
            titel = block.strip('„“')
            zitat = next((s for e, s in stellen if e == f['eintrag'] and titel in s and s.startswith('Förderheft')), None)
            f['reihe'] = reihe_name
            f['grund'] = grund
            f['zitat'] = zitat or block
            continue
        f['grund'] = grund
        if reihe:
            f['reihe'] = reihe
        else:
            name = next((r for r in REIHEN if re.match(r'^(Der |Die )?' + re.escape(r) + r'\b', grund)
                         or re.match(r'^(Der |Die )?' + re.escape(r) + r'-', grund)), None)
            f['reihe'] = name or '–'
        # v0.2: bei mehreren Stellen mit demselben Grund die aus der eigenen Reihe und Einheit (vorher: die erste)
        einheiten = {int(x) for x in re.findall(r'\d+', f['einheit'])}
        kandidaten = [(u, s) for e, u, g, s in inline if e == f['eintrag'] and g == grund and s]
        eigene = [s for u, s in kandidaten if reihe and re.match(re.escape(reihe) + r'[,:]', s) and (not einheiten or u in einheiten)]
        treffer = eigene or [s for u, s in kandidaten]
        f['zitat'] = treffer[0] if treffer else '–'
    for f in faelle:
        for name, muster, _ in SORTEN:
            if re.search(muster, f['grund']):
                f['sorte'] = name
                break
    return faelle, zahlenblock


def zitat_kurz(s):
    """Aus einer Belegzeile Reihe/Seite, Zitat und Zeilennummer."""
    if s == '–':
        return '–'
    s = re.sub(r'^Förderheft: ', '', s)
    return s.replace('|', '/')


def schreibe(faelle, zahlenblock):
    gruppen = OrderedDict((n, []) for n, _, _ in SORTEN)
    for f in faelle:
        gruppen[f['sorte']].append(f)
    z = ['# Ermessensfälle der Klassenbelege, nach Sorte gruppiert',
         'Abgeleitet von `werkzeuge/klassen-ermessen.py` aus `katalog/_klassen-belege.md`, nie von Hand ändern.',
         'Zweck: das Urteil über die Ermessensfälle der Klassenbelege im Chat gebündelt fällen. Keine Bewertung: '
         'die Datei ordnet nur, sie entscheidet nicht.',
         '',
         'Lesart: Ein Fall ist ein Punkt der Liste „Ermessen (n)“ am Schluss eines Eintrags. Zitat = die '
         'Verzeichniszeile, an der derselbe Grund im Eintrag steht (bei Förderheft-Blöcken die Förderheftzeile mit '
         'dem Blocktitel; „–“, wenn der Grund die ganze Einheit betrifft). Sorte = die erste zutreffende Regel der '
         'Liste unten, in dieser Reihenfolge; die Muster sind aus dem Wortlaut der Gründe abgeleitet und stehen im '
         'Skript.',
         '',
         f'Gegenprobe: {len(faelle)} Fälle; Zahlenblock von `_klassen-belege.md`: {zahlenblock}'
         + (' – stimmt.' if zahlenblock == len(faelle) else ' – Abweichung (Befund).'),
         '',
         '## Sorten',
         '',
         '| Sorte | Fälle | Kennzeichen im Wortlaut |',
         '|---|---|---|']
    erkl = {n: e for n, _, e in SORTEN}
    for name, liste in sorted(gruppen.items(), key=lambda x: (-len(x[1]), list(gruppen).index(x[0]))):
        z.append(f'| {name} | {len(liste)} | {erkl[name]} |')
    z.append(f'| zusammen | {len(faelle)} | |')
    z.append('')
    for name, liste in sorted(gruppen.items(), key=lambda x: (-len(x[1]), list(gruppen).index(x[0]))):
        if not liste:
            continue
        z.append(f'## {name} ({len(liste)})')
        z.append('')
        z.append('| Eintrag | Einheit | Reihe | Zitat | Grund |')
        z.append('|---|---|---|---|---|')
        for f in liste:
            z.append(f"| {f['eintrag']} | {f['einheit']} | {f['reihe'].replace('|', '/')} | {zitat_kurz(f['zitat'])} "
                     f"| {f['grund'].replace('|', '/')} |")
        z.append('')
    return '\n'.join(z).rstrip('\n') + '\n'


def main():
    faelle, zahlenblock = baue()
    text = schreibe(faelle, zahlenblock)
    if '--probe' in sys.argv:
        alt = open(AUSGABE, encoding='utf-8').read() if os.path.exists(AUSGABE) else ''
        print('unverändert' if alt == text else 'weicht ab')
        return
    with open(AUSGABE, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(f'{os.path.relpath(AUSGABE, REPO)} geschrieben: {len(faelle)} Fälle (Zahlenblock {zahlenblock}).')


if __name__ == '__main__':
    main()
