# Prueft die Loesungen von Blatt 0 unabhaengig nach.
tests = []
def t(nr, skript, blatt):
    tests.append((nr, skript, blatt))

t("1a", 30/100*100, 30)
t("1b", 7/100*100, 7)
t("1c", 0.45*100, 45)
t("1d", 8/100, 0.08)
t("1e", 12/48*100, 25)
t("1f", 100-45-30, 25)
t("2a", 1, 1)  # Ordnung, s.u.
t("2g", 50/5, 10)
t("3a", 360, 360)
t("3b", 360/4, 90)
t("3c", 360/2, 180)
t("3d", 360/3, 120)
t("3e", 360/10, 36)
t("3f", 45/360, 1/8)
t("4a", 3*10, 30)
t("4b", 45/10, 4.5)
t("4c", 7.2*10, 72)
t("4d", 10*10, 100)
t("5a", 2.5+3.5, 6)
t("5b", 12/4, 3)
t("5c", 18.6+4.9+0.5, 24)
t("5d", 78/5, 15.6)
t("5e", 61.5/4, 15.375)
t("5f", round(61.5/4,1), 15.4)
t("5g", round(3847.6/100)*100, 3800)
t("6a", 60/2, 30)
t("6b", 90/3, 30)
t("6c", 70/4, 17.5)
t("6d", 2*45, 90)
t("6e", 210+210/3, 280)
t("6f", 1/25*100, 4)
t("7a", 27/36*100, 75)
t("7b", 21/60*100, 35)

ordnung = sorted([4.7,4.07,4.71,4.17]) == [4.07,4.17,4.7,4.71] and \
          sorted([12.5,9.8,12.05,9.75]) == [9.75,9.8,12.05,12.5]

ab = 0
out = []
for nr, s, b in tests:
    ok = abs(s-b) < 1e-9
    if not ok: ab += 1
    out.append(f"{nr}\t{s}\t{b}\t{'OK' if ok else 'ABWEICHUNG'}")
out.append(f"2a/2b Ordnung\t{ordnung}\tTrue\t{'OK' if ordnung else 'ABWEICHUNG'}")
if not ordnung: ab += 1
out.append(f"Abweichungen: {ab}")
open("pruef_out_blatt0.txt","w").write("\n".join(out)+"\n")
print("\n".join(out[-4:]))
