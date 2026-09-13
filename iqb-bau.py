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
    "stapel": "2022-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2022MgrundlegendAAnalysis11": 5,
        "2022MgrundlegendAAnalysis12": 5,
        "2022MgrundlegendAAnalysis13": 5,
        "2022MgrundlegendAAnalysis2": 5,
        "2022MgrundlegendAAGLAA11": 5,
        "2022MgrundlegendAAGLAA12": 5,
        "2022MgrundlegendAAGLAA211": 5,
        "2022MgrundlegendAAGLAA212": 5,
        "2022MgrundlegendAAGLAA213": 5,
        "2022MgrundlegendAAGLAA22": 5,
        "2022MgrundlegendAStochastik11": 5,
        "2022MgrundlegendAStochastik12": 5,
        "2022MgrundlegendAStochastik13": 5,
        "2022MgrundlegendAStochastik2": 5,
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
# niveau_geschaetzt nach der Deutungsliste v0.6; bei III nennt bemerkung den Eintrag.

# ---- Analysis 1.1: cos x + 1, Fläche unter der Hochpunktgeraden
COS_SKIZZE = ("Koordinatensystem ohne Gitter, x-Achse mit den Markierungen 0, π und 2π, y-Achse ohne Werte; "
              "Graph von cos x + 1 von etwa −π/2 bis 2,5π mit Hochpunkten über 0 und 2π und Tiefpunkt (π; 0); "
              "waagerechte Gerade g durch die Hochpunkte; grau markiert das Flächenstück zwischen g und dem "
              "Graphen von x = 0 bis x = 2π")
row("2022MgrundlegendAAnalysis11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Extrempunkte: Gerade durch die Hochpunkte einer Kosinusfunktion begründen", typ_neben="",
    stichwoerter="cos x ≤ 1, Maximum 2|alle Hochpunkte haben y = 2|g: y = 2",
    voraussetzungen="Wertebereich des Kosinus|Hochpunkte einer verschobenen Kosinusfunktion",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=COS_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = cos(x) + 1 in IR; Graph mit Gerade g durch die Hochpunkte in der Abbildung",
    gesucht="Begründung, dass g durch y = 2 dargestellt werden kann",
    verfahren="alle Hochpunkte haben die y-Koordinate 2, da der Kosinus höchstens 1 ist",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="alle Hochpunkte des Graphen von f haben die y-Koordinate 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="mit einem einzelnen Hochpunkt argumentieren statt mit allen",
    bemerkung="Standardbezug: K1 I, K6 I. Amtlich.")

row("2022MgrundlegendAAnalysis11", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph und Hochpunktgerade über eine Periode berechnen", typ_neben="",
    stichwoerter="Fläche zwischen g und Gf von 0 bis 2π|Integral über 2 − (cos x + 1) = 1 − cos x|[x − sin x] von 0 bis 2π = 2π|alternativ: Symmetrie, Rechteck 2 · π",
    voraussetzungen="Fläche zwischen zwei Graphen als Integral der Differenz|Stammfunktion von cos|Grenzen aus der Abbildung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=COS_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = cos(x) + 1, g: y = 2; grau markiertes Flächenstück zwischen g und dem Graphen von x = 0 bis x = 2π",
    gesucht="Inhalt der grau markierten Fläche",
    verfahren="Integral von 0 bis 2π über 2 − f(x) dx oder Ergänzung zum Rechteck über Symmetrie",
    schritte="3", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="2022MgrundlegendAAnalysis11-a",
    ergebnis="der Inhalt der grau markierten Fläche stimmt mit dem Inhalt der Fläche überein, die g mit der x-Achse und den Geraden x = 0 und x = π einschließt; der gesuchte Inhalt beträgt 2 · π (amtlich)",
    zwischenergebnis="Integral von 0 bis 2π über (1 − cos x) dx = 2π",
    niveau_geschaetzt="II",
    fehlerquelle="Integral über f statt über 2 − f bilden (Fläche unter dem Graphen, ebenfalls 2π, aber falsche Fläche)",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt (Integral der Differenz). Der Erwartungshorizont nutzt die Symmetrie; die Integration ist gleichwertig, deshalb keine Deutung nach (b).")

# ---- Analysis 1.2: Exponentialfunktion aus dem Graphen, Verschiebung als Streckung
EXP_SKIZZE = ("Koordinatensystem mit Gitter (Schrittweite 1), x-Achse von −3 bis 1,5 mit den Markierungen −2, −1, 0, 1, "
              "y-Achse von −0,5 bis 3,5 mit den Markierungen 1, 2, 3; exponentiell steigender Graph durch (0; 0,5) und (1; 2), "
              "links nahe der x-Achse")
row("2022MgrundlegendAAnalysis12", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Parameter einer Exponentialfunktion aus zwei Punkten des Graphen bestimmen", typ_neben="",
    stichwoerter="f(x) = a · b^x|f(0) = 1/2 gibt a = 1/2|f(1) = 2 gibt 1/2 · b = 2, b = 4",
    voraussetzungen="b⁰ = 1|Punkte am Gitter ablesen|lineare Gleichung in b",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=EXP_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f: x ↦ a · b^x mit a, b > 0; Graph in der Abbildung durch (0; 0,5) und (1; 2)",
    gesucht="Werte von a und b",
    verfahren="f(0) = a ablesen, dann f(1) = a · b nach b auflösen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f(0) = 1/2 ⇔ a = 1/2; damit f(1) = 2 ⇔ 1/2 · b = 2 ⇔ b = 4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Punkt (−1; 1/8) ungenau ablesen und damit rechnen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Werte aus der Abbildung.")

row("2022MgrundlegendAAnalysis12", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Verschiebung einer Exponentialfunktion als Streckung nachweisen", typ_neben="",
    stichwoerter="g(x) = 3^x|Verschiebung um 2 nach links: g(x + 2)|3^(x+2) = 3^x · 3² = 9 · g(x)|Streckung mit Faktor 9 in y-Richtung",
    voraussetzungen="Verschiebung in negative x-Richtung als g(x + 2)|Potenzgesetz|Streckung in y-Richtung als Vorfaktor",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x ↦ 3^x in IR; Graph um 2 in negative x-Richtung verschoben",
    gesucht="Nachweis, dass der verschobene Graph auch durch eine Streckung des Graphen von g in y-Richtung entsteht",
    verfahren="g(x + 2) mit dem Potenzgesetz umformen",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="g(x + 2) = 3^(x + 2) = 3^x · 3² = 9 · g(x) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Verschiebung nach links als g(x − 2) ansetzen",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- Analysis 1.3: 1/x², Verschiebung und Ableitung (ungegliedert)
row("2022MgrundlegendAAnalysis13", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Ableitungswert einer verschobenen Funktion über die Ausgangsfunktion berechnen", typ_neben="",
    stichwoerter="g(x) = 1/(x − 1)² − 5 aus f(x) = 1/x²|um 1 in positive x-Richtung, um 5 in negative y-Richtung|f'(x) = −2/x³|g'(2) = f'(1) = −2",
    voraussetzungen="Verschiebungen am Term ablesen|Potenzregel mit negativem Exponenten|Ableitung des verschobenen Graphen an der verschobenen Stelle",
    format="Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="g: x ↦ 1/(x − 1)² − 5 in IR ohne 1; f: x ↦ 1/x² in IR ohne 0; der Graph von g entsteht aus dem von f durch Verschiebung in x- und in y-Richtung",
    gesucht="die beiden Verschiebungen; Term von f'; Wert g'(2) mit diesem Term",
    verfahren="Verschiebungen am Term ablesen; f als x^(−2) ableiten; g'(2) = f'(2 − 1), da die Verschiebung in y-Richtung die Steigung nicht ändert",
    schritte="3", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="Verschiebung um 1 in positive x-Richtung und um 5 in negative y-Richtung; f'(x) = −2/x³; g'(2) = f'(1) = −2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="g'(2) = f'(2) = −1/4 rechnen (Verschiebung in x-Richtung vergessen)",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 1.3).")

# ---- Analysis 2: Fläche zwischen Parabel und Ursprungsgerade (ungegliedert)
row("2022MgrundlegendAAnalysis2", seite="1", punkte="5", afb_amtlich="III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Steigung einer Ursprungsgeraden aus dem Flächeninhalt zwischen Parabel und Gerade bestimmen", typ_neben="",
    stichwoerter="f(x) = x², y = mx mit m < 0|Schnittstellen 0 und m|Integral von m bis 0 über (mx − x²) dx = −m³/6|−m³/6 = 36 ⇔ m = −6",
    voraussetzungen="Schnittstellen mit Parameter|Gerade oberhalb der Parabel auf [m; 0]|Integral mit Parametergrenze|Gleichung dritten Grades",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x² in IR; Gerade y = m · x mit m < 0; Graph und Gerade schließen eine Fläche mit Inhalt 36 ein",
    gesucht="Wert von m",
    verfahren="Schnittstellen 0 und m, Integral der Differenz Gerade minus Parabel von m bis 0 als Term in m, gleich 36 setzen",
    schritte="4", zahlenraum="ganz|negativ|Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="x² = mx ⇔ x = 0 oder x = m; Integral von m bis 0 über (mx − x²) dx = [1/2 mx² − 1/3 x³] von m bis 0 = −1/2 m³ + 1/3 m³ = −1/6 m³; −1/6 m³ = 36 ⇔ m = −6 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Integral von 0 bis m bilden und das Vorzeichen falsch deuten",
    bemerkung="Standardbezug: K2 III, K5 III. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2, einzige Datei der Gruppe). Eichregel: (c) Flächeninhalt als Term in m herleiten (Grenzen, Orientierung mit m < 0) und (a) Flächenbedingung als Gleichung.")

# ---- AG/LA (A1) 1: Stromanbieter
STROM_SKIZZE = ("Übergangsdiagramm mit drei Knoten A (oben), B (links unten), C (rechts unten): Schleifen A 0,4, B 0,6, "
                "C 0,3; Pfeile A→B 0,4, B→A 0,1, A→C 0,2, C→A 0,2, B→C 0,3, C→B 0,5")
row("2022MgrundlegendAAGLAA11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsmatrix aus dem Diagramm unter zwei Darstellungen auswählen und ergänzen", typ_neben="",
    stichwoerter="v_(n+1) = M · v_n|Spalten sind Abgänge von A, B, C|Darstellung I|x = 0,5 (C nach B), y = 0,3 (B nach C)",
    voraussetzungen="Spalte der Übergangsmatrix als Abgänge eines Zustands lesen|Spaltensumme 1",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text|Zahl",
    material="Diagramm", skizze=STROM_SKIZZE, kontext="Stromanbieter/Kundenwechsel", textumfang="lang",
    gegeben="drei Stromanbieter A, B, C; Übergangsdiagramm je Quartal in der Abbildung; v_(n+1) = M · v_n mit Kundenzahlen (a_n; b_n; c_n); zwei Darstellungen I und II der Matrix mit Unbekannten x und y",
    gesucht="die zutreffende Darstellung sowie x und y",
    verfahren="erste Spalte mit den Abgängen von A vergleichen (0,4; 0,4; 0,2), fehlende Einträge aus dem Diagramm",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Darstellung I; x = 0,5; y = 0,3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauschen (Darstellung II)",
    bemerkung="Standardbezug: K4 I, K6 I. Amtlich, eigene Rechnung bestätigt (Spaltensummen 1). Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2022MgrundlegendAAGLAA11", "b", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Eintrag von M² berechnen und Zeile von M² im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="(M²)_11 = 0,4 · 0,4 + 0,1 · 0,4 + 0,2 · 0,2 = 0,24|dritte Zeile von M²: Kunden von C zwei Quartale später",
    voraussetzungen="Zeile mal Spalte|M² als Übergang über zwei Schritte",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Beschreiben Sie", antwort="Zahl|Text",
    material="Diagramm", skizze=STROM_SKIZZE, kontext="Stromanbieter/Kundenwechsel", textumfang="mittel",
    gegeben="M aus a (erste Zeile 0,4; 0,1; 0,2; erste Spalte 0,4; 0,4; 0,2)",
    gesucht="Eintrag der ersten Zeile und ersten Spalte von M²; Bedeutung der dritten Zeile von M²",
    verfahren="erste Zeile mit erster Spalte multiplizieren; dritte Zeile als Zugänge nach C über zwei Quartale deuten",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2022MgrundlegendAAGLAA11-a",
    ergebnis="0,4 · 0,4 + 0,1 · 0,4 + 0,2 · 0,2 = 0,24; zur Kundenverteilung zu einem bestimmten Zeitpunkt liefert die dritte Zeile von M² die Anzahl der Kunden des Anbieters C zwei Quartale später (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Eintrag von M² als 0,4² rechnen",
    bemerkung="Standardbezug: K1 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2.")

# ---- AG/LA (A1) 2: selbstinverse Matrix (ungegliedert)
row("2022MgrundlegendAAGLAA12", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Bedingung für eine selbstinverse Matrix mit Parametern herleiten", typ_neben="",
    stichwoerter="selbstinvers heißt M · M = E|M² = ((a² + bc; 0), (0; a² + bc))|a² + bc = 1 ⇔ bc = 1 − a² ≤ 1|a = 5: bc = −24, z. B. b = −4, c = 6",
    voraussetzungen="Definition der inversen Matrix als M · M⁻¹ = E|Matrizenprodukt mit Parametern|a² ≥ 0",
    format="Rechnung", operator="Zeigen Sie|Bestimmen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="M = ((a; b), (c; −a)) mit reellen a, b, c; M heißt selbstinvers, wenn M⁻¹ = M",
    gesucht="Nachweis, dass b · c ≤ 1 gilt, wenn M selbstinvers ist; für a = 5 je ein Wert von b und c mit M selbstinvers",
    verfahren="M⁻¹ = M in M² = E übersetzen, M² ausrechnen, bc = 1 − a² und a² ≥ 0; a = 5 einsetzen",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="M² = ((a² + bc; 0), (0; a² + bc)); M² = E ⇔ bc = 1 − a², d. h. bc ≤ 1; für a = 5 ergibt sich bc = 1 − 5² = −24, damit sind −4 und 6 mögliche Werte von b bzw. c (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Inverse mit der Formel berechnen und mit M vergleichen statt M² = E zu nutzen",
    bemerkung="Standardbezug: K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2). Eichregel: (a) die Definition „selbstinvers“ in M² = E übersetzen und (c) allgemeiner Nachweis mit Parametern.")

# ---- AG/LA (A2) 1.1: Ebene 3x − 2y = 0
row("2022MgrundlegendAAGLAA211", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen", typ_neben="",
    stichwoerter="E: 3x − 2y = 0|3 · 1 − 2 · 1,5 = 0|Punkt liegt in E",
    voraussetzungen="Koordinaten einsetzen",
    format="Rechnung", operator="Prüfen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: 3 · x − 2 · y = 0; Punkt (1; 1,5; 7)",
    gesucht="Prüfung, ob der Punkt in E liegt",
    verfahren="einsetzen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="3 · 1 − 2 · 1,5 = 0, d. h. der Punkt liegt in E (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die dritte Koordinate 7 vermissen und deshalb zweifeln",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet.")

row("2022MgrundlegendAAGLAA211", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Besondere Lage einer Ebene im Koordinatensystem beschreiben", typ_neben="",
    stichwoerter="Gleichung ohne z, rechte Seite 0|alle Punkte (0; 0; z) erfüllen die Gleichung|E enthält die z-Achse",
    voraussetzungen="fehlende Koordinate heißt parallel zur Achse|Ursprung in E heißt Achse enthalten",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: 3 · x − 2 · y = 0",
    gesucht="Beschreibung der besonderen Lage von E im Koordinatensystem",
    verfahren="z kommt nicht vor und der Ursprung liegt in E, also enthält E die z-Achse",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="E enthält die z-Achse (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur „parallel zur z-Achse“ sagen",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2022MgrundlegendAAGLAA211", "c", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Parameter für die Orthogonalität zweier Ebenen bestimmen", typ_neben="",
    stichwoerter="Normalenvektoren (3; −2; 0) und (2; s; 1)|Skalarprodukt 6 − 2s = 0|s = 3",
    voraussetzungen="Ebenen senkrecht heißt Normalenvektoren senkrecht|Skalarprodukt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: 3 · x − 2 · y = 0; F: 2 · x + s · y + z = 4",
    gesucht="Wert von s, für den F senkrecht zu E steht",
    verfahren="Skalarprodukt der Normalenvektoren null setzen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(2; s; 1) · (3; −2; 0) = 6 − 2s = 0 ⇔ s = 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Normalenvektoren als kollinear ansetzen (Parallelität statt Orthogonalität)",
    bemerkung="Standardbezug: K2 I, K5 II. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 1.2: gleichschenkliges Dreieck, Fläche 35
row("2022MgrundlegendAAGLAA212", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Gleichschenkligkeit eines Dreiecks mit Parameter über die Schenkellängen nachweisen", typ_neben="",
    stichwoerter="A(0; 0; 0), B(8; 6; 0), C(4; 3; z)|AC = (4; 3; z), BC = (−4; −3; z)|beide Längen √(25 + z²)",
    voraussetzungen="Länge eines Vektors mit Parameter|gleichschenklig mit Basis AB heißt |AC| = |BC|",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(0; 0; 0), B(8; 6; 0), C(4; 3; z) mit z > 0",
    gesucht="Nachweis, dass ABC gleichschenklig mit Basis AB ist",
    verfahren="|AC| und |BC| berechnen und vergleichen",
    schritte="1", zahlenraum="Wurzel|Potenz", einheiten="", abhaengig_von="",
    ergebnis="|AC| = |(4; 3; z)| = √(25 + z²), |BC| = |(−4; −3; z)| = √(25 + z²) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="|AB| mit einer Schenkellänge vergleichen",
    bemerkung="Standardbezug: K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2022MgrundlegendAAGLAA212", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Parameter einer Ecke aus dem Flächeninhalt eines gleichschenkligen Dreiecks bestimmen", typ_neben="",
    stichwoerter="Mittelpunkt M(4; 3; 0) von AB|Höhe MC = z|1/2 · |AB| · |MC| = 1/2 · 10 · z = 5z|5z = 35 ⇔ z = 7",
    voraussetzungen="Höhe eines gleichschenkligen Dreiecks trifft die Basis in der Mitte|Mittelpunkt einer Strecke|Flächenformel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(0; 0; 0), B(8; 6; 0), C(4; 3; z) mit z > 0; Dreieck ABC gleichschenklig mit Basis AB; Flächeninhalt 35",
    gesucht="Wert von z",
    verfahren="Höhe als Strecke vom Mittelpunkt der Basis zu C, Flächenformel nach z auflösen",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="2022MgrundlegendAAGLAA212-a",
    ergebnis="Mittelpunkt von AB: M(4; 3; 0); 1/2 · |AB| · |MC| = 1/2 · √(64 + 36) · z = 5z = 35 ⇔ z = 7 (amtlich)",
    zwischenergebnis="|AB| = 10",
    niveau_geschaetzt="II",
    fehlerquelle="|AC| als Höhe nehmen",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Die Gleichschenkligkeit ist in a gezeigt, nach dem Prinzip keine Deutung nach (b).")

# ---- AG/LA (A2) 1.3: parallele Geraden, Teilpunkt
row("2022MgrundlegendAAGLAA213", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Nichtidentität zweier paralleler Geraden über den Verbindungsvektor begründen", typ_neben="",
    stichwoerter="P(2; 0; 1), Q(2; 4; 9), Richtung (3; −1; 2)|PQ = (0; 4; 8) kein Vielfaches von (3; −1; 2)|Q liegt nicht auf g",
    voraussetzungen="parallele Geraden sind identisch, wenn ein Punkt der einen auf der anderen liegt|Kollinearität prüfen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(2; 0; 1), Q(2; 4; 9); g: x = OP + λ · (3; −1; 2), h: x = OQ + μ · (3; −1; 2)",
    gesucht="Nachweis, dass g und h nicht identisch sind",
    verfahren="Verbindungsvektor PQ mit dem Richtungsvektor vergleichen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="PQ = (0; 4; 8) ≠ λ · (3; −1; 2) für alle reellen λ (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="gleiche Richtungsvektoren als Identität lesen",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt. Anderer Lösungsweg als „Nichtidentität zweier Geraden über die Richtungsvektoren begründen“ (2023-ea-A), deshalb eigener Typ.")

row("2022MgrundlegendAAGLAA213", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Parallele Gerade durch einen Teilpunkt einer Strecke bestimmen", typ_neben="",
    stichwoerter="3 · |PT| = |QT| heißt T teilt PQ im Verhältnis 1 : 3|OT = OP + 1/4 · PQ = (2; 1; 3)|x = (2; 1; 3) + σ · (3; −1; 2)",
    voraussetzungen="Teilverhältnis in einen Bruchteil des Verbindungsvektors übersetzen|Parallele Gerade hat denselben Richtungsvektor",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(2; 0; 1), Q(2; 4; 9); parallele Geraden g und h mit Richtungsvektor (3; −1; 2); gesuchte Gerade schneidet PQ in T mit 3 · |PT| = |QT|",
    gesucht="Gleichung der Geraden parallel zu g und h durch T",
    verfahren="T = P + 1/4 · PQ, Gerade mit dem gemeinsamen Richtungsvektor",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2022MgrundlegendAAGLAA213-a",
    ergebnis="OT = OP + 1/4 · PQ = (2; 1; 3); damit x = (2; 1; 3) + σ · (3; −1; 2), σ reell (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="T = P + 1/3 · PQ ansetzen (Verhältnis 1 : 3 als Drittel lesen)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Das Teilverhältnis ist wörtlich vorgegeben, nach dem Prinzip keine Deutung nach (a).")

# ---- AG/LA (A2) 2: Quadrat in einer Ebene (ungegliedert)
row("2022MgrundlegendAAGLAA22", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Eckpunkt eines Quadrats in einer Ebene aus zwei benachbarten Ecken berechnen", typ_neben="",
    stichwoerter="P(1; 1; 1), Q(1; 1; 3), Ebene x1 − x2 = 0|PQ = (0; 0; 2), Seitenlänge 2|Richtung v senkrecht zu PQ und zum Normalenvektor (1; −1; 0): v = (1; 1; 0)|R = P + 2/|v| · v = (1 + √2; 1 + √2; 1)",
    voraussetzungen="Seite in der Ebene und senkrecht zur Nachbarseite über zwei Skalarprodukte|Vektor auf Länge skalieren|Seitenlänge aus PQ",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="P(1; 1; 1) und Q(1; 1; 3) benachbarte Ecken eines Quadrats in der Ebene x1 − x2 = 0",
    gesucht="Koordinaten eines möglichen weiteren Eckpunkts",
    verfahren="Richtungsvektor der Seite durch P aus Orthogonalität zu PQ und zum Normalenvektor, Länge 2 anpassen",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="v · (0; 0; 2) = 0 und v · (1; −1; 0) = 0 liefert v = (1; 1; 0) als Richtungsvektor der Geraden durch P und einen weiteren Eckpunkt R; die Seitenlänge ist 2; OR = (1; 1; 1) + 2/|(1; 1; 0)| · (1; 1; 0) = (1 + √2; 1 + √2; 1) (amtlich)",
    zwischenergebnis="ebenso (1 − √2; 1 − √2; 1) oder die Punkte über Q",
    niveau_geschaetzt="III",
    fehlerquelle="v = (1; 1; 0) ohne Anpassung der Länge verwenden (R = (2; 2; 1))",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2, einzige Datei der Gruppe). Eichregel: (a) die Bedingungen „Quadrat“ und „in der Ebene“ in zwei Orthogonalitäten und eine Längenbedingung übersetzen.")

# ---- Stochastik 1.1: Münze und zwei Tetraeder
row("2022MgrundlegendAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Ergebnisse eines zusammengesetzten Experiments zu einem Zahlenwert aufzählen", typ_neben="",
    stichwoerter="Münze + oder −, blaues und grünes Tetraeder 1 bis 4|+: Summe, −: blau minus grün|Zahlenwert 3: (−; 4; 1), (+; 1; 2), (+; 2; 1)",
    voraussetzungen="Ergebnis als Tripel lesen|systematisch durchgehen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Münze und Tetraeder", textumfang="lang",
    gegeben="Münze mit + und −, blaues und grünes Tetraeder mit 1 bis 4; bei + Summe, bei − blau minus grün; Beispiel (−; 2; 3) liefert −1",
    gesucht="alle Ergebnisse mit Zahlenwert 3",
    verfahren="Summe 3 aus zwei Augenzahlen, Differenz 3 aus zwei Augenzahlen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(−; 4; 1), (+; 1; 2), (+; 2; 1) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="(−; 1; 4) mitzählen (ergibt −3)",
    bemerkung="Standardbezug: K3 I, K6 I. Amtlich, eigene Rechnung bestätigt (Aufzählung aller 32 Ergebnisse).")

row("2022MgrundlegendAStochastik11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeit durch Abzählen günstiger Ergebnisse berechnen", typ_neben="",
    stichwoerter="negativ nur bei − und blau < grün|sechs Ergebnisse (−; 1; 2), (−; 1; 3), (−; 1; 4), (−; 2; 3), (−; 2; 4), (−; 3; 4)|2 · 4² = 32 Ergebnisse|6/32 = 3/16",
    voraussetzungen="Anzahl aller Ergebnisse als Produkt|günstige Ergebnisse aufzählen|Laplace-Formel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Münze und Tetraeder", textumfang="mittel",
    gegeben="Zufallsexperiment aus a mit 2 · 4 · 4 gleich wahrscheinlichen Ergebnissen",
    gesucht="Wahrscheinlichkeit für einen negativen Zahlenwert",
    verfahren="günstige Ergebnisse (− und blau kleiner als grün) zählen, durch 32 teilen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="2022MgrundlegendAStochastik11-a",
    ergebnis="einen negativen Zahlenwert liefern (−; 1; 2), (−; 1; 3), (−; 1; 4), (−; 2; 3), (−; 2; 4) und (−; 3; 4); damit 6/(2 · 4²) = 3/16 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="6/16 = 3/8 rechnen (die Münze im Nenner vergessen)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 1.2: Reiseregionen
row("2022MgrundlegendAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="P(A) = 60 %, P(B) = 30 %, P(A ∩ B) = 20 %|P_A(B) = 20 %/60 % = 1/3",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient|„sowohl als auch“ als Schnitt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Reiseunternehmen", textumfang="mittel",
    gegeben="60 % der Kunden reisen gerne in Region A, 30 % in Region B, 20 % in beide",
    gesucht="Wahrscheinlichkeit, dass eine zufällig gewählte Person aus den A-Kunden auch gerne nach B reist",
    verfahren="Schnittanteil durch Anteil A",
    schritte="1", zahlenraum="Prozent|Bruch", einheiten="", abhaengig_von="",
    ergebnis="20 %/60 % = 1/3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="20 %/30 % rechnen (Bedingung vertauscht)",
    bemerkung="Standardbezug: K3 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2022MgrundlegendAStochastik12", "b", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Anteil für genau eines von zwei Ereignissen aus Anteilen und Schnitt berechnen", typ_neben="",
    stichwoerter="entweder A oder B: A ohne B plus B ohne A|60 % + 30 % − 2 · 20 % = 50 %",
    voraussetzungen="„entweder oder“ als ausschließendes Oder|Schnitt zweimal abziehen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Reiseunternehmen", textumfang="kurz",
    gegeben="P(A) = 60 %, P(B) = 30 %, P(A ∩ B) = 20 %",
    gesucht="Anteil der Kunden, die entweder in A oder in B gerne reisen",
    verfahren="Anteile addieren, Schnitt zweimal abziehen",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="60 % + 30 % − 2 · 20 % = 50 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Vereinigung 70 % angeben (den Schnitt nur einmal abziehen)",
    bemerkung="Standardbezug: K1 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2. Das „entweder oder“ ist wörtlich, nach dem Prinzip keine Deutung.")

# ---- Stochastik 1.3: Kugeln auf drei Kisten
row("2022MgrundlegendAStochastik13", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="drei rote, drei gelbe Kugeln, zwei in die erste Kiste|rot dann gelb 1/2 · 3/5, gelb dann rot ebenso|2 · 1/2 · 3/5 = 3/5",
    voraussetzungen="Verteilen als Ziehen ohne Zurücklegen deuten|zwei Reihenfolgen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="drei rote und drei gelbe Kugeln werden zufällig auf drei Kisten zu je zwei Kugeln verteilt",
    gesucht="Wahrscheinlichkeit, dass in die erste Kiste eine rote und eine gelbe Kugel kommen",
    verfahren="Pfadregel für zwei Züge ohne Zurücklegen, beide Reihenfolgen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="2 · 1/2 · 3/5 = 6/10 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="mit Zurücklegen rechnen (2 · 1/2 · 1/2 = 1/2)",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2026-ga-A wiederverwendet.")

row("2022MgrundlegendAStochastik13", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsgrößen und Verteilungen",
    typ="Wahrscheinlichkeitsverteilung über ein unmögliches Ergebnis vervollständigen", typ_neben="",
    stichwoerter="X Anzahl der Kisten mit zwei Farben|P(X = 0) = 0, P(X = 1) = 0,6 gegeben|genau zwei gemischte Kisten unmöglich, P(X = 2) = 0|P(X = 3) = 1 − 0,6 = 0,4",
    voraussetzungen="erkennen, dass bei zwei gemischten Kisten die dritte auch gemischt ist|Summe der Wahrscheinlichkeiten 1",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Verteilung aus a; X = Anzahl der Kisten mit verschiedenfarbigen Kugeln; P(X = 0) = 0, P(X = 1) = 0,6",
    gesucht="P(X = 2) und P(X = 3)",
    verfahren="X = 2 als unmöglich begründen (zwei gemischte Kisten lassen eine rote und eine gelbe Kugel für die dritte), Rest auf X = 3",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2022MgrundlegendAStochastik13-a",
    ergebnis="es ist nicht möglich, in genau zwei Kisten verschiedenfarbige Kugeln zu legen, also P(X = 2) = 0; damit P(X = 3) = 1 − 0,6 = 0,4 (amtlich)",
    zwischenergebnis="Kontrolle durch Abzählen aller 20 Verteilungen: 12 mit X = 1, 8 mit X = 3",
    niveau_geschaetzt="III",
    fehlerquelle="P(X = 2) und P(X = 3) als je 0,2 raten",
    bemerkung="Standardbezug: K1 II, K2 I, K3 II, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Sonderfall erkennen – X = 2 ist unmöglich, das steht nirgends und muss gefunden werden; amtlich II.")

# ---- Stochastik 2: Glücksrad, maximale Wahrscheinlichkeit (ungegliedert)
row("2022MgrundlegendAStochastik2", seite="1", punkte="5", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Sektorwinkel eines Glücksrads aus der Maximierung einer Wahrscheinlichkeit ermitteln", typ_neben="",
    stichwoerter="P(blau) = 1/5, P(rot) = p, P(gelb) = 4/5 − p|A: einmal rot, einmal gelb bei zwei Drehungen|P(A) = 2 · p · (4/5 − p)|Parabel mit Nullstellen 0 und 4/5, Scheitel bei p = 2/5|2/5 · 360° = 144°",
    voraussetzungen="Restwahrscheinlichkeit als Term in p|Pfadregel mit zwei Reihenfolgen|Scheitel einer Parabel aus den Nullstellen|Wahrscheinlichkeit in Mittelpunktswinkel umrechnen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="lang",
    gegeben="Glücksrad mit blauem, rotem und gelbem Sektor, P(blau) = 1/5; zwei Drehungen; A: einmal rot und einmal gelb; der rote Sektor ist so gewählt, dass P(A) maximal ist",
    gesucht="Mittelpunktswinkel des roten Sektors",
    verfahren="P(A) als Term in p aufstellen, Maximum über die Symmetrie der Parabel, p in Grad umrechnen",
    schritte="4", zahlenraum="Bruch|ganz", einheiten="°", abhaengig_von="",
    ergebnis="mit p für die Wahrscheinlichkeit des roten Sektors gilt P(A) = 2 · p · (4/5 − p); der Term beschreibt eine nach unten geöffnete Parabel mit den Nullstellen 0 und 4/5; mit p = 2/5 ergibt sich 2/5 · 360° = 144° (amtlich)",
    zwischenergebnis="P(A) maximal 8/25",
    niveau_geschaetzt="III",
    fehlerquelle="den Faktor 2 für die Reihenfolgen vergessen (ändert das Maximum nicht) oder die Restwahrscheinlichkeit 1 − p statt 4/5 − p ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2, einzige Datei der Gruppe). Eichregel: (a) das Ereignis mit unbekanntem Sektor in einen Term in p übersetzen und (d) Maximum des Terms als Winkel deuten.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Extrempunkte: Gerade durch die Hochpunkte einer Kosinusfunktion begründen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Begründen, dass alle Hochpunkte einer verschobenen Kosinusfunktion auf einer waagerechten Geraden liegen.",
     "2022MgrundlegendAAnalysis11-a"),
    ("Fläche: Fläche zwischen Graph und Hochpunktgerade über eine Periode berechnen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Inhalt der Fläche zwischen einer trigonometrischen Funktion und der Geraden durch ihre Hochpunkte "
     "über eine Periode berechnen, durch Integration der Differenz oder über die Symmetrie.",
     "2022MgrundlegendAAnalysis11-b"),
    ("Parameter einer Exponentialfunktion aus zwei Punkten des Graphen bestimmen", "Analysis",
     "Rekonstruktion von Funktionsgleichungen",
     "Die Parameter a und b von a · b^x aus zwei am Graphen abgelesenen Punkten bestimmen.",
     "2022MgrundlegendAAnalysis12-a"),
    ("Transformation: Verschiebung einer Exponentialfunktion als Streckung nachweisen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Mit dem Potenzgesetz zeigen, dass die Verschiebung des Graphen von b^x in x-Richtung dieselbe Wirkung "
     "hat wie eine Streckung in y-Richtung.",
     "2022MgrundlegendAAnalysis12-b"),
    ("Transformation: Ableitungswert einer verschobenen Funktion über die Ausgangsfunktion berechnen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Die Verschiebungen zwischen zwei Graphen am Term ablesen und den Ableitungswert der verschobenen Funktion "
     "über die Ableitung der Ausgangsfunktion an der verschobenen Stelle berechnen.",
     "2022MgrundlegendAAnalysis13"),
    ("Fläche: Steigung einer Ursprungsgeraden aus dem Flächeninhalt zwischen Parabel und Gerade bestimmen",
     "Analysis", "Flächeninhalt durch Integration",
     "Den Parameter m einer Geraden y = mx bestimmen, für den die mit der Normalparabel eingeschlossene Fläche "
     "einen vorgegebenen Inhalt hat: Schnittstellen mit Parameter, Integral als Term in m, Gleichung lösen.",
     "2022MgrundlegendAAnalysis2"),
    ("Übergangsprozess: Übergangsmatrix aus dem Diagramm unter zwei Darstellungen auswählen und ergänzen",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus zwei vorgelegten Matrizen mit Unbekannten diejenige auswählen, die zum Übergangsdiagramm passt, und "
     "die fehlenden Einträge angeben.",
     "2022MgrundlegendAAGLAA11-a"),
    ("Übergangsprozess: Eintrag von M² berechnen und Zeile von M² im Sachzusammenhang deuten",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen Eintrag der Matrix M² als Zeile mal Spalte berechnen und eine Zeile von M² als Übergang über zwei "
     "Schritte deuten.",
     "2022MgrundlegendAAGLAA11-b"),
    ("Matrizenalgebra: Bedingung für eine selbstinverse Matrix mit Parametern herleiten", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Aus M⁻¹ = M die Bedingung M² = E gewinnen, sie für eine Matrix mit Parametern auswerten und Beispielwerte "
     "angeben.",
     "2022MgrundlegendAAGLAA12"),
    ("Besondere Lage einer Ebene im Koordinatensystem beschreiben", "Analytische Geometrie", "Ebenen",
     "Aus einer Koordinatengleichung ohne eine Variable und ohne Absolutglied die Lage der Ebene beschreiben "
     "(enthält eine Koordinatenachse).",
     "2022MgrundlegendAAGLAA211-b"),
    ("Geraden und Ebenen: Parameter für die Orthogonalität zweier Ebenen bestimmen", "Analytische Geometrie",
     "Orthogonalität",
     "Den Parameter einer Ebenengleichung so bestimmen, dass die Normalenvektoren zweier Ebenen senkrecht stehen.",
     "2022MgrundlegendAAGLAA211-c"),
    ("Ebene Figur: Gleichschenkligkeit eines Dreiecks mit Parameter über die Schenkellängen nachweisen",
     "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Zeigen, dass ein Dreieck mit einer Parameterkoordinate gleichschenklig ist, indem beide Schenkellängen "
     "als gleicher Term berechnet werden.",
     "2022MgrundlegendAAGLAA212-a"),
    ("Ebene Figur: Parameter einer Ecke aus dem Flächeninhalt eines gleichschenkligen Dreiecks bestimmen",
     "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Die Parameterkoordinate der Spitze eines gleichschenkligen Dreiecks aus dem vorgegebenen Flächeninhalt "
     "bestimmen, mit der Höhe vom Mittelpunkt der Basis.",
     "2022MgrundlegendAAGLAA212-b"),
    ("Nichtidentität zweier paralleler Geraden über den Verbindungsvektor begründen", "Analytische Geometrie",
     "Geraden",
     "Zeigen, dass zwei parallele Geraden nicht identisch sind, weil der Verbindungsvektor der Stützpunkte "
     "kein Vielfaches des Richtungsvektors ist.",
     "2022MgrundlegendAAGLAA213-a"),
    ("Parallele Gerade durch einen Teilpunkt einer Strecke bestimmen", "Analytische Geometrie", "Geraden",
     "Die Gleichung einer zu gegebenen Geraden parallelen Geraden aufstellen, die eine Strecke in einem durch "
     "ein Teilverhältnis festgelegten Punkt schneidet.",
     "2022MgrundlegendAAGLAA213-b"),
    ("Ebene Figur: Eckpunkt eines Quadrats in einer Ebene aus zwei benachbarten Ecken berechnen",
     "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Einen weiteren Eckpunkt eines Quadrats berechnen, wenn zwei benachbarte Ecken und die Ebene des Quadrats "
     "gegeben sind: Seitenrichtung aus zwei Orthogonalitäten, Länge anpassen.",
     "2022MgrundlegendAAGLAA22"),
    ("Laplace-Experiment: Ergebnisse eines zusammengesetzten Experiments zu einem Zahlenwert aufzählen",
     "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Alle Ergebnisse eines aus mehreren Zufallsgeräten zusammengesetzten Experiments angeben, die nach einer "
     "Rechenregel einen vorgegebenen Wert liefern.",
     "2022MgrundlegendAStochastik11-a"),
    ("Laplace-Experiment: Wahrscheinlichkeit durch Abzählen günstiger Ergebnisse berechnen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die Wahrscheinlichkeit eines Ereignisses als Anzahl der günstigen durch Anzahl aller gleich "
     "wahrscheinlichen Ergebnisse berechnen.",
     "2022MgrundlegendAStochastik11-b"),
    ("Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", "Stochastik",
     "Bedingte Wahrscheinlichkeit und Bayes",
     "Eine bedingte Wahrscheinlichkeit als Quotient aus dem Anteil des Schnitts und dem Anteil der Bedingung "
     "berechnen, ohne Baumdiagramm oder Vierfeldertafel.",
     "2022MgrundlegendAStochastik12-a"),
    ("Anteil für genau eines von zwei Ereignissen aus Anteilen und Schnitt berechnen", "Stochastik",
     "Ereignisse und Mengenoperationen",
     "Den Anteil des ausschließenden Oders zweier Ereignisse aus den Einzelanteilen und dem Schnittanteil "
     "berechnen.",
     "2022MgrundlegendAStochastik12-b"),
    ("Wahrscheinlichkeitsverteilung über ein unmögliches Ergebnis vervollständigen", "Stochastik",
     "Zufallsgrößen und Verteilungen",
     "Fehlende Wahrscheinlichkeiten einer Verteilung bestimmen, indem ein Wert der Zufallsgröße als unmöglich "
     "erkannt und der Rest über die Summe 1 ergänzt wird.",
     "2022MgrundlegendAStochastik13-b"),
    ("Laplace-Experiment: Sektorwinkel eines Glücksrads aus der Maximierung einer Wahrscheinlichkeit ermitteln",
     "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Die Wahrscheinlichkeit eines Ereignisses als Term in der unbekannten Sektorwahrscheinlichkeit aufstellen, "
     "das Maximum bestimmen und in einen Mittelpunktswinkel umrechnen.",
     "2022MgrundlegendAStochastik2"),
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
