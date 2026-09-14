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
    "stapel": "2026-ea-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2026MerhoehtBAnalysisWTR1": 30,
        "2026MerhoehtBAnalysisWTR2": 30,
        "2026MerhoehtBAnalysisWTR3": 30,
        "2026MerhoehtBAGLAA1WTR": 20,
        "2026MerhoehtBAGLAA2WTR1": 20,
        "2026MerhoehtBAGLAA2WTR2": 20,
        "2026MerhoehtBStochastikWTR1": 20,
        "2026MerhoehtBStochastikWTR2": 20,
        "2026MerhoehtBStochastikWTR3": 8,
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
# Stapel 2026-ea-B, WTR-Zweig. innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Trägerbindung: „Traegerbindung: Kontext“ am Anfang von bemerkung; kein Vermerk heißt frei.
# Standardbezug Teil B: „AB amtlich: …“ ist die Spalte Anforderungsbereich (maßgeblich für die Eichung).
# Stochastik WTR 3, Aufgabe 1 ist wortgleich mit Stochastik WTR 2, Aufgabe 1: keine Zeile, Soll 8 statt 20.

SOLL = {"2026MerhoehtBAnalysisWTR1": 30, "2026MerhoehtBAnalysisWTR2": 30, "2026MerhoehtBAnalysisWTR3": 30,
        "2026MerhoehtBAGLAA1WTR": 20, "2026MerhoehtBAGLAA2WTR1": 20, "2026MerhoehtBAGLAA2WTR2": 20,
        "2026MerhoehtBStochastikWTR1": 20, "2026MerhoehtBStochastikWTR2": 20, "2026MerhoehtBStochastikWTR3": 8}

# ---- Analysis WTR 1, Aufgabe 1: Schar f_a = 1/4 x³ + ax² + ax + 1/4
G0 = "Koordinatensystem mit Gitter, x von −2 bis 2, y von −1 bis 3; Graph G0 von 1/4 x³ + 1/4, monoton steigend durch (−1; 0) und (0; 0,25)"
row("2026MerhoehtBAnalysisWTR1", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt bestimmen und Wendepunkt nachweisen", typ_neben="",
    stichwoerter="1/4 + a + a + 1/4 = −1 ⇔ a = −3/4|f_a'' = 3/2 x + 2a, f''(1) = 3/2 − 3/2 = 0|f''' = 3/2 ≠ 0",
    voraussetzungen="Punktprobe mit Parameter|zweite und dritte Ableitung|Wendepunktkriterium",
    format="Rechnung|Begründung", operator="Berechnen Sie|Zeigen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=G0, kontext="ohne", textumfang="mittel",
    gegeben="f_a(x) = 1/4 x³ + ax² + ax + 1/4 in IR, a ∈ IR; Punkt (1 | −1) auf G_a",
    gesucht="Wert von a und Nachweis, dass (1 | −1) Wendepunkt ist",
    verfahren="a aus f_a(1) = −1, Wendepunkt über f'' = 0 und f''' ≠ 0",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="1/4 + a + a + 1/4 = −1 ⇔ a = −3/4; f_a'(x) = 3/4 x² + 2ax + a, f_a''(x) = 3/2 x + 2a, f_a'''(x) = 3/2; f''_{−3/4}(1) = 0, f'''_{−3/4}(1) ≠ 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur f'' = 0 prüfen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Verkettung von Reproduktionen, in Teil B als I geschätzt (Befund 2026-ga-B).")

row("2026MerhoehtBAnalysisWTR1", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gemeinsame Punkte aller Graphen einer Schar bestimmen", typ_neben="",
    stichwoerter="f_a(x) = f_b(x) ⇔ (a − b)(x² + x) = 0|x = −1 oder x = 0|f_a(−1) = 0, f_a(0) = 1/4 für alle a",
    voraussetzungen="zwei Scharfunktionen gleichsetzen|Parameter herauskürzen|Punkte parameterunabhängig",
    format="Rechnung", operator="Zeigen Sie|Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a wie in a",
    gesucht="Nachweis, dass genau zwei Punkte auf allen Graphen liegen, und ihre Koordinaten",
    verfahren="f_0 = f_1 lösen, Werte prüfen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f_0(x) = f_1(x) ⇔ 1/4 x³ + 1/4 = 1/4 x³ + x² + x + 1/4 ⇔ x · (x + 1) = 0 ⇔ x = −1 ∨ x = 0; f_a(−1) = 0, f_a(0) = 1/4; Punkte (−1 | 0), (0 | 1/4) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur zwei konkrete Parameterwerte vergleichen, ohne die Allgemeinheit zu zeigen",
    bemerkung="Standardbezug: K2 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAnalysisWTR1", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Abbildung zwischen zwei Graphen angeben", typ_neben="",
    stichwoerter="1/4 (x + 1)³ = 1/4 x³ + 3/4 x² + 3/4 x + 1/4 (a = 3/4)|aus G_0: um 1 nach links, um 1/4 nach unten",
    voraussetzungen="Verschiebung im Argument und im Wert",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Scharfunktion mit Term 1/4 (x + 1)³; G_0 Graph von 1/4 x³ + 1/4",
    gesucht="Verschiebungen, die den Graphen aus G_0 erzeugen",
    verfahren="Term als verschobenes 1/4 x³ lesen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Verschiebung um 1 in negative x-Richtung und um 1/4 in negative y-Richtung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Verschiebung nach rechts",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2026MerhoehtBAnalysisWTR1", "d", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentenabschnitt auf der x-Achse als Quotient f/f' am Graphen begründen", typ_neben="",
    stichwoerter="Tangente in P_u, Q_u = (u; 0) Lotfußpunkt, T_u Schnitt mit der x-Achse|Steigungsdreieck: f_0'(u) = |P_uQ_u| / |T_uQ_u| = f_0(u)/|T_uQ_u||für u > 0 sind f_0(u) > 0 und f_0'(u) > 0",
    voraussetzungen="Steigung als Gegenkathete durch Ankathete im Steigungsdreieck|Vorzeichen für u > 0|Eintragungen in die Abbildung",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=G0, kontext="ohne", textumfang="mittel",
    gegeben="G_0; für u > 0 Tangente t_u in P_u(u | f_0(u)), Punkt Q_u(u | 0), T_u Schnittpunkt von t_u mit der x-Achse",
    gesucht="Begründung mit Eintragungen in der Abbildung, dass |T_uQ_u| = f_0(u)/f_0'(u)",
    verfahren="Steigungsdreieck P_u, Q_u, T_u einzeichnen und die Steigung als Quotient lesen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="für jeden Wert u > 0 gilt f_0'(u) > 0 sowie f_0(u) > 0 und damit f_0'(u) = |P_uQ_u| / |T_uQ_u| = f_0(u) / |T_uQ_u|, woraus |T_uQ_u| = f_0(u)/f_0'(u) folgt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die Tangentengleichung aufstellen und rechnen statt am Steigungsdreieck zu argumentieren",
    bemerkung="Standardbezug: K1 III, K2 II, K4 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis mit der am Steigungsdreieck hergeleiteten Beziehung.")

KREIS2 = "keine Abbildung zu e; Graph von f_0' = 3/4 x² gedacht"
row("2026MerhoehtBAnalysisWTR1", "e", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Mittelpunkt eines den Graphen berührenden Kreises über die Normale im Berührpunkt bestimmen", typ_neben="",
    stichwoerter="f_0''(1) = 3/2 Tangentensteigung an f_0' in A|Normale y = −2/3 x + n, A(1; 3/4): n = 17/12|Mittelpunkt (0; 17/12)",
    voraussetzungen="Berührung: Mittelpunkt auf der Normalen|zweite Ableitung|Achsenschnitt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f_0'(x) = 3/4 x²; Kreis mit Mittelpunkt auf der y-Achse berührt den Graphen von f_0' in genau zwei Punkten, A(1 | 3/4) ist Berührpunkt",
    gesucht="y-Koordinate des Mittelpunkts, rechnerisch",
    verfahren="Normale an den Graphen von f_0' in A, Schnitt mit der y-Achse",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Steigung der Tangente an den Graphen von f_0' in A: f_0''(1) = 3/2; Normale: y = −2/3 x + n, 3/4 = −2/3 + n ⇔ n = 17/12; y-Koordinate 17/12 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="f_0' statt f_0'' als Steigung",
    bemerkung="Standardbezug: K2 III, K4 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Berührung in Normalenbedingung übersetzen. Typ wiederverwendet (2026-ga-B, dort mit Abbildung).")

# ---- Analysis WTR 1, Aufgabe 2: Fontäne h(x) = −π/4 cos(π/3 x) + 1
FONT = "Koordinatensystem x 0 bis 10 (Sekunden), y 0 bis 2; Kosinuswelle um 1 mit Amplitude π/4, Minima bei 0 und 6, Maxima bei 3 und 9"
row("2026MerhoehtBAnalysisWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Periode einer Kosinusfunktion im Sachzusammenhang deuten und Stelle stärkster Zunahme am Graphen angeben", typ_neben="",
    stichwoerter="Periode 2π/(π/3) = 6 s|Maxima bei 3, 9, …: in 60 s zehnmal|stärkste Zunahme an der steigenden Wendestelle 1,5",
    voraussetzungen="Periode aus dem Argument|Maxima abzählen|Wendestelle als stärkste Zunahme",
    format="Rechnung|Kurzantwort", operator="Bestimmen Sie|Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=FONT, kontext="Wasserfontäne/Durchflussrate", textumfang="lang",
    gegeben="h(x) = −π/4 · cos(π/3 · x) + 1, x Zeit in Sekunden, h(x) Durchflussrate in Litern je Sekunde; Graph in der Abbildung",
    gesucht="Anzahl der Maxima in der ersten Minute und ein Zeitpunkt stärkster Zunahme",
    verfahren="Periode 6, 60/6 Maxima; Wendestelle im steigenden Ast",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="Sekunden|Liter", abhaengig_von="",
    ergebnis="Anzahl: 60/6 = 10; Zeitpunkt: 1,5 Sekunden nach Beobachtungsbeginn (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Maximum bei 60 mitzählen oder Maximum als stärkste Zunahme nennen",
    bemerkung="Standardbezug: K3 II, K4 I, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2026MerhoehtBAnalysisWTR1", "b", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="∫_5^9 h(x) dx = [−3/4 sin(π/3 x) + x]_5^9 = (32 − 3√3)/8 ≈ 3,35|Wassermenge in Litern zwischen 5 und 9 Sekunden",
    voraussetzungen="Stammfunktion von cos(bx)|Integral einer Rate als Menge",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Interpretieren Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Wasserfontäne/Durchflussrate", textumfang="kurz",
    gegeben="h wie in a; Integral von 5 bis 9 über h(x) dx",
    gesucht="Wert des Integrals und seine Bedeutung",
    verfahren="Stammfunktion, Einsetzen, als Wassermenge deuten",
    schritte="3", zahlenraum="Bruch|Wurzel|dezimal", einheiten="Liter|Sekunden", abhaengig_von="",
    ergebnis="∫_5^9 h(x) dx = [−3/4 · sin(π/3 x) + x]_5^9 = −3/4 sin(3π) + 9 + 3/4 sin(5π/3) − 5 = (32 − 3√3)/8; im Zeitraum von fünf bis neun Sekunden nach Beobachtungsbeginn treten etwa 3,35 Liter Wasser an der Düse aus (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Kettenfaktor 3/π beim Integrieren vergessen",
    bemerkung="Standardbezug: K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAnalysisWTR1", "c", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Graphen einer periodischen Funktion mit vorgegebenem Maximum und Periode skizzieren", typ_neben="",
    stichwoerter="Periode 1,5 · 6 = 9 s|Maximalwert 2 Liter je Sekunde|z. B. Kosinuskurve mit Minimum bei 0, Maximum 2 bei 4,5",
    voraussetzungen="Periode skalieren|Amplitude und Lage aus dem Maximalwert",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=FONT, kontext="Wasserfontäne/Durchflussrate", textumfang="mittel",
    gegeben="andere Düse: maximale Rate 2 Liter je Sekunde, Abstand der Maxima 1,5-mal so groß wie bei h (also 9 s)",
    gesucht="möglicher Graph in der Abbildung",
    verfahren="periodische Kurve mit Maximum 2 und Periode 9 einzeichnen",
    schritte="2", zahlenraum="dezimal", einheiten="Sekunden|Liter", abhaengig_von="",
    ergebnis="Kurve mit Periode 9 und Maximalwert 2, z. B. gestrichelt von etwa 0,2 bei 0 über das Maximum 2 bei 4,5 zurück auf 0,2 bei 9 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Periode 1,5 s statt 9 s",
    bemerkung="Standardbezug: K2 II, K3 II, K4 II. AB amtlich: II. Amtlich.")

# ---- Analysis WTR 2, Aufgabe 1: Schar g_a = e^x + a e^−x
SCH = "Koordinatensystem ohne Skalen; drei nach oben geöffnete Kurven I (durchgezogen, tiefstes Minimum), II (gestrichelt), III (gestrichelt, höchstes Minimum), alle links steil fallend, rechts steigend"
row("2026MerhoehtBAnalysisWTR2", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Positivität, y-Achsenabschnitt und Steigung einer Schar begründen und berechnen", typ_neben="",
    stichwoerter="e^x > 0, a e^−x > 0 ⇒ g_a > 0|g_a(0) = 1 + a|g_a'(x) = e^x − a e^−x, g_a'(0) = 1 − a",
    voraussetzungen="Positivität der e-Funktion|Wert bei 0|Ableitung mit Parameter",
    format="Begründung|Rechnung", operator="Begründen Sie|Geben Sie an|Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="g_a(x) = e^x + a · e^−x in IR, a > 0",
    gesucht="Begründung G_a oberhalb der x-Achse, Schnittpunkt mit der y-Achse, Steigung dort",
    verfahren="Summanden positiv, g_a(0), g_a'(0)",
    schritte="3", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="wegen e^x > 0 und a · e^−x > 0 für a > 0 gilt g_a(x) > 0; Schnittpunkt mit der y-Achse (0 | 1 + a); g_a'(x) = e^x − a · e^−x, g_a'(0) = 1 − a (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Ableitung von a e^−x ohne Vorzeichenwechsel",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAnalysisWTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter den Graphen über den y-Achsenabschnitt zuordnen", typ_neben="",
    stichwoerter="g_a(0) = 1 + a wächst mit a|1/k < k < k² für k > 1|I: 1/k, II: k, III: k²",
    voraussetzungen="y-Achsenabschnitt aus a|Ordnung der Parameterwerte",
    format="Kurzantwort|Begründung", operator="Ordnen Sie zu|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SCH, kontext="ohne", textumfang="mittel",
    gegeben="Abbildung mit Graphen von g_a zu a = 1/k, k, k² für ein k > 1",
    gesucht="Zuordnung mit Begründung",
    verfahren="Schnittpunkte mit der y-Achse vergleichen",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="aus g_a(0) = 1 + a und 1/k < k < k² ergibt sich I: 1/k, II: k, III: k² (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Zuordnung über das Minimum ohne Begründung",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. AB amtlich: II. Amtlich. Vom Typ „Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen“ getrennt (Achsenabschnitt).")

row("2026MerhoehtBAnalysisWTR2", "c", innen="1", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Verschobene Scharfunktion als gerade Funktion nachweisen", typ_neben="",
    stichwoerter="h_a(x) = e^{x + ½ ln a} + a e^{−x − ½ ln a} = e^x √a + a e^−x / √a = √a (e^x + e^−x)|h_a(−x) = h_a(x)",
    voraussetzungen="Potenzgesetze mit e^{½ ln a} = √a|Symmetrie über h(−x) = h(x)",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="h_a(x) = g_a(x + 1/2 ln a), a > 0",
    gesucht="rechnerischer Nachweis h_a(x) = √a (e^x + e^−x) und der Achsensymmetrie",
    verfahren="Exponenten aufspalten, e^{½ ln a} = √a, dann h_a(−x) bilden",
    schritte="4", zahlenraum="Wurzel|Potenz", einheiten="", abhaengig_von="",
    ergebnis="h_a(x) = e^{x + ½ ln a} + a · e^{−(x + ½ ln a)} = e^x · a^{1/2} + a · e^−x · a^{−1/2} = √a · (e^x + e^−x); h_a(−x) = √a · (e^−x + e^x) = h_a(x) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="e^{½ ln a} = ½ a rechnen",
    bemerkung="Standardbezug: K1 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Geschätzt II: Nachrechnen einer Identität mit mitgeführtem Parameter (Prinzip); amtlich III über K5 – die Potenzumformung mit ln a wertet das IQB als anspruchsvoll.")

row("2026MerhoehtBAnalysisWTR2", "d", innen="1", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Symmetrieachse einer Scharkurve aus der Verschiebung einer geraden Funktion begründen", typ_neben="",
    stichwoerter="G_a entsteht aus dem Graphen von h_a durch Verschiebung um ½ ln a in x-Richtung|Symmetrieachse x = ½ ln a",
    voraussetzungen="g_a(x) = h_a(x − ½ ln a)|Verschiebung erhält die Achsensymmetrie",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="h_a gerade (aus c), h_a(x) = g_a(x + ½ ln a)",
    gesucht="Begründung, dass G_a achsensymmetrisch ist, und Gleichung der Achse in a",
    verfahren="G_a als verschobenen Graphen von h_a deuten",
    schritte="2", zahlenraum="Potenz", einheiten="", abhaengig_von="2026MerhoehtBAnalysisWTR2-1c",
    ergebnis="da G_a aus dem Graphen von h_a durch eine Verschiebung in x-Richtung erzeugt werden kann, ist G_a symmetrisch bezüglich einer zur y-Achse parallelen Geraden; Gleichung: x = 1/2 ln a (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Vorzeichen der Verschiebung (x = −½ ln a)",
    bemerkung="Standardbezug: K1 III, K2 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Symmetrie über die Verschiebung der geraden Funktion erkennen, verkettet mit der Richtung der Verschiebung.")

# ---- Analysis WTR 2, Aufgabe 2: Bahnhofshalle f(x) = 2,6 − 0,5(e^x + e^−x)
HALLE = "Skizze: Vorderansicht einer Halle, symmetrisch zur y-Achse, Dachprofil als nach unten geöffnete Kurve zwischen x = −1,2 und 1,2, senkrechte Seitenkanten, zwei bogenförmige Einfahrten (linke und rechte) im unteren Bereich, graue Fläche außerhalb der Einfahrten"
row("2026MerhoehtBAnalysisWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="Breite 2 · 1,2 · 20 m = 48 m|Höhe f(0) · 20 m = 1,6 · 20 m = 32 m",
    voraussetzungen="Maßstab 1 LE = 20 m|f(0)",
    format="Rechnung", operator="Zeigen Sie|Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=HALLE, kontext="Bahnhofshalle", textumfang="lang",
    gegeben="f(x) = 2,6 − 0,5 · (e^x + e^−x); Profil für −1,2 ≤ x ≤ 1,2; 1 LE = 20 m",
    gesucht="Nachweis der Breite 48 m und die Höhe der Halle",
    verfahren="Breite aus den Grenzen, Höhe aus f(0), beide mit dem Maßstab",
    schritte="2", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="Breite: 2 · 1,2 · 20 m = 48 m; Höhe: f(0) · 20 m = 1,6 · 20 m = 32 m (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Maßstab vergessen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2026MerhoehtBAnalysisWTR2", "b", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Flächeninhalt einer Vorderansicht als Integral mit Maßstab und Abzug berechnen", typ_neben="",
    stichwoerter="2 ∫_0^1,2 f(x) dx = 2 [2,6x − ½(e^x − e^−x)]_0^1,2 ≈ 3,221|3,221 · (20 m)² − 447 m² ≈ 841 m²",
    voraussetzungen="Symmetrie für die Grenzen|Stammfunktion von e^x + e^−x|Flächenmaßstab 400 m² je FE|Abzug der Einfahrten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=HALLE, kontext="Bahnhofshalle", textumfang="mittel",
    gegeben="Vorderansicht zwischen x-Achse, x = ±1,2 und Graph von f; Einfahrten zusammen etwa 447 m²; 1 LE = 20 m",
    gesucht="Flächeninhalt der grau markierten Fläche (Vorderansicht ohne Einfahrten)",
    verfahren="Integral über die Halbseite verdoppeln, mit 400 multiplizieren, 447 abziehen",
    schritte="4", zahlenraum="dezimal|Potenz", einheiten="m²", abhaengig_von="",
    ergebnis="2 · ∫_0^1,2 f(x) dx = 2 · [2,6x − 1/2 (e^x − e^−x)]_0^1,2 ≈ 3,221; Flächeninhalt 3,221 · (20 m)² − 447 m² ≈ 841 m² (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Maßstab nur einfach statt quadratisch anwenden",
    bemerkung="Traegerbindung: Kontext (die graue Fläche und die Einfahrten sind nur aus der Abbildung der Halle zu verstehen). Standardbezug: K2 II, K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAnalysisWTR2", "c", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Winkel zwischen Graph und senkrechter Kante über die Ableitung berechnen", typ_neben="",
    stichwoerter="f'(x) = −0,5 (e^x − e^−x), f'(−1,2) ≈ 1,509|tan(α − 90°) = f'(−1,2), α ≈ 146,5°",
    voraussetzungen="Steigungswinkel der Tangente|Winkel zur Senkrechten als 90° plus Steigungswinkel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=HALLE, kontext="Bahnhofshalle", textumfang="kurz",
    gegeben="Profillinie f für −1,2 ≤ x ≤ 1,2; linke Seitenkante senkrecht bei x = −1,2",
    gesucht="Winkel zwischen Profillinie und linker Seitenkante",
    verfahren="f'(−1,2), Winkel zur Senkrechten über den Tangens",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="°", abhaengig_von="",
    ergebnis="f'(x) = −0,5 · (e^x − e^−x); tan(α − 90°) = f'(−1,2) liefert α ≈ 146,5° (amtlich)",
    zwischenergebnis="Steigungswinkel ≈ 56,5°",
    niveau_geschaetzt="II",
    fehlerquelle="Winkel zur x-Achse (56,5°) angeben",
    bemerkung="Traegerbindung: Kontext (welcher Winkel gemeint ist, zeigt nur die Abbildung). Standardbezug: K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAnalysisWTR2", "d", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Abstand eines Punktes von einem Graphen über die Normalenbedingung deuten", typ_neben="",
    stichwoerter="(r(x_Q) − 0,6)/(x_Q − 0,8) · r'(x_Q) = −1: Verbindungsgerade PQ steht senkrecht auf der Tangente in Q|√(…) · 20 ≈ 0,85: Abstand der Signalleuchte vom oberen Rand in Metern",
    voraussetzungen="Produkt der Steigungen −1 als Orthogonalität|Abstand als Länge des Lots|Maßstab",
    format="Kurzantwort", operator="Geben Sie an|Erläutern Sie", antwort="Text",
    material="Skizze", skizze=HALLE, kontext="Bahnhofshalle", textumfang="lang",
    gegeben="r(x) = 0,75 − 10 (x − 0,5)⁴ oberer Rand der rechten Einfahrt, Signalleuchte P(0,8 | 0,6); vorgelegte Rechnung mit x_Q ≈ 0,835 und Ergebnis 0,85",
    gesucht="Bedeutung von 0,85 und Erläuterung des Ansatzes für x_Q",
    verfahren="Gleichung als Orthogonalität von PQ und Tangente deuten, Ergebnis als Abstand",
    schritte="2", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="der Abstand der Signalleuchte zum oberen Rand der Einfahrt beträgt etwa 0,85 m; die x-Koordinate von Q wird so bestimmt, dass die Strecke QP senkrecht auf dem Graphen von r steht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="0,85 als Höhe der Leuchte deuten",
    bemerkung="Traegerbindung: Kontext (Signalleuchte und Einfahrt aus der Trägeraufgabe). Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis WTR 3: f(x) = 5e^{−3x/5} − 5, Umkehrfunktion
GF3 = "Koordinatensystem x −4 bis 4, y −4 bis 4; Gf streng monoton fallend durch den Ursprung, links steil nach oben, rechts gegen y = −5; Abb. 2 zusätzlich mit dem an y = x gespiegelten Graphen von g"
row("2026MerhoehtBAnalysisWTR3", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Monotonie, Nullstelle und Grenzwert einer e-Funktion am Term begründen", typ_neben="",
    stichwoerter="e^−x streng monoton fallend, gestreckt und verschoben|f(0) = 5 − 5 = 0|lim f = −5",
    voraussetzungen="Monotonie von e^−x bleibt unter Streckung und Verschiebung|Grenzwert von e^−x",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=GF3, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 5 · e^{−3/5 x} − 5 in IR",
    gesucht="Begründung: streng monoton fallend und durch den Ursprung; Grenzwert für x → +∞",
    verfahren="Term als Transformation von e^−x lesen",
    schritte="3", zahlenraum="ganz|Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="da G_f gegenüber dem streng monoton fallenden Graphen von x ↦ e^−x gestreckt und verschoben ist, ist G_f streng monoton fallend; f(0) = 5 · e⁰ − 5 = 0; lim f(x) = −5 für x → +∞ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Grenzwert 0 statt −5",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Grenzwerte und Verhalten im Unendlichen.")

row("2026MerhoehtBAnalysisWTR3", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Bestimmtes Integral mit vorgegebener Stammfunktion berechnen", typ_neben="",
    stichwoerter="F(5/3) − F(0) = −25/3 e^−1 − 25/3 + 25/3 = −25/3 e^−1",
    voraussetzungen="Hauptsatz mit gegebener Stammfunktion",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="F(x) = −25/3 e^{−3/5 x} − 5x Stammfunktion von f",
    gesucht="∫_0^{5/3} f(x) dx",
    verfahren="F(5/3) − F(0)",
    schritte="1", zahlenraum="Bruch|Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="∫_0^{5/3} f(x) dx = F(5/3) − F(0) = −25/3 · e^−1 − 25/3 − (−25/3) = −25/3 · e^−1 (amtlich)",
    zwischenergebnis="≈ −3,07", niveau_geschaetzt="I",
    fehlerquelle="F(0) = 0 annehmen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAnalysisWTR3", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Eindeutige Lösung einer Flächengleichung über die Monotonie des Flächeninhalts begründen", typ_neben="",
    stichwoerter="A = ∫_{−1}^0 f fest, A_k = −∫_0^k f wächst streng mit k|A_1 < A und A_2 > A|genau ein k",
    voraussetzungen="Integrale als Flächen deuten|Monotonie einer Flächenfunktion|Zwischenwertargument",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF3, kontext="ohne", textumfang="mittel",
    gegeben="Aussage: es gibt genau ein k > 0 mit ∫_{−1}^0 f(x) dx = −∫_0^k f(x) dx",
    gesucht="Begründung ohne Stammfunktion",
    verfahren="linke Seite als feste Fläche, rechte als wachsende Fläche unter der x-Achse",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="A_k wächst mit zunehmendem Wert von k; da zudem A_1 < A und A_2 > A gilt, ist die Aussage wahr (amtlich)",
    zwischenergebnis="A ≈ 3,19, A_1 ≈ 2,26, A_2 ≈ 3,83", niveau_geschaetzt="II",
    fehlerquelle="nur die Existenz, nicht die Eindeutigkeit begründen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAnalysisWTR3", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Aufgabenstellung zu einem Rotationsvolumen-Anteil aus dem Lösungsweg formulieren", typ_neben="",
    stichwoerter="V1 = π ∫_0^4 f² dx Rotationskörper|V2 = π f(4)² · 4 Zylinder mit Radius |f(4)| und Höhe 4|Anteil V1/V2 ≈ 54 %",
    voraussetzungen="Rotationsvolumen-Formel|Zylindervolumen|Quotient als Anteil",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Lösungsweg: V1 = π · ∫_0^4 (f(x))² dx ≈ 141,02; V2 = π · (f(4))² · 4 ≈ 259,74; V1/V2 ≈ 0,54",
    gesucht="passende Aufgabenstellung",
    verfahren="Terme als Rotationskörper und Zylinder deuten",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="betrachtet wird der Körper, der bei Rotation des Graphen von f um die x-Achse im Bereich 0 ≤ x ≤ 4 entsteht; berechnen Sie den Anteil des Volumens dieses Körpers an dem eines Zylinders mit dem Radius |f(4)| und der Höhe 4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="V2 als Kegel deuten",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Rotationsvolumen in Teil B.")

row("2026MerhoehtBAnalysisWTR3", "e", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Umkehrfunktion",
    typ="Definitionsbereich der Umkehrfunktion angeben und ihren Term nachweisen", typ_neben="",
    stichwoerter="Wertemenge von f: ]−5; ∞[ = Definitionsbereich von g|y = 5e^{−3x/5} − 5 ⇔ (y + 5)/5 = e^{−3x/5} ⇔ x = −5/3 ln((y + 5)/5)|g(x) = −5/3 ln(1/5 x + 1)",
    voraussetzungen="Definitionsbereich der Umkehrfunktion als Wertemenge|Auflösen nach x mit Logarithmus",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Zeigen Sie", antwort="Term",
    material="Koordinatensystem", skizze=GF3, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 5e^{−3/5 x} − 5; g Umkehrfunktion von f",
    gesucht="Definitionsbereich von g und Nachweis g(x) = −5/3 · ln(1/5 x + 1)",
    verfahren="Gleichung nach x auflösen, Variablen tauschen",
    schritte="3", zahlenraum="Bruch|Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Definitionsbereich von g: ]−5; +∞[; y = 5 · e^{−3/5 x} − 5 ⇔ (y + 5)/5 = e^{−3/5 x} ⇔ ln((y + 5)/5) = −3/5 x ⇔ −5/3 · ln((y + 5)/5) = x, somit g(x) = −5/3 · ln(1/5 x + 1) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Definitionsbereich von g mit dem von f verwechseln",
    bemerkung="Standardbezug: K1 II, K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAnalysisWTR3", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt der Tangente mit vorgegebener Steigung berechnen", typ_neben="",
    stichwoerter="f'(x) = −3e^{−3x/5}|f'(x_Q) = −1 ⇔ e^{−3x/5} = 1/3 ⇔ x_Q = 5/3 ln 3|f(x_Q) = −10/3",
    voraussetzungen="Ableitung der e-Funktion|Exponentialgleichung mit ln",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Tangente t an G_f mit Steigung −1 berührt in Q; Kontrolle x_Q = 5/3 ln 3",
    gesucht="Koordinaten von Q",
    verfahren="f'(x) = −1 lösen, f(x_Q)",
    schritte="3", zahlenraum="Bruch|Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −3e^{−3/5 x}; f'(x_Q) = −1 ⇔ −3/5 x_Q = ln 1/3 ⇔ x_Q = 5/3 · ln 3; f(x_Q) = −10/3 (amtlich)",
    zwischenergebnis="Q ≈ (1,83 | −3,33)", niveau_geschaetzt="II",
    fehlerquelle="ln(1/3) = −ln 3 falsch aufgelöst",
    bemerkung="Standardbezug: K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Tangente mit vorgegebener Steigung außerhalb eines Punktes angeben“ getrennt (Berührpunkt berechnen).")

row("2026MerhoehtBAnalysisWTR3", "g", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Umkehrfunktion",
    typ="Tangente an Funktion und Umkehrfunktion über die Spiegelung an y = x begründen", typ_neben="",
    stichwoerter="t hat Steigung −1, ist also symmetrisch zu y = x|Graph von g ist Spiegelbild von G_f an y = x|t berührt g im Spiegelpunkt P(f(x_Q) | x_Q)",
    voraussetzungen="Gerade mit Steigung −1 wird auf sich abgebildet|Umkehrfunktion als Spiegelung|Spiegelpunkt",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF3, kontext="ohne", textumfang="mittel",
    gegeben="t Tangente an G_f in Q mit Steigung −1; g Umkehrfunktion",
    gesucht="Begründung ohne Rechnung, dass t auch den Graphen von g berührt, in P(f(x_Q) | x_Q)",
    verfahren="Spiegelung an y = x auf t und G_f anwenden",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2026MerhoehtBAnalysisWTR3-1f",
    ergebnis="t hat die Steigung −1 und ist daher symmetrisch bezüglich der Geraden y = x; da der Graph von g aus G_f durch Spiegelung an dieser Geraden erzeugt werden kann, berührt t auch den Graphen von g, und zwar im Spiegelpunkt von Q (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Tangente an g neu berechnen statt zu spiegeln",
    bemerkung="Standardbezug: K1 III, K2 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Symmetrie zu y = x erkennen (Steigung −1) und mit der Spiegelung der Umkehrfunktion verketten.")

row("2026MerhoehtBAnalysisWTR3", "h", innen="1", seite="2", punkte="6", afb_amtlich="II|III",
    leitidee="Analysis", thema="Umkehrfunktion",
    typ="Flächeninhalt eines Vierecks aus Berührpunkten und Spiegelpunkten als Trapez begründen", typ_neben="",
    stichwoerter="PQRS symmetrisch zu y = x, PQ ∥ RS (beide Steigung −1): Trapez|Fläche (|PQ| + |RS|)/2 · h|S hat die y-Koordinate von P, ∠QPS = 45°, Dreieck SPT gleichschenklig|h = (|PQ| − |RS|)/2",
    voraussetzungen="Viereck einzeichnen|Symmetrie zu y = x|Trapezformel|45°-Dreieck für die Höhe",
    format="Zeichnen|Begründung", operator="Zeichnen Sie ein|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF3, kontext="ohne", textumfang="mittel",
    gegeben="Q(x_Q | f(x_Q)), P(f(x_Q) | x_Q), R(x_Q | g(x_Q)), S(g(x_Q) | x_Q)",
    gesucht="Viereck PQRS in der Abbildung und Begründung des Flächenterms (|PQ| + |RS|)/2 · (|PQ| − |RS|)/2",
    verfahren="Trapez erkennen, Höhe über das gleichschenklig-rechtwinklige Dreieck",
    schritte="4", zahlenraum="ganz", einheiten="", abhaengig_von="2026MerhoehtBAnalysisWTR3-1g",
    ergebnis="das Viereck ist aufgrund seiner Symmetrie bezüglich y = x ein Trapez mit Flächeninhalt (|PQ| + |RS|)/2 · h, h Abstand der parallelen Seiten; aufgrund der Symmetrie und weil S die gleiche y-Koordinate wie P hat, gilt ∠QPS = 45°, das Dreieck SPT ist gleichschenklig und h = (|PQ| − |RS|)/2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Höhe als |PS| nehmen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (b) Symmetrie und 45°-Sonderfall erkennen, verkettet mit der Trapezformel.")

# ---- AG/LA (A1) WTR: Quader, Verflechtung
QUADER = "Schrägbild eines Quaders ABCDEFGH, aufgespannt von u (AB), v (AD), w (AE); A vorn links unten"
row("2026MerhoehtBAGLAA1WTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Verbindungsvektor zweier Kantenmittelpunkte als Linearkombination der Kantenvektoren angeben", typ_neben="",
    stichwoerter="M1 Mitte von BC, M2 Mitte von EF|M1M2 = −½ u − ½ v + w|r = s = −1/2, t = 1",
    voraussetzungen="Mittelpunkte über halbe Kanten|Vektorkette im Quader",
    format="Zeichnen|Kurzantwort", operator="Zeichnen Sie ein|Geben Sie an", antwort="Zahl",
    material="Körper", skizze=QUADER, kontext="ohne", textumfang="mittel",
    gegeben="Quader ABCDEFGH von u, v, w aufgespannt; M1 Mittelpunkt von BC, M2 Mittelpunkt von EF",
    gesucht="Strecke M1M2 in der Abbildung und r, s, t mit M1M2 = r u + s v + t w",
    verfahren="Weg von M1 über B und A nach E und M2 als Vektorkette",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="r = s = −1/2; t = 1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen von r (Richtung von u)",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MerhoehtBAGLAA1WTR", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen berechnen", typ_neben="",
    stichwoerter="AG = (−6; 8; h), CE = (6; −8; h)|AG · CE = −36 − 64 + h² = 0 ⇔ h = 10|V = 6 · 8 · 10 = 480",
    voraussetzungen="Diagonalvektoren mit Parameter|Skalarprodukt null|Quadervolumen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=QUADER, kontext="ohne", textumfang="kurz",
    gegeben="A(6 | 0 | 0), B(6 | 8 | 0), C(0 | 8 | 0), E(6 | 0 | h), h > 0; Raumdiagonalen AG und CE senkrecht",
    gesucht="h und Volumen des Quaders",
    verfahren="Skalarprodukt der Diagonalen null setzen, Volumen aus den Kanten",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="mit AG = (−6; 8; h) und CE = (6; −8; h) gilt AG · CE = 0 ⇔ −36 − 64 + h² = 0 ⇔ h = 10; Volumen 6 · 8 · 10 = 480 (amtlich)",
    zwischenergebnis="G(0 | 8 | 10)", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen in CE",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MerhoehtBAGLAA1WTR", "a", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix berechnen", typ_neben="",
    stichwoerter="z = Z · (1; 1) = (5; 5; 4)|r1 = 5 · 5 + 4 · 5 + 5 · 4 = 65",
    voraussetzungen="zweistufige Verflechtung|Matrix-Vektor-Produkt|eine Zeile der Rohstoffmatrix",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Verflechtung", textumfang="lang",
    gegeben="R · z = r mit R = ((5; 4; 5), (4; 5; 6), (5; 6; 6)); Z · e = z mit Z = ((2; 3), (3; 2), (2; 2)); je eine ME von E1 und E2",
    gesucht="ME der drei Zwischenprodukte und des Rohstoffs R1",
    verfahren="Z · (1; 1), dann erste Zeile von R mal z",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(z1; z2; z3) = ((2; 3), (3; 2), (2; 2)) · (1; 1) = (5; 5; 4); r1 = 5 · 5 + 4 · 5 + 5 · 4 = 65 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="R mit e statt mit z multiplizieren",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zweistufig). Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MerhoehtBAGLAA1WTR", "b", innen="2", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Gesamtmatrix im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="R · Z = ((32; 33), (35; 34), (40; 39)) ordnet Endproduktmengen direkt Rohstoffmengen zu",
    voraussetzungen="Produkt zweier Bedarfsmatrizen als Gesamtbedarf",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Produktion/Verflechtung", textumfang="kurz",
    gegeben="R · Z = ((32; 33), (35; 34), (40; 39))",
    gesucht="Bedeutung der Matrix",
    verfahren="Gesamtmatrix als Rohstoff-Endprodukt-Verflechtung deuten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="mithilfe der berechneten Matrix können aus gegebenen Anzahlen der Mengeneinheiten der beiden Endprodukte die hierfür benötigten Anzahlen der Mengeneinheiten der drei Rohstoffe berechnet werden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauscht deuten",
    bemerkung="Standardbezug: K3 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MerhoehtBAGLAA1WTR", "c", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Maximale Produktionsmenge aus dem Rohstoffvorrat ermitteln", typ_neben="",
    stichwoerter="nur E2: Bedarf (33e; 34e; 39e)|39e ≤ 429 ⇔ e ≤ 11|maximal 11 ME",
    voraussetzungen="Spalte der Gesamtmatrix|knappster Rohstoff entscheidet|Ganzzahligkeit",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Verflechtung", textumfang="mittel",
    gegeben="je 429 ME der drei Rohstoffe; nur E2 wird gefertigt",
    gesucht="maximale Anzahl ME von E2",
    verfahren="Rohstoffbedarf je ME E2 mit dem Vorrat vergleichen, engster Rohstoff",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2026MerhoehtBAGLAA1WTR-2b",
    ergebnis="aus ((32; 33), (35; 34), (40; 39)) · (0; e) = (33e; 34e; 39e) und 39e ≤ 429 folgt, dass maximal 11 Mengeneinheiten gefertigt werden können (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="429/33 = 13 nehmen (erster statt engster Rohstoff)",
    bemerkung="Standardbezug: K1 II, K2 II, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MerhoehtBAGLAA1WTR", "d", innen="2", seite="2", punkte="6", afb_amtlich="I|II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Maximale Kostensteigerung eines Rohstoffs aus einer Kostenschranke bestimmen", typ_neben="",
    stichwoerter="Kosten je ME E1 heute: 32 · 5 + 35 · 6 + 40 · 7 = 650|nach fünf Jahren: (160 + 210) · 1,03⁵ + 280 · x⁵|≤ 1,2 · 650 ⇔ x ≤ ⁵√((780 − 370 · 1,03⁵)/280) ≈ 1,0463|höchstens etwa 4,6 % pro Jahr",
    voraussetzungen="Rohstoffbedarf je ME E1 aus der Gesamtmatrix|Kosten als Summe Menge mal Preis|exponentielles Wachstum über fünf Jahre|Ungleichung nach x auflösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle Rohstoff R1, R2, R3 mit Anschaffungskosten 5, 6, 7 je ME", kontext="Produktion/Verflechtung", textumfang="lang",
    gegeben="Kosten je ME 5, 6, 7 GE; R1, R2 steigen 3 % je Jahr; Gesamtkosten der Rohstoffe für E1 dürfen in fünf Jahren um höchstens 20 % steigen",
    gesucht="maximaler jährlicher prozentualer Anstieg für R3",
    verfahren="Kostenterm heute und in fünf Jahren aufstellen, Ungleichung nach dem Wachstumsfaktor lösen",
    schritte="5", zahlenraum="dezimal|Potenz|Prozent", einheiten="GE|Prozent", abhaengig_von="2026MerhoehtBAGLAA1WTR-2b",
    ergebnis="K0 = 32 · 5 + 35 · 6 + 40 · 7 = 650; K5 = (32 · 5 + 35 · 6) · 1,03⁵ + 40 · 7 · x⁵ = 370 · 1,03⁵ + 280 · x⁵; mit K5 ≤ 1,2 · K0 folgt x ≤ ⁵√((1,2 · 650 − 370 · 1,03⁵)/280) ≈ 1,0463; der maximale Anstieg beträgt etwa 4,6 % pro Jahr (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Anstieg linear (5 · 3 %) statt exponentiell ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III, K4 I, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Kostenschranke in eine Ungleichung mit Wachstumsfaktor übersetzen, verkettet über Matrix, Kosten und Wurzel. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA (A2) WTR 1: Sprungschanze
SCHANZE = "Schrägbild: Körper ABCDEF über der xy-Ebene (grau als Wasseroberfläche), Schanzentisch AEFD schräg ansteigend nach hinten (y-Richtung), Kante EF oben; A und D bei z = −0,5"
row("2026MerhoehtBAGLAA2WTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Parallelogramm als Rechteck über das Skalarprodukt nachweisen", typ_neben="",
    stichwoerter="AE = (0; 5; 1,5), AD = (−4; 0; 0)|AE · AD = 0",
    voraussetzungen="rechter Winkel im Parallelogramm genügt",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Körper", skizze=SCHANZE, kontext="Sprungschanze/Wasserski", textumfang="lang",
    gegeben="A(2 | 0 | −0,5), D(−2 | 0 | −0,5), E(2 | 5 | 1), F(−2 | 5 | 1); AEFD Parallelogramm",
    gesucht="Nachweis, dass AEFD ein Rechteck ist",
    verfahren="Skalarprodukt zweier benachbarter Seiten",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="AE · AD = (0; 5; 1,5) · (−4; 0; 0) = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="alle vier Winkel prüfen wollen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAGLAA2WTR1", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebenen eines Körpers aus den Koordinaten begründen", typ_neben="",
    stichwoerter="A und D, E und F, B und C unterscheiden sich nur im Vorzeichen der x-Koordinate",
    voraussetzungen="Spiegelung an der yz-Ebene kehrt x um",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=SCHANZE, kontext="Sprungschanze/Wasserski", textumfang="kurz",
    gegeben="Körper ABCDEF mit A(2 | 0 | −0,5), B(3 | 5 | −0,5), C(−3 | 5 | −0,5), D(−2 | 0 | −0,5), E(2 | 5 | 1), F(−2 | 5 | 1)",
    gesucht="Begründung, dass die yz-Ebene Symmetrieebene ist",
    verfahren="Punktepaare mit gespiegelter x-Koordinate",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="die Koordinaten von A und D unterscheiden sich nur im Vorzeichen der x-Koordinate; dies gilt ebenso für E und F sowie B und C (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur ein Paar nennen",
    bemerkung="Standardbezug: K1 I, K2 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-A).")

row("2026MerhoehtBAGLAA2WTR1", "c", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Komponente des Normalenvektors aus der Orthogonalität zur Koordinatenebene begründen", typ_neben="",
    stichwoerter="Ebene AEFD steht senkrecht zur yz-Ebene (Symmetrieebene)|Normalenvektor liegt in der yz-Ebene: x-Komponente 0",
    voraussetzungen="Normalenvektor einer zu einer Ebene senkrechten Ebene ist Richtungsvektor dieser Ebene",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=SCHANZE, kontext="Sprungschanze/Wasserski", textumfang="kurz",
    gegeben="(k; 3; −10) Normalenvektor der Ebene AEFD; yz-Ebene Symmetrieebene (aus b)",
    gesucht="Begründung ohne Rechnung, dass k = 0",
    verfahren="Lage der Ebene zur yz-Ebene deuten",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MerhoehtBAGLAA2WTR1-1b",
    ergebnis="die Ebene, in der das Rechteck AEFD liegt, steht senkrecht zur yz-Ebene; damit ist jeder Normalenvektor dieser Ebene ein Richtungsvektor der yz-Ebene (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="doch mit AE und AD rechnen",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAGLAA2WTR1", "d", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="n = (0; 3; −10), n_xy = (0; 0; 1)|cos α = 10/√109|α ≈ 16,7°",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=SCHANZE, kontext="Sprungschanze/Wasserski", textumfang="kurz",
    gegeben="Normalenvektor (0; 3; −10) der Schanzentischebene; xy-Ebene Wasseroberfläche",
    gesucht="Neigungswinkel des Schanzentischs gegen die Wasseroberfläche",
    verfahren="Winkelformel mit den Normalenvektoren",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2026MerhoehtBAGLAA2WTR1-1c",
    ergebnis="cos α = |(0; 3; −10) · (0; 0; 1)| / (|(0; 3; −10)| · |(0; 0; 1)|) liefert α ≈ 16,7° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Winkel zwischen AE und der xy-Ebene nehmen (gleicher Wert, aber anderer Weg)",
    bemerkung="Standardbezug: K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAGLAA2WTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Teilverhältnis auf einer Kante deuten und Teilfläche eines Rechtecks berechnen", typ_neben="",
    stichwoerter="A + r · AE in der xy-Ebene für r = 1/3: ein Drittel von AE liegt unter Wasser|Werbefläche 2/3 · |AE| · |EF| = 2/3 · √27,25 · 4 ≈ 13,92 m²",
    voraussetzungen="Spurpunkt einer Kante als Wasserlinie|Rechteckfläche anteilig",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=SCHANZE, kontext="Sprungschanze/Wasserski", textumfang="lang",
    gegeben="Gleichung (2; 0; −0,5) + r · (0; 5; 1,5) = (x; y; 0) mit r = 1/3; Werbefläche = Teil des Schanzentischs oberhalb der Wasseroberfläche",
    gesucht="Bedeutung von r = 1/3 und Flächeninhalt der Werbefläche",
    verfahren="r als Anteil der Kante AE unter Wasser deuten, Restrechteck berechnen",
    schritte="3", zahlenraum="Bruch|Wurzel|dezimal", einheiten="m²", abhaengig_von="",
    ergebnis="für r = 1/3 ergibt sich, dass ein Drittel der Kante AE des Schanzentischs sich im Wasser befindet; Flächeninhalt in Quadratmetern 2/3 · |AE| · |EF| = 2/3 · |(0; 5; 1,5)| · 4 ≈ 13,92 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="1/3 der Fläche statt 2/3 nehmen",
    bemerkung="Traegerbindung: Kontext (Wasserlinie und Werbefläche nur aus der Trägeraufgabe). Standardbezug: K2 II, K3 I, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAGLAA2WTR1", "f", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Übereinstimmung einer Ebene mit einer Koordinatenebene beurteilen", typ_neben="",
    stichwoerter="Symmetrieebene ist die yz-Ebene x = 0|L: 10x − 3y = 0 ist nicht x = 0|Weg liegt nicht in der Symmetrieebene",
    voraussetzungen="Gleichung der yz-Ebene|Vergleich zweier Ebenengleichungen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Körper", skizze=SCHANZE, kontext="Sprungschanze/Wasserski", textumfang="lang",
    gegeben="Weg des Fahrers in der Ebene L: 10x − 3y = 0 (senkrecht zur xy-Ebene); Symmetrieebene des Körpers ist die yz-Ebene",
    gesucht="ob der Weg in der Symmetrieebene verläuft",
    verfahren="L mit x = 0 vergleichen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2026MerhoehtBAGLAA2WTR1-1b",
    ergebnis="da L nicht mit der yz-Ebene übereinstimmt, ist dies nicht der Fall (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="L wegen des Ursprungs für die Symmetrieebene halten",
    bemerkung="Traegerbindung: Kontext (Weg des Fahrers als Ebene L aus dem Sachtext). Standardbezug: K1 I, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich.")

row("2026MerhoehtBAGLAA2WTR1", "g", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Sprungweite als Abstand zweier Punkte einer Parameterkurve in der Grundebene berechnen", typ_neben="",
    stichwoerter="Auftreffen: z = 0 ⇔ −0,05(a − 2,61)(a − 13,39) = 0, a = 13,39 (Absprung bei a = 5 liegt dazwischen)|W(4,017 | 13,39 | 0)|V'(1,5 | 5 | 0) unter dem Absprung V(1,5 | 5 | 1)|Weite √((4,017 − 1,5)² + (13,39 − 5)²) ≈ 8,8 m",
    voraussetzungen="Nullstelle der z-Koordinate|Absprungpunkt auf EF in L|Projektion auf die Wasseroberfläche|Abstand",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze="Abb. 2: Seitenansicht in der Ebene L, Anlauf bis V, gestrichelte Flugkurve bis W auf der Wasseroberfläche, eingetragene Weite von V' bis W", kontext="Sprungschanze/Wasserski", textumfang="lang",
    gegeben="Sprungkurve (0,3a | a | −0,05 · (a − 2,61) · (a − 13,39)); Absprung an der Kante EF (y = 5), Auftreffen W auf z = 0; Weite = Abstand in der Wasseroberfläche",
    gesucht="Weite des Sprungs auf zehntel Meter",
    verfahren="a für z = 0 bestimmen, W und Lotfußpunkt des Absprungs, Abstand",
    schritte="4", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="−0,05 · (a − 2,61) · (a − 13,39) = 0 liefert a = 13,39 und damit W(4,017 | 13,39 | 0); V'(1,5 | 5 | 0) beschreibt den Ort auf der Wasseroberfläche unter dem Absprung; √((4,017 − 1,5)² + (13,39 − 5)²) ≈ 8,8; die Weite beträgt etwa 8,8 m (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Weite von V (z = 1) statt V' messen oder a = 2,61 wählen",
    bemerkung="Traegerbindung: Kontext (Absprungkante, Weite in der Wasseroberfläche und Abbildung 2). Standardbezug: K2 III, K3 II, K4 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „Weite“ in den Abstand der Projektionen übersetzen, verkettet mit Nullstelle und Absprungpunkt.")

# ---- AG/LA (A2) WTR 2: Pyramide, Drehung um CD
PYR2 = "Schrägbild einer Pyramide ABCDS mit Trapezgrundfläche in der xy-Ebene (A, D auf der y-Achse, B, C bei x = 4), Spitze S(2 | 0 | 4)"
row("2026MerhoehtBAGLAA2WTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Trapezgrundfläche nachweisen und Pyramidenvolumen berechnen", typ_neben="",
    stichwoerter="AD = (0; 6; 0), BC = (0; 2; 0) kollinear|Trapezfläche ½(6 + 2) · 4 = 16|V = 1/3 · 16 · 4 = 64/3",
    voraussetzungen="Parallelität|Trapezformel|Pyramidenvolumen mit Höhe 4",
    format="Rechnung", operator="Zeigen Sie|Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=PYR2, kontext="ohne", textumfang="kurz",
    gegeben="A(0 | −3 | 0), B(4 | −1 | 0), C(4 | 1 | 0), D(0 | 3 | 0), S(2 | 0 | 4)",
    gesucht="Nachweis Trapez und Volumen der Pyramide",
    verfahren="AD und BC vergleichen, Fläche mal Höhe durch drei",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="AD = (0; 6; 0) und BC = (0; 2; 0) sind kollinear; Volumen 1/3 · 1/2 · (6 + 2) · 4 · 4 = 64/3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Trapezhöhe 6 statt 4",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen“ (2026-ga-B) getrennt: Volumen statt Flächeninhalt.")

row("2026MerhoehtBAGLAA2WTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Winkel zwischen zwei Kanten über das Skalarprodukt berechnen", typ_neben="",
    stichwoerter="CD = (−4; 2; 0), CS = (−2; −1; 4)|cos α = 6/(√20 √21)|α ≈ 73,0°",
    voraussetzungen="Kantenvektoren|Winkelformel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=PYR2, kontext="ohne", textumfang="kurz",
    gegeben="C(4 | 1 | 0), D(0 | 3 | 0), S(2 | 0 | 4)",
    gesucht="Winkel zwischen CD und CS",
    verfahren="Skalarprodukt",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="cos α = ((−4; 2; 0) · (−2; −1; 4)) / (|(−4; 2; 0)| · |(−2; −1; 4)|) = 6/(√20 · √21) liefert α ≈ 73,0° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vektor DC statt CD",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2026MerhoehtBAGLAA2WTR2", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schnittpunkt von Gerade und Ebene berechnen", typ_neben="",
    stichwoerter="CD: x = (0; 3; 0) + μ (2; −1; 0)|−2 · 2μ + 3 − μ + 4 = 0 ⇔ μ = 1,4|H(2,8; 1,6; 0)",
    voraussetzungen="Kante als Gerade|Einsetzen in die Ebenengleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=PYR2, kontext="ohne", textumfang="kurz",
    gegeben="L: −2x + y + 4 = 0 schneidet die Kante CD in H; Kontrolle H(2,8 | 1,6 | 0)",
    gesucht="Koordinaten von H",
    verfahren="Geradengleichung der Kante, Parameter aus L",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="CD: x = (0; 3; 0) + μ · (2; −1; 0), μ ∈ IR; −2 · 2μ + 3 − μ + 4 = 0 ⇔ μ = 1,4; OH = (2,8; 1,6; 0) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Parameter aus [0; 1] erwarten und μ = 1,4 verwerfen (Stützpunkt D)",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2019-ea-A).")

row("2026MerhoehtBAGLAA2WTR2", "d", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Kreisbahn einer Drehung um eine Kante als Kreis in einer Ebene mit Mittelpunkt begründen", typ_neben="",
    stichwoerter="CD = (−4; 2; 0) kollinear zum Normalenvektor (−2; 1; 0) von L: L ⊥ CD|S ∈ L (−4 + 0 + 4 = 0)|Kreis liegt in L, Mittelpunkt = Schnitt von CD und L = H",
    voraussetzungen="Drehung um eine Achse: Bahn in der Ebene senkrecht zur Achse durch den Punkt|Mittelpunkt auf der Achse",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=PYR2, kontext="ohne", textumfang="mittel",
    gegeben="Pyramide wird um die Gerade CD um 360° gedreht; Spitze S durchläuft einen Kreis; L: −2x + y + 4 = 0; H = CD ∩ L",
    gesucht="Begründung, dass der Kreis in L liegt und H sein Mittelpunkt ist",
    verfahren="L senkrecht zur Achse und durch S, Mittelpunkt auf der Achse",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MerhoehtBAGLAA2WTR2-1c",
    ergebnis="da CD = (−4; 2; 0) kollinear zum Normalenvektor (−2; 1; 0) von L ist und −2 · 2 + 0 + 4 = 0 gilt, verläuft L senkrecht zur Geraden CD und enthält S; damit liegt der Kreis in L; dessen Mittelpunkt liegt folglich sowohl auf CD als auch in L und ist somit H (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="S ∈ L nicht prüfen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBAGLAA2WTR2", "e", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Existenz eines Kreispunkts mit vorgegebener Koordinate über den Radius widerlegen", typ_neben="",
    stichwoerter="Annahme S'(x; 5,6; z) auf dem Kreis|S' ∈ L: −2x + 5,6 + 4 = 0 ⇔ x = 4,8|HS' = (2; 4; z), |HS'|² = 20 + z² > 19,2 = r²|Widerspruch, Aussage falsch",
    voraussetzungen="Kreispunkt liegt in L und hat Abstand r von H|Abstand mit Parameter abschätzen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Körper", skizze=PYR2, kontext="ohne", textumfang="mittel",
    gegeben="Kreis um H(2,8 | 1,6 | 0) in L mit Radius √19,2; Aussage: es gibt eine Position mit y-Koordinate 5,6 der Spitze",
    gesucht="Beurteilung der Aussage",
    verfahren="Punkt mit y = 5,6 in L ansetzen, Abstand zu H mit dem Radius vergleichen",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="2026MerhoehtBAGLAA2WTR2-1d",
    ergebnis="Annahme: S'(x_S | 5,6 | z_S) liegt auf dem Kreis; dann liegt S' in L und −2x_S + 5,6 + 4 = 0 ⇔ x_S = 4,8; |HS'| = |(2; 4; z_S)| = √(20 + z_S²); wegen √(20 + z_S²) > √19,2 ein Widerspruch; die Aussage ist falsch (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="z frei lassen und die Aussage für wahr halten",
    bemerkung="Standardbezug: K1 III, K2 III, K4 III, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Aussage in Bedingungen an einen Kreispunkt übersetzen, verkettet mit der Abschätzung 20 + z² > 19,2.")

# ---- Stochastik WTR 1: Treuepunkte (erhöht)
VERT2 = "Säulendiagramm P(B = k), k = 0 bis 10, Maximum etwa 0,28 bei 2 (wie 2026-ga-B)"
BAUM2 = "Baumdiagramm T (75 %) / nicht T, darunter w (80 %) bzw. w (a) (wie 2026-ga-B)"
row("2026MerhoehtBStochastikWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="P(A < 8) = P(A ≤ 7) mit n = 10, p = 0,75 ≈ 47,4 %",
    voraussetzungen="„weniger als 8“ als A ≤ 7",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Supermarkt/Treuepunkte", textumfang="lang",
    gegeben="75 % sammeln Treuepunkte; A Anzahl der Sammler unter 10 Personen, binomialverteilt",
    gesucht="P(A < 8)",
    verfahren="kumulierte Verteilung am Rechner",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(A < 8) ≈ 47,4 % (n = 10, p = 0,75) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="A ≤ 8",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet; Teilaufgabe wortgleich mit 2026-ga-B Stochastik WTR 1, 1b (andere Trägeraufgabe, eigene Zeile).")

row("2026MerhoehtBStochastikWTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern", typ_neben="",
    stichwoerter="P(A = 6) = P(B = 4) mit B ~ B(10; 0,25)|Säule bei k = 4",
    voraussetzungen="Gegenzufallsgröße 10 − A",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Diagramm", skizze=VERT2, kontext="Supermarkt/Treuepunkte", textumfang="mittel",
    gegeben="Abbildung der Verteilung von B mit n = 10, p = 0,25",
    gesucht="Erläuterung, wie P(A = 6) aus der Abbildung folgt",
    verfahren="A = 6 heißt B = 4",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="wegen P(A = 6) = P(B = 4) (n = 10; p = 0,75 bzw. 0,25) entspricht in der Abbildung der Wert für k = 4 der gesuchten Wahrscheinlichkeit (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="k = 6 ablesen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet; wortgleich mit 2026-ga-B Stochastik WTR 1, 1c.")

row("2026MerhoehtBStochastikWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Absolute Anzahl aus einer Pfadwahrscheinlichkeit mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="P(w und T) = 0,75 · 0,8 = 0,6|0,6 < 400000/500000 = 0,8|Anzahl 300000 < 400000",
    voraussetzungen="Pfadregel|Anzahl als Anteil mal Gesamtzahl",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Diagramm", skizze=BAUM2, kontext="Supermarkt/Treuepunkte", textumfang="mittel",
    gegeben="Kundenkreis 500000 Personen; 75 % sammeln, davon 80 % weiblich",
    gesucht="ob die Anzahl der weiblichen Sammler kleiner als 400000 ist",
    verfahren="Pfad berechnen und mit 0,8 vergleichen",
    schritte="2", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="0,75 · 0,8 = 0,6 < 400000/500000; die Anzahl der Personen, die weiblich sind und Treuepunkte sammeln, ist kleiner als 400000 (amtlich)",
    zwischenergebnis="300000", niveau_geschaetzt="I",
    fehlerquelle="0,8 · 500000 = 400000 als Anzahl der Sammlerinnen nehmen",
    bemerkung="Standardbezug: K2 I, K3 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBStochastikWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen", typ_neben="",
    stichwoerter="0,75 · 0,2 + 0,25 · (1 − a) = 0,3 ⇔ a = 0,4",
    voraussetzungen="Randwahrscheinlichkeit als Pfadsumme|lineare Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=BAUM2, kontext="Supermarkt/Treuepunkte", textumfang="kurz",
    gegeben="Baumdiagramm mit a; 30 % nicht weiblich",
    gesucht="a",
    verfahren="Pfadsumme gleich 0,3",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,75 · 0,2 + 0,25 · (1 − a) = 0,3 ⇔ 0,4 − 0,25a = 0,3 ⇔ a = 0,4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Pfad über T vergessen",
    bemerkung="Standardbezug: K2 I, K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet; wortgleich mit 2026-ga-B Stochastik WTR 1, 2b.")

row("2026MerhoehtBStochastikWTR1", "c", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen", typ_neben="",
    stichwoerter="P(T | nicht w) = 0,15/(0,15 + 0,25 (1 − a))|a steigt ⇒ Nenner fällt ⇒ Quotient steigt|wahr",
    voraussetzungen="Bayes-Quotient mit Parameter|Monotonie",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Diagramm", skizze=BAUM2, kontext="Supermarkt/Treuepunkte", textumfang="lang",
    gegeben="ein Jahr später: 75 % Sammler, 80 % davon weiblich, a gestiegen; Aussage: P(T | nicht weiblich) größer als vor einem Jahr",
    gesucht="Beurteilung",
    verfahren="Term in a aufstellen, Monotonie begründen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="die Aussage ist wahr; mit 0,75 · 0,2 / (0,75 · 0,2 + 0,25 · (1 − a)) kann die Wahrscheinlichkeit berechnet werden; wenn a steigt, nimmt der Nenner ab und der Quotient zu (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Zähler für abhängig von a halten",
    bemerkung="Standardbezug: K1 III, K2 II, K3 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Sachaussage in Bayes-Term übersetzen und mit der Monotonie verketten. Typ wiederverwendet; wortgleich mit 2026-ga-B Stochastik WTR 1, 2c.")

row("2026MerhoehtBStochastikWTR1", "a", innen="3", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen", typ_neben="",
    stichwoerter="P(C = 20) = P(19,5 ≤ X ≤ 20,5) mit μ = 19, σ = 3 ≈ 12,5 %",
    voraussetzungen="Definition von C über Intervalle von X|Normalverteilung am Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Supermarkt/Treuepunkte", textumfang="mittel",
    gegeben="X normalverteilt mit μ = 19, σ = 3; P(C = k) = P(k − 0,5 ≤ X ≤ k + 0,5) für k ≥ 1",
    gesucht="P(C = 20)",
    verfahren="Intervallwahrscheinlichkeit der Normalverteilung",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(C = 20) = P(19,5 ≤ X ≤ 20,5) ≈ 12,5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P(X = 20) = 0 antworten",
    bemerkung="Standardbezug: K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erster Rechner-Typ zur Normalverteilung.")

row("2026MerhoehtBStochastikWTR1", "b", innen="3", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen", typ_neben="",
    stichwoerter="P(C = 1000) = P(999,5 ≤ X ≤ 1000,5) > 0, aber verschwindend klein (über 300 σ entfernt)",
    voraussetzungen="Normalverteilung ordnet jedem Intervall positive Wahrscheinlichkeit zu|Größenordnung ferner Werte",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Supermarkt/Treuepunkte", textumfang="lang",
    gegeben="C Anzahl der ausgegebenen Treuepunkte bei einem Einkauf von 95 bis 99,99 €; im Modell P(C = 1000) > 0",
    gesucht="Begründung, dass dies kein Argument gegen das Modell ist",
    verfahren="Wahrscheinlichkeit als verschwindend gering einordnen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="gemäß dem Modell ist die Wahrscheinlichkeit für diesen unrealistischen Fall verschwindend gering (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Modell wegen P > 0 verwerfen",
    bemerkung="Traegerbindung: Kontext (Treuepunkte je 5 € Warenwert erklären, warum 1000 unrealistisch ist). Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich.")

row("2026MerhoehtBStochastikWTR1", "c", innen="3", seite="3", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="Warenwert 95 bis 99,99 € entspricht 19 Treuepunkten|höchstens zwei Abweichung: 17 ≤ C ≤ 21|P(16,5 ≤ X ≤ 21,5) ≈ 59,5 % ≥ 50 %",
    voraussetzungen="Sollanzahl aus dem Warenwert|Abweichung als Intervall von C|Stetigkeitsübergang auf X",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Supermarkt/Treuepunkte", textumfang="lang",
    gegeben="Annahme: mit mindestens 50 % weicht die ausgegebene Anzahl von der dem Warenwert entsprechenden Anzahl um höchstens zwei ab; Einkauf 95 bis 99,99 €, ein Punkt je 5 €",
    gesucht="Beurteilung der Annahme",
    verfahren="Sollwert 19, Intervall 17 bis 21, Normalverteilung von 16,5 bis 21,5",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(17 ≤ C ≤ 21) = P(16,5 ≤ X ≤ 21,5) ≈ 59,5 %; die Annahme des Managements trifft bei dem betrachteten Einkauf zu (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Intervall 17 bis 21 ohne Stetigkeitskorrektur (≈ 49,5 %)",
    bemerkung="Traegerbindung: Kontext (Sollanzahl 19 nur aus Warenwert und Punkteregel). Standardbezug: K1 II, K2 III, K3 III, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Sachbedingung in ein Intervall von C und weiter in ein Intervall von X übersetzen.")

# ---- Stochastik WTR 2: Kraftfahrzeuge, Signifikanztest
ALTER = "Säulendiagramm der Anteile nach Alter: 0–4 Jahre 0,31, 5–9 0,26, 10–14 0,21, 15–19 0,13, 20–24 0,05, 25–29 0,02, mindestens 30 0,02"
row("2026MerhoehtBStochastikWTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X ~ B(200; 0,8), P(X ≤ 170) ≈ 0,972",
    voraussetzungen="kumulierte Verteilung am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kraftfahrzeuge/Statistik", textumfang="mittel",
    gegeben="80 % der Kraftfahrzeuge sind Pkw; 200 zufällig ausgewählt",
    gesucht="P(höchstens 170 Pkw)",
    verfahren="P(X ≤ 170) am Rechner",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="X Anzahl der Pkw; P(X ≤ 170) ≈ 0,972 (n = 200, p = 0,8) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X < 170)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2026MerhoehtBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="P(B) = 0,8, P(A) = 0,708, P(nicht A und nicht B) = 0,044|Felder 0,552, 0,248, 0,156, 0,044",
    voraussetzungen="Ränder und Differenzen",
    format="Tabelle", operator="Vervollständigen Sie", antwort="Tabelle",
    material="Tabelle", skizze="Vierfeldertafel A / nicht A gegen B / nicht B, nur 0,044 (nicht A und nicht B) und 1 eingetragen", kontext="Kraftfahrzeuge/Statistik", textumfang="mittel",
    gegeben="A: mindestens fünf Jahre alt (70,8 %); B: Pkw (80 %); P(nicht A und nicht B) = 0,044",
    gesucht="alle Felder der Vierfeldertafel",
    verfahren="Ränder eintragen, Felder als Differenzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="A und B 0,552, nicht A und B 0,248, A und nicht B 0,156, nicht A und nicht B 0,044; Ränder 0,8 / 0,2 und 0,708 / 0,292 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="0,044 als P(nicht A) lesen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2026MerhoehtBStochastikWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Anteile aus der Vierfeldertafel vergleichen", typ_neben="",
    stichwoerter="P(A | B) = 0,552/0,8 = 0,69|P(A | nicht B) = 0,156/0,2 = 0,78|unter den Pkw kleiner",
    voraussetzungen="zwei bedingte Wahrscheinlichkeiten aus der Tafel|Vergleich",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Tabelle", skizze="Vierfeldertafel aus b", kontext="Kraftfahrzeuge/Statistik", textumfang="kurz",
    gegeben="Vierfeldertafel aus b",
    gesucht="ob der Anteil der mindestens fünf Jahre alten Fahrzeuge unter den Pkw größer ist als unter den übrigen",
    verfahren="beide bedingten Anteile berechnen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2026MerhoehtBStochastikWTR2-1b",
    ergebnis="0,552/0,8 = 0,69; 0,156/0,2 = 0,78; somit ist der Anteil unter den Pkw kleiner als unter den übrigen Kraftfahrzeugen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Schnittanteile 0,552 und 0,156 direkt vergleichen",
    bemerkung="Standardbezug: K1 II, K3 I, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBStochastikWTR2", "d", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Lage- und Streumaße einer Stichprobe",
    typ="Medianklasse aus einem Säulendiagramm relativer Häufigkeiten begründen", typ_neben="",
    stichwoerter="kumuliert: 0,31 nach der ersten Klasse, 0,57 nach der zweiten|Median liegt in 5 bis 9 Jahre",
    voraussetzungen="Median als Mitte der sortierten Liste|kumulierte Anteile",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm", skizze=ALTER, kontext="Kraftfahrzeuge/Statistik", textumfang="mittel",
    gegeben="Anteile der Pkw nach sieben Altersklassen (Abbildung); Pkw, für den gleich viele jünger wie älter sind",
    gesucht="Altersklasse dieses Pkw mit Begründung",
    verfahren="Anteile bis 50 % aufsummieren",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="Jahre", abhaengig_von="",
    ergebnis="Zeitintervall 5 bis 9 Jahre; der Abbildung ist zu entnehmen, dass weniger als 50 % der Pkw ein Alter von 0 bis 4 Jahren haben, ein Alter von 0 bis 9 Jahren hingegen mehr als 50 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Klasse mit dem größten Anteil (0 bis 4) nennen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtBStochastikWTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Lage- und Streumaße einer Stichprobe",
    typ="Gewichtete Summe der Intervallgrenzen als Schranke des Mittelwerts deuten", typ_neben="",
    stichwoerter="Summanden: untere Intervallgrenze mal Anteil der Klassen ab 5 Jahren|Wert 7,45: untere Grenze für das Durchschnittsalter in Jahren",
    voraussetzungen="gewichtetes Mittel aus Klassen|untere Grenze, weil jede Klasse mit ihrer Untergrenze eingeht (erste Klasse mit 0)",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text",
    material="Diagramm", skizze=ALTER, kontext="Kraftfahrzeuge/Statistik", textumfang="mittel",
    gegeben="Term 5 · 0,26 + 10 · 0,21 + 15 · 0,13 + 20 · 0,05 + 25 · 0,02 + 30 · 0,02 und Abbildung 1",
    gesucht="Zusammenhang zwischen Term und Abbildung sowie Bedeutung des Werts",
    verfahren="Faktoren als Untergrenzen und Anteile erkennen, Wert als Mindestdurchschnitt deuten",
    schritte="2", zahlenraum="dezimal", einheiten="Jahre", abhaengig_von="",
    ergebnis="die Summanden sind jeweils das Produkt aus der unteren Intervallgrenze und dem zugehörigen Anteil der abgebildeten Zeitintervalle; der Wert des Terms ist eine untere Grenze für das durchschnittliche Alter der zugelassenen Pkw in Jahren (amtlich)",
    zwischenergebnis="7,45", niveau_geschaetzt="III",
    fehlerquelle="Wert als Durchschnittsalter statt als untere Grenze deuten",
    bemerkung="Standardbezug: K1 III, K3 II, K4 III, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) zwei Deutungen verkettet – Summanden als Grenze mal Anteil und Summe als Schranke des Mittelwerts.")

ABLEHN = "Koordinatensystem p von 0,7 bis 0,8 gegen Wahrscheinlichkeit 0 bis 0,25; fallende Kurve: bei p = 0,72 etwa 0,25, bei 0,73 etwa 0,16, bei 0,75 etwa 0,05, gegen 0 bei 0,8"
row("2026MerhoehtBStochastikWTR2", "a", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel eines linksseitigen Signifikanztests bestimmen", typ_neben="",
    stichwoerter="H0: p ≥ 0,75, n = 400, α = 5 %|Y ~ B(400; 0,75): P(Y ≤ 285) ≈ 4,86 %, P(Y ≤ 286) ≈ 6,10 %|Ablehnung bei weniger als 286",
    voraussetzungen="linksseitiger Test|größtes k mit P(Y ≤ k) ≤ α am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Fahrgemeinschaften/Signifikanztest", textumfang="lang",
    gegeben="Nullhypothese: Anteil der Alleinfahrenden mindestens 75 %; Signifikanzniveau 5 %; Stichprobe 400",
    gesucht="Entscheidungsregel",
    verfahren="kumulierte Binomialwahrscheinlichkeiten an der Grenze vergleichen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Y Anzahl der allein fahrenden Personen; P(Y ≤ 285) ≈ 4,86 %, P(Y ≤ 286) ≈ 6,10 % (n = 400, p = 0,75); befinden sich weniger als 286 allein fahrende Personen in der Stichprobe, so wird die Nullhypothese abgelehnt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="286 in den Ablehnungsbereich nehmen",
    bemerkung="Standardbezug: K2 II, K3 II, K4 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Hypothesentests.")

row("2026MerhoehtBStochastikWTR2", "b", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Fehler zweiter Art aus dem Graphen der Ablehnwahrscheinlichkeit ermitteln", typ_neben="",
    stichwoerter="Fehler 2. Art: H0 falsch (p < 0,75), aber nicht abgelehnt|für p = 0,73: Ablehnwahrscheinlichkeit ≈ 0,16, Fehler 2. Art ≈ 0,84",
    voraussetzungen="Fehler zweiter Art als Gegenwahrscheinlichkeit der Ablehnung bei falscher H0|p < 0,75 wählen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=ABLEHN, kontext="Fahrgemeinschaften/Signifikanztest", textumfang="lang",
    gegeben="Abbildung: Ablehnwahrscheinlichkeit in Abhängigkeit von p für festes n",
    gesucht="für ein geeignetes Beispiel die Wahrscheinlichkeit des Fehlers zweiter Art",
    verfahren="p < 0,75 wählen, Wert ablesen, 1 minus",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="wählt man beispielsweise p = 0,73, so beträgt die Wahrscheinlichkeit für den zugehörigen Fehler zweiter Art etwa 1 − 0,16 = 0,84 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="p ≥ 0,75 wählen (dann Fehler erster Art)",
    bemerkung="Standardbezug: K2 III, K4 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Ablesung). Eichregel: (d) Fehler zweiter Art als Gegenwahrscheinlichkeit der Ablehnung bei falscher Nullhypothese deuten, verkettet mit der Wahl eines zulässigen p.")

# ---- Stochastik WTR 3: Aufgabe 1 Dublette von WTR 2 (keine Zeile); Aufgabe 2 Konfidenzintervalle
KONF = "Abb. 2: 20 waagerechte Strecken (Konfidenzintervalle 1 bis 20) über einer p-Achse von 0,64 bis 0,8, Breite je etwa 0,08; Nummer 14 endet bei etwa 0,75, Nummer 13 liegt ganz rechts von 0,73"
row("2026MerhoehtBStochastikWTR3", "a", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Konfidenzintervall aus dem Diagramm identifizieren und Stichprobenergebnis aus der Grenze berechnen", typ_neben="",
    stichwoerter="Intervall Nummer 14 endet bei 0,75|h = 0,75 − 1,96 √(0,75 · 0,25/500) ≈ 0,712|Anzahl 0,712 · 500 ≈ 356",
    voraussetzungen="obere Grenze als p mit h = p − 1,96 σ_p|relative in absolute Häufigkeit",
    format="Rechnung", operator="Geben Sie an|Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=KONF, kontext="Fahrgemeinschaften/Konfidenzintervalle", textumfang="lang",
    gegeben="20 Konfidenzintervalle (95 %) aus Stichproben vom Umfang 500 nach |h − p| = 1,96 √(p(1 − p)/n); eines hat die obere Grenze 0,75",
    gesucht="Nummer dieses Intervalls und passende Anzahl der Alleinfahrenden in der Stichprobe",
    verfahren="Intervall ablesen, h aus der Grenzgleichung, mal 500",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="Nummer des Konfidenzintervalls: 14; (0,75 − 1,96 · √(0,75 · 0,25/500)) · 500 ≈ 356; Anzahl der Personen: 356 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="0,75 · 500 = 375 als Anzahl nehmen",
    bemerkung="Traegerbindung: Kontext (Zuordnung der Nummer nur aus Abbildung 2). Standardbezug: K2 I, K3 I, K4 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Thema ersatzweise Hypothesentests (Konfidenzintervalle haben keine Themenzeile).")

row("2026MerhoehtBStochastikWTR3", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben", typ_neben="",
    stichwoerter="p = 0,73 liegt in allen Intervallen außer Nummer 13",
    voraussetzungen="verträglich heißt vom Intervall überdeckt|Senkrechte im Diagramm",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl",
    material="Diagramm", skizze=KONF, kontext="Fahrgemeinschaften/Konfidenzintervalle", textumfang="kurz",
    gegeben="Abbildung 2 mit 20 Konfidenzintervallen",
    gesucht="ein p, das mit genau 19 der 20 Ergebnisse verträglich ist, mit Begründung",
    verfahren="Senkrechte suchen, die genau 19 Intervalle schneidet",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="für p = 0,73 ist der Abbildung zu entnehmen, dass alle Konfidenzintervalle bis auf das mit der Nummer 13 diesen Wert von p überdecken (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="p wählen, das alle 20 Intervalle trifft",
    bemerkung="Traegerbindung: Kontext (nur mit Abbildung 2 lösbar). Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich. Thema ersatzweise Hypothesentests.")

row("2026MerhoehtBStochastikWTR3", "c", innen="2", seite="3", punkte="3", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen", typ_neben="",
    stichwoerter="jedes Intervall überdeckt p mit etwa 95 %, unabhängig|Y ~ B(20; 0,95)|P(Y = 19) ≈ 0,38 < 0,42",
    voraussetzungen="Sicherheitswahrscheinlichkeit als Trefferwahrscheinlichkeit|Bernoulli-Kette|Einzelwahrscheinlichkeit am Rechner",
    format="Begründung|Rechnung", operator="Geben Sie an|Erläutern Sie|Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Fahrgemeinschaften/Konfidenzintervalle", textumfang="lang",
    gegeben="20 weitere Stichproben (n = 500), Konfidenzintervalle zu 95 %, p konstant; Y Anzahl der Intervalle, die p überdecken; Aussage: P(genau 19) < 42 %",
    gesucht="Verteilung von Y mit Erläuterung und Nachweis der Aussage",
    verfahren="Y binomialverteilt mit n = 20, q = 0,95; P(Y = 19) berechnen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="für jedes Konfidenzintervall hat die Wahrscheinlichkeit, p zu überdecken, etwa den Wert der Sicherheitswahrscheinlichkeit; daher kann Y als binomialverteilt mit n = 20 und q = 0,95 angenommen werden; P(Y = 19) ≈ 0,38 < 0,42 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="P(Y ≥ 19) statt P(Y = 19)",
    bemerkung="Standardbezug: K1 III, K2 II, K3 III, K5 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Sicherheitswahrscheinlichkeit als Trefferwahrscheinlichkeit einer Bernoulli-Kette deuten, verkettet mit der Binomialrechnung. Thema ersatzweise Hypothesentests. Aufgabe 1 dieser Datei ist wortgleich mit Stochastik WTR 2, Aufgabe 1 (Dublette, keine Zeile, Soll 8).")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Scharparameter aus einem Punkt bestimmen und Wendepunkt nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameter einer Schar aus einem Punkt des Graphen berechnen und nachweisen, dass dieser Punkt Wendepunkt ist (f'' = 0, f''' ≠ 0).",
     "2026MerhoehtBAnalysisWTR1-1a"),
    ("Gemeinsame Punkte aller Graphen einer Schar bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Zeigen, dass alle Graphen einer Schar genau bestimmte Punkte gemeinsam haben, indem zwei Scharfunktionen gleichgesetzt werden und der Parameter herausfällt.",
     "2026MerhoehtBAnalysisWTR1-1b"),
    ("Tangentenabschnitt auf der x-Achse als Quotient f/f' am Graphen begründen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Mit Eintragungen im Steigungsdreieck begründen, dass der Abstand zwischen dem Lotfußpunkt eines Graphenpunkts und dem Schnittpunkt seiner Tangente mit der x-Achse gleich f(u)/f'(u) ist.",
     "2026MerhoehtBAnalysisWTR1-1d"),
    ("Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten", "Analysis", "Rekonstruktion von Beständen",
     "Ein bestimmtes Integral über eine Ratenfunktion berechnen und den Wert als im Zeitraum umgesetzte Menge mit Einheit deuten.",
     "2026MerhoehtBAnalysisWTR1-2b"),
    ("Transformation: Graphen einer periodischen Funktion mit vorgegebenem Maximum und Periode skizzieren", "Analysis", "Funktionsklassen und Eigenschaften",
     "In ein vorhandenes Koordinatensystem einen periodischen Graphen mit vorgegebenem Maximalwert und vorgegebener Periode (als Vielfaches einer gegebenen) skizzieren.",
     "2026MerhoehtBAnalysisWTR1-2c"),
    ("Positivität, y-Achsenabschnitt und Steigung einer Schar begründen und berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Für eine Schar aus e-Termen begründen, dass alle Graphen oberhalb der x-Achse liegen, und Achsenschnittpunkt und Steigung dort in Abhängigkeit vom Parameter angeben.",
     "2026MerhoehtBAnalysisWTR2-1a"),
    ("Scharparameter den Graphen über den y-Achsenabschnitt zuordnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Abgebildete Graphen einer Schar den Parameterwerten zuordnen, indem der parameterabhängige y-Achsenabschnitt geordnet wird.",
     "2026MerhoehtBAnalysisWTR2-1b"),
    ("Verschobene Scharfunktion als gerade Funktion nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Rechnerisch zeigen, dass die um einen parameterabhängigen Wert verschobene Scharfunktion einen symmetrischen Term hat (Potenzgesetze mit ln), und die Achsensymmetrie nachweisen.",
     "2026MerhoehtBAnalysisWTR2-1c"),
    ("Symmetrieachse einer Scharkurve aus der Verschiebung einer geraden Funktion begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Begründen, dass jeder Graph einer Schar achsensymmetrisch ist, weil er aus einer geraden Funktion durch Verschiebung entsteht, und die Achse in Abhängigkeit vom Parameter angeben.",
     "2026MerhoehtBAnalysisWTR2-1d"),
    ("Fläche: Flächeninhalt einer Vorderansicht als Integral mit Maßstab und Abzug berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Den realen Flächeninhalt einer modellierten Figur über ein Integral berechnen, mit dem quadratischen Maßstab umrechnen und vorgegebene Teilflächen abziehen.",
     "2026MerhoehtBAnalysisWTR2-2b"),
    ("Winkel zwischen Graph und senkrechter Kante über die Ableitung berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Winkel zwischen einem Graphen und einer senkrechten Geraden an ihrem Treffpunkt aus dem Steigungswinkel der Tangente berechnen.",
     "2026MerhoehtBAnalysisWTR2-2c"),
    ("Abstand eines Punktes von einem Graphen über die Normalenbedingung deuten", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Eine vorgelegte Rechnung deuten, in der der nächstgelegene Graphenpunkt über die Orthogonalität von Verbindungsstrecke und Tangente bestimmt und der Abstand berechnet wird.",
     "2026MerhoehtBAnalysisWTR2-2d"),
    ("Monotonie, Nullstelle und Grenzwert einer e-Funktion am Term begründen", "Analysis", "Grenzwerte und Verhalten im Unendlichen",
     "Für eine gestreckte und verschobene e-Funktion Monotonie und Nullstelle am Term begründen und den Grenzwert für x → ∞ angeben.",
     "2026MerhoehtBAnalysisWTR3-1a"),
    ("Bestimmtes Integral mit vorgegebener Stammfunktion berechnen", "Analysis", "Stammfunktion und Hauptsatz",
     "Ein bestimmtes Integral über den Hauptsatz mit einer vorgegebenen Stammfunktion berechnen.",
     "2026MerhoehtBAnalysisWTR3-1b"),
    ("Integralwert: Eindeutige Lösung einer Flächengleichung über die Monotonie des Flächeninhalts begründen", "Analysis", "Flächeninhalt durch Integration",
     "Ohne Stammfunktion begründen, dass eine Gleichung zwischen einer festen Fläche und einer mit der Grenze wachsenden Fläche genau eine Lösung hat.",
     "2026MerhoehtBAnalysisWTR3-1c"),
    ("Aufgabenstellung zu einem Rotationsvolumen-Anteil aus dem Lösungsweg formulieren", "Analysis", "Rotationsvolumen",
     "Zu einem vorgelegten Lösungsweg mit Rotationsvolumen und Zylindervolumen die passende Aufgabenstellung angeben.",
     "2026MerhoehtBAnalysisWTR3-1d"),
    ("Definitionsbereich der Umkehrfunktion angeben und ihren Term nachweisen", "Analysis", "Umkehrfunktion",
     "Den Definitionsbereich der Umkehrfunktion als Wertemenge der Funktion angeben und den Term der Umkehrfunktion durch Auflösen nachweisen.",
     "2026MerhoehtBAnalysisWTR3-1e"),
    ("Berührpunkt der Tangente mit vorgegebener Steigung berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Punkt berechnen, in dem die Tangente eine vorgegebene Steigung hat (f'(x) = m lösen, Funktionswert).",
     "2026MerhoehtBAnalysisWTR3-1f"),
    ("Tangente an Funktion und Umkehrfunktion über die Spiegelung an y = x begründen", "Analysis", "Umkehrfunktion",
     "Begründen, dass eine Tangente mit Steigung −1 auch den Graphen der Umkehrfunktion berührt, weil beide an y = x gespiegelt in sich bzw. ineinander übergehen.",
     "2026MerhoehtBAnalysisWTR3-1g"),
    ("Flächeninhalt eines Vierecks aus Berührpunkten und Spiegelpunkten als Trapez begründen", "Analysis", "Umkehrfunktion",
     "Ein zu y = x symmetrisches Viereck aus Berührpunkt, Spiegelpunkt und zwei weiteren Punkten einzeichnen und seinen Flächeninhalt über Trapezformel und 45°-Dreieck begründen.",
     "2026MerhoehtBAnalysisWTR3-1h"),
    ("Verbindungsvektor zweier Kantenmittelpunkte als Linearkombination der Kantenvektoren angeben", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Die Strecke zwischen zwei Kantenmittelpunkten eines Quaders einzeichnen und ihren Vektor als Linearkombination der aufspannenden Vektoren angeben.",
     "2026MerhoehtBAGLAA1WTR-1a"),
    ("Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Volumen berechnen", "Analytische Geometrie", "Orthogonalität",
     "Die unbekannte Höhe eines Quaders aus dem verschwindenden Skalarprodukt zweier Raumdiagonalen bestimmen und das Volumen berechnen.",
     "2026MerhoehtBAGLAA1WTR-1b"),
    ("Verflechtung: Gesamtmatrix im Sachzusammenhang deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Das Produkt zweier Bedarfsmatrizen als direkte Zuordnung von Endproduktmengen zu Rohstoffmengen beschreiben.",
     "2026MerhoehtBAGLAA1WTR-2b"),
    ("Verflechtung: Maximale Produktionsmenge aus dem Rohstoffvorrat ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus einem Rohstoffvorrat die maximal herstellbare Menge eines Endprodukts über den knappsten Rohstoff (Spalte der Gesamtmatrix) ermitteln.",
     "2026MerhoehtBAGLAA1WTR-2c"),
    ("Verflechtung: Maximale Kostensteigerung eines Rohstoffs aus einer Kostenschranke bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Die Rohstoffkosten je Produkteinheit heute und nach mehreren Jahren exponentiellen Preisanstiegs aufstellen und aus einer Kostenschranke den maximalen Wachstumsfaktor eines Rohstoffs bestimmen.",
     "2026MerhoehtBAGLAA1WTR-2d"),
    ("Ebene Figur: Parallelogramm als Rechteck über das Skalarprodukt nachweisen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Zeigen, dass ein Parallelogramm ein Rechteck ist, indem das Skalarprodukt zweier benachbarter Seitenvektoren null ist.",
     "2026MerhoehtBAGLAA2WTR1-1a"),
    ("Komponente des Normalenvektors aus der Orthogonalität zur Koordinatenebene begründen", "Analytische Geometrie", "Ebenen",
     "Ohne Rechnung begründen, dass eine Komponente des Normalenvektors null ist, weil die Ebene senkrecht zu einer Koordinatenebene steht.",
     "2026MerhoehtBAGLAA2WTR1-1c"),
    ("Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Den Winkel zwischen einer Ebene und einer Koordinatenebene über die Normalenvektoren berechnen.",
     "2026MerhoehtBAGLAA2WTR1-1d"),
    ("Ebene Figur: Teilverhältnis auf einer Kante deuten und Teilfläche eines Rechtecks berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Einen vorgegebenen Parameterwert als Teilverhältnis auf einer Kante im Sachzusammenhang deuten und den Inhalt der entsprechenden Teilfläche eines Rechtecks berechnen.",
     "2026MerhoehtBAGLAA2WTR1-1e"),
    ("Übereinstimmung einer Ebene mit einer Koordinatenebene beurteilen", "Analytische Geometrie", "Ebenen",
     "Beurteilen, ob eine durch eine Gleichung gegebene Ebene mit einer Koordinatenebene (etwa einer Symmetrieebene) übereinstimmt.",
     "2026MerhoehtBAGLAA2WTR1-1f"),
    ("Sprungweite als Abstand zweier Punkte einer Parameterkurve in der Grundebene berechnen", "Analytische Geometrie", "Abstände",
     "Aus einer Parameterdarstellung einer Flugkurve den Auftreffpunkt (z = 0) und den Lotfußpunkt des Absprungs bestimmen und ihren Abstand als Weite berechnen.",
     "2026MerhoehtBAGLAA2WTR1-1g"),
    ("Körper: Trapezgrundfläche nachweisen und Pyramidenvolumen berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Die Grundfläche einer Pyramide als Trapez nachweisen (kollineare Seiten) und das Volumen über Trapezfläche und Höhe berechnen.",
     "2026MerhoehtBAGLAA2WTR2-1a"),
    ("Gerade und Ebene: Kreisbahn einer Drehung um eine Kante als Kreis in einer Ebene mit Mittelpunkt begründen", "Analytische Geometrie", "Lagebeziehungen",
     "Begründen, dass ein bei Drehung um eine Kante bewegter Punkt einen Kreis in der zur Kante senkrechten Ebene durch den Punkt beschreibt, mit dem Schnittpunkt von Kante und Ebene als Mittelpunkt.",
     "2026MerhoehtBAGLAA2WTR2-1d"),
    ("Existenz eines Kreispunkts mit vorgegebener Koordinate über den Radius widerlegen", "Analytische Geometrie", "Abstände",
     "Eine Aussage über einen Kreispunkt mit vorgegebener Koordinate widerlegen, indem der Punkt in der Kreisebene angesetzt und sein Abstand zum Mittelpunkt mit dem Radius verglichen wird.",
     "2026MerhoehtBAGLAA2WTR2-1e"),
    ("Absolute Anzahl aus einer Pfadwahrscheinlichkeit mit einer Schranke vergleichen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Aus einer Pfadwahrscheinlichkeit und einer Gesamtzahl entscheiden, ob eine absolute Anzahl eine Schranke unterschreitet.",
     "2026MerhoehtBStochastikWTR1-2a"),
    ("Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Für eine normalverteilte Zufallsgröße die Wahrscheinlichkeit eines Intervalls mit dem Rechner berechnen, etwa als Näherung einer diskreten Zufallsgröße.",
     "2026MerhoehtBStochastikWTR1-3a"),
    ("Vernachlässigbare Wahrscheinlichkeit eines unrealistischen Werts als Modellargument begründen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Begründen, dass eine positive, aber verschwindend kleine Wahrscheinlichkeit eines unrealistischen Werts kein Argument gegen ein Normalverteilungsmodell ist.",
     "2026MerhoehtBStochastikWTR1-3b"),
    ("Wahrscheinlichkeit einer Abweichung um höchstens k über die Normalverteilung mit einer Schranke vergleichen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Eine Sachbedingung „weicht um höchstens k ab“ in ein Intervall übersetzen, seine Wahrscheinlichkeit über die Normalverteilung berechnen und mit einer Schranke vergleichen.",
     "2026MerhoehtBStochastikWTR1-3c"),
    ("Bedingte Anteile aus der Vierfeldertafel vergleichen", "Stochastik", "Bedingte Wahrscheinlichkeit und Bayes",
     "Zwei bedingte Wahrscheinlichkeiten aus einer Vierfeldertafel berechnen und vergleichen.",
     "2026MerhoehtBStochastikWTR2-1c"),
    ("Medianklasse aus einem Säulendiagramm relativer Häufigkeiten begründen", "Stochastik", "Lage- und Streumaße einer Stichprobe",
     "Aus einem Säulendiagramm klassierter Anteile die Klasse angeben, in der der Median liegt, über kumulierte Anteile.",
     "2026MerhoehtBStochastikWTR2-1d"),
    ("Gewichtete Summe der Intervallgrenzen als Schranke des Mittelwerts deuten", "Stochastik", "Lage- und Streumaße einer Stichprobe",
     "Eine Summe aus Intervallgrenzen mal Klassenanteilen mit dem Diagramm in Beziehung setzen und ihren Wert als untere oder obere Grenze des Mittelwerts deuten.",
     "2026MerhoehtBStochastikWTR2-1e"),
    ("Entscheidungsregel eines linksseitigen Signifikanztests bestimmen", "Stochastik", "Hypothesentests",
     "Für eine Nullhypothese p ≥ p0 die Entscheidungsregel bestimmen: größtes k mit P(Y ≤ k) ≤ α über kumulierte Binomialwahrscheinlichkeiten.",
     "2026MerhoehtBStochastikWTR2-2a"),
    ("Fehler zweiter Art aus dem Graphen der Ablehnwahrscheinlichkeit ermitteln", "Stochastik", "Hypothesentests",
     "Für ein selbst gewähltes p, bei dem die Nullhypothese falsch ist, die Wahrscheinlichkeit des Fehlers zweiter Art als Gegenwahrscheinlichkeit der abgelesenen Ablehnwahrscheinlichkeit ermitteln.",
     "2026MerhoehtBStochastikWTR2-2b"),
    ("Konfidenzintervall aus dem Diagramm identifizieren und Stichprobenergebnis aus der Grenze berechnen", "Stochastik", "Hypothesentests",
     "Unter abgebildeten Konfidenzintervallen das mit vorgegebener Grenze finden und aus der Grenzgleichung die absolute Häufigkeit der Stichprobe berechnen.",
     "2026MerhoehtBStochastikWTR3-2a"),
    ("Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben", "Stochastik", "Hypothesentests",
     "Im Diagramm mehrerer Konfidenzintervalle einen Wert angeben, der von genau k Intervallen überdeckt wird.",
     "2026MerhoehtBStochastikWTR3-2b"),
    ("Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen", "Stochastik", "Hypothesentests",
     "Die Anzahl der Konfidenzintervalle, die den wahren Anteil überdecken, als binomialverteilt mit der Sicherheitswahrscheinlichkeit begründen und eine Wahrscheinlichkeit dazu berechnen.",
     "2026MerhoehtBStochastikWTR3-2c"),
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
