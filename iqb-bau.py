# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.5 · 14.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.7

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

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
    "stapel": "2019-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2019MerhoehtAAnalysis11": 5,
        "2019MerhoehtAAnalysis12": 5,
        "2019MerhoehtAAnalysis2": 5,
        "2019MerhoehtAAGLAA11": 5,
        "2019MerhoehtAAGLAA12": 5,
        "2019MerhoehtAAGLAA21": 5,
        "2019MerhoehtAAGLAA22": 5,
        "2019MerhoehtAStochastik11": 5,
        "2019MerhoehtAStochastik12": 5,
        "2019MerhoehtAStochastik2": 5,
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
# niveau_geschaetzt nach der Deutungsliste v0.7; bei III nennt bemerkung den Eintrag.

# ---- Analysis 1.1: 1 − 1/x²
HYP_SKIZZE = ("Koordinatensystem mit Skalen −3 bis 3 auf der x-Achse, −3 bis 1 auf der y-Achse; Graph von 1 − 1/x² "
              "achsensymmetrisch, zwei Äste von oben (y → 1 für |x| → ∞) durch die Nullstellen ±1 steil nach −∞ an der y-Achse; "
              "Gerade y = −3 nicht eingezeichnet")
row("2019MerhoehtAAnalysis11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Schnittstelle mit einer waagerechten Geraden durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="f(1/2) = 1 − 1/(1/4) = 1 − 4 = −3",
    voraussetzungen="Funktionswert berechnen|Schnittpunkt mit y = −3 heißt f(x) = −3",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=HYP_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 1 − 1/x² in IR ohne 0, Nullstellen ±1, Graph achsensymmetrisch; Gerade g: y = −3",
    gesucht="Nachweis, dass ein Schnittpunkt von g und dem Graphen die x-Koordinate 1/2 hat",
    verfahren="f(1/2) berechnen",
    schritte="1", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(1/2) = −3 (amtlich)",
    zwischenergebnis="zweiter Schnittpunkt bei −1/2",
    niveau_geschaetzt="I",
    fehlerquelle="1/(1/2)² = 2 statt 4",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2019MerhoehtAAnalysis11", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph, x-Achse und waagerechter Gerade aus Rechteck und Integral berechnen", typ_neben="",
    stichwoerter="Fläche symmetrisch zur y-Achse|Rechteck von −1/2 bis 1/2 unter der x-Achse bis y = −3: 1 · 3|dazu zweimal |∫ von 1/2 bis 1 über f(x) dx| = 2 · 1/2|Stammfunktion x + 1/x|gesamt 4",
    voraussetzungen="Symmetrie ausnutzen|Zerlegung in Rechteck und Flächenstück unter der x-Achse|Stammfunktion von 1/x²|Betrag des Integrals",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=HYP_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1 − 1/x², Nullstellen ±1, Gerade y = −3 mit Schnittstellen ±1/2 (aus a)",
    gesucht="Inhalt der Fläche, die Graph, x-Achse und g einschließen",
    verfahren="Rechteck 1 · 3 plus zweimal den Betrag des Integrals von 1/2 bis 1",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2019MerhoehtAAnalysis11-a",
    ergebnis="1 · 3 + 2 · |∫ von 1/2 bis 1 über f(x) dx| = 3 + 2 · |[x + 1/x] von 1/2 bis 1| = 3 + 2 · 1/2 = 4 (amtlich)",
    zwischenergebnis="∫ von 1/2 bis 1 über f(x) dx = −1/2",
    niveau_geschaetzt="II",
    fehlerquelle="Integral von −1/2 bis 1/2 ansetzen (Polstelle bei 0)",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt. Die Symmetrie ist im Text vorgegeben, Zerlegung in Rechteck und Integral ist Verkettung ohne Deutung, II.")

# ---- Analysis 1.2: Graph und Ableitungsgraphen
GF_SKIZZE = ("vier kleine Koordinatensysteme mit Skalen −3 bis 3: Gf mit Hochpunkt bei etwa (−1,5; 1), Nullstellen bei etwa −3, 0 und 3, "
             "Tiefpunkt bei etwa (1,5; −1); Graph I Parabel nach oben mit Nullstellen etwa ±1,5 und Scheitel (0; −1); "
             "Graph II flache Parabel nach oben mit Scheitel (0; −1) und Nullstellen etwa ±3; Graph III steile Parabel mit "
             "Scheitel (0; −2) und Nullstellen etwa ±1,5")
row("2019MerhoehtAAnalysis12", "a", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Graphen von Funktion und Ableitung einander zuordnen", typ_neben="",
    stichwoerter="Graph I|II nicht: Extremstellen von f müssen Nullstellen von f' sein (Nullstellen von II bei ±3)|III nicht: Steigung von Gf bei 0 ist nicht kleiner als −1 (III hat f'(0) = −2)",
    voraussetzungen="Extremstellen von f als Nullstellen von f'|Steigung an einer Stelle mit dem Wert von f' vergleichen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Graph Gf; drei Graphen I, II, III, einer davon gehört zu f'",
    gesucht="der Ableitungsgraph und Begründung, warum die beiden anderen nicht infrage kommen",
    verfahren="Nullstellen von f' mit den Extremstellen von f vergleichen, Steigung bei 0 abschätzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Graph I; Graph II kommt nicht infrage, da die Extremstellen von f Nullstellen von f' sein müssen; Graph III kommt nicht infrage, da die Steigung des Graphen von f im Punkt (0 | f(0)) nicht kleiner als −1 ist (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="III wegen gleicher Nullstellen für richtig halten und den Wert bei 0 nicht prüfen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. Amtlich. Typ wiederverwendet (Zuordnen von Graph und Ableitungsgraph ist nach der Liste II).")

row("2019MerhoehtAAnalysis12", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Monotonie aus dem Vorzeichen der Ableitung am Graphen begründen", typ_neben="",
    stichwoerter="F' = f|f(x) ≤ 0 auf [1; 3] (Graph unterhalb der x-Achse)|F monoton fallend",
    voraussetzungen="F' = f|Monotonie aus dem Vorzeichen der Ableitung",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph Gf; F ist eine Stammfunktion von f; Intervall [1; 3]",
    gesucht="Monotonieverhalten von F in [1; 3] mit Begründung",
    verfahren="Vorzeichen von f auf dem Intervall ablesen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="für 1 ≤ x ≤ 3 gilt F'(x) = f(x) ≤ 0, damit ist F im gegebenen Intervall monoton fallend (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Monotonie von f statt von F angeben (f fällt bis 1,5 und steigt dann)",
    bemerkung="Standardbezug: K1 II, K2 I, K4 I. Amtlich. Typ wiederverwendet (f ist hier die Ableitung von F, gleiche Fertigkeit). (e) ohne Verkettung, ein einziger Schritt: II.")

# ---- Analysis 2: f' = e^{g(x)}
G_SKIZZE = ("Koordinatensystem ohne Skalen; Graph Gg von links unten steil steigend, Hochpunkt links der y-Achse knapp über der "
            "x-Achse, danach flach fallend, rechts unterhalb der x-Achse gegen die Achse laufend")
row("2019MerhoehtAAnalysis2", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Fehlende Extrempunkte über eine positive Ableitung begründen", typ_neben="",
    stichwoerter="f'(x) = e^{g(x)} > 0 für alle x|keine Nullstelle von f'|kein Extrempunkt",
    voraussetzungen="e-Funktion nur positiv|notwendige Bedingung f' = 0",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=G_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Graph Gg einer differenzierbaren Funktion g; f in IR mit f'(x) = e^{g(x)}",
    gesucht="ob der Graph von f einen Extrempunkt hat",
    verfahren="Vorzeichen von f' aus der e-Funktion ablesen",
    schritte="1", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="wegen f'(x) = e^{g(x)} > 0 für alle x ∈ IR hat der Graph von f keinen Extrempunkt (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Hochpunkt von g als Extrempunkt von f deuten",
    bemerkung="Standardbezug: K1 II, K4 I, K5 I. Amtlich. Eine Beobachtung mit Begründung, aber über die Verkettung f' = e^g: II.")

row("2019MerhoehtAAnalysis2", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendepunkt über den Vorzeichenwechsel der zweiten Ableitung aus der Kettenregel am Graphen nachweisen", typ_neben="",
    stichwoerter="f''(x) = g'(x) · e^{g(x)}|e^{g(x)} > 0|Vorzeichen von f'' wie das von g'|g' wechselt am Maximum von g das Vorzeichen|Wendepunkt",
    voraussetzungen="Kettenregel|Faktor e^g positiv|Vorzeichenwechsel von g' an der Extremstelle von g|hinreichende Bedingung für Wendepunkt",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=G_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Graph Gg mit einem Hochpunkt; f'(x) = e^{g(x)}",
    gesucht="ob der Graph von f einen Wendepunkt hat",
    verfahren="f'' mit der Kettenregel bilden, Vorzeichenwechsel von g' am Graphen ablesen",
    schritte="3", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="f''(x) = g'(x) · e^{g(x)}; an der Stelle, an der g ein Maximum annimmt, ändert sich das Vorzeichen von g'(x); wegen e^{g(x)} > 0 ändert sich damit an dieser Stelle auch das Vorzeichen von f''(x), d. h. der Graph von f hat einen Wendepunkt (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Wendepunkt von g statt von f untersuchen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis mit der hergeleiteten Beziehung f'' = g' · e^g, verkettet mit der Deutung des Vorzeichenwechsels von g' am Graphen.")

# ---- AG/LA (A1) 1: zwei Zustände
AB_SKIZZE = ("Übergangsdiagramm mit zwei Kreisen A und B; Schleife an A mit 1/2, Pfeil von A nach B mit 1/2, Schleife an B mit 1")
row("2019MerhoehtAAGLAA11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Langfristige Verteilung aus dem Übergangsdiagramm beschreiben", typ_neben="",
    stichwoerter="B absorbierend (Schleife 1)|von A geht je Schritt die Hälfte nach B|Anteil in A → 0, Anteil in B → 1",
    voraussetzungen="Übergangsdiagramm lesen|absorbierenden Zustand erkennen",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Diagramm", skizze=AB_SKIZZE, kontext="Zustandssystem", textumfang="lang",
    gegeben="Zustände A und B mit Anteilen a_n, b_n > 0 zum Zeitpunkt 0; Diagramm: A bleibt mit 1/2, A → B mit 1/2, B bleibt mit 1; M = ((1/2; 0), (1/2; 1))",
    gesucht="Beschreibung der langfristigen Entwicklung der Verteilung mithilfe der Abbildung",
    verfahren="Halbierung des A-Anteils je Schritt, B nimmt alles auf",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="der Anteil im Zustand A nähert sich 0, während sich der Anteil im Zustand B 1 nähert (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="stationäre Verteilung mit beiden Anteilen größer null vermuten",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. Amtlich. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2019MerhoehtAAGLAA11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Kleinsten Zeitpunkt für das Unterschreiten eines Anteils aus dem Matrixterm bestimmen", typ_neben="",
    stichwoerter="M · (a_n; b_n) = (1/2 a_n; 1/2 a_n + b_n)|a_n = (1/2)^n · a_0|(1/2)³ = 1/8 > 1/10, (1/2)⁴ = 1/16 < 1/10|n = 4",
    voraussetzungen="Matrix-Vektor-Produkt|Halbierung je Schritt als Potenz|„auf weniger als 10 % abnimmt“ als (1/2)^n < 0,1",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=AB_SKIZZE, kontext="Zustandssystem", textumfang="mittel",
    gegeben="M = ((1/2; 0), (1/2; 1)); Term M · (a_n; b_n); Anteil in A soll bis zum Zeitpunkt n auf weniger als 10 % des Anfangswerts abnehmen",
    gesucht="kleinster solcher Wert von n",
    verfahren="aus M · v den Faktor 1/2 für a_n ablesen, Potenzen mit 0,1 vergleichen",
    schritte="3", zahlenraum="Bruch|Potenz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="M · (a_n; b_n) = (1/2 a_n; 1/2 a_n + b_n); (1/2)³ = 1/8 > 1/10, (1/2)⁴ = 1/16 < 1/10, d. h. der gesuchte Wert von n ist 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="n = 3 angeben (1/8 ist nicht kleiner als 1/10)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. „Weniger als 10 %“ ist wörtlich vorgegeben, Verkettung ohne Deutung: II. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A1) 2: orthogonale Matrizen
row("2019MerhoehtAAGLAA12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Orthogonalität einer Matrix über das Produkt mit der Transponierten nachweisen", typ_neben="",
    stichwoerter="M^T = ((3/5; 4/5), (−4/5; 3/5))|M^T · M = ((9/25 + 16/25; −12/25 + 12/25), (−12/25 + 12/25; 16/25 + 9/25)) = E",
    voraussetzungen="Definition der transponierten Matrix|Matrixprodukt|Vergleich mit der Einheitsmatrix",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Definition: M^T durch Vertauschen von b und c; M orthogonal, wenn M^T · M = E; M = ((3/5; −4/5), (4/5; 3/5))",
    gesucht="Nachweis, dass M orthogonal ist",
    verfahren="M^T bilden und M^T · M ausrechnen",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="((3/5; 4/5), (−4/5; 3/5)) · ((3/5; −4/5), (4/5; 3/5)) = ((1; 0), (0; 1)) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="M · M statt M^T · M berechnen",
    bemerkung="Standardbezug: K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Neue Begriffe (transponiert, orthogonal) aus dem Text anwenden, II. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2019MerhoehtAAGLAA12", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Hohe Potenz einer Vertauschungsmatrix über das Quadrat gleich Einheitsmatrix bestimmen", typ_neben="",
    stichwoerter="V = ((0; 1), (1; 0)), V² = E|V^101 = (V²)^50 · V = V|V^T · V = V · V = E, also orthogonal",
    voraussetzungen="V² = E erkennen|Potenzgesetze für Matrizen|Definition aus dem Text anwenden",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Definition der Orthogonalität aus a; Matrix ((0; 1), (1; 0))^101",
    gesucht="ob diese Matrix orthogonal ist",
    verfahren="Potenz über V² = E auf V zurückführen, dann V^T · V prüfen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2019MerhoehtAAGLAA12-a",
    ergebnis="((0; 1), (1; 0))^101 = (((0; 1), (1; 0)) · ((0; 1), (1; 0)))^50 · ((0; 1), (1; 0)) = ((1; 0), (0; 1))^50 · ((0; 1), (1; 0)) = ((0; 1), (1; 0)); ((0; 1), (1; 0))^T · ((0; 1), (1; 0)) = ((1; 0), (0; 1)), d. h. die Matrix ist orthogonal (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Potenz nicht auflösen und die Orthogonalität nur behaupten",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Sonderfall erkennen – V² = E, ungerade Potenz gleich V – und mit dem Nachweis aus a verketten. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A2) 1: Gerade und Ebene
SP_SKIZZE = ("Skizze ohne Koordinatensystem: graues Parallelogramm als Ebene E, Gerade g schräg durch die Ebene (hinter der Ebene "
             "gestrichelt), Pfeil SP1 links oben auf g in Richtung vom Schnittpunkt weg; S, P1, P2 nicht beschriftet")
row("2019MerhoehtAAGLAA21", "a", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schnittpunkt von Gerade und Ebene berechnen", typ_neben="",
    stichwoerter="Gerade in E einsetzen: 2r + 2 · (2 + 4r) − 2r = 2|r = −1/4|S(−1/2; 1; −1/4)",
    voraussetzungen="Koordinaten der Geradenpunkte in die Koordinatengleichung einsetzen|lineare Gleichung|Punkt aus r",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=SP_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="g: x = (0; 2; 0) + r · (2; 4; 1); E: x1 + 2x2 − 2x3 = 2; g und E schneiden sich in S",
    gesucht="Koordinaten von S",
    verfahren="Einsetzen, r bestimmen, Punkt berechnen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="2r + 2 · (2 + 4r) − 2r = 2 ⇔ r = −1/4, d. h. S(−1/2 | 1 | −1/4) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="−2x3 mit +2r ansetzen",
    bemerkung="Standardbezug: K5 II. Amtlich, eigene Rechnung bestätigt. Verkettung Einsetzen – lösen – Punkt, II.")

row("2019MerhoehtAAGLAA21", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Punkt zu einem Vektorterm in das Schrägbild einzeichnen", typ_neben="",
    stichwoerter="S Schnittpunkt von g und E|P1 auf g in Richtung SP1 vom Schnittpunkt|OP2 = OP1 − 4 · SP1: P2 auf g auf der anderen Seite von S, dreimal so weit wie P1",
    voraussetzungen="Vektorterm als Verschiebung deuten|P1 − 4 · SP1 = S − 3 · SP1",
    format="Zeichnen", operator="Zeichnen Sie ein", antwort="Grafik",
    material="Skizze", skizze=SP_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Abbildung mit E, g und einem Repräsentanten von SP1; P1 auf g, nicht in E; OP2 = OP1 − 4 · SP1",
    gesucht="S, P1 und P2 in der Abbildung",
    verfahren="S am Durchstoßpunkt, P1 am Pfeilende, P2 jenseits von S im dreifachen Abstand",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="S am Schnitt von g und E, P1 auf g oberhalb von E am Ende des Pfeils SP1, P2 auf g unterhalb von E mit |SP2| = 3 · |SP1| – Zeichnung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="P2 auf derselben Seite wie P1 einzeichnen (Vorzeichen von −4)",
    bemerkung="Standardbezug: K2 II, K4 II, K6 I. Amtlich. Typ wiederverwendet (hier Abbildung von Ebene und Gerade statt Körper, gleiche Fertigkeit).")

# ---- AG/LA (A2) 2: gleiche Koordinaten
row("2019MerhoehtAAGLAA22", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Punkt der Ebene mit drei gleichen Koordinaten bestimmen", typ_neben="",
    stichwoerter="x1 = x2 = x3 = a|3a + 2a + 2a = 6 ⇔ a = 6/7|Punkt (6/7; 6/7; 6/7)",
    voraussetzungen="Bedingung in eine Variable übersetzen|Koordinatengleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: 3x1 + 2x2 + 2x3 = 6 enthält einen Punkt mit drei übereinstimmenden Koordinaten",
    gesucht="diese Koordinaten",
    verfahren="a für alle drei Koordinaten einsetzen und lösen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="mit x1 = x2 = x3 = a ergibt sich 3a + 2a + 2a = 6 ⇔ a = 6/7 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="a = 6/3 aus dem ersten Koeffizienten",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Die Übersetzung „drei Koordinaten übereinstimmen“ in x1 = x2 = x3 ist wörtlich vorgegeben, II.")

row("2019MerhoehtAAGLAA22", "b", seite="1", punkte="3", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Existenz unendlich vieler Ebenen ohne Punkt mit drei gleichen Koordinaten begründen", typ_neben="",
    stichwoerter="Punkte mit gleichen Koordinaten bilden die Gerade x = b · (1; 1; 1)|Ebenen parallel zu dieser Geraden, die sie nicht enthalten|unendlich viele solche Ebenen",
    voraussetzungen="Punktmenge als Ursprungsgerade erkennen|echt parallele Ebenen zu einer Geraden|Existenz unendlich vieler",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Aussage: Es gibt unendlich viele Ebenen, die keinen Punkt enthalten, dessen drei Koordinaten übereinstimmen",
    gesucht="Begründung, dass die Aussage richtig ist",
    verfahren="Punktmenge als Gerade durch den Ursprung mit Richtung (1; 1; 1) beschreiben, echt parallele Ebenen angeben",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="alle Punkte, deren drei Koordinaten übereinstimmen, liegen auf der Geraden x = b · (1; 1; 1), b ∈ IR; es gibt unendlich viele Ebenen, die parallel zu dieser Geraden sind und die Gerade nicht enthalten (amtlich)",
    zwischenergebnis="z. B. x1 − x2 = c mit c ≠ 0",
    niveau_geschaetzt="III",
    fehlerquelle="nur eine Beispielebene nennen",
    bemerkung="Standardbezug: K1 III, K2 III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Bedingung „gleiche Koordinaten“ in eine Gerade übersetzen und (b) die Lage echt paralleler Ebenen als Sonderfall erkennen, verkettet.")

# ---- Stochastik 1.1: kumulierte Verteilung, n = 5
KUM_SKIZZE = ("Säulendiagramm P(X ≤ k) über k = 0 bis 5 mit y-Marken 0,5 und 1: Säulen bei 0 etwa 0,03, bei 1 etwa 0,2, bei 2 etwa 0,5, "
              "bei 3 etwa 0,85, bei 4 etwa 0,97; Säule bei 5 fehlt")
row("2019MerhoehtAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit aus dem Diagramm kumulierter Wahrscheinlichkeiten ermitteln", typ_neben="",
    stichwoerter="P(X ≤ 5) = 1 eintragen|P(X = 2) = P(X ≤ 2) − P(X ≤ 1) ≈ 0,5 − 0,2 = 0,3",
    voraussetzungen="kumulierte Verteilung: letzter Wert 1|Einzelwahrscheinlichkeit als Differenz benachbarter kumulierter Werte",
    format="Rechnung|Eintragen", operator="Zeichnen Sie ein|Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=KUM_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Diagramm mit kumulierten Werten P(X ≤ k) einer Binomialverteilung mit n = 5 für k = 0 bis 4",
    gesucht="Säule für k = 5 und P(X = 2)",
    verfahren="Säule der Höhe 1 ergänzen, Differenz zweier kumulierter Werte ablesen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Säule bei k = 5 mit Höhe 1; P(X = 2) ≈ 0,5 − 0,2 = 0,3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="P(X ≤ 2) = 0,5 als P(X = 2) ablesen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. Amtlich, Ablesung bestätigt. Vom Typ „Werte zu Wahrscheinlichkeitsbedingungen aus dem Säulendiagramm ablesen“ getrennt: hier Differenz kumulierter Werte, dort Ablesen von k.")

row("2019MerhoehtAStochastik11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Trefferwahrscheinlichkeit aus einer Gleichung zweier Einzelwahrscheinlichkeiten berechnen", typ_neben="",
    stichwoerter="P(Y = 4) = 5 p⁴ (1 − p), P(Y = 5) = p⁵|5 p⁴ (1 − p) = 10 p⁵|5 − 5p = 10p (p > 0)|p = 1/3",
    voraussetzungen="Bernoulli-Formel für k = 4 und k = 5|Kürzen durch p⁴ wegen p > 0|lineare Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Y binomialverteilt mit n = 5 und p > 0; P(Y = 4) = 10 · P(Y = 5)",
    gesucht="Wert von p",
    verfahren="beide Wahrscheinlichkeiten als Terme in p, Gleichung lösen",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="für p > 0 gilt 5 · p⁴ · (1 − p) = 10 · p⁵ ⇔ 5 − 5p = 10p ⇔ 15p = 5 ⇔ p = 1/3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="(5 über 4) = 5 vergessen",
    bemerkung="Standardbezug: K2 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Die Bedingung ist als Gleichung vorgegeben, II.")

# ---- Stochastik 1.2: Glücksrad 0, 1, 2, 9, 9
row("2019MerhoehtAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen", typ_neben="",
    stichwoerter="P(2) = P(0) = P(1) = 1/5, P(9) = 2/5|(1/5)³ · 2/5 = 2/625",
    voraussetzungen="Sektorwahrscheinlichkeiten|Pfadmultiplikation",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="mittel",
    gegeben="Glücksrad mit fünf gleich großen Sektoren 0, 1, 2, 9, 9; viermal gedreht",
    gesucht="Wahrscheinlichkeit für die Folge 2, 0, 1, 9 in dieser Reihenfolge",
    verfahren="Produkt der vier Sektorwahrscheinlichkeiten",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(1/5)³ · 2/5 = 2/625 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="P(9) = 1/5 statt 2/5",
    bemerkung="Standardbezug: K3 I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Term für die Wahrscheinlichkeit eines mehrstufigen Pfads angeben“ getrennt (dort Term angeben, hier Wert berechnen).")

row("2019MerhoehtAStochastik12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit einer vorgegebenen Augensumme bei zwei Würfen über Pfade berechnen", typ_neben="",
    stichwoerter="Summe ≥ 11 nur mit mindestens einer 9: 9 + 9 = 18, 9 + 2 = 2 + 9 = 11|2/5 · 2/5 + 2 · 2/5 · 1/5 = 8/25",
    voraussetzungen="günstige Ergebnispaare finden|beide Reihenfolgen zählen|Pfadregeln",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="kurz",
    gegeben="Glücksrad 0, 1, 2, 9, 9; zweimal gedreht",
    gesucht="Wahrscheinlichkeit, dass die Summe mindestens 11 beträgt",
    verfahren="Paare mit Summe ≥ 11 aufzählen, Pfadwahrscheinlichkeiten addieren",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="2/5 · 2/5 + 2 · 2/5 · 1/5 = 8/25 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Paar (9; 2) nur einmal zählen (6/25)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Glücksrad statt Würfel, Schranke „mindestens 11“ statt fester Summe, gleiche Fertigkeit).")

# ---- Stochastik 2: zwei Urnen
row("2019MerhoehtAStochastik2", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Mögliche Anzahlen nach dem Umlegen zweier Kugeln angeben", typ_neben="",
    stichwoerter="rot weg, blau zurück: 4|gleiche Farbe zurück: 5|blau weg, rot zurück: 6",
    voraussetzungen="Fälle nach den Farben der beiden umgelegten Kugeln",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="lang",
    gegeben="Urne A mit 5 roten und 5 blauen Kugeln, Urne B mit n roten und 3n blauen (n > 0); eine Kugel von A nach B, dann eine von B nach A",
    gesucht="alle möglichen Anzahlen roter Kugeln in A danach",
    verfahren="Farbkombinationen der umgelegten Kugeln durchgehen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="in der Urne A können sich 4, 5 oder 6 rote Kugeln befinden (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="5 vergessen (gleiche Farbe hin und zurück)",
    bemerkung="Standardbezug: K3 I, K6 I. Amtlich.")

row("2019MerhoehtAStochastik2", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Kugelzahl aus einer Wahrscheinlichkeitsbedingung beim Umlegen einer Kugel bestimmen", typ_neben="",
    stichwoerter="fünf rote in A heißt: umgelegte Kugeln gleichfarbig|rot hin, rot zurück: 1/2 · (n + 1)/(4n + 1)|blau hin, blau zurück: 1/2 · (3n + 1)/(4n + 1)|Summe (2n + 1)/(4n + 1) = 15/29 ⇔ n = 7",
    voraussetzungen="Bedingung auf die Farben der umgelegten Kugeln zurückführen|Urne B nach dem ersten Umlegen: 4n + 1 Kugeln|zwei Pfade addieren|Bruchgleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Urnen wie in a; für ein bestimmtes n ist die Wahrscheinlichkeit für fünf rote Kugeln in A nach dem Umlegen 15/29",
    gesucht="dieser Wert von n",
    verfahren="beide gleichfarbigen Pfade als Terme in n, Summe gleich 15/29 setzen",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="2019MerhoehtAStochastik2-a",
    ergebnis="1/2 · (n + 1)/(4n + 1) + 1/2 · (3n + 1)/(4n + 1) = (4n + 2)/(2 · (4n + 1)) = (2n + 1)/(4n + 1) = 15/29 ⇔ n = 7 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Urne B nach dem ersten Umlegen mit 4n statt 4n + 1 Kugeln ansetzen",
    bemerkung="Standardbezug: K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „fünf rote Kugeln“ in die beiden gleichfarbigen Umlegepfade übersetzen, verkettet zur Bruchgleichung in n. Typ wiederverwendet (2023-ea-A; dort einmaliges Umlegen, hier hin und zurück – gleiche Fertigkeit, Vorschlag für den Abgleich: Definition um mehrmaliges Umlegen erweitern).")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Nullstellen und Werte: Schnittstelle mit einer waagerechten Geraden durch Einsetzen nachweisen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Zeigen, dass der Graph eine waagerechte Gerade an einer genannten Stelle schneidet, indem der Funktionswert "
     "dort berechnet wird.",
     "2019MerhoehtAAnalysis11-a"),
    ("Fläche: Fläche zwischen Graph, x-Achse und waagerechter Gerade aus Rechteck und Integral berechnen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Inhalt einer von Graph, x-Achse und einer waagerechten Geraden begrenzten Fläche berechnen, indem sie in "
     "ein Rechteck und Flächenstücke unter dem Graphen zerlegt wird (Symmetrie, Betrag des Integrals).",
     "2019MerhoehtAAnalysis11-b"),
    ("Fehlende Extrempunkte über eine positive Ableitung begründen", "Analysis", "Kurvenuntersuchung",
     "Begründen, dass der Graph keinen Extrempunkt hat, weil die Ableitung (etwa als e-Funktion) überall positiv ist.",
     "2019MerhoehtAAnalysis2-a"),
    ("Wendepunkt über den Vorzeichenwechsel der zweiten Ableitung aus der Kettenregel am Graphen nachweisen", "Analysis",
     "Kurvenuntersuchung",
     "Für eine Funktion mit f' = e^g die zweite Ableitung mit der Kettenregel bilden und aus dem am Graphen von g "
     "ablesbaren Vorzeichenwechsel von g' einen Wendepunkt von f nachweisen.",
     "2019MerhoehtAAnalysis2-b"),
    ("Übergangsprozess: Langfristige Verteilung aus dem Übergangsdiagramm beschreiben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Aus einem Übergangsdiagramm (etwa mit absorbierendem Zustand) beschreiben, wie sich die Verteilung auf lange "
     "Sicht entwickelt, ohne zu rechnen.",
     "2019MerhoehtAAGLAA11-a"),
    ("Übergangsprozess: Kleinsten Zeitpunkt für das Unterschreiten eines Anteils aus dem Matrixterm bestimmen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus dem Term M · v den Faktor je Schritt für einen Anteil ablesen und den kleinsten Zeitpunkt bestimmen, zu "
     "dem der Anteil eine vorgegebene Schranke unterschreitet (Potenzen vergleichen).",
     "2019MerhoehtAAGLAA11-b"),
    ("Matrizenalgebra: Orthogonalität einer Matrix über das Produkt mit der Transponierten nachweisen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Mit den im Text definierten Begriffen transponierte Matrix und orthogonale Matrix nachweisen, dass eine "
     "gegebene Matrix orthogonal ist (M^T · M = E ausrechnen).",
     "2019MerhoehtAAGLAA12-a"),
    ("Matrizenalgebra: Hohe Potenz einer Vertauschungsmatrix über das Quadrat gleich Einheitsmatrix bestimmen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine hohe Potenz einer Matrix mit M² = E auf M oder E zurückführen und eine Eigenschaft (etwa "
     "Orthogonalität) der Potenz untersuchen.",
     "2019MerhoehtAAGLAA12-b"),
    ("Schnittpunkt von Gerade und Ebene berechnen", "Analytische Geometrie", "Schnittmengen",
     "Den Schnittpunkt einer Geraden in Parameterform mit einer Ebene in Koordinatenform berechnen (Einsetzen, "
     "Parameter bestimmen, Punkt angeben).",
     "2019MerhoehtAAGLAA21-a"),
    ("Punkt und Ebene: Punkt der Ebene mit drei gleichen Koordinaten bestimmen", "Analytische Geometrie", "Lagebeziehungen",
     "Den Punkt einer Ebene bestimmen, dessen Koordinaten übereinstimmen (x1 = x2 = x3 = a in die "
     "Koordinatengleichung einsetzen).",
     "2019MerhoehtAAGLAA22-a"),
    ("Gerade und Ebene: Existenz unendlich vieler Ebenen ohne Punkt mit drei gleichen Koordinaten begründen",
     "Analytische Geometrie", "Lagebeziehungen",
     "Begründen, dass es unendlich viele Ebenen ohne Punkt mit übereinstimmenden Koordinaten gibt: die Punktmenge "
     "als Gerade durch den Ursprung erkennen, echt parallele Ebenen angeben.",
     "2019MerhoehtAAGLAA22-b"),
    ("Einzelwahrscheinlichkeit aus dem Diagramm kumulierter Wahrscheinlichkeiten ermitteln", "Stochastik", "Binomialverteilung",
     "In einem Diagramm kumulierter Wahrscheinlichkeiten P(X ≤ k) den fehlenden letzten Wert 1 eintragen und eine "
     "Einzelwahrscheinlichkeit als Differenz benachbarter kumulierter Werte ablesen.",
     "2019MerhoehtAStochastik11-a"),
    ("Trefferwahrscheinlichkeit aus einer Gleichung zweier Einzelwahrscheinlichkeiten berechnen", "Stochastik", "Binomialverteilung",
     "Bei bekanntem n den Wert von p aus einer vorgegebenen Gleichung zwischen zwei Einzelwahrscheinlichkeiten "
     "berechnen (Bernoulli-Terme, Kürzen, lineare Gleichung).",
     "2019MerhoehtAStochastik11-b"),
    ("Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit einer in fester Reihenfolge vorgegebenen Folge von Ergebnissen als Produkt der "
     "Einzelwahrscheinlichkeiten berechnen.",
     "2019MerhoehtAStochastik12-a"),
    ("Ziehen ohne Zurücklegen: Mögliche Anzahlen nach dem Umlegen zweier Kugeln angeben", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Alle möglichen Anzahlen einer Farbe in einer Urne angeben, nachdem eine Kugel in eine andere Urne und eine "
     "von dort zurückgelegt wurde (Fälle nach den Farben der umgelegten Kugeln).",
     "2019MerhoehtAStochastik2-a"),
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
