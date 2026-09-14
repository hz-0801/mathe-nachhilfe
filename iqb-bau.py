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
    "stapel": "2024-ea-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2024MerhoehtBAnalysisWTR1": 40,
        "2024MerhoehtBAnalysisWTR2": 40,
        "2024MerhoehtBAnalysisWTR3": 40,
        "2024MerhoehtBAGLAA1WTR": 25,
        "2024MerhoehtBAGLAA2WTR1": 25,
        "2024MerhoehtBStochastikWTR1": 25,
        "2024MerhoehtBStochastikWTR2": 25,
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
# Stapel 2024-ea-B, WTR-Zweig. innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Pool 2024 erhöht: Analysis 40 BE, AG/LA und Stochastik 25 BE.

SOLL = {"2024MerhoehtBAnalysisWTR1": 40, "2024MerhoehtBAnalysisWTR2": 40, "2024MerhoehtBAnalysisWTR3": 40,
        "2024MerhoehtBAGLAA1WTR": 25, "2024MerhoehtBAGLAA2WTR1": 25,
        "2024MerhoehtBStochastikWTR1": 25, "2024MerhoehtBStochastikWTR2": 25}

# ---- Analysis WTR 1, Aufgabe 1: f(x) = 4/(1 + e^x), Schar w
GL = "Koordinatensystem x von −5 bis 5, y von −5 bis 5; fallende S-Kurve von 4 (links) über den Wendepunkt (0 | 2) nach 0 (rechts); Erwartungshorizont: Sekante von (−1 | f(−1)) nach (1 | f(1)) und Tangente im Wendepunkt gestrichelt, Graph von f' als flache Mulde mit Minimum (0 | −1)"
row("2024MerhoehtBAnalysisWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Nullstellenfreiheit und Grenzwerte eines Bruchs mit e-Funktion am Term begründen", typ_neben="",
    stichwoerter="Bruch mit Zähler 4 wird nie null|x → −∞: e^x → 0, f → 4|x → +∞: Nenner → ∞, f → 0",
    voraussetzungen="Bruch ohne Nullstelle|Grenzwerte von e^x",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=GL, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 4/(1 + e^x) in IR; Graph symmetrisch zum Wendepunkt (0 | 2)",
    gesucht="Begründung ohne Nullstelle; Grenzwerte für x → ±∞",
    verfahren="Zähler betrachten, Nenner für beide Grenzfälle",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f hat keine Nullstelle, da der Funktionsterm als Bruch mit dem Zähler 4 gegeben ist; lim f(x) = 4 für x → −∞, lim f(x) = 0 für x → +∞ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Grenzwerte vertauschen",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR1", "b", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Steigung berechnen und Tangentensteigung im Wendepunkt grafisch bestimmen", typ_neben="",
    stichwoerter="(f(1) − f(−1))/(1 − (−1)) ≈ −0,92|Tangente im Wendepunkt (0 | 2) einzeichnen, Steigung etwa −1",
    voraussetzungen="Differenzenquotient|Tangente zeichnen und Steigung ablesen",
    format="Rechnung|Zeichnen", operator="Berechnen Sie|Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GL, kontext="ohne", textumfang="kurz",
    gegeben="f wie in a; Bereich −1 ≤ x ≤ 1; Wendepunkt (0 | 2)",
    gesucht="mittlere Steigung auf Hundertstel; Steigung im Wendepunkt grafisch",
    verfahren="Differenzenquotient, Tangente am Wendepunkt anlegen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="(f(1) − f(−1))/(1 − (−1)) ≈ −0,92; Steigung des Graphen im Wendepunkt etwa −1 (amtlich)",
    zwischenergebnis="f'(0) = −1 exakt", niveau_geschaetzt="I",
    fehlerquelle="Betrag statt Vorzeichen der Steigung",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Achsensymmetrie des Ableitungsgraphen aus f'(−x) = f'(x) deuten und Graphen skizzieren", typ_neben="",
    stichwoerter="f'(−x) = f'(x): Graph von f' symmetrisch zur y-Achse|f' < 0 überall, Minimum −1 bei 0, gegen 0 nach beiden Seiten",
    voraussetzungen="gerade Funktion als Achsensymmetrie|Ableitungsgraph aus dem Monotonieverlauf skizzieren",
    format="Kurzantwort|Zeichnen", operator="Geben Sie an|Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=GL, kontext="ohne", textumfang="kurz",
    gegeben="f'(−x) = f'(x) für alle x",
    gesucht="Bedeutung für den Graphen von f' und Skizze",
    verfahren="Symmetrie benennen, Graph mit Tiefpunkt (0 | −1) skizzieren",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2024MerhoehtBAnalysisWTR1-1b",
    ergebnis="der Graph von f' ist symmetrisch bezüglich der y-Achse; Skizze mit Tiefpunkt (0 | −1) und Annäherung an die x-Achse (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Graph von f' oberhalb der x-Achse zeichnen",
    bemerkung="Standardbezug: K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR1", "d", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion durch Ableiten nachweisen", typ_neben="",
    stichwoerter="F'(x) = 4 − 4/(e^x + 1) · e^x = (4(e^x + 1) − 4e^x)/(e^x + 1) = 4/(e^x + 1)",
    voraussetzungen="Ableitung von ln(e^x + 1) mit der Kettenregel|auf einen Bruch bringen",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="F(x) = 4x − 4 · ln(e^x + 1)",
    gesucht="Nachweis F' = f",
    verfahren="ableiten, zusammenfassen",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="F'(x) = 4 − 4/(e^x + 1) · e^x = (4 · (e^x + 1) − 4e^x)/(e^x + 1) = 4/(e^x + 1) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="innere Ableitung e^x vergessen",
    bemerkung="Standardbezug: K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2024MerhoehtBAnalysisWTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Lage eines Graphen unterhalb der x-Achse über eine Logarithmus-Abschätzung beurteilen", typ_neben="",
    stichwoerter="e^x + 1 > e^x ⇒ ln(e^x + 1) > ln e^x = x|4x − 4 ln(e^x + 1) < 4x − 4x = 0|Aussage richtig",
    voraussetzungen="Monotonie des Logarithmus|ln e^x = x|Abschätzung als Beweisidee",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="F wie in d; Aussage: der Graph von F verläuft vollständig unterhalb der x-Achse",
    gesucht="Beurteilung",
    verfahren="ln(e^x + 1) gegen x abschätzen",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="2024MerhoehtBAnalysisWTR1-1d",
    ergebnis="die Aussage ist richtig, da 4x − 4 · ln(e^x + 1) < 4x − 4 · ln e^x = 0 gilt (amtlich)",
    zwischenergebnis="F(5) ≈ −0,03", niveau_geschaetzt="III",
    fehlerquelle="nur Werte einsetzen statt allgemein abzuschätzen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis, bei dem die Abschätzung ln(e^x + 1) > x erst gefunden werden muss.")

row("2024MerhoehtBAnalysisWTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral über die Summe aus ungerader Funktion und Konstante ohne Stammfunktion begründen", typ_neben="",
    stichwoerter="Graph punktsymmetrisch zu (0 | 2): Flächenstücke zwischen Graph und y = 2 über [−k; 0] und [0; k] gleich groß|Integral = Rechteck 2k · 2 = 4k",
    voraussetzungen="Punktsymmetrie|Flächenausgleich|Rechteckfläche",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Term",
    material="Koordinatensystem", skizze=GL, kontext="ohne", textumfang="kurz",
    gegeben="∫_{−k}^k f(x) dx für k > 0; Graph symmetrisch zu (0 | 2)",
    gesucht="Begründung, dass der Wert ohne Stammfunktion exakt bestimmbar ist; der Wert",
    verfahren="Symmetrie zu (0 | 2) auf die Fläche übertragen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="aufgrund der Symmetrie des Graphen von f haben die beiden Flächenstücke, die der Graph und die Gerade y = 2 für −k ≤ x ≤ 0 bzw. 0 ≤ x ≤ k einschließen, den gleichen Inhalt; damit stimmt der Wert des Integrals mit dem Flächeninhalt eines Rechtecks mit den Seitenlängen 2k und 2 überein; Wert 4k (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Rechteck der Höhe 4 statt 2",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Punktsymmetrie um (0 | 2) für den Flächenausgleich ausnutzen. Typ wiederverwendet (Teil A).")

# ---- Analysis WTR 1, Aufgabe 2: Schar w_{a;b;c}, Seeadler
SCHW = "drei kleine Koordinatensysteme: I waagerechte Gerade oberhalb der x-Achse, II fallende S-Kurve gegen 0, III steigende S-Kurve von 0 aus"
row("2024MerhoehtBAnalysisWTR1", "a", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen", typ_neben="",
    stichwoerter="c = 0: konstant a/(b + 1), Graph I|c = 1: lim für x → +∞ ist 0, Graph II|c = −1: Graph III",
    voraussetzungen="Grenzverhalten je nach Vorzeichen des Exponenten|konstanter Fall",
    format="Kurzantwort|Begründung", operator="Ordnen Sie zu|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SCHW, kontext="ohne", textumfang="mittel",
    gegeben="w_{a;b;c}(x) = a/(b + e^{cx}), a, b > 0; Graphen I, II, III zu c = −1, 0, 1 bei festen a, b",
    gesucht="Zuordnung mit Begründung",
    verfahren="c = 0 als Konstante, Vorzeichen von c über den Grenzwert",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="c = 0 gehört zu I, da die Funktionswerte von w_{a;b;0} konstant sind; c = 1 zu II, da lim w_{a;b;1} = 0 für x → +∞ gilt; damit gehört c = −1 zu III (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="II und III vertauschen (Vorzeichen im Exponenten)",
    bemerkung="Standardbezug: K1 II, K2 I, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2024MerhoehtBAnalysisWTR1", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Anfangswert angeben und Zeitpunkt für einen Bestand bei logistischem Wachstum berechnen", typ_neben="",
    stichwoerter="w(0) = 40/2 = 20 Seeadler angesiedelt|w(x) = 32 ⇔ 1 + e^{−0,2x} = 5/4 ⇔ e^{−0,2x} = 1/4 ⇒ x ≈ 7",
    voraussetzungen="Funktionswert bei 0|Exponentialgleichung mit ln",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Seeadler/Population", textumfang="lang",
    gegeben="w(x) = 40/(1 + e^{−0,2x}), x Jahre seit der Ansiedlung, w(x) Anzahl der Seeadler",
    gesucht="Anzahl bei der Ansiedlung; Zeitpunkt, zu dem 32 erreicht sind",
    verfahren="w(0), Gleichung nach x auflösen",
    schritte="3", zahlenraum="ganz|Bruch|Potenz", einheiten="Jahre", abhaengig_von="",
    ergebnis="es wurden 20 Seeadler angesiedelt; w(x) = 32 ⇔ 1 + e^{−0,2x} = 5/4 ⇔ e^{−0,2x} = 1/4 liefert x ≈ 7, d. h. nach etwa sieben Jahren ist die Anzahl auf 32 angewachsen (amtlich)",
    zwischenergebnis="x = 5 ln 4 ≈ 6,93", niveau_geschaetzt="II",
    fehlerquelle="ln(1/4) = −ln 4 mit falschem Vorzeichen",
    bemerkung="Standardbezug: K3 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR1", "c", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Näherung durch die Tangente mit dem Funktionswert im Sachzusammenhang vergleichen", typ_neben="",
    stichwoerter="Tangente: 20 + 2 · 4 = 28|w(4) ≈ 27,6|etwa gleich",
    voraussetzungen="Tangente als lineare Näherung|Funktionswert",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Seeadler/Population", textumfang="mittel",
    gegeben="Tangente an den Graphen von w in (0 | w(0)) mit Steigung 2",
    gesucht="ob die Tangente nach vier Jahren dieselbe Anzahl liefert wie w",
    verfahren="beide Werte bei x = 4 berechnen und vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="Jahre", abhaengig_von="2024MerhoehtBAnalysisWTR1-2b",
    ergebnis="w(4) ≈ 27,6; bei Beschreibung mithilfe der Tangente ergeben sich 20 + 2 · 4 = 28 Seeadler und damit etwa die gleiche Anzahl (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Tangente mit Steigung w'(4) ansetzen",
    bemerkung="Standardbezug: K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR1", "d", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gleichungen eines Bestimmungssystems für Scharparameter im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="(1) a/(b + 1) = 20: Anfangsbestand 20|(2) Grenzwert 45: langfristig 45 Seeadler|(3) a/(b + e^{15c}) = 35: nach 15 Jahren 35",
    voraussetzungen="Funktionswert bei 0|Grenzwert als Langzeitverhalten|Wert an einer Stelle",
    format="Kurzantwort", operator="Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Seeadler/Population", textumfang="mittel",
    gegeben="andere Funktion der Schar w_{a;b;c}; Gleichungen (1) a/(b + 1) = 20, (2) lim a/(b + e^{cx}) = 45 für x → +∞, (3) a/(b + e^{15c}) = 35",
    gesucht="Deutung jeder Gleichung",
    verfahren="Stelle bzw. Grenzwert in Sachaussage übersetzen",
    schritte="1", zahlenraum="ganz", einheiten="Jahre", abhaengig_von="",
    ergebnis="(1) es werden 20 Seeadler angesiedelt; (2) langfristig werden laut Modell 45 Seeadler auf der Inselgruppe leben; (3) nach 15 Jahren leben laut Modell 35 Seeadler auf der Inselgruppe (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="(2) als Maximum statt Grenzwert deuten",
    bemerkung="Standardbezug: K3 II, K4 II, K6 II. AB amtlich: II. Amtlich.")

row("2024MerhoehtBAnalysisWTR1", "e", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus Anfangswert und Grenzwert über das Vorzeichen des Exponenten bestimmen", typ_neben="",
    stichwoerter="Grenzwert 45 > 20 = Anfangswert ⇒ Bestand wächst ⇒ c < 0, e^{cx} → 0 ⇒ a/b = 45|a = 45b in (1): 45b = 20b + 20 ⇒ b = 4/5, a = 36",
    voraussetzungen="Grenzwert je nach Vorzeichen von c|Fallentscheidung c < 0|Gleichungssystem",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Seeadler/Population", textumfang="kurz",
    gegeben="Gleichungen (1) bis (3) aus d",
    gesucht="Werte von a und b",
    verfahren="aus (2) und (1) das Vorzeichen von c schließen, a/b = 45, in (1) einsetzen",
    schritte="3", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="2024MerhoehtBAnalysisWTR1-2d",
    ergebnis="aus (2) und (1) folgt c < 0 und damit a/b = 45; in Verbindung mit (1) ergibt sich 45b = 20b + 20, d. h. b = 4/5, und a = 36 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Grenzwert für c > 0 (Wert 0) nehmen und Widerspruch übersehen",
    bemerkung="Standardbezug: K1 II, K2 III, K4 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: Fallunterscheidung nach dem Vorzeichen von c mit verschiedenem Ausgang (Grenzwert 0 oder a/b), verkettet mit dem Gleichungssystem.")

# ---- Analysis WTR 2, Aufgabe 1: Schar f_{a;b} = ax³ − bx
GS = "Koordinatensystem x von −4 bis 4, y von −4 bis 4; Graph von x³ − 4x mit Nullstellen −2, 0, 2, Hochpunkt bei etwa (−1,2 | 3,1), Tiefpunkt bei etwa (1,2 | −3,1)"
row("2024MerhoehtBAnalysisWTR2", "a", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Symmetrieart am Term über die Exponenten begründen", typ_neben="",
    stichwoerter="ax³ − bx enthält nur ungerade Exponenten",
    voraussetzungen="Kriterium ungerade Exponenten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GS, kontext="ohne", textumfang="kurz",
    gegeben="f_{a;b}(x) = ax³ − bx, a, b > 0",
    gesucht="Begründung der Punktsymmetrie zum Ursprung",
    verfahren="Exponenten prüfen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Term von f_{a;b} ist ein Polynom mit ausschließlich ungeraden Exponenten von x (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="f(−x) = −f(x) nur für ein Beispiel prüfen",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A).")

row("2024MerhoehtBAnalysisWTR2", "b", innen="1", seite="2", punkte="6", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Tiefpunkt einer Schar mit zwei Parametern nachweisen und Hochpunkt über die Punktsymmetrie begründen", typ_neben="",
    stichwoerter="f' = 3ax² − b, f'(√(b/3a)) = 0|f'' = 6ax > 0 an der Stelle: Tiefpunkt|Punktsymmetrie: Hochpunkt bei −√(b/3a), also links vom Tiefpunkt",
    voraussetzungen="Ableitungen mit Parametern|hinreichende Bedingung|Symmetrie überträgt Extrempunkte",
    format="Rechnung|Begründung", operator="Weisen Sie nach|Begründen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Schar f_{a;b} wie in a",
    gesucht="Nachweis eines Tiefpunkts bei x = √(b/3a); Begründung eines Hochpunkts mit kleinerer x-Koordinate",
    verfahren="f' und f'' an der Stelle, Punktsymmetrie für den Hochpunkt",
    schritte="4", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="2024MerhoehtBAnalysisWTR2-1a",
    ergebnis="f'(x) = 3ax² − b, f'(√(b/3a)) = 3a · b/3a − b = 0; f''(x) = 6ax, f''(√(b/3a)) = 6a · √(b/3a) > 0; aufgrund der Punktsymmetrie hat der Graph an der Stelle −√(b/3a) einen Hochpunkt, dessen x-Koordinate damit kleiner ist als die des Tiefpunkts (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Hochpunkt erneut mit f'' nachrechnen statt über die Symmetrie",
    bemerkung="Standardbezug: K1 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR2", "c", innen="1", seite="2", punkte="7", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen", typ_neben="",
    stichwoerter="I: f(3) = 0 ⇒ 27a − 3b = 0 ⇒ b = 9a|II: ∫_0^3 f = −40,5 (Flächenstück im vierten Quadranten)|a[1/4 x⁴ − 9/2 x²]_0^3 = −81/4 a = −40,5 ⇒ a = 2, b = 18",
    voraussetzungen="Nullstellenbedingung|Fläche unterhalb der x-Achse als negatives Integral|Gleichungssystem mit Parametern",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Funktion der Schar mit Nullstelle 3, deren Graph im vierten Quadranten mit der x-Achse ein Flächenstück vom Inhalt 40,5 einschließt",
    gesucht="a und b",
    verfahren="b = 9a aus der Nullstelle, Integral von 0 bis 3 gleich −40,5",
    schritte="4", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="I f_{a;b}(3) = 0, II ∫_0^3 f_{a;b}(x) dx = −40,5; aus I ergibt sich 27a − 3b = 0 ⇔ b = 9a; in II: ∫_0^3 (ax³ − 9ax) dx = −40,5 ⇔ a · [1/4 x⁴ − 9/2 x²]_0^3 = −40,5 ⇔ −81/4 a = −40,5 ⇔ a = 2; b = 18 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Integral positiv ansetzen (Vorzeichen des Flächenstücks unter der Achse)",
    bemerkung="Standardbezug: K1 II, K2 III, K4 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Flächenstück im vierten Quadranten in ein negatives Integral von 0 bis zur Nullstelle übersetzen, verkettet mit der Nullstellenbedingung.")

row("2024MerhoehtBAnalysisWTR2", "d", innen="1", seite="2", punkte="7", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Flächeninhalt des Dreiecks aus Tangente, Gerade und x-Achse berechnen", typ_neben="",
    stichwoerter="f'(x) = 3x² − 4, f'(2) = 8, t: y = 8x − 16|Schnitt mit g: 8x − 16 = −x − 2 ⇒ x = 14/9, y = −32/9|Dreieck mit Ecken A(2 | 0), (−2 | 0), Schnittpunkt: 1/2 · 4 · 32/9 = 64/9",
    voraussetzungen="Tangentengleichung|Schnittpunkt zweier Geraden|Nullstelle von g|Dreiecksfläche",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GS, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − 4x; Tangente in A(2 | 0); Gerade g: y = −x − 2",
    gesucht="Flächeninhalt des von t, x-Achse und g eingeschlossenen Dreiecks",
    verfahren="t aufstellen, Schnittpunkt mit g, Grundseite auf der x-Achse, Höhe",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 3x² − 4, f'(2) = 8; 0 = 8 · 2 + n ⇔ n = −16, Tangente y = 8x − 16; Schnittpunkt mit g: 8x − 16 = −x − 2 ⇔ x = 14/9, y = −14/9 − 2 = −32/9; Flächeninhalt 1/2 · 4 · 32/9 = 64/9 (amtlich)",
    zwischenergebnis="g schneidet die x-Achse bei −2", niveau_geschaetzt="II",
    fehlerquelle="Grundseite 2 statt 4 (Nullstelle von g bei −2 übersehen)",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR2", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Mittelpunkte der Strecken zum Ursprung auf einem gegebenen Graphen allgemein nachweisen", typ_neben="",
    stichwoerter="P(x | f(x)), Mittelpunkt (x/2 | f(x)/2)|h(x/2) = 4 (x/2)³ − 4 · x/2 = 1/2 (x³ − 4x) = 1/2 f(x)",
    voraussetzungen="Mittelpunkt als halbe Koordinaten|Punktprobe mit Parameter x",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = x³ − 4x; h(x) = 4x³ − 4x; Aussage: der Mittelpunkt von P und O liegt für jeden Graphenpunkt P auf dem Graphen von h",
    gesucht="Begründung der Aussage",
    verfahren="Mittelpunkt allgemein ansetzen, in h einsetzen",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="bezeichnet x die x-Koordinate eines Graphenpunkts P, so ist nachzuweisen, dass (x/2 | f(x)/2) auf dem Graphen von h liegt: h(x/2) = 4 · (x/2)³ − 4 · x/2 = 1/2 · (x³ − 4x) = 1/2 · f(x) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur einen konkreten Punkt prüfen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis mit Parameter, bei dem die Beziehung h(x/2) = f(x)/2 hergeleitet wird.")

# ---- Analysis WTR 2, Aufgabe 2: Lesebestätigungen
row("2024MerhoehtBAnalysisWTR2", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen", typ_neben="",
    stichwoerter="(4364 − 1701)/1,5 ≈ 1775 je Stunde",
    voraussetzungen="Differenzenquotient aus Tabellenwerten|Zeitraum in Stunden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle Zeitpunkt 7:30 bis 15:00 Uhr mit bis dahin eingegangenen Lesebestätigungen: 252, 899, 1701, 2627, 3503, 4364, …, 7552, 7572", kontext="Lesebestätigungen/E-Mail", textumfang="mittel",
    gegeben="Tabelle der bis zum Zeitpunkt eingegangenen Lesebestätigungen; 8:30 Uhr 1701, 10:00 Uhr 4364",
    gesucht="mittlere Anzahl je Stunde von 8:30 bis 10:00 Uhr",
    verfahren="Differenz durch 1,5 Stunden",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="Stunden", abhaengig_von="",
    ergebnis="(4364 − 1701)/1,5 ≈ 1775 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="durch 3 Halbstunden statt durch 1,5 teilen",
    bemerkung="Standardbezug: K2 I, K3 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-B), hier aus der Tabelle statt aus dem Graphen – Vorschlag für den Abgleich: Definition auf Tabelle erweitern.")

row("2024MerhoehtBAnalysisWTR2", "b", innen="2", seite="3", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="k(2) = u(2) = 800 − 3600 + 4600 = 1800|um 9:00 Uhr momentane Änderungsrate 1800 je Stunde",
    voraussetzungen="richtigen Abschnitt wählen (x = 2 < 3: u)|Deutung als Rate",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Interpretieren Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Lesebestätigungen/E-Mail", textumfang="lang",
    gegeben="k(x) = u(x) = 100x³ − 900x² + 2300x für 0 ≤ x < 3, v(x) = 20x² − 520x + 2880 für 3 ≤ x ≤ 8; x Stunden seit 7:00 Uhr, k(x) momentane Änderungsrate der Anzahl der Lesebestätigungen in 1/h",
    gesucht="k(2) und Deutung",
    verfahren="u(2) berechnen, als Rate um 9:00 Uhr deuten",
    schritte="2", zahlenraum="ganz", einheiten="1/h|Stunden", abhaengig_von="",
    ergebnis="k(2) = 1800, d. h. um 9:00 Uhr beträgt die momentane Änderungsrate der Anzahl der seit 7:00 Uhr eingegangenen Lesebestätigungen laut Modell 1800 1/h (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="k(2) als Anzahl der Bestätigungen um 9:00 Uhr deuten",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2024MerhoehtBAnalysisWTR2", "c", innen="2", seite="3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Eignung eines Modells über das Vorzeichen der Änderungsrate nach einer Nullstelle beurteilen", typ_neben="",
    stichwoerter="v(x) = 20(x − 18)(x − 8) wechselt bei 8 das Vorzeichen von plus nach minus|nach 15:00 Uhr negative Änderungsrate: unmöglich (Anzahl kann nicht sinken)",
    voraussetzungen="Vorzeichenwechsel aus der Faktorisierung|Rate einer Anzahl kann nicht negativ sein",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Lesebestätigungen/E-Mail", textumfang="kurz",
    gegeben="v(x) = 20 · (x − 18) · (x − 8)",
    gesucht="Begründung, dass v nach 15:00 Uhr (x > 8) ungeeignet ist",
    verfahren="Vorzeichen von v für x etwas größer als 8",
    schritte="2", zahlenraum="ganz", einheiten="Stunden", abhaengig_von="",
    ergebnis="da v(x) an der Stelle 8 sein Vorzeichen von plus nach minus ändert, würden sich unmittelbar nach 15:00 Uhr negative Änderungsraten ergeben, was in diesem Sachzusammenhang unmöglich ist (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit der Nullstelle 18 argumentieren",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR2", "d", innen="2", seite="3", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten", typ_neben="Prozentuale Abweichung eines Näherungswerts vom exakten Wert berechnen",
    stichwoerter="10:00 bis 15:00 Uhr: x von 3 bis 8, Abschnitt v|∫_3^8 v = [20/3 x³ − 260x² + 2880x]_3^8 ≈ 3333|Tabelle: 7572 − 4364 = 3208|Abweichung (3333 − 3208)/3208 ≈ 3,9 %",
    voraussetzungen="Zeitraum auf den richtigen Abschnitt abbilden|Integral der Rate als Anzahl|Tabellendifferenz|relative Abweichung",
    format="Rechnung", operator="Berechnen Sie|Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle wie in a", kontext="Lesebestätigungen/E-Mail", textumfang="mittel",
    gegeben="k wie in b; Tabellenwerte 4364 (10:00 Uhr) und 7572 (15:00 Uhr)",
    gesucht="Anzahl der Lesebestätigungen von 10:00 bis 15:00 Uhr laut Modell; prozentuale Abweichung vom Tabellenwert",
    verfahren="Integral über v von 3 bis 8, Differenz der Tabellenwerte, Quotient",
    schritte="4", zahlenraum="ganz|Bruch|Prozent", einheiten="Stunden", abhaengig_von="",
    ergebnis="∫_3^8 k(x) dx = [20/3 x³ − 260x² + 2880x]_3^8 ≈ 3333; (3333 − (7572 − 4364))/(7572 − 4364) ≈ 3,9 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Integral über u statt v oder Grenzen 10 bis 15",
    bemerkung="Standardbezug: K1 I, K2 II, K3 II, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B), Abweichung als typ_neben (2025-ga-B).")

# ---- Analysis WTR 3, Aufgabe 1: Rutschbahn f(x) = 3(x + 10) e^{−0,1x}
RUT = "Koordinatensystem x von 0 bis 45, y von 0 bis 30; fallender Graph von (0 | 30) über den Wendepunkt bei x = 10 (etwa 22) nach (44 | 2); Erwartungshorizont b: Sekante von (0 | 30) nach (44 | 2) und Gerade durch (0 | 30) und (30 | 0) gestrichelt"
row("2024MerhoehtBAnalysisWTR3", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="f(0) − f(44) ≈ 28,0|1 LE = 10 cm: 280 cm",
    voraussetzungen="zwei Funktionswerte|Maßstab",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=RUT, kontext="Rutschbahn", textumfang="lang",
    gegeben="f(x) = 3 · (x + 10) · e^{−0,1x}, 0 ≤ x ≤ 44 Längsschnitt einer Rutschbahn; 1 LE = 10 cm",
    gesucht="Höhenunterschied zwischen Anfang und Ende",
    verfahren="f(0) − f(44), mal 10 cm",
    schritte="2", zahlenraum="dezimal", einheiten="cm", abhaengig_von="",
    ergebnis="f(0) − f(44) ≈ 28,0; der Höhenunterschied beträgt etwa 280 cm (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Maßstab vergessen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2024MerhoehtBAnalysisWTR3", "b", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Sekantenwinkel gegen eine Schranke am Graphen beurteilen", typ_neben="",
    stichwoerter="Gerade durch (0 | 30) und (30 | 0) hat Neigung 45°|Sekante von Anfang zu Ende verläuft flacher|Kriterium I erfüllt",
    voraussetzungen="45°-Gerade als Steigung −1|Vergleich der Sekante mit der Hilfsgeraden",
    format="Begründung|Zeichnen", operator="Beurteilen Sie|Veranschaulichen Sie", antwort="Text",
    material="Koordinatensystem", skizze=RUT, kontext="Rutschbahn", textumfang="mittel",
    gegeben="Kriterium I: der durch Anfangs- und Endpunkt festgelegte Winkel gegen die Horizontale höchstens 45°",
    gesucht="Beurteilung ohne Rechnung mit Eintragung in der Abbildung",
    verfahren="45°-Gerade durch den Anfangspunkt und Sekante einzeichnen und vergleichen",
    schritte="2", zahlenraum="ganz", einheiten="°", abhaengig_von="",
    ergebnis="die Gerade durch (0 | 30) und (30 | 0) schließt mit der x-Achse einen Winkel von 45° ein und verläuft steiler als die eingezeichnete Sekante; das Sicherheitskriterium I ist erfüllt (amtlich)",
    zwischenergebnis="Sekantensteigung ≈ −0,64, Winkel ≈ 32°", niveau_geschaetzt="II",
    fehlerquelle="Tangente am Anfang statt Sekante betrachten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR3", "c", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Maximalen Neigungswinkel über die Wendestelle berechnen und mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="f''(x) = 0 ⇔ x = 10, laut Abbildung Wendestelle (steilste Stelle)|tan α = f'(10) ⇒ α ≈ −48°|Betrag unter 60°: Kriterium II erfüllt",
    voraussetzungen="steilste Stelle als Wendestelle|Steigungswinkel über den Tangens",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=RUT, kontext="Rutschbahn", textumfang="kurz",
    gegeben="f'(x) = −0,3x · e^{−0,1x}, f''(x) = 0,03 · (x − 10) · e^{−0,1x}; Kriterium II: nirgends Neigung über 60°",
    gesucht="rechnerische Prüfung von Kriterium II",
    verfahren="Wendestelle aus f'' = 0, Winkel aus f'(10)",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="°", abhaengig_von="",
    ergebnis="aus f''(x) = 0 ⇔ x = 10 ergibt sich in Verbindung mit der Abbildung 10 als Wendestelle; tan α = f'(10) ⇒ α ≈ −48°; das Sicherheitskriterium II ist erfüllt (amtlich)",
    zwischenergebnis="f'(10) ≈ −1,10", niveau_geschaetzt="II",
    fehlerquelle="Winkel am Anfang (f'(0) = 0) prüfen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR3", "d", innen="1", seite="2", punkte="6", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Länge der Normalen vom Graphenpunkt bis zur x-Achse berechnen", typ_neben="",
    stichwoerter="Normalensteigung m = −1/f'(40) = e⁴/12|b = f(40) − m · 40|Nullstelle der Normalen x1 ≈ 39,4|Länge √(f(40)² + (40 − x1)²) ≈ 2,8 → 28 cm",
    voraussetzungen="Normale als Gerade mit negativem Kehrwert|Schnitt mit der x-Achse|Abstand zweier Punkte|Maßstab",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=RUT, kontext="Rutschbahn", textumfang="mittel",
    gegeben="Strebe von P(40 | f(40)) senkrecht zur Tangente in P bis zur x-Achse (Erdboden); 1 LE = 10 cm",
    gesucht="Länge der Strebe",
    verfahren="Normale aufstellen, Nullstelle, Abstand",
    schritte="4", zahlenraum="dezimal|Potenz", einheiten="cm", abhaengig_von="",
    ergebnis="die Strecke ist Teil der Geraden y = m · x + b mit m = −1/f'(40) = e⁴/12 und b = f(40) − e⁴/12 · 40 = 150 · e^−4 − 10 · e⁴/3; 0 = e⁴/12 · x + 150 · e^−4 − 10 · e⁴/3 führt zu x1 ≈ 39,4; √((f(40))² + (40 − x1)²) ≈ 2,8; die Strebe hat eine Länge von etwa 28 cm (amtlich)",
    zwischenergebnis="f(40) ≈ 2,75", niveau_geschaetzt="II",
    fehlerquelle="Länge nur als f(40) (senkrecht zum Boden statt zur Tangente)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis WTR 3, Aufgabe 2: Schar f_k = k(x + 10) e^{−0,1x}
row("2024MerhoehtBAnalysisWTR3", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben", typ_neben="",
    stichwoerter="k · e^{−0,1x} ≠ 0 ⇒ nur x = −10|x → −∞: −∞ für k > 0, +∞ für k < 0",
    voraussetzungen="Nullprodukt|Vorzeichen von k bestimmt den Grenzwert",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_k(x) = k · (x + 10) · e^{−0,1x}, k ≠ 0",
    gesucht="Begründung der einzigen Nullstelle −10; Verhalten für x → −∞ nach k",
    verfahren="Faktoren betrachten, Fallunterscheidung nach dem Vorzeichen von k",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="wegen k · e^{−0,1x} ≠ 0 ist −10 die einzige Lösung von f_k(x) = 0; lim f_k(x) = −∞ für k > 0 und +∞ für k < 0 (x → −∞) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Fallunterscheidung nach k vergessen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-B), hier mit Parameter.")

row("2024MerhoehtBAnalysisWTR3", "b", innen="2", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Extrempunkt einer Schar mit Art nach dem Parametervorzeichen bestimmen", typ_neben="",
    stichwoerter="f_k'(x) = k(e^{−0,1x} − 0,1(x + 10) e^{−0,1x}) = −0,1 k x e^{−0,1x}|f_k' = 0 ⇔ x = 0, f_k(0) = 10k|Extrempunkt (0 | 10k); mit Nullstelle −10: Hochpunkt für k > 0, Tiefpunkt für k < 0",
    voraussetzungen="Produkt- und Kettenregel mit Parameter|Art über Vergleich mit der Nullstelle oder Vorzeichen von f'",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_k wie in a; genau ein Extrempunkt je Graph",
    gesucht="Koordinaten und Art des Extrempunkts in Abhängigkeit von k",
    verfahren="f_k' faktorisieren, Nullstelle, Art nach k",
    schritte="3", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="2024MerhoehtBAnalysisWTR3-2a",
    ergebnis="f_k'(x) = k · (e^{−0,1x} − 0,1 · (x + 10) · e^{−0,1x}) = −0,1 · k · x · e^{−0,1x}; f_k'(x) = 0 ⇔ x = 0; f_k(0) = 10k; Extrempunkt (0 | 10k); unter Berücksichtigung der Nullstelle −10 folgt, dass für positive k ein Hoch-, für negative k ein Tiefpunkt vorliegt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Art des Extremums ohne Fallunterscheidung nach k",
    bemerkung="Standardbezug: K1 I, K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR3", "c", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Abstand der y-Achsenabschnitte zweier benachbarter Scharkurven berechnen", typ_neben="",
    stichwoerter="f_{k+1}(0) − f_k(0) = (k + 1) · 10 − k · 10 = 10",
    voraussetzungen="y-Achsenabschnitt 10k|Differenz",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="G_k und G_{k+1} für k ≠ −1",
    gesucht="Abstand der Schnittpunkte mit der y-Achse",
    verfahren="Differenz der Werte bei 0",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_{k+1}(0) − f_k(0) = (k + 1) · 10 − k · 10 = 10 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Abstand als 10(k + 1) angeben",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR3", "d", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Spiegelung an der x-Achse als Scharmitglied nachweisen", typ_neben="",
    stichwoerter="Spiegelung an der x-Achse: −f_k(x) = −k(x + 10) e^{−0,1x} = f_{−k}(x)|Aussage wahr",
    voraussetzungen="Spiegelung an der x-Achse als Vorzeichenwechsel|Parameter −k zulässig (k ≠ 0)",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Aussage: Spiegelt man einen beliebigen Graphen der Schar an der x-Achse, so entsteht ein anderer Graph der Schar",
    gesucht="Beurteilung",
    verfahren="−f_k als f_{−k} erkennen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="−f_k(x) = −k · (x + 10) · e^{−0,1x} = f_{−k}(x); die Aussage ist wahr (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Spiegelung an der y-Achse prüfen",
    bemerkung="Standardbezug: K1 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAnalysisWTR3", "e", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Gerade zur Halbierung der Fläche zwischen Scharkurve und Koordinatenachsen ermitteln", typ_neben="",
    stichwoerter="Fläche im zweiten Quadranten: ∫_{−10}^0 f_k = F_k(0) − F_k(−10) = 100k(e − 2)|h_k geht durch die Nullstelle (−10 | 0) (schneidet G_k für x < 0 nur auf der x-Achse) mit Achsenabschnitt b_k|Dreieck 1/2 · 10 · b_k = 50k(e − 2) ⇒ b_k = 10k(e − 2), m_k = b_k/10 = k(e − 2)",
    voraussetzungen="Fläche über die Stammfunktion|Gerade durch die Nullstelle als Dreiecksteiler|Dreiecksfläche gleich halber Fläche",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="lang",
    gegeben="k > 0; F_k(x) = −10k · (x + 20) · e^{−0,1x} Stammfunktion; Fläche zwischen G_k und den Koordinatenachsen im zweiten Quadranten; Gerade h_k halbiert sie und schneidet G_k für x < 0 nur auf der x-Achse",
    gesucht="Gleichung von h_k",
    verfahren="Gesamtfläche, Gerade durch (−10 | 0) mit Achsenabschnitt b_k aus der Dreiecksfläche",
    schritte="4", zahlenraum="Potenz|ganz", einheiten="", abhaengig_von="",
    ergebnis="Flächeninhalt eines der beiden Flächenstücke: 1/2 · ∫_{−10}^0 f_k(x) dx = 1/2 · (F_k(0) − F_k(−10)) = 1/2 · ((−200k) − (−100k · e)) = 50k(e − 2); h_k: y = m_k · x + b_k mit 1/2 · 10 · b_k = 50k(e − 2) ⇔ b_k = 10k(e − 2) und m_k = b_k/10 = k(e − 2) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Gerade durch den Ursprung statt durch die Nullstelle ansetzen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Bedingung „schneidet G_k nur auf der x-Achse“ in eine Gerade durch die Nullstelle übersetzen und die Halbierung als Dreiecksfläche ansetzen.")

row("2024MerhoehtBAnalysisWTR3", "f", innen="2", seite="2", punkte="6", afb_amtlich="II|III",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Aufgabenstellung zu einer Extremwertaufgabe mit Dreiecksfläche aus dem Lösungsweg formulieren und Schritte erläutern", typ_neben="",
    stichwoerter="p_k(u) = 1/2 (u + 10) f_k(u): Dreieck mit Grundseite von −10 bis u und Höhe f_k(u)|(2), (3): u = 10 einziges Extremum, Maximum|(4) größter Flächeninhalt ≈ 73,6k",
    voraussetzungen="Term als Dreiecksfläche lesen|notwendige und hinreichende Bedingung|Aufgabenstellung formulieren",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Erläutern Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Schritte (1) p_k(u) = 1/2 · (u + 10) · f_k(u), (2) p_k'(u) = 0 ⇔ u = 10, (3) p_k''(10) < 0, (4) p_k(10) ≈ 73,6 · k; Punkte (−10 | 0) und (u | 0), u > −10",
    gesucht="passende Aufgabenstellung und Erläuterung der Schritte",
    verfahren="Dreieck mit den Ecken (−10 | 0), (u | 0), (u | f_k(u)) erkennen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Aufgabenstellung: Bestimmen Sie in Abhängigkeit von k den größten Flächeninhalt eines Dreiecks mit den Eckpunkten (−10 | 0), (u | 0) und (u | f_k(u)); Erläuterung: p_k gibt den Flächeninhalt eines solchen Dreiecks an (Grundseite u + 10, Höhe f_k(u)); in den Schritten (2) und (3) wird der Wert von u bestimmt, für den p_k als einziges Extremum ein Maximum annimmt; dieses Maximum beträgt etwa 73,6 · k (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Dreieck mit Ecke im Ursprung statt in (−10 | 0)",
    bemerkung="Standardbezug: K1 III, K2 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Term als Dreiecksfläche und Ableitungsschritte als Extremwertbestimmung – zwei Deutungen verkettet.")

# ---- AG/LA (A1) WTR: Population mit Parameter k, Dreieck
row("2024MerhoehtBAGLAA1WTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="Knoten J, M, A|Pfeile J→J k, J→M 0,8, M→J 0,4, M→A 0,6, A→J 0,05, A→A 0,4",
    voraussetzungen="Spalte = Herkunft|Parameter k als Beschriftung",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Population/Altersklassen", textumfang="lang",
    gegeben="v_{n+1} = P · v_n mit P = ((k; 0,4; 0,05), (0,8; 0; 0), (0; 0,6; 0,4)), k ≥ 0; Komponenten J, M, A",
    gesucht="Übergangsdiagramm",
    verfahren="Matrixspalten als ausgehende Pfeile",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Übergangsdiagramm mit sechs Pfeilen, darunter die Schleifen J (k) und A (0,4) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen als Herkunft",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A). Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MerhoehtBAGLAA1WTR", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixparameter aus einer Komponente nach zwei Schritten bestimmen", typ_neben="",
    stichwoerter="P · (200; 0; 0) = (200k; 160; 0)|P · (200k; 160; 0) hat J = 200k² + 64 = 66|k = 0,1 (k ≥ 0)",
    voraussetzungen="zwei Übergangsschritte mit Parameter|quadratische Gleichung|Vorzeichenbedingung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Population/Altersklassen", textumfang="mittel",
    gegeben="Start 200 junge Tiere; nach zwei Jahren 66 junge Tiere",
    gesucht="Wert von k",
    verfahren="P² · v_0 berechnen, erste Komponente gleich 66",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="P² · (200; 0; 0) = (66; M; A) ⇔ P · (200k; 160; 0) = (66; M; A) ⇒ 200k² + 64 = 66 ⇒ k = 0,1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="k = −0,1 nicht verwerfen",
    bemerkung="Standardbezug: K1 I, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MerhoehtBAGLAA1WTR", "c", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Konstanten Faktor der Komponentensumme von Q · u über die Spaltensummen nachweisen", typ_neben="",
    stichwoerter="Q · u = (0,2u1 + 0,3u2 + 0,2u3; 0,7u1; 0,6u2 + 0,7u3)|Summe (0,2 + 0,7)u1 + (0,3 + 0,6)u2 + (0,2 + 0,7)u3 = 0,9(u1 + u2 + u3)",
    voraussetzungen="Matrix-Vektor-Produkt allgemein|Summanden nach u_i ordnen|Spaltensummen 0,9",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Population/Altersklassen", textumfang="mittel",
    gegeben="Q = ((0,2; 0,3; 0,2), (0,7; 0; 0), (0; 0,6; 0,7)); Aussage: für jeden Vektor u ist die Komponentensumme von Q · u das 0,9-Fache der Komponentensumme von u",
    gesucht="Nachweis der Aussage",
    verfahren="Q · u mit allgemeinem u, Komponenten addieren",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="mit u = (u1; u2; u3) gilt Q · u = (0,2u1 + 0,3u2 + 0,2u3; 0,7u1; 0,6u2 + 0,7u3); Summe der Komponenten (0,2 + 0,7)u1 + (0,3 + 0,6)u2 + (0,2 + 0,7)u3 = 0,9 · (u1 + u2 + u3) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur ein Zahlenbeispiel",
    bemerkung="Standardbezug: K1 III, K2 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Geschätzt II: Nachrechnen mit mitgeführtem Vektor (Prinzip); amtlich III über K1. Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MerhoehtBAGLAA1WTR", "d", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zeitpunkt für das Unterschreiten eines Anteils der Populationsgröße über einen konstanten Faktor bestimmen", typ_neben="",
    stichwoerter="G_{n+1} = 0,9 G_n (aus c) ⇒ G_n = 0,9^n G_0|0,9^n < 0,2 ⇔ n > ln 0,2/ln 0,9 ≈ 15,3|nach 16 Jahren erstmals",
    voraussetzungen="Ergebnis aus c als Rekursion|exponentielle Abnahme|Ungleichung mit Logarithmus, ganzzahlig aufrunden",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Population/Altersklassen", textumfang="mittel",
    gegeben="andere Population mit Matrix Q; Größe = Summe aller Tiere",
    gesucht="nach wie vielen Jahren die Größe erstmals unter 20 % des Anfangswerts liegt",
    verfahren="Faktor 0,9 je Jahr, Exponentialungleichung",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="Jahre", abhaengig_von="2024MerhoehtBAGLAA1WTR-1c",
    ergebnis="mit G_n für die Größe nach n Jahren gilt gemäß c G_{n+1} = 0,9 · G_n, damit G_n = 0,9^n · G_0; 0,9^n · G_0 < 0,2 · G_0 ⇔ 0,9^n < 0,2, es folgt n > ln(0,2)/ln(0,9) ≈ 15,3; nach 16 Jahren ist dies zum ersten Mal der Fall (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="15 statt 16 (nicht aufrunden)",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Aussage aus c in die Rekursion der Populationsgröße übersetzen, verkettet mit der Exponentialungleichung. Aufgabengruppe A1, außerhalb der Geltung.")

DREI = "Schrägbild: Dreieck ABC mit A im Ursprung, B(−3 | −4 | 0) in der xy-Ebene und C(0 | 0 | 12) auf der z-Achse"
row("2024MerhoehtBAGLAA1WTR", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Rechten Winkel aus der Lage zu den Koordinatenachsen begründen", typ_neben="",
    stichwoerter="AB liegt in der xy-Ebene, C auf der z-Achse|z-Achse senkrecht zur xy-Ebene ⇒ rechter Winkel bei A",
    voraussetzungen="Koordinatenachse senkrecht zur Koordinatenebene",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=DREI, kontext="ohne", textumfang="kurz",
    gegeben="A(0 | 0 | 0), B(−3 | −4 | 0), C(0 | 0 | 12); Umfang 30",
    gesucht="Begründung, dass ABC rechtwinklig ist",
    verfahren="Lage von AB und AC zu den Achsen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="das Dreieck ABC hat einen rechten Winkel bei A, denn AB liegt in der xy-Ebene und C auf der z-Achse (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="rechten Winkel bei B vermuten",
    bemerkung="Standardbezug: K1 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MerhoehtBAGLAA1WTR", "b", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Eckpunkt auf einer Achse aus dem Umfang eines Dreiecks bestimmen", typ_neben="",
    stichwoerter="|AB| = 5, |AC*| = z, |BC*| = √(25 + z²)|5 + z + √(25 + z²) = 15 ⇒ √(25 + z²) = 10 − z ⇒ 25 + z² = 100 − 20z + z² ⇒ z = 3,75",
    voraussetzungen="Seitenlängen mit Parameter|Wurzelgleichung durch Isolieren und Quadrieren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=DREI, kontext="ohne", textumfang="kurz",
    gegeben="C*(0 | 0 | z), z > 0; Umfang von ABC* halb so groß wie der von ABC (30)",
    gesucht="z-Koordinate von C*",
    verfahren="Umfang als Gleichung in z, Wurzel isolieren",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="5 + z + √(3² + 4² + z²) = 1/2 · 30 ⇒ √(25 + z²) = 10 − z ⇒ 25 + z² = 100 − 20z + z² ⇒ z = 3,75 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Quadrieren ohne Isolieren der Wurzel",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MerhoehtBAGLAA1WTR", "c", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Bildpunkte einer Drehung um eine Koordinatenachse mit vorgegebener Koordinate angeben", typ_neben="",
    stichwoerter="Drehung um AC (z-Achse): B* in der xy-Ebene mit |AB*| = 5|eine Koordinate 3: (3 | 4 | 0), (3 | −4 | 0), (4 | 3 | 0)",
    voraussetzungen="Drehung um die z-Achse erhält z und den Abstand zur Achse|Pythagoras mit 3, 4, 5",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Körper", skizze=DREI, kontext="ohne", textumfang="kurz",
    gegeben="Dreieck ABC wird um die Seite AC gedreht; Dreiecke AB*C",
    gesucht="drei Punkte B*, bei denen jeweils eine Koordinate 3 ist",
    verfahren="Kreis um A mit Radius 5 in der xy-Ebene, Punkte mit Koordinate 3",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="B*(3 | 4 | 0), B*(3 | −4 | 0), B*(4 | 3 | 0) (amtlich)",
    zwischenergebnis="auch (−3 | ±4 | 0), (−4 | 3 | 0), (4 | 3 | 0) möglich", niveau_geschaetzt="II",
    fehlerquelle="z-Koordinate 3 wählen (verlässt die Kreisbahn)",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA (A2) WTR 1: quadratische Pyramide ABCDS, Ebenenschar
PYR = "Abb. 1: Schrägbild der Pyramide ABCDS mit quadratischer Grundfläche (A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0)) in der xy-Ebene, O im Zentrum, Spitze S(0 | 0 | 4); Abb. 2 zusätzlich mit einer Spurgeraden g_k in der xy-Ebene und dem Lotfußpunkt R_k; Erwartungshorizont g: R_1 auf der Kante BC bei (3 | 0 | 0), R_{−1} auf AD bei (−3 | 0 | 0)"
row("2024MerhoehtBAGLAA2WTR1", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen", typ_neben="",
    stichwoerter="Seitenfläche 1/2 · 6 · √(4² + 3²) = 15|Oberfläche 6 · 6 + 4 · 15 = 96",
    voraussetzungen="Höhe einer Seitenfläche über Pythagoras|Grundfläche plus vier Dreiecke",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="kurz",
    gegeben="A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0), S(0 | 0 | 4)",
    gesucht="Oberflächeninhalt der Pyramide",
    verfahren="Seitenhöhe, Dreiecksfläche, Summe",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="Inhalt einer Seitenfläche 1/2 · 6 · √(4² + 3²) = 15; Inhalt der Oberfläche 6 · 6 + 4 · 15 = 96 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Kantenlänge |SC| statt Seitenhöhe",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAGLAA2WTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebene einer Pyramide unter vorgegebenen Gleichungen auswählen und eine ausschließen", typ_neben="",
    stichwoerter="(3) x + y = 0: Diagonalebene durch B, D, S – Symmetrieebene|(1) x − z = 0 enthält S nicht (0 − 4 ≠ 0): keine Symmetrieebene|(2) x + y + z = 4 enthält S, aber nicht O",
    voraussetzungen="Symmetrieebene enthält die Spitze und die Achse|Punktprobe",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="mittel",
    gegeben="Gleichungen (1) x − z = 0, (2) x + y + z = 4, (3) x + y = 0; genau eine beschreibt eine Symmetrieebene",
    gesucht="die Symmetrieebene; Begründung für eine der anderen",
    verfahren="Ebene durch S und O suchen, Gegenbeispiel über Punktprobe",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(3) beschreibt eine Ebene, die Symmetrieebene der Pyramide ist; die Koordinaten von S erfüllen Gleichung (1) nicht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="(2) wegen S ∈ Ebene für die Symmetrieebene halten",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAGLAA2WTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="CD = (−6; 0; 0) ⇒ n1 = 0|CS = (−3; −3; 4): −3n2 + 4n3 = 0 ⇒ n = (0; 4; 3)|4y + 3z = d, C: d = 12",
    voraussetzungen="Normalenvektor aus Skalarprodukten|Punkt einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="kurz",
    gegeben="Ebene E durch C, D, S; Kontrolle 4y + 3z = 12",
    gesucht="Koordinatengleichung von E",
    verfahren="Skalarprodukte mit CD und CS, d aus C",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(−6; 0; 0) · n = 0 liefert n1 = 0, (−3; −3; 4) · n = 0 liefert n3 = 3/4 n2; damit ist (0; 4; 3) ein Normalenvektor von E; E: 4y + 3z = d, aus C ∈ E ergibt sich d = 12 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="d aus S: 12 (gleich, aber Kontrolle nötig)",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Lauf 7).")

row("2024MerhoehtBAGLAA2WTR1", "d", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lösungsweg für den Punkt gleichen Abstands zu allen Seitenflächen einer Pyramide erläutern", typ_neben="",
    stichwoerter="I: Lotgerade zu E durch P(0 | 0 | p) mit dem Normalenvektor (0; 4; 3)|II: Q liegt in E – Schnittpunkt der Lotgeraden mit E, also Lotfußpunkt|III: |PQ| = p – Abstand zu E gleich Abstand zur Grundfläche (z = 0), also p; Symmetrie liefert die übrigen Seitenflächen",
    voraussetzungen="Lotgerade und Lotfußpunkt|Abstand Punkt–Ebene als Lotlänge|Abstand zur Grundfläche gleich z-Koordinate|Symmetrie der Pyramide",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="lang",
    gegeben="P(0 | 0 | p) im Innern mit gleichem Abstand zu allen vier Seitenflächen und zur Grundfläche; Gleichungssystem I OQ = (0; 0; p) + t · (0; 4; 3), II 4 · 4t + 3 · (p + 3t) = 12, III |PQ| = p",
    gesucht="Erläuterung der geometrischen Überlegungen",
    verfahren="jede Gleichung als Lot, Lotfußpunkt, Abstandsgleichheit deuten",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2024MerhoehtBAGLAA2WTR1-1c",
    ergebnis="Q ist ein Punkt der Lotgeraden zu E durch P; Q liegt außerdem in E und ist damit der Schnittpunkt der Lotgeraden mit E; der Abstand von P zu E stimmt mit dem Abstand von P zur Grundfläche überein (amtlich)",
    zwischenergebnis="p = 1,5", niveau_geschaetzt="III",
    fehlerquelle="III als Abstand zur Spitze deuten",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (p = 1,5). Eichregel: (d) drei Deutungen verkettet – Lotgerade, Lotfußpunkt, Abstandsgleichheit mit der Grundfläche.")

row("2024MerhoehtBAGLAA2WTR1", "e", innen="1", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Gemeinsamen Punkt aller Ebenen einer Schar nachweisen", typ_neben="",
    stichwoerter="4k · 0 + 4√(1 − k²) · 0 + 3 · 4 = 12 für alle k",
    voraussetzungen="Punktprobe mit Parameter",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E_k: 4k · x + 4√(1 − k²) · y + 3z = 12, k ∈ [−1; 1]; S(0 | 0 | 4)",
    gesucht="Nachweis S ∈ E_k für alle k",
    verfahren="S einsetzen",
    schritte="1", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="wegen 4k · 0 + 4√(1 − k²) · 0 + 3 · 4 = 12 gilt S ∈ E_k (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="keine",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAGLAA2WTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Schnittwinkel einer Geraden mit allen Ebenen einer Schar als parameterunabhängig nachweisen", typ_neben="",
    stichwoerter="Richtungsvektor von OS: (0; 0; 1)|sin α = |n_k · (0; 0; 1)|/|n_k| = 3/√(16k² + 16 − 16k² + 9) = 3/5|unabhängig von k",
    voraussetzungen="Winkel Gerade–Ebene über den Normalenvektor|Betrag mit Parameter vereinfachen",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Gerade OS; Schar E_k wie in e",
    gesucht="Nachweis, dass der Schnittwinkel nicht von k abhängt",
    verfahren="Sinus des Winkels mit n_k, k fällt heraus",
    schritte="2", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="",
    ergebnis="((4k; 4√(1 − k²); 3) · (0; 0; 1)) / (|(4k; 4√(1 − k²); 3)| · |(0; 0; 1)|) = 3/√(16k² + 16 − 16k² + 9) = 3/5; damit ist die Größe des Winkels unabhängig von k (amtlich)",
    zwischenergebnis="α ≈ 36,9°", niveau_geschaetzt="II",
    fehlerquelle="cos statt sin (Winkel Gerade–Ebene)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAGLAA2WTR1", "g", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Lotfußpunkte vom Ursprung auf Spurgeraden von Scharebenen einzeichnen", typ_neben="",
    stichwoerter="E_{−1}: −4x + 3z = 12, Spur in der xy-Ebene x = −3 (Kante AD) ⇒ R_{−1}(−3 | 0 | 0)|E_1: 4x + 3z = 12, Spur x = 3 (Kante BC) ⇒ R_1(3 | 0 | 0)",
    voraussetzungen="Spurgerade für z = 0|Punkt kleinsten Abstands als Lotfußpunkt|Kantenmitten",
    format="Zeichnen", operator="Zeichnen Sie ein", antwort="Grafik",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="mittel",
    gegeben="g_k Schnittgerade von E_k mit der xy-Ebene, R_k Punkt auf g_k mit kleinstem Abstand zu O; Abbildung 2",
    gesucht="R_{−1} und R_1 in Abbildung 2",
    verfahren="Spuren von E_{±1} als Kanten AD und BC erkennen, Mittelpunkte markieren",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="R_1 als Mittelpunkt der Kante BC, R_{−1} als Mittelpunkt der Kante AD eingezeichnet (amtlich)",
    zwischenergebnis="R_{±1}(±3 | 0 | 0)", niveau_geschaetzt="II",
    fehlerquelle="R_k auf die Ecken B, C legen",
    bemerkung="Standardbezug: K2 I, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBAGLAA2WTR1", "h", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Rotationskörper einer Scharfläche als halben Kegel beschreiben und Volumen bestimmen", typ_neben="",
    stichwoerter="R_k durchläuft für k von −1 bis 1 den Halbkreis mit Radius 3 um O (y ≥ 0)|Dreieck OR_kS dreht sich um OS um 180°: halber Kegel mit Radius 3 und Höhe 4|V = 1/2 · 1/3 · π · 9 · 4 = 6π",
    voraussetzungen="Lage der R_k auf einem Halbkreis|Drehung um die Achse erzeugt einen Kegel|Kegelvolumen halbiert",
    format="Kurzantwort|Rechnung", operator="Beschreiben Sie|Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=PYR, kontext="ohne", textumfang="mittel",
    gegeben="Fläche OR_kS dreht sich für k von −1 bis 1 um die Strecke OS",
    gesucht="Form und Volumen des entstehenden Körpers",
    verfahren="Bahn der R_k als Halbkreis, halber Kegel",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2024MerhoehtBAGLAA2WTR1-1g",
    ergebnis="der Körper hat die Form eines senkrecht zur Grundfläche halbierten Kegels; Volumen 1/6 · π · 3² · 4 = 6π (amtlich)",
    zwischenergebnis="|OR_k| = 3 für alle k", niveau_geschaetzt="III",
    fehlerquelle="ganzen Kegel (12π) angeben",
    bemerkung="Standardbezug: K2 III, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) die Bahn der R_k als Halbkreis und den Körper als halben Kegel erkennen.")

# ---- Stochastik WTR 1: Streamingdienst
BAUMS = "Baumdiagramm: A (70 %, höchstens 40 Jahre) / nicht A (30 %), darunter B (Komplettpaket) 80 % bzw. 50 %"
row("2024MerhoehtBStochastikWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="A: höchstens 40 Jahre (70 %), B: Komplettpaket|P(B | A) = 80 %, P(B | nicht A) = 50 %",
    voraussetzungen="zweistufiges Baumdiagramm|Gegenwahrscheinlichkeiten",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Streamingdienst/Abonnenten", textumfang="mittel",
    gegeben="70 % höchstens 40 Jahre, davon 80 % Komplettpaket; von den Älteren 50 % Komplettpaket",
    gesucht="beschriftetes Baumdiagramm",
    verfahren="erste Stufe Alter, zweite Stufe Paket",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Baumdiagramm mit A (70 %), nicht A (30 %); B | A 80 %, nicht B | A 20 %; B | nicht A 50 %, nicht B | nicht A 50 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Stufen vertauschen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A).")

row("2024MerhoehtBStochastikWTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(A | B) = 0,7 · 0,8 / (0,7 · 0,8 + 0,3 · 0,5) = 0,56/0,71 ≈ 79 %",
    voraussetzungen="Bayes: Pfad durch Summe der Pfade zu B",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=BAUMS, kontext="Streamingdienst/Abonnenten", textumfang="kurz",
    gegeben="Baumdiagramm aus a; Person mit Komplettpaket",
    gesucht="P(höchstens 40 Jahre | Komplettpaket)",
    verfahren="Bayes-Quotient",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2024MerhoehtBStochastikWTR1-1a",
    ergebnis="0,7 · 0,8 / (0,7 · 0,8 + 0,3 · 0,5) ≈ 79 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P(B | A) = 80 % als Antwort",
    bemerkung="Standardbezug: K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBStochastikWTR1", "c", innen="1", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln", typ_neben="",
    stichwoerter="X ~ B(n; 0,3), P(X > 5) ≥ 0,99|n = 39: 98,91 %, n = 40: 99,14 %|mindestens 40",
    voraussetzungen="p = 0,3 (älter als 40)|P(X > 5) = 1 − P(X ≤ 5) am Rechner|n durch Probieren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Streamingdienst/Abonnenten", textumfang="mittel",
    gegeben="30 % der Abonnenten älter als 40; mit mindestens 99 % mehr als fünf Ältere unter n Ausgewählten",
    gesucht="kleinstes n",
    verfahren="P(X > 5) für n = 39 und 40 vergleichen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="X Anzahl der Abonnenten, die älter als 40 sind; wegen P(X > 5) ≈ 98,91 % für n = 39 und ≈ 99,14 % für n = 40 (p = 0,3) müssten mindestens 40 Personen zufällig ausgewählt werden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P(X ≥ 5) statt P(X > 5)",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Geschätzt II (Mindestumfang durch Probieren), amtlich III über K2.")

row("2024MerhoehtBStochastikWTR1", "a", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Wahl der Nullhypothese aus der Sicht des Entscheiders begründen", typ_neben="",
    stichwoerter="H0: p ≤ 0,6 – Ablehnung nur bei deutlichem Erfolg|vermeiden, den Algorithmus dauerhaft einzusetzen, obwohl er die Zufriedenheit nicht erhöht",
    voraussetzungen="Fehler erster Art als der zu vermeidende Fehler|Nullhypothese als Gegenteil des Erwünschten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Streamingdienst/Signifikanztest", textumfang="lang",
    gegeben="Anteil zufriedener Abonnenten derzeit 60 %; Nullhypothese „Anteil höchstens 60 %“, Stichprobe 200, Signifikanzniveau 5 %; Entscheidung über den dauerhaften Einsatz des Algorithmus",
    gesucht="mögliche Überlegung des Managements zur Wahl dieser Nullhypothese",
    verfahren="den durch das Signifikanzniveau begrenzten Fehler benennen",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="es soll möglichst vermieden werden, den Algorithmus dauerhaft einzusetzen, obwohl der Einsatz die Zufriedenheit unter den Abonnenten nicht erhöht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Fehler zweiter Art als Grund nennen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich.")

row("2024MerhoehtBStochastikWTR1", "b", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen", typ_neben="",
    stichwoerter="P(Y ≥ 132) ≈ 0,047 ≤ 0,05 zeigt nur, dass 132 zulässig ist|es könnte ein k < 132 mit P(Y ≥ k) ≤ 0,05 geben|P(Y ≥ 131) ≈ 0,064 > 0,05 ⇒ 132 ist die untere Grenze",
    voraussetzungen="Ablehnungsbereich als größtmöglicher Bereich unter α|Nachbarwert prüfen",
    format="Begründung|Rechnung", operator="Begründen Sie|Ergänzen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Streamingdienst/Signifikanztest", textumfang="mittel",
    gegeben="Ablehnungsbereich {132; …; 200}; Lösungsschritte: Y Anzahl der zufriedenen Abonnenten, P(Y ≥ 132) ≈ 0,047 (n = 200, p = 0,6)",
    gesucht="Begründung, warum die Schritte nicht ausreichen, und Ergänzung",
    verfahren="Minimalität der Grenze über P(Y ≥ 131) belegen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="es könnte eine natürliche Zahl k < 132 geben, für die P(Y ≥ k) ≤ 0,05 gilt; P(Y ≥ 131) ≈ 0,064; damit ist 132 die untere Grenze des Ablehnungsbereichs (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P(Y ≥ 133) prüfen (falsche Richtung)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBStochastikWTR1", "c", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Fehler zweiter Art für einen selbst gewählten Anteil berechnen und mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="p > 0,6 wählen, z. B. 0,61 (H0 falsch)|Fehler 2. Art: Y ≤ 131|P_{0,61}(Y ≤ 131) ≈ 91,7 % > 90 %",
    voraussetzungen="Fehler zweiter Art als Nichtablehnung bei falscher H0|Anteil knapp über 60 % wählen|kumulierte Wahrscheinlichkeit",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Streamingdienst/Signifikanztest", textumfang="kurz",
    gegeben="Ablehnungsbereich {132; …; 200}",
    gesucht="Nachweis, dass der Fehler zweiter Art mehr als 90 % betragen könnte",
    verfahren="p knapp über 0,6 wählen, P(Y ≤ 131) berechnen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2024MerhoehtBStochastikWTR1-2b",
    ergebnis="beträgt der Anteil der zufriedenen Abonnenten beispielsweise 61 %, dann trifft die Nullhypothese nicht zu und die Wahrscheinlichkeit des zugehörigen Fehlers zweiter Art beträgt P(Y ≤ 131) ≈ 91,7 % (n = 200, p = 0,61) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="p ≤ 0,6 wählen (dann kein Fehler zweiter Art)",
    bemerkung="Standardbezug: K1 III, K2 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Fehler zweiter Art als Nichtablehnung unter einer selbst zu wählenden Alternative deuten – die Wahl von p nahe 0,6 ist die zu findende Idee.")

row("2024MerhoehtBStochastikWTR1", "a", innen="3", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen", typ_neben="",
    stichwoerter="26⁸ Kennwörter nur aus Kleinbuchstaben, 80⁸ insgesamt|26⁸/80⁸ ≈ 0,00012 < 0,001",
    voraussetzungen="Anzahl mit Wiederholung als Potenz|Quotient",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Kennwörter", textumfang="mittel",
    gegeben="80 Zeichen (26 Groß-, 26 Kleinbuchstaben, 10 Ziffern, 18 Sonderzeichen); Kennwörter aus genau acht Zeichen, Wiederholung erlaubt",
    gesucht="Nachweis, dass Kennwörter nur aus Kleinbuchstaben weniger als ein Tausendstel ausmachen",
    verfahren="Potenzen bilden, Quotient",
    schritte="2", zahlenraum="Potenz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="26⁸/80⁸ ≈ 0,00012 < 0,001 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="8 · 26 statt 26⁸",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtBStochastikWTR1", "b", innen="3", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen", typ_neben="",
    stichwoerter="Niclas belegt sechs der acht Stellen in fester Reihenfolge|zwei Stellen für Zusatzzeichen: C(8; 2) Lagen|Zusatzzeichen verschieden und nicht aus Niclas: 74 · 73|C(8; 2) · 74 · 73 = 151256",
    voraussetzungen="Lagen der Zusatzstellen als Binomialkoeffizient|verbleibende Zeichen ohne Wiederholung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kennwörter", textumfang="lang",
    gegeben="acht verschiedene Zeichen; Buchstaben von Niclas in Reihenfolge und Schreibung enthalten; Beispiele Nic4+las, nNicl*as",
    gesucht="Anzahl solcher Kennwörter",
    verfahren="Lagen der zwei freien Stellen mal Zeichenwahl",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="C(8; 2) · 74 · 73 = 151256 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="74² (Wiederholung) oder 80 · 79 (Buchstaben von Niclas nicht ausschließen)",
    bemerkung="Standardbezug: K2 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik WTR 2: junge Haushalte, Reifen
VERT = "Koordinatensystem x von 0 bis 8 (Tausend km), y von 0 bis 1; S-förmiger Graph der Verteilungsfunktion von Z, nahe 0 bis x ≈ 4,5, 0,1 bei x = 5, 0,5 bei x = 5,5, nahe 1 ab x ≈ 6,5"
row("2024MerhoehtBStochastikWTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="P(A) = 0,6 Pkw, P(B) = 0,08 Lastenrad, P(B | nicht A) = 0,14|nicht A ∩ B = 0,4 · 0,14 = 0,056|A ∩ B = 0,08 − 0,056 = 0,024|Felder 0,024, 0,576, 0,056, 0,344",
    voraussetzungen="bedingten Anteil in einen Schnittanteil umrechnen|Ränder und Differenzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Haushalte/Lastenrad", textumfang="mittel",
    gegeben="60 % mit Pkw, 8 % mit Lastenrad, 14 % der Haushalte ohne Pkw mit Lastenrad",
    gesucht="vollständige Vierfeldertafel",
    verfahren="0,4 · 0,14 als Schnitt, Rest über Differenzen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="A und B 0,024, A und nicht B 0,576, nicht A und B 0,056, nicht A und nicht B 0,344; Ränder 0,6 / 0,4 und 0,08 / 0,92 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="0,14 direkt als Feld eintragen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B); hier ist ein Anteil bedingt gegeben – Vorschlag für den Abgleich: Definition darauf erweitern.")

row("2024MerhoehtBStochastikWTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Anteile aus der Vierfeldertafel vergleichen", typ_neben="",
    stichwoerter="P(B | A) = 0,024/0,6 = 0,04|3 · 0,04 = 0,12 < 0,14 = P(B | nicht A)|Aussage wahr",
    voraussetzungen="bedingter Anteil aus der Tafel|Vergleich mit dem Dreifachen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Tabelle", skizze="Vierfeldertafel aus a", kontext="Haushalte/Lastenrad", textumfang="mittel",
    gegeben="Vierfeldertafel aus a; Aussage: P(Lastenrad | ohne Pkw) ist mehr als dreimal so groß wie P(Lastenrad | mit Pkw)",
    gesucht="Beurteilung",
    verfahren="P(B | A) berechnen, verdreifachen, vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2024MerhoehtBStochastikWTR2-1a",
    ergebnis="3 · 0,024/0,6 = 0,12 < 0,14; damit ist die Aussage wahr (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Schnittanteile 0,056 und 0,024 vergleichen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")

row("2024MerhoehtBStochastikWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X ~ B(300; 0,08), P(21 ≤ X ≤ 30) ≈ 68 %",
    voraussetzungen="„mehr als 20 und höchstens 30“ als 21 ≤ X ≤ 30",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Haushalte/Lastenrad", textumfang="kurz",
    gegeben="300 zufällig ausgewählte Haushalte; Anteil Lastenrad 8 %",
    gesucht="P(mehr als 20 und höchstens 30 mit Lastenrad)",
    verfahren="Differenz kumulierter Wahrscheinlichkeiten",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="X Anzahl der Haushalte mit Lastenrad; P(21 ≤ X ≤ 30) ≈ 68 % (n = 300, p = 0,08) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="20 einschließen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2024MerhoehtBStochastikWTR2", "d", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="1 − Σ_{k=201}^{300} C(300; k) 0,6^k 0,4^{300−k} = P(X ≤ 200) mit p = 0,6 (Pkw)|höchstens 200 der 300 Haushalte mit Pkw",
    voraussetzungen="p = 0,6 als Pkw-Anteil erkennen|Gegenereignis der Summe",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Haushalte/Lastenrad", textumfang="kurz",
    gegeben="Term 1 − Σ_{k=201}^{300} C(300; k) · 0,6^k · 0,4^{300−k}",
    gesucht="Ereignis im Sachzusammenhang",
    verfahren="Summe als P(X ≥ 201), Gegenereignis",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="höchstens 200 dieser Haushalte sind mit mindestens einem Pkw ausgestattet (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="0,6 auf das Lastenrad beziehen",
    bemerkung="Standardbezug: K3 I, K4 II, K6 II. AB amtlich: II. Amtlich. Typ wiederverwendet (2026-ga-B).")

row("2024MerhoehtBStochastikWTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Hypergeometrische Verteilung",
    typ="Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen", typ_neben="",
    stichwoerter="C(12; 2) · C(68; 8) / C(80; 10) ≈ 29,6 %",
    voraussetzungen="Ziehen ohne Zurücklegen als Auswahl von Teilmengen|Binomialkoeffizienten",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kita/Lastenrad", textumfang="mittel",
    gegeben="80 Kinder, 12 davon mit Lastenrad gebracht; 10 zufällig ausgewählt",
    gesucht="Nachweis P(genau zwei mit Lastenrad) ≈ 29,6 %",
    verfahren="günstige durch mögliche Teilmengen",
    schritte="2", zahlenraum="ganz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="C(12; 2) · C(68; 8) / C(80; 10) ≈ 29,6 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="binomial mit p = 0,15 rechnen (≈ 27,6 %)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Hypergeometrische Verteilung.")

row("2024MerhoehtBStochastikWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen", typ_neben="",
    stichwoerter="V ~ N(6800; 530): P(6200 ≤ V ≤ 7400) ≈ 74 %",
    voraussetzungen="Abweichung um höchstens 600 als symmetrisches Intervall",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Reifen/Laufleistung", textumfang="mittel",
    gegeben="Laufleistung V der Vorderradreifen normalverteilt mit μ = 6800 km, σ = 530 km",
    gesucht="P(Abweichung vom Erwartungswert höchstens 600 km)",
    verfahren="Intervall 6200 bis 7400 am Rechner",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="km", abhaengig_von="",
    ergebnis="P(6200 ≤ V ≤ 7400) ≈ 74 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="einseitig P(V ≤ 7400) rechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")

row("2024MerhoehtBStochastikWTR2", "b", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Quantil einer Normalverteilung bestimmen und Wahrscheinlichkeit dafür bei einer zweiten Verteilung beurteilen", typ_neben="",
    stichwoerter="P(V > c) = 0,9 ⇒ c ≈ 6120,8 km (10 %-Quantil)|H ~ N(4600; 480): P(H ≥ 6120,8) ≈ 0,0008|Hinterradreifen unterschreitet c nahezu sicher",
    voraussetzungen="Quantil über die Umkehrung der Verteilungsfunktion|Wahrscheinlichkeit bei der zweiten Verteilung|„nahezu mit Sicherheit“ als sehr kleine Gegenwahrscheinlichkeit",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Reifen/Laufleistung", textumfang="lang",
    gegeben="V ~ N(6800; 530), H ~ N(4600; 480); Aussage: die Laufleistung, die ein Vorderradreifen mit 90 % übertrifft, unterschreitet ein Hinterradreifen nahezu sicher",
    gesucht="Begründung, dass die Aussage wahr ist",
    verfahren="c aus P(V > c) = 0,9, dann P(H ≥ c)",
    schritte="3", zahlenraum="dezimal", einheiten="km", abhaengig_von="",
    ergebnis="P(V > c) = 0,9 liefert c ≈ 6120,8; ein zufällig ausgewählter Hinterradreifen hat wegen P(H ≥ 6120,8) ≈ 0,0008 mit nur sehr geringer Wahrscheinlichkeit eine Laufleistung von mindestens 6120,8 km (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="c als 90 %-Quantil (7479 km) bestimmen",
    bemerkung="Standardbezug: K1 III, K3 III, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Sachaussage in ein Quantil der einen und eine Überschreitungswahrscheinlichkeit der anderen Verteilung übersetzen.")

row("2024MerhoehtBStochastikWTR2", "c", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Parameter einer Normalverteilung aus dem Graphen der Verteilungsfunktion ermitteln", typ_neben="",
    stichwoerter="f(x) = P(Z ≤ 1000x); f = 0,5 bei x = 5,5 ⇒ μ = 5500|f(5) ≈ 0,1: P(Z ≤ 5000) = 0,1 ⇒ (5000 − 5500)/σ ≈ −1,28 ⇒ σ ≈ 390 (systematisches Probieren)",
    voraussetzungen="Median als Erwartungswert|zweiten Punkt ablesen|σ aus einer Quantilbedingung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=VERT, kontext="Reifen/Laufleistung", textumfang="mittel",
    gegeben="Z ~ N(μ; σ); Abbildung des Graphen von f(x) = P(Z ≤ 1000 · x)",
    gesucht="μ und σ in km",
    verfahren="μ am Wert 0,5, σ aus einem weiteren abgelesenen Punkt",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="km", abhaengig_von="",
    ergebnis="wegen P(Z ≤ 5500) ≈ 0,5 ist μ ≈ 5500; der Abbildung ist P(Z ≤ 5000) ≈ 0,1 zu entnehmen; damit erhält man durch systematisches Probieren σ ≈ 390 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Skalierung 1000x übersehen (μ = 5,5)",
    bemerkung="Standardbezug: K1 III, K2 III, K4 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Graph als Verteilungsfunktion lesen und zwei Ablesungen in Bedingungen an μ und σ übersetzen.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Nullstellenfreiheit und Grenzwerte eines Bruchs mit e-Funktion am Term begründen", "Analysis", "Grenzwerte und Verhalten im Unendlichen",
     "Am Term eines Bruchs mit e-Funktion im Nenner begründen, dass es keine Nullstelle gibt, und die Grenzwerte für x → ±∞ angeben.",
     "2024MerhoehtBAnalysisWTR1-1a"),
    ("Mittlere Steigung berechnen und Tangentensteigung im Wendepunkt grafisch bestimmen", "Analysis", "Ableitung und Änderungsrate",
     "Die mittlere Steigung über ein Intervall als Differenzenquotient berechnen und die Steigung im Wendepunkt durch Anlegen einer Tangente grafisch bestimmen.",
     "2024MerhoehtBAnalysisWTR1-1b"),
    ("Achsensymmetrie des Ableitungsgraphen aus f'(−x) = f'(x) deuten und Graphen skizzieren", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Die Beziehung f'(−x) = f'(x) als Achsensymmetrie des Graphen von f' deuten und den Ableitungsgraphen in die Abbildung skizzieren.",
     "2024MerhoehtBAnalysisWTR1-1c"),
    ("Nullstellen und Werte: Lage eines Graphen unterhalb der x-Achse über eine Logarithmus-Abschätzung beurteilen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Eine Aussage über die Lage eines Graphen gegenüber der x-Achse über eine Abschätzung mit ln(e^x + 1) > x beurteilen.",
     "2024MerhoehtBAnalysisWTR1-1e"),
    ("Anfangswert angeben und Zeitpunkt für einen Bestand bei logistischem Wachstum berechnen", "Analysis", "Gleichungen lösen",
     "Den Anfangswert einer logistischen Funktion angeben und den Zeitpunkt für einen vorgegebenen Bestand über eine Exponentialgleichung berechnen.",
     "2024MerhoehtBAnalysisWTR1-2b"),
    ("Näherung durch die Tangente mit dem Funktionswert im Sachzusammenhang vergleichen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Wert einer Tangente (lineare Näherung) an einer Stelle mit dem Funktionswert vergleichen und das Ergebnis im Sachzusammenhang einordnen.",
     "2024MerhoehtBAnalysisWTR1-2c"),
    ("Gleichungen eines Bestimmungssystems für Scharparameter im Sachzusammenhang deuten", "Analysis", "Funktionsscharen und Ortskurven",
     "Gleichungen wie Anfangswert, Grenzwert und Wert an einer Stelle, die die Parameter einer Schar festlegen, im Sachzusammenhang deuten.",
     "2024MerhoehtBAnalysisWTR1-2d"),
    ("Scharparameter aus Anfangswert und Grenzwert über das Vorzeichen des Exponenten bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Parameter einer Schar mit e^{cx} aus Anfangswert und Grenzwert bestimmen, wobei das Vorzeichen von c erst aus dem Vergleich beider Werte folgt.",
     "2024MerhoehtBAnalysisWTR1-2e"),
    ("Tiefpunkt einer Schar mit zwei Parametern nachweisen und Hochpunkt über die Punktsymmetrie begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Einen Tiefpunkt an einer parameterabhängigen Stelle über f' und f'' nachweisen und den Hochpunkt über die Punktsymmetrie des Graphen begründen.",
     "2024MerhoehtBAnalysisWTR2-1b"),
    ("Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Zwei Parameter einer Schar aus einer vorgegebenen Nullstelle und dem Inhalt eines Flächenstücks zwischen Graph und x-Achse bestimmen.",
     "2024MerhoehtBAnalysisWTR2-1c"),
    ("Flächeninhalt des Dreiecks aus Tangente, Gerade und x-Achse berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Tangente in einem Punkt aufstellen, ihren Schnittpunkt mit einer gegebenen Geraden berechnen und den Flächeninhalt des mit der x-Achse gebildeten Dreiecks bestimmen.",
     "2024MerhoehtBAnalysisWTR2-1d"),
    ("Mittelpunkte der Strecken zum Ursprung auf einem gegebenen Graphen allgemein nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Allgemein nachweisen, dass die Mittelpunkte der Strecken von Graphenpunkten zum Ursprung auf dem Graphen einer angegebenen Funktion liegen (Ortskurve).",
     "2024MerhoehtBAnalysisWTR2-1e"),
    ("Eignung eines Modells über das Vorzeichen der Änderungsrate nach einer Nullstelle beurteilen", "Analysis", "Ableitung und Änderungsrate",
     "Begründen, dass eine Ratenfunktion jenseits einer Nullstelle mit Vorzeichenwechsel im Sachzusammenhang ungeeignet ist.",
     "2024MerhoehtBAnalysisWTR2-2c"),
    ("Sekantenwinkel gegen eine Schranke am Graphen beurteilen", "Analysis", "Ableitung und Änderungsrate",
     "Ohne Rechnung beurteilen, ob die Sekante zwischen zwei Graphenpunkten einen Winkel unter einer Schranke hat, durch Vergleich mit einer eingezeichneten Hilfsgeraden.",
     "2024MerhoehtBAnalysisWTR3-1b"),
    ("Maximalen Neigungswinkel über die Wendestelle berechnen und mit einer Schranke vergleichen", "Analysis", "Kurvenuntersuchung",
     "Die Stelle größter Steigung als Wendestelle bestimmen, den Steigungswinkel dort berechnen und mit einer Schranke vergleichen.",
     "2024MerhoehtBAnalysisWTR3-1c"),
    ("Länge der Normalen vom Graphenpunkt bis zur x-Achse berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Normale in einem Graphenpunkt aufstellen, ihre Nullstelle bestimmen und die Länge der Strecke vom Punkt bis zur x-Achse berechnen.",
     "2024MerhoehtBAnalysisWTR3-1d"),
    ("Extrempunkt einer Schar mit Art nach dem Parametervorzeichen bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Extrempunkt einer Schar berechnen und seine Art in Abhängigkeit vom Vorzeichen des Parameters angeben.",
     "2024MerhoehtBAnalysisWTR3-2b"),
    ("Abstand der y-Achsenabschnitte zweier benachbarter Scharkurven berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Differenz der y-Achsenabschnitte von G_k und G_{k+1} berechnen.",
     "2024MerhoehtBAnalysisWTR3-2c"),
    ("Spiegelung an der x-Achse als Scharmitglied nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Nachweisen, dass das Spiegelbild eines Schargraphen an der x-Achse wieder zur Schar gehört (−f_k = f_{−k}).",
     "2024MerhoehtBAnalysisWTR3-2d"),
    ("Fläche: Gerade zur Halbierung der Fläche zwischen Scharkurve und Koordinatenachsen ermitteln", "Analysis", "Flächeninhalt durch Integration",
     "Die Gleichung einer Geraden durch die Nullstelle ermitteln, die die Fläche zwischen Graph und Koordinatenachsen halbiert (Dreiecksfläche gleich halbes Integral).",
     "2024MerhoehtBAnalysisWTR3-2e"),
    ("Aufgabenstellung zu einer Extremwertaufgabe mit Dreiecksfläche aus dem Lösungsweg formulieren und Schritte erläutern", "Analysis", "Extremalprobleme",
     "Zu Lösungsschritten (Zielfunktion, notwendige und hinreichende Bedingung, Maximalwert) die passende Extremwertaufgabe formulieren und die Schritte erläutern.",
     "2024MerhoehtBAnalysisWTR3-2f"),
    ("Übergangsprozess: Matrixparameter aus einer Komponente nach zwei Schritten bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen unbekannten Eintrag der Übergangsmatrix aus einer vorgegebenen Komponente des Vektors nach zwei Übergangsschritten bestimmen.",
     "2024MerhoehtBAGLAA1WTR-1b"),
    ("Matrizenalgebra: Konstanten Faktor der Komponentensumme von Q · u über die Spaltensummen nachweisen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Für einen allgemeinen Vektor u nachweisen, dass die Komponentensumme von Q · u ein festes Vielfaches der Komponentensumme von u ist (gleiche Spaltensummen).",
     "2024MerhoehtBAGLAA1WTR-1c"),
    ("Übergangsprozess: Zeitpunkt für das Unterschreiten eines Anteils der Populationsgröße über einen konstanten Faktor bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus einem konstanten Faktor je Schritt die Anzahl der Schritte bestimmen, nach der die Gesamtgröße erstmals unter einen Anteil des Anfangswerts fällt (Exponentialungleichung).",
     "2024MerhoehtBAGLAA1WTR-1d"),
    ("Dreieck: Rechten Winkel aus der Lage zu den Koordinatenachsen begründen", "Analytische Geometrie", "Orthogonalität",
     "Einen rechten Winkel eines Dreiecks ohne Rechnung aus der Lage der Schenkel in einer Koordinatenebene und auf der dazu senkrechten Achse begründen.",
     "2024MerhoehtBAGLAA1WTR-2a"),
    ("Ebene Figur: Eckpunkt auf einer Achse aus dem Umfang eines Dreiecks bestimmen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Die unbekannte Koordinate eines Eckpunkts auf einer Koordinatenachse aus einem vorgegebenen Umfang über eine Wurzelgleichung bestimmen.",
     "2024MerhoehtBAGLAA1WTR-2b"),
    ("Punkt: Bildpunkte einer Drehung um eine Koordinatenachse mit vorgegebener Koordinate angeben", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Punkte auf der Kreisbahn angeben, die ein Punkt bei Drehung um eine Koordinatenachse beschreibt, wenn eine Koordinate vorgegeben ist.",
     "2024MerhoehtBAGLAA1WTR-2c"),
    ("Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Oberflächeninhalt einer quadratischen Pyramide aus Grundfläche und vier Seitendreiecken (Seitenhöhe über Pythagoras) berechnen.",
     "2024MerhoehtBAGLAA2WTR1-1a"),
    ("Symmetrieebene einer Pyramide unter vorgegebenen Gleichungen auswählen und eine ausschließen", "Analytische Geometrie", "Spiegelung",
     "Unter mehreren Ebenengleichungen die Symmetrieebene eines Körpers auswählen und für eine andere über eine Punktprobe begründen, dass sie keine ist.",
     "2024MerhoehtBAGLAA2WTR1-1b"),
    ("Lösungsweg für den Punkt gleichen Abstands zu allen Seitenflächen einer Pyramide erläutern", "Analytische Geometrie", "Abstände",
     "Einen vorgelegten Lösungsweg mit Lotgerade, Lotfußpunkt und Abstandsgleichheit zur Grundfläche für den Mittelpunkt der Inkugel einer Pyramide erläutern.",
     "2024MerhoehtBAGLAA2WTR1-1d"),
    ("Gemeinsamen Punkt aller Ebenen einer Schar nachweisen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Durch Einsetzen nachweisen, dass ein Punkt in allen Ebenen einer Schar liegt.",
     "2024MerhoehtBAGLAA2WTR1-1e"),
    ("Schnittwinkel einer Geraden mit allen Ebenen einer Schar als parameterunabhängig nachweisen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Den Sinus des Schnittwinkels zwischen einer Geraden und den Scharebenen mit Parameter berechnen und zeigen, dass der Parameter herausfällt.",
     "2024MerhoehtBAGLAA2WTR1-1f"),
    ("Lotfußpunkte vom Ursprung auf Spurgeraden von Scharebenen einzeichnen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Für ausgewählte Parameterwerte die Spurgeraden der Scharebenen in einer Koordinatenebene und die Lotfußpunkte vom Ursprung in das Schrägbild einzeichnen.",
     "2024MerhoehtBAGLAA2WTR1-1g"),
    ("Körper: Rotationskörper einer Scharfläche als halben Kegel beschreiben und Volumen bestimmen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Körper beschreiben, der beim Durchlaufen eines Parameters durch Drehung eines Dreiecks um eine Achse entsteht (halber Kegel), und sein Volumen berechnen.",
     "2024MerhoehtBAGLAA2WTR1-1h"),
    ("Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", "Stochastik", "Bedingte Wahrscheinlichkeit und Bayes",
     "Eine bedingte Wahrscheinlichkeit gegen die Richtung des Baumdiagramms als Quotient aus einem Pfad und der Summe der Pfade zum Ereignis berechnen.",
     "2024MerhoehtBStochastikWTR1-1b"),
    ("Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln", "Stochastik", "Binomialverteilung",
     "Den kleinsten Stichprobenumfang n ermitteln, für den P(X > k) eine vorgegebene Schranke erreicht, durch Probieren am Rechner.",
     "2024MerhoehtBStochastikWTR1-1c"),
    ("Wahl der Nullhypothese aus der Sicht des Entscheiders begründen", "Stochastik", "Hypothesentests",
     "Angeben, welche Überlegung (welcher zu vermeidende Fehler) zur Wahl einer bestimmten Nullhypothese führt.",
     "2024MerhoehtBStochastikWTR1-2a"),
    ("Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen", "Stochastik", "Hypothesentests",
     "Begründen, dass der Nachweis P(Y ≥ k) ≤ α allein die Ablehnungsgrenze nicht festlegt, und den fehlenden Nachbarwert ergänzen.",
     "2024MerhoehtBStochastikWTR1-2b"),
    ("Fehler zweiter Art für einen selbst gewählten Anteil berechnen und mit einer Schranke vergleichen", "Stochastik", "Hypothesentests",
     "Für einen selbst gewählten Anteil, bei dem die Nullhypothese falsch ist, die Wahrscheinlichkeit des Fehlers zweiter Art berechnen und nachweisen, dass sie eine Schranke überschreitet.",
     "2024MerhoehtBStochastikWTR1-2c"),
    ("Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen", "Stochastik", "Kombinatorik",
     "Die Anzahl der Zeichenfolgen fester Länge mit Wiederholung als Potenz bilden und den Anteil einer Teilmenge der Zeichen berechnen.",
     "2024MerhoehtBStochastikWTR1-3a"),
    ("Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen", "Stochastik", "Kombinatorik",
     "Die Anzahl der Zeichenfolgen bestimmen, die eine feste Teilfolge in Reihenfolge enthalten und mit verschiedenen weiteren Zeichen aufgefüllt sind (Lagen mal Zeichenwahl).",
     "2024MerhoehtBStochastikWTR1-3b"),
    ("Hypergeometrische Wahrscheinlichkeit für genau k Treffer über Binomialkoeffizienten nachweisen", "Stochastik", "Hypergeometrische Verteilung",
     "Die Wahrscheinlichkeit für genau k Treffer beim Ziehen ohne Zurücklegen als Quotient von Binomialkoeffizienten berechnen.",
     "2024MerhoehtBStochastikWTR2-1e"),
    ("Quantil einer Normalverteilung bestimmen und Wahrscheinlichkeit dafür bei einer zweiten Verteilung beurteilen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Aus P(V > c) = q den Wert c bestimmen und für eine zweite Normalverteilung die Wahrscheinlichkeit beurteilen, c zu erreichen.",
     "2024MerhoehtBStochastikWTR2-2b"),
    ("Parameter einer Normalverteilung aus dem Graphen der Verteilungsfunktion ermitteln", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "μ als Stelle des Werts 0,5 und σ aus einem weiteren abgelesenen Punkt des Graphen der Verteilungsfunktion ermitteln.",
     "2024MerhoehtBStochastikWTR2-2c"),
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
