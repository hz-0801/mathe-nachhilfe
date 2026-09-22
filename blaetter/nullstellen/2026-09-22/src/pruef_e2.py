import sympy as sp
x = sp.Symbol('x'); zeilen=[]; abw=0
def pruef(nr, s, b):
    global abw
    ok = str(s).replace(' ','')==str(b).replace(' ','')
    if not ok: abw+=1
    zeilen.append(f"{nr:<10} Skript: {str(s):<32} Blatt: {str(b):<32} {'OK' if ok else 'ABWEICHUNG'}")
def loes(e):
    return sorted([sp.nsimplify(v) for v in sp.solve(e,x) if v.is_real], key=lambda v: float(v))
# 10 Vorstufe
for nr,rechts,soll in [("10a",0,"ja"),("10b",12,"nein"),("10c",0,"ja"),("10d",24,"nein"),("10e",0,"ja")]:
    pruef(nr,"ja" if rechts==0 else "nein",soll)
# 11
pruef("11-Bsp",loes(sp.Eq((x-3)*(x+8),0)),[-8,3])
kette=[("11a",(x-2)*(x-9),[2,9]),("11b",(x-4)*(x-11),[4,11]),("11c",(x-1)*(x-6),[1,6]),
       ("11d",(x-5)*(x-12),[5,12]),("11e",(x+7)*(x-3),[-7,3]),("11f",x*(x+4),[-4,0]),
       ("11g",(x-6)*(x-6),[6]),("11h",x**2+9*x,[-9,0]),("11i",x**2-13*x,[0,13]),
       ("11j",4*x**2+20*x,[-5,0]),("11k",3*x**2-12*x,[0,4])]
for nr,t,soll in kette: pruef(nr,loes(sp.Eq(t,0)),soll)
# 12 umformen: Normalform
for nr,l,r,soll in [("12a",x*(x+6),27,x**2+6*x-27),("12b",(x-2)*(x+5),18,x**2+3*x-28),
                    ("12c",x*(x-9),-14,x**2-9*x+14)]:
    pruef(nr,sp.expand(l-r),sp.expand(soll))
# 13 Probe
def probe(l,r,w): return sp.simplify(l.subs(x,w)-r)==0
pruef("13a",probe(x*(x+10),-24,-6),True)
pruef("13b",probe((x-7)*(x+2),-20,3),True)
pruef("13c",probe((x+5)*(x-1),9,-2),False)
# 14 Fehler finden
pruef("14-falsch",[11],[11])
pruef("14-richtig",loes(sp.Eq(x**2,11*x)),[0,11])
pruef("14a",loes(sp.Eq(x**2,6*x)),[0,6])
# 15 Begruenden
pruef("15c-1",loes(sp.Eq((x+3)*(x-3),0)),[-3,3])
pruef("15c-2",loes(sp.Eq((x+3)*(x+3),0)),[-3])
# 16 Ankreuzen
pruef("16a",loes(sp.Eq(x*(x-6),0)),[0,6])
pruef("16a-Opt",[o for o in [0,6,-6,1] if sp.simplify((x*(x-6)).subs(x,o))==0],[0,6])
pruef("16b",loes(sp.Eq(x*(x+7),-12)),[-4,-3])
pruef("16b-Opt",[o for o in [3,-3,-12,4] if sp.simplify((x*(x+7)).subs(x,o))==-12],[-3])
open("pruef_out_e2.txt","w").write("\n".join(zeilen)+f"\nAbweichungen: {abw}\n")
print("\n".join(zeilen)); print("Abweichungen:",abw)
