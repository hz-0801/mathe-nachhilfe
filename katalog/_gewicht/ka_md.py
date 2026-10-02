import re, collections
from ka_daten import R
from ka_bau import nteil, ein, T, agg, fehl
K=lambda r:(r[0],r[3],r[4])
def sel(f):
    rs=[r for r in R if f(r)]; return sum(nteil(r[4]) for r in rs), len({(r[0],r[3]) for r in rs}), len({(r[0],r[1]) for r in rs})
G=[
("Ähnlichkeit und zentrische Streckung: Streckfaktor, Ähnlichkeit prüfen, Bild zeichnen", lambda r:r[6]=="strahlensaetze" and r[7]=="E2" and "k²" not in r[8]),
("Scheitelpunktform lesen, zuordnen, aus dem Graphen aufstellen", lambda r:r[6]=="quadratische-funktionen" and r[7]=="E2"),
("Kreisteile: Ausschnitt, Bogen, Kreisring, Winkel aus Anteil", lambda r:r[6]=="kreis" and r[7]=="E3"),
("Kreisgrößen r, d, u, A ineinander umrechnen (auch rückwärts)", lambda r:r[6]=="kreis" and r[7] in("E1","E2")),
("Lösen quadratischer Gleichungen mit p-q-Formel, Normieren, Diskriminante", lambda r:r[6]=="quadratische-gleichungen" and r[7]=="E2" and r[10]!="nein"),
("Wurzel- und Potenzfunktionen (Graph, Definitionsbereich, Verschiebung)", lambda r:"Potenz- und Wurzelfunktionen" in r[8] or "wie Kap. 3 Nr. 6" in r[8]),
("Strahlensätze: Verhältnisse aufstellen, Längen und Sachaufgaben", lambda r:r[6]=="strahlensaetze" and r[7]=="E3"),
("Graph einer Parabel zeichnen, Wertetabelle, Öffnung/Breite", lambda r:r[6]=="quadratische-funktionen" and r[7]=="E1" and r[5].find("einordnen")<0),
("Kenngrößen und Streuung (Mittel, Median, Varianz, Standardabweichung, Deutung)", lambda r:r[6]=="daten" and r[7] in("E4","E6") and "Klassen" not in r[8]),
("Pythagoras in Figuren und Körpern (Sachaufgaben, Raumdiagonale)", lambda r:r[6]=="pythagoras" and r[7]=="E3"),
("Flächen bei Streckung (Faktor k²)", lambda r:"k²" in r[8]),
("Ungleichungen (linear und quadratisch, auch Systeme)", lambda r:"Ungleichung" in r[5] or "Ungleichung" in r[8] or "Ungleichungssystem" in r[5]),
("Satzgruppe: Kathetensatz und Höhensatz", lambda r:"Kathetensatz" in r[8] or "wie Kap. 6 Nr. 2c" in r[8]),
]
res=sorted([(n,a,k,l) for l,f in G for n,a,k in [sel(f)]],reverse=True)
L=[]
L.append("# Klassenarbeiten Duden „Wissen – Üben – Testen, Mathematik 9“ (2017): Gewichtung\n")
L.append("Stand 2026-10-02. Quelle: Musterklassenarbeiten (PDF-S. 12, 24–26, 38–43, 56–61, 74–77, 86–89, 96–98, 107–109, 113–115, 125–126); Zeilen in `ka-duden9.csv`. Kapitel 4 aus der Inventartabelle in `abgleich-quadratische-gleichungen-duden9.md` übernommen, Minuten nachgesehen.\n")
L.append("## Kurzfassung\n\nKURZFASSUNG\n")
nkas=len({(r[0],r[1]) for r in R}); nauf=len({(r[0],r[3]) for r in R})
s=collections.Counter()
for r in R: s[r[10]]+=nteil(r[4])
L.append(f"## Zahlen\n\n{nkas} Klassenarbeiten, {nauf} Aufgaben, {T} Teilaufgaben (Teilaufgabe = Buchstabe; Aufgabe ohne Buchstaben = 1), {len(R)} CSV-Zeilen. Punkte: Das Buch vergibt keine; gewichtet wird daher nach Teilaufgaben. Zuordnung: Sprosse sicher {s['ja']} ({100*s['ja']/T:.0f} %), nur Einheit sicher {s['einheit']} ({100*s['einheit']/T:.0f} %), kein Eintrag oder Sprosse fehlt {s['nein']} ({100*s['nein']/T:.0f} %).\n")
mins={}
for r in R: mins[(r[0],r[1])]=r[2]
L.append("Minuten je Klassenarbeit: "+"; ".join(f"Kap. {k}: "+", ".join(f"KA{ka} {m}" for (kk,ka),m in sorted(mins.items()) if kk==k) for k in sorted({k for k,_ in mins}))+".\n")
L.append("## Je Katalogeintrag und Einheit\n")
L.append("| Eintrag | Einheit | Teilaufgaben | Anteil | Aufgaben | Klassenarbeiten |\n|---|---|---|---|---|---|")
byE=collections.defaultdict(list)
for (e,u),v in agg.items(): byE[e].append((u,v))
tot=lambda e:sum(v[0] for u,v in byE[e])
for e in sorted(byE,key=lambda e:-tot(e)):
    for u,(n,k,z) in sorted(byE[e]):
        a=len({(r[0],r[3]) for r in R if r[6]==e and r[7]==u})
        L.append(f"| {e} | {u} {ein.get((e,u),'')} | {n} | {100*n/T:.1f} % | {a} | {len(k)} |")
    if len(byE[e])>1: L.append(f"| **{e} gesamt** | | **{tot(e)}** | **{100*tot(e)/T:.1f} %** | | |")
L.append("\n## Die zehn am häufigsten geprüften Typen\n")
L.append("Typ = Bündel gleichartiger Teilaufgaben (Einheit oder Kette); gezählt nach Teilaufgaben.\n")
L.append("| Rang | Typ | Teilaufgaben | Aufgaben | Klassenarbeiten |\n|---|---|---|---|---|")
for i,(n,a,k,l) in enumerate(res[:10],1): L.append(f"| {i} | {l} | {n} | {a} | {k} |")
L.append(f"\nKnapp dahinter: "+"; ".join(f"{l} ({n})" for n,a,k,l in res[10:])+".\n")
L.append("## Typen aus Klassenarbeiten ohne Katalogsprosse\n")
L.append("| Kap. | Nr. | Teil | Typ | Teilaufg. | Vorschlag / Befund |\n|---|---|---|---|---|---|")
for r in R:
    if r[10]=="nein": L.append(f"| {r[0]} | {r[3]} | {r[4].replace('-','–')} | {r[5]} | {nteil(r[4])} | {r[8]} |")
L.append("\n## Einheiten des Katalogs ohne Klassenarbeit\n")
L.append("Bezug: die 16 Einträge in `katalog-kompakt-kl9.md`.\n")
for e,u,t in fehl: L.append(f"- {e} {u} {t}")
L.append("\nDazu nur mit einer einzigen Teilaufgabe: "+", ".join(f"{e} {u} {ein.get((e,u),'')}" for (e,u),v in sorted(agg.items()) if v[0]==1 and e!="kein Eintrag")+".")
form=collections.Counter()
for r in R:
    for f in r[9].split(" + "): form[f]+=nteil(r[4])
L.append("\n## Formen\n\nTeilaufgaben je Form (Mehrfachform zählt in jeder): "+", ".join(f"{f} {n}" for f,n in form.most_common())+".\n")
open("ka-duden9.md","w",encoding="utf-8").write("\n".join(L)+"\n")
print("\n".join(L[:6])); print(res)
