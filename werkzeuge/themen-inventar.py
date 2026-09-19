# -*- coding: utf-8 -*-
"""
themen-inventar.py v0.1 · 19.09.2026 · Themeninventar der vier Prüfungskataloge

Zählt je Profil (msa, fhr, abi, iqb) und je Paar (leitidee, thema) die
Katalogzeilen, die verschiedenen typ-Werte und die drei häufigsten Typen, und
schreibt werkzeuge/themen-inventar.md. Vorstufe der Themenkonkordanz
(themen.csv, Wurzel); das Zusammenführen der Namen entscheidet der Chat, nicht
dieses Skript. Namen werden wortgleich wiedergegeben, samt Tippfehlern – keine
Normalisierung, kein erfundener Name; ein leeres Feld erscheint als „(leer)".

Gezählt wird aus den Katalogen, nicht aus den Typenlisten: abitur-typen.csv ist
für abi und iqb gemeinsam und trägt kein Profilfeld. Die Typenlisten werden nur
für den Abschnitt „Befunde" gelesen (Themen dort ohne Katalogzeile und
umgekehrt). Referenz der Sek-I-Themennamen sind die Dateinamen in katalog/
(*.md ohne führenden Unterstrich, ohne Endung; index.md ist das Verzeichnis
der Einträge und kein Thema, es bleibt draußen).

Liest nur; einzige Ausgabe ist werkzeuge/themen-inventar.md.

Aufruf aus der Repo-Wurzel:
  python werkzeuge/themen-inventar.py
"""
import collections
import csv
import datetime
import io
import os

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/
VERSION = "themen-inventar.py v0.1"
AUSGABE = os.path.join(HIER, "werkzeuge", "themen-inventar.md")
LEER = "(leer)"

# Kataloge je Profil (msa: zwei Dateien, ein Profil)
KATALOGE = collections.OrderedDict([
    ("msa", ["msa/msa-katalog-basis.csv", "msa/msa-katalog-kontext.csv"]),
    ("fhr", ["fhr/fhr-katalog.csv"]),
    ("abi", ["abitur/abi-katalog.csv"]),
    ("iqb", ["abitur/iqb-katalog.csv"]),
])
# Typenlisten und die Profile, deren Kataloge sie abdecken
TYPENLISTEN = collections.OrderedDict([
    ("msa/msa-typen.csv", ["msa"]),
    ("fhr/fhr-typen.csv", ["fhr"]),
    ("abitur/abitur-typen.csv", ["abi", "iqb"]),
])
KATALOG_ORDNER = "katalog"


def lies_csv(relpfad):
    """Alle Zeilen einer Semikolon-CSV als Liste von dicts (Kopfzeile = Feldnamen)."""
    with io.open(os.path.join(HIER, relpfad), encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def wert(zeile, feld):
    """Feldwert wortgleich; leer wird als (leer) geführt, nicht übersprungen."""
    v = zeile.get(feld) or ""
    return v if v.strip() else LEER


def zelle(text):
    """Text für eine Markdown-Tabellenzelle: nur der Spaltentrenner wird maskiert."""
    return text.replace("|", "\\|")


def inventar():
    """Je Profil: Zeilen gesamt, je (leitidee, thema) Zeilenzahl und Typzähler."""
    ergebnis = collections.OrderedDict()
    for profil, dateien in KATALOGE.items():
        zeilen = []
        for d in dateien:
            zeilen.extend(lies_csv(d))
        paare = collections.OrderedDict()  # (leitidee, thema) -> {"zeilen": n, "typen": Counter}
        for z in zeilen:
            schluessel = (wert(z, "leitidee"), wert(z, "thema"))
            eintrag = paare.setdefault(schluessel, {"zeilen": 0, "typen": collections.Counter()})
            eintrag["zeilen"] += 1
            eintrag["typen"][wert(z, "typ")] += 1
        ergebnis[profil] = {
            "zeilen": len(zeilen),
            "paare": paare,
            "themen": {t for _, t in paare},
            "typen": {wert(z, "typ") for z in zeilen},
        }
    return ergebnis


def sek1_referenz():
    """Dateinamen in katalog/: *.md ohne führenden Unterstrich, ohne Endung; index.md ausgenommen."""
    namen = []
    for name in sorted(os.listdir(os.path.join(HIER, KATALOG_ORDNER))):
        if name.endswith(".md") and not name.startswith("_") and name != "index.md":
            namen.append(name[:-3])
    return namen


def typenlisten_themen():
    """Je Typenliste die Menge der Paare (leitidee, thema)."""
    return collections.OrderedDict(
        (pfad, {(wert(z, "leitidee"), wert(z, "thema")) for z in lies_csv(pfad)})
        for pfad in TYPENLISTEN
    )


def schreibe(inv, referenz, listen):
    heute = datetime.date.today().isoformat()
    out = []
    w = out.append
    w("# Themeninventar der vier Prüfungskataloge")
    w("")
    w(f"Erzeugt am {heute} von `{VERSION}` aus "
      + ", ".join(f"`{d}`" for dateien in KATALOGE.values() for d in dateien)
      + "; Typenlisten " + ", ".join(f"`{p}`" for p in TYPENLISTEN)
      + f"; Sek-I-Referenz aus `{KATALOG_ORDNER}/`.")
    w("")
    w("**Diese Datei wird abgeleitet und nie von Hand geändert.** Namen stehen wortgleich wie in den "
      "Dateien, samt Tippfehlern; ein leeres Feld heißt „(leer)\". Vorstufe der Themenkonkordanz – "
      "das Zusammenführen entscheidet der Chat, nicht das Skript.")
    w("")

    # ---- Kennzahlen
    w("## 1 Kennzahlen")
    w("")
    w("| Profil | Zeilen gesamt | Themen gesamt | Typen gesamt |")
    w("|---|---:|---:|---:|")
    for profil, e in inv.items():
        w(f"| {profil} | {e['zeilen']} | {len(e['themen'])} | {len(e['typen'])} |")
    w("")
    w("Themen gesamt = verschiedene Werte in `thema`; Typen gesamt = verschiedene Werte in `typ` "
      "(nur Haupttyp, `typ_neben` nicht gezählt).")
    w("")

    # ---- Themen je Profil
    w("## 2 Themen je Profil")
    w("")
    for profil, e in inv.items():
        w(f"### {profil}")
        w("")
        w("| Leitidee | Thema | Zeilen | Typen | drei häufigste Typen |")
        w("|---|---|---:|---:|---|")
        reihen = sorted(e["paare"].items(), key=lambda kv: (kv[0][0], -kv[1]["zeilen"], kv[0][1]))
        for (leitidee, thema), daten in reihen:
            top = " · ".join(f"{t} ({n})" for t, n in daten["typen"].most_common(3))
            w(f"| {zelle(leitidee)} | {zelle(thema)} | {daten['zeilen']} | {len(daten['typen'])} | {zelle(top)} |")
        w("")

    # ---- Namensgleiche Themen
    w("## 3 Namensgleiche Themen")
    w("")
    vorkommen = collections.OrderedDict()
    for profil, e in inv.items():
        for thema in sorted(e["themen"]):
            vorkommen.setdefault(thema, []).append(profil)
    gleich = [(t, p) for t, p in vorkommen.items() if len(p) > 1]
    if gleich:
        w("Themenname wortgleich in mehr als einem Profil:")
        w("")
        w("| Thema | Profile |")
        w("|---|---|")
        for thema, profile in sorted(gleich):
            w(f"| {zelle(thema)} | {', '.join(profile)} |")
    else:
        w("Kein Themenname kommt wortgleich in mehr als einem Profil vor.")
    w("")
    w(f"{len(gleich)} namensgleiche Themen.")
    w("")

    # ---- Sek-I-Referenz
    w("## 4 Sek-I-Referenz (Dateinamen in katalog/)")
    w("")
    w("| Name | wortgleich als Thema in |")
    w("|---|---|")
    treffer = 0
    for name in referenz:
        profile = [p for p, e in inv.items() if name in e["themen"]]
        if profile:
            treffer += 1
        w(f"| {zelle(name)} | {', '.join(profile) if profile else '–'} |")
    w("")
    w(f"{len(referenz)} Namen, {treffer} mit Treffer, {len(referenz) - treffer} ohne.")
    w("")

    # ---- Befunde
    w("## 5 Befunde")
    w("")
    w("Paare (Leitidee, Thema) je Typenliste gegen die Kataloge der Profile, die sie abdeckt.")
    w("")
    for pfad, profile in TYPENLISTEN.items():
        katalog_paare = set()
        for p in profile:
            katalog_paare |= set(inv[p]["paare"])
        nur_liste = sorted(listen[pfad] - katalog_paare)
        nur_katalog = sorted(katalog_paare - listen[pfad])
        w(f"### `{pfad}` gegen {', '.join(profile)}")
        w("")
        w(f"In der Typenliste, in keinem Katalog ({len(nur_liste)}):")
        w("")
        for leitidee, thema in nur_liste:
            w(f"- {leitidee} / {thema}")
        if not nur_liste:
            w("- keine")
        w("")
        w(f"Im Katalog, nicht in der Typenliste ({len(nur_katalog)}):")
        w("")
        for leitidee, thema in nur_katalog:
            w(f"- {leitidee} / {thema}")
        if not nur_katalog:
            w("- keine")
        w("")

    with io.open(AUSGABE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out))
    return len(out), len(gleich), treffer, len(referenz)


def main():
    inv = inventar()
    referenz = sek1_referenz()
    listen = typenlisten_themen()
    n_zeilen, n_gleich, n_treffer, n_ref = schreibe(inv, referenz, listen)
    print(f"{os.path.relpath(AUSGABE, HIER)} geschrieben: {n_zeilen} Zeilen.")
    for profil, e in inv.items():
        print(f"  {profil}: {e['zeilen']} Zeilen, {len(e['themen'])} Themen, {len(e['typen'])} Typen")
    print(f"  namensgleiche Themen: {n_gleich}; Sek-I-Referenz: {n_ref} Namen, {n_treffer} mit Treffer")


if __name__ == "__main__":
    main()
