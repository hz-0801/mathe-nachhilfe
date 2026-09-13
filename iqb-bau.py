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
    "stapel": "2024-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2024MerhoehtAAnalysis11": 5,
        "2024MerhoehtAAnalysis12": 5,
        "2024MerhoehtAAnalysis13": 5,
        "2024MerhoehtAAnalysis21": 5,
        "2024MerhoehtAAnalysis22": 5,
        "2024MerhoehtAAnalysis23": 5,
        "2024MerhoehtAAGLAA11": 5,
        "2024MerhoehtAAGLAA121": 5,
        "2024MerhoehtAAGLAA122": 5,
        "2024MerhoehtAAGLAA211": 5,
        "2024MerhoehtAAGLAA212": 5,
        "2024MerhoehtAAGLAA221": 5,
        "2024MerhoehtAAGLAA222": 5,
        "2024MerhoehtAAGLAA223": 5,
        "2024MerhoehtAStochastik11": 5,
        "2024MerhoehtAStochastik12": 5,
        "2024MerhoehtAStochastik21": 5,
        "2024MerhoehtAStochastik22": 5,
        "2024MerhoehtAStochastik23": 5,
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
# niveau_geschaetzt nach der Deutungsliste (a)–(d) in iqb.md § 7 v0.5 (erster Stapel mit der
# geänderten Liste); bei III nennt bemerkung den Eintrag („Eichregel: …").

# ---- Analysis 1.1: 2 sin(x/2), Integral am Graphen, Tangente im Ursprung
SIN_SKIZZE = ("Koordinatensystem mit x-Achse von −3 bis 13 und y-Achse von −3 bis 3, Gitter; Graph G_f "
              "(beschriftet links unten) von f(x) = 2 · sin(x/2): durch den Ursprung steigend, Hochpunkt "
              "(π; 2) bei etwa 3,1, Nullstelle bei 2π ≈ 6,3, Tiefpunkt (3π; −2) bei etwa 9,4, Nullstelle "
              "bei 4π ≈ 12,6; links Tiefpunkt bei −π")
row("2024MerhoehtAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Vorzeichen eines Integrals am Graphen beurteilen", typ_neben="",
    stichwoerter="Integral von −2 bis 8|Fläche oberhalb (0 bis 2π) größer als unterhalb (−2 bis 0 und 2π bis 8)|Wert nicht negativ",
    voraussetzungen="Integral als orientierten Flächeninhalt deuten|Flächenstücke am Graphen vergleichen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 2 · sin(1/2 x), definiert in IR, Graph G_f in der Abbildung; Integral von −2 bis 8 über f(x) dx",
    gesucht="Beurteilung mithilfe der Abbildung, ob der Wert des Integrals negativ ist",
    verfahren="die Fläche zwischen G_f, x-Achse, x = −2 und x = 8 zerlegen: der Teil oberhalb der Achse (0 bis 2π) ist größer als die beiden Teile unterhalb",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="der Graph G_f, die x-Achse und die Geraden x = −2 und x = 8 schließen eine Fläche ein, deren Teil unterhalb der x-Achse einen kleineren Inhalt hat als der Teil oberhalb; der Wert des Integrals ist nicht negativ (amtlich)",
    zwischenergebnis="Wert ≈ 4,8",
    niveau_geschaetzt="II",
    fehlerquelle="nur den Teil rechts von 2π ansehen und „negativ“ antworten",
    bemerkung="Standardbezug: K1 I, K2 II, K4 I. Amtlich, eigene Rechnung bestätigt. Beurteilung als Flächenvergleich, kein Eintrag der Deutungsliste (Stand v0.5).")

row("2024MerhoehtAAnalysis11", "b", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente im Ursprung als Gerade durch zwei Punkte nachweisen", typ_neben="",
    stichwoerter="f'(x) = cos(x/2)|f'(0) = 1, f(0) = 0|Tangente y = x|Gerade durch (−1; −1) und (1; 1) ist y = x",
    voraussetzungen="Kettenregel mit linearer innerer Funktion|Tangentengleichung|Gerade durch zwei Punkte",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="Koordinatensystem", skizze=SIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 2 · sin(1/2 x); Aussage: die Tangente an G_f im Koordinatenursprung ist die Gerade durch (−1; −1) und (1; 1)",
    gesucht="rechnerischer Nachweis der Aussage",
    verfahren="f' bilden, Steigung f'(0) und Punkt (0; 0) liefern y = x; die Gerade durch die beiden Punkte hat dieselbe Gleichung",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="wegen f'(x) = cos(1/2 x), f'(0) = 1 und f(0) = 0 hat die Tangente im Ursprung die Gleichung y = x, die auch die Gerade durch die beiden gegebenen Punkte beschreibt (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die innere Ableitung 1/2 vergessen und f'(0) = 2 erhalten",
    bemerkung="Standardbezug: K1 I, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2.")

# ---- Analysis 1.2: Schar a x³ + a x²
row("2024MerhoehtAAnalysis12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben", typ_neben="",
    stichwoerter="f_a(1) = a + a = 2a|2a = 6|a = 3",
    voraussetzungen="Punkt in den Term einsetzen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = a · x³ + a · x², definiert in IR, a > 0",
    gesucht="Wert von a, sodass (1; 6) auf dem Graphen von f_a liegt",
    verfahren="x = 1 einsetzen und nach a auflösen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="a = 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="6 = a · 1³ ansetzen und a = 6 angeben",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt. Thema Funktionsscharen und Ortskurven (nicht für das grundlegende Niveau in BE und BB).")

row("2024MerhoehtAAnalysis12", "b", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen", typ_neben="",
    stichwoerter="f_a(x) = a x² (x + 1)|Nullstellen −1 und 0|Integral von −1 bis 0|Stammfunktion 1/4 a x⁴ + 1/3 a x³|Inhalt a/12",
    voraussetzungen="Nullstellen durch Ausklammern mit Parameter|Potenzregel der Integration mit Parameter|Vorzeichen des Integranden prüfen",
    format="Rechnung", operator="Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = a · x³ + a · x² mit a > 0; der Graph schließt mit der x-Achse eine Fläche ein",
    gesucht="Inhalt dieser Fläche in Abhängigkeit von a",
    verfahren="Nullstellen −1 und 0 bestimmen, das Integral über [−1; 0] mit der Stammfunktion auswerten (dort ist f_a ≥ 0)",
    schritte="3", zahlenraum="Bruch|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f_a(x) = 0 ⇔ a x² (x + 1) = 0 ⇔ x = −1 oder x = 0; Integral von −1 bis 0 über (a x³ + a x²) dx = [1/4 a x⁴ + 1/3 a x³] von −1 bis 0 = 1/12 a (amtlich)",
    zwischenergebnis="Wert an der Stelle −1: a/4 − a/3 = −a/12",
    niveau_geschaetzt="II",
    fehlerquelle="das Vorzeichen bei der Auswertung an der unteren Grenze verlieren (−a/12 als Inhalt)",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Routinekette mit mitgeführtem Parameter, kein Eintrag der Deutungsliste.")

# ---- Analysis 1.3: Schar x e^(ax)
XEAX_SKIZZE = ("zwei Abbildungen ohne Skalen, je ein Koordinatensystem: Abb. 1 zeigt einen Graphen, der von links "
               "unten steil durch den Ursprung steigt, rechts einen Hochpunkt hat und dann flach gegen die x-Achse "
               "abfällt; Abb. 2 zeigt einen Graphen, der von links flach knapp unter der x-Achse kommt, einen "
               "Tiefpunkt links vom Ursprung hat, durch den Ursprung steigt und rechts steil nach oben verläuft")
row("2024MerhoehtAAnalysis13", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Vorzeichen der Funktionswerte einer Schar begründen", typ_neben="",
    stichwoerter="f_a(x) = x · e^(ax)|e^(ax) > 0|Produkt mit negativem x negativ|unterhalb der x-Achse für x < 0",
    voraussetzungen="Positivität der e-Funktion|Vorzeichen eines Produkts",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=XEAX_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = x · e^(a · x), definiert in IR, a ≠ 0; jede f_a hat genau eine Extremstelle",
    gesucht="Begründung, dass der Graph von f_a für x < 0 unterhalb der x-Achse verläuft",
    verfahren="Vorzeichen der beiden Faktoren betrachten",
    schritte="1", zahlenraum="negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="wegen e^(a · x) > 0 sind die Funktionswerte x · e^(a · x) von f_a für negative x ebenfalls negativ (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="das Vorzeichen von a für ausschlaggebend halten",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich. Die Abbildungen gehören zu Teilaufgabe b.")

row("2024MerhoehtAAnalysis13", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen", typ_neben="",
    stichwoerter="für a > 0 strebt f_a(x) gegen +∞ für x → +∞|Abb. 1 fällt rechts gegen 0|genau eine Extremstelle|Abb. 2 gehört zu a > 0",
    voraussetzungen="Grenzverhalten von x · e^(ax) nach dem Vorzeichen von a|Anzahl der Extrempunkte am Graphen zählen",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=XEAX_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = x · e^(a · x), a ≠ 0, genau eine Extremstelle je Funktion; Abbildungen 1 und 2 zeigen je einen Graphen der Schar, einer davon für positives a",
    gesucht="Entscheidung, welche Abbildung den Graphen zu positivem a zeigt, mit Begründung",
    verfahren="für a > 0 wächst f_a für x → +∞ unbeschränkt; Abbildung 1 fällt rechts gegen die Achse und müsste dazu einen weiteren Extrempunkt haben, was ausgeschlossen ist",
    schritte="2", zahlenraum="Potenz", einheiten="", abhaengig_von="2024MerhoehtAAnalysis13-a",
    ergebnis="Abbildung 2; wegen lim f_a(x) = +∞ für x → +∞ bei a > 0 ist Abbildung 1 aufgrund des Fehlens weiterer Extrempunkte ausgeschlossen (amtlich)",
    zwischenergebnis="Extremstelle bei −1/a",
    niveau_geschaetzt="II",
    fehlerquelle="Abbildung 1 wählen, weil der Graph dort für x > 0 zunächst steigt",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt. Verkettung Grenzverhalten und Extremstellenzahl, kein Eintrag der Deutungsliste.")

# ---- Analysis 2.1: Schar a x², Tangente (Schar-Fassung von 2024-ga-A 2.1)
PAR3_SKIZZE = ("Koordinatensystem mit x-Achse von −4 bis 7 (Markierungen in Zweierschritten) und y-Achse von "
               "−10 bis 12, Gitter; Parabel f_1/2(x) = 1/2 x² mit Scheitel im Ursprung durch (4; 8) (markiert) und "
               "(−4; 8); Tangente t im Punkt (4; 8): Gerade mit Steigung 4 durch (2; 0) und (0; −8)")
row("2024MerhoehtAAnalysis21", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung aus der Abbildung ablesen", typ_neben="",
    stichwoerter="Nullstelle der Tangente bei 2|y-Achsenabschnitt −8|Steigung 4|y = 4x − 8",
    voraussetzungen="Geradengleichung aus zwei Gitterpunkten ablesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Koordinatensystem", skizze=PAR3_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = a · x² für positives a; Graph von f_1/2 und Tangente t im Punkt (4; f_1/2(4)) in der Abbildung",
    gesucht="Gleichung von t anhand der Abbildung",
    verfahren="zwei Gitterpunkte der Tangente ablesen, etwa (2; 0) und (4; 8)",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="y = 4x − 8 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Steigung als 2 ablesen",
    bemerkung="Standardbezug: K2 I, K4 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2024-ga-A wiederverwendet; die Aufgabe ist die Schar-Fassung von 2024-ga-A Analysis 2.1 mit derselben Abbildung.")

row("2024MerhoehtAAnalysis21", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="y-Achsenabschnitt der Tangente allgemein nachweisen", typ_neben="",
    stichwoerter="Tangente in (u; f_a(u))|m = f_a'(u) = 2au|a u² = 2au · u + n|n = −a u² = −f_a(u)",
    voraussetzungen="Tangentengleichung mit allgemeiner Stelle u und Scharparameter a|Ableitung|nach n auflösen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Koordinatensystem", skizze=PAR3_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = a · x², a > 0; für jedes reelle u die Tangente an den Graphen von f_a im Punkt (u; f_a(u))",
    gesucht="Nachweis, dass diese Tangente die y-Achse im Punkt (0; −f_a(u)) schneidet",
    verfahren="Ansatz y = mx + n mit m = f_a'(u) = 2au, Berührpunkt einsetzen, n bestimmen",
    schritte="3", zahlenraum="Potenz", einheiten="", abhaengig_von="2024MerhoehtAAnalysis21-a",
    ergebnis="Gleichung der Tangente y = mx + n; f_a(u) = a · u², m = f_a'(u) = 2a · u; a · u² = 2a · u · u + n ⇔ n = −a · u², d. h. n = −f_a(u) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur a = 1/2 und u = 4 aus a nachrechnen",
    bemerkung="Standardbezug: K1 III, K2 II, K5 III. Amtlich, eigene Rechnung bestätigt. Typ aus 2024-ga-A wiederverwendet (dort ohne Scharparameter). Eichregel: (c) allgemeiner Nachweis mit Parameter, Beziehung n = −f_a(u) hergeleitet.")

# ---- Analysis 2.2: Rechteck aus Nullstellen und Normale (ungegliedert)
RECHT_SKIZZE = ("Koordinatensystem ohne Skalen; Graph G von f(x) = x³ − 2a x² + a² x: durch den Ursprung steigend, "
                "Hochpunkt zwischen 0 und a, Berührpunkt mit der x-Achse in (a; 0), danach steil steigend; Gerade h "
                "(beschriftet) durch den Ursprung mit kleiner negativer Steigung, senkrecht zur Tangente in O")
row("2024MerhoehtAAnalysis22", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Flächeninhalt eines Rechtecks aus Nullstellen und Normale als parameterunabhängig nachweisen", typ_neben="",
    stichwoerter="f(x) = x (x − a)²|Nullstellen 0 und a als Rechteckecken|h senkrecht zur Tangente in O: Steigung −1/f'(0) = −1/a²|h(x) = −x/a²|Diagonale auf h: vierte Ecke (a; −1/a)|Fläche a · 1/a = 1",
    voraussetzungen="Nullstellen mit Parameter|Normale als Gerade mit Steigung −1/m|Rechteck aus zwei Ecken und Diagonalenrichtung konstruieren|Fläche mit Parameter vereinfachen",
    format="Zeichnen|Begründung", operator="Skizzieren Sie|Zeigen Sie", antwort="Grafik|Text",
    material="Koordinatensystem", skizze=RECHT_SKIZZE, kontext="ohne", textumfang="lang",
    gegeben="a > 0; f(x) = x³ − 2a x² + a² x mit Graph G, Gerade h durch den Ursprung senkrecht zur Tangente an G im Ursprung; G berührt die x-Achse in (a; 0); Rechteck mit den gemeinsamen Punkten von G und x-Achse als benachbarten Ecken und einer Diagonale auf h",
    gesucht="Skizze des Rechtecks in der Abbildung|Nachweis, dass sein Flächeninhalt nicht von a abhängt",
    verfahren="f'(0) = a² liefert die Steigung −1/a² von h; das Rechteck hat die Ecken (0; 0), (a; 0) und die Höhe |h(a)| = 1/a unterhalb der Achse; Fläche a · 1/a",
    schritte="4", zahlenraum="Bruch|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 3x² − 4ax + a²; die Steigung von h beträgt −1/f'(0) = −1/a², also h(x) = −1/a² · x; Flächeninhalt des Rechtecks |h(a)| · a = 1/a · a = 1; Rechteck mit den Ecken (0; 0), (a; 0), (a; −1/a), (0; −1/a) unterhalb der x-Achse (amtlich)",
    zwischenergebnis="f'(0) = a²",
    niveau_geschaetzt="III",
    fehlerquelle="h als Tangente statt als Normale ansetzen (Steigung a²)",
    bemerkung="Standardbezug: K1 II, K2 III, K4 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Eichregel: (a) geometrische Bedingungen (Normale, Diagonale auf h) in Gleichungen übersetzen und (c) Nachweis für alle a.")

# ---- Analysis 2.3: hundertste Ableitung (ungegliedert)
row("2024MerhoehtAAnalysis23", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Verschiebung zwischen Graph und hundertster Ableitung berechnen", typ_neben="",
    stichwoerter="f'(x) = 2e^(2x), f(0) = 1, also f(x) = e^(2x)|f^(100)(x) = 2^100 · e^(2x)|f(x − c) = f^(100)(x)|e^(−2c) = 2^100|c = −1/2 · ln(2^100) = −50 · ln 2",
    voraussetzungen="Stammfunktion mit Anfangswert|Ableitung von e^(2x) wiederholt|Verschiebung in x-Richtung als f(x − c)|Exponentialgleichung mit ln lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f in IR definiert mit f'(x) = 2 · e^(2x) und f(0) = 1; f^(100) ist die hundertste Ableitungsfunktion; der Graph von f^(100) entsteht aus dem Graphen von f durch eine Verschiebung in x-Richtung",
    gesucht="um wie viele Einheiten der Graph von f dazu in x-Richtung zu verschieben ist",
    verfahren="f = e^(2x) rekonstruieren, f^(100) = 2^100 · e^(2x) erkennen, die Verschiebungsgleichung f(x − c) = f^(100)(x) nach c auflösen",
    schritte="4", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(x) = e^(2x); f^(100)(x) = 2^100 · e^(2x); f(x − c) = f^(100)(x) ⇔ e^(2x) · e^(−2c) = 2^100 · e^(2x) ⇔ e^(−2c) = 2^100 ⇔ c = −1/2 · ln(2^100) (amtlich)",
    zwischenergebnis="c = −50 · ln 2 ≈ −34,66, Verschiebung um etwa 34,66 nach links",
    niveau_geschaetzt="III",
    fehlerquelle="f^(100) = 2^100 · e^(2x) als Streckung deuten und keine Verschiebung finden",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.3). Eichregel: (a) Verschiebung als Gleichung f(x − c) = f^(100)(x) übersetzen.")

# ---- AG/LA (A1) 1: zweistufige Verflechtung (Datei mit drei Seiten, b auf Seite 2)
row("2024MerhoehtAAGLAA11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Rohstoffbedarf über die Verflechtungsmatrix berechnen", typ_neben="",
    stichwoerter="r = ((5; 4), (12; 10)) · e|e = (2; 2)|r = (18; 44)",
    voraussetzungen="Matrix-Vektor-Produkt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion", textumfang="lang",
    gegeben="Produktionsprozess mit r = ((5; 4), (12; 10)) · e (Rohstoffe aus Endprodukten) und z = ((2; 1), (1; 1), (2; 2)) · e (Zwischenprodukte aus Endprodukten); Mengeneinheiten",
    gesucht="Mengeneinheiten jedes Rohstoffs für 2 ME des ersten und 2 ME des zweiten Endprodukts",
    verfahren="Matrix mit (2; 2) multiplizieren",
    schritte="1", zahlenraum="ganz", einheiten="ME", abhaengig_von="",
    ergebnis="(r1; r2) = ((5; 4), (12; 10)) · (2; 2) = (18; 44) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Zwischenproduktmatrix verwenden",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Einzige Aufgabe der Gruppe 1 (aufgabe „1“). Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand). Datei mit drei Seiten.")

row("2024MerhoehtAAGLAA11", "b", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtungsmatrix aus Sachbedingungen und Matrixprodukt bestimmen", typ_neben="",
    stichwoerter="r = M · z mit M = ((a; a; a), (2; 2; b))|M · Z = R|((a; a; a), (2; 2; b)) · ((2; 1), (1; 1), (2; 2)) = ((5; 4), (12; 10))|5a = 5, 6 + 2b = 12|a = 1, b = 3",
    voraussetzungen="Sachbedingungen als Matrixform lesen|Verkettung r = M · z = M · Z · e|Matrizenprodukt mit Variablen|Koeffizientenvergleich",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Produktion", textumfang="lang",
    gegeben="r = ((5; 4), (12; 10)) · e und z = ((2; 1), (1; 1), (2; 2)) · e; für je 1 ME der drei Zwischenprodukte ist gleich viel des ersten Rohstoffs nötig; für 1 ME des ersten und des zweiten Zwischenprodukts je 2 ME des zweiten Rohstoffs",
    gesucht="Matrix M mit r = M · z",
    verfahren="M mit den Unbekannten a (erste Zeile) und b ansetzen, M · Z = R lösen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2024MerhoehtAAGLAA11-a",
    ergebnis="M hat die Form ((a; a; a), (2; 2; b)); ((a; a; a), (2; 2; b)) · ((2; 1), (1; 1), (2; 2)) = ((5; 4), (12; 10)) liefert 5a = 5 ⇔ a = 1 sowie 6 + 2b = 12 ⇔ b = 3 (amtlich)",
    zwischenergebnis="M = ((1; 1; 1), (2; 2; 3))",
    niveau_geschaetzt="II",
    fehlerquelle="M als 3×2-Matrix ansetzen",
    bemerkung="Standardbezug: K2 II, K3 II, K4 I, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2. Sachbedingungen wörtlich, kein Eintrag der Deutungsliste.")

# ---- AG/LA (A1) 2.1: Permutationsmatrix (ungegliedert)
row("2024MerhoehtAAGLAA121", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Wirkung einer Permutationsmatrix beschreiben und Einträge aus M · A · M = A bestimmen", typ_neben="",
    stichwoerter="M = ((1; 0; 0), (0; 0; 1), (0; 1; 0))|von rechts: letzte beide Spalten vertauscht|von links: letzte beide Zeilen vertauscht|A bleibt bei beiden Vertauschungen gleich|a = 2, b = 1, 2c = c − a, 2d − b = d|c = −2, d = 1",
    voraussetzungen="Matrizenprodukt mit einer Vertauschungsmatrix|Bedingung M · A · M = A strukturell deuten|lineare Gleichungen",
    format="Kurzantwort|Rechnung", operator="Beschreiben Sie|Bestimmen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="M = ((1; 0; 0), (0; 0; 1), (0; 1; 0)); A = ((0; a; 2), (b; 2c; d), (1; 2d − b; c − a)) mit reellen a, b, c, d",
    gesucht="Beschreibung der Änderung einer beliebigen 3×3-Matrix bei Multiplikation mit M von rechts bzw. von links|Werte a, b, c, d mit M · A · M = A",
    verfahren="M vertauscht die letzten beiden Spalten (rechts) bzw. Zeilen (links); A muss unter beiden Vertauschungen unverändert bleiben, Einträge vergleichen",
    schritte="4", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="die Multiplikation mit M von rechts vertauscht die letzten beiden Spalten, von links die letzten beiden Zeilen; erfüllt A die Eigenschaft, ändert sie sich beim Vertauschen der letzten beiden Zeilen und anschließend der letzten beiden Spalten nicht; es folgen a = 2 und b = 1 sowie 2c = c − a und 2d − b = d, d. h. c = −2 und d = 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="M · A · M vollständig ausmultiplizieren und sich verrechnen",
    bemerkung="Standardbezug: K1 III, K2 II, K4 II, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.1). Eichregel: (a) Strukturbedingung (Invarianz unter Vertauschung) in Gleichungen übersetzen.")

# ---- AG/LA (A1) 2.2: Mischungsaufgabe
row("2024MerhoehtAAGLAA122", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lineares Gleichungssystem im Sachzusammenhang interpretieren", typ_neben="",
    stichwoerter="(1) 5x + 10y + 20z = 15|(2) x + y + z = 1|x, y, z Anteile der Säfte|Orangensaftanteile 5 %, 10 %, 20 % ergeben 15 %",
    voraussetzungen="Variablen als Anteile deuten|Mischungsgleichung lesen",
    format="Kurzantwort", operator="Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Fruchtsaftmischung", textumfang="mittel",
    gegeben="LGS (1) 5x + 10y + 20z = 15, (2) x + y + z = 1; Mischung aus F_x (5 % Orangensaft), F_y (10 %), F_z (20 %) zu 15 %",
    gesucht="Interpretation des Gleichungssystems im Sachzusammenhang",
    verfahren="(2) als Summe der Anteile gleich 1, (1) als Bilanz der Orangensaftanteile lesen",
    schritte="1", zahlenraum="ganz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Gleichung (1) stellt die Orangensaftanteile der drei Fruchtsäfte mit dem Anteil 15 % des neuen Fruchtsafts in Beziehung, wobei x, y und z für die Anteile von F_x, F_y bzw. F_z am neuen Saft stehen (Gleichung (2)) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="x, y, z als Prozentzahlen der Orangensaftanteile deuten",
    bemerkung="Standardbezug: K3 II, K4 II, K6 II. Amtlich. Einfache Deutung, kein Eintrag der Deutungsliste.")

row("2024MerhoehtAAGLAA122", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Aussage über die Lösungsmenge eines Gleichungssystems mit Nichtnegativität nachweisen", typ_neben="",
    stichwoerter="Lösungsmenge (−1 + 2s; 2 − 3s; s)|2x ≤ z ⇔ 2(−1 + 2s) ≤ s ⇔ s ≤ 2/3|y ≥ 0 ⇒ 2 − 3s ≥ 0 ⇒ s ≤ 2/3|Aussage wahr",
    voraussetzungen="Aussage in eine Ungleichung übersetzen|Anteile sind nichtnegativ|Ungleichungen mit Parameter",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Fruchtsaftmischung", textumfang="mittel",
    gegeben="Lösungsmenge des LGS {(−1 + 2s; 2 − 3s; s) | s reell}; Aussage: der Anteil von F_z am neuen Saft ist mindestens doppelt so groß wie der von F_x",
    gesucht="Nachweis, dass die Aussage wahr ist",
    verfahren="2x ≤ z in s ausdrücken; die Bedingung y ≥ 0 (Anteil) liefert dieselbe Schranke s ≤ 2/3",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2024MerhoehtAAGLAA122-a",
    ergebnis="es gilt 2x ≤ z ⇔ 2 · (−1 + 2s) ≤ s ⇔ s ≤ 2/3; wegen y ≥ 0 ⇒ 2 − 3s ≥ 0 ⇒ s ≤ 2/3 folgt die Behauptung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Nichtnegativität von y nicht heranziehen und die Aussage für falsch halten",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Sachbedingung (Anteile nichtnegativ) in eine Ungleichung übersetzen.")

# ---- AG/LA (A2) 1.1: Parallelogramm, Projektion (Datei mit drei Seiten, b auf Seite 2)
PARA_SKIZZE = ("Koordinatensystem x1 von −5 bis 5 und x2 von −3 bis 5, Gitter, ohne eingezeichnete Punkte; "
               "zu ergänzen: B'(4; 3), C'(2; 4), M'(3; 2), A'(4; 0), D'(2; 1) und das Parallelogramm A'B'C'D' mit Diagonalen")
row("2024MerhoehtAAGLAA211", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Projektion eines Parallelogramms in eine Koordinatenebene einzeichnen", typ_neben="",
    stichwoerter="Verschiebung parallel zur x3-Achse: x3-Koordinate weglassen|B'(4; 3), C'(2; 4), M'(3; 2)|A' = 2M' − C' = (4; 0), D' = 2M' − B' = (2; 1)",
    voraussetzungen="Projektion in die x1x2-Ebene als Weglassen der dritten Koordinate|Diagonalenschnittpunkt als Mittelpunkt|Punktspiegelung am Mittelpunkt",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=PARA_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="B(4; 3; 12), C(2; 4; 10) Eckpunkte eines Parallelogramms ABCD mit Diagonalenschnittpunkt M(3; 2; 1); alle Punkte werden parallel zur x3-Achse in die x1x2-Ebene verschoben",
    gesucht="A'B'C'D' und M' in der Abbildung",
    verfahren="B', C', M' aus den ersten beiden Koordinaten eintragen; A' und D' durch Spiegelung von C' und B' an M'",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="B'(4; 3), C'(2; 4), M'(3; 2), A'(4; 0), D'(2; 1) und das Parallelogramm A'B'C'D' mit den Diagonalen durch M' (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="A' und D' durch Verschieben von B' und C' um denselben Vektor statt durch Punktspiegelung an M' bestimmen",
    bemerkung="Standardbezug: K2 II, K4 I. Amtlich, eigene Rechnung bestätigt. Datei mit drei Seiten; der Erwartungshorizont zeigt die Zeichnung. Das Feld skizze beschreibt das Material.")

row("2024MerhoehtAAGLAA211", "b", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Winkelart aus dem Vorzeichen des Skalarprodukts beurteilen", typ_neben="",
    stichwoerter="CM = (1; −2; −9), CB = (2; −1; 2)|CM · CB = 2 + 2 − 18 = −14|negativ, Winkel nicht kleiner als 90°",
    voraussetzungen="Skalarprodukt|Vorzeichen des Skalarprodukts als Winkelmaß",
    format="Rechnung", operator="Berechnen Sie|Beurteilen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="CM = (1; −2; −9) und CB = (2; −1; 2) (aus B(4; 3; 12), C(2; 4; 10), M(3; 2; 1))",
    gesucht="Wert des Skalarprodukts CM · CB|Beurteilung, ob der Winkel zwischen CM und CB kleiner als 90° ist",
    verfahren="Skalarprodukt ausrechnen, Vorzeichen deuten",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="aus (1; −2; −9) · (2; −1; 2) = −14 < 0 folgt, dass der Winkel zwischen den Vektoren nicht kleiner als 90° ist (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="aus −14 auf einen Winkel von 90° oder auf „kleiner“ schließen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2.")

# ---- AG/LA (A2) 1.2: Ebenenschar
row("2024MerhoehtAAGLAA212", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharparameter für Parallelität von Ebene und Gerade ermitteln", typ_neben="",
    stichwoerter="E_a: 2a x1 − 4 x2 + (a − 2) x3 = 12|Normalenvektor (2a; −4; a − 2)|Richtungsvektor (−1; 0; 1)|Skalarprodukt −2a + a − 2 = 0|a = −2",
    voraussetzungen="Parallelität Ebene–Gerade als Normalenvektor senkrecht zum Richtungsvektor|Skalarprodukt mit Parameter",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Ebenenschar E_a: 2a · x1 − 4 · x2 + (a − 2) · x3 = 12, a reell; Gerade x = (0; 1; 1) + b · (−1; 0; 1)",
    gesucht="Wert von a, für den E_a parallel zur Geraden verläuft",
    verfahren="Skalarprodukt von Normalen- und Richtungsvektor gleich null setzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(2a; −4; a − 2) · (−1; 0; 1) = 0 ⇔ −2a + a − 2 = 0 ⇔ a = −2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den Stützpunkt der Geraden in die Ebenengleichung einsetzen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Thema Scharen von Geraden und Ebenen (nicht für das grundlegende Niveau in BE und BB).")

row("2024MerhoehtAAGLAA212", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Zugehörigkeit einer Ebene zu einer Schar prüfen", typ_neben="",
    stichwoerter="6 x1 − 8 x2 + x3 = 24|Normalenvektoren kollinear: (2a; −4; a − 2) = k · (6; −8; 1)|k = 0,5|2a = 3 und a − 2 = 0,5 widersprechen sich|nicht zur Schar",
    voraussetzungen="gleiche Ebene heißt Vielfaches der Koordinatengleichung|Gleichungssystem für a und k auf Widerspruch prüfen",
    format="Rechnung", operator="Prüfen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar E_a: 2a · x1 − 4 · x2 + (a − 2) · x3 = 12; Ebene 6 x1 − 8 x2 + x3 = 24",
    gesucht="Prüfung, ob die Ebene zur Schar gehört",
    verfahren="Normalenvektor der Schar als Vielfaches k des gegebenen ansetzen; aus der zweiten Koordinate k = 0,5, die übrigen Gleichungen für a widersprechen sich",
    schritte="3", zahlenraum="ganz|dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="(2a; −4; a − 2) = k · (6; −8; 1) ergibt k = 0,5; das Gleichungssystem I 2a = 3, II a − 2 = 0,5 besitzt keine Lösung, die Ebene gehört nicht zur Schar (amtlich)",
    zwischenergebnis="aus I a = 1,5, aus II a = 2,5",
    niveau_geschaetzt="II",
    fehlerquelle="nur die rechte Seite vergleichen (24 = 2 · 12) und Zugehörigkeit bejahen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 2.1: Oktaeder im Würfel
OKT_SKIZZE = ("Schrägbild ohne Koordinatenachsen: gestrichelter Würfel, darin ein Oktaeder mit durchgezogenen Kanten, "
              "dessen sechs Ecken die Mittelpunkte der Würfelflächen sind; die vier Ecken A (vorn), B (rechts), C "
              "(hinten) und D (links) liegen in einer Ebene, die beiden übrigen oben und unten")
row("2024MerhoehtAAGLAA221", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Kantenlänge eines Würfels aus gegenüberliegenden Oktaederecken nachweisen", typ_neben="",
    stichwoerter="A und C gegenüberliegende Flächenmittelpunkte|AC = (−4; −8; 8)|Länge √144 = 12 = Kantenlänge",
    voraussetzungen="Abstand gegenüberliegender Flächenmittelpunkte gleich Kantenlänge|Betrag eines Vektors",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Körper", skizze=OKT_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Oktaeder mit den Flächenmittelpunkten eines Würfels als Ecken; A(1; 2; 1), B, C(−3; −6; 9), D liegen in der Ebene H: 2 x1 + x2 + 2 x3 = 6",
    gesucht="Nachweis, dass die Kantenlänge des Würfels 12 beträgt",
    verfahren="A und C sind Mittelpunkte gegenüberliegender Würfelflächen, ihr Abstand ist die Kantenlänge",
    schritte="2", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="Kantenlänge des Würfels |AC| = |(−4; −8; 8)| = √144 = 12 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="|AC| als Oktaederkante deuten",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

row("2024MerhoehtAAGLAA221", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt auf einer Lotgeraden mit vorgegebenem Abstand zur Ebene bestimmen", typ_neben="",
    stichwoerter="Mittelpunkt M von AC: (−1; −2; 5) ist der Würfelmittelpunkt|Normalenvektor n = (2; 1; 2) mit |n| = 3|Abstand zur fehlenden Ecke: halbe Kante 6|OM + 2 · n = (3; 0; 9)",
    voraussetzungen="Würfelmittelpunkt als Mitte von AC|Normalenvektor der Ebene normieren|halbe Kantenlänge entlang der Normalen abtragen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=OKT_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Oktaeder im Würfel der Kantenlänge 12; A(1; 2; 1), C(−3; −6; 9) in H: 2 x1 + x2 + 2 x3 = 6; zwei Ecken des Oktaeders liegen nicht in H",
    gesucht="Koordinaten einer dieser beiden Ecken",
    verfahren="Mittelpunkt M von AC ist der Würfelmittelpunkt; die fehlenden Ecken liegen im Abstand 6 (halbe Kante) senkrecht zu H, also M ± 6 · n/|n|",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2024MerhoehtAAGLAA221-a",
    ergebnis="Mittelpunkt M der Strecke AC: M(−1; −2; 5); Normalenvektor n = (2; 1; 2) mit |n| = 3; OM + 2 · n = (3; 0; 9) (amtlich)",
    zwischenergebnis="zweite Ecke (−5; −4; 1)",
    niveau_geschaetzt="III",
    fehlerquelle="die volle Kantenlänge 12 statt 6 abtragen",
    bemerkung="Standardbezug: K2 III, K4 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ea-A wiederverwendet. Eichregel: (a) Lage der Ecke (Würfelmitte, halbe Kante senkrecht zu H) in eine Vektorgleichung übersetzen.")

# ---- AG/LA (A2) 2.2: Spiegelung einer Geraden an einer Geraden (ungegliedert)
row("2024MerhoehtAAGLAA222", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Spiegelgerade zweier Geraden zeichnen und Punkt der Winkelhalbierenden als Vektorterm angeben", typ_neben="",
    stichwoerter="g durch A und P, g* durch B und P|h Winkelhalbierende durch P|Raute aus gleich langen Vektoren|OB + |PB|/|AP| · AP liefert Punkt von h",
    voraussetzungen="Spiegelung einer Geraden an einer Geraden durch den Schnittpunkt als Winkelhalbierende|Vektor auf vorgegebene Länge skalieren|Rauteneigenschaft der Diagonalen",
    format="Zeichnen|Kurzantwort", operator="Zeichnen Sie|Geben Sie an", antwort="Grafik|Term",
    material="Figur", skizze="Zeichenebene mit drei markierten Punkten ohne Koordinaten: A links unten, P rechts der Mitte, B oben links von P; zu ergänzen: g durch A und P, g* durch B und P, h durch P als Winkelhalbierende",
    kontext="ohne", textumfang="mittel",
    gegeben="Punkte A, B, P in einer Ebene (Abbildung); g durch A, g* durch B, h durch P; g und g* schneiden sich in P; g* entsteht aus g durch Spiegelung an h",
    gesucht="g, g* und eine Gerade h in der Abbildung|Term, der aus A, B, P den Ortsvektor eines weiteren Punktes von h liefert",
    verfahren="g = AP, g* = BP zeichnen, h als Winkelhalbierende in P; von B aus den Vektor AP auf die Länge |PB| skaliert abtragen: die Raute aus PB und dem skalierten Vektor hat h als Diagonale",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Zeichnung mit g durch A und P, g* durch B und P, h durch P als Winkelhalbierende; Term OB + |PB|/|AP| · AP (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="OA + OB als Term angeben (Mittelpunkt statt Raute)",
    bemerkung="Standardbezug: K2 III, K4 III, K5 II, K6 II. Amtlich, eigene Rechnung mit Beispielkoordinaten bestätigt (Term liefert Punkt der Winkelhalbierenden). Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Eichregel: (a) Spiegelbedingung in eine Vektorkonstruktion übersetzen.")

# ---- AG/LA (A2) 2.3: Geradenschar und Quadrat
row("2024MerhoehtAAGLAA223", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Parallelität aller Geraden einer Schar begründen", typ_neben="",
    stichwoerter="g_k: x = (k; −4k; k) + μ · (4; 8; 1)|Richtungsvektor ohne k|alle parallel",
    voraussetzungen="Parallelität über gleiche Richtungsvektoren",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Geradenschar g_k: x = (k; −4k; k) + μ · (4; 8; 1), μ und k reell",
    gesucht="Begründung, dass alle Geraden der Schar parallel zueinander sind",
    verfahren="Richtungsvektor betrachten",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="alle Geraden der Schar haben denselben Vektor als Richtungsvektor (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="mit den Stützvektoren argumentieren",
    bemerkung="Standardbezug: K1 I, K2 I, K6 I. Amtlich.")

row("2024MerhoehtAAGLAA223", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Nachbarschaft zweier Quadratecken auf einer Geradenschar durch Fallunterscheidung ausschließen", typ_neben="",
    stichwoerter="O und P(11; 4; 5) Ecken, zwei Seiten auf Scharengeraden|Fall 1: O, P auf derselben Geraden: (11; 4; 5) = s · (4; 8; 1) unlösbar|Fall 2: auf verschiedenen Geraden: OP müsste senkrecht zum Richtungsvektor sein, (11; 4; 5) · (4; 8; 1) = 81 ≠ 0|nicht benachbart",
    voraussetzungen="Lage benachbarter Quadratecken relativ zu zwei parallelen Seitengeraden deuten|Kollinearität prüfen|Orthogonalität über das Skalarprodukt",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Schar g_k mit Richtungsvektor (4; 8; 1); Quadrat mit den Ecken O(0; 0; 0) und P(11; 4; 5), zwei Seiten liegen auf Geraden der Schar",
    gesucht="Nachweis, dass O und P keine benachbarten Ecken des Quadrats sind",
    verfahren="benachbarte Ecken liegen entweder auf derselben Scharengeraden (OP parallel zum Richtungsvektor) oder auf zwei verschiedenen (OP senkrecht dazu); beides ausschließen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2024MerhoehtAAGLAA223-a",
    ergebnis="da (11; 4; 5) = s · (4; 8; 1) für reelles s nicht lösbar ist, sind O und P keine benachbarten Ecken auf derselben Geraden der Schar; da (11; 4; 5) · (4; 8; 1) = 44 + 32 + 5 ≠ 0, sind O und P keine benachbarten Ecken auf verschiedenen Geraden der Schar (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur den Fall „auf derselben Geraden“ prüfen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: Fallunterscheidung (Grundregel) mit geometrischer Deutung der Nachbarschaft.")

# ---- Stochastik 1.1: Glücksrad, Standardabweichung, Sektoren
BIN24_SKIZZE = ("Säulendiagramm P(X = k) für k von 0 bis 100 mit Achsenunterbrechung zwischen 5 und 50, y-Achse "
                "ohne Zahlen; Säulen ab etwa k = 60 sichtbar, höchste Säule bei k = 75, symmetrischer Abfall bis "
                "etwa k = 88")
row("2024MerhoehtAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Gleiche Standardabweichung zweier komplementärer Zufallsgrößen begründen", typ_neben="",
    stichwoerter="X Anzahl Blau, Y Anzahl Gelb bei 100 Drehungen|p und 1 − p|σ = √(100 · p · (1 − p)) für beide",
    voraussetzungen="Formel für die Standardabweichung der Binomialverteilung|Gegenwahrscheinlichkeit",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="mittel",
    gegeben="Glücksrad mit 20 gleich großen blauen oder gelben Sektoren, 100-mal gedreht; X zählt Blau, Y zählt Gelb, beide binomialverteilt",
    gesucht="Begründung, dass X und Y dieselbe Standardabweichung haben",
    verfahren="mit p für Blau ist 1 − p die Wahrscheinlichkeit für Gelb; σ hängt symmetrisch von p und 1 − p ab",
    schritte="1", zahlenraum="Wurzel", einheiten="", abhaengig_von="",
    ergebnis="ist p die Wahrscheinlichkeit für Blau beim einmaligen Drehen, dann ist 1 − p die für Gelb; somit ist √(100 · p · (1 − p)) die Standardabweichung sowohl von X als auch von Y (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="mit gleichen Erwartungswerten argumentieren",
    bemerkung="Standardbezug: K1 II, K2 II, K3 I, K5 I. Amtlich, eigene Rechnung bestätigt. Das Diagramm gehört zu Teilaufgabe b.")

row("2024MerhoehtAStochastik11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln", typ_neben="",
    stichwoerter="Erwartungswert ganzzahlig, also an der höchsten Säule: 75|75 = 100 · b/20|b = 15 blaue Sektoren",
    voraussetzungen="ganzzahliger Erwartungswert liegt an der höchsten Säule|E = n · p|p als Anteil der Sektoren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=BIN24_SKIZZE, kontext="Glücksrad", textumfang="mittel",
    gegeben="Glücksrad mit 20 Sektoren, 100 Drehungen, X Anzahl Blau mit ganzzahligem Erwartungswert; Wahrscheinlichkeitsverteilung von X in der Abbildung",
    gesucht="Anzahl der blauen Sektoren",
    verfahren="Erwartungswert als Lage der höchsten Säule ablesen, 75 = 100 · b/20 nach b auflösen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Abbildung ist zu entnehmen, dass 75 der Erwartungswert von X ist; mit b blauen Sektoren gilt 75 = 100 · b/20 ⇔ b = 15 (amtlich)",
    zwischenergebnis="p = 0,75",
    niveau_geschaetzt="II",
    fehlerquelle="15 als p deuten oder 75 als Sektorenzahl",
    bemerkung="Standardbezug: K1 II, K2 II, K3 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet (dort p, hier die Sektorenzahl aus p).")

# ---- Stochastik 1.2: Normalverteilung
NV_SKIZZE = ("Koordinatensystem mit x-Achse von 0 bis 40 (Markierungen in Zweierschritten) und y-Achse von 0 bis "
             "0,06 (Schritt 0,01), Gitter; Glockenkurve der Dichtefunktion mit Maximum etwa 0,06 bei x = 20, "
             "Wendepunkte etwa bei 13 und 27, an den Rändern nahe null")
row("2024MerhoehtAStochastik12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Wahrscheinlichkeit eines Einzelwerts einer stetigen Zufallsgröße angeben", typ_neben="",
    stichwoerter="normalverteilt, stetig|P(X = 14) = 0",
    voraussetzungen="Einzelwerte einer stetigen Zufallsgröße haben Wahrscheinlichkeit null",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=NV_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph der Dichtefunktion einer normalverteilten Zufallsgröße X mit Erwartungswert 20 in der Abbildung",
    gesucht="Wahrscheinlichkeit, dass X den Wert 14 annimmt",
    verfahren="Eigenschaft stetiger Verteilungen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="P(X = 14) = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="den Dichtewert bei 14 (etwa 0,03) als Wahrscheinlichkeit angeben",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich. Erste Fundstelle des Themas Normalverteilung und Sigma-Regeln (nicht für das grundlegende Niveau in BE und BB).")

row("2024MerhoehtAStochastik12", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Näherung einer Normalverteilungswahrscheinlichkeit über Rechteck und Symmetrie erläutern", typ_neben="",
    stichwoerter="P(18 ≤ X ≤ 20) ≈ Rechteck Breite 2, Höhe 0,06|0,12|Symmetrie zu 20: P(|X − 20| ≤ 2) ≈ 2 · 0,12|Gegenereignis 1 − 0,24 = 0,76",
    voraussetzungen="Wahrscheinlichkeit als Fläche unter der Dichte|Rechtecknäherung|Symmetrie der Normalverteilung|Gegenereignis",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Koordinatensystem", skizze=NV_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Dichtefunktion von X mit Erwartungswert 20 in der Abbildung; vorgegebene Rechnung P(18 ≤ X ≤ 20) ≈ 2 · 0,06 = 0,12, somit P(|X − 20| > 2) ≈ 1 − 2 · 0,12 = 0,76",
    gesucht="Erläuterung der Überlegungen, die zu dieser Bestimmung führen",
    verfahren="die Fläche unter der Dichte über [18; 20] durch ein Rechteck der Breite 2 und Höhe 0,06 nähern; Symmetrie liefert dieselbe Fläche über [20; 22]; Gegenereignis",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="2024MerhoehtAStochastik12-a",
    ergebnis="der Inhalt der Fläche zwischen Dichtefunktion, x-Achse, x = 18 und x = 20 ist etwa der eines Rechtecks mit Breite 2 und Höhe 0,06, also P(18 ≤ X ≤ 20) ≈ 0,12; aufgrund der Symmetrie gilt P(|X − 20| > 2) = 1 − 2 · P(18 ≤ X ≤ 20) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="0,06 als Wahrscheinlichkeit statt als Dichtewert deuten",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K6 II. Amtlich, eigene Rechnung bestätigt. Die Symmetrie ist in der vorgegebenen Rechnung schon benutzt, das Erläutern ist keine eigene Deutung – kein Eintrag der Deutungsliste.")

# ---- Stochastik 2.1: drei Behälter, Bayes (ungegliedert)
row("2024MerhoehtAStochastik21", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bayes-Term für drei Behälter nachweisen und Kugelzahl bestimmen", typ_neben="",
    stichwoerter="P(C) = 1/3|P_C(S) = 3/(w + 3)|A und B liefern beide P(S) = 1/4|Nenner 1/3 · 3/(w + 3) + 2/3 · 1/4|P_S(C) = 1/5 ⇔ w = 21",
    voraussetzungen="Formel von Bayes bzw. Pfadregeln mit Parameter|Sonderfall erkennen: A und B haben dieselbe Schwarzwahrscheinlichkeit|Bruchgleichung lösen",
    format="Rechnung", operator="Weisen Sie nach|Berechnen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="lang",
    gegeben="Behälter A (dreimal so viele weiße wie schwarze Kugeln), B (12 weiße, 4 schwarze), C (3 schwarze, w weiße); Behälter zufällig wählen, Kugel ziehen; Term (1/3 · 3/(w + 3)) / (1/3 · 3/(w + 3) + 2/3 · 1/4) für P(Behälter C | schwarz)",
    gesucht="Nachweis des Terms|w, wenn diese Wahrscheinlichkeit 1/5 beträgt",
    verfahren="P(C) = 1/3, P_C(S) = 3/(w + 3), P_(nicht C)(S) = 1/4, weil A und B beide Schwarzanteil 1/4 haben; Bayes-Formel; dann 1/5 setzen und nach w auflösen",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="C: Behälter C gewählt, S: Kugel schwarz; aus P(C) = 1/3, P_C(S) = 3/(w + 3) und P_(nicht C)(S) = 1/4 folgt der Term für P_S(C); P_S(C) = 1/5 ⇔ 5 · 1/(w + 3) = 1/(w + 3) + 1/6 ⇔ 30 = 6 + w + 3 ⇔ w = 21 (amtlich)",
    zwischenergebnis="Schwarzanteil in A: 1/4, in B: 4/16 = 1/4",
    niveau_geschaetzt="III",
    fehlerquelle="A und B im Nenner getrennt mit je 1/3 · 1/4 ansetzen und die Zusammenfassung 2/3 · 1/4 nicht erkennen",
    bemerkung="Standardbezug: K1 III, K3 III, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.1). Eichregel: (b) Sonderfall erkennen (A und B mit gleichem Schwarzanteil) und Bayes ansetzen. Thema nur in Brandenburg Prüfungsgegenstand (iqb.md § 6).")

# ---- Stochastik 2.2: Würfelbeschriftung (ungegliedert)
row("2024MerhoehtAStochastik22", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen", typ_neben="",
    stichwoerter="sichtbar 5, 5, 1|drei verdeckte Seiten aus 3, 4, 5, 6|Erwartungswert 4 heißt Summe 24, verdeckt 13|genau drei verschiedene Zahlen|P(zweimal gleich) = 1/2|3, 5, 5: (4/6)² + 2 · (1/6)² = 1/2|möglich",
    voraussetzungen="Erwartungswert als Mittel der sechs Zahlen|Bedingungen kombinieren|Wahrscheinlichkeit für gleiche Zahl bei zwei Würfen als Summe der Quadrate",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Figur", skizze="Schrägbild eines Würfels mit drei sichtbaren Seiten, beschriftet mit 5 (vorn), 1 (rechts) und 5 (oben)",
    kontext="Würfel", textumfang="lang",
    gegeben="Würfel mit sichtbaren Seiten 5, 5, 1; drei unsichtbare Seiten sollen mit Zahlen aus 3, 4, 5, 6 beschriftet werden (Wiederholung erlaubt); Bedingungen: Erwartungswert beim einmaligen Werfen 4, genau drei verschiedene Zahlen auf dem Würfel, P(zweimal dieselbe Zahl bei zwei Würfen) = 1/2",
    gesucht="Untersuchung, ob eine Beschriftung alle drei Eigenschaften erfüllt",
    verfahren="aus E = 4 die Summe 24, also 13 für die verdeckten Seiten; Kandidaten mit genau drei verschiedenen Zahlen prüfen; für 3, 5, 5 die Wahrscheinlichkeit gleicher Zahlen ausrechnen",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="aus dem Erwartungswert 4 ergibt sich für die Summe der drei Zahlen auf den nicht sichtbaren Seiten der Wert 13; mit 3, 5 und 5 treffen die ersten beiden Aussagen zu, und die Wahrscheinlichkeit für zweimal dieselbe Zahl beträgt 4/6 · 4/6 + 2 · 1/6 · 1/6 = 1/2; die Beschriftung ist möglich (amtlich)",
    zwischenergebnis="Alternativen 3, 4, 6 und 4, 4, 5 verletzen die zweite oder dritte Bedingung",
    niveau_geschaetzt="III",
    fehlerquelle="die sichtbaren Seiten beim Erwartungswert vergessen (Summe 13 auf sechs Seiten verteilen)",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt (Abzählen aller Beschriftungen, 3, 5, 5 ist die einzige). Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Eichregel: (a) drei Sachbedingungen in Gleichungen übersetzen.")

# ---- Stochastik 2.3: Tetraeder (Datei mit drei Seiten, b auf Seite 2)
TET_SKIZZE = ("Abb. 1: Säulendiagramm P(X = k) für k = 0 bis 4 mit y-Achse 0 bis 0,5 (Schritt 0,1), Gitter; Säulen "
              "etwa 0,32, 0,42, 0,21, 0,05, 0,004. Abb. 2: leeres Koordinatensystem P(Y = k), k = 0 bis 4, gleiche "
              "Achsen, zum Eintragen")
row("2024MerhoehtAStochastik23", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Verteilung der Gegenzufallsgröße im Diagramm darstellen", typ_neben="",
    stichwoerter="Y = 4 − X|P(Y = k) = P(X = 4 − k)|Säulen gespiegelt: 0,004, 0,05, 0,21, 0,42, 0,32",
    voraussetzungen="Zusammenhang Y = n − X|Säulen ablesen und spiegeln",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="Diagramm", skizze=TET_SKIZZE, kontext="Tetraeder", textumfang="mittel",
    gegeben="Tetraeder mit Zahlen 1 bis 4, gleich wahrscheinlich, viermal geworfen; X zählt die Würfe mit 1, Verteilung in Abbildung 1; Y zählt die Würfe ohne 1",
    gesucht="Wahrscheinlichkeitsverteilung von Y in Abbildung 2",
    verfahren="Y = 4 − X, also die Säulen von Abbildung 1 in umgekehrter Reihenfolge eintragen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Säulen bei k = 0 bis 4 mit etwa 0,004, 0,05, 0,21, 0,42, 0,32 (Spiegelbild von Abbildung 1) (amtlich)",
    zwischenergebnis="X binomialverteilt mit n = 4, p = 1/4",
    niveau_geschaetzt="II",
    fehlerquelle="Abbildung 1 unverändert abzeichnen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II. Amtlich, eigene Rechnung bestätigt; der Erwartungshorizont zeigt das Diagramm. Datei mit drei Seiten. Das Feld skizze beschreibt das Material.")

row("2024MerhoehtAStochastik23", "b", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Zufallsgröße mit gleicher Binomialverteilung in einem anderen Experiment angeben", typ_neben="",
    stichwoerter="roter und grüner Würfel viermal gleichzeitig|Ereignis je Wurf mit Wahrscheinlichkeit 1/4 nötig|36 gleich wahrscheinliche Paare, 9 mit beiden Zahlen höchstens 3|Z: Anzahl der Würfe, bei denen keine Zahl größer als 3 ist|binomialverteilt mit n = 4, p = 1/4",
    voraussetzungen="Binomialverteilung durch n und p charakterisiert|Laplace-Ereignis mit Wahrscheinlichkeit 1/4 im Zweiwürfelexperiment konstruieren",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Würfel", textumfang="mittel",
    gegeben="X binomialverteilt mit n = 4 und p = 1/4 (Tetraeder); anderes Experiment: ein roter und ein grüner Würfel (1 bis 6) werden viermal gleichzeitig geworfen",
    gesucht="eine Zufallsgröße Z zu diesem Experiment mit derselben Verteilung wie X, mit Begründung",
    verfahren="ein Ereignis je Doppelwurf mit Wahrscheinlichkeit 1/4 finden (9 von 36 Paaren) und Z als Anzahl der Würfe mit diesem Ereignis definieren",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="2024MerhoehtAStochastik23-a",
    ergebnis="Z: Anzahl der Würfe, bei denen keine der beiden erzielten Zahlen größer als drei ist; beim einmaligen Werfen der beiden Würfel gibt es 36 gleich wahrscheinliche Ergebnisse, bei neun ist keine Zahl größer als drei, die Wahrscheinlichkeit beträgt 9/36 = 1/4; damit sind X und Z beide binomialverteilt mit p = 1/4 und n = 4 (amtlich)",
    zwischenergebnis="ebenso möglich: beide Zahlen gerade, beide ungerade",
    niveau_geschaetzt="III",
    fehlerquelle="ein Ereignis mit Wahrscheinlichkeit 1/6 (Pasch) wählen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 III, K6 III. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2. Eichregel: (a) Verteilungsgleichheit in die Bedingung p = 1/4 übersetzen und ein passendes Ereignis konstruieren.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Vorzeichen eines Integrals am Graphen beurteilen", "Analysis", "Flächeninhalt durch Integration",
     "Am Graphen die Flächenstücke über und unter der x-Achse im Integrationsintervall vergleichen und "
     "daraus das Vorzeichen des Integrals beurteilen.",
     "2024MerhoehtAAnalysis11-a"),
    ("Tangente im Ursprung als Gerade durch zwei Punkte nachweisen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die Tangente an einer Stelle über Ableitung und Funktionswert aufstellen und zeigen, dass sie "
     "mit der Geraden durch zwei gegebene Punkte übereinstimmt.",
     "2024MerhoehtAAnalysis11-b"),
    ("Scharparameter aus einem Punkt des Graphen angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameterwert einer Funktionsschar angeben, für den ein gegebener Punkt auf dem Graphen liegt.",
     "2024MerhoehtAAnalysis12-a"),
    ("Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Nullstellen einer Schar bestimmen und den Inhalt der eingeschlossenen Fläche als Term im "
     "Scharparameter berechnen.",
     "2024MerhoehtAAnalysis12-b"),
    ("Vorzeichen der Funktionswerte einer Schar begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus den Vorzeichen der Faktoren eines Scharterms begründen, dass der Graph in einem Bereich "
     "unterhalb oder oberhalb der x-Achse verläuft.",
     "2024MerhoehtAAnalysis13-a"),
    ("Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Unter abgebildeten Graphen einer Schar den zum Parametervorzeichen passenden auswählen, über "
     "Grenzverhalten und Anzahl der Extrempunkte.",
     "2024MerhoehtAAnalysis13-b"),
    ("Flächeninhalt eines Rechtecks aus Nullstellen und Normale als parameterunabhängig nachweisen",
     "Analysis", "Tangente, Normale, Schnittwinkel",
     "Ein Rechteck aus Nullstellen eines Scharterms und der Normalen im Ursprung skizzieren und "
     "zeigen, dass sein Flächeninhalt nicht vom Parameter abhängt.",
     "2024MerhoehtAAnalysis22"),
    ("Verschiebung zwischen Graph und hundertster Ableitung berechnen", "Analysis", "Ableitungsregeln",
     "Für eine e-Funktion die n-te Ableitung als Vielfaches erkennen und die Verschiebung in "
     "x-Richtung, die den Graphen in den der Ableitung überführt, über eine Exponentialgleichung "
     "berechnen.",
     "2024MerhoehtAAnalysis23"),
    ("Rohstoffbedarf über die Verflechtungsmatrix berechnen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Den Bedarf an Rohstoffen für vorgegebene Produktmengen als Matrix-Vektor-Produkt berechnen.",
     "2024MerhoehtAAGLAA11-a"),
    ("Verflechtungsmatrix aus Sachbedingungen und Matrixprodukt bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Eine Verflechtungsmatrix mit Unbekannten aus Sachbedingungen ansetzen und die Unbekannten "
     "über das Produkt der Stufenmatrizen bestimmen.",
     "2024MerhoehtAAGLAA11-b"),
    ("Wirkung einer Permutationsmatrix beschreiben und Einträge aus M · A · M = A bestimmen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Die Wirkung einer Vertauschungsmatrix bei Multiplikation von links und rechts beschreiben und "
     "daraus die Einträge einer Matrix bestimmen, die unter M · A · M invariant ist.",
     "2024MerhoehtAAGLAA121"),
    ("Lineares Gleichungssystem im Sachzusammenhang interpretieren", "Analytische Geometrie",
     "Lineare Gleichungssysteme",
     "Die Gleichungen eines linearen Gleichungssystems als Bilanzen eines Sachverhalts deuten und die "
     "Variablen benennen.",
     "2024MerhoehtAAGLAA122-a"),
    ("Aussage über die Lösungsmenge eines Gleichungssystems mit Nichtnegativität nachweisen",
     "Analytische Geometrie", "Lineare Gleichungssysteme",
     "Eine Aussage über die Lösungen eines Gleichungssystems nachweisen, indem sie in eine "
     "Ungleichung im freien Parameter übersetzt und mit der Nichtnegativität der Variablen verglichen wird.",
     "2024MerhoehtAAGLAA122-b"),
    ("Projektion eines Parallelogramms in eine Koordinatenebene einzeichnen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Punkte parallel zu einer Achse in eine Koordinatenebene projizieren und fehlende Ecken eines "
     "Parallelogramms über den Diagonalenschnittpunkt ergänzen.",
     "2024MerhoehtAAGLAA211-a"),
    ("Winkelart aus dem Vorzeichen des Skalarprodukts beurteilen", "Analytische Geometrie",
     "Skalarprodukt und Winkel",
     "Ein Skalarprodukt berechnen und aus seinem Vorzeichen beurteilen, ob der Winkel zwischen den "
     "Vektoren spitz, rechtwinklig oder stumpf ist.",
     "2024MerhoehtAAGLAA211-b"),
    ("Scharparameter für Parallelität von Ebene und Gerade ermitteln", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Den Parameter einer Ebenenschar ermitteln, für den die Ebene parallel zu einer Geraden ist, "
     "über das Skalarprodukt von Normalen- und Richtungsvektor.",
     "2024MerhoehtAAGLAA212-a"),
    ("Zugehörigkeit einer Ebene zu einer Schar prüfen", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Prüfen, ob eine gegebene Ebene zu einer Ebenenschar gehört, indem die Koordinatengleichung als "
     "Vielfaches der Schargleichung angesetzt und das Gleichungssystem auf Widerspruch geprüft wird.",
     "2024MerhoehtAAGLAA212-b"),
    ("Kantenlänge eines Würfels aus gegenüberliegenden Oktaederecken nachweisen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Den Abstand zweier gegenüberliegender Flächenmittelpunkte als Kantenlänge des Würfels deuten "
     "und berechnen.",
     "2024MerhoehtAAGLAA221-a"),
    ("Spiegelgerade zweier Geraden zeichnen und Punkt der Winkelhalbierenden als Vektorterm angeben",
     "Analytische Geometrie", "Spiegelung",
     "Zwei sich schneidende Geraden und ihre Spiegelachse zeichnen und einen Vektorterm angeben, der "
     "über gleich lange Vektoren (Raute) einen Punkt der Winkelhalbierenden liefert.",
     "2024MerhoehtAAGLAA222"),
    ("Parallelität aller Geraden einer Schar begründen", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Begründen, dass alle Geraden einer Schar parallel sind, weil der Richtungsvektor nicht vom "
     "Parameter abhängt.",
     "2024MerhoehtAAGLAA223-a"),
    ("Nachbarschaft zweier Quadratecken auf einer Geradenschar durch Fallunterscheidung ausschließen",
     "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Nachweisen, dass zwei Punkte keine benachbarten Ecken eines Quadrats mit Seiten auf einer "
     "Geradenschar sind, indem Kollinearität und Orthogonalität zum Richtungsvektor ausgeschlossen werden.",
     "2024MerhoehtAAGLAA223-b"),
    ("Gleiche Standardabweichung zweier komplementärer Zufallsgrößen begründen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Begründen, dass die Trefferzahl und die Nichttrefferzahl einer Bernoulli-Kette dieselbe "
     "Standardabweichung haben, über die Symmetrie der Formel in p und 1 − p.",
     "2024MerhoehtAStochastik11-a"),
    ("Wahrscheinlichkeit eines Einzelwerts einer stetigen Zufallsgröße angeben", "Stochastik",
     "Normalverteilung und Sigma-Regeln",
     "Angeben, dass ein einzelner Wert einer normalverteilten Zufallsgröße die Wahrscheinlichkeit "
     "null hat.",
     "2024MerhoehtAStochastik12-a"),
    ("Näherung einer Normalverteilungswahrscheinlichkeit über Rechteck und Symmetrie erläutern",
     "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Eine vorgegebene Näherungsrechnung erläutern: Fläche unter der Dichte durch ein Rechteck "
     "nähern, Symmetrie des Graphen und Gegenereignis nutzen.",
     "2024MerhoehtAStochastik12-b"),
    ("Bayes-Term für drei Behälter nachweisen und Kugelzahl bestimmen", "Stochastik",
     "Bedingte Wahrscheinlichkeit und Bayes",
     "Einen vorgegebenen Bayes-Term für die Wahrscheinlichkeit eines Behälters bei bekannter "
     "Kugelfarbe nachweisen und aus einem vorgegebenen Wert eine Kugelzahl berechnen.",
     "2024MerhoehtAStochastik21"),
    ("Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Untersuchen, ob sich die Seiten eines Würfels so beschriften lassen, dass Erwartungswert, "
     "Anzahl verschiedener Zahlen und eine Wahrscheinlichkeitsbedingung zugleich gelten.",
     "2024MerhoehtAStochastik22"),
    ("Verteilung der Gegenzufallsgröße im Diagramm darstellen", "Stochastik", "Binomialverteilung",
     "Die Wahrscheinlichkeitsverteilung von n − X aus dem Diagramm von X durch Spiegeln der Säulen "
     "darstellen.",
     "2024MerhoehtAStochastik23-a"),
    ("Zufallsgröße mit gleicher Binomialverteilung in einem anderen Experiment angeben", "Stochastik",
     "Binomialverteilung",
     "In einem anderen Zufallsexperiment ein Ereignis mit derselben Trefferwahrscheinlichkeit "
     "konstruieren und die zugehörige Trefferzahl als gleichverteilte Zufallsgröße begründen.",
     "2024MerhoehtAStochastik23-b"),
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
