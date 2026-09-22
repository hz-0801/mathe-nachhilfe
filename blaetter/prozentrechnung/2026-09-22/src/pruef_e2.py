# -*- coding: utf-8 -*-
from decimal import Decimal, ROUND_HALF_UP
res=[]
def r1(x): return float(Decimal(repr(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
def t(nr,soll,blatt):
    ok="OK" if abs(float(soll)-float(blatt))<1e-9 else "ABWEICHUNG"; res.append((nr,soll,blatt,ok))
# 8 Vorstufe: das Ganze
t("8a",25,25); t("8b",60,60); t("8c",400,400); t("8d",8+12,20); t("8e",30,30)
# 9 Streifen
t("9a",6/20*100,30); t("9b",35/50*100,70); t("9c",32/80*100,40); t("9d",90/200*100,45)
# 10
t("10a",19/100*100,19); t("10b",7/100*100,7); t("10c",64/100*100,64); t("10d",90/100*100,90)
t("10e",21/25*100,84); t("10f",21/60*100,35); t("10g",r1(5/12*100),41.7)
# 11 Umkehrung (Musterpaare)
t("11a",8/16*100,50); t("11b",5/20*100,25); t("11c1",2/5*100,40); t("11c2",20/50*100,40)
# 12
t("12a",26/40*100,65); t("12b",18/(18+32)*100,36); t("12c",(80-68)/80*100,15)
t("12d",r1(7/(7+17)*100),29.2)
# 13
t("13a",24/40*100,60); t("13b",36/45*100,80)
# 15
t("15a",12/20*100,60); t("15b",21/35*100,60); t("15c",12/20-21/35,0)
ab=0; lines=[]
for nr,s,b,ok in res:
    if ok!="OK": ab+=1
    lines.append(f"{nr:7s} Skript={float(s):<12.6g} Blatt={float(b):<12.6g} {ok}")
lines.append(f"Abweichungen: {ab}")
open("pruef_out_e2.txt","w").write("\n".join(lines)+"\n"); print(lines[-1])
