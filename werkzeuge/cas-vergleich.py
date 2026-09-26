# -*- coding: utf-8 -*-
"""cas-vergleich.py – CAS-Fassung eines Landeshefts je Teilaufgabe gegen die WTR-Fassung halten.
Version 0.1 · 28.09.2026 · Auftrag Nacht 2026-09-28, Teil 3 (Befund abitur/befund-cas-berlin-2026-09-28.md)

Misst, nicht erfasst: für jede Teilaufgabe der CAS-Fassung die Teilaufgabe der
WTR-Fassung derselben Aufgabe mit dem ähnlichsten Text (difflib) und das Urteil
„wortgleich“ (normierter Text gleich), „nur Zahlen“ (gleich bis auf Ziffernfolgen)
oder „abweichend <Ähnlichkeit>“; dazu die BE beider Fassungen aus den BE-Tabellen.
Normierung wie beim Pool-Abgleich (iqb-quellen.py): nur Buchstaben und Ziffern,
ohne Seitenköpfe und Fußzeilen, ohne die Wörter CAS und WTR. Zwischenstämme
(Text zwischen zwei Teilaufgaben ohne Buchstaben) hängen an der vorangehenden
Teilaufgabe – eine Abweichung dort betrifft die folgende; das und die Art der
Abweichung liest man in der Diff-Ausgabe von Hand nach (Befunddatei).
Mit einem dritten Heft (z. B. 2017-bb-ea-cas) wird jede Teilaufgabe einer Aufgabe
mit gleichem Titel auch gegen dieses Heft gehalten (gleicher Buchstabe).

Aufruf (aus der Repo-Wurzel):
  python werkzeuge/cas-vergleich.py 2017-be-gk            (hefte/abi/2017-be-gk.pdf gegen -cas.pdf)
  python werkzeuge/cas-vergleich.py 2017-be-lk 2017-bb-ea-cas
Braucht pdftotext (MiKTeX, %LocalAppData%\\Programs\\MiKTeX\\miktex\\bin\\x64) und die Hefte
unter hefte/abi/ (lokal, nicht im Repo).
"""
import difflib, os, re, subprocess, sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDFTOTEXT = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "MiKTeX", "miktex", "bin", "x64", "pdftotext.exe")
KOPF = re.compile(r"^\s*(Grundkurs|Leistungskurs) mit CAS\s*$|^\s*Kurs auf erh\S+htem Anforderungsniveau.*$"
                  r"|^\s*Fortsetzung auf der n\S+chsten Seite\s*$|^\s*Verteilung der Bewertungseinheiten.*$"
                  r"|^_{20,}\s*$|^\s*Seite \d+ von \d+.*$|^\s*(Grundkurs|Leistungskurs)\s*$"
                  r"|^\s*Zentrale sch\w*liche Abiturpr.*$|^\s*Anlage\s*$|^\s*Mathematik\s*$", re.M)
HEAD = re.compile(r"^\s*(Fortsetzung von )?Aufgabe (\d\.\d)(?: CAS)?\s*:\s*([^\n]*?)\s*(\(Fortsetzung\))?\s*$", re.M)
ANH = re.compile(r"^\s*(Anlage|Koordinatensystem|Material|Tabelle) zu (Aufgabe )?\d.*$|^\s*Anhang\s*$", re.M)
BE = re.compile(r"^\s*(?:Teilaufgabe|Aufgabenteil)\s+(a\).*)$\n\s*BE\s+(\d.*)$", re.M)


def text(heft):
    pfad = os.path.join(WURZEL, "hefte", "abi", heft + ".pdf")
    return subprocess.run([PDFTOTEXT, "-layout", "-enc", "UTF-8", "-eol", "unix", pfad, "-"],
                          capture_output=True, check=True).stdout.decode("utf-8")


def aufgaben(txt):
    txt = KOPF.sub("", txt)
    marks = [(m.start(), m.end(), m.group(2), m.group(3)) for m in HEAD.finditer(txt)]
    anh = [m.start() for m in ANH.finditer(txt)]
    out = {}
    for i, (s, e, nr, titel) in enumerate(marks):
        ende = marks[i + 1][0] if i + 1 < len(marks) else len(txt)
        for a in anh:
            if e < a < ende:
                ende = a
                break
        d = out.setdefault(nr, {"titel": re.sub(r"\s*\(Fortsetzung\)", "", titel), "body": ""})
        d["body"] += "\n" + txt[e:ende]
    for d in out.values():
        body, be = d["body"], {}
        mt = BE.search(body)
        if mt:
            buchst = re.findall(r"([a-z])\)", mt.group(1))
            be = dict(zip(buchst + ["Summe"], re.findall(r"\d+", mt.group(2))))
            body = body[:mt.start()] + body[mt.end():]
        st = re.split(r"\n\s{0,8}([a-z])\)\s", "\n" + body)
        d["stamm"], d["ta"], d["be"] = st[0], {st[j]: st[j + 1] for j in range(1, len(st), 2)}, be
    return out


def norm(t):
    return re.sub(r"[^0-9A-Za-zÄÖÜäöüß]", "", re.sub(r"\b(CAS|WTR)\b", "", t))


def q(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def urteil(tw, tc):
    nw, nc = norm(tw), norm(tc)
    if nw == nc:
        return "wortgleich"
    if re.sub(r"\d+", "#", nw) == re.sub(r"\d+", "#", nc):
        return "nur Zahlen"
    return "abweichend %.3f" % q(tw, tc)


def diff(a, b):
    for zeile in difflib.unified_diff([x.strip() for x in a.splitlines() if x.strip()],
                                      [x.strip() for x in b.splitlines() if x.strip()], lineterm="", n=0):
        if not zeile.startswith(("---", "+++", "@@")):
            print("      " + zeile)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        return
    heft = sys.argv[1]
    W, C = aufgaben(text(heft)), aufgaben(text(heft + "-cas"))
    BB = aufgaben(text(sys.argv[2])) if len(sys.argv) > 2 else {}
    for nr in sorted(set(W) | set(C)):
        aw, ac = W.get(nr), C.get(nr)
        if not aw or not ac:
            print(nr, "fehlt in", "WTR" if not aw else "CAS")
            continue
        bbnr = [k for k, v in BB.items() if v["titel"] == ac["titel"]]
        print(f"== {nr} {ac['titel']}  BE-Summe WTR {aw['be'].get('Summe')} / CAS {ac['be'].get('Summe')}"
              + (f"  [{sys.argv[2]} {bbnr[0]}]" if bbnr else ""))
        u = urteil(aw["stamm"], ac["stamm"])
        print(f"   Einleitung: {u}")
        if u != "wortgleich":
            diff(aw["stamm"], ac["stamm"])
        benutzt = set()
        for teil in sorted(ac["ta"]):
            tc = ac["ta"][teil]
            wb = max(aw["ta"], key=lambda k: (q(aw["ta"][k], tc), k == teil))
            if q(aw["ta"][wb], tc) < 0.5:
                wb = "-"
            else:
                benutzt.add(wb)
            u = urteil(aw["ta"][wb], tc) if wb != "-" else "ohne WTR-Gegenstück"
            zus = ""
            if bbnr and teil in BB[bbnr[0]]["ta"]:
                zus = f"  | {sys.argv[2]} {bbnr[0]} {teil}: {urteil(BB[bbnr[0]]['ta'][teil], tc)}"
            print(f"   {teil} (WTR {wb}): {u}  BE {aw['be'].get(wb, '-')}/{ac['be'].get(teil, '-')}{zus}")
            if wb == "-":
                diff("", tc)
            elif u != "wortgleich":
                diff(aw["ta"][wb], tc)
        for k in sorted(set(aw["ta"]) - benutzt):
            print(f"   WTR {k} ohne CAS-Gegenstück, BE {aw['be'].get(k, '-')}")
            diff(aw["ta"][k], "")


if __name__ == "__main__":
    main()
