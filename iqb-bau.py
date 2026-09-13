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
    "stapel": "2023-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2023MgrundlegendAAnalysis11": 5,
        "2023MgrundlegendAAnalysis12": 5,
        "2023MgrundlegendAAnalysis13": 5,
        "2023MgrundlegendAAnalysis2": 5,
        "2023MgrundlegendAAGLAA111": 5,
        "2023MgrundlegendAAGLAA112": 5,
        "2023MgrundlegendAAGLAA12": 5,
        "2023MgrundlegendAAGLAA212": 5,
        "2023MgrundlegendAAGLAA213": 5,
        "2023MgrundlegendAAGLAA22": 5,
        "2023MgrundlegendAStochastik11": 5,
        "2023MgrundlegendAStochastik12": 5,
        "2023MgrundlegendAStochastik2": 5,
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
# niveau_geschaetzt nach der Deutungsliste v0.6 (Prinzip, (a)–(e)); bei III nennt bemerkung
# den Eintrag. Typnamen mit Gegenstandsklasse nach iqb.md § 6 (Entscheidung 24).

# ---- Analysis 1.1: lineare Funktion, Abstand des Ursprungs
LIN_SKIZZE = ("Koordinatensystem mit x-Achse von −11 bis 3 (Markierungen in Zweierschritten) und y-Achse "
              "von 0 bis 6, kein Gitter; Gerade durch (−10; 0) und (0; 5), steigend bis über (2; 6)")
row("2023MgrundlegendAAnalysis11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Geradengleichung aus der Abbildung begründen", typ_neben="",
    stichwoerter="Nullstelle −10, y-Achsenabschnitt 5|Steigung 5/10 = 1/2|f(x) = 1/2 x + 5",
    voraussetzungen="Steigung aus zwei Achsenschnittpunkten|Geradengleichung y = mx + n",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=LIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph einer in IR definierten linearen Funktion f in der Abbildung",
    gesucht="Begründung, dass f(x) = 1/2 x + 5 gilt",
    verfahren="Achsenschnittpunkte (−10; 0) und (0; 5) ablesen, daraus Steigung und Achsenabschnitt",
    schritte="1", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="der Graph ist eine Gerade mit der Steigung 5/10, die die y-Achse im Punkt (0; 5) schneidet (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Steigung als 10/5 = 2 ablesen",
    bemerkung="Standardbezug: K1 I, K4 I. Amtlich, eigene Rechnung bestätigt. Werte nur aus der Abbildung.")

row("2023MgrundlegendAAnalysis11", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Abstand des Ursprungs zu einer Geraden über das Lot berechnen", typ_neben="",
    stichwoerter="Lot vom Ursprung: y = −2x (Steigung −1/m)|Schnitt 1/2 x + 5 = −2x, x = −2|Lotfußpunkt (−2; 4)|Abstand √(2² + 4²) = √20",
    voraussetzungen="Normale mit Steigung −1/m|Schnittpunkt zweier Geraden|Abstand zweier Punkte",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=LIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/2 x + 5, Graph in der Abbildung",
    gesucht="Abstand des Koordinatenursprungs zum Graphen",
    verfahren="Lotgerade durch den Ursprung mit Steigung −2 aufstellen, mit dem Graphen schneiden, Abstand des Lotfußpunkts zum Ursprung",
    schritte="3", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="2023MgrundlegendAAnalysis11-a",
    ergebnis="Gleichung des Lots vom Ursprung auf den Graphen: y = −2x; 1/2 x + 5 = −2x ⇔ 2,5x = −5 ⇔ x = −2, f(−2) = 4; Abstand √(2² + 4²) = √20 (amtlich)",
    zwischenergebnis="√20 ≈ 4,47",
    niveau_geschaetzt="II",
    fehlerquelle="den Abstand zum y-Achsenabschnitt (5) oder zur Nullstelle (10) nehmen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Routinekette Normale, Schnittpunkt, Abstand.")

# ---- Analysis 1.2: symmetrische Tangenten
row("2023MgrundlegendAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente am gespiegelten Punkt über die Achsensymmetrie angeben", typ_neben="",
    stichwoerter="Graph symmetrisch zur y-Achse|t1: y = 4/3 x + 4 in (1; f(1))|t2 in (−1; f(−1)): y = −4/3 x + 4|Spiegelung von t1 an der y-Achse",
    voraussetzungen="Achsensymmetrie auf Tangenten übertragen|Spiegelung einer Geraden an der y-Achse (Vorzeichen der Steigung)",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktion f mit zur y-Achse symmetrischem Graphen; Tangente t1 im Punkt (1; f(1)) hat die Gleichung y = 4/3 x + 4",
    gesucht="Gleichung der Tangente t2 im Punkt (−1; f(−1)) mit Begründung",
    verfahren="t2 ist das Spiegelbild von t1 an der y-Achse: Steigung wechselt das Vorzeichen, Achsenabschnitt bleibt",
    schritte="1", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="y = −4/3 x + 4; aufgrund der Symmetrie des Graphen von f liegen t1 und t2 symmetrisch bezüglich der y-Achse (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="auch den Achsenabschnitt spiegeln (y = −4/3 x − 4)",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt. Die Symmetrie ist im Text vorgegeben, (b) feuert nach dem Prinzip nicht.")

row("2023MgrundlegendAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Umfang des Dreiecks aus zwei Tangenten und der x-Achse berechnen", typ_neben="",
    stichwoerter="t1 schneidet die Achsen in (−3; 0) und (0; 4)|Dreieck mit Ecken (−3; 0), (3; 0), (0; 4)|Schenkel √(3² + 4²) = 5|Umfang 2 · 3 + 2 · 5 = 16",
    voraussetzungen="Nullstelle und Achsenabschnitt einer Geraden|Satz des Pythagoras|Symmetrie des Dreiecks",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="t1: y = 4/3 x + 4 und t2: y = −4/3 x + 4 schließen mit der x-Achse ein Dreieck ein",
    gesucht="Umfang des Dreiecks",
    verfahren="Schnittpunkte von t1 mit den Achsen, Schenkellänge mit Pythagoras, Grundseite 6",
    schritte="3", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="2023MgrundlegendAAnalysis12-a",
    ergebnis="t1 schneidet die Koordinatenachsen in (−3; 0) und (0; 4); Umfang des Dreiecks 2 · 3 + 2 · √(3² + 4²) = 16 (amtlich)",
    zwischenergebnis="Schenkel 5",
    niveau_geschaetzt="II",
    fehlerquelle="die Höhe 4 als Schenkel nehmen (Umfang 14)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 1.3: x⁴ − 4x³, Integral und Achsenskalierung
QUART_SKIZZE = ("Koordinatensystem ohne Skalen, x- und y-Achse beschriftet; Graph von f(x) = x⁴ − 4x³: von links "
                "oben steil fallend durch den Ursprung, Tiefpunkt rechts unten bei x = 3 (weit unterhalb der Achse), "
                "Nullstelle bei 4, dann steil steigend; die Abbildung ist in y-Richtung stark gestaucht")
row("2023MgrundlegendAAnalysis13", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Bestimmtes Integral einer ganzrationalen Funktion berechnen", typ_neben="",
    stichwoerter="Stammfunktion 1/5 x⁵ − x⁴|Grenzen 0 und 1|Wert −4/5",
    voraussetzungen="Potenzregel der Integration|Grenzen einsetzen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=QUART_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x⁴ − 4x³, definiert in IR, Graph in der Abbildung; Integral von 0 bis 1 über f(x) dx",
    gesucht="Wert des Integrals",
    verfahren="Stammfunktion bilden und Grenzen einsetzen",
    schritte="2", zahlenraum="Bruch|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Integral von 0 bis 1 über f(x) dx = [1/5 x⁵ − x⁴] von 0 bis 1 = −4/5 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="4x³ zu 4/4 x⁴ = x⁴ mit falschem Vorzeichen integrieren",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet.")

row("2023MgrundlegendAAnalysis13", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Aussage über die Achsenskalierung einer Abbildung beurteilen", typ_neben="",
    stichwoerter="Nullstellen 0 und 4|f(3) = −27|Punkt (3; −27) liegt in der Abbildung nicht neunmal so weit von der x-Achse wie von der y-Achse|Aussage falsch",
    voraussetzungen="Nullstellen durch Ausklammern|Funktionswert berechnen|Verhältnis von Koordinaten mit der Abbildung vergleichen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=QUART_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x⁴ − 4x³ mit Graph in der Abbildung ohne Skalen; Aussage: eine Längeneinheit auf der x-Achse ist ebenso groß gewählt wie auf der y-Achse",
    gesucht="Beurteilung, ob die Aussage richtig ist",
    verfahren="einen Punkt mit bekannten Koordinaten (etwa (3; −27) oder die Nullstelle 4) mit den Abständen in der Abbildung vergleichen",
    schritte="2", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="die Aussage ist falsch; f hat die Nullstellen 0 und 4, der Punkt mit der x-Koordinate 3 hat die y-Koordinate −27, liegt aber nicht neunmal so weit von der x-Achse entfernt wie von der y-Achse (amtlich)",
    zwischenergebnis="f(x) = x³ (x − 4)",
    niveau_geschaetzt="II",
    fehlerquelle="aus dem Fehlen von Skalen keine Prüfung ableiten",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Beurteilung durch Vergleich eines Funktionswerts mit der Abbildung, kein Eintrag der Deutungsliste.")

# ---- Analysis 2: e^(x²) (Gruppe 2, einzige Datei, aufgabe „2“)
row("2023MgrundlegendAAnalysis2", "a", seite="1", punkte="2", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Wertemenge einer verketteten e-Funktion angeben", typ_neben="",
    stichwoerter="f(x) = e^(x²)|x² ≥ 0|e^(x²) ≥ e^0 = 1|Wertemenge [1; ∞[",
    voraussetzungen="Wertemenge von x²|Monotonie der e-Funktion|Intervallschreibweise",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = e^(x²), definiert in IR",
    gesucht="Wertemenge von f",
    verfahren="x² nimmt alle Werte ab 0 an, die e-Funktion ist streng monoton steigend, also alle Werte ab e^0 = 1",
    schritte="1", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="[1; +∞[ (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="]0; ∞[ wie bei e^x angeben",
    bemerkung="Standardbezug: K1 III, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt. Einzige Datei der Gruppe 2 (aufgabe „2“). Eichregel: kein Eintrag; als Verkettung zweier Wertemengen II geschätzt, amtlich III über K1.")

row("2023MgrundlegendAAnalysis2", "b", seite="1", punkte="3", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Steigung im Schnittpunkt von Graph und Ableitungsgraph bestimmen", typ_neben="",
    stichwoerter="f'(x) = 2x · f(x)|Schnitt: f(x) = 2x · f(x)|f(x) > 0, kürzen: 2x = 1|x = 1/2|f'(1/2) = e^(1/4)",
    voraussetzungen="Schnittpunkt als Gleichung f = f'|durch f(x) ≠ 0 kürzen|Ableitungswert als Steigung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = e^(x²); f'(x) = 2x · f(x); die Graphen von f und f' schneiden sich in genau einem Punkt",
    gesucht="Steigung des Graphen von f in diesem Punkt",
    verfahren="f(x) = 2x · f(x) durch f(x) > 0 teilen, x = 1/2, dann f'(1/2)",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2023MgrundlegendAAnalysis2-a",
    ergebnis="f(x) = 2x · f(x) ⇔ x = 1/2; f'(1/2) = e^(1/4) (amtlich)",
    zwischenergebnis="f(1/2) = e^(1/4) ebenfalls (Schnittpunkt)",
    niveau_geschaetzt="III",
    fehlerquelle="die Gleichung ausmultiplizieren statt durch f(x) zu kürzen",
    bemerkung="Standardbezug: K2 III, K4 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Schnittbedingung in die Gleichung f = 2x · f übersetzen und (b) Sonderfall f > 0 zum Kürzen erkennen.")

# ---- AG/LA (A1) 1.1: Gleichungssystem (Sachgebiet nur „AG/LA“, Dublette 2023MgrundlegendAAGLAA211)
row("2023MgrundlegendAAGLAA111", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Eindeutigkeit der Lösung eines Gleichungssystems durch Einsetzen und Vergleich begründen", typ_neben="",
    stichwoerter="I 3x − y = 4, II −3x − 15y = 12|x = 1, y = −1 einsetzen|Gleichungen nicht äquivalent|keine weitere Lösung",
    voraussetzungen="Werte einsetzen|zwei Gleichungen als nicht proportional erkennen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Gleichungssystem I 3x − y = 4, II −3x − 15y = 12 mit reellen x, y",
    gesucht="Begründung, dass es nur die Lösung x = 1 und y = −1 hat",
    verfahren="Lösung in beide Gleichungen einsetzen; da die Gleichungen nicht äquivalent sind, gibt es keine weitere",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="es gilt 3 · 1 − (−1) = 4 und −3 · 1 − 15 · (−1) = 12; da die beiden Gleichungen nicht äquivalent sind, hat das Gleichungssystem keine weitere Lösung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="nur einsetzen und die Eindeutigkeit nicht begründen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Die Kurzbeschreibung nennt nur AG/LA; die Datei liegt wortgleich als 2023MgrundlegendAAGLAA211 ein zweites Mal vor (Dublette ohne Zeile).")

row("2023MgrundlegendAAGLAA111", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lösungsanzahl eines erweiterten Gleichungssystems in Abhängigkeit vom Parameter angeben", typ_neben="",
    stichwoerter="III −2x + y = t|Lösung (1; −1) einsetzen: −2 − 1 = −3|t = −3: genau eine Lösung|sonst keine",
    voraussetzungen="eindeutige Lösung von I und II in III einsetzen|Fallunterscheidung nach t",
    format="Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="I und II mit der einzigen Lösung (1; −1), erweitert um III −2x + y = t mit reellem t",
    gesucht="Anzahl der Lösungen des erweiterten Systems in Abhängigkeit von t, mit Begründung",
    verfahren="die einzige Lösung von I und II in III einsetzen: III ist genau für t = −3 erfüllt",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2023MgrundlegendAAGLAA111-a",
    ergebnis="es gilt −2 · 1 + (−1) = −3; damit hat das erweiterte Gleichungssystem für t = −3 genau eine Lösung und für alle anderen Werte von t keine Lösung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="für t = −3 unendlich viele Lösungen erwarten",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A1) 1.2: Matrix mit Nullzeile
row("2023MgrundlegendAAGLAA112", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Unlösbarkeit einer Matrix-Vektor-Gleichung über eine Nullzeile begründen", typ_neben="",
    stichwoerter="M = ((1; 0; −3), (0; 1; −2), (0; 0; 0))|dritte Zeile null|dritte Komponente von M · u stets 0|kein u mit M · u = (3; 2; 1)",
    voraussetzungen="Zeile der Matrix als Komponente des Produkts lesen",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="M = ((1; 0; −3), (0; 1; −2), (0; 0; 0))",
    gesucht="Entscheidung mit Begründung, ob es einen Vektor u mit M · u = (3; 2; 1) gibt",
    verfahren="dritte Zeile von M betrachten",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="aufgrund der dritten Zeile von M ist die dritte Komponente eines Vektors M · u stets null; damit gibt es keinen Vektor u mit der angegebenen Eigenschaft (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="ein Gleichungssystem aufstellen und sich in den ersten beiden Zeilen verlieren",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2023MgrundlegendAAGLAA112", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Kollinearität von M · x − x mit einem Vektor untersuchen", typ_neben="",
    stichwoerter="v = M · (a; b; c) − (a; b; c) = (−3c; −2c; −c)|v = −c · (3; 2; 1) = −c · w|kollinear für alle a, b und c ≠ 0",
    voraussetzungen="Matrix-Vektor-Produkt mit Variablen|Vektorsubtraktion|Kollinearität als Vielfaches",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="M = ((1; 0; −3), (0; 1; −2), (0; 0; 0)); v = M · (a; b; c) − (a; b; c) mit c ≠ 0; w = (3; 2; 1)",
    gesucht="für welche reellen a, b, c die Vektoren v und w kollinear sind",
    verfahren="v ausrechnen; es bleibt −c · w",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="v = (a − 3c; b − 2c; 0) − (a; b; c) = (−3c; −2c; −c) = −c · w; damit sind v und w kollinear für alle reellen a, b und alle c ≠ 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Bedingungen an a und b suchen, obwohl sie herausfallen",
    bemerkung="Standardbezug: K2 I, K5 II. Amtlich, eigene Rechnung bestätigt. Identität mit mitgeführten Parametern, nach dem Prinzip II.")

# ---- AG/LA (A1) 2: Eigenvektoren einer 2×2-Matrix (ungegliedert)
row("2023MgrundlegendAAGLAA12", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Alle Vektoren mit M · v = t · v durch Fallunterscheidung bestimmen", typ_neben="",
    stichwoerter="M = ((2; 0), (3; 1))|(2a; 3a + b) = t · (a; b)|I 2a = ta, II 3a + b = tb|a = 0: t = 1, Vektoren (0; b)|a ≠ 0: t = 2, b = 3a, Vektoren (a; 3a)",
    voraussetzungen="Matrix-Vektor-Produkt|Gleichungssystem mit Parameter t|Fallunterscheidung a = 0 und a ≠ 0",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="M = ((2; 0), (3; 1)); gesucht sind alle Vektoren (a; b) ≠ (0; 0), für die ein reelles t mit M · (a; b) = t · (a; b) existiert",
    gesucht="alle diese Vektoren",
    verfahren="Produkt gleichsetzen; aus I 2a = ta folgt a = 0 oder t = 2; beide Fälle in II einsetzen",
    schritte="4", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="M · (a; b) = (2a; 3a + b) = t · (a; b) liefert I 2a = t · a, II 3a + b = t · b; für a = 0 ist I für alle t erfüllt, II nur für t = 1, also genau die Vektoren (0; b) mit b ≠ 0; für a ≠ 0 ist I nur für t = 2 erfüllt und II nur für 3a = b, also genau die Vektoren (a; 3a) (amtlich)",
    zwischenergebnis="Eigenwerte 1 und 2",
    niveau_geschaetzt="III",
    fehlerquelle="I durch a teilen, ohne a = 0 zu betrachten, und die Vektoren (0; b) verlieren",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2). Eichregel: Fallunterscheidung (Grundregel).")

# ---- AG/LA (A2) 1.2: zwei Geraden, gemeinsamer Punkt
row("2023MgrundlegendAAGLAA212", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punktprobe an einer Geraden durchführen", typ_neben="",
    stichwoerter="g: x = (2; 3; −7) + s · (1; 0; 5)|zweite Koordinate aller Punkte von g ist 3|A(4; 0; 0) hat 0",
    voraussetzungen="Koordinate mit Richtungskomponente 0 als konstant erkennen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (2; 3; −7) + s · (1; 0; 5), s reell; A(4; 0; 0)",
    gesucht="Begründung, dass A nicht auf g liegt",
    verfahren="zweite Koordinate vergleichen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="alle Punkte von g haben die x2-Koordinate 3, A hat die x2-Koordinate 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="aus der ersten Koordinate s = 2 folgern und nicht weiterprüfen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. Amtlich. Typ aus 2025-ga-A wiederverwendet (hier über die konstante Koordinate).")

row("2023MgrundlegendAAGLAA212", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Parameter aus dem Schnitt zweier Geraden ermitteln", typ_neben="",
    stichwoerter="h durch A(4; 0; 0) und B(5; 1; b): x = (4; 0; 0) + r · (1; 1; b)|Gleichsetzen: 2 + s = 4 + r, 3 = r, −7 + 5s = rb|r = 3, s = 5|18 = 3b, b = 6",
    voraussetzungen="Geradengleichung aus zwei Punkten|Gleichsetzen und koordinatenweise lösen|Parameter aus der dritten Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (2; 3; −7) + s · (1; 0; 5); h durch A(4; 0; 0) und B(5; 1; b) mit reellem b; g und h haben einen gemeinsamen Punkt",
    gesucht="Wert von b",
    verfahren="h aufstellen, mit g gleichsetzen; die zweite Koordinate liefert r, die erste s, die dritte b",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2023MgrundlegendAAGLAA212-a",
    ergebnis="(2; 3; −7) + s · (1; 0; 5) = (4; 0; 0) + r · (1; 1; b) liefert r = 3, s = 5 und damit 18 = 3b ⇔ b = 6 (amtlich)",
    zwischenergebnis="gemeinsamer Punkt (7; 3; 18)",
    niveau_geschaetzt="II",
    fehlerquelle="für h denselben Parameter s wie für g verwenden",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Schnittmengen im grundlegenden Niveau.")

# ---- AG/LA (A2) 1.3: Standseilbahn
row("2023MgrundlegendAAGLAA213", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Parametergleichung einer Strecke im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="x = (−13; 9; 4) + λ · (−20; 60; 30) mit λ in [0; 1]|Stützpunkt A, Richtung AE|Streckenabschnitt der Seilbahn",
    voraussetzungen="Parameterbereich [0; 1] als Strecke deuten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Foto", skizze="Foto einer Standseilbahn auf geradliniger Strecke am Hang, ohne Maße", kontext="Standseilbahn", textumfang="mittel",
    gegeben="Abschnitt einer Standseilbahn von A(−13; 9; 4) bis E(−33; 69; 34), Talstation im Ursprung, x1x2-Ebene horizontal, 1 LE = 10 m; Gleichung x = (−13; 9; 4) + λ · (−20; 60; 30) mit λ in [0; 1]",
    gesucht="Bedeutung der Gleichung im Sachzusammenhang",
    verfahren="Stützpunkt und Richtungsvektor AE mit dem Parameterbereich als Strecke lesen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="m", abhaengig_von="",
    ergebnis="die Gleichung stellt den beschriebenen Streckenabschnitt dar (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Gleichung als die ganze Gerade deuten",
    bemerkung="Standardbezug: K5 I, K6 I. Amtlich. Das Foto zeigt nur die Bahn, keine Werte.")

row("2023MgrundlegendAAGLAA213", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Höhe eines Punktes auf einer Strecke aus der Entfernung vom Anfang berechnen", typ_neben="",
    stichwoerter="|AE| = √(20² + 60² + 30²) = 70 (700 m)|140 m = 14 LE, Anteil 14/70|x3 = 4 + 14/70 · 30 = 10|Höhe 100 m",
    voraussetzungen="Länge des Richtungsvektors|Meter in Längeneinheiten umrechnen|Parameter als Anteil der Strecke|x3 als Höhe deuten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Foto", skizze="Foto einer Standseilbahn auf geradliniger Strecke am Hang, ohne Maße", kontext="Standseilbahn", textumfang="mittel",
    gegeben="Strecke von A(−13; 9; 4) nach E(−33; 69; 34), 1 LE = 10 m, Talstation im Ursprung, x1x2-Ebene horizontal; die Bahn ist 140 m vom Anfang A entfernt",
    gesucht="Höhe der Seilbahn über der Talstation an dieser Stelle",
    verfahren="Streckenlänge 70 LE, 140 m sind 14 LE, also λ = 14/70; x3-Koordinate 4 + λ · 30, in Meter umrechnen",
    schritte="3", zahlenraum="ganz|Wurzel|Bruch", einheiten="m", abhaengig_von="2023MgrundlegendAAGLAA213-a",
    ergebnis="|AE| = √(20² + 60² + 30²) = 70; 4 + 14/70 · 30 = 10, d. h. die gesuchte Höhe beträgt 100 Meter (amtlich)",
    zwischenergebnis="λ = 0,2",
    niveau_geschaetzt="II",
    fehlerquelle="140 direkt als λ oder als Längeneinheiten einsetzen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 2: Dreieck und Pyramide mit Parameter
PYR_SKIZZE = ("Schrägbild mit Koordinatenachsen x (nach vorn links), y (nach rechts), z (nach oben); Dreieck mit "
              "A(5; 0; 0) auf der x-Achse, B(0; 3; 0) auf der y-Achse, C(0; 0; 4) auf der z-Achse; Kanten zum "
              "Ursprung angedeutet")
row("2023MgrundlegendAAGLAA22", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen", typ_neben="",
    stichwoerter="12x + 20y + tz = 60|C(0; 0; 4) einsetzen|4t = 60|t = 15",
    voraussetzungen="Punkt in die Koordinatengleichung einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=PYR_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Dreieck ABC mit A(5; 0; 0), B(0; 3; 0), C(0; 0; 4) in der Abbildung; seine Ebene hat eine Gleichung der Form 12x + 20y + tz = 60",
    gesucht="Wert von t",
    verfahren="C einsetzen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="da C in der Ebene liegt, ergibt sich 4t = 60 ⇔ t = 15 (amtlich)",
    zwischenergebnis="A und B erfüllen die Gleichung: 60 = 60",
    niveau_geschaetzt="I",
    fehlerquelle="A oder B einsetzen, wo t herausfällt",
    bemerkung="Standardbezug: K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ea-A wiederverwendet. Koordinaten der Punkte stehen nur in der Abbildung.")

row("2023MgrundlegendAAGLAA22", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Parameter für das größte Volumen einer Pyramide bestimmen", typ_neben="",
    stichwoerter="A_k(5 − k; 0; 0), B_k(0; 3 + k; 0), C(0; 0; 4)|Volumen 1/3 · 1/2 · (3 + k)(5 − k) · 4|Parabel in k mit Nullstellen −3 und 5|Scheitel in der Mitte: k = 1",
    voraussetzungen="Volumen einer Pyramide mit rechtwinkliger Grundfläche|Term als quadratische Funktion in k deuten|Scheitel aus der Symmetrie der Nullstellen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=PYR_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Pyramide O A_k B_k C mit A_k(5 − k; 0; 0), B_k(0; 3 + k; 0), C(0; 0; 4) für k in ]−3; 5[",
    gesucht="Wert von k, für den das Volumen am größten ist",
    verfahren="Volumen als Term in k aufstellen; er beschreibt eine nach unten geöffnete Parabel mit den Nullstellen −3 und 5, das Maximum liegt in der Mitte",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="das Volumen der Pyramide O A_k B_k C kann mit dem Term 1/3 · 1/2 · (3 + k) · (5 − k) · 4 berechnet werden; als Funktion von k ergibt sich eine Parabel mit Hochpunkt, die bei −3 und 5 die k-Achse schneidet; damit hat die Pyramide für k = 1 das größte Volumen (amtlich)",
    zwischenergebnis="Volumen bei k = 1: 32/3",
    niveau_geschaetzt="III",
    fehlerquelle="das Volumen für einige k ausprobieren statt den Term zu untersuchen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt (Ableitung null bei k = 1). Eichregel: (a) Volumen als Term in k aufstellen und (b) Symmetrie der Parabel ausnutzen.")

# ---- Stochastik 1.1: Erwartungswert und Standardabweichung aus Tabellen
row("2023MgrundlegendAStochastik11", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="Werte 1, 3, 4, x4 mit 1/2, 5/18, 1/6, 1/18|Erwartungswert 3|1/2 + 5/6 + 2/3 + x4/18 = 3|x4 = 18",
    voraussetzungen="Erwartungswert als gewichtete Summe|Bruchgleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle mit den Werten x_i = 1, 3, 4, x4 und P(X = x_i) = 1/2, 5/18, 1/6, 1/18", kontext="ohne", textumfang="kurz",
    gegeben="Wahrscheinlichkeitsverteilung von X: Werte 1, 3, 4, x4 mit Wahrscheinlichkeiten 1/2, 5/18, 1/6, 1/18; Erwartungswert 3",
    gesucht="Wert von x4",
    verfahren="Erwartungswert ansetzen und nach x4 auflösen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/2 + 5/18 · 3 + 1/6 · 4 + 1/18 · x4 = 3 ⇔ 2 + 1/18 · x4 = 3 ⇔ x4 = 18 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="1/2 als 1/2 · 0 statt 1/2 · 1 ansetzen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ nach dem Abgleichlauf wiederverwendet (zusammengezogen aus „Unbekannte Werte einer Zufallsgröße aus dem Erwartungswert bestimmen“ und „Anzahl der Kugeln aus einer Fairnessbedingung bestimmen“).")

row("2023MgrundlegendAStochastik11", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Standardabweichung über einen Summanden der Varianz abschätzen", typ_neben="",
    stichwoerter="Y mit Erwartungswert 5, P(Y = 2) = 1/4 bekannt|Varianz ≥ (2 − 5)² · 1/4 = 9/4|σ ≥ 3/2 > 1",
    voraussetzungen="Varianz als Summe nichtnegativer Summanden|einen Summanden als untere Schranke nutzen|Wurzel ziehen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Tabelle", skizze="Tabelle mit y_i = 2, …, 5, … und P(Y = y_i) = 1/4, …, 3/8, …; übrige Werte fehlen", kontext="ohne", textumfang="kurz",
    gegeben="Teil der Verteilung von Y mit Erwartungswert 5: P(Y = 2) = 1/4, P(Y = 5) = 3/8, weitere Werte unbekannt",
    gesucht="Nachweis, dass die Standardabweichung von Y größer als 1 ist",
    verfahren="der Summand (2 − 5)² · 1/4 der Varianz ist allein schon 9/4 > 1, alle anderen Summanden sind nichtnegativ",
    schritte="2", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="√Var(Y) ≥ √(3² · 1/4) > 1 (amtlich)",
    zwischenergebnis="σ ≥ 1,5",
    niveau_geschaetzt="II",
    fehlerquelle="die Varianz vollständig berechnen wollen, obwohl Werte fehlen",
    bemerkung="Standardbezug: K1 II, K2 I, K5 II. Amtlich, eigene Rechnung bestätigt. Abschätzung über einen Summanden – Sonderfall (b) im Ansatz, aber als einzelner Schritt II geschätzt.")

# ---- Stochastik 1.2: Würfel und Münze
row("2023MgrundlegendAStochastik12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Ergebnisse zur Schnittmenge zweier Ereignisse angeben", typ_neben="",
    stichwoerter="A: gerade Zahl und Wappen|B: Zahl größer als 3|A ∩ B = {(4; W), (6; W)}",
    voraussetzungen="Ergebnisse als Paare (Würfel; Münze)|Schnittmenge zweier Ereignisse",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Würfel und Münze", textumfang="mittel",
    gegeben="Würfel (1 bis 6) und Münze (Zahl, Wappen) je einmal geworfen; A: gerade Zahl und Wappen; B: Zahl größer als 3",
    gesucht="Ergebnisse, die zu A ∩ B gehören",
    verfahren="gerade Zahlen größer als 3 mit Wappen kombinieren",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(4; W), (6; W) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="(4; Z) und (6; Z) mit aufzählen",
    bemerkung="Standardbezug: K1 I, K6 I. Amtlich, eigene Rechnung bestätigt (Abzählen). Nahe am Typ „Ergebnisse zum Gegenereignis zweier Ereignisse aufzählen“ (2026-ga-A) – Vorschlag für den nächsten Abgleich: beide zu „Ergebnisse zu einer Mengenoperation zweier Ereignisse angeben“.")

row("2023MgrundlegendAStochastik12", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="Auszahlung 6 € bei A oder B|A ∪ B = {(2; W), (4; Z), (4; W), (5; Z), (5; W), (6; Z), (6; W)}, 7 von 12 Ergebnissen|Einsätze und Auszahlungen gleichen sich aus|Einsatz 7/12 · 6 € = 3,50 €",
    voraussetzungen="Vereinigung zweier Ereignisse abzählen|Laplace-Wahrscheinlichkeit 7/12|Erwartungswert der Auszahlung gleich Einsatz",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Würfel und Münze", textumfang="lang",
    gegeben="Einsatz, dann Würfel und Münze je einmal; bei A oder B werden 6 € ausgezahlt; auf lange Sicht gleichen sich Einsätze und Auszahlungen aus",
    gesucht="Höhe des Einsatzes",
    verfahren="A ∪ B abzählen (7 von 12 Ergebnissen), Einsatz gleich Erwartungswert der Auszahlung",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="€", abhaengig_von="2023MgrundlegendAStochastik12-a",
    ergebnis="A ∪ B = {(2; W), (4; Z), (4; W), (5; Z), (5; W), (6; Z), (6; W)}; damit beträgt der Einsatz 7/12 · 6 € = 3,50 € (amtlich)",
    zwischenergebnis="P(A ∪ B) = 7/12",
    niveau_geschaetzt="II",
    fehlerquelle="P(A) + P(B) = 3/12 + 6/12 ohne Abzug des Schnitts (Einsatz 4,50 €)",
    bemerkung="Standardbezug: K1 I, K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Die Ausgleichsbedingung ist wörtlich vorgegeben, nach dem Prinzip keine Deutung – II (Liste v0.5/v0.6 ohne „faires Spiel“).")

# ---- Stochastik 2: Tetraeder, Verhältnis der Auszahlungen (ungegliedert, aufgabe „2“)
row("2023MgrundlegendAStochastik2", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Verhältnis zweier Auszahlungen aus dem Ausgleich der Erwartungswerte berechnen", typ_neben="",
    stichwoerter="Tetraeder 1 bis 4, Spieler A und B je ein Wurf|B um mindestens 2 größer: (1; 3), (1; 4), (2; 4) – 3/16|gleiche Zahl 4/16, sonst 9/16|Ausgleich: 3/16 · x = 9/16 · y|x : y = 3 : 1",
    voraussetzungen="16 gleich wahrscheinliche Paare abzählen|drei Fälle mit Zahlungsrichtung unterscheiden|Ausgleich als Gleichheit der erwarteten Zahlungen ansetzen|Verhältnis bilden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Tetraederspiel", textumfang="lang",
    gegeben="Spieler A und B werfen je einmal ein Tetraeder (1 bis 4); ist Bs Zahl um mindestens 2 größer, zahlt A den Betrag x an B; bei gleicher Zahl keine Zahlung; sonst zahlt B den Betrag y an A; auf lange Sicht gleichen sich die Zahlungen aus",
    gesucht="Verhältnis von x und y",
    verfahren="Wahrscheinlichkeiten der drei Fälle abzählen (3/16, 4/16, 9/16), erwartete Zahlung von A gleich erwarteter Zahlung von B setzen",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="(1/4 · 1/2 + 1/4 · 1/4) · x = (1 − (1/4 · 1/2 + 1/4 · 1/4 + 1/4)) · y ⇔ 3/16 · x = 9/16 · y ⇔ x/y = 3/1 (amtlich)",
    zwischenergebnis="günstige Paare für B: (1; 3), (1; 4), (2; 4)",
    niveau_geschaetzt="III",
    fehlerquelle="die Fälle „gleich“ und „B kleiner“ zusammenwerfen (Verhältnis 13 : 3)",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, einzige Datei der Gruppe 2 (aufgabe „2“). Eichregel: (a) die drei Fälle mit Zahlungsrichtung erst finden und den Ausgleich als Gleichung 3/16 · x = 9/16 · y übersetzen – anders als bei „Einsatz gleich Erwartungswert“ ist die Gleichung nicht wörtlich vorgegeben.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Nullstellen und Werte: Geradengleichung aus der Abbildung begründen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Aus Nullstelle und y-Achsenabschnitt einer abgebildeten Geraden die Gleichung der linearen "
     "Funktion begründen.",
     "2023MgrundlegendAAnalysis11-a"),
    ("Abstand des Ursprungs zu einer Geraden über das Lot berechnen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Den Abstand eines Punktes zu einer Geraden in der Ebene berechnen: Lotgerade mit Steigung −1/m, "
     "Lotfußpunkt als Schnittpunkt, Abstand der Punkte.",
     "2023MgrundlegendAAnalysis11-b"),
    ("Tangente am gespiegelten Punkt über die Achsensymmetrie angeben", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Aus einer Tangente an einen achsensymmetrischen Graphen die Tangente am gespiegelten Punkt "
     "angeben und über die Symmetrie begründen.",
     "2023MgrundlegendAAnalysis12-a"),
    ("Umfang des Dreiecks aus zwei Tangenten und der x-Achse berechnen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Aus den Achsenschnittpunkten zweier symmetrischer Geraden das eingeschlossene Dreieck "
     "bestimmen und seinen Umfang mit dem Satz des Pythagoras berechnen.",
     "2023MgrundlegendAAnalysis12-b"),
    ("Nullstellen und Werte: Aussage über die Achsenskalierung einer Abbildung beurteilen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Über berechnete Nullstellen oder Funktionswerte prüfen, ob eine Abbildung ohne Skalen gleiche "
     "Längeneinheiten auf beiden Achsen hat.",
     "2023MgrundlegendAAnalysis13-b"),
    ("Nullstellen und Werte: Wertemenge einer verketteten e-Funktion angeben", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Die Wertemenge einer Verkettung wie e^(x²) aus der Wertemenge der inneren Funktion und der "
     "Monotonie der äußeren angeben.",
     "2023MgrundlegendAAnalysis2-a"),
    ("Steigung im Schnittpunkt von Graph und Ableitungsgraph bestimmen", "Analysis", "Gleichungen lösen",
     "Die Schnittstelle von f und f' über die Gleichung f = f' bestimmen (Kürzen durch f ≠ 0) und "
     "die Steigung dort angeben.",
     "2023MgrundlegendAAnalysis2-b"),
    ("Eindeutigkeit der Lösung eines Gleichungssystems durch Einsetzen und Vergleich begründen",
     "Analytische Geometrie", "Lineare Gleichungssysteme",
     "Eine vorgegebene Lösung durch Einsetzen bestätigen und begründen, dass es keine weitere gibt, "
     "weil die Gleichungen nicht äquivalent sind.",
     "2023MgrundlegendAAGLAA111-a"),
    ("Lösungsanzahl eines erweiterten Gleichungssystems in Abhängigkeit vom Parameter angeben",
     "Analytische Geometrie", "Lineare Gleichungssysteme",
     "Für ein um eine Gleichung mit Parameter erweitertes System angeben, für welchen Parameterwert "
     "die eindeutige Lösung erhalten bleibt und sonst keine existiert.",
     "2023MgrundlegendAAGLAA111-b"),
    ("Matrizenalgebra: Unlösbarkeit einer Matrix-Vektor-Gleichung über eine Nullzeile begründen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Begründen, dass M · u = b keine Lösung hat, weil eine Nullzeile von M die entsprechende "
     "Komponente stets null macht.",
     "2023MgrundlegendAAGLAA112-a"),
    ("Matrizenalgebra: Kollinearität von M · x − x mit einem Vektor untersuchen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "M · x − x mit Variablen berechnen und untersuchen, für welche Werte der Vektor ein Vielfaches "
     "eines gegebenen Vektors ist.",
     "2023MgrundlegendAAGLAA112-b"),
    ("Matrizenalgebra: Alle Vektoren mit M · v = t · v durch Fallunterscheidung bestimmen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Alle Vektoren bestimmen, die eine Matrix auf ein Vielfaches abbildet (Eigenvektoren), über das "
     "Gleichungssystem mit Fallunterscheidung nach einer Komponente.",
     "2023MgrundlegendAAGLAA12"),
    ("Parameter aus dem Schnitt zweier Geraden ermitteln", "Analytische Geometrie", "Schnittmengen",
     "Zwei Geraden gleichsetzen und aus der Bedingung eines gemeinsamen Punktes einen Parameter "
     "in einem Richtungsvektor ermitteln.",
     "2023MgrundlegendAAGLAA212-b"),
    ("Parametergleichung einer Strecke im Sachzusammenhang deuten", "Analytische Geometrie", "Geraden",
     "Eine Geradengleichung mit eingeschränktem Parameterbereich als Strecke zwischen zwei "
     "Sachpunkten deuten.",
     "2023MgrundlegendAAGLAA213-a"),
    ("Höhe eines Punktes auf einer Strecke aus der Entfernung vom Anfang berechnen",
     "Analytische Geometrie", "Geraden",
     "Aus der Länge des Richtungsvektors und einer Entfernung den Parameter als Anteil bestimmen und "
     "eine Koordinate des Punktes im Sachzusammenhang (Höhe, Maßstab) berechnen.",
     "2023MgrundlegendAAGLAA213-b"),
    ("Körper: Parameter für das größte Volumen einer Pyramide bestimmen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Das Volumen einer Pyramide mit parameterabhängigen Ecken als Term aufstellen und den "
     "Parameter mit maximalem Volumen bestimmen (Scheitel einer Parabel).",
     "2023MgrundlegendAAGLAA22-b"),
    ("Standardabweichung über einen Summanden der Varianz abschätzen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Zeigen, dass die Standardabweichung eine Schranke übersteigt, indem ein einzelner Summand der "
     "Varianz als untere Abschätzung benutzt wird.",
     "2023MgrundlegendAStochastik11-b"),
    ("Ergebnisse zur Schnittmenge zweier Ereignisse angeben", "Stochastik", "Ereignisse und Mengenoperationen",
     "Die Ergebnisse eines zweistufigen Experiments aufzählen, die zur Schnittmenge zweier "
     "beschriebener Ereignisse gehören.",
     "2023MgrundlegendAStochastik12-a"),
    ("Verhältnis zweier Auszahlungen aus dem Ausgleich der Erwartungswerte berechnen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Für ein Spiel mit Zahlungen in beide Richtungen die Fallwahrscheinlichkeiten abzählen, die "
     "erwarteten Zahlungen gleichsetzen und das Verhältnis der Beträge berechnen.",
     "2023MgrundlegendAStochastik2"),
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
