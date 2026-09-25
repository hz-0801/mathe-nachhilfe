# archiv.py – schreibt protokoll.txt und chat.txt und packt das Protokoll-Archiv (6.3)
import re, glob, zipfile, os

EINGABE = 'lineare funktionen 8 nur das neue – Antworten auf Planfrage und Zone: alle; baue ohne Halt bis zum Ausgabeblock durch'

ZWEIGE = [
    ('Einheit 1 von 5 · Proportionale Funktion',
     'Hier lernst du, Funktionen mit y = m · x zu berechnen, zu zeichnen und zu erkennen · neu in diesem Jahr · P10 oft · baut auf: Koordinatensystem, proportionale Zuordnungen (Dreisatz)'),
    ('Einheit 2 von 5 · Lineare Funktion f(x) = m · x + n',
     'Hier lernst du, Geraden mit f(x) = m · x + n zu zeichnen, m und n abzulesen und zu deuten · neu in diesem Jahr · P10 oft · baut auf: proportionale Funktion (Einheit 1), Brüche, negative Zahlen'),
    ('Einheit 3 von 5 · Punkte und Werte',
     'Hier lernst du, Funktionswerte zu berechnen, Punkte zu prüfen und Nullstellen und Achsenschnittpunkte zu bestimmen · neu in diesem Jahr · P10 oft · baut auf: lineare Funktion (Einheit 2), lineare Gleichungen lösen, negative Zahlen'),
    ('Einheit 4 von 5 · Gleichung bestimmen',
     'Hier lernst du, die Gleichung einer Geraden aus dem Graphen, aus Steigung und Punkt oder aus zwei Punkten zu bestimmen und den Schnittpunkt zweier Geraden zu berechnen · neu in diesem Jahr · P10 · baut auf: m und n ablesen (Einheit 2), Punktprobe und Nullstelle (Einheit 3), lineare Gleichungen, Terme zusammenfassen'),
    ('Einheit 5 von 5 · Anwendungen',
     'Hier lernst du, Tarife und andere Sachsituationen mit linearen Funktionen zu beschreiben, zu berechnen und zu vergleichen · neu in diesem Jahr · P10 oft · baut auf: Gleichung, Graph und Schnittpunkt (Einheit 2 bis 4), Dreisatz'),
]

DEUTUNG = '→ Lernblatt · Standpunkt Oberschule (Gymnasium ebenfalls Kl. 8) · 5 Zweige, alle neu in Kl. 8 · ohne Zone, ohne Ausblick'
PLANFRAGE = 'Alle Zweige, oder welche? (alle · Nummern · ein Typ für den Fokus)'
ANTWORT = 'alle'

AUSGABEBLOCK = open('ausgabeblock.txt', encoding='utf-8').read().strip()
DATEIEN = ['LinFkt_Lernblatt.pdf', 'LinFkt_Gesamt.pdf', 'LinFkt_Loesungen.pdf', 'LinFkt_2026-09-25_protokoll.zip']

SCHRITTE = open('schritte.txt', encoding='utf-8').read().strip()

def titel(datei):
    return re.findall(r'\\begin\{aufgabe\}\{\\textbf\{(.+?)\}(?= )', open(datei, encoding='utf-8').read())

def zaehlung(name, loesung=False):
    txt = open(f'{name}.txt', encoding='utf-8').read()
    seiten = len([s for s in txt.split('\f') if s.strip()])
    if loesung:
        nrs = sorted(set(int(n) for n in re.findall(r'(?m)^\s*(\d+)\) ', txt)))
        return f'{name}.pdf: Lösungen zu {len(nrs)} Nummern, Seiten {seiten}'
    seitenliste = txt.split('\f')
    ab = next(i for i, s in enumerate(seitenliste) if 'Hake ab, was du kannst' in s)
    body = '\f'.join(seitenliste[1:ab])
    haupt = len(set(re.findall(r'(?m)^\s*(\d+)\.\s+Ich', body)))
    teil = len(re.findall(r'(?m)(?:^|\s{2,})[a-z]\)\s', body))
    graf = sum(open(f'e{i}_a.tex', encoding='utf-8').read().count(r'\begin{ksys}') for i in range(1, 6))
    tab = sum(open(f'e{i}_a.tex', encoding='utf-8').read().count(r'\wertetabelle') + open(f'e{i}_a.tex', encoding='utf-8').read().count(r'\begin{dreisatz}') for i in range(1, 6))
    return f'{name}.pdf: Hauptnummern {haupt}, Teilaufgaben {teil}, Koordinatensysteme {graf}, Tabellen und Dreisatzschemata {tab}, Seiten {seiten}'

def zeiten():
    z = {}
    for line in open('zeiten.txt', encoding='ascii'):
        k, v = line.split()
        z[k] = int(v)   # letzter Stempel je Wort gilt
    t0 = z['t0']
    out = ['Zone: entfällt (nur das Neue, keine Zone)', 'Weiter: entfällt (kein Halt, Antworten in der Eingabe)']
    for i in range(1, 6):
        out.append(f'E {i}: {z[f"e{i}"] - t0} s')
    out.append(f'Lernblatt: {z["lernblatt"] - t0} s')
    out.append(f'Gesamt: {z["gesamt"] - t0} s')
    out.append(f'Lösungen: {z["loesungen"] - t0} s')
    return out

kopf = open('lineare-funktionen.md', encoding='utf-8').read().splitlines()[1]
sty2 = open('mathblatt.sty', encoding='utf-8').read().splitlines()[1].lstrip('% ').strip()

P = []
P.append('Prompt: Unterrichtsblatt-Prompt v4.3')
P.append('Modell: Claude Opus 5.5')
P.append('Vorlage: ' + sty2)
P.append('Katalog: lineare-funktionen.md, ' + kopf)
P.append('Bestellung: nur das Neue')
P.append('Standpunkt: Kl. 8, ohne Schulform (Oberschule Standpunkt, Gymnasium gleiche Marke)')
P.append('')
P.append('Zweige (gebaut: alle fünf; abgewählt: keine; Ausblick: keiner – alle Marken OS/GYM Kl. 8):')
nr = 0
for i, (k, zz) in enumerate(ZWEIGE, 1):
    P.append(f'{k}')
    P.append(f'  Zweigzeile: {zz}')
    for t in titel(f'e{i}_a.tex'):
        nr += 1
        P.append(f'  {nr}. {t}')
P.append('')
P.append('Zählung aus der Textextraktion:')
P.append(zaehlung('lernblatt'))
P.append(zaehlung('gesamt'))
P.append(zaehlung('loesungen', True))
for name in ['lernblatt', 'gesamt']:
    P.append(f'Verzeichnis {name}.pdf:')
    P.append(open(f'{name}.txt', encoding='utf-8').read().split('\f')[0].strip())
P.append('')
P.append('Werkzeugaufrufe (Schritt · Anlass):')
P.append(SCHRITTE)
P.append('')
P.append('Vorlage: fehlende Bausteine · Warnungen aus dem Log')
P.append('  fehlende Bausteine: \\zweigzeile (zweite Zeile des Einheitenkopfs), Abhakseite „Das kann ich“ (minipage/tabular), unbeschriftetes Steigungsdreieck (TikZ-\\draw im ksys, Nr. 10)')
logs = ''.join(open(f, encoding='utf-8', errors='ignore').read() for f in ['lernblatt.log', 'gesamt.log', 'loesungen.log'])
warn = sorted(set(re.findall(r'Package mathblatt Warning[^\n]*|Overfull[^\n]*', logs)))
P.append('  Warnungen aus dem Log: ' + ('; '.join(warn) if warn else 'keine'))
P.append('')
P.append(f'Korrekturrunden: 5 von {len(SCHRITTE.splitlines())} Schritten (E2 Nr. 16 Abweichung; E1–E3 Buchstaben der geteilten Nummern und Überlappung Nr. 24; E4 Nr. 35 Systemhöhe; E5 Nr. 48 Feldumbruch; Abhakseite Kopf ohne Tabelle)')
P.extend(zeiten())
open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(P) + '\n')

C = [EINGABE, '', DEUTUNG, '']
for k, zz in ZWEIGE:
    C.append(f'{k}: {zz}')
C += ['', PLANFRAGE, 'Antwort: ' + ANTWORT, '', AUSGABEBLOCK, '', 'Dateien:'] + DATEIEN
open('chat.txt', 'w', encoding='utf-8').write('\n'.join(C) + '\n')

ziel = 'LinFkt_2026-09-25_protokoll.zip'
dateien = sorted(set(glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + glob.glob('pruef_out_*.txt'))) + \
    ['pruef.py', 'mathblatt.sty', 'Anleitung_mathblatt.md', 'lineare-funktionen.md', 'zeiten.txt', 'protokoll.txt', 'chat.txt',
     'rahmen.py', 'einheit.ps1', 'rahmen.ps1', 'archiv.py']
with zipfile.ZipFile(ziel, 'w', zipfile.ZIP_DEFLATED) as zf:
    for d in dateien:
        zf.write(d)
print(ziel, len(dateien), 'Dateien')
print(open('protokoll.txt', encoding='utf-8').read()[-900:])
