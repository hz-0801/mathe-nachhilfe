# build.py – kompiliert eine Rahmendatei mit xelatex (zweimal), liest das Log,
# rendert die Seiten (pdftoppm -r 60) und gibt je Seite die Hauptnummern aus der
# Textextraktion aus.  Aufruf: python build.py <rahmen.tex> <jobname> [render]
import sys, subprocess, re, os

rahmen, job = sys.argv[1], sys.argv[2]
render = len(sys.argv) > 3 and sys.argv[3] == 'render'
for _ in range(2):
    subprocess.run(['xelatex', '-interaction=nonstopmode', f'-jobname={job}', rahmen],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
log = open(f'{job}.log', encoding='utf-8', errors='replace').read()
fehler = [l for l in log.splitlines() if l.startswith('!')]
warn = [l.strip() for l in log.splitlines()
        if ('Warning' in l and 'rerunfilecheck' not in l) or l.startswith('Overfull')]
print('LOG Fehler:', fehler if fehler else 'keine')
print('LOG Warnungen/Overfull:', warn if warn else 'keine')
info = subprocess.run(['pdfinfo', f'{job}.pdf'], capture_output=True, text=True).stdout
seiten = int(re.search(r'Pages:\s+(\d+)', info).group(1))
print('Seiten:', seiten)
for s in range(1, seiten + 1):
    t = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', str(s), '-l', str(s),
                        f'{job}.pdf', '-'], capture_output=True, text=True, encoding='utf-8').stdout
    nrs = re.findall(r'^\s*(\d+)\. ', t, re.M)
    teile = len(re.findall(r'(?:^|\s)[a-z]\) ', t))
    kopf = re.findall(r'(Einheit \d von \d|Kennst du schon|Das kann ich|Inhalt)', t)
    zeichen = len(t.strip())
    print(f'S.{s}: Nr {",".join(nrs)} · Teilaufgaben {teile} · Zeichen {zeichen} · {sorted(set(kopf))}')
if render:
    subprocess.run(['pdftoppm', '-png', '-r', '60', f'{job}.pdf', f'bild_{job}'])
