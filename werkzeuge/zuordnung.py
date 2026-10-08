#!/usr/bin/env python3
"""Zuordnung Prüfungsheft (P10, Abitur GK) <-> Aufgabenbank, Zählung je Stufe, je Kapitel.

Verallgemeinerung von werkzeuge/prozent-zuordnung.py (Stand 2026-10-05);
die Ausgabe für Prozent ist byteidentisch mit der des alten Skripts.
v2 (08.10.2026, Entscheidung A): die Stufendaten (Stufen, Originale, Bank-Muster,
Kern-Urteil, Verwechselbar) und die Plätze der Originale stehen nicht mehr im
Skript, sondern in der Prüfungsgliederung msa/gliederung/<kapitel>.md bzw.
abitur/gliederung/<kapitel>.md (Format msa/gliederung/README.md, Leser
werkzeuge/gliederung.py); die Ausgabe ist mit v1 (a1c9fd3) byteidentisch.

Aufruf (aus der Wurzel von mathe-nachhilfe):
    python3 werkzeuge/zuordnung.py KAPITEL [--bank PFAD] [--aus DATEI] [--zeige]
    python3 werkzeuge/zuordnung.py KAPITEL --nur-spalten   (nur Zusatzspalten, s. u.)
    KAPITEL: kurvenuntersuchung, ableitung-tangente, integral, punkte-flaechen-koerper, winkel-abstaende, geraden-ebenen, baum-bedingte-wahrscheinlichkeit, binomialverteilung, erwartungswert (Abitur GK,
             Ausgabe abitur/), prozent, lineare, quadratische, dreiecke, daten,
             wahrscheinlichkeit, koerper, flaechen, wachstum,
             gleichungssysteme (Kapitel aus msa/skript-zuschnitt-p10.csv)
Eingaben:
    --bank  Klon von hz-0801/aufgabenbank (Vorgabe ../aufgabenbank);
            gelesen werden bank/<eintrag>/e*.jsonl der Einträge des Kapitels
    msa/<kapitel>-zusatz.jsonl  Zusatzaufgaben für Stufen ohne Bank-Sprosse
            (Eintrag „<kapitel>-zusatz“, kette = Name der Stufe)
    Stufen, echte Teilaufgaben, Sprossen-Zuordnung und Kern-Urteil stehen
    in der Gliederungsdatei des Kapitels (Feld Bank: Muster (eintrag, sprosse,
    filter): filter None = alle Zeilen, Liste von Original-Kennungen,
    oder Liste von Varianten „v1“ …; viertes Glied 'inner' = die Sprosse
    ist innermathematisch, jede Zeile zählt; im Muster „(i)“).
Ausgabe: msa/zuordnung-<kapitel>.csv (oder --aus), Spalten
    stufe;kern;katalog_ids;bank_sprossen;anzahl_echt;anzahl_bank;ziel;fehlen;kern_grund
    anzahl_bank zählt Bank- und Zusatzaufgaben; ziel 12 bei Kern, sonst 6
    (Beschluss 05.10.); fehlen = max(0, ziel - echt - anzahl_bank).
    --zeige druckt je Stufe die gewählten und die nicht gezählten Zeilen.

Zusatzspalten (Auftrag K, 06.10.; Beschlüsse N2.6, N2.7, N4.19 in
aufgabenbank/bau/pruefheft/beschluesse-2026-10-06b.md), nur P10:
    jahre_letzte5  Zählung B: Zahl der Jahre 2022–2026, in denen der
                   Handgriff gebraucht wurde (Hauptplatz, ganz_auch oder
                   Zwischenschritt in den Tabellen „Plätze der Originale“
                   der Gliederung = msa/handgriffe-p10.csv; nur OS, EBR,
                   FOR, nicht GYM); dahinter in Klammern die Jahre
    nebenplaetze   Teilaufgaben, deren ganze Aufgabe der Handgriff ist,
                   obwohl anders etikettiert (Spalte ganz_auch)
    verwechselbar  Stufen, mit denen der Handgriff verwechselt wird
                   (Feld Verwechselbar der Gliederung; leer, wenn keine)
    Die drei Spalten werden an die bestehende Datei angehängt bzw. dort
    ersetzt (--nur-spalten), ohne die übrigen Spalten neu zu bauen; der
    volle Lauf hängt sie ebenfalls an.

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
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import gliederung as GL
MN=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK=os.path.join(os.path.dirname(MN),'aufgabenbank')
# ---- Daten: aus der Prüfungsgliederung (v2) ----
def _lade_gliederung():
  """KAPITEL wie in v1: {kap: dict(pruefung, eintraege, stufen=[(name, echte, muster)], kern={name:(ja|nein, grund)})}
  und VERWECHSELBAR {(kap, stufe): [(kap, stufe)]} – aus msa/gliederung und abitur/gliederung."""
  K,V={},{}
  for pr in ('msa','abitur'):
    for kap,G in GL.alle(MN,pr).items():
      if not G['skript']: continue
      K[kap]=dict(pruefung=pr,eintraege=G['bank'],
        stufen=[(s['name'],s['originale'],[(e,p,f,'inner') if i else (e,p,f) for e,p,f,i in s['bank']]) for s in G['stufen']],
        kern={s['name']:(s['kern'],s['kern_grund']) for s in G['stufen']},gliederung=G)
      for s in G['stufen']:
        if s['verwechselbar']: V[(kap,s['name'])]=list(s['verwechselbar'])
  return K,V
KAPITEL,VERWECHSELBAR=_lade_gliederung()
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
  zus=os.path.join(MN,K.get('pruefung','msa'),kap+'-zusatz.jsonl')
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
ZUSATZ=['jahre_letzte5','nebenplaetze','verwechselbar']
def lade_handgriffe(pfad=None):
  """Plätze der Originale: aus den Gliederungsdateien (Tabellen „Plätze der Originale“, alle P10-Kapitel),
  oder aus einer handgriffe-CSV, wenn pfad angegeben ist; Zeilen wie msa/handgriffe-p10.csv."""
  if pfad:
    rows=[]
    with open(pfad,encoding='utf-8') as f:
      kopf=f.readline().rstrip('\n').split(';')
      for z in f:
        t=z.rstrip('\n').split(';')
        d=dict(zip(kopf,t))
        for c in ('hauptplatz','ganz_auch','zwischenschritt'):
          d[c]=[x.strip() for x in d[c].split('|') if x.strip()]
        rows.append(d)
    return rows
  rows=[dict(p) for G in GL.alle(MN,'msa').values() for p in G['plaetze']]
  return sorted(rows,key=lambda d:d['id'])
def zusatz(kap,name,H):
  key=f'{kap}:{name}'
  jahre=sorted({d['id'][:4] for d in H if '-GYM-' not in d['id'] and 2022<=int(d['id'][:4])<=2026
               and key in d['hauptplatz']+d['ganz_auch']+d['zwischenschritt']})
  neben=[d['id'] for d in H if key in d['ganz_auch']]
  verw=' | '.join(f'{k}:{s}' if k!=kap else s for k,s in VERWECHSELBAR.get((kap,name),[]))
  return [f'{len(jahre)} ({" ".join(jahre)})' if jahre else '0',' '.join(neben),verw]
def ergaenze(kap,pfad):
  """Hängt jahre_letzte5, nebenplaetze, verwechselbar an pfad an (oder ersetzt sie)."""
  if KAPITEL[kap].get('pruefung','msa')!='msa': return
  H=lade_handgriffe()
  zl=open(pfad,encoding='utf-8').read().rstrip('\n').split('\n')
  kopf=zl[0].split(';')
  idx=[kopf.index(c) for c in ZUSATZ if c in kopf]
  if idx: kopf=kopf[:min(idx)]
  out=[';'.join(kopf+ZUSATZ)]
  for z in zl[1:]:
    t=z.split(';')[:len(kopf)]
    out.append(';'.join(t+zusatz(kap,t[0],H)))
  open(pfad,'w',encoding='utf-8').write('\n'.join(out)+'\n')
def main(kap,pfad,zeige=False):
  K=KAPITEL[kap]
  A=lade(kap,K);res=zaehle2(kap,K,A,zeige)
  zl=['stufe;kern;katalog_ids;bank_sprossen;anzahl_echt;anzahl_bank;ziel;fehlen;kern_grund']
  for (name,echt,maps),(n2,e2,roh,n,art) in zip(K['stufen'],res):
    k,g=K['kern'][name];ziel=12 if k=='ja' else 6
    zus=sum(1 for d in A if d['eintrag']==kap+'-zusatz' and d['kette']==name)
    bs=(muster(maps)+(f' {K.get("pruefung","msa")}/{kap}-zusatz.jsonl({zus})' if zus else '')).strip()
    zl.append(f'{name};{k};{" ".join(echt)};{bs or "–"};{len(echt)};{n};{ziel};{max(0,ziel-len(echt)-n)};{g}')
  open(pfad,'w',encoding='utf-8').write('\n'.join(zl)+'\n')
  ergaenze(kap,pfad)
  if zeige: print(open(pfad,encoding='utf-8').read())

if __name__=='__main__':
  ap=argparse.ArgumentParser()
  ap.add_argument('kapitel',choices=sorted(KAPITEL))
  ap.add_argument('--bank',default=BANK)
  ap.add_argument('--aus')
  ap.add_argument('--zeige',action='store_true')
  ap.add_argument('--nur-spalten',action='store_true',help='nur jahre_letzte5, nebenplaetze, verwechselbar an die bestehende Datei anhängen')
  a=ap.parse_args();BANK=a.bank
  if a.nur_spalten:
    ergaenze(a.kapitel,a.aus or os.path.join(MN,'msa',f'zuordnung-{a.kapitel}.csv')); sys.exit(0)
  main(a.kapitel,a.aus or os.path.join(MN,KAPITEL[a.kapitel].get('pruefung','msa'),f'zuordnung-{a.kapitel}.csv'),a.zeige)
