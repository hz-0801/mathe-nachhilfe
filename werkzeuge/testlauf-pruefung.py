#!/usr/bin/env python3
r"""testlauf-pruefung.py – Prüfpunkte, Vergleich und Gegenproben eines Testlaufs (v0.1, 26.09.2026)

Auftrag: archiv/auftrag-testlauf-2026-09-26.md, Teil 3 Schritte 2–4 (Prompt v4.4). Hängt an
blaetter/testlauf-<datum>/kennzahlen.md (nach testlauf-messen.py) drei Abschnitte an:
  1. Tabelle v44-pruefung, je Eingabe eine Zeile, je Punkt a)–h) eine Spalte,
  2. Vergleichstabelle des Vorlaufs gegen diesen Lauf,
  3. die Gegenproben des Auftrags mit Belegquelle.

  python werkzeuge/testlauf-pruefung.py blaetter/testlauf-<datum> --vorlauf blaetter/testlauf-<alt>
         --bericht-alt bericht-testlauf-<alt>.md [--probe]

--probe gibt die Abschnitte aus und schreibt nichts. Das Skript schreibt nur an das Ende von
kennzahlen.md dieses Laufs; ein zweiter Aufruf ersetzt, was ein erster angehängt hat (ab der
Überschrift „# Prüfpunkte v4.4“).

Lesarten (je Eingabe das Gesamt- bzw. Fokus-PDF nach blatt-pruef.py, Quelltext = dessen
Rahmendatei mit allen \input, ohne Kommentare):
 a) Zahl `\rechenplatz` (auch `\rechenplatz[halb]`); Zahl `\begin{beispiel}`.
 b) Seite „Inhalt“: eine Zeile, die nur „Inhalt“ lautet, im PDF-Text, oder ein Kopf „Inhalt“ im
    Quelltext. `\verzeichniszeile` im Quelltext von Gesamt und Lernblatt (Fokus: der Fokus).
 c) Nummern aus der Textextraktion (Hauptnummern wie in testlauf-messen.py, ohne Abhakseite):
    „ja“, wenn die Nummern 1, 2, … ohne Neubeginn bis zur letzten laufen und keine „Z<n>“-Nummer
    vorkommt; die Zone ist der Bereich „Kennst du schon (Nr. a–b)“ der Verzeichniszeile oder
    beim Fokus die Nummern vor dem Zweigkopf. „Z1“: jedes „Z1“ als eigenes Wort im PDF-Text.
 d) Zahl `\verfahren`; Zahl `\anweisung`.
 e) In den Rahmen- und Einheitsdateien (die .tex der übergebenen PDFs, zone_*, e<n>_*, abhaken,
    fokus*): `\newcommand`, `\def`, `\newenvironment`, deren Name in ../blattbau/
    Anleitung_mathblatt.md als Makro (`\name`) oder Umgebung (`\begin{name}`) vorkommt. Eigene
    Definitionen mit anderem Namen stehen darunter als Auskunft.
 f) chat.txt: die erste Zeile, die mit „→“, „Lernblatt ·“ oder „Fokus “ beginnt, beginnt mit „→“.
 g) zeiten.txt: jedes Stempelwort genau einmal, kein „e<n>“ ohne Leerzeichen.
 h) PDF-Text (Zeilenumbrüche zu Leerzeichen): Klammern „(P10 JJJJ …)“, davon mit FOR, EBR, OS
    oder GYM als erstem Wort nach dem Jahr.
Vergleich: links Seiten, Hauptnummern, Teilaufgaben aus der Vergleichstabelle von
<vorlauf>/kennzahlen.md, Werkzeugaufrufe laut protokoll.txt, Aufrufe (Umgebung) und Zeit aus der
Tabelle des alten Berichts; rechts dieselben Größen dieses Laufs (kennzahlen.md, protokoll.txt
nach testlauf-ablage.py, aufrufe.txt nach testlauf-verlauf.py, zeiten.txt: letzter Stempel − t0).
Misst blatt-pruef.py den Vorlauf heute anders als dessen kennzahlen.md, steht das darunter.
"""

import collections
import csv
import importlib.util
import re
import sys
from pathlib import Path

WERKZEUGE = Path(__file__).resolve().parent
WURZEL = WERKZEUGE.parent
ANLEITUNG = WURZEL.parent / 'blattbau' / 'Anleitung_mathblatt.md'
MARKE = '# Prüfpunkte v4.4'


def lade(name, datei):
    spec = importlib.util.spec_from_file_location(name, WERKZEUGE / datei)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


BP = lade('blatt_pruef', 'blatt-pruef.py')
TM = lade('testlauf_messen', 'testlauf-messen.py')
TA = lade('testlauf_ablage', 'testlauf-ablage.py')

DEUTUNG = re.compile(r'^\s*(→|Lernblatt ·|Fokus )')
PAPIERE = ('FOR', 'EBR', 'OS', 'GYM')


def csv_zeilen():
    with open(WERKZEUGE / 'testlauf-eingaben.csv', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))


def anleitung_namen():
    t = ANLEITUNG.read_text(encoding='utf-8')
    return set(re.findall(r'\\([A-Za-z]+)', t)) | set(re.findall(r'\\begin\{([A-Za-z]+)\}', t))


def zaehle(tex, name):
    return len(re.findall(r'\\' + name + r'(?![A-Za-z])', tex))


def rahmendateien(o):
    pdfs = {p.stem for p in o.glob('*.pdf') if re.search(r'_(KennstDuSchon|Lernblatt|Gesamt|Loesungen|Fokus)', p.name)}
    for p in sorted(o.glob('*.tex')):
        s = p.stem
        if s in pdfs or re.match(r'(zone|e\d+)_[al]$', s) or s == 'abhaken' or s.lower().startswith('fokus'):
            yield p


def definitionen(o, namen):
    treffer, eigene = [], []
    for p in rahmendateien(o):
        t = BP.ohne_kommentar(p.read_text(encoding='utf-8', errors='replace'))
        for art, name in re.findall(r'\\(newcommand|renewcommand|providecommand)\*?\s*\{?\\([A-Za-z]+)', t) \
                + re.findall(r'\\(def)\s*\\([A-Za-z]+)', t) \
                + re.findall(r'\\(newenvironment)\s*\{([A-Za-z]+)\}', t):
            eintrag = f'{p.name}: \\{art} {name}'
            if art in ('newcommand', 'def', 'newenvironment') and name in namen:
                treffer.append(eintrag)
            else:
                eigene.append(eintrag)
    return treffer, eigene


def zeilen_von(pfad):
    return pfad.read_text(encoding='utf-8', errors='replace').replace('\r', '').split('\n') if pfad.exists() else []


def deutungszeile(o):
    return next((z.strip() for z in zeilen_von(o / 'chat.txt') if DEUTUNG.match(z)), None)


def stempel(o):
    worte = []
    for z in zeilen_von(o / 'zeiten.txt'):
        m = re.match(r'^\s*(.*?)\s+(\d{9,})\s*$', z)
        if m:
            worte.append((m.group(1), int(m.group(2))))
    return worte


def zeit_min(o):
    s = stempel(o)
    t0 = next((t for w, t in s if w == 't0'), None)
    if t0 is None or len(s) < 2:
        return None
    return (max(t for _, t in s) - t0) / 60


def komma(x, stellen=1):
    return f'{x:.{stellen}f}'.replace('.', ',')


def umgebung(o):
    for z in zeilen_von(o / 'aufrufe.txt'):
        m = re.match(r'Werkzeugaufrufe \(Umgebung\):\s*(\d+)', z)
        if m:
            return int(m.group(1))
    return None


def pruefe_blatt(pdf, o, t, namen):
    tex = BP.lies_tex(t['tex']) if t['tex'] else ''
    seiten = BP.pdf_text(pdf)
    text = '\n'.join(seiten)
    fokus = 'fokus' in pdf.name.lower()
    r = {}
    # a
    r['rechenplatz'] = zaehle(tex, 'rechenplatz')
    r['beispiel'] = len(re.findall(r'\\begin\{beispiel\}', tex))
    # b
    inhalt = bool(re.search(r'(?m)^\s*Inhalt\s*$', text)) or bool(re.search(r'\{Inhalt\}', tex))
    r['inhalt'] = 'ja' if inhalt else 'nein'
    verz = []
    if fokus:
        verz.append(f"Fokus {'ja' if zaehle(tex, 'verzeichniszeile') else 'nein'}")
    else:
        verz.append(f"Gesamt {'ja' if zaehle(tex, 'verzeichniszeile') else 'nein'}")
        lb = next((p for p in o.glob('*_Lernblatt.pdf')), None)
        lbt = BP.testlauf_tex(lb, o) if lb else None
        verz.append(f"Lernblatt {('ja' if zaehle(BP.lies_tex(lbt), 'verzeichniszeile') else 'nein') if lbt else '– (keine Datei)'}")
    r['verz'] = ' · '.join(verz)
    # c
    abhak, koepfe, zweig, hns = TM.zerlege_text(seiten)
    z_nummern = [h['nr'] for h in hns if h['nr'].startswith('Z')]
    nummern = [int(h['nr']) for h in hns if not h['nr'].startswith('Z')]
    neubeginn = sum(1 for i, n in enumerate(nummern) if i and n == 1)
    zone = re.search(r'Kennst du schon \(Nr\.\s*(\d+)\s*[–-]\s*(\d+)\)', ' '.join(text.split()))
    if fokus and koepfe:
        erste = min(k['seite'] for k in koepfe)
        vor = [int(h['nr']) for h in hns if not h['nr'].startswith('Z') and h['seite'] < erste]
        zone_txt = f'Zone {vor[0]}–{vor[-1]}' if vor else 'keine Zone'
    elif zone:
        zone_txt = f'Zone {zone.group(1)}–{zone.group(2)}'
    else:
        zone_txt = 'keine Zone'
    lueckenlos = nummern == list(range(1, len(nummern) + 1)) and not z_nummern
    r['nummern'] = (f"{'ja' if lueckenlos else 'nein'} ({zone_txt}, "
                    f"{'1–' + str(nummern[-1]) if nummern else 'keine'} im Text"
                    + (f", {neubeginn}× Neubeginn bei 1" if neubeginn else '')
                    + (f", Z-Nummern {len(z_nummern)}" if z_nummern else '') + ')')
    r['z1'] = 'ja' if re.search(r'(?<![A-Za-z0-9])Z1(?![0-9])', text) else 'nein'
    # d
    r['verfahren'] = zaehle(tex, 'verfahren')
    r['anweisung'] = zaehle(tex, 'anweisung')
    # e
    treffer, eigene = definitionen(o, namen)
    r['nachbau'] = f"{len(treffer)}" + (f" ({'; '.join(treffer)})" if treffer else '')
    r['eigene'] = eigene
    # f
    d = deutungszeile(o)
    r['pfeil'] = ('ja' if d.startswith('→') else 'nein') if d else '– (keine Deutungszeile in chat.txt)'
    r['deutung'] = d
    # g
    s = stempel(o)
    zaehlung = collections.Counter(w for w, _ in s)
    doppelt = [w for w, n in zaehlung.items() if n > 1]
    ohne = [w for w in zaehlung if re.fullmatch(r'e\d+', w)]
    fehler = ([f"doppelt: {', '.join(doppelt)}"] if doppelt else []) + ([f"ohne Leerzeichen: {', '.join(ohne)}"] if ohne else [])
    r['zeiten'] = ('ja' if s and not fehler else 'nein') + (f" ({'; '.join(fehler)})" if fehler else '') \
        + ('' if s else ' (zeiten.txt fehlt oder leer)')
    # h
    flach = ' '.join(text.split())
    marken = re.findall(r'\(P10\s+(\d{4})([^)]*)\)', flach)
    mit = [m for m in marken if m[1].strip().split(' ')[0] in PAPIERE]
    r['marken'] = f'{len(marken)} / {len(mit)}'
    r['markenliste'] = [f"(P10 {j}{rest})" for j, rest in marken]
    return r, koepfe, hns, seiten


def tabelle_alt(vorlauf, bericht):
    """{kurzname: {...}} aus der alten kennzahlen.md und dem alten Bericht."""
    alt, drin = {}, False
    for z in zeilen_von(vorlauf / 'kennzahlen.md'):
        if z.startswith('## '):
            drin = z.strip() == '## Vergleichstabelle'
        if drin and re.match(r'\| \d+-', z):
            f = [x.strip() for x in z.strip('|').split('|')]
            alt.setdefault(f[0], {}).update({'datei': f[3], 'seiten': f[4], 'hn': f[5], 'ta': f[6]})
    for z in zeilen_von(bericht):
        m = re.match(r'^\| (\d+) \| ([a-z0-9-]+) \| (\d+) \| (\w+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', z)
        if m:
            k = f'{m.group(1)}-{m.group(2)}'
            alt.setdefault(k, {}).update({'prot': m.group(5).strip(), 'umg': m.group(6).strip(),
                                          'zeit': m.group(8).strip()})
    return alt


def vergleich(ordner, vorlauf, bericht):
    alt = tabelle_alt(vorlauf, bericht)
    neu = tabelle_alt(ordner, Path('/nicht-vorhanden'))
    z = ['## Vergleich v4.3 gegen v4.4', '',
         f'Links {vorlauf.name} (v4.3): Seiten, Hauptnummern, Teilaufgaben aus `{vorlauf.name}/kennzahlen.md`, '
         f'Werkzeugaufrufe, Aufrufe (Umgebung) und Zeit aus `{bericht.name}`. Rechts {ordner.name} (v4.4): '
         'kennzahlen.md oben, protokoll.txt, aufrufe.txt, zeiten.txt (letzter Stempel − t0). Der Lauf vom 25.09. '
         'lief mit zehn Sitzungen gleichzeitig, dieser nacheinander.', '',
         '| Eingabe | Seiten v4.3 | Seiten v4.4 | Hauptnummern v4.3 | Hauptnummern v4.4 | Teilaufgaben v4.3 | '
         'Teilaufgaben v4.4 | Aufrufe protokoll.txt v4.3 | Aufrufe protokoll.txt v4.4 | Aufrufe (Umgebung) v4.3 | '
         'Aufrufe (Umgebung) v4.4 | Zeit v4.3 | Zeit v4.4 |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for zeile in csv_zeilen():
        k = f"{zeile['nr']}-{zeile['kurzname']}"
        o = ordner / k
        a, n = alt.get(k, {}), neu.get(k, {})
        prot = TA.werkzeugaufrufe(o / 'protokoll.txt') if o.is_dir() else None
        umg = umgebung(o) if o.is_dir() else None
        zm = zeit_min(o) if o.is_dir() else None
        z.append(f"| {k} | {a.get('seiten', '–')} | {n.get('seiten', '–')} | {a.get('hn', '–')} | {n.get('hn', '–')} | "
                 f"{a.get('ta', '–')} | {n.get('ta', '–')} | {re.sub(r' .*', '', a.get('prot', '–'))} | "
                 f"{prot if prot is not None else '–'} | {a.get('umg', '–')} | {umg if umg is not None else '–'} | "
                 f"{a.get('zeit', '–')} | {komma(zm) + ' min' if zm is not None else '–'} |")
    # Vorlauf heute gemessen
    stand, reg = BP.register()
    heute = {}
    for pdf, o, t in BP.testlauf_blaetter(vorlauf):
        s = BP.zusammen(BP.messe(pdf, o, reg, t))
        if s:
            heute[o.name] = s
    abw = [f"{k} Teilaufgaben {heute[k]['ta']} statt {v['ta']}" for k, v in alt.items()
           if k in heute and 'ta' in v and heute[k]['ta'] != v['ta']]
    abw += [f"{k} Hauptnummern {heute[k]['hn']} statt {v['hn']}" for k, v in alt.items()
            if k in heute and 'hn' in v and heute[k]['hn'] != v['hn']]
    z += ['', 'blatt-pruef.py in der heutigen Fassung misst den Vorlauf '
          + (('abweichend von seiner kennzahlen.md: ' + '; '.join(abw) + '.') if abw else 'wie seine kennzahlen.md.'), '']
    return z


def eintrag_einheiten(o):
    namen = BP.testlauf_protokoll(o)['namen']
    if not namen:
        return None, []
    pfad = WURZEL / 'katalog' / f'{namen[0]}.md'
    return namen[0], BP.lerneinheiten(pfad.read_text(encoding='utf-8')) if pfad.exists() else []


def gegenproben(ordner, blaetter):
    z = ['## Gegenproben (Auftrag 2026-09-26, Teil 3 Schritt 4)', '']
    mess = {(o, pdf): TM.messe(pdf) for pdf, o, _ in blaetter}
    alte = TM.gegenproben(ordner, mess)[2:]      # 1: Eingabe 1/2, 2: Eingabe 8, 3: Eingabe 4
    z.append('Belegquellen: Eingabe 1/2 katalog/quadratische-gleichungen.md, Marken Einheit 2 (OS Kl. 10, GYM '
             'Kl. 8–9); Eingabe 5 werkzeuge/testlauf-eingaben.csv nach Teil 0; Eingabe 9 unterrichtsblatt.md v4.4, '
             '1.5; Eingabe 7 unterrichtsblatt.md v4.4, 2.5. Gemessen am Gesamt- bzw. Fokus-PDF (Textextraktion) '
             'und an chat.txt.')
    z.append('')
    z += alte

    def blatt(prefix):
        return next(((pdf, o, m) for (o, pdf), m in mess.items() if o.name.startswith(prefix)), (None, None, None))

    # Eingabe 5
    pdf, o, m = blatt('5-')
    z.append('4. Eingabe 5 – Deutungszeile nennt „mit Ausblick“ ohne Zweig.')
    z.append('')
    if o:
        d = deutungszeile(o) or '– keine –'
        ausblick = [k for k in m['koepfe'] if k['ausblick']]
        z.append(f"   - Deutungszeile (chat.txt): „{TM.zeile_md(d)}“; nennt „mit Ausblick“: "
                 f"{'ja' if 'mit ausblick' in d.lower() else 'nein'}.")
        z.append(f"   - Ausblick-Zweige im PDF: {len(ausblick)}"
                 + (' (' + '; '.join(f"Einheit {k['nr']} · {TM.zeile_md(k['titel'])}" for k in ausblick) + ')' if ausblick else '')
                 + '.')
    else:
        z.append('   - nicht messbar: Eingabe 5 ohne Gesamt-PDF.')
    z.append('')
    # Eingabe 9
    pdf, o, m = blatt('9-')
    z.append('5. Eingabe 9 – kein Zweig liegt in der Zone; die Zweige tragen eine Zeitmarke mit „Q1“.')
    z.append('')
    if o:
        name, einheiten = eintrag_einheiten(o)
        erste = min((k['seite'] for k in m['koepfe']), default=None)
        zone = [h for h in m['hns'] if erste is None or h['seite'] < erste]
        z.append(f"   - Zweige im PDF: {len(m['koepfe'])}; Lerneinheiten im Eintrag {name}: {len(einheiten)}.")
        for k in m['koepfe']:
            zm = TM.zeitmarke(k)
            z.append(f"   - {'Ausblick ' if k['ausblick'] else ''}Einheit {k['nr']}{TM.von(k)} · {TM.zeile_md(k['titel'])}: "
                     f"Zeitmarke „{TM.zeile_md(zm[0])}“ – „Q1“: {'ja' if 'Q1' in zm[0] else 'nein'}.")
        z.append(f"   - Zone: {len(zone)} Hauptnummern vor dem ersten Zweig: "
                 + '; '.join(f"Nr. {h['nr']} „{TM.zeile_md(h['titel'])}“" for h in zone) + '.')
        z.append(f"   - Deutungszeile (chat.txt): „{TM.zeile_md(deutungszeile(o) or '– keine –')}“.")
    else:
        z.append('   - nicht messbar: Eingabe 9 ohne Gesamt-PDF.')
    z.append('')
    # Eingabe 7
    pdf, o, m = blatt('7-')
    z.append('6. Eingabe 7 – Zweigkopf ohne „von“.')
    z.append('')
    if pdf:
        zeilen = [(i + 1, zl.strip()) for i, s in enumerate(BP.pdf_text(pdf)) for zl in s.split('\n')
                  if re.match(r'^\s*(Ausblick\s+)?Einheit\s+\d+', zl)]
        for seite, zl in zeilen[:3]:
            z.append(f"   - S. {seite}: „{TM.zeile_md(zl)}“ – „von“: {'ja' if re.search(r'Einheit\s+\d+\s+von\s+\d', zl) else 'nein'}.")
        if not zeilen:
            z.append('   - keine Zeile „Einheit n …“ im Fokus-PDF.')
    else:
        z.append('   - nicht messbar: Eingabe 7 ohne Fokus-PDF.')
    z.append('')
    return z


def v44(ordner, blaetter):
    namen = anleitung_namen()
    z = [MARKE, '', 'Erzeugt von `werkzeuge/testlauf-pruefung.py` (Lesarten im Skriptkopf). Quelltext = Rahmendatei '
         'des Gesamt- bzw. Fokus-PDFs mit allen `\\input`.', '',
         '## v44-pruefung', '',
         '| Eingabe | Datei | a) \\rechenplatz | a) beispiel (Soll 0) | b) Seite „Inhalt“ (Soll nein) | '
         'b) \\verzeichniszeile (Soll ja) | c) Nummern durchlaufend (Soll ja) | c) „Z1“ (Soll nein) | d) \\verfahren | '
         'd) \\anweisung | e) Nachbau (Soll 0) | f) „→“ (Soll ja) | g) zeiten.txt (Soll ja) | h) P10-Marken / mit Papier |',
         '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    details = []
    ergebnisse = {}
    for pdf, o, t in blaetter:
        r, _, _, _ = pruefe_blatt(pdf, o, t, namen)
        ergebnisse[o.name] = r
        z.append(f"| {o.name} | {pdf.name} | {r['rechenplatz']} | {r['beispiel']} | {r['inhalt']} | {r['verz']} | "
                 f"{TM.zeile_md(r['nummern'])} | {r['z1']} | {r['verfahren']} | {r['anweisung']} | "
                 f"{TM.zeile_md(r['nachbau'])} | {r['pfeil']} | {TM.zeile_md(r['zeiten'])} | {r['marken']} |")
        details.append(f"- {o.name}: Deutungszeile „{TM.zeile_md(r['deutung'] or '–')}“; eigene Definitionen: "
                       f"{'; '.join(r['eigene']) or 'keine'}; P10-Marken: {', '.join(r['markenliste']) or 'keine'}.")
    fehlend = [f"{zl['nr']}-{zl['kurzname']}" for zl in csv_zeilen()
               if f"{zl['nr']}-{zl['kurzname']}" not in ergebnisse]
    if fehlend:
        z.append('')
        z.append('Ohne Gesamt- oder Fokus-PDF (nicht gemessen): ' + ', '.join(fehlend) + '.')
    z += ['', '### Je Blatt: Deutungszeile, eigene Definitionen, Prüfungsmarken', ''] + details + ['']
    return z, ergebnisse


def main():
    args = sys.argv[1:]
    probe = '--probe' in args
    args = [a for a in args if a != '--probe']

    def opt(name):
        i = args.index(name)
        wert = args[i + 1]
        del args[i:i + 2]
        return Path(wert).resolve()
    vorlauf, bericht = opt('--vorlauf'), opt('--bericht-alt')
    if len(args) != 1:
        sys.exit(__doc__)
    ordner = Path(args[0]).resolve()
    blaetter = BP.testlauf_blaetter(ordner)
    teil, _ = v44(ordner, blaetter)
    teil += vergleich(ordner, vorlauf, bericht)
    teil += gegenproben(ordner, blaetter)
    text = '\n'.join(teil).rstrip('\n') + '\n'
    if probe:
        print(text)
        return
    ziel = ordner / 'kennzahlen.md'
    alt = ziel.read_text(encoding='utf-8')
    if MARKE in alt:
        alt = alt[:alt.index(MARKE)]
    with open(ziel, 'w', encoding='utf-8', newline='\n') as f:
        f.write(alt.rstrip('\n') + '\n\n' + text)
    print(f'{ziel}: Prüfpunkte, Vergleich und Gegenproben angehängt.')


if __name__ == '__main__':
    main()
