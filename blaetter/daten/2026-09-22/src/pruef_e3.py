tests=[]
def t(nr,s,b): tests.append((nr,s,b))
for nr,p,b in [("23a",40,4),("23b",20,2),("23c",70,7),("23d",5,0.5),("23e",45,4.5)]: t(nr,p/10,b)
for nr,p,b in [("23f-Rad",25,2.5),("23f-Bus",40,4),("23f-Fuss",20,2),("23f-Auto",15,1.5)]: t(nr,p/10,b)
t("23f-summe",(25+40+20+15)/10,10); t("23g",100-30-25-20,25)
for nr,p,b in [("24a",50,180),("24b",25,90),("24c",10,36),("24d",75,270),("24e",12,43.2),("24f",37.5,135)]:
    t(nr,p/100*360,b)
t("24g",8/25*360,115.2); t("24h",15/400*360,13.5); t("24i",round(3/7*360,1),154.3)
t("25c",360-90-120,150)
t("25d-F",100/240*360,150); t("25d-H",80/240*360,120); t("25d-J",60/240*360,90)
t("26-summe",38+27+21+14,100); t("26c",round(17/450*360,1),13.6)
t("27a",0.24*360,86.4); t("27b",0.45*360,162)
t("28a",360/100,3.6)
ab=0; out=[]
for nr,s,b in tests:
    ok=abs(s-b)<1e-9
    if not ok: ab+=1
    out.append(f"{nr}\t{s}\t{b}\t{'OK' if ok else 'ABWEICHUNG'}")
out.append(f"Abweichungen: {ab}")
open("pruef_out_e3.txt","w").write("\n".join(out)+"\n"); print(out[-1])
