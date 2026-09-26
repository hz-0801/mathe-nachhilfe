# zaehl.py – Zählung aus der Textextraktion (Hauptnummern, Teilaufgaben, Seiten, Kopfzeilen, Seitenfüllung)
import re, sys, statistics
GRAF = r"\\(streifen|streifenleer|streifenfeld|bruchrechteck|zahlenstrahl|dreieckrw|begin\{dreisatz\}|sachtabelle)\b"

def quelle(dateien):
    n = 0
    for d in dateien:
        n += len(re.findall(GRAF, open(d, encoding="utf-8").read()))
    return n

def zaehle(txt, loesung=False):
    seiten = open(txt, encoding="utf-8").read().split("\f")
    seiten = [s for s in seiten if s.strip()]
    nummern, teile, kopf, fuell = [], 0, [], []
    for s in seiten:
        zeilen = s.splitlines()
        kopf.append(zeilen[0].strip() if zeilen else "")
        if loesung:
            nummern += [int(m) for m in re.findall(r"(?m)^\s*(\d+)\)\s", s)]
        else:
            nummern += [int(m) for m in re.findall(r"(?m)^\s*(\d+)\.\s+Ich", s)]
            teile += len(re.findall(r"(?:^|\s)([a-z])\)\s", s))
        fuell.append(len(re.sub(r"\s+", "", s)))
    return seiten, nummern, teile, kopf, fuell

for name, txt, src, loes in [("Zone", "z.txt", ["zone_a.tex"], False),
                             ("Lernblatt", "lernblatt.txt", ["e1_a.tex", "e2_a.tex", "e3_a.tex", "e4_a.tex"], False),
                             ("Gesamt", "gesamt.txt", ["zone_a.tex", "e1_a.tex", "e2_a.tex", "e3_a.tex", "e4_a.tex"], False),
                             ("Lösungen", "loesungen.txt", [], True)]:
    seiten, nr, teile, kopf, fuell = zaehle(txt, loes)
    lauf = nr == list(range(nr[0], nr[0] + len(nr))) if nr else False
    print(f"{name}: Seiten {len(seiten)} · Nummern {len(nr)} ({nr[0] if nr else '-'}–{nr[-1] if nr else '-'}, durchlaufend: {lauf}) · Teilaufgaben {teile} · Grafiken (Quelle) {quelle(src)}")
    if not loes:
        med = statistics.median(fuell[:-2] if name != "Zone" else fuell)
        leer = [i + 1 for i, f in enumerate(fuell) if f < med / 3]
        print(f"   Seiten unter 1/3 des Medians ({med:.0f} Zeichen): {leer}")
        print("   Kopfzeilen:", " | ".join(sorted(set(kopf))))
