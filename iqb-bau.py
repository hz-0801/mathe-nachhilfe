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
    "stapel": "2024-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2024MgrundlegendAAnalysis11": 5,
        "2024MgrundlegendAAnalysis12": 5,
        "2024MgrundlegendAAnalysis13": 5,
        "2024MgrundlegendAAnalysis21": 5,
        "2024MgrundlegendAAnalysis22": 5,
        "2024MgrundlegendAAGLAA111": 5,
        "2024MgrundlegendAAGLAA112": 5,
        "2024MgrundlegendAAGLAA12": 5,
        "2024MgrundlegendAAGLAA211": 5,
        "2024MgrundlegendAAGLAA213": 5,
        "2024MgrundlegendAAGLAA221": 5,
        "2024MgrundlegendAStochastik11": 5,
        "2024MgrundlegendAStochastik12": 5,
        "2024MgrundlegendAStochastik13": 5,
        "2024MgrundlegendAStochastik21": 5,
        "2024MgrundlegendAStochastik22": 5,
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
# niveau_geschaetzt nach der engen Fassung „Kombinieren mit Deutung heißt III" (iqb.md § 7).
# Bei III und bei erwarteten Abweichungen nennt bemerkung den Eintrag der Deutungsliste,
# der gefeuert hat („Eichregel: …").

# ---- Analysis 1.1: Integral grafisch, Spiegelung und Verschiebung
GF_SKIZZE = ("Koordinatensystem mit x-Achse von −4 bis 1,5 und y-Achse von 0 bis 4, Gitter mit "
             "Schrittweite 0,5; Graph G_f (beschriftet): von links bei etwa (−4; 1,1) leicht steigend "
             "zum Hochpunkt etwa (−3; 1,25), dann fallend über (−1,5; 0,9) zum Tiefpunkt (0; 0), "
             "danach steil steigend durch (1; 1) bis über 4 hinaus")
row("2024MgrundlegendAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert grafisch durch Kästchenzählen bestimmen", typ_neben="",
    stichwoerter="Integral von −3 bis −1,5|Kästchen 0,5 × 0,5 mit Inhalt 0,25|etwa 8 Kästchen|Wert etwa 2",
    voraussetzungen="Integral als Fläche unter dem Graphen deuten|Kästchenfläche aus der Gitterweite",
    format="Kurzantwort", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GF_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph G_f einer in IR definierten Funktion f in der Abbildung, Gitter 0,5; Integral von −3 bis −1,5 über f(x) dx",
    gesucht="Wert des Integrals, grafisch bestimmt",
    verfahren="Kästchen zwischen Graph und x-Achse über [−3; −1,5] zählen und mit dem Kästcheninhalt 0,25 multiplizieren",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="Anzahl der Kästchen etwa 8; 8 · 0,25 = 2, der Wert des Integrals ist etwa 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Kästchen als Einheitsquadrate zählen und 8 angeben",
    bemerkung="Standardbezug: K2 I, K4 I. Amtlich. Werte nur aus der Abbildung; Ergebnis als Näherung.")

row("2024MgrundlegendAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Abbildung zwischen zwei Graphen angeben",
    typ_neben="Extrempunkt eines transformierten Graphen angeben",
    stichwoerter="u(x) = −f(x) + 2|Spiegelung an der x-Achse|Verschiebung um 2 in positive y-Richtung|Tiefpunkt (0; 0) wird Hochpunkt (0; 2)",
    voraussetzungen="Vorzeichenwechsel als Spiegelung an der x-Achse deuten|Addition einer Konstanten als Verschiebung|Extrempunkt mit abbilden",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text|Zahl",
    material="Koordinatensystem", skizze=GF_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph G_f mit Tiefpunkt (0; 0) in der Abbildung; u(x) = −f(x) + 2, definiert in IR",
    gesucht="Beschreibung, wie der Graph von u aus G_f entsteht|Koordinaten des Hochpunkts des Graphen von u",
    verfahren="Spiegelung an der x-Achse, dann Verschiebung um 2 nach oben; der Tiefpunkt (0; 0) von f wird zum Hochpunkt (0; 2)",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Graph von u entsteht aus G_f durch Spiegelung an der x-Achse und anschließende Verschiebung um 2 in positive y-Richtung|Hochpunkt (0; 2) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="erst verschieben und dann spiegeln und den Hochpunkt (0; −2) erhalten",
    bemerkung="Standardbezug: K2 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ea-A wiederverwendet (dort Verschiebung, hier Spiegelung und Verschiebung).")

# ---- Analysis 1.2: Punktsymmetrie, Fläche aus zwei Flächenstücken
row("2024MgrundlegendAAnalysis12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Punktsymmetrie am Term über ungerade Exponenten begründen", typ_neben="",
    stichwoerter="f(x) = x³ − 4x|nur ungerade Exponenten|symmetrisch zum Ursprung",
    voraussetzungen="Symmetriekriterium für ganzrationale Funktionen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − 4x, definiert in IR",
    gesucht="Begründung, dass der Graph symmetrisch bezüglich des Koordinatenursprungs ist",
    verfahren="Exponenten der Potenzen im Term prüfen",
    schritte="1", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="das Polynom f(x) enthält ausschließlich Potenzen von x mit ungeraden Exponenten (amtlich)",
    zwischenergebnis="f(−x) = −x³ + 4x = −f(x)",
    niveau_geschaetzt="I",
    fehlerquelle="mit dem Vorzeichen des Koeffizienten −4 argumentieren",
    bemerkung="Standardbezug: K1 I, K4 I. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendAAnalysis12", "b", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen", typ_neben="",
    stichwoerter="Nullstellen −2, 0, 2|Stammfunktion 1/4 x⁴ − 2x²|Integral von −2 bis 0 gleich 4|Symmetrie: doppelt|Inhalt 8",
    voraussetzungen="Nullstellen durch Ausklammern|Potenzregel der Integration|Flächenstücke einzeln oder über Symmetrie",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − 4x, punktsymmetrisch zum Ursprung; der Graph und die x-Achse schließen eine Fläche aus zwei Flächenstücken ein",
    gesucht="Inhalt dieser Fläche",
    verfahren="Nullstellen bestimmen, Integral über [−2; 0] mit der Stammfunktion auswerten und wegen der Symmetrie verdoppeln (oder beide Stücke mit Betrag addieren)",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="2024MgrundlegendAAnalysis12-a",
    ergebnis="f(x) = 0 ⇔ x · (x² − 4) = 0 ⇔ x = −2 oder x = 0 oder x = 2; 2 · Integral von −2 bis 0 über f(x) dx = 2 · [1/4 x⁴ − 2x²] von −2 bis 0 = 2 · (0 − (4 − 8)) = 8 (amtlich)",
    zwischenergebnis="Integral von 0 bis 2 gleich −4",
    niveau_geschaetzt="II",
    fehlerquelle="von −2 bis 2 in einem Zug integrieren und 0 erhalten",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: „Symmetrie ausnutzen“ hätte nach dem Wortlaut feuern können, nicht angewendet – die Symmetrie ist in a schon gegeben und die Fläche ist auch ohne sie eine Routinekette (Nullstellen, Stammfunktion, Beträge).")

# ---- Analysis 1.3: Ableitung am Graphen, Verschiebung beurteilen
EXP2_SKIZZE = ("Koordinatensystem mit x-Achse von −3 bis 2 und y-Achse von −2 bis 5, Gitter; Graph von h "
               "(beschriftet „Graph von h“, oben): von links waagerecht nahe y = 1 kommend, durch (0; 2), "
               "steil steigend; Graph von g (beschriftet „Graph von g“, unten): von links nahe y = −2, "
               "durch (0; 0) und (1; etwa 3,4), steil steigend; beide Graphen schneiden sich bei etwa (1,1; 4)")
row("2024MgrundlegendAAnalysis13", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Ableitungswert berechnen und als Tangentensteigung veranschaulichen", typ_neben="",
    stichwoerter="g(x) = 2e^x − 2|g'(x) = 2e^x|g'(0) = 2|Tangente im Ursprung mit Steigungsdreieck",
    voraussetzungen="Ableitung der e-Funktion mit Faktor|Ableitung als Tangentensteigung|Steigungsdreieck zeichnen",
    format="Rechnung|Zeichnen", operator="Berechnen Sie|Veranschaulichen Sie", antwort="Zahl|Grafik",
    material="Koordinatensystem", skizze=EXP2_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="g(x) = 2 · e^x − 2 und h(x) = e^x + 1, definiert in IR, Graphen in der Abbildung; g' ist die Ableitungsfunktion von g",
    gesucht="g'(0)|Veranschaulichung in der Abbildung, wie man diesen Wert grafisch ermittelt",
    verfahren="g' bilden und 0 einsetzen; die Tangente an den Graphen von g im Punkt (0; 0) einzeichnen und ein Steigungsdreieck (1 nach rechts, 2 nach oben) anlegen",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="g'(x) = 2 · e^x; g'(0) = 2; Tangente im Punkt (0; 0) mit Steigungsdreieck (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Konstante −2 mit ableiten oder die Sekante durch (0; 0) und (1; g(1)) zeichnen",
    bemerkung="Standardbezug: K2 I, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt; der Erwartungshorizont zeigt die Abbildung mit Tangente und Steigungsdreieck. Das Feld skizze beschreibt das Material.")

row("2024MgrundlegendAAnalysis13", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Aussage über eine Verschiebung zwischen zwei Graphen beurteilen", typ_neben="",
    stichwoerter="Verschiebung in y-Richtung ändert die Steigung nicht|g'(0) = 2, h'(0) = 1|Aussage falsch",
    voraussetzungen="Verschiebung in y-Richtung erhält Ableitung|Steigungen an einer Stelle vergleichen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=EXP2_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="g(x) = 2 · e^x − 2 mit g'(0) = 2, h(x) = e^x + 1; Aussage: es gibt eine Verschiebung in y-Richtung, durch die der Graph von h aus dem Graphen von g erzeugt werden kann",
    gesucht="Beurteilung der Aussage",
    verfahren="eine Verschiebung in y-Richtung lässt die Steigung an jeder Stelle unverändert; an der Stelle 0 haben g und h die Steigungen 2 und 1",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="2024MgrundlegendAAnalysis13-a",
    ergebnis="die Aussage ist falsch, da die Steigungen der Graphen von g und h an der Stelle 0 nicht übereinstimmen (amtlich)",
    zwischenergebnis="h(x) − g(x) = 3 − e^x nicht konstant",
    niveau_geschaetzt="III",
    fehlerquelle="aus h(0) − g(0) = 2 auf eine Verschiebung um 2 schließen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: „Aussage beurteilen“ hat gefeuert (Verkettung Steigungen vergleichen und Invarianz deuten), amtlich II.")

# ---- Analysis 2.1: Tangente ablesen, y-Achsenabschnitt allgemein
PAR2_SKIZZE = ("Koordinatensystem mit x-Achse von −4 bis 7 (Markierungen in Zweierschritten) und y-Achse von "
               "−10 bis 12, Gitter; Parabel f(x) = 1/2 x² mit Scheitel im Ursprung durch (4; 8) (markiert) und "
               "(−4; 8); Tangente t im Punkt (4; 8): Gerade mit Steigung 4 durch (2; 0) und (0; −8)")
row("2024MgrundlegendAAnalysis21", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung aus der Abbildung ablesen", typ_neben="",
    stichwoerter="Nullstelle der Tangente bei 2|y-Achsenabschnitt −8|Steigung 4|y = 4x − 8",
    voraussetzungen="Geradengleichung aus zwei Gitterpunkten ablesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Koordinatensystem", skizze=PAR2_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/2 x², definiert in IR; Graph und Tangente t im Punkt (4; f(4)) in der Abbildung",
    gesucht="Gleichung von t anhand der Abbildung",
    verfahren="zwei Gitterpunkte der Tangente ablesen, etwa (2; 0) und (4; 8), Steigung und Achsenabschnitt bestimmen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="y = 4x − 8 (amtlich)",
    zwischenergebnis="f'(4) = 4 bestätigt die Steigung",
    niveau_geschaetzt="I",
    fehlerquelle="die Steigung aus dem Achsenabschnitt −8 und dem Berührpunkt falsch als 2 ablesen",
    bemerkung="Standardbezug: K2 I, K4 I. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendAAnalysis21", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="y-Achsenabschnitt der Tangente allgemein nachweisen", typ_neben="",
    stichwoerter="Tangente in (u; f(u))|Steigung f'(u) = u|1/2 u² = u · u + n|n = −1/2 u² = −f(u)",
    voraussetzungen="Tangentengleichung mit allgemeiner Stelle u aufstellen|Ableitung|Gleichung nach n auflösen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Koordinatensystem", skizze=PAR2_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/2 x²; für jedes reelle u die Tangente an den Graphen im Punkt (u; f(u))",
    gesucht="Nachweis, dass diese Tangente die y-Achse im Punkt (0; −f(u)) schneidet",
    verfahren="Ansatz y = mx + n mit m = f'(u) = u; Berührpunkt einsetzen und n bestimmen",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2024MgrundlegendAAnalysis21-a",
    ergebnis="Gleichung der Tangente y = mx + n; f(u) = 1/2 u², m = f'(u) = u; 1/2 u² = u · u + n ⇔ n = −1/2 u², d. h. n = −f(u) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur den Fall u = 4 aus a nachrechnen",
    bemerkung="Standardbezug: K1 III, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: kein Listeneintrag; III wegen des allgemeinen Nachweises mit Parameter (verallgemeinern), wie 2025-ea-A Analysis 2.1 a und AGLAA222 b – Kandidat für die Deutungsliste.")

# ---- Analysis 2.2: lokale gleich mittlere Änderungsrate (ungegliedert)
row("2024MgrundlegendAAnalysis22", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Stelle mit lokaler gleich mittlerer Änderungsrate bestimmen", typ_neben="",
    stichwoerter="f(x) = √x, g: y = 1/4 x|Schnittstellen 0 und 16|mittlere Änderungsrate gleich Steigung von g|f'(x) = 1/(2√x) = 1/4|x = 4",
    voraussetzungen="Schnittstellen von Wurzelfunktion und Gerade|mittlere Änderungsrate als Sekantensteigung deuten|Ableitung der Wurzelfunktion|Wurzelgleichung lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = √x mit Definitionsmenge IR_0^+; Gerade g: y = 1/4 x; Intervall zwischen den x-Koordinaten der beiden Schnittpunkte von Graph und Gerade; in diesem Intervall gibt es eine Stelle, an der die lokale Änderungsrate von f mit der mittleren Änderungsrate von f im Intervall übereinstimmt",
    gesucht="diese Stelle",
    verfahren="die Sekante durch die Schnittpunkte ist g selbst, die mittlere Änderungsrate also 1/4; f'(x) = 1/4 lösen",
    schritte="3", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="die betrachtete mittlere Änderungsrate ist gleich der Steigung von g; für x > 0 gilt f'(x) = 1/4 ⇔ 1/(2√x) = 1/4 ⇔ √x = 2 ⇔ x = 4 (amtlich)",
    zwischenergebnis="Schnittstellen 0 und 16",
    niveau_geschaetzt="III",
    fehlerquelle="die mittlere Änderungsrate über die Schnittstellen erst umständlich berechnen oder f' falsch bilden",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Eichregel: „Bedingung in Gleichung übersetzen“ hat gefeuert (mittlere Änderungsrate als Steigung der Geraden erkennen).")

# ---- AG/LA (A1) 1.1: Verflechtungsdiagramm, Matrixeintrag aus Bedingungen
row("2024MgrundlegendAAGLAA111", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtungsdiagramm zu einer Matrix zeichnen", typ_neben="",
    stichwoerter="Rohstoffe R1, R2, Endprodukte E1, E2|Matrix ((x; 4), (6; y))|Pfeile R1→E1 mit x, R2→E1 mit 4, R1→E2 mit 6, R2→E2 mit y",
    voraussetzungen="Matrixeinträge als Pfeilbeschriftungen lesen (Zeile Rohstoff, Spalte Endprodukt)",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="zu zeichnen: vier Knoten R1, R2 (links) und E1, E2 (rechts), Pfeile R1→E1 (x), R2→E1 (4), R1→E2 (6), R2→E2 (y)",
    kontext="Produktion", textumfang="mittel",
    gegeben="Produktionsprozess Rohstoffe R1, R2 zu Endprodukten E1, E2 mit ((x; 4), (6; y)) · (e1; e2) = (r1; r2); Einträge der Vektoren sind Mengeneinheiten",
    gesucht="beschriftetes Verflechtungsdiagramm",
    verfahren="je Matrixeintrag einen Pfeil vom Rohstoff der Zeile zum Endprodukt der Spalte mit dem Eintrag beschriften",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Diagramm mit Knoten R1, R2, E1, E2 und Pfeilen R1→E1 (x), R2→E1 (4), R1→E2 (6), R2→E2 (y) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauschen (4 an R1→E2)",
    bemerkung="Standardbezug: K4 I. Amtlich. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand in BE und BB). Das Feld skizze beschreibt die zu erstellende Zeichnung.")

row("2024MgrundlegendAAGLAA111", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrixeintrag aus Mengenbedingungen ermitteln", typ_neben="",
    stichwoerter="e1 = 2 · e2|r1 = 4 · e1 = 8 · e2|erste Zeile: x · e1 + 4 · e2 = r1|x · 2e2 + 4e2 = 8e2|x = 2",
    voraussetzungen="Sachbedingungen als Gleichungen zwischen e1, e2, r1|erste Zeile des Matrix-Vektor-Produkts|durch e2 kürzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion", textumfang="mittel",
    gegeben="((x; 4), (6; y)) · (e1; e2) = (r1; r2); von E1 wird doppelt so viel produziert wie von E2; die eingesetzte Menge von R1 ist viermal so groß wie die produzierte Menge von E1",
    gesucht="Wert von x",
    verfahren="e1 = 2e2 und r1 = 4e1 = 8e2 in die erste Zeile x · e1 + 4 · e2 = r1 einsetzen und nach x auflösen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="für e1 = 2e2 und r1 = 4e1 = 8e2 ergibt sich x · 2e2 + 4e2 = 8e2 ⇔ x = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="„viermal so groß“ als r1 = e1/4 ansetzen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Eichregel: „Bedingung in Gleichung übersetzen“ hätte nach dem Wortlaut feuern können, nicht angewendet – die Übersetzung ist wörtlich (doppelt, viermal), keine Umdeutung.")

# ---- AG/LA (A1) 1.2: Dreieck und Trapez (ungegliedert, Dublette 2024MgrundlegendAAGLAA212)
row("2024MgrundlegendAAGLAA112", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Flächenverhältnis von Dreieck und Trapez über einen Vektorterm ermitteln", typ_neben="",
    stichwoerter="OD = OC − 2 · AB|D durch Abtragen von −2 · AB an C|CD parallel zu AB, doppelt so lang|gleiche Höhe h|Dreieck 1/2 · |AB| · h, Trapez 3/2 · |AB| · h|Verhältnis 1 : 3",
    voraussetzungen="Vektorterm als Konstruktionsvorschrift deuten|Trapezformel|gemeinsame Höhe erkennen",
    format="Rechnung|Zeichnen", operator="Ermitteln Sie|Stellen Sie dar", antwort="Zahl|Grafik",
    material="Figur", skizze="Dreieck ABC ohne Koordinaten: A links unten, B rechts unten (AB kurz), C rechts oben (lange Seite AC); zu ergänzen: D links oben mit CD = −2 · AB, Höhe h von A auf CD",
    kontext="ohne", textumfang="mittel",
    gegeben="Dreieck ABC in der Abbildung ohne Koordinaten; Punkt D mit OD = OC − 2 · AB, O der Ursprung",
    gesucht="Verhältnis des Flächeninhalts von Dreieck ABC zu dem des Trapezes ABCD|Darstellung des Vorgehens in der Abbildung",
    verfahren="D konstruieren (von C aus den Vektor −2 · AB abtragen), CD ist parallel zu AB und doppelt so lang; Dreieck und Trapez haben dieselbe Höhe h zwischen AB und CD; Trapezformel",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Flächeninhalt des Dreiecks ABC: 1/2 · |AB| · h; Flächeninhalt des Trapezes ABCD: 1/2 · (|AB| + |CD|) · h = 1/2 · (|AB| + 2 · |AB|) · h = 3/2 · |AB| · h; das Verhältnis ist 1 : 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="D am falschen Ende abtragen (von A aus) oder das Verhältnis 1 : 2 aus den Grundseiten ablesen",
    bemerkung="Standardbezug: K1 II, K4 II, K5 I. Amtlich, eigene Rechnung mit Beispielkoordinaten bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 1.2); die Datei liegt wortgleich als 2024MgrundlegendAAGLAA212 ein zweites Mal vor (Dublette ohne Zeile). Ebene Figur, Thema ersatzweise Flächeninhalt und Volumen im Raum.")

# ---- AG/LA (A1) 2: Matrix mit Kern und Fixvektoren
row("2024MgrundlegendAAGLAA12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Existenz mehrerer Lösungen von M · a = 0 begründen", typ_neben="",
    stichwoerter="M = ((1; 0; 0), (1; 1; −1), (1; 0; 0))|Gleichungssystem x = 0, x + y − z = 0|y = z frei|neben dem Nullvektor z. B. (0; 1; 1)",
    voraussetzungen="Matrix-Vektor-Produkt als Gleichungssystem|freie Variable erkennen|Beispielvektor angeben",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="M = ((1; 0; 0), (1; 1; −1), (1; 0; 0))",
    gesucht="Begründung, dass es mehr als einen Vektor a mit M · a = (0; 0; 0) gibt",
    verfahren="das Gleichungssystem liefert x = 0 und y = z; neben dem Nullvektor erfüllt jeder Vektor (0; s; s) die Bedingung",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="das lineare Gleichungssystem M · (x; y; z) = (0; 0; 0) liefert x = 0 und y = z; neben dem Nullvektor erfüllt beispielsweise (0; 1; 1) die Bedingung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur den Nullvektor finden, weil x = 0 auf y = z = 0 übertragen wird",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2024MgrundlegendAAGLAA12", "b", seite="1", punkte="3", afb_amtlich="I|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Alle Fixvektoren einer Matrix ermitteln", typ_neben="",
    stichwoerter="M · b = b|(x; x + y − z; x) = (x; y; z)|x = z, y frei|Lösungsmenge (s; t; s) mit s, t reell",
    voraussetzungen="Matrix-Vektor-Produkt mit Variablen|Koordinatenvergleich|Lösungsmenge mit zwei Parametern beschreiben",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="M = ((1; 0; 0), (1; 1; −1), (1; 0; 0))",
    gesucht="alle Vektoren b mit M · b = b",
    verfahren="M · (x; y; z) = (x; x + y − z; x) mit (x; y; z) gleichsetzen; die zweite Koordinate liefert x = z, die dritte ebenfalls, y bleibt frei",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2024MgrundlegendAAGLAA12-a",
    ergebnis="M · (x; y; z) = (x; x + y − z; x); (x; x + y − z; x) = (x; y; z) ⇔ x = z; die Vektoren b = (s; t; s) mit reellen s, t bilden die Lösungsmenge (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur einen Fixvektor angeben statt der zweiparametrigen Lösungsmenge",
    bemerkung="Standardbezug: K1 III, K2 III, K5 I. Amtlich, eigene Rechnung bestätigt. Eichregel: kein Listeneintrag hat gefeuert (Produkt, Gleichsetzen, Auflösen als Routinekette); amtlich III über K1/K2 für das Beschreiben einer zweiparametrigen Lösungsmenge – Kandidat „Lösungsmenge mit freien Parametern beschreiben“.")

# ---- AG/LA (A2) 1.1: Quader, Verschiebung in den Ursprung
QUADER_SKIZZE = ("Schrägbild eines Quaders ABCDEFGH im Koordinatensystem: A(1; 1; 0) vorn unten (Innenecke), "
                 "B(4; 1; 0) vorn links auf der x-Richtung, D vorn rechts auf der y-Richtung, C rechts vorn unten, "
                 "E(1; 1; 4) über A, F über B, G über C, H(1; 7; 4) über D; Grundfläche mit Gitter; Achsen x "
                 "(nach vorn links), y (nach rechts), z (nach oben) beschriftet, verdeckte Kanten gestrichelt")
row("2024MgrundlegendAAGLAA211", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Koordinaten eines Eckpunkts eines Prismas angeben", typ_neben="",
    stichwoerter="Quader A(1; 1; 0), B(4; 1; 0), E(1; 1; 4), H(1; 7; 4)|G gegenüber von A|G(4; 7; 4)",
    voraussetzungen="Kantenvektoren aus gegebenen Ecken ablesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Körper", skizze=QUADER_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Quader ABCDEFGH mit A(1; 1; 0), B(4; 1; 0), E(1; 1; 4), H(1; 7; 4), Abbildung",
    gesucht="Koordinaten von G",
    verfahren="G = B + AD + AE mit AD = EH = (0; 6; 0) und AE = (0; 0; 4)",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="G(4; 7; 4) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="G mit C(4; 7; 0) verwechseln",
    bemerkung="Standardbezug: K4 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet (Quader als Prisma).")

row("2024MgrundlegendAAGLAA211", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Verschobenen Punkt über den Diagonalenschnittpunkt bestimmen", typ_neben="",
    stichwoerter="Schnittpunkt der Raumdiagonalen = Mittelpunkt von AG|S(2,5; 4; 2)|Verschiebung um −OS|H'(−1,5; 3; 2)",
    voraussetzungen="Mittelpunkt einer Strecke|Verschiebungsvektor aus Bild und Urbild|Vektoraddition",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=QUADER_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Quader mit A(1; 1; 0), G(4; 7; 4), H(1; 7; 4); der Quader wird parallel zu einer Geraden so verschoben, dass der Schnittpunkt seiner Raumdiagonalen im Ursprung liegt; es entsteht A'B'C'D'E'F'G'H'",
    gesucht="Koordinaten von H'",
    verfahren="Schnittpunkt S der Raumdiagonalen als Mittelpunkt von AG; Verschiebung um −OS auf H anwenden",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="2024MgrundlegendAAGLAA211-a",
    ergebnis="Schnittpunkt der Raumdiagonalen S(2,5; 4; 2); OH' = (1; 7; 4) + (−2,5; −4; −2) = (−1,5; 3; 2) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="S als Mittelpunkt von A und H (Flächendiagonale) berechnen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendAAGLAA211", "c", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Eckpunkt mit vorgegebenen Vorzeichen nach einer Verschiebung angeben", typ_neben="",
    stichwoerter="Quader symmetrisch zum Ursprung|nur positive Koordinaten: Ecke, deren Koordinaten alle größer als die von S sind|G' = (1,5; 3; 2)",
    voraussetzungen="Lage der Ecken relativ zum Mittelpunkt deuten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Körper", skizze=QUADER_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="verschobener Quader A'B'C'D'E'F'G'H' mit Diagonalenschnittpunkt im Ursprung; S(2,5; 4; 2), G(4; 7; 4)",
    gesucht="ein Eckpunkt des verschobenen Quaders mit nur positiven Koordinaten",
    verfahren="die Ecke, deren Koordinaten alle größer als die von S sind, ist G; nach der Verschiebung G'(1,5; 3; 2)",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2024MgrundlegendAAGLAA211-b",
    ergebnis="G' (amtlich)",
    zwischenergebnis="G'(1,5; 3; 2)",
    niveau_geschaetzt="II",
    fehlerquelle="H' nennen, weil H die größte y-Koordinate hat",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt (genau eine Ecke mit lauter positiven Koordinaten).")

# ---- AG/LA (A2) 1.3: Punkt mit Parameter, Lage und rechter Winkel
row("2024MgrundlegendAAGLAA213", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden", typ_neben="",
    stichwoerter="P(2; 0; 23), Q_t(6; t; 20)|parallel zur xy-Ebene heißt gleiche z-Koordinaten|23 ≠ 20 für alle t|kein solches t",
    voraussetzungen="Parallelität zur xy-Ebene als z-Komponente 0 des Richtungsvektors deuten",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(2; 0; 23) und Q_t(6; t; 20) mit reellem t",
    gesucht="Entscheidung mit Begründung, ob es ein t gibt, für das die Gerade PQ_t parallel zur xy-Ebene verläuft",
    verfahren="die Gerade ist genau dann parallel zur xy-Ebene, wenn P und Q_t dieselbe z-Koordinate haben; die z-Koordinaten hängen nicht von t ab",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="es gibt keinen solchen Wert von t, da P und Q_t für alle reellen t verschiedene z-Koordinaten haben (amtlich)",
    zwischenergebnis="Richtungsvektor (4; t; −3)",
    niveau_geschaetzt="II",
    fehlerquelle="t = 0 vorschlagen, weil dann die y-Koordinaten übereinstimmen",
    bemerkung="Standardbezug: K1 I, K2 II, K4 I. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendAAGLAA213", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Parameter für einen rechten Winkel über das Skalarprodukt ermitteln", typ_neben="",
    stichwoerter="Dreieck O, P, Q_t|rechter Winkel in Q_t|Q_tO · Q_tP = 0|(−6; −t; −20) · (−4; −t; 3) = t² − 36|t = ±6",
    voraussetzungen="Vektoren vom Scheitel zu den anderen Ecken|Skalarprodukt mit Parameter|quadratische Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Ursprung O, P(2; 0; 23), Q_t(6; t; 20) bilden ein Dreieck",
    gesucht="Werte von t, für die das Dreieck in Q_t einen rechten Winkel hat",
    verfahren="Skalarprodukt der Vektoren Q_tO und Q_tP gleich null setzen",
    schritte="2", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Q_tO · Q_tP = 0 ⇔ (−6; −t; −20) · (−4; −t; 3) = 0 ⇔ t² − 36 = 0 ⇔ t = −6 oder t = 6 (amtlich)",
    zwischenergebnis="24 + t² − 60",
    niveau_geschaetzt="II",
    fehlerquelle="die Vektoren OP und OQ_t verwenden (rechter Winkel in O)",
    bemerkung="Standardbezug: K1 I, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Nahe am Typ „Rechten Winkel eines Dreiecks mit Parameter nachweisen“ (2026-ga-A), dort Nachweis, hier Parameter ermitteln – Vorschlag für den Abgleich.")

# ---- AG/LA (A2) 2.1: Quadrat in der x1x2-Ebene (ungegliedert)
row("2024MgrundlegendAAGLAA221", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Diagonalenschnittpunkt und Flächeninhalt eines Quadrats aus dem Spurpunkt einer Geraden bestimmen", typ_neben="",
    stichwoerter="Quadrat in der x1x2-Ebene, Ecke im Ursprung|Diagonalenschnittpunkt M auf g und in x3 = 0|λ = 2, M(3; 4; 0)|halbe Diagonale |OM| = 5|Fläche 4 · 1/2 · 5² = 50",
    voraussetzungen="Spurpunkt einer Geraden mit einer Koordinatenebene|Diagonalenschnittpunkt als Mittelpunkt|Quadratfläche aus der Diagonalen (vier rechtwinklige Dreiecke oder d²/2)",
    format="Rechnung", operator="Bestimmen Sie|Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Quadrat in der x1x2-Ebene mit einer Ecke im Ursprung; der Schnittpunkt seiner Diagonalen liegt auf g: x = (−1; 4; −2) + λ · (2; 0; 1), λ reell",
    gesucht="Koordinaten des Diagonalenschnittpunkts|Flächeninhalt des Quadrats",
    verfahren="Schnittpunkt von g mit x3 = 0 bestimmen; sein Abstand zum Ursprung ist die halbe Diagonale; das Quadrat besteht aus vier rechtwinkligen Dreiecken mit Katheten 5",
    schritte="4", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="(−1; 4; −2) + λ · (2; 0; 1) = (x1; x2; 0) liefert λ = 2; Schnittpunkt M der Diagonalen: M(3; 4; 0); |OM| = √(3² + 4²) = 5; Flächeninhalt des Quadrats 4 · 1/2 · 5² = 50 (amtlich)",
    zwischenergebnis="Diagonale 10, Fläche 10²/2 = 50",
    niveau_geschaetzt="III",
    fehlerquelle="|OM| = 5 als Seitenlänge nehmen (Fläche 25)",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.1). Eichregel: „Bedingung in Gleichung übersetzen“ hat gefeuert (Diagonalenschnittpunkt in der Ebene als Spurpunkt, Fläche über die halbe Diagonale).")

# ---- Stochastik 1.1: Glitzerbälle
row("2024MgrundlegendAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit für lauter Treffer berechnen und mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="p = 0,4|drei Kinder|0,4³ = 0,064|kleiner als 10 %",
    voraussetzungen="Pfadregel für unabhängige Wiederholungen|Dezimalpotenz",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Werbeaktion/Spielzeug", textumfang="mittel",
    gegeben="jedes Kind erhält einen verpackten Ball, Wahrscheinlichkeit für Glitzerfärbung 40 %; Gruppe von drei Kindern",
    gesucht="Nachweis, dass die Wahrscheinlichkeit, dass jedes der drei Kinder einen Glitzerball erhält, kleiner als 10 % ist",
    verfahren="0,4 dreimal multiplizieren und mit 0,1 vergleichen",
    schritte="1", zahlenraum="dezimal|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="0,4³ = 0,064 < 0,1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="3 · 0,4 rechnen",
    bemerkung="Standardbezug: K1 I, K2 I, K3 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendAStochastik11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="(3/5)⁴ + 4 · (3/5)³ · 2/5|3/5 ohne Glitzer|vier Kinder|mindestens drei Bälle ohne Glitzerfärbung",
    voraussetzungen="3/5 als Gegenwahrscheinlichkeit erkennen|Binomialterme für vier und genau drei Treffer|Zufallsexperiment mit Stufenzahl nennen",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Werbeaktion/Spielzeug", textumfang="mittel",
    gegeben="Wahrscheinlichkeit für Glitzerfärbung 40 %; Term (3/5)⁴ + 4 · (3/5)³ · 2/5",
    gesucht="ein Zufallsexperiment im Sachzusammenhang und ein Ereignis, dessen Wahrscheinlichkeit der Term liefert",
    verfahren="3/5 ist die Wahrscheinlichkeit für keine Glitzerfärbung; vier Faktoren heißt vier Bälle; erster Summand alle vier ohne Glitzer, zweiter genau drei ohne (vier Anordnungen)",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Zufallsexperiment: vier Kinder erhalten jeweils einen Ball; Ereignis: mindestens drei dieser Bälle haben keine Glitzerfärbung (amtlich)",
    zwischenergebnis="Wert ≈ 0,475",
    niveau_geschaetzt="II",
    fehlerquelle="3/5 der Glitzerfärbung zuordnen und „mindestens drei mit Glitzer“ formulieren",
    bemerkung="Standardbezug: K3 I, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ea-A wiederverwendet (viertes Vorkommen).")

# ---- Stochastik 1.2: Glücksrad auf der Spendengala
row("2024MgrundlegendAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen", typ_neben="",
    stichwoerter="10 % grüne Sektoren|zweimal drehen|0,1 · 0,9 + 0,9 · 0,1|0,18",
    voraussetzungen="Pfadregeln mit zwei Reihenfolgen",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksspiel/Spendengala", textumfang="mittel",
    gegeben="Glücksrad mit gleich großen Sektoren, 10 % davon grün; zweimal drehen",
    gesucht="Nachweis, dass die Wahrscheinlichkeit für genau einmal grün 18 % beträgt",
    verfahren="beide Pfade grün–nicht grün und nicht grün–grün addieren",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,1 · 0,9 + 0,9 · 0,1 = 0,18 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="nur einen Pfad rechnen (0,09)",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ea-A wiederverwendet.")

row("2024MgrundlegendAStochastik12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert der Auszahlung mit dem Einsatz vergleichen", typ_neben="",
    stichwoerter="Einsatz 3 €|Auszahlung 10 € je grün: 10 € mit 0,18, 20 € mit 0,01|Erwartungswert 2 €|Einsatz größer|Veranstalter nimmt auf lange Sicht mehr ein",
    voraussetzungen="Verteilung der Auszahlung aufstellen|Erwartungswert berechnen|Erwartungswert mit dem Einsatz vergleichen und deuten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksspiel/Spendengala", textumfang="mittel",
    gegeben="Einsatz 3 €, zweimal drehen, 10 % grün, je grünem Sektor 10 € Auszahlung; P(genau einmal grün) = 0,18",
    gesucht="Begründung, dass der Veranstalter auf lange Sicht mehr einnimmt als auszahlt",
    verfahren="Erwartungswert der Auszahlung 20 · 0,01 + 10 · 0,18 = 2 € berechnen und mit dem Einsatz 3 € vergleichen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="€", abhaengig_von="2024MgrundlegendAStochastik12-a",
    ergebnis="wegen 20 · 1/100 + 10 · 18/100 = 2 ist der Erwartungswert für die Auszahlung 2 €; der Einsatz ist größer (amtlich)",
    zwischenergebnis="P(zweimal grün) = 0,01",
    niveau_geschaetzt="III",
    fehlerquelle="die Auszahlung 10 € nur mit 0,18 gewichten und 20 € vergessen (Erwartungswert 1,80 €)",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Eichregel: „faires Spiel als Erwartungswert gleich Einsatz“ hat gefeuert (hier Ungleichheit), amtlich II – dritter Fall, in dem der Eintrag über dem Standardbezug liegt.")

# ---- Stochastik 1.3: Stühle in einer Reihe
row("2024MgrundlegendAStochastik13", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Auswahlen mit Abstandsbedingung aufzählen", typ_neben="",
    stichwoerter="sechs Stühle in einer Reihe|drei auswählen, zwischen je zweien mindestens ein Stuhl|Stühle 1, 3, 5; 1, 3, 6; 1, 4, 6; 2, 4, 6",
    voraussetzungen="systematisch aufzählen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Klassenzimmer", textumfang="kurz",
    gegeben="sechs Stühle in einer Reihe; es gibt vier Möglichkeiten, drei Stühle so auszuwählen, dass zwischen je zwei ausgewählten mindestens ein weiterer steht",
    gesucht="diese vier Möglichkeiten",
    verfahren="mit dem ersten Stuhl beginnen und die Lücken systematisch verteilen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Stühle 1, 3, 5; 1, 3, 6; 1, 4, 6; 2, 4, 6 (amtlich); der Erwartungshorizont zeigt die Auswahlen als Abbildung mit ausgefüllten Kreisen",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Auswahl 2, 4, 6 vergessen, weil man immer mit Stuhl 1 beginnt",
    bemerkung="Standardbezug: K2 II, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt (Abzählen).")

row("2024MgrundlegendAStochastik13", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl der Sitzordnungen mit Abstandsbedingung berechnen", typ_neben="",
    stichwoerter="vier Stuhlauswahlen|drei Schüler auf drei Stühle: 3! Anordnungen|4 · 3! = 24",
    voraussetzungen="Auswahl und Anordnung multiplizieren|Fakultät",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Klassenzimmer", textumfang="kurz",
    gegeben="sechs Stühle, vier zulässige Auswahlen von drei Stühlen (aus a); Aaron, Bert und Can setzen sich so, dass zwischen je zwei Schülern mindestens ein Stuhl frei bleibt",
    gesucht="Anzahl der Möglichkeiten",
    verfahren="je Stuhlauswahl die drei Schüler in 3! Reihenfolgen verteilen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2024MgrundlegendAStochastik13-a",
    ergebnis="4 · 3! = 24 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="4 · 3 = 12 rechnen",
    bemerkung="Standardbezug: K1 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 2.1: Endkontrolle
row("2024MgrundlegendAStochastik21", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen", typ_neben="",
    stichwoerter="90 % fehlerfrei|fehlerfreies Gerät zu 99 % als fehlerfrei eingestuft|0,9 · 0,99 = 0,891",
    voraussetzungen="bedingte Angaben im Text als Astwahrscheinlichkeiten lesen|Pfadmultiplikation",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Qualitätskontrolle", textumfang="lang",
    gegeben="Geräte sind zu 90 % fehlerfrei; die Endkontrolle stuft ein fehlerfreies Gerät zu 99 % als fehlerfrei ein, ein fehlerhaftes zu 5 % ebenfalls als fehlerfrei",
    gesucht="Nachweis, dass die Wahrscheinlichkeit für „fehlerfrei und als fehlerfrei eingestuft“ 89,1 % beträgt",
    verfahren="Pfad fehlerfrei → als fehlerfrei eingestuft multiplizieren",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,9 · 0,99 = 0,891 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="0,9 + 0,99 oder 0,9 · 0,95 rechnen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Eichregel: kein Listeneintrag; als einzelne Rechnung I geschätzt, amtlich II über K2/K3 (Sachtext in einen Pfad übersetzen).")

row("2024MgrundlegendAStochastik21", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Sachaussage zu einer Ungleichung mit Binomialsumme formulieren", typ_neben="",
    stichwoerter="0,891 + 0,1 · 0,05 = 0,896 als P(als fehlerfrei eingestuft)|Summe k = 90 bis 100 von (100 über k) · 0,896^k · 0,104^(100 − k)|P(X ≥ 90) > 0,5|mindestens 90 von 100 als fehlerfrei eingestuft",
    voraussetzungen="totale Wahrscheinlichkeit aus zwei Pfaden deuten|Binomialsumme als kumulierte Wahrscheinlichkeit lesen|Aussage im Sachzusammenhang formulieren",
    format="Kurzantwort", operator="Formulieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Qualitätskontrolle", textumfang="lang",
    gegeben="Gleichung 0,891 + 0,1 · 0,05 = 0,896; Ungleichung: Summe von k = 90 bis 100 über (100 über k) · 0,896^k · 0,104^(100 − k) > 0,5",
    gesucht="eine Aussage im Sachzusammenhang, die sich aus Gleichung und Ungleichung ergibt",
    verfahren="0,896 als Wahrscheinlichkeit erkennen, dass ein Gerät als fehlerfrei eingestuft wird (beide Pfade); die Summe als P(X ≥ 90) für 100 Geräte lesen",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="2024MgrundlegendAStochastik21-a",
    ergebnis="die Wahrscheinlichkeit dafür, dass bei der Endkontrolle von 100 Geräten mindestens 90 als fehlerfrei eingestuft werden, ist größer als 50 % (amtlich)",
    zwischenergebnis="Summe ≈ 0,53",
    niveau_geschaetzt="III",
    fehlerquelle="0,896 als Anteil fehlerfreier Geräte deuten",
    bemerkung="Standardbezug: K2 III, K3 III, K4 III, K6 II. Amtlich, eigene Rechnung bestätigt (Summe ≈ 0,530). Eichregel: kein Listeneintrag wörtlich; III wegen der Verkettung zweier Deutungen (Gleichung als totale Wahrscheinlichkeit, Summe als kumulierte Binomialwahrscheinlichkeit) – Kandidat „Term in Sachaussage übersetzen“ als Gegenstück zu „Bedingung in Gleichung übersetzen“.")

# ---- Stochastik 2.2: Randomized Response (Datei mit drei Seiten, Teilaufgaben auf Seite 2)
RR_SKIZZE = ("Baumdiagramm mit zwei Stufen: Wurzel, erste Stufe F1 (Ast beschriftet 0,6) und F2 (unbeschriftet), "
             "zweite Stufe je Ja und Nein in Kästchen; nur der Ast F1 → Ja ist mit p beschriftet, alle anderen "
             "Äste der zweiten Stufe und der Ast zu F2 sind leer")
row("2024MgrundlegendAStochastik22", "a", seite="2", punkte="2", afb_amtlich="I|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm eines Befragungsverfahrens mit unbekanntem Anteil vervollständigen", typ_neben="",
    stichwoerter="60 % Frage F1, 40 % Frage F2|F1 Ja mit p, Nein mit 1 − p|F2 fragt das Gegenteil: Ja mit 1 − p, Nein mit p|Randomized Response",
    voraussetzungen="Gegenwahrscheinlichkeiten|erkennen, dass F2 die Verneinung von F1 ist|Anteil p als Astwahrscheinlichkeit",
    format="Eintragen", operator="Vervollständigen Sie", antwort="Grafik",
    material="Diagramm", skizze=RR_SKIZZE, kontext="Befragung", textumfang="lang",
    gegeben="Befragung: 60 % erhalten F1 (ob sie schon einmal unentschuldigt gefehlt haben), 40 % F2 (ob sie noch nie unentschuldigt gefehlt haben), wahrheitsgemäße Antwort Ja/Nein; Anteil p der Gefehlt-Habenden unter den F1-Befragten wie unter allen; Baumdiagramm mit 0,6 und p vorgegeben",
    gesucht="vervollständigtes Baumdiagramm",
    verfahren="F2 mit 0,4; unter F1 Nein mit 1 − p; unter F2 Ja mit 1 − p und Nein mit p, weil F2 die Verneinung von F1 ist",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="F1 0,6: Ja p, Nein 1 − p; F2 0,4: Ja 1 − p, Nein p (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="unter F2 ebenfalls Ja mit p beschriften",
    bemerkung="Standardbezug: K3 III, K4 I, K6 III. Amtlich. Datei mit drei Seiten, Teilaufgaben a und b stehen auf Seite 2. Eichregel: „Bedingung aus dem Sachverhalt übersetzen“ hat gefeuert (Verneinung der Frage als Vertauschung von p und 1 − p). Das Feld skizze beschreibt das vorgegebene Diagramm.")

row("2024MgrundlegendAStochastik22", "b", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil aus dem Ergebnis eines Befragungsverfahrens berechnen", typ_neben="",
    stichwoerter="1000 Befragte, 420 Ja|P(Ja) = 0,6 · p + 0,4 · (1 − p) = 0,42|0,2 · p = 0,02|p = 0,1",
    voraussetzungen="relative Häufigkeit als Wahrscheinlichkeit|Summe der Ja-Pfade|lineare Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=RR_SKIZZE, kontext="Befragung", textumfang="mittel",
    gegeben="Baumdiagramm aus a (F1 0,6 mit Ja p, F2 0,4 mit Ja 1 − p); 1000 Jugendliche befragt, 420 antworten mit Ja",
    gesucht="Anteil p auf Grundlage dieses Ergebnisses",
    verfahren="Wahrscheinlichkeit für Ja über beide Pfade mit der relativen Häufigkeit 0,42 gleichsetzen und nach p auflösen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2024MgrundlegendAStochastik22-a",
    ergebnis="0,6 · p + 0,4 · (1 − p) = 0,42 ⇔ 0,2 · p = 0,02 ⇔ p = 0,1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="0,42 direkt als p deuten oder nur den F1-Pfad ansetzen (0,6p = 0,42)",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: „Bedingung in Gleichung übersetzen“ hat gefeuert (Ja-Anteil als Summe zweier Pfade gleich relative Häufigkeit).")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Integralwert grafisch durch Kästchenzählen bestimmen", "Analysis", "Flächeninhalt durch Integration",
     "Den Wert eines bestimmten Integrals näherungsweise aus der Abbildung bestimmen, indem die "
     "Kästchen unter dem Graphen gezählt und mit dem Kästcheninhalt multipliziert werden.",
     "2024MgrundlegendAAnalysis11-a"),
    ("Extrempunkt eines transformierten Graphen angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den Extrempunkt eines durch Spiegelung oder Verschiebung entstandenen Graphen aus dem "
     "Extrempunkt des Ausgangsgraphen angeben.",
     "2024MgrundlegendAAnalysis11-b"),
    ("Punktsymmetrie am Term über ungerade Exponenten begründen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Die Punktsymmetrie eines Graphen zum Ursprung damit begründen, dass der ganzrationale Term "
     "nur ungerade Exponenten enthält.",
     "2024MgrundlegendAAnalysis12-a"),
    ("Fläche zwischen Graph und x-Achse aus zwei Flächenstücken berechnen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Inhalt der von Graph und x-Achse eingeschlossenen Fläche berechnen, wenn sie aus zwei "
     "Stücken ober- und unterhalb der Achse besteht: Nullstellen, Integrale je Stück mit Betrag "
     "oder Symmetrie.",
     "2024MgrundlegendAAnalysis12-b"),
    ("Ableitungswert berechnen und als Tangentensteigung veranschaulichen", "Analysis",
     "Ableitung und Änderungsrate",
     "Den Wert der Ableitung an einer Stelle berechnen und in der Abbildung durch Tangente und "
     "Steigungsdreieck sichtbar machen.",
     "2024MgrundlegendAAnalysis13-a"),
    ("Aussage über eine Verschiebung zwischen zwei Graphen beurteilen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Beurteilen, ob ein Graph durch Verschiebung in y-Richtung aus einem anderen entsteht, über "
     "den Vergleich der Steigungen an einer Stelle oder die Differenz der Terme.",
     "2024MgrundlegendAAnalysis13-b"),
    ("Tangentengleichung aus der Abbildung ablesen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Gleichung einer eingezeichneten Tangente aus zwei Gitterpunkten ablesen.",
     "2024MgrundlegendAAnalysis21-a"),
    ("y-Achsenabschnitt der Tangente allgemein nachweisen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Für eine allgemeine Stelle u die Tangentengleichung aufstellen und eine Aussage über ihren "
     "y-Achsenabschnitt nachweisen.",
     "2024MgrundlegendAAnalysis21-b"),
    ("Stelle mit lokaler gleich mittlerer Änderungsrate bestimmen", "Analysis",
     "Ableitung und Änderungsrate",
     "Die Stelle bestimmen, an der die Ableitung gleich der mittleren Änderungsrate über ein "
     "Intervall ist, dessen Sekante als Gerade gegeben ist.",
     "2024MgrundlegendAAnalysis22"),
    ("Verflechtungsdiagramm zu einer Matrix zeichnen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Aus einer Verflechtungsmatrix ein beschriftetes Diagramm mit Knoten und Pfeilen zeichnen.",
     "2024MgrundlegendAAGLAA111-a"),
    ("Matrixeintrag aus Mengenbedingungen ermitteln", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Einen unbekannten Eintrag einer Verflechtungsmatrix aus Verhältnisangaben zwischen "
     "Rohstoff- und Produktmengen über eine Zeile des Produkts ermitteln.",
     "2024MgrundlegendAAGLAA111-b"),
    ("Flächenverhältnis von Dreieck und Trapez über einen Vektorterm ermitteln", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Einen durch einen Vektorterm gegebenen vierten Punkt konstruieren und das Verhältnis der "
     "Flächeninhalte von Dreieck und Trapez über gemeinsame Höhe und Grundseiten ermitteln.",
     "2024MgrundlegendAAGLAA112"),
    ("Existenz mehrerer Lösungen von M · a = 0 begründen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Über das Gleichungssystem begründen, dass eine Matrix neben dem Nullvektor weitere Vektoren "
     "auf den Nullvektor abbildet.",
     "2024MgrundlegendAAGLAA12-a"),
    ("Alle Fixvektoren einer Matrix ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Die Lösungsmenge von M · b = b mit freien Parametern beschreiben.",
     "2024MgrundlegendAAGLAA12-b"),
    ("Verschobenen Punkt über den Diagonalenschnittpunkt bestimmen", "Analytische Geometrie",
     "Vektoren und Rechenoperationen",
     "Den Bildpunkt einer Verschiebung bestimmen, die den Diagonalenschnittpunkt eines Körpers "
     "in den Ursprung bringt: Mittelpunkt berechnen, Verschiebungsvektor anwenden.",
     "2024MgrundlegendAAGLAA211-b"),
    ("Eckpunkt mit vorgegebenen Vorzeichen nach einer Verschiebung angeben", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Nach einer Verschiebung des Körpers den Eckpunkt angeben, dessen Koordinaten eine "
     "Vorzeichenbedingung erfüllen, aus der Lage relativ zum Mittelpunkt.",
     "2024MgrundlegendAAGLAA211-c"),
    ("Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden",
     "Analytische Geometrie", "Lagebeziehungen",
     "Entscheiden, ob eine Gerade durch zwei Punkte (mit Parameter) parallel zu einer "
     "Koordinatenebene sein kann, über die Gleichheit der entsprechenden Koordinaten.",
     "2024MgrundlegendAAGLAA213-a"),
    ("Parameter für einen rechten Winkel über das Skalarprodukt ermitteln", "Analytische Geometrie",
     "Orthogonalität",
     "Die Parameterwerte ermitteln, für die ein Dreieck an einer Ecke einen rechten Winkel hat, "
     "über das Skalarprodukt der Schenkelvektoren.",
     "2024MgrundlegendAAGLAA213-b"),
    ("Diagonalenschnittpunkt und Flächeninhalt eines Quadrats aus dem Spurpunkt einer Geraden bestimmen",
     "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Diagonalenschnittpunkt eines Quadrats in einer Koordinatenebene als Spurpunkt einer "
     "Geraden bestimmen und den Flächeninhalt über die halbe Diagonale berechnen.",
     "2024MgrundlegendAAGLAA221"),
    ("Pfadwahrscheinlichkeit für lauter Treffer berechnen und mit einer Schranke vergleichen",
     "Stochastik", "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit, dass alle Versuche Treffer sind, als Potenz berechnen und mit einer "
     "vorgegebenen Schranke vergleichen.",
     "2024MgrundlegendAStochastik11-a"),
    ("Erwartungswert der Auszahlung mit dem Einsatz vergleichen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Den Erwartungswert der Auszahlung eines Spiels berechnen und aus dem Vergleich mit dem "
     "Einsatz begründen, wer auf lange Sicht gewinnt.",
     "2024MgrundlegendAStochastik12-b"),
    ("Auswahlen mit Abstandsbedingung aufzählen", "Stochastik", "Kombinatorik",
     "Alle Auswahlen von Plätzen in einer Reihe aufzählen, die eine Abstandsbedingung erfüllen.",
     "2024MgrundlegendAStochastik13-a"),
    ("Anzahl der Sitzordnungen mit Abstandsbedingung berechnen", "Stochastik", "Kombinatorik",
     "Die Anzahl der Möglichkeiten berechnen, unterscheidbare Personen auf zulässige Platzauswahlen "
     "zu verteilen: Anzahl der Auswahlen mal Anzahl der Anordnungen.",
     "2024MgrundlegendAStochastik13-b"),
    ("Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Aus bedingten Angaben im Text die Wahrscheinlichkeit eines zweistufigen Pfads als Produkt "
     "berechnen.",
     "2024MgrundlegendAStochastik21-a"),
    ("Sachaussage zu einer Ungleichung mit Binomialsumme formulieren", "Stochastik", "Binomialverteilung",
     "Eine gegebene Ungleichung mit kumulierter Binomialwahrscheinlichkeit, deren Parameter aus "
     "einer Gleichung im Sachzusammenhang stammt, als Aussage im Sachzusammenhang formulieren.",
     "2024MgrundlegendAStochastik21-b"),
    ("Baumdiagramm eines Befragungsverfahrens mit unbekanntem Anteil vervollständigen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Ein zweistufiges Baumdiagramm mit einem unbekannten Anteil p vervollständigen, wobei eine "
     "Stufe die Verneinung der anderen abfragt (p und 1 − p vertauscht).",
     "2024MgrundlegendAStochastik22-a"),
    ("Anteil aus dem Ergebnis eines Befragungsverfahrens berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Den unbekannten Anteil p aus der beobachteten Ja-Häufigkeit berechnen, indem die Summe der "
     "Ja-Pfade mit der relativen Häufigkeit gleichgesetzt wird.",
     "2024MgrundlegendAStochastik22-b"),
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
