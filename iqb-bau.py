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
    "stapel": "2025-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2025MgrundlegendAAnalysis11": 5,
        "2025MgrundlegendAAnalysis12": 5,
        "2025MgrundlegendAAnalysis13": 5,
        "2025MgrundlegendAAnalysis21": 5,
        "2025MgrundlegendAAnalysis22": 5,
        "2025MgrundlegendAAGLAA11": 5,
        "2025MgrundlegendAAGLAA12": 5,
        "2025MgrundlegendAAGLAA211": 5,
        "2025MgrundlegendAAGLAA212": 5,
        "2025MgrundlegendAAGLAA213": 5,
        "2025MgrundlegendAAGLAA221": 5,
        "2025MgrundlegendAStochastik11": 5,
        "2025MgrundlegendAStochastik12": 5,
        "2025MgrundlegendAStochastik13": 5,
        "2025MgrundlegendAStochastik21": 5,
        "2025MgrundlegendAStochastik22": 5,
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
# niveau_geschaetzt nach der Regel „Kombinieren heißt III" (weite Fassung, iqb.md § 7);
# wo die enge Fassung (III nur mit Deutung oder Fallunterscheidung) abweicht, steht
# „Schätzung enge Fassung: …" in bemerkung.

# ---- Analysis 1.1: Tangente und parallele Tangente
KUB3_SKIZZE = ("Koordinatensystem mit x-Achse von −4 bis 5 und y-Achse von −6 bis 6, Gitter; "
               "Graph G von f(x) = 1/8 x^3 − 3/8 x^2 − 1: von links unten steil steigend, "
               "Hochpunkt (0; −1), Tiefpunkt (2; −1,5), dann steigend durch P(4; 1) markiert, "
               "steil nach rechts oben")
row("2025MgrundlegendAAnalysis11", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen", typ_neben="",
    stichwoerter="Ableitung 3/8 x^2 − 3/4 x|Steigung f'(4) = 3|y = mx + b|b = −11",
    voraussetzungen="Potenzregel|Punkt in die Geradengleichung einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Koordinatensystem", skizze=KUB3_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/8 x^3 − 3/8 x^2 − 1, definiert in IR, Graph G in der Abbildung; Tangente t an G im Punkt P(4; 1)",
    gesucht="Gleichung von t, rechnerisch",
    verfahren="f'(x) = 3/8 x^2 − 3/4 x, Steigung m = f'(4) = 3; b aus 1 = 3 · 4 + b",
    schritte="3", zahlenraum="Bruch|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 3/8 x^2 − 3/4 x, m = f'(4) = 3, b = 1 − 3 · 4 = −11, also t: y = 3x − 11 (amtlich)",
    zwischenergebnis="f'(4) = 6 − 3 = 3",
    niveau_geschaetzt="I",
    fehlerquelle="f(4) statt f'(4) als Steigung nehmen",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt. Datei mit drei Seiten.")

row("2025MgrundlegendAAnalysis11", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Parallele Tangente über die Ableitung finden und skizzieren", typ_neben="",
    stichwoerter="f'(x) = 3|zweite Stelle x = −2|Berührpunkt (−2; −3,5)|parallele Gerade skizzieren",
    voraussetzungen="quadratische Gleichung lösen|Gerade mit vorgegebener Steigung durch einen Punkt zeichnen",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=KUB3_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/8 x^3 − 3/8 x^2 − 1, Graph G in der Abbildung; die Tangente t in P(4; 1) hat die Steigung 3; es gibt genau eine weitere Tangente an G, die parallel zu t verläuft",
    gesucht="Skizze dieser weiteren Tangente in der Abbildung",
    verfahren="f'(x) = 3 lösen: 3/8 x^2 − 3/4 x − 3 = 0, also x^2 − 2x − 8 = 0 mit den Stellen 4 und −2; Berührpunkt (−2; f(−2)) = (−2; −3,5), dort eine Gerade mit Steigung 3 einzeichnen",
    schritte="3", zahlenraum="ganz|negativ|dezimal", einheiten="", abhaengig_von="2025MgrundlegendAAnalysis11-a",
    ergebnis="Gerade mit Steigung 3 durch den Berührpunkt (−2; −3,5), parallel zu t (amtlich)",
    zwischenergebnis="x^2 − 2x − 8 = 0|f(−2) = −1 − 1,5 − 1 = −3,5",
    niveau_geschaetzt="II",
    fehlerquelle="die Tangente nach Augenmaß am Hochpunkt (0; −1) ansetzen statt die Berührstelle zu berechnen",
    bemerkung="Standardbezug: K2 II, K4 II. Amtlich; der Erwartungshorizont zeigt die Abbildung mit beiden Tangenten, die parallele gestrichelt durch (−2; −3,5). Eigene Rechnung bestätigt. Das Feld skizze beschreibt das Material, die Lösung ist eine Zeichnung.")

# ---- Analysis 1.2: Stammfunktion durch Punkt, Integral über symmetrisches Intervall
row("2025MgrundlegendAAnalysis12", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion durch einen vorgegebenen Punkt bestimmen", typ_neben="",
    stichwoerter="F(x) = x^4 − 3x^2 + c|Punkt (1; 0)|c = 2",
    voraussetzungen="Potenzregel der Integration|Integrationskonstante über eine Punktbedingung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 4x^3 − 6x, ganzrational, definiert in IR",
    gesucht="die Stammfunktion F von f, deren Graph durch (1; 0) verläuft",
    verfahren="allgemeine Stammfunktion x^4 − 3x^2 + c bilden und F(1) = 0 nach c auflösen",
    schritte="2", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="F(x) = x^4 − 3x^2 + 2 (amtlich)",
    zwischenergebnis="F(1) = 1 − 3 + c = 0",
    niveau_geschaetzt="II",
    fehlerquelle="die Konstante c vergessen und F(x) = x^4 − 3x^2 als einzige Stammfunktion angeben",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendAAnalysis12", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integral null über die Punktsymmetrie begründen", typ_neben="",
    stichwoerter="ohne zu rechnen|Intervall [−3; 3] symmetrisch zu 0|nur ungerade Exponenten|Punktsymmetrie zum Ursprung|Flächen heben sich auf",
    voraussetzungen="Punktsymmetrie am Term erkennen|Integral als orientierten Flächeninhalt deuten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 4x^3 − 6x, definiert in IR; Integral von −3 bis 3 über f(x) dx",
    gesucht="Begründung ohne Rechnung, dass das Integral den Wert 0 hat",
    verfahren="der Term enthält nur ungerade Potenzen, der Graph ist punktsymmetrisch zum Ursprung; über einem zu 0 symmetrischen Intervall heben sich die orientierten Flächen links und rechts auf",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="das Intervall [−3; 3] ist symmetrisch zu 0 und der Graph von f ist punktsymmetrisch zum Koordinatenursprung, weil der Term nur ungerade Exponenten enthält (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="mit Achsensymmetrie argumentieren",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt (Integral gleich 0).")

# ---- Analysis 1.3: e-Funktion, Fläche mit den Achsen
EXP_SKIZZE = ("Koordinatensystem mit x-Achse von −4 bis 2 und y-Achse von −4 bis 2; Graph von "
              "f(x) = 2e^x − 2e: von links waagerecht nahe −2e ≈ −5,4 kommend, steigend durch "
              "(0; 2 − 2e ≈ −3,4) und die Nullstelle 1, dann steil nach oben")
row("2025MgrundlegendAAnalysis13", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstelle durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="f(1) = 2e − 2e = 0|Nullstelle 1|e-Funktion",
    voraussetzungen="e^1 = e einsetzen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Koordinatensystem", skizze=EXP_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 2e^x − 2e, definiert in IR, Graph in der Abbildung",
    gesucht="Nachweis, dass 1 eine Nullstelle von f ist",
    verfahren="x = 1 einsetzen",
    schritte="1", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f(1) = 2e^1 − 2e = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="e als Variable behandeln und die Gleichung lösen wollen",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendAAnalysis13", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche zwischen Graph und Koordinatenachsen berechnen", typ_neben="",
    stichwoerter="Grenzen 0 und 1|Stammfunktion 2e^x − 2ex|Integral −2|Flächeninhalt 2",
    voraussetzungen="Grenzen als y-Achse und Nullstelle erkennen|Stammfunktion von e^x und einer Konstanten|negatives Integral als Fläche deuten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=EXP_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 2e^x − 2e mit der Nullstelle 1; der Graph schließt mit den Koordinatenachsen eine Fläche ein (zwischen x = 0 und x = 1 unter der x-Achse)",
    gesucht="Inhalt dieser Fläche",
    verfahren="Integral von 0 bis 1 über f mit der Stammfunktion 2e^x − 2ex auswerten, Betrag nehmen",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="2025MgrundlegendAAnalysis13-a",
    ergebnis="Integral von 0 bis 1 über f(x) dx = [2e^x − 2ex] von 0 bis 1 = 2e − 2e − 2 = −2; der Inhalt der Fläche ist 2 (amtlich)",
    zwischenergebnis="Stammfunktion 2e^x − 2ex|Wert an der Stelle 0: 2",
    niveau_geschaetzt="II",
    fehlerquelle="−2 als Flächeninhalt angeben oder 2e als 2e^x integrieren",
    bemerkung="Standardbezug: K1 I, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 2.1: Verschiebung und Flächenhalbierung
QUAD_SKIZZE = ("Koordinatensystem mit x-Achse von etwa −1,5 bis 1,5 und y-Achse von −1,5 bis 1,5; "
               "gestrichelt ein Quadrat mit den Ecken (±1; ±1), symmetrisch zu beiden Achsen; "
               "Graph von f(x) = x^4 − x^2: W-Form mit Nullstellen −1, 0, 1, Tiefpunkten bei etwa "
               "(±0,7; −0,25) und Hochpunkt im Ursprung, außerhalb des Quadrats steil steigend")
row("2025MgrundlegendAAnalysis21", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Verschobenen Graphen in die Abbildung skizzieren", typ_neben="",
    stichwoerter="Verschiebung um 1 in y-Richtung|Graph von x^4 − x^2 + 1|Skizze",
    voraussetzungen="Verschiebung in y-Richtung als Addition einer Konstanten",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=QUAD_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x^4 − x^2, definiert in IR, Graph und Quadrat mit Seitenlänge 2 symmetrisch zu beiden Achsen in der Abbildung; der Graph wird um 1 in y-Richtung verschoben",
    gesucht="Skizze des verschobenen Graphen in der Abbildung",
    verfahren="jeden Punkt des Graphen um 1 nach oben setzen: Hochpunkt (0; 1) auf der oberen Quadratseite, Tiefpunkte bei (±0,7; 0,75), Punkte (±1; 1) in den oberen Ecken",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Graph von x^4 − x^2 + 1: W-Form mit Hochpunkt (0; 1), Tiefpunkten bei etwa (±0,7; 0,75) und durch die oberen Ecken (±1; 1) des Quadrats (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="den Graphen nach rechts statt nach oben verschieben",
    bemerkung="Standardbezug: K2 I, K4 I. Amtlich; der Erwartungshorizont zeigt beide Graphen im Quadrat. Das Feld skizze beschreibt das Material, die Lösung ist eine Zeichnung.")

row("2025MgrundlegendAAnalysis21", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Verschiebung für die Halbierung einer Fläche über ein Integral bestimmen", typ_neben="",
    stichwoerter="Quadrat mit Fläche 4|Graph teilt das Quadrat in zwei gleiche Flächen|Symmetrie zur y-Achse|Integral von 0 bis 1 gleich null|c = 2/15",
    voraussetzungen="Flächenhalbierung als Bedingung an ein Integral übersetzen|Symmetrie ausnutzen|Stammfunktion mit Parameter",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=QUAD_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = x^4 − x^2; Quadrat mit den Ecken (±1; ±1); der Graph wird um c > 0 in y-Richtung verschoben, sodass er das Quadrat in zwei Flächen gleichen Inhalts teilt",
    gesucht="Wert von c",
    verfahren="der verschobene Graph x^4 − x^2 + c teilt das Quadrat genau dann in gleiche Teile, wenn er die x-Achse als Mittellinie im Mittel trifft: Integral von 0 bis 1 über x^4 − x^2 + c gleich 0 (Symmetrie zur y-Achse); 1/5 − 1/3 + c = 0",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="2025MgrundlegendAAnalysis21-a",
    ergebnis="Integral von 0 bis 1 über (x^4 − x^2 + c) dx = 0 ist gleichwertig zu 1/5 − 1/3 + c = 0, also c = 2/15 (amtlich)",
    zwischenergebnis="[1/5 x^5 − 1/3 x^3 + cx] von 0 bis 1",
    niveau_geschaetzt="III",
    fehlerquelle="das Integral gleich 2 (halbe Quadratfläche) setzen statt gleich 0, oder über [−1; 1] ohne Symmetrie rechnen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Enge und weite Fassung der Schätzung stimmen überein (Deutung der Flächenhalbierung).")

# ---- Analysis 2.2: Gleichung mit Differenzenquotient und Ableitung
PAR_SKIZZE = ("Koordinatensystem mit x-Achse von −2 bis 6 und y-Achse von −6 bis 3, Gitter; nach "
              "unten geöffnete Parabel f(x) = −x^2 + 4x − 1 mit Scheitel (2; 3), Nullstellen bei "
              "etwa 0,27 und 3,73, y-Achsenabschnitt −1")
row("2025MgrundlegendAAnalysis22", "a", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Gleichung aus Differenzenquotient und Ableitung lösen",
    typ_neben="Ableitung einer quadratischen Funktion angeben",
    stichwoerter="f'(x) = −2x + 4|(f(x) − 0)/(x − 0) = f'(x)|Bruchgleichung|x^2 = 1|x = ±1",
    voraussetzungen="Potenzregel|Bruchgleichung durch Multiplikation mit x lösen|Ergebnis auf x ungleich 0 prüfen",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Ermitteln Sie", antwort="Term|Zahl",
    material="Koordinatensystem", skizze=PAR_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −x^2 + 4x − 1, definiert in IR, Graph in der Abbildung; Gleichung (f(x) − 0)/(x − 0) = f'(x)",
    gesucht="Term von f'|Lösungen der Gleichung, rechnerisch",
    verfahren="f'(x) = −2x + 4; die Gleichung mit x multiplizieren: −x^2 + 4x − 1 = −2x^2 + 4x, also x^2 = 1",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −2x + 4|(−x^2 + 4x − 1)/x = −2x + 4 ist gleichwertig zu x^2 = 1, also x = −1 oder x = 1 (amtlich)",
    zwischenergebnis="−x^2 + 4x − 1 = −2x^2 + 4x",
    niveau_geschaetzt="III",
    fehlerquelle="beim Multiplizieren mit x den Term 4x auf der rechten Seite vergessen oder nur x = 1 angeben",
    bemerkung="Standardbezug: K2 II, K4 II, K5 III. Amtlich, eigene Rechnung bestätigt. Schätzung enge Fassung: II (Verkettung zweier Standardschritte ohne Deutung).")

row("2025MgrundlegendAAnalysis22", "b", seite="1", punkte="2", afb_amtlich="III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Gleichung als Tangentenbedingung geometrisch deuten", typ_neben="",
    stichwoerter="Differenzenquotient zum Ursprung|Steigung der Verbindungsgeraden|gleich der Tangentensteigung|Tangente durch den Ursprung",
    voraussetzungen="Differenzenquotient als Steigung einer Sekante deuten|Ableitung als Tangentensteigung",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=PAR_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −x^2 + 4x − 1; Gleichung (f(x) − 0)/(x − 0) = f'(x) mit den Lösungen x = −1 und x = 1",
    gesucht="geometrische Bedeutung der Gleichung für ihre Lösungen",
    verfahren="die linke Seite ist die Steigung der Geraden durch den Ursprung und (x; f(x)), die rechte die Tangentensteigung; Gleichheit heißt, die Tangente in (x; f(x)) geht durch den Ursprung",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2025MgrundlegendAAnalysis22-a",
    ergebnis="ist x eine Lösung, dann verläuft die Tangente an den Graphen von f im Punkt (x; f(x)) durch den Koordinatenursprung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Gleichung als Schnitt von f und f' deuten",
    bemerkung="Standardbezug: K4 III, K6 III. Amtlich.")

# ---- AG/LA (A1) 1: Matrix mit Parametern, Fixvektor (ungegliedert)
row("2025MgrundlegendAAGLAA11", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Parameter einer Matrix aus einer Matrix-Vektor-Gleichung untersuchen", typ_neben="",
    stichwoerter="M · v = v|Matrix mit Parametern a und b|drei Gleichungen|b = 1/2, a = 1/4|dritte Gleichung als Probe",
    voraussetzungen="Matrix-Vektor-Produkt mit Parametern|überbestimmtes Gleichungssystem lösen und prüfen",
    format="Rechnung", operator="Untersuchen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="M = ((0; b; 0), (1; 0; a), (0; 0,5; 1 − a)) mit reellen a und b; v = (1; 2; 4)",
    gesucht="Untersuchung, ob es Werte von a und b gibt, sodass M · v = v gilt",
    verfahren="M · v = (2b; 1 + 4a; 5 − 4a) mit v gleichsetzen: I 2b = 1, II 1 + 4a = 2, III 5 − 4a = 4; aus I und II folgen b und a, III bestätigt",
    schritte="3", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="ja: aus 2b = 1 folgt b = 1/2, aus 1 + 4a = 2 folgt a = 1/4, und 5 − 4 · 1/4 = 4 bestätigt die dritte Gleichung (amtlich)",
    zwischenergebnis="M · v = (2b; 1 + 4a; 5 − 4a)",
    niveau_geschaetzt="III",
    fehlerquelle="die dritte Gleichung nicht prüfen oder aus III einen zweiten Wert für a ableiten",
    bemerkung="Standardbezug: K1 II, K4 I, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, einzige Aufgabe der Gruppe 1 (aufgabe „1“); die Kurzbeschreibung schreibt „AG/LA (1)“. Thema Matrizen und Übergangsprozesse auch auf grundlegendem Niveau. Schätzung enge Fassung: II (Aufstellen und Lösen eines Gleichungssystems ohne Deutung).")

# ---- AG/LA (A1) 2: lineares Gleichungssystem mit Parameter (Dublette 2025MgrundlegendAAGLAA222)
row("2025MgrundlegendAAGLAA12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lösung eines Gleichungssystems durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="zwei Gleichungen, drei Unbekannte|x = 2, y = −3, z = −2|Einsetzen",
    voraussetzungen="Werte in beide Gleichungen einsetzen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="lineares Gleichungssystem I: 2x − y − 2z = 11, II: x + 4z = −6",
    gesucht="Nachweis, dass x = 2, y = −3, z = −2 eine Lösung ist",
    verfahren="Werte in I und II einsetzen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="4 + 3 + 4 = 11 und 2 − 8 = −6, also Lösung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen beim Einsetzen von y = −3 in −y verfehlen",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt. Die Kurzbeschreibung nennt nur AG/LA; die Datei liegt wortgleich als 2025MgrundlegendAAGLAA222 ein zweites Mal vor (Dublette ohne Zeile).")

row("2025MgrundlegendAAGLAA12", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lösbarkeit eines Gleichungssystems mit Parameter beurteilen", typ_neben="",
    stichwoerter="dritte Gleichung mit Parameter a|I + II = III für a = 5|unendlich viele Lösungen|Aussage wahr",
    voraussetzungen="Gleichungen addieren|abhängige Gleichung als redundant erkennen|Lösungsmenge mit freiem Parameter deuten",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="I: 2x − y − 2z = 11, II: x + 4z = −6, III: 3x − y + 2z = a; Aussage: es gibt ein reelles a, für das das System aus I, II und III unendlich viele Lösungen hat",
    gesucht="Beurteilung der Aussage",
    verfahren="I + II ergibt 3x − y + 2z = 5, also stimmt III für a = 5 mit I + II überein; für jedes z liefern II und I Werte für x und y, die dann auch III erfüllen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="die Aussage ist wahr: die Addition von I und II liefert 3x − y + 2z = 5; für a = 5 ist III eine Folge von I und II, und für jedes z gibt es passende x und y, also unendlich viele Lösungen (amtlich)",
    zwischenergebnis="a = 5",
    niveau_geschaetzt="III",
    fehlerquelle="das System für a = 5 als widersprüchlich halten oder für alle a eindeutig lösbar erklären",
    bemerkung="Standardbezug: K1 III, K2 II, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Enge und weite Fassung stimmen überein (Beurteilung).")

# ---- AG/LA (A2) 1.1: Gerade, Punktprobe, Orthogonalität
row("2025MgrundlegendAAGLAA211", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punktprobe an einer Geraden durchführen",
    typ_neben="Punkt auf einer Geraden mit vorgegebener Koordinate angeben",
    stichwoerter="Parameter s aus zwei Koordinaten verschieden|s = 1 und s = 2|Punkt nicht auf g|Q(4; 3; 0) für s = 1",
    voraussetzungen="Parametergleichung koordinatenweise ansetzen|Widerspruch im Parameter erkennen",
    format="Begründung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="g: x = (8; 3; −3) + s · (−4; 0; 3), s reell; P(4; 3; 3)",
    gesucht="Nachweis, dass P nicht auf g liegt|Koordinaten eines Punktes Q auf g, der sich nur in einer Koordinate von P unterscheidet",
    verfahren="Ansatz (4; 3; 3) = (8; 3; −3) + s · (−4; 0; 3): erste Koordinate s = 1, dritte s = 2, Widerspruch; Q für s = 1: (4; 3; 0)",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="aus der ersten Koordinate folgt s = 1, aus der dritten s = 2, also liegt P nicht auf g|Q(4; 3; 0) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur eine Koordinate prüfen und P auf g wähnen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendAAGLAA211", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Orthogonalität zweier Geraden über das Skalarprodukt untersuchen", typ_neben="",
    stichwoerter="parallel zur y-Achse|Richtungsvektor (0; 1; 0)|Skalarprodukt 0|senkrecht",
    voraussetzungen="Richtungsvektor einer achsenparallelen Geraden angeben|Skalarprodukt",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (8; 3; −3) + s · (−4; 0; 3); die Gerade h verläuft parallel zur y-Achse und schneidet g im Punkt (8; 3; −3)",
    gesucht="Untersuchung, ob g und h senkrecht zueinander verlaufen",
    verfahren="Richtungsvektor (0; 1; 0) von h mit dem Richtungsvektor von g skalar multiplizieren",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(0; 1; 0) ist Richtungsvektor von h; wegen (−4; 0; 3) · (0; 1; 0) = 0 verlaufen g und h senkrecht zueinander (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den Richtungsvektor von h aus dem Schnittpunkt ablesen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 1.2: Lage zur xy-Ebene, gleichschenkliges Dreieck
row("2025MgrundlegendAAGLAA212", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Lage zweier Punkte zu einer Koordinatenebene begründen", typ_neben="",
    stichwoerter="xy-Ebene|z-Koordinaten −1 und −4|gleiches Vorzeichen|dieselbe Seite",
    voraussetzungen="Koordinatenebene über die dritte Koordinate deuten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(3; 1; −1) und Q(4; 2; −4)",
    gesucht="Begründung, dass P und Q auf derselben Seite bezüglich der xy-Ebene liegen",
    verfahren="Vorzeichen der z-Koordinaten vergleichen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="die z-Koordinaten beider Punkte haben dasselbe Vorzeichen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die x- oder y-Koordinaten vergleichen",
    bemerkung="Standardbezug: K1 I, K2 I. Amtlich.")

row("2025MgrundlegendAAGLAA212", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen", typ_neben="",
    stichwoerter="Basis OQ mit Länge 6|Mittelpunkt M(2; 1; −2)|Höhe MP|MP = (1; 0; 1), Länge √2|Fläche 3√2",
    voraussetzungen="Mittelpunkt einer Strecke|Höhe im gleichschenkligen Dreieck trifft die Basismitte|Vektorlänge",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="P(3; 1; −1), Q(4; 2; −4) und der Ursprung O sind Eckpunkte eines gleichschenkligen Dreiecks mit der Basis OQ der Länge 6",
    gesucht="Flächeninhalt des Dreiecks",
    verfahren="Mittelpunkt M von OQ bestimmen; MP ist die Höhe auf die Basis; Fläche 1/2 · |OQ| · |MP|",
    schritte="3", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="2025MgrundlegendAAGLAA212-a",
    ergebnis="M(2; 1; −2), MP = (1; 0; 1); Flächeninhalt 1/2 · |OQ| · |MP| = 3√2 (amtlich)",
    zwischenergebnis="|MP| = √2|Probe: |OP| = |PQ| = √11",
    niveau_geschaetzt="III",
    fehlerquelle="die Höhe von P auf OQ mit |OP| gleichsetzen",
    bemerkung="Standardbezug: K1 I, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Schätzung enge Fassung: II (Mittelpunkt, Höhe, Fläche als Standardkette ohne Deutung).")

# ---- AG/LA (A2) 1.3: Punktspiegelung, Normalenvektor
row("2025MgrundlegendAAGLAA213", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Spiegelpunkt an einem Punkt bestimmen", typ_neben="",
    stichwoerter="Punktspiegelung|OP' = OQ + PQ|P'(4; 11; 5)",
    voraussetzungen="Verbindungsvektor bilden und abtragen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(0; −1; 1) und Q(2; 5; 3); P' entsteht durch Spiegelung von P am Punkt Q",
    gesucht="Koordinaten von P'",
    verfahren="OP' = OQ + PQ, also Q plus den Vektor PQ = (2; 6; 2)",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="OP' = OQ + PQ = (4; 11; 5), also P'(4; 11; 5) (amtlich)",
    zwischenergebnis="PQ = (2; 6; 2)",
    niveau_geschaetzt="II",
    fehlerquelle="PQ an P statt an Q abtragen und Q selbst erhalten",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendAAGLAA213", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punktprobe an einer Ebenengleichung durchführen",
    typ_neben="Vektor als Normalenvektor einer Ebene über Kollinearität nachweisen",
    stichwoerter="Koordinatengleichung x1 + 3x2 + x3 = 20|Q einsetzen|PQ = (2; 6; 2) kollinear zu (1; 3; 1)",
    voraussetzungen="Normalenvektor aus der Koordinatengleichung ablesen|Vielfaches erkennen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(0; −1; 1), Q(2; 5; 3); E: x1 + 3x2 + x3 = 20",
    gesucht="Nachweis, dass Q in E liegt|Nachweis, dass PQ ein Normalenvektor von E ist",
    verfahren="Q in die Koordinatengleichung einsetzen; PQ = (2; 6; 2) = 2 · (1; 3; 1) mit dem Normalenvektor vergleichen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="2 + 3 · 5 + 3 = 20, also liegt Q in E|PQ = (2; 6; 2) ist kollinear zum Normalenvektor (1; 3; 1) von E (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="für den Normalenvektor das Skalarprodukt PQ · (1; 3; 1) = 0 erwarten",
    bemerkung="Standardbezug: K1 II, K2 I, K5 I. Amtlich, eigene Rechnung bestätigt. Punktprobe aus 2026-ga-A wiederverwendet; der Nebentyp ist dieselbe Prüfung wie „Orthogonalität von Gerade und Ebene über Normalen- und Richtungsvektor begründen“, hier ohne Gerade – Vorschlag für den Abgleich, beide zusammenzuziehen.")

# ---- AG/LA (A2) 2.1: Ebene in Parameterform, Spiegelung mit Abstand
row("2025MgrundlegendAAGLAA221", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen", typ_neben="",
    stichwoerter="Parameterform|zwei Spannvektoren|Skalarprodukte −12 + 12 und 12 − 12|senkrecht",
    voraussetzungen="Vektor senkrecht zur Ebene heißt senkrecht zu beiden Spannvektoren",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: x = (1; −3; 0) + r · (−3; 4; 1) + s · (3; −4; 0), r und s reell; Vektor (4; 3; 0)",
    gesucht="Nachweis, dass (4; 3; 0) senkrecht zu E steht",
    verfahren="Skalarprodukte mit beiden Spannvektoren bilden",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(−3; 4; 1) · (4; 3; 0) = −12 + 12 = 0 und (3; −4; 0) · (4; 3; 0) = 12 − 12 = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur einen Spannvektor prüfen",
    bemerkung="Standardbezug: K1 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendAAGLAA221", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Punkt mit vorgegebenem Abstand zu seinem Spiegelbild an einer Ebene bestimmen", typ_neben="",
    stichwoerter="Spiegelung an E|Abstand zum Spiegelbild 20 heißt Abstand 10 zu E|Normalenvektor mit Länge 5|Stützpunkt plus 2 · Normalenvektor|P(9; 3; 0)",
    voraussetzungen="Abstand Punkt–Spiegelbild als doppelten Abstand zur Ebene deuten|Länge des Normalenvektors|Punkt entlang der Normalen versetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="E: x = (1; −3; 0) + r · (−3; 4; 1) + s · (3; −4; 0); (4; 3; 0) ist Normalenvektor von E; gesucht ist ein Punkt P, dessen Spiegelbild an E von P den Abstand 20 hat",
    gesucht="Koordinaten eines solchen Punktes P",
    verfahren="P muss Abstand 10 zu E haben; |(4; 3; 0)| = 5, also vom Ebenenpunkt (1; −3; 0) aus 2 · (4; 3; 0) abtragen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2025MgrundlegendAAGLAA221-a",
    ergebnis="|(4; 3; 0)| = √(16 + 9) = 5; (1; −3; 0) + 2 · (4; 3; 0) = (9; 3; 0) (amtlich)",
    zwischenergebnis="Abstand von P zu E gleich 10|weiterer möglicher Punkt (−7; −9; 0)",
    niveau_geschaetzt="III",
    fehlerquelle="Abstand 20 statt 10 zur Ebene ansetzen und 4 · (4; 3; 0) abtragen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Enge und weite Fassung stimmen überein (Deutung des Spiegelabstands).")

# ---- Stochastik 1.1: Baumdiagramm Onlinespiel
row("2025MgrundlegendAStochastik11", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="Startpunkt A 40 %|P(C|A) = 80 %|P(B und C) = 42 %|fehlender Ast 0,42/0,6 = 70 %|Beschriftung",
    voraussetzungen="Pfadwahrscheinlichkeit rückwärts in eine Astwahrscheinlichkeit umrechnen|Gegenwahrscheinlichkeiten",
    format="Zeichnen", operator="Erstellen Sie", antwort="Grafik",
    material="keins", skizze="zu zeichnen ist ein zweistufiges Baumdiagramm mit erster Stufe A (40 %) und A quer (60 %), zweiter Stufe C und C quer: unter A 80 % und 20 %, unter A quer 70 % und 30 %; Ereignisse A Startpunkt A zugewiesen, C Spieler trifft auf den Charakter",
    kontext="Onlinespiel", textumfang="lang",
    gegeben="Startpunkt A wird mit 40 % zugewiesen, sonst B; bei Start A trifft der Spieler mit 80 % auf einen bestimmten Charakter; Startpunkt B und Treffen auf den Charakter zusammen 42 %",
    gesucht="beschriftetes Baumdiagramm zum Sachverhalt",
    verfahren="erste Stufe A/B mit 0,4 und 0,6; zweite Stufe unter A 0,8 und 0,2; unter B den Ast 0,42/0,6 = 0,7 und 0,3",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Baumdiagramm mit A (40 %) und A quer (60 %), darunter C (80 %) und C quer (20 %) bzw. C (70 %) und C quer (30 %); A: Startpunkt A zugewiesen, C: Spieler trifft auf den Charakter (amtlich)",
    zwischenergebnis="P(C|B) = 0,42/0,6 = 0,7",
    niveau_geschaetzt="II",
    fehlerquelle="42 % als Astwahrscheinlichkeit unter B eintragen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Typname aus abi-typen.csv übernommen. Das Feld skizze beschreibt die zu erstellende Zeichnung.")

row("2025MgrundlegendAStochastik11", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="1 − (0,4 · 0,8 + 0,42)|Gegenereignis|trifft nicht auf den Charakter",
    voraussetzungen="Pfadsumme als P(C) erkennen|Gegenereignis formulieren",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Onlinespiel", textumfang="mittel",
    gegeben="Baumdiagramm mit P(A) = 0,4, P(C|A) = 0,8, P(B und C) = 0,42; Term 1 − (0,4 · 0,8 + 0,42)",
    gesucht="ein Ereignis im Sachzusammenhang, dessen Wahrscheinlichkeit der Term liefert",
    verfahren="die Klammer ist P(C) als Summe beider Pfade zu C; 1 minus das ist das Gegenereignis",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2025MgrundlegendAStochastik11-a",
    ergebnis="der Spieler trifft im Spiel nicht auf den Charakter (amtlich)",
    zwischenergebnis="Wert 0,26",
    niveau_geschaetzt="II",
    fehlerquelle="das Ereignis auf Startpunkt B einschränken",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. Amtlich. Typ aus 2026-ea-A wiederverwendet.")

# ---- Stochastik 1.2: Glücksrad mit acht Sektoren
RAD_SKIZZE = ("Glücksrad als Kreis mit acht gleich großen Sektoren, im Uhrzeigersinn von oben "
              "beschriftet mit 7, 6, 7, 6, 7, 6, 7, 5 (viermal 7, dreimal 6, einmal 5), Zeiger oben")
row("2025MgrundlegendAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="(3/8)^2|drei von acht Sektoren mit 6|zweimal die 6",
    voraussetzungen="Sektorenanteil als Wahrscheinlichkeit|Potenz als zweimaliges Drehen",
    format="Kurzantwort", operator="Interpretieren Sie", antwort="Text",
    material="Figur", skizze=RAD_SKIZZE, kontext="Glücksrad", textumfang="kurz",
    gegeben="Glücksrad mit acht gleich großen Sektoren, beschriftet mit viermal 7, dreimal 6 und einmal 5; zweimaliges Drehen; Term (3/8)^2",
    gesucht="Bedeutung des Terms im Sachzusammenhang",
    verfahren="3/8 als Wahrscheinlichkeit für die 6 erkennen, Quadrat als zweimal hintereinander",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="der Term gibt die Wahrscheinlichkeit an, bei zweimaligem Drehen zweimal die Zahl 6 zu erzielen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="3/8 der 7 zuordnen, weil sie im Bild am häufigsten auffällt",
    bemerkung="Standardbezug: K3 I, K6 I. Amtlich. Die Zahlen stehen nur in der Abbildung.")

row("2025MgrundlegendAStochastik12", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit einer ungeraden Summe über Pfade berechnen", typ_neben="",
    stichwoerter="ungerade Summe heißt eine gerade und eine ungerade Zahl|P(6) = 3/8|P(ungerade) = 5/8|zwei Pfade|30/64",
    voraussetzungen="Parität der Summe deuten|Pfadregeln mit zwei Reihenfolgen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze=RAD_SKIZZE, kontext="Glücksrad", textumfang="kurz",
    gegeben="Glücksrad mit viermal 7, dreimal 6 und einmal 5 auf acht gleichen Sektoren; zweimaliges Drehen",
    gesucht="Wahrscheinlichkeit, dass die Summe der beiden Zahlen ungerade ist",
    verfahren="die Summe ist ungerade, wenn genau einmal die 6 fällt: 3/8 · 5/8 + 5/8 · 3/8",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="3/8 · 5/8 + 5/8 · 3/8 = 30/64 (amtlich)",
    zwischenergebnis="P(ungerade Zahl) = 5/8|30/64 = 15/32",
    niveau_geschaetzt="II",
    fehlerquelle="nur einen Pfad rechnen (15/64)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 1.3: Schwimmgruppe, Ziehen ohne Zurücklegen
row("2025MgrundlegendAStochastik13", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="20 Kinder, 9 mit Bronze|zwei zufällig ausgewählt|9/20 · 8/19|72/380",
    voraussetzungen="Nenner nach dem ersten Zug verringern",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Schwimmgruppe", textumfang="kurz",
    gegeben="Schwimmgruppe mit 20 Kindern, 9 haben das Schwimmabzeichen Bronze; zwei Kinder werden zufällig ausgewählt",
    gesucht="Wahrscheinlichkeit, dass beide das Abzeichen Bronze haben",
    verfahren="Pfadregel ohne Zurücklegen: 9/20 · 8/19",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="9/20 · 8/19 = 72/380 (amtlich)",
    zwischenergebnis="≈ 0,19",
    niveau_geschaetzt="I",
    fehlerquelle="mit Zurücklegen rechnen (9/20)^2",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendAStochastik13", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypergeometrische Verteilung",
    typ="Hypergeometrischen Term im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="(9 über 2) · (11 über 4) / (20 über 6)|Auswahl von 6 Kindern|genau 2 mit Bronze|Binomialkoeffizienten",
    voraussetzungen="Binomialkoeffizient als Anzahl der Auswahlen|Zähler als Kombination zweier Gruppen deuten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Schwimmgruppe", textumfang="kurz",
    gegeben="20 Kinder, 9 mit Bronze, 11 ohne; Term (9 über 2) · (11 über 4) / (20 über 6)",
    gesucht="Bedeutung des Terms im Sachzusammenhang",
    verfahren="Nenner: alle Auswahlen von 6 aus 20; Zähler: 2 aus den 9 mit Bronze und 4 aus den 11 ohne",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Term gibt die Wahrscheinlichkeit an, dass in einer zufälligen Auswahl von sechs Kindern der Gruppe genau zwei das Abzeichen Bronze haben (amtlich)",
    zwischenergebnis="Wert ≈ 0,31",
    niveau_geschaetzt="II",
    fehlerquelle="„mindestens zwei“ statt „genau zwei“ formulieren",
    bemerkung="Standardbezug: K3 II, K4 II, K6 II. Amtlich. Erste Fundstelle des Themas Hypergeometrische Verteilung.")

# ---- Stochastik 2.1: Binomialverteilung, n ungerade
BIN21_SKIZZE = ("Säulendiagramm P(X = k) für k = 0 bis 22, y-Achse ohne Zahlen; zwei gleich hohe "
                "höchste Säulen bei k = 10 und k = 11, symmetrischer Abfall nach beiden Seiten, "
                "Säulen ab k = 3 bzw. bis k = 18 sichtbar")
row("2025MgrundlegendAStochastik21", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Parität von n aus zwei gleich hohen Säulen der Verteilung begründen", typ_neben="",
    stichwoerter="P(X = 10) = P(X = 11)|zwei Maxima|Erwartungswert n · 0,5 nicht ganzzahlig|n ungerade",
    voraussetzungen="Erwartungswert n · p|Lage des Maximums bei symmetrischer Verteilung",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Diagramm", skizze=BIN21_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="binomialverteilte Zufallsgröße X mit unbekanntem n und p = 0,5, Säulendiagramm mit zwei gleich hohen höchsten Säulen bei 10 und 11; P(X = 10) = P(X = 11)",
    gesucht="Begründung, dass n nicht gerade ist",
    verfahren="das Maximum liegt zwischen 10 und 11, also ist E(X) = n · 0,5 = 10,5 nicht ganzzahlig",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="die Verteilung nimmt bei k = 10 und k = 11 ihren größten Wert an, also ist der Erwartungswert n · 0,5 nicht ganzzahlig und n nicht gerade (amtlich)",
    zwischenergebnis="n = 21",
    niveau_geschaetzt="II",
    fehlerquelle="aus der Symmetrie um 10,5 auf n = 20 schließen",
    bemerkung="Standardbezug: K1 II, K4 I, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt (n = 21 passt zu den Werten in b).")

row("2025MgrundlegendAStochastik21", "b", seite="1", punkte="3", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen", typ_neben="",
    stichwoerter="P(X >= 9) ≈ 0,81|P(X = 12) ≈ 0,14|Symmetrie P(X = 9) = P(X = 12)|P(X >= 11) = 0,5|P(X = 10) ≈ 0,17",
    voraussetzungen="Symmetrie der Verteilung bei p = 0,5|kumulierte Wahrscheinlichkeit zerlegen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=BIN21_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="X binomialverteilt mit p = 0,5, symmetrisch um 10,5; P(X >= 9) ≈ 0,81 und P(X = 12) ≈ 0,14",
    gesucht="Näherungswert für P(X = 10) unter Verwendung dieser Werte",
    verfahren="wegen der Symmetrie P(X = 9) = P(X = 12) ≈ 0,14 und P(X >= 11) = 0,5; P(X = 10) = P(X >= 9) − P(X = 9) − P(X >= 11)",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="2025MgrundlegendAStochastik21-a",
    ergebnis="P(X = 10) ≈ 0,81 − 0,14 − 0,5 = 0,17 (amtlich)",
    zwischenergebnis="P(X = 9) ≈ 0,14|P(X >= 11) = 0,5|exakt für n = 21: 0,168",
    niveau_geschaetzt="III",
    fehlerquelle="P(X >= 11) mit 0,81 − 0,14 verwechseln oder die Symmetrie nicht nutzen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt. Enge und weite Fassung stimmen überein (Symmetrie-Deutung).")

# ---- Stochastik 2.2: Kugelspiel, faires Spiel
row("2025MgrundlegendAStochastik22", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Wahrscheinlichkeit für den ersten Zug angeben", typ_neben="",
    stichwoerter="eine schwarze, w = 3 weiße Kugeln|erster Zug|1/4",
    voraussetzungen="Anteil der günstigen Kugeln",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Behälter mit einer schwarzen und w weißen Kugeln, w >= 2; zweimal Ziehen ohne Zurücklegen; Annahme w = 3",
    gesucht="Wahrscheinlichkeit, dass die schwarze Kugel bereits im ersten Zug entnommen wird",
    verfahren="eine von vier Kugeln ist schwarz",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="1/3 angeben, weil w = 3 ist",
    bemerkung="Standardbezug: K2 I, K3 I, K6 I. Amtlich.")

row("2025MgrundlegendAStochastik22", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Anzahl der Kugeln aus einer Fairnessbedingung bestimmen", typ_neben="",
    stichwoerter="Einsatz 2 €|Auszahlung 8 € beim ersten, 4 € beim zweiten Zug|Erwartungswert der Auszahlung gleich Einsatz|8/(w + 1) + 4 · w/(w + 1) · 1/w = 2|w = 5",
    voraussetzungen="Pfadwahrscheinlichkeiten ohne Zurücklegen mit Parameter|faires Spiel als Erwartungswert gleich Einsatz|Bruchgleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="lang",
    gegeben="Behälter mit einer schwarzen und w weißen Kugeln, w >= 2; zweimal Ziehen ohne Zurücklegen; Einsatz 2 €; Auszahlung 8 € bei schwarz im ersten Zug, 4 € bei schwarz im zweiten Zug, sonst nichts; auf lange Sicht gleichen sich Einsätze und Auszahlungen aus",
    gesucht="zugehöriger Wert von w",
    verfahren="Erwartungswert der Auszahlung 8 · 1/(w + 1) + 4 · w/(w + 1) · 1/w gleich 2 setzen; vereinfacht 12/(w + 1) = 2",
    schritte="3", zahlenraum="Bruch", einheiten="€", abhaengig_von="",
    ergebnis="8 · 1/(w + 1) + 4 · w/(w + 1) · 1/w = 2 ist gleichwertig zu 12 · 1/(w + 1) = 2, also w = 5 (amtlich)",
    zwischenergebnis="P(schwarz im zweiten Zug) = w/(w + 1) · 1/w = 1/(w + 1)",
    niveau_geschaetzt="III",
    fehlerquelle="die Wahrscheinlichkeit für schwarz im zweiten Zug als 1/w ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt. Typname aus abi-typen.csv übernommen (dort 2018-be-gk-B3.1e, gleiche Fertigkeit). Enge und weite Fassung stimmen überein (Deutung der Fairness).")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Tangentengleichung in einem Punkt des Graphen aufstellen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die Gleichung der Tangente an einen Graphen in einem gegebenen Punkt aus der Ableitung als "
     "Steigung und dem Punkt aufstellen.",
     "2025MgrundlegendAAnalysis11-a"),
    ("Parallele Tangente über die Ableitung finden und skizzieren", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die weitere Stelle bestimmen, an der die Ableitung eine vorgegebene Steigung annimmt, und "
     "die dortige Tangente in die Abbildung einzeichnen.",
     "2025MgrundlegendAAnalysis11-b"),
    ("Stammfunktion durch einen vorgegebenen Punkt bestimmen", "Analysis",
     "Stammfunktion und Hauptsatz",
     "Die allgemeine Stammfunktion bilden und die Integrationskonstante so bestimmen, dass der "
     "Graph durch einen gegebenen Punkt verläuft.",
     "2025MgrundlegendAAnalysis12-a"),
    ("Integral null über die Punktsymmetrie begründen", "Analysis", "Flächeninhalt durch Integration",
     "Ohne Rechnung begründen, dass ein Integral über ein zu 0 symmetrisches Intervall null ist, "
     "weil der Integrand nur ungerade Potenzen enthält und sich die orientierten Flächen aufheben.",
     "2025MgrundlegendAAnalysis12-b"),
    ("Nullstelle durch Einsetzen nachweisen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Eine vorgegebene Zahl in den Funktionsterm einsetzen und zeigen, dass der Wert null ist.",
     "2025MgrundlegendAAnalysis13-a"),
    ("Fläche zwischen Graph und Koordinatenachsen berechnen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Inhalt der Fläche, die ein Graph mit beiden Koordinatenachsen einschließt, über das "
     "Integral von 0 bis zur Nullstelle berechnen und das Vorzeichen deuten.",
     "2025MgrundlegendAAnalysis13-b"),
    ("Verschobenen Graphen in die Abbildung skizzieren", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Den um einen Wert in y-Richtung verschobenen Graphen einer gegebenen Funktion in ein "
     "vorhandenes Koordinatensystem einzeichnen.",
     "2025MgrundlegendAAnalysis21-a"),
    ("Verschiebung für die Halbierung einer Fläche über ein Integral bestimmen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Verschiebungswert bestimmen, für den ein Graph eine symmetrische Figur in zwei "
     "inhaltsgleiche Teile teilt, indem die Bedingung als Integral gleich null formuliert wird.",
     "2025MgrundlegendAAnalysis21-b"),
    ("Gleichung aus Differenzenquotient und Ableitung lösen", "Analysis", "Gleichungen lösen",
     "Eine Gleichung, die den Differenzenquotienten zu einem festen Punkt mit der Ableitung "
     "gleichsetzt, als Bruchgleichung lösen.",
     "2025MgrundlegendAAnalysis22-a"),
    ("Ableitung einer quadratischen Funktion angeben", "Analysis", "Ableitungsregeln",
     "Den Term der ersten Ableitung einer quadratischen Funktion mit der Potenzregel angeben.",
     "2025MgrundlegendAAnalysis22-a"),
    ("Gleichung als Tangentenbedingung geometrisch deuten", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die Gleichheit von Differenzenquotient zu einem Punkt und Ableitung als Bedingung deuten, "
     "dass die Tangente durch diesen Punkt verläuft.",
     "2025MgrundlegendAAnalysis22-b"),
    ("Parameter einer Matrix aus einer Matrix-Vektor-Gleichung untersuchen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Untersuchen, ob die Parameter einer Matrix so gewählt werden können, dass M · v = v gilt: "
     "Produkt bilden, Gleichungssystem lösen und die überzählige Gleichung prüfen.",
     "2025MgrundlegendAAGLAA11"),
    ("Lösung eines Gleichungssystems durch Einsetzen nachweisen", "Analytische Geometrie",
     "Lineare Gleichungssysteme",
     "Vorgegebene Werte in alle Gleichungen eines linearen Gleichungssystems einsetzen und die "
     "Gültigkeit zeigen.",
     "2025MgrundlegendAAGLAA12-a"),
    ("Lösbarkeit eines Gleichungssystems mit Parameter beurteilen", "Analytische Geometrie",
     "Lineare Gleichungssysteme",
     "Beurteilen, für welchen Parameterwert ein lineares Gleichungssystem unendlich viele "
     "Lösungen hat, indem eine Gleichung als Kombination der anderen erkannt wird.",
     "2025MgrundlegendAAGLAA12-b"),
    ("Punktprobe an einer Geraden durchführen", "Analytische Geometrie", "Geraden",
     "Prüfen, ob ein Punkt auf einer Geraden in Parameterform liegt, indem der Parameter aus "
     "den Koordinaten bestimmt und auf Widerspruch geprüft wird.",
     "2025MgrundlegendAAGLAA211-a"),
    ("Punkt auf einer Geraden mit vorgegebener Koordinate angeben", "Analytische Geometrie",
     "Geraden",
     "Einen Punkt der Geraden angeben, der eine Koordinatenbedingung erfüllt, über den passenden "
     "Parameterwert.",
     "2025MgrundlegendAAGLAA211-a"),
    ("Orthogonalität zweier Geraden über das Skalarprodukt untersuchen", "Analytische Geometrie",
     "Orthogonalität",
     "Prüfen, ob zwei Geraden senkrecht zueinander verlaufen, indem das Skalarprodukt ihrer "
     "Richtungsvektoren gebildet wird; der Richtungsvektor einer achsenparallelen Geraden ist "
     "ein Einheitsvektor.",
     "2025MgrundlegendAAGLAA211-b"),
    ("Lage zweier Punkte zu einer Koordinatenebene begründen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Aus dem Vorzeichen einer Koordinate begründen, auf welcher Seite einer Koordinatenebene "
     "Punkte liegen.",
     "2025MgrundlegendAAGLAA212-a"),
    ("Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen",
     "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Die Höhe eines gleichschenkligen Dreiecks als Vektor von der Basismitte zur Spitze "
     "bestimmen und den Flächeninhalt aus Basis und Höhe berechnen.",
     "2025MgrundlegendAAGLAA212-b"),
    ("Spiegelpunkt an einem Punkt bestimmen", "Analytische Geometrie", "Spiegelung",
     "Den Bildpunkt einer Punktspiegelung als Spiegelzentrum plus Verbindungsvektor berechnen.",
     "2025MgrundlegendAAGLAA213-a"),
    ("Vektor als Normalenvektor einer Ebene über Kollinearität nachweisen", "Analytische Geometrie",
     "Lagebeziehungen",
     "Zeigen, dass ein gegebener Vektor Normalenvektor einer Ebene in Koordinatenform ist, weil "
     "er ein Vielfaches des ablesbaren Normalenvektors ist.",
     "2025MgrundlegendAAGLAA213-b"),
    ("Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen",
     "Analytische Geometrie", "Orthogonalität",
     "Zeigen, dass ein Vektor senkrecht auf einer Ebene in Parameterform steht, indem die "
     "Skalarprodukte mit beiden Spannvektoren null ergeben.",
     "2025MgrundlegendAAGLAA221-a"),
    ("Punkt mit vorgegebenem Abstand zu seinem Spiegelbild an einer Ebene bestimmen",
     "Analytische Geometrie", "Spiegelung",
     "Einen Punkt bestimmen, dessen Spiegelbild an einer Ebene einen vorgegebenen Abstand hat: "
     "halber Abstand zur Ebene, entlang des normierten Normalenvektors von einem Ebenenpunkt "
     "aus abtragen.",
     "2025MgrundlegendAAGLAA221-b"),
    ("Baumdiagramm zu einer zweistufigen Situation erstellen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Aus Sachangaben ein beschriftetes zweistufiges Baumdiagramm zeichnen, wobei fehlende "
     "Astwahrscheinlichkeiten aus Pfadwahrscheinlichkeiten und Gegenwahrscheinlichkeiten "
     "berechnet werden.",
     "2025MgrundlegendAStochastik11-a"),
    ("Wahrscheinlichkeit einer ungeraden Summe über Pfade berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit, dass die Summe zweier Ergebnisse ungerade ist, über die Pfade mit "
     "genau einem geraden Ergebnis berechnen.",
     "2025MgrundlegendAStochastik12-b"),
    ("Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die Wahrscheinlichkeit, dass zwei ohne Zurücklegen gezogene Objekte beide eine Eigenschaft "
     "haben, mit der Pfadregel und verringertem Nenner berechnen.",
     "2025MgrundlegendAStochastik13-a"),
    ("Hypergeometrischen Term im Sachzusammenhang deuten", "Stochastik",
     "Hypergeometrische Verteilung",
     "Einen Quotienten aus Produkten von Binomialkoeffizienten als Wahrscheinlichkeit einer "
     "Auswahl ohne Zurücklegen mit vorgegebener Trefferzahl deuten.",
     "2025MgrundlegendAStochastik13-b"),
    ("Parität von n aus zwei gleich hohen Säulen der Verteilung begründen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Aus zwei gleich hohen höchsten Säulen einer Binomialverteilung mit p = 0,5 begründen, dass "
     "der Erwartungswert nicht ganzzahlig und n ungerade ist.",
     "2025MgrundlegendAStochastik21-a"),
    ("Einzelwahrscheinlichkeit aus Symmetrie und kumulierten Werten berechnen", "Stochastik",
     "Binomialverteilung",
     "Eine Einzelwahrscheinlichkeit einer symmetrischen Binomialverteilung aus gegebenen "
     "kumulierten und einzelnen Werten über Symmetrie und Zerlegung näherungsweise berechnen.",
     "2025MgrundlegendAStochastik21-b"),
    ("Laplace-Wahrscheinlichkeit für den ersten Zug angeben", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die Wahrscheinlichkeit für ein Ergebnis beim ersten Ziehen als Anteil der günstigen Objekte "
     "angeben.",
     "2025MgrundlegendAStochastik22-a"),
    ("Anzahl der Kugeln aus einer Fairnessbedingung bestimmen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die Gewinnwahrscheinlichkeiten eines Urnenspiels in Abhängigkeit von der Kugelzahl "
     "aufstellen, die Fairnessbedingung als Erwartungswert gleich Einsatz formulieren und die "
     "entstehende Gleichung lösen.",
     "2025MgrundlegendAStochastik22-b"),
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
