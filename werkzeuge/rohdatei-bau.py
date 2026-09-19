# -*- coding: utf-8 -*-
"""
rohdatei-bau.py v0.2 · 19.09.2026 · Rohdatei je kanonischem Thema

Änderungen gegenüber 0.1 (Auftrag Rohdateien für alle Themen, 19.09.2026):
Teil C (Sammlung der Fehlerquellen und Stichwörter) gestrichen – im Probelauf
kam fast jeder Wert genau einmal vor, die Zählung trug nichts. Teil A und B,
Zeilenform und Sortierung unverändert.

Eine Rohdatei ist der Lesestoff, aus dem ein Chat den Themenkatalog-Eintrag
schreibt: alles, was zu einem kanonischen Thema aus themen.csv in den fünf
Prüfungskatalogen tatsächlich geprüft wird. Je Thema entsteht
rohdaten/<kanonisch>.md, abgeleitet und nie von Hand geändert:

  Kopf     – Titel, Stufe, je Profilthema eine Zeile mit Zeilenzahl aus
             themen.csv, Stand (Datum, kurzer Hash des HEAD-Commits).
  Teil A   – Typenprofil: jeder typ der zugehörigen Zeilen, absteigend nach
             Zeilenzahl, mit Profilen, Jahren, Status und Definition aus der
             Typenliste des Profils (msa/msa-typen.csv, fhr/fhr-typen.csv,
             abitur/abitur-typen.csv für abi und iqb; steht der Name in
             mehreren Listen, alle Definitionen); danach die Nebentypen aus
             typ_neben mit Zeilenzahl.
  Teil B   – Zeilenliste: eine Zeile je Katalogzeile, sortiert nach Profil
             (msa, fhr, abi, iqb), typ, jahr, id, mit Zwischenüberschrift je
             Profil; Form id | punkte | hilfsmittel | format · operator |
             gegeben → gesucht | verfahren. Senkrechte Striche im Inhalt
             werden zu ¦, Zeilenumbrüche zu Leerzeichen; nichts wird gekürzt.

Listenfelder (typ_neben) trennen mehrere Werte mit „|" (katalog-prompt.md § 5).
Zuordnung Katalogzeile → Thema über (profil, leitidee, thema) aus themen.csv;
jede Zeile landet so in höchstens einer Rohdatei. Vor dem Schreiben wird je
Profilthema geprüft, dass die Zeilenzahl der Spalte zeilen in themen.csv
entspricht; bei Abweichung wird nichts geschrieben.

Liest nur; einzige Ausgabe sind die Dateien unter rohdaten/.

Aufruf aus der Repo-Wurzel:
  python werkzeuge/rohdatei-bau.py               alle kanonischen Themen mit Katalogzeilen
  python werkzeuge/rohdatei-bau.py <thema> ...   nur die genannten
"""
import collections
import csv
import datetime
import io
import os
import re
import subprocess
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/
VERSION = "rohdatei-bau.py v0.2"
KONKORDANZ = "themen.csv"
AUSGABE = "rohdaten"
PROFILE = ["msa", "fhr", "abi", "iqb"]  # Reihenfolge in Teil B
KATALOGE = collections.OrderedDict([
    ("msa", ["msa/msa-katalog-basis.csv", "msa/msa-katalog-kontext.csv"]),
    ("fhr", ["fhr/fhr-katalog.csv"]),
    ("abi", ["abitur/abi-katalog.csv"]),
    ("iqb", ["abitur/iqb-katalog.csv"]),
])
TYPENLISTEN = collections.OrderedDict([
    ("msa/msa-typen.csv", ["msa"]),
    ("fhr/fhr-typen.csv", ["fhr"]),
    ("abitur/abitur-typen.csv", ["abi", "iqb"]),
])
TRENNER = "|"  # mehrere Werte in einem Feld (katalog-prompt.md § 5)


def lies_csv(relpfad):
    with io.open(os.path.join(HIER, relpfad), encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def head_kurz():
    """Kurzer Hash des HEAD-Commits: git, sonst aus .git gelesen (git liegt hier nicht im PATH)."""
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=HIER, capture_output=True,
                              text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    try:
        head = io.open(os.path.join(HIER, ".git", "HEAD"), encoding="utf-8").read().strip()
        if head.startswith("ref: "):
            ref = head[5:]
            pfad = os.path.join(HIER, ".git", *ref.split("/"))
            if os.path.exists(pfad):
                return io.open(pfad, encoding="utf-8").read().strip()[:7]
            for zeile in io.open(os.path.join(HIER, ".git", "packed-refs"), encoding="utf-8"):
                if zeile.strip().endswith(" " + ref):
                    return zeile.split()[0][:7]
        return head[:7]
    except OSError:
        return "unbekannt"


def glatt(text):
    """Feldinhalt für eine Zeile von Teil B: | -> ¦, Zeilenumbrüche -> Leerzeichen, nichts gekürzt."""
    return re.sub(r"\s*[\r\n]+\s*", " ", text).replace("|", "¦")


def einzelwerte(text):
    return [t.strip() for t in text.split(TRENNER) if t.strip()]


def lade():
    """Konkordanz, Kataloge (je Zeile mit profil) und Typenlisten."""
    konk = lies_csv(KONKORDANZ)
    zuordnung = {}  # (profil, leitidee, thema) -> kanonisch
    themen = collections.OrderedDict()  # kanonisch -> Zeilen der Konkordanz
    for z in konk:
        themen.setdefault(z["kanonisch"], []).append(z)
        if z["profil"]:
            k = (z["profil"], z["leitidee"], z["thema"])
            if k in zuordnung and zuordnung[k] != z["kanonisch"]:
                sys.exit(f"{KONKORDANZ}: {k} zwei kanonischen Themen zugeordnet: {zuordnung[k]}, {z['kanonisch']}")
            zuordnung[k] = z["kanonisch"]
    zeilen = collections.OrderedDict((k, []) for k in themen)
    ohne = []
    for profil, dateien in KATALOGE.items():
        for d in dateien:
            for z in lies_csv(d):
                z["profil"] = profil
                k = zuordnung.get((profil, z["leitidee"], z["thema"]))
                if k is None:
                    ohne.append(f"{profil} / {z['leitidee']} / {z['thema']} ({z['id']})")
                else:
                    zeilen[k].append(z)
    if ohne:
        sys.exit("Katalogzeilen ohne Zuordnung in themen.csv:\n  " + "\n  ".join(ohne))
    typen = {}  # typname -> [(liste, status, definition)]
    for pfad in TYPENLISTEN:
        for t in lies_csv(pfad):
            typen.setdefault(t["typ"], []).append((pfad, t["status"], t["definition"]))
    return themen, zeilen, typen


def pruefe_zahlen(kanonisch, konk_zeilen, kat_zeilen):
    """Zeilenzahl je Profilthema gegen Spalte zeilen; Summe gegen Teil B."""
    fehler = []
    ist = collections.Counter((z["profil"], z["leitidee"], z["thema"]) for z in kat_zeilen)
    soll_summe = 0
    for z in konk_zeilen:
        if not z["profil"]:
            continue
        soll = int(z["zeilen"])
        soll_summe += soll
        n = ist.get((z["profil"], z["leitidee"], z["thema"]), 0)
        if n != soll:
            fehler.append(f"{kanonisch}: {z['profil']} / {z['thema']}: themen.csv {soll} Zeilen, Katalog {n}")
    if len(kat_zeilen) != soll_summe:
        fehler.append(f"{kanonisch}: Teil B {len(kat_zeilen)} Zeilen, Summe zeilen in themen.csv {soll_summe}")
    return fehler


def baue(kanonisch, konk_zeilen, kat_zeilen, typen, stand):
    """Text der Rohdatei und Kennzahlen für den Bericht."""
    out = []
    w = out.append
    stufen = sorted({z["stufe"] for z in konk_zeilen})
    w(f"# Rohdatei {kanonisch}")
    w("")
    w(f"Stufe: {', '.join(stufen)}")
    w("")
    for z in konk_zeilen:
        if z["profil"]:
            w(f"- {z['profil']}: {z['thema']} ({z['zeilen']} Zeilen)")
    w("")
    w(f"Stand: {stand}")
    w("")

    # ---- Teil A
    w("## A Typenprofil")
    w("")
    je_typ = collections.OrderedDict()
    for z in kat_zeilen:
        je_typ.setdefault(z["typ"], []).append(z)
    reihen = sorted(je_typ.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ohne_def = 0
    for typ, zs in reihen:
        profile = collections.Counter(z["profil"] for z in zs)
        jahre = sorted(z["jahr"] for z in zs)
        spanne = jahre[0] if jahre[0] == jahre[-1] else f"{jahre[0]}–{jahre[-1]}"
        prof = " ".join(f"{p} {profile[p]}" for p in PROFILE if p in profile)
        w(f"**{typ}** · {len(zs)} {'Zeile' if len(zs) == 1 else 'Zeilen'} · {prof} · Jahre {spanne}")
        listen = [pfad for pfad, ps in TYPENLISTEN.items() if any(p in profile for p in ps)]
        gefunden = typen.get(typ, [])
        fehlt = False
        for pfad in listen:
            treffer = [(s, d) for (l, s, d) in gefunden if l == pfad and d.strip()]
            if treffer:
                for status, definition in treffer:
                    w(f"{pfad} ({status}): {definition}")
            else:
                w(f"(keine Definition in {pfad})")
                fehlt = True
        for (l, s, d) in gefunden:
            if l not in listen and d.strip():
                w(f"{l} ({s}): {d}")
        if fehlt:
            ohne_def += 1
        w("")
    neben = collections.Counter(t for z in kat_zeilen for t in einzelwerte(z["typ_neben"]))
    if neben:
        w("**Nebentypen:** " + " · ".join(f"{t} ({n})" for t, n in sorted(neben.items(), key=lambda kv: (-kv[1], kv[0]))))
    else:
        w("**Nebentypen:** keine")
    w("")

    # ---- Teil B
    w("## B Zeilenliste")
    w("")
    reihenfolge = {p: i for i, p in enumerate(PROFILE)}
    sortiert = sorted(kat_zeilen, key=lambda z: (reihenfolge[z["profil"]], z["typ"], z["jahr"], z["id"]))
    aktuell = None
    for z in sortiert:
        if z["profil"] != aktuell:
            aktuell = z["profil"]
            w(f"## {aktuell}")
            w("")
        w(" | ".join([glatt(z["id"]), glatt(z["punkte"]), glatt(z["hilfsmittel"]),
                      glatt(z["format"]) + " · " + glatt(z["operator"]),
                      glatt(z["gegeben"]) + " → " + glatt(z["gesucht"]),
                      glatt(z["verfahren"])]))
    w("")
    text = "\n".join(out)
    return text, {
        "zeilen_b": len(sortiert),
        "typen_a": len(reihen),
        "ohne_definition": ohne_def,
    }


def main():
    themen, zeilen, typen = lade()
    mit = [k for k, zs in zeilen.items() if zs]
    ohne = [k for k, zs in zeilen.items() if not zs]
    gewuenscht = sys.argv[1:] or mit
    unbekannt = [k for k in gewuenscht if k not in themen]
    if unbekannt:
        sys.exit(f"nicht in {KONKORDANZ}: {', '.join(unbekannt)}")
    leer = [k for k in gewuenscht if not zeilen[k]]
    if leer:
        sys.exit(f"keine Katalogzeilen, keine Rohdatei: {', '.join(leer)}")

    stand = f"{datetime.date.today().isoformat()}, Commit {head_kurz()}"
    fehler = []
    ergebnisse = collections.OrderedDict()
    for k in gewuenscht:
        fehler += pruefe_zahlen(k, themen[k], zeilen[k])
        ergebnisse[k] = baue(k, themen[k], zeilen[k], typen, stand)
    if fehler:
        print("ABBRUCH – Zeilenzahlen weichen von themen.csv ab, nichts geschrieben:")
        for f in fehler:
            print("  -", f)
        return 1

    ordner = os.path.join(HIER, AUSGABE)
    os.makedirs(ordner, exist_ok=True)
    for k, (text, kenn) in ergebnisse.items():
        pfad = os.path.join(ordner, f"{k}.md")
        with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        groesse = os.path.getsize(pfad)
        print(f"{AUSGABE}/{k}.md: Teil B {kenn['zeilen_b']} Zeilen; Teil A {kenn['typen_a']} Typen, "
              f"{kenn['ohne_definition']} ohne Definition; {text.count(chr(10)) + 1} Zeilen, {groesse / 1024:.1f} KB")
    print(f"{len(ergebnisse)} Rohdateien geschrieben; kanonische Themen mit Katalogzeilen: {len(mit)}, "
          f"ohne: {len(ohne)} ({', '.join(ohne) or 'keine'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
