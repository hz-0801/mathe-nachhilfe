#!/usr/bin/env python3
r"""testlauf-lesezettel.py – Lesezettel eines Testlaufs des Unterrichtsblatt-Prompts (v0.2, 26.09.2026)

v0.2: unter „Worauf beim Gegenlesen achten“ zusätzlich die Prüfpunkte a)–h) aus
werkzeuge/testlauf-pruefung.py, die ihr Soll verfehlen („v4.4-Prüfpunkt:“), sonst eine Zeile, dass
alle Soll erfüllt sind (Auftrag Testlauf 2026-09-26, Teil 4 Schritt 1); ein Komma vor „weil“
trennt in der Spalte „prüft“ kein Stück ab.

Auftrag: archiv/auftrag-testlauf-<datum>.md, Teil 4 Schritt 1. Schreibt
blaetter/testlauf-<datum>/lesezettel.md: je Eingabe der CSV werkzeuge/testlauf-eingaben.csv
ein Abschnitt. Der Lesezettel zeigt, er bewertet nicht.

  python werkzeuge/testlauf-lesezettel.py blaetter/testlauf-<datum> [--probe]

Je Abschnitt:
  Eingabe        Spalte „eingabe“ der CSV, dahinter die Zeile, wie die Sitzung sie bekam.
  Deutungszeile und Plan
                 wortgleich aus chat.txt: von der ersten Zeile, die mit „→“, „Lernblatt ·“ oder
                 „Fokus “ beginnt, bis vor die erste Zeile, die einen anderen Teil des Chats
                 eröffnet (Planfrage, Antwort, Zone, Rückfragen, Dateien, Ausgabeblock).
  Ausgabeblock   wortgleich aus chat.txt: nach der Überschrift „Ausgabeblock:“ (samt dem, was auf
                 derselben Zeile dahinter steht; fehlt sie: ab der ersten Zeile „1. “, fehlt auch die:
                 ab der Zeile nach der letzten Zeile, die nur ein Dateiname .pdf/.zip ist, seit v0.2) bis vor
                 „Übergebene Dateien“/„Dateien:“ oder zum Ende.
  PDFs           die Übergabedateien nach dem Namensschema des Prompts (4.5) mit Pfad relativ
                 zum Lesezettel; die Zwischenkompilate der Sitzung in einer Zeile dahinter.
  Worauf beim Gegenlesen achten
                 die Stücke der Spalte „prüft“ (getrennt an „, “ und „; “ außerhalb von
                 Klammern und Anführungszeichen), zu höchstens fünf Zeilen gebündelt; darunter,
                 mit „Messung:“ markiert, was die Kennzahlen dieses Blatts zeigen: Einheitenköpfe
                 ohne Zweigzeile, Titel ohne Ich-Form, „Blatt 0“ im PDF, Typen ohne vollen
                 Treffer in den gebauten Einheiten (blatt-pruef.py, Kennzahl 9; „kein Treffer“
                 mit Namen), Werkzeugaufrufe über 60 laut protokoll.txt.
"""

import csv
import importlib.util
import re
import sys
from pathlib import Path

WERKZEUGE = Path(__file__).resolve().parent
WURZEL = WERKZEUGE.parent


def lade(name, datei):
    spec = importlib.util.spec_from_file_location(name, WERKZEUGE / datei)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


BP = lade('blatt_pruef', 'blatt-pruef.py')
TM = lade('testlauf_messen', 'testlauf-messen.py')
TA = lade('testlauf_ablage', 'testlauf-ablage.py')
TP = lade('testlauf_pruefung', 'testlauf-pruefung.py')
NAMEN = TP.anleitung_namen()


def soll_verfehlt(r, fokus):
    """Prüfpunkte a)–h) (testlauf-pruefung.py), die ihr Soll verfehlen."""
    z = []
    if r['beispiel']:
        z.append(f"a) Umgebung beispiel {r['beispiel']}-mal (Soll 0)")
    if r['inhalt'] != 'nein':
        z.append('b) Seite „Inhalt“ vorhanden (Soll nein)')
    if not fokus and 'nein' in r['verz']:
        z.append(f"b) \\verzeichniszeile: {r['verz']} (Soll ja)")
    if not r['nummern'].startswith('ja'):
        z.append(f"c) Nummern: {r['nummern']} (Soll ja)")
    if r['z1'] != 'nein':
        z.append('c) „Z1“ kommt vor (Soll nein)')
    if not r['nachbau'].startswith('0'):
        z.append(f"e) Bausteine der Vorlage nachgebaut: {r['nachbau']} (Soll 0)")
    if r['pfeil'] != 'ja':
        z.append(f"f) Deutungszeile ohne „→“: {r['pfeil']} (Soll ja)")
    if not r['zeiten'].startswith('ja'):
        z.append(f"g) zeiten.txt: {r['zeiten']} (Soll ja)")
    return z

DEUTUNG = re.compile(r'^\s*(→|Lernblatt ·|Fokus )')
STOPP = re.compile(r'^\s*(Planfrage|Alle Zweige, oder welche|Schüler ist|Gemeint ist|Antwort|Zweite Antwort|'
                   r'Nach der Zone|Zone:|Rückfragen|Übergebene Dateien|Dateien:|Ausgabeblock|Es gab keine Planfrage|'
                   r'\[Datei\]|[A-Za-z]+_KennstDuSchon\.pdf)')
AUSGABE_ENDE = re.compile(r'^\s*(Übergebene Dateien|Dateien:)')


def schneide(zeilen, anfang, ende):
    teil = zeilen[anfang:ende]
    while teil and not teil[-1].strip():
        teil.pop()
    while teil and not teil[0].strip():
        teil.pop(0)
    return teil


def deutung_und_plan(zeilen):
    i = next((k for k, z in enumerate(zeilen) if DEUTUNG.match(z)), None)
    if i is None:
        return None
    j = next((k for k in range(i + 1, len(zeilen)) if STOPP.match(zeilen[k])), len(zeilen))
    return schneide(zeilen, i, j)


def ausgabeblock(zeilen):
    kopf = next((k for k, z in enumerate(zeilen) if z.strip().startswith('Ausgabeblock')), None)
    erste = []
    if kopf is not None:
        i = kopf + 1
        rest = zeilen[kopf].split(':', 1)[1] if ':' in zeilen[kopf] else ''
        if rest.strip():   # Überschrift und erste Zeile auf einer Zeile („Ausgabeblock:1. …“)
            erste = [rest]
    else:
        i = next((k for k, z in enumerate(zeilen) if re.match(r'^1\. ', z)), None)
    if i is None:
        # v0.2: ohne Überschrift und Nummern der Block unter der letzten reinen Dateizeile (v4.4)
        dateien = [k for k, z in enumerate(zeilen) if re.match(r'^\s*\S+\.(pdf|zip)\s*$', z)]
        i = dateien[-1] + 1 if dateien else None
    if i is None:
        return None
    j = next((k for k in range(i, len(zeilen)) if AUSGABE_ENDE.match(zeilen[k])), len(zeilen))
    return schneide(erste + zeilen[i:j], 0, len(erste) + j - i)


def stuecke(text):
    teile, akt, tiefe, zitat = [], '', 0, False
    k = 0
    while k < len(text):
        c = text[k]
        if c in '(':
            tiefe += 1
        elif c in ')':
            tiefe -= 1
        elif c == '„':
            zitat = True
        elif c in '“"' and zitat:
            zitat = False
        if not tiefe and not zitat and text[k:k + 2] in (', ', '; ') and not text[k + 2:].startswith('weil '):
            teile.append(akt.strip())
            akt = ''
            k += 2
            continue
        akt += c
        k += 1
    if akt.strip():
        teile.append(akt.strip())
    return teile


def buendle(teile, hoechstens=5):
    if len(teile) <= hoechstens:
        return teile
    zeilen = [[] for _ in range(hoechstens)]
    for n, t in enumerate(teile):
        zeilen[n * hoechstens // len(teile)].append(t)
    return [', '.join(z) for z in zeilen]


def codeblock(zeilen):
    return ['```text'] + zeilen + ['```'] if zeilen else ['(in chat.txt nicht gefunden)']


def abschnitt(ordner, zeile):
    o = ordner / f"{zeile['nr']}-{zeile['kurzname']}"
    z = [f"## {zeile['nr']} {zeile['kurzname']}", '']
    if not o.is_dir():
        return z + ['Ordner fehlt – die Eingabe ist offen (stand.md).', '']
    z.append(f"Eingabe: „{zeile['eingabe']}“ – an die Sitzung: „{zeile['eingabe']} – Antworten auf Planfrage "
             f"und Zone: {zeile['antworten']}; baue ohne Halt bis zum Ausgabeblock durch“")
    z.append('')
    chat = o / 'chat.txt'
    zeilen = chat.read_text(encoding='utf-8', errors='replace').replace('\r', '').split('\n') if chat.exists() else []
    z.append('Deutungszeile und Plan (chat.txt, wortgleich):')
    z.append('')
    z += codeblock(deutung_und_plan(zeilen) if zeilen else None)
    z.append('')
    z.append('Ausgabeblock (chat.txt, wortgleich):')
    z.append('')
    z += codeblock(ausgabeblock(zeilen) if zeilen else None)
    z.append('')
    pdfs = sorted(o.glob('*.pdf'), key=lambda p: p.name.lower())
    schema = [p for p in pdfs if re.search(r'_(KennstDuSchon|Lernblatt|Gesamt|Loesungen|Fokus|E\d)', p.name)]
    rest = [p for p in pdfs if p not in schema]
    z.append('PDFs:')
    z.append('')
    for p in schema:
        z.append(f'- [{p.name}]({o.name}/{p.name})')
    if rest:
        z.append(f"- Zwischenkompilate der Sitzung: {', '.join(p.name for p in rest)}")
    z.append('')
    z.append('Worauf beim Gegenlesen achten:')
    z.append('')
    for t in buendle(stuecke(zeile['prueft'])):
        z.append(f'- {t}')
    # Messung
    tripel = [t for t in BP.testlauf_blaetter(ordner) if t[1] == o]
    for pdf, oo, tl in tripel:
        m = TM.messe(pdf)
        ohne_zweig = [k for k in m['koepfe'] if not k['zweig']]
        if ohne_zweig:
            z.append(f"- Messung: {pdf.name} – Einheitenkopf ohne Zweigzeile: "
                     + '; '.join(f"Einheit {k['nr']} · {k['titel']}" for k in ohne_zweig))
        ohne_ich = [h for h in m['hns'] if not h['titel'].startswith(TM.ICH)]
        if ohne_ich:
            z.append(f"- Messung: {pdf.name} – Titel ohne Ich-Form: "
                     + '; '.join(f"Nr. {h['nr']} „{h['titel']}“" for h in ohne_ich))
        if m['blatt0']:
            z.append(f"- Messung: {pdf.name} – „Blatt 0“ kommt {m['blatt0']}-mal im PDF vor.")
        k = BP.messe(pdf, oo, None, tl)
        if not k.get('fehlt_tex') and k.get('typen'):
            s = BP.zusammen(k)
            kein = [t for t in k['typen'] if (t[2] or not any(k['gebaut'].values()))
                    and t[4] == 'kein Treffer' and not t[7]]
            zeile_t = f"- Messung: {pdf.name} – Typen ohne vollen Treffer (blatt-pruef.py, Kennzahl 9): {s['ohne']}"
            if kein:
                zeile_t += '; ohne jeden Treffer: ' + '; '.join(f"E{t[1]} {t[3]}" for t in kein)
            z.append(zeile_t + '.')
        r, _, _, _ = TP.pruefe_blatt(pdf, oo, tl, NAMEN)
        verfehlt = soll_verfehlt(r, 'fokus' in pdf.name.lower())
        for v in verfehlt:
            z.append(f'- v4.4-Prüfpunkt: {pdf.name} – {v}.')
        if not verfehlt:
            z.append(f'- v4.4-Prüfpunkte: {pdf.name} – a)–g) erfüllen ihr Soll.')
    aufrufe = TA.werkzeugaufrufe(o / 'protokoll.txt')
    if aufrufe and aufrufe > 60:
        z.append(f'- Messung: {aufrufe} Werkzeugaufrufe laut protokoll.txt (Zählgrenze 60).')
    z.append('')
    return z


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        sys.exit(__doc__)
    ordner = Path(args[0]).resolve()
    with open(WERKZEUGE / 'testlauf-eingaben.csv', encoding='utf-8', newline='') as f:
        zeilen = list(csv.DictReader(f, delimiter=';'))
    z = [f'# Lesezettel {ordner.name}', '',
         'Je Eingabe: was die Sitzung sagte (wortgleich aus chat.txt), welche PDFs entstanden und worauf '
         'beim Gegenlesen zu achten ist – aus der Spalte „prüft“ von werkzeuge/testlauf-eingaben.csv, '
         'ergänzt um „Messung:“-Zeilen aus kennzahlen.md und protokoll.txt. Der Lesezettel zeigt, er '
         'bewertet nicht. Erzeugt von werkzeuge/testlauf-lesezettel.py.', '']
    for zeile in zeilen:
        z += abschnitt(ordner, zeile)
    text = '\n'.join(z).rstrip('\n') + '\n'
    if '--probe' in sys.argv:
        print(text)
        return
    with open(ordner / 'lesezettel.md', 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print(f"{ordner / 'lesezettel.md'} geschrieben: {len(zeilen)} Eingaben.")


if __name__ == '__main__':
    main()
