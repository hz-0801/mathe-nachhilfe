# -*- coding: utf-8 -*-
"""
themen-pruef.py v0.2 · 20.09.2026 · Prüfung der Themenkonkordanz themen.csv

Änderungen gegenüber 0.1 (Auftrag E37 abschließen, 20.09.2026): Prüfung 4
kennt die Namensregel der Entscheidung 37 (konzept.md § 4) – ein kanonischer
Sek-II-Name, der weder Vokabular- noch abi/iqb-Thema ist, besteht, wenn er
eine eigene Katalogdatei hat (erster Fall zufallsexperimente-und-pfadregeln,
Commit 3d33427; seit b996221 mit Datei). Die Ausnahme „kombinatorik" in
Prüfung 3 ist gestrichen: das Thema trägt seit 3d33427 Stufe II und seit
diesem Auftrag eine Katalogdatei.

Prüft themen.csv (Repo-Wurzel) gegen die fünf Katalogdateien, den Themenkatalog
katalog/ und die Themenliste in abitur/abitur-vokabular.md § 2. Liest nur,
ändert keine Datei. Vier Prüfungen:

  1. Jedes Paar (leitidee, thema) jedes Profils (msa = Basis + Kontext, fhr,
     abi, iqb) steht genau einmal in themen.csv, und jede Profilzeile in
     themen.csv hat ein Gegenstück im Katalog.
  2. zeilen und typen jeder Profilzeile stimmen mit der Zählung aus dem
     Katalog überein (typen = verschiedene Werte in typ).
  3. Jede Datei katalog/*.md ohne führenden Unterstrich und ohne index.md
     kommt als kanonisch vor, und jeder kanonisch mit Stufe I hat eine
     Katalogdatei – außer funktionen-allgemein.
  4. Jeder kanonisch mit Stufe II ist ein Thema aus abitur-vokabular.md
     (Umschrift: Kleinschreibung, ä→ae ö→oe ü→ue ß→ss, alles andere als
     Buchstabe oder Ziffer wird zum Bindestrich), hat eine abi/iqb-Zeile,
     deren Thema in dieser Umschrift der kanonische Schlüssel ist, oder hat
     eine eigene Katalogdatei (Entscheidung 37: eigener Sek-II-Eintrag unter
     eigenem kanonischem Thema; ohne Datei bleibt ein solcher Name eine
     Abweichung, bis der Eintrag gebaut ist).

Stufe I+II zählt für 3 und 4. Ausgabe je Prüfung „bestanden" oder die
Abweichungen; Rückgabewert 0 nur, wenn alle vier bestehen.

Aufruf aus der Repo-Wurzel (nach jeder Katalogänderung):
  python werkzeuge/themen-pruef.py
"""
import collections
import csv
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/
VERSION = "themen-pruef.py v0.2"
KONKORDANZ = "themen.csv"
KATALOGE = collections.OrderedDict([
    ("msa", ["msa/msa-katalog-basis.csv", "msa/msa-katalog-kontext.csv"]),
    ("fhr", ["fhr/fhr-katalog.csv"]),
    ("abi", ["abitur/abi-katalog.csv"]),
    ("iqb", ["abitur/iqb-katalog.csv"]),
])
KATALOG_ORDNER = "katalog"
VOKABULAR = "abitur/abitur-vokabular.md"
OHNE_KATALOGDATEI = {"funktionen-allgemein"}  # v0.2: kombinatorik hat seit 20.09.2026 eine Datei (Stufe II)
KOPF = ["kanonisch", "stufe", "profil", "leitidee", "thema", "zeilen", "typen", "bemerkung"]
UMLAUTE = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}


def lies_csv(relpfad):
    with io.open(os.path.join(HIER, relpfad), encoding="utf-8-sig", newline="") as fh:  # -sig: eine BOM stört die Kopfzeile nicht
        return list(csv.DictReader(fh, delimiter=";"))


def umschrift(name):
    """'Lage- und Streumaße einer Stichprobe' -> 'lage-und-streumasse-einer-stichprobe'."""
    s = name.lower()
    for a, b in UMLAUTE.items():
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def vokabular_themen():
    """Themen aus abitur-vokabular.md § 2: Zeilen '**Sachgebiet:** A · B · C' bis zur Leerzeile."""
    with io.open(os.path.join(HIER, VOKABULAR), encoding="utf-8") as fh:
        text = fh.read()
    teile = re.split(r"^## ", text, flags=re.M)
    abschnitt = next((t for t in teile if "Themenliste" in t.splitlines()[0]), None)
    if abschnitt is None:
        sys.exit(f"{VOKABULAR}: Abschnitt „Themenliste“ nicht gefunden.")
    themen = set()
    for m in re.finditer(r"^\*\*([^*:]+):\*\*(.+?)(?=\n\s*\n)", abschnitt, re.S | re.M):
        themen.update(s.strip() for s in re.sub(r"\s+", " ", m.group(2)).split("·") if s.strip())
    if not themen:
        sys.exit(f"{VOKABULAR}: keine Themenzeile in der Themenliste gefunden.")
    return themen


def katalog_zaehlung():
    """Je Profil: (leitidee, thema) -> {'zeilen': n, 'typen': Menge der typ-Werte}."""
    zaehlung = collections.OrderedDict()
    for profil, dateien in KATALOGE.items():
        paare = {}
        for d in dateien:
            for z in lies_csv(d):
                e = paare.setdefault((z["leitidee"], z["thema"]), {"zeilen": 0, "typen": set()})
                e["zeilen"] += 1
                e["typen"].add(z["typ"])
        zaehlung[profil] = paare
    return zaehlung


def main():
    zeilen = lies_csv(KONKORDANZ)
    if not zeilen or list(zeilen[0].keys()) != KOPF:
        sys.exit(f"{KONKORDANZ}: Kopfzeile weicht ab, erwartet {';'.join(KOPF)}")
    kataloge = katalog_zaehlung()
    befunde = collections.OrderedDict((k, []) for k in ("1 Paare", "2 Zahlen", "3 Sek I", "4 Sek II"))

    # ---- 1 Paare: Katalog <-> Konkordanz, genau einmal
    profilzeilen = [z for z in zeilen if z["profil"].strip()]
    for z in profilzeilen:
        if z["profil"] not in KATALOGE:
            befunde["1 Paare"].append(f"unbekanntes Profil „{z['profil']}“: {z['kanonisch']} / {z['leitidee']} / {z['thema']}")
    vorkommen = collections.Counter((z["profil"], z["leitidee"], z["thema"]) for z in profilzeilen)
    for profil, paare in kataloge.items():
        for (leitidee, thema) in sorted(paare):
            n = vorkommen.get((profil, leitidee, thema), 0)
            if n == 0:
                befunde["1 Paare"].append(f"Katalogpaar fehlt in {KONKORDANZ}: {profil} / {leitidee} / {thema}")
            elif n > 1:
                befunde["1 Paare"].append(f"Katalogpaar {n}-mal in {KONKORDANZ}: {profil} / {leitidee} / {thema}")
    for (profil, leitidee, thema) in vorkommen:
        if profil in KATALOGE and (leitidee, thema) not in kataloge[profil]:
            befunde["1 Paare"].append(f"Zeile ohne Gegenstück im Katalog: {profil} / {leitidee} / {thema}")

    # ---- 2 Zahlen: zeilen und typen
    for z in profilzeilen:
        k = kataloge.get(z["profil"], {}).get((z["leitidee"], z["thema"]))
        if k is None:
            continue  # schon unter 1 gemeldet
        soll_z, soll_t = k["zeilen"], len(k["typen"])
        if z["zeilen"].strip() != str(soll_z) or z["typen"].strip() != str(soll_t):
            befunde["2 Zahlen"].append(
                f"{z['profil']} / {z['leitidee']} / {z['thema']}: {KONKORDANZ} zeilen={z['zeilen']} typen={z['typen']}, "
                f"Katalog zeilen={soll_z} typen={soll_t}")

    # ---- 3 Sek I: katalog/*.md <-> kanonisch mit Stufe I
    dateien = sorted(n[:-3] for n in os.listdir(os.path.join(HIER, KATALOG_ORDNER))
                     if n.endswith(".md") and not n.startswith("_") and n != "index.md")
    kanonisch = collections.OrderedDict()
    for z in zeilen:
        kanonisch.setdefault(z["kanonisch"], []).append(z)
    for name in dateien:
        if name not in kanonisch:
            befunde["3 Sek I"].append(f"Katalogdatei ohne Zeile in {KONKORDANZ}: {KATALOG_ORDNER}/{name}.md")
    for name, zs in kanonisch.items():
        stufen = {s.strip() for z in zs for s in z["stufe"].split("+")}
        if "I" in stufen and name not in dateien and name not in OHNE_KATALOGDATEI:
            befunde["3 Sek I"].append(f"kanonisch mit Stufe I ohne Katalogdatei: {name}")

    # ---- 4 Sek II: kanonisch mit Stufe II <-> Themenliste des Vokabulars
    # (oder eigene Katalogdatei nach Entscheidung 37, v0.2)
    vokabular = {umschrift(t) for t in vokabular_themen()}
    for name, zs in kanonisch.items():
        stufen = {s.strip() for z in zs for s in z["stufe"].split("+")}
        if "II" not in stufen:
            continue
        if name in vokabular:
            continue
        if any(z["profil"] in ("abi", "iqb") and umschrift(z["thema"]) == name for z in zs):
            continue
        if name in dateien:
            continue  # Entscheidung 37: eigener Sek-II-Eintrag unter eigenem kanonischem Namen
        befunde["4 Sek II"].append(f"kanonisch mit Stufe II weder Vokabularthema noch abi/iqb-Thema noch Katalogdatei: {name}")

    # ---- Ausgabe
    print(f"{VERSION}: {len(zeilen)} Zeilen in {KONKORDANZ}, {len(kanonisch)} kanonische Themen, "
          f"{len(profilzeilen)} Profilzeilen; Kataloge: "
          + ", ".join(f"{p} {len(k)} Paare" for p, k in kataloge.items())
          + f"; {len(dateien)} Katalogdateien; {len(vokabular)} Vokabularthemen")
    fehler = 0
    for name, liste in befunde.items():
        if liste:
            fehler += len(liste)
            print(f"Prüfung {name}: {len(liste)} Abweichungen")
            for b in liste:
                print(f"  - {b}")
        else:
            print(f"Prüfung {name}: bestanden")
    print("Alle Prüfungen bestanden." if not fehler else f"{fehler} Abweichungen, nichts geändert.")
    return 0 if not fehler else 1


if __name__ == "__main__":
    sys.exit(main())
