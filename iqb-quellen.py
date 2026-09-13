# -*- coding: utf-8 -*-
"""iqb-quellen.py – erzeugt iqb-quellen.csv aus der Übersichtsseite des IQB.
Version 0.1 · 13.09.2026 · gehört zum Profil iqb (iqb-quellen.md § 4)

Ablauf:
  1. Übersichtsseiten ?page=1 … holen, bis eine Seite keine Aufgabe mehr nennt;
     alle Kennungen <Kennung>_Aufgabe.pdf sammeln.
  2. Kennungen zerlegen (Jahr, Niveau, Teil, Sachgebiet, Gruppe/Hilfsmittel,
     Nummer), papier und stapel nach iqb.md § 4 und § 7 bilden, sortieren.
  3. Teil-A-Dateien in den Cache-Ordner laden (nur fehlende), Seitenzahl lesen
     und den Text des Abschnitts „1 Aufgabe" vergleichen: wortgleiche Dateien
     sind Dubletten, die spätere zeigt auf die frühere (Spalte dublette_von).
  4. iqb-quellen.csv schreiben. Kennungen dürfen nur hinzukommen; fehlt eine
     bisherige, bricht das Skript ab.

Aufruf: python iqb-quellen.py [CACHE-ORDNER]   (Standard: ./iqb-pdf, wird angelegt)
Braucht pypdf. Teil-B-Dateien werden nicht geladen; ihre Spalten seiten und
dublette_von bleiben leer, bis Teil B erfasst wird.
"""
import csv, io, os, re, sys, urllib.request, collections

LISTE = "https://www.iqb.hu-berlin.de/de/schule/aufgaben/sekii/abiturpruefungsaufgaben-mathematik/"
DATEIEN = "https://www.iqb.hu-berlin.de/media/exercise_files/Abituraufgaben_Mathematik/"
ZIEL = "iqb-quellen.csv"
KOPF = ["kennung", "jahr", "niveau", "teil", "sachgebiet", "gruppe", "hilfsmittel", "nr",
        "papier", "stapel", "seiten", "dublette_von"]
MUSTER = re.compile(r"^(?P<jahr>\d{4}|Beispielaufgaben)M(?P<niveau>erhoeht|grundlegend)"
                    r"(?P<teil>A|B)(?P<sach>Analysis|AGLAA1|AGLAA2|Stochastik)(?P<rest>.*)$")
NIVEAU = {"grundlegend": "ga", "erhoeht": "ea"}
SACH = {"Analysis": "Analysis", "AGLAA1": "AG/LA (A1)", "AGLAA2": "AG/LA (A2)", "Stochastik": "Stochastik"}
SACH_ORD = ["Analysis", "AG/LA (A1)", "AG/LA (A2)", "Stochastik"]


def hole(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (iqb-quellen.py)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def kennungen():
    """Seiten holen, bis eine Seite nichts Neues bringt – die Seite hinter der
    letzten liefert die letzte noch einmal, nicht eine leere."""
    gesehen, eindeutig, seite = set(), [], 1
    while seite <= 200:
        html = hole(LISTE + (f"?page={seite}" if seite > 1 else "")).decode("utf-8", "replace")
        treffer = re.findall(r"Abituraufgaben_Mathematik/([^\"' /]+)_Aufgabe\.pdf", html)
        neu = [k for k in treffer if k not in gesehen]
        if not neu:
            break
        for k in neu:
            gesehen.add(k); eindeutig.append(k)
        seite += 1
    print(f"{seite - 1} Übersichtsseiten, {len(eindeutig)} Kennungen")
    return eindeutig


def zerlege(k):
    m = MUSTER.match(k)
    if not m:
        sys.exit(f"{k}: Kennung nicht zerlegbar")
    d = m.groupdict(); rest = d.pop("rest")
    if d["teil"] == "A":
        mm = re.fullmatch(r"(\d)(\d*)", rest)
        if not mm:
            sys.exit(f"{k}: Teil A ohne Aufgabengruppe")
        d["gruppe"], d["nr"], d["hilfsmittel"] = mm.group(1), mm.group(2), ""
    else:
        mm = re.fullmatch(r"(WTR|CAS|MMS)(\d*)", rest)
        if not mm:
            sys.exit(f"{k}: Teil B ohne Hilfsmittel")
        d["hilfsmittel"], d["nr"], d["gruppe"] = mm.group(1), mm.group(2), ""
    d["jahr"] = "bsp" if d["jahr"] == "Beispielaufgaben" else d["jahr"]
    d["sachgebiet"] = SACH[d.pop("sach")]
    niveau = NIVEAU[d["niveau"]]
    d["papier"] = f"{d['jahr']}-iqb-{niveau}" + ("-mms" if d["hilfsmittel"] in ("CAS", "MMS") else "")
    d["stapel"] = f"{d['jahr']}-{niveau}-{d['teil']}"
    d["kennung"] = k
    return d


def sortkey(r):
    j = 0 if r["jahr"] == "bsp" else int(r["jahr"])
    return (-j, r["niveau"] != "grundlegend", r["teil"], SACH_ORD.index(r["sachgebiet"]),
            r["gruppe"], {"": 0, "WTR": 1, "CAS": 2, "MMS": 2}[r["hilfsmittel"]], int(r["nr"] or 0))


def scanne_teil_a(rows, cache):
    from pypdf import PdfReader
    os.makedirs(cache, exist_ok=True)
    texte = {}
    for r in rows:
        if r["teil"] != "A":
            continue
        pfad = os.path.join(cache, r["kennung"] + ".pdf")
        if not os.path.exists(pfad):
            with open(pfad, "wb") as fh:
                fh.write(hole(DATEIEN + r["kennung"] + "_Aufgabe.pdf"))
        rd = PdfReader(pfad)
        r["seiten"] = str(len(rd.pages))
        t = "\n".join(p.extract_text() for p in rd.pages)
        m = re.search(r"1\s+Aufgabe(.*?)2\s+Erwartungshorizont", t, re.S)
        texte[r["kennung"]] = re.sub(r"\s+", " ", m.group(1) if m else t).strip()
    reihe = {r["kennung"]: i for i, r in enumerate(rows)}
    gruppen = collections.defaultdict(list)
    for k, t in texte.items():
        gruppen[t].append(k)
    dubl = {}
    for ks in gruppen.values():
        if len(ks) > 1:
            erste = min(ks, key=lambda k: reihe[k])
            for k in ks:
                if k != erste:
                    dubl[k] = erste
    for r in rows:
        r["dublette_von"] = dubl.get(r["kennung"], "")
    print(f"Teil A: {len(texte)} Dateien gescannt, {len(dubl)} Dubletten")


def main():
    cache = sys.argv[1] if len(sys.argv) > 1 else "iqb-pdf"
    rows = [zerlege(k) for k in kennungen()]
    for r in rows:
        r.setdefault("seiten", ""); r.setdefault("dublette_von", "")
    rows.sort(key=sortkey)
    ziel = collections.Counter((r["jahr"], r["niveau"], r["teil"], r["sachgebiet"], r["gruppe"],
                                r["hilfsmittel"], r["nr"]) for r in rows)
    doppelt = [z for z, n in ziel.items() if n > 1]
    if doppelt:
        sys.exit(f"Zerlegung nicht eindeutig: {doppelt}")
    if os.path.exists(ZIEL):
        alt = {r[0] for r in csv.reader(io.open(ZIEL, encoding="utf-8", newline=""), delimiter=";")} - {"kennung"}
        fehlt = alt - {r["kennung"] for r in rows}
        if fehlt:
            sys.exit(f"Kennungen aus der bisherigen Liste fehlen auf der Seite: {sorted(fehlt)}")
    scanne_teil_a(rows, cache)
    with io.open(ZIEL, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(KOPF)
        for r in rows:
            w.writerow([r[k] for k in KOPF])
    st = collections.Counter(r["stapel"] for r in rows if r["teil"] == "A")
    print(f"{ZIEL} geschrieben: {len(rows)} Zeilen, Teil A {sum(st.values())} Dateien in {len(st)} Stapeln")


if __name__ == "__main__":
    main()
