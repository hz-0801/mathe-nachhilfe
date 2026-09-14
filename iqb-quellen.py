# -*- coding: utf-8 -*-
"""iqb-quellen.py – erzeugt iqb-quellen.csv aus der Übersichtsseite des IQB.
Version 0.3 · 15.09.2026 · gehört zum Profil iqb (iqb-quellen.md § 4)

Ablauf:
  1. Übersichtsseiten ?page=1 … holen, bis eine Seite keine Aufgabe mehr nennt;
     alle Kennungen <Kennung>_Aufgabe.pdf sammeln.
  2. Kennungen zerlegen (Jahr, Niveau, Teil, Sachgebiet, Gruppe/Hilfsmittel,
     Nummer), papier und stapel nach iqb.md § 4 und § 7 bilden, sortieren.
  3. Teil-A-Dateien in den Cache-Ordner laden (nur fehlende), Seitenzahl lesen
     und den Text des Abschnitts „1 Aufgabe" vergleichen: wortgleiche Dateien
     sind Dubletten, die spätere zeigt auf die frühere (Spalte dublette_von).
  3b. Teil-B-Dateien ebenso laden (v0.3, Entscheidung des Lehrers 15.09.2026:
     MMS/CAS als Delta zum WTR-Zweig). Dublette in Teil B heißt: der Abschnitt
     „1 Aufgabe" ist nach Normierung (ohne Leerraum, ohne Hilfsmittelkennung)
     gleich; die spätere Datei (Ordnung § 7: WTR vor CAS/MMS) zeigt auf die
     frühere. Erwartungshorizont und Standardbezug dürfen abweichen (anderer
     Rechnerweg) – abweichende werden gemeldet. Schwelle: Gleichheit; Paare mit
     Ähnlichkeit ≥ 0,95 (difflib) ohne Gleichheit werden als „nahe" gemeldet,
     nicht markiert – sie sind von Hand anzusehen.
  4. iqb-quellen.csv schreiben. Kennungen dürfen nur hinzukommen; fehlt eine
     bisherige, bricht das Skript ab.

Aufruf: python iqb-quellen.py [CACHE-ORDNER]   (Standard: ./iqb-pdf, wird angelegt)
Braucht pypdf.
"""
import csv, io, os, re, sys, urllib.request, collections, difflib

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
        texte[r["kennung"]] = abschnitte([p.extract_text() or "" for p in rd.pages])
    # Dublette nur, wenn Aufgabe, Erwartungshorizont und Standardbezug gleich sind
    # (iqb.md § 7). Gleiche Aufgabe mit anderem Erwartungshorizont oder
    # Standardbezug ist eine eigene Fassung und wird gemeldet, nicht markiert.
    reihe = {r["kennung"]: i for i, r in enumerate(rows)}
    nach_aufgabe = collections.defaultdict(list)
    for k, (a, e, s) in texte.items():
        nach_aufgabe[a].append(k)
    dubl, fassungen = {}, []
    for ks in nach_aufgabe.values():
        if len(ks) < 2:
            continue
        erste = min(ks, key=lambda k: reihe[k])
        for k in ks:
            if k == erste:
                continue
            if texte[k] == texte[erste]:
                dubl[k] = erste
            else:
                fassungen.append((erste, k))
    for r in rows:
        r["dublette_von"] = dubl.get(r["kennung"], "")
    print(f"Teil A: {len(texte)} Dateien gescannt, {len(dubl)} Dubletten")
    for erste, k in fassungen:
        print(f"  Achtung: {k} hat dieselbe Aufgabe wie {erste}, aber anderen Erwartungshorizont "
              f"oder Standardbezug – eigene Fassung, keine Dublette (iqb.md § 7)")


# Von Hand bestätigte Dubletten in Teil B (nahe Paare, deren Unterschied nur in
# der Textextraktion liegt, nicht im Wortlaut): Kennung → erste Datei, Grund.
DUBLETTEN_HAND = {
    "2023MgrundlegendBStochastikMMS2": ("2023MgrundlegendBStochastikWTR2",
        "Kurzbeschreibung „MMS/WTR“, gleiches Dokument; pypdf setzt die BE-Summe 20 der Aufgabe an eine andere Stelle"),
}


def scanne_teil_b(rows, cache):
    """Teil B (v0.3): Dateien laden, Seitenzahl lesen, Abschnitt „1 Aufgabe"
    innerhalb desselben Stapels und Sachgebiets vergleichen. Gleicher
    Aufgabentext heißt Dublette (die spätere Datei zeigt auf die frühere, WTR
    steht vor CAS/MMS); abweichender Erwartungshorizont oder Standardbezug wird
    gemeldet, nicht als Gegengrund gewertet (Rechnerweg). Nahe Paare
    (Ähnlichkeit ≥ NAHE) werden gemeldet, nicht markiert."""
    from pypdf import PdfReader
    NAHE = 0.95
    texte = {}
    for r in rows:
        if r["teil"] != "B":
            continue
        pfad = os.path.join(cache, r["kennung"] + ".pdf")
        if not os.path.exists(pfad):
            with open(pfad, "wb") as fh:
                fh.write(hole(DATEIEN + r["kennung"] + "_Aufgabe.pdf"))
        rd = PdfReader(pfad)
        r["seiten"] = str(len(rd.pages))
        texte[r["kennung"]] = abschnitte([p.extract_text() or "" for p in rd.pages])
    reihe = {r["kennung"]: i for i, r in enumerate(rows)}
    gruppen = collections.defaultdict(list)
    for r in rows:
        if r["teil"] == "B":
            gruppen[(r["stapel"], r["sachgebiet"])].append(r["kennung"])
    dubl, abweichend, nahe = {}, [], []
    for ks in gruppen.values():
        ks.sort(key=lambda k: reihe[k])
        for i, k in enumerate(ks):
            for erste in ks[:i]:
                if erste in dubl:
                    continue
                if texte[k][0] == texte[erste][0]:
                    dubl[k] = erste
                    if texte[k][1:] != texte[erste][1:]:
                        abweichend.append((erste, k))
                    break
                q = difflib.SequenceMatcher(None, texte[k][0], texte[erste][0]).ratio()
                if q >= NAHE:
                    nahe.append((erste, k, q))
    for k, (erste, grund) in DUBLETTEN_HAND.items():
        if k not in texte or erste not in texte:
            sys.exit(f"DUBLETTEN_HAND: {k} oder {erste} unbekannt")
        if texte[k][0] == texte[erste][0]:
            print(f"  DUBLETTEN_HAND überflüssig: {k} ist ohnehin wortgleich mit {erste}")
        dubl[k] = erste
        nahe = [n for n in nahe if n[1] != k]
    for r in rows:
        if r["teil"] == "B":
            r["dublette_von"] = dubl.get(r["kennung"], "")
    print(f"Teil B: {len(texte)} Dateien gescannt, {len(dubl)} Dubletten "
          f"({sum(1 for k in dubl if rows[reihe[k]]['hilfsmittel'] != 'WTR')} in CAS/MMS, "
          f"{len(DUBLETTEN_HAND)} von Hand bestätigt):")
    for k in sorted(dubl, key=lambda k: reihe[k]):
        print(f"  {k} → {dubl[k]}" + (f" (von Hand: {DUBLETTEN_HAND[k][1]})" if k in DUBLETTEN_HAND else ""))
    for erste, k in abweichend:
        print(f"  Hinweis: {k} ist wortgleich mit {erste}, Erwartungshorizont oder Standardbezug weichen ab (Rechnerweg)")
    for erste, k, q in nahe:
        print(f"  Achtung: {k} und {erste} sind nahe (Ähnlichkeit {q:.3f}), nicht wortgleich – von Hand ansehen")


KOPFZEILE = re.compile(r"^\s*\d\s+(?:Aufgabe|Erwartungshorizont|Standardbezug|Bewertungshinweise)\s*\n\s*\d+\s*\n")


def abschnitte(seiten):
    """(Aufgabe, Erwartungshorizont, Standardbezug) als normierter Text, ohne
    Fußzeilen-Kennung, ohne die Alternative im Sachgebietsnamen, ohne
    Hilfsmittelkennung (v0.3), nur Buchstaben und Ziffern
    (2024MgrundlegendAAGLAA112/212 unterscheiden sich nur in „1: 3"
    gegen „1:3"; 2023MerhoehtAAGLAA111/211 nur in den Glyphen für ≠ und −, die
    der jeweilige PDF-Erzeuger anders ausgibt – v0.2). seiten ist die Liste der
    Seitentexte: ab Seite 2 trägt jede Seite eine Kopfzeile mit dem Abschnitt,
    der auf ihr beginnt oder weiterläuft („2 Erwartungshorizont“ über den
    letzten Teilaufgaben); sie wird entfernt, damit die Abschnittsgrenzen nur an
    den echten Überschriften liegen (v0.3 – ohne das endete der Vergleich der
    Aufgabe in Teil B an der Seitengrenze)."""
    t = "\n".join([seiten[0]] + [KOPFZEILE.sub("", s, count=1) for s in seiten[1:]])
    t = re.sub(r"(?:\d{4}|Beispielaufgaben)_M_\w+", "", t)
    t = re.sub(r"AG/LA \(A[12]\)", "AG/LA", t)
    t = re.sub(r"\b(?:WTR|CAS|MMS)\b", "", t)
    teile = []
    for anfang, ende in (("1\\s+Aufgabe", "2\\s+Erwartungshorizont"),
                         ("2\\s+Erwartungshorizont", "3\\s+Standardbezug"),
                         ("3\\s+Standardbezug", "4\\s+Bewertungshinweise")):
        m = re.search(anfang + r"(.*?)" + ende, t, re.S)
        teile.append(re.sub(r"[^0-9A-Za-zÄÖÜäöüß]", "", m.group(1) if m else t))
    return tuple(teile)


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
    scanne_teil_b(rows, cache)
    with io.open(ZIEL, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(KOPF)
        for r in rows:
            w.writerow([r[k] for k in KOPF])
    st = collections.Counter(r["stapel"] for r in rows if r["teil"] == "A")
    sb = collections.Counter(r["stapel"] + "-" + r["hilfsmittel"].lower() for r in rows if r["teil"] == "B")
    print(f"{ZIEL} geschrieben: {len(rows)} Zeilen, Teil A {sum(st.values())} Dateien in {len(st)} Stapeln, "
          f"Teil B {sum(sb.values())} Dateien in {len(sb)} Stapeln je Rechnerfassung")


if __name__ == "__main__":
    main()
