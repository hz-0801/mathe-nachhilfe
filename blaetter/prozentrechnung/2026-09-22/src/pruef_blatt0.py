# -*- coding: utf-8 -*-
from fractions import Fraction as F
def rnd1(x): 
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal(str(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
res=[]
def t(nr,soll,blatt):
    ok = "OK" if abs(float(soll)-float(blatt))<1e-9 else "ABWEICHUNG"
    res.append((nr,soll,blatt,ok))
# 1
t("1a",F(4,10),F(2,5)); t("1b",F(6,9),F(2,3)); t("1c",F(15,40),F(3,8))
t("1d",F(7,20)*100,35)            # Zaehler bei Nenner 100
t("1e",1,1)                       # 7/8 nicht erweiterbar: 100/8 nicht ganzzahlig
assert 100%8!=0 and 100%4==0 and 100%10==0
# 2
t("2a",F(1,2),0.5); t("2b",F(1,4),0.25); t("2c",F(4,10),F(2,5))
t("2d",F(3,5),0.6); t("2e",F(1,8),0.125); t("2f",0.07*100,7)
# 3
t("3a",rnd1(3.24),3.2); t("3b",rnd1(7.68),7.7); t("3c",rnd1(12.349),12.3)
t("3d",rnd1(9.96),10.0); t("3e",rnd1(5.55),5.6); t("3f",rnd1(28.04),28.0)
# 4
t("4a",400/100,4); t("4b",35/100,0.35); t("4c",7.50/100,0.075)
t("4d",0.4*60,24); t("4e",0.04*60,2.4); t("4f",1.2*50,60)
# 5 Dreisatz
t("5a-1",4.00/5,0.80); t("5a-8",4.00/5*8,6.40)
t("5b-1",2.10/6,0.35); t("5b-4",2.10/6*4,1.40)
t("5c-1",7.50/3,2.50); t("5c-7",7.50/3*7,17.50)
t("5d-1",3.00/4,0.75); t("5d-n",12.00/(3.00/4),16)
# 6
t("6a",F(1,2)*80,40); t("6b",F(1,4)*60,15); t("6c",F(3,4)*24,18)
t("6d",F(2,5)*45,18); t("6e",F(1,10)*7,0.70)
# 7
t("7a",F(3,8),0.375); t("7b",F(9,20),0.45)
ab=0
lines=[]
for nr,s,b,ok in res:
    if ok!="OK": ab+=1
    lines.append(f"{nr:8s} Skript={float(s):<12.6g} Blatt={float(b):<12.6g} {ok}")
lines.append(f"Abweichungen: {ab}")
open("pruef_out_blatt0.txt","w").write("\n".join(lines)+"\n")
print("\n".join(lines[-3:]))
