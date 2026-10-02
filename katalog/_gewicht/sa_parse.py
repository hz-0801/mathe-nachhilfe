#!/usr/bin/env python3
"""Seitenumfang je Unterkapitel aus DNB-Inhaltsverzeichnissen (Kl. 7-10).
Ausgabe sa-roh.csv: reihe;klasse;kapitel;nr;titel;start;seiten;art;plausibel
Seitenumfang = Startseite des naechsten Eintrags (nach Seite sortiert) minus
eigene Startseite. Zweispaltige Verzeichnisse werden ueber Spaltenpositionen
zusammengesetzt; Titel ohne Seitenzahl bleiben mit leerer Seite stehen."""
import re, csv, sys, os

Q = 'mathe-nachhilfe/quellen/'
REIHEN = {  # kuerzel: (datei, format A=Titel..Seite, B=Seite Titel)
    'mathedelta':  ('quelle-buchner-mathedelta-bb-2016-inhalt.txt', 'A'),
    'fundamente17': ('quelle-cornelsen-fundamente-bb-ausgabeb2017-inhalt.txt', 'A'),
    'fundamente24': ('quelle-cornelsen-fundamente-bb-ausgabeb2024-inhalt.txt', 'A'),
    'schnittpunkt': ('quelle-klett-schnittpunkt-mathematik-diff2017-inhalt.txt', 'A'),
    'elemente':    ('quelle-westermann-elemente-der-mathematik-bb-2016u2025-inhalt.txt', 'A'),
    'mathematik23': ('quelle-westermann-mathematik2023-bebbstth-inhalt.txt', 'B'),
    'mheute':      ('quelle-westermann-mathematikheute-bebb-inhalt.txt', 'A'),
    'sekundo':     ('quelle-westermann-sekundo-bb-2017-inhalt.txt', 'A'),
}

ART = [
    ('oeffner', r'^(vorwort|v o r w o rt|dein f ?u ?n ?d|dein fundament|deine grundlagen|das kann ich sch|entdecken|standpunkt|auftakt|lern ?fe|lemfe|bleib|basiswissen|f ?it ?f|vorbereitung zur|einstieg|mathematische zeichen|zum methodischen|über dieses|uber dieses|inhalt)'),
    ('test', r'^(prüfung am ende|prüfe|prufe|prüfedein|das kann ich|bist du fit|rückspiegel|ruckspiegel|tüv|tuv|diagnosetest|ausgangstest|teste dich|test\b|check)'),
    ('zusammenfassung', r'^(zusammenfassung|auf einen b|das wichtigste|was du gelernt|wissen kompakt|merkwissen)'),
    ('vermischt', r'^(\d+(\.\d+)*\s+)?(vermischte|vermochte|komplexe aufgaben|aufgaben zum|basistraining|anwenden\. nachdenken|aufgaben zur|üben|uben|punkte ?sammeln|training|wiederholung|zum üben|kreuz und quer)'),
    ('streifzug', r'^(streifzug|extra|werkzeug|themenseite|im blickpunkt|projekt|vertiefen|lvl|cd |exkurs|lernen lernen|mathematik in|geschichte|tabellenkalkulation|tipps|methode|forschungsauftrag)'),
    ('anhang', r'^(lösungen|losungen|stichwort|register|bildquellen|abkürzungen)'),
]

LEADER = re.compile(r'(?:[\.·•■…_—–\-,:;\'`´^~°“"]\s?){3,}|(?:\s[\._]){3,}')


def art_of(t):
    s = t.lower().strip(' "»*>•-')
    s = re.sub(r'^\d+(\.\d+)*\.?\s+', lambda m: m.group(0) if 'vermischt' in t.lower() else '', s)
    for a, rx in ART:
        if re.search(rx, s):
            return a
    return 'uk'


def clean(t):
    t = re.sub(r'[฀-๿א-׿‏‪-‮�■�]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip(' .·•_—-')
    return t


def sections(lines, reihe):
    """liefert (klasse, [zeilen]) nur fuer Klasse 7-10."""
    cur = None; buf = []
    for l in lines:
        m = re.match(r'^== (.*) ==\s*$', l)
        if m:
            if cur: yield cur, buf
            h = m.group(1); buf = []; cur = None
            km = re.search(r'Klasse (\d+)', h)
            if not km or int(km.group(1)) < 7: continue
            if 'Stoffverteilungsplan' in h: continue
            if reihe == 'elemente' and 'Ausgabe 2016' not in h: continue
            cur = int(km.group(1))
        elif cur:
            buf.append(l)
    if cur: yield cur, buf


def chunks(line):
    line = LEADER.sub('   ', line)
    line = re.sub(r'^(\d{1,2})\.?\s{2,}(?:[I/|]\s+)?(?=[^\d\s])', r'\1 ', line)  # Kapitelnummer und -titel zusammenhalten
    out = []
    for m in re.finditer(r'\S+(?:\s\S+)*', line):
        out.append((m.start(), m.group(0)))
    return out


NUM = re.compile(r'^[»"*>•\'”“]?\s*(\d{1,3})$')
NUMSTART = re.compile(r'^(\d+(\.\d+)+|\d+\.?\s+\D|[A-Z]\d|\d+\s*[IĪ/|]\s)')


def parse_A(lines):
    ents = []      # [col, titel, seite, zeilenidx]
    pend = []      # offene Titel: [col, text, idx]
    for i, l in enumerate(lines):
        for col, ch in chunks(l):
            m = NUM.match(ch)
            tail = re.match(r'^(.*\D)\s(\d{1,3})$', ch)
            if m and pend:
                left = [p for p in pend if p[0] < col]
                p = max(left, key=lambda p: p[0]) if left else pend[-1]
                pend.remove(p)
                ents.append([p[0], p[1], int(m.group(1)), p[2]])
                continue
            if m:
                continue
            text, page = (tail.group(1), int(tail.group(2))) if tail else (ch, None)
            # Fortsetzung eines offenen Titels in derselben Spalte?
            near = [p for p in pend if abs(p[0] - col) <= 12]
            if near and not NUMSTART.match(text) and art_of(text) == 'uk':
                p = near[-1]; pend.remove(p)
                text = p[1] + ' ' + text; col = p[0]
            else:
                for p in near:
                    pend.remove(p); ents.append([p[0], p[1], None, p[2]])
            if page is not None:
                ents.append([col, text, page, i])
            else:
                pend.append([col, text, i])
    for p in pend:
        ents.append([p[0], p[1], None, p[2]])
    return ents


def parse_B(lines):
    """Mathematik 2023: Seite vor Titel, zwei Spalten."""
    ents = []
    last = {}
    for i, l in enumerate(lines):
        l2 = re.sub(r'[»"*>•”“\']', ' ', l)
        found = False
        for m in re.finditer(r'(?:(?<=\s)|^)(\d{1,3})\s{1,6}([A-ZÄÖÜa-zäöü][^\n]*?)(?=\s{2,}\d{1,3}\s{1,6}[A-ZÄÖÜa-zäöü]|\s{3,}\S|$)', l2):
            col = m.start(1); ents.append([col, m.group(2), int(m.group(1)), i])
            last[col // 40] = ents[-1]; found = True
        if not found:
            for col, ch in chunks(l2):
                if re.fullmatch(r'\d{1,2}', ch) or not ch.strip():
                    continue
                k = col // 40
                # eingerueckte Fortsetzung
                cand = [e for e in ents[-6:] if e[3] >= i - 2 and 0 < col - e[0] <= 12]
                if cand:
                    cand[-1][1] += ' ' + ch
                elif col < 10:
                    ents.append([col, ch, None, i])  # Kapitelueberschrift ohne Seite
    return ents


def is_chapter(reihe, col, t, p=None):
    if reihe == 'mathematik23':
        return False
    if reihe in ('mathedelta', 'fundamente17', 'fundamente24', 'elemente'):
        return col <= 3 and re.match(r'^\d{1,2}[\.·•]?\s+[^\d\s.]', t) is not None
    if reihe == 'schnittpunkt':
        return p is None and col <= 3 and re.match(r'^\d{1,2}\s+[A-ZÄÖÜ]', t) is not None
    if reihe in ('mheute', 'sekundo'):
        return re.match(r'^(\d{1,2}|ใ|ไ)\s+[A-ZÄÖÜ]', t) is not None
    return False


def main():
    rows = []
    for reihe, (f, fmt) in REIHEN.items():
        L = open(Q + f, encoding='utf-8').read().splitlines()
        for kl, lines in sections(L, reihe):
            ents = parse_A(lines) if fmt == 'A' else parse_B(lines)
            items = []
            for col, t, p, idx in ents:
                t = clean(t)
                if not t or len(t) < 3 or re.fullmatch(r'[\d\s.]+', t):
                    continue
                kap = is_chapter(reihe, col, t, p)
                if re.match(r'^(INHALT|Inhalt)', t): continue
                if fmt == 'B' and p is None:
                    continue  # Kapitelkopf ohne Seite; Kapitel werden unten ueber 'Ausgangstest' gebildet
                nr = ''
                m = re.match(r'^(\d+(?:[\.•·]\d+)*)\.?\s+(.*)', t)
                if m and not kap:
                    nr, t = m.group(1).replace('•', '.').replace('·', '.'), m.group(2)
                elif m and kap:
                    nr, t = m.group(1), m.group(2)
                t = re.sub(r'^[I/|]\s+', '', t)
                if re.match(r'^(Lösungen|Losungen|Stichwort|Register|Bildquellen|Mathematische Zeichen)', t):
                    a = 'anhang'
                else:
                    a = 'kapitel' if kap else art_of(t)
                items.append(dict(reihe=reihe, klasse=kl, nr=nr, titel=t, start=p, art=a, idx=idx, col=col))
            # Kapitelstart ohne Seite: Seite des naechsten Eintrags gleicher Spalte (Zeilenfolge)
            for j, it in enumerate(items):
                if it['art'] == 'kapitel' and it['start'] is None:
                    nxt = [x for x in items if x['idx'] > it['idx'] and x['start'] is not None and abs(x['col'] - it['col']) < 40]
                    if nxt:
                        it['start'] = min(nxt, key=lambda x: x['idx'])['start']
                        it['kapstart_geerbt'] = True
            if reihe == 'mathematik23':  # Kapitel = Abschnitte bis "Ausgangstest"
                pass
            mx = max([x['start'] for x in items if x['start'] is not None] or [0])
            anh = [x['start'] for x in items if x['start'] is not None and x['start'] > 0.6 * mx and re.match(r'^(Lösungen|Losungen|Grundwissen|Eingangstests|Anhang|Bist du topfit|Basiswissen zum|Stichwort|Register|Formeln und Gesetze|Selbsttest)', x['titel'])]
            if anh:
                for x in items:
                    if x['start'] is not None and x['start'] >= min(anh) and x['art'] != 'kapitel':
                        x['art'] = 'anhang'
            pg = sorted([x for x in items if x['start'] is not None], key=lambda x: (x['start'], x['art'] != 'kapitel', x['idx']))
            # Seitenumfang: naechster Start, Kapitelzeilen zaehlen nicht als Grenze fuer Kapitel selbst
            nonkap = [x for x in pg if x['art'] != 'kapitel']
            for a, b in zip(nonkap, nonkap[1:]):
                a['seiten'] = b['start'] - a['start']
            # Kapitel: Ordnung nach Seite
            kaps = [x for x in pg if x['art'] == 'kapitel']
            if reihe == 'mathematik23':
                kaps = []; first = True; n = 0
                for x in nonkap:
                    if first:
                        n += 1
                        kap = dict(reihe=reihe, klasse=kl, nr=str(n), titel='(Kapitel ab: ' + x['titel'][:40] + ')', start=x['start'], art='kapitel', idx=-1, col=0)
                        kaps.append(kap); first = False
                    if x['art'] == 'test':
                        first = True
                items += kaps
            for a, b in zip(kaps, kaps[1:]):
                a['seiten'] = b['start'] - a['start']
            if kaps and nonkap:
                ende = min([x['start'] for x in nonkap if x['art'] == 'anhang'] or [nonkap[-1]['start']])
                kaps[-1]['seiten'] = (ende - kaps[-1]['start']) if ende >= kaps[-1]['start'] else None
            for x in nonkap:
                ks = [k for k in kaps if k['start'] <= x['start']]
                x['kapitel'] = (ks[-1]['nr'] + ' ' + ks[-1]['titel']) if ks else ''
            for k in kaps:
                k['kapitel'] = k['nr'] + ' ' + k['titel']
            # Kapitelnummer aus Abschnittsnummer, falls vorhanden
            for x in items:
                s = x.get('seiten')
                if x['start'] is None:
                    x['plausibel'] = 'ohne Seite'
                elif s is None:
                    x['plausibel'] = 'letzter Eintrag'
                elif s < 0 or (x['art'] != 'kapitel' and s > 30) or (x['art'] == 'kapitel' and s > 80):
                    x['plausibel'] = 'nein'
                else:
                    x['plausibel'] = 'ja'
                x.setdefault('kapitel', '')
            items.sort(key=lambda x: (x['start'] if x['start'] is not None else 9999, x['art'] != 'kapitel', x['idx']))
            rows += items
    with open('sa-roh.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh, delimiter=';')
        w.writerow(['reihe', 'klasse', 'kapitel', 'nr', 'titel', 'start', 'seiten', 'art', 'plausibel'])
        for x in rows:
            w.writerow([x['reihe'], x['klasse'], x['kapitel'], x['nr'], x['titel'], x['start'] if x['start'] is not None else '', x.get('seiten', '') if x.get('seiten') is not None else '', x['art'], x['plausibel']])
    # Kurzstatistik
    from collections import Counter
    c = Counter(); cp = Counter(); cs = Counter()
    for x in rows:
        if x['art'] in ('uk',):
            c[x['reihe']] += 1
            cp[x['reihe']] += x['plausibel'] == 'ja'
        cs[(x['reihe'], x['plausibel'])] += 1
    for r in REIHEN:
        print(r, 'UK', c[r], 'plausibel', cp[r], {k[1]: v for k, v in cs.items() if k[0] == r})


if __name__ == '__main__':
    main()
