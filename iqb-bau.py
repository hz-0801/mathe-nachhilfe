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
    "stapel": "2018-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2018MerhoehtAAnalysis11": 5,
        "2018MerhoehtAAnalysis12": 5,
        "2018MerhoehtAAnalysis2": 5,
        "2018MerhoehtAAGLAA111": 5,
        "2018MerhoehtAAGLAA112": 5,
        "2018MerhoehtAAGLAA12": 5,
        "2018MerhoehtAAGLAA211": 5,
        "2018MerhoehtAAGLAA212": 5,
        "2018MerhoehtAAGLAA22": 5,
        "2018MerhoehtAStochastik11": 5,
        "2018MerhoehtAStochastik12": 5,
        "2018MerhoehtAStochastik2": 5,
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

# ---- Analysis 1.1: e^x + x/2 und Geraden
EXP_SKIZZE = ("Koordinatensystem mit Skalen −1 bis 1 auf der x-Achse, −1 bis 4 auf der y-Achse; Graph von f steil steigend "
              "durch (0; 1); Gerade g_c mit Steigung 1/2 unterhalb, schneidet die y-Achse bei −c (etwa −1)")
row("2018MerhoehtAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Fehlenden Schnittpunkt zweier Graphen über eine unlösbare Gleichung begründen", typ_neben="",
    stichwoerter="f(x) = g(x) ⇔ e^x + 1/2 x = 1/2 x − 1 ⇔ e^x = −1|e^x > 0, keine Lösung",
    voraussetzungen="Gleichsetzen|e^x > 0 für alle x",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = e^x + 1/2 x und g(x) = 1/2 x − 1 in IR",
    gesucht="Begründung, dass die Graphen keinen gemeinsamen Punkt haben",
    verfahren="Gleichung f(x) = g(x) auf e^x = −1 zurückführen",
    schritte="1", zahlenraum="Bruch|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="die Funktionsterme von f und g unterscheiden sich nur in den Summanden e^x bzw. −1; es gilt e^x ≠ −1 für alle x ∈ IR (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Gleichung numerisch lösen wollen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2018MerhoehtAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen zwei Graphen bestimmen", typ_neben="",
    stichwoerter="f(x) − g_c(x) = e^x + c|Integral von 0 bis 1 über (e^x + c) dx = [e^x + cx] von 0 bis 1 = e + c − 1|e + c − 1 = 3 ⇔ c = 4 − e",
    voraussetzungen="Differenzfunktion|Stammfunktion mit Parameter|Gleichung nach c auflösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=EXP_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = e^x + 1/2 x, g_c(x) = 1/2 x − c mit c > 0; Fläche zwischen beiden Graphen, der y-Achse und x = 1 hat den Inhalt 3",
    gesucht="Wert von c",
    verfahren="Integral der Differenz von 0 bis 1 gleich 3 setzen",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Integral von 0 bis 1 über (f(x) − g_c(x)) dx = Integral von 0 bis 1 über (e^x + c) dx = [e^x + cx] von 0 bis 1 = e + c − 1; e + c − 1 = 3 ⇔ c = 4 − e (amtlich)",
    zwischenergebnis="c ≈ 1,28",
    niveau_geschaetzt="II",
    fehlerquelle="1/2 x nicht herauskürzen und die Stammfunktion falsch bilden",
    bemerkung="Standardbezug: K2 II, K4 II, K5 II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Fläche: Steigung einer Ursprungsgeraden aus dem Flächeninhalt zwischen Parabel und Gerade bestimmen“ getrennt: dort Steigung und Schnittstelle vom Parameter abhängig, hier feste Grenzen.")

# ---- Analysis 1.2: kubische Funktion mit Wendepunkt
KUB_SKIZZE = ("Koordinatensystem ohne Skalen; Graph von −x³ + 3x² − 2x: von oben links durch den Ursprung fallend, "
              "Tiefpunkt rechts vom Ursprung unter der Achse, Nullstelle bei 1, Hochpunkt über der Achse, Nullstelle bei 2, dann fallend; Gf beschriftet")
row("2018MerhoehtAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentensteigung an einer Nullstelle über die Ableitung nachweisen", typ_neben="",
    stichwoerter="f'(x) = −3x² + 6x − 2|f'(1) = −3 + 6 − 2 = 1",
    voraussetzungen="Ableitung einer ganzrationalen Funktion|Tangentensteigung als Ableitungswert",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=KUB_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −x³ + 3x² − 2x in IR; Wendepunkt W bei x = 1",
    gesucht="Nachweis, dass die Tangente in W die Steigung 1 hat",
    verfahren="f'(1) berechnen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −3x² + 6x − 2, f'(1) = 1 (amtlich)",
    zwischenergebnis="W(1 | 0)",
    niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen beim Ableiten von −x³",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2021-ea-A; die Definition gilt für jeden Punkt des Graphen, hier der Wendepunkt – Vorschlag für den Abgleich: Name auf „in einem Punkt“ verallgemeinern).")

row("2018MerhoehtAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Anzahl der Schnittpunkte von Geraden durch den Wendepunkt mit dem Graphen nach der Steigung unterscheiden", typ_neben="",
    stichwoerter="Wendetangente hat Steigung 1|flachere Gerade (0 < m < 1) schneidet dreimal|Gerade mit m ≥ 1 nur in W",
    voraussetzungen="Wendetangente als Grenzfall|Lage des Graphen zur Wendetangente|Fallunterscheidung nach m",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=KUB_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="Gf mit Wendepunkt W(1 | 0) und Wendetangente der Steigung 1 (aus a); Geraden durch W mit positiver Steigung m",
    gesucht="Anzahl der Schnittpunkte dieser Geraden mit Gf in Abhängigkeit von m",
    verfahren="am Graphen: Geraden flacher als die Wendetangente schneiden dreimal, steilere nur in W",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2018MerhoehtAAnalysis12-a",
    ergebnis="die Anzahl der Schnittpunkte ist 3 für 0 < m < 1 und 1 für m ≥ 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="m = 1 zum Fall „drei Schnittpunkte“ zählen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. Amtlich, eigene Rechnung bestätigt. Geschätzt III über die Fallunterscheidung 0 < m < 1 gegen m ≥ 1 mit verschiedenem Ausgang (Grundregel), verkettet mit der Deutung der Wendetangente als Grenzfall; amtlich II – das IQB wertet die Fallunterscheidung am Graphen als Routine.")

# ---- Analysis 2: 4/x²
HYP2_SKIZZE = ("Koordinatensystem mit Skalen −5 bis 5 auf der x-Achse, 0 bis 5 auf der y-Achse; Graph von 4/x² achsensymmetrisch, "
               "zwei Äste von der y-Achse steil abfallend gegen die x-Achse; Gf beschriftet")
row("2018MerhoehtAAnalysis2", "a", seite="1", punkte="2", afb_amtlich="I|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Höhe einer waagerechten Sekante aus dem Abstand ihrer Schnittpunkte über die Symmetrie bestimmen", typ_neben="",
    stichwoerter="Schnittpunkte symmetrisch zur y-Achse|Abstand 1 heißt x-Koordinaten ±1/2|p = f(1/2) = 4/(1/4) = 16",
    voraussetzungen="Achsensymmetrie ausnutzen|Abstand in Schnittstellen übersetzen|Funktionswert",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=HYP2_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 4/x² in IR ohne 0, Graph achsensymmetrisch; Gerade parallel zur x-Achse durch P(0 | p) schneidet Gf in zwei Punkten mit Abstand 1",
    gesucht="Wert von p",
    verfahren="Schnittstellen ±1/2 aus der Symmetrie, p als Funktionswert",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="",
    ergebnis="p = f(0,5) = 16 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Abstand 1 als Schnittstelle x = 1 lesen (p = 4)",
    bemerkung="Standardbezug: K1 III, K2 III, K5 I. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) den Abstand 1 der Schnittpunkte mit der Symmetrie in die Schnittstellen ±1/2 übersetzen, verkettet mit dem Funktionswert.")

row("2018MerhoehtAAnalysis2", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt der Tangente mit gleichschenkligem Achsendreieck über die Steigung −1 berechnen", typ_neben="",
    stichwoerter="gleichschenkliges Dreieck mit den Achsen heißt Steigung −1 (u > 0, fallend)|f'(x) = −8/x³|f'(u) = −1 ⇔ u = 2|Q(2 | 1)",
    voraussetzungen="gleiche Achsenabschnitte als Steigung ±1 deuten|Ableitung von 4/x²|Gleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=HYP2_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = 4/x²; Tangente in Q(u | f(u)) mit u > 0 schließt mit den Koordinatenachsen ein gleichschenkliges Dreieck ein",
    gesucht="Koordinaten von Q",
    verfahren="Bedingung in f'(u) = −1 übersetzen und lösen",
    schritte="3", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −8/x³, f'(u) = −1 ⇔ u = 2, f(2) = 1 (amtlich)",
    zwischenergebnis="Tangente y = −x + 3",
    niveau_geschaetzt="III",
    fehlerquelle="Steigung +1 ansetzen (keine Lösung für u > 0)",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Gleichschenkligkeit des Achsendreiecks in die Steigung −1 übersetzen, verkettet mit Ableitung und Gleichung. Umkehrung des Typs „Gleichschenkligkeit des Dreiecks aus Tangente und Koordinatenachsen allgemein begründen“ (2019-ga-A).")

# ---- AG/LA (A1) 1.1: Übergangstabelle
row("2018MerhoehtAAGLAA111", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="Schleife A mit 0,7|Pfeil A → B mit 0,3|Schleife B mit 1|kein Pfeil B → A (0)",
    voraussetzungen="Tabelle von/nach lesen|Diagramm mit Schleifen und Pfeilen",
    format="Zeichnen", operator="Erstellen Sie", antwort="Grafik",
    material="Tabelle", skizze="Übergangstabelle von A, B (Spalten) nach A, B (Zeilen): 0,7 und 0,3 in der Spalte A, 0 und 1 in der Spalte B", kontext="Zustandssystem", textumfang="lang",
    gegeben="Zustände A und B mit Anteilen a_n, b_n; Übergangstabelle: A → A 0,7, A → B 0,3, B → A 0, B → B 1; v_(n+1) = M · v_n",
    gesucht="zugehöriges Übergangsdiagramm",
    verfahren="Tabelleneinträge als Schleifen und Pfeile eintragen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Diagramm mit Schleife 0,7 an A, Pfeil 0,3 von A nach B, Schleife 1 an B (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten der Tabelle vertauschen (Pfeil B → A mit 0,3)",
    bemerkung="Standardbezug: K4 I, K6 I. Amtlich. Umkehrung des Typs „Übergangsprozess: Zeile der Übergangsmatrix aus dem Diagramm angeben“. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2018MerhoehtAAGLAA111", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Monotone Entwicklung der Anteile aus der Übergangstabelle begründen", typ_neben="",
    stichwoerter="Übergänge nur von A nach B, keiner zurück|a_(n+1) = 0,7 a_n < a_n|b_(n+1) = b_n + 0,3 a_n > b_n",
    voraussetzungen="Tabelle deuten|absorbierender Zustand B",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Tabelle", skizze="Übergangstabelle wie in a", kontext="Zustandssystem", textumfang="mittel",
    gegeben="Übergangstabelle aus a; Startverteilung mit 0 < a_0 < 1 und 0 < b_0 < 1",
    gesucht="Begründung, dass mit wachsendem n eine Koordinate von v_n kleiner und die andere größer wird",
    verfahren="aus der Tabelle die Einbahnrichtung A → B ablesen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2018MerhoehtAAGLAA111-a",
    ergebnis="der Tabelle ist zu entnehmen, dass Übergänge nur vom Zustand A in den Zustand B stattfinden (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur mit Zahlenbeispielen rechnen, ohne die Richtung der Übergänge zu nennen",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2018MerhoehtAAGLAA111", "c", seite="2", punkte="1", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Stationäre Verteilung bei absorbierendem Zustand angeben", typ_neben="",
    stichwoerter="M · v = v|B absorbierend: v = (0; 1)",
    voraussetzungen="Fixvektor als unveränderte Verteilung|absorbierender Zustand",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Tabelle", skizze="Übergangstabelle wie in a", kontext="Zustandssystem", textumfang="kurz",
    gegeben="M aus der Übergangstabelle",
    gesucht="eine Zustandsverteilung v mit M · v = v",
    verfahren="Verteilung ganz in B wählen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2018MerhoehtAAGLAA111-a",
    ergebnis="v = (0; 1) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Gleichungssystem aufstellen und an 0,7a = a scheitern (a = 0)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen“ getrennt: hier eine Verteilung angeben, aus dem Sachzusammenhang. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A1) 1.2: Diagramm, M²
AB2_SKIZZE = ("Übergangsdiagramm mit zwei Kreisen A und B; Schleife an A mit 0,5, Pfeil von A nach B mit 0,5, Pfeil von B nach A mit 1")
row("2018MerhoehtAAGLAA112", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Quadrat der Übergangsmatrix aus dem Diagramm berechnen", typ_neben="",
    stichwoerter="M = ((0,5; 1), (0,5; 0)) aus dem Diagramm|M² = ((0,75; 0,5), (0,25; 0,5))",
    voraussetzungen="Übergangsmatrix aus dem Diagramm|Matrixprodukt",
    format="Rechnung", operator="Berechnen Sie", antwort="Term",
    material="Diagramm", skizze=AB2_SKIZZE, kontext="Zustandssystem", textumfang="lang",
    gegeben="Zustände A und B; Diagramm: A bleibt 0,5, A → B 0,5, B → A 1; v_(n+1) = M · v_n",
    gesucht="M²",
    verfahren="M ablesen, M · M ausrechnen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="M² = ((0,5; 1), (0,5; 0)) · ((0,5; 1), (0,5; 0)) = ((0,75; 0,5), (0,25; 0,5)) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="M transponiert ablesen",
    bemerkung="Standardbezug: K2 I, K4 II, K5 I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Übergangsprozess: Quadrat der Übergangsmatrix berechnen und M² · v als Zustand nach zwei Schritten deuten“ (2018-ga-A) getrennt: hier Matrix erst aus dem Diagramm, keine Deutung. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2018MerhoehtAAGLAA112", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Rückrechnung eines Verteilungsvektors über die Inverse von M² beschreiben", typ_neben="",
    stichwoerter="v_(n+2) = M² · v_n|v_n = (M²)⁻¹ · v_(n+2)",
    voraussetzungen="Potenz als zwei Schritte|inverse Matrix hebt die Abbildung auf",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Diagramm", skizze=AB2_SKIZZE, kontext="Zustandssystem", textumfang="kurz",
    gegeben="M² aus a",
    gesucht="Verfahren, um aus v_(n+2) den Vektor v_n zu bestimmen",
    verfahren="Inverse von M² bilden und anwenden",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2018MerhoehtAAGLAA112-a",
    ergebnis="man bestimmt die zu M² inverse Matrix und multipliziert diese mit v_(n+2) (amtlich)",
    zwischenergebnis="(M²)⁻¹ = ((2; −2), (−1; 3))",
    niveau_geschaetzt="II",
    fehlerquelle="durch M² „dividieren“ wollen oder M⁻¹ nur einmal anwenden",
    bemerkung="Standardbezug: K2 II, K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A1) 2: Abbildungsmatrizen
row("2018MerhoehtAAGLAA12", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Abbildungsmatrix als Spiegelung an einer Koordinatenachse deuten", typ_neben="",
    stichwoerter="((−1; 0), (0; 1)) · (a; b) = (−a; b)|x-Koordinate wird Gegenzahl, y-Koordinate bleibt: Spiegelung an der y-Achse",
    voraussetzungen="Matrix-Vektor-Produkt mit Platzhaltern|Vorzeichenwechsel einer Koordinate als Achsenspiegelung",
    format="Rechnung|Begründung", operator="Bestimmen Sie|Begründen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="jede 2×2-Matrix M ordnet P(a | b) über M · (a; b) = (a'; b') den Bildpunkt P' zu; M = ((−1; 0), (0; 1))",
    gesucht="Koordinaten von P' in a und b und Begründung, dass die Zuordnung eine Spiegelung an der y-Achse ist",
    verfahren="Produkt ausrechnen, Koordinatenänderung deuten",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="((−1; 0), (0; 1)) · (a; b) = (−a; b), d. h. P'(−a | b); die x-Koordinate von P' ist die Gegenzahl der x-Koordinate von P, die y-Koordinate von P' stimmt mit der von P überein (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Spiegelung an der x-Achse nennen",
    bemerkung="Standardbezug: K1 II, K5 I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2018MerhoehtAAGLAA12", "b", seite="1", punkte="3", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Abbildungsmatrix aus einer geometrischen Bedingung an den Bildpunkt bestimmen", typ_neben="",
    stichwoerter="Spiegelung an der x-Achse: P*(a | −b), Matrix ((1; 0), (0; −1))|P* Mittelpunkt von O und P' heißt P' = 2 · P* = (2a | −2b)|M = ((2; 0), (0; −2))",
    voraussetzungen="Spiegelung an der x-Achse als Matrix|Mittelpunktsbedingung in P' = 2 P* übersetzen|Matrix aus der Koordinatenzuordnung ablesen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="P*(a* | b*) Spiegelpunkt von P an der x-Achse; P* soll Mittelpunkt der Strecke von O nach P' sein",
    gesucht="Matrix M, die P auf P' abbildet",
    verfahren="P* bestimmen, P' als 2 · P*, Matrix ablesen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2018MerhoehtAAGLAA12-a",
    ergebnis="die Spiegelung von P an der x-Achse ließe sich durch M = ((1; 0), (0; −1)) beschreiben; die Koordinaten von P' gehen jeweils aus der entsprechenden Koordinate von P* durch Multiplikation mit 2 hervor; damit wird die Zuordnung von P zu P' durch M = ((2; 0), (0; −2)) beschrieben (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="P' als Mittelpunkt von O und P* nehmen (Faktor 1/2 statt 2)",
    bemerkung="Standardbezug: K2 III, K4 III, K6 III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Mittelpunktsbedingung in P' = 2 · P* übersetzen, verkettet mit der Spiegelung und dem Ablesen der Matrix. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A2) 1.1: Ebene, Spiegelung einer Geraden
row("2018MerhoehtAAGLAA211", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen", typ_neben="",
    stichwoerter="S(−2; −4; 5) in x2 − 3x3 = −19: −4 − 15 = −19",
    voraussetzungen="Koordinaten einsetzen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: x2 − 3x3 = −19; S(−2 | −4 | 5)",
    gesucht="Nachweis, dass S in E liegt",
    verfahren="Einsetzen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="−4 − 3 · 5 = −19 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="x1 = −2 mit einsetzen wollen (kommt nicht vor)",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-A).")

row("2018MerhoehtAAGLAA211", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Orthogonalität zu einer Ebene über Kollinearität mit dem Normalenvektor begründen", typ_neben="",
    stichwoerter="PQ = (0; −3; 9)|Normalenvektor n = (0; 1; −3)|PQ = −3 · n",
    voraussetzungen="Verbindungsvektor|Normalenvektor aus der Koordinatengleichung|Vielfaches erkennen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: x2 − 3x3 = −19; P(1 | 2 | 2), Q(1 | −1 | 11)",
    gesucht="Nachweis, dass die Gerade PQ senkrecht zu E steht",
    verfahren="PQ als Vielfaches des Normalenvektors zeigen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="für PQ = (0; −3; 9) und den Normalenvektor n = (0; 1; −3) der Ebene gilt PQ = −3 · n (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Normalenvektor (1; −3; 0) aus den Koeffizienten falsch zuordnen (x1 fehlt)",
    bemerkung="Standardbezug: K1 I, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-A).")

row("2018MerhoehtAAGLAA211", "c", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Spiegelgerade einer Geraden an einer Ebene aus Fixpunkt und bekanntem Spiegelpunkt angeben", typ_neben="",
    stichwoerter="S liegt in E, bleibt bei der Spiegelung fest|P und Q gleich weit von E, PQ senkrecht zu E: Q ist Spiegelpunkt von P|h durch S und Q: x = OS + λ · SQ",
    voraussetzungen="Fixpunkt der Spiegelung in E|Spiegelpunkt aus gleichem Abstand und Lot|Gerade aus zwei Punkten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="P und Q gleich weit von E, PQ senkrecht zu E (aus b), S in E (aus a); g durch S und P, h Spiegelbild von g an E",
    gesucht="eine Gleichung von h",
    verfahren="Q als Spiegelpunkt von P erkennen, h durch S und Q",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2018MerhoehtAAGLAA211-a|2018MerhoehtAAGLAA211-b",
    ergebnis="h: x = OS + λ · SQ, λ ∈ IR (amtlich)",
    zwischenergebnis="SQ = (3; 3; 6)",
    niveau_geschaetzt="II",
    fehlerquelle="h durch P und Q legen (das ist die Lotgerade)",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. Amtlich, eigene Rechnung bestätigt. Gleicher Abstand und Lot sind im Text vorgegeben, Q als Spiegelpunkt damit praktisch benannt – nach dem Prinzip II.")

# ---- AG/LA (A2) 1.2: zwei Geraden, Ebene
row("2018MerhoehtAAGLAA212", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Orthogonalität zweier Geraden über das Skalarprodukt untersuchen", typ_neben="",
    stichwoerter="gleicher Stützpunkt (3; −3; 3) ist der Schnittpunkt|(3; 0; −1) · (1; 0; 3) = 3 − 3 = 0",
    voraussetzungen="gemeinsamen Stützpunkt erkennen|Skalarprodukt der Richtungsvektoren",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g: x = (3; −3; 3) + r · (3; 0; −1), h: x = (3; −3; 3) + s · (1; 0; 3)",
    gesucht="Schnittpunkt von g und h und Nachweis der Orthogonalität",
    verfahren="Stützpunkt ablesen, Skalarprodukt",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Koordinaten des Schnittpunkts: (3 | −3 | 3); (3; 0; −1) · (1; 0; 3) = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Schnittpunkt über ein Gleichungssystem berechnen statt den gemeinsamen Stützpunkt zu sehen",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-A).")

row("2018MerhoehtAAGLAA212", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung der Ebene durch zwei sich schneidende Geraden bestimmen", typ_neben="",
    stichwoerter="beide Richtungsvektoren haben x2 = 0|Normalenvektor (0; 1; 0)|E: x2 = c, Punkt (3; −3; 3) einsetzen: c = −3",
    voraussetzungen="Normalenvektor senkrecht zu beiden Richtungsvektoren (Kreuzprodukt oder Ablesen)|Koordinatenform mit Punkt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E enthält g und h aus a",
    gesucht="Gleichung von E in Koordinatenform",
    verfahren="Normalenvektor aus den Richtungsvektoren, Konstante über den Schnittpunkt",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2018MerhoehtAAGLAA212-a",
    ergebnis="der Vektor (0; 1; 0) steht senkrecht zu den Richtungsvektoren von g und h; damit hat die Gleichung von E die Form x2 = c mit c ∈ IR; es gilt (3 | −3 | 3) ∈ E ⇔ c = −3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Konstante c vergessen (x2 = 0)",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Der Normalenvektor ist ablesbar (beide x2-Komponenten null), Verkettung ohne zu findende Deutung, II.")

# ---- AG/LA (A2) 2: Quadrat in der yz-Ebene
row("2018MerhoehtAAGLAA22", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Lage einer Figur in einer Koordinatenebene aus Eckpunkt und orthogonaler Geraden begründen", typ_neben="",
    stichwoerter="P(0; 1; 5) hat x = 0, liegt in der yz-Ebene|Richtungsvektor (1; 0; 0) von g steht senkrecht auf der yz-Ebene|Ebene des Quadrats durch P senkrecht zu g ist die yz-Ebene",
    voraussetzungen="yz-Ebene als x = 0|Normalenvektor (1; 0; 0) der yz-Ebene|Ebene durch Punkt mit Normalenrichtung eindeutig",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="P(0 | 1 | 5) Eckpunkt eines Quadrats; g: x = (5; 4; 1) + t · (1; 0; 0) orthogonal zur Ebene des Quadrats",
    gesucht="Begründung, dass das Quadrat in der yz-Ebene liegt",
    verfahren="P in der yz-Ebene und g senkrecht zu ihr",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="P liegt in der yz-Ebene, der Richtungsvektor von g steht senkrecht dazu (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur P ∈ yz-Ebene nennen, ohne die Orthogonalität von g",
    bemerkung="Standardbezug: K1 II. Amtlich, eigene Rechnung bestätigt.")

row("2018MerhoehtAAGLAA22", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Benachbarte Ecke eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen", typ_neben="",
    stichwoerter="Diagonalenschnittpunkt auf g und in der yz-Ebene: Spurpunkt S(0; 4; 1)|SP = (0; −3; 4), SQ = (0; 4; 3)|gleich lang (5) und senkrecht: Q ist Nachbarecke von P",
    voraussetzungen="Diagonalenschnittpunkt als Spurpunkt von g in der yz-Ebene|Nachbarecken eines Quadrats: gleicher Abstand zum Mittelpunkt und rechter Winkel dort",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Diagonalenschnittpunkt des Quadrats liegt auf g; Q(0 | 8 | 4) in der yz-Ebene",
    gesucht="Nachweis, dass Q eine der beiden zu P benachbarten Ecken ist",
    verfahren="Spurpunkt S berechnen, |SP| = |SQ| und SP ⊥ SQ zeigen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2018MerhoehtAAGLAA22-a",
    ergebnis="Schnittpunkt der Diagonalen: S(0 | 4 | 1); mit SP = (0; −3; 4) und SQ = (0; 4; 3) ergibt sich |SP| = |SQ| und SP · SQ = 0 (amtlich)",
    zwischenergebnis="|SP| = |SQ| = 5",
    niveau_geschaetzt="III",
    fehlerquelle="nur |PQ| berechnen, ohne S zu bestimmen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Diagonalenschnittpunkt als Spurpunkt von g in der yz-Ebene übersetzen, verkettet mit der Nachbarschaftsbedingung (gleich lang, rechter Winkel bei S). Vom Typ „Ebene Figur: Diagonalenschnittpunkt und Flächeninhalt eines Quadrats aus dem Spurpunkt einer Geraden bestimmen“ getrennt: dort Flächeninhalt, hier Nachbarschaft einer Ecke.")

# ---- Stochastik 1.1: Binomialverteilung B(10; 0,8), symmetrische Verteilung
BIN_SKIZZE = ("drei Säulendiagramme P(X = k) über k = 0 bis 13: Abb. 1 mit Säulen von 3 bis 11, Maximum etwa 0,24 bei 8; Abb. 2 mit Säulen "
              "von 4 bis 10, Maximum etwa 0,3 bei 8; Abb. 3 mit y-Skala bis 0,6 und Säulen von 4 bis 10, Maximum etwa 0,6 bei 8 (Summe über 1)")
row("2018MerhoehtAStochastik11", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen", typ_neben="",
    stichwoerter="n = 10: keine Säulen über 10, Abb. 1 scheidet aus (P(X > 10) > 0)|Abb. 3: Summe der Säulen größer als 1|Abb. 2 passt",
    voraussetzungen="Wertebereich 0 bis n|Summe einer Verteilung ist 1",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm", skizze=BIN_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="X binomialverteilt mit n = 10, p = 0,8; drei Säulendiagramme, eines zeigt die Verteilung von X",
    gesucht="die beiden Diagramme, die X nicht darstellen, mit Begründung",
    verfahren="Wertebereich und Summe prüfen",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Abbildung 1 stellt die Verteilung nicht dar, da P(X > 10) > 0; Abbildung 3 nicht, da die Summe der P(X = k) über k = 0 bis 10 größer als 1 ist (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Abb. 1 wegen der Lage des Maximums bei 8 für richtig halten",
    bemerkung="Standardbezug: K1 II, K4 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2021-ga-A; hier Wertebereich und Summe statt Erwartungswert).")

row("2018MerhoehtAStochastik11", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Parameter n aus Erwartungswert und Symmetrie einer Binomialverteilung ermitteln", typ_neben="",
    stichwoerter="symmetrische Binomialverteilung heißt p = 0,5|n · 0,5 = 8 ⇔ n = 16",
    voraussetzungen="Symmetrie genau für p = 0,5|Erwartungswert n · p",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Y binomialverteilt mit n und p; E(Y) = 8; Verteilung symmetrisch",
    gesucht="Wert von n",
    verfahren="p = 0,5 aus der Symmetrie, n aus dem Erwartungswert",
    schritte="2", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="aufgrund der Symmetrie der Wahrscheinlichkeitsverteilung gilt p = 0,5; n · 0,5 = 8 ⇔ n = 16 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Symmetrie nicht in p = 0,5 übersetzen und n unbestimmt lassen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Die Symmetrie ist wörtlich vorgegeben, ihre Übersetzung in p = 0,5 ist Standardwissen, II.")

# ---- Stochastik 1.2: Glücksrad 1, 2, 3
row("2018MerhoehtAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsgrößen und Verteilungen",
    typ="Wahrscheinlichkeitsverteilung der Augensumme in einer Tabelle vervollständigen", typ_neben="",
    stichwoerter="neun gleich wahrscheinliche Paare|Summe 3: (1; 2), (2; 1) → 2/9|Summe 5: (2; 3), (3; 2) → 2/9|Summe 6: (3; 3) → 1/9",
    voraussetzungen="Laplace-Paare abzählen",
    format="Tabelle", operator="Ergänzen Sie", antwort="Tabelle",
    material="Figur", skizze="Glücksrad mit drei gleich großen Sektoren 1, 2, 3 und Zeiger; Tabelle k = 2 bis 6 mit P(X = 2) = 1/9 und P(X = 4) = 1/3 eingetragen, drei Felder leer", kontext="Glücksrad", textumfang="kurz",
    gegeben="Glücksrad mit drei gleichen Sektoren 1, 2, 3, zweimal gedreht; X Summe der Zahlen; Tabelle mit P(X = 2) = 1/9 und P(X = 4) = 1/3",
    gesucht="fehlende Werte P(X = 3), P(X = 5), P(X = 6)",
    verfahren="günstige Paare je Summe zählen, durch 9 teilen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="P(X = 3) = 2/9, P(X = 5) = 2/9, P(X = 6) = 1/9 (amtlich)",
    zwischenergebnis="Summe der Tabelle 1",
    niveau_geschaetzt="I",
    fehlerquelle="Paare (1; 2) und (2; 1) nur einmal zählen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2018MerhoehtAStochastik12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen", typ_neben="",
    stichwoerter="P(A) = 3/9 = 1/3, P(B) = 1/3|A ∩ B = {(2; 2)}, P(A ∩ B) = 1/9|P(A) · P(B) = 1/9 = P(A ∩ B): unabhängig",
    voraussetzungen="Wahrscheinlichkeiten der Ereignisse abzählen|Schnittereignis bestimmen|Produktregel als Kriterium",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Figur", skizze="Glücksrad wie in a", kontext="Glücksrad", textumfang="mittel",
    gegeben="A: (1; 3), (2; 2) oder (3; 1) wird erzielt; B: beim ersten Drehen eine 2",
    gesucht="ob A und B stochastisch unabhängig sind",
    verfahren="P(A), P(B), P(A ∩ B) berechnen und Produktregel prüfen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="P(A) · P(B) = 1/3 · 1/3 = 1/9 = P((2; 2)) = P(A ∩ B), d. h. A und B sind stochastisch unabhängig (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="A ∩ B mit drei Ergebnissen ansetzen",
    bemerkung="Standardbezug: K1 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- Stochastik 2: Zufallsgrößen mit Werten 3, 4, 5
row("2018MerhoehtAStochastik2", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert aus einer Verteilung mit fehlender Wahrscheinlichkeit berechnen", typ_neben="",
    stichwoerter="P(X = 5) = 1 − 1/3 − 1/4 = 5/12|E(X) = 1/3 · 3 + 1/4 · 4 + 5/12 · 5 = 49/12",
    voraussetzungen="fehlende Wahrscheinlichkeit über die Summe 1|Erwartungswertformel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X mit Werten 3, 4, 5; P(X = 3) = 1/3, P(X = 4) = 1/4",
    gesucht="Erwartungswert von X",
    verfahren="P(X = 5) ergänzen, gewichtete Summe",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/3 · 3 + 1/4 · 4 + (1 − 1/3 − 1/4) · 5 = 49/12 (amtlich)",
    zwischenergebnis="≈ 4,08",
    niveau_geschaetzt="II",
    fehlerquelle="P(X = 5) vergessen (E = 2)",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2018MerhoehtAStochastik2", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Wertebereich des Erwartungswerts aus Ungleichungen für die Wahrscheinlichkeiten bestimmen", typ_neben="",
    stichwoerter="P(Y = 4) + P(Y = 5) = 2/3|E(Y) = 1 + 4 · (2/3 − P(Y = 5)) + 5 · P(Y = 5) = 11/3 + P(Y = 5)|1/6 ≤ P(Y = 5) ≤ 3/6|23/6 ≤ E(Y) ≤ 25/6",
    voraussetzungen="Summe 1|Erwartungswert als Term in einer Wahrscheinlichkeit|Schranken aus beiden Ungleichungen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Y mit Werten 3, 4, 5; P(Y = 3) = 1/3, P(Y = 4) ≥ 1/6, P(Y = 5) ≥ 1/6",
    gesucht="alle Werte, die für E(Y) infrage kommen",
    verfahren="E(Y) in P(Y = 5) ausdrücken, Schranken für P(Y = 5) aus beiden Ungleichungen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="mit 1/6 ≤ P(Y = 5) ≤ 3/6 ergibt sich 23/6 ≤ E(Y) ≤ 25/6 (amtlich)",
    zwischenergebnis="Randfälle: (1/3; 1/2; 1/6) und (1/3; 1/6; 1/2)",
    niveau_geschaetzt="III",
    fehlerquelle="nur die beiden Randverteilungen rechnen und nicht alle Werte dazwischen nennen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Ungleichungen für die Wahrscheinlichkeiten erst in Schranken für P(Y = 5) und dann in Schranken für E(Y) übersetzen, verkettet mit dem Erwartungswertterm.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Fehlenden Schnittpunkt zweier Graphen über eine unlösbare Gleichung begründen", "Analysis", "Gleichungen lösen",
     "Begründen, dass zwei Graphen keinen gemeinsamen Punkt haben, weil die Gleichsetzung auf eine unlösbare "
     "Gleichung führt (etwa e^x = −1).",
     "2018MerhoehtAAnalysis11-a"),
    ("Fläche: Parameter einer Geraden aus dem Flächeninhalt zwischen zwei Graphen bestimmen", "Analysis",
     "Flächeninhalt durch Integration",
     "Den Parameter einer Geraden so bestimmen, dass die Fläche zwischen Graph und Gerade über einem festen "
     "Intervall einen vorgegebenen Inhalt hat (Integral der Differenz mit Parameter, Gleichung lösen).",
     "2018MerhoehtAAnalysis11-b"),
    ("Anzahl der Schnittpunkte von Geraden durch den Wendepunkt mit dem Graphen nach der Steigung unterscheiden", "Analysis",
     "Kurvenuntersuchung",
     "Für Geraden durch den Wendepunkt einer kubischen Funktion die Anzahl der Schnittpunkte mit dem Graphen nach "
     "der Steigung angeben (Wendetangente als Grenzfall).",
     "2018MerhoehtAAnalysis12-b"),
    ("Symmetrie: Höhe einer waagerechten Sekante aus dem Abstand ihrer Schnittpunkte über die Symmetrie bestimmen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Die Höhe einer waagerechten Geraden bestimmen, deren Schnittpunkte mit einem achsensymmetrischen Graphen "
     "einen vorgegebenen Abstand haben (Schnittstellen ±d/2, Funktionswert).",
     "2018MerhoehtAAnalysis2-a"),
    ("Berührpunkt der Tangente mit gleichschenkligem Achsendreieck über die Steigung −1 berechnen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Den Punkt bestimmen, in dem die Tangente mit den Koordinatenachsen ein gleichschenkliges Dreieck bildet "
     "(Gleichschenkligkeit als Steigung ±1 deuten, f'(u) = ∓1 lösen).",
     "2018MerhoehtAAnalysis2-b"),
    ("Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Aus einer Von-nach-Tabelle der Übergangsanteile das Übergangsdiagramm mit Schleifen und Pfeilen zeichnen.",
     "2018MerhoehtAAGLAA111-a"),
    ("Übergangsprozess: Monotone Entwicklung der Anteile aus der Übergangstabelle begründen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Begründen, dass ein Anteil mit jedem Schritt kleiner und der andere größer wird, weil Übergänge nur in eine "
     "Richtung stattfinden (absorbierender Zustand).",
     "2018MerhoehtAAGLAA111-b"),
    ("Übergangsprozess: Stationäre Verteilung bei absorbierendem Zustand angeben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Eine Verteilung mit M · v = v angeben, wenn ein Zustand absorbierend ist (alles in diesem Zustand).",
     "2018MerhoehtAAGLAA111-c"),
    ("Übergangsprozess: Quadrat der Übergangsmatrix aus dem Diagramm berechnen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Die Übergangsmatrix aus dem Diagramm ablesen und ihr Quadrat ausrechnen.",
     "2018MerhoehtAAGLAA112-a"),
    ("Übergangsprozess: Rückrechnung eines Verteilungsvektors über die Inverse von M² beschreiben", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Beschreiben, wie aus dem Verteilungsvektor zwei Schritte später der frühere Vektor bestimmt wird "
     "(inverse Matrix von M² anwenden).",
     "2018MerhoehtAAGLAA112-b"),
    ("Matrizenalgebra: Abbildungsmatrix als Spiegelung an einer Koordinatenachse deuten", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Den Bildpunkt einer durch eine 2×2-Matrix gegebenen Abbildung allgemein berechnen und die Abbildung als "
     "Spiegelung an einer Koordinatenachse begründen.",
     "2018MerhoehtAAGLAA12-a"),
    ("Matrizenalgebra: Abbildungsmatrix aus einer geometrischen Bedingung an den Bildpunkt bestimmen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Die 2×2-Matrix bestimmen, die einen Punkt auf einen durch eine geometrische Bedingung (Spiegelung, "
     "Mittelpunkt, Streckung) beschriebenen Bildpunkt abbildet.",
     "2018MerhoehtAAGLAA12-b"),
    ("Spiegelgerade einer Geraden an einer Ebene aus Fixpunkt und bekanntem Spiegelpunkt angeben", "Analytische Geometrie",
     "Spiegelung",
     "Die Gleichung des Spiegelbilds einer Geraden an einer Ebene angeben, wenn ihr Schnittpunkt mit der Ebene "
     "und der Spiegelpunkt eines weiteren Geradenpunkts bekannt sind.",
     "2018MerhoehtAAGLAA211-c"),
    ("Koordinatengleichung der Ebene durch zwei sich schneidende Geraden bestimmen", "Analytische Geometrie", "Ebenen",
     "Für die Ebene, die zwei sich schneidende Geraden enthält, eine Koordinatengleichung aufstellen "
     "(Normalenvektor senkrecht zu beiden Richtungsvektoren, Konstante über den Schnittpunkt).",
     "2018MerhoehtAAGLAA212-b"),
    ("Lage einer Figur in einer Koordinatenebene aus Eckpunkt und orthogonaler Geraden begründen", "Analytische Geometrie",
     "Ebenen",
     "Begründen, dass eine ebene Figur in einer Koordinatenebene liegt, wenn ein Eckpunkt darin liegt und eine "
     "zur Figurenebene orthogonale Gerade achsenparallel ist.",
     "2018MerhoehtAAGLAA22-a"),
    ("Ebene Figur: Benachbarte Ecke eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen",
     "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Nachweisen, dass ein Punkt eine zu einer gegebenen Ecke benachbarte Ecke eines Quadrats ist: "
     "Diagonalenschnittpunkt als Spurpunkt einer Geraden bestimmen, gleiche Abstände und rechten Winkel dort zeigen.",
     "2018MerhoehtAAGLAA22-b"),
    ("Parameter n aus Erwartungswert und Symmetrie einer Binomialverteilung ermitteln", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Aus der Symmetrie einer Binomialverteilung p = 0,5 folgern und n aus dem Erwartungswert n · p berechnen.",
     "2018MerhoehtAStochastik11-b"),
    ("Wahrscheinlichkeitsverteilung der Augensumme in einer Tabelle vervollständigen", "Stochastik",
     "Zufallsgrößen und Verteilungen",
     "Fehlende Wahrscheinlichkeiten in der Tabelle der Verteilung einer Summe aus zwei Laplace-Versuchen durch "
     "Abzählen der Paare ergänzen.",
     "2018MerhoehtAStochastik12-a"),
    ("Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen", "Stochastik", "Unabhängigkeit",
     "Für zwei beschriebene Ereignisse P(A), P(B) und P(A ∩ B) bestimmen und mit P(A) · P(B) = P(A ∩ B) über die "
     "Unabhängigkeit entscheiden.",
     "2018MerhoehtAStochastik12-b"),
    ("Erwartungswert aus einer Verteilung mit fehlender Wahrscheinlichkeit berechnen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Die fehlende Wahrscheinlichkeit einer Verteilung über die Summe 1 ergänzen und den Erwartungswert berechnen.",
     "2018MerhoehtAStochastik2-a"),
    ("Wertebereich des Erwartungswerts aus Ungleichungen für die Wahrscheinlichkeiten bestimmen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Alle möglichen Erwartungswerte einer Zufallsgröße bestimmen, wenn für die Wahrscheinlichkeiten nur "
     "Ungleichungen vorliegen (Erwartungswert als Term in einer Wahrscheinlichkeit, Schranken einsetzen).",
     "2018MerhoehtAStochastik2-b"),
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
