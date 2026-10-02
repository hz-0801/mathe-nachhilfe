import csv, re, collections
from ka_daten import R
def nteil(t):
    if not t: return 1
    n=0
    for p in t.split(","):
        m=re.fullmatch(r"([a-z])-([a-z])",p.strip())
        n+= (ord(m.group(2))-ord(m.group(1))+1) if m else 1
    return n
with open("ka-duden9.csv","w",encoding="utf-8",newline="") as f:
    w=csv.writer(f,delimiter=";",lineterminator="\n")
    w.writerow("kapitel;ka;minuten;aufgabe;teil;punkte;typ;eintrag;einheit;kette_sprosse;form;zuordnung_sicher".split(";"))
    for r in R:
        k,ka,mi,a,t,typ,e,u,ks,fo,s=r
        w.writerow([k,ka,mi,a,t.replace("-","–"),"",typ,e,u,ks,fo,s])
# Einheiten aus kompakt
ein={}; cur=None
for line in open("katalog-kompakt-kl9.md",encoding="utf-8"):
    m=re.match(r"## (\S+)",line)
    if m: cur=m.group(1); continue
    m=re.match(r"E (\d+)\. (.*?)(?: –|$)",line.strip())
    if m and cur: ein[(cur,"E"+m.group(1))]=m.group(2).strip()
kas={(r[0],r[1]) for r in R}; aufg={(r[0],r[3]) for r in R}
T=sum(nteil(r[4]) for r in R)
print("KA",len(kas),"Aufgaben",len(aufg),"Zeilen",len(R),"Teilaufgaben",T, "Minuten", sum({(r[0],r[1]):r[2] for r in R}.values()))
s=collections.Counter(); 
for r in R: s[r[10]]+=nteil(r[4])
print("sicher",dict(s))
agg=collections.defaultdict(lambda:[0,set(),0])
for r in R:
    key=(r[6],r[7]); n=nteil(r[4]); agg[key][0]+=n; agg[key][1].add((r[0],r[1])); agg[key][2]+=1
agg_e=collections.Counter()
for r in R: agg_e[r[6]]+=nteil(r[4])
for e,n in agg_e.most_common(): print(f"{e:28s}{n:4d} {100*n/T:5.1f}%")
print()
for (e,u),(n,k,z) in sorted(agg.items(),key=lambda x:-x[1][0]): print(e,u,n,len(k),ein.get((e,u),""))
fehl=[(e,u,t) for (e,u),t in ein.items() if (e,u) not in agg]
print("FEHLEND",len(fehl)); [print(x) for x in fehl]
form=collections.Counter()
for r in R:
    for f in r[9].split(" + "): form[f]+=nteil(r[4])
print(form.most_common())
