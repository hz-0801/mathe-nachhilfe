# archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3, Punkt 4)
import re, subprocess, zipfile, glob, os
from pypdf import PdfReader

THEMA = 'Kurvenuntersuchung'
DATUM = '2026-09-25'

def text(pdf):
    return subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, '-'], capture_output=True).stdout.decode('utf-8')

def seiten(pdf):
    return len(PdfReader(pdf).pages)

def grafiken(quellen):
    n = 0
    for q in quellen:
        s = open(q, encoding='utf-8').read()
        n += s.count('\\begin{ksys}') + 2 * s.count('\\ableitungspaar')
    return n

def zaehle_aufgaben(pdf, quellen):
    t = text(pdf)
    hn = len(re.findall(r'(?m)^\s*\d+\. (?:Ich )', t))
    teil = len(re.findall(r'(?:^|\s)[a-z]\) ', t))
    return hn, teil, grafiken(quellen), seiten(pdf)

def zaehle_loesungen(pdf, quellen):
    t = text(pdf)
    nrn = sorted(set(int(m) for m in re.findall(r'(?m)^\s*(\d+)\) ', t)))
    return len(nrn), grafiken(quellen), seiten(pdf)

def verzeichnis(pdf):
    t = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', '1', '-l', '1', pdf, '-'], capture_output=True).stdout.decode('utf-8')
    return [z.strip() for z in t.splitlines() if '·' in z and ('Seite' in z)]

E = ['e1', 'e2', 'e3', 'e4', 'e5']
z = []
z.append('Prompt: Unterrichtsblatt-Prompt v4.3')
z.append('Modell: Opus 5.5 (claude-opus-5-5)')
sty2 = open('mathblatt.sty', encoding='utf-8').read().splitlines()[1]
z.append('Vorlage: ' + sty2.lstrip('% ').strip())
kat2 = open('kurvenuntersuchung.md', encoding='utf-8').read().splitlines()[1]
z.append('Katalog: kurvenuntersuchung.md, ' + kat2.split(' · ')[0])
z.append('Bestellung: mit Wiederholung · mit Ausblick (kein Ausblick-Zweig vorhanden)')
z.append('Standpunkt: Klasse 12, Berlin, Gymnasium (Abitur-Gang), Grundkurs')
z.append('')
z.append('Zweige (gebaut: 1–5; abgewählt: keine; Ausblick: keiner):')
zweig = {}
for e in E:
    s = open(e + '_a.tex', encoding='utf-8').read()
    kopf = re.search(r'\\einheitenkopf\{(.*?)\}', s).group(1)
    zeile = re.search(r'\\zweigzeile\{(.*?)\}\n', s).group(1)
    z.append('  ' + kopf)
    z.append('    ' + zeile)
titel = open('titel.txt', encoding='utf-8').read().splitlines()
z.append('')
z.append('Hauptnummern mit Titel (Zone und Zweige):')
z += ['  ' + t for t in titel]
z.append('')
z.append('Zählung aus der Textextraktion der Kompilate (Grafiken aus dem Quelltext gezählt, weil die Textextraktion Vektorgrafik nicht erfasst):')
hn, teil, gr, s = zaehle_aufgaben(f'{THEMA}_KennstDuSchon.pdf', ['zone_a.tex'])
z.append(f'  {THEMA}_KennstDuSchon.pdf: {hn} Hauptnummern, {teil} Teilaufgaben, {gr} Grafiken, {s} Seiten')
hn, teil, gr, s = zaehle_aufgaben(f'{THEMA}_Lernblatt.pdf', [e + '_a.tex' for e in E])
z.append(f'  {THEMA}_Lernblatt.pdf: {hn} Hauptnummern, {teil} Teilaufgaben, {gr} Grafiken, {s} Seiten; Verzeichnis:')
z += ['    ' + v for v in verzeichnis(f'{THEMA}_Lernblatt.pdf')]
hn, teil, gr, s = zaehle_aufgaben(f'{THEMA}_Gesamt.pdf', ['zone_a.tex'] + [e + '_a.tex' for e in E])
z.append(f'  {THEMA}_Gesamt.pdf: {hn} Hauptnummern, {teil} Teilaufgaben, {gr} Grafiken, {s} Seiten; Verzeichnis:')
z += ['    ' + v for v in verzeichnis(f'{THEMA}_Gesamt.pdf')]
n, gr, s = zaehle_loesungen(f'{THEMA}_Loesungen.pdf', ['zone_l.tex'] + [e + '_l.tex' for e in E])
z.append(f'  {THEMA}_Loesungen.pdf: Lösungen zu {n} Nummern, {gr} Lösungsgrafiken, {s} Seiten')
z.append('')
z.append('Werkzeugaufrufe (Schritt · Anlass):')
schritte = open('schritte.txt', encoding='utf-8').read().splitlines()
z += ['  ' + s for s in schritte]
z.append('')
z.append('Vorlage: fehlende Bausteine · Warnungen aus dem Log')
z.append('  fehlende Bausteine: zweite Zeile des Einheitenkopfs (\\zweigzeile), Abhakseite (\\abhakgruppe, \\abhak), Verzeichniszeile mit Link (\\verzeile) – im Vorspann von Lernblatt und Gesamt definiert, \\zweigzeile auch im Prüfrahmen check.tex')
warn = set()
for lg in glob.glob(THEMA + '_*.log'):
    for l in open(lg, encoding='utf-8', errors='replace'):
        if 'mathblatt Warning' in l or 'Overfull' in l:
            warn.add(os.path.basename(lg) + ': ' + l.strip())
z.append('  Warnungen: ' + ('; '.join(sorted(warn)) if warn else 'keine'))
korr = sum(1 for s in schritte if 'Korrektur' in s)
z.append('')
z.append(f'Korrekturrunden: {korr} von {len(schritte)} Schritten')
st = {}
for l in open('zeiten.txt', encoding='ascii'):
    teile = l.split()
    st[' '.join(teile[:-1])] = int(teile[-1])
t0 = st['t0']
z.append(f"Zone: {st['zone'] - t0} s")
z.append(f"Weiter: {st['weiter']} s (Stempel; Wartezeit {st['weiter'] - st['zone']} s, unbeaufsichtigter Lauf ohne Klick)")
for i in range(1, 6):
    z.append(f"E {i}: {st['e %d' % i] - t0} s")
z.append(f"Lernblatt: {st['lernblatt'] - t0} s")
z.append(f"Gesamt: {st['gesamt'] - t0} s")
z.append(f"Lösungen: {st['loesungen'] - t0} s")
open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(z) + '\n')

open('chat.txt', 'w', encoding='utf-8').write(open('chat_quelle.txt', encoding='utf-8').read())

name = f'{THEMA}_{DATUM}_protokoll.zip'
dateien = sorted(set(glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + glob.glob('pruef_out_*.txt') +
                     ['pruef.py', 'rahmen.py', 'archiv.py', 'mathblatt.sty', 'Anleitung_mathblatt.md', 'kurvenuntersuchung.md',
                      'zeiten.txt', 'protokoll.txt', 'chat.txt', 'titel.txt', 'schritte.txt']))
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for d in dateien:
        if os.path.exists(d): zf.write(d)
print(name, len(dateien), 'Dateien')
print('\n'.join(z[-12:]))
