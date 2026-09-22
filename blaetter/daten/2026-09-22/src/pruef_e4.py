from statistics import mean, median
tests=[]
def t(nr,s,b): tests.append((nr,s,b))
L=[4,11,7,2,9]; t("31a-min",min(L),2); t("31a-max",max(L),11)
L2=[21,15,30,18]; t("31b-min",min(L2),15); t("31b-max",max(L2),30)
L3=[3.4,2.9,4.1,3.0]; t("31c-min",min(L3),2.9); t("31c-max",max(L3),4.1)
L4=[9,12,7,14,11,12,8]; t("31d-min",min(L4),7); t("31d-max",max(L4),14)
t("31e",max(L)-min(L),9)
L5=[8.7,9.2,8.5,9.0]; t("31f",round(max(L5)-min(L5),10),0.7)
L6=[6,4,6,9,4,6]; t("31g",max(set(L6),key=L6.count),6)
t("31h",median([5,2,8,1,9]),5); t("31i",median([14,11,20,17]),15.5)
D=[45,30,60,20,55]; t("31j-min",min(D),20); t("31j-max",max(D),60); t("31j-sp",max(D)-min(D),40)
t("32a",mean([3,5,7]),5); t("32b",mean([2,4,6,8]),5); t("32c",mean([10,20,30]),20); t("32d",mean([1,2,3,4,5]),3)
t("32e",mean([12.5,13.5,14.0,12.0]),13)
t("32f",round(mean([8.4,9.1,7.6,8.9,9.0,8.4]),1),8.6)
t("32g",round(4390/17),258); t("32h",344/8,43)
t("32i",6*15-(12+18+14+11+16),19)
A=[16,28,31,35,38,41,30,35,52]; t("32j-9",mean(A),34)
B=sorted(A)[1:-1]; t("32j-7",mean(B),34); t("32j-n",len(B),7)
W=[9,4,7,4,12]
t("33a",max(W)-min(W),8); t("33b",max(set(W),key=W.count),4); t("33c",median(W),7); t("33d",mean(W),7.2)
t("34a",median([12,5,9,3,7]),7); t("34b",median([20,14,25,11,18,22]),19)
ab=0; out=[]
for nr,s,b in tests:
    ok=abs(s-b)<1e-9
    if not ok: ab+=1
    out.append(f"{nr}\t{s}\t{b}\t{'OK' if ok else 'ABWEICHUNG'}")
out.append(f"Abweichungen: {ab}")
open("pruef_out_e4.txt","w").write("\n".join(out)+"\n"); print(out[-1])
