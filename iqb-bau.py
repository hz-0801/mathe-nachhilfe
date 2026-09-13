# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.2 · 13.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.2

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

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
    "stapel": "2026-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2026MerhoehtAAnalysis11": 5,
        "2026MerhoehtAAnalysis12": 5,
        "2026MerhoehtAAnalysis13": 5,
        "2026MerhoehtAAnalysis14": 5,
        "2026MerhoehtAAnalysis21": 5,
        "2026MerhoehtAAnalysis22": 5,
        "2026MerhoehtAAnalysis23": 5,
        "2026MerhoehtAAGLAA11": 5,
        "2026MerhoehtAAGLAA121": 5,
        "2026MerhoehtAAGLAA122": 5,
        "2026MerhoehtAAGLAA211": 5,
        "2026MerhoehtAAGLAA212": 5,
        "2026MerhoehtAAGLAA221": 5,
        "2026MerhoehtAAGLAA222": 5,
        "2026MerhoehtAAGLAA223": 5,
        "2026MerhoehtAStochastik11": 5,
        "2026MerhoehtAStochastik12": 5,
        "2026MerhoehtAStochastik21": 5,
        "2026MerhoehtAStochastik22": 5,
        "2026MerhoehtAStochastik23": 5,
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
    "neue_typen_anteil": 0.60, "neue_typen_ab_bestand": 100,
    "ersatzweise_anteil": 0.10, "ersatzweise_mindestens": 2,
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

# ---- Analysis 1.1: Exponentialfunktionen, senkrechter Schnitt
row("2026MerhoehtAAnalysis11", "a", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Abbildung zwischen zwei Graphen angeben", typ_neben="",
    stichwoerter="e-Funktion|Spiegelung an der y-Achse|f(x) = g(−x)|Parameter k",
    voraussetzungen="Vorzeichenwechsel im Exponenten als Spiegelung deuten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="k > 0; f(x) = 2e^(k · x) und g(x) = 2e^(−k · x), beide in IR definiert",
    gesucht="wie der Graph von f aus dem Graphen von g erzeugt werden kann",
    verfahren="f(x) = g(−x) erkennen, also Spiegelung an der y-Achse",
    schritte="1", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="durch Spiegelung an der y-Achse (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Spiegelung an der x-Achse angeben, weil nur das Vorzeichen wechselt",
    bemerkung="Standardbezug: K2 II, K4 II, K6 I. Amtlich.")

row("2026MerhoehtAAnalysis11", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Parameter aus dem senkrechten Schnitt zweier Graphen bestimmen", typ_neben="",
    stichwoerter="Schnittstelle x = 0|Ableitung der e-Funktion|Steigungen ±2k|senkrecht heißt Produkt der Steigungen −1|k = 1/2",
    voraussetzungen="Schnittstelle über Gleichsetzen bestimmen|Kettenregel bei e^(k · x)|Orthogonalitätsbedingung für Steigungen oder Steigungswinkel 45°",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="k > 0; f(x) = 2e^(k · x) und g(x) = 2e^(−k · x), beide in IR definiert; die Graphen von f und g schneiden sich senkrecht",
    gesucht="Wert von k",
    verfahren="Schnittstelle aus 2e^(k · x) = 2e^(−k · x), also x = 0; f'(x) = 2k · e^(k · x), f'(0) = 2k und g'(0) = −2k; senkrechter Schnitt bei symmetrischen Steigungen heißt f'(0) = tan 45° = 1, also 2k = 1",
    schritte="3", zahlenraum="ganz|Bruch|Potenz", einheiten="", abhaengig_von="2026MerhoehtAAnalysis11-a",
    ergebnis="k = 1/2 (amtlich)",
    zwischenergebnis="Schnittstelle x = 0|f'(x) = 2k · e^(k · x)|f'(0) = 2k, g'(0) = −2k|über f'(0) · g'(0) = −1: 4k^2 = 1",
    niveau_geschaetzt="III",
    fehlerquelle="die Bedingung f'(0) · g'(0) = −1 mit der Symmetrie verwechseln und 2k = −(−2k) setzen",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt (über das Produkt der Steigungen). Schätzung III nach der Regel „Kombinieren heißt III“ (Schnittstelle, Ableitung, Winkelbedingung), amtlich bis II.")

# ---- Analysis 1.2: lineare Funktion, Integral null, Stammfunktionen
LIN_SKIZZE = ("Koordinatensystem mit x-Achse von −1 bis 5 und y-Achse von −4 bis 5, Gitter; die "
              "Gerade g(x) = −2x + 4 fallend durch (0; 4) und (2; 0), bei x = 4 bei −4")
row("2026MerhoehtAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integral mit Wert null am Graphen veranschaulichen", typ_neben="",
    stichwoerter="Integral von 0 bis k gleich null|inhaltsgleiche Flächen über und unter der x-Achse|k = 4|Dreiecke",
    voraussetzungen="Integral als orientierten Flächeninhalt deuten",
    format="Zeichnen", operator="Veranschaulichen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=LIN_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="g(x) = −2x + 4, Graph in der Abbildung; k > 0 ist Lösung der Gleichung Integral von 0 bis k über g(x) dx = 0",
    gesucht="Veranschaulichung der geometrischen Bedeutung der Gleichung in der Abbildung",
    verfahren="k = 4 erkennen; das Dreieck zwischen Graph und x-Achse von 0 bis 2 (über der Achse) und das Dreieck von 2 bis 4 (unter der Achse) markieren und als inhaltsgleich kennzeichnen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="zwei markierte Dreiecksflächen A1 (0 bis 2, über der x-Achse) und A2 (2 bis 4, unter der x-Achse) mit dem Vermerk, dass sie inhaltsgleich sind (amtlich)",
    zwischenergebnis="k = 4",
    niveau_geschaetzt="I",
    fehlerquelle="nur die Nullstelle 2 markieren und k = 2 annehmen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. Amtlich; der Erwartungshorizont zeigt die Abbildung mit den grau markierten Flächen A1 und A2. Das Feld skizze beschreibt das Material, die Lösung ist eine Zeichnung.")

row("2026MerhoehtAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktionen mit einer Wertebedingung bestimmen", typ_neben="",
    stichwoerter="Schar der Stammfunktionen|Integrationskonstante c|Maximum der Stammfunktion|ausschließlich negative Werte|c < −4",
    voraussetzungen="Stammfunktion einer linearen Funktion|Scheitel einer nach unten geöffneten Parabel bestimmen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Koordinatensystem", skizze=LIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="g(x) = −2x + 4, definiert in IR",
    gesucht="alle Stammfunktionen von g, die ausschließlich negative Funktionswerte haben",
    verfahren="alle Stammfunktionen G_c(x) = −x^2 + 4x + c aufstellen; größter Funktionswert im Scheitel bei x = 2: G_c(2) = 4 + c; Bedingung 4 + c < 0",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="G_c(x) = −x^2 + 4x + c mit c < −4 (amtlich)",
    zwischenergebnis="G_c(2) = 4 + c",
    niveau_geschaetzt="II",
    fehlerquelle="c < 0 fordern, ohne den Scheitelwert 4 zu berücksichtigen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Datei mit drei Seiten.")

# ---- Analysis 1.3: Logarithmusfunktionen
LN_SKIZZE = ("Koordinatensystem mit x-Achse von −2 bis 5 und y-Achse von −5 bis 1, Gitter; Graph "
             "von g beschriftet: von unten an der senkrechten Asymptote x = −2 steil steigend, "
             "durch (−1; −1), Nullstelle bei etwa 0,7, dann flach steigend bis etwa (5; 0,95)")
row("2026MerhoehtAAnalysis13", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Nullstelle einer Logarithmusfunktion berechnen", typ_neben="",
    stichwoerter="ln(x + 5) + 1 = 0|Umkehrung mit e|x = e^(−1) − 5|exakter Wert",
    voraussetzungen="Logarithmusgleichung durch Anwenden der e-Funktion lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = ln(x + 5) + 1 mit größtmöglicher Definitionsmenge",
    gesucht="Nullstelle von f",
    verfahren="ln(x + 5) = −1 setzen, e-Funktion anwenden, x + 5 = e^(−1), nach x auflösen",
    schritte="2", zahlenraum="negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="x = e^(−1) − 5 (amtlich)",
    zwischenergebnis="x + 5 = e^(−1)|x ≈ −4,63",
    niveau_geschaetzt="I",
    fehlerquelle="ln(x + 5) = −1 zu x + 5 = −e umformen",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtAAnalysis13", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Parameter einer Logarithmusfunktion aus Asymptote und Punkt ermitteln", typ_neben="",
    stichwoerter="Definitionsbereich ]a; ∞[|senkrechte Asymptote x = −2|Punkt (−1; −1)|ln 1 = 0|a = −2, b = −1",
    voraussetzungen="Definitionsbereich von ln(x − a) kennen|Asymptote am Graphen ablesen|Punkt einsetzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=LN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="g(x) = ln(x − a) + b mit ganzzahligen a und b und größtmöglicher Definitionsmenge; der Graph verläuft durch (−1; −1); Abbildung mit dem Graphen von g, senkrechte Asymptote bei x = −2",
    gesucht="a und b",
    verfahren="Definitionsbereich ]a; ∞[ mit der Asymptote im Bild vergleichen: a = −2; dann (−1; −1) einsetzen: ln 1 + b = −1",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="a = −2 und b = −1 (amtlich)",
    zwischenergebnis="ln(−1 + 2) = 0",
    niveau_geschaetzt="II",
    fehlerquelle="a = 2 setzen, weil der Term x − a lautet",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 1.4: Fläche zwischen e-Funktions-Graphen mit gegebener Stammfunktion
row("2026MerhoehtAAnalysis14", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Schnittstellen zweier Graphen über den gemeinsamen Exponentialfaktor nachweisen", typ_neben="",
    stichwoerter="f(x) = g(x)|gemeinsamer Faktor e^(x/2 + 1)|4 = x^2|x = ±2",
    voraussetzungen="Exponentialfaktor als stets positiv erkennen und kürzen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 4e^(1/2 x + 1) und g(x) = x^2 · e^(1/2 x + 1), beide in IR definiert",
    gesucht="Nachweis, dass sich die Graphen nur für x = −2 und x = 2 schneiden",
    verfahren="Gleichsetzen, durch den positiven Faktor e^(1/2 x + 1) teilen, 4 = x^2 lösen",
    schritte="2", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f(x) = g(x) ist gleichwertig zu 4 = x^2, also x = −2 oder x = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="nur x = 2 angeben oder den Exponentialfaktor gleich null setzen wollen",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtAAnalysis14", "b", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche zwischen zwei Graphen mit vorgegebener Stammfunktion berechnen", typ_neben="",
    stichwoerter="Fläche zwischen f und g|Grenzen −2 und 2|Stammfunktion G gegeben|Stammfunktion von f selbst bilden|Ergebnis 32",
    voraussetzungen="Stammfunktion von 4e^(1/2 x + 1) mit Faktor 2 bilden|Hauptsatz auf eine Differenz anwenden|e^2-Terme heben sich auf",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 4e^(1/2 x + 1) und g(x) = x^2 · e^(1/2 x + 1); die Graphen schneiden sich nur bei x = −2 und x = 2; G(x) = (2x^2 − 8x + 16) · e^(1/2 x + 1) ist eine Stammfunktion von g",
    gesucht="Inhalt der Fläche, die die Graphen von f und g einschließen",
    verfahren="Integral von −2 bis 2 über f(x) − g(x) mit der Stammfunktion 8e^(1/2 x + 1) − G(x) auswerten; die Terme mit e^2 heben sich auf",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="2026MerhoehtAAnalysis14-a",
    ergebnis="[8e^(1/2 x + 1) − (2x^2 − 8x + 16) · e^(1/2 x + 1)] von −2 bis 2 = 8e^2 − 8e^2 − (8 − 40) = 32 (amtlich)",
    zwischenergebnis="Stammfunktion von f: 8e^(1/2 x + 1)|an der Stelle 2: 8e^2 − 8e^2 = 0|an der Stelle −2: 8 − 40 = −32",
    niveau_geschaetzt="II",
    fehlerquelle="die Stammfunktion von f mit 2e^(1/2 x + 1) ansetzen (Faktor 1/2 im Exponenten vergessen)",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Zwischen −2 und 2 liegt f über g.")

# ---- Analysis 2.1: Wertemenge und Transformation
row("2026MerhoehtAAnalysis21", "a", seite="1", punkte="1", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Fehlende Punktsymmetrie aus der Wertemenge begründen", typ_neben="",
    stichwoerter="Wertemenge [−3; 2[|Punktsymmetrie zum Ursprung|−3 enthalten, 3 nicht|Gegenbeispiel",
    voraussetzungen="Punktsymmetrie als f(−x) = −f(x) und Folge für die Wertemenge kennen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="eine in IR definierte Funktion f mit der Wertemenge [−3; 2[",
    gesucht="Begründung, dass der Graph von f nicht symmetrisch bezüglich des Koordinatenursprungs ist",
    verfahren="bei Punktsymmetrie müsste mit jedem Wert y auch −y angenommen werden; −3 wird angenommen, 3 nicht",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="in der Wertemenge ist −3 enthalten, 3 aber nicht; bei Punktsymmetrie zum Ursprung müsste zu f(x) = −3 der Wert f(−x) = 3 gehören (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="mit der Achsensymmetrie argumentieren oder das offene Intervallende als Grund nennen",
    bemerkung="Standardbezug: K1 II, K2 II. Amtlich. Keine Funktionsgleichung gegeben, Argument allein aus der Wertemenge.")

row("2026MerhoehtAAnalysis21", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Wertemenge einer transformierten Funktion begründen", typ_neben="",
    stichwoerter="h(x) = −2 · f(x − 5) + 1|Spiegelung an der x-Achse|Streckung Faktor 2|Verschiebung um 1 nach oben|Verschiebung in x-Richtung ohne Einfluss|]−3; 7]",
    voraussetzungen="Wirkung von Vorzeichen, Faktor und Summand auf die Wertemenge|Intervallgrenzen mit offen und abgeschlossen vertauschen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f in IR definiert mit Wertemenge [−3; 2[; h(x) = −2 · f(x − 5) + 1, definiert in IR",
    gesucht="Wertemenge von h mit Begründung",
    verfahren="die Verschiebung um 5 in x-Richtung ändert die Wertemenge nicht; Spiegelung an der x-Achse und Streckung mit 2 machen aus [−3; 2[ das Intervall ]−4; 6]; die Verschiebung um 1 nach oben liefert ]−3; 7]",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Wertemenge von h: ]−3; 7]; die Spiegelung an der x-Achse, die Streckung mit Faktor 2 in y-Richtung und die Verschiebung um 1 in positive y-Richtung wirken auf die Wertemenge, die Verschiebung in x-Richtung nicht (amtlich)",
    zwischenergebnis="−2 · [−3; 2[ = ]−4; 6]|+1: ]−3; 7]",
    niveau_geschaetzt="III",
    fehlerquelle="die Verschiebung um 5 auf die Wertemenge anwenden oder die Intervallenden nicht vertauschen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 2.2: Schar h_a = f + a·x, eine waagerechte Tangente (ungegliedert)
KUB2_SKIZZE = ("Koordinatensystem mit x-Achse von −3 bis 3 und y-Achse von −3 bis 3, Gitter; Graph "
               "von f punktsymmetrisch zum Ursprung: Nullstellen −3, 0 und 3, Hochpunkt bei etwa "
               "(−1,7; 3,5), Tiefpunkt bei etwa (1,7; −3,5), im Ursprung fallend mit Steigung etwa −3")
row("2026MerhoehtAAnalysis22", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für genau eine waagerechte Tangente aus dem Graphen bestimmen", typ_neben="",
    stichwoerter="h_a(x) = f(x) + a · x|h_a' = f' + a|Parabel mit Scheitel auf der y-Achse|genau eine Nullstelle von h_a' heißt Scheitel auf der x-Achse|f'(0) ≈ −3 aus dem Graphen|a = 3",
    voraussetzungen="Ableitung einer Summe|waagerechte Tangente als Nullstelle der Ableitung|Steigung im Ursprung am Graphen ablesen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=KUB2_SKIZZE, kontext="ohne", textumfang="lang",
    gegeben="Abbildung des zum Ursprung symmetrischen Graphen einer ganzrationalen Funktion f (Nullstellen −3, 0, 3; Steigung im Ursprung etwa −3); h_a(x) = f(x) + a · x für reelle a; der Graph von h_a' ist für jedes a eine Parabel mit Scheitelpunkt auf der y-Achse; es gibt genau einen ganzzahligen Wert a, für den der Graph von h_a genau eine waagerechte Tangente besitzt",
    gesucht="dieser Wert von a, mithilfe der Abbildung",
    verfahren="h_a'(x) = f'(x) + a; genau eine waagerechte Tangente heißt, die Parabel h_a' berührt die x-Achse im Scheitel bei x = 0, also h_a'(0) = 0 und a = −f'(0); f'(0) über eine Tangente im Ursprung als etwa −3 ablesen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="a = 3 (amtlich)",
    zwischenergebnis="h_a'(x) = f'(x) + a|h_a'(0) = 0 gleichwertig zu a = −f'(0)|f'(0) ≈ −3",
    niveau_geschaetzt="III",
    fehlerquelle="die waagerechte Tangente von h_a an den Extremstellen von f suchen statt im Ursprung",
    bemerkung="Standardbezug: K2 III, K4 II, K5 II, K6 II. Amtlich; der Erwartungshorizont zeigt die Abbildung mit eingezeichneter Tangente im Ursprung und f'(0) ≈ −3. Eigene Rechnung mit f(x) = (x^3 − 9x)/3, die zum Bild passt, bestätigt f'(0) = −3. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE.")

# ---- Analysis 2.3: Nullstellen einer Integralfunktion (ungegliedert)
INT_SKIZZE = ("Koordinatensystem mit x-Achse von −3 bis 4 und y-Achse von −4 bis 4, Gitter; Graph "
              "von f: von links unten (etwa (−3; −4)) steil steigend durch die Nullstelle −1,5, kleines "
              "Maximum bei etwa (−0,8; 0,5), fallend zur Berührstelle im Ursprung, danach steigend und "
              "sich für große x dem Wert 2 nähernd (bei x = 4 etwa 1,9)")
row("2026MerhoehtAAnalysis23", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Anzahl der Nullstellen einer Integralfunktion am Graphen beurteilen", typ_neben="",
    stichwoerter="Integralfunktion J mit unterer Grenze 0|J(0) = 0|J' = f|streng monoton für x > 0|Flächenbilanz links von −1,5|genau zwei Nullstellen",
    voraussetzungen="untere Integrationsgrenze als Nullstelle erkennen|J' = f und Monotonie|Integral als Flächenbilanz mit Vorzeichen deuten",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=INT_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Abbildung des Graphen einer in IR definierten differenzierbaren Funktion f mit genau zwei Nullstellen −1,5 und 0 (bei 0 Berührung der x-Achse, für x > 0 positiv, links von −1,5 negativ und unbeschränkt fallend); J(x) = Integral von 0 bis x über f(t) dt; Aussage: J hat genau zwei Nullstellen",
    gesucht="Beurteilung der Aussage",
    verfahren="J(0) = 0 als erste Nullstelle; für x > 0 ist J' = f > 0, J streng monoton steigend, keine Nullstelle; für x < 0 ist J zwischen −1,5 und 0 positiv (Fläche über der Achse, von rechts nach links durchlaufen), und links von −1,5 nimmt J wegen der großen negativen Fläche ab, bis der Wert J(−1,5) ausgeglichen ist: genau eine weitere Nullstelle a < −1,5",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="die Aussage ist wahr: 0 ist Nullstelle von J; für x > 0 ist J wegen J' = f > 0 streng monoton steigend ohne Nullstelle; für x < 0 hat J genau eine Nullstelle, weil f dort nur die Nullstelle −1,5 hat und es laut Abbildung ein a < −1,5 gibt, für das das Integral von −1,5 bis a über f gleich −J(−1,5) ist (amtlich)",
    zwischenergebnis="J(−1,5) = Integral von 0 bis −1,5 über f > 0",
    niveau_geschaetzt="III",
    fehlerquelle="die Nullstellen von f für Nullstellen von J halten und die Aussage deshalb für wahr erklären, ohne die Flächenbilanz zu betrachten",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 III. Amtlich. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE.")

# ---- AG/LA (A1) 1: Übergangsmatrix Insekten (einzige Aufgabe der Gruppe, Text auf Seite 1 und 2)
UEB_SKIZZE = ("Übergangsdiagramm mit drei Knoten C (oben links), B (oben rechts), A (unten Mitte); "
              "Pfeile mit Beschriftung: B nach C 0,6, C nach B 0, A nach C 0, C nach A 2, A nach B r, "
              "B nach A 0; Schleifen an A, B und C je 0")
row("2026MerhoehtAAGLAA11", "a", seite="1|2", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Fehler in einem Übergangsdiagramm gegen die Matrix begründen", typ_neben="",
    stichwoerter="Übergangsmatrix 3 mal 3|Übergangsdiagramm|Pfeilbeschriftung vertauscht|Spalte gibt Ausgangsstadium an",
    voraussetzungen="Matrixeintrag m_ij als Übergang von Stadium j nach Stadium i lesen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Diagramm", skizze=UEB_SKIZZE, kontext="Biologie/Insektenpopulation", textumfang="lang",
    gegeben="Population in drei Stadien A, B, C; Verteilung v_n = (A; B; C); Übergang von einem Tag zum nächsten v_(n+1) = M · v_n mit M = ((0; 0; 2), (r; 0; 0), (0; 0,6; 0)), r reell; v_0 ungleich Nullvektor; das abgebildete Übergangsdiagramm",
    gesucht="Begründung, dass das Übergangsdiagramm fehlerhaft ist",
    verfahren="Einträge der Matrix mit den Pfeilen vergleichen: M sagt A nach B mit r, B nach C mit 0,6, C nach A mit 2; im Diagramm sind die Pfeile zwischen A und C mit 2 und 0 vertauscht beschriftet",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="im Diagramm ist die Beschriftung der Pfeile zwischen A und C vertauscht: nach der Matrix geht der Übergang mit Faktor 2 von C nach A, nicht von A nach C (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten der Matrix vertauscht lesen und das Diagramm für richtig halten",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I. Amtlich. Der Aufgabenstamm steht auf Seite 1, die Teilaufgaben mit dem Diagramm auf Seite 2; Datei mit drei Seiten. Thema Matrizen und Übergangsprozesse (nur A1, iqb.md § 6).")

row("2026MerhoehtAAGLAA11", "b", seite="1|2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Parameter einer Übergangsmatrix aus einer Zykluslänge bestimmen", typ_neben="",
    stichwoerter="M hoch 3|Matrizenmultiplikation|M^3 = 1,2r · E|Verteilung nach drei Tagen gleich Anfangsverteilung|r = 5/6",
    voraussetzungen="Matrizen multiplizieren|Vielfaches der Einheitsmatrix erkennen|v_3 = M^3 · v_0",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=UEB_SKIZZE, kontext="Biologie/Insektenpopulation", textumfang="mittel",
    gegeben="v_(n+1) = M · v_n mit M = ((0; 0; 2), (r; 0; 0), (0; 0,6; 0)), r reell, v_0 ungleich Nullvektor; nach drei Tagen stimmt die Verteilung mit der zu Beobachtungsbeginn überein",
    gesucht="Wert von r",
    verfahren="M^3 berechnen: M^2 = ((0; 1,2; 0), (0; 0; 2r), (0,6r; 0; 0)), M^3 = 1,2r · E; aus v_3 = M^3 · v_0 = v_0 und v_0 ungleich Nullvektor folgt 1,2r = 1",
    schritte="3", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="r = 5/6 (amtlich)",
    zwischenergebnis="M^2 = ((0; 1,2; 0), (0; 0; 2r), (0,6r; 0; 0))|M^3 = ((1,2r; 0; 0), (0; 1,2r; 0), (0; 0; 1,2r))",
    niveau_geschaetzt="II",
    fehlerquelle="M^3 als komponentenweise dritte Potenz der Einträge bilden",
    bemerkung="Standardbezug: K1 II, K2 I, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A1) 2.1: Eigenvektor und inverse Matrix
row("2026MerhoehtAAGLAA121", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen", typ_neben="",
    stichwoerter="A · v = 4 · v|Eigenvektor|zweite Komponente 4a = 4|a = 1",
    voraussetzungen="Matrix-Vektor-Produkt komponentenweise ausrechnen|eine geeignete Komponente auswählen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A = ((6; −2; 0), (4; 0; 0), (−4; 4; −2)); v_a = (a; 1; 0) mit reellem a; es gilt A · v_a = 4 · v_a",
    gesucht="Wert von a",
    verfahren="A · v_a = (6a − 2; 4a; −4a + 4) mit 4 · v_a = (4a; 4; 0) vergleichen; die zweite Komponente liefert 4a = 4",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="a = 1 (amtlich)",
    zwischenergebnis="A · v_a = (6a − 2; 4a; 4 − 4a)",
    niveau_geschaetzt="II",
    fehlerquelle="aus der ersten Komponente 6a − 2 = 4a rechnen und den Wert nicht an den übrigen Komponenten prüfen",
    bemerkung="Standardbezug: K1 II, K2 I, K5 I. Amtlich, eigene Rechnung bestätigt: alle drei Komponenten stimmen für a = 1.")

row("2026MerhoehtAAGLAA121", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Gleichung mit inverser Matrix über die Eigenvektorbeziehung lösen", typ_neben="",
    stichwoerter="A^(−1) · (b · v) = c · v|Multiplikation mit A|A · v = 4 · v nutzen|b = 4c|ohne Berechnung der Inversen",
    voraussetzungen="A · A^(−1) = E anwenden|Linearität des Matrix-Vektor-Produkts|Vektorgleichung mit v ungleich Nullvektor kürzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="A = ((6; −2; 0), (4; 0; 0), (−4; 4; −2)); v_a = (1; 1; 0) mit A · v_a = 4 · v_a; für jedes reelle c gibt es ein reelles b mit A^(−1) · (b · v_a) = c · v_a; A^(−1) soll nicht berechnet werden",
    gesucht="b in Abhängigkeit von c",
    verfahren="beide Seiten mit A multiplizieren: b · v_a = A · (c · v_a) = c · (A · v_a) = c · 4 · v_a; weil v_a nicht der Nullvektor ist, folgt b = 4c",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2026MerhoehtAAGLAA121-a",
    ergebnis="b = 4c (amtlich)",
    zwischenergebnis="b · v_a = 4c · v_a",
    niveau_geschaetzt="III",
    fehlerquelle="b = c/4 angeben, weil die Inverse den Faktor umkehrt, ohne die Gleichung umzuformen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A1) 2.2: orthogonale Matrizen
row("2026MerhoehtAAGLAA122", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrix mit vorgegebener Eigenschaft angeben", typ_neben="",
    stichwoerter="transponierte Matrix|orthogonal heißt M · M^T = E|Einträge 0 und 1|Vertauschungsmatrix",
    voraussetzungen="Definition der Transponierten anwenden|Matrizenprodukt 2 mal 2",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="für M = ((a; b), (c; d)) ist M^T = ((a; c), (b; d)) die transponierte Matrix; M heißt orthogonal, wenn M · M^T = ((1; 0), (0; 1))",
    gesucht="eine orthogonale Matrix der Form M mit a, b, c, d aus {0; 1}, die nicht die Einheitsmatrix ist",
    verfahren="eine Matrix wählen, deren Zeilen die Länge 1 haben und zueinander senkrecht sind, etwa die Vertauschung der beiden Einheitsvektoren",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="M = ((0; 1), (1; 0)) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="eine Matrix mit einer Nullzeile angeben, deren Produkt mit der Transponierten nicht die Einheitsmatrix ist",
    bemerkung="Standardbezug: K1 I, K2 I, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt. Transponierte und orthogonale Matrix werden in der Aufgabe definiert.")

row("2026MerhoehtAAGLAA122", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Existenz von Matrizen mit vorgegebener Eigenschaft über ein Gleichungssystem beurteilen", typ_neben="",
    stichwoerter="M · M^T = E ausmultiplizieren|a = d = √5/3|5/9 + b^2 = 1|b = ±2/3, c = −b|zwei verschiedene Matrizen",
    voraussetzungen="Matrizenprodukt mit Variablen|nichtlineares Gleichungssystem lösen|Fallunterscheidung im Ergebnis",
    format="Begründung|Rechnung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="M = ((a; b), (c; d)) orthogonal, wenn M · M^T = ((1; 0), (0; 1)); Aussage: es gibt orthogonale Matrizen der Form M mit a = d = 1/3 · √5, die ungleich sind",
    gesucht="Beurteilung der Aussage",
    verfahren="M · M^T mit a = d = √5/3 ausmultiplizieren: 5/9 + b^2 = 1, (√5/3) · b + (√5/3) · c = 0, c^2 + 5/9 = 1; daraus b = 2/3 und c = −2/3 oder b = −2/3 und c = 2/3",
    schritte="4", zahlenraum="Bruch|Wurzel|negativ", einheiten="", abhaengig_von="2026MerhoehtAAGLAA122-a",
    ergebnis="die Aussage ist wahr: aus 5/9 + b^2 = 1, √5/3 · b + √5/3 · c = 0 und c^2 + 5/9 = 1 folgen genau die beiden Matrizen mit b = 2/3, c = −2/3 und mit b = −2/3, c = 2/3 (amtlich)",
    zwischenergebnis="b^2 = 4/9|c = −b",
    niveau_geschaetzt="III",
    fehlerquelle="aus b^2 = 4/9 nur b = 2/3 nehmen und die Aussage für falsch halten",
    bemerkung="Standardbezug: K1 III, K2 II, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 1.1: Lotgerade und Abstand
row("2026MerhoehtAAGLAA211", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Orthogonalität von Gerade und Ebene über Normalen- und Richtungsvektor begründen",
    typ_neben="Punktprobe an einer Ebenengleichung durchführen",
    stichwoerter="Richtungsvektor gleich Normalenvektor|Koordinatengleichung|Punktprobe|Lotgerade",
    voraussetzungen="Normalenvektor aus der Koordinatengleichung ablesen|Punkt in die Gleichung einsetzen",
    format="Begründung", operator="Begründen Sie|Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (−4; 2; −2) + t · (−2; −1; 2), t reell; E: −2x1 − x2 + 2x3 − 2 = 0; P(−4; 2; −2)",
    gesucht="Begründung, dass g senkrecht zu E steht|Nachweis, dass P in E liegt",
    verfahren="der Richtungsvektor (−2; −1; 2) von g ist zugleich Normalenvektor von E; P einsetzen: −2 · (−4) − 2 + 2 · (−2) − 2 = 0",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="der Vektor (−2; −1; 2) ist Richtungsvektor von g und Normalenvektor von E, also steht g senkrecht auf E|−2 · (−4) − 2 + 2 · (−2) − 2 = 0, also liegt P in E (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="das Skalarprodukt von Richtungs- und Normalenvektor gleich null erwarten",
    bemerkung="Standardbezug: K1 I, K2 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Beide Typen aus 2026-ga-A (AGLAA211-a) wiederverwendet, Reihenfolge der Leistungen hier umgekehrt.")

row("2026MerhoehtAAGLAA211", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt auf einer Lotgeraden mit vorgegebenem Abstand zur Ebene bestimmen", typ_neben="",
    stichwoerter="Lotgerade durch P in E|Betrag des Richtungsvektors 3|Abstand 12 heißt t = ±4|Punkt (−12; −2; 6)",
    voraussetzungen="Abstand entlang der Lotgeraden als Vielfaches des Richtungsvektors|Vektorlänge berechnen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (−4; 2; −2) + t · (−2; −1; 2), t reell, steht senkrecht auf E: −2x1 − x2 + 2x3 − 2 = 0; P(−4; 2; −2) liegt in E und auf g",
    gesucht="Koordinaten eines Punktes auf g mit Abstand 12 zu E",
    verfahren="der Abstand eines Punktes von g zu E ist |t| · |(−2; −1; 2)| = 3|t|; für Abstand 12 also t = 4 oder t = −4; Punkt einsetzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MerhoehtAAGLAA211-a",
    ergebnis="|(−2; −1; 2)| = 3; (−4; 2; −2) + 4 · (−2; −1; 2) = (−12; −2; 6) (amtlich)",
    zwischenergebnis="t = ±4|zweiter möglicher Punkt (4; 6; −10)",
    niveau_geschaetzt="II",
    fehlerquelle="t = 12 einsetzen, ohne den Richtungsvektor auf die Länge 1 zu beziehen",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 1.2: Prisma (Variante von 2026MgrundlegendAAGLAA213)
PRISMA_SKIZZE = ("Schrägbild eines dreiseitigen geraden Prismas ABCDEF in einem räumlichen "
                 "Koordinatensystem mit x-Achse nach vorn links, y-Achse nach rechts, z-Achse nach "
                 "oben; Grundfläche das Dreieck A(0; 0; 0), B(6; 0; 0), C(0; 4; 0), Deckfläche "
                 "D(0; 0; 3), E(6; 0; 3), F(0; 4; 3); die Kanten AD und AC verdeckt gestrichelt; "
                 "Buchstaben an allen Ecken")
row("2026MerhoehtAAGLAA212", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Koordinaten eines Eckpunkts eines Prismas angeben", typ_neben="",
    stichwoerter="gerades Prisma|Deckfläche|Eckpunkt F|Verschiebung um die Höhe",
    voraussetzungen="Punkt im Schrägbild dem Koordinatensystem zuordnen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Körper", skizze=PRISMA_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="gerades Prisma ABCDEF mit A(0; 0; 0), B(6; 0; 0), C(0; 4; 0) und D(0; 0; 3), Abbildung",
    gesucht="Koordinaten des Punktes F",
    verfahren="F liegt senkrecht über C in der Höhe von D",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="F(0; 4; 3) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="E und F verwechseln und (6; 0; 3) angeben",
    bemerkung="Standardbezug: K4 I. Amtlich. Gleicher Aufgabenstamm wie 2026MgrundlegendAAGLAA213 (Variante auf erhöhtem Niveau mit anderer Teilaufgabe b).")

row("2026MerhoehtAAGLAA212", "b", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Parameter eines Punktes aus einer Flächengleichheit bestimmen", typ_neben="",
    stichwoerter="Dreieck APC gegen Rechteck ACFD|P(k; 0; 3) auf DE|Rechteckfläche 12|1/2 · |AC| · |AP| = |AC| · |AD||k = √27",
    voraussetzungen="Ansatz für P auf der Kante DE|Orthogonalität von AC und AP erkennen|Rechteckfläche|Wurzelgleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=PRISMA_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Prisma mit A(0; 0; 0), B(6; 0; 0), C(0; 4; 0), D(0; 0; 3), E(6; 0; 3), F(0; 4; 3); P liegt auf der Kante DE; das Dreieck APC hat den gleichen Flächeninhalt wie das Viereck ACFD",
    gesucht="Koordinaten von P",
    verfahren="P(k; 0; 3) mit k > 0 ansetzen; AC steht senkrecht auf AP, also Dreiecksfläche 1/2 · |AC| · |AP|; das Rechteck ACFD hat |AC| · |AD|; gleichsetzen: 1/2 · √(k^2 + 9) = 3",
    schritte="4", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="2026MerhoehtAAGLAA212-a",
    ergebnis="P(√27; 0; 3), also k = √27 (amtlich)",
    zwischenergebnis="|AC| = 4, |AD| = 3|√(k^2 + 3^2) = 6|k ≈ 5,20",
    niveau_geschaetzt="II",
    fehlerquelle="das Viereck ACFD als Dreieck behandeln oder den Faktor 1/2 auf beiden Seiten setzen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2026MgrundlegendAAGLAA213-c wiederverwendet; dort Dreieck gegen Dreieck, hier Dreieck gegen Rechteck, derselbe Lösungsweg – Vorschlag, die Definition auf beide Fälle zu fassen.")

# ---- AG/LA (A2) 2.1: Geradenschar in einer Ebene, gleicher Abstand
row("2026MerhoehtAAGLAA221", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen", typ_neben="",
    stichwoerter="Geradenschar in einer Ebene|Stützpunkt einsetzen|2x2 + x3 = c|c = −5",
    voraussetzungen="gemeinsamen Stützpunkt der Schar erkennen|Punkt in die Koordinatengleichung einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="g_a: x = (1; −1; −3) + t · (1; a; −2a) für reelle a und t; E: 2x2 + x3 = c; jede Gerade g_a liegt in E",
    gesucht="Wert von c",
    verfahren="der gemeinsame Punkt (1; −1; −3) aller Geraden liegt in E: 2 · (−1) + (−3) = c",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="c = −5 (amtlich)",
    zwischenergebnis="Probe: Richtungsvektor (1; a; −2a) mit Normalenvektor (0; 2; 1): 2a − 2a = 0",
    niveau_geschaetzt="I",
    fehlerquelle="den Richtungsvektor statt des Stützpunkts einsetzen",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtAAGLAA221", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Gleichen Abstand eines Punktes zu einer Geradenschar über den Lotfußpunkt beurteilen", typ_neben="",
    stichwoerter="ohne Abstandsberechnung|gemeinsamer Punkt Q aller Geraden|PQ kollinear zum Normalenvektor|Q ist Lotfußpunkt von P auf E|Aussage wahr",
    voraussetzungen="Abstand Punkt-Gerade als Länge des Lots|Lotfußpunkt auf der Ebene über den Normalenvektor erkennen|Schar als Geradenbüschel durch einen Punkt deuten",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="g_a: x = (1; −1; −3) + t · (1; a; −2a), alle in E: 2x2 + x3 = −5; P(1; 3; −1); Aussage: P hat zu jeder Geraden g_a den gleichen Abstand; Abstände sollen nicht berechnet werden",
    gesucht="Beurteilung der Aussage",
    verfahren="Q(1; −1; −3) ist gemeinsamer Punkt aller g_a; PQ = (0; −4; −2) ist kollinear zum Normalenvektor (0; 2; 1) von E, also ist Q der Lotfußpunkt von P auf E; das Lot von P auf E steht senkrecht auf jeder Geraden durch Q in E, der Abstand ist stets |PQ|",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MerhoehtAAGLAA221-a",
    ergebnis="die Aussage ist wahr: Q(1; −1; −3) liegt auf jeder g_a, PQ = (0; −4; −2) ist kollinear zum Normalenvektor (0; 2; 1), also ist Q der Lotfußpunkt von P auf E und P hat zu jeder Geraden den Abstand |PQ| (amtlich)",
    zwischenergebnis="PQ = −2 · (0; 2; 1)|zum Vergleich |PQ| = √20",
    niveau_geschaetzt="III",
    fehlerquelle="Abstände für einzelne Werte von a berechnen und daraus verallgemeinern",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 III. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 2.2: Dreiecke mit zwei Parametern
GER_SKIZZE = ("Koordinatensystem mit s-Achse von −4 bis 4 und t-Achse von −6 bis 9, Gitter; eine "
              "Gerade durch den Ursprung mit Steigung 5 (durch (1; 5) und (−1; −5))")
row("2026MerhoehtAAGLAA222", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Rechten Winkel eines Dreiecks mit Parameter nachweisen", typ_neben="",
    stichwoerter="B_s in der xy-Ebene|C_t auf der z-Achse|rechter Winkel in A für alle s, t|Skalarprodukt (4s; 3s; 0) · (0; 0; t) = 0",
    voraussetzungen="Lage der Punkte in Koordinatenebene und Achse erkennen oder Skalarprodukt mit Parametern",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GER_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Dreiecke AB_sC_t mit A(0; 0; 0), B_s(4s; 3s; 0) und C_t(0; 0; t), s und t positiv reell",
    gesucht="Begründung, dass jedes Dreieck AB_sC_t in A rechtwinklig ist",
    verfahren="die Seite AB_s liegt in der xy-Ebene, die Seite AC_t auf der z-Achse, die auf dieser Ebene senkrecht steht; rechnerisch ist (4s; 3s; 0) · (0; 0; t) = 0",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="AB_s liegt in der xy-Ebene und AC_t auf der z-Achse, die senkrecht zur xy-Ebene steht, also ist der Winkel bei A für alle s und t ein rechter (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur für ein Zahlenbeispiel von s und t rechnen",
    bemerkung="Standardbezug: K1 II, K2 I, K4 II, K6 I. Amtlich. Typ aus 2026MgrundlegendAAGLAA112-a wiederverwendet; der Erwartungshorizont argumentiert über die Lage, das Skalarprodukt führt zum selben Nachweis. Das abgebildete s-t-Koordinatensystem gehört zu Teilaufgabe b.")

row("2026MerhoehtAAGLAA222", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen",
    typ_neben="Beziehung zweier Parameter mit einer abgebildeten Geraden abgleichen",
    stichwoerter="|AB_s| = |AC_t||√((4s)^2 + (3s)^2) = 5s|t = 5s|Gerade durch den Ursprung mit Steigung 5|Punkte (s; t)",
    voraussetzungen="Vektorbetrag mit Parameter|Gleichung der abgebildeten Geraden ablesen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GER_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Dreiecke AB_sC_t mit A(0; 0; 0), B_s(4s; 3s; 0), C_t(0; 0; t), s und t positiv, rechtwinklig in A; zu jedem s gibt es ein t mit gleichschenkligem Dreieck; Abbildung eines s-t-Koordinatensystems mit einer Geraden durch den Ursprung mit Steigung 5",
    gesucht="Nachweis, dass die zugehörigen Punkte (s; t) auf der abgebildeten Geraden liegen",
    verfahren="gleichschenklig im rechten Winkel heißt |AB_s| = |AC_t|: √(16s^2 + 9s^2) = 5s = t; die abgebildete Gerade hat die Gleichung t = 5s",
    schritte="2", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="2026MerhoehtAAGLAA222-a",
    ergebnis="t = 5s ist eine Gleichung der dargestellten Geraden; |AB_s| = |AC_t| ist gleichwertig zu √((4s)^2 + (3s)^2) = t, also t = 5s (amtlich)",
    zwischenergebnis="|AB_s| = 5s",
    niveau_geschaetzt="III",
    fehlerquelle="die Hypotenuse B_sC_t mit einer Kathete gleichsetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Haupttyp aus 2026MgrundlegendAAGLAA112-b wiederverwendet.")

# ---- AG/LA (A2) 2.3: Symmetrieebenen einer Pyramidenschar (ungegliedert)
row("2026MerhoehtAAGLAA223", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebenen eines Körpers aus den Koordinaten begründen", typ_neben="",
    stichwoerter="Pyramidenschar|Grundfläche Rechteck|Symmetrieebene x = 0|Symmetrieebene y = t|Mittelwert der y-Koordinaten|Spitze in beiden Ebenen",
    voraussetzungen="Spiegelung an einer Koordinatenebene als Vorzeichenwechsel|Mittelebene zweier Punkte über den Mittelwert einer Koordinate|Koordinatengleichung achsenparalleler Ebenen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="lang",
    gegeben="für t > 0 die Pyramide A_tB_tCDS_t mit A_t(1; 1 + 2t; 0), B_t(−1; 1 + 2t; 0), C(−1; −1; 0), D(1; −1; 0) und S_t(0; t; 6); jede Pyramide hat genau zwei Symmetrieebenen",
    gesucht="je eine Gleichung der beiden Symmetrieebenen für jeden Wert von t, mit Begründung",
    verfahren="x = 0: D und C sowie A_t und B_t unterscheiden sich nur im Vorzeichen der x-Koordinate, S_t hat x = 0; y = t: D und A_t sowie C und B_t unterscheiden sich nur in der y-Koordinate mit Mittelwert (1 + 2t − 1)/2 = t, S_t hat y = t",
    schritte="4", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="x = 0 und y = t; bei x = 0 gehen C und D bzw. A_t und B_t durch Vorzeichenwechsel der x-Koordinate ineinander über und S_t liegt in der Ebene; bei y = t ist t der Mittelwert der y-Koordinaten von D und A_t bzw. C und B_t, und S_t liegt in der Ebene (amtlich)",
    zwischenergebnis="Grundfläche ist ein Rechteck mit den Seiten 2 und 2 + 2t|Mittelwert (1 + 2t + (−1))/2 = t",
    niveau_geschaetzt="III",
    fehlerquelle="y = 1 + t als Mitte der Grundfläche schätzen statt den Mittelwert der y-Koordinaten zu bilden",
    bemerkung="Standardbezug: K1 II, K2 III, K4 III, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE. Keine Abbildung.")

# ---- Stochastik 1.1: Binomialverteilung n = 36, p = 0,5
BIN36_SKIZZE = ("Säulendiagramm der Wahrscheinlichkeitsverteilung P(X = k) für k = 0 bis 36 (Achse "
                "beschriftet in Zweierschritten), y-Achse von 0 bis 0,15 mit Marken 0,05, 0,1 und "
                "feinem Gitter; symmetrische Glockenform um k = 18 mit Höhen etwa 0,13 (k = 18), "
                "0,125 (17 und 19), 0,11 (16 und 20), 0,08 (15 und 21), 0,055 (14 und 22), "
                "0,035 (13 und 23), 0,02 (12 und 24), unter 0,01 ab k = 10 bzw. 26")
row("2026MerhoehtAStochastik11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben", typ_neben="",
    stichwoerter="B(36; 0,5)|P(X = 27)|Binomialkoeffizient 36 über 27|Term angeben",
    voraussetzungen="Bernoulli-Formel",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="binomialverteilte Zufallsgröße X mit n = 36 und p = 0,5",
    gesucht="Term, mit dem P(X = 27) berechnet werden kann",
    verfahren="Bernoulli-Formel mit k = 27 aufschreiben",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(36 über 27) · 0,5^27 · 0,5^9 (amtlich)",
    zwischenergebnis="Wert ≈ 0,0018",
    niveau_geschaetzt="I",
    fehlerquelle="den Binomialkoeffizienten weglassen",
    bemerkung="Standardbezug: K5 I. Amtlich. Typ aus 2026MgrundlegendAStochastik12-a wiederverwendet.")

row("2026MerhoehtAStochastik11", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Wahrscheinlichkeit eines Sigma-Intervalls aus dem Säulendiagramm ermitteln", typ_neben="",
    stichwoerter="μ = 18, σ = 3|halbes Sigma-Intervall|P(16,5 <= X <= 19,5) = P(17 <= X <= 19)|Säulen addieren|≈ 0,38",
    voraussetzungen="μ = n · p und σ = √(n · p · (1 − p))|Intervall auf ganze Zahlen übertragen|Säulenhöhen ablesen und addieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=BIN36_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="X binomialverteilt mit n = 36 und p = 0,5; Säulendiagramm der Verteilung mit Höhen etwa 0,13 bei k = 18 und 0,125 bei k = 17 und 19; μ Erwartungswert, σ Standardabweichung",
    gesucht="Näherungswert für P(μ − 0,5 · σ <= X <= μ + 0,5 · σ)",
    verfahren="μ = 36 · 0,5 = 18 und σ = √(18 · 0,5) = 3 berechnen; das Intervall [16,5; 19,5] enthält k = 17, 18, 19; deren Säulenhöhen addieren",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="μ = 18, σ = 3; P(17 <= X <= 19) ≈ 0,13 + 2 · 0,125 = 0,38 (amtlich)",
    zwischenergebnis="μ − 0,5σ = 16,5|μ + 0,5σ = 19,5|exakt 0,382",
    niveau_geschaetzt="III",
    fehlerquelle="σ = √(n · p) = √18 rechnen oder die Grenzen 16,5 und 19,5 auf k = 16 bis 20 runden",
    bemerkung="Standardbezug: K1 II, K2 I, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt (exakt 0,382). Schätzung III nach der Regel „Kombinieren heißt III“ (zwei Kenngrößen, Intervall übersetzen, Diagramm lesen), amtlich bis II.")

# ---- Stochastik 1.2: Glücksrad, abwechselnd drehen
row("2026MerhoehtAStochastik12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Term für die Wahrscheinlichkeit eines mehrstufigen Pfads angeben", typ_neben="",
    stichwoerter="Glücksrad ein Drittel grün|viermal kein Grün|(2/3)^4|unentschieden",
    voraussetzungen="Pfadmultiplikation bei gleichbleibender Wahrscheinlichkeit",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Glücksrad/Spiel", textumfang="lang",
    gegeben="Glücksrad mit drei gleich großen Sektoren, einer grün; A und B drehen abwechselnd, wer zuerst Grün erzielt, gewinnt; nach je zwei Drehungen ohne Grün endet das Spiel unentschieden; A beginnt",
    gesucht="Term für die Wahrscheinlichkeit, dass das Spiel unentschieden endet",
    verfahren="unentschieden heißt viermal nacheinander kein Grün, also (2/3)^4",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(2/3)^4 (amtlich)",
    zwischenergebnis="Wert 16/81",
    niveau_geschaetzt="I",
    fehlerquelle="(1/3)^4 als Wahrscheinlichkeit für vier Fehlversuche ansetzen",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtAStochastik12", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Gewinnwahrscheinlichkeiten in einem Wechselspiel vergleichen", typ_neben="",
    stichwoerter="A gewinnt in Runde 1 oder 3|B gewinnt in Runde 2 oder 4|P(A) = 1/3 + (2/3)^2 · 1/3|P(B) = 2/3 · P(A)|Faktor 1,5|Aussage wahr",
    voraussetzungen="Pfade für die Gewinnzüge aufstellen|Summenregel|Verhältnis zweier Wahrscheinlichkeiten bilden",
    format="Begründung|Rechnung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksrad/Spiel", textumfang="mittel",
    gegeben="Glücksrad mit Trefferwahrscheinlichkeit 1/3; A und B drehen abwechselnd, höchstens je zweimal, A beginnt; wer zuerst Grün erzielt, gewinnt; Aussage: P(A gewinnt) ist das 1,5-Fache von P(B gewinnt)",
    gesucht="Beurteilung der Aussage",
    verfahren="P(A) = 1/3 + (2/3)^2 · 1/3 (erster oder dritter Dreh), P(B) = 2/3 · 1/3 + (2/3)^3 · 1/3 (zweiter oder vierter Dreh) = 2/3 · P(A); also P(A) = 1,5 · P(B)",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2026MerhoehtAStochastik12-a",
    ergebnis="P(A gewinnt) = 1/3 + (2/3)^2 · 1/3 und P(B gewinnt) = 2/3 · 1/3 + (2/3)^3 · 1/3 = 2/3 · P(A gewinnt), also P(A gewinnt) = 1,5 · P(B gewinnt): die Aussage ist wahr (amtlich)",
    zwischenergebnis="P(A) = 13/27|P(B) = 26/81",
    niveau_geschaetzt="II",
    fehlerquelle="für B nur den zweiten Dreh berücksichtigen",
    bemerkung="Standardbezug: K1 II, K2 I, K3 I, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 2.1: zwei Würfel mit Netzen
WUERFEL_SKIZZE = ("zwei Würfelnetze nebeneinander in Kreuzform: Würfel A mit der Reihe 3, 3, 5, 3 "
                  "und darüber und darunter je 5 (drei Dreien, drei Fünfen); Würfel B mit der Reihe "
                  "4, 4, 4, 4 und darüber und darunter je 1 (vier Vieren, zwei Einsen)")
row("2026MerhoehtAStochastik21", "a", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit eines Vergleichs zweier Zufallsgeräte über Pfade berechnen", typ_neben="",
    stichwoerter="Würfelnetze|A: 3 oder 5 je 1/2|B: 4 mit 2/3, 1 mit 1/3|A größer als B mit 2/3|zwei Runden (2/3)^2 = 4/9",
    voraussetzungen="Wahrscheinlichkeiten aus den Netzen ablesen|Fälle für A > B aufstellen|Pfadregeln über zwei Runden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur", skizze=WUERFEL_SKIZZE, kontext="Würfelspiel", textumfang="mittel",
    gegeben="Würfel A mit den Zahlen 3, 3, 3, 5, 5, 5 und Würfel B mit 4, 4, 4, 4, 1, 1 (aus den abgebildeten Netzen); pro Runde wird jeder Würfel einmal geworfen; es werden zwei Runden gespielt",
    gesucht="Wahrscheinlichkeit, dass in beiden Runden mit A eine größere Zahl erzielt wird als mit B",
    verfahren="in einer Runde ist A größer bei A = 5 (Wahrscheinlichkeit 1/2) oder bei A = 3 und B = 1 (1/2 · 1/3), zusammen 2/3; für zwei Runden quadrieren",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="in einer Runde 1/2 · 1/3 + 1/2 = 2/3, in zwei Runden (2/3)^2 = 4/9 (amtlich)",
    zwischenergebnis="P(A = 5) = 1/2|P(A = 3 und B = 1) = 1/6",
    niveau_geschaetzt="III",
    fehlerquelle="den Fall A = 3 und B = 1 vergessen und mit (1/2)^2 rechnen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Die Zahlen stehen nur in der Abbildung.")

row("2026MerhoehtAStochastik21", "b", seite="1", punkte="2", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen", typ_neben="",
    stichwoerter="Summen 4, 6, 7, 9 mit 1/6, 1/6, 1/3, 1/3|alle vier Summen verschieden|4! Anordnungen|Term v · (1/2)^w · (1/3)^2 · (2/3)^2|v = 24, w = 4",
    voraussetzungen="Verteilung der Summe aus den Netzen aufstellen|Permutationen von vier verschiedenen Ergebnissen zählen|Produkt in die vorgegebene Form umschreiben",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Figur", skizze=WUERFEL_SKIZZE, kontext="Würfelspiel", textumfang="lang",
    gegeben="Würfel A mit 3, 3, 3, 5, 5, 5 und B mit 4, 4, 4, 4, 1, 1; vier Runden, je Runde die Summe beider Zahlen; Ereignis: alle vier Summen sind verschieden; Term v · (1/2)^w · (1/3)^2 · (2/3)^2",
    gesucht="natürliche Zahlen v und w, mit denen der Term die Wahrscheinlichkeit des Ereignisses liefert",
    verfahren="mögliche Summen 4, 6, 7, 9 mit den Wahrscheinlichkeiten 1/6, 1/6, 1/3, 1/3; vier verschiedene Summen in vier Runden in 4! = 24 Reihenfolgen; Produkt (1/6)^2 · (1/3)^2 = (1/2)^4 · (1/3)^2 · (2/3)^2 · … umschreiben",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2026MerhoehtAStochastik21-a",
    ergebnis="v = 24; w = 4 (amtlich)",
    zwischenergebnis="P(4) = P(6) = 1/6, P(7) = P(9) = 1/3|Wahrscheinlichkeit 24 · (1/6)^2 · (1/3)^2 = 2/27",
    niveau_geschaetzt="III",
    fehlerquelle="die Reihenfolgen nicht zählen und v = 1 setzen",
    bemerkung="Standardbezug: K2 III, K3 II, K4 III, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt: 24 · (1/2)^4 · (1/3)^2 · (2/3)^2 = 2/27.")

# ---- Stochastik 2.2: Zahlencodes
row("2026MerhoehtAStochastik22", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen", typ_neben="",
    stichwoerter="zwei Zahlencodes|p = 0,1|genau einer enthält die Ziffernfolge|2 · 0,1 · 0,9 = 0,18",
    voraussetzungen="zwei Pfade für genau einen Treffer|Pfadregeln",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Zufallsgenerator/Zahlencodes", textumfang="mittel",
    gegeben="ein Zufallsgenerator erzeugt Zahlencodes; jeder Code enthält eine bestimmte Ziffernfolge mit derselben Wahrscheinlichkeit p; zwei Codes werden erzeugt; p = 0,1",
    gesucht="Wahrscheinlichkeit, dass genau einer der beiden Codes die Ziffernfolge enthält",
    verfahren="zwei Pfade (erster ja, zweiter nein und umgekehrt) mit je 0,1 · 0,9 addieren",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="2 · 0,1 · 0,9 = 0,18 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur einen Pfad rechnen und 0,09 angeben",
    bemerkung="Standardbezug: K3 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt.")

row("2026MerhoehtAStochastik22", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Term für eine bedingte Wahrscheinlichkeit mit Parameter aufstellen", typ_neben="",
    stichwoerter="Bedingung mindestens einer|Gegenereignis 1 − (1 − p)^2|genau einer im Zähler|Term in p|Bruch aus Pfadsummen",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient|Gegenereignis zu mindestens einer|Pfade mit Parameter",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Zufallsgenerator/Zahlencodes", textumfang="mittel",
    gegeben="jeder von zwei erzeugten Zahlencodes enthält die Ziffernfolge mit Wahrscheinlichkeit p, 0 < p < 1; mindestens einer der beiden Codes enthält die Ziffernfolge",
    gesucht="Term in p für die Wahrscheinlichkeit, dass die Ziffernfolge nicht in beiden Codes enthalten ist",
    verfahren="unter der Bedingung mindestens einer ist nicht in beiden gleichbedeutend mit genau einer: Zähler p · (1 − p) + (1 − p) · p, Nenner 1 − (1 − p)^2",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="2026MerhoehtAStochastik22-a",
    ergebnis="(p · (1 − p) + (1 − p) · p) / (1 − (1 − p)^2) (amtlich)",
    zwischenergebnis="gekürzt 2(1 − p)/(2 − p)|für p = 0,1: 18/19",
    niveau_geschaetzt="III",
    fehlerquelle="die Bedingung übersehen und nur 2p(1 − p) angeben",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 2.3: Kugeln mit Zahlen, Erwartungswert
row("2026MerhoehtAStochastik23", "a", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="1 − 2/5 · 1/4|Gegenereignis|zweimal b ohne Zurücklegen|höchstens eine Kugel mit b",
    voraussetzungen="Pfad 2/5 · 1/4 als beide Kugeln mit b lesen|Gegenereignis formulieren",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Urne/Kugeln mit Zahlen", textumfang="mittel",
    gegeben="fünf Kugeln, drei mit der Zahl a, zwei mit der Zahl b; a + b = 17; zwei Kugeln werden gleichzeitig zufällig entnommen; Term 1 − 2/5 · 1/4",
    gesucht="ein Ereignis im Sachzusammenhang, dessen Wahrscheinlichkeit der Term liefert",
    verfahren="2/5 · 1/4 ist die Wahrscheinlichkeit für zwei Kugeln mit b (ohne Zurücklegen); 1 minus das ist das Gegenereignis",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="es wird höchstens eine Kugel mit der Zahl b entnommen (amtlich)",
    zwischenergebnis="Wert 9/10",
    niveau_geschaetzt="II",
    fehlerquelle="das Ereignis als genau eine Kugel mit b beschreiben",
    bemerkung="Standardbezug: K2 I, K3 II, K6 II. Amtlich. Typname aus abi-typen.csv übernommen (dort unter Binomialverteilung), hier Ziehen ohne Zurücklegen.")

row("2026MerhoehtAStochastik23", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Werte einer Zufallsgröße aus dem Erwartungswert bestimmen", typ_neben="",
    stichwoerter="Summe zweier Kugeln|Verteilung 2a mit 3/10, 17 mit 6/10, 2b mit 1/10|E(X) = 16|b = 17 − a|a = 6, b = 11",
    voraussetzungen="Wahrscheinlichkeiten beim Ziehen ohne Zurücklegen|Erwartungswert als gewichtete Summe|lineare Gleichung mit Nebenbedingung lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugeln mit Zahlen", textumfang="mittel",
    gegeben="fünf Kugeln, drei mit a, zwei mit b, a + b = 17, natürliche Zahlen; zwei Kugeln werden gleichzeitig entnommen; X ist die Summe der beiden Zahlen; E(X) = 16",
    gesucht="a und b",
    verfahren="P(2a) = 3/5 · 2/4, P(a + b) = 2 · 3/5 · 2/4, P(2b) = 2/5 · 1/4; Erwartungswert mit b = 17 − a aufstellen und nach a auflösen",
    schritte="4", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="3/5 · 2/4 · 2a + 2 · 3/5 · 2/4 · 17 + 2/5 · 1/4 · 2 · (17 − a) = 16 führt auf 2a + 4 · 17 = 5 · 16, also a = 6 und b = 11 (amtlich)",
    zwischenergebnis="P(X = 2a) = 3/10|P(X = 17) = 6/10|P(X = 2b) = 1/10",
    niveau_geschaetzt="III",
    fehlerquelle="P(a + b) nur mit einer Reihenfolge ansetzen (3/10 statt 6/10)",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. Amtlich, eigene Rechnung bestätigt.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Abbildung zwischen zwei Graphen angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Zu zwei gegebenen Funktionstermen angeben, durch welche Spiegelung, Streckung oder "
     "Verschiebung der eine Graph aus dem anderen hervorgeht.",
     "2026MerhoehtAAnalysis11-a"),
    ("Parameter aus dem senkrechten Schnitt zweier Graphen bestimmen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Den Parameter zweier Funktionen so bestimmen, dass sich ihre Graphen senkrecht schneiden: "
     "Schnittstelle bestimmen, Steigungen dort berechnen und die Orthogonalitätsbedingung "
     "für Steigungen anwenden.",
     "2026MerhoehtAAnalysis11-b"),
    ("Integral mit Wert null am Graphen veranschaulichen", "Analysis",
     "Flächeninhalt durch Integration",
     "Die Gleichung Integral von 0 bis k gleich null am abgebildeten Graphen deuten und die "
     "inhaltsgleichen Flächen über und unter der x-Achse markieren.",
     "2026MerhoehtAAnalysis12-a"),
    ("Stammfunktionen mit einer Wertebedingung bestimmen", "Analysis", "Stammfunktion und Hauptsatz",
     "Die Schar aller Stammfunktionen aufstellen und über den größten oder kleinsten "
     "Funktionswert die Integrationskonstanten bestimmen, für die eine Wertebedingung gilt.",
     "2026MerhoehtAAnalysis12-b"),
    ("Nullstelle einer Logarithmusfunktion berechnen", "Analysis", "Gleichungen lösen",
     "Eine Gleichung der Form ln(x + a) + b = 0 durch Anwenden der e-Funktion exakt lösen.",
     "2026MerhoehtAAnalysis13-a"),
    ("Parameter einer Logarithmusfunktion aus Asymptote und Punkt ermitteln", "Analysis",
     "Rekonstruktion von Funktionsgleichungen",
     "Bei ln(x − a) + b den Parameter a aus der senkrechten Asymptote im abgebildeten Graphen "
     "und b aus einem Punkt des Graphen bestimmen.",
     "2026MerhoehtAAnalysis13-b"),
    ("Schnittstellen zweier Graphen über den gemeinsamen Exponentialfaktor nachweisen", "Analysis",
     "Gleichungen lösen",
     "Beim Gleichsetzen zweier Terme mit demselben positiven Exponentialfaktor diesen kürzen und "
     "die verbleibende Gleichung lösen, um alle Schnittstellen nachzuweisen.",
     "2026MerhoehtAAnalysis14-a"),
    ("Fläche zwischen zwei Graphen mit vorgegebener Stammfunktion berechnen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Inhalt der von zwei Graphen eingeschlossenen Fläche mit dem Hauptsatz berechnen, wobei "
     "eine Stammfunktion vorgegeben ist und die andere selbst gebildet wird.",
     "2026MerhoehtAAnalysis14-b"),
    ("Fehlende Punktsymmetrie aus der Wertemenge begründen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Aus einer Wertemenge, die zu einem Wert y nicht −y enthält, begründen, dass der Graph "
     "nicht punktsymmetrisch zum Ursprung ist.",
     "2026MerhoehtAAnalysis21-a"),
    ("Wertemenge einer transformierten Funktion begründen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Die Wertemenge von a · f(x − d) + e aus der Wertemenge von f herleiten, indem Spiegelung, "
     "Streckung und Verschiebung in y-Richtung auf die Intervallgrenzen angewendet werden.",
     "2026MerhoehtAAnalysis21-b"),
    ("Scharparameter für genau eine waagerechte Tangente aus dem Graphen bestimmen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Für eine Schar f(x) + a · x den Parameter bestimmen, bei dem die Ableitung genau eine "
     "Nullstelle hat, indem die Steigung von f an der passenden Stelle am Graphen abgelesen wird.",
     "2026MerhoehtAAnalysis22"),
    ("Anzahl der Nullstellen einer Integralfunktion am Graphen beurteilen", "Analysis",
     "Stammfunktion und Hauptsatz",
     "Eine Aussage über die Nullstellen einer Integralfunktion beurteilen, über die untere "
     "Grenze als Nullstelle, die Monotonie aus dem Vorzeichen des Integranden und die "
     "Flächenbilanz am abgebildeten Graphen.",
     "2026MerhoehtAAnalysis23"),
    ("Fehler in einem Übergangsdiagramm gegen die Matrix begründen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Ein Übergangsdiagramm mit der zugehörigen Übergangsmatrix vergleichen und einen "
     "Widerspruch in der Pfeilbeschriftung benennen.",
     "2026MerhoehtAAGLAA11-a"),
    ("Parameter einer Übergangsmatrix aus einer Zykluslänge bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Aus der Bedingung, dass eine Verteilung nach n Schritten wieder erreicht wird, über die "
     "Matrixpotenz M^n den unbekannten Eintrag der Übergangsmatrix bestimmen.",
     "2026MerhoehtAAGLAA11-b"),
    ("Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Aus einer Gleichung A · v = k · v den unbekannten Eintrag des Vektors über eine geeignete "
     "Komponente bestimmen.",
     "2026MerhoehtAAGLAA121-a"),
    ("Gleichung mit inverser Matrix über die Eigenvektorbeziehung lösen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Eine Gleichung mit A^(−1) ohne Berechnung der Inversen lösen, indem beide Seiten mit A "
     "multipliziert und A · v = k · v sowie die Linearität genutzt werden.",
     "2026MerhoehtAAGLAA121-b"),
    ("Matrix mit vorgegebener Eigenschaft angeben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Zu einer in der Aufgabe definierten Eigenschaft (etwa Orthogonalität) eine passende "
     "Matrix mit vorgegebenen Einträgen angeben.",
     "2026MerhoehtAAGLAA122-a"),
    ("Existenz von Matrizen mit vorgegebener Eigenschaft über ein Gleichungssystem beurteilen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine Aussage über die Existenz von Matrizen mit einer definierten Eigenschaft beurteilen, "
     "indem die Eigenschaft in ein Gleichungssystem für die Einträge übersetzt und gelöst wird.",
     "2026MerhoehtAAGLAA122-b"),
    ("Punkt auf einer Lotgeraden mit vorgegebenem Abstand zur Ebene bestimmen",
     "Analytische Geometrie", "Abstände",
     "Auf einer zur Ebene senkrechten Geraden durch einen Ebenenpunkt den Punkt mit gegebenem "
     "Abstand zur Ebene über die Länge des Richtungsvektors bestimmen.",
     "2026MerhoehtAAGLAA211-b"),
    ("Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen",
     "Analytische Geometrie", "Lagebeziehungen",
     "Den freien Parameter einer Koordinatengleichung bestimmen, indem ein Punkt eingesetzt "
     "wird, der in der Ebene liegen soll.",
     "2026MerhoehtAAGLAA221-a"),
    ("Gleichen Abstand eines Punktes zu einer Geradenschar über den Lotfußpunkt beurteilen",
     "Analytische Geometrie", "Abstände",
     "Ohne Abstandsrechnung beurteilen, ob ein Punkt zu allen Geraden einer Schar in einer Ebene "
     "denselben Abstand hat, indem der gemeinsame Punkt der Schar als Lotfußpunkt erkannt wird.",
     "2026MerhoehtAAGLAA221-b"),
    ("Beziehung zweier Parameter mit einer abgebildeten Geraden abgleichen", "Analytische Geometrie",
     "Abstände",
     "Eine hergeleitete Beziehung zwischen zwei Parametern mit der Gleichung einer im "
     "Parameter-Koordinatensystem abgebildeten Geraden vergleichen.",
     "2026MerhoehtAAGLAA222-b"),
    ("Symmetrieebenen eines Körpers aus den Koordinaten begründen", "Analytische Geometrie",
     "Spiegelung",
     "Für einen Körper mit Parameter die Gleichungen seiner achsenparallelen Symmetrieebenen "
     "angeben und über Vorzeichenwechsel und Mittelwerte von Koordinaten begründen.",
     "2026MerhoehtAAGLAA223"),
    ("Wahrscheinlichkeit eines Sigma-Intervalls aus dem Säulendiagramm ermitteln", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Erwartungswert und Standardabweichung einer Binomialverteilung berechnen, das "
     "Sigma-Intervall auf ganze Zahlen übertragen und die Wahrscheinlichkeit als Summe der "
     "abgelesenen Säulenhöhen ermitteln.",
     "2026MerhoehtAStochastik11-b"),
    ("Term für die Wahrscheinlichkeit eines mehrstufigen Pfads angeben", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Für ein in Worten beschriebenes Ereignis, das genau einem Pfad entspricht, den Term aus "
     "dem Produkt der Astwahrscheinlichkeiten angeben.",
     "2026MerhoehtAStochastik12-a"),
    ("Gewinnwahrscheinlichkeiten in einem Wechselspiel vergleichen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Für ein Spiel, in dem zwei Personen abwechselnd ziehen und der erste Treffer gewinnt, die "
     "Gewinnwahrscheinlichkeiten über die Pfade aufstellen und ihr Verhältnis beurteilen.",
     "2026MerhoehtAStochastik12-b"),
    ("Wahrscheinlichkeit eines Vergleichs zweier Zufallsgeräte über Pfade berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Aus den Verteilungen zweier Zufallsgeräte die Wahrscheinlichkeit, dass das eine einen "
     "größeren Wert liefert als das andere, über die passenden Pfade berechnen und für mehrere "
     "Runden potenzieren.",
     "2026MerhoehtAStochastik21-a"),
    ("Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen", "Stochastik", "Kombinatorik",
     "Einen vorgegebenen Term mit Platzhaltern so ergänzen, dass er die Wahrscheinlichkeit eines "
     "Ereignisses liefert, wobei Anzahl der Anordnungen und Einzelwahrscheinlichkeiten zu "
     "bestimmen sind.",
     "2026MerhoehtAStochastik21-b"),
    ("Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen", "Stochastik",
     "Binomialverteilung",
     "Die Wahrscheinlichkeit für genau einen Treffer in zwei unabhängigen Versuchen als Summe "
     "der beiden Pfade berechnen.",
     "2026MerhoehtAStochastik22-a"),
    ("Term für eine bedingte Wahrscheinlichkeit mit Parameter aufstellen", "Stochastik",
     "Bedingte Wahrscheinlichkeit und Bayes",
     "Eine bedingte Wahrscheinlichkeit als Quotient aus Pfadsummen in Abhängigkeit von einer "
     "Trefferwahrscheinlichkeit p aufstellen, ohne sie auszurechnen.",
     "2026MerhoehtAStochastik22-b"),
    ("Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Zu einem vorgegebenen Rechenterm ein Ereignis im Sachzusammenhang formulieren, dessen "
     "Wahrscheinlichkeit der Term liefert, etwa über Gegenereignis und Pfadprodukt.",
     "2026MerhoehtAStochastik23-a"),
    ("Unbekannte Werte einer Zufallsgröße aus dem Erwartungswert bestimmen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Die Verteilung einer Zufallsgröße mit unbekannten Werten aufstellen und die Unbekannten "
     "aus dem gegebenen Erwartungswert und einer Nebenbedingung berechnen.",
     "2026MerhoehtAStochastik23-b"),
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


def eichung(zeilen):
    """Trefferquote niveau_geschaetzt gegen den höchsten amtlichen Bereich (iqb.md § 4)."""
    treffer, abw = 0, []
    for z in zeilen:
        amt = hoechster_afb(z["afb_amtlich"])
        eig = ORD.get(z["niveau_geschaetzt"], 0)
        if amt == eig:
            treffer += 1
        else:
            abw.append(f"{z['id']} geschätzt {z['niveau_geschaetzt']}, amtlich höchstens "
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
        print(f"Selbstprüfung bestanden: {len(alt)} Katalogzeilen, {len(alt_typ)} Typen, "
              f"alle Typen verwendet, {len(stapel)} Stapel vollständig. ZEILEN ist leer, nichts geschrieben.")
        if alt:
            print(f"Eichung über den Bestand: {treffer} von {len(alt)} Zeilen treffen den höchsten "
                  f"amtlichen Bereich ({100 * treffer // len(alt)} %).")
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
    if len(alt) >= SCHWELLEN["neue_typen_ab_bestand"] and verwendet:
        anteil = len(neu & verwendet) / len(verwendet)
        a(anteil <= SCHWELLEN["neue_typen_anteil"],
          f"Schwelle gerissen: {len(neu & verwendet)} von {len(verwendet)} verwendeten Typen neu "
          f"({100 * anteil:.0f} %), erlaubt {100 * SCHWELLEN['neue_typen_anteil']:.0f} %")

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
    print(f"Schwellen: {len(unsicher)} Zeilen mit „?“ (erlaubt {grenze_frage}), "
          f"{len(ersatz)} ohne passendes Thema (erlaubt {grenze_ersatz})")
    # Kennzahlen je Stapel (iqb.md § 7): gemessene Quoten, aus denen nach drei
    # Stapeln die Schwellenwerte abgeleitet werden. Zeile für iqb-pruefungen.md § 4.
    print(f"Kennzahlen: | {stapel} | {n} | {len(verwendet)} | {len(neu & verwendet)} "
          f"({100 * len(neu & verwendet) / len(verwendet):.0f} %) | {treffer} von {n} "
          f"({100 * treffer / n:.0f} %) | {len(unsicher)} | {len(ersatz)} |")
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
