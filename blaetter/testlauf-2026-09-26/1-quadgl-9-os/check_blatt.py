# Prüft Lernblatt/Gesamt am Kompilat: Nummernfolge, Kopfzeilen, Verzeichnis-Sprungziele, Abhakseite, Seitenfüllung
import re, subprocess, sys
from pypdf import PdfReader

pdf = sys.argv[1]
r = PdfReader(pdf)
n = len(r.pages)
texte = [subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', '-f', str(i), '-l', str(i), pdf, '-'],
                        capture_output=True).stdout.decode('utf-8') for i in range(1, n + 1)]
nummern, abhak, seiten = [], [], []
for i, t in enumerate(texte, 1):
    kopf = t.strip().splitlines()[0] if t.strip() else ''
    nr = [int(m) for m in re.findall(r'^\s*(\d+)\. ', t, re.M)]
    if 'Das kann ich' in t and not nr:
        abhak += [int(m) for m in re.findall(r'☐?\s*(\d+)\s+Ich ', t)]
    nummern += nr
    seiten.append((i, kopf, nr, len(t)))
    print(f"Seite {i:2d} | {kopf} | Nr. {nr} | Zeichen {len(t)}")
erw = list(range(nummern[0], nummern[0] + len(nummern))) if nummern else []
print("Hauptnummern:", len(nummern), "lückenlos und aufsteigend:", nummern == erw, f"({nummern[0]}–{nummern[-1]})")
# Abhakseite: Nummern in der Reihenfolge der Seite
abh = []
for t in texte:
    if re.search(r'Das kann ich', t) and re.search(r'Ich kann|Ich erkenne|Ich finde', t) :
        abh += [int(m) for m in re.findall(r'□\s*(\d+)\.\s', t)]
print("Abhakseite:", len(abh), "Einträge, gleich den Hauptnummern:", abh == nummern)
# Sprungziele
nd = r.named_destinations
ziele = {}
for name, d in nd.items():
    try:
        ziele[name] = r.get_destination_page_number(d) + 1
    except Exception:
        pass
links = []
for a in r.pages[0].get('/Annots', []) or []:
    a = a.get_object()
    if a.get('/Subtype') == '/Link':
        act = a.get('/A')
        dest = a.get('/Dest') or (act.get_object().get('/D') if act else None)
        links.append(str(dest))
print("Links auf Seite 1:", [(l, ziele.get(l)) for l in links])
# Seitenfüllung (5.2 a): Aufgabenseiten mit weniger als einem Drittel des mittleren Textumfangs
aufg = [s for s in seiten if s[2]]
mittel = sum(s[3] for s in aufg) / len(aufg)
print("Seiten unter 1/3 des mittleren Textumfangs:", [s[0] for s in aufg if s[3] < mittel / 3])
