# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.6 · 14.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.7

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

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
    "stapel": "2026-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2026MgrundlegendBAnalysisWTR1": 25,
        "2026MgrundlegendBAnalysisWTR2": 25,
        "2026MgrundlegendBAGLAA1WTR": 15,
        "2026MgrundlegendBAGLAA2WTR1": 15,
        "2026MgrundlegendBAGLAA2WTR2": 15,
        "2026MgrundlegendBStochastikWTR1": 15,
        "2026MgrundlegendBStochastikWTR2": 15,
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
# Probestapel Teil B, WTR-Zweig. Ein Eintrag je Teilaufgabe; innen = Aufgabennummer in der Datei
# (Dateien mit nur einer, unnummerierten Aufgabe: innen = "1").
# niveau_geschaetzt nach der Deutungsliste v0.7; bei III nennt bemerkung den Eintrag.
# Messung Trägerbindung in bemerkung: „frei" (Zeile ohne die Trägeraufgabe beschreibbar, Stamm in gegeben
# wiederholt) oder „Kontext" (ohne den Sachkontext der Trägeraufgabe nicht beschreibbar).
# Standardbezug in Teil B mit eigener Spalte Anforderungsbereich; in bemerkung als „AB amtlich: …".

SOLL = {"2026MgrundlegendBAnalysisWTR1": 25, "2026MgrundlegendBAnalysisWTR2": 25, "2026MgrundlegendBAGLAA1WTR": 15,
        "2026MgrundlegendBAGLAA2WTR1": 15, "2026MgrundlegendBAGLAA2WTR2": 15, "2026MgrundlegendBStochastikWTR1": 15,
        "2026MgrundlegendBStochastikWTR2": 15}

# ---- Analysis WTR 1, Aufgabe 1: f(x) = 1/4 x³ + 1/4
G1 = ("Koordinatensystem mit Gitter, x von −2 bis 2, y von −1 bis 3; Graph G von 1/4 x³ + 1/4 monoton steigend "
      "durch (−1; 0) und (0; 0,25), bei 2 etwa 2,25; beschriftet G")
row("2026MgrundlegendBAnalysisWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Monotonie über das Vorzeichen der Ableitung am Term nachweisen", typ_neben="",
    stichwoerter="f'(x) = 3/4 x² ≥ 0 für alle x|monoton steigend",
    voraussetzungen="Ableitung|Quadrat nichtnegativ|Monotoniekriterium",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=G1, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/4 x³ + 1/4 in IR, Graph G",
    gesucht="Nachweis, dass G monoton steigend ist",
    verfahren="f' bilden, Vorzeichen begründen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="für alle x ∈ IR gilt f'(x) = 3/4 x² ≥ 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="f'(0) = 0 als Gegenargument werten",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Abbildung zwischen zwei Graphen angeben", typ_neben="",
    stichwoerter="Streckung mit Faktor 1/4 in y-Richtung|Verschiebung um 1/4 in positive y-Richtung",
    voraussetzungen="Faktor als Streckung, Summand als Verschiebung",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=G1, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/4 x³ + 1/4; u(x) = x³",
    gesucht="Beschreibung, wie G aus dem Graphen von u entsteht",
    verfahren="Term als Streckung und Verschiebung von x³ lesen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="G kann aus dem Graphen von u durch eine Streckung mit dem Faktor 1/4 in y-Richtung und eine anschließende Verschiebung um 1/4 in positive y-Richtung erzeugt werden (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Reihenfolge vertauschen (erst verschieben, dann strecken ergibt 1/4 x³ + 1/16)",
    bemerkung="Standardbezug: K1 II, K6 II. AB amtlich: II. Amtlich. Typ wiederverwendet (2026-ea-A). Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR1", "c", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung und Schnittwinkel der Tangente mit der x-Achse bestimmen", typ_neben="",
    stichwoerter="f'(3) = 27/4|y-Achsenabschnitt −53/4 vorgegeben: y = 27/4 x − 53/4|tan α = 27/4, α ≈ 81,6°",
    voraussetzungen="Ableitung als Steigung|Tangentengleichung|Steigungswinkel über den Tangens",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Koordinatensystem", skizze=G1, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 1/4 x³ + 1/4; Tangente in (3 | f(3)) schneidet die y-Achse in (0 | −53/4)",
    gesucht="Gleichung der Tangente und Winkel, unter dem sie die x-Achse schneidet",
    verfahren="Steigung f'(3), Gleichung mit Achsenabschnitt, Winkel aus tan α = m",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="f'(3) = 27/4; Gleichung der Tangente: y = 27/4 x − 53/4; tan α = 27/4 liefert α ≈ 81,6° (amtlich)",
    zwischenergebnis="f(3) = 7",
    niveau_geschaetzt="II",
    fehlerquelle="Winkel im Bogenmaß angeben oder arctan der Ableitung falsch eintippen",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Geschätzt II als Verkettung Ableitung, Gleichung, Winkel; amtlich I – in Teil B gilt die Verkettung dreier Standardschritte als Reproduktion. Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR1", "d", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion mit einer Wertebedingung bestimmen", typ_neben="",
    stichwoerter="F(x) = 1/16 x⁴ + 1/4 x + c|F(4) = 16 ⇔ 16 + 1 + c = 16 ⇔ c = −1",
    voraussetzungen="Potenzregel rückwärts|Konstante aus dem Punkt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/4 x³ + 1/4; Punkt (4 | 16) auf dem Graphen der Stammfunktion",
    gesucht="Term dieser Stammfunktion",
    verfahren="allgemeine Stammfunktion, c aus F(4) = 16",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="ein Term der gesuchten Stammfunktion hat die Form F(x) = 1/16 x⁴ + 1/4 x + c; F(4) = 16 ⇔ c = −1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Integrationskonstante vergessen",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-A). Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral über die Summe aus ungerader Funktion und Konstante ohne Stammfunktion begründen", typ_neben="",
    stichwoerter="∫ 1/4 x³ über [−k; k] = 0 wegen Punktsymmetrie zum Ursprung|∫ 1/4 dx über [−k; k] = Rechteck 2k · 1/4",
    voraussetzungen="Zerlegung des Integrals als Summe (vorgegeben)|Punktsymmetrie von x³|Integral einer Konstanten als Rechteckinhalt",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 1/4 x³ + 1/4; k > 0; Zerlegung ∫_{−k}^{k} f = ∫_{−k}^{k} 1/4 x³ + ∫_{−k}^{k} 1/4 vorgegeben",
    gesucht="Begründung ohne Stammfunktionen, dass ∫_{−k}^{k} f(x) dx = 2k · 1/4",
    verfahren="ersten Summanden über die Symmetrie null setzen, zweiten als Rechteck deuten",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="∫_{−k}^{k} 1/4 x³ dx = 0, da der Graph von x ↦ 1/4 x³ symmetrisch bezüglich des Koordinatenursprungs ist; der Wert des Integrals ∫_{−k}^{k} 1/4 dx kann als Flächeninhalt eines Rechtecks mit den Seitenlängen 2k und 1/4 interpretiert werden (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="doch mit Stammfunktion rechnen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Punktsymmetrie erkennen, verkettet mit der Deutung des Integrals als Rechteckinhalt. Vom Typ „Integralwert: Integral null über die Punktsymmetrie begründen“ getrennt: hier zusätzlich der konstante Anteil. Trägerbindung: frei.")

KREIS = ("Koordinatensystem ohne Skalen; Parabel (Graph von f' = 3/4 x²) mit Scheitel im Ursprung, beschriftet „Graph von f'“; "
         "Kreis mit Mittelpunkt (Kreuz) auf der y-Achse, der die Parabel in zwei Punkten berührt, rechter Berührpunkt A markiert")
row("2026MgrundlegendBAnalysisWTR1", "f", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Mittelpunkt eines den Graphen berührenden Kreises über die Normale im Berührpunkt bestimmen", typ_neben="",
    stichwoerter="Mittelpunkt liegt auf der Normalen an f' in A|f''(1) = 3/2|Normale y = −2/3 x + n durch A(1; 3/4): n = 17/12|Schnitt mit der y-Achse: y = 17/12",
    voraussetzungen="Berührung: Radius senkrecht zur Tangente|Ableitung von f' (also f'')|Normalensteigung −1/m|Achsenschnitt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=KREIS, kontext="ohne", textumfang="mittel",
    gegeben="f'(x) = 3/4 x²; Kreis mit Mittelpunkt auf der y-Achse berührt den Graphen von f' in genau zwei Punkten, einer davon A(1 | 3/4)",
    gesucht="y-Koordinate des Mittelpunkts, rechnerisch",
    verfahren="Normale an den Graphen von f' in A aufstellen, Schnitt mit der y-Achse",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Steigung der Tangente an den Graphen von f' in A: f''(1) = 3/2; Gleichung der Normale in A: y = −2/3 x + n, 3/4 = −2/3 + n ⇔ n = 17/12; y-Koordinate 17/12 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="f' statt f'' als Steigung nehmen oder Tangente statt Normale ansetzen",
    bemerkung="Standardbezug: K2 III, K4 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „Kreis berührt“ in „Mittelpunkt auf der Normalen im Berührpunkt“ übersetzen, verkettet mit Ableitung und Normalengleichung. Trägerbindung: frei.")

# ---- Analysis WTR 1, Aufgabe 2: Luftvolumen h(x) = 1/6 cos(2π/3 x) + 8/3
LUNGE = ("Koordinatensystem mit Gitter, x von 0 bis 8 (Sekunden), y von 0 bis 3 (Liter); Graph von h als flache Kosinuswelle "
         "um y ≈ 2,67 mit Amplitude 1/6 und Periode 3, Maximum bei 0, 3, 6")
row("2026MgrundlegendBAnalysisWTR1", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="h(2,5) = 1/6 · cos(5π/3) + 8/3 = 1/12 + 8/3 = 11/4|2,75 Liter",
    voraussetzungen="Einsetzen, Bogenmaß am Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=LUNGE, kontext="Atmung/Luftvolumen", textumfang="lang",
    gegeben="h(x) = 1/6 · cos(2π/3 · x) + 8/3, x Zeit in Sekunden ab Beobachtungsbeginn, h(x) Luftvolumen in Litern",
    gesucht="Luftvolumen 2,5 Sekunden nach Beobachtungsbeginn",
    verfahren="h(2,5) berechnen",
    schritte="1", zahlenraum="Bruch|dezimal", einheiten="Liter|Sekunden", abhaengig_von="",
    ergebnis="h(2,5) = 11/4; Luftvolumen 2,75 Liter (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Rechner im Gradmaß",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei (Term und Deutung der Variablen in gegeben).")

row("2026MgrundlegendBAnalysisWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Periode einer Kosinusfunktion im Sachzusammenhang deuten und Stelle stärkster Zunahme am Graphen angeben", typ_neben="",
    stichwoerter="Periode 2π/(2π/3) = 3 Sekunden je Atemzyklus|60/3 = 20 Zyklen pro Minute|stärkste Zunahme an der steigenden Wendestelle, z. B. x = 2,25",
    voraussetzungen="Periode aus dem Faktor im Argument|Zyklus als Periode deuten|Wendestelle als Stelle größter Steigung am Graphen",
    format="Rechnung|Kurzantwort", operator="Bestimmen Sie|Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=LUNGE, kontext="Atmung/Luftvolumen", textumfang="mittel",
    gegeben="h(x) = 1/6 · cos(2π/3 · x) + 8/3; ein Atemzyklus ist ein vollständiger Aus- und Einatmungsvorgang; Abbildung des Graphen",
    gesucht="Anzahl der Atemzyklen pro Minute und ein Zeitpunkt stärkster Zunahme des Luftvolumens",
    verfahren="Periode berechnen und auf 60 s beziehen, Wendestelle im steigenden Ast ablesen",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="Sekunden|Minute", abhaengig_von="",
    ergebnis="Anzahl 60/3 = 20; Zeitpunkt 2,25 Sekunden nach Beobachtungsbeginn (amtlich)",
    zwischenergebnis="ebenso 5,25, 8,25 …",
    niveau_geschaetzt="II",
    fehlerquelle="Maximum statt Wendestelle als stärkste Zunahme nennen",
    bemerkung="Standardbezug: K3 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Trägerbindung: Kontext (Atemzyklus als Periode und Einatmen als Zunahme sind nur aus dem Sachtext zu verstehen).")

row("2026MgrundlegendBAnalysisWTR1", "c", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Differenz und Differenzenquotient im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="h(3) − h(1,5): Zunahme des Luftvolumens beim Einatmen (von 1,5 bis 3 s) in Litern|(h(3) − h(1,5))/1,5: durchschnittliche Zunahme in Litern pro Sekunde",
    voraussetzungen="Differenz als absolute Änderung|Differenzenquotient als mittlere Änderungsrate|erster Zyklus: Ausatmen 0 bis 1,5, Einatmen 1,5 bis 3",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=LUNGE, kontext="Atmung/Luftvolumen", textumfang="mittel",
    gegeben="h wie in a; erster Atemzyklus (0 bis 3 Sekunden, Minimum bei 1,5); Terme I h(3) − h(1,5) und II (h(3) − h(1,5))/1,5",
    gesucht="Bedeutung beider Terme im Sachzusammenhang",
    verfahren="Differenz und Differenzenquotient auf das Einatmen beziehen",
    schritte="2", zahlenraum="dezimal", einheiten="Liter|Sekunden", abhaengig_von="",
    ergebnis="I: Zunahme des Luftvolumens in der Lunge beim Einatmen in Litern; II: durchschnittliche Zunahme des Luftvolumens in der Lunge beim Einatmen in Litern pro Sekunde (amtlich)",
    zwischenergebnis="I = 1/3, II = 2/9",
    niveau_geschaetzt="II",
    fehlerquelle="II als momentane Änderungsrate deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Je Term eine Deutung, nicht verkettet – (d) feuert nicht. Trägerbindung: Kontext.")

# ---- Analysis WTR 2, Aufgabe 1: f(x) = 3e^x + 1
EXP = ("Koordinatensystem mit Gitter, x von −3 bis 2, y von 0 bis 6; Graph Gf von 3e^x + 1, links gegen y = 1, "
       "durch (0; 4), steil steigend; in Abb. 2 zusätzlich Fläche zwischen Gf, y = 1, x = u (u < 0) und der y-Achse schraffiert")
row("2026MgrundlegendBAnalysisWTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstellenfreiheit und Wertemenge einer e-Funktion aus dem Term begründen", typ_neben="",
    stichwoerter="e^x > 0 ⇒ 3e^x + 1 > 1 > 0|Wertemenge ]1; ∞[",
    voraussetzungen="Positivität der e-Funktion|Wertemenge über die Verschiebung",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=EXP, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3e^x + 1 in IR",
    gesucht="Begründung am Term, dass Gf die x-Achse nicht schneidet, und Wertemenge",
    verfahren="e^x > 0 nutzen",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="für alle x ∈ IR gilt e^x > 0 und damit 3e^x + 1 > 0; Wertemenge ]1; +∞[ (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Wertemenge mit 1 einschließen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen", typ_neben="",
    stichwoerter="f(0) = 4, f'(x) = 3e^x, f'(0) = 3|y = 3x + 4",
    voraussetzungen="Schnittpunkt mit der y-Achse bei x = 0|Ableitung der e-Funktion",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3e^x + 1; Tangente t im Schnittpunkt von Gf mit der y-Achse; Kontrolle y = 3x + 4",
    gesucht="Gleichung von t",
    verfahren="f(0), f'(0), Gleichung",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f(0) = 4; f'(x) = 3e^x; f'(0) = 3; Gleichung der Tangente: y = 3x + 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="f'(0) = 3e⁰ = 0 rechnen",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-A). Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen", typ_neben="",
    stichwoerter="Nullstelle der Tangente −4/3, y-Achsenabschnitt 4|Hypotenuse √(16 + 16/9) = 4/3 √10|Umfang 16/3 + 4/3 √10 ≈ 9,55",
    voraussetzungen="Achsenschnittpunkte der Tangente|Pythagoras|Summe der Seiten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Tangente t: y = 3x + 4 (aus b)",
    gesucht="Umfang des Dreiecks aus t und den Koordinatenachsen",
    verfahren="Achsenabschnitte, Hypotenuse, Summe",
    schritte="3", zahlenraum="Bruch|Wurzel|negativ", einheiten="", abhaengig_von="2026MgrundlegendBAnalysisWTR2-1b",
    ergebnis="0 = 3x + 4 ⇔ x = −4/3; Umfang des Dreiecks: 4/3 + 4 + √(4² + (4/3)²) = 16/3 + 4/3 √10 (amtlich)",
    zwischenergebnis="≈ 9,55",
    niveau_geschaetzt="II",
    fehlerquelle="Flächeninhalt statt Umfang berechnen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Umfang des Dreiecks aus zwei Tangenten und der x-Achse berechnen“ getrennt (eine Tangente und beide Achsen). Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Flächeninhalt zwischen Graph und waagerechter Gerade als Term in der Grenze nachweisen", typ_neben="",
    stichwoerter="Fläche zwischen Gf und y = 1 von u bis 0|∫_u^0 (f(x) − 1) dx = [3e^x]_u^0 = 3 − 3e^u",
    voraussetzungen="Differenz zur Geraden y = 1|Stammfunktion von 3e^x|Grenzen u und 0",
    format="Begründung", operator="Weisen Sie nach", antwort="Term",
    material="Koordinatensystem", skizze=EXP, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 3e^x + 1; Fläche zwischen Gf, der y-Achse, y = 1 und x = u mit u < 0",
    gesucht="Nachweis, dass der Inhalt 3 − 3e^u beträgt",
    verfahren="Integral über f(x) − 1 von u bis 0",
    schritte="2", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="∫_u^0 (f(x) − 1) dx = [3e^x]_u^0 = 3 − 3e^u (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Grenzen vertauschen (Vorzeichen)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Senkrechte Gerade zur Halbierung einer Fläche über den Flächenterm bestimmen", typ_neben="",
    stichwoerter="Gesamtfläche für u = −ln 5: 3 − 3e^{−ln 5} = 3 − 3/5 = 12/5|Teilfläche von a bis 0: 3 − 3e^a = 6/5|e^a = 3/5, a = ln(3/5)",
    voraussetzungen="Flächenterm aus d|Halbierung als Gleichung|e^{−ln 5} = 1/5|Logarithmus",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=EXP, kontext="ohne", textumfang="mittel",
    gegeben="Flächeninhalt 3 − 3e^u (aus d); u = −ln 5; die Gerade x = a teilt die Fläche in zwei inhaltsgleiche Teile",
    gesucht="Wert von a",
    verfahren="Fläche von a bis 0 gleich halber Gesamtfläche setzen",
    schritte="3", zahlenraum="Bruch|Potenz|negativ", einheiten="", abhaengig_von="2026MgrundlegendBAnalysisWTR2-1d",
    ergebnis="3 − 3e^a = 1/2 · (3 − 3e^{−ln 5}) ⇔ 3 − 3e^a = 6/5 ⇔ a = ln(3/5) (amtlich)",
    zwischenergebnis="a ≈ −0,51",
    niveau_geschaetzt="III",
    fehlerquelle="Halbierung auf den Term mit u statt a anwenden",
    bemerkung="Standardbezug: K2 III, K4 I, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Flächenhalbierung in eine Gleichung übersetzen, verkettet mit Logarithmus. Vom Typ „Fläche: Verschiebung für die Halbierung einer Fläche über ein Integral bestimmen“ getrennt (senkrechte Grenze statt Verschiebung). Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR2", "f", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Abbildung zwischen zwei Graphen angeben", typ_neben="",
    stichwoerter="e^{−x/400}: Spiegelung an der y-Achse und Streckung in x-Richtung mit Faktor 400",
    voraussetzungen="Vorzeichen im Exponenten als Spiegelung|Faktor 1/400 im Argument als Streckung um 400",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 3e^x + 1; k(x) = 60e^{−x/400} + 20 entsteht aus f durch Streckung in y-Richtung mit Faktor 20 und weitere Veränderungen durch den Faktor −1/400",
    gesucht="diese weiteren Veränderungen",
    verfahren="Faktor im Exponenten in Spiegelung und Streckung zerlegen",
    schritte="1", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Spiegelung an der y-Achse und Streckung in x-Richtung mit dem Faktor 400 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Streckung mit Faktor 1/400 (Stauchung) statt 400",
    bemerkung="Standardbezug: K1 I, K2 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2026-ea-A). Trägerbindung: frei.")

# ---- Analysis WTR 2, Aufgabe 2: Speicherofen k(x) = 60e^{−x/400} + 20
row("2026MgrundlegendBAnalysisWTR2", "a", innen="2", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="k(0) = 60 + 20 = 80 °C",
    voraussetzungen="Beginn heißt x = 0",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Speicherofen/Abkühlung", textumfang="lang",
    gegeben="k(x) = 60e^{−x/400} + 20, x Zeit in Minuten seit Beginn des Abkühlens, k(x) Oberflächentemperatur in °C",
    gesucht="Oberflächentemperatur zu Beginn",
    verfahren="k(0)",
    schritte="1", zahlenraum="ganz", einheiten="°C|Minuten", abhaengig_von="",
    ergebnis="80 °C (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="60 °C (Verschiebung 20 vergessen)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR2", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere und momentane Änderungsrate im Sachzusammenhang vergleichen", typ_neben="",
    stichwoerter="mittlere Rate (k(60) − k(0))/60 ≈ −0,139|momentane Rate k'(60) ≈ −0,129|relative Abweichung ≈ 0,08 < 0,1",
    voraussetzungen="Differenzenquotient|Ableitungswert (k' vorgegeben)|prozentuale Abweichung als Quotient",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Speicherofen/Abkühlung", textumfang="mittel",
    gegeben="k(x) = 60e^{−x/400} + 20; k'(x) = −1/400 · 60e^{−x/400}; erste 60 Minuten",
    gesucht="ob die mittlere Änderungsrate der ersten 60 Minuten um mehr als 10 % von der momentanen Änderungsrate bei 60 Minuten abweicht",
    verfahren="beide Raten berechnen, relative Abweichung bilden",
    schritte="3", zahlenraum="dezimal|Prozent|negativ", einheiten="°C|Minuten", abhaengig_von="",
    ergebnis="((k(60) − k(0))/(60 − 0) − k'(60)) / k'(60) ≈ 0,08, d. h. die zu untersuchende prozentuale Abweichung beträgt weniger als 10 % (amtlich)",
    zwischenergebnis="mittlere Rate ≈ −0,139 °C/min, k'(60) ≈ −0,129 °C/min",
    niveau_geschaetzt="II",
    fehlerquelle="Abweichung auf die mittlere statt die momentane Rate beziehen (≈ 0,072, gleiches Urteil) oder absolute Differenz mit 10 % vergleichen",
    bemerkung="Standardbezug: K2 I, K3 II, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAnalysisWTR2", "c", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Proportionalität zwischen Bestand und Änderungsrate im Sachzusammenhang nachweisen", typ_neben="",
    stichwoerter="k(x) − 20 = 60e^{−x/400}|k'(x) = −1/400 · 60e^{−x/400}|k(x) − 20 = −400 · k'(x), c = −400",
    voraussetzungen="Differenzterm|Ableitung vorgegeben|Faktor zwischen beiden Termen erkennen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Speicherofen/Abkühlung", textumfang="lang",
    gegeben="k(x) − 20 Differenz zur Umgebungstemperatur; k'(x) = −1/400 · 60e^{−x/400}; Aussage: es gibt c mit k(x) − 20 = c · k'(x) für alle x",
    gesucht="Begründung, dass die Aussage im Modell wahr ist",
    verfahren="k − 20 als Vielfaches von k' schreiben",
    schritte="2", zahlenraum="ganz|negativ|Potenz", einheiten="°C|Minuten", abhaengig_von="",
    ergebnis="k(x) − 20 = 60e^{−x/400} = −400 · k'(x); somit existiert die beschriebene Konstante c (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="c positiv erwarten und die Aussage verwerfen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis, bei dem die Beziehung k − 20 = −400 k' aus den Termen hergeleitet wird, verkettet mit (d) Übersetzung der Sachaussage. Trägerbindung: Kontext (die Aussage ist in Sachbegriffen formuliert).")

# ---- AG/LA (A1) WTR: Käferpopulation
row("2026MgrundlegendBAGLAA1WTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="E → L 0,6|L → K 0,4|K → K 0,8 (Schleife)|K → E 20",
    voraussetzungen="Spalte = von, Zeile = nach|Schleife für den bleibenden Anteil",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Käfer/Population", textumfang="lang",
    gegeben="v = (E; L; K) Eier, Larven, Käfer am Monatsanfang; v_(n+1) = P · v_n mit P = ((0; 0; 20), (0,6; 0; 0), (0; 0,4; 0,8))",
    gesucht="Übergangsdiagramm",
    verfahren="Matrixeinträge als Pfeile zwischen E, L, K eintragen",
    schritte="1", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="Diagramm mit drei Knoten E, L, K; Pfeile E → L mit 0,6, L → K mit 0,4, K → E mit 20, Schleife an K mit 0,8 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauschen (Pfeil E → K mit 20)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2018-ea-A; dort aus der Tabelle, hier aus der Matrix – gleiche Fertigkeit, Vorschlag für den Abgleich: Definition auf Matrix erweitern). Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg. Trägerbindung: frei.")

row("2026MgrundlegendBAGLAA1WTR", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Matrix-Vektor-Produkt berechnen", typ_neben="",
    stichwoerter="P · (1000; 2000; 3000) = (60000; 600; 3200)",
    voraussetzungen="Matrix-Vektor-Produkt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Käfer/Population", textumfang="kurz",
    gegeben="P aus a; Anfang April 1000 Eier, 2000 Larven, 3000 Käfer",
    gesucht="Zusammensetzung Anfang Mai",
    verfahren="P · v",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P · (1000; 2000; 3000) = (60000; 600; 3200) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Zeile mal Spalte vertauschen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2020-ga-A). Aufgabengruppe A1, außerhalb der Geltung. Trägerbindung: frei.")

row("2026MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Term mit Matrixpotenz und Zugang im Sachzusammenhang auswählen und deuten", typ_neben="",
    stichwoerter="Zugabe Anfang Mai: h = P · (P · v + z)|f = P · P · (v + z): Zugabe schon Anfang April|g = P · P · v + z: Zugabe erst Anfang Juni",
    voraussetzungen="Reihenfolge von Übergang und Zugabe im Term lesen|Matrixprodukt als Monatsschritt",
    format="Kurzantwort", operator="Entscheiden Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Käfer/Population", textumfang="lang",
    gegeben="v = (1000; 2000; 3000) Anfang April, z = (0; 0; 1000); Terme f = P · P · (v + z), g = P · P · v + z, h = P · (P · v + z); Anfang Mai werden 1000 Käfer hinzugefügt",
    gesucht="welcher Term die Zusammensetzung Anfang Juni beschreibt und die Bedeutung eines anderen",
    verfahren="Position der Zugabe zwischen den Matrixschritten deuten",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Vektor h; Vektor f beschreibt die Zusammensetzung der Population Anfang Juni, wenn Anfang April zusätzlich tausend voll entwickelte Käfer hinzugefügt würden (amtlich)",
    zwischenergebnis="g: Zugabe erst Anfang Juni",
    niveau_geschaetzt="II",
    fehlerquelle="g wählen (Zugabe wird nicht mehr transformiert)",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung. Trägerbindung: Kontext (Monatsfolge April/Mai/Juni trägt die Deutung).")

row("2026MgrundlegendBAGLAA1WTR", "d", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen", typ_neben="",
    stichwoerter="P · (10000; 3000; K0) = r · (10000; 3000; K0)|20 K0 = 10000 r, 6000 = 3000 r, 1200 + 0,8 K0 = r K0|r = 2, K0 = 1000",
    voraussetzungen="Matrix-Vektor-Gleichung komponentenweise|r aus der zweiten Komponente|K0 aus der ersten|Probe dritte",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Käfer/Population", textumfang="mittel",
    gegeben="v0 = (10000; 3000; K0), P · v0 = r · v0 mit K0 natürlich und r > 1",
    gesucht="r und K0",
    verfahren="Gleichungssystem aus den Komponenten lösen",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P · (10000; 3000; K0) = (r · 10000; r · 3000; r · K0) ⇔ 20 K0 = r · 10000 ∧ 6000 = r · 3000 ∧ 1200 + 0,8 K0 = r · K0 ⇔ r = 2 ∧ K0 = 1000 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="dritte Gleichung als Widerspruch lesen statt als Probe",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-A; hier zusätzlich der Faktor r). Aufgabengruppe A1, außerhalb der Geltung. Trägerbindung: frei.")

KURVEN = ("Koordinatensystem ohne Skalen, y-Achse mit Marke K0; drei Kurven von (0; K0): I fallend gegen die x-Achse, "
          "II Gerade steigend, III exponentiell steigend, oberhalb von II")
row("2026MgrundlegendBAGLAA1WTR", "e", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Exponentielles Wachstum aus einem Eigenvektor begründen und Kurve zuordnen", typ_neben="",
    stichwoerter="P · v0 = 2 · v0 ⇒ v_n = 2^n · v0|K_n = K0 · 2^n exponentiell|Kurve III",
    voraussetzungen="Vervielfachung je Schritt aus d|Potenz als wiederholte Vervielfachung|exponentielles gegen lineares Wachstum",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=KURVEN, kontext="Käfer/Population", textumfang="kurz",
    gegeben="P · v0 = r · v0 mit r = 2 (aus d); Punkte (n | K_n); Kurven I (fallend), II (linear), III (exponentiell)",
    gesucht="die Kurve, auf der die Punkte liegen, mit Begründung",
    verfahren="K_n = K0 · r^n herleiten, Wachstumsart benennen",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="2026MgrundlegendBAGLAA1WTR-1d",
    ergebnis="Kurve III; wegen K_n = K0 · r^n und r > 1 liegt eine exponentielle Zunahme vor, Kurve I und Kurve II zeigen dies jeweils nicht (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Kurve II wählen (Zunahme, aber linear gedacht)",
    bemerkung="Standardbezug: K1 III, K4 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) die Beziehung v_n = r^n v0 aus der Eigenvektorgleichung herleiten, verkettet mit der Zuordnung am Graphen. Aufgabengruppe A1, außerhalb der Geltung. Trägerbindung: frei.")

# ---- AG/LA (A2) WTR 1: Prisma als Behälter
PRISMA = ("Schrägbild eines geraden Prismas ABCDEF: Grundfläche Dreieck ABC bei x = 10 (A auf der x-Achse, B und C bei z = 20 mit y = ±5), "
          "Deckfläche DEF mit D im Ursprung; Kanten AD, BE, CF parallel zur x-Achse; Koordinatenachsen x, y, z")
row("2026MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Lage eines Dreiecks parallel zu einer Koordinatenebene und symmetrisch zu einer anderen begründen", typ_neben="",
    stichwoerter="A, B, C haben x = 10: Ebene x = 10 parallel zur yz-Ebene|A in der xz-Ebene, B und C unterscheiden sich nur im Vorzeichen von y",
    voraussetzungen="gleiche Koordinate als Parallelität|Symmetrie zur xz-Ebene als Vorzeichenwechsel von y",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=PRISMA, kontext="ohne", textumfang="mittel",
    gegeben="gerades Prisma ABCDEF mit A(10 | 0 | 0), B(10 | 5 | 20), C(10 | −5 | 20), D(0 | 0 | 0)",
    gesucht="Begründung, dass ABC parallel zur yz-Ebene und symmetrisch zur xz-Ebene liegt",
    verfahren="Koordinaten vergleichen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Parallelität: ABC liegt in der Ebene x = 10; Symmetrie: A liegt in der xz-Ebene, die Koordinaten von B und C unterscheiden sich nur im Vorzeichen der y-Koordinate (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Symmetrie zur yz-Ebene behaupten",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen eines geraden Prismas über einem Dreieck nachweisen", typ_neben="",
    stichwoerter="Grundfläche 1/2 · 10 · 20 = 100 (Basis BC = 10, Höhe 20)|Prismenhöhe |AD| = 10|V = 1000",
    voraussetzungen="Dreiecksfläche aus Basis und Höhe|Prisma: Grundfläche mal Höhe",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Körper", skizze=PRISMA, kontext="ohne", textumfang="kurz",
    gegeben="Prisma aus a, Grundfläche ABC in x = 10, D(0 | 0 | 0)",
    gesucht="Nachweis, dass das Volumen 1000 beträgt",
    verfahren="Dreiecksfläche mal Kantenlänge AD",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="1/2 · (5 − (−5)) · 20 · 10 = 1000 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Pyramidenformel mit 1/3 verwenden",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Körper: Volumen eines Prismas über einer Raute berechnen“ getrennt (Dreieck, Nachweis). Trägerbindung: frei.")

row("2026MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene durch drei Punkte bestimmen", typ_neben="",
    stichwoerter="Normalenvektor senkrecht zu DB = (10; 5; 20) und DA = (10; 0; 0): n = (0; 4; −1)|4y − z = c, D einsetzen: c = 0",
    voraussetzungen="Normalenvektor über Skalarprodukte oder Kreuzprodukt|Punkt einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=PRISMA, kontext="ohne", textumfang="kurz",
    gegeben="A(10 | 0 | 0), B(10 | 5 | 20), D(0 | 0 | 0); Kontrolle 4y − z = 0",
    gesucht="Koordinatengleichung der Ebene ABD",
    verfahren="Normalenvektor aus zwei Richtungsvektoren, Konstante über einen Punkt",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="n · (0; 5; 20) = 0 ∧ n · (−10; 0; 0) = 0 liefert n = (0; 4; −1) als Normalenvektor; die Ebene hat eine Gleichung der Form 4y − z = c; da D in der Ebene liegt, folgt 4y − z = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Normalenvektor (0; 1; 4) (Komponenten vertauscht)",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Koordinatengleichung der Ebene durch zwei sich schneidende Geraden bestimmen“ (2018-ea-A) getrennt (drei Punkte; Abgleich prüfen). Trägerbindung: frei.")

DREH = ("Abb. 2: Prisma in Ausgangslage und um die Achse AD gedreht, Drehpfeil bis 120°; Abb. 3: Koordinatensystem Drehwinkel 0° bis 90° "
        "gegen Wasservolumen in Litern 0 bis 1,1; Graph nur von α (≈ 55°) bei 0,5 Liter fallend bis β (≈ 76°) bei 0 eingezeichnet")
row("2026MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Füllvolumen eines gedrehten Behälters am Graphen ergänzen und Grenzwinkel deuten", typ_neben="",
    stichwoerter="Fassungsvermögen 1000 cm³ = 1 Liter, halb voll: 0,5 Liter|bis zum Winkel α bleibt das Volumen 0,5 (waagerechte Strecke)|α: Winkel, bei dem das Wasser auszulaufen beginnt",
    voraussetzungen="Volumen aus b in Liter umrechnen|bis zum Überlaufen bleibt das Volumen konstant|Bedeutung des Knickpunkts",
    format="Eintragen|Kurzantwort", operator="Zeichnen Sie ein|Geben Sie an", antwort="Grafik",
    material="Diagramm", skizze=DREH, kontext="Behälter/Drehung", textumfang="lang",
    gegeben="Behälter = Prisma (1000 cm³, Öffnung BEFC), halb gefüllt; Drehung um die Achse AD bis 120°; Graph Volumen gegen Drehwinkel für [α; β] vorgegeben",
    gesucht="Graph für [0°; α[ und Bedeutung von α",
    verfahren="konstante 0,5 Liter bis α einzeichnen, α als Beginn des Auslaufens deuten",
    schritte="2", zahlenraum="dezimal", einheiten="Liter|°", abhaengig_von="2026MgrundlegendBAGLAA2WTR1-1b",
    ergebnis="waagerechte Strecke bei 0,5 Litern von 0° bis α; bei diesem Drehwinkel beginnt das Wasser aus dem Behälter zu laufen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Graph ab 0° fallend zeichnen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich. Trägerbindung: Kontext (Behälter, Öffnung, Drehung und halbe Füllung sind nur aus der Trägeraufgabe zu verstehen; ohne sie ist die Zeile nicht nachbaubar).")

row("2026MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Winkel zwischen einer Seitenfläche und der Horizontalen als Grenzwinkel im Sachzusammenhang bestimmen", typ_neben="",
    stichwoerter="Wasser ist ganz ausgelaufen, wenn die Seitenwand ADEB waagerecht liegt|Winkel zwischen Ebene ABD (n = (0; 4; −1)) und xy-Ebene (n = (0; 0; 1))|cos β = 1/√17, β ≈ 76°",
    voraussetzungen="β als Winkel, bei dem die Wand ADEB horizontal wird|Winkel zwischen Ebenen über Normalenvektoren|Normalenvektor aus c",
    format="Rechnung", operator="Bestimmen Sie|Erläutern Sie", antwort="Zahl",
    material="Diagramm", skizze=DREH, kontext="Behälter/Drehung", textumfang="mittel",
    gegeben="Ebene ABD: 4y − z = 0 (aus c); Drehung um AD; β Drehwinkel, bei dem das Volumen 0 erreicht",
    gesucht="rechnerisch ein geeigneter Wert für β mit Erläuterung des Ansatzes",
    verfahren="Winkel zwischen der Wandebene ABD und der xy-Ebene über die Normalenvektoren",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2026MgrundlegendBAGLAA2WTR1-1c",
    ergebnis="cos β = |(0; 4; −1) · (0; 0; 1)| / (|(0; 4; −1)| · |(0; 0; 1)|) = 1/√17 liefert β ≈ 76°; wenn sich die Seitenwand ADEB in horizontaler Lage befindet, ist das gesamte Wasser aus dem Behälter gelaufen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Winkel zwischen Kante AB und der xy-Ebene nehmen (≈ 44°) oder α statt β rechnen",
    bemerkung="Standardbezug: K1 III, K2 II, K3 III, K4 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „Behälter leer“ in „Wand ADEB horizontal“ und in den Winkel zwischen Ebene ABD und xy-Ebene übersetzen, verkettet mit der Winkelberechnung. Trägerbindung: Kontext.")

# ---- AG/LA (A2) WTR 2: Pyramide ABCDS
PYR = ("Schrägbild einer Pyramide ABCDS mit trapezförmiger Grundfläche in der xy-Ebene (A und D auf der y-Achse, B und C bei x = 5), "
       "Spitze S über der Grundfläche, Koordinatenachsen; in Abb. 2 zusätzlich die Schnittpunkte T, U, V, W der Seitenkanten mit z = 2")
row("2026MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen", typ_neben="",
    stichwoerter="AD = (0; 4; 0), BC = (0; 2; 0) kollinear|Höhe 5 (x-Abstand)|A = 1/2 · (4 + 2) · 5 = 15",
    voraussetzungen="Parallelität über Kollinearität|Trapezformel",
    format="Rechnung", operator="Zeigen Sie|Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="mittel",
    gegeben="A(0 | −2 | 0), B(5 | −1 | 0), C(5 | 1 | 0), D(0 | 2 | 0), S(2 | 0 | 4); Pyramide symmetrisch zur xz-Ebene",
    gesucht="Nachweis, dass ABCD ein Trapez ist, und sein Flächeninhalt",
    verfahren="AD und BC vergleichen, Trapezformel mit Höhe 5",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="AD = (0; 4; 0) und BC = (0; 2; 0) sind kollinear; Flächeninhalt 1/2 · (4 + 2) · 5 = 15 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Schenkel AB als Höhe nehmen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Winkel zwischen zwei Kanten über das Skalarprodukt berechnen", typ_neben="",
    stichwoerter="CD = (−5; 1; 0), CS = (−3; −1; 4)|cos α = 14/(√26 · √26) = 7/13|α ≈ 57,4°",
    voraussetzungen="Kantenvektoren vom gemeinsamen Eckpunkt|Winkelformel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="kurz",
    gegeben="C(5 | 1 | 0), D(0 | 2 | 0), S(2 | 0 | 4)",
    gesucht="Größe des Winkels zwischen den Kanten CD und CS",
    verfahren="Skalarprodukt der Kantenvektoren",
    schritte="2", zahlenraum="Bruch|Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="cos α = ((−5; 1; 0) · (−3; −1; 4)) / (|(−5; 1; 0)| · |(−3; −1; 4)|) = 7/13 liefert α ≈ 57,4° (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Vektoren DC und CS mischen (Nebenwinkel 122,6°)",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lotfußpunkt aus Geradengleichung und Orthogonalitätsbedingung im Gleichungspaar deuten", typ_neben="",
    stichwoerter="I: P auf der Geraden CS|II: DP senkrecht zu CS|P ist der Fußpunkt des Lotes von D auf die Gerade CS",
    voraussetzungen="Parametergleichung einer Geraden lesen|Skalarprodukt null als Orthogonalität|Lotfußpunkt",
    format="Kurzantwort", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="mittel",
    gegeben="Lot von D auf eine Gerade durch zwei Eckpunkte; Gleichungen I OP = OC + t · CS und II DP · CS = 0 liefern gemeinsam einen Wert von t",
    gesucht="Bedeutung des Punktes P für diesen Wert von t",
    verfahren="beide Gleichungen geometrisch deuten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="P ist der Fußpunkt des Lotes von D auf die Gerade durch die Eckpunkte C und S (amtlich)",
    zwischenergebnis="t = 7/26",
    niveau_geschaetzt="II",
    fehlerquelle="P als Lotfußpunkt auf die Kante CD deuten",
    bemerkung="Standardbezug: K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Analog zu „Gleichung als Tangentenbedingung geometrisch deuten“. Trägerbindung: frei.")

row("2026MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Mittelpunkt einer Kante nachweisen und symmetrischen Schnittpunkt angeben", typ_neben="",
    stichwoerter="1/2 · (D + S) = (1; 1; 2) = W|T symmetrisch zu W bezüglich der xz-Ebene: T(1; −1; 2)",
    voraussetzungen="Mittelpunktsformel|Symmetrie der Pyramide zur xz-Ebene",
    format="Begründung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Zahl",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="mittel",
    gegeben="Ebene F: z = 2 schneidet die Seitenkanten in T, U(3,5 | −0,5 | 2), V, W(1 | 1 | 2); D(0 | 2 | 0), S(2 | 0 | 4); Pyramide symmetrisch zur xz-Ebene",
    gesucht="Nachweis, dass W Mittelpunkt von DS ist, und Koordinaten von T",
    verfahren="Mittelpunkt berechnen, T durch Spiegelung von W an der xz-Ebene",
    schritte="2", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="1/2 · ((0; 2; 0) + (2; 0; 4)) = (1; 1; 2); T(1 | −1 | 2) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="T auf der Kante BS statt AS suchen",
    bemerkung="Standardbezug: K1 I, K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBAGLAA2WTR2", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Spiegelebene aus Punkt und Spiegelpunkt bestimmen", typ_neben="",
    stichwoerter="Trapeze TUVW und BUVC teilen die Seite UV; C und W entsprechen sich|CW = (−4; 0; 2) Normalenvektor von H|−4x + 2z = d, U einsetzen: d = −10",
    voraussetzungen="einander entsprechende Ecken der beiden Trapeze erkennen|Verbindungsvektor als Normalenvektor|Punkt der Ebene (U auf der gemeinsamen Seite)",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="kurz",
    gegeben="Trapeze TUVW (in z = 2) und BUVC (Seitenfläche) symmetrisch zu einer Ebene H; C(5 | 1 | 0), W(1 | 1 | 2), U(3,5 | −0,5 | 2)",
    gesucht="Gleichung von H",
    verfahren="C und W als Spiegelpaar, Normalenvektor CW, Konstante über U",
    schritte="3", zahlenraum="ganz|dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="die Punkte C und W sind bezüglich H symmetrisch zueinander, folglich ist CW = (−4; 0; 2) ein Normalenvektor von H; H: −4x + 2z = d, da U in H liegt, gilt d = −4 · 3,5 + 2 · 2 = −10 (amtlich)",
    zwischenergebnis="Mittelpunkt von CW (3; 1; 1) liegt in H",
    niveau_geschaetzt="III",
    fehlerquelle="H als Ebene durch U und V senkrecht zur xy-Ebene ansetzen",
    bemerkung="Standardbezug: K1 II, K2 III, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Symmetrie erkennen – welche Ecken sich entsprechen (C ↔ W, gemeinsame Seite UV) –, verkettet mit der Ebenengleichung. Typ wiederverwendet (2022-ea-A; dort Spiegelpaar vorgegeben, II). Trägerbindung: frei.")

# ---- Stochastik WTR 1: Treuepunkte
row("2026MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen", typ_neben="",
    stichwoerter="(b über 3) · c³ · 0,25⁷ mit b = 10, c = 0,75|a = 3: genau drei sammeln Treuepunkte",
    voraussetzungen="Bernoulli-Formel mit n = 10, p = 0,75|Exponenten 3 und 7 ergänzen sich zu 10",
    format="Kurzantwort", operator="Geben Sie an|Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Supermarkt/Treuepunkte", textumfang="lang",
    gegeben="75 % des Kundenkreises sammeln Treuepunkte; X Anzahl der Sammler unter 10 zufällig Ausgewählten, binomialverteilt; Term P(X = a) = (b über 3) · c³ · 0,25⁷",
    gesucht="Werte a, b, c und Beschreibung des Ereignisses",
    verfahren="Platzhalter aus n, p und k lesen",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="a = 3; b = 10; c = 0,75; genau drei Personen sammeln Treuepunkte (amtlich)",
    zwischenergebnis="P ≈ 0,0031",
    niveau_geschaetzt="I",
    fehlerquelle="a = 7 (Exponent von 0,25 als Trefferzahl)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-A; Thema hier Binomialverteilung). Trägerbindung: frei.")

row("2026MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="P(X < 8) = P(X ≤ 7) mit n = 10, p = 0,75|≈ 47,4 %",
    voraussetzungen="„weniger als 8“ als X ≤ 7|kumulierte Binomialverteilung am WTR",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Supermarkt/Treuepunkte", textumfang="kurz",
    gegeben="X binomialverteilt mit n = 10, p = 0,75",
    gesucht="P(X < 8)",
    verfahren="kumulierte Wahrscheinlichkeit am Rechner",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(X < 8) ≈ 47,4 % (n = 10, p = 0,75) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="P(X ≤ 8) rechnen (≈ 75,6 %)",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erster Typ mit Rechnereinsatz (Teil B). Trägerbindung: frei.")

VERT = ("Säulendiagramm P(Y = k) für k = 0 bis 10 mit y-Marken 0,1 bis 0,3: Säulen bei 0 etwa 0,06, 1 etwa 0,19, 2 etwa 0,28, 3 etwa 0,25, "
        "4 etwa 0,15, 5 etwa 0,06, 6 etwa 0,02, danach kaum sichtbar")
row("2026MgrundlegendBStochastikWTR1", "c", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern", typ_neben="",
    stichwoerter="Y = 10 − X ist B(10; 0,25)-verteilt|P(X = 6) = P(Y = 4)|Säule bei k = 4 ablesen",
    voraussetzungen="Gegenzufallsgröße mit p' = 1 − p|Zuordnung k ↔ n − k",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Diagramm", skizze=VERT, kontext="Supermarkt/Treuepunkte", textumfang="mittel",
    gegeben="Abbildung: Verteilung von Y mit n = 10, p = 0,25; X Anzahl der Sammler mit p = 0,75",
    gesucht="Erläuterung, wie man mit der Abbildung P(X = 6) ermittelt",
    verfahren="X = 6 Sammler heißt Y = 4 Nichtsammler",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="wegen P(X = 6) = P(Y = 4) (n = 10; p = 0,75 bzw. 0,25) entspricht in der Abbildung der Wert für k = 4 der gesuchten Wahrscheinlichkeit (amtlich)",
    zwischenergebnis="≈ 0,146",
    niveau_geschaetzt="II",
    fehlerquelle="Säule bei k = 6 ablesen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Eine Deutung (Gegenzufallsgröße) ohne Verkettung, II. Trägerbindung: frei.")

BAUM = ("Baumdiagramm: erste Stufe T (75 %) und nicht T; zweite Stufe w (80 %) und nicht w unter T, w (a) und nicht w unter nicht T")
row("2026MgrundlegendBStochastikWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen", typ_neben="",
    stichwoerter="P(w und T) = 0,75 · 0,8 = 0,6|P(nicht w und nicht T) = 0,25 · 0,4 = 0,1|0,6 = 6 · 0,1: wahr",
    voraussetzungen="Pfadregel|Gegenwahrscheinlichkeiten 0,25 und 1 − a|Vergleich als Faktor",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Diagramm", skizze=BAUM, kontext="Supermarkt/Treuepunkte", textumfang="lang",
    gegeben="75 % sammeln (T); unter den Sammlern 80 % weiblich; unter den Nichtsammlern Anteil a weiblich; a = 0,6",
    gesucht="ob P(weiblich und T) sechsmal so groß ist wie P(nicht weiblich und nicht T)",
    verfahren="beide Pfade berechnen und vergleichen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="wegen 0,75 · 0,8 = 6 · 0,25 · 0,4 ist die Aussage wahr (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="1 − a = 0,4 nicht bilden und mit a = 0,6 rechnen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBStochastikWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen", typ_neben="",
    stichwoerter="P(nicht w) = 0,75 · 0,2 + 0,25 · (1 − a) = 0,3|0,4 − 0,25a = 0,3|a = 0,4",
    voraussetzungen="Randwahrscheinlichkeit als Summe zweier Pfade|lineare Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=BAUM, kontext="Supermarkt/Treuepunkte", textumfang="kurz",
    gegeben="Baumdiagramm wie in a; Anteil der nicht weiblichen Personen im Kundenkreis 30 %",
    gesucht="Anteil a",
    verfahren="Summe der Pfade zu „nicht weiblich“ gleich 0,3 setzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,75 · 0,2 + 0,25 · (1 − a) = 0,3 ⇔ 0,4 − 0,25a = 0,3 ⇔ a = 0,4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Pfad 0,75 · 0,2 vergessen",
    bemerkung="Standardbezug: K2 I, K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Anteil aus dem Ergebnis eines Befragungsverfahrens berechnen“ getrennt (Randwahrscheinlichkeit statt Ja-Häufigkeit; Abgleich prüfen). Trägerbindung: frei.")

row("2026MgrundlegendBStochastikWTR1", "c", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen", typ_neben="",
    stichwoerter="P(T | nicht w) = 0,75 · 0,2 / (0,75 · 0,2 + 0,25 · (1 − a))|a steigt ⇒ Nenner fällt ⇒ Quotient steigt|Aussage wahr",
    voraussetzungen="bedingte Wahrscheinlichkeit als Bayes-Quotient in a|Monotonie eines Bruchs im Nenner",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Diagramm", skizze=BAUM, kontext="Supermarkt/Treuepunkte", textumfang="lang",
    gegeben="ein Jahr später: weiterhin 75 % Sammler, 80 % davon weiblich, a gestiegen; Aussage: P(T | nicht weiblich) ist größer als vor einem Jahr",
    gesucht="Beurteilung der Aussage",
    verfahren="Term in a aufstellen und Monotonie begründen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="die Aussage ist wahr; mit dem Term 0,75 · 0,2 / (0,75 · 0,2 + 0,25 · (1 − a)) kann die beschriebene Wahrscheinlichkeit berechnet werden; wenn a steigt, nimmt der Nenner ab und der Quotient zu (amtlich)",
    zwischenergebnis="a = 0,4: 0,5; a = 0,6: 0,6",
    niveau_geschaetzt="III",
    fehlerquelle="mit Zahlenbeispiel statt allgemein argumentieren; Zähler für abhängig von a halten",
    bemerkung="Standardbezug: K1 III, K2 II, K3 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Sachaussage in einen Bayes-Term mit Parameter übersetzen und mit der Monotonie des Bruchs verketten. Trägerbindung: frei (Baumdiagramm mit a in gegeben).")

# ---- Stochastik WTR 2: Playlist
row("2026MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="Ränder 0,32 / 0,68 und 0,4 / 0,6|Innenfelder 0,14, 0,26, 0,18, 0,42",
    voraussetzungen="Randsummen aus den Anteilen|Differenzen",
    format="Tabelle", operator="Ergänzen Sie", antwort="Tabelle",
    material="Tabelle", skizze="Vierfeldertafel H / nicht H gegen L / nicht L, nur 0,14 (H und L) und die Summe 1 eingetragen", kontext="Playlist/Musik", textumfang="mittel",
    gegeben="32 % Hip-Hop-Songs (H), 40 % mindestens 4 Minuten lang (L), P(H und L) = 0,14",
    gesucht="fehlende Wahrscheinlichkeiten der Vierfeldertafel",
    verfahren="Ränder eintragen, Innenfelder als Differenzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="H und L 0,14, nicht H und L 0,26, H und nicht L 0,18, nicht H und nicht L 0,42; Ränder 0,4, 0,6, 0,32, 0,68 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="0,32 · 0,4 als Schnitt ansetzen (Unabhängigkeit unterstellt)",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Trägerbindung: frei.")

row("2026MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="P(L | H) = 0,14/0,32 ≈ 43,8 %",
    voraussetzungen="Bedingung als Nenner|Schnitt aus der Vierfeldertafel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze="Vierfeldertafel aus a", kontext="Playlist/Musik", textumfang="kurz",
    gegeben="P(H) = 0,32, P(H und L) = 0,14",
    gesucht="P(L | H)",
    verfahren="Quotient",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2026MgrundlegendBStochastikWTR2-1a",
    ergebnis="0,14/0,32 ≈ 43,8 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="0,14/0,4 (Bedingung vertauscht)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2022-ga-A; hier mit Vierfeldertafel – Definition „ohne Vierfeldertafel“ beim Abgleich lockern). Trägerbindung: frei.")

row("2026MgrundlegendBStochastikWTR2", "c", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X ~ B(20; 0,32)|P(X > 5) = 1 − P(X ≤ 5) ≈ 65,7 %",
    voraussetzungen="„mehr als 5“ als Gegenereignis von X ≤ 5|kumulierte Verteilung am WTR",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Playlist/Musik", textumfang="mittel",
    gegeben="20 zufällig ausgewählte Lieder, Anzahl der Hip-Hop-Songs binomialverteilt mit p = 0,32",
    gesucht="P(mehr als 5 Hip-Hop-Songs)",
    verfahren="1 − P(X ≤ 5) am Rechner",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="X: Anzahl der Hip-Hop-Songs; P(X > 5) ≈ 65,7 % (n = 20, p = 0,32) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="P(X ≥ 5) rechnen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Stochastik WTR 1 dieses Stapels). Trägerbindung: frei.")

row("2026MgrundlegendBStochastikWTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Summe k = 0 bis 8 von (20 über k) · 0,32^k · 0,68^(20 − k) = P(X ≤ 8)|höchstens acht Hip-Hop-Songs unter den 20 Liedern, etwa 84,3 %",
    voraussetzungen="Binomialsumme als kumulierte Wahrscheinlichkeit|n = 20, p = 0,32 im Sachzusammenhang",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Playlist/Musik", textumfang="mittel",
    gegeben="20 Lieder, p = 0,32; Aussage Summe k = 0 bis 8 von (20 über k) · 0,32^k · 0,68^(20 − k) ≈ 0,843",
    gesucht="Bedeutung der Aussage im Sachzusammenhang",
    verfahren="Summe als P(X ≤ 8) lesen",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="die Wahrscheinlichkeit dafür, dass unter den ausgewählten Liedern höchstens acht Hip-Hop-Songs sind, beträgt etwa 84,3 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="„genau acht“ statt „höchstens acht“",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Sachaussage zu einer Ungleichung mit Binomialsumme formulieren“ getrennt (Gleichung mit Wert statt Ungleichung mit Parameter; Abgleich prüfen). Trägerbindung: frei.")

row("2026MgrundlegendBStochastikWTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Lage- und Streumaße einer Stichprobe",
    typ="Fehlenden Wert aus dem arithmetischen Mittel berechnen", typ_neben="",
    stichwoerter="Summe der fünf Längen 4:45 + 3:56 + 3:35 + 4:36 + 4:08 = 21:00|6 · 4:05 = 24:30|sechstes Lied 3:30",
    voraussetzungen="Mittelwert als Summe durch Anzahl|Zeitangaben in Sekunden umrechnen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle Nummer 1 bis 5 mit Längen 4:45, 3:56, 3:35, 4:36, 4:08", kontext="Playlist/Musik", textumfang="mittel",
    gegeben="Längen der ersten fünf Lieder 4:45, 3:56, 3:35, 4:36, 4:08; Durchschnitt der ersten sechs 4:05",
    gesucht="Länge des sechsten Liedes",
    verfahren="Gesamtsumme aus dem Mittelwert minus Summe der fünf",
    schritte="3", zahlenraum="ganz", einheiten="Minuten|Sekunden", abhaengig_von="",
    ergebnis="die Summe der Längen der ersten fünf Lieder beträgt 21 Minuten; die Länge des sechsten Liedes ist somit 6 · (4 min 5 s) − 21 min = 3 min 30 s (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="4:05 als 4,05 Minuten rechnen",
    bemerkung="Standardbezug: K1 I, K2 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Lage- und Streumaße einer Stichprobe. Trägerbindung: frei.")

row("2026MgrundlegendBStochastikWTR2", "f", innen="1", seite="2", punkte="3", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl der Sitzordnungen mit Abstandsbedingung berechnen", typ_neben="",
    stichwoerter="zwei kurze Lieder (k), drei lange (l)|Muster ohne kk nebeneinander: klkll, kllkl, klllk, lklkl, lkllk, llklk – sechs|je Muster 2! · 3! Anordnungen|6 · 2 · 6 = 72",
    voraussetzungen="kurze und lange Lieder aus der Tabelle zählen|zulässige Muster aufzählen|Permutationen innerhalb der Sorten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle wie in e", kontext="Playlist/Musik", textumfang="lang",
    gegeben="fünf Lieder mit Längen aus der Tabelle (zwei unter 4 Minuten); jedes genau einmal; kurze Lieder nicht direkt nacheinander",
    gesucht="Anzahl der zulässigen Reihenfolgen",
    verfahren="Muster der Sorten aufzählen, mit den Anordnungen innerhalb der Sorten multiplizieren",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="genau zwei der Lieder sind kürzer als 4 Minuten; mit k für kurz und l für lang sind sechs Anordnungen möglich: klkll, kllkl, klllk, lklkl, lkllk, llklk; somit gibt es insgesamt 6 · 2! · 3! = 72 Möglichkeiten (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Muster zählen und die 2! · 3! vergessen (6) oder 5! − 4! · 2 = 72 ohne Begründung",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K5 I, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Aufzählung). Eichregel: (a) die Regel „nicht direkt nacheinander“ in zulässige Muster übersetzen, verkettet mit dem Abzählen der Anordnungen. Typ wiederverwendet (2024-ga-A; dort Personen und Plätze, gleiche Fertigkeit). Trägerbindung: frei.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Monotonie über das Vorzeichen der Ableitung am Term nachweisen", "Analysis", "Kurvenuntersuchung",
     "Zeigen, dass ein Graph auf ganz IR monoton ist, indem die Ableitung gebildet und ihr Vorzeichen am Term "
     "begründet wird (etwa als Quadrat).",
     "2026MgrundlegendBAnalysisWTR1-1a"),
    ("Tangentengleichung und Schnittwinkel der Tangente mit der x-Achse bestimmen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Tangente in einem Punkt aufstellen (Steigung aus der Ableitung, Achsenabschnitt gegeben oder berechnet) und "
     "ihren Schnittwinkel mit der x-Achse über tan α = m bestimmen.",
     "2026MgrundlegendBAnalysisWTR1-1c"),
    ("Integralwert: Integral über die Summe aus ungerader Funktion und Konstante ohne Stammfunktion begründen", "Analysis",
     "Flächeninhalt durch Integration",
     "Ein Integral über ein zu 0 symmetrisches Intervall ohne Stammfunktion begründen: der ungerade Anteil liefert "
     "null (Punktsymmetrie), der konstante Anteil ein Rechteck.",
     "2026MgrundlegendBAnalysisWTR1-1e"),
    ("Mittelpunkt eines den Graphen berührenden Kreises über die Normale im Berührpunkt bestimmen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Für einen Kreis, der einen Graphen in einem gegebenen Punkt berührt und dessen Mittelpunkt auf einer Achse "
     "liegt, den Mittelpunkt als Schnitt der Normalen im Berührpunkt mit der Achse berechnen.",
     "2026MgrundlegendBAnalysisWTR1-1f"),
    ("Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den Wert einer Modellfunktion an einer Stelle berechnen oder angeben und mit Einheit im Sachzusammenhang nennen.",
     "2026MgrundlegendBAnalysisWTR1-2a"),
    ("Transformation: Periode einer Kosinusfunktion im Sachzusammenhang deuten und Stelle stärkster Zunahme am Graphen angeben",
     "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus dem Faktor im Argument einer trigonometrischen Modellfunktion die Periode bestimmen, sie als Zyklusdauer "
     "deuten (etwa Zyklen je Minute) und die Stelle größter Zunahme am Graphen (steigende Wendestelle) angeben.",
     "2026MgrundlegendBAnalysisWTR1-2b"),
    ("Differenz und Differenzenquotient im Sachzusammenhang deuten", "Analysis", "Ableitung und Änderungsrate",
     "Eine Differenz f(b) − f(a) als absolute Änderung und den Differenzenquotienten als mittlere Änderungsrate mit "
     "Einheiten im Sachzusammenhang beschreiben.",
     "2026MgrundlegendBAnalysisWTR1-2c"),
    ("Nullstellen und Werte: Nullstellenfreiheit und Wertemenge einer e-Funktion aus dem Term begründen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Am Term begründen, dass eine Funktion a · e^x + c keine Nullstelle hat, und ihre Wertemenge angeben.",
     "2026MgrundlegendBAnalysisWTR2-1a"),
    ("Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Umfang des Dreiecks aus einer Tangente und beiden Koordinatenachsen über die Achsenabschnitte und den "
     "Satz des Pythagoras berechnen.",
     "2026MgrundlegendBAnalysisWTR2-1c"),
    ("Fläche: Flächeninhalt zwischen Graph und waagerechter Gerade als Term in der Grenze nachweisen", "Analysis",
     "Flächeninhalt durch Integration",
     "Nachweisen, dass der Inhalt der Fläche zwischen Graph, waagerechter Gerade und einer variablen senkrechten "
     "Grenze durch einen vorgegebenen Term in der Grenze beschrieben wird (Integral der Differenz).",
     "2026MgrundlegendBAnalysisWTR2-1d"),
    ("Fläche: Senkrechte Gerade zur Halbierung einer Fläche über den Flächenterm bestimmen", "Analysis",
     "Flächeninhalt durch Integration",
     "Die senkrechte Gerade x = a bestimmen, die eine Fläche halbiert, indem der Flächenterm in der Grenze gleich der "
     "halben Gesamtfläche gesetzt wird (Exponentialgleichung, Logarithmus).",
     "2026MgrundlegendBAnalysisWTR2-1e"),
    ("Mittlere und momentane Änderungsrate im Sachzusammenhang vergleichen", "Analysis", "Ableitung und Änderungsrate",
     "Die mittlere Änderungsrate über ein Intervall und die momentane Änderungsrate am Intervallende berechnen und "
     "ihre relative Abweichung mit einer Schranke vergleichen.",
     "2026MgrundlegendBAnalysisWTR2-2b"),
    ("Proportionalität zwischen Bestand und Änderungsrate im Sachzusammenhang nachweisen", "Analysis",
     "Ableitung und Änderungsrate",
     "Eine als Sachaussage formulierte Beziehung f(x) − c = k · f'(x) für eine Exponentialfunktion nachweisen, indem "
     "beide Terme verglichen werden.",
     "2026MgrundlegendBAnalysisWTR2-2c"),
    ("Übergangsprozess: Term mit Matrixpotenz und Zugang im Sachzusammenhang auswählen und deuten", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Unter Termen wie P · (P · v + z), P · P · (v + z), P · P · v + z den auswählen, der eine Zugabe zu einem "
     "bestimmten Zeitpunkt beschreibt, und die anderen im Sachzusammenhang deuten.",
     "2026MgrundlegendBAGLAA1WTR-1c"),
    ("Übergangsprozess: Exponentielles Wachstum aus einem Eigenvektor begründen und Kurve zuordnen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Aus P · v0 = r · v0 mit r > 1 die Beziehung v_n = r^n · v0 herleiten, das exponentielle Wachstum einer "
     "Komponente begründen und unter abgebildeten Kurven die passende angeben.",
     "2026MgrundlegendBAGLAA1WTR-1e"),
    ("Ebene Figur: Lage eines Dreiecks parallel zu einer Koordinatenebene und symmetrisch zu einer anderen begründen",
     "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Aus den Koordinaten der Eckpunkte begründen, dass ein Dreieck parallel zu einer Koordinatenebene liegt "
     "(gleiche Koordinate) und symmetrisch zu einer anderen ist (Vorzeichenwechsel einer Koordinate).",
     "2026MgrundlegendBAGLAA2WTR1-1a"),
    ("Körper: Volumen eines geraden Prismas über einem Dreieck nachweisen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Das Volumen eines geraden Prismas mit dreieckiger Grundfläche als Dreiecksfläche mal Kantenlänge nachweisen.",
     "2026MgrundlegendBAGLAA2WTR1-1b"),
    ("Koordinatengleichung einer Ebene durch drei Punkte bestimmen", "Analytische Geometrie", "Ebenen",
     "Für die Ebene durch drei Punkte eine Koordinatengleichung aufstellen (Normalenvektor senkrecht zu zwei "
     "Verbindungsvektoren, Konstante über einen Punkt).",
     "2026MgrundlegendBAGLAA2WTR1-1c"),
    ("Körper: Füllvolumen eines gedrehten Behälters am Graphen ergänzen und Grenzwinkel deuten", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Für einen als Körper modellierten, teilweise gefüllten Behälter, der um eine Kante gedreht wird, den Graphen "
     "Füllvolumen gegen Drehwinkel im konstanten Anfangsbereich ergänzen und den Winkel deuten, ab dem der Inhalt "
     "ausläuft.",
     "2026MgrundlegendBAGLAA2WTR1-1d"),
    ("Winkel zwischen einer Seitenfläche und der Horizontalen als Grenzwinkel im Sachzusammenhang bestimmen",
     "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Den Drehwinkel bestimmen, bei dem eine Seitenfläche eines Körpers waagerecht liegt, als Winkel zwischen der "
     "Ebene der Seitenfläche und einer Koordinatenebene über die Normalenvektoren, mit Erläuterung des Ansatzes.",
     "2026MgrundlegendBAGLAA2WTR1-1e"),
    ("Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Ein Viereck über kollineare Verbindungsvektoren zweier Seiten als Trapez nachweisen und seinen Flächeninhalt "
     "mit der Trapezformel berechnen.",
     "2026MgrundlegendBAGLAA2WTR2-1a"),
    ("Winkel zwischen zwei Kanten über das Skalarprodukt berechnen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Den Winkel zwischen zwei Kanten eines Körpers mit gemeinsamem Eckpunkt über die Winkelformel des "
     "Skalarprodukts berechnen.",
     "2026MgrundlegendBAGLAA2WTR2-1b"),
    ("Lotfußpunkt aus Geradengleichung und Orthogonalitätsbedingung im Gleichungspaar deuten", "Analytische Geometrie", "Abstände",
     "Ein vorgegebenes Gleichungspaar (Punkt auf einer Geraden, Skalarprodukt mit dem Richtungsvektor null) als "
     "Bestimmung des Lotfußpunkts eines Punktes auf die Gerade deuten.",
     "2026MgrundlegendBAGLAA2WTR2-1c"),
    ("Punkt: Mittelpunkt einer Kante nachweisen und symmetrischen Schnittpunkt angeben", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Nachweisen, dass ein Punkt Mittelpunkt einer Kante ist (Mittelpunktsformel), und einen weiteren Punkt über "
     "die Symmetrie des Körpers zu einer Koordinatenebene angeben.",
     "2026MgrundlegendBAGLAA2WTR2-1d"),
    ("Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", "Stochastik", "Binomialverteilung",
     "Eine kumulierte Wahrscheinlichkeit einer Binomialverteilung (weniger als, mehr als, höchstens) mit dem "
     "Rechner ermitteln; „mehr als“ über das Gegenereignis.",
     "2026MgrundlegendBStochastikWTR1-1b"),
    ("Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern", "Stochastik", "Binomialverteilung",
     "Erläutern, wie eine Wahrscheinlichkeit P(X = k) aus dem abgebildeten Diagramm der Verteilung von n − X "
     "(Trefferwahrscheinlichkeit 1 − p) abgelesen wird.",
     "2026MgrundlegendBStochastikWTR1-1c"),
    ("Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Eine Aussage über das Verhältnis zweier Pfadwahrscheinlichkeiten (etwa „sechsmal so groß“) durch Berechnen "
     "beider Pfade prüfen.",
     "2026MgrundlegendBStochastikWTR1-2a"),
    ("Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Einen unbekannten Ast-Anteil bestimmen, indem die Summe der Pfade zu einem Ergebnis der zweiten Stufe mit der "
     "gegebenen Randwahrscheinlichkeit gleichgesetzt wird.",
     "2026MgrundlegendBStochastikWTR1-2b"),
    ("Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen", "Stochastik",
     "Bedingte Wahrscheinlichkeit und Bayes",
     "Eine Aussage über das Wachsen einer bedingten Wahrscheinlichkeit beurteilen, indem sie als Bayes-Quotient in "
     "einem Parameter aufgestellt und die Monotonie des Bruchs begründet wird.",
     "2026MgrundlegendBStochastikWTR1-2c"),
    ("Vierfeldertafel aus Anteilen vervollständigen", "Stochastik", "Vierfeldertafel",
     "Aus zwei Randanteilen und einem Schnittanteil alle Felder einer Vierfeldertafel ergänzen.",
     "2026MgrundlegendBStochastikWTR2-1a"),
    ("Kumulierte Binomialsumme als Sachaussage formulieren", "Stochastik", "Binomialverteilung",
     "Eine gegebene Summe von Binomialtermen mit ihrem Wert als Wahrscheinlichkeitsaussage („höchstens k von n“) "
     "im Sachzusammenhang beschreiben.",
     "2026MgrundlegendBStochastikWTR2-1d"),
    ("Fehlenden Wert aus dem arithmetischen Mittel berechnen", "Stochastik", "Lage- und Streumaße einer Stichprobe",
     "Aus dem arithmetischen Mittel einer Datenreihe und den übrigen Werten den fehlenden Wert berechnen "
     "(Gesamtsumme minus Teilsumme), gegebenenfalls mit Einheitenumrechnung.",
     "2026MgrundlegendBStochastikWTR2-1e"),
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
        amt = hoechster_afb(z["afb_amtlich"])
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
