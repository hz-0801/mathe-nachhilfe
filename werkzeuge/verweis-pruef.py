# -*- coding: utf-8 -*-
"""
verweis-pruef.py v0.1 · 21.09.2026 · Verweis- und Namensprüfung des Themenkatalogs

Der Themenkatalog (katalog/, 73 Einträge) war bis zu diesem Werkzeug nie maschinell
auf innere Stimmigkeit geprüft: ob die Verweise <name>.md ein Ziel haben, ob die
Einheitsnummern hinter Verweisen in der Zieldatei existieren, ob Dateinamen,
H1-Überschriften und die Themenkonkordanz themen.csv zusammenpassen, ob ein
vorausgesetzter Eintrag den voraussetzenden erwähnt und welche Einträge ihre
Voraussetzungen noch in Wortform nennen (Auftrag Verweis- und Namensprüfung,
21.09.2026 – vor dem Umbau der beiden Blatt-Prompte). Das Werkzeug ändert keinen
Katalogeintrag und keine Zeile in themen.csv; es berichtet.

Lesarten aus werkzeuge/tragfaehigkeit.py (v0.1), importiert, nicht nachgebaut, damit
beide Werkzeuge gleich zählen: die Liste der Einträge (katalog/*.md ohne _* und
index.md), der Abschnitt „### Voraussetzungen (Blatt 0)“ bis zur nächsten
Überschrift (blatt0), die Verweisform <name>.md (VERWEIS; ein Pfad davor wird
mitgenommen), die Nennung in Wortform „Thema X“ (WORTFORM, Heuristik) und der
Fundort einer Datei außerhalb von katalog/ (fundort). Die Themenliste aus
abitur/abitur-vokabular.md § 2 liest vokabular_themen() von themen-pruef.py.

Fünf Prüfungen (Einzelheiten in der Messweise jedes Abschnitts von _verweise.md):
  1 Dateiverweise    – jeder Verweis <name>.md in jedem Abschnitt jedes Eintrags;
                       Gruppe a: Ziel in katalog/, b: anderswo im Repo, c: keine Datei.
                       b und c vollständig mit Quelldatei und Abschnitt.
  2 Einheitennummern – Einheitenangabe direkt hinter einem Verweis („x.md Einheit 4“,
                       „x.md, Einheit 6 und 8“, „x.md (Einheiten 2 bis 4)“) gegen die
                       Zahl der Zeilen „<n>. “ im Abschnitt „### Lerneinheiten“ der
                       Zieldatei; Nummer größer als vorhanden wird gemeldet. Angaben,
                       die sich keinem Verweis eindeutig zuordnen lassen (Verweisreihung
                       davor, kurzer Zwischentext, Angabe vor dem Verweis), werden
                       getrennt gelistet, nicht geraten.
  3 Namensgleichheit – Datei <-> kanonisch in themen.csv (Stufe II braucht eine Datei);
                       H1 gegen die thema-Werte der eigenen Zeilen (melden, nicht
                       bewerten); abi/iqb-Themen gegen Vokabular § 2 und die vier
                       Geltungstabellen § 1, msa/fhr-Themen gegen die Themenspalte ihres
                       Typenkatalogs – jeweils in beide Richtungen. Ist die Themenspalte
                       einer Datei über die Kopfzeile nicht eindeutig, bricht die
                       Teilprüfung ab und meldet es.
  4 Gegenrichtung    – A nennt B unter Blatt 0, B nennt A.md in keinem Abschnitt: Paar.
  5 Formlücke        – Einträge ohne Verweis auf einen anderen Katalogeintrag in Blatt 0
                       (dieselbe Menge wie die Messlücken von _tragfaehigkeit.md), je
                       Eintrag die Zahl der Nennungen in Wortform und jede Zeile, die
                       eine trägt, als wörtliches Zitat.

Schreibt katalog/_verweise.md (Kopf mit Stand und Commit, je Prüfung Messweise und
Befunde, am Ende „Schwäche der Messung“) und eine Kurzfassung auf stdout (höchstens
40 Zeilen je Prüfung). Zwei Läufe hintereinander erzeugen dieselbe Datei bis auf die
Stand-Zeile. _pruef_struktur.py importiert messe() für Kennzahl 8 (Verweise auf
fehlende Dateien, Einheitsnummern größer als vorhanden).

Aufruf aus der Repo-Wurzel (nach jeder Katalogänderung, vor dem Commit):
  python werkzeuge/verweis-pruef.py
"""
import collections
import csv
import datetime
import importlib.util
import io
import os
import re
import sys

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Repo-Wurzel; Skript liegt in werkzeuge/
WERKZEUGE = os.path.join(HIER, "werkzeuge")
VERSION = "verweis-pruef.py v0.1"
KATALOG_ORDNER = "katalog"
KONKORDANZ = "themen.csv"
VOKABULAR = "abitur/abitur-vokabular.md"
GELTUNG = ["abitur/abi-be-gk-geltung.md", "abitur/abi-be-lk-geltung.md",
           "abitur/abi-bb-gk-geltung.md", "abitur/abi-bb-ea-geltung.md"]
TYPENKATALOGE = collections.OrderedDict([("msa", "msa/msa-typen.csv"), ("fhr", "fhr/fhr-typen.csv")])
AUSGABE = "_verweise.md"  # in katalog/
STDOUT_ZEILEN = 40  # Kurzfassung: höchstens so viele Befundzeilen je Prüfung

if WERKZEUGE not in sys.path:
    sys.path.insert(0, WERKZEUGE)
import tragfaehigkeit as T  # noqa: E402  (Vorbild: Einträge, blatt0, VERWEIS, WORTFORM, fundort, head_kurz)


def lade_modul(dateiname, name):
    """Modul aus einer Datei laden, deren Name kein Python-Bezeichner ist (themen-pruef.py)."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(WERKZEUGE, dateiname))
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


TP = lade_modul("themen-pruef.py", "themen_pruef")  # vokabular_themen(), lies_csv()

UEBERSCHRIFT = re.compile(r"^(#{1,6}) (.+?)[ \t]*$", re.M)
KURZNAME = {  # Abschnittsüberschrift -> Kurzname in den Listen
    "Verortung": "Verortung", "Lerneinheiten": "Lerneinheiten", "Typen je Lerneinheit": "Typen",
    "Voraussetzungen (Blatt 0)": "Blatt 0", "Merkkasten": "Merkkasten", "Typische Fehler": "Fehler",
    "Für schwache Schüler": "Schwache", "Prüfungsform (P10)": "Prüfungsform",
    "Prüfungsform (fhr / abi / iqb)": "Prüfungsform", "Offene Punkte des Eintrags": "Offene Punkte",
}
# Einheitenangabe: „Einheit 4“, „Einheit 6 und 8“, „Einheiten 2 bis 4“, „Einheit 2, 3 und 5“, „Einheit 1–2“,
# „Einheit 1 und Einheit 3“; Nummern ein- oder zweistellig, damit Jahreszahlen und ids nicht anhängen.
# Fortsetzungswörter wie in _pruef_struktur.py und _pruef_katalog.py (bis, –, -, und, Komma, /).
ZAHL = r"\d{1,2}(?!\d)"
EINHEIT = re.compile(r"Einheit(?:en)?\s+" + ZAHL + r"(?:\s*(?:bis|–|-|und|,|/)\s*(?:Einheit(?:en)?\s+)?" + ZAHL + r")*")
DIREKT = re.compile(r"\s*|,\s*|\s*\(\s*")                     # zwischen <name>.md und „Einheit“: direkt dahinter
# (kein Gedankenstrich: „x.md – Einheit 4 führt hier …“ leitet einen neuen Satzteil über eine eigene Einheit ein)
REIHUNG = re.compile(r"\s*(?:,|und|oder|bzw\.|sowie)\s*")     # zwischen zwei Verweisen: „a.md und b.md Einheit 2“
DAVOR = re.compile(r"\s+(?:in|von|aus|der|des|bei|im)\s+(?:der\s+|des\s+)?")  # „Einheit 4 in <name>.md“
KLAUSEL = re.compile(r"[.;:)\]]")                             # Satz- oder Klammerende im Zwischentext
KURZ_WOERTER = 4                                              # Zwischentext bis zu so vielen Wörtern gilt als „nah“
LERNEINHEITEN = re.compile(r"^### Lerneinheiten[^\n]*\n(.*?)(?=^### |^## |\Z)", re.S | re.M)
NUMMERIERT = re.compile(r"^\d+\. ", re.M)
H1 = re.compile(r"^# (.+?)[ \t]*$", re.M)


# ---------------------------------------------------------------- Hilfen

def lies(pfad):
    with io.open(pfad, encoding="utf-8") as fh:
        return fh.read()


def zeilennr(text, pos):
    """Zeilennummer (ab 1) der Position pos im Text."""
    return text.count("\n", 0, pos) + 1


def kurzname(rauten, titel):
    if rauten == "#":
        return "Kopf"
    if titel.startswith("Prüfliste"):
        return "Prüfliste"
    return KURZNAME.get(titel, titel)


def abschnitte(text):
    """[(kurzname, anfang, ende)] – die Abschnitte eines Eintrags nach seinen Überschriften (#, ##, ###);
    Text vor der ersten Überschrift hieße „Kopf“ (kommt nicht vor: jeder Eintrag beginnt mit „# Titel“, dessen
    Statuszeilen bis zur ersten ###-Überschrift der Kopf sind)."""
    treffer = list(UEBERSCHRIFT.finditer(text))
    teile = []
    if not treffer:
        return [("Kopf", 0, len(text))]
    if treffer[0].start() > 0:
        teile.append(("Kopf", 0, treffer[0].start()))
    for i, m in enumerate(treffer):
        ende = treffer[i + 1].start() if i + 1 < len(treffer) else len(text)
        teile.append((kurzname(m.group(1), m.group(2)), m.end(), ende))
    return teile


def zeilen(text, anfang, ende):
    """[(zeilentext, absolute Anfangsposition)] der Zeilen von text[anfang:ende]."""
    aus = []
    pos = anfang
    for z in text[anfang:ende].split("\n"):
        aus.append((z, pos))
        pos += len(z) + 1
    return aus


def lerneinheiten(text):
    """Zahl der Lerneinheiten: Zeilen im Abschnitt „### Lerneinheiten“, die mit „<n>. “ beginnen; None ohne Abschnitt."""
    m = LERNEINHEITEN.search(text)
    return len(NUMMERIERT.findall(m.group(1))) if m else None


def fenster(zeile, anfang, ende, davor=50, danach=40):
    """Ausschnitt einer Zeile um [anfang, ende) mit Auslassungszeichen."""
    a, e = max(0, anfang - davor), min(len(zeile), ende + danach)
    return ("…" if a > 0 else "") + zeile[a:e] + ("…" if e < len(zeile) else "")


def themenspalte_tabelle(text, datei):
    """Werte der Spalte „Thema“ der Tabelle in § 1 einer Geltungsdatei; (werte, None) oder (None, Grund)."""
    m = re.search(r"^## 1 Themen[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return None, f"{datei}: Abschnitt „## 1 Themen“ nicht gefunden"
    reihen = [z for z in m.group(1).splitlines() if z.strip().startswith("|")]
    if not reihen:
        return None, f"{datei}: keine Tabelle in § 1"
    kopf = [c.strip() for c in reihen[0].strip().strip("|").split("|")]
    if kopf.count("Thema") != 1:
        return None, f"{datei}: Kopfzeile {kopf} nennt „Thema“ {kopf.count('Thema')}-mal – Themenspalte nicht eindeutig"
    i = kopf.index("Thema")
    werte = []
    for z in reihen[1:]:
        zellen = [c.strip() for c in z.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in zellen if c):
            continue  # Trennzeile
        if i < len(zellen) and zellen[i]:
            werte.append(zellen[i])
    return werte, None


def themenspalte_csv(pfad, datei):
    """Werte der Spalte thema eines Typenkatalogs; (werte, None) oder (None, Grund)."""
    with io.open(pfad, encoding="utf-8-sig", newline="") as fh:
        leser = csv.reader(fh, delimiter=";")
        kopf = next(leser, None)
        if kopf is None:
            return None, f"{datei}: leer"
        if kopf.count("thema") != 1:
            return None, f"{datei}: Kopfzeile {kopf} nennt „thema“ {kopf.count('thema')}-mal – Themenspalte nicht eindeutig"
        i = kopf.index("thema")
        return [z[i].strip() for z in leser if len(z) > i], None


# ---------------------------------------------------------------- Prüfungen

def pruefe_verweise(texte, vorhanden):
    """Prüfung 1. Jede Fundstelle: quelle, abschnitt, zeile, verweis (wie geschrieben), pfad, ziel, gruppe (a/b/c),
    art (a: eintrag | eintrag-pfad | selbst | sonstige; b/c: -), ort (Ordner relativ zur Wurzel oder None)."""
    funde = []
    orte = {}
    for name, text in texte.items():
        for kurz, a, e in abschnitte(text):
            for m in T.VERWEIS.finditer(text, a, e):
                pfad, ziel = m.group(1), m.group(2)
                verweis = pfad + ziel + ".md"
                if pfad:
                    voll = os.path.normpath(os.path.join(HIER, pfad, ziel + ".md"))
                    ort = [os.path.relpath(os.path.dirname(voll), HIER).replace(os.sep, "/")] if os.path.isfile(voll) else None
                elif ziel in vorhanden:
                    ort = [KATALOG_ORDNER]
                else:
                    if verweis not in orte:
                        orte[verweis] = T.fundort(verweis)
                    ort = orte[verweis]
                if ort is None:
                    gruppe, art = "c", "-"
                elif KATALOG_ORDNER in ort:
                    gruppe = "a"
                    if ziel not in vorhanden:
                        art = "sonstige"
                    elif pfad:
                        art = "eintrag-pfad"
                    elif ziel == name:
                        art = "selbst"
                    else:
                        art = "eintrag"
                else:
                    gruppe, art = "b", "-"
                funde.append({"quelle": name, "abschnitt": kurz, "zeile": zeilennr(text, m.start()),
                              "verweis": verweis, "pfad": pfad, "ziel": ziel, "gruppe": gruppe, "art": art,
                              "ort": ort})
    return funde


def pruefe_einheiten(texte, vorhanden, einheiten):
    """Prüfung 2. zugeordnet: Einheitenangaben direkt hinter einem Verweis (ziel, nummern, vorhanden, zu_gross,
    pruefbar); unklar: Einheitenangaben im Verweiskontext ohne eindeutigen Verweis (art, zitat); gesamt: alle
    Einheitenangaben der Einträge (die übrigen gelten als eigene Einheiten des Eintrags und werden nicht geprüft)."""
    zugeordnet, unklar = [], []
    gesamt = 0
    for name, text in texte.items():
        for kurz, a, e in abschnitte(text):
            for zeile, pos in zeilen(text, a, e):
                refs = list(T.VERWEIS.finditer(zeile))
                angaben = list(EINHEIT.finditer(zeile))
                gesamt += len(angaben)
                if not refs:
                    continue
                for m in angaben:
                    fund = {"quelle": name, "abschnitt": kurz, "zeile": zeilennr(text, pos), "angabe": m.group(0)}
                    davor = [r for r in refs if r.end() <= m.start()]
                    danach = [r for r in refs if r.start() >= m.end()]
                    if davor:
                        r = davor[-1]
                        luecke = zeile[r.end():m.start()]
                        if DIREKT.fullmatch(luecke):
                            i = refs.index(r)
                            if i > 0 and REIHUNG.fullmatch(zeile[refs[i - 1].end():r.start()]):
                                fund.update(art="Verweisreihung davor", kandidaten=[refs[i - 1].group(0), r.group(0)],
                                            zitat=fenster(zeile, refs[i - 1].start(), m.end()))
                                unklar.append(fund)
                                continue
                            ziel, pfad = r.group(2), r.group(1)
                            nummern = [int(z) for z in re.findall(r"\d+", m.group(0))]
                            pruefbar = not pfad and ziel in vorhanden and einheiten.get(ziel) is not None
                            fund.update(verweis=r.group(0), ziel=ziel, nummern=nummern, pruefbar=pruefbar,
                                        vorhanden=einheiten.get(ziel) if pruefbar else None,
                                        zu_gross=pruefbar and max(nummern) > einheiten[ziel],
                                        zitat=fenster(zeile, r.start(), m.end()))
                            zugeordnet.append(fund)
                            continue
                        if (not EINHEIT.search(luecke) and not KLAUSEL.search(luecke)
                                and len(re.findall(r"\w+", luecke)) <= KURZ_WOERTER):
                            fund.update(art="kurzer Zwischentext", kandidaten=[r.group(0)],
                                        zitat=fenster(zeile, r.start(), m.end()))
                            unklar.append(fund)
                            continue
                    if danach:
                        r = danach[0]
                        if DAVOR.fullmatch(zeile[m.end():r.start()]):
                            fund.update(art="Angabe vor dem Verweis", kandidaten=[r.group(0)],
                                        zitat=fenster(zeile, m.start(), r.end()))
                            unklar.append(fund)
    return {"zugeordnet": zugeordnet, "unklar": unklar, "gesamt": gesamt}


def pruefe_namen(texte, konkordanz):
    """Prüfung 3, vier Abgleiche; jedes Ergebnis ist eine Liste von Befundzeilen (leer = bestanden) oder trägt
    unter 'abbruch' den Grund, warum eine Teilprüfung nicht lief."""
    aus = collections.OrderedDict()
    dateien = list(texte)
    nach_kanonisch = collections.OrderedDict()
    for z in konkordanz:
        nach_kanonisch.setdefault(z["kanonisch"].strip(), []).append(z)

    # (a) Datei <-> kanonisch
    a = []
    for name in dateien:
        if name not in nach_kanonisch:
            a.append(f"Katalogdatei ohne Zeile in {KONKORDANZ}: {name}.md")
    for name, zs in nach_kanonisch.items():
        stufen = {s.strip() for z in zs for s in z["stufe"].split("+")}
        if "II" in stufen and name not in texte:
            a.append(f"kanonisch mit Stufe II ohne Katalogdatei: {name}")
    aus["a"] = {"befunde": a, "dateien": len(dateien), "kanonisch": len(nach_kanonisch),
                "stufe2": sum(1 for zs in nach_kanonisch.values()
                              if "II" in {s.strip() for z in zs for s in z["stufe"].split("+")})}

    # (b) H1 gegen thema-Werte der eigenen Zeilen
    b, ohne, gleich = [], [], 0
    for name in dateien:
        m = H1.search(texte[name])
        h1 = m.group(1).strip() if m else None
        werte = [(z["profil"].strip(), z["thema"].strip()) for z in nach_kanonisch.get(name, []) if z["thema"].strip()]
        if h1 is None:
            b.append(f"{name}.md: keine H1-Überschrift")
            continue
        if not werte:
            ohne.append(f"{name}.md: H1 „{h1}“")
            continue
        passend = [p for p, w in werte if w == h1]
        abweichend = [(p, w) for p, w in werte if w != h1]
        if abweichend:
            b.append(f"{name}.md: H1 „{h1}“ – gleich: {', '.join(passend) if passend else '–'}; abweichend: "
                     + ", ".join(f"{p} „{w}“" for p, w in abweichend))
        else:
            gleich += 1
    aus["b"] = {"befunde": b, "ohne": ohne, "gleich": gleich}

    # (c) abi/iqb-Themen gegen Vokabular § 2 und die vier Geltungstabellen § 1
    abi_iqb = sorted({z["thema"].strip() for z in konkordanz if z["profil"].strip() in ("abi", "iqb")})
    listen = collections.OrderedDict()
    abbrueche = []
    try:
        listen["abitur-vokabular.md § 2"] = sorted(TP.vokabular_themen())
    except SystemExit as ex:  # vokabular_themen() beendet bei fehlendem Abschnitt das Programm
        abbrueche.append(str(ex))
    for rel in GELTUNG:
        werte, grund = themenspalte_tabelle(lies(os.path.join(HIER, rel)), rel)
        if grund:
            abbrueche.append(grund)
        else:
            listen[os.path.basename(rel) + " § 1"] = werte
    c = []
    for bezeichnung, werte in listen.items():
        menge = set(werte)
        doppelt = [w for w, k in collections.Counter(werte).items() if k > 1]
        if doppelt:
            c.append(f"{bezeichnung}: doppelt geführt: " + ", ".join(f"„{w}“" for w in doppelt))
        for w in abi_iqb:
            if w not in menge:
                c.append(f"abi/iqb-Thema fehlt in {bezeichnung}: „{w}“")
        for w in werte:
            if w not in abi_iqb:
                c.append(f"{bezeichnung} nennt ein Thema ohne abi/iqb-Zeile in {KONKORDANZ}: „{w}“")
    aus["c"] = {"befunde": c, "abbruch": abbrueche, "themen": len(abi_iqb),
                "listen": {k: len(v) for k, v in listen.items()}}

    # (d) msa/fhr-Themen gegen die Themenspalte des Typenkatalogs
    d = collections.OrderedDict()
    for profil, rel in TYPENKATALOGE.items():
        eigene = sorted({z["thema"].strip() for z in konkordanz if z["profil"].strip() == profil})
        werte, grund = themenspalte_csv(os.path.join(HIER, rel), rel)
        if grund:
            d[profil] = {"befunde": [], "abbruch": grund, "themen": len(eigene), "typen_themen": None}
            continue
        typen_themen = sorted(set(werte))
        befunde = []
        for w in eigene:
            if w not in typen_themen:
                befunde.append(f"{profil}-Thema aus {KONKORDANZ} fehlt in {rel}: „{w}“")
        for w in typen_themen:
            if w not in eigene:
                befunde.append(f"{rel} nennt ein Thema ohne {profil}-Zeile in {KONKORDANZ}: „{w}“")
        d[profil] = {"befunde": befunde, "abbruch": None, "themen": len(eigene), "typen_themen": len(typen_themen)}
    aus["d"] = d
    return aus


def pruefe_gegenrichtung(trag, texte):
    """Prüfung 4. paare: [(a, b)] – a nennt b unter Blatt 0, b nennt a.md nirgends; kanten: Zahl aller Blatt-0-Kanten."""
    erwaehnt = {b: {ziel for pfad, ziel in T.VERWEIS.findall(t) if pfad in ("", KATALOG_ORDNER + "/")}
                for b, t in texte.items()}
    paare, kanten = [], 0
    for a, ziele in trag["voraussetzungen"].items():
        for b in ziele:
            kanten += 1
            if a not in erwaehnt[b]:
                paare.append((a, b))
    return {"paare": paare, "kanten": kanten}


def pruefe_formluecke(trag, texte):
    """Prüfung 5. Je Eintrag ohne Verweis auf einen anderen Katalogeintrag in Blatt 0 (Lesart des Vorbilds):
    (name, nennungen, [(zeilennr, nennungen_in_zeile, zeile)]); dazu die Einträge, deren Blatt 0 nach der
    wörtlichen Lesart (überhaupt kein <name>.md) verweisfrei ist, zum Vergleich."""
    liste = []
    for name in sorted(trag["ohne_verweis"] + trag["ohne_abschnitt"]):
        text = texte[name]
        m = T.ABSCHNITT.search(text)
        if not m:
            liste.append((name, None, []))
            continue
        zitate = []
        for zeile, pos in zeilen(text, m.start(1), m.end(1)):
            k = len(T.WORTFORM.findall(zeile))
            if k:
                zitate.append((zeilennr(text, pos), k, zeile))
        liste.append((name, len(T.WORTFORM.findall(m.group(1))), zitate))
    woertlich = sorted(n for n, t in texte.items()
                       if T.blatt0(t) is not None and not T.VERWEIS.search(T.blatt0(t)))
    return {"liste": liste, "woertlich": woertlich}


def messe(wurzel=HIER):
    """Alle fünf Prüfungen; Listen sortiert, damit die Ausgabe deterministisch ist."""
    katalog = os.path.join(wurzel, KATALOG_ORDNER)
    namen = T.eintraege(katalog)
    texte = collections.OrderedDict((n, lies(os.path.join(katalog, n + ".md"))) for n in namen)
    vorhanden = set(namen)
    einheiten = {n: lerneinheiten(t) for n, t in texte.items()}
    konkordanz = TP.lies_csv(KONKORDANZ)
    trag = T.messe(katalog, os.path.join(wurzel, KONKORDANZ))
    return {
        "eintraege": namen,
        "einheiten": einheiten,
        "p1": {"funde": pruefe_verweise(texte, vorhanden)},
        "p2": pruefe_einheiten(texte, vorhanden, einheiten),
        "p3": pruefe_namen(texte, konkordanz),
        "p4": pruefe_gegenrichtung(trag, texte),
        "p5": pruefe_formluecke(trag, texte),
    }


# ---------------------------------------------------------------- Ausgabe

def gruppiert(funde):
    """verweis -> quelle -> Counter(abschnitt), Ziele und Quellen alphabetisch."""
    baum = collections.OrderedDict()
    for f in sorted(funde, key=lambda f: (f["verweis"], f["quelle"], f["zeile"])):
        baum.setdefault(f["verweis"], collections.OrderedDict()).setdefault(f["quelle"], collections.Counter())[f["abschnitt"]] += 1
    return baum


def abschnittsliste(zaehler):
    return ", ".join(f"{a}" + (f" ×{k}" if k > 1 else "") for a, k in zaehler.items())


def lage(ort):
    if ort is None:
        return "keine Datei dieses Namens im Repo"
    return "liegt in " + ", ".join("Wurzel" if o == "." else o + "/" for o in ort)


def zeilen_gruppe(funde):
    """Befundzeilen einer Verweisgruppe: eine je Ziel, darunter eine je Quelldatei mit Abschnitten."""
    aus = []
    for verweis, quellen in gruppiert(funde).items():
        n = sum(sum(c.values()) for c in quellen.values())
        ort = next(f["ort"] for f in funde if f["verweis"] == verweis)
        aus.append(f"- **{verweis}** ({lage(ort)}) – {n} {'Verweis' if n == 1 else 'Verweise'} aus {len(quellen)} "
                   f"{'Eintrag' if len(quellen) == 1 else 'Einträgen'}")
        for quelle, zaehler in quellen.items():
            aus.append(f"  - {quelle}.md ({abschnittsliste(zaehler)})")
    return aus


def zeilen_p1(m):
    funde = m["p1"]["funde"]
    je = collections.Counter(f["gruppe"] for f in funde)
    arten = collections.Counter(f["art"] for f in funde if f["gruppe"] == "a")
    ziele_b = len({f["verweis"] for f in funde if f["gruppe"] == "b"})
    ziele_c = len({f["verweis"] for f in funde if f["gruppe"] == "c"})
    kopf = (f"{len(funde)} Verweise in {len({f['quelle'] for f in funde})} Einträgen. Gruppe (a) Ziel in `katalog/`: "
            f"{je['a']} – davon {arten['eintrag']} auf andere Katalogeinträge, {arten['selbst']} Selbstverweise, "
            f"{arten['eintrag-pfad']} auf Katalogeinträge mit Pfadangabe, {arten['sonstige']} auf andere Dateien in "
            f"`katalog/` (`_*.md`, `index.md`). Gruppe (b) Ziel anderswo im Repo: {je['b']} Verweise auf {ziele_b} "
            f"Dateien. Gruppe (c) Ziel gibt es nicht: {je['c']} Verweise auf {ziele_c} Namen.")
    b = zeilen_gruppe([f for f in funde if f["gruppe"] == "b"]) or ["- keine"]
    c = zeilen_gruppe([f for f in funde if f["gruppe"] == "c"]) or ["- keine"]
    a_sonst = zeilen_gruppe([f for f in funde if f["gruppe"] == "a" and f["art"] == "sonstige"]) or ["- keine"]
    a_pfad = [f"- {f['verweis']} ← {f['quelle']}.md ({f['abschnitt']}, Zeile {f['zeile']})"
              for f in sorted(funde, key=lambda f: (f["verweis"], f["quelle"], f["zeile"]))
              if f["gruppe"] == "a" and f["art"] == "eintrag-pfad"] or ["- keine"]
    return kopf, b, c, a_sonst, a_pfad, je, ziele_b, ziele_c


def zeilen_p2(m):
    p2 = m["p2"]
    zu = p2["zugeordnet"]
    gross = [z for z in zu if z["zu_gross"]]
    unpruefbar = [z for z in zu if not z["pruefbar"]]
    def zeile_zu(z):
        soll = f"{z['vorhanden']} vorhanden" if z["pruefbar"] else "Ziel kein Katalogeintrag"
        return (f"- {z['quelle']}.md ({z['abschnitt']}, Zeile {z['zeile']}): „{z['verweis']} … {z['angabe']}“ – "
                f"{soll}; Zitat: {z['zitat']}")
    def zeile_un(u):
        return (f"- {u['quelle']}.md ({u['abschnitt']}, Zeile {u['zeile']}): {u['art']} – „{u['angabe']}“ bei "
                f"{' / '.join(u['kandidaten'])}; Zitat: {u['zitat']}")
    kopf = (f"{p2['gesamt']} Einheitenangaben in den Einträgen. Direkt hinter einem Verweis: {len(zu)} "
            f"({len(zu) - len(unpruefbar)} geprüft, {len(unpruefbar)} nicht prüfbar, weil das Ziel kein Katalogeintrag "
            f"ist); davon Nummer größer als vorhanden: {len(gross)}. Nicht eindeutig einem Verweis zuordenbar: "
            f"{len(p2['unklar'])}. Die übrigen {p2['gesamt'] - len(zu) - len(p2['unklar'])} stehen ohne Verweis "
            f"davor oder weiter von ihm entfernt; sie gelten als eigene Einheiten des Eintrags und sind nicht geprüft.")
    return kopf, [zeile_zu(z) for z in gross] or ["- keine"], [zeile_zu(z) for z in unpruefbar] or ["- keine"], \
        [zeile_un(u) for u in p2["unklar"]] or ["- keine"], gross, unpruefbar


def zeilen_p3(m):
    p3 = m["p3"]
    aus = collections.OrderedDict()
    a = p3["a"]
    aus["a"] = (f"(a) Datei ↔ kanonisch: {a['dateien']} Katalogdateien, {a['kanonisch']} kanonische Namen in "
                f"`{KONKORDANZ}`, davon {a['stufe2']} mit Stufe II. "
                + (f"{len(a['befunde'])} Abweichungen." if a["befunde"] else "Bestanden."), a["befunde"])
    b = p3["b"]
    aus["b"] = (f"(b) H1 gegen thema-Werte: {b['gleich']} Einträge mit H1 gleich allen thema-Werten, "
                f"{len(b['befunde'])} mit Abweichung, {len(b['ohne'])} ohne thema-Wert (kein Prüfungsthema).",
                b["befunde"], b["ohne"])
    c = p3["c"]
    listen = "; ".join(f"{k}: {v}" for k, v in c["listen"].items())
    aus["c"] = (f"(c) abi/iqb-Themen: {c['themen']} verschiedene thema-Werte der abi/iqb-Zeilen; Listen: {listen}. "
                + ("ABGEBROCHEN: " + " | ".join(c["abbruch"]) + ". " if c["abbruch"] else "")
                + (f"{len(c['befunde'])} Abweichungen." if c["befunde"] else "Bestanden."), c["befunde"])
    d_text, d_bef = [], []
    for profil, d in p3["d"].items():
        if d["abbruch"]:
            d_text.append(f"{profil}: ABGEBROCHEN – {d['abbruch']}")
        else:
            d_text.append(f"{profil}: {d['themen']} thema-Werte in `{KONKORDANZ}`, {d['typen_themen']} Themen in "
                          f"`{TYPENKATALOGE[profil]}`, " + (f"{len(d['befunde'])} Abweichungen" if d["befunde"] else "bestanden"))
            d_bef.extend(d["befunde"])
    aus["d"] = ("(d) msa/fhr-Themen gegen den Typenkatalog: " + "; ".join(d_text) + ".", d_bef)
    return aus


def zeilen_p4(m):
    p4 = m["p4"]
    je_b = collections.OrderedDict()
    for a, b in sorted(p4["paare"], key=lambda p: (p[1], p[0])):
        je_b.setdefault(b, []).append(a)
    kopf = (f"{p4['kanten']} Blatt-0-Verweise auf andere Katalogeinträge (Kanten A → B); {len(p4['paare'])} davon "
            f"ohne Gegenrichtung: B nennt A.md in keinem Abschnitt. Gruppiert nach B (dort stünde die Erwähnung), "
            f"{len(je_b)} Einträge B betroffen.")
    liste = [f"- **{b}** ({len(quellen)}): " + ", ".join(quellen) for b, quellen in je_b.items()] or ["- keine"]
    return kopf, liste, je_b


def baue(m, stand):
    """Text von _verweise.md."""
    n = len(m["eintraege"])
    out = []
    w = out.append
    w("# Verweise und Namen – Prüfung des Themenkatalogs")
    w(f"Stand {stand}.")
    w(f"Erzeugt von `werkzeuge/{VERSION.replace(' ', '` (')}) aus den Einträgen, `themen.csv`, "
      "`abitur/abitur-vokabular.md`, den vier `abitur/abi-*-geltung.md` und den Typenkatalogen `msa/msa-typen.csv` "
      "und `fhr/fhr-typen.csv`; abgeleitet, nie von Hand ändern. Fünf Prüfungen der inneren Stimmigkeit vor dem "
      "Umbau der Blatt-Prompte: Dateiverweise, Einheitennummern, Namensgleichheit, Gegenrichtung, Formlücke. "
      "Befunde werden berichtet, nicht behoben; wo eine Zuordnung nicht eindeutig ist, steht der Fall in einer "
      "eigenen Liste statt in einer Entscheidung.")
    w("")
    w(f"Gemessen: {n} Einträge (`katalog/*.md` ohne `_*` und `index.md`). Lesarten wie in "
      "`werkzeuge/tragfaehigkeit.py` (v0.1), importiert, nicht nachgebaut: Verweis = Zeichenkette der Form "
      "`<name>.md` (auch in Klammern oder Backticks; ein Pfad davor wird mitgenommen), Blatt-0-Abschnitt = "
      "„### Voraussetzungen (Blatt 0)“ bis zur nächsten Überschrift, Nennung in Wortform = „Thema “ vor einem "
      "Großbuchstaben (Heuristik), Fundort einer Datei außerhalb von `katalog/` = Suche im Repo nach dem Dateinamen. "
      "Abschnitt einer Fundstelle = die nächste Überschrift davor (#, ##, ###); in den Listen abgekürzt: Kopf "
      "(Titel und Statuszeilen), Verortung, Lerneinheiten, Typen (Typen je Lerneinheit), Blatt 0, Merkkasten, "
      "Fehler (Typische Fehler), Schwache (Für schwache Schüler), Prüfungsform, Offene Punkte, Prüfliste. "
      "Zeilennummern zählen ab 1 in der Datei. Zahl der Lerneinheiten eines Eintrags = Zeilen im Abschnitt "
      "„### Lerneinheiten“, die mit „<n>. “ beginnen.")
    w("")

    # ---- 1
    kopf, b, c, a_sonst, a_pfad, je, ziele_b, ziele_c = zeilen_p1(m)
    w("## 1 Dateiverweise")
    w("Jeder Verweis `<name>.md` in jedem Abschnitt jedes Eintrags, nicht nur in Blatt 0. Gruppe (a): das Ziel "
      "liegt in `katalog/` (Katalogeintrag, Selbstverweis, Katalogeintrag mit Pfadangabe oder eine andere Datei "
      "des Ordners); Gruppe (b): das Ziel liegt anderswo im Repo (ohne Pfadangabe über den Fundort, mit Pfadangabe "
      "über den Pfad relativ zur Wurzel); Gruppe (c): keine Datei dieses Namens im Repo. Gruppe (b) und (c) "
      "vollständig, je Ziel eine Zeile und darunter je Quelldatei die Abschnitte (×n = mehrfach im Abschnitt).")
    w("")
    w(kopf)
    w("")
    w("### Gruppe (b) – Ziel anderswo im Repo")
    out.extend(b)
    w("")
    w("### Gruppe (c) – Ziel gibt es nicht")
    out.extend(c)
    w("")
    w("### Gruppe (a), Sonderfälle")
    w("Verweise auf Dateien in `katalog/`, die kein Eintrag sind (zählen in `tragfaehigkeit.py` als Verweise auf "
      "Nicht-Katalogdateien):")
    out.extend(a_sonst)
    w("")
    w("Verweise auf Katalogeinträge mit Pfadangabe (`katalog/<name>.md`; zählen in `tragfaehigkeit.py` nicht als "
      "Katalogverweis, weil der Pfad mitgenommen wird):")
    out.extend(a_pfad)
    w("")

    # ---- 2
    kopf, gross, unpruefbar, unklar, _, _ = zeilen_p2(m)
    w("## 2 Einheitennummern")
    w("Eine Einheitenangabe ist „Einheit n“ oder „Einheiten n“ mit einer oder zwei Ziffern, fortgesetzt mit „und“, "
      "„bis“, „–“, Komma oder Schrägstrich („Einheit 6 und 8“, „Einheiten 2 bis 4“, „Einheit 2, 3 und 5“). Sie "
      "steht hinter einem Verweis, wenn zwischen `<name>.md` und „Einheit“ nur Leerraum, ein Komma oder eine "
      "öffnende Klammer steht („x.md Einheit 4“, „x.md, Einheit 4“, „x.md (Einheit 4)“); dann wird die größte "
      "genannte Nummer gegen die Zahl der Lerneinheiten der Zieldatei gehalten. Nicht eindeutig zuordenbar und "
      "deshalb nur gelistet: (1) der Verweis "
      "davor steht in einer Reihung („a.md und b.md Einheit 2“, „a.md, b.md Einheit 2“) – welcher gemeint ist, "
      f"steht nicht da; (2) zwischen Verweis und Angabe stehen bis zu {KURZ_WOERTER} Wörter ohne Satz- oder "
      "Klammerende („x.md, dessen Einheit 5“, „x.md (Sek I, Einheit 3)“) – hier kann auch eine eigene Einheit "
      "gemeint sein; (3) die Angabe steht vor dem Verweis mit „in“, „im“, „von“, „aus“, „der“, „des“ oder „bei“ "
      "dazwischen („Einheit 4 in x.md“). Alle anderen Einheitenangaben – ohne Verweis in der Zeile, hinter einem Satzende "
      "oder weiter entfernt – gelten als eigene Einheiten des Eintrags und werden nicht geprüft; Angaben an "
      "Nennungen in Wortform („Thema Terme, Einheit 2“) haben keinen Verweis, dem sie zugeordnet werden könnten "
      "(die in Blatt 0 stehen unter Prüfung 5).")
    w("")
    w(kopf)
    w("")
    w("### Nummer größer als vorhanden")
    out.extend(gross)
    w("")
    w("### Direkt hinter einem Verweis, aber nicht prüfbar")
    out.extend(unpruefbar)
    w("")
    w("### Nicht eindeutig einem Verweis zuordenbar")
    out.extend(unklar)
    w("")
    w("Zahl der Lerneinheiten je Eintrag (Zeilen „<n>. “ im Abschnitt „### Lerneinheiten“): "
      + ", ".join(f"{name} {m['einheiten'][name] if m['einheiten'][name] is not None else '– (kein Abschnitt)'}"
                  for name in m["eintraege"]) + ".")
    w("")

    # ---- 3
    p3 = zeilen_p3(m)
    w("## 3 Namensgleichheit")
    w("Vier Abgleiche, jeder in beide Richtungen. (a) Jede `katalog/<x>.md` hat eine Zeile in `themen.csv` mit "
      "`kanonisch` = x; jeder kanonische Name mit `stufe` II (auch „I+II“) hat eine Katalogdatei. (b) Die "
      "H1-Überschrift jedes Eintrags gegen die `thema`-Werte seiner Zeilen (Zeilen mit leerem Thema zählen nicht); "
      "Abweichungen werden gemeldet, nicht bewertet – ein Eintrag kann mehrere Prüfungsthemen tragen. (c) Die "
      "`thema`-Werte der Zeilen mit `profil` abi oder iqb gegen die Themenliste in `abitur-vokabular.md` § 2 "
      "(Lesart von `themen-pruef.py`) und gegen die Spalte „Thema“ der Tabelle in § 1 jeder der vier "
      "`abi-*-geltung.md`. (d) Die `thema`-Werte der Zeilen mit `profil` msa gegen die Spalte `thema` von "
      "`msa/msa-typen.csv`, fhr gegen `fhr/fhr-typen.csv`. Ist eine Themenspalte über die Kopfzeile nicht eindeutig "
      "(kein oder mehr als ein Treffer), wird die Teilprüfung abgebrochen und der Grund genannt.")
    w("")
    w(p3["a"][0])
    out.extend(f"- {x}" for x in p3["a"][1])
    w("")
    w(p3["b"][0])
    out.extend(f"- {x}" for x in p3["b"][1])
    if p3["b"][2]:
        w("")
        w("Ohne `thema`-Wert in `themen.csv` (kein Prüfungsthema; H1 zum Nachlesen):")
        out.extend(f"- {x}" for x in p3["b"][2])
    w("")
    w(p3["c"][0])
    out.extend(f"- {x}" for x in p3["c"][1])
    w("")
    w(p3["d"][0])
    out.extend(f"- {x}" for x in p3["d"][1])
    w("")

    # ---- 4
    kopf, liste, _ = zeilen_p4(m)
    w("## 4 Gegenrichtung")
    w("Nennt Eintrag A unter „Voraussetzungen (Blatt 0)“ den Eintrag B (Kante wie in `tragfaehigkeit.py`: "
      "Verweis `<B>.md` ohne Pfad, kein Selbstverweis), wird geprüft, ob B irgendwo in seinem Text `<A>.md` nennt "
      "(auch als `katalog/<A>.md`; Nennungen in Wortform zählen nicht). Fehlt das, ist (A, B) ein Paar. Nur "
      "aufgelistet, nicht bewertet.")
    w("")
    w(kopf)
    out.extend(liste)
    w("")

    # ---- 5
    p5 = m["p5"]
    w("## 5 Formlücke")
    w("Einträge, deren Blatt-0-Abschnitt keinen Verweis auf einen anderen Katalogeintrag enthält – dieselbe "
      "Menge wie „Einträge ohne Verweis“ in den Messlücken von `_tragfaehigkeit.md` (Lesart des Vorbilds: Verweise "
      "auf Nicht-Katalogdateien und Selbstverweise zählen nicht). Je Eintrag die Zahl der Nennungen in Wortform "
      "(Heuristik „Thema “ vor einem Großbuchstaben) und jede Zeile des Abschnitts, die eine trägt, als wörtliches "
      "Zitat mit Zeilennummer; steht eine Zeile für mehrere Nennungen, ist ihre Zahl vermerkt.")
    w("")
    gleich = p5["woertlich"] == [name for name, _, _ in p5["liste"]]
    w(f"{len(p5['liste'])} von {n} Einträgen. Wörtliche Lesart (überhaupt kein `<name>.md` im Abschnitt): "
      + ("dieselbe Menge." if gleich else f"abweichend – {', '.join(p5['woertlich']) or 'keiner'}."))
    for name, k, zitate in p5["liste"]:
        if k is None:
            w(f"- **{name}** – kein Abschnitt „### Voraussetzungen (Blatt 0)“")
            continue
        w(f"- **{name}** – {k} {'Nennung' if k == 1 else 'Nennungen'} in Wortform"
          + (f" in {len(zitate)} {'Zeile' if len(zitate) == 1 else 'Zeilen'}:" if zitate else ""))
        for nr, kz, zeile in zitate:
            w(f"  - Zeile {nr}" + (f" ({kz} Nennungen)" if kz > 1 else "") + ":")
            w(f"    > {zeile}")
    w("")

    # ---- Schwäche
    w("## Schwäche der Messung")
    w("Die Prüfungen sehen Zeichenketten, keine Bedeutung. Prüfung 1 findet nur die Form `<name>.md`; ein Thema, das "
      "in Wortform genannt ist („Thema Lineare Gleichungen“), hat weder Ziel noch Fundort und fehlt in allen "
      "Gruppen – Prüfung 5 zeigt, wie viele Einträge so schreiben. Prüfung 2 ordnet nur zu, was unmittelbar hinter "
      "einem Verweis steht; die Nennungen in Wortform tragen ihre Einheitsnummern ungeprüft, und eine Angabe, die "
      "einen Satz weiter steht, gilt als eigene Einheit, auch wenn die Zieldatei gemeint war. Die Zahl der "
      "Lerneinheiten ist die Zahl der nummerierten Zeilen, nicht die höchste Nummer; der Verweiseintrag hat null. "
      "Prüfung 3 vergleicht Namen wortgleich – eine abweichende H1 kann Absicht sein (Sammelthema, mehrere "
      "Prüfungsthemen), eine gleiche H1 sagt nichts über den Inhalt. Prüfung 4 zählt eine Erwähnung in jedem "
      "Abschnitt gleich, auch eine in der Prüfliste oder in einem offenen Punkt; ob die Gegenrichtung fachlich "
      "nötig ist, entscheidet sie nicht. Prüfung 5 zählt mit der Heuristik des Vorbilds; sie übersieht Nennungen "
      "ohne das Wort „Thema“ und zählt das Wort auch, wo es kein Verweis ist. Alle fünf messen die Schreibform der "
      "Einträge, nicht den Unterricht.")
    w("")
    return "\n".join(out)


def kurz(zeilen_liste, n=STDOUT_ZEILEN):
    """Höchstens n Zeilen für stdout, der Rest als Hinweis auf die Datei."""
    if len(zeilen_liste) <= n:
        return zeilen_liste
    return zeilen_liste[:n] + [f"  … {len(zeilen_liste) - n} weitere in {KATALOG_ORDNER}/{AUSGABE}"]


def main():
    m = messe()
    stand = f"{datetime.date.today().isoformat()}, Katalog auf Commit {T.head_kurz()}"
    text = baue(m, stand)
    pfad = os.path.join(HIER, KATALOG_ORDNER, AUSGABE)
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    n = len(m["eintraege"])
    print(f"{VERSION}: {n} Einträge geprüft; {KATALOG_ORDNER}/{AUSGABE} geschrieben ({text.count(chr(10))} Zeilen).")

    kopf, b, c, a_sonst, a_pfad, je, ziele_b, ziele_c = zeilen_p1(m)
    funde = m["p1"]["funde"]
    print(f"Prüfung 1 Dateiverweise: {len(funde)} Verweise – (a) {je['a']} in katalog/, (b) {je['b']} anderswo im Repo "
          f"({ziele_b} Dateien), (c) {je['c']} ohne Datei ({ziele_c} Namen)")
    zielzeilen = []
    for gruppe in ("c", "b"):  # (c) alphabetisch, (b) nach Zahl der Verweise absteigend – die Datei listet alles alphabetisch
        reihen = []
        for verweis, quellen in gruppiert([f for f in funde if f["gruppe"] == gruppe]).items():
            k = sum(sum(z.values()) for z in quellen.values())
            ort = next(f["ort"] for f in funde if f["verweis"] == verweis)
            reihen.append((k, verweis, f"  ({gruppe}) {verweis} – {lage(ort)}; {k}× aus {', '.join(quellen)}"))
        if gruppe == "b":
            reihen.sort(key=lambda r: (-r[0], r[1]))
        zielzeilen.extend(r[2] for r in reihen)
    for z in kurz(zielzeilen):
        print(z)

    kopf, gross, unpruefbar, unklar, gross_l, unpr_l = zeilen_p2(m)
    p2 = m["p2"]
    print(f"Prüfung 2 Einheitennummern: {len(p2['zugeordnet'])} Angaben direkt hinter einem Verweis "
          f"({len(gross_l)} größer als vorhanden, {len(unpr_l)} nicht prüfbar), {len(p2['unklar'])} nicht eindeutig "
          f"zuordenbar, {p2['gesamt']} Einheitenangaben insgesamt")
    for z in kurz([("  größer: " + z[2:]) for z in gross if z != "- keine"]
                  + [("  unklar: " + z[2:]) for z in unklar if z != "- keine"]):
        print(z)

    p3 = zeilen_p3(m)
    p3_zeilen = []
    for schluessel in ("a", "b", "c", "d"):
        p3_zeilen.append("  " + p3[schluessel][0])
        p3_zeilen.extend("    - " + x for x in p3[schluessel][1])
    print(f"Prüfung 3 Namensgleichheit: {sum(len(p3[s][1]) for s in 'abcd')} Abweichungen in vier Abgleichen"
          + (" (Teilprüfung abgebrochen, siehe unten)" if m["p3"]["c"]["abbruch"]
             or any(d["abbruch"] for d in m["p3"]["d"].values()) else ""))
    for z in kurz(p3_zeilen):
        print(z)

    kopf, liste, je_b = zeilen_p4(m)
    print(f"Prüfung 4 Gegenrichtung: {len(m['p4']['paare'])} Paare ohne Gegenrichtung von {m['p4']['kanten']} "
          f"Blatt-0-Kanten, {len(je_b)} Einträge B betroffen")
    for z in kurz(["  " + z[2:] for z in liste if z != "- keine"]):
        print(z)

    p5 = m["p5"]
    print(f"Prüfung 5 Formlücke: {len(p5['liste'])} von {n} Einträgen ohne Verweis in Blatt 0"
          + ("" if p5["woertlich"] == [x[0] for x in p5["liste"]] else " (wörtliche Lesart weicht ab, siehe Datei)"))
    for z in kurz([f"  {name} ({k} {'Nennung' if k == 1 else 'Nennungen'} in Wortform)" if k is not None
                   else f"  {name} (kein Abschnitt)" for name, k, _ in p5["liste"]]):
        print(z)
    return 0


if __name__ == "__main__":
    sys.exit(main())
