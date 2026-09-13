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
    "stapel": "2026-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2026MgrundlegendAAnalysis11": 5, "2026MgrundlegendAAnalysis12": 5,
        "2026MgrundlegendAAnalysis13": 5, "2026MgrundlegendAAnalysis14": 5,
        "2026MgrundlegendAAnalysis21": 5, "2026MgrundlegendAAnalysis22": 5,
        "2026MgrundlegendAAGLAA111": 5, "2026MgrundlegendAAGLAA112": 5,
        "2026MgrundlegendAAGLAA12": 5, "2026MgrundlegendAAGLAA211": 5,
        "2026MgrundlegendAAGLAA213": 5, "2026MgrundlegendAAGLAA221": 5,
        "2026MgrundlegendAAGLAA222": 5, "2026MgrundlegendAStochastik11": 5,
        "2026MgrundlegendAStochastik12": 5, "2026MgrundlegendAStochastik13": 5,
        "2026MgrundlegendAStochastik21": 5, "2026MgrundlegendAStochastik22": 5,
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

row("2026MgrundlegendAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen", typ_neben="",
    stichwoerter="ganzrationale Funktion dritten Grades|notwendige Bedingung|hinreichende Bedingung|zweite Ableitung",
    voraussetzungen="Potenzregel anwenden|Vorzeichen der zweiten Ableitung deuten",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x^3 − 3x, definiert in IR; Graph G",
    gesucht="Nachweis, dass G einen Hochpunkt mit der x-Koordinate −1 hat",
    verfahren="erste und zweite Ableitung bilden, f'(−1) = 0 und f''(−1) < 0 zeigen",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 3x^2 − 3, f''(x) = 6x; f'(−1) = 0 und f''(−1) = −6 < 0, also Hochpunkt bei x = −1 (amtlich)",
    zwischenergebnis="f'(x) = 3x^2 − 3|f''(x) = 6x",
    niveau_geschaetzt="I",
    fehlerquelle="nur f'(−1) = 0 zeigen und die hinreichende Bedingung weglassen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MgrundlegendAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Abstand zweier Extrempunkte über die Punktsymmetrie berechnen", typ_neben="",
    stichwoerter="Punktsymmetrie zum Ursprung|Hochpunkt|Tiefpunkt|Abstand zweier Punkte",
    voraussetzungen="Funktionswert berechnen|Abstand zweier Punkte mit dem Satz des Pythagoras|Punktsymmetrie nutzen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x^3 − 3x, definiert in IR; Graph G; G ist symmetrisch zum Koordinatenursprung; G hat einen Hochpunkt mit der x-Koordinate −1",
    gesucht="Abstand zwischen Hoch- und Tiefpunkt von G",
    verfahren="f(−1) = 2 berechnen, Hochpunkt H(−1; 2); wegen der Punktsymmetrie ist der Tiefpunkt T(1; −2); Abstand als Länge der Strecke HT, gleich dem Doppelten des Abstands von H zum Ursprung",
    schritte="3", zahlenraum="ganz|negativ|Wurzel", einheiten="",
    abhaengig_von="2026MgrundlegendAAnalysis11-a",
    ergebnis="2 · √((−1)^2 + 2^2) = 2√5 (amtlich)",
    zwischenergebnis="f(−1) = 2|H(−1; 2)|T(1; −2)",
    niveau_geschaetzt="II",
    fehlerquelle="den Tiefpunkt neu über die Ableitung berechnen statt die Symmetrie zu nutzen, oder nur den Abstand von H zum Ursprung angeben",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt: 2√5 ≈ 4,47.")

# ---- Analysis 1.2: Sinus, Dreieck aus Extrempunkten
SIN_SKIZZE = ("Koordinatensystem mit x-Achse von 0 bis 3π (Marken π/2, π, 3π/2, 2π, 5π/2, 3π) und "
              "y-Achse; gestrichelt der Graph von f(x) = sin x; durchgezogen das Dreieck ABC mit "
              "A(π/2; 1) und C(5π/2; 1) oben und B(3π/2; −1) unten, also drei aufeinanderfolgende "
              "Extrempunkte; die Seiten AB und BC schneiden die x-Achse bei π und 2π")
row("2026MgrundlegendAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Flächeninhalt eines Dreiecks aus Extrempunkten der Sinusfunktion berechnen", typ_neben="",
    stichwoerter="Sinusfunktion|Extrempunkte|Dreieck|Grundseite 2π|Höhe 2",
    voraussetzungen="Extrempunkte von sin x kennen|Dreiecksfläche aus Grundseite und Höhe",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=SIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = sin x, definiert in IR; Dreieck ABC, dessen Eckpunkte drei direkt aufeinanderfolgende Extrempunkte des Graphen sind: A(π/2; 1), B(3π/2; −1), C(5π/2; 1) (aus der Abbildung)",
    gesucht="Flächeninhalt des Dreiecks ABC",
    verfahren="Grundseite AC mit Länge 2π und Höhe 2 (Abstand von B zur Geraden AC) ablesen, Fläche als halbes Produkt",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="A = 1/2 · 2π · (1 − (−1)) = 2π (amtlich)",
    zwischenergebnis="Grundseite 2π|Höhe 2",
    niveau_geschaetzt="I",
    fehlerquelle="die Höhe mit 1 statt 2 ansetzen, weil der Tiefpunkt bei −1 liegt",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MgrundlegendAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Abstand von Extrempunkten einer gestreckten Sinusfunktion vergleichen", typ_neben="",
    stichwoerter="Streckung in x-Richtung|Streckung in y-Richtung|Faktor 3 und 2|Abstand der Extrempunkte",
    voraussetzungen="Wirkung der Parameter a und b in a · sin(b · x) kennen|Streckenlänge aus Koordinatendifferenzen",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SIN_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = sin x mit den Extrempunkten A(π/2; 1) und B(3π/2; −1); g(x) = 2 · sin(1/3 · x), definiert in IR; betrachtet wird die Strecke zwischen zwei direkt aufeinanderfolgenden Extrempunkten des Graphen von g",
    gesucht="Untersuchung, ob diese Strecke kürzer als die Strecke AB ist",
    verfahren="den Graphen von g als Streckung des Graphen von f in x-Richtung mit Faktor 3 und in y-Richtung mit Faktor 2 erkennen; beide Faktoren größer als 1, also wächst die waagerechte und die senkrechte Differenz der Extrempunkte, die Strecke ist länger",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2026MgrundlegendAAnalysis12-a",
    ergebnis="nein, die Strecke ist nicht kürzer als AB, weil der Graph von g durch Streckung in x- und in y-Richtung mit Faktoren größer als 1 aus dem Graphen von f entsteht (amtlich)",
    zwischenergebnis="rechnerisch: |AB| = √(π^2 + 4) ≈ 3,72; bei g Extrempunkte (3π/2; 2) und (9π/2; −2) mit Abstand √(9π^2 + 16) ≈ 10,24",
    niveau_geschaetzt="II",
    fehlerquelle="den Faktor 1/3 als Stauchung in x-Richtung deuten",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. Amtlich; das amtliche Ergebnis argumentiert ohne Rechnung, eigene Rechnung bestätigt.")

# ---- Analysis 1.3: Integral und Flächeninhalt
KUB_SKIZZE = ("Koordinatensystem mit x-Achse von −2 bis 2 und y-Achse von −3 bis 4, Gitter; Graph "
              "von f(x) = x^3 + x^2 − 2x: von links unten steil steigend durch die Nullstelle −2, "
              "Hochpunkt bei etwa (−1,2; 2,1), fallend durch den Ursprung, Tiefpunkt bei etwa "
              "(0,55; −0,6), Nullstelle 1, dann steil steigend")
row("2026MgrundlegendAAnalysis13", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Bestimmtes Integral einer ganzrationalen Funktion berechnen", typ_neben="",
    stichwoerter="Stammfunktion|Hauptsatz|Integral von −1 bis 0|Bruchrechnung",
    voraussetzungen="Potenzregel der Integration|Brüche addieren",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=KUB_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x^3 + x^2 − 2x, definiert in IR; Nullstellen −2, 0 und 1; Graph in der Abbildung",
    gesucht="Wert des Integrals von −1 bis 0 über f(x) dx",
    verfahren="Stammfunktion F(x) = 1/4 x^4 + 1/3 x^3 − x^2 bilden und F(0) − F(−1) berechnen",
    schritte="2", zahlenraum="ganz|negativ|Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="13/12 (amtlich)",
    zwischenergebnis="F(x) = 1/4 x^4 + 1/3 x^3 − x^2|F(−1) = 1/4 − 1/3 − 1 = −13/12",
    niveau_geschaetzt="I",
    fehlerquelle="beim Einsetzen von −1 die Vorzeichen der ungeraden Potenz verfehlen",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MgrundlegendAAnalysis13", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Summe zweier Integrale als Flächeninhalt beurteilen", typ_neben="",
    stichwoerter="Fläche zwischen Graph und x-Achse|zwei Flächenstücke|negatives Integral|Vorzeichen",
    voraussetzungen="Integral unterhalb der x-Achse als negativ erkennen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=KUB_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = x^3 + x^2 − 2x, definiert in IR; Nullstellen −2, 0 und 1; der Graph und die x-Achse schließen eine Fläche aus zwei Flächenstücken ein (über der Achse zwischen −2 und 0, unter der Achse zwischen 0 und 1); Term: Integral von −2 bis 0 über f plus Integral von 0 bis 1 über f",
    gesucht="Beurteilung, ob der Wert des Terms dem Inhalt dieser Fläche entspricht",
    verfahren="das zweite Integral ist negativ, weil der Graph zwischen 0 und 1 unter der x-Achse liegt; die Summe ist deshalb kleiner als der Flächeninhalt",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="nein; das Integral von 0 bis 1 ist negativ und entspricht nicht dem Inhalt des Flächenstücks unter der x-Achse, das Integral von −2 bis 0 entspricht dem Flächenstück über der Achse, die Summe ist also nicht der Flächeninhalt (amtlich)",
    zwischenergebnis="rechnerisch: Integral von −2 bis 0 gleich 8/3, von 0 bis 1 gleich −5/12",
    niveau_geschaetzt="II",
    fehlerquelle="jedes Integral als Flächeninhalt lesen und die Summe für richtig halten",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 1.4: Funktion und Ableitung im Bild
ABL_SKIZZE = ("Koordinatensystem mit x-Achse von −3 bis 3 und y-Achse von −2 bis 2, Gitter; Graph I "
              "durchgezogen: von links unten flach steigend, Hochpunkt (0; 2), fallend zum Tiefpunkt "
              "(2; 0) mit Berührung der x-Achse, dann steil steigend; Graph II gestrichelt: von links "
              "nahe null, kleines Maximum bei etwa (−2; 0,3), Nullstelle 0, Tiefpunkt bei etwa "
              "(1; −1,6), Nullstelle 2, dann steil steigend")
row("2026MgrundlegendAAnalysis14", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Graph der Funktion vom Graphen der Ableitung unterscheiden", typ_neben="",
    stichwoerter="Graph und Ableitungsgraph|negative Steigung|Vorzeichen der Ableitung|Zuordnung begründen",
    voraussetzungen="Steigung des Graphen mit dem Vorzeichen der Ableitung verknüpfen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ABL_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung mit zwei Graphen I und II: der Graph einer in IR definierten Funktion f und der Graph ihrer Ableitungsfunktion f'; Graph I hat einen Hochpunkt bei (0; 2) und berührt die x-Achse bei 2, Graph II hat Nullstellen bei 0 und 2 und einen Tiefpunkt bei etwa (1; −1,6)",
    gesucht="Begründung, dass Graph I der Graph von f ist",
    verfahren="einen Bereich nennen, in dem Graph I fällt und Graph II negativ ist (0 bis 2), oder umgekehrt in dem Graph II fällt, Graph I aber nicht negativ ist; die Zuordnung Graph II = f' passt zu Graph I",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="es gibt einen Bereich, in dem Graph II negative Steigung hat, Graph I dort aber keine Punkte unterhalb der x-Achse besitzt, also kann Graph I nicht die Ableitung von Graph II sein (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur behaupten, dass Graph II die Ableitung ist, ohne einen Bereich mit passendem Vorzeichen zu nennen",
    bemerkung="Standardbezug: K1 I, K4 I. Amtlich. Die amtliche Begründung geht vom Widerspruch aus: Graph I kann nicht Ableitung von Graph II sein.")

row("2026MgrundlegendAAnalysis14", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integral einer Differenzfunktion grafisch abschätzen", typ_neben="",
    stichwoerter="Integral der Differenz|Fläche zwischen zwei Graphen|Vergleichsrechteck 4 mal 3|Eintragen in die Abbildung",
    voraussetzungen="Integral einer Differenz als Fläche zwischen den Graphen deuten|Rechteckfläche berechnen",
    format="Zeichnen", operator="Veranschaulichen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=ABL_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung mit dem Graphen von f (Graph I, Hochpunkt (0; 2), Tiefpunkt (2; 0)) und dem Graphen von f' (Graph II, Nullstellen 0 und 2, Tiefpunkt bei etwa (1; −1,6)); Aussage: das Integral von −2 bis 2 über f(x) − f'(x) dx ist kleiner als 12",
    gesucht="grafische Veranschaulichung der Aussage durch Eintragungen in der Abbildung",
    verfahren="die Fläche zwischen Graph I und Graph II von x = −2 bis x = 2 schraffieren und ein Rechteck von x = −2 bis 2 und y = −2 bis 1 (Fläche 4 · 3 = 12) eintragen, das die schraffierte Fläche ganz enthält",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MgrundlegendAAnalysis14-a",
    ergebnis="schraffierte Fläche zwischen den beiden Graphen über dem Intervall von −2 bis 2, umschlossen von einem Rechteck der Breite 4 und Höhe 3 mit Flächeninhalt 12 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Fläche unter Graph I schraffieren und Graph II nicht berücksichtigen",
    bemerkung="Standardbezug: K1 II, K2 I, K4 II. Amtlich; der Erwartungshorizont zeigt die Abbildung mit Schraffur und grau hinterlegtem Rechteck von y = −2 bis 1. Das Feld skizze beschreibt das vorgegebene Material, die Lösung ist eine Zeichnung.")

# ---- Analysis 2.1: Produktregel mit Werten aus dem Graphen
PROD_SKIZZE = ("Koordinatensystem mit x-Achse von −6 bis 10 und y-Achse von −10 bis 10, Gitter; die "
               "Gerade g steigend durch (1; 0) und (3; 4) mit Steigung 2; der Graph von f "
               "parabelförmig: von links oben fallend durch (0; 0), Tiefpunkt (3; −6), steigend durch "
               "(6; 0) nach rechts oben")
row("2026MgrundlegendAAnalysis21", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Steigung einer Geraden am Graphen begründen", typ_neben="",
    stichwoerter="lineare Funktion|Steigungsdreieck|Ableitung konstant|g'(3) = 2",
    voraussetzungen="Ableitung einer linearen Funktion als Steigung kennen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=PROD_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung mit dem Graphen der in IR definierten linearen Funktion g (durch (1; 0) und (3; 4)) und dem Graphen der differenzierbaren Funktion f",
    gesucht="Begründung, dass g'(3) = 2 gilt",
    verfahren="am Graphen von g ein Steigungsdreieck ablesen (2 nach rechts, 4 nach oben); die Ableitung einer linearen Funktion ist überall ihre Steigung",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="anhand eines Steigungsdreiecks hat die Gerade die Steigung 2, also ist g'(3) = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="g(3) = 4 als Ableitungswert nehmen",
    bemerkung="Standardbezug: K1 I, K4 I. Amtlich. Werte nur aus der Abbildung; eine Funktionsgleichung ist nicht gegeben.")

row("2026MgrundlegendAAnalysis21", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung eines Produkts aus Graphenwerten mit der Produktregel bestimmen", typ_neben="",
    stichwoerter="Produktregel|Tangentensteigung|Werte aus dem Graphen|Tiefpunkt hat Ableitung null",
    voraussetzungen="Produktregel anwenden|Funktionswerte und Steigungen aus Graphen ablesen|Tiefpunkt als Stelle mit f' = 0 erkennen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=PROD_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung mit dem Graphen der linearen Funktion g (Steigung 2, g(3) = 4) und dem Graphen der differenzierbaren Funktion f (Tiefpunkt (3; −6)); h(x) = f(x) · g(x), definiert in IR",
    gesucht="Steigung der Tangente an den Graphen von h im Punkt (3; h(3))",
    verfahren="h'(3) = f'(3) · g(3) + f(3) · g'(3) mit der Produktregel; f'(3) = 0 (Tiefpunkt), g(3) = 4, f(3) = −6 und g'(3) = 2 aus der Abbildung einsetzen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MgrundlegendAAnalysis21-a",
    ergebnis="h'(3) = f'(3) · g(3) + f(3) · g'(3) = 0 · 4 + (−6) · 2 = −12 (amtlich)",
    zwischenergebnis="f'(3) = 0|f(3) = −6|g(3) = 4|g'(3) = 2",
    niveau_geschaetzt="II",
    fehlerquelle="h'(3) als f'(3) · g'(3) bilden oder f'(3) nicht als null erkennen",
    bemerkung="Standardbezug: K2 III, K4 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eigene Schätzung II, amtlich bis III.")

# ---- Analysis 2.2: Graph der Ableitung, Monotonie und Stammfunktion
ABL2_SKIZZE = ("Koordinatensystem mit x-Achse von −4 bis 4 und y-Achse von −3 bis 4, Gitter; Graph "
               "von f' beschriftet: von links unten steil steigend durch die einzige Nullstelle −3, "
               "Hochpunkt (−2; 4), dann fallend und sich für große x von oben der x-Achse nähernd "
               "(bei x = 4 etwa 0,2)")
row("2026MgrundlegendAAnalysis22", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Monotonie aus dem Vorzeichen der Ableitung am Graphen begründen", typ_neben="",
    stichwoerter="Graph der Ableitung|Vorzeichenwechsel|monoton fallend|monoton steigend",
    voraussetzungen="Monotoniekriterium mit dem Vorzeichen von f' kennen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ABL2_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung mit dem Graphen der Ableitungsfunktion f' einer in IR definierten Funktion f; die einzige Nullstelle von f' ist −3; f' ist links von −3 negativ, rechts davon positiv",
    gesucht="Begründung, dass f für x <= −3 monoton fallend und für x >= −3 monoton steigend ist",
    verfahren="am Graphen von f' das Vorzeichen links und rechts von −3 ablesen; f' wechselt an seiner einzigen Nullstelle von minus nach plus",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f' wechselt an seiner einzigen Nullstelle −3 das Vorzeichen von minus nach plus, also fällt f links davon und steigt rechts davon (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den abgebildeten Graphen für den Graphen von f halten und mit dessen Steigung argumentieren",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. Amtlich.")

row("2026MgrundlegendAAnalysis22", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Aussage über Extrempunkte einer Stammfunktion beurteilen", typ_neben="",
    stichwoerter="Stammfunktion F|F' = f|Tiefpunkt (−3; 2)|f überall positiv|kein Extrempunkt",
    voraussetzungen="F' = f verwenden|Tiefpunkt von f aus der Monotonie folgern|notwendige Bedingung für Extrempunkte",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ABL2_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Abbildung mit dem Graphen von f' (einzige Nullstelle −3, Vorzeichenwechsel von minus nach plus); f(−3) = 2; Aussage: ist F eine Stammfunktion von f, dann besitzt der Graph von F keinen Extrempunkt",
    gesucht="Beurteilung der Aussage",
    verfahren="aus der Monotonie folgt, dass f bei (−3; 2) seinen einzigen Extrempunkt, einen Tiefpunkt, hat; f ist damit überall positiv, also hat F' = f keine Nullstelle und F keinen Extrempunkt",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MgrundlegendAAnalysis22-a",
    ergebnis="die Aussage ist wahr: der Graph von f hat mit dem Tiefpunkt (−3; 2) seinen einzigen Extrempunkt, f nimmt nur positive Werte an, F' = f hat also keine Nullstelle (amtlich)",
    zwischenergebnis="Tiefpunkt von f bei (−3; 2)|f(x) > 0 für alle x",
    niveau_geschaetzt="III",
    fehlerquelle="die Nullstelle von f' bei −3 als Extremstelle von F deuten",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 III. Amtlich.")

# ---- AG/LA (A1) 1.1: rechtwinkliges Dreieck und Pyramide
row("2026MgrundlegendAAGLAA111", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen", typ_neben="",
    stichwoerter="Skalarprodukt null|Betrag eines Vektors|gleichschenklig|Katheten 10",
    voraussetzungen="Skalarprodukt bilden|Vektorlänge berechnen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="gleichschenkliges Dreieck OAB mit O(0; 0; 0), A(8; 6; 0) und B(0; 0; 10)",
    gesucht="Nachweis, dass OAB in O rechtwinklig ist und die Katheten die Länge 10 haben",
    verfahren="Skalarprodukt OA · OB = 0 zeigen; |OB| = 10 berechnen und aus der Gleichschenkligkeit im rechten Winkel |OA| = |OB| folgern oder |OA| = √(64 + 36) = 10 direkt rechnen",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="OA · OB = 8 · 0 + 6 · 0 + 0 · 10 = 0, also rechter Winkel in O; |OB| = 10 und wegen der Gleichschenkligkeit |OA| = |OB| = 10 (amtlich)",
    zwischenergebnis="|OA| = √(8^2 + 6^2) = 10",
    niveau_geschaetzt="I",
    fehlerquelle="den rechten Winkel bei A oder B prüfen statt bei O",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MgrundlegendAAGLAA111", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Höhe einer Pyramide aus dem Volumen bestimmen", typ_neben="",
    stichwoerter="Pyramide|Volumen 100|Spitze senkrecht über dem rechten Winkel|Höhe 6",
    voraussetzungen="Volumenformel der Pyramide|Skalarprodukt null als Orthogonalität deuten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Dreieck OAB mit O(0; 0; 0), A(8; 6; 0), B(0; 0; 10), rechtwinklig in O mit Kathetenlänge 10; Pyramide OABS mit Spitze S und Volumen 100; OS · OA = 0 und OS · OB = 0",
    gesucht="Länge |OS|",
    verfahren="OS steht senkrecht auf der Grundfläche OAB, ist also die Höhe; Grundfläche 1/2 · 10 · 10 = 50; aus V = 1/3 · 50 · |OS| = 100 folgt |OS| = 6",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2026MgrundlegendAAGLAA111-a",
    ergebnis="1/3 · 1/2 · 10 · 10 · |OS| = 100, also |OS| = 6 (amtlich)",
    zwischenergebnis="Grundfläche 50",
    niveau_geschaetzt="II",
    fehlerquelle="den Faktor 1/3 der Pyramidenformel vergessen",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A1) 1.2: Dreieck mit Parameter (Dublette 2026MgrundlegendAAGLAA212)
row("2026MgrundlegendAAGLAA112", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Rechten Winkel eines Dreiecks mit Parameter nachweisen", typ_neben="",
    stichwoerter="Skalarprodukt mit Parameter|6t − 6t = 0|rechter Winkel in A",
    voraussetzungen="Skalarprodukt mit Variablen ausrechnen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Dreieck ABC mit A(0; 0; 0), B(6; 2; 3) und C(t; −3t; 0), t positiv reell",
    gesucht="Nachweis, dass das Dreieck in A einen rechten Winkel hat",
    verfahren="Skalarprodukt AB · AC = 6t − 6t + 0 = 0 für jedes t",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="AB · AC = 6 · t + 2 · (−3t) + 3 · 0 = 6t − 6t = 0, also rechter Winkel in A (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="das Skalarprodukt nur für einen Zahlenwert von t prüfen",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt. Die Kurzbeschreibung nennt das Sachgebiet nur als AG/LA ohne Alternative; die Datei ist wortgleich als 2026MgrundlegendAAGLAA212 ein zweites Mal abgelegt (Dublette ohne Zeile).")

row("2026MgrundlegendAAGLAA112", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen", typ_neben="",
    stichwoerter="gleichschenklig|Kathetenlängen gleich|Betrag mit Parameter|√10 · t = 7",
    voraussetzungen="Vektorlänge mit Parameter berechnen|Wurzelgleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Dreieck ABC mit A(0; 0; 0), B(6; 2; 3) und C(t; −3t; 0), t positiv, rechtwinklig in A; das Dreieck ist gleichschenklig",
    gesucht="Wert von t",
    verfahren="im rechtwinkligen gleichschenkligen Dreieck sind die Katheten AB und AC gleich lang: |AB| = 7 und |AC| = √(t^2 + 9t^2) = √10 · t gleichsetzen",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="2026MgrundlegendAAGLAA112-a",
    ergebnis="t = 7/√10 (amtlich)",
    zwischenergebnis="|AB| = √(36 + 4 + 9) = 7|AC| = √10 · t|t ≈ 2,21",
    niveau_geschaetzt="II",
    fehlerquelle="die Hypotenuse BC mit einer Kathete gleichsetzen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A1) 2: lineares Gleichungssystem mit Bedingungen (ungegliedert)
row("2026MgrundlegendAAGLAA12", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lösung eines unterbestimmten Gleichungssystems unter Zusatzbedingungen auswählen", typ_neben="",
    stichwoerter="LGS mit drei Unbekannten|Gleichungen II und III Vielfache|Lösungsschar mit Parameter|negativ und ganzzahlig|größtes y",
    voraussetzungen="abhängige Gleichungen erkennen|Lösungsmenge mit Parameter angeben|Bedingungen an den Parameter übersetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="lineares Gleichungssystem I: −4x + z = 4, II: 2y − z = 4, III: 4y − 2z = 8; betrachtet werden nur Lösungen (x; y; z), bei denen x, y und z negativ und ganzzahlig sind",
    gesucht="die Lösung mit dem größten Wert für y",
    verfahren="II und III sind Vielfache, das System hat unendlich viele Lösungen; mit z = t folgt x = t/4 − 1 und y = t/2 + 2; alle drei negativ heißt t < −4, ganzzahlig heißt t Vielfaches von 4; größtes y bei t = −8",
    schritte="4", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="(−3; −2; −8) (amtlich)",
    zwischenergebnis="allgemeine Lösung (t/4 − 1; t/2 + 2; t) mit t aus IR|Bedingung t < −4 und t Vielfaches von 4",
    niveau_geschaetzt="III",
    fehlerquelle="das System für eindeutig lösbar halten oder die Ganzzahligkeit von x übersehen und t = −6 nehmen",
    bemerkung="Standardbezug: K1 III, K2 II, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE. Lineare Gleichungssysteme stehen im Pool unter AG/LA, in der Themenliste deshalb auch unter Analytische Geometrie (iqb.md § 6).")

# ---- AG/LA (A2) 1.1: Ebene, Lotgerade, Spiegelpunkt
row("2026MgrundlegendAAGLAA211", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punktprobe an einer Ebenengleichung durchführen",
    typ_neben="Orthogonalität von Gerade und Ebene über Normalen- und Richtungsvektor begründen",
    stichwoerter="Koordinatengleichung|Punktprobe|Normalenvektor|Richtungsvektor kollinear|Lotgerade",
    voraussetzungen="Normalenvektor aus der Koordinatengleichung ablesen|Richtungsvektor aus zwei Punkten bilden|Kollinearität erkennen",
    format="Begründung", operator="Zeigen Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Ebene E: x1 − 3x2 + 2x3 = 11; Gerade g durch P(5; 0; 3) und Q(9; −12; 11)",
    gesucht="Nachweis, dass P in E liegt|Begründung, dass g senkrecht zu E steht",
    verfahren="P in die Koordinatengleichung einsetzen; Richtungsvektor PQ = (4; −12; 8) mit dem Normalenvektor (1; −3; 2) vergleichen: PQ = 4 · n, also kollinear",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="5 − 3 · 0 + 2 · 3 = 11, also liegt P in E|der Richtungsvektor (4; −12; 8) von g und der Normalenvektor (1; −3; 2) von E sind kollinear, also steht g senkrecht auf E (amtlich)",
    zwischenergebnis="PQ = (4; −12; 8) = 4 · (1; −3; 2)",
    niveau_geschaetzt="II",
    fehlerquelle="für die Orthogonalität das Skalarprodukt von Richtungs- und Normalenvektor gleich null erwarten",
    bemerkung="Standardbezug: K1 I, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ Punktprobe an einer Ebenengleichung durchführen aus abi-typen.csv übernommen.")

row("2026MgrundlegendAAGLAA211", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen", typ_neben="",
    stichwoerter="Spiegelung an einer Ebene|Lotfußpunkt P|symmetrisch bezüglich E|Vektor PQ rückwärts abtragen",
    voraussetzungen="P als Lotfußpunkt von Q erkennen|Ortsvektor über Vektoraddition bestimmen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Ebene E: x1 − 3x2 + 2x3 = 11; P(5; 0; 3) liegt in E; die Gerade g durch P und Q(9; −12; 11) steht senkrecht auf E; Q und R liegen symmetrisch bezüglich E",
    gesucht="Koordinaten von R",
    verfahren="P ist der Lotfußpunkt von Q auf E, also ist R = P − PQ (den Vektor PQ von P aus in Gegenrichtung abtragen)",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MgrundlegendAAGLAA211-a",
    ergebnis="OR = OP − PQ = (1; 12; −5), also R(1; 12; −5) (amtlich)",
    zwischenergebnis="PQ = (4; −12; 8)",
    niveau_geschaetzt="II",
    fehlerquelle="den Lotfußpunkt neu berechnen, obwohl er mit P gegeben ist, oder R = Q − PQ = P erhalten",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 1.3: gerades Prisma
PRISMA_SKIZZE = ("Schrägbild eines dreiseitigen geraden Prismas ABCDEF in einem räumlichen "
                 "Koordinatensystem mit x-Achse nach vorn links, y-Achse nach rechts, z-Achse nach "
                 "oben; Grundfläche das Dreieck A(0; 0; 0), B(6; 0; 0), C(0; 4; 0) mit gepunktetem "
                 "Gitter in der xy-Ebene, Deckfläche D(0; 0; 3), E(6; 0; 3), F(0; 4; 3); die Kanten "
                 "AD und AC verdeckt gestrichelt; Buchstaben an allen Ecken")
row("2026MgrundlegendAAGLAA213", "a", seite="1", punkte="1", afb_amtlich="I",
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
    bemerkung="Standardbezug: K4 I. Amtlich. Datei mit drei Seiten (Bewertungshinweise auf Seite 3).")

row("2026MgrundlegendAAGLAA213", "b", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Dreieck in ein Schrägbild einzeichnen", typ_neben="",
    stichwoerter="Punkt auf einer Kante|P(2; 0; 3) auf DE|Dreieck APC|Schrägbild",
    voraussetzungen="Punkt auf einer Kante im Schrägbild verorten",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Körper", skizze=PRISMA_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Prisma ABCDEF mit A(0; 0; 0), B(6; 0; 0), C(0; 4; 0), D(0; 0; 3), E(6; 0; 3), F(0; 4; 3); P(2; 0; 3) liegt auf der Kante DE",
    gesucht="Dreieck APC in der Abbildung",
    verfahren="P auf DE ein Drittel von D aus markieren und mit A und C verbinden; die Kante AP läuft im Innern des Prismas",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Dreieck mit den Ecken A, P (auf DE, zwei Einheiten von D entfernt) und C, Seiten AP und PC eingezeichnet (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="P bei zwei Dritteln der Kante DE eintragen",
    bemerkung="Standardbezug: K4 I. Amtlich; der Erwartungshorizont zeigt die Abbildung mit dem eingezeichneten Dreieck. Das Feld skizze beschreibt das Material, die Lösung ist eine Zeichnung.")

row("2026MgrundlegendAAGLAA213", "c", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Parameter eines Punktes aus einer Flächengleichheit bestimmen", typ_neben="",
    stichwoerter="Dreiecksfläche|rechter Winkel bei A|gleiche Flächeninhalte|Wurzelgleichung|k = √27",
    voraussetzungen="Orthogonalität von AC und AQ erkennen|Dreiecksfläche als halbes Kathetenprodukt|Wurzelgleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=PRISMA_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Prisma mit A(0; 0; 0), B(6; 0; 0), C(0; 4; 0), D(0; 0; 3); Q(k; 0; 3) mit 0 <= k <= 6; das Dreieck AQC hat den gleichen Flächeninhalt wie das Dreieck ABC",
    gesucht="Wert von k",
    verfahren="AC steht senkrecht auf AB und auf AQ, beide Dreiecke sind rechtwinklig in A mit gemeinsamer Kathete AC; Flächengleichheit heißt |AQ| = |AB|, also √(k^2 + 9) = 6",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="1/2 · |AC| · |AQ| = 1/2 · |AC| · |AB| führt auf √(k^2 + 3^2) = 6, also k = √27 (amtlich)",
    zwischenergebnis="|AB| = 6|k^2 = 27|k ≈ 5,20",
    niveau_geschaetzt="II",
    fehlerquelle="die Fläche mit einer Höhe berechnen, die nicht auf AC senkrecht steht, oder k^2 = 36 setzen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 2.1: Punkt aus drei Bedingungen (ungegliedert)
row("2026MgrundlegendAAGLAA221", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen", typ_neben="",
    stichwoerter="Ansatz C(x; y; 6)|Skalarprodukt null|Punkt in Ebene|lineares Gleichungssystem zwei Unbekannte|Bruchlösung",
    voraussetzungen="Bedingungen in Gleichungen übersetzen|Skalarprodukt mit Unbekannten ausrechnen|LGS mit zwei Unbekannten lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="A(2; −3; −1) und B(10; −5; 3); für C gilt: die z-Koordinate von C ist 6; die Geraden AB und AC verlaufen senkrecht zueinander; C liegt in der Ebene x + 2y = 0",
    gesucht="Koordinaten von C",
    verfahren="C(x; y; 6) ansetzen; AB · AC = 8(x − 2) − 2(y + 3) + 4 · 7 = 8x − 2y + 6 = 0 und x + 2y = 0 als Gleichungssystem lösen",
    schritte="4", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="C(−2/3; 1/3; 6) (amtlich)",
    zwischenergebnis="AB = (8; −2; 4)|AC = (x − 2; y + 3; 7)|I: 8x − 2y + 6 = 0, II: x + 2y = 0",
    niveau_geschaetzt="III",
    fehlerquelle="die Ebenengleichung x + 2y = 0 als Gerade in der Ebene missdeuten oder beim Skalarprodukt die Konstante 28 vergessen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE.")

# ---- AG/LA (A2) 2.2: Prisma mit Rautengrundfläche, Drehung
RAUTE_SKIZZE = ("Schrägbild eines Prismas ABCDEFGH über einer Raute in einem räumlichen "
                "Koordinatensystem (x nach vorn links, y nach rechts, z nach oben) mit gepunktetem "
                "Gitter in der xy-Ebene; Grundfläche A(2; 0; 0) vorn, B(0; 5; 0) rechts, C(−2; 0; 0) "
                "hinten, D(0; −5; 0) links, Ursprung O in der Mitte; Deckfläche E über A, F(0; 5; 6) "
                "über B, G über C, H über D; verdeckte Kanten gestrichelt")
row("2026MgrundlegendAAGLAA222", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Volumen eines Prismas über einer Raute berechnen", typ_neben="",
    stichwoerter="Raute aus vier rechtwinkligen Dreiecken|Diagonalen 4 und 10|Höhe 6|Volumen 120",
    voraussetzungen="Rautenfläche aus den Diagonalen oder aus vier Dreiecken|Prismenvolumen Grundfläche mal Höhe",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=RAUTE_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Prisma ABCDEFGH mit A(2; 0; 0), B(0; 5; 0), C(−2; 0; 0), D(0; −5; 0) und F(0; 5; 6); die Grundfläche ABCD ist eine Raute",
    gesucht="Volumen des Prismas",
    verfahren="Raute als vier rechtwinklige Dreiecke mit Katheten 2 und 5 (oder halbes Diagonalenprodukt 1/2 · 4 · 10 = 20); Höhe 6 aus F; Volumen 20 · 6",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="V = 4 · 1/2 · 2 · 5 · 6 = 120 (amtlich)",
    zwischenergebnis="Grundfläche 20|Höhe 6",
    niveau_geschaetzt="II",
    fehlerquelle="die Raute als Rechteck 4 mal 10 nehmen und 240 erhalten",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MgrundlegendAAGLAA222", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Ortsvektor eines gedrehten Punktes als Term aufstellen", typ_neben="",
    stichwoerter="Drehung um eine Kante|Punkt in der xy-Ebene|Richtung senkrecht zu AB|Einheitsvektor mal Länge|Term statt Zahl",
    voraussetzungen="zu AB senkrechten Vektor in der xy-Ebene finden|Vektor auf eine Länge normieren|Ortsvektor als Summe aufstellen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Körper", skizze=RAUTE_SKIZZE, kontext="ohne", textumfang="lang",
    gegeben="Prisma ABCDEFGH mit A(2; 0; 0), B(0; 5; 0), C(−2; 0; 0), D(0; −5; 0), F(0; 5; 6); das Prisma wird so um die Kante AB gedreht, dass F nach der Drehung in der xy-Ebene liegt und eine positive x-Koordinate hat; dieser Punkt heißt F'",
    gesucht="Term für den Ortsvektor von F', mit dem die Koordinaten von F' berechnet werden können",
    verfahren="F' liegt in der xy-Ebene senkrecht zu AB im Abstand |BF| = 6 von B: (5; 2; 0) steht senkrecht auf AB = (−2; 5; 0) und zeigt in positive x-Richtung; OF' = OB + |BF|/|AB| · (5; 2; 0), weil (5; 2; 0) die Länge |AB| = √29 hat",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="OF' = OB + |BF|/|AB| · (5; 2; 0) (amtlich)",
    zwischenergebnis="|BF| = 6|AB = (−2; 5; 0), |AB| = √29|F' ≈ (5,57; 7,23; 0)",
    niveau_geschaetzt="III",
    fehlerquelle="F einfach auf die xy-Ebene projizieren und F' = B setzen, oder die Richtung (5; 2; 0) nicht auf die Länge 6 bringen",
    bemerkung="Standardbezug: K2 III, K4 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt: |BF'| = 6.")

# ---- Stochastik 1.1: Binomialverteilung aus dem Säulendiagramm
BIN_SKIZZE = ("Säulendiagramm der Wahrscheinlichkeitsverteilung P(X = k) für k = 0 bis 12 mit "
              "y-Achse von 0 bis 0,25 (Marken 0,05, 0,1, 0,15, 0,2) und feinem Gitter; Säulenhöhen "
              "etwa 0,01 (k = 0), 0,06 (1), 0,14 (2), 0,205 (3), 0,22 (4, höchste), 0,175 (5), "
              "0,11 (6), 0,055 (7), 0,02 (8), 0,007 (9), danach nahe null")
row("2026MgrundlegendAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln", typ_neben="",
    stichwoerter="Binomialverteilung n = 20|Säulendiagramm|Erwartungswert ganzzahlig|höchste Säule bei 4|p = 0,2",
    voraussetzungen="Erwartungswert n · p kennen|Erwartungswert als Lage der höchsten Säule deuten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=BIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Säulendiagramm der Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße X mit n = 20 und unbekanntem p; höchste Säule bei k = 4; der Erwartungswert von X ist ganzzahlig",
    gesucht="Wert von p",
    verfahren="der ganzzahlige Erwartungswert liegt an der höchsten Säule, also 20 · p = 4",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="20 · p = 4 liefert p = 0,2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="p aus der Höhe der höchsten Säule (0,22) ablesen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MgrundlegendAStochastik11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen", typ_neben="",
    stichwoerter="P(X = v) ≈ 0,175|kumulierte Wahrscheinlichkeit|0,15 < P(X <= w) < 0,25|Säulen addieren",
    voraussetzungen="Einzelwahrscheinlichkeit als Säulenhöhe lesen|kumulierte Wahrscheinlichkeit als Summe von Säulen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Diagramm", skizze=BIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Säulendiagramm von P(X = k) für X binomialverteilt mit n = 20 und p = 0,2: Säulenhöhen etwa 0,01, 0,06, 0,14, 0,205, 0,22, 0,175 für k = 0 bis 5; Bedingungen P(X = v) ≈ 0,175 und 0,15 < P(X <= w) < 0,25",
    gesucht="natürliche Zahlen v und w",
    verfahren="v an der Säule mit Höhe 0,175 ablesen; für w die Säulen von k = 0 an addieren, bis die Summe zwischen 0,15 und 0,25 liegt",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2026MgrundlegendAStochastik11-a",
    ergebnis="v = 5; w = 2 (amtlich)",
    zwischenergebnis="P(X <= 1) ≈ 0,07|P(X <= 2) ≈ 0,21|P(X <= 3) ≈ 0,41",
    niveau_geschaetzt="II",
    fehlerquelle="für w die Säule mit Höhe zwischen 0,15 und 0,25 nehmen statt die Summe zu bilden",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt (P(X = 5) = 0,175, P(X <= 2) = 0,206).")

# ---- Stochastik 1.2: fünf Münzwürfe
row("2026MgrundlegendAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben", typ_neben="",
    stichwoerter="fünf Münzwürfe|höchstens einmal Wappen|Term angeben|Binomialkoeffizient 5",
    voraussetzungen="höchstens einmal als kein Mal oder genau einmal zerlegen|Anzahl der Anordnungen zählen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Münzwurf", textumfang="mittel",
    gegeben="eine Münze mit Zahl und Wappen wird fünfmal geworfen; Ergebnisse sind Abfolgen wie ZWZZW; Ereignis A: es wird höchstens einmal Wappen erzielt",
    gesucht="Term, mit dem P(A) berechnet werden kann",
    verfahren="P(kein Wappen) + P(genau einmal Wappen) mit (1/2)^5 und 5 · 1/2 · (1/2)^4",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(1/2)^5 + 5 · 1/2 · (1/2)^4 (amtlich)",
    zwischenergebnis="Wert 6/32 = 3/16",
    niveau_geschaetzt="I",
    fehlerquelle="den Faktor 5 für die Position des Wappens vergessen",
    bemerkung="Standardbezug: K2 I, K3 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MgrundlegendAStochastik12", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Ergebnisse zum Gegenereignis zweier Ereignisse aufzählen", typ_neben="",
    stichwoerter="weder A noch B|Gegenereignis|erste zwei Würfe Zahl|mindestens zweimal Wappen|vier Ergebnisse",
    voraussetzungen="weder-noch als Schnitt der Gegenereignisse deuten|Ergebnisse systematisch aufzählen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Münzwurf", textumfang="mittel",
    gegeben="fünf Münzwürfe mit Ergebnissen als Abfolgen von Z und W; A: höchstens einmal Wappen; B: bei den ersten beiden Würfen mindestens einmal Wappen; es tritt weder A noch B ein",
    gesucht="alle Ergebnisse, bei denen weder A noch B eintritt",
    verfahren="nicht B heißt die ersten beiden Würfe sind ZZ; nicht A heißt mindestens zweimal Wappen, also in den letzten drei Würfen zwei oder drei W; alle Abfolgen aufzählen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="ZZWWW, ZZZWW, ZZWZW, ZZWWZ (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nicht A als genau zweimal Wappen lesen und ZZWWW vergessen",
    bemerkung="Standardbezug: K2 II, K3 II, K6 II. Amtlich, eigene Aufzählung bestätigt.")

# ---- Stochastik 1.3: Baumdiagramm Versand
BAUM_SKIZZE = ("zweistufiges Baumdiagramm: erste Stufe A (40 %) und A quer, zweite Stufe je V und "
               "V quer; am Ast A–V steht x, am Ende 8 %; am Ast A quer–V steht 30 %, am Ende y; die "
               "übrigen Äste ohne Angabe")
row("2026MgrundlegendAStochastik13", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Fehlende Wahrscheinlichkeiten im Baumdiagramm über die Pfadregel ermitteln", typ_neben="",
    stichwoerter="Baumdiagramm|Pfadmultiplikation rückwärts|x = 0,08/0,4|y = 0,6 · 0,3|Prozentangaben",
    voraussetzungen="Pfadregel|Gegenwahrscheinlichkeit 1 − 0,4",
    format="Rechnung|Begründung", operator="Ermitteln Sie|Weisen Sie nach", antwort="Zahl|Text",
    material="Diagramm", skizze=BAUM_SKIZZE, kontext="Onlinehandel/Versand", textumfang="mittel",
    gegeben="Sendungen werden zu 40 % mit Versandunternehmen A verschickt; 8 % aller Sendungen werden mit A verschickt und verspätet zugestellt; 30 % der nicht mit A verschickten Sendungen werden verspätet zugestellt; Baumdiagramm mit den Anteilen x (Ast A nach V) und y (Ende des Pfads A quer, V)",
    gesucht="Anteil x|Nachweis, dass y = 18 % gilt",
    verfahren="x als bedingter Anteil 0,08/0,4; y als Pfadprodukt (1 − 0,4) · 0,3",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="x = 0,08/0,4 = 0,2, also 20 %|y = (1 − 0,4) · 0,3 = 0,18, also 18 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="x = 0,08 direkt an den Ast schreiben, ohne durch 0,4 zu teilen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2026MgrundlegendAStochastik13", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus dem Baumdiagramm mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="bedingte Wahrscheinlichkeit|Bedingung verspätet|0,18/(0,08 + 0,18)|größer als 50 %",
    voraussetzungen="Bedingung als Nenner aus zwei Pfaden zusammensetzen",
    format="Rechnung", operator="Untersuchen Sie", antwort="Zahl|Text",
    material="Diagramm", skizze=BAUM_SKIZZE, kontext="Onlinehandel/Versand", textumfang="mittel",
    gegeben="Baumdiagramm: P(A) = 0,4, P(A und verspätet) = 0,08, P(nicht A und verspätet) = 0,18; eine zufällig ausgewählte Sendung wird verspätet zugestellt",
    gesucht="Untersuchung, ob die Wahrscheinlichkeit, dass diese Sendung nicht mit A verschickt wurde, größer als 50 % ist",
    verfahren="P(nicht A | verspätet) = 0,18/(0,08 + 0,18) berechnen und mit 0,5 vergleichen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2026MgrundlegendAStochastik13-a",
    ergebnis="0,18/(0,08 + 0,18) = 0,18/0,26 > 0,5, also ja (amtlich)",
    zwischenergebnis="0,18/0,26 ≈ 0,69",
    niveau_geschaetzt="II",
    fehlerquelle="mit 0,3 (Anteil unter den nicht mit A verschickten) statt mit der bedingten Wahrscheinlichkeit unter der Bedingung verspätet antworten",
    bemerkung="Standardbezug: K1 I, K3 II, K4 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 2.1: Glücksrad (ungegliedert)
row("2026MgrundlegendAStochastik21", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Sektorwinkel eines Glücksrads aus einer Wahrscheinlichkeitsbedingung berechnen", typ_neben="",
    stichwoerter="Glücksrad zwei Sektoren|zweimal gleiche Farbe|p^2 + (1 − p)^2 = 5/9|quadratische Gleichung|Mittelpunktswinkel 120°",
    voraussetzungen="Pfadregel für zwei Drehungen|quadratische Gleichung lösen|Anteil in Winkel umrechnen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="kurz",
    gegeben="Glücksrad mit einem roten und einem weißen Sektor; die Wahrscheinlichkeit, beim zweimaligen Drehen zweimal die gleiche Farbe zu erzielen, beträgt 5/9",
    gesucht="Größe des Mittelpunktswinkels des kleineren Sektors",
    verfahren="p für den kleineren Sektor ansetzen, p^2 + (1 − p)^2 = 5/9 aufstellen, die quadratische Gleichung 2p^2 − 2p + 4/9 = 0 lösen und die kleinere Lösung 1/3 mit 360° multiplizieren",
    schritte="4", zahlenraum="Bruch", einheiten="°", abhaengig_von="",
    ergebnis="p = 1/3, Mittelpunktswinkel 1/3 · 360° = 120° (amtlich)",
    zwischenergebnis="2p^2 − 2p + 4/9 = 0|p = 1/2 − √(1/4 − 2/9) = 1/3 (andere Lösung 2/3)",
    niveau_geschaetzt="III",
    fehlerquelle="nur einen Pfad (zweimal rot) ansetzen oder die Lösung 2/3 als kleineren Sektor nehmen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE.")

# ---- Stochastik 2.2: n und p aus Erwartungswert und Standardabweichung (ungegliedert)
row("2026MgrundlegendAStochastik22", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen",
    typ_neben="Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben",
    stichwoerter="μ = n · p|σ = √(n · p · (1 − p))|p = 0,8 und n = 25|parameterfreier Term|P(X = 21)",
    voraussetzungen="Formeln für Erwartungswert und Standardabweichung der Binomialverteilung|Gleichungssystem durch Einsetzen lösen|Bernoulli-Formel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="binomialverteilte Zufallsgröße X mit Erwartungswert μ = 20 und Standardabweichung σ = 2",
    gesucht="parameterfreier Term für P(X = 21)",
    verfahren="aus σ^2 = n · p · (1 − p) = μ · (1 − p) folgt 4 = 20 · (1 − p), also p = 0,8 und n = μ/p = 25; dann Bernoulli-Formel für k = 21",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(25 über 21) · 0,8^21 · 0,2^4 (amtlich)",
    zwischenergebnis="1 − p = 0,2|p = 0,8|n = 25|Wert ≈ 0,187",
    niveau_geschaetzt="II",
    fehlerquelle="σ statt σ^2 in die Formel setzen und 2 = 20 · (1 − p) rechnen",
    bemerkung="Standardbezug: K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE. Eigene Schätzung II, amtlich bis III.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Extrempunkt an vorgegebener Stelle nachweisen", "Analysis", "Kurvenuntersuchung",
     "Für eine genannte Stelle zeigen, dass dort ein Hoch- oder Tiefpunkt liegt: erste Ableitung "
     "null (notwendige Bedingung) und Vorzeichen der zweiten Ableitung (hinreichende Bedingung).",
     "2026MgrundlegendAAnalysis11-a"),
    ("Abstand zweier Extrempunkte über die Punktsymmetrie berechnen", "Analysis",
     "Kurvenuntersuchung",
     "Aus einem bekannten Extrempunkt und der Punktsymmetrie des Graphen zum Ursprung den "
     "gegenüberliegenden Extrempunkt gewinnen und den Abstand der beiden Punkte berechnen.",
     "2026MgrundlegendAAnalysis11-b"),
    ("Flächeninhalt eines Dreiecks aus Extrempunkten der Sinusfunktion berechnen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Aufeinanderfolgende Extrempunkte von sin x als Eckpunkte eines Dreiecks lesen und dessen "
     "Flächeninhalt aus Grundseite (Vielfaches von π) und Höhe berechnen.",
     "2026MgrundlegendAAnalysis12-a"),
    ("Abstand von Extrempunkten einer gestreckten Sinusfunktion vergleichen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Aus den Parametern a und b in a · sin(b · x) die Streckung des Graphen in x- und y-Richtung "
     "erkennen und daraus den Abstand aufeinanderfolgender Extrempunkte mit dem der Grundfunktion "
     "vergleichen, ohne zu rechnen.",
     "2026MgrundlegendAAnalysis12-b"),
    ("Bestimmtes Integral einer ganzrationalen Funktion berechnen", "Analysis",
     "Stammfunktion und Hauptsatz",
     "Stammfunktion einer ganzrationalen Funktion bilden und den Wert des Integrals über ein "
     "Intervall mit dem Hauptsatz berechnen.",
     "2026MgrundlegendAAnalysis13-a"),
    ("Summe zweier Integrale als Flächeninhalt beurteilen", "Analysis",
     "Flächeninhalt durch Integration",
     "Beurteilen, ob die Summe von Integralen über Teilintervalle den Inhalt der vom Graphen und "
     "der x-Achse eingeschlossenen Fläche liefert, anhand des Vorzeichens der Integrale unterhalb "
     "der Achse.",
     "2026MgrundlegendAAnalysis13-b"),
    ("Graph der Funktion vom Graphen der Ableitung unterscheiden", "Analysis",
     "Ableitungsgraph und Funktionsgraph",
     "Von zwei abgebildeten Graphen begründen, welcher zur Funktion und welcher zur Ableitung "
     "gehört, über die Steigung des einen und das Vorzeichen des anderen in einem Bereich.",
     "2026MgrundlegendAAnalysis14-a"),
    ("Integral einer Differenzfunktion grafisch abschätzen", "Analysis",
     "Flächeninhalt durch Integration",
     "Das Integral über die Differenz zweier Funktionen als Fläche zwischen ihren Graphen "
     "deuten, diese in der Abbildung markieren und mit einem Vergleichsrechteck gegen eine "
     "Schranke abschätzen.",
     "2026MgrundlegendAAnalysis14-b"),
    ("Steigung einer Geraden am Graphen begründen", "Analysis", "Ableitung und Änderungsrate",
     "Den Ableitungswert einer linearen Funktion als ihre Steigung erkennen und diese am "
     "abgebildeten Graphen über ein Steigungsdreieck begründen.",
     "2026MgrundlegendAAnalysis21-a"),
    ("Ableitung eines Produkts aus Graphenwerten mit der Produktregel bestimmen", "Analysis",
     "Ableitungsregeln",
     "Die Ableitung von f · g an einer Stelle mit der Produktregel berechnen, wobei Funktionswerte "
     "und Steigungen von f und g nur aus abgebildeten Graphen abgelesen werden, etwa f' = 0 an "
     "einem Extrempunkt.",
     "2026MgrundlegendAAnalysis21-b"),
    ("Monotonie aus dem Vorzeichen der Ableitung am Graphen begründen", "Analysis",
     "Ableitungsgraph und Funktionsgraph",
     "Aus dem abgebildeten Graphen der Ableitung über deren Vorzeichen links und rechts einer "
     "Nullstelle das Monotonieverhalten der Funktion begründen.",
     "2026MgrundlegendAAnalysis22-a"),
    ("Aussage über Extrempunkte einer Stammfunktion beurteilen", "Analysis",
     "Stammfunktion und Hauptsatz",
     "Eine Behauptung über Extrempunkte einer Stammfunktion F beurteilen, indem F' = f genutzt "
     "und das Vorzeichen von f aus dem Graphen der Ableitung f' und einem Funktionswert "
     "erschlossen wird.",
     "2026MgrundlegendAAnalysis22-b"),
    ("Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen", "Analytische Geometrie",
     "Orthogonalität",
     "Über das Skalarprodukt zweier Seitenvektoren den rechten Winkel eines Dreiecks nachweisen "
     "und die Längen der Katheten als Vektorbeträge berechnen.",
     "2026MgrundlegendAAGLAA111-a"),
    ("Höhe einer Pyramide aus dem Volumen bestimmen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Aus dem gegebenen Volumen einer Pyramide und ihrer Grundfläche die Höhe bestimmen, wobei "
     "die Höhenkante über Skalarprodukte als senkrecht zur Grundfläche erkannt wird.",
     "2026MgrundlegendAAGLAA111-b"),
    ("Rechten Winkel eines Dreiecks mit Parameter nachweisen", "Analytische Geometrie",
     "Orthogonalität",
     "Zeigen, dass ein Dreieck, dessen Eckpunkt einen Parameter enthält, für jeden Parameterwert "
     "einen rechten Winkel hat, weil das Skalarprodukt der Seitenvektoren identisch null ist.",
     "2026MgrundlegendAAGLAA112-a"),
    ("Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen", "Analytische Geometrie",
     "Abstände",
     "Den Parameter eines Eckpunkts so bestimmen, dass zwei Seiten eines Dreiecks gleich lang sind, "
     "über das Gleichsetzen von Vektorbeträgen und Lösen der Wurzelgleichung.",
     "2026MgrundlegendAAGLAA112-b"),
    ("Lösung eines unterbestimmten Gleichungssystems unter Zusatzbedingungen auswählen",
     "Analytische Geometrie", "Lineare Gleichungssysteme",
     "Bei einem linearen Gleichungssystem mit unendlich vielen Lösungen die Lösungsschar mit einem "
     "Parameter angeben und aus Bedingungen wie Vorzeichen und Ganzzahligkeit eine bestimmte "
     "Lösung auswählen.",
     "2026MgrundlegendAAGLAA12"),
    ("Punktprobe an einer Ebenengleichung durchführen", "Analytische Geometrie", "Lagebeziehungen",
     "Die Koordinaten eines Punktes in die Koordinatengleichung einer Ebene einsetzen und aus dem "
     "Erfülltsein der Gleichung auf die Lage in der Ebene schließen.",
     "2026MgrundlegendAAGLAA211-a"),
    ("Orthogonalität von Gerade und Ebene über Normalen- und Richtungsvektor begründen",
     "Analytische Geometrie", "Orthogonalität",
     "Begründen, dass eine Gerade senkrecht auf einer Ebene steht, weil ihr Richtungsvektor ein "
     "Vielfaches des Normalenvektors der Ebene ist.",
     "2026MgrundlegendAAGLAA211-a"),
    ("Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen", "Analytische Geometrie",
     "Spiegelung",
     "Den Spiegelpunkt eines Punktes an einer Ebene bestimmen, wenn der Lotfußpunkt bereits "
     "bekannt ist, indem der Verbindungsvektor vom Lotfußpunkt aus in Gegenrichtung abgetragen "
     "wird.",
     "2026MgrundlegendAAGLAA211-b"),
    ("Koordinaten eines Eckpunkts eines Prismas angeben", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Aus gegebenen Eckpunkten eines geraden Prismas und dem Schrägbild die Koordinaten eines "
     "weiteren Eckpunkts der Deckfläche angeben.",
     "2026MgrundlegendAAGLAA213-a"),
    ("Dreieck in ein Schrägbild einzeichnen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Einen durch Koordinaten gegebenen Punkt auf einer Kante im Schrägbild verorten und das "
     "Dreieck aus ihm und zwei Eckpunkten des Körpers einzeichnen.",
     "2026MgrundlegendAAGLAA213-b"),
    ("Parameter eines Punktes aus einer Flächengleichheit bestimmen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Den Parameter eines Punktes so bestimmen, dass zwei Dreiecke mit gemeinsamer Seite gleichen "
     "Flächeninhalt haben, über den Vergleich der zugehörigen Höhen oder Katheten.",
     "2026MgrundlegendAAGLAA213-c"),
    ("Punkt aus Orthogonalitäts- und Ebenenbedingung bestimmen", "Analytische Geometrie",
     "Orthogonalität",
     "Einen Punkt mit teilweise bekannten Koordinaten aus der Bedingung, dass zwei Verbindungs"
     "vektoren orthogonal sind, und einer Ebenengleichung über ein lineares Gleichungssystem "
     "bestimmen.",
     "2026MgrundlegendAAGLAA221"),
    ("Volumen eines Prismas über einer Raute berechnen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Das Volumen eines geraden Prismas berechnen, dessen Grundfläche eine Raute mit Eckpunkten "
     "auf den Koordinatenachsen ist, über die Rautenfläche aus den Diagonalen und die Höhe.",
     "2026MgrundlegendAAGLAA222-a"),
    ("Ortsvektor eines gedrehten Punktes als Term aufstellen", "Analytische Geometrie",
     "Vektoren und Rechenoperationen",
     "Für einen Punkt, der durch Drehung eines Körpers um eine Kante in eine Koordinatenebene "
     "kommt, den Ortsvektor als Summe aus einem Ortsvektor und einem auf die richtige Länge "
     "gebrachten, zur Drehkante senkrechten Vektor aufstellen.",
     "2026MgrundlegendAAGLAA222-b"),
    ("Trefferwahrscheinlichkeit aus dem ganzzahligen Erwartungswert im Diagramm ermitteln",
     "Stochastik", "Kenngrößen von Verteilungen",
     "Aus dem Säulendiagramm einer Binomialverteilung mit bekanntem n die Lage des ganzzahligen "
     "Erwartungswerts ablesen und daraus p über n · p bestimmen.",
     "2026MgrundlegendAStochastik11-a"),
    ("Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen", "Stochastik",
     "Binomialverteilung",
     "Aus dem Säulendiagramm einer Verteilung die Werte k ablesen, für die eine Einzel- oder eine "
     "kumulierte Wahrscheinlichkeit eine vorgegebene Bedingung erfüllt.",
     "2026MgrundlegendAStochastik11-b"),
    ("Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben", "Stochastik",
     "Binomialverteilung",
     "Für ein Ereignis in einer Bernoulli-Kette einen Rechenterm mit Potenzen von p und 1 − p und "
     "der Anzahl der Anordnungen angeben, ohne den Wert zu berechnen.",
     "2026MgrundlegendAStochastik12-a"),
    ("Ergebnisse zum Gegenereignis zweier Ereignisse aufzählen", "Stochastik",
     "Ereignisse und Mengenoperationen",
     "Alle Ergebnisse eines mehrstufigen Experiments aufzählen, bei denen keines von zwei in "
     "Worten beschriebenen Ereignissen eintritt.",
     "2026MgrundlegendAStochastik12-b"),
    ("Fehlende Wahrscheinlichkeiten im Baumdiagramm über die Pfadregel ermitteln", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "In einem teilweise beschrifteten Baumdiagramm fehlende Ast- oder Pfadwahrscheinlichkeiten "
     "aus gegebenen Pfad- und Astwerten über die Pfadmultiplikation bestimmen.",
     "2026MgrundlegendAStochastik13-a"),
    ("Bedingte Wahrscheinlichkeit aus dem Baumdiagramm mit einer Schranke vergleichen",
     "Stochastik", "Bedingte Wahrscheinlichkeit und Bayes",
     "Eine bedingte Wahrscheinlichkeit als Quotient aus einem Pfad und der Summe der Pfade mit der "
     "Bedingung berechnen und mit einer vorgegebenen Schranke vergleichen.",
     "2026MgrundlegendAStochastik13-b"),
    ("Sektorwinkel eines Glücksrads aus einer Wahrscheinlichkeitsbedingung berechnen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die Sektorwahrscheinlichkeit eines zweifarbigen Glücksrads aus einer Bedingung an ein "
     "zweistufiges Ergebnis über eine quadratische Gleichung bestimmen und in den "
     "Mittelpunktswinkel umrechnen.",
     "2026MgrundlegendAStochastik21"),
    ("Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen",
     "Stochastik", "Kenngrößen von Verteilungen",
     "Aus μ = n · p und σ = √(n · p · (1 − p)) die Parameter n und p einer Binomialverteilung "
     "bestimmen.",
     "2026MgrundlegendAStochastik22"),
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
