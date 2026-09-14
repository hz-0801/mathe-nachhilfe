# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.7 · 14.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.8

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

Änderungen gegenüber 0.6 (Vorarbeit Teil B, Auftrag des Lehrers): Eichung in
Teil B gegen die Spalte Anforderungsbereich des Standardbezugs („AB amtlich:
III." in bemerkung, Pflicht in Teil B; weicht sie vom höchsten Kompetenzeintrag
ab, muss bemerkung den Hinweis tragen); Teil A unverändert (Maximum).
Trägerbindung: feste Markierung „Traegerbindung: Kontext" am Anfang von
bemerkung, exakter Wortlaut geprüft, kein eigenes Feld, kein Vermerk heißt frei.

Änderungen gegenüber 0.5: Erfassungseinheit in Teil B ist der Stapel je
Rechnerfassung (KONFIG["stapel"] = "2026-ga-B-wtr"), damit der WTR-Zweig ohne
die MMS-Fassung vollständig sein kann (Probestapel 2026-ga-B); Teil A
unverändert. Eine Datei mit nur einer, unnummerierten Aufgabe in Teil B
führt innen="1" (id …-1a, aufgabe 1).

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
    "stapel": "2025-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2025MgrundlegendBAnalysisWTR1": 25,
        "2025MgrundlegendBAnalysisWTR2": 25,
        "2025MgrundlegendBAGLAA1WTR": 15,
        "2025MgrundlegendBAGLAA2WTR1": 15,
        "2025MgrundlegendBAGLAA2WTR2": 15,
        "2025MgrundlegendBStochastikWTR1": 15,
        "2025MgrundlegendBStochastikWTR2": 15,
        "2025MgrundlegendBStochastikWTR3": 15,
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


def einheit(q):
    """Erfassungseinheit: in Teil A der Stapel, in Teil B der Stapel je Rechnerfassung
    (2026-ga-B-wtr, 2026-ga-B-mms), weil WTR- und MMS-Fassung getrennt erfasst werden (v0.6)."""
    return q["stapel"] if q["teil"] == "A" else f"{q['stapel']}-{q['hilfsmittel'].lower()}"


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
# Stapel 2025-ga-B, WTR-Zweig. innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).

SOLL = {"2025MgrundlegendBAnalysisWTR1": 25, "2025MgrundlegendBAnalysisWTR2": 25,
        "2025MgrundlegendBAGLAA1WTR": 15, "2025MgrundlegendBAGLAA2WTR1": 15, "2025MgrundlegendBAGLAA2WTR2": 15,
        "2025MgrundlegendBStochastikWTR1": 15, "2025MgrundlegendBStochastikWTR2": 15, "2025MgrundlegendBStochastikWTR3": 15}

# ---- Analysis WTR 1, Aufgabe 1: f(x) = 1/3 x³ − 2x + 4
GF1 = "Koordinatensystem mit Gitter, x von −3 bis 3, y von −1 bis 7; Gf punktsymmetrisch zu (0 | 4), Hochpunkt bei etwa (−1,4 | 5,9), Tiefpunkt bei etwa (1,4 | 2,1)"
row("2025MgrundlegendBAnalysisWTR1", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extremstellen berechnen und Monotonieverhalten angeben", typ_neben="",
    stichwoerter="f'(x) = x² − 2 = 0 ⇔ x = ±√2|monoton zunehmend für x ≤ −√2 und x ≥ √2, abnehmend dazwischen",
    voraussetzungen="Ableitung|Nullstellen der Ableitung|Monotonie aus dem Vorzeichen von f'",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/3 x³ − 2x + 4 in IR; Gf symmetrisch zu (0 | 4)",
    gesucht="Extremstellen und Monotonieverhalten",
    verfahren="f' = 0 lösen, Monotoniebereiche angeben",
    schritte="3", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = x² − 2; f'(x) = 0 ⇔ x = −√2 ∨ x = √2; f ist monoton zunehmend für x ≤ −√2 und x ≥ √2 sowie monoton abnehmend für −√2 ≤ x ≤ √2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Monotonie mit offenen statt abgeschlossenen Intervallen oder nur eine Extremstelle",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBAnalysisWTR1", "b", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen", typ_neben="",
    stichwoerter="f(3) = 7, f'(3) = 7|7 = 7 · 3 + n ⇔ n = −14|t: y = 7x − 14|P und t einzeichnen",
    voraussetzungen="Funktionswert und Ableitungswert|Punkt-Steigungs-Form|Gerade einzeichnen",
    format="Rechnung|Zeichnen", operator="Bestimmen Sie|Zeichnen Sie ein", antwort="Term",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="kurz",
    gegeben="f wie in a; Tangente t in P(3 | f(3)); Kontrolle t: y = 7x − 14",
    gesucht="Gleichung von t rechnerisch; P und t in Abbildung 1",
    verfahren="Steigung f'(3), Achsenabschnitt aus P",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(3) = 7; f(3) = 7; 7 = 7 · 3 + n ⇔ n = −14; t: y = 7x − 14; P(3 | 7) und t eingezeichnet (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P außerhalb des Bildausschnitts (y = 7 am oberen Rand) ungenau eintragen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2025MgrundlegendBAnalysisWTR1", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Weiteren Schnittpunkt von Tangente und Graph aus einer vorgegebenen Faktorisierung begründen", typ_neben="",
    stichwoerter="f(x) = 7x − 14 ⇔ f(x) − (7x − 14) = 0 ⇔ 1/3 (x − 3)² (x + 6) = 0|x = 3 (Berührstelle) oder x = −6|genau ein weiterer Punkt",
    voraussetzungen="gemeinsame Punkte als Nullstellen der Differenz|Satz vom Nullprodukt|doppelte Nullstelle als Berührstelle",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) − (7x − 14) = 1/3 (x − 3)² (x + 6) für alle x; t: y = 7x − 14 berührt in P(3 | 7)",
    gesucht="Begründung, dass t und Gf neben P genau einen weiteren gemeinsamen Punkt haben",
    verfahren="Differenz null setzen, Faktoren auswerten",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2025MgrundlegendBAnalysisWTR1-1b",
    ergebnis="f(x) = 7x − 14 ⇔ f(x) − (7x − 14) = 0 ⇔ 1/3 (x − 3)² (x + 6) = 0 ⇔ x = 3 ∨ x = −6 (amtlich)",
    zwischenergebnis="weiterer Punkt (−6 | −56)", niveau_geschaetzt="II",
    fehlerquelle="x = 3 als zweiten Schnittpunkt zählen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBAnalysisWTR1", "d", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Lösung einer Integralgleichung über die Punktsymmetrie und ein Rechteck am Graphen begründen", typ_neben="",
    stichwoerter="k = −1/2|Intervall [−1/2; 1/2] symmetrisch zu 0, Gf punktsymmetrisch zu (0 | 4)|die beiden Flächenstücke über und unter y = 4 sind gleich groß|Integral = Rechteck 1 · 4",
    voraussetzungen="Punktsymmetrie des Graphen|Integral als Fläche|Ausgleich zweier kongruenter Flächenstücke",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="mittel",
    gegeben="Gleichung ∫_k^{k+1} f(x) dx = 4; es gibt eine Lösung k mit −1,5 ≤ k ≤ 1,5; Gf symmetrisch zu (0 | 4)",
    gesucht="diese Lösung ohne Rechnung mit Begründung durch Eintragungen in Abbildung 1",
    verfahren="Intervall um 0 legen, Rechteck der Höhe 4 und Breite 1 einzeichnen, Flächenstücke über und unter 4 gegeneinander aufrechnen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="k = −1/2; aufgrund der Symmetrie von Gf haben die beiden schraffierten Flächen gleichen Inhalt; daher entspricht der Wert des Integrals von −1/2 bis 1/2 über f(x) dx dem Inhalt der Fläche eines Rechtecks der Länge 4 und der Breite 1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="k = 0 oder k = 1/2 wählen (Intervall nicht symmetrisch zu 0)",
    bemerkung="Standardbezug: K1 II, K2 II, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Punktsymmetrie um (0 | 4) erkennen und für den Flächenausgleich nutzen.")

# ---- Analysis WTR 1, Aufgabe 2: Reichweite r(x), Abbildung
REICH = "Koordinatensystem x von −12 bis 36 (°C), y von 0 bis 1,2; Graph von r steigt von etwa 0,55 bei −12 über 0,8 bei 4 zum Hochpunkt (22 | 1,2) und fällt auf etwa 0,95 bei 36"
row("2025MgrundlegendBAnalysisWTR1", "a", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Extrempunkte: Hochpunkt aus dem Graphen ablesen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Hochpunkt (22 | 1,2)|größte Reichweite bei 22 °C|das 1,2-Fache der Nennreichweite",
    voraussetzungen="Ablesen|Koordinaten als Temperatur und Quotient deuten",
    format="Kurzantwort", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=REICH, kontext="Elektroauto/Reichweite", textumfang="lang",
    gegeben="r(x) Quotient aus tatsächlicher Reichweite und Nennreichweite bei Außentemperatur x in °C, −12 ≤ x ≤ 36; Graph in Abbildung 2",
    gesucht="Koordinaten des Hochpunkts und ihre Bedeutung",
    verfahren="Ablesen, beide Koordinaten deuten",
    schritte="2", zahlenraum="dezimal", einheiten="°C", abhaengig_von="",
    ergebnis="(22 | 1,2); die größte tatsächliche Reichweite liegt bei einer Außentemperatur von 22 °C vor; diese beträgt das 1,2-Fache der Nennreichweite (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="1,2 als Reichweite in km deuten",
    bemerkung="Standardbezug: K3 II, K4 I, K6 II. AB amtlich: II. Amtlich (Ablesung).")

row("2025MgrundlegendBAnalysisWTR1", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Bereich mit Funktionswerten über einer Schranke aus dem Graphen bestimmen", typ_neben="",
    stichwoerter="tatsächliche Reichweite größer als Nennreichweite ⇔ r(x) > 1|Gerade y = 1 einzeichnen|etwa 10 °C bis etwa 34 °C",
    voraussetzungen="Bedingung als r(x) > 1|Schnittstellen mit y = 1 ablesen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=REICH, kontext="Elektroauto/Reichweite", textumfang="kurz",
    gegeben="r wie in a; es gibt Temperaturen mit tatsächlicher Reichweite größer als Nennreichweite",
    gesucht="dieser Temperaturbereich mithilfe von Abbildung 2",
    verfahren="r(x) > 1 am Graphen ablesen",
    schritte="2", zahlenraum="ganz", einheiten="°C", abhaengig_von="",
    ergebnis="der gesuchte Temperaturbereich erstreckt sich von etwa 10 °C bis etwa 34 °C (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Bereich um den Hochpunkt schätzen statt r = 1 abzulesen",
    bemerkung="Standardbezug: K2 I, K3 II, K4 I. AB amtlich: II. Amtlich (Ablesung).")

# ---- Analysis WTR 2, Aufgabe 1: f(x) = (2 − x) e^x
GF2 = "Koordinatensystem x von −5 bis 2, y von 0 bis 3; Graph von (2 − x) e^x, von links nahe 0 ansteigend, durch (0 | 2), Hochpunkt (1 | e), Nullstelle 2, danach steil fallend"
row("2025MgrundlegendBAnalysisWTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben", typ_neben="",
    stichwoerter="Nullstelle 2|lim x → −∞: 0|lim x → +∞: −∞",
    voraussetzungen="Nullprodukt|e^x dominiert|Vorzeichen von 2 − x",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=GF2, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = (2 − x) · e^x in IR; Graph in Abbildung 1",
    gesucht="Nullstelle und Verhalten für x → −∞ und x → +∞",
    verfahren="Faktoren betrachten",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Nullstelle: 2; lim f(x) = 0 für x → −∞, lim f(x) = −∞ für x → +∞ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Verhalten für x → +∞ als +∞ (Vorzeichen von 2 − x übersehen)",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBAnalysisWTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen", typ_neben="",
    stichwoerter="f'(x) = −e^x + (2 − x) e^x = (1 − x) e^x|f'(x) = 0 ⇔ x = 1|f(1) = e; Hochpunkt (1 | e)",
    voraussetzungen="Produktregel|Nullstelle der Ableitung|Funktionswert",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GF2, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = (2 − x) · e^x",
    gesucht="Koordinaten des Hochpunkts",
    verfahren="Produktregel, f' = 0, einsetzen",
    schritte="3", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −e^x + (2 − x) · e^x = (1 − x) · e^x; f'(x) = 0 ⇔ x = 1; f(1) = e; Hochpunkt (1 | e) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Produktregel ohne die Ableitung von 2 − x",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Art des Extremums aus der Abbildung, kein Nachweis verlangt.")

row("2025MgrundlegendBAnalysisWTR2", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Näherungswert eines Integrals als Dreiecksfläche am Graphen begründen", typ_neben="",
    stichwoerter="Dreieck mit Ecken (−3 | 0), (1 | 0), (1 | e), Katheten 4 und e|Fläche 1/2 · e · 4|Hypotenuse liegt nahe am Graphen",
    voraussetzungen="Integral als Fläche zwischen Graph und x-Achse|Dreiecksfläche|Näherung durch eine Sehne",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF2, kontext="ohne", textumfang="kurz",
    gegeben="Term 1/2 · e · 4 als Näherungswert für ∫_{−3}^1 f(x) dx",
    gesucht="geometrische Begründung mit Eintragungen in Abbildung 1",
    verfahren="rechtwinkliges Dreieck unter dem Graphen zwischen x = −3 und x = 1 einzeichnen",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="der Inhalt der Fläche, die der Graph von f mit der x-Achse und den Geraden x = −3 und x = 1 einschließt, stimmt näherungsweise mit dem Flächeninhalt des eingezeichneten Dreiecks mit den Kathetenlängen 4 und e überein (amtlich)",
    zwischenergebnis="Dreiecksfläche 2e ≈ 5,44", niveau_geschaetzt="II",
    fehlerquelle="Dreieck mit Kathete 5 (von −3 bis 2) ansetzen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBAnalysisWTR2", "d", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Bestimmtes Integral mit vorgegebener Stammfunktion berechnen", typ_neben="Prozentuale Abweichung eines Näherungswerts vom exakten Wert berechnen",
    stichwoerter="∫_{−3}^1 f = F(1) − F(−3) = 2e − 6e^{−3}|Abweichung (2e − (2e − 6e^{−3}))/(2e − 6e^{−3}) ≈ 6 %",
    voraussetzungen="Hauptsatz|relative Abweichung bezogen auf den exakten Wert",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="F(x) = (3 − x) · e^x Stammfunktion von f; Näherungswert 1/2 · e · 4",
    gesucht="exakter Wert des Integrals von −3 bis 1 und prozentuale Abweichung des Näherungswerts",
    verfahren="F(1) − F(−3), Differenz durch exakten Wert",
    schritte="3", zahlenraum="Potenz|Prozent", einheiten="", abhaengig_von="2025MgrundlegendBAnalysisWTR2-1c",
    ergebnis="∫_{−3}^1 f(x) dx = F(1) − F(−3) = 2e − 6/e³; (2e − (2e − 6/e³))/(2e − 6/e³) ≈ 6 % (amtlich)",
    zwischenergebnis="exakt ≈ 5,138; Näherung ≈ 5,437", niveau_geschaetzt="II",
    fehlerquelle="Abweichung auf den Näherungswert statt auf den exakten Wert beziehen",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (5,8 %). Typ wiederverwendet (2026-ea-B), Abweichung als typ_neben.")

# ---- Analysis WTR 2, Aufgabe 2: Likes a(x), Abbildung
LIKES = "Koordinatensystem x von 0 bis 7 (Stunden), y von 0 bis 3000; Graph von a steigt von 0 erst immer steiler, ab etwa x = 1 immer flacher und nähert sich 2500; a(2) ≈ 1500, a(4) ≈ 2300"
row("2025MgrundlegendBAnalysisWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Verlauf eines Graphen im Sachzusammenhang beschreiben", typ_neben="",
    stichwoerter="Anzahl der Likes nimmt zunächst immer stärker zu|ab einem Zeitpunkt immer schwächer|nähert sich 2500",
    voraussetzungen="Monotonie und Krümmung in Worten|Sättigung als Grenzwert",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=LIKES, kontext="Internetbeitrag/Likes", textumfang="mittel",
    gegeben="a(x) Anzahl der seit 12:00 Uhr abgegebenen Likes, x Stunden seit 12:00 Uhr; Graph in Abbildung 2",
    gesucht="Verlauf des Graphen im Sachzusammenhang",
    verfahren="Graphen abschnittweise beschreiben",
    schritte="1", zahlenraum="ganz", einheiten="Stunden", abhaengig_von="",
    ergebnis="die Anzahl der seit der Veröffentlichung abgegebenen Likes nimmt zunächst immer mehr zu, ab einem bestimmten Zeitpunkt dann immer weniger zu und nähert sich schließlich dem Wert 2500 an (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Abnahme der Likes behaupten (Graph fällt nirgends)",
    bemerkung="Standardbezug: K3 II, K4 I, K6 II. AB amtlich: II. Amtlich.")

row("2025MgrundlegendBAnalysisWTR2", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen", typ_neben="",
    stichwoerter="14:00 bis 16:00 Uhr: x = 2 bis 4|(a(4) − a(2))/2 ≈ (2300 − 1500)/2 = 400",
    voraussetzungen="Uhrzeiten in x umrechnen|Werte ablesen|Differenzenquotient",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=LIKES, kontext="Internetbeitrag/Likes", textumfang="kurz",
    gegeben="a wie in a",
    gesucht="durchschnittlich pro Stunde abgegebene Likes von 14:00 bis 16:00 Uhr",
    verfahren="Werte ablesen, Differenzenquotient",
    schritte="2", zahlenraum="ganz", einheiten="Stunden", abhaengig_von="",
    ergebnis="(a(4) − a(2))/(4 − 2) ≈ (2300 − 1500)/2 = 400 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="a(4)/4 als Durchschnitt nehmen",
    bemerkung="Standardbezug: K2 I, K3 II, K4 II, K5 I. AB amtlich: II. Amtlich (Ablesung), Rechnung bestätigt.")

row("2025MgrundlegendBAnalysisWTR2", "c", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Funktionalgleichung mit Zeitverschiebung grafisch lösen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="a(x + 3) = a(x) + 1000: Stelle, an der der Graph drei Einheiten weiter rechts 1000 höher liegt|Lösung x ≈ 1,9|Zeitpunkt, zu dem die Anzahl der Likes um 1000 kleiner ist als drei Stunden später",
    voraussetzungen="Gleichung als Bedingung an zwei Graphenpunkte lesen|Rechteck 3 breit, 1000 hoch zwischen den Punkten|Deutung",
    format="Rechnung|Kurzantwort", operator="Ermitteln Sie|Interpretieren Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=LIKES, kontext="Internetbeitrag/Likes", textumfang="mittel",
    gegeben="Gleichung a(x + 3) = a(x) + 1000 mit genau einer Lösung für x > 0",
    gesucht="Lösung grafisch in Abbildung 2 und Bedeutung der Gleichung",
    verfahren="Punkte P(x | a(x)) und Q(x + 3 | a(x) + 1000) auf dem Graphen suchen, x ablesen; deuten",
    schritte="3", zahlenraum="dezimal", einheiten="Stunden", abhaengig_von="",
    ergebnis="Lösung der Gleichung: x ≈ 1,9; die Gleichung liefert denjenigen Zeitpunkt, zu dem die Anzahl der für den Beitrag abgegebenen Likes um 1000 kleiner ist als drei Stunden später (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Gleichung als a(3) = a(0) + 1000 lesen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K4 III, K6 II. AB amtlich: III. Amtlich (Ablesung). Eichregel: (a) Gleichung in eine Bedingung an zwei Graphenpunkte übersetzen, verkettet mit der Deutung.")

# ---- AG/LA (A1) WTR: Population, Rechteck mit Parameter
row("2025MgrundlegendBAGLAA1WTR", "a", innen="1", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Eintrag 0,9 in Zeile e, Spalte j|90 % der Jungtiere überleben das zweite Lebensjahr und werden erwachsen",
    voraussetzungen="Zeile = Ziel, Spalte = Herkunft",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Population/Altersklassen", textumfang="lang",
    gegeben="v_{n+1} = M · v_n mit M = ((0; 0,1; 1,5), (0,4; 0; 0), (0; 0,9; 0,7)), Komponenten b (Babys), j (Jungtiere), e (erwachsene Tiere)",
    gesucht="Bedeutung des Eintrags 0,9",
    verfahren="Position in der Matrix deuten",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="90 % der Jungtiere überleben das zweite Lebensjahr (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Eintrag als Anteil der Erwachsenen deuten (Zeile und Spalte vertauscht)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A). Aufgabengruppe A1, außerhalb der Geltung.")

row("2025MgrundlegendBAGLAA1WTR", "b", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Aussage über eine gleichbleibende Komponente aus einer Matrixzeile beurteilen", typ_neben="",
    stichwoerter="e = 3j im Jahr n|dritte Zeile: 0 · b + 0,9 · j + 0,7 · 3j = 3j|Aussage wahr",
    voraussetzungen="eine Zeile der Matrix als Rechenvorschrift|Vektor (x; y; 3y) einsetzen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Population/Altersklassen", textumfang="mittel",
    gegeben="M wie in a; Aussage: sind im Jahr n dreimal so viele erwachsene Tiere wie Jungtiere, so gibt es im nächsten Jahr genauso viele erwachsene Tiere wie im Jahr n",
    gesucht="Beurteilung der Aussage",
    verfahren="dritte Zeile von M auf (x; y; 3y) anwenden",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="(0; 0,9; 0,7) · (x; y; 3y) = 3y; die Aussage ist wahr (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit konkreten Zahlen rechnen, ohne die Allgemeinheit zu zeigen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2025MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag aus einem beobachteten Fixvektor bestimmen", typ_neben="",
    stichwoerter="Zusammensetzung ändert sich nicht: Fixvektor (500; y; 600)|Eintrag Erwachsene → Babys wird a|0,4 · 500 = y ⇒ y = 200|500 = 0,1 · 200 + 600a ⇒ a = 0,8|Kontrolle dritte Zeile: 0,9 · 200 + 0,7 · 600 = 600",
    voraussetzungen="stabile Zusammensetzung als M · v = v|zu ändernden Eintrag aus dem Sachtext bestimmen (Fortpflanzungsrate der Erwachsenen)|lineares Gleichungssystem",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Population/Altersklassen", textumfang="lang",
    gegeben="beobachtete, unveränderliche Population mit 500 Babys und 600 erwachsenen Tieren; neues Modell: nur der Eintrag für die Fortpflanzungsrate der erwachsenen Tiere (Zeile b, Spalte e) wird geändert",
    gesucht="Wert des neuen Eintrags",
    verfahren="M mit Unbekannter a, Fixvektorgleichung mit unbekanntem j, Gleichungssystem lösen",
    schritte="4", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="((0; 0,1; a), (0,4; 0; 0), (0; 0,9; 0,7)) · (500; y; 600) = (500; y; 600); es folgt 500 = 0,1 · y + 600 · a ∧ y = 200 ∧ 0,9 · y + 420 = 600; daraus a = 0,8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="falschen Eintrag ändern (0,7 statt 1,5) oder j unbekannt lassen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) unveränderte Zusammensetzung als Fixvektorgleichung mit zwei Unbekannten übersetzen. Aufgabengruppe A1, außerhalb der Geltung.")

row("2025MgrundlegendBAGLAA1WTR", "a", innen="2", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Rechteck mit Parameter nachweisen und Seitenlänge in Abhängigkeit vom Parameter berechnen", typ_neben="",
    stichwoerter="AB = DC = (3; 0; 0)|AB · BC = (3; 0; 0) · (0; −5; 1 − m) = 0|BC| = √(25 + (1 − m)²)",
    voraussetzungen="Parallelogramm über gleiche Gegenseiten|rechter Winkel über Skalarprodukt|Betrag mit Parameter",
    format="Begründung|Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(−1 | 7 | m), B(2 | 7 | m), C(2 | 2 | 1), D(−1 | 2 | 1), m natürlich",
    gesucht="Nachweis Rechteck und Seitenlänge √(25 + (1 − m)²)",
    verfahren="Vektoren AB, DC, BC; Skalarprodukt; Betrag",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="AB = (3; 0; 0) = DC; AB · BC = (3; 0; 0) · (0; −5; 1 − m) = 0; |BC| = √(0² + (−5)² + (1 − m)²) = √(25 + (1 − m)²) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Parallelogramm-Eigenschaft (AB = DC) weglassen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2025MgrundlegendBAGLAA1WTR", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Parameter aus Seitenlänge und Flächeninhalt eines Rechtecks bestimmen", typ_neben="",
    stichwoerter="|AB| = 3|3 · √(25 + (1 − m)²) = 39 ⇔ (1 − m)² = 144 ⇔ m = 13 (m natürlich)",
    voraussetzungen="Rechteckfläche als Produkt der Seiten|Wurzelgleichung|Lösung m = −11 verwerfen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Rechteck aus 2a; eine Seite hat Länge 3, Flächeninhalt 39",
    gesucht="m",
    verfahren="Flächengleichung nach m auflösen",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="2025MgrundlegendBAGLAA1WTR-2a",
    ergebnis="3 · √(25 + (1 − m)²) = 39 ⇔ (1 − m)² = 144 ⇔ m = 13 (amtlich)",
    zwischenergebnis="m = −11 entfällt (nicht natürlich)", niveau_geschaetzt="II",
    fehlerquelle="1 − m = 12 als einzige Lösung ohne Begründung",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA (A2) WTR 1: Partyzelt
ZELT = "Abb. 1: Schrägbild eines Partyzelts, achteckiges Prisma mit aufgesetzter Pyramide (Dachkanten, Dachflächen, Seitenwände); Abb. 2: derselbe Körper im Koordinatensystem mit A(5 | 0 | 0), B(4 | 3 | 0), C(0 | 5 | 0), D, E, F darüber bei x3 = 3, Spitze S(0 | 0 | 5); Abb. 3: Gitter x1, x2 von −6 bis 6 mit den Strecken C–B–A und der gespiegelten Hälfte links unten"
row("2025MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Symmetrisches Achteck in der Koordinatenebene vervollständigen", typ_neben="",
    stichwoerter="Symmetrie zur x1- und zur x2-Achse|fehlende Ecken (−4 | 3), (−5 | 0), (4 | −3), (0 | −5) ergänzen",
    voraussetzungen="Spiegelung an den Achsen|Achteck schließen",
    format="Zeichnen", operator="Vervollständigen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=ZELT, kontext="Partyzelt", textumfang="lang",
    gegeben="A(5 | 0 | 0), B(4 | 3 | 0), C(0 | 5 | 0); x1x3- und x2x3-Ebene sind Symmetrieebenen; Abbildung 3 zeigt einen Teil der Grundfläche",
    gesucht="vollständige Grundfläche in Abbildung 3",
    verfahren="Ecken an beiden Achsen spiegeln und verbinden",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="regelmäßig wirkendes Achteck mit den Ecken (±5 | 0), (±4 | ±3), (0 | ±5) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Ecke (4 | −3) statt (−4 | −3) links unten setzen",
    bemerkung="Standardbezug: K2 I, K4 I. AB amtlich: I. Amtlich.")

row("2025MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Gesamtlänge der Dachkanten einer Pyramide mit Zuschlag berechnen", typ_neben="",
    stichwoerter="|DS| = |(−5; 0; 2)| = √29|8 · (√29 + 0,6) ≈ 47,88|etwa 48 m",
    voraussetzungen="Kantenlänge als Vektorbetrag|acht gleich lange Kanten|Zuschlag 60 cm je Kante|Maßstab 1 LE = 1 m",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=ZELT, kontext="Partyzelt", textumfang="mittel",
    gegeben="D(5 | 0 | 3), S(0 | 0 | 5); acht gleich lange Dachkanten; Girlande je 60 cm länger als die Kante; 1 LE = 1 m",
    gesucht="Gesamtlänge aller Girlanden",
    verfahren="|DS| berechnen, mal acht, Zuschlag addieren",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="m", abhaengig_von="",
    ergebnis="|DS| = |(−5; 0; 2)| = √29; 8 · √29 + 8 · 0,6 ≈ 47,88; die Gesamtlänge beträgt etwa 48 m (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zuschlag 60 statt 0,6 addieren (Einheit)",
    bemerkung="Standardbezug: K1 I, K2 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Normalenvektor einer Ebene aus zwei Richtungsvektoren über Skalarprodukte bestimmen", typ_neben="",
    stichwoerter="EF = (−4; 2; 0), ES = (−4; −3; 2)|n · EF = 0 und n · ES = 0|n = (1; 2; 5)",
    voraussetzungen="Richtungsvektoren aus Punkten|zwei Skalarprodukte null|eine Komponente frei wählen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=ZELT, kontext="Partyzelt", textumfang="kurz",
    gegeben="E(4 | 3 | 3), F(0 | 5 | 3), S(0 | 0 | 5)",
    gesucht="Normalenvektor der Ebene EFS, rechnerisch",
    verfahren="Skalarprodukte mit zwei Richtungsvektoren null setzen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="aus (n1; n2; n3) · (0; −5; 2) = 0 ∧ n2 = 2 folgt n3 = 5; aus (n1; 2; 5) · (−4; −3; 2) = 0 folgt n1 = 1; Normalenvektor (1; 2; 5) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichenfehler in einem Richtungsvektor",
    bemerkung="Standardbezug: K1 I, K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Geraden und Ebenen: Normalenvektor einer Ebene in Parameterform über Skalarprodukte nachweisen“ getrennt (bestimmen statt nachweisen).")

row("2025MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="n = (1; 2; 5), n_xy = (0; 0; 1)|cos α = 5/√30|α ≈ 24,1°",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=ZELT, kontext="Partyzelt", textumfang="kurz",
    gegeben="Ebene EFS: x1 + 2x2 + 5x3 = 25; x1x2-Ebene ist die Horizontale",
    gesucht="Neigungswinkel der Dachfläche EFS gegen die Horizontale",
    verfahren="Winkelformel mit Normalenvektoren",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="cos α = ((1; 2; 5) · (0; 0; 1)) / (|(1; 2; 5)| · |(0; 0; 1)|) = 5/√30 liefert α ≈ 24,1° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Winkel als 90° − 24,1° angeben",
    bemerkung="Standardbezug: K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")

row("2025MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Lösungsansatz für eine bewegte Gerade durch einen festen Punkt erläutern und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="OP_t = OS + t · SM, t ∈ [0; 1]: Positionen des Strahlers auf der Schiene|x = OP_t + r · (−1; −2; −2): Laserstrahl als Gerade von P_t aus|L auf dieser Geraden ⇔ Strahl dringt durch das Loch",
    voraussetzungen="Parameterdarstellung einer Strecke|Gerade durch Punkt mit Richtungsvektor|Punktprobe als Gleichungssystem in r und t",
    format="Begründung", operator="Erläutern Sie|Deuten Sie", antwort="Text",
    material="Körper", skizze=ZELT, kontext="Partyzelt", textumfang="lang",
    gegeben="Schiene von S(0 | 0 | 5) bis M(2 | 4 | 3); Strahler sendet in Richtung (−1; −2; −2); Loch L(−2 | −4 | 0,5); Ansatz OP_t + r · (−1; −2; −2) = (−2; −4; 0,5) mit OP_t = (0; 0; 5) + t · (2; 4; −2), t ∈ [0; 1]",
    gesucht="Erläuterung der geometrischen Sachverhalte des Ansatzes und Deutung im Sachzusammenhang",
    verfahren="P_t als Strahlerposition, Gerade als Strahl, Gleichung als Bedingung L auf dem Strahl",
    schritte="3", zahlenraum="ganz|dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="die Positionen des Strahlers entlang der Schiene werden durch die Punkte P_t mit OP_t = (0; 0; 5) + t · (2; 4; −2), t ∈ [0; 1], beschrieben; befindet sich der Strahler in P_t, so wird der Laserstrahl durch die Gerade x = OP_t + r · (−1; −2; −2) beschrieben; liegt L auf dieser Geraden, dann dringt der Laserstrahl durch das Loch nach außen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="t und r verwechseln oder das Intervall für t nicht erläutern",
    bemerkung="Standardbezug: K1 II, K2 III, K3 III, K5 II, K6 III. AB amtlich: III. Amtlich. Eichregel: (d) zwei Deutungen verkettet – Streckenparameter als Position und Geradengleichung als Strahl mit Punktprobe.")

# ---- AG/LA (A2) WTR 2: Pyramide über Drachenviereck
DRACHE = "Schrägbild: Pyramide ABCDS, Grundfläche Drachenviereck in der xy-Ebene mit A im Ursprung, B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), Spitze S(0 | 0 | 6) senkrecht über A"
row("2025MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Kürzeste und längste Kante und Volumen einer Pyramide über einem Drachenviereck berechnen", typ_neben="",
    stichwoerter="|AB| = |AD| = 2√2 kürzeste|CS| = |(0; −6; 6)| = 6√2 längste|Drachenfläche 1/2 · 6 · 4 = 12|V = 1/3 · 12 · 6 = 24",
    voraussetzungen="Kantenlängen als Beträge|Drachenfläche aus den Diagonalen|Pyramidenvolumen mit Höhe AS",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="kurz",
    gegeben="A(0 | 0 | 0), B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), S(0 | 0 | 6); ABCD Drachenviereck",
    gesucht="Länge der kürzesten und der längsten Kante, Volumen",
    verfahren="acht Kantenlängen vergleichen, Grundfläche über Diagonalen, Volumen",
    schritte="4", zahlenraum="Wurzel|ganz", einheiten="", abhaengig_von="",
    ergebnis="größte Kantenlänge |CS| = |(0; −6; 6)| = 6√2; kleinste Kantenlänge |AB| = |(2; 2; 0)| = 2√2; Grundfläche 1/2 · 6 · 4 = 12; Volumen 1/3 · 12 · 6 = 24 (amtlich)",
    zwischenergebnis="|BC| = |CD| = 2√5, |AS| = 6, |BS| = |DS| = 2√11", niveau_geschaetzt="I",
    fehlerquelle="Drachenfläche als 6 · 4 ohne den Faktor 1/2",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene durch drei Punkte bestimmen", typ_neben="",
    stichwoerter="BC = (−2; 4; 0), BS = (−2; −2; 6)|n · BC = 0 ∧ n · BS = 0 ⇒ n = (2; 1; 1)|2x + y + z = d, B einsetzen: d = 6",
    voraussetzungen="Richtungsvektoren|Normalenvektor über Skalarprodukte|Punkt einsetzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="kurz",
    gegeben="Seitenfläche BCS in der Ebene E; Kontrolle 2x + y + z = 6",
    gesucht="Koordinatengleichung von E",
    verfahren="Normalenvektor aus zwei Skalarprodukten, d aus B",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(−2; 4; 0) · n = 0 ∧ (−2; −2; 6) · n = 0 ⇔ −2n1 + 4n2 = 0 ∧ −2n1 − 2n2 + 6n3 = 0; n2 = 1 liefert (2; 1; 1); E: 2x + y + z = d, aus B ∈ E folgt d = 6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="d aus dem Ursprung statt aus B bestimmen",
    bemerkung="Standardbezug: K1 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2025MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="n = (2; 1; 1), n_xy = (0; 0; 1)|cos α = 1/√6|α ≈ 65,9°",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="kurz",
    gegeben="E: 2x + y + z = 6",
    gesucht="Winkel zwischen E und der xy-Ebene",
    verfahren="Winkelformel mit Normalenvektoren",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2025MgrundlegendBAGLAA2WTR2-1b",
    ergebnis="cos α = ((2; 1; 1) · (0; 0; 1)) / (|(2; 1; 1)| · |(0; 0; 1)|) = 1/√6 liefert α ≈ 65,9° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Betrag von (2; 1; 1) als √5",
    bemerkung="Standardbezug: K2 I, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")

row("2025MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Ansatz für einen rechten Innenwinkel eines Vierecks über das Skalarprodukt mit unbekannter Koordinate erläutern", typ_neben="",
    stichwoerter="Verschiebung parallel zur y-Achse: B'(2 | y | 0)|AB' = (2; y; 0), CB' = (2; y − 6; 0)|Skalarprodukt null ⇔ rechter Winkel bei B'",
    voraussetzungen="Verschiebung nur in y ändert nur die y-Koordinate|Vektoren von B' zu den Nachbarecken|Orthogonalität über Skalarprodukt",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=DRACHE, kontext="ohne", textumfang="mittel",
    gegeben="B wird parallel zur y-Achse zu B' verschoben, so dass AB'CD in B' einen rechten Innenwinkel hat; Ansatz (2; y; 0) · (2; y − 6; 0) = 0",
    gesucht="Erläuterung des Ansatzes",
    verfahren="B' = (2 | y | 0), Vektoren AB' und CB' erkennen, Skalarprodukt null als rechter Winkel",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Koordinaten von B' können in der Form (2 | y | 0) geschrieben werden; damit gilt (2; y; 0) = AB' und (2; y − 6; 0) = CB'; wenn das Skalarprodukt AB' · CB' gleich null ist, dann ist der Winkel zwischen AB' und CB' ein rechter Winkel (amtlich)",
    zwischenergebnis="y = 3 + √5 ≈ 5,24 (Lösung, nicht verlangt)", niveau_geschaetzt="III",
    fehlerquelle="(2; y − 6; 0) als B'C statt CB' lesen und die Orthogonalität trotzdem behaupten",
    bemerkung="Standardbezug: K1 II, K2 III, K4 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) zwei Deutungen verkettet – Koordinatenform der Verschiebung und Skalarprodukt als rechter Winkel.")

# ---- Stochastik WTR 1: überbelegte Haushalte
BAUMH = "Baumdiagramm: K (28,5 %) / nicht K (71,5 %), darunter B (15,9 % bzw. 6,5 %) und nicht B; Abbildung zu e: fallender Graph von f von (0 | 0,5) bis (0,159 | 0), x-Achse 0 bis 0,16"
row("2025MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="K: mindestens ein Kind (28,5 %), B: überbelegt|P(B | K) = 15,9 %, P(B | nicht K) = 6,5 %|Gegenwahrscheinlichkeiten 71,5 %, 84,1 %, 93,5 %",
    voraussetzungen="zweistufiges Baumdiagramm|Gegenwahrscheinlichkeiten",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Wohnen/Haushalte", textumfang="mittel",
    gegeben="28,5 % der Haushalte mit mindestens einem Kind, davon 15,9 % überbelegt; ohne Kind 6,5 % überbelegt",
    gesucht="beschriftetes Baumdiagramm",
    verfahren="erste Stufe Kind, zweite Stufe überbelegt",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Baumdiagramm mit K (28,5 %), nicht K (71,5 %); B | K 15,9 %, nicht B | K 84,1 %; B | nicht K 6,5 %, nicht B | nicht K 93,5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Stufen vertauschen (überbelegt zuerst)",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A).")

row("2025MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Totale Wahrscheinlichkeit über die Pfadregeln nachweisen", typ_neben="",
    stichwoerter="0,285 · 0,159 + 0,715 · 0,065 ≈ 0,0918",
    voraussetzungen="Pfadmultiplikation und Pfadaddition",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Wohnen/Haushalte", textumfang="kurz",
    gegeben="Baumdiagramm aus a",
    gesucht="Nachweis, dass etwa 9,18 % aller Haushalte überbelegt sind",
    verfahren="beide Pfade zu B addieren",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2025MgrundlegendBStochastikWTR1-1a",
    ergebnis="0,285 · 0,159 + 0,715 · 0,065 ≈ 0,0918 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur den Pfad über K nehmen",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBStochastikWTR1", "c", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen", typ_neben="",
    stichwoerter="E(X) = 1000 · 0,0918 = 91,8|Maximum der Verteilung nahe beim Erwartungswert, also bei 92, nicht 90|Aussage falsch",
    voraussetzungen="Erwartungswert n · p|Maximum in der Nähe des Erwartungswerts",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Wohnen/Haushalte", textumfang="mittel",
    gegeben="X Anzahl überbelegter Haushalte unter 1000, binomialverteilt mit p = 0,0918; Aussage: die Verteilung nimmt für 90 den größten Wert an",
    gesucht="Beurteilung ohne Berechnung von Wahrscheinlichkeiten",
    verfahren="Erwartungswert berechnen und mit 90 vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2025MgrundlegendBStochastikWTR1-1b",
    ergebnis="wegen E(X) = 1000 · 0,0918 = 91,8 ist die Aussage falsch (amtlich)",
    zwischenergebnis="P(X = 92) ≈ 0,0436 > P(X = 90) ≈ 0,0428", niveau_geschaetzt="II",
    fehlerquelle="Wahrscheinlichkeiten doch berechnen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBStochastikWTR1", "d", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kleinstes k mit kumulierter Wahrscheinlichkeit über einer Schranke mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="P(X ≤ 103) ≈ 0,8984 < 0,9|P(X ≤ 104) ≈ 0,9159 > 0,9|k = 104",
    voraussetzungen="kumulierte Verteilung am Rechner|beide Nachbarwerte belegen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Wohnen/Haushalte", textumfang="kurz",
    gegeben="X wie in c; P(X ≤ k) soll mehr als 90 % betragen",
    gesucht="kleinstmögliches k",
    verfahren="kumulierte Wahrscheinlichkeiten um 90 % vergleichen",
    schritte="2", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="2025MgrundlegendBStochastikWTR1-1b",
    ergebnis="P(X ≤ 103) ≈ 0,8984, P(X ≤ 104) ≈ 0,9159 (n = 1000, p = 0,0918); somit ist 104 der kleinstmögliche Wert für k (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="k = 103 angeben (Schranke nicht überschritten)",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBStochastikWTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bayes-Term mit Parameter grafisch lösen und Parameter und Funktionswert im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="f(x) = 0,4 grafisch: x ≈ 0,05|0,159 − x: neuer Anteil überbelegter Haushalte unter denen mit Kind, um x verringert|f(x) = P(K | B): Anteil der Haushalte mit Kind an den überbelegten, 40 %",
    voraussetzungen="Ablesen am Graphen|Term als Bayes-Quotient erkennen|Parameter als Verringerung deuten",
    format="Rechnung|Kurzantwort", operator="Bestimmen Sie|Interpretieren Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=BAUMH, kontext="Wohnen/Haushalte", textumfang="lang",
    gegeben="zwei Jahre später unverändert: 28,5 % mit Kind, 6,5 % überbelegt ohne Kind; f(x) = 0,285 · (0,159 − x) / (0,285 · (0,159 − x) + 0,715 · 0,065), 0 ≤ x ≤ 0,159; Graph in der Abbildung",
    gesucht="x mit f(x) = 0,4 grafisch; Deutung von x und f(x)",
    verfahren="Waagerechte bei 0,4 schneiden, Zähler und Nenner deuten",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="x ≈ 0,05; der Anteil der überbelegten Haushalte an den Haushalten mit mindestens einem Kind hat sich um 0,05 verringert, und der Anteil der Haushalte mit mindestens einem Kind an den überbelegten Haushalten beträgt 40 % (amtlich)",
    zwischenergebnis="rechnerisch x ≈ 0,0503", niveau_geschaetzt="III",
    fehlerquelle="f(x) als Anteil der überbelegten an den Haushalten mit Kind deuten (Richtung der Bedingung)",
    bemerkung="Standardbezug: K1 II, K2 III, K3 III, K4 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Term als Bayes-Quotient und Parameter als Verringerung – zwei Deutungen verkettet.")

# ---- Stochastik WTR 2: Brettspiel
VERTB = "Säulendiagramm P(X = k) ohne Skalen, Säulen von etwa k = 4 bis 30, Maximum in der Mitte (bei 15); Erwartungshorizont trägt 0,12 an der y-Achse und 15 an der k-Achse ein"
row("2025MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeit einer Augensumme beim Wurf zweier Würfel begründen", typ_neben="",
    stichwoerter="Augensumme 8: 5 von 36|Augensumme 9: 4 von 36|5/36 + 4/36 = 1/4",
    voraussetzungen="36 gleich wahrscheinliche Ergebnisse|günstige Paare abzählen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Brettspiel/Würfel", textumfang="mittel",
    gegeben="zwei Würfel mit 1 bis 6; Ereigniskarte bei Augensumme 8 oder 9",
    gesucht="Begründung, dass P(Ereigniskarte) = 1/4",
    verfahren="günstige Ergebnisse zählen, durch 36",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="die Wahrscheinlichkeit für die Augensumme 8 beträgt 5/36, für die Augensumme 9 beträgt sie 4/36; 5/36 + 4/36 = 1/4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="(2; 6) und (6; 2) nur einmal zählen",
    bemerkung="Standardbezug: K1 I, K2 I, K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="(1/4)⁵: fünfmal Ereigniskarte|(3/4)⁵: keinmal|Summe: alle fünf oder keine",
    voraussetzungen="Potenz als Pfad mit gleichen Ausgängen|Summe als Oder",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Brettspiel/Würfel", textumfang="kurz",
    gegeben="erste fünf Spielzüge; Term (1/4)⁵ + (3/4)⁵",
    gesucht="Ereignis im Sachzusammenhang",
    verfahren="beide Summanden als Pfade deuten",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="in den ersten fünf Spielzügen werden fünf Ereigniskarten aufgedeckt oder es wird keine Ereigniskarte aufgedeckt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="(3/4)⁵ als „mindestens eine“ deuten",
    bemerkung="Standardbezug: K2 II, K3 I, K4 II, K6 II. AB amtlich: II. Amtlich. Typ wiederverwendet (Teil A).")

row("2025MgrundlegendBStochastikWTR2", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X ~ B(60; 1/4), P(X < 12) = P(X ≤ 11) ≈ 14,8 %",
    voraussetzungen="„weniger als zwölf“ als X ≤ 11",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Brettspiel/Würfel", textumfang="kurz",
    gegeben="X Anzahl der Ereigniskarten in 60 Spielzügen, p = 1/4",
    gesucht="P(weniger als zwölf)",
    verfahren="kumulierte Verteilung am Rechner",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(X < 12) ≈ 14,8 % (n = 60, p = 1/4) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≤ 12) ≈ 21,6 %",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2025MgrundlegendBStochastikWTR2", "d", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Achsen eines Verteilungsdiagramms über Erwartungswert und größte Einzelwahrscheinlichkeit skalieren", typ_neben="",
    stichwoerter="E(X) = 60 · 1/4 = 15 unter der höchsten Säule|P(X = 15) ≈ 0,12 an der y-Achse",
    voraussetzungen="Erwartungswert als Lage des Maximums|Einzelwahrscheinlichkeit am Rechner",
    format="Rechnung|Eintragen", operator="Skalieren Sie", antwort="Zahl",
    material="Diagramm", skizze=VERTB, kontext="Brettspiel/Würfel", textumfang="mittel",
    gegeben="Abbildung der Verteilung von X ohne Achsenwerte",
    gesucht="je ein geeigneter Wert auf beiden Achsen",
    verfahren="Erwartungswert und zugehörige Wahrscheinlichkeit berechnen und eintragen",
    schritte="2", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="E(X) = 60 · 1/4 = 15; P(X = 15) ≈ 0,12 (n = 60, p = 1/4); Werte an den Achsen unter bzw. neben der höchsten Säule eingetragen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="15 an eine beliebige Säule schreiben",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBStochastikWTR2", "e", innen="1", seite="2", punkte="4", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl der Kombinationen aus zwei getrennten Auswahlgruppen ermitteln", typ_neben="",
    stichwoerter="zwei von drei Landschaften: C(3; 2) = 3|Tiere: ein Symbol (2 Möglichkeiten) oder beide (1): 3|3 · 3 = 9",
    voraussetzungen="Binomialkoeffizient|Fallunterscheidung ein oder zwei Tiersymbole|Produktregel",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Brettspiel/Würfel", textumfang="lang",
    gegeben="drei Landschaftssymbole, zwei Tiersymbole; je Plättchen genau zwei Landschaften und ein oder zwei Tiere, kein Symbol doppelt",
    gesucht="Höchstzahl verschiedener Plättchen",
    verfahren="Landschaftspaare mal Tierauswahlen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="C(3; 2) · (2 + 1) = 9 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Tiere als 2 · 1 = 2 Möglichkeiten (ein Tier zweimal) statt 2 + 1",
    bemerkung="Standardbezug: K2 III, K3 III, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Zählmodell aus den Bedingungen des Sachtexts aufbauen (ein oder zwei Tiersymbole).")

# ---- Stochastik WTR 3: Naturkostkette
row("2025MgrundlegendBStochastikWTR3", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="J: jünger als 50 (0,72), G: Großstadt (0,75), P(J und nicht G) = 0,18|Felder 0,54, 0,21, 0,18, 0,07",
    voraussetzungen="Ränder und Differenzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Naturkostkette/Kundschaft", textumfang="mittel",
    gegeben="72 % jünger als 50 Jahre; 18 % jünger als 50 und nicht in einer Großstadt; 75 % in einer Großstadt",
    gesucht="vollständige Vierfeldertafel",
    verfahren="Ränder eintragen, Felder als Differenzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="G und J 0,54, G und nicht J 0,21, nicht G und J 0,18, nicht G und nicht J 0,07; Ränder 0,75 / 0,25 und 0,72 / 0,28 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="0,18 als P(nicht G) lesen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2025MgrundlegendBStochastikWTR3", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen", typ_neben="",
    stichwoerter="entweder G oder nicht J: (G und J) oder (nicht G und nicht J)|0,54 + 0,07 = 0,61 > 0,6|Aussage falsch",
    voraussetzungen="ausschließendes Oder als zwei Felder|Vergleich mit 60 %",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Tabelle", skizze="Vierfeldertafel aus a", kontext="Naturkostkette/Kundschaft", textumfang="mittel",
    gegeben="Vierfeldertafel aus a; Aussage: P(entweder in Großstadt oder nicht jünger als 50) < 60 %",
    gesucht="Beurteilung",
    verfahren="die beiden passenden Felder addieren",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2025MgrundlegendBStochastikWTR3-1a",
    ergebnis="die Aussage ist falsch, da 0,54 + 0,07 = 0,61 > 0,6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="einschließendes Oder rechnen (0,75 + 0,28 − 0,21 = 0,82)",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2025MgrundlegendBStochastikWTR3", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Σ_{k=40}^{110} C(160; k) · 0,75^k · 0,25^{160−k}|Zufallsexperiment: 160 Personen zufällig auswählen|P(mindestens 40 und höchstens 110 wohnen in einer Großstadt)",
    voraussetzungen="Binomialsumme lesen|n, p und Summationsgrenzen deuten",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Naturkostkette/Kundschaft", textumfang="mittel",
    gegeben="Anteil Großstadt 75 %, Anzahl binomialverteilt; Term Σ_{k=40}^{110} C(160; k) · 0,75^k · 0,25^{160−k}",
    gesucht="Zufallsexperiment und Bedeutung des Terms",
    verfahren="n = 160, p = 0,75, Grenzen 40 und 110 deuten",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Zufallsexperiment: 160 Personen werden zufällig ausgewählt; mit dem Term kann die Wahrscheinlichkeit dafür berechnet werden, dass von 160 zufällig ausgewählten Personen mindestens 40 und höchstens 110 Personen in einer Großstadt wohnen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Grenzen als „mehr als 40“ deuten",
    bemerkung="Standardbezug: K2 II, K4 I, K6 II. AB amtlich: II. Amtlich. Typ wiederverwendet (2026-ga-B).")

row("2025MgrundlegendBStochastikWTR3", "d", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X ~ B(50; 0,1), P(X ≤ 6) ≈ 0,77",
    voraussetzungen="kumulierte Verteilung am Rechner",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Naturkostkette/Brotaufstrich", textumfang="lang",
    gegeben="Kiste mit 50 Gläsern, Mangel mit 10 % je Glas",
    gesucht="Nachweis P(höchstens sechs Gläser mit Mangel) ≈ 0,77",
    verfahren="P(X ≤ 6) am Rechner",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="X Anzahl der Gläser in der Kiste mit Mangel; P(X ≤ 6) ≈ 0,77 (n = 50, p = 0,1) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X < 6)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2025MgrundlegendBStochastikWTR3", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="Gewinn je Glas: x − 2 mit 0,77, 0,5x − 2 mit 0,17, −2 mit 0,06|(x − 2) · 0,77 + (0,5x − 2) · 0,17 − 2 · 0,06 ≥ 0,5|0,855x − 2 ≥ 0,5 ⇔ x ≥ 500/171 ≈ 2,9239|Preis 2,93 €",
    voraussetzungen="Gewinn je Fall als Preis minus Kosten|Erwartungswert als gewichtete Summe|Ungleichung lösen, auf Cent aufrunden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Naturkostkette/Brotaufstrich", textumfang="lang",
    gegeben="Kosten 2,00 € je Glas; volle Zahlung bei höchstens sechs Mängeln (0,77), halbe bei sieben oder acht (0,17), sonst nichts; Gewinn im Mittel mindestens 0,50 € je Glas",
    gesucht="geringster Preis je Glas auf Cent genau",
    verfahren="Erwartungswert des Gewinns je Glas in x aufstellen, Ungleichung lösen",
    schritte="4", zahlenraum="dezimal|Bruch", einheiten="€", abhaengig_von="",
    ergebnis="x Preis je Glas in €: (x − 2) · 0,77 + (0,5 · x − 2) · 0,17 − 2 · (1 − 0,77 − 0,17) ≥ 0,5 ⇔ 0,855 · x − 2 ≥ 0,5 ⇔ x ≥ 500/171 ≈ 2,9239; Preis pro Glas 2,93 € (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Kosten nur in den bezahlten Fällen abziehen oder auf 2,92 € abrunden",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) gestaffelte Bezahlung in einen Erwartungswertterm des Gewinns übersetzen. Typ wiederverwendet (Teil A).")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Extremstellen berechnen und Monotonieverhalten angeben", "Analysis", "Kurvenuntersuchung",
     "Die Extremstellen einer Funktion über die Nullstellen der Ableitung berechnen und die Monotoniebereiche angeben.",
     "2025MgrundlegendBAnalysisWTR1-1a"),
    ("Weiteren Schnittpunkt von Tangente und Graph aus einer vorgegebenen Faktorisierung begründen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Mit einer vorgegebenen Faktorisierung von f(x) − t(x) begründen, wie viele weitere gemeinsame Punkte Tangente und Graph neben dem Berührpunkt haben.",
     "2025MgrundlegendBAnalysisWTR1-1c"),
    ("Integralwert: Lösung einer Integralgleichung über die Punktsymmetrie und ein Rechteck am Graphen begründen", "Analysis", "Flächeninhalt durch Integration",
     "Ohne Rechnung die Lösung einer Gleichung ∫_k^{k+1} f = c angeben und über die Punktsymmetrie des Graphen und ein eingezeichnetes Rechteck begründen.",
     "2025MgrundlegendBAnalysisWTR1-1d"),
    ("Extrempunkte: Hochpunkt aus dem Graphen ablesen und im Sachzusammenhang deuten", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Koordinaten eines Hochpunkts aus der Abbildung ablesen und beide Koordinaten im Sachzusammenhang deuten.",
     "2025MgrundlegendBAnalysisWTR1-2a"),
    ("Nullstellen und Werte: Bereich mit Funktionswerten über einer Schranke aus dem Graphen bestimmen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Eine Sachbedingung als f(x) > c lesen und den zugehörigen Bereich der x-Werte am Graphen ablesen.",
     "2025MgrundlegendBAnalysisWTR1-2b"),
    ("Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben", "Analysis", "Grenzwerte und Verhalten im Unendlichen",
     "Für ein Produkt aus linearem Faktor und e-Funktion die Nullstelle und das Verhalten für x → ±∞ angeben.",
     "2025MgrundlegendBAnalysisWTR2-1a"),
    ("Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen", "Analysis", "Kurvenuntersuchung",
     "Den Hochpunkt eines Produkts aus Polynom und e-Funktion mit der Produktregel berechnen (Art aus der Abbildung).",
     "2025MgrundlegendBAnalysisWTR2-1b"),
    ("Integralwert: Näherungswert eines Integrals als Dreiecksfläche am Graphen begründen", "Analysis", "Flächeninhalt durch Integration",
     "Einen vorgegebenen Term als Flächeninhalt eines in die Abbildung eingezeichneten Dreiecks deuten und als Näherung des Integrals begründen.",
     "2025MgrundlegendBAnalysisWTR2-1c"),
    ("Prozentuale Abweichung eines Näherungswerts vom exakten Wert berechnen", "Analysis", "Stammfunktion und Hauptsatz",
     "Die relative Abweichung eines Näherungswerts vom exakten Integralwert in Prozent berechnen (Nebenleistung).",
     "2025MgrundlegendBAnalysisWTR2-1d"),
    ("Verlauf eines Graphen im Sachzusammenhang beschreiben", "Analysis", "Kurvenuntersuchung",
     "Monotonie, Krümmungswechsel und Sättigung eines abgebildeten Graphen in Worten des Sachzusammenhangs beschreiben.",
     "2025MgrundlegendBAnalysisWTR2-2a"),
    ("Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen", "Analysis", "Ableitung und Änderungsrate",
     "Für ein Zeitintervall die Werte am Graphen ablesen und den Differenzenquotienten als Durchschnitt je Zeiteinheit berechnen.",
     "2025MgrundlegendBAnalysisWTR2-2b"),
    ("Funktionalgleichung mit Zeitverschiebung grafisch lösen und im Sachzusammenhang deuten", "Analysis", "Gleichungen lösen",
     "Eine Gleichung der Form a(x + c) = a(x) + d am Graphen lösen (zwei Graphenpunkte mit festem Abstand in x und y) und im Sachzusammenhang deuten.",
     "2025MgrundlegendBAnalysisWTR2-2c"),
    ("Übergangsprozess: Aussage über eine gleichbleibende Komponente aus einer Matrixzeile beurteilen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine Aussage, dass eine Komponente unter einer Bedingung an den Vektor gleich bleibt, über eine Zeile der Übergangsmatrix allgemein beurteilen.",
     "2025MgrundlegendBAGLAA1WTR-1b"),
    ("Übergangsprozess: Matrixeintrag aus einem beobachteten Fixvektor bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen zu ändernden Eintrag der Übergangsmatrix so bestimmen, dass ein beobachteter, teilweise bekannter Vektor Fixvektor wird.",
     "2025MgrundlegendBAGLAA1WTR-1c"),
    ("Ebene Figur: Rechteck mit Parameter nachweisen und Seitenlänge in Abhängigkeit vom Parameter berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Ein Viereck mit Parameterkoordinaten als Rechteck nachweisen (Gegenseiten gleich, Skalarprodukt null) und eine Seitenlänge als Term im Parameter berechnen.",
     "2025MgrundlegendBAGLAA1WTR-2a"),
    ("Ebene Figur: Parameter aus Seitenlänge und Flächeninhalt eines Rechtecks bestimmen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Parameter eines Rechtecks aus einer bekannten Seitenlänge und dem Flächeninhalt über eine Wurzelgleichung bestimmen.",
     "2025MgrundlegendBAGLAA1WTR-2b"),
    ("Ebene Figur: Symmetrisches Achteck in der Koordinatenebene vervollständigen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Eine zu beiden Koordinatenachsen symmetrische ebene Figur aus einem gegebenen Teil im Gitter vervollständigen.",
     "2025MgrundlegendBAGLAA2WTR1-1a"),
    ("Körper: Gesamtlänge der Dachkanten einer Pyramide mit Zuschlag berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Die Länge einer Kante als Vektorbetrag berechnen und mit Anzahl und Zuschlag zur Gesamtlänge im Sachzusammenhang hochrechnen.",
     "2025MgrundlegendBAGLAA2WTR1-1b"),
    ("Normalenvektor einer Ebene aus zwei Richtungsvektoren über Skalarprodukte bestimmen", "Analytische Geometrie", "Ebenen",
     "Einen Normalenvektor einer durch drei Punkte gegebenen Ebene rechnerisch bestimmen, indem zwei Skalarprodukte null gesetzt werden.",
     "2025MgrundlegendBAGLAA2WTR1-1c"),
    ("Lösungsansatz für eine bewegte Gerade durch einen festen Punkt erläutern und im Sachzusammenhang deuten", "Analytische Geometrie", "Geraden",
     "Einen vorgelegten Ansatz mit Streckenparameter und Geradenparameter erläutern: Positionen auf einer Strecke, Gerade von jeder Position aus, Punktprobe eines festen Punktes; im Sachzusammenhang deuten.",
     "2025MgrundlegendBAGLAA2WTR1-1e"),
    ("Körper: Kürzeste und längste Kante und Volumen einer Pyramide über einem Drachenviereck berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Alle Kantenlängen einer Pyramide vergleichen und das Volumen über die Drachenfläche (halbes Diagonalenprodukt) und die Höhe berechnen.",
     "2025MgrundlegendBAGLAA2WTR2-1a"),
    ("Ebene Figur: Ansatz für einen rechten Innenwinkel eines Vierecks über das Skalarprodukt mit unbekannter Koordinate erläutern", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Einen vorgelegten Ansatz erläutern, in dem ein verschobener Eckpunkt mit unbekannter Koordinate angesetzt und der rechte Winkel über das Skalarprodukt der Nachbarseiten ausgedrückt wird.",
     "2025MgrundlegendBAGLAA2WTR2-1d"),
    ("Totale Wahrscheinlichkeit über die Pfadregeln nachweisen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Eine vorgegebene Gesamtwahrscheinlichkeit als Summe der Pfadwahrscheinlichkeiten nachweisen.",
     "2025MgrundlegendBStochastikWTR1-1b"),
    ("Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen", "Stochastik", "Binomialverteilung",
     "Ohne Wahrscheinlichkeitsrechnung beurteilen, ob die Binomialverteilung an einer genannten Stelle ihr Maximum hat, über den Erwartungswert n · p.",
     "2025MgrundlegendBStochastikWTR1-1c"),
    ("Kleinstes k mit kumulierter Wahrscheinlichkeit über einer Schranke mit dem Rechner ermitteln", "Stochastik", "Binomialverteilung",
     "Das kleinste k ermitteln, für das P(X ≤ k) eine vorgegebene Schranke überschreitet, mit beiden Nachbarwerten am Rechner.",
     "2025MgrundlegendBStochastikWTR1-1d"),
    ("Bayes-Term mit Parameter grafisch lösen und Parameter und Funktionswert im Sachzusammenhang deuten", "Stochastik", "Bedingte Wahrscheinlichkeit und Bayes",
     "Am Graphen eines Bayes-Quotienten mit Parameter die Stelle zu einem Funktionswert ablesen und Parameter (Änderung eines Anteils) und Funktionswert (bedingter Anteil) im Sachzusammenhang deuten.",
     "2025MgrundlegendBStochastikWTR1-1e"),
    ("Laplace-Experiment: Wahrscheinlichkeit einer Augensumme beim Wurf zweier Würfel begründen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Die Wahrscheinlichkeit für bestimmte Augensummen beim Wurf zweier Würfel über das Abzählen der günstigen unter 36 Ergebnissen begründen.",
     "2025MgrundlegendBStochastikWTR2-1a"),
    ("Achsen eines Verteilungsdiagramms über Erwartungswert und größte Einzelwahrscheinlichkeit skalieren", "Stochastik", "Binomialverteilung",
     "In einem unbeschrifteten Säulendiagramm einer Binomialverteilung je einen Achsenwert eintragen: Erwartungswert unter der höchsten Säule und deren Wahrscheinlichkeit.",
     "2025MgrundlegendBStochastikWTR2-1d"),
    ("Anzahl der Kombinationen aus zwei getrennten Auswahlgruppen ermitteln", "Stochastik", "Kombinatorik",
     "Die Anzahl der Möglichkeiten ermitteln, wenn aus zwei Symbolgruppen unabhängig ausgewählt wird (Binomialkoeffizient mal Fallsumme).",
     "2025MgrundlegendBStochastikWTR2-1e"),
    ("Aussage über ein Entweder-oder-Ereignis aus der Vierfeldertafel beurteilen", "Stochastik", "Vierfeldertafel",
     "Ein ausschließendes Oder als Summe zweier Felder der Vierfeldertafel berechnen und eine Aussage darüber beurteilen.",
     "2025MgrundlegendBStochastikWTR3-1b"),
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
    t = t.replace(MARKE_KONTEXT.lower(), " ")  # feste Markierung, bewusst umlautfrei (v0.7)
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
    # Trägerbindung: nur die feste Markierung am Feldanfang, keine andere Schreibweise (v0.7)
    b = z["bemerkung"]
    a("Trägerbindung" not in b and "Traegerbindung: frei" not in b,
      f"{i}: Trägerbindung nur als „{MARKE_KONTEXT}“ am Anfang von bemerkung (kein Vermerk heißt frei)")
    if MARKE_KONTEXT.lower() in b.lower():
        a(b.startswith(MARKE_KONTEXT) and (b[len(MARKE_KONTEXT):len(MARKE_KONTEXT) + 1] in (".", " ")),
          f"{i}: Markierung „{MARKE_KONTEXT}“ muss am Anfang von bemerkung stehen, gefolgt von Punkt oder Klammer")
    if z["block"] == "B":
        m = AB_SPALTE.search(b)
        a(m is not None, f"{i}: Teil B braucht „AB amtlich: I|II|III.“ in bemerkung (Spalte Anforderungsbereich)")
        if m and z["afb_amtlich"]:
            a(ORD[m.group(1)] == hoechster_afb(z["afb_amtlich"]) or AB_HINWEIS in b,
              f"{i}: Spalte Anforderungsbereich ≠ höchster Kompetenzeintrag, bemerkung braucht „{AB_HINWEIS}“")
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
        # id und abhaengig_von tragen in Teil B den Bindestrich vor der Aufgabennummer (…WTR1-2a), v0.6
        a(k in ("id", "abhaengig_von") or not re.search(r"(?<=[\d\s(])-(?=\d)", v),
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
# Teil B: der Standardbezug hat eine eigene Spalte Anforderungsbereich; sie steht in
# bemerkung als „AB amtlich: III" und ist für die Eichung maßgeblich (iqb.md § 4, v0.7).
AB_SPALTE = re.compile(r"AB amtlich: (I{1,3})\.")
AB_HINWEIS = "Anforderungsbereich weicht vom höchsten Kompetenzeintrag ab"
# Trägerbindung (iqb.md § 7): feste Markierung am Anfang von bemerkung, kein eigenes Feld.
MARKE_KONTEXT = "Traegerbindung: Kontext"


def amtlich_von(z):
    """Amtlicher Bereich für die Eichung: Teil A das Maximum über afb_amtlich, Teil B die
    Spalte Anforderungsbereich aus bemerkung."""
    if z["block"] == "B":
        m = AB_SPALTE.search(z["bemerkung"])
        return ORD[m.group(1)] if m else 0
    return hoechster_afb(z["afb_amtlich"])


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
        amt = amtlich_von(z)
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
        stapel = {einheit(QUELLE[k]) for k in kennungen if k in QUELLE}
        for s in sorted(stapel):
            fehlt = [k for k, q in QUELLE.items()
                     if einheit(q) == s and not q["dublette_von"] and k not in kennungen]
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
    im_stapel = {k for k, q in QUELLE.items() if einheit(q) == stapel}
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
