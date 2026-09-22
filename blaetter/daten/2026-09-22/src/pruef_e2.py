tests=[]
def t(nr,s,b): tests.append((nr,s,b))
t("14a",10,10); t("14b",100/2,50); t("14c",20/4,5); t("14d",0.05/5,0.01); t("14e",200/4,50)
t("15b",40,40); t("15d",3.10,3.10); t("15e",820,820)
g={"Mo":20,"Di":60,"Mi":40,"Do":80,"Fr":55,"Sa":75,"So":65}
for k,v in g.items(): t("16-"+k,v,v)
t("16g",sum(1 for v in g.values() if v>60),3)
t("16h-max",max(g.values()),80); t("16h-min",min(g.values()),20)
t("16i",g["Sa"]-g["Mi"],35)
z={"2021":30,"2022":24,"2023":38,"2024":46}
t("16j",z["2022"]*1000,24000); t("16k",z["2024"]*1000,46000); t("16l",(z["2024"]-z["2021"])*1000,16000)
t("17a",24,24); t("17b",14,14)
temp=[2,5,4,9,14,17]
t("17d",temp[2],4); t("17e",min(temp),2)
t("18f-min",75,75)
t("19a",120/4,30); t("19b",6*30,180); t("19c",3*30,90); t("19d",210/30,7)
t("19e-kaestchen",480/6,80); t("19e-hindi",320/80,4); t("19e-port",240/80,3); t("19e-arab",400/80,5)
t("20a",18*1000,18000); t("20b",25*1000,25000)
t("21b",50/5,10)
ab=0; out=[]
for nr,s,b in tests:
    ok=abs(s-b)<1e-9
    if not ok: ab+=1
    out.append(f"{nr}\t{s}\t{b}\t{'OK' if ok else 'ABWEICHUNG'}")
out.append(f"Abweichungen: {ab}")
open("pruef_out_e2.txt","w").write("\n".join(out)+"\n"); print(out[-1])
