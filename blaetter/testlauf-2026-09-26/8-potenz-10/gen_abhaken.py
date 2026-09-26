# Erzeugt abhaken.tex (Abhakseite) und die Verzeichniszeilen aus den Aufgabenquelltexten.
import re

DATEIEN = [("zone_a.tex", "zone"), ("e1_a.tex", "e1"), ("e2_a.tex", "e2"), ("e3_a.tex", "e3"), ("e4_a.tex", "e4"), ("e5_a.tex", "e5")]

def titel_arg(text, start):
    """liest das geschweifte Argument ab Position start (auf '{')."""
    tiefe, i = 0, start
    while True:
        c = text[i]
        if c == "{":
            tiefe += 1
        elif c == "}":
            tiefe -= 1
            if tiefe == 0:
                return text[start + 1:i], i
        i += 1

bloecke, bereiche = [], {}
for datei, ziel in DATEIEN:
    t = open(datei, encoding="utf-8").read()
    t = "\n".join(z for z in t.splitlines() if not z.lstrip().startswith("%"))
    n = int(re.search(r"\\setcounter\{aufgabe\}\{(\d+)\}", t).group(1))
    m = re.search(r"\\einheitenkopf\[[^\]]*\]\[([^\]]*)\]\{", t)
    kurz = m.group(1)
    kopf, _ = titel_arg(t, m.end() - 1)
    eintraege, erste = [], None
    for mm in re.finditer(r"\\verfahren\{|\\begin\{aufgabe\}\{", t):
        arg, _ = titel_arg(t, mm.end() - 1)
        if mm.group(0).startswith("\\verfahren"):
            eintraege.append(("v", arg))
        else:
            n += 1
            erste = erste or n
            eintraege.append(("a", n, arg))
    bereiche[ziel] = (erste, n, kurz, kopf)
    bloecke.append((ziel, kopf, eintraege))

out = ["% abhaken.tex – erzeugt von gen_abhaken.py aus den Aufgabenquelltexten", "\\begin{abhakseite}"]
for ziel, kopf, eintraege in bloecke:
    if ziel == "zone":
        out.append("\\ifmitzone")
    out.append("\\abhakgruppe{" + kopf.replace("Das kennst du schon", "Kennst du schon") + "}")
    for e in eintraege:
        if e[0] == "v":
            out.append("\\abhakgruppe{\\quad\\textit{" + e[1] + "}}")
        else:
            out.append("\\abhak{" + str(e[1]) + "}{" + e[2] + "}")
    if ziel == "zone":
        out.append("\\fi")
out.append("\\end{abhakseite}")
open("abhaken.tex", "w", encoding="utf-8").write("\n".join(out) + "\n")

def verz(mit_zone):
    teile = []
    for ziel, (a, b, kurz, kopf) in bereiche.items():
        if ziel == "zone":
            if mit_zone:
                teile.append("\\verz{zone}{Kennst du schon (Nr.~%d–%d)}" % (a, b))
        else:
            teile.append("\\verz{%s}{%s (Nr.~%d–%d)}" % (ziel, kurz, a, b))
    teile.append("\\verz{abhaken}{Das kann ich}")
    return "\\verzeichniszeile{" + " \\verztrenn ".join(teile) + "}\n"

open("verz_lernblatt.tex", "w", encoding="utf-8").write(verz(False))
open("verz_gesamt.tex", "w", encoding="utf-8").write(verz(True))
for z, (a, b, kurz, kopf) in bereiche.items():
    print(z, a, b, kurz)
print(verz(True))
