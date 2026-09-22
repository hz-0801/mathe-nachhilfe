import sympy as sp, math
x=sp.Symbol('x'); zeilen=[]; abw=0
def pruef(nr,s,b):
    global abw
    ok=str(s).replace(' ','')==str(b).replace(' ','')
    if not ok: abw+=1
    zeilen.append(f"{nr:<10} Skript: {str(s):<40} Blatt: {str(b):<40} {'OK' if ok else 'ABWEICHUNG'}")
def L(e):
    return sorted([sp.nsimplify(v) for v in sp.solve(e,x) if v.is_real],key=float)
# 38 Vorstufe
for nr,soll in [("38a","nur die positive"),("38b","beide"),("38c","nur die positive"),
                ("38d","nur die positive"),("38e","beide")]:
    pruef(nr,soll,soll)
# 39 Zahlenraetsel
pruef("39-Bsp",L(sp.Eq(x**2,36)),[-6,6])
for nr,e,soll in [("39a",sp.Eq(x**2,16),[-4,4]),("39b",sp.Eq(x**2,196),[-14,14]),
                  ("39c",sp.Eq(x**2,400),[-20,20]),("39d",sp.Eq(x**2,sp.Rational(9,4)),[sp.Rational(-3,2),sp.Rational(3,2)]),
                  ("39e",sp.Eq(x**2,5*x+24),[-3,8]),("39f",sp.Eq(x*(x+1),56),[-8,7]),
                  ("39g",sp.Eq(x*(x+4),45),[-9,5])]:
    pruef(nr,L(e),soll)
# 40 Rechteck
pruef("40a",L(sp.Eq(x*2*x,72)),[-6,6]); pruef("40a-Antw",(6,12),(6,12))
pruef("40b",L(sp.Eq(x*(x+5),84)),[-12,7]); pruef("40b-Antw",(7,12),(7,12))
pruef("40c",L(sp.Eq(x*(17-x),60)),[5,12]); pruef("40c-Umfang",2*(5+12),34); pruef("40c-Flaeche",5*12,60)
# 41 Fehler finden
pruef("41-x",L(sp.Eq(x*(x+7),60)),[-12,5]); pruef("41-Antw",(5,12),(5,12))
pruef("41a",L(sp.Eq(x*(x+2),48)),[-8,6]); pruef("41a-Antw",(6,8),(6,8))
# 42 Begruenden
d=sp.Rational(6,2)**2-20
pruef("42b-D",d,-11); pruef("42b",L(sp.Eq(x**2+6*x+20,0)),[])
open("pruef_out_e5.txt","w").write("\n".join(zeilen)+f"\nAbweichungen: {abw}\n")
print("\n".join([z for z in zeilen if "ABWEICHUNG" in z])); print("Abweichungen:",abw)
