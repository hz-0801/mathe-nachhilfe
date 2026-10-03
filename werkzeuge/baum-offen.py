import re
F,A,V='fix','arbeit','vor'
L=lambda *n:[(x,A,[]) for x in n]
LF=lambda *n:[(x,F,[]) for x in n]
ART=lambda st=A:[("Original",st,[]),("Original neu",st,[]),("Skript",st,[])]
TH={"Geometrie":["Trigonometrie","Flächen + Körper"],"Funktionen":["Funktionen","Wachstum"],"Daten + Zufall":["Daten + Prozent","Wahrscheinlichk."]}
AL={"Geometrie":"Alles Geometrie","Funktionen":"Alle Funktionen","Daten + Zufall":"Alles Daten+Zuf."}
NEU={"Geometrie":([AL["Geometrie"]]+TH["Geometrie"],F),"Funktionen":(["Alle Funktionen","Lineare","Quadratische","Wachstum"],F),"Daten + Zufall":([AL["Daten + Zufall"]]+TH["Daten + Zufall"],A)}
def ast(n): return (n,F,[("Original",F,[(t,F,[]) for t in [AL[n]]+TH[n]]),("Original neu",F,[(t,NEU[n][1],[]) for t in NEU[n][0]]),("Skript",F,[(t,A,[]) for t in TH[n]])])
tree=("P10",F,[
 ("Basis",F,[("Original",F,[("Zeitraum",F,[])]),("Original neu",F,[("Zeitraum",F,[])]),("Skript",F,[])]),
 ast("Geometrie"),ast("Funktionen"),ast("Daten + Zufall")])
W=[32,78,78,96]; G=22; X=[6]
for w in W[:-1]: X.append(X[-1]+w+G)
def draw(tree,W,G=22,k=1.6):
    X=[6]
    for w in W[:-1]: X.append(X[-1]+w+G)
    rows=[];edges=[];nodes=[]
    def lay(n,d):
        name,st,ch=n
        if not ch: y=len(rows)*26+16; rows.append(1)
        else:
            ys=[lay(c,d+1) for c in ch]; y=sum(ys)/len(ys)
            for yc in ys: edges.append((X[d]+W[d],y,X[d+1],yc))
        nodes.append((d,y,name,st)); return y
    lay(tree,0)
    H=len(rows)*26+8; Wt=X[-1]+W[-1]+6
    sty={F:('var(--fg)','',"var(--fg)"),A:('var(--mute)',' stroke-dasharray="4 3"','var(--mute)'),V:('#d9822b','','#d9822b')}
    o=[f'<svg viewBox="0 0 {Wt} {H}" width="100%" style="max-width:{int(Wt*k)}px" role="img" aria-label="Entscheidungsbaum">']
    for x1,y1,x2,y2 in edges:
        m=(x1+x2)/2; o.append(f'<path d="M{x1},{y1} C{m},{y1} {m},{y2} {x2},{y2}" fill="none" stroke="var(--mute)" stroke-width="1"/>')
    for d,y,name,st in nodes:
        s,dash,t=sty[st]
        o.append(f'<rect x="{X[d]}" y="{y-11}" width="{W[d]}" height="22" rx="5" fill="var(--bg)" stroke="{s}"{dash}/>')
        o.append(f'<text x="{X[d]+W[d]/2}" y="{y+3.5}" text-anchor="middle" font-size="10" fill="{t}">{name.replace("‹","&#8249;").replace("›","&#8250;")}</text>')
    o.append('</svg>')
    return '\n'.join(o)
ZT=("Zeitraum",F,[("neuestes offenes",F,[]),("2022–2026",F,[]),("ältere",F,[("neuestes offenes",F,[]),("2017–2021",F,[]),("ältere → 2014–16",F,[]),("Jahr wählen",F,[])]),("Jahr wählen",F,[])])
ZR=lambda: [("Zeitraum",F,[])]
GEO=("Geometrie",F,[("Original",F,[(t,F,ZR()) for t in [AL["Geometrie"]]+TH["Geometrie"]]),("Original neu",F,[(t,F,ZR()) for t in [AL["Geometrie"]]+TH["Geometrie"]]),("Skript",F,[("Trigonometrie",F,[("Pythagoras",F,[]),("Sin/Kos/Tan",F,[]),("Sinussatz",F,[])]),("Flächen + Körper",F,[("Flächen",F,[]),("Körper",F,[])])])])
FKT=("Funktionen",F,[("Original",F,[(t,F,ZR()) for t in ["Alle Funktionen","Funktionen","Wachstum"]]),("Original neu",F,[(t,F,ZR()) for t in ["Alle Funktionen","Lineare","Quadratische","Wachstum"]]),("Skript",F,[(t,A,[]) for t in ["Lineare","Quadratische","Gleichungssysteme","Wachstum"]])])
svg='<div id="baum"><h1 style="font-size:15px">Im Gespräch: Funktionen</h1>\n'+draw(FKT,[66,74,100,72],k=1.3)+'\n<h1 style="margin-top:14px;font-size:15px">Gesamtbaum</h1>\n'+draw(tree,W)+'\n<h1 style="margin-top:14px;font-size:15px">Zeitraum bei Original und Original neu (nach dem Thema; Basis statt des Themas)</h1>\n'+draw(ZT,[62,92,100],k=1.15)+'\n<p style="margin-top:6px"><b style="display:inline">Lösung, keine Wahl, immer dabei:</b> Original → Lösungsblatt als eigene Datei, immer mitgeliefert, Druck nach Wahl · Original neu → Streifen · Basis-Skript → nur Streifen · Themen-Skript → Kontrollwerte auf dem Blatt, Lösungsweg als eigenes Blatt, Tipps nur für Schwache (vorn auf dem Lösungsblatt); Umfang so ungefähr 4 Seiten, Richtwert, keine Grenze. Schwach kommt aus der Schülerliste oder per Freitext, nie als Knopf. Der Baum zeigt nur Entscheidungen. Stufen: Ast → Art → Thema. Original = Heftseiten · Original neu = neu gesetzt (Layout), nach Teilaufgaben zugeschnitten, passende Teilaufgaben aus anderen Aufgaben erlaubt; Bau zuletzt (Wortlaut Aufgaben 2–7 noch nicht erfasst) · Skript = aus der Bank. Ein Blatt für EBR und FOR, FOR-Teile mit *. Original in den Themen-Ästen: ganze Aufgaben, jüngste zuerst. „neuestes offenes“ = neuestes Jahr, das der genannte Schüler noch nicht bekommen hat; ohne Namen das neueste. Vor dem Bau eine Zeile „Name · Sorte“ zum Prüfen.</p></div>'
s=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','offen.html'),encoding='utf-8').read()
s=re.sub(r'<p>Stand 03.10.2026 · Freitext.*?</p>','<p>Stand 03.10.2026 · Freitext geht immer · durchgezogen = fest, gestrichelt = in Arbeit, <span style="color:#d9822b;font-size:13px">orange = Schritt mit Vorschlag</span></p>',s,count=1,flags=re.S)
if '<div id="baum">' in s: s=re.sub(r'<div id="baum">.*?</div>',lambda m:svg,s,count=1,flags=re.S)
else: s=re.sub(r'<svg.*?</svg>(\n<p style="margin-top:6px">.*?</p>)*',lambda m:svg,s,count=1,flags=re.S)
open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','offen.html'),'w',encoding='utf-8').write(s)
