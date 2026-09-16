# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 1.2 · 16.09.2026 · gilt mit katalog-prompt.md v0.4, abitur-vokabular.md v1.1 und iqb.md v1.4

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

Änderungen gegenüber 1.1 (Auftrag „abi-Bestand gegen den Pool abgleichen"):
Kennzahl Landesverwendung – Zeilen des Stapels, auf die abi-Zeilen mit
„Dublette von:" verweisen (Kennzahlenzeile, Selbstprüfung je Stapel); Zeilen,
die abi als „Poolaufgabe (nicht erfasst)" vorgemerkt hat, werden beim
Stapellauf gemeldet (Vermerk danach per abgleich.py umstellen) und in der
Selbstprüfung gegen den Bestand geprüft.

Änderungen gegenüber 1.0 (Entscheidung des Lehrers, 16.09.2026: Themenfeld
bereinigen): leitidee und thema einer Zeile müssen gleich leitidee und thema
ihres Typs in abitur-typen.csv sein (geprüft für ZEILEN und in der
Selbstprüfung für den Bestand); der Schnitt Thema × Klasse × Handlung wird
über das Thema des Typs gemessen (Lauf 13 von abgleich.py hat den Bestand
darauf gebracht).

Änderungen gegenüber 0.9 (Entscheidung 25, 15.09.2026: gemeinsame Typenliste
für abi und iqb): Sachgebiete, Themen, Geltungstabelle, Gegenstandsklassen und
Handlungen kommen aus abitur-vokabular.md statt aus iqb.md; die Typenliste heißt
abitur-typen.csv und wird mit dem Profil abi geteilt – beispiel_id darf in
abi-katalog.csv zeigen, und ein Typ gilt als verwendet, wenn er in einem der
beiden Kataloge steht (ANDERE_KATALOGE). Umbenennungen laufen über abgleich.py.

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
  1. abitur-vokabular.md, katalog-prompt.md, iqb-quellen.csv, iqb-katalog.csv,
     abi-katalog.csv und abitur-typen.csv neben dieses Skript legen (aus dem Repo).
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen.
  3. python iqb-bau.py – schreibt beide CSV-Dateien, gibt Prüftabelle und
     Bericht aus. Bei einem Fehler wird nichts geschrieben.
  4. Ist ZEILEN leer, läuft nur die Selbstprüfung über den Gesamtbestand.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    # Stapel nach Spalte stapel in iqb-quellen.csv: Jahr-Niveau-Teil
    "stapel": "2017-ea-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2017MerhoehtAAnalysis11": 5, "2017MerhoehtAAnalysis12": 5, "2017MerhoehtAAnalysis2": 5,
        "2017MerhoehtAAGLAA111": 5, "2017MerhoehtAAGLAA112": 5,
        "2017MerhoehtAAGLAA211": 5, "2017MerhoehtAAGLAA212": 5, "2017MerhoehtAAGLAA22": 5,
        "2017MerhoehtAStochastik11": 5, "2017MerhoehtAStochastik12": 5, "2017MerhoehtAStochastik2": 5,
    },
    # True: Probelauf – prüfen und berichten, nichts schreiben, Stapel darf
    # unvollständig sein. False: Stapel muss vollständig sein, dann schreiben.
    "probe": False,
}

# ========================================= QUELLEN UND PRÜFUNG, NICHT ÄNDERN
KAT = "iqb-katalog.csv"
TYP = "abitur-typen.csv"
QUELLEN = "iqb-quellen.csv"
VOKABULAR = "abitur-vokabular.md"
KERN = "katalog-prompt.md"
# Kataloge der anderen Profile mit derselben Typenliste (Entscheidung 25): ihre
# ids gelten für beispiel_id, ihre Typfelder zählen als Verwendung.
ANDERE_KATALOGE = ["abi-katalog.csv"]
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


def abschnitt(text, wort, quelle):
    """Abschnitt einer Markdown-Datei, dessen Überschrift (## …) das Wort enthält."""
    for teil in re.split(r"^## ", text, flags=re.M)[1:]:
        if wort in teil.splitlines()[0]:
            return teil
    sys.exit(f"{quelle}: Abschnitt „{wort}“ nicht gefunden.")


def vokabular():
    """Kopfzeile und Formvokabular aus dem Kern, Sachgebiete und Themen aus abitur-vokabular.md."""
    kern, profil = lies(KERN), lies(VOKABULAR)

    m = re.search(r"^Kopfzeile:\s*\n(id;.+)$", kern, re.M)
    if not m:
        sys.exit(f"{KERN}: Kopfzeile nicht gefunden.")
    head = m.group(1).strip().split(";")

    v = {feld: liste_aus_klammer(kern, feld, KERN)
         for feld in ("format", "antwort", "material", "zahlenraum",
                      "textumfang", "niveau_geschaetzt")}

    m = re.search(r"trägt das Sachgebiet:\s*\*\*(.+?)\*\*", profil, re.S)
    if not m:
        sys.exit(f"{VOKABULAR}: Sachgebiete nicht gefunden.")
    leitideen = [s.strip() for s in re.sub(r"\s+", " ", m.group(1)).split("·") if s.strip()]

    themen = {}
    for m in re.finditer(r"^\*\*([^*:]+):\*\*(.+?)(?=\n\s*\n)", profil, re.S | re.M):
        name = m.group(1).strip()
        if name not in leitideen:
            continue
        themen[name] = [s.strip() for s in re.sub(r"\s+", " ", m.group(2)).split("·") if s.strip()]
    fehlt = [l for l in leitideen if l not in themen]
    if fehlt:
        sys.exit(f"{VOKABULAR}: keine Themenzeile für {fehlt}")
    return head, v, leitideen, themen


def geltung():
    """Geltungstabelle aus abitur-vokabular.md § 3: Thema × Zielprüfung, ja/nein.
    Liefert (Zielprüfungen, {thema: Menge der Zielprüfungen mit ja})."""
    profil = abschnitt(lies(VOKABULAR), "Geltung", VOKABULAR)
    m = re.search(r"^\| Thema \|(.+?)\|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)", profil, re.M)
    if not m:
        sys.exit(f"{VOKABULAR}: Geltungstabelle nicht gefunden.")
    ziele = [z.strip() for z in m.group(1).split("|") if z.strip()]
    tab = {}
    for zeile in m.group(2).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != len(ziele) + 1:
            sys.exit(f"{VOKABULAR}: Geltungszeile hat {len(zellen)} Zellen: {zeile}")
        thema, werte = zellen[0], zellen[1:]
        if any(w not in ("ja", "nein") for w in werte):
            sys.exit(f"{VOKABULAR}: Geltung muss ja oder nein sein: {zeile}")
        tab[thema] = {z for z, w in zip(ziele, werte) if w == "ja"}
    alle = {t for liste in THEMEN.values() for t in liste}
    fehlt = sorted(alle - set(tab))
    if fehlt:
        sys.exit(f"{VOKABULAR}: Themen ohne Geltungszeile: {fehlt}")
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{VOKABULAR}: Geltungszeilen ohne Thema in der Liste: {fremd}")
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
    """Gegenstandsklassen je Thema aus abitur-vokabular.md § 4 (Tabelle „Thema | Gegenstandsklassen").
    Liefert {thema: [Klasse, ...]}; Themen ohne Zeile führen keine Unterklasse."""
    profil = abschnitt(lies(VOKABULAR), "Gegenstandsklassen", VOKABULAR)
    m = re.search(r"^\| Thema \| Gegenstandsklassen \|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)",
                  profil, re.M)
    if not m:
        sys.exit(f"{VOKABULAR}: Tabelle der Gegenstandsklassen nicht gefunden.")
    tab = {}
    for zeile in m.group(1).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != 2:
            sys.exit(f"{VOKABULAR}: Klassenzeile hat {len(zellen)} Zellen: {zeile}")
        tab[zellen[0]] = [k.strip() for k in zellen[1].split("·") if k.strip()]
    alle = {t for liste in THEMEN.values() for t in liste}
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{VOKABULAR}: Klassenzeilen ohne Thema in der Liste: {fremd}")
    return tab


def handlungen():
    """Handlung je format-Wert aus dem Kern § 5 (Tabelle „format | Handlung"; bis Kern v0.3 in
    abitur-vokabular.md § 5)."""
    kern = abschnitt(lies(KERN), "Felder", KERN)
    m = re.search(r"^\| format \| Handlung \|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)", kern, re.M)
    if not m:
        sys.exit(f"{KERN}: Tabelle der Handlungen nicht gefunden.")
    tab = {}
    for zeile in m.group(1).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != 2:
            sys.exit(f"{KERN}: Handlungszeile hat {len(zellen)} Zellen: {zeile}")
        tab[zellen[0]] = zellen[1]
    fehlt = sorted(VOK["format"] - set(tab))
    if fehlt:
        sys.exit(f"{KERN}: format-Werte ohne Handlung: {fehlt}")
    return tab


def klasse_von(typ):
    """Gegenstandsklasse aus dem Typnamen (Wort vor dem Doppelpunkt) oder leer."""
    m = re.match(r"([^:]+): ", typ)
    return m.group(1) if m else ""


def pruefe_typname(typ, thema, a, wo):
    """Präfixregel abitur-vokabular.md § 4: Themen mit Klassen verlangen ein gültiges Präfix, andere keins."""
    k = klasse_von(typ)
    if thema in KLASSEN:
        a(k in KLASSEN[thema],
          f"{wo}: Typ „{typ}“ braucht ein Präfix aus {KLASSEN[thema]} (Thema {thema})")
    else:
        a(k == "", f"{wo}: Typ „{typ}“ trägt ein Präfix, Thema {thema} führt keine Klassen")


# typ → (leitidee, thema) aus abitur-typen.csv und NEUE_TYPEN; füllt main(). Seit v1.1
# (Lauf 13) trägt jede Zeile leitidee und thema ihres Typs, der Schnitt liest sie hier.
TYP_THEMA = {}


def pruefe_thema(z, a):
    """Zeilenthema = Typthema (abitur-vokabular.md § 4, Entscheidung 16.09.2026)."""
    if z["typ"] in TYP_THEMA:
        a(TYP_THEMA[z["typ"]] == (z["leitidee"], z["thema"]),
          f"{z['id']}: leitidee/thema ({z['leitidee']}, {z['thema']}) weichen vom Typ ab "
          f"{TYP_THEMA[z['typ']]}")


HEAD, VOK, LEITIDEEN, THEMEN = vokabular()
ZIELE, GELTUNG = geltung()
KLASSEN = klassen()
HANDLUNG = handlungen()
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
# Stapel 2017-ea-A (Reserve, geöffnet 16.09.2026 wegen der Landesheftverweise:
# 2017-bb-ea Teil 1 = Analysis 1.1, AG/LA (A2) 2, Stochastik 2). Elf Dateien zu
# je 5 BE, Bewertungshinweise ohne AB-Spalte (Teil A).
row("2017MerhoehtAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Nullstelle einer Exponentialfunktion durch Logarithmieren bestimmen", typ_neben="",
    stichwoerter="f(x) = 2e^(x/2) − 1|e^(x/2) = 1/2|x = 2 · ln(1/2) = −2 ln 2",
    voraussetzungen="Exponentialgleichung nach der Exponentialfunktion auflösen|Logarithmieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktion f mit f(x) = 2 · e^(1/2 · x) − 1, x ∈ IR",
    gesucht="Nullstelle von f",
    verfahren="f(x) = 0 nach e^(x/2) auflösen und logarithmieren",
    schritte="3", zahlenraum="Bruch|dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="2e^(x/2) − 1 = 0 ⇔ x = 2 · ln(1/2) (amtlich); x = −2 ln 2 ≈ −1,39",
    zwischenergebnis="e^(x/2) = 1/2", niveau_geschaetzt="I",
    fehlerquelle="den Faktor 2 vor der Exponentialfunktion beim Logarithmieren mitziehen",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2017-bb-ea Teil 1 (Analysis a); Typ von dort übernommen.")
row("2017MerhoehtAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Gleichschenkligkeit des Dreiecks aus Tangente und Koordinatenachsen allgemein begründen",
    typ_neben="Tangentengleichung in einem Punkt des Graphen aufstellen",
    stichwoerter="f'(x) = e^(x/2), f'(0) = 1|Tangente in S(0 | 1) mit Steigung 1|Winkel 45° an der x-Achse|zwei gleiche Winkel",
    voraussetzungen="Ableitung der e-Funktion mit Kettenregel|Steigung als Winkel deuten oder Achsenabschnitte vergleichen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 2 · e^(1/2 · x) − 1; die Tangente an den Graphen in S(0 | 1) begrenzt mit den Koordinatenachsen ein Dreieck",
    gesucht="Nachweis, dass dieses Dreieck gleichschenklig ist",
    verfahren="f'(0) = 1, also schließt die Tangente mit der x-Achse 45° ein; wegen des rechten Winkels im Ursprung ist auch der dritte Winkel 45°",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = e^(x/2), f'(0) = 1; ein Winkel des Dreiecks ist 45°, wegen des rechten Winkels der Achsen auch der dritte, also stimmen zwei Winkel überein (amtlich)",
    zwischenergebnis="t: y = x + 1, Achsenschnittpunkte (−1 | 0) und (0 | 1)", niveau_geschaetzt="II",
    fehlerquelle="die Gleichschenkligkeit ohne Steigung oder Achsenabschnitte behaupten",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2017-bb-ea Teil 1 (Analysis b); Typ von dort übernommen, der Erwartungshorizont argumentiert über die Winkel statt über die Achsenabschnitte.")
row("2017MerhoehtAAnalysis12", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate aus dem Funktionsterm im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="n(t) = 3t² − 60t + 500|Differenzenquotient (n(2) − n(0))/2 = (392 − 500)/2|−54 Pollen je Kubikmeter und Stunde",
    voraussetzungen="Funktionswerte berechnen|Differenzenquotient als mittlere Änderungsrate",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Messstation/Pollen", textumfang="mittel",
    gegeben="Anzahl der Pollen pro Kubikmeter zum Zeitpunkt t (Stunden nach Messbeginn): n(t) = 3t² − 60t + 500, 0 ≤ t ≤ 10",
    gesucht="mittlere Änderung der Pollenanzahl pro Kubikmeter und Stunde in den ersten beiden Stunden",
    verfahren="Differenzenquotient über [0; 2]",
    schritte="2", zahlenraum="ganz|negativ", einheiten="Pollen je m³ und h", abhaengig_von="",
    ergebnis="(n(2) − n(0))/2 = (392 − 500)/2 = −54 (amtlich); die Anzahl nimmt im Mittel um 54 Pollen pro Kubikmeter und Stunde ab",
    zwischenergebnis="n(2) = 392", niveau_geschaetzt="II",
    fehlerquelle="die Ableitung an einer Stelle statt des Differenzenquotienten nehmen",
    bemerkung="Standardbezug: K3 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt. Der Funktionsterm ist am gerenderten Blatt geprüft (Textextraktion vertauscht die Vorzeichen).")
row("2017MerhoehtAAnalysis12", "b", seite="1|2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Stelle mit vorgegebener momentaner Änderungsrate über die Ableitung berechnen", typ_neben="",
    stichwoerter="n'(t) = 6t − 60|n'(t) = −30 ⇔ t = 5|fünf Stunden nach Messbeginn",
    voraussetzungen="Ableitung als momentane Änderungsrate|lineare Gleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Messstation/Pollen", textumfang="kurz",
    gegeben="n(t) = 3t² − 60t + 500, 0 ≤ t ≤ 10",
    gesucht="Zeitpunkt, zu dem die momentane Änderungsrate −30 Pollen pro Kubikmeter und Stunde beträgt",
    verfahren="n'(t) = 6t − 60 gleich −30 setzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="h", abhaengig_von="",
    ergebnis="n'(t) = 6t − 60; n'(t) = −30 ⇔ t = 5; fünf Stunden nach Beginn der Messung (amtlich)",
    zwischenergebnis="n'(t) = 6t − 60", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen der Änderungsrate verwechseln (n'(t) = 30 liefert t = 15, außerhalb des Bereichs)",
    bemerkung="Standardbezug: K3 II, K5 I, K6 II. Amtlich, eigene Rechnung bestätigt.")
row("2017MerhoehtAAnalysis2", "a", seite="1|2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Flächeninhalt zwischen Graph, x-Achse und senkrechter Gerade über das Integral nachweisen", typ_neben="",
    stichwoerter="f(x) = −x³ + 12x|Integral von 0 bis 2|Stammfunktion −x⁴/4 + 6x²|Wert 20",
    voraussetzungen="Stammfunktion ganzrationaler Terme|Hauptsatz",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit dem Graphen von f(x) = −x³ + 12x im Bereich von etwa −1 bis 4, Hochpunkt H(2 | 16) markiert und beschriftet; der Graph steigt vom Ursprung zu H und fällt danach durch die Nullstelle bei √12 ≈ 3,5.",
    kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −x³ + 12x, x ∈ IR, mit Hochpunkt H(2 | 16); Graph, x-Achse und die Gerade x = 2 schließen für 0 ≤ x ≤ 2 eine Fläche ein",
    gesucht="Nachweis, dass diese Fläche den Inhalt 20 hat",
    verfahren="Integral von 0 bis 2 über f berechnen",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="∫ von 0 bis 2 f(x) dx = [−x⁴/4 + 6x²] von 0 bis 2 = 20 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Stammfunktion von 12x als 12x² ansetzen",
    bemerkung="Standardbezug: K4 I, K5 II. Amtlich, eigene Rechnung bestätigt.")
row("2017MerhoehtAAnalysis2", "b", seite="1|2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Achsenschnittpunkt einer Geraden aus einer Flächenbedingung über Rechteck und Dreieck bestimmen", typ_neben="",
    stichwoerter="Gerade g durch H(2 | 16) mit negativer Steigung|Fläche zwischen Graph, y-Achse und g gleich 20|Rechteck 2 · 16 = 32, davon 20 unter dem Graphen, also 12 über dem Graphen|Dreieck zwischen y = 16 und g mit Inhalt 8: 1/2 · 2 · h = 8|Schnittpunkt (0 | 24)",
    voraussetzungen="Flächen zerlegen (Rechteck, Dreieck)|Ergebnis aus a nutzen|Dreiecksfläche",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze="Wie in a: Graph von f mit Hochpunkt H(2 | 16).", kontext="ohne", textumfang="mittel",
    gegeben="f(x) = −x³ + 12x mit H(2 | 16); Fläche unter dem Graphen über [0; 2] ist 20 (aus a); Gerade g durch H mit negativer Steigung; Graph, y-Achse und g schließen für 0 ≤ x ≤ 2 eine Fläche mit dem Inhalt 20 ein",
    gesucht="Koordinaten des Schnittpunkts von g mit der y-Achse",
    verfahren="Die Fläche zwischen Graph, y-Achse und y = 16 ist 2 · 16 − 20 = 12; die Fläche zwischen y = 16, y-Achse und g muss dann 20 − 12 = 8 sein, ein Dreieck mit Grundseite 2 (auf y = 16) und Höhe h auf der y-Achse: 1/2 · 2 · h = 8",
    schritte="4", zahlenraum="ganz", einheiten="", abhaengig_von="2017MerhoehtAAnalysis2-a",
    ergebnis="h = 8, Schnittpunkt (0 | 24) (amtlich)",
    zwischenergebnis="Fläche zwischen Graph und y = 16 über [0; 2]: 12|Dreiecksfläche 8", niveau_geschaetzt="III",
    fehlerquelle="die Flächenbedingung als Integral über g − f ansetzen und an der unbekannten Steigung scheitern",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Flächenbedingung in eine Zerlegung Rechteck minus Integral plus Dreieck übersetzen, verkettet mit der Dreiecksfläche.")
row("2017MerhoehtAAGLAA111", "a", seite="1|2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lineares Gleichungssystem mit drei Variablen lösen", typ_neben="",
    stichwoerter="3x1 − 2x2 = 13, x2 + 2x3 = 5, x2 + x3 = 3|x3 = 2, x2 = 1, x1 = 5|Lösungsmenge {(5; 1; 2)}",
    voraussetzungen="Gleichungssystem durch Einsetzen oder Subtraktion lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Gleichungssystem 3x1 − 2x2 = 13; x2 + 2x3 = 5; x2 + x3 = 3",
    gesucht="Lösungsmenge",
    verfahren="Zweite minus dritte Gleichung liefert x3, dann x2, dann x1",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="{(5; 1; 2)} (amtlich)",
    zwischenergebnis="x3 = 2, x2 = 1", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen beim Auflösen von 3x1 − 2x2 = 13",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt.")
row("2017MerhoehtAAGLAA111", "b", seite="1|2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lineare Gleichungssysteme",
    typ="Lösbarkeit eines Gleichungssystems mit Parameter beurteilen", typ_neben="",
    stichwoerter="3x1 + 2x2 + x3 = 4, 3x1 + 2x2 = 5, 3x1 + 2x2 + p x3 = 4|p = 1: erste und dritte Gleichung gleich, unendlich viele Lösungen|p ≠ 1: (1 − p) x3 = 0, also x3 = 0, dann 4 = 5 Widerspruch|nie genau eine Lösung",
    voraussetzungen="Gleichungen vergleichen und subtrahieren|Fallunterscheidung nach dem Parameter",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Zeigen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Gleichungssystem 3x1 + 2x2 + x3 = 4; 3x1 + 2x2 = 5; 3x1 + 2x2 + p · x3 = 4 mit p ∈ IR",
    gesucht="ein Wert von p mit unendlich vielen Lösungen; Nachweis, dass es keinen Wert von p mit genau einer Lösung gibt",
    verfahren="Für p = 1 stimmen erste und dritte Gleichung überein; für p ≠ 1 liefert die Differenz x3 = 0 und damit den Widerspruch 4 = 5 zwischen erster und zweiter Gleichung",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="p = 1 (unendlich viele Lösungen); für p ≠ 1 keine Lösung, also nie genau eine (amtlich)",
    zwischenergebnis="(1 − p) · x3 = 0", niveau_geschaetzt="II",
    fehlerquelle="nur p = 1 prüfen und den allgemeinen Fall p ≠ 1 nicht ausführen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-A); hier zusätzlich der Nachweis, dass keine eindeutige Lösung möglich ist.")
row("2017MerhoehtAAGLAA112", "a", seite="1|2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsmatrix aus dem Übergangsdiagramm aufstellen", typ_neben="",
    stichwoerter="vier Räume R1 bis R4|Pfeile R1→R2 1; R2→R1 0,7; R2→R3 0,3; R3→R2 0,8; R3→R4 0,2; R4→R3 0,6; R4→R4 0,4|Spalten summieren sich zu 1",
    voraussetzungen="Spalte = Ausgangszustand, Zeile = Zielzustand|Diagramm lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Diagramm",
    skizze="Übergangsdiagramm mit vier Kreisen R1, R2, R3, R4 in einer Reihe; Pfeile: R1→R2 mit 1, R2→R1 mit 0,7, R2→R3 mit 0,3, R3→R2 mit 0,8, R3→R4 mit 0,2, R4→R3 mit 0,6, Schleife an R4 mit 0,4.",
    kontext="Labor/Ratten", textumfang="mittel",
    gegeben="Übergangsdiagramm für das Wechseln von Ratten zwischen vier Räumen R1 bis R4 (Anteile je Beobachtungsschritt wie in der Skizze)",
    gesucht="zugehörige Übergangsmatrix",
    verfahren="Anteile spaltenweise nach Ausgangsraum eintragen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="M = ((0; 0,7; 0; 0), (1; 0; 0,8; 0), (0; 0,3; 0; 0,6), (0; 0; 0,2; 0,4)) mit Spalten als Ausgangsräume (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauschen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. Amtlich, eigene Rechnung bestätigt.")
row("2017MerhoehtAAGLAA112", "b", seite="1|2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Diagramm der zeitlichen Entwicklung eines Zustands aus dem Übergangsdiagramm auswählen und begründen", typ_neben="",
    stichwoerter="Start: 50 Ratten in R1|Zeitpunkt 1: alle in R2|Zeitpunkt 2: keine in R2, 35 in R1|Zeitpunkt 3: keine in R1|nur Abbildung II hat 0 bei t = 3",
    voraussetzungen="Erste Schritte des Prozesses aus dem Diagramm verfolgen|Punktdiagramme lesen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm",
    skizze="Drei Punktdiagramme I, II, III: waagerecht Beobachtungszeitpunkt 0 bis 10, senkrecht Anzahl Ratten in R1 von 0 bis 60. I: 50 bei 0, dann etwa 35 und konstant um 33. II: 50 bei 0, 0 bei 1, 35 bei 2, 0 bei 3, dann abwechselnd etwa 33 und 0. III: 50 bei 0, dann zwischen 20 und 45 schwankend ansteigend.",
    kontext="Labor/Ratten", textumfang="mittel",
    gegeben="Übergangsdiagramm aus a; zu Beginn 50 Ratten in R1, die anderen Räume leer; drei Abbildungen mit möglichen Verläufen der Anzahl in R1",
    gesucht="die passende Abbildung mit Begründung",
    verfahren="Erste Schritte durchrechnen: Zeitpunkt 1 alle in R2, Zeitpunkt 2 keine in R2 (35 in R1, 15 in R3), Zeitpunkt 3 keine in R1; nur Abbildung II zeigt 0 zum Zeitpunkt 3",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="2017MerhoehtAAGLAA112-a",
    ergebnis="Abbildung II: zum Zeitpunkt 1 alle Ratten in R2, zum Zeitpunkt 2 keine in R2, zum Zeitpunkt 3 keine in R1 – das erfüllt nur II (amtlich)",
    zwischenergebnis="Verteilung nach 2 Schritten (35; 0; 15; 0)", niveau_geschaetzt="II",
    fehlerquelle="Abbildung I wählen, weil der Wert 35 zum Zeitpunkt 2 passt, ohne den Zeitpunkt 3 zu prüfen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II. Amtlich, eigene Rechnung bestätigt.")
row("2017MerhoehtAAGLAA211", "a", seite="1|2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen", typ_neben="",
    stichwoerter="E: x1 + x2 + 2x3 = 4|x1 = 0: x2 + 2x3 = 4|Spurpunkte (0 | 4 | 0) und (0 | 0 | 2)|Gerade durch beide einzeichnen",
    voraussetzungen="Koordinatenebene durch x1 = 0 beschreiben|Achsenschnittpunkte aus der Koordinatengleichung",
    format="Zeichnen", operator="Zeichnen Sie ein", antwort="Grafik",
    material="Koordinatensystem",
    skizze="Schrägbild eines räumlichen Koordinatensystems mit x1-Achse nach vorn links, x2-Achse nach rechts, x3-Achse nach oben, jeweils bis 5 mit Teilstrichen und der Beschriftung 5 an den Achsen.",
    kontext="ohne", textumfang="kurz",
    gegeben="Ebene E: x1 + x2 + 2x3 = 4 und die Gerade g: x = (2; 1; −2) + λ · (2; −1; −3); Schrägbild eines Koordinatensystems",
    gesucht="Schnittgerade von E mit der x2x3-Ebene in der Abbildung",
    verfahren="x1 = 0 setzen, die Spurpunkte auf der x2- und der x3-Achse bestimmen und verbinden",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Gerade in der x2x3-Ebene durch (0 | 4 | 0) und (0 | 0 | 2), als Zeichnung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Spurgerade in der x1x2-Ebene zeichnen",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. Amtlich (Erwartungshorizont zeigt die Zeichnung), eigene Rechnung bestätigt.")
row("2017MerhoehtAAGLAA211", "b", seite="1|2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schnittpunkt von Gerade und Ebene berechnen", typ_neben="",
    stichwoerter="g in E einsetzen: (2 + 2λ) + (1 − λ) + 2(−2 − 3λ) = 4|λ = −1|S(0 | 2 | 1)",
    voraussetzungen="Parameterform in die Koordinatengleichung einsetzen|lineare Gleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: x1 + x2 + 2x3 = 4; g: x = (2; 1; −2) + λ · (2; −1; −3), λ ∈ IR",
    gesucht="Koordinaten des Schnittpunkts von E und g",
    verfahren="Koordinaten von g in E einsetzen, λ bestimmen, Punkt berechnen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(2 + 2λ) + (1 − λ) + 2 · (−2 − 3λ) = 4 ⇔ λ = −1; Schnittpunkt (0 | 2 | 1) (amtlich)",
    zwischenergebnis="λ = −1", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen bei 2 · (−2 − 3λ)",
    bemerkung="Standardbezug: K5 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2019-ea-A).")
row("2017MerhoehtAAGLAA212", "a", seite="1|2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines rechtwinkligen Dreiecks über die Kathetenlängen nachweisen", typ_neben="",
    stichwoerter="A(3 | 3 | 3), B(6 | 7 | 3), C(2 | 10 | 3), rechter Winkel bei B|AB = (3; 4; 0), BC = (−4; 3; 0)|beide Länge 5|Fläche 1/2 · 5 · 5 = 25/2",
    voraussetzungen="Betrag eines Vektors|Fläche des rechtwinkligen Dreiecks aus den Katheten",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Dreieck ABC mit A(3 | 3 | 3), B(6 | 7 | 3), C(2 | 10 | 3), rechtwinklig bei B, in der Ebene z = 3",
    gesucht="Nachweis, dass das Dreieck den Flächeninhalt 25/2 hat",
    verfahren="Katheten |AB| und |BC| berechnen, halbes Produkt",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="|AB| = |BC| = 5, A = 1/2 · 5 · 5 = 25/2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Hypotenuse als Kathete nehmen",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt.")
row("2017MerhoehtAAGLAA212", "b", seite="1|2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Höhe einer Pyramide aus dem Volumen bestimmen", typ_neben="",
    stichwoerter="V = 1/3 · 25/2 · h = 25 ⇔ h = 6|Dreieck in z = 3, Höhe senkrecht dazu|D(3 | 3 | 9) (eine Möglichkeit)",
    voraussetzungen="Pyramidenvolumen 1/3 · G · h|Höhe senkrecht zur Ebene z = 3 als z-Verschiebung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Dreieck ABC (Fläche 25/2, in der Ebene z = 3) als Grundfläche einer Pyramide ABCD",
    gesucht="Koordinaten eines Punktes D, für den das Volumen 25 ist",
    verfahren="Höhe aus V = 1/3 · G · h, dann einen Punkt in der Höhe 6 über der Ebene z = 3 wählen",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2017MerhoehtAAGLAA212-a",
    ergebnis="1/3 · 25/2 · h = 25 ⇔ h = 6; mögliche Koordinaten (3 | 3 | 9) (amtlich)",
    zwischenergebnis="h = 6", niveau_geschaetzt="II",
    fehlerquelle="D in der Ebene z = 3 wählen (Volumen null) oder h = 2 aus 25 = 25/2 · h",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-A): hier ist die Grundfläche achsenparallel, die Höhe eine z-Verschiebung, kein Skalarprodukt nötig.")
row("2017MerhoehtAAGLAA22", "a", seite="1|2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines Dreiecks aus den Spurpunkten einer Ebene berechnen",
    typ_neben="Spurpunkte einer Ebene auf den Koordinatenachsen bestimmen",
    stichwoerter="E: 2x1 + x2 − 2x3 = −18|Spurpunkte (−9 | 0 | 0) und (0 | −18 | 0)|rechtwinkliges Dreieck am Ursprung|Fläche 1/2 · 9 · 18 = 81",
    voraussetzungen="Spurpunkte durch Nullsetzen|Fläche des rechtwinkligen Dreiecks",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Ebene E: 2x1 + x2 − 2x3 = −18; Dreieck aus den Schnittpunkten von E mit der x1- und der x2-Achse und dem Ursprung",
    gesucht="Flächeninhalt des Dreiecks",
    verfahren="Spurpunkte bestimmen, Katheten 9 und 18",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Spurpunkte (−9 | 0 | 0) und (0 | −18 | 0); Flächeninhalt 1/2 · 9 · 18 = 81 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="negative Achsenabschnitte als negative Längen einsetzen",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2017-bb-ea Teil 1 (Geometrie a); Typen von dort übernommen.")
row("2017MerhoehtAAGLAA22", "b", seite="1|2", punkte="3", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Normalenvektor als Ortsvektor eines Ebenenpunktes bestimmen", typ_neben="",
    stichwoerter="Normalenvektoren r · (2; 1; −2), r ≠ 0|als Punkt in E: 2 · 2r + r − 2 · (−2r) = −18 ⇔ r = −2|(−4; −2; 4)",
    voraussetzungen="Normalenvektor aus der Koordinatenform|Vielfache ansetzen|Punktprobe",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Ebene E: 2x1 + x2 − 2x3 = −18",
    gesucht="Koordinaten des Vektors, der Normalenvektor von E und Ortsvektor eines Punktes von E ist",
    verfahren="Ansatz r · (2; 1; −2) in die Ebenengleichung einsetzen, r bestimmen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="9r = −18 ⇔ r = −2; Vektor (−4; −2; 4) (amtlich)",
    zwischenergebnis="Ansatz r · (2; 1; −2)", niveau_geschaetzt="III",
    fehlerquelle="den Normalenvektor (2; 1; −2) selbst einsetzen und aus dem Widerspruch auf Unlösbarkeit schließen",
    bemerkung="Standardbezug: K2 III, K5 III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Doppelbedingung Normalenvektor und Ortsvektor in den Ansatz r · n als Ebenenpunkt übersetzen. Wortgleich im Landesheft 2017-bb-ea Teil 1 (Geometrie b); Typ von dort übernommen.")
row("2017MerhoehtAStochastik11", "a", seite="1|2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="Glücksrad, P(blau) = p|Term (1 − p)^7|bei sieben Drehungen nie blau",
    voraussetzungen="Gegenwahrscheinlichkeit|Potenz als Produkt unabhängiger Wiederholungen",
    format="Kurzantwort", operator="Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="kurz",
    gegeben="Glücksrad mit blauem, gelbem und rotem Sektor; P(blau) = p beim einmaligen Drehen; Term (1 − p)^7",
    gesucht="Bedeutung des Terms im Sachzusammenhang",
    verfahren="1 − p als Wahrscheinlichkeit für nicht blau, Potenz 7 als sieben Drehungen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Wahrscheinlichkeit, dass bei sieben Drehungen der blaue Sektor nicht getroffen wird (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="„genau einmal nicht blau“ statt „nie blau“",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II. Amtlich.")
row("2017MerhoehtAStochastik11", "b", seite="1|2", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Term für eine Wahrscheinlichkeit einer Bernoulli-Kette angeben", typ_neben="",
    stichwoerter="zehnmal drehen|genau zweimal blau|C(10; 2) · p² · (1 − p)^8",
    voraussetzungen="Bernoulli-Formel",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="kurz",
    gegeben="Glücksrad mit P(blau) = p, zehn Drehungen",
    gesucht="Term für die Wahrscheinlichkeit, dass der blaue Sektor genau zweimal getroffen wird",
    verfahren="Bernoulli-Formel mit n = 10, k = 2",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="C(10; 2) · p² · (1 − p)^8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Binomialkoeffizient vergessen",
    bemerkung="Standardbezug: K3 I, K5 I. Amtlich. Typ wiederverwendet.")
row("2017MerhoehtAStochastik11", "c", seite="1|2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen", typ_neben="",
    stichwoerter="P(gelb) = 50 %|100 Drehungen mit deutlich weniger als 50 % gelb|Folgerung „nächste 100 deutlich mehr als 50 %“|falsch: jede Drehung hat dieselbe Wahrscheinlichkeit",
    voraussetzungen="Unabhängigkeit der Wiederholungen|Wahrscheinlichkeit ist keine Ausgleichsregel",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksrad", textumfang="mittel",
    gegeben="P(gelb) = 50 % je Drehung; nach 100 Drehungen mit deutlich weniger als 50 % gelb folgert Felix, dass bei den nächsten 100 Drehungen der Anteil deutlich größer als 50 % sein muss",
    gesucht="Beurteilung der Aussage",
    verfahren="Die Wahrscheinlichkeit für gelb ist bei jeder Drehung gleich groß und hängt nicht von früheren Drehungen ab",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist falsch, weil die Wahrscheinlichkeit für den gelben Sektor bei allen Drehungen gleich groß ist (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das empirische Gesetz der großen Zahlen als Ausgleichspflicht der nächsten Versuche lesen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. Amtlich. Thema Unabhängigkeit (Unabhängigkeit der Drehungen); keine Klasse unter Zufallsexperimente passt.")
row("2017MerhoehtAStochastik12", "a", seite="1|2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen", typ_neben="",
    stichwoerter="Anteil mit Figur 25 %|zehn Eier, nur die letzten beiden mit Figur|0,75^8 · 0,25²",
    voraussetzungen="Feste Reihenfolge als Produkt der Einzelwahrscheinlichkeiten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Überraschungseier", textumfang="kurz",
    gegeben="Anteil der Überraschungseier mit Figur 25 %; zehn Eier werden nacheinander zufällig ausgewählt",
    gesucht="Term für die Wahrscheinlichkeit, dass nur in den letzten beiden Eiern eine Figur ist",
    verfahren="acht Misserfolge, dann zwei Erfolge in fester Reihenfolge multiplizieren",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="0,75^8 · 0,25² (amtlich); ≈ 0,0063",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Binomialkoeffizient C(10; 2) ergänzen, obwohl die Reihenfolge festliegt",
    bemerkung="Standardbezug: K3 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2019-ea-A), hier als Term ohne Zahlenwert.")
row("2017MerhoehtAStochastik12", "b", seite="1|2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen", typ_neben="",
    stichwoerter="X: Figuren unter sechs Eiern, B(6; 0,25)|E(X) = 1,5|Abbildung I passt|II Gleichverteilung|III Erwartungswert größer als 1,5",
    voraussetzungen="Erwartungswert n · p|Form einer Binomialverteilung",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm",
    skizze="Drei Säulendiagramme P(X = k) für k = 0 bis 6, Achse bis 0,4. I: Säulen 0,18, 0,36, 0,30, 0,13, 0,03, nahe 0, nahe 0 (Maximum bei 1). II: sieben gleich hohe Säulen 0,14. III: Säulen 0, 0,02, 0,12, 0,30, 0,36, 0,18, 0,03 (Maximum bei 4).",
    kontext="Überraschungseier", textumfang="mittel",
    gegeben="X: Anzahl der Eier mit Figur unter sechs zufällig ausgewählten (p = 0,25); drei Abbildungen, eine zeigt die Verteilung von X",
    gesucht="die passende Abbildung; Begründung, dass die beiden anderen nicht passen",
    verfahren="Erwartungswert 6 · 0,25 = 1,5: Abbildung II ist eine Gleichverteilung, Abbildung III hat einen Erwartungswert größer als 1,5",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Abbildung I; X ist binomialverteilt mit E(X) = 1,5, II zeigt eine Gleichverteilung, III eine Verteilung mit größerem Erwartungswert (amtlich)",
    zwischenergebnis="E(X) = 1,5", niveau_geschaetzt="II",
    fehlerquelle="Abbildung III wählen, weil sie wie eine Binomialverteilung aussieht",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2021-ga-A).")
row("2017MerhoehtAStochastik2", "a", seite="1|2", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit bei zweistufigem Umlegen zwischen Urnen berechnen", typ_neben="",
    stichwoerter="Urne A 2 weiß 2 schwarz, B 2 weiß 1 schwarz, C 2 weiß|Kugel von A nach B, dann von B nach C|C hat zwei weiße und eine schwarze, wenn die zweite Kugel schwarz ist|1/2 · 1/2 + 1/2 · 1/4 = 3/8",
    voraussetzungen="Pfadregeln|veränderten Urneninhalt nach dem Umlegen berücksichtigen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Figur",
    skizze="Drei nach oben offene Urnen nebeneinander, beschriftet Urne A, Urne B, Urne C: A mit zwei weißen und zwei schwarzen Kugeln, B mit zwei weißen und einer schwarzen, C mit zwei weißen; schwarze Kugeln ausgefüllt.",
    kontext="Urne/Kugeln", textumfang="mittel",
    gegeben="Urne A: 2 weiße, 2 schwarze Kugeln; Urne B: 2 weiße, 1 schwarze; Urne C: 2 weiße. Aus A wird eine Kugel zufällig in B gelegt, dann aus B eine Kugel zufällig in C",
    gesucht="Wahrscheinlichkeit, dass danach in C zwei weiße und eine schwarze Kugel liegen",
    verfahren="Zweite Kugel muss schwarz sein: Pfad schwarz–schwarz 1/2 · 2/4, Pfad weiß–schwarz 1/2 · 1/4",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/2 · 1/2 + 1/2 · 1/4 = 3/8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit unverändertem Inhalt von B rechnen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2017-bb-ea Teil 1 (Stochastik a); Typ von dort übernommen.")
row("2017MerhoehtAStochastik2", "b", seite="1|2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen",
    typ_neben="Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen",
    stichwoerter="Einsatz 1 Euro, Urne zufällig, Kugel zufällig|P(schwarz) = 1/3 · 1/2 + 1/3 · 1/3 = 5/18|5/18 · (x − 1) + 13/18 · (−1) = 0|x = 3,60 Euro",
    voraussetzungen="totale Wahrscheinlichkeit|Erwartungswert des Gewinns null setzen|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur", skizze="Wie in a: drei Urnen A, B, C mit ihren Kugeln.", kontext="Glücksspiel/Urnen", textumfang="mittel",
    gegeben="Urnen wie in a; Spiel: Einsatz 1 Euro, eine der drei Urnen wird zufällig gewählt, daraus eine Kugel gezogen; nur bei schwarz wird ein Betrag x ausgezahlt",
    gesucht="Betrag, bei dem auf lange Sicht Einsätze und Auszahlungen ausgeglichen sind",
    verfahren="P(schwarz) über die drei gleich wahrscheinlichen Urnen, Erwartungswert des Gewinns gleich null setzen",
    schritte="4", zahlenraum="Bruch|dezimal", einheiten="Euro", abhaengig_von="",
    ergebnis="P(schwarz) = 5/18; 5/18 · (x − 1) + 13/18 · (−1) = 0 ⇔ x = 3,6; der Betrag muss 3,60 Euro sein (amtlich)",
    zwischenergebnis="P(schwarz) = 5/18", niveau_geschaetzt="II",
    fehlerquelle="die drei Urnenwahrscheinlichkeiten ohne Gewichtung 1/3 addieren",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. Amtlich, eigene Rechnung bestätigt. Geschätzt II nach der engen Fassung (Fairness als Erwartungswert gleich Einsatz ist von der Deutungsliste gestrichen); amtlich III – dritter Beleg für „faires Spiel“ mit III gegen zwei mit II. Wortgleich im Landesheft 2017-bb-ea Teil 1 (Stochastik b); Typen von dort übernommen.")

NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Mittlere Änderungsrate aus dem Funktionsterm im Sachzusammenhang berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Den Differenzenquotienten einer Funktion über ein vorgegebenes Intervall aus den Funktionswerten des Terms berechnen und als mittlere Änderung je Zeiteinheit im Sachzusammenhang angeben.",
     "2017MerhoehtAAnalysis12-a"),
    ("Stelle mit vorgegebener momentaner Änderungsrate über die Ableitung berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Die Stelle bestimmen, an der die Ableitung einen vorgegebenen Wert annimmt (Ableitung bilden, Gleichung lösen), und sie im Sachzusammenhang als Zeitpunkt deuten.",
     "2017MerhoehtAAnalysis12-b"),
    ("Fläche: Flächeninhalt zwischen Graph, x-Achse und senkrechter Gerade über das Integral nachweisen", "Analysis", "Flächeninhalt durch Integration",
     "Den vorgegebenen Inhalt einer Fläche zwischen Graph, x-Achse und einer senkrechten Geraden durch Berechnen des bestimmten Integrals über eine Stammfunktion bestätigen.",
     "2017MerhoehtAAnalysis2-a"),
    ("Fläche: Achsenschnittpunkt einer Geraden aus einer Flächenbedingung über Rechteck und Dreieck bestimmen", "Analysis", "Flächeninhalt durch Integration",
     "Den Achsenschnittpunkt einer Geraden durch einen Graphenpunkt so bestimmen, dass eine Fläche zwischen Graph, Achse und Gerade einen vorgegebenen Inhalt hat, indem die Fläche in Rechteck, bekanntes Integral und Dreieck zerlegt wird.",
     "2017MerhoehtAAnalysis2-b"),
    ("Lineares Gleichungssystem mit drei Variablen lösen", "Analytische Geometrie", "Lineare Gleichungssysteme",
     "Ein lineares Gleichungssystem mit drei Gleichungen und drei Variablen durch Einsetzen oder Subtraktion lösen und die Lösungsmenge angeben.",
     "2017MerhoehtAAGLAA111-a"),
    ("Übergangsprozess: Übergangsmatrix aus dem Übergangsdiagramm aufstellen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus einem Übergangsdiagramm mit mehreren Zuständen die vollständige Übergangsmatrix aufstellen (Spalten als Ausgangszustände, Spaltensummen 1).",
     "2017MerhoehtAAGLAA112-a"),
    ("Übergangsprozess: Diagramm der zeitlichen Entwicklung eines Zustands aus dem Übergangsdiagramm auswählen und begründen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Unter mehreren Punktdiagrammen das auswählen, das die Entwicklung eines Zustands beschreibt, indem die ersten Schritte des Prozesses aus dem Übergangsdiagramm verfolgt und mit den Diagrammen verglichen werden.",
     "2017MerhoehtAAGLAA112-b"),
    ("Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen", "Analytische Geometrie", "Schnittmengen",
     "Die Schnittgerade einer Ebene in Koordinatenform mit einer Koordinatenebene über ihre beiden Spurpunkte auf den Achsen bestimmen und in ein Schrägbild einzeichnen.",
     "2017MerhoehtAAGLAA211-a"),
    ("Ebene Figur: Flächeninhalt eines rechtwinkligen Dreiecks über die Kathetenlängen nachweisen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Für ein Dreieck mit bekanntem rechten Winkel die beiden Katheten als Vektorbeträge berechnen und den Flächeninhalt als halbes Produkt nachweisen.",
     "2017MerhoehtAAGLAA212-a"),
    ("Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen", "Stochastik", "Unabhängigkeit",
     "Eine Aussage, nach der ein zu kleiner beobachteter Anteil bei den nächsten Versuchen durch einen zu großen ausgeglichen werden müsse, als falsch beurteilen, weil die Einzelwahrscheinlichkeit bei jeder Wiederholung gleich bleibt.",
     "2017MerhoehtAStochastik11-c"),
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
# Verweise aus abi-katalog.csv auf Poolzeilen (abi.md § 7; v1.2 gezählt als Landesverwendung)
MARKE_DUBLETTE = re.compile(r"Dublette von: (" + KENNUNG.pattern + r"(?:-\d*[a-z]?)?)")
MARKE_POOL_OFFEN = re.compile(r"Poolaufgabe \(nicht erfasst(, abgewandelt)?\): (" + KENNUNG.pattern + r"(?:-\d*[a-z]?)?)")


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
    TYP_THEMA.update({r[0]: (r[1], r[2]) for r in alt_typ})
    TYP_THEMA.update({t[0]: (t[1], t[2]) for t in NEUE_TYPEN if len(t) == 5})
    # andere Kataloge derselben Typenliste (Entscheidung 25): ids und verwendete Typen
    andere = [dict(zip(HEAD, r)) for p in ANDERE_KATALOGE for r in lade(p, HEAD)[1]]
    andere_ids = {z["id"] for z in andere}
    andere_typen = set()
    for z in andere:
        andere_typen |= typen_von(z)
    # Landesverwendung (v1.2): abi-Zeilen, die auf eine Poolzeile verweisen – als
    # „Dublette von: <id>" (erfasst) oder „Poolaufgabe (nicht erfasst): <id>" (vorgemerkt)
    verweis, vorgemerkt = {}, {}
    for z in andere:
        m = MARKE_DUBLETTE.search(z["bemerkung"])
        if m:
            verweis.setdefault(m.group(1), []).append(z["id"])
        m = MARKE_POOL_OFFEN.search(z["bemerkung"])
        if m:
            vorgemerkt.setdefault(m.group(2), []).append(z["id"])
    print(f"Vokabular: {len(HEAD)} Felder, {len(LEITIDEEN)} Sachgebiete, "
          f"{sum(len(v) for v in THEMEN.values())} Themen – gelesen aus {KERN} und {VOKABULAR}; "
          f"{len(QUELLE)} Kennungen aus {QUELLEN}; {len(andere)} Zeilen aus {ANDERE_KATALOGE}")

    # ---- Selbstprüfung: kein neuer Stapel, nur die vorhandenen Zeilen prüfen
    if not ZEILEN:
        for z in alt:
            a(len(z) == len(HEAD), f"{z.get('id')}: Feldzahl weicht ab")
            pruefe_zeile(z, a)
        typ_namen = {r[0] for r in alt_typ}
        a(len(typ_namen) == len(alt_typ), "doppelter Typ in der Typenliste")
        benutzt = set(andere_typen)
        for z in alt:
            for t in typen_von(z):
                benutzt.add(t)
                a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
            pruefe_thema(z, a)
        a(not (typ_namen - benutzt), f"Typen unbenutzt: {sorted(typ_namen - benutzt)}")
        ids = {z["id"] for z in alt}
        a(len(ids) == len(alt), "doppelte id im Katalog")
        a(not (ids & andere_ids), f"ids auch in einem anderen Katalog: {sorted(ids & andere_ids)[:5]}")
        for z in alt:
            for dep in [s for s in z["abhaengig_von"].split("|") if s]:
                a(dep in ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
        for r in alt_typ:
            a(r[1] in THEMEN and r[2] in THEMEN.get(r[1], []),
              f"Typ {r[0]}: Sachgebiet oder Thema unbekannt")
            a(r[4] in ids or r[4] in andere_ids, f"Typ {r[0]}: beispiel_id in keinem Katalog")
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
        for pid in verweis:
            a(pid in ids, f"abi-Verweis auf {pid}, aber die Zeile steht nicht im Katalog")
        if fehler:
            print(f"\nSelbstprüfung: {len(fehler)} Fehler")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        treffer, abw, gew = eichung(alt)
        treffer_eng, _, _ = eichung(alt, eng=True)
        eigene = set()
        for z in alt:
            eigene |= typen_von(z)
        print(f"Selbstprüfung bestanden: {len(alt)} Katalogzeilen, {len(alt_typ)} Typen "
              f"(gemeinsame Liste, {len(eigene - andere_typen)} nur hier, {len(eigene & andere_typen)} in beiden Katalogen), "
              f"alle Typen verwendet, {len(stapel)} Stapel vollständig. ZEILEN ist leer, nichts geschrieben.")
        if gew:
            print(f"Eichung über den Bestand: {treffer} von {gew} gewerteten Zeilen treffen den höchsten "
                  f"amtlichen Bereich ({100 * treffer // gew} %), enge Fassung {treffer_eng} "
                  f"({100 * treffer_eng // gew} %); {len(alt) - gew} Zeilen ohne Standardbezug.")
            print("Außerhalb der Geltung: " + ", ".join(
                f"{ziel} {sum(1 for z in alt if ziel not in GELTUNG.get(z['thema'], set()))}"
                for ziel in ZIELE) + f" von {len(alt)} Zeilen")
        # Landesverwendung je Stapel (v1.2): Poolzeilen, die ein Landesheft wortgleich stellt
        je_stapel, vorgemerkt_stapel = {}, {}
        for pid in verweis:
            k = kennung_aus_id(pid)[0]
            if k in QUELLE:
                je_stapel[einheit(QUELLE[k])] = je_stapel.get(einheit(QUELLE[k]), 0) + 1
        offen = []
        for pid in vorgemerkt:
            if pid in ids:  # Übergangszustand: offener Posten, kein Fehler (abi.md § 7)
                offen.append(f"{pid} ist erfasst, in {', '.join(vorgemerkt[pid])} noch vorgemerkt – abgleich.py")
            k = kennung_aus_id(pid)[0]
            s = einheit(QUELLE[k]) if k in QUELLE else "unbekannt"
            vorgemerkt_stapel[s] = vorgemerkt_stapel.get(s, 0) + 1
        print("In Landesheften (Dublette von): " + (", ".join(f"{s} {n}" for s, n in sorted(je_stapel.items())) or "keine")
              + f" – {sum(je_stapel.values())} Zeilen; vorgemerkt (Poolaufgabe (nicht erfasst)): "
              + (", ".join(f"{s} {n}" for s, n in sorted(vorgemerkt_stapel.items())) or "keine")
              + (f"; offene Posten mit erfasster Poolzeile: {len(offen)}" if offen else ""))
        for o in offen:
            print("  -", o)
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
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog des Stapels")
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
        pruefe_thema(z, a)
        for dep in [s for s in z["abhaengig_von"].split("|") if s]:
            a(dep in neue_ids or dep in alt_ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
    alle_verwendet = set(verwendet) | andere_typen
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
    # Geltung (abitur-vokabular.md § 3): Zeilen, deren Thema für eine Zielprüfung nicht gilt
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
    # Schnitt Thema × Gegenstandsklasse × Handlung (abitur-vokabular.md § 4): Werte des Stapels,
    # davon schon in einem Stapel desselben Niveaus vorhanden; Thema ist das des Typs (v1.1)
    def schnitt(z):
        return (TYP_THEMA.get(z["typ"], ("", z["thema"]))[1], klasse_von(z["typ"]),
                HANDLUNG.get(z["format"].split("|")[0], "?"))
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
    land = [i for i in neue_ids if i in verweis or i in vorgemerkt]
    print(f"Kennzahlen: | {stapel} | {n} | {len(verwendet)} | {len(neu & verwendet)} "
          f"({100 * len(neu & verwendet) / len(verwendet):.0f} %) | {treffer} von {gew} "
          f"({100 * treffer / gew if gew else 0:.0f} %)"
          + (f", eng {treffer_eng} ({100 * treffer_eng / gew:.0f} %)" if treffer_eng != treffer else "")
          + f" | {len(unsicher)} | {len(ersatz)} | {len(wieder)} von {len(verwendet)} "
          f"({100 * len(wieder) / len(verwendet):.0f} %) | {geltung_txt} | "
          f"Schnitt {len(schnitt_neu)} Werte, {schnitt_bekannt} von {n} Zeilen bekannt "
          f"({100 * schnitt_bekannt / n:.0f} %) | in Landesheften {len(land)} |")
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    # Landesverwendung (v1.2): abi-Zeilen, die eine Zeile dieses Stapels als „Poolaufgabe
    # (nicht erfasst)" vorgemerkt haben – nach dem Lauf wird der Vermerk zum Verweis.
    for i in neue_ids:
        if i in vorgemerkt:
            warnung.append(f"{i}: in {', '.join(vorgemerkt[i])} als „Poolaufgabe (nicht erfasst)“ vorgemerkt – "
                           f"Vermerk mit abgleich.py in „Dublette von:“ umstellen")
    print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
          "(Häufigkeit in Klammern):")
    liste = umschrift_liste(ZEILEN)
    print("  " + ", ".join(f"{w} ({n_}" + ")" for w, n_ in liste) if liste else "  keines")
    for w in warnung:
        print("Hinweis:", w)
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
