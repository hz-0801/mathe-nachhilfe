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
    "stapel": "2023-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2023MerhoehtAAnalysis11": 5,
        "2023MerhoehtAAnalysis12": 5,
        "2023MerhoehtAAnalysis13": 5,
        "2023MerhoehtAAnalysis21": 5,
        "2023MerhoehtAAnalysis22": 5,
        "2023MerhoehtAAGLAA111": 5,
        "2023MerhoehtAAGLAA112": 5,
        "2023MerhoehtAAGLAA12": 5,
        "2023MerhoehtAAGLAA212": 5,
        "2023MerhoehtAAGLAA213": 5,
        "2023MerhoehtAAGLAA221": 5,
        "2023MerhoehtAAGLAA222": 5,
        "2023MerhoehtAStochastik11": 5,
        "2023MerhoehtAStochastik12": 5,
        "2023MerhoehtAStochastik13": 5,
        "2023MerhoehtAStochastik21": 5,
        "2023MerhoehtAStochastik22": 5,
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

# ---- Analysis 1.1: Eigenschaften einer ganzrationalen Funktion, Graph skizzieren
STELLEN_SKIZZE = ("Koordinatensystem ohne Skalen, y-Achse links; auf der x-Achse rechts vom Ursprung drei "
                  "markierte Stellen x1 < x2 < x3 mit wachsendem Abstand")
row("2023MerhoehtAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen", typ_neben="",
    stichwoerter="f' hat ein Minimum bei x3|Grad von f' mindestens 2|Grad von f mindestens 3",
    voraussetzungen="Extremstelle von f' heißt Grad von f' mindestens 2|Grad sinkt beim Ableiten um 1",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=STELLEN_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="ganzrationale, nicht lineare Funktion f in IR: Nullstelle x1; f'(x2) = 0 und f''(x2) ≠ 0; f' hat ein Minimum an der Stelle x3; Lage von x1, x2, x3 in der Abbildung",
    gesucht="Begründung, dass der Grad von f mindestens 3 ist",
    verfahren="aus dem Minimum von f' folgt Grad von f' mindestens 2, also Grad von f mindestens 3",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="da f' an der Stelle x3 ein Minimum hat, ist der Grad von f' mindestens 2 und damit der Grad von f mindestens 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="mit der Nullstelle x1 oder der Extremstelle x2 allein argumentieren (Grad 2 reicht dafür)",
    bemerkung="Standardbezug: K1 II, K6 I. Amtlich.")

row("2023MerhoehtAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren", typ_neben="",
    stichwoerter="Nullstelle x1, Extremstelle x2, Wendestelle x3 (Minimum von f')|steigend durch x1, Hochpunkt bei x2, Wendepunkt bei x3, danach fallend",
    voraussetzungen="Minimum von f' als Wendestelle deuten|Graph aus Stellen skizzieren",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=STELLEN_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Eigenschaften aus a: Nullstelle x1, f'(x2) = 0 mit f''(x2) ≠ 0, Minimum von f' bei x3; Abbildung mit x1, x2, x3",
    gesucht="Skizze eines möglichen Graphen von f in der Abbildung",
    verfahren="Graph durch (x1; 0) steigend, Hochpunkt (oder Tiefpunkt) über x2, Wendepunkt über x3 mit dort minimaler Steigung, danach wieder steigend",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2023MerhoehtAAnalysis11-a",
    ergebnis="Graph mit Nullstelle x1, Hochpunkt bei x2 und Wendepunkt bei x3, z. B. von links unten steigend durch x1, Hochpunkt über x2, fallend mit Wendepunkt über x3, danach flacher; der Erwartungshorizont zeigt eine solche Skizze (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="bei x3 einen Extrempunkt statt eines Wendepunkts zeichnen",
    bemerkung="Standardbezug: K4 II, K6 I. Amtlich. Das Feld skizze beschreibt das Material.")

# ---- Analysis 1.2: Parabelschar und Quadrat
PARQ_SKIZZE = ("Koordinatensystem ohne Skalen; nach unten geöffnete Parabel durch den Ursprung mit Hochpunkt "
               "rechts oben und zweiter Nullstelle rechts; gestricheltes Quadrat mit zwei Seiten auf den Achsen, "
               "dessen obere Seite durch den Hochpunkt geht")
row("2023MerhoehtAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen", typ_neben="",
    stichwoerter="f(x) = −x² + 2ax, Nullstellen 0 und 2a|Integral von 0 bis 2a|Stammfunktion −1/3 x³ + ax²|−8/3 a³ + 4a³ = 4/3 a³",
    voraussetzungen="Integration mit Parameter|Grenzen mit Parameter einsetzen",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=PARQ_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −x² + 2ax, definiert in IR, a > 1; Nullstellen 0 und 2a",
    gesucht="Nachweis, dass das Flächenstück zwischen Graph und x-Achse den Inhalt 4/3 a³ hat",
    verfahren="Integral von 0 bis 2a mit Stammfunktion auswerten",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Integral von 0 bis 2a über f(x) dx = [−1/3 x³ + ax²] von 0 bis 2a = −8/3 a³ + 4a³ = 4/3 a³ (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="(2a)³ als 2a³ einsetzen",
    bemerkung="Standardbezug: K5 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2024-ea-A wiederverwendet. Die Abbildung gehört zu b.")

row("2023MerhoehtAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus der Flächengleichheit von Quadrat und Flächenstück bestimmen", typ_neben="",
    stichwoerter="Hochpunkt (a; a²)|Quadrat mit Seitenlänge a² (obere Seite durch den Hochpunkt)|a⁴ = 4/3 a³|a = 4/3",
    voraussetzungen="Hochpunkt einer Parabel mit Parameter|Seitenlänge des Quadrats aus dem Hochpunkt ablesen|Gleichung mit Potenzen lösen, a > 1 beachten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=PARQ_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −x² + 2ax mit a > 1; Flächenstück mit Inhalt 4/3 a³; Quadrat mit zwei Seiten auf den Koordinatenachsen, der Hochpunkt liegt auf einer Seite; Quadrat und Flächenstück sind inhaltsgleich",
    gesucht="Wert von a",
    verfahren="Hochpunkt (a; a²) bestimmen, Seitenlänge a², Gleichung (a²)² = 4/3 a³ lösen",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2023MerhoehtAAnalysis12-a",
    ergebnis="Hochpunkt des Graphen von f: (a; a²); für a > 1 gilt 4/3 a³ = (a²)² ⇔ a = 4/3 (amtlich)",
    zwischenergebnis="a = 0 ausgeschlossen",
    niveau_geschaetzt="II",
    fehlerquelle="die Seitenlänge des Quadrats als a (x-Koordinate) nehmen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Die Gleichsetzung ist wörtlich vorgegeben, nach dem Prinzip keine Deutung.")

# ---- Analysis 1.3: Steigung am Graphen, Rotationsvolumen abschätzen
ROT_SKIZZE = ("Koordinatensystem mit x-Achse von 0 bis etwa 2,5 und y-Achse von 0 bis 2, Gitter mit Schrittweite "
              "0,5; Graph von f: bei (0; 2) beginnend fallend, Tiefpunkt etwa (0,6; 0,5), steigend zum Hochpunkt "
              "etwa (1,5; 1,5), dann fallend bis etwa (2; 1)")
row("2023MerhoehtAAnalysis13", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Aussage über die Steigung am Graphen beurteilen", typ_neben="",
    stichwoerter="größte Steigung in [0; 2] am Wendepunkt bei x = 1|Tangente dort mit Steigung kleiner als 3|Aussage richtig",
    voraussetzungen="Stelle größter Steigung am Graphen finden|Tangentensteigung abschätzen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ROT_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph einer in IR definierten Funktion f in der Abbildung; Aussage: für 0 ≤ x ≤ 2 ist die Steigung des Graphen kleiner als 3",
    gesucht="Beurteilung der Aussage",
    verfahren="die Stelle größter Steigung (Wendepunkt bei etwa 1) suchen und die Tangentensteigung dort mit 3 vergleichen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Abbildung ist zu entnehmen, dass für 0 ≤ x ≤ 2 die Steigung im Punkt (1; f(1)) am größten und die Tangentensteigung dort kleiner als 3 ist; die Aussage ist richtig (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Steigung am Rand (bei 0) prüfen, wo der Graph fällt",
    bemerkung="Standardbezug: K1 I, K2 II, K4 I, K6 I. Amtlich. Werte nur aus der Abbildung.")

row("2023MerhoehtAAnalysis13", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Rotationsvolumen über einbeschriebene Zylinder abschätzen", typ_neben="",
    stichwoerter="π · Integral von 0 bis 2 über f(x)² dx als Rotationsvolumen um die x-Achse|f ≥ 0,5 auf [0; 1], f ≥ 1 auf [1; 2]|zwei Zylinder mit Radien 0,5 und 1, Höhe 1|Volumen größer als π · 0,5² + π · 1²",
    voraussetzungen="Rotationsvolumen als Integral deuten|Untergrenze für f am Graphen ablesen|Zylindervolumen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ROT_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Graph von f in der Abbildung; Term π · Integral von 0 bis 2 über (f(x))² dx beschreibt das Volumen eines Körpers",
    gesucht="Begründung, dass dieses Volumen größer als π · 0,5² + π · 1² ist",
    verfahren="Term als Volumen des Rotationskörpers über [0; 2] deuten; der Graph liegt auf [0; 1] über 0,5 und auf [1; 2] über 1, also enthält der Körper zwei Zylinder",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="der Term beschreibt das Volumen des Körpers, der entsteht, wenn das Flächenstück zwischen Graph, Koordinatenachsen und x = 2 um die x-Achse rotiert; dieses Volumen ist größer als die Summe der Volumina der beiden Zylinder mit Radien 0,5 bzw. 1 und Höhe 1, also größer als π · 0,5² + π · 1² (amtlich)",
    zwischenergebnis="Vergleichswert 1,25π",
    niveau_geschaetzt="III",
    fehlerquelle="das Integral über f statt f² lesen und mit Flächen argumentieren",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I, K6 II. Amtlich. Erste Fundstelle des Themas Rotationsvolumen (nicht für das grundlegende Niveau). Eichregel: (d) Term als Rotationskörper deuten und mit einbeschriebenen Zylindern abschätzen – zwei verkettete Deutungen; amtlich II.")

# ---- Analysis 2.1: Transformation, Stammfunktionsgraph durch P
FP_SKIZZE = ("Koordinatensystem mit x-Achse von −3 bis 2,5 und y-Achse von −0,5 bis 5, Gitter mit Schrittweite "
             "0,5; Graph von f: von links nahe 0, Hochpunkt (−1; 1), Tiefpunkt (0; 0), danach steigend bis etwa "
             "(2; 2); Punkt P(0,5; 3) markiert")
row("2023MerhoehtAAnalysis21", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Extrempunkt eines transformierten Graphen angeben", typ_neben="",
    stichwoerter="g(x) = −f(x − 3): Spiegelung an der x-Achse und Verschiebung um 3 nach rechts|Hochpunkt (−1; 1) von f wird Tiefpunkt (2; −1) von g",
    voraussetzungen="Spiegelung an der x-Achse macht Hoch- zu Tiefpunkten|Verschiebung in x-Richtung um +3",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=FP_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph von f mit den einzigen Extrempunkten (−1; 1) und (0; 0) in der Abbildung; g(x) = −f(x − 3)",
    gesucht="Koordinaten des Tiefpunkts des Graphen von g",
    verfahren="der Hochpunkt (−1; 1) von f wird durch Spiegelung zum Tiefpunkt (−1; −1) und durch Verschiebung um 3 nach rechts zu (2; −1)",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(2; −1) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="um 3 nach links verschieben oder den Tiefpunkt (0; 0) von f verwenden (der wird Hochpunkt (3; 0))",
    bemerkung="Standardbezug: K1 II, K4 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2024-ga-A wiederverwendet (dort Nebentyp).")

row("2023MerhoehtAAnalysis21", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Graph einer Stammfunktion durch einen Punkt skizzieren", typ_neben="",
    stichwoerter="F' = f|f ≥ 0, also F monoton steigend|Extrempunkte von f werden Wendepunkte von F|bei 0 waagerechte Tangente (Terrassenpunkt)|Graph durch P(0,5; 3)",
    voraussetzungen="Vorzeichen von f als Monotonie von F|Extremstellen von f als Wendestellen von F|Nullstelle mit Vorzeichenwechsel-frei als Sattelpunkt",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=FP_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="Graph von f mit Hochpunkt (−1; 1) und Tiefpunkt (0; 0), f ≥ 0; Punkt P(0,5; 3); der Graph einer Stammfunktion von f verläuft durch P",
    gesucht="Skizze dieses Graphen in der Abbildung",
    verfahren="F steigt überall, links flach (f nahe 0), Wendepunkt über −1 (größte Steigung), Terrassenpunkt über 0, danach zunehmend steil; durch P legen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="monoton steigender Graph mit waagerechter Tangente bei x = 0 (etwa in (0; 2,5)), Wendepunkt bei x = −1, links flach nahe 2, durch P(0,5; 3), rechts steil steigend; der Erwartungshorizont zeigt die Skizze (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="bei x = 0 einen Tiefpunkt von F zeichnen (f wechselt dort das Vorzeichen nicht)",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II. Amtlich. Eichregel: (e) Beziehung Funktion–Stammfunktion am Graphen deuten (Vorzeichen, Extremstellen, Terrassenpunkt).")

# ---- Analysis 2.2: Kosinusfunktion aus Periode, Hoch- und Wendepunkt (ungegliedert)
row("2023MerhoehtAAnalysis22", seite="1", punkte="5", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Steigung einer aus Periode und Extrempunkt rekonstruierten Kosinusfunktion allgemein bestimmen", typ_neben="",
    stichwoerter="Periode p, Hochpunkt (p/2; p), Wendepunkt (p/4; p/2)|Amplitude p/2, Mittellinie p/2, Minimum bei 0|f(x) = −p/2 · cos(2π/p · x) + p/2|f'(x) = π · sin(2π/p · x)|f'(p/4) = π",
    voraussetzungen="Parameter einer Kosinusfunktion aus Periode, Amplitude und Verschiebung|Kettenregel|Sinuswert an π/2",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Kosinusfunktion f in IR mit Periode p; (p/2; p) ist Hochpunkt, (p/4; p/2) Wendepunkt",
    gesucht="Steigung des Graphen an der Stelle p/4",
    verfahren="aus Hoch- und Wendepunkt Amplitude p/2 und Mittellinie p/2 ablesen, Minimum im Ursprung: f(x) = −p/2 · cos(2π/p · x) + p/2; ableiten und p/4 einsetzen",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f(x) = −p/2 · cos(2π/p · x) + p/2; f'(x) = π · sin(2π/p · x); f'(p/4) = π (amtlich)",
    zwischenergebnis="Steigung unabhängig von p",
    niveau_geschaetzt="III",
    fehlerquelle="Amplitude p statt p/2 ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.2). Eichregel: (a) Punktangaben in die Parameter der Funktionsgleichung übersetzen und (c) Nachweis mit allgemeinem p.")

# ---- AG/LA (A1) 1.1: LGS mit Parameter b (ungegliedert, Sachgebiet „AG/LA“, Dublette 2023MerhoehtAAGLAA211)
row("2023MerhoehtAAGLAA111", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lösungsanzahl eines gestaffelten Gleichungssystems mit Parameter durch Fallunterscheidung begründen", typ_neben="",
    stichwoerter="I 2x + z = 0, II −y + 2z = 0, III 2y + bz = 1|2 · II + III: (4 + b) z = 1|b = −4: keine Lösung|b ≠ −4: z = 1/(4 + b), x = −1/2 · 1/(4 + b), y = 2/(4 + b), genau eine Lösung",
    voraussetzungen="Gleichungen kombinieren|Koeffizient null als Fall erkennen|Lösung mit Parameter angeben",
    format="Rechnung", operator="Untersuchen Sie|Geben Sie an", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="I 2x + z = 0, II −y + 2z = 0, III 2y + bz = 1 mit reellen x, y, z und Parameter b",
    gesucht="Anzahl der Lösungen in Abhängigkeit von b, gegebenenfalls die Lösungen",
    verfahren="II und III zu (4 + b) · z = 1 kombinieren; b = −4 liefert 0 = 1, sonst z und daraus y und x",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="II und III liefern 2 · (−y + 2z) + 2y + bz = 1 ⇔ (4 + b) · z = 1; für b = −4 keine Lösung; für b ≠ −4 gilt z = 1/(4 + b), x = −1/2 · 1/(4 + b), y = 2 · 1/(4 + b), also genau eine Lösung (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="durch (4 + b) teilen, ohne b = −4 auszuschließen",
    bemerkung="Standardbezug: K1 II, K2 I, K5 II. Amtlich, eigene Rechnung bestätigt. Typ aus 2025-ea-A wiederverwendet. Die Kurzbeschreibung nennt nur AG/LA; die Datei liegt wortgleich als 2023MerhoehtAAGLAA211 ein zweites Mal vor (Dublette ohne Zeile, vom Scan v0.2 erkannt). Eichregel: Fallunterscheidung (Grundregel) hat gefeuert, amtlich II – der Fall ist ein einzelner Koeffizient null.")

# ---- AG/LA (A1) 1.2: Brettspiel, Übergangsmatrix (Datei mit drei Seiten, c auf Seite 2)
UEB_SKIZZE = ("Übergangsdiagramm mit drei Feldern A (oben), B (links unten), C (rechts unten): Schleifen A 1/6, "
              "B 2/3, C 1/2; Pfeile A→B 1/2, A→C 1/3, B→C 1/3, C→A 1/2")
row("2023MerhoehtAAGLAA112", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Spielregel zu den Übergangswahrscheinlichkeiten eines Feldes angeben", typ_neben="",
    stichwoerter="Feld B: bleibt mit 2/3, nach C mit 1/3|Würfel: Augenzahl höchstens 4 bleiben, 5 oder 6 nach C",
    voraussetzungen="Wahrscheinlichkeiten 2/3 und 1/3 als Würfelereignisse deuten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Diagramm", skizze=UEB_SKIZZE, kontext="Brettspiel", textumfang="lang",
    gegeben="Brettspiel mit drei Feldern, je Runde ein Würfelwurf je Figur; Übergangsdiagramm mit den Wahrscheinlichkeiten in der Abbildung",
    gesucht="eine mögliche Spielregel (bezogen auf die Augenzahl) für eine Figur auf Feld B",
    verfahren="2/3 und 1/3 auf sechs Augenzahlen aufteilen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="beträgt die Augenzahl höchstens 4, bleibt die Figur stehen, anderenfalls wird sie auf das Feld C gezogen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Pfeile von A nach B mitlesen (Regel für Figuren auf A)",
    bemerkung="Standardbezug: K3 II, K4 I, K6 I. Amtlich. Datei mit drei Seiten. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2023MerhoehtAAGLAA112", "b", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zeile der Übergangsmatrix aus dem Diagramm angeben", typ_neben="",
    stichwoerter="v_(n+1) = M · v_n mit Anteilen (a; b; c)|zweite Zeile: Zugänge nach B|(1/2; 2/3; 0)",
    voraussetzungen="Zeile der Matrix als Zugänge in einen Zustand lesen (von A, von B, von C)",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Diagramm", skizze=UEB_SKIZZE, kontext="Brettspiel", textumfang="kurz",
    gegeben="Übergangsdiagramm; Modell v_(n+1) = M · v_n mit Vektoren (a; b; c) der Anteile auf A, B, C",
    gesucht="zweite Zeile von M",
    verfahren="Übergänge nach B ablesen: von A 1/2, von B 2/3, von C 0",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="(1/2; 2/3; 0) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Abgänge von B (Spalte) statt der Zugänge nach B (Zeile) angeben",
    bemerkung="Standardbezug: K3 I, K4 I. Amtlich, eigene Rechnung bestätigt (Spaltensummen 1).")

row("2023MerhoehtAAGLAA112", "c", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Einträge der Grenzmatrix im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Grenzmatrix mit Spalten (0,24; 0,36; 0,4)|Verteilung nach vielen Runden unabhängig vom Start|24 % auf A, 36 % auf B, 40 % auf C",
    voraussetzungen="Grenzmatrix als stabile Verteilung deuten|gleiche Spalten heißt Unabhängigkeit vom Startvektor",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Diagramm", skizze=UEB_SKIZZE, kontext="Brettspiel", textumfang="mittel",
    gegeben="Grenzmatrix zu M mit Zeilen (0,24; 0,24; 0,24), (0,36; 0,36; 0,36), (0,4; 0,4; 0,4)",
    gesucht="Bedeutung der drei verschiedenen Einträge im Sachzusammenhang",
    verfahren="Einträge als langfristige Anteile bzw. Wahrscheinlichkeiten je Feld lesen",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2023MerhoehtAAGLAA112-b",
    ergebnis="jede Spielfigur steht nach einer großen Anzahl von Spielrunden mit Wahrscheinlichkeit 24 % auf Feld A, 36 % auf Feld B und 40 % auf Feld C (amtlich)",
    zwischenergebnis="M^60 bestätigt die Grenzmatrix",
    niveau_geschaetzt="II",
    fehlerquelle="die Einträge als Übergangswahrscheinlichkeiten einer Runde deuten",
    bemerkung="Standardbezug: K3 II, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2.")

# ---- AG/LA (A1) 2: Marienkäfer, inverse Matrix
row("2023MerhoehtAAGLAA12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag aus einer Potenz der inversen Matrix bestimmen", typ_neben="",
    stichwoerter="M⁻¹ = ((0; 1/b; 0), (0; 0; 1/c), (1/a; 0; 0))|(M⁻¹)² hat den Eintrag 1/(c · a) an der Stelle (2; 1)|1/(ca) = 1/(60c)|a = 60",
    voraussetzungen="Matrizenprodukt mit Brüchen|Einträge vergleichen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Population/Marienkäfer", textumfang="lang",
    gegeben="Population (E; L; K) mit v_(n−1) = M⁻¹ · v_n, M⁻¹ = ((0; 1/b; 0), (0; 0; 1/c), (1/a; 0; 0)); (M⁻¹)² = ((0; 0; 3/c), (1/(60c); 0; 0), (0; 1/20; 0))",
    gesucht="Wert von a",
    verfahren="den Eintrag (2; 1) von (M⁻¹)² als Produkt 1/c · 1/a berechnen und mit 1/(60c) vergleichen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/c · 1/a = 1/(60c) ⇔ a = 60 (amtlich)",
    zwischenergebnis="aus Eintrag (1; 3): 1/(bc) = 3/c, also b = 1/3; aus (3; 2): 1/(ab) = 1/20 passt",
    niveau_geschaetzt="II",
    fehlerquelle="die Matrix quadrieren wollen statt einen Eintrag zu berechnen",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt. Thema Matrizen und Übergangsprozesse (nirgends Prüfungsgegenstand).")

row("2023MerhoehtAAGLAA12", "b", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Entwicklung einer Population aus einer Potenz der inversen Matrix beschreiben", typ_neben="",
    stichwoerter="(M⁻¹)³ = 1/(20c) · E|drei Monate zurück heißt Faktor 1/(20c), vorwärts Faktor 20c|c < 1/20: Abnahme, c > 1/20: Zunahme, c = 1/20: periodisch|Größe der Population",
    voraussetzungen="Vielfaches der Einheitsmatrix als Streckung deuten|inverse Richtung (rückwärts) umkehren|Fallunterscheidung nach c",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Population/Marienkäfer", textumfang="lang",
    gegeben="v_(n−1) = M⁻¹ · v_n; (M⁻¹)³ = ((1/(20c); 0; 0), (0; 1/(20c); 0), (0; 0; 1/(20c))) mit c > 0",
    gesucht="Beschreibung der Entwicklung der Population mit fortschreitender Zeit in Abhängigkeit von c, einschließlich der Größe",
    verfahren="(M⁻¹)³ = 1/(20c) · E heißt: drei Monate zurück ist jede Anzahl durch 20c geteilt, also drei Monate vorwärts mit 20c multipliziert; Fälle nach 20c gegen 1",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2023MerhoehtAAGLAA12-a",
    ergebnis="im Abstand von jeweils drei Monaten ändert sich jede der Anzahlen der Eier, Larven und Käfer mit dem Faktor 20c; für c < 1/20 nehmen die Anzahlen mit der Zeit ab, für c > 1/20 zu, für c = 1/20 wiederholen sie sich regelmäßig (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="den Faktor 1/(20c) als Wachstumsfaktor vorwärts lesen (Richtung vertauscht)",
    bemerkung="Standardbezug: K1 II, K3 III, K4 II, K6 II. Amtlich, eigene Rechnung bestätigt. Teilaufgabe steht auf Seite 2. Eichregel: (d) Matrixpotenz in eine Sachaussage übersetzen mit zwei Deutungen (Vielfaches der Einheitsmatrix, Richtungsumkehr) und Fallunterscheidung.")

# ---- AG/LA (A2) 1.2: Raute
row("2023MerhoehtAAGLAA212", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punktprobe an einer Geraden durchführen", typ_neben="",
    stichwoerter="g durch B(1; 1; 1) mit Richtung (1; 2; 2)|A(3; 5; 5) = B + 2 · (1; 2; 2)",
    voraussetzungen="Verbindungsvektor als Vielfaches des Richtungsvektors",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(3; 5; 5), B(1; 1; 1); g durch B mit Richtungsvektor (1; 2; 2)",
    gesucht="Nachweis, dass A auf g liegt",
    verfahren="A als B plus Vielfaches des Richtungsvektors schreiben",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(3; 5; 5) = (1; 1; 1) + 2 · (1; 2; 2) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="A mit dem Richtungsvektor statt mit dem Verbindungsvektor vergleichen",
    bemerkung="Standardbezug: K2 I, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ aus 2025-ga-A wiederverwendet.")

row("2023MerhoehtAAGLAA212", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Eckpunkte einer Raute mit einer Seite auf einer Geraden bestimmen", typ_neben="",
    stichwoerter="|AB| = √(4 + 16 + 16) = 6|C auf h durch B mit Richtung (1; 0; 0): C = B + 6 · (1; 0; 0) = (7; 1; 1)|D = A + 6 · (1; 0; 0) = (9; 5; 5)|alle Seiten 6",
    voraussetzungen="Raute als Parallelogramm mit gleich langen Seiten|Punkt auf einer Geraden in vorgegebenem Abstand|Vektoraddition",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(3; 5; 5), B(1; 1; 1); h durch B mit Richtungsvektor (1; 0; 0); C liegt auf h, ABCD ist eine Raute",
    gesucht="Koordinaten von C und D",
    verfahren="Seitenlänge |AB| = 6; C auf h im Abstand 6 von B (Einheitsvektor (1; 0; 0)); D = A + BC",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="2023MerhoehtAAGLAA212-a",
    ergebnis="|AB| = √(2² + 4² + 4²) = 6; OC = OB + 6 · (1; 0; 0) = (7; 1; 1), OD = OA + 6 · (1; 0; 0) = (9; 5; 5) (amtlich)",
    zwischenergebnis="ebenso möglich C(−5; 1; 1), D(−3; 5; 5)",
    niveau_geschaetzt="II",
    fehlerquelle="C auf h beliebig wählen, ohne die Seitenlänge 6 zu beachten",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt (alle Seiten 6, gegenüberliegende Seiten parallel).")

# ---- AG/LA (A2) 1.3: Gerade in Ebene, windschief zur Schar
row("2023MerhoehtAAGLAA213", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="g: x = (0; 1; 1) + λ · (1; 0; −1)|in x + y + z = 2 einsetzen|λ + 1 + 1 − λ = 2 für alle λ",
    voraussetzungen="Parameterdarstellung in die Koordinatengleichung einsetzen|λ fällt heraus",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (0; 1; 1) + λ · (1; 0; −1), λ reell; Ebene x + y + z = 2",
    gesucht="Nachweis, dass g in der Ebene liegt",
    verfahren="allgemeinen Punkt von g einsetzen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="λ + 1 + 1 − λ = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="nur den Stützpunkt einsetzen",
    bemerkung="Standardbezug: K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtAAGLAA213", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Windschiefe Lage einer Geraden zu einer Geradenschar nachweisen", typ_neben="",
    stichwoerter="h_a: x = (0; 0; 1) + μ · (1; a; 0)|Richtungsvektoren (1; 0; −1) und (1; a; 0) nie kollinear|Schnitt: I λ = μ, II 1 = μa, III 1 − λ = 1|λ = 0, μ = 0 widerspricht II|windschief für alle a",
    voraussetzungen="Windschief heißt nicht parallel und kein Schnittpunkt|Gleichungssystem mit Scharparameter auf Widerspruch führen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (0; 1; 1) + λ · (1; 0; −1); Schar h_a: x = (0; 0; 1) + μ · (1; a; 0), a reell",
    gesucht="Nachweis, dass g und h_a für jedes a windschief sind",
    verfahren="Kollinearität der Richtungsvektoren ausschließen (dritte Koordinate), Schnittgleichungen lösen: III gibt λ = 0, I gibt μ = 0, II wird 1 = 0",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2023MerhoehtAAGLAA213-a",
    ergebnis="g und h_a sind nicht parallel, da ihre Richtungsvektoren nicht kollinear sind; das Gleichungssystem I λ = μ, II 1 = μ · a, III 1 − λ = 1 liefert λ = 0 und μ = 0 im Widerspruch zu II (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Parallelität ausschließen und den Schnitt nicht prüfen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Nachrechnen mit mitgeführtem Parameter a, nach dem Prinzip II.")

# ---- AG/LA (A2) 2.1: gleichschenklig-rechtwinkliges Dreieck (ungegliedert)
row("2023MerhoehtAAGLAA221", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Eckpunkt eines gleichschenklig-rechtwinkligen Dreiecks mit Kathete in einer Koordinatenebene ermitteln", typ_neben="",
    stichwoerter="A im Ursprung, B(3; 5; −4)|zweite Kathete in der x1x3-Ebene: Richtung (4; 0; 3) senkrecht zu AB|Länge |AB| = √50|C = √50/5 · (4; 0; 3) = (4√2; 0; 3√2)",
    voraussetzungen="Vektor in der x1x3-Ebene mit Skalarprodukt null zu AB finden|Vektor auf die Länge |AB| skalieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Dreieck ABC mit A(0; 0; 0), B(3; 5; −4), gleichschenklig und rechtwinklig, AB Kathete, zweite Kathete in der x1x3-Ebene",
    gesucht="Koordinaten eines möglichen Punktes C",
    verfahren="rechter Winkel in A: Richtung (4; 0; 3) liegt in der x1x3-Ebene und ist senkrecht zu AB; auf die Länge |AB| bringen",
    schritte="3", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="die Gerade durch A mit Richtungsvektor (4; 0; 3) liegt in der x1x3-Ebene und steht wegen (4; 0; 3) · (3; 5; −4) = 0 senkrecht zu AB; |AB|/|(4; 0; 3)| · (4; 0; 3) = √2 · (4; 0; 3); für C kommt (4√2; 0; 3√2) infrage (amtlich)",
    zwischenergebnis="ebenso (−4√2; 0; −3√2)",
    niveau_geschaetzt="III",
    fehlerquelle="die Länge des Richtungsvektors nicht an |AB| anpassen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 II. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben (Aufgabe 2.1). Eichregel: (a) drei Bedingungen (Ebene, Orthogonalität, gleiche Länge) in eine Vektorkonstruktion übersetzen.")

# ---- AG/LA (A2) 2.2: Spiegelebene zweier Geraden
row("2023MerhoehtAAGLAA222", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Nichtidentität zweier Geraden über die Richtungsvektoren begründen", typ_neben="",
    stichwoerter="g: (1; 1; 1) + r · (1; 2; 0), h: (1; 1; 1) + s · (2; 1; 0)|gleicher Stützpunkt|Richtungsvektoren nicht kollinear",
    voraussetzungen="Kollinearität prüfen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (1; 1; 1) + r · (1; 2; 0) und h: x = (1; 1; 1) + s · (2; 1; 0)",
    gesucht="Begründung, dass g und h nicht identisch sind",
    verfahren="Richtungsvektoren vergleichen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Richtungsvektoren von g und h sind nicht kollinear (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="wegen des gemeinsamen Stützpunkts Identität annehmen",
    bemerkung="Standardbezug: K1 I, K4 I. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtAAGLAA222", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Spiegelebene zweier sich schneidender Geraden bestimmen", typ_neben="",
    stichwoerter="Richtungsvektoren gleich lang|Summe (3; 3; 0) ist Normalenvektor einer Spiegelebene|Ebene x1 + x2 + c = 0 durch (1; 1; 1)|c = −2",
    voraussetzungen="Spiegelebene senkrecht zur Winkelhalbierenden|Summe gleich langer Vektoren als Winkelhalbierende|Ebene durch den Schnittpunkt",
    format="Rechnung", operator="Bestimmen Sie|Erläutern Sie", antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g und h mit gemeinsamem Punkt (1; 1; 1) und den Richtungsvektoren (1; 2; 0) und (2; 1; 0); g soll durch Spiegelung an einer Ebene auf h abgebildet werden",
    gesucht="Gleichung einer geeigneten Ebene mit Erläuterung",
    verfahren="die Richtungsvektoren sind gleich lang, ihre Summe halbiert den Winkel und ist Normalenvektor der Ebene, die g auf h spiegelt; Ebene durch den Schnittpunkt legen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2023MerhoehtAAGLAA222-a",
    ergebnis="da die Richtungsvektoren gleich lang sind, ist (1; 2; 0) + (2; 1; 0) = (3; 3; 0) ein Normalenvektor einer solchen Ebene; sie hat die Form x1 + x2 + c = 0, und (1; 1; 1) liegt genau dann darin, wenn 1 + 1 + c = 0, d. h. c = −2 (amtlich)",
    zwischenergebnis="zweite Lösung: Ebene mit Normalenvektor (1; 2; 0) − (2; 1; 0) = (−1; 1; 0), also x1 − x2 = 0",
    niveau_geschaetzt="III",
    fehlerquelle="die Summe der Richtungsvektoren als Richtung der Ebene statt als Normalenvektor nehmen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt (Spiegelung von (1; 2; 0) an der Ebene ergibt −(2; 1; 0)). Eichregel: (b) Sonderfall gleich langer Richtungsvektoren erkennen und (a) Spiegelbedingung in eine Ebenengleichung übersetzen.")

# ---- Stochastik 1.1: Kugeln mit Zahlen, Erwartungswert des Produkts
row("2023MerhoehtAStochastik11", "a", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="fünf Kugeln: dreimal 2, zweimal a|zweimal Ziehen mit Zurücklegen|2 · 3/5 · 2/5|verschiedene Zahlen",
    voraussetzungen="Faktor 2 als zwei Reihenfolgen deuten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Behälter mit fünf Kugeln, drei mit der Zahl 2, zwei mit der negativen Zahl a; zweimal Ziehen mit Zurücklegen; Term 2 · 3/5 · 2/5",
    gesucht="Ereignis, dessen Wahrscheinlichkeit der Term liefert",
    verfahren="3/5 · 2/5 ist ein Pfad mit einer 2 und einem a, der Faktor 2 beide Reihenfolgen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="auf den beiden entnommenen Kugeln stehen unterschiedliche Zahlen (amtlich)",
    zwischenergebnis="Wert 12/25",
    niveau_geschaetzt="II",
    fehlerquelle="„erst 2, dann a“ angeben und den Faktor 2 übersehen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (nach dem Abgleich mit Präfix).")

row("2023MerhoehtAStochastik11", "b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="X Produkt der beiden Zahlen: 4 mit 9/25, 2a mit 12/25, a² mit 4/25|E(X) = 4|a² + 6a − 16 = 0|a = −8 (a = 2 entfällt, a negativ)",
    voraussetzungen="Verteilung des Produkts aus den Pfaden|Erwartungswert ansetzen|quadratische Gleichung, Vorzeichenbedingung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Kugeln dreimal 2 und zweimal a (a < 0), zweimal Ziehen mit Zurücklegen; X ist das Produkt der gezogenen Zahlen; E(X) = 4",
    gesucht="Wert von a",
    verfahren="Werte 4, 2a, a² mit 9/25, 12/25, 4/25 ansetzen, E(X) = 4 nach a lösen, negative Lösung wählen",
    schritte="3", zahlenraum="Bruch|negativ|Potenz", einheiten="", abhaengig_von="2023MerhoehtAStochastik11-a",
    ergebnis="4 · 9/25 + 2a · 12/25 + a² · 4/25 = 4; a² + 6a − 16 = 0 ⇔ a = −3 − √(9 + 16) = −8 oder a = −3 + √(9 + 16) = 2; damit a = −8 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="a = 2 als Lösung nehmen und a < 0 übersehen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zusammengezogener Typ).")

# ---- Stochastik 1.2: Glücksrad, Baum mit Abbruch, Unabhängigkeit
row("2023MerhoehtAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm mit Abbruchbedingung erstellen", typ_neben="",
    stichwoerter="Sektoren 2 (p) und 3 (1 − p)|drehen bis Summe 5, 6 oder 7|Pfade 2, 2, 2 (Summe 6); 2, 2, 3 (7); 2, 3 (5); 3, 2 (5); 3, 3 (6)|Gewinn bei 6",
    voraussetzungen="Abbruchbedingung in Pfadlängen übersetzen|Äste mit p und 1 − p beschriften",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="zu zeichnen: Baum mit Wurzel, erste Stufe 2 (p) und 3 (1 − p); unter 2 wieder 2 (p) und 3 (1 − p), unter der Folge 2, 2 nochmals 2 (p) und 3 (1 − p); unter 3: 2 (p) und 3 (1 − p); Blätter mit den Summen 6, 7, 5, 5, 6",
    kontext="Glücksrad", textumfang="lang",
    gegeben="Glücksrad mit Sektoren 2 und 3, P(2) = p; gedreht wird, bis die Summe 5, 6 oder 7 ist; bei 6 Gewinn",
    gesucht="beschriftetes Baumdiagramm des Sachverhalts",
    verfahren="alle Pfade bis zum Erreichen einer Summe von mindestens 5 aufzeichnen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Baum mit den Pfaden (2, 2, 2), (2, 2, 3), (2, 3), (3, 2), (3, 3) und Astwahrscheinlichkeiten p bzw. 1 − p; der Erwartungshorizont zeigt das Diagramm (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="alle Pfade auf drei Stufen führen, auch nach den Folgen 2, 3 oder 3, 3",
    bemerkung="Standardbezug: K1 II, K4 I, K6 I. Amtlich. Das Feld skizze beschreibt die zu erstellende Zeichnung.")

row("2023MerhoehtAStochastik12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Gleichung für p aus der Unabhängigkeit zweier Ereignisse im Baumdiagramm aufstellen", typ_neben="",
    stichwoerter="E: erste Drehung 2, G: Gewinn (Summe 6)|Unabhängigkeit: P_E(G) = P(G)|P_E(G) = p² (nach der ersten 2 gewinnt nur die Folge 2, 2)|P(G) = p³ + (1 − p)²|p² = p³ + (1 − p)²",
    voraussetzungen="Unabhängigkeit als P_E(G) = P(G)|bedingte Wahrscheinlichkeit im Baum ablesen|Gewinnpfade summieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="mittel",
    gegeben="Baumdiagramm aus a; E: erste Drehung ergibt 2; G: Gewinn; E und G sind stochastisch unabhängig",
    gesucht="eine Gleichung in p, aus der p berechnet werden kann",
    verfahren="P_E(G) aus dem Teilbaum nach der ersten 2 (nur die Folge 2, 2 gewinnt: p²), P(G) aus den Pfaden (2, 2, 2) und (3, 3); gleichsetzen",
    schritte="3", zahlenraum="Potenz", einheiten="", abhaengig_von="2023MerhoehtAStochastik12-a",
    ergebnis="P_E(G) = P(G) ⇔ p² = p³ + (1 − p)² (amtlich)",
    zwischenergebnis="Lösung p ≈ 0,618",
    niveau_geschaetzt="II",
    fehlerquelle="P(E ∩ G) = p³ mit P_E(G) verwechseln",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt. Die Unabhängigkeit ist als Definition vorgegeben, das Ablesen der Pfade ist Routine.")

# ---- Stochastik 1.3: Kugel umlegen
row("2023MerhoehtAStochastik13", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Kugelzahl aus einer Wahrscheinlichkeitsbedingung beim Umlegen einer Kugel bestimmen", typ_neben="",
    stichwoerter="B1 fünf rote, B2 zwei rote und n blaue (n > 1)|eine Kugel aus B2 nach B1|ein Behälter einfarbig genau dann, wenn die Kugel rot ist (B2 behält beide Farben)|2/(n + 2) = 1/5|n = 8",
    voraussetzungen="Ereignis „einfarbig“ auf die Farbe der umgelegten Kugel zurückführen|Laplace-Wahrscheinlichkeit mit Parameter|Bruchgleichung",
    format="Rechnung", operator="Bestimmen Sie|Beschreiben Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="lang",
    gegeben="Behälter B1 mit fünf roten Kugeln, B2 mit zwei roten und n > 1 blauen; eine Kugel wird zufällig aus B2 nach B1 gelegt; die Wahrscheinlichkeit, dass danach ein Behälter nur Kugeln einer Farbe enthält, beträgt 1/5",
    gesucht="Wert von n mit Beschreibung des Gedankengangs",
    verfahren="B2 behält immer beide Farben, B1 bleibt genau dann einfarbig, wenn die umgelegte Kugel rot ist; P(rot) = 2/(n + 2) gleich 1/5 setzen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="da im Behälter B2 mindestens eine rote und eine blaue Kugel verbleiben, muss die in B1 gelegte Kugel rot sein; damit 2/(n + 2) = 1/5 ⇔ n = 8 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="P(blau) = 1/5 ansetzen (n = 1/2)",
    bemerkung="Standardbezug: K1 II, K2 I, K3 I, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Bedingung „ein Behälter einfarbig“ erst auf das Ereignis „rote Kugel“ zurückführen und dann in eine Gleichung übersetzen; amtlich II.")

row("2023MerhoehtAStochastik13", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeit eines sicheren Ereignisses beim Umlegen einer Kugel begründen", typ_neben="",
    stichwoerter="n = 6: B2 zwei rote, sechs blaue|Kugel rot: B1 sechs rote, B2 sechs blaue|Kugel blau: B1 fünf rote, B2 fünf blaue|in jedem Fall gleich, Wahrscheinlichkeit 1",
    voraussetzungen="beide Fälle durchspielen|sicheres Ereignis",
    format="Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="B1 fünf rote Kugeln, B2 zwei rote und sechs blaue; eine Kugel wird aus B2 nach B1 gelegt",
    gesucht="Wahrscheinlichkeit, dass danach die Anzahl der roten Kugeln in B1 mit der Anzahl der blauen in B2 übereinstimmt, mit Begründung",
    verfahren="beide Farben der umgelegten Kugel betrachten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="1; ist die umgelegte Kugel rot, enthält B1 sechs rote und B2 sechs blaue Kugeln, andernfalls B1 fünf rote und B2 fünf blaue (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur den Fall „rot“ betrachten und 2/8 angeben",
    bemerkung="Standardbezug: K1 II, K2 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 2.1: Tetraeder fünfmal
row("2023MerhoehtAStochastik21", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="Tetraeder 1 bis 4, fünfmal|(3/4)⁵|keinmal die 1 (oder keinmal eine bestimmte Zahl)",
    voraussetzungen="3/4 als Gegenwahrscheinlichkeit einer Zahl|Potenz als fünf unabhängige Würfe",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Tetraeder", textumfang="kurz",
    gegeben="Tetraeder mit 1 bis 4, fünfmal geworfen; Term (3/4)⁵",
    gesucht="ein Ereignis mit dieser Wahrscheinlichkeit, mit Begründung",
    verfahren="3/4 als Wahrscheinlichkeit für „nicht die 1“ deuten, fünfmal hintereinander",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Ereignis: es wird keinmal die Zahl 1 erzielt; bei jedem der fünf Würfe beträgt die Wahrscheinlichkeit, nicht die 1 zu erzielen, 3/4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="„fünfmal nicht die 1“ als „mindestens einmal“ formulieren",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K6 I. Amtlich. Typ wiederverwendet.")

row("2023MerhoehtAStochastik21", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Term für die Wahrscheinlichkeit aufstellen, dass jede Zahl mindestens einmal fällt", typ_neben="",
    stichwoerter="fünf Würfe, vier Zahlen, jede mindestens einmal: genau eine Zahl doppelt|erster Wurf beliebig (1), dann neue Zahl 3/4, neue 2/4, neue 1/4, die doppelte 1/4|Position der Wiederholung: (5 über 2)|(5 über 2) · 1 · 1/4 · 3/4 · 2/4 · 1/4",
    voraussetzungen="Ereignis als „genau eine Zahl doppelt“ deuten|Pfad mit abnehmenden Wahrscheinlichkeiten|Anzahl der Positionen der Wiederholung als Binomialkoeffizient",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Tetraeder", textumfang="kurz",
    gegeben="Tetraeder mit 1 bis 4, fünfmal geworfen",
    gesucht="Term für die Wahrscheinlichkeit, dass jede Zahl mindestens einmal erzielt wird",
    verfahren="genau eine Zahl fällt zweimal; Anzahl der Anordnungen mal Pfadwahrscheinlichkeit",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="(5 über 2) · 1 · 1/4 · 3/4 · 2/4 · 1/4 (amtlich)",
    zwischenergebnis="Wert 60/256 = 15/64 (Abzählen: 240 von 1024)",
    niveau_geschaetzt="III",
    fehlerquelle="(3/4 · 2/4 · 1/4) ohne die Anordnungen oder mit 5! statt (5 über 2)",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K6 II. Amtlich, eigene Rechnung bestätigt (Abzählen aller 1024 Folgen). Eichregel: (a) die Bedingung „jede Zahl mindestens einmal“ in „genau eine Wiederholung“ übersetzen und zählen.")

# ---- Stochastik 2.2: Kugeln nach Würfelwurf
row("2023MerhoehtAStochastik22", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit für mindestens zwei Treffer bei drei Versuchen nachweisen", typ_neben="",
    stichwoerter="je Kugel schwarz mit 2/3|genau zwei schwarz 3 · (2/3)² · 1/3 = 12/27|drei schwarz (2/3)³ = 8/27|Summe 20/27",
    voraussetzungen="Bernoulli-Kette mit n = 3|zwei Fälle addieren",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="drei Kugeln werden nacheinander gewählt: bei Augenzahl 1 oder 2 gelb, sonst schwarz",
    gesucht="Nachweis, dass mindestens zwei schwarze Kugeln mit Wahrscheinlichkeit 20/27 im Behälter liegen",
    verfahren="P(genau 2) + P(genau 3) mit p = 2/3",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="3 · 2/3 · 2/3 · 1/3 + (2/3)³ = 12/27 + 8/27 = 20/27 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den Faktor 3 für die Anordnungen vergessen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I, K6 I. Amtlich, eigene Rechnung bestätigt.")

row("2023MerhoehtAStochastik22", "b", seite="1", punkte="3", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen", typ_neben="",
    stichwoerter="Zusammensetzung zufällig: zwei schwarz mit 12/27, drei schwarz mit 8/27|dann zwei Kugeln ohne Zurücklegen|12/27 · 2/3 · 1/2 + 8/27 · 1 = 12/27",
    voraussetzungen="zwei Stufen verketten: Zusammensetzung, dann Ziehen|nur Zusammensetzungen mit mindestens zwei schwarzen tragen bei|Ziehen ohne Zurücklegen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Behälter mit drei zufällig gefärbten Kugeln (schwarz mit 2/3 je Kugel); zwei der drei Kugeln werden zufällig entnommen",
    gesucht="Wahrscheinlichkeit, dass beide entnommenen Kugeln schwarz sind",
    verfahren="über die Zusammensetzung aufsummieren: bei zwei schwarzen 2/3 · 1/2, bei drei schwarzen 1",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2023MerhoehtAStochastik22-a",
    ergebnis="12/27 · 2/3 · 1/2 + 8/27 = 12/27 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="mit fester Zusammensetzung (zwei schwarz) rechnen oder mit Zurücklegen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) das Experiment als zweistufig (zufällige Urne, dann Ziehen) modellieren.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Mindestgrad einer ganzrationalen Funktion aus Eigenschaften der Ableitung begründen", "Analysis",
     "Kurvenuntersuchung",
     "Aus Extremstellen der Ableitung auf den Mindestgrad der Ableitung und damit der Funktion schließen.",
     "2023MerhoehtAAnalysis11-a"),
    ("Graphen zu vorgegebenen Nullstellen, Extrem- und Wendestellen skizzieren", "Analysis",
     "Kurvenuntersuchung",
     "Einen möglichen Graphen skizzieren, der vorgegebene Nullstellen, Extremstellen und Wendestellen "
     "(auch als Extremstellen der Ableitung formuliert) besitzt.",
     "2023MerhoehtAAnalysis11-b"),
    ("Scharparameter aus der Flächengleichheit von Quadrat und Flächenstück bestimmen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Den Parameter bestimmen, für den ein aus dem Hochpunkt abgeleitetes Quadrat denselben Inhalt "
     "hat wie das Flächenstück unter der Parabel.",
     "2023MerhoehtAAnalysis12-b"),
    ("Aussage über die Steigung am Graphen beurteilen", "Analysis", "Ableitung und Änderungsrate",
     "Eine Aussage über die Steigung in einem Intervall beurteilen, indem die Stelle größter Steigung "
     "am Graphen gefunden und die Tangentensteigung dort abgeschätzt wird.",
     "2023MerhoehtAAnalysis13-a"),
    ("Rotationsvolumen über einbeschriebene Zylinder abschätzen", "Analysis", "Rotationsvolumen",
     "Einen Term π · Integral f² als Rotationsvolumen deuten und über einbeschriebene Zylinder eine "
     "untere Schranke begründen.",
     "2023MerhoehtAAnalysis13-b"),
    ("Graph einer Stammfunktion durch einen Punkt skizzieren", "Analysis", "Stammfunktion und Hauptsatz",
     "Den Graphen einer Stammfunktion durch einen vorgegebenen Punkt skizzieren, aus Vorzeichen, "
     "Nullstellen und Extremstellen des abgebildeten Graphen von f.",
     "2023MerhoehtAAnalysis21-b"),
    ("Steigung einer aus Periode und Extrempunkt rekonstruierten Kosinusfunktion allgemein bestimmen",
     "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Aus Periode, Hoch- und Wendepunkt mit allgemeinem Parameter die Gleichung einer Kosinusfunktion "
     "aufstellen und die Steigung an einer Stelle bestimmen.",
     "2023MerhoehtAAnalysis22"),
    ("Übergangsprozess: Spielregel zu den Übergangswahrscheinlichkeiten eines Feldes angeben",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Zu den Übergangswahrscheinlichkeiten eines Zustands eine passende Würfelregel formulieren.",
     "2023MerhoehtAAGLAA112-a"),
    ("Übergangsprozess: Zeile der Übergangsmatrix aus dem Diagramm angeben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Eine Zeile der Übergangsmatrix als Zugänge in einen Zustand aus dem Übergangsdiagramm ablesen.",
     "2023MerhoehtAAGLAA112-b"),
    ("Übergangsprozess: Einträge der Grenzmatrix im Sachzusammenhang deuten", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Die Einträge einer Grenzmatrix mit gleichen Spalten als langfristige Anteile je Zustand deuten.",
     "2023MerhoehtAAGLAA112-c"),
    ("Übergangsprozess: Matrixeintrag aus einer Potenz der inversen Matrix bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Einen unbekannten Eintrag einer Matrix aus einem vorgegebenen Eintrag ihrer Potenz durch "
     "Ausmultiplizieren der betreffenden Zeile und Spalte bestimmen.",
     "2023MerhoehtAAGLAA12-a"),
    ("Übergangsprozess: Entwicklung einer Population aus einer Potenz der inversen Matrix beschreiben",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus einer Potenz der inversen Übergangsmatrix, die ein Vielfaches der Einheitsmatrix ist, die "
     "zeitliche Entwicklung der Population mit Fallunterscheidung nach dem Faktor beschreiben.",
     "2023MerhoehtAAGLAA12-b"),
    ("Ebene Figur: Eckpunkte einer Raute mit einer Seite auf einer Geraden bestimmen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Die fehlenden Ecken einer Raute bestimmen, wenn zwei Ecken und die Gerade einer Seite gegeben "
     "sind: Seitenlänge, Punkt auf der Geraden im Abstand, Parallelogrammergänzung.",
     "2023MerhoehtAAGLAA212-b"),
    ("Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen", "Analytische Geometrie",
     "Lagebeziehungen",
     "Zeigen, dass eine Gerade in einer Ebene liegt, indem ihr allgemeiner Punkt die Koordinatengleichung "
     "für alle Parameterwerte erfüllt.",
     "2023MerhoehtAAGLAA213-a"),
    ("Windschiefe Lage einer Geraden zu einer Geradenschar nachweisen", "Analytische Geometrie",
     "Scharen von Geraden und Ebenen",
     "Nachweisen, dass eine Gerade zu jeder Geraden einer Schar windschief ist: Richtungsvektoren nie "
     "kollinear, Schnittgleichungssystem für alle Parameter widersprüchlich.",
     "2023MerhoehtAAGLAA213-b"),
    ("Dreieck: Eckpunkt eines gleichschenklig-rechtwinkligen Dreiecks mit Kathete in einer Koordinatenebene ermitteln",
     "Analytische Geometrie", "Orthogonalität",
     "Einen Eckpunkt aus Orthogonalität zur gegebenen Kathete, Lage in einer Koordinatenebene und gleicher "
     "Kathetenlänge konstruieren.",
     "2023MerhoehtAAGLAA221"),
    ("Nichtidentität zweier Geraden über die Richtungsvektoren begründen", "Analytische Geometrie", "Geraden",
     "Begründen, dass zwei Geraden mit gemeinsamem Punkt nicht identisch sind, weil die Richtungsvektoren "
     "nicht kollinear sind.",
     "2023MerhoehtAAGLAA222-a"),
    ("Spiegelebene zweier sich schneidender Geraden bestimmen", "Analytische Geometrie", "Spiegelung",
     "Eine Ebene bestimmen, die eine Gerade auf eine sie schneidende Gerade spiegelt: Summe gleich langer "
     "Richtungsvektoren als Normalenvektor, Ebene durch den Schnittpunkt.",
     "2023MerhoehtAAGLAA222-b"),
    ("Baumdiagramm mit Abbruchbedingung erstellen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Ein Baumdiagramm zeichnen, dessen Pfade unterschiedlich lang sind, weil das Experiment bei einer "
     "Bedingung (etwa erreichter Summe) endet.",
     "2023MerhoehtAStochastik12-a"),
    ("Gleichung für p aus der Unabhängigkeit zweier Ereignisse im Baumdiagramm aufstellen", "Stochastik",
     "Unabhängigkeit",
     "Aus der Unabhängigkeit zweier Ereignisse die Gleichung P_E(G) = P(G) mit den Pfadwahrscheinlichkeiten "
     "in p aufstellen.",
     "2023MerhoehtAStochastik12-b"),
    ("Ziehen ohne Zurücklegen: Kugelzahl aus einer Wahrscheinlichkeitsbedingung beim Umlegen einer Kugel bestimmen",
     "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Eine unbekannte Kugelzahl bestimmen, indem eine Bedingung an die Behälter auf die Farbe der "
     "umgelegten Kugel zurückgeführt und als Gleichung gelöst wird.",
     "2023MerhoehtAStochastik13-a"),
    ("Laplace-Experiment: Wahrscheinlichkeit eines sicheren Ereignisses beim Umlegen einer Kugel begründen",
     "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Begründen, dass ein Ereignis in allen Fällen eintritt, indem beide Ausgänge des Umlegens "
     "durchgespielt werden.",
     "2023MerhoehtAStochastik13-b"),
    ("Term für die Wahrscheinlichkeit aufstellen, dass jede Zahl mindestens einmal fällt", "Stochastik",
     "Kombinatorik",
     "Einen Term für die Wahrscheinlichkeit aufstellen, dass bei n + 1 Würfen eines n-seitigen Zufallsgeräts "
     "jede Zahl vorkommt: genau eine Wiederholung, Anordnungen mal Pfadwahrscheinlichkeit.",
     "2023MerhoehtAStochastik21-b"),
    ("Wahrscheinlichkeit für mindestens zwei Treffer bei drei Versuchen nachweisen", "Stochastik",
     "Binomialverteilung",
     "P(mindestens zwei Treffer) einer Bernoulli-Kette mit n = 3 als Summe der Fälle zwei und drei "
     "Treffer nachweisen.",
     "2023MerhoehtAStochastik22-a"),
    ("Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen",
     "Stochastik", "Baumdiagramm und Pfadregeln",
     "Eine Wahrscheinlichkeit berechnen, wenn erst die Zusammensetzung der Urne zufällig entsteht und "
     "dann daraus gezogen wird: über die Zusammensetzungen summieren.",
     "2023MerhoehtAStochastik22-b"),
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
