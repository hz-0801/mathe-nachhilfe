#!/usr/bin/env python3
"""Strukturprüfung aller Katalogeinträge (seit 09e, Maßnahme b der Opus-Arbeitsweise):
1. Sind alle Pflichtabschnitte vorhanden?
2. Trägt jeder Eintrag eine Zeile „Zuordnung:“ am Zeilenanfang (seit 10d)? Ohne sie läuft die
   P10-Typenprüfung von _pruef_katalog.py --thema nicht; drei Einträge hatten sie über einen Monat nicht.
3. Trägt jede Sprossenkette „(Einheit n)“ (seit 10d) und endet sie mit „Prüfungshöhe“?
4. Existiert jede genannte Original-id in katalog-basis.csv oder katalog-kontext.csv (msa) bzw. in
   fhr-katalog.csv, abi-katalog.csv oder iqb-katalog.csv (Sek II, seit Auftrag Sek-II-Werkzeuge)?
5. Kennzahl 5 (seit 10h): die Gegenrichtung – wie viele Originale der Kataloge stehen in keinem
   Eintrag? Das ist bewusst eine Kennzahl und kein Befund: sie sinkt mit jedem Gegenlese-Block
   und soll den einen gewollt sichtbaren Befund nicht zudecken. Bis 10g fiel diese Lücke nur von Hand
   auf (2021-OS-K6b am 10g, 2023-OS-K5c und 2024-OS-B1c am 10h). Zählt seit Auftrag Sek-II-Werkzeuge
   auch fhr-, abi- und iqb-Originale.
6. Kennzahl 7 (seit Auftrag Tragfähigkeit, 21.09.2026): Einträge, deren Abschnitt „Voraussetzungen
   (Blatt 0)“ keinen Verweis der Form <name>.md auf einen anderen Eintrag trägt (oder den Abschnitt
   nicht hat). Das ist bewusst nicht die Rangliste der Tragfähigkeit – die steht in _tragfaehigkeit.md
   (werkzeuge/tragfaehigkeit.py) –, sondern das Loch in ihrer Messung: was diese Einträge voraussetzen,
   zählt dort nicht. Die Zählregel wird von dort importiert, damit beide Zahlen dieselbe sind.
7. Kennzahl 8 (seit Auftrag Verweis- und Namensprüfung, 21.09.2026): die zwei harten Befunde der
   Verweisprüfung – Verweise <name>.md auf Dateien, die es im Repo nicht gibt, und Einheitsnummern hinter
   einem Verweis, die größer sind als die Zahl der Lerneinheiten der Zieldatei. Die vollständige Prüfung
   (fünf Teile, auch Namensgleichheit, Gegenrichtung und Formlücke) steht in _verweise.md
   (werkzeuge/verweis-pruef.py); hier nur, was auf null gehört. Die Zählregel wird importiert.
Aufruf im Ordner katalog/: python3 _pruef_struktur.py – die CSVs werden eine Ebene darüber erwartet.
Aufgabenstämme ohne Teilaufgabenbuchstaben (2017-OS-K7; bei iqb eine Kennung, deren Aufgabe
Teilaufgaben hat) werden nicht geprüft.
"""
import re,sys,csv,glob,os
ids=set()
for f in ('../msa/msa-katalog-basis.csv','../msa/msa-katalog-kontext.csv'):  # Umbau 2026-09-19: Kataloge liegen in msa/
    for r in csv.DictReader(open(f,encoding='utf-8'),delimiter=';'): ids.add(r['id'])
for f in ('../fhr/fhr-katalog.csv','../abitur/abi-katalog.csv','../abitur/iqb-katalog.csv'):  # Sek II (seit Auftrag Sek-II-Werkzeuge)
    for r in csv.DictReader(open(f,encoding='utf-8'),delimiter=';'): ids.add(r['id'])
# Sek-II-id-Muster (Auftrag Sek-II-Werkzeuge), empirisch aus den drei CSVs oben abgeglichen (0 Abweichungen):
# fhr Jahr-Papier-AufgabeTeilaufgabe (fhr.md § 4), abi Jahr-Land-Niveau-BlockAufgabe[.Unteraufgabe]Teilaufgabe
# (abi.md § 4), iqb Kennung[-Teilaufgabe] mit Kennung = Jahr|Beispielaufgaben, M, Niveau, Teil, Sachgebiet,
# in Teil A Aufgabengruppe[Nummer], in Teil B Hilfsmittel[Dateinummer]-Aufgabennummer (iqb.md § 4).
ID_SEK2=(r"\d{4}-[ABC]-\d+[a-z]"
    r"|\d{4}-(?:be|bb|bebb)-(?:gk|ea|lk)-[AB]\d+(?:\.\d+)?[a-z]"
    r"|(?:\d{4}|Beispielaufgaben)M(?:grundlegend|erhoeht)A(?:AGLAA[12]?|Analysis|Stochastik)\d{1,3}(?:-[a-z])?"
    r"|(?:\d{4}|Beispielaufgaben)M(?:grundlegend|erhoeht)B(?:AGLAA[12]?|Analysis|Stochastik)(?:WTR|CAS|MMS)\d{0,2}-\d{1,2}[a-z]?")
ID_MUSTER=re.compile(r"\b(?:20\d\d-(?:OS|FOR)-[BK]\d+[a-z]|"+ID_SEK2+r")\b")
ABS=["### Verortung","### Lerneinheiten","### Typen je Lerneinheit","### Voraussetzungen (Blatt 0)","### Merkkasten","### Typische Fehler","### Für schwache Schüler","### Prüfungsform","### Offene Punkte des Eintrags","## Prüfliste"]
bad=0
for p in sorted(glob.glob('*.md')):
    if p.startswith('_') or p=='index.md': continue
    t=open(p,encoding='utf-8').read()
    miss=[a for a in ABS if a not in t]
    if miss: print(p,'FEHLENDE ABSCHNITTE:',miss); bad+=1
    zeile=re.search(r"^Zuordnung: ?(\S.*)$",t,re.M)
    ist_sek2='### Prüfungsform (fhr / abi / iqb)' in t
    if not zeile:
        # Sek-II (konzept.md § 4 Entscheidung 36): kein eigener Zuordnungs-Absatz mehr - die
        # Einheitenzuordnung steht in der Klammer hinter jeder Typnennung der Profillisten
        # und wird dort von _pruef_katalog.py (Sek-II-Modus) geprüft.
        if not ist_sek2:
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
    for m in set(ID_MUSTER.findall(t)):
        # iqb: eine Kennung ohne Teilaufgabenbuchstaben ist entweder selbst ein vollständiges id
        # (Aufgabe ohne Gliederung) oder ein Stammverweis auf eine Aufgabe mit Teilaufgaben - wie
        # bei msa (Docstring oben) wird der reine Stammverweis nicht geprüft.
        if m not in ids and not any(i.startswith(m+'-') for i in ids):
            print(p,'UNBEKANNTE ID:',m); bad+=1
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

    # Sek II (seit Auftrag Sek-II-Werkzeuge): CSV-Thema -> Datei steht bereits in themen.csv
    # (Spalten kanonisch/profil/thema), eine eigene Zuordnung wie oben für msa ist unnötig.
    zuord2 = {}
    for r in csv.DictReader(open('../themen.csv', encoding='utf-8'), delimiter=';'):
        if r['profil'] not in ('fhr', 'abi', 'iqb'): continue
        zuord2.setdefault((r['profil'], r['thema'].strip()), []).append(r['kanonisch'].strip() + '.md')
    for profil, pfad in (('fhr', '../fhr/fhr-katalog.csv'), ('abi', '../abitur/abi-katalog.csv'), ('iqb', '../abitur/iqb-katalog.csv')):
        for r in csv.DictReader(open(pfad, encoding='utf-8'), delimiter=';'):
            th = r['thema'].strip()
            key = (profil, th)
            if key not in zuord2:
                unbekannt.append((r['id'], th)); continue
            for d in zuord2[key]:
                if d not in inhalt:
                    inhalt[d] = open(d, encoding='utf-8').read() if os.path.exists(d) else ''
            if not any(r['id'] in inhalt[d] for d in zuord2[key]):
                falsch.append((r['id'], th, '/'.join(zuord2[key])))

    print(f'Kennzahl 6 – Originale nicht in der Datei ihres CSV-Themas: {len(falsch)} von {len(ids)}'
          f' (davon {len([f for f in falsch if f[0] in ohne])} in gar keinem Eintrag, siehe Kennzahl 5)')
    if unbekannt:
        print(f'   CSV-Thema ohne Zuordnung in index.md/themen.csv: {sorted(set(t for _, t in unbekannt))}')
    if '-v' in sys.argv:
        for i, th, d in falsch: print('   ', i, '–', th, '→', d)
except (FileNotFoundError, IndexError):
    print('Kennzahl 6 – Abschnitt „CSV-Themen und führende Dateien“ in index.md fehlt')

# --- Kennzahl 7 (seit Auftrag Tragfähigkeit, 21.09.2026): Einträge ohne Verweis in Blatt 0.
# werkzeuge/tragfaehigkeit.py zählt je Eintrag die Verweise <name>.md im Abschnitt „Voraussetzungen
# (Blatt 0)“ und schreibt daraus die Rangliste _tragfaehigkeit.md. Ein Eintrag ohne solchen Verweis
# (Sek-I-Form „[Thema Lineare Gleichungen, Einheit 2]“ oder gar keine Nennung) stellt dort keine
# Nachfrage – die Rangliste bildet insoweit die eigene Schreibsorgfalt ab, nicht den Unterricht. Die
# Kennzahl misst dieses Loch; sie wird mit derselben Zählregel erhoben (Import), nicht nachgebaut.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'werkzeuge'))
try:
    import tragfaehigkeit
    mess = tragfaehigkeit.messe('.')
    ohne7 = sorted(mess['ohne_verweis'] + mess['ohne_abschnitt'])
    print(f'Kennzahl 7 – Einträge ohne Verweis in Blatt 0: {len(ohne7)} von {len(mess["eintraege"])}')
    if '-v' in sys.argv:
        for p in ohne7: print('   ', p + '.md')
except ImportError:
    print('Kennzahl 7 – werkzeuge/tragfaehigkeit.py fehlt')

# --- Kennzahl 8 (seit Auftrag Verweis- und Namensprüfung, 21.09.2026): harte Verweisbefunde.
# werkzeuge/verweis-pruef.py prüft jeden Verweis <name>.md in jedem Abschnitt jedes Eintrags (hat das Ziel
# eine Datei?) und jede Einheitenangabe direkt hinter einem Verweis (hat die Zieldatei so viele Lerneinheiten?)
# und schreibt daraus _verweise.md (dort auch Namensgleichheit, Gegenrichtung, Formlücke). Die Kennzahl zählt
# nur die zwei Befunde, die kein Ermessen sind und auf null gehören; sie wird mit derselben Zählregel erhoben
# (Import über den Dateipfad, weil der Skriptname einen Bindestrich trägt), nicht nachgebaut.
try:
    import importlib.util
    _spec = importlib.util.spec_from_file_location(
        'verweis_pruef', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'werkzeuge', 'verweis-pruef.py'))
    verweis_pruef = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(verweis_pruef)
    mv = verweis_pruef.messe()
    fehlend = [f for f in mv['p1']['funde'] if f['gruppe'] == 'c']
    zu_gross = [z for z in mv['p2']['zugeordnet'] if z['zu_gross']]
    print(f'Kennzahl 8 – Verweisbefunde: {len(fehlend)} Verweise auf Dateien, die es nicht gibt '
          f'({len(set(f["verweis"] for f in fehlend))} Namen), {len(zu_gross)} Einheitsnummern größer als vorhanden')
    if '-v' in sys.argv:
        for f in fehlend: print('   ', f['verweis'], '←', f['quelle'] + '.md', f'({f["abschnitt"]}, Zeile {f["zeile"]})')
        for z in zu_gross: print('   ', z['verweis'], z['angabe'], '←', z['quelle'] + '.md', f'({z["abschnitt"]}, Zeile {z["zeile"]}), {z["vorhanden"]} vorhanden')
except (ImportError, FileNotFoundError, AttributeError):
    print('Kennzahl 8 – werkzeuge/verweis-pruef.py fehlt')
