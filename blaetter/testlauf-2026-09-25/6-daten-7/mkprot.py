# mkprot.py – protokoll.txt und chat.txt schreiben, dann das Protokoll-Archiv packen (6.3)
import re, subprocess, zipfile, glob, os

def text(pdf, f=None, l=None):
    a = ['pdftotext', '-layout', '-enc', 'UTF-8']
    if f: a += ['-f', str(f), '-l', str(l)]
    return subprocess.run(a + [pdf, '-'], capture_output=True, text=True, encoding='utf-8').stdout

def seiten(pdf):
    return int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))

GRAF = r'\\(saeulenab|balkenab|liniendia|kreisleer|kreisdiagrammleer|kreisdiagramm|streifenleer|streifen|zahlenstrahl|winkelstrahl)\b|\\begin\{boxplots\}'
def grafiken(dateien):
    return sum(len(re.findall(GRAF, open(d, encoding='utf-8').read())) for d in dateien)

def aufgaben(pdf, quellen):
    t = text(pdf)
    t = t.split('Das kann ich')[0] if 'Das kann ich (Nr.' not in t else t
    haupt = len(re.findall(r'^\s*\d+\. Ich', t, re.M))
    teil = len(re.findall(r'(?:^|\s)[a-l]\) ', t, re.M))
    return f'Hauptnummern {haupt}, Teilaufgaben {teil}, Grafiken {grafiken(quellen)} (aus dem Quelltext gezählt), Seiten {seiten(pdf)}'

def loes(pdf):
    t = text(pdf)
    return f'Nummern mit Lösung {len(re.findall(r"^\s*\d+\)", t, re.M))}, Lösungsgrafiken {grafiken(["e1_l.tex", "e2_l.tex"])}, Seiten {seiten(pdf)}'

def verz(pdf):
    return ' | '.join(z.strip() for z in text(pdf, 1, 1).splitlines() if '·' in z and 'Seite' in z)

stempel = {}
for z in open('zeiten.txt', encoding='ascii').read().split('\n'):
    if z.strip():
        k, v = z.rsplit(' ', 1); stempel[k] = int(v)   # letzter Stempel je Wort zählt
t0 = stempel['t0']

EINGABE = 'daten 7 – Antworten auf Planfrage und Zone: sek i, alle; baue ohne Halt bis zum Ausgabeblock durch'
DEUTUNG = ('→ Lernblatt · Kl. 7 · Standpunkt Oberschule, Gymnasium als Zusatz · mit Wiederholung, ohne Ausblick (Thema im Register der Blätter) · '
           '2 Zweige · Einheiten 1, 2 und 4 (Marke vor Kl. 7) als Fertigkeiten in der Zone · Einheit 6 (Sek II) und Einheit 7 (Vierfeldertafel, Kl. 9) weggelassen · Zone aus 9 Fertigkeiten')
PLAN = ['Einheit 1 von 2 · Streifen- und Kreisdiagramm – Hier lernst du, Anteile als Streifen und als Kreisdiagramm darzustellen · neu oder schon bekannt – je nach Buch (am Gymnasium schon seit Klasse 6) · P10 oft · baut auf: Häufigkeiten und Anteile (Kennst du schon), Prozentsatz, Längen in cm und mm, Winkel zeichnen',
        'Einheit 2 von 2 · Diagramme beurteilen und Boxplot – Hier lernst du, Aussagen zu Diagrammen zu prüfen, täuschende Diagramme zu erkennen und Boxplots zu lesen · neu oder schon bekannt – je nach Buch, bis Klasse 9 (am Gymnasium neu in diesem Jahr) · P10 · baut auf: Säulendiagramme lesen und Kenngrößen (Kennst du schon), Prozentsatz, Bruchteil und Vielfaches']
PLANFRAGE = ('Keine Planfrage gestellt: der Plan hat zwei Zweige (unter vier), die Stufe ist durch Kl. 7 aufgelöst. '
             'Antwort aus der Eingabe „sek i, alle“ – bestätigt Sek I und alle Zweige.')
ZONEZEILE = 'Weiter baut Einheit 1 bis 2, Gesamt und Lösungen.'
DATEIEN = ['Daten_KennstDuSchon.pdf', 'Daten_Lernblatt.pdf', 'Daten_Gesamt.pdf', 'Daten_Loesungen.pdf', 'Daten_2026-09-25_protokoll.zip']
AUSGABE = open('ausgabeblock.txt', encoding='utf-8').read().strip()

TITEL = {}
for d in ['zone_a.tex', 'e1_a.tex', 'e2_a.tex']:
    t = open(d, encoding='utf-8').read()
    s = int(re.search(r'\\setcounter\{aufgabe\}\{(\d+)\}', t).group(1))
    TITEL[d] = [f'{s + i + 1}. {x}' for i, x in enumerate(re.findall(r'\\begin\{aufgabe\}\{\\textbf\{([^{}]*)\}', t))]

sty2 = open('mathblatt.sty', encoding='utf-8').read().splitlines()[1].lstrip('% ').strip()
stand = open('daten.md', encoding='utf-8').read().splitlines()[1]

p = []
p += ['Prompt: Unterrichtsblatt-Prompt v4.3', 'Modell: Claude Opus 5.5 (claude-opus-5-5)', f'Vorlage: {sty2}',
      f'Katalog: daten.md, {stand}', 'Bestellung: mit Wiederholung (ohne Ausblick: das Register der Blätter führt „daten“ seit 2026-09-22)',
      'Standpunkt: Kl. 7, Oberschule (keine Schulform genannt), Gymnasium als Zusatz', '']
p += ['Zweige:', 'Gebaut:'] + ['  ' + z for z in PLAN]
p += ['Zone (Wiederholung, Marke vor Kl. 7): Katalog-Einheit 1 Häufigkeiten (OS Kl. 5–6), Einheit 2 Säulen-, Balken- und Liniendiagramme (OS Kl. 5–6), Einheit 4 Kenngrößen (OS Kl. 6) – je eine Fertigkeit mit dem Grundfall',
      'Abgewählt/weggelassen: Einheit 6 Kenngrößen aus Häufigkeitstabellen und Klassen (Sek II); Einheit 7 Vierfeldertafel (OS Kl. 9, GYM Kl. 9–10 – Ausblick, nicht bestellt)',
      'Ausblick: keiner', '']
p += ['Hauptnummern:', 'Kennst du schon:'] + ['  ' + x for x in TITEL['zone_a.tex']]
p += ['Einheit 1 von 2:'] + ['  ' + x for x in TITEL['e1_a.tex']]
p += ['Einheit 2 von 2:'] + ['  ' + x for x in TITEL['e2_a.tex']] + ['']
p += ['Zählung aus der Textextraktion:',
      'Daten_KennstDuSchon.pdf: ' + aufgaben('Daten_KennstDuSchon.pdf', ['zone_a.tex']),
      'Daten_Lernblatt.pdf: ' + aufgaben('Daten_Lernblatt.pdf', ['e1_a.tex', 'e2_a.tex']),
      '  Verzeichnis: ' + verz('Daten_Lernblatt.pdf'),
      'Daten_Gesamt.pdf: ' + aufgaben('Daten_Gesamt.pdf', ['zone_a.tex', 'e1_a.tex', 'e2_a.tex']),
      '  Verzeichnis: ' + verz('Daten_Gesamt.pdf'),
      'Daten_Loesungen.pdf: ' + loes('Daten_Loesungen.pdf'), '']
p += ['Schritte (Schritt · Anlass):'] + open('schritte.txt', encoding='utf-8').read().strip().splitlines() + ['']
p += ['Vorlage: fehlende Bausteine · Warnungen aus dem Log',
      'Fehlende Bausteine: zweite Zeile des Einheitenkopfs für die Zweigzeile (\\zweigkopf im Vorspann von Lernblatt und Gesamt), Zonenkopf (\\zonekopf), Abschnittskopf der Lösungen (\\loesungskopf), Abhakseite „Das kann ich“ (von verz.py aus den Titeln erzeugt, mit \\einheitenkopf und $\\square$)',
      'Warnungen aus dem Log: „Package mathblatt Warning: Hauptnummer 26 ist hoeher als eine Seite“ (Folge eines Tabellenfehlers, behoben); Overfull \\hbox 0,9 pt bei den drei Winkelstrahlen der Zone (Nr. 7, verbleibt); sonst keine', '']
p += ['Korrekturrunden: 14 von 44 Schritten (zwei davon abgebrochene Aufrufe)']
p += [f"Zone: {stempel['zone'] - t0} s",
      f"Weiter: {stempel['weiter']} (Stempel des Durchlaufs ohne Wartezeit; kein Gegenüber, „weiter“ lag in der Eingabe)",
      f"E 1: {stempel['e 1'] - t0} s", f"E 2: {stempel['e 2'] - t0} s",
      f"Lernblatt: {stempel['lernblatt'] - t0} s", f"Gesamt: {stempel['gesamt'] - t0} s", f"Lösungen: {stempel['loesungen'] - t0} s",
      'Hinweis: „zone“, „lernblatt“ und „gesamt“ wurden nach Korrekturrunden erneut gestempelt; gezählt ist jeweils der letzte Stempel.']
open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(p) + '\n')

c = ['Eingabe des Lehrers:', EINGABE, '', 'Deutungszeile und Plan:', DEUTUNG] + PLAN + ['', 'Planfrage mit Antwort:', PLANFRAGE, '',
     'Nach der Zone:', ZONEZEILE, '', 'Rückfragen: keine', '', 'Ausgabeblock:', AUSGABE, '', 'Übergebene Dateien:'] + DATEIEN
open('chat.txt', 'w', encoding='utf-8').write('\n'.join(c) + '\n')

inhalt = (glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + ['pruef.py', 'verz.py', 'mkprot.py', 'linkcheck.py']
          + glob.glob('pruef_out_*.txt') + ['mathblatt.sty', 'Anleitung_mathblatt.md', 'daten.md', 'zeiten.txt', 'protokoll.txt', 'chat.txt'])
with zipfile.ZipFile('Daten_2026-09-25_protokoll.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for f in sorted(set(inhalt)):
        z.write(f)
print(open('protokoll.txt', encoding='utf-8').read())
print('Archiv:', len(set(inhalt)), 'Dateien')
