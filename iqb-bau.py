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
    "stapel": "2022-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2022MerhoehtAAnalysis11": 5,
        "2022MerhoehtAAnalysis12": 5,
        "2022MerhoehtAAnalysis13": 5,
        "2022MerhoehtAAnalysis2": 5,
        "2022MerhoehtAAGLAA111": 5,
        "2022MerhoehtAAGLAA112": 5,
        "2022MerhoehtAAGLAA12": 5,
        "2022MerhoehtAAGLAA211": 5,
        "2022MerhoehtAAGLAA212": 5,
        "2022MerhoehtAAGLAA213": 5,
        "2022MerhoehtAAGLAA221": 5,
        "2022MerhoehtAAGLAA222": 5,
        "2022MerhoehtAStochastik11": 5,
        "2022MerhoehtAStochastik12": 5,
        "2022MerhoehtAStochastik13": 5,
        "2022MerhoehtAStochastik21": 5,
        "2022MerhoehtAStochastik22": 5,
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
# niveau_geschaetzt nach der Deutungsliste v0.6; bei III nennt bemerkung den Eintrag.

# ---- Analysis 1.1: Graph der Stammfunktion, Integral und Ableitungswert
GF_SKIZZE = ("Koordinatensystem mit Gitter (Schrittweite 1), x-Achse von 0 bis 7,5, y-Achse von −1 bis 5,5; "
             "Graph G_F: von links unten steigend durch (1; 1), Hochpunkt (2; 2,5), fallend durch (3; 1,5), "
             "Tiefpunkt (4; −0,2), steigend durch (5; 1), (6; 3) und (7; 5)")
row("2022MerhoehtAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Integral über f aus dem Graphen der Stammfunktion bestimmen", typ_neben="",
    stichwoerter="Integral von 1 bis 7 über f = F(7) − F(1)|F(7) = 5, F(1) = 1 am Graphen|Wert 4",
    voraussetzungen="Hauptsatz|Werte am Gitter ablesen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GF_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f und F in IR, F Stammfunktion von f; Graph G_F in der Abbildung mit F(1) = 1 und F(7) = 5",
    gesucht="Wert des Integrals von 1 bis 7 über f(x) dx",
    verfahren="Hauptsatz mit den abgelesenen Werten F(7) und F(1)",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Integral von 1 bis 7 über f(x) dx = F(7) − F(1) = 5 − 1 = 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Fläche unter G_F bestimmen wollen",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I. Amtlich, Werte aus der Abbildung.")

row("2022MerhoehtAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Funktionswert von f als Tangentensteigung am Graphen der Stammfunktion bestimmen", typ_neben="",
    stichwoerter="f = F'|f(1) = F'(1)|Tangente an G_F in (1; 1) einzeichnen, Steigung 4",
    voraussetzungen="f als Ableitung von F|Tangentensteigung am Graphen ablesen und einzeichnen",
    format="Rechnung|Zeichnen", operator="Bestimmen Sie|Veranschaulichen Sie", antwort="Zahl|Grafik",
    material="Koordinatensystem", skizze=GF_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph G_F; F Stammfunktion von f",
    gesucht="f(1) mit Veranschaulichung des Vorgehens in der Abbildung",
    verfahren="Tangente in (1; 1) an G_F zeichnen und ihre Steigung als Steigungsdreieck ablesen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f(1) = F'(1) = 4; Tangente an G_F im Punkt (1; 1) mit Steigungsdreieck (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="f(1) als F(1) = 1 ablesen",
    bemerkung="Standardbezug: K2 II, K4 II. Amtlich, Wert aus der Abbildung. Eine Deutung (f = F') ohne Verkettung, nach dem Prinzip II.")

# ---- Analysis 1.2: Schar x⁴ + (2 − k)x³ − kx²
row("2022MerhoehtAAnalysis12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Achsensymmetrie am Term über gerade Exponenten begründen", typ_neben="",
    stichwoerter="f_2(x) = x⁴ − 2x²|nur gerade Exponenten|achsensymmetrisch zur y-Achse",
    voraussetzungen="k = 2 einsetzen|Exponentenregel für Achsensymmetrie",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_k(x) = x⁴ + (2 − k) · x³ − k · x² in IR, k reell",
    gesucht="Begründung, dass der Graph von f_2 symmetrisch zur y-Achse ist",
    verfahren="f_2 aufstellen, Exponenten prüfen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Funktionsterm von f_2 enthält nur Potenzen von x mit geraden Exponenten (amtlich)",
    zwischenergebnis="f_2(x) = x⁴ − 2x²",
    niveau_geschaetzt="I",
    fehlerquelle="den x³-Term übersehen und für allgemeines k argumentieren",
    bemerkung="Standardbezug: K1 I, K4 I. Amtlich, eigene Rechnung bestätigt. Gegenstück zu „Symmetrie: Punktsymmetrie am Term über ungerade Exponenten begründen“ (2026-ga-A).")

row("2022MerhoehtAAnalysis12", "b", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für eine vorgegebene Wendestelle berechnen", typ_neben="",
    stichwoerter="f_k'(x) = 4x³ + 3(2 − k)x² − 2kx|f_k''(x) = 12x² + 6(2 − k)x − 2k|f_k''(1) = 24 − 8k = 0|k = 3",
    voraussetzungen="zweimal ableiten mit Parameter|notwendige Bedingung für Wendestellen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_k(x) = x⁴ + (2 − k) · x³ − k · x²; es gibt genau einen Wert von k, für den 1 Wendestelle ist",
    gesucht="dieser Wert von k",
    verfahren="f_k''(1) = 0 nach k auflösen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_k'(x) = 4x³ + 3 · (2 − k) · x² − 2kx; f_k''(x) = 12x² + 6 · (2 − k) · x − 2k; f_k''(1) = 0 ⇔ 24 − 8k = 0 ⇔ k = 3 (amtlich)",
    zwischenergebnis="f_3'''(1) = 30 ≠ 0",
    niveau_geschaetzt="II",
    fehlerquelle="Fehler beim Ableiten des Parameterterms (2 − k) · x³",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 1.3: cos x und k · x²
COSK_SKIZZE = ("Koordinatensystem mit Gitter (Schrittweite 1), x-Achse von −9 bis 9 mit den Markierungen −8, −6, −4, "
               "−2, 0, 2, 4, 6, 8, y-Achse von −5 bis 5 mit den Markierungen −4, −2, 2, 4; Graph von cos x über "
               "den ganzen Bereich; flache Parabel 1/50 · x² durch den Ursprung, bei x = ±8 etwa 1,3 hoch")
row("2022MerhoehtAAnalysis13", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Graph der Schar zu einem Parameterwert in die Abbildung skizzieren", typ_neben="",
    stichwoerter="g_(1/4)(x) = 1/4 · x²|Parabel durch (0; 0), (2; 1), (4; 4)|steiler als g_(1/50)",
    voraussetzungen="Parabel mit Streckfaktor skizzieren|Stützpunkte berechnen",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=COSK_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = cos x, g_k(x) = k · x² mit k > 0; Abbildung mit den Graphen von f und g_(1/50)",
    gesucht="Skizze des Graphen von g_(1/4) in der Abbildung",
    verfahren="Stützpunkte (±2; 1), (±4; 4) einzeichnen und verbinden",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Parabel durch den Ursprung und die Punkte (±2; 1), (±4; 4); der Erwartungshorizont zeigt die Skizze (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Parabel zu flach (mit g_(1/50) verwechselt)",
    bemerkung="Standardbezug: K4 I. Amtlich.")

row("2022MerhoehtAAnalysis13", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Existenz von Scharparametern mit beliebig vielen Schnittstellen begründen", typ_neben="",
    stichwoerter="kleines k: Parabel bleibt lange unter 1|cos x schneidet sie in jeder Periode zweimal, solange k · x² < 1|Anzahl der Lösungen wächst unbeschränkt|ja, es gibt solche k",
    voraussetzungen="Wirkung von k als Stauchung|Periodizität des Kosinus|Argument mit beliebig kleinem k",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=COSK_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = cos x, g_k(x) = k · x² mit k > 0",
    gesucht="Entscheidung mit Begründung, ob es k gibt, für die f(x) = g_k(x) mehr als 2022 Lösungen hat",
    verfahren="für beliebig kleine k ist die Parabel beliebig stark gestaucht und schneidet den Kosinusgraphen beliebig oft",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="für beliebig kleine Werte von k sind die Graphen von g_k gegenüber dem Graphen von g_1 beliebig stark gestaucht und schneiden damit den Graphen von x ↦ cos x beliebig oft; damit gibt es Werte von k, für die die Gleichung mehr als 2022 Lösungen hat (amtlich)",
    zwischenergebnis="k = 10⁻⁸ liefert mehrere tausend Lösungen",
    niveau_geschaetzt="II",
    fehlerquelle="mit der Abbildung (k = 1/50, wenige Schnittpunkte) auf „nein“ schließen",
    bemerkung="Standardbezug: K1 II, K6 II. Amtlich, eigene Rechnung bestätigt (Vorzeichenwechsel für k = 10⁻⁸ gezählt). Eine Deutung (Stauchung) ohne Verkettung, nach dem Prinzip II.")

# ---- Analysis 2: quadratische Funktion aus zwei Eigenschaften (ungegliedert)
row("2022MerhoehtAAnalysis2", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Quadratische Funktion aus senkrechtem Schnitt mit einer Geraden und einer Extrempunktbedingung ermitteln", typ_neben="",
    stichwoerter="g(x) = ax² + bx + c|g(0) = 1 gibt c = 1|senkrecht zu y = 1/4 x + 1: g'(0) = −4, b = −4|Extremstelle x = 2/a|g(2/a) = 2/a gibt a = 6|g(x) = 6x² − 4x + 1",
    voraussetzungen="rechter Winkel als Produkt der Steigungen −1|Ableitung im Schnittpunkt|Extremstelle mit Parameter|Bedingung x = y am Extrempunkt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="quadratische Funktion g; der Graph schneidet y = 1/4 x + 1 im Punkt (0; 1) unter einem rechten Winkel; x- und y-Koordinate des Extrempunkts stimmen überein",
    gesucht="Gleichung von g",
    verfahren="c aus dem Punkt, b aus der Orthogonalität der Steigungen, a aus der Extrempunktbedingung",
    schritte="4", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="g(x) = ax² + bx + c, g(0) = 1 ⇔ c = 1; g'(x) = 2ax + b, g'(0) = b = −1/(1/4) = −4; g'(x) = 0 ⇔ x = 2/a; g(2/a) = 4/a − 8/a + 1 = −4/a + 1, d. h. g(2/a) = 2/a ⇔ a = 6 (amtlich)",
    zwischenergebnis="g(x) = 6x² − 4x + 1, Extrempunkt (1/3; 1/3)",
    niveau_geschaetzt="III",
    fehlerquelle="rechten Winkel als g'(0) = 1/4 oder −1/4 ansetzen",
    bemerkung="Standardbezug: K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2, einzige Datei der Gruppe). Eichregel: (a) beide Eigenschaften in Gleichungen übersetzen (Orthogonalität der Steigungen, Extrempunkt mit x = y) und verketten.")

# ---- AG/LA (A1) 1.1: Insekten (Datei mit drei Seiten, c auf Seite 2)
row("2022MerhoehtAAGLAA111", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="M = ((0,5; 0; 0,3), (30; 0; 0), (0; 0,2; 0)) auf (A; E; L)|Eintrag 0,2 in Zeile L, Spalte E|20 % der Eier werden Larven",
    voraussetzungen="Zeile als Ziel, Spalte als Quelle lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Population/Insekten", textumfang="lang",
    gegeben="Vektoren (A; E; L) für ausgewachsene Insekten, Eier, Larven; v_(n+1) = M · v_n mit M = ((0,5; 0; 0,3), (30; 0; 0), (0; 0,2; 0)) je Woche",
    gesucht="Bedeutung des Eintrags 0,2 im Sachzusammenhang",
    verfahren="Position des Eintrags (Zeile L, Spalte E) deuten",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="20 % der Eier entwickeln sich innerhalb einer Woche zu Larven (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Zeile und Spalte vertauschen (20 % der Larven werden Eier)",
    bemerkung="Standardbezug: K3 I, K6 I. Amtlich. Datei mit drei Seiten. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2022MerhoehtAAGLAA111", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unbekannte Anzahl aus einer Bedingung an den Folgezustand berechnen", typ_neben="",
    stichwoerter="A_(n+1) = 0,5 · A_n + 0,3 · L_n|0,5 · 30 + 0,3 · L = 30|L = 50",
    voraussetzungen="eine Zeile des Matrix-Vektor-Produkts ansetzen|lineare Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Population/Insekten", textumfang="mittel",
    gegeben="zu Beginn 30 ausgewachsene Insekten, 10 Eier, L Larven; eine Woche später unverändert 30 ausgewachsene Insekten",
    gesucht="Anzahl der Larven zu Beginn",
    verfahren="erste Zeile von M · v = 30 nach L auflösen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,5 · 30 + 0,3 · L = 30 ⇔ L = 50 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Eier (Spalte E, Eintrag 0 in der A-Zeile) mit einrechnen",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtAAGLAA111", "c", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrix bei geänderter Reihenfolge der Zustände angeben", typ_neben="",
    stichwoerter="Vektoren nun (E; L; A)|Zeilen und Spalten von M umsortieren|N = ((0; 0; 30), (0,2; 0; 0), (0; 0,3; 0,5))",
    voraussetzungen="Einträge als Übergänge zwischen Zuständen lesen|Reihenfolge der Zustände in Zeilen und Spalten gleich ändern",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Population/Insekten", textumfang="mittel",
    gegeben="M für die Reihenfolge (A; E; L); neue Reihenfolge (E; L; A) mit w_(n+1) = N · w_n",
    gesucht="Matrix N",
    verfahren="jeden Übergang (Quelle → Ziel) an die neue Position schreiben",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="N = ((0; 0; 30), (0,2; 0; 0), (0; 0,3; 0,5)) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Zeilen, nicht die Spalten umsortieren",
    bemerkung="Standardbezug: K3 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt (N · w und M · v liefern dieselben Anzahlen). Teilaufgabe steht auf Seite 2.")

# ---- AG/LA (A1) 1.2: M = ((1; 3), (1; −1))
row("2022MerhoehtAAGLAA112", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Faktor aus M² als Vielfachem der Einheitsmatrix ermitteln", typ_neben="",
    stichwoerter="M = ((1; 3), (1; −1))|M² = ((4; 0), (0; 4)) = 4 · E|M² · u = 4 · u, a = 4",
    voraussetzungen="Matrizenprodukt|Vielfaches der Einheitsmatrix als Streckung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="M = ((1; 3), (1; −1)); für jeden Vektor u gilt M² · u = a · u",
    gesucht="Wert von a",
    verfahren="M² berechnen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="M² = ((1; 3), (1; −1)) · ((1; 3), (1; −1)) = ((4; 0), (0; 4)) = 4 · ((1; 0), (0; 1)), d. h. a = 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="M² elementweise quadrieren",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2022MerhoehtAAGLAA112", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen", typ_neben="",
    stichwoerter="M · v = (v1 + 3v2; v1 − v2) = (2v1; 2v2)|beide Gleichungen liefern v1 = 3v2|v = (3b; b), b reell",
    voraussetzungen="Matrix-Vektor-Gleichung als Gleichungssystem|Lösungsmenge mit freiem Parameter angeben",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="M = ((1; 3), (1; −1))",
    gesucht="alle Vektoren v mit M · v = 2 · v",
    verfahren="Gleichungssystem aufstellen, beide Gleichungen auf v1 = 3v2 bringen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="M · (v1; v2) = (v1 + 3v2; v1 − v2) = 2 · (v1; v2) liefert v1 = 3v2; damit ist v = (3b; b) mit b reell (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur die eine Lösung (3; 1) angeben",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Vorschlag für den Abgleich: mit „Matrizenalgebra: Alle Fixvektoren einer Matrix ermitteln“ (t = 1) zusammenziehen.")

# ---- AG/LA (A1) 2: stochastische Matrizen
row("2022MerhoehtAAGLAA12", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Alle Fixvektoren einer Matrix ermitteln", typ_neben="",
    stichwoerter="M = ((0,4; 0,3), (0,6; 0,7))|M · v = v ⇔ 0,4 v_x + 0,3 v_y = v_x ⇔ v_y = 2 v_x|v = (1; 2)",
    voraussetzungen="Fixvektorgleichung als Gleichungssystem|eine Lösung ungleich dem Nullvektor wählen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="stochastische Matrix M = ((0,4; 0,3), (0,6; 0,7)) (Spaltensummen 1, Einträge nicht negativ)",
    gesucht="ein Vektor v ≠ 0 mit M · v = v",
    verfahren="Gleichungssystem lösen, Vielfaches wählen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="((0,4; 0,3), (0,6; 0,7)) · (v_x; v_y) = (v_x; v_y) ⇔ v_y = 2v_x; damit (1; 2) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="v_y = 2 v_x und v = (2; 1) vertauschen",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2025-ea-A wiederverwendet; hier ist nur ein Fixvektor verlangt, die Fertigkeit ist dieselbe.")

row("2022MerhoehtAAGLAA12", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Erhalt der Spaltensumme unter einer stochastischen Matrix allgemein nachweisen", typ_neben="",
    stichwoerter="N = ((a; b), (c; d)) mit a + c = 1, b + d = 1|N · u = (a u_x + b u_y; c u_x + d u_y)|Summe (a + c) u_x + (b + d) u_y = u_x + u_y = 5",
    voraussetzungen="stochastisch als a + c = 1 und b + d = 1 übersetzen|allgemeines Produkt aufschreiben|Summanden umordnen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="N stochastische 2×2-Matrix; u Vektor mit Komponentensumme 5",
    gesucht="Nachweis, dass N · u ebenfalls die Komponentensumme 5 hat",
    verfahren="N und u allgemein ansetzen, Summe der Komponenten von N · u nach u_x und u_y sortieren, Spaltensummen 1 einsetzen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="mit N = ((a; b), (c; d)) und u = (u_x; u_y) ergibt sich N · u = (a · u_x + b · u_y; c · u_x + d · u_y); a · u_x + b · u_y + c · u_x + d · u_y = (a + c) · u_x + (b + d) · u_y = 1 · u_x + 1 · u_y = u_x + u_y = 5 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="mit einer Zahlenmatrix statt allgemein rechnen",
    bemerkung="Standardbezug: K2 III, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Definition „stochastisch“ in a + c = 1, b + d = 1 übersetzen und (c) allgemeiner Nachweis mit Parametern.")

# ---- AG/LA (A2) 1.1: Gerade senkrecht zu E, parallele Gerade mit kleinstem Abstand
row("2022MerhoehtAAGLAA211", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen", typ_neben="",
    stichwoerter="g: (7; 3; 3) + r · (3; 0; −1)|E: 3x1 − x3 = −2, Normalenvektor (3; 0; −1)|Richtungsvektor gleich Normalenvektor",
    voraussetzungen="Normalenvektor aus der Koordinatengleichung ablesen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (7; 3; 3) + r · (3; 0; −1); E: 3x1 − x3 = −2",
    gesucht="Begründung, dass g senkrecht zu E steht",
    verfahren="Richtungsvektor mit dem Normalenvektor vergleichen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="der Richtungsvektor von g stimmt mit dem Normalenvektor von E überein (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Skalarprodukt null erwarten statt Kollinearität",
    bemerkung="Standardbezug: K1 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2025-ea-A wiederverwendet (zusammengezogener Typ).")

row("2022MerhoehtAAGLAA211", "b", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Gerade in einer Ebene parallel zu einer Geraden mit kleinstem Abstand bestimmen", typ_neben="",
    stichwoerter="h: (7; 3; 3) + s · (1; 2; 3), parallel zu E|Gerade mit kleinstem Abstand geht durch den Lotfußpunkt des Stützpunkts|g ist das Lot: Schnitt mit E bei r = −2, Punkt (1; 3; 5)|x = (1; 3; 5) + t · (1; 2; 3)",
    voraussetzungen="Abstand paralleler Geraden über das Lot|g als Lotgerade durch den Stützpunkt von h erkennen|Schnittpunkt Gerade–Ebene",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="h: x = (7; 3; 3) + s · (1; 2; 3) ohne gemeinsamen Punkt mit E; g aus a (durch (7; 3; 3), senkrecht zu E)",
    gesucht="Gleichung der Geraden in E, die parallel zu h ist und von h den kleinsten Abstand hat",
    verfahren="Lotfußpunkt des Stützpunkts von h als Schnittpunkt von g mit E, dann Richtung von h",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2022MerhoehtAAGLAA211-a",
    ergebnis="3 · (7 + 3r) − (3 − r) + 2 = 0 ⇔ 10r + 20 = 0 ⇔ r = −2, d. h. g schneidet E im Punkt (1; 3; 5); damit x = (1; 3; 5) + t · (1; 2; 3), t reell (amtlich)",
    zwischenergebnis="Abstand √(36 + 4) = √40",
    niveau_geschaetzt="III",
    fehlerquelle="irgendeine Gerade in E parallel zu h angeben, ohne den Lotfußpunkt",
    bemerkung="Standardbezug: K2 II, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Sonderfall erkennen – g aus a ist das Lot vom Stützpunkt von h auf E – und (a) „kleinster Abstand“ in den Lotfußpunkt übersetzen; amtlich II.")

# ---- AG/LA (A2) 1.2: Spiegelebene aus P und Q
row("2022MerhoehtAAGLAA212", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Spiegelebene aus Punkt und Spiegelpunkt bestimmen", typ_neben="",
    stichwoerter="P(1; 2; 3), Q(7; 2; 11)|PQ = (6; 0; 8) Normalenvektor|Mittelpunkt M(4; 2; 7) in E|6x + 8z − 80 = 0",
    voraussetzungen="Verbindungsvektor als Normalenvektor der Spiegelebene|Mittelpunkt liegt in der Ebene|Koordinatenform",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Spiegelung von P(1; 2; 3) an E ergibt Q(7; 2; 11)",
    gesucht="Gleichung von E in Koordinatenform",
    verfahren="Normalenvektor PQ, Mittelpunkt einsetzen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="PQ = (6; 0; 8) ist ein Normalenvektor von E, die Gleichung hat die Form 6x + 8z + c = 0; der Mittelpunkt M(4; 2; 7) von PQ liegt genau dann in E, wenn c = −6 · 4 − 8 · 7 = −80 (amtlich)",
    zwischenergebnis="gleichwertig 3x + 4z = 40",
    niveau_geschaetzt="II",
    fehlerquelle="P statt M in die Ebenengleichung einsetzen",
    bemerkung="Standardbezug: K2 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtAAGLAA212", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Punkt auf der Spiegelachse mit vorgegebenem Abstandsverhältnis zur Spiegelebene bestimmen", typ_neben="",
    stichwoerter="R und S symmetrisch zu E auf der Geraden PQ|RS doppelt so lang wie PQ|R = M − PQ = (−2; 2; −1)",
    voraussetzungen="Symmetrie zu E heißt gleicher Abstand vom Mittelpunkt|Streckenverhältnis als Vektorvielfaches|Seite von P wählen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="P, Q, M(4; 2; 7); R und S auf der Geraden PQ symmetrisch zu E, R auf der Seite von P; |RS| = 2 · |PQ|",
    gesucht="Koordinaten von R",
    verfahren="R = M − PQ (Abstand |PQ| vom Mittelpunkt in Richtung P)",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2022MerhoehtAAGLAA212-a",
    ergebnis="OR = OM − PQ = (−2; 2; −1) (amtlich)",
    zwischenergebnis="S(10; 2; 15)",
    niveau_geschaetzt="II",
    fehlerquelle="R = P − PQ = (−5; 2; −5) rechnen (Verhältnis von P statt von M aus)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. „Doppelt so groß“ ist wörtlich vorgegeben, nach dem Prinzip keine Deutung.")

# ---- AG/LA (A2) 1.3: Mittelsenkrechte parallel zur x1x3-Ebene (ungegliedert)
row("2022MerhoehtAAGLAA213", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Mittelsenkrechte einer Strecke parallel zu einer Koordinatenebene bestimmen", typ_neben="",
    stichwoerter="A(−5; 5; −3), B(−1; 1; −1)|Mittelpunkt (−3; 3; −2)|Richtung (a; 0; b) wegen Parallelität zur x1x3-Ebene|AB · (a; 0; b) = 4a + 2b = 0|a = −1, b = 2",
    voraussetzungen="Mittelpunkt|parallel zur x1x3-Ebene heißt zweite Komponente 0|Skalarprodukt mit AB null",
    format="Rechnung", operator="Geben Sie an|Bestimmen Sie", antwort="Zahl|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(−5; 5; −3), B(−1; 1; −1)",
    gesucht="Mittelpunkt von AB; Gleichung der Mittelsenkrechten von AB, die parallel zur x1x3-Ebene verläuft",
    verfahren="Mittelpunkt als Stützpunkt, Richtungsvektor (a; 0; b) senkrecht zu AB",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Mittelpunkt (−3; 3; −2); die gesuchte Gleichung hat die Form x = (−3; 3; −2) + λ · (a; 0; b); AB · (a; 0; b) = (4; −4; 2) · (a; 0; b) = 0 liefert a = −1 und b = 2 als geeignete Werte (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Mittelsenkrechte als Ebene aufstellen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 1.3). Die Bedingung „parallel zur x1x3-Ebene“ ist eine unmittelbare Übersetzung (zweite Komponente 0), nach dem Prinzip II.")

# ---- AG/LA (A2) 2.1: Quadrat, Lot von A auf g
QUAD_SKIZZE = ("nicht maßstabsgetreue Skizze: Quadrat ABCD, A unten, B rechts, C oben rechts, D links oben; "
               "waagerechte Gerade g durch B und den Mittelpunkt M von AD mit Richtungspfeil v nach rechts; "
               "F auf g zwischen M und B als Lotfußpunkt von A")
row("2022MerhoehtAAGLAA221", "a", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Streckenverhältnis am Lot im Quadrat über ähnliche Dreiecke begründen", typ_neben="",
    stichwoerter="Dreiecke ABM und ABF: gemeinsamer Winkel bei B, je ein rechter Winkel|ähnlich|BF/AF = AB/AM = 2|BF = 2 · AF",
    voraussetzungen="Ähnlichkeit über zwei gleiche Winkel|Verhältnis entsprechender Seiten|AM = AD/2 = AB/2",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Skizze", skizze=QUAD_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Quadrat ABCD; g durch B und den Mittelpunkt M von AD mit Richtungsvektor v; F Lotfußpunkt von A auf g",
    gesucht="Begründung, dass |BF| = 2 · |AF| gilt",
    verfahren="Dreiecke ABM und ABF als ähnlich erkennen und Seitenverhältnisse übertragen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Dreiecke ABM und ABF haben bei B einen gemeinsamen Winkel und außerdem jeweils einen rechten Winkel, d. h. sie sind ähnlich; damit gilt |BF|/|AF| = |AB|/|AM| = 2 (amtlich)",
    zwischenergebnis="Kontrolle mit Koordinaten (Seite 2): F = B + 4/5 · BM",
    niveau_geschaetzt="III",
    fehlerquelle="mit Koordinaten rechnen wollen, obwohl keine gegeben sind",
    bemerkung="Standardbezug: K1 II, K2 III, K4 II. Amtlich, eigene Rechnung bestätigt (Koordinatenmodell). Eichregel: (b) Sonderfall erkennen – Ähnlichkeit der beiden rechtwinkligen Dreiecke – und mit dem Seitenverhältnis verketten.")

row("2022MerhoehtAAGLAA221", "b", seite="1", punkte="2", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Vektorterm für einen Punkt aus Lotfußpunkt, Abstand und Richtungsvektor angeben", typ_neben="",
    stichwoerter="B liegt auf g im Abstand |BF| = 2 · |AF| von F in Richtung v|OB = OF + 2 · |AF| · v/|v|",
    voraussetzungen="Einheitsvektor v/|v||Länge aus a|Richtung am Bild ablesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Skizze", skizze=QUAD_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Koordinaten von A und F sowie v als bekannt angenommen; |BF| = 2 · |AF| aus a",
    gesucht="Term für die Koordinaten von B",
    verfahren="vom Lotfußpunkt F um die Länge 2 · |AF| in Richtung des Einheitsvektors von v gehen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2022MerhoehtAAGLAA221-a",
    ergebnis="OB = OF + 2 · |AF| · v/|v| (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="v ohne Normierung verwenden (OF + 2 · |AF| · v)",
    bemerkung="Standardbezug: K2 III, K4 II. Amtlich, eigene Rechnung bestätigt (Koordinatenmodell). Eichregel: (a) die Lage von B (auf g, Abstand 2 · |AF| von F, Richtung v) in einen Vektorterm mit Einheitsvektor übersetzen – Verkettung mit dem Ergebnis aus a.")

# ---- AG/LA (A2) 2.2: Ebenenschar ax + y + 4z = 4
SCHAR_SKIZZE = ("Schrägbild mit y-Achse nach rechts (Markierungen −4, 4), z-Achse nach oben (Markierungen −2, 2), "
                "x-Achse nach links unten (Markierung 4 bei etwa (−2; −2) der Zeichenebene); Gitter; Gerade h in "
                "der yz-Ebene durch (y; z) = (0; 1) und (4; 0), fallend von links oben nach rechts unten")
row("2022MerhoehtAAGLAA222", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Gemeinsame Gerade aller Ebenen einer Schar aus der Abbildung begründen", typ_neben="",
    stichwoerter="E_a: ax + y + 4z = 4|h in der yz-Ebene durch (0; 0; 1) und (0; 4; 0)|beide Punkte erfüllen die Gleichung für jedes a (x = 0)",
    voraussetzungen="Punkte von h aus dem Schrägbild ablesen|Punktprobe mit Parameter|Gerade in Ebene über zwei Punkte",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SCHAR_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Schar E_a: ax + y + 4z = 4, a reell; Gerade h in der yz-Ebene in der Abbildung",
    gesucht="Begründung, dass alle Ebenen der Schar h enthalten",
    verfahren="zwei Punkte von h ablesen und in die Schargleichung einsetzen; wegen x = 0 fällt a heraus",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Punkte (0; 0; 1) und (0; 4; 0) liegen auf h und erfüllen die Gleichung von E_a (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur einen Punkt prüfen",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt. Punkte aus der Abbildung.")

row("2022MerhoehtAAGLAA222", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Darstellung einer Ebene im Schrägbild als Gerade beurteilen", typ_neben="",
    stichwoerter="(2; 1; 1) Richtungsvektor von E: a = −5/2|E enthält h und den Punkt (2; 1; 2) = (0; 0; 1) + (2; 1; 1)|im Schrägbild fällt (2; 1; 2) auf h (x-Einheit auf (−1/2; −1/2))|Aussage richtig",
    voraussetzungen="Richtungsvektor ergänzt h zu einem weiteren Punkt|Projektion im Schrägbild|Ebene erscheint als Gerade, wenn ihre Richtungen auf h abgebildet werden",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SCHAR_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="(2; 1; 1) ist Richtungsvektor einer Ebene E der Schar; Aussage: die Darstellung von E in der Abbildung würde mit der von h übereinstimmen",
    gesucht="Beurteilung der Aussage",
    verfahren="Punkt (2; 1; 2) von E bilden und sein Bild im Schrägbild mit h vergleichen",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2022MerhoehtAAGLAA222-a",
    ergebnis="da (2; 1; 1) ein Richtungsvektor der Ebene ist, enthält diese Ebene neben den Punkten von h auch den Punkt (2; 1; 2); würde man diesen Punkt in der Abbildung darstellen, so fiele diese Darstellung mit einem Punkt von h zusammen; die Aussage ist also richtig (amtlich)",
    zwischenergebnis="E = E_(−5/2): −5/2 x + y + 4z = 4; Bild von (2; 1; 2) ist (y; z) = (0; 1) auf h",
    niveau_geschaetzt="III",
    fehlerquelle="die Aussage verneinen, weil eine Ebene „immer eine Fläche“ sei",
    bemerkung="Standardbezug: K1 III, K2 III, K4 III, K6 II. Amtlich, eigene Rechnung bestätigt (Projektion mit x-Einheit auf (−1/2; −1/2), wie die Markierung 4 in der Abbildung zeigt). Eichregel: (b) Sonderfall erkennen – die Blickrichtung des Schrägbilds liegt in E – und (d) in die Aussage über die Darstellung übersetzen.")

# ---- Stochastik 1.1: Augensumme und Binomialverteilung
DIAG_SKIZZE = ("drei Säulendiagramme I, II, III mit Werten 0 bis 12 auf der x-Achse und y-Achse bis 0,2: I symmetrisch "
               "um 7 mit Maximum etwa 0,19, Säulen bei 2 und 12 kaum sichtbar; II symmetrisch um 7 mit Maximum etwa "
               "0,17, Säule bei 2 etwa 0,03 und bei 3 etwa 0,06; III asymmetrisch mit Maximum etwa 0,23 bei 7, "
               "links flacher auslaufend als rechts, Säule bei 12 sichtbar")
row("2022MerhoehtAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Gleichheit zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen", typ_neben="",
    stichwoerter="X Augensumme zweier Würfel|Summe 4: (1;3), (2;2), (3;1)|Summe 10: (4;6), (5;5), (6;4)|je drei von 36 Ergebnissen",
    voraussetzungen="Ergebnisraum der Paare|Ergebnisse zu einer Summe aufzählen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Würfel", textumfang="mittel",
    gegeben="X Augensumme bei zwei Würfen eines Würfels mit 1 bis 6",
    gesucht="Begründung, dass P(X = 4) = P(X = 10)",
    verfahren="günstige Ergebnisse beider Ereignisse zählen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="bei Verwendung des Ergebnisraums {(1; 1), (1; 2), …, (2; 1), …, (6; 6)} bestehen beide betrachteten Ereignisse jeweils aus drei Ergebnissen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="(2; 2) doppelt zählen",
    bemerkung="Standardbezug: K1 I, K3 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ea-A wiederverwendet.")

row("2022MerhoehtAStochastik11", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsgrößen und Verteilungen",
    typ="Verteilungen zweier Zufallsgrößen den Säulendiagrammen zuordnen", typ_neben="",
    stichwoerter="Y ~ B(12; 0,6) asymmetrisch: Diagramm III|X symmetrisch, P(X = 3) = 2 · P(X = 2): Diagramm II|Diagramm I passt zu keiner",
    voraussetzungen="Binomialverteilung mit p ≠ 0,5 ist asymmetrisch|Symmetrie der Augensumme|Verhältnis kleiner Wahrscheinlichkeiten prüfen",
    format="Begründung", operator="Ordnen Sie zu|Begründen Sie", antwort="Text",
    material="Diagramm", skizze=DIAG_SKIZZE, kontext="Würfel und Urne", textumfang="mittel",
    gegeben="X Augensumme zweier Würfel; Y Anzahl schwarzer Kugeln bei zwölf Zügen mit Zurücklegen aus 60 schwarzen und 40 weißen; Diagramme I, II, III",
    gesucht="Zuordnung von X und Y zu den Diagrammen mit Begründung",
    verfahren="Asymmetrie für Y, Verhältnis P(X = 3) : P(X = 2) = 2 für X",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="da die Wahrscheinlichkeitsverteilung von Y asymmetrisch ist, kommt dafür nur das Diagramm III infrage; die Wahrscheinlichkeit P(X = 3) ist doppelt so groß wie P(X = 2), folglich wird die Verteilung von X durch das Diagramm II dargestellt (amtlich)",
    zwischenergebnis="P(X = 2) = 1/36, P(X = 3) = 2/36",
    niveau_geschaetzt="II",
    fehlerquelle="X dem Diagramm I zuordnen (Säulen bei 2 und 3 nicht prüfen)",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Zufallsgrößen und Verteilungen im erhöhten Niveau.")

# ---- Stochastik 1.2: Spielfeld (Datei mit drei Seiten, a und b auf Seite 2)
FELD_SKIZZE = ("Spielfeld: Gitter mit Spalten A bis E und Zeilen 1 bis 5, Spielfigur auf (A|1) links unten; Tabelle "
               "der Würfelseiten: „rechts“ 2 Seiten (Zug ein Feld nach rechts), „oben“ 3 Seiten (ein Feld nach oben), "
               "„rechts oben“ 1 Seite (diagonal ein Feld nach rechts oben)")
row("2022MerhoehtAStochastik12", "a", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für das Erreichen eines Feldes über die Pfadregel berechnen", typ_neben="",
    stichwoerter="von (A|1) nach (A|4): dreimal „oben“|P(oben) = 3/6 = 1/2|(1/2)³ = 1/8",
    voraussetzungen="Zugwahrscheinlichkeiten aus der Tabelle|einziger Pfad|Pfadregel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm|Tabelle", skizze=FELD_SKIZZE, kontext="Brettspiel", textumfang="lang",
    gegeben="Spielfeld A–E × 1–5, Start (A|1); Würfel mit 2 Seiten „rechts“, 3 Seiten „oben“, 1 Seite „rechts oben“",
    gesucht="Wahrscheinlichkeit, dass die Figur im Laufe eines Spiels (A|4) erreicht",
    verfahren="nur der Pfad oben, oben, oben führt dorthin",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(1/2)³ = 1/8 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="(3/6)³ mit 3/6 als 3 rechnen oder Pfade mit „rechts“ mitzählen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Datei mit drei Seiten, Teilaufgaben auf Seite 2.")

row("2022MerhoehtAStochastik12", "b", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="3 · (1/3)² · 1/2: zweimal rechts, einmal oben in beliebiger Reihenfolge|2 · 1/6 · 1/3: einmal rechts, einmal rechts oben|beide führen nach (C|2)|Wert 5/18",
    voraussetzungen="Faktoren als Zugwahrscheinlichkeiten lesen|Vorfaktoren als Anzahl der Reihenfolgen|Zielfeld aus den Zügen",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text",
    material="Diagramm|Tabelle", skizze=FELD_SKIZZE, kontext="Brettspiel", textumfang="lang",
    gegeben="Term 3 · (1/3)² · 1/2 + 2 · 1/6 · 1/3",
    gesucht="Begründung, dass der Term die Wahrscheinlichkeit für das Erreichen eines bestimmten Punktes liefert; Koordinaten dieses Punktes",
    verfahren="beide Summanden als Zugfolgen deuten, Zielfeld bestimmen",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2022MerhoehtAStochastik12-a",
    ergebnis="der Term 3 · (1/3)² · 1/2 gibt die Wahrscheinlichkeit an, dass in beliebiger Reihenfolge zweimal „rechts“ und einmal „oben“ erzielt wird; der Term 2 · 1/6 · 1/3 die, dass einmal „rechts“ und einmal „rechts oben“ erzielt wird; diese Ergebnisse sind genau diejenigen, die vom Startpunkt zum Punkt (C|2) führen (amtlich)",
    zwischenergebnis="Wert 5/18, durch Aufzählen aller Zugfolgen bestätigt",
    niveau_geschaetzt="III",
    fehlerquelle="den Vorfaktor 3 als dritte Zugwahrscheinlichkeit lesen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Term → Ereignis, hier mit Anordnungsfaktoren und Zielfeld). Eichregel: (d) Term in eine Sachaussage mit zwei Deutungen (zwei Summanden als Zugfolgen) und Verkettung zum Zielpunkt; amtlich II.")

# ---- Stochastik 1.3: Normalverteilung
NV_SKIZZE = ("Koordinatensystem mit Gitter (Schrittweite 1 in x, 0,1 in y), x-Achse von 0 bis 17 mit den Markierungen "
             "0, 2, …, 16, y-Achse bis 0,3; Glockenkurve mit Maximum 0,2 bei x = 8, Wendestellen etwa 6 und 10, "
             "bei 2 und 14 praktisch null")
row("2022MerhoehtAStochastik13", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Wahrscheinlichkeit außerhalb eines symmetrischen Intervalls über die Symmetrie der Normalverteilung berechnen", typ_neben="",
    stichwoerter="P(6 ≤ A ≤ 10) ≈ 68 %, μ = 8|außerhalb 32 %, symmetrisch aufgeteilt|P(A > 10) = 16 %",
    voraussetzungen="Symmetrie der Dichte um μ|Gegenwahrscheinlichkeit",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=NV_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="A normalverteilt, Dichte in der Abbildung mit Maximum bei 8; P(A in [6; 10]) ≈ 68 %",
    gesucht="P(A > 10)",
    verfahren="(100 % − 68 %)/2",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="(100 % − 68 %)/2 = 16 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="32 % angeben (nicht halbieren)",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Normalverteilung im Pool 2022.")

row("2022MerhoehtAStochastik13", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Dichtefunktion mit gleichem Erwartungswert und größerer Standardabweichung skizzieren", typ_neben="",
    stichwoerter="gleiches μ = 8, größeres σ|Kurve breiter und niedriger|Maximum unter 0,2, Wendestellen weiter außen",
    voraussetzungen="Wirkung von σ auf Breite und Höhe der Glockenkurve|Flächeninhalt 1 bleibt",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=NV_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Dichte von A in der Abbildung; B normalverteilt mit gleichem Erwartungswert und größerer Standardabweichung",
    gesucht="Skizze eines möglichen Graphen der Dichte von B in der Abbildung",
    verfahren="flachere, breitere Glockenkurve mit Maximum bei 8 einzeichnen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Glockenkurve mit Maximum bei x = 8, niedriger (etwa 0,13) und breiter als die von A; der Erwartungshorizont zeigt die Skizze (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Kurve breiter, aber gleich hoch zeichnen (Fläche größer als 1)",
    bemerkung="Standardbezug: K4 II, K6 II. Amtlich.")

# ---- Stochastik 2.1: Auszahlung nach Kugelzahl (ungegliedert)
row("2022MerhoehtAStochastik21", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Kugelzahl für den größten Erwartungswert der Auszahlung ermitteln", typ_neben="",
    stichwoerter="b blaue, 100 − b rote Kugeln|rot: Auszahlung b Cent mit (100 − b)/100; blau: 10 Cent mit b/100|E = −1/100 · b · (b − 110)|Parabel mit Nullstellen 0 und 110, Scheitel bei 55",
    voraussetzungen="Erwartungswert als Term in b|Auszahlung hängt selbst von b ab|Scheitel aus den Nullstellen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel/Urne", textumfang="lang",
    gegeben="100 Kugeln, b blaue vom Spieler gewählt; eine Kugel wird gezogen; rot: Auszahlung b Cent, blau: 10 Cent",
    gesucht="Wahl von b, für die der Erwartungswert der Auszahlung möglichst groß ist",
    verfahren="E(b) aufstellen, als Parabel deuten, Scheitel in der Mitte der Nullstellen",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="Cent", abhaengig_von="",
    ergebnis="mit b für die Anzahl der blauen Kugeln kann der Erwartungswert der Auszahlung in Cent mit (100 − b)/100 · b + b/100 · 10 = −1/100 · b · (b − 110) berechnet werden; der Term beschreibt eine nach unten geöffnete Parabel mit den Nullstellen 0 und 110; der Spieler muss sich also für 55 blaue Kugeln entscheiden (amtlich)",
    zwischenergebnis="E(55) = 30,25 Cent",
    niveau_geschaetzt="III",
    fehlerquelle="die Auszahlung bei rot als feste Zahl statt als b ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.1). Eichregel: (a) die Spielregel in einen Erwartungswertterm in b übersetzen, in dem b zugleich Wahrscheinlichkeit und Auszahlung bestimmt, und das Maximum bestimmen.")

# ---- Stochastik 2.2: Würfel mit 1, 2, 3 je zweimal
row("2022MerhoehtAStochastik22", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Verhältnis zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen", typ_neben="",
    stichwoerter="Zahlen 1, 2, 3 je mit 1/3|dreimal gleich: 3 Ergebnisse (1;1;1), (2;2;2), (3;3;3)|drei verschiedene: 3! = 6 Ergebnisse|jedes Tripel gleich wahrscheinlich, Verhältnis 1 : 2",
    voraussetzungen="Ergebnisse als Tripel gleich wahrscheinlich|Permutationen zählen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Würfel", textumfang="mittel",
    gegeben="Würfel mit den Zahlen 1, 2, 3 je zweimal; dreimal geworfen",
    gesucht="Begründung, dass P(dreimal dieselbe Zahl) halb so groß ist wie P(drei verschiedene Zahlen)",
    verfahren="Anzahl der Ergebnisse beider Ereignisse vergleichen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="das Ereignis „Es wird dreimal die gleiche Zahl erzielt.“ besteht aus 3 Ergebnissen, das Ereignis „Es werden drei verschiedene Zahlen erzielt“ aus 3! = 6 Ergebnissen (amtlich)",
    zwischenergebnis="1/9 und 2/9",
    niveau_geschaetzt="II",
    fehlerquelle="für „drei verschiedene“ nur ein Ergebnis {1, 2, 3} zählen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. Amtlich, eigene Rechnung bestätigt. Vorschlag für den Abgleich: mit „Laplace-Experiment: Gleichheit zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen“ zu „Vergleich zweier Wahrscheinlichkeiten …“ zusammenziehen.")

row("2022MerhoehtAStochastik22", "b", seite="1", punkte="3", afb_amtlich="III",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Term für das Gegenereignis einer festen Häufigkeitsverteilung bei mehreren Würfen angeben", typ_neben="",
    stichwoerter="sechs Würfe, jede Zahl genau zweimal: (6 über 2) · (4 über 2) Anordnungen mal (1/3)⁶|Gegenereignis: 1 − (6 über 2) · (1/3)² · (4 über 2) · (1/3)² · (1/3)²",
    voraussetzungen="Gegenereignis|Anordnungen einer festen Häufigkeitsverteilung als Produkt von Binomialkoeffizienten|Pfadwahrscheinlichkeit",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Würfel", textumfang="kurz",
    gegeben="Würfel mit 1, 2, 3 je zweimal; sechsmal geworfen",
    gesucht="Term für die Wahrscheinlichkeit, dass nicht jede Zahl genau zweimal erzielt wird",
    verfahren="über das Gegenereignis „jede Zahl genau zweimal“ mit Auswahl der Positionen",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="1 − (6 über 2) · (1/3)² · (4 über 2) · (1/3)² · (1/3)² (amtlich)",
    zwischenergebnis="Wert 1 − 10/81 = 71/81, durch Abzählen aller 729 Folgen bestätigt",
    niveau_geschaetzt="III",
    fehlerquelle="Binomialverteilung mit n = 6, p = 1/3 für eine einzelne Zahl ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „nicht jede Zahl zweimal“ als Gegenereignis einer Häufigkeitsverteilung übersetzen und mit dem Abzählen der Anordnungen verketten.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Integral über f aus dem Graphen der Stammfunktion bestimmen", "Analysis", "Stammfunktion und Hauptsatz",
     "Ein bestimmtes Integral über f mit dem Hauptsatz aus abgelesenen Werten des abgebildeten Graphen einer "
     "Stammfunktion berechnen.",
     "2022MerhoehtAAnalysis11-a"),
    ("Funktionswert von f als Tangentensteigung am Graphen der Stammfunktion bestimmen", "Analysis",
     "Stammfunktion und Hauptsatz",
     "Einen Funktionswert von f als Steigung der Tangente an den abgebildeten Graphen der Stammfunktion "
     "ablesen und das Vorgehen einzeichnen.",
     "2022MerhoehtAAnalysis11-b"),
    ("Symmetrie: Achsensymmetrie am Term über gerade Exponenten begründen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Die Achsensymmetrie eines Graphen zur y-Achse damit begründen, dass der Term nur gerade Exponenten enthält.",
     "2022MerhoehtAAnalysis12-a"),
    ("Scharparameter für eine vorgegebene Wendestelle berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameter einer Schar so berechnen, dass eine vorgegebene Stelle Wendestelle ist (zweite Ableitung "
     "mit Parameter gleich null).",
     "2022MerhoehtAAnalysis12-b"),
    ("Graph der Schar zu einem Parameterwert in die Abbildung skizzieren", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Den Graphen eines Scharmitglieds zu einem vorgegebenen Parameterwert in eine Abbildung mit anderen "
     "Scharmitgliedern skizzieren.",
     "2022MerhoehtAAnalysis13-a"),
    ("Existenz von Scharparametern mit beliebig vielen Schnittstellen begründen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Begründen, dass es Parameterwerte gibt, für die eine Schar einen periodischen Graphen beliebig oft "
     "schneidet (Stauchung für kleine Parameter).",
     "2022MerhoehtAAnalysis13-b"),
    ("Quadratische Funktion aus senkrechtem Schnitt mit einer Geraden und einer Extrempunktbedingung ermitteln",
     "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Die Gleichung einer quadratischen Funktion aus einem Punkt, der Orthogonalität zu einer Geraden dort "
     "und einer Bedingung an die Koordinaten des Extrempunkts ermitteln.",
     "2022MerhoehtAAnalysis2"),
    ("Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Einen Eintrag der Übergangsmatrix als Anteil oder Faktor eines Übergangs zwischen zwei Zuständen deuten.",
     "2022MerhoehtAAGLAA111-a"),
    ("Übergangsprozess: Unbekannte Anzahl aus einer Bedingung an den Folgezustand berechnen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine unbekannte Komponente des Startvektors aus einer Bedingung an eine Komponente des Folgevektors "
     "über eine Zeile des Matrix-Vektor-Produkts berechnen.",
     "2022MerhoehtAAGLAA111-b"),
    ("Übergangsprozess: Matrix bei geänderter Reihenfolge der Zustände angeben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Die Übergangsmatrix für eine andere Reihenfolge der Zustände im Vektor angeben (Zeilen und Spalten "
     "gleich umsortieren).",
     "2022MerhoehtAAGLAA111-c"),
    ("Matrizenalgebra: Faktor aus M² als Vielfachem der Einheitsmatrix ermitteln", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "M² berechnen und den Faktor a mit M² = a · E ablesen.",
     "2022MerhoehtAAGLAA112-a"),
    ("Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Alle Lösungen der Gleichung M · v = t · v für einen vorgegebenen Wert t als Vielfache eines Vektors angeben.",
     "2022MerhoehtAAGLAA112-b"),
    ("Matrizenalgebra: Erhalt der Spaltensumme unter einer stochastischen Matrix allgemein nachweisen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Mit allgemeiner Matrix und allgemeinem Vektor zeigen, dass eine stochastische Matrix die Komponentensumme "
     "eines Vektors erhält.",
     "2022MerhoehtAAGLAA12-b"),
    ("Gerade in einer Ebene parallel zu einer Geraden mit kleinstem Abstand bestimmen", "Analytische Geometrie",
     "Abstände",
     "Zu einer Geraden parallel zur Ebene die Gerade in der Ebene bestimmen, die parallel ist und den kleinsten "
     "Abstand hat: durch den Lotfußpunkt eines Punktes der Geraden.",
     "2022MerhoehtAAGLAA211-b"),
    ("Spiegelebene aus Punkt und Spiegelpunkt bestimmen", "Analytische Geometrie", "Spiegelung",
     "Die Koordinatengleichung der Spiegelebene aus einem Punkt und seinem Spiegelpunkt aufstellen: "
     "Verbindungsvektor als Normalenvektor, Mittelpunkt in der Ebene.",
     "2022MerhoehtAAGLAA212-a"),
    ("Punkt auf der Spiegelachse mit vorgegebenem Abstandsverhältnis zur Spiegelebene bestimmen",
     "Analytische Geometrie", "Spiegelung",
     "Einen Punkt auf der Geraden durch Punkt und Spiegelpunkt bestimmen, dessen Abstand zur Spiegelebene in "
     "einem vorgegebenen Verhältnis zum Abstand des Punktes steht.",
     "2022MerhoehtAAGLAA212-b"),
    ("Geraden und Ebenen: Mittelsenkrechte einer Strecke parallel zu einer Koordinatenebene bestimmen",
     "Analytische Geometrie", "Orthogonalität",
     "Die Gleichung der Mittelsenkrechten einer Strecke aufstellen, deren Richtungsvektor parallel zu einer "
     "Koordinatenebene und senkrecht zur Strecke ist.",
     "2022MerhoehtAAGLAA213"),
    ("Dreieck: Streckenverhältnis am Lot im Quadrat über ähnliche Dreiecke begründen", "Analytische Geometrie",
     "Orthogonalität",
     "Ein Streckenverhältnis am Lotfußpunkt in einer Quadratfigur ohne Koordinaten über die Ähnlichkeit "
     "rechtwinkliger Dreiecke begründen.",
     "2022MerhoehtAAGLAA221-a"),
    ("Vektorterm für einen Punkt aus Lotfußpunkt, Abstand und Richtungsvektor angeben", "Analytische Geometrie",
     "Vektoren und Rechenoperationen",
     "Den Ortsvektor eines Punktes als Lotfußpunkt plus Abstand mal Einheitsvektor einer gegebenen Richtung angeben.",
     "2022MerhoehtAAGLAA221-b"),
    ("Gemeinsame Gerade aller Ebenen einer Schar aus der Abbildung begründen", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Begründen, dass alle Ebenen einer Schar eine abgebildete Gerade enthalten, indem zwei abgelesene Punkte "
     "der Geraden die Schargleichung für jeden Parameter erfüllen.",
     "2022MerhoehtAAGLAA222-a"),
    ("Darstellung einer Ebene im Schrägbild als Gerade beurteilen", "Analytische Geometrie", "Ebenen",
     "Beurteilen, ob eine Ebene im Schrägbild mit einer Geraden zusammenfällt, indem ein weiterer Punkt der "
     "Ebene projiziert wird.",
     "2022MerhoehtAAGLAA222-b"),
    ("Verteilungen zweier Zufallsgrößen den Säulendiagrammen zuordnen", "Stochastik",
     "Zufallsgrößen und Verteilungen",
     "Zwei beschriebene Zufallsgrößen den passenden Säulendiagrammen zuordnen und die Zuordnung über Symmetrie "
     "und Verhältnisse einzelner Wahrscheinlichkeiten begründen.",
     "2022MerhoehtAStochastik11-b"),
    ("Wahrscheinlichkeit für das Erreichen eines Feldes über die Pfadregel berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit berechnen, ein Feld eines Spielfelds zu erreichen, wenn nur ein Pfad von Zügen "
     "dorthin führt.",
     "2022MerhoehtAStochastik12-a"),
    ("Wahrscheinlichkeit außerhalb eines symmetrischen Intervalls über die Symmetrie der Normalverteilung berechnen",
     "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Aus der Wahrscheinlichkeit eines um den Erwartungswert symmetrischen Intervalls die Wahrscheinlichkeit "
     "einer Seite außerhalb über die Symmetrie berechnen.",
     "2022MerhoehtAStochastik13-a"),
    ("Dichtefunktion mit gleichem Erwartungswert und größerer Standardabweichung skizzieren", "Stochastik",
     "Normalverteilung und Sigma-Regeln",
     "In die Abbildung einer Dichtefunktion eine zweite mit gleichem Erwartungswert und größerer "
     "Standardabweichung skizzieren (breiter und niedriger).",
     "2022MerhoehtAStochastik13-b"),
    ("Kugelzahl für den größten Erwartungswert der Auszahlung ermitteln", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Die vom Spieler wählbare Kugelzahl bestimmen, die den Erwartungswert der Auszahlung maximiert, wenn "
     "die Kugelzahl Wahrscheinlichkeit und Auszahlung zugleich bestimmt.",
     "2022MerhoehtAStochastik21"),
    ("Laplace-Experiment: Verhältnis zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen",
     "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Das Verhältnis der Wahrscheinlichkeiten zweier Ereignisse über die Anzahl ihrer gleich wahrscheinlichen "
     "Ergebnisse begründen.",
     "2022MerhoehtAStochastik22-a"),
    ("Term für das Gegenereignis einer festen Häufigkeitsverteilung bei mehreren Würfen angeben", "Stochastik",
     "Kombinatorik",
     "Einen Term für die Wahrscheinlichkeit angeben, dass eine vorgegebene Häufigkeitsverteilung der Ergebnisse "
     "nicht eintritt: Gegenereignis mit Anordnungen als Produkt von Binomialkoeffizienten.",
     "2022MerhoehtAStochastik22-b"),
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
