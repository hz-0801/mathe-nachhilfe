# -*- coding: utf-8 -*-
"""fhr-bau.py – Gerüst für die Erfassung eines Hefts im Profil fhr.
Version 0.1 · 12.09.2026 · gilt mit katalog-prompt.md v0.3 und fhr.md v0.3

Je Heft werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles darunter
bleibt unverändert und prüft nach Kern Abschnitt 7.

Ablauf:
  1. Vorhandene fhr-katalog.csv und fhr-typen.csv neben dieses Skript legen
     (aus dem Repo, mit dem geprüften SHA). Fehlen sie, wird neu angelegt.
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen.
  3. python3 fhr-bau.py – schreibt beide CSV-Dateien und gibt Prüftabelle
     und Bericht aus. Bei einem Fehler wird nichts geschrieben.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    "jahr": "2026",
    "papier": "C",
    "datei": "26_FOS_Ma_LH_C.pdf",
    "seiten": 10,
    # Sollpunkte je Aufgabe aus der Punktetabelle am Ende jeder Aufgabe
    "soll": {"1": 27, "2": 23, "3": 20},
    "soll_gesamt": 70,
}

# ---- technischer Block, nicht ändern ----
HEAD = ("id;jahr;papier;block;aufgabe;titel;teilaufgabe;seite;punkte;stern;hilfsmittel;afb_amtlich;"
        "leitidee;thema;typ;typ_neben;stichwoerter;voraussetzungen;format;operator;antwort;material;"
        "skizze;kontext;textumfang;gegeben;gesucht;verfahren;schritte;zahlenraum;einheiten;"
        "abhaengig_von;ergebnis;zwischenergebnis;niveau_geschaetzt;fehlerquelle;bemerkung").split(";")

ZEILEN = []

def row(**kw):
    z = {k: "" for k in HEAD}
    z.update(jahr=KONFIG["jahr"], papier=KONFIG["papier"], block="", stern="",
             hilfsmittel="ja", afb_amtlich="")
    unbekannt = set(kw) - set(HEAD)
    if unbekannt:
        sys.exit(f"unbekanntes Feld: {sorted(unbekannt)}")
    z.update(kw)
    ZEILEN.append(z)

# ============================================================ ZEILEN JE HEFT
# Ein Eintrag je Teilaufgabe der Punktetabelle. Nicht genannte Felder bleiben
# leer; jahr, papier, hilfsmittel und die leeren Festwerte setzt row() selbst.
# Vorlage:
#   row(id="2026-B-1a", aufgabe="1", titel="Differentialrechnung",
#       teilaufgabe="a", seite="2", punkte="3",
#       leitidee="...", thema="...", typ="...", typ_neben="",
#       stichwoerter="...|...", voraussetzungen="",
#       format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
#       material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
#       gegeben="...", gesucht="...", verfahren="...", schritte="2",
#       zahlenraum="dezimal", einheiten="", abhaengig_von="",
#       ergebnis="... (amtlich)", zwischenergebnis="",
#       niveau_geschaetzt="II", fehlerquelle="...", bemerkung="Gutachten: ...")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = []

# ======================================================== AB HIER UNVERÄNDERT
KAT = "fhr-katalog.csv"
TYP = "fhr-typen.csv"
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]

# Themenliste nach fhr.md Abschnitt 6. Bei Änderung dort hier mitziehen.
THEMEN = {
 "Differentialrechnung": ["Ableitungen bilden", "Nullstellen ganzrationaler Funktionen",
   "Extrem- und Sattelpunkte", "Monotonie und Krümmung", "Wendepunkte", "Symmetrie nachweisen",
   "Verhalten im Unendlichen", "Graph zeichnen und zuordnen", "Anstieg und Tangente", "Normale",
   "Schnittpunkte von Funktionsgraphen", "Funktionsgleichung bestimmen", "Extremwertaufgaben"],
 "Integralrechnung": ["Stammfunktion bilden", "Bestimmtes Integral berechnen",
   "Fläche zwischen Graph und x-Achse", "Fläche zwischen zwei Graphen",
   "Rotationsvolumen um die x-Achse", "Körpervolumen aus Grundfläche und Länge"],
 "Stochastik": ["Daten darstellen und aufbereiten", "Statistische Kenngrößen",
   "Mehrstufige Zufallsexperimente", "Baumdiagramm und Pfadregeln",
   "Unabhängigkeit von Ereignissen", "Erwartungswert", "Kombinatorische Abzählverfahren"],
 "Grundlagen": ["Prozentrechnung", "Gleichungen lösen", "Größen und Einheiten", "Terme umformen"],
}
FORMATE = {"Ankreuzen","Kurzantwort","Rechnung","Begründung","Zeichnen","Konstruieren","Tabelle","Eintragen"}
ANTWORTEN = {"Zahl","Term","Text","Grafik","Kreuz","Tabelle"}
MATERIAL = {"keins","Figur","Körper","Koordinatensystem","Diagramm","Tabelle","Skizze","Foto"}
ZAHLENRAUM = {"ganz","dezimal","Bruch","negativ","Prozent","Potenz","Wurzel"}
PFLICHT = ("id jahr papier aufgabe teilaufgabe seite punkte hilfsmittel leitidee thema typ format "
           "operator antwort material skizze kontext textumfang gegeben gesucht verfahren schritte "
           "ergebnis niveau_geschaetzt fehlerquelle").split()

def lade(pfad, kopf):
    if not os.path.exists(pfad):
        return kopf, []
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    if not rows:
        return kopf, []
    if rows[0] != kopf:
        sys.exit(f"{pfad}: Kopfzeile weicht ab")
    return rows[0], rows[1:]

def schreibe(pfad, kopf, zeilen):
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(kopf)
        for z in zeilen:
            w.writerow(z)

def main():
    if not ZEILEN:
        sys.exit("ZEILEN ist leer – erst die Datensätze des Hefts eintragen.")
    fehler = []
    def a(cond, msg):
        if not cond:
            fehler.append(msg)

    _, alt_kat = lade(KAT, HEAD)
    _, alt_typ = lade(TYP, TYP_HEAD)
    alt_ids = {r[0] for r in alt_kat}
    typ_namen = {r[0] for r in alt_typ} | {t[0] for t in NEUE_TYPEN}
    neue_ids = [z["id"] for z in ZEILEN]

    # Kennungen
    a(len(set(neue_ids)) == len(neue_ids), "doppelte id in ZEILEN")
    for i in neue_ids:
        a(i not in alt_ids, f"{i}: Kennung steht schon im Katalog")
        a(re.fullmatch(r"\d{4}-[ABC]-\d[a-h]", i), f"{i}: Kennung folgt nicht dem Muster Jahr-papier-AufgabeTeilaufgabe")
    for t in NEUE_TYPEN:
        a(t[0] not in {r[0] for r in alt_typ}, f"Typ {t[0]}: steht schon in {TYP}")
        a(t[1] in THEMEN and t[2] in THEMEN.get(t[1], []), f"Typ {t[0]}: Leitidee oder Thema unbekannt")
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog")
        a(len(t[3]) > 20, f"Typ {t[0]}: Definition zu knapp")

    # Punkte
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        a(ist == soll, f"Aufgabe {nr}: Punkte {ist}, Soll {soll}")
    a(sum(int(z["punkte"]) for z in ZEILEN) == KONFIG["soll_gesamt"],
      f"Gesamtpunktzahl weicht von {KONFIG['soll_gesamt']} ab")

    # Felder
    verwendet = set()
    for z in ZEILEN:
        for k in PFLICHT:
            a(z[k].strip() != "", f"{z['id']}: Pflichtfeld leer: {k}")
        a(z["jahr"] == KONFIG["jahr"] and z["papier"] == KONFIG["papier"], f"{z['id']}: Heftkennung falsch")
        a(z["leitidee"] in THEMEN, f"{z['id']}: Leitidee unbekannt")
        a(z["thema"] in THEMEN.get(z["leitidee"], []), f"{z['id']}: Thema passt nicht zur Leitidee")
        a(z["niveau_geschaetzt"] in ("I", "II", "III"), f"{z['id']}: Niveau ungültig")
        a(z["textumfang"] in ("kurz", "mittel", "lang"), f"{z['id']}: textumfang ungültig")
        a(int(z["seite"]) <= KONFIG["seiten"], f"{z['id']}: Seite größer als der Heftumfang")
        for wert, menge, name in ((z["format"], FORMATE, "format"), (z["antwort"], ANTWORTEN, "antwort"),
                                  (z["material"], MATERIAL, "material"), (z["zahlenraum"], ZAHLENRAUM, "zahlenraum")):
            for teil in [s for s in wert.split("|") if s]:
                a(teil in menge, f"{z['id']}: {name} hat unbekannten Wert: {teil}")
        for feld in ("typ", "typ_neben"):
            for t in [s for s in z[feld].split("|") if s]:
                verwendet.add(t)
                a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        for dep in [s for s in z["abhaengig_von"].split("|") if s]:
            a(dep in neue_ids or dep in alt_ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
        for k, v in z.items():
            a("?" not in v or k == "bemerkung" or z["bemerkung"].strip() != "",
              f"{z['id']}: Fragezeichen in {k} ohne Grund in bemerkung")
            a(not re.search(r"(?<=[\d\s(])-(?=\d)", v),
              f"{z['id']}: ASCII-Bindestrich als Minus in {k}")
            a(not re.search(r"[A-Za-z](ae|oe|ue|ss)[a-z]", v) or k in ("stichwoerter",) or
              re.search(r"[äöüß]", v) or v in ("Masse",),
              f"{z['id']}: mögliche ASCII-Umschrift in {k}: {v[:40]}")
    a(not ({t[0] for t in NEUE_TYPEN} - verwendet),
      f"neue Typen unbenutzt: {sorted({t[0] for t in NEUE_TYPEN} - verwendet)}")

    if fehler:
        print(f"ABBRUCH – {len(fehler)} Fehler, nichts geschrieben:")
        for f_ in fehler:
            print(" -", f_)
        sys.exit(1)

    schreibe(KAT, HEAD, alt_kat + [[z[k] for k in HEAD] for z in ZEILEN])
    schreibe(TYP, TYP_HEAD, alt_typ + [[t[0], t[1], t[2], t[3], t[4], "neu"] for t in NEUE_TYPEN])

    # Rückweg: geschriebene Datei mit echtem Leser einlesen und vergleichen
    _, zurueck = lade(KAT, HEAD)
    for gel, z in zip(zurueck[len(alt_kat):], ZEILEN):
        if len(gel) != 37 or any(v != z[k] for k, v in zip(HEAD, gel)):
            sys.exit(f"{z['id']}: Rückweg verändert die Zeile")
    roh = io.open(KAT, encoding="utf-8", newline="").read()
    if "\r" in roh or not all(l.startswith('"') and l.endswith('"') for l in roh.splitlines()):
        sys.exit("Ausgabe nicht vollständig gequotet oder CRLF")

    # Prüftabelle
    print(f"Heft {KONFIG['jahr']} {KONFIG['papier']} – {len(ZEILEN)} Zeilen, "
          f"{len(NEUE_TYPEN)} Typen neu, Katalog jetzt {len(alt_kat) + len(ZEILEN)} Zeilen\n")
    print(f"{'id':<12} {'P':>2}  {'thema':<38} {'typ':<44} ergebnis")
    for z in ZEILEN:
        print(f"{z['id']:<12} {z['punkte']:>2}  {z['thema']:<38} {z['typ']:<44} {z['ergebnis'][:60]}")
    print()
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        print(f"Aufgabe {nr}: Ist {ist} / Soll {soll}")
    print(f"Gesamt: {sum(int(z['punkte']) for z in ZEILEN)} / {KONFIG['soll_gesamt']}")
    unsicher = [z["id"] for z in ZEILEN if any("?" in v for v in z.values())]
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    print("Alle Prüfungen bestanden.")

if __name__ == "__main__":
    main()
