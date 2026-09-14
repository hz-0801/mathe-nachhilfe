# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.8 · 14.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.8

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

Änderungen gegenüber 0.7 (2024-ga-B): In Teil B darf eine nummerierte Aufgabe
ohne Teilaufgabenbuchstaben stehen (erstmals 2024-ga-B Stochastik WTR 2,
Aufgabe 3): row(kennung, "", innen="3") ergibt id Kennung-3, teilaufgabe leer.
Die Prüfung „ungegliederte Aufgabe neben gegliederten Zeilen" gilt je
Aufgabennummer, nicht je Datei.

Änderungen gegenüber 0.6 (Vorarbeit Teil B, Auftrag des Lehrers): Eichung in
Teil B gegen die Spalte Anforderungsbereich des Standardbezugs („AB amtlich:
III." in bemerkung, Pflicht in Teil B; weicht sie vom höchsten Kompetenzeintrag
ab, muss bemerkung den Hinweis tragen); Teil A unverändert (Maximum).
Trägerbindung: feste Markierung „Traegerbindung: Kontext" am Anfang von
bemerkung, exakter Wortlaut geprüft, kein eigenes Feld, kein Vermerk heißt frei.

Änderungen gegenüber 0.5: Erfassungseinheit in Teil B ist der Stapel je
Rechnerfassung (KONFIG["stapel"] = "2026-ga-B-wtr"), damit der WTR-Zweig ohne
die MMS-Fassung vollständig sein kann (Probestapel 2026-ga-B); Teil A
unverändert. Eine Datei mit nur einer, unnummerierten Aufgabe in Teil B
führt innen="1" (id …-1a, aufgabe 1).

Änderungen gegenüber 0.4: afb_amtlich darf leer sein, wenn die Zeile der
Teilaufgabe im Standardbezug leer ist (erstmals 2019-ga-A AGLAA22 a); dann
muss bemerkung „Standardbezug: keine Eintragung" nennen. Solche Zeilen zählen
in der Eichung weder als Treffer noch als Abweichung; die Nenner nennen die
gewerteten Zeilen.

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
    "stapel": "2023-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2023MgrundlegendBAnalysisWTR1": 35,
        "2023MgrundlegendBAnalysisWTR2": 35,
        "2023MgrundlegendBAGLAA1WTR": 20,
        "2023MgrundlegendBAGLAA2WTR1": 20,
        "2023MgrundlegendBAGLAA2WTR2": 20,
        "2023MgrundlegendBStochastikWTR1": 20,
        "2023MgrundlegendBStochastikWTR2": 20,
        "2023MgrundlegendBStochastikWTR3": 20,
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


def einheit(q):
    """Erfassungseinheit: in Teil A der Stapel, in Teil B der Stapel je Rechnerfassung
    (2026-ga-B-wtr, 2026-ga-B-mms), weil WTR- und MMS-Fassung getrennt erfasst werden (v0.6)."""
    return q["stapel"] if q["teil"] == "A" else f"{q['stapel']}-{q['hilfsmittel'].lower()}"


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
# Stapel 2023-ga-B, WTR-Zweig. innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Pool 2023 grundlegend: Analysis 35 BE, AG/LA und Stochastik 20 BE.

SOLL = {"2023MgrundlegendBAnalysisWTR1": 35, "2023MgrundlegendBAnalysisWTR2": 35,
        "2023MgrundlegendBAGLAA1WTR": 20, "2023MgrundlegendBAGLAA2WTR1": 20, "2023MgrundlegendBAGLAA2WTR2": 20,
        "2023MgrundlegendBStochastikWTR1": 20, "2023MgrundlegendBStochastikWTR2": 20, "2023MgrundlegendBStochastikWTR3": 20}

# ---- Analysis WTR 1, Aufgabe 1: r(x) = −(x² − x − 1), s(x) = e^x
RS = "Koordinatensystem ohne Skalierung; nach unten geöffnete Parabel (r) mit Hochpunkt rechts der y-Achse, gestrichelte e-Kurve (s) von links unten steil nach rechts oben; beide Graphen treffen sich nur im Punkt (0 | 1) auf der y-Achse"
row("2023MgrundlegendBAnalysisWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Nullstellen und Extremstelle einer Parabel berechnen", typ_neben="",
    stichwoerter="x² − x − 1 = 0 lösen|Extremstelle als Mitte der Nullstellen oder über r'",
    voraussetzungen="quadratische Gleichung lösen|Scheitel einer Parabel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=RS, kontext="ohne", textumfang="kurz",
    gegeben="r(x) = −(x² − x − 1) in IR; Graph in Abbildung 1",
    gesucht="Nullstellen und Extremstelle von r",
    verfahren="Quadratische Gleichung lösen, Extremstelle als Mitte der Nullstellen",
    schritte="2", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="",
    ergebnis="x₁ = 1/2 − √(1/4 + 1), x₂ = 1/2 + √(1/4 + 1); Extremstelle 1/2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen beim Auflösen der Klammer",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAnalysisWTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Abstand zwischen Parabel und waagerechter Gerade über den Scheitel beschreiben", typ_neben="",
    stichwoerter="Hochpunkt y-Koordinate 5/4|4 minus y-Koordinate des Hochpunkts",
    voraussetzungen="Hochpunkt einer Parabel|Abstand als Differenz von y-Werten",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=RS, kontext="ohne", textumfang="kurz",
    gegeben="r wie in a; Gerade y = 4",
    gesucht="Vorgehen zur Berechnung des Abstands zwischen Graph von r und Gerade",
    verfahren="y-Koordinate des Hochpunkts bestimmen und von 4 subtrahieren",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2023MgrundlegendBAnalysisWTR1-1a",
    ergebnis="Bestimmt man die y-Koordinate des Hochpunkts des Graphen von r und subtrahiert diese von 4, so erhält man den Abstand (amtlich)",
    zwischenergebnis="r(1/2) = 5/4, Abstand 11/4", niveau_geschaetzt="I",
    fehlerquelle="Abstand an einer beliebigen Stelle statt am Hochpunkt",
    bemerkung="Standardbezug: K1 I, K2 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAnalysisWTR1", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Schnittwinkel eines Graphen mit einer waagerechten Geraden über die Ableitung berechnen", typ_neben="",
    stichwoerter="s(x) = 4 ⇒ x = ln 4|s'(ln 4) = 4|tan φ = 4, φ ≈ 76°",
    voraussetzungen="Exponentialgleichung lösen|Ableitung von e^x|Steigungswinkel über den Tangens",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=RS, kontext="ohne", textumfang="kurz",
    gegeben="s(x) = e^x; Gerade y = 4",
    gesucht="Größe des Schnittwinkels",
    verfahren="Schnittstelle aus s(x) = 4, Steigung s'(x) = 4, Winkel über den Tangens",
    schritte="3", zahlenraum="dezimal", einheiten="°", abhaengig_von="",
    ergebnis="φ ≈ 76° (amtlich)",
    zwischenergebnis="x = ln 4, s'(ln 4) = 4", niveau_geschaetzt="II",
    fehlerquelle="Winkel zwischen Tangente und y-Achse statt zur waagerechten Geraden",
    bemerkung="Standardbezug: K2 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAnalysisWTR1", "d", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Gemeinsame Tangente zweier Graphen im Schnittpunkt nachweisen und angeben", typ_neben="",
    stichwoerter="r'(x) = −2x + 1|r'(0) = 1 = s'(0)|y = x + 1",
    voraussetzungen="Ableitung bilden|Tangentengleichung aus Punkt und Steigung",
    format="Rechnung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Term",
    material="Koordinatensystem", skizze=RS, kontext="ohne", textumfang="kurz",
    gegeben="r(x) = −(x² − x − 1), s(x) = e^x; gemeinsamer Punkt auf der y-Achse",
    gesucht="Nachweis gleicher Steigung im gemeinsamen Punkt; Tangentengleichung",
    verfahren="Beide Ableitungen an der Stelle 0 vergleichen, Tangente durch (0 | 1) mit Steigung 1",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="r'(0) = 1 = s'(0); Tangente y = x + 1 (amtlich)",
    zwischenergebnis="gemeinsamer Punkt (0 | 1)", niveau_geschaetzt="I",
    fehlerquelle="nur gleichen Funktionswert, nicht gleiche Steigung nachweisen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAnalysisWTR1", "e", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen", typ_neben="",
    stichwoerter="Grenzen 0 und 2|Stammfunktion e^x + 1/3x³ − 1/2x² − x|e² − 7/3",
    voraussetzungen="Stammfunktion von e^x und Polynom|Integral mit Grenzen auswerten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=RS, kontext="ohne", textumfang="kurz",
    gegeben="r und s wie oben; Gerade x = 2; Graphen treffen sich nur bei x = 0",
    gesucht="Inhalt des von r, s und x = 2 begrenzten Flächenstücks",
    verfahren="Integral über s − r von 0 bis 2",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="∫₀² (s(x) − r(x)) dx = e² − 7/3 (amtlich)",
    zwischenergebnis="≈ 5,06", niveau_geschaetzt="II",
    fehlerquelle="untere Grenze falsch (nicht am gemeinsamen Punkt)",
    bemerkung="Standardbezug: K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

# ---- Analysis WTR 1, Aufgabe 2: Bewässerungskanal, Durchflussrate w
WK = "Koordinatensystem mit Kästchenraster, x von −1 bis 10 (Sekunden), y von 0 bis 6 (m³/s); Graph von w = w₄: Start bei (0 | 0), steiler Anstieg, Hochpunkt etwa (3 | 5), danach fallend mit Wendepunkt etwa bei (4,3 | 4,7), nähert sich von oben dem Wert 4; Erwartungshorizont: Fläche unter dem Graphen zwischen x = 4 und x = 6 schraffiert, etwa 9 Kästchen"
row("2023MgrundlegendBAnalysisWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integralwert grafisch durch Kästchenzählen bestimmen", typ_neben="",
    stichwoerter="Fläche unter w zwischen 4 und 6|Kästchen 1 m³|etwa 9 m³",
    voraussetzungen="Integral als Fläche unter der Ratenkurve|Kästchen zählen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=WK, kontext="Bewässerungskanal/Durchfluss", textumfang="mittel",
    gegeben="w(x) momentane Durchflussrate in m³/s, x Zeit in s seit Beobachtungsbeginn; Graph in Abbildung 2; Zeitraum 4 s bis 6 s",
    gesucht="Volumen des in diesem Zeitraum vorbeifließenden Wassers",
    verfahren="Fläche unter dem Graphen zwischen 4 und 6 durch Kästchenzählen bestimmen",
    schritte="1", zahlenraum="ganz", einheiten="m³", abhaengig_von="",
    ergebnis="etwa 9 m³ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Funktionswert statt Fläche abgelesen",
    bemerkung="Standardbezug: K3 II, K4 II. AB amtlich: II. Amtlich, eigene Rechnung mit w₄ bestätigt (9,05). Typ wiederverwendet (Teil A).")

row("2023MgrundlegendBAnalysisWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Funktionswert an der Stelle stärkster Abnahme am Graphen ablesen", typ_neben="",
    stichwoerter="Wendepunkt im fallenden Bereich|x-Koordinate größer als 3|y ≈ 4,7",
    voraussetzungen="Wendepunkt als Stelle stärkster Abnahme|Ablesen am Graphen",
    format="Kurzantwort", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=WK, kontext="Bewässerungskanal/Durchfluss", textumfang="kurz",
    gegeben="Graph von w in Abbildung 2; erste elf Sekunden",
    gesucht="momentane Durchflussrate zum Zeitpunkt der stärksten Abnahme",
    verfahren="Wendepunkt im fallenden Bereich am Graphen aufsuchen und y-Koordinate ablesen",
    schritte="1", zahlenraum="dezimal", einheiten="m³/s", abhaengig_von="",
    ergebnis="y-Koordinate des Wendepunkts mit x-Koordinate größer als 3 etwa 4,7, Durchflussrate etwa 4,7 m³/s (amtlich)",
    zwischenergebnis="Wendestelle x ≈ 4,3", niveau_geschaetzt="II",
    fehlerquelle="Wendepunkt im steigenden Bereich oder Tiefpunkt gewählt",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (w₄(4,30) ≈ 4,72).")

row("2023MgrundlegendBAnalysisWTR1", "c", innen="2", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Relative Abweichung zwischen Tangente und Funktion als Ungleichung im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="|t(x) − w(x)| / w(x) < 0,05|relative Abweichung unter 5 %|Tangente als Näherung auf [0,7; 1,4]",
    voraussetzungen="Tangente als lineare Näherung|relative Abweichung",
    format="Begründung", operator="Interpretieren Sie", antwort="Text",
    material="Koordinatensystem", skizze=WK, kontext="Bewässerungskanal/Durchfluss", textumfang="mittel",
    gegeben="Tangente y = t(x) an den Graphen von w im Punkt (1 | w(1)); Aussage: für alle x ∈ [0,7; 1,4] gilt |(t(x) − w(x)) / w(x)| < 0,05",
    gesucht="Bedeutung der Aussage im Sachzusammenhang",
    verfahren="Quotient als relative Abweichung erkennen, Zeitraum und Schranke in Worte fassen",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Für den Zeitraum von 0,7 s bis 1,4 s beschreibt die Tangente die zeitliche Entwicklung der momentanen Durchflussrate mit einer relativen Abweichung von weniger als 5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="absolute statt relative Abweichung",
    bemerkung="Standardbezug: K3 III, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Abweichung 3,1 % und 3,9 % an den Rändern). Eichregel: (d) Quotient als relative Abweichung deuten, verkettet mit Tangente als Näherung.")

# ---- Analysis WTR 1, Aufgabe 3: Schar w_a(x) = 4(x² − x − 1)e^(−x) + a
row("2023MgrundlegendBAnalysisWTR1", "a", innen="3", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Einfluss eines additiven Scharparameters auf den Graphen beschreiben", typ_neben="",
    stichwoerter="Summand a|Verschiebung in y-Richtung",
    voraussetzungen="Verschiebung eines Graphen",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=WK, kontext="ohne", textumfang="kurz",
    gegeben="w_a(x) = 4(x² − x − 1)e^(−x) + a in IR, a ∈ IR; Extremstellen 0 und 3 unabhängig von a; w₄ ist w aus Aufgabe 2",
    gesucht="Einfluss von a auf den Graphen",
    verfahren="a als Summand erkennen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Eine Veränderung des Werts von a bewirkt eine Verschiebung des Graphen von w_a in y-Richtung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Streckung statt Verschiebung",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich.")

row("2023MgrundlegendBAnalysisWTR1", "b", innen="3", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für den Mittelpunkt der Extrempunkte auf der x-Achse bestimmen", typ_neben="",
    stichwoerter="Extrempunkte (0 | a − 4) und (3 | a + 20e⁻³)|Mittelpunkt y-Koordinate 1/2(w_a(0) + w_a(3)) = 0|a = 2 − 10e⁻³",
    voraussetzungen="Funktionswerte mit Parameter|Mittelpunkt einer Strecke|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="w_a wie in a; Extremstellen 0 und 3",
    gesucht="a, für das der Mittelpunkt der Strecke zwischen den Extrempunkten auf der x-Achse liegt",
    verfahren="Bedingung in 1/2(w_a(0) + w_a(3)) = 0 übersetzen und nach a auflösen",
    schritte="3", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="1/2(w_a(0) + w_a(3)) = 1/2(2a − 4 + 20e⁻³); 2a − 4 + 20e⁻³ = 0 ⇔ a = 2 − 10e⁻³ (amtlich)",
    zwischenergebnis="w_a(0) = a − 4, w_a(3) = a + 20e⁻³; a ≈ 1,50", niveau_geschaetzt="III",
    fehlerquelle="Mittelpunkt über die x-Koordinaten statt die y-Koordinaten",
    bemerkung="Standardbezug: K1 II, K2 III, K4 II, K5 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Lagebedingung in eine Gleichung übersetzen.")

row("2023MgrundlegendBAnalysisWTR1", "c", innen="3", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für genau eine Nullstelle über die Lage der Extrempunkte angeben", typ_neben="",
    stichwoerter="w₄(3) = 4 + 20e⁻³|Tiefpunkt (0 | a − 4), Hochpunkt (3 | a + 20e⁻³)|Grenzwert a für x → ∞|genau eine Nullstelle für a < −20e⁻³ und a = 4",
    voraussetzungen="Funktionswert berechnen|Verlauf mit Tief- und Hochpunkt und Grenzwert|Nullstellenzahl über die Lage der Extrempunkte",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Term",
    material="Koordinatensystem", skizze=WK, kontext="ohne", textumfang="kurz",
    gegeben="w_a wie in a; Graph von w₄ in Abbildung 2; Extremstellen 0 (Tiefpunkt) und 3 (Hochpunkt)",
    gesucht="Wert w₄(3); alle a mit genau einer Nullstelle",
    verfahren="w₄(3) berechnen; Graph von w₄ um a − 4 verschieben: genau eine Nullstelle, wenn der Tiefpunkt auf der x-Achse liegt (a = 4) oder der Hochpunkt unterhalb (a + 20e⁻³ < 0)",
    schritte="4", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="w₄(3) = 4 + 20e⁻³; w_a hat für a < −20e⁻³ und für a = 4 genau eine Nullstelle (amtlich)",
    zwischenergebnis="w₄(3) ≈ 5,00; lim w_a = a für x → +∞, lim w_a = +∞ für x → −∞", niveau_geschaetzt="III",
    fehlerquelle="Fall a = 4 (Tiefpunkt auf der x-Achse) übersehen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung III, da Grenzwert, Lage beider Extrempunkte und Verschiebung zu verketten sind; amtlich II.")

# ---- Analysis WTR 2, Aufgabe 1: f(x) = 1/27x³ − 4/3x
row("2023MgrundlegendBAnalysisWTR2", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Symmetrieart am Term über die Exponenten begründen", typ_neben="Stellen mit vorgegebenem Funktionswert durch Ausklammern berechnen",
    stichwoerter="nur ungerade Exponenten ⇒ punktsymmetrisch zum Ursprung|f(x) = 1/27x(x² − 36)|Schnittpunkte (0 | 0), (−6 | 0), (6 | 0)",
    voraussetzungen="Symmetriekriterium ganzrationaler Funktionen|Nullstellen durch Ausklammern",
    format="Begründung|Rechnung", operator="Begründen Sie|Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/27x³ − 4/3x in IR; Wendepunkt (0 | 0)",
    gesucht="Begründung der Symmetrie zum Wendepunkt; Schnittpunkte mit den Achsen",
    verfahren="Exponenten betrachten, x ausklammern",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Der Term ist ganzrational und enthält nur ungerade Exponenten; Schnittpunkte (0 | 0), (−6 | 0) und (6 | 0) (amtlich)",
    zwischenergebnis="f(x) = 1/27x(x² − 36)", niveau_geschaetzt="I",
    fehlerquelle="x² − 36 = 0 nur eine Lösung",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A), Schnittpunkte als typ_neben (Teil A).")

row("2023MgrundlegendBAnalysisWTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen", typ_neben="",
    stichwoerter="f'(x) = 1/9x² − 4/3|f'(√12) = 0|f''(x) = 2/9x, f''(√12) > 0",
    voraussetzungen="Ableitungen bilden|hinreichende Bedingung für Tiefpunkt",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f wie in a; zwei Extrempunkte",
    gesucht="Nachweis eines Tiefpunkts an der Stelle √12",
    verfahren="Erste Ableitung an der Stelle √12 gleich null, zweite Ableitung positiv",
    schritte="3", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="",
    ergebnis="f'(√12) = 1/9 · 12 − 4/3 = 0 und f''(√12) > 0 (amtlich)",
    zwischenergebnis="f''(√12) = 2√12/9 ≈ 0,77", niveau_geschaetzt="I",
    fehlerquelle="(√12)² falsch berechnet",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2023MgrundlegendBAnalysisWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen", typ_neben="",
    stichwoerter="f'(6) = 8/3|f(6) = 0|c = −16",
    voraussetzungen="Ableitungswert|Punkt einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f wie in a; Punkt P(6 | f(6)); Kontrolle t: y = 8/3x − 16",
    gesucht="Gleichung der Tangente t in P",
    verfahren="Steigung aus f'(6), Achsenabschnitt aus f(6) = 0",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="t: y = 8/3x − 16 (amtlich)",
    zwischenergebnis="f'(6) = 8/3, f(6) = 0", niveau_geschaetzt="I",
    fehlerquelle="f(6) ≠ 0 angenommen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2023MgrundlegendBAnalysisWTR2", "d", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen", typ_neben="",
    stichwoerter="Grenzen −12 und 6|f(x) − t(x) = 1/27x³ − 4x + 16|Stammfunktion 1/108x⁴ − 2x² + 16x|324",
    voraussetzungen="Differenzfunktion bilden|Stammfunktion eines Polynoms|Integral auswerten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f und t wie in c; t hat mit dem Graphen neben P nur Q(−12 | f(−12)) gemeinsam",
    gesucht="Inhalt der von Graph und t eingeschlossenen Fläche",
    verfahren="Integral über f − t von −12 bis 6",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2023MgrundlegendBAnalysisWTR2-1c",
    ergebnis="∫₋₁₂⁶ (f(x) − 8/3x + 16) dx = [1/108x⁴ − 2x² + 16x]₋₁₂⁶ = 324 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen bei −t(x)",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2023MgrundlegendBAnalysisWTR2", "e", innen="1", seite="1", punkte="4", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Anzahl verschiedener Ergebnisse bei vertauschter Reihenfolge von Spiegelung und Verschiebungen begründen", typ_neben="",
    stichwoerter="Spiegeln an der x-Achse, Verschieben um 6 in x-Richtung, um 14 in y-Richtung|x-Verschiebung ohne Einfluss|Reihenfolge Spiegelung/y-Verschiebung entscheidet|Wendepunkt (0 | 0) nach (6 | 14) oder (6 | −14)|zwei Graphen",
    voraussetzungen="Wirkung von Spiegelung und Verschiebung|Kommutativität prüfen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Graph von f; drei Schritte: Spiegeln an der x-Achse, Verschieben um 6 in positive x-Richtung, Verschieben um 14 in positive y-Richtung, in allen möglichen Reihenfolgen",
    gesucht="Anzahl der verschiedenen neuen Graphen mit Begründung",
    verfahren="Erkennen, dass nur die Reihenfolge von Spiegelung und y-Verschiebung das Ergebnis ändert; am Wendepunkt nachvollziehen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Zwei verschiedene neue Graphen: Nur die Reihenfolge von Spiegelung und y-Verschiebung ist wesentlich, der Wendepunkt (0 | 0) geht in (6 | 14) oder (6 | −14) über (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="alle sechs Reihenfolgen als verschieden zählen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (c) allgemeiner Nachweis über die Vertauschbarkeit der Schritte.")

# ---- Analysis WTR 2, Aufgabe 2: Tagesdurchschnittstemperatur g, h
TG = "Koordinatensystem mit Kästchenraster, x von 0 bis 12 (Monate), y von 0 bis 16 (°C); Graph von g: Start bei (0 | 14), fällt auf Tiefpunkt etwa (2,5 | 11), Wendepunkt (6 | 14), Hochpunkt etwa (9,5 | 17), fällt bis (12 | 14)"
row("2023MgrundlegendBAnalysisWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendepunkt als Zeitpunkt stärkster Abnahme im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Wendestelle 6|stärkste Zunahme der Tagesdurchschnittstemperatur",
    voraussetzungen="Wendestelle aus dem Graphen oder aus der Symmetrie|Wendepunkt als Stelle stärkster Änderung",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=TG, kontext="Temperatur/Jahresverlauf", textumfang="mittel",
    gegeben="g(x) = −1/27x(x − 6)(x − 12) + 14 für 0 ≤ x < 12, x Zeit in Monaten, g(x) Tagesdurchschnittstemperatur in °C; Graph in der Abbildung; g entsteht aus f durch die drei Schritte",
    gesucht="Wendestelle von g; Bedeutung für den Temperaturverlauf",
    verfahren="Wendestelle als verschobener Wendepunkt (6) angeben und als Zeitpunkt der stärksten Zunahme deuten",
    schritte="2", zahlenraum="ganz", einheiten="Monate", abhaengig_von="",
    ergebnis="Wendestelle 6; die Wendestelle gibt den Zeitpunkt an, zu dem die Tagesdurchschnittstemperatur am stärksten zunimmt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Wendestelle als Zeitpunkt der höchsten Temperatur deuten",
    bemerkung="Standardbezug: K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ga-B), hier stärkste Zunahme statt Abnahme – Vorschlag für den Abgleich: Etikett und Definition auf Zu- und Abnahme erweitern.")

row("2023MgrundlegendBAnalysisWTR2", "b", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Aufgabenstellung zu Extremstellen und Wertedifferenz aus dem Lösungsweg formulieren und erläutern", typ_neben="",
    stichwoerter="g'(x) = 0 ⇔ x = 6 ± √12|g(6 + √12) − g(6 − √12) ≈ 6,2|Differenz höchste minus niedrigste Temperatur",
    voraussetzungen="Extremstellen über die Ableitung|Lösungsweg lesen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Erläutern Sie", antwort="Text",
    material="Koordinatensystem", skizze=TG, kontext="Temperatur/Jahresverlauf", textumfang="mittel",
    gegeben="Rechnungen: g'(x) = 0 ⇔ x = 6 − √12 ∨ x = 6 + √12; g(6 + √12) − g(6 − √12) ≈ 6,2; Abbildung",
    gesucht="passende Aufgabenstellung; Erläuterung des Lösungswegs",
    verfahren="Erste Zeile als Extremstellen, zweite als Differenz der Extremwerte erkennen",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°C", abhaengig_von="",
    ergebnis="Aufgabenstellung: Ermitteln Sie die Differenz zwischen der höchsten und der niedrigsten Tagesdurchschnittstemperatur; in der ersten Zeile werden die Extremstellen von g bestimmt, in der zweiten die Differenz der zugehörigen Funktionswerte (amtlich)",
    zwischenergebnis="Differenz ≈ 6,16", niveau_geschaetzt="II",
    fehlerquelle="Differenz der Extremstellen statt der Funktionswerte",
    bemerkung="Standardbezug: K1 II, K3 I, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAnalysisWTR2", "c", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Wertemenge und Häufigkeit der Werte einer Sinusfunktion auf einer Periode angeben", typ_neben="",
    stichwoerter="h(x) = −3sin(π/6x) + 14|Werte von 11 bis 17|11 und 17 je einmal, alle anderen zweimal|Periode 12",
    voraussetzungen="Amplitude und Verschiebung einer Sinusfunktion|Periode 2π/b|Verlauf über eine Periode",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Temperatur/Jahresverlauf", textumfang="mittel",
    gegeben="h(x) = −3 · sin(π/6 · x) + 14 für 0 ≤ x < 12 als alternatives Modell",
    gesucht="alle angenommenen Temperaturen; wie oft jede angenommen wird",
    verfahren="Wertebereich aus Amplitude 3 um 14, Periode 12 ausnutzen: Extremwerte einmal, alle anderen zweimal",
    schritte="2", zahlenraum="ganz", einheiten="°C", abhaengig_von="",
    ergebnis="Alle Temperaturen von 11 °C bis 17 °C; 11 °C und 17 °C jeweils einmal, alle anderen jeweils zweimal (amtlich)",
    zwischenergebnis="Minimum bei x = 3, Maximum bei x = 9", niveau_geschaetzt="II",
    fehlerquelle="Häufigkeit der Randwerte falsch (Intervall halboffen, x = 0 und x = 12 nicht doppelt)",
    bemerkung="Standardbezug: K1 II, K2 II, K3 I, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAnalysisWTR2", "d", innen="2", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Länge der Monotoniebereiche zweier Modellfunktionen vergleichen und eine Aussage beurteilen", typ_neben="",
    stichwoerter="h steigt von x = 3 bis x = 9, Länge 6|g steigt von 6 − √12 bis 6 + √12, Länge 2√12|2√12 − 6 ≈ 0,93|Aussage richtig",
    voraussetzungen="Extremstellen einer Sinusfunktion aus Spiegelung und Streckung|Extremstellen von g|Differenz vergleichen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=TG, kontext="Temperatur/Jahresverlauf", textumfang="mittel",
    gegeben="g und h wie oben; Aussage: Im Modell mit h ist der Zeitraum steigender Tagesdurchschnittstemperatur etwa einen Monat kürzer als mit g",
    gesucht="Beurteilung der Aussage",
    verfahren="Monotoniebereiche beider Funktionen bestimmen (h: Minimum bei 3, Maximum bei 9; g: Extremstellen 6 ± √12) und Längen vergleichen",
    schritte="4", zahlenraum="Wurzel|dezimal", einheiten="Monate", abhaengig_von="2023MgrundlegendBAnalysisWTR2-2b",
    ergebnis="h nimmt für 0 ≤ x < 12 das Minimum bei x = 3 und das Maximum bei x = 9 an; 2√12 − 6 ≈ 0,93, die Aussage ist richtig (amtlich)",
    zwischenergebnis="Anstiegsdauer h: 6 Monate, g: 2√12 ≈ 6,93 Monate", niveau_geschaetzt="III",
    fehlerquelle="Extremstellen von h ohne Beachtung der Spiegelung",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K4 II, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Monotoniebereiche zweier Modelle bestimmen und die Aussage über die Differenz prüfen.")

# ---- AG/LA A1 WTR: Milchverpackung, Verflechtung Molkerei
VP = "Schrägbild eines Körpers mit Grundfläche ABCD (Quadrat 4,5 × 4,5 in der x₁x₂-Ebene) und schräger Deckfläche EFGH (E und H auf Höhe 13,5, F und G auf Höhe 12); Punkt P auf der Deckfläche; Achsen x₁, x₂, x₃"
row("2023MgrundlegendBAGLAA1WTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Parallelogramm als Rechteck über das Skalarprodukt nachweisen", typ_neben="",
    stichwoerter="EH = FG = (0; 4,5; 0)|EH · EF = 0",
    voraussetzungen="Verbindungsvektoren|Skalarprodukt null bei rechtem Winkel",
    format="Rechnung", operator="Weisen Sie nach", antwort="Term",
    material="Körper", skizze=VP, kontext="Verpackung/Molkerei", textumfang="mittel",
    gegeben="A(0|0|0), B(4,5|0|0), C(4,5|4,5|0), D(0|4,5|0), E(0|0|13,5), F(4,5|0|12), G(4,5|4,5|12), H(0|4,5|13,5); 1 LE = 1 cm; P(1,5|2,25|13) Einstichstelle; Trinkhalm 14 cm",
    gesucht="Nachweis, dass die Deckfläche EFGH rechteckig ist",
    verfahren="Gegenüberliegende Seiten als gleiche Vektoren, Skalarprodukt benachbarter Seiten null",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="EH = (0; 4,5; 0) = FG, EH · EF = (0; 4,5; 0) · (4,5; 0; −1,5) = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur Parallelogramm nachgewiesen, rechter Winkel fehlt",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-B). Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MgrundlegendBAGLAA1WTR", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen eines Prismas mit Trapezquerschnitt im Sachzusammenhang berechnen und mit einer Vorgabe vergleichen", typ_neben="",
    stichwoerter="Trapezfläche 1/2(13,5 + 12) · 4,5|mal Tiefe 4,5|≈ 258 cm³ ≥ 250 ml",
    voraussetzungen="Trapezfläche|Prismenvolumen|1 cm³ = 1 ml",
    format="Rechnung", operator="Prüfen Sie", antwort="Zahl",
    material="Körper", skizze=VP, kontext="Verpackung/Molkerei", textumfang="kurz",
    gegeben="Körper wie in a; Füllmenge 250 ml",
    gesucht="ob die Verpackung 250 ml fasst",
    verfahren="Körper als Prisma mit Trapezquerschnitt auffassen, Volumen berechnen und vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="cm³", abhaengig_von="",
    ergebnis="1/2 · (13,5 cm + 12 cm) · 4,5 cm · 4,5 cm ≈ 258 cm³, die Befüllung ist möglich (amtlich)",
    zwischenergebnis="258,19 cm³", niveau_geschaetzt="I",
    fehlerquelle="Quader mit Höhe 13,5 statt Trapezprisma",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Erreichbarkeit der Grundfläche über den größten Abstand zu einem Punkt beurteilen", typ_neben="",
    stichwoerter="entfernteste Ecken B und C|CP = (−3; 2,25; 13)|√(3² + 2,25² + 13²) ≈ 13,53 < 14",
    voraussetzungen="Abstand zweier Punkte|entfernteste Stelle einer Fläche ist eine Ecke",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Körper", skizze=VP, kontext="Verpackung/Molkerei", textumfang="kurz",
    gegeben="Körper und P wie in a; Trinkhalm 14 cm lang, gerade",
    gesucht="ob jede Stelle der Grundfläche mit dem Trinkhalm erreichbar ist",
    verfahren="Entfernteste Ecken B und C bestimmen, Abstand zu P berechnen und mit 14 vergleichen",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="cm", abhaengig_von="",
    ergebnis="|CP| = |BP| = √(3² + 2,25² + 13²) ≈ 13,53 < 14, beide Ecken und damit jede Stelle lassen sich erreichen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Abstand zur nächsten statt zur entferntesten Ecke",
    bemerkung="Standardbezug: K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

VF = "Verflechtungsdiagramm: Rohstoffe R₁ bis R₄ links, Zwischenprodukte Z₁, Z₂, Z₃ in der Mitte, Getränke M₁, M₂ rechts; Pfeile mit Bedarfen: R₁→Z₁ 0,5, R₁→Z₂ 0,6, R₁→Z₃ 0,5; R₂→Z₁ 0,2, R₂→Z₂ 0,4, R₂→Z₃ 0,2; R₃→Z₁ 0,2; R₄→Z₃ 0,3, R₄→Z₁ 0,1; Z₁→M₁ 0,8; Z₂→M₁ 0,1, Z₂→M₂ 0,3; Z₃→M₁ 0,1, Z₃→M₂ 0,7"
row("2023MgrundlegendBAGLAA1WTR", "a", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Eintrag der Gesamtmatrix aus dem Diagramm bestätigen und Nulleintrag begründen", typ_neben="",
    stichwoerter="x = 0,4 · 0,3 + 0,2 · 0,7 = 0,26|y: R₃ nur für Z₁, Z₁ nicht für M₂|y = 0",
    voraussetzungen="Zweistufigen Bedarf über Pfade summieren|Matrix als Gesamtbedarf lesen",
    format="Rechnung|Begründung", operator="Bestätigen Sie|Begründen Sie", antwort="Zahl",
    material="Diagramm", skizze=VF, kontext="Verpackung/Molkerei", textumfang="mittel",
    gegeben="Diagramm Rohstoffe R₁–R₄ → Zwischenprodukte Z₁–Z₃ → Getränke M₁, M₂; Gesamtmatrix K = ((0,51; 0,53), (0,22; x), (0,16; y), (0,11; 0,21)) Rohstoffe je Getränk",
    gesucht="Bestätigung x = 0,26; Begründung y = 0",
    verfahren="Bedarf von R₂ für M₂ über Z₂ und Z₃ summieren; für y die Pfade von R₃ nach M₂ betrachten",
    schritte="3", zahlenraum="dezimal", einheiten="ME", abhaengig_von="",
    ergebnis="x = 0,4 · 0,3 + 0,2 · 0,7 = 0,26; y gibt die Mengeneinheiten von R₃ je Mengeneinheit M₂ an; M₂ braucht nur Z₂ und Z₃, die ohne R₃ hergestellt werden, also y = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Pfad R₂ → Z₁ → M₂ mitgezählt, obwohl Z₁ nicht in M₂ eingeht",
    bemerkung="Standardbezug: K1 II, K2 I, K3 II, K4 I, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MgrundlegendBAGLAA1WTR", "b", innen="2", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Höchstmenge aus einer Kostenschranke bei festem Mengenverhältnis ermitteln", typ_neben="",
    stichwoerter="Produktionsvektor (3m₂; m₂)|Rohstoffvektor K · (3m₂; m₂) = (2,06m₂; 0,92m₂; 0,48m₂; 0,54m₂)|Kosten (0,1; 0,1; 0,5; 0,3) · Rohstoffvektor = 0,7m₂|0,7m₂ ≤ 3500 ⇒ m₂ = 5000, m₁ = 15000",
    voraussetzungen="Matrix mal Vektor|Kostenvektor als Skalarprodukt|Ungleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle Rohstoff R₁ R₂ R₃ R₄, Kosten 0,1 GE 0,1 GE 0,5 GE 0,3 GE; dazu Diagramm wie in a", kontext="Verpackung/Molkerei", textumfang="mittel",
    gegeben="K wie in a mit x = 0,26, y = 0; Kosten je ME Rohstoff 0,1; 0,1; 0,5; 0,3 GE; dreimal so viele ME von M₁ wie von M₂; Gesamtkosten höchstens 3500 GE",
    gesucht="Höchstmengen von M₁ und M₂",
    verfahren="Produktionsvektor mit einer Unbekannten ansetzen, Rohstoffbedarf und Kosten als Term in m₂, Schranke auflösen",
    schritte="4", zahlenraum="dezimal|ganz", einheiten="ME|GE", abhaengig_von="",
    ergebnis="0,7m₂ = 3500 ⇔ m₂ = 5000, d. h. m₁ = 15000 (amtlich)",
    zwischenergebnis="Rohstoffvektor (2,06m₂; 0,92m₂; 0,48m₂; 0,54m₂)", niveau_geschaetzt="III",
    fehlerquelle="Verhältnis 3 : 1 umgekehrt angesetzt",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II, K6 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Mengenverhältnis und Kostenschranke in einen Ansatz mit einer Unbekannten übersetzen. Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MgrundlegendBAGLAA1WTR", "c", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Format der Bedarfsmatrix aus der Anzahl der Stufenprodukte begründen", typ_neben="",
    stichwoerter="L hat vier Spalten ⇒ vier Zwischenprodukte|N: vier Zeilen, zwei Spalten",
    voraussetzungen="Zeilen und Spalten einer Bedarfsmatrix zuordnen|Verkettung L · N",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Verpackung/Molkerei", textumfang="mittel",
    gegeben="Veränderter Prozess; Matrix L (Rohstoffe je Zwischenprodukt) hat vier Zeilen und vier Spalten; weiterhin zwei Getränke",
    gesucht="Zeilen- und Spaltenzahl der Matrix N (Zwischenprodukte je Getränk) mit Begründung",
    verfahren="Spaltenzahl von L als Zahl der Zwischenprodukte lesen, Getränkezahl als Spaltenzahl von N",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="N hat vier Zeilen (ein Zwischenprodukt kam hinzu, da L vier Spalten hat) und zwei Spalten (weiterhin zwei Getränke) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Zeilen und Spalten vertauscht",
    bemerkung="Standardbezug: K1 I, K3 II, K6 I. AB amtlich: II. Amtlich. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA A2 WTR 1: Anbau mit Glasdach (Prisma ABCDEFGH)
AN = "Schrägbild eines Prismas: Grundfläche ABCD in der x₁x₂-Ebene (A(0|0|0), B(5|0|0), C(5|4|0), D(0|4|0)), E(0|0|4), F(5|0|4) über A und B, G(5|3|3), H(0|3|3); Wand ABFE dunkel, Glasdach EFGH schräg abfallend nach hinten; Achsen x₁, x₂, x₃"
row("2023MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Drachenviereck über zwei Paare gleich langer Seiten nachweisen", typ_neben="",
    stichwoerter="|BC| = 4 = |BF||GC| = √(1² + 3²) = |GF|",
    voraussetzungen="Streckenlänge aus Koordinaten|Kennzeichen des Drachenvierecks",
    format="Rechnung", operator="Begründen Sie", antwort="Term",
    material="Körper", skizze=AN, kontext="Gebäude/Anbau", textumfang="mittel",
    gegeben="A(0|0|0), B(5|0|0), C(5|4|0), D(0|4|0), E(0|0|4), F(5|0|4), G(5|3|3), H(0|3|3); EFGH Glasdach, ABFE geschlossene Wand; 1 LE = 1 m; x₁x₂-Ebene Untergrund",
    gesucht="Nachweis, dass BCGF ein Drachenviereck ist",
    verfahren="Zwei Paare benachbarter gleich langer Seiten nachrechnen",
    schritte="2", zahlenraum="ganz|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="|BC| = 4 = |BF|, |GC| = √(1² + 3²) = |GF| (amtlich)",
    zwischenergebnis="√10 ≈ 3,16", niveau_geschaetzt="I",
    fehlerquelle="gegenüberliegende statt benachbarte Seiten verglichen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen", typ_neben="",
    stichwoerter="G(5|3|3) einsetzen: 3r + 3s = 0|r = 1, s = −1",
    voraussetzungen="Punktprobe|Gleichung mit zwei Unbekannten frei wählen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=AN, kontext="Gebäude/Anbau", textumfang="kurz",
    gegeben="Ebene L durch A, B, G mit Gleichung r · x₂ + s · x₃ = 0",
    gesucht="passende Werte für r und s",
    verfahren="G in die Gleichung einsetzen, ein Wert frei wählen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Da G in der Ebene liegt, gilt 3r + 3s = 0, beispielsweise r = 1 und s = −1 (amtlich)",
    zwischenergebnis="A und B erfüllen die Gleichung für alle r, s", niveau_geschaetzt="II",
    fehlerquelle="r = s = 0 als Lösung",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2023MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebene eines geraden Prismas über die Symmetrieachse der Grundfläche begründen", typ_neben="",
    stichwoerter="Prisma mit Grundfläche BCGF ist gerade|L enthält die Symmetrieachse BG des Drachens|L senkrecht zur Grundfläche",
    voraussetzungen="Symmetrieachse eines Drachenvierecks|gerades Prisma|Ebene senkrecht zur Grundfläche",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=AN, kontext="Gebäude/Anbau", textumfang="kurz",
    gegeben="Körper ABCDEFGH; Ebene L: x₂ − x₃ = 0 durch A, B, G",
    gesucht="Begründung, dass L Symmetrieebene des Körpers ist",
    verfahren="Körper als gerades Prisma über dem Drachen BCGF auffassen, L enthält die Symmetrieachse der Grundfläche und steht senkrecht auf ihr",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2023MgrundlegendBAGLAA2WTR1-1b",
    ergebnis="Das Prisma ABCDEFGH mit dem Drachenviereck BCGF als Grundfläche ist gerade; L enthält die Symmetrieachse der Grundfläche und steht zu dieser senkrecht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur einzelne Punktepaare gespiegelt, keine allgemeine Begründung",
    bemerkung="Standardbezug: K1 II, K4 I, K6 I. AB amtlich: II. Amtlich. Kein Rückgriff auf „Symmetrieebenen eines Körpers aus den Koordinaten begründen“ (anderer Lösungsweg: Prisma und Symmetrieachse statt Koordinatenvergleich).")

row("2023MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumenrechnung eines Prismas aus einem Lösungsweg erläutern", typ_neben="",
    stichwoerter="I: 2 · 1/2 · 4 · 3 · 5 = 60|Höhe 5 (Länge AB)|Grundfläche BCGF doppeltes Dreieck BCG|II: 3 · 5 · 4 = 60 als Quader-Ansatz",
    voraussetzungen="Prismenvolumen Grundfläche mal Höhe|Drachenfläche aus zwei Dreiecken",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=AN, kontext="Gebäude/Anbau", textumfang="kurz",
    gegeben="Rechnungen I: 2 · 1/2 · 4 · 3 · 5 = 60 und II: 3 · 5 · 4 = 60 für das Volumen des Anbaus",
    gesucht="Gedankengang einer der beiden Rechnungen",
    verfahren="Faktoren der Rechnung geometrisch deuten",
    schritte="1", zahlenraum="ganz", einheiten="m³", abhaengig_von="",
    ergebnis="I: Das Prisma hat die Höhe 5; der Inhalt der Grundfläche BCGF ist doppelt so groß wie der Inhalt 1/2 · 4 · 3 des Dreiecks BCG (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Höhe des Prismas mit Gebäudehöhe 4 verwechselt",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Geschwindigkeit entlang einer Kante aus Kantenlänge und Zeit berechnen", typ_neben="",
    stichwoerter="|FG| = √10 m|eine Minute = 60 s|√10 · 100 cm / 60 s ≈ 5,3 cm/s",
    voraussetzungen="Streckenlänge|Einheiten m → cm, min → s|Geschwindigkeit als Weg durch Zeit",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=AN, kontext="Gebäude/Anbau", textumfang="mittel",
    gegeben="Rollo läuft in einer Minute von der Dachkante EF bis zur unteren Dachkante HG",
    gesucht="mittlere Geschwindigkeit in cm/s",
    verfahren="Länge der Dachstrecke FG berechnen, in cm umrechnen, durch 60 s teilen",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="cm/s", abhaengig_von="",
    ergebnis="|FG| · 100 cm / 60 s ≈ 5,3 cm/s (amtlich)",
    zwischenergebnis="|FG| = √10 ≈ 3,16 m", niveau_geschaetzt="I",
    fehlerquelle="Höhendifferenz 1 m statt Dachlänge",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAGLAA2WTR1", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen", typ_neben="",
    stichwoerter="Richtungsvektor (1; −1; −2)|Normalenvektor des Untergrunds (0; 0; 1)|sin φ = 2/√6|φ ≈ 55°",
    voraussetzungen="Winkelformel Gerade–Ebene mit Sinus|Betrag eines Vektors",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Gebäude/Anbau", textumfang="kurz",
    gegeben="Sonnenlicht als parallele Geraden mit Richtungsvektor (1; −1; −2); Untergrund x₁x₂-Ebene",
    gesucht="Winkel, unter dem das Licht auf den Untergrund trifft",
    verfahren="Sinus des Winkels aus Skalarprodukt von Richtungs- und Normalenvektor durch die Beträge",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="sin φ = |(1; −1; −2) · (0; 0; 1)| / (|(1; −1; −2)| · |(0; 0; 1)|) liefert φ ≈ 55° (amtlich)",
    zwischenergebnis="sin φ = 2/√6", niveau_geschaetzt="II",
    fehlerquelle="Kosinus statt Sinus (Winkel zur Normalen)",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAGLAA2WTR1", "g", innen="1", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Spurpunkt einer Lichtgeraden als Schatten auf der Wand aus einem Lösungsweg erläutern", typ_neben="",
    stichwoerter="Gerade durch H(0|3|3) mit Richtung (1; −1; −2)|Schnitt mit x₁x₃-Ebene bei μ = 3: S(3|0|−3)|Schatten der unteren Rollokante HG auf der Wandebene|Zeichnung Wand ABFE mit Schattenlinie von F nach S",
    voraussetzungen="Gerade durch Punkt mit Richtungsvektor|Spurpunkt mit Koordinatenebene|zweidimensionale Zeichnung in der x₁x₃-Ebene",
    format="Begründung|Zeichnen", operator="Beschreiben Sie|Fertigen Sie an", antwort="Grafik",
    material="Körper", skizze=AN + "; Erwartungshorizont: Zeichnung in der x₁x₃-Ebene mit Rechteck ABFE (Wand), S(3|−3) unterhalb der x₁-Achse, Schattenbereich im Wandrechteck zwischen der Geraden von G nach S (Spur des Lichts) und der Kante FE schraffiert", kontext="Gebäude/Anbau", textumfang="lang",
    gegeben="Rechnung (x₁; 0; x₃) = (0; 3; 3) + μ · (1; −1; −2) liefert μ = 3 und (3|0|−3); geschlossene Wand ABFE; vollständig herabgelassenes Rollo (Unterkante HG)",
    gesucht="Bedeutung des Lösungsschritts; Zeichnung von Wand und Schatten in der x₁x₃-Ebene",
    verfahren="Punkt als Spurpunkt der Lichtgeraden durch H in der Wandebene erkennen; Wand als Rechteck 5 × 4 zeichnen, Schattenkante durch die Spur des Lichts von G aus, Bereich schraffieren",
    schritte="3", zahlenraum="ganz|negativ", einheiten="m", abhaengig_von="",
    ergebnis="(3|0|−3) ist der Schnittpunkt S der Geraden durch H mit dem gegebenen Richtungsvektor und der x₁x₃-Ebene; Zeichnung: Rechteck ABFE mit S unterhalb, Schattenfläche zwischen der Verbindung G–S und der oberen Wandkante schraffiert (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Schatten des Rollos an der Unterkante HG statt an der Oberkante EF beginnen lassen; S liegt außerhalb der Wand",
    bemerkung="Traegerbindung: Kontext (Wand, Rollo und Lichtrichtung nur aus der Trägeraufgabe). Standardbezug: K1 II, K2 III, K3 II, K4 II, K5 II, K6 I. AB amtlich: III. Amtlich. Eichregel: (d) Spurpunkt deuten, verkettet mit der Übertragung in die ebene Zeichnung. Typ wiederverwendet (2025-ga-B).")

# ---- AG/LA A2 WTR 2: Körper ABCDEF, Pyramide mit Spitze S
PY = "Schrägbild: Dreieck ABC in der x₁x₂-Ebene (A(10|0|0) vorn, B(0|7,5|0) rechts, C(0|−7,5|0) links), Deckdreieck DEF mit D(8|0|1), E(0|3|3), F(0|−3|3); Kanten AD, BE, CF verlängert treffen sich in der Spitze S auf der x₃-Achse; Achsen x₁, x₂, x₃"
row("2023MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Gleichschenkligkeit über Seitenlängen nachweisen und Parallelität einer Kante zur Grundfläche begründen", typ_neben="",
    stichwoerter="AB = (−10; 7,5; 0), AC = (−10; −7,5; 0), |AB| = |AC||Grundfläche in der x₁x₂-Ebene, E und F gleiche x₃-Koordinate",
    voraussetzungen="Streckenlängen aus Koordinaten|Parallelität zu einer Koordinatenebene über gleiche Koordinate",
    format="Rechnung|Begründung", operator="Zeigen Sie|Begründen Sie", antwort="Term",
    material="Körper", skizze=PY, kontext="ohne", textumfang="mittel",
    gegeben="A(10|0|0), B(0|7,5|0), C(0|−7,5|0), D(8|0|1), E(0|3|3), F(0|−3|3); Grundfläche ABC, Deckfläche DEF in Ebene L",
    gesucht="Nachweis der Gleichschenkligkeit von ABC; Begründung EF parallel zur Grundfläche",
    verfahren="Schenkellängen vergleichen; gleiche x₃-Koordinate von E und F",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="AB = (−10; 7,5; 0), AC = (−10; −7,5; 0), also |AB| = |AC|; die Grundfläche liegt in der x₁x₂-Ebene, E und F haben die gleiche x₃-Koordinate (amtlich)",
    zwischenergebnis="|AB| = 12,5", niveau_geschaetzt="I",
    fehlerquelle="Basis BC als Schenkel behandelt",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="Parameterform mit F, FD = (8; 3; −2), FE = (0; 6; 0)|Parameter eliminieren: x₁ = 8r, x₃ = 3 − 2r|x₁ + 4x₃ = 12",
    voraussetzungen="Parameterform aus drei Punkten|Parameter eliminieren oder Normalenvektor",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=PY, kontext="ohne", textumfang="kurz",
    gegeben="D, E, F wie in a; Kontrolle x₁ + 4x₃ = 12",
    gesucht="Koordinatengleichung von L",
    verfahren="Parametergleichung aufstellen und die Parameter über die Koordinatengleichungen eliminieren",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="x = (0; −3; 3) + r(8; 3; −2) + s(0; 6; 0) liefert x₁ = 8r, x₃ = 3 − 2r, also 4x₃ = 12 − 8r und x₁ + 4x₃ = 12 (amtlich)",
    zwischenergebnis="Normalenvektor (1; 0; 4)", niveau_geschaetzt="II",
    fehlerquelle="x₂-Gleichung mitschleppen, obwohl sie nicht gebraucht wird",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Lauf 7).")

row("2023MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen", typ_neben="",
    stichwoerter="Richtung der x₃-Achse (0; 0; 1)|Normalenvektor (1; 0; 4)|sin φ = 4/√17|φ ≈ 76°",
    voraussetzungen="Winkelformel Gerade–Ebene mit Sinus|Normalenvektor aus der Koordinatengleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="L: x₁ + 4x₃ = 12; x₃-Achse",
    gesucht="Schnittwinkel der x₃-Achse mit L",
    verfahren="Sinus des Winkels aus Skalarprodukt von Achsenrichtung und Normalenvektor durch die Beträge",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2023MgrundlegendBAGLAA2WTR2-1b",
    ergebnis="sin φ = |(0; 0; 1) · (1; 0; 4)| / |(1; 0; 4)| = 4/√(1² + 4²) liefert φ ≈ 76° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Kosinus statt Sinus",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2023-ga-B, Teilaufgabe f der Aufgabe AGLAA2WTR1).")

row("2023MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen", typ_neben="",
    stichwoerter="S auf der x₃-Achse (Symmetrie)|Gerade AD: (10; 0; 0) + t(−2; 0; 1)|t = 5 ⇒ S(0|0|5)",
    voraussetzungen="Gerade durch zwei Punkte|Schnitt mit einer Koordinatenachse",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=PY, kontext="ohne", textumfang="mittel",
    gegeben="Körper ABCDEF ergänzt zur Pyramide mit Grundfläche ABC und Spitze S; D, E, F auf den Kanten; Kontrolle S(0|0|5)",
    gesucht="Koordinaten von S",
    verfahren="S liegt auf der x₃-Achse; Gerade durch A und D mit der x₃-Achse schneiden",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="S liegt auf der x₃-Achse; (10; 0; 0) + t · (−2; 0; 1) = (0; 0; x₃) liefert t = 5 und x₃ = 5, S(0|0|5) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Richtungsvektor AD statt DA mit falschem Vorzeichen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAGLAA2WTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Abstand eines Punktes zu einer Ebene über eine Schrägstrecke nach oben abschätzen", typ_neben="",
    stichwoerter="M(0|0|3) Mittelpunkt von EF|SM = 2 senkrecht zur x₁x₂-Ebene, aber nicht zu L|Abstand S–L kleiner als |SM| = 2|Skizze: Lot von S auf DM einzeichnen",
    voraussetzungen="Abstand als kürzeste Verbindung|Mittelpunkt einer Strecke|Skizze in der x₁x₃-Ebene",
    format="Begründung|Zeichnen", operator="Begründen Sie|Veranschaulichen Sie", antwort="Text",
    material="Skizze", skizze="Abbildung 2 in der x₁x₃-Ebene: Punkte D (links unten), M (rechts, unter S) und S (oben) ohne Achsen; Erwartungshorizont: Strecke DM (Spur von L), Senkrechte SM und Lot von S auf DM mit rechtem Winkel", kontext="ohne", textumfang="mittel",
    gegeben="S(0|0|5) Spitze der Pyramide mit Grundfläche DEF; M Mittelpunkt von EF; Abbildung 2 mit D, M, S in der x₁x₃-Ebene",
    gesucht="Begründung Abstand S–L < 2; Eintragung in Abbildung 2",
    verfahren="Abstand zu L als Lotlänge kleiner als die schräge Strecke SM = 2; Lot in die Abbildung eintragen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2023MgrundlegendBAGLAA2WTR2-1d",
    ergebnis="Der Abstand von S zu L ist kleiner als der Abstand von S zu M, und der Abstand von S zu M ist 2; Zeichnung mit Lot von S auf die Spur DM (amtlich)",
    zwischenergebnis="exakter Abstand 8/√17 ≈ 1,94", niveau_geschaetzt="II",
    fehlerquelle="SM als Abstand zur Ebene angesehen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBAGLAA2WTR2", "f", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumenverlauf eines Restkörpers in Abhängigkeit vom Parameter als linear begründen und Graphen zuordnen", typ_neben="",
    stichwoerter="D_t(8 − 8t|0|1 + 4t) auf DS|V = V(ABCS) − 1/3 · A_EFS · (8 − 8t)|Abstand von D_t zur Ebene EFS proportional zu 8 − 8t|linear wachsend ⇒ Graph II",
    voraussetzungen="Pyramidenvolumen|Volumen als Differenz|linearer Term erkennen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm", skizze="Abbildung 3: Koordinatensystem t von 0 bis 1, Volumen nach oben; Graph I gekrümmt (konkav) von einem Startwert steigend, Graph II gestrichelt und geradlinig steigend, beide mit gleichem Anfangs- und Endpunkt", kontext="ohne", textumfang="mittel",
    gegeben="Punkte D_t(8 − 8t|0|1 + 4t) auf DS für t ∈ [0; 1]; Abbildung 3 mit Graphen I (gekrümmt) und II (gerade); einer zeigt das Volumen von ABCD_tEF",
    gesucht="passender Graph mit Begründung",
    verfahren="Volumen als konstante Pyramide ABCS minus Pyramide EFSD_t, deren Höhe linear in t ist",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2023MgrundlegendBAGLAA2WTR2-1d",
    ergebnis="Graph II; das Volumen ergibt sich aus dem konstanten Volumen der Pyramide ABCS minus dem Volumen der Pyramide EFSD_t = 1/3 · A_EFS · (8 − 8t), es nimmt mit t linear zu (amtlich)",
    zwischenergebnis="V(ABCS) = 125", niveau_geschaetzt="III",
    fehlerquelle="Volumen des Restkörpers direkt statt als Differenz ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis der Linearität über den Volumenterm.")

# ---- Stochastik WTR 1: Röstkaffee, Prüfplan, Mängel
row("2023MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl geordneter Auswahlen ohne Wiederholung berechnen", typ_neben="",
    stichwoerter="5 · 4 · 3 = 60|Reihenfolge festgelegt, ohne Wiederholung",
    voraussetzungen="Produktregel|Auswahl mit Reihenfolge",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kaffee/Messe", textumfang="kurz",
    gegeben="fünf Röstgrade; jeder Besucher probiert drei verschiedene und legt die Reihenfolge fest",
    gesucht="Anzahl der Möglichkeiten",
    verfahren="Produkt 5 · 4 · 3",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="5 · 4 · 3 = 60 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Binomialkoeffizient ohne Reihenfolge (10)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Hypergeometrische Verteilung",
    typ="Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen", typ_neben="",
    stichwoerter="200 Packungen, 10 mit Gutschein, 180 verschenkt|alle 10 Gutscheine dabei ⇔ 170 der 190 ohne Gutschein|C(190; 170) / C(200; 180) ≈ 34 %",
    voraussetzungen="Ziehen ohne Zurücklegen|Binomialkoeffizient|günstige durch mögliche",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kaffee/Messe", textumfang="mittel",
    gegeben="200 Probepackungen, 10 davon mit Gutschein; 180 zufällig ausgewählte werden verschenkt",
    gesucht="Wahrscheinlichkeit, dass alle Gutscheinpackungen verschenkt werden",
    verfahren="Anzahl günstiger Auswahlen (alle 10 Gutscheine und 170 der 190 anderen) durch Anzahl aller Auswahlen",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="C(190; 170) / C(200; 180) ≈ 34 % (amtlich)",
    zwischenergebnis="≈ 0,340", niveau_geschaetzt="II",
    fehlerquelle="Binomialverteilung mit p = 0,05 statt Ziehen ohne Zurücklegen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Modell ohne Zurücklegen selbst erkennen und günstige Fälle zählen), amtlich I. Typ wiederverwendet (2024-ea-B).")

row("2023MgrundlegendBStochastikWTR1", "a", innen="2", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit eines zweistufigen Prüfplans über Binomialwahrscheinlichkeiten berechnen", typ_neben="",
    stichwoerter="X Anzahl einwandfreier Säcke, n = 50, p = 0,96|P(X ≥ 48) direkt|P(X = 47) · P(Y ≥ 24) mit n = 25|≈ 81 %",
    voraussetzungen="Kumulierte Binomialwahrscheinlichkeit am Rechner|Pfadregeln für den zweiten Schritt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kaffee/Qualitätsprüfung", textumfang="lang",
    gegeben="96 % der Säcke einwandfrei; Schritt 1: 50 Säcke, höchstens zwei mangelhaft ⇒ Vertrag; genau drei mangelhaft ⇒ Schritt 2: 25 Säcke, höchstens ein mangelhaft ⇒ Vertrag; sonst kein Vertrag",
    gesucht="Wahrscheinlichkeit für den Vertragsabschluss",
    verfahren="Direkter Abschluss plus Pfad über genau drei Mängel und zweiten Schritt, beide binomial",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="X: Anzahl der Säcke, die den Qualitätsanforderungen entsprechen; P₀,₉₆⁵⁰(X ≥ 48) + P₀,₉₆⁵⁰(X = 47) · P₀,₉₆²⁵(X ≥ 24) ≈ 81 % (amtlich)",
    zwischenergebnis="≈ 0,812", niveau_geschaetzt="II",
    fehlerquelle="zweiten Schritt ohne Faktor P(X = 47) addieren",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR1", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wirkung eines kleineren Stichprobenumfangs auf eine Annahmewahrscheinlichkeit ohne Rechnung beurteilen", typ_neben="",
    stichwoerter="höchstens ein mangelhafter Sack bei 15 wahrscheinlicher als bei 25|kleinere Stichprobe für den Großhändler vorteilhaft",
    voraussetzungen="Monotonie von P(höchstens k) im Stichprobenumfang",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Kaffee/Qualitätsprüfung", textumfang="kurz",
    gegeben="zweiter Schritt mit 15 statt 25 Säcken, sonst gleiche Bedingungen",
    gesucht="ob das für den Großhändler von Vorteil sein könnte, ohne Rechnung",
    verfahren="Wahrscheinlichkeit für höchstens einen Mangel wächst bei kleinerer Stichprobe",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Wahrscheinlichkeit, dass höchstens ein Sack nicht den Anforderungen entspricht und der Vertrag zustande kommt, ist bei 15 Säcken größer als bei 25; die kleinere Anzahl könnte für den Großhändler vorteilhaft sein (amtlich)",
    zwischenergebnis="Kontrolle: P(≤ 1 Mangel) 0,88 bei 15 gegenüber 0,74 bei 25", niveau_geschaetzt="II",
    fehlerquelle="größere Stichprobe pauschal als besser ansehen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR1", "c", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Schnittwahrscheinlichkeit zweier Ereignisse im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="M₁ ∩ ¬M₂|zu viele Verunreinigungen und mindestens 60 kg",
    voraussetzungen="Schnitt und Gegenereignis lesen",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Kaffee/Qualitätsprüfung", textumfang="mittel",
    gegeben="M₁: zu viele Verunreinigungen; M₂: weniger als 60 kg; Mängel unabhängig; P(M₁) = 1 %",
    gesucht="Ereignis M₁ ∩ ¬M₂ in Worten",
    verfahren="Schnitt mit Gegenereignis in den Sachzusammenhang übersetzen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Der Sack enthält mindestens 60 kg Kaffee, der Kaffee weist aber zu viele Verunreinigungen auf (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Gegenereignis als „genau 60 kg“",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A).")

row("2023MgrundlegendBStochastikWTR1", "d", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Wahrscheinlichkeit eines Schnitts aus einem Randanteil und dem Anteil ohne beide Mängel nachweisen", typ_neben="",
    stichwoerter="P(¬M₁) = 99 %|P(¬M₁ ∩ ¬M₂) = 96 % (Sack einwandfrei)|P(¬M₁ ∩ M₂) = 99 % − 96 % = 3 %",
    voraussetzungen="Einwandfrei heißt keiner der Mängel|Zerlegung P(A) = P(A ∩ B) + P(A ∩ ¬B)",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kaffee/Qualitätsprüfung", textumfang="mittel",
    gegeben="96 % der Säcke ohne Mangel; P(M₁) = 1 %; jeder mangelhafte Sack hat M₁ oder M₂",
    gesucht="Nachweis P(¬M₁ ∩ M₂) = 3 %",
    verfahren="Anteil ohne Verunreinigung minus Anteil ohne beide Mängel",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(¬M₁ ∩ M₂) = P(¬M₁) − P(¬M₁ ∩ ¬M₂) = 99 % − 96 % = 3 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="96 % als P(¬M₂) statt als P(¬M₁ ∩ ¬M₂) lesen",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR1", "e", innen="2", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen", typ_neben="",
    stichwoerter="Unabhängigkeit: P(M₂) = P(M₂ | ¬M₁)|P(¬M₁ ∩ M₂) / P(¬M₁) = 0,03 / 0,99 = 1/33",
    voraussetzungen="Unabhängigkeit als Gleichheit von bedingter und unbedingter Wahrscheinlichkeit|bedingte Wahrscheinlichkeit als Quotient",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kaffee/Qualitätsprüfung", textumfang="kurz",
    gegeben="M₁, M₂ unabhängig; P(M₁) = 1 %; P(¬M₁ ∩ M₂) = 3 % aus d",
    gesucht="P(M₂)",
    verfahren="Unabhängigkeit ausnutzen: P(M₂) = P(¬M₁ ∩ M₂) / P(¬M₁)",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="2023MgrundlegendBStochastikWTR1-2d",
    ergebnis="P(M₂) = P_¬M₁(M₂) = P(¬M₁ ∩ M₂) / P(¬M₁) = 1/33 (amtlich)",
    zwischenergebnis="≈ 3,03 %", niveau_geschaetzt="III",
    fehlerquelle="P(M₂) = 3 % ohne Division durch 0,99",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K5 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Unabhängigkeit in eine Gleichung für die gesuchte Wahrscheinlichkeit übersetzen. Typ wiederverwendet (2026-ea-B).")

# ---- Stochastik WTR 2: Würfel mit Netz 2/4, Spiel, zweiter Würfel
WN = "Abbildung 1: Würfelnetz in Kreuzform, waagerechte Reihe 2, 4, 2, 4, darüber 2, darunter 2 (also vier Flächen mit 2, zwei mit 4)"
row("2023MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen", typ_neben="",
    stichwoerter="nur zwei Ergebnisse je Wurf („4“ oder nicht)|zwei von sechs Flächen ⇒ p = 1/3|Würfe unabhängig|n = 30",
    voraussetzungen="Bernoulli-Kette|Laplace-Wahrscheinlichkeit aus dem Netz",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Figur", skizze=WN, kontext="Würfelspiel", textumfang="kurz",
    gegeben="Würfelnetz mit Zahlen 2, 4, 2, 4 und 2, 2; 30 Würfe; X Anzahl der „4“",
    gesucht="Begründung, dass X binomialverteilt mit p = 1/3 ist",
    verfahren="Bernoulli-Bedingungen nennen und p aus dem Netz ablesen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Bei jedem Wurf gibt es nur zwei mögliche Ergebnisse; „4“ tritt mit 1/3 ein, da zwei der sechs Seiten so beschriftet sind; jeder Wurf ist unabhängig von den anderen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Unabhängigkeit der Würfe nicht genannt",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K6 I. AB amtlich: I. Amtlich.")

row("2023MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="„4“ häufiger als „2“ ⇔ X ≥ 16|P(X ≥ 16) ≈ 2 % bei n = 30, p = 1/3",
    voraussetzungen="Bedingung in X ≥ 16 übersetzen|kumulierte Wahrscheinlichkeit am Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur", skizze=WN, kontext="Würfelspiel", textumfang="kurz",
    gegeben="X wie in a, n = 30, p = 1/3",
    gesucht="Wahrscheinlichkeit, dass „4“ häufiger erzielt wird als „2“",
    verfahren="Ereignis als X ≥ 16 (mehr als die Hälfte) erkennen, Rechner",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="2023MgrundlegendBStochastikWTR2-1a",
    ergebnis="P⅓³⁰(X ≥ 16) ≈ 2 % (amtlich)",
    zwischenergebnis="≈ 0,0188", niveau_geschaetzt="II",
    fehlerquelle="X ≥ 15 statt X ≥ 16",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Ereignis „häufiger als“ selbst in X ≥ 16 übersetzen), amtlich I. Typ wiederverwendet (2026-ga-B).")

row("2023MgrundlegendBStochastikWTR2", "c", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="C(29; 8) · (1/3)⁸ · (2/3)²¹ · 1/3|acht „4“ in den ersten 29 Würfen, „4“ beim 30. Wurf|neunmal „4“, unter anderem beim letzten Wurf",
    voraussetzungen="Bernoulli-Formel lesen|letzter Faktor als Bedingung an den letzten Wurf",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Figur", skizze=WN, kontext="Würfelspiel", textumfang="kurz",
    gegeben="Term C(29; 8) · (1/3)⁸ · (2/3)²¹ · 1/3",
    gesucht="Ereignis im Sachzusammenhang",
    verfahren="Term in Bernoulli-Anteil für 29 Würfe und Einzelfaktor für den letzten Wurf zerlegen",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Bei neun Würfen wird die „4“ erzielt, unter anderem beim letzten Wurf (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="letzten Faktor 1/3 übersehen und „genau acht Vieren“ antworten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (Teil A).")

row("2023MgrundlegendBStochastikWTR2", "d", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert der Augensumme aus dem Erwartungswert der Trefferzahl berechnen", typ_neben="",
    stichwoerter="E(X) = 30 · 1/3 = 10|10 · 4 + 20 · 2 = 80",
    voraussetzungen="Erwartungswert n · p|Summe aus Anzahl mal Wert",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Figur", skizze=WN, kontext="Würfelspiel", textumfang="kurz",
    gegeben="30 Würfe des Würfels mit 2 und 4; X Anzahl der „4“",
    gesucht="Erwartungswert der Summe der erzielten Zahlen",
    verfahren="Erwartete Anzahl der Vieren mal 4 plus erwartete Anzahl der Zweien mal 2",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2023MgrundlegendBStochastikWTR2-1a",
    ergebnis="E(X) = 10; 10 · 4 + (30 − 10) · 2 = 80 (amtlich)",
    zwischenergebnis="alternativ 30 · (1/3 · 4 + 2/3 · 2) = 80", niveau_geschaetzt="II",
    fehlerquelle="nur die Vieren gezählt",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR2", "e", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Wahrscheinlichkeitsterm über das Gegenereignis gleicher Ergebnisse begründen", typ_neben="",
    stichwoerter="(1/3)³ dreimal „4“, (2/3)³ dreimal „2“|sonst spätestens im dritten Wurf entschieden|1 − (1/3)³ − (2/3)³",
    voraussetzungen="Gegenereignis|Spielregel: Entscheidung beim ersten Wechsel der Zahl",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Figur", skizze=WN, kontext="Würfelspiel", textumfang="mittel",
    gegeben="Zwei Personen würfeln abwechselnd, bis eine Person eine andere Zahl erzielt als die andere beim unmittelbar vorhergehenden Wurf; die größere Zahl gewinnt; Term 1 − (1/3)³ − (2/3)³",
    gesucht="Begründung, dass der Term die Wahrscheinlichkeit für eine Entscheidung spätestens im dritten Wurf angibt",
    verfahren="Nicht entschieden nach drei Würfen heißt dreimal dieselbe Zahl; Gegenereignis",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(1/3)³ und (2/3)³ sind die Wahrscheinlichkeiten, dass dreimal nacheinander die „4“ bzw. die „2“ erzielt wird; in allen anderen Fällen ist das Spiel spätestens mit dem dritten Wurf entschieden (amtlich)",
    zwischenergebnis="Wert 2/3", niveau_geschaetzt="II",
    fehlerquelle="Term als Wahrscheinlichkeit für „genau im dritten Wurf“ deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR2", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit eines Spielausgangs über Pfade mit Abbruch berechnen", typ_neben="",
    stichwoerter="Anfänger verliert, wenn der Wechsel zu seinen Ungunsten ausfällt|Pfade „2, 4“ (2/3 · 1/3), „4, 4, 2“ (1/3 · 1/3 · 2/3), „2, 2, 2, 4“ (2/3 · 2/3 · 2/3 · 1/3)|Summe 32/81",
    voraussetzungen="Pfadregeln|Spielregel in Pfade übersetzen|Abbruch beim ersten Wechsel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze=WN, kontext="Würfelspiel", textumfang="mittel",
    gegeben="Spielregel wie in e; eine Person beginnt",
    gesucht="Wahrscheinlichkeit, dass der Anfänger verliert und höchstens viermal geworfen wird",
    verfahren="Alle Wurffolgen bis Länge 4 aufzählen, bei denen der erste Wechsel gegen den Anfänger ausgeht, Pfadwahrscheinlichkeiten addieren",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="2/3 · 1/3 + 1/3 · 1/3 · 2/3 + 2/3 · 2/3 · 2/3 · 1/3 = 32/81 (amtlich)",
    zwischenergebnis="≈ 0,395", niveau_geschaetzt="III",
    fehlerquelle="Pfad „4, 2“ (Anfänger hat die größere Zahl, gewinnt) mitzählen oder Werferwechsel beim Pfad „4, 4, 2“ übersehen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung III (Spielregel mit wechselnden Werfern und Abbruch in Pfade übersetzen), amtlich II.")

row("2023MgrundlegendBStochastikWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Lage- und Streumaße einer Stichprobe",
    typ="Relative Häufigkeit aus absoluten Häufigkeiten berechnen", typ_neben="",
    stichwoerter="1500 − (735 + 285) = 480|480/1500 = 32 %",
    voraussetzungen="Restanzahl bilden|relative Häufigkeit als Quotient",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Figur", skizze="Abbildung 2: Würfelnetz in Kreuzform, waagerechte Reihe 1, 3, 6, 3, darüber 1, darunter 1 (drei Flächen mit 1, zwei mit 3, eine mit 6)", kontext="Würfelspiel", textumfang="kurz",
    gegeben="zweiter Würfel mit 1, 3, 6, 3 und 1, 1; 7500 Würfe; in den ersten 1500 Würfen 735-mal „1“ und 285-mal „6“",
    gesucht="relative Häufigkeit der „3“ in den ersten 1500 Würfen",
    verfahren="Restanzahl durch 1500",
    schritte="2", zahlenraum="ganz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="(1500 − (735 + 285)) / 1500 = 32 % (amtlich)",
    zwischenergebnis="480 Würfe mit „3“", niveau_geschaetzt="I",
    fehlerquelle="Laplace-Wahrscheinlichkeit 1/3 statt beobachteter Häufigkeit",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR2", "b", innen="2", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Bedingte Restwahrscheinlichkeit nach bekannten Ergebnissen über die Binomialverteilung berechnen", typ_neben="",
    stichwoerter="17 % von 7500 = 1275|285 bereits erzielt ⇒ höchstens 990 weitere „6“|Y Anzahl der „6“ in den restlichen 6000 Würfen, p = 1/6|P(Y ≤ 990) ≈ 37 %",
    voraussetzungen="Prozentanteil in Anzahl umrechnen|bekannte Würfe abziehen|kumulierte Binomialwahrscheinlichkeit am Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur", skizze="Abbildung 2 wie in a", kontext="Würfelspiel", textumfang="kurz",
    gegeben="7500 Würfe, davon 1500 mit 285-mal „6“ bekannt; p(„6“) = 1/6",
    gesucht="Wahrscheinlichkeit, dass bei höchstens 17 % der 7500 Würfe die „6“ erzielt wird",
    verfahren="Bedingung 285 + k ≤ 0,17 · 7500 nach k auflösen, Binomialverteilung für die restlichen 6000 Würfe",
    schritte="3", zahlenraum="ganz|Prozent|Bruch", einheiten="", abhaengig_von="",
    ergebnis="Y: Anzahl der Würfe mit „6“; aus 285 + k ≤ 0,17 · 7500 ⇔ k ≤ 990 ergibt sich P⅙⁶⁰⁰⁰(Y ≤ 990) ≈ 37 % (amtlich)",
    zwischenergebnis="≈ 0,372", niveau_geschaetzt="III",
    fehlerquelle="alle 7500 Würfe als zufällig ansetzen (P(Z ≤ 1275) statt P(Y ≤ 990))",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Anteilsbedingung mit bekannten Ergebnissen in eine Schranke für die Restwürfe übersetzen.")

# ---- Stochastik WTR 3: Lehrkräfte, Kugelspiel
row("2023MgrundlegendBStochastikWTR3", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="G Gymnasium, W weiblich|W∩G 15 %, W∩¬G 57 %, ¬W∩G 10 %, ¬W∩¬G 18 %|Ränder 25 %/75 %, 72 %/28 %",
    voraussetzungen="Vierfeldertafel aus Rand- und Schnittanteil ergänzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Lehrkräfte/Schulstatistik", textumfang="kurz",
    gegeben="25 % der Lehrkräfte am Gymnasium; 15 % weiblich und am Gymnasium; 72 % weiblich",
    gesucht="vollständige Vierfeldertafel",
    verfahren="Fehlende Felder als Differenzen",
    schritte="3", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="W∩G 15 %, W∩¬G 57 %, ¬W∩G 10 %, ¬W∩¬G 18 %; Ränder W 72 %, ¬W 28 %, G 25 %, ¬G 75 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="15 % als bedingte Wahrscheinlichkeit lesen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2023MgrundlegendBStochastikWTR3", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen", typ_neben="",
    stichwoerter="W ∪ G|Gegenereignis ¬W ∩ ¬G = 18 %|1 − 18 % = 82 %",
    voraussetzungen="„oder“ als Vereinigung|Gegenereignis aus der Tafel",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Lehrkräfte/Schulstatistik", textumfang="kurz",
    gegeben="Vierfeldertafel aus a",
    gesucht="Wahrscheinlichkeit, dass eine Lehrkraft weiblich ist oder am Gymnasium arbeitet",
    verfahren="Eins minus Feld ¬W∩¬G",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="2023MgrundlegendBStochastikWTR3-1a",
    ergebnis="1 − 18 % = 82 % (amtlich)",
    zwischenergebnis="alternativ 72 % + 25 % − 15 %", niveau_geschaetzt="I",
    fehlerquelle="72 % + 25 % ohne Abzug des Schnitts",
    bemerkung="Standardbezug: K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR3", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="P_W(G) = 15 % / 72 %|≈ 21 %",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Lehrkräfte/Schulstatistik", textumfang="kurz",
    gegeben="Vierfeldertafel aus a; ausgewählte Lehrkraft ist weiblich",
    gesucht="Wahrscheinlichkeit, dass sie am Gymnasium arbeitet",
    verfahren="Schnittanteil durch Randanteil",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="2023MgrundlegendBStochastikWTR3-1a",
    ergebnis="15 % / 72 % ≈ 21 % (amtlich)",
    zwischenergebnis="≈ 0,208", niveau_geschaetzt="I",
    fehlerquelle="Bedingung vertauscht (15 %/25 %)",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2023MgrundlegendBStochastikWTR3", "d", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Bedingung an ein Anzahlverhältnis in eine Binomialwahrscheinlichkeit übersetzen", typ_neben="",
    stichwoerter="X Anzahl nicht am Gymnasium, n = 100, p = 0,75|X ≥ 4 · (100 − X) ⇔ X ≥ 80|P(X ≥ 80) ≈ 15 %",
    voraussetzungen="Verhältnisbedingung als Ungleichung|kumulierte Binomialwahrscheinlichkeit am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Lehrkräfte/Schulstatistik", textumfang="mittel",
    gegeben="100 zufällig ausgewählte Lehrkräfte; 75 % nicht am Gymnasium",
    gesucht="Wahrscheinlichkeit, dass die Anzahl nicht am Gymnasium mindestens viermal so groß ist wie die am Gymnasium",
    verfahren="Bedingung in X ≥ 80 übersetzen, Rechner",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="X: Anzahl der Lehrkräfte, die nicht an einem Gymnasium arbeiten; P₀,₇₅¹⁰⁰(X ≥ 80) ≈ 15 % (amtlich)",
    zwischenergebnis="≈ 0,149", niveau_geschaetzt="II",
    fehlerquelle="X ≥ 75 (viermal so viele wie erwartet) statt X ≥ 80",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR3", "e", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Σ von k = 75 bis 100 C(100; k) 0,75^k 0,25^(100−k)|mindestens 75 nicht am Gymnasium|höchstens 25 am Gymnasium",
    voraussetzungen="Summe als kumulierte Binomialwahrscheinlichkeit lesen|Komplement zur Anzahl am Gymnasium",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Lehrkräfte/Schulstatistik", textumfang="kurz",
    gegeben="Term Σ_{k=75}^{100} C(100; k) · 0,75^k · 0,25^(100−k)",
    gesucht="Bedeutung im Sachzusammenhang",
    verfahren="Summe als P(X ≥ 75) mit p = 0,75 erkennen und übersetzen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Der Term gibt die Wahrscheinlichkeit an, dass höchstens 25 der 100 ausgewählten Lehrkräfte an einem Gymnasium arbeiten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="„mindestens 75 am Gymnasium“",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2025-ga-B).")

row("2023MgrundlegendBStochastikWTR3", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Summand eines Erwartungswertterms im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="2 · 2 · 4/9 · 5/9|eine weiße und eine schwarze Kugel in zwei Reihenfolgen|Betrag verdoppelt und halbiert: 2 Euro",
    voraussetzungen="Erwartungswert als Summe Wert mal Wahrscheinlichkeit|Reihenfolgen zählen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Erläutern Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksspiel/Kugeln", textumfang="lang",
    gegeben="vier weiße, fünf schwarze Kugeln; Einsatz 2 Euro ausgelegt; zweimal ziehen mit Zurücklegen; weiß verdoppelt, schwarz halbiert den Betrag; Term 8 · (4/9)² + 2 · 2 · 4/9 · 5/9 + 1/2 · (5/9)²",
    gesucht="Bedeutung des zweiten Summanden mit Erläuterung",
    verfahren="Faktoren als Auszahlung 2 Euro, zwei Reihenfolgen und Wahrscheinlichkeiten 4/9 und 5/9 deuten",
    schritte="1", zahlenraum="Bruch", einheiten="Euro", abhaengig_von="",
    ergebnis="Der zweite Summand erfasst den Fall, dass eine weiße und eine schwarze Kugel gezogen werden (Wahrscheinlichkeiten 4/9 bzw. 5/9), in zwei Reihenfolgen möglich; der Spieler erhält dafür jeweils 2 Euro (amtlich)",
    zwischenergebnis="E ≈ 2,72 Euro", niveau_geschaetzt="II",
    fehlerquelle="Faktor 2 für die Reihenfolgen als Auszahlung deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MgrundlegendBStochastikWTR3", "b", innen="2", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="p Wahrscheinlichkeit für weiß|E = 8p² + 4p(1 − p) + 1/2(1 − p)² = 9/2p² + 3p + 1/2|E = 2 ⇔ p² + 2/3p − 1/3 = 0|p = 1/3 ⇒ schwarze doppelt so viele wie weiße",
    voraussetzungen="Erwartungswertterm mit Unbekannter|faires Spiel: Erwartungswert gleich Einsatz|quadratische Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel/Kugeln", textumfang="mittel",
    gegeben="Spielregel wie in a mit unbekanntem Kugelverhältnis; Spieler und Spielleiter sollen gleiche Gewinnerwartung haben",
    gesucht="Verhältnis der Anzahlen weißer und schwarzer Kugeln",
    verfahren="Erwartungswert mit p ansetzen, gleich dem Einsatz 2 setzen, quadratische Gleichung lösen, p in ein Anzahlverhältnis übersetzen",
    schritte="4", zahlenraum="Bruch|Wurzel", einheiten="Euro", abhaengig_von="",
    ergebnis="8p² + 2 · 2 · p(1 − p) + 1/2(1 − p)² = 9/2p² + 3p + 1/2 = 2 ⇔ p² + 2/3p − 1/3 = 0 ⇔ p = −1 ∨ p = 1/3; die Anzahl der schwarzen Kugeln müsste doppelt so groß sein wie die der weißen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="gleiche Gewinnerwartung als E = 0 statt E = Einsatz ansetzen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K4 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „gleiche Gewinnerwartung“ in E = Einsatz übersetzen, mit Erwartungswertterm in p. Typ wiederverwendet (Teil A).")

NEUE_TYPEN = [
    ("Nullstellen und Extremstelle einer Parabel berechnen", "Analysis", "Kurvenuntersuchung",
     "Die Nullstellen einer quadratischen Funktion über die Lösungsformel und die Extremstelle als Mitte der Nullstellen oder über die Ableitung berechnen.",
     "2023MgrundlegendBAnalysisWTR1-1a"),
    ("Abstand zwischen Parabel und waagerechter Gerade über den Scheitel beschreiben", "Analysis", "Kurvenuntersuchung",
     "Beschreiben, dass der Abstand zwischen dem Graphen einer nach unten geöffneten Parabel und einer waagerechten Geraden oberhalb als Differenz von Geradenhöhe und y-Koordinate des Hochpunkts berechnet wird.",
     "2023MgrundlegendBAnalysisWTR1-1b"),
    ("Schnittwinkel eines Graphen mit einer waagerechten Geraden über die Ableitung berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Schnittstelle eines Graphen mit einer waagerechten Geraden bestimmen und den Schnittwinkel über tan φ = f'(x₀) berechnen.",
     "2023MgrundlegendBAnalysisWTR1-1c"),
    ("Gemeinsame Tangente zweier Graphen im Schnittpunkt nachweisen und angeben", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Für zwei Graphen mit gemeinsamem Punkt nachweisen, dass die Ableitungen dort übereinstimmen, und die Gleichung der gemeinsamen Tangente angeben.",
     "2023MgrundlegendBAnalysisWTR1-1d"),
    ("Funktionswert an der Stelle stärkster Abnahme am Graphen ablesen", "Analysis", "Kurvenuntersuchung",
     "Den Wendepunkt im fallenden Bereich eines Graphen als Stelle stärkster Abnahme aufsuchen und seine y-Koordinate im Sachzusammenhang ablesen.",
     "2023MgrundlegendBAnalysisWTR1-2b"),
    ("Relative Abweichung zwischen Tangente und Funktion als Ungleichung im Sachzusammenhang deuten", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Eine Ungleichung der Form |t(x) − f(x)| / f(x) < c auf einem Intervall als Aussage über die Güte der Tangente als Näherung der Funktion im Sachzusammenhang interpretieren.",
     "2023MgrundlegendBAnalysisWTR1-2c"),
    ("Einfluss eines additiven Scharparameters auf den Graphen beschreiben", "Analysis", "Funktionsscharen und Ortskurven",
     "Beschreiben, dass ein additiver Scharparameter den Graphen in y-Richtung verschiebt.",
     "2023MgrundlegendBAnalysisWTR1-3a"),
    ("Scharparameter für den Mittelpunkt der Extrempunkte auf der x-Achse bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Scharparameter bestimmen, für den der Mittelpunkt der Strecke zwischen den beiden Extrempunkten auf der x-Achse liegt, über die Bedingung an die Summe der Funktionswerte.",
     "2023MgrundlegendBAnalysisWTR1-3b"),
    ("Scharparameter für genau eine Nullstelle über die Lage der Extrempunkte angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Alle Werte eines additiven Scharparameters angeben, für die die Funktion genau eine Nullstelle hat, aus der Lage von Tief- und Hochpunkt zur x-Achse und dem Grenzverhalten.",
     "2023MgrundlegendBAnalysisWTR1-3c"),
    ("Transformation: Anzahl verschiedener Ergebnisse bei vertauschter Reihenfolge von Spiegelung und Verschiebungen begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Begründen, wie viele verschiedene Graphen entstehen, wenn Spiegelung an der x-Achse und Verschiebungen in x- und y-Richtung in allen Reihenfolgen ausgeführt werden.",
     "2023MgrundlegendBAnalysisWTR2-1e"),
    ("Aufgabenstellung zu Extremstellen und Wertedifferenz aus dem Lösungsweg formulieren und erläutern", "Analysis", "Kurvenuntersuchung",
     "Zu einer Rechnung, die Extremstellen bestimmt und die Differenz der zugehörigen Funktionswerte bildet, eine passende Aufgabenstellung im Sachzusammenhang formulieren und die Schritte erläutern.",
     "2023MgrundlegendBAnalysisWTR2-2b"),
    ("Nullstellen und Werte: Wertemenge und Häufigkeit der Werte einer Sinusfunktion auf einer Periode angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Für eine gestreckte und verschobene Sinusfunktion auf einer Periode alle angenommenen Werte und angeben, wie oft jeder Wert angenommen wird.",
     "2023MgrundlegendBAnalysisWTR2-2c"),
    ("Länge der Monotoniebereiche zweier Modellfunktionen vergleichen und eine Aussage beurteilen", "Analysis", "Kurvenuntersuchung",
     "Die Länge des Bereichs steigender Werte zweier Modellfunktionen aus ihren Extremstellen bestimmen und eine Aussage über den Unterschied beurteilen.",
     "2023MgrundlegendBAnalysisWTR2-2d"),
    ("Körper: Volumen eines Prismas mit Trapezquerschnitt im Sachzusammenhang berechnen und mit einer Vorgabe vergleichen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Das Volumen eines Körpers mit Trapezquerschnitt als Prisma berechnen und mit einer vorgegebenen Füllmenge vergleichen.",
     "2023MgrundlegendBAGLAA1WTR-1b"),
    ("Erreichbarkeit der Grundfläche über den größten Abstand zu einem Punkt beurteilen", "Analytische Geometrie", "Abstände",
     "Die von einem Punkt am weitesten entfernten Ecken einer Fläche bestimmen, den Abstand berechnen und mit einer vorgegebenen Länge vergleichen.",
     "2023MgrundlegendBAGLAA1WTR-1c"),
    ("Verflechtung: Eintrag der Gesamtmatrix aus dem Diagramm bestätigen und Nulleintrag begründen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen Eintrag der Gesamtbedarfsmatrix als Summe der Pfadprodukte im Verflechtungsdiagramm nachrechnen und einen Nulleintrag über fehlende Pfade begründen.",
     "2023MgrundlegendBAGLAA1WTR-2a"),
    ("Verflechtung: Höchstmenge aus einer Kostenschranke bei festem Mengenverhältnis ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Bei festem Verhältnis der Produktionsmengen den Rohstoffbedarf und die Kosten als Term in einer Unbekannten ansetzen und die Höchstmengen aus einer Kostenschranke ermitteln.",
     "2023MgrundlegendBAGLAA1WTR-2b"),
    ("Verflechtung: Format der Bedarfsmatrix aus der Anzahl der Stufenprodukte begründen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Zeilen- und Spaltenzahl einer Bedarfsmatrix aus der Anzahl der Produkte der beteiligten Stufen angeben und begründen.",
     "2023MgrundlegendBAGLAA1WTR-2c"),
    ("Ebene Figur: Drachenviereck über zwei Paare gleich langer Seiten nachweisen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Ein Viereck als Drachenviereck nachweisen, indem zwei Paare benachbarter gleich langer Seiten aus den Koordinaten berechnet werden.",
     "2023MgrundlegendBAGLAA2WTR1-1a"),
    ("Symmetrieebene eines geraden Prismas über die Symmetrieachse der Grundfläche begründen", "Analytische Geometrie", "Spiegelung",
     "Begründen, dass eine Ebene Symmetrieebene eines geraden Prismas ist, weil sie die Symmetrieachse der Grundfläche enthält und senkrecht auf der Grundfläche steht.",
     "2023MgrundlegendBAGLAA2WTR1-1c"),
    ("Körper: Volumenrechnung eines Prismas aus einem Lösungsweg erläutern", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Die Faktoren einer vorgegebenen Volumenrechnung eines Prismas geometrisch deuten (Grundfläche, Höhe, Zerlegung).",
     "2023MgrundlegendBAGLAA2WTR1-1d"),
    ("Körper: Geschwindigkeit entlang einer Kante aus Kantenlänge und Zeit berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Die Länge einer Kante aus den Koordinaten berechnen und mit einer Zeitangabe und Einheitenumrechnung eine mittlere Geschwindigkeit bestimmen.",
     "2023MgrundlegendBAGLAA2WTR1-1e"),
    ("Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Den Winkel zwischen einer Geraden und einer Ebene über sin φ = |u · n| / (|u| · |n|) aus Richtungs- und Normalenvektor berechnen.",
     "2023MgrundlegendBAGLAA2WTR1-1f"),
    ("Ebene Figur: Gleichschenkligkeit über Seitenlängen nachweisen und Parallelität einer Kante zur Grundfläche begründen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Ein Dreieck über gleiche Schenkellängen als gleichschenklig nachweisen und die Parallelität einer Kante zu einer Koordinatenebene über gleiche Koordinaten begründen.",
     "2023MgrundlegendBAGLAA2WTR2-1a"),
    ("Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen", "Analytische Geometrie", "Schnittmengen",
     "Die Spitze einer Pyramide als Schnittpunkt der Geraden durch zwei Punkte einer Kante mit einer Koordinatenachse berechnen.",
     "2023MgrundlegendBAGLAA2WTR2-1d"),
    ("Abstand eines Punktes zu einer Ebene über eine Schrägstrecke nach oben abschätzen", "Analytische Geometrie", "Abstände",
     "Begründen, dass der Abstand eines Punktes zu einer Ebene kleiner als die Länge einer nicht senkrechten Verbindungsstrecke zu einem Ebenenpunkt ist, und dies in einer Skizze veranschaulichen.",
     "2023MgrundlegendBAGLAA2WTR2-1e"),
    ("Körper: Volumenverlauf eines Restkörpers in Abhängigkeit vom Parameter als linear begründen und Graphen zuordnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Das Volumen eines Restkörpers als Differenz eines konstanten Volumens und eines Pyramidenvolumens mit linear vom Parameter abhängiger Höhe darstellen und den passenden Graphen begründen.",
     "2023MgrundlegendBAGLAA2WTR2-1f"),
    ("Anzahl geordneter Auswahlen ohne Wiederholung berechnen", "Stochastik", "Kombinatorik",
     "Die Anzahl der Möglichkeiten, k aus n Objekten in festgelegter Reihenfolge ohne Wiederholung auszuwählen, als Produkt n · (n − 1) · … berechnen.",
     "2023MgrundlegendBStochastikWTR1-1a"),
    ("Wahrscheinlichkeit eines zweistufigen Prüfplans über Binomialwahrscheinlichkeiten berechnen", "Stochastik", "Binomialverteilung",
     "Die Annahmewahrscheinlichkeit eines Prüfplans mit einer ersten Stichprobe und einer bedingten zweiten Stichprobe als Summe von Binomialwahrscheinlichkeiten und einem Produkt berechnen.",
     "2023MgrundlegendBStochastikWTR1-2a"),
    ("Wirkung eines kleineren Stichprobenumfangs auf eine Annahmewahrscheinlichkeit ohne Rechnung beurteilen", "Stochastik", "Binomialverteilung",
     "Ohne Rechnung beurteilen, wie sich ein kleinerer Stichprobenumfang bei gleicher Annahmezahl auf die Wahrscheinlichkeit „höchstens k Ausschuss“ auswirkt und für wen das vorteilhaft ist.",
     "2023MgrundlegendBStochastikWTR1-2b"),
    ("Wahrscheinlichkeit eines Schnitts aus einem Randanteil und dem Anteil ohne beide Mängel nachweisen", "Stochastik", "Ereignisse und Mengenoperationen",
     "P(¬A ∩ B) als Differenz P(¬A) − P(¬A ∩ ¬B) nachweisen, wenn der Anteil ohne beide Merkmale und ein Randanteil gegeben sind.",
     "2023MgrundlegendBStochastikWTR1-2d"),
    ("Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen", "Stochastik", "Binomialverteilung",
     "Begründen, dass eine Zufallsgröße binomialverteilt ist (zwei Ergebnisse je Versuch, feste Trefferwahrscheinlichkeit, Unabhängigkeit), und p aus dem Sachzusammenhang ablesen.",
     "2023MgrundlegendBStochastikWTR2-1a"),
    ("Erwartungswert der Augensumme aus dem Erwartungswert der Trefferzahl berechnen", "Stochastik", "Kenngrößen von Verteilungen",
     "Den Erwartungswert der Summe der erzielten Zahlen bei einem zweiwertigen Würfel aus E(X) = n · p und der Restanzahl berechnen.",
     "2023MgrundlegendBStochastikWTR2-1d"),
    ("Term und Ereignis: Wahrscheinlichkeitsterm über das Gegenereignis gleicher Ergebnisse begründen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Begründen, dass ein Term der Form 1 − p^n − (1 − p)^n die Wahrscheinlichkeit dafür angibt, dass ein Spiel spätestens nach n Würfen entschieden ist (Gegenereignis: alle Ergebnisse gleich).",
     "2023MgrundlegendBStochastikWTR2-1e"),
    ("Wahrscheinlichkeit eines Spielausgangs über Pfade mit Abbruch berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Für ein Spiel mit abwechselnden Würfen und Abbruch beim ersten Wechsel die Wahrscheinlichkeit eines Ausgangs bei begrenzter Wurfzahl als Summe der Pfadwahrscheinlichkeiten berechnen.",
     "2023MgrundlegendBStochastikWTR2-1f"),
    ("Relative Häufigkeit aus absoluten Häufigkeiten berechnen", "Stochastik", "Lage- und Streumaße einer Stichprobe",
     "Die relative Häufigkeit eines Ergebnisses aus der Gesamtzahl und den Häufigkeiten der übrigen Ergebnisse berechnen.",
     "2023MgrundlegendBStochastikWTR2-2a"),
    ("Bedingte Restwahrscheinlichkeit nach bekannten Ergebnissen über die Binomialverteilung berechnen", "Stochastik", "Binomialverteilung",
     "Eine Anteilsbedingung für eine Gesamtserie, von der ein Teil mit bekanntem Ergebnis vorliegt, in eine Schranke für die restlichen Versuche übersetzen und die Wahrscheinlichkeit binomial berechnen.",
     "2023MgrundlegendBStochastikWTR2-2b"),
    ("Wahrscheinlichkeit einer Vereinigung aus der Vierfeldertafel über das Gegenereignis berechnen", "Stochastik", "Vierfeldertafel",
     "P(A ∪ B) aus der Vierfeldertafel als 1 − P(¬A ∩ ¬B) berechnen.",
     "2023MgrundlegendBStochastikWTR3-1b"),
    ("Bedingung an ein Anzahlverhältnis in eine Binomialwahrscheinlichkeit übersetzen", "Stochastik", "Binomialverteilung",
     "Eine Bedingung wie „mindestens viermal so viele wie“ in eine Ungleichung für die Trefferzahl übersetzen und die Wahrscheinlichkeit mit dem Rechner ermitteln.",
     "2023MgrundlegendBStochastikWTR3-1d"),
    ("Summand eines Erwartungswertterms im Sachzusammenhang deuten", "Stochastik", "Kenngrößen von Verteilungen",
     "Einen Summanden eines gegebenen Erwartungswertterms als Produkt aus Auszahlung, Anzahl der Reihenfolgen und Wahrscheinlichkeiten im Sachzusammenhang erläutern.",
     "2023MgrundlegendBStochastikWTR3-2a"),
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
    t = t.replace(MARKE_KONTEXT.lower(), " ")  # feste Markierung, bewusst umlautfrei (v0.7)
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
    ist die Aufgabe ungegliedert (Kennung, '', ''); in Teil B kann eine nummerierte
    Aufgabe ohne Buchstaben stehen (Kennung-3, Buchstabe '')."""
    m = re.fullmatch(r"(" + KENNUNG.pattern + r")(?:-(?=.)(\d*)([a-z]?))?", i)
    if not m:
        return None, None, None
    return m.group(1), m.group(2) or "", m.group(3) or ""


def hoechster_afb(v):
    return max(ORD.get(t, 0) for t in v.split("|")) if v else 0


def pruefe_zeile(z, a):
    """Alle Prüfungen, die eine einzelne Zeile aus sich selbst und iqb-quellen.csv bestehen kann."""
    i = z["id"] or "(ohne id)"
    for k in PFLICHT:
        if k == "afb_amtlich" and z[k] == "" and "Standardbezug: keine Eintragung" in z["bemerkung"]:
            continue  # Zeile der Teilaufgabe im Standardbezug leer (v0.5)
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
    if z["afb_amtlich"] == "":
        a("Standardbezug: keine Eintragung" in z["bemerkung"],
          f"{i}: afb_amtlich leer, bemerkung nennt nicht „Standardbezug: keine Eintragung“")
    else:
        a(AFB.fullmatch(z["afb_amtlich"]) is not None, f"{i}: afb_amtlich ungültig: {z['afb_amtlich']}")
        teile = z["afb_amtlich"].split("|")
        a(all(t in ORD for t in teile) and [ORD[t] for t in teile if t in ORD] == sorted(
            {ORD[t] for t in teile if t in ORD}), f"{i}: afb_amtlich nicht aufsteigend ohne Wiederholung")
    a("Standardbezug:" in z["bemerkung"], f"{i}: bemerkung nennt den Standardbezug nicht")
    # Trägerbindung: nur die feste Markierung am Feldanfang, keine andere Schreibweise (v0.7)
    b = z["bemerkung"]
    a("Trägerbindung" not in b and "Traegerbindung: frei" not in b,
      f"{i}: Trägerbindung nur als „{MARKE_KONTEXT}“ am Anfang von bemerkung (kein Vermerk heißt frei)")
    if MARKE_KONTEXT.lower() in b.lower():
        a(b.startswith(MARKE_KONTEXT) and (b[len(MARKE_KONTEXT):len(MARKE_KONTEXT) + 1] in (".", " ")),
          f"{i}: Markierung „{MARKE_KONTEXT}“ muss am Anfang von bemerkung stehen, gefolgt von Punkt oder Klammer")
    if z["block"] == "B":
        m = AB_SPALTE.search(b)
        a(m is not None, f"{i}: Teil B braucht „AB amtlich: I|II|III.“ in bemerkung (Spalte Anforderungsbereich)")
        if m and z["afb_amtlich"]:
            a(ORD[m.group(1)] == hoechster_afb(z["afb_amtlich"]) or AB_HINWEIS in b,
              f"{i}: Spalte Anforderungsbereich ≠ höchster Kompetenzeintrag, bemerkung braucht „{AB_HINWEIS}“")
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
        # id und abhaengig_von tragen in Teil B den Bindestrich vor der Aufgabennummer (…WTR1-2a), v0.6
        a(k in ("id", "abhaengig_von") or not re.search(r"(?<=[\d\s(])-(?=\d)", v),
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
# Teil B: der Standardbezug hat eine eigene Spalte Anforderungsbereich; sie steht in
# bemerkung als „AB amtlich: III" und ist für die Eichung maßgeblich (iqb.md § 4, v0.7).
AB_SPALTE = re.compile(r"AB amtlich: (I{1,3})\.")
AB_HINWEIS = "Anforderungsbereich weicht vom höchsten Kompetenzeintrag ab"
# Trägerbindung (iqb.md § 7): feste Markierung am Anfang von bemerkung, kein eigenes Feld.
MARKE_KONTEXT = "Traegerbindung: Kontext"


def amtlich_von(z):
    """Amtlicher Bereich für die Eichung: Teil A das Maximum über afb_amtlich, Teil B die
    Spalte Anforderungsbereich aus bemerkung."""
    if z["block"] == "B":
        m = AB_SPALTE.search(z["bemerkung"])
        return ORD[m.group(1)] if m else 0
    return hoechster_afb(z["afb_amtlich"])


def geschaetzt_eng(z):
    """Schätzung nach der engen Fassung (iqb.md § 7): steht sie in bemerkung, gilt sie,
    sonst niveau_geschaetzt. Zeilen, die schon nach der engen Fassung erfasst sind,
    tragen keinen Vermerk."""
    m = ENG.search(z["bemerkung"])
    return m.group(1) if m else z["niveau_geschaetzt"]


def eichung(zeilen, eng=False):
    """Trefferquote der Schätzung gegen den höchsten amtlichen Bereich (iqb.md § 4);
    eng=True wertet die enge Fassung aus. Rückgabe: Treffer, Abweichungen, Zahl
    der gewerteten Zeilen (ohne afb_amtlich leer, v0.5)."""
    treffer, abw, gewertet = 0, [], 0
    for z in zeilen:
        amt = amtlich_von(z)
        if not amt:
            continue
        gewertet += 1
        wert = geschaetzt_eng(z) if eng else z["niveau_geschaetzt"]
        if amt == ORD.get(wert, 0):
            treffer += 1
        else:
            abw.append(f"{z['id']} geschätzt {wert}, amtlich höchstens "
                       f"{[k for k, v in ORD.items() if v == amt][0]}")
    return treffer, abw, gewertet


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
        stapel = {einheit(QUELLE[k]) for k in kennungen if k in QUELLE}
        for s in sorted(stapel):
            fehlt = [k for k, q in QUELLE.items()
                     if einheit(q) == s and not q["dublette_von"] and k not in kennungen]
            a(not fehlt, f"Stapel {s} im Bestand unvollständig, es fehlen {fehlt}")
        je_datei = {}
        for z in alt:
            k_, innen_, _ = kennung_aus_id(z["id"])
            je_datei.setdefault((k_, innen_), []).append(z["teilaufgabe"])
        for k, tl in je_datei.items():
            a("" not in tl or len(tl) == 1, f"{k}: ungegliederte Aufgabe neben gegliederten Zeilen")
        if fehler:
            print(f"\nSelbstprüfung: {len(fehler)} Fehler")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        treffer, abw, gew = eichung(alt)
        treffer_eng, _, _ = eichung(alt, eng=True)
        print(f"Selbstprüfung bestanden: {len(alt)} Katalogzeilen, {len(alt_typ)} Typen, "
              f"alle Typen verwendet, {len(stapel)} Stapel vollständig. ZEILEN ist leer, nichts geschrieben.")
        if gew:
            print(f"Eichung über den Bestand: {treffer} von {gew} gewerteten Zeilen treffen den höchsten "
                  f"amtlichen Bereich ({100 * treffer // gew} %), enge Fassung {treffer_eng} "
                  f"({100 * treffer_eng // gew} %); {len(alt) - gew} Zeilen ohne Standardbezug.")
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
    im_stapel = {k for k, q in QUELLE.items() if einheit(q) == stapel}
    dubletten = {k for k in im_stapel if QUELLE[k]["dublette_von"]}
    a(im_stapel, f"Stapel {stapel} unbekannt in {QUELLEN}")
    dateien = {z["_kennung"] for z in ZEILEN}
    for k in sorted(dateien - im_stapel):
        a(False, f"{k}: gehört nicht zum Stapel {stapel}")
    je_datei = {}
    for z in ZEILEN:
        je_datei.setdefault((z["_kennung"], kennung_aus_id(z["id"])[1]), []).append(z["teilaufgabe"])
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
    treffer_eng, abw_eng, gew = eichung(ZEILEN, eng=True)
    if gew >= SCHWELLEN["eichung_ab_zeilen"]:
        a(treffer_eng / gew >= SCHWELLEN["eichung_mindestens"],
          f"Schwelle gerissen: Eichung (enge Fassung) {treffer_eng} von {gew} "
          f"({100 * treffer_eng / gew:.0f} %), verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %: "
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
    treffer, abw, gew = eichung(ZEILEN)
    print(f"Eichung: {treffer} von {gew} gewerteten Zeilen treffen den höchsten amtlichen Bereich"
          + (f" ({n - gew} ohne Standardbezug)" if gew != n else "")
          + (f"; Abweichungen: {'; '.join(abw)}" if abw else ""))
    if treffer_eng != treffer:
        print(f"Eichung enge Fassung: {treffer_eng} von {gew}")
    print(f"Schwellen: {len(unsicher)} Zeilen mit „?“ (erlaubt {grenze_frage}), "
          f"{len(ersatz)} ohne passendes Thema (erlaubt {grenze_ersatz}), "
          f"Eichung {100 * treffer_eng / gew if gew else 0:.0f} % (verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %)")
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
          f"({100 * len(neu & verwendet) / len(verwendet):.0f} %) | {treffer} von {gew} "
          f"({100 * treffer / gew if gew else 0:.0f} %)"
          + (f", eng {treffer_eng} ({100 * treffer_eng / gew:.0f} %)" if treffer_eng != treffer else "")
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
