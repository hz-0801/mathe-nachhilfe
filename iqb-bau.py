# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.7 · 14.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.8

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

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
    "stapel": "2025-ea-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2025MerhoehtBAnalysisWTR1": 30,
        "2025MerhoehtBAnalysisWTR2": 30,
        "2025MerhoehtBAnalysisWTR3": 30,
        "2025MerhoehtBAGLAA1WTR": 20,
        "2025MerhoehtBAGLAA2WTR": 20,
        "2025MerhoehtBStochastikWTR1": 20,
        "2025MerhoehtBStochastikWTR2": 20,
        "2025MerhoehtBStochastikWTR3": 16,
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
# Stapel 2025-ea-B, WTR-Zweig. innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Stochastik WTR 3, Aufgabe 1 ist wortgleich mit Stochastik WTR 2, Aufgabe 1: keine Zeile, Soll 16 statt 20.
# Stochastik WTR 3, Aufgabe 2 teilt a und b mit WTR 2, Aufgabe 2, unterscheidet sich in c und d: Zeilen bleiben.

SOLL = {"2025MerhoehtBAnalysisWTR1": 30, "2025MerhoehtBAnalysisWTR2": 30, "2025MerhoehtBAnalysisWTR3": 30,
        "2025MerhoehtBAGLAA1WTR": 20, "2025MerhoehtBAGLAA2WTR": 20,
        "2025MerhoehtBStochastikWTR1": 20, "2025MerhoehtBStochastikWTR2": 20, "2025MerhoehtBStochastikWTR3": 16}

# ---- Analysis WTR 1, Aufgabe 1: Schar f_a = 1/3 x³ − ax + 2a, dann f = f_2
GF1 = "Koordinatensystem mit Gitter, x von −3 bis 3, y von −1 bis 7; Graph von f_2 punktsymmetrisch zu (0 | 4), Hochpunkt bei etwa (−1,4 | 5,9), Tiefpunkt bei etwa (1,4 | 2,1)"
row("2025MerhoehtBAnalysisWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben", typ_neben="",
    stichwoerter="f_a(0) = 2a = 4 ⇔ a = 2",
    voraussetzungen="y-Achsenabschnitt der Schar",
    format="Begründung", operator="Begründen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = 1/3 x³ − ax + 2a, a ∈ IR; abgebildeter Graph durch (0 | 4)",
    gesucht="Begründung, dass es der Graph von f_2 ist",
    verfahren="f_a(0) = 4 nach a auflösen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_a(0) = 4 ⇔ 2a = 4 ⇔ a = 2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Punktprobe mit a = 2 ohne Eindeutigkeit",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2025MerhoehtBAnalysisWTR1", "b", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Einzigen Wendepunkt einer Schar nachweisen und angeben", typ_neben="",
    stichwoerter="f_a'(x) = x² − a, f_a''(x) = 2x, f_a'''(x) = 2|f'' = 0 ⇔ x = 0, f''' ≠ 0|Wendepunkt (0 | 2a)",
    voraussetzungen="Ableitungen mit Parameter|Wendepunktkriterium|Parameterabhängige Koordinaten",
    format="Rechnung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a wie in a",
    gesucht="Nachweis genau eines Wendepunkts je Graph und dessen Koordinaten",
    verfahren="f'' = 0 lösen, f''' prüfen, f_a(0)",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_a'(x) = x² − a; f_a''(x) = 2x; f_a'''(x) = 2; wegen f_a''(x) = 0 ⇔ x = 0 und f_a'''(0) = 2 ≠ 0 besitzt der Graph von f_a mit (0 | 2a) genau einen Wendepunkt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Eindeutigkeit (nur eine Nullstelle von f'') nicht benennen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBAnalysisWTR1", "c", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einer Integralbedingung bestimmen", typ_neben="",
    stichwoerter="∫_0^2 f_a = [1/12 x⁴ − 1/2 ax² + 2ax]_0^2 = 4/3 + 2a|= 0 ⇔ a = −2/3",
    voraussetzungen="Stammfunktion mit Parameter|lineare Gleichung in a",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Bedingung ∫_0^2 f_a(x) dx = 0",
    gesucht="Wert von a",
    verfahren="Integral in a berechnen, null setzen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="∫_0^2 f_a(x) dx = [1/12 x⁴ − 1/2 ax² + 2ax]_0^2 = 4/3 + 2a; ∫_0^2 f_a(x) dx = 0 ⇔ a = −2/3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="2a beim Integrieren als Konstante vergessen",
    bemerkung="Standardbezug: K1 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBAnalysisWTR1", "d", innen="1", seite="2", punkte="6", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Faktorisierung von f(x) − t(x) nachweisen und weiteren Schnittpunkt von Tangente und Graph begründen", typ_neben="",
    stichwoerter="f(x) − (7x − 14) = 1/3 x³ − 9x + 18|1/3 (x − 3)² (x + 6) ausmultipliziert = 1/3 x³ − 9x + 18|f(x) = 7x − 14 ⇔ x = 3 ∨ x = −6",
    voraussetzungen="Termumformung mit Binom|gemeinsame Punkte als Nullstellen der Differenz|Satz vom Nullprodukt",
    format="Rechnung|Begründung", operator="Zeigen Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 1/3 x³ − 2x + 4 (= f_2); Tangente t in P(3 | f(3)) mit y = 7x − 14; Behauptung f(x) − (7x − 14) = 1/3 (x − 3)² (x + 6)",
    gesucht="rechnerischer Nachweis der Identität und Begründung genau eines weiteren gemeinsamen Punkts",
    verfahren="beide Seiten ausmultiplizieren, dann Nullprodukt",
    schritte="4", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(x) − (7x − 14) = 1/3 x³ − 9x + 18; 1/3 (x − 3)² (x + 6) = 1/3 (x² − 6x + 9)(x + 6) = 1/3 (x³ − 6x² + 9x + 6x² − 36x + 54) = 1/3 x³ − 9x + 18; f(x) = 7x − 14 ⇔ 1/3 (x − 3)² (x + 6) = 0 ⇔ x = 3 ∨ x = −6 (amtlich)",
    zwischenergebnis="weiterer Punkt (−6 | −56)", niveau_geschaetzt="II",
    fehlerquelle="Ausmultiplizieren des Binoms mit Vorzeichenfehler",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Weiteren Schnittpunkt … aus einer vorgegebenen Faktorisierung begründen“ (2025-ga-B, 1c) getrennt: hier ist die Faktorisierung nachzuweisen.")

row("2025MerhoehtBAnalysisWTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Anzahl der Lösungen einer Integralgleichung über gleitende Streifen am Graphen untersuchen", typ_neben="",
    stichwoerter="∫_k^{k+1} f = Fläche eines Streifens der Breite 1 unter G_f (f > 0 dort)|für k = 1,5 kleiner als 4, mit wachsendem k stetig wachsend (G_f steigt)|für k = 2,5 schon größer als 4|genau eine Lösung für k ≥ 1,5",
    voraussetzungen="Integral als Streifenfläche|Monotonie des Streifeninhalts aus dem Graphen|Zwischenwertargument",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="mittel",
    gegeben="Gleichung ∫_k^{k+1} f(x) dx = 4; für −1,5 ≤ k ≤ 1,5 genau eine Lösung",
    gesucht="Anzahl der Lösungen für k ≥ 1,5, grafisch mit Abbildung 1",
    verfahren="Streifen der Breite 1 nach rechts schieben, Inhalt vergleichen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="der Wert des Integrals entspricht für k ≥ 1,5 dem Inhalt des Flächenstücks zwischen G_f und der x-Achse im Bereich k ≤ x ≤ k + 1, einem Streifen der Breite 1; mit wachsendem k, beginnend bei k = 1,5, wird der Wert, der für k = 1,5 kleiner als 4 ist, kontinuierlich größer; da er für k = 2,5 bereits größer als 4 ist, gibt es im Bereich k ≥ 1,5 genau eine Lösung (amtlich)",
    zwischenergebnis="k = 1,5: ≈ 2,83; k = 2,5: ≈ 7,25; Lösung k ≈ 1,90", niveau_geschaetzt="III",
    fehlerquelle="nur die Existenz einer Lösung begründen",
    bemerkung="Standardbezug: K1 III, K2 II, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (e) Integral als gleitender Streifen am Graphen gedeutet, verkettet mit Monotonie und Zwischenwert.")

# ---- Analysis WTR 1, Aufgabe 2: Reichweite (Sachtext wortgleich mit 2025-ga-B Analysis WTR 1, Aufgabe 2)
REICH = "Koordinatensystem x von −12 bis 36 (°C), y von 0 bis 1,2; Graph von r steigt von etwa 0,55 bei −12 über 0,7 bei 0 zum Hochpunkt (22 | 1,2) und fällt auf etwa 0,95 bei 36"
row("2025MerhoehtBAnalysisWTR1", "a", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Extrempunkte: Hochpunkt aus dem Graphen ablesen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Hochpunkt (22 | 1,2)|größte Reichweite bei 22 °C|das 1,2-Fache der Nennreichweite",
    voraussetzungen="Ablesen|Koordinaten als Temperatur und Quotient deuten",
    format="Kurzantwort", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=REICH, kontext="Elektroauto/Reichweite", textumfang="lang",
    gegeben="r(x) Quotient aus tatsächlicher Reichweite und Nennreichweite bei Außentemperatur x in °C, −12 ≤ x ≤ 36; Graph in Abbildung 2",
    gesucht="Koordinaten des Hochpunkts und ihre Bedeutung",
    verfahren="Ablesen, beide Koordinaten deuten",
    schritte="2", zahlenraum="dezimal", einheiten="°C", abhaengig_von="",
    ergebnis="(22 | 1,2); die größte tatsächliche Reichweite liegt bei einer Außentemperatur von 22 °C vor; diese beträgt das 1,2-Fache der Nennreichweite (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="1,2 als Reichweite in km deuten",
    bemerkung="Standardbezug: K3 II, K4 I, K6 II. AB amtlich: II. Amtlich (Ablesung). Teilaufgabe wortgleich mit 2025-ga-B Analysis WTR 1, 2a (andere Trägeraufgabe, eigene Zeile, gemeinsamer Typ).")

row("2025MerhoehtBAnalysisWTR1", "b", innen="2", seite="3", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Gleichheit zweier Sachgrößen als Bedingung an den Funktionswert übersetzen und Stelle am Graphen ablesen", typ_neben="",
    stichwoerter="r(x) · 320 km = r(0) · 500 km|r(x) = r(0) · 500/320 ≈ 0,7 · 500/320 ≈ 1,1|r(14) ≈ 1,1: etwa 14 °C",
    voraussetzungen="tatsächliche Reichweite = r · Nennreichweite|Gleichung nach r(x) auflösen|r(0) ablesen|Stelle zu einem Wert ablesen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=REICH, kontext="Elektroauto/Reichweite", textumfang="mittel",
    gegeben="Nennreichweiten 320 km (Auto A) und 500 km (Auto B); r wie in a",
    gesucht="eine Außentemperatur, bei der A dieselbe tatsächliche Reichweite hat wie B bei 0 °C",
    verfahren="Gleichung der Reichweiten aufstellen, r(x) berechnen, am Graphen ablesen",
    schritte="4", zahlenraum="dezimal", einheiten="°C|km", abhaengig_von="",
    ergebnis="r(x) · 320 km = r(0) · 500 km ⇒ r(x) = r(0) · 500 km/320 km ≈ 0,7 · 500/320 ≈ 1,1; r(14) ≈ 1,1; mögliche Außentemperatur etwa 14 °C (amtlich)",
    zwischenergebnis="auch etwa 30 °C möglich (zweite Stelle mit r ≈ 1,1)", niveau_geschaetzt="III",
    fehlerquelle="Quotient 320/500 statt 500/320",
    bemerkung="Standardbezug: K2 III, K3 II, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (1,09). Eichregel: (a) Gleichheit der Reichweiten in eine Gleichung für r(x) übersetzen, verkettet mit zwei Ablesungen.")

# ---- Analysis WTR 2, Aufgabe 1: f(x) = 5x e^−x, Wappen
GW = "Koordinatensystem x von 0 bis 6, y von −2 bis 3; Graph G von 5x e^−x durch den Ursprung, Hochpunkt (1 | 1,84), rechts abflachend gegen 0; Abb. 2: Wappenfigur zwischen y = 5 und den Kurvenstücken H1 (Spiegelung von G an y = x für x ∈ [ln 5; 5]) und H2 (Spiegelung von H1 an x = ln 5), Spitze S(ln 5 | ln 5)"
row("2025MerhoehtBAnalysisWTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen", typ_neben="",
    stichwoerter="f'(x) = 5e^−x + 5x e^−x · (−1) = 5(1 − x) e^−x|f'(x) = 0 ⇔ x = 1|f(1) = 5/e",
    voraussetzungen="Produkt- und Kettenregel|Nullstelle der Ableitung|Funktionswert",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GW, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 5x · e^−x in IR; G hat genau einen Extrempunkt; Kontrolle (1 | 5/e)",
    gesucht="Koordinaten des Extrempunkts",
    verfahren="f' = 0, einsetzen",
    schritte="3", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 5e^−x + 5x · e^−x · (−1) = 5 · (1 − x) · e^−x; f'(x) = 0 ⇔ x = 1; f(1) = 5/e; Extrempunkt (1 | 5/e) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="innere Ableitung −1 vergessen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-B).")

row("2025MerhoehtBAnalysisWTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Gerade senkrecht zu einer gegebenen Tangente durch einen Punkt aufstellen", typ_neben="",
    stichwoerter="t: y = −5/e² x + 20/e², Steigung −5/e²|senkrecht: Steigung e²/5|durch (1 | 5/e): n = 5/e − e²/5",
    voraussetzungen="negativer Kehrwert der Steigung|Achsenabschnitt aus einem Punkt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Tangente im Wendepunkt t: y = −5/e² · x + 20/e²; Extrempunkt (1 | 5/e)",
    gesucht="Gleichung der Geraden durch den Extrempunkt senkrecht zu t",
    verfahren="Steigung e²/5, Punkt einsetzen",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2025MerhoehtBAnalysisWTR2-1a",
    ergebnis="y = e²/5 · x + n; 5/e = e²/5 · 1 + n ⇔ n = 5/e − e²/5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Steigung 5/e² (Vorzeichen) statt e²/5",
    bemerkung="Standardbezug: K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBAnalysisWTR2", "c", innen="1", seite="1", punkte="6", afb_amtlich="I|II",
    leitidee="Analysis", thema="Umkehrfunktion",
    typ="Umkehrbarkeit auf einem Intervall begründen und Definitions- und Wertebereich der Umkehrfunktion angeben", typ_neben="",
    stichwoerter="f nicht umkehrbar: zwei x-Werte mit f(x) = 1 (Abbildung)|h auf [1; ∞[ streng monoton (einzige Extremstelle 1)|D_{h⁻¹} = ]0; 5/e], W_{h⁻¹} = [1; ∞[",
    voraussetzungen="Umkehrbarkeit als Injektivität am Graphen|strenge Monotonie ohne Extremstelle im Inneren|Tausch von Definitions- und Wertebereich",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=GW, kontext="ohne", textumfang="mittel",
    gegeben="f wie in a; h auf [1; +∞[ mit h(x) = f(x)",
    gesucht="Begründung: f nicht umkehrbar, h umkehrbar; Definitions- und Wertebereich von h⁻¹",
    verfahren="waagerechte Gerade schneidet G zweimal; Monotonie von h; Bereiche tauschen",
    schritte="4", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="2025MerhoehtBAnalysisWTR2-1a",
    ergebnis="Abbildung 1 ist zu entnehmen, dass es zwei x-Werte gibt, für die f(x) = 1 gilt, daher ist f nicht umkehrbar; h ist umkehrbar, da f nur die Extremstelle 1 besitzt und somit im Intervall [1; +∞[ streng monoton ist; Definitionsbereich der Umkehrfunktion von h: ]0; 5/e]; Wertebereich: [1; +∞[ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Definitionsbereich [0; 5/e] (0 wird nicht angenommen, Grenzwert)",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K6 II. AB amtlich: II. Amtlich.")

row("2025MerhoehtBAnalysisWTR2", "d", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Flächenterm einer an y = x gespiegelten Figur über Rechteck und Integral begründen", typ_neben="",
    stichwoerter="(5 − ln 5) · ln 5: Rechteck von x = ln 5 bis 5 mit Höhe ln 5 (unter der Spitze S)|∫_{ln 5}^5 f: Fläche unter G zwischen ln 5 und 5|Differenz = Fläche zwischen G und y = ln 5, gespiegelt an y = x die rechte Hälfte der Figur|mal 2 wegen Symmetrie zu x = ln 5",
    voraussetzungen="Spiegelung an y = x erhält Flächeninhalte|Rechteck minus Integral als Fläche zwischen Graph und waagerechter Gerade|Symmetrie der Figur",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GW, kontext="Wappen", textumfang="lang",
    gegeben="Figur aus Abbildung 2: Rand y = 5, H1 (G für x ∈ [ln 5; 5] an y = x gespiegelt), H2 (H1 an x = ln 5 gespiegelt), S(ln 5 | ln 5); Term 2 · ((5 − ln 5) · ln 5 − ∫_{ln 5}^5 f(x) dx)",
    gesucht="Begründung, dass der Term den Flächeninhalt der Figur liefert",
    verfahren="Rechteck und Integral am Graphen von f deuten, Differenz als halbe Figur über die Spiegelung erkennen",
    schritte="4", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="(5 − ln 5) · ln 5 ist der Flächeninhalt eines Rechtecks der Länge 5 − ln 5 und der Breite ln 5; ∫_{ln 5}^5 f(x) dx entspricht dem Inhalt des Flächenstücks, das G und die Geraden x = ln 5 und x = 5 mit der x-Achse einschließen; die Differenz ist der Inhalt der schraffierten Fläche, die durch Spiegeln an y = x in eine Hälfte der Figur übergeht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="ln 5 als Nullstelle statt als f-Wert 5 an der Spiegelstelle deuten (f(ln 5) = 5 ln 5/5 = ln 5)",
    bemerkung="Traegerbindung: Kontext (die Figur mit H1, H2 und S ist nur über Abbildung 2 und die Spiegelvorschriften der Trägeraufgabe fassbar). Standardbezug: K1 III, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Spiegelung an y = x und an x = ln 5 erkennen und für die Flächengleichheit ausnutzen.")

row("2025MerhoehtBAnalysisWTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Flächeninhalt aus einem vorgegebenen Term mit Stammfunktion berechnen", typ_neben="",
    stichwoerter="2 · ((5 − ln 5) · ln 5 − (F(5) − F(ln 5))) ≈ 6,1",
    voraussetzungen="Hauptsatz mit gegebener Stammfunktion|Term auswerten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Wappen", textumfang="kurz",
    gegeben="F(x) = −5(x + 1) e^−x Stammfunktion von f; Term aus d",
    gesucht="Flächeninhalt der Figur auf Zehntel",
    verfahren="Integral über F, einsetzen",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="2025MerhoehtBAnalysisWTR2-1d",
    ergebnis="2 · ((5 − ln 5) · ln 5 − (F(5) − F(ln 5))) ≈ 6,1 (amtlich)",
    zwischenergebnis="6,099", niveau_geschaetzt="I",
    fehlerquelle="F(ln 5) mit e^{−ln 5} = 1/5 falsch auswerten",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis WTR 2, Aufgabe 2: Schar g_k = −5x e^{−kx}
GK = "Koordinatensystem x von −5 bis 5, y von −5 bis 5; vier Graphen: I (punktiert) mit Hochpunkt bei etwa (−2 | 3,7) links, II (gestrichelt) mit Hochpunkt bei etwa (−1 | 1,8), III (durchgezogen) mit Tiefpunkt (1 | −1,84), IV (strichpunktiert) mit Tiefpunkt bei etwa (2 | −3,7)"
row("2025MerhoehtBAnalysisWTR2", "a", innen="2", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter den Graphen über Spiegelung und Extremstelle zuordnen", typ_neben="",
    stichwoerter="Spiegelung von G an der x-Achse: −f(x) = −5x e^−x = g_1(x), k = 1|Tiefpunkt (1 | −5/e)|Extremstelle 1/k: I k = −0,5, II k = −1, IV k = 0,5",
    voraussetzungen="Spiegelung an der x-Achse als −f|Extremstelle 1/k aus der Ableitung|Vorzeichen von k und Lage",
    format="Kurzantwort", operator="Geben Sie an|Ordnen Sie zu", antwort="Zahl",
    material="Koordinatensystem", skizze=GK, kontext="ohne", textumfang="mittel",
    gegeben="g_k(x) = −5x · e^{−kx}, k ≠ 0; Abbildung 3 mit Graphen zu k = −1, −0,5, 0,5, 1; Graph III entsteht durch Spiegeln von G an der x-Achse",
    gesucht="k zu Graph III, Tiefpunkt von III, Zuordnung der übrigen k",
    verfahren="Spiegelung erkennen, Extremstellen vergleichen",
    schritte="3", zahlenraum="dezimal|Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Graph III: k = 1, Tiefpunkt (1 | −5/e); I: k = −0,5; II: k = −1; IV: k = 0,5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="I und II vertauschen (Extremstelle −2 gehört zu k = −0,5)",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBAnalysisWTR2", "b", innen="2", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Punktsymmetrie zweier Scharkurven zueinander aus einer Identität nachweisen und deuten", typ_neben="",
    stichwoerter="−g_{−k}(x) = −(−5x e^{kx}) = −5 · (−x) · e^{−k(−x)} = g_k(−x)|Graphen von g_k und g_{−k} sind symmetrisch zum Ursprung",
    voraussetzungen="Term mit −x und −k umformen|g(−x) = −h(x) als Punktsymmetrie zweier Graphen zueinander",
    format="Rechnung|Kurzantwort", operator="Zeigen Sie|Interpretieren Sie", antwort="Text",
    material="Koordinatensystem", skizze=GK, kontext="ohne", textumfang="kurz",
    gegeben="Schar g_k wie in a; Gleichung g_k(−x) = −g_{−k}(x)",
    gesucht="Nachweis für alle x und Deutung für die Graphen",
    verfahren="rechte Seite umformen, Symmetrie deuten",
    schritte="2", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="−g_{−k}(x) = −(−5x · e^{−(−k)·x}) = −5 · (−x) · e^{−k·(−x)} = g_k(−x); die Graphen von g_k und g_{−k} sind zueinander symmetrisch bezüglich des Koordinatenursprungs (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Achsensymmetrie statt Punktsymmetrie",
    bemerkung="Standardbezug: K1 III, K4 III, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: Nachrechnen der Identität allein wäre II (Prinzip); die Deutung als Punktsymmetrie zweier verschiedener Graphen zueinander ist zu finden – (b) verkettet.")

# ---- Analysis WTR 3: Schar f_a = −3x² e^{ax}, Photovoltaik
GA3 = "Koordinatensystem x von −12 bis 3, y von −7 bis 0; Graph von f_{0,5} unterhalb der x-Achse, Hochpunkt im Ursprung, Tiefpunkt bei etwa (−4 | −6,5), links gegen 0, rechts steil fallend"
row("2025MerhoehtBAnalysisWTR3", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben", typ_neben="",
    stichwoerter="−48e^−2 = −3 · (−4)² · e^{−4a} ⇔ e^{−4a} = e^−2 ⇔ a = 0,5",
    voraussetzungen="Punktprobe|Exponentenvergleich",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GA3, kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = −3x² · e^{ax}, a ≠ 0; Graph durch (−4 | −48e^−2)",
    gesucht="zugehöriger Wert von a",
    verfahren="Punkt einsetzen, Exponenten vergleichen",
    schritte="2", zahlenraum="dezimal|Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="−48e^−2 = −3 · (−4)² · e^{−4a} ⇔ a = 0,5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen im Exponenten (a = −0,5)",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2025MerhoehtBAnalysisWTR3", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Vorzeichen aller Funktionswerte einer Schar am Term begründen", typ_neben="",
    stichwoerter="x² ≥ 0, e^{ax} > 0 ⇒ −3x² e^{ax} ≤ 0",
    voraussetzungen="Vorzeichen der Faktoren",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = −3x² · e^{ax}",
    gesucht="Begründung, dass f_a für jedes a keine positiven Werte hat",
    verfahren="Faktoren einzeln betrachten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="wegen x² ≥ 0 und e^{ax} > 0 gilt f_a(x) = −3x² · e^{ax} ≤ 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen von a für relevant halten",
    bemerkung="Standardbezug: K1 I, K2 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBAnalysisWTR3", "c", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Hochpunkt im Ursprung über das Vorzeichen begründen und Tiefstelle einer Schar berechnen", typ_neben="",
    stichwoerter="f_a ≤ 0 und f_a(0) = 0 ⇒ Hochpunkt im Ursprung|f_a'(x) = −3x (2 + ax) e^{ax}|f_a' = 0 ⇔ x = 0 ∨ x = −2/a",
    voraussetzungen="Maximum aus der Wertebeschränkung|Produkt- und Kettenregel mit Parameter|Nullstellen der Ableitung",
    format="Begründung|Rechnung", operator="Begründen Sie|Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="G_a hat genau zwei Extrempunkte, einer im Ursprung; Kontrolle x_T = −2/a",
    gesucht="Begründung Hochpunkt im Ursprung und x-Koordinate des Tiefpunkts",
    verfahren="Wertebeschränkung aus b nutzen, f_a' faktorisieren",
    schritte="3", zahlenraum="Bruch|Potenz|negativ", einheiten="", abhaengig_von="2025MerhoehtBAnalysisWTR3-1b",
    ergebnis="da f_a keine positiven Funktionswerte besitzt, liegt im Koordinatenursprung der Hochpunkt; f_a'(x) = −6x · e^{ax} − 3x² · a · e^{ax} = −3x · (2 + a · x) · e^{ax}; f_a'(x) = 0 ⇔ x = 0 ∨ x = −2/a; x-Koordinate des Tiefpunkts −2/a (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Hochpunkt über f'' nachweisen wollen statt über das Vorzeichen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBAnalysisWTR3", "d", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für einen Extrempunkt als Quadratecke bestimmen und Flächeninhalt berechnen", typ_neben="",
    stichwoerter="Quadrat mit zwei Seiten auf den Achsen, Ecke im Ursprung: gegenüberliegende Ecke (−2/a | −2/a)|f_a(−2/a) = −2/a ⇔ −3 · 4/a² · e^−2 = −2/a ⇔ a = 6/e²|Seite 2/a = e²/3, Fläche e⁴/9",
    voraussetzungen="Quadratbedingung: beide Koordinaten gleich|Tiefpunkt (−2/a | f_a(−2/a))|Exponentialgleichung in a|Flächeninhalt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="positiver Wert von a, für den der Tiefpunkt Eckpunkt eines Quadrats mit zwei Seiten auf den Koordinatenachsen ist",
    gesucht="dieser Wert von a und der Flächeninhalt des Quadrats",
    verfahren="Tiefpunkt mit gleichen Koordinaten ansetzen, a bestimmen, Seitenlänge quadrieren",
    schritte="4", zahlenraum="Bruch|Potenz|negativ", einheiten="", abhaengig_von="2025MerhoehtBAnalysisWTR3-1c",
    ergebnis="für den gesuchten Wert ist (−2/a | −2/a) der dem Ursprung gegenüberliegende Eckpunkt; f_a(−2/a) = −2/a ⇔ −3 · 4/a² · e^−2 = −2/a ⇔ a = 6/e²; Flächeninhalt e²/3 · e²/3 = e⁴/9 (amtlich)",
    zwischenergebnis="a ≈ 0,81; Fläche ≈ 6,07", niveau_geschaetzt="III",
    fehlerquelle="Quadratbedingung als |x_T| = |y_T| mit falschem Vorzeichen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Quadrat mit Seiten auf den Achsen in die Bedingung x_T = y_T übersetzen.")

# ---- Analysis WTR 3, Aufgabe 2: Photovoltaik k(x), h(x)
PV = "Koordinatensystem x von 0 bis 20 (Stunden), y von 0 bis 3,5 (kW); Graph von k als Sinusbogen von (6 | 0,5) über das Maximum (13 | 3,4) nach (20 | 0,5); Graph von h gestrichelt darüber bei x < 10 und x > 16, dazwischen darunter, Maximum etwa 3,2"
row("2025MerhoehtBAnalysisWTR3", "a", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Zeitpunkt für einen Anteil des Maximalwerts einer Sinusfunktion berechnen", typ_neben="",
    stichwoerter="k(13) = 3,4, 50 %: 1,7|sin(π/12 (x − 7)) = 7/24|π/12 (x − 7) ≈ 0,296 ⇒ x ≈ 8,13|8:08 Uhr",
    voraussetzungen="Maximalwert einsetzen|Sinusgleichung mit arcsin|Dezimalstunden in Minuten",
    format="Rechnung", operator="Ermitteln Sie|Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=PV, kontext="Photovoltaik/Leistung", textumfang="lang",
    gegeben="k(x) = 2,4 · sin(π/12 · (x − 7)) + 1 Leistung in kW, x Stunden seit 0:00 Uhr, 6 ≤ x ≤ 20; Maximum um 13:00 Uhr",
    gesucht="ein Zeitpunkt mit 50 % der Maximalleistung als Uhrzeit in Stunden und Minuten",
    verfahren="k(x) = 0,5 · k(13) lösen, Uhrzeit umrechnen",
    schritte="4", zahlenraum="dezimal|Bruch", einheiten="kW|Stunden", abhaengig_von="",
    ergebnis="0,5 · k(13) = 1,7; k(x) = 1,7 ⇔ sin(π/12 · (x − 7)) = 7/24; damit ist beispielsweise π/12 · (x − 7) ≈ 0,296 und x ≈ 8,13; Uhrzeit 8:08 Uhr (amtlich)",
    zwischenergebnis="zweite Lösung 17:52 Uhr", niveau_geschaetzt="II",
    fehlerquelle="0,13 h als 13 Minuten lesen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBAnalysisWTR3", "b", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Schnittstellen zweier Graphen im Sachzusammenhang ablesen", typ_neben="",
    stichwoerter="Schnittpunkte der Graphen von k und h bei x = 10 und x = 16|10 Uhr und 16 Uhr",
    voraussetzungen="Gleichheit als Schnittpunkt|Ablesen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=PV, kontext="Photovoltaik/Leistung", textumfang="kurz",
    gegeben="Graphen von k (abgegebene Leistung) und h (aufgenommene Leistung) in Abbildung 2",
    gesucht="Zeitpunkte gleicher Leistung, grafisch",
    verfahren="Schnittstellen ablesen",
    schritte="1", zahlenraum="ganz", einheiten="Stunden", abhaengig_von="",
    ergebnis="10 Uhr und 16 Uhr (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Maximum von k statt der Schnittstellen nennen",
    bemerkung="Standardbezug: K3 I, K4 I. AB amtlich: I. Amtlich (Ablesung).")

row("2025MerhoehtBAnalysisWTR3", "c", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Bestimmtes Integral mit vorgegebener Stammfunktion berechnen", typ_neben="",
    stichwoerter="∫_6^20 k = K(20) − K(6) = −144/(5π) (cos(13π/12) − cos(−π/12)) + 14 ≈ 31,7|etwa 32 kWh",
    voraussetzungen="Integral der Leistung als Energie (vorgegeben)|Hauptsatz|Einheit kWh",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Photovoltaik/Leistung", textumfang="lang",
    gegeben="K(x) = −144/(5π) · cos(π/12 · (x − 7)) + x Stammfunktion von k; Integral der Leistung über die Zeit in Stunden gibt die Energie in kWh",
    gesucht="von 6:00 bis 20:00 Uhr abgegebene Energie",
    verfahren="K(20) − K(6)",
    schritte="2", zahlenraum="dezimal|Bruch", einheiten="kWh", abhaengig_von="",
    ergebnis="∫_6^20 k(x) dx = [−144/(5π) · cos(π/12 · (x − 7)) + x]_6^20 = −144/(5π) · (cos(13π/12) − cos(−π/12)) + 14 ≈ 31,7; abgegebene elektrische Energie etwa 32 kWh (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Rechner im Gradmaß",
    bemerkung="Standardbezug: K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B); die Deutung als Energie ist im Text vorgegeben.")

row("2025MerhoehtBAnalysisWTR3", "d", innen="2", seite="3", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Vorzeichen eines Differenzintegrals über Flächenvergleich am Graphen begründen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Flächen A1 (6 bis 10, h über k), A2 (10 bis 16, k über h), A3 (16 bis 20, h über k)|A2 < A1 + A3 nach Augenmaß|∫(k − h) = −A1 + A2 − A3 < 0|Anlage gibt insgesamt weniger Energie ab, als das Haus aufnimmt",
    voraussetzungen="Differenzintegral als vorzeichenbehaftete Flächenbilanz|Flächen am Graphen abschätzen|Integral als Energie",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Interpretieren Sie", antwort="Text",
    material="Koordinatensystem", skizze=PV, kontext="Photovoltaik/Leistung", textumfang="mittel",
    gegeben="Aussage ∫_6^20 (k(x) − h(x)) dx < 0; Graphen von k und h; Integral der Leistung ist die Energie",
    gesucht="Begründung mit Abbildung 2 und Deutung",
    verfahren="drei Flächenstücke zwischen den Graphen vergleichen, Vorzeichen zuordnen, deuten",
    schritte="3", zahlenraum="ganz", einheiten="kWh", abhaengig_von="",
    ergebnis="der Flächeninhalt A2 (k über h zwischen 10 und 16) ist kleiner als die Summe der Flächeninhalte A1 und A3 (h über k davor und danach); damit gilt ∫_6^20 (k(x) − h(x)) dx = −A1 + A2 − A3 < 0; im Zeitraum von 6:00 Uhr bis 20:00 Uhr gibt die Photovoltaikanlage insgesamt weniger elektrische Energie ab als im Haus in diesem Zeitraum insgesamt aufgenommen wird (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur A1 oder nur A3 gegen A2 stellen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 III, K4 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (e) Differenzintegral als Flächenbilanz am Graphen gedeutet, verkettet mit (d) Deutung als Energiebilanz.")

# ---- AG/LA (A1) WTR: Pay-TV, Prisma
PRISMA = "Schrägbild eines geraden Prismas, Grundfläche V-förmiges Siebeneck ABCDEFG in der Ebene x = 1 (A(1 | 1 | 0) und G unten, B(1 | 2 | 4) und F(1 | −2 | 4) oben außen, C und E oben innen, D(1 | 0 | 1) als Knick), Deckfläche gespiegelt in x = −1 mit H(−1 | 1 | 0); symmetrisch zur xz- und zur yz-Ebene"
row("2025MerhoehtBAGLAA1WTR", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Eintrag 0 (Zeile K, Spalte S): niemand wechselt von S zu K|Eintrag 0,8 (P, P): 80 % der Premium-Kunden bleiben",
    voraussetzungen="Zeile = Ziel, Spalte = Herkunft",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Pay-TV/Abonnements", textumfang="lang",
    gegeben="v_{n+1} = M · v_n mit M = ((0,6; 0,1; 0), (0,3; 0,8; 0,5), (0,1; 0,1; 0,5)), Komponenten k, p, s (Kino, Premium, Sport); 3000 Kunden, Wechsel je Quartal",
    gesucht="Bedeutung der Einträge 0 und 0,8",
    verfahren="Positionen deuten",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="der Eintrag 0 bedeutet, dass von einem Quartal zum nächsten kein Kunde vom Sport-Abo zum Kino-Abo wechselt; der Eintrag 0,8 bedeutet, dass 80 % der Kunden mit einem Premium-Abo bei diesem bleiben (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="0 als Wechsel von K zu S lesen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A). Aufgabengruppe A1, außerhalb der Geltung.")

row("2025MerhoehtBAGLAA1WTR", "b", innen="1", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Stationäre Verteilung mit vorgegebener Gesamtzahl berechnen und einen Anteil beurteilen", typ_neben="",
    stichwoerter="M · (k; p; 3000 − k − p) = (k; p; 3000 − k − p)|I: −0,4k + 0,1p = 0, II: 0,4k + 1,4p = 3000|1,5p = 3000 ⇒ p = 2000 > 1800|mehr als 60 %",
    voraussetzungen="Fixvektor mit Summenbedingung|lineares Gleichungssystem|Anteil vergleichen",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Pay-TV/Abonnements", textumfang="mittel",
    gegeben="M wie in a; 3000 Kunden; Verteilung, die sich nicht mehr ändert",
    gesucht="ob dabei mehr als 60 % der Kunden P haben",
    verfahren="Fixvektorgleichung mit s = 3000 − k − p, zwei Gleichungen lösen",
    schritte="4", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="M · (k; p; 3000 − k − p) = (k; p; 3000 − k − p) liefert I: 0,6k + 0,1p = k, II: 0,3k + 0,8p + 1500 − 0,5k − 0,5p = p; aus I folgt −0,4k + 0,1p = 0 und aus II 0,4k + 1,4p = 3000; Addition: 1,5p = 3000, p = 2000 > 1800; es haben mehr als 60 % der Kunden die Abo-Variante P (amtlich)",
    zwischenergebnis="k = 500, s = 500", niveau_geschaetzt="II",
    fehlerquelle="Fixvektor nur bis auf Vielfache bestimmen und die 3000 vergessen",
    bemerkung="Standardbezug: K1 I, K2 II, K3 II, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2025MerhoehtBAGLAA1WTR", "c", innen="1", seite="2", punkte="6", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Größtmögliche Anzahl im Vorquartal über die inverse Matrix und Nichtnegativität bestimmen", typ_neben="",
    stichwoerter="Verteilung (x; x; 3000 − 2x), 0 ≤ x ≤ 1500|Vorquartal M⁻¹ · v = (x + 750; 4x − 4500; 6750 − 5x)|alle Komponenten in [0; 3000]: x ≤ 1350|K im Vorquartal x + 750 ≤ 2100",
    voraussetzungen="Gleichheit zweier Komponenten als Ansatz mit einer Unbekannten|inverse Matrix als Rückrechnung|Nichtnegativität und Obergrenze aller Komponenten|Maximum eines linearen Terms",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Pay-TV/Abonnements", textumfang="lang",
    gegeben="1/4 · ((7; −1; 1), (−2; 6; −6), (−1; −1; 9)) · M = E; zu Quartalsbeginn gleich viele Kunden mit K wie mit P",
    gesucht="größtmögliche Anzahl der K-Kunden im vorausgegangenen Quartal",
    verfahren="Verteilung parametrisieren, mit der Inversen zurückrechnen, Zulässigkeit als Ungleichungen, Maximum",
    schritte="5", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="Kundenverteilung im betrachteten Quartal (x; x; 3000 − 2x) mit 0 ≤ x ≤ 1500; im vorausgegangenen Quartal 1/4 · ((7; −1; 1), (−2; 6; −6), (−1; −1; 9)) · (x; x; 3000 − 2x) = (x + 750; 4x − 4500; 6750 − 5x); x + 750 ≤ 3000 ∧ 4x − 4500 ≤ 3000 ∧ 0 ≤ 6750 − 5x ⇔ x ≤ 1350; somit hatten höchstens 2100 Kunden die Abo-Variante K (amtlich)",
    zwischenergebnis="auch 4x − 4500 ≥ 0 ⇒ x ≥ 1125", niveau_geschaetzt="III",
    fehlerquelle="x = 1500 als Maximum nehmen (dann s im Vorquartal negativ)",
    bemerkung="Standardbezug: K1 II, K2 III, K3 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Bedingung „gleich viele K wie P“ und Zulässigkeit des Vorquartals in Ungleichungen übersetzen, verkettet mit der Rückrechnung über die Inverse. Aufgabengruppe A1, außerhalb der Geltung.")

row("2025MerhoehtBAGLAA1WTR", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Koordinaten gespiegelter Eckpunkte aus den Symmetrieebenen eines Körpers angeben", typ_neben="",
    stichwoerter="F Spiegelbild von B an der xz-Ebene: (1 | −2 | 4)|H Spiegelbild von A an der yz-Ebene: (−1 | 1 | 0)",
    voraussetzungen="Spiegelung an der xz-Ebene kehrt y um, an der yz-Ebene x",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Körper", skizze=PRISMA, kontext="Skulptur/Prisma", textumfang="mittel",
    gegeben="gerades Prisma, Grundfläche Siebeneck ABCDEFG, H weiterer Eckpunkt; A(1 | 1 | 0), B(1 | 2 | 4), D(1 | 0 | 1); symmetrisch zur xz- und zur yz-Ebene",
    gesucht="Koordinaten von F und H",
    verfahren="B und A an den Symmetrieebenen spiegeln (Lage aus der Abbildung)",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="F(1 | −2 | 4), H(−1 | 1 | 0) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="F und H an der falschen Ebene spiegeln",
    bemerkung="Standardbezug: K2 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2025MerhoehtBAGLAA1WTR", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Fehlende Koordinate eines Punktes aus der Parallelität zweier Kanten bestimmen", typ_neben="",
    stichwoerter="C(1 | y | 4)|AB = (0; 1; 4), DC = (0; y; 3)|DC = k · AB ⇒ k = 3/4, y = 3/4",
    voraussetzungen="Parallelität als Kollinearität|Komponentenvergleich",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=PRISMA, kontext="Skulptur/Prisma", textumfang="mittel",
    gegeben="C mit x = 1 und z = 4; Kanten AB und DC parallel; A(1 | 1 | 0), B(1 | 2 | 4), D(1 | 0 | 1)",
    gesucht="y-Koordinate von C",
    verfahren="DC als Vielfaches von AB ansetzen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="C(1 | y | 4); AB = (0; 1; 4), DC = (0; y; 3); (0; y; 3) = k · (0; 1; 4) ⇔ k = 3/4 ∧ y = 3/4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="k aus der y-Komponente statt aus der z-Komponente bestimmen (zirkulär)",
    bemerkung="Standardbezug: K2 II, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA (A2) WTR: Pyramide über Drachenviereck (wie 2025-ga-B AG/LA A2 WTR 2), Ebenenschar
DRACHE = "Schrägbild: Pyramide ABCDS, Grundfläche Drachenviereck in der xy-Ebene mit A im Ursprung, B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), Spitze S(0 | 0 | 6) senkrecht über A; Erwartungshorizont d: Dreieck BDQ_2 mit Q_2(0 | 2 | 4) eingezeichnet"
row("2025MerhoehtBAGLAA2WTR", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Kürzeste und längste Kante und Volumen einer Pyramide über einem Drachenviereck berechnen", typ_neben="",
    stichwoerter="|AB| = |(2; 2; 0)| = 2√2 kürzeste|Drachenfläche 1/2 · 6 · 4 = 12|V = 1/3 · 12 · 6 = 24",
    voraussetzungen="Kantenlängen als Beträge|Drachenfläche aus den Diagonalen|Pyramidenvolumen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="kurz",
    gegeben="A(0 | 0 | 0), B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), S(0 | 0 | 6); ABCD Drachenviereck",
    gesucht="Länge der kürzesten Kante und Volumen",
    verfahren="Kantenlängen vergleichen, Grundfläche über Diagonalen, Volumen",
    schritte="3", zahlenraum="Wurzel|ganz", einheiten="", abhaengig_von="",
    ergebnis="kleinste Kantenlänge |AB| = |(2; 2; 0)| = 2√2; Grundfläche 1/2 · 6 · 4 = 12; Volumen 1/3 · 12 · 6 = 24 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Drachenfläche ohne den Faktor 1/2",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-B, dort zusätzlich die längste Kante); Trägeraufgabe wortgleich mit 2025-ga-B AG/LA A2 WTR 2 in a bis c, hier ohne die längste Kante.")

row("2025MerhoehtBAGLAA2WTR", "b", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Normalenvektor aus der Orthogonalität zu Vielfachen der Spannvektoren begründen", typ_neben="",
    stichwoerter="(−1; 2; 0) kollinear zu BC = (−2; 4; 0)|(−1; −1; 3) kollinear zu BS = (−2; −2; 6)|n senkrecht zu beiden Spannvektoren ⇒ Normalenvektor",
    voraussetzungen="Kollinearität erkennen|Normalenvektor als Vektor senkrecht zu zwei aufspannenden Vektoren",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="mittel",
    gegeben="Vektoren n ≠ 0 mit n · (−1; 2; 0) = 0 und n · (−1; −1; 3) = 0; Ebene E durch B, C, S",
    gesucht="Begründung, dass ein solcher Vektor Normalenvektor von E ist",
    verfahren="die beiden Vektoren als Vielfache von BC und BS erkennen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(−1; 2; 0) ist kollinear zu BC, (−1; −1; 3) ist kollinear zu BS; da BC und BS die Ebene E aufspannen und n zu diesen Vektoren senkrecht steht, ist n ein Normalenvektor von E (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="n konkret ausrechnen statt zu begründen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBAGLAA2WTR", "c", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="n = (2; 1; 1), n_xy = (0; 0; 1)|cos α = 1/√6|α ≈ 65,9°",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="kurz",
    gegeben="E: 2x + y + z = 6",
    gesucht="Winkel zwischen E und der xy-Ebene",
    verfahren="Winkelformel mit Normalenvektoren",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="cos α = ((2; 1; 1) · (0; 0; 1)) / (|(2; 1; 1)| · |(0; 0; 1)|) = 1/√6 liefert α ≈ 65,9° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Betrag von (2; 1; 1) als √5",
    bemerkung="Standardbezug: K2 I, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet; wortgleich mit 2025-ga-B AG/LA A2 WTR 2, c.")

row("2025MerhoehtBAGLAA2WTR", "d", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharebene für einen Parameterwert angeben und Schnittfigur mit der Pyramide einzeichnen", typ_neben="",
    stichwoerter="F_2: 2y + 0 · z = 4 ⇔ y = 2|Ebene durch B und D parallel zur xz-Ebene|Q_2 auf SC mit y = 2: (0 | 2 | 4)|Dreieck BDQ_2 einzeichnen",
    voraussetzungen="Parameter einsetzen|Ebene y = 2 im Schrägbild|Schnittpunkt mit der Kante SC",
    format="Kurzantwort|Zeichnen", operator="Geben Sie an|Zeichnen Sie ein", antwort="Term",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="mittel",
    gegeben="Schar F_k: k · y + (k − 2) · z = 2k, k ∈ ]0; 3[; jede F_k schneidet die Pyramide im Dreieck BDQ_k mit Q_k auf SC",
    gesucht="Gleichung von F_2 und Schnittfigur in der Abbildung",
    verfahren="k = 2 einsetzen, Q_2 auf SC bestimmen, Dreieck zeichnen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Gleichung von F_2: y = 2; Schnittfigur Dreieck BDQ_2 mit Q_2(0 | 2 | 4) eingezeichnet (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Q_2 auf der Kante AS statt SC suchen",
    bemerkung="Standardbezug: K1 II, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Q_2 = S + 1/3 (C − S)).")

row("2025MerhoehtBAGLAA2WTR", "e", innen="1", seite="2", punkte="6", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharparameter für den minimalen Flächeninhalt eines Schnittdreiecks über die Orthogonalität zur Kante ermitteln", typ_neben="",
    stichwoerter="Grundseite BD fest, Höhe |MQ_k| mit M Mittelpunkt von BD|minimal, wenn MQ_k ⊥ SC, dann F_k ⊥ SC|Normalenvektor (0; k; k − 2) = λ · (0; 6; −6)|k = 6λ, k − 2 = −6λ ⇒ k = 1",
    voraussetzungen="Dreiecksfläche mit fester Grundseite über die Höhe|kürzester Abstand als Lot|Ebene senkrecht zur Kante: Normalenvektor kollinear zum Richtungsvektor",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="kurz",
    gegeben="Schar F_k wie in d; Dreiecke BDQ_k; es gibt k mit minimalem Flächeninhalt",
    gesucht="dieser Wert von k",
    verfahren="Minimum der Höhe als Lot von M auf SC, Orthogonalität der Ebene zur Kante, Kollinearität lösen",
    schritte="4", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Flächeninhalt des Dreiecks BDQ_k ist minimal, wenn |MQ_k| am kleinsten ist, M Mittelpunkt von BD; die zugehörige Ebene F_k steht dann senkrecht zur Kante SC; (0; k; k − 2) = λ · (0; 6; −6) ⇒ k = 6λ ∧ k − 2 = −6λ ⇒ k − 2 = −k ⇒ k = 1 (amtlich)",
    zwischenergebnis="Q_1(0 | 4 | 2), Kontrolle über die Ableitung von |MQ_t|² bestätigt", niveau_geschaetzt="III",
    fehlerquelle="Flächeninhalt als Funktion von k aufstellen und ableiten (lang, fehleranfällig)",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Minimalität in die Orthogonalität der Ebene zur Kante übersetzen (Höhe als Lot), verkettet mit der Kollinearität.")

# ---- Stochastik WTR 1: Naturkostkette (Aufgabe 1 teilt a mit 2025-ga-B Stochastik WTR 3), Füllmenge
row("2025MerhoehtBStochastikWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="J: jünger als 50 (0,72), G: Großstadt (0,75), P(J und nicht G) = 0,18|Felder 0,54, 0,21, 0,18, 0,07",
    voraussetzungen="Ränder und Differenzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Naturkostkette/Kundschaft", textumfang="mittel",
    gegeben="72 % jünger als 50 Jahre; 18 % jünger als 50 und nicht in einer Großstadt; 75 % in einer Großstadt",
    gesucht="vollständige Vierfeldertafel",
    verfahren="Ränder eintragen, Felder als Differenzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="G und J 0,54, G und nicht J 0,21, nicht G und J 0,18, nicht G und nicht J 0,07; Ränder 0,75 / 0,25 und 0,72 / 0,28 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="0,18 als P(nicht G) lesen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet; wortgleich mit 2025-ga-B Stochastik WTR 3, a.")

row("2025MerhoehtBStochastikWTR1", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen", typ_neben="",
    stichwoerter="P(G und nicht J) = 0,21|entweder G oder nicht J: 0,54 + 0,07 = 0,61|0,21 ist deutlich weniger als die Hälfte von 0,61 (0,305)|Aussage falsch",
    voraussetzungen="Schnittfeld ablesen|ausschließendes Oder als zwei Felder|Verhältnis prüfen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Tabelle", skizze="Vierfeldertafel aus a", kontext="Naturkostkette/Kundschaft", textumfang="lang",
    gegeben="Vierfeldertafel aus a; Aussage: P(G und nicht J) ist etwa halb so groß wie P(entweder G oder nicht J)",
    gesucht="Beurteilung",
    verfahren="beide Wahrscheinlichkeiten aus der Tafel, Verhältnis",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="2025MerhoehtBStochastikWTR1-1a",
    ergebnis="die Aussage ist falsch, da 0,54 + 0,07 = 0,61 deutlich größer ist als 2 · 0,21 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="einschließendes Oder (0,82) rechnen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-B, dort Vergleich mit 60 %).")

row("2025MerhoehtBStochastikWTR1", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="weniger als drei Viertel von 160: X ≤ 119|P(X ≤ 119) ≈ 0,46 (n = 160, p = 0,75)",
    voraussetzungen="Anteil in Anzahl umrechnen|„weniger als“ als X ≤ 119",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Naturkostkette/Kundschaft", textumfang="kurz",
    gegeben="160 Personen; Anzahl in Großstadt binomialverteilt mit p = 0,75",
    gesucht="P(weniger als drei Viertel in einer Großstadt)",
    verfahren="P(X ≤ 119) am Rechner",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="X Anzahl der Personen, die in einer Großstadt wohnen; P(X ≤ 119) ≈ 0,46 (n = 160, p = 0,75) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≤ 120) ≈ 0,54",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2025MerhoehtBStochastikWTR1", "a", innen="2", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Parameter aus der Dichtefunktion ablesen und Bedingungen an Wahrscheinlichkeiten der Normalverteilung prüfen", typ_neben="",
    stichwoerter="φ mit μ = 250, σ = 2|Bedingung I: μ = 250 ≥ 250 erfüllt|II: P(Y ≤ 245,5) ≈ 0,012 ≤ 0,06|III: P(Y ≤ 241) ≈ 0,000003 ≤ 0,002",
    voraussetzungen="μ und σ aus der Dichte|Minusabweichung 4,5 g als Grenzen 245,5 und 241|Normalverteilung am Rechner",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Naturkostkette/Füllmenge", textumfang="lang",
    gegeben="Füllmenge in g normalverteilt mit φ(x) = 1/(2√(2π)) · e^{−1/2 ((x − 250)/2)²}; Minusabweichung 4,5 g; Bedingungen: I Erwartungswert ≥ 250, II P(Y ≤ 245,5) ≤ 6 %, III P(Y ≤ 241) ≤ 0,2 %",
    gesucht="ob jede der drei Bedingungen erfüllt ist",
    verfahren="Parameter ablesen, zwei Wahrscheinlichkeiten berechnen",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="g", abhaengig_von="",
    ergebnis="Y tatsächliche Füllmenge in Gramm; μ = 250, damit ist Bedingung I erfüllt; σ = 2; wegen P(Y ≤ 245,5) ≈ 0,012 < 0,06 ist Bedingung II und wegen P(Y ≤ 241) ≈ 0,000003 < 0,002 Bedingung III erfüllt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="σ = 4 aus dem Nenner 2 im Vorfaktor lesen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBStochastikWTR1", "b", innen="2", seite="2", punkte="6", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Implikation zweier Wahrscheinlichkeitsbedingungen der Normalverteilung über eine Schranke für σ begründen", typ_neben="",
    stichwoerter="P(Z < 245,5) < 0,06 ⇒ σ < 3 (systematisches Probieren, σ = 3 gibt 0,067)|für σ = 3: P(Z < 241) ≈ 0,00135 (3σ-Regel)|kleineres σ ⇒ kleinere Wahrscheinlichkeit ⇒ P(Z < 241) < 0,00135 < 0,002",
    voraussetzungen="Monotonie der Wahrscheinlichkeit in σ|Schranke für σ aus Bedingung II|3σ-Regel oder Rechner",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Naturkostkette/Füllmenge", textumfang="mittel",
    gegeben="andere Anlage: Füllmenge normalverteilt mit μ = 250 und unbekanntem σ; Aussage: erfüllt sie Bedingung II (P(Z ≤ 245,5) ≤ 6 %), so auch Bedingung III (P(Z ≤ 241) ≤ 0,2 %)",
    gesucht="Begründung, dass die Aussage richtig ist",
    verfahren="aus II eine Schranke für σ gewinnen, mit ihr III prüfen",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="g", abhaengig_von="",
    ergebnis="Z tatsächliche Füllmenge in Gramm, normalverteilt mit μ = 250 und σ; aus P(Z < 245,5) < 0,06 erhält man durch systematisches Probieren σ < 3; für σ = 3 beträgt P(Z ≤ 241) etwa 0,00135; P(Z < 241) < 0,00135 < 0,002 (amtlich)",
    zwischenergebnis="σ = 3: P(Z < 245,5) ≈ 0,067", niveau_geschaetzt="III",
    fehlerquelle="Monotonie in σ nicht benennen (nur den Fall σ = 3 rechnen)",
    bemerkung="Standardbezug: K1 III, K2 II, K3 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Bedingung II in eine Schranke für σ übersetzen, verkettet mit der Monotonie in σ.")

# ---- Stochastik WTR 2: Radausflügler, Fahrkarten, Signifikanztest
BAUMF = "Baumdiagramm: A (80 %, Buchung spätestens am Vortag) / nicht A (20 %), darunter B (genutzt) 90 % bzw. 95 % und nicht B 10 % bzw. 5 %"
row("2025MerhoehtBStochastikWTR2", "a", innen="1", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X ~ B(300; 0,14), P(X = 36) ≈ 4 %",
    voraussetzungen="Einzelwahrscheinlichkeit am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Naturpark/Radausflügler", textumfang="kurz",
    gegeben="14 % Radausflügler, Anzahl binomialverteilt; Stichprobe 300",
    gesucht="P(genau 36 Radausflügler)",
    verfahren="P(X = 36) am Rechner",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="X Anzahl der Radausflügler; P(X = 36) ≈ 4 % (n = 300, p = 0,14) (amtlich)",
    zwischenergebnis="4,2 %", niveau_geschaetzt="I",
    fehlerquelle="kumulierte statt Einzelwahrscheinlichkeit",
    bemerkung="Standardbezug: K3 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBStochastikWTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen", typ_neben="",
    stichwoerter="μ = 300 · 0,14 = 42|mindestens 10 % größer: X ≥ 46,2, also X ≥ 47|P(X ≥ 47) ≈ 22 %",
    voraussetzungen="Erwartungswert n · p|Schranke aufrunden|Gegenereignis am Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Naturpark/Radausflügler", textumfang="kurz",
    gegeben="X wie in a",
    gesucht="P(Anzahl um mindestens 10 % größer als der Erwartungswert)",
    verfahren="μ berechnen, 1,1μ aufrunden, P(X ≥ 47)",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="μ = 300 · 0,14 = 42; P(X ≥ 47) ≈ 22 % (n = 300, p = 0,14) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="X ≥ 46 rechnen (46 < 46,2)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtBStochastikWTR2", "a", innen="2", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="A: spätestens am Vortag gebucht (80 %), B: genutzt|P(B | A) = 90 %, P(B | nicht A) = 95 %",
    voraussetzungen="zweistufiges Baumdiagramm|Gegenwahrscheinlichkeiten",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Naturpark/Shuttlebus", textumfang="mittel",
    gegeben="80 % der Fahrkarten spätestens am Vortag gebucht, davon 90 % genutzt; von den am Tag gebuchten 95 % genutzt",
    gesucht="beschriftetes Baumdiagramm",
    verfahren="erste Stufe Buchungszeitpunkt, zweite Stufe Nutzung",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Baumdiagramm mit A (80 %), nicht A (20 %); B | A 90 %, nicht B | A 10 %; B | nicht A 95 %, nicht B | nicht A 5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Stufen vertauschen",
    bemerkung="Standardbezug: K2 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A).")

row("2025MerhoehtBStochastikWTR2", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen", typ_neben="",
    stichwoerter="P(A | nicht B) = 0,8 · 0,1 / P(nicht B) = 0,08/P(nicht B)|P(nicht A | nicht B) = 0,2 · 0,05 / P(nicht B) = 0,01/P(nicht B)|Verhältnis 8, Aussage richtig",
    voraussetzungen="bedingte Wahrscheinlichkeit als Pfad durch Gesamtwahrscheinlichkeit|gemeinsamer Nenner kürzt sich",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Diagramm", skizze=BAUMF, kontext="Naturpark/Shuttlebus", textumfang="mittel",
    gegeben="Baumdiagramm aus a; nicht genutzte Fahrkarte; Aussage: P(Vortag | nicht genutzt) ist achtmal so groß wie P(am Tag | nicht genutzt)",
    gesucht="Beurteilung",
    verfahren="beide bedingten Wahrscheinlichkeiten als Brüche mit gleichem Nenner",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="2025MerhoehtBStochastikWTR2-2a",
    ergebnis="P(A | nicht B) = 0,8 · 0,1 / P(nicht B) = 0,08 / P(nicht B); P(nicht A | nicht B) = 0,2 · 0,05 / P(nicht B) = 0,01 / P(nicht B); die Aussage ist richtig (amtlich)",
    zwischenergebnis="P(nicht B) = 0,09", niveau_geschaetzt="II",
    fehlerquelle="unbedingte Pfade 0,08 und 0,01 vergleichen und die Bedingung übersehen (Ergebnis gleich, Begründung unvollständig)",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2025MerhoehtBStochastikWTR2", "c", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel eines rechtsseitigen Signifikanztests bestimmen", typ_neben="",
    stichwoerter="H0: p ≤ 0,14, n = 500, α = 8 %|Y ~ B(500; 0,14): P(Y ≥ 81) ≈ 9,0 %, P(Y ≥ 82) ≈ 7,1 %|Ablehnung bei mindestens 82",
    voraussetzungen="rechtsseitiger Test|kleinstes k mit P(Y ≥ k) ≤ α am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Naturpark/Signifikanztest", textumfang="lang",
    gegeben="Nullhypothese: Anteil der Radausflügler höchstens 14 %; Signifikanzniveau 8 %; Stichprobe 500; Busse laufen nur bei Ablehnung weiter",
    gesucht="Entscheidungsregel",
    verfahren="kumulierte Wahrscheinlichkeiten von oben an der Grenze vergleichen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Y Anzahl der Radausflügler; P(Y ≥ 81) ≈ 9,0 %, P(Y ≥ 82) ≈ 7,1 % (n = 500, p = 0,14); befinden sich mindestens 82 Radausflügler in der Stichprobe, so wird die Nullhypothese abgelehnt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="linksseitig testen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Entscheidungsregel eines linksseitigen Signifikanztests bestimmen“ (2026-ea-B) getrennt: Richtung.")

row("2025MerhoehtBStochastikWTR2", "d", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben", typ_neben="",
    stichwoerter="n = 200, Ablehnung bei mehr als 35|Fehler 2. Art: H0 nicht abgelehnt (Y ≤ 35), obwohl p > 0,14|P_{0,20}(Y ≤ 35) ≈ 22 %, P_{0,21}(Y ≤ 35) ≈ 13 % ≤ 15 %|p mindestens 21 %|Deutung: Anteil gestiegen, Busse trotzdem eingestellt",
    voraussetzungen="Fehler zweiter Art als Annahmebereich unter der Alternative|Anteil auf ganze Prozent probieren|Deutung über die Entscheidung",
    format="Rechnung|Kurzantwort", operator="Ermitteln Sie|Beschreiben Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Naturpark/Signifikanztest", textumfang="lang",
    gegeben="Test mit n = 200; Ablehnung bei mehr als 35 Radausflüglern; Fehler zweiter Art höchstens 15 %; Busse laufen nur bei Ablehnung weiter",
    gesucht="Mindestanteil auf ganze Prozent und Bedeutung des Fehlers zweiter Art",
    verfahren="P_p(Y ≤ 35) für p in ganzen Prozent, kleinstes p mit ≤ 15 %; deuten",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(Y ≤ 35) ≈ 22 % für p = 0,20 und ≈ 13 % für p = 0,21 (n = 200); der tatsächliche Anteil müsste mindestens 21 % betragen; obwohl der Anteil der Radausflügler auf über 14 % gestiegen ist, entscheidet man sich aufgrund des Testergebnisses dafür, den Betrieb der Shuttlebusse einzustellen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Fehler zweiter Art als P(Y > 35) unter p = 0,14 rechnen (das ist der Fehler erster Art)",
    bemerkung="Standardbezug: K1 II, K2 III, K3 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Fehler zweiter Art als Annahme unter der Alternative deuten, verkettet mit der Suche nach dem Mindestanteil und der Sachdeutung der Entscheidung.")

# ---- Stochastik WTR 3: Aufgabe 1 Dublette von WTR 2 (keine Zeile); Aufgabe 2 a, b wortgleich mit WTR 2, c, d Konfidenzintervalle
KONFG = "Koordinatensystem p von 0 bis 0,2, y von 0 bis 0,2; zwei fast gerade Kurven: g2 (gestrichelt) über der Winkelhalbierenden, g1 (durchgezogen) darunter, Abstand zur Winkelhalbierenden etwa 0,02 bei p = 0,17; Erwartungshorizont: Waagerechte bei 0,17 schneidet g2 bei 0,15 und g1 bei 0,19"
row("2025MerhoehtBStochastikWTR3", "a", innen="2", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="A: spätestens am Vortag gebucht (80 %), B: genutzt|P(B | A) = 90 %, P(B | nicht A) = 95 %",
    voraussetzungen="zweistufiges Baumdiagramm|Gegenwahrscheinlichkeiten",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Naturpark/Shuttlebus", textumfang="mittel",
    gegeben="80 % der Fahrkarten spätestens am Vortag gebucht, davon 90 % genutzt; von den am Tag gebuchten 95 % genutzt",
    gesucht="beschriftetes Baumdiagramm",
    verfahren="erste Stufe Buchungszeitpunkt, zweite Stufe Nutzung",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Baumdiagramm mit A (80 %), nicht A (20 %); B | A 90 %, nicht B | A 10 %; B | nicht A 95 %, nicht B | nicht A 5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Stufen vertauschen",
    bemerkung="Standardbezug: K2 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet. Teilaufgabe wortgleich mit Stochastik WTR 2, 2a; Aufgabe 2 ist als Ganzes nicht wortgleich (c, d anders), daher Zeile.")

row("2025MerhoehtBStochastikWTR3", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen", typ_neben="",
    stichwoerter="P(A | nicht B) = 0,08/P(nicht B), P(nicht A | nicht B) = 0,01/P(nicht B)|Verhältnis 8, Aussage richtig",
    voraussetzungen="bedingte Wahrscheinlichkeit als Pfad durch Gesamtwahrscheinlichkeit|gemeinsamer Nenner kürzt sich",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Diagramm", skizze=BAUMF, kontext="Naturpark/Shuttlebus", textumfang="mittel",
    gegeben="Baumdiagramm aus a; nicht genutzte Fahrkarte; Aussage: P(Vortag | nicht genutzt) ist achtmal so groß wie P(am Tag | nicht genutzt)",
    gesucht="Beurteilung",
    verfahren="beide bedingten Wahrscheinlichkeiten als Brüche mit gleichem Nenner",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="2025MerhoehtBStochastikWTR3-2a",
    ergebnis="P(A | nicht B) = 0,8 · 0,1 / P(nicht B) = 0,08 / P(nicht B); P(nicht A | nicht B) = 0,2 · 0,05 / P(nicht B) = 0,01 / P(nicht B); die Aussage ist richtig (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="unbedingte Pfade vergleichen und die Bedingung übersehen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet; wortgleich mit Stochastik WTR 2, 2b.")

row("2025MerhoehtBStochastikWTR3", "c", innen="2", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen", typ_neben="",
    stichwoerter="h = 153/900 = 0,17|Waagerechte y = 0,17 schneidet g2 bei p ≈ 0,15 und g1 bei p ≈ 0,19|Konfidenzintervall [0,15; 0,19]|0,2 nicht enthalten: Vermutung nicht verträglich",
    voraussetzungen="relative Häufigkeit|Konfidenzintervall als Menge der p mit g1(p) ≤ h ≤ g2(p)|Ablesen|Verträglichkeit als Enthaltensein",
    format="Rechnung|Begründung", operator="Ermitteln Sie|Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=KONFG, kontext="Naturpark/Konfidenzintervall", textumfang="lang",
    gegeben="Vermutung p = 20 %; Stichprobe 900 mit 153 Radausflüglern; Graphen von g1(p) = p − 1,64 √(p(1 − p)/900) und g2(p) = p + 1,64 √(p(1 − p)/900); Sicherheitswahrscheinlichkeit 90 %",
    gesucht="Konfidenzintervall grafisch und Beurteilung der Vermutung",
    verfahren="h berechnen, Waagerechte mit beiden Graphen schneiden, 0,2 prüfen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="für das zur Anzahl gehörende Konfidenzintervall ergibt sich näherungsweise [0,15; 0,19]; 0,2 ∉ [0,15; 0,19], d. h. die Vermutung ist mit dem Stichprobenergebnis nicht verträglich (amtlich)",
    zwischenergebnis="rechnerisch [0,150; 0,192]", niveau_geschaetzt="II",
    fehlerquelle="Senkrechte bei p = 0,17 statt Waagerechte bei h = 0,17 (liefert [0,15; 0,19] nur zufällig ähnlich)",
    bemerkung="Standardbezug: K1 I, K2 I, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Thema ersatzweise Hypothesentests (Konfidenzintervalle haben keine Themenzeile).")

row("2025MerhoehtBStochastikWTR3", "d", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Verträglichkeit zweier Annahmen mit demselben Stichprobenanteil über den Stichprobenumfang beurteilen", typ_neben="",
    stichwoerter="Rechnung I: für n ≥ 360 liegt die obere Grenze des Intervalls um p = 0,14 unter 0,17, also 0,14 nicht verträglich|Rechnung II: für n ≤ 478 liegt die untere Grenze um p = 0,20 unter 0,17, also 0,20 verträglich|für 360 ≤ n ≤ 478 gilt beides: Aussage richtig",
    voraussetzungen="Intervallbreite fällt mit n|Grenzgleichung als Schwelle für n|Asymmetrie durch p(1 − p)",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Naturpark/Konfidenzintervall", textumfang="lang",
    gegeben="Stichprobenanteil h = 0,17, Sicherheitswahrscheinlichkeit 90 %; Aussage: obwohl 0,17 in der Mitte zwischen 0,14 und 0,20 liegt, kann p = 0,14 unverträglich und p = 0,20 verträglich sein; Rechnungen I: 0,17 = 0,14 + 1,64 √(0,14 · 0,86/n) ⇒ n ≈ 359,8; II: 0,17 = 0,20 − 1,64 √(0,2 · 0,8/n) ⇒ n ≈ 478,2",
    gesucht="Beurteilung der Aussage mit beiden Rechnungen",
    verfahren="beide Gleichungen als Schwellen für n deuten, Schnittbereich angeben",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="die Aussage ist richtig; aus Rechnung I folgt, dass die untere Grenze des Konfidenzintervalls für n ≥ 360 größer als 0,14 ist, aus Rechnung II, dass die obere Grenze für n ≤ 478 größer als 0,2 ist; somit ist für 360 ≤ n ≤ 478 die Annahme p = 0,14 mit dem Stichprobenergebnis nicht verträglich, die Annahme p = 0,20 hingegen schon (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Richtung der Ungleichungen in n vertauschen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K4 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) zwei Grenzgleichungen als Schwellen für n deuten und zum Schnittbereich verketten. Thema ersatzweise Hypothesentests. Aufgabe 1 dieser Datei ist wortgleich mit Stochastik WTR 2, Aufgabe 1 (Dublette, keine Zeile, Soll 16).")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Einzigen Wendepunkt einer Schar nachweisen und angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Rechnerisch zeigen, dass jeder Graph einer Schar genau einen Wendepunkt hat (f'' = 0 eindeutig, f''' ≠ 0), und seine parameterabhängigen Koordinaten angeben.",
     "2025MerhoehtBAnalysisWTR1-1b"),
    ("Scharparameter aus einer Integralbedingung bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameter einer Schar bestimmen, für den ein bestimmtes Integral einen vorgegebenen Wert hat.",
     "2025MerhoehtBAnalysisWTR1-1c"),
    ("Faktorisierung von f(x) − t(x) nachweisen und weiteren Schnittpunkt von Tangente und Graph begründen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Eine vorgegebene Faktorisierung der Differenz aus Funktion und Tangente durch Termumformung nachweisen und daraus die weiteren gemeinsamen Punkte begründen.",
     "2025MerhoehtBAnalysisWTR1-1d"),
    ("Integralwert: Anzahl der Lösungen einer Integralgleichung über gleitende Streifen am Graphen untersuchen", "Analysis", "Flächeninhalt durch Integration",
     "Grafisch untersuchen, wie viele k eine Gleichung ∫_k^{k+1} f = c erfüllen, indem der Streifen der Breite 1 verschoben und sein Inhalt mit c verglichen wird.",
     "2025MerhoehtBAnalysisWTR1-1e"),
    ("Nullstellen und Werte: Gleichheit zweier Sachgrößen als Bedingung an den Funktionswert übersetzen und Stelle am Graphen ablesen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus der Gleichheit zweier über Faktoren skalierter Funktionswerte den gesuchten Funktionswert berechnen und die zugehörige Stelle am Graphen ablesen.",
     "2025MerhoehtBAnalysisWTR1-2b"),
    ("Gerade senkrecht zu einer gegebenen Tangente durch einen Punkt aufstellen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Gleichung der Geraden durch einen Punkt aufstellen, die senkrecht zu einer gegebenen Tangente verläuft (negativer Kehrwert der Steigung).",
     "2025MerhoehtBAnalysisWTR2-1b"),
    ("Umkehrbarkeit auf einem Intervall begründen und Definitions- und Wertebereich der Umkehrfunktion angeben", "Analysis", "Umkehrfunktion",
     "Begründen, dass eine Funktion auf IR nicht, auf einem Monotonieintervall aber umkehrbar ist, und Definitions- und Wertebereich der Umkehrfunktion angeben.",
     "2025MerhoehtBAnalysisWTR2-1c"),
    ("Integralwert: Flächenterm einer an y = x gespiegelten Figur über Rechteck und Integral begründen", "Analysis", "Flächeninhalt durch Integration",
     "Einen vorgegebenen Term aus Rechteck und Integral als Flächeninhalt einer Figur begründen, deren Rand durch Spiegelung des Graphen an y = x entsteht.",
     "2025MerhoehtBAnalysisWTR2-1d"),
    ("Fläche: Flächeninhalt aus einem vorgegebenen Term mit Stammfunktion berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Einen vorgegebenen Flächenterm mit Integral über eine gegebene Stammfunktion auswerten.",
     "2025MerhoehtBAnalysisWTR2-1e"),
    ("Scharparameter den Graphen über Spiegelung und Extremstelle zuordnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Abgebildete Graphen einer Schar den Parameterwerten zuordnen, indem ein Graph als Spiegelbild eines bekannten erkannt und die Extremstellen verglichen werden.",
     "2025MerhoehtBAnalysisWTR2-2a"),
    ("Punktsymmetrie zweier Scharkurven zueinander aus einer Identität nachweisen und deuten", "Analysis", "Funktionsscharen und Ortskurven",
     "Eine Identität der Form g_k(−x) = −g_{−k}(x) nachrechnen und als Punktsymmetrie der Graphen von g_k und g_{−k} zueinander deuten.",
     "2025MerhoehtBAnalysisWTR2-2b"),
    ("Vorzeichen aller Funktionswerte einer Schar am Term begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Am Funktionsterm begründen, dass eine Schar für jeden Parameter nur Werte eines Vorzeichens annimmt.",
     "2025MerhoehtBAnalysisWTR3-1b"),
    ("Hochpunkt im Ursprung über das Vorzeichen begründen und Tiefstelle einer Schar berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Hochpunkt einer Schar im Ursprung über die Wertebeschränkung begründen und die Tiefstelle in Abhängigkeit vom Parameter aus der Ableitung berechnen.",
     "2025MerhoehtBAnalysisWTR3-1c"),
    ("Scharparameter für einen Extrempunkt als Quadratecke bestimmen und Flächeninhalt berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameter bestimmen, für den ein Extrempunkt gleiche Koordinaten hat (Ecke eines Quadrats mit Seiten auf den Achsen), und den Flächeninhalt des Quadrats berechnen.",
     "2025MerhoehtBAnalysisWTR3-1d"),
    ("Zeitpunkt für einen Anteil des Maximalwerts einer Sinusfunktion berechnen", "Analysis", "Gleichungen lösen",
     "Eine Gleichung k(x) = c mit einer Sinusfunktion rechnerisch lösen, wobei c ein Anteil des Maximalwerts ist, und die Lösung als Uhrzeit angeben.",
     "2025MerhoehtBAnalysisWTR3-2a"),
    ("Nullstellen und Werte: Schnittstellen zweier Graphen im Sachzusammenhang ablesen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Stellen, an denen zwei abgebildete Graphen gleiche Werte haben, ablesen und im Sachzusammenhang angeben.",
     "2025MerhoehtBAnalysisWTR3-2b"),
    ("Integralwert: Vorzeichen eines Differenzintegrals über Flächenvergleich am Graphen begründen und im Sachzusammenhang deuten", "Analysis", "Flächeninhalt durch Integration",
     "Das Vorzeichen von ∫(k − h) über die Flächenstücke zwischen den Graphen begründen und die Aussage im Sachzusammenhang (Bilanz) deuten.",
     "2025MerhoehtBAnalysisWTR3-2d"),
    ("Übergangsprozess: Stationäre Verteilung mit vorgegebener Gesamtzahl berechnen und einen Anteil beurteilen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Die stationäre Verteilung eines Übergangsprozesses bei fester Gesamtzahl über ein Gleichungssystem berechnen und einen Anteil mit einer Schranke vergleichen.",
     "2025MerhoehtBAGLAA1WTR-1b"),
    ("Übergangsprozess: Größtmögliche Anzahl im Vorquartal über die inverse Matrix und Nichtnegativität bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine parametrisierte Verteilung mit der inversen Matrix zurückrechnen und aus der Zulässigkeit aller Komponenten die größtmögliche Anzahl im Vorzustand bestimmen.",
     "2025MerhoehtBAGLAA1WTR-1c"),
    ("Koordinaten gespiegelter Eckpunkte aus den Symmetrieebenen eines Körpers angeben", "Analytische Geometrie", "Spiegelung",
     "Die Koordinaten weiterer Eckpunkte eines Körpers aus den gegebenen Punkten und den Symmetrieebenen (Koordinatenebenen) angeben.",
     "2025MerhoehtBAGLAA1WTR-2a"),
    ("Fehlende Koordinate eines Punktes aus der Parallelität zweier Kanten bestimmen", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Eine unbekannte Koordinate so bestimmen, dass zwei Kantenvektoren kollinear sind.",
     "2025MerhoehtBAGLAA1WTR-2b"),
    ("Normalenvektor aus der Orthogonalität zu Vielfachen der Spannvektoren begründen", "Analytische Geometrie", "Ebenen",
     "Begründen, dass ein Vektor, der zu zwei Vielfachen der Spannvektoren einer Ebene senkrecht ist, Normalenvektor dieser Ebene ist.",
     "2025MerhoehtBAGLAA2WTR-1b"),
    ("Scharebene für einen Parameterwert angeben und Schnittfigur mit der Pyramide einzeichnen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Für einen Parameterwert die Gleichung der Scharebene angeben und die Schnittfigur mit einem Körper in das Schrägbild einzeichnen.",
     "2025MerhoehtBAGLAA2WTR-1d"),
    ("Scharparameter für den minimalen Flächeninhalt eines Schnittdreiecks über die Orthogonalität zur Kante ermitteln", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Den Parameter ermitteln, für den ein Schnittdreieck mit fester Grundseite minimalen Flächeninhalt hat, indem die Höhe als Lot und die Ebene senkrecht zur Kante angesetzt wird.",
     "2025MerhoehtBAGLAA2WTR-1e"),
    ("Parameter aus der Dichtefunktion ablesen und Bedingungen an Wahrscheinlichkeiten der Normalverteilung prüfen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "μ und σ aus dem Term der Dichtefunktion ablesen und mehrere Bedingungen an Erwartungswert und Unterschreitungswahrscheinlichkeiten prüfen.",
     "2025MerhoehtBStochastikWTR1-2a"),
    ("Implikation zweier Wahrscheinlichkeitsbedingungen der Normalverteilung über eine Schranke für σ begründen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Begründen, dass aus einer Unterschreitungsbedingung eine zweite folgt, indem aus der ersten eine Schranke für σ gewonnen und die Monotonie in σ genutzt wird.",
     "2025MerhoehtBStochastikWTR1-2b"),
    ("Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln", "Stochastik", "Binomialverteilung",
     "P(X = k) einer Binomialverteilung mit dem Rechner ermitteln.",
     "2025MerhoehtBStochastikWTR2-1a"),
    ("Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen", "Stochastik", "Binomialverteilung",
     "Den Erwartungswert berechnen, eine relative Abweichung nach oben in eine ganzzahlige Schranke übersetzen und P(X ≥ k) ermitteln.",
     "2025MerhoehtBStochastikWTR2-1b"),
    ("Entscheidungsregel eines rechtsseitigen Signifikanztests bestimmen", "Stochastik", "Hypothesentests",
     "Für eine Nullhypothese p ≤ p0 die Entscheidungsregel bestimmen: kleinstes k mit P(Y ≥ k) ≤ α über kumulierte Binomialwahrscheinlichkeiten.",
     "2025MerhoehtBStochastikWTR2-2c"),
    ("Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben", "Stochastik", "Hypothesentests",
     "Den kleinsten Anteil ermitteln, für den die Wahrscheinlichkeit des Fehlers zweiter Art eine Schranke nicht überschreitet, und den Fehler zweiter Art im Sachzusammenhang beschreiben.",
     "2025MerhoehtBStochastikWTR2-2d"),
    ("Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen", "Stochastik", "Hypothesentests",
     "Aus den Graphen der unteren und oberen Grenzfunktion das Konfidenzintervall zu einem Stichprobenanteil ablesen und prüfen, ob ein vermuteter Anteil darin liegt.",
     "2025MerhoehtBStochastikWTR3-2c"),
    ("Verträglichkeit zweier Annahmen mit demselben Stichprobenanteil über den Stichprobenumfang beurteilen", "Stochastik", "Hypothesentests",
     "Mit zwei Grenzgleichungen begründen, für welche Stichprobenumfänge ein Anteil mit der einen Annahme verträglich und mit der anderen unverträglich ist.",
     "2025MerhoehtBStochastikWTR3-2d"),
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
            je_datei.setdefault(kennung_aus_id(z["id"])[0], []).append(z["teilaufgabe"])
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
