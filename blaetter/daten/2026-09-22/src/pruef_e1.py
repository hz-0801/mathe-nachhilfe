from fractions import Fraction as F
tests=[]
def t(nr,s,b): tests.append((nr,s,b))
# 8  Ganzes
for nr,v,b in [("8a",18,18),("8b",250,250),("8c",14+12,26),("8d",40,40),("8e",12+8+5,25)]: t(nr,v,b)
# 9  Strichlisten
t("9a",5+3,8); t("9b",5+5+2,12); t("9c",4,4); t("9d",5+5+5+1,16)
url=[3,5,1,3,6,3,2,5,3,1,6,4,3,2,5,3,6,1,4,3]
for k,b in zip(range(1,7),[3,2,7,2,3,3]): t(f"9e-{k}",url.count(k),b)
t("9e-summe",len(url),20)
# 10
t("10a",float(F(3,10)),0.3); t("10b",float(F(7,20)),0.35); t("10c",float(F(9,25)),0.36); t("10d",float(F(4,50)),0.08)
t("10e",float(F(6,24)),0.25); t("10f",13/20,0.65); t("10g",17/40,0.425); t("10g%",17/40*100,42.5)
t("10h",round(5/9*100,1),55.6); t("10i",100-45-35,20)
t("10j",9/(12+9+15+4)*100,22.5); t("10k",0.15*320,48)
t("10l-bruch",float(F(26,40)),float(F(13,20))); t("10l-prozent",26/40*100,65)
# 11
t("11a",8/32*100,25); t("11b-bruch",float(F(18,45)),float(F(2,5))); t("11b-prozent",18/45*100,40)
# 12
t("12b-7a",12/24*100,50); t("12b-7b",15/30*100,50)
# 13
t("13a-nord",84/240*100,35); t("13a-sued",78/195*100,40)
ab=0; out=[]
for nr,s,b in tests:
    ok=abs(s-b)<1e-9
    if not ok: ab+=1
    out.append(f"{nr}\t{s}\t{b}\t{'OK' if ok else 'ABWEICHUNG'}")
out.append(f"Abweichungen: {ab}")
open("pruef_out_e1.txt","w").write("\n".join(out)+"\n")
print(out[-1])
