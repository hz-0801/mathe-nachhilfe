#!/usr/bin/env python3
"""Zuordnung Prüfungsheft Prozent (P10) <-> Aufgabenbank, Zählung je Stufe.

Aufruf (aus der Wurzel von mathe-nachhilfe):
    python3 werkzeuge/prozent-zuordnung.py [--bank PFAD] [--aus DATEI]
Eingaben:
    --bank  Klon von hz-0801/aufgabenbank (Vorgabe ../aufgabenbank);
            gelesen werden bank/prozentrechnung/e*.jsonl und
            bank/zinsrechnung/e*.jsonl
    msa/prozent-zusatz.jsonl  Zusatzaufgaben für Stufen ohne Bank-Sprosse
            (Eintrag „prozent-zusatz“, kette = Name der Stufe)
    Stufen, echte Teilaufgaben, Sprossen-Zuordnung und Kern-Urteil stehen
    als Daten in diesem Skript (STUFEN, KERN; Stand 2026-10-05).
Ausgabe: msa/zuordnung-prozent.csv (oder --aus), Spalten
    stufe;kern;katalog_ids;bank_sprossen;anzahl_echt;anzahl_bank;ziel;fehlen;kern_grund
    anzahl_bank zählt Bank- und Zusatzaufgaben; ziel 12 bei Kern, sonst 6
    (Beschluss 05.10.); fehlen = max(0, ziel - echt - anzahl_bank).

Zählregel (Beschluss 05.10.: neu zählt nur, was der Schüler nicht durch
Erinnern lösen kann): Eine Sprosse ist zugeordnet, wenn sie denselben
Handgriff ohne Gerüst verlangt (kein Streifen, keine Vorform, kein
vorgegebener Teilschritt, keine „gemischt“-Sprosse); Prüfungshöhe-Sprossen
nur mit den Originalen der Stufe ([...] im Muster). Innermathematische
Aufgaben (Text ohne Zahlen und Formeln kürzer als 40 Zeichen) zählen je
Zeile. Eine Sachaufgabe zählt nicht, wenn ihr Gerippe (Zahlen, Formeln,
Prüfkennung und Ankreuzoptionen entfernt) zu mindestens 70 % mit dem einer
schon gezählten Aufgabe der Stufe übereinstimmt (difflib.SequenceMatcher
ratio >= 0.7) – „nur andere Zahlen im selben Text“.
Nur Standardbibliothek.
"""
import argparse,collections,difflib,glob,json,os,re,sys
MN=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK=os.path.join(os.path.dirname(MN),'aufgabenbank')
P='prozentrechnung';Z='zinsrechnung'
STUFEN=[
 ('Prozent und Anteil umwandeln',['2022-OS-B1f','2020-OS-B1a'],[(P,'e1-k1-s3',None),(P,'e1-k1-s6',None),(P,'e1-k1-s8',['2020-OS-B1a','2022-OS-B1f'])]),
 ('Prozentwert',['2026-FOR-B1a','2014-OS-B1a','2017-OS-B1b','2021-OS-B1c','2019-OS-K5a','2015-OS-K2a'],[(P,'e3-k1-s6',None),(P,'e3-k1-s7',None),(P,'e3-k1-s11',None),(P,'e3-k2-s1',None),(P,'e3-k3-s4',None)]),
 ('Prozentsatz',['2023-OS-K6a','2018-OS-K7a','2015-OS-K7c'],[(P,'e2-k3-s5',None),(P,'e2-k3-s6',None),(P,'e2-k3-s7',None),(P,'e2-k3-s9',None),(P,'e2-k5-s4',None)]),
 ('Grundwert',['2023-OS-B1b','2025-OS-B1a'],[(P,'e4-k2-s5',None),(P,'e4-k2-s6',None),(P,'e4-k2-s8',None),(P,'e4-k3-s4',None)]),
 ('Erhöhung und Veränderung in Prozent',['2024-OS-B1e','2022-OS-K4b','2026-FOR-K3c','2016-OS-K2c','2021-OS-K5a','2020-OS-K2d','2015-OS-K2b','2020-OS-K4c'],[(P,'e5-k2-s3',None),(P,'e5-k2-s4',None),(P,'e5-k2-s5',None),(P,'e5-k2-s6',None),(P,'e5-k2-s8',None),(P,'e5-k2-s9',['2026-FOR-K3c','2022-OS-K4b','2016-OS-K2c','2024-OS-B1e','2015-OS-K2b']),(P,'e5-k3-s4',None)]),
 ('Aussagen prüfen',['2023-OS-K6b','2025-OS-K4b','2017-OS-K2b','2019-OS-K5b'],[(P,'e1-k1-s8',['2023-OS-K6b','2019-OS-K5b','2017-OS-K2b','2021-OS-K5b']),(P,'e1-k3-s4',None),(P,'e5-k2-s7',None),(P,'e5-k2-s9',['2025-OS-K4b'])]),
 ('Prozent aus einer berechneten Fläche',['2023-OS-K5c'],[]),
 ('Zinsen und Zinssatz',['2014-OS-B1e','2014-OS-K3a','2015-OS-B1e'],[(Z,'e1-k1-s1',None),(Z,'e1-k1-s4',None),(Z,'e1-k1-s5',None),(Z,'e1-k1-s6',None),(Z,'e1-k1-s7',None),(Z,'e1-k1-s12',None)]),
 ('Zinseszins und Guthabentabelle',['2014-OS-K3b','2014-OS-K3c'],[(Z,'e2-k1-s4',None),(Z,'e2-k1-s6',None),(Z,'e2-k1-s11',None),(Z,'e2-k2-s1',None),(Z,'e2-k4-s3',None)]),
]
def gerippe(t):
  t=re.sub(r'\(P10[^)]*\)','',t)
  t=re.sub(r'\$[^$]*\$','#',t)
  t=re.sub(r'\d[\d\\,.{}]*','#',t)
  t=re.sub(r'\\kreuz\{[^}]*\}','',t)
  return re.sub(r'\s+',' ',t).strip()[:120]
def innermath(t):
  g=gerippe(t)
  return len(re.sub(r'[#\\{}()%€\s.,:;?]','',g))<40
def lade():
  A=[]
  for e in (P,Z):
    for f in sorted(glob.glob(os.path.join(BANK,'bank',e,'e*.jsonl'))):
      for l in open(f): A.append(json.loads(l))
  zus=os.path.join(MN,'msa','prozent-zusatz.jsonl')
  try:
    for l in open(zus): A.append(json.loads(l))
  except FileNotFoundError: pass
  return A
def gleich(a,b):
  return difflib.SequenceMatcher(None,gerippe(a),gerippe(b)).ratio()>=0.7
def zaehle2(A,zeige=False):
  out=[]
  for name,echt,maps in STUFEN:
    sel=[]
    for e,pre,orig in maps:
      for d in A:
        if d['eintrag']==e and d['id'].startswith(e+'-'+pre+'-v') and (orig is None or (d.get('original') or {}).get('id') in orig):
          sel.append(d)
    sel+=[d for d in A if d['eintrag']=='prozent-zusatz' and d['kette']==name]
    reps=[];n=0;art=collections.Counter()
    for d in sel:
      if innermath(d['aufgabe']): n+=1; art['inner']+=1; continue
      if any(gleich(d['aufgabe'],r['aufgabe']) for r in reps):
        if zeige: print('   gleich:',d['id'])
        continue
      reps.append(d);n+=1;art['sach']+=1
    out.append((name,echt,len(sel),n,art))
  return out
KERN={
 'Prozent und Anteil umwandeln':('ja','Basisteil 2020 und 2022 (Niveau I), Bank-Einheit 1 mit Grundfall, Grundlage aller Prozentaufgaben'),
 'Prozentwert':('ja','6 echte Teilaufgaben 2014–2026, fast jedes Jahr im Basisteil (Niveau I), Bank-Einheit 3 mit Grundfall'),
 'Prozentsatz':('ja','3 echte (2015, 2018, 2023, Niveau I/II), Bank-Einheit 2 mit Grundfall, trägt Aussagen prüfen und Diagramme'),
 'Grundwert':('ja','Basisteil 2023 und 2025 (Niveau I), Bank-Einheit 4 mit Grundfall'),
 'Erhöhung und Veränderung in Prozent':('ja','8 echte, die meisten der Prüfung (Niveau I/II), Bank-Einheit 5 mit Grundfall'),
 'Aussagen prüfen':('nein','4 echte, aber Niveau II und nur als Prüfungshöhe auf Prozentsatz gesetzt (keine eigene Kette mit Grundfall)'),
 'Prozent aus einer berechneten Fläche':('nein','1 echte (2023, Sternchen, Niveau III), Nebenthema aus der Geometrie'),
 'Zinsen und Zinssatz':('nein','3 echte, zuletzt 2015, seit 2016 nicht geprüft, Zuschnitt 2022–2026 führt keine Zins-Stufe'),
 'Zinseszins und Guthabentabelle':('nein','2 echte, nur 2014 (Niveau II)'),
}
def muster(maps):
  t=[]
  for e,pre,orig in maps:
    s=f'{e}-{pre}'
    if orig: s+='['+','.join(orig)+']'
    t.append(s)
  return ' '.join(t)
def main(pfad):
  A=lade();res=zaehle2(A)
  zl=['stufe;kern;katalog_ids;bank_sprossen;anzahl_echt;anzahl_bank;ziel;fehlen;kern_grund']
  for (name,echt,maps),(n2,e2,roh,n,art) in zip(STUFEN,res):
    k,g=KERN[name];ziel=12 if k=='ja' else 6
    zus=sum(1 for d in A if d['eintrag']=='prozent-zusatz' and d['kette']==name)
    bs=(muster(maps)+(f' msa/prozent-zusatz.jsonl({zus})' if zus else '')).strip()
    zl.append(f'{name};{k};{" ".join(echt)};{bs or "–"};{len(echt)};{n};{ziel};{max(0,ziel-len(echt)-n)};{g}')
  open(pfad,'w',encoding='utf-8').write('\n'.join(zl)+'\n')

if __name__=='__main__':
  ap=argparse.ArgumentParser()
  ap.add_argument('--bank',default=BANK)
  ap.add_argument('--aus',default=os.path.join(MN,'msa','zuordnung-prozent.csv'))
  a=ap.parse_args();BANK=a.bank
  main(a.aus)
