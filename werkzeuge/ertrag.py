# -*- coding: utf-8 -*-
"""
ertrag.py v0.1 · 22.09.2026 · Ertrag je Typ, Profil msa

Auftrag Ertrag je Typ (msa, 22.09.2026): ziel.md § 5 führt als offenen Posten
„Ertrag je Typ“ – ein Skript aus msa-typen.csv (Jahrgänge, BE, block, schritte).
Der Ertrag ordnet im Blattbau die Typen (ziel.md § 2: „die Typen stehen nach
Ertrag“) und bestimmt, welche Sprossen die Option „schwach“ weglässt. Dieses
Skript liefert die Zahlen; die Schwelle für „selten“ setzt der Lehrer an
Tabelle C.

Liest msa/msa-katalog-basis.csv, msa/msa-katalog-kontext.csv und
msa/msa-typen.csv, ändert keine der drei. Je Typ aus msa-typen.csv (Spalte
typ) sowie je typ- oder typ_neben-Wert der Kataloge, der dort fehlt (Status
„nicht in typen.csv“), zählt das Skript:

  Hauptzeilen      – Katalogzeilen mit typ = Typ.
  Nebenzeilen      – Katalogzeilen, in deren Pipe-Feld typ_neben der Typ steht
                      (unabhängig vom Haupttyp der Zeile).
  jahre_haupt      – verschiedene jahr-Werte der Hauptzeilen.
  jahre_gesamt     – dasselbe über Haupt- und Nebenzeilen.
  erster, letzter  – kleinstes und größtes jahr (Haupt- und Nebenzeilen).
  punkte_haupt     – Summe punkte der Hauptzeilen.
  punkte_anteil    – punkte_haupt an der Punktsumme beider Kataloge, in
                      Prozent, auf 0,1 gerundet.
  basis, kontext   – Hauptzeilen je block.
  niveau_I/II/III  – Hauptzeilen je niveau_geschaetzt.
  schritte_mittel  – Mittel der Hauptzeilen-Werte schritte, auf eine
                      Dezimalstelle; nicht numerische oder leere Werte zählen
                      nicht mit, sondern in schritte_fehlt.
  thema, leitidee, status – aus msa-typen.csv (leer bei „nicht in typen.csv“).
  ertrag           – die Sortiergröße: (punkte_haupt, jahre_gesamt,
                      zeilen_haupt), bei Gleichstand zusätzlich der Typname
                      (für ein deterministisches Ergebnis bei wiederholten
                      Läufen).

Schreibt msa/msa-ertrag.csv (eine Zeile je Typ, Spalten wie oben, Reihenfolge
wie Tabelle A) und msa/msa-ertrag.md:
  Kopf      – Stand-Zeile (Datum, kurzer Hash des HEAD-Commits), Zählregel,
              Gesamtzahlen (Zeilen, Punkte, Typen mit Hauptzeile, Typen nur
              als Nebentyp, Typen ohne Vorkommen).
  Tabelle A – alle Typen nach ertrag absteigend, mit Rang und allen Spalten.
  Tabelle B – je thema (Themen nach Punktsumme absteigend) die Typen des
              Themas in Ertragsfolge.
  Tabelle C – Verteilung als Hilfe für die Schwelle „selten“: für
              punkte_haupt, jahre_gesamt und zeilen_haupt je der Wert, unter
              dem 10 %, 25 %, 50 % der Typen mit Hauptzeile liegen (Rang-
              Perzentil: sortierte Werte aufsteigend, Index floor(p/100 · n),
              n = Zahl der Typen mit Hauptzeile), dazu die Zahl der Typen mit
              Hauptzeile und jahre_gesamt ≤ 2.
  Liste D   – Typen ohne Hauptzeile: nur als Nebentyp vorkommend, und ganz
              ohne Vorkommen; je mit Thema.
Zwei Läufe hintereinander erzeugen dieselbe Datei bis auf die Stand-Zeile.

Gegenprobe am Ende des Laufs (Ausgabe auf stdout, kein Abbruch bei
Abweichung – die Abweichung ist dann der Befund, das Skript wird nicht an
die Zahl angepasst): Zeilen mit thema „Prozentrechnung“, deren Punktsumme,
Punktsumme beider Kataloge, Zahl verschiedener jahr-Werte im Thema
Prozentrechnung, Hauptzeilen „Prozentwert berechnen“ mit Thema
Prozentrechnung – Sollwerte aus katalog/prozentrechnung.md, Abschnitt
„Prüfungsform (P10)“.

Aufruf aus der Repo-Wurzel (braucht nur die Standardbibliothek):
  python werkzeuge/ertrag.py
"""
import collections
import csv
import datetime
import io
import os
import subprocess
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/
VERSION = "ertrag.py v0.1"
MSA = "msa"
KATALOGE = ["msa-katalog-basis.csv", "msa-katalog-kontext.csv"]
TYPENLISTE = "msa-typen.csv"
AUSGABE_CSV = "msa-ertrag.csv"  # in msa/
AUSGABE_MD = "msa-ertrag.md"  # in msa/
NICHT_IN_TYPEN = "nicht in typen.csv"

# Gegenprobe (Schritt 3 des Auftrags), Sollwerte aus katalog/prozentrechnung.md, „Prüfungsform (P10)“.
# Der letzte Sollwert ist 5, nicht 4: die Ausgangslage von archiv/auftrag-ertrag.md zählt nur
# 2014-OS-B1a, 2017-OS-B1b, 2021-OS-B1c, 2026-FOR-B1a auf und übersieht 2019-OS-K5a (Kontext-Katalog,
# ebenfalls typ „Prozentwert berechnen“, thema Prozentrechnung); vom Lehrer am 22.09.2026 bestätigt.
GEGENPROBE_THEMA = "Prozentrechnung"
GEGENPROBE_TYP = "Prozentwert berechnen"
GEGENPROBE_SOLL = {
    "Zeilen Thema Prozentrechnung": 22,
    "Punktsumme Thema Prozentrechnung": 38,
    "Punktsumme beider Kataloge": 780,
    "Jahre im Thema Prozentrechnung": 13,
    "Hauptzeilen „Prozentwert berechnen“ mit Thema Prozentrechnung": 5,
}

SPALTEN = [
    "typ", "ertrag", "punkte_haupt", "punkte_anteil", "zeilen_haupt", "zeilen_neben",
    "jahre_haupt", "jahre_gesamt", "erster", "letzter", "basis", "kontext",
    "niveau_I", "niveau_II", "niveau_III", "schritte_mittel", "schritte_fehlt",
    "thema", "leitidee", "status",
]


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


def messe(katalog_zeilen, typen_zeilen):
    """Alle Größen je Typ als Wörterbuch typ -> Kennzahlen; dazu die Katalog-Gesamtzahlen.

    typ_info      – typ -> {thema, leitidee, status} aus msa-typen.csv
    haupt, neben  – typ -> Liste der Katalogzeilen (Haupt- bzw. Nebenvorkommen)
    """
    typ_info = {z["typ"]: {"thema": z["thema"], "leitidee": z["leitidee"], "status": z["status"]}
                for z in typen_zeilen}

    haupt = collections.defaultdict(list)
    neben = collections.defaultdict(list)
    for z in katalog_zeilen:
        haupt[z["typ"]].append(z)
        for n in z["typ_neben"].split("|"):
            n = n.strip()
            if n:
                neben[n].append(z)

    alle_typen = set(typ_info) | set(haupt) | set(neben)
    gesamtpunkte = sum(int(z["punkte"]) for z in katalog_zeilen)

    kennzahlen = {}
    for typ in alle_typen:
        h, n = haupt.get(typ, []), neben.get(typ, [])
        jahre_haupt = {int(z["jahr"]) for z in h}
        jahre_gesamt = jahre_haupt | {int(z["jahr"]) for z in n}
        punkte_haupt = sum(int(z["punkte"]) for z in h)
        schritte_werte, schritte_fehlt = [], 0
        for z in h:
            try:
                schritte_werte.append(int(z["schritte"]))
            except ValueError:
                schritte_fehlt += 1
        info = typ_info.get(typ, {"thema": "", "leitidee": "", "status": NICHT_IN_TYPEN})
        k = {
            "typ": typ,
            "punkte_haupt": punkte_haupt,
            "punkte_anteil": round(punkte_haupt / gesamtpunkte * 100, 1),
            "zeilen_haupt": len(h),
            "zeilen_neben": len(n),
            "jahre_haupt": len(jahre_haupt),
            "jahre_gesamt": len(jahre_gesamt),
            "erster": min(jahre_gesamt) if jahre_gesamt else None,
            "letzter": max(jahre_gesamt) if jahre_gesamt else None,
            "basis": sum(1 for z in h if z["block"] == "Basis"),
            "kontext": sum(1 for z in h if z["block"] == "Kontext"),
            "niveau_I": sum(1 for z in h if z["niveau_geschaetzt"] == "I"),
            "niveau_II": sum(1 for z in h if z["niveau_geschaetzt"] == "II"),
            "niveau_III": sum(1 for z in h if z["niveau_geschaetzt"] == "III"),
            "schritte_mittel": round(sum(schritte_werte) / len(schritte_werte), 1) if schritte_werte else None,
            "schritte_fehlt": schritte_fehlt,
            "thema": info["thema"],
            "leitidee": info["leitidee"],
            "status": info["status"],
        }
        k["ertrag"] = (k["punkte_haupt"], k["jahre_gesamt"], k["zeilen_haupt"])
        kennzahlen[typ] = k
    return kennzahlen, gesamtpunkte


def reihenfolge(kennzahlen):
    """Alle Typen nach ertrag absteigend, bei Gleichstand alphabetisch nach typ (Determinismus)."""
    return sorted(kennzahlen.values(), key=lambda k: (tuple(-x for x in k["ertrag"]), k["typ"]))


def gesamtzahlen(kennzahlen, katalog_zeilen, gesamtpunkte):
    mit_hauptzeile = [k for k in kennzahlen.values() if k["zeilen_haupt"] > 0]
    nur_neben = [k for k in kennzahlen.values() if k["zeilen_haupt"] == 0 and k["zeilen_neben"] > 0]
    ohne_vorkommen = [k for k in kennzahlen.values() if k["zeilen_haupt"] == 0 and k["zeilen_neben"] == 0]
    return {
        "zeilen": len(katalog_zeilen),
        "punkte": gesamtpunkte,
        "mit_hauptzeile": len(mit_hauptzeile),
        "nur_neben": len(nur_neben),
        "ohne_vorkommen": len(ohne_vorkommen),
    }


def perzentil(werte_aufsteigend, p):
    """Wert, unter dem rund p Prozent der (aufsteigend sortierten) Werte liegen: Rang-Perzentil,
    Index floor(p/100 * n) auf die sortierte Liste, n = Zahl der Werte."""
    n = len(werte_aufsteigend)
    return werte_aufsteigend[min(int(p / 100 * n), n - 1)]


def tabelle_c(kennzahlen):
    mit_hauptzeile = [k for k in kennzahlen.values() if k["zeilen_haupt"] > 0]
    zeilen = []
    for feld in ("punkte_haupt", "jahre_gesamt", "zeilen_haupt"):
        werte = sorted(k[feld] for k in mit_hauptzeile)
        zeilen.append((feld, perzentil(werte, 10), perzentil(werte, 25), perzentil(werte, 50)))
    selten = sum(1 for k in mit_hauptzeile if k["jahre_gesamt"] <= 2)
    return zeilen, selten, len(mit_hauptzeile)


def tabelle_b(rang_a):
    """thema -> (punktsumme, [Typen in Ertragsfolge]), Themen nach Punktsumme absteigend (alphabetisch bei Gleichstand)."""
    gruppen = collections.defaultdict(list)
    for k in rang_a:
        gruppen[k["thema"]].append(k)
    themen = sorted(gruppen, key=lambda t: (-sum(k["punkte_haupt"] for k in gruppen[t]), t))
    return [(t, sum(k["punkte_haupt"] for k in gruppen[t]), gruppen[t]) for t in themen]


def de(zahl):
    """1234.5 -> '1234,5' fürs Markdown; None -> '–'."""
    if zahl is None:
        return "–"
    text = f"{zahl:.1f}" if isinstance(zahl, float) else str(zahl)
    return text.replace(".", ",")


def zeile_a(rang, k):
    return (f"| {rang} | {k['typ']} | {k['punkte_haupt']} | {de(k['punkte_anteil'])} % | {k['zeilen_haupt']} | "
            f"{k['zeilen_neben']} | {k['jahre_haupt']} | {k['jahre_gesamt']} | {k['erster'] or '–'} | "
            f"{k['letzter'] or '–'} | {k['basis']} | {k['kontext']} | {k['niveau_I']} | {k['niveau_II']} | "
            f"{k['niveau_III']} | {de(k['schritte_mittel'])} | {k['schritte_fehlt']} | {k['thema'] or '–'} | "
            f"{k['leitidee'] or '–'} | {k['status']} |")


def baue_md(kennzahlen, gesamt, stand, katalog_zeilen):
    rang_a = reihenfolge(kennzahlen)
    b = tabelle_b(rang_a)
    c_zeilen, c_selten, c_n = tabelle_c(kennzahlen)
    out = []
    w = out.append
    w("# Ertrag je Typ – Profil msa")
    w(f"Stand {stand}.")
    w("")
    w("Gezählt werden die Zeilen aus msa-katalog-basis.csv und msa-katalog-kontext.csv. Hauptzeilen sind "
      "Zeilen, deren Feld typ dem Typ entspricht; Nebenzeilen sind Zeilen, in deren Pipe-getrenntem Feld "
      "typ_neben der Typ vorkommt, unabhängig vom Haupttyp der Zeile. Jede Zeile hat genau einen Haupttyp, "
      "aber keine, eine oder mehrere Nebentypen; punkte_haupt, basis/kontext und niveau_I/II/III zählen nur "
      "Hauptzeilen.")
    w("")
    w(f"Gesamt: {gesamt['zeilen']} Zeilen, {gesamt['punkte']} Punkte, {gesamt['mit_hauptzeile']} Typen mit "
      f"Hauptzeile, {gesamt['nur_neben']} Typen nur als Nebentyp, {gesamt['ohne_vorkommen']} Typen ohne "
      "Vorkommen.")
    w("")
    w(f"Erzeugt von `werkzeuge/{VERSION.split()[0]}` ({VERSION.split()[1]}) aus den msa-Katalogen und "
      "msa-typen.csv; abgeleitet, nie von Hand ändern.")
    w("")
    w("## A Alle Typen nach Ertrag")
    w("Absteigend nach ertrag (punkte_haupt, bei Gleichstand jahre_gesamt, dann zeilen_haupt); bei "
      "vollständigem Gleichstand alphabetisch nach Typ. Typen mit Status „nicht in typen.csv“ haben kein "
      "Thema und keine Leitidee.")
    w("")
    w("| Rang | Typ | punkte_haupt | punkte_anteil | zeilen_haupt | zeilen_neben | jahre_haupt | "
      "jahre_gesamt | erster | letzter | basis | kontext | niveau_I | niveau_II | niveau_III | "
      "schritte_mittel | schritte_fehlt | thema | leitidee | status |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for rang, k in enumerate(rang_a, 1):
        w(zeile_a(rang, k))
    w("")
    w("## B Typen je Thema")
    w("Themen nach Punktsumme (punkte_haupt ihrer Typen) absteigend; die Typen je Thema in Ertragsfolge.")
    w("")
    for thema, punktsumme, typen in b:
        titel = thema if thema else "(kein Thema – Status „nicht in typen.csv“)"
        w(f"### {titel} – {punktsumme} Punkte, {len(typen)} Typen")
        w("")
        w("| Rang im Thema | Typ | punkte_haupt | zeilen_haupt | jahre_gesamt |")
        w("|---|---|---|---|---|")
        for rang, k in enumerate(typen, 1):
            w(f"| {rang} | {k['typ']} | {k['punkte_haupt']} | {k['zeilen_haupt']} | {k['jahre_gesamt']} |")
        w("")
    w("## C Verteilung (Hilfe für die Schwelle „selten“)")
    w(f"Nur Typen mit Hauptzeile ({c_n}). Perzentil im Rang-Sinn: sortierte Werte aufsteigend, Index "
      "floor(p/100 · n) – der Wert, unter dem rund p % der Typen liegen.")
    w("")
    w("| Kennzahl | 10 % | 25 % | 50 % |")
    w("|---|---|---|---|")
    for feld, p10, p25, p50 in c_zeilen:
        w(f"| {feld} | {p10} | {p25} | {p50} |")
    w("")
    w(f"Typen mit Hauptzeile und jahre_gesamt ≤ 2: {c_selten} von {c_n}.")
    w("")
    w("## D Typen ohne Hauptzeile")
    nur_neben = [k for k in rang_a if k["zeilen_haupt"] == 0 and k["zeilen_neben"] > 0]
    ohne_vorkommen = [k for k in rang_a if k["zeilen_haupt"] == 0 and k["zeilen_neben"] == 0]
    w(f"### Nur Nebentyp ({len(nur_neben)})")
    for k in nur_neben:
        w(f"- {k['typ']} – {k['thema'] or '–'}")
    if not nur_neben:
        w("- keine")
    w("")
    w(f"### Ohne Vorkommen ({len(ohne_vorkommen)})")
    for k in ohne_vorkommen:
        w(f"- {k['typ']} – {k['thema'] or '–'}")
    if not ohne_vorkommen:
        w("- keine")
    w("")
    return "\n".join(out)


def schreibe_csv(pfad, rang_a):
    with io.open(pfad, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writerow(SPALTEN)
        for k in rang_a:
            zeile = dict(k)
            zeile["ertrag"] = k["punkte_haupt"]  # Anzeige der Sortiergröße als Zahl; Tie-Break in jahre_gesamt/zeilen_haupt bereits eigene Spalten
            zeile["erster"] = k["erster"] if k["erster"] is not None else ""
            zeile["letzter"] = k["letzter"] if k["letzter"] is not None else ""
            zeile["schritte_mittel"] = f"{k['schritte_mittel']:.1f}" if k["schritte_mittel"] is not None else ""
            writer.writerow([zeile[s] for s in SPALTEN])


def gegenprobe(katalog_zeilen, gesamtpunkte):
    """Prüft die fünf Sollwerte aus katalog/prozentrechnung.md, „Prüfungsform (P10)“; meldet nur, bricht nicht ab."""
    thema_zeilen = [z for z in katalog_zeilen if z["thema"] == GEGENPROBE_THEMA]
    ist = {
        "Zeilen Thema Prozentrechnung": len(thema_zeilen),
        "Punktsumme Thema Prozentrechnung": sum(int(z["punkte"]) for z in thema_zeilen),
        "Punktsumme beider Kataloge": gesamtpunkte,
        "Jahre im Thema Prozentrechnung": len({z["jahr"] for z in thema_zeilen}),
        "Hauptzeilen „Prozentwert berechnen“ mit Thema Prozentrechnung":
            sum(1 for z in thema_zeilen if z["typ"] == GEGENPROBE_TYP),
    }
    print("Gegenprobe (katalog/prozentrechnung.md, „Prüfungsform (P10)“):")
    abweichungen = 0
    for name, soll in GEGENPROBE_SOLL.items():
        istwert = ist[name]
        if istwert == soll:
            print(f"  {name}: {istwert} (Soll {soll}) – ok")
        else:
            abweichungen += 1
            print(f"  {name}: {istwert} (Soll {soll}) – ABWEICHUNG")
    print("Alle fünf Werte stimmen." if not abweichungen else f"{abweichungen} von 5 Werten weichen ab.")
    return ist


def pruefungen(kennzahlen, katalog_zeilen, rang_a):
    """Die vier Prüfungen aus dem Auftrag (neben der Gegenprobe); meldet nur, bricht nicht ab."""
    print("Prüfungen:")
    summe_punkte_haupt = sum(k["punkte_haupt"] for k in kennzahlen.values())
    gesamtpunkte = sum(int(z["punkte"]) for z in katalog_zeilen)
    print(f"  Summe punkte_haupt = {summe_punkte_haupt}, Punktsumme beider Kataloge = {gesamtpunkte} – "
          + ("ok" if summe_punkte_haupt == gesamtpunkte else "ABWEICHUNG"))
    summe_zeilen_haupt = sum(k["zeilen_haupt"] for k in kennzahlen.values())
    print(f"  Summe zeilen_haupt = {summe_zeilen_haupt} (Soll 393) – "
          + ("ok" if summe_zeilen_haupt == 393 else "ABWEICHUNG"))
    ueberschuss = [k["typ"] for k in kennzahlen.values() if k["jahre_haupt"] > k["zeilen_haupt"]]
    print("  Typen mit jahre_haupt > zeilen_haupt: " + (", ".join(ueberschuss) if ueberschuss else "keine"))
    print(f"  Datenzeilen msa-ertrag.csv = Zeilen Tabelle A = {len(rang_a)} – ok (aus derselben Liste erzeugt).")


def main():
    msa = os.path.join(HIER, MSA)
    katalog_zeilen = []
    for name in KATALOGE:
        katalog_zeilen.extend(lies_csv(os.path.join(msa, name)))
    typen_zeilen = lies_csv(os.path.join(msa, TYPENLISTE))

    kennzahlen, gesamtpunkte = messe(katalog_zeilen, typen_zeilen)
    gesamt = gesamtzahlen(kennzahlen, katalog_zeilen, gesamtpunkte)
    rang_a = reihenfolge(kennzahlen)
    stand = f"{datetime.date.today().isoformat()}, Katalog auf Commit {head_kurz()}"

    schreibe_csv(os.path.join(msa, AUSGABE_CSV), rang_a)
    text = baue_md(kennzahlen, gesamt, stand, katalog_zeilen)
    with io.open(os.path.join(msa, AUSGABE_MD), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    fehlend_status = sorted(k["typ"] for k in kennzahlen.values() if k["status"] == NICHT_IN_TYPEN)
    print(f"{VERSION}: {len(katalog_zeilen)} Katalogzeilen, {len(typen_zeilen)} Typen aus {TYPENLISTE}, "
          f"{len(kennzahlen)} Typen insgesamt gezählt; {MSA}/{AUSGABE_CSV} und {MSA}/{AUSGABE_MD} geschrieben "
          f"({text.count(chr(10))} Zeilen).")
    print(f"typ/typ_neben-Werte nicht in {TYPENLISTE}: " + (", ".join(fehlend_status) if fehlend_status else "keine"))
    print(f"Gesamtzahlen: {gesamt['zeilen']} Zeilen, {gesamt['punkte']} Punkte, {gesamt['mit_hauptzeile']} Typen "
          f"mit Hauptzeile, {gesamt['nur_neben']} Typen nur als Nebentyp, {gesamt['ohne_vorkommen']} Typen ohne "
          "Vorkommen.")
    print("Tabelle A, die zehn obersten (Typ · punkte_haupt · jahre_gesamt · zeilen_haupt):")
    for k in rang_a[:10]:
        print(f"  {k['punkte_haupt']:4d} · {k['jahre_gesamt']:2d} · {k['zeilen_haupt']:2d} · {k['typ']}")

    pruefungen(kennzahlen, katalog_zeilen, rang_a)
    gegenprobe(katalog_zeilen, gesamtpunkte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
