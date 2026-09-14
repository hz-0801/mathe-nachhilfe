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
    "stapel": "2023-ea-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2023MerhoehtBAnalysisWTR1": 40,
        "2023MerhoehtBAnalysisWTR2": 40,
        "2023MerhoehtBAGLAA1WTR": 25,
        "2023MerhoehtBAGLAA2WTR1": 25,
        "2023MerhoehtBAGLAA2WTR2": 25,
        "2023MerhoehtBStochastikWTR1": 25,
        "2023MerhoehtBStochastikWTR2": 25,
        "2023MerhoehtBStochastikWTR3": 25,
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
# Stapel 2023-ea-B, WTR-Zweig. innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Pool 2023 erhöht: Analysis 40 BE, AG/LA und Stochastik 25 BE.

SOLL = {"2023MerhoehtBAnalysisWTR1": 40, "2023MerhoehtBAnalysisWTR2": 40,
        "2023MerhoehtBAGLAA1WTR": 25, "2023MerhoehtBAGLAA2WTR1": 25, "2023MerhoehtBAGLAA2WTR2": 25,
        "2023MerhoehtBStochastikWTR1": 25, "2023MerhoehtBStochastikWTR2": 25, "2023MerhoehtBStochastikWTR3": 25}

# ---- Analysis WTR 1, Aufgabe 1: Stau, f(x) = x(8 − 5x)(1 − x/4)², s(x) = (x/4)²(4 − x)³
ST = "Abbildung 1: Koordinatensystem ohne Skalierung außer 0 und 4 auf der x-Achse; Graph von f für 0 ≤ x ≤ 4: von (0 | 0) steil zu einem Hochpunkt bei etwa x = 0,6, fallend durch die Nullstelle 1,6, Tiefpunkt bei etwa 2,6, zurück auf null bei x = 4 (Berührung)"
row("2023MerhoehtBAnalysisWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstellen aus Linearfaktoren im Sachzusammenhang nennen und ihre Vollständigkeit über die Faktorstruktur begründen", typ_neben="",
    stichwoerter="Faktoren x, 8 − 5x, (1 − x/4)²|Nullstellen 0, 8/5, 4|06:00, 07:36, 10:00 Uhr|vier Linearfaktoren, zwei gleich ⇒ genau drei Nullstellen",
    voraussetzungen="Nullstellen aus Faktoren|Stunden in Uhrzeit umrechnen",
    format="Kurzantwort|Begründung", operator="Nennen Sie|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ST, kontext="Verkehr/Stau", textumfang="lang",
    gegeben="f(x) = x · (8 − 5x) · (1 − x/4)² = −5/16x⁴ + 3x³ − 9x² + 8x, x Stunden nach 06:00 Uhr, f(x) Änderungsrate der Staulänge in km/h; Stau von 06:00 bis 10:00 Uhr; f'(x) = (5x² − 16x + 8)(1 − x/4)",
    gesucht="Zeitpunkte mit Änderungsrate null; Begründung, dass es keine weiteren gibt",
    verfahren="Nullstellen der Linearfaktoren ablesen, Anzahl über die Faktorstruktur begründen",
    schritte="2", zahlenraum="Bruch", einheiten="Uhr", abhaengig_von="",
    ergebnis="06:00 Uhr, 07:36 Uhr, 10:00 Uhr; der Term von f besteht aus vier Linearfaktoren, von denen zwei übereinstimmen, damit hat f genau drei Nullstellen (amtlich)",
    zwischenergebnis="Nullstellen 0, 8/5, 4", niveau_geschaetzt="II",
    fehlerquelle="8/5 h als 8:05 Uhr statt 07:36 Uhr",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Vollständigkeit über die Faktorstruktur begründen), amtlich I.")

row("2023MerhoehtBAnalysisWTR1", "b", innen="1", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Negativen Wert einer Änderungsrate im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="f(2) < 0|um 08:00 Uhr nimmt die Staulänge ab",
    voraussetzungen="Vorzeichen der Rate als Zu- oder Abnahme",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=ST, kontext="Verkehr/Stau", textumfang="kurz",
    gegeben="f wie in a; f(2) < 0",
    gesucht="Bedeutung im Sachzusammenhang",
    verfahren="Negative Rate als Abnahme deuten, x = 2 als 08:00 Uhr",
    schritte="1", zahlenraum="ganz|negativ", einheiten="Uhr", abhaengig_von="",
    ergebnis="Um 08:00 Uhr nimmt die Staulänge ab (amtlich)",
    zwischenergebnis="f(2) = −1", niveau_geschaetzt="I",
    fehlerquelle="negative Staulänge statt Abnahme",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAnalysisWTR1", "c", innen="1", seite="2", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Zeitpunkt der größten Rate aus der Ableitung angeben", typ_neben="",
    stichwoerter="f'(x) = 0 ⇔ 5x² − 16x + 8 = 0 ∨ x = 4|x₁ = 8/5 − √(64/25 − 8/5) ≈ 0,62, x₂ ≈ 2,58|Maximum von f bei x₁ laut Abbildung|stärkste Zunahme etwa 0,62 h nach 06:00 Uhr",
    voraussetzungen="Stärkste Zunahme als Maximum der Rate|quadratische Gleichung|Abbildung zur Auswahl",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ST, kontext="Verkehr/Stau", textumfang="kurz",
    gegeben="f und f' wie in a; Graph in Abbildung 1",
    gesucht="Zeitpunkt der stärksten Zunahme der Staulänge, rechnerisch",
    verfahren="Nullstellen von f' berechnen und mit der Abbildung das Maximum von f auswählen",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="h", abhaengig_von="",
    ergebnis="f'(x) = 0 ⇔ x² − 16/5x + 8/5 = 0 ∨ x = 4; x₁ = 8/5 − √((8/5)² − 8/5) ≈ 0,62 und x₂ ≈ 2,58; nach der Abbildung nimmt f bei x₁ sein Maximum an, die Staulänge nimmt etwa 0,62 Stunden nach 06:00 Uhr am stärksten zu (amtlich)",
    zwischenergebnis="x₁ ≈ 0,620, x₂ ≈ 2,580", niveau_geschaetzt="II",
    fehlerquelle="x₂ (Minimum von f, stärkste Abnahme) als Antwort",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Rate maximieren, Lösung über die Abbildung auswählen), amtlich I. Typ wiederverwendet (Teil A), hier mit quadratischer Gleichung.")

row("2023MerhoehtBAnalysisWTR1", "d", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen", typ_neben="",
    stichwoerter="Staulänge nimmt zu, solange f(x) > 0|Vorzeichenwechsel bei 8/5|längster Stau um 07:36 Uhr",
    voraussetzungen="Rate positiv heißt Bestand wächst|Nullstelle mit Vorzeichenwechsel",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ST, kontext="Verkehr/Stau", textumfang="kurz",
    gegeben="f wie in a mit Nullstellen 0, 8/5, 4",
    gesucht="Zeitpunkt des längsten Staus mit Begründung",
    verfahren="Bestand wächst genau bei positiver Rate, also bis zur Nullstelle mit Vorzeichenwechsel",
    schritte="1", zahlenraum="Bruch", einheiten="Uhr", abhaengig_von="2023MerhoehtBAnalysisWTR1-1a",
    ergebnis="Die Länge des Staus nimmt genau dann zu, wenn f(x) > 0 gilt; damit ist der Stau um 07:36 Uhr am längsten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Hochpunkt von f (stärkste Zunahme) mit dem längsten Stau verwechseln",
    bemerkung="Standardbezug: K1 I, K3 II. AB amtlich: II. Amtlich.")

row("2023MerhoehtBAnalysisWTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen", typ_neben="",
    stichwoerter="s'(x) = f(x)|s(0) = 0|s(4) = 0 ⇒ Stau um 10:00 Uhr aufgelöst",
    voraussetzungen="Bestand als Stammfunktion der Rate mit Anfangswert|Ableiten eines Produkts|Funktionswert",
    format="Begründung|Rechnung", operator="Begründen Sie|Bestätigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Verkehr/Stau", textumfang="mittel",
    gegeben="s(x) = (x/4)² · (4 − x)³ = −1/16x⁵ + 3/4x⁴ − 3x³ + 4x²; Aussage: die Staulänge kann für jeden Zeitpunkt von 06:00 bis 10:00 Uhr durch s angegeben werden",
    gesucht="Begründung der Aussage; rechnerische Bestätigung, dass sich der Stau um 10:00 Uhr aufgelöst hat",
    verfahren="s' mit f vergleichen und s(0) = 0 prüfen; s(4) berechnen",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="km", abhaengig_von="",
    ergebnis="Es gilt s'(x) = f(x) und s(0) = 0; s(4) = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur s' = f zeigen, Anfangswert s(0) = 0 vergessen",
    bemerkung="Standardbezug: K1 II, K2 I, K3 II, K4 I, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAnalysisWTR1", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zunahme eines Bestands als Differenz der Bestandsfunktion und mittlere Änderungsrate im Zeitraum berechnen", typ_neben="",
    stichwoerter="s(2) − s(0,5) ≈ 1,3 km|1,3 km / 1,5 h ≈ 0,9 km/h",
    voraussetzungen="Zeiten in x umrechnen|Bestandsdifferenz|Differenzenquotient",
    format="Rechnung", operator="Berechnen Sie|Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Verkehr/Stau", textumfang="kurz",
    gegeben="s wie in e; Zeitraum 06:30 bis 08:00 Uhr",
    gesucht="Zunahme der Staulänge; durchschnittliche Änderungsrate im Zeitraum",
    verfahren="Differenz der Bestandswerte, geteilt durch die Zeitspanne 1,5 h",
    schritte="2", zahlenraum="dezimal", einheiten="km|km/h", abhaengig_von="2023MerhoehtBAnalysisWTR1-1e",
    ergebnis="s(2) − s(0,5) ≈ 1,3, die Länge hat um etwa 1,3 km zugenommen; durchschnittliche Änderungsrate etwa 1,3 km / 1,5 h ≈ 0,9 km/h (amtlich)",
    zwischenergebnis="s(2) − s(0,5) = 1,330", niveau_geschaetzt="II",
    fehlerquelle="Integral über f zwischen 0,5 und 2 zwar richtig, aber mit falschen Grenzen (Uhrzeiten statt Stunden)",
    bemerkung="Standardbezug: K2 I, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAnalysisWTR1", "g", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zeitpunkt gleichen Bestands am Ratengraphen über gleich große Flächen markieren und begründen", typ_neben="",
    stichwoerter="Nullstelle a des Graphen bei etwa 2,3|Fläche über der x-Achse von 1,5 bis a gleich Fläche unter der x-Achse von a bis b|b etwa 3,3 markieren",
    voraussetzungen="Bestandsänderung als Integral der Rate|gleiche Bestandswerte heißt Flächenbilanz null",
    format="Zeichnen|Begründung", operator="Markieren Sie|Begründen Sie|Veranschaulichen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze="Abbildung 2: Kästchenraster, x von 0 bis 4, y von −1 bis 2; Ratengraph für einen anderen Tag: von (0 | 0) steil zu einem Hochpunkt etwa (0,8 | 1,8), fallend durch die Nullstelle bei etwa 2,3, Tiefpunkt etwa (3,2 | −1,1), zurück auf null bei 4; Erwartungshorizont: Flächen zwischen 1,5 und a (über der Achse) und zwischen a und b (unter der Achse) schraffiert, b bei etwa 3,3 markiert", kontext="Verkehr/Stau", textumfang="lang",
    gegeben="Graph der Änderungsrate der Staulänge für einen anderen Tag (Abbildung 2), x Stunden nach 06:00 Uhr; um 07:30 Uhr hat der Stau eine bestimmte Länge, zu einem anderen Zeitpunkt dieselbe",
    gesucht="diesen Zeitpunkt markieren, begründen, Begründung in der Abbildung veranschaulichen",
    verfahren="Zeitpunkt b so wählen, dass die Flächen zwischen Graph und x-Achse von 1,5 bis zur Nullstelle a und von a bis b gleich groß sind",
    schritte="2", zahlenraum="dezimal", einheiten="h", abhaengig_von="",
    ergebnis="Der gesuchte Zeitpunkt b liegt so, dass die Inhalte der Flächen, die der Graph mit der x-Achse für 1,5 ≤ x ≤ a und a ≤ x ≤ b einschließt, übereinstimmen (a Nullstelle des Graphen); Markierung bei etwa b = 3,3 mit beiden Flächen schraffiert (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Zeitpunkt mit gleichem Ratenwert statt gleicher Staulänge markieren",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich. Abweichung: meine Schätzung III (Flächenbilanz als Bestandsgleichheit deuten und in die Zeichnung übertragen), amtlich II.")

# ---- Analysis WTR 1, Aufgabe 2: Schar h_k(x) = (x − 3)^k + 1, k ∈ IN \ {0}
HK = "Abbildung 3 (k = 4) und Abbildung 4 (k = 5): Koordinatensysteme mit Skalierung 5 auf beiden Achsen; Graph von h_k (Parabel vierter Ordnung mit Tiefpunkt (3 | 1) bzw. Kurve fünften Grades mit Terrassenpunkt (3 | 1)) und Graph von h_k' (kubisch bzw. quartisch); Punkte P(4 | h_k(4)), Q(4 | h_k'(4)), R(2 | h_k(2)), S(2 | h_k'(2)) markiert"
row("2023MerhoehtBAnalysisWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Grenzverhalten einer Potenzschar nach der Parität des Exponenten begründen", typ_neben="",
    stichwoerter="Polynom mit Leitterm x^k|k ungerade: h_k → −∞|k gerade: h_k → +∞",
    voraussetzungen="Grenzverhalten ganzrationaler Funktionen über den Leitterm|Fallunterscheidung gerade/ungerade",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="h_k(x) = (x − 3)^k + 1 in IR, k ∈ IN ohne 0",
    gesucht="Verhalten für x → −∞ in Abhängigkeit von k mit Begründung",
    verfahren="Leitterm x^k betrachten, Vorzeichen nach der Parität von k",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Für alle k ist der Term ein Polynom mit x^k als Summand mit dem größten Exponenten; damit gilt lim h_k(x) = −∞ für x → −∞ bei ungeradem k und +∞ bei geradem k (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Verschiebung um 3 als maßgeblich ansehen",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAnalysisWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gemeinsame Punkte aller Graphen einer Schar bestimmen", typ_neben="",
    stichwoerter="(x − 3)^k unabhängig von k für x − 3 = 0 und x − 3 = 1|(3 | 1) und (4 | 2)",
    voraussetzungen="Potenzen von 0 und 1|Punkte aus den Stellen berechnen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="h_k wie in a; alle Graphen haben zwei Punkte gemeinsam",
    gesucht="Koordinaten der beiden gemeinsamen Punkte",
    verfahren="Stellen finden, an denen (x − 3)^k nicht von k abhängt",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Für x − 3 = 0 und x − 3 = 1 hat h_k(x) für alle k denselben Wert; (3 | 1), (4 | 2) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur (3 | 1) finden",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2023MerhoehtBAnalysisWTR1", "c", innen="2", seite="2", punkte="6", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Aussage über den Ableitungsgraphen einer Schar als Tangente an den Scharfgraphen beurteilen", typ_neben="",
    stichwoerter="Graph von h_k' nur für k = 1 und k = 2 eine Gerade|k = 1: h₁' = 1 konstant, keine Tangente an h₁(x) = x − 2|k = 2: h₂'(x) = 2x − 6, Steigung 2 bei x = 4, h₂(4) = 2 = h₂'(4)|Aussage richtig",
    voraussetzungen="Tangente ist eine Gerade|Ableitung einer Potenzfunktion|Berührbedingung gleicher Wert und gleiche Steigung",
    format="Begründung|Rechnung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Aussage: es gibt genau einen Wert von k, für den der Graph von h_k' Tangente an den Graphen von h_k ist",
    gesucht="Beurteilung der Aussage",
    verfahren="Nur k = 1 und k = 2 liefern Geraden als Ableitungsgraphen; k = 1 ausschließen (parallele Gerade), für k = 2 Berührpunkt bei x = 4 nachweisen",
    schritte="4", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Nur für k = 1 und k = 2 ist der Graph von h_k' eine Gerade, für k = 1 aber keine Tangente an den Graphen von h_k; es gilt h₂'(x) = 2x − 6, h₂'(x) = 2 ⇔ x = 4 und h₂(4) = 2, damit ist die Aussage richtig (amtlich)",
    zwischenergebnis="h₁(x) = x − 2, h₁'(x) = 1", niveau_geschaetzt="III",
    fehlerquelle="k ≥ 3 nicht ausschließen (Ableitungsgraph ist keine Gerade)",
    bemerkung="Standardbezug: K1 III, K2 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis über alle k mit Fallunterscheidung.")

row("2023MerhoehtBAnalysisWTR1", "d", innen="2", seite="3", punkte="7", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Trapez aus Funktions- und Ableitungswerten einer Schar begründen und Flächengleichheit für k und k + 1 nachweisen", typ_neben="",
    stichwoerter="P, Q gleiche x-Koordinate 4, R, S gleiche x-Koordinate 2 ⇒ PQ parallel RS|Trapezfläche (|h_k'(4) − h_k(4)| + |h_k'(2) − h_k(2)|)/2 · 2 = k − 2 + |k(−1)^(k−1) − (−1)^k − 1||gerades k: k − 2 + |−k − 1 − 1| = 2k|k + 1: k + 1 − 2 + |(k + 1) + 1 − 1| = 2k",
    voraussetzungen="Parallelität über gleiche x-Koordinaten|Trapezformel|Werte von h_k und h_k' an 2 und 4 mit Vorzeichen (−1)^k|Betrag",
    format="Begründung|Rechnung", operator="Begründen Sie|Zeigen Sie", antwort="Term",
    material="Koordinatensystem", skizze=HK, kontext="ohne", textumfang="lang",
    gegeben="Für k ≥ 4: P(4 | h_k(4)), Q(4 | h_k'(4)), R(2 | h_k(2)), S(2 | h_k'(2)) bilden ein Viereck; Abbildungen 3 (k = 4) und 4 (k = 5); Aussage: für jedes gerade k ≥ 4 stimmen die Trapezflächen für k und k + 1 überein",
    gesucht="Begründung, dass jedes Viereck ein Trapez ist; Nachweis der Aussage",
    verfahren="Parallelität von PQ und RS über die x-Koordinaten; Trapezfläche allgemein in k mit (−1)^k aufstellen und für gerades k sowie k + 1 auswerten",
    schritte="5", zahlenraum="ganz|Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="P und Q sowie R und S haben übereinstimmende x-Koordinaten, damit sind PQ und RS parallel; Flächeninhalt (|h_k'(4) − h_k(4)| + |h_k'(2) − h_k(2)|)/2 · 2 = k − 2 + |k · (−1)^(k−1) − (−1)^k − 1|; für gerades k ergibt sich k − 2 + |−k − 1 − 1| = 2k, für k + 1 ergibt sich k + 1 − 2 + |(k + 1) + 1 − 1| = 2k (amtlich)",
    zwischenergebnis="h_k(4) = 2, h_k'(4) = k, h_k(2) = (−1)^k + 1, h_k'(2) = k(−1)^(k−1); k = 4 und 5: 8, k = 6 und 7: 12", niveau_geschaetzt="III",
    fehlerquelle="Betrag bei h_k'(2) − h_k(2) vergessen, Vorzeichen von (−1)^k",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (k = 4 bis 7). Eichregel: (c) allgemeiner Nachweis mit hergeleiteter Beziehung in k.")

# ---- Analysis WTR 2: Hängebrücke, r(x) = 253/100 · (e^((32 − x)/11) − 1), s(x) = (1/8)⁶(x⁴ + 2560x²) + 125/256
BR = "Abbildung 1: schematische Seitenansicht einer achsensymmetrischen Hängebrücke; horizontale Fahrbahn als x-Achse, y-Achse in der Mitte; zwei Pfeiler bei x = ±20, Tragseil dazwischen durchhängend, Abspannseile von den Pfeilerspitzen zu den Fahrbahnenden bei x = ±32, senkrechte Halteseile; Wasseroberfläche 20 m unter der Fahrbahn; Beschriftungen Fahrbahn, Pfeiler, Tragseil, Halteseil, Abspannseil, linker/mittlerer/rechter Abschnitt; 1 LE = 10 m"
row("2023MerhoehtBAnalysisWTR2", "a", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Gesamtlänge aus einer Nullstelle und der Achsensymmetrie im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="r(x) = 0 ⇔ (32 − x)/11 = 0 ⇔ x = 32|Fahrbahnende bei x = 32|2 · 32 · 10 m = 640 m",
    voraussetzungen="Exponentialgleichung e^t = 1|Symmetrie zur y-Achse|Maßstab 1 LE = 10 m",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="lang",
    gegeben="r(x) = 253/100 · (e^((32 − x)/11) − 1) beschreibt das rechte Abspannseil; Pfeilerabstand 400 m; 1 LE = 10 m; Brücke achsensymmetrisch zur y-Achse",
    gesucht="Nachweis, dass die Fahrbahn 640 m lang ist",
    verfahren="Nullstelle von r als Fahrbahnende, verdoppeln und umrechnen",
    schritte="2", zahlenraum="ganz", einheiten="m", abhaengig_von="",
    ergebnis="r(x) = 0 ⇔ 1/11 · (32 − x) = 0 ⇔ x = 32; 2 · 32 · 10 m = 640 m (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Maßstab vergessen (64 m) oder nur eine Hälfte",
    bemerkung="Standardbezug: K2 II, K3 I, K4 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAnalysisWTR2", "b", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Term und Intervall des an der y-Achse gespiegelten Graphen angeben", typ_neben="",
    stichwoerter="ℓ(x) = r(−x)|Intervall [−32; −20]",
    voraussetzungen="Spiegelung an der y-Achse als x → −x|Symmetrie der Brücke",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="kurz",
    gegeben="r wie in a für das rechte Abspannseil; linkes Abspannseil spiegelbildlich",
    gesucht="Term ℓ(x) für das linke Abspannseil und sein Intervall",
    verfahren="Spiegelung an der y-Achse, Intervall aus Pfeiler und Fahrbahnende",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2023MerhoehtBAnalysisWTR2-1a",
    ergebnis="ℓ(x) = r(−x), [−32; −20] (amtlich)",
    zwischenergebnis="ℓ(x) = 253/100 · (e^((32 + x)/11) − 1)", niveau_geschaetzt="I",
    fehlerquelle="Intervall [−32; 32] oder Spiegelung an der x-Achse",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K6 I. AB amtlich: I. Amtlich.")

row("2023MerhoehtBAnalysisWTR2", "c", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="r(20) ≈ 5|r(20) · 10 m + 20 m ≈ 70 m",
    voraussetzungen="Funktionswert|Maßstab|Höhe der Fahrbahn über dem Wasser addieren",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="kurz",
    gegeben="r wie in a; Pfeiler bei x = 20; Wasseroberfläche 20 m unter der Fahrbahn",
    gesucht="Höhe der Pfeiler über der Wasseroberfläche",
    verfahren="r(20) umrechnen und 20 m addieren",
    schritte="2", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="r(20) · 10 m + 20 m ≈ 70 m (amtlich)",
    zwischenergebnis="r(20) ≈ 5,00", niveau_geschaetzt="I",
    fehlerquelle="20 m Wassertiefe vergessen",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B), hier mit Maßstab und Sockelhöhe.")

row("2023MerhoehtBAnalysisWTR2", "d", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Winkel zwischen Graph und senkrechter Kante über die Ableitung berechnen", typ_neben="",
    stichwoerter="r'(x) = −23/100 · e^((32 − x)/11)|tan α = r'(20)|Winkel zum Pfeiler 90° + α ≈ 56°",
    voraussetzungen="Kettenregel für e-Funktion|Steigungswinkel über den Tangens|Winkel zur Senkrechten aus dem Steigungswinkel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="kurz",
    gegeben="r wie in a; rechter Pfeiler senkrecht bei x = 20",
    gesucht="Winkel, unter dem das Abspannseil auf den Pfeiler trifft",
    verfahren="Ableitung an der Stelle 20, Steigungswinkel, Ergänzung zum Winkel gegen die Senkrechte",
    schritte="3", zahlenraum="dezimal|negativ|Potenz", einheiten="°", abhaengig_von="",
    ergebnis="r'(x) = −23/100 · e^((32 − x)/11); tan α = r'(20) liefert für die gesuchte Winkelgröße 90° + α ≈ 56° (amtlich)",
    zwischenergebnis="r'(20) ≈ −0,685, α ≈ −34,4°", niveau_geschaetzt="II",
    fehlerquelle="Steigungswinkel 34° gegen die Fahrbahn statt gegen den Pfeiler",
    bemerkung="Standardbezug: K2 II, K3 I, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")

row("2023MerhoehtBAnalysisWTR2", "e", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Flächeninhalt zwischen Graph, x-Achse und senkrechter Gerade im Sachzusammenhang mit Maßstab berechnen", typ_neben="",
    stichwoerter="∫₂₀³² r(x) dx = 253/100 · [−11e^((32 − x)/11) − x]₂₀³² ≈ 25|Maßstab 10 m je LE, also 100 m² je FE|etwa 2500 m²",
    voraussetzungen="Stammfunktion von e^(c − x/11)|Grenzen aus Pfeiler und Fahrbahnende|quadratischer Maßstab",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="kurz",
    gegeben="Flächenstück zwischen rechtem Pfeiler (x = 20), Abspannseil r und Fahrbahn (x-Achse) bis x = 32",
    gesucht="Inhalt in der Realität",
    verfahren="Integral von 20 bis 32 über r, mit 100 m² je Flächeneinheit umrechnen",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="m²", abhaengig_von="2023MerhoehtBAnalysisWTR2-1a",
    ergebnis="∫₂₀³² r(x) dx = 253/100 · [−11 · e^((32 − x)/11) − x]₂₀³² ≈ 25; der Flächeninhalt beträgt etwa 2500 m² (amtlich)",
    zwischenergebnis="Integral ≈ 24,66, Fläche ≈ 2466 m²", niveau_geschaetzt="II",
    fehlerquelle="Maßstab linear (Faktor 10) statt quadratisch anwenden",
    bemerkung="Standardbezug: K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAnalysisWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Symmetrieart am Term über die Exponenten begründen", typ_neben="",
    stichwoerter="s(x) = (1/8)⁶(x⁴ + 2560x²) + 125/256|nur gerade Exponenten ⇒ achsensymmetrisch zur y-Achse",
    voraussetzungen="Symmetriekriterium ganzrationaler Funktionen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="mittel",
    gegeben="Tragseil im mittleren Abschnitt: s(x) = (1/8)⁶ · (x⁴ + 2560x²) + 125/256; Halteseile senkrecht mit Abstand 16 m",
    gesucht="Begründung, dass der Term zur Achsensymmetrie der Seitenansicht passt",
    verfahren="Exponenten betrachten",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Der Funktionsterm ist ganzrational und enthält Potenzen von x ausschließlich mit geradzahligen Exponenten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Konstante 125/256 als Störung der Symmetrie ansehen",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A).")

row("2023MerhoehtBAnalysisWTR2", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Gleichung für zwei Graphenpunkte mit festem horizontalem Abstand und Höhenunterschied aufstellen", typ_neben="",
    stichwoerter="40 m = 4 LE, 5 m = 0,5 LE|höherer Punkt weiter außen (x größer)|s(x) − s(x − 4) = 0,5",
    voraussetzungen="Maßstab|monotones Steigen des Tragseils rechts der Mitte|Differenz von Funktionswerten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="mittel",
    gegeben="zwei Punkte des Tragseils in der rechten Hälfte mit horizontalem Abstand 40 m und Höhenunterschied 5 m",
    gesucht="Gleichung, deren Lösung die x-Koordinate des höheren Punkts ist",
    verfahren="Maße in LE umrechnen, Differenz s(x) − s(x − 4) gleich 0,5 setzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="s(x) − s(x − 4) = 0,5 (amtlich)",
    zwischenergebnis="Lösung x ≈ 8,19", niveau_geschaetzt="II",
    fehlerquelle="Abstände in Metern in den Term schreiben (s(x) − s(x − 40) = 5)",
    bemerkung="Standardbezug: K1 I, K3 II, K4 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Lösung existiert).")

row("2023MerhoehtBAnalysisWTR2", "c", innen="2", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Summe von Funktionswerten mit Maßstab als Gesamtlänge im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Stellen −20 + 1,6k für k = 1 bis 24: die 24 Halteseile im Abstand 16 m = 1,6 LE|s(−20 + 1,6k) Länge eines Halteseils im Modell|Faktor 10 Maßstab|Gesamtlänge der Halteseile",
    voraussetzungen="Funktionswert als Höhe des Tragseils über der Fahrbahn|Summenzeichen|Maßstab",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="mittel",
    gegeben="Term (Σ_{k=1}^{24} s(−20 + 1,6 · k)) · 10; Halteseile mit Abstand 16 m von den Pfeilern und untereinander",
    gesucht="Bedeutung des Terms mit Begründung",
    verfahren="Stellen als Positionen der 24 Halteseile erkennen, Funktionswerte als Seillängen, Faktor 10 als Maßstab",
    schritte="2", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="Mit dem Term kann die Gesamtlänge der Halteseile im mittleren Brückenabschnitt berechnet werden; s(−20 + 1,6 · k) gibt für jedes der 24 Halteseile die Länge im Modell an, der Faktor 10 berücksichtigt den Maßstab (amtlich)",
    zwischenergebnis="Wert ≈ 429 m", niveau_geschaetzt="III",
    fehlerquelle="Pfeiler als Halteseile mitzählen (Stellen ±20 fehlen im Term)",
    bemerkung="Standardbezug: K1 III, K3 II, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Laufindex als Seilposition und Funktionswert als Seillänge deuten, verkettet mit dem Maßstab.")

row("2023MerhoehtBAnalysisWTR2", "d", innen="2", seite="2", punkte="6", afb_amtlich="III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Abstand eines Punktes von einem Graphen über die Normalenbedingung deuten", typ_neben="",
    stichwoerter="(s(x) − 0)/(x − 20) Steigung der Verbindung von (20 | 0) zu (x | s(x))|Produkt mit s'(x) gleich −1 ⇒ Verbindung senkrecht zur Tangente|Abstand des Pfeilerfußpunkts (20 | 0) zum Tragseil",
    voraussetzungen="Steigung einer Verbindungsstrecke|Orthogonalität über m₁ · m₂ = −1|kürzeste Verbindung senkrecht zur Tangente",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Skizze", skizze=BR, kontext="Hängebrücke/Bauwesen", textumfang="mittel",
    gegeben="Gleichung (s(x) − 0)/(x − 20) · s'(x) = −1",
    gesucht="welcher Abstand sich aus der Lösung berechnen lässt, mit Begründung",
    verfahren="Quotient als Steigung der Verbindung zu (20 | 0) deuten, Produkt −1 als Orthogonalität zur Tangente, damit Lotfußpunkt",
    schritte="2", zahlenraum="ganz", einheiten="m", abhaengig_von="",
    ergebnis="Die Lösung ermöglicht die Berechnung des Abstands desjenigen Punkts des rechten Pfeilers zum Tragseil, der auf der Höhe der Fahrbahn liegt; sie ist die x-Koordinate desjenigen Punkts P des Graphen von s, dessen Verbindungsstrecke zum Punkt (20 | 0) senkrecht zur Tangente in P steht (amtlich)",
    zwischenergebnis="x_P ≈ 18,16, Abstand ≈ 45 m", niveau_geschaetzt="III",
    fehlerquelle="Abstand als s(20) (senkrecht nach oben) deuten",
    bemerkung="Standardbezug: K1 III, K2 II, K3 III, K4 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Steigung und Orthogonalität deuten, verkettet mit dem Abstandsbegriff. Typ wiederverwendet (Teil A).")

row("2023MerhoehtBAnalysisWTR2", "e", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Länge eines Kreisbogens durch drei Punkte über den Winkel am Mittelpunkt berechnen", typ_neben="",
    stichwoerter="Radius 1699/36 − 1/2|tan(β/2) = 20/(1699/36 − 5)|Bogenlänge β/360° · 2π · r ≈ 41,3|Tragseil etwa 413 m",
    voraussetzungen="Radius aus Mittelpunkt und Punkt|halber Mittelpunktswinkel im rechtwinkligen Dreieck|Bogenlängenformel|Maßstab",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze="Abbildung 2: Koordinatensystem mit Punkten A(−20 | 5), B(20 | 5), C(0 | 1/2) auf einem flachen Kreisbogen und Mittelpunkt M(0 | 1699/36) hoch auf der y-Achse; Erwartungshorizont: Radien MA, MB, MC und Winkel β/2 zwischen MC und MB eingezeichnet", kontext="Hängebrücke/Bauwesen", textumfang="mittel",
    gegeben="Kreis mit Mittelpunkt M(0 | 1699/36) durch A(−20 | 5), B(20 | 5), C(0 | 1/2) als Näherung des Tragseils",
    gesucht="Länge des Tragseils über den Kreisbogen",
    verfahren="Halben Mittelpunktswinkel über den Tangens im Dreieck M, (0 | 5), B, Bogenlänge über Winkel und Radius, Maßstab",
    schritte="4", zahlenraum="Bruch|dezimal", einheiten="m", abhaengig_von="",
    ergebnis="Mit tan(β/2) = 20/(1699/36 − 5) ergibt sich für die Länge des Kreisbogens β/360° · 2π · (1699/36 − 1/2) ≈ 41,3; das Tragseil ist etwa 413 m lang (amtlich)",
    zwischenergebnis="r ≈ 46,69, β ≈ 50,7°", niveau_geschaetzt="II",
    fehlerquelle="Radius als 1699/36 statt 1699/36 − 1/2",
    bemerkung="Standardbezug: K2 II, K3 I, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Thema ersatzweise Skalarprodukt und Winkel (Kreisbogen und Mittelpunktswinkel haben keine Themenzeile).")

# ---- AG/LA A1 WTR: Verflechtung Rohstoffe R1–R3, Zwischenprodukte Z1, Z2, Endprodukte E1–E3; Dreieck OPQ
VD = "Abbildung 1: Verflechtungsdiagramm R₁, R₂, R₃ links, Z₁, Z₂ in der Mitte, E₁, E₂, E₃ rechts; Pfeile R₁→Z₁ s, R₂→Z₂ 0,8, R₃→Z₁ 0,04, R₃→Z₂ 0,04, Z₁→E₁ 1, Z₁→E₂ 0,4, Z₂→E₂ 0,7, Z₂→E₃ 1,2"
row("2023MerhoehtBAGLAA1WTR", "a", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Fehlenden Eintrag des Diagramms aus der Bedarfsmatrix angeben und deuten", typ_neben="",
    stichwoerter="s = a₁₁ = 0,5|ME von R₁ je ME von Z₁",
    voraussetzungen="Matrix zeilenweise als Rohstoff, spaltenweise als Produkt lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Diagramm", skizze=VD, kontext="Produktion/Verflechtung", textumfang="lang",
    gegeben="A = ((0,5; 0), (0; 0,8), (0,04; 0,04)) Rohstoffe je Zwischenprodukt, B = ((1; 0,4; 0), (0; 0,7; 1,2)) Zwischenprodukte je Endprodukt, C = ((0,5; 0,2; 0), (0; 0,56; 0,96), (0,04; 0,044; 0,048)) Rohstoffe je Endprodukt; Pfeil R₁ → Z₁ mit s",
    gesucht="Wert und Bedeutung von s",
    verfahren="Eintrag der Matrix A ablesen",
    schritte="1", zahlenraum="dezimal", einheiten="ME", abhaengig_von="",
    ergebnis="s = 0,5; der Wert gibt an, wie viele Mengeneinheiten von R₁ zur Herstellung einer Mengeneinheit von Z₁ benötigt werden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Eintrag aus C statt A lesen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (C = A · B). Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MerhoehtBAGLAA1WTR", "b", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Rohstoffmenge aus den übrigen Rohstoffen über die Gesamtmatrix bestimmen", typ_neben="",
    stichwoerter="C · (e₁; 10; 25) = (6; r₂; r₃)|0,5e₁ + 2 = 6 ⇒ e₁ = 8|r₃ = 0,04 · 8 + 0,44 + 1,2 = 1,96",
    voraussetzungen="Matrix-Vektor-Produkt|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=VD, kontext="Produktion/Verflechtung", textumfang="mittel",
    gegeben="Produktion: e₁ ME von E₁, 10 ME von E₂, 25 ME von E₃; Verbrauch 6 ME von R₁",
    gesucht="benötigte Mengeneinheiten von R₃",
    verfahren="Erste Zeile von C liefert e₁, dritte Zeile den Bedarf an R₃",
    schritte="3", zahlenraum="dezimal", einheiten="ME", abhaengig_von="",
    ergebnis="C · (e₁; 10; 25) = (6; r₂; r₃) liefert 0,5e₁ + 2 = 6 und 0,04e₁ + 0,44 + 1,2 = r₃; daraus e₁ = 8 und r₃ = 1,96 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="e₁ als 6 einsetzen",
    bemerkung="Standardbezug: K2 I, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A). Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MerhoehtBAGLAA1WTR", "c", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Nichtinvertierbarkeit der Gesamtmatrix im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="C nicht invertierbar|nicht jeder Rohstoffvektor hat einen Produktionsvektor|Rohstoffe bleiben übrig",
    voraussetzungen="Inverse Matrix als Rückrechnung von Rohstoffen auf Produkte",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Produktion/Verflechtung", textumfang="kurz",
    gegeben="C ist nicht invertierbar",
    gesucht="eine Bedeutung im Sachzusammenhang",
    verfahren="Fehlende Inverse als fehlende eindeutige Rückrechnung deuten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Nicht aus jeder vorgegebenen Menge an Rohstoffen lassen sich Endprodukte so herstellen, dass keine Rohstoffe übrig bleiben (amtlich)",
    zwischenergebnis="det C = 0", niveau_geschaetzt="II",
    fehlerquelle="Aussage über die Hinrichtung (Bedarf berechnen) statt über die Rückrechnung",
    bemerkung="Standardbezug: K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (det C = 0). Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MerhoehtBAGLAA1WTR", "d", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Bedarf eines neuen Endprodukts an Zwischenprodukten aus der Produktgleichung der Matrizen ermitteln", typ_neben="",
    stichwoerter="B* mit vierter Spalte (x; y)|C* = A · B*|dritte Zeile: 0,06 = 0,04(x + y) ⇒ x + y = 1,5",
    voraussetzungen="Gesamtmatrix als Produkt|Matrixprodukt spaltenweise|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Verflechtung", textumfang="mittel",
    gegeben="C* = C mit vierter Spalte (u; v; 0,06) für das neue Endprodukt E₄ aus den beiden Zwischenprodukten",
    gesucht="Summe der Mengeneinheiten der Zwischenprodukte je ME von E₄",
    verfahren="B* mit Spalte (x; y) ansetzen, C* = A · B*, dritte Zeile auswerten",
    schritte="3", zahlenraum="dezimal", einheiten="ME", abhaengig_von="",
    ergebnis="Aus C* = A · B* mit B* = ((1; 0,4; 0; x), (0; 0,7; 1,2; y)) ergibt sich 0,06 = 0,04 · (x + y) ⇔ x + y = 1,5, d. h. insgesamt 1,5 Mengeneinheiten der Zwischenprodukte (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="u und v für nötig halten, obwohl die dritte Zeile genügt",
    bemerkung="Standardbezug: K1 II, K2 III, K3 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Produktstruktur C = A · B auf die neue Spalte übertragen und die Summe aus einer Zeile gewinnen. Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MerhoehtBAGLAA1WTR", "e", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Rohstoffbedarf in Abhängigkeit von einem Matrixparameter als Gerade darstellen und erläutern", typ_neben="",
    stichwoerter="R₂ nur für Z₂, 0,8 je ME|B_t · (10; 15; 25) liefert Z₂: 46,5 − 15t|R₂: 37,2 − 12t|Gerade von (0 | 37,2) nach (1,1 | 24)",
    voraussetzungen="Matrix mit Parameter mal Vektor|Rohstoffweg über das Diagramm|lineare Funktion zeichnen",
    format="Zeichnen|Begründung", operator="Stellen Sie dar|Erläutern Sie", antwort="Grafik",
    material="Koordinatensystem", skizze="Abbildung 2: Koordinatensystem t von 0 bis 1 (Raster 0,1), Bedarf von 0 bis 40 (Raster 10); Erwartungshorizont: fallende Strecke von (0 | 37,2) bis (1,1 | 24)", kontext="Produktion/Verflechtung", textumfang="lang",
    gegeben="B_t = ((1; t; 0), (0; 1,1 − t; 1,2)), t ∈ [0; 1,1]; Produktion 10 ME E₁, 15 ME E₂, 25 ME E₃",
    gesucht="Bedarf an R₂ in Abhängigkeit von t grafisch; Erläuterung",
    verfahren="Zwischenproduktbedarf mit B_t berechnen, R₂ nur über Z₂ mit Faktor 0,8, linearen Term zeichnen",
    schritte="3", zahlenraum="dezimal", einheiten="ME", abhaengig_von="",
    ergebnis="R₂ ist nur für Z₂ erforderlich, 0,8 ME je ME Z₂; B_t · (10; 15; 25) liefert 46,5 − 15t für Z₂, damit 37,2 − 12t für R₂; Gerade in Abbildung 2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Bedarf über C statt über A · B_t berechnen (C gilt nur für t = 0,4)",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K4 I, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Parameterabhängigen Bedarf über zwei Stufen herleiten, verkettet mit der grafischen Darstellung. Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MerhoehtBAGLAA1WTR", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Innenwinkel eines Dreiecks über gleiche Seitenlängen als gleichseitig bestimmen", typ_neben="",
    stichwoerter="|OP| = |PQ| = |OQ| = √24|gleichseitig ⇒ alle Winkel 60°",
    voraussetzungen="Beträge von Verbindungsvektoren|Winkel im gleichseitigen Dreieck",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Dreieck O(0|0|0), P(−2|4|−2), Q(−4|2|2); Innenwinkel bei Q 60°",
    gesucht="die beiden anderen Innenwinkel",
    verfahren="Seitenlängen berechnen, Gleichseitigkeit erkennen",
    schritte="2", zahlenraum="Wurzel", einheiten="°", abhaengig_von="",
    ergebnis="Wegen OP = (−2; 4; −2), PQ = (−2; −2; 4), OQ = (−4; 2; 2) gilt |OP| = |PQ| = |OQ|; damit sind auch die beiden anderen Innenwinkel 60° groß (amtlich)",
    zwischenergebnis="alle Seiten √24", niveau_geschaetzt="II",
    fehlerquelle="beide Winkel einzeln über das Skalarprodukt rechnen und Rundungsfehler",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Gleichseitigkeit als Abkürzung erkennen), amtlich I. Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MerhoehtBAGLAA1WTR", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Eckpunkt eines flächen- und umfangsgleichen Dreiecks über eine Parallelverschiebung angeben", typ_neben="",
    stichwoerter="OT = PQ|T(−2 | −2 | 4)|Parallelogramm OPQT: Dreieck OTQ kongruent zu OPQ",
    voraussetzungen="Kongruente Dreiecke durch Verschieben|Vektoraddition",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Dreieck OPQ wie in a; Dreieck OTQ mit gleichem Flächeninhalt und Umfang",
    gesucht="Koordinaten von T",
    verfahren="T so wählen, dass OPQT ein Parallelogramm ist (OT = PQ)",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Mit OT = PQ ergibt sich T(−2 | −2 | 4) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="T = P + Q (Spiegelung an OQ) ergibt zwar gleiche Fläche, aber nur bei gleichseitigem Dreieck gleichen Umfang",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2023MerhoehtBAGLAA1WTR", "c", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächengleichheit zweier Dreiecke mit gemeinsamer Seite über gleiche Höhen an einer Skizze begründen", typ_neben="",
    stichwoerter="K = P + 2 · PQ, Q Mittelpunkt von PK|gemeinsame Seite OQ|Höhen von P und K auf OQ gleich lang",
    voraussetzungen="Vektorgleichung als Lage von K auf der Geraden PQ|Fläche = 1/2 Grundseite mal Höhe|Skizze",
    format="Zeichnen|Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine; Erwartungshorizont: Skizze mit O, P, Q, K, Q als Mittelpunkt von PK, Höhen von P und K auf die Gerade OQ mit rechten Winkeln", kontext="ohne", textumfang="kurz",
    gegeben="OK = OP + 2 · PQ",
    gesucht="Begründung ohne Rechnung anhand einer Skizze, dass die Dreiecke OPQ und OQK flächengleich sind",
    verfahren="Q als Mittelpunkt von PK erkennen, gemeinsame Seite OQ, gleiche Höhen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Dreiecke OPQ und OQK haben die Seite OQ gemeinsam; die Längen der Höhen bezüglich der Eckpunkte P bzw. K stimmen überein (amtlich)",
    zwischenergebnis="K(−6 | 0 | 6)", niveau_geschaetzt="II",
    fehlerquelle="doch rechnen (Kreuzprodukt) statt Skizze und Höhenargument",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA A2 WTR 1: Werbemast mit drei Werbeflächen, Mauer, Fußball
WM = "Abbildung 1: Schrägbild eines senkrechten Masts auf der x₁x₂-Ebene (Ursprung Mastfuß), drei rechteckige Werbeflächen um den Mast, die graue Fläche ABED mit A(5|−2|11), B(5|5|11), D(5|−2|15), E(−2|5|15), dazu F(−2|−2|15); Abbildung 2: dieselbe Fläche mit Dreieck GBH (G auf AB, H auf BE), das vom Punkt K aus nicht sichtbar ist"
row("2023MerhoehtBAGLAA2WTR1", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines Rechtecks aus Kantenlängen berechnen und rechten Winkel zweier Flächen prüfen", typ_neben="",
    stichwoerter="D(5|−2|15), |DE| = √98 = 7√2|Höhe 4 ⇒ 28√2 ≈ 40 m²|FD · FE = (7; 0; 0) · (0; 7; 0) = 0",
    voraussetzungen="Eckpunkt aus Vertikalität ergänzen|Betrag|Skalarprodukt null",
    format="Rechnung", operator="Bestimmen Sie|Prüfen Sie", antwort="Zahl",
    material="Körper", skizze=WM, kontext="Werbemast/Gebäude", textumfang="lang",
    gegeben="Mast 15 m hoch, Durchmesser 80 cm, Mittelpunkt der Grundfläche im Ursprung; A(5|−2|11), E(−2|5|15), F(−2|−2|15) Ecken der Werbeflächen; seitliche Kanten vertikal; 1 LE = 1 m",
    gesucht="Flächeninhalt der grauen Werbefläche; ob die anderen beiden Flächen einen rechten Winkel einschließen",
    verfahren="D über A ergänzen, Rechteckseiten 4 und |DE|; Skalarprodukt der Oberkanten FD und FE",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="m²", abhaengig_von="",
    ergebnis="Mit D(5|−2|15) ergibt sich 4 · |DE| = 4 · √(7² · 2) = 28√2, der Flächeninhalt beträgt etwa 40 m²; FD · FE = (7; 0; 0) · (0; 7; 0) = 0, die beiden anderen Flächen schließen einen rechten Winkel ein (amtlich)",
    zwischenergebnis="28√2 ≈ 39,6", niveau_geschaetzt="I",
    fehlerquelle="Höhe der Fläche als 15 statt 15 − 11 = 4",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAGLAA2WTR1", "b", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Parameter einer Ebenengleichung aus einem enthaltenen Punkt bestimmen", typ_neben="",
    stichwoerter="a · x₁ + a · x₂ = b|A einsetzen: 5a − 2a = b ⇒ 3a = b|a = 1, b = 3",
    voraussetzungen="Punktprobe|Parameter frei wählen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=WM, kontext="Werbemast/Gebäude", textumfang="kurz",
    gegeben="Ebene der grauen Werbefläche in der Form a · x₁ + a · x₂ = b",
    gesucht="passende Werte für a und b",
    verfahren="A (oder E) einsetzen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Da A in der Ebene liegt, gilt 3a = b; damit a = 1, b = 3 (amtlich)",
    zwischenergebnis="E: −2a + 5a = 3a ✓", niveau_geschaetzt="II",
    fehlerquelle="a = b = 0 als Lösung",
    bemerkung="Standardbezug: K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2023MerhoehtBAGLAA2WTR1", "c", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Abstand einer vertikalen Fläche zu einer Achse über den Mittelpunkt der Oberkante begründen", typ_neben="",
    stichwoerter="x₃-Achse Symmetrieachse des Masts|D und E gleich weit von (0|0|15)|kein Punkt von DE näher an der Achse als der Mittelpunkt M|vertikale Kanten: gilt für das ganze Rechteck",
    voraussetzungen="Abstand zu einer Achse als Abstand in der Projektion|Lot vom Mittelpunkt bei gleichschenkligem Dreieck|Vertikalität",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=WM, kontext="Werbemast/Gebäude", textumfang="mittel",
    gegeben="graue Werbefläche ABED, Mast entlang der x₃-Achse mit Durchmesser 0,8 m",
    gesucht="Begründung, dass der Abstand der Fläche zum Mast gleich dem Abstand des Mittelpunkts der Oberkante DE zum Mast ist",
    verfahren="Mast auf die Achse zurückführen, Symmetrie von D und E zur Achse, Vertikalität der Fläche",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die x₃-Achse ist Symmetrieachse des Masts; D und E haben den gleichen Abstand zum Punkt (0|0|15), damit hat kein Punkt der Strecke DE einen kleineren Abstand zur x₃-Achse als ihr Mittelpunkt M; da die seitlichen Kanten vertikal verlaufen, gilt dies für alle Punkte des Vierecks ABED (amtlich)",
    zwischenergebnis="M(1,5 | 1,5 | 15), Abstand zur Achse √4,5 ≈ 2,12, abzüglich Radius 0,4", niveau_geschaetzt="III",
    fehlerquelle="Abstand des Punktes A oder D zur Achse als Flächenabstand",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung III (Symmetrie- und Vertikalitätsargument verketten), amtlich II.")

row("2023MerhoehtBAGLAA2WTR1", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Strecke gegen die Horizontale über ihre Projektion berechnen", typ_neben="",
    stichwoerter="KG = (−20; −16; 10)|Projektion (−20; −16; 0)|cos φ = 656/(√(20² + 16² + 10²) · √(20² + 16²))|φ ≈ 21°",
    voraussetzungen="Verbindungsvektor|Projektion in die Horizontale|Winkelformel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=WM, kontext="Werbemast/Gebäude", textumfang="mittel",
    gegeben="Sichtlinie von K(24|15|1) zu G(4|−1|11)",
    gesucht="Winkel der Sichtlinie gegenüber der Horizontalen",
    verfahren="Winkel zwischen KG und seiner Projektion in die x₁x₂-Ebene",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="cos φ = ((−20; −16; 10) · (−20; −16; 0)) / (|(−20; −16; 10)| · |(−20; −16; 0)|) = 656 / (√(20² + 16² + 10²) · √(20² + 16²)) liefert φ ≈ 21° (amtlich)",
    zwischenergebnis="alternativ sin φ = 10/√756", niveau_geschaetzt="II",
    fehlerquelle="Winkel zur Vertikalen (69°) angeben",
    bemerkung="Standardbezug: K3 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAGLAA2WTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Rechenweg für den Schnittpunkt einer Geraden mit einer Ebene durch drei Punkte beschreiben", typ_neben="",
    stichwoerter="H Schnittpunkt der Geraden BE mit der Ebene KPQ|OB + λ · BE = OK + μ · KP + σ · KQ|λ liefert H",
    voraussetzungen="Sichtgrenze als Ebene durch Auge und Mauerkante|Gerade und Ebene in Parameterform gleichsetzen",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Körper", skizze=WM, kontext="Werbemast/Gebäude", textumfang="lang",
    gegeben="Mauerkante PQ mit P(20|−5|3), Q(20|25|3); Auge K(24|15|1); nicht sichtbares Dreieck GBH mit H auf BE",
    gesucht="Beschreibung, wie H rechnerisch bestimmt werden könnte",
    verfahren="H als Schnittpunkt der Kantengeraden BE mit der Ebene durch K, P, Q; Gleichungssystem nach λ",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="H ist der Schnittpunkt der Geraden BE mit der Ebene, die K, P und Q enthält; die Gleichung OB + λ · BE = OK + μ · KP + σ · KQ liefert λ und damit OB + λ · BE als Ortsvektor von H (amtlich)",
    zwischenergebnis="H(1,2 | 5 | 13,4) nach eigener Rechnung", niveau_geschaetzt="III",
    fehlerquelle="Sichtgrenze als Gerade durch K und einen Mauerpunkt statt als Ebene ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III, K4 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (H berechnet). Eichregel: (a) Sichtschatten als Ebene durch Auge und Kante modellieren, verkettet mit dem Schnitt.")

row("2023MerhoehtBAGLAA2WTR1", "f", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Achsenparallele Ebene einer Bewegung aus der Parameterdarstellung angeben", typ_neben="",
    stichwoerter="x₂ = 5 konstant|L parallel zur x₁x₃-Ebene|x₂ = 5",
    voraussetzungen="Konstante Koordinate als Ebene|Parallelität zu Koordinatenebenen",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Werbemast/Gebäude", textumfang="mittel",
    gegeben="Flugbahn (32 − 8t | 5 | −5t² + 6,5t + 0,3), t Sekunden seit dem Schuss",
    gesucht="besondere Lage der Ebene L der Flugbahn; Gleichung",
    verfahren="x₂-Koordinate konstant erkennen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="L verläuft parallel zur x₁x₃-Ebene und wird durch x₂ = 5 dargestellt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Ebene als x₁x₃-Ebene selbst bezeichnen",
    bemerkung="Standardbezug: K1 I, K4 I. AB amtlich: I. Amtlich.")

row("2023MerhoehtBAGLAA2WTR1", "g", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Lage eines bewegten Punktes gegenüber einer Mauer über Zeitpunkt und Höhe untersuchen", typ_neben="",
    stichwoerter="Mauer bei x₁ = 20: 32 − 8t = 20 ⇔ t = 1,5|Höhe −5 · 1,5² + 6,5 · 1,5 + 0,3 < 0|Ball schon am Boden ⇒ trifft die Mauer nicht",
    voraussetzungen="Zeitpunkt aus einer Koordinate|Höhe zum Zeitpunkt auswerten|Vergleich mit Boden und Mauerhöhe",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Werbemast/Gebäude", textumfang="kurz",
    gegeben="Flugbahn wie in f; Mauer in der Ebene x₁ = 20 mit Höhe 3",
    gesucht="ob der Ball die Mauer trifft, bevor er den Boden berührt",
    verfahren="Zeitpunkt des Erreichens von x₁ = 20 berechnen, Höhe dort prüfen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="s|m", abhaengig_von="",
    ergebnis="32 − 8t = 20 ⇔ t = 3/2; wegen −5 · (3/2)² + 6,5 · 3/2 + 0,3 < 0 trifft der Ball die Mauer nicht, bevor er den Boden berührt (amtlich)",
    zwischenergebnis="Höhe −1,2", niveau_geschaetzt="III",
    fehlerquelle="Höhe nur mit 3 vergleichen, Bodenberührung (Höhe 0) übersehen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K4 II, K5 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Treffbedingung in Zeitpunkt und Höhenvergleich übersetzen.")

# ---- AG/LA A2 WTR 2: Körper ABCDEF (Prisma mit schräger Deckfläche)
KO = "Abbildung: Schrägbild des Körpers mit Grundfläche ABC in der x₁x₂-Ebene (A(6|3|0), B(0|6|0), C(3|0|0)), senkrechten Kanten AD (Länge 6), BE (Länge 6), CF (Länge 12) und schräger Deckfläche DEF; Achsen x₁, x₂, x₃"
row("2023MerhoehtBAGLAA2WTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="x = (6; 3; 6) + μ(1; 1; −2) + σ(−2; 1; 0)|Parameter eliminieren|2x₁ + 4x₂ + 3x₃ − 42 = 0",
    voraussetzungen="Parameterform aus drei Punkten|Gleichungssystem eliminieren oder Normalenvektor",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="Körper", skizze=KO, kontext="ohne", textumfang="kurz",
    gegeben="A(6|3|0), B(0|6|0), C(3|0|0), D(6|3|6), E(0|6|6), F(3|0|12); L durch D, E, F; Kontrolle 2x₁ + 4x₂ + 3x₃ − 42 = 0",
    gesucht="Koordinatengleichung von L",
    verfahren="Parametergleichung aufstellen, Parameter über die Koordinatengleichungen eliminieren",
    schritte="3", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="x = (6; 3; 6) + μ(1; 1; −2) + σ(−2; 1; 0) liefert x₁ = 6 + μ − 2σ, x₂ = 3 + μ + σ, x₃ = 6 − 2μ; aus III μ = 3 − x₃/2, aus II σ = −6 + x₂ + x₃/2, mit I x₁ = 21 − 2x₂ − 3/2x₃ (amtlich)",
    zwischenergebnis="Normalenvektor (2; 4; 3)", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen beim Eliminieren",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Lauf 7).")

row("2023MerhoehtBAGLAA2WTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="n = (2; 4; 3), Normalenvektor der x₁x₂-Ebene (0; 0; 1)|cos φ = 3/√29|φ ≈ 56°",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=KO, kontext="ohne", textumfang="kurz",
    gegeben="L: 2x₁ + 4x₂ + 3x₃ = 42",
    gesucht="Winkel zwischen L und der x₁x₂-Ebene",
    verfahren="Kosinus des Winkels aus den Normalenvektoren",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2023MerhoehtBAGLAA2WTR2-1a",
    ergebnis="cos φ = ((2; 4; 3) · (0; 0; 1)) / √(2² + 4² + 3²) = 3/√29 liefert φ ≈ 56° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Sinus statt Kosinus",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")

row("2023MerhoehtBAGLAA2WTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächenterm eines Dreiecks als Quadrat minus Randdreiecke in der Abbildung veranschaulichen", typ_neben="",
    stichwoerter="Quadrat 6 × 6 in der x₁x₂-Ebene|abgezogen: Dreieck mit Katheten 3, 3 und zwei Dreiecke mit Katheten 3, 6|Eintragungen in die Abbildung",
    voraussetzungen="Umbeschriebenes Quadrat|Katheten aus Koordinaten",
    format="Zeichnen", operator="Veranschaulichen Sie", antwort="Grafik",
    material="Körper", skizze=KO + "; Erwartungshorizont: in die Grundebene eingezeichnetes Quadrat mit Seite 6 um das Dreieck ABC, die drei abgeschnittenen rechtwinkligen Dreiecke mit Katheten 3, 3 und 3, 6 (zweimal) beschriftet", kontext="ohne", textumfang="kurz",
    gegeben="Flächeninhalt von ABC über 6 · 6 − 1/2 · 3 · 3 − 2 · 1/2 · 3 · 6",
    gesucht="Veranschaulichung durch Eintragungen in der Abbildung",
    verfahren="Quadrat um das Dreieck legen, die drei Eckdreiecke markieren und bemaßen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Quadrat der Seitenlänge 6 um ABC in der Grundebene, davon abgezogen ein Dreieck mit Katheten 3 und 3 sowie zwei Dreiecke mit Katheten 3 und 6 (amtlich)",
    zwischenergebnis="Fläche 27/2", niveau_geschaetzt="II",
    fehlerquelle="Dreieck ABC selbst statt der Restdreiecke beschriften",
    bemerkung="Standardbezug: K1 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (27/2 über das Kreuzprodukt). Abweichung: meine Schätzung II (Zerlegung in der Abbildung erkennen), amtlich I.")

row("2023MerhoehtBAGLAA2WTR2", "d", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen aus Prisma und aufgesetzter Pyramide berechnen", typ_neben="",
    stichwoerter="Grundfläche 27/2|Prisma bis Höhe 6: 27/2 · 6|Pyramide mit Spitze F, Höhe 6: 1/3 · 27/2 · 6|108",
    voraussetzungen="Zerlegung in Prisma und Pyramide|Volumenformeln",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=KO, kontext="ohne", textumfang="kurz",
    gegeben="Körper ABCDEF wie in a; Grundfläche 27/2",
    gesucht="Volumen",
    verfahren="Prisma der Höhe 6 plus Pyramide über dem Dreieck in Höhe 6 mit Spitze F",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="6 · 6 − 1/2 · 3 · 3 − 2 · 1/2 · 3 · 6 = 27/2; 27/2 · 6 + 1/3 · 27/2 · 6 = 108 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Pyramidenvolumen ohne Faktor 1/3",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Zerlegung des schrägen Körpers), amtlich I.")

row("2023MerhoehtBAGLAA2WTR2", "e", innen="1", seite="1", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Parameterbereich, in dem eine Ebenenschar dieselben Kanten eines Körpers schneidet, bestimmen", typ_neben="",
    stichwoerter="N_k enthält x₃-Achse und P_k(1 − k | k | 0): senkrechte Ebene durch den Ursprung|P_k auf OA für 6/3 = (1 − k)/k ⇔ k = 1/3|größter Bereich ]1/3; 1[|Kanten BC, EF, AB, DE",
    voraussetzungen="Ebene durch Achse als Drehung um die x₃-Achse|Richtung von P_k mit OA, OB, OC vergleichen|Kanten des Prismas über der Grundfläche",
    format="Rechnung|Kurzantwort", operator="Bestimmen Sie|Geben Sie an", antwort="Text",
    material="Körper", skizze=KO, kontext="ohne", textumfang="lang",
    gegeben="N_k enthält die x₃-Achse und P_k(1 − k | k | 0), k ∈ ]0; 1[; Bereiche ]a; b[ mit jeweils gleichen geschnittenen Kanten",
    gesucht="größter solcher Bereich und die zugehörigen Kanten",
    verfahren="Parameter bestimmen, für die N_k durch A, B oder C läuft (Richtungsvergleich in der Grundebene), Bereiche ablesen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="P_k liegt genau dann auf OA, wenn 6/3 = (1 − k)/k ⇔ k = 1/3 gilt; Intervall ]1/3; 1[; Kanten BC, EF, AB, DE (amtlich)",
    zwischenergebnis="P_k auf OC nur für k = 0, auf OB nur für k = 1 (Ränder)", niveau_geschaetzt="III",
    fehlerquelle="Bereich ]0; 1/3[ als größer ansehen oder senkrechte Kanten mitzählen",
    bemerkung="Standardbezug: K1 II, K2 III, K4 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Ebene als Drehung um die Achse deuten, verkettet mit der Fallunterscheidung an den Eckpunkten.")

row("2023MerhoehtBAGLAA2WTR2", "f", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Koordinate eines Punktes auf einer Kante für einen rechten Winkel über das Skalarprodukt berechnen", typ_neben="",
    stichwoerter="Q(6|3|q), 0 ≤ q ≤ 6|QR · QF = 0: 9 + (2 − q)(12 − q) = 0|q² − 14q + 33 = 0|q = 3",
    voraussetzungen="Punkt auf einer Kante mit Parameter|Skalarprodukt null|quadratische Gleichung mit Bereichsprüfung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=KO, kontext="ohne", textumfang="kurz",
    gegeben="Q auf AD, R(0|6|2) auf BE; Dreieck FQR mit rechtem Winkel bei Q",
    gesucht="x₃-Koordinate von Q",
    verfahren="Q(6|3|q) ansetzen, QR · QF = 0 lösen, Lösung im Kantenbereich wählen",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="QR · QF = 0 ⇔ (−6; 3; 2 − q) · (−3; −3; 12 − q) = 0 ⇔ 9 + (2 − q)(12 − q) = 0 ⇔ q² − 14q + 33 = 0 ⇔ q = 7 − √(49 − 33) = 3 (amtlich)",
    zwischenergebnis="zweite Lösung 11 außerhalb der Kante", niveau_geschaetzt="II",
    fehlerquelle="Lösung 11 nicht ausschließen",
    bemerkung="Standardbezug: K1 I, K2 II, K4 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBAGLAA2WTR2", "g", innen="1", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Aufgabenstellung zu einer Drehung um eine Kante aus Lotfußpunkt und Rechenweg formulieren", typ_neben="",
    stichwoerter="AB · (OB + λ · BA − OC) = 0 ⇒ λ = 0,8, S(4,8 | 3,6 | 0)|S Lotfußpunkt von C auf AB|OT = OS + |CS| · (0; 0; 1): C nach der Drehung|Aufgabe: Koordinaten von T ermitteln",
    voraussetzungen="Lotfußpunkt über Orthogonalität|Drehung um eine Achse erhält den Abstand|Rechenweg lesen",
    format="Kurzantwort|Begründung", operator="Formulieren Sie|Geben Sie an", antwort="Text",
    material="Körper", skizze=KO, kontext="ohne", textumfang="lang",
    gegeben="Drehung um die Gerade AB, D landet in der x₁x₂-Ebene mit positiver x₂-Koordinate; Rechnungen: (6; −3; 0) · ((0; 6; 0) + λ(6; −3; 0) − (3; 0; 0)) = 0 ⇔ λ = 0,8, S(4,8 | 3,6 | 0); OT = OS + |CS| · (0; 0; 1)",
    gesucht="passende Aufgabenstellung; Bedeutung von S",
    verfahren="Erste Rechnung als Lot von C auf AB erkennen, zweite als Drehung von C um 90° nach oben",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Aufgabenstellung: Der mit C bezeichnete Eckpunkt wird nach der Drehung mit T bezeichnet, ermitteln Sie die Koordinaten von T; S ist der Fußpunkt des Lots von C auf AB (amtlich)",
    zwischenergebnis="|CS| = √(1,8² + 3,6²) ≈ 4,02, T(4,8 | 3,6 | 4,02)", niveau_geschaetzt="III",
    fehlerquelle="S als Mittelpunkt von AB deuten",
    bemerkung="Standardbezug: K1 III, K2 II, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Lotfußpunkt und Drehung um 90° aus dem Rechenweg deuten, verkettet zur Aufgabenstellung.")

# ---- Stochastik WTR 1: Glücksrad 0–9, Spiel, zehnseitiger Holzkörper
GR = "Glücksrad mit zehn gleich großen Sektoren, beschriftet mit 0 bis 9"
row("2023MerhoehtBStochastikWTR1", "", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln", typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="X Anzahl ungerader Zahlen, n = 20, p = 0,5|P(X = 7) ≈ 7 %|P(8 ≤ X ≤ 12) ≈ 74 %",
    voraussetzungen="p = 0,5 aus fünf ungeraden Sektoren|Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Figur", skizze=GR, kontext="Glücksrad/Spiel", textumfang="kurz",
    gegeben="Glücksrad 0 bis 9 gleich groß, 20 Drehungen; A: genau siebenmal ungerade; B: mehr als siebenmal und höchstens zwölfmal ungerade",
    gesucht="P(A), P(B)",
    verfahren="Binomialverteilung n = 20, p = 0,5 am Rechner",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="X: Anzahl der erzielten ungeraden Zahlen; P₀,₅²⁰(X = 7) ≈ 7 %, P₀,₅²⁰(8 ≤ X ≤ 12) ≈ 74 % (amtlich)",
    zwischenergebnis="0,0739, 0,7368", niveau_geschaetzt="I",
    fehlerquelle="„mehr als siebenmal“ als X ≥ 7",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typen wiederverwendet (2025-ea-B, 2026-ga-B).")

row("2023MerhoehtBStochastikWTR1", "", innen="2", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen", typ_neben="",
    stichwoerter="Ergebnisraum 100 Paare|C: Summe < 4: 10 Ergebnisse|D: Produkt 2 oder 3: 4 Ergebnisse, davon 2 in C|Anteil 2/10 ≠ 4/100 ⇒ abhängig",
    voraussetzungen="Ergebnisse auszählen|Unabhängigkeit über Anteile oder Produktregel",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Figur", skizze=GR, kontext="Glücksrad/Spiel", textumfang="mittel",
    gegeben="zweimal drehen; C: Summe kleiner als 4; D: Produkt ist 2 oder 3",
    gesucht="ob C und D stochastisch unabhängig sind",
    verfahren="Günstige Paare zählen, P(D | C) mit P(D) oder P(C ∩ D) mit P(C) · P(D) vergleichen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Im Ergebnisraum {(0;0), (0;1), …, (9;9)} ist die Summe bei zehn Ergebnissen kleiner als 4; bei zwei dieser zehn, aber nur bei vier von allen ist das Produkt 2 oder 3; die Anteile stimmen nicht überein, C und D sind stochastisch abhängig (amtlich)",
    zwischenergebnis="P(C ∩ D) = 0,02 ≠ 0,1 · 0,04", niveau_geschaetzt="II",
    fehlerquelle="Paare (1;2) und (2;1) nur einmal zählen",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2023MerhoehtBStochastikWTR1", "a", innen="3", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für mehrere Wiederholungen ohne Abbruch als Potenz berechnen", typ_neben="",
    stichwoerter="keine „0“ in vier Drehungen|(9/10)⁴ ≈ 66 %",
    voraussetzungen="Pfadregel mit gleichen Faktoren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Figur", skizze=GR, kontext="Glücksrad/Spiel", textumfang="lang",
    gegeben="Spiel: beliebig oft drehen, Auszahlung Summe der Zahlen in Euro, bei „0“ Ende ohne Auszahlung; erster Spieler dreht viermal, sofern keine „0“",
    gesucht="Wahrscheinlichkeit für eine Auszahlung",
    verfahren="Viermal keine „0“",
    schritte="1", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="(9/10)⁴ ≈ 66 % (amtlich)",
    zwischenergebnis="0,6561", niveau_geschaetzt="I",
    fehlerquelle="1 − (1/10)⁴",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBStochastikWTR1", "b", innen="3", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert einer weiteren Runde mit dem sicheren Betrag vergleichen und eine Empfehlung begründen", typ_neben="",
    stichwoerter="Auszahlung 61 bis 69 je 1/10, bei „0“ nichts|E = 1/10 · (61 + … + 69) = 58,5|58,5 < 60 ⇒ beenden",
    voraussetzungen="Erwartungswert einer Gleichverteilung|Vergleich mit sicherem Wert",
    format="Rechnung|Begründung", operator="Berechnen Sie|Geben Sie ab|Begründen Sie", antwort="Zahl",
    material="Figur", skizze=GR, kontext="Glücksrad/Spiel", textumfang="mittel",
    gegeben="zweiter Spieler hat Summe 60; sofort beenden oder genau einmal weiterdrehen",
    gesucht="Erwartungswert der Auszahlung bei einer weiteren Drehung; Empfehlung mit Begründung",
    verfahren="Erwartungswert über die zehn gleich wahrscheinlichen Ausgänge, mit 60 vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="Euro", abhaengig_von="",
    ergebnis="Erwartungswert in Euro: 1/10 · (61 + 62 + … + 69) = 58,5; wegen 58,5 < 60 sollte der Spieler das Spiel sofort beenden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Ausgang „0“ als Auszahlung 60 statt 0 werten",
    bemerkung="Standardbezug: K1 II, K3 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBStochastikWTR1", "c", innen="3", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Aussage über gleiche Erwartungswerte aufeinanderfolgender Parameterwerte über eine Gleichung beurteilen", typ_neben="",
    stichwoerter="5n · 0,9ⁿ = 5(n + 1) · 0,9ⁿ⁺¹ ⇔ n = (n + 1) · 0,9 ⇔ n = 9|nur 9 und 10 gleich ⇒ Aussage richtig",
    voraussetzungen="Gleichung mit Potenzen kürzen|Eindeutigkeit der Lösung",
    format="Begründung|Rechnung", operator="Beurteilen Sie", antwort="Text",
    material="Figur", skizze=GR, kontext="Glücksrad/Spiel", textumfang="mittel",
    gegeben="Erwartungswert bei n Drehungen 5n · 0,9ⁿ; Aussage: es gibt zwei, aber nicht drei aufeinanderfolgende n mit gleichem Erwartungswert",
    gesucht="Beurteilung",
    verfahren="E(n) = E(n + 1) lösen, Eindeutigkeit als Begründung",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="5n · (9/10)ⁿ = 5 · (n + 1) · (9/10)ⁿ⁺¹ ⇔ n = (n + 1) · 9/10 ⇔ n = 9; damit sind 9 und 10 die einzigen aufeinanderfolgenden Werte mit gleichem Erwartungswert, die Aussage ist richtig (amtlich)",
    zwischenergebnis="E(9) = E(10) ≈ 17,4", niveau_geschaetzt="III",
    fehlerquelle="Werte durchprobieren ohne Nachweis der Eindeutigkeit",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis über die Gleichung in n.")

row("2023MerhoehtBStochastikWTR1", "a", innen="4", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Konfidenzintervalle",
    typ="Obere Grenze eines Konfidenzintervalls über den Stichprobenanteil begründen und Verträglichkeit einer Annahme beschreiben", typ_neben="",
    stichwoerter="Stichprobenanteil 12/80 = 0,15 > 0,1 liegt im Intervall|obere Grenze größer als 0,15 > 0,1|Annahme p = 0,1 mit dem Ergebnis verträglich",
    voraussetzungen="Stichprobenanteil liegt im Konfidenzintervall|Verträglichkeit als Enthaltensein",
    format="Begründung", operator="Begründen Sie|Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksrad/Spiel", textumfang="lang",
    gegeben="zehnseitiger Holzkörper 0 bis 9; 80 Würfe, zwölfmal „0“; Konfidenzintervall zur Sicherheitswahrscheinlichkeit 95 % mit unterer Grenze etwa 0,09",
    gesucht="Begründung, dass die obere Grenze größer als 0,1 ist; Bedeutung für die Annahme p = 10 %",
    verfahren="Stichprobenanteil als Punkt im Intervall, Vergleich mit 0,1",
    schritte="2", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="12/80 ist größer als 0,1 und liegt innerhalb des Konfidenzintervalls; das Ergebnis der 80 Würfe steht bei der gegebenen Sicherheitswahrscheinlichkeit in Einklang mit der Annahme (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="obere Grenze über die Symmetrie um 0,15 rechnen wollen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBStochastikWTR1", "b", innen="4", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Konfidenzintervalle",
    typ="Kleinsten Stichprobenumfang für die Unverträglichkeit eines Anteils mit einer Annahme über die Näherungsformel ermitteln", typ_neben="",
    stichwoerter="|0,15 − 0,1| ≤ 1,96 · √(0,1 · 0,9/n) für n = 120|> für n = 140|kleinstes n = 140 (in Zwanzigerschritten geprüft)|Grenze n ≈ 138,3",
    voraussetzungen="Sigma-Umgebung um p mit 1,96|Ungleichung in n|Probieren am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksrad/Spiel", textumfang="mittel",
    gegeben="Annahme p = 0,1; beobachtet genau 15 % „0“; Sicherheitswahrscheinlichkeit 95 %",
    gesucht="kleinste Anzahl von Würfen, bei der 15 % nicht mit p = 0,1 verträglich sind",
    verfahren="Abstand 0,05 mit 1,96 · √(p(1 − p)/n) vergleichen, n suchen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="|0,15 − 0,1| ≤ 1,96 · √(0,1(1 − 0,1)/120) und |0,15 − 0,1| > 1,96 · √(0,1(1 − 0,1)/140); damit ist 140 die gesuchte Anzahl von Würfen; bei anderen Näherungsverfahren können sich abweichende Ergebnisse ergeben (amtlich)",
    zwischenergebnis="exakte Grenze der Näherung n > 138,3, also 139 mit ganzzahligem Schritt", niveau_geschaetzt="III",
    fehlerquelle="Anzahl statt Anteil in die Formel setzen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt; der Erwartungshorizont prüft n = 120 und 140, die Ungleichung gibt 139 als kleinste ganze Zahl – beides zulässig (Hinweis im Erwartungshorizont). Eichregel: (a) Unverträglichkeit in eine Ungleichung für n übersetzen.")

# ---- Stochastik WTR 2 (Kurzbeschreibung „MMS/WTR“, MMS-Zwilling ist Dublette): Urlaubsreisen, Gewinnspiel
row("2023MerhoehtBStochastikWTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen", typ_neben="Baumdiagramm zu einer zweistufigen Situation erstellen",
    stichwoerter="Baum: W 45 % mit Z 80 %, ¬W 55 % mit Z a|0,45 · 0,8 + 0,55 · a = 0,778|a = 0,76",
    voraussetzungen="Baumdiagramm beschriften|Pfadregeln|lineare Gleichung",
    format="Zeichnen|Rechnung", operator="Stellen Sie dar|Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine; Erwartungshorizont: Baumdiagramm mit W 45 % / ¬W 55 % und Ästen Z 80 %, ¬Z 20 % bzw. Z a, ¬Z 1 − a", kontext="Urlaubsreisen/Umfrage", textumfang="lang",
    gegeben="45 % weiblich; unter den weiblichen 80 % zufrieden, unter den nicht weiblichen Anteil a; P(Z) = 77,8 %",
    gesucht="Baumdiagramm; Wert von a",
    verfahren="Beide Pfade zu Z addieren und gleich 0,778 setzen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,45 · 0,8 + 0,55 · a = 0,778 ⇔ a = 0,76; Baumdiagramm mit W 45 %, ¬W 55 %, Z 80 %, ¬Z 20 %, Z a, ¬Z 1 − a (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="a als P(Z ∩ ¬W) statt als bedingten Anteil",
    bemerkung="Standardbezug: K2 II, K3 I, K4 I, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typen wiederverwendet (2026-ga-B, Teil A).")

row("2023MerhoehtBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anzahlvergleich zweier Teilgruppen über Pfadwahrscheinlichkeiten nachweisen", typ_neben="",
    stichwoerter="0,45 · 0,8 = 0,36|0,55 · 0,7 = 0,385|0,36 < 0,385",
    voraussetzungen="Pfadwahrscheinlichkeiten als Anteile an der Gesamtgruppe",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urlaubsreisen/Umfrage", textumfang="kurz",
    gegeben="a = 0,7",
    gesucht="Nachweis, dass weniger weibliche als nicht weibliche Personen zufrieden waren",
    verfahren="Beide Schnittanteile berechnen und vergleichen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,45 · 0,8 = 0,36 < 0,385 = 0,55 · 0,7 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur 0,8 mit 0,7 vergleichen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBStochastikWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen", typ_neben="",
    stichwoerter="a = 0,8|gleicher Zufriedenheitsanteil in beiden Gruppen ⇒ Z unabhängig von W",
    voraussetzungen="Unabhängigkeit als Gleichheit der bedingten Anteile",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urlaubsreisen/Umfrage", textumfang="kurz",
    gegeben="Baumdiagramm wie in a mit unbekanntem a",
    gesucht="a für stochastische Unabhängigkeit von W und Z, Begründung ohne Rechnung",
    verfahren="Bedingte Anteile gleichsetzen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="a = 0,8; für diesen Wert ist der Anteil der Zufriedenen unter den nicht weiblichen Personen ebenso groß wie unter den weiblichen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="a = 0,45 (Anteil der Weiblichen) angeben",
    bemerkung="Standardbezug: K1 I, K3 I, K6 I. AB amtlich: I. Amtlich. Abweichung: meine Schätzung II (Unabhängigkeit über gleiche bedingte Anteile begründen), amtlich I.")

row("2023MerhoehtBStochastikWTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen", typ_neben="",
    stichwoerter="P(W | ¬Z) = 0,45 · 0,2 / (0,45 · 0,2 + 0,55 · (1 − a))|a größer ⇒ Anteil Unzufriedener unter ¬W sinkt|unter den Unzufriedenen wächst der Anteil der Weiblichen",
    voraussetzungen="Bedingte Wahrscheinlichkeit als Anteil unter den Unzufriedenen|Zusammensetzung der Bedingungsmenge",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Urlaubsreisen/Umfrage", textumfang="mittel",
    gegeben="Person war nicht zufrieden; a wächst",
    gesucht="Begründung im Sachzusammenhang, dass P(weiblich | nicht zufrieden) mit a zunimmt",
    verfahren="Unzufriedene unter ¬W nehmen ab, unter W bleiben sie konstant, also wächst der Anteil der Weiblichen unter den Unzufriedenen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Mit zunehmendem a nimmt der Anteil der Unzufriedenen unter den nicht weiblichen Personen ab, während er unter den weiblichen konstant bleibt; damit nimmt unter den Unzufriedenen der Anteil der weiblichen Personen zu (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="mit P(¬Z | W) statt P(W | ¬Z) argumentieren",
    bemerkung="Standardbezug: K1 III, K3 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (d) Bayes-Quotient im Sachzusammenhang deuten, verkettet mit der Monotonie in a. Typ wiederverwendet (2026-ga-B), hier begründen statt beurteilen.")

row("2023MerhoehtBStochastikWTR2", "a", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Restwahrscheinlichkeit und Erwartungswert eines Teilgewinns aus dem Gesamterwartungswert bestimmen", typ_neben="",
    stichwoerter="1 − (8 · 10⁻⁴ + 5 · 10⁻⁵ + 2 · 10⁻⁵ + 3 · 10⁻⁶) = 0,999127 > 0,999|0,999127 · x + 0,16 + 0,025 + 0,02 + 0,03 = 0,435|x ≈ 0,20 Euro",
    voraussetzungen="Gegenwahrscheinlichkeit|Erwartungswert als gewichtete Summe|Gleichung nach dem unbekannten Wert auflösen",
    format="Rechnung", operator="Zeigen Sie|Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle: Anzahl Strandkörbe 2, 3, 4, 5; Gutscheinwert 200, 500, 1000, 10 000 Euro; Wahrscheinlichkeit 8 · 10⁻⁴, 5 · 10⁻⁵, 2 · 10⁻⁵, 3 · 10⁻⁶", kontext="Gewinnspiel/Reiseunternehmen", textumfang="lang",
    gegeben="Gewinnspiel mit 1 bis 5 Strandkörben; bei 1 Strandkorb Sachgewinne; Tabelle der Gutscheine; Erwartungswert des Gewinns 43,5 Cent je Person",
    gesucht="Nachweis P(1 Strandkorb) > 1 − 0,001; Erwartungswert des Gewinns bei einem Strandkorb",
    verfahren="Gegenwahrscheinlichkeit der Gutscheine; Erwartungswertgleichung nach dem Sachgewinn-Erwartungswert x auflösen",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="Euro", abhaengig_von="",
    ergebnis="1 − (8 · 10⁻⁴ + 5 · 10⁻⁵ + 2 · 10⁻⁵ + 3 · 10⁻⁶) = 0,999127 > 1 − 0,001; 0,999127 · x + 8 · 10⁻⁴ · 200 + 5 · 10⁻⁵ · 500 + 2 · 10⁻⁵ · 1000 + 3 · 10⁻⁶ · 10000 = 0,435 liefert x ≈ 0,20, der Erwartungswert beträgt etwa 20 Cent (amtlich)",
    zwischenergebnis="x ≈ 0,2002", niveau_geschaetzt="II",
    fehlerquelle="Cent und Euro mischen",
    bemerkung="Standardbezug: K2 I, K3 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBStochastikWTR2", "b", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln", typ_neben="",
    stichwoerter="μ = 8 · 10⁻⁴ · 80 000 = 64|P(55 ≤ X ≤ 73) ≈ 77 %|P(54 ≤ X ≤ 74) ≈ 81 %|c = 10",
    voraussetzungen="Erwartungswert n · p|kumulierte Binomialwahrscheinlichkeit am Rechner|Probieren mit Nachbarwerten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Gewinnspiel/Reiseunternehmen", textumfang="mittel",
    gegeben="80 000 Teilnehmer; X Anzahl mit zwei Strandkörben, p = 8 · 10⁻⁴; Intervall [μ − c; μ + c] mit Wahrscheinlichkeit mindestens 80 %",
    gesucht="kleinster ganzzahliger Wert von c",
    verfahren="μ berechnen, symmetrische Intervalle mit wachsendem c am Rechner prüfen",
    schritte="3", zahlenraum="ganz|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="μ = 8 · 10⁻⁴ · 80000 = 64; P(55 ≤ X ≤ 73) ≈ 77 %, P(54 ≤ X ≤ 74) ≈ 81 %; damit c = 10 (amtlich)",
    zwischenergebnis="σ ≈ 8, Sigma-Regel 1,28σ ≈ 10,2", niveau_geschaetzt="II",
    fehlerquelle="c über die Sigma-Regel ohne Nachbarwertprüfung",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Kein Rückgriff auf „Kleinste Umgebungsbreite unterhalb des Erwartungswerts …“ (einseitig, anderer Ansatz).")

row("2023MerhoehtBStochastikWTR2", "c", innen="2", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Nutzen eines größeren Stichprobenumfangs über den Fehler zweiter Art an den Gütekurven begründen", typ_neben="",
    stichwoerter="H₀: p ≥ 2 %, Ablehnung heißt keine Verlängerung|Fehler zweiter Art: p < 0,02, aber nicht abgelehnt ⇒ irrtümliche Verlängerung|bei p = 0,014 liegt der Graph zu n₂ höher ⇒ kleinerer Fehler zweiter Art für n₂|lohnt sich, wenn die Mehrkosten des Tests gering gegen die vermiedenen Verluste sind",
    voraussetzungen="Gütekurve lesen (Ablehnwahrscheinlichkeit in Abhängigkeit von p)|Fehler zweiter Art als Gegenwahrscheinlichkeit der Ablehnung bei falscher H₀|Kosten-Nutzen-Abwägung",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm", skizze="Koordinatensystem p von 0 bis 0,02 (und darüber), Wahrscheinlichkeit 0 bis 1; zwei fallende Kurven der Ablehnwahrscheinlichkeit: Graph zu n₁ (gepunktet) flacher, Graph zu n₂ (gestrichelt) steiler, beide nahe 1 bei p = 0 und nahe 0 ab etwa p = 0,02, n₁ < n₂", kontext="Gewinnspiel/Reiseunternehmen", textumfang="lang",
    gegeben="p Buchungswahrscheinlichkeit; Verlängerung lohnt für p ≥ 2 %; H₀: p ≥ 2 % auf 5 %; größerer Stichprobenumfang teurer; Abbildung der Ablehnwahrscheinlichkeit für n₁ < n₂",
    gesucht="Bedingung, unter der sich der größere Umfang lohnen könnte, begründet mit Abbildung und Fehler zweiter Art",
    verfahren="Fehler zweiter Art als irrtümliche Verlängerung deuten, an einem p < 0,02 die Kurven vergleichen, gegen die Testkosten abwägen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Der Fehler zweiter Art kann bei p < 0,02 auftreten, etwa p = 0,014; dort liegt der Graph zu n₂ oberhalb des Graphen zu n₁, die Wahrscheinlichkeit, das Gewinnspiel irrtümlich zu verlängern, ist für n₂ kleiner; bei größerem Umfang ist das Verlustrisiko geringer, die Testkosten aber höher – der größere Umfang könnte sich lohnen, wenn die zusätzlichen Kosten verhältnismäßig gering wären (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Fehler erster Art (irrtümliches Nichtverlängern) heranziehen",
    bemerkung="Standardbezug: K1 III, K3 III, K4 II, K6 III. AB amtlich: III. Amtlich. Eichregel: (d) Fehler zweiter Art im Sachzusammenhang deuten, verkettet mit dem Kurvenvergleich und der Kostenabwägung.")

# ---- Stochastik WTR 3: Olivenöl, Füllmenge, Anhänger
row("2023MerhoehtBStochastikWTR3", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aufgabenstellung zu einer Potenz der Gegenwahrscheinlichkeit formulieren und Ansatz erläutern", typ_neben="",
    stichwoerter="0,985¹² ≈ 83,4 %|0,985 = 1 − 0,015 Wahrscheinlichkeit für mindestens 600 ml|zwölf Flaschen alle in Ordnung",
    voraussetzungen="Gegenwahrscheinlichkeit|Pfadregel für gleiche unabhängige Ereignisse",
    format="Kurzantwort|Begründung", operator="Formulieren Sie|Erläutern Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Olivenöl/Abfüllung", textumfang="mittel",
    gegeben="Karton mit zwölf Flaschen; P(Flasche unter 600 ml) = 1,5 %; Rechnung 0,985¹² ≈ 83,4 %",
    gesucht="passende Aufgabenstellung; Erläuterung des Ansatzes",
    verfahren="0,985 als Gegenwahrscheinlichkeit je Flasche, Potenz 12 als alle Flaschen des Kartons",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Aufgabenstellung: Berechnen Sie die Wahrscheinlichkeit dafür, dass in einem Karton alle Flaschen mindestens 600 ml Öl enthalten; die Wahrscheinlichkeit für eine Flasche beträgt 1 − 0,015 = 0,985, für alle zwölf Flaschen 0,985¹² (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="„höchstens eine Flasche zu wenig“ formulieren (das wäre der Karton ohne Fehler, ein anderer Term)",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Term in eine Aufgabenstellung übersetzen), amtlich I.")

row("2023MerhoehtBStochastikWTR3", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Mindestanzahl aus einer Erwartungswertbedingung n · p > c ermitteln", typ_neben="",
    stichwoerter="m · 0,985 > 780|m ≥ 792",
    voraussetzungen="Erwartungswert n · p als Mittel|Ungleichung lösen und aufrunden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Olivenöl/Abfüllung", textumfang="kurz",
    gegeben="Lieferung von m Flaschen; im Mittel mehr als 780 Flaschen mit mindestens 600 ml",
    gesucht="Mindestzahl gelieferter Flaschen",
    verfahren="m · 0,985 > 780 nach m auflösen, auf ganze Zahl aufrunden",
    schritte="2", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="m · 0,985 > 780 ⇔ m ≥ 792 (amtlich)",
    zwischenergebnis="780/0,985 ≈ 791,9", niveau_geschaetzt="II",
    fehlerquelle="m = 791 (abrunden)",
    bemerkung="Standardbezug: K1 I, K2 II, K3 I, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtBStochastikWTR3", "c", innen="1", seite="1", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Fehlerwahrscheinlichkeit einer Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden", typ_neben="",
    stichwoerter="Y Flaschen unter 600 ml je Karton, n = 12, p = 0,015: P(Y ≥ 2) ≈ 0,013|Z fehlerhafte Kartons, n = 150, p = 0,013|3 % von 150 = 4,5 ⇒ Z ≥ 5|P(Z ≥ 5) ≈ 5 %",
    voraussetzungen="„mehr als eine“ als Y ≥ 2|zweistufiges Modell|Prozentanteil in Anzahl umrechnen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Olivenöl/Abfüllung", textumfang="mittel",
    gegeben="Karton fehlerhaft, wenn mehr als eine Flasche unter 600 ml; Lieferung 150 Kartons",
    gesucht="Wahrscheinlichkeit, dass mehr als 3 % der Kartons fehlerhaft sind",
    verfahren="Fehlerwahrscheinlichkeit eines Kartons binomial, dann Binomialverteilung über die Kartons mit Z ≥ 5",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Y: Anzahl der Flaschen mit weniger als 600 ml; P₀,₀₁₅¹²(Y ≥ 2) ≈ 0,013; Z: Anzahl der fehlerhaften Kartons; 3 % · 150 = 4,5; P₀,₀₁₃¹⁵⁰(Z ≥ 5) ≈ 5 % (amtlich)",
    zwischenergebnis="0,01344; 0,0528", niveau_geschaetzt="III",
    fehlerquelle="„mehr als 3 %“ als Z ≥ 4 oder Y ≥ 1 statt Y ≥ 2",
    bemerkung="Standardbezug: K2 III, K3 I, K5 I, K6 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) zwei Binomialmodelle verketten, Anteilsbedingung übersetzen.")

row("2023MerhoehtBStochastikWTR3", "a", innen="2", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Wahrscheinlichkeit eines Intervalls der Normalverteilung mit dem Rechner berechnen", typ_neben="",
    stichwoerter="μ = 600,5, σ = 0,23|P(X > 601) ≈ 1,5 %|P(600 ≤ X ≤ 601) ≈ 97,0 %",
    voraussetzungen="Normalverteilung am Rechner|„höchstens 0,5 ml Abweichung“ als Intervall",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Olivenöl/Abfüllung", textumfang="kurz",
    gegeben="Füllmenge normalverteilt mit μ = 600,5 ml, σ = 0,23 ml; A: mehr als 601 ml; B: höchstens 0,5 ml vom Erwartungswert entfernt",
    gesucht="P(A), P(B)",
    verfahren="Normalverteilung am Rechner",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="ml", abhaengig_von="",
    ergebnis="X: Füllmenge in ml; P(A) = P(X > 601) ≈ 1,5 %; P(B) = P(600 ≤ X ≤ 601) ≈ 97,0 % (amtlich)",
    zwischenergebnis="0,01486; 0,9703", niveau_geschaetzt="I",
    fehlerquelle="B einseitig als P(X ≤ 601)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (Phi über erf). Typ wiederverwendet (2026-ea-B).")

row("2023MerhoehtBStochastikWTR3", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Eignung der Normalverteilung trotz negativer Werte im Definitionsbereich begründen", typ_neben="",
    stichwoerter="Wahrscheinlichkeit negativer Füllmengen praktisch null|Modell vernachlässigbar ungenau",
    voraussetzungen="Sigma-Regeln: weit entfernte Bereiche haben verschwindende Wahrscheinlichkeit",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Olivenöl/Abfüllung", textumfang="mittel",
    gegeben="Füllmenge nie negativ; Normalverteilung auch für negative Zahlen definiert mit positiven Dichtewerten",
    gesucht="Begründung, dass die Normalverteilung dennoch sinnvoll ist",
    verfahren="Wahrscheinlichkeit für negative Werte als vernachlässigbar klein einordnen",
    schritte="1", zahlenraum="dezimal", einheiten="ml", abhaengig_von="",
    ergebnis="Die Wahrscheinlichkeit, die die Normalverteilung für negative Füllmengen liefert, ist so gering, dass sie im Sachzusammenhang vernachlässigt werden kann (amtlich)",
    zwischenergebnis="μ liegt über 2600 Standardabweichungen über 0", niveau_geschaetzt="II",
    fehlerquelle="Dichtewert mit Wahrscheinlichkeit verwechseln",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich.")

row("2023MerhoehtBStochastikWTR3", "c", innen="2", seite="2", punkte="6", afb_amtlich="II",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Dichtefunktionen zu verschobenem Erwartungswert und kleinerer Standardabweichung skizzieren und Wirkung auf eine Wahrscheinlichkeit begründen", typ_neben="",
    stichwoerter="Vorschlag 1: Glockenkurve nach rechts verschoben|Vorschlag 2: schmalere, höhere Glocke um 600,5|Fläche links von 600 wird jeweils kleiner",
    voraussetzungen="Wirkung von μ und σ auf die Dichtekurve|Wahrscheinlichkeit als Fläche unter der Dichte",
    format="Zeichnen|Begründung", operator="Skizzieren Sie|Begründen Sie", antwort="Grafik",
    material="Diagramm", skizze="Abbildungen 1 und 2: je der Graph der Dichtefunktion (Glockenkurve) mit Maximum bei 600,5 auf einer x-Achse von 599,5 bis 601,5; Erwartungshorizont: in Abbildung 1 eine gleich hohe, nach rechts verschobene Glocke gestrichelt, in Abbildung 2 eine schmalere und höhere Glocke um 600,5 gestrichelt", kontext="Olivenöl/Abfüllung", textumfang="lang",
    gegeben="Vorschlag 1: eingestellte Füllmenge 600,5 ml erhöhen; Vorschlag 2: Genauigkeit erhöhen; Abbildungen 1 und 2 mit der bisherigen Dichtefunktion",
    gesucht="je Vorschlag eine passende Dichtefunktion skizzieren und begründen, dass P(X < 600) kleiner wird",
    verfahren="Verschiebung bzw. Stauchung der Glocke einzeichnen, Fläche links von 600 vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="ml", abhaengig_von="",
    ergebnis="Abbildung 1: nach rechts verschobene Glocke; Abbildung 2: schmalere, höhere Glocke um 600,5; die Wahrscheinlichkeit für weniger als 600 ml entspricht der Fläche zwischen Dichtegraph und x-Achse für x ≤ 600, jeder Vorschlag verkleinert diese Fläche (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="bei kleinerem σ die Glocke niedriger statt höher zeichnen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich. Kein Rückgriff auf „Dichtefunktion mit gleichem Erwartungswert und größerer Standardabweichung skizzieren“ (andere Richtung, zwei Vorschläge mit Begründung).")

row("2023MerhoehtBStochastikWTR3", "", innen="3", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Kleinstes n, für das die Wahrscheinlichkeit lauter verschiedener Ergebnisse unter eine Schranke fällt, ermitteln", typ_neben="",
    stichwoerter="P(alle verschieden) = n!/nⁿ|n = 6: 6!/6⁶ ≈ 1,5 %|n = 7: 7!/7⁷ ≈ 0,6 % < 1 %|kleinstes n = 7",
    voraussetzungen="Anzahl aller Folgen nⁿ|Anzahl der Folgen ohne Wiederholung n!|Probieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Olivenöl/Abfüllung", textumfang="mittel",
    gegeben="n verschiedene Motive, je Flasche zufällig eines; bei n Flaschen sind alle Motive verschieden mit Wahrscheinlichkeit unter 1 %",
    gesucht="kleinster möglicher Wert von n",
    verfahren="n!/nⁿ für wachsendes n berechnen, bis der Wert unter 1 % fällt",
    schritte="3", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Mit 6!/6⁶ ≈ 1,5 % und 7!/7⁷ ≈ 0,6 % ergibt sich 7 als kleinster möglicher Wert von n (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Anzahl der Folgen ohne Wiederholung als nⁿ − n",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Bedingung in den Term n!/nⁿ übersetzen, Schranke suchen.")

NEUE_TYPEN = [
    ("Nullstellen und Werte: Nullstellen aus Linearfaktoren im Sachzusammenhang nennen und ihre Vollständigkeit über die Faktorstruktur begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Nullstellen eines in Linearfaktoren gegebenen Terms als Zeitpunkte im Sachzusammenhang nennen und über die Anzahl und Gleichheit der Faktoren begründen, dass es keine weiteren gibt.",
     "2023MerhoehtBAnalysisWTR1-1a"),
    ("Negativen Wert einer Änderungsrate im Sachzusammenhang deuten", "Analysis", "Ableitung und Änderungsrate",
     "Die Aussage f(x₀) < 0 für eine Änderungsrate als Abnahme der Bestandsgröße zu diesem Zeitpunkt deuten.",
     "2023MerhoehtBAnalysisWTR1-1b"),
    ("Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen", "Analysis", "Rekonstruktion von Beständen",
     "Den Zeitpunkt des maximalen Bestands als die Nullstelle der Rate angeben, an der die Rate von positiv nach negativ wechselt, und dies über das Vorzeichen der Rate begründen.",
     "2023MerhoehtBAnalysisWTR1-1d"),
    ("Funktion als Bestandsfunktion über Ableitung und Anfangswert begründen und Endwert bestätigen", "Analysis", "Rekonstruktion von Beständen",
     "Begründen, dass eine gegebene Funktion s den Bestand beschreibt, weil s' gleich der Rate ist und s zum Startzeitpunkt den Anfangsbestand hat, und einen Bestandswert (etwa null am Ende) nachrechnen.",
     "2023MerhoehtBAnalysisWTR1-1e"),
    ("Zunahme eines Bestands als Differenz der Bestandsfunktion und mittlere Änderungsrate im Zeitraum berechnen", "Analysis", "Rekonstruktion von Beständen",
     "Die Zunahme eines Bestands in einem Zeitraum als Differenz zweier Werte der Bestandsfunktion und die durchschnittliche Änderungsrate als Quotient mit der Zeitspanne berechnen.",
     "2023MerhoehtBAnalysisWTR1-1f"),
    ("Zeitpunkt gleichen Bestands am Ratengraphen über gleich große Flächen markieren und begründen", "Analysis", "Rekonstruktion von Beständen",
     "Am Graphen einer Änderungsrate den zweiten Zeitpunkt mit demselben Bestand markieren: die Fläche über der Achse bis zur Nullstelle und die Fläche unter der Achse danach müssen gleich groß sein; Begründung und Veranschaulichung in der Abbildung.",
     "2023MerhoehtBAnalysisWTR1-1g"),
    ("Grenzverhalten einer Potenzschar nach der Parität des Exponenten begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Für eine Schar mit Leitterm x^k das Verhalten für x → −∞ getrennt nach geradem und ungeradem k angeben und über den Leitterm begründen.",
     "2023MerhoehtBAnalysisWTR1-2a"),
    ("Aussage über den Ableitungsgraphen einer Schar als Tangente an den Scharfgraphen beurteilen", "Analysis", "Funktionsscharen und Ortskurven",
     "Beurteilen, für welche Parameterwerte der Graph der Ableitungsfunktion Tangente an den Scharfgraphen ist: Geradenfälle eingrenzen, Berührbedingung (gleicher Wert und gleiche Steigung) prüfen.",
     "2023MerhoehtBAnalysisWTR1-2c"),
    ("Trapez aus Funktions- und Ableitungswerten einer Schar begründen und Flächengleichheit für k und k + 1 nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Vier Punkte aus Werten von h_k und h_k' an zwei Stellen als Trapez (parallele Seiten über gleiche x-Koordinaten) begründen und den Flächeninhalt als Term in k mit (−1)^k so auswerten, dass die Gleichheit für gerades k und k + 1 folgt.",
     "2023MerhoehtBAnalysisWTR1-2d"),
    ("Nullstellen und Werte: Gesamtlänge aus einer Nullstelle und der Achsensymmetrie im Sachzusammenhang berechnen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus der Nullstelle einer Modellfunktion (Ende eines Bauteils) und der Symmetrie des Modells die Gesamtlänge mit Maßstab berechnen.",
     "2023MerhoehtBAnalysisWTR2-1a"),
    ("Transformation: Term und Intervall des an der y-Achse gespiegelten Graphen angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Für ein spiegelbildliches Bauteil den Term r(−x) und das gespiegelte Definitionsintervall angeben.",
     "2023MerhoehtBAnalysisWTR2-1b"),
    ("Fläche: Flächeninhalt zwischen Graph, x-Achse und senkrechter Gerade im Sachzusammenhang mit Maßstab berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Den Inhalt einer von Graph, Achse und einer senkrechten Geraden begrenzten Fläche als Integral berechnen und mit dem quadratischen Maßstab in die Realität umrechnen.",
     "2023MerhoehtBAnalysisWTR2-1e"),
    ("Gleichung für zwei Graphenpunkte mit festem horizontalem Abstand und Höhenunterschied aufstellen", "Analysis", "Gleichungen lösen",
     "Eine Gleichung der Form s(x) − s(x − d) = h angeben, deren Lösung die Stelle eines Graphenpunkts mit vorgegebenem horizontalem Abstand und Höhenunterschied zu einem zweiten Graphenpunkt ist (Maßstab beachten).",
     "2023MerhoehtBAnalysisWTR2-2b"),
    ("Nullstellen und Werte: Summe von Funktionswerten mit Maßstab als Gesamtlänge im Sachzusammenhang deuten", "Analysis", "Funktionsklassen und Eigenschaften",
     "Einen Summenterm über Funktionswerte an äquidistanten Stellen mit Maßstabsfaktor als Gesamtlänge gleichartiger Bauteile deuten und die Stellen, Werte und den Faktor begründen.",
     "2023MerhoehtBAnalysisWTR2-2c"),
    ("Länge eines Kreisbogens durch drei Punkte über den Winkel am Mittelpunkt berechnen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Für einen Kreis mit gegebenem Mittelpunkt durch drei Punkte den Radius und den halben Mittelpunktswinkel über den Tangens bestimmen und die Bogenlänge als Anteil des Umfangs mit Maßstab berechnen.",
     "2023MerhoehtBAnalysisWTR2-2e"),
    ("Verflechtung: Fehlenden Eintrag des Diagramms aus der Bedarfsmatrix angeben und deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen im Verflechtungsdiagramm fehlenden Bedarfswert aus der zugehörigen Matrix ablesen und als Mengeneinheiten je Mengeneinheit deuten.",
     "2023MerhoehtBAGLAA1WTR-1a"),
    ("Verflechtung: Nichtinvertierbarkeit der Gesamtmatrix im Sachzusammenhang deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Die Nichtinvertierbarkeit der Bedarfsmatrix als Aussage deuten, dass nicht jede Rohstoffmenge restlos in Endprodukte umgesetzt werden kann.",
     "2023MerhoehtBAGLAA1WTR-1c"),
    ("Verflechtung: Bedarf eines neuen Endprodukts an Zwischenprodukten aus der Produktgleichung der Matrizen ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus C = A · B mit einer neuen Spalte für ein weiteres Endprodukt eine Gleichung für die unbekannten Zwischenproduktbedarfe gewinnen und die verlangte Größe (etwa ihre Summe) ermitteln.",
     "2023MerhoehtBAGLAA1WTR-1d"),
    ("Verflechtung: Rohstoffbedarf in Abhängigkeit von einem Matrixparameter als Gerade darstellen und erläutern", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Für eine Bedarfsmatrix mit Parameter t den Bedarf eines Rohstoffs bei fester Produktion als linearen Term in t herleiten, grafisch darstellen und den Weg erläutern.",
     "2023MerhoehtBAGLAA1WTR-1e"),
    ("Innenwinkel eines Dreiecks über gleiche Seitenlängen als gleichseitig bestimmen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Die fehlenden Innenwinkel eines Dreiecks bestimmen, indem über die Beträge der Seitenvektoren die Gleichseitigkeit nachgewiesen wird.",
     "2023MerhoehtBAGLAA1WTR-2a"),
    ("Ebene Figur: Eckpunkt eines flächen- und umfangsgleichen Dreiecks über eine Parallelverschiebung angeben", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Einen Punkt T so angeben, dass das Dreieck OTQ zu OPQ flächen- und umfangsgleich ist, über die Ergänzung zum Parallelogramm (OT = PQ).",
     "2023MerhoehtBAGLAA1WTR-2b"),
    ("Ebene Figur: Flächengleichheit zweier Dreiecke mit gemeinsamer Seite über gleiche Höhen an einer Skizze begründen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Ohne Rechnung an einer Skizze begründen, dass zwei Dreiecke mit gemeinsamer Seite gleichen Flächeninhalt haben, weil die Höhen auf diese Seite gleich lang sind (dritter Punkt aus einer Vektorgleichung).",
     "2023MerhoehtBAGLAA1WTR-2c"),
    ("Ebene Figur: Flächeninhalt eines Rechtecks aus Kantenlängen berechnen und rechten Winkel zweier Flächen prüfen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Flächeninhalt eines Rechtecks im Raum aus zwei Kantenlängen (ein Eckpunkt ergänzt) berechnen und über das Skalarprodukt zweier Kanten prüfen, ob zwei Flächen einen rechten Winkel einschließen.",
     "2023MerhoehtBAGLAA2WTR1-1a"),
    ("Abstand einer vertikalen Fläche zu einer Achse über den Mittelpunkt der Oberkante begründen", "Analytische Geometrie", "Abstände",
     "Begründen, dass der Abstand einer vertikalen Fläche zu einer vertikalen Achse gleich dem Abstand des Mittelpunkts ihrer Oberkante ist, über die Symmetrie der Endpunkte zur Achse und die Vertikalität.",
     "2023MerhoehtBAGLAA2WTR1-1c"),
    ("Neigungswinkel einer Strecke gegen die Horizontale über ihre Projektion berechnen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Den Winkel einer Sichtlinie oder Strecke gegenüber der Horizontalen als Winkel zwischen ihrem Richtungsvektor und dessen Projektion in die Grundebene berechnen.",
     "2023MerhoehtBAGLAA2WTR1-1d"),
    ("Rechenweg für den Schnittpunkt einer Geraden mit einer Ebene durch drei Punkte beschreiben", "Analytische Geometrie", "Schnittmengen",
     "Beschreiben, wie ein Punkt als Schnittpunkt einer Kantengeraden mit einer durch drei Punkte gegebenen Ebene über das Gleichsetzen der Parameterformen berechnet wird.",
     "2023MerhoehtBAGLAA2WTR1-1e"),
    ("Achsenparallele Ebene einer Bewegung aus der Parameterdarstellung angeben", "Analytische Geometrie", "Ebenen",
     "Aus einer Bewegungsgleichung mit konstanter Koordinate die Ebene der Bewegung als achsenparallele Ebene beschreiben und ihre Gleichung angeben.",
     "2023MerhoehtBAGLAA2WTR1-1f"),
    ("Punkt: Lage eines bewegten Punktes gegenüber einer Mauer über Zeitpunkt und Höhe untersuchen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Aus einer Bewegungsgleichung den Zeitpunkt des Erreichens einer Ebene bestimmen und über die Höhe zu diesem Zeitpunkt entscheiden, ob ein Hindernis getroffen wird.",
     "2023MerhoehtBAGLAA2WTR1-1g"),
    ("Ebene Figur: Flächenterm eines Dreiecks als Quadrat minus Randdreiecke in der Abbildung veranschaulichen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Einen vorgegebenen Flächenterm (umbeschriebenes Quadrat minus rechtwinklige Eckdreiecke) durch Eintragungen in die Abbildung des Körpers veranschaulichen.",
     "2023MerhoehtBAGLAA2WTR2-1c"),
    ("Körper: Volumen aus Prisma und aufgesetzter Pyramide berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Das Volumen eines Körpers mit ebener Grundfläche und schräger Deckfläche als Summe aus einem geraden Prisma und einer Pyramide berechnen.",
     "2023MerhoehtBAGLAA2WTR2-1d"),
    ("Parameterbereich, in dem eine Ebenenschar dieselben Kanten eines Körpers schneidet, bestimmen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Für eine Ebenenschar durch eine Achse den größten Parameterbereich bestimmen, in dem die Ebenen dieselben Kanten eines Körpers schneiden, über die Parameterwerte, bei denen die Ebene durch Eckpunkte läuft.",
     "2023MerhoehtBAGLAA2WTR2-1e"),
    ("Dreieck: Koordinate eines Punktes auf einer Kante für einen rechten Winkel über das Skalarprodukt berechnen", "Analytische Geometrie", "Orthogonalität",
     "Die unbekannte Koordinate eines Punktes auf einer Kante so berechnen, dass ein Dreieck dort einen rechten Winkel hat (Skalarprodukt der Schenkelvektoren null, quadratische Gleichung, Bereich prüfen).",
     "2023MerhoehtBAGLAA2WTR2-1f"),
    ("Aufgabenstellung zu einer Drehung um eine Kante aus Lotfußpunkt und Rechenweg formulieren", "Analytische Geometrie", "Abstände",
     "Einen Rechenweg aus Lotfußpunkt auf eine Kante und Verschiebung um den Abstand in Achsenrichtung als Drehung eines Eckpunkts deuten, eine passende Aufgabenstellung formulieren und den Lotfußpunkt benennen.",
     "2023MerhoehtBAGLAA2WTR2-1g"),
    ("Wahrscheinlichkeit für mehrere Wiederholungen ohne Abbruch als Potenz berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit, dass ein Abbruchereignis in n Wiederholungen nicht eintritt, als Potenz der Gegenwahrscheinlichkeit berechnen.",
     "2023MerhoehtBStochastikWTR1-3a"),
    ("Erwartungswert einer weiteren Runde mit dem sicheren Betrag vergleichen und eine Empfehlung begründen", "Stochastik", "Kenngrößen von Verteilungen",
     "Den Erwartungswert der Auszahlung bei einer weiteren Spielrunde berechnen, mit dem sicheren Betrag bei Abbruch vergleichen und daraus eine Empfehlung begründen.",
     "2023MerhoehtBStochastikWTR1-3b"),
    ("Aussage über gleiche Erwartungswerte aufeinanderfolgender Parameterwerte über eine Gleichung beurteilen", "Stochastik", "Kenngrößen von Verteilungen",
     "Eine Aussage über gleiche Erwartungswerte für aufeinanderfolgende n beurteilen, indem E(n) = E(n + 1) gelöst und die Eindeutigkeit der Lösung genutzt wird.",
     "2023MerhoehtBStochastikWTR1-3c"),
    ("Obere Grenze eines Konfidenzintervalls über den Stichprobenanteil begründen und Verträglichkeit einer Annahme beschreiben", "Stochastik", "Konfidenzintervalle",
     "Aus der Lage des Stichprobenanteils im Konfidenzintervall eine Aussage über eine Intervallgrenze begründen und beschreiben, ob eine Annahme über p mit dem Intervall verträglich ist.",
     "2023MerhoehtBStochastikWTR1-4a"),
    ("Kleinsten Stichprobenumfang für die Unverträglichkeit eines Anteils mit einer Annahme über die Näherungsformel ermitteln", "Stochastik", "Konfidenzintervalle",
     "Den kleinsten Stichprobenumfang ermitteln, ab dem ein beobachteter Anteil nicht mehr mit einer Annahme p verträglich ist, über |h − p| > 1,96 · √(p(1 − p)/n).",
     "2023MerhoehtBStochastikWTR1-4b"),
    ("Anzahlvergleich zweier Teilgruppen über Pfadwahrscheinlichkeiten nachweisen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Nachweisen, welche von zwei Teilgruppen größer ist, indem die zugehörigen Pfadwahrscheinlichkeiten als Anteile an der Gesamtgruppe verglichen werden.",
     "2023MerhoehtBStochastikWTR2-1b"),
    ("Anteil für stochastische Unabhängigkeit ohne Rechnung angeben und begründen", "Stochastik", "Unabhängigkeit",
     "Den Wert eines bedingten Anteils angeben, für den zwei Ereignisse unabhängig sind, und ohne Rechnung über die Gleichheit der bedingten Anteile begründen.",
     "2023MerhoehtBStochastikWTR2-1c"),
    ("Restwahrscheinlichkeit und Erwartungswert eines Teilgewinns aus dem Gesamterwartungswert bestimmen", "Stochastik", "Kenngrößen von Verteilungen",
     "Die Wahrscheinlichkeit des verbleibenden Ausgangs als Gegenwahrscheinlichkeit nachweisen und aus dem bekannten Gesamterwartungswert den Erwartungswert des zugehörigen Teilgewinns über eine Gleichung bestimmen.",
     "2023MerhoehtBStochastikWTR2-2a"),
    ("Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln", "Stochastik", "Binomialverteilung",
     "Das kleinste ganzzahlige c ermitteln, für das P(μ − c ≤ X ≤ μ + c) eine vorgegebene Schranke erreicht, mit Nachbarwerten am Rechner.",
     "2023MerhoehtBStochastikWTR2-2b"),
    ("Nutzen eines größeren Stichprobenumfangs über den Fehler zweiter Art an den Gütekurven begründen", "Stochastik", "Hypothesentests",
     "Anhand der Graphen der Ablehnwahrscheinlichkeit für zwei Stichprobenumfänge begründen, dass der größere Umfang den Fehler zweiter Art verkleinert, und die Bedingung nennen, unter der er sich trotz höherer Kosten lohnt.",
     "2023MerhoehtBStochastikWTR2-2c"),
    ("Aufgabenstellung zu einer Potenz der Gegenwahrscheinlichkeit formulieren und Ansatz erläutern", "Stochastik", "Binomialverteilung",
     "Zu einer Rechnung der Form (1 − p)ⁿ eine passende Aufgabenstellung im Sachzusammenhang formulieren und den Ansatz (Gegenwahrscheinlichkeit, n unabhängige Wiederholungen) erläutern.",
     "2023MerhoehtBStochastikWTR3-1a"),
    ("Mindestanzahl aus einer Erwartungswertbedingung n · p > c ermitteln", "Stochastik", "Kenngrößen von Verteilungen",
     "Die kleinste Anzahl n ermitteln, für die der Erwartungswert n · p eine vorgegebene Schranke überschreitet (Ungleichung lösen, aufrunden).",
     "2023MerhoehtBStochastikWTR3-1b"),
    ("Fehlerwahrscheinlichkeit einer Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden", "Stochastik", "Binomialverteilung",
     "Die Wahrscheinlichkeit, dass eine Verpackungseinheit fehlerhaft ist, über eine Binomialverteilung berechnen und mit ihr als p die Wahrscheinlichkeit für eine Anzahl fehlerhafter Einheiten in einer Lieferung bestimmen (Anteilsbedingung in eine Anzahl übersetzen).",
     "2023MerhoehtBStochastikWTR3-1c"),
    ("Eignung der Normalverteilung trotz negativer Werte im Definitionsbereich begründen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Begründen, dass die Normalverteilung für eine nichtnegative Größe sinnvoll ist, weil die Wahrscheinlichkeit negativer Werte vernachlässigbar klein ist.",
     "2023MerhoehtBStochastikWTR3-2b"),
    ("Dichtefunktionen zu verschobenem Erwartungswert und kleinerer Standardabweichung skizzieren und Wirkung auf eine Wahrscheinlichkeit begründen", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Zu zwei Änderungsvorschlägen (größeres μ bzw. kleineres σ) je eine Dichtefunktion in die Abbildung skizzieren und über die Fläche unter der Dichte begründen, dass eine Unterschreitungswahrscheinlichkeit sinkt.",
     "2023MerhoehtBStochastikWTR3-2c"),
    ("Kleinstes n, für das die Wahrscheinlichkeit lauter verschiedener Ergebnisse unter eine Schranke fällt, ermitteln", "Stochastik", "Kombinatorik",
     "Die Wahrscheinlichkeit, dass n zufällige Auswahlen aus n Möglichkeiten alle verschieden sind, als n!/nⁿ ansetzen und das kleinste n ermitteln, für das sie eine Schranke unterschreitet.",
     "2023MerhoehtBStochastikWTR3-3"),
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
