#!/usr/bin/env python3
"""zwtrenner.py – Trennzeichen im Katalogfeld zwischenergebnis (v0.1, 05.10.2026).

Seit katalog-prompt.md 0.10 trennt „ ; “ die Zwischenergebnisse einer Zeile
(vorher „ | “ in msa, „|“ ohne Leerzeichen in abi, iqb, fhr). „|“ bleibt in
Klammern – P(A | B), P(1 | 2 | 3), ⟨1 | 2 | 3⟩ – und in Beträgen wie |PQ|.

umstellen(s, stil) – stil "msa": jedes „ | “ außerhalb von Klammern ist ein
    Trenner; stil "ohne": jedes „|“ außerhalb von Klammern und außerhalb eines
    Betrags, das links und rechts ein Zeichen ohne Leerraum hat (a|b), ist ein
    Trenner, außer es folgt eines der Zeichen / ^ ² ³ ) (Ende eines Betrags). Rückgabe: (neuer Text, Zahl der umgestellten Trenner, Zahl der
    stehengebliebenen „|“ außerhalb von Klammern).
umstellen_neu(s) – beide Stile nacheinander, für Werte aus Korrektur- und
    Beitabellen (die tragen „|“).
teile(s) – zerlegt einen umgestellten Wert an „ ; “ außerhalb von Klammern.

Benutzt von msa/msa-bau.py --trenner, fhr/fhr-bau.py --trenner,
abitur/vorrat-uebernahme.py --trenner und werkzeuge/bestand.py.
"""
import re

AUF, ZU = "([{⟨", ")]}⟩"
NEU = " ; "
# Betrag eines Namens (|PQ|, |M₁M₂|, |v|, |AB_s|, |MQ_t|) oder eines Ausdrucks mit Vektor (|SN · ⟨0 | 0 | 1⟩|)
BETRAG = re.compile(r"\|[A-Za-zÄÖÜäöüα-ω][A-Za-z0-9₀-₉_′']{0,10}\||\|[^|⟨⟩]{0,20}⟨[^⟩]*⟩\|")
# Ein „|“, auf das eines dieser Zeichen folgt, schließt einen Betrag (|u · v|/…, |R Q|^2).
NACH_BETRAG = "/^²³)"


def _tiefen(s):
    t, out = 0, []
    for ch in s:
        if ch in AUF:
            t += 1
        elif ch in ZU:
            t = max(0, t - 1)
        out.append(t)
    return out


def umstellen(s, stil):
    if "|" not in s:
        return s, 0, 0
    tief = _tiefen(s)
    geschuetzt = set()
    for i, ch in enumerate(s):
        if ch == "|" and tief[i] == 0 and i not in geschuetzt:
            m = BETRAG.match(s, i)
            if m and tief[m.end() - 1] == 0:
                geschuetzt.update((m.start(), m.end() - 1))
    teile_, start, n, rest = [], 0, 0, 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "|" and tief[i] == 0 and i not in geschuetzt:
            if stil == "msa":
                trenner = s[i - 1:i + 2] == " | "
            else:
                trenner = (0 < i < len(s) - 1 and not s[i - 1].isspace() and not s[i + 1].isspace()
                           and s[i + 1] not in NACH_BETRAG)
            if trenner:
                teile_.append(s[start:i].rstrip())
                start = i + 1
                n += 1
            else:
                rest += 1
        i += 1
    teile_.append(s[start:].lstrip() if n else s[start:])
    if n:
        teile_ = [teile_[0]] + [t.lstrip() for t in teile_[1:]]
    return NEU.join(teile_), n, rest


def umstellen_neu(s):
    """Für neu eingehende Werte (Korrektur- und Beitabellen): erst „ | “, dann „|“ ohne Leerzeichen."""
    return umstellen(umstellen(s, "msa")[0], "ohne")[0]


def teile(s):
    s = (s or "").strip()
    if not s:
        return []
    tief = _tiefen(s)
    out, start = [], 0
    for m in re.finditer(re.escape(NEU), s):
        if tief[m.start()] == 0:
            out.append(s[start:m.start()])
            start = m.end()
    out.append(s[start:])
    return [x.strip() for x in out if x.strip()]


if __name__ == "__main__":
    probe = [
        ("msa", "a = 2 | P(1 | 2) ⇒ b", "a = 2 ; P(1 | 2) ⇒ b"),
        ("ohne", "M(0 | 4 | 1)|MP = (0 | −3 | 4)|Seitenlänge |PQ| = 5·√2",
         "M(0 | 4 | 1) ; MP = (0 | −3 | 4) ; Seitenlänge |PQ| = 5·√2"),
        ("ohne", "EF = (1; 5; 0)|FG = (−5; 1; 0)||EF| = |FG| = √26",
         "EF = (1; 5; 0) ; FG = (−5; 1; 0) ; |EF| = |FG| = √26"),
        ("ohne", "sin α = |SN · ⟨0 | 0 | 1⟩|/|SN| = 1/√1526", "sin α = |SN · ⟨0 | 0 | 1⟩|/|SN| = 1/√1526"),
        ("ohne", "f(−1) = 2|H(−1; 2)|T(1; −2)", "f(−1) = 2 ; H(−1; 2) ; T(1; −2)"),
        ("ohne", "u = ⟨4 | 4⟩ kollinear|cos φ = |u · v|/(|u| · |v|) ≈ 0,99|S", "u = ⟨4 | 4⟩ kollinear ; cos φ = |u · v|/(|u| · |v|) ≈ 0,99 ; S"),
        ("ohne", "x = ⟨4 | 3⟩ + r · ⟨−4 | 0⟩|in E: r = 1", "x = ⟨4 | 3⟩ + r · ⟨−4 | 0⟩ ; in E: r = 1"),
    ]
    for stil, ein, soll in probe:
        ist = umstellen(ein, stil)[0]
        print("ok " if ist == soll else "FEHLER", repr(ist))
        assert teile(ist) == [x.strip() for x in soll.split(NEU)]
