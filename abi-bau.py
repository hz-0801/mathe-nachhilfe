# -*- coding: utf-8 -*-
"""abi-bau.py – Gerüst für die Erfassung eines Hefts im Profil abi.
Version 0.8 · 16.09.2026 · gilt mit katalog-prompt.md v0.5, abitur-vokabular.md v1.2 und abi.md v0.14

Je Heft werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" und unter „AB HIER UNVERÄNDERT" bleibt unverändert.

Änderungen gegenüber 0.7 (Heft 2022-bebb-lk, 16.09.2026): Die Eichschwelle
zählt nur eigene Schätzungen. Eine Dublette, die die Schätzung ihrer Poolzeile
trägt, ist dort schon gemessen (Eichung des Stapels in iqb-pruefungen.md); sie
für die Schwelle des Hefts noch einmal zu zählen, misst nichts Neues, sondern
nur die zufällige Teilmenge des Pools, die das Heft übernimmt (2022-bebb-lk:
27 von 32 geerbten Zeilen, 84 %, alle fünf Abweichungen in der Poolzeile
vermerkt). Die Kennzahl Eichung je Heft nennt weiter alle gewerteten Zeilen
und weist die geerbten aus; die Schwelle greift bei mindestens zehn eigenen
gewerteten Zeilen. Die Schätzung selbst bleibt unverändert (keine
nachträgliche Anpassung an den Standardbezug, iqb.md § 7).

Änderungen gegenüber 0.6 (Auftrag „Geltung klären, Reste schließen, vier
Stark-Hefte erfassen", 16.09.2026): Geltung je Heft – ein Heft wird gegen die
Zielprüfung(en) seines papier-Kürzels gemessen (ziele_von: be-gk, be-lk,
bb-ea; gemeinsame Hefte bebb-gk gegen be-gk und bb-gk, bebb-lk gegen be-lk
und bb-ea); eine Zeile liegt in der Geltung, wenn ihr Thema in mindestens
einer dieser Spalten gilt, der Bericht nennt beide Spalten einzeln und
daneben weiter alle vier Zielprüfungen (abitur-vokabular.md § 3).

Änderungen gegenüber 0.5 (Auftrag „Reserve öffnen, Verweise schließen",
16.09.2026): Die Vormerkung „Poolaufgabe (nicht erfasst …)" ist ein
Übergangszustand – offener Posten, bis der Stapel erfasst ist; danach stellt
abgleich.py sie auf „Dublette von:" (wortgleich) oder auf den neuen Verweis
„Abgewandelt von: <Kennung>; <Unterschied>." (abgewandelte Fassung, kein
geteilter Typ verlangt) um. Beide Verweise werden geprüft (Kennung, Feldanfang,
Poolzeile erfasst); die Poolquote zählt „Abgewandelt von" wie bisher die
abgewandelte Vormerkung.

Änderungen gegenüber 0.4 (Auftrag „Heft 2023 nachprüfen, abi-Bestand gegen
den Pool abgleichen"): Poolquote je Heft als Kennzahl (Zeilen und BE, die
wortgleich im Pool stehen; in der Kennzahlenzeile und in der Selbstprüfung je
Heft); Vermerk „Poolaufgabe (nicht erfasst): <Kennung>" als Vorstufe des
Verweises „Dublette von:", geprüft (Kennung, Feldanfang, noch nicht erfasst);
Pool-Kennungen mit Aufgabennummer vom ASCII-Minus-Test ausgenommen (schon im
Heftlauf 2023).

Änderungen gegenüber 0.3 (Entscheidung des Lehrers, 16.09.2026: Themenfeld
bereinigen): leitidee und thema einer Zeile müssen gleich leitidee und thema
ihres Typs in abitur-typen.csv sein (geprüft für ZEILEN und in der
Selbstprüfung für den Bestand); der Schnitt Thema × Klasse × Handlung wird
über das Thema des Typs gemessen (Lauf 13 von abgleich.py hat den Bestand
darauf gebracht). Wie iqb-bau.py v1.1.

Änderungen gegenüber 0.2 (Entscheidung 25, 15.09.2026: gemeinsame Typenliste
für abi und iqb, abi auf dem Typenschnitt nach Entscheidung 24) – das Skript
zieht auf den Stand von iqb-bau.py v1.0 nach:
  - Sachgebiete, Themen, Geltungstabelle, Gegenstandsklassen und Handlungen
    kommen aus abitur-vokabular.md; das Profil abi.md liefert kein Vokabular mehr.
  - Typenliste abitur-typen.csv, geteilt mit iqb: beispiel_id darf in iqb-katalog.csv
    zeigen, ein Typ gilt als verwendet, wenn er in einem der Kataloge steht
    (ANDERE_KATALOGE). Präfixregel (abitur-vokabular.md § 4) für Typenliste und
    NEUE_TYPEN.
  - SCHWELLEN: Qualitätsschranke im Skript („?", ersatzweise, Eichung).
  - Eichung, wo ein amtlicher Bereich vorliegt (afb_amtlich, in Teil B
    zusätzlich „AB amtlich: …" in bemerkung wie im Profil iqb); die Hefte bis
    2018 haben keinen und zählen nicht.
  - Vollständigkeit: jede Aufgabe in KONFIG["soll"] muss Zeilen haben, jede
    Punktsumme stimmen; KONFIG["probe"] = True prüft, schreibt aber nichts.
  - Pool-Teilaufgaben in Landesheften (abi.md § 7): eigene Zeile mit
    geteiltem Typ, Verweis „Dublette von: <iqb-id>" in bemerkung; das Skript
    prüft, dass die id im iqb-Katalog steht und typ wie typ_neben gleich sind.
  - Trägerbindung wie im Profil iqb: feste Markierung „Traegerbindung: Kontext"
    am Anfang von bemerkung, kein eigenes Feld.
  - Kennzahlenzeile je Heft (Typen neu, Eichung, Wiederverwendung im Niveau,
    Geltung, Schnitt) für abi-pruefungen.md § 2.
  - papier-Kürzel bebb für die gemeinsamen Hefte 2019–2025; aufgabe darf ein-
    oder zweistufig sein (Aufgabe 3 gegen 2.1).
Umbenennungen und Zusammenziehungen laufen über abgleich.py (Kern § 9).

Ablauf:
  1. abitur-vokabular.md, katalog-prompt.md, abi-katalog.csv, iqb-katalog.csv und
     abitur-typen.csv neben dieses Skript legen (aus dem Repo).
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen.
  3. python abi-bau.py – schreibt beide CSV-Dateien, gibt Prüftabelle und
     Bericht aus. Bei einem Fehler wird nichts geschrieben.
  4. Ist ZEILEN leer, läuft nur die Selbstprüfung über den Gesamtbestand.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    "jahr": "2021",
    "papier": "2021-be-gk",
    "datei": "hefte/2021-be-gk.pdf",  # Stark-Band Berlin GK (Band zum Abitur 2021, Jahrgang 2021 online), PDF mit Textebene, lokal (abi.md § 2)
    "seiten": 45,
    # Sollpunkte je Aufgabe aus der BE-Spalte; jede Aufgabe des Hefts muss hier
    # stehen (Vollständigkeit). Hilfsmittelfreier Teil (Aufgabe 1) als 1.1 bis 1.7
    # in Heftreihenfolge (Analysis 1–3, Geometrie 1–2, Stochastik 1–2, je 5 BE;
    # angeboten 35, bearbeitet 25 wie in der Sonderregelung 2022: drei
    # Analysis-Einheiten Pflicht plus zwei Geometrie oder zwei Stochastik). Teil B:
    # 2.1/2.2 Analysis je 45, 3 Geometrie 30, 4 Stochastik 30 – Geometrie und
    # Stochastik ohne Wahl; angeboten 185.
    "soll": {"1.1": 5, "1.2": 5, "1.3": 5, "1.4": 5, "1.5": 5, "1.6": 5, "1.7": 5,
             "2.1": 45, "2.2": 45, "3": 30, "4": 30},  # 2.2: Teilaufgaben summieren sich zu 45, der Band druckt „35“ – Druckfehler (abi-pruefungen.md § 4)
    "probe": False,
}

# ========================================= QUELLEN UND PRÜFUNG, NICHT ÄNDERN
KAT = "abi-katalog.csv"
TYP = "abitur-typen.csv"
VOKABULAR = "abitur-vokabular.md"
KERN = "katalog-prompt.md"
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]
# Kataloge der anderen Profile mit derselben Typenliste (Entscheidung 25): ihre
# ids gelten für beispiel_id und für „Dublette von:", ihre Typfelder zählen als
# Verwendung.
ANDERE_KATALOGE = ["iqb-katalog.csv"]

PFLICHT = ("id jahr papier block aufgabe titel teilaufgabe seite punkte hilfsmittel leitidee "
           "thema typ format operator antwort material skizze kontext textumfang gegeben gesucht "
           "verfahren schritte ergebnis niveau_geschaetzt fehlerquelle").split()

# Qualitätsschranke (abi.md § 7, wie iqb.md § 7). Anteile beziehen sich auf die
# Zeilen des Hefts; „mindestens" ist die Zahl, die immer erlaubt ist.
SCHWELLEN = {
    "fragezeichen_anteil": 0.10, "fragezeichen_mindestens": 2,
    "neue_typen_anteil": None, "neue_typen_ab_bestand": 100,
    "ersatzweise_anteil": 0.10, "ersatzweise_mindestens": 2,
    # Eichung gegen den amtlichen Bereich, ab dieser Zahl eigener gewerteter Zeilen
    # scharf; geerbte Schätzungen der Dubletten zählen nicht (v0.8).
    "eichung_mindestens": 0.85, "eichung_ab_zeilen": 10,
}

# Stämme, die eine ASCII-Umschrift von ä, ö, ü oder ß verraten. Positivliste,
# weil ein Mustertest auf ae|oe|ue|ss bei Koeffizient oder Quader fehlschlägt.
UMSCHRIFT = ("flaeche", "laenge", "naechst", "haeufig", "zufaell", "waehl", "aender", "aeusser",
 "gefaess", "verhaeltnis", "erklaer", "zaehl", "traeg", "gaeng", "maessig", "hoehe", "groesse",
 "groess", "loesung", "loes", "moegl", "koerper", "oeffn", "schoen", "pruef", "stueck",
 "kruemmung", "ueber", "fuer", "muess", "fuehr", "gueltig", "zurueck", "huelle", "schluessel",
 "urspruengl", "gross", "massstab", "masszahl", "schliess", "heisst", "weiss", "strasse",
 "gemaess", "fuss", "flaechen", "abstaend", "schaerfe", "raeum", "waehrend", "naeher",
 "gegenueber", "unabhaeng", "abhaeng", "zulaessig", "moeglich", "hoeher", "wuerfel", "erhoeh")
# Felder, die bewusst umlautfrei sind: Dateinamen und papier-Kürzel (abi.md § 4).
OHNE_UMLAUT = ("id", "papier", "abhaengig_von")
# Kennungen des Pools, wie sie in bemerkung zitiert werden (Dublette von: …).
KENNUNG = re.compile(r"(?:\d{4}|Beispielaufgaben)M(?:erhoeht|grundlegend)[AB]"
                     r"(?:Analysis|AGLAA1|AGLAA2|Stochastik)(?:WTR|CAS|MMS)?\d*(?:-\d*[a-z]?)?")
PAPIER = re.compile(r"(\d{4})-(be|bb|bebb)-(gk|lk|ea)(-(cas|mms))?")
AFB = re.compile(r"I{1,3}(?:\|I{1,3})*")
ORD = {"I": 1, "II": 2, "III": 3}


def lies(pfad):
    if not os.path.exists(pfad):
        sys.exit(f"{pfad} fehlt – Quelldatei neben das Skript legen.")
    return io.open(pfad, encoding="utf-8").read()


def liste_aus_klammer(text, feld, quelle):
    """'feld (a; b c; d)' -> {'a','b','d'} – erstes Wort je Teil."""
    m = re.search(r"\b" + re.escape(feld) + r" \(([^()]*)\)", text)
    if not m:
        sys.exit(f"{quelle}: Werteliste für {feld} nicht gefunden.")
    werte = {t.strip().split()[0] for t in m.group(1).split(";") if t.strip()}
    if not werte:
        sys.exit(f"{quelle}: Werteliste für {feld} ist leer.")
    return werte


def abschnitt(text, wort, quelle):
    """Abschnitt einer Markdown-Datei, dessen Überschrift (## …) das Wort enthält."""
    for teil in re.split(r"^## ", text, flags=re.M)[1:]:
        if wort in teil.splitlines()[0]:
            return teil
    sys.exit(f"{quelle}: Abschnitt „{wort}“ nicht gefunden.")


def vokabular():
    """Kopfzeile und Formvokabular aus dem Kern, Sachgebiete und Themen aus abitur-vokabular.md."""
    kern, profil = lies(KERN), lies(VOKABULAR)

    m = re.search(r"^Kopfzeile:\s*\n(id;.+)$", kern, re.M)
    if not m:
        sys.exit(f"{KERN}: Kopfzeile nicht gefunden.")
    head = m.group(1).strip().split(";")

    v = {feld: liste_aus_klammer(kern, feld, KERN)
         for feld in ("format", "antwort", "material", "zahlenraum",
                      "textumfang", "niveau_geschaetzt")}

    m = re.search(r"trägt das Sachgebiet:\s*\*\*(.+?)\*\*", profil, re.S)
    if not m:
        sys.exit(f"{VOKABULAR}: Sachgebiete nicht gefunden.")
    leitideen = [s.strip() for s in re.sub(r"\s+", " ", m.group(1)).split("·") if s.strip()]

    themen = {}
    for m in re.finditer(r"^\*\*([^*:]+):\*\*(.+?)(?=\n\s*\n)", profil, re.S | re.M):
        name = m.group(1).strip()
        if name not in leitideen:
            continue
        themen[name] = [s.strip() for s in re.sub(r"\s+", " ", m.group(2)).split("·") if s.strip()]
    fehlt = [l for l in leitideen if l not in themen]
    if fehlt:
        sys.exit(f"{VOKABULAR}: keine Themenzeile für {fehlt}")
    return head, v, leitideen, themen


def geltung():
    """Geltungstabelle aus abitur-vokabular.md § 3: Thema × Zielprüfung, ja/nein.
    Liefert (Zielprüfungen, {thema: Menge der Zielprüfungen mit ja})."""
    profil = abschnitt(lies(VOKABULAR), "Geltung", VOKABULAR)
    m = re.search(r"^\| Thema \|(.+?)\|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)", profil, re.M)
    if not m:
        sys.exit(f"{VOKABULAR}: Geltungstabelle nicht gefunden.")
    ziele = [z.strip() for z in m.group(1).split("|") if z.strip()]
    tab = {}
    for zeile in m.group(2).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != len(ziele) + 1:
            sys.exit(f"{VOKABULAR}: Geltungszeile hat {len(zellen)} Zellen: {zeile}")
        thema, werte = zellen[0], zellen[1:]
        if any(w not in ("ja", "nein") for w in werte):
            sys.exit(f"{VOKABULAR}: Geltung muss ja oder nein sein: {zeile}")
        tab[thema] = {z for z, w in zip(ziele, werte) if w == "ja"}
    alle = {t for liste in THEMEN.values() for t in liste}
    fehlt = sorted(alle - set(tab))
    if fehlt:
        sys.exit(f"{VOKABULAR}: Themen ohne Geltungszeile: {fehlt}")
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{VOKABULAR}: Geltungszeilen ohne Thema in der Liste: {fremd}")
    return ziele, tab


def klassen():
    """Gegenstandsklassen je Thema aus abitur-vokabular.md § 4 (Tabelle „Thema | Gegenstandsklassen").
    Liefert {thema: [Klasse, ...]}; Themen ohne Zeile führen keine Unterklasse."""
    profil = abschnitt(lies(VOKABULAR), "Gegenstandsklassen", VOKABULAR)
    m = re.search(r"^\| Thema \| Gegenstandsklassen \|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)",
                  profil, re.M)
    if not m:
        sys.exit(f"{VOKABULAR}: Tabelle der Gegenstandsklassen nicht gefunden.")
    tab = {}
    for zeile in m.group(1).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != 2:
            sys.exit(f"{VOKABULAR}: Klassenzeile hat {len(zellen)} Zellen: {zeile}")
        tab[zellen[0]] = [k.strip() for k in zellen[1].split("·") if k.strip()]
    alle = {t for liste in THEMEN.values() for t in liste}
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{VOKABULAR}: Klassenzeilen ohne Thema in der Liste: {fremd}")
    return tab


def handlungen():
    """Handlung je format-Wert aus dem Kern § 5 (Tabelle „format | Handlung"; bis Kern v0.3 in
    abitur-vokabular.md § 5)."""
    kern = abschnitt(lies(KERN), "Felder", KERN)
    m = re.search(r"^\| format \| Handlung \|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)", kern, re.M)
    if not m:
        sys.exit(f"{KERN}: Tabelle der Handlungen nicht gefunden.")
    tab = {}
    for zeile in m.group(1).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != 2:
            sys.exit(f"{KERN}: Handlungszeile hat {len(zellen)} Zellen: {zeile}")
        tab[zellen[0]] = zellen[1]
    fehlt = sorted(VOK["format"] - set(tab))
    if fehlt:
        sys.exit(f"{KERN}: format-Werte ohne Handlung: {fehlt}")
    return tab


def klasse_von(typ):
    """Gegenstandsklasse aus dem Typnamen (Wort vor dem Doppelpunkt) oder leer."""
    m = re.match(r"([^:]+): ", typ)
    return m.group(1) if m else ""


def pruefe_typname(typ, thema, a, wo):
    """Präfixregel abitur-vokabular.md § 4: Themen mit Klassen verlangen ein gültiges Präfix, andere keins."""
    k = klasse_von(typ)
    if thema in KLASSEN:
        a(k in KLASSEN[thema],
          f"{wo}: Typ „{typ}“ braucht ein Präfix aus {KLASSEN[thema]} (Thema {thema})")
    else:
        a(k == "", f"{wo}: Typ „{typ}“ trägt ein Präfix, Thema {thema} führt keine Klassen")


# typ → (leitidee, thema) aus abitur-typen.csv und NEUE_TYPEN; füllt main(). Seit v0.4
# (Lauf 13) trägt jede Zeile leitidee und thema ihres Typs, der Schnitt liest sie hier.
TYP_THEMA = {}


def pruefe_thema(z, a):
    """Zeilenthema = Typthema (abitur-vokabular.md § 4, Entscheidung 16.09.2026)."""
    if z["typ"] in TYP_THEMA:
        a(TYP_THEMA[z["typ"]] == (z["leitidee"], z["thema"]),
          f"{z['id']}: leitidee/thema ({z['leitidee']}, {z['thema']}) weichen vom Typ ab "
          f"{TYP_THEMA[z['typ']]}")


def niveau_von(papier):
    """Niveau aus dem papier-Kürzel: gk, lk oder ea (abi.md § 4)."""
    m = PAPIER.fullmatch(papier)
    return m.group(3) if m else ""


def ziele_von(papier):
    """Zielprüfungen, gegen die ein Heft gemessen wird (abitur-vokabular.md § 3, Entscheidung
    des Lehrers 16.09.2026): be-gk → be-gk, be-lk → be-lk, bb-ea → bb-ea; gemeinsame Hefte
    bebb-gk → be-gk und bb-gk, bebb-lk → be-lk und bb-ea. Eine Zeile liegt in der Geltung des
    Hefts, wenn ihr Thema in mindestens einer dieser Spalten gilt; der Bericht nennt beide."""
    m = PAPIER.fullmatch(papier)
    if not m:
        return []
    land, niveau = m.group(2), m.group(3)
    if land == "bebb":
        return ["be-gk", "bb-gk"] if niveau == "gk" else ["be-lk", "bb-ea"]
    return [f"{land}-{niveau}"]


def in_geltung(z, ziele=None):
    """True, wenn das Thema der Zeile in mindestens einer Zielprüfung ihres Hefts gilt."""
    ziele = ziele or ziele_von(z["papier"])
    return any(ziel in GELTUNG.get(z["thema"], set()) for ziel in ziele)


HEAD, VOK, LEITIDEEN, THEMEN = vokabular()
ZIELE, GELTUNG = geltung()
KLASSEN = klassen()
HANDLUNG = handlungen()

# ======================================================== AB HIER JE HEFT
ZEILEN = []


def row(**kw):
    z = {k: "" for k in HEAD}
    z.update(jahr=KONFIG["jahr"], papier=KONFIG["papier"], stern="")
    unbekannt = set(kw) - set(HEAD)
    if unbekannt:
        sys.exit(f"unbekanntes Feld: {sorted(unbekannt)}")
    z.update(kw)
    if not z["hilfsmittel"]:
        z["hilfsmittel"] = "nein" if z["block"] == "A" else "ja"
    ZEILEN.append(z)


# ============================================================ ZEILEN JE HEFT
# Heft 2021-be-gk (Stark-Band zum Abitur 2021, Berlin Grundkurs, Jahrgang 2021
# online; 45 Seiten A5 mit Tipps und Verlagslösungen, Textebene; Auftrag B,
# 17.09.2026). Aufbau wie die Sonderjahrgänge 2022/2023 (185 BE angeboten: 7 × 5,
# 45, 45, 30, 30). Pool 2021 grundlegend: Teil A erfasst (Analysis 1 = Analysis
# 1.2 wortgleich), Teil B Reserve (3 Holzkörper = AG/LA (A2) WTR 1 zu sechs von
# neun Teilaufgaben, 4 Smartphone-Spiel = Stochastik WTR 2 zu vier wortgleichen
# und zwei abgewandelten von neun – Vormerkungen). Landesaufgaben: Analysis 2, 3,
# Geometrie 1, 2, Stochastik 1, 2 (Teil A), 2.1 Turbinenschaufel, 2.2
# Flugzeugflügel, 3 b, e, f, 4 b, e, f. Verlagslösungen sind kein
# Erwartungshorizont: ergebnis ohne „amtlich“, afb_amtlich der Landeszeilen leer.
# ---- Aufgabe 1: hilfsmittelfreier Teil (Seiten 1–3), 7 × 5 BE
A2_SK = "Graph einer Funktion f mit den markierten Punkten A (links, auf der x-Achse, Stelle x_A < 0), B (Hochpunkt bei x_B), C (auf dem fallenden Ast bei x_C < 0), D (rechts unten, unterhalb der x-Achse bei x_D > 0); der Graph verläuft von A über B und C oberhalb der x-Achse, schneidet sie rechts von C und fällt zu D; Stellen x_A, x_B, x_C, x_D auf der x-Achse markiert"
row(id="2021-be-gk-A1.2a", block="A", aufgabe="1.2", titel="Analysis 2", teilaufgabe="a", seite="1", punkte="3",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Vorzeichen der Ableitung an vorgegebenen Stellen aus dem Funktionsgraphen angeben", typ_neben="",
    stichwoerter="x_A: steigend, f' positiv|x_B: Hochpunkt, f' null|x_C: fallend, f' negativ",
    voraussetzungen="Ableitung als Steigung des Graphen",
    format="Tabelle", operator="Geben Sie an", antwort="Tabelle",
    material="Koordinatensystem", skizze=A2_SK, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung des Graphen einer Funktion f mit den Punkten A, B, C, D auf dem Graphen; Tabelle mit den Stellen x_A, x_B, x_C",
    gesucht="ob f'(x) an den drei Stellen positiv, negativ oder null ist",
    verfahren="Steigungsverhalten des Graphen an den Stellen ablesen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f'(x_A) positiv, f'(x_B) = 0 (Hochpunkt), f'(x_C) negativ",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Funktionswerte statt Steigungen beurteilen (f(x_C) > 0, aber f'(x_C) < 0)",
    bemerkung="Landesaufgabe (nicht im Pool 2021). Eigene Lösung; Verlagslösung stimmt überein.")
row(id="2021-be-gk-A1.2b", block="A", aufgabe="1.2", titel="Analysis 2", teilaufgabe="b", seite="1", punkte="2",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Aussage über zwei Integrale über die Lage des Graphen zur x-Achse beurteilen", typ_neben="",
    stichwoerter="I₁ über [x_A; x_C]: Graph oberhalb der x-Achse, I₁ > 0|I₂ über [x_C; x_D]: größtenteils unterhalb, I₂ < 0|I₁ > I₂, Aussage falsch",
    voraussetzungen="Integral als Flächenbilanz mit Vorzeichen",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=A2_SK, kontext="ohne", textumfang="kurz",
    gegeben="Graph von f wie in a; I₁ = Integral von x_A bis x_C über f, I₂ = Integral von x_C bis x_D über f; Aussage I₁ < I₂",
    gesucht="Entscheidung, ob die Aussage wahr ist, mit Begründung",
    verfahren="Vorzeichen der Integrale aus der Lage des Graphen zur x-Achse",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Falsch: I₁ > 0 (Graph über der x-Achse), I₂ < 0 (Flächenbilanz überwiegend unter der x-Achse), also I₁ > I₂",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Integrale als Flächeninhalte ohne Vorzeichen vergleichen",
    bemerkung="Landesaufgabe. Enge Fassung: Deutung des Integrals als Bilanz, ein Schluss – II. Eigene Lösung.")
row(id="2021-be-gk-A1.3a", block="A", aufgabe="1.3", titel="Analysis 3", teilaufgabe="a", seite="2", punkte="2",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen", typ_neben="",
    stichwoerter="f'(x) = 3x² − 6x, f'(2) = 0|f''(x) = 6x − 6, f''(2) = 6 ≠ 0",
    voraussetzungen="notwendige und hinreichende Bedingung",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze="Graph von f (Hochpunkt links der y-Achse, Tiefpunkt bei x = 2 auf der x-Achse) mit einem Punkt P(x | f(x)) für 0 < x < 2 und dem achsenparallelen Rechteck zwischen Ursprung und P", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − 3x² + 4",
    gesucht="Nachweis, dass x_E = 2 eine der beiden Extremstellen ist",
    verfahren="f'(2) = 0 und f''(2) ≠ 0 (oder Vorzeichenwechsel von f' = 3x(x − 2))",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f'(2) = 12 − 12 = 0 und f''(2) = 6 > 0: Extremstelle (Tiefpunkt)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur f'(2) = 0 zeigen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2026-ga-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-A1.3b", block="A", aufgabe="1.3", titel="Analysis 3", teilaufgabe="b", seite="2", punkte="3",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Ausschluss einer Stelle als Maximalstelle einer Rechtecksfläche über die notwendige Bedingung nachweisen", typ_neben="",
    stichwoerter="A(x) = x · f(x) = x⁴ − 3x³ + 4x|A'(x) = 4x³ − 9x² + 4|A'(1) = −1 ≠ 0",
    voraussetzungen="Zielfunktion aufstellen|notwendige Bedingung für Extremstellen",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="Koordinatensystem", skizze="wie a: Rechteck zwischen Ursprung und P(x | f(x))", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − 3x² + 4; P(x | f(x)) mit 0 < x < 2 legt ein achsenparalleles Rechteck fest, dessen Flächeninhalt für genau ein x_max maximal ist",
    gesucht="Nachweis, dass x_max ≠ 1",
    verfahren="A(x) = x · f(x) ableiten und A'(1) ≠ 0 zeigen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="A'(1) = 4 − 9 + 4 = −1 ≠ 0, also ist 1 keine Extremstelle von A und x_max ≠ 1 (tatsächlich x_max ≈ 0,84)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="f'(1) statt A'(1) betrachten",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt (A' = 0 bei 0,843).")
row(id="2021-be-gk-A1.4a", block="A", aufgabe="1.4", titel="Geometrie 1", teilaufgabe="a", seite="2", punkte="1",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatenform einer Ebene aus der Normalenform durch Ausmultiplizieren angeben", typ_neben="",
    stichwoerter="n = (−5 | 2 | 8), p = (1 | 8 | 3)|n · p = −5 + 16 + 24 = 35|F: −5x + 2y + 8z = 35",
    voraussetzungen="Normalenform lesen|Skalarprodukt",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: 2x + y + 4z = 6; F: (x − (1 | 8 | 3)) · (−5 | 2 | 8) = 0",
    gesucht="Koordinatenform von F",
    verfahren="Skalarprodukt ausmultiplizieren",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="F: −5x + 2y + 8z = 35",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="das Skalarprodukt n · p mit falschem Vorzeichen übernehmen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-A1.4b", block="A", aufgabe="1.4", titel="Geometrie 1", teilaufgabe="b", seite="2", punkte="2",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="s: x = (1 | −4 | 2) + r · (0 | 8 | −2)|2 · 1 + (−4 + 8r) + 4 · (2 − 2r) = 6 für alle r",
    voraussetzungen="allgemeinen Geradenpunkt in die Koordinatengleichung einsetzen",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: 2x + y + 4z = 6; Gerade s: x = (1 | −4 | 2) + r · (0 | 8 | −2), r ∈ IR, liegt in F",
    gesucht="Nachweis, dass s auch in E liegt",
    verfahren="Koordinaten von s in E einsetzen; r fällt heraus",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="2 − 4 + 8r + 8 − 8r = 6 gilt für alle r, also liegt s in E (s ist die Schnittgerade von E und F)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur den Stützpunkt prüfen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2023-ea-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-A1.4c", block="A", aufgabe="1.4", titel="Geometrie 1", teilaufgabe="c", seite="2", punkte="2",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Ebene senkrecht zu zwei gegebenen Ebenen angeben", typ_neben="",
    stichwoerter="Richtungsvektor der Schnittgeraden s (0 | 8 | −2) ~ (0 | 4 | −1) als Normalenvektor|H: 4y − z = 0|alternativ Spannvektoren (2 | 1 | 4) und (−5 | 2 | 8)",
    voraussetzungen="Ebene senkrecht zu zwei Ebenen enthält beide Normalenvektoren",
    format="Kurzantwort", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: 2x + y + 4z = 6, F: −5x + 2y + 8z = 35, Schnittgerade s mit Richtungsvektor (0 | 8 | −2)",
    gesucht="Gleichung einer Ebene H senkrecht zu E und F",
    verfahren="Normalenvektor von H = Richtungsvektor von s, beliebiger Stützpunkt",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2021-be-gk-A1.4b",
    ergebnis="z. B. H: 4y − z = 0 (Normalenvektor (0 | 4 | −1)); oder H: x = r · (2 | 1 | 4) + s · (−5 | 2 | 8)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="eine zu E parallele Ebene angeben",
    bemerkung="Landesaufgabe. Enge Fassung: Zusammenhang Schnittgerade–Normalenvektor selbst herstellen – II. Eigene Rechnung, mit sympy bestätigt (Kreuzprodukt der Normalenvektoren ~ (0 | 4 | −1)).")
row(id="2021-be-gk-A1.5a", block="A", aufgabe="1.5", titel="Geometrie 2", teilaufgabe="a", seite="2", punkte="2",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen", typ_neben="",
    stichwoerter="1 + 3s = 4, 2 + 2t = 6, 3 + t − s = 4|s = 1, t = 2 erfüllt alle drei Gleichungen",
    voraussetzungen="LGS aus der Parameterform",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(4 | 6 | 4); E: x = (1 | 2 | 3) + t · (0 | 2 | 1) + s · (3 | 0 | −1), t, s ∈ IR",
    gesucht="Nachweis, dass P in E liegt",
    verfahren="Gleichsetzen, t und s aus zwei Gleichungen, dritte prüfen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="t = 2, s = 1 erfüllen alle drei Koordinatengleichungen, also P ∈ E",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die dritte Gleichung nicht prüfen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2026-ga-A); hier an der Parameterform. Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-A1.5b", block="A", aufgabe="1.5", titel="Geometrie 2", teilaufgabe="b", seite="2", punkte="3",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Gerade in einer Ebene durch einen Punkt parallel zu einer Koordinatenebene angeben", typ_neben="",
    stichwoerter="Richtungsvektor t · (0 | 2 | 1) + s · (3 | 0 | −1) mit z-Komponente 0 ⇔ t = s|z. B. (3 | 2 | 0)|g: x = (4 | 6 | 4) + v · (3 | 2 | 0)",
    voraussetzungen="Richtungsvektoren einer Ebene als Linearkombination|Parallelität zur xy-Ebene heißt z-Komponente 0",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(4 | 6 | 4) in E: x = (1 | 2 | 3) + t · (0 | 2 | 1) + s · (3 | 0 | −1); g liegt in E, geht durch P und hat keinen Schnittpunkt mit der xy-Ebene",
    gesucht="Gleichung von g",
    verfahren="Richtungsvektor in E mit z-Komponente 0 (t = s), Stützpunkt P",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2021-be-gk-A1.5a",
    ergebnis="g: x = (4 | 6 | 4) + v · (3 | 2 | 0), v ∈ IR (Richtungsvektor aus t = s = 1)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="einen Spannvektor von E als Richtungsvektor nehmen (schneidet die xy-Ebene)",
    bemerkung="Landesaufgabe. Enge Fassung: drei Bedingungen ohne Rechenschema in einen Ansatz übersetzen – III. Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-A1.6a", block="A", aufgabe="1.6", titel="Stochastik 1", teilaufgabe="a", seite="3", punkte="2",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeit eines Vergleichsereignisses beim Wurf zweier Würfel über die Ergebnistabelle nachweisen", typ_neben="",
    stichwoerter="36 Ergebnisse|blau > rot in 5 + 4 + 3 + 2 + 1 = 15 Fällen|15/36",
    voraussetzungen="Laplace-Wahrscheinlichkeit|systematisches Abzählen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Würfelspiel", textumfang="kurz",
    gegeben="Ein roter und ein blauer Laplace-Würfel (1 bis 6) werden gleichzeitig geworfen; Aussage P(blau > rot) = 15/36",
    gesucht="Begründung, dass die Aussage wahr ist",
    verfahren="Günstige Paare abzählen (bei rot = 1 fünf, rot = 2 vier, …)",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Von 36 gleich wahrscheinlichen Paaren sind 15 mit größerer blauer Augenzahl: P = 15/36",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="gleiche Augenzahlen mitzählen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2019-be-gk 4.2 b). Eigene Rechnung.")
row(id="2021-be-gk-A1.6b", block="A", aufgabe="1.6", titel="Stochastik 1", teilaufgabe="b", seite="3", punkte="3",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="P(X = 0) = 15/36, P(X = 1) = 6/36, P(X = 2) = 15/36|E(X) = 0 + 6/36 + 30/36 = 1",
    voraussetzungen="Verteilung aus dem Abzählen|Erwartungswert als gewichtete Summe",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Würfelspiel", textumfang="mittel",
    gegeben="Zwei Laplace-Würfel; X = 0, wenn rot < blau, X = 1 bei gleichen Augenzahlen, X = 2, wenn rot > blau; aus a P(blau > rot) = 15/36",
    gesucht="Erwartungswert von X",
    verfahren="Verteilung von X (15, 6, 15 von 36) und E(X) = Summe x · P(X = x)",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="2021-be-gk-A1.6a",
    ergebnis="E(X) = 0 · 15/36 + 1 · 6/36 + 2 · 15/36 = 1",
    zwischenergebnis="P(X = 1) = 6/36", niveau_geschaetzt="II",
    fehlerquelle="P(X = 2) = 21/36 (mit Gleichstand) ansetzen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-bb-ea). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-A1.7a", block="A", aufgabe="1.7", titel="Stochastik 2", teilaufgabe="a", seite="3", punkte="2",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Totale Wahrscheinlichkeit über die Pfadregeln nachweisen", typ_neben="",
    stichwoerter="6 weiße, 4 schwarze Kugeln, ohne Zurücklegen|P(W2) = 6/10 · 5/9 + 4/10 · 6/9 = 3/5",
    voraussetzungen="zweistufiges Baumdiagramm|Pfad- und Summenregel",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Auswahlverfahren / Urne", textumfang="mittel",
    gegeben="Urne mit 6 weißen und 4 schwarzen Kugeln; 10 Bewerber ziehen nacheinander ohne Zurücklegen, wer weiß zieht, ist ausgewählt",
    gesucht="Nachweis, dass der zweite Bewerber mit 60 % ausgewählt wird",
    verfahren="Beide Pfade zur zweiten weißen Ziehung addieren",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P = 6/10 · 5/9 + 4/10 · 6/9 = 30/90 + 24/90 = 3/5 = 60 %",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur den Pfad weiß–weiß rechnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2025-ga-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-A1.7b", block="A", aufgabe="1.7", titel="Stochastik 2", teilaufgabe="b", seite="3", punkte="3",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Gleiche Chance verschiedener Ziehungspositionen beim Ziehen ohne Zurücklegen begründen", typ_neben="",
    stichwoerter="P(W1) = 6/10|P(W3) über vier Pfade = 3/5|gleiche Chance|Symmetrie: jede Position zieht mit 60 % weiß",
    voraussetzungen="dreistufiges Baumdiagramm oder Symmetrieargument",
    format="Begründung|Rechnung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Auswahlverfahren / Urne", textumfang="kurz",
    gegeben="Urne wie a (6 weiße, 4 schwarze, ohne Zurücklegen)",
    gesucht="ob der erste oder der dritte Bewerber die größere Chance hat, mit Begründung",
    verfahren="P(W3) als Summe der vier Pfade (oder Symmetrie: die Ziehungsposition ist gleichgültig) mit P(W1) = 0,6 vergleichen",
    schritte="3", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="2021-be-gk-A1.7a",
    ergebnis="Beide haben dieselbe Chance 3/5: P(W3) = 6/10 · 5/9 · 4/8 + 2 · 6/10 · 4/9 · 5/8 + 4/10 · 3/9 · 6/8 = 3/5 = P(W1)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="annehmen, dass frühere Bewerber die Chance der späteren senken",
    bemerkung="Landesaufgabe. Enge Fassung: Entscheidung gegen die Intuition, eigener Ansatz über Pfade oder Symmetrie – III. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.1 Turbinenschaufel (Seiten 13–14), 45 BE, Landesaufgabe
TB = "f(x) = 1/12 x³ − x² + 3x und p(x) = −x² + 3,8x − 1,36, beide in IR; Graphen G_f und G_p (Parabel)"
TB_SK = "Abbildung 1 (Seite 14): Koordinatensystem x von 0 bis 6, y von 0 bis 3, Graph G_f (durch den Ursprung, Hochpunkt (2 | 8/3), Wendepunkt bei 4, Berührnullstelle bei 6) und Parabel G_p (Nullstellen 0,4 und 3,4, Scheitel (1,9 | 2,25)); grau die Querschnittsfläche der Turbinenschaufel zwischen G_f oben, G_p unten, x-Achse und der Geraden x = 4,5; 1 LE = 10 cm"
row(id="2021-be-gk-B2.1a", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="a", seite="13", punkte="2",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="p(0,4) = −0,16 + 1,52 − 1,36 = 0|p(3,4) = −11,56 + 12,92 − 1,36 = 0",
    voraussetzungen="Funktionswerte berechnen",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=TB,
    gesucht="Nachweis, dass G_p die x-Achse bei x₁ = 0,4 und x₂ = 3,4 schneidet",
    verfahren="Einsetzen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="p(0,4) = 0 und p(3,4) = 0",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Rechenfehler mit den Dezimalzahlen",
    bemerkung="Landesaufgabe (nicht im Pool 2021). Typ wiederverwendet (Lauf 1). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1b", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="b", seite="13", punkte="3",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstellen einer ganzrationalen Funktion durch Ausklammern und Faktorisieren berechnen", typ_neben="",
    stichwoerter="f(x) = 1/12 x (x² − 12x + 36) = 1/12 x (x − 6)²|x = 0 einfach, x = 6 doppelt",
    voraussetzungen="Ausklammern|p-q-Formel oder binomische Formel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=TB,
    gesucht="Nullstellen von f",
    verfahren="x ausklammern, quadratischen Faktor lösen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="x = 0 (einfach) und x = 6 (doppelt)",
    zwischenergebnis="x² − 12x + 36 = (x − 6)²", niveau_geschaetzt="II",
    fehlerquelle="die Nullstelle 0 beim Teilen durch x verlieren",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2022-bebb-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1c", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="c", seite="13", punkte="4",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen", typ_neben="",
    stichwoerter="f'(x) = 1/4 x² − 2x + 3, f'(2) = 0|f''(x) = 1/2 x − 2, f''(2) = −1 < 0|f(2) = 8/3",
    voraussetzungen="Ableitungen|hinreichende Bedingung",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=TB,
    gesucht="Nachweis, dass H(2 | 8/3) Hochpunkt von G_f ist",
    verfahren="f'(2) = 0, f''(2) < 0, f(2) = 8/3",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f'(2) = 1 − 4 + 3 = 0, f''(2) = −1 < 0, f(2) = 8/12 − 4 + 6 = 8/3: Hochpunkt",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Funktionswert nicht prüfen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2026-ga-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1d", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="d", seite="13", punkte="3",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendepunkte über die zweite Ableitung berechnen", typ_neben="",
    stichwoerter="f''(x) = 1/2 x − 2 = 0 ⇔ x = 4|f'''(x) = 1/2 ≠ 0|W(4 | 4/3)",
    voraussetzungen="zweite und dritte Ableitung",
    format="Rechnung", operator="Untersuchen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=TB,
    gesucht="ob G_f einen Wendepunkt besitzt",
    verfahren="f'' = 0 lösen, f''' ≠ 0",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Ja, genau einer: W(4 | 4/3)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="hinreichende Bedingung weglassen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2023-bebb-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1e", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="e", seite="13", punkte="5",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph und waagerechter Gerade zwischen zwei nachgewiesenen Schnittstellen berechnen", typ_neben="",
    stichwoerter="f(2) = f(8) = 8/3 = g|Integral von 2 bis 8 über (8/3 − f) = 9",
    voraussetzungen="Funktionswerte|Integral einer Differenz",
    format="Rechnung", operator="Zeigen Sie|Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=TB + "; Gerade g(x) = 8/3 und G_f haben zwei gemeinsame Punkte, keine weiteren Schnittpunkte (ohne Nachweis)",
    gesucht="Nachweis, dass die gemeinsamen Punkte bei x₃ = 2 und x₄ = 8 liegen; Inhalt der von g und G_f begrenzten Fläche",
    verfahren="f(2) und f(8) mit 8/3 vergleichen; Integral von 2 bis 8 über g − f",
    schritte="3", zahlenraum="Bruch", einheiten="FE", abhaengig_von="",
    ergebnis="f(2) = f(8) = 8/3; A = 9 FE",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Integral von f allein bilden (ohne die Gerade abzuziehen)",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1f", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="f", seite="13", punkte="4",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Abstand zweier Extrempunkte verschiedener Graphen mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="p'(x) = −2x + 3,8 = 0 ⇔ x = 1,9, p(1,9) = 2,25|d = √(0,1² + (8/3 − 2,25)²) = √661/60 ≈ 0,429 > 5/12 ≈ 0,417",
    voraussetzungen="Scheitel über die Ableitung|Abstand zweier Punkte",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=TB + "; Hochpunkt H(2 | 8/3) von G_f; der Scheitel von G_p ist ein Hochpunkt (ohne Nachweis)",
    gesucht="Nachweis, dass der Abstand der beiden Hochpunkte größer als 5/12 ist",
    verfahren="Scheitel von p über p' = 0, Abstand zu H berechnen und mit 5/12 vergleichen",
    schritte="3", zahlenraum="dezimal|Bruch|Wurzel", einheiten="", abhaengig_von="2021-be-gk-B2.1c",
    ergebnis="Scheitel S(1,9 | 2,25); d = √(0,01 + 25/144) = √661/60 ≈ 0,4285 > 5/12 ≈ 0,4167",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur die Differenz der y-Werte 5/12 als Abstand nehmen (dann gleich, nicht größer)",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1g", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="g", seite="13", punkte="6",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Monotonieintervalle und Wertebereich einer Differenzfunktion auf einem Intervall über die Ableitung ermitteln", typ_neben="",
    stichwoerter="d(x) = f(x) − p(x) = 1/12 x³ − 0,8x + 1,36|d'(x) = 1/4 x² − 0,8 = 0 ⇔ x = √3,2 ≈ 1,79|fallend auf [0,4; √3,2], steigend auf [√3,2; 3,4]|W = [d(√3,2); d(3,4)] ≈ [0,406; 1,915]",
    voraussetzungen="Differenzfunktion|Monotonie über das Vorzeichen der Ableitung|Randwerte",
    format="Rechnung", operator="Ermitteln Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=TB + "; auf 0,4 ≤ x ≤ 3,4 liegt G_f oberhalb von G_p; d(x) = f(x) − p(x) ist der senkrechte Abstand",
    gesucht="Intervalle, in denen d steigt bzw. fällt; Wertebereich von d",
    verfahren="d' = 0, Vorzeichen von d'; Minimum und Randwerte vergleichen",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="d fällt auf [0,4; √3,2] und steigt auf [√3,2; 3,4] (√3,2 ≈ 1,79); Wertebereich [d(√3,2); d(3,4)] ≈ [0,406; 1,915]",
    zwischenergebnis="d(0,4) ≈ 1,045", niveau_geschaetzt="II",
    fehlerquelle="das Maximum am linken Rand statt am rechten Rand annehmen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1h", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="h", seite="14", punkte="6",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen mit verschiedenen Grenzen als Differenz zweier Integrale berechnen", typ_neben="",
    stichwoerter="A = Integral von 0 bis 4,5 über f − Integral von 0,4 bis 3,4 über p|≈ 8,54 − 4,50 = 4,04 FE|1 FE = 100 cm²: ≈ 404 cm²",
    voraussetzungen="Nullstellen beider Graphen (a, b)|Integrale mit verschiedenen Grenzen|Maßstab",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=TB_SK, kontext="Wasserkraft / Turbinenschaufel", textumfang="mittel",
    gegeben=TB + "; Querschnittsfläche eingeschlossen von G_f, G_p, der x-Achse und x = 4,5 (Abbildung 1); 1 LE = 10 cm",
    gesucht="Flächeninhalt der Querschnittsfläche",
    verfahren="Fläche unter G_f von 0 bis 4,5 minus Fläche unter G_p zwischen den Nullstellen 0,4 und 3,4",
    schritte="4", zahlenraum="dezimal", einheiten="FE|cm²", abhaengig_von="2021-be-gk-B2.1a|2021-be-gk-B2.1b",
    ergebnis="A ≈ 4,04 FE ≈ 404 cm²",
    zwischenergebnis="Integral f 0..4,5 ≈ 8,54|Integral p 0,4..3,4 = 4,5", niveau_geschaetzt="III",
    fehlerquelle="beide Integrale über dieselben Grenzen bilden",
    bemerkung="Landesaufgabe. Enge Fassung: Zerlegung mit verschiedenen Grenzen aus der Abbildung selbst erkennen – III. Eigene Rechnung, mit sympy bestätigt (4,043).")
row(id="2021-be-gk-B2.1i", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="i", seite="14", punkte="3",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Gleiche Ableitungswerte zweier Funktionen nachweisen und als parallele Tangenten deuten", typ_neben="",
    stichwoerter="p'(0,4) = −0,8 + 3,8 = 3|f'(0) = 3|Tangenten an G_p in (0,4 | 0) und an G_f im Ursprung parallel",
    voraussetzungen="Ableitungswerte|Steigung als Tangentenanstieg",
    format="Rechnung|Begründung", operator="Weisen Sie nach|Erläutern Sie", antwort="Text",
    material="Koordinatensystem", skizze=TB_SK, kontext="Wasserkraft / Turbinenschaufel", textumfang="kurz",
    gegeben=TB,
    gesucht="Nachweis p'(0,4) = f'(0); anschauliche Bedeutung im Sachzusammenhang",
    verfahren="Ableitungen auswerten; gleiche Steigung heißt parallele Tangenten an den unteren Enden der Schaufel",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="p'(0,4) = 3 = f'(0); die Schaufelränder starten am unteren Ende mit gleicher Steigung (parallele Tangenten), die Schaufel hat dort gleichbleibende Dicke",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Gleichheit als gleichen Funktionswert deuten",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1j", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="j", seite="14", punkte="5",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen",
    typ_neben="Schnittwinkel zwischen Tangente und Gerade über die Anstiege berechnen",
    stichwoerter="f(3) = 9/4 = h(3)|h'(3) = 4/3, f'(3) = −3/4|Produkt −1: Schnittwinkel 90°|Gerade h in Abbildung 1 einzeichnen",
    voraussetzungen="Funktionswerte|Schnittwinkel über die Anstiege (tan-Formel oder Orthogonalität m₁ · m₂ = −1)",
    format="Rechnung|Zeichnen", operator="Zeigen Sie|Zeichnen Sie|Ermitteln Sie", antwort="Text|Grafik|Zahl",
    material="Koordinatensystem", skizze=TB_SK, kontext="Wasserkraft / Turbinenschaufel", textumfang="mittel",
    gegeben=TB + "; Bruchlinie h(x) = 4/3 x − 7/4",
    gesucht="Nachweis, dass h den Graphen G_f in P(3 | f(3)) schneidet; h einzeichnen; Schnittwinkel zwischen h und G_f in P",
    verfahren="f(3) = h(3); Gerade zeichnen; Anstiege f'(3) und 4/3 vergleichen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="°", abhaengig_von="",
    ergebnis="f(3) = h(3) = 9/4; f'(3) = −3/4 und h' = 4/3 mit Produkt −1, Schnittwinkel 90°",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Winkel der Geraden mit der x-Achse statt mit der Tangente berechnen",
    bemerkung="Landesaufgabe. Nebentyp wiederverwendet (2018-be-gk 1.2 b). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.1k", block="B", aufgabe="2.1", titel="Turbinenschaufel", teilaufgabe="k", seite="14", punkte="4",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Quadratische Funktion aus Nullstelle und Scheitelpunkt rekonstruieren", typ_neben="",
    stichwoerter="q(x) = ax² + bx (c = 0)|q(2) = 2,2, q'(2) = 0|a = −0,55, b = 2,2|q(x) = −0,55x² + 2,2x",
    voraussetzungen="Ansatz|LGS oder Scheitelpunktform",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Wasserkraft / Turbinenschaufel", textumfang="kurz",
    gegeben="Parabel q mit q(0) = 0 und Hochpunkt H_q(2 | 2,2) als neue untere Begrenzung",
    gesucht="Funktionsgleichung von q",
    verfahren="Ansatz ax² + bx, Bedingungen q(2) = 2,2 und q'(2) = 0",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="q(x) = −0,55x² + 2,2x = −0,55 (x − 2)² + 2,2",
    zwischenergebnis="4a + 2b = 2,2|4a + b = 0", niveau_geschaetzt="II",
    fehlerquelle="Scheitelpunktform ohne die Nullstellenbedingung ansetzen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.2 Flugzeugflügel (Seiten 22–23), 35 BE, Landesaufgabe
FL = "f(x) = (−1/10 x² + 2x) · e^(−0,1x) und h(x) = −3/4 x · e^(−0,1x), beide in IR; Graphen G und H"
FL_SK = "Abbildung 1 (Seite 22): Querschnitt des Flugzeugflügels als Fläche zwischen G (oben) und H (unten) von S₁ links bis S₂ rechts, mit der Verbindungslinie S₁S₂ und der Beschriftung „Länge des Flugzeugflügels“ als horizontaler Abstand; Abbildung 2 (Seite 23): S₁ und S₂ auf einer nahezu waagerechten Linie mit der x-Achse"
row(id="2021-be-gk-B2.2a", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="a", seite="22", punkte="4",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstelle und y-Achsenschnittpunkt eines Produkts mit e-Funktion angeben", typ_neben="",
    stichwoerter="−1/10 x² + 2x = 0 ⇔ x = 0 oder x = 20|f(0) = 0|Schnittpunkte (0 | 0) und (20 | 0)",
    voraussetzungen="Satz vom Nullprodukt|e-Faktor positiv",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FL,
    gesucht="Schnittpunkte von G mit den Koordinatenachsen",
    verfahren="Polynomfaktor null setzen; f(0)",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="N₁(0 | 0) (zugleich y-Achsenschnittpunkt) und N₂(20 | 0)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="x = 0 vergessen",
    bemerkung="Landesaufgabe (nicht im Pool 2021). Typ wiederverwendet (2024-bebb-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.2b", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="b", seite="22", punkte="2",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben", typ_neben="",
    stichwoerter="x → +∞: f → 0|x → −∞: −1/10 x² → −∞ und e^(−0,1x) → +∞, f → −∞",
    voraussetzungen="Dominanz der e-Funktion",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FL,
    gesucht="Verhalten von f für x → +∞ und x → −∞",
    verfahren="Grenzwertbetrachtung",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f(x) → 0 für x → +∞; f(x) → −∞ für x → −∞",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen des quadratischen Terms für x → −∞ übersehen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2023-bebb-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.2c", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="c", seite="22", punkte="1",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="f(0) = 0 = h(0)",
    voraussetzungen="Funktionswerte",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FL,
    gesucht="Nachweis des gemeinsamen Punkts S₁(0 | 0)",
    verfahren="Einsetzen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f(0) = 0 und h(0) = 0, also S₁(0 | 0) auf beiden Graphen",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="keine",
    bemerkung="Landesaufgabe. Eigene Rechnung.")
row(id="2021-be-gk-B2.2d", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="d", seite="22", punkte="6",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Lage und Art aller lokalen Extrempunkte bestimmen", typ_neben="",
    stichwoerter="f'(x) = (1/100 x² − 2/5 x + 2) · e^(−0,1x) = 0 ⇔ x² − 40x + 200 = 0|x = 20 ∓ 10√2|f'' vorgegeben: Hochpunkt (5,86 | 4,61), Tiefpunkt (34,14 | −1,59)",
    voraussetzungen="Produkt- und Kettenregel|p-q-Formel|hinreichende Bedingung mit gegebenem f''",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=FL + "; ohne Nachweis: f''(x) = (−1/1000 x² + 3/50 x − 3/5) · e^(−0,1x)",
    gesucht="Koordinaten und Art der lokalen Extrempunkte von G",
    verfahren="f' bilden, quadratische Gleichung lösen, f'' auswerten, Funktionswerte",
    schritte="6", zahlenraum="dezimal|Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="Hochpunkt H(20 − 10√2 | 20(√2 − 1) · e^(−2+√2)) ≈ H(5,86 | 4,61); Tiefpunkt T(20 + 10√2 | −20(√2 + 1) · e^(−2−√2)) ≈ T(34,14 | −1,59)",
    zwischenergebnis="f'(x) = (1/100 x² − 2/5 x + 2) · e^(−0,1x)", niveau_geschaetzt="II",
    fehlerquelle="Kettenregel beim Ableiten des e-Faktors vergessen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-be-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.2e", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="e", seite="22", punkte="3",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Existenz eines Wendepunkts aus Tiefpunkt und Grenzverhalten über eine Skizze begründen", typ_neben="",
    stichwoerter="h' hat genau eine Nullstelle x = 10 mit Vorzeichenwechsel − nach +: Tiefpunkt (h(10) < 0)|lim h = 0 für x → +∞|ohne Wendepunkt bliebe H linksgekrümmt und ginge gegen +∞: Widerspruch",
    voraussetzungen="Vorzeichenwechsel der Ableitung|Krümmung und Grenzverhalten",
    format="Begründung|Zeichnen", operator="Begründen Sie", antwort="Text|Grafik",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="h(x) = −3/4 x · e^(−0,1x) mit lim h = 0 (x → +∞), lim h = +∞ (x → −∞), h'(x) = (3/40 x − 3/4) · e^(−0,1x)",
    gesucht="Begründung mithilfe einer Skizze, dass H einen Wendepunkt besitzt",
    verfahren="Tiefpunkt bei x = 10 im IV. Quadranten; danach steigt H gegen 0 – ohne Krümmungswechsel unmöglich",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="H fällt bis zum Tiefpunkt T(10 | h(10)) und steigt danach gegen die x-Achse (Grenzwert 0); ein durchgehend linksgekrümmter Graph ginge gegen +∞, also muss H rechtsgekrümmt werden: Wendepunkt (bei x = 20)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="h'' berechnen statt zu begründen",
    bemerkung="Landesaufgabe. Enge Fassung: indirektes Argument aus Skizze, Monotonie und Grenzwert – III. Eigene Rechnung, mit sympy bestätigt (Tiefstelle 10).")
row(id="2021-be-gk-B2.2f", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="f", seite="22", punkte="5",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung im Ursprung aufstellen und Grenze einer Dreiecksfläche aus dem Flächeninhalt berechnen", typ_neben="",
    stichwoerter="h'(0) = −3/4, t(x) = −3/4 x|Dreieck unter t von 0 bis b: 3/8 b² = 75/2|b = 10",
    voraussetzungen="Tangente im Ursprung|Dreiecksfläche oder Integral|Wurzelziehen mit b > 0",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="h(x) = −3/4 x · e^(−0,1x); Tangente t an H im Schnittpunkt mit der x-Achse (Ursprung); t, x-Achse und x = b (b > 0) schließen eine Fläche von 75/2 FE ein",
    gesucht="b",
    verfahren="t(x) = h'(0) · x; Fläche 1/2 · b · |t(b)| = 3/8 b² = 75/2",
    schritte="3", zahlenraum="Bruch", einheiten="FE", abhaengig_von="2021-be-gk-B2.2c",
    ergebnis="t(x) = −3/4 x; b = 10",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen: Fläche unterhalb der x-Achse mit negativem Integral gleichsetzen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.2g", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="g", seite="22", punkte="4",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Schnittstellen zweier Graphen durch Lösen einer quadratischen Gleichung nachweisen", typ_neben="",
    stichwoerter="f = h ⇔ (−1/10 x² + 2x + 3/4 x) · e^(−0,1x) = 0|x (−1/10 x + 11/4) = 0 ⇔ x = 0 oder x = 27,5|Länge 27,5 dm",
    voraussetzungen="e-Faktor kürzen|Ausklammern",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=FL_SK, kontext="Flugzeugbau / Flügelprofil", textumfang="mittel",
    gegeben=FL + "; Querschnitt zwischen den Schnittpunkten S₁ und S₂ von G und H; 1 LE = 1 dm; Länge = horizontaler Abstand von S₁ und S₂",
    gesucht="Nachweis, dass die Länge 27,5 dm beträgt",
    verfahren="f(x) = h(x) lösen",
    schritte="3", zahlenraum="dezimal|Bruch", einheiten="dm", abhaengig_von="",
    ergebnis="Schnittstellen 0 und 27,5, Länge 27,5 dm; S₂(27,5 | f(27,5)) mit f(27,5) ≈ −1,32",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Nullstelle 0 beim Kürzen verlieren",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2019-ga-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B2.2h", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="h", seite="23", punkte="2",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Horizontalen Abstand zweier Punkte als kürzer als ihre Verbindungsstrecke begründen", typ_neben="",
    stichwoerter="Verbindungslinie ist Hypotenuse über dem horizontalen Abstand (Kathete)|Pythagoras: √(Δx² + Δy²) > Δx, da Δy ≠ 0",
    voraussetzungen="Satz des Pythagoras",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Skizze", skizze="Abbildung 2: S₁ und S₂ mit der Verbindungslinie, S₂ etwas unterhalb der x-Achse", kontext="Flugzeugbau / Flügelprofil", textumfang="kurz",
    gegeben="Länge des Flügels = horizontaler Abstand von S₁ und S₂; S₂ liegt unterhalb der x-Achse (Abbildung 2)",
    gesucht="Begründung ohne Rechnung, dass die Länge kürzer als die Verbindungslinie S₁S₂ ist",
    verfahren="Die Verbindungslinie ist die Hypotenuse eines rechtwinkligen Dreiecks mit dem horizontalen Abstand als Kathete",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Verbindungslinie ist Hypotenuse, der horizontale Abstand eine Kathete; da S₂ nicht auf der x-Achse liegt, ist die Kathete echt kürzer",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit gerechneten Werten statt mit einer Begründung antworten",
    bemerkung="Landesaufgabe. Elementargeometrische Begründung, deshalb Thema Abstände (Analytische Geometrie). Eigene Überlegung.")
row(id="2021-be-gk-B2.2i", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="i", seite="23", punkte="7",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen", typ_neben="",
    stichwoerter="d(x) = f(x) − h(x) = (−1/10 x² + 11/4 x) · e^(−0,1x)|d'(x) = (1/100 x² − 19/40 x + 11/4) · e^(−0,1x) = 0 ⇔ x² − 47,5x + 275 = 0|x ≈ 6,75 (40,75 außerhalb)|d(6,75) ≈ 7,13 < 7,15",
    voraussetzungen="Differenzfunktion|Produktregel|quadratische Gleichung|Vergleich mit der Vorgabe",
    format="Rechnung", operator="Untersuchen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Flugzeugbau / Flügelprofil", textumfang="mittel",
    gegeben=FL + "; d(x) = f(x) − h(x) beschreibt die vertikale Höhe des Flügels auf [0; 27,5]; die maximale Höhe darf 7,15 dm nicht überschreiten",
    gesucht="ob die Konstrukteure die Vorgabe beachtet haben",
    verfahren="d' = 0 lösen, die Stelle im Intervall wählen, d dort berechnen und mit 7,15 vergleichen",
    schritte="5", zahlenraum="dezimal", einheiten="dm", abhaengig_von="2021-be-gk-B2.2g",
    ergebnis="Maximale Höhe d(6,75) ≈ 7,13 dm < 7,15 dm: Vorgabe eingehalten",
    zwischenergebnis="d'(x) = 0 bei x ≈ 6,75 und 40,75", niveau_geschaetzt="II",
    fehlerquelle="die Lösung außerhalb des Intervalls verwenden",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-be-gk 1.1 g). Eigene Rechnung, mit sympy bestätigt (7,131 bei 6,748).")
row(id="2021-be-gk-B2.2j", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="j", seite="23", punkte="2",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen", typ_neben="",
    stichwoerter="A = D(27,5) − D(0) mit D(x) = (x² − 15/2 x − 75) · e^(−0,1x)|475 · e^(−2,75) + 75 ≈ 105,4 dm²",
    voraussetzungen="Hauptsatz mit vorgegebener Stammfunktion",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Flugzeugbau / Flügelprofil", textumfang="kurz",
    gegeben="d(x) = f(x) − h(x) auf [0; 27,5]; ohne Nachweis: D(x) = (x² − 15/2 x − 75) · e^(−0,1x) ist eine Stammfunktion von d",
    gesucht="Querschnittsfläche des Flügels",
    verfahren="Integral von 0 bis 27,5 über d mit D",
    schritte="2", zahlenraum="dezimal", einheiten="dm²", abhaengig_von="2021-be-gk-B2.2g",
    ergebnis="A = D(27,5) − D(0) = 475 · e^(−2,75) + 75 ≈ 105,4 FE (dm²)",
    zwischenergebnis="D(0) = −75", niveau_geschaetzt="I",
    fehlerquelle="D(0) = −75 als 0 behandeln (dann ≈ 30,4)",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2019-ga-A); hier mit vorgegebener Stammfunktion. Eigene Rechnung, mit sympy bestätigt (105,37; Stammfunktion D nachgeprüft).")
row(id="2021-be-gk-B2.2k", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="k", seite="23", punkte="3",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Rechenschritte zur Winkelbestimmung aus Höhen- und Horizontalabstand beurteilen und berichtigen", typ_neben="",
    stichwoerter="(1) f(27,5) ≈ −1,32: Betrag nehmen (vertikaler Abstand 1,32)|(2) sin α = 1,32 / √(27,5² + 1,32²) – Pluszeichen unter der Wurzel, Rundungszeichen|α ≈ 2,75°",
    voraussetzungen="Sinus im rechtwinkligen Dreieck|Pythagoras|Vorzeichen und Betrag",
    format="Begründung", operator="Beurteilen Sie|Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Flugzeugbau / Flügelprofil", textumfang="mittel",
    gegeben="Vorgelegte Schritte: (1) f(27,5) ≈ 1,32; (2) sin α = 1,32 / √(27,5² − 1,32²) ⇔ α ≈ 2,75°; gesucht ist der Neigungswinkel der Verbindungslinie S₁S₂ gegen die Horizontale",
    gesucht="Beurteilung jedes Teilschritts und Berichtigung fehlerhafter Schritte",
    verfahren="Schritt 1: f(27,5) ist negativ, gemeint ist der Betrag; Schritt 2: Hypotenuse √(27,5² + 1,32²), oder einfacher tan α = 1,32/27,5",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="°", abhaengig_von="2021-be-gk-B2.2g",
    ergebnis="(1) richtig als Betrag |f(27,5)| ≈ 1,32 (f ist negativ); (2) im Nenner muss + stehen (Pythagoras), Ergebnis α ≈ 2,75° bleibt; alternativ tan α = 1,32/27,5",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das Ergebnis 2,75° als Bestätigung der Schritte nehmen",
    bemerkung="Landesaufgabe. Enge Fassung: fremde Rechnung prüfen und berichtigen – III. Eigene Rechnung, mit sympy bestätigt (2,748°).")
row(id="2021-be-gk-B2.2l", block="B", aufgabe="2.2", titel="Flugzeugflügel", teilaufgabe="l", seite="23", punkte="6",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendepunkte über die zweite Ableitung berechnen",
    typ_neben="Winkel zwischen Sehne zum Wendepunkt und Verbindungslinie zweier Schnittpunkte über Steigungswinkel berechnen",
    stichwoerter="f'' = 0 ⇔ x² − 60x + 600 = 0 ⇔ x = 30 ∓ 10√3|x_R = 30 − 10√3 ≈ 12,68 (< 20), f(x_R) ≈ 2,61|tan β = 2,61/12,68, β ≈ 11,6°|δ = α + β ≈ 2,75° + 11,6° ≈ 14,4° < 18°",
    voraussetzungen="Wendestelle aus f''|Steigungswinkel über den Tangens|Winkel zusammensetzen",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Flugzeugbau / Flügelprofil", textumfang="lang",
    gegeben=FL + "; f''(x) = (−1/1000 x² + 3/50 x − 3/5) · e^(−0,1x); R(x_R | f(x_R)) mit x_R < 20 ist der Punkt, in dem G die Krümmungsart ändert; Kontrolle R(12,68 | 2,61); α ≈ 2,75° aus k",
    gesucht="Nachweis, dass der Winkel δ = ∠S₂S₁R höchstens 18° beträgt",
    verfahren="Wendestelle aus f'' = 0 (kleinere Lösung), Steigungswinkel der Sehne S₁R über den Tangens, δ als Summe mit dem Neigungswinkel der Linie S₁S₂",
    schritte="5", zahlenraum="dezimal|Wurzel", einheiten="°", abhaengig_von="2021-be-gk-B2.2k",
    ergebnis="R(30 − 10√3 | f(x_R)) ≈ R(12,68 | 2,61); β ≈ 11,6°, δ ≈ 14,4° < 18°",
    zwischenergebnis="x² − 60x + 600 = 0", niveau_geschaetzt="III",
    fehlerquelle="δ nur als β nehmen und α vergessen (S₂ liegt unter der x-Achse)",
    bemerkung="Landesaufgabe. Kontrollergebnis bestätigt. Enge Fassung: Winkel aus zwei Teilwinkeln in der Skizze zusammensetzen – III. Eigene Rechnung, mit sympy bestätigt (14,39°).")
# ---- Aufgabe 3 Holzkörper (Seiten 32–33), 30 BE – Pool 2021 grundlegend AG/LA (A2) WTR 1 (Reserve): a, c, d, g, h, i vorgemerkt; b, e, f Landes
HK = "Holzkörper mit den Eckpunkten A(0 | 0 | 0), B(10 | 0 | 0), C(10 | 10 | 0), D(0 | 10 | 0) und E(0 | 10 | 6) (Pyramide über dem Quadrat ABCD mit Spitze E senkrecht über D); B, D, E liegen in der Symmetrieebene; 1 LE = 1 cm"
HK_SK = "Schrägbild (Seite 32): Koordinatensystem mit Quadrat ABCD in der xy-Ebene und der Spitze E über D, Kanten AE, BE, CE, DE; Dreieck BCE als Seitenfläche"
row(id="2021-be-gk-B3a", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="a", seite="32", punkte="5",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen",
    typ_neben="Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen",
    stichwoerter="BC = (0 | 10 | 0), CE = (−10 | 0 | 6), Skalarprodukt 0: rechter Winkel bei C|A_BCE = 1/2 · 10 · √136 = 10√34|A_CDE = 1/2 · 10 · 6 = 30|O = 100 + 2 · 10√34 + 2 · 30 ≈ 276,6 cm²",
    voraussetzungen="Skalarprodukt|Flächen rechtwinkliger Dreiecke|Symmetrie des Körpers",
    format="Rechnung", operator="Zeigen Sie|Berechnen Sie", antwort="Text|Zahl",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="mittel",
    gegeben=HK,
    gesucht="Nachweis, dass BCE rechtwinklig ist; Inhalt der Gesamtoberfläche",
    verfahren="Skalarprodukt BC · CE = 0; Oberfläche aus Quadrat, zwei Dreiecken BCE/ABE (symmetrisch) und zwei Dreiecken CDE/ADE",
    schritte="4", zahlenraum="Wurzel|dezimal", einheiten="cm|cm²", abhaengig_von="",
    ergebnis="BC · CE = 0, rechter Winkel bei C; O = 160 + 20√34 ≈ 276,6 cm²",
    zwischenergebnis="|CE| = √136", niveau_geschaetzt="II",
    fehlerquelle="die Dreiecke ABE und ADE vergessen (nur drei Flächen zählen)",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBAGLAA2WTR1-1a. Wortgleich mit der Poolaufgabe 2021 grundlegend AG/LA (A2) WTR 1 a bis auf „Gesamtoberfläche“ statt „Oberfläche“ (Reserve-Stapel 2021-ga-B). Typen aus dem Bestand (2026-ga-A, 2024-ea-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B3b", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="b", seite="32", punkte="3",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Geradengleichung durch zwei Punkte aufstellen und windschiefe Lage begründen", typ_neben="",
    stichwoerter="h: x = (10 | 10 | 0) + r · (−10 | 0 | 6)|BD liegt in der xy-Ebene, h trifft sie nur in C, C ∉ BD|nicht parallel, kein Schnittpunkt: windschief",
    voraussetzungen="Parameterform|Lage zweier Geraden",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Term|Text",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=HK,
    gesucht="Gleichung der Geraden h durch C und E; Begründung, dass h windschief zur Geraden BD ist",
    verfahren="Richtungsvektor CE; h schneidet die xy-Ebene nur in C, das nicht auf BD liegt, und ist nicht parallel zu BD",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="h: x = (10 | 10 | 0) + r · (−10 | 0 | 6), r ∈ IR; windschief, weil h die xy-Ebene (mit BD) nur in C durchstößt, C nicht auf BD liegt und die Richtungsvektoren nicht kollinear sind",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur „kein Schnittpunkt“ zeigen und die Parallelität nicht ausschließen",
    bemerkung="Landesaufgabe (nicht im Pool: der Pool hat diese Teilaufgabe nicht). Typ wiederverwendet (2018-ga-B). Eigene Rechnung.")
row(id="2021-be-gk-B3c", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="c", seite="32", punkte="3",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="n = BC × CE = (60 | 0 | 100) ~ (3 | 0 | 5)|B einsetzen: 3 · 10 = 30|L: 3x + 5z = 30",
    voraussetzungen="Kreuzprodukt oder Ansatz|Punkt einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=HK + "; Kontrollergebnis L: 3x + 5z = 30",
    gesucht="Koordinatenform der Ebene L durch B, C, E",
    verfahren="Normalenvektor aus dem Kreuzprodukt der Kantenvektoren, d aus B",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="L: 3x + 5z = 30",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="y-Koeffizient ungleich null vermuten (L ist parallel zur y-Achse)",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBAGLAA2WTR1-1b. Wortgleich mit der Poolaufgabe b (Reserve-Stapel 2021-ga-B). Typ wiederverwendet (2018-ea-A). Kontrollergebnis bestätigt (sympy).")
row(id="2021-be-gk-B3d", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="d", seite="32", punkte="2",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="cos α = |(3 | 0 | 5) · (0 | 0 | 1)| / √34 = 5/√34|α ≈ 31,0°",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=HK + "; L: 3x + 5z = 30 (Seitenfläche BCE), Grundfläche in der xy-Ebene",
    gesucht="Winkel zwischen Grundfläche und Seitenfläche BCE",
    verfahren="Kosinus des Winkels der Normalenvektoren (3 | 0 | 5) und (0 | 0 | 1)",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2021-be-gk-B3c",
    ergebnis="α = arccos(5/√34) ≈ 31,0°",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Winkel zwischen Normalenvektor und Ebene (Komplement) angeben",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBAGLAA2WTR1-1c. Wortgleich mit der Poolaufgabe c (Reserve-Stapel 2021-ga-B). Typ wiederverwendet (2026-ea-B). Eigene Rechnung, mit sympy bestätigt (30,96°).")
row(id="2021-be-gk-B3e", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="e", seite="32", punkte="4",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Halbierung eines Quadrats durch gegebene Ebenen entscheiden und begründen", typ_neben="",
    stichwoerter="E₁: y = 5 Mittelparallele, halbiert|E₂: −x + y = 0 enthält die Diagonale AC, halbiert|E₃: z = 5 parallel zur xy-Ebene, schneidet das Quadrat nicht",
    voraussetzungen="Lage einfacher Ebenen|Symmetrien des Quadrats",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="mittel",
    gegeben="Quadrat ABCD mit A(0 | 0 | 0), B(10 | 0 | 0), C(10 | 10 | 0), D(0 | 10 | 0); Ebenen E₁: y = 5, E₂: −x + y = 0, E₃: z = 5",
    gesucht="für jede Ebene, ob sie das Quadrat in zwei flächengleiche Figuren teilt",
    verfahren="Schnittmenge jeder Ebene mit dem Quadrat bestimmen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="E₁ ja (Mittelparallele durch die Kantenmitten), E₂ ja (Diagonale AC), E₃ nein (schneidet die xy-Ebene nicht)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="E₂ als Ebene durch B und D lesen",
    bemerkung="Landesaufgabe (nicht im Pool). Eigene Überlegung; Verlagslösung stimmt überein.")
row(id="2021-be-gk-B3f", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="f", seite="32", punkte="3",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Eckpunkte eines gleichschenkligen Trapezes aus einem Flächenverhältnis zum Quadrat bestimmen", typ_neben="",
    stichwoerter="A'(0 | λ | 0), D'(0 | 10 − λ | 0)|A = 1/2 · (10 + 10 − 2λ) · 10 = 100 − 10λ = 80|λ = 2: A'(0 | 2 | 0), D'(0 | 8 | 0)",
    voraussetzungen="Trapezformel|Symmetrie|Gleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben="Quadrat ABCD (Seite 10); A und D werden auf der y-Achse symmetrisch verschoben, sodass ein gleichschenkliges Trapez A'BCD' mit 4/5 der Quadratfläche entsteht, A' und D' auf der Strecke AD",
    gesucht="Koordinaten von A' und D'",
    verfahren="Ansatz mit λ, Trapezfläche gleich 80",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="A'(0 | 2 | 0), D'(0 | 8 | 0)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Verschiebung nur auf einer Seite ansetzen (kein gleichschenkliges Trapez)",
    bemerkung="Landesaufgabe (nicht im Pool). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B3g", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="g", seite="32", punkte="4",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Rechenweg für die kürzeste Linie über eine Kante aus Lotfußpunkt und Symmetrie erläutern", typ_neben="",
    stichwoerter="P(10 − 10t | 10t | 6t) allgemeiner Punkt der Kante BE|PC · PB = 0: kürzeste Strecke von C zur Kante steht senkrecht, t = 25/59|2 · |PC| ≈ 15,2 wegen der Symmetrie (|AP| = |PC|)",
    voraussetzungen="Parametrisierung einer Kante|Orthogonalität für den kürzesten Abstand|Symmetrieebene",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="mittel",
    gegeben=HK + "; vorgelegter Rechenweg für die kürzeste Linie von A über die Kante BE nach C: P(10 − 10t | 10t | 6t); PC · PB = 0 mit t = 25/59; 2 · |PC| ≈ 15,2",
    gesucht="Erläuterung des Vorgehens",
    verfahren="Die drei Schritte deuten: Kantenpunkt parametrisieren, Lotbedingung, Verdopplung aus der Symmetrie",
    schritte="0", zahlenraum="Bruch|dezimal", einheiten="cm", abhaengig_von="",
    ergebnis="P ist ein allgemeiner Punkt der Kante BE; die Verbindung PC ist am kürzesten, wenn sie senkrecht auf BE steht (Skalarprodukt mit PB null), das liefert t = 25/59; wegen der Symmetrieebene durch B, D, E ist |AP| = |PC|, also Gesamtlänge 2 · |PC| ≈ 15,2 cm",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die Verdopplung nicht mit der Symmetrie begründen",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBAGLAA2WTR1-1d. Wortgleich mit der Poolaufgabe d (Reserve-Stapel 2021-ga-B). Enge Fassung: fremden Lösungsweg mit Begründung deuten – III. Eigene Rechnung, mit sympy bestätigt (15,18).")
row(id="2021-be-gk-B3h", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="h", seite="33", punkte="2",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen", typ_neben="",
    stichwoerter="F(0 | 0 | 6) Schnittpunkt von L mit der z-Achse|Spurgerade in der xz-Ebene durch B und F|Spurgerade in der yz-Ebene z = 6 durch F und E",
    voraussetzungen="Achsenschnittpunkt aus der Koordinatengleichung|Spurgeraden zeichnen",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=HK + "; L: 3x + 5z = 30; F = Schnittpunkt von L mit der z-Achse",
    gesucht="F und die Schnittgeraden von L mit der xz- und der yz-Ebene in die Abbildung einzeichnen",
    verfahren="F aus x = y = 0; Spurgeraden durch B und F bzw. F und E",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2021-be-gk-B3c",
    ergebnis="F(0 | 0 | 6); Spurgerade in der xz-Ebene BF, in der yz-Ebene die Gerade FE (z = 6)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="F auf der falschen Höhe eintragen",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBAGLAA2WTR1-1e. Wortgleich mit der Poolaufgabe e (Reserve-Stapel 2021-ga-B). Typ wiederverwendet (2017-ea-A). Eigene Lösung.")
row(id="2021-be-gk-B3i", block="B", aufgabe="3", titel="Holzkörper", teilaufgabe="i", seite="33", punkte="4",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumenverhältnis zweier Körper über Formeln ohne Zahlenwerte ermitteln", typ_neben="",
    stichwoerter="ABCDE Pyramide: 1/3 · |AB|² · |DE||ABCDEF Prisma mit Dreieck CDE: 1/2 · |AB|² · |DE||Verhältnis 3/2: um 50 % größer",
    voraussetzungen="Pyramiden- und Prismenvolumen|Verhältnis bilden",
    format="Rechnung|Begründung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=HK_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=HK + "; F(0 | 0 | 6); Körper ABCDEF (Prisma) und ABCDE (Pyramide)",
    gesucht="um wie viel Prozent das Volumen von ABCDEF größer ist als das von ABCDE, ohne konkrete Volumina",
    verfahren="Beide Volumenformeln mit denselben Größen aufstellen und dividieren",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="V_Prisma / V_Pyramide = (1/2) / (1/3) = 3/2: um 50 % größer",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Volumina mit Zahlen berechnen (200 und 300) statt allgemein",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBAGLAA2WTR1-1f. Wortgleich mit der Poolaufgabe f (Reserve-Stapel 2021-ga-B). Enge Fassung: Verhältnis über Formeln allgemein herleiten – III. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 4 Smartphone-Spiel (Seiten 40–41), 30 BE – Pool 2021 grundlegend Stochastik WTR 2 (Reserve): c, g, h, i wortgleich, a, d abgewandelt; b, e, f Landes
SM = "Smartphone-Spiel: jeden Sonntag zehn Versuche, je Versuch mit 40 % ein Stern; X = Anzahl der Sterne bei zehn Versuchen, binomialverteilt (n = 10, p = 0,4)"
SM2 = "Bonuspunkte beim täglichen Start: 10 mit 50 %, 20 mit 40 %, 50 mit 10 %"
row(id="2021-be-gk-B4a", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="a", seite="40|41", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", typ_neben="",
    stichwoerter="P(X > 6) = 1 − P(X ≤ 6) = 1 − 0,9452 = 0,0548|P(5 ≤ X ≤ 8) = P(X ≤ 8) − P(X ≤ 4) = 0,9983 − 0,6331 = 0,3652",
    voraussetzungen="Tabelle der summierten Binomialverteilung n = 10 (Anlage)",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Anlage Seite 41: Tabelle der summierten Binomialverteilung für n = 10 (p = 0,05 bis 0,5)", kontext="Smartphone-Spiel", textumfang="mittel",
    gegeben=SM + "; Tabelle in der Anlage",
    gesucht="P(A): mehr als sechs Sterne; P(B): mindestens fünf, höchstens acht Sterne",
    verfahren="Kumulierte Werte aus der Tabelle kombinieren",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(A) ≈ 0,055 (5,5 %); P(B) ≈ 0,365 (36,5 %)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≤ 5) statt P(X ≤ 4) abziehen",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2021MgrundlegendBStochastikWTR2-1a; das Heft fragt zusätzlich nach B (mindestens fünf, höchstens acht Sterne), der Pool nur nach mehr als sechs. Reserve-Stapel 2021-ga-B. Typ wiederverwendet (2019-be-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B4b", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="b", seite="40", punkte="3",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit für zwei unabhängige Spieler als Produkt binomialer Wahrscheinlichkeiten berechnen", typ_neben="",
    stichwoerter="P(X > 4) = 1 − 0,6331 = 0,3669|zwei Spieler unabhängig: 0,3669² ≈ 0,135",
    voraussetzungen="kumulierte Wahrscheinlichkeit aus der Tabelle|Produktregel für unabhängige Spieler",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle wie in a", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=SM + "; zwei Spieler machen je zehn Versuche",
    gesucht="Wahrscheinlichkeit, dass jeder der beiden mehr als vier Sterne gewinnt",
    verfahren="P(X > 4) für einen Spieler, dann quadrieren",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,3669² ≈ 0,135 (13,5 %)",
    zwischenergebnis="P(X > 4) ≈ 0,3669", niveau_geschaetzt="II",
    fehlerquelle="mit 20 Versuchen eines Spielers rechnen",
    bemerkung="Landesaufgabe (nicht im Pool). Eigene Rechnung, mit sympy bestätigt (0,1346).")
row(id="2021-be-gk-B4c", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="c", seite="40", punkte="2",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen", typ_neben="",
    stichwoerter="Sonntage sind unabhängig|frühere Ergebnisse ändern die Wahrscheinlichkeit nicht|Aussage falsch",
    voraussetzungen="Unabhängigkeit von Wiederholungen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=SM + "; Aussage eines Spielers: nach dreimal acht Sternen sei die Chance auf acht Sterne an diesem Sonntag deutlich kleiner",
    gesucht="Beurteilung der Aussage",
    verfahren="Unabhängigkeit der Sonntage",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Falsch: die Versuche der Sonntage sind unabhängig, die Wahrscheinlichkeit für acht Sterne bleibt gleich",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit der Seltenheit von viermal acht Sternen argumentieren",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBStochastikWTR2-1b. Wortgleich mit der Poolaufgabe b (Reserve-Stapel 2021-ga-B). Typ wiederverwendet (2017-ea-A). Eigene Überlegung.")
row(id="2021-be-gk-B4d", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="d", seite="40", punkte="3",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Fehlerwahrscheinlichkeit einer Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden", typ_neben="",
    stichwoerter="P(X = 5) = 0,8338 − 0,6331 = 0,2007|Y = Anzahl der Spieler mit genau fünf Sternen, n = 4|P(Y = 2) = 6 · 0,2007² · 0,7993² ≈ 0,154",
    voraussetzungen="Einzelwahrscheinlichkeit aus der Tabelle|zweite Binomialverteilung mit n = 4",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle wie in a", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=SM + "; vier Spieler machen je zehn Versuche",
    gesucht="Wahrscheinlichkeit, dass genau zwei der vier Spieler jeweils genau fünf Sterne gewinnen",
    verfahren="P(X = 5) als Trefferwahrscheinlichkeit einer Binomialverteilung mit n = 4",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P ≈ 0,154 (15,4 %)",
    zwischenergebnis="P(X = 5) ≈ 0,2007", niveau_geschaetzt="II",
    fehlerquelle="P(X = 5)² ohne Binomialkoeffizient und Gegenwahrscheinlichkeit",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2021MgrundlegendBStochastikWTR2-1c; das Heft sagt „genau zwei der vier Spieler jeweils genau fünf Sterne“, der Pool „zwei der vier Spieler jeweils fünf Sterne“. Reserve-Stapel 2021-ga-B. Typ wiederverwendet (2023-ea-B). Eigene Rechnung, mit sympy bestätigt (0,1544).")
row(id="2021-be-gk-B4e", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="e", seite="40", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen", typ_neben="",
    stichwoerter="1 − 0,6ⁿ ≥ 0,95|0,6ⁿ ≤ 0,05|n ≥ ln 0,05 / ln 0,6 ≈ 5,86, also n = 6",
    voraussetzungen="Gegenereignis|Logarithmieren",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=SM,
    gesucht="Mindestzahl der Versuche, um mit mindestens 95 % mindestens einen Stern zu gewinnen",
    verfahren="Ungleichung über das Gegenereignis „kein Stern“",
    schritte="3", zahlenraum="dezimal|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="n ≥ 5,86, also mindestens 6 Versuche",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Relationszeichen beim Teilen durch ln 0,6 nicht umkehren",
    bemerkung="Landesaufgabe (nicht im Pool). Typ wiederverwendet (2017-bb-ea). Eigene Rechnung, mit sympy bestätigt (5,865).")
row(id="2021-be-gk-B4f", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="f", seite="40", punkte="4",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen",
    typ_neben="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben",
    stichwoerter="Term 1 − (a¹⁰ + 10 · 0,4 · a^b)|a = 0,6, b = 9|1 − P(X = 0) − P(X = 1) = P(X > 1)|mehr als ein Stern bei zehn Versuchen",
    voraussetzungen="Bernoulli-Terme lesen|Gegenereignis",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Smartphone-Spiel", textumfang="mittel",
    gegeben=SM + "; Term 1 − (a¹⁰ + 10 · 0,4 · a^b) mit a, b ∈ IR⁺",
    gesucht="Werte für a und b, sodass der Term eine Wahrscheinlichkeit im Sachzusammenhang ist; Beschreibung des Ereignisses",
    verfahren="a = 1 − 0,4 als Nietenwahrscheinlichkeit, b = 9; Summe der Bernoulli-Terme für 0 und 1 Treffer",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="a = 0,6, b = 9; Ereignis: ein Spieler gewinnt bei zehn Versuchen mehr als einen Stern (mindestens zwei); Wert ≈ 0,954",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="a = 0,4 setzen (dann kein Bernoulli-Term)",
    bemerkung="Landesaufgabe (nicht im Pool). Typen wiederverwendet (2026-ea-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B4g", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="g", seite="40", punkte="2",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen", typ_neben="",
    stichwoerter="nur die Folge 50, 20, 10|0,1 · 0,4 · 0,5 = 0,02",
    voraussetzungen="Pfadregel|Tabelle der Verteilung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle Bonuspunkte 10 / 20 / 50 mit 50 % / 40 % / 10 %", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=SM2 + "; ein Spieler startet an drei aufeinanderfolgenden Tagen",
    gesucht="Wahrscheinlichkeit, von Tag zu Tag weniger Bonuspunkte zu erhalten",
    verfahren="Einzige passende Folge 50 – 20 – 10 als Pfadprodukt",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,1 · 0,4 · 0,5 = 0,02 (2 %)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="auch gleichbleibende Punktzahlen zulassen",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBStochastikWTR2-1e. Wortgleich mit der Poolaufgabe e (Reserve-Stapel 2021-ga-B). Typ wiederverwendet (2019-ea-A). Eigene Rechnung.")
row(id="2021-be-gk-B4h", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="h", seite="41", punkte="4",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit einer Summe über alle Ergebnisfolgen mit Reihenfolgen berechnen", typ_neben="",
    stichwoerter="80 Punkte aus vier Tagen: 50 + 10 + 10 + 10 (vier Reihenfolgen) oder 20 + 20 + 20 + 20|4 · 0,1 · 0,5³ + 0,4⁴ = 0,05 + 0,0256 = 0,0756",
    voraussetzungen="Zerlegung der Summe|Anzahl der Reihenfolgen|Pfadregel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle wie in g", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=SM2 + "; ein Spieler startet an vier Tagen",
    gesucht="Wahrscheinlichkeit für insgesamt 80 Bonuspunkte",
    verfahren="Alle Kombinationen mit Summe 80 samt Reihenfolgen addieren",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P = 4 · 0,1 · 0,5³ + 0,4⁴ = 0,0756 (7,56 %)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die vier Reihenfolgen von 50, 10, 10, 10 nicht zählen",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBStochastikWTR2-1f. Wortgleich mit der Poolaufgabe f (Reserve-Stapel 2021-ga-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2021-be-gk-B4i", block="B", aufgabe="4", titel="Smartphone-Spiel", teilaufgabe="i", seite="41", punkte="4",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen", typ_neben="",
    stichwoerter="x für 10, 0,9 − x für 20, 0,1 für 50|E = 3000/200 = 15 Punkte pro Tag|10x + 20(0,9 − x) + 5 = 15 ⇔ x = 0,8|P(10) = 80 %, P(20) = 10 %",
    voraussetzungen="Erwartungswert als Mittel pro Tag|Summenbedingung|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle wie in g", kontext="Smartphone-Spiel", textumfang="mittel",
    gegeben=SM2 + "; die Wahrscheinlichkeiten für 10 und 20 werden so geändert, dass in 200 Tagen im Mittel 3 000 Bonuspunkte anfallen (50 bleibt bei 10 %)",
    gesucht="die beiden geänderten Wahrscheinlichkeiten",
    verfahren="Erwartungswert 15 pro Tag ansetzen, P(20) = 0,9 − P(10)",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(10 Punkte) = 0,8, P(20 Punkte) = 0,1",
    zwischenergebnis="E = 15", niveau_geschaetzt="II",
    fehlerquelle="den Erwartungswert 3000 statt 15 je Tag ansetzen",
    bemerkung="Poolaufgabe (nicht erfasst): 2021MgrundlegendBStochastikWTR2-1g. Wortgleich mit der Poolaufgabe g (Reserve-Stapel 2021-ga-B). Eigene Rechnung, mit sympy bestätigt.")
# ---- Dubletten aus dem Pool (dubletten.py, map_2021gk.py)
row(id="2021-be-gk-A1.1a", block="A", aufgabe="1.1", titel="Analysis 1", teilaufgabe="a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Passenden Graphen zu einem Funktionsterm über Funktionswerte auswählen",
    typ_neben="",
    stichwoerter="f(x) = x³ − x, Nullstellen −1, 0, 1|Graph II: f(0,5) < 0, dort aber positiv|Graph III: Steigung zwischen −0,5 und 0,5 konstant, f' nicht konstant",
    voraussetzungen="Funktionswert prüfen|Ableitung nicht konstant",
    format="Begründung",
    operator="Geben Sie an|Begründen Sie",
    antwort="Text",
    material="Koordinatensystem",
    skizze="drei kleine Skizzen ohne Gitter mit Nullstellen −1, 0, 1: I kubische Kurve, zwischen −1 und 0 oberhalb, zwischen 0 und 1 unterhalb der Achse; II umgekehrt (zwischen 0 und 1 oberhalb); III Streckenzug mit denselben Nullstellen, zwischen −0,5 und 0,5 geradlinig",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = x³ − x in IR; Graphen I, II, III, einer stellt f dar",
    gesucht="die Graphen, die nicht infrage kommen, mit Begründung",
    verfahren="Vorzeichen eines Funktionswerts und Nichtkonstanz der Steigung prüfen",
    schritte="2",
    zahlenraum="dezimal|negativ",
    einheiten="",
    ergebnis="der Graph II kommt nicht infrage, da f(0,5) < 0 gilt, der Graph III nicht, da die Steigung des Graphen von f für −0,5 ≤ x ≤ 0,5 nicht konstant ist",
    zwischenergebnis="f(0,5) = −0,375",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Nullstellen prüfen (alle drei passen)",
    abhaengig_von="",
    bemerkung="Dublette von: 2021MgrundlegendAAnalysis12-a. Wortgleich mit der Poolaufgabe 2021 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.2 a (Graphen I, II, III wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2021-be-gk-A1.1b", block="A", aufgabe="1.1", titel="Analysis 1", teilaufgabe="b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen",
    typ_neben="",
    stichwoerter="Nullstellen −1, 0, 1|Punktsymmetrie: 2 · Integral von −1 bis 0|[1/4 x⁴ − 1/2 x²] = 1/4|Inhalt 1/2",
    voraussetzungen="Nullstellen|Symmetrie oder Beträge|Stammfunktion",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = x³ − x",
    gesucht="Inhalt der Fläche, die Graph und x-Achse einschließen",
    verfahren="zwei Flächenstücke, über Symmetrie eines verdoppeln",
    schritte="3",
    zahlenraum="Bruch|negativ",
    einheiten="",
    ergebnis="2 · Integral von −1 bis 0 über (x³ − x) dx = 2 · [1/4 x⁴ − 1/2 x²] von −1 bis 0 = 2 · (−1/4 + 1/2) = 1/2",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Integral von −1 bis 1 bilden (ergibt 0)",
    abhaengig_von="",
    bemerkung="Dublette von: 2021MgrundlegendAAnalysis12-b. Wortgleich mit der Poolaufgabe 2021 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.2 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")

NEUE_TYPEN = [
    ("Vorzeichen der Ableitung an vorgegebenen Stellen aus dem Funktionsgraphen angeben", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Aus dem Verlauf eines Funktionsgraphen an markierten Stellen angeben, ob die Ableitung dort positiv, null oder negativ ist (Steigung, waagerechte Tangente).",
     "2021-be-gk-A1.2a"),
    ("Integralwert: Aussage über zwei Integrale über die Lage des Graphen zur x-Achse beurteilen", "Analysis", "Flächeninhalt durch Integration",
     "Eine Ungleichung zwischen zwei bestimmten Integralen am Graphen beurteilen, indem das Vorzeichen jedes Integrals aus der Lage des Graphen ober- oder unterhalb der x-Achse (Flächenbilanz) abgelesen wird.",
     "2021-be-gk-A1.2b"),
    ("Ausschluss einer Stelle als Maximalstelle einer Rechtecksfläche über die notwendige Bedingung nachweisen", "Analysis", "Extremalprobleme",
     "Die Zielfunktion einer Rechtecksfläche unter einem Graphen aufstellen und über A'(x₀) ≠ 0 nachweisen, dass eine vorgegebene Stelle nicht die Maximalstelle ist.",
     "2021-be-gk-A1.3b"),
    ("Koordinatenform einer Ebene aus der Normalenform durch Ausmultiplizieren angeben", "Analytische Geometrie", "Ebenen",
     "Eine in Normalenform (n · (x − p) = 0) gegebene Ebene durch Ausmultiplizieren des Skalarprodukts in Koordinatenform überführen.",
     "2021-be-gk-A1.4a"),
    ("Geraden und Ebenen: Ebene senkrecht zu zwei gegebenen Ebenen angeben", "Analytische Geometrie", "Orthogonalität",
     "Eine Ebene angeben, die zu zwei sich schneidenden Ebenen senkrecht steht: der Richtungsvektor der Schnittgeraden ist ihr Normalenvektor, oder beide Normalenvektoren dienen als Spannvektoren.",
     "2021-be-gk-A1.4c"),
    ("Gerade in einer Ebene durch einen Punkt parallel zu einer Koordinatenebene angeben", "Analytische Geometrie", "Geraden",
     "Eine Gerade angeben, die in einer Ebene liegt, durch einen gegebenen Punkt geht und eine Koordinatenebene nicht schneidet: Richtungsvektor als Linearkombination der Spannvektoren mit verschwindender Koordinate.",
     "2021-be-gk-A1.5b"),
    ("Ziehen ohne Zurücklegen: Gleiche Chance verschiedener Ziehungspositionen beim Ziehen ohne Zurücklegen begründen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Entscheiden und begründen, ob eine spätere Ziehungsposition beim Ziehen ohne Zurücklegen eine andere Erfolgswahrscheinlichkeit hat als die erste, über die totale Wahrscheinlichkeit aller Pfade oder ein Symmetrieargument.",
     "2021-be-gk-A1.7b"),
    ("Fläche: Fläche zwischen Graph und waagerechter Gerade zwischen zwei nachgewiesenen Schnittstellen berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Zwei vorgegebene Stellen als gemeinsame Punkte von Graph und waagerechter Gerade durch Einsetzen nachweisen und den Inhalt der eingeschlossenen Fläche als Integral der Differenz berechnen.",
     "2021-be-gk-B2.1e"),
    ("Abstand zweier Extrempunkte verschiedener Graphen mit einer Schranke vergleichen", "Analysis", "Kurvenuntersuchung",
     "Den Hochpunkt (Scheitel) eines zweiten Graphen berechnen und den Abstand zum bekannten Hochpunkt des ersten Graphen mit einer vorgegebenen Schranke vergleichen.",
     "2021-be-gk-B2.1f"),
    ("Monotonieintervalle und Wertebereich einer Differenzfunktion auf einem Intervall über die Ableitung ermitteln", "Analysis", "Kurvenuntersuchung",
     "Für die Differenz zweier Funktionen auf einem abgeschlossenen Intervall die Monotonieintervalle aus der Ableitung bestimmen und den Wertebereich aus Minimum und Randwerten angeben.",
     "2021-be-gk-B2.1g"),
    ("Fläche: Fläche zwischen zwei Graphen mit verschiedenen Grenzen als Differenz zweier Integrale berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Eine von zwei Graphen, der x-Achse und einer senkrechten Geraden begrenzte Fläche als Differenz zweier Integrale mit jeweils eigenen Grenzen (Nullstellen, Randgerade) berechnen, gegebenenfalls mit Maßstab.",
     "2021-be-gk-B2.1h"),
    ("Gleiche Ableitungswerte zweier Funktionen nachweisen und als parallele Tangenten deuten", "Analysis", "Ableitung und Änderungsrate",
     "Nachweisen, dass zwei Funktionen an vorgegebenen Stellen denselben Ableitungswert haben, und die Bedeutung als parallele Tangenten (gleicher Anstieg) im Sachzusammenhang erläutern.",
     "2021-be-gk-B2.1i"),
    ("Quadratische Funktion aus Nullstelle und Scheitelpunkt rekonstruieren", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Eine Parabel aus der Nullstelle im Ursprung und dem Hochpunkt (Scheitel) bestimmen, über das lineare Gleichungssystem q(2) = y, q'(2) = 0 oder die Scheitelpunktform.",
     "2021-be-gk-B2.1k"),
    ("Existenz eines Wendepunkts aus Tiefpunkt und Grenzverhalten über eine Skizze begründen", "Analysis", "Kurvenuntersuchung",
     "Aus dem Vorzeichenwechsel der Ableitung (Tiefpunkt) und dem Grenzwert null für x → +∞ mithilfe einer Skizze begründen, dass der Graph seine Krümmung wechseln muss, also einen Wendepunkt hat.",
     "2021-be-gk-B2.2e"),
    ("Tangentengleichung im Ursprung aufstellen und Grenze einer Dreiecksfläche aus dem Flächeninhalt berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Tangente an einen Graphen in seinem Schnittpunkt mit der x-Achse aufstellen und die senkrechte Gerade x = b so bestimmen, dass Tangente, x-Achse und Gerade eine Fläche vorgegebenen Inhalts einschließen.",
     "2021-be-gk-B2.2f"),
    ("Horizontalen Abstand zweier Punkte als kürzer als ihre Verbindungsstrecke begründen", "Analytische Geometrie", "Abstände",
     "Ohne Rechnung begründen, dass der horizontale Abstand zweier Punkte kleiner ist als die Länge ihrer Verbindungsstrecke (Hypotenuse länger als Kathete, Satz des Pythagoras).",
     "2021-be-gk-B2.2h"),
    ("Rechenschritte zur Winkelbestimmung aus Höhen- und Horizontalabstand beurteilen und berichtigen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Vorgelegte Teilschritte einer Winkelberechnung (Funktionswert als Höhe, Sinus im rechtwinkligen Dreieck) auf Fehler prüfen (Betrag, Vorzeichen im Nenner, Rundung) und die Berichtigung angeben.",
     "2021-be-gk-B2.2k"),
    ("Winkel zwischen Sehne zum Wendepunkt und Verbindungslinie zweier Schnittpunkte über Steigungswinkel berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Winkel zwischen zwei Sehnen vom Ursprung (zum Wendepunkt und zu einem zweiten Punkt) als Summe bzw. Differenz der Steigungswinkel über den Tangens berechnen und mit einer Schranke vergleichen.",
     "2021-be-gk-B2.2l"),
    ("Halbierung eines Quadrats durch gegebene Ebenen entscheiden und begründen", "Analytische Geometrie", "Schnittmengen",
     "Für vorgegebene Ebenengleichungen entscheiden, ob die Ebene ein Quadrat in einer Koordinatenebene in zwei flächengleiche Teile schneidet (Mittelparallele, Diagonale, keine Schnittmenge), mit Begründung.",
     "2021-be-gk-B3e"),
    ("Ebene Figur: Eckpunkte eines gleichschenkligen Trapezes aus einem Flächenverhältnis zum Quadrat bestimmen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Zwei Eckpunkte eines Quadrats symmetrisch auf einer Kante so verschieben, dass das entstehende gleichschenklige Trapez einen vorgegebenen Anteil der Quadratfläche hat; Koordinaten über die Trapezformel.",
     "2021-be-gk-B3f"),
    ("Rechenweg für die kürzeste Linie über eine Kante aus Lotfußpunkt und Symmetrie erläutern", "Analytische Geometrie", "Abstände",
     "Einen vorgelegten Rechenweg erläutern: Punkt auf der Kante parametrisieren, Orthogonalität über das Skalarprodukt als Bedingung für die kürzeste Verbindung, Symmetrie des Körpers für die Verdopplung der Strecke.",
     "2021-be-gk-B3g"),
    ("Körper: Volumenverhältnis zweier Körper über Formeln ohne Zahlenwerte ermitteln", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Das Verhältnis der Volumina zweier Körper (etwa Pyramide und Prisma über derselben Grundfläche) aus den Volumenformeln allgemein bestimmen und als Prozentsatz angeben, ohne konkrete Werte zu berechnen.",
     "2021-be-gk-B3i"),
    ("Wahrscheinlichkeit für zwei unabhängige Spieler als Produkt binomialer Wahrscheinlichkeiten berechnen", "Stochastik", "Binomialverteilung",
     "Eine kumulierte Binomialwahrscheinlichkeit (aus der Tabelle) für einen Spieler bestimmen und für zwei unabhängige Spieler quadrieren.",
     "2021-be-gk-B4b"),
    ("Wahrscheinlichkeit einer Summe über alle Ergebnisfolgen mit Reihenfolgen berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Für eine feste Anzahl von Ziehungen mit tabellierter Verteilung alle Wertkombinationen mit vorgegebener Summe auflisten, ihre Reihenfolgen zählen und die Pfadwahrscheinlichkeiten addieren.",
     "2021-be-gk-B4h"),
    ("Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen", "Stochastik", "Kenngrößen von Verteilungen",
     "In einer Verteilung mit zwei unbekannten Wahrscheinlichkeiten diese aus der Summenbedingung und einem vorgegebenen Erwartungswert (etwa als Mittel über viele Tage) berechnen.",
     "2021-be-gk-B4i"),
]


# ======================================================== AB HIER UNVERÄNDERT
def lade(pfad, kopf):
    if not os.path.exists(pfad):
        return kopf, []
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    if not rows:
        return kopf, []
    if rows[0] != kopf:
        sys.exit(f"{pfad}: Kopfzeile weicht von der Quelle ab\n  Datei:  {rows[0]}\n  Quelle: {kopf}")
    return rows[0], rows[1:]


def schreibe(pfad, kopf, zeilen):
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(kopf)
        for z in zeilen:
            w.writerow(z)


# Feste Markierungen in bemerkung (abi.md § 7; wie iqb.md § 7), bewusst umlautfrei.
MARKE_KONTEXT = "Traegerbindung: Kontext"
MARKE_DUBLETTE = re.compile(r"Dublette von: (" + KENNUNG.pattern + r")")
# Vorstufe des Verweises (v0.5, Lauf 14): Poolaufgabe, deren Stapel im Profil iqb
# noch nicht erfasst ist; die Kennung ist die voraussichtliche iqb-id. Wird zum
# „Dublette von:", sobald der Stapel erfasst ist (abgleich.py).
MARKE_POOL_OFFEN = re.compile(r"Poolaufgabe \(nicht erfasst(, abgewandelt)?\): (" + KENNUNG.pattern + r")")
# Abgewandelte Poolaufgabe mit erfasster Poolzeile (v0.6, Lauf 15): kein Dublettenverweis
# (nicht wortgleich), aber ein Verweis auf die Poolzeile; der Unterschied folgt nach „;".
MARKE_ABGEWANDELT = re.compile(r"Abgewandelt von: (" + KENNUNG.pattern + r"); ")
OFFENE_POSTEN = []  # Vermerke, deren Poolzeile inzwischen erfasst ist (Ausgabe am Ende, kein Abbruch)


def pool_stand(z, andere):
    """'dublette' (Verweis auf erfasste Poolzeile), 'offen' (wortgleich, Pool nicht erfasst),
    'abgewandelt' (Vormerkung oder Verweis auf abgewandelte Poolzeile) oder '' – für die Poolquote je Heft."""
    if MARKE_DUBLETTE.search(z["bemerkung"]):
        return "dublette"
    if MARKE_ABGEWANDELT.search(z["bemerkung"]):
        return "abgewandelt"
    m = MARKE_POOL_OFFEN.search(z["bemerkung"])
    if m:
        return "abgewandelt" if m.group(1) else "offen"
    return ""


def poolquote(zeilen, andere):
    """Zeilen und BE je Heft, die wortgleich im Pool stehen (erfasst oder nicht),
    dazu die abgewandelten; Text für die Kennzahlenzeile."""
    st = [(pool_stand(z, andere), int(z["punkte"])) for z in zeilen if z["punkte"].isdigit()]
    be = sum(p for _, p in st)
    wort = [(s, p) for s, p in st if s in ("dublette", "offen")]
    abw = [(s, p) for s, p in st if s == "abgewandelt"]
    txt = (f"Pool {len(wort)} von {len(zeilen)} Zeilen, {sum(p for _, p in wort)} von {be} BE "
           f"({100 * sum(p for _, p in wort) / be if be else 0:.0f} %)")
    offen = sum(1 for s, _ in wort if s == "offen")
    if offen:
        txt += f", davon {offen} Zeilen mit nicht erfasster Poolzeile"
    if abw:
        txt += f"; abgewandelt {len(abw)} Zeilen, {sum(p for _, p in abw)} BE"
    return txt
AB_SPALTE = re.compile(r"AB amtlich: (I{1,3})\.")
ENG = re.compile(r"Schätzung enge Fassung: (I{1,3})")


def ohne_feldnamen(v):
    """Feldnamen des Schemas, Kennungen und Markierungen aus dem Text nehmen. Sie sind
    bewusst umlautfrei und stehen in bemerkung als Fachwort, ohne Umschrift zu sein."""
    t = KENNUNG.sub(" ", v).lower()
    t = t.replace(MARKE_KONTEXT.lower(), " ")
    for f in sorted(HEAD, key=len, reverse=True):
        t = t.replace(f, " ")
    return t


def umschrift_liste(zeilen):
    """Sichtprüfung, kein Assert: alle Wörter mit ss, ae, oe oder ue."""
    worte = {}
    for z in zeilen:
        for k, v in z.items():
            if k in OHNE_UMLAUT:
                continue
            for w in re.findall(r"[^\W\d_]+", ohne_feldnamen(v), re.UNICODE):
                if any(p in w for p in ("ss", "ae", "oe", "ue")):
                    worte[w] = worte.get(w, 0) + 1
    return sorted(worte.items())


def hoechster_afb(v):
    return max(ORD.get(t, 0) for t in v.split("|")) if v else 0


def typen_von(z):
    t = set()
    for feld in ("typ", "typ_neben"):
        t |= {s for s in z[feld].split("|") if s}
    return t


def pruefe_zeile(z, a, andere, heftkennung=True):
    """Alle Prüfungen, die eine einzelne Zeile aus sich selbst und den anderen
    Katalogen (Dublettenverweis) bestehen kann."""
    i = z["id"] or "(ohne id)"
    for k in PFLICHT:
        a(z[k].strip() != "", f"{i}: Pflichtfeld leer: {k}")
    a(z["block"] in ("A", "B"), f"{i}: block muss A oder B sein")
    a(z["stern"] == "", f"{i}: stern ist im Profil abi immer leer")
    a(z["hilfsmittel"] == ("nein" if z["block"] == "A" else "ja"),
      f"{i}: hilfsmittel passt nicht zu block {z['block']}")
    a(PAPIER.fullmatch(z["papier"]) is not None, f"{i}: papier folgt nicht dem Muster Jahr-Land-Niveau[-cas|-mms]")
    a(z["papier"].startswith(z["jahr"] + "-"), f"{i}: papier beginnt nicht mit dem Jahr")
    if z["jahr"] <= "2018":
        a(z["afb_amtlich"] == "", f"{i}: afb_amtlich ist für {z['jahr']} nicht ausgewiesen")
    elif z["afb_amtlich"]:
        a(AFB.fullmatch(z["afb_amtlich"]) is not None, f"{i}: afb_amtlich ungültig: {z['afb_amtlich']}")
        teile = z["afb_amtlich"].split("|")
        a([ORD[t] for t in teile if t in ORD] == sorted({ORD[t] for t in teile if t in ORD}),
          f"{i}: afb_amtlich nicht aufsteigend ohne Wiederholung")
    a(re.fullmatch(r"\d+(\.\d+)?", z["aufgabe"]), f"{i}: aufgabe muss eine Nummer wie 3 oder 2.1 sein")
    a(re.fullmatch(r"[a-z]", z["teilaufgabe"]), f"{i}: teilaufgabe muss ein Kleinbuchstabe sein")
    a(z["id"] == f"{z['papier']}-{z['block']}{z['aufgabe']}{z['teilaufgabe']}",
      f"{i}: id folgt nicht dem Muster papier-BlockAufgabeTeilaufgabe")
    if heftkennung:
        a(z["jahr"] == KONFIG["jahr"] and z["papier"] == KONFIG["papier"],
          f"{i}: Heftkennung passt nicht zu KONFIG")
    a(re.fullmatch(r"\d+", z["punkte"]) and int(z["punkte"]) > 0, f"{i}: punkte ungültig")
    a(re.fullmatch(r"\d+(\|\d+)?", z["seite"]), f"{i}: seite ungültig (Zahl oder Zahl|Zahl)")
    for s in z["seite"].split("|"):
        if s.isdigit() and heftkennung:
            a(int(s) <= KONFIG["seiten"], f"{i}: Seite {s} größer als der Heftumfang")
    a(re.fullmatch(r"\d+", z["schritte"]), f"{i}: schritte muss eine Zahl sein")
    a(z["leitidee"] in THEMEN, f"{i}: Sachgebiet unbekannt: {z['leitidee']}")
    a(z["thema"] in THEMEN.get(z["leitidee"], []),
      f"{i}: Thema passt nicht zum Sachgebiet: {z['thema']}")
    for feld in ("format", "antwort", "material", "zahlenraum"):
        for teil in [s for s in z[feld].split("|") if s]:
            a(teil in VOK[feld], f"{i}: {feld} hat unbekannten Wert: {teil}")
    for feld in ("textumfang", "niveau_geschaetzt"):
        a(z[feld] in VOK[feld], f"{i}: {feld} ungültig: {z[feld]}")
    b = z["bemerkung"]
    # Trägerbindung: nur die feste Markierung am Feldanfang
    a("Trägerbindung" not in b and "Traegerbindung: frei" not in b,
      f"{i}: Trägerbindung nur als „{MARKE_KONTEXT}“ am Anfang von bemerkung (kein Vermerk heißt frei)")
    if MARKE_KONTEXT.lower() in b.lower():
        a(b.startswith(MARKE_KONTEXT) and (b[len(MARKE_KONTEXT):len(MARKE_KONTEXT) + 1] in (".", " ")),
          f"{i}: Markierung „{MARKE_KONTEXT}“ muss am Anfang von bemerkung stehen, gefolgt von Punkt oder Klammer")
    # Pool-Teilaufgabe (abi.md § 7): Verweis auf die iqb-Zeile, geteilter Typ
    m = MARKE_DUBLETTE.search(b)
    if "Dublette von" in b:
        a(m is not None, f"{i}: „Dublette von:“ ohne gültige Pool-Kennung in bemerkung")
    if m:
        ref = andere.get(m.group(1))
        a(ref is not None, f"{i}: Dublette von {m.group(1)}, aber die Zeile steht in keinem anderen Katalog")
        if ref:
            a(z["typ"] == ref["typ"],
              f"{i}: Dublette von {m.group(1)}, aber typ weicht ab (geteilter Typ verlangt; typ_neben darf Nebenleistungen des Landeshefts nennen)")
            a(z["punkte"] == ref["punkte"] or "BE" in b,
              f"{i}: Dublette von {m.group(1)} mit anderer Punktzahl – bemerkung muss die BE nennen")
    # Vorstufe (v0.5): Poolaufgabe, deren Stapel noch nicht erfasst ist
    mo = MARKE_POOL_OFFEN.search(b)
    if "Poolaufgabe (nicht erfasst" in b:
        a(mo is not None, f"{i}: „Poolaufgabe (nicht erfasst …):“ ohne gültige Pool-Kennung in bemerkung")
    if mo:
        a(b.startswith("Poolaufgabe (nicht erfasst"), f"{i}: Vermerk „Poolaufgabe (nicht erfasst …)“ muss am Anfang von bemerkung stehen")
        # Übergangszustand (abi.md § 7): erfasste Poolzeile heißt offener Posten, kein Fehler
        if mo.group(2) in andere:
            OFFENE_POSTEN.append(f"{i}: Poolzeile {mo.group(2)} ist erfasst – Vermerk mit abgleich.py in „Dublette von:“ umstellen")
        a(m is None, f"{i}: „Dublette von:“ und „Poolaufgabe (nicht erfasst)“ zugleich")
    # Abgewandelte Poolaufgabe mit erfasster Poolzeile (v0.6): Verweis am Anfang, Zeile muss stehen
    ma = MARKE_ABGEWANDELT.search(b)
    if "Abgewandelt von" in b:
        a(ma is not None, f"{i}: „Abgewandelt von:“ ohne gültige Pool-Kennung oder ohne „; Unterschied“ in bemerkung")
    if ma:
        a(b.startswith("Abgewandelt von"), f"{i}: Verweis „Abgewandelt von:“ muss am Anfang von bemerkung stehen")
        a(ma.group(1) in andere, f"{i}: Abgewandelt von {ma.group(1)}, aber die Zeile steht in keinem anderen Katalog")
        a(m is None and mo is None, f"{i}: „Abgewandelt von:“ neben einem weiteren Poolvermerk")
    for k, v in z.items():
        a("?" not in v or k == "bemerkung" or z["bemerkung"].strip() != "",
          f"{i}: Fragezeichen in {k} ohne Grund in bemerkung")
        # Pool-Kennungen (…WTR3-1a) tragen den Bindestrich vor der Aufgabennummer, v0.4
        a(not re.search(r"(?<=[\d\s(])-(?=\d)", KENNUNG.sub(" ", v)),
          f"{i}: ASCII-Bindestrich als Minus in {k}")
        if k not in OHNE_UMLAUT:
            treffer = [w for w in UMSCHRIFT if w in ohne_feldnamen(v)]
            a(not treffer, f"{i}: ASCII-Umschrift in {k}: {treffer}")


def amtlich_von(z):
    """Amtlicher Bereich für die Eichung: die Spalte „AB amtlich" aus bemerkung, sonst das
    Maximum über afb_amtlich; 0, wenn nichts ausgewiesen ist (Hefte bis 2018)."""
    m = AB_SPALTE.search(z["bemerkung"])
    if m:
        return ORD[m.group(1)]
    return hoechster_afb(z["afb_amtlich"])


def geschaetzt_eng(z):
    m = ENG.search(z["bemerkung"])
    return m.group(1) if m else z["niveau_geschaetzt"]


def geerbt(z, andere):
    """Dublette, die die Schätzung ihrer Poolzeile trägt (v0.8): dort schon geeicht."""
    m = MARKE_DUBLETTE.search(z["bemerkung"])
    return bool(m and m.group(1) in andere
                and andere[m.group(1)]["niveau_geschaetzt"] == z["niveau_geschaetzt"])


def eichung(zeilen, eng=False, andere=None):
    """Trefferquote der Schätzung gegen den amtlichen Bereich. Rückgabe: Treffer,
    Abweichungen, Zahl der gewerteten Zeilen (nur Zeilen mit amtlichem Bereich).
    Mit andere (Poolzeilen) werden geerbte Schätzungen (Dubletten) übergangen (v0.8)."""
    treffer, abw, gewertet = 0, [], 0
    for z in zeilen:
        amt = amtlich_von(z)
        if not amt or (andere is not None and geerbt(z, andere)):
            continue
        gewertet += 1
        wert = geschaetzt_eng(z) if eng else z["niveau_geschaetzt"]
        if amt == ORD.get(wert, 0):
            treffer += 1
        else:
            abw.append(f"{z['id']} geschätzt {wert}, amtlich höchstens "
                       f"{[k for k, v in ORD.items() if v == amt][0]}")
    return treffer, abw, gewertet


def schnitt(z):
    """Schnittwert Thema × Gegenstandsklasse × Handlung (abitur-vokabular.md § 4); Thema des Typs (v0.4)."""
    return (TYP_THEMA.get(z["typ"], ("", z["thema"]))[1], klasse_von(z["typ"]),
            HANDLUNG.get(z["format"].split("|")[0], "?"))


def main():
    fehler, warnung = [], []
    def a(cond, msg):
        if not cond:
            fehler.append(msg)

    _, alt_kat = lade(KAT, HEAD)
    _, alt_typ = lade(TYP, TYP_HEAD)
    alt = [dict(zip(HEAD, r)) for r in alt_kat]
    TYP_THEMA.update({r[0]: (r[1], r[2]) for r in alt_typ})
    TYP_THEMA.update({t[0]: (t[1], t[2]) for t in NEUE_TYPEN if len(t) == 5})
    # andere Kataloge derselben Typenliste (Entscheidung 25)
    andere_liste = [dict(zip(HEAD, r)) for p in ANDERE_KATALOGE for r in lade(p, HEAD)[1]]
    andere = {z["id"]: z for z in andere_liste}
    andere_typen = set()
    for z in andere_liste:
        andere_typen |= typen_von(z)
    print(f"Vokabular: {len(HEAD)} Felder, {len(LEITIDEEN)} Sachgebiete, "
          f"{sum(len(v) for v in THEMEN.values())} Themen – gelesen aus {KERN} und {VOKABULAR}; "
          f"{len(andere)} Zeilen aus {ANDERE_KATALOGE}")

    # ---- Selbstprüfung: kein neues Heft, nur die vorhandenen Zeilen prüfen
    if not ZEILEN:
        for z in alt:
            a(len(z) == len(HEAD), f"{z.get('id')}: Feldzahl weicht ab")
            pruefe_zeile(z, a, andere, heftkennung=False)
        typ_namen = {r[0] for r in alt_typ}
        a(len(typ_namen) == len(alt_typ), "doppelter Typ in der Typenliste")
        benutzt = set(andere_typen)
        for z in alt:
            for t in typen_von(z):
                benutzt.add(t)
                a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
            pruefe_thema(z, a)
        a(not (typ_namen - benutzt), f"Typen unbenutzt: {sorted(typ_namen - benutzt)}")
        ids = {z["id"] for z in alt}
        a(len(ids) == len(alt), "doppelte id im Katalog")
        a(not (ids & set(andere)), f"ids auch in einem anderen Katalog: {sorted(ids & set(andere))[:5]}")
        for z in alt:
            for dep in [s for s in z["abhaengig_von"].split("|") if s]:
                a(dep in ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
        for r in alt_typ:
            a(r[1] in THEMEN and r[2] in THEMEN.get(r[1], []),
              f"Typ {r[0]}: Sachgebiet oder Thema unbekannt")
            a(r[4] in ids or r[4] in andere, f"Typ {r[0]}: beispiel_id in keinem Katalog")
            pruefe_typname(r[0], r[2], a, TYP)
        if fehler:
            print(f"\nSelbstprüfung: {len(fehler)} Fehler")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        hefte = sorted({z["papier"] for z in alt})
        eigene = {t for z in alt for t in typen_von(z)}
        print(f"Selbstprüfung bestanden: {len(alt)} Katalogzeilen aus {len(hefte)} Heften, {len(alt_typ)} Typen "
              f"(gemeinsame Liste, {len(eigene - andere_typen)} nur hier, {len(eigene & andere_typen)} in beiden "
              f"Katalogen), alle Typen verwendet. ZEILEN ist leer, nichts geschrieben.")
        treffer, abw, gew = eichung(alt)
        if gew:
            print(f"Eichung über den Bestand: {treffer} von {gew} gewerteten Zeilen ({100 * treffer // gew} %); "
                  f"{len(alt) - gew} Zeilen ohne amtlichen Bereich.")
        else:
            print(f"Eichung: keine Zeile mit amtlichem Bereich ({len(alt)} Zeilen).")
        print("Außerhalb der Geltung: " + ", ".join(
            f"{ziel} {sum(1 for z in alt if ziel not in GELTUNG.get(z['thema'], set()))}"
            for ziel in ZIELE) + f" von {len(alt)} Zeilen (jede Zeile gegen jede Zielprüfung)")
        # Geltung des eigenen Hefts (v0.7): Zielprüfungen aus dem papier-Kürzel, bebb gegen beide
        for h in hefte:
            zh = [z for z in alt if z["papier"] == h]
            ziele = ziele_von(h)
            aus = [z["id"] for z in zh if not in_geltung(z, ziele)]
            print(f"Geltung {h} ({' oder '.join(ziele)}): {len(zh) - len(aus)} von {len(zh)} Zeilen in Geltung"
                  + (f", außerhalb: {', '.join(aus)}" if aus else "")
                  + "".join(f"; nur {ziel}: {sum(1 for z in zh if ziel not in GELTUNG.get(z['thema'], set()))} außerhalb" for ziel in ziele if len(ziele) > 1))
        werte = {schnitt(z) for z in alt}
        andere_werte = {schnitt(z) for z in andere_liste}
        print(f"Schnitt: {len(werte)} Werte auf {len(alt)} Zeilen, {len(werte - andere_werte)} davon nicht "
              f"in {ANDERE_KATALOGE}; Dublettenverweise: "
              f"{sum(1 for z in alt if MARKE_DUBLETTE.search(z['bemerkung']))}, abgewandelt: "
              f"{sum(1 for z in alt if MARKE_ABGEWANDELT.search(z['bemerkung']))}")
        # Poolquote je Heft (v0.5): Kennzahl für abi-pruefungen.md § 2
        for h in hefte:
            print(f"Poolquote {h}: {poolquote([z for z in alt if z['papier'] == h], andere)}")
        offen = sum(1 for z in alt if MARKE_POOL_OFFEN.search(z["bemerkung"]))  # Übergangszustand (v0.6)
        print(f"Offene Posten (Poolaufgabe (nicht erfasst …), Übergangszustand): {offen} Zeilen"
              + (f", davon {len(OFFENE_POSTEN)} mit inzwischen erfasster Poolzeile:" if OFFENE_POSTEN else ""))
        for o in OFFENE_POSTEN:
            print("  -", o)
        print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
              "(Häufigkeit in Klammern):")
        liste = umschrift_liste(alt)
        print("  " + ", ".join(f"{w} ({n})" for w, n in liste) if liste else "  keines")
        return

    # ---- Normalfall: neues Heft anhängen
    probe = bool(KONFIG.get("probe"))
    alt_ids = {z["id"] for z in alt}
    typ_namen = {r[0] for r in alt_typ} | {t[0] for t in NEUE_TYPEN}
    neue_ids = [z["id"] for z in ZEILEN]
    a(len(set(neue_ids)) == len(neue_ids), "doppelte id in ZEILEN")
    for i in neue_ids:
        a(i not in alt_ids, f"{i}: Kennung steht schon im Katalog")

    for t in NEUE_TYPEN:
        a(len(t) == 5, f"Typ {t[0]}: Eintrag braucht fünf Felder")
        a(t[0] not in {r[0] for r in alt_typ}, f"Typ {t[0]}: steht schon in {TYP}")
        a(t[1] in THEMEN and t[2] in THEMEN.get(t[1], []),
          f"Typ {t[0]}: Sachgebiet oder Thema unbekannt")
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog des Hefts")
        a(len(t[3]) > 20, f"Typ {t[0]}: Definition zu knapp")
        if len(t) == 5:
            pruefe_typname(t[0], t[2], a, "NEUE_TYPEN")
    a(len({t[0] for t in NEUE_TYPEN}) == len(NEUE_TYPEN), "doppelter Typ in NEUE_TYPEN")

    # Vollständigkeit und Punkte je Aufgabe (Kern § 7): jede Aufgabe aus KONFIG["soll"]
    # muss Zeilen haben, jede Punktsumme stimmen; Aufgaben ohne Soll sind ein Fehler.
    aufgaben = sorted({z["aufgabe"] for z in ZEILEN})
    for nr in aufgaben:
        a(nr in KONFIG["soll"], f"Aufgabe {nr}: kein Soll in KONFIG")
    fehlt = sorted(set(KONFIG["soll"]) - set(aufgaben))
    if fehlt and not probe:
        a(False, f"Heft {KONFIG['papier']} unvollständig, es fehlen die Aufgaben {fehlt}")
    elif fehlt:
        warnung.append(f"Probelauf: {len(fehlt)} von {len(KONFIG['soll'])} Aufgaben fehlen noch: {fehlt}")
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr and z["punkte"].isdigit())
        if nr in aufgaben:
            a(ist == soll, f"Aufgabe {nr}: Punkte {ist}, Soll {soll}")
    if KONFIG.get("soll_teil1"):
        teil1 = [z for z in ZEILEN + alt
                 if z["block"] == "A" and z["papier"] == KONFIG["papier"]]
        ist1 = sum(int(z["punkte"]) for z in teil1 if z["punkte"].isdigit())
        a(probe or ist1 == KONFIG["soll_teil1"], f"Teil A: Punkte {ist1}, Soll {KONFIG['soll_teil1']}")

    verwendet = set()
    for z in ZEILEN:
        pruefe_zeile(z, a, andere)
        for t in typen_von(z):
            verwendet.add(t)
            a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        pruefe_thema(z, a)
        for dep in [s for s in z["abhaengig_von"].split("|") if s]:
            a(dep in neue_ids or dep in alt_ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
    warnung += OFFENE_POSTEN
    alle_verwendet = set(verwendet) | andere_typen
    for z in alt:
        alle_verwendet |= typen_von(z)
    a(not (typ_namen - alle_verwendet), f"Typen unbenutzt: {sorted(typ_namen - alle_verwendet)}")

    # Qualitätsschranke (abi.md § 7)
    n = len(ZEILEN)
    unsicher = [z["id"] for z in ZEILEN if any("?" in v for v in z.values())]
    ersatz = [z["id"] for z in ZEILEN if "ersatzweise" in z["bemerkung"].lower()]
    neu = {t[0] for t in NEUE_TYPEN}
    grenze_frage = max(SCHWELLEN["fragezeichen_mindestens"], int(SCHWELLEN["fragezeichen_anteil"] * n))
    grenze_ersatz = max(SCHWELLEN["ersatzweise_mindestens"], int(SCHWELLEN["ersatzweise_anteil"] * n))
    a(len(unsicher) <= grenze_frage,
      f"Schwelle gerissen: {len(unsicher)} Zeilen mit „?“, erlaubt {grenze_frage}: {unsicher}")
    a(len(ersatz) <= grenze_ersatz,
      f"Schwelle gerissen: {len(ersatz)} Zeilen ohne passendes Thema, erlaubt {grenze_ersatz}: {ersatz}")
    if (SCHWELLEN["neue_typen_anteil"] is not None
            and len(alt) >= SCHWELLEN["neue_typen_ab_bestand"] and verwendet):
        anteil = len(neu & verwendet) / len(verwendet)
        a(anteil <= SCHWELLEN["neue_typen_anteil"],
          f"Schwelle gerissen: {len(neu & verwendet)} von {len(verwendet)} verwendeten Typen neu "
          f"({100 * anteil:.0f} %), erlaubt {100 * SCHWELLEN['neue_typen_anteil']:.0f} %")
    # Eichschwelle nur über eigene Schätzungen; geerbte Schätzungen der Dubletten
    # sind im Pool gemessen (v0.8).
    treffer_eng, abw_eng, gew = eichung(ZEILEN, eng=True, andere=andere)
    if gew >= SCHWELLEN["eichung_ab_zeilen"]:
        a(treffer_eng / gew >= SCHWELLEN["eichung_mindestens"],
          f"Schwelle gerissen: Eichung {treffer_eng} von {gew} eigenen Zeilen "
          f"({100 * treffer_eng / gew:.0f} %), verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %: "
          f"{'; '.join(abw_eng)}")
    ausserhalb = {ziel: [z["id"] for z in ZEILEN if ziel not in GELTUNG.get(z["thema"], set())]
                  for ziel in ZIELE}

    if fehler:
        print(f"ABBRUCH – {len(fehler)} Fehler, nichts geschrieben:")
        for f_ in fehler:
            print(" -", f_)
        sys.exit(1)

    if not probe:
        schreibe(KAT, HEAD, alt_kat + [[z[k] for k in HEAD] for z in ZEILEN])
        schreibe(TYP, TYP_HEAD, alt_typ + [[t[0], t[1], t[2], t[3], t[4], "neu"] for t in NEUE_TYPEN])

        # Rückweg: geschriebene Datei mit echtem Leser einlesen und vergleichen
        _, zurueck = lade(KAT, HEAD)
        for gel, z in zip(zurueck[len(alt_kat):], ZEILEN):
            if len(gel) != len(HEAD) or any(v != z[k] for k, v in zip(HEAD, gel)):
                sys.exit(f"{z['id']}: Rückweg verändert die Zeile")
        roh = io.open(KAT, encoding="utf-8", newline="").read()
        if "\r" in roh or not all(l.startswith('"') and l.endswith('"') for l in roh.splitlines()):
            sys.exit("Ausgabe nicht vollständig gequotet oder CRLF")

    # Prüftabelle
    print(f"\nHeft {KONFIG['papier']}{' (Probelauf, nichts geschrieben)' if probe else ''} – "
          f"{len(ZEILEN)} Zeilen aus {len(aufgaben)} Aufgaben, {len(NEUE_TYPEN)} Typen neu, "
          f"Katalog {'bliebe' if probe else 'jetzt'} {len(alt_kat) + len(ZEILEN)} Zeilen\n")
    print(f"{'id':<22} {'BE':>2} {'afb':<8} {'thema':<34} {'typ':<46} ergebnis")
    for z in ZEILEN:
        print(f"{z['id']:<22} {z['punkte']:>2} {z['afb_amtlich']:<8} {z['thema'][:34]:<34} "
              f"{z['typ'][:46]:<46} {z['ergebnis'][:40]}")
    print()
    for nr in aufgaben:
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        print(f"Aufgabe {nr}: Ist {ist} / Soll {KONFIG['soll'].get(nr, '–')}")
    haupt = {z["typ"] for z in ZEILEN} | {z["typ"] for z in alt}
    neben = set()
    for z in ZEILEN + alt:
        neben |= {s for s in z["typ_neben"].split("|") if s}
    print(f"Typen: {len(typ_namen)} in der gemeinsamen Liste; im Heft {len(verwendet)} verwendet, "
          f"davon {len(neu & verwendet)} neu, {len(verwendet & andere_typen)} aus {ANDERE_KATALOGE}")
    treffer, abw, gew_alle = eichung(ZEILEN)
    geerbte = sum(1 for z in ZEILEN if amtlich_von(z) and geerbt(z, andere))
    if gew_alle:
        print(f"Eichung: {treffer} von {gew_alle} gewerteten Zeilen treffen den amtlichen Bereich"
              + (f" ({n - gew_alle} ohne amtlichen Bereich)" if gew_alle != n else "")
              + (f"; davon {geerbte} Zeilen mit geerbter Schätzung (Dubletten, im Pool geeicht), "
                 f"{gew_alle - geerbte} eigene" if geerbte else "")
              + (f"; Abweichungen: {'; '.join(abw)}" if abw else ""))
    else:
        print("Eichung: keine Zeile mit amtlichem Bereich.")
    print(f"Schwellen: {len(unsicher)} Zeilen mit „?“ (erlaubt {grenze_frage}), "
          f"{len(ersatz)} ohne passendes Thema (erlaubt {grenze_ersatz}), "
          f"Eichung eigener Zeilen {100 * treffer_eng / gew if gew else 0:.0f} % "
          f"(verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %"
          f"{', nicht scharf' if gew < SCHWELLEN['eichung_ab_zeilen'] else ''})")
    # Wiederverwendung im selben Niveau (gk, lk, ea) und Schnitt (abitur-vokabular.md § 4)
    niveau = niveau_von(KONFIG["papier"])
    im_niveau = set()
    for z in alt:
        if niveau_von(z["papier"]) == niveau:
            im_niveau |= typen_von(z)
    wieder = verwendet & im_niveau
    schnitt_alt = {schnitt(z) for z in alt if niveau_von(z["papier"]) == niveau}
    schnitt_alle = {schnitt(z) for z in alt} | {schnitt(z) for z in andere_liste}
    schnitt_neu = {schnitt(z) for z in ZEILEN}
    schnitt_bekannt = sum(1 for z in ZEILEN if schnitt(z) in schnitt_alt)
    # Geltung des Hefts (v0.7): eigene Zielprüfung(en) aus dem papier-Kürzel; bei bebb-Heften
    # liegt eine Zeile in der Geltung, wenn ihr Thema in einer der beiden Spalten gilt.
    ziele_heft = ziele_von(KONFIG["papier"])
    aus_heft = [z["id"] for z in ZEILEN if not in_geltung(z, ziele_heft)]
    geltung_txt = (f"Heft ({' oder '.join(ziele_heft)}) {len(aus_heft)}"
                   + ("".join(f", nur {ziel} {len(ausserhalb[ziel])}" for ziel in ziele_heft) if len(ziele_heft) > 1 else "")
                   + "; alle Zielprüfungen: " + ", ".join(f"{ziel} {len(ids)}" for ziel, ids in ausserhalb.items()))
    if aus_heft:
        print(f"Außerhalb der Geltung des Hefts ({' oder '.join(ziele_heft)}): {', '.join(aus_heft)}")
    for ziel, ids in ausserhalb.items():
        if ids:
            print(f"Außerhalb der Geltung {ziel}: {', '.join(ids)}")
    print(f"Kennzahlen: | {KONFIG['papier']} | {n} | {len(verwendet)} | {len(neu & verwendet)} "
          f"({100 * len(neu & verwendet) / len(verwendet):.0f} %) | "
          + (f"{treffer} von {gew_alle} ({100 * treffer / gew_alle:.0f} %)"
             + (f", davon {geerbte} geerbt" if geerbte else "") if gew_alle else "–")
          + f" | {len(unsicher)} | {len(ersatz)} | {len(wieder)} von {len(verwendet)} "
          f"({100 * len(wieder) / len(verwendet):.0f} %) | {geltung_txt} | "
          f"Schnitt {len(schnitt_neu)} Werte, {schnitt_bekannt} von {n} Zeilen im Niveau bekannt "
          f"({100 * schnitt_bekannt / n:.0f} %), {len(schnitt_neu - schnitt_alle)} Werte neu im Gesamtbestand | "
          f"{poolquote(ZEILEN, andere)} |")
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
          "(Häufigkeit in Klammern):")
    liste = umschrift_liste(ZEILEN)
    print("  " + ", ".join(f"{w} ({n_})" for w, n_ in liste) if liste else "  keines")
    for w in warnung:
        print("Hinweis:", w)
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
