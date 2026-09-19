#!/usr/bin/env python3
"""Strukturprüfung aller Katalogeinträge (seit 09e, Maßnahme b der Opus-Arbeitsweise):
1. Sind alle Pflichtabschnitte vorhanden?
2. Trägt jeder Eintrag eine Zeile „Zuordnung:“ am Zeilenanfang (seit 10d)? Ohne sie läuft die
   P10-Typenprüfung von _pruef_katalog.py --thema nicht; drei Einträge hatten sie über einen Monat nicht.
3. Trägt jede Sprossenkette „(Einheit n)“ (seit 10d) und endet sie mit „Prüfungshöhe“?
4. Existiert jede genannte Original-id in katalog-basis.csv oder katalog-kontext.csv?
5. Kennzahl 5 (seit 10h): die Gegenrichtung – wie viele Originale der beiden CSV-Dateien stehen in
   keinem Eintrag? Das ist bewusst eine Kennzahl und kein Befund: sie sinkt mit jedem Gegenlese-Block
   und soll den einen gewollt sichtbaren Befund nicht zudecken. Bis 10g fiel diese Lücke nur von Hand
   auf (2021-OS-K6b am 10g, 2023-OS-K5c und 2024-OS-B1c am 10h).
Aufruf im Ordner katalog/: python3 _pruef_struktur.py – die CSVs werden eine Ebene darüber erwartet.
Aufgabenstämme ohne Teilaufgabenbuchstaben (2017-OS-K7) werden nicht geprüft.
"""
import re,sys,csv,glob,os
ids=set()
for f in ('../msa/msa-katalog-basis.csv','../msa/msa-katalog-kontext.csv'):  # Umbau 2026-09-19: Kataloge liegen in msa/
    for r in csv.DictReader(open(f,encoding='utf-8'),delimiter=';'): ids.add(r['id'])
ABS=["### Verortung","### Lerneinheiten","### Typen je Lerneinheit","### Voraussetzungen (Blatt 0)","### Merkkasten","### Typische Fehler","### Für schwache Schüler","### Prüfungsform","### Offene Punkte des Eintrags","## Prüfliste"]
bad=0
for p in sorted(glob.glob('*.md')):
    if p.startswith('_') or p=='index.md': continue
    t=open(p,encoding='utf-8').read()
    miss=[a for a in ABS if a not in t]
    if miss: print(p,'FEHLENDE ABSCHNITTE:',miss); bad+=1
    zeile=re.search(r"^Zuordnung: ?(\S.*)$",t,re.M)
    if not zeile:
        print(p,'FEHLENDE ZEILE: Zuordnung:'); bad+=1
    else:
        # seit 10g: die Rahmenbedingung verlangt, dass Einheiten ohne Typ ausdrücklich als
        # „kein Typ“ geführt werden. Bis 10f prüfte das Skript nur, DASS die Zeile da ist –
        # drei Einträge ließen eine Einheit stillschweigend weg, ohne dass eine Kennzahl fiel.
        # Sammelformen („Einheit 2 bis 4 – kein Typ“, „keine eigenen Typen“) gelten als erfüllt.
        z=zeile.group(1)
        einheiten=sorted(set(int(x) for x in re.findall(r"^Einheit (\d+):",t,re.M)))
        genannt=set()
        for a,b in re.findall(r"Einheit(?:en)? (\d+)\s*(?:bis|–|-|und|,)\s*(\d+)",z):
            genannt.update(range(int(a),int(b)+1))
        genannt.update(int(x) for x in re.findall(r"Einheit(?:en)? (\d+)",z))
        if 'keine eigenen Typen' in z: genannt.update(einheiten)
        fehlt=[u for u in einheiten if u not in genannt]
        if fehlt: print(p,'ZUORDNUNGSZEILE NENNT EINHEIT NICHT:',fehlt); bad+=1
    schwach=re.search(r"^### Für schwache Schüler(.*?)(?=^### |\Z)",t,re.S|re.M).group(1)
    for line in schwach.splitlines():
        if not line.startswith('- '): continue
        hat_einheit=re.match(r"^- .*?\(Einheit \d+[^)]*\):",line)
        if hat_einheit and 'Prüfungshöhe' not in line:
            print(p,'SPROSSE OHNE PRÜFUNGSHÖHE:',line[:70]); bad+=1
        # seit 10d: eine Sprossenkette ohne „(Einheit n)“ fällt durch beide Prüfer – die
        # Kastenzahlen ihrer Einheit werden nie gegen sie gehalten und die Prüfungshöhe nie geprüft.
        if not hat_einheit and 'Prüfungshöhe' in line:
            print(p,'SPROSSE OHNE EINHEITENANGABE:',line[:70]); bad+=1
    for m in set(re.findall(r"\b20\d\d-(?:OS|FOR)-[BK]\d+[a-z]\b",t)):
        if m not in ids: print(p,'UNBEKANNTE ID:',m); bad+=1
print('Strukturprüfung:', 'ok' if bad==0 else f'{bad} Befunde')

# --- Kennzahlen (seit 10a, gehören in jede Übergabe) ---
eintraege=[p for p in sorted(glob.glob('*.md')) if not p.startswith('_') and p!='index.md']
gelesen=[]
for p in eintraege:
    kopf=open(p,encoding='utf-8').read().split('\n',3)[:3]
    if re.search(r'gegengelesen:\s*ja',' '.join(kopf)): gelesen.append(p)
print(f'Kennzahl 1 – gegengelesen: {len(gelesen)} von {len(eintraege)} Einträgen')

try:
    fr=open('_fragen.md',encoding='utf-8').read()
except FileNotFoundError:
    print('Kennzahl 2 – _fragen.md fehlt'); sys.exit(0)
quer=0; eintr=0; fragen=0
for line in fr.splitlines():
    m=re.match(r'^- \[ \] (\*\*)?([A-Z]\d\b|[a-z][a-z-]+)',line)
    if not m: continue
    if re.fullmatch(r'A\d',m.group(2)): quer+=1
    else: eintr+=1; fragen+=line.count(" | ")+1
zu=len(re.findall(r'^- \[x\]',fr,re.M))
print(f'Kennzahl 2 – offene Entscheidungen: {quer+fragen} '
      f'({quer} Querschnittsfragen, {fragen} Einzelfragen in {eintr} Einträgen), entschieden: {zu}')

# --- Kennzahl 3 (seit 10f): Einträge, an denen die Gegenlese fertig ist und nur noch [FS] fehlt.
# Ohne sie stünde Kennzahl 1 bis zur Lieferung der Formelsammlung auf null, obwohl die Blöcke laufen.
fs=[p for p in eintraege
    if re.search(r'gegengelesen:\s*bis auf \[FS\]','\n'.join(open(p,encoding='utf-8').read().split('\n',3)[:3]))]
print(f'Kennzahl 3 – gegengelesen bis auf [FS]: {len(fs)} von {len(eintraege)} Einträgen')
try:
    fsl=open('_formelsammlung.md',encoding='utf-8').read()
    offen=len(re.findall(r'^- \[ \]',fsl,re.M)); fertig=len(re.findall(r'^- \[x\]',fsl,re.M))
    print(f'Kennzahl 4 – Formelsammlung [FS]: {fertig} von {offen+fertig} Kastenzeilen geprüft')
except FileNotFoundError:
    print('Kennzahl 4 – _formelsammlung.md fehlt')

# --- Kennzahl 5 (seit 10h): Originale, die in keinem Eintrag vorkommen.
volltext=' '.join(open(p,encoding='utf-8').read() for p in eintraege)
ohne=sorted(i for i in ids if i not in volltext)
print(f'Kennzahl 5 – Originale in keinem Eintrag: {len(ohne)} von {len(ids)}')
if '-v' in sys.argv:
    for i in ohne: print('   ', i)

# --- Kennzahl 6 (seit 10i): Originale, die nicht in der Datei ihres CSV-Themas stehen.
# Warum zusätzlich zu Kennzahl 5: Kennzahl 5 zählt jede Nennung, auch eine in einer Fehler-
# zeile eines fremden Eintrags. Ein Original kann dort „gezählt“ sein, ohne in irgendeiner
# Prüfungsform zu stehen – so blieb 2015-OS-K7c bis 10i unentdeckt (CSV-Thema Prozentrechnung,
# genannt nur in der Fehlerzeile von daten.md). Die Gliederungsregel sagt: das Original wird
# bei seinem CSV-Thema geführt. Kennzahl 6 prüft genau das und schließt Kennzahl 5 ein;
# die Differenz beider Zahlen ist die Zahl der Originale, die im falschen Eintrag stehen.
# Die Zuordnung CSV-Thema → Datei steht in index.md unter „CSV-Themen und führende Dateien“
# (ein Thema kann über zwei Dateien gehen, dann genügt eine von beiden).
try:
    idx = open('index.md', encoding='utf-8').read()
    block = idx.split('## CSV-Themen und führende Dateien')[1].split('\n##')[0]
    zuord = {}
    for zeile in block.splitlines():
        if '=' not in zeile or zeile.strip().startswith('('):
            continue
        th, d = zeile.split('=', 1)
        zuord[th.strip().lstrip('-* ')] = [x.strip() for x in d.split(',') if x.strip()]
    inhalt = {}
    falsch, unbekannt = [], []
    for f in ('../msa/msa-katalog-basis.csv', '../msa/msa-katalog-kontext.csv'):  # Umbau 2026-09-19: Kataloge liegen in msa/
        for r in csv.DictReader(open(f, encoding='utf-8'), delimiter=';'):
            th = r['thema'].strip()
            if th not in zuord:
                unbekannt.append((r['id'], th)); continue
            for d in zuord[th]:
                if d not in inhalt:
                    inhalt[d] = open(d, encoding='utf-8').read() if os.path.exists(d) else ''
            if not any(r['id'] in inhalt[d] for d in zuord[th]):
                falsch.append((r['id'], th, '/'.join(zuord[th])))
    print(f'Kennzahl 6 – Originale nicht in der Datei ihres CSV-Themas: {len(falsch)} von {len(ids)}'
          f' (davon {len([f for f in falsch if f[0] in ohne])} in gar keinem Eintrag, siehe Kennzahl 5)')
    if unbekannt:
        print(f'   CSV-Thema ohne Zuordnung in index.md: {sorted(set(t for _, t in unbekannt))}')
    if '-v' in sys.argv:
        for i, th, d in falsch: print('   ', i, '–', th, '→', d)
except (FileNotFoundError, IndexError):
    print('Kennzahl 6 – Abschnitt „CSV-Themen und führende Dateien“ in index.md fehlt')
