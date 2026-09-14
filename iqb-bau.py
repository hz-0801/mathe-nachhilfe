# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.9 · 15.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v1.0

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

Änderungen gegenüber 0.8 (Entscheidung des Lehrers, 15.09.2026: MMS/CAS als
Delta): Die Erfassungseinheit „Stapel je Rechnerfassung" bleibt für WTR; für
einen mms-/cas-Stapel gilt: vollständig sind die nicht wortgleichen Dateien,
das Soll rechnet nur gegen sie. Wortgleiche Dateien stehen in iqb-quellen.csv
(v0.3, Textvergleich des Abschnitts „1 Aufgabe") mit dublette_von auf die
WTR-Datei und bekommen keine Zeile – dieselbe Mechanik wie bei den A1/A2-Paaren
in Teil A. Neu geprüft: die erste Datei einer Dublette muss im Katalog stehen
(im Stapellauf und in der Selbstprüfung), damit der WTR-Zweig vor dem
MMS-Zweig erfasst ist.

Änderungen gegenüber 0.7 (2024-ga-B): In Teil B darf eine nummerierte Aufgabe
ohne Teilaufgabenbuchstaben stehen (erstmals 2024-ga-B Stochastik WTR 2,
Aufgabe 3): row(kennung, "", innen="3") ergibt id Kennung-3, teilaufgabe leer.
Die Prüfung „ungegliederte Aufgabe neben gegliederten Zeilen" gilt je
Aufgabennummer, nicht je Datei.

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
    "stapel": "2022-ea-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2022MerhoehtBAnalysisWTR1": 40,
        "2022MerhoehtBAnalysisWTR2": 40,
        "2022MerhoehtBAnalysisWTR3": 40,
        "2022MerhoehtBAGLAA1WTR": 25,
        "2022MerhoehtBAGLAA2WTR1": 25,
        "2022MerhoehtBAGLAA2WTR2": 25,
        "2022MerhoehtBStochastikWTR1": 25,
        "2022MerhoehtBStochastikWTR2": 25,
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
# Stapel 2022-ea-B, WTR-Zweig. innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Pool 2022 erhöht: Analysis 40 BE, AG/LA und Stochastik 25 BE.

SOLL = {"2022MerhoehtBAnalysisWTR1": 40, "2022MerhoehtBAnalysisWTR2": 40, "2022MerhoehtBAnalysisWTR3": 40,
        "2022MerhoehtBAGLAA1WTR": 25, "2022MerhoehtBAGLAA2WTR1": 25, "2022MerhoehtBAGLAA2WTR2": 25,
        "2022MerhoehtBStochastikWTR1": 25, "2022MerhoehtBStochastikWTR2": 25}

# ---- Analysis WTR 1, Aufgabe 1: ICE, f(x) = 30x³ − 90x² + 240, Schar f_p
IC = "Abbildung 1: Koordinatensystem x von −1 bis 3, y mit Marken 100 und 200; waagerechte Linie bei 240 für x < 0, Graph von f von (0 | 240) fallend mit Wendepunkt bei x = 1 bis (2 | 120), danach waagerecht bei 120; Abbildung 2 zusätzlich mit G₂₅₀ (gestrichelt, zunächst über f mit Hochpunkt, dann steil fallend) und G₋₈₀ (gestrichelt, unter f)"
row("2022MerhoehtBAnalysisWTR1", "a", innen="1", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert und Änderungsbeträge zweier Zeitabschnitte im Sachzusammenhang vergleichen", typ_neben="",
    stichwoerter="f(0,5) = 221,25 ≈ 220 km/h|f(0) − f(0,5) = 18,75|f(0,5) − f(1) = 41,25",
    voraussetzungen="Funktionswerte|Differenzen bilden und vergleichen",
    format="Rechnung", operator="Bestimmen Sie|Zeigen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=IC, kontext="Bahn/ICE-Geschwindigkeit", textumfang="lang",
    gegeben="f(x) = 30x³ − 90x² + 240, x Minuten seit 15:00 Uhr, f(x) Geschwindigkeit in km/h für 0 ≤ x ≤ 2; davor und danach konstante Geschwindigkeit",
    gesucht="Geschwindigkeit nach einer halben Minute; Nachweis, dass die Abnahme in der ersten halben Minute kleiner ist als in der zweiten",
    verfahren="f(0,5) berechnen, beide Differenzen bilden und vergleichen",
    schritte="3", zahlenraum="dezimal", einheiten="km/h", abhaengig_von="",
    ergebnis="f(0,5) = 221,25, die Geschwindigkeit beträgt etwa 220 km/h; f(0) − f(0,5) = 18,75, f(0,5) − f(1) = 41,25 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Ableitungswerte statt Differenzen vergleichen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR1", "b", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen", typ_neben="",
    stichwoerter="f'(x) = 90x² − 180x = 90x(x − 2)|Parabel mit Minimum in der Mitte der Nullstellen 0 und 2|x = 1, 15:01 Uhr",
    voraussetzungen="Ableitung|Minimum einer quadratischen Funktion|stärkste Abnahme als minimale Ableitung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=IC, kontext="Bahn/ICE-Geschwindigkeit", textumfang="kurz",
    gegeben="f wie in a",
    gesucht="Zeitpunkt der stärksten Abnahme der Geschwindigkeit",
    verfahren="f' aufstellen, Minimum von f' über die Nullstellensymmetrie oder f'' = 0",
    schritte="3", zahlenraum="ganz", einheiten="Uhr", abhaengig_von="",
    ergebnis="f'(x) = 90x² − 180x = 90x · (x − 2); f' ist quadratisch mit Minimum, die Nullstellen 0 und 2 liefern das Minimum bei x = 1; der gesuchte Zeitpunkt ist 15:01 Uhr (amtlich)",
    zwischenergebnis="f''(x) = 180x − 180", niveau_geschaetzt="II",
    fehlerquelle="Nullstelle von f' (x = 2) als stärkste Abnahme",
    bemerkung="Standardbezug: K1 I, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR1", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zurückgelegte Strecke als Integral der Geschwindigkeit mit Umrechnung der Einheiten berechnen", typ_neben="",
    stichwoerter="1/60 · ∫₀² f(x) dx|Stammfunktion 15/2x⁴ − 30x³ + 240x|6 km",
    voraussetzungen="Strecke als Integral der Geschwindigkeit|Minuten in Stunden (Faktor 1/60)",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bahn/ICE-Geschwindigkeit", textumfang="kurz",
    gegeben="f wie in a; erste zwei Minuten",
    gesucht="Länge der zurückgelegten Strecke",
    verfahren="Integral von 0 bis 2 über f, mit 1/60 in km umrechnen",
    schritte="3", zahlenraum="Bruch", einheiten="km", abhaengig_von="",
    ergebnis="1/60 · ∫₀² f(x) dx = 1/60 · [15/2x⁴ − 30x³ + 240x]₀² = 6; der ICE legt sechs Kilometer zurück (amtlich)",
    zwischenergebnis="Integral 360", niveau_geschaetzt="II",
    fehlerquelle="Faktor 1/60 vergessen (360 km)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR1", "d", innen="1", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Aussage über den Bremsweg bei konstanter Abnahme über die Tangente und ein Dreieck untersuchen", typ_neben="",
    stichwoerter="f'(1) = −90, f(1) = 180|Tangente y = −90x + 270 mit Nullstelle 3|Dreieck zwischen x = 1, x-Achse und Tangente: 1/2 · 2 · 180 / 60 = 3 km|Aussage richtig",
    voraussetzungen="Tangente als Modell konstanter Abnahme|Nullstelle der Tangente als Stillstand|Dreiecksfläche als Strecke mit Umrechnung",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=IC, kontext="Bahn/ICE-Geschwindigkeit", textumfang="mittel",
    gegeben="Aussage: Bliebe die Abnahme der Geschwindigkeit ab 15:01 Uhr konstant, käme der ICE nach drei Kilometern zum Stehen",
    gesucht="ob die Aussage richtig ist",
    verfahren="Tangente in (1 | f(1)) aufstellen, Nullstelle bestimmen, Fläche unter der Tangente bis dorthin in km umrechnen",
    schritte="4", zahlenraum="ganz|negativ", einheiten="km", abhaengig_von="",
    ergebnis="f'(1) = −90, f(1) = 180; Tangente y = −90x + 270 mit der Nullstelle 3; sie schließt mit der x-Achse und der Geraden x = 1 eine Fläche mit dem Inhalt 1/2 · 2/60 · f(1) = 3 ein, die Aussage ist richtig (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Nullstelle 3 als drei Kilometer statt als Zeitpunkt lesen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) konstante Abnahme als Tangente deuten, verkettet mit Stillstand und Strecke als Fläche.")

row("2022MerhoehtBAnalysisWTR1", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Bedingungen für den sprungfreien Übergang von Funktionswert und Ableitung angeben", typ_neben="",
    stichwoerter="f_p(0) = 240|f_p'(0) = 0",
    voraussetzungen="Stetiger Anschluss an eine Konstante|Anschluss der Steigung an null",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Koordinatensystem", skizze=IC, kontext="Bahn/ICE-Geschwindigkeit", textumfang="mittel",
    gegeben="f_p(x) = p/4 · x⁴ + (30 − p)x³ + (p − 90)x² + 240, p ∈ IR; Übergang bei 15:00 Uhr ohne Sprung in Geschwindigkeit und Änderungsrate",
    gesucht="die beiden Bedingungen, die f_p erfüllen",
    verfahren="Werte der konstanten Fahrt vor 15:00 Uhr (240, Rate 0) an der Stelle 0 fordern",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_p(0) = 240, f_p'(0) = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Bedingungen an der Stelle 2 statt 0",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II („ohne Sprung“ in Bedingungen an f_p und f_p' übersetzen), amtlich I.")

row("2022MerhoehtBAnalysisWTR1", "f", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter der Ausgangsfunktion angeben und Eignung zweier Scharfunktionen am Graphen beurteilen", typ_neben="",
    stichwoerter="p = 0|G₂₅₀ hat für 0 < x < 2 einen Extrempunkt (Geschwindigkeit nähme zu)|G₋₈₀ nicht ⇒ nur f₋₈₀ passend",
    voraussetzungen="Term vergleichen|Monotonie am Graphen lesen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=IC, kontext="Bahn/ICE-Geschwindigkeit", textumfang="mittel",
    gegeben="f_p wie in e; Abbildung 2 mit G₋₈₀ und G₂₅₀",
    gesucht="p mit f_p = f; Eignung von f₋₈₀ und f₂₅₀ anhand der Graphen",
    verfahren="p = 0 ablesen; Graphen auf Extrempunkte im Intervall prüfen (Geschwindigkeit muss abnehmen)",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="p = 0; der Graph von f₂₅₀ hat für 0 < x < 2 einen Extrempunkt, der von f₋₈₀ nicht, damit könnte nur f₋₈₀ die Geschwindigkeitsentwicklung passend beschreiben (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="f₂₅₀ wegen des Anschlusses an 120 bei x = 2 für passend halten",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (Extremstellen 0,64 bzw. 2,125).")

row("2022MerhoehtBAnalysisWTR1", "g", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Eignung der Scharfunktionen über die Lage einer dritten Extremstelle beurteilen", typ_neben="",
    stichwoerter="f_p' hat Nullstellen 0, 2 und x₃ = 1 − 90/p|x₃ ≤ 0 ⇔ 0 < p ≤ 90, x₃ ≥ 2 ⇔ −90 ≤ p < 0|nur für −90 ≤ p < 0 und 0 < p ≤ 90 kein Extremum in ]0; 2[",
    voraussetzungen="Extremstelle außerhalb des Intervalls als Bedingung|gegebene Informationen verknüpfen|Fallunterscheidung nach dem Vorzeichen von p",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=IC, kontext="Bahn/ICE-Geschwindigkeit", textumfang="lang",
    gegeben="Für p ≠ 0: f_p'(x) = 0 hat neben 0 und 2 die Lösung x₃ = 1 − 90/p; x₃ ≤ 0 ⇔ 0 < p ≤ 90, x₃ ≥ 2 ⇔ −90 ≤ p < 0",
    gesucht="Beurteilung der Eignung von f_p mit p ≠ 0",
    verfahren="Eignung heißt kein Extremum in ]0; 2[, also x₃ außerhalb; Bedingungen an p übernehmen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Für p ≠ 0 nimmt f_p nur für −90 ≤ p < 0 und 0 < p ≤ 90 im Bereich 0 < x < 2 kein Extremum an; nur für diese Werte könnten die Funktionen die Geschwindigkeitsentwicklung passend beschreiben (amtlich)",
    zwischenergebnis="Kontrolle: p = 45 liefert x₃ = −1, p = 250 liefert 0,64", niveau_geschaetzt="III",
    fehlerquelle="Randwerte p = ±90 (x₃ = 0 bzw. 2 ohne Extremum im offenen Intervall) ausschließen",
    bemerkung="Standardbezug: K1 III, K3 III, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Eignung in eine Bedingung an die dritte Extremstelle übersetzen, verkettet mit der Fallunterscheidung.")

# ---- Analysis WTR 1, Aufgabe 2: s(x) = a sin(bx) + 1 mit Extrempunkten E₁(−2|−1), E₂(2|3)
SI = "Abbildung 3: Koordinatensystem mit Sinuskurve s durch (−2 | −1) Tiefpunkt, (0 | 1), (2 | 3) Hochpunkt, (4 | 1); Quadrat mit Ecken (0 | 0), (2 | 0), (2 | 2), (0 | 2) eingezeichnet; Flächenstücke zwischen Graph und x-Achse über [−2; 2] schraffiert (A₁ unter der Achse links, A₂ und A₃ im Quadrat, A₄ über dem Quadrat)"
row("2022MerhoehtBAnalysisWTR1", "a", innen="2", seite="3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Parameter einer Sinusfunktion aus zwei aufeinanderfolgenden Extrempunkten bestimmen", typ_neben="",
    stichwoerter="Amplitude a = (3 − (−1))/2 = 2|halbe Periode 4 ⇒ Periode 8|b = 2π/8 = π/4",
    voraussetzungen="Amplitude aus Hoch- und Tiefpunkt|Periode aus dem Abstand aufeinanderfolgender Extremstellen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="s(x) = a · sin(b · x) + 1; E₁(−2 | −1) und E₂(2 | 3) direkt aufeinanderfolgende Extrempunkte; Kontrolle a = 2, b = π/4",
    gesucht="a und b",
    verfahren="Amplitude als halbe Differenz der Extremwerte, b aus der Periode",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="a = 3 − 1 = 2, b = π/(2 − (−2)) = 1/4 · π (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Abstand der Extremstellen als ganze Periode nehmen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR1", "b", innen="2", seite="3", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integralwert über die Punktsymmetrie und ein Quadrat geometrisch begründen", typ_neben="",
    stichwoerter="Graph punktsymmetrisch zu (0 | 1)|A₁ = A₄, A₂ = A₃|Flächenstücke ergänzen sich zum Quadrat 2 × 2|Integral = 4",
    voraussetzungen="Symmetrie um den Wendepunkt|Vorzeichen von Flächen unter der Achse|Umlegen von Flächenstücken",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=SI, kontext="ohne", textumfang="mittel",
    gegeben="∫₋₂² s(x) dx = 4; Abbildung 3 mit Quadrat und Flächenstücken A₁ bis A₄",
    gesucht="geometrische Begründung des Werts mithilfe der Abbildung",
    verfahren="Punktsymmetrie zu (0 | 1) nutzen: A₁ und A₄ gleich groß, A₂ und A₃ gleich groß, Lage zur Achse und zum Quadrat ergibt das Quadrat",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2022MerhoehtBAnalysisWTR1-2a",
    ergebnis="Der Graph ist symmetrisch bezüglich (0 | 1); damit haben A₁ und A₄ sowie A₂ und A₃ jeweils gleichen Inhalt; wegen ihrer Lage bezüglich der x-Achse und des Quadrats stimmt der Integralwert mit dem Flächeninhalt des Quadrats überein, ist also 2² = 4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="A₁ mit positivem Vorzeichen addieren",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR1", "c", innen="2", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendestellen einer Sinusfunktion als ganzzahlig nachweisen und die beiden Wendetangentensteigungen zeigen", typ_neben="",
    stichwoerter="s(x) = 1 ⇔ sin(π/4 x) = 0 ⇔ x = 4k, k ∈ ZZ|s'(x) = π/2 cos(π/4 x)|s'(4k) = ±π/2",
    voraussetzungen="Nullstellen des Sinus|Kettenregel|Kosinus an Vielfachen von π",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Wendepunkte sind die Punkte mit y-Koordinate 1",
    gesucht="Nachweis ganzzahliger Wendestellen; Steigung dort −π/2 oder +π/2",
    verfahren="s(x) = 1 lösen, Ableitung an den Wendestellen auswerten",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2022MerhoehtBAnalysisWTR1-2a",
    ergebnis="s(x) = 1 ⇔ sin(π/4 · x) = 0 ⇔ π/4 · x = k · π ⇔ x = 4k, k ∈ ZZ; s'(x) = π/2 · cos(π/4 · x) liefert für alle k: s'(4k) = −π/2 ∨ s'(4k) = π/2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="innere Ableitung π/4 vergessen",
    bemerkung="Standardbezug: K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR1", "d", innen="2", seite="3", punkte="3", afb_amtlich="III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente durch einen entfernten Punkt über die Rationalität der Steigung ausschließen", typ_neben="",
    stichwoerter="Wendepunkte (4k | 1)|Steigung der Geraden zu P(2022 | 2022): 2021/(2022 − 4k)|rational, Tangentensteigung ±π/2 irrational ⇒ keine Tangente",
    voraussetzungen="Steigung durch zwei Punkte|rational gegen irrational unterscheiden",
    format="Begründung|Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Geraden durch je einen Wendepunkt und P(2022 | 2022)",
    gesucht="ob eine dieser Geraden im Wendepunkt Tangente ist",
    verfahren="Steigung der Geraden allgemein in k, mit ±π/2 vergleichen",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2022MerhoehtBAnalysisWTR1-2c",
    ergebnis="Die Wendepunkte haben die Koordinaten (4k | 1), die Geraden die Steigungen 2021/(2022 − 4k); die Tangenten haben Steigung −π/2 oder +π/2; da 2021/(2022 − 4k) für jedes k rational ist, ist keine der Geraden Tangente (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="einzelne k durchprobieren statt allgemein argumentieren",
    bemerkung="Standardbezug: K1 III, K2 III, K5 I, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis über die Rationalität.")

# ---- Analysis WTR 2: f(x) = x · e^(−x²/2 + 1/2), Schar f_a
GF = "Abbildung 1: Graph von f ohne Koordinatensystem – von links nahe null kommend, Tiefpunkt, steiler Anstieg durch die Mitte, Hochpunkt, dann fallend gegen null (punktsymmetrische Form); Abbildung 2: Graph der Gruppe I (zwei Extrempunkte, Achsen −1 bis 1); Abbildung 3: Graph der Gruppe II (streng monoton steigend, ohne Extrempunkte)"
row("2022MerhoehtBAnalysisWTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Punktsymmetrie über f(−x) = −f(x) nachweisen, eindeutige Nullstelle begründen und Grenzwert angeben", typ_neben="",
    stichwoerter="f(−x) = −x · e^(−x²/2 + 1/2) = −f(x)|e-Faktor stets positiv ⇒ f(x) = 0 ⇔ x = 0|lim f(x) = 0 für x → +∞",
    voraussetzungen="Symmetriebedingung am Term|Produkt null|Exponentialfunktion dominiert",
    format="Rechnung|Begründung|Kurzantwort", operator="Zeigen Sie|Begründen Sie|Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=GF, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x · e^(−x²/2 + 1/2) in IR; Graph in Abbildung 1 ohne Koordinatensystem",
    gesucht="Nachweis der Punktsymmetrie zum Ursprung; Begründung genau einer Nullstelle; Grenzwert für x → +∞",
    verfahren="f(−x) umformen, Faktor e^(…) > 0, Grenzwert über das Wachstum der e-Funktion",
    schritte="3", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="f(−x) = (−x) · e^(−(−x)²/2 + 1/2) = −x · e^(−x²/2 + 1/2) = −f(x); wegen e^(−x²/2 + 1/2) > 0 gilt f(x) = 0 ⇔ x = 0; lim f(x) = 0 für x → +∞ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Symmetrie nur am Bild ablesen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden", typ_neben="",
    stichwoerter="f'(x) = e^(…) + x · (−x) · e^(…)|(1 − x²) · e^(−x²/2 + 1/2)",
    voraussetzungen="Produktregel|Kettenregel für e^(g(x))",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f wie in a; Kontrolle f'(x) = (1 − x²) · e^(−x²/2 + 1/2)",
    gesucht="Term von f'",
    verfahren="Produkt- und Kettenregel, ausklammern",
    schritte="2", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = e^(−x²/2 + 1/2) + x · (−x) · e^(−x²/2 + 1/2) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="innere Ableitung −x vergessen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR2", "c", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Monotonie über das Vorzeichen der Ableitung am Term nachweisen", typ_neben="Koordinatenachsen zu einem gegebenen Graphen ergänzen und skalieren",
    stichwoerter="f'(x) = 0 ⇔ x = ±1|−1 < x < 1: f' > 0, streng monoton zunehmend|sonst abnehmend|f(1) = 1 ⇒ Achsen mit Hochpunkt (1 | 1) einzeichnen",
    voraussetzungen="Vorzeichen von 1 − x²|Extrempunkte als Anker für die Skalierung",
    format="Rechnung|Zeichnen", operator="Untersuchen Sie|Ergänzen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=GF, kontext="ohne", textumfang="kurz",
    gegeben="f und f' wie in a, b; Abbildung 1 ohne Achsen",
    gesucht="Monotonieverhalten rechnerisch; Koordinatenachsen mit Skalierung in Abbildung 1",
    verfahren="Nullstellen von f' und Vorzeichen, Achsen durch den Symmetriepunkt legen, Skalierung über (1 | 1)",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2022MerhoehtBAnalysisWTR2-1b",
    ergebnis="f'(x) = 0 ⇔ x = −1 ∨ x = 1; f ist für −1 < x < 1 wegen f'(x) > 0 streng monoton zunehmend, für x < −1 und x > 1 wegen f'(x) < 0 streng monoton abnehmend; es gilt f(1) = 1, Achsen entsprechend eingezeichnet (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Achsen so legen, dass der Ursprung nicht auf dem Graphen liegt",
    bemerkung="Standardbezug: K1 I, K2 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2022MerhoehtBAnalysisWTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Analysis", thema="Integrationsregeln",
    typ="Integral über eine vorgegebene Regel für g' · e^g berechnen", typ_neben="",
    stichwoerter="f(x) = −(−x) · e^(−x²/2 + 1/2), g(x) = −x²/2 + 1/2, g'(x) = −x|∫₀¹ f = −[e^(g(x))]₀¹ = −1 + e^(1/2)",
    voraussetzungen="Integrand in die Form g' · e^g bringen|Vorzeichen anpassen|Regel anwenden",
    format="Rechnung", operator="Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Regel ∫ g'(x) · e^(g(x)) dx = [e^(g(x))] über [u; v]",
    gesucht="Wert von ∫₀¹ f(x) dx",
    verfahren="f als −g' · e^g mit g = −x²/2 + 1/2 schreiben, Regel anwenden",
    schritte="3", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="∫₀¹ f(x) dx = −∫₀¹ (−x) · e^(−x²/2 + 1/2) dx = −[e^(−x²/2 + 1/2)]₀¹ = −1 + e^(1/2) (amtlich)",
    zwischenergebnis="≈ 0,649", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen: g'(x) = −x, nicht x",
    bemerkung="Standardbezug: K1 II, K4 III, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (gegebene Regel anwenden), amtlich III.")

row("2022MerhoehtBAnalysisWTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Uneigentliche Integrale",
    typ="Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten", typ_neben="",
    stichwoerter="F(w) − F(0) = ∫₀^w f|Flächenstück bis x = w|stimmt für w > 2022 nahezu mit der Fläche bis x = 2022 überein, da f → 0",
    voraussetzungen="Hauptsatz|Fläche zwischen Graph, Achse und senkrechter Gerade|Grenzverhalten",
    format="Begründung", operator="Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Für jede Stammfunktion F und jedes w > 2022 gilt F(w) − F(0) ≈ ∫₀²⁰²² f(x) dx",
    gesucht="geometrische Deutung",
    verfahren="Differenz als Integral, Integral als Flächeninhalt, Zusatzfläche jenseits von 2022 vernachlässigbar",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Für jedes w > 2022 schließen der Graph von f, die x-Achse und die Gerade x = w ein Flächenstück ein; dessen Inhalt stimmt ungefähr mit dem Inhalt des Flächenstücks überein, das Graph, x-Achse und die Gerade x = 2022 einschließen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Aussage als Gleichheit von Stammfunktionen deuten",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich.")

row("2022MerhoehtBAnalysisWTR2", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben", typ_neben="",
    stichwoerter="f_a(1) = 1 ⇔ e^(−a/2 + 1/2) = 1 ⇔ −a/2 + 1/2 = 0 ⇔ a = 1|genau eine Lösung ⇒ genau ein Graph",
    voraussetzungen="Exponentialgleichung e^t = 1|Eindeutigkeit der Lösung",
    format="Rechnung", operator="Zeigen Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = x · e^(−a · x²/2 + 1/2), a ∈ IR",
    gesucht="Nachweis, dass genau ein Graph (1 | 1) enthält; zugehöriges a",
    verfahren="Punkt einsetzen, Gleichung eindeutig nach a lösen",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="f_a(1) = 1 ⇔ e^(−a/2 + 1/2) = 1 ⇔ −a/2 + 1/2 = 0 ⇔ a = 1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Eindeutigkeit nicht aus der Äquivalenzkette ableiten",
    bemerkung="Standardbezug: K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A), hier mit Nachweis der Eindeutigkeit.")

row("2022MerhoehtBAnalysisWTR2", "b", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Steigung und Achsenschnittpunkt des linearen Sonderfalls einer Schar angeben", typ_neben="",
    stichwoerter="f₀(x) = x · e^(1/2)|Steigung √e|Schnittpunkt (0 | 0)",
    voraussetzungen="Parameter null einsetzen|Gerade durch den Ursprung",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Graph von f₀ ist eine Gerade",
    gesucht="Steigung und Schnittpunkt mit der y-Achse",
    verfahren="a = 0 einsetzen",
    schritte="1", zahlenraum="Potenz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="Steigung √e; Schnittpunkt (0 | 0) (amtlich)",
    zwischenergebnis="√e ≈ 1,65", niveau_geschaetzt="I",
    fehlerquelle="Steigung e statt e^(1/2)",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR2", "c", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Folgerungen aus gemeinsamen Eigenschaften einer Schar für den Verlauf der Graphen angeben", typ_neben="",
    stichwoerter="f_a(0) = 0: alle durch den Ursprung|f_a'(0) = f₀'(0): gleiche Steigung dort|f_a1(x) = f_a2(x) nur für x = 0: keine weiteren gemeinsamen Punkte",
    voraussetzungen="Aussagen über Funktionswerte und Ableitungen geometrisch lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Für alle a, a₁, a₂: f_a(0) = 0; f_a'(0) = f₀'(0); f_a1(x) = f_a2(x) ⇔ a₁ = a₂ ∨ x = 0",
    gesucht="Folgerungen für den Verlauf der Graphen",
    verfahren="Jede Aussage in eine Lageeigenschaft übersetzen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Alle Graphen der Schar schneiden sich im Ursprung und haben dort die gleiche Steigung; keiner der Graphen hat einen weiteren Punkt mit einem anderen Graphen gemeinsam (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="dritte Aussage als Berührung deuten",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. AB amtlich: II. Amtlich.")

row("2022MerhoehtBAnalysisWTR2", "d", innen="2", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gleichmäßige Streckung eines Scharfgraphen als Graph einer anderen Scharfunktion nachweisen", typ_neben="",
    stichwoerter="Streckung: k · f_a(x/k)|= x · e^(−a/k² · x²/2 + 1/2) = f_(a/k²)(x)",
    voraussetzungen="Streckung in x-Richtung als x/k, in y-Richtung als Faktor k|Term umformen",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Aussage: wird der Graph von f_a mit demselben Faktor k > 0 in x- und y-Richtung gestreckt, entsteht wieder ein Graph der Schar",
    gesucht="Nachweis für jedes a",
    verfahren="Gestreckten Term k · f_a(x/k) bilden und als f_b mit b = a/k² erkennen",
    schritte="2", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="k · f_a(x/k) = k · x/k · e^(−a · (x/k)²/2 + 1/2) = x · e^(−a/k² · x²/2 + 1/2) = f_(a/k²)(x) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Streckung in x-Richtung als k · x statt x/k",
    bemerkung="Standardbezug: K2 II, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis mit hergeleitetem Parameter a/k².")

row("2022MerhoehtBAnalysisWTR2", "e", innen="2", seite="3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameterwerte nach der Anzahl der Extrempunkte über die Lösbarkeit der Extremstellengleichung begründen", typ_neben="",
    stichwoerter="a · x² = 1: für a > 0 zwei Lösungen, für a ≤ 0 keine|Gruppe I: a > 0, Gruppe II: a ≤ 0",
    voraussetzungen="Lösbarkeit einer quadratischen Gleichung nach dem Vorzeichen des Koeffizienten",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF, kontext="ohne", textumfang="mittel",
    gegeben="Gruppe I: genau zwei Extrempunkte (Abbildung 2), Gruppe II: keine (Abbildung 3); Extremstellen sind die Lösungen von a · x² = 1",
    gesucht="alle a je Gruppe mit Begründung",
    verfahren="Lösungsanzahl von a · x² = 1 nach a unterscheiden",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Die Gleichung a · x² = 1 hat für a > 0 genau zwei Lösungen, für a ≤ 0 keine; damit gehören zur Gruppe I die Werte a > 0, zur Gruppe II die Werte a ≤ 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="a = 0 der Gruppe I zuordnen",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR2", "f", innen="2", seite="3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Ortskurve der Extrempunkte einer Schar als Gerade über Sonderfall und Streckungseigenschaft begründen", typ_neben="",
    stichwoerter="f₁ = f hat den Hochpunkt (1 | 1) auf y = x und ist punktsymmetrisch (Tiefpunkt (−1 | −1))|alle anderen Extrempunkte entstehen durch gleichmäßige Streckung, die y = x erhält",
    voraussetzungen="Ergebnisse aus 1c und 2d verknüpfen|Gerade y = x unter Streckung invariant",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Alle Extrempunkte der Schar liegen auf einer Geraden",
    gesucht="Begründung, dass es die Gerade y = x ist",
    verfahren="Sonderfall f₁ = f mit Hochpunkt (1 | 1) und Symmetrie; Streckung mit gleichem Faktor führt die Extrempunkte entlang y = x",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2022MerhoehtBAnalysisWTR2-1c",
    ergebnis="f₁ ist die Funktion f aus Aufgabe 1; ihr Graph ist symmetrisch bezüglich des Ursprungs und hat den Hochpunkt (1 | 1) (amtlich)",
    zwischenergebnis="Extrempunkte (±1/√a | ±1/√a)", niveau_geschaetzt="II",
    fehlerquelle="Ortskurve über die allgemeine Extremstelle ausrechnen, obwohl Sonderfall und Streckung genügen",
    bemerkung="Standardbezug: K1 I, K2 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Extrempunkte (±1/√a | ±1/√a)).")

row("2022MerhoehtBAnalysisWTR2", "g", innen="2", seite="3", punkte="6", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für einen vorgegebenen Flächeninhalt eines Vierecks aus Hochpunkt und Achsenpunkten bestimmen", typ_neben="",
    stichwoerter="Skizze: Viereck O, (v | 0), (v | f_a(v)) mit f_a(v) = v (auf y = x), (0 | 2/v)|Trapez mit parallelen Seiten 2/v und v, Breite v: 1/2 · (v + 2/v) · v = 49|v² = 96|a · 96 = 1 ⇒ a = 1/96",
    voraussetzungen="Hochpunkt auf y = x|Trapezfläche|Extremstellenbedingung a · v² = 1",
    format="Zeichnen|Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine; Erwartungshorizont: Skizze mit Achsen, Punkten (0 | 2/v), O, (v | 0), Hochpunkt (v | v) und schraffiertem Viereck", kontext="ohne", textumfang="mittel",
    gegeben="für a > 0: Hochpunkt (v | f_a(v)), Punkt (0 | 2/v), Ursprung und (v | 0) bilden ein Viereck; Flächeninhalt 49",
    gesucht="zugehöriger Wert von a, ausgehend von einer Skizze",
    verfahren="Viereck als Trapez skizzieren, Flächeninhalt in v ausdrücken, v² bestimmen, a aus a · v² = 1",
    schritte="4", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="2022MerhoehtBAnalysisWTR2-2f",
    ergebnis="Für v > 0 gilt 1/2 · (v + 2/v) · v = 49 ⇔ 1/2v² + 1 = 49 ⇔ v² = 96; a · 96 = 1 ⇔ a = 1/96 (amtlich)",
    zwischenergebnis="v = √96 ≈ 9,80", niveau_geschaetzt="III",
    fehlerquelle="f_a(v) nicht als v erkennen (Ortskurve y = x)",
    bemerkung="Standardbezug: K2 III, K4 II, K5 II, K6 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Viereck als Trapez skizzieren, Fläche über die Ortskurve in v ausdrücken, verkettet mit der Extremstellenbedingung.")

# ---- Analysis WTR 3: Behälter, M(h) = 100e^(−0,04h), Kugelvolumen V(h), Füllvolumen V(t)
MB = "Abbildung 1: Koordinatensystem h von 0 bis 100 (Raster 10), M(h) von 0 bis 100 (Raster 20); fallende Exponentialkurve von (0 | 100) über (20 | 45) nach (100 | 2)"
row("2022MerhoehtBAnalysisWTR3", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Anfangswert angeben und Stelle für einen vorgegebenen Wert einer Exponentialfunktion berechnen", typ_neben="",
    stichwoerter="M(0) = 100|M(h) = 2 ⇔ e^(−0,04h) = 0,02 ⇔ h = −25 · ln(0,02) ≈ 98",
    voraussetzungen="Funktionswert an der Stelle 0|Exponentialgleichung mit ln lösen",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=MB, kontext="Produktion/Behälter", textumfang="mittel",
    gegeben="M(h) = 100 · e^(−0,04h), h Füllhöhe in cm; größte zugelassene Füllhöhe bei M = 2",
    gesucht="Wert von M bei leerem Behälter; größte zugelassene Füllhöhe",
    verfahren="M(0) ablesen, M(h) = 2 logarithmieren",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="cm", abhaengig_von="",
    ergebnis="Bei leerem Behälter hat M den Wert 100; M(h) = 2 ⇔ e^(−0,04h) = 0,02 ⇔ h = −25 · ln(0,02), die größte zugelassene Füllhöhe beträgt etwa 98 cm (amtlich)",
    zwischenergebnis="h ≈ 97,8", niveau_geschaetzt="I",
    fehlerquelle="ln(2) statt ln(0,02)",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR3", "b", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Verschiebung einer Exponentialfunktion als Streckung nachweisen", typ_neben="",
    stichwoerter="M(h − 25) = 100 · e^(−0,04(h − 25)) = 100 · e^(−0,04h + 1) = e · M(h)|k = e unabhängig von h",
    voraussetzungen="Potenzgesetz e^(u+v) = e^u · e^v|Term mit verschobenem Argument",
    format="Rechnung", operator="Weisen Sie nach|Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Produktion/Behälter", textumfang="mittel",
    gegeben="Abnahme der Füllhöhe um 25 cm ändert M vom Ausgangswert zum k-fachen",
    gesucht="Nachweis, dass k unabhängig von der Ausgangshöhe ist; Wert von k",
    verfahren="M(h − 25) umformen und als Vielfaches von M(h) schreiben",
    schritte="2", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="M(h − 25) = 100 · e^(−0,04 · (h − 25)) = 100 · e^(−0,04h + 1) = e · M(h), d. h. k = e (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="k = e^(−1) durch Verschiebung in die falsche Richtung",
    bemerkung="Standardbezug: K2 II, K3 I, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2022MerhoehtBAnalysisWTR3", "c", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Logarithmus einer Exponentialfunktion als lineare Funktion nachweisen und Steigung und Achsenabschnitt angeben", typ_neben="",
    stichwoerter="ln(100 · e^(−0,04h)) = ln 100 − 0,04h|Steigung −0,04|Punkt (0 | ln 100)",
    voraussetzungen="Logarithmengesetze ln(ab) = ln a + ln b, ln e^t = t",
    format="Rechnung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Produktion/Behälter", textumfang="kurz",
    gegeben="Zuordnung h ↦ ln(100 · e^(−0,04h))",
    gesucht="Nachweis geradlinigen Verlaufs; Steigung; Schnittpunkt mit der y-Achse",
    verfahren="Logarithmus umformen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="ln(100 · e^(−0,04h)) = ln 100 − 0,04 · h; Steigung −0,04; gemeinsamer Punkt (0 | ln 100) (amtlich)",
    zwischenergebnis="ln 100 ≈ 4,61", niveau_geschaetzt="II",
    fehlerquelle="ln(100 · e^…) als 100 · ln(e^…)",
    bemerkung="Standardbezug: K1 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR3", "a", innen="2", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion eines Polynomterms nach dem Ausmultiplizieren angeben", typ_neben="",
    stichwoerter="π(50² − (50 − x)²) = 100πx − πx²|Stammfunktion 50πx² − 1/3πx³",
    voraussetzungen="binomische Formel|Potenzregel der Integration",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Produktion/Behälter", textumfang="mittel",
    gegeben="kugelförmiger Behälter, Innendurchmesser 100 cm; V(h) = 1/1000 · ∫₀^h π(50² − (50 − x)²) dx in Litern; i(x) = π(50² − (50 − x)²)",
    gesucht="Term einer Stammfunktion von i",
    verfahren="Ausmultiplizieren, gliedweise integrieren",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="π(50² − (50 − x)²) = 100πx − πx²; Term einer Stammfunktion: 50πx² − 1/3πx³ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="(50 − x)² falsch ausmultipliziert",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR3", "b", innen="2", seite="2", punkte="6", afb_amtlich="III",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Integranden als Querschnittsfläche über den Satz des Pythagoras deuten und Umrechnungsfaktor erläutern", typ_neben="",
    stichwoerter="Radius des Flüssigkeitsspiegels in Höhe x: √(50² − (50 − x)²) nach Pythagoras|π · r² Flächeninhalt des horizontalen Schnitts|1/1000: cm³ in Liter",
    voraussetzungen="Kreisfläche|Pythagoras im Kugelschnitt|Volumen als Integral über Querschnittsflächen|Einheiten",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie|Beschreiben Sie", antwort="Text",
    material="Skizze", skizze="Abbildung 2: vertikaler Schnitt durch den Kugelmittelpunkt, Kreis mit Mittelpunkt, Radius 50 schräg nach rechts unten eingezeichnet, waagerechte fette Strecke vom Mittelpunkt bis zum Kreisrand in Höhe x über dem tiefsten Punkt, gestrichelte Sehne", kontext="Produktion/Behälter", textumfang="lang",
    gegeben="Term π(50² − (50 − x)²) im Integranden; Faktor 1/1000; Abbildung 2",
    gesucht="Bedeutung des Terms mit Begründung an der Abbildung; Bedeutung des Faktors",
    verfahren="Fette Strecke als Radius des Spiegels über Pythagoras, Kreisfläche; Umrechnung der Einheiten",
    schritte="3", zahlenraum="ganz", einheiten="cm³|l", abhaengig_von="",
    ergebnis="Der Term gibt den Flächeninhalt des horizontalen Schnitts in der Höhe x an; die fette Strecke hat nach Pythagoras die Länge √(50² − (50 − x)²) und ist der Radius der Flüssigkeitsoberfläche; der Faktor 1/1000 wandelt Kubikzentimeter in Liter um (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Term als Kugelfläche oder Umfang deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (d) Integrand als Querschnitt deuten, verkettet mit Pythagoras in der Skizze und dem Maßstab.")

row("2022MerhoehtBAnalysisWTR3", "c", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Wendestelle einer Integralfunktion über die Ableitung des Integranden begründen und Funktionswert berechnen", typ_neben="",
    stichwoerter="V'(h) = i(h)/1000, V''(h) = (100π − 2πh)/1000 = 0 ⇔ h = 50|V(50) = 1/1000 · 1/2 · 4/3π · 50³ = 250/3 π ≈ 262 l",
    voraussetzungen="Ableitung einer Integralfunktion ist der Integrand|Wendestelle über V'' = 0|halbe Kugel",
    format="Begründung|Rechnung", operator="Begründen Sie|Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="Abbildung 3: Koordinatensystem h von 0 bis 100, V(h) von 0 bis 500; S-förmig steigender Graph von (0 | 0) über den Wendepunkt (50 | 262) nach (100 | 524)", kontext="Produktion/Behälter", textumfang="mittel",
    gegeben="Graph von h ↦ V(h) in Abbildung 3",
    gesucht="Begründung der Wendestelle 50; zugehöriges Füllvolumen",
    verfahren="Zweite Ableitung von V über den Integranden, Nullstelle; V(50) als halbe Kugel oder über die Stammfunktion",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="l", abhaengig_von="2022MerhoehtBAnalysisWTR3-2a",
    ergebnis="Der Term 1/1000 · (100π − 2πh) der zweiten Ableitung von h ↦ V(h) hat genau dann den Wert 0, wenn h = 50; V(50) = 1/1000 · 1/2 · 4/3 · π · 50³ = 250/3 · π (amtlich)",
    zwischenergebnis="≈ 261,8 l", niveau_geschaetzt="II",
    fehlerquelle="V'' aus der Stammfunktion falsch ableiten",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAnalysisWTR3", "a", innen="3", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Minimalwert einer verschobenen Sinusfunktion begründen", typ_neben="",
    stichwoerter="sin(π/12 t) minimal −1|V minimal −150 + 300 = 150",
    voraussetzungen="Wertebereich des Sinus|Amplitude und Verschiebung",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Produktion/Behälter", textumfang="mittel",
    gegeben="V(t) = 150 · sin(π/12 · t) + 300, t Minuten, V(t) Füllvolumen in Litern",
    gesucht="Begründung, dass das minimale Füllvolumen 150 Liter beträgt",
    verfahren="Minimum des Sinus einsetzen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="l", abhaengig_von="",
    ergebnis="Der minimale Wert von sin(π/12 · t) ist −1, der minimale Wert von V(t) also −150 + 300 = 150 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Minimum bei t = 0 (V = 300) vermuten",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich.")

row("2022MerhoehtBAnalysisWTR3", "b", innen="3", seite="2", punkte="6", afb_amtlich="III",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Alle Zeitpunkte für einen Wert einer Sinusfunktion in einem Intervall berechnen", typ_neben="",
    stichwoerter="sin(π/12 t) = 1/2|π/12 t = π/6, π − π/6, 2π + π/6, 3π − π/6|t = 2, 10, 26, 34|in [0; 30]: 2, 10, 26 Minuten",
    voraussetzungen="Sinusgleichung mit allen Lösungen (Periodizität, Symmetrie zu π/2)|Intervall beachten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Behälter", textumfang="kurz",
    gegeben="V wie in a; erste halbe Stunde; Füllvolumen 375 Liter",
    gesucht="alle Zeitpunkte mit V(t) = 375 in den ersten 30 Minuten",
    verfahren="Gleichung auf sin(π/12 t) = 1/2 bringen, alle Lösungen über π/6 und π − π/6 plus Perioden, Intervall",
    schritte="4", zahlenraum="Bruch|ganz", einheiten="min", abhaengig_von="",
    ergebnis="150 · sin(π/12 · t) + 300 = 375 ⇔ sin(π/12 · t) = 1/2; π/12 · t = π/6 ⇔ t = 2, = π − π/6 ⇔ t = 10, = 2π + π/6 ⇔ t = 26, = 3π − π/6 ⇔ t = 34; die gesuchten Zeitpunkte liegen 2, 10 und 26 Minuten nach Beginn (amtlich)",
    zwischenergebnis="Periode 24 Minuten", niveau_geschaetzt="II",
    fehlerquelle="nur die Rechnerlösung t = 2 angeben",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Sinusgleichung mit Periodizität lösen), amtlich III. Kein Rückgriff auf „Zeitpunkt für einen Anteil des Maximalwerts einer Sinusfunktion berechnen“ (dort eine Lösung, hier alle Lösungen im Intervall).")

row("2022MerhoehtBAnalysisWTR3", "c", innen="3", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Wert einer Funktion berechnen und die zugehörige Stelle einer zweiten Funktion am Graphen ablesen", typ_neben="",
    stichwoerter="V(50) = 375 Liter|Abbildung 3: V(h) = 375 bei h ≈ 65 cm",
    voraussetzungen="Funktionswert|Umkehrung am Graphen ablesen|zwei Modelle verketten",
    format="Rechnung|Kurzantwort", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="Abbildung 3 wie in 2c", kontext="Produktion/Behälter", textumfang="kurz",
    gegeben="V(t) wie in 3a; Abbildung 3 mit V(h)",
    gesucht="Füllhöhe 50 Minuten nach Beginn",
    verfahren="V(50) berechnen, in Abbildung 3 die zugehörige Höhe ablesen",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="l|cm", abhaengig_von="",
    ergebnis="Für t = 50 liefert V(t) den Wert 375; mithilfe der Abbildung 3 ergibt sich dafür eine Füllhöhe von etwa 65 cm (amtlich)",
    zwischenergebnis="rechnerisch h ≈ 64,8", niveau_geschaetzt="II",
    fehlerquelle="t = 50 als Füllhöhe in Abbildung 3 einsetzen",
    bemerkung="Standardbezug: K2 II, K3 I, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA A1 WTR: Drachenviereck, Lampen mit Übergangsmatrix N und Schar F_a
DV = "Schrägbild: Drachenviereck ABCD mit A im Ursprung, C(0|0|40) auf der z-Achse, B(−3|4|35) und D(3|−4|35) seitlich nahe der Spitze; Achsen x, y, z"
row("2022MerhoehtBAGLAA1WTR", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Rechten Winkel zwischen zwei Seiten einer Figur über das Skalarprodukt nachweisen", typ_neben="",
    stichwoerter="CB = (−3; 4; −5), CD = (3; −4; −5)|CB · CD = −9 − 16 + 25 = 0",
    voraussetzungen="Verbindungsvektoren|Skalarprodukt null",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="Figur", skizze=DV, kontext="ohne", textumfang="kurz",
    gegeben="Drachenviereck A(0|0|0), B(−3|4|35), C(0|0|40), D(3|−4|35)",
    gesucht="Nachweis des rechten Winkels zwischen BC und CD",
    verfahren="Skalarprodukt der Seitenvektoren",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="CB · CD = (−3; 4; −5) · (3; −4; −5) = −9 − 16 + 25 = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vektoren BC und CD mit falscher Orientierung (Vorzeichen ändert nichts am Ergebnis null)",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2022MerhoehtBAGLAA1WTR", "b", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Vierten Eckpunkt eines Quadrats über eine Vektoraddition bestimmen", typ_neben="",
    stichwoerter="OE = OD + CB = (3; −4; 35) + (−3; 4; −5) = (0; 0; 30)|E auf der Diagonale AC",
    voraussetzungen="Quadrat als Parallelogramm mit rechtem Winkel und gleichen Seiten|Vektoraddition",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Figur", skizze=DV, kontext="ohne", textumfang="kurz",
    gegeben="E auf der längeren Diagonale AC; BCDE Quadrat",
    gesucht="Koordinaten von E",
    verfahren="E = D + CB",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2022MerhoehtBAGLAA1WTR-1a",
    ergebnis="OE = OD + CB = (3; −4; 35) + (−3; 4; −5) = (0; 0; 30) (amtlich)",
    zwischenergebnis="|CB| = |CD| = √50", niveau_geschaetzt="II",
    fehlerquelle="E = D + BC (falsche Richtung) ergibt einen Punkt außerhalb der Diagonale",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2022MerhoehtBAGLAA1WTR", "c", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen", typ_neben="Gleichschenkligkeit eines dritten Dreiecks aus zwei Gleichschenkligkeiten begründen",
    stichwoerter="|BS_k| = |CS_k| ⇔ 125 + (k − 35)² = 100 + (k − 40)²|10k = 350 ⇔ k = 35|BS = CS und BS = DS ⇒ CS = DS",
    voraussetzungen="Abstände mit Parameter|quadratische Terme kürzen|Transitivität gleicher Längen",
    format="Rechnung|Begründung", operator="Bestimmen Sie|Begründen Sie", antwort="Zahl",
    material="Figur", skizze=DV, kontext="ohne", textumfang="mittel",
    gegeben="S_k(8|6|k); BDS_k stets gleichschenklig mit Basis BD",
    gesucht="k, für das BCS_k gleichschenklig mit Basis BC ist; Begründung ohne Rechnung, dass dann auch CDS_k gleichschenklig ist",
    verfahren="|BS_k| = |CS_k| quadriert lösen; aus BS = CS und BS = DS folgt CS = DS",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="|BS_k| = |CS_k| ⇔ √(125 + (k − 35)²) = √(100 + (k − 40)²) ⇔ 10k = 350 ⇔ k = 35; wegen |BS_k| = |CS_k| und |BS_k| = |DS_k| gilt auch |CS_k| = |DS_k| (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Basis und Schenkel verwechseln (|BS| = |BC| ansetzen)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A). Aufgabengruppe A1, außerhalb der Geltung.")

row("2022MerhoehtBAGLAA1WTR", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="Spalten von N als Abgänge|Schleifen r 0,4, g 0,2, b 0,3|r → g 0,3, r → b 0,3, g → r 0,2, g → b 0,6, b → r 0,2, b → g 0,5",
    voraussetzungen="Spaltenkonvention lesen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine; Erwartungshorizont: Diagramm mit Knoten r, g, b, Schleifen 0,4, 0,2, 0,3 und sechs Pfeilen mit den Übergangsraten", kontext="Lampen/Farbwechsel", textumfang="lang",
    gegeben="4500 Lampen in Rot, Grün, Blau; v_{n+1} = N · v_n mit N = ((0,4; 0,2; 0,2), (0,3; 0,2; 0,5), (0,3; 0,6; 0,3)) (zeilenweise)",
    gesucht="Übergangsdiagramm",
    verfahren="Einträge n_ij als Pfeil von j nach i",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Diagramm mit Schleifen 0,4 (r), 0,2 (g), 0,3 (b) und Pfeilen r → g 0,3, r → b 0,3, g → r 0,2, g → b 0,6, b → r 0,2, b → g 0,5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen als Abgänge lesen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A). Aufgabengruppe A1, außerhalb der Geltung.")

row("2022MerhoehtBAGLAA1WTR", "b", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Verhältnis der Anfangsbestände aus einer Gleichverteilung nach einem Übergang bestimmen", typ_neben="",
    stichwoerter="N · (r; g; 1000) = (1500; 1500; 1500)|I 0,4r + 0,2g + 200 = 1500, II 0,3r + 0,2g + 500 = 1500|r = 3000, g = 500|r : g = 6 : 1",
    voraussetzungen="Gesamtzahl 4500 gleich verteilt|lineares Gleichungssystem",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Lampen/Farbwechsel", textumfang="mittel",
    gegeben="1000 Lampen blau; nach dem Wechsel je 1500 rot, grün, blau",
    gesucht="Verhältnis rot zu grün vor dem Wechsel",
    verfahren="Matrixgleichung mit Unbekannten r, g aufstellen, zwei Gleichungen lösen",
    schritte="3", zahlenraum="ganz", einheiten="Lampen", abhaengig_von="",
    ergebnis="N · (r; g; 1000) = (1500; 1500; 1500) liefert 0,4r + 0,2g + 200 = 1500 und 0,3r + 0,2g + 500 = 1500; daraus 0,1r = 300 ⇔ r = 3000 und g = 500, d. h. r : g = 6 : 1 (amtlich)",
    zwischenergebnis="Probe r + g + 1000 = 4500", niveau_geschaetzt="II",
    fehlerquelle="Gleichverteilung als 1500 vor dem Wechsel ansetzen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2022MerhoehtBAGLAA1WTR", "c", innen="2", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Parameterbereich für endliche Grenzwerte der Matrixpotenzen über eine Potenzfolge bestimmen", typ_neben="",
    stichwoerter="Einträge 1/2 · (2a)^k und 1 − (2a)^k|(2a)^k → ∞ für a > 1/2, → 1 für a = 1/2, → 0 für a < 1/2|endlich nur für a ≤ 1/2",
    voraussetzungen="Grenzverhalten geometrischer Folgen|Einträge der gegebenen Potenzmatrix lesen",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Lampen/Farbwechsel", textumfang="lang",
    gegeben="F_a = ((a; a; 0), (a; a; 0), (1 − 2a; 1 − 2a; 1)), a ≥ 0; F_a^k mit Einträgen 1/2 · 2^k a^k, 1 − 2^k a^k und 0, 1",
    gesucht="a, für die sich jeder Eintrag von F_a^k für k → ∞ einem endlichen Wert nähert",
    verfahren="2^k a^k = (2a)^k nach dem Wert von 2a untersuchen",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Für k → ∞ gilt (2a)^k → ∞ für a > 1/2, (2a)^k → 1 für a = 1/2 und (2a)^k → 0 für a < 1/2; damit nähert sich nur für a ≤ 1/2 jeder Eintrag einem endlichen Wert (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="a = 1/2 ausschließen (Grenzwert 1 ist endlich)",
    bemerkung="Standardbezug: K1 II, K2 III, K4 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeine Fallunterscheidung über die Potenzfolge. Aufgabengruppe A1, außerhalb der Geltung.")

row("2022MerhoehtBAGLAA1WTR", "d", innen="2", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsverhalten einer parametrisierten Matrix nach Fällen im Sachzusammenhang beschreiben", typ_neben="",
    stichwoerter="a = 0: alle sofort blau|0 < a < 1/2: blau bleibt, von rot/grün bleibt Anteil a, Anteil a wechselt zur anderen Farbe, Rest 1 − 2a zu blau, langfristig alles blau|a = 1/2: blau bleibt, rot und grün tauschen je zur Hälfte",
    voraussetzungen="Matrixeinträge als Übergangsanteile deuten|Grenzmatrix deuten|Fallunterscheidung",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Lampen/Farbwechsel", textumfang="lang",
    gegeben="F_a für a ≤ 1/2 beschreibt Farbwechsel; für a < 1/2 gilt F_a^k → ((0; 0; 0), (0; 0; 0), (1; 1; 1))",
    gesucht="Beschreibung der Farbwechsel in Abhängigkeit von a",
    verfahren="Spalten von F_a als Abgänge deuten, Fälle a = 0, 0 < a < 1/2, a = 1/2 trennen, Grenzmatrix als Endzustand",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2022MerhoehtBAGLAA1WTR-2c",
    ergebnis="a = 0: unabhängig vom Ausgangszustand leuchten nach dem ersten Wechsel alle Lampen blau; 0 < a < 1/2: blaue Lampen bleiben blau, von den roten und grünen behält je Wechsel der Anteil a die Farbe, der Anteil a wechselt zur jeweils anderen Farbe und die übrigen zu Blau, bis schließlich alle blau leuchten; a = 1/2: blaue bleiben blau, von den roten wechselt je Wechsel die Hälfte zu Grün und umgekehrt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Fall a = 1/2 (kein Abfluss nach Blau) übersehen",
    bemerkung="Standardbezug: K1 III, K3 III, K4 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (d) Matrixeinträge deuten, verkettet mit Grenzmatrix und Fallunterscheidung. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA A2 WTR 1: Pyramiden ABCD_k, Quader mit Q(1|1|3)
PK = "Abbildung 1: Schrägbild der Pyramide mit A im Ursprung, B(4|0|0), C(0|4|0), Spitze D_k(0|0|k) auf der x₃-Achse; Abbildung 2: dazu ein Quader mit Ecken A und Q(1|1|3), Seitenflächen parallel zu den Koordinatenebenen, Eckpunkte P und R auf der oberen Fläche; Abbildung 3: Pyramide ABCD₆ mit einbeschriebenem Quader über quadratischer Grundfläche bei A, Eckpunkt Q_h in der Fläche BCD₆"
row("2022MerhoehtBAGLAA2WTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Gleichschenkligkeit über kongruente rechtwinklige Dreiecke begründen", typ_neben="",
    stichwoerter="ABD_k und ACD_k rechtwinklig bei A mit Katheten 4 und k|Hypotenusen BD_k und CD_k gleich lang",
    voraussetzungen="Rechte Winkel an den Achsen|Kongruenz über gleiche Katheten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=PK, kontext="ohne", textumfang="kurz",
    gegeben="Pyramiden ABCD_k mit A(0|0|0), B(4|0|0), C(0|4|0), D_k(0|0|k), 0 < k ≤ 6",
    gesucht="Begründung, dass BCD_k gleichschenklig ist",
    verfahren="Kongruente rechtwinklige Dreiecke ABD_k und ACD_k",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Dreiecke ABD_k und ACD_k sind rechtwinklig und stimmen in den Längen ihrer Katheten überein; damit sind auch die beiden Hypotenusen gleich lang (amtlich)",
    zwischenergebnis="|BD_k| = |CD_k| = √(16 + k²)", niveau_geschaetzt="I",
    fehlerquelle="BC als Schenkel ansehen",
    bemerkung="Standardbezug: K1 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAGLAA2WTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen", typ_neben="",
    stichwoerter="M(2|2|0) Mittelpunkt der Basis BC|MD_k Höhe wegen Gleichschenkligkeit|A = 1/2 · √32 · √(8 + k²)",
    voraussetzungen="Höhe eines gleichschenkligen Dreiecks trifft den Basismittelpunkt|Betrag mit Parameter",
    format="Begründung|Rechnung", operator="Begründen Sie|Bestimmen Sie", antwort="Term",
    material="Körper", skizze=PK, kontext="ohne", textumfang="kurz",
    gegeben="M(2|2|0) Mittelpunkt von BC; |MD_k| = |(−2; −2; k)|",
    gesucht="Begründung, dass |MD_k| eine Höhe ist; Flächeninhalt von BCD_k",
    verfahren="Gleichschenkligkeit mit Basis BC, Höhe durch den Basismittelpunkt, Flächenformel",
    schritte="2", zahlenraum="Wurzel", einheiten="", abhaengig_von="2022MerhoehtBAGLAA2WTR1-1a",
    ergebnis="Da BCD_k gleichschenklig mit Basis BC ist, stellt MD_k eine Höhe dar; Flächeninhalt 1/2 · |BC| · |MD_k| = 1/2 · √32 · √(8 + k²) (amtlich)",
    zwischenergebnis="= 2√(16 + 2k²)", niveau_geschaetzt="II",
    fehlerquelle="Höhe ohne Begründung über M annehmen",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (Kreuzprodukt). Abweichung: meine Schätzung II (Höhe begründen, Term mit Parameter), amtlich I. Typ wiederverwendet (Teil A).")

row("2022MerhoehtBAGLAA2WTR1", "c", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="Ursprung nicht in L_k ⇒ Form ax₁ + bx₂ + cx₃ = 4|B: 4a = 4, C: 4b = 4, D_k: ck = 4|x₁ + x₂ + 4/k · x₃ = 4",
    voraussetzungen="Achsenabschnittsansatz|Punkte einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=PK, kontext="ohne", textumfang="kurz",
    gegeben="Seitenfläche BCD_k in der Ebene L_k; Kontrolle x₁ + x₂ + 4/k · x₃ = 4",
    gesucht="Koordinatengleichung von L_k",
    verfahren="Ansatz mit rechter Seite 4, Koeffizienten aus den Achsenpunkten",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Da der Ursprung nicht in L_k liegt, lässt sich die Gleichung als ax₁ + bx₂ + cx₃ = 4 schreiben; mit B, C und D_k ergibt sich a = 1, b = 1 und c · k = 4 ⇔ c = 4/k (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Normalenvektor über Kreuzprodukt mit Parameter verrechnen",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Lauf 7), hier über Achsenabschnitte mit Parameter.")

row("2022MerhoehtBAGLAA2WTR1", "d", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharparameter für einen vorgegebenen Schnittwinkel zwischen Achse und Ebene ermitteln", typ_neben="",
    stichwoerter="sin 30° = (4/k)/√(2 + 16/k²) = 1/2|2 + 16/k² = 64/k²|k² = 24 ⇔ k = 2√6",
    voraussetzungen="Winkel Gerade–Ebene mit Sinus|Gleichung mit Parameter im Normalenvektor lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=PK, kontext="ohne", textumfang="kurz",
    gegeben="L_k wie in c; x₃-Achse",
    gesucht="k mit Schnittwinkel 30° zwischen x₃-Achse und L_k",
    verfahren="Sinusformel mit (0; 0; 1) und (1; 1; 4/k), quadrieren, nach k auflösen",
    schritte="3", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="2022MerhoehtBAGLAA2WTR1-1c",
    ergebnis="Für k > 0: sin 30° = ((0; 0; 1) · (1; 1; 4/k)) / (|(0; 0; 1)| · |(1; 1; 4/k)|) ⇔ 1/2 = (4/k)/√(1 + 1 + 16/k²) ⇔ 2 + 16/k² = 64/k² ⇔ k² = 24 ⇔ k = 2√6 (amtlich)",
    zwischenergebnis="k ≈ 4,90", niveau_geschaetzt="II",
    fehlerquelle="Kosinus statt Sinus ansetzen (Winkel zur Normalen 60°)",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAGLAA2WTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen", typ_neben="",
    stichwoerter="P(1|0|3) Eckpunkt des Quaders|1 + 12/k = 4 ⇔ k = 4",
    voraussetzungen="Eckpunkte des Quaders aus A und Q ableiten|Punktprobe mit Parameter",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=PK, kontext="ohne", textumfang="mittel",
    gegeben="Quader mit Ecken A und Q(1|1|3), Seitenflächen achsenparallel; BCD_k enthält die Quaderecken P und R; Kontrolle k = 4",
    gesucht="dieser Wert von k",
    verfahren="P(1|0|3) in L_k einsetzen",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2022MerhoehtBAGLAA2WTR1-1c",
    ergebnis="Enthält L_k den Punkt P(1|0|3), so gilt 1 + 12/k = 4 ⇔ k = 4 (amtlich)",
    zwischenergebnis="R(0|1|3) liefert dasselbe", niveau_geschaetzt="II",
    fehlerquelle="Q statt P einsetzen (ergibt k = 6)",
    bemerkung="Standardbezug: K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A), hier mit Ablesen der Quaderecke aus der Abbildung.")

row("2022MerhoehtBAGLAA2WTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben", typ_neben="",
    stichwoerter="k = 6: Ebene durch Q, k = 4: durch P und R, k = 3: durch (0|0|3)|4 ≤ k < 6: Dreieck|3 < k < 4: Fünfeck|0 < k ≤ 3: Viereck",
    voraussetzungen="Parameterwerte, bei denen die Ebene Quaderecken trifft|Schnittfigur einer Ebene mit einem Quader vorstellen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Körper", skizze=PK, kontext="ohne", textumfang="kurz",
    gegeben="Für k = 6 enthält BCD_k die Ecke Q, für kleinere k schneidet die Fläche den Quader in einem Vieleck",
    gesucht="Anzahl der Eckpunkte des Vielecks in Abhängigkeit von k",
    verfahren="Übergangswerte k = 6, 4, 3 aus den Ecken Q, P/R, (0|0|3) bestimmen, Schnittfiguren zuordnen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2022MerhoehtBAGLAA2WTR1-1e",
    ergebnis="4 ≤ k < 6: drei Eckpunkte; 3 < k < 4: fünf Eckpunkte; 0 < k ≤ 3: vier Eckpunkte (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Übergang bei k = 3 (Ebene durch die Deckflächenecke auf der x₃-Achse) übersehen",
    bemerkung="Standardbezug: K1 III, K4 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Übergangswerte). Eichregel: (d) Übergangswerte an den Ecken bestimmen, verkettet mit dem räumlichen Vorstellen der Schnittfigur.")

row("2022MerhoehtBAGLAA2WTR1", "g", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Koordinaten eines Punktes auf einer Strecke in Abhängigkeit von seiner Höhe ermitteln", typ_neben="",
    stichwoerter="Q_h liegt auf MD₆ (Symmetrie der quadratischen Grundfläche)|x = (2; 2; 0) + λ(−2; −2; 6), λ = h/6|Q_h(2 − h/3 | 2 − h/3 | h)",
    voraussetzungen="Symmetrie des einbeschriebenen Quaders|Strecke in Parameterform|Parameter aus der Höhe",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="Körper", skizze=PK, kontext="ohne", textumfang="lang",
    gegeben="Pyramide ABCD₆; einbeschriebene Quader mit quadratischer Grundfläche bei A in der x₁x₂-Ebene, Höhe h, 0 < h < 6; Q_h in der Fläche BCD₆",
    gesucht="Koordinaten von Q_h",
    verfahren="Q_h als Punkt der Strecke MD₆ mit x₃ = h",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Q_h ist der Punkt der Strecke MD₆ mit der x₃-Koordinate h; x = (2; 2; 0) + λ · (−2; −2; 6) liefert für λ = h/6: x₁ = x₂ = 2 − h/3 (amtlich)",
    zwischenergebnis="alternativ über L₆: 2x₁ + 4/6 · h = 4", niveau_geschaetzt="III",
    fehlerquelle="Q_h auf der Kante BD₆ statt auf der Mittellinie MD₆ suchen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Symmetrie ausnutzen: Q_h auf der Mittellinie MD₆.")

# ---- AG/LA A2 WTR 2: Saarpolygon A(11|11|0), B(−11|11|28), C(11|−11|28), D(−11|−11|0)
SP = "Abbildung 1: Foto des Saarpolygons (begehbares Denkmal, zwei schräge Stege, oben verbunden); Abbildung 2: Schrägbild des Streckenzugs A–B–C–D als Kanten eines gestrichelten Quaders 22 × 22 × 28, A und D unten, B und C oben; Abbildungen 3 und 4: schematische Ansichten (X-Form bzw. Λ-Form)"
row("2022MerhoehtBAGLAA2WTR2", "a", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrie zweier Punkte bezüglich einer Koordinatenachse über die Koordinaten begründen", typ_neben="",
    stichwoerter="B(−11|11|28), C(11|−11|28)|x₁ und x₂ nur im Vorzeichen verschieden, x₃ gleich",
    voraussetzungen="Spiegelung an der x₃-Achse kehrt x₁ und x₂ um",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=SP, kontext="Saarpolygon/Denkmal", textumfang="lang",
    gegeben="Streckenzug A(11|11|0), B(−11|11|28), C(11|−11|28), D(−11|−11|0), Ecken eines Quaders; 1 LE = 1 m",
    gesucht="Begründung, dass B und C symmetrisch zur x₃-Achse liegen",
    verfahren="Koordinaten vergleichen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Sowohl die x₁- als auch die x₂-Koordinaten von B und C unterscheiden sich nur in ihren Vorzeichen, die x₃-Koordinaten stimmen überein (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Symmetrie zur x₁x₃-Ebene behaupten",
    bemerkung="Standardbezug: K1 I, K4 I. AB amtlich: I. Amtlich.")

row("2022MerhoehtBAGLAA2WTR2", "b", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Länge eines Streckenzugs aus Kanten und Diagonalen eines Quaders im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="|AB| = |CD| = √(22² + 28²)|BC = √(22² + 22²)|2 · 35,6 + 31,1 ≈ 102 m",
    voraussetzungen="Beträge von Verbindungsvektoren|Summe",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=SP, kontext="Saarpolygon/Denkmal", textumfang="kurz",
    gegeben="Streckenzug AB, BC, CD wie in a",
    gesucht="Länge des Streckenzugs in der Wirklichkeit",
    verfahren="Drei Streckenlängen addieren",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="m", abhaengig_von="",
    ergebnis="2 · √(22² + 28²) + √(22² + 22²) ≈ 102, die Länge beträgt etwa 102 m (amtlich)",
    zwischenergebnis="102,3", niveau_geschaetzt="I",
    fehlerquelle="Kante 28 statt Diagonale √(22² + 28²)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAGLAA2WTR2", "c", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="x = (11; 11; 0) + r(−22; 0; 28) + s(0; −22; 28)|I x₁ = 11 − 22r, II x₂ = 11 − 22s, III x₃ = 28r + 28s|x₃ = 28 − 28/22 x₁ − 28/22 x₂ ⇔ 14x₁ + 14x₂ + 11x₃ = 308",
    voraussetzungen="Parameterform|Parameter eliminieren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=SP, kontext="Saarpolygon/Denkmal", textumfang="kurz",
    gegeben="E durch A, B, C; Kontrolle 14x₁ + 14x₂ + 11x₃ = 308",
    gesucht="Koordinatengleichung von E",
    verfahren="Parametergleichung, r und s aus I und II, in III einsetzen",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="x = (11; 11; 0) + r · (−22; 0; 28) + s · (0; −22; 28) liefert x₁ = 11 − 22r, x₂ = 11 − 22s, x₃ = 28r + 28s; aus I und II folgt 28r + 28s = 28 − 28/22 · x₁ − 28/22 · x₂, damit x₃ = 28 − 28/22 · x₁ − 28/22 · x₂ (amtlich)",
    zwischenergebnis="Normalenvektor (14; 14; 11)", niveau_geschaetzt="II",
    fehlerquelle="Bruch 28/22 falsch gekürzt",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Lauf 7).")

row("2022MerhoehtBAGLAA2WTR2", "d", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="Winkel zwischen zwei spiegelbildlichen Ebenen als Term im Neigungswinkel angeben",
    stichwoerter="cos φ = 11/√(2 · 14² + 11²)|φ ≈ 61°|Winkel zwischen E und F: 180° − 2φ",
    voraussetzungen="Normalenvektoren|Symmetrie von E und F zur x₁x₂-Ebene|Winkelsumme",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Term",
    material="Körper", skizze=SP, kontext="Saarpolygon/Denkmal", textumfang="mittel",
    gegeben="E: 14x₁ + 14x₂ + 11x₃ = 308; F durch B, C, D",
    gesucht="Winkel φ zwischen E und der x₁x₂-Ebene; Term für den Winkel zwischen E und F aus φ",
    verfahren="Kosinusformel mit (14; 14; 11) und (0; 0; 1); F ist zu E spiegelbildlich, Winkel 180° − 2φ",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2022MerhoehtBAGLAA2WTR2-1c",
    ergebnis="cos φ = ((14; 14; 11) · (0; 0; 1)) / |(14; 14; 11)| = 11/√(2 · 14² + 11²) liefert φ ≈ 61°; Term: 180° − 2φ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Winkel zwischen E und F als 2φ",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")

row("2022MerhoehtBAGLAA2WTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumenanteil einer Pyramide am Quader ohne Volumenberechnung begründen", typ_neben="",
    stichwoerter="Seitenfläche mit A und C als Grundfläche G, Quaderhöhe h|Pyramide: 1/3 · 1/2 · G · h = 1/6 · G · h = 1/6 · V",
    voraussetzungen="Pyramide über halber Quaderfläche|Pyramidenvolumen 1/3 G h",
    format="Begründung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=SP, kontext="Saarpolygon/Denkmal", textumfang="kurz",
    gegeben="E teilt den Quader in zwei Teilkörper, einer pyramidenförmig",
    gesucht="Anteil des Pyramidenvolumens am Quadervolumen ohne Volumenberechnung",
    verfahren="Pyramide mit halber Seitenfläche als Grundfläche und Quaderhöhe, Faktor 1/3",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Mit der Seitenfläche, die A und C enthält, als Grundfläche G, der zugehörigen Quaderhöhe h und dem Quadervolumen V ergibt sich für die Pyramide 1/3 · 1/2 · G · h = 1/6 · G · h = 1/6 · V (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Faktor 1/2 für das Dreieck vergessen (1/3)",
    bemerkung="Standardbezug: K1 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBAGLAA2WTR2", "f", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Blickrichtungsvektoren zu schematischen Ansichten angeben und eine weitere Ansicht zeichnen", typ_neben="",
    stichwoerter="Abbildung 3 (X-Form): Blick in Richtung (0; −1; 0)|Abbildung 4 (Λ-Form): Blick in Richtung (1; −1; 0)|von oben: Z-förmiger Streckenzug (Diagonale BC des Quadrats)",
    voraussetzungen="Projektion des Streckenzugs in Blickrichtung vorstellen|Ansicht von oben als Projektion in die x₁x₂-Ebene",
    format="Kurzantwort|Zeichnen", operator="Geben Sie an|Stellen Sie dar", antwort="Grafik",
    material="Skizze", skizze=SP + "; Erwartungshorizont: Ansicht von oben als Z-Form – zwei parallele Strecken (AB und CD) verbunden durch die Diagonale BC", kontext="Saarpolygon/Denkmal", textumfang="mittel",
    gegeben="Abbildungen 3 (X-Form) und 4 (Λ-Form) als schematische Ansichten",
    gesucht="je ein möglicher Blickrichtungsvektor; schematische Darstellung von oben",
    verfahren="Ansicht mit Blick entlang der x₂-Achse bzw. entlang der Diagonalen, Draufsicht als Projektion",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Abbildung 3: (0; −1; 0), Abbildung 4: (1; −1; 0); von oben: Z-förmige Figur aus den Strecken AB, BC, CD (amtlich)",
    zwischenergebnis="auch entgegengesetzte Vektoren möglich", niveau_geschaetzt="III",
    fehlerquelle="Blickrichtung (1; 0; 0) für die X-Form (ergibt ebenfalls ein X, richtig) – aber (1; 1; 0) für die Λ-Form (ergibt eine Strecke)",
    bemerkung="Standardbezug: K4 III. AB amtlich: III. Amtlich. Eichregel: (d) räumliche Lage in Projektionen übersetzen, verkettet über drei Ansichten.")

row("2022MerhoehtBAGLAA2WTR2", "g", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lösungsweg für einen Punkt mit gleichem Abstand zu drei Strecken über Lotfußpunkt und Abstandsgleichheit erläutern", typ_neben="",
    stichwoerter="Q Punkt auf AB (Gleichung I)|PQ · AB = 0: PQ senkrecht zu AB, |PQ| Abstand von P zu AB|28 − h Abstand von P(0|0|h) zur waagerechten Strecke BC in Höhe 28|Gleichsetzen liefert h",
    voraussetzungen="Abstand Punkt–Gerade über den Lotfußpunkt|Abstand zu einer waagerechten Strecke über der Achse|Symmetrie zu CD",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=SP, kontext="Saarpolygon/Denkmal", textumfang="lang",
    gegeben="P(0|0|h) im Quader mit gleichem Abstand zu AB, BC, CD; Gleichungssystem: I OQ = (11; 11; 0) + t · (−22; 0; 28), t ∈ [0; 1]; II PQ · AB = 0; III |PQ| = 28 − h",
    gesucht="Erläuterung der Überlegungen hinter dem Vorgehen",
    verfahren="I als Punkt auf AB, II als Lotbedingung, |PQ| als Abstand zu AB, 28 − h als Abstand zu BC, Gleichsetzen",
    schritte="3", zahlenraum="ganz", einheiten="m", abhaengig_von="",
    ergebnis="Q ist ein Punkt auf AB; gilt PQ · AB = 0, steht PQ senkrecht zu AB und |PQ| ist der Abstand von P zu AB; dieser Abstand muss mit 28 − h, dem Abstand von P zu BC, übereinstimmen (amtlich)",
    zwischenergebnis="h ≈ 16,9 nach eigener Rechnung", niveau_geschaetzt="III",
    fehlerquelle="28 − h nicht als Abstand zu BC erkennen (BC liegt über der x₃-Achse in Höhe 28)",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (h ≈ 16,86). Eichregel: (d) Gleichungen als Lot und Abstände deuten, verkettet mit der Symmetrie des Streckenzugs.")

# ---- Stochastik WTR 1: Krankenversicherung (Datenschutzbedenken D, Fitnessarmband F), Signifikanztest Armbänder
row("2022MerhoehtBStochastikWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm mit aus einer Pfadwahrscheinlichkeit erschlossener Einzelwahrscheinlichkeit erstellen", typ_neben="",
    stichwoerter="D 59 %, ¬D 41 %|D: F 23 %, ¬F 77 %|¬D: F x mit 0,41 · x = 0,19 ⇒ x ≈ 46 %, ¬F 54 %",
    voraussetzungen="Pfadregel rückwärts|Baum beschriften",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine; Erwartungshorizont: Baum D 59 % / ¬D 41 %, darunter F 23 % / ¬F 77 % bzw. F 46 % / ¬F 54 %", kontext="Versicherung/Datenschutz", textumfang="mittel",
    gegeben="59 % mit Datenschutzbedenken; davon 23 % mit Fitnessarmband; 19 % aller Kunden ohne Bedenken und mit Armband",
    gesucht="beschriftetes Baumdiagramm",
    verfahren="Anteil im Ast ¬D → F aus 0,41 · x = 0,19",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="D: Datenschutzbedenken, F: Fitnessarmband; 0,41 · x = 0,19 liefert x ≈ 46 %; Baumdiagramm mit 59 %/41 %, 23 %/77 %, 46 %/54 % (amtlich)",
    zwischenergebnis="x = 0,4634", niveau_geschaetzt="II",
    fehlerquelle="19 % direkt als Astwahrscheinlichkeit eintragen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Astanteil aus einer Pfadwahrscheinlichkeit erschließen), amtlich I. Typ wiederverwendet (Teil A).")

row("2022MerhoehtBStochastikWTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(D | F) = 0,59 · 0,23 / (0,59 · 0,23 + 0,19) ≈ 42 %",
    voraussetzungen="Satz von Bayes über Pfade",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Versicherung/Datenschutz", textumfang="kurz",
    gegeben="Person nutzt ein Fitnessarmband",
    gesucht="Wahrscheinlichkeit für Datenschutzbedenken",
    verfahren="Pfad D–F durch Summe der Pfade zu F",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2022MerhoehtBStochastikWTR1-1a",
    ergebnis="0,59 · 0,23 / (0,59 · 0,23 + 0,19) ≈ 42 % (amtlich)",
    zwischenergebnis="0,4166", niveau_geschaetzt="II",
    fehlerquelle="P(F | D) = 23 % als Antwort",
    bemerkung="Standardbezug: K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ea-B).")

row("2022MerhoehtBStochastikWTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen", typ_neben="",
    stichwoerter="0,23 = P(F | D)|0,59 · 0,23 + 0,19 = P(F)|ungleich ⇒ abhängig",
    voraussetzungen="Unabhängigkeit als P(F | D) = P(F)|Terme als Anteile deuten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Versicherung/Datenschutz", textumfang="mittel",
    gegeben="0,23 ≠ 0,59 · 0,23 + 0,19",
    gesucht="Begründung, dass D und F stochastisch abhängig sind",
    verfahren="Beide Terme als bedingten und unbedingten Anteil der Armbandnutzer deuten",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,23 ist der Anteil der Armbandnutzer unter den Kunden mit Datenschutzbedenken, 0,59 · 0,23 + 0,19 der Anteil unter allen Kunden; da die Anteile nicht übereinstimmen, sind die Ereignisse stochastisch abhängig (amtlich)",
    zwischenergebnis="P(F) = 0,3257", niveau_geschaetzt="II",
    fehlerquelle="Ungleichung nur wiederholen, ohne die Terme zu deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A), hier mit vorgegebenem Vergleich.")

row("2022MerhoehtBStochastikWTR1", "d", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X Anzahl mit Bedenken, n = 100, p = 0,59|P(X > 50) ≈ 96 %",
    voraussetzungen="„mehr als 50 %“ von 100 als X > 50|Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Versicherung/Datenschutz", textumfang="kurz",
    gegeben="100 zufällig ausgewählte Kunden; p = 0,59",
    gesucht="Wahrscheinlichkeit, dass mehr als 50 % Datenschutzbedenken haben",
    verfahren="Binomialverteilung am Rechner",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="X: Anzahl der Kunden mit Datenschutzbedenken; P₀,₅₉¹⁰⁰(X > 50) ≈ 96 % (amtlich)",
    zwischenergebnis="0,957", niveau_geschaetzt="I",
    fehlerquelle="X ≥ 50",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2022MerhoehtBStochastikWTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen", typ_neben="",
    stichwoerter="1 − Σ_{k=51}^{100} C(100; k) · 0,59^k · a^b|a = 0,41, b = 100 − k|Ereignis: höchstens die Hälfte hat Bedenken",
    voraussetzungen="Bernoulli-Formel|Gegenereignis der Summe",
    format="Kurzantwort", operator="Geben Sie an|Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Versicherung/Datenschutz", textumfang="mittel",
    gegeben="Term 1 − Σ_{k=51}^{100} C(100; k) · 0,59^k · a^b mit Platzhaltern a, b",
    gesucht="Ersetzung der Platzhalter; zugehöriges Ereignis",
    verfahren="Bernoulli-Formel vervollständigen, Summe als P(X ≥ 51), Gegenereignis beschreiben",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="a = 0,41, b = 100 − k; Ereignis: höchstens die Hälfte der ausgewählten Kunden hat Datenschutzbedenken (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Ereignis „mehr als die Hälfte“ (die Summe selbst) statt des Gegenereignisses",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2026-ga-B).")

row("2022MerhoehtBStochastikWTR1", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussage über die Halbierung einer Potenzwahrscheinlichkeit bei doppeltem Umfang allgemein widerlegen", typ_neben="",
    stichwoerter="P(niemand) bei n Kunden: 0,41ⁿ|bei 2n: 0,41²ⁿ = 0,41ⁿ · 0,41ⁿ|≠ 1/2 · 0,41ⁿ für alle n > 0 ⇒ kein solches n",
    voraussetzungen="Potenzgesetz|Gleichung 0,41ⁿ = 1/2 hat keine natürliche Lösung",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Versicherung/Datenschutz", textumfang="mittel",
    gegeben="Aussage: bei 2n Kunden ist P(niemand hat Bedenken) halb so groß wie bei n Kunden",
    gesucht="ob es ein n > 0 gibt, für das die Aussage richtig ist",
    verfahren="Beide Wahrscheinlichkeiten als Potenzen von 0,41 vergleichen",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="0,41²ⁿ = 0,41ⁿ · 0,41ⁿ ≠ 1/2 · 0,41ⁿ, d. h. es gibt keinen solchen Wert von n (amtlich)",
    zwischenergebnis="0,41ⁿ = 1/2 hätte n ≈ 0,78", niveau_geschaetzt="III",
    fehlerquelle="für einzelne n rechnen statt allgemein",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung III (allgemeiner Nachweis über das Potenzgesetz), amtlich II.")

row("2022MerhoehtBStochastikWTR1", "a", innen="2", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Stichprobenumfang eines Tests aus Ablehnungsgrenze und Fehler erster Art am Graphen ermitteln", typ_neben="",
    stichwoerter="Abbildung: bei p = 0,07 Fehler erster Art zwischen 0,095 und 0,1|P(Y ≤ 4) für n = 112: 0,101, n = 113: 0,097, n = 114: 0,093|n = 113",
    voraussetzungen="Fehler erster Art als P(Ablehnung | H₀ wahr)|Ablesen am Graphen|Probieren von n am Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze="Koordinatensystem p von 0,065 bis 0,085, Wahrscheinlichkeit 0 bis 0,1 (Raster 0,02); fallende Kurve des Fehlers erster Art von etwa 0,12 bei 0,065 über etwa 0,097 bei 0,07 bis etwa 0,025 bei 0,085", kontext="Fitnessarmbänder/Qualitätstest", textumfang="lang",
    gegeben="H₀: Anteil fehlerhafter Armbänder mindestens 7 %; Ablehnung bei höchstens vier fehlerhaften; Graph des Fehlers erster Art in Abhängigkeit von p",
    gesucht="Stichprobenumfang",
    verfahren="Fehler erster Art bei p = 0,07 ablesen, P(Y ≤ 4) für Nachbarwerte von n vergleichen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Die Abbildung liefert für p = 0,07 einen Wert zwischen 0,095 und 0,1; Y: Anzahl der fehlerhaften Armbänder; P₀,₀₇¹¹²(Y ≤ 4) ≈ 0,101, P₀,₀₇¹¹³(Y ≤ 4) ≈ 0,097, P₀,₀₇¹¹⁴(Y ≤ 4) ≈ 0,093; die Stichprobe hatte den Umfang 113 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Fehler erster Art an der falschen Stelle (p ≠ 0,07) ablesen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 III, K4 II, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Fehler erster Art am Graphen deuten, verkettet mit der Rückrechnung auf n.")

row("2022MerhoehtBStochastikWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Wahl der Nullhypothese aus der Sicht des Entscheiders begründen", typ_neben="",
    stichwoerter="Irrtum vermeiden, von zu geringem Anteil auszugehen (Reklamationen)|bei H₀: p ≥ 7 % ist dieses Risiko höchstens 9,7 %|umgekehrter Irrtum kann viel größer sein",
    voraussetzungen="Fehler erster Art als kontrolliertes Risiko|Folgen der Fehlentscheidung im Sachzusammenhang",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Fitnessarmbänder/Qualitätstest", textumfang="mittel",
    gegeben="Alternative Nullhypothese „Anteil höchstens 7 %“",
    gesucht="Überlegung des Händlers für die gewählte H₀ mit Begründung",
    verfahren="Kontrollierten Fehler dem für den Händler schädlichen Irrtum zuordnen",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="2022MerhoehtBStochastikWTR1-2a",
    ergebnis="Der Händler möchte vermeiden, irrtümlich von einem zu geringen Anteil fehlerhafter Armbänder auszugehen (etwa wegen vieler Reklamationen); bei der gewählten Nullhypothese beträgt das Risiko dafür höchstens 9,7 % und ist damit gering, die Wahrscheinlichkeit, irrtümlich von einem zu großen Anteil auszugehen, kann dagegen wesentlich größer sein (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Fehler zweiter Art als kontrolliert ansehen",
    bemerkung="Standardbezug: K1 III, K3 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (d) Fehlerarten im Sachzusammenhang deuten, verkettet mit der Interessenlage. Typ wiederverwendet (2024-ea-B).")

# ---- Stochastik WTR 2: Telefonanbieter (Tarife S, M, L; Hotline), Zahlenkombination, Wartezeit normalverteilt
row("2022MerhoehtBStochastikWTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Tabelle mit drei Spalten analog zur Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="S 20 %, L 25 % ⇒ M 55 %|M angerufen 27,5 %|S nicht angerufen 11 % ⇒ S angerufen 9 %|L angerufen 47 − 9 − 27,5 = 10,5 %, L nicht 14,5 %",
    voraussetzungen="Randsummen|Differenzen bilden",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="Tabelle", skizze="Tabelle 2 × 3 mit Randspalten: Zeilen Hotline angerufen / nicht angerufen, Spalten Tarif S, M, L, Summe 100 %", kontext="Telefonanbieter/Tarife", textumfang="mittel",
    gegeben="20 % Tarif S, 25 % L; 47 % haben angerufen, darunter die Hälfte der M-Kunden; 11 % haben S und nicht angerufen",
    gesucht="vollständige Tabelle",
    verfahren="M-Anteil als Rest, dann Zeilen und Spalten ergänzen",
    schritte="4", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="angerufen: S 9 %, M 27,5 %, L 10,5 %, gesamt 47 %; nicht angerufen: S 11 %, M 27,5 %, L 14,5 %, gesamt 53 %; Spalten 20 %, 55 %, 25 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="„die Hälfte der M-Kunden“ als 50 % aller Kunden lesen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Kein Rückgriff auf „Vierfeldertafel aus Anteilen vervollständigen“ (drei Spalten, Randanteil aus dem Rest, bedingter Anteil).")

row("2022MerhoehtBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="P(S | nicht angerufen) = 11 %/53 % ≈ 21 %",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient aus der Tabelle",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle wie in a", kontext="Telefonanbieter/Tarife", textumfang="kurz",
    gegeben="Kunde hat die Hotline noch nicht angerufen",
    gesucht="Wahrscheinlichkeit für Tarif S",
    verfahren="Schnittanteil durch Randanteil",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="2022MerhoehtBStochastikWTR2-1a",
    ergebnis="11 %/53 % ≈ 21 % (amtlich)",
    zwischenergebnis="0,2075", niveau_geschaetzt="I",
    fehlerquelle="11 %/20 % (Bedingung vertauscht)",
    bemerkung="Standardbezug: K3 II, K4 I, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung I (Quotient aus der fertigen Tabelle), amtlich II. Typ wiederverwendet (Teil A).")

row("2022MerhoehtBStochastikWTR2", "c", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Anteil eines Entweder-oder-Ereignisses aus einer Tafel berechnen", typ_neben="",
    stichwoerter="entweder L oder nicht angerufen: L∩angerufen 10,5 % + (S∩nicht 11 % + M∩nicht 27,5 %) = 49 %",
    voraussetzungen="„entweder – oder“ als ausschließendes Oder|Felder der Tabelle auswählen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle wie in a", kontext="Telefonanbieter/Tarife", textumfang="kurz",
    gegeben="Tabelle aus a",
    gesucht="Anteil der Kunden mit entweder Tarif L oder nicht angerufen",
    verfahren="Felder L∩angerufen und (S, M)∩nicht angerufen addieren",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="2022MerhoehtBStochastikWTR2-1a",
    ergebnis="10,5 % + 11 % + 27,5 % = 49 % (amtlich)",
    zwischenergebnis="alternativ P(L) + P(nicht) − 2 · P(L∩nicht) = 25 + 53 − 29", niveau_geschaetzt="II",
    fehlerquelle="Vereinigung (63,5 %) statt ausschließendem Oder",
    bemerkung="Standardbezug: K1 II, K4 I, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBStochastikWTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Σ_{i=470}^{490} C(600; i) 0,8^i 0,2^(600−i)|p = 0,8: Kunden mit Tarif M oder L|mindestens 470 und höchstens 490 der 600 Befragten",
    voraussetzungen="Summe als kumulierte Binomialwahrscheinlichkeit|0,8 als Gegenwahrscheinlichkeit zu S",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Telefonanbieter/Tarife", textumfang="mittel",
    gegeben="600 Befragte, Anzahl mit Tarif S binomialverteilt (p = 0,2); Term Σ_{i=470}^{490} C(600; i) · 0,8^i · 0,2^(600−i)",
    gesucht="Bedeutung im Sachzusammenhang",
    verfahren="0,8 als Anteil M oder L erkennen, Grenzen übersetzen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Der Term gibt die Wahrscheinlichkeit dafür an, dass mindestens 470 und höchstens 490 der befragten Kunden einen der Tarife M und L haben (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="0,8 als Tarif S lesen",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2025-ga-B).")

row("2022MerhoehtBStochastikWTR2", "e", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Größtes k mit kumulierter Wahrscheinlichkeit unter einer Schranke mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X Anzahl mit Tarif S, n = 600, p = 0,2|P(X < 113) ≈ 22 %, P(X < 114) ≈ 26 %|k = 113",
    voraussetzungen="„weniger als k“ als X ≤ k − 1|Nachbarwerte am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Telefonanbieter/Tarife", textumfang="kurz",
    gegeben="Befragung wie in d; Schranke 25 %",
    gesucht="größtes k mit P(X < k) < 25 %",
    verfahren="Kumulierte Wahrscheinlichkeiten um μ − 0,67σ probieren",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="X: Anzahl der Kunden mit Tarif S; P₀,₂⁶⁰⁰(X < 113) ≈ 22 % und P₀,₂⁶⁰⁰(X < 114) ≈ 26 %, d. h. k = 113 (amtlich)",
    zwischenergebnis="μ = 120, σ ≈ 9,8", niveau_geschaetzt="II",
    fehlerquelle="k = 114 (Grenze mit ≤ statt <)",
    bemerkung="Standardbezug: K1 I, K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Spiegelbild von „Kleinstes k mit kumulierter Wahrscheinlichkeit über einer Schranke mit dem Rechner ermitteln“ – Vorschlag für den Abgleich: zu einem Etikett zusammenziehen.")

row("2022MerhoehtBStochastikWTR2", "", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl der Zahlenkombinationen mit einer vierfachen Ziffer aus drei Ziffern berechnen", typ_neben="",
    stichwoerter="3 Wahlen für die vierfache Ziffer|C(6; 2) Plätze für die beiden anderen|2 Anordnungen ⇒ 3 · 15 · 2 = 90",
    voraussetzungen="Produktregel|Binomialkoeffizient für Positionen|alle drei Ziffern kommen vor",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Telefonanbieter/Tarife", textumfang="mittel",
    gegeben="sechsstellige Kombination aus den Ziffern 1, 5, 9, alle kommen vor, eine Ziffer viermal",
    gesucht="Anzahl der möglichen Kombinationen",
    verfahren="Vierfache Ziffer wählen, Plätze der beiden übrigen wählen, deren Reihenfolge",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="3 · C(6; 2) · 2 = 90 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Reihenfolge der beiden Einzelziffern (Faktor 2) vergessen",
    bemerkung="Standardbezug: K1 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2022MerhoehtBStochastikWTR2", "a", innen="3", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Maximale Wahrscheinlichkeit eines Intervalls fester Länge über die Lage um den Erwartungswert begründen", typ_neben="",
    stichwoerter="symmetrisches Intervall um μ hat die größte Wahrscheinlichkeit, unabhängig von μ|σ = 1,25: P(μ − 1 ≤ Y ≤ μ + 1) ≈ 57,6 % < 60 %|kein solches Intervall",
    voraussetzungen="Dichte maximal um μ|Symmetrie der Normalverteilung|Rechner",
    format="Begründung|Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Telefonanbieter/Tarife", textumfang="mittel",
    gegeben="Wartezeit normalverteilt mit σ = 1 min 15 s; Erwartungswert unbekannt",
    gesucht="ob ein zweiminütiges Intervall mit Wahrscheinlichkeit mindestens 60 % existiert",
    verfahren="Bestes Intervall symmetrisch um μ, Wahrscheinlichkeit mit beliebigem μ berechnen und mit 60 % vergleichen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="min", abhaengig_von="",
    ergebnis="Unter allen Zeitintervallen der Länge zwei Minuten hat das zum Erwartungswert symmetrische die größte Wahrscheinlichkeit, deren Wert unabhängig vom Erwartungswert ist; Y: Wartezeit; P₁;₁,₂₅(0 ≤ Y ≤ 2) < 60 %, es gibt kein solches Zeitintervall (amtlich)",
    zwischenergebnis="0,576", niveau_geschaetzt="III",
    fehlerquelle="μ als unbekannt für unlösbar halten",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Symmetrie und Lage um μ als Extremfall erkennen.")

row("2022MerhoehtBStochastikWTR2", "b", innen="3", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Erwartungswert einer Normalverteilung aus einer Wahrscheinlichkeitsvorgabe ermitteln und weitere Wahrscheinlichkeit berechnen", typ_neben="",
    stichwoerter="P(Y ≤ 3) = 15 % mit σ = 1,25|μ = 4,2: 16,9 %, μ = 4,3: 14,9 % ⇒ μ ≈ 4,3|P(Y ≥ 5) ≈ 29 %",
    voraussetzungen="Rückwärtsrechnung über Probieren oder Quantil|Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Telefonanbieter/Tarife", textumfang="mittel",
    gegeben="P(Y ≤ 3) = 15 %, σ = 1,25",
    gesucht="P(Y ≥ 5) unter dieser Annahme",
    verfahren="μ aus der Vorgabe ermitteln, dann die Wahrscheinlichkeit berechnen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="min", abhaengig_von="",
    ergebnis="Mit P₄,₂;₁,₂₅(Y ≤ 3) ≈ 16,9 % und P₄,₃;₁,₂₅(Y ≤ 3) ≈ 14,9 % ergibt sich μ ≈ 4,3; P₄,₃;₁,₂₅(Y ≥ 5) ≈ 29 % (amtlich)",
    zwischenergebnis="μ = 3 + 1,036 · 1,25 ≈ 4,30", niveau_geschaetzt="III",
    fehlerquelle="μ = 3 setzen",
    bemerkung="Standardbezug: K2 III, K3 I, K5 II, K6 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Vorgabe in eine Bedingung an μ übersetzen, verkettet mit der zweiten Wahrscheinlichkeit.")

NEUE_TYPEN = [
    ("Nullstellen und Werte: Funktionswert und Änderungsbeträge zweier Zeitabschnitte im Sachzusammenhang vergleichen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Einen Funktionswert einer Modellfunktion berechnen und die Differenzen der Funktionswerte über zwei gleich lange Zeitabschnitte berechnen und vergleichen.", "2022MerhoehtBAnalysisWTR1-1a"),
    ("Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen", "Analysis", "Kurvenuntersuchung",
     "Den Zeitpunkt der stärksten Abnahme einer Größe rechnerisch als Minimum der Ableitung bestimmen (Nullstellensymmetrie der quadratischen Ableitung oder zweite Ableitung).", "2022MerhoehtBAnalysisWTR1-1b"),
    ("Zurückgelegte Strecke als Integral der Geschwindigkeit mit Umrechnung der Einheiten berechnen", "Analysis", "Rekonstruktion von Beständen",
     "Die in einem Zeitraum zurückgelegte Strecke als Integral über die Geschwindigkeitsfunktion berechnen und die Zeiteinheit (Minuten gegen Stunden) umrechnen.", "2022MerhoehtBAnalysisWTR1-1c"),
    ("Aussage über den Bremsweg bei konstanter Abnahme über die Tangente und ein Dreieck untersuchen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Eine gleichbleibende Abnahme ab einem Zeitpunkt als Tangente modellieren, den Stillstand als Nullstelle der Tangente bestimmen und den Weg als Dreiecksfläche unter der Tangente mit Einheitenumrechnung prüfen.", "2022MerhoehtBAnalysisWTR1-1d"),
    ("Bedingungen für den sprungfreien Übergang von Funktionswert und Ableitung angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus dem sprungfreien Anschluss an einen konstanten Verlauf die Bedingungen f_p(x₀) = c und f_p'(x₀) = 0 angeben.", "2022MerhoehtBAnalysisWTR1-1e"),
    ("Scharparameter der Ausgangsfunktion angeben und Eignung zweier Scharfunktionen am Graphen beurteilen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameterwert angeben, für den die Schar die Ausgangsfunktion liefert, und für zwei abgebildete Scharfunktionen über Extrempunkte im Intervall beurteilen, ob sie den Sachverhalt beschreiben können.", "2022MerhoehtBAnalysisWTR1-1f"),
    ("Eignung der Scharfunktionen über die Lage einer dritten Extremstelle beurteilen", "Analysis", "Funktionsscharen und Ortskurven",
     "Mit vorgegebenen Informationen über die parameterabhängige dritte Nullstelle der Ableitung die Parameterwerte angeben, für die im Intervall kein Extremum liegt, und daraus die Eignung beurteilen.", "2022MerhoehtBAnalysisWTR1-1g"),
    ("Parameter einer Sinusfunktion aus zwei aufeinanderfolgenden Extrempunkten bestimmen", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Amplitude als halbe Differenz der Extremwerte und den Frequenzparameter aus dem Abstand zweier aufeinanderfolgender Extremstellen (halbe Periode) bestimmen.", "2022MerhoehtBAnalysisWTR1-2a"),
    ("Integralwert: Integralwert über die Punktsymmetrie und ein Quadrat geometrisch begründen", "Analysis", "Flächeninhalt durch Integration",
     "Den Wert eines Integrals über ein zum Symmetriepunkt symmetrisches Intervall geometrisch begründen: gleich große Flächenstücke über die Punktsymmetrie umlegen, sodass ein Quadrat entsteht.", "2022MerhoehtBAnalysisWTR1-2b"),
    ("Wendestellen einer Sinusfunktion als ganzzahlig nachweisen und die beiden Wendetangentensteigungen zeigen", "Analysis", "Kurvenuntersuchung",
     "Die Wendestellen einer verschobenen Sinusfunktion über die Nullstellen des Sinus als Vielfache einer ganzen Zahl nachweisen und über die Ableitung zeigen, dass die Steigung dort nur zwei Werte annimmt.", "2022MerhoehtBAnalysisWTR1-2c"),
    ("Tangente durch einen entfernten Punkt über die Rationalität der Steigung ausschließen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Für Geraden durch die Wendepunkte und einen festen Punkt die Steigung allgemein bilden und über rational gegen irrational (±π/2) ausschließen, dass eine davon Tangente ist.", "2022MerhoehtBAnalysisWTR1-2d"),
    ("Symmetrie: Punktsymmetrie über f(−x) = −f(x) nachweisen, eindeutige Nullstelle begründen und Grenzwert angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Am Term f(−x) = −f(x) nachweisen, über den positiven Exponentialfaktor die einzige Nullstelle begründen und den Grenzwert für x → +∞ angeben.", "2022MerhoehtBAnalysisWTR2-1a"),
    ("Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden", "Analysis", "Ableitungsregeln",
     "Die Ableitung eines Terms x · e^(g(x)) mit Produkt- und Kettenregel bilden und den gemeinsamen Faktor ausklammern.", "2022MerhoehtBAnalysisWTR2-1b"),
    ("Koordinatenachsen zu einem gegebenen Graphen ergänzen und skalieren", "Analysis", "Kurvenuntersuchung",
     "In eine Abbildung eines Graphen ohne Koordinatensystem die Achsen so einzeichnen und skalieren, dass Symmetrie und berechnete markante Punkte (etwa ein Hochpunkt) stimmen.", "2022MerhoehtBAnalysisWTR2-1c"),
    ("Integral über eine vorgegebene Regel für g' · e^g berechnen", "Analysis", "Integrationsregeln",
     "Einen Integranden in die Form g'(x) · e^(g(x)) bringen (Vorzeichen anpassen) und das Integral mit der vorgegebenen Regel [e^(g(x))] berechnen.", "2022MerhoehtBAnalysisWTR2-1d"),
    ("Näherung eines Integrals mit großer oberer Grenze durch ein festes Integral geometrisch deuten", "Analysis", "Uneigentliche Integrale",
     "Die Aussage F(w) − F(0) ≈ ∫₀^c f für alle w > c als Aussage über Flächenstücke unter einem gegen null gehenden Graphen deuten.", "2022MerhoehtBAnalysisWTR2-1e"),
    ("Steigung und Achsenschnittpunkt des linearen Sonderfalls einer Schar angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Für den Parameterwert, bei dem die Scharfunktion linear wird, Steigung und Schnittpunkt mit der y-Achse angeben.", "2022MerhoehtBAnalysisWTR2-2b"),
    ("Folgerungen aus gemeinsamen Eigenschaften einer Schar für den Verlauf der Graphen angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Vorgegebene Aussagen über Funktionswerte, Ableitungswerte und gemeinsame Punkte der Scharfunktionen in Aussagen über die Lage der Graphen zueinander übersetzen.", "2022MerhoehtBAnalysisWTR2-2c"),
    ("Gleichmäßige Streckung eines Scharfgraphen als Graph einer anderen Scharfunktion nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Nachweisen, dass k · f_a(x/k) wieder eine Funktion der Schar ist, und den zugehörigen Parameter angeben.", "2022MerhoehtBAnalysisWTR2-2d"),
    ("Parameterwerte nach der Anzahl der Extrempunkte über die Lösbarkeit der Extremstellengleichung begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus der Lösungsanzahl einer vorgegebenen Gleichung für die Extremstellen (etwa a · x² = 1) die Parameterbereiche mit zwei bzw. keinem Extrempunkt angeben und begründen.", "2022MerhoehtBAnalysisWTR2-2e"),
    ("Ortskurve der Extrempunkte einer Schar als Gerade über Sonderfall und Streckungseigenschaft begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Begründen, dass alle Extrempunkte einer Schar auf y = x liegen, über einen Sonderfall mit bekanntem Extrempunkt und Symmetrie sowie die Streckungseigenschaft der Schar.", "2022MerhoehtBAnalysisWTR2-2f"),
    ("Scharparameter für einen vorgegebenen Flächeninhalt eines Vierecks aus Hochpunkt und Achsenpunkten bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Ein Viereck aus Hochpunkt, Achsenpunkten und Ursprung skizzieren, seinen Flächeninhalt als Term in der Extremstelle ausdrücken, aus dem vorgegebenen Inhalt die Extremstelle und daraus den Parameter bestimmen.", "2022MerhoehtBAnalysisWTR2-2g"),
    ("Anfangswert angeben und Stelle für einen vorgegebenen Wert einer Exponentialfunktion berechnen", "Analysis", "Gleichungen lösen",
     "Den Wert einer Exponentialfunktion an der Stelle 0 angeben und die Stelle zu einem vorgegebenen Funktionswert über den Logarithmus berechnen.", "2022MerhoehtBAnalysisWTR3-1a"),
    ("Logarithmus einer Exponentialfunktion als lineare Funktion nachweisen und Steigung und Achsenabschnitt angeben", "Analysis", "Kurvenuntersuchung",
     "Mit den Logarithmengesetzen zeigen, dass h ↦ ln(c · e^(kh)) linear ist, und Steigung und Schnittpunkt mit der y-Achse angeben.", "2022MerhoehtBAnalysisWTR3-1c"),
    ("Stammfunktion eines Polynomterms nach dem Ausmultiplizieren angeben", "Analysis", "Stammfunktion und Hauptsatz",
     "Einen in Klammern gegebenen Integranden ausmultiplizieren und gliedweise eine Stammfunktion angeben.", "2022MerhoehtBAnalysisWTR3-2a"),
    ("Integranden als Querschnittsfläche über den Satz des Pythagoras deuten und Umrechnungsfaktor erläutern", "Analysis", "Rotationsvolumen",
     "Den Integranden eines Volumenintegrals als Flächeninhalt eines Kreisschnitts deuten, den Radius an der Abbildung über den Satz des Pythagoras begründen und einen Vorfaktor als Einheitenumrechnung erläutern.", "2022MerhoehtBAnalysisWTR3-2b"),
    ("Wendestelle einer Integralfunktion über die Ableitung des Integranden begründen und Funktionswert berechnen", "Analysis", "Stammfunktion und Hauptsatz",
     "Die Wendestelle einer Integralfunktion über die Nullstelle der Ableitung des Integranden (zweite Ableitung) begründen und den Funktionswert dort berechnen.", "2022MerhoehtBAnalysisWTR3-2c"),
    ("Nullstellen und Werte: Minimalwert einer verschobenen Sinusfunktion begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den kleinsten Wert von a · sin(bx) + c über den Wertebereich des Sinus begründen.", "2022MerhoehtBAnalysisWTR3-3a"),
    ("Alle Zeitpunkte für einen Wert einer Sinusfunktion in einem Intervall berechnen", "Analysis", "Gleichungen lösen",
     "Die Gleichung a · sin(bx) + c = d nach dem Sinus auflösen, alle Lösungen über die Symmetrie zu π/2 und die Periode bilden und die im Intervall liegenden angeben.", "2022MerhoehtBAnalysisWTR3-3b"),
    ("Nullstellen und Werte: Wert einer Funktion berechnen und die zugehörige Stelle einer zweiten Funktion am Graphen ablesen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Einen Funktionswert eines ersten Modells berechnen und am Graphen eines zweiten Modells die Stelle ablesen, an der dieser Wert angenommen wird (Verkettung zweier Modelle).", "2022MerhoehtBAnalysisWTR3-3c"),
    ("Rechten Winkel zwischen zwei Seiten einer Figur über das Skalarprodukt nachweisen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Nachweisen, dass zwei Seiten einer Figur einen rechten Winkel einschließen, indem das Skalarprodukt der Seitenvektoren null ist.", "2022MerhoehtBAGLAA1WTR-1a"),
    ("Vierten Eckpunkt eines Quadrats über eine Vektoraddition bestimmen", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Den fehlenden Eckpunkt eines Quadrats aus drei gegebenen Ecken über die Addition eines Seitenvektors bestimmen.", "2022MerhoehtBAGLAA1WTR-1b"),
    ("Gleichschenkligkeit eines dritten Dreiecks aus zwei Gleichschenkligkeiten begründen", "Analytische Geometrie", "Abstände",
     "Ohne Rechnung begründen, dass aus gleichen Abständen eines Punktes zu B und C sowie zu B und D auch die Gleichheit der Abstände zu C und D folgt.", "2022MerhoehtBAGLAA1WTR-1c"),
    ("Übergangsprozess: Verhältnis der Anfangsbestände aus einer Gleichverteilung nach einem Übergang bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus M · v = w mit teilweise bekanntem v und bekanntem w die unbekannten Komponenten von v über ein Gleichungssystem bestimmen und ihr Verhältnis angeben.", "2022MerhoehtBAGLAA1WTR-2b"),
    ("Matrizenalgebra: Parameterbereich für endliche Grenzwerte der Matrixpotenzen über eine Potenzfolge bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus der vorgegebenen Form der Matrixpotenzen die Parameterwerte bestimmen, für die alle Einträge für k → ∞ endlich bleiben (Grenzverhalten einer geometrischen Folge).", "2022MerhoehtBAGLAA1WTR-2c"),
    ("Übergangsprozess: Übergangsverhalten einer parametrisierten Matrix nach Fällen im Sachzusammenhang beschreiben", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Die Übergänge einer Matrix mit Parameter nach Fällen (Randwerte, Zwischenbereich) im Sachzusammenhang beschreiben, einschließlich des langfristigen Verhaltens aus der Grenzmatrix.", "2022MerhoehtBAGLAA1WTR-2d"),
    ("Ebene Figur: Gleichschenkligkeit über kongruente rechtwinklige Dreiecke begründen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Die Gleichschenkligkeit eines Dreiecks begründen, indem zwei Seiten als Hypotenusen kongruenter rechtwinkliger Dreiecke mit gleichen Katheten erkannt werden.", "2022MerhoehtBAGLAA2WTR1-1a"),
    ("Scharparameter für einen vorgegebenen Schnittwinkel zwischen Achse und Ebene ermitteln", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Den Parameter einer Ebenenschar so bestimmen, dass der Winkel zwischen einer Koordinatenachse und der Ebene einen vorgegebenen Wert hat (Sinusformel mit parameterabhängigem Normalenvektor).", "2022MerhoehtBAGLAA2WTR1-1d"),
    ("Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Die Parameterwerte bestimmen, bei denen eine Ebene der Schar Quaderecken enthält, und für die Bereiche dazwischen die Eckenzahl der Schnittfigur angeben.", "2022MerhoehtBAGLAA2WTR1-1f"),
    ("Punkt: Koordinaten eines Punktes auf einer Strecke in Abhängigkeit von seiner Höhe ermitteln", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Einen Punkt auf einer Strecke (etwa der Mittellinie einer Pyramidenfläche) in Abhängigkeit von seiner Höhe über die Parameterform der Strecke ermitteln.", "2022MerhoehtBAGLAA2WTR1-1g"),
    ("Symmetrie zweier Punkte bezüglich einer Koordinatenachse über die Koordinaten begründen", "Analytische Geometrie", "Spiegelung",
     "Begründen, dass zwei Punkte symmetrisch zu einer Koordinatenachse liegen, weil zwei Koordinaten entgegengesetzt und die dritte gleich sind.", "2022MerhoehtBAGLAA2WTR2-1a"),
    ("Körper: Länge eines Streckenzugs aus Kanten und Diagonalen eines Quaders im Sachzusammenhang berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Die Gesamtlänge eines Streckenzugs aus mehreren Strecken über die Beträge der Verbindungsvektoren mit Maßstab berechnen.", "2022MerhoehtBAGLAA2WTR2-1b"),
    ("Winkel zwischen zwei spiegelbildlichen Ebenen als Term im Neigungswinkel angeben", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Für zwei zur Grundebene spiegelbildliche Ebenen den Winkel zwischen ihnen als Term im Neigungswinkel gegen die Grundebene angeben (180° − 2φ).", "2022MerhoehtBAGLAA2WTR2-1d"),
    ("Körper: Volumenanteil einer Pyramide am Quader ohne Volumenberechnung begründen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Anteil eines pyramidenförmigen Teilkörpers am Quader über Grundfläche als halbe Seitenfläche und Faktor 1/3 begründen, ohne Volumina zu berechnen.", "2022MerhoehtBAGLAA2WTR2-1e"),
    ("Blickrichtungsvektoren zu schematischen Ansichten angeben und eine weitere Ansicht zeichnen", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Zu schematischen Ansichten eines Streckenzugs passende Blickrichtungsvektoren angeben und die Ansicht aus einer weiteren Richtung (von oben) zeichnen.", "2022MerhoehtBAGLAA2WTR2-1f"),
    ("Lösungsweg für einen Punkt mit gleichem Abstand zu drei Strecken über Lotfußpunkt und Abstandsgleichheit erläutern", "Analytische Geometrie", "Abstände",
     "Ein vorgegebenes Gleichungssystem (Punkt auf einer Strecke, Lotbedingung, Gleichheit zweier Abstände) als Weg zum Punkt mit gleichem Abstand zu mehreren Strecken erläutern.", "2022MerhoehtBAGLAA2WTR2-1g"),
    ("Aussage über die Halbierung einer Potenzwahrscheinlichkeit bei doppeltem Umfang allgemein widerlegen", "Stochastik", "Binomialverteilung",
     "Über das Potenzgesetz q^(2n) = q^n · q^n allgemein zeigen, dass die Wahrscheinlichkeit für null Treffer bei doppeltem Umfang für kein n halb so groß ist.", "2022MerhoehtBStochastikWTR1-1f"),
    ("Stichprobenumfang eines Tests aus Ablehnungsgrenze und Fehler erster Art am Graphen ermitteln", "Stochastik", "Hypothesentests",
     "Den Fehler erster Art an der Grenze der Nullhypothese am Graphen ablesen und den Stichprobenumfang durch Vergleich kumulierter Wahrscheinlichkeiten für benachbarte n ermitteln.", "2022MerhoehtBStochastikWTR1-2a"),
    ("Tabelle mit drei Spalten analog zur Vierfeldertafel aus Anteilen vervollständigen", "Stochastik", "Vierfeldertafel",
     "Eine Tafel mit zwei Zeilen und drei Spalten aus Rand-, Schnitt- und bedingten Anteilen vollständig ausfüllen.", "2022MerhoehtBStochastikWTR2-1a"),
    ("Anteil eines Entweder-oder-Ereignisses aus einer Tafel berechnen", "Stochastik", "Ereignisse und Mengenoperationen",
     "Den Anteil für „entweder A oder B“ (ausschließendes Oder) als Summe der passenden Felder einer Tafel berechnen.", "2022MerhoehtBStochastikWTR2-1c"),
    ("Größtes k mit kumulierter Wahrscheinlichkeit unter einer Schranke mit dem Rechner ermitteln", "Stochastik", "Binomialverteilung",
     "Das größte k ermitteln, für das P(X < k) eine vorgegebene Schranke unterschreitet, mit beiden Nachbarwerten am Rechner.", "2022MerhoehtBStochastikWTR2-1e"),
    ("Anzahl der Zahlenkombinationen mit einer vierfachen Ziffer aus drei Ziffern berechnen", "Stochastik", "Kombinatorik",
     "Die Anzahl der Ziffernfolgen fester Länge berechnen, in denen drei vorgegebene Ziffern vorkommen und eine davon mehrfach: Wahl der Mehrfachziffer, Plätze der übrigen, deren Reihenfolge.", "2022MerhoehtBStochastikWTR2-2"),
    ("Maximale Wahrscheinlichkeit eines Intervalls fester Länge über die Lage um den Erwartungswert begründen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Begründen, dass ein Intervall fester Länge symmetrisch um den Erwartungswert die größte Wahrscheinlichkeit hat, diese unabhängig von μ berechnen und mit einer Schranke vergleichen.", "2022MerhoehtBStochastikWTR2-3a"),
    ("Erwartungswert einer Normalverteilung aus einer Wahrscheinlichkeitsvorgabe ermitteln und weitere Wahrscheinlichkeit berechnen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Bei bekannter Standardabweichung μ aus einer vorgegebenen Unterschreitungswahrscheinlichkeit ermitteln (Probieren oder Quantil) und damit eine weitere Wahrscheinlichkeit berechnen.", "2022MerhoehtBStochastikWTR2-3b"),
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
    ist die Aufgabe ungegliedert (Kennung, '', ''); in Teil B kann eine nummerierte
    Aufgabe ohne Buchstaben stehen (Kennung-3, Buchstabe '')."""
    m = re.fullmatch(r"(" + KENNUNG.pattern + r")(?:-(?=.)(\d*)([a-z]?))?", i)
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
            # v0.9: Dubletten eines angefangenen Stapels zeigen auf erfasste Dateien
            for k, q in QUELLE.items():
                if einheit(q) == s and q["dublette_von"]:
                    a(q["dublette_von"] in kennungen,
                      f"Stapel {s}: {k} ist Dublette von {q['dublette_von']}, die nicht im Katalog steht")
        je_datei = {}
        for z in alt:
            k_, innen_, _ = kennung_aus_id(z["id"])
            je_datei.setdefault((k_, innen_), []).append(z["teilaufgabe"])
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
        je_datei.setdefault((z["_kennung"], kennung_aus_id(z["id"])[1]), []).append(z["teilaufgabe"])
    for k, tl in je_datei.items():
        a("" not in tl or len(tl) == 1, f"{k}: ungegliederte Aufgabe neben gegliederten Zeilen")
    fehlt = sorted(im_stapel - dubletten - dateien)
    if fehlt and not probe:
        a(False, f"Stapel {stapel} unvollständig, es fehlen {len(fehlt)} Dateien: {fehlt}")
    elif fehlt:
        warnung.append(f"Probelauf: {len(fehlt)} von {len(im_stapel - dubletten)} Dateien des Stapels fehlen noch")
    if dubletten:
        warnung.append(f"{len(dubletten)} Dubletten im Stapel ohne Zeile: {sorted(dubletten)}")
    # Teil B, MMS/CAS als Delta (v0.9): eine Dublette verweist auf die erste
    # Datei (WTR), deren Zeilen müssen schon im Katalog stehen – sonst fehlt
    # die Aufgabe im Bestand, wenn der WTR-Zweig später erfasst wird.
    alt_kennungen = {kennung_aus_id(z["id"])[0] for z in alt}
    for k in sorted(dubletten):
        erste = QUELLE[k]["dublette_von"]
        a(erste in alt_kennungen or erste in dateien,
          f"{k}: Dublette von {erste}, aber {erste} ist noch nicht erfasst (erste Datei zuerst)")
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
