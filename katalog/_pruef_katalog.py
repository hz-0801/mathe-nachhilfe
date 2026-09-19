#!/usr/bin/env python3
"""Prüfung eines Katalogeintrags:
1. Kastenzahlen je Einheit gegen die Sprossen-Zeile und die Blatt-0-Zeilen derselben Einheit.
2. P10-Typen eines typen.csv-Themas gegen die Zuordnungszeilen der genannten Dateien.
Aufruf (im Ordner katalog/): python3 _pruef_katalog.py eintrag.md [--thema "Volumen und Oberfläche" --dateien a.md,b.md]
typen.csv wird eine Ebene über katalog/ erwartet (--typen für einen anderen Pfad).
Nicht als Zahl gezählt: Belegklammern (seit 10c), Original-ids, Jahreszahlen, Etiketten „Einheit n“, „Kl. n“, „S. n“, „Blatt 0“ (seit 08h), Kapitel „I 2“ und Kapitelbereiche „II 3–4“ (seit 08i), „(4×)“ und Vorzahlen an Variablen (2x). Gezählt wird seit 08j auch die Zahl vor einer Hochzahl („6²“ → 6), seit 09a vor jeder Hochzahl ⁰–⁹ („3⁴“ → 3, „10⁶“ → 10).
Seit 09b werden alle Sprossen-Zeilen einer Einheit geprüft (mehrere Verfahrenstypen je Einheit), nicht nur die zuletzt gelesene.
"""
import re, sys, csv, argparse

ap = argparse.ArgumentParser()
ap.add_argument("eintrag")
ap.add_argument("--thema", action="append", default=[])
ap.add_argument("--dateien", default="")
import os
ap.add_argument("--typen", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "msa", "msa-typen.csv"))  # Umbau 2026-09-19: Typenliste liegt in msa/
a = ap.parse_args()

text = open(a.eintrag, encoding="utf-8").read()

def strip_noise(s):
    s = re.sub(r"\[[A-ZÄÖÜ][^\]]*\]", " ", s)          # Belegklammern (seit 10c): Text in eckigen Klammern, der mit einem Großbuchstaben beginnt, ist eine Quellen- oder Verweisangabe der Werkstatt und erreicht kein Blatt – „[MSK B1A 1.1–1.2, DB 1.1, MO]“, „[LS-AA Kl. 9 III 3–5]“, „[RLP E „vier Quadranten“; P10 2019-OS-K2d]“. Klammern, die mit Kleinbuchstabe, Ziffer oder Pfeil beginnen („[ggf. bis 10 000]“, „[1–3 Zahlenbeispiele]“, „[→GOST]“), bleiben in der Prüfung.
    s = re.sub(r"\d{4}-(OS|FOR)-\w+", " ", s)          # Original-ids
    s = re.sub(r"\b(Einheit|Einheiten|Kl\.|S\.|Klasse|Blatt)\s*\d+(\s*(und|bis|,|/|–)\s*\d+)*", " ", s)   # „Blatt 0“ ist ein Etikett, keine Zahl (seit 08h); seit 10c auch Kommalisten („Einheit 1, 3 und 5“), die vorher nur bis zur ersten Zahl gelesen wurden
    s = re.sub(r"\(\d+×", "(", s)                          # Kettenangabe „(4×)“ ist ein Etikett; seit 10c auch mit Zusatz („(4×, mit Probe)“) – der Rest der Klammer bleibt geprüft
    s = re.sub(r"(\d)[⁰¹²³⁴⁵⁶⁷⁸⁹]", r"\1 ", s)            # Hochzahl abtrennen: „6²“ zählt als 6 (seit 08j; ² ist ein \w-Zeichen und verdeckte die Zahl); seit 09a alle Hochzahlen ⁰–⁹ („3⁴“ → 3, „10⁶“ → 10)
    s = re.sub(r"\b(19|20)\d\d\b", " ", s)               # Jahreszahlen
    s = re.sub(r"\b[IVX]+\s+\d+(?:\s*(?:und|bis|–|/)\s*\d+)*\b", " ", s)   # LS-AA-Kapitel „I 2“, auch Bereiche „II 3–4“ (seit 08i)
    return s

NUM = re.compile(r"(?<![\w,])\d+(?:,\d+)?(?!\w)(?!,\d)")   # seit 08i: „25, aber“ zählt (Komma mit Leerzeichen ist kein Dezimalkomma)
def numbers(s):
    return set(NUM.findall(strip_noise(s)))

# --- Abschnitte
def section(name):
    m = re.search(r"^### " + re.escape(name) + r".*?$(.*?)(?=^### |^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""

kasten = section("Merkkasten")
blatt0 = section("Voraussetzungen (Blatt 0)")
schwach = section("Für schwache Schüler")

# Kästen je Einheit
kaesten = {}
for m in re.finditer(r"^Einheit (\d+)[^\n]*:\n(.*?)(?=^Einheit \d+|\Z)", kasten, re.S | re.M):
    n = int(m.group(1)); body = m.group(2)
    body = re.sub(r"^Quelle:.*$", "", body, flags=re.M)
    body = re.sub(r"^\s*Formelsammlung:.*$", "", body, flags=re.M)
    kaesten[n] = numbers(body)

# Sprossen je Einheit
sprossen = {}   # seit 09b: Liste aller Sprossen-Zeilen je Einheit
for line in schwach.splitlines():
    m = re.match(r"^- .*?\(Einheit (\d+)[^)]*\):", line)   # seit 10d auch mit Zusatz in der Klammer: „(Einheit 1, Vorrat):“
    if m:
        sprossen.setdefault(int(m.group(1)), []).append(line)
grund = "\n".join(l for l in schwach.splitlines() if l.startswith("Grundvorstellung"))

# Blatt-0-Zeilen je Einheit: Zeilen, die „Einheit n“ oder „alle Einheiten“ nennen
def blatt0_lines(n):
    out = []
    for l in blatt0.splitlines():
        if not l.startswith("- "): continue
        refs = re.findall(r"Einheit (\d+)(?:\s*(?:und|bis|,)\s*(\d+))?", l)
        nums = set()
        for x, y in refs:
            nums.add(int(x))
            if y:
                if "bis" in l:
                    nums.update(range(int(x), int(y) + 1))
                nums.add(int(y))
        if n in nums or "alle Einheiten" in l or "allen Einheiten" in l:
            out.append(l)
    return out

ok = True
for n in sorted(kaesten):
    kz = kaesten[n]
    ziel = " ".join(sprossen.get(n, []) + [grund] + blatt0_lines(n))
    treffer = kz & numbers(ziel)
    print(f"Einheit {n}: Kastenzahlen {sorted(kz, key=lambda s: float(s.replace(',', '.')))}")
    if treffer:
        ok = False
        print(f"   TREFFER in Sprossen/Blatt 0: {sorted(treffer)}")
        for t in sorted(treffer):
            for l in sprossen.get(n, []) + [grund] + blatt0_lines(n):
                for mm in re.finditer(NUM, strip_noise(l)):
                    if mm.group(0) == t:
                        s0 = max(0, mm.start() - 40); print(f"      …{strip_noise(l)[s0:mm.end()+40]}…")
    else:
        print("   keine Kastenzahl in Sprossen oder Blatt 0")
    if n not in sprossen:
        print(f"   WARNUNG: keine Sprossen-Zeile für Einheit {n}")

# --- Sek II (Auftrag Sek-II-Werkzeuge): greift, wenn der Eintrag eine Prüfungsform-Liste
# fhr/abi/iqb statt P10-Typen hat (konzept.md § 4 Entscheidung 36).
if "### Prüfungsform (fhr / abi / iqb)" in text:
    basename = os.path.splitext(os.path.basename(a.eintrag))[0]
    themen_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "themen.csv")

    # (a) Zählzeile "N1 + N2 + ... = T Haupttypen, M1 + M2 + ... = S Zeilen" gegen die
    # tatsächlich gelisteten Typen und ihre Zeilenzahl in Klammern (ggf. mit Anmerkung "(1; ...)"),
    # je Einheit und in der Summe.
    typen_sec = section("Typen je Lerneinheit")
    zm = re.search(r"^Zählung:\s*([\d\s+]+?)=\s*(\d+)\s*Haupttypen,\s*([\d\s+]+?)=\s*(\d+)\s*Zeilen", typen_sec, re.M)
    if not zm:
        print("Sek-II Typen je Lerneinheit: Zählzeile fehlt oder unerwartetes Format"); ok = False
    else:
        soll_typen = [int(x) for x in re.findall(r"\d+", zm.group(1))]
        soll_zeilen = [int(x) for x in re.findall(r"\d+", zm.group(3))]
        ist_typen, ist_zeilen = [], []
        for n_str, body in re.findall(r"^Einheit (\d+):(.*?)(?=^Einheit \d+:|^Zählung:|\Z)", typen_sec, re.S | re.M):
            nums = re.findall(r"\((\d+)(?:;[^)]*)?\)", body.split(" Dazu:")[0])
            ist_typen.append(len(nums)); ist_zeilen.append(sum(int(x) for x in nums))
        print(f"Sek-II Typen je Lerneinheit: Zählzeile {' + '.join(map(str, soll_typen))} = {int(zm.group(2))} Haupttypen, "
              f"{' + '.join(map(str, soll_zeilen))} = {int(zm.group(4))} Zeilen")
        if ist_typen != soll_typen or sum(ist_typen) != int(zm.group(2)):
            print(f"   ABWEICHUNG Haupttypen je Einheit: gezählt {ist_typen} = {sum(ist_typen)}"); ok = False
        if ist_zeilen != soll_zeilen or sum(ist_zeilen) != int(zm.group(4)):
            print(f"   ABWEICHUNG Zeilen je Einheit: gezählt {ist_zeilen} = {sum(ist_zeilen)}"); ok = False

    # (b)+(c) Profillisten fhr/abi/iqb: jede Typnennung trägt genau eine Einheitsnummer E1–E9 in
    # der Klammerform „(n, Ek)“ bzw. „(Ek)“ bei je-1-Typen (Entscheidung 36; die Zahl der Einheiten
    # ist frei, bis 2026-09-19 ließ das Muster nur E1–E5 zu); die Summe der n
    # (bzw. 1 ohne n) je Profil gegen die Zeilenwerte des Themas in themen.csv (kanonisch = Dateiname).
    pf_sec = section("Prüfungsform (fhr / abi / iqb)")
    zeilen_je_profil = {}
    with open(themen_csv, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            if r["kanonisch"].strip() != basename or not r["profil"].strip():
                continue
            zeilen_je_profil[r["profil"]] = zeilen_je_profil.get(r["profil"], 0) + int(r["zeilen"])
    for profil in ("fhr", "abi", "iqb"):
        pm = re.search(r"^" + profil + r" \(.*?\)\s*\[.*?\]:\s*(.*?)\.\s*Muster:", pf_sec, re.M)
        if not pm:
            continue
        summe = 0
        for seg in pm.group(1).split(" · "):
            bm = re.search(r"\((?:(\d+),\s*)?E[1-9]\)\s*$", seg.strip())
            if not bm:
                print(f"Sek-II Prüfungsform {profil}: Typnennung ohne gültige Klammerform „(n, Ek)“/„(Ek)“: …{seg.strip()[-60:]}")
                ok = False; continue
            summe += int(bm.group(1)) if bm.group(1) else 1
        erwartet = zeilen_je_profil.get(profil)
        if erwartet is None:
            print(f"Sek-II Prüfungsform {profil}: kein Eintrag in themen.csv für kanonisch={basename}"); ok = False
        elif summe != erwartet:
            print(f"Sek-II Prüfungsform {profil}: Zeilensumme der Profilliste {summe} ≠ themen.csv {erwartet}"); ok = False
        else:
            print(f"Sek-II Prüfungsform {profil}: Zeilensumme {summe} = themen.csv {erwartet}")

# --- P10-Typen
if a.thema:
    with open(a.typen, encoding="utf-8") as f:
        typen = [r for r in csv.DictReader(f, delimiter=";") if r["thema"] in a.thema and r["status"] == "gültig"]
    zuordnung = ""
    # seit 10f: ohne --dateien lief die Schleife null Mal, zuordnung blieb leer und *jeder* Typ galt als
    # fehlend – ein Fehlalarm, der den Prüfer wertlos macht. Ohne Angabe wird jetzt der Eintrag selbst geprüft.
    dateien = [x for x in a.dateien.split(",") if x] or [a.eintrag]
    for fn in dateien:
        t = open(fn, encoding="utf-8").read()
        m = re.search(r"^Zuordnung:.*$", t, re.M)
        zuordnung += (m.group(0) if m else "") + "\n"
    fehlt = [r["typ"] for r in typen if r["typ"] not in zuordnung]
    print(f"P10-Typen der Themen {a.thema}: {len(typen)}; in Zuordnungszeilen fehlend: {fehlt or 'keine'}")
    if fehlt: ok = False

print("ERGEBNIS:", "ok" if ok else "Befunde")
