# -*- coding: utf-8 -*-
"""
gym-vergleich.py v0.3 · 24.09.2026 · Vergleich GYM gegen OS/EBR/FOR, Profil msa

Auftrag Gymnasialhefte (23.09.2026), Schritt 7: Nach Abschluss der GYM-
Erfassung (2014-2025, msa-katalog-gym.csv) vergleicht dieses Skript die
Typenverwendung des neuen papier-Werts GYM mit der der bisherigen Papiere
OS/EBR/FOR/MUSTER-EBR/MUSTER-FOR (msa-katalog-basis.csv und
msa-katalog-kontext.csv). Die Typenliste (msa-typen.csv) ist beiden Gruppen
gemeinsam (msa.md § 4); dieses Skript zeigt, wie stark sie sich tatsächlich
überschneidet.

Änderungen gegenüber 0.2 (Auftrag Nacht, Teil 1 Schritt 4, 24.09.2026):
Option --gruppen vergleicht statt GYM gegen OS/EBR/FOR zwei Papiergruppen
innerhalb von msa-katalog-basis.csv/msa-katalog-kontext.csv: Gruppe A =
papier EBR, Gruppe B = papier FOR und OS (Zweck: seit Heft 2026 EBR erfasst
ist, zeigt der Vergleich, ob EBR im Themenkatalog eine eigene Marke
braucht). Schreibt dann msa/ebr-vergleich.md nach demselben Muster wie
msa/gym-vergleich.md (Zählregel, Aufbau und Ausgabefunktionen unverändert,
nur Herkunft und Beschriftung der beiden Gruppen sind austauschbar).

Änderungen gegenüber 0.1 (Auftrag Abgleichlauf GYM, 24.09.2026, Schritt 6):
Ein Typ zählt für eine Gruppe (GYM bzw. OS/EBR/FOR) jetzt, wenn er dort als
Haupttyp (Feld typ) ODER als Nebentyp (Pipe-getrenntes Feld typ_neben)
steht; die Ausgabe nennt beides getrennt (Haupt; Haupt+Neben). „nur GYM"
heißt jetzt: in OS/EBR/FOR weder Haupt- noch Nebentyp.

Liest msa/msa-katalog-basis.csv, msa/msa-katalog-kontext.csv,
msa/msa-katalog-gym.csv und msa/msa-typen.csv, ändert keine der vier.

Ohne Option (Standard, GYM gegen OS/EBR/FOR): Für jeden Typ, der als typ
oder als Glied von typ_neben in einem der drei Kataloge vorkommt, wird
geprüft, ob er in mindestens einer GYM-Zeile bzw. mindestens einer
OS/EBR/FOR-Zeile steht – getrennt für „nur als Haupttyp" und „als Haupt-
oder Nebentyp". Daraus ergeben sich je Ebene drei Gruppen:

  nur GYM        – nur in msa-katalog-gym.csv.
  nur OS/EBR/FOR – nur in msa-katalog-basis.csv/msa-katalog-kontext.csv.
  beide          – in GYM und in mindestens einem der beiden anderen.

Ebenso für thema (aus msa-typen.csv, über den Haupttyp der Zeile; bei
Typen ohne Typenlisteneintrag "ohne Thema"): nur GYM, nur OS/EBR/FOR,
beide.

Mit --gruppen: dieselbe Zählregel, aber Gruppe A = Zeilen mit papier EBR,
Gruppe B = Zeilen mit papier FOR oder OS (beide aus msa-katalog-basis.csv
und msa-katalog-kontext.csv; MUSTER-EBR/MUSTER-FOR und GYM bleiben
außen vor).

Schreibt msa/gym-vergleich.md (Standard) oder msa/ebr-vergleich.md
(--gruppen): Kopf (Stand, Gesamtzahlen als die drei Zahlen je Ebene, für
Typen zweimal – Haupt und Haupt+Neben), dann je Ebene die Listen. Zwei
Läufe hintereinander erzeugen dieselbe Datei bis auf die Stand-Zeile.

Aufruf aus der Repo-Wurzel (braucht nur die Standardbibliothek):
  python werkzeuge/gym-vergleich.py
  python werkzeuge/gym-vergleich.py --gruppen
"""
import csv
import datetime
import io
import os
import subprocess
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/
VERSION = "gym-vergleich.py v0.3"
MSA = "msa"
KATALOGE_OS = ["msa-katalog-basis.csv", "msa-katalog-kontext.csv"]
KATALOG_GYM = "msa-katalog-gym.csv"
TYPENLISTE = "msa-typen.csv"
AUSGABE_MD = "gym-vergleich.md"  # in msa/
AUSGABE_MD_GRUPPEN = "ebr-vergleich.md"  # in msa/, nur mit --gruppen


def lies_csv(pfad):
    with io.open(pfad, encoding="utf-8-sig", newline="") as fh:  # -sig: eine BOM stört die Kopfzeile nicht
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


def haupt_und_neben(zeilen):
    """(Menge der Haupttypen, Menge der Haupt- oder Nebentypen) einer Liste von Katalogzeilen."""
    haupt = {z["typ"] for z in zeilen if z["typ"]}
    neben = set()
    for z in zeilen:
        for g in z["typ_neben"].split("|"):
            g = g.strip()
            if g:
                neben.add(g)
    return haupt, haupt | neben


def gruppiere(werte_gym, werte_os):
    nur_gym = sorted(werte_gym - werte_os)
    nur_os = sorted(werte_os - werte_gym)
    beide = sorted(werte_gym & werte_os)
    return nur_gym, nur_os, beide


def liste_md(titel, werte):
    out = [f"**{titel}** ({len(werte)}):", ""]
    if werte:
        out += [f"- {w}" for w in werte]
    else:
        out.append("- keine")
    out.append("")
    return out


def vergleich(kat_a, kat_b, typen, titel_zeile, beschreibung, label_a, label_b, ausgabe_datei):
    thema_je_typ = {z["typ"]: (z["thema"] or "ohne Thema") for z in typen}

    haupt_a, hn_a = haupt_und_neben(kat_a)
    haupt_b, hn_b = haupt_und_neben(kat_b)
    nur_a_h, nur_b_h, beide_h = gruppiere(haupt_a, haupt_b)
    nur_a_hn, nur_b_hn, beide_hn = gruppiere(hn_a, hn_b)

    themen_a = {thema_je_typ.get(z["typ"], "ohne Thema") for z in kat_a if z["typ"]}
    themen_b = {thema_je_typ.get(z["typ"], "ohne Thema") for z in kat_b if z["typ"]}
    nur_a_thema, nur_b_thema, beide_thema = gruppiere(themen_a, themen_b)

    stand = f"{datetime.date.today().isoformat()}, HEAD {head_kurz()}"
    out = []
    w = out.append
    w(titel_zeile)
    w(f"Stand {stand}.")
    w("")
    w(beschreibung)
    w("")
    w(f"Typen (Haupt): {len(nur_a_h)} nur {label_a}, {len(nur_b_h)} nur {label_b}, {len(beide_h)} in "
      "beiden.")
    w(f"Typen (Haupt+Neben): {len(nur_a_hn)} nur {label_a}, {len(nur_b_hn)} nur {label_b}, "
      f"{len(beide_hn)} in beiden.")
    w(f"Themen: {len(nur_a_thema)} nur {label_a}, {len(nur_b_thema)} nur {label_b}, {len(beide_thema)} "
      "in beiden.")
    w("")
    w(f"Erzeugt von `werkzeuge/{VERSION.split()[0]}` ({VERSION.split()[1]}) aus den msa-Katalogen und "
      "msa-typen.csv; abgeleitet, nie von Hand ändern.")
    w("")
    w("## Typen (Haupt)")
    w("")
    out += liste_md(f"nur {label_a}", nur_a_h)
    out += liste_md(f"nur {label_b}", nur_b_h)
    out += liste_md("in beiden", beide_h)
    w("## Typen (Haupt+Neben)")
    w("")
    out += liste_md(f"nur {label_a}", nur_a_hn)
    out += liste_md(f"nur {label_b}", nur_b_hn)
    out += liste_md("in beiden", beide_hn)
    w("## Themen")
    w("")
    out += liste_md(f"nur {label_a}", nur_a_thema)
    out += liste_md(f"nur {label_b}", nur_b_thema)
    out += liste_md("in beiden", beide_thema)

    with io.open(ausgabe_datei, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out) + "\n")

    return (len(nur_a_h), len(nur_b_h), len(beide_h), len(nur_a_hn), len(nur_b_hn), len(beide_hn),
            len(nur_a_thema), len(nur_b_thema), len(beide_thema), len(out))


def main():
    msa_pfad = os.path.join(HIER, MSA)
    gruppen = "--gruppen" in sys.argv[1:]
    kat_os_alle = []
    for datei in KATALOGE_OS:
        kat_os_alle += lies_csv(os.path.join(msa_pfad, datei))
    typen = lies_csv(os.path.join(msa_pfad, TYPENLISTE))

    if gruppen:
        kat_a = [z for z in kat_os_alle if z["papier"] == "EBR"]
        kat_b = [z for z in kat_os_alle if z["papier"] in ("FOR", "OS")]
        werte = vergleich(
            kat_a, kat_b, typen,
            "# Vergleich EBR gegen FOR/OS – Profil msa",
            "Vergleicht die Verwendung von Typ und Thema zwischen Gruppe A (Zeilen mit papier EBR) und "
            "Gruppe B (Zeilen mit papier FOR oder OS), beide aus msa-katalog-basis.csv und "
            "msa-katalog-kontext.csv (MUSTER-EBR/MUSTER-FOR und GYM bleiben außen vor). Die Typenliste "
            "msa-typen.csv ist beiden Gruppen gemeinsam (msa.md § 4). Bei Typen wird zwischen „Haupt“ "
            "(Feld typ) und „Haupt+Neben“ (Feld typ oder ein Glied des Pipe-getrennten Feldes typ_neben) "
            "unterschieden; „nur A“ heißt bei Haupt+Neben: in Gruppe B weder Haupt- noch Nebentyp. "
            "Themen werden nur über den Haupttyp der Zeile gezählt.",
            "A (EBR)", "B (FOR/OS)", os.path.join(msa_pfad, AUSGABE_MD_GRUPPEN))
        ausgabe = AUSGABE_MD_GRUPPEN
        bez_a, bez_b = "EBR", "FOR-OS"
    else:
        kat_gym = lies_csv(os.path.join(msa_pfad, KATALOG_GYM))
        werte = vergleich(
            kat_gym, kat_os_alle, typen,
            "# Vergleich GYM gegen OS/EBR/FOR – Profil msa",
            "Vergleicht die Verwendung von Typ und Thema zwischen dem Papier GYM (msa-katalog-gym.csv) "
            "und den Papieren OS/EBR/FOR/MUSTER-EBR/MUSTER-FOR (msa-katalog-basis.csv, "
            "msa-katalog-kontext.csv). Die Typenliste msa-typen.csv ist beiden Gruppen gemeinsam "
            "(msa.md § 4). Bei Typen wird zwischen „Haupt“ (Feld typ) und „Haupt+Neben“ (Feld typ oder "
            "ein Glied des Pipe-getrennten Feldes typ_neben) unterschieden; „nur GYM“ heißt bei "
            "Haupt+Neben: in OS/EBR/FOR weder Haupt- noch Nebentyp. Themen werden nur über den Haupttyp "
            "der Zeile gezählt.",
            "GYM", "OS/EBR/FOR", os.path.join(msa_pfad, AUSGABE_MD))
        ausgabe = AUSGABE_MD
        bez_a, bez_b = "GYM", "OS-FOR"

    (nur_a_h, nur_b_h, beide_h, nur_a_hn, nur_b_hn, beide_hn,
     nur_a_thema, nur_b_thema, beide_thema, n_zeilen) = werte
    print(f"{VERSION}: Haupt {nur_a_h} nur {bez_a} / {nur_b_h} nur {bez_b} / {beide_h} beide; "
          f"Haupt+Neben {nur_a_hn} nur {bez_a} / {nur_b_hn} nur {bez_b} / {beide_hn} beide (Typen); "
          f"{nur_a_thema} nur {bez_a} / {nur_b_thema} nur {bez_b} / {beide_thema} beide (Themen). "
          f"msa/{ausgabe} geschrieben ({n_zeilen} Zeilen).")


if __name__ == "__main__":
    sys.exit(main())
