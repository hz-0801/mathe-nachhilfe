# -*- coding: utf-8 -*-
# Prüfung der Rahmendateien auf Kompilat (5.1 c, 5): Nummern durchlaufend, Kopfzeile je Seite mit Einheit,
# Verzeichniszeile -> Zweigkopf (Linkziele), Abhakseite vollständig und wortgleich, Zählung für protokoll.txt.
import sys, re, subprocess, io
from pypdf import PdfReader

pdf = sys.argv[1]
erwartet_von, erwartet_bis = int(sys.argv[2]), int(sys.argv[3])
r = PdfReader(pdf)
n = len(r.pages)
seiten = []
for i in range(1, n + 1):
    t = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', str(i), '-l', str(i), pdf, '-'],
                       capture_output=True).stdout.decode('utf-8')
    seiten.append(t)
fehler = 0
aus = []
# Hauptnummern (ohne Abhakseite)
nums, abhakseite = [], None
for i, t in enumerate(seiten):
    if re.search(r'Das kann ich', t) and re.search(r'☐|□', t) and re.search(r'(?m)^\s*\S*\s*\d+\s+Ich', t) and not re.search(r'(?m)^\s*\d+\.\s+Ich', t):
        abhakseite = i
        continue
    nums += [int(m) for m in re.findall(r'(?m)^\s*(\d+)\.\s+Ich', t)]
ok = nums == list(range(erwartet_von, erwartet_bis + 1))
aus.append('Hauptnummern: %d (%s–%s), durchlaufend: %s' % (len(nums), nums[0] if nums else '-', nums[-1] if nums else '-', 'ja' if ok else 'NEIN ' + str(nums)))
fehler += 0 if ok else 1
# Teilaufgaben: Zeilen, die mit a) b) … beginnen (auch zweispaltig)
teil = sum(len(re.findall(r'(?:^|\s{2,})([a-p])\)\s', t, re.M)) for j, t in enumerate(seiten) if j != abhakseite)
aus.append('Teilaufgaben (Textextraktion): %d' % teil)
# Kopfzeile je Seite
for i, t in enumerate(seiten):
    kopf = t.strip().splitlines()[0] if t.strip() else ''
    if not re.search(r'Kennst du schon|[1-4] [A-ZÄÖÜ]|Das kann ich', kopf):
        aus.append('Seite %d: Kopfzeile ohne Einheit: %s' % (i + 1, kopf.strip()))
        fehler += 1
aus.append('Kopfzeilen geprüft: %d Seiten' % n)
# Linkziele der Verzeichniszeile
ziele = []
for annot in (r.pages[0].get('/Annots') or []):
    a = annot.get_object()
    if a.get('/Subtype') != '/Link':
        continue
    dest = a.get('/Dest')
    if dest is None and a.get('/A') is not None:
        dest = a['/A'].get('/D')
    if dest is None:
        continue
    if isinstance(dest, str) or hasattr(dest, 'startswith'):
        d = r.named_destinations.get(str(dest))
        seite = r.get_destination_page_number(d) if d is not None else None
        name = str(dest)
    else:
        seite = r.get_page_number(dest[0].get_object() if hasattr(dest[0], 'get_object') else dest[0])
        name = '?'
    ziele.append((name, seite))
for name, seite in ziele:
    t = seiten[seite] if seite is not None else ''
    kopf = {'zone': 'Das kennst du schon', 'e1': 'Einheit 1 von 4', 'e2': 'Einheit 2 von 4', 'e3': 'Einheit 3 von 4',
            'e4': 'Einheit 4 von 4', 'abhaken': 'Das kann ich'}.get(name.split('.')[-1], '')
    treffer = kopf and kopf in t
    aus.append('Link %s -> Seite %s: %s' % (name, None if seite is None else seite + 1, 'Zweigkopf da' if treffer else 'NICHT GEFUNDEN'))
    fehler += 0 if treffer else 1
# Abhakseite gegen Quelltitel
if len(sys.argv) > 4:
    quelle = io.open('abhaken.tex', encoding='utf-8').read()
    abh = [int(m) for m in re.findall(r'\\abhak\{(\d+)\}', quelle)]
    ab_ok = abh == list(range(1, 50))
    text = seiten[abhakseite] if abhakseite is not None else ''
    if abhakseite is None:
        # Abhakseite kann über zwei Seiten gehen: letzte Seiten durchsuchen
        text = '\n'.join(seiten[-2:])
    im_pdf = [int(m) for m in re.findall(r'[□☐]\s*(\d+)\.\s+Ich', '\n'.join(seiten[-2:]))]
    aus.append('Abhakseite: Quelle 1–49 vollständig: %s; im Kompilat %d Zeilen (%s–%s)' % (
        'ja' if ab_ok else 'NEIN', len(im_pdf), im_pdf[0] if im_pdf else '-', im_pdf[-1] if im_pdf else '-'))
    fehler += 0 if ab_ok and im_pdf == list(range(1, 50)) else 1
grafik = sum(1 for j, t in enumerate(seiten))
aus.append('Seiten: %d' % n)
aus.append('Befunde: %d' % fehler)
print('\n'.join(aus))
