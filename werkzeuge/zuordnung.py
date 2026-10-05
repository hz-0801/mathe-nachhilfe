#!/usr/bin/env python3
"""Zuordnung Prüfungsheft (P10) <-> Aufgabenbank, Zählung je Stufe, je Kapitel.

Verallgemeinerung von werkzeuge/prozent-zuordnung.py (Stand 2026-10-05);
die Ausgabe für Prozent ist byteidentisch mit der des alten Skripts.

Aufruf (aus der Wurzel von mathe-nachhilfe):
    python3 werkzeuge/zuordnung.py KAPITEL [--bank PFAD] [--aus DATEI] [--zeige]
    KAPITEL: prozent, lineare, quadratische, dreiecke, daten,
             wahrscheinlichkeit, koerper, flaechen, wachstum,
             gleichungssysteme (Kapitel aus msa/skript-zuschnitt-p10.csv)
Eingaben:
    --bank  Klon von hz-0801/aufgabenbank (Vorgabe ../aufgabenbank);
            gelesen werden bank/<eintrag>/e*.jsonl der Einträge des Kapitels
    msa/<kapitel>-zusatz.jsonl  Zusatzaufgaben für Stufen ohne Bank-Sprosse
            (Eintrag „<kapitel>-zusatz“, kette = Name der Stufe)
    Stufen, echte Teilaufgaben, Sprossen-Zuordnung und Kern-Urteil stehen
    als Daten in diesem Skript (KAPITEL; Muster (eintrag, sprosse,
    filter): filter None = alle Zeilen, Liste von Original-Kennungen,
    oder Liste von Varianten „v1“ …; viertes Glied 'inner' = die Sprosse
    ist innermathematisch, jede Zeile zählt; im Muster „(i)“).
Ausgabe: msa/zuordnung-<kapitel>.csv (oder --aus), Spalten
    stufe;kern;katalog_ids;bank_sprossen;anzahl_echt;anzahl_bank;ziel;fehlen;kern_grund
    anzahl_bank zählt Bank- und Zusatzaufgaben; ziel 12 bei Kern, sonst 6
    (Beschluss 05.10.); fehlen = max(0, ziel - echt - anzahl_bank).
    --zeige druckt je Stufe die gewählten und die nicht gezählten Zeilen.

Echte Teilaufgaben: die Kennungen der Stufe im Zuschnitt 2022–2026 (ids
und neben) und die Katalogzeilen 2014–2021 (msa-katalog-basis/-kontext),
deren typ oder typ_neben denselben Handgriff nennt (Urteil je Stufe,
Liste in den Daten).

Zählregel (Beschluss 05.10.: neu zählt nur, was der Schüler nicht durch
Erinnern lösen kann): Eine Sprosse ist zugeordnet, wenn sie denselben
Handgriff ohne Gerüst verlangt (kein Streifen, keine Vorform, kein
vorgegebener Teilschritt, keine „gemischt“-Sprosse, außer die Stufe ist
selbst die Mischung); Prüfungshöhe-Sprossen nur mit den Originalen der
Stufe ([...] im Muster). Innermathematische Aufgaben (Text ohne Zahlen und
Formeln kürzer als 40 Zeichen, oder Sprosse als innermathematisch
markiert, weil die Zahlen in Term oder Grafik stehen) zählen je Zeile. Eine Sachaufgabe zählt
nicht, wenn ihr Gerippe (Zahlen, Formeln, Prüfkennung und Ankreuzoptionen
entfernt) zu mindestens 70 % mit dem einer schon gezählten Aufgabe der
Stufe übereinstimmt (difflib.SequenceMatcher ratio >= 0.7) – „nur andere
Zahlen im selben Text“.
Nur Standardbibliothek.
"""
import argparse,collections,difflib,glob,json,os,re,sys
MN=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK=os.path.join(os.path.dirname(MN),'aufgabenbank')
KAPITEL={}
# ---- Daten je Kapitel (Stand 2026-10-05) ----
#@DATEN@
P='prozentrechnung';Z='zinsrechnung'
KAPITEL['prozent']=dict(eintraege=[P,Z],stufen=[
 ('Prozent und Anteil umwandeln',['2022-OS-B1f','2020-OS-B1a'],[(P,'e1-k1-s3',None),(P,'e1-k1-s6',None),(P,'e1-k1-s8',['2020-OS-B1a','2022-OS-B1f'])]),
 ('Prozentwert',['2026-FOR-B1a','2014-OS-B1a','2017-OS-B1b','2021-OS-B1c','2019-OS-K5a','2015-OS-K2a'],[(P,'e3-k1-s6',None),(P,'e3-k1-s7',None),(P,'e3-k1-s11',None),(P,'e3-k2-s1',None),(P,'e3-k3-s4',None)]),
 ('Prozentsatz',['2023-OS-K6a','2018-OS-K7a','2015-OS-K7c'],[(P,'e2-k3-s5',None),(P,'e2-k3-s6',None),(P,'e2-k3-s7',None),(P,'e2-k3-s9',None),(P,'e2-k5-s4',None)]),
 ('Grundwert',['2023-OS-B1b','2025-OS-B1a'],[(P,'e4-k2-s5',None),(P,'e4-k2-s6',None),(P,'e4-k2-s8',None),(P,'e4-k3-s4',None)]),
 ('Erhöhung und Veränderung in Prozent',['2024-OS-B1e','2022-OS-K4b','2026-FOR-K3c','2016-OS-K2c','2021-OS-K5a','2020-OS-K2d','2015-OS-K2b','2020-OS-K4c'],[(P,'e5-k2-s3',None),(P,'e5-k2-s4',None),(P,'e5-k2-s5',None),(P,'e5-k2-s6',None),(P,'e5-k2-s8',None),(P,'e5-k2-s9',['2026-FOR-K3c','2022-OS-K4b','2016-OS-K2c','2024-OS-B1e','2015-OS-K2b']),(P,'e5-k3-s4',None)]),
 ('Aussagen prüfen',['2023-OS-K6b','2025-OS-K4b','2017-OS-K2b','2019-OS-K5b'],[(P,'e1-k1-s8',['2023-OS-K6b','2019-OS-K5b','2017-OS-K2b','2021-OS-K5b']),(P,'e1-k3-s4',None),(P,'e5-k2-s7',None),(P,'e5-k2-s9',['2025-OS-K4b'])]),
 ('Prozent aus einer berechneten Fläche',['2023-OS-K5c'],[]),
 ('Zinsen und Zinssatz',['2014-OS-B1e','2014-OS-K3a','2015-OS-B1e'],[(Z,'e1-k1-s1',None),(Z,'e1-k1-s4',None),(Z,'e1-k1-s5',None),(Z,'e1-k1-s6',None),(Z,'e1-k1-s7',None),(Z,'e1-k1-s12',None)]),
 ('Zinseszins und Guthabentabelle',['2014-OS-K3b','2014-OS-K3c'],[(Z,'e2-k1-s4',None),(Z,'e2-k1-s6',None),(Z,'e2-k1-s11',None),(Z,'e2-k2-s1',None),(Z,'e2-k4-s3',None)]),
],kern={
 'Prozent und Anteil umwandeln':('ja','Basisteil 2020 und 2022 (Niveau I), Bank-Einheit 1 mit Grundfall, Grundlage aller Prozentaufgaben'),
 'Prozentwert':('ja','6 echte Teilaufgaben 2014–2026, fast jedes Jahr im Basisteil (Niveau I), Bank-Einheit 3 mit Grundfall'),
 'Prozentsatz':('ja','3 echte (2015, 2018, 2023, Niveau I/II), Bank-Einheit 2 mit Grundfall, trägt Aussagen prüfen und Diagramme'),
 'Grundwert':('ja','Basisteil 2023 und 2025 (Niveau I), Bank-Einheit 4 mit Grundfall'),
 'Erhöhung und Veränderung in Prozent':('ja','8 echte, die meisten der Prüfung (Niveau I/II), Bank-Einheit 5 mit Grundfall'),
 'Aussagen prüfen':('nein','4 echte, aber Niveau II und nur als Prüfungshöhe auf Prozentsatz gesetzt (keine eigene Kette mit Grundfall)'),
 'Prozent aus einer berechneten Fläche':('nein','1 echte (2023, Sternchen, Niveau III), Nebenthema aus der Geometrie'),
 'Zinsen und Zinssatz':('nein','3 echte, zuletzt 2015, seit 2016 nicht geprüft, Zuschnitt 2022–2026 führt keine Zins-Stufe'),
 'Zinseszins und Guthabentabelle':('nein','2 echte, nur 2014 (Niveau II)'),
})
L='lineare-funktionen';Q='quadratische-funktionen'
KAPITEL['lineare']=dict(eintraege=[L,Q],stufen=[
 ('erkennen und ablesen',['2025-OS-B1f','2024-OS-B1i','2016-OS-B1c','2019-OS-K2a','2019-OS-K2b','2019-OS-K2c'],[(L,'e2-k5-s1',None,'inner'),(L,'e2-k5-s2',None,'inner'),(L,'e2-k5-s3',None,'inner'),(L,'e2-k5-s4',None,'inner'),(L,'e2-k5-s5',None,'inner'),(L,'e2-k5-s6',None,'inner')]),
 ('aus Gleichung zeichnen',['2024-OS-K3a','2026-FOR-K5a','2022-OS-K3a','2021-OS-K2a'],[(L,'e2-k4-s5',None,'inner'),(L,'e2-k4-s6',None,'inner'),(L,'e2-k4-s7',None,'inner'),(L,'e2-k4-s8',None,'inner')]),
 ('durch zwei Punkte, Gleichung ablesen',['2025-OS-K5a','2017-OS-K5a','2015-OS-K4d'],[(L,'e4-k2-s1',None,'inner'),(L,'e4-k1-s3',None,'inner'),(L,'e4-k1-s4',None,'inner'),(L,'e4-k1-s5',None,'inner'),(L,'e4-k1-s6',['v1','v2','v5','v6'],'inner'),(L,'e4-k1-s6',['v3','v4']),(L,'e4-k4-s4',None)]),
 ('zeichnen und Aussagen prüfen',['2023-OS-K4a','2021-OS-K2b'],[(L,'e2-k6-s1',None,'inner'),(L,'e2-k7-s2',None,'inner'),(L,'e4-k4-s2',None,'inner'),(L,'e3-k2-s7',['2023-OS-K4a','2021-OS-K2b'])]),
 ('ankreuzen',['2023-OS-B1i'],[(L,'e3-k2-s5',None,'inner'),(L,'e3-k2-s7',['2023-OS-B1i'])]),
 ('rechnerisch an Gerade und Parabel',['2026-FOR-K5b','2024-OS-K3c','2017-OS-K5b'],[(L,'e3-k2-s7',['2026-FOR-K5b','2017-OS-K5b','2019-OS-K2a','2021-OS-K6d','2022-OS-K3a']),(Q,'e1-k1-s4',None),(Q,'e3-k1-s2',None),(Q,'e4-k1-s14',None)]),
 ('Endwert berechnen',['2022-OS-K6a','2021-OS-K6a'],[(L,'e5-k1-s3',None),(L,'e5-k4-s4',None),(L,'e5-k1-s5',['2022-OS-K6a','2021-OS-K6a'])]),
 ('Graph zum Tarif zuordnen',['2023-OS-K3a','2016-OS-K6a'],[(L,'e5-k2-s1',None),(L,'e5-k1-s5',['2023-OS-K3a','2016-OS-K6a'])]),
 ('Gleichung aufstellen und rückwärts rechnen',['2022-OS-K6b','2016-OS-K6c','2021-OS-K6c','2021-OS-K6d','2021-OS-K7a'],[(L,'e5-k1-s1',None),(L,'e5-k1-s2',None),(L,'e5-k3-s1',None),(L,'e5-k4-s1',None),(L,'e1-k1-s8',None),(L,'e5-k1-s5',['2022-OS-K6b','2016-OS-K6c','2021-OS-K7a'])]),
 ('Tarife vergleichen',['2023-OS-K3b','2016-OS-K6b'],[(L,'e5-k1-s4',None),(L,'e5-k4-s2',None),(L,'e5-k1-s5',['2023-OS-K3b','2016-OS-K6b'])]),
],kern={
 'erkennen und ablesen':('ja','6 echte 2016–2025, Basisteil 2016, 2024, 2025 (Niveau I), Bank-Kette Ablesen mit Grundfall'),
 'aus Gleichung zeichnen':('ja','4 echte (2021, 2022, 2024, 2026), fast jedes Jahr Einstieg der Funktionsaufgabe, Bank-Kette Graph zeichnen mit Grundfall'),
 'durch zwei Punkte, Gleichung ablesen':('ja','3 echte (2015, 2017, 2025), Bank-Kette Gleichung bestimmen mit Grundfall'),
 'zeichnen und Aussagen prüfen':('nein','2 echte (2021, 2023), Aussagen zu Eigenschaften nur als Zusatz zum Zeichnen, keine eigene Kette mit Grundfall'),
 'ankreuzen':('nein','1 echte (Basisteil 2023), Punktprobe ist Kern der rechnerischen Stufe'),
 'rechnerisch an Gerade und Parabel':('ja','3 echte (2017, 2024, 2026), Bank-Kette Funktionswert mit Grundfall, Punktprobe trägt auch Quadratische'),
 'Endwert berechnen':('nein','2 echte (2021, 2022), Teilschritt der Sachkette, Grundfall der Kette ist das Aufstellen'),
 'Graph zum Tarif zuordnen':('nein','2 echte (2016, 2023), nur Zuordnen, keine eigene Kette mit Grundfall'),
 'Gleichung aufstellen und rückwärts rechnen':('ja','5 echte (2016, 2021 dreimal, 2022), Bank-Kette Anwendung mit Grundfall (Gleichung ankreuzen)'),
 'Tarife vergleichen':('nein','2 echte (2016, 2023), Niveau II, als Prüfungshöhe auf die Anwendungskette gesetzt'),
})
# ---- Ende Daten ----

def gerippe(t):
  t=re.sub(r'\(P10[^)]*\)','',t)
  t=re.sub(r'\$[^$]*\$','#',t)
  t=re.sub(r'\d[\d\\,.{}]*','#',t)
  t=re.sub(r'\\kreuz\{[^}]*\}','',t)
  return re.sub(r'\s+',' ',t).strip()[:120]
def innermath(t):
  g=gerippe(t)
  return len(re.sub(r'[#\\{}()%€\s.,:;?]','',g))<40
def lade(kap,K):
  A=[]
  for e in K['eintraege']:
    for f in sorted(glob.glob(os.path.join(BANK,'bank',e,'e*.jsonl'))):
      for l in open(f): A.append(json.loads(l))
  zus=os.path.join(MN,'msa',kap+'-zusatz.jsonl')
  try:
    for l in open(zus): A.append(json.loads(l))
  except FileNotFoundError: pass
  return A
def gleich(a,b):
  return difflib.SequenceMatcher(None,gerippe(a),gerippe(b)).ratio()>=0.7
def passt(d,e,pre,orig,*_):
  if d['eintrag']!=e or not d['id'].startswith(e+'-'+pre+'-v'): return False
  if orig is None: return True
  oid=(d.get('original') or {}).get('id')
  vs=[o for o in orig if o.startswith('v')]
  if vs: return ('v'+d['id'].rsplit('-v',1)[1]) in vs
  return oid in orig
def zaehle2(kap,K,A,zeige=False):
  out=[]
  for name,echt,maps in K['stufen']:
    sel=[]
    inn=set()
    for m in maps:
      for d in A:
        if passt(d,*m) and d not in sel:
          sel.append(d)
          if len(m)>3 and m[3]=='inner': inn.add(d['id'])
    sel+=[d for d in A if d['eintrag']==kap+'-zusatz' and d['kette']==name]
    inn|={d['id'] for d in sel if d.get('innermath')}
    reps=[];n=0;art=collections.Counter()
    if zeige: print('##',name)
    for d in sel:
      if d['id'] in inn or innermath(d['aufgabe']):
        n+=1; art['inner']+=1
        if zeige: print('   inner:',d['id'])
        continue
      if any(gleich(d['aufgabe'],r['aufgabe']) for r in reps):
        if zeige: print('   gleich:',d['id'])
        continue
      reps.append(d);n+=1;art['sach']+=1
      if zeige: print('   sach:',d['id'])
    out.append((name,echt,len(sel),n,art))
  return out
def muster(maps):
  t=[]
  for m in maps:
    e,pre,orig=m[:3]
    s=f'{e}-{pre}'
    if orig: s+='['+','.join(orig)+']'
    if len(m)>3 and m[3]=='inner': s+='(i)'
    t.append(s)
  return ' '.join(t)
def main(kap,pfad,zeige=False):
  K=KAPITEL[kap]
  A=lade(kap,K);res=zaehle2(kap,K,A,zeige)
  zl=['stufe;kern;katalog_ids;bank_sprossen;anzahl_echt;anzahl_bank;ziel;fehlen;kern_grund']
  for (name,echt,maps),(n2,e2,roh,n,art) in zip(K['stufen'],res):
    k,g=K['kern'][name];ziel=12 if k=='ja' else 6
    zus=sum(1 for d in A if d['eintrag']==kap+'-zusatz' and d['kette']==name)
    bs=(muster(maps)+(f' msa/{kap}-zusatz.jsonl({zus})' if zus else '')).strip()
    zl.append(f'{name};{k};{" ".join(echt)};{bs or "–"};{len(echt)};{n};{ziel};{max(0,ziel-len(echt)-n)};{g}')
  open(pfad,'w',encoding='utf-8').write('\n'.join(zl)+'\n')
  if zeige: print('\n'.join(zl))

if __name__=='__main__':
  ap=argparse.ArgumentParser()
  ap.add_argument('kapitel',choices=sorted(KAPITEL))
  ap.add_argument('--bank',default=BANK)
  ap.add_argument('--aus')
  ap.add_argument('--zeige',action='store_true')
  a=ap.parse_args();BANK=a.bank
  main(a.kapitel,a.aus or os.path.join(MN,'msa',f'zuordnung-{a.kapitel}.csv'),a.zeige)
