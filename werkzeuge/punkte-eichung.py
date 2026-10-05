"""Punkte-Eichung: Taugt die Faustregel fuer Zwischenergebnisse auf dem
Loesungsblatt? Liest werkzeuge/punkte-eichung.csv, gibt Quoten aus.

(a)  mit_ergebnis - 1 <= be - 1   (bepunktete Ergebnisse sprengen BE nicht)
(a2) erg_ewh <= be                (alle Ergebnisse, die der Erwartungshorizont
                                   hinschreibt, passen unter BE)
(b)  mit_ergebnis == handgriffe
(c)  |mit_ergebnis - handgriffe| <= 1
Aufruf: python3 werkzeuge/punkte-eichung.py
"""
import csv, collections, pathlib

pfad = pathlib.Path(__file__).with_name("punkte-eichung.csv")
zeilen = list(csv.DictReader(pfad.open(encoding="utf-8"), delimiter=";"))

def tests(z):
    be, m, e, h = (int(z[k]) for k in ("be", "mit_ergebnis", "erg_ewh", "handgriffe"))
    return {"a": m - 1 <= be - 1, "a2": e <= be, "b": m == h, "c": abs(m - h) <= 1}

def quote(gruppe):
    n = len(gruppe)
    t = [tests(z) for z in gruppe]
    return n, {k: sum(x[k] for x in t) for k in ("a", "a2", "b", "c")}

def zeile(name, gruppe):
    n, s = quote(gruppe)
    teile = "  ".join(f"{k}: {s[k]:>2}/{n:<2} {100*s[k]/n:5.1f} %" for k in s)
    print(f"{name:<12} n={n:<3} {teile}")

print("Gesamt")
zeile("alle", zeilen)
for z in zeilen:
    z["be_band"] = "BE 1-4" if int(z["be"]) <= 4 else "BE 5-8"
for feld in ("stufe", "antwortart", "be_band"):
    print(f"\nje {feld}")
    gr = collections.defaultdict(list)
    for z in zeilen:
        gr[z[feld]].append(z)
    for k in sorted(gr):
        zeile(k, gr[k])

print("\nPunkte ohne Ergebnis (BE-Stellen je Art)")
arten = collections.Counter()
for z in zeilen:
    if int(z["ohne_ergebnis"]):
        art = z["ohne_art"].split(" (")[0]
        arten[art] += int(z["ohne_ergebnis"])
for art, n in arten.most_common():
    print(f"  {n:>2}  {art}")
ohne = sum(int(z["ohne_ergebnis"]) for z in zeilen)
be = sum(int(z["be"]) for z in zeilen)
print(f"  zusammen {ohne} von {be} BE ({100*ohne/be:.1f} %)")

print("\nDifferenz mit_ergebnis - handgriffe")
d = collections.Counter(int(z["mit_ergebnis"]) - int(z["handgriffe"]) for z in zeilen)
for k in sorted(d):
    print(f"  {k:+d}: {d[k]}")
print("\nAbweichung > 1:")
for z in zeilen:
    diff = int(z["mit_ergebnis"]) - int(z["handgriffe"])
    if abs(diff) > 1:
        print(f"  {z['id']}: BE {z['be']}, mit {z['mit_ergebnis']}, Handgriffe {z['handgriffe']}")

# Gegenprobe mit bekannten Werten: Zeilenzahl und BE-Summe der Stichprobe
assert len(zeilen) == 46, len(zeilen)
assert all(int(z["mit_ergebnis"]) + int(z["ohne_ergebnis"]) == int(z["stellen"]) for z in zeilen)
