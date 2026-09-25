# archiv.py – schreibt protokoll.txt (Zählung aus der Textextraktion, Zeiten aus zeiten.txt) und packt das Archiv
import glob, re, subprocess, zipfile

def extrakt(pdf):
    return subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, '-'], capture_output=True, encoding='utf-8').stdout

def seiten(pdf):
    return int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))

GRAFIK = r'\\(streifen\w*|zahlenstrahl|bruchrechteck|dreieckrw)\b|\\begin\{dreisatz\}'
def grafiken(texdateien):
    return sum(len(re.findall(GRAFIK, open(f, encoding='utf-8').read())) for f in texdateien)

def zaehl_aufgaben(pdf, texdateien):
    t = extrakt(pdf)
    teil = t.split('Hake ab, was du kannst.')[0]
    hn = len(re.findall(r'^\s*\d+\. Ich ', teil, flags=re.M))
    ta = len(re.findall(r'(?:^|\s{2,})[a-h]\) ', teil, flags=re.M))
    return f'{hn} Hauptnummern, {ta} Teilaufgaben, {grafiken(texdateien)} Grafiken (aus dem Quelltext gezählt), {seiten(pdf)} Seiten'

vorlage = open('mathblatt.sty', encoding='utf-8').read().splitlines()[1].lstrip('% ').strip()
katalog = open('prozentrechnung.md', encoding='utf-8').read().splitlines()[1].strip()

z = {}
for zeile in open('zeiten.txt', encoding='ascii').read().splitlines():
    teile = zeile.rsplit(' ', 1)
    z[teile[0]] = int(teile[1])          # der letzte Stempel eines Worts zählt
t0 = z['t0']

lb_verz = [l.strip() for l in extrakt('Prozentrechnung_Lernblatt.pdf').split('\f')[0].splitlines() if 'Seite' in l and '·' in l and 'Prozentrechnung' not in l]
ges_verz = [l.strip() for l in extrakt('Prozentrechnung_Gesamt.pdf').split('\f')[0].splitlines() if 'Seite' in l and '·' in l and 'Prozentrechnung' not in l]
los = extrakt('Prozentrechnung_Loesungen.pdf')
los_nr = len(re.findall(r'^\s*(\d+)\)', los, flags=re.M))

einheiten = ['e1_a.tex', 'e2_a.tex', 'e3_a.tex', 'e4_a.tex']
P = []
P += ['Prompt: Unterrichtsblatt-Prompt v4.3', 'Modell: Opus 5.5', f'Vorlage: {vorlage}',
      f'Katalog: prozentrechnung.md, {katalog}', 'Bestellung: mit Wiederholung (ohne Ausblick: Thema im Register der Blätter)',
      'Standpunkt: Klasse 7, Oberschule (Gymnasium als Zusatz); Option schwach', '']
P += open('protokoll_teil.txt', encoding='utf-8').read().rstrip('\n').splitlines()
P += ['', 'Zählung (Textextraktion der Kompilate):',
      '- Prozentrechnung_KennstDuSchon.pdf: ' + zaehl_aufgaben('Prozentrechnung_KennstDuSchon.pdf', ['zone_a.tex']),
      '- Prozentrechnung_Lernblatt.pdf: ' + zaehl_aufgaben('Prozentrechnung_Lernblatt.pdf', einheiten),
      '  Verzeichnis: ' + ' | '.join(lb_verz),
      '- Prozentrechnung_Gesamt.pdf: ' + zaehl_aufgaben('Prozentrechnung_Gesamt.pdf', ['zone_a.tex'] + einheiten),
      '  Verzeichnis: ' + ' | '.join(ges_verz),
      f'- Prozentrechnung_Loesungen.pdf: Lösungen zu {los_nr} Nummern, {seiten("Prozentrechnung_Loesungen.pdf")} Seiten',
      '']
P += open('protokoll_schritte.txt', encoding='utf-8').read().rstrip('\n').splitlines()
P += ['', f"Zone: {z['zone'] - t0} s", f"Weiter: {z['weiter']} s (Stempel des Klicks; hier kam „weiter“ aus der Eingabe, ohne Wartezeit)"]
for n in range(1, 5):
    P.append(f"E {n}: {z['e %d' % n] - t0} s")
P += [f"Lernblatt: {z['lernblatt'] - t0} s", f"Gesamt: {z['gesamt'] - t0} s", f"Lösungen: {z['loesungen'] - t0} s",
      'Hinweis: Der Stempel „e 2“ wurde zu Beginn des Aufrufs für Einheit 3 gesetzt (nach der Durchsicht von Einheit 2), „e 3“ ebenso zu Beginn des Aufrufs für Einheit 4; „zone“ und „loesungen“ stehen zweimal in zeiten.txt, gezählt ist der letzte Stempel nach der Korrektur.']
open('protokoll.txt', 'w', encoding='utf-8').write('\n'.join(P) + '\n')

name = 'Prozentrechnung_2026-09-25_protokoll.zip'
dateien = sorted(set(glob.glob('*.pdf') + glob.glob('*.tex') + glob.glob('*.log') + glob.glob('pruef_out_*.txt') +
                 ['pruef.py', 'verzeichnis.py', 'kontrolle.py', 'archiv.py', 'mathblatt.sty', 'Anleitung_mathblatt.md',
                  'prozentrechnung.md', 'zeiten.txt', 'protokoll.txt', 'chat.txt']))
with zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for f in dateien:
        zf.write(f)
print(open('protokoll.txt', encoding='utf-8').read())
print(name, len(dateien), 'Dateien')
