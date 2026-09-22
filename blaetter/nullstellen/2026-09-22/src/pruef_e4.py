import sympy as sp, math
x=sp.Symbol('x'); zeilen=[]; abw=0
def pruef(nr,s,b):
    global abw
    ok=str(s).replace(' ','')==str(b).replace(' ','')
    if not ok: abw+=1
    zeilen.append(f"{nr:<10} Skript: {str(s):<44} Blatt: {str(b):<44} {'OK' if ok else 'ABWEICHUNG'}")
def NS(t):
    return sorted([sp.nsimplify(v) for v in sp.solve(sp.Eq(sp.expand(t),0),x) if v.is_real],key=float)
def SP(p,f):
    xs=sorted([sp.nsimplify(v) for v in sp.solve(sp.Eq(sp.expand(p),sp.expand(f)),x) if v.is_real],key=float)
    return [(v,sp.simplify(f.subs(x,v))) for v in xs]
# 29 Vorstufe
for nr,g in [("29a","x^2-5x+4=0"),("29b","x^2+2x=3x+6"),("29c","x^2-4x=12"),
             ("29d","(x-7)^2-9=0"),("29e","(x+1)^2=-x+5")]:
    pruef(nr,g,g)
# 30
pruef("30-Bsp",NS((x-4)**2-9),[1,7])
for nr,t,soll in [("30a",(x-3)**2-16,[-1,7]),("30b",(x+2)**2-25,[-7,3]),("30c",(x-5)**2-4,[3,7]),
                  ("30d",(x+6)**2-1,[-7,-5]),("30e",(x-8)**2,[8]),("30f",(x-2)**2+5,[]),
                  ("30g",-(x-1)**2+9,[-2,4]),("30h",(x+4)**2+2,[]),("30i",-(x-3)**2+7,[3-sp.sqrt(7),3+sp.sqrt(7)])]:
    pruef(nr,NS(t),soll)
pruef("30i-anz",len(NS(-(x-3)**2+7)),2)
# 31
pruef("31-Bsp",NS(x**2-2*x-15),[-3,5])
for nr,t,soll in [("31a",x**2-7*x+10,[2,5]),("31b",x**2+9*x+20,[-5,-4]),("31c",x**2-3*x-18,[-3,6]),
                  ("31d",x**2+2*x-24,[-6,4]),("31e",2*x**2-10*x+12,[2,3]),("31f",3*x**2+3*x-18,[-3,2]),
                  ("31g",x**2-4*x+1,[2-sp.sqrt(3),2+sp.sqrt(3)]),("31h",x**2-8*x+14,[4-sp.sqrt(2),4+sp.sqrt(2)])]:
    pruef(nr,NS(t),soll)
pruef("31g-nah",[round(float(2-math.sqrt(3)),2),round(float(2+math.sqrt(3)),2)],[0.27,3.73])
pruef("31h-nah",[round(float(4-math.sqrt(2)),2),round(float(4+math.sqrt(2)),2)],[2.59,5.41])
# 32 Grafik p=(x-1)^2-4, f=x-3
p32=(x-1)**2-4; f32=3*x-7
pruef("32a",NS(p32),[-1,3])
pruef("32b",SP(p32,f32),[(1,-4),(4,5)])
pruef("32-Bereich",all(-3<=v<=6 for v in [-1,3,1,4]) and all(-5<=w<=6 for w in [0,0,-4,5]),True)
# 33 Argument
for nr,p,c,soll in [("33a",x**2+4*x,12,[-6,2]),("33b",x**2-6*x,7,[-1,7]),("33c",-x**2-2*x+7,-8,[-5,3])]:
    pruef(nr,sorted([sp.nsimplify(v) for v in sp.solve(sp.Eq(p,c),x) if v.is_real],key=float),soll)
# 34 Schnittpunkte
pruef("34-Bsp",SP(x**2+3*x+1,x+9),[(-4,5),(2,11)])
for nr,p,f,soll in [("34a",x**2+5*x,2*x+4,[(-4,-4),(1,6)]),("34b",x**2-4,3*x+6,[(-2,0),(5,21)]),
                    ("34c",x**2+2*x+3,6*x+3,[(0,3),(4,27)]),("34d",(x-2)**2+2,2*x+1,[(1,3),(5,11)]),
                    ("34e",(x-4)**2-5,-3*x+11,[(0,11),(5,-4)])]:
    pruef(nr,SP(p,f),soll)
pruef("34f",SP(x**2+x-3,2*x**2-5*x+5),[(2,3),(4,17)])
# 35 Punktprobe
def pp(t,xv): return sp.simplify(t.subs(x,xv))
pruef("35a",(pp(x**2-5,3),pp(2*x-2,3)),(4,4))
pruef("35b",(pp(x**2-3,-2),pp(-x-1,-2)),(1,1))
pruef("35c",(pp(x**2+3*x-4,1),pp(2*x-1,1)),(0,1))
# 36 Fehler finden
pruef("36-x",SP(x**2+4*x,x+4),[(-4,0),(1,5)])
pruef("36a",SP(x**2-2*x,x+4),[(-1,3),(4,8)])
# 37 Begruenden
pruef("37b-Scheitel",sp.simplify(sp.expand((x-3)**2-4)-(x**2-6*x+5)),0)
open("pruef_out_e4.txt","w").write("\n".join(zeilen)+f"\nAbweichungen: {abw}\n")
print("\n".join([z for z in zeilen if "ABWEICHUNG" in z])); print("Abweichungen:",abw)
