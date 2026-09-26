# pruef.py – rechnet die Lösungen des Blatts „Daten" (Kl. 7) unabhängig nach.
# Aufruf: python pruef.py zone | e1 | e2   → schreibt pruef_out_<teil>.txt
# Blattwerte sind aus den Lösungsquelltexten (zone_l.tex, e1_l.tex, e2_l.tex) übertragen.
import sys
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction as F
from statistics import median

def rnd(x, n=1):
    q = Decimal(1).scaleb(-n)
    return float(Decimal(str(float(x))).quantize(q, rounding=ROUND_HALF_UP))

def pct(teil, ganz, n=None):
    v = F(teil, 1) / F(ganz, 1) * 100 if not isinstance(teil, F) else teil / ganz * 100
    return rnd(v, n) if n is not None else float(v)

def winkel(anteil):          # Anteil als Fraction oder Prozentzahl
    return float(anteil * 360)

def quartile(liste):
    s = sorted(liste); n = len(s)
    h = n // 2
    unten = s[:h]; oben = s[h + (n % 2):]
    return [s[0], median(unten), median(s), median(oben), s[-1]]

checks = {}

# ---------------- Zone ----------------
z = []
z += [("1a", pct(3, 10), 30), ("1b", pct(1, 4), 25), ("1c", pct(9, 20), 45),
      ("1d", pct(7, 8), 87.5), ("1e", pct(5, 12, 1), 41.7)]
z += [("2a", 0.5, 0.5), ("2b", 25/100, 0.25), ("2c", 12.5/100, 0.125), ("2d", 5/100, 0.05)]
strich = {"Rad": 8, "Bus": 6, "Fuss": 4, "Auto": 2}
z += [("3a", strich["Rad"], 8), ("3b", sum(strich.values()), 20),
      ("3c Bruch", float(F(8, 20)), float(F(2, 5))), ("3c %", pct(8, 20), 40),
      ("3d", pct(14, 400), 3.5), ("3e Bruch", float(F(12, 48)), 0.25), ("3e %", pct(12, 12 + 36), 25)]
z += [("4a", 4, 4), ("4b", 3, 3), ("4c", 2.75, 2.75), ("4d", 3.5 * 1000, 3500)]
z += [("5a", float(F(180, 360)), 0.5), ("5b", float(F(90, 360)), 0.25), ("5c", float(F(120, 360)), 1/3),
      ("5d", float(F(45, 360)), 0.125), ("5e", winkel(F(1, 5)), 72)]
z += [("7a", 3 * 10, 30), ("7b", 50 / 10, 5), ("7c", 4.5 * 10, 45), ("7d", 7 / 10, 0.7), ("7f", 3.5 * 10, 35)]
q = [12, 7, 15, 9, 11]
z += [("8a", min(q), 7), ("8b", max(q), 15), ("8c", max(q) - min(q), 8), ("8d", median(q), 11),
      ("8e", median([8, 3, 10, 5, 6, 12]), 7)]
z += [("9a", 80 / 2, 40), ("9b", 35 * 2, 70), ("9c", 150 * 2 / 3, 100), ("9d", 120 * F(4, 3), 160),
      ("9e", 200 * F(3, 4), 150)]
z += [("10 richtig", pct(10, 25), 40), ("11a", pct(14, 40), 35), ("11b", pct(18, 18 + 42), 30)]
checks["zone"] = z

# ---------------- Einheit 1 (Katalog-Einheit 3) ----------------
e = []
e += [("14a", 30 / 10, 3), ("14b", 60 / 10, 6), ("14c", 90 / 10, 9), ("14d", 20 / 10, 2),
      ("14e", 45 / 10, 4.5), ("14f mm", 8, 8)]
e += [("15a", 70 / 10 + 30 / 10, 10), ("15b Summe", 45 + 35 + 20, 100),
      ("15c zu Fuss", 100 - 35 - 40, 25), ("15d Summe", 45 + 25 + 5 + 25, 100),
      ("15d Wasser cm", 5 / 10, 0.5)]
e += [("16a", winkel(F(50, 100)), 180), ("16b", winkel(F(25, 100)), 90), ("16c", winkel(F(10, 100)), 36),
      ("16d", winkel(F(75, 100)), 270), ("16e", winkel(F(15, 100)), 54), ("16f", winkel(F(5, 100)), 18),
      ("16g", winkel(F(3, 8)), 135), ("16h", winkel(F(27, 120)), 81), ("16i", winkel(F(14, 400)), 12.6),
      ("16j", rnd(winkel(F(5, 13)), 1), 138.5)]
e += [("17c", winkel(F(40, 100)), 144)]
e += [("18a", [winkel(F(p, 100)) for p in (50, 25, 25)], [180, 90, 90]),
      ("18b", [winkel(F(p, 100)) for p in (55, 30, 15)], [198, 108, 54]),
      ("18c", [winkel(F(k, 24)) for k in (12, 8, 4)], [180, 120, 60])]
e += [("19a", float(F(180, 360)), 0.5), ("19b", float(F(90, 360)), 0.25), ("19c", float(F(120, 360)), 1/3),
      ("19d", float(F(60, 360)), 1/6), ("19e", pct(144, 360), 40)]
# 20/21: Reihenfolge der Sektoren ab oben im Uhrzeigersinn = Reihenfolge im Quelltext; Zuordnung nach Größe
e += [("21d Summe", 175 + 130 + 72 + 17 + 96, 490), ("21d Winkel", rnd(winkel(F(17, 490)), 1), 12.5)]
e += [("22a richtig", winkel(F(20, 100)), 72), ("22a falsch", 20, 20), ("22b richtig", winkel(F(15, 100)), 54),
      ("22b falsch", 400 * 15 / 100, 60)]
e += [("23a", 360 / 100, 3.6), ("23b Summe", 45 + 35 + 30, 110)]
st = {"Kletterpark": 96, "Zoo": 60, "Schwimmbad": 51, "Museum": 33}
g = sum(st.values())
e += [("24 Summe", g, 240)]
blatt24 = {"Kletterpark": (40, 144), "Zoo": (25, 90), "Schwimmbad": (21.25, 76.5), "Museum": (13.75, 49.5)}
for k, v in st.items():
    e += [(f"24a {k} %", pct(v, g), blatt24[k][0]), (f"24a {k} °", winkel(F(v, g)), blatt24[k][1])]
e += [("24c Ziele >= 25 %", sorted(k for k, v in st.items() if F(v, g) >= F(1, 4)), sorted(["Kletterpark", "Zoo"]))]
checks["e1"] = e

# ---------------- Einheit 2 (Katalog-Einheit 5) ----------------
f = []
zoo = {2019: 56, 2020: 50, 2021: 44, 2022: 46, 2023: 40, 2024: 36}
f += [("26a", zoo[2019] == 56, True), ("26b", zoo[2023] == 44, False), ("26c", zoo[2021] < zoo[2022], True),
      ("26d 50 Besucher", zoo[2020] * 1000 == 50, False), ("26e", zoo[2023] - zoo[2024] == 4, True),
      ("26f", all(zoo[y + 1] < zoo[y] for y in range(2019, 2024)), False)]
fach = {"Sport": 76, "Mathematik": 40, "Kunst": 30, "Deutsch": 22, "Musik": 12}
n = sum(fach.values())
f += [("27 Summe", n, 180), ("27a", fach["Sport"] > n / 2, False),
      ("27b", fach["Mathematik"] == fach["Kunst"] * F(4, 3), True),
      ("27c", fach["Musik"] == n / 15, True), ("27d", fach["Musik"] == n * 15 / 100, False),
      ("27d Anteil", pct(fach["Musik"], n, 1), 6.7),
      ("27f", fach["Sport"] == max(fach.values()) and fach["Deutsch"] == fach["Mathematik"] / 2, False)]
f += [("28a Höhe über 400", (440 - 400) / (420 - 400), 2), ("28b", pct(20, 420, 1), 4.8)]
f += [("29c", pct(F(160 - 120, 1), 120, 1), 33.3)]
dvd = {2019: 520, 2020: 440, 2021: 360, 2022: 280, 2023: 200, 2024: 160}
f += [("30a Rückgänge", [dvd[y] - dvd[y + 1] for y in range(2019, 2024)], [80, 80, 80, 80, 40]),
      ("30b mit -80", dvd[2024] - 2 * 80, 0), ("30b mit -40", dvd[2024] - 2 * 40, 80)]
kino = {2019: 122, 2020: 112, 2021: 116, 2022: 104, 2023: 98, 2024: 96}
f += [("31a jedes Jahr weniger", all(kino[y + 1] < kino[y] for y in range(2019, 2024)), False),
      ("31a Mio. über 90 (2019/2024)", [kino[2019] - 90, kino[2024] - 90], [32, 6]),
      ("31a mehr als fünfmal", (kino[2019] - 90) / (kino[2024] - 90) > 5, True),
      ("31a Rückgang %", pct(kino[2019] - kino[2024], kino[2019], 0), 21)]
bp = [260, 310, 340, 380, 450]
f += [("32a", bp[0], 260), ("32b", bp[4], 450), ("32c", bp[2], 340), ("32d", [bp[1], bp[3]], [310, 380]),
      ("32e", bp[4] - bp[0], 190), ("32f", 75, 75)]
f += [("33a", [3, 6, 9, 12, 18], [3, 6, 9, 12, 18]),
      ("33b", quartile([4, 6, 7, 9, 11, 12, 14, 17]), [4, 6.5, 10, 13, 17]),
      ("33c", quartile([15, 8, 11, 5, 19, 10, 13, 7, 12, 16, 9, 14]), [5, 8.5, 11.5, 14.5, 19])]
a7, b7 = [6, 10, 13, 15, 19], [9, 11, 12, 14, 16]
f += [("34a Mediane", [a7[2], b7[2]], [13, 12]), ("34b Spannweiten", [a7[4] - a7[0], b7[4] - b7[0]], [13, 7]),
      ("34c Boxbreiten", [a7[3] - a7[1], b7[3] - b7[1]], [5, 3])]
f += [("35a", rnd((95 - 80) / (85 - 80), 0), 3), ("35a mehr %", pct(10, 85, 1), 11.8),
      ("35b Spannweite", 41 - 12, 29), ("35b Box", 35 - 20, 15)]
f += [("37a A", [990 - 960, pct(30, 960, 1)], [30, 3.1]), ("37a B", [440 - 400, pct(40, 400, 1)], [40, 10]),
      ("37b Höhen über 950", (990 - 950) / (960 - 950), 4)]
checks["e2"] = f

def gleich(a, b):
    if isinstance(a, (list, tuple)):
        return len(a) == len(b) and all(gleich(x, y) for x, y in zip(a, b))
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(a, str):
        return a == b
    return abs(float(a) - float(b)) < 1e-6

teil = sys.argv[1]
zeilen, abw = [], 0
for nr, s, b in checks[teil]:
    ok = gleich(s, b)
    abw += 0 if ok else 1
    zeilen.append(f"{nr}\tSkript: {s}\tBlatt: {b}\t{'OK' if ok else 'ABWEICHUNG'}")
zeilen.append(f"Abweichungen: {abw}")
out = "\n".join(zeilen)
open(f"pruef_out_{teil}.txt", "w", encoding="utf-8").write(out + "\n")
print(out)
