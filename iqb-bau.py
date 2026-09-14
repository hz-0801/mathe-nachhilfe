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
    "stapel": "2020-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2020MerhoehtAAnalysis11": 5,
        "2020MerhoehtAAnalysis12": 5,
        "2020MerhoehtAAnalysis13": 5,
        "2020MerhoehtAAnalysis21": 5,
        "2020MerhoehtAAnalysis22": 5,
        "2020MerhoehtAAGLAA11": 5,
        "2020MerhoehtAAGLAA12": 5,
        "2020MerhoehtAAGLAA211": 5,
        "2020MerhoehtAAGLAA212": 5,
        "2020MerhoehtAAGLAA22": 5,
        "2020MerhoehtAStochastik11": 5,
        "2020MerhoehtAStochastik12": 5,
        "2020MerhoehtAStochastik13": 5,
        "2020MerhoehtAStochastik21": 5,
        "2020MerhoehtAStochastik22": 5,
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
# niveau_geschaetzt nach der Deutungsliste v0.7 (Nullfall-Regel); bei III nennt bemerkung den Eintrag.

# ---- Analysis 1.1: Dreiecke unter x · e^(−x)
XEX_SKIZZE = ("Koordinatensystem ohne Skalen; Graph von x · e^(−x): von links unten steil steigend durch den "
              "Ursprung, Hochpunkt bei etwa (1; 0,37), dann flach gegen die x-Achse abfallend")
row("2020MerhoehtAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen", typ_neben="",
    stichwoerter="Dreieck O(0; 0), P(a; 0), Q(a; f(a))|rechter Winkel bei P|1/2 · a · f(a) = 1/2 · a · a · e^(−a) = 1/2 a² e^(−a)",
    voraussetzungen="Grundseite a, Höhe f(a)|Flächenformel",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=XEX_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = x · e^(−x) in IR; Dreiecke mit O(0; 0), P(a; 0), Q(a; f(a)), a > 0",
    gesucht="Begründung, dass der Flächeninhalt 1/2 a² e^(−a) beträgt",
    verfahren="Grundseite und Höhe einsetzen",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="1/2 · a · f(a) = 1/2 · a · a · e^(−a) = 1/2 a² e^(−a) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Höhe als a statt f(a) nehmen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Extremalprobleme.")

row("2020MerhoehtAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Parameter für den größten Flächeninhalt über die Ableitung bestimmen", typ_neben="",
    stichwoerter="A(a) = 1/2 a² e^(−a)|A'(a) = a e^(−a) − 1/2 a² e^(−a) = 1/2 a e^(−a) · (2 − a)|A'(a) = 0 ⇔ a = 2 (a > 0)",
    voraussetzungen="Zielfunktion aus a|Produktregel|Nullstelle der Ableitung, Vorzeichenwechsel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=XEX_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Flächeninhalt A(a) = 1/2 a² e^(−a) aus a; unter den Dreiecken hat eines den größten Inhalt",
    gesucht="zugehöriger Wert von a",
    verfahren="A ableiten, Nullstelle mit a > 0",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2020MerhoehtAAnalysis11-a",
    ergebnis="betrachtet man 1/2 a² e^(−a) als Term einer Funktion A, so gilt für a > 0: A'(a) = a e^(−a) − 1/2 a² e^(−a) = 1/2 a e^(−a) · (2 − a) = 0 ⇔ a = 2 (amtlich)",
    zwischenergebnis="A(2) = 2/e² ≈ 0,27",
    niveau_geschaetzt="II",
    fehlerquelle="Kettenregel bei e^(−a) vergessen (Vorzeichen)",
    bemerkung="Standardbezug: K1 I, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Die Zielfunktion ist in a vorgegeben, nach dem Prinzip keine Deutung.")

# ---- Analysis 1.2: sin x und x
row("2020MerhoehtAAnalysis12", "a", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen bis zu einer vorgegebenen Grenze berechnen", typ_neben="",
    stichwoerter="g(x) = x über f(x) = sin x auf [0; π]|Integral von 0 bis π über (x − sin x) dx|[1/2 x² + cos x] von 0 bis π = π²/2 − 2",
    voraussetzungen="Differenzfunktion|Stammfunktion von sin|Grenzen 0 (gemeinsamer Punkt) und π",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = sin x, g(x) = x in IR; einziger gemeinsamer Punkt O(0; 0) mit gleicher Steigung; Gerade x = π",
    gesucht="Inhalt der Fläche zwischen den Graphen von f und g und der Geraden x = π",
    verfahren="Integral der Differenz von 0 bis π",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Integral von 0 bis π über (g(x) − f(x)) dx = [1/2 x² + cos x] von 0 bis π = 1/2 π² − 2 (amtlich)",
    zwischenergebnis="≈ 2,93",
    niveau_geschaetzt="II",
    fehlerquelle="cos π = 1 statt −1 einsetzen",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

row("2020MerhoehtAAnalysis12", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente mit vorgegebener Steigung außerhalb eines Punktes angeben", typ_neben="",
    stichwoerter="parallel zu g: Steigung 1|cos x = 1 ⇔ x = 2kπ|x = 2π: Tangente y = x − 2π (nicht durch O)",
    voraussetzungen="Parallelität als gleiche Steigung|Stellen mit f'(x) = 1|Tangentengleichung",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = sin x, g(x) = x; gesuchte Tangente parallel zu g und nicht durch O",
    gesucht="Gleichung einer solchen Tangente",
    verfahren="Berührstelle mit cos x = 1 außer 0, z. B. 2π",
    schritte="2", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="y = x − 2π (amtlich)",
    zwischenergebnis="ebenso y = x + 2π",
    niveau_geschaetzt="II",
    fehlerquelle="Tangente bei π (Steigung −1) wählen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Parallele Tangente über die Ableitung finden und skizzieren“ getrennt (andere Handlung, Gleichung angeben).")

# ---- Analysis 1.3: Schar −k(x⁴ − 4x³)
SCHAR_SKIZZE = ("Koordinatensystem ohne Skalen; zwei Graphen der Schar durch den Ursprung und (4; 0), zwischen 0 und 4 "
                "oberhalb der Achse mit Hochpunkt über 3, der durchgezogene höher als der gestrichelte; links und "
                "rechts davon nach unten")
row("2020MerhoehtAAnalysis13", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Hochpunkt einer Schar mit Parameterfaktor bestimmen", typ_neben="",
    stichwoerter="f_k'(x) = −k(4x³ − 12x²) = −4kx² · (x − 3)|Vorzeichenwechsel nur bei 3|Hochpunkt bei x = 3",
    voraussetzungen="Ableitung mit Faktor k|Faktorisieren|nur die Nullstelle mit Vorzeichenwechsel zählt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=SCHAR_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f_k(x) = −k · (x⁴ − 4x³) mit k > 0; Nullstellen 0 und 4",
    gesucht="x-Koordinate des Hochpunkts von f_k",
    verfahren="Ableitung faktorisieren, Vorzeichenwechsel",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_k'(x) = −k · (4x³ − 12x²) = −4kx² · (x − 3); da f_k' nur bei x = 3 sein Vorzeichen ändert, hat der Hochpunkt die x-Koordinate 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="x = 0 als Extremstelle angeben (Sattelpunkt)",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MerhoehtAAnalysis13", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameterunabhängigkeit der Fläche zwischen zwei Scharkurven nachweisen", typ_neben="",
    stichwoerter="f_{k+1}(x) − f_k(x) = −(x⁴ − 4x³)|Schnittstellen 0 und 4 für alle k|Differenz und Grenzen ohne k, also Inhalt ohne k",
    voraussetzungen="Differenz zweier Scharterme|Schnittstellen der Schar|Fläche als Integral der Differenz",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SCHAR_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f_k und f_{k+1} mit gemeinsamen Nullstellen 0 und 4",
    gesucht="Nachweis, dass das von beiden Graphen eingeschlossene Flächenstück für alle k denselben Inhalt hat",
    verfahren="Differenz bilden, k fällt heraus",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_{k+1}(x) − f_k(x) = −(k + 1) · (x⁴ − 4x³) + k · (x⁴ − 4x³) = −(x⁴ − 4x³); da sowohl die x-Koordinaten der Schnittpunkte als auch die Differenz unabhängig von k sind, gilt dies auch für den Inhalt des Flächenstücks (amtlich)",
    zwischenergebnis="Inhalt 256/5",
    niveau_geschaetzt="II",
    fehlerquelle="das Integral mit k ausrechnen wollen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Nachrechnen mit mitgeführtem Parameter (k fällt heraus), nach dem Prinzip II.")

# ---- Analysis 2.1: Stammfunktionen der Schar a(x − 2)³
row("2020MerhoehtAAnalysis21", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion durch Ableiten nachweisen", typ_neben="",
    stichwoerter="F(x) = 1/2 (x − 2)⁴ + 3|F'(x) = 2 · (x − 2)³ = f_2(x)",
    voraussetzungen="Kettenregel|F' = f",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = a · (x − 2)³ für a ≠ 0; F(x) = 1/2 · (x − 2)⁴ + 3",
    gesucht="Nachweis, dass F Stammfunktion von f_2 ist",
    verfahren="F ableiten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="F'(x) = 2 · (x − 2)³ = f_2(x) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="f_2 integrieren wollen statt F abzuleiten",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MerhoehtAAnalysis21", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Vorzeichen der Stammfunktionen einer Schar durch Fallunterscheidung untersuchen", typ_neben="",
    stichwoerter="Stammfunktionen F_(a,b)(x) = a/4 · (x − 2)⁴ + b|a > 0: nach oben geöffnet, Minimum b, für b < 0 Nullstellen, nie nur negativ|a < 0: nach unten geöffnet, Maximum b < 0 möglich|nur für a < 0",
    voraussetzungen="allgemeine Stammfunktion mit Konstante|Form der Graphen nach dem Vorzeichen von a|Skizzen beider Fälle",
    format="Begründung|Zeichnen", operator="Untersuchen Sie", antwort="Text|Grafik",
    material="keins", skizze="zu zeichnen: zwei Graphen, I nach oben geöffnete Kurve mit Tiefpunkt bei x = 2 oberhalb der Achse, II nach unten geöffnete Kurve mit Hochpunkt bei x = 2 unterhalb der Achse",
    kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = a · (x − 2)³, a ≠ 0",
    gesucht="Untersuchung mit Skizzen, für welche a es Stammfunktionen von f_a mit nur negativen Werten gibt",
    verfahren="Stammfunktionen mit Parameter b aufstellen, nach dem Vorzeichen von a unterscheiden und skizzieren",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="die Terme aller Stammfunktionen von f_a lassen sich durch F_(a,b)(x) = a/4 · (x − 2)⁴ + b mit reellem b darstellen; für a > 0 hat F_(a,b) stets Funktionswerte, die nicht negativ sind (Graph I), für a < 0 gibt es stets Werte von b, sodass F_(a,b) nur negative Funktionswerte hat (Graph II); der Erwartungshorizont zeigt beide Skizzen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Integrationskonstante vergessen und nur F_(a,0) betrachten",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt. Eichregel: Fallunterscheidung a > 0 / a < 0 mit verschiedenem Ausgang (Grundregel, kein Nullfall) und (e) Beziehung Funktion–Stammfunktion in der Skizze.")

# ---- Analysis 2.2: Verkettung aus zwei Graphen (ungegliedert)
GG_SKIZZE = ("Koordinatensystem mit Gitter (Schrittweite 1), x-Achse von −4 bis 6,5, y-Achse von −3,5 bis 4,5; oberer "
             "Graph von g: von links oben fallend, Tiefpunkt (−2; 1), steigend zum Hochpunkt etwa (3; 4), dann "
             "fallend durch (6; 0); unterer Graph von f: von links fallend, Tiefpunkt etwa (−2; −2,3), Hochpunkt "
             "etwa (2,5; −1,7), fallend durch (4; −2)")
row("2020MerhoehtAAnalysis22", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Tangente an eine Verkettung aus zwei abgebildeten Graphen über die Kettenregel bestimmen", typ_neben="",
    stichwoerter="h = g ∘ f|h'(4) = g'(f(4)) · f'(4)|f(4) = −2 aus der Abbildung|g'(−2) = 0 (Tiefpunkt von g), also h'(4) = 0|h(4) = g(−2) = 1|Tangente y = 1",
    voraussetzungen="Kettenregel|Werte am Graphen ablesen|Extrempunkt als Nullstelle der Ableitung|waagerechte Tangente",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Koordinatensystem", skizze=GG_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graphen der ganzrationalen Funktionen f und g in der Abbildung; f(4) = −2, g hat den Tiefpunkt (−2; 1); h(x) = g(f(x))",
    gesucht="Gleichung der Tangente an den Graphen von h in (4; h(4))",
    verfahren="Kettenregel an der Stelle 4, g'(−2) = 0 am Tiefpunkt erkennen, h(4) ablesen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="h'(4) = g'(f(4)) · f'(4) = g'(−2) · f'(4) = 0 · f'(4) = 0; mit h(4) = g(f(4)) = g(−2) = 1 ergibt sich für die gesuchte Gleichung y = 1 (amtlich)",
    zwischenergebnis="f'(4) wird nicht benötigt",
    niveau_geschaetzt="III",
    fehlerquelle="f'(4) am Graphen schätzen und mit einer geschätzten Steigung von g rechnen",
    bemerkung="Standardbezug: K2 III, K4 II, K5 II. Amtlich, Werte aus der Abbildung. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Eichregel: (b) Sonderfall erkennen – f(4) trifft den Tiefpunkt von g, g'(−2) = 0 – verkettet mit der Kettenregel am Graphen.")

# ---- AG/LA (A1) 1: Apfelplantage
APFEL_SKIZZE = ("Übergangsdiagramm mit drei Knoten J (oben), M (links unten), G (rechts unten): Schleifen J 0,7, M s; "
                "Pfeile J→M 0,3, M→J 0,2, G→J 0,1, G→M 0,9, M→G r")
row("2020MerhoehtAAGLAA11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="0,9: 90 % der guttragenden Bäume tragen im nächsten Jahr mäßig|0,1: 10 % der guttragenden Bäume werden durch Jungbäume ersetzt",
    voraussetzungen="Pfeile als Übergänge je Jahr lesen",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Diagramm", skizze=APFEL_SKIZZE, kontext="Apfelplantage", textumfang="mittel",
    gegeben="Jungbäume J, mäßigtragende M, guttragende G; Übergangsdiagramm je Jahr in der Abbildung",
    gesucht="Bedeutung der Zahlen 0,1 und 0,9 im Sachzusammenhang",
    verfahren="Pfeile von G lesen",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="90 % der guttragenden Bäume tragen im folgenden Jahr mäßig, 10 % werden ersetzt (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Pfeilrichtung vertauschen (90 % der mäßigtragenden werden guttragend)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. Amtlich. Typ aus 2022-ea-A wiederverwendet (dort Matrixeintrag, hier Diagrammzahl – dieselbe Fertigkeit). Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2020MerhoehtAAGLAA11", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen", typ_neben="",
    stichwoerter="A = ((0,7; 0,2; 0,1), (0,3; s; 0,9), (0; r; 0))|A · (k; 300; 180) = (k; 300; 180)|I 0,7k + 60 + 18 = k gibt k = 260|II 0,3k + 300s + 162 = 300 gibt s = 0,2|III 300r = 180 gibt r = 0,6",
    voraussetzungen="Übergangsmatrix aus dem Diagramm|stationärer Vektor als Gleichungssystem|nacheinander lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=APFEL_SKIZZE, kontext="Apfelplantage", textumfang="lang",
    gegeben="v_(n+1) = A · v_n mit (J; M; G); Zusammensetzung mit k Jungbäumen, 300 mäßigtragenden und 180 guttragenden Bäumen bleibt unverändert",
    gesucht="Werte von r, s und k",
    verfahren="Matrix aufstellen, A · v = v zeilenweise lösen",
    schritte="4", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="aus ((0,7; 0,2; 0,1), (0,3; s; 0,9), (0; r; 0)) · (k; 300; 180) = (k; 300; 180) resultiert I 0,7k + 60 + 18 = k, II 0,3k + 300s + 162 = 300, III 300r = 180; aus I ergibt sich k = 260, damit aus II s = 0,2 und aus III r = 0,6 (amtlich)",
    zwischenergebnis="Spaltensummen 1 bestätigt: 0,2 + s + r = 1",
    niveau_geschaetzt="II",
    fehlerquelle="Zeilen und Spalten der Matrix vertauschen",
    bemerkung="Standardbezug: K2 II, K3 II, K4 I, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A1) 2: spaltenstochastische Matrix (ungegliedert)
row("2020MerhoehtAAGLAA12", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Erhalt der Spaltensumme unter einer stochastischen Matrix allgemein nachweisen", typ_neben="",
    stichwoerter="M = ((a; b), (c; d)) mit a + c = 1, b + d = 1, Einträge ≥ 0|M² = ((a² + bc; ab + bd), (ac + cd; bc + d²))|Einträge nicht negativ|Spaltensumme a(a + c) + c(b + d) = a + c = 1, ebenso b + d = 1",
    voraussetzungen="Definition in Bedingungen übersetzen|M² allgemein|Spaltensummen geschickt faktorisieren",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="spaltenstochastisch: Einträge ≥ 0, jede Spaltensumme 1; M = ((a; b), (c; d)) spaltenstochastisch",
    gesucht="Nachweis, dass M² spaltenstochastisch ist",
    verfahren="M² berechnen, Nichtnegativität und Spaltensummen mit a + c = 1, b + d = 1 zeigen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="M² = ((a² + bc; ab + bd), (ac + cd; bc + d²)); mit a, b, c und d sind auch die Einträge von M² nicht negativ; a² + bc + ac + cd = a · (a + c) + c · (b + d) = a + c = 1 und ab + bd + bc + d² = b · (a + c) + d · (b + d) = b + d = 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Spaltensummen ausmultipliziert stehen lassen, ohne a + c = 1 einzusetzen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2). Typ aus 2022-ea-A wiederverwendet (dort N · u, hier M²; die Fertigkeit – Spaltensumme über a + c = 1 und b + d = 1 erhalten – ist dieselbe). Eichregel: (a) Definition in Gleichungen übersetzen und (c) allgemeiner Nachweis mit Parametern.")

# ---- AG/LA (A2) 1.1: Zylinder
row("2020MerhoehtAAGLAA211", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Punkt auf dem Rand der Grundfläche eines Zylinders nachweisen", typ_neben="",
    stichwoerter="Grundfläche in der x1x2-Ebene, Mittelpunkt N(8; 5; 0) unter M(8; 5; 10)|P(5; 1; 0) in der Ebene|NP = (−3; −4; 0), Länge 5 = Radius",
    voraussetzungen="Mittelpunkt der Grundfläche aus M und Höhe|Abstand vom Mittelpunkt gleich Radius",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="gerader Zylinder, Radius 5, Höhe 10, Grundfläche in der x1x2-Ebene, M(8; 5; 10) Mittelpunkt der Deckfläche; P(5; 1; 0)",
    gesucht="Nachweis, dass P auf dem Rand der Grundfläche liegt",
    verfahren="P in der Grundflächenebene, Abstand zu N gleich 5",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="P liegt in der x1x2-Ebene; der Mittelpunkt der Grundfläche ist N(8; 5; 0); es gilt |NP| = |(−3; −4; 0)| = √((−3)² + (−4)²) = 5 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Abstand zu M statt zu N berechnen",
    bemerkung="Standardbezug: K1 I, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MerhoehtAAGLAA211", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Nächsten und fernsten Punkt des Deckflächenrands eines Zylinders zu einem Randpunkt der Grundfläche bestimmen", typ_neben="",
    stichwoerter="kleinster Abstand: S senkrecht über P, S(5; 1; 10)|größter Abstand: T diametral gegenüber, OT = OM + SM = (11; 9; 10)",
    voraussetzungen="Punkt senkrecht über P auf dem Deckflächenrand|Gegenpunkt über den Mittelpunkt",
    format="Rechnung", operator="Geben Sie an|Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Zylinder wie in a; S nächster, T fernster Punkt des Deckflächenrands zu P",
    gesucht="Koordinaten von S und T",
    verfahren="S = P + (0; 0; 10), T = M + SM",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2020MerhoehtAAGLAA211-a",
    ergebnis="S(5; 1; 10); OT = OM + SM = (8; 5; 10) + (3; 4; 0) = (11; 9; 10), d. h. T(11; 9; 10) (amtlich)",
    zwischenergebnis="|PS| = 10, |PT| = √200",
    niveau_geschaetzt="II",
    fehlerquelle="T = M + MS statt M + SM (Vorzeichen)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Lage von S und T ist am Zylinder unmittelbar einsichtig (senkrecht darüber, gegenüber), nach dem Prinzip II.")

# ---- AG/LA (A2) 1.2: Theaterkulisse, Schatten (ungegliedert)
KULISSE_SKIZZE = ("Schrägbild eines Quaders (Kulisse) mit x-Achse nach vorn links (0 bis 5), y-Achse nach rechts (0 bis 7), "
                  "z-Achse nach oben (0 bis 5); Quader über der Bühne 0 ≤ x ≤ 4, 0 ≤ y ≤ 7, 0 ≤ z ≤ 3 mit grauen Wänden "
                  "bei y = 0 und y = 7; Lampe L als Punkt links oben mit gestrichelter Senkrechten zur Bühne")
row("2020MerhoehtAAGLAA212", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Schattenpunkt auf einer Wand als Schnitt von Lichtstrahl und Ebene untersuchen", typ_neben="",
    stichwoerter="rechte Wand: y = 7|Lichtstrahl OL + t · LS = (4; 0; 5) + t · (−3; 6; −3)|y = 7 bei t = 7/6: Punkt (0,5; 7; 1,5)|0 < 0,5 < 4 und 0 < 1,5 < 3: auf der Wand",
    voraussetzungen="Wand als Ebene y = 7|Lichtstrahl als Gerade durch L und S|Schnittpunkt und Lage im Rechteck prüfen",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Körper", skizze=KULISSE_SKIZZE, kontext="Theaterkulisse/Schatten", textumfang="lang",
    gegeben="Kulisse 7 m breit, linke Wand in der xz-Ebene, rechte Wand parallel dazu (y = 7), Höhe 3, Tiefe 4; Lampe L(4; 0; 5), Spitze S(1; 6; 2)",
    gesucht="rechnerische Untersuchung, ob der Schatten der Spitze auf der rechten Wand liegt",
    verfahren="Gerade LS mit y = 7 schneiden, Koordinaten gegen die Wandmaße prüfen",
    schritte="3", zahlenraum="Bruch|dezimal|negativ", einheiten="m", abhaengig_von="",
    ergebnis="alle Punkte der rechten Seitenwand haben die y-Koordinate 7; OL + 7/6 · LS = (4; 0; 5) + 7/6 · (−3; 6; −3) = (0,5; 7; 1,5); da 0 < 0,5 < 4 und 0 < 1,5 < 3 gilt, liegt der Schatten auf der rechten Seitenwand (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur den Schnittpunkt berechnen, ohne die Wandmaße zu prüfen",
    bemerkung="Standardbezug: K1 I, K2 II, K3 I, K4 I, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 1.2). Schatten als Schnitt von Gerade und Ebene ist die Standardmodellierung, nach dem Prinzip keine Deutung.")

# ---- AG/LA (A2) 2: Pyramidenschar und Ebene
PYR_SKIZZE = ("Schrägbild der Pyramide für t = 6: quadratische Grundfläche A(0; 0; 0), B6, C6, D6 in der xy-Ebene, "
              "Spitze S6 flach darüber (z = 0,75); Achsen x nach vorn links, y nach rechts, z nach oben")
row("2020MerhoehtAAGLAA22", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Parallelität einer Ebene zu einer Koordinatenachse über die Koordinatengleichung begründen", typ_neben="",
    stichwoerter="E: 3y + 4z = 24|x kommt nicht vor|E parallel zur x-Achse",
    voraussetzungen="fehlende Variable als Parallelität zur Achse",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=PYR_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="E: 3y + 4z = 24",
    gesucht="Begründung, dass E parallel zur x-Achse verläuft",
    verfahren="Gleichung ohne x deuten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Gleichung von E liefert nur eine Bedingung für die y- und die z-Koordinate der Punkte der Ebene (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="„enthält die x-Achse“ behaupten (Ursprung liegt nicht in E)",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MerhoehtAAGLAA22", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Parameterwerte für gemeinsame Punkte einer Pyramidenschar mit einer Ebene untersuchen", typ_neben="",
    stichwoerter="E schneidet die xy-Ebene in y = 8|D_t(0; t; 0) liegt für t = 8 auf E|t > 8: A und D_t auf verschiedenen Seiten von E|t < 8: alle Eckpunkte auf derselben Seite (S_t unter E)|gemeinsame Punkte genau für t ≥ 8",
    voraussetzungen="Spurgerade der Ebene in der Grundebene|Lage von Punkten relativ zur Ebene über die Gleichung|Fallunterscheidung nach t|Konvexität der Pyramide",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Körper", skizze=PYR_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Pyramiden A B_t C_t D_t S_t mit A(0; 0; 0), B_t(t; 0; 0), C_t(t; t; 0), D_t(0; t; 0), S_t mit z = t/8; E: 3y + 4z = 24, enthält S_12",
    gesucht="Werte von t, für die Pyramide und E gemeinsame Punkte haben",
    verfahren="Spurgerade y = 8 in der Grundfläche, Lage von D_t und der übrigen Ecken zu E nach t unterscheiden",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="E schneidet die xy-Ebene in der Geraden y = 8; für t = 8 liegt D_t auf dieser Geraden, für t > 8 befinden sich A und D_t auf verschiedenen Seiten von E und für t < 8 liegen alle Eckpunkte der Pyramide auf derselben Seite von E; folglich haben Pyramide und E genau dann gemeinsame Punkte, wenn t ≥ 8 gilt (amtlich)",
    zwischenergebnis="S_t: 3 · t/2 + 4 · t/8 = 2t < 24 für t < 12, also S_t erst ab t = 12 auf oder über E",
    niveau_geschaetzt="III",
    fehlerquelle="nur die Spitze S_t prüfen (t ≥ 12) und die Grundfläche vergessen",
    bemerkung="Standardbezug: K1 II, K2 III, K6 III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) die Spurgerade y = 8 als entscheidende Lage erkennen, Fallunterscheidung t < 8, t = 8, t > 8 mit verschiedenem Ausgang (Grundregel).")

# ---- Stochastik 1.1: Binomialverteilung n = 40
BIN_SKIZZE = ("Säulendiagramm P(X = k) ohne Achsenwerte, Säulen etwa von k = 15 bis 35 mit Maximum bei 26; die Säulen "
              "bis einschließlich 26 grau markiert, die rechten weiß; drei gestrichelte waagerechte Hilfslinien")
row("2020MerhoehtAStochastik11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben", typ_neben="",
    stichwoerter="n = 40, p = 0,65|P(X = 30) = (40 über 30) · 0,65³⁰ · 0,35¹⁰",
    voraussetzungen="Bernoulli-Formel",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X binomialverteilt mit n = 40 und p = 0,65",
    gesucht="Term für P(X = 30)",
    verfahren="Formel einsetzen",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="(40 über 30) · 0,65³⁰ · 0,35¹⁰ (amtlich)",
    zwischenergebnis="≈ 0,057",
    niveau_geschaetzt="I",
    fehlerquelle="Exponenten vertauschen",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet.")

row("2020MerhoehtAStochastik11", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Obere Grenze einer im Diagramm markierten kumulierten Wahrscheinlichkeit über den Erwartungswert ermitteln", typ_neben="",
    stichwoerter="graue Säulen bis zur höchsten Säule|Maximum beim Erwartungswert 40 · 0,65 = 26|k = 26",
    voraussetzungen="höchste Säule beim Erwartungswert (ganzzahlig)|kumulierte Wahrscheinlichkeit als Säulen bis k",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=BIN_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Diagramm der Verteilung von X ohne Achsenwerte; die grauen Säulen stellen P(X ≤ k) dar und enden bei der höchsten Säule",
    gesucht="Wert von k",
    verfahren="Erwartungswert berechnen, mit der höchsten Säule identifizieren",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="der Erwartungswert von X ist 40 · 0,65 = 26; die Verteilung nimmt ihr einziges Maximum für k = 26 an; der Abbildung ist zu entnehmen, dass dieser Wert mit dem gesuchten übereinstimmt (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Säulen abzählen wollen (keine Achsenwerte)",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MerhoehtAStochastik11", "c", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Bedingung an p für das Verhältnis zweier symmetrisch liegender Einzelwahrscheinlichkeiten angeben", typ_neben="",
    stichwoerter="n = 40, 10 und 30 symmetrisch zu 20|P(Y = 10) > P(Y = 30) genau dann, wenn die Verteilung nach links verschoben ist|p < 0,5",
    voraussetzungen="Symmetrie der Binomialverteilung bei p = 0,5|Verschiebung des Maximums mit p",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Y binomialverteilt mit n = 40 und p_Y, 0 < p_Y < 1",
    gesucht="alle p_Y mit P(Y = 10) > P(Y = 30)",
    verfahren="Lage von 10 und 30 zur Mitte 20 mit p vergleichen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="p_Y < 0,5 (amtlich)",
    zwischenergebnis="Gleichheit bei p = 0,5",
    niveau_geschaetzt="II",
    fehlerquelle="p > 0,5 angeben",
    bemerkung="Standardbezug: K1 II, K2 II. Amtlich, eigene Rechnung bestätigt (Vorzeichen der Differenz für p = 1/4, 1/2, 3/4).")

# ---- Stochastik 1.2: Tetraeder und Würfel
row("2020MerhoehtAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für mindestens einmal über das Gegenereignis im Baumdiagramm nachweisen", typ_neben="",
    stichwoerter="keine 3: erster Wurf Tetraeder nicht 3 (3/4), dann Würfel nicht 3 (5/6)|1 − 3/4 · 5/6 = 3/8",
    voraussetzungen="zweistufiges Experiment mit Weiche|Gegenereignis",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksspiel", textumfang="lang",
    gegeben="Tetraeder 1 bis 4, Würfel 1 bis 6; Tetraeder einmal werfen; bei 3 nochmals Tetraeder, sonst Würfel",
    gesucht="Nachweis, dass P(mindestens einmal 3) = 3/8",
    verfahren="Gegenereignis über den einzigen Pfad ohne 3",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1 − 3/4 · 5/6 = 3/8 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="beide Zweige mit 1/4 ansetzen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MerhoehtAStochastik12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="Auszahlung nur bei genau einer 3: 3/8 − 1/4 · 1/4 = 5/16|5/16 · x = 5 Euro|x = 16 Euro",
    voraussetzungen="genau einmal aus mindestens einmal minus zweimal|Erwartungswert gleich Einsatz",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel", textumfang="mittel",
    gegeben="Einsatz 5 Euro; Auszahlung nur bei genau einer 3 in den beiden Würfen; P(mindestens eine 3) = 3/8; Ausgleich von Einsätzen und Auszahlungen",
    gesucht="Höhe der Auszahlung",
    verfahren="P(genau eine 3) = 3/8 − P(zweimal 3), Erwartungswert gleich 5",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="Euro", abhaengig_von="2020MerhoehtAStochastik12-a",
    ergebnis="(3/8 − 1/4 · 1/4) · x = 5/16 · x = 5 € ⇔ x = 16 € (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="mit 3/8 statt 5/16 rechnen (zweimal 3 nicht abziehen)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zusammengezogener Typ). Ausgleichsbedingung wörtlich, nach dem Prinzip II.")

# ---- Stochastik 1.3: Würfelnetz 1, 2, 2, 2, 2, 3
row("2020MerhoehtAStochastik13", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit einer vorgegebenen Augensumme bei zwei Würfen über Pfade berechnen", typ_neben="",
    stichwoerter="Würfel mit 1, 2, 2, 2, 2, 3|Summe 4: (1; 3), (3; 1), (2; 2)|2 · 1/6 · 1/6 + 4/6 · 4/6 = 1/2",
    voraussetzungen="Wahrscheinlichkeiten aus dem Netz|Pfade zur Summe 4",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze="Würfelnetz in Kreuzform: obere und untere Fläche 2, mittlere Reihe 1, 2, 2, 3",
    kontext="Würfel", textumfang="kurz",
    gegeben="Würfelnetz mit den Zahlen 1, 2, 2, 2, 2, 3; zweimal geworfen",
    gesucht="P(Summe 4)",
    verfahren="Pfade summieren",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="2 · 1/6 · 1/6 + 4/6 · 4/6 = 1/2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Pfad (2; 2) vergessen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt (alle 36 Paare).")

row("2020MerhoehtAStochastik13", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="neue Zahlen x und 3x statt 1 und 3|E = 1/6 · x + 4/6 · 2 + 1/6 · 3x = 4|4/6 x = 8/3, x = 4|Zahlen 4 und 12",
    voraussetzungen="Erwartungswert mit Unbekannten|Verhältnis 1 : 3 als 3x",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Skizze", skizze="Würfelnetz in Kreuzform: obere und untere Fläche 2, mittlere Reihe 1, 2, 2, 3",
    kontext="Würfel", textumfang="mittel",
    gegeben="1 und 3 werden durch neue Zahlen im Verhältnis 1 : 3 ersetzt; Erwartungswert der geworfenen Zahl 4",
    gesucht="die beiden neuen Zahlen",
    verfahren="E(X) = 4 mit x und 3x lösen",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="",
    ergebnis="1/6 · x + 4/6 · 2 + 1/6 · 3x = 4 ⇔ 4/6 x = 8/3 ⇔ x = 4; die neuen Zahlen sind 4 und 12 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die vier Zweien als eine Zahl mit 1/6 gewichten",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zusammengezogener Typ).")

# ---- Stochastik 2.1: Urne mit 100 Kugeln
row("2020MerhoehtAStochastik21", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="100 Kugeln, 20 weiß, ohne Zurücklegen|20/100 · 19/99|beide Kugeln weiß",
    voraussetzungen="Pfad ohne Zurücklegen lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Urne mit 100 Kugeln, 20 weiß; zwei Kugeln nacheinander ohne Zurücklegen; Term 20/100 · 19/99",
    gesucht="ein Ereignis mit dieser Wahrscheinlichkeit",
    verfahren="Faktoren als zwei Züge deuten",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="beide gezogenen Kugeln sind weiß (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="„genau eine weiße“ angeben",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. Amtlich. Typ wiederverwendet (zusammengezogener Typ).")

row("2020MerhoehtAStochastik21", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Kugelzahl aus dem Vergleich der zweiten Zugwahrscheinlichkeit mit und ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="erste Kugel weiß|ohne Zurücklegen: P(zweite weiß) = (w − 1)/99 = p|mit Zurücklegen: w/100 = 1,02 · p|w/100 = 1,02 · (w − 1)/99 ⇔ 99w = 102w − 102 ⇔ w = 34",
    voraussetzungen="bedingte Wahrscheinlichkeit des zweiten Zugs in beiden Fällen|„2 % von p größer“ als Faktor 1,02|Bruchgleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="lang",
    gegeben="andere Urne mit 100 Kugeln, w weiße (1 < w < 99); erste gezogene Kugel weiß; P(zweite weiß) ohne Zurücklegen p, mit Zurücklegen um 2 % von p größer",
    gesucht="Wert von w",
    verfahren="beide Wahrscheinlichkeiten in w aufstellen, Gleichung mit Faktor 1,02 lösen",
    schritte="3", zahlenraum="Bruch|dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="w/100 = 1,02 · (w − 1)/99 ⇔ 99w = 102w − 102 ⇔ w = 34 (amtlich)",
    zwischenergebnis="p = 33/99 = 1/3, mit Zurücklegen 0,34",
    niveau_geschaetzt="III",
    fehlerquelle="„2 % größer“ als + 0,02 statt Faktor 1,02 ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die beiden Fälle in Terme in w und „2 % von p größer“ in den Faktor 1,02 übersetzen, verkettet zur Gleichung.")

# ---- Stochastik 2.2: Tulpensträuße
row("2020MerhoehtAStochastik22", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Faktoren eines kombinatorischen Terms im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="(3 über 2): zwei der drei Farben auswählen|14: Anzahl der Tulpen der ersten Farbe von 1 bis 14, Rest die zweite Farbe",
    voraussetzungen="Binomialkoeffizient als Auswahl|Aufteilung von 15 auf zwei Farben mit je mindestens einer",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Gärtnerei/Tulpensträuße", textumfang="mittel",
    gegeben="Sträuße mit 15 Tulpen in Gelb, Orange, Rot; Strauß mit genau zwei Farben; Term (3 über 2) · 14",
    gesucht="Bedeutung beider Faktoren im Sachzusammenhang",
    verfahren="Auswahl der Farben und Aufteilung der Anzahl deuten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der erste Faktor gibt die Anzahl der Möglichkeiten an, zwei der drei Farben auszuwählen, der zweite die Anzahl der Möglichkeiten für die Anzahl der Tulpen einer der beiden Farben (amtlich)",
    zwischenergebnis="42 Möglichkeiten",
    niveau_geschaetzt="II",
    fehlerquelle="14 als Anzahl der übrigen Tulpen deuten",
    bemerkung="Standardbezug: K3 II, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MerhoehtAStochastik22", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl der Zusammensetzungen mit Mengenbedingungen je Sorte bestimmen", typ_neben="",
    stichwoerter="je Farbe 4 bis 6 Tulpen, Summe 15|Zusammensetzungen 5 + 5 + 5 und 4 + 5 + 6|Zerlegung 4, 5, 6 in 3 · 2 = 6 Zuordnungen|insgesamt 7",
    voraussetzungen="Zerlegungen von 15 unter den Schranken finden|Anordnungen der Farben zählen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Gärtnerei/Tulpensträuße", textumfang="kurz",
    gegeben="Strauß mit 15 Tulpen; je Farbe mindestens vier und höchstens sechs",
    gesucht="Anzahl der Möglichkeiten, den Strauß zusammenzustellen",
    verfahren="Zerlegungen von 15 in drei Zahlen aus {4, 5, 6} und ihre Farbzuordnungen zählen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="es gibt eine Möglichkeit, den Strauß aus jeweils fünf Tulpen der drei Farben, und 3 · 2 Möglichkeiten, den Strauß aus vier Tulpen einer ersten, fünf Tulpen einer zweiten und sechs Tulpen der dritten Farbe zusammenzustellen – insgesamt also sieben Möglichkeiten (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="3! = 6 für die Zerlegung 4, 5, 6 vergessen oder 3³ = 27 zählen",
    bemerkung="Standardbezug: K2 III, K3 II. Amtlich, eigene Rechnung bestätigt (Aufzählung). Eichregel: (a) die Schranken in die zulässigen Zerlegungen von 15 übersetzen und mit dem Zählen der Farbzuordnungen verketten.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen", "Analysis", "Extremalprobleme",
     "Den Term für den Flächeninhalt eines Dreiecks mit einer Ecke auf dem Graphen aus Grundseite und Höhe "
     "in Abhängigkeit vom Parameter begründen.",
     "2020MerhoehtAAnalysis11-a"),
    ("Parameter für den größten Flächeninhalt über die Ableitung bestimmen", "Analysis", "Extremalprobleme",
     "Den Parameterwert bestimmen, für den eine vorgegebene Flächeninhaltsfunktion maximal wird (Ableitung, "
     "Nullstelle mit Einschränkung des Parameters).",
     "2020MerhoehtAAnalysis11-b"),
    ("Fläche: Fläche zwischen zwei Graphen bis zu einer vorgegebenen Grenze berechnen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Inhalt der Fläche zwischen zwei Graphen von ihrem Schnittpunkt bis zu einer vorgegebenen senkrechten "
     "Geraden als Integral der Differenz berechnen.",
     "2020MerhoehtAAnalysis12-a"),
    ("Tangente mit vorgegebener Steigung außerhalb eines Punktes angeben", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Eine Tangente mit vorgegebener Steigung angeben, deren Berührpunkt nicht ein genannter Punkt ist "
     "(Stellen mit f' gleich Steigung, Tangentengleichung).",
     "2020MerhoehtAAnalysis12-b"),
    ("Hochpunkt einer Schar mit Parameterfaktor bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die x-Koordinate des Hochpunkts einer Schar bestimmen, deren Parameter ein Vorfaktor ist (Ableitung "
     "faktorisieren, Vorzeichenwechsel).",
     "2020MerhoehtAAnalysis13-a"),
    ("Parameterunabhängigkeit der Fläche zwischen zwei Scharkurven nachweisen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Zeigen, dass die von zwei benachbarten Scharkurven eingeschlossene Fläche nicht vom Parameter abhängt "
     "(Differenz und Schnittstellen ohne Parameter).",
     "2020MerhoehtAAnalysis13-b"),
    ("Stammfunktion durch Ableiten nachweisen", "Analysis", "Stammfunktion und Hauptsatz",
     "Zeigen, dass eine vorgegebene Funktion Stammfunktion ist, indem ihre Ableitung gebildet wird.",
     "2020MerhoehtAAnalysis21-a"),
    ("Vorzeichen der Stammfunktionen einer Schar durch Fallunterscheidung untersuchen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Mit Skizzen untersuchen, für welche Parameterwerte es Stammfunktionen mit nur negativen (oder nur "
     "positiven) Werten gibt: allgemeine Stammfunktion mit Konstante, Fallunterscheidung nach dem Vorzeichen.",
     "2020MerhoehtAAnalysis21-b"),
    ("Tangente an eine Verkettung aus zwei abgebildeten Graphen über die Kettenregel bestimmen", "Analysis",
     "Ableitungsregeln",
     "Die Tangente an den Graphen einer Verkettung g(f(x)) an einer Stelle bestimmen, wenn nur die Graphen "
     "von f und g abgebildet sind (Kettenregel mit abgelesenen Werten, Extremstelle als Nullstelle der Ableitung).",
     "2020MerhoehtAAnalysis22"),
    ("Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus der Bedingung A · v = v mit unbekannten Matrixeinträgen und einer unbekannten Komponente von v "
     "alle Unbekannten über das Gleichungssystem bestimmen.",
     "2020MerhoehtAAGLAA11-b"),
    ("Körper: Punkt auf dem Rand der Grundfläche eines Zylinders nachweisen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Nachweisen, dass ein Punkt auf dem Rand der Grundfläche eines Zylinders liegt: in der Grundebene und "
     "im Abstand des Radius vom Mittelpunkt.",
     "2020MerhoehtAAGLAA211-a"),
    ("Nächsten und fernsten Punkt des Deckflächenrands eines Zylinders zu einem Randpunkt der Grundfläche bestimmen",
     "Analytische Geometrie", "Abstände",
     "Zu einem Punkt auf dem Grundflächenrand eines geraden Zylinders den nächsten (senkrecht darüber) und den "
     "fernsten (diametral gegenüber) Punkt des Deckflächenrands bestimmen.",
     "2020MerhoehtAAGLAA211-b"),
    ("Gerade und Ebene: Schattenpunkt auf einer Wand als Schnitt von Lichtstrahl und Ebene untersuchen",
     "Analytische Geometrie", "Lagebeziehungen",
     "Den Schatten eines Punktes bei einer Punktlichtquelle als Schnittpunkt der Geraden Lichtquelle–Punkt "
     "mit einer Wandebene berechnen und prüfen, ob er innerhalb der Wandmaße liegt.",
     "2020MerhoehtAAGLAA212"),
    ("Parallelität einer Ebene zu einer Koordinatenachse über die Koordinatengleichung begründen",
     "Analytische Geometrie", "Ebenen",
     "Begründen, dass eine Ebene parallel zu einer Koordinatenachse ist, weil die zugehörige Variable in der "
     "Koordinatengleichung nicht vorkommt.",
     "2020MerhoehtAAGLAA22-a"),
    ("Punkt und Ebene: Parameterwerte für gemeinsame Punkte einer Pyramidenschar mit einer Ebene untersuchen",
     "Analytische Geometrie", "Lagebeziehungen",
     "Untersuchen, für welche Parameterwerte eine Pyramide mit parameterabhängigen Ecken eine feste Ebene "
     "trifft: Spurgerade in der Grundebene, Lage der Ecken zur Ebene, Fallunterscheidung.",
     "2020MerhoehtAAGLAA22-b"),
    ("Obere Grenze einer im Diagramm markierten kumulierten Wahrscheinlichkeit über den Erwartungswert ermitteln",
     "Stochastik", "Binomialverteilung",
     "Den Wert k ermitteln, bis zu dem Säulen einer Binomialverteilung ohne Achsenwerte markiert sind, wenn "
     "die Markierung an der höchsten Säule endet (Erwartungswert n · p).",
     "2020MerhoehtAStochastik11-b"),
    ("Bedingung an p für das Verhältnis zweier symmetrisch liegender Einzelwahrscheinlichkeiten angeben",
     "Stochastik", "Binomialverteilung",
     "Angeben, für welche p eine Einzelwahrscheinlichkeit größer ist als die zu n/2 symmetrisch liegende "
     "(Symmetrie bei p = 0,5, Verschiebung des Maximums).",
     "2020MerhoehtAStochastik11-c"),
    ("Wahrscheinlichkeit für mindestens einmal über das Gegenereignis im Baumdiagramm nachweisen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit für mindestens ein Auftreten in einem zweistufigen Experiment mit Weiche über den "
     "einzigen Pfad ohne Treffer nachweisen.",
     "2020MerhoehtAStochastik12-a"),
    ("Wahrscheinlichkeit einer vorgegebenen Augensumme bei zwei Würfen über Pfade berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit einer bestimmten Augensumme bei zwei Würfen eines unregelmäßig beschrifteten "
     "Würfels über die passenden Pfade berechnen.",
     "2020MerhoehtAStochastik13-a"),
    ("Ziehen ohne Zurücklegen: Kugelzahl aus dem Vergleich der zweiten Zugwahrscheinlichkeit mit und ohne Zurücklegen berechnen",
     "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Die Kugelzahl bestimmen, wenn das Verhältnis der Wahrscheinlichkeiten für den zweiten Zug mit und ohne "
     "Zurücklegen vorgegeben ist (Terme in w, Bruchgleichung).",
     "2020MerhoehtAStochastik21-b"),
    ("Faktoren eines kombinatorischen Terms im Sachzusammenhang deuten", "Stochastik", "Kombinatorik",
     "Die Faktoren eines Anzahlterms (Binomialkoeffizient, Anzahl der Aufteilungen) im Sachzusammenhang deuten.",
     "2020MerhoehtAStochastik22-a"),
    ("Anzahl der Zusammensetzungen mit Mengenbedingungen je Sorte bestimmen", "Stochastik", "Kombinatorik",
     "Die Anzahl der Möglichkeiten bestimmen, eine feste Gesamtzahl auf Sorten mit Unter- und Obergrenzen "
     "aufzuteilen: zulässige Zerlegungen finden, Zuordnungen zählen.",
     "2020MerhoehtAStochastik22-b"),
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
