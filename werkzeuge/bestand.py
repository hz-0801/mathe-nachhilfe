#!/usr/bin/env python3
"""Bestandszählung: Aufgabenbank und Prüfungskataloge (reine Zählung).

Aufruf:  python3 werkzeuge/bestand.py <pfad-zum-bank-klon> > befund.md
Der Pfad zu mathe-nachhilfe ist die Wurzel über diesem Skript.
Sprosse = (einheit, kette_nr, sprosse) in bank/<eintrag>/e<n>.jsonl.
Zone (zone.jsonl) und weg.jsonl zählen getrennt. Ordner mit führendem
Unterstrich (_basis) bleiben außen vor. Kernmarke: kein Feld in der Bank;
ableitbar aus hoehe == "grundfall".
"""
import csv, json, os, sys, glob, re, collections

BANK = sys.argv[1]
MN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rows(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def teil_zw(s):
    """Zwischenergebnisse trennen an „ ; “ außerhalb von Klammern (seit 05.10.2026, werkzeuge/zwtrenner.py)."""
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import zwtrenner
    return zwtrenner.teile(s)


def num(s):
    try:
        return float(str(s).replace(",", "."))
    except ValueError:
        return None


# ---------- A ----------
A = []
for d in sorted(os.listdir(os.path.join(BANK, "bank"))):
    p = os.path.join(BANK, "bank", d)
    if d.startswith("_") or not os.path.isdir(p):
        continue
    r = dict(eintrag=d, aufg=0, zone=0, einheiten=set(), sprossen=collections.Counter(),
             grund=0, vorstufe_h=0, vorstufe_f=0, tipp=0, weg=0, v2=0, muster=os.path.exists(os.path.join(p, "muster.md")),
             ketten=set())
    for f in sorted(glob.glob(os.path.join(p, "*.jsonl"))):
        b = os.path.basename(f)
        rs = rows(f)
        if b == "zone.jsonl":
            r["zone"] += len(rs)
        elif b == "weg.jsonl":
            r["weg"] += len(rs)
        elif re.fullmatch(r"e\d+\.jsonl", b):
            for x in rs:
                r["aufg"] += 1
                r["einheiten"].add(x.get("einheit"))
                r["sprossen"][(x.get("einheit"), x.get("kette_nr"), x.get("sprosse"))] += 1
                r["ketten"].add((x.get("einheit"), x.get("kette_nr")))
                if x.get("hoehe") == "grundfall": r["grund"] += 1
                if x.get("hoehe") == "vorstufe": r["vorstufe_h"] += 1
                if x.get("vorstufe"): r["vorstufe_f"] += 1
                if x.get("tipp"): r["tipp"] += 1
                if (x.get("variante") or 0) >= 2: r["v2"] += 1
    sp = r["sprossen"]
    r["n_spr"] = len(sp)
    r["s1"] = sum(1 for v in sp.values() if v == 1)
    r["s2"] = sum(1 for v in sp.values() if v == 2)
    r["s3"] = sum(1 for v in sp.values() if v >= 3)
    r["luecke"] = r["s1"] + r["s2"]
    A.append(r)
A.sort(key=lambda r: (-r["luecke"], r["eintrag"]))

o = []
w = o.append
w("# Befund Bestand (Zählung, ohne Urteil)\n")
w("Quelle A: Klon aufgabenbank, `bank/<eintrag>/` ohne `_basis`. Quelle B: Kataloge in mathe-nachhilfe. Erzeugt von `werkzeuge/bestand.py`.\n")
w("## A. Aufgabenbank je Eintrag\n")
w("Aufg = Zeilen in e<n>.jsonl; Zone = Zeilen zone.jsonl; Einh = Einheiten; Spr = Sprossen (Einheit, Kette, Sprosse); S1/S2/S3+ = Sprossen mit 1, 2, mindestens 3 Aufgaben (S3+ = Ersatz-fähig: nach der Blattaufgabe bleiben zwei für Rückblick und Check); Lücke = S1+S2; Vst-h = Zeilen mit hoehe vorstufe; Vst-f = Feld vorstufe; Tipp = Feld tipp; Weg = Zeilen weg.jsonl (angefangene Lösung/Weg); v2+ = Zeilen mit Variante ab 2; Kern = Zeilen hoehe grundfall; Mu = muster.md vorhanden.\n")
w("| Eintrag | Aufg | Zone | Einh | Spr | S1 | S2 | S3+ | Lücke | Vst-h | Vst-f | Tipp | Weg | v2+ | Kern | Mu |")
w("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:-:|")
T = collections.Counter()
for r in A:
    w("| {eintrag} | {aufg} | {zone} | {ne} | {n_spr} | {s1} | {s2} | {s3} | {luecke} | {vorstufe_h} | {vorstufe_f} | {tipp} | {weg} | {v2} | {grund} | {mu} |".format(
        ne=len(r["einheiten"]), mu="ja" if r["muster"] else "nein", **r))
    for k in ("aufg", "zone", "n_spr", "s1", "s2", "s3", "luecke", "vorstufe_h", "vorstufe_f", "tipp", "weg", "v2", "grund"):
        T[k] += r[k]
    T["einh"] += len(r["einheiten"]); T["mu"] += 1 if r["muster"] else 0
w("| **Summe ({} Einträge)** | {aufg} | {zone} | {einh} | {n_spr} | {s1} | {s2} | {s3} | {luecke} | {vorstufe_h} | {vorstufe_f} | {tipp} | {weg} | {v2} | {grund} | {mu} |".format(len(A), **T))
w("\nKernmarke: kein Feld in der Bank (Feldliste bank.md); ableitbar aus `hoehe == \"grundfall\"` (Spalte Kern), bei Bedarf plus `kette_nr`/`sprosse == 1`.\n")
w("Verteilung Aufgaben je Sprosse (alle Einträge): " + ", ".join(
    f"{k}: {v}" for k, v in sorted(collections.Counter(min(c, 6) for r in A for c in r["sprossen"].values()).items())) + " (6 = 6 und mehr)\n")
w("### Einträge ohne muster.md\n")
ohne = [r for r in A if not r["muster"]]
w(f"{len(ohne)} von {len(A)}: " + (", ".join(r["eintrag"] + f" ({r['aufg']})" for r in ohne) or "keine") + "\n")
w("### Einträge mit vielen Sprossen unter 3 Aufgaben\n")
w("Kriterium (Zählgrenze): mindestens 10 Sprossen unter 3 und mindestens die Hälfte aller Sprossen; Eintrag mit Anteil unter 3 und Zahl.\n")
w("| Eintrag | Spr | unter 3 | Anteil |\n|---|--:|--:|--:|")
viele = [r for r in A if r["luecke"] >= 10 and r["luecke"] * 2 >= r["n_spr"]]
for r in viele:
    w(f"| {r['eintrag']} | {r['n_spr']} | {r['luecke']} | {100*r['luecke']/r['n_spr']:.0f} % |")
if not viele: w("| (keiner) | | | |")
w(f"\n{len(viele)} Einträge. Einträge ohne jede Sprosse unter 3: " + (", ".join(r["eintrag"] for r in A if r["luecke"] == 0 and r["n_spr"]) or "keine") + "\n")

# ---------- B ----------
KAT = ["msa/msa-katalog-basis.csv", "msa/msa-katalog-kontext.csv", "msa/msa-katalog-gym.csv",
       "abitur/abi-katalog.csv", "abitur/iqb-katalog.csv", "fhr/fhr-katalog.csv"]
w("## B. Prüfungskataloge (mathe-nachhilfe)\n")
w("Zeilen = Katalogzeilen; KL/ZW/NB/SW = Zahl Zeilen mit gefüllter kurzloesung/zwischenergebnis/neben/stichwoerter; ZW0..ZW3+ = Verteilung der Zwischenergebnisse je Zeile (Trenner ` ; `, nicht innerhalb von (…), […], ⟨…⟩); ZW>P-1 = Zeilen mit mehr Zwischenergebnissen als punkte − 1, Anteil an Zeilen mit lesbaren Punkten (P-ok).\n")
w("| Katalog | Papier | Zeilen | KL | ZW | NB | SW | ZW0 | ZW1 | ZW2 | ZW3+ | P-ok | ZW>P-1 | Anteil |")
w("|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|")
GT = collections.Counter()
for k in KAT:
    path = os.path.join(MN, k)
    with open(path, encoding="utf-8", newline="") as f:
        rd = list(csv.DictReader(f, delimiter=";", quotechar='"'))
    by = collections.defaultdict(collections.Counter)
    for x in rd:
        pap = x.get("papier", "") or "(leer)"
        for scope in (pap, "_ges"):
            c = by[scope]
            c["z"] += 1
            for col, key in (("kurzloesung", "kl"), ("zwischenergebnis", "zw"), ("neben", "nb"), ("stichwoerter", "sw")):
                if (x.get(col) or "").strip(): c[key] += 1
            n = len(teil_zw(x.get("zwischenergebnis")))
            c["n%d" % min(n, 3)] += 1
            p = num(x.get("punkte"))
            if p is not None:
                c["pok"] += 1
                if n > p - 1: c["gt"] += 1
    name = os.path.basename(k)
    for scope in sorted(s for s in by if s != "_ges") + ["_ges"]:
        c = by[scope]
        an = f"{100*c['gt']/c['pok']:.0f} %" if c["pok"] else "-"
        lab = "**alle**" if scope == "_ges" else scope
        w(f"| {name} | {lab} | {c['z']} | {c['kl']} | {c['zw']} | {c['nb']} | {c['sw']} | {c['n0']} | {c['n1']} | {c['n2']} | {c['n3']} | {c['pok']} | {c['gt']} | {an} |")
        if scope == "_ges":
            for kk, v in c.items(): GT[kk] += v
an = f"{100*GT['gt']/GT['pok']:.0f} %" if GT["pok"] else "-"
w(f"| **alle Kataloge** | | {GT['z']} | {GT['kl']} | {GT['zw']} | {GT['nb']} | {GT['sw']} | {GT['n0']} | {GT['n1']} | {GT['n2']} | {GT['n3']} | {GT['pok']} | {GT['gt']} | {an} |")
print("\n".join(o))
