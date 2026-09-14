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
    "stapel": "2018-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2018MgrundlegendAAnalysis11": 5,
        "2018MgrundlegendAAnalysis12": 5,
        "2018MgrundlegendAAnalysis2": 5,
        "2018MgrundlegendAAGLAA111": 5,
        "2018MgrundlegendAAGLAA112": 5,
        "2018MgrundlegendAAGLAA12": 5,
        "2018MgrundlegendAAGLAA211": 5,
        "2018MgrundlegendAAGLAA212": 5,
        "2018MgrundlegendAAGLAA22": 5,
        "2018MgrundlegendAStochastik11": 5,
        "2018MgrundlegendAStochastik12": 5,
        "2018MgrundlegendAStochastik2": 5,
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

# ---- Analysis 1.1: 2/x² + 1
row("2018MgrundlegendAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Graph einer gestreckten und verschobenen Potenzfunktion skizzieren", typ_neben="",
    stichwoerter="Graph von 1/x² mit Faktor 2 gestreckt und um 1 nach oben verschoben|Polstelle bei 0, Asymptote y = 1|achsensymmetrisch, nur Werte über 1",
    voraussetzungen="Graph von 1/x²|Streckung und Verschiebung|Asymptote und Pol",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 2/x² + 1 in IR ohne 0",
    gesucht="Skizze des Graphen von f",
    verfahren="Graph von 1/x² transformieren, Asymptote und Pol beachten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="zwei achsensymmetrische Äste über der Geraden y = 1, an der y-Achse gegen +∞, für |x| → ∞ gegen 1; Skizze (amtlich)",
    zwischenergebnis="f(1) = f(−1) = 3, f(2) = 1,5",
    niveau_geschaetzt="II",
    fehlerquelle="Asymptote y = 0 statt y = 1 zeichnen",
    bemerkung="Standardbezug: K4 II. Amtlich. Kein Koordinatensystem vorgegeben; Pol, Asymptote und Symmetrie sind aus dem Term zu erkennen, II.")

row("2018MgrundlegendAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph und waagerechter Gerade über einem Intervall berechnen", typ_neben="",
    stichwoerter="f(x) − 1 = 2/x²|Integral von 1 bis 2 über 2/x² dx = [−2/x] von 1 bis 2 = −1 + 2 = 1",
    voraussetzungen="Differenz zur Geraden y = 1|Stammfunktion von 2/x²|Grenzen 1 und 2",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 2/x² + 1; Flächenstück zwischen Graph, y = 1, x = 1 und x = 2",
    gesucht="Inhalt dieses Flächenstücks",
    verfahren="Integral über f(x) − 1 von 1 bis 2",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Integral von 1 bis 2 über 2/x² dx = [−2/x] von 1 bis 2 = 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Stammfunktion von x⁻² als −x⁻¹ ohne Faktor 2 oder mit falschem Vorzeichen",
    bemerkung="Standardbezug: K2 I, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 1.2: 3 − 2 sin x
row("2018MgrundlegendAAnalysis12", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen", typ_neben="",
    stichwoerter="f'(x) = −2 cos x|f'(0) = −2, f(0) = 3|y = −2x + 3",
    voraussetzungen="Ableitung von sin|Tangentengleichung aus Steigung und Punkt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3 − 2 sin x in IR; Punkt (0 | f(0))",
    gesucht="Gleichung der Tangente in diesem Punkt",
    verfahren="f' bilden, f'(0) und f(0) einsetzen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −2 cos x, f'(0) = −2, f(0) = 3; damit y = −2x + 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen der Ableitung (−2 cos x)",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-A).")

row("2018MgrundlegendAAnalysis12", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Wertebereich einer gestreckten und verschobenen Sinusfunktion angeben", typ_neben="",
    stichwoerter="sin x zwischen −1 und 1|−2 sin x zwischen −2 und 2|3 − 2 sin x zwischen 1 und 5|[1; 5]",
    voraussetzungen="Wertebereich von sin|Wirkung von Faktor und Verschiebung",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3 − 2 sin x in IR",
    gesucht="Wertebereich von f",
    verfahren="Wertebereich von sin durch Faktor −2 und Verschiebung 3 transformieren",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="[1; 5] (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="[−5; −1] durch falsches Vorzeichen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Transformation: Wertemenge einer transformierten Funktion begründen“ (2026-ea-A) getrennt: dort begründen, hier angeben.")

# ---- Analysis 2: Zuflussrate
row("2018MgrundlegendAAnalysis2", "a", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zunahme eines Bestands aus dem Vorzeichen der Rate begründen", typ_neben="",
    stichwoerter="Volumen nimmt zu, solange die Zuflussrate positiv ist|f(t) = −t(t − 4): Parabel nach unten mit Nullstellen 0 und 4|f(t) > 0 für 0 < t < 4",
    voraussetzungen="Rate als Ableitung des Bestands|Vorzeichen einer Parabel zwischen den Nullstellen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Behälter/Zufluss", textumfang="mittel",
    gegeben="Behälter mit 2 Litern zu Beginn; Zuflussrate f(t) = −t · (t − 4) in Litern je Stunde für 0 ≤ t ≤ 5",
    gesucht="Begründung, dass das Volumen in den ersten vier Stunden durchgehend zunimmt",
    verfahren="Zunahme auf positive Rate zurückführen, Vorzeichen von f auf (0; 4) über die Nullstellen",
    schritte="2", zahlenraum="ganz", einheiten="Liter|Stunden", abhaengig_von="",
    ergebnis="der Graph von f ist eine nach unten geöffnete Parabel, die bei t = 0 und t = 4 die t-Achse schneidet, d. h. es gilt f(t) > 0 für 0 < t < 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="f als Volumen statt als Rate lesen und Monotonie von f untersuchen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (e) Zunahme des Bestands aus dem Vorzeichen der Rate deuten, verkettet mit dem Vorzeichennachweis der Parabel.")

row("2018MgrundlegendAAnalysis2", "b", seite="1", punkte="2", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Gleichung für den Zeitpunkt eines Bestandswerts über ein Integral der Rate angeben", typ_neben="",
    stichwoerter="Volumen zur Zeit t: 2 + Integral von 0 bis t über f(x) dx|Gleichung 2 + Integral von 0 bis t über f(x) dx = 7",
    voraussetzungen="Bestand als Anfangswert plus Integral der Rate|variable obere Grenze",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Behälter/Zufluss", textumfang="mittel",
    gegeben="Anfangsvolumen 2 Liter, Rate f(t) = −t · (t − 4)",
    gesucht="Gleichung für die Zeit t, nach der der Behälter 7 Liter enthält",
    verfahren="Anfangsbestand plus Integral der Rate bis t gleich 7 setzen",
    schritte="1", zahlenraum="ganz", einheiten="Liter|Stunden", abhaengig_von="",
    ergebnis="2 + Integral von 0 bis t über f(x) dx = 7 (amtlich)",
    zwischenergebnis="t ≈ 1,92",
    niveau_geschaetzt="III",
    fehlerquelle="Anfangsbestand 2 vergessen oder f(t) = 7 ansetzen",
    bemerkung="Standardbezug: K2 II, K3 III, K5 II. Amtlich, eigene Rechnung bestätigt (Lösung der Gleichung). Eichregel: (a) „enthält sieben Liter“ in eine Gleichung mit Integral und variabler Grenze übersetzen. Vom Typ „Term für einen Bestand aus einer Rate über ein Integral angeben“ (2021-ea-A) getrennt: dort Term, hier Gleichung mit Bedingung.")

# ---- AG/LA (A1) 1.1: inverse Matrix, Matrixformate
row("2018MgrundlegendAAGLAA111", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Inverse Matrix über ein Gleichungssystem aus A · B = E bestimmen", typ_neben="",
    stichwoerter="A · B = ((7a + 4c; 7b + 4d), (2a; 2b)) = E|2a = 0, 2b = 1, 7a + 4c = 1, 7b + 4d = 0|a = 0, b = 1/2, c = 1/4, d = −7/8",
    voraussetzungen="Matrixprodukt mit Platzhaltern|Einträge mit E vergleichen|Gleichungssystem lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="A = ((7; 4), (2; 0)), B = ((a; b), (c; d)); A · B = E",
    gesucht="Werte von a, b, c, d",
    verfahren="Produkt ausrechnen, vier Gleichungen lösen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="((7; 4), (2; 0)) · ((a; b), (c; d)) = ((7a + 4c; 7b + 4d), (2a; 2b)) = ((1; 0), (0; 1)) ⇔ a = 0 ∧ b = 1/2 ∧ c = 1/4 ∧ d = −7/8 (amtlich)",
    zwischenergebnis="B = A⁻¹",
    niveau_geschaetzt="II",
    fehlerquelle="Produkt B · A statt A · B ansetzen (hier gleiches Ergebnis, aber falsche Zuordnung der Gleichungen)",
    bemerkung="Standardbezug: K2 I, K5 II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Matrizenalgebra: Einträge der inversen Matrix mit Platzhaltern angeben“ (2020-ga-A) getrennt: dort Kehrwerte in vorgegebener Form, hier vier Unbekannte über ein Gleichungssystem; Abgleich prüfen. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2018MgrundlegendAAGLAA111", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Mögliche Formate einer Matrix aus der Bildbarkeit eines Produkts beschreiben", typ_neben="",
    stichwoerter="C · A bildbar heißt Spaltenzahl von C gleich Zeilenzahl von A, also 2|A · C nicht bildbar heißt Zeilenzahl von C ungleich 2|C hat 2 Spalten und 1 oder mindestens 3 Zeilen",
    voraussetzungen="Bedingung für die Bildbarkeit eines Matrixprodukts (Spalten links gleich Zeilen rechts)",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A ist eine 2×2-Matrix; für C ist C · A bildbar, A · C nicht",
    gesucht="alle möglichen Formen von C",
    verfahren="Formatbedingung für beide Produkte auswerten",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Anzahl der Spalten von C ist 2, die Anzahl der Zeilen 1 oder mindestens 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur „C ist keine 2×2-Matrix“ antworten",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A1) 1.2: Population J, H, E
row("2018MgrundlegendAAGLAA112", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Eintrag 0,05: Anteil der Jungtiere, die heranwachsend werden|1 − 0,05 = 0,95|95 % überleben das erste Jahr nicht",
    voraussetzungen="Spalte J der Matrix lesen|Gegenanteil",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Tiere/Population", textumfang="lang",
    gegeben="Vektor (J; H; E) für Jungtiere, heranwachsende und erwachsene Tiere; P = ((0; 0; 200), (0,05; 0; 0), (0; 0,1; 0)) je Jahr",
    gesucht="Prozentsatz der Jungtiere, die das erste Lebensjahr nicht überleben",
    verfahren="Übergangsanteil 0,05 ablesen, Gegenanteil bilden",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="%", abhaengig_von="",
    ergebnis="95 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="5 % angeben (Überlebende statt Nichtüberlebende)",
    bemerkung="Standardbezug: K3 I, K4 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2022-ea-A; hier Gegenanteil zum Eintrag). Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2018MgrundlegendAAGLAA112", "b", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Quadrat der Übergangsmatrix berechnen und M² · v als Zustand nach zwei Schritten deuten", typ_neben="",
    stichwoerter="P² = ((0; 20; 0), (0; 0; 10), (0,005; 0; 0))|P² · v_n ist die Zusammensetzung im Jahr n + 2",
    voraussetzungen="Matrixprodukt|Potenz der Übergangsmatrix als Mehrfachschritt",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Beschreiben Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Tiere/Population", textumfang="kurz",
    gegeben="P = ((0; 0; 200), (0,05; 0; 0), (0; 0,1; 0)); v_(n+1) = P · v_n",
    gesucht="P² und Bedeutung von P² · v_n",
    verfahren="P · P ausrechnen, Produkt mit v_n als zwei Jahresschritte deuten",
    schritte="2", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="P² = ((0; 20; 0), (0; 0; 10), (0,005; 0; 0)); mit dem Term P² · v_n lässt sich die Zusammensetzung der Population im Jahr n + 2 berechnen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Einträge elementweise quadrieren",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Übergangsprozess: Eintrag von M² berechnen und Zeile von M² im Sachzusammenhang deuten“ getrennt: dort ein Eintrag und eine Zeile, hier die ganze Matrix und der Term M² · v. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2018MgrundlegendAAGLAA112", "c", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Potenz der Übergangsmatrix gleich Einheitsmatrix als Zyklus deuten", typ_neben="",
    stichwoerter="P³ = E|P³ · v_n = v_n|Zusammensetzung wiederholt sich alle drei Jahre",
    voraussetzungen="Einheitsmatrix lässt Vektoren unverändert|Potenz als drei Jahresschritte",
    format="Kurzantwort", operator="Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Tiere/Population", textumfang="kurz",
    gegeben="P³ = E (Einheitsmatrix)",
    gesucht="Deutung im Sachzusammenhang",
    verfahren="P³ · v = v als Rückkehr zur Ausgangszusammensetzung nach drei Jahren deuten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2018MgrundlegendAAGLAA112-b",
    ergebnis="die Zusammensetzung der Population wiederholt sich im Abstand von drei Jahren (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="„die Population bleibt konstant“ (auch die Zwischenjahre) behaupten",
    bemerkung="Standardbezug: K3 II, K4 I, K6 II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Langfristige Entwicklung aus M³ als Vielfachem der Einheitsmatrix durch Fallunterscheidung beschreiben“ (2019-ga-A) getrennt: dort Parameterfälle, hier nur der Zyklus. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A1) 2: binomische Formel für Matrizen
row("2018MgrundlegendAAGLAA12", "a", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Parameter aus der Gültigkeit der binomischen Formel für zwei Matrizen bestimmen", typ_neben="",
    stichwoerter="A + B = ((1; 2), (0; b))|(A + B)² = ((1; 2 + 2b), (0; b²))|Vergleich mit ((1; 3 + 3b), (0; b²)): 2 + 2b = 3 + 3b ⇔ b = −1",
    voraussetzungen="(A + B)² als Produkt (A + B) · (A + B) ausrechnen|Einträge vergleichen|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="A = ((1; 1), (0; 0)), B = ((0; 1), (0; b)); A² + 2 · A · B + B² = ((1; 3 + 3b), (0; b²)) vorgegeben; (A + B)² = A² + 2 · A · B + B² gilt nur für einen Wert von b",
    gesucht="dieser Wert von b",
    verfahren="(A + B)² ausrechnen und mit dem vorgegebenen Term vergleichen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(A + B)² = ((1; 2), (0; b)) · ((1; 2), (0; b)) = ((1; 2 + 2b), (0; b²)) = ((1; 3 + 3b), (0; b²)) ⇔ 2 + 2b = 3 + 3b ⇔ b = −1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="(A + B)² über die binomische Formel berechnen – dann ist die Gleichung trivial und b bleibt offen",
    bemerkung="Standardbezug: K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Geschätzt II: die rechte Seite ist vorgegeben, es bleibt Ausmultiplizieren und Eintragsvergleich ohne zu findende Deutung; amtlich III über K2. Vom Typ „Matrizenalgebra: Alle mit einer Matrix vertauschbaren Matrizen ermitteln“ (2025-ea-A, 2021-ea-A) getrennt: dort allgemeiner Ansatz mit Lösungsmenge, hier ein Parameter und Vergleich mit vorgegebenem Term. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2018MgrundlegendAAGLAA12", "b", seite="1", punkte="2", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Quadrat einer Summe zweier Matrizen mit C · D = −D · C vereinfachen", typ_neben="",
    stichwoerter="(C + D)² = (C + D) · (C + D) = C² + C · D + D · C + D²|C · D + D · C = 0|= C² + D²",
    voraussetzungen="Distributivgesetz ohne Kommutativität|Bedingung C · D = −D · C einsetzen",
    format="Begründung", operator="Stellen Sie dar|Vereinfachen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="2×2-Matrizen C und D mit C · D = −D · C",
    gesucht="(C + D)² als Summe dargestellt und so weit wie möglich vereinfacht",
    verfahren="Produkt ausmultiplizieren, Mittelterme mit der Bedingung aufheben",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(C + D)² = (C + D) · (C + D) = C² + C · D + D · C + D² = C² + D² (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="binomische Formel mit 2 · C · D anwenden",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt (Beispielpaar). Eichregel: (c) allgemeiner Nachweis, bei dem die Beziehung C · D + D · C = 0 aus der Voraussetzung hergeleitet und mit dem nichtkommutativen Ausmultiplizieren verkettet wird. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A2) 1.1: Punkte A, B, C mit OC = 2 OA
row("2018MgrundlegendAAGLAA211", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Länge einer Strecke aus einer Vektorbeziehung der Ortsvektoren berechnen", typ_neben="",
    stichwoerter="AC = OC − OA = OA|AC| = |OA| = √(1 + 1 + 1) = √3",
    voraussetzungen="Verbindungsvektor aus Ortsvektoren|Betrag",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(1 | 1 | −1), B(3 | −5 | 2), C mit OC = 2 · OA",
    gesucht="Länge der Strecke AC",
    verfahren="AC = OA, Betrag berechnen",
    schritte="2", zahlenraum="ganz|Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="|AC| = |OA| = √(1 + 1 + 1) = √3 (amtlich)",
    zwischenergebnis="C(2 | 2 | −2)",
    niveau_geschaetzt="I",
    fehlerquelle="|OC| = 2√3 als Streckenlänge nehmen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2018MgrundlegendAAGLAA211", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Eindeutigkeit einer Ebene durch vier Punkte über die Kollinearität dreier Punkte begründen", typ_neben="",
    stichwoerter="OC = 2 · OA: O, A, C auf einer Geraden|OB ≠ λ · OA für alle λ: B nicht auf dieser Geraden|Gerade und Punkt außerhalb legen genau eine Ebene fest",
    voraussetzungen="Kollinearität aus Vielfachheit der Ortsvektoren|Punkt außerhalb einer Geraden prüfen|Ebene durch Gerade und Punkt eindeutig",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(1 | 1 | −1), B(3 | −5 | 2), C mit OC = 2 · OA, Koordinatenursprung O",
    gesucht="Begründung, dass genau eine Ebene A, B, C und O enthält",
    verfahren="O, A, C als kollinear erkennen, B als nicht kollinear nachweisen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="da OC = 2 · OA gilt, liegen A, C und der Koordinatenursprung auf einer Geraden; wegen OB ≠ λ · OA für alle λ ∈ IR enthält diese Gerade nicht den Punkt B (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Ebene durch A, B, C aufstellen und O nicht einbeziehen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Die Kollinearität von O, A, C ist mit OC = 2 · OA praktisch vorgegeben, dazu eine Prüfung: II.")

# ---- AG/LA (A2) 1.2: Pyramide
PYR_SKIZZE = ("Koordinatensystem x1 (waagerecht, −1 bis 4) und x2 (senkrecht, −3 bis 2) mit Gitter; B' als Kreuz bei (2; 1), "
              "A' als Kreuz bei (3; −2); C' und S' nicht eingezeichnet")
row("2018MgrundlegendAAGLAA212", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Parallelität der Grundfläche einer Pyramide zu einer Koordinatenebene begründen und Höhe angeben", typ_neben="",
    stichwoerter="x3-Koordinaten von A, B, C alle 1|Grundfläche in der Ebene x3 = 1, parallel zur x1x2-Ebene|Höhe 5 − 1 = 4",
    voraussetzungen="gleiche dritte Koordinate heißt Ebene parallel zur x1x2-Ebene|Höhe als Koordinatendifferenz",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Pyramide mit Grundfläche A(3 | −2 | 1), B(2 | 1 | 1), C(0 | −0,5 | 1) und Spitze S(1 | −1,5 | 5)",
    gesucht="Begründung der Parallelität der Grundfläche zur x1x2-Ebene und Höhe der Pyramide",
    verfahren="dritte Koordinaten vergleichen, Höhe als Differenz",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="die x3-Koordinaten von A, B und C stimmen überein; die Höhe der Pyramide ist 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Höhe 5 statt 4",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2018MgrundlegendAAGLAA212", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Lage des Höhenfußpunkts einer Pyramide über die Projektion in die Grundflächenebene entscheiden", typ_neben="",
    stichwoerter="C' = (0; −0,5), S' = (1; −1,5) eintragen|Dreieck A'B'C' zeichnen|S' liegt außerhalb des Dreiecks, also Fußpunkt außerhalb der Grundfläche",
    voraussetzungen="Projektion parallel zur x3-Achse: erste beiden Koordinaten|Höhenfußpunkt hat die x1x2-Koordinaten von S|Lage eines Punktes zum Dreieck ablesen",
    format="Kurzantwort|Eintragen", operator="Entscheiden Sie", antwort="Text",
    material="Koordinatensystem", skizze=PYR_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Pyramide ABCS aus a; A' und B' (Projektionen in die x1x2-Ebene) in der Abbildung",
    gesucht="Entscheidung mithilfe der ergänzten Abbildung, ob der Höhenfußpunkt innerhalb oder außerhalb der Grundfläche liegt",
    verfahren="C' und S' eintragen, Dreieck A'B'C' zeichnen, Lage von S' ablesen",
    schritte="3", zahlenraum="ganz|dezimal|negativ", einheiten="", abhaengig_von="2018MgrundlegendAAGLAA212-a",
    ergebnis="der Fußpunkt der Höhe liegt außerhalb der Grundfläche (amtlich)",
    zwischenergebnis="S'(1 | −1,5) links unterhalb der Seite A'C'",
    niveau_geschaetzt="II",
    fehlerquelle="S selbst statt seiner Projektion S' betrachten",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt (baryzentrische Koordinaten). Vom Typ „Ebene Figur: Projektion eines Parallelogramms in eine Koordinatenebene einzeichnen“ getrennt: hier Entscheidung über den Höhenfußpunkt aus der Projektion.")

# ---- AG/LA (A2) 2: Dreiecke mit Parameter
row("2018MgrundlegendAAGLAA22", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Rechten Winkel eines Dreiecks mit Parameter nachweisen", typ_neben="",
    stichwoerter="BA = (2; 0; −4), BC_t = (2t; 0; t)|BA · BC_t = 4t − 4t = 0 für alle t",
    voraussetzungen="Verbindungsvektoren mit Parameter|Skalarprodukt identisch null",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(7 | 3 | 0), B(5 | 3 | 4), C_t(5 + 2t | 3 | 4 + t) mit t ≠ 0",
    gesucht="Nachweis, dass jedes Dreieck ABC_t bei B einen rechten Winkel hat",
    verfahren="Skalarprodukt der Schenkelvektoren bei B",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="BA · BC_t = (2; 0; −4) · (2t; 0; t) = 4t − 4t = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Vektor AC statt BC ansetzen",
    bemerkung="Standardbezug: K5 II. Amtlich, eigene Rechnung bestätigt. Geschätzt I wie beim gleichen Typ in 2026-ga-A (Identität mit mitgeführtem Parameter nachrechnen); amtlich II über K5. Typ wiederverwendet.")

row("2018MgrundlegendAAGLAA22", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Parameter aus der Gleichschenkligkeit eines Dreiecks berechnen", typ_neben="",
    stichwoerter="zwei gleiche Innenwinkel heißt gleichschenklig|bei rechtem Winkel in B nur |BA| = |BC_t| möglich|√20 = √(5t²) ⇔ t = ±2",
    voraussetzungen="gleiche Winkel als gleiche Schenkel deuten|rechter Winkel schließt die Basis als Schenkel aus|Beträge gleichsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Dreiecke ABC_t aus a, rechtwinklig bei B",
    gesucht="alle t, für die zwei Innenwinkel gleich groß sind",
    verfahren="Bedingung in |BA| = |BC_t| übersetzen und lösen",
    schritte="3", zahlenraum="ganz|Wurzel|negativ", einheiten="", abhaengig_von="2018MgrundlegendAAGLAA22-a",
    ergebnis="|BA| = |BC_t| ⇔ √20 = √(5t²) ⇔ t = −2 ∨ t = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur t = 2 angeben oder |AB| = |AC_t| ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „zwei Innenwinkel gleich groß“ erst in Gleichschenkligkeit und mit dem rechten Winkel aus a in |BA| = |BC_t| übersetzen. Typ wiederverwendet (2026-ga-A; dort ist die Gleichschenkligkeit wörtlich vorgegeben, II).")

# ---- Stochastik 1.1: acht Karten
row("2018MgrundlegendAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="2/8 · 1/7 = 1/28",
    voraussetzungen="Pfad ohne Zurücklegen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Karten", textumfang="mittel",
    gegeben="acht Karten, je zwei mit 1, 2, 3, 4; gemischt und nacheinander abgelegt",
    gesucht="Wahrscheinlichkeit, dass die beiden ersten Karten mit 1 beschriftet sind",
    verfahren="Produkt der beiden Zugwahrscheinlichkeiten",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="2/8 · 1/7 = 1/28 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="mit Zurücklegen rechnen (1/16)",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-A).")

row("2018MgrundlegendAStochastik11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit für spätestens den dritten Zug über das Gegenereignis berechnen", typ_neben="",
    stichwoerter="Gegenereignis: die ersten drei Karten ungerade|4/8 · 3/7 · 2/6 = 1/14|1 − 1/14 = 13/14",
    voraussetzungen="„spätestens die dritte“ als Gegenereignis „erste drei ungerade“|Pfad ohne Zurücklegen mit drei Zügen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Karten", textumfang="kurz",
    gegeben="acht Karten (vier gerade, vier ungerade), nacheinander aufgedeckt",
    gesucht="Wahrscheinlichkeit, dass spätestens die dritte Karte eine gerade Zahl trägt",
    verfahren="1 minus Wahrscheinlichkeit für drei ungerade Karten",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1 − 4/8 · 3/7 · 2/6 = 13/14 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="alle Pfade mit einer geraden Karte einzeln addieren und einen vergessen",
    bemerkung="Standardbezug: K2 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 1.2: Glücksrad A/B, Einsatz 4 Euro
row("2018MgrundlegendAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsgrößen und Verteilungen",
    typ="Mögliche Werte einer Auszahlung aus zweistufigen Spielregeln nachweisen", typ_neben="",
    stichwoerter="AA: 4 · 1/2 · 1/2 = 1|AB und BA: 4 · 1/2 · 2 = 4|BB: 4 · 2 · 2 = 16",
    voraussetzungen="vier Ergebnisfolgen|Halbieren und Verdoppeln nacheinander anwenden",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksspiel/Glücksrad", textumfang="lang",
    gegeben="Einsatz 4 Euro, zweimal drehen; A halbiert, B verdoppelt den Betrag; der Betrag nach dem zweiten Drehen wird ausgezahlt",
    gesucht="Nachweis, dass nur 1, 4 und 16 Euro ausgezahlt werden können",
    verfahren="alle vier Ergebnisfolgen durchrechnen",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="Euro", abhaengig_von="",
    ergebnis="AA: 4 · 1/2 · 1/2 = 1, AB: 4 · 1/2 · 2 = 4, BA: 4 · 2 · 1/2 = 4, BB: 4 · 2 · 2 = 16 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="AB und BA als verschiedene Beträge erwarten",
    bemerkung="Standardbezug: K5 I, K6 II. Amtlich, eigene Rechnung bestätigt.")

row("2018MgrundlegendAStochastik12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert der Auszahlung mit dem Einsatz vergleichen", typ_neben="",
    stichwoerter="E(X) = 4/9 · 1 + 4/9 · 4 + 1/9 · 16 = 4|gleich dem Einsatz 4 Euro|auf lange Sicht gleichen sich Einsätze und Auszahlungen aus",
    voraussetzungen="Erwartungswert aus der Tabelle|Vergleich mit dem Einsatz deuten",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Interpretieren Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle x = 1, 4, 16 mit P(X = x) = 4/9, 4/9, 1/9", kontext="Glücksspiel/Glücksrad", textumfang="mittel",
    gegeben="X Auszahlung in Euro mit P(X = 1) = 4/9, P(X = 4) = 4/9, P(X = 16) = 1/9; Einsatz 4 Euro",
    gesucht="Erwartungswert von X und Deutung unter Berücksichtigung des Einsatzes",
    verfahren="Erwartungswert berechnen, mit dem Einsatz vergleichen",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="Euro", abhaengig_von="",
    ergebnis="4/9 · 1 + 4/9 · 4 + 1/9 · 16 = 4; auf lange Sicht gleichen sich Einsätze und Auszahlungen aus (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Erwartungswert als Gewinn je Spiel deuten, ohne den Einsatz abzuziehen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ga-A). Reine Verkettung Erwartungswert und Vergleich mit dem Einsatz, nach der Liste II.")

# ---- Stochastik 2: Glücksrad blau, gelb, rot
row("2018MgrundlegendAStochastik2", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Sektorwinkel eines Glücksrads aus einer Wahrscheinlichkeitsbedingung berechnen", typ_neben="",
    stichwoerter="P(Gelb)² = 1/4 ⇔ P(Gelb) = 1/2|Mittelpunktswinkel 1/2 · 360° = 180°",
    voraussetzungen="Pfad zweimal Gelb als Quadrat|Wurzel ziehen|Anteil in Winkel umrechnen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel/Glücksrad", textumfang="mittel",
    gegeben="Glücksrad mit blauem, gelbem, rotem Sektor; P(Rot) = 1/3; P(zweimal Gelb bei zwei Drehungen) = 1/4",
    gesucht="Mittelpunktswinkel des gelben Sektors",
    verfahren="p² = 1/4 lösen, Winkel als Anteil von 360°",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="°", abhaengig_von="",
    ergebnis="die Wahrscheinlichkeit für „Gelb“ bei einmaligem Drehen beträgt 1/2, d. h. der Mittelpunktswinkel ist 180° groß (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="1/4 direkt als Anteil nehmen (90°)",
    bemerkung="Standardbezug: K2 II, K3 II, K6 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-A; dort quadratische Gleichung mit zwei Fällen, hier p² = 1/4).")

row("2018MgrundlegendAStochastik2", "b", seite="1", punkte="3", afb_amtlich="III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="1/9 = (1/3)² = P(zweimal Rot in einem Spiel)|Summe i = 0 bis 3 von (10 über i) · (1/9)^i · (8/9)^(10 − i): kumulierte Binomialwahrscheinlichkeit, n = 10, höchstens 3 Treffer|Zufallsexperiment: das Spiel wird zehnmal durchgeführt",
    voraussetzungen="1/9 als Quadrat von 1/3 erkennen|Binomialsumme als „höchstens 3 von 10“ lesen|Zufallsexperiment und Ereignis benennen",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksspiel/Glücksrad", textumfang="mittel",
    gegeben="Glücksrad mit P(Rot) = 1/3, Spiel mit zwei Drehungen; Term Summe i = 0 bis 3 von (10 über i) · (1/9)^i · (8/9)^(10 − i)",
    gesucht="ein Zufallsexperiment im Sachzusammenhang und das Ereignis, dessen Wahrscheinlichkeit der Term angibt",
    verfahren="1/9 als zweimal Rot in einem Spiel deuten, Binomialsumme als höchstens drei von zehn Spielen",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Zufallsexperiment: das Spiel wird zehnmal durchgeführt; Ereignis: „Bei höchstens drei Spielen wird zweimal ‚Rot‘ erzielt.“ (amtlich)",
    zwischenergebnis="Wert ≈ 0,98",
    niveau_geschaetzt="III",
    fehlerquelle="1/9 als Sektorwahrscheinlichkeit einer Farbe deuten",
    bemerkung="Standardbezug: K1 III, K3 III, K4 III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) zwei Deutungen verkettet – 1/9 als Wahrscheinlichkeit für zweimal Rot in einem Spiel und die Summe als kumulierte Binomialwahrscheinlichkeit über zehn Spiele. Typ wiederverwendet (zusammengezogener Typ).")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Transformation: Graph einer gestreckten und verschobenen Potenzfunktion skizzieren", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Den Graphen einer Funktion wie a/x^n + c ohne vorgegebenes Koordinatensystem skizzieren (Pol, Asymptote, "
     "Symmetrie aus dem Term erkennen).",
     "2018MgrundlegendAAnalysis11-a"),
    ("Fläche: Fläche zwischen Graph und waagerechter Gerade über einem Intervall berechnen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Inhalt der Fläche zwischen einem Graphen und einer waagerechten Geraden zwischen zwei senkrechten "
     "Geraden als Integral der Differenz berechnen.",
     "2018MgrundlegendAAnalysis11-b"),
    ("Transformation: Wertebereich einer gestreckten und verschobenen Sinusfunktion angeben", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Den Wertebereich einer Funktion a + b · sin x aus dem Wertebereich [−1; 1] der Sinusfunktion über Streckung "
     "und Verschiebung angeben.",
     "2018MgrundlegendAAnalysis12-b"),
    ("Zunahme eines Bestands aus dem Vorzeichen der Rate begründen", "Analysis", "Rekonstruktion von Beständen",
     "Begründen, dass ein Bestand in einem Zeitraum durchgehend zunimmt, weil die als Term gegebene Rate dort "
     "positiv ist (Rate als Ableitung des Bestands, Vorzeichen über Nullstellen).",
     "2018MgrundlegendAAnalysis2-a"),
    ("Gleichung für den Zeitpunkt eines Bestandswerts über ein Integral der Rate angeben", "Analysis",
     "Rekonstruktion von Beständen",
     "Eine Gleichung mit Integral und variabler oberer Grenze angeben, aus der sich der Zeitpunkt berechnen "
     "lässt, zu dem ein Bestand einen vorgegebenen Wert erreicht (Anfangsbestand plus Integral der Rate).",
     "2018MgrundlegendAAnalysis2-b"),
    ("Matrizenalgebra: Inverse Matrix über ein Gleichungssystem aus A · B = E bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Alle Einträge der Matrix B mit A · B = E bestimmen, indem das Produkt mit Platzhaltern ausgerechnet und das "
     "entstehende lineare Gleichungssystem gelöst wird.",
     "2018MgrundlegendAAGLAA111-a"),
    ("Matrizenalgebra: Mögliche Formate einer Matrix aus der Bildbarkeit eines Produkts beschreiben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Aus der Angabe, welche Produkte mit einer Matrix bildbar sind und welche nicht, alle möglichen Zeilen- und "
     "Spaltenzahlen der Matrix beschreiben.",
     "2018MgrundlegendAAGLAA111-b"),
    ("Übergangsprozess: Quadrat der Übergangsmatrix berechnen und M² · v als Zustand nach zwei Schritten deuten",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Das Quadrat einer Übergangsmatrix ausrechnen und den Term M² · v als Zusammensetzung nach zwei Schritten "
     "im Sachzusammenhang beschreiben.",
     "2018MgrundlegendAAGLAA112-b"),
    ("Übergangsprozess: Potenz der Übergangsmatrix gleich Einheitsmatrix als Zyklus deuten", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Eine Gleichung M^n = E im Sachzusammenhang deuten: die Zusammensetzung wiederholt sich nach n Schritten.",
     "2018MgrundlegendAAGLAA112-c"),
    ("Matrizenalgebra: Parameter aus der Gültigkeit der binomischen Formel für zwei Matrizen bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Den Parameterwert bestimmen, für den (A + B)² = A² + 2AB + B² gilt, indem (A + B)² als Produkt ausgerechnet "
     "und eintragsweise mit dem vorgegebenen Term verglichen wird.",
     "2018MgrundlegendAAGLAA12-a"),
    ("Matrizenalgebra: Quadrat einer Summe zweier Matrizen mit C · D = −D · C vereinfachen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "(C + D)² für Matrizen mit C · D = −D · C als Summe ausmultiplizieren (ohne Kommutativität) und mit der "
     "Voraussetzung zu C² + D² vereinfachen.",
     "2018MgrundlegendAAGLAA12-b"),
    ("Punkt: Länge einer Strecke aus einer Vektorbeziehung der Ortsvektoren berechnen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Die Länge einer Strecke berechnen, wenn ein Endpunkt nur über eine Beziehung der Ortsvektoren (etwa "
     "OC = 2 · OA) gegeben ist.",
     "2018MgrundlegendAAGLAA211-a"),
    ("Eindeutigkeit einer Ebene durch vier Punkte über die Kollinearität dreier Punkte begründen", "Analytische Geometrie",
     "Ebenen",
     "Begründen, dass genau eine Ebene vier gegebene Punkte enthält, wenn drei davon auf einer Geraden liegen und "
     "der vierte nicht (Vielfachheit der Ortsvektoren prüfen).",
     "2018MgrundlegendAAGLAA211-b"),
    ("Körper: Parallelität der Grundfläche einer Pyramide zu einer Koordinatenebene begründen und Höhe angeben",
     "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Aus übereinstimmenden dritten Koordinaten der Grundflächenecken die Parallelität zur Koordinatenebene "
     "begründen und die Höhe als Koordinatendifferenz zur Spitze angeben.",
     "2018MgrundlegendAAGLAA212-a"),
    ("Körper: Lage des Höhenfußpunkts einer Pyramide über die Projektion in die Grundflächenebene entscheiden",
     "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Grundfläche und Spitze einer Pyramide mit achsenparalleler Höhe in die Grundflächenebene projizieren, in "
     "eine Abbildung eintragen und ablesen, ob der Höhenfußpunkt innerhalb der Grundfläche liegt.",
     "2018MgrundlegendAAGLAA212-b"),
    ("Ziehen ohne Zurücklegen: Wahrscheinlichkeit für spätestens den dritten Zug über das Gegenereignis berechnen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die Wahrscheinlichkeit, dass ein Merkmal spätestens beim dritten Zug ohne Zurücklegen auftritt, über das "
     "Gegenereignis (drei Züge ohne das Merkmal) berechnen.",
     "2018MgrundlegendAStochastik11-b"),
    ("Mögliche Werte einer Auszahlung aus zweistufigen Spielregeln nachweisen", "Stochastik", "Zufallsgrößen und Verteilungen",
     "Alle möglichen Werte einer Auszahlung nachweisen, indem alle Ergebnisfolgen eines zweistufigen Spiels nach "
     "den Regeln durchgerechnet werden.",
     "2018MgrundlegendAStochastik12-a"),
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
