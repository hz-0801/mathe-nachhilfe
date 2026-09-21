# -*- coding: utf-8 -*-
"""
blatt0-belege.py v0.1 · 21.09.2026 · Belege der Blatt-0-Fertigkeiten ohne Ziel

Nach dem Auftrag „Blatt 0: Dateiverweise nachgetragen“ (Commit cfa4723) tragen 112
Fertigkeitszeilen der Sek-I-Einträge unter „### Voraussetzungen (Blatt 0)“ einen
Dateiverweis, 35 tragen keinen – nicht, weil der Verweis fehlt, sondern weil offen
ist, ob es zu der Fertigkeit überhaupt ein Katalogthema gibt („Vielfache und Teiler“,
„Vierecksarten kennen“). Jede dieser Zeilen trägt aber eine Quellenklammer. Dieses
Werkzeug löst die Klammern gegen die Register auf, die im Repo liegen, und legt das
Ergebnis als Vorschlagsliste vor (Auftrag Belege der Blatt-0-Fertigkeiten ohne Ziel,
21.09.2026). Es ändert keinen Eintrag und entscheidet nichts.

Lesarten aus werkzeuge/tragfaehigkeit.py (v0.1), importiert, nicht nachgebaut: die
Liste der Einträge (katalog/*.md ohne _* und index.md), der Abschnitt „### Voraus-
setzungen (Blatt 0)“ bis zur nächsten Überschrift (ABSCHNITT), die Verweisform
<name>.md (VERWEIS) und der kurze HEAD-Hash (head_kurz). Die Konkordanz themen.csv
liest lies_csv() von themen-pruef.py.

Eigene Lesarten (hier festgelegt, in _blatt0-belege.md als Messweise wiederholt):
  Fertigkeitszeile – Zeile des Blatt-0-Abschnitts, die mit „- “ beginnt und VOR der
                     Zwischenzeile „Erkennungsschritte…“ steht (Zeilenanfang); die
                     Erkennungsschritte gehören dem Thema selbst und bleiben außen vor.
                     Ein Eintrag ohne diese Zwischenzeile (der Verweiseintrag) hat den
                     ganzen Abschnitt als Fertigkeitenteil.
  Ziel             – ein Verweis <name>.md ohne Pfad auf einen anderen vorhandenen
                     Katalogeintrag, irgendwo in der Zeile (auch in der Klammer).
                     Selbstverweise zählen nicht (wie in tragfaehigkeit.py).
  Klammer          – die letzte eckige Klammer der Zeile; steht sie nicht am Zeilenende,
                     wird das vermerkt. Ohne Klammer: Sorte „keine Klammer“.
  Bestandteile     – die Klammer wird an „;“ und „,“ zerlegt, nicht innerhalb von „…“
                     und nicht innerhalb runder Klammern. Ein Teil, der mit einer
                     P10-Aufgabenkennung beginnt (2018-OS-K6d), setzt den vorigen Teil
                     fort (Kennungsliste); ein Teil, der nur aus einem MSK-Code besteht,
                     setzt einen vorigen MSK-Teil fort („MSK D, DB“).
  Sechs Sorten     – P10-Typ (Text enthält „P10“ und einen Typnamen in „…“ oder eine
                     Aufgabenkennung), LS-AA-Kapitel („LS-AA Kl. 8 II 1“, auch ohne
                     Lerneinheit oder mit Bereich „2–3“), RLP mit Zitat („RLP D „…““),
                     RLP ohne Zitat („RLP D“, „RLP D/E“, auch mit Zusatz ohne Anführungs-
                     zeichen), MSK-Code („MSK B2B“), sonstiges oder keine Klammer.

Register und Auflösung (soweit ein Register es hergibt; alles andere bleibt offen):
  P10-Typ          – msa/msa-typen.csv: Typname in „…“ gegen die Spalte typ, Kennung
                     gegen beispiel_id; je Treffer Thema (und über themen.csv, profil
                     msa, das kanonische Thema). Kennungen zusätzlich gegen die id-
                     Spalte von msa/msa-katalog-basis.csv und msa-katalog-kontext.csv
                     (thema, typ, typ_neben der Katalogzeile), weil msa-typen.csv je Typ
                     nur eine beispiel_id führt. Sind typ- oder thema-Spalte über die
                     Kopfzeile nicht eindeutig, fällt die Sorte aus und es wird gemeldet.
  LS-AA-Kapitel    – quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt, Teil 1
                     (Gliederung je Klasse: Kapitel mit Lerneinheiten, zweispaltig):
                     Kapiteltitel und Titel der Lerneinheit; Teil 2 (RLP-Inhalte mit
                     „Zu finden in Studyly“): die RLP-Blöcke (Niveaustufe, Jahrgang,
                     Themenbereich, Bereich), unter denen das Kapitel mit dieser
                     Lerneinheit genannt ist.
  RLP mit Zitat    – quellen/quelle-rlp-teil-c-mathematik-2023.txt: das Zitat wird in
                     den Spalten der Tabellen gesucht (der Text ist mehrspaltig gesetzt;
                     ein Block sind die Zeilen zwischen zwei Leerzeilen, darin wird jede
                     Zelle an die Zelle der Zeile davor gehängt, mit der sie sich am
                     weitesten überlappt, je Zelle höchstens eine Fortsetzung; Silben-
                     trennung am Zeilenende wird zusammengezogen; „…“ im Zitat erlaubt
                     eine Lücke; zuerst genau, dann ohne Groß-/Kleinschreibung).
                     Fundstelle: Zeilen des Treffers, Block, Niveaustufenbuchstabe(n)
                     am Block, Seitenkopf „Themenbereich … – Niveaustufen …“. Steht das
                     Zitat nicht im Text, wird der längste Wortanfang (mindestens drei
                     Wörter und die Hälfte) als Teiltreffer genannt, ohne als Auflösung
                     zu zählen.
  RLP ohne Zitat, MSK-Code, sonstiges – nicht aufgelöst. Beim MSK-Code wird der
                     Bausteintitel aus katalog/_quellen.md (Registerzeile [MSK])
                     beigelegt, soweit er dort genannt ist.
  themen.csv       – je Zeile ohne Ziel: welche kanonischen Namen der Wortlaut der
                     Zeile ohne ihre Quellenklammer wörtlich nennt – der Name selbst
                     (Bindestrich als Leerzeichen, Groß-/Kleinschreibung frei), ein
                     thema-Wert seiner Zeilen in themen.csv oder die H1-Überschrift
                     seiner Katalogdatei, jeweils als ganzes Wort und mit dem Umfeld des
                     Treffers; der eigene Eintrag zählt nicht. Keine Ähnlichkeitssuche.

Gegenprobe (Auftrag): in den 22 Sek-I-Einträgen des Auftrags Blatt-0-Dateiverweise
147 Fertigkeitszeilen, 112 mit Ziel, 35 ohne. Weicht eine Zahl ab, ist die
Abschnitts- oder Zeilenerkennung falsch – das Skript bricht dann ab und schreibt
nichts. Für die übrigen 51 Einträge wird gezählt und berichtet, nicht geprüft.

Schreibt katalog/_blatt0-belege.md (Kopf mit Stand, Commit, Skript, Messweise;
Teil 1 die 22 Sek-I-Einträge des Auftrags, Teil 2 die übrigen; je Eintrag die Zeilen
ohne Ziel mit Zeilennummer, Wortlaut, Klammer, Bestandteilen, Sorte, Auflösung und
themen.csv-Treffern; am Ende die Schwäche der Messung) und eine Kurzfassung auf
stdout. Zwei Läufe hintereinander erzeugen dieselbe Datei bis auf die Stand-Zeile.
_pruef_struktur.py importiert zaehle() für Kennzahl 9 (Fertigkeitszeilen ohne Ziel).

Aufruf aus der Repo-Wurzel (nach jeder Änderung an einem Blatt-0-Abschnitt):
  python werkzeuge/blatt0-belege.py            – schreibt die Datei
  python werkzeuge/blatt0-belege.py --debug    – gibt zusätzlich die Registerlesung aus
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
VERSION = "blatt0-belege.py v0.1"
KATALOG_ORDNER = "katalog"
KONKORDANZ = "themen.csv"
MSA_TYPEN = "msa/msa-typen.csv"
MSA_KATALOGE = ["msa/msa-katalog-basis.csv", "msa/msa-katalog-kontext.csv"]
LSAA_QUELLE = "quellen/quelle-klett-fahrplan-ls-aa-berlin-2024.txt"
RLP_QUELLE = "quellen/quelle-rlp-teil-c-mathematik-2023.txt"
QUELLENREGISTER = "katalog/_quellen.md"
AUSGABE = "_blatt0-belege.md"  # in katalog/

if WERKZEUGE not in sys.path:
    sys.path.insert(0, WERKZEUGE)
import tragfaehigkeit as T  # noqa: E402  (Vorbild: eintraege, ABSCHNITT, VERWEIS, head_kurz)


def lade_modul(dateiname, name):
    """Modul aus einer Datei laden, deren Name kein Python-Bezeichner ist (themen-pruef.py)."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(WERKZEUGE, dateiname))
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


TP = lade_modul("themen-pruef.py", "themen_pruef")  # lies_csv()

# Die 22 Sek-I-Einträge des Auftrags „Blatt 0: Dateiverweise nachgetragen“ (21.09.2026): die 21 Dateien aus
# archiv/ersetzungen-blatt0-2026-09-21.txt und terme.md – dieselbe Menge wie _verweise.md § 5 (Formlücke) auf
# Commit c05e6f0, die einzigen Einträge, deren Blatt 0 damals keinen Dateiverweis trug. Der Auftrag Belege
# nennt sie „die 22 Sek-I-Einträge“ und gibt für sie die Gegenprobe 147/112/35. Sieben weitere Einträge tragen
# in der Statuszeile Stufe Sek I oder Sek I + II (potenzen-wurzeln, reelle-zahlen, trigonometrische-funktionen,
# zinsrechnung; daten, einheiten, lineare-gleichungssysteme); sie stehen am Anfang von Teil 2.
SEK1_AUFTRAG = ["binomische-formeln", "bruchrechnung", "brueche-dezimalzahlen", "flaechen", "koerper", "kreis",
                "lineare-funktionen", "lineare-gleichungen", "potenz-exponentialfunktionen", "prozentrechnung",
                "pyramide-kegel-kugel", "pythagoras", "quadratische-funktionen", "quadratische-gleichungen",
                "rationale-zahlen", "strahlensaetze", "symmetrie-abbildungen", "terme", "trigonometrie",
                "wahrscheinlichkeit", "winkel-dreiecke", "zuordnungen"]
GEGENPROBE = (147, 112, 35)  # Fertigkeitszeilen, mit Ziel, ohne Ziel in den 22 Einträgen (Auftrag)

ERKENNUNG = re.compile(r"^Erkennungsschritte")            # die Zwischenzeile, ab der die Fertigkeiten enden
FERTIGKEIT = "- "                                           # Zeilenanfang einer Fertigkeitszeile
KLAMMER_ENDE = re.compile(r"\[([^\[\]]*)\]\s*$")            # eckige Klammer am Zeilenende
KLAMMER = re.compile(r"\[([^\[\]]*)\]")                     # irgendeine eckige Klammer
KENNUNG = re.compile(r"\b(20\d\d-(?:OS|FOR)-[BK]\d+[a-z]?)\b")  # P10-Aufgabenkennung (msa.md § 4)
ZITAT = re.compile(r"„([^“]+)“")
LSAA = re.compile(r"LS-AA Kl\. (\d+) ([IVX]+)(?:\s+(\d+)(?:\s*[–-]\s*(\d+))?)?")
RLP = re.compile(r"^RLP\s+([A-H](?:\s*[/–-]\s*[A-H])*)(?![\w])")
MSK = re.compile(r"^MSK\s+([A-Z]{1,2}\d{0,2}[A-Z]?)(?![\w])")
MSK_CODE_ALLEIN = re.compile(r"^[A-Z]{1,2}\d{0,2}[A-Z]?$")
STUFE = re.compile(r"Stufe: ([^·\n]+?)\s*(?:·|$)", re.M)
H1 = re.compile(r"^# (.+?)[ \t]*$", re.M)
SORTEN = ["P10-Typ", "LS-AA-Kapitel", "RLP mit Zitat", "RLP ohne Zitat", "MSK-Code", "sonstiges oder keine Klammer"]
WORT = r"[^\W\d_]"


# ---------------------------------------------------------------- Hilfen

def lies(pfad):
    with io.open(pfad, encoding="utf-8") as fh:
        return fh.read()


def zellen(zeile, mindestluecke=2):
    """[(start, ende, text)] – die Zellen einer Zeile eines mehrspaltigen Textes: Textstücke, die durch
    mindestens `mindestluecke` Leerzeichen getrennt sind."""
    aus = []
    for m in re.finditer(r"\S+(?: {1,%d}\S+)*" % (mindestluecke - 1), zeile):
        aus.append((m.start(), m.end(), m.group(0)))
    return aus


def haenge_an(text, stueck):
    """Zwei Zeilen einer Spalte verketten; Silbentrennung („Grund-“ + „rechen…“) zusammenziehen."""
    if text.endswith("-") and stueck[:1].islower():
        return text[:-1] + stueck
    return text + " " + stueck


# ---------------------------------------------------------------- Zeilen sammeln

def fertigkeitszeilen(text):
    """[(zeilennr, zeile)] der Fertigkeitszeilen des Blatt-0-Abschnitts; dazu, ob die Zwischenzeile da ist.
    None, wenn der Eintrag den Abschnitt nicht hat."""
    m = T.ABSCHNITT.search(text)
    if not m:
        return None, False
    start = text.count("\n", 0, m.start(1)) + 1
    aus, zwischenzeile = [], False
    for i, z in enumerate(m.group(1).split("\n")):
        if ERKENNUNG.match(z):
            zwischenzeile = True
            break
        if z.startswith(FERTIGKEIT):
            aus.append((start + i, z))
    return aus, zwischenzeile


def ziele(zeile, name, vorhanden):
    """Sortierte Ziele einer Zeile: Verweise <name>.md ohne Pfad auf andere vorhandene Katalogeinträge."""
    return sorted({ziel for pfad, ziel in T.VERWEIS.findall(zeile) if not pfad and ziel in vorhanden and ziel != name})


def klammer(zeile):
    """(inhalt, am_ende) – die letzte eckige Klammer der Zeile; (None, None) ohne Klammer."""
    m = KLAMMER_ENDE.search(zeile)
    if m:
        return m.group(1), True
    alle = list(KLAMMER.finditer(zeile))
    if alle:
        return alle[-1].group(1), False
    return None, None


def zerlege(inhalt):
    """Bestandteile einer Klammer: getrennt an „;“ und „,“ außerhalb von „…“ und runden Klammern; Teile, die
    mit einer Aufgabenkennung beginnen, setzen den vorigen Teil fort; ein bloßer MSK-Code setzt einen
    MSK-Teil fort."""
    teile, akt, tiefe, zitat, trenner = [], [], 0, False, ""
    for ch in inhalt:
        if ch == "„":
            zitat = True
        elif ch == "“":
            zitat = False
        elif ch == "(" and not zitat:
            tiefe += 1
        elif ch == ")" and not zitat:
            tiefe = max(0, tiefe - 1)
        if ch in ";," and not zitat and tiefe == 0:
            teile.append((trenner, "".join(akt).strip()))
            akt, trenner = [], ch + " "
        else:
            akt.append(ch)
    teile.append((trenner, "".join(akt).strip()))
    aus = []
    for trenner, t in teile:
        if not t:
            continue
        if aus and (KENNUNG.match(t) or (MSK_CODE_ALLEIN.match(t) and MSK.match(aus[-1]))):
            aus[-1] = aus[-1] + trenner + t
        else:
            aus.append(t)
    return aus


def sorte(teil):
    """Eine der sechs Sorten für einen Bestandteil."""
    if "P10" in teil and (ZITAT.search(teil) or KENNUNG.search(teil)):
        return SORTEN[0]
    if LSAA.search(teil):
        return SORTEN[1]
    if RLP.match(teil):
        return SORTEN[2] if ZITAT.search(teil) else SORTEN[3]
    if MSK.match(teil):
        return SORTEN[4]
    return SORTEN[5]


# ---------------------------------------------------------------- Register: msa-typen.csv, msa-Kataloge, themen.csv

def lade_msa_typen(pfad):
    """(typen, beispiel, grund) – typ -> Zeile, beispiel_id -> typ; grund, wenn typ/thema nicht eindeutig sind."""
    if not os.path.exists(pfad):
        return None, None, f"{MSA_TYPEN} fehlt"
    with io.open(pfad, encoding="utf-8-sig", newline="") as fh:
        leser = csv.reader(fh, delimiter=";")
        kopf = next(leser, None)
        if kopf is None:
            return None, None, f"{MSA_TYPEN}: leer"
        for spalte in ("typ", "thema"):
            if kopf.count(spalte) != 1:
                return None, None, (f"{MSA_TYPEN}: Kopfzeile {kopf} nennt „{spalte}“ {kopf.count(spalte)}-mal – "
                                    "Spalte nicht eindeutig; Sorte P10-Typ ausgelassen")
        i_typ, i_thema = kopf.index("typ"), kopf.index("thema")
        i_bsp = kopf.index("beispiel_id") if kopf.count("beispiel_id") == 1 else None
        i_lid = kopf.index("leitidee") if kopf.count("leitidee") == 1 else None
        typen, beispiel = collections.OrderedDict(), {}
        for z in leser:
            if len(z) <= max(i_typ, i_thema):
                continue
            eintrag = {"typ": z[i_typ].strip(), "thema": z[i_thema].strip(),
                       "leitidee": z[i_lid].strip() if i_lid is not None and len(z) > i_lid else "",
                       "beispiel_id": z[i_bsp].strip() if i_bsp is not None and len(z) > i_bsp else ""}
            typen[eintrag["typ"]] = eintrag
            if eintrag["beispiel_id"]:
                beispiel.setdefault(eintrag["beispiel_id"], []).append(eintrag["typ"])
    return typen, beispiel, None


def lade_msa_kataloge(pfade):
    """id -> (datei, thema, typ, typ_neben) aus den msa-Katalogen; Dateien ohne eindeutige Spalten werden gemeldet."""
    zeilen, meldungen = {}, []
    for rel in pfade:
        pfad = os.path.join(HIER, rel)
        if not os.path.exists(pfad):
            meldungen.append(f"{rel} fehlt")
            continue
        with io.open(pfad, encoding="utf-8-sig", newline="") as fh:
            leser = csv.reader(fh, delimiter=";")
            kopf = next(leser, None) or []
            if any(kopf.count(s) != 1 for s in ("id", "thema", "typ")):
                meldungen.append(f"{rel}: Spalten id/thema/typ nicht eindeutig – nicht benutzt")
                continue
            i_id, i_th, i_ty = kopf.index("id"), kopf.index("thema"), kopf.index("typ")
            i_tn = kopf.index("typ_neben") if kopf.count("typ_neben") == 1 else None
            for z in leser:
                if len(z) <= max(i_id, i_th, i_ty):
                    continue
                zeilen[z[i_id].strip()] = (os.path.basename(rel), z[i_th].strip(), z[i_ty].strip(),
                                           z[i_tn].strip() if i_tn is not None and len(z) > i_tn else "")
    return zeilen, meldungen


def lade_konkordanz():
    """(nach_kanonisch, msa_thema_nach_kanonisch): kanonisch -> Zeilen; msa-thema -> [kanonisch]."""
    zeilen = TP.lies_csv(KONKORDANZ)
    nach_kanonisch, msa = collections.OrderedDict(), collections.OrderedDict()
    for z in zeilen:
        k = z["kanonisch"].strip()
        nach_kanonisch.setdefault(k, []).append(z)
        if z["profil"].strip() == "msa" and z["thema"].strip():
            msa.setdefault(z["thema"].strip(), [])
            if k not in msa[z["thema"].strip()]:
                msa[z["thema"].strip()].append(k)
    return nach_kanonisch, msa


# ---------------------------------------------------------------- Register: LS-AA-Fahrplan

LSAA_SEITENKOPF = ("Fahrplan Studyly", "auf der Grundlage des Rahmenlehrplans", "sowie des Rahmenlehrplans",
                   "Ernst Klett Verlag")
LSAA_KLASSE = re.compile(r"^(Klasse \d+|Einführungsphase|Qualifikationsphase)$")
LSAA_KAPITEL = re.compile(r"^Kapitel ([IVX]+)$")
LSAA_EINHEIT = re.compile(r"^(\d+) (.+)$")
LSAA_TEIL2 = re.compile(r"^\s*Klasse\s+Inhalte\s")
LSAA_NENNUNG = re.compile(r"^(Klasse \d+|Einführungsphase|Qualifikationsphase) Kapitel ([IVX]+)\s*(.*)$")
LSAA_STUFE = re.compile(r"^[A-H](?:/[A-H])?$")
LSAA_JAHRGANG = re.compile(r"^\d{1,2}(?:/\d{1,2})?$")
LSAA_SPALTE = 100  # Zellen ab dieser Spalte gehören zur rechten Spalte (Teil 1: Kapitel IV ff.; Teil 2: „Zu finden in“)


def lade_lsaa(pfad):
    """Fahrplan lesen. gliederung: (klasse, kapitel) -> {"titel", "einheiten": OrderedDict(nr -> titel)};
    zuordnung: [(blockkopf, (klasse, kapitel), [nummern])] aus Teil 2; None, None, grund ohne Datei."""
    if not os.path.exists(pfad):
        return None, None, f"{LSAA_QUELLE} fehlt"
    zeilen = lies(pfad).split("\n")
    teil2_ab = next((i for i, z in enumerate(zeilen) if LSAA_TEIL2.match(z)), len(zeilen))
    gliederung = collections.OrderedDict()
    # Teil 1: je Klassenseite zwei Spalten; jede Spalte in Zeilenfolge lesen.
    klasse, spalten = None, {"links": [], "rechts": []}

    def schliesse_seite():
        for seite in ("links", "rechts"):
            kapitel, letzte = None, None
            for text in spalten[seite]:
                if isinstance(text, tuple):  # (Kapitel-Zelle, Titel)
                    kapitel = (klasse, LSAA_KAPITEL.match(text[0]).group(1))
                    gliederung[kapitel] = {"titel": text[1], "einheiten": collections.OrderedDict()}
                    letzte = None
                    continue
                me = LSAA_EINHEIT.match(text)
                if me and kapitel:
                    letzte = int(me.group(1))
                    gliederung[kapitel]["einheiten"][letzte] = me.group(2)
                elif kapitel and letzte is not None:
                    gliederung[kapitel]["einheiten"][letzte] = haenge_an(gliederung[kapitel]["einheiten"][letzte], text)
        spalten["links"], spalten["rechts"] = [], []

    for z in zeilen[:teil2_ab]:
        if not z.strip() or any(k in z for k in LSAA_SEITENKOPF):
            continue
        zl = zellen(z)
        if zl and zl[0][0] == 0 and LSAA_KLASSE.match(zl[0][2]):
            schliesse_seite()
            klasse = zl[0][2]
            zl = zl[1:]
        if klasse is None:
            continue
        i = 0
        while i < len(zl):
            start, ende, text = zl[i]
            seite = "links" if start < LSAA_SPALTE else "rechts"
            if LSAA_KAPITEL.match(text) and i + 1 < len(zl) and zl[i + 1][0] - ende <= 30:
                spalten[seite].append((text, zl[i + 1][2]))
                i += 2
                continue
            spalten[seite].append(text)
            i += 1
    schliesse_seite()

    # Teil 2: links RLP-Blöcke (Stufe/Themenbereich, Jahrgang/Bereich), rechts „Klasse N Kapitel R Titel“ mit Einheiten.
    zuordnung = []
    block, nennung, erwartet_jahrgang = None, None, False
    for z in zeilen[teil2_ab:]:
        if not z.strip() or any(k in z for k in LSAA_SEITENKOPF):
            continue
        zl = zellen(z)
        links = [c for c in zl if c[0] < LSAA_SPALTE]
        rechts = [c for c in zl if c[0] >= LSAA_SPALTE]
        if links and links[0][0] <= 2:
            if LSAA_STUFE.match(links[0][2]) and len(links) > 1 and links[1][2].startswith("Themenbereich"):
                block = {"stufe": links[0][2], "themenbereich": links[1][2], "jahrgang": "", "bereich": ""}
                nennung, erwartet_jahrgang = None, True
                continue
            if erwartet_jahrgang and LSAA_JAHRGANG.match(links[0][2]) and block is not None:
                block["jahrgang"] = links[0][2]
                block["bereich"] = links[1][2] if len(links) > 1 else ""
                erwartet_jahrgang = False
        for start, ende, text in rechts:
            mn = LSAA_NENNUNG.match(text)
            if mn:
                nennung = [dict(block) if block else None, (mn.group(1), mn.group(2)), []]
                zuordnung.append(nennung)
                continue
            me = LSAA_EINHEIT.match(text)
            if me and nennung is not None:
                nennung[2].append(int(me.group(1)))
    return gliederung, zuordnung, None


def blockkopf_text(b):
    if not b:
        return "ohne Blockkopf"
    tb = re.sub(r"^Themenbereich\s+", "", b["themenbereich"])
    return f"RLP {b['stufe']}, Jg. {b['jahrgang']}, Themenbereich {tb} – {b['bereich']}".strip(" –")


def loese_lsaa(teil, lsaa):
    """Auflösung eines LS-AA-Bestandteils: (aufgeloest, [textzeilen])."""
    gliederung, zuordnung = lsaa
    aus, gut = [], False
    for m in LSAA.finditer(teil):
        klasse, kapitel = f"Klasse {m.group(1)}", m.group(2)
        nummern = []
        if m.group(3):
            a = int(m.group(3))
            b = int(m.group(4)) if m.group(4) else a
            nummern = list(range(a, b + 1))
        g = gliederung.get((klasse, kapitel))
        if g is None:
            aus.append(f"„{m.group(0)}“: {klasse}, Kapitel {kapitel} im Fahrplan (Teil 1) nicht gefunden")
            continue
        text = f"„{m.group(0)}“ → {klasse}, Kapitel {kapitel} „{g['titel']}“"
        if nummern:
            titel = []
            for n in nummern:
                titel.append(f"{n} „{g['einheiten'][n]}“" if n in g["einheiten"] else f"{n} (im Kapitel nicht gefunden)")
            text += ", Lerneinheit " + ", ".join(titel)
            treffer = all(n in g["einheiten"] for n in nummern)
        else:
            text += " (Lerneinheiten: " + " · ".join(f"{n} {t}" for n, t in g["einheiten"].items()) + ")"
            treffer = True
        gut = gut or treffer
        # Teil 2: Blöcke, unter denen das Kapitel (mit dieser Einheit) genannt ist
        koepfe = []
        for block, kap, einheiten in zuordnung:
            if kap != (klasse, kapitel):
                continue
            if nummern and not any(n in einheiten for n in nummern):
                continue
            k = blockkopf_text(block)
            if k not in koepfe:
                koepfe.append(k)
        text += "; Fahrplan-Zuordnung (Teil 2): " + ("; ".join(koepfe) if koepfe else "keine Nennung mit dieser Lerneinheit")
        aus.append(text)
    return gut, aus


# ---------------------------------------------------------------- Register: RLP Teil C

RLP_KOPF = re.compile(r"Themenbereich „([^“]+)“\s*[–-]\s*Niveaustufen?\s*([A-H](?:\s*,\s*[A-H])*)")
RLP_BUCHSTABE = re.compile(r"^([A-H])(?:\s|$)")


def verkette(teile, zusammenziehen):
    """(text, [(anfang, zeilennr)]) – die Zellen eines Spaltenstroms verkettet; mit zusammenziehen wird die
    Silbentrennung am Zeilenende aufgelöst. anfang = Position der Zelle im Text."""
    text, anfaenge = "", []
    for t, nr in teile:
        if text:
            if zusammenziehen and text.endswith("-") and t[:1].islower():
                text = text[:-1]
            else:
                text += " "
        anfaenge.append((len(text), nr))
        text += t
    return text, anfaenge


def lade_rlp(pfad):
    """Blöcke des RLP-Texts: [{"von", "bis", "buchstaben", "kopf", "stroeme": [(text, anfaenge), …]}] – je Strom
    zwei Fassungen (Zellen mit Leerzeichen verkettet; Silbentrennung zusammengezogen)."""
    if not os.path.exists(pfad):
        return None, f"{RLP_QUELLE} fehlt"
    zeilen = lies(pfad).split("\n")
    bloecke, kopf = [], None
    i, n = 0, len(zeilen)
    while i < n:
        if not zeilen[i].strip():
            i += 1
            continue
        j = i
        while j < n and zeilen[j].strip():
            j += 1
        block = {"von": i + 1, "bis": j, "buchstaben": [], "kopf": kopf, "stroeme": []}
        vorige, stroeme = [], []  # vorige: [(start, ende, index in stroeme)]
        for k in range(i, j):
            z = zeilen[k]
            mk = RLP_KOPF.search(z)
            if mk:
                kopf = f"Themenbereich „{mk.group(1)}“ – Niveaustufen {mk.group(2)}"
                block["kopf"] = kopf
            zl = zellen(z)
            if zl and zl[0][0] == 0:
                mb = RLP_BUCHSTABE.match(zl[0][2])
                if mb:
                    block["buchstaben"].append((mb.group(1), k + 1))
                    rest = zl[0][2][2:].strip()
                    zl = ([(2, zl[0][1], rest)] if rest else []) + zl[1:]
            if not zl:  # nur der Buchstabe oder nichts: die Spalten laufen weiter
                continue
            aktuelle, belegt = [], set()
            for start, ende, text in zl:
                # Fortsetzung der Spalte mit der größten Überlappung in der Zeile davor; jede vorige Zelle
                # setzt höchstens eine Zelle fort (eine breite Kopfzeile darf nicht zwei Spalten verschmelzen)
                beste, ueberlappung = None, 0
                for vs, ve, idx in vorige:
                    u = min(ende, ve) - max(start, vs)
                    if u > ueberlappung and idx not in belegt:
                        beste, ueberlappung = idx, u
                if beste is None:
                    stroeme.append([(text, k + 1)])
                    beste = len(stroeme) - 1
                else:
                    stroeme[beste].append((text, k + 1))
                belegt.add(beste)
                aktuelle.append((start, ende, beste))
            vorige = aktuelle
        for teile in stroeme:
            block["stroeme"].append((verkette(teile, False), verkette(teile, True)))
        bloecke.append(block)
        i = j
    return bloecke, None


def zeile_zu_position(anfaenge, pos):
    """Zeilennummer der Zelle, in der die Textposition pos liegt."""
    nr = anfaenge[0][1]
    for anfang, zeilennr in anfaenge:
        if anfang <= pos:
            nr = zeilennr
        else:
            break
    return nr


def suche_rlp(zitat, bloecke):
    """Fundstellen eines Zitats: [(block, genau, (zeile_von, zeile_bis))] – genau=False bei Treffer ohne
    Groß-/Kleinschreibung; „…“ im Zitat erlaubt eine Lücke."""
    teile = [re.sub(r"\s+", " ", t).strip() for t in re.split(r"…|\.\.\.", zitat)]
    teile = [t for t in teile if t]

    def enthaelt(text, genau):
        """(anfang, ende) des Treffers oder None."""
        pos, erster = 0, None
        haystack = text if genau else text.lower()
        for t in teile:
            nadel = t if genau else t.lower()
            p = haystack.find(nadel, pos)
            if p < 0:
                return None
            if erster is None:
                erster = p
            pos = p + len(nadel)
        return erster, pos

    aus = []
    for genau in (True, False):
        for b in bloecke:
            for fassungen in b["stroeme"]:
                fund = None
                for text, anfaenge in fassungen:
                    span = enthaelt(text, genau)
                    if span:
                        fund = (zeile_zu_position(anfaenge, span[0]), zeile_zu_position(anfaenge, max(span[0], span[1] - 1)))
                        break
                if fund:
                    aus.append((b, genau, fund))
                    break
        if aus:
            break
    return aus


def fundstelle_text(b, genau, zeilen):
    buchstaben = ", ".join(f"{x} (Zeile {nr})" for x, nr in b["buchstaben"]) or "kein Buchstabe am Block"
    wo = f"Zeile {zeilen[0]}" if zeilen[0] == zeilen[1] else f"Zeilen {zeilen[0]}–{zeilen[1]}"
    return (f"{wo} (Block {b['von']}–{b['bis']}), Niveaustufe am Block: {buchstaben}; Seitenkopf: "
            f"{b['kopf'] or 'keiner davor'}" + ("" if genau else "; Schreibweise abweichend (ohne Groß-/Kleinschreibung)"))


MIN_WOERTER_ANFANG = 3  # Wortanfang eines nicht gefundenen Zitats: mindestens so viele Wörter und mindestens die Hälfte


def suche_rlp_anfang(zitat, bloecke):
    """(k, n, funde) – der längste Wortanfang eines nicht gefundenen Zitats (k von n Wörtern), der im Text steht;
    None, wenn das Zitat eine Lücke „…“ hat oder kein Anfang mit mindestens MIN_WOERTER_ANFANG Wörtern und
    mindestens der Hälfte der Wörter vorkommt."""
    if "…" in zitat or "..." in zitat:
        return None
    woerter = zitat.split()
    n = len(woerter)
    for k in range(n - 1, max(MIN_WOERTER_ANFANG, (n + 1) // 2) - 1, -1):
        funde = suche_rlp(" ".join(woerter[:k]), bloecke)
        if funde:
            return k, n, funde
    return None


def loese_rlp_zitat(teil, bloecke):
    """(aufgeloest, [textzeilen]) für einen RLP-Bestandteil mit Zitat."""
    stufe = RLP.match(teil).group(1)
    aus, alle = [], True
    for m in ZITAT.finditer(teil):
        funde = suche_rlp(m.group(1), bloecke)
        if funde:
            aus.append(f"„{m.group(1)}“ (Klammer nennt {stufe}): " + " | ".join(fundstelle_text(b, g, z) for b, g, z in funde))
            continue
        alle = False
        anfang = suche_rlp_anfang(m.group(1), bloecke)
        if anfang:
            k, n, funde = anfang
            aus.append(f"„{m.group(1)}“ (Klammer nennt {stufe}): im RLP-Text nicht gefunden; Teiltreffer – der "
                       f"Wortanfang „{' '.join(m.group(1).split()[:k])}“ ({k} von {n} Wörtern) steht in: "
                       + " | ".join(fundstelle_text(b, g, z) for b, g, z in funde))
        else:
            aus.append(f"„{m.group(1)}“ (Klammer nennt {stufe}): im RLP-Text nicht gefunden")
    return alle and bool(aus), aus


# ---------------------------------------------------------------- Register: MSK-Bausteintitel aus _quellen.md

MSK_TITEL = re.compile(r"(?:^|\s)([A-Z]{1,2}\d{0,2}[A-Z]?)(?:\s+([A-C]–[A-C]))?\s+(„[^“]+“|[A-ZÄÖÜ][^,;()]*)")


def lade_msk_titel(pfad):
    """code -> Bausteintitel aus der Registerzeile [MSK] von katalog/_quellen.md; {} wenn nichts lesbar ist."""
    if not os.path.exists(pfad):
        return {}, f"{QUELLENREGISTER} fehlt"
    zeile = next((z for z in lies(pfad).split("\n") if z.startswith("- [MSK]")), None)
    if zeile is None:
        return {}, f"{QUELLENREGISTER}: keine Registerzeile „- [MSK]“"
    titel = collections.OrderedDict()
    for segment in re.split(r"[,;()]", zeile):
        for m in MSK_TITEL.finditer(segment):
            code, bereich, t = m.group(1), m.group(2), m.group(3).strip()
            t = re.split(r"\s+nur\s", t)[0].strip().rstrip(".:")
            if not t.startswith("„") and not re.search(r"[a-zäöüß]", t):
                continue  # kein Titel (z. B. „CC BY-NC-SA 4.0“)
            if code not in titel:
                titel[code] = (t.strip("„“"), bereich)
    return titel, None


# ---------------------------------------------------------------- Auflösung je Bestandteil

def loese_p10(teil, typen, beispiel, kataloge, msa_kanonisch):
    """(aufgeloest, [textzeilen]) für einen P10-Bestandteil."""
    aus, gut = [], False

    def kanonisch(thema):
        k = msa_kanonisch.get(thema)
        return f" → themen.csv: {', '.join(k)}" if k else " → themen.csv: kein kanonisches Thema mit diesem msa-Thema"

    for m in ZITAT.finditer(teil):
        name = m.group(1)
        if typen is None:
            aus.append(f"„{name}“: Sorte ausgelassen (siehe Meldung)")
        elif name in typen:
            e = typen[name]
            aus.append(f"Typ „{name}“ in {MSA_TYPEN}: Thema „{e['thema']}“ (Leitidee {e['leitidee'] or '–'})" + kanonisch(e["thema"]))
            gut = True
        else:
            aus.append(f"„{name}“: kein Typname in {MSA_TYPEN}")
    for m in KENNUNG.finditer(teil):
        kennung = m.group(1)
        stuecke = []
        if beispiel and kennung in beispiel:
            for t in beispiel[kennung]:
                stuecke.append(f"beispiel_id des Typs „{t}“ in {MSA_TYPEN}, Thema „{typen[t]['thema']}“" + kanonisch(typen[t]["thema"]))
            gut = True
        if kennung in kataloge:
            datei, thema, typ, neben = kataloge[kennung]
            stuecke.append(f"Katalogzeile ({datei}): Thema „{thema}“, Typ „{typ}“"
                           + (f", Nebentypen „{neben}“" if neben else "") + kanonisch(thema))
            gut = True
        if not stuecke:
            stuecke.append(f"in {MSA_TYPEN} (beispiel_id) und den msa-Katalogen nicht gefunden")
        aus.append(f"Kennung {kennung}: " + "; ".join(stuecke))
    return gut, aus


def loese_msk(teil, msk_titel):
    """[textzeilen] – Bausteintitel je Code, soweit _quellen.md ihn nennt (keine Auflösung)."""
    codes = re.findall(r"(?<![\w])([A-Z]{1,2}\d{0,2}[A-Z]?)(?![\w])", teil[4:])
    aus = []
    for code in codes:
        if code in msk_titel:
            t, bereich = msk_titel[code]
            aus.append(f"{code}: Bausteintitel in _quellen.md „{t}“" + (f" ({bereich})" if bereich else ""))
        else:
            aus.append(f"{code}: Bausteintitel in _quellen.md nicht genannt")
    return aus


def ohne_klammer(zeile):
    """Der Wortlaut der Zeile ohne ihre eckigen Klammern (die Quellenklammer ist Beleg, nicht Wortlaut)."""
    return KLAMMER.sub(" ", zeile)


def themen_treffer(zeile, name, nach_kanonisch, h1):
    """[(kanonisch, form, treffer, kontext)] – kanonische Namen, deren Name, thema-Wert oder H1 als ganzes Wort im
    Wortlaut der Zeile (ohne Quellenklammer) steht; der eigene Eintrag zählt nicht."""
    text = ohne_klammer(zeile)
    aus = []
    for k, zs in nach_kanonisch.items():
        if k == name:
            continue
        kandidaten = [("Name", k), ("Name", k.replace("-", " "))]
        for z in zs:
            t = z["thema"].strip()
            if t:
                kandidaten.append(("thema", t))
        if k in h1 and h1[k]:
            kandidaten.append(("H1", h1[k]))
        for form, wort in kandidaten:
            m = re.search(r"(?<!" + WORT + r")" + re.escape(wort) + r"(?!" + WORT + r")", text,
                          re.I if form == "Name" else 0)
            if m:
                a, e = max(0, m.start() - 30), min(len(text), m.end() + 30)
                kontext = ("…" if a > 0 else "") + text[a:e].strip() + ("…" if e < len(text) else "")
                aus.append((k, form, m.group(0), re.sub(r"\s+", " ", kontext)))
                break
    return aus


def tick(text):
    """Text für die Ausgabe in Backticks; enthält er selbst einen Backtick, in Anführungszeichen."""
    return f"`{text}`" if "`" not in text else f"„{text}“"


# ---------------------------------------------------------------- Messung

def zaehle(katalog):
    """Nur die Zahlen, ohne Register: Eintrag -> (fertigkeitszeilen, mit_ziel, ohne_ziel); None ohne Abschnitt.
    _pruef_struktur.py importiert diese Zählregel für Kennzahl 9."""
    namen = T.eintraege(katalog)
    vorhanden = set(namen)
    aus = collections.OrderedDict()
    for name in namen:
        zeilen_, _ = fertigkeitszeilen(lies(os.path.join(katalog, name + ".md")))
        if zeilen_ is None:
            aus[name] = None
            continue
        mit = sum(1 for _, z in zeilen_ if ziele(z, name, vorhanden))
        aus[name] = (len(zeilen_), mit, len(zeilen_) - mit)
    return aus


def messe(wurzel=HIER, debug=False):
    katalog = os.path.join(wurzel, KATALOG_ORDNER)
    namen = T.eintraege(katalog)
    vorhanden = set(namen)
    texte = collections.OrderedDict((n, lies(os.path.join(katalog, n + ".md"))) for n in namen)
    h1 = {n: (H1.search(t).group(1).strip() if H1.search(t) else "") for n, t in texte.items()}
    stufe = {}
    for n, t in texte.items():
        m = STUFE.search("\n".join(t.split("\n", 3)[:3]))
        stufe[n] = m.group(1).strip() if m else "–"

    meldungen = []
    typen, beispiel, grund = lade_msa_typen(os.path.join(wurzel, MSA_TYPEN))
    if grund:
        meldungen.append(grund)
    kataloge, m2 = lade_msa_kataloge(MSA_KATALOGE)
    meldungen.extend(m2)
    nach_kanonisch, msa_kanonisch = lade_konkordanz()
    gliederung, zuordnung, grund = lade_lsaa(os.path.join(wurzel, LSAA_QUELLE))
    if grund:
        meldungen.append(grund)
    bloecke, grund = lade_rlp(os.path.join(wurzel, RLP_QUELLE))
    if grund:
        meldungen.append(grund)
    msk_titel, grund = lade_msk_titel(os.path.join(wurzel, QUELLENREGISTER))
    if grund:
        meldungen.append(grund)

    if debug:
        print("LS-AA Teil 1 – Gliederung:")
        for (kl, kap), g in gliederung.items():
            print(f"  {kl} Kapitel {kap} „{g['titel']}“: " + " · ".join(f"{n} {t}" for n, t in g["einheiten"].items()))
        print(f"LS-AA Teil 2 – {len(zuordnung)} Kapitelnennungen unter RLP-Blöcken, z. B.:")
        for block, kap, einheiten in zuordnung[:8]:
            print(f"  {blockkopf_text(block)} ← {kap[0]} Kapitel {kap[1]} {einheiten}")
        print(f"RLP – {len(bloecke)} Blöcke, {sum(len(b['stroeme']) for b in bloecke)} Spaltenströme")
        print("MSK-Bausteintitel aus _quellen.md: " + "; ".join(f"{c} = „{t}“{' (' + b + ')' if b else ''}" for c, (t, b) in msk_titel.items()))

    eintraege = collections.OrderedDict()
    for name in namen:
        zeilen_, zwischenzeile = fertigkeitszeilen(texte[name])
        e = {"stufe": stufe[name], "abschnitt": zeilen_ is not None, "zwischenzeile": zwischenzeile,
             "fertigkeiten": 0, "mit": 0, "ohne": 0, "zeilen": []}
        for nr, zeile in (zeilen_ or []):
            e["fertigkeiten"] += 1
            if ziele(zeile, name, vorhanden):
                e["mit"] += 1
                continue
            e["ohne"] += 1
            inhalt, am_ende = klammer(zeile)
            teile = []
            if inhalt is None:
                teile.append({"text": "keine Klammer", "sorte": SORTEN[5], "aufgeloest": False, "auskunft": []})
            else:
                for t in zerlege(inhalt):
                    s = sorte(t)
                    gut, auskunft = False, []
                    if s == SORTEN[0]:
                        if typen is None:
                            auskunft = ["Sorte ausgelassen: " + [m for m in meldungen if MSA_TYPEN in m][0]]
                        else:
                            gut, auskunft = loese_p10(t, typen, beispiel, kataloge, msa_kanonisch)
                    elif s == SORTEN[1]:
                        if gliederung is None:
                            auskunft = ["Register fehlt"]
                        else:
                            gut, auskunft = loese_lsaa(t, (gliederung, zuordnung))
                    elif s == SORTEN[2]:
                        if bloecke is None:
                            auskunft = ["Register fehlt"]
                        else:
                            gut, auskunft = loese_rlp_zitat(t, bloecke)
                    elif s == SORTEN[4]:
                        auskunft = loese_msk(t, msk_titel)
                    teile.append({"text": t, "sorte": s, "aufgeloest": gut, "auskunft": auskunft})
            e["zeilen"].append({"nr": nr, "zeile": zeile, "klammer": inhalt, "am_ende": am_ende, "teile": teile,
                                "themen": themen_treffer(zeile, name, nach_kanonisch, h1)})
        eintraege[name] = e

    fehlend = [n for n in SEK1_AUFTRAG if n not in eintraege]
    if fehlend:
        meldungen.append("Einträge der 22 fehlen: " + ", ".join(fehlend))
    return {"eintraege": eintraege, "meldungen": meldungen, "msk_titel": msk_titel, "msa_typen_ok": typen is not None}


def gruppen(m):
    """(sek1, rest) – die 22 des Auftrags in ihrer Reihenfolge; die übrigen: Sek I, Sek I + II, Sek II, je alphabetisch."""
    e = m["eintraege"]
    sek1 = [n for n in SEK1_AUFTRAG if n in e]
    rang = {"Sek I": 0, "Sek I + II": 1, "Sek II": 2}
    rest = sorted((n for n in e if n not in SEK1_AUFTRAG), key=lambda n: (rang.get(e[n]["stufe"], 3), n))
    return sek1, rest


def summen(m, namen):
    f = sum(m["eintraege"][n]["fertigkeiten"] for n in namen)
    mit = sum(m["eintraege"][n]["mit"] for n in namen)
    ohne = sum(m["eintraege"][n]["ohne"] for n in namen)
    return f, mit, ohne


def sortenzaehlung(m, namen):
    """sorte -> (bestandteile, aufgeloest); dazu MSK-Codes mit Bausteintitel."""
    z = collections.OrderedDict((s, [0, 0]) for s in SORTEN)
    msk_titel = 0
    for n in namen:
        for zl in m["eintraege"][n]["zeilen"]:
            for t in zl["teile"]:
                z[t["sorte"]][0] += 1
                if t["aufgeloest"]:
                    z[t["sorte"]][1] += 1
                if t["sorte"] == SORTEN[4] and any("Bausteintitel in _quellen.md „" in a for a in t["auskunft"]):
                    msk_titel += 1
    return z, msk_titel


# ---------------------------------------------------------------- Ausgabe

def baue(m, stand):
    e = m["eintraege"]
    sek1, rest = gruppen(m)
    n = len(e)
    out = []
    w = out.append
    w("# Belege der Blatt-0-Fertigkeiten ohne Ziel")
    w(f"Stand {stand}.")
    w(f"Erzeugt von `werkzeuge/{VERSION.replace(' ', '` (')}) aus den Blatt-0-Abschnitten der Einträge, "
      f"`{MSA_TYPEN}`, `{MSA_KATALOGE[0]}`, `{MSA_KATALOGE[1]}`, `{KONKORDANZ}`, `{LSAA_QUELLE}`, "
      f"`{RLP_QUELLE}` und der Registerzeile [MSK] in `{QUELLENREGISTER}`; abgeleitet, nie von Hand ändern. "
      "Vorschlagsliste für die Fertigkeitszeilen, die keinen Dateiverweis tragen: was ihre Quellenklammer "
      "hergibt, wenn man sie gegen die Register im Repo hält. Kein Eintrag wird geändert, nichts wird "
      "entschieden; eine Zeile, deren Klammer kein Register auflöst, bleibt ohne Vorschlag – das ist ein "
      "Ergebnis, kein Mangel.")
    w("")
    w(f"Gemessen: {n} Einträge (`katalog/*.md` ohne `_*` und `index.md`). Lesarten wie in "
      "`werkzeuge/tragfaehigkeit.py` (v0.1), importiert: Blatt-0-Abschnitt = „### Voraussetzungen (Blatt 0)“ bis "
      "zur nächsten Überschrift, Verweis = `<name>.md`. Fertigkeitszeile = Zeile des Abschnitts, die mit „- “ "
      "beginnt und vor der Zwischenzeile „Erkennungsschritte…“ steht (die Erkennungsschritte gehören dem Thema "
      "selbst). Ziel = Verweis ohne Pfad auf einen anderen vorhandenen Katalogeintrag, irgendwo in der Zeile; "
      "Selbstverweise zählen nicht. Klammer = die letzte eckige Klammer der Zeile (vermerkt, wenn sie nicht am "
      "Zeilenende steht). Bestandteile = Klammer an „;“ und „,“ zerlegt, nicht in „…“ und nicht in runden "
      "Klammern; ein Teil, der mit einer P10-Aufgabenkennung beginnt, setzt den vorigen fort, ein bloßer "
      "MSK-Code einen MSK-Teil. Sechs Sorten je Bestandteil: P10-Typ (enthält „P10“ und einen Typnamen in „…“ "
      "oder eine Aufgabenkennung), LS-AA-Kapitel („LS-AA Kl. 8 II 1“), RLP mit Zitat, RLP ohne Zitat (auch mit "
      "Zusatz ohne Anführungszeichen), MSK-Code, sonstiges oder keine Klammer. Zeilennummern zählen ab 1 in der "
      "Datei.")
    w("")
    w("Auflösung, soweit ein Register es hergibt: P10-Typ – Typname gegen die Spalte `typ` von "
      f"`{MSA_TYPEN}`, Kennung gegen `beispiel_id`; je Treffer das Thema und über `{KONKORDANZ}` (profil msa) "
      "das kanonische Thema; Kennungen zusätzlich gegen die `id`-Spalte der beiden msa-Kataloge (Thema, Typ, "
      "Nebentypen der Katalogzeile), weil die Typenliste je Typ nur eine beispiel_id führt. LS-AA-Kapitel – "
      "Fahrplan Teil 1 (Gliederung je Klasse, zweispaltig): Kapiteltitel und Titel der Lerneinheit; Teil 2 "
      "(RLP-Inhalte mit „Zu finden in Studyly“): die RLP-Blöcke (Niveaustufe, Jahrgang, Themenbereich, Bereich), "
      "unter denen das Kapitel mit dieser Lerneinheit genannt ist. RLP mit Zitat – das Zitat wird in den Spalten "
      "des RLP-Texts gesucht (mehrspaltig gesetzt; ein Block sind die Zeilen zwischen zwei Leerzeilen, darin wird "
      "jede Zelle an die Zelle der Zeile davor gehängt, mit der sie sich am weitesten überlappt – je Zelle "
      "höchstens eine Fortsetzung –, Silbentrennung wird zusammengezogen, „…“ im Zitat erlaubt eine Lücke); "
      "Fundstelle mit Zeilen des Treffers, Block, Niveaustufenbuchstabe(n) am Block (der Buchstabe steht einmal "
      "je Stufe am linken Rand, in der Mitte seiner Zeilen) und Seitenkopf – zuerst genau, sonst ohne "
      "Groß-/Kleinschreibung. Steht das Zitat nicht im Text, wird noch der längste Wortanfang gesucht (mindestens "
      f"{MIN_WOERTER_ANFANG} Wörter und mindestens die Hälfte; nicht bei Zitaten mit Lücke) und als Teiltreffer "
      "genannt, ohne als Auflösung zu zählen. RLP ohne Zitat, MSK-Code und sonstiges werden nach Auftrag nicht "
      "aufgelöst („nicht aufzulösen“; „nicht aufgelöst“ heißt dagegen: das Register gab nichts her); beim "
      f"MSK-Code steht der Bausteintitel aus `{QUELLENREGISTER}` dabei, soweit er dort genannt ist. Zusätzlich "
      f"je Zeile: welche kanonischen Namen aus `{KONKORDANZ}` der Wortlaut der Zeile ohne ihre Quellenklammer "
      "wörtlich nennt (der Name selbst mit Bindestrich als Leerzeichen und ohne Rücksicht auf "
      "Groß-/Kleinschreibung, ein `thema`-Wert seiner Zeilen oder die H1-Überschrift seiner Katalogdatei, jeweils "
      "als ganzes Wort, mit dem Umfeld des Treffers; der eigene Eintrag zählt nicht) – keine Ähnlichkeitssuche, "
      "kein Raten; ob das Wort in der Zeile das Thema meint, steht nicht hier.")
    w("")
    f1, m1, o1 = summen(m, sek1)
    f2, m2, o2 = summen(m, rest)
    w("## Zahlen")
    w(f"Teil 1, die {len(sek1)} Sek-I-Einträge des Auftrags Blatt-0-Dateiverweise (21 Dateien aus "
      "`archiv/ersetzungen-blatt0-2026-09-21.txt` und `terme.md`; dieselbe Menge wie `_verweise.md` § 5 auf "
      f"Commit c05e6f0): {f1} Fertigkeitszeilen, {m1} mit Ziel, {o1} ohne. Gegenprobe des Auftrags "
      f"{GEGENPROBE[0]}/{GEGENPROBE[1]}/{GEGENPROBE[2]}: " + ("bestanden." if (f1, m1, o1) == GEGENPROBE else "ABWEICHUNG."))
    w(f"Teil 2, die übrigen {len(rest)} Einträge: {f2} Fertigkeitszeilen, {m2} mit Ziel, {o2} ohne – berichtet, "
      "nicht geprüft. Darunter sieben Einträge mit Stufe Sek I oder Sek I + II in der Statuszeile "
      f"({', '.join(x for x in rest if e[x]['stufe'] != 'Sek II')}); sie stehen in Teil 2 vorn.")
    for teil_name, namen in (("Teil 1", sek1), ("Teil 2", rest)):
        z, titel = sortenzaehlung(m, namen)
        w(f"Bestandteile der Klammern in {teil_name} nach Sorte (Bestandteile · davon aufgelöst): "
          + "; ".join(f"{s} {b} · {a}" for s, (b, a) in z.items())
          + f". MSK-Codes mit Bausteintitel aus _quellen.md: {titel}.")
    ohne_abschnitt = [x for x in e if not e[x]["abschnitt"]]
    ohne_zwischenzeile = [x for x in e if e[x]["abschnitt"] and not e[x]["zwischenzeile"]]
    w(f"Einträge ohne Blatt-0-Abschnitt: {', '.join(ohne_abschnitt) or 'keine'}. Einträge ohne Zwischenzeile "
      f"„Erkennungsschritte…“ (der ganze Abschnitt gilt als Fertigkeitenteil): {', '.join(ohne_zwischenzeile) or 'keine'}.")
    if m["meldungen"]:
        w("Meldungen: " + " | ".join(m["meldungen"]))
    w("")

    def eintrag(name):
        d = e[name]
        kopf = (f"### {name} – Stufe {d['stufe']}; {d['fertigkeiten']} Fertigkeitszeilen, {d['mit']} mit Ziel, "
                f"{d['ohne']} ohne")
        w(kopf)
        if not d["abschnitt"]:
            w("Kein Abschnitt „### Voraussetzungen (Blatt 0)“.")
            w("")
            return
        if not d["zeilen"]:
            w("Alle Fertigkeitszeilen tragen ein Ziel." if d["fertigkeiten"] else "Keine Fertigkeitszeile.")
            w("")
            return
        for zl in d["zeilen"]:
            w(f"- Zeile {zl['nr']}:")
            w(f"  > {zl['zeile']}")
            if zl["klammer"] is None:
                w("  - Klammer: keine – Sorte sonstiges oder keine Klammer.")
            else:
                w(f"  - Klammer: {tick(zl['klammer'])}" + ("" if zl["am_ende"] else " (nicht am Zeilenende)")
                  + f" – {len(zl['teile'])} {'Bestandteil' if len(zl['teile']) == 1 else 'Bestandteile'}:")
                for t in zl["teile"]:
                    status = ("aufgelöst" if t["aufgeloest"] else
                              ("nicht aufgelöst" if t["sorte"] in SORTEN[:3] else "nicht aufzulösen"))
                    w(f"    - {tick(t['text'])} – {t['sorte']}, {status}" + ("." if not t["auskunft"] else ":"))
                    for a in t["auskunft"]:
                        w(f"      - {a}")
            if zl["themen"]:
                w("  - themen.csv wörtlich im Wortlaut: " + "; ".join(f"**{k}** ({form} „{treffer}“ in „{kontext}“)"
                                                                     for k, form, treffer, kontext in zl["themen"]) + ".")
            else:
                w("  - themen.csv: kein kanonischer Name, kein thema-Wert und keine H1 wörtlich im Wortlaut.")
        w("")

    w("## 1 Die 22 Sek-I-Einträge des Auftrags Blatt-0-Dateiverweise")
    w("Reihenfolge wie in der Ersetzungsdatei (alphabetisch). Je Eintrag die Fertigkeitszeilen ohne Ziel mit "
      "Zeilennummer, Wortlaut, Klammer, Bestandteilen, Sorte, dem, was die Register hergeben, und den wörtlichen "
      "themen.csv-Treffern.")
    w("")
    for name in sek1:
        eintrag(name)
    w("## 2 Die übrigen Einträge")
    w("Zuerst die Einträge mit Stufe Sek I und Sek I + II in der Statuszeile, dann die Sek-II-Einträge, je "
      "alphabetisch. Gleicher Aufbau wie Teil 1; die Zahlen sind nicht gegengeprüft.")
    w("")
    for name in rest:
        eintrag(name)
    w("## Schwäche der Messung")
    w("Die Zerlegung sieht Zeichenketten, keine Bedeutung. Ob eine Zeile ein Ziel hat, entscheidet allein die "
      "Form `<name>.md`; eine Zeile, die ihr Thema in Wortform nennt („Thema Prozentrechnung, Einheit 3“), gilt "
      "als ohne Ziel und landet hier – der themen.csv-Treffer zeigt solche Fälle, ohne sie zu deuten. Die Sorten "
      "hängen an Signalwörtern („P10“, „LS-AA Kl.“, „RLP“ mit Buchstabe, „MSK“); eine Klammer in anderer "
      "Schreibweise fällt unter sonstiges. Die Zerlegung an Komma und Semikolon kann eine Aufzählung innerhalb "
      "eines Belegs trennen, wo weder Anführungszeichen noch Kennung noch MSK-Code den Zusammenhang zeigen. Beim "
      "P10-Typ sagt ein gefundener Typ nur, welches Thema die Typenliste ihm gibt, nicht, ob die Fertigkeit der "
      "Zeile dort gelehrt wird; die Katalogzeile einer Kennung nennt Thema und Typ der Aufgabe, nicht der "
      "Fertigkeit. Beim LS-AA-Fahrplan hängt die Lesung an der zweispaltigen Textfassung (Spaltengrenze bei "
      f"Zeichen {LSAA_SPALTE}); Teil 2 nennt nur die Blöcke, unter denen das Kapitel mit der Lerneinheit steht, "
      "nicht die RLP-Zeile daneben. Beim RLP-Text werden Spalten nach der Überlappung der Zellen verkettet; ein "
      "Zitat, das über eine Seite hinweg umbricht oder im Katalog gekürzt wurde, wird nicht gefunden – „nicht "
      "gefunden“ heißt hier nur: nicht in dieser Textfassung, in dieser Schreibweise. Der Niveaustufenbuchstabe "
      "steht im RLP-Text einmal je Block in der Mitte; fehlt er am Block, ist die Stufe nur über den Seitenkopf "
      "und die Nachbarblöcke zu lesen; ein Teiltreffer über den Wortanfang zeigt nur, wo der Anfang des Zitats "
      "steht, nicht, was der Katalog daraus gemacht hat. Der themen.csv-Abgleich meldet jedes ganze Wort, auch "
      "wenn es in der Zeile etwas anderes meint („Einheiten“ in „alle Einheiten“ sind Lerneinheiten, „Geraden“ "
      "kann eine Sek-I-Gerade sein); das Umfeld steht dabei, die Deutung nicht – er ist ein Hinweis, kein Vorschlag.")
    w("")
    return "\n".join(out)


def main():
    debug = "--debug" in sys.argv
    m = messe(debug=debug)
    sek1, rest = gruppen(m)
    f1, m1, o1 = summen(m, sek1)
    if (f1, m1, o1) != GEGENPROBE:
        print(f"{VERSION}: Gegenprobe verfehlt – die {len(sek1)} Sek-I-Einträge des Auftrags haben {f1} Fertigkeits"
              f"zeilen, {m1} mit Ziel, {o1} ohne (erwartet {GEGENPROBE[0]}/{GEGENPROBE[1]}/{GEGENPROBE[2]}). "
              "Abschnitts- oder Zeilenerkennung prüfen; nichts geschrieben.")
        for n in sek1:
            d = m["eintraege"][n]
            print(f"  {n}: {d['fertigkeiten']} / {d['mit']} / {d['ohne']}")
        return 1
    stand = f"{datetime.date.today().isoformat()}, Katalog auf Commit {T.head_kurz()}"
    text = baue(m, stand)
    pfad = os.path.join(HIER, KATALOG_ORDNER, AUSGABE)
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    f2, m2, o2 = summen(m, rest)
    print(f"{VERSION}: {len(m['eintraege'])} Einträge gemessen; {KATALOG_ORDNER}/{AUSGABE} geschrieben "
          f"({text.count(chr(10))} Zeilen).")
    print(f"Gegenprobe: {len(sek1)} Sek-I-Einträge des Auftrags – {f1} Fertigkeitszeilen, {m1} mit Ziel, {o1} ohne "
          f"(erwartet {GEGENPROBE[0]}/{GEGENPROBE[1]}/{GEGENPROBE[2]}): bestanden.")
    print(f"Übrige {len(rest)} Einträge – {f2} Fertigkeitszeilen, {m2} mit Ziel, {o2} ohne (berichtet, nicht geprüft).")
    for teil_name, namen in (("Teil 1", sek1), ("Teil 2", rest)):
        z, titel = sortenzaehlung(m, namen)
        print(f"{teil_name}, Bestandteile nach Sorte (Bestandteile · aufgelöst): "
              + "; ".join(f"{s} {b} · {a}" for s, (b, a) in z.items()) + f"; MSK mit Bausteintitel {titel}")
    for meldung in m["meldungen"]:
        print("Meldung:", meldung)
    return 0


if __name__ == "__main__":
    sys.exit(main())
