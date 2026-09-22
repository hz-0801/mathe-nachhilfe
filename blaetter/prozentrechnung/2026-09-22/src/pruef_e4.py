res=[]
def t(nr,soll,blatt):
    ok="OK" if abs(float(soll)-float(blatt))<1e-9 else "ABWEICHUNG"; res.append((nr,soll,blatt,ok))
t("24a",8/20*100,40); t("24b",35/50*100,70); t("24c",4/10*100,40); t("24d",12/25*100,48)
t("25bsp",21/35*100,60)
t("25a",14/50*100,28); t("25b",9/25*100,36); t("25c",7/20*100,35); t("25d",6/10*100,60)
t("25e",18/40*100,45); t("25f",42/12*100,350)
t("26a",18/60*100,30); t("26b",27/15*100,180)
t("27a",35/25*100,140); t("27a-fehler",0.25*35,8.75); t("27b",60/20*100,300)
t("29a",0.15*40,6); t("29b",14/56*100,25); t("29c",33/55*100,60)
t("29d",0.45*120,54); t("29e",8/16*100,50)
ab=0; lines=[]
for nr,s,b,ok in res:
    if ok!="OK": ab+=1
    lines.append(f"{nr:12s} Skript={float(s):<12.6g} Blatt={float(b):<12.6g} {ok}")
lines.append(f"Abweichungen: {ab}")
open("pruef_out_e4.txt","w").write("\n".join(lines)+"\n"); print(lines[-1])
