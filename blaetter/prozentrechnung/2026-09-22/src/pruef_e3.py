res=[]
def t(nr,soll,blatt):
    ok="OK" if abs(float(soll)-float(blatt))<1e-9 else "ABWEICHUNG"; res.append((nr,soll,blatt,ok))
t("16a",30/100*10,3); t("16b",75/100*4,3); t("16c",5/100*10,0.5); t("16d",60,60)
t("17a",0.50*80,40); t("17b",0.25*60,15); t("17c",0.10*200,20); t("17d",0.75*24,18)
t("18a",0.5*60,30); t("18b",0.25*80,20); t("18c",0.1*70,7); t("18d",0.5*46,23)
t("18e",300/100*7,21); t("18f",80/100*15,12); t("18g",0.35*140,49)
t("18h",0.40*7.50,3.00); t("18i",1.20*50,60)
t("19a",0.20*45,9); t("19b",45-0.20*45,36); t("19c",0.19*240,45.60); t("19d",0.15*320,48)
t("19d-distr",320-0.15*320,272)
t("20a",0.4*60,24); t("20b",0.7*90,63)
t("21b-1",0.25*80,20); t("21b-2",0.80*25,20)
t("22a",0.45*24000,10800); t("22b",0.60*15000,9000)
ab=0; lines=[]
for nr,s,b,ok in res:
    if ok!="OK": ab+=1
    lines.append(f"{nr:11s} Skript={float(s):<12.6g} Blatt={float(b):<12.6g} {ok}")
lines.append(f"Abweichungen: {ab}")
open("pruef_out_e3.txt","w").write("\n".join(lines)+"\n"); print(lines[-1])
