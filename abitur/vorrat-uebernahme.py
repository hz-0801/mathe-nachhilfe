#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""vorrat-uebernahme.py – Beitabelle eines Vorratslaufs in den Katalog übernehmen.

Version 0.2 · 05.10.2026 · gilt mit abi-bau.py v0.16, iqb-bau.py v1.11
(Zusatzfelder kurzloesung und neben).

Der Katalog ist abgeleitet: abi-bau.py hängt je Heft Zeilen an, die
Beitabelle (id;kurz;zwischen;stich;neben;abh;sympy) trägt je Teilaufgabe
nach, was der Vorratslauf ermittelt hat. Dieses Skript führt beide zusammen
und schreibt den Katalog im Format von abi-bau.schreibe (Semikolon,
alles gequotet, LF). Feldzuordnung (Beschlüsse des Lehrers 05.10.2026):

  kurz     → kurzloesung (neues Feld nach ergebnis; ergebnis bleibt)
  zwischen → zwischenergebnis (Beitabelle hat Vorrang, wo gefüllt)
  stich    → stichwoerter (ersetzt); Rechenschritte der alten Stichwörter,
             die nicht schon in verfahren stehen, werden an verfahren
             angehängt („; “), reine Begriffe fallen weg
  neben    → neben (neues Feld nach typ_neben; typ_neben bleibt)
  abh      → abhaengig_von (ergänzt, wo die Beitabelle einen Wert hat)
  sympy    → nur Bericht
  Vektoren in kurzloesung und zwischenergebnis als ⟨1 | 2 | 3⟩, Punkte
  bleiben P(1 | 2 | 3).

Aufruf (im Ordner abitur/):
  python3 vorrat-uebernahme.py <beitabelle.csv> <katalog.csv> [--nur <papier>] [--korrektur id=feld=alt=neu ...]
      --nur übernimmt nur die Zeilen der Beitabelle, deren id mit <papier>- beginnt.
      --streng hängt nur alte Stichwörter mit Rechenzeichen an verfahren an
      (Hefte 2017–2021: die alten Stichwörter sind Begriffe und Sachphrasen,
      keine Rechenschritte).
  python3 vorrat-uebernahme.py --nur-spalten <katalog.csv>
      legt nur die Zusatzfelder (leer) an, etwa für iqb-katalog.csv.
Der Bericht geht nach stdout; nichts wird gelesen außer den zwei Dateien.
"""
import csv
import io
import re
import sys

ZUSATZFELDER = (("kurzloesung", "ergebnis"), ("neben", "typ_neben"))

# Punktname unmittelbar vor der Klammer: ein Großbuchstabe, ggf. Index oder Strich.
PUNKTNAME = re.compile(r"(?<![A-Za-z])[A-Z][0-9₀-₉]*['′]*$")
TUPEL = re.compile(r"\(\s*([^()|]*)\|([^()|]*)\|([^()|]*)\)")
# Wörter, nach denen ein namenloses Tripel ein Punkt ist (Zweifelsfall, Bericht).
PUNKTWORT = re.compile(r"(?i:punkt|punkte|ecke|ecken|lage|quadrats|dreiecks|mitte)\s*$")
VEKTORWORT = re.compile(r"vektor\s*$")
FORTSETZUNG = re.compile(r"(,|≈|\(oder|und|bzw\.)\s*$")

NAME = re.compile(r"[A-Za-z][A-Za-z0-9']?")
SCHLIESST = re.compile(r"[=≈<>≤≥:,·+−]|(und|oder|dann|bzw\.)\b")
OEFFNET = re.compile(r"(\bmit|\bund|\boder|\bdann|[=≈<>≤≥:·+−(])$")
MATHE = re.compile(r"[0-9=≈<>≤≥∫⇒→′'√·∞∈⊥∉≠±×∑∩∪∅%]|\b[a-zA-Z]\(")


def lade(pfad):
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    return rows[0], rows[1:]


def schreibe(pfad, kopf, zeilen):
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(kopf)
        for z in zeilen:
            w.writerow(z)


def erweitere(kopf, zeilen):
    """Zusatzfelder einfügen, falls sie fehlen; alle Zeilen auffüllen."""
    neu = []
    for feld, nach in ZUSATZFELDER:
        if feld in kopf:
            continue
        pos = kopf.index(nach) + 1
        kopf.insert(pos, feld)
        for z in zeilen:
            z.insert(pos, "")
        neu.append(feld)
    return neu


def markiere_vektoren(text, zweifel, wo):
    """(a | b | c) → ⟨a | b | c⟩, außer nach einem Punktnamen oder Punktwort."""
    out, pos, letzte = [], 0, None
    for m in TUPEL.finditer(text):
        davor = text[:m.start()]
        inhalt = m.group(0)
        if any("=" in g for g in m.groups()):
            out.append(text[pos:m.end()])
            pos = m.end()
            continue
        if PUNKTNAME.search(davor):
            art = "punkt"
        elif VEKTORWORT.search(davor):
            art = "vektor"
        elif PUNKTWORT.search(davor):
            art = "punkt"
            zweifel.append(f"{wo}: Punkt nach Wort „{davor[-20:].strip()}“ → {inhalt}")
        elif FORTSETZUNG.search(davor) and letzte is not None:
            art = letzte
            if art == "punkt":
                zweifel.append(f"{wo}: Punkt als Fortsetzung „{davor[-12:].strip()}“ → {inhalt}")
        else:
            art = "vektor"
        if art == "vektor":
            inhalt = "⟨" + inhalt[1:-1].strip() + "⟩"
        out.append(text[pos:m.start()])
        out.append(inhalt)
        pos = m.end()
        letzte = art
    out.append(text[pos:])
    return "".join(out)


def schritte(stich):
    """Alte Stichwörter in Teile trennen: „|“ nur außerhalb von Klammern.
    Betragsstriche |AB| zerlegt das ebenfalls; Bruchstücke (Name zwischen den
    Strichen, Bindewörter, Teile mit „=“ am Anfang) werden mit ihren Nachbarn
    wieder verbunden, die Abstände bleiben wie im Original."""
    teile, tiefe, akt = [], 0, []
    for ch in stich:
        if ch == "(":
            tiefe += 1
        elif ch == ")":
            tiefe = max(0, tiefe - 1)
        if ch == "|" and tiefe == 0:
            teile.append("".join(akt))
            akt = []
        else:
            akt.append(ch)
    teile.append("".join(akt))
    out, glue = [], False
    for t in teile:
        st = t.strip()
        name = bool(NAME.fullmatch(st))
        schliesst = st == "" or name or bool(SCHLIESST.match(st))
        oeffnet = name or bool(OEFFNET.search(st))
        if out and (glue or schliesst):
            out[-1] = out[-1] + "|" + t
        else:
            out.append(t)
        glue = oeffnet
    return [t.strip() for t in out if t.strip()]


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def ist_rechenschritt(t):
    return bool(MATHE.search(t)) or len(t.split()) > 3


def main():
    args = sys.argv[1:]
    if args and args[0] == "--nur-spalten":
        kopf, zeilen = lade(args[1])
        neu = erweitere(kopf, zeilen)
        schreibe(args[1], kopf, zeilen)
        print(f"{args[1]}: Felder ergänzt {neu or 'keine'}, {len(zeilen)} Zeilen, {len(kopf)} Felder")
        return
    beitabelle, katalog = args[0], args[1]
    korrekturen, nur, streng = [], None, False
    rest = args[2:]
    while rest:
        a = rest.pop(0)
        if a == "--korrektur":
            continue
        if a == "--nur":
            nur = rest.pop(0)
            continue
        if a == "--streng":
            streng = True
            continue
        korrekturen.append(a.split("=", 3))

    kopf, zeilen = lade(katalog)
    neu = erweitere(kopf, zeilen)
    ix = {k: i for i, k in enumerate(kopf)}
    nach_id = {z[ix["id"]]: z for z in zeilen}
    with io.open(beitabelle, encoding="utf-8", newline="") as fh:
        bt = list(csv.DictReader(fh, delimiter=";"))
    if nur:
        bt = [r for r in bt if r["id"].startswith(nur + "-")]

    zw_abw, zweifel, abh_neu, verf_an, begriffe_weg, sympy = [], [], [], 0, [], {}
    fehlt = [r["id"] for r in bt if r["id"] not in nach_id]
    if fehlt:
        sys.exit(f"ids der Beitabelle nicht im Katalog: {fehlt}")
    for r in bt:
        z = nach_id[r["id"]]
        i = r["id"]
        # kurz → kurzloesung
        z[ix["kurzloesung"]] = markiere_vektoren(r["kurz"], zweifel, f"{i} kurzloesung")
        # zwischen → zwischenergebnis
        alt = z[ix["zwischenergebnis"]]
        if r["zwischen"]:
            neu_zw = markiere_vektoren(r["zwischen"], zweifel, f"{i} zwischenergebnis")
            if alt and norm(alt) != norm(r["zwischen"]):
                zw_abw.append((i, alt, r["zwischen"]))
            z[ix["zwischenergebnis"]] = neu_zw
        elif alt:
            z[ix["zwischenergebnis"]] = markiere_vektoren(alt, zweifel, f"{i} zwischenergebnis (alt)")
        # stich → stichwoerter; Rechenschritte der alten nach verfahren
        verf = z[ix["verfahren"]]
        anhang = []
        for t in schritte(z[ix["stichwoerter"]]):
            if any(norm(t) in norm(v) for v in (verf, r["stich"], r["kurz"], r["zwischen"], z[ix["ergebnis"]])):
                continue
            if bool(MATHE.search(t)) if streng else ist_rechenschritt(t):
                anhang.append(t)
            else:
                begriffe_weg.append((i, t))
        if anhang:
            z[ix["verfahren"]] = verf.rstrip() + "; " + "; ".join(anhang)
            verf_an += 1
        z[ix["stichwoerter"]] = r["stich"]
        # neben, abh
        z[ix["neben"]] = r["neben"]
        if r["abh"]:
            if not z[ix["abhaengig_von"]]:
                abh_neu.append(f"{i} ← {r['abh']}")
            elif z[ix["abhaengig_von"]] != r["abh"]:
                zweifel.append(f"{i}: abhaengig_von Katalog {z[ix['abhaengig_von']]} ≠ Beitabelle {r['abh']} (Beitabelle übernommen)")
            z[ix["abhaengig_von"]] = r["abh"]
        sympy.setdefault(r["sympy"].split(":")[0], []).append(i)

    for i, feld, alt, neu_w in korrekturen:
        z = nach_id[i]
        treffer = [f for f in (feld, "ergebnis", "kurzloesung") if alt in z[ix[f]]]
        for f in treffer:
            z[ix[f]] = z[ix[f]].replace(alt, neu_w)
        print(f"Korrektur {i}: {alt} → {neu_w} in {treffer or 'keinem Feld (nicht gefunden)'}")

    schreibe(katalog, kopf, zeilen)
    print(f"{katalog}: Felder ergänzt {neu or 'keine'}; {len(bt)} Zeilen übernommen, "
          f"{len(zeilen)} Zeilen, {len(kopf)} Felder")
    print(f"zwischenergebnis: {len(zw_abw)} Abweichungen Beitabelle ≠ alter Katalogwert")
    for i, a_, b_ in zw_abw:
        print(f"  {i}\n    alt: {a_}\n    neu: {b_}")
    print(f"abhaengig_von ergänzt ({len(abh_neu)}): {', '.join(abh_neu)}")
    print(f"verfahren: bei {verf_an} Zeilen Rechenschritte angehängt; "
          f"{len(begriffe_weg)} reine Begriffe weggefallen")
    for i, t in begriffe_weg:
        print(f"  weg {i}: {t}")
    print(f"Vektor-Zweifelsfälle ({len(zweifel)}):")
    for s in zweifel:
        print("  " + s)
    print("sympy: " + ", ".join(f"{k} {len(v)}" for k, v in sorted(sympy.items())))
    for k, v in sympy.items():
        if k != "ok" and k != "nicht rechenbar":
            print(f"  {k}: {', '.join(v)}")


if __name__ == "__main__":
    main()
