# -*- coding: utf-8 -*-
"""fhr-typenbibliothek.py – erzeugt fhr-typenbibliothek.md aus dem Katalog.
Version 0.1 · 12.09.2026 · Profil fhr · gilt mit katalog-prompt.md v0.3 und fhr.md v1.5

Die Bibliothek wird abgeleitet, nie von Hand geändert (konzept.md § 2). Nach jeder
Katalogänderung neu erzeugen:

    python3 fhr-typenbibliothek.py

Es liest fhr-katalog.csv und fhr-typen.csv aus demselben Verzeichnis und schreibt
fhr-typenbibliothek.md. Alles, was die Ausgabe enthält, folgt aus diesen beiden Dateien.

ZÄHLWEISE – hier steht, was die Ausgabe bedeutet:

1. Ein "Original" eines Typs ist eine Katalogzeile, in der er im Feld typ steht. Zeilen,
   in denen er nur in typ_neben vorkommt, werden getrennt als "Nebenvorkommen" geführt und
   nirgends mit den Originalen vermischt. Grund: Für eine Heftkette ist der Typ die
   Hauptnummer; eine Zeile, die ihn nur nebenbei verlangt, taugt nicht als deren Decke.

2. DECKENKANDIDAT ist eine vorläufige Rechnung, keine Regel. blatt-konzept.md § 3 nennt als
   Decke das Original mit den meisten Merkmalen (bei Gleichstand Punkte, dann jüngeres Jahr),
   aber "Merkmal" ist kein Katalogfeld; welche Felder es abbilden und in welcher Rangfolge,
   ist am 12.09.2026 bewusst offen geblieben (blatt-konzept.md § 7). Dieses Skript rechnet
   ersatzweise mit

       M = Leistungen / Typen / Schritte

   also der Zahl der durch "|" getrennten Einträge in gesucht, der Zahl der Einträge in typ
   plus typ_neben und dem Wert von schritte, lexikographisch in dieser Reihenfolge, danach
   punkte, danach jahr. Bekannte Schwäche: Aussagenlisten stehen in gesucht als eine einzige
   Leistung, obwohl mehrere Aussagen zu begründen sind (2019-C-1a: 8 BE, vier Aussagen). Solche
   Zeilen werden von dieser Rechnung unterschätzt und sind in der Ausgabe mit "!" markiert.
   Die Zahlen sind Lesehilfe für die Bauplanung, kein Ersatz für die Entscheidung beim Bau.

3. Ein Thema, das in keiner Zeile das Feld thema stellt, trägt kein eigenes Heft; solche
   Themen stehen im Überblick eigens vermerkt (fhr.md § 6).
"""
import csv, io, os, sys, collections, datetime

KAT = "fhr-katalog.csv"
TYP = "fhr-typen.csv"
AUS = "fhr-typenbibliothek.md"
SKRIPT = "fhr-typenbibliothek.py v0.1"

# Reihenfolge der Leitideen und Themen nach fhr.md Abschnitt 6.
THEMEN = [
    ("Differentialrechnung", ["Ableitungen bilden", "Nullstellen ganzrationaler Funktionen",
        "Extrem- und Sattelpunkte", "Monotonie und Krümmung", "Wendepunkte", "Symmetrie nachweisen",
        "Verhalten im Unendlichen", "Graph zeichnen und zuordnen", "Anstieg und Tangente", "Normale",
        "Schnittpunkte von Funktionsgraphen", "Funktionsgleichung bestimmen", "Extremwertaufgaben"]),
    ("Integralrechnung", ["Stammfunktion bilden", "Bestimmtes Integral berechnen",
        "Fläche zwischen Graph und x-Achse", "Fläche zwischen zwei Graphen",
        "Rotationsvolumen um die x-Achse", "Körpervolumen aus Grundfläche und Länge"]),
    ("Stochastik", ["Daten darstellen und aufbereiten", "Statistische Kenngrößen",
        "Mehrstufige Zufallsexperimente", "Baumdiagramm und Pfadregeln",
        "Unabhängigkeit von Ereignissen", "Erwartungswert", "Kombinatorische Abzählverfahren",
        "Laplace-Wahrscheinlichkeit"]),
    ("Grundlagen", ["Prozentrechnung", "Gleichungen lösen", "Größen und Einheiten", "Terme umformen"]),
]


def lade(pfad, pflichtkopf=None):
    if not os.path.exists(pfad):
        sys.exit(f"{pfad} fehlt – Katalogdateien neben dieses Skript legen.")
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    if not rows:
        sys.exit(f"{pfad} ist leer.")
    return rows[0], rows[1:]


def leistungen(z):
    return len([s for s in z["gesucht"].split("|") if s])


def typzahl(z):
    return len([s for s in (z["typ"] + "|" + z["typ_neben"]).split("|") if s])


def merkmale(z):
    return (leistungen(z), typzahl(z), int(z["schritte"]))


def rang(z):
    return (merkmale(z), int(z["punkte"]), int(z["jahr"]))


def aussagenliste(z):
    """Zeilen, die die Merkmalsrechnung unterschätzt: mehrere Aussagen, aber eine Leistung
    in gesucht. Erkannt an mehreren nummerierten Aussagen in stichwoerter."""
    if leistungen(z) > 2:
        return False
    s = z["stichwoerter"]
    marken = sum(s.count(m) for m in ("Aussage", "(I)", "(1)", "(2)", "(3)", "(4)"))
    return marken >= 2


def main():
    kopf, zeilen = lade(KAT)
    D = [dict(zip(kopf, r)) for r in zeilen]
    _, trows = lade(TYP)
    typen = [dict(zip(["typ", "leitidee", "thema", "definition", "beispiel_id", "status"], r))
             for r in trows]

    haupt = collections.defaultdict(list)
    neben = collections.defaultdict(list)
    for z in D:
        haupt[z["typ"]].append(z)
        for t in [s for s in z["typ_neben"].split("|") if s]:
            neben[t].append(z)

    # Themen, die in keiner Zeile das Feld thema stellen
    gestellt = {z["thema"] for z in D}
    ohne_heft = [(li, th) for li, ths in THEMEN for th in ths if th not in gestellt]

    hefte = sorted({(z["jahr"], z["papier"]) for z in D})
    unbekannt = [t["typ"] for t in typen
                 if t["leitidee"] not in dict(THEMEN) or t["thema"] not in dict(THEMEN)[t["leitidee"]]]
    if unbekannt:
        sys.exit(f"Typen mit unbekannter Leitidee oder Thema: {unbekannt}")

    o = []
    w = o.append
    w("# FHR – Typenbibliothek")
    w("")
    w(f"Erzeugt am {datetime.date.today().isoformat()} von `{SKRIPT}` aus `{KAT}` "
      f"({len(D)} Zeilen, {len(hefte)} Hefte, Punktsumme {sum(int(z['punkte']) for z in D)}) "
      f"und `{TYP}` ({len(typen)} Typen).")
    w("")
    w("**Diese Datei wird abgeleitet und nie von Hand geändert** (konzept.md § 2). Nach jeder "
      "Katalogänderung mit dem Skript neu erzeugen; Korrekturen gehören in den Katalog, nicht hierher.")
    w("")
    w("Gliederung nach Leitidee, Thema und Typ wie in fhr.md § 6. Je Typ stehen die Definition aus "
      "`fhr-typen.csv`, die **Originale** (Zeilen, in denen der Typ das Feld `typ` stellt) und die "
      "**Nebenvorkommen** (Zeilen, in denen er nur in `typ_neben` steht). Für eine Heftkette zählt die "
      "erste Gruppe: Die Hauptnummer eines Hefts ist ein Typ, und nur eine Zeile, die ihn selbst "
      "verlangt, taugt als deren Decke.")
    w("")
    w("Zu jeder Zeile steht `P` für die Punkte und `M` für die Merkmalszahlen "
      "Leistungen / Typen / Schritte. **Der Deckenkandidat ist eine vorläufige Rechnung, keine Regel.** "
      "blatt-konzept.md § 3 nennt als Decke das Original mit den meisten Merkmalen (bei Gleichstand "
      "Punkte, dann jüngeres Jahr); was ein Merkmal ist, ist bewusst offen (blatt-konzept.md § 7). "
      "Das Skript rechnet ersatzweise nach M, dann Punkte, dann Jahr. Zeilen mit `!` sind "
      "Aussagenlisten: Sie stehen in `gesucht` als eine Leistung, verlangen aber mehrere Begründungen, "
      "und werden von dieser Rechnung unterschätzt. Beim Bau entscheidet der Prompt, das Protokoll "
      "weist die Wahl aus.")
    w("")

    # ---- Überblick
    w("## Überblick")
    w("")
    w("| Leitidee | Thema | Typen | Originale | Typen mit nur einem Original |")
    w("|---|---|---|---|---|")
    for li, ths in THEMEN:
        for th in ths:
            tl = [t for t in typen if t["leitidee"] == li and t["thema"] == th]
            orig = sum(len(haupt[t["typ"]]) for t in tl)
            einzeln = sum(1 for t in tl if len(haupt[t["typ"]]) == 1)
            leer = " –" if th not in gestellt else ""
            w(f"| {li} | {th}{leer} | {len(tl)} | {orig} | {einzeln} |")
    w("")
    if ohne_heft:
        w("Themen mit „–\": Sie stellen in keiner Katalogzeile das Feld `thema`, ihre Typen kommen nur "
          "innerhalb anderer Aufgaben vor. Aus ihnen lässt sich kein eigenes Heft bauen "
          "(fhr.md § 6): " + ", ".join(f"{th}" for _, th in ohne_heft) + ".")
        w("")

    mehrere = [t for t in typen if len(haupt[t["typ"]]) > 1]
    ohne = [t for t in typen if not haupt[t["typ"]] and not neben[t["typ"]]]
    w(f"Von {len(typen)} Typen stellen {sum(1 for t in typen if haupt[t['typ']])} mindestens einmal das "
      f"Feld `typ`; bei {len(mehrere)} davon stehen mehrere Originale zur Wahl, dort ist der "
      f"Deckenkandidat ausgewiesen. "
      f"{sum(1 for t in typen if len(haupt[t['typ']]) == 1)} Typen haben genau ein Original.")
    if ohne:
        w("")
        w("Ohne jedes Vorkommen: " + ", ".join(t["typ"] for t in ohne) + ".")
    w("")

    # ---- Hauptteil
    for li, ths in THEMEN:
        w(f"## {li}")
        w("")
        for th in ths:
            tl = sorted([t for t in typen if t["leitidee"] == li and t["thema"] == th],
                        key=lambda t: (-len(haupt[t["typ"]]), t["typ"]))
            orig = sum(len(haupt[t["typ"]]) for t in tl)
            marke = "  ·  kein eigenes Heft baubar" if th not in gestellt else ""
            w(f"### {th}")
            w("")
            w(f"*{len(tl)} Typen, {orig} Originale{marke}*")
            w("")
            for t in tl:
                w(f"**{t['typ']}**  ")
                w(f"{t['definition']}  ")
                H = sorted(haupt[t["typ"]], key=rang, reverse=True)
                if H:
                    teile = []
                    for i, z in enumerate(H):
                        m = "/".join(str(x) for x in merkmale(z))
                        mark = "!" if aussagenliste(z) else ""
                        spitze = " ←" if (len(H) > 1 and i == 0) else ""
                        teile.append(f"`{z['id']}`{mark} P{z['punkte']} M{m}{spitze}")
                    w("Originale: " + " · ".join(teile) + "  ")
                    if len(H) > 1:
                        w(f"Deckenkandidat: `{H[0]['id']}` (vorläufig, siehe Kopf)  ")
                else:
                    w("Originale: keine – kommt nur als Nebentyp vor  ")
                N = sorted(neben[t["typ"]], key=lambda z: z["id"])
                if N:
                    w("Nebenvorkommen: " + ", ".join(f"`{z['id']}`" for z in N) + "  ")
                w("")
        w("")

    with io.open(AUS, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(o) + "\n")
    print(f"{AUS} geschrieben: {len(o)} Zeilen, {len(typen)} Typen, {len(D)} Katalogzeilen.")
    print(f"Themen ohne eigenes Heft: {len(ohne_heft)} | Typen mit mehreren Originalen: {len(mehrere)}")


if __name__ == "__main__":
    main()
