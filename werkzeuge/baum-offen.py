import re
F,A,V,I='fix','arbeit','vor','inhalt'
L=lambda *n:[(x,A,[]) for x in n]
LF=lambda *n:[(x,F,[]) for x in n]
ART=lambda st=A:[("Original",st,[]),("Original neu",st,[]),("Skript",st,[])]
TH={"Geometrie":["Trigonometrie","Flächen + Körper"],"Funktionen":["Funktionen","Wachstum"],"Daten + Zufall":["Daten","Wahrscheinlichk."]}
AL={"Geometrie":"Alles","Funktionen":"Alles","Daten + Zufall":"Alles"}
NEU={"Geometrie":([AL["Geometrie"]]+TH["Geometrie"],F),"Funktionen":(["Alles","Lineare","Quadratische","Wachstum"],F),"Daten + Zufall":([AL["Daten + Zufall"]]+TH["Daten + Zufall"],F)}
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
    sty={I:('none','','var(--mute)'),F:('var(--fg)','',"var(--fg)"),A:('var(--mute)',' stroke-dasharray="4 3"','var(--mute)'),V:('#d9822b','','#d9822b')}
    o=[f'<svg viewBox="0 0 {Wt} {H}" width="100%" style="max-width:{int(Wt*k)}px" role="img" aria-label="Entscheidungsbaum">']
    for x1,y1,x2,y2 in edges:
        m=(x1+x2)/2; o.append(f'<path d="M{x1},{y1} C{m},{y1} {m},{y2} {x2},{y2}" fill="none" stroke="var(--mute)" stroke-width="1"/>')
    for d,y,name,st in nodes:
        s,dash,t=sty[st]
        if st!=I: o.append(f'<rect x="{X[d]}" y="{y-11}" width="{W[d]}" height="22" rx="5" fill="var(--bg)" stroke="{s}"{dash}/>')
        anc,xx=('start',X[d]+2) if st==I else ('middle',X[d]+W[d]/2)
        o.append(f'<text x="{xx}" y="{y+3.5}" text-anchor="{anc}" font-size="{9 if st==I else 10}" font-style="{"italic" if st==I else "normal"}" fill="{t}">{name.replace("‹","&#8249;").replace("›","&#8250;")}</text>')
    o.append('</svg>')
    return '\n'.join(o)
ZT=("Zeitraum",F,[("neuestes offenes",F,[]),("2022–2026",F,[]),("ältere",F,[("neuestes offenes",F,[]),("2017–2021",F,[]),("ältere → 2014–16",F,[]),("Jahr wählen",F,[])]),("Jahr wählen",F,[])])
ZR=lambda: [("Zeitraum",F,[])]
GEO=("Geometrie",F,[("Original",F,[(t,F,ZR()) for t in [AL["Geometrie"]]+TH["Geometrie"]]),("Original neu",F,[(t,F,ZR()) for t in [AL["Geometrie"]]+TH["Geometrie"]]),("Skript",F,[("Trigonometrie",F,[("Pythagoras",F,[]),("Sin/Kos/Tan",F,[]),("Sinussatz",F,[])]),("Flächen + Körper",F,[("Flächen",F,[]),("Körper",F,[])])])])
LE=lambda *n:[(x,I,[]) for x in n]
FKT=("Funktionen",F,[
 ("Original",F,[(t,F,ZR()) for t in ["Alles","Funktionen","Wachstum"]]),
 ("Original neu",F,[(t,F,ZR()) for t in ["Alles","Lineare","Quadratische","Wachstum"]]),
 ("Skript",F,[
   ("Lineare",F,LE("proportional, Zuordnungen","f(x) = mx + n zeichnen","Punkte, Werte, Punktprobe","Gleichung bestimmen","Anwendungen, Tarife")),
   ("Quadratische",F,LE("Normalparabel, Streckfaktor","Scheitelpunktform","Normalform","Nullstellen, Schnittpunkte")),
   ("Gleichungssysteme",F,LE("grafisch lösen","Einsetzungsverfahren","Additionsverfahren","Sachaufgaben aufstellen")),
   ("Wachstum",F,LE("linear oder exponentiell","Faktor, Wachstumstabelle","Funktion aufstellen","Verdopplung, Halbwertszeit"))])])
DZ=("Daten + Zufall",F,[
 ("Original",F,[(t,F,ZR()) for t in ["Alles","Daten","Wahrscheinlichk."]]),
 ("Original neu",F,[(t,F,ZR()) for t in ["Alles","Daten","Wahrscheinlichk."]]),
 ("Skript",F,[
   ("Daten",A,LE("Häufigkeiten","Säulen-, Balken-, Liniendiagr.","Streifen- und Kreisdiagramm","Kenngrößen","Diagramme beurteilen, Boxplot")),
   ("Prozent",A,LE("Prozente als Anteile","Prozentsatz","Prozentwert","Grundwert","Veränderung, Zinsen")),
   ("Wahrscheinlichk.",A,LE("Zählen, Ergebnismengen","einstufig (Laplace)","Baumdiagramm, Pfadregeln","ohne Zurücklegen"))])])
svg='<div id="baum"><h1 style="font-size:15px">Im Gespräch: Daten und Zufall</h1><p>kursiv = Inhalt des Skripts (Lerneinheiten aus dem Katalog, auf P10 gefiltert), keine Wahl</p>\n'+draw(DZ,[72,70,104,124],k=1.3)+'\n<h1 style="margin-top:14px;font-size:15px">Gesamtbaum</h1>\n'+draw(tree,W)+'\n<h1 style="margin-top:14px;font-size:15px">Zeitraum bei Original und Original neu (nach dem Thema; Basis statt des Themas)</h1>\n'+draw(ZT,[62,92,100],k=1.15)+'\n<p style="margin-top:6px"><b style="display:inline">Lösung, keine Wahl, immer dabei:</b> Original → Lösungsblatt als eigene Datei, immer mitgeliefert, Druck nach Wahl · Original neu → Streifen · Basis-Skript → nur Streifen · Themen-Skript → Kontrollwerte auf dem Blatt, Lösungsweg als eigenes Blatt, Tipps nur für Schwache (vorn auf dem Lösungsblatt); Skript-Heft vollständig (einmal gebaut, liegt bereit): Inhaltsverzeichnis mit Seitenbereichen, jeder Abschnitt auf neuer Seite, Sprungmarken/Lesezeichen, Druckbereich frei wählbar; je Abschnitt so ungefähr 4 Seiten, lose. Ziel: besser als Lernblatt und Original – Gewichtung nach P10-Ertrag, Prüfungsform oben, gemischter Schlussabschnitt, Aufgaben zu typischen Fehlern, echte Prüfungsaufgabe vorn als Ziel und hinten als Prüfstein. Schwach kommt aus der Schülerliste oder per Freitext, nie als Knopf. Kleine Themen (Zuordnungen, Einheiten, Winkel, Maßstab, Kombinatorik u. a.) ohne Knopf: als untere Sprossen im passenden Thema, gezielt per Freitext (Skript). Gleichungssysteme bei Original neu ohne Knopf (Freitext), im Skript mit Knopf. Zeitraum bei Original neu wie beim Original (gleicher Ablauf überall). Die Zeitraum-Knöpfe bei Original und Original neu nennen den Umfang in Seiten (≈ wenn geschätzt); das Skript nicht (Richtwert etwa 4 Seiten). Regel: Umfang steht dort, wo die Wahl ihn ändert – beim Vereinheitlichen prüfen. Original neu und Skript filtern gegen den Katalog (RLP). Der Baum zeigt nur Entscheidungen. Stufen: Ast → Art → Thema. Original = Heftseiten · Original neu = neu gesetzt (Layout), nach Teilaufgaben zugeschnitten, passende Teilaufgaben aus anderen Aufgaben erlaubt; Bau zuletzt (Wortlaut Aufgaben 2–7 noch nicht erfasst) · Skript = aus der Bank. Ein Blatt für EBR und FOR, FOR-Teile mit *. Original in den Themen-Ästen: ganze Aufgaben, jüngste zuerst. „neuestes offenes“ = neuestes Jahr, das der genannte Schüler noch nicht bekommen hat; ohne Namen das neueste. Vor dem Bau eine Zeile „Name · Sorte“ zum Prüfen.</p></div>'
s=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','offen.html'),encoding='utf-8').read()
s=re.sub(r'<p>Stand 03.10.2026 · Freitext.*?</p>','<p>Stand 03.10.2026 · Freitext geht immer · durchgezogen = fest, gestrichelt = in Arbeit, <span style="color:#d9822b;font-size:13px">orange = Schritt mit Vorschlag</span></p>',s,count=1,flags=re.S)
if '<div id="baum">' in s: s=re.sub(r'<div id="baum">.*?</div>',lambda m:svg,s,count=1,flags=re.S)
else: s=re.sub(r'<svg.*?</svg>(\n<p style="margin-top:6px">.*?</p>)*',lambda m:svg,s,count=1,flags=re.S)
open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','offen.html'),'w',encoding='utf-8').write(s)
