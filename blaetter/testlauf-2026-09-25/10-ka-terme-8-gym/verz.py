# -*- coding: utf-8 -*-
# verz.py – Verzeichnis für Lernblatt und Gesamt aus der Textextraktion des Kompilats (nie geschätzt).
# Aufruf: python verz.py lernblatt|gesamt [pruefen]
import sys, io, os, subprocess

THEMA = 'TermeBinomischeFormeln'
EINTRAEGE = [
    ('e1', 'Einheit 1 · Klammern auflösen (Nr. 8–15)', 'Einheit 1 von 5'),
    ('e2', 'Einheit 2 · Ausklammern (Nr. 16–19)', 'Einheit 2 von 5'),
    ('e3', 'Einheit 3 · Summe mal Summe (Nr. 20–27)', 'Einheit 3 von 5'),
    ('e4', 'Einheit 4 · Binomische Formeln (Nr. 28–38)', 'Einheit 4 von 5'),
    ('e5', 'Einheit 5 · Faktorisieren (Nr. 39–46)', 'Einheit 5 von 5'),
    ('abhaken', 'Das kann ich (Abhakseite)', 'Das kann ich'),
]

def seiten(pdf):
    out = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, '-'], capture_output=True).stdout.decode('utf-8')
    s = out.split('\f')
    if s and not s[-1].strip():
        s = s[:-1]
    return s

def main():
    name = sys.argv[1]
    pruefen = len(sys.argv) > 2
    eintraege = list(EINTRAEGE)
    if name == 'gesamt':
        eintraege.insert(0, ('zone', 'Kennst du schon (Nr. 1–7)', 'Das kennst du schon'))
    pdf = f'{THEMA}_{name.capitalize()}.pdf'
    vz = f'verz_{name}.tex'
    if not os.path.exists(pdf):
        with io.open(vz, 'w', encoding='utf-8', newline='\n') as f:
            for ziel, text, _ in eintraege:
                f.write(f'\\verzzeile{{{ziel}}}{{{text} · Seiten ?–?}}\n')
        print('Platzhalter geschrieben:', vz)
        return
    s = seiten(pdf)
    start = []
    for ziel, text, marke in eintraege:
        treffer = [i + 1 for i, t in enumerate(s) if marke in t and i > 0]
        start.append(treffer[0] if treffer else None)
    zeilen = []
    for j, (ziel, text, marke) in enumerate(eintraege):
        a = start[j]
        e = (start[j + 1] - 1) if j + 1 < len(eintraege) else len(s)
        bereich = f'Seite {a}' if a == e else f'Seiten {a}–{e}'
        zeilen.append((ziel, f'{text} · {bereich}', a))
    if not pruefen:
        with io.open(vz, 'w', encoding='utf-8', newline='\n') as f:
            for ziel, zeile, _ in zeilen:
                f.write(f'\\verzzeile{{{ziel}}}{{{zeile}}}\n')
        for _, zeile, _ in zeilen:
            print(zeile)
        return
    # Prüfen: Verzeichnis im Kompilat (Seite 1) gegen die Seitenzahlen, Bereiche lückenlos, Links auf die Zweigköpfe
    fehler = 0
    seite1 = ' '.join(s[0].split())
    for ziel, zeile, a in zeilen:
        ok = ' '.join(zeile.split()) in seite1
        fehler += not ok
        print(('OK  ' if ok else 'FEHLT ') + zeile)
    ok = start == sorted(start) and start[0] == 2
    fehler += not ok
    print('Bereiche lückenlos ab Seite 2:', ok, '· Seiten gesamt:', len(s))
    from pypdf import PdfReader
    r = PdfReader(pdf)
    ziele = {str(k): r.get_destination_page_number(v) + 1 for k, v in r.named_destinations.items()}
    for annot in r.pages[0].get('/Annots', []) or []:
        a = annot.get_object()
        d = a.get('/A', {}).get('/D')
        if d is None:
            continue
        d = str(d)
        soll = dict((z, st) for z, _, st in zeilen).get(d)
        ist = ziele.get(d)
        ok = soll == ist
        fehler += not ok
        print(f'Link {d}: Ziel Seite {ist}, Verzeichnis Seite {soll}', 'OK' if ok else 'FEHLER')
    print('Fehler:', fehler)

main()
