# -*- coding: utf-8 -*-
"""
gym-vergleich.py v0.2 · 24.09.2026 · Vergleich GYM gegen OS/EBR/FOR, Profil msa

Auftrag Gymnasialhefte (23.09.2026), Schritt 7: Nach Abschluss der GYM-
Erfassung (2014-2025, msa-katalog-gym.csv) vergleicht dieses Skript die
Typenverwendung des neuen papier-Werts GYM mit der der bisherigen Papiere
OS/EBR/FOR/MUSTER-EBR/MUSTER-FOR (msa-katalog-basis.csv und
msa-katalog-kontext.csv). Die Typenliste (msa-typen.csv) ist beiden Gruppen
gemeinsam (msa.md § 4); dieses Skript zeigt, wie stark sie sich tatsächlich
überschneidet.

Änderungen gegenüber 0.1 (Auftrag Abgleichlauf GYM, 24.09.2026, Schritt 6):
Ein Typ zählt für eine Gruppe (GYM bzw. OS/EBR/FOR) jetzt, wenn er dort als
Haupttyp (Feld typ) ODER als Nebentyp (Pipe-getrenntes Feld typ_neben)
steht; die Ausgabe nennt beides getrennt (Haupt; Haupt+Neben). „nur GYM"
heißt jetzt: in OS/EBR/FOR weder Haupt- noch Nebentyp.

Liest msa/msa-katalog-basis.csv, msa/msa-katalog-kontext.csv,
msa/msa-katalog-gym.csv und msa/msa-typen.csv, ändert keine der vier.

Für jeden Typ, der als typ oder als Glied von typ_neben in einem der drei
Kataloge vorkommt, wird geprüft, ob er in mindestens einer GYM-Zeile bzw.
mindestens einer OS/EBR/FOR-Zeile steht – getrennt für „nur als Haupttyp"
und „als Haupt- oder Nebentyp". Daraus ergeben sich je Ebene drei Gruppen:

  nur GYM        – nur in msa-katalog-gym.csv.
  nur OS/EBR/FOR – nur in msa-katalog-basis.csv/msa-katalog-kontext.csv.
  beide          – in GYM und in mindestens einem der beiden anderen.

Ebenso für thema (aus msa-typen.csv, über den Haupttyp der Zeile; bei
Typen ohne Typenlisteneintrag "ohne Thema"): nur GYM, nur OS/EBR/FOR,
beide.

Schreibt msa/gym-vergleich.md: Kopf (Stand, Gesamtzahlen als die drei
Zahlen je Ebene, für Typen zweimal – Haupt und Haupt+Neben), dann je Ebene
die Listen. Zwei Läufe hintereinander erzeugen dieselbe Datei bis auf die
Stand-Zeile.

Aufruf aus der Repo-Wurzel (braucht nur die Standardbibliothek):
  python werkzeuge/gym-vergleich.py
"""
import csv
import datetime
import io
import os
import subprocess
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/
VERSION = "gym-vergleich.py v0.2"
MSA = "msa"
KATALOGE_OS = ["msa-katalog-basis.csv", "msa-katalog-kontext.csv"]
KATALOG_GYM = "msa-katalog-gym.csv"
TYPENLISTE = "msa-typen.csv"
AUSGABE_MD = "gym-vergleich.md"  # in msa/


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


def main():
    msa_pfad = os.path.join(HIER, MSA)
    kat_os = []
    for datei in KATALOGE_OS:
        kat_os += lies_csv(os.path.join(msa_pfad, datei))
    kat_gym = lies_csv(os.path.join(msa_pfad, KATALOG_GYM))
    typen = lies_csv(os.path.join(msa_pfad, TYPENLISTE))
    thema_je_typ = {z["typ"]: (z["thema"] or "ohne Thema") for z in typen}

    haupt_gym, hn_gym = haupt_und_neben(kat_gym)
    haupt_os, hn_os = haupt_und_neben(kat_os)
    nur_gym_h, nur_os_h, beide_h = gruppiere(haupt_gym, haupt_os)
    nur_gym_hn, nur_os_hn, beide_hn = gruppiere(hn_gym, hn_os)

    themen_gym = {thema_je_typ.get(z["typ"], "ohne Thema") for z in kat_gym if z["typ"]}
    themen_os = {thema_je_typ.get(z["typ"], "ohne Thema") for z in kat_os if z["typ"]}
    nur_gym_thema, nur_os_thema, beide_thema = gruppiere(themen_gym, themen_os)

    stand = f"{datetime.date.today().isoformat()}, HEAD {head_kurz()}"
    out = []
    w = out.append
    w("# Vergleich GYM gegen OS/EBR/FOR – Profil msa")
    w(f"Stand {stand}.")
    w("")
    w("Vergleicht die Verwendung von Typ und Thema zwischen dem Papier GYM (msa-katalog-gym.csv) und "
      "den Papieren OS/EBR/FOR/MUSTER-EBR/MUSTER-FOR (msa-katalog-basis.csv, msa-katalog-kontext.csv). "
      "Die Typenliste msa-typen.csv ist beiden Gruppen gemeinsam (msa.md § 4). Bei Typen wird zwischen "
      "„Haupt“ (Feld typ) und „Haupt+Neben“ (Feld typ oder ein Glied des Pipe-getrennten Feldes "
      "typ_neben) unterschieden; „nur GYM“ heißt bei Haupt+Neben: in OS/EBR/FOR weder Haupt- noch "
      "Nebentyp. Themen werden nur über den Haupttyp der Zeile gezählt.")
    w("")
    w(f"Typen (Haupt): {len(nur_gym_h)} nur GYM, {len(nur_os_h)} nur OS/EBR/FOR, {len(beide_h)} in "
      "beiden.")
    w(f"Typen (Haupt+Neben): {len(nur_gym_hn)} nur GYM, {len(nur_os_hn)} nur OS/EBR/FOR, {len(beide_hn)} "
      "in beiden.")
    w(f"Themen: {len(nur_gym_thema)} nur GYM, {len(nur_os_thema)} nur OS/EBR/FOR, {len(beide_thema)} in "
      "beiden.")
    w("")
    w(f"Erzeugt von `werkzeuge/{VERSION.split()[0]}` ({VERSION.split()[1]}) aus den msa-Katalogen und "
      "msa-typen.csv; abgeleitet, nie von Hand ändern.")
    w("")
    w("## Typen (Haupt)")
    w("")
    out += liste_md("nur GYM", nur_gym_h)
    out += liste_md("nur OS/EBR/FOR", nur_os_h)
    out += liste_md("in beiden", beide_h)
    w("## Typen (Haupt+Neben)")
    w("")
    out += liste_md("nur GYM", nur_gym_hn)
    out += liste_md("nur OS/EBR/FOR", nur_os_hn)
    out += liste_md("in beiden", beide_hn)
    w("## Themen")
    w("")
    out += liste_md("nur GYM", nur_gym_thema)
    out += liste_md("nur OS/EBR/FOR", nur_os_thema)
    out += liste_md("in beiden", beide_thema)

    ziel = os.path.join(msa_pfad, AUSGABE_MD)
    with io.open(ziel, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out) + "\n")

    print(f"{VERSION}: Haupt {len(nur_gym_h)} nur GYM / {len(nur_os_h)} nur OS-FOR / {len(beide_h)} "
          f"beide; Haupt+Neben {len(nur_gym_hn)} nur GYM / {len(nur_os_hn)} nur OS-FOR / {len(beide_hn)} "
          f"beide (Typen); {len(nur_gym_thema)} nur GYM / {len(nur_os_thema)} nur OS-FOR / "
          f"{len(beide_thema)} beide (Themen). msa/{AUSGABE_MD} geschrieben ({len(out)} Zeilen).")


if __name__ == "__main__":
    sys.exit(main())
