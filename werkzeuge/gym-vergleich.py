# -*- coding: utf-8 -*-
"""
gym-vergleich.py v0.1 · 23.09.2026 · Vergleich GYM gegen OS/EBR/FOR, Profil msa

Auftrag Gymnasialhefte (23.09.2026), Schritt 7: Nach Abschluss der GYM-
Erfassung (2014-2025, msa-katalog-gym.csv) vergleicht dieses Skript die
Typenverwendung des neuen papier-Werts GYM mit der der bisherigen Papiere
OS/EBR/FOR/MUSTER-EBR/MUSTER-FOR (msa-katalog-basis.csv und
msa-katalog-kontext.csv). Die Typenliste (msa-typen.csv) ist beiden Gruppen
gemeinsam (msa.md § 4); dieses Skript zeigt, wie stark sie sich tatsächlich
überschneidet.

Liest msa/msa-katalog-basis.csv, msa/msa-katalog-kontext.csv,
msa/msa-katalog-gym.csv und msa/msa-typen.csv, ändert keine der vier.

Für jeden Typ aus msa-typen.csv sowie jeden typ- oder typ_neben-Wert der
drei Kataloge, der dort fehlt, wird geprüft, ob er als Haupttyp (Feld typ)
in mindestens einer GYM-Zeile bzw. mindestens einer OS/EBR/FOR-Zeile
vorkommt (Nebentypen zählen hier nicht mit, anders als in ertrag.py, weil
die Fragestellung "in welchem Papier wird dieser Typ geprüft" den
Haupttyp meint). Daraus ergeben sich drei Gruppen:

  nur GYM        – Haupttyp nur in msa-katalog-gym.csv.
  nur OS/EBR/FOR – Haupttyp nur in msa-katalog-basis.csv/msa-katalog-kontext.csv.
  beide          – Haupttyp in GYM und in mindestens einem der beiden anderen.

Ebenso für thema (aus msa-typen.csv; bei Typen ohne Typenlisteneintrag
"ohne Thema"): nur GYM, nur OS/EBR/FOR, beide.

Schreibt msa/gym-vergleich.md: Kopf (Stand, Gesamtzahlen als die drei
Zahlen je Ebene), dann je Ebene (Typ, Thema) drei Listen. Zwei Läufe
hintereinander erzeugen dieselbe Datei bis auf die Stand-Zeile.

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
VERSION = "gym-vergleich.py v0.1"
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

    typen_gym = {z["typ"] for z in kat_gym}
    typen_os = {z["typ"] for z in kat_os}
    nur_gym_typ, nur_os_typ, beide_typ = gruppiere(typen_gym, typen_os)

    themen_gym = {thema_je_typ.get(z["typ"], "ohne Thema") for z in kat_gym}
    themen_os = {thema_je_typ.get(z["typ"], "ohne Thema") for z in kat_os}
    nur_gym_thema, nur_os_thema, beide_thema = gruppiere(themen_gym, themen_os)

    stand = f"{datetime.date.today().isoformat()}, HEAD {head_kurz()}"
    out = []
    w = out.append
    w("# Vergleich GYM gegen OS/EBR/FOR – Profil msa")
    w(f"Stand {stand}.")
    w("")
    w("Vergleicht die Verwendung von Typ und Thema (jeweils als Haupttyp, Feld typ) zwischen dem Papier "
      "GYM (msa-katalog-gym.csv) und den Papieren OS/EBR/FOR/MUSTER-EBR/MUSTER-FOR "
      "(msa-katalog-basis.csv, msa-katalog-kontext.csv). Die Typenliste msa-typen.csv ist beiden Gruppen "
      "gemeinsam (msa.md § 4); Nebentypen (typ_neben) zählen hier nicht mit.")
    w("")
    w(f"Typen: {len(nur_gym_typ)} nur GYM, {len(nur_os_typ)} nur OS/EBR/FOR, {len(beide_typ)} in beiden.")
    w(f"Themen: {len(nur_gym_thema)} nur GYM, {len(nur_os_thema)} nur OS/EBR/FOR, {len(beide_thema)} in "
      "beiden.")
    w("")
    w(f"Erzeugt von `werkzeuge/{VERSION.split()[0]}` ({VERSION.split()[1]}) aus den msa-Katalogen und "
      "msa-typen.csv; abgeleitet, nie von Hand ändern.")
    w("")
    w("## Typen")
    w("")
    out += liste_md("nur GYM", nur_gym_typ)
    out += liste_md("nur OS/EBR/FOR", nur_os_typ)
    out += liste_md("in beiden", beide_typ)
    w("## Themen")
    w("")
    out += liste_md("nur GYM", nur_gym_thema)
    out += liste_md("nur OS/EBR/FOR", nur_os_thema)
    out += liste_md("in beiden", beide_thema)

    ziel = os.path.join(msa_pfad, AUSGABE_MD)
    with io.open(ziel, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out) + "\n")

    print(f"{VERSION}: {len(nur_gym_typ)} nur GYM / {len(nur_os_typ)} nur OS-FOR / {len(beide_typ)} beide "
          f"(Typen); {len(nur_gym_thema)} nur GYM / {len(nur_os_thema)} nur OS-FOR / {len(beide_thema)} "
          f"beide (Themen). msa/{AUSGABE_MD} geschrieben ({len(out)} Zeilen).")


if __name__ == "__main__":
    sys.exit(main())
