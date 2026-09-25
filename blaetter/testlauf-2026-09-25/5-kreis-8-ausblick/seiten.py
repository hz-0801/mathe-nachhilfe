# seiten.py – Seitenbereiche und Zählung aus der Textextraktion eines Kompilats
# Aufruf: python seiten.py <datei.txt>   (pdftotext -layout)
import sys, re
txt = open(sys.argv[1], encoding='utf-8').read()
seiten = txt.split('\f')
if seiten and not seiten[-1].strip():
    seiten = seiten[:-1]
marken = [('zone', 'Das kennst du schon'), ('e1', 'Einheit 1 von 3'), ('e2', 'Einheit 2 von 3'),
          ('e3', 'Einheit 3 von 3'), ('abhaken', 'Das kann ich')]
start = {}
for i, s in enumerate(seiten, 1):
    if i == 1 and 'Inhalt' in s:
        continue  # Verzeichnis
    for k, m in marken:
        ende = r'\s*$' if k in ('zone', 'abhaken') else ''
        if k not in start and re.search(r'^\s*' + re.escape(m) + ende, s, re.M):
            start[k] = i
# die Gruppenzeile „Das kennst du schon“ der Abhakseite ist kein Zonenbeginn
if 'zone' in start and 'e1' in start and start['zone'] > start['e1']:
    del start['zone']
reihe = [k for k, _ in marken if k in start]
for j, k in enumerate(reihe):
    ende = (start[reihe[j+1]] - 1) if j + 1 < len(reihe) else len(seiten)
    print(f"{k}: Seiten {start[k]}–{ende}")
print(f"Seiten gesamt: {len(seiten)}")
nummern = re.findall(r'^\s{0,3}(\d+)\. Ich ', txt, re.M)
teile = re.findall(r'(?:^|\s)([a-h])\) ', txt)
print(f"Hauptnummern (Titelzeilen): {len(nummern)}: {' '.join(nummern)}")
print(f"Teilaufgaben-Marken a)–h): {len(teile)}")
# Seitenfüllung
laengen = [len(re.sub(r'\s+', '', s)) for s in seiten]
print("Zeichen je Seite:", laengen)
