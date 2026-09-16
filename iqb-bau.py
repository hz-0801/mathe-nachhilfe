# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 1.3 · 16.09.2026 · gilt mit katalog-prompt.md v0.5, abitur-vokabular.md v1.1 und iqb.md v1.5

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

Änderungen gegenüber 1.2 (Auftrag „Reserve öffnen, Verweise schließen",
16.09.2026): Die Vormerkung „Poolaufgabe (nicht erfasst …)" ist ein
Übergangszustand (offener Posten, bis der Stapel erfasst ist); nach der
Erfassung stellt abgleich.py sie auf „Dublette von:" (wortgleich) oder
„Abgewandelt von: <id>; <Unterschied>." (abgewandelte Fassung) um. Beide
Verweise zählen als Landesverwendung; der Bestand des Stapels wird beim Lauf
gegen die Vormerkungen gemeldet.

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
    "stapel": "2018-ea-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2018MerhoehtBAnalysisWTR1": 50, "2018MerhoehtBAnalysisWTR2": 50, "2018MerhoehtBAGLAA1WTR": 25,
        "2018MerhoehtBAGLAA2WTR1": 25, "2018MerhoehtBAGLAA2WTR2": 25, "2018MerhoehtBAGLAA2WTR3": 25,
        "2018MerhoehtBStochastikWTR1": 25, "2018MerhoehtBStochastikWTR2": 25,
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
# Stapel 2018-ea-B (WTR-Zweig; Reserve, geöffnet 16.09.2026 wegen der
# Landesheftverweise 2018-be-gk 3.2 e und g auf Stochastik WTR 2). Acht Dateien,
# Standardbezug mit Spalte Anforderungsbereich; Analysis-Dateien mit 50 BE.
# ---- Analysis WTR 1: Aufgabe 1 (Graph dritten Grades, 30 BE), Aufgabe 2 (Kosten, 20 BE)
ANA = "f(x) = 1/18 · (x³ − 15x² + 50x), ganzrational dritten Grades, G_f schneidet die x-Achse bei 0, 5 und 10 und geht durch (1 | 2); Abbildung 1 zeigt G_f"
ANA_SK = ("Koordinatensystem auf Gitter, x von −1 bis 11, y von −3 bis 3. Graph G_f: vom Ursprung steigend zum "
          "Hochpunkt bei etwa (2,1 | 2,7), fallend durch den Wendepunkt W(5 | 0) zum Tiefpunkt bei etwa (7,9 | −2,7), "
          "dann steigend durch (10 | 0); Beschriftung G_f.")
row("2018MerhoehtBAnalysisWTR1", "a", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Ganzrationale Funktion dritten Grades aus drei Nullstellen und einem Punkt rekonstruieren", typ_neben="",
    stichwoerter="f(x) = a · x · (x − 5) · (x − 10)|f(1) = 36a = 2|a = 1/18",
    voraussetzungen="Produktform aus Nullstellen|Streckfaktor aus einem Punkt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="Koordinatensystem", skizze=ANA_SK, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung 1: Graph einer ganzrationalen Funktion dritten Grades mit Nullstellen 0, 5, 10 durch (1 | 2); Kontrolle f(x) = 1/18 (x³ − 15x² + 50x)",
    gesucht="ein Funktionsterm von f",
    verfahren="Produktansatz mit den drei Nullstellen, a aus f(1) = 2",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f(x) = a · x · (x − 5) · (x − 10) mit f(1) = 2 ⇔ a = 1/18 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Ansatz mit allgemeinen Koeffizienten und Gleichungssystem statt Produktform",
    bemerkung="Standardbezug: K1 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabe 1 dieser Datei stimmt in b und c mit dem grundlegenden Pool (Analysis WTR 1 a, b) überein, Vorfaktor 1/18 statt 1/8.")
row("2018MerhoehtBAnalysisWTR1", "b", innen="1", seite="1", punkte="6", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendepunkt an vorgegebener Stelle nachweisen und Wendetangente aufstellen", typ_neben="",
    stichwoerter="f'(x) = 1/18 (3x² − 30x + 50), f''(x) = 1/18 (6x − 30), f''' = 1/3|f''(5) = 0, f'''(5) ≠ 0|f'(5) = −25/18|Tangente y = −25/18 x + 125/18",
    voraussetzungen="Ableitungen ganzrationaler Funktionen|Wendepunktbedingung|Tangentengleichung",
    format="Rechnung", operator="Zeigen Sie|Ermitteln Sie", antwort="Term",
    material="Koordinatensystem", skizze=ANA_SK, kontext="ohne", textumfang="kurz",
    gegeben=ANA + "; Punkt W(5 | 0)",
    gesucht="Nachweis, dass W ein Wendepunkt ist; Gleichung der Tangente in W",
    verfahren="f''(5) = 0 und f'''(5) = 1/3 ≠ 0; f(5) = 0, f'(5) = −25/18",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f''(5) = 0, f'''(5) ≠ 0; Tangente y = −25/18 x + 125/18 (amtlich)",
    zwischenergebnis="f'(x) = 1/18 (3x² − 30x + 50)|f''(x) = 1/18 (6x − 30)", niveau_geschaetzt="II",
    fehlerquelle="hinreichende Bedingung weglassen",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ga-B). Geschätzt II (Verkettung), amtlich I – wie im grundlegenden Zwilling.")
row("2018MerhoehtBAnalysisWTR1", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Punktsymmetrie zum Wendepunkt über die Verschiebung einer ungeraden Funktion begründen", typ_neben="",
    stichwoerter="g(x) = 1/18 (x³ − 25x)|Verschiebung um 5|nur ungerade Potenzen, punktsymmetrisch zum Ursprung|G_f symmetrisch zu W(5 | 0)",
    voraussetzungen="Verschiebung in x-Richtung|ungerade Potenzen und Punktsymmetrie",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=ANA + "; G_f entsteht aus dem Graphen von g(x) = 1/18 (x³ − 25x) durch Verschiebung in positive x-Richtung",
    gesucht="Betrag der Verschiebung; Begründung der Symmetrie von G_f zum Wendepunkt mithilfe von g",
    verfahren="g(x − 5) = f(x): Verschiebung 5; g punktsymmetrisch zum Ursprung, also f zu W",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Verschiebung um 5; g hat nur ungerade Potenzen und ist punktsymmetrisch zum Ursprung, G_f also zu W(5 | 0) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Symmetrie an f statt an g prüfen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ga-B).")
FIN = "F1(x) = ∫ von 1 bis x f(t) dt (Integralfunktion zu f mit unterer Grenze 1)"
row("2018MerhoehtBAnalysisWTR1", "d", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Ganzzahlige Nullstellen einer Integralfunktion über gleiche Grenzen und Symmetrie begründen", typ_neben="",
    stichwoerter="F1(1) = 0, Grenzen stimmen überein|F1(9) = 0: Flächenstücke von 1 bis 5 oberhalb und 5 bis 9 unterhalb sind wegen der Symmetrie zu W gleich groß",
    voraussetzungen="Integral mit gleichen Grenzen|Flächenbilanz|Punktsymmetrie des Integranden",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="Koordinatensystem", skizze=ANA_SK, kontext="ohne", textumfang="kurz",
    gegeben=ANA + "; " + FIN + "; F1 hat für 0 ≤ x ≤ 10 zwei ganzzahlige Nullstellen",
    gesucht="die beiden Nullstellen mit Begründung",
    verfahren="x = 1 wegen gleicher Grenzen; x = 9, weil G_f symmetrisch zu (5 | 0) ist und die Flächenstücke über [1; 5] und [5; 9] sich aufheben",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="x = 1 (Integrationsgrenzen stimmen überein) und x = 9 (die Flächenstücke ober- und unterhalb der x-Achse im Bereich 1 bis 9 sind wegen der Symmetrie gleich groß) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="x = 5 oder x = 10 als Nullstelle von F1 nennen (Nullstellen von f)",
    bemerkung="Standardbezug: K1 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (F1(9) = 0). Eichregel: (e) Nullstellen einer Integralfunktion als Flächenbilanz am Graphen, mit (b) Symmetrie – geschätzt III, amtlich II.")
row("2018MerhoehtBAnalysisWTR1", "e", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Weitere Nullstelle einer Integralfunktion über die Flächenbilanz am Graphen begründen", typ_neben="",
    stichwoerter="F1(10) < 0, weil das Flächenstück unter der x-Achse zwischen 5 und 10 größer ist als das über [1; 5]|für x > 10 wächst F1 unbeschränkt|Flächenbilanz wird null",
    voraussetzungen="Vorzeichen von f als Monotonie von F1|Flächenbilanz",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ANA_SK, kontext="ohne", textumfang="kurz",
    gegeben=ANA + "; " + FIN,
    gesucht="Begründung mithilfe der Abbildung, dass F1 mindestens eine weitere positive Nullstelle hat",
    verfahren="Für ein x > 10 sind die Inhalte der Flächenstücke oberhalb der x-Achse zusammen so groß wie das Flächenstück unterhalb",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Für ein x > 10 sind die Flächenstücke oberhalb der x-Achse im Integrationsbereich zusammen ebenso groß wie das unterhalb liegende, dort ist F1(x) = 0 (amtlich)",
    zwischenergebnis="F1(10) = −∫ von 0 bis 1 f < 0", niveau_geschaetzt="III",
    fehlerquelle="mit dem Grad von F1 statt mit dem Graphen von f argumentieren",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Nullstelle bei etwa 10,83). Eichregel: (e) Nullstelle einer Integralfunktion als Flächenbilanz – geschätzt III, amtlich II.")
row("2018MerhoehtBAnalysisWTR1", "f", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Höchstzahl der Nullstellen einer Integralfunktion über den Grad begründen", typ_neben="",
    stichwoerter="F1 ist ganzrational vierten Grades|höchstens vier Nullstellen",
    voraussetzungen="Grad der Stammfunktion|Nullstellenzahl ganzrationaler Funktionen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=ANA + "; " + FIN,
    gesucht="Begründung, dass F1 höchstens vier Nullstellen hat",
    verfahren="Grad von F1 ist 4",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="F1 ist ganzrational vierten Grades und hat als solche höchstens vier Nullstellen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Grad 3 annehmen",
    bemerkung="Standardbezug: K1 II, K5 II. AB amtlich: II. Amtlich. Geschätzt I (eine begründete Beobachtung), amtlich II.")
row("2018MerhoehtBAnalysisWTR1", "g", innen="1", seite="2", punkte="6", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Sinusfunktion mit gleichen Nullstellen und gleichem Flächeninhalt wie ein Graph bestimmen", typ_neben="",
    stichwoerter="h(x) = a · sin(bx)|Nullstellen 0 und 5: b = π/5|∫ von 0 bis 5 h = 10a/π = 625/72|a = 125π/144",
    voraussetzungen="Periode einer Sinusfunktion aus Nullstellen|Integral der Sinusfunktion|Gleichung nach a auflösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Koordinatensystem", skizze=ANA_SK, kontext="ohne", textumfang="mittel",
    gegeben=ANA + "; für 0 ≤ x ≤ 5 haben G_f und der Graph einer trigonometrischen Funktion h dieselben Schnittpunkte mit der x-Achse, verlaufen nicht unterhalb der x-Achse und schließen mit ihr je eine Fläche des Inhalts 625/72 ein",
    gesucht="ein Term einer solchen Funktion h",
    verfahren="Ansatz a · sin(bx); b aus der Nullstelle 5 (halbe Periode); a aus dem Integral über [0; 5]",
    schritte="3", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="h(x) = a · sin(π/5 · x) mit ∫ von 0 bis 5 h(x) dx = 10a/π = 625/72 ⇔ a = 125π/144 (amtlich)",
    zwischenergebnis="∫ von 0 bis 5 f = 625/72", niveau_geschaetzt="III",
    fehlerquelle="b = 2π/5 (volle Periode auf [0; 5]) wählen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die drei Sachbedingungen (Nullstellen, Vorzeichen, Flächeninhalt) in Ansatz und Gleichung übersetzen.")
row("2018MerhoehtBAnalysisWTR1", "h", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Gemeinsamen Punkt zweier Graphen über gleiche Flächeninhalte indirekt begründen", typ_neben="",
    stichwoerter="ohne gemeinsamen Punkt läge G_f ganz oberhalb oder ganz unterhalb von G_h|dann wären die Flächeninhalte verschieden|Widerspruch",
    voraussetzungen="Zwischenwertargument|Flächenvergleich bei Lage eines Graphen über dem anderen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ANA_SK, kontext="ohne", textumfang="mittel",
    gegeben=ANA + "; h wie in g (gleiche Nullstellen, gleicher Flächeninhalt 625/72 über [0; 5])",
    gesucht="Begründung, dass G_f und G_h für 0 < x < 5 mindestens einen gemeinsamen Punkt haben",
    verfahren="Indirekt: ohne gemeinsamen Punkt verliefe G_f vollständig ober- oder unterhalb von G_h, die Flächeninhalte wären dann verschieden",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Hätten die Graphen keinen gemeinsamen Punkt, verliefe G_f dort vollständig oberhalb oder vollständig unterhalb von G_h; das widerspricht den gleichen Flächeninhalten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur die gemeinsamen Nullstellen 0 und 5 nennen (liegen nicht im offenen Intervall)",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (a) gleiche Flächeninhalte in eine Aussage über die Lage der Graphen übersetzen.")
KOS = ("Kostenfunktion K(x) = x³ − 12x² + 50x + 20, 0 ≤ x ≤ 9, K(x) in 1000 Euro für die Produktion von x Kubikmetern "
       "einer Flüssigkeit; Abbildung 2 zeigt den Graphen von K")
KOS_SK = ("Koordinatensystem auf Gitter, x von −1 bis 9, y von 0 bis 220 in Zwanzigerschritten. Graph von K: bei "
          "(0 | 20) beginnend, ansteigend mit abnehmender Steigung bis zu einem flachen Bereich um (4 | 90), danach "
          "zunehmend steil bis etwa (9 | 230).")
row("2018MerhoehtBAnalysisWTR1", "a", innen="2", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Stelle zu einem vorgegebenen Funktionswert am Graphen ablesen", typ_neben="",
    stichwoerter="K(x) = 125|am Graphen x ≈ 7",
    voraussetzungen="Einheit 1000 Euro|Ablesen am Graphen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=KOS_SK, kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS,
    gesucht="Produktionsmenge mit Kosten 125 000 Euro, mithilfe der Abbildung",
    verfahren="y = 125 am Graphen suchen",
    schritte="1", zahlenraum="ganz", einheiten="m³", abhaengig_von="",
    ergebnis="etwa 7 m³ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Einheit der y-Achse übersehen",
    bemerkung="Standardbezug: K3 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabe 2 a–e wortgleich mit dem grundlegenden Pool Analysis WTR 2 a, b, d, e, f; Typen von dort.")
row("2018MerhoehtBAnalysisWTR1", "b", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Verlauf eines Graphen im Sachzusammenhang beschreiben", typ_neben="",
    stichwoerter="K streng monoton wachsend|mehr Produktion, höhere Kosten",
    voraussetzungen="Monotonie am Graphen",
    format="Kurzantwort", operator="Geben Sie an|Deuten Sie", antwort="Text",
    material="Koordinatensystem", skizze=KOS_SK, kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS,
    gesucht="Monotonieverhalten von K mit Deutung",
    verfahren="Am Graphen ablesen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="K ist streng monoton wachsend: mit zunehmender Produktionsmenge nehmen die Kosten zu (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="flachen Bereich als Abnahme deuten",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet.")
row("2018MerhoehtBAnalysisWTR1", "c", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Gleichheit zweier Funktionswerte durch Einsetzen im Sachzusammenhang nachweisen", typ_neben="",
    stichwoerter="E(x) = 23x, G = E − K|E(4) − K(4) = 92 − 92 = 0",
    voraussetzungen="Funktionswerte|Gewinn als Differenz",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS + "; Erlös E(x) = 23x, Gewinn G = E − K",
    gesucht="Nachweis, dass bei vier verkauften Kubikmetern kein Gewinn entsteht",
    verfahren="E(4) und K(4) vergleichen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="E(4) − K(4) = 92 − 92 = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Rechenfehler bei K(4)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ga-B).")
row("2018MerhoehtBAnalysisWTR1", "d", innen="2", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Gewinnbereich als Bereich zwischen den Schnittstellen von Erlösgerade und Kostengraph zeichnerisch bestimmen", typ_neben="",
    stichwoerter="Gerade E(x) = 23x in Abbildung 2|Schnittstellen 4 und x_S ≈ 8,6|Gewinn für 4 < x < x_S",
    voraussetzungen="Ursprungsgerade zeichnen|Gewinnbereich als Lage der Erlösgeraden über dem Kostengraphen",
    format="Zeichnen|Kurzantwort", operator="Zeichnen Sie ein|Bestimmen Sie", antwort="Grafik|Zahl",
    material="Koordinatensystem", skizze=KOS_SK, kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS + "; E(x) = 23x, G = E − K",
    gesucht="Graph von E in Abbildung 2; Bereich der verkauften Menge mit Gewinn",
    verfahren="Gerade einzeichnen, Schnittstellen ablesen",
    schritte="2", zahlenraum="dezimal", einheiten="m³", abhaengig_von="2018MerhoehtBAnalysisWTR1-2c",
    ergebnis="Gewinn nur für 4 < x < x_S mit x_S ≈ 8,6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Bereich links von 4 mitnehmen",
    bemerkung="Standardbezug: K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ga-B).")
row("2018MerhoehtBAnalysisWTR1", "e", innen="2", seite="3", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Maximum einer Gewinnfunktion über die Ableitung berechnen", typ_neben="",
    stichwoerter="G(x) = −x³ + 12x² − 27x − 20|G'(x) = −3x² + 24x − 27 = 0 ⇔ x = 4 ± √7|Maximum bei 4 + √7 ≈ 6,6",
    voraussetzungen="Differenzfunktion|Extremstellen|Lösung im Gewinnbereich",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS + "; E(x) = 23x, G = E − K, Gewinnbereich 4 < x < x_S ≈ 8,6",
    gesucht="verkaufte Menge mit dem größten Gewinn",
    verfahren="G aufstellen, G' = 0, Lösung im Gewinnbereich",
    schritte="4", zahlenraum="Wurzel|dezimal|negativ", einheiten="m³", abhaengig_von="",
    ergebnis="G'(x) = 0 ⇔ x = 4 + √7 ≈ 6,6 im Bereich 4 < x < x_S; etwa 6,6 Kubikmeter (amtlich)",
    zwischenergebnis="G'(x) = −3x² + 24x − 27", niveau_geschaetzt="II",
    fehlerquelle="4 − √7 nicht ausschließen",
    bemerkung="Standardbezug: K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ga-B).")
row("2018MerhoehtBAnalysisWTR1", "f", innen="2", seite="3", punkte="6", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Strenge Monotonie einer Schar über die Diskriminante der Ableitung für einen Parameterbereich nachweisen", typ_neben="",
    stichwoerter="K_b(x) = x³ − bx² + 50x + 20, b > 0|K_b'(x) = 3x² − 2bx + 50|Diskriminante 4b² − 600 < 0 ⇔ b < √150|K_b'(0) = 50 > 0, K_b' ohne Nullstellen, also positiv",
    voraussetzungen="Ableitung mit Parameter|Diskriminante einer quadratischen Gleichung|Vorzeichen einer nullstellenfreien Funktion über einen Wert",
    format="Rechnung|Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Produktion/Kosten", textumfang="mittel",
    gegeben="Schar K_b(x) = x³ − bx² + 50x + 20, x ∈ IR, b > 0",
    gesucht="Nachweis, dass K_b für b < √150 streng monoton wachsend ist",
    verfahren="K_b' = 0 hat für 4b² − 600 < 0 keine Lösung; K_b'(0) > 0, also K_b' > 0 überall",
    schritte="3", zahlenraum="Wurzel", einheiten="", abhaengig_von="",
    ergebnis="K_b'(x) = 3x² − 2bx + 50 hat für b² < 150, also 0 < b < √150, keine Nullstelle; wegen K_b'(0) > 0 ist K_b' > 0 und K_b streng monoton wachsend (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="aus fehlenden Nullstellen von K_b' nicht auf das Vorzeichen schließen",
    bemerkung="Standardbezug: K1 III, K2 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis mit Parameter, Bedingung b < √150 hergeleitet. Textextraktion zeigt „b < 150“, das Bild √150.")
# ---- Analysis WTR 2: Kugelstoßen (Aufgabe 1, 42 BE), Behälter mit Kugel (Aufgabe 2, 8 BE)
KUG = ("Kugelstoßen im Koordinatensystem (1 LE = 1 m, x-Achse ist der Boden): Bahn von der Ruhelage R bis zum Abstoßpunkt "
       "A durch f(x) = 0,4 + 1,6 · e^(0,5x), x ∈ [−2; 0]; Flugkurven p_a(x) = −ax² + bx + 2, a > 0, ohne Knick in A")
KUG_SK = ("Koordinatensystem auf Gitter, x von −2 bis 7, y von 0 bis 3. Von R(−2 | 1) steigt die Bahn nach rechts zum "
          "Abstoßpunkt A(0 | 2); von A aus drei nach unten geöffnete Parabelbögen mit Hochpunkten bei etwa (1,3 | 2,7), "
          "(2 | 2,8) und (2,7 | 3), die die x-Achse bei etwa 4,5, 5,7 und 7 erreichen. Beschriftungen R, A, Abb. 1.")
row("2018MerhoehtBAnalysisWTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Länge der Verbindungsstrecke zweier Graphenpunkte als Näherung der Bogenlänge berechnen", typ_neben="",
    stichwoerter="f(−2) ≈ 1, f(0) = 2|Strecke √(2² + 1²) ≈ 2,24",
    voraussetzungen="Funktionswerte einer Exponentialfunktion|Pythagoras",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=KUG_SK, kontext="Kugelstoßen", textumfang="mittel",
    gegeben=KUG,
    gesucht="Länge der Bahn von R bis A näherungsweise als Streckenlänge",
    verfahren="R(−2 | f(−2)) und A(0 | 2), Abstand",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="√(1² + 2²) ≈ 2,24; die Bahn ist etwa 2,24 m lang (amtlich)",
    zwischenergebnis="f(−2) = 0,4 + 1,6 · e^(−1) ≈ 0,99", niveau_geschaetzt="I",
    fehlerquelle="Bogenlänge über ein Integral versuchen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (2,241).")
row("2018MerhoehtBAnalysisWTR2", "b", innen="1", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Exponentialgleichung für einen Funktionswert durch Logarithmieren lösen und als Abstand im Sachzusammenhang angeben", typ_neben="",
    stichwoerter="f(x) = 1,5 ⇔ e^(0,5x) = 1,1/1,6 ⇔ x = 2 · ln(1,1/1,6) ≈ −0,75|Abstand von R: −0,75 − (−2) = 1,25",
    voraussetzungen="Exponentialgleichung durch Logarithmieren|Abstand als Differenz der x-Werte",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="kurz",
    gegeben=KUG,
    gesucht="horizontaler Abstand der Kugel von der Ruhelage bei Höhe 1,50 m",
    verfahren="f(x) = 1,5 lösen, Differenz zu x = −2",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="",
    ergebnis="f(x) = 1,5 ⇔ x = 2 · ln(1,1/1,6) ≈ −0,75; der Abstand beträgt etwa 1,25 m (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="x ≈ −0,75 als Abstand angeben (Ruhelage bei x = −2)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBAnalysisWTR2", "c", innen="1", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Aussage zur Modellgüte über die Summe vorzeichenbehafteter Abweichungen beurteilen", typ_neben="",
    stichwoerter="Betrag der Summe Σ (h_i − f(x_i)) klein|große Abweichungen mit verschiedenen Vorzeichen heben sich auf|Aussage falsch",
    voraussetzungen="Summe von Differenzen deuten|Aufheben von Vorzeichen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="mittel",
    gegeben=KUG + "; gemessene Höhen h1 bis h5 an den Stellen x1 bis x5; Aussage: Ist |Σ (h_i − f(x_i))| klein, beschreibt das Modell die Messwerte gut",
    gesucht="Beurteilung der Aussage",
    verfahren="Gegenargument: betragsgroße Abweichungen mit verschiedenen Vorzeichen können sich in der Summe aufheben",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist falsch: Werte h_i − f(x_i) mit großen Beträgen können sich zumindest teilweise aufheben, wenn sie verschiedene Vorzeichen haben (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Betrag der Summe mit Summe der Beträge verwechseln",
    bemerkung="Standardbezug: K1 III, K3 III, K4 III. AB amtlich: III. Amtlich. Eichregel: (d) den Summenterm in eine Sachaussage über die Modellgüte übersetzen, mit der Deutung des Vorzeichenausgleichs. Thema ersatzweise: die Themenliste hat kein Thema für Modellgüte und Messwertabweichung; Nullstellen und Werte (Funktionswerte gegen Messwerte) ist das nächstliegende.")
row("2018MerhoehtBAnalysisWTR2", "d", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameter einer Parabelschar aus dem knickfreien Übergang zu einem Graphen bestimmen", typ_neben="",
    stichwoerter="p_a'(x) = −2ax + b, f'(x) = 0,8 · e^(0,5x)|p_a'(0) = f'(0) ⇔ b = 0,8",
    voraussetzungen="knickfrei heißt gleiche Steigung|Ableitung der Exponentialfunktion",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="kurz",
    gegeben=KUG + "; Kontrolle b = 0,8",
    gesucht="Wert von b",
    verfahren="Steigungen von f und p_a an der Stelle 0 gleichsetzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="p_a'(0) = f'(0) ⇔ b = 0,8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Knickfreiheit als gleiche Funktionswerte deuten",
    bemerkung="Standardbezug: K1 I, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBAnalysisWTR2", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben", typ_neben="",
    stichwoerter="−9a + 2,4 + 2 = 3,5|a = 0,1",
    voraussetzungen="Punktprobe mit Parameter",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="kurz",
    gegeben=KUG + "; b = 0,8",
    gesucht="Wert von a, für den der Graph von p_a durch (3 | 3,5) verläuft",
    verfahren="Einsetzen und nach a auflösen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2018MerhoehtBAnalysisWTR2-1d",
    ergebnis="−a · 3² + 0,8 · 3 + 2 = 3,5 ⇔ a = 0,1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen von −ax² übersehen",
    bemerkung="Standardbezug: K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ea-A, angeben; hier berechnet).")
row("2018MerhoehtBAnalysisWTR2", "f", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Auftreffwinkel einer Flugkurve über die Ableitung an der Nullstelle berechnen", typ_neben="",
    stichwoerter="a = 0,1, Stoßweite 10, Auftreffen bei x = 10|tan φ = p'(10) = −1,2|φ ≈ 50°",
    voraussetzungen="Steigung als Tangens des Neigungswinkels|Ableitung an einer Stelle",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="kurz",
    gegeben=KUG + "; b = 0,8; für a = 0,1 beträgt die Stoßweite 10 m",
    gesucht="Größe des Winkels, unter dem die Kugel auf den Boden trifft",
    verfahren="p_0,1'(10) = −1,2, Winkel über den Arkustangens",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="Grad", abhaengig_von="",
    ergebnis="tan φ = p_0,1'(10) = −1,2, φ ≈ −50°; die Kugel trifft unter etwa 50° auf (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Winkel zur Senkrechten (40°) angeben",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (50,2°).")
row("2018MerhoehtBAnalysisWTR2", "g", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Hochpunkt einer Parabelschar mit Parameterkoordinaten nachweisen", typ_neben="",
    stichwoerter="nach unten geöffnete Parabel|p_a'(0,4/a) = −0,8 + 0,8 = 0|p_a(0,4/a) = 2 + 0,16/a",
    voraussetzungen="Öffnung einer Parabel|Ableitung null|Funktionswert mit Parameter",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="kurz",
    gegeben=KUG + "; b = 0,8",
    gesucht="Nachweis, dass (0,4/a | 2 + 0,16/a) Hochpunkt des Graphen von p_a ist",
    verfahren="Parabel nach unten geöffnet, p_a'(0,4/a) = 0, Funktionswert einsetzen",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="p_a'(0,4/a) = −2a · 0,4/a + 0,8 = 0; p_a(0,4/a) = −a · (0,4/a)² + 0,8 · 0,4/a + 2 = 2 + 0,16/a; Parabel nach unten geöffnet (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Art des Extremums nicht begründen",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBAnalysisWTR2", "h", innen="1", seite="2", punkte="3", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Steigung der Ortsgeraden der Hochpunkte einer Schar aus zwei Hochpunkten berechnen", typ_neben="",
    stichwoerter="a = 1: (0,4 | 2,16), a = 2: (0,2 | 2,08)|Steigung (2,16 − 2,08)/(0,4 − 0,2) = 0,4",
    voraussetzungen="Hochpunkt mit Parameter|Steigung aus zwei Punkten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="kurz",
    gegeben=KUG + "; Hochpunkt (0,4/a | 2 + 0,16/a); alle Hochpunkte liegen auf einer Geraden",
    gesucht="Steigung dieser Geraden",
    verfahren="Zwei Hochpunkte berechnen und die Steigung bilden (oder y = 2 + 0,4x eliminieren)",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2018MerhoehtBAnalysisWTR2-1g",
    ergebnis="Für a = 1 Hochpunkt (0,4 | 2,16), für a = 2 (0,2 | 2,08); Steigung 0,4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Steigung als Quotient der Koordinaten eines Hochpunkts",
    bemerkung="Standardbezug: K2 III, K3 I, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Geschätzt II (Verkettung: zwei Punkte, Steigung; die Gerade ist vorgegeben), amtlich III.")
row("2018MerhoehtBAnalysisWTR2", "i", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gleichung zwischen Scharparameter und Nullstelle aus der Nullstellenbedingung herleiten", typ_neben="",
    stichwoerter="p_a(s) = 0|−as² + 0,8s + 2 = 0|a = 0,8/s + 2/s²",
    voraussetzungen="Stoßweite als Nullstelle|Umstellen nach a",
    format="Rechnung", operator="Leiten Sie her", antwort="Term",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="kurz",
    gegeben=KUG + "; b = 0,8; Zusammenhang a = 0,8/s + 2/s² zwischen a und Stoßweite s > 0",
    gesucht="Herleitung dieser Gleichung",
    verfahren="Nullstellenbedingung p_a(s) = 0 nach a auflösen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="p_a(s) = 0 ⇔ a · s² = 0,8s + 2 ⇔ a = 0,8/s + 2/s² (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Stoßweite mit der Hochpunktstelle verwechseln",
    bemerkung="Standardbezug: K2 II, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBAnalysisWTR2", "j", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus der Weite berechnen und Höhe des Hochpunkts angeben", typ_neben="",
    stichwoerter="s = 20: a = 0,8/20 + 2/400 = 0,045|Höhe 2 + 0,16/0,045 ≈ 5,6",
    voraussetzungen="Parameter aus der Weite|Hochpunkthöhe mit Parameter",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kugelstoßen", textumfang="kurz",
    gegeben=KUG + "; a = 0,8/s + 2/s²; Hochpunkthöhe 2 + 0,16/a; Stoßweite 20 m",
    gesucht="Höhe der Flugkurve",
    verfahren="a aus s = 20, dann Hochpunkthöhe",
    schritte="2", zahlenraum="dezimal", einheiten="m", abhaengig_von="2018MerhoehtBAnalysisWTR2-1i",
    ergebnis="a = 0,8/20 + 2/20² = 0,045; Höhe 2 + 0,16/0,045 ≈ 5,6 m (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Höhe als 0,16/a ohne den Summanden 2 angeben",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (5,56).")
KUG_AB2 = ("Kleines Koordinatensystem auf Gitter, s von 0 bis 18, a von 0 bis 0,9: fallende Kurve a(s) = 0,8/s + 2/s², "
           "bei s = 2 in Höhe 0,9, bei s = 10 in Höhe 0,1, gegen die s-Achse abflachend; Beschriftung Abb. 2.")
row("2018MerhoehtBAnalysisWTR2", "k", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Aussage über das Verhältnis zweier Funktionswerte durch Einsetzen widerlegen", typ_neben="",
    stichwoerter="s = 10: a = 0,1; s = 12: a ≈ 0,08, nicht 0,05|Aussage falsch",
    voraussetzungen="Funktionswerte berechnen oder ablesen|Gegenbeispiel",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=KUG_AB2, kontext="Kugelstoßen", textumfang="mittel",
    gegeben="Abbildung 2: Graph von a(s) = 0,8/s + 2/s²; Aussage: Unterscheiden sich zwei Weiten um 2 m, ist der Wert von a zur größeren Weite halb so groß",
    gesucht="Beurteilung der Aussage",
    verfahren="Gegenbeispiel s = 10 und s = 12",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2018MerhoehtBAnalysisWTR2-1i",
    ergebnis="Die Aussage ist falsch: für s = 10 ist a = 0,1, für s = 12 etwa 0,08 und damit deutlich mehr als die Hälfte (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Aussage an nur einem Wertepaar aus dem Graphen grob bestätigen",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (a(12) ≈ 0,081).")
row("2018MerhoehtBAnalysisWTR2", "l", innen="1", seite="2", punkte="7", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Flächeninhalt zwischen Graph, Achse und zwei Parallelen über Rechtecke und Integral berechnen", typ_neben="",
    stichwoerter="Parallelen a = 0,9 (s = 2) und a = 0,1 (s = 10)|Fläche = 2 · 0,9 + ∫ von 2 bis 10 (0,8/s + 2/s²) ds − 10 · 0,1|0,8 · ln 5 + 0,8 + 0,8 = ≈ 2,9",
    voraussetzungen="Parallelen zur s-Achse durch Graphenpunkte|Flächenstück in Rechtecke und Integral zerlegen|Stammfunktion von 1/s und 1/s²",
    format="Zeichnen|Rechnung", operator="Zeichnen Sie ein|Berechnen Sie", antwort="Grafik|Zahl",
    material="Koordinatensystem", skizze=KUG_AB2, kontext="Kugelstoßen", textumfang="mittel",
    gegeben="Abbildung 2 mit a(s) = 0,8/s + 2/s²; Parallelen zur s-Achse durch die Graphenpunkte mit s = 2 und s = 10",
    gesucht="die beiden Parallelen in Abbildung 2; Inhalt des Flächenstücks zwischen Graph, a-Achse und den Parallelen",
    verfahren="a(2) = 0,9, a(10) = 0,1; Fläche als Rechteck 2 · 0,9 plus Integral von 2 bis 10 minus Rechteck 10 · 0,1",
    schritte="4", zahlenraum="dezimal", einheiten="", abhaengig_von="2018MerhoehtBAnalysisWTR2-1i",
    ergebnis="2 · 0,9 + ∫ von 2 bis 10 (0,8/s + 2/s²) ds − 10 · 0,1 = 0,8 + 0,8 · ln 10 − 0,8 · ln 2 + 0,8 ≈ 2,9 (amtlich)",
    zwischenergebnis="a(2) = 0,9, a(10) = 0,1|∫ von 2 bis 10 = 0,8 · ln 5 + 0,8 ≈ 2,09", niveau_geschaetzt="III",
    fehlerquelle="nur das Integral von 2 bis 10 berechnen",
    bemerkung="Standardbezug: K2 III, K4 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (2,888). Eichregel: (a) das von Graph, Achse und Parallelen berandete Flächenstück erst in Rechtecke und Integral übersetzen.")
BEH = ("Behälter mit Kugel (Abbildung 3, um 90° gedreht, 1 LE = 1 cm): Seitenwand durch Rotation des Graphen von "
       "q(x) = √(5x + 40), x ∈ [0; 13], um die x-Achse; Kugel mit Durchmesser 10 cm liegt auf dem Boden (x = 0), "
       "vollständig unter Wasser")
BEH_SK = ("Koordinatensystem, x von 0 bis 13 nach rechts, y von −8 bis 8: zwei symmetrische Kurvenäste von (0 | ±√40) "
          "nach rechts auseinanderlaufend (Behälterwand), dazwischen ein Kreis mit Mittelpunkt (5 | 0) und Radius 5, "
          "der die y-Achse berührt; Beschriftung Abb. 3.")
row("2018MerhoehtBAnalysisWTR2", "a", innen="2", seite="3", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Wasservolumen als Differenz aus Rotationsvolumen und Kugelvolumen nach unten abschätzen", typ_neben="",
    stichwoerter="Wasser reicht mindestens bis x = 10 (Kugel unter Wasser)|π · ∫ von 0 bis 10 (5x + 40) dx = 650π|Kugel 4/3 π · 125|650π − 500π/3 ≈ 1518 > 1500",
    voraussetzungen="Rotationsvolumen als π∫q²|Kugelvolumen|Untergrenze aus der Sachlage",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=BEH_SK, kontext="Behälter/Kugel", textumfang="mittel",
    gegeben=BEH,
    gesucht="Nachweis, dass sich mehr als 1500 cm³ Wasser im Behälter befinden",
    verfahren="Rotationsvolumen bis zur Kugeloberkante x = 10 minus Kugelvolumen",
    schritte="3", zahlenraum="dezimal", einheiten="cm³", abhaengig_von="",
    ergebnis="π · ∫ von 0 bis 10 (q(x))² dx − 4/3 · π · 5³ = π · [5x²/2 + 40x] von 0 bis 10 − 500π/3 ≈ 1518 > 1500 (amtlich)",
    zwischenergebnis="650π", niveau_geschaetzt="III",
    fehlerquelle="Kugelvolumen nicht abziehen; obere Grenze 13 statt 10 (Wasserstand unbekannt)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (1518,4). Eichregel: (a) „Kugel vollständig unter Wasser“ in die Untergrenze x = 10 des Rotationsvolumens übersetzen – geschätzt III, amtlich II.")
row("2018MerhoehtBAnalysisWTR2", "b", innen="2", seite="3", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Gleichung für die Füllhöhe aus einem Rotationsvolumen zwischen variablen Grenzen aufstellen", typ_neben="",
    stichwoerter="Füllhöhe t vor dem Einfüllen|π · ∫ von t bis t + 1 (q(x))² dx = 300",
    voraussetzungen="Volumenzuwachs als Rotationsvolumen einer Schicht|variable Grenzen",
    format="Rechnung", operator="Stellen Sie auf", antwort="Term",
    material="Koordinatensystem", skizze=BEH_SK, kontext="Behälter/Kugel", textumfang="kurz",
    gegeben=BEH + "; zusätzlich 300 cm³ Wasser lassen die Füllhöhe um 1 cm steigen",
    gesucht="Gleichung zur Berechnung der Füllhöhe vor dem Einfüllen",
    verfahren="Schicht zwischen t und t + 1 als Rotationsvolumen gleich 300",
    schritte="1", zahlenraum="ganz", einheiten="cm³", abhaengig_von="",
    ergebnis="π · ∫ von t bis t + 1 (q(x))² dx = 300 mit t als Füllhöhe vor dem Einfüllen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die Kugel in die Schicht einrechnen (liegt unterhalb)",
    bemerkung="Standardbezug: K1 III, K3 II, K5 II. AB amtlich: III. Amtlich. Eichregel: (a) den Höhenzuwachs in ein Rotationsintegral mit variablen Grenzen übersetzen.")
# ---- AG/LA (A1) WTR: Parallelogramm (Aufgabe 1, 9 BE), Springkraut (Aufgabe 2, 16 BE)
PAR = "Viereck ABCD mit A(0 | 0 | 0), B(0 | 6 | 0), C(−4 | 14 | 4), D(−4 | 8 | 4) im räumlichen Koordinatensystem (Abbildung mit Achsen x, y, z)"
PAR_SK = ("Schrägbild eines räumlichen Koordinatensystems auf Gitter, y-Achse nach rechts bis 16, z-Achse nach oben bis "
          "8, x-Achse schräg nach vorn links; alle Achsen in Viererschritten beschriftet, ohne eingetragene Punkte.")
row("2018MerhoehtBAGLAA1WTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen",
    typ_neben="Ebene Figur: Viereck in ein Schrägbild einzeichnen",
    stichwoerter="AB = (0; 6; 0) = DC|Parallelogramm|Punkte ins Schrägbild eintragen und verbinden",
    voraussetzungen="Verbindungsvektoren|Parallelogrammkriterium|Schrägbild",
    format="Rechnung|Zeichnen", operator="Zeigen Sie|Zeichnen Sie ein", antwort="Text|Grafik",
    material="Koordinatensystem", skizze=PAR_SK, kontext="ohne", textumfang="kurz",
    gegeben=PAR,
    gesucht="Nachweis, dass ABCD ein Parallelogramm ist; Zeichnung in der Abbildung",
    verfahren="AB und DC vergleichen; Punkte eintragen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="DC = (0; 6; 0) = AB, also Parallelogramm; Zeichnung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen der negativen Koordinaten beim Eintragen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Koordinaten am Bild geprüft (C(−4 | 14 | 4), D(−4 | 8 | 4); die Textextraktion verliert die Minuszeichen).")
row("2018MerhoehtBAGLAA1WTR", "b", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Endpunkt der Schnittstrecke eines Vierecks mit einer achsenparallelen Ebene bestimmen", typ_neben="",
    stichwoerter="Ebene z = 1|auf AD: A + k · (−4; 8; 4) mit 4k = 1, k = 1/4|(−1 | 2 | 1)",
    voraussetzungen="Ebene parallel zur xy-Ebene als z = 1|Punkt auf einer Seite über den Parameter",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=PAR_SK, kontext="ohne", textumfang="kurz",
    gegeben=PAR + "; Ebene parallel zur xy-Ebene durch (0 | 0 | 1) schneidet das Viereck in einer Strecke",
    gesucht="Koordinaten eines Endpunkts dieser Strecke",
    verfahren="z-Koordinate 1 auf der Seite AD (oder BC) über den Parameter",
    schritte="2", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="(0; 0; 0) + 1/4 · AD = (−1 | 2 | 1) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="k = 1/4 auf AC statt auf einer Seite anwenden",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBAGLAA1WTR", "c", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lotfußpunkt auf einer Geraden über das Skalarprodukt mit dem Richtungsvektor berechnen", typ_neben="",
    stichwoerter="G(−4k | 8k | 4k) auf AD|AD · CG = 0: 96k − 144 = 0|k = 3/2|G(−6 | 12 | 6)",
    voraussetzungen="Punkt auf der Geraden mit Parameter|Orthogonalität über das Skalarprodukt",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=PAR + "; Punkt G auf der Geraden AD, sodass CG senkrecht zu AD ist",
    gesucht="Koordinaten von G",
    verfahren="G = k · AD, Skalarprodukt AD · CG = 0 nach k lösen",
    schritte="3", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Mit G(−4k | 8k | 4k): AD · CG = 96k − 144 = 0 ⇔ k = 3/2; G(−6 | 12 | 6) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="G auf der Strecke AD suchen (liegt außerhalb, k = 1,5)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
SPR = ("Indisches Springkraut: Zustand (S; P) mit Samen S und Pflanzen P; Frühjahr bis Herbst F · u mit "
       "F = ((f1; f2), (0; 0)), Herbst bis Frühjahr H · v mit H = ((0,3; 0), (0,01; 0)); Frühjahr zu Frühjahr J · u mit "
       "J = ((0,3; 150), (0,01; 5))")
row("2018MerhoehtBAGLAA1WTR", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Einträge einer Faktormatrix aus dem Produkt mit einer bekannten Matrix bestimmen", typ_neben="",
    stichwoerter="H · F = J|0,3 f1 = 0,3, 0,3 f2 = 150|f1 = 1, f2 = 500",
    voraussetzungen="Hintereinanderausführung als Matrixprodukt|Koeffizientenvergleich",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Springkraut/Population", textumfang="lang",
    gegeben=SPR,
    gesucht="Werte von f1 und f2",
    verfahren="H · F = J ausmultiplizieren und vergleichen",
    schritte="2", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="H · F = J ⇔ ((0,3 f1; 0,3 f2), (0,01 f1; 0,01 f2)) = J ⇔ f1 = 1 ∧ f2 = 500 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="F · H statt H · F bilden (Reihenfolge der Schritte)",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBAGLAA1WTR", "b", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zustände nach einem und zwei Schritten aus einem Anfangszustand berechnen", typ_neben="",
    stichwoerter="J · (1000; 0) = (300; 10)|J · (300; 10) = (1590; 53)",
    voraussetzungen="Matrix mal Vektor",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Springkraut/Population", textumfang="kurz",
    gegeben=SPR + "; zu Frühjahrsbeginn 1000 Samen, keine Pflanzen",
    gesucht="Samen und Pflanzen zu Beginn des nächsten und des übernächsten Frühjahrs",
    verfahren="J zweimal anwenden",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="J · (1000; 0) = (300; 10); J · (300; 10) = (1590; 53) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="im zweiten Schritt wieder vom Anfangszustand ausgehen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBAGLAA1WTR", "c", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unmöglichkeit eines konstanten Zustands über eine negative Lösung begründen", typ_neben="",
    stichwoerter="0,01 S + 5P = P|S = −400P < 0|negative Samenzahl nicht sinnvoll",
    voraussetzungen="Zeile der Übergangsgleichung|Sachprüfung einer Lösung",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Springkraut/Population", textumfang="mittel",
    gegeben=SPR + "; zu Frühjahrsbeginn Samen und Pflanzen vorhanden",
    gesucht="ob die Pflanzenzahl bis zum nächsten Frühjahr unverändert bleiben kann",
    verfahren="Zweite Zeile von J · (S; P) = (…; P) nach S auflösen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="0,01 S + 5P = P liefert S = −400P < 0; eine negative Samenzahl ist nicht sinnvoll, im Modell also nicht möglich (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="beide Komponenten konstant fordern (Fixvektor)",
    bemerkung="Standardbezug: K1 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBAGLAA1WTR", "d", innen="2", seite="2", punkte="7", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Anteil zu entfernender Individuen für einen stationären Zustand berechnen", typ_neben="",
    stichwoerter="Zustand (S; P3) vor dem Entfernen, (S; P4) danach|J · (S; P4) = (S; P3)|0,3 S + 150 P4 = S ⇒ S = 1500/7 P4|0,01 S + 5 P4 = P3 ⇒ P3 = 50/7 P4|Anteil 1 − 7/50 = 86 %",
    voraussetzungen="Bedingung in ein Gleichungssystem übersetzen|Verhältnis der Pflanzenzahlen|Anteil in Prozent",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Springkraut/Population", textumfang="lang",
    gegeben=SPR + "; zu Frühjahrsbeginn wird ein Anteil der Pflanzen entfernt, sodass der Zustand zum nächsten Frühjahr mit dem vor dem Entfernen übereinstimmt",
    gesucht="Anteil der zu entfernenden Pflanzen in Prozent",
    verfahren="J · (S; P4) = (S; P3) als Gleichungssystem, S eliminieren, P4/P3 = 7/50",
    schritte="4", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="J · (S; P4) = (S; P3): 0,3 S + 150 P4 = S und 0,01 S + 5 P4 = P3; mit S = 1500/7 · P4 folgt P3 = 50/7 · P4 = 7,14 P4; entfernt werden 86 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Fixvektor von J suchen (existiert nicht)",
    bemerkung="Standardbezug: K2 III, K3 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Bedingung „Zustand nach einem Jahr gleich Zustand vor dem Entfernen“ erst in J · (S; P4) = (S; P3) übersetzen.")
# ---- AG/LA (A2) WTR 1: Quader (25 BE), Teilaufgaben a, b, d, e, f wortgleich mit dem grundlegenden Pool A2 WTR 1
QUA = ("Quader mit den Eckpunkten A(4 | 0 | 0), B(4 | 4 | 0), C(0 | 4 | 0) und F(4 | 4 | 3); die Gerade h verläuft "
       "durch B und F; P_t(4 | 4 | t) auf h, Ebenenschar E_t: t x1 + t x2 − 4 x3 − 4t = 0 durch A, C und P_t")
QUA_SK = ("Schrägbild auf Gitter: Quader mit Grundfläche OABC in der x1x2-Ebene (Kantenlänge 4) und Höhe 3, "
          "Beschriftungen A, B, C, F, Achsen x1, x2, x3; die Gerade h als senkrechte Gerade durch B und F über den "
          "Quader hinaus; gepunktet die Schnittfigur einer Ebene E_t durch A und C (Viereck mit Ecken auf den "
          "senkrechten Kanten über A und C).")
row("2018MerhoehtBAGLAA2WTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Rechtwinkliges gleichschenkliges Dreieck aus den Koordinaten begründen und Flächeninhalt angeben", typ_neben="",
    stichwoerter="OABC Quadrat mit Seite 4|ABC halbes Quadrat, rechter Winkel bei B|Flächeninhalt 8",
    voraussetzungen="Quadrat aus Koordinaten|halbes Quadrat",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text|Zahl",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="kurz",
    gegeben=QUA,
    gesucht="Begründung, dass ABC rechtwinklig und gleichschenklig ist; Flächeninhalt",
    verfahren="OABC ist ein Quadrat, ABC eine Hälfte",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="OABC ist ein Quadrat, also ABC rechtwinklig und gleichschenklig; Flächeninhalt 8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="rechten Winkel bei A vermuten",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem grundlegenden Pool A2 WTR 1 a; Typ von dort.")
row("2018MerhoehtBAGLAA2WTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Geradengleichung durch zwei Punkte aufstellen und windschiefe Lage begründen", typ_neben="",
    stichwoerter="x = (4; 0; 0) + u · (−1; 1; 0)|h trifft die x1x2-Ebene nur in B, AC liegt in der Ebene ohne B|windschief",
    voraussetzungen="Parameterform|windschief über die Lage in einer Koordinatenebene",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Term|Text",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="kurz",
    gegeben=QUA,
    gesucht="Gleichung der Geraden AC; Begründung der Windschiefe zu h",
    verfahren="Richtungsvektor AC; h schneidet die x1x2-Ebene nur in B",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="x = (4; 0; 0) + u · (−1; 1; 0), u ∈ IR; h schneidet die x1x2-Ebene in B, AC liegt in dieser Ebene und geht nicht durch B (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur fehlende Parallelität nennen",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem grundlegenden Pool A2 WTR 1 b; Typ von dort.")
row("2018MerhoehtBAGLAA2WTR1", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharparameter für einen vorgegebenen Winkel zwischen Ebene und Scharebene berechnen", typ_neben="",
    stichwoerter="Normalenvektor (t; t; −4), x1x2-Ebene (0; 0; 1)|cos 60° = 4/√(2t² + 16) = 1/2|2t² + 16 = 64|t = ±√24",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren|Wurzelgleichung mit Parameter",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=QUA,
    gesucht="Werte von t, für die E_t mit der x1x2-Ebene einen Winkel von 60° einschließt",
    verfahren="cos 60° = |n_t · e3|/(|n_t| · |e3|) nach t lösen",
    schritte="3", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="4/√(2t² + 16) = cos 60° ⇔ 2t² + 16 = 64 ⇔ t = −√24 ∨ t = √24 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die negative Lösung vergessen",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B MMS).")
row("2018MerhoehtBAGLAA2WTR1", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Koordinate eines Punktes aus der Schnittfigur zeichnerisch ermitteln und Vorgehen beschreiben", typ_neben="",
    stichwoerter="Seite der Schnittfigur bis zur Geraden h verlängern|x3-Koordinate des Schnittpunkts ist t = 6",
    voraussetzungen="Schnittfigur im Schrägbild|Verlängerung einer Schnittkante",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="mittel",
    gegeben=QUA + "; eine Ebene E_t zerlegt den Quader, die Schnittfigur ist gepunktet abgebildet",
    gesucht="Beschreibung, wie man mithilfe der Abbildung t = 6 ermittelt",
    verfahren="Passende Seite der Schnittfigur bis h verlängern, x3 des Schnittpunkts ablesen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Verlängert man eine passende Seite der Schnittfigur bis zur Geraden h, stimmt die x3-Koordinate des Schnittpunkts mit t überein (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P_t innerhalb der Schnittfigur suchen",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich. Wortgleich (bis auf t statt 6) mit dem grundlegenden Pool A2 WTR 1 c; Typ von dort.")
row("2018MerhoehtBAGLAA2WTR1", "e", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen eines Teilkörpers als Differenz zweier Pyramiden berechnen und erläutern", typ_neben="",
    stichwoerter="Pyramide ABCP_6: 1/3 · 8 · 6 = 16|Ergänzungspyramide 1/3 · 2 · 3 = 2|Teilkörper 14",
    voraussetzungen="Pyramidenvolumen|Differenzansatz",
    format="Rechnung|Begründung", operator="Berechnen Sie|Erläutern Sie", antwort="Zahl|Text",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="mittel",
    gegeben=QUA + "; E_6 zerlegt den Quader in zwei Teilkörper",
    gesucht="Volumen des Teilkörpers mit B, mit Erläuterung",
    verfahren="Pyramide ABCP_6 minus die Pyramide über der Deckfläche",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2018MerhoehtBAGLAA2WTR1-1d",
    ergebnis="V(ABCP_6) = 1/3 · 8 · 6 = 16, Ergänzungspyramide 1/3 · 2 · 3 = 2, Teilkörper 16 − 2 = 14 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den über den Quader hinausragenden Teil nicht abziehen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem grundlegenden Pool A2 WTR 1 d; Typ von dort.")
row("2018MerhoehtBAGLAA2WTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben", typ_neben="",
    stichwoerter="Dreieck für t ∈ [−3; 3] ohne 0|Ecken A und C stets|0 < t ≤ 3: dritte Ecke auf BF, −3 ≤ t < 0: auf der gegenüberliegenden Kante",
    voraussetzungen="Schnittfigur nach Lage von P_t|Quaderhöhe 3",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl|Text",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="mittel",
    gegeben=QUA + "; für manche t ist die Schnittfigur ein Dreieck",
    gesucht="alle t mit Dreieck; Lage der Eckpunkte in Abhängigkeit von t",
    verfahren="|t| ≤ 3, t ≠ 0; Fallunterscheidung nach dem Vorzeichen von t",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="t ∈ [−3; 3] ohne 0; zwei Ecken sind stets A und C, die dritte liegt für 0 < t ≤ 3 auf BF, für −3 ≤ t < 0 auf der gegenüberliegenden Seitenkante (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="t = 0 nicht ausschließen",
    bemerkung="Standardbezug: K2 III, K4 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (b) Fallunterscheidung nach dem Vorzeichen von t. Wortgleich mit dem grundlegenden Pool A2 WTR 1 f; Typ wiederverwendet (2022-ea-B).")
row("2018MerhoehtBAGLAA2WTR1", "g", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Aufgabenstellung zum Abstand eines Punktes von einer Scharebene aus dem Lösungsweg formulieren", typ_neben="",
    stichwoerter="Betrag von (t · 4 + t · 4 − 4 · 0 − 4t) durch √(t² + t² + 16) gleich 2|Hessesche Normalform mit B eingesetzt|t = ±2√2|Aufgabe: Werte von t, für die B von E_t den Abstand 2 hat",
    voraussetzungen="Hessesche Normalform erkennen|eingesetzte Koordinaten als Punkt B deuten",
    format="Begründung", operator="Formulieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=QUA + "; Lösung einer Aufgabe: (t · 4 + t · 4 − 4 · 0 − 4t)/√(t² + t² + 16) = 2 ⇔ t = −2√2 ∨ t = 2√2",
    gesucht="eine passende Aufgabenstellung",
    verfahren="Term als Abstand des Punktes (4 | 4 | 0) = B von E_t lesen",
    schritte="1", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="Bestimmen Sie diejenigen Werte von t, für die B und E_t den Abstand 2 voneinander haben (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die eingesetzten Koordinaten nicht als B erkennen",
    bemerkung="Standardbezug: K1 III, K4 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (t = ±2√2). Eichregel: (d) sinngemäß – den Lösungsterm in eine Sachaussage (Abstand Punkt–Ebene) zurückübersetzen.")
# ---- AG/LA (A2) WTR 2: Kletteranlage (25 BE); a, c, d wortgleich mit dem grundlegenden Pool A2 WTR 2 und 2018-be-gk 2.2
KLE = ("Kletteranlage im Koordinatensystem (x1x2-Ebene ist der Untergrund, 1 LE = 1 m): Pfähle durch P1(0 | 0 | 0) und "
       "P2(5 | 10 | 0); Kletterwand mit den Eckpunkten A(3 | 0 | 2), B(0 | 3 | 2), E(6 | 0 | 0), F(0 | 6 | 0); "
       "Plattform 2 mit den Eckpunkten R(5 | 7 | 3), S(8 | 13 | 3), T(2 | 10 | 3)")
KLE_SK = ("Schrägbild eines räumlichen Koordinatensystems mit zwei waagerechten Plattformen um senkrechte Pfähle "
          "(Plattform 1 in Höhe 2 um den Pfahl durch P1, Plattform 2 in Höhe 3 um den Pfahl durch P2) und der "
          "geneigten Kletterwand ABFE zwischen Plattform 1 und dem Untergrund; Beschriftungen A, B, E, F, R, S, T.")
row("2018MerhoehtBAGLAA2WTR2", "a", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Streckenlänge im Raum berechnen", typ_neben="Punkt: Mittelpunkt einer Strecke im Raum bestimmen",
    stichwoerter="M1(1,5 | 1,5 | 2), M2(3 | 3 | 0)|1,2 · √(1,5² + 1,5² + 4) ≈ 3,5",
    voraussetzungen="Mittelpunkt|Betrag|Prozentaufschlag",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="mittel",
    gegeben=KLE + "; Seil zwischen den Mittelpunkten von AB und EF, 20 % länger als deren Abstand",
    gesucht="Länge des Seils",
    verfahren="Mittelpunkte, Abstand, mal 1,2",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="1,2 · |M1M2| = 1,2 · √(1,5² + 1,5² + 4) ≈ 3,5 m (amtlich)",
    zwischenergebnis="M1(1,5 | 1,5 | 2), M2(3 | 3 | 0)", niveau_geschaetzt="I",
    fehlerquelle="20 % des Abstands als Seillänge",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem grundlegenden Pool A2 WTR 2 a und dem Landesheft 2018-be-gk 2.2 a; Typen von dort.")
row("2018MerhoehtBAGLAA2WTR2", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen", typ_neben="",
    stichwoerter="EF = (−6; 6; 0) = 2 · AB|AB ∥ EF",
    voraussetzungen="Vektoren auf Vielfache prüfen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="kurz",
    gegeben=KLE + "; A, B, E, F in L: 2x1 + 2x2 + 3x3 − 12 = 0",
    gesucht="Nachweis, dass die Kletterwand ein Trapez ist",
    verfahren="EF als Vielfaches von AB",
    schritte="1", zahlenraum="ganz|negativ", einheiten="m", abhaengig_von="",
    ergebnis="EF = 2 · AB, also AB ∥ EF (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Parallelität über gleiche Länge prüfen",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Definition deckt den Nachweis ohne Flächeninhalt); der grundlegende Pool verlangt zusätzlich gleich lange Seiten.")
row("2018MerhoehtBAGLAA2WTR2", "c", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="n = (2; 2; 3), e3 = (0; 0; 1)|cos α = 3/√17|α ≈ 43°",
    voraussetzungen="Winkel zwischen Ebenen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="kurz",
    gegeben=KLE + "; L: 2x1 + 2x2 + 3x3 − 12 = 0",
    gesucht="Winkel zwischen Kletterwand und Untergrund",
    verfahren="cos α über die Normalenvektoren",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="Grad", abhaengig_von="",
    ergebnis="cos α = 3/√17, α ≈ 43° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Komplementwinkel angeben",
    bemerkung="Standardbezug: K2 I, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem grundlegenden Pool A2 WTR 2 c und 2018-be-gk 2.2 c; Typ von dort.")
row("2018MerhoehtBAGLAA2WTR2", "d", innen="1", seite="2", punkte="6", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punktprobe an einer Geraden durchführen",
    typ_neben="Schattenpunkt bei paralleler Projektion bestimmen|Ebene Figur: Schatten einer Fläche in eine Abbildung einzeichnen",
    stichwoerter="ET' = 5/6 · EF|Lichtrichtung RR' = (−1; −5; −3)|S' = (7 | 8 | 0)|Schatten einzeichnen",
    voraussetzungen="Punkt auf einer Strecke|Richtungsvektor aus Punkt und Schattenpunkt|Verschiebung|Schrägbild",
    format="Begründung|Rechnung|Zeichnen", operator="Zeigen Sie|Berechnen Sie|Stellen Sie dar", antwort="Text|Zahl|Grafik",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="mittel",
    gegeben=KLE + "; Sonnenlicht als parallele Geraden; Schattenpunkte R'(4 | 2 | 0), S', T'(1 | 5 | 0)",
    gesucht="Nachweis, dass T' auf der Strecke EF liegt; Koordinaten von S'; Schatten der Plattform 2 in der Abbildung",
    verfahren="ET' = 5/6 · EF; S' = S + RR'; Dreieck R'S'T' einzeichnen",
    schritte="4", zahlenraum="ganz|negativ|Bruch", einheiten="m", abhaengig_von="",
    ergebnis="ET' = 5/6 · EF, also T' auf EF; S' = (8; 13; 3) + (−1; −5; −3) = (7 | 8 | 0); Schatten als Dreieck R'S'T' (amtlich)",
    zwischenergebnis="RR' = (−1; −5; −3)", niveau_geschaetzt="II",
    fehlerquelle="Parameterbereich beim Streckennachweis weglassen",
    bemerkung="Standardbezug: K1 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem grundlegenden Pool A2 WTR 2 d und 2018-be-gk 2.2 d; Typen von dort.")
NETZ = ("Kletternetz als ebenes Viereck zwischen den Pfählen: untere Ecken bei (0 | 0 | 2) am Pfahl 1 und oberhalb "
        "der Plattform 2 am Pfahl 2, an jedem Pfahl Abstand 1,80 m zwischen den beiden dort befestigten Ecken")
row("2018MerhoehtBAGLAA2WTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines ebenen Vierecks mit zwei parallelen senkrechten Seiten aus Seitenlänge und Pfahlabstand berechnen", typ_neben="",
    stichwoerter="zwei parallele senkrechte Seiten der Länge 1,8|Abstand der Pfähle √125|Fläche 1,8 · √125 ≈ 20",
    voraussetzungen="Parallelogramm mit senkrechten Seiten|Abstand der Pfähle als Höhe",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="mittel",
    gegeben=KLE + "; " + NETZ,
    gesucht="Flächeninhalt des Netzes",
    verfahren="Grundseite 1,8 mal Abstand der Pfähle",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="m²", abhaengig_von="",
    ergebnis="1,8 · |P1P2| = 9√5 ≈ 20; das Netz hat etwa 20 m² (amtlich)",
    zwischenergebnis="|P1P2| = √125", niveau_geschaetzt="II",
    fehlerquelle="das Netz als Rechteck mit der Seillänge statt dem Pfahlabstand rechnen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (20,12).")
row("2018MerhoehtBAGLAA2WTR2", "f", innen="1", seite="2", punkte="8", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Höhe des Endpunkts einer Strecke auf einer senkrechten Geraden über den Schnitt mit einer Kante berechnen", typ_neben="",
    stichwoerter="U(5 | 10 | z_U) am Pfahl 2|Gerade durch (0 | 0 | 2) und U: x = (0; 0; 2) + λ · (5; 10; z_U − 2)|Gerade RT: x = (5; 7; 3) + μ · (−3; 3; 0)|Gleichsetzen: λ = 0,8, μ = 1/3|2 + 0,8 (z_U − 2) = 3 ⇒ z_U = 3,25|Abstand 0,25 m",
    voraussetzungen="Gerade durch zwei Punkte mit unbekannter Koordinate|Schnitt zweier Geraden|Höhendifferenz",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="lang",
    gegeben=KLE + "; " + NETZ + "; die untere Netzkante berührt die Plattform 2 an der Seite RT",
    gesucht="Abstand des unteren Eckpunkts am Pfahl 2 von der Plattform 2",
    verfahren="Untere Netzkante als Gerade durch (0 | 0 | 2) und U(5 | 10 | z_U), Schnitt mit der Geraden RT aus den ersten beiden Koordinaten, dritte Gleichung liefert z_U",
    schritte="5", zahlenraum="dezimal|Bruch", einheiten="m", abhaengig_von="",
    ergebnis="Aus 5λ = 5 − 3μ und 10λ = 7 + 3μ folgt λ = 0,8; 2 + 0,8 · (z_U − 2) = 3 liefert z_U = 3,25, der Abstand beträgt 25 cm (amtlich)",
    zwischenergebnis="μ = 1/3", niveau_geschaetzt="III",
    fehlerquelle="U auf der Höhe 3 der Plattform ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Berührbedingung in den Schnitt der Netzkante mit der Geraden RT übersetzen, mit unbekannter Höhe als Variable. Rechnerische Fassung der Beschreibungsaufgabe A2 WTR 2 e des grundlegenden Pools.")
# ---- AG/LA (A2) WTR 3: Beachvolleyball (25 BE)
BEA = ("Beachvolleyballfeld im Koordinatensystem (1 LE = 1 m, x1x2-Ebene ist der Sandboden): Spielfeld ABCD 8 m × 16 m, "
       "Netzoberkante zwischen E und F(−1 | 8 | 2,4) in 2,4 m Höhe; Tribüne als Viereck GHIJ mit G(−4 | 0 | 0), "
       "H(−4 | 16 | 0), I(−10 | 20 | 4), J(−10 | −4 | 4) in L: 2x1 + 3x3 = −8")
BEA_SK = ("Schrägbild: Spielfeld ABCD als Rechteck in der Grundebene (A nahe dem Ursprung, B in x1-Richtung bei 8, D in "
          "x2-Richtung bei 16), das Netz als dunkle Fläche zwischen den Pfosten E und F quer über die Mitte, links "
          "daneben die Tribüne als große geneigte graue Fläche GHIJ, die von G und H am Boden zu I und J in Höhe 4 "
          "ansteigt; Achsen x1, x2, x3 beschriftet.")
row("2018MerhoehtBAGLAA2WTR3", "a", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen", typ_neben="",
    stichwoerter="GH = (0; 16; 0), IJ = (0; −24; 0) kollinear|GJ = (−6; −4; 4), HI = (−6; 4; 4), beide Länge √68",
    voraussetzungen="kollineare Vektoren|Beträge vergleichen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Körper", skizze=BEA_SK, kontext="Beachvolleyball", textumfang="mittel",
    gegeben=BEA,
    gesucht="Nachweis, dass die Tribüne ein Trapez mit zwei gleich langen gegenüberliegenden Seiten ist",
    verfahren="GH und IJ kollinear; |GJ| = |HI|",
    schritte="2", zahlenraum="ganz|negativ|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="GH = (0; 16; 0) und IJ = (0; −24; 0) sind kollinear; |GJ| = |HI| = √68 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="GJ und HI als parallel nachweisen wollen",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Definition deckt den Nachweis ohne Flächeninhalt, wie beim grundlegenden Pool A2 WTR 2 b).")
row("2018MerhoehtBAGLAA2WTR3", "b", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Zuschauerzahl aus dem Flächeninhalt eines Trapezes im Raum und dem Platzbedarf berechnen", typ_neben="",
    stichwoerter="Mittelpunkte M(−4 | 8 | 0) von GH und N(−10 | 8 | 4) von IJ|Höhe |MN| = √52|Fläche 1/2 (16 + 24) · √52 ≈ 144|144/0,5 = 288",
    voraussetzungen="Trapezformel mit Höhe als Abstand der Mittelpunkte|Division durch den Platzbedarf",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=BEA_SK, kontext="Beachvolleyball", textumfang="kurz",
    gegeben=BEA + "; pro Person 0,5 m² der Tribüne",
    gesucht="Anzahl der Zuschauer für eine voll besetzte Tribüne",
    verfahren="Trapezhöhe als Abstand der Seitenmittelpunkte, Fläche, durch 0,5",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="m²", abhaengig_von="",
    ergebnis="1/2 · (|GH| + |IJ|) · |MN| ≈ 144; 144/0,5 = 288 Zuschauer (amtlich)",
    zwischenergebnis="M(−4 | 8 | 0), N(−10 | 8 | 4)", niveau_geschaetzt="II",
    fehlerquelle="die Schenkellänge √68 als Höhe verwenden",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (144,2).")
row("2018MerhoehtBAGLAA2WTR3", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen", typ_neben="",
    stichwoerter="|2 · (−1) + 3 · 2,4 + 8|/√13 ≈ 3,7",
    voraussetzungen="Hessesche Normalform",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Beachvolleyball", textumfang="kurz",
    gegeben=BEA,
    gesucht="Abstand des Punktes F von der Ebene L",
    verfahren="Koordinaten von F in die normierte Ebenengleichung einsetzen",
    schritte="1", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="|2 · (−1) + 3 · 2,4 + 8|/√13 ≈ 3,7 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Normalenvektor (2; 0; 3) nicht normieren",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (3,66). Typ wiederverwendet (2017-bb-ea). Geschätzt I (eine Rechnung), amtlich II.")
row("2018MerhoehtBAGLAA2WTR3", "d", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lotfußpunkt außerhalb einer Figur als Grund für größere Abstände aller Figurpunkte zeichnerisch begründen", typ_neben="",
    stichwoerter="Lot von F auf L|Lotfußpunkt liegt außerhalb des Vierecks GHIJ|jeder Punkt des Vierecks ist weiter von F entfernt als der Lotfußpunkt",
    voraussetzungen="Abstand Punkt–Ebene wird nur im Lotfußpunkt angenommen|Lage des Lotfußpunkts in einer Skizze",
    format="Begründung|Zeichnen", operator="Begründen Sie", antwort="Text|Grafik",
    material="Körper", skizze=BEA_SK, kontext="Beachvolleyball", textumfang="mittel",
    gegeben=BEA + "; Abstand von F zu L etwa 3,7",
    gesucht="Begründung anhand einer Zeichnung, dass kein Punkt des Vierecks GHIJ von F den Abstand 3,7 hat",
    verfahren="Skizze mit Lotfußpunkt außerhalb des Vierecks; nur dort wird der Ebenenabstand angenommen",
    schritte="2", zahlenraum="dezimal", einheiten="m", abhaengig_von="2018MerhoehtBAGLAA2WTR3-1c",
    ergebnis="Der Fußpunkt des Lots von F auf L liegt außerhalb des Vierecks; damit sind die Abstände aller Punkte des Vierecks von F größer als der Abstand der Ebene L von F (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="den Lotfußpunkt rechnerisch bestimmen statt zeichnerisch begründen",
    bemerkung="Standardbezug: K1 II, K4 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (a) sinngemäß – die Abstandsaussage in die Lage des Lotfußpunkts zur Figur übersetzen.")
row("2018MerhoehtBAGLAA2WTR3", "e", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Berühren einer Geraden mit einem Netz über die Höhe des Durchstoßpunkts in der Netzebene untersuchen", typ_neben="",
    stichwoerter="Ball von (2 | 7,5 | 3) in Richtung (0; 4; −3)|Netzebene x2 = 8 nach 0,5 in x2-Richtung, also λ = 1/8|x3 = 3 − 0,375 = 2,625 > 2,4|berührt nicht",
    voraussetzungen="Netz als Teil der Ebene x2 = 8|Parameter aus einer Koordinate|Höhenvergleich",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Körper", skizze=BEA_SK, kontext="Beachvolleyball", textumfang="mittel",
    gegeben=BEA + "; Ball bewegt sich von (2 | 7,5 | 3) geradlinig in Richtung (0; 4; −3)",
    gesucht="rechnerische Untersuchung, ob der Ball das Netz berührt",
    verfahren="Weg bis x2 = 8 (0,5), zugehörige Abnahme der Höhe 0,375, Vergleich mit 2,4",
    schritte="3", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="Bis zur Netzebene 0,5 in x2-Richtung und 0,375 nach unten: 3 − 0,375 = 2,625 > 2,4, der Ball berührt das Netz nicht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Netzebene x1 = const annehmen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
BAHN = "Bahn des Balls nach dem Aufschlag: X_t(3 | 12t − 1 | −5t² + 4t + 2,8), t Zeit in Sekunden; der Ball überfliegt das Netz"
row("2018MerhoehtBAGLAA2WTR3", "f", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Achsenparallele Ebene einer Bewegung aus der Parameterdarstellung angeben", typ_neben="",
    stichwoerter="x1 = 3 für alle t|Ebene x1 = 3",
    voraussetzungen="konstante Koordinate als Ebene",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text|Term",
    material="keins", skizze="keine", kontext="Beachvolleyball", textumfang="kurz",
    gegeben=BEA + "; " + BAHN,
    gesucht="Begründung, dass sich der Ball in einer Ebene bewegt; Gleichung dieser Ebene",
    verfahren="Alle X_t haben x1 = 3",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Alle Punkte X_t haben die x1-Koordinate 3; Ebene x1 = 3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Ebene in Parameterform mit t suchen",
    bemerkung="Standardbezug: K1 I, K3 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2023-ea-B).")
row("2018MerhoehtBAGLAA2WTR3", "g", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Auftreffpunkt einer Bahnkurve auf der Grundebene berechnen und Lage innerhalb des Spielfelds prüfen", typ_neben="",
    stichwoerter="−5t² + 4t + 2,8 = 0, t ≥ 0: t ≈ 1,25|x2 ≈ 12 · 1,25 − 1 = 14 < 16, x1 = 3|innerhalb des Spielfelds",
    voraussetzungen="Auftreffen als x3 = 0|quadratische Gleichung, positive Lösung|Feldgrenzen",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Körper", skizze=BEA_SK, kontext="Beachvolleyball", textumfang="mittel",
    gegeben=BEA + "; " + BAHN,
    gesucht="ob der Ball innerhalb des Spielfelds auf dem Boden auftrifft",
    verfahren="x3 = 0 nach t lösen, Auftreffpunkt mit den Feldgrenzen vergleichen",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="−5t² + 4t + 2,8 = 0 liefert für t ≥ 0 t ≈ 1,25; X_t mit x3 = 0 hat x2 ≈ 14, also trifft der Ball innerhalb des Spielfelds auf (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur die Zeit berechnen und die Lage nicht prüfen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (t = 1,249, x2 = 13,98). Eichregel: (a) „trifft auf dem Boden auf“ in x3 = 0 und „innerhalb des Spielfelds“ in Koordinatenschranken übersetzen.")
# ---- Stochastik WTR 1: Kunststoffteile (Aufgabe 1, 15 BE), Glücksrad (Aufgabe 2, 10 BE)
KUN = "Kunststoffteile, 4 % fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten ist binomialverteilt"
row("2018MerhoehtBStochastikWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="X ~ B(50; 0,04)|P(X = 2) ≈ 27,6 %|mindestens 6 % von 50 = mindestens 3: P(X ≥ 3) = 1 − P(X ≤ 2) ≈ 32,3 %",
    voraussetzungen="Binomialverteilung am Rechner|Anteil in Anzahl umrechnen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Qualität", textumfang="kurz",
    gegeben=KUN + "; 50 Teile zufällig ausgewählt",
    gesucht="P(A): genau zwei fehlerhaft; P(B): mindestens 6 % fehlerhaft",
    verfahren="Einzel- und kumulierte Wahrscheinlichkeit mit n = 50, p = 0,04",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(A) = P(X = 2) ≈ 27,6 %; 6 % · 50 = 3, P(B) = P(X ≥ 3) = 1 − P(X ≤ 2) ≈ 32,3 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="„mindestens 6 %“ als X ≥ 6 lesen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,2762; 0,3233). Typen wiederverwendet.")
row("2018MerhoehtBStochastikWTR1", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen für mindestens drei Treffer mit vorgegebener Wahrscheinlichkeit durch Probieren ermitteln", typ_neben="",
    stichwoerter="Y: Anzahl fehlerfreier Teile, p = 0,96|n = 3: P(Y ≥ 3) = 0,96³ ≈ 88,5 % < 95 %|n = 4: P(Y ≥ 3) = 1 − P(Y ≤ 2) ≈ 99,1 %|mindestens vier Teile",
    voraussetzungen="Trefferdefinition wechseln (fehlerfrei)|kumulierte Wahrscheinlichkeit für kleine n prüfen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Qualität", textumfang="mittel",
    gegeben=KUN,
    gesucht="Mindestanzahl zufällig ausgewählter Teile, sodass mit mindestens 95 % mindestens drei fehlerfrei sind",
    verfahren="n = 3 und n = 4 mit Y ~ B(n; 0,96) prüfen",
    schritte="3", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(Y ≥ 3) ≈ 88,5 % für n = 3, ≈ 99,1 % für n = 4; es müssen mindestens vier Teile ausgewählt werden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit p = 0,04 (fehlerhaft) statt 0,96 rechnen",
    bemerkung="Standardbezug: K1 I, K2 III, K3 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Geschätzt II (Verkettung: Trefferwechsel, zwei kumulierte Werte), amtlich III.")
row("2018MerhoehtBStochastikWTR1", "c", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel eines einseitigen Signifikanztests bestimmen", typ_neben="",
    stichwoerter="H0: p ≥ 0,04, n = 200, α = 5 %|linksseitig: P(X ≤ k) ≤ 0,05 ⇔ k ≤ 3|Ablehnung bei höchstens drei fehlerhaften Teilen",
    voraussetzungen="Ablehnungsbereich links|kumulierte Wahrscheinlichkeit gegen α",
    format="Rechnung", operator="Bestimmen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Produktion/Qualität", textumfang="mittel",
    gegeben=KUN + "; nach Granulatwechsel Test der Nullhypothese „Anteil fehlerhafter Teile mindestens 4 %“ mit n = 200 auf dem Niveau 5 %",
    gesucht="zugehörige Entscheidungsregel",
    verfahren="Größtes k mit P(X ≤ k) ≤ 0,05 für B(200; 0,04)",
    schritte="2", zahlenraum="Prozent|ganz", einheiten="", abhaengig_von="",
    ergebnis="P(X ≤ k) ≤ 5 % ⇔ k ≤ 3; sind höchstens drei der 200 Teile fehlerhaft, wird die Nullhypothese abgelehnt (amtlich)",
    zwischenergebnis="P(X ≤ 3) ≈ 0,040, P(X ≤ 4) ≈ 0,095", niveau_geschaetzt="II",
    fehlerquelle="rechtsseitig testen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")
row("2018MerhoehtBStochastikWTR1", "d", innen="1", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Wahl der Nullhypothese aus der Sicht des Entscheiders begründen", typ_neben="",
    stichwoerter="teures Granulat soll nicht ohne Nutzen dauerhaft eingesetzt werden|Fehler erster Art: irrtümlich eine Reduktion annehmen|höchstens 5 %",
    voraussetzungen="Fehler erster Art als kontrollierter Fehler|Nullhypothese als das, was man absichern will",
    format="Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Produktion/Qualität", textumfang="mittel",
    gegeben=KUN + "; H0: Anteil mindestens 4 %; das neue Granulat ist teurer",
    gesucht="Überlegung, die zur Wahl der Nullhypothese geführt haben könnte, mit Begründung",
    verfahren="Der teure Wechsel soll nur bei nachgewiesener Verbesserung erfolgen; das Risiko, irrtümlich eine Reduktion anzunehmen, ist durch α begrenzt",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Es soll vermieden werden, das teurere Granulat dauerhaft einzusetzen, obwohl sich der Anteil nicht reduziert hat; das Risiko, irrtümlich von einer Reduktion auszugehen, beträgt höchstens 5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit dem Fehler zweiter Art argumentieren",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. AB amtlich: III. Amtlich. Typ wiederverwendet (2024-ea-B). Geschätzt II, amtlich III.")
GLU = ("Glücksrad mit den Sektoren Blau 180°, Rot 120°, Grün 60°; Einsatz 5 Euro für drei Drehungen; dreimal die gleiche "
       "Farbe: 10 Euro Auszahlung; drei verschiedene Farben: anderer Betrag; sonst nichts; P(dreimal gleiche Farbe) = 1/6")
row("2018MerhoehtBStochastikWTR1", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeit für drei verschiedene Ergebnisse über Pfadprodukt und Reihenfolgen nachweisen", typ_neben="",
    stichwoerter="P(B) = 1/2, P(R) = 1/3, P(G) = 1/6|3! Reihenfolgen|3! · 1/2 · 1/3 · 1/6 = 1/6",
    voraussetzungen="Sektorwinkel als Wahrscheinlichkeit|Anzahl der Reihenfolgen",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle mit den Farben Blau, Rot, Grün und den Mittelpunktswinkeln 180°, 120°, 60°.", kontext="Glücksspiel", textumfang="mittel",
    gegeben=GLU,
    gesucht="Nachweis, dass P(drei verschiedene Farben) = 1/6",
    verfahren="Pfadprodukt mal 3! Reihenfolgen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="3! · 1/2 · 1/3 · 1/6 = 1/6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Reihenfolgen vergessen (1/36)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2018MerhoehtBStochastikWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="Gewinn: 1/6 · (10 − 5) + 1/6 · (a − 5) + 4/6 · (−5) = 0|a = 20",
    voraussetzungen="Erwartungswert des Gewinns|faires Spiel als Erwartungswert null",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel", textumfang="kurz",
    gegeben=GLU + "; Einsätze und Auszahlungen gleichen sich auf lange Sicht aus",
    gesucht="Auszahlung bei drei verschiedenen Farben",
    verfahren="Erwartungswert des Gewinns gleich null setzen",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="Euro", abhaengig_von="2018MerhoehtBStochastikWTR1-2a",
    ergebnis="1/6 · (10 − 5) + 1/6 · (a − 5) − 4/6 · 5 = 0 ⇔ a = 20 Euro (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Einsatz bei den Auszahlungen nicht abziehen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet. „Faires Spiel“ bleibt gestrichen, hier amtlich II (vierter Beleg, 2 : 2 bleibt ein Patt, dieser Fall stützt die Streichung: 3 : 2).")
row("2018MerhoehtBStochastikWTR1", "c", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Sektorwinkel eines Glücksrads aus einer Wahrscheinlichkeitsbedingung berechnen", typ_neben="",
    stichwoerter="geändertes Rad: P(G) = p, P(R) = 2p, P(B) = 1 − 3p|Pfad R–B: 2p · (1 − 3p) = 0,14|6p² − 2p + 0,14 = 0, p = 0,1 (p < 1/6)|Blau 0,7 · 360° = 252°",
    voraussetzungen="Baumdiagramm mit Parameter lesen|quadratische Gleichung|Lösung über die Sachbedingung auswählen|Anteil in Winkel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm",
    skizze="Ausschnitt eines Baumdiagramms: erste Stufe mit den Ästen R (beschriftet 2p) und G; von R aus zweite Stufe B (Pfadwahrscheinlichkeit 0,14), R, G (beschriftet p).",
    kontext="Glücksspiel", textumfang="mittel",
    gegeben=GLU + "; geändertes Rad mit verkleinertem grünen Sektor; Baumdiagramm: P(R) = 2p, P(G) = p, Pfad Rot–Blau 0,14",
    gesucht="Mittelpunktswinkel des blauen Sektors",
    verfahren="P(B) = 1 − 3p, Pfadgleichung nach p lösen, kleinere Lösung wegen des verkleinerten grünen Sektors, Winkel",
    schritte="4", zahlenraum="dezimal", einheiten="Grad", abhaengig_von="",
    ergebnis="2p · (1 − 3p) = 0,14 ⇔ p = 0,1 (für p < 1/6); (1 − p − 2p) · 360° = 252° (amtlich)",
    zwischenergebnis="zweite Lösung p = 7/30 verworfen", niveau_geschaetzt="II",
    fehlerquelle="die zweite Lösung nicht ausschließen",
    bemerkung="Standardbezug: K2 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-A).")
# ---- Stochastik WTR 2: Bildschirme (25 BE); a wortgleich mit dem grundlegenden Pool WTR 2 a, d mit WTR 2 g
BIL = "Flachbildschirme, im Mittel einer von fünf fehlerhaft"
row("2018MerhoehtBStochastikWTR2", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="A: unter 50 höchstens 8, P ≈ 30,7 %|B: unter 200 mehr als 15 % und weniger als 25 %, also 31 bis 49: P ≈ 90,8 %",
    voraussetzungen="Anteile in Anzahlen umrechnen|kumulierte Wahrscheinlichkeit",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="mittel",
    gegeben=BIL + "; Anzahl fehlerhafter Geräte unter zufällig ausgewählten binomialverteilt (p = 0,2)",
    gesucht="P(A): von 50 höchstens 8 fehlerhaft; P(B): von 200 mehr als 15 % und weniger als 25 % fehlerhaft",
    verfahren="P(X ≤ 8) mit n = 50; P(30 < X < 50) mit n = 200",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(A) ≈ 30,7 %; P(B) = P(30 < X < 50) ≈ 90,8 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Prozentgrenzen 15 % und 25 % einschließen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Bis auf die Prozentangabe wortgleich mit dem grundlegenden Pool WTR 2 a (dort 30 und 50); Typ von dort.")
row("2018MerhoehtBStochastikWTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="D 10,7 %, weder noch 87,3 %, entweder D oder N 11,7 %|D∩N = 100 − 87,3 − 11,7 = 1,0 %|D∩¬N 9,7 %, ¬D∩N 2,0 %, N 3,0 %",
    voraussetzungen="Entweder-oder als Summe zweier Felder|Tafel aus drei Angaben ergänzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="mittel",
    gegeben="Für einen zufällig ausgewählten Bildschirm: Display defekt 10,7 %, weder Display noch Netzteil defekt 87,3 %, entweder Display oder Netzteil defekt 11,7 %",
    gesucht="vollständig ausgefüllte Vierfeldertafel",
    verfahren="D∩N aus 100 − 87,3 − 11,7; Rest als Differenzen",
    schritte="4", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="D∩N 1,0 %, ¬D∩N 2,0 %, D∩¬N 9,7 %, ¬D∩¬N 87,3 %; Ränder N 3,0 %, ¬N 97,0 %, D 10,7 %, ¬D 89,3 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="11,7 % als P(D ∪ N) lesen",
    bemerkung="Standardbezug: K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet. Das Landesheft 2018-be-gk 3.2 e ist hierauf als abgewandelt vorgemerkt (dort 3,0 % Netzteil vorgegeben, 3 BE) – es ist wortgleich mit dem grundlegenden Pool WTR 2 e, Umstellung dorthin im Abgleichlauf 15.")
row("2018MerhoehtBStochastikWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen", typ_neben="",
    stichwoerter="P(D) · P(N) = 0,107 · 0,03 = 0,00321 ≠ 0,01 = P(D ∩ N)|nicht unabhängig",
    voraussetzungen="Produktregel als Unabhängigkeitskriterium",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="kurz",
    gegeben="Vierfeldertafel aus b (D 10,7 %, N 3,0 %, D∩N 1,0 %)",
    gesucht="ob die beiden Defekte unabhängig voneinander auftreten",
    verfahren="Produkt der Randwahrscheinlichkeiten mit dem Schnitt vergleichen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2018MerhoehtBStochastikWTR2-1b",
    ergebnis="P(D) · P(N) = 0,107 · 0,03 = 0,00321 ≠ 0,01 = P(D ∩ N), die Defekte treten nicht unabhängig auf (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Unabhängigkeit mit Unvereinbarkeit verwechseln",
    bemerkung="Standardbezug: K1 I, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ea-A). Geschätzt I (ein Produktvergleich), amtlich II.")
row("2018MerhoehtBStochastikWTR2", "d", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Ungeeignetheit des Binomialmodells begründen", typ_neben="",
    stichwoerter="40 geprüfte, 6 fehlerhaft, 10 ausgewählt|binomial wären 7 fehlerhafte möglich|Widerspruch",
    voraussetzungen="Wertebereich einer Binomialverteilung|Ziehen ohne Zurücklegen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="kurz",
    gegeben="Von 40 geprüften Bildschirmen mit 6 fehlerhaften werden 10 zufällig ausgewählt",
    gesucht="Beurteilung, ob die Anzahl fehlerhafter Bildschirme unter den ausgewählten binomialverteilt ist",
    verfahren="Bei Binomialverteilung wären sieben fehlerhafte möglich",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Nicht binomialverteilt: sonst wären beispielsweise sieben fehlerhafte Bildschirme möglich, im Widerspruch zum Sachzusammenhang (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Binomialverteilung wegen zweier Ausgänge bejahen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich. Typ wiederverwendet. Wortgleich mit dem grundlegenden Pool WTR 2 g und dem Landesheft 2018-be-gk 3.2 g (dort hierauf vorgemerkt; Umstellung auf den grundlegenden Pool im Abgleichlauf 15).")
row("2018MerhoehtBStochastikWTR2", "e", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Mindestwert einer Erkennungswahrscheinlichkeit aus einer Bedingung an eine bedingte Wahrscheinlichkeit bestimmen", typ_neben="",
    stichwoerter="fehlerfrei stets als fehlerfrei eingestuft, fehlerhaft mit x als fehlerhaft|P(fehlerhaft | als fehlerfrei eingestuft) = 0,2 (1 − x)/(0,8 + 0,2 (1 − x)) ≤ 0,05|x ≥ 15/19",
    voraussetzungen="Bayes-Ansatz mit Parameter|Ungleichung mit Bruch lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="lang",
    gegeben=BIL + "; alle fehlerfreien werden als fehlerfrei eingestuft, ein fehlerhafter mit Wahrscheinlichkeit x als fehlerhaft; ein als fehlerfrei eingestufter Bildschirm wird ausgewählt",
    gesucht="kleinstmögliches x, sodass P(fehlerhaft | als fehlerfrei eingestuft) ≤ 5 %",
    verfahren="Bedingte Wahrscheinlichkeit über den Baum aufstellen und die Ungleichung nach x auflösen",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,2 · (1 − x)/(0,8 + 0,2 · (1 − x)) ≤ 0,05 ⇔ x ≥ 15/19; der kleinstmögliche Wert ist 15/19 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Bedingung umgekehrt ansetzen (als fehlerfrei eingestuft | fehlerhaft)",
    bemerkung="Standardbezug: K2 III, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (0,7895). Eichregel: (a) die Sachbedingung in eine Bayes-Ungleichung mit Parameter übersetzen.")
KON_SK = ("Koordinatensystem, p von 0 bis 0,3 waagerecht, f_k(p) bzw. g_k(p) von 0 bis 0,3 senkrecht, mit der "
          "Winkelhalbierenden als Bezug: vier vom Ursprung ausgehende, leicht gekrümmte Kurven, A (strichpunktiert) "
          "und B (durchgezogen) oberhalb, C (durchgezogen) und D (gepunktet) unterhalb der Winkelhalbierenden; A liegt "
          "über B, D unter C.")
row("2018MerhoehtBStochastikWTR2", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Konfidenzintervalle",
    typ="Konfidenzintervall aus den Graphen der Grenzfunktionen ablesen und eine Vermutung auf Verträglichkeit beurteilen", typ_neben="",
    stichwoerter="Stichprobenanteil 0,15|äußere Graphen A und D gehören zu 95 %|Intervall etwa [0,11; 0,21]|enthält 0,2, Aussage gestützt",
    voraussetzungen="Grenzfunktionen f_k und g_k|größeres k für höhere Sicherheit|Ablesen bei h = 0,15",
    format="Rechnung|Begründung", operator="Bestimmen Sie|Entscheiden Sie", antwort="Zahl|Text",
    material="Diagramm", skizze=KON_SK, kontext="Bildschirme/Produktion", textumfang="lang",
    gegeben=BIL + "; große Stichprobe mit 15 % fehlerhaften; Graphen A, B, C, D der Funktionen f_k(p) = p − k · √(p(1 − p)/n) und g_k(p) = p + k · √(p(1 − p)/n) für die Sicherheitswahrscheinlichkeiten 90 % und 95 %",
    gesucht="Konfidenzintervall zu 95 %; Entscheidung, ob die Aussage „einer von fünf fehlerhaft“ gestützt wird",
    verfahren="Die äußeren Graphen (größeres k) bei 0,15 schneiden und die p-Werte ablesen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Konfidenzintervall näherungsweise [0,11; 0,21]; es enthält 0,2, die Aussage kann gestützt werden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die inneren Graphen B und C (90 %) verwenden",
    bemerkung="Standardbezug: K3 II, K4 II. AB amtlich: II. Amtlich. Typ wiederverwendet (2025-ea-B).")
row("2018MerhoehtBStochastikWTR2", "g", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Konfidenzintervalle",
    typ="Länge eines Konfidenzintervalls bei doppeltem Stichprobenumfang über den Faktor 1/√2 begründen", typ_neben="",
    stichwoerter="Länge 2k · √(0,15 · 0,85/n)|bei 2n: 2k · √(0,15 · 0,85/(2n)) = 1/√2 · Länge|1/√2 < 1 und ≠ 1/2",
    voraussetzungen="Intervalllänge aus der Näherungsformel|Wurzel im Nenner",
    format="Rechnung|Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="mittel",
    gegeben=BIL + "; zweite Stichprobe vom Umfang 2n, ebenfalls 15 % fehlerhaft; gleiche Sicherheitswahrscheinlichkeit",
    gesucht="Begründung, dass das Konfidenzintervall kürzer, aber nicht halb so lang ist",
    verfahren="Länge 2k√(h(1 − h)/n) mit 2n vergleichen: Faktor 1/√2",
    schritte="2", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="",
    ergebnis="2k · √(0,15 · 0,85/(2n)) = 1/√2 · 2k · √(0,15 · 0,85/n); es gilt 1/√2 < 1 und 1/√2 ≠ 1/2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Länge als proportional zu 1/n annehmen",
    bemerkung="Standardbezug: K1 III, K2 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis mit n als Parameter, Faktor 1/√2 hergeleitet.")

NEUE_TYPEN = [
    ("Ganzrationale Funktion dritten Grades aus drei Nullstellen und einem Punkt rekonstruieren", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Aus drei am Graphen abgelesenen Nullstellen den Produktansatz a · (x − x1)(x − x2)(x − x3) aufstellen und den Streckfaktor aus einem weiteren Punkt bestimmen.",
     "2018MerhoehtBAnalysisWTR1-1a"),
    ("Ganzzahlige Nullstellen einer Integralfunktion über gleiche Grenzen und Symmetrie begründen", "Analysis", "Stammfunktion und Hauptsatz",
     "Die Nullstellen einer Integralfunktion angeben und begründen: die untere Grenze (Integral mit gleichen Grenzen) und die Stelle, an der sich wegen der Punktsymmetrie des Integranden die Flächenstücke ober- und unterhalb der Achse aufheben.",
     "2018MerhoehtBAnalysisWTR1-1d"),
    ("Weitere Nullstelle einer Integralfunktion über die Flächenbilanz am Graphen begründen", "Analysis", "Stammfunktion und Hauptsatz",
     "Mithilfe des Graphen des Integranden begründen, dass die Integralfunktion eine weitere Nullstelle hat, weil die Flächenbilanz bei wachsender oberer Grenze wieder null wird.",
     "2018MerhoehtBAnalysisWTR1-1e"),
    ("Höchstzahl der Nullstellen einer Integralfunktion über den Grad begründen", "Analysis", "Stammfunktion und Hauptsatz",
     "Aus dem Grad des Integranden den Grad der Integralfunktion ableiten und daraus die Höchstzahl ihrer Nullstellen begründen.",
     "2018MerhoehtBAnalysisWTR1-1f"),
    ("Sinusfunktion mit gleichen Nullstellen und gleichem Flächeninhalt wie ein Graph bestimmen", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Eine Funktion a · sin(bx) so bestimmen, dass sie auf einem Intervall dieselben Nullstellen wie ein gegebener Graph hat (b aus der halben Periode) und dieselbe Fläche mit der x-Achse einschließt (a aus dem Integral).",
     "2018MerhoehtBAnalysisWTR1-1g"),
    ("Gemeinsamen Punkt zweier Graphen über gleiche Flächeninhalte indirekt begründen", "Analysis", "Kurvenuntersuchung",
     "Indirekt begründen, dass zwei Graphen mit gleichen Randnullstellen und gleichem Flächeninhalt über einem Intervall dort einen gemeinsamen Punkt haben: läge einer ganz oberhalb, wären die Flächeninhalte verschieden.",
     "2018MerhoehtBAnalysisWTR1-1h"),
    ("Strenge Monotonie einer Schar über die Diskriminante der Ableitung für einen Parameterbereich nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Für eine Funktionenschar zeigen, dass die Ableitung für einen Parameterbereich keine Nullstelle hat (Diskriminante negativ) und wegen eines positiven Werts überall positiv ist, die Schar also streng monoton wächst.",
     "2018MerhoehtBAnalysisWTR1-2f"),
    ("Nullstellen und Werte: Länge der Verbindungsstrecke zweier Graphenpunkte als Näherung der Bogenlänge berechnen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Zwei Punkte eines Graphen über ihre Funktionswerte bestimmen und den Abstand als Näherung für die Länge des Graphenbogens berechnen.",
     "2018MerhoehtBAnalysisWTR2-1a"),
    ("Exponentialgleichung für einen Funktionswert durch Logarithmieren lösen und als Abstand im Sachzusammenhang angeben", "Analysis", "Gleichungen lösen",
     "Die Stelle zu einem vorgegebenen Funktionswert einer Exponentialfunktion durch Logarithmieren berechnen und daraus einen Abstand zu einem Bezugspunkt im Sachzusammenhang angeben.",
     "2018MerhoehtBAnalysisWTR2-1b"),
    ("Nullstellen und Werte: Aussage zur Modellgüte über die Summe vorzeichenbehafteter Abweichungen beurteilen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Beurteilen, ob ein kleiner Betrag der Summe der Abweichungen zwischen Messwerten und Modellwerten eine gute Modellbeschreibung belegt; Gegenargument: Abweichungen mit verschiedenen Vorzeichen heben sich auf.",
     "2018MerhoehtBAnalysisWTR2-1c"),
    ("Parameter einer Parabelschar aus dem knickfreien Übergang zu einem Graphen bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Koeffizienten einer Parabelschar aus der Bedingung bestimmen, dass der Übergang zu einem anderen Graphen an der Nahtstelle knickfrei ist (gleiche Ableitung).",
     "2018MerhoehtBAnalysisWTR2-1d"),
    ("Auftreffwinkel einer Flugkurve über die Ableitung an der Nullstelle berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Winkel, unter dem eine als Graph modellierte Flugkurve auf den Boden trifft, aus der Ableitung an der Auftreffstelle über den Tangens berechnen.",
     "2018MerhoehtBAnalysisWTR2-1f"),
    ("Hochpunkt einer Parabelschar mit Parameterkoordinaten nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Für eine Parabelschar nachweisen, dass ein in Abhängigkeit vom Parameter angegebener Punkt Hochpunkt ist: Ableitung dort null, Funktionswert bestätigen, Öffnung nach unten.",
     "2018MerhoehtBAnalysisWTR2-1g"),
    ("Steigung der Ortsgeraden der Hochpunkte einer Schar aus zwei Hochpunkten berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Steigung der Geraden, auf der alle Hochpunkte einer Schar liegen, aus zwei konkreten Hochpunkten (oder durch Eliminieren des Parameters) berechnen.",
     "2018MerhoehtBAnalysisWTR2-1h"),
    ("Gleichung zwischen Scharparameter und Nullstelle aus der Nullstellenbedingung herleiten", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus p_a(s) = 0 eine vorgegebene Gleichung herleiten, die den Scharparameter a durch die Nullstelle s ausdrückt.",
     "2018MerhoehtBAnalysisWTR2-1i"),
    ("Scharparameter aus der Weite berechnen und Höhe des Hochpunkts angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus einer vorgegebenen Nullstelle (Weite) über die Beziehung zwischen Parameter und Nullstelle den Parameter bestimmen und daraus die Höhe des Hochpunkts angeben.",
     "2018MerhoehtBAnalysisWTR2-1j"),
    ("Nullstellen und Werte: Aussage über das Verhältnis zweier Funktionswerte durch Einsetzen widerlegen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Eine Aussage über das Verhältnis der Funktionswerte an zwei Stellen mit festem Abstand durch Berechnen oder Ablesen eines Gegenbeispiels widerlegen.",
     "2018MerhoehtBAnalysisWTR2-1k"),
    ("Fläche: Flächeninhalt zwischen Graph, Achse und zwei Parallelen über Rechtecke und Integral berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Zwei Parallelen zur Abszissenachse durch Graphenpunkte einzeichnen und den Inhalt des von Graph, Ordinatenachse und den Parallelen berandeten Flächenstücks als Summe und Differenz von Rechtecken und einem Integral berechnen.",
     "2018MerhoehtBAnalysisWTR2-1l"),
    ("Wasservolumen als Differenz aus Rotationsvolumen und Kugelvolumen nach unten abschätzen", "Analysis", "Rotationsvolumen",
     "Aus der Sachlage (Kugel vollständig unter Wasser) eine Untergrenze des Wasserstands gewinnen, das Rotationsvolumen bis dorthin berechnen und das Kugelvolumen abziehen.",
     "2018MerhoehtBAnalysisWTR2-2a"),
    ("Gleichung für die Füllhöhe aus einem Rotationsvolumen zwischen variablen Grenzen aufstellen", "Analysis", "Rotationsvolumen",
     "Den Volumenzuwachs einer Schicht als Rotationsintegral mit variablen Grenzen t und t + 1 ansetzen und mit dem eingefüllten Volumen gleichsetzen, ohne die Gleichung zu lösen.",
     "2018MerhoehtBAnalysisWTR2-2b"),
    ("Ebene Figur: Viereck in ein Schrägbild einzeichnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Die Eckpunkte eines Vierecks aus ihren Koordinaten in ein vorgegebenes Schrägbild eintragen und verbinden.",
     "2018MerhoehtBAGLAA1WTR-1a"),
    ("Endpunkt der Schnittstrecke eines Vierecks mit einer achsenparallelen Ebene bestimmen", "Analytische Geometrie", "Schnittmengen",
     "Für eine zu einer Koordinatenebene parallele Ebene den Punkt bestimmen, in dem sie eine Seite eines Vierecks schneidet, über den Parameter der Seite.",
     "2018MerhoehtBAGLAA1WTR-1b"),
    ("Lotfußpunkt auf einer Geraden über das Skalarprodukt mit dem Richtungsvektor berechnen", "Analytische Geometrie", "Abstände",
     "Den Punkt einer Geraden berechnen, dessen Verbindung zu einem gegebenen Punkt senkrecht zur Geraden steht: Punkt mit Parameter ansetzen, Skalarprodukt mit dem Richtungsvektor null setzen.",
     "2018MerhoehtBAGLAA1WTR-1c"),
    ("Matrizenalgebra: Einträge einer Faktormatrix aus dem Produkt mit einer bekannten Matrix bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Die unbekannten Einträge einer Matrix F aus der Gleichung H · F = J mit bekannten Matrizen H und J durch Ausmultiplizieren und Vergleich bestimmen.",
     "2018MerhoehtBAGLAA1WTR-2a"),
    ("Übergangsprozess: Zustände nach einem und zwei Schritten aus einem Anfangszustand berechnen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus einem Anfangszustand durch ein- und zweimaliges Anwenden der Übergangsmatrix die Zustände der beiden folgenden Schritte berechnen.",
     "2018MerhoehtBAGLAA1WTR-2b"),
    ("Übergangsprozess: Unmöglichkeit eines konstanten Zustands über eine negative Lösung begründen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Untersuchen, ob eine Komponente des Zustands nach einem Übergang unverändert bleiben kann, indem die zugehörige Gleichung gelöst und die Lösung im Sachzusammenhang (negative Anzahl) verworfen wird.",
     "2018MerhoehtBAGLAA1WTR-2c"),
    ("Übergangsprozess: Anteil zu entfernender Individuen für einen stationären Zustand berechnen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Den Anteil bestimmen, um den eine Komponente vor dem Übergang verringert werden muss, damit der Zustand nach dem Übergang dem vor dem Eingriff gleicht: Gleichungssystem J · (S; P') = (S; P) aufstellen und P'/P berechnen.",
     "2018MerhoehtBAGLAA1WTR-2d"),
    ("Aufgabenstellung zum Abstand eines Punktes von einer Scharebene aus dem Lösungsweg formulieren", "Analytische Geometrie", "Abstände",
     "Einen vorgelegten Lösungsweg (Hessesche Normalform mit eingesetzten Koordinaten, gleich einem Abstand) als Abstandsbedingung erkennen und eine passende Aufgabenstellung formulieren.",
     "2018MerhoehtBAGLAA2WTR1-1g"),
    ("Ebene Figur: Flächeninhalt eines ebenen Vierecks mit zwei parallelen senkrechten Seiten aus Seitenlänge und Pfahlabstand berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Flächeninhalt eines ebenen Vierecks berechnen, dessen zwei gegenüberliegende Seiten senkrecht stehen und gleich lang sind (Parallelogramm): Seitenlänge mal Abstand der Trägergeraden.",
     "2018MerhoehtBAGLAA2WTR2-1e"),
    ("Höhe des Endpunkts einer Strecke auf einer senkrechten Geraden über den Schnitt mit einer Kante berechnen", "Analytische Geometrie", "Schnittmengen",
     "Die unbekannte Höhe eines Punktes auf einer senkrechten Geraden berechnen, wenn die Strecke von einem bekannten Punkt zu ihm eine gegebene Kante berührt: Gerade mit der Höhe als Variable ansetzen, Schnitt mit der Kantengeraden, dritte Gleichung auflösen.",
     "2018MerhoehtBAGLAA2WTR2-1f"),
    ("Ebene Figur: Zuschauerzahl aus dem Flächeninhalt eines Trapezes im Raum und dem Platzbedarf berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Flächeninhalt eines Trapezes im Raum über die Trapezformel mit der Höhe als Abstand der Mittelpunkte der parallelen Seiten berechnen und durch den Platzbedarf je Person teilen.",
     "2018MerhoehtBAGLAA2WTR3-1b"),
    ("Lotfußpunkt außerhalb einer Figur als Grund für größere Abstände aller Figurpunkte zeichnerisch begründen", "Analytische Geometrie", "Abstände",
     "Anhand einer Zeichnung begründen, dass kein Punkt einer ebenen Figur von einem Punkt den Abstand hat, den dieser zur Trägerebene hat, weil der Lotfußpunkt außerhalb der Figur liegt.",
     "2018MerhoehtBAGLAA2WTR3-1d"),
    ("Gerade und Ebene: Berühren einer Geraden mit einem Netz über die Höhe des Durchstoßpunkts in der Netzebene untersuchen", "Analytische Geometrie", "Lagebeziehungen",
     "Rechnerisch untersuchen, ob eine geradlinige Bahn ein Netz berührt: Parameter für das Erreichen der Netzebene bestimmen und die Höhe des Punktes dort mit der Netzhöhe vergleichen.",
     "2018MerhoehtBAGLAA2WTR3-1e"),
    ("Punkt und Ebene: Auftreffpunkt einer Bahnkurve auf der Grundebene berechnen und Lage innerhalb des Spielfelds prüfen", "Analytische Geometrie", "Lagebeziehungen",
     "Für eine durch Punkte X_t beschriebene Bahn den Zeitpunkt mit x3 = 0 aus einer quadratischen Gleichung bestimmen und prüfen, ob der Auftreffpunkt innerhalb vorgegebener Koordinatenschranken liegt.",
     "2018MerhoehtBAGLAA2WTR3-1g"),
    ("Mindestanzahl von Versuchen für mindestens drei Treffer mit vorgegebener Wahrscheinlichkeit durch Probieren ermitteln", "Stochastik", "Binomialverteilung",
     "Die kleinste Anzahl n bestimmen, für die P(Y ≥ 3) bei Y ~ B(n; p) eine Schranke erreicht, durch Prüfen der ersten in Frage kommenden Werte von n.",
     "2018MerhoehtBStochastikWTR1-1b"),
    ("Laplace-Experiment: Wahrscheinlichkeit für drei verschiedene Ergebnisse über Pfadprodukt und Reihenfolgen nachweisen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Die Wahrscheinlichkeit, bei drei Durchgängen drei verschiedene Ergebnisse zu erhalten, als Produkt der Einzelwahrscheinlichkeiten mal Anzahl der Reihenfolgen (3!) nachweisen.",
     "2018MerhoehtBStochastikWTR1-2a"),
    ("Mindestwert einer Erkennungswahrscheinlichkeit aus einer Bedingung an eine bedingte Wahrscheinlichkeit bestimmen", "Stochastik", "Bedingte Wahrscheinlichkeit und Bayes",
     "Eine bedingte Wahrscheinlichkeit (Bayes) mit der Erkennungswahrscheinlichkeit x als Parameter aufstellen und aus einer Schranke an diese Wahrscheinlichkeit den kleinsten zulässigen Wert von x berechnen.",
     "2018MerhoehtBStochastikWTR2-1e"),
    ("Länge eines Konfidenzintervalls bei doppeltem Stichprobenumfang über den Faktor 1/√2 begründen", "Stochastik", "Konfidenzintervalle",
     "Aus der Näherungsformel für die Intervallgrenzen begründen, dass die Länge des Konfidenzintervalls bei doppeltem Stichprobenumfang und gleichem Stichprobenanteil um den Faktor 1/√2 kleiner, also kürzer, aber nicht halb so lang wird.",
     "2018MerhoehtBStochastikWTR2-1g"),
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
MARKE_ABGEWANDELT = re.compile(r"Abgewandelt von: (" + KENNUNG.pattern + r"(?:-\d*[a-z]?)?)")
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
    # Landesverwendung (v1.2, v1.3): abi-Zeilen, die auf eine Poolzeile verweisen – als
    # „Dublette von: <id>" (wortgleich), „Abgewandelt von: <id>" (abgewandelt, v1.3)
    # oder „Poolaufgabe (nicht erfasst): <id>" (vorgemerkt, Übergangszustand)
    verweis, abgewandelt, vorgemerkt = {}, {}, {}
    for z in andere:
        m = MARKE_DUBLETTE.search(z["bemerkung"])
        if m:
            verweis.setdefault(m.group(1), []).append(z["id"])
        m = MARKE_ABGEWANDELT.search(z["bemerkung"])
        if m:
            abgewandelt.setdefault(m.group(1), []).append(z["id"])
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
        for pid in list(verweis) + list(abgewandelt):
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
        je_stapel, abgew_stapel, vorgemerkt_stapel = {}, {}, {}
        for pid in verweis:
            k = kennung_aus_id(pid)[0]
            if k in QUELLE:
                je_stapel[einheit(QUELLE[k])] = je_stapel.get(einheit(QUELLE[k]), 0) + 1
        for pid in abgewandelt:
            k = kennung_aus_id(pid)[0]
            if k in QUELLE:
                abgew_stapel[einheit(QUELLE[k])] = abgew_stapel.get(einheit(QUELLE[k]), 0) + 1
        offen = []
        for pid in vorgemerkt:
            if pid in ids:  # Übergangszustand: offener Posten, kein Fehler (abi.md § 7)
                offen.append(f"{pid} ist erfasst, in {', '.join(vorgemerkt[pid])} noch vorgemerkt – abgleich.py")
            k = kennung_aus_id(pid)[0]
            s = einheit(QUELLE[k]) if k in QUELLE else "unbekannt"
            vorgemerkt_stapel[s] = vorgemerkt_stapel.get(s, 0) + 1
        print("In Landesheften (Dublette von): " + (", ".join(f"{s} {n}" for s, n in sorted(je_stapel.items())) or "keine")
              + f" – {sum(je_stapel.values())} Zeilen; abgewandelt (Abgewandelt von): "
              + (", ".join(f"{s} {n}" for s, n in sorted(abgew_stapel.items())) or "keine")
              + "; vorgemerkt (Poolaufgabe (nicht erfasst), offener Posten): "
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
    land = [i for i in neue_ids if i in verweis or i in abgewandelt or i in vorgemerkt]
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
