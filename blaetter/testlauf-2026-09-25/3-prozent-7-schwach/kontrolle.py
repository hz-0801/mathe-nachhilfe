# kontrolle.py – Verzeichnis gegen Kompilat (Links, Seiten), durchlaufende Nummern, Seitenfüllung, Zählung
#   python kontrolle.py <rahmen>
import re, sys, subprocess
from pypdf import PdfReader

rahmen = sys.argv[1]
r = PdfReader(rahmen + '.pdf')
n = len(r.pages)
texte = []
for s in range(1, n + 1):
    t = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', str(s), '-l', str(s), rahmen + '.pdf', '-'],
                       capture_output=True, encoding='utf-8').stdout
    texte.append(t)

# Links auf Seite 1 -> Zielseite
if '/Annots' in r.pages[0]:
    ziele = {}
    for a in r.pages[0]['/Annots']:
        a = a.get_object()
        dest = a.get('/Dest') or (a.get('/A') or {}).get('/D')
        if dest is None:
            continue
        if isinstance(dest, str) or hasattr(dest, 'encode'):
            d = r.named_destinations.get(str(dest))
            seite = r.get_destination_page_number(d) + 1 if d is not None else None
        else:
            seite = r.get_page_number(dest[0].get_object()) + 1 if hasattr(dest[0], 'get_object') else None
        ziele[str(dest)] = seite
    print('Links Seite 1 -> Zielseite:', ziele)

# Verzeichniszeilen gegen erste Seite
for m in re.finditer(r'(Einheit \d|Kennst du schon|Das kann ich).*?Seiten? (\d+)(?:–(\d+))?', re.sub(r'\s+', ' ', texte[0])):
    s = int(m.group(2))
    kopf = {'Kennst du schon': 'Das kennst du schon', 'Das kann ich': 'Das kann ich'}.get(m.group(1), m.group(1) + ' von 4')
    ok = kopf in re.sub(r'\s+', ' ', texte[s - 1])
    print(f'Verzeichnis {m.group(1):16s} Seite {s}: Kopf gefunden = {ok}')

# durchlaufende Hauptnummern (ohne Abhakseite und Verzeichnis)
nummern = []
for t in texte[1:]:
    if 'Das kann ich' in t and 'Hake ab' in t:
        break
    nummern += [int(x) for x in re.findall(r'^\s*(\d+)\. Ich ', t, flags=re.M)]
print('Hauptnummern:', nummern[:3], '...', nummern[-3:], 'Anzahl', len(nummern),
      'durchlaufend' if nummern == list(range(nummern[0], nummern[0] + len(nummern))) else 'LÜCKE/DOPPELT')

# Teilaufgaben (a), b) … am Zeilenanfang oder nach Leerraum), Seitenfüllung
teil = sum(len(re.findall(r'(?:^|\s{2,})[a-h]\) ', t, flags=re.M)) for t in texte[1:])
laengen = [len(re.sub(r'\s+', '', t)) for t in texte]
aufgabenseiten = [l for l in laengen[1:]]
median = sorted(aufgabenseiten)[len(aufgabenseiten) // 2]
leer = [i + 2 for i, l in enumerate(aufgabenseiten) if l < median / 3]
print('Seiten', n, '· Teilaufgaben (Textextraktion)', teil, '· Median Zeichen/Seite', median, '· Seiten unter 1/3:', leer)
