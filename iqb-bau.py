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
    "stapel": "2020-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2020MgrundlegendAAnalysis11": 5,
        "2020MgrundlegendAAnalysis12": 5,
        "2020MgrundlegendAAGLAA111": 5,
        "2020MgrundlegendAAGLAA112": 5,
        "2020MgrundlegendAAGLAA12": 5,
        "2020MgrundlegendAAGLAA211": 5,
        "2020MgrundlegendAAGLAA212": 5,
        "2020MgrundlegendAStochastik11": 5,
        "2020MgrundlegendAStochastik12": 5,
        "2020MgrundlegendAStochastik2": 5,
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

# ---- Analysis 1.1: x³ − 12x + 16
row("2020MgrundlegendAAnalysis11", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen", typ_neben="",
    stichwoerter="f(x) = x³ − 12x + 16|f'(x) = 3x² − 12 = 0 ⇔ x = ±2|Vorzeichenwechsel von f' bei −2 und 2",
    voraussetzungen="Ableitung|notwendige und hinreichende Bedingung",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − 12x + 16 in IR",
    gesucht="Nachweis, dass −2 und 2 die Extremstellen von f sind",
    verfahren="f' null setzen, Vorzeichenwechsel prüfen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 3x² − 12 = 0 ⇔ x² = 4 ⇔ x = −2 oder x = 2; f'(x) ändert bei x = −2 und bei x = 2 sein Vorzeichen (amtlich)",
    zwischenergebnis="f''(−2) = −12 < 0 (Hochpunkt), f''(2) = 12 > 0 (Tiefpunkt)",
    niveau_geschaetzt="I",
    fehlerquelle="hinreichende Bedingung vergessen",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet (hier zwei Stellen).")

row("2020MgrundlegendAAnalysis11", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Berührung des Graphen mit der x-Achse über die Extrempunkte begründen", typ_neben="",
    stichwoerter="Berühren ohne Terrassenpunkt nur in einem Extrempunkt|f(−2) = 32 ≠ 0, f(2) = 0|genau ein Berührpunkt (2; 0)",
    voraussetzungen="Berührung der x-Achse als Extrempunkt mit Wert 0|Funktionswerte an den Extremstellen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x³ − 12x + 16 mit den Extremstellen −2 und 2",
    gesucht="Begründung, dass die x-Achse den Graphen in genau einem Punkt berührt",
    verfahren="Funktionswerte an beiden Extremstellen prüfen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2020MgrundlegendAAnalysis11-a",
    ergebnis="die x-Achse kann diesen Funktionsgraphen, der keinen Terrassenpunkt hat, nur in einem Extrempunkt berühren; es gilt f(−2) ≠ 0 und f(2) = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur f(2) = 0 zeigen, ohne f(−2) ≠ 0",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Eine Deutung (Berühren heißt Extrempunkt auf der Achse), nach dem Prinzip II.")

# ---- Analysis 1.2: quadratische Funktion aus Tangente (ungegliedert)
row("2020MgrundlegendAAnalysis12", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Quadratische Funktion aus Ursprung und Tangentengleichung bestimmen", typ_neben="",
    stichwoerter="f(x) = ax² + bx + c, f(0) = 0 gibt c = 0|Tangente y = 4x − 2 in (2; f(2)): f(2) = 6, f'(2) = 4|I 4a + 2b = 6, II 4a + b = 4|b = 2, a = 1/2",
    voraussetzungen="Punkt auf der Tangente als Funktionswert|Tangentensteigung als Ableitungswert|Gleichungssystem",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="quadratische Funktion f durch den Ursprung; Tangente in (2; f(2)) mit y = 4x − 2",
    gesucht="Funktionsterm von f",
    verfahren="drei Bedingungen aufstellen und lösen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(x) = ax² + bx + c; f(0) = 0 ⇔ c = 0; f(2) = 4 · 2 − 2 = 6 und f'(2) = 4 liefern I 4a + 2b = 6, II 4a + b = 4; aus I und II ergibt sich b = 2 und damit a = 1/2 (amtlich)",
    zwischenergebnis="f(x) = 1/2 x² + 2x",
    niveau_geschaetzt="II",
    fehlerquelle="f(2) = 4 statt 6 ansetzen (Achsenabschnitt der Tangente übersehen)",
    bemerkung="Standardbezug: K2 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 1.2).")

# ---- AG/LA (A1) 1.1: Vertauschungsmatrix
row("2020MgrundlegendAAGLAA111", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Matrix-Vektor-Produkt berechnen", typ_neben="",
    stichwoerter="M = ((0; 1; 0), (0; 0; 1), (1; 0; 0)), v = (1; 2; 3)|M · v = (2; 3; 1)",
    voraussetzungen="Zeile mal Spalte",
    format="Rechnung", operator="Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Vertauschungsmatrix (je Zeile und Spalte genau eine 1) M = ((0; 1; 0), (0; 0; 1), (1; 0; 0)); v = (1; 2; 3)",
    gesucht="Vektor M · v",
    verfahren="multiplizieren",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="((0; 1; 0), (0; 0; 1), (1; 0; 0)) · (1; 2; 3) = (2; 3; 1) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Spalten statt Zeilen mit v multiplizieren ((3; 1; 2))",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2020MgrundlegendAAGLAA111", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Inverse einer Vertauschungsmatrix angeben", typ_neben="",
    stichwoerter="Umkehrung der Vertauschung|M⁻¹ = ((0; 0; 1), (1; 0; 0), (0; 1; 0)) = M^T",
    voraussetzungen="Inverse macht die Vertauschung rückgängig|Transponierte einer Vertauschungsmatrix",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="M = ((0; 1; 0), (0; 0; 1), (1; 0; 0))",
    gesucht="inverse Matrix zu M",
    verfahren="Vertauschung umkehren",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="((0; 0; 1), (1; 0; 0), (0; 1; 0)) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="M selbst als Inverse angeben (M³ = E, nicht M²)",
    bemerkung="Standardbezug: K1 II, K2 I, K4 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MgrundlegendAAGLAA111", "c", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Aufbau von Vertauschungsmatrizen mit vorgegebener Wirkung beschreiben", typ_neben="",
    stichwoerter="genau zwei Einträge vertauscht heißt ein Eintrag bleibt|Eins auf der Diagonale hält einen Eintrag fest|genau eine Eins auf der Diagonale, die anderen nicht",
    voraussetzungen="Eins auf der Diagonale als Festhalten|Vertauschung zweier Einträge",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Vertauschungsmatrizen N (3×3); N · v hat gegenüber v genau zwei vertauschte Einträge",
    gesucht="Beschreibung des Aufbaus aller solchen N",
    verfahren="Rolle der Diagonaleinträge deuten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="eine der Einsen steht auf der Diagonale, die anderen nicht (amtlich)",
    zwischenergebnis="drei solche Matrizen",
    niveau_geschaetzt="II",
    fehlerquelle="„zwei Einsen auf der Diagonale“ (das wäre die Einheitsmatrix)",
    bemerkung="Standardbezug: K1 II, K2 II, K6 I. Amtlich, eigene Rechnung bestätigt (alle sechs Vertauschungsmatrizen geprüft).")

# ---- AG/LA (A1) 1.2: inverse Matrix, Fixvektor
row("2020MgrundlegendAAGLAA112", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Einträge der inversen Matrix mit Platzhaltern angeben", typ_neben="",
    stichwoerter="A = ((0; 1/2; 0), (0; 0; −1/5), (−10; 0; 0))|A⁻¹ = ((0; 0; c), (a; 0; 0), (0; b; 0))|A · A⁻¹ = E: a · 1/2 = 1, b · (−1/5) = 1, c · (−10) = 1|a = 2, b = −5, c = −1/10",
    voraussetzungen="A · A⁻¹ = E|Kehrwerte der Einträge",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A = ((0; 1/2; 0), (0; 0; −1/5), (−10; 0; 0)); A⁻¹ = ((0; 0; c), (a; 0; 0), (0; b; 0))",
    gesucht="Werte von a, b, c",
    verfahren="Produkt mit E vergleichen oder Kehrwerte",
    schritte="1", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="a = 2, b = −5, c = −1/10 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen bei b und c",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2020MgrundlegendAAGLAA112", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen", typ_neben="",
    stichwoerter="A · v = v: I 1/2 y = x, II −1/5 z = y, III −10x = z|z = 10 gibt y = −2, x = −1|v = (−1; −2; 10)",
    voraussetzungen="Gleichungssystem aus A · v = v|eine Lösung ungleich null wählen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A wie in a; es gibt v ≠ 0 mit A · v = v",
    gesucht="ein solcher Vektor",
    verfahren="Gleichungssystem aufstellen, z frei wählen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="A · v = v liefert I 1/2 y = x, II −1/5 z = y, III −10x = z; eine Lösung ist x = −1, y = −2 und z = 10 (amtlich)",
    zwischenergebnis="alle Lösungen t · (−1; −2; 10)",
    niveau_geschaetzt="II",
    fehlerquelle="das System als eindeutig lösbar behandeln und nur v = 0 finden",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zusammengezogener Typ, t = 1).")

# ---- AG/LA (A1) 2: M · M mit ganzzahligen Einträgen (ungegliedert)
row("2020MgrundlegendAAGLAA12", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Ganzzahlige Einträge einer Matrix aus ihrem Quadrat bestimmen", typ_neben="",
    stichwoerter="M = ((0; 0; c), (a; 0; 0), (d; b; 0))|M² = ((cd; bc; 0), (0; 0; ac), (ab; 0; cd))|I cd = −10, II bc = 2, III ac = 6, IV ab = 3|ganzzahlig: aus II und IV b = ±1|(−3; −1; −2; 5) und (3; 1; 2; −5)",
    voraussetzungen="Matrizenprodukt mit Parametern|Gleichungssystem in Produkten|Ganzzahligkeit als Fallunterscheidung nach b",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="M = ((0; 0; c), (a; 0; 0), (d; b; 0)) mit ganzzahligen a, b, c, d; M · M = ((−10; 2; 0), (0; 0; 6), (3; 0; −10))",
    gesucht="alle Zahlentupel (a; b; c; d)",
    verfahren="M² ausrechnen, Einträge vergleichen, Ganzzahligkeit nutzen",
    schritte="4", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="mit M² = ((cd; bc; 0), (0; 0; ac), (ab; 0; cd)) ergibt sich I cd = −10, II bc = 2, III ac = 6, IV ab = 3, V cd = −10; da alle Werte ganzzahlig sein sollen, kommen aufgrund von II und IV für b nur −1 und 1 infrage; damit ergeben sich die beiden Möglichkeiten (−3; −1; −2; 5) und (3; 1; 2; −5) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur eine der beiden Lösungen finden oder b = ±2 zulassen (dann a nicht ganzzahlig)",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt (Suche über alle ganzzahligen Tupel). Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2). Eichregel: (a) Ganzzahligkeit in die Bedingung b teilt 2 und 3 übersetzen und Fallunterscheidung b = ±1 mit zwei verschiedenen Ausgängen (Grundregel, kein Nullfall). Thema Matrizen (nirgends Prüfungsgegenstand).")

# ---- AG/LA (A2) 1.1: Prisma
PRISMA_SKIZZE = ("Schrägbild eines dreiseitigen Prismas ABCDEF: Grundfläche ABC links unten, Deckfläche DEF rechts "
                 "oben, Kanten AD, BE, CF parallel; E in der Mitte hinten gestrichelt verbunden")
row("2020MgrundlegendAAGLAA211", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen", typ_neben="",
    stichwoerter="L: x + 6y + 2z = 33, Normalenvektor (1; 6; 2)|BE = (3; 18; 6) = 3 · (1; 6; 2)|Seitenkante senkrecht zur Grundfläche",
    voraussetzungen="gerades Prisma heißt Seitenkante senkrecht zur Grundfläche|Normalenvektor ablesen|Kollinearität",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=PRISMA_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Prisma ABCDEF mit A(3; 3; 6), B(−1; 5; 2), C(7; 4; 1), E(2; 23; 8); A, B, C in L: x + 6y + 2z = 33",
    gesucht="Begründung, dass das Prisma gerade ist",
    verfahren="BE mit dem Normalenvektor von L vergleichen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="BE = (3; 18; 6) = 3 · (1; 6; 2), d. h. die Seite BE steht senkrecht zur Grundfläche des Prismas (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Skalarprodukt BE · n = 0 erwarten",
    bemerkung="Standardbezug: K1 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zusammengezogener Typ).")

row("2020MgrundlegendAAGLAA211", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Parallele Ebene mit vorgegebenem Volumenverhältnis eines Prismas ermitteln", typ_neben="",
    stichwoerter="M parallel zu L: x + 6y + 2z = b|Volumen des Teilkörpers mit E doppelt so groß: M in 1/3 der Höhe über L|Punkt B + 1/3 · BE = (0; 11; 4) in M|b = 74",
    voraussetzungen="Volumenverhältnis paralleler Schnitte eines Prismas als Höhenverhältnis|Punkt auf der Kante im Verhältnis 1 : 2|Ebenengleichung mit Normalenvektor",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="Körper", skizze=PRISMA_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Prisma wie in a; M parallel zu L teilt das Prisma so, dass der Teilkörper mit E doppelt so groß ist wie der andere",
    gesucht="Gleichung von M",
    verfahren="Volumenverhältnis 1 : 2 in Höhenverhältnis übersetzen, Punkt in 1/3 der Kante BE, in x + 6y + 2z = b einsetzen",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2020MgrundlegendAAGLAA211-a",
    ergebnis="M: x + 6y + 2z = b; (−1; 5; 2) + 1/3 · (3; 18; 6) = (0; 11; 4), d. h. der Punkt (0; 11; 4) liegt in M; damit ergibt sich b = 74 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="M in halber Höhe ansetzen oder in 2/3 der Höhe (Teilkörper mit E wäre dann der kleinere)",
    bemerkung="Standardbezug: K2 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) das Volumenverhältnis 1 : 2 erst in ein Höhenverhältnis am Prisma übersetzen und dann in einen Punkt der Kante; amtlich II.")

# ---- AG/LA (A2) 1.2: Pyramide über rechtwinkligem Dreieck
row("2020MgrundlegendAAGLAA212", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen einer Pyramide über einem rechtwinkligen Dreieck mit Pythagoras berechnen", typ_neben="",
    stichwoerter="Hypotenuse 5, Kathete 4: BC = √(25 − 16) = 3|Grundfläche 1/2 · 4 · 3 = 6|V = 1/3 · 6 · 7 = 14",
    voraussetzungen="Satz des Pythagoras|Dreiecksfläche|Pyramidenvolumen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Pyramide ABCS; Grundfläche rechtwinkliges Dreieck ABC mit Hypotenuse AB = 5 cm, Kathete AC = 4 cm; CS senkrecht zur Grundfläche, 7 cm",
    gesucht="Volumen der Pyramide",
    verfahren="zweite Kathete, Grundfläche, Volumenformel",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="cm³", abhaengig_von="",
    ergebnis="BC = √(5² − 4²) = 3; 1/3 · 1/2 · 4 · 3 · 7 = 14, d. h. die Pyramide hat ein Volumen von 14 cm³ (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Grundfläche mit 4 · 5 statt 4 · 3 rechnen",
    bemerkung="Standardbezug: K2 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Keine Koordinaten in a.")

row("2020MgrundlegendAAGLAA212", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Koordinaten der Eckpunkte eines beschriebenen Körpers wählen", typ_neben="",
    stichwoerter="C in den Ursprung, Katheten auf die Achsen|A(4; 0; 0), B(0; 3; 0), C(0; 0; 0), S(0; 0; 7)",
    voraussetzungen="rechten Winkel in den Ursprung legen|Höhe auf die z-Achse",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Pyramide aus a; Koordinatensystem mit 1 LE = 1 cm",
    gesucht="mögliche Koordinaten der Eckpunkte",
    verfahren="rechtwinklige Lage an den Achsen ausnutzen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2020MgrundlegendAAGLAA212-a",
    ergebnis="A(4; 0; 0), B(0; 3; 0), C(0; 0; 0), S(0; 0; 7) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="B(0; 5; 0) setzen (Hypotenuse als Kathete)",
    bemerkung="Standardbezug: K2 II, K6 I. Amtlich, eigene Rechnung bestätigt (Längen und rechte Winkel geprüft).")

# ---- Stochastik 1.1: drei blaue, zwei rote Kugeln
row("2020MgrundlegendAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="drei blaue, zwei rote|blau dann rot 3/5 · 2/4, rot dann blau 2/5 · 3/4|Summe 3/5",
    voraussetzungen="Pfadregel ohne Zurücklegen|beide Reihenfolgen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="kurz",
    gegeben="Behälter mit drei blauen und zwei roten Kugeln; zwei Kugeln werden entnommen",
    gesucht="Wahrscheinlichkeit für zwei verschiedene Farben",
    verfahren="zwei Pfade addieren",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="3/5 · 2/4 + 2/5 · 3/4 = 3/5 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="nur einen Pfad rechnen (3/10)",
    bemerkung="Standardbezug: K3 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet.")

row("2020MgrundlegendAStochastik11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Gewinnwahrscheinlichkeiten in einem Wechselspiel vergleichen", typ_neben="",
    stichwoerter="erste Spielerin gewinnt sofort mit 2/5|oder blau, blau, rot: 3/5 · 2/4 · 2/3|zusammen 3/5 > 1/2",
    voraussetzungen="Pfade ohne Zurücklegen mit Abbruch bei rot|Gewinnpfade der ersten Spielerin summieren|mit 1/2 vergleichen",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Behälter wieder mit drei blauen und zwei roten Kugeln; zwei Spielerinnen ziehen abwechselnd ohne Zurücklegen; wer zuerst rot zieht, gewinnt",
    gesucht="Nachweis, dass die zuerst ziehende Spielerin im Vorteil ist",
    verfahren="Gewinnwahrscheinlichkeit der ersten Spielerin über die Pfade 1. Zug rot und 3. Zug rot",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="für die Wahrscheinlichkeit dafür, dass die Spielerin gewinnt, die die erste Kugel entnimmt, gilt 2/5 + 3/5 · 2/4 · 2/3 = 3/5 > 1/2 (amtlich)",
    zwischenergebnis="spätestens im vierten Zug fällt rot; 5. Zug entfällt",
    niveau_geschaetzt="II",
    fehlerquelle="mit Zurücklegen rechnen oder den Pfad blau, blau, rot vergessen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet.")

# ---- Stochastik 1.2: Fest mit Verkleideten
row("2020MgrundlegendAStochastik12", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Anteil aus Anteilen und bedingten Anteilen über die Vierfeldertafel berechnen", typ_neben="",
    stichwoerter="Erwachsene 60 %, davon verkleidet 12 % aller Gäste, nicht verkleidet 48 %|Jugendliche 40 %, davon 75 % verkleidet, 25 % nicht: 0,25 · 0,4 = 10 %|nicht verkleidet 58 %",
    voraussetzungen="Anteile absolut und bedingt unterscheiden|Vierfeldertafel oder Baum",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Fest/Verkleidung", textumfang="mittel",
    gegeben="Anteil verkleideter Erwachsener unter allen Gästen 12 %, Anteil aller Erwachsenen 60 %; 75 % der Jugendlichen verkleidet",
    gesucht="Anteil der nicht Verkleideten unter allen Gästen",
    verfahren="0,48 + 0,25 · 0,4",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,48 + 0,25 · 0,4 = 58 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="12 % als bedingten Anteil unter den Erwachsenen lesen",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Vierfeldertafel im grundlegenden Niveau.")

row("2020MgrundlegendAStochastik12", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bayes-Term im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Zähler 0,12 verkleidete Erwachsene|Nenner 0,12 + 0,75 · 0,4 alle Verkleideten|Anteil der Erwachsenen unter den Verkleideten",
    voraussetzungen="Nenner als Gesamtanteil der Verkleideten|Quotient als bedingter Anteil",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Fest/Verkleidung", textumfang="kurz",
    gegeben="Term 0,12/(0,12 + 0,75 · 0,4)",
    gesucht="Bedeutung des Terms im Sachzusammenhang",
    verfahren="Zähler und Nenner deuten",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="der Term gibt den Anteil der Erwachsenen unter allen Verkleideten an (amtlich)",
    zwischenergebnis="Wert 2/7",
    niveau_geschaetzt="II",
    fehlerquelle="Anteil der Verkleideten unter den Erwachsenen (Bedingung vertauscht)",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2021-ga-A wiederverwendet.")

# ---- Stochastik 2: Binomialverteilung
row("2020MgrundlegendAStochastik2", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit einer Binomialverteilung aus n und Erwartungswert berechnen", typ_neben="",
    stichwoerter="n = 4, E = 2: p = 1/2|P(X = 4) = (1/2)⁴ = 1/16",
    voraussetzungen="E = n · p|Wahrscheinlichkeit für lauter Treffer",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X1 binomialverteilt mit n1 = 4 und p1; E(X1) = 2",
    gesucht="P(X1 = 4)",
    verfahren="p aus dem Erwartungswert, dann p⁴",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="mit n1 · p1 = 2 ⇔ p1 = 1/2 ergibt sich P(X1 = 4) = 1/16 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="(4 über 4) vergessen ist unschädlich; p = 2 aus E = 2 lesen",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2020MgrundlegendAStochastik2", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Sachaussage zu einer Ungleichung mit Binomialsumme formulieren", typ_neben="",
    stichwoerter="0,8^n = P(kein Treffer)|1 − 0,8^n = P(mindestens ein Treffer)|Ungleichung < 0,3: alle n, für die diese Wahrscheinlichkeit kleiner als 0,3 ist",
    voraussetzungen="Gegenereignis|Potenz als Pfad ohne Treffer|Ungleichung als Bedingung an n",
    format="Kurzantwort", operator="Formulieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X2 binomialverteilt mit n2 und p2 = 0,2; Ansatz 1 − 0,8^(n2) < 0,3",
    gesucht="eine Aufgabenstellung, die sich mit diesem Ansatz lösen lässt",
    verfahren="Term als Wahrscheinlichkeit für mindestens einen Treffer deuten, Ungleichung als Bedingung an n",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="die Wahrscheinlichkeit dafür, dass mindestens ein Treffer erzielt wird, ist kleiner als 0,3; bestimmen Sie alle Werte, die für n2 infrage kommen (amtlich)",
    zwischenergebnis="Lösung n2 = 1",
    niveau_geschaetzt="III",
    fehlerquelle="0,8^n als Wahrscheinlichkeit für mindestens einen Treffer deuten",
    bemerkung="Standardbezug: K1 III, K4 II, K5 II, K6 III. Amtlich, eigene Rechnung bestätigt. Typ aus 2024-ga-A wiederverwendet (dort Binomialsumme, hier Gegenereignis). Eichregel: (d) Ungleichung in eine Sachaussage mit zwei Deutungen (Gegenereignis, Bedingung an n) übersetzen.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Berührung des Graphen mit der x-Achse über die Extrempunkte begründen", "Analysis", "Kurvenuntersuchung",
     "Begründen, dass die x-Achse den Graphen in genau einem Punkt berührt: Berühren nur in einem Extrempunkt "
     "mit Funktionswert null, Funktionswerte der Extremstellen prüfen.",
     "2020MgrundlegendAAnalysis11-b"),
    ("Quadratische Funktion aus Ursprung und Tangentengleichung bestimmen", "Analysis",
     "Rekonstruktion von Funktionsgleichungen",
     "Den Term einer quadratischen Funktion aus einem Punkt und einer Tangentengleichung (Funktionswert und "
     "Steigung an der Berührstelle) über ein Gleichungssystem bestimmen.",
     "2020MgrundlegendAAnalysis12"),
    ("Matrizenalgebra: Matrix-Vektor-Produkt berechnen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Das Produkt einer Matrix mit einem Vektor berechnen.",
     "2020MgrundlegendAAGLAA111-a"),
    ("Matrizenalgebra: Inverse einer Vertauschungsmatrix angeben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Die Inverse einer Vertauschungsmatrix angeben, die die Vertauschung rückgängig macht (Transponierte).",
     "2020MgrundlegendAAGLAA111-b"),
    ("Matrizenalgebra: Aufbau von Vertauschungsmatrizen mit vorgegebener Wirkung beschreiben",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Beschreiben, wie Vertauschungsmatrizen mit einer vorgegebenen Wirkung auf einen Vektor aufgebaut sind "
     "(Lage der Einsen relativ zur Diagonale).",
     "2020MgrundlegendAAGLAA111-c"),
    ("Matrizenalgebra: Einträge der inversen Matrix mit Platzhaltern angeben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Die Platzhalter einer vorgegebenen inversen Matrix über A · A⁻¹ = E oder Kehrwerte angeben.",
     "2020MgrundlegendAAGLAA112-a"),
    ("Matrizenalgebra: Ganzzahlige Einträge einer Matrix aus ihrem Quadrat bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Alle ganzzahligen Einträge einer Matrix mit Platzhaltern aus dem vorgegebenen Quadrat der Matrix "
     "bestimmen: Produktgleichungen, Ganzzahligkeit als Fallunterscheidung.",
     "2020MgrundlegendAAGLAA12"),
    ("Parallele Ebene mit vorgegebenem Volumenverhältnis eines Prismas ermitteln", "Analytische Geometrie", "Ebenen",
     "Die zur Grundfläche parallele Ebene ermitteln, die ein gerades Prisma in einem vorgegebenen "
     "Volumenverhältnis teilt (Höhenverhältnis, Punkt auf der Kante, Koordinatenform).",
     "2020MgrundlegendAAGLAA211-b"),
    ("Körper: Volumen einer Pyramide über einem rechtwinkligen Dreieck mit Pythagoras berechnen",
     "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Das Volumen einer Pyramide aus Seitenlängen ohne Koordinaten berechnen: fehlende Kathete mit Pythagoras, "
     "Grundfläche, Volumenformel.",
     "2020MgrundlegendAAGLAA212-a"),
    ("Körper: Koordinaten der Eckpunkte eines beschriebenen Körpers wählen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Für einen nur durch Längen und rechte Winkel beschriebenen Körper passende Koordinaten der Eckpunkte "
     "angeben (rechte Winkel auf die Achsen legen).",
     "2020MgrundlegendAAGLAA212-b"),
    ("Anteil aus Anteilen und bedingten Anteilen über die Vierfeldertafel berechnen", "Stochastik", "Vierfeldertafel",
     "Einen Anteil an der Gesamtheit aus gegebenen absoluten und bedingten Anteilen berechnen (Vierfeldertafel "
     "oder Baum).",
     "2020MgrundlegendAStochastik12-a"),
    ("Einzelwahrscheinlichkeit einer Binomialverteilung aus n und Erwartungswert berechnen", "Stochastik",
     "Binomialverteilung",
     "Aus n und dem Erwartungswert p bestimmen und damit eine Einzelwahrscheinlichkeit berechnen.",
     "2020MgrundlegendAStochastik2-a"),
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
