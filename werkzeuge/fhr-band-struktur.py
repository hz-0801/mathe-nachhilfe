# -*- coding: utf-8 -*-
"""
fhr-band-struktur.py v0.2 · 18.09.2026 · Profil fhr
Erzeugt die Strukturliste fhr-band.csv für band-bau.py. Anleitung: band-anleitung.md.

Änderungen gegenüber 0.1 (Nachtrag zum Musterband): ein Heft der Heftliste ohne
Katalogzeilen führt zu einem klaren Abbruch („erst erfassen, dann bauen") statt zu
einem KeyError; Ausgabe unverändert (fhr-band.csv byteidentisch).

Quellen (nur gelesen): fhr-pruefungen.md (Heftliste: Jahr, Buchstabe, Prüfungsdatum,
BE-Verteilung), fhr-katalog.csv (Aufgabenstart und Titel je Aufgabe, Feld seite =
Heftseite ab 1), hefte/fhr/<jahr>-<papier>.pdf (Seitentext zur Erkennung von
Deckblatt, Erwartungshorizont und Gutachtenbogen; Deckblattdatum als Ersatz, wenn
fhr-pruefungen.md nur das Jahr nennt).

Die Liste ist ausgabeunabhängig: Reihenfolge, Kennung, Titel, Datei und Seitenbereich
je Einheit, dazu eine Hinweiszeile je Heft. Seiten sind Heftseiten ab 1, keine
Bandseiten. Drei Ebenen:
  1  Jahrgang        kennung <jahr>
  2  Heft            kennung <jahr>-<papier>, datei, von 1 bis Seitenzahl, hinweis
  3  Abschnitt       kennung <heft>-deckblatt | <heft>-<aufgabe> | <heft>-<aufgabe>-eh | <heft>-gutachten
Konvention für band-bau.py: die Aufgabenkennung ist Präfix der Katalog-ids
(2026-C-1 → 2026-C-1a); der Erwartungshorizont einer Aufgabe trägt das Suffix -eh.

Läuft die Datei schon vorhanden, bleiben die Zeilen der Ebenen 1 und 2 in ihrer
Reihenfolge und mit ihren Texten erhalten (dort darf von Hand umgestellt werden);
nur die Abschnittszeilen (Ebene 3) werden neu erzeugt, neue Hefte aus
fhr-pruefungen.md werden angehängt. Abschnittszeilen nie von Hand pflegen.

Aufruf: python fhr-band-struktur.py   (neben den Quelldateien; pypdf im PYTHONPATH)
"""
import csv
import io
import re
import sys
import logging
from pathlib import Path

logging.disable(logging.CRITICAL)  # pypdf-Warnungen zu Schriften unterdrücken
from pypdf import PdfReader

HIER = Path(__file__).resolve().parent.parent  # Umbau 2026-09-19: Repo-Wurzel; Skript liegt in werkzeuge/
PRUEFUNGEN = HIER / "fhr" / "fhr-pruefungen.md"
KATALOG = HIER / "fhr" / "fhr-katalog.csv"
HEFTE = HIER / "hefte" / "fhr"
ZIEL = HIER / "werkzeuge" / "fhr-band.csv"

KOPF = ["ebene", "kennung", "titel", "datei", "von", "bis", "hinweis"]
HINWEIS = ("Prüfung {datum} · 180 Minuten · 70 BE ({punkte}) · Formelsammlung, "
           "WTR ohne CAS · drei Aufgaben, alle zu bearbeiten")

MONATE = {"Januar": 1, "Februar": 2, "März": 3, "April": 4, "Mai": 5, "Juni": 6, "Juli": 7,
          "August": 8, "September": 9, "Oktober": 10, "November": 11, "Dezember": 12}


def heftliste():
    """Tabelle „Hefte im Erfassungsumfang" aus fhr-pruefungen.md: (jahr, papier) → Zeile."""
    hefte = {}
    for zeile in PRUEFUNGEN.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d{4})\s*\|\s*([A-C])\s*\|\s*(\S+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", zeile)
        if m:
            jahr, papier, datei, pruefung, seiten, punkte = m.groups()
            hefte[(jahr, papier)] = dict(datei=datei, pruefung=pruefung, seiten=int(seiten),
                                        punkte=punkte.split("=")[0].replace(" ", ""))
    return hefte


def aufgaben_aus_katalog():
    """(jahr, papier) → {aufgabe: (Startseite, Titel)} aus fhr-katalog.csv."""
    aufg = {}
    with open(KATALOG, encoding="utf-8", newline="") as f:
        for z in csv.DictReader(f, delimiter=";", quotechar='"'):
            k = (z["jahr"], z["papier"])
            a = int(z["aufgabe"])
            s = int(z["seite"])
            alt = aufg.setdefault(k, {}).get(a)
            if alt is None or s < alt[0]:
                aufg[k][a] = (s, z["titel"])
    return aufg


def seitensorte(text):
    if re.search(r"Gutachten zur schriftlichen", text):
        return "G"
    if re.search(r"Erwartete Teilleistung", text):
        return "E"
    if re.search(r"\d\.\s*Aufgabe\s*:", text):
        return "A"
    if re.search(r"Unterlagen für die Lehrkraft", text):
        return "D"
    return "?"  # Folgeseite ohne eigene Kopfzeile: erbt die Sorte der Vorseite


def deckblattdatum(text):
    m = re.search(r"(\d{2})\.\s*(\w+)\s+(\d{4})", text)
    if m and m.group(2) in MONATE:
        return f"{int(m.group(1)):02d}.{MONATE[m.group(2)]:02d}.{m.group(3)}"
    return None


def abschnitte(jahr, papier, aufg, meldungen):
    """Abschnittszeilen (Ebene 3) eines Hefts aus Seitentext und Katalog; dazu Seitenzahl und Deckblattdatum."""
    datei = HEFTE / f"{jahr}-{papier.lower()}.pdf"
    rd = PdfReader(str(datei))
    texte = [p.extract_text() or "" for p in rd.pages]
    n = len(texte)
    sorten = [seitensorte(t) for t in texte]
    for i in range(1, n):
        if sorten[i] == "?":
            sorten[i] = sorten[i - 1]
    if sorten[0] == "?":
        raise SystemExit(f"{datei.name}: Seite 1 nicht erkannt")
    laeufe, start = [], 0
    for i in range(1, n + 1):
        if i == n or sorten[i] != sorten[start]:
            laeufe.append((sorten[start], start + 1, i))
            start = i
    heft = f"{jahr}-{papier}"
    zeilen, anr = [], 0
    for sorte, von, bis in laeufe:
        if sorte == "D":
            zeilen.append(["3", f"{heft}-deckblatt", "Deckblatt", "", von, bis, ""])
        elif sorte == "A":
            anr += 1
            if anr not in aufg:
                raise SystemExit(f"{heft}: Aufgabe {anr} im Katalog nicht gefunden")
            ks, titel = aufg[anr]
            if ks != von:
                raise SystemExit(f"{heft}: Aufgabe {anr} beginnt laut Katalog S. {ks}, laut Seitentext S. {von}")
            zeilen.append(["3", f"{heft}-{anr}", f"Aufgabe {anr}: {titel}", "", von, bis, ""])
        elif sorte == "E":
            zeilen.append(["3", f"{heft}-{anr}-eh", f"Erwartungshorizont Aufgabe {anr}", "", von, bis, ""])
        elif sorte == "G":
            zeilen.append(["3", f"{heft}-gutachten", "Gutachtenbogen", "", von, bis, ""])
    if anr != len(aufg):
        raise SystemExit(f"{heft}: {anr} Aufgaben im Heft, {len(aufg)} im Katalog")
    return zeilen, n, deckblattdatum(texte[0])


def vorhandene_liste():
    if not ZIEL.exists():
        return []
    with open(ZIEL, encoding="utf-8", newline="") as f:
        r = csv.reader(f, delimiter=";", quotechar='"')
        kopf = next(r)
        if kopf != KOPF:
            raise SystemExit(f"{ZIEL.name}: unerwartete Kopfzeile {kopf}")
        return [z for z in r if z]


def main():
    hefte = heftliste()
    aufg = aufgaben_aus_katalog()
    fehlt = sorted(set(aufg) - set(hefte))
    if fehlt:
        raise SystemExit(f"Im Katalog, aber nicht in fhr-pruefungen.md: {fehlt}")
    nicht_erfasst = sorted(set(hefte) - set(aufg))
    if nicht_erfasst:
        raise SystemExit(f"In fhr-pruefungen.md, aber ohne Katalogzeilen: {nicht_erfasst} – "
                         "erst erfassen, dann bauen (band-anleitung.md § 6)")
    meldungen = []

    alt = vorhandene_liste()
    # Ebenen 1 und 2 der vorhandenen Liste behalten, Ebene 3 verwerfen
    grund = [z for z in alt if z[0] in ("1", "2")]
    bekannt = {z[1] for z in grund if z[0] == "2"}
    # neue Hefte aus fhr-pruefungen.md anhängen, aufsteigend nach Jahr und Buchstabe
    for (jahr, papier) in sorted(hefte):
        k = f"{jahr}-{papier}"
        if k in bekannt:
            continue
        if not any(z[0] == "1" and z[1] == jahr for z in grund):
            grund.append(["1", jahr, f"Prüfung {jahr}", "", "", "", ""])
        # hinter dem letzten Heft desselben Jahrgangs einfügen
        pos = max(i for i, z in enumerate(grund) if z[1] == jahr or (z[0] == "2" and z[1].startswith(jahr + "-"))) + 1
        grund.insert(pos, ["2", k, f"Aufgabenvorschlag {papier}", f"hefte/fhr/{jahr}-{papier.lower()}.pdf", "", "", ""])
        bekannt.add(k)

    neu = []
    for z in grund:
        neu.append(z)
        if z[0] != "2":
            continue
        jahr, papier = z[1].split("-")
        h = hefte[(jahr, papier)]
        zeilen, n, datum_deck = abschnitte(jahr, papier, aufg[(jahr, papier)], meldungen)
        if n != h["seiten"]:
            raise SystemExit(f"{z[1]}: {n} PDF-Seiten, fhr-pruefungen.md nennt {h['seiten']}")
        z[4], z[5] = "1", str(n)
        if not z[6]:  # Hinweiszeile nur setzen, wenn noch keine da ist (Handänderung bleibt)
            datum = h["pruefung"]
            if not re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", datum):
                if datum_deck:
                    meldungen.append(f'{z[1]}: fhr-pruefungen.md nennt „{datum}", Deckblatt sagt {datum_deck} – Deckblattdatum verwendet')
                    datum = datum_deck
                else:
                    meldungen.append(f'{z[1]}: kein Prüfungsdatum gefunden, „{datum}" übernommen')
            z[6] = HINWEIS.format(datum=datum, punkte=h["punkte"])
        elif datum_deck and datum_deck not in z[6]:
            meldungen.append(f"{z[1]}: Hinweiszeile nennt nicht das Deckblattdatum {datum_deck} (belassen)")
        for a in zeilen:
            a[4], a[5] = str(a[4]), str(a[5])
        neu.extend(zeilen)

    # Schreiben: Semikolon, alles gequotet, UTF-8, LF – wie die Kataloge
    puffer = io.StringIO()
    w = csv.writer(puffer, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(KOPF)
    for z in neu:
        w.writerow(z)
    ZIEL.write_bytes(puffer.getvalue().encode("utf-8"))

    e1 = sum(1 for z in neu if z[0] == "1"); e2 = sum(1 for z in neu if z[0] == "2"); e3 = sum(1 for z in neu if z[0] == "3")
    print(f"{ZIEL.name} geschrieben: {e1} Jahrgänge, {e2} Hefte, {e3} Abschnitte, {sum(int(z[5]) for z in neu if z[0] == '2')} Heftseiten")
    for m in meldungen:
        print("Hinweis:", m)


if __name__ == "__main__":
    main()
