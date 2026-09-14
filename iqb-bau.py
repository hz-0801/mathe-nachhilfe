# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.4 · 13.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.6

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

Änderungen gegenüber 0.3: Gegenstandsklassen je Thema aus iqb.md § 6
(Präfix „Klasse: " im Typnamen, geprüft für Typenliste und NEUE_TYPEN);
Schnitt Thema × Klasse × Handlung als Kennzahl (Werte im Stapel, davon im
Niveau bekannt). Umbenennungen und Zusammenziehungen laufen über
iqb-abgleich.py.

Änderungen gegenüber 0.2: Geltungstabelle aus iqb.md § 6 (Zeilen außerhalb der
Geltung je Zielprüfung in den Kennzahlen); Eichung auch nach der engen Fassung
(Vermerk „Schätzung enge Fassung: …" in bemerkung) mit Schranke; Schranke für
neue Typen abschaltbar (None); Wiederverwendung im selben Niveau als Kennzahl.

Änderungen gegenüber 0.1: Aufgaben ohne Teilaufgabenbuchstaben (row ohne
teilaufgabe, id gleich Kennung, genau eine Zeile je Datei); Dubletten nach
Spalte dublette_von bekommen keine Zeile und fehlen nicht; Seitenzahl je Datei
aus iqb-quellen.csv statt aus KONFIG.

Abgeleitet aus abi-bau.py v0.2 (Vokabular aus katalog-prompt.md § 5 und dem
Profil § 5–6, Selbstprüfung bei leerem ZEILEN). Neu gegenüber abi-bau.py:
  - Die Einheit ist der Stapel (iqb.md § 7): KONFIG nennt ihn, iqb-quellen.csv
    liefert seine Dateien; fehlt eine, wird nichts geschrieben.
  - row() nimmt die Kennung der Datei und leitet id, jahr, papier, block,
    aufgabe, titel und hilfsmittel aus iqb-quellen.csv ab (iqb.md § 4).
  - afb_amtlich ist Pflicht und wird gegen das Muster geprüft; bemerkung muss
    den Standardbezug nennen.
  - SCHWELLEN: Qualitätsschranke im Skript statt im Urteil des Lehrers.
  - Eichung: Trefferquote niveau_geschaetzt gegen den höchsten amtlichen Bereich.
  - KONFIG["probe"] = True: alle Prüfungen laufen, nichts wird geschrieben.

Ablauf:
  1. iqb.md, katalog-prompt.md, iqb-quellen.csv, iqb-katalog.csv und
     iqb-typen.csv neben dieses Skript legen (aus dem Repo, geprüfter SHA).
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen.
  3. python iqb-bau.py – schreibt beide CSV-Dateien, gibt Prüftabelle und
     Bericht aus. Bei einem Fehler wird nichts geschrieben.
  4. Ist ZEILEN leer, läuft nur die Selbstprüfung über den Gesamtbestand.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    # Stapel nach Spalte stapel in iqb-quellen.csv: Jahr-Niveau-Teil
    "stapel": "2021-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2021MgrundlegendAAnalysis11": 5,
        "2021MgrundlegendAAnalysis12": 5,
        "2021MgrundlegendAAnalysis13": 5,
        "2021MgrundlegendAAnalysis2": 5,
        "2021MgrundlegendAAGLAA111": 5,
        "2021MgrundlegendAAGLAA112": 5,
        "2021MgrundlegendAAGLAA12": 5,
        "2021MgrundlegendAAGLAA211": 5,
        "2021MgrundlegendAStochastik11": 5,
        "2021MgrundlegendAStochastik12": 5,
        "2021MgrundlegendAStochastik2": 5,
    },
    # True: Probelauf – prüfen und berichten, nichts schreiben, Stapel darf
    # unvollständig sein. False: Stapel muss vollständig sein, dann schreiben.
    "probe": False,
}

# ========================================= QUELLEN UND PRÜFUNG, NICHT ÄNDERN
KAT = "iqb-katalog.csv"
TYP = "iqb-typen.csv"
QUELLEN = "iqb-quellen.csv"
PROFIL = "iqb.md"
KERN = "katalog-prompt.md"
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]
QUELLEN_HEAD = ["kennung", "jahr", "niveau", "teil", "sachgebiet", "gruppe",
                "hilfsmittel", "nr", "papier", "stapel", "seiten", "dublette_von"]

# teilaufgabe fehlt: Aufgaben ohne Buchstaben sind eine Zeile mit leerem Feld (iqb.md § 4).
PFLICHT = ("id jahr papier block aufgabe titel seite punkte hilfsmittel afb_amtlich "
           "leitidee thema typ format operator antwort material skizze kontext textumfang gegeben "
           "gesucht verfahren schritte ergebnis niveau_geschaetzt fehlerquelle bemerkung").split()

# Qualitätsschranke (iqb.md § 7). Anteile beziehen sich auf die Zeilen bzw. die
# verwendeten Typen des Stapels; „mindestens" ist die Zahl, die immer erlaubt ist.
SCHWELLEN = {
    "fragezeichen_anteil": 0.10, "fragezeichen_mindestens": 2,
    # Schranke für neue Typen deaktiviert (13.09.2026, Entscheidung des Lehrers),
    # bis der Typenschnitt für Teil A geklärt ist; gemessen wird sie weiter.
    "neue_typen_anteil": None, "neue_typen_ab_bestand": 100,
    "ersatzweise_anteil": 0.10, "ersatzweise_mindestens": 2,
    # Eichung nach der engen Fassung (iqb.md § 7): Trefferquote gegen den
    # höchsten amtlichen Bereich, ab dieser Zeilenzahl im Stapel scharf.
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
# Felder, die bewusst umlautfrei sind: Kennungen und papier-Kürzel (iqb.md § 4).
OHNE_UMLAUT = ("id", "papier", "abhaengig_von")
# Kennungen des Pools, wie sie in bemerkung oder skizze zitiert werden dürfen.
KENNUNG = re.compile(r"(?:\d{4}|Beispielaufgaben)M(?:erhoeht|grundlegend)[AB]"
                     r"(?:Analysis|AGLAA1|AGLAA2|Stochastik)(?:WTR|CAS|MMS)?\d*")
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


def vokabular():
    """Kopfzeile und Formvokabular aus dem Kern, Sachgebiete und Themen aus dem Profil."""
    kern, profil = lies(KERN), lies(PROFIL)

    m = re.search(r"^Kopfzeile:\s*\n(id;.+)$", kern, re.M)
    if not m:
        sys.exit(f"{KERN}: Kopfzeile nicht gefunden.")
    head = m.group(1).strip().split(";")

    v = {feld: liste_aus_klammer(kern, feld, KERN)
         for feld in ("format", "antwort", "material", "zahlenraum",
                      "textumfang", "niveau_geschaetzt")}

    m = re.search(r"trägt das Sachgebiet:\s*\*\*(.+?)\*\*", profil, re.S)
    if not m:
        sys.exit(f"{PROFIL}: Sachgebiete nicht gefunden.")
    leitideen = [s.strip() for s in re.sub(r"\s+", " ", m.group(1)).split("·") if s.strip()]

    themen = {}
    for m in re.finditer(r"^\*\*([^*:]+):\*\*(.+?)(?=\n\s*\n)", profil, re.S | re.M):
        name = m.group(1).strip()
        if name not in leitideen:
            continue
        themen[name] = [s.strip() for s in re.sub(r"\s+", " ", m.group(2)).split("·") if s.strip()]
    fehlt = [l for l in leitideen if l not in themen]
    if fehlt:
        sys.exit(f"{PROFIL}: keine Themenzeile für {fehlt}")
    return head, v, leitideen, themen


def geltung():
    """Geltungstabelle aus iqb.md § 6: Thema × Zielprüfung, ja/nein.
    Liefert (Zielprüfungen, {thema: Menge der Zielprüfungen mit ja})."""
    profil = lies(PROFIL)
    m = re.search(r"^\| Thema \|(.+?)\|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)", profil, re.M)
    if not m:
        sys.exit(f"{PROFIL}: Geltungstabelle nicht gefunden.")
    ziele = [z.strip() for z in m.group(1).split("|") if z.strip()]
    tab = {}
    for zeile in m.group(2).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != len(ziele) + 1:
            sys.exit(f"{PROFIL}: Geltungszeile hat {len(zellen)} Zellen: {zeile}")
        thema, werte = zellen[0], zellen[1:]
        if any(w not in ("ja", "nein") for w in werte):
            sys.exit(f"{PROFIL}: Geltung muss ja oder nein sein: {zeile}")
        tab[thema] = {z for z, w in zip(ziele, werte) if w == "ja"}
    alle = {t for liste in THEMEN.values() for t in liste}
    fehlt = sorted(alle - set(tab))
    if fehlt:
        sys.exit(f"{PROFIL}: Themen ohne Geltungszeile: {fehlt}")
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{PROFIL}: Geltungszeilen ohne Thema in der Liste: {fremd}")
    return ziele, tab


def quellen():
    """iqb-quellen.csv: Kennung -> Zeile (Zerlegung, papier, stapel)."""
    with io.open(QUELLEN, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    if not rows or rows[0] != QUELLEN_HEAD:
        sys.exit(f"{QUELLEN}: Kopfzeile weicht ab")
    q = {}
    for r in rows[1:]:
        d = dict(zip(QUELLEN_HEAD, r))
        q[d["kennung"]] = d
    return q


def klassen():
    """Gegenstandsklassen je Thema aus iqb.md § 6 (Tabelle „Thema | Gegenstandsklassen").
    Liefert {thema: [Klasse, ...]}; Themen ohne Zeile führen keine Unterklasse."""
    profil = lies(PROFIL)
    m = re.search(r"^\| Thema \| Gegenstandsklassen \|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)",
                  profil, re.M)
    if not m:
        sys.exit(f"{PROFIL}: Tabelle der Gegenstandsklassen nicht gefunden.")
    tab = {}
    for zeile in m.group(1).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != 2:
            sys.exit(f"{PROFIL}: Klassenzeile hat {len(zellen)} Zellen: {zeile}")
        tab[zellen[0]] = [k.strip() for k in zellen[1].split("·") if k.strip()]
    alle = {t for liste in THEMEN.values() for t in liste}
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{PROFIL}: Klassenzeilen ohne Thema in der Liste: {fremd}")
    return tab


HANDLUNG = {"Rechnung": "berechnen", "Begründung": "begründen", "Kurzantwort": "angeben",
            "Ankreuzen": "angeben", "Zeichnen": "zeichnen", "Eintragen": "zeichnen",
            "Konstruieren": "zeichnen", "Tabelle": "angeben"}


def klasse_von(typ):
    """Gegenstandsklasse aus dem Typnamen (Wort vor dem Doppelpunkt) oder leer."""
    m = re.match(r"([^:]+): ", typ)
    return m.group(1) if m else ""


def pruefe_typname(typ, thema, a, wo):
    """Präfixregel iqb.md § 6: Themen mit Klassen verlangen ein gültiges Präfix, andere keins."""
    k = klasse_von(typ)
    if thema in KLASSEN:
        a(k in KLASSEN[thema],
          f"{wo}: Typ „{typ}“ braucht ein Präfix aus {KLASSEN[thema]} (Thema {thema})")
    else:
        a(k == "", f"{wo}: Typ „{typ}“ trägt ein Präfix, Thema {thema} führt keine Klassen")


HEAD, VOK, LEITIDEEN, THEMEN = vokabular()
ZIELE, GELTUNG = geltung()
KLASSEN = klassen()
QUELLE = quellen()


def aufgabe_aus(q):
    """Feld aufgabe nach iqb.md § 4: Teil A Gruppe[.Nr], Teil B (vorläufig) Nr."""
    if q["teil"] == "A":
        return q["gruppe"] + ("." + q["nr"] if q["nr"] else "")
    return q["nr"]


# ======================================================== AB HIER JE STAPEL
ZEILEN = []


def row(kennung, teilaufgabe="", **kw):
    """Eine Zeile. id, jahr, papier, block, aufgabe, titel, stern und hilfsmittel
    kommen aus der Kennung (iqb-quellen.csv); teilaufgabe bleibt leer, wenn die
    Aufgabe keine Buchstaben hat (id ist dann die Kennung); in Teil B ist innen=
    die Aufgabennummer innerhalb der Datei (vorläufig, iqb.md § 9)."""
    if kennung not in QUELLE:
        sys.exit(f"{kennung}: nicht in {QUELLEN}")
    q = QUELLE[kennung]
    innen = kw.pop("innen", "")
    z = {k: "" for k in HEAD}
    suffix = f"-{innen}{teilaufgabe}" if (innen or teilaufgabe) else ""
    z.update(id=kennung + suffix, jahr=q["jahr"], papier=q["papier"],
             block=q["teil"], titel=q["sachgebiet"], teilaufgabe=teilaufgabe, stern="",
             hilfsmittel="nein" if q["teil"] == "A" else "ja")
    z["aufgabe"] = aufgabe_aus(q) if q["teil"] == "A" else (
        f"{q['nr']}.{innen}" if q["nr"] else innen)
    unbekannt = set(kw) - set(HEAD)
    if unbekannt:
        sys.exit(f"{z['id']}: unbekanntes Feld: {sorted(unbekannt)}")
    fest = set(kw) & {"id", "jahr", "papier", "block", "aufgabe", "titel", "teilaufgabe",
                      "stern", "hilfsmittel"}
    if fest:
        sys.exit(f"{z['id']}: {sorted(fest)} werden aus der Kennung abgeleitet, nicht übergeben")
    z.update(kw)
    z["_kennung"] = kennung
    ZEILEN.append(z)


# ============================================================ ZEILEN JE STAPEL
# Ein Eintrag je Teilaufgabe. Nicht genannte Felder bleiben leer.
# niveau_geschaetzt nach der Deutungsliste v0.7 (Nullfall-Regel); bei III nennt bemerkung den Eintrag.

# ---- Analysis 1.1: Graph von f und Graph von F
FF_SKIZZE = ("zwei Koordinatensysteme mit Gitter (Schrittweite 1), x-Achse 0 bis 7,5, y-Achse −1,5 bis 2,5. "
             "Abb. 1 Graph von f: bei (0; 2) beginnend fallend, Nullstelle bei 1, Tiefpunkt etwa (2,5; −1), "
             "Nullstelle bei 4, Hochpunkt etwa (6,5; 1), dann fallend. Abb. 2 Graph von F: von links unten "
             "steigend, Hochpunkt etwa (1,2; 1,7) mit F(1) ≈ 1,7, fallend durch (2,5; 0), Tiefpunkt etwa (4; −1,5), "
             "steigend mit F(5) ≈ −1,3, Nullstelle etwa 6,5, weiter steigend bis (7,5; 0,8)")
row("2021MgrundlegendAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Integral über f aus dem Graphen der Stammfunktion bestimmen", typ_neben="",
    stichwoerter="Integral von 1 bis 5 über f = F(5) − F(1)|F(5) ≈ −1,3, F(1) ≈ 1,7|Wert −3",
    voraussetzungen="Hauptsatz|Werte am Graphen von F ablesen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=FF_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Abb. 1 Graph von f, Abb. 2 Graph einer Stammfunktion F mit F(1) ≈ 1,7 und F(5) ≈ −1,3; nur Abb. 2 darf verwendet werden",
    gesucht="Wert des Integrals von 1 bis 5 über f(x) dx",
    verfahren="Hauptsatz mit den abgelesenen Werten",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="F(5) − F(1) ≈ −1,3 − 1,7 = −3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="F(1) − F(5) rechnen (Vorzeichen)",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. Amtlich, Werte aus der Abbildung. Typ aus 2022-ea-A wiederverwendet.")

row("2021MgrundlegendAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Vorgehen zur grafischen Bestimmung eines Integrals beschreiben", typ_neben="",
    stichwoerter="Kästchen zwischen Graph von f und x-Achse für 1 ≤ x ≤ 5 zählen|Kästchenfläche 0,25|Graph unterhalb der Achse: mit −1 multiplizieren",
    voraussetzungen="Integral als orientierte Fläche|Kästchengröße aus dem Gitter|Vorzeichen unterhalb der Achse",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=FF_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Abb. 1 Graph von f (zwischen 1 und 4 unterhalb, zwischen 4 und 5 oberhalb der x-Achse); nur Abb. 1 darf verwendet werden",
    gesucht="Beschreibung, wie der Wert des Integrals von 1 bis 5 über f(x) dx mit Abb. 1 bestimmt werden könnte",
    verfahren="Kästchen zählen, mit 0,25 multiplizieren, Vorzeichen beachten",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2021MgrundlegendAAnalysis11-a",
    ergebnis="man könnte die Anzahl der Kästchen bestimmen, die der Graph von f für 1 ≤ x ≤ 5 mit der x-Achse einschließt; multipliziert man die Anzahl der Kästchen mit 0,25 und mit −1, so erhält man den gesuchten Wert (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="das Flächenstück oberhalb der Achse (4 bis 5) mit demselben Vorzeichen zählen",
    bemerkung="Standardbezug: K1 I, K4 I, K6 II. Amtlich. Vom Typ „Integralwert: Integralwert grafisch durch Kästchenzählen bestimmen“ (2026-ga-A) getrennt: dort wird gezählt, hier das Vorgehen beschrieben (andere Handlung).")

# ---- Analysis 1.2: x³ − x
row("2021MgrundlegendAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Unpassende Graphen zu einem Funktionsterm ausschließen", typ_neben="",
    stichwoerter="f(x) = x³ − x, Nullstellen −1, 0, 1|Graph II: f(0,5) < 0, dort aber positiv|Graph III: Steigung zwischen −0,5 und 0,5 konstant, f' nicht konstant",
    voraussetzungen="Funktionswert prüfen|Ableitung nicht konstant",
    format="Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze="drei kleine Skizzen ohne Gitter mit Nullstellen −1, 0, 1: I kubische Kurve, zwischen −1 und 0 oberhalb, zwischen 0 und 1 unterhalb der Achse; II umgekehrt (zwischen 0 und 1 oberhalb); III Streckenzug mit denselben Nullstellen, zwischen −0,5 und 0,5 geradlinig",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − x in IR; Graphen I, II, III, einer stellt f dar",
    gesucht="die Graphen, die nicht infrage kommen, mit Begründung",
    verfahren="Vorzeichen eines Funktionswerts und Nichtkonstanz der Steigung prüfen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="der Graph II kommt nicht infrage, da f(0,5) < 0 gilt, der Graph III nicht, da die Steigung des Graphen von f für −0,5 ≤ x ≤ 0,5 nicht konstant ist (amtlich)",
    zwischenergebnis="f(0,5) = −0,375",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Nullstellen prüfen (alle drei passen)",
    bemerkung="Standardbezug: K1 II, K4 II. Amtlich, eigene Rechnung bestätigt.")

row("2021MgrundlegendAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen", typ_neben="",
    stichwoerter="Nullstellen −1, 0, 1|Punktsymmetrie: 2 · Integral von −1 bis 0|[1/4 x⁴ − 1/2 x²] = 1/4|Inhalt 1/2",
    voraussetzungen="Nullstellen|Symmetrie oder Beträge|Stammfunktion",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − x",
    gesucht="Inhalt der Fläche, die Graph und x-Achse einschließen",
    verfahren="zwei Flächenstücke, über Symmetrie eines verdoppeln",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="2 · Integral von −1 bis 0 über (x³ − x) dx = 2 · [1/4 x⁴ − 1/2 x²] von −1 bis 0 = 2 · (−1/4 + 1/2) = 1/2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Integral von −1 bis 1 bilden (ergibt 0)",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2024-ga-A wiederverwendet.")

# ---- Analysis 1.3: sin x + 1
row("2021MgrundlegendAAnalysis13", "a", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Bestimmtes Integral einer trigonometrischen Funktion über eine Periode berechnen", typ_neben="",
    stichwoerter="Integral von 0 bis 2π über (sin x + 1)|Integral über sin über eine Periode 0|Integral über 1 gleich 2π",
    voraussetzungen="Stammfunktion von sin|Integral über eine volle Periode|Summenregel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = sin(x) + 1 in IR",
    gesucht="Wert des Integrals von 0 bis 2π über f(x) dx",
    verfahren="Integral aufspalten",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Integral von 0 bis 2π über f(x) dx = Integral über sin(x) dx + Integral über 1 dx = 0 + 2π = 2π (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Stammfunktion von sin als cos statt −cos (ändert hier nichts, aber Rechenfehler bei anderen Grenzen)",
    bemerkung="Standardbezug: K5 II. Amtlich, eigene Rechnung bestätigt.")

row("2021MgrundlegendAAnalysis13", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Funktionsterm nach Streckung in x-Richtung und Verschiebung angeben", typ_neben="",
    stichwoerter="Strecken mit Faktor 0,2 in x-Richtung: f(5x)|Verschieben um 3 in y-Richtung: + 3|g(x) = sin(5x) + 4",
    voraussetzungen="Streckung in x-Richtung mit Faktor k als f(x/k)|Verschiebung in y-Richtung als Summand",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = sin(x) + 1; Graph von g entsteht durch Strecken mit Faktor 0,2 in x-Richtung und Verschieben um 3 in positive y-Richtung",
    gesucht="Funktionsterm von g",
    verfahren="f(5x) + 3 vereinfachen",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="sin(5x) + 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="sin(0,2x) ansetzen (Faktor statt Kehrwert)",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 2: 3x · e^x
XE_SKIZZE = ("Koordinatensystem mit Gitter (Schrittweite 1), x-Achse von −3,5 bis 3,5, y-Achse von −3,5 bis 3,5; "
             "Graph von f: von links nahe 0 unter der Achse, Tiefpunkt (−1; −1,1), Nullstelle im Ursprung, dann "
             "steil steigend, bei x = 0,5 etwa 2,5")
row("2021MgrundlegendAAnalysis2", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen", typ_neben="",
    stichwoerter="f(x) = 3x · e^x|Produktregel f'(x) = 3e^x + 3x · e^x = 3e^x(1 + x)|f'(−1) = 0|genau eine Extremstelle vorausgesetzt",
    voraussetzungen="Produktregel|e^x ≠ 0",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=XE_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3x · e^x in IR mit genau einer Extremstelle; Graph in der Abbildung",
    gesucht="rechnerischer Nachweis, dass die Extremstelle −1 ist",
    verfahren="ableiten und −1 einsetzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 3e^x + 3x · e^x, f'(−1) = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Produktregel vergessen (f' = 3e^x)",
    bemerkung="Standardbezug: K2 I, K5 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet; die hinreichende Bedingung entfällt, weil genau eine Extremstelle vorausgesetzt ist.")

row("2021MgrundlegendAAnalysis2", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Graph einer Stammfunktion durch einen Punkt skizzieren", typ_neben="",
    stichwoerter="F' = f|f < 0 für x < 0: F fällt, f > 0 für x > 0: F steigt|Tiefpunkt von F im Ursprung|Wendepunkt von F bei −1|links flach gegen eine Asymptote",
    voraussetzungen="Vorzeichen von f als Monotonie von F|Nullstelle von f mit Vorzeichenwechsel als Tiefpunkt|Extremstelle von f als Wendestelle von F",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=XE_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph von f in der Abbildung; F Stammfunktion durch den Koordinatenursprung; nur der Graph von f darf verwendet werden",
    gesucht="Skizze des Graphen von F in der Abbildung",
    verfahren="fallend von links (flach) mit Wendepunkt über −1, Tiefpunkt im Ursprung, danach steil steigend",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Graph mit Tiefpunkt im Ursprung, links davon fallend mit Wendepunkt bei x = −1 und flach auslaufend (gegen 3), rechts steil steigend; der Erwartungshorizont zeigt die Skizze (amtlich)",
    zwischenergebnis="F(x) = 3(x − 1)e^x + 3",
    niveau_geschaetzt="III",
    fehlerquelle="Tiefpunkt von f (bei −1) als Tiefpunkt von F zeichnen",
    bemerkung="Standardbezug: K1 III, K2 II, K4 III. Amtlich, eigene Rechnung bestätigt. Typ aus 2023-ea-A wiederverwendet. Eichregel: (e) Beziehung Funktion–Stammfunktion am Graphen deuten.")

# ---- AG/LA (A1) 1.1: Verflechtung (Datei mit drei Seiten, b auf Seite 2)
VERFL_SKIZZE = ("Verflechtungsdiagramm mit drei Ebenen: unten R1, R2; Mitte Z1, Z2, Z3; oben E1, E2. Pfeile mit "
                "Mengen: R1→Z1 1, R1→Z2 2, R2→Z2 1, R2→Z3 2; Z1→E1 1, Z1→E2 2, Z2→E2 2, Z3→E1 1, Z3→E2 1")
row("2021MgrundlegendAAGLAA111", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Verflechtungsmatrix aus dem Diagramm angeben", typ_neben="",
    stichwoerter="z = M · e|Zeilen Z1, Z2, Z3, Spalten E1, E2|M = ((1; 2), (0; 2), (1; 1))",
    voraussetzungen="Bedarf je Endprodukt als Spalte lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Diagramm", skizze=VERFL_SKIZZE, kontext="Produktion", textumfang="lang",
    gegeben="Rohstoffe R1, R2, Zwischenprodukte Z1, Z2, Z3, Endprodukte E1, E2 mit Bedarfen im Diagramm; r = ((1; 6), (2; 4)) · e",
    gesucht="Matrix M mit z = M · e",
    verfahren="Bedarf an Zwischenprodukten je Endprodukt aus dem Diagramm ablesen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="M = ((1; 2), (0; 2), (1; 1)) (amtlich)",
    zwischenergebnis="Kontrolle: Rohstoffmatrix ((1; 2; 0), (0; 1; 2)) mal M ergibt ((1; 6), (2; 4))",
    niveau_geschaetzt="I",
    fehlerquelle="Matrix transponiert angeben (2×3)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt. Datei mit drei Seiten. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2021MgrundlegendAAGLAA111", "b", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Produktionsmengen aus dem Rohstoffverbrauch über ein Gleichungssystem ermitteln", typ_neben="",
    stichwoerter="((1; 6), (2; 4)) · e = (28; 40)|I e1 + 6e2 = 28, II 2e1 + 4e2 = 40|e2 = 2, e1 = 16",
    voraussetzungen="Matrix-Vektor-Gleichung als Gleichungssystem|zwei Gleichungen lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=VERFL_SKIZZE, kontext="Produktion", textumfang="mittel",
    gegeben="r = ((1; 6), (2; 4)) · e; verbraucht 28 Mengeneinheiten R1 und 40 Mengeneinheiten R2",
    gesucht="hergestellte Mengeneinheiten von E1 und E2",
    verfahren="Gleichungssystem aufstellen und lösen",
    schritte="2", zahlenraum="ganz", einheiten="Mengeneinheiten", abhaengig_von="",
    ergebnis="((1; 6), (2; 4)) · (e1; e2) = (28; 40) liefert I e1 + 6e2 = 28, II 2e1 + 4e2 = 40; aus I ergibt sich 2e1 + 12e2 = 56 und daraus mit II e2 = 2, damit aus I e1 = 16 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Matrix mit r statt e multiplizieren",
    bemerkung="Standardbezug: K2 II, K3 I, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2.")

# ---- AG/LA (A1) 1.2: A(5; 0; a), B(2; 4; 5) (Sachgebiet „AG/LA“, Dublette 2021MgrundlegendAAGLAA212)
row("2021MgrundlegendAAGLAA112", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Koordinate eines Vektors aus vorgegebener Länge bestimmen", typ_neben="",
    stichwoerter="AB = (−3; 4; 5 − a)|√(25 + (5 − a)²) = 5|a = 5",
    voraussetzungen="Betrag eines Vektors|Gleichung mit Quadrat",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(5; 0; a), B(2; 4; 5)",
    gesucht="Wert von a, für den A und B den Abstand 5 haben",
    verfahren="Betragsgleichung lösen",
    schritte="2", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="|AB| = |(−3; 4; 5 − a)| = √(25 + (5 − a)²) = 5 ⇔ a = 5 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="(5 − a)² = 0 übersehen und zwei Lösungen erwarten",
    bemerkung="Standardbezug: K2 I, K5 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2025-ea-A wiederverwendet. Die Kurzbeschreibung nennt nur AG/LA; die Datei liegt wortgleich als 2021MgrundlegendAAGLAA212 ein zweites Mal vor (Dublette ohne Zeile).")

row("2021MgrundlegendAAGLAA112", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln", typ_neben="",
    stichwoerter="rechter Winkel bei B: OB · AB = 0|(2; 4; 5) · (−3; 4; 5 − a) = 35 − 5a|a = 7",
    voraussetzungen="rechter Winkel als Skalarprodukt der anliegenden Vektoren|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="O Ursprung, A(5; 0; a), B(2; 4; 5)",
    gesucht="Wert von a, für den das Dreieck OAB bei B rechtwinklig ist",
    verfahren="Skalarprodukt BO · BA null setzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="OB · AB = (2; 4; 5) · (−3; 4; 5 − a) = 35 − 5a = 0 ⇔ a = 7 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Skalarprodukt OA · OB ansetzen (rechter Winkel bei O)",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2024-ga-A wiederverwendet.")

# ---- AG/LA (A1) 2: Quader mit Ortsvektoren (Sachgebiet „AG/LA“, Dublette 2021MgrundlegendAAGLAA22)
QUADER_SKIZZE = ("Schrägbild eines Quaders OABC DEFG über quadratischer Grundfläche OABC in der xy-Ebene, D über O, "
                 "Kante OD deutlich länger als OA; Vektoren a = OA (x-Richtung), b = OB (Diagonale der Grundfläche, "
                 "gestrichelt) und d = OD (z-Richtung) eingezeichnet; Achsen x nach vorn links, y nach rechts, z nach oben")
row("2021MgrundlegendAAGLAA12", "a", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Lage eines Punktes zu einem Vektorterm im Quader beschreiben", typ_neben="",
    stichwoerter="1/2 · (b − a) = 1/2 · AB = 1/2 · OC|Mittelpunkt der Strecke OC",
    voraussetzungen="b − a als Verbindungsvektor AB|AB = OC im Quadrat|halber Vektor als Mittelpunkt",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Körper", skizze=QUADER_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Quader mit quadratischer Grundfläche OABC, Ortsvektoren a, b, d der Punkte A, B, D",
    gesucht="Lage des Punktes mit Ortsvektor 1/2 · (b − a)",
    verfahren="b − a als OC deuten und halbieren",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="der Punkt ist der Mittelpunkt der Strecke OC (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den Mittelpunkt von AB nennen",
    bemerkung="Standardbezug: K4 II, K6 I. Amtlich, eigene Rechnung bestätigt. Die Kurzbeschreibung nennt nur AG/LA; die Datei liegt wortgleich als 2021MgrundlegendAAGLAA22 ein zweites Mal vor (Dublette ohne Zeile).")

row("2021MgrundlegendAAGLAA12", "b", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Punkt zu einem Vektorterm in das Schrägbild einzeichnen", typ_neben="",
    stichwoerter="OP = 1/2 · b + d|halbe Grunddiagonale, dann Höhe|P Mittelpunkt der Deckfläche DEFG",
    voraussetzungen="Vektoraddition im Bild ausführen",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Körper", skizze=QUADER_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="P mit Ortsvektor 1/2 · b + d",
    gesucht="P in der Abbildung",
    verfahren="vom Ursprung halb entlang b, dann um d nach oben",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="P ist der Mittelpunkt der Deckfläche DEFG, im Erwartungshorizont eingezeichnet (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="P auf der Kante DG statt in der Flächenmitte",
    bemerkung="Standardbezug: K4 I. Amtlich.")

row("2021MgrundlegendAAGLAA12", "c", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Abhängigkeit eines Skalarprodukts nur von der Seitenlänge allgemein begründen", typ_neben="",
    stichwoerter="b · OP = b · (1/2 b + d) = 1/2 · (b · b) + b · d|b senkrecht zu d: b · d = 0|Wert 1/2 · |b|²|b ist die Diagonale des Quadrats, hängt nur von der Seitenlänge ab",
    voraussetzungen="Distributivgesetz des Skalarprodukts|b · b = |b|²|Orthogonalität von Grundfläche und Höhe",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=QUADER_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Quader mit quadratischer Grundfläche; OP = 1/2 · b + d",
    gesucht="Begründung, dass b · OP nur von der Seitenlänge der Grundfläche abhängt",
    verfahren="Skalarprodukt ausmultiplizieren, b · d = 0 erkennen, |b| über die Diagonale",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2021MgrundlegendAAGLAA12-b",
    ergebnis="b · OP = b · (1/2 · b + d) = 1/2 · (b · b) + b · d = 1/2 · |b|²; die Länge des Vektors b hängt nur von der Seitenlänge der Grundfläche ab (amtlich)",
    zwischenergebnis="Wert s² bei Seitenlänge s",
    niveau_geschaetzt="III",
    fehlerquelle="mit Koordinaten rechnen wollen, obwohl keine gegeben sind",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt (Koordinatenmodell). Eichregel: (c) allgemeiner Nachweis ohne Koordinaten mit der hergeleiteten Beziehung b · OP = |b|²/2 und (b) Orthogonalität b ⊥ d erkennen.")

# ---- AG/LA (A2) 1.1: Gleichungssystem mit zwei Variablen (Sachgebiet „AG/LA“)
row("2021MgrundlegendAAGLAA211", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lösungsmenge eines Gleichungssystems mit zwei Variablen als Gerade zeichnen und eine Lösung angeben", typ_neben="",
    stichwoerter="I −x + y = −3, II 2x − 2y = 6, II = −2 · I|Lösungen: Gerade y = x − 3|y = 1 gibt x = 4",
    voraussetzungen="abhängige Gleichungen|Gerade zeichnen|Wert einsetzen",
    format="Zeichnen|Kurzantwort", operator="Stellen Sie dar|Geben Sie an", antwort="Grafik|Zahl",
    material="keins", skizze="zu zeichnen: Koordinatensystem mit Gitter, Gerade y = x − 3 durch (0; −3) und (3; 0)",
    kontext="ohne", textumfang="kurz",
    gegeben="I −x + y = −3, II 2x − 2y = 6 mit reellen x, y; unendlich viele Lösungen",
    gesucht="grafische Darstellung der Lösungen; die Lösung mit y = 1",
    verfahren="Gerade y = x − 3 zeichnen, y = 1 einsetzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Gerade y = x − 3 im Koordinatensystem; für y = 1 gilt x = 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Gerade mit Steigung −1 zeichnen",
    bemerkung="Standardbezug: K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Die Kurzbeschreibung nennt nur AG/LA.")

row("2021MgrundlegendAAGLAA211", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Koeffizienten für ein unlösbares Gleichungssystem angeben und begründen", typ_neben="",
    stichwoerter="II*: a · x − 3y = b|parallel zu I: a = 3|b so, dass Widerspruch: b = −3|3 · I + II* liefert 0 = −12",
    voraussetzungen="unlösbar heißt parallele Geraden|Koeffizientenvielfaches mit anderer rechter Seite",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="I −x + y = −3; II* a · x − 3y = b mit reellen a, b",
    gesucht="Werte von a und b, für die I und II* keine Lösung haben, mit Begründung",
    verfahren="II* als Vielfaches der linken Seite von I mit unpassender rechter Seite wählen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2021MgrundlegendAAGLAA211-a",
    ergebnis="a = 3, b = −3; Begründung: 3 · I + II* liefert 0 = −12 (amtlich)",
    zwischenergebnis="jedes b ≠ −9 mit a = 3 ist möglich",
    niveau_geschaetzt="II",
    fehlerquelle="a = −3 wählen (dann eindeutig lösbar)",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 1.1: Allergietest
row("2021MgrundlegendAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen", typ_neben="",
    stichwoerter="P(kein Heuschnupfen) = 0,85|P(positiv | kein Heuschnupfen) = 0,02|0,85 · 0,02 = 0,017",
    voraussetzungen="Gegenwahrscheinlichkeit|Pfadregel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Allergietest", textumfang="mittel",
    gegeben="P(Heuschnupfen) = 15 %; Test positiv bei Heuschnupfen mit 90 %; Test positiv ohne Heuschnupfen mit 2 %",
    gesucht="Wahrscheinlichkeit, dass eine Person keinen Heuschnupfen hat und der Test positiv ist",
    verfahren="Produkt der Pfadwahrscheinlichkeiten",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,85 · 0,02 = 0,017 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="0,15 · 0,02 rechnen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2024-ga-A wiederverwendet.")

row("2021MgrundlegendAStochastik11", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bayes-Term im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Zähler 0,15 · 0,9 = P(Heuschnupfen und positiv)|Nenner 0,15 · 0,9 + 0,85 · 0,02 = P(positiv)|Quotient P(Heuschnupfen | positiv)",
    voraussetzungen="Pfade im Zähler und Nenner erkennen|bedingte Wahrscheinlichkeit als Quotient",
    format="Kurzantwort", operator="Deuten Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Allergietest", textumfang="kurz",
    gegeben="Term 0,15 · 0,9 / (0,15 · 0,9 + 0,85 · 0,02)",
    gesucht="Deutung des Terms im Sachzusammenhang",
    verfahren="Zähler und Nenner als Pfade lesen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="der Term gibt die Wahrscheinlichkeit dafür an, dass eine zufällig ausgewählte Person, bei der der Test positiv ist, tatsächlich Heuschnupfen hat (amtlich)",
    zwischenergebnis="Wert ≈ 0,888",
    niveau_geschaetzt="II",
    fehlerquelle="Bedingung umkehren (Test positiv, wenn Heuschnupfen)",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt. Eine Deutung (Term als bedingte Wahrscheinlichkeit), nach dem Prinzip II.")

# ---- Stochastik 1.2: keine Sechs bei zwei Würfeln
SAEULEN_SKIZZE = ("drei Säulendiagramme über k = 0 bis 40: Abb. 1 Maximum etwa 0,13 bei 20, Werte etwa 12 bis 28; "
                  "Abb. 2 Maximum etwa 0,29 bei 25, y-Achse bis 0,35, Werte etwa 17 bis 32; Abb. 3 Maximum etwa "
                  "0,08 bei 25, y-Achse bis 0,1, Werte etwa 12 bis 38")
row("2021MgrundlegendAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen", typ_neben="",
    stichwoerter="ein Würfel keine 6: 5/6|beide: 5/6 · 5/6 = 25/36",
    voraussetzungen="Gegenwahrscheinlichkeit|Unabhängigkeit der Würfel",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Würfel", textumfang="kurz",
    gegeben="zwei Würfel mit 1 bis 6, einmal gemeinsam geworfen",
    gesucht="Begründung, dass P(keine 6) = 25/36",
    verfahren="Produkt der Einzelwahrscheinlichkeiten",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="die Wahrscheinlichkeit dafür, dass einer der beiden Würfel keine 6 zeigt, ist 5/6; damit ergibt sich für beide Würfel 5/6 · 5/6 = 25/36 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="1 − 2/6 = 4/6 rechnen",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet (zusammengezogener Typ).")

row("2021MgrundlegendAStochastik12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen", typ_neben="",
    stichwoerter="X ~ B(36; 25/36), E(X) = 25|Abb. 1: höchste Säule bei 20 statt 25|Abb. 2: Summe der Säulen größer als 1|Abb. 3: Säule bei 37 > 0, aber n = 36",
    voraussetzungen="Erwartungswert n · p|Summe der Wahrscheinlichkeiten 1|Wertebereich 0 bis n",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Diagramm", skizze=SAEULEN_SKIZZE, kontext="Würfel", textumfang="mittel",
    gegeben="36 Würfe; X Anzahl der Würfe ohne 6, binomialverteilt mit p = 25/36; Abb. 1 bis 3",
    gesucht="je Abbildung eine Begründung, dass sie nicht die Verteilung von X zeigt",
    verfahren="je ein Merkmal prüfen: Lage des Maximums, Summe, Wertebereich",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="2021MgrundlegendAStochastik12-a",
    ergebnis="Abb. 1: die höchste Säule befindet sich bei 20, nicht bei 25; Abb. 2: die Summe der Höhen der Säulen ist größer als 1; Abb. 3: die Höhe der Säule bei 37 ist größer als null (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Abb. 2 nur wegen der Form ablehnen",
    bemerkung="Standardbezug: K1 II, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt (E(X) = 25).")

# ---- Stochastik 2: Bernoulli-Term, symmetrische Verteilung
SYM_SKIZZE = ("Säulendiagramm P(Y = k) für k = 0 bis 27 ohne y-Skala: Säulen von etwa 6 bis 21, symmetrisch um 13,5, "
              "höchste Säulen bei 13 und 14, gleich hohe Säulen bei 12 und 15")
row("2021MgrundlegendAStochastik2", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben", typ_neben="",
    stichwoerter="P(X = □) = (□ über 3) · (□)² · (1/4)³|p = 1/4, drei Treffer, zwei Nieten|n = 5, k = 3, Niete 3/4",
    voraussetzungen="Bernoulli-Formel|Platzhalter aus Exponenten ablesen",
    format="Kurzantwort", operator="Vervollständigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X binomialverteilt mit p = 1/4; Gleichung P(X = □) = (□ über 3) · (□)² · (1/4)³ mit Platzhaltern",
    gesucht="vervollständigte Gleichung",
    verfahren="Anzahl der Treffer 3 aus (1/4)³, n = 3 + 2, Nietenwahrscheinlichkeit 3/4",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="P(X = 3) = (5 über 3) · (3/4)² · (1/4)³ (amtlich)",
    zwischenergebnis="Wert 90/1024",
    niveau_geschaetzt="II",
    fehlerquelle="n = 3 oder (1/4)² einsetzen",
    bemerkung="Standardbezug: K1 II, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet.")

row("2021MgrundlegendAStochastik2", "b", seite="1", punkte="3", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen", typ_neben="",
    stichwoerter="Symmetrie um 13,5: P(Y = 15) = P(Y = 12) ≈ 0,13, P(Y ≤ 13) = 0,5|P(Y = 14) = P(Y ≤ 15) − P(Y = 15) − P(Y ≤ 13)|0,78 − 0,13 − 0,5 = 0,15",
    voraussetzungen="Symmetrieachse aus dem Diagramm|Symmetrie der Einzelwahrscheinlichkeiten|Zerlegung kumulierter Wahrscheinlichkeiten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=SYM_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="symmetrische Verteilung von Y im Diagramm (Symmetrie um 13,5); P(Y ≤ 15) ≈ 0,78, P(Y = 12) ≈ 0,13",
    gesucht="P(Y = 14) aus diesen Werten",
    verfahren="Symmetrie liefert P(Y = 15) und P(Y ≤ 13) = 0,5, dann Differenz",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="mit P(Y = 15) = P(Y = 12) ergibt sich P(Y = 14) = P(Y ≤ 15) − P(Y = 15) − P(Y ≤ 13) ≈ 0,78 − 0,13 − 0,5 = 0,15 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Symmetrieachse bei 14 statt 13,5 annehmen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2025-ga-A wiederverwendet. Eichregel: (b) Symmetrie um 13,5 erkennen und ausnutzen, mit der Zerlegung der kumulierten Wahrscheinlichkeit verkettet.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Integralwert: Vorgehen zur grafischen Bestimmung eines Integrals beschreiben", "Analysis",
     "Flächeninhalt durch Integration",
     "Beschreiben, wie ein bestimmtes Integral aus dem Graphen bestimmt werden kann (Kästchen zählen, "
     "Kästchenfläche, Vorzeichen), ohne es auszuführen.",
     "2021MgrundlegendAAnalysis11-b"),
    ("Nullstellen und Werte: Unpassende Graphen zu einem Funktionsterm ausschließen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Unter vorgelegten Graphen die ausschließen, die nicht zum Term passen, über einen Funktionswert oder die "
     "Nichtkonstanz der Steigung.",
     "2021MgrundlegendAAnalysis12-a"),
    ("Bestimmtes Integral einer trigonometrischen Funktion über eine Periode berechnen", "Analysis",
     "Stammfunktion und Hauptsatz",
     "Ein bestimmtes Integral über sin oder cos plus Konstante über eine volle Periode berechnen (der "
     "trigonometrische Anteil liefert null).",
     "2021MgrundlegendAAnalysis13-a"),
    ("Transformation: Funktionsterm nach Streckung in x-Richtung und Verschiebung angeben", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Den Term der Funktion angeben, deren Graph durch Streckung in x-Richtung und Verschiebung in "
     "y-Richtung aus einem gegebenen Graphen entsteht.",
     "2021MgrundlegendAAnalysis13-b"),
    ("Verflechtung: Verflechtungsmatrix aus dem Diagramm angeben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Die Matrix einer Produktionsstufe aus den Bedarfsangaben eines Verflechtungsdiagramms angeben.",
     "2021MgrundlegendAAGLAA111-a"),
    ("Verflechtung: Produktionsmengen aus dem Rohstoffverbrauch über ein Gleichungssystem ermitteln",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Die hergestellten Mengen der Endprodukte aus dem Rohstoffverbrauch über die Matrix-Vektor-Gleichung "
     "als lineares Gleichungssystem ermitteln.",
     "2021MgrundlegendAAGLAA111-b"),
    ("Lage eines Punktes zu einem Vektorterm im Quader beschreiben", "Analytische Geometrie",
     "Vektoren und Rechenoperationen",
     "Die Lage des Punktes beschreiben, dessen Ortsvektor als Term aus den Ortsvektoren der Ecken eines "
     "Quaders gegeben ist (Mittelpunkt einer Strecke, Flächenmitte).",
     "2021MgrundlegendAAGLAA12-a"),
    ("Punkt zu einem Vektorterm in das Schrägbild einzeichnen", "Analytische Geometrie",
     "Vektoren und Rechenoperationen",
     "Den Punkt mit einem als Vektorterm gegebenen Ortsvektor in das Schrägbild eines Körpers einzeichnen.",
     "2021MgrundlegendAAGLAA12-b"),
    ("Abhängigkeit eines Skalarprodukts nur von der Seitenlänge allgemein begründen", "Analytische Geometrie",
     "Skalarprodukt und Winkel",
     "Ohne Koordinaten begründen, dass ein Skalarprodukt aus Ortsvektoren eines Körpers nur von einer "
     "Abmessung abhängt: ausmultiplizieren, Orthogonalität nutzen, Betrag deuten.",
     "2021MgrundlegendAAGLAA12-c"),
    ("Lösungsmenge eines Gleichungssystems mit zwei Variablen als Gerade zeichnen und eine Lösung angeben",
     "Analytische Geometrie", "Lineare Gleichungssysteme",
     "Die unendlich vielen Lösungen eines Gleichungssystems mit zwei Variablen als Gerade darstellen und "
     "eine Lösung zu einem vorgegebenen Wert angeben.",
     "2021MgrundlegendAAGLAA211-a"),
    ("Koeffizienten für ein unlösbares Gleichungssystem angeben und begründen", "Analytische Geometrie",
     "Lineare Gleichungssysteme",
     "Koeffizienten einer Gleichung so wählen, dass das Gleichungssystem keine Lösung hat (gleiche linke "
     "Seite bis auf einen Faktor, andere rechte Seite), und den Widerspruch zeigen.",
     "2021MgrundlegendAAGLAA211-b"),
    ("Bayes-Term im Sachzusammenhang deuten", "Stochastik", "Bedingte Wahrscheinlichkeit und Bayes",
     "Einen Quotienten aus Pfadwahrscheinlichkeiten als bedingte Wahrscheinlichkeit im Sachzusammenhang "
     "deuten (Zähler ein Pfad, Nenner die Summe der Pfade zum Ereignis).",
     "2021MgrundlegendAStochastik11-b"),
    ("Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen", "Stochastik",
     "Binomialverteilung",
     "Für vorgelegte Säulendiagramme begründen, dass sie nicht die Verteilung einer beschriebenen "
     "binomialverteilten Zufallsgröße zeigen (Lage des Maximums, Summe 1, Wertebereich).",
     "2021MgrundlegendAStochastik12-b"),
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


def ohne_feldnamen(v):
    """Feldnamen des Schemas und Kennungen aus dem Text nehmen. Beide sind bewusst
    umlautfrei und stehen in bemerkung als Fachwort, ohne Umschrift zu sein."""
    t = KENNUNG.sub(" ", v).lower()
    for f in sorted(HEAD, key=len, reverse=True):
        t = t.replace(f, " ")
    return t


def umschrift_liste(zeilen):
    """Sichtprüfung, kein Assert: alle Wörter mit ss, ae, oe oder ue."""
    worte = {}
    for z in zeilen:
        for k, v in z.items():
            if k in OHNE_UMLAUT or k.startswith("_"):
                continue
            for w in re.findall(r"[^\W\d_]+", ohne_feldnamen(v), re.UNICODE):
                if any(p in w for p in ("ss", "ae", "oe", "ue")):
                    worte[w] = worte.get(w, 0) + 1
    return sorted(worte.items())


def kennung_aus_id(i):
    """id -> (Kennung, Aufgabennummer innerhalb der Datei, Buchstabe); ohne Suffix
    ist die Aufgabe ungegliedert (Kennung, '', '')."""
    m = re.fullmatch(r"(" + KENNUNG.pattern + r")(?:-(\d*)([a-z]))?", i)
    if not m:
        return None, None, None
    return m.group(1), m.group(2) or "", m.group(3) or ""


def hoechster_afb(v):
    return max(ORD.get(t, 0) for t in v.split("|")) if v else 0


def pruefe_zeile(z, a):
    """Alle Prüfungen, die eine einzelne Zeile aus sich selbst und iqb-quellen.csv bestehen kann."""
    i = z["id"] or "(ohne id)"
    for k in PFLICHT:
        a(z[k].strip() != "", f"{i}: Pflichtfeld leer: {k}")
    kennung, innen, buchst = kennung_aus_id(z["id"])
    a(kennung is not None, f"{i}: id folgt nicht dem Muster Kennung-[Aufgabennummer]Teilaufgabe")
    q = QUELLE.get(kennung)
    a(q is not None, f"{i}: Kennung nicht in {QUELLEN}")
    if q:
        a(not q["dublette_von"], f"{i}: Dublette von {q['dublette_von']}, bekommt keine Zeile")
        a(z["jahr"] == q["jahr"], f"{i}: jahr passt nicht zur Kennung ({q['jahr']})")
        a(z["papier"] == q["papier"], f"{i}: papier passt nicht zur Kennung ({q['papier']})")
        a(z["block"] == q["teil"], f"{i}: block passt nicht zum Prüfungsteil ({q['teil']})")
        a(z["titel"] == q["sachgebiet"], f"{i}: titel muss das Sachgebiet sein ({q['sachgebiet']})")
        if q["teil"] == "A":
            a(z["aufgabe"] == aufgabe_aus(q), f"{i}: aufgabe muss {aufgabe_aus(q)} sein")
            a(innen == "", f"{i}: Teil A hat keine Aufgabennummer innerhalb der Datei")
        else:
            a(innen != "" and z["aufgabe"].endswith(innen),
              f"{i}: Teil B braucht die Aufgabennummer innerhalb der Datei in id und aufgabe")
        a(z["teilaufgabe"] == buchst, f"{i}: teilaufgabe passt nicht zur id")
    a(z["block"] in ("A", "B"), f"{i}: block muss A oder B sein")
    a(z["stern"] == "", f"{i}: stern ist im Profil iqb immer leer")
    a(z["hilfsmittel"] == ("nein" if z["block"] == "A" else "ja"),
      f"{i}: hilfsmittel passt nicht zu block {z['block']}")
    a(re.fullmatch(r"[a-z]?", z["teilaufgabe"]),
      f"{i}: teilaufgabe muss ein Kleinbuchstabe oder leer sein")
    a(re.fullmatch(r"\d{4}|bsp", z["jahr"]), f"{i}: jahr muss vierstellig oder bsp sein")
    a(AFB.fullmatch(z["afb_amtlich"]) is not None, f"{i}: afb_amtlich ungültig: {z['afb_amtlich']}")
    teile = z["afb_amtlich"].split("|")
    a(all(t in ORD for t in teile) and [ORD[t] for t in teile if t in ORD] == sorted(
        {ORD[t] for t in teile if t in ORD}), f"{i}: afb_amtlich nicht aufsteigend ohne Wiederholung")
    a("Standardbezug:" in z["bemerkung"], f"{i}: bemerkung nennt den Standardbezug nicht")
    a("(amtlich)" in z["ergebnis"], f"{i}: ergebnis ohne Zusatz (amtlich)")
    a(re.fullmatch(r"\d+", z["punkte"]) and int(z["punkte"]) > 0, f"{i}: punkte ungültig")
    a(re.fullmatch(r"\d+(\|\d+)?", z["seite"]), f"{i}: seite ungültig (Zahl oder Zahl|Zahl)")
    grenze = int(q["seiten"]) if q and q["seiten"].isdigit() else 99
    for s in z["seite"].split("|"):
        if s.isdigit():
            a(int(s) <= grenze, f"{i}: Seite {s} größer als der Dateiumfang ({grenze})")
    a(re.fullmatch(r"\d+", z["schritte"]), f"{i}: schritte muss eine Zahl sein")
    a(z["leitidee"] in THEMEN, f"{i}: Sachgebiet unbekannt: {z['leitidee']}")
    a(z["thema"] in THEMEN.get(z["leitidee"], []),
      f"{i}: Thema passt nicht zum Sachgebiet: {z['thema']}")
    for feld in ("format", "antwort", "material", "zahlenraum"):
        for teil in [s for s in z[feld].split("|") if s]:
            a(teil in VOK[feld], f"{i}: {feld} hat unbekannten Wert: {teil}")
    for feld in ("textumfang", "niveau_geschaetzt"):
        a(z[feld] in VOK[feld], f"{i}: {feld} ungültig: {z[feld]}")
    for k, v in z.items():
        if k.startswith("_"):
            continue
        a("?" not in v or k == "bemerkung" or z["bemerkung"].strip() != "",
          f"{i}: Fragezeichen in {k} ohne Grund in bemerkung")
        a(not re.search(r"(?<=[\d\s(])-(?=\d)", v),
          f"{i}: ASCII-Bindestrich als Minus in {k}")
        if k not in OHNE_UMLAUT:
            treffer = [w for w in UMSCHRIFT if w in ohne_feldnamen(v)]
            a(not treffer, f"{i}: ASCII-Umschrift in {k}: {treffer}")


def typen_von(z):
    t = set()
    for feld in ("typ", "typ_neben"):
        t |= {s for s in z[feld].split("|") if s}
    return t


ENG = re.compile(r"Schätzung enge Fassung: (I{1,3})")


def geschaetzt_eng(z):
    """Schätzung nach der engen Fassung (iqb.md § 7): steht sie in bemerkung, gilt sie,
    sonst niveau_geschaetzt. Zeilen, die schon nach der engen Fassung erfasst sind,
    tragen keinen Vermerk."""
    m = ENG.search(z["bemerkung"])
    return m.group(1) if m else z["niveau_geschaetzt"]


def eichung(zeilen, eng=False):
    """Trefferquote der Schätzung gegen den höchsten amtlichen Bereich (iqb.md § 4);
    eng=True wertet die enge Fassung aus."""
    treffer, abw = 0, []
    for z in zeilen:
        amt = hoechster_afb(z["afb_amtlich"])
        wert = geschaetzt_eng(z) if eng else z["niveau_geschaetzt"]
        if amt == ORD.get(wert, 0):
            treffer += 1
        else:
            abw.append(f"{z['id']} geschätzt {wert}, amtlich höchstens "
                       f"{[k for k, v in ORD.items() if v == amt][0] if amt else '–'}")
    return treffer, abw


def main():
    fehler, warnung = [], []
    def a(cond, msg):
        if not cond:
            fehler.append(msg)

    _, alt_kat = lade(KAT, HEAD)
    _, alt_typ = lade(TYP, TYP_HEAD)
    alt = [dict(zip(HEAD, r)) for r in alt_kat]
    print(f"Vokabular: {len(HEAD)} Felder, {len(LEITIDEEN)} Sachgebiete, "
          f"{sum(len(v) for v in THEMEN.values())} Themen – gelesen aus {KERN} und {PROFIL}; "
          f"{len(QUELLE)} Kennungen aus {QUELLEN}")

    # ---- Selbstprüfung: kein neuer Stapel, nur die vorhandenen Zeilen prüfen
    if not ZEILEN:
        for z in alt:
            a(len(z) == len(HEAD), f"{z.get('id')}: Feldzahl weicht ab")
            pruefe_zeile(z, a)
        typ_namen = {r[0] for r in alt_typ}
        benutzt = set()
        for z in alt:
            for t in typen_von(z):
                benutzt.add(t)
                a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        a(not (typ_namen - benutzt), f"Typen unbenutzt: {sorted(typ_namen - benutzt)}")
        ids = {z["id"] for z in alt}
        a(len(ids) == len(alt), "doppelte id im Katalog")
        for z in alt:
            for dep in [s for s in z["abhaengig_von"].split("|") if s]:
                a(dep in ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
        for r in alt_typ:
            a(r[1] in THEMEN and r[2] in THEMEN.get(r[1], []),
              f"Typ {r[0]}: Sachgebiet oder Thema unbekannt")
            a(r[4] in ids, f"Typ {r[0]}: beispiel_id nicht im Katalog")
            pruefe_typname(r[0], r[2], a, TYP)
        # Stapelvollständigkeit im Bestand: jeder angefangene Stapel ganz
        # (Dubletten ausgenommen); ungegliederte Aufgaben genau eine Zeile
        kennungen = {kennung_aus_id(z["id"])[0] for z in alt}
        stapel = {QUELLE[k]["stapel"] for k in kennungen if k in QUELLE}
        for s in sorted(stapel):
            fehlt = [k for k, q in QUELLE.items()
                     if q["stapel"] == s and not q["dublette_von"] and k not in kennungen]
            a(not fehlt, f"Stapel {s} im Bestand unvollständig, es fehlen {fehlt}")
        je_datei = {}
        for z in alt:
            je_datei.setdefault(kennung_aus_id(z["id"])[0], []).append(z["teilaufgabe"])
        for k, tl in je_datei.items():
            a("" not in tl or len(tl) == 1, f"{k}: ungegliederte Aufgabe neben gegliederten Zeilen")
        if fehler:
            print(f"\nSelbstprüfung: {len(fehler)} Fehler")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        treffer, abw = eichung(alt)
        treffer_eng, _ = eichung(alt, eng=True)
        print(f"Selbstprüfung bestanden: {len(alt)} Katalogzeilen, {len(alt_typ)} Typen, "
              f"alle Typen verwendet, {len(stapel)} Stapel vollständig. ZEILEN ist leer, nichts geschrieben.")
        if alt:
            print(f"Eichung über den Bestand: {treffer} von {len(alt)} Zeilen treffen den höchsten "
                  f"amtlichen Bereich ({100 * treffer // len(alt)} %), enge Fassung {treffer_eng} "
                  f"({100 * treffer_eng // len(alt)} %).")
            print("Außerhalb der Geltung: " + ", ".join(
                f"{ziel} {sum(1 for z in alt if ziel not in GELTUNG.get(z['thema'], set()))}"
                for ziel in ZIELE) + f" von {len(alt)} Zeilen")
        print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
              "(Häufigkeit in Klammern):")
        liste = umschrift_liste(alt)
        print("  " + ", ".join(f"{w} ({n})" for w, n in liste) if liste else "  keines")
        return

    # ---- Normalfall: neuen Stapel anhängen
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
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog")
        a(len(t[3]) > 20, f"Typ {t[0]}: Definition zu knapp")
        if len(t) == 5:
            pruefe_typname(t[0], t[2], a, "NEUE_TYPEN")
    a(len({t[0] for t in NEUE_TYPEN}) == len(NEUE_TYPEN), "doppelter Typ in NEUE_TYPEN")

    # Stapel: alle Zeilen gehören zum Stapel, jede Datei des Stapels ist da
    stapel = KONFIG["stapel"]
    im_stapel = {k for k, q in QUELLE.items() if q["stapel"] == stapel}
    dubletten = {k for k in im_stapel if QUELLE[k]["dublette_von"]}
    a(im_stapel, f"Stapel {stapel} unbekannt in {QUELLEN}")
    dateien = {z["_kennung"] for z in ZEILEN}
    for k in sorted(dateien - im_stapel):
        a(False, f"{k}: gehört nicht zum Stapel {stapel}")
    je_datei = {}
    for z in ZEILEN:
        je_datei.setdefault(z["_kennung"], []).append(z["teilaufgabe"])
    for k, tl in je_datei.items():
        a("" not in tl or len(tl) == 1, f"{k}: ungegliederte Aufgabe neben gegliederten Zeilen")
    fehlt = sorted(im_stapel - dubletten - dateien)
    if fehlt and not probe:
        a(False, f"Stapel {stapel} unvollständig, es fehlen {len(fehlt)} Dateien: {fehlt}")
    elif fehlt:
        warnung.append(f"Probelauf: {len(fehlt)} von {len(im_stapel - dubletten)} Dateien des Stapels fehlen noch")
    if dubletten:
        warnung.append(f"{len(dubletten)} Dubletten im Stapel ohne Zeile: {sorted(dubletten)}")
    for k in sorted(dateien):
        a(k in KONFIG["soll"], f"{k}: kein Soll in KONFIG")
    for k, soll in KONFIG["soll"].items():
        a(k in im_stapel - dubletten, f"{k}: Soll für eine Datei außerhalb des Stapels oder eine Dublette")
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["_kennung"] == k and z["punkte"].isdigit())
        a(ist == soll, f"{k}: Punkte {ist}, Soll {soll}")

    verwendet = set()
    for z in ZEILEN:
        pruefe_zeile(z, a)
        for t in typen_von(z):
            verwendet.add(t)
            a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        for dep in [s for s in z["abhaengig_von"].split("|") if s]:
            a(dep in neue_ids or dep in alt_ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
    alle_verwendet = set(verwendet)
    for z in alt:
        alle_verwendet |= typen_von(z)
    a(not (typ_namen - alle_verwendet), f"Typen unbenutzt: {sorted(typ_namen - alle_verwendet)}")

    # Qualitätsschranke (iqb.md § 7)
    n = len(ZEILEN)
    unsicher = [z["id"] for z in ZEILEN if any("?" in v for k, v in z.items() if not k.startswith("_"))]
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
    treffer_eng, abw_eng = eichung(ZEILEN, eng=True)
    if n >= SCHWELLEN["eichung_ab_zeilen"]:
        a(treffer_eng / n >= SCHWELLEN["eichung_mindestens"],
          f"Schwelle gerissen: Eichung (enge Fassung) {treffer_eng} von {n} "
          f"({100 * treffer_eng / n:.0f} %), verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %: "
          f"{'; '.join(abw_eng)}")
    # Geltung (iqb.md § 6): Zeilen, deren Thema für eine Zielprüfung nicht gilt
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
    print(f"\nStapel {stapel}{' (Probelauf, nichts geschrieben)' if probe else ''} – "
          f"{len(ZEILEN)} Zeilen aus {len(dateien)} Dateien, {len(NEUE_TYPEN)} Typen neu, "
          f"Katalog {'bliebe' if probe else 'jetzt'} {len(alt_kat) + len(ZEILEN)} Zeilen\n")
    print(f"{'id':<34} {'BE':>2} {'afb':<8} {'thema':<34} {'typ':<46} ergebnis")
    for z in ZEILEN:
        print(f"{z['id']:<34} {z['punkte']:>2} {z['afb_amtlich']:<8} {z['thema'][:34]:<34} "
              f"{z['typ'][:46]:<46} {z['ergebnis'][:40]}")
    print()
    for k in sorted(dateien):
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["_kennung"] == k)
        print(f"{k}: Ist {ist} / Soll {KONFIG['soll'][k]}")
    haupt = {z["typ"] for z in ZEILEN} | {z["typ"] for z in alt}
    neben = set()
    for z in ZEILEN + alt:
        neben |= {s for s in z["typ_neben"].split("|") if s}
    print(f"Typen: {len(haupt | neben)} gesamt, {len(neben - haupt)} nur als typ_neben; "
          f"im Stapel {len(verwendet)} verwendet, davon {len(neu & verwendet)} neu")
    treffer, abw = eichung(ZEILEN)
    print(f"Eichung: {treffer} von {n} Zeilen treffen den höchsten amtlichen Bereich"
          + (f"; Abweichungen: {'; '.join(abw)}" if abw else ""))
    if treffer_eng != treffer:
        print(f"Eichung enge Fassung: {treffer_eng} von {n}")
    print(f"Schwellen: {len(unsicher)} Zeilen mit „?“ (erlaubt {grenze_frage}), "
          f"{len(ersatz)} ohne passendes Thema (erlaubt {grenze_ersatz}), "
          f"Eichung {100 * treffer_eng / n:.0f} % (verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %)")
    # Wiederverwendung im selben Niveau: Typen des Stapels, die schon in einem
    # Stapel desselben Niveaus vorkamen (Konvergenzmessung, iqb-pruefungen.md § 4)
    niveau = QUELLE[next(iter(dateien))]["niveau"]
    im_niveau = set()
    for z in alt:
        k = kennung_aus_id(z["id"])[0]
        if k in QUELLE and QUELLE[k]["niveau"] == niveau:
            im_niveau |= typen_von(z)
    wieder = verwendet & im_niveau
    # Schnitt Thema × Gegenstandsklasse × Handlung (iqb.md § 6): Werte des Stapels,
    # davon schon in einem Stapel desselben Niveaus vorhanden
    def schnitt(z):
        return (z["thema"], klasse_von(z["typ"]), HANDLUNG.get(z["format"].split("|")[0], "?"))
    schnitt_alt = {schnitt(z) for z in alt
                   if kennung_aus_id(z["id"])[0] in QUELLE
                   and QUELLE[kennung_aus_id(z["id"])[0]]["niveau"] == niveau}
    schnitt_neu = {schnitt(z) for z in ZEILEN}
    schnitt_bekannt = sum(1 for z in ZEILEN if schnitt(z) in schnitt_alt)
    # Geltung je Zielprüfung
    geltung_txt = ", ".join(f"{ziel} {len(ids)}" for ziel, ids in ausserhalb.items())
    for ziel, ids in ausserhalb.items():
        if ids:
            print(f"Außerhalb der Geltung {ziel}: {', '.join(ids)}")
    # Kennzahlen je Stapel (iqb.md § 7). Zeile für iqb-pruefungen.md § 4.
    print(f"Kennzahlen: | {stapel} | {n} | {len(verwendet)} | {len(neu & verwendet)} "
          f"({100 * len(neu & verwendet) / len(verwendet):.0f} %) | {treffer} von {n} "
          f"({100 * treffer / n:.0f} %)"
          + (f", eng {treffer_eng} ({100 * treffer_eng / n:.0f} %)" if treffer_eng != treffer else "")
          + f" | {len(unsicher)} | {len(ersatz)} | {len(wieder)} von {len(verwendet)} "
          f"({100 * len(wieder) / len(verwendet):.0f} %) | {geltung_txt} | "
          f"Schnitt {len(schnitt_neu)} Werte, {schnitt_bekannt} von {n} Zeilen bekannt "
          f"({100 * schnitt_bekannt / n:.0f} %) |")
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
          "(Häufigkeit in Klammern):")
    liste = umschrift_liste(ZEILEN)
    print("  " + ", ".join(f"{w} ({n_}" + ")" for w, n_ in liste) if liste else "  keines")
    for w in warnung:
        print("Hinweis:", w)
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
