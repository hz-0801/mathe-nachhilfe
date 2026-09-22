from decimal import Decimal, ROUND_HALF_UP
def r1(x): return float(Decimal(repr(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
res=[]
def t(nr,soll,blatt):
    ok="OK" if abs(float(soll)-float(blatt))<1e-9 else "ABWEICHUNG"; res.append((nr,soll,blatt,ok))
t("30a",100-25,75); t("30b",100-10,90); t("30c",100-60,40); t("30d",100+20,120); t("30e",105-100,5)
t("31a",260,260); t("31b",480,480); t("31c",180,180); t("31d",3.20,3.20); t("31e",60,60)
t("32bsp",80*1.15,92)
t("32a",200*1.10,220); t("32b",60*0.75,45); t("32c",40*1.50,60); t("32d",90*0.90,81)
t("32e",35*1.2,42); t("32f",65*0.8,52); t("32g",4.80*1.25,6.00); t("32g-falle",0.25*4.80,1.20)
t("33bsp",8/50*100,16)
t("33a",(220-200)/200*100,10); t("33b",(80-60)/80*100,25); t("33c",(52-40)/40*100,30)
t("33d",(300-285)/300*100,5); t("33e",r1((0.58-0.55)/0.55*100),5.5)
t("34bsp",48/0.8,60)
t("34a",36/0.9,40); t("34b",15/1.25,12); t("34c",238/1.19,200); t("34d",21.40/1.07,20.00)
t("35a",46-40,6); t("35b",(46-40)/40*100,15); t("35c1",25-22,3); t("35c2",(25-22)/25*100,12)
t("36a",8,8); t("36b",6/50*100,12); t("36c",21/250*100,8.4)
t("37a",(75-60)/60*100,25); t("37a-falle",(75-60)/75*100,20); t("37b",(54-45)/45*100,20)
t("38b",100*1.1*0.9,99)
ab=0; lines=[]
for nr,s,b,ok in res:
    if ok!="OK": ab+=1
    lines.append(f"{nr:12s} Skript={float(s):<12.6g} Blatt={float(b):<12.6g} {ok}")
lines.append(f"Abweichungen: {ab}")
open("pruef_out_e5.txt","w").write("\n".join(lines)+"\n"); print(lines[-1])
