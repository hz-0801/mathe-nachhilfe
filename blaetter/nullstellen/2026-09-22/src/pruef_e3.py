import sympy as sp, math
x=sp.Symbol('x'); zeilen=[]; abw=0
def pruef(nr,s,b):
    global abw
    ok=str(s).replace(' ','')==str(b).replace(' ','')
    if not ok: abw+=1
    zeilen.append(f"{nr:<10} Skript: {str(s):<40} Blatt: {str(b):<40} {'OK' if ok else 'ABWEICHUNG'}")
def loes(t):
    return sorted([sp.nsimplify(v) for v in sp.solve(sp.Eq(sp.expand(t),0),x) if v.is_real],key=lambda v: float(v))
def pq(t):
    P=sp.Poly(sp.expand(t),x); return (P.coeff_monomial(x), P.coeff_monomial(1))
# 17 Formen
for nr,f in [("17a","nur x^2"),("17b","Normalform"),("17c","Produkt=0"),("17d","Klammer im Quadrat"),("17e","Normalform")]:
    pruef(nr,f,f)
# 18 p und q
for nr,t,soll in [("18a",x**2+10*x+3,(10,3)),("18b",x**2-4*x+9,(-4,9)),("18c",x**2+7*x-5,(7,-5)),
                  ("18d",x**2-9*x-2,(-9,-2)),("18e",x**2-x+6,(-1,6)),("18f",x**2+15-8*x,(-8,15))]:
    pruef(nr,pq(t),soll)
# 19 Vorzahl
for nr,a,soll in [("19a",1,"nein"),("19b",3,"ja, durch 3"),("19c",1,"nein"),("19d",-1,"ja, durch -1"),("19e",5,"ja, durch 5")]:
    pruef(nr,"nein" if a==1 else f"ja, durch {a}",soll)
# 20 rechnen
for nr,t,soll in [("20-Bsp",x**2+6*x-16,[-8,2]),("20a",x**2+8*x+15,[-5,-3]),("20b",x**2+10*x+21,[-7,-3]),
                  ("20c",x**2+6*x+5,[-5,-1]),("20d",x**2+12*x+32,[-8,-4]),("20e",x**2+4*x-21,[-7,3]),
                  ("20f",x**2-10*x+24,[4,6]),("20g",x**2-2*x-35,[-5,7]),("20h",x**2+5*x+6,[-3,-2])]:
    pruef(nr,loes(t),soll)
# 21 wie viele Loesungen
def disk(t):
    p,q=pq(t); return sp.nsimplify(sp.Rational(p,2)**2-q)
pruef("21a-D",disk(x**2-14*x+49),0); pruef("21a",loes(x**2-14*x+49),[7])
pruef("21b-D",disk(x**2+4*x+9),-5); pruef("21b",loes(x**2+4*x+9),[])
pruef("21c-D",disk(x**2-8*x+11),5); pruef("21c",loes(x**2-8*x+11),[4-sp.sqrt(5),4+sp.sqrt(5)])
pruef("21c-nah",[round(float(4-math.sqrt(5)),2),round(float(4+math.sqrt(5)),2)],[1.76,6.24])
# 22 ordnen
pruef("22a-norm",sp.expand(x**2+5*x-24),sp.expand(x**2+5*x-24)); pruef("22a",loes(x**2+5*x-24),[-8,3])
pruef("22b-norm",sp.expand(x**2-7*x-18),sp.expand(x**2-7*x-18)); pruef("22b",loes(x**2-7*x-18),[-2,9])
pruef("22c-norm",sp.expand((x+3)**2-(4*x+21)),sp.expand(x**2+2*x-12))
pruef("22c",loes((x+3)**2-(4*x+21)),[-1-sp.sqrt(13),-1+sp.sqrt(13)])
pruef("22c-nah",[round(float(-1-math.sqrt(13)),2),round(float(-1+math.sqrt(13)),2)],[-4.61,2.61])
# 23 normieren
pruef("23a-norm",sp.expand((2*x**2+14*x+12)/2),sp.expand(x**2+7*x+6)); pruef("23a",loes(2*x**2+14*x+12),[-6,-1])
pruef("23b-norm",sp.expand((3*x**2-18*x+24)/3),sp.expand(x**2-6*x+8)); pruef("23b",loes(3*x**2-18*x+24),[2,4])
pruef("23c-norm",sp.expand(-(-x**2+2*x+8)),sp.expand(x**2-2*x-8)); pruef("23c",loes(-x**2+2*x+8),[-2,4])
pruef("23-Bsp",loes(2*x**2-6*x-20),[-2,5])
# 24 Probe
pruef("24a",loes(x**2-9*x+20),[4,5]); pruef("24a-probe",sp.simplify((x**2-9*x+20).subs(x,5)),0)
pruef("24b",loes(x**2+3*x-10),[-5,2]); pruef("24b-probe",sp.simplify((x**2+3*x-10).subs(x,-5)),0)
# 25 aus der Pruefung
pruef("25a-norm",sp.expand((2*x**2+14*x+24)/2),sp.expand(x**2+7*x+12)); pruef("25a",loes(2*x**2+14*x+24),[-4,-3])
pruef("25b-norm",sp.expand(-(-x**2-4*x+7+5)),sp.expand(x**2+4*x-12)); pruef("25b",loes(-x**2-4*x+7+5),[-6,2])
pruef("25c",loes(x**2-10*x+23),[5-sp.sqrt(2),5+sp.sqrt(2)])
pruef("25c-nah",[round(float(5-math.sqrt(2)),2),round(float(5+math.sqrt(2)),2)],[3.59,6.41])
# 26 Fehler finden
pruef("26-falsch",[-6,-2],[-6,-2]); pruef("26-richtig",loes(x**2-8*x+12),[2,6])
pruef("26a",loes(x**2-12*x+27),[3,9])
# 27 Begruenden
pruef("27b-D",disk(x**2+6*x+11),-2); pruef("27b",loes(x**2+6*x+11),[])
# 28 Loesungsweg
for nr,w in [("28a","Wurzelziehen"),("28b","Nullprodukt"),("28c","Lösungsformel"),("28d","Wurzelziehen"),("28e","Nullprodukt")]:
    pruef(nr,w,w)
pruef("28b-kontrolle",loes(x**2-15*x),[0,15])
pruef("28d-kontrolle",sorted([sp.nsimplify(v) for v in sp.solve(sp.Eq((x-4)**2,49),x)],key=float),[-3,11])
pruef("28e-kontrolle",loes((x+2)*(x-11)),[-2,11])
pruef("28a-kontrolle",sorted([sp.nsimplify(v) for v in sp.solve(sp.Eq(x**2,144),x)],key=float),[-12,12])
pruef("28c-kontrolle",loes(x**2+9*x+14),[-7,-2])
open("pruef_out_e3.txt","w").write("\n".join(zeilen)+f"\nAbweichungen: {abw}\n")
print("\n".join([z for z in zeilen if "ABWEICHUNG" in z])); print("Abweichungen:",abw)
