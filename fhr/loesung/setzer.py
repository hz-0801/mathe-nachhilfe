#!/usr/bin/env python3
"""Setzer Lösungen Sek II: Daten je Teilaufgabe -> LaTeX (xelatex).

Aufruf: python setzer.py daten/2026-C-1.txt [ziel.tex] [--hinweise]
--hinweise: nur Fragen und Ansätze (Hinweisblatt vor der Lösung).
Form: plan.md § 10 18.10. b (Frage mit „?“, Ansatz in allgemeiner
Form, Zeilen „Rechnung ⇒ Schluss“, Unterfrage); ⇒ in einer Spalte.

Zeilen der Datei (LaTeX-Text, Formeln in $…$):
  # Titel | rechts      Kopf
  f: …                  Funktionszeile unter dem Kopf
  bez: …                graue Bezeichnerzeile
  a) Frage              neue Teilaufgabe mit Hauptfrage
  ? Frage               Unterfrage
  > Ansatz              Ansatz in allgemeiner Form
  | Rechnung => Schluss Zeile (=> und Schluss oder Rechnung dürfen fehlen)
  ! Ergebnis            Ergebniszeile, fett, über Rechnung und Schluss
  ~ 1/x_1, 2/x_2 ; -/fällt, +/steigt, -/fällt   Zahlenstrahl
  **…**                 fett (auch Formeln)
"""
import re
import sys

KOPF = r"""\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{DejaVu Sans}[Scale=0.9]
\usepackage{amsmath,amssymb}
\usepackage[left=16mm,right=16mm,top=14mm,bottom=14mm]{geometry}
\usepackage{xcolor,array,tabularx,tikz}
\definecolor{grau}{gray}{0.45}
\definecolor{linie}{gray}{0.8}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\newcommand{\g}[1]{{\small\color{grau}#1}}
\newcommand{\ans}{\leavevmode{\footnotesize\color{grau}Ansatz}}
\newcolumntype{L}{@{}p{7mm}}
\newcolumntype{A}{p{13mm}}
\newcolumntype{R}{>{\raggedright\arraybackslash}p{78mm}}
\newcolumntype{I}{@{}c@{\hspace{4pt}}}
\newcolumntype{S}{>{\raggedright\arraybackslash}X@{}}
\renewcommand{\arraystretch}{1.22}
\begin{document}
"""


def fett(s):
    return re.sub(r"\*\*(.+?)\*\*", r"{\\bfseries\\boldmath \1}", s)


def zahlenstrahl(spec):
    stellen, felder = spec.split(";")
    st = []
    for teil in re.split(r",\s+", stellen.strip()):
        wert, name = teil.strip().split("/")
        st.append((float(wert.replace(",", ".")), wert.strip(), name.strip()))
    fe = [f.strip().split("/") for f in re.split(r",\s+", felder.strip())]
    lo, hi = st[0][0] - 1.4, st[-1][0] + 1.4
    sk = 7.0 / (hi - lo)
    x = lambda v: (v - lo) * sk
    t = [r"\begin{tikzpicture}[baseline=-2pt]",
         rf"\draw[->] (0,0) -- ({x(hi)+0.3:.2f},0) node[right,font=\scriptsize] {{$x$}};"]
    for v, txt, name in st:
        t.append(rf"\draw ({x(v):.2f},0.1)--({x(v):.2f},-0.1);")
        t.append(rf"\node[below,font=\scriptsize] at ({x(v):.2f},-0.08) {{${txt.replace(',', '{,}')}$}};")
        t.append(rf"\node[below,font=\scriptsize,text=grau] at ({x(v):.2f},-0.42) {{${name}$}};")
    grenzen = [lo] + [v for v, _, _ in st] + [hi]
    for i, (vz, wort) in enumerate(fe):
        m = (grenzen[i] + grenzen[i + 1]) / 2
        vz = {"-": "$-$", "+": "$+$"}.get(vz, vz)
        t.append(rf"\node[above,font=\scriptsize] at ({x(m):.2f},0.02) {{{vz} {wort}}};")
    t.append(r"\end{tikzpicture}")
    return " ".join(t)


def setze(zeilen, hinweise=False):
    out = [KOPF]
    offen = False
    erste = True

    def schliessen():
        nonlocal offen
        if offen:
            out.append(r"\end{tabularx}\par")
            offen = False

    for roh in zeilen:
        z = roh.rstrip("\n")
        if not z.strip():
            continue
        if z.startswith("# "):
            titel, _, rechts = z[2:].partition("|")
            if hinweise:
                rechts = rechts.replace("Lösung", "Hinweise")
            out.append(rf"{{\large\bfseries {titel.strip()}}}\hfill\g{{{rechts.strip()}}}\par")
            out.append(r"\vspace{2pt}\hrule height 1.2pt\vspace{5pt}")
            continue
        if z.startswith("f: "):
            out.append(z[3:] + r"\par")
            continue
        if z.startswith("bez: "):
            out.append(r"\g{" + z[5:] + r"}\par")
            continue
        m = re.match(r"^([a-z])\)\s+(.*)$", z)
        if m:
            schliessen()
            if not erste:
                out.append(r"\vspace{6pt}{\color{linie}\hrule}")
            erste = False
            out.append(r"\vspace{3pt}\noindent\begin{tabularx}{\linewidth}{LARIS}")
            offen = True
            out.append(rf"\textbf{{{m.group(1)})}} & \multicolumn{{4}}{{l@{{}}}}{{{fett(m.group(2))}}}\\")
            continue
        kind, text = z[0], z[1:].strip()
        if hinweise and kind in "|!~":
            continue
        if kind == "?":
            out.append(rf"\rule{{0pt}}{{16pt}}& \multicolumn{{4}}{{l@{{}}}}{{{fett(text)}}}\\")
        elif kind == ">":
            out.append(rf"& \ans & \multicolumn{{3}}{{l@{{}}}}{{{fett(text)}}}\\")
        elif kind == "|":
            r, pfeil, s = text.partition("=>")
            r, s = fett(r.strip()), fett(s.strip())
            if pfeil:
                out.append(rf"& & {r} & $\Rightarrow$ & {s}\\")
            else:
                out.append(rf"& & \multicolumn{{3}}{{l@{{}}}}{{{r}}}\\")
        elif kind == "!":
            out.append(rf"& & \multicolumn{{3}}{{l@{{}}}}{{\bfseries\boldmath {text}}}\\")
        elif kind == "~":
            out.append(rf"& & \multicolumn{{3}}{{l@{{}}}}{{\rule{{0pt}}{{22pt}}{zahlenstrahl(text)}}}\\[12pt]")
        else:
            sys.exit(f"unbekannte Zeile: {z}")
    schliessen()
    out.append(r"\end{document}")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    hinweise = "--hinweise" in sys.argv
    quelle = args[0]
    ziel = args[1] if len(args) > 1 else re.sub(r"\.txt$", ".tex", quelle)
    with open(quelle, encoding="utf-8") as fh:
        tex = setze(fh, hinweise)
    with open(ziel, "w", encoding="utf-8") as fh:
        fh.write(tex)
    print(ziel)
