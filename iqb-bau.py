# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.3 · 13.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.4

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

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
    "stapel": "2025-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2025MerhoehtAAnalysis11": 5,
        "2025MerhoehtAAnalysis12": 5,
        "2025MerhoehtAAnalysis13": 5,
        "2025MerhoehtAAnalysis21": 5,
        "2025MerhoehtAAnalysis22": 5,
        "2025MerhoehtAAnalysis23": 5,
        "2025MerhoehtAAGLAA11": 5,
        "2025MerhoehtAAGLAA121": 5,
        "2025MerhoehtAAGLAA122": 5,
        "2025MerhoehtAAGLAA211": 5,
        "2025MerhoehtAAGLAA212": 5,
        "2025MerhoehtAAGLAA221": 5,
        "2025MerhoehtAAGLAA222": 5,
        "2025MerhoehtAAGLAA223": 5,
        "2025MerhoehtAStochastik11": 5,
        "2025MerhoehtAStochastik12": 5,
        "2025MerhoehtAStochastik21": 5,
        "2025MerhoehtAStochastik22": 5,
        "2025MerhoehtAStochastik23": 5,
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


HEAD, VOK, LEITIDEEN, THEMEN = vokabular()
ZIELE, GELTUNG = geltung()
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
# niveau_geschaetzt nach der engen Fassung „Kombinieren mit Deutung heißt III" (iqb.md § 7,
# seit 2025-ga-A geltende Regel); ein Vermerk „Schätzung enge Fassung" ist deshalb nicht nötig.

# ---- Analysis 1.1: Schar x · e^(−a x²), Steigung im Ursprung, Punktsymmetrie
row("2025MerhoehtAAnalysis11", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gleiche Steigung aller Graphen einer Schar im Ursprung nachweisen", typ_neben="",
    stichwoerter="Produkt- und Kettenregel|f_a'(x) = e^(−a x²) + x · (−2ax · e^(−a x²))|f_a'(0) = 1|unabhängig von a",
    voraussetzungen="Produktregel|Kettenregel mit e-Funktion|Parameter als Konstante behandeln",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = x · e^(−a · x²), definiert in IR, a reell und a > 0; jeder Graph verläuft durch den Ursprung",
    gesucht="Nachweis, dass alle Graphen der Schar im Ursprung dieselbe Steigung haben",
    verfahren="f_a' mit Produkt- und Kettenregel bilden und x = 0 einsetzen; der Wert hängt nicht von a ab",
    schritte="2", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="f_a'(x) = 1 · e^(−a x²) + x · (−2a · x · e^(−a x²)); f_a'(0) = 1 für alle Werte von a (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Kettenregel bei e^(−a x²) vergessen (innere Ableitung −2ax)",
    bemerkung="Standardbezug: K4 I, K5 II. Amtlich, eigene Rechnung bestätigt. Thema Funktionsscharen und Ortskurven (nicht für das grundlegende Niveau in BE und BB).")

row("2025MerhoehtAAnalysis11", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Punktsymmetrie aller Graphen einer Schar zum Ursprung nachweisen", typ_neben="",
    stichwoerter="f_a(−x) = −f_a(x)|(−x)² = x²|Symmetriekriterium",
    voraussetzungen="Kriterium für Punktsymmetrie zum Ursprung|−x in einen Term mit Quadrat einsetzen",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = x · e^(−a · x²), a > 0",
    gesucht="Nachweis, dass alle Graphen der Schar punktsymmetrisch zum Ursprung sind",
    verfahren="f_a(−x) bilden und mit −f_a(x) vergleichen",
    schritte="1", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f_a(−x) = (−x) · e^(−a · (−x)²) = −x · e^(−a x²) = −f_a(x) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="das Vorzeichen im Exponenten mit umdrehen und Achsensymmetrie folgern",
    bemerkung="Standardbezug: K1 I, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 1.2: Extremstelle, Graph einer Stammfunktion
STAMM_SKIZZE = ("Koordinatensystem mit x-Achse von −10 bis 10 und y-Achse von −7 bis 4, Gitter; "
                "Graph II (beschriftet oben rechts): W-Form mit Hochpunkt (0; 3), Nullstellen bei etwa "
                "±1,5 und ±4,7, Tiefpunkten bei etwa (±3,5; −6), außerhalb von ±5 steil steigend; "
                "Graph I (beschriftet unten rechts): flache Welle mit Hochpunkt (0; 1), Nullstellen "
                "bei etwa ±2,5, Tiefpunkten bei etwa (±8; −7), an den Rändern wieder steigend")
row("2025MerhoehtAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen", typ_neben="",
    stichwoerter="f'(x) = 3/4 x² − 3|f'(2) = 0|f''(2) ≠ 0 vorgegeben|Extremstelle 2",
    voraussetzungen="Potenzregel|notwendige und hinreichende Bedingung für Extremstellen",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=STAMM_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/4 x³ − 3x, definiert in IR; es gilt f''(2) ≠ 0",
    gesucht="Nachweis, dass 2 eine Extremstelle von f ist",
    verfahren="f' bilden und f'(2) = 0 zeigen; zusammen mit f''(2) ≠ 0 folgt die Extremstelle",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 3/4 x² − 3; f'(2) = 0 (amtlich)",
    zwischenergebnis="f''(2) = 3",
    niveau_geschaetzt="I",
    fehlerquelle="f(2) = −4 berechnen und als Nachweis ansehen",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet; hier ist die hinreichende Bedingung vorgegeben. Die Abbildung gehört zu Teilaufgabe b.")

row("2025MerhoehtAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Graph einer Stammfunktion unter vorgegebenen Graphen begründet auswählen", typ_neben="",
    stichwoerter="Graph II|Extremstelle 2 von f ist Wendestelle von F|Nullstellen von f sind Extremstellen von F|Nullstellen 0 und ±2√3 ≈ ±3,46",
    voraussetzungen="F' = f|Extremstellen von f als Wendestellen von F deuten|Nullstellen einer kubischen Funktion",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=STAMM_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/4 x³ − 3x mit der Extremstelle 2; zwei abgebildete Graphen I und II, einer davon ist der Graph einer Stammfunktion von f",
    gesucht="dieser Graph mit Begründung",
    verfahren="der Graph jeder Stammfunktion F hat an der Extremstelle 2 von f einen Wendepunkt; Graph II wendet bei 2, Graph I nicht (oder: F hat Extremstellen bei den Nullstellen 0 und ±3,46 von f, das passt nur zu Graph II)",
    schritte="2", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="2025MerhoehtAAnalysis12-a",
    ergebnis="Graph II; der Graph jeder Stammfunktion F von f hat im Punkt (2; F(2)) einen Wendepunkt (amtlich)",
    zwischenergebnis="Nullstellen von f: 0, −2√3, 2√3|Tiefpunkte von Graph II bei etwa ±3,5",
    niveau_geschaetzt="II",
    fehlerquelle="den Graphen von f selbst suchen und Graph I wegen des Hochpunkts bei 0 wählen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. Amtlich, eigene Rechnung bestätigt (F(2√3) = −6 passt zu den Tiefpunkten von Graph II). Nahe am Typ „Graph der Funktion vom Graphen der Ableitung unterscheiden“ aus 2026-ga-A, dort zwei Graphen gegeneinander, hier Term von f gegen zwei Kandidaten – Vorschlag für den Abgleich.")

# ---- Analysis 1.3: Kosinus, Integral, Parameter aus zwei Punkten
COS_SKIZZE = ("Koordinatensystem mit x-Achse von −π bis 2π (Markierungen −π, −π/2, 0, π/2, π, 3π/2, 2π) "
              "und y-Achse von −3 bis 3, Gitter; Graph von f(x) = 3 · cos(x): Hochpunkte (0; 3) und "
              "(2π; 3), Tiefpunkte (−π; −3) und (π; −3), Nullstellen bei ±π/2 und 3π/2")
row("2025MerhoehtAAnalysis13", "a", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert aus der Symmetrie des Graphen angeben", typ_neben="",
    stichwoerter="Integral von 0 bis π über 3 cos x|Flächen über und unter der Achse gleich groß|Wert 0",
    voraussetzungen="Integral als orientierten Flächeninhalt deuten|Symmetrie des Kosinus zu π/2",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=COS_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3 · cos(x), definiert in IR, Graph in der Abbildung; Integral von 0 bis π über f(x) dx",
    gesucht="Wert des Integrals",
    verfahren="am Graphen: die Fläche über der x-Achse in [0; π/2] ist so groß wie die darunter in [π/2; π], die orientierten Inhalte heben sich auf",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den Flächeninhalt 6 statt des Integralwerts angeben",
    bemerkung="Standardbezug: K1 I, K4 II. Amtlich, eigene Rechnung bestätigt. Nahe am Typ „Integral mit Wert null am Graphen veranschaulichen“ aus 2026-ea-A (dort Veranschaulichen, hier Wert angeben).")

row("2025MerhoehtAAnalysis13", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Parameter einer Linearkombination aus Funktion und Gerade aus zwei Punkten bestimmen", typ_neben="",
    stichwoerter="g(x) = a · f(x) + b · x|g(0) = −3|g(π/2) = 3π/4|cos(0) = 1, cos(π/2) = 0|a = −1, b = 3/2",
    voraussetzungen="Punkte in den Term einsetzen|Werte des Kosinus an 0 und π/2|Gleichung mit π lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=COS_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 3 · cos(x); g(x) = a · f(x) + b · x mit reellen a und b; die Punkte (0; −3) und (π/2; 3π/4) liegen auf dem Graphen von g",
    gesucht="a und b",
    verfahren="beide Punkte einsetzen: 3a · cos(0) + b · 0 = −3 liefert a; 3a · cos(π/2) + b · π/2 = 3π/4 liefert b",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="3a · cos(0) + b · 0 = −3, also a = −1; 3a · cos(π/2) + b · π/2 = 3π/4, also b = 3/2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="cos(π/2) mit 1 oder cos(0) mit 0 verwechseln",
    bemerkung="Standardbezug: K1 I, K2 I, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 2.1: g = f · e^x, waagerechte Tangente
FEX_SKIZZE = ("Koordinatensystem mit x-Achse von −3 bis 3 und y-Achse von −3 bis 3, Gitter; Graph von f: "
              "von links knapp unter der x-Achse kommend, fallend durch (0; −1), bei x = 1 etwa −1,7, "
              "Tiefpunkt etwa (2; −2,7), dann steil steigend mit Nullstelle bei etwa 2,8 und bis über 3 hinaus")
row("2025MerhoehtAAnalysis21", "a", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Bedingung für eine waagerechte Tangente eines Produkts mit e^x nachweisen", typ_neben="",
    stichwoerter="g(x) = f(x) · e^x|Produktregel|g'(a) = 0|f'(a) · e^a + f(a) · e^a = 0|e^a ≠ 0|f'(a) = −f(a)",
    voraussetzungen="Produktregel mit allgemeiner Funktion f|e^a ≠ 0 ausnutzen|Implikation als Nachweis führen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f und g in IR definiert und differenzierbar mit g(x) = f(x) · e^x; Aussage: hat der Graph von g im Punkt (a; g(a)) eine waagerechte Tangente, dann gilt f'(a) = −f(a)",
    gesucht="Nachweis, dass die Aussage wahr ist",
    verfahren="g' mit der Produktregel bilden, g'(a) = 0 setzen, durch e^a ≠ 0 teilen",
    schritte="3", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="g'(a) = 0 ⇒ f'(a) · e^a + f(a) · e^a = 0 ⇒ f'(a) · e^a = −f(a) · e^a ⇒ f'(a) = −f(a) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="g' = f' · e^x ohne Produktregel ansetzen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 III. Amtlich, eigene Rechnung bestätigt. Nachweis mit allgemeinem f (verallgemeinern), daher III; die Abbildung gehört zu Teilaufgabe b.")

row("2025MerhoehtAAnalysis21", "b", seite="1", punkte="2", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Fehlende waagerechte Tangente über Vorzeichen am Graphen begründen", typ_neben="",
    stichwoerter="f(1) < 0 aus der Abbildung|f'(1) < 0 (fallend)|f'(1) ≠ −f(1)|Aussage aus a",
    voraussetzungen="Funktionswert und Steigungsvorzeichen am Graphen ablesen|Kontraposition der Aussage aus a",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=FEX_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="g(x) = f(x) · e^x; Graph von f in der Abbildung; nach Teilaufgabe a folgt aus einer waagerechten Tangente von g an der Stelle a die Gleichung f'(a) = −f(a)",
    gesucht="Nachweis mithilfe der Abbildung, dass der Graph von g im Punkt (1; g(1)) keine waagerechte Tangente hat",
    verfahren="am Graphen: f(1) < 0 und f'(1) < 0, also −f(1) > 0 > f'(1); die Bedingung aus a ist verletzt",
    schritte="2", zahlenraum="negativ", einheiten="", abhaengig_von="2025MerhoehtAAnalysis21-a",
    ergebnis="der Abbildung ist zu entnehmen, dass f(1) < 0 und f'(1) < 0 gilt; mit der Aussage aus a ist die Behauptung gezeigt (amtlich)",
    zwischenergebnis="f(1) ≈ −1,7",
    niveau_geschaetzt="III",
    fehlerquelle="nur f'(1) ≠ 0 ablesen und daraus auf g'(1) ≠ 0 schließen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 II. Amtlich. Werte nur aus der Abbildung.")

# ---- Analysis 2.2: Umkehrfunktion und Flächen (ungegliedert)
UMK_SKIZZE = ("Koordinatensystem im ersten Quadranten ohne Skalen, Ursprung mit 0 beschriftet; zwei "
              "Kurven vom Ursprung aus: G_g (oben, beschriftet) rechtsgekrümmt wie eine Wurzelfunktion, "
              "G_f (unten, beschriftet) linksgekrümmt; beide schneiden sich außer im Ursprung in einem "
              "Punkt rechts oben, danach liegt G_f oberhalb")
row("2025MerhoehtAAnalysis22", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Umkehrfunktion",
    typ="Flächenbeziehung zwischen Funktion und Umkehrfunktion über die Spiegelung an y = x beurteilen", typ_neben="",
    stichwoerter="Integral über g − f von 0 bis x_S|Fläche zwischen G_f und G_g|Integral über x − f(x)|Fläche zwischen y = x und G_f|Spiegelung an y = x|doppelter Inhalt|Aussage wahr",
    voraussetzungen="Integral einer Differenz als Fläche zwischen Graphen deuten|Graph der Umkehrfunktion als Spiegelbild an y = x|Symmetrie einer Fläche ausnutzen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=UMK_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f und g definiert in IR_0^+, g ist die Umkehrfunktion von f; Graphen G_f und G_g in der Abbildung schneiden sich nur im Ursprung und im Punkt (x_S; f(x_S)); Aussage: Integral von 0 bis x_S über (g(x) − f(x)) dx = 2 · Integral von 0 bis x_S über (x − f(x)) dx",
    gesucht="Beurteilung der Aussage",
    verfahren="linkes Integral als Inhalt der von G_f und G_g eingeschlossenen Fläche deuten, rechtes als Inhalt der Fläche zwischen der Geraden y = x und G_f; G_g ist das Spiegelbild von G_f an y = x, die Gerade halbiert die Fläche",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Aussage ist wahr: das linke Integral ist der Inhalt der von G_f und G_g eingeschlossenen Fläche, das rechte der Inhalt der von y = x und G_f eingeschlossenen Fläche; weil G_g durch Spiegelung von G_f an y = x entsteht, ist der erste Inhalt doppelt so groß wie der zweite (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Gerade y = x nicht als Symmetrieachse erkennen und die Aussage für falsch halten",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 III. Amtlich. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Erste Fundstelle des Themas Umkehrfunktion.")

# ---- Analysis 2.3: Wurzelfunktion, Tangente einzeichnen, Sekantensteigungen
WURZ_SKIZZE = ("Koordinatensystem mit x-Achse von 0 bis etwa 9 (Markierungen 2, 4, 6, 8) und y-Achse von 0 "
               "bis 4 (Markierungen 2, 4), Gitter mit Schrittweite 1; Graph G von f(x) = √(x − 2): beginnt "
               "in (2; 0), verläuft durch P(3; 1) (markiert und beschriftet) und (6; 2), flach steigend bis "
               "etwa (9; 2,6); G beschriftet")
row("2025MerhoehtAAnalysis23", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente mit gegebener Gleichung in die Abbildung einzeichnen", typ_neben="",
    stichwoerter="y = 1/2 x − 1/2|durch (1; 0) und P(3; 1)|Gerade zeichnen",
    voraussetzungen="Gerade aus der Gleichung über zwei Punkte zeichnen",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=WURZ_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = √(x − 2) für x ≥ 2, Graph G und Punkt P(3; 1) in der Abbildung; die Gerade y = 1/2 x − 1/2 ist die Tangente an G in P und hat mit G nur P gemeinsam",
    gesucht="die Tangente in der Abbildung",
    verfahren="zwei Punkte der Geraden bestimmen, etwa (1; 0) und (3; 1), und die Gerade durchziehen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Gerade durch (1; 0) und P(3; 1), Steigung 1/2, berührt G in P und verläuft rechts von P oberhalb von G (amtlich)",
    zwischenergebnis="weiterer Punkt (5; 2)",
    niveau_geschaetzt="I",
    fehlerquelle="die Gerade durch den Ursprung zeichnen",
    bemerkung="Standardbezug: K4 I. Amtlich; der Erwartungshorizont zeigt die Abbildung mit eingezeichneter Tangente. Das Feld skizze beschreibt das Material, die Lösung ist eine Zeichnung.")

row("2025MerhoehtAAnalysis23", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Steigungen aller Sekanten durch einen Punkt des Graphen angeben", typ_neben="",
    stichwoerter="Geraden durch P und einen weiteren Punkt von G|Sekante durch (2; 0) hat Steigung 1|Steigungen nähern sich der Tangentensteigung 1/2|rechts von P Steigungen zwischen 0 und 1/2|1/2 < m ≤ 1 oder 0 < m < 1/2",
    voraussetzungen="Sekantensteigung als Differenzenquotient|Tangente als Grenzlage der Sekanten|Verhalten des Graphen am Rand und im Unendlichen deuten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Koordinatensystem", skizze=WURZ_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = √(x − 2) für x ≥ 2, Graph G, P(3; 1); die Tangente in P hat die Steigung 1/2 und mit G nur P gemeinsam; betrachtet werden alle Geraden, die mit G sowohl P als auch einen weiteren Punkt gemeinsam haben",
    gesucht="Steigungen dieser Geraden",
    verfahren="links von P: Sekantensteigung von 1 (durch (2; 0)) fallend gegen 1/2; rechts von P: von 1/2 fallend gegen 0, weil G rechtsgekrümmt ist und flacher wird; die Tangentensteigung selbst kommt nicht vor",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2025MerhoehtAAnalysis23-a",
    ergebnis="m ist genau dann Steigung einer solchen Geraden, wenn 1/2 < m ≤ 1 oder 0 < m < 1/2 gilt (amtlich)",
    zwischenergebnis="Sekantensteigung (√(x − 2) − 1)/(x − 3) = 1/(√(x − 2) + 1)",
    niveau_geschaetzt="III",
    fehlerquelle="1/2 einschließen oder die Steigung 1 der Sekante durch (2; 0) übersehen",
    bemerkung="Standardbezug: K1 II, K2 III, K4 III. Amtlich, eigene Rechnung bestätigt (Sekantensteigung streng monoton fallend von 1 gegen 0).")

# ---- AG/LA (A1) 1: Vektor mit Parameter und Matrix (Gruppe 1, Aufgabe „1“)
row("2025MerhoehtAAGLAA11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Koordinate eines Vektors aus vorgegebener Länge bestimmen", typ_neben="",
    stichwoerter="|v| = 10|√(6² + a²) = 10|a² = 64|a = 8 wegen a > 0",
    voraussetzungen="Betrag eines Vektors|Wurzelgleichung lösen|Vorzeichenbedingung beachten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="v = (6; a) mit a > 0",
    gesucht="Wert von a, sodass |v| = 10",
    verfahren="Betragsgleichung √(36 + a²) = 10 quadrieren und a > 0 wählen",
    schritte="2", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="√(6² + a²) = 10 ⇒ a = 8 (amtlich)",
    zwischenergebnis="a² = 64",
    niveau_geschaetzt="I",
    fehlerquelle="6 + a = 10 ansetzen und a = 4 erhalten",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt. Vektoren mit zwei Koordinaten; einzige Aufgabe der Gruppe 1 (aufgabe „1“), Kurzbeschreibung „AG/LA (A1)“.")

row("2025MerhoehtAAGLAA11", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Parameter einer Matrix aus der Orthogonalität von v und M · v bestimmen", typ_neben="",
    stichwoerter="M = ((0; b), (2; 0))|v = (6; 5)|M · v = (5b; 12)|v · (M · v) = 30b + 60 = 0|b = −2",
    voraussetzungen="Matrix-Vektor-Produkt|Orthogonalität als Skalarprodukt null|lineare Gleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="v = (6; a) mit a = 5; M = ((0; b), (2; 0)) mit reellem b",
    gesucht="Wert von b, sodass v und M · v orthogonal sind",
    verfahren="M · v berechnen, Skalarprodukt mit v gleich 0 setzen und nach b auflösen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="M · v = (5b; 12); v · (M · v) = 0 ⇔ 30b + 60 = 0 ⇔ b = −2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Zeilen und Spalten der Matrix beim Produkt vertauschen (M · v = (12; 5b))",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand in BE und BB); die Verkettung ist Routine, daher II.")

# ---- AG/LA (A1) 2.1: gestaffeltes LGS mit Parameter (Dublette 2025MerhoehtAAGLAA224)
row("2025MerhoehtAAGLAA121", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Gestaffeltes Gleichungssystem für einen Parameterwert lösen", typ_neben="",
    stichwoerter="a = 0|III: 4z = 2|z = 1/2|II: −y + 2 = 2, y = 0|I: x = 0",
    voraussetzungen="Parameterwert einsetzen|Rückwärtseinsetzen in Dreiecksform",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="lineares Gleichungssystem mit Parameter a: I x + 2y = a, II −y + 4z = 2, III (4 − a²) · z = 2 + a",
    gesucht="Lösung für a = 0",
    verfahren="a = 0 einsetzen, aus III z, aus II y, aus I x",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="4z = 2 ⇒ z = 1/2 ⇒ y = 0 ⇒ x = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="in II das Vorzeichen von y übersehen und y = 4 erhalten",
    bemerkung="Standardbezug: K1 I, K5 II. Amtlich, eigene Rechnung bestätigt. Die Datei liegt wortgleich als 2025MerhoehtAAGLAA224 ein zweites Mal vor (Dublette ohne Zeile).")

row("2025MerhoehtAAGLAA121", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lösungsanzahl eines gestaffelten Gleichungssystems mit Parameter durch Fallunterscheidung begründen", typ_neben="",
    stichwoerter="y = 4z − 2 und x = −8z + 4 + a eindeutig aus z|III: (2 + a)(2 − a) · z = 2 + a|a = 2: 0 = 4, keine Lösung|a = −2: 0 = 0, unendlich viele Lösungen",
    voraussetzungen="dritte binomische Formel|Fallunterscheidung beim Koeffizienten null|Lösungsanzahl auf eine Gleichung zurückführen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="I x + 2y = a, II −y + 4z = 2, III (4 − a²) · z = 2 + a; Aussage: es gibt einen Wert von a ohne Lösung und einen Wert von a mit unendlich vielen Lösungen",
    gesucht="Begründung der Aussage",
    verfahren="aus II und I folgen y und x eindeutig aus z, die Lösungsanzahl entspricht der von III; 4 − a² faktorisieren: für a = 2 wird III zu 0 = 4, für a = −2 zu 0 = 0",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="wegen y = 4z − 2 (aus II) und x = −8z + 4 + a (aus I) entspricht die Anzahl der Lösungen der Anzahl der Lösungen von III für z; III lautet (2 + a) · (2 − a) · z = 2 + a; für a = 2 keine Lösung, für a = −2 unendlich viele (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="III durch 4 − a² teilen, ohne den Fall a = ±2 zu unterscheiden",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt. Vom Typ „Lösbarkeit eines Gleichungssystems mit Parameter beurteilen“ (2025-ga-A) getrennt: dort Erkennen einer abhängigen Gleichung, hier Fallunterscheidung am Koeffizienten.")

# ---- AG/LA (A1) 2.2: Matrizenprodukt, Vertauschbarkeit (ungegliedert)
row("2025MerhoehtAAGLAA122", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Bedingungen für die Vertauschbarkeit zweier Matrizen aus einer binomischen Gleichung untersuchen", typ_neben="",
    stichwoerter="(X + A)² = X² + X · A + A · X + A²|Gleichung gilt genau dann, wenn X · A = A · X|X · A = ((0; a), (0; c))|A · X = ((c; d), (0; 0))|a = d und c = 0",
    voraussetzungen="Matrizenprodukt ist nicht kommutativ|Produkt zweier 2×2-Matrizen mit Variablen|Koeffizientenvergleich",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="A = ((0; 1), (0; 0)) und X = ((a; b), (c; d)) mit reellen a, b, c, d; Gleichung (X + A) · (X + A) = X² + 2 · A · X + A²",
    gesucht="Bedingungen an a, b, c, d, unter denen die Gleichung gilt",
    verfahren="(X + A)² ausmultiplizieren, ohne die Reihenfolge zu vertauschen; die Gleichung reduziert sich auf X · A = A · X; beide Produkte berechnen und vergleichen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="wegen (X + A) · (X + A) = X² + X · A + A · X + A² gilt die Gleichung genau dann, wenn X · A = A · X; mit X · A = ((0; a), (0; c)) und A · X = ((c; d), (0; 0)) folgt: genau dann, wenn a = d und c = 0 (amtlich)",
    zwischenergebnis="b bleibt frei",
    niveau_geschaetzt="III",
    fehlerquelle="die binomische Formel für Matrizen als allgemeingültig ansehen und keine Bedingung finden",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand in BE und BB).")

# ---- AG/LA (A2) 1.1: Skalarprodukt-Ausdrücke, Winkel mindestens 90°
row("2025MerhoehtAAGLAA211", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Art des Ergebnisses von Ausdrücken mit Skalarprodukt ankreuzen", typ_neben="",
    stichwoerter="a ∘ (a + b): Skalarprodukt zweier Vektoren, Zahl|a + (a ∘ b): Vektor plus Zahl, nicht definiert|Ankreuztabelle Vektor/Zahl/nicht definiert",
    voraussetzungen="Skalarprodukt liefert eine Zahl|Vektoraddition nur zwischen Vektoren",
    format="Ankreuzen", operator="Entscheiden Sie", antwort="Kreuz",
    material="Tabelle", skizze="Tabelle mit zwei Zeilen (a ∘ (a + b) und a + (a ∘ b)) und drei Spalten mit Kästchen: Vektor mit drei Koordinaten, Zahl, nicht definiert",
    kontext="ohne", textumfang="kurz",
    gegeben="zwei Vektoren a und b mit jeweils drei Koordinaten; Ausdrücke a ∘ (a + b) und a + (a ∘ b)",
    gesucht="je Ausdruck: Vektor mit drei Koordinaten, Zahl oder nicht definiert",
    verfahren="Rechenarten von innen nach außen prüfen: Summe zweier Vektoren ist ein Vektor, Skalarprodukt eine Zahl; Vektor plus Zahl ist nicht erklärt",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="a ∘ (a + b): Zahl|a + (a ∘ b): nicht definiert (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="a + (a ∘ b) als Vektor ankreuzen, weil a ein Vektor ist",
    bemerkung="Standardbezug: K1 II, K4 I, K5 II. Amtlich. Aussagenliste: stichwoerter nennt beide Ausdrücke, ergebnis die Bewertung je Ausdruck.")

row("2025MerhoehtAAGLAA211", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Parameter für einen Winkel von mindestens 90° über das Skalarprodukt ermitteln", typ_neben="",
    stichwoerter="u = (2; 3; 0), v_r = (r; 4; 2)|u ∘ v_r = 2r + 12|Winkel ≥ 90° genau dann, wenn Skalarprodukt ≤ 0|r ≤ −6",
    voraussetzungen="Skalarprodukt mit Parameter|Vorzeichen des Skalarprodukts als Winkelmaß deuten|lineare Ungleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="u = (2; 3; 0) und v_r = (r; 4; 2) mit reellem r; Winkel zwischen u und v_r",
    gesucht="alle Werte von r, für die der Winkel mindestens 90° groß ist",
    verfahren="Skalarprodukt bilden; der Winkel ist genau dann mindestens 90°, wenn das Skalarprodukt kleiner oder gleich 0 ist",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="u ∘ v_r = 2 · r + 12; der Winkel hat genau dann eine Größe von mindestens 90°, wenn u ∘ v_r ≤ 0, d. h. r ≤ −6 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur r = −6 (genau 90°) angeben oder das Ungleichheitszeichen umdrehen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 1.2: Würfel, Ebene K, Schnittfigur und Schnittgerade (Datei mit drei Seiten)
WUERFEL_SKIZZE = ("Schrägbild eines Würfels ABCDEFGH der Kantenlänge 4 im Koordinatensystem: A im Ursprung, "
                  "B(4; 0; 0) auf der x-Achse (nach vorn links), D(0; 4; 0) auf der y-Achse (nach rechts), "
                  "E(0; 0; 4) auf der z-Achse, C(4; 4; 0), F(4; 0; 4), G(4; 4; 4), H(0; 4; 4); Ebene K als "
                  "graues Viereck durch A, B und die Mittelpunkte (4; 2; 4) von FG und (0; 2; 4) von EH; "
                  "verdeckte Kanten gestrichelt, Achsen x, y, z beschriftet")
row("2025MerhoehtAAGLAA212", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Volumen eines Teilkörpers eines Würfels berechnen", typ_neben="",
    stichwoerter="Ebene K durch A, B und Mittelpunkt von FG|Teilkörper ist ein Dreiecksprisma|Grundfläche 1/2 · 2 · 4 = 4, Länge 4|Viertel des Würfels|Volumen 16",
    voraussetzungen="Schnittkörper im Schrägbild erkennen|Prismenvolumen|Mittelpunkt einer Kante",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=WUERFEL_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Würfel ABCDEFGH der Kantenlänge 4, drei Seitenflächen in den Koordinatenebenen; A(0; 0; 0), B(4; 0; 0); Ebene K enthält A, B und den Mittelpunkt der Kante FG; K teilt den Würfel in zwei Teilkörper",
    gesucht="Volumen des kleineren Teilkörpers",
    verfahren="der kleinere Teilkörper ist ein Prisma mit dreieckiger Grundfläche (Dreieck A, E, Mittelpunkt von EH in der Ebene x = 0) und Länge 4; Grundfläche 1/2 · 2 · 4 = 4",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Volumen 1/4 · 4³ = 16 (amtlich)",
    zwischenergebnis="Mittelpunkt von FG: (4; 2; 4)|K: z = 2y",
    niveau_geschaetzt="I",
    fehlerquelle="den Teilkörper als halben Würfel (32) ansehen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Datei mit drei Seiten.")

row("2025MerhoehtAAGLAA212", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schnittfigur einer Ebene mit einem Würfel einzeichnen",
    typ_neben="Schnittgerade zweier Ebenen aus dem Schrägbild angeben",
    stichwoerter="Ebene L durch E, F und Mittelpunkt (4; 2; 0) von BC|Schnittfigur Rechteck E, F, (4; 2; 0), (0; 2; 0)|K und L enthalten Geraden parallel zur x-Achse|Schnittgerade durch (0; 1; 2) mit Richtung (1; 0; 0)",
    voraussetzungen="Schnittfigur über parallele Schnittkanten konstruieren|Schnittgerade zweier Ebenen aus zwei gemeinsamen Punkten oder aus Symmetrie|Geradengleichung in Parameterform",
    format="Zeichnen|Kurzantwort", operator="Zeichnen Sie|Geben Sie an", antwort="Grafik|Term",
    material="Körper", skizze=WUERFEL_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Würfel ABCDEFGH der Kantenlänge 4 wie in der Abbildung, Ebene K durch A, B und den Mittelpunkt von FG; Ebene L enthält E(0; 0; 4), F(4; 0; 4) und den Mittelpunkt (4; 2; 0) der Kante BC",
    gesucht="Schnittfigur von L mit dem Würfel in der Abbildung|Gleichung der Schnittgeraden von K und L",
    verfahren="L schneidet die Flächen x = 4 und x = 0 in parallelen Strecken von F bzw. E zu den Kantenmitten (4; 2; 0) bzw. (0; 2; 0), die Schnittfigur ist ein Rechteck; beide Ebenen enthalten Geraden in x-Richtung, die Schnittgerade verläuft durch den Schnittpunkt (0; 1; 2) der Schnittstrecken in der Ebene x = 0",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2025MerhoehtAAGLAA212-a",
    ergebnis="Schnittfigur: Rechteck mit den Ecken E, F, (4; 2; 0) und (0; 2; 0); Schnittgerade x = (0; 1; 2) + t · (1; 0; 0), t reell (amtlich)",
    zwischenergebnis="K: z = 2y|L: 2y + z = 4",
    niveau_geschaetzt="II",
    fehlerquelle="die Schnittfigur an den Ecken B und C enden lassen statt an den Kantenmitten",
    bemerkung="Standardbezug: K2 II, K4 II. Amtlich, eigene Rechnung bestätigt (Punkt und Richtung in beiden Ebenen). Der Erwartungshorizont zeigt die Abbildung mit beiden Schnittfiguren. Das Feld skizze beschreibt das Material, der erste Teil der Lösung ist eine Zeichnung.")

# ---- AG/LA (A2) 2.1: Geradenschar, Ursprung, Identität
row("2025MerhoehtAAGLAA221", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Punktprobe an einer Geraden durchführen", typ_neben="",
    stichwoerter="g_k: x = (5 − 6k; 3k; 4 − 9k) + r · (2; −1; 3)|Ansatz (0; 0; 0)|zweite Koordinate r = 3k|erste Koordinate 0 = 5|Widerspruch für jedes k",
    voraussetzungen="Parameteransatz koordinatenweise|Scharparameter mitführen|Widerspruch erkennen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Geradenschar g_k: x = (5 − 6k; 3k; 4 − 9k) + r · (2; −1; 3), r reell, für jede reelle Zahl k",
    gesucht="Nachweis, dass der Ursprung für keinen Wert von k auf g_k liegt",
    verfahren="Ursprung gleichsetzen; aus der zweiten Koordinate r = 3k, in die erste eingesetzt 0 = 5",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="aus 0 = 3k − r folgt r = 3k; eingesetzt in 0 = 5 − 6k + 2r führt das zur falschen Aussage 0 = 5 (amtlich)",
    zwischenergebnis="dritte Koordinate: 4 − 9k + 9k = 4 ≠ 0 ebenfalls Widerspruch",
    niveau_geschaetzt="II",
    fehlerquelle="k und r als denselben Parameter behandeln",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2025-ga-A wiederverwendet (gleicher Lösungsweg, hier mit Scharparameter); Thema Scharen von Geraden und Ebenen (nicht für das grundlegende Niveau in BE und BB).")

row("2025MerhoehtAAGLAA221", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Identität aller Geraden einer Schar beurteilen", typ_neben="",
    stichwoerter="Stützvektor (5 − 6k; 3k; 4 − 9k) = (5; 0; 4) − 3k · (2; −1; 3)|Stützpunkt liegt auf der Geraden zu k = 0|gleicher Richtungsvektor|Aussage wahr",
    voraussetzungen="Stützvektor als Punkt plus Vielfaches des Richtungsvektors zerlegen|Identität von Geraden über gemeinsamen Punkt und Richtung",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g_k: x = (5 − 6k; 3k; 4 − 9k) + r · (2; −1; 3), r reell; Aussage: alle Geraden g_k sind identisch",
    gesucht="Beurteilung der Aussage",
    verfahren="den Stützvektor als (5; 0; 4) − 3k · (2; −1; 3) schreiben; damit hat jede g_k die Darstellung (5; 0; 4) + r' · (2; −1; 3) mit r' = r − 3k",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="der Vektor (5 − 6k; 3k; 4 − 9k) lässt sich als (5; 0; 4) − 3k · (2; −1; 3) schreiben; jede g_k wird durch x = (5; 0; 4) + r' · (2; −1; 3) mit r' = r − 3k beschrieben, die Aussage ist wahr (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="wegen verschiedener Stützvektoren auf verschiedene, parallele Geraden schließen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 2.2: Ebenenschar, senkrechte Koordinatenebene, keine Parallelität
row("2025MerhoehtAAGLAA222", "a", seite="1", punkte="1", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Koordinatenebene senkrecht zu allen Ebenen einer Schar angeben", typ_neben="",
    stichwoerter="E_k: kx + (2 − k) · y = k|kein z in der Gleichung|Normalenvektor (k; 2 − k; 0)|alle E_k parallel zur z-Achse|senkrecht zur xy-Ebene",
    voraussetzungen="fehlende Koordinate in der Ebenengleichung als Parallelität zur Achse deuten|Normalenvektor ablesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar der Ebenen E_k: k · x + (2 − k) · y = k mit reellem k",
    gesucht="die Koordinatenebene, zu der alle Ebenen der Schar senkrecht stehen",
    verfahren="der Normalenvektor (k; 2 − k; 0) liegt für jedes k in der xy-Ebene, also stehen alle E_k senkrecht auf der xy-Ebene",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="xy-Ebene (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die xz- oder yz-Ebene nennen, weil z in der Gleichung fehlt",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtAAGLAA222", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Nichtparallelität verschiedener Ebenen einer Schar über die Normalenvektoren nachweisen", typ_neben="",
    stichwoerter="E_a und E_b mit a ≠ b|Normalenvektoren (a; 2 − a; 0) und (b; 2 − b; 0)|Ansatz (a; 2 − a; 0) = r · (b; 2 − b; 0)|a = rb und 2 − a = 2r − rb|r = 1, also a = b|Widerspruch",
    voraussetzungen="Parallelität von Ebenen über kollineare Normalenvektoren|Gleichungssystem mit zwei Scharparametern lösen|Widerspruch zur Voraussetzung a ≠ b",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar E_k: k · x + (2 − k) · y = k, k reell",
    gesucht="Nachweis, dass je zwei verschiedene Ebenen der Schar nicht parallel sind",
    verfahren="zwei Ebenen E_a und E_b mit a ≠ b betrachten und annehmen, die Normalenvektoren seien Vielfache voneinander; aus den beiden Koordinatengleichungen folgt r = 1 und damit a = b",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2025MerhoehtAAGLAA222-a",
    ergebnis="für E_a und E_b mit a ≠ b liefert (a; 2 − a; 0) = r · (b; 2 − b; 0) die Gleichungen a = rb und 2 − a = 2r − rb, also 2 − a = 2r − a und r = 1; das ist wegen a ≠ b nicht möglich (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur zwei konkrete Werte von k prüfen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt. Allgemeiner Nachweis mit zwei Parametern (verallgemeinern).")

# ---- AG/LA (A2) 2.3: Pyramidenstumpf, Symmetrieebene, Vektorterm für F
STUMPF_SKIZZE = ("Schrägbild eines Pyramidenstumpfs im Koordinatensystem: unteres kleineres Rechteck ABCD grau "
                 "mit A im Ursprung, B(4; 0; 0) auf der x-Achse (nach vorn links), C(4; 6; 0), D(0; 6; 0) auf "
                 "der y-Achse (nach rechts); oberes größeres Rechteck EFGH (E hinten links, F vorn links, G vorn "
                 "rechts, H hinten rechts) in der Höhe 5, hellgrau; Seitenkanten laufen nach unten gestrichelt "
                 "in einer Pyramidenspitze unterhalb von ABCD zusammen; z-Achse nach oben")
row("2025MerhoehtAAGLAA223", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebenen eines Körpers aus den Koordinaten begründen", typ_neben="",
    stichwoerter="gerade Pyramide, rechteckige Grundflächen|Symmetrieebenen durch die Mittelparallelen|x = 2 oder y = 3",
    voraussetzungen="Symmetrie eines geraden Pyramidenstumpfs|Koordinatengleichung einer achsenparallelen Ebene",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Körper", skizze=STUMPF_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Körper ABCDEFGH ist Teil einer geraden Pyramide mit rechteckiger Grundfläche EFGH; ABCD und EFGH liegen in parallelen Ebenen mit Abstand 5; A(0; 0; 0), B(4; 0; 0), C(4; 6; 0), D(0; 6; 0)",
    gesucht="Gleichung einer der beiden Symmetrieebenen des Körpers",
    verfahren="die Symmetrieebenen stehen senkrecht auf den Rechtecken durch deren Mittellinien: x = 2 (Mitte von AB) oder y = 3 (Mitte von AD)",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="x = 2 (amtlich), ebenso möglich y = 3",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="eine Diagonalebene angeben, die beim Rechteck keine Symmetrieebene ist",
    bemerkung="Standardbezug: K4 I, K5 I. Amtlich. Typ aus 2026-ea-A wiederverwendet (dort mit Begründung, hier nur Angabe).")

row("2025MerhoehtAAGLAA223", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Vektorterm für einen Eckpunkt eines Pyramidenstumpfs begründen", typ_neben="",
    stichwoerter="Term (2; 3; 5) + 2 · ((4; 0; 0) − (2; 3; 0))|M(2; 3; 0) Mittelpunkt von ABCD|M*(2; 3; 5) Mittelpunkt von EFGH|vierfacher Flächeninhalt heißt doppelte Seitenlängen und Diagonalen|AF = AM* + 2 · MB",
    voraussetzungen="Mittelpunkt eines Rechtecks|Ähnlichkeit: Flächenfaktor 4 heißt Längenfaktor 2|Ortsvektor als Vektorkette",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=STUMPF_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Pyramidenstumpf wie in a; Flächeninhalt von EFGH ist viermal so groß wie der von ABCD; Abstand der Rechteckebenen 5; A(0; 0; 0), B(4; 0; 0), C(4; 6; 0), D(0; 6; 0); Term (2; 3; 5) + 2 · ((4; 0; 0) − (2; 3; 0))",
    gesucht="Begründung, dass der Term die Koordinaten von F liefert",
    verfahren="(2; 3; 0) ist der Mittelpunkt M von ABCD, (2; 3; 5) der Mittelpunkt M* von EFGH (gerade Pyramide, Abstand 5); EFGH ist zu ABCD ähnlich mit vierfachem Inhalt, also doppelt so langen Diagonalen; F liegt über B im Sinne der Streckung, daher AF = AM* + 2 · MB",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Mittelpunkt von ABCD: M(2; 3; 0); Mittelpunkt von EFGH: M*(2; 3; 5); da EFGH zu ABCD ähnlich ist und den vierfachen Flächeninhalt besitzt, haben die Diagonalen von EFGH die doppelte Länge; folglich gilt AF = AM* + 2 · MB (amtlich)",
    zwischenergebnis="F(6; −3; 5)",
    niveau_geschaetzt="III",
    fehlerquelle="Flächenfaktor 4 als Längenfaktor 4 ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt (F(6; −3; 5), Rechteck EFGH 8 × 12).")

# ---- Stochastik 1.1: Würfelspiel, Auszahlung
row("2025MerhoehtAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für zweimal kein Treffer über die Pfadregel begründen", typ_neben="",
    stichwoerter="Würfel zweimal|keine 3|5/6 je Wurf|(5/6)² = 25/36",
    voraussetzungen="Gegenwahrscheinlichkeit beim Würfel|Pfadregel für unabhängige Würfe",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Würfelspiel", textumfang="kurz",
    gegeben="Spiel: ein Würfel mit den Zahlen 1 bis 6 wird zweimal geworfen",
    gesucht="Begründung, dass die Wahrscheinlichkeit für keine 3 bei beiden Würfen 25/36 beträgt",
    verfahren="Wahrscheinlichkeit 5/6 für keine 3 bei einem Wurf, Pfadregel für beide Würfe",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="die Wahrscheinlichkeit, bei einem Wurf nicht die 3 zu erzielen, beträgt 5/6; (5/6)² = 25/36 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="5/6 + 5/6 oder 1 − 1/36 rechnen",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtAStochastik11", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Werte einer Zufallsgröße aus dem Erwartungswert bestimmen", typ_neben="",
    stichwoerter="Einsatz 2 €|Auszahlung 0, 5, x je nach Anzahl der Dreien|P(genau eine 3) = 10/36, P(zwei Dreien) = 1/36|Ausgleich auf lange Sicht heißt Erwartungswert gleich Einsatz|x = 22",
    voraussetzungen="Wahrscheinlichkeiten für 0, 1, 2 Dreien über Pfade|faires Spiel als Erwartungswert gleich Einsatz deuten|lineare Gleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle mit zwei Zeilen: Anzahl der Würfe mit der Zahl 3 (0, 1, 2) und Auszahlung in Euro (0, 5, x)", kontext="Würfelspiel", textumfang="mittel",
    gegeben="Würfel zweimal geworfen; Einsatz 2 €; Auszahlung 0 € bei keiner 3, 5 € bei genau einer 3, x € bei zwei Dreien; auf lange Sicht gleichen sich Einsätze und Auszahlungen aus",
    gesucht="Wert von x",
    verfahren="Erwartungswert der Auszahlung 1/36 · x + 10/36 · 5 gleich 2 setzen",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="€", abhaengig_von="2025MerhoehtAStochastik11-a",
    ergebnis="1/36 · x + 10/36 · 5 = 2 ⇔ x = 22 (amtlich)",
    zwischenergebnis="P(genau eine 3) = 2 · 1/6 · 5/6 = 10/36",
    niveau_geschaetzt="III",
    fehlerquelle="P(genau eine 3) = 5/36 ansetzen (nur eine Reihenfolge)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ea-A wiederverwendet. Nach der engen Fassung III (faires Spiel als Erwartungswert gleich Einsatz deuten), amtlich II – Messwert zur Regel.")

# ---- Stochastik 1.2: zwei Binomialverteilungen im Diagramm
BIN12_SKIZZE = ("Abb. 1: Säulendiagramm P(X1 = k) für k von 0 bis 30 (Achse in Zweierschritten beschriftet), "
                "y-Achse mit 0 und 0,1; Säulen ab etwa k = 5 sichtbar, höchste Säule bei k = 14 knapp über 0,1, "
                "symmetrischer Abfall, ab etwa k = 24 nicht mehr sichtbar. Abb. 2: Säulendiagramm P(X2 = k) für k "
                "von 0 bis 82 mit Achsenunterbrechung zwischen 4 und 36, y-Achse mit 0 und 0,1; Säulen ab etwa "
                "k = 44 sichtbar, höchste Säule bei k = 56 etwa 0,08, bis etwa k = 68 sichtbar")
row("2025MerhoehtAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussage über eine Summe von Wahrscheinlichkeiten am Säulendiagramm entscheiden", typ_neben="",
    stichwoerter="Summe P(X1 = k) für k = 16 bis 20|fünf Säulen|jede kleiner als 0,1|Summe kleiner als 0,5|Aussage falsch",
    voraussetzungen="Summenzeichen als Addition von Einzelwahrscheinlichkeiten lesen|Säulenhöhen mit einer Schranke vergleichen",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Diagramm", skizze=BIN12_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="binomialverteilte Zufallsgröße X1 mit Parametern n1 und p1, Wahrscheinlichkeitsverteilung in Abbildung 1; Aussage: Summe von k = 16 bis 20 über P(X1 = k) > 0,5",
    gesucht="Entscheidung, ob die Aussage richtig ist, mit Begründung",
    verfahren="die fünf Säulen von 16 bis 20 sind alle niedriger als 0,1, ihre Summe ist also kleiner als 5 · 0,1",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="die Aussage ist falsch; der Abbildung 1 ist zu entnehmen, dass jeder der fünf zu betrachtenden Werte kleiner als 0,1 ist (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Summe von 16 bis 20 mit P(X1 ≥ 16) verwechseln und über das Diagramm hinaus argumentieren",
    bemerkung="Standardbezug: K1 I, K4 II, K5 I, K6 I. Amtlich. Werte nur aus der Abbildung.")

row("2025MerhoehtAStochastik12", "b", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Verhältnis zweier Trefferwahrscheinlichkeiten aus den Erwartungswerten im Diagramm nachweisen", typ_neben="",
    stichwoerter="Erwartungswerte ganzzahlig, also an der höchsten Säule|E(X1) = 14, E(X2) = 56|n1 · p1 = 14, n2 · p2 = 56|n1 = n2|p2 = 4 · p1",
    voraussetzungen="ganzzahliger Erwartungswert liegt an der höchsten Säule|Erwartungswert n · p|Gleichungen dividieren",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Diagramm", skizze=BIN12_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="X1 und X2 binomialverteilt mit Parametern n1, p1 bzw. n2, p2, Verteilungen in den Abbildungen 1 und 2; Erwartungswerte ganzzahlig; n1 = n2",
    gesucht="Nachweis mithilfe der Abbildungen, dass p2 = 4 · p1 gilt",
    verfahren="Erwartungswerte als Lage der höchsten Säule ablesen (14 und 56), als n · p schreiben und wegen n1 = n2 dividieren",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="mithilfe der Abbildungen erhält man 14 = n1 · p1 und 56 = n2 · p2; mit n2 · p2 = 4 · 14 = 4 · n1 · p1 und n1 = n2 folgt die Behauptung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Säulenhöhen statt der Lage der Maxima vergleichen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2. Nahe am Typ „Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln“ aus 2026-ga-A – Vorschlag für den Abgleich.")

# ---- Stochastik 2.1: n und p aus Verhältnis und Erwartungswert (ungegliedert)
row("2025MerhoehtAStochastik21", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Parameter n und p aus einem Verhältnis zweier Einzelwahrscheinlichkeiten und dem Erwartungswert berechnen", typ_neben="",
    stichwoerter="P(X = 1) = 14 · P(X = 0)|n · p · (1 − p)^(n − 1) = 14 · (1 − p)^n|kürzen durch (1 − p)^(n − 1)|n · p = 10 einsetzen|10 = 14 · (1 − p), p = 2/7|n = 35",
    voraussetzungen="Bernoulli-Formel für k = 0 und k = 1|Potenzen kürzen|Erwartungswert n · p als Ersatz einsetzen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X binomialverteilt mit n und p, p < 1; P(X = 1) ist vierzehnmal so groß wie P(X = 0); E(X) = 10",
    gesucht="Werte von p und n",
    verfahren="beide Wahrscheinlichkeiten mit der Bernoulli-Formel ansetzen, durch (1 − p)^(n − 1) kürzen, n · p durch 10 ersetzen, p bestimmen und dann n aus n · p = 10",
    schritte="4", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="P(X = 1) = 14 · P(X = 0) ⇔ n · p · (1 − p)^(n − 1) = 14 · (1 − p)^n ⇔ 10 = 14 · (1 − p) ⇔ p = 2/7; n · 2/7 = 10 ⇔ n = 35 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="(1 − p)^n nicht kürzen und mit n als Exponent stecken bleiben",
    bemerkung="Standardbezug: K1 II, K2 III, K5 III. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.1). Nach der engen Fassung II (algebraische Verkettung ohne Deutung des Sachverhalts), amtlich III – Messwert zur Regel.")

# ---- Stochastik 2.2: Produkt der Augenzahlen
row("2025MerhoehtAStochastik22", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Gleichheit zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen", typ_neben="",
    stichwoerter="X Produkt zweier Augenzahlen|10 = 2 · 5, 15 = 3 · 5|je zwei Reihenfolgen|gleich viele günstige Ergebnisse|Laplace",
    voraussetzungen="Zerlegung einer Zahl in zwei Faktoren von 1 bis 6|Laplace-Wahrscheinlichkeit über Anzahlen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Würfel", textumfang="kurz",
    gegeben="Würfel mit den Zahlen 1 bis 6, zweimal geworfen; X ist das Produkt der beiden Zahlen",
    gesucht="Begründung, dass P(X = 10) = P(X = 15)",
    verfahren="alle Faktorzerlegungen von 10 und 15 mit Faktoren von 1 bis 6 aufzählen; beide Male genau zwei Ergebnisse von 36",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="bis auf Vertauschung der Faktoren sind 2 · 5 und 3 · 5 die einzigen Möglichkeiten, 10 bzw. 15 als Produkt zweier erzielter Zahlen darzustellen; somit sind die Wahrscheinlichkeiten gleich groß (amtlich)",
    zwischenergebnis="P(X = 10) = P(X = 15) = 2/36",
    niveau_geschaetzt="II",
    fehlerquelle="1 · 10 als Zerlegung mitzählen",
    bemerkung="Standardbezug: K1 II, K2 I, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2025MerhoehtAStochastik22", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Term für die Wahrscheinlichkeit eines Produktereignisses bei n Würfen ermitteln", typ_neben="",
    stichwoerter="n Würfe, n > 2|Produkt 2, 3 oder 5|genau ein Wurf zeigt 2, 3 oder 5, alle anderen 1|Position des Wurfs n-fach wählbar|3 · n · 1/6 · (1/6)^(n − 1)",
    voraussetzungen="Primzahl als Produkt nur mit Einsen deuten|Pfadregel mit n Stufen|Anzahl der Reihenfolgen als Faktor n",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Würfel", textumfang="mittel",
    gegeben="Würfel mit den Zahlen 1 bis 6 wird n-mal geworfen, n > 2; Ereignis: das Produkt der n Zahlen ist 2, 3 oder 5",
    gesucht="Term für die Wahrscheinlichkeit dieses Ereignisses",
    verfahren="das Produkt ist genau dann 2, 3 oder 5, wenn genau ein Wurf diese Zahl zeigt und alle anderen Würfe 1 zeigen; drei Zahlen, n mögliche Positionen, Pfadwahrscheinlichkeit (1/6)^n",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="3 · n · 1/6 · (1/6)^(n − 1) (amtlich)",
    zwischenergebnis="für n = 3: 9/216 (Abzählen bestätigt)",
    niveau_geschaetzt="III",
    fehlerquelle="den Faktor n für die Position des Wurfs vergessen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 2.3: unabhängige Ereignisse (ungegliedert)
row("2025MerhoehtAStochastik23", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen", typ_neben="",
    stichwoerter="A und B unabhängig|P(B) = P(A) + 0,6|P(A und nicht B) = 0,04|x · (1 − (x + 0,6)) = 0,04|x² − 0,4x + 0,04 = 0|x = 0,2",
    voraussetzungen="Unabhängigkeit als Produktregel für A und das Gegenereignis von B|Gegenwahrscheinlichkeit|quadratische Gleichung mit doppelter Lösung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="zwei stochastisch unabhängige Ereignisse A und B mit P(B) = P(A) + 0,6 und P(A und nicht B) = 0,04",
    gesucht="P(A)",
    verfahren="mit x = P(A): P(nicht B) = 1 − (x + 0,6) = 0,4 − x; Unabhängigkeit liefert x · (0,4 − x) = 0,04; quadratische Gleichung lösen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="mit x = P(A) gilt x · (0,4 − x) = 0,04 ⇔ x² − 0,4x + 0,04 = 0 ⇔ x = 0,2 (amtlich)",
    zwischenergebnis="P(B) = 0,8|(x − 0,2)² = 0",
    niveau_geschaetzt="III",
    fehlerquelle="P(A und nicht B) = P(A) − P(B) oder P(A) · P(B) ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II. Amtlich, eigene Rechnung bestätigt; der Erwartungshorizont zeigt ein Baumdiagramm mit x, x + 0,6 und 0,4 − x. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.3). Erste Fundstelle des Themas Unabhängigkeit.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Gleiche Steigung aller Graphen einer Schar im Ursprung nachweisen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Die Ableitung einer Funktionsschar bilden und zeigen, dass ihr Wert an einer Stelle nicht "
     "vom Scharparameter abhängt.",
     "2025MerhoehtAAnalysis11-a"),
    ("Punktsymmetrie aller Graphen einer Schar zum Ursprung nachweisen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Für eine Funktionsschar f_a(−x) = −f_a(x) für alle Parameterwerte nachrechnen.",
     "2025MerhoehtAAnalysis11-b"),
    ("Graph einer Stammfunktion unter vorgegebenen Graphen begründet auswählen", "Analysis",
     "Ableitungsgraph und Funktionsgraph",
     "Aus mehreren abgebildeten Graphen den einer Stammfunktion auswählen, indem Extremstellen "
     "der Funktion als Wendestellen oder Nullstellen als Extremstellen der Stammfunktion gedeutet werden.",
     "2025MerhoehtAAnalysis12-b"),
    ("Integralwert aus der Symmetrie des Graphen angeben", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Wert eines bestimmten Integrals ohne Rechnung angeben, weil sich die orientierten "
     "Flächen über und unter der Achse am Graphen sichtbar aufheben.",
     "2025MerhoehtAAnalysis13-a"),
    ("Parameter einer Linearkombination aus Funktion und Gerade aus zwei Punkten bestimmen", "Analysis",
     "Rekonstruktion von Funktionsgleichungen",
     "Die Koeffizienten a und b in g(x) = a · f(x) + b · x aus zwei Punkten des Graphen von g "
     "über zwei Gleichungen bestimmen.",
     "2025MerhoehtAAnalysis13-b"),
    ("Bedingung für eine waagerechte Tangente eines Produkts mit e^x nachweisen", "Analysis",
     "Ableitungsregeln",
     "Für g = f · e^x mit allgemeinem f mit der Produktregel nachweisen, dass g'(a) = 0 die "
     "Gleichung f'(a) = −f(a) nach sich zieht.",
     "2025MerhoehtAAnalysis21-a"),
    ("Fehlende waagerechte Tangente über Vorzeichen am Graphen begründen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Aus den am Graphen abgelesenen Vorzeichen von Funktionswert und Steigung begründen, dass "
     "eine notwendige Bedingung für eine waagerechte Tangente verletzt ist.",
     "2025MerhoehtAAnalysis21-b"),
    ("Flächenbeziehung zwischen Funktion und Umkehrfunktion über die Spiegelung an y = x beurteilen",
     "Analysis", "Umkehrfunktion",
     "Eine Aussage über Integrale von Funktion und Umkehrfunktion beurteilen, indem die Integrale "
     "als Flächen gedeutet werden und die Spiegelung an der Winkelhalbierenden ausgenutzt wird.",
     "2025MerhoehtAAnalysis22"),
    ("Tangente mit gegebener Gleichung in die Abbildung einzeichnen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Eine Gerade mit vorgegebener Gleichung über zwei Punkte in ein vorhandenes "
     "Koordinatensystem einzeichnen.",
     "2025MerhoehtAAnalysis23-a"),
    ("Steigungen aller Sekanten durch einen Punkt des Graphen angeben", "Analysis",
     "Ableitung und Änderungsrate",
     "Die Menge der Steigungen aller Geraden angeben, die einen festen Punkt des Graphen mit "
     "einem weiteren verbinden, aus Randpunkt, Krümmung und Tangentensteigung als Grenzlage.",
     "2025MerhoehtAAnalysis23-b"),
    ("Koordinate eines Vektors aus vorgegebener Länge bestimmen", "Analytische Geometrie",
     "Vektoren und Rechenoperationen",
     "Eine unbekannte Koordinate eines Vektors aus seiner Länge über die Betragsgleichung "
     "bestimmen, mit Vorzeichenbedingung.",
     "2025MerhoehtAAGLAA11-a"),
    ("Parameter einer Matrix aus der Orthogonalität von v und M · v bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "M · v mit Parameter berechnen und den Parameter so bestimmen, dass das Skalarprodukt "
     "von v und M · v null ist.",
     "2025MerhoehtAAGLAA11-b"),
    ("Gestaffeltes Gleichungssystem für einen Parameterwert lösen", "Analytische Geometrie",
     "Lineare Gleichungssysteme",
     "Einen Parameterwert einsetzen und ein Gleichungssystem in Dreiecksform durch "
     "Rückwärtseinsetzen lösen.",
     "2025MerhoehtAAGLAA121-a"),
    ("Lösungsanzahl eines gestaffelten Gleichungssystems mit Parameter durch Fallunterscheidung begründen",
     "Analytische Geometrie", "Lineare Gleichungssysteme",
     "Die Lösungsanzahl auf eine Gleichung mit parameterabhängigem Koeffizienten zurückführen "
     "und die Fälle Koeffizient null mit wahrer bzw. falscher Aussage unterscheiden.",
     "2025MerhoehtAAGLAA121-b"),
    ("Bedingungen für die Vertauschbarkeit zweier Matrizen aus einer binomischen Gleichung untersuchen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Erkennen, dass eine binomische Formel für Matrizen genau bei Vertauschbarkeit gilt, und "
     "die Bedingungen an die Einträge aus X · A = A · X ableiten.",
     "2025MerhoehtAAGLAA122"),
    ("Art des Ergebnisses von Ausdrücken mit Skalarprodukt ankreuzen", "Analytische Geometrie",
     "Skalarprodukt und Winkel",
     "Für Ausdrücke aus Vektoren mit Skalarprodukt und Addition ankreuzen, ob sie einen Vektor, "
     "eine Zahl oder nichts Definiertes darstellen.",
     "2025MerhoehtAAGLAA211-a"),
    ("Parameter für einen Winkel von mindestens 90° über das Skalarprodukt ermitteln",
     "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Die Parameterwerte bestimmen, für die der Winkel zweier Vektoren mindestens 90° beträgt, "
     "über die Ungleichung Skalarprodukt kleiner oder gleich null.",
     "2025MerhoehtAAGLAA211-b"),
    ("Volumen eines Teilkörpers eines Würfels berechnen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Den Teilkörper, den eine Ebene von einem Würfel abschneidet, im Schrägbild als Prisma "
     "erkennen und sein Volumen berechnen.",
     "2025MerhoehtAAGLAA212-a"),
    ("Schnittfigur einer Ebene mit einem Würfel einzeichnen", "Analytische Geometrie", "Schnittmengen",
     "Die Schnittfigur einer durch drei Punkte gegebenen Ebene mit einem Würfel über parallele "
     "Schnittkanten in das Schrägbild einzeichnen.",
     "2025MerhoehtAAGLAA212-b"),
    ("Schnittgerade zweier Ebenen aus dem Schrägbild angeben", "Analytische Geometrie", "Schnittmengen",
     "Eine Gleichung der Schnittgeraden zweier Ebenen aus gemeinsamen Punkten und Richtungen "
     "im Schrägbild angeben, ohne Ebenengleichungen aufzustellen.",
     "2025MerhoehtAAGLAA212-b"),
    ("Identität aller Geraden einer Schar beurteilen", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Beurteilen, ob alle Geraden einer Schar identisch sind, indem der parameterabhängige "
     "Stützvektor als fester Punkt plus Vielfaches des Richtungsvektors geschrieben wird.",
     "2025MerhoehtAAGLAA221-b"),
    ("Koordinatenebene senkrecht zu allen Ebenen einer Schar angeben", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Aus einer fehlenden Koordinate in der Koordinatengleichung einer Ebenenschar die "
     "Koordinatenebene angeben, auf der alle Ebenen senkrecht stehen.",
     "2025MerhoehtAAGLAA222-a"),
    ("Nichtparallelität verschiedener Ebenen einer Schar über die Normalenvektoren nachweisen",
     "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Für zwei Ebenen einer Schar mit verschiedenen Parametern zeigen, dass ihre "
     "Normalenvektoren nicht kollinear sind.",
     "2025MerhoehtAAGLAA222-b"),
    ("Vektorterm für einen Eckpunkt eines Pyramidenstumpfs begründen", "Analytische Geometrie",
     "Vektoren und Rechenoperationen",
     "Einen vorgegebenen Vektorterm für einen Eckpunkt über Mittelpunkte, Ähnlichkeit "
     "(Flächenfaktor als Längenfaktor) und eine Vektorkette begründen.",
     "2025MerhoehtAAGLAA223-b"),
    ("Wahrscheinlichkeit für zweimal kein Treffer über die Pfadregel begründen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit, bei zwei unabhängigen Versuchen beide Male kein Treffer zu "
     "erzielen, als Quadrat der Gegenwahrscheinlichkeit begründen.",
     "2025MerhoehtAStochastik11-a"),
    ("Aussage über eine Summe von Wahrscheinlichkeiten am Säulendiagramm entscheiden", "Stochastik",
     "Binomialverteilung",
     "Eine Aussage über eine Summe von Einzelwahrscheinlichkeiten entscheiden, indem die "
     "Säulenhöhen im Diagramm gegen eine Schranke abgeschätzt werden.",
     "2025MerhoehtAStochastik12-a"),
    ("Verhältnis zweier Trefferwahrscheinlichkeiten aus den Erwartungswerten im Diagramm nachweisen",
     "Stochastik", "Kenngrößen von Verteilungen",
     "Die ganzzahligen Erwartungswerte zweier Binomialverteilungen an den höchsten Säulen "
     "ablesen und bei gleichem n das Verhältnis der Trefferwahrscheinlichkeiten nachweisen.",
     "2025MerhoehtAStochastik12-b"),
    ("Parameter n und p aus einem Verhältnis zweier Einzelwahrscheinlichkeiten und dem Erwartungswert berechnen",
     "Stochastik", "Binomialverteilung",
     "n und p einer Binomialverteilung aus dem Verhältnis P(X = 1) zu P(X = 0) und dem "
     "Erwartungswert berechnen, indem die Bernoulli-Terme gekürzt werden und n · p ersetzt wird.",
     "2025MerhoehtAStochastik21"),
    ("Gleichheit zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Begründen, dass zwei Werte einer Zufallsgröße gleich wahrscheinlich sind, weil gleich "
     "viele Ergebnisse des Laplace-Experiments zu ihnen führen.",
     "2025MerhoehtAStochastik22-a"),
    ("Term für die Wahrscheinlichkeit eines Produktereignisses bei n Würfen ermitteln", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Einen Term in n für die Wahrscheinlichkeit aufstellen, dass das Produkt von n Augenzahlen "
     "einen vorgegebenen Wert hat, über die möglichen Belegungen und die Pfadregel.",
     "2025MerhoehtAStochastik22-b"),
    ("Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen",
     "Stochastik", "Unabhängigkeit",
     "P(A) aus der Unabhängigkeit von A und B, einer Beziehung zwischen P(A) und P(B) und einer "
     "Schnittwahrscheinlichkeit über eine Gleichung bestimmen.",
     "2025MerhoehtAStochastik23"),
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
          f"({100 * len(wieder) / len(verwendet):.0f} %) | {geltung_txt} |")
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
