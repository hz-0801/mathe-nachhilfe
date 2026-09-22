# -*- coding: utf-8 -*-
from fractions import Fraction as F
res=[]
def t(nr,soll,blatt):
    try: ok = "OK" if abs(float(soll)-float(blatt))<1e-9 else "ABWEICHUNG"
    except TypeError: ok = "OK" if soll==blatt else "ABWEICHUNG"
    res.append((nr,soll,blatt,ok))
def pz(f): return float(F(f)*100)
# 1 Streifen: Fuellung in % direkt abgelesen
for nr,v in [("1a",20),("1b",60),("1c",10),("1d",90)]: t(nr,v,v)
t("1e", 40/100*10, 4)          # Kaestchen von 10
t("1f", 65/100*10, 6.5)
# 2
t("2a",pz(F(23,100)),23); t("2b",pz(F(9,100)),9); t("2c",pz(F(57,100)),57)
t("2d",pz(F(80,100)),80); t("2e",pz(F(13,25)),52); t("2f",0.36*100,36)
t("2g",62/100,0.62); t("2h",F(40,100),F(2,5)); t("2i",pz(F(1,10)),10)
t("2j",16,16)                  # "16 von 100"
# 3
t("3a-min",min(8,80,18),8); t("3a-max",max(8,80,18),80)
t("3b-1",pz(F(1,5)),20); t("3b-2",25,25); t("3b-3",0.3*100,30)
t("3c",pz(F(2,5)),40)          # 40 % < 45 % -> Packung B
# 4
t("4a",100-40,60); t("4b",100-25,75); t("4c",100-70,30)
t("4d",100-30-45,25); t("4e",100-28-22-15,35)
t("4f",max(28,22,100-28-22-15,15),35)
# 5
t("5a",pz(F(1,8)),12.5); t("5b",pz(F(1,20)),5)
# 6
t("6a",F(1,20)*100,5); t("6b",0.5/100,0.005)
# 7
t("7-bus",30,30); t("7-drittel",round(100/3,1),33.3)
ab=0; lines=[]
for nr,s,b,ok in res:
    if ok!="OK": ab+=1
    lines.append(f"{nr:9s} Skript={float(s):<12.6g} Blatt={float(b):<12.6g} {ok}")
lines.append(f"Abweichungen: {ab}")
open("pruef_out_e1.txt","w").write("\n".join(lines)+"\n")
print(lines[-1])
