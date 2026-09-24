# -*- coding: utf-8 -*-
"""
typen-abgleich.py v0.1 · 24.09.2026 · Abgleichlauf nach Kern § 9, Profil msa

Auftrag Abgleichlauf GYM (24.09.2026): Nach der GYM-Erfassung (archiv/
auftrag-gym-erfassung.md) ergab die Gegenlese des Lehrers nach Kern § 6
(„Kontext, Zahlen und Format ändern den Typ nicht; trenne, wenn der
Lösungsweg ein anderer ist"), dass ein Teil der neuen GYM-Typen Dubletten
oder Aufgabenbeschreibungen statt Fertigkeiten sind. Dieses Skript setzt
eine entschiedene Abgleichliste (alt;neu;thema_neu;art) um: Es benennt
Typen um oder zieht sie zu einem vorhandenen Typ zusammen, in der
Typenliste und in allen Katalogen eines Profils zugleich. Fakten (gegeben,
ergebnis, Punkte, ...) bleiben unverändert – nur die Etiketten typ,
typ_neben, thema und leitidee ändern sich.

Ablauf je Zeile der Abgleichliste, in Dateireihenfolge:
  a) In allen Katalogen des Profils: alt in typ und in jedem Glied von
     typ_neben (Pipe-getrennt) durch neu ersetzen; ist neu bereits ein
     anderes Glied derselben typ_neben-Liste, die Doppelung entfernen.
  b) Jede Katalogzeile, deren Feld typ durch (a) auf neu geändert wurde,
     bekommt thema und leitidee des Typs neu aus der (zu diesem Zeitpunkt
     schon aktualisierten) Typenliste, falls ihr eigenes thema davon
     abweicht (Kern § 6, Zeilenthema = Typthema; nur für Zeilen, deren typ
     dieser Lauf geändert hat – die profileigene Regel „Thema der
     Aufgabenstellung" (msa.md § 6) gilt für alle anderen Zeilen
     unverändert weiter).
  c) Typenliste: art „umbenennen" benennt die Zeile mit typ = alt auf
     typ = neu um (und setzt thema = thema_neu, falls angegeben); art
     „zusammenziehen" löscht die Zeile mit typ = alt (neu muss zu diesem
     Zeitpunkt in der Typenliste stehen – von Anfang an oder weil eine
     frühere Zeile derselben Liste es dorthin umbenannt hat); beispiel_id
     von neu bleibt unverändert.

Das Skript ist idempotent: ein zweiter Lauf über dieselbe (bereits
angewendete) Liste ändert keine Datei mehr, weil kein alt mehr vorkommt.
Vor dem Schreiben prüft es, dass jedes alt zu Beginn in der Typenliste
steht und dass jedes neu am Ende genau einmal in der Typenliste steht;
bei einem Fehler wird nichts geschrieben.

Zusatzoptionen (je eigener Lauf, unabhängig von der Abgleichliste):
  --thema ALT NEU        benennt ein Thema in msa-typen.csv, allen
                          Katalogen des Profils und in themen.csv (Zeile
                          profil=msa, thema=ALT; die zeilen/typen-Spalten
                          dort werden aus den Katalogen neu gezählt) um.
  --status-neu-gueltig    setzt in msa-typen.csv den Status jeder Zeile
                          mit status „neu" auf „gültig".
Beide Optionen schreiben nur die genannten Dateien, keine Abgleichliste
nötig; --thema und --status-neu-gueltig können mit der Abgleichliste in
einem Lauf kombiniert werden (erst die Liste, dann --thema, dann
--status-neu-gueltig) oder einzeln aufgerufen werden.

Aufruf aus der Repo-Wurzel:
  python werkzeuge/typen-abgleich.py msa/gym-abgleich.csv msa
  python werkzeuge/typen-abgleich.py --thema Sinussatz "Sinus- und Kosinussatz" msa
  python werkzeuge/typen-abgleich.py --status-neu-gueltig msa
Braucht nur die Standardbibliothek.
"""
import argparse
import csv
import io
import os
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/

KATALOGE = {
    "msa": ["msa-katalog-basis.csv", "msa-katalog-kontext.csv", "msa-katalog-gym.csv"],
}
TYPENLISTE = {"msa": "msa-typen.csv"}
THEMEN_CSV = "themen.csv"


def lies_csv(pfad):
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    if not rows:
        sys.exit(f"{pfad}: leer")
    return rows[0], rows[1:]


def schreibe_csv(pfad, kopf, zeilen):
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(kopf)
        for z in zeilen:
            w.writerow(z)


def lade_typenliste(pfad):
    kopf, zeilen = lies_csv(pfad)
    idx = {name: i for i, name in enumerate(kopf)}
    return kopf, zeilen, idx


def lade_abgleichliste(pfad):
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter=";"))
    return rows


def hauptlauf(profil, abgleich_pfad):
    msa_pfad = os.path.join(HIER, profil)
    typenliste_pfad = os.path.join(msa_pfad, TYPENLISTE[profil])
    typ_kopf, typ_zeilen, typ_idx = lade_typenliste(typenliste_pfad)
    typ_i, thema_i, leitidee_i = typ_idx["typ"], typ_idx["thema"], typ_idx["leitidee"]

    abgleich = lade_abgleichliste(abgleich_pfad)

    # Typenliste Zeile für Zeile umsetzen. Idempotenz: fehlt alt bereits (voriger Lauf hat es
    # umbenannt oder gelöscht) und steht neu schon in der Typenliste, ist die Zeile bereits
    # angewendet – übersprungen, kein Fehler. Fehlen beide, ist die Liste oder der Bestand kaputt.
    typ_by_name = {z[typ_i]: z for z in typ_zeilen}
    uebersprungen = []
    for a in abgleich:
        alt, neu, thema_neu, art = a["alt"], a["neu"], a["thema_neu"].strip(), a["art"].strip()
        if alt not in typ_by_name:
            if neu in typ_by_name:
                uebersprungen.append(alt)
                continue
            sys.exit(f"ABBRUCH – weder „{alt}“ noch „{neu}“ stehen in der Typenliste")
        if art == "umbenennen":
            z = typ_by_name.pop(alt)
            z[typ_i] = neu
            if thema_neu:
                z[thema_i] = thema_neu
            typ_by_name[neu] = z
        elif art == "zusammenziehen":
            if neu not in typ_by_name:
                sys.exit(f"ABBRUCH – zusammenziehen: „{neu}“ (Ziel von „{alt}“) steht nicht in der "
                         "Typenliste (weder von Anfang an noch durch eine frühere Zeile der Liste)")
            del typ_by_name[alt]
        else:
            sys.exit(f"ABBRUCH – unbekannte art „{art}“ bei alt={alt}")

    neue_typ_zeilen = list(typ_by_name.values())
    thema_von_typ = {z[typ_i]: z[thema_i] for z in neue_typ_zeilen}
    leitidee_von_typ = {z[typ_i]: z[leitidee_i] for z in neue_typ_zeilen}

    # Endzustand prüfen: jedes neu genau einmal in der Typenliste.
    namen_nachher = [z[typ_i] for z in neue_typ_zeilen]
    for a in abgleich:
        vork = namen_nachher.count(a["neu"])
        if vork != 1:
            sys.exit(f"ABBRUCH – „{a['neu']}“ kommt {vork}-mal in der Typenliste vor (soll genau 1)")

    ersetzung = {a["alt"]: a["neu"] for a in abgleich}

    # Kataloge umsetzen.
    berichte = []
    katalog_ergebnisse = []
    for name in KATALOGE[profil]:
        pfad = os.path.join(msa_pfad, name)
        kopf, zeilen = lies_csv(pfad)
        idx = {f: i for i, f in enumerate(kopf)}
        typ_col, neben_col = idx["typ"], idx["typ_neben"]
        thema_col, leitidee_col = idx["thema"], idx["leitidee"]
        id_col = idx["id"]
        geaendert = 0
        for z in zeilen:
            typ_geaendert = False
            if z[typ_col] in ersetzung:
                neu = ersetzung[z[typ_col]]
                berichte.append(f"{z[id_col]}: {z[typ_col]} → {neu}")
                z[typ_col] = neu
                typ_geaendert = True
                geaendert += 1
            if z[neben_col]:
                glieder = z[neben_col].split("|")
                neue_glieder = []
                for g in glieder:
                    g2 = ersetzung.get(g, g)
                    if g2 not in neue_glieder:
                        neue_glieder.append(g2)
                if neue_glieder != glieder:
                    z[neben_col] = "|".join(neue_glieder)
                    geaendert += 1
            if typ_geaendert:
                typ_thema = thema_von_typ.get(z[typ_col])
                typ_leitidee = leitidee_von_typ.get(z[typ_col])
                if typ_thema is not None and z[thema_col] != typ_thema:
                    z[thema_col] = typ_thema
                    z[leitidee_col] = typ_leitidee
        schreibe_csv(pfad, kopf, zeilen)
        katalog_ergebnisse.append((name, geaendert))

    schreibe_csv(typenliste_pfad, typ_kopf, neue_typ_zeilen)

    print(f"typen-abgleich.py: {len(abgleich)} Zeilen der Abgleichliste verarbeitet, "
          f"{sum(1 for a in abgleich if a['art'].strip() == 'umbenennen')} umbenannt, "
          f"{sum(1 for a in abgleich if a['art'].strip() == 'zusammenziehen')} zusammengezogen, "
          f"{len(uebersprungen)} bereits angewendet (übersprungen).")
    print(f"Typenliste: {len(typ_zeilen)} -> {len(neue_typ_zeilen)} Typen.")
    for name, n in katalog_ergebnisse:
        print(f"{name}: {n} geänderte Zeilen")
    print("Geänderte Katalogzeilen:")
    for b in berichte:
        print(" ", b)
    return berichte, katalog_ergebnisse


def option_thema(profil, alt, neu):
    msa_pfad = os.path.join(HIER, profil)
    typenliste_pfad = os.path.join(msa_pfad, TYPENLISTE[profil])
    typ_kopf, typ_zeilen, typ_idx = lade_typenliste(typenliste_pfad)
    thema_i = typ_idx["thema"]
    n_typ = 0
    for z in typ_zeilen:
        if z[thema_i] == alt:
            z[thema_i] = neu
            n_typ += 1
    schreibe_csv(typenliste_pfad, typ_kopf, typ_zeilen)

    n_katalog = 0
    for name in KATALOGE[profil]:
        pfad = os.path.join(msa_pfad, name)
        kopf, zeilen = lies_csv(pfad)
        idx = {f: i for i, f in enumerate(kopf)}
        thema_col = idx["thema"]
        for z in zeilen:
            if z[thema_col] == alt:
                z[thema_col] = neu
                n_katalog += 1
        schreibe_csv(pfad, kopf, zeilen)

    # themen.csv: Zeile profil=msa, thema=alt umbenennen und zeilen/typen neu zaehlen
    # (nur Basis+Kontext, wie werkzeuge/themen-pruef.py und werkzeuge/ertrag.py fuer msa).
    themen_pfad = os.path.join(HIER, THEMEN_CSV)
    tkopf, tzeilen = lies_csv(themen_pfad)
    tidx = {f: i for i, f in enumerate(tkopf)}
    n_themen = 0
    for z in tzeilen:
        if z[tidx["profil"]] == profil and z[tidx["thema"]] == alt:
            z[tidx["thema"]] = neu
            zeilen_zahl, typen_menge = zaehle_thema(profil, msa_pfad, neu)
            z[tidx["zeilen"]] = str(zeilen_zahl)
            z[tidx["typen"]] = str(len(typen_menge))
            n_themen += 1
    schreibe_csv(themen_pfad, tkopf, tzeilen)

    print(f"typen-abgleich.py --thema: {n_typ} Typenlisten-Zeilen, {n_katalog} Katalogzeilen "
          f"(Basis+Kontext+GYM), {n_themen} themen.csv-Zeile(n) von „{alt}“ auf „{neu}“ umbenannt.")


def zaehle_thema(profil, msa_pfad, thema):
    """zeilen, {typen} fuer Basis+Kontext (wie themen-pruef.py/ertrag.py: msa = Basis+Kontext, ohne GYM)."""
    zeilen_zahl = 0
    typen = set()
    for name in ("msa-katalog-basis.csv", "msa-katalog-kontext.csv"):
        pfad = os.path.join(msa_pfad, name)
        kopf, zeilen = lies_csv(pfad)
        idx = {f: i for i, f in enumerate(kopf)}
        for z in zeilen:
            if z[idx["thema"]] == thema:
                zeilen_zahl += 1
                typen.add(z[idx["typ"]])
    return zeilen_zahl, typen


def option_status_neu_gueltig(profil):
    msa_pfad = os.path.join(HIER, profil)
    typenliste_pfad = os.path.join(msa_pfad, TYPENLISTE[profil])
    typ_kopf, typ_zeilen, typ_idx = lade_typenliste(typenliste_pfad)
    status_i = typ_idx["status"]
    n = 0
    for z in typ_zeilen:
        if z[status_i] == "neu":
            z[status_i] = "gültig"
            n += 1
    schreibe_csv(typenliste_pfad, typ_kopf, typ_zeilen)
    print(f"typen-abgleich.py --status-neu-gueltig: {n} Typen von „neu“ auf „gültig“ gesetzt.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("abgleichliste", nargs="?", help="Pfad zur Abgleichliste (alt;neu;thema_neu;art)")
    ap.add_argument("--profil", default="msa", help="Profil (Standard: msa)")
    ap.add_argument("--thema", nargs=2, metavar=("ALT", "NEU"))
    ap.add_argument("--status-neu-gueltig", action="store_true")
    args = ap.parse_args()

    if args.abgleichliste:
        hauptlauf(args.profil, os.path.join(HIER, args.abgleichliste)
                  if not os.path.isabs(args.abgleichliste) else args.abgleichliste)
    if args.thema:
        option_thema(args.profil, args.thema[0], args.thema[1])
    if args.status_neu_gueltig:
        option_status_neu_gueltig(args.profil)
    if not args.abgleichliste and not args.thema and not args.status_neu_gueltig:
        ap.print_help()


if __name__ == "__main__":
    main()
