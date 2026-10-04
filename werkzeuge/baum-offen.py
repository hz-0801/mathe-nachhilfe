import re
F,A,V,I='fix','arbeit','vor','inhalt'
L=lambda *n:[(x,A,[]) for x in n]
LF=lambda *n:[(x,F,[]) for x in n]
ART=lambda st=A:[("Original",st,[]),("Original neu",st,[]),("Skript",st,[])]
TH={"Geometrie":["Trigonometrie","Flächen + Körper"],"Funktionen":["Funktionen","Wachstum"],"Daten + Zufall":["Daten","Wahrscheinlichk."]}
AL={"Geometrie":"Alles","Funktionen":"Alles","Daten + Zufall":"Alles"}
NEU={"Geometrie":([AL["Geometrie"]]+TH["Geometrie"],F),"Funktionen":(["Alles","Lineare","Quadratische","Wachstum"],F),"Daten + Zufall":([AL["Daten + Zufall"]]+TH["Daten + Zufall"],F)}
SK={"Geometrie":[("Trigonometrie",F),("Flächen + Körper",F),("Weitere (RLP)",F)],"Funktionen":[("Lineare",F),("Quadratische",F),("Gleichungssysteme",F),("Wachstum",F),("Weitere (RLP)",F)],"Daten + Zufall":[("Daten",F),("Prozent",F),("Wahrscheinlichk.",F),("Weitere (RLP)",F)]}
def ast(n): return (n,F,[("Original",F,[(t,F,[]) for t in [AL[n]]+TH[n]]),("Original neu",F,[(t,NEU[n][1],[]) for t in NEU[n][0]]),("Skript",F,[(t,st,[]) for t,st in SK[n]])])
tree=("P10",F,[
 ("Basis",F,[("Original",F,[("Zeitraum",F,[])]),("Original neu",F,[("Zeitraum",F,[])]),("Skript",F,[])]),
 ast("Geometrie"),ast("Funktionen"),ast("Daten + Zufall"),
 ("Ganze Prüfung",F,[("Original",F,[("Zeitraum",F,[])]),("Original neu",F,[("Zeitraum",F,[])]),("Skript",F,[])])])
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
   ("Daten",F,LE("Häufigkeiten","Säulen-, Balken-, Liniendiagr.","Streifen- und Kreisdiagramm","Kenngrößen","Diagramme beurteilen, Boxplot")),
   ("Prozent",F,LE("Prozente als Anteile","Prozentsatz","Prozentwert","Grundwert","Veränderung, Zinsen")),
   ("Wahrscheinlichk.",F,LE("Zählen, Ergebnismengen","einstufig (Laplace)","Baumdiagramm, Pfadregeln","ohne Zurücklegen")),
   ("Weitere (RLP)",F,LE("im RLP bis G, nie geprüft","z. B. Vierfeldertafel"))])])
GP=("Ganze Prüfung",F,[("Original",F,[("Heft ‹Jahr›",I,[])]),("Original neu",F,[("neu gesetzt ‹Jahr›, Lösungsblatt",I,[])]),("Skript",F,[("Probeprüfung",I,[])])])
HG=("Hilfsmittelfrei",F,[(t,F,[(g,F,[]) for g in ["Analysis","Geometrie","Stochastik"]]+[("Zeitraum",A,[])]) for t in ["Original","Original neu","Skript"]])
ABI=("Abitur",F,[HG]+[(x,F,[("Original",F,[("Zeitraum",F,[])]),("Original neu",F,[("Themen",A,[])]),("Skript",F,[("Themen wie Original neu + Weitere (RLP)",A,[])])]) for x in ["Analysis","Geometrie","Stochastik"]]+[("Ganze Prüfung",F,[("Original",F,[("Zeitraum",F,[])]),("Original neu",F,[]),("Skript",F,[])])])
FHR=("FHR",F,[(x,F,[("Original",F,[("Zeitraum",F,[])]),("Skript",A,[])]) for x in ["Analysis","Stochastik","Ganze Prüfung"]])
ZZ=lambda: [("Zeitraum",F,[])]
OP10=("P10 Original",F,[("Basis",F,ZZ()),
 ("Hauptteil",F,[(g,F,ZZ()) for g in ["Geometrie","Funktionen","Daten + Zufall","Alles"]]),
 ("Ganze Prüfung",F,ZZ())])
GB=lambda: [(g,F,ZZ()) for g in ["Analysis","Geometrie","Stochastik","Alles"]]
OABI=("Abitur Original",F,[("Hilfsmittelfrei",F,GB()),("Hauptteil",F,GB()),("Ganze Prüfung",F,ZZ())])
OFHR=("FHR Original",F,[("Analysis",F,ZZ()),("Stochastik",F,ZZ()),("Ganze Prüfung",F,ZZ())])
TZ=lambda ts: [(t,F,ZZ()) for t in ts]+[("Alles",F,ZZ())]
NP10=("P10 Original neu",F,[("Basis",F,ZZ()),
 ("Hauptteil",F,[("Geometrie",F,TZ(["Trigonometrie","Flächen + Körper"])),
   ("Funktionen",F,TZ(["Lineare","Quadratische","Wachstum"])),
   ("Daten + Zufall",F,TZ(["Daten","Wahrscheinlichk."])),("Alles",F,ZZ())]),
 ("Ganze Prüfung",F,ZZ())])
NABI=("Abitur Original neu",F,[("Hilfsmittelfrei",F,[(g,F,ZZ()) for g in ["Analysis","Geometrie","Stochastik","Alles"]]),
 ("Hauptteil",F,[("Analysis",F,TZ(["Kurvenuntersuchung","Ableitung + Tangente","Integral","Scharen (LK)"])),
   ("Geometrie",F,TZ(["Punkte, Flächen, Körper","Winkel + Abstände","Geraden + Ebenen","Scharen (LK)"])),
   ("Stochastik",F,TZ(["Baumdiagr. + bed. W.","Binomialverteilung","Testen (LK)"])),("Alles",F,ZZ())]),
 ("Ganze Prüfung",F,ZZ())])
NFHR=("FHR Original neu",F,[("Analysis",F,TZ(["Kurvendiskussion","Sachaufgaben"])),("Stochastik",F,TZ(["Daten","Wahrscheinlichkeit"])),("Ganze Prüfung",F,ZZ())])
FOKUS=('<h1 style="font-size:15px">Im Fokus: Original neu – Aufbau (Vorschlag 04.10.)</h1><p>Wie Original (Kurzteil · Hauptteil · Ganze Prüfung, Gebiete, „Alles“ zuletzt), dazu nach dem Gebiet eine Themenstufe; Themen vorläufig, Schnittprüfung offen.</p>\n'
 +draw(NP10,[86,70,80,92,52],G=16,k=1.15)+'\n'+draw(NABI,[98,84,72,118,52],G=16,k=1.15)+'\n'+draw(NFHR,[84,76,104,52],G=16,k=1.15)
 +'\n<h1 style="font-size:15px;margin-top:12px">Original (fertig 04.10.)</h1><p>Fest: Form, Schnitt an Aufgabengrenzen, Aufbau Kurzteil · Hauptteil · Ganze Prüfung, „Alles“ zuletzt. Regel ohne Ausnahme: jede Ebene, die sich aufteilt, endet mit „Alles“ (auch Hauptteil → Alles, z. B. Teil B am Stück). Original ohne Themenknöpfe, überall Gebiet → Zeitraum; nach Thema nur Original neu und Skript. Zeitraum fest: neuestes offenes · 2022–2026 · ältere · Jahr wählen. Lösung fest: Basis → Antwortbogen; sonst Lösungsblatt, je Heft eine Seite, je Aufgabe Kopfzeile, je Teilaufgabe links Lösung, rechts Zwischenwerte, keine Sätze; Aufgabe nie über Seitenwechsel; reicht eine Seite nicht: kleinere Schrift, dann zweite Seite. Original damit fertig.</p>\n'+draw(OP10,[66,76,80,52],k=1.0)+'\n'+draw(OABI,[74,78,72,52],k=1.0)+'\n'+draw(OFHR,[70,80,52],k=1.0)+'\n<hr style="border:0;border-top:1px solid var(--line);margin:14px 0">\n')
svg='<div id="baum">'+FOKUS+'<h1 style="font-size:15px">Abitur – Stufe 1 und 2 fest, Stufe 3 in Arbeit (03.10.)</h1><p>Kurs vorher aus der Schülerliste, sonst eine Frage; GK und LK sind getrennte Hefte, kein Sternchen-Blatt (2024–2026 kein gleicher Aufgabentext). Gebietsknöpfe nur Teil B; Hilfsmittelfrei eigener Knopf; Sonderwünsche per Freitext. Art wie P10. <b style="display:inline">Wer bekommt was (gilt für alle Prüfungen):</b> Original und Original neu sind für den Lehrer (Vorbereitung, Zeigen in der Stunde), Wortlaut nur privat; mitgegeben wird Skript (eigener Wortlaut) oder ein Antwortbogen zum amtlichen Heft; dazu Fundstelle mit QR-Code zum Bildungsserver. Original = ganze Aufgaben, Wortlaut unverändert, ohne Schnitt, layoutoptimiert (was das heißt: beim Bau); in den Gebieten ohne Themenwahl, direkt Zeitraum (eine Abitur-Aufgabe mischt alle Themen ihres Gebiets; P10 hat sechs Aufgaben mit je einem Thema). Original neu schneidet nach Teilaufgaben, wo es eine tiefere Themengliederung braucht (Vorspann und Zwischenergebnisse wiederholt; Themenknopf ab etwa 10 Teilaufgaben in fünf Jahren, sonst bündeln). Skript hat dieselbe Gliederung wie Original neu plus „Weitere (RLP)“ und bereitet darauf vor. Hilfsmittelfrei nach Gebiet (jede kleine Aufgabe gehört zu genau einem Gebiet, Schnitt an Aufgabengrenzen). CAS: kein eigener Ast, Unterschiede stecken in einzelnen Teilaufgaben (Umgang offen). Was nicht vorliegt, gibt es nicht (Berlin 2026, LK Berlin 2019–21). Zeitraum wie P10 (neuestes offenes · 2022–2026 · ältere · Jahr wählen; ältere endet bei 2017–2021, LK dort nur 2017/2018 BB). Themen Analysis (vorläufig, Abgleich mit Stark-Register offen): Alles · Kurvenuntersuchung (Kern Nullstellen, Extrem-, Wendepunkte zuerst) · Ableitung + Tangente · Integral · Scharen (nur LK). Skript = Lernblatt mit Leiter aus Katalog und Bank; ohne Rechner Geprüftes ist eine Sprosse mit Vermerk, kein eigener Abschnitt; anders als das Lernblatt: Gewichtung nach Prüfungsertrag, Prüfungsform und -sprache (Operatoren, Sie-Form), echte Prüfungsaufgabe vorn als Ziel und hinten als Prüfstein mit Fundstellen, typische Fehler, Aufgabenketten mit Kontrollergebnis, Punkte je Aufgabe (passt erstmal, 03.10.). Themen Geometrie (vorerst): Alles · Punkte, Flächen, Körper · Winkel + Abstände · Geraden + Ebenen · Scharen (nur LK). Themen Stochastik (vorerst): Alles · Baumdiagramm + bedingte Wahrscheinlichkeit · Binomialverteilung · Testen (nur LK). Die Themenknöpfe sind zugleich die Themenliste der Handreichungen GK/LK (eine Quelle: KNOPF in werkzeuge/handreichung-abi.py).</p>\n'+draw(ABI,[40,84,70,150],k=1.0)+'\n<h1 style="margin-top:14px;font-size:15px">FHR – Entwurf (03./04.10.)</h1><p>Eine Brandenburger Prüfung, ein Niveau, kein hilfsmittelfreier Teil, kein CAS; Original und Skript, kein Original neu (Vorschlag, offen). Themen: Analysis = Kurvendiskussion (mit Tangente, Normale, Integral – Kette, Schnitt dazwischen braucht Vorgaben) · Sachaufgaben (Funktion aufstellen, Extremwertaufgaben); Stochastik = Daten · Wahrscheinlichkeit.</p>\n'+draw(FHR,[30,70,70,46],k=1.0)+'\n<h1 style="margin-top:14px;font-size:15px">P10 – Gesamtbaum (fertig)</h1>\n'+draw(tree,W)+'\n<h1 style="margin-top:14px;font-size:15px">Zeitraum bei Original und Original neu (nach dem Thema; Basis statt des Themas)</h1>\n'+draw(ZT,[62,92,100],k=1.15)+'\n<p style="margin-top:6px"><b style="display:inline">Lösung, keine Wahl, immer dabei (vorerst):</b> Basis → für den Schüler ein Antwortbogen zum amtlichen Heft (QR-Code, Antwortfeld je Aufgabennummer, Lösungen im Faltstreifen), die Originalseiten bleiben beim Lehrer (03.10.) · sonst überall → Lösungsblatt als eigene Datei mit Rechenweg, Druck nach Wahl · Skript zusätzlich Kontrollwerte auf dem Blatt und Tipps für Schwache (vorn auf dem Lösungsblatt). Rechenweg, Kontrollwerte und Tipps stehen noch zur Diskussion. Skript-Heft vollständig (einmal gebaut, liegt bereit): Inhaltsverzeichnis mit Seitenbereichen, jeder Abschnitt auf neuer Seite, Sprungmarken/Lesezeichen, Druckbereich frei wählbar; je Abschnitt so ungefähr 4 Seiten, lose. Ziel: besser als Lernblatt und Original – Gewichtung nach P10-Ertrag, Prüfungsform oben, gemischter Schlussabschnitt, Aufgaben zu typischen Fehlern, echte Prüfungsaufgabe vorn als Ziel und hinten als Prüfstein. Schwach kommt aus der Schülerliste oder per Freitext, nie als Knopf. Kleine Themen (Zuordnungen, Einheiten, Winkel, Maßstab, Kombinatorik u. a.) ohne Knopf: als untere Sprossen im passenden Thema, gezielt per Freitext (Skript). Gleichungssysteme bei Original neu ohne Knopf (Freitext), im Skript mit Knopf. Zeitraum bei Original neu wie beim Original (gleicher Ablauf überall). Die Zeitraum-Knöpfe bei Original und Original neu nennen den Umfang in Seiten (≈ wenn geschätzt); das Skript nicht (Richtwert etwa 4 Seiten). Regel: Umfang steht dort, wo die Wahl ihn ändert – beim Vereinheitlichen prüfen. Original neu und Skript filtern gegen den Katalog (RLP). Prüfungsrelevant ist der RLP (Fachbrief 8): FOR bis Niveaustufe G, EBR bis F plus Liste aus G. Skript hat in jedem Ast als letzten Knopf „Weitere (RLP)“: Themen aus dem RLP, die noch nie geprüft wurden. Der Baum zeigt nur Entscheidungen. Freitext unklar oder passt nicht (z. B. „Daten“ – mit oder ohne Prozent, „Lineare“ gibt es nicht als Original): nachfragen oder sagen, was nicht passt, und mit Knöpfen zum Ziel führen; nur Knöpfe zeigen, die zu einem Blatt führen. Ganze Prüfung immer mit Basis; „ohne Basis“ per Freitext. Stufen: Ast → Art → Thema. Original = Heftseiten · Original neu = neu gesetzt (Layout), nach Teilaufgaben zugeschnitten, passende Teilaufgaben aus anderen Aufgaben erlaubt; Bau zuletzt (Wortlaut Aufgaben 2–7 noch nicht erfasst) · Skript = aus der Bank. Ein Blatt für EBR und FOR, FOR-Teile mit * (Original neu, Skript); Original ab 2026 (zwei Hefte): Heft nach Schülerliste, ohne Angabe FOR. Original in den Themen-Ästen: ganze Aufgaben, jüngste zuerst. „neuestes offenes“ = neuestes Jahr, das der genannte Schüler in diesem Ast/Thema noch nicht bekommen hat; dafür merkt sich eine Liste jedes gelieferte Blatt (Name, Ast, Art, Thema, Jahre). Ohne Namen oder ohne Eintrag: neuestes Jahr, Knopf zeigt die Zahl; Papier dann FOR; ein neuer Name wird in der Liste angelegt. Vor dem Bau eine Zeile „Name · Papier · Sorte“ zum Prüfen.</p></div>'
s=open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','offen.html'),encoding='utf-8').read()
s=re.sub(r'<p>Stand 03.10.2026 · Freitext.*?</p>','<p>Stand 03.10.2026 · Freitext geht immer · durchgezogen = fest, gestrichelt = in Arbeit, <span style="color:#d9822b;font-size:13px">orange = Schritt mit Vorschlag</span></p>',s,count=1,flags=re.S)
if '<div id="baum">' in s: s=re.sub(r'<div id="baum">.*?</div>',lambda m:svg,s,count=1,flags=re.S)
else: s=re.sub(r'<svg.*?</svg>(\n<p style="margin-top:6px">.*?</p>)*',lambda m:svg,s,count=1,flags=re.S)
open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','offen.html'),'w',encoding='utf-8').write(s)
