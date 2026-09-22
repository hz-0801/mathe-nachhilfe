tests=[]
def t(nr,s,b): tests.append((nr,s,b))
A={2020:840,2021:910,2022:880,2023:1050,2024:1200}
t("36b",A[2022]>900,False); t("36d",A[2020]<800,False)
t("36e",A[2024]>A[2023],True)
t("36f",all(A[j]<A[j+1] for j in range(2020,2024)),False)
t("36g",A[2024]>2*A[2020],False)
t("36h",A[2020]*1.25,1050)
t("36i",1/8*100,12.5)
M={2021:410,2022:420,2023:430,2024:450}
t("37a",400,400); t("37b",round((450-410)/410*100,1),9.8)
t("37c-hoehen",[M[j]-400 for j in M],[10,20,30,50])
bp=[3,7,11,15,19]
for nr,v,b in [("38a",bp[0],3),("38b",bp[4],19),("38c",bp[2],11),("38d",bp[1],7),("38e",bp[3],15),("38f",bp[4]-bp[0],16)]: t(nr,v,b)
t("38g",50,50); t("38h",25,25)
t("39b",round((240-220)/220*100,1),9.1)
ab=0; out=[]
for nr,s,b in tests:
    ok = (s==b) if isinstance(b,(bool,list)) else abs(s-b)<1e-9
    if not ok: ab+=1
    out.append(f"{nr}\t{s}\t{b}\t{'OK' if ok else 'ABWEICHUNG'}")
out.append(f"Abweichungen: {ab}")
open("pruef_out_e5.txt","w").write("\n".join(out)+"\n"); print(out[-1])
