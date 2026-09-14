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
    "stapel": "2021-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2021MerhoehtAAnalysis11": 5,
        "2021MerhoehtAAnalysis12": 5,
        "2021MerhoehtAAnalysis13": 5,
        "2021MerhoehtAAnalysis21": 5,
        "2021MerhoehtAAnalysis22": 5,
        "2021MerhoehtAAGLAA111": 5,
        "2021MerhoehtAAGLAA112": 5,
        "2021MerhoehtAAGLAA113": 5,
        "2021MerhoehtAAGLAA121": 5,
        "2021MerhoehtAAGLAA122": 5,
        "2021MerhoehtAAGLAA211": 5,
        "2021MerhoehtAAGLAA213": 5,
        "2021MerhoehtAStochastik11": 5,
        "2021MerhoehtAStochastik12": 5,
        "2021MerhoehtAStochastik13": 5,
        "2021MerhoehtAStochastik21": 5,
        "2021MerhoehtAStochastik22": 5,
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

# ---- Analysis 1.1: sin x mit Tangenten in den Nullstellen
SIN_SKIZZE = ("Koordinatensystem ohne Gitter, x-Achse mit den Markierungen 0 und π; Graph von sin x von etwa −0,5 "
              "bis 3,5 mit dem Bogen über [0; π]; gestrichelte Tangenten in (0; 0) mit Steigung 1 und in (π; 0) "
              "mit Steigung −1, die sich über dem Bogen bei x = π/2 schneiden")
row("2021MerhoehtAAnalysis11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentensteigung an einer Nullstelle über die Ableitung nachweisen", typ_neben="",
    stichwoerter="f(x) = sin x|f'(0) = cos 0 = 1",
    voraussetzungen="Ableitung des Sinus|Tangentensteigung als Ableitungswert",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = sin x in IR; Abbildung mit G_f und den Tangenten in den dargestellten Nullstellen",
    gesucht="Nachweis, dass die Tangente durch den Ursprung die Steigung 1 hat",
    verfahren="f'(0) berechnen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f'(0) = cos(0) = 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="f'(x) = −cos x ansetzen",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2021MerhoehtAAnalysis11", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph und zwei Tangenten berechnen", typ_neben="",
    stichwoerter="Tangenten y = x und y = −(x − π), Schnittpunkt bei π/2|Symmetrie: 2 · Integral von 0 bis π/2 über (x − sin x)|2 · [1/2 x² + cos x] = π²/4 − 2",
    voraussetzungen="Tangentengleichungen in den Nullstellen|Schnittpunkt der Tangenten|Fläche zwischen Gerade und Graph als Integral|Symmetrie oder zwei Integrale",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=SIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = sin x; Tangenten in (0; 0) und (π; 0) aus der Abbildung, Steigung 1 nach a",
    gesucht="Inhalt des Flächenstücks zwischen G_f und den beiden Tangenten",
    verfahren="Tangenten aufstellen, Schnittpunkt bei π/2, Integral der Differenz Tangente minus Sinus über [0; π/2] verdoppeln",
    schritte="4", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2021MerhoehtAAnalysis11-a",
    ergebnis="2 · Integral von 0 bis π/2 über (x − sin x) dx = 2 · [1/2 x² + cos x] von 0 bis π/2 = π²/4 − 2 (amtlich)",
    zwischenergebnis="≈ 0,467; ohne Symmetrie als Summe zweier Integrale gleich",
    niveau_geschaetzt="II",
    fehlerquelle="Integral von 0 bis π über (x − sin x) bilden (zweite Tangente vergessen)",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt. Die Symmetrie ist nur eine Abkürzung, zwei Integrale führen ebenso zum Ziel – nach dem Prinzip keine Deutung nach (b).")

# ---- Analysis 1.2: x⁴ − kx²
row("2021MerhoehtAAnalysis12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung mit Parameter in faktorisierter Form nachweisen", typ_neben="",
    stichwoerter="f(x) = x⁴ − kx²|f'(x) = 4x³ − 2kx = 2x · (2x² − k)",
    voraussetzungen="Potenzregel mit Parameter|Ausklammern",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze="Koordinatensystem ohne Skalen; W-förmiger Graph mit Hochpunkt im Ursprung und zwei Tiefpunkten unterhalb der x-Achse",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x⁴ − k · x² in IR mit k > 0; Graph in der Abbildung",
    gesucht="Nachweis, dass f'(x) = 2x · (2x² − k) gilt",
    verfahren="ableiten und ausklammern",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 4x³ − 2kx = 2x · (2x² − k) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="k beim Ableiten wie eine Variable behandeln",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2021MerhoehtAAnalysis12", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus der y-Koordinate der Tiefpunkte ermitteln", typ_neben="",
    stichwoerter="f'(x) = 0 mit x ≠ 0: x = ±√(k/2)|f(√(k/2)) = k²/4 − k²/2 = −k²/4|−k²/4 = −1 ⇔ k = 2 (k > 0)",
    voraussetzungen="Extremstellen aus der faktorisierten Ableitung|Funktionswert mit Parameter|Gleichung in k mit Vorzeichenbedingung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="Koordinatensystem ohne Skalen; W-förmiger Graph mit Hochpunkt im Ursprung und zwei Tiefpunkten unterhalb der x-Achse",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x⁴ − k · x² mit k > 0; f'(x) = 2x · (2x² − k); beide Tiefpunkte haben die y-Koordinate −1",
    gesucht="Wert von k",
    verfahren="Tiefstellen ±√(k/2) aus f' = 0, Funktionswert gleich −1 setzen",
    schritte="3", zahlenraum="Wurzel|Bruch|negativ", einheiten="", abhaengig_von="2021MerhoehtAAnalysis12-a",
    ergebnis="für x ≠ 0 ergibt sich 2x² − k = 0 ⇔ x = ±√(k/2); für k > 0 gilt f(√(k/2)) = k²/4 − k · k/2 = −k²/4 = −1 ⇔ k = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="k = −2 nicht ausschließen oder x = 0 als Tiefstelle nehmen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 1.3: Computervirus
row("2021MerhoehtAAnalysis13", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen", typ_neben="",
    stichwoerter="f(t) = 2t · e^(−t/100)|Produkt- und Kettenregel|f'(t) = 2e^(−t/100) + 2t · e^(−t/100) · (−1/100) = 2 · (1 − t/100) · e^(−t/100)",
    voraussetzungen="Produktregel|Kettenregel mit innerer Ableitung −1/100|Ausklammern",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Computervirus/Infektionsrate", textumfang="lang",
    gegeben="f(t) = 2 · t · e^(−t/100), t in Tagen, f(t) Rate in Tausend Computern pro Tag",
    gesucht="Nachweis, dass 2 · (1 − t/100) · e^(−t/100) ein Term von f' ist",
    verfahren="Produktregel anwenden und zusammenfassen",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(t) = 2 · e^(−t/100) + 2 · t · e^(−t/100) · (−1/100) = 2 · (1 − t/100) · e^(−t/100) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="innere Ableitung −1/100 vergessen",
    bemerkung="Standardbezug: K5 II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Ableitung mit Parameter in faktorisierter Form nachweisen“ (Analysis 1.2 a) getrennt: dort Potenzregel, hier Produkt- und Kettenregel (anderer Lösungsweg).")

row("2021MerhoehtAAnalysis13", "b", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Zeitpunkt der größten Rate aus der Ableitung angeben", typ_neben="",
    stichwoerter="f'(t) = 0 ⇔ t = 100|Vorzeichenwechsel von + nach −|100 Tage",
    voraussetzungen="Nullstelle des Faktors 1 − t/100|Maximum der Rate",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Computervirus/Infektionsrate", textumfang="kurz",
    gegeben="f'(t) = 2 · (1 − t/100) · e^(−t/100)",
    gesucht="Zeitpunkt der größten Infektionsrate",
    verfahren="Nullstelle von f' ablesen",
    schritte="1", zahlenraum="ganz", einheiten="Tage", abhaengig_von="2021MerhoehtAAnalysis13-a",
    ergebnis="100 Tage nach der ersten Infizierung eines Computers (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="f(100) statt t = 100 angeben",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2021MerhoehtAAnalysis13", "c", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Term für einen Bestand aus einer Rate über ein Integral angeben", typ_neben="",
    stichwoerter="zweite Woche: Tag 7 bis Tag 14|Integral über die Rate|Einheit Tausend Computer: Faktor 1000|1000 · Integral von 7 bis 14 über f(t) dt",
    voraussetzungen="Bestandsänderung als Integral der Rate|Grenzen aus dem Zeitraum|Einheit umrechnen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Computervirus/Infektionsrate", textumfang="mittel",
    gegeben="f(t) Rate in Tausend Computern pro Tag; Zeitraum der zweiten Woche nach der ersten Infizierung",
    gesucht="Term für die Anzahl der in diesem Zeitraum infizierten Computer",
    verfahren="Integral der Rate von 7 bis 14 mal 1000",
    schritte="1", zahlenraum="ganz", einheiten="Computer", abhaengig_von="",
    ergebnis="1000 · Integral von 7 bis 14 über f(t) dt (amtlich)",
    zwischenergebnis="Wert ≈ 132 000",
    niveau_geschaetzt="II",
    fehlerquelle="Grenzen 8 bis 14 oder Faktor 1000 vergessen",
    bemerkung="Standardbezug: K3 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Rekonstruktion von Beständen.")

# ---- Analysis 2.1: symmetrische Funktionen
row("2021MerhoehtAAnalysis21", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Weiteren Extrempunkt aus der Symmetrie des Graphen angeben", typ_neben="",
    stichwoerter="f achsensymmetrisch: Hochpunkt (−2; 1)|g punktsymmetrisch: Tiefpunkt (−2; −1)",
    voraussetzungen="Achsensymmetrie spiegelt Hochpunkte auf Hochpunkte|Punktsymmetrie macht aus Hoch- Tiefpunkte",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f in IR mit zur y-Achse symmetrischem Graphen, g in IR mit zum Ursprung symmetrischem Graphen; beide Graphen haben den Hochpunkt (2; 1)",
    gesucht="je ein weiterer Extrempunkt mit Art",
    verfahren="Spiegelung des Hochpunkts",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="der Graph von f hat den Hochpunkt (−2; 1), der Graph von g den Tiefpunkt (−2; −1) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="für g einen Hochpunkt (−2; 1) angeben",
    bemerkung="Standardbezug: K1 II, K2 I, K6 I. Amtlich.")

row("2021MerhoehtAAnalysis21", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Symmetrie eines Produkts symmetrischer Funktionen allgemein nachweisen", typ_neben="",
    stichwoerter="h(x) = f(x) · (g(x))³|h(−x) = f(−x) · (g(−x))³ = f(x) · (−g(x))³ = −f(x) · (g(x))³ = −h(x)|punktsymmetrisch zum Ursprung",
    voraussetzungen="f(−x) = f(x), g(−x) = −g(x)|ungerade Potenz erhält das Vorzeichen|Symmetriebedingung prüfen",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f achsensymmetrisch, g punktsymmetrisch; h(x) = f(x) · (g(x))³ in IR",
    gesucht="Untersuchung des Graphen von h auf Symmetrie",
    verfahren="h(−x) mit den Symmetrieeigenschaften umformen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="h(−x) = f(−x) · (g(−x))³ = f(x) · (−g(x))³ = −f(x) · (g(x))³ = −h(x); damit ist der Graph von h symmetrisch bezüglich des Koordinatenursprungs (amtlich)",
    zwischenergebnis="Kontrolle mit Beispielfunktionen",
    niveau_geschaetzt="III",
    fehlerquelle="(−g(x))³ = (g(x))³ setzen und Achsensymmetrie folgern",
    bemerkung="Standardbezug: K1 III, K4 II, K5 III. Amtlich, eigene Rechnung bestätigt (mit Beispielfunktionen). Eichregel: (c) allgemeiner Nachweis ohne Terme, die Beziehung h(−x) = −h(x) wird aus den Symmetrieeigenschaften hergeleitet.")

# ---- Analysis 2.2: Graph mit Ableitungsgraph, gestreckte Schar
FG_SKIZZE = ("Koordinatensystem mit Gitter (Schrittweite 1), x-Achse von −3 bis 2,5, y-Achse von −0,5 bis 4,5; "
             "G_f (durchgezogen) exponentiell wachsend durch (0; 2), links gegen etwa 1 abflachend; Graph von f' "
             "(gestrichelt) durch (0; 1), links gegen 0, rechts steil steigend")
row("2021MerhoehtAAnalysis22", "a", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Tangentensteigung aus dem Graphen der Ableitung ablesen", typ_neben="",
    stichwoerter="Steigung der Tangente in (0; f(0)) = f'(0)|Ableitungsgraph bei x = 0: Wert 1",
    voraussetzungen="Tangentensteigung als Wert von f'|Wert am gestrichelten Graphen ablesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=FG_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung mit G_f und dem Graphen von f'; f'(0) = 1 am Graphen",
    gesucht="Steigung der Tangente an G_f im Punkt (0; f(0))",
    verfahren="f'(0) ablesen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Steigung ist 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="f(0) = 2 statt f'(0) ablesen",
    bemerkung="Standardbezug: K4 II, K5 I. Amtlich, Wert aus der Abbildung.")

row("2021MerhoehtAAnalysis22", "b", seite="1", punkte="4", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Nullstelle der Tangente an einen gestreckten Graphen als parameterunabhängig nachweisen", typ_neben="",
    stichwoerter="g_c = c · f, g_c' = c · f'|Tangente in (0; g_c(0)): y = c · f'(0) · x + c · f(0) = c · x + 2c|c · x + 2c = 0 ⇔ x = −2 für jedes c",
    voraussetzungen="Streckung in y-Richtung als Vorfaktor|Ableitung des Vielfachen|Tangentengleichung mit Parameter|Nullstelle unabhängig von c",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=FG_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Schar g_c mit c > 0, Graph von g_c aus G_f durch Streckung mit Faktor c in y-Richtung; f(0) = 2 und f'(0) = 1 aus der Abbildung",
    gesucht="x-Koordinate des Schnittpunkts der Tangente an den Graphen von g_c in (0; g_c(0)) mit der x-Achse, rechnerisch",
    verfahren="Tangentengleichung mit c aufstellen und null setzen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2021MerhoehtAAnalysis22-a",
    ergebnis="Tangente an den Graphen von g_c: y = g_c'(0) · x + g_c(0) = c · f'(0) · x + c · f(0) = c · x + 2c; c · x + 2c = 0 ⇔ x = −2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="g_c'(0) = f'(0) setzen (Streckung nicht ableiten)",
    bemerkung="Standardbezug: K1 III, K2 III, K4 I, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis mit Parameter c, bei dem die Beziehung g_c' = c · f' hergeleitet wird und die Nullstelle als c-unabhängig folgt; (a) Streckung in Terme übersetzen.")

# ---- AG/LA (A1) 1.1: Spur (ungegliedert)
row("2021MerhoehtAAGLAA111", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Parameter für gleiche Spur von Matrix und Inverser bestimmen", typ_neben="",
    stichwoerter="M_k = ((1; 0), (−k; k))|Inverse über M · X = E: a = 1, b = 0, d = 1/k, c = 1|Spur von M_k: 1 + k, Spur der Inversen: 1 + 1/k|1 + k = 1 + 1/k ⇔ k = ±1",
    voraussetzungen="Definition der Spur (im Text vorgegeben)|Inverse über die Gleichung M · X = E|Gleichung k = 1/k",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Spur einer quadratischen Matrix als Summe der Hauptdiagonale (mit Beispiel); M_k = ((1; 0), (−k; k)) mit k ≠ 0",
    gesucht="alle k, für die M_k und die inverse Matrix dieselbe Spur haben",
    verfahren="Inverse bestimmen, Spuren gleichsetzen",
    schritte="3", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="((1; 0), (−k; k)) · ((a; b), (c; d)) = ((1; 0), (0; 1)) liefert a = 1, b = 0 und damit k · d = 1 ⇔ d = 1/k; es gilt 1 + k = 1 + 1/k ⇔ k = −1 oder k = 1 (amtlich)",
    zwischenergebnis="Inverse ((1; 0), (1; 1/k))",
    niveau_geschaetzt="II",
    fehlerquelle="Spur der Inversen als Kehrwert der Spur ansetzen",
    bemerkung="Standardbezug: K2 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 1.1). Die Definition „Spur“ ist wörtlich vorgegeben, nach dem Prinzip keine Deutung. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

# ---- AG/LA (A1) 1.2: A(2; −3; 1), B(2; 3; 1) (Sachgebiet „AG/LA“, Dublette 2021MerhoehtAAGLAA212)
row("2021MerhoehtAAGLAA112", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Parallelität einer Geraden zu einer Koordinatenachse über die Koordinaten begründen", typ_neben="",
    stichwoerter="A(2; −3; 1), B(2; 3; 1)|gleiche x- und z-Koordinate|AB = (0; 6; 0) parallel zur y-Achse",
    voraussetzungen="Richtungsvektor aus zwei Punkten|Koordinatenachse als Richtung",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(2; −3; 1), B(2; 3; 1)",
    gesucht="Begründung, dass die Gerade AB parallel zur y-Achse ist",
    verfahren="Koordinaten vergleichen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="A und B haben die gleiche x-Koordinate und die gleiche z-Koordinate (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="„liegt auf der y-Achse“ statt „parallel“",
    bemerkung="Standardbezug: K1 I, K4 I. Amtlich, eigene Rechnung bestätigt. Die Kurzbeschreibung nennt nur AG/LA; die Datei liegt wortgleich als 2021MerhoehtAAGLAA212 ein zweites Mal vor (Dublette ohne Zeile).")

row("2021MerhoehtAAGLAA112", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Punkte auf einer Koordinatenachse mit rechtem Winkel zu zwei Punkten bestimmen", typ_neben="",
    stichwoerter="C(0; c; 0) auf der y-Achse|CA · CB = (2; −3 − c; 1) · (2; 3 − c; 1) = 5 − 9 + c² = 0|c = ±2|C(0; −2; 0) und C(0; 2; 0)",
    voraussetzungen="Punkt auf der y-Achse ansetzen|rechter Winkel bei C als Skalarprodukt|quadratische Gleichung, beide Lösungen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(2; −3; 1), B(2; 3; 1); C auf der y-Achse; Gerade AC senkrecht zu Gerade BC",
    gesucht="Koordinaten aller möglichen Punkte C",
    verfahren="C(0; c; 0), Skalarprodukt CA · CB = 0 lösen",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="es gilt C(0; c; 0) mit reellem c; damit CA · CB = (2; −3 − c; 1) · (2; 3 − c; 1) = 5 − 9 + c² = 0 ⇔ c = −2 oder c = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur c = 2 angeben",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. „C auf der y-Achse“ ist eine unmittelbare Übersetzung, nach dem Prinzip II.")

# ---- AG/LA (A1) 1.3: Verflechtung mit a und b
VERFL3_SKIZZE = ("Verflechtungsdiagramm mit drei Ebenen: oben R1, R2, R3; Mitte Z1, Z2, Z3; unten E1, E2. Pfeile mit "
                 "Mengen: R1→Z1 a, R2→Z1 b, R2→Z2 2, R3→Z2 1, R3→Z3 5; Z1→E1 2, Z2→E1 3, Z2→E2 2, Z3→E1 1, Z3→E2 2")
row("2021MerhoehtAAGLAA113", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Rohstoffmenge aus den übrigen Rohstoffen über die Gesamtmatrix bestimmen", typ_neben="",
    stichwoerter="r = ((4; 0), (12; 4), (8; 12)) · e|4e1 = 8 gibt e1 = 2|12 · 2 + 4e2 = 28 gibt e2 = 1|r3 = 8 · 2 + 12 · 1 = 28",
    voraussetzungen="Zeilen der Gesamtmatrix als Gleichungen|Produktionsmengen aus zwei Zeilen, dritte Zeile auswerten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=VERFL3_SKIZZE, kontext="Produktion", textumfang="lang",
    gegeben="Rohstoffe R1, R2, R3, Zwischenprodukte Z1, Z2, Z3, Endprodukte E1, E2; r = ((4; 0), (12; 4), (8; 12)) · e; verbraucht 8 Mengeneinheiten R1, 28 Mengeneinheiten R2 und r3 Mengeneinheiten R3, nichts bleibt übrig",
    gesucht="Wert von r3",
    verfahren="e1 und e2 aus den ersten beiden Zeilen, r3 aus der dritten",
    schritte="3", zahlenraum="ganz", einheiten="Mengeneinheiten", abhaengig_von="",
    ergebnis="mit 4e1 = 8 ⇔ e1 = 2 ergibt sich 12 · 2 + 4e2 = 28 ⇔ e2 = 1, d. h. r3 = 8 · 2 + 12 · 1 = 28 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="r3 aus dem Diagramm statt aus der Matrix zusammensetzen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2021MerhoehtAAGLAA113", "b", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Unbekannte Bedarfe im Diagramm aus der Gesamtmatrix bestimmen", typ_neben="",
    stichwoerter="R1-Zeile: a · 2 = 4, a = 2|R2-Zeile: b · 2 + 2 · 3 = 12, b = 3",
    voraussetzungen="Gesamtmatrix als Produkt Rohstoff-Zwischenprodukt mal Zwischenprodukt-Endprodukt|einzelne Einträge als Summe von Wegen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=VERFL3_SKIZZE, kontext="Produktion", textumfang="kurz",
    gegeben="Diagramm mit unbekannten Bedarfen a (R1 → Z1) und b (R2 → Z1); Gesamtmatrix ((4; 0), (12; 4), (8; 12))",
    gesucht="Werte von a und b",
    verfahren="Einträge der Gesamtmatrix über die Wege R1 → Z1 → E1 und R2 → (Z1, Z2) → E1 aufstellen",
    schritte="2", zahlenraum="ganz", einheiten="Mengeneinheiten", abhaengig_von="",
    ergebnis="2a = 4 ⇔ a = 2, 2b + 3 · 2 = 12 ⇔ b = 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="b aus 2b = 12 ohne den Weg über Z2 berechnen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt (Matrixprodukt). Teilaufgabe steht auf Seite 2.")

# ---- AG/LA (A1) 2.1: Parallelogramm, Teilverhältnis (Sachgebiet „AG/LA“, Dublette 2021MerhoehtAAGLAA22)
row("2021MerhoehtAAGLAA121", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen", typ_neben="",
    stichwoerter="A(0; 0; 0), B(3; 4; 1), C(1; 7; 3), D(−2; 3; 2)|AB = (3; 4; 1) = DC",
    voraussetzungen="Parallelogramm über AB = DC",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(0; 0; 0), B(3; 4; 1), C(1; 7; 3), D(−2; 3; 2)",
    gesucht="Nachweis, dass ABCD ein Parallelogramm ist",
    verfahren="zwei gegenüberliegende Verbindungsvektoren vergleichen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="AB = (3; 4; 1) = DC (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="AB mit CD statt DC vergleichen (Vorzeichen)",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt. Die Kurzbeschreibung nennt nur AG/LA; die Datei liegt wortgleich als 2021MerhoehtAAGLAA22 ein zweites Mal vor (Dublette ohne Zeile).")

row("2021MerhoehtAAGLAA121", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Teilverhältnis eines Punktes auf einer Strecke aus einem rechten Winkel ermitteln", typ_neben="",
    stichwoerter="T = λ · C auf AC|rechter Winkel bei B: AB · TB = 0|(3; 4; 1) · (3 − λ; 4 − 7λ; 1 − 3λ) = 26 − 34λ = 0|λ = 13/17|AT : CT = 13 : 4",
    voraussetzungen="Punkt auf einer Strecke mit Parameter|rechter Winkel als Skalarprodukt|Teilverhältnis aus λ und 1 − λ",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A, B, C wie in a; T auf der Strecke AC; Dreieck ABT bei B rechtwinklig",
    gesucht="Verhältnis |AT| : |CT|",
    verfahren="T als λ · AC ansetzen, Skalarprodukt AB · TB = 0 lösen, Verhältnis λ : (1 − λ)",
    schritte="3", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="2021MerhoehtAAGLAA121-a",
    ergebnis="T hat den Ortsvektor λ · AC; AB · TB = (3; 4; 1) · (3 − λ; 4 − 7λ; 1 − 3λ) = 9 − 3λ + 16 − 28λ + 1 − 3λ = 26 − 34λ = 0 ⇔ λ = 13/17; damit beträgt das gesuchte Verhältnis 13 : 4 (amtlich)",
    zwischenergebnis="T(13/17; 91/17; 39/17)",
    niveau_geschaetzt="III",
    fehlerquelle="Verhältnis als 13 : 17 angeben (λ statt λ : (1 − λ))",
    bemerkung="Standardbezug: K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Lage von T und den rechten Winkel in eine Gleichung in λ übersetzen und λ in ein Teilverhältnis zurückübersetzen (Verkettung).")

# ---- AG/LA (A1) 2.2: vertauschbare Matrizen (ungegliedert)
row("2021MerhoehtAAGLAA122", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln", typ_neben="",
    stichwoerter="A = ((1; 2), (0; 1)), B = ((a; b), (c; d))|A · B = ((a + 2c; b + 2d), (c; d)), B · A = ((a; 2a + b), (c; 2c + d))|a + 2c = a, b + 2d = 2a + b, d = 2c + d|c = 0, a = d|B = ((a; b), (0; a))",
    voraussetzungen="allgemeine Matrix ansetzen|beide Produkte berechnen|Einträge vergleichen, Lösungsmenge mit zwei freien Parametern angeben",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A = ((1; 2), (0; 1)); für B gilt A · B = B · A",
    gesucht="alle Matrizen B, die die Bedingung erfüllen",
    verfahren="B allgemein ansetzen, Produkte gleichsetzen, Bedingungen ablesen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Matrizen haben die Form ((a; b), (c; d)); A · B = B · A ⇔ ((a + 2c; b + 2d), (c; d)) = ((a; 2a + b), (c; 2c + d)) liefert a + 2c = a, b + 2d = 2a + b und d = 2c + d, d. h. c = 0 und a = d; damit kommen für B die Matrizen ((a; b), (0; a)) mit reellen a, b infrage (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur B = A oder B = E angeben",
    bemerkung="Standardbezug: K2 III, K4 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Eichregel: (c) allgemeiner Ansatz mit vier Parametern, aus dem die Beziehungen c = 0 und a = d hergeleitet werden, Lösungsmenge mit freien Parametern (offener Punkt der Liste). Vorschlag für den Abgleich: gegen „Matrizenalgebra: Bedingungen für die Vertauschbarkeit zweier Matrizen aus einer binomischen Gleichung untersuchen“ (2025-ea-A) prüfen. Thema Matrizen (nirgends Prüfungsgegenstand).")

# ---- AG/LA (A2) 1.1: Spiegelung an E
row("2021MerhoehtAAGLAA211", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen", typ_neben="",
    stichwoerter="E: x1 + 3x2 = 0|P(−1; 7; 2): −1 + 3 · 7 = 20 ≠ 0",
    voraussetzungen="Koordinaten einsetzen",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(−1; 7; 2), E: x1 + 3x2 = 0",
    gesucht="Nachweis, dass P nicht in E liegt",
    verfahren="einsetzen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="−1 + 3 · 7 ≠ 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="x3 = 2 einsetzen wollen (kommt nicht vor)",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet.")

row("2021MerhoehtAAGLAA211", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Spiegelpunkt an einer Ebene über die Lotgerade bestimmen", typ_neben="",
    stichwoerter="Lotgerade x = (−1; 7; 2) + λ · (1; 3; 0)|Schnitt mit E: −1 + λ + 3(7 + 3λ) = 0 ⇔ λ = −2|Spiegelpunkt mit 2λ: (−1; 7; 2) − 4 · (1; 3; 0) = (−5; −5; 2)",
    voraussetzungen="Lotgerade mit dem Normalenvektor|Schnitt mit der Ebene|doppelten Parameter für den Spiegelpunkt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(−1; 7; 2), E: x1 + 3x2 = 0",
    gesucht="Koordinaten des Spiegelpunkts von P an E",
    verfahren="Lotgerade aufstellen, Lotfußpunkt über λ, Parameter verdoppeln",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Gleichung der Geraden g senkrecht zu E durch P: x = (−1; 7; 2) + λ · (1; 3; 0); mit −1 + λ + 3 · (7 + 3λ) = 0 ⇔ 10λ = −20 ⇔ λ = −2 ergibt sich für den Ortsvektor des gesuchten Punkts (−1; 7; 2) − 4 · (1; 3; 0) = (−5; −5; 2) (amtlich)",
    zwischenergebnis="Lotfußpunkt (−3; 1; 2)",
    niveau_geschaetzt="II",
    fehlerquelle="beim Lotfußpunkt stehen bleiben (λ statt 2λ)",
    bemerkung="Standardbezug: K1 I, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Spiegelpunkt an einer Ebene über den bekannten Lotfußpunkt bestimmen“ (2026-ga-A) getrennt: dort ist der Lotfußpunkt gegeben.")

# ---- AG/LA (A2) 1.3: Geradenschar und Ebene
row("2021MerhoehtAAGLAA213", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharparameter für Orthogonalität von Gerade und Ebene bestimmen", typ_neben="",
    stichwoerter="E: x1 − x2 + x3 = 3, Normalenvektor (1; −1; 1)|g_a Richtung (2; 1 + a; 2)|(2; 1 + a; 2) = μ · (1; −1; 1) ⇔ μ = 2 und a = −3",
    voraussetzungen="senkrecht zur Ebene heißt Richtungsvektor kollinear zum Normalenvektor|Komponentenvergleich",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: x1 − x2 + x3 − 3 = 0; g_a: x = (1; −2; 0) + λ · (2; 1 + a; 2), a reell",
    gesucht="Wert von a, für den g_a senkrecht zu E steht",
    verfahren="Richtungsvektor als Vielfaches des Normalenvektors ansetzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(2; 1 + a; 2) = μ · (1; −1; 1) ⇔ μ = 2 und a = −3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Skalarprodukt null setzen (Parallelität statt Orthogonalität)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2021MerhoehtAAGLAA213", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Existenz eines Scharparameters für eine Gerade in der Ebene untersuchen", typ_neben="",
    stichwoerter="Stützpunkt (1; −2; 0) in E: 1 + 2 + 0 − 3 = 0|Richtungsvektor senkrecht zum Normalenvektor: 2 − (1 + a) + 2 = 0 ⇔ a = 3|ja, für a = 3",
    voraussetzungen="Gerade in Ebene heißt Stützpunkt in E und Richtung senkrecht zum Normalenvektor|lineare Gleichung in a",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E und g_a wie in a",
    gesucht="Untersuchung, ob es ein a gibt, für das g_a in E liegt",
    verfahren="Stützpunkt prüfen, Skalarprodukt Richtung mal Normalenvektor null setzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2021MerhoehtAAGLAA213-a",
    ergebnis="wegen 1 − (−2) + 0 − 3 = 0 gilt (1; −2; 0) in E; (1; −1; 1) · (2; 1 + a; 2) = 0 liefert die Gleichung 2 − 1 − a + 2 = 0; da diese Gleichung lösbar ist, gibt es einen Wert von a, für den g_a in E liegt (amtlich)",
    zwischenergebnis="a = 3",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Richtung prüfen, den Stützpunkt vergessen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 1.1: Vierfeldertafel mit p
VFT_SKIZZE = ("Vierfeldertafel mit Zeilen A, nicht A und Spalten B, nicht B: Feld A∩B = p, Zeilensumme A = 3p, "
              "Zeilensumme nicht A = 1 − 3p, Spaltensumme B = 4p; übrige Felder leer")
row("2021MerhoehtAStochastik11", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel mit Parameter vervollständigen und einen Parameterwert ausschließen", typ_neben="",
    stichwoerter="A∩B̄ = 3p − p = 2p|Ā∩B = 4p − p = 3p|Ā∩B̄ = 1 − 3p − 3p = 1 − 6p|Spalte B̄: 1 − 4p|für p = 1/5 wäre 1 − 6p < 0",
    voraussetzungen="Randsummen und Differenzen|Wahrscheinlichkeiten nicht negativ",
    format="Tabelle|Begründung", operator="Vervollständigen Sie|Zeigen Sie", antwort="Term|Text",
    material="Tabelle", skizze=VFT_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Vierfeldertafel mit P(A∩B) = p, P(A) = 3p, P(Ā) = 1 − 3p, P(B) = 4p; p ≠ 0",
    gesucht="vollständige Tafel; Nachweis, dass p nicht 1/5 sein kann",
    verfahren="fehlende Felder als Differenzen, Vorzeichen von 1 − 6p prüfen",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Tafel: A∩B = p, A∩B̄ = 2p, Ā∩B = 3p, Ā∩B̄ = 1 − 6p, Spaltensummen 4p und 1 − 4p, Gesamtsumme 1; für p = 1/5 gilt 1 − 6p < 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="1 − 3p − 3p falsch als 1 − 3p rechnen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Vierfeldertafel.")

row("2021MerhoehtAStochastik11", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Parameter für die Unabhängigkeit zweier Ereignisse aus der Vierfeldertafel ermitteln", typ_neben="",
    stichwoerter="P(A) · P(B) = P(A∩B)|3p · 4p = p|12p = 1 (p ≠ 0)|p = 1/12",
    voraussetzungen="Produktformel der Unabhängigkeit|durch p kürzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze=VFT_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Tafel aus a; für einen Wert von p sind A und B stochastisch unabhängig",
    gesucht="dieser Wert von p",
    verfahren="Produktformel ansetzen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="2021MerhoehtAStochastik11-a",
    ergebnis="für p ≠ 0 gilt: P(A) · P(B) = P(A∩B) ⇔ 3p · 4p = p ⇔ 12p = 1 ⇔ p = 1/12 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="p = 0 als Lösung angeben",
    bemerkung="Standardbezug: K3 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 1.2: B(100; p), E = 50
row("2021MerhoehtAStochastik12", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Standardabweichung einer Binomialverteilung aus n und Erwartungswert berechnen", typ_neben="",
    stichwoerter="100 · p = 50 ⇔ p = 0,5|σ = √(100 · 0,5 · 0,5) = 5",
    voraussetzungen="E = n · p|σ = √(n · p · (1 − p))",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X binomialverteilt mit n = 100 und p; E(X) = 50",
    gesucht="Standardabweichung von X",
    verfahren="p aus dem Erwartungswert, dann σ",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="100 · p = 50 ⇔ p = 0,5; damit ergibt sich für die Standardabweichung √(100 · 0,5 · 0,5) = 5 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Varianz 25 als Standardabweichung angeben",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2021MerhoehtAStochastik12", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit eines symmetrischen Intervalls über die Symmetrie der Binomialverteilung berechnen", typ_neben="",
    stichwoerter="p = 0,5: Verteilung symmetrisch um 50|P(X ≥ 61) = P(X ≤ 39) ≈ 2 %|P(40 ≤ X ≤ 60) ≈ 100 % − 2 · 2 % = 96 %",
    voraussetzungen="Symmetrie der Binomialverteilung für p = 0,5|Komplement",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X ~ B(100; 0,5); P(X ≥ 61) ≈ 2 %",
    gesucht="P(40 ≤ X ≤ 60) aus diesem Wert",
    verfahren="beide Ränder abziehen",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="2021MerhoehtAStochastik12-a",
    ergebnis="P(40 ≤ X ≤ 60) ≈ 100 % − 2 · 2 % = 96 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="98 % angeben (nur einen Rand abziehen)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Die Symmetrie folgt aus p = 0,5 in a; nach dem Prinzip keine Deutung.")

# ---- Stochastik 1.3: Gewinnspiel mit Verteilung im Diagramm
GEW_SKIZZE = ("Säulendiagramm P(A = k) mit Säulen bei k = 0 (Höhe p), k = b (Höhe 3p) und k = 6 (Höhe 2p); "
              "y-Achse mit den Markierungen p, 2p, 3p")
row("2021MerhoehtAStochastik13", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsgrößen und Verteilungen",
    typ="Wahrscheinlichkeit p aus der Summe 1 im Diagramm nachweisen", typ_neben="",
    stichwoerter="p + 3p + 2p = 1|p = 1/6",
    voraussetzungen="Summe der Wahrscheinlichkeiten 1",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Diagramm", skizze=GEW_SKIZZE, kontext="Glücksspiel", textumfang="mittel",
    gegeben="Einsatz 3 Euro; Auszahlung A mit P(A = 0) = p, P(A = b) = 3p, P(A = 6) = 2p aus dem Diagramm",
    gesucht="Nachweis, dass p = 1/6",
    verfahren="Summe der Säulen gleich 1",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="p + 3p + 2p = 1 ⇔ p = 1/6 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Säulenhöhen als Auszahlungen lesen",
    bemerkung="Standardbezug: K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2021MerhoehtAStochastik13", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="Erwartungswert der Auszahlung gleich Einsatz 3|1/6 · 0 + 3/6 · b + 2/6 · 6 = 3|b = 2",
    voraussetzungen="Erwartungswert aus der Verteilung|Ausgleich als Gleichung (wörtlich vorgegeben)",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=GEW_SKIZZE, kontext="Glücksspiel", textumfang="kurz",
    gegeben="Verteilung aus a mit p = 1/6; auf lange Sicht gleichen sich Einsätze (3 Euro) und Auszahlungen aus",
    gesucht="Wert von b",
    verfahren="E(A) = 3 nach b auflösen",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="Euro", abhaengig_von="2021MerhoehtAStochastik13-a",
    ergebnis="3/6 · b + 2/6 · 6 = 3 ⇔ b = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="E(A) = 0 (Gewinn) statt E(A) = 3 (Auszahlung) ansetzen",
    bemerkung="Standardbezug: K3 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zusammengezogener Typ). Die Ausgleichsbedingung ist wörtlich vorgegeben, nach dem Prinzip II.")

row("2021MerhoehtAStochastik13", "c", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Urnenmodell zu einer vorgegebenen Verteilung beschreiben", typ_neben="",
    stichwoerter="Wahrscheinlichkeiten 1/6, 3/6, 2/6|eine rote, drei grüne, zwei blaue Kugeln|rot 0 Euro, grün 2 Euro, blau 6 Euro",
    voraussetzungen="Wahrscheinlichkeiten als Anteile von Kugeln|Zuordnung der Auszahlungen",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Diagramm", skizze=GEW_SKIZZE, kontext="Glücksspiel", textumfang="kurz",
    gegeben="Verteilung P(A = 0) = 1/6, P(A = 2) = 3/6, P(A = 6) = 2/6; Behälter mit roten, grünen und blauen Kugeln",
    gesucht="Beschreibung einer Durchführung des Spiels mit dem Behälter",
    verfahren="Kugelzahlen im Verhältnis 1 : 3 : 2, eine Kugel ziehen, Farbe als Auszahlung",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2021MerhoehtAStochastik13-b",
    ergebnis="in den Behälter werden eine rote, drei grüne und zwei blaue Kugeln gelegt; der Spieler entnimmt zufällig eine Kugel; ist sie rot, erfolgt keine Auszahlung, ist sie grün, werden 2 Euro ausgezahlt, ist sie blau, 6 Euro (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Zuordnung der Farben zu den Auszahlungen weglassen",
    bemerkung="Standardbezug: K3 II, K6 II. Amtlich.")

# ---- Stochastik 2.1: gelbe Kugeln
row("2021MerhoehtAStochastik21", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen", typ_neben="",
    stichwoerter="jede dritte Kugel gelb: P(gelb) = 1/3|mit Zurücklegen: (1/3)² = 1/9",
    voraussetzungen="Anteil als Wahrscheinlichkeit|Unabhängigkeit bei Zurücklegen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="kurz",
    gegeben="Behälter, jede dritte Kugel gelb; zweimal Ziehen mit Zurücklegen",
    gesucht="Wahrscheinlichkeit, dass beide Kugeln gelb sind",
    verfahren="Quadrat der Einzelwahrscheinlichkeit",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/3 · 1/3 = 1/9 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="ohne Zurücklegen rechnen (Kugelzahl unbekannt)",
    bemerkung="Standardbezug: K3 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet (zusammengezogener Typ).")

row("2021MerhoehtAStochastik21", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Kugelzahl aus zwei Wahrscheinlichkeitsbedingungen vor und nach einem Austausch ermitteln", typ_neben="",
    stichwoerter="nach dem Austausch P(gelb, gelb) = 1/16, also P(gelb) = 1/4|vorher jede dritte gelb: x gelbe von 4x Kugeln nach dem Austausch|(x + 2)/(4x) = 1/3|3x + 6 = 4x ⇔ x = 6",
    voraussetzungen="Quadratwurzel aus 1/16 als Anteil|Gesamtzahl aus dem neuen Anteil|Anteil vor dem Austausch als Gleichung|Bruchgleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="jede dritte Kugel gelb; zwei gelbe durch zwei blaue ersetzt; danach P(beide gelb) = 1/16 bei zweimaligem Ziehen mit Zurücklegen",
    gesucht="Anzahl der gelben Kugeln nach dem Austausch",
    verfahren="aus 1/16 den Anteil 1/4 folgern, Gesamtzahl 4x, Anteil vor dem Austausch (x + 2)/(4x) = 1/3",
    schritte="3", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="2021MerhoehtAStochastik21-a",
    ergebnis="da die Wahrscheinlichkeit für zwei gelbe Kugeln nach dem Austausch 1/16 beträgt, ist nun jede vierte Kugel gelb; mit x für die gesuchte Anzahl ergibt sich (x + 2)/(4x) = 1/3 ⇔ 3x + 6 = 4x ⇔ x = 6 (amtlich)",
    zwischenergebnis="24 Kugeln insgesamt, vorher 8 gelbe",
    niveau_geschaetzt="III",
    fehlerquelle="Gesamtzahl bei 3x belassen (vor dem Austausch war sie 3 · 8 = 24 = 4x)",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die beiden Anteilsangaben (1/16 als Quadrat, „jede dritte“ vor dem Austausch) in eine Gleichung in x übersetzen; Verkettung zweier Zustände des Behälters.")

# ---- Stochastik 2.2: Glücksrad, Gleichung für p (ungegliedert)
row("2021MerhoehtAStochastik22", seite="1", punkte="5", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten", typ_neben="",
    stichwoerter="P(1) = 1/3 (120°), P(2) = p, P(3) = 2/3 − p|Auszahlung nur bei Summe ≥ 5: (2; 3) oder (3; 2) mit Auszahlung 5, (3; 3) mit 6|Erwartungswert gleich Einsatz 1|2 · p · (2/3 − p) · 5 + (2/3 − p)² · 6 = 1",
    voraussetzungen="Sektorwahrscheinlichkeit aus dem Winkel|Restwahrscheinlichkeit in p|Ergebnisse mit Summe ≥ 5 finden|Pfadwahrscheinlichkeiten|Erwartungswert gleich Einsatz",
    format="Rechnung", operator="Leiten Sie her|Erläutern Sie", antwort="Term|Text",
    material="Skizze", skizze="Glücksrad mit drei Sektoren 1 (120°, links unten), 2 (oben) und 3 (rechts unten); Zeiger oben",
    kontext="Glücksspiel", textumfang="lang",
    gegeben="Glücksrad mit Sektoren 1 (120°), 2 (Wahrscheinlichkeit p) und 3; Einsatz 1 Euro, zwei Drehungen, Auszahlung der Summe bei Summe mindestens 5, sonst nichts; Einsätze und Auszahlungen gleichen sich auf lange Sicht aus",
    gesucht="Herleitung einer Gleichung für p mit Erläuterung",
    verfahren="Auszahlungsfälle bestimmen, Wahrscheinlichkeiten in p, Erwartungswert gleich 1",
    schritte="4", zahlenraum="Bruch", einheiten="Euro", abhaengig_von="",
    ergebnis="eine Auszahlung erfolgt nur bei zweimal 3 oder den Zahlen 2 und 3; P(3, 3) = (2/3 − p)², P(2 und 3) = 2 · p · (2/3 − p); der Erwartungswert der Auszahlung muss mit dem Einsatz übereinstimmen: 2 · p · (2/3 − p) · 5 + (2/3 − p)² · 6 = 1 (amtlich)",
    zwischenergebnis="p ≈ 0,205 (eigene Lösung der Gleichung)",
    niveau_geschaetzt="III",
    fehlerquelle="P(3) = 1 − p ansetzen (Sektor 1 vergessen) oder Summe 4 (2 und 2) mitzählen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K4 I, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Eichregel: (a) die Spielregel in Auszahlungsfälle und Wahrscheinlichkeiten in p übersetzen, P(3) aus dem Winkel herleiten; die Ausgleichsbedingung selbst ist wörtlich, die Verkettung mit den erst zu findenden Fällen macht III.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Tangentensteigung an einer Nullstelle über die Ableitung nachweisen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die Steigung der Tangente in einem Punkt des Graphen über den Ableitungswert nachweisen.",
     "2021MerhoehtAAnalysis11-a"),
    ("Fläche: Fläche zwischen Graph und zwei Tangenten berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Den Inhalt der Fläche zwischen einem Graphen und zwei sich schneidenden Tangenten berechnen: "
     "Tangentengleichungen, Schnittpunkt, Integrale der Differenzen (auch über Symmetrie).",
     "2021MerhoehtAAnalysis11-b"),
    ("Ableitung mit Parameter in faktorisierter Form nachweisen", "Analysis", "Ableitungsregeln",
     "Eine vorgegebene faktorisierte Ableitung einer ganzrationalen Funktion mit Parameter durch Ableiten "
     "und Ausklammern nachweisen.",
     "2021MerhoehtAAnalysis12-a"),
    ("Scharparameter aus der y-Koordinate der Tiefpunkte ermitteln", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameter einer Schar aus der vorgegebenen y-Koordinate der Extrempunkte ermitteln: Extremstellen "
     "mit Parameter, Funktionswert gleichsetzen.",
     "2021MerhoehtAAnalysis12-b"),
    ("Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen", "Analysis", "Ableitungsregeln",
     "Eine vorgegebene Ableitung eines Produkts aus Potenz und e-Funktion mit Produkt- und Kettenregel "
     "nachweisen und in die vorgegebene Form bringen.",
     "2021MerhoehtAAnalysis13-a"),
    ("Zeitpunkt der größten Rate aus der Ableitung angeben", "Analysis", "Ableitung und Änderungsrate",
     "Den Zeitpunkt der größten Rate im Sachzusammenhang als Nullstelle der gegebenen Ableitung angeben.",
     "2021MerhoehtAAnalysis13-b"),
    ("Term für einen Bestand aus einer Rate über ein Integral angeben", "Analysis", "Rekonstruktion von Beständen",
     "Einen Term für die in einem Zeitraum angefallene Menge als Integral über die Rate angeben, mit "
     "Grenzen aus dem Zeitraum und Umrechnung der Einheit.",
     "2021MerhoehtAAnalysis13-c"),
    ("Symmetrie: Weiteren Extrempunkt aus der Symmetrie des Graphen angeben", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Aus einem bekannten Extrempunkt und der Achsen- oder Punktsymmetrie des Graphen einen weiteren "
     "Extrempunkt mit seiner Art angeben.",
     "2021MerhoehtAAnalysis21-a"),
    ("Symmetrie: Symmetrie eines Produkts symmetrischer Funktionen allgemein nachweisen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Ohne Terme nachweisen, welche Symmetrie ein aus achsen- und punktsymmetrischen Funktionen gebildetes "
     "Produkt hat (h(−x) umformen).",
     "2021MerhoehtAAnalysis21-b"),
    ("Tangentensteigung aus dem Graphen der Ableitung ablesen", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Die Steigung der Tangente an einer Stelle als Wert des abgebildeten Ableitungsgraphen ablesen.",
     "2021MerhoehtAAnalysis22-a"),
    ("Nullstelle der Tangente an einen gestreckten Graphen als parameterunabhängig nachweisen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Für eine in y-Richtung gestreckte Schar die Tangente in einem Punkt mit Parameter aufstellen und zeigen, "
     "dass ihre Nullstelle nicht vom Streckfaktor abhängt.",
     "2021MerhoehtAAnalysis22-b"),
    ("Matrizenalgebra: Parameter für gleiche Spur von Matrix und Inverser bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Die Inverse einer Parametermatrix über M · X = E bestimmen und den Parameter so wählen, dass Matrix und "
     "Inverse dieselbe Spur haben.",
     "2021MerhoehtAAGLAA111"),
    ("Parallelität einer Geraden zu einer Koordinatenachse über die Koordinaten begründen", "Analytische Geometrie",
     "Geraden",
     "Begründen, dass die Gerade durch zwei Punkte parallel zu einer Koordinatenachse ist, weil die beiden "
     "anderen Koordinaten übereinstimmen.",
     "2021MerhoehtAAGLAA112-a"),
    ("Dreieck: Punkte auf einer Koordinatenachse mit rechtem Winkel zu zwei Punkten bestimmen",
     "Analytische Geometrie", "Orthogonalität",
     "Alle Punkte einer Koordinatenachse bestimmen, von denen aus zwei gegebene Punkte unter einem rechten "
     "Winkel erscheinen (Skalarprodukt mit Parameter, quadratische Gleichung).",
     "2021MerhoehtAAGLAA112-b"),
    ("Verflechtung: Rohstoffmenge aus den übrigen Rohstoffen über die Gesamtmatrix bestimmen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus zwei bekannten Rohstoffverbräuchen die Produktionsmengen und daraus den dritten Verbrauch über die "
     "Gesamtmatrix bestimmen.",
     "2021MerhoehtAAGLAA113-a"),
    ("Verflechtung: Unbekannte Bedarfe im Diagramm aus der Gesamtmatrix bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Unbekannte Einträge eines Verflechtungsdiagramms aus der gegebenen Gesamtmatrix über die Wege durch "
     "die Zwischenstufe bestimmen.",
     "2021MerhoehtAAGLAA113-b"),
    ("Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Nachweisen, dass vier Punkte ein Parallelogramm bilden, weil zwei gegenüberliegende Verbindungsvektoren "
     "gleich sind.",
     "2021MerhoehtAAGLAA121-a"),
    ("Dreieck: Teilverhältnis eines Punktes auf einer Strecke aus einem rechten Winkel ermitteln",
     "Analytische Geometrie", "Orthogonalität",
     "Den Punkt einer Strecke mit Parameter ansetzen, aus einem rechten Winkel den Parameter bestimmen und "
     "in ein Teilverhältnis übersetzen.",
     "2021MerhoehtAAGLAA121-b"),
    ("Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Alle Matrizen B mit A · B = B · A für eine gegebene Matrix A ermitteln: allgemeiner Ansatz, Produkte "
     "vergleichen, Lösungsmenge mit freien Parametern.",
     "2021MerhoehtAAGLAA122"),
    ("Spiegelpunkt an einer Ebene über die Lotgerade bestimmen", "Analytische Geometrie", "Spiegelung",
     "Den Spiegelpunkt eines Punktes an einer Ebene bestimmen: Lotgerade mit dem Normalenvektor, Schnitt mit "
     "der Ebene, Parameter verdoppeln.",
     "2021MerhoehtAAGLAA211-b"),
    ("Scharparameter für Orthogonalität von Gerade und Ebene bestimmen", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Den Parameter einer Geradenschar so bestimmen, dass der Richtungsvektor kollinear zum Normalenvektor "
     "einer Ebene ist.",
     "2021MerhoehtAAGLAA213-a"),
    ("Existenz eines Scharparameters für eine Gerade in der Ebene untersuchen", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Untersuchen, ob eine Gerade der Schar in einer Ebene liegt: Stützpunkt in der Ebene, Richtungsvektor "
     "senkrecht zum Normalenvektor als Gleichung im Parameter.",
     "2021MerhoehtAAGLAA213-b"),
    ("Vierfeldertafel mit Parameter vervollständigen und einen Parameterwert ausschließen", "Stochastik",
     "Vierfeldertafel",
     "Eine Vierfeldertafel mit Einträgen in einem Parameter vervollständigen und einen Parameterwert über "
     "eine negative Wahrscheinlichkeit ausschließen.",
     "2021MerhoehtAStochastik11-a"),
    ("Parameter für die Unabhängigkeit zweier Ereignisse aus der Vierfeldertafel ermitteln", "Stochastik",
     "Unabhängigkeit",
     "Den Parameter einer Vierfeldertafel so ermitteln, dass die Produktformel P(A) · P(B) = P(A∩B) gilt.",
     "2021MerhoehtAStochastik11-b"),
    ("Standardabweichung einer Binomialverteilung aus n und Erwartungswert berechnen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Aus n und dem Erwartungswert p bestimmen und daraus die Standardabweichung berechnen.",
     "2021MerhoehtAStochastik12-a"),
    ("Wahrscheinlichkeit eines symmetrischen Intervalls über die Symmetrie der Binomialverteilung berechnen",
     "Stochastik", "Binomialverteilung",
     "Für p = 0,5 die Wahrscheinlichkeit eines um den Erwartungswert symmetrischen Intervalls aus einer "
     "Randwahrscheinlichkeit über die Symmetrie berechnen.",
     "2021MerhoehtAStochastik12-b"),
    ("Wahrscheinlichkeit p aus der Summe 1 im Diagramm nachweisen", "Stochastik", "Zufallsgrößen und Verteilungen",
     "Den Wert eines Parameters p nachweisen, mit dem die Säulenhöhen einer Verteilung angegeben sind, über "
     "die Summe 1.",
     "2021MerhoehtAStochastik13-a"),
    ("Laplace-Experiment: Urnenmodell zu einer vorgegebenen Verteilung beschreiben", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Ein Urnenexperiment mit farbigen Kugeln beschreiben, das eine vorgegebene Wahrscheinlichkeitsverteilung "
     "erzeugt (Kugelzahlen im Verhältnis der Wahrscheinlichkeiten, Zuordnung der Werte).",
     "2021MerhoehtAStochastik13-c"),
    ("Laplace-Experiment: Kugelzahl aus zwei Wahrscheinlichkeitsbedingungen vor und nach einem Austausch ermitteln",
     "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Die Kugelzahl eines Behälters aus Anteilsangaben vor und nach dem Austausch von Kugeln ermitteln "
     "(Pfadwahrscheinlichkeit als Quadrat des Anteils, Bruchgleichung).",
     "2021MerhoehtAStochastik21-b"),
    ("Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Aus Spielregeln mit unbekannter Sektorwahrscheinlichkeit die Auszahlungsfälle und ihre "
     "Wahrscheinlichkeiten bestimmen und die Gleichung Erwartungswert gleich Einsatz aufstellen.",
     "2021MerhoehtAStochastik22"),
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
