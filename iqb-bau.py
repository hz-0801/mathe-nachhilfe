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
    "stapel": "2018-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2018MgrundlegendBAnalysisWTR": 40, "2018MgrundlegendBAGLAA1WTR": 20,
        "2018MgrundlegendBAGLAA2WTR1": 20, "2018MgrundlegendBAGLAA2WTR2": 20,
        "2018MgrundlegendBStochastikWTR1": 20, "2018MgrundlegendBStochastikWTR2": 20,
        "2018MgrundlegendBStochastikWTR3": 20,
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
# Stapel 2018-ga-B (WTR-Zweig; Reserve, geöffnet 16.09.2026 wegen der
# Landesheftverweise: 2018-be-gk 2.2 = AG/LA (A2) WTR 2, 3.2 a–d = Stochastik
# WTR 2 a–d). Sieben Dateien, Standardbezug mit Spalte Anforderungsbereich.
# ---- Analysis WTR (Aufgabe 1: Graph mit Wendepunkt, 24 BE; Aufgabe 2: Kosten, 16 BE)
ANA = "f(x) = 1/8 · (x³ − 15x² + 50x), x ∈ IR; Abbildung 1 zeigt den Graphen G_f"
ANA_SK = ("Koordinatensystem auf Gitter, x von −1 bis 11, y von −6 bis 6, ganze Zahlen beschriftet. Graph G_f: "
          "vom Ursprung steigend zum Hochpunkt bei etwa (2,1 | 6), fallend durch den Wendepunkt W(5 | 0) zum "
          "Tiefpunkt bei etwa (7,9 | −6), dann steigend durch (10 | 0) und oben aus dem Bild; Beschriftung G_f.")
row("2018MgrundlegendBAnalysisWTR", "a", innen="1", seite="1", punkte="6", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendepunkt an vorgegebener Stelle nachweisen und Wendetangente aufstellen", typ_neben="",
    stichwoerter="f'(x) = 1/8 (3x² − 30x + 50), f''(x) = 1/8 (6x − 30), f''' = 3/4|f''(5) = 0, f'''(5) ≠ 0|f'(5) = −25/8|Tangente y = −25/8 x + 125/8",
    voraussetzungen="Ableitungen ganzrationaler Funktionen|Wendepunktbedingung f'' = 0 und f''' ≠ 0|Tangentengleichung",
    format="Rechnung", operator="Zeigen Sie|Ermitteln Sie", antwort="Term",
    material="Koordinatensystem", skizze=ANA_SK, kontext="ohne", textumfang="kurz",
    gegeben=ANA + "; Punkt W(5 | 0)",
    gesucht="Nachweis, dass W ein Wendepunkt ist; Gleichung der Tangente in W",
    verfahren="f'' und f''' bilden, f''(5) = 0 und f'''(5) = 3/4 ≠ 0; f(5) = 0, f'(5) = −25/8, Tangente aufstellen",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f''(5) = 0, f'''(5) = 3/4 ≠ 0, f(5) = 0; Tangente y = −25/8 x + 125/8 (amtlich)",
    zwischenergebnis="f'(x) = 1/8 (3x² − 30x + 50)|f''(x) = 1/8 (6x − 30)", niveau_geschaetzt="II",
    fehlerquelle="f''(5) = 0 ohne hinreichende Bedingung als Nachweis werten",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Geschätzt II (Verkettung Ableitungen, Bedingung, Tangente), amtlich I.")
row("2018MgrundlegendBAnalysisWTR", "b", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Punktsymmetrie zum Wendepunkt über die Verschiebung einer ungeraden Funktion begründen", typ_neben="",
    stichwoerter="g(x) = 1/8 (x³ − 25x)|Verschiebung um 5 in positive x-Richtung|g hat nur ungerade Potenzen, punktsymmetrisch zum Ursprung|G_f symmetrisch zu W(5 | 0)",
    voraussetzungen="Verschiebung eines Graphen in x-Richtung|Ungerade Potenzen bedeuten Punktsymmetrie zum Ursprung",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=ANA + "; G_f geht aus dem Graphen von g(x) = 1/8 (x³ − 25x) durch Verschiebung in positive x-Richtung hervor",
    gesucht="Betrag der Verschiebung; Begründung mit g, dass G_f symmetrisch zum Wendepunkt ist",
    verfahren="f(x) = g(x − 5) nachrechnen oder an W erkennen: Verschiebung 5; g ist punktsymmetrisch zum Ursprung, weil nur ungerade Potenzen vorkommen, also G_f zu W(5 | 0)",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2018MgrundlegendBAnalysisWTR-1a",
    ergebnis="Verschiebung um 5; g enthält nur ungerade Potenzen, ist also punktsymmetrisch zum Ursprung, G_f damit symmetrisch bezüglich W(5 | 0) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Symmetrie von f direkt an f(x) prüfen statt über g",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (g(x − 5) = f(x)).")
row("2018MgrundlegendBAnalysisWTR", "c", innen="1", seite="2", punkte="4", afb_amtlich="I|II|III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Oberflächeninhalt des Rotationskegels eines rechtwinkligen Dreiecks berechnen", typ_neben="",
    stichwoerter="A(0 | 0), B(4 | 0), C(4 | f(4)) mit f(4) = 3|Rotation um AB ergibt einen Kegel mit Radius 3, Höhe 4|Mantellinie 5|O = π · 3² + π · 3 · 5 = 24π ≈ 75,4",
    voraussetzungen="Rotationskörper eines rechtwinkligen Dreiecks als Kegel erkennen|Pythagoras für die Mantellinie|Kegeloberfläche πr² + πrs",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=ANA + "; Dreieck ABC mit A(0 | 0), B(4 | 0), C(4 | f(4)) rotiert um die Seite AB",
    gesucht="Inhalt der Oberfläche des entstehenden Körpers",
    verfahren="f(4) = 3 als Radius, 4 als Höhe, Mantellinie √(9 + 16) = 5; Grundkreis plus Mantel",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="f(4)² · π + f(4) · π · √(f(4)² + 4²) = 24π (amtlich); ≈ 75,4",
    zwischenergebnis="f(4) = 3, s = 5", niveau_geschaetzt="III",
    fehlerquelle="nur den Mantel oder nur die Grundfläche rechnen; Rotation um die y-Achse annehmen",
    bemerkung="Standardbezug: K2 III, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) den Rotationskörper als Kegel mit Radius f(4) erkennen und die Oberflächenformel darauf übersetzen. Thema Flächeninhalt und Volumen im Raum (Klasse Körper), nicht Rotationsvolumen: kein Integral, Elementargeometrie; leitidee folgt dem Typ, die Aufgabe steht in der Analysis-Datei.")
row("2018MgrundlegendBAnalysisWTR", "d", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Bestimmtes Integral einer ganzrationalen Funktion berechnen", typ_neben="",
    stichwoerter="∫ von 0 bis 5 f(x) dx|Stammfunktion 1/8 (x⁴/4 − 5x³ + 25x²)|625/32 ≈ 19,53",
    voraussetzungen="Stammfunktion ganzrationaler Terme|Hauptsatz",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=ANA,
    gesucht="Wert des Integrals von 0 bis 5 über f",
    verfahren="Stammfunktion bilden und Grenzen einsetzen",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="∫ von 0 bis 5 f(x) dx = [x⁴/32 − 5x³/8 + 25x²/8] von 0 bis 5 = 625/32 (amtlich); ≈ 19,53",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Faktor 1/8 beim Integrieren vergessen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-A).")
row("2018MgrundlegendBAnalysisWTR", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Ungleichung zweier Integrale über das Vorzeichen des Teilintegrals am Graphen begründen", typ_neben="",
    stichwoerter="∫ von 0 bis 8 = ∫ von 0 bis 5 + ∫ von 5 bis 8|Graph zwischen 5 und 8 unterhalb der x-Achse|Teilintegral negativ",
    voraussetzungen="Intervalladditivität|Vorzeichen eines Integrals am Graphen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ANA_SK, kontext="ohne", textumfang="kurz",
    gegeben=ANA + " (Graph unterhalb der x-Achse zwischen 5 und 10)",
    gesucht="Begründung ohne Rechnung, dass ∫ von 0 bis 8 f(x) dx < ∫ von 0 bis 5 f(x) dx",
    verfahren="Integral über [0; 8] in [0; 5] und [5; 8] zerlegen; das zweite ist negativ, weil das Flächenstück unter der x-Achse liegt",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="∫ von 0 bis 8 = ∫ von 0 bis 5 + ∫ von 5 bis 8, und ∫ von 5 bis 8 f(x) dx < 0, weil das Flächenstück zwischen x = 5 und x = 8 unterhalb der x-Achse liegt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit Flächeninhalten statt mit orientierten Integralen argumentieren",
    bemerkung="Standardbezug: K1 II, K5 II. AB amtlich: II. Amtlich.")
row("2018MgrundlegendBAnalysisWTR", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Lage zweier Graphen aus dem Graphen ihrer Differenzfunktion beschreiben", typ_neben="",
    stichwoerter="Abbildung 2 zeigt h(x) − f(x)|Nullstellen 0, x_S ≈ 2,2 und 5 sind gemeinsame Punkte|zwischen 0 und x_S ist f oberhalb von h, zwischen x_S und 5 unterhalb|Tiefpunkt: größter Abstand der Graphen",
    voraussetzungen="Nullstellen der Differenz als Schnittstellen|Vorzeichen der Differenz als Lage|Extremum der Differenz als maximaler Abstand",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem",
    skizze="Kleines Koordinatensystem auf Gitter, x von 0 bis 6, y von −1 bis 2. Graph von h − f: beginnt im Ursprung, fällt bis zu einem Tiefpunkt bei etwa (1 | −0,7), steigt durch die Nullstelle bei etwa 2,2 bis etwa (3,6 | 0,4) und fällt durch die Nullstelle 5 unter die x-Achse.",
    kontext="ohne", textumfang="mittel",
    gegeben=ANA + "; eine in IR definierte Funktion h; Abbildung 2 zeigt h(x) − f(x) mit Nullstellen bei 0, etwa 2,2 und 5 und Tiefpunkt bei etwa x = 1",
    gesucht="Beschreibung der gegenseitigen Lage der Graphen von f und h für x ∈ [0; 5] mit Bedeutung der Nullstellen und der Tiefpunktstelle",
    verfahren="Nullstellen der Differenz = gemeinsame Punkte; negative Differenz = f oberhalb h; Tiefpunkt = größter Abstand der Punkte gleicher x-Koordinate",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Bei x = 0, x_S ≈ 2,2 und x = 5 haben f und h gemeinsame Punkte; für 0 < x < x_S liegt G_f oberhalb, für x_S < x < 5 unterhalb des Graphen von h; an der Tiefpunktstelle haben die Punkte gleicher x-Koordinate den größten Abstand (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das Vorzeichen von h − f als Lage von h unter f statt über f lesen",
    bemerkung="Standardbezug: K1 II, K4 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (e) sinngemäß – den Graphen einer Differenzfunktion in die Lage zweier Graphen übersetzen, mit Extremum als maximalem Abstand.")
KOS = ("Kostenfunktion K(x) = x³ − 12x² + 50x + 20, 0 ≤ x ≤ 9, K(x) in 1000 Euro für die Produktion von x Kubikmetern "
       "einer Flüssigkeit; Abbildung 3 zeigt den Graphen von K")
KOS_SK = ("Koordinatensystem auf Gitter, x von −1 bis 9, y von 0 bis 220 in Zwanzigerschritten. Graph von K: bei "
          "(0 | 20) beginnend, ansteigend mit abnehmender Steigung bis zu einem flachen Bereich um (4 | 90), danach "
          "zunehmend steil bis etwa (9 | 230).")
row("2018MgrundlegendBAnalysisWTR", "a", innen="2", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Stelle zu einem vorgegebenen Funktionswert am Graphen ablesen", typ_neben="",
    stichwoerter="Kosten 125 000 Euro heißt K(x) = 125|am Graphen etwa x = 7",
    voraussetzungen="Einheit 1000 Euro umrechnen|Ablesen am Graphen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=KOS_SK, kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS,
    gesucht="Produktionsmenge, bei der die Kosten 125 000 Euro betragen, mithilfe der Abbildung",
    verfahren="y = 125 am Graphen suchen",
    schritte="1", zahlenraum="ganz", einheiten="m³", abhaengig_von="",
    ergebnis="etwa 7 m³ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="125 000 als 125 000 Einheiten der y-Achse suchen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (K(7) = 125).")
row("2018MgrundlegendBAnalysisWTR", "b", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Verlauf eines Graphen im Sachzusammenhang beschreiben", typ_neben="",
    stichwoerter="K streng monoton wachsend|mehr Produktion, höhere Kosten",
    voraussetzungen="Monotonie am Graphen erkennen und deuten",
    format="Kurzantwort", operator="Geben Sie an|Deuten Sie", antwort="Text",
    material="Koordinatensystem", skizze=KOS_SK, kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS,
    gesucht="Monotonieverhalten von K mit Deutung im Sachzusammenhang",
    verfahren="Am Graphen ablesen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="K ist streng monoton wachsend: mit zunehmender Produktionsmenge nehmen die Kosten zu (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den flachen Bereich um x = 4 als Abnahme deuten",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2025-ga-B), hier nur die Monotonie.")
row("2018MgrundlegendBAnalysisWTR", "c", innen="2", seite="2", punkte="2", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Aussage über die Zunahme der Zusatzkosten über Differenzen von Funktionswerten beurteilen", typ_neben="",
    stichwoerter="Zusatzkosten eines weiteren Kubikmeters = K(x + 1) − K(x)|K(3) − K(2) = 9 < K(2) − K(1) = 21|Aussage falsch (Graph wird zunächst flacher)",
    voraussetzungen="Zusatzkosten als Differenz oder Steigung|Gegenbeispiel aus Funktionswerten",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=KOS_SK, kontext="Produktion/Kosten", textumfang="mittel",
    gegeben=KOS + "; Aussage: Je größer die Produktionsmenge, desto höher die Kosten eines zusätzlichen Kubikmeters",
    gesucht="Beurteilung der Aussage",
    verfahren="Ein Gegenbeispiel mit zwei Differenzen: K(3) − K(2) < K(2) − K(1), also nehmen die Zusatzkosten zunächst ab",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist falsch: K(3) − K(2) = 9 < K(2) − K(1) = 21 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die Aussage mit der Monotonie von K (steigend) bestätigen statt die Steigungsänderung zu prüfen",
    bemerkung="Standardbezug: K1 II, K4 III, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „Kosten eines zusätzlichen Kubikmeters“ in Differenzen K(x + 1) − K(x) übersetzen und mit einem Gegenbeispiel widerlegen.")
row("2018MgrundlegendBAnalysisWTR", "d", innen="2", seite="3", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Gleichheit zweier Funktionswerte durch Einsetzen im Sachzusammenhang nachweisen", typ_neben="",
    stichwoerter="E(x) = 23x|G(x) = E(x) − K(x)|E(4) − K(4) = 92 − 92 = 0",
    voraussetzungen="Funktionswerte berechnen|Gewinn als Erlös minus Kosten",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS + "; Erlösfunktion E(x) = 23x, Gewinnfunktion G = E − K (positive Werte Gewinn, negative Verlust)",
    gesucht="Nachweis, dass bei vier verkauften Kubikmetern kein Gewinn entsteht",
    verfahren="E(4) und K(4) berechnen und vergleichen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="E(4) − K(4) = 92 − 92 = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Rechenfehler bei K(4) = 64 − 192 + 200 + 20",
    bemerkung="Standardbezug: K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2018MgrundlegendBAnalysisWTR", "e", innen="2", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Gewinnbereich als Bereich zwischen den Schnittstellen von Erlösgerade und Kostengraph zeichnerisch bestimmen", typ_neben="",
    stichwoerter="Gerade E(x) = 23x in Abbildung 3|Schnittstellen bei 4 und x_S ≈ 8,6|Gewinn für 4 < x < x_S",
    voraussetzungen="Gerade durch den Ursprung zeichnen|Gewinn als Bereich, in dem die Erlösgerade über dem Kostengraphen liegt",
    format="Zeichnen|Kurzantwort", operator="Zeichnen Sie ein|Bestimmen Sie", antwort="Grafik|Zahl",
    material="Koordinatensystem", skizze=KOS_SK, kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS + "; E(x) = 23x, G = E − K",
    gesucht="Graph von E in Abbildung 3; Bereich der verkauften Menge mit Gewinn, aus der Darstellung",
    verfahren="Gerade durch (0 | 0) und (9 | 207) einzeichnen; zwischen den Schnittpunkten liegt E über K",
    schritte="2", zahlenraum="dezimal", einheiten="m³", abhaengig_von="2018MgrundlegendBAnalysisWTR-2d",
    ergebnis="Gewinn nur für 4 < x < x_S mit x_S ≈ 8,6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Bereich links von 4 mitnehmen",
    bemerkung="Standardbezug: K4 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Nullstellen von G bei 4 und 8,58).")
row("2018MgrundlegendBAnalysisWTR", "f", innen="2", seite="3", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Maximum einer Gewinnfunktion über die Ableitung berechnen", typ_neben="",
    stichwoerter="G(x) = −x³ + 12x² − 27x − 20|G'(x) = −3x² + 24x − 27 = 0 ⇔ x = 4 ± √7|Maximum im Gewinnbereich bei x = 4 + √7 ≈ 6,6",
    voraussetzungen="Differenzfunktion aufstellen|Extremstellen über die Ableitung|Lösung im zulässigen Bereich auswählen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Kosten", textumfang="kurz",
    gegeben=KOS + "; E(x) = 23x, G = E − K, Gewinnbereich 4 < x < x_S ≈ 8,6",
    gesucht="verkaufte Menge mit dem größten Gewinn",
    verfahren="G aufstellen, G' = 0 lösen, die Lösung im Gewinnbereich nehmen",
    schritte="4", zahlenraum="Wurzel|dezimal|negativ", einheiten="m³", abhaengig_von="",
    ergebnis="G'(x) = 0 ⇔ x = 4 + √7 ≈ 6,6 (im Bereich 4 < x < x_S); etwa 6,6 Kubikmeter (amtlich)",
    zwischenergebnis="G'(x) = −3x² + 24x − 27|zweite Lösung 4 − √7 ≈ 1,35 außerhalb", niveau_geschaetzt="II",
    fehlerquelle="die Lösung 4 − √7 nicht ausschließen; Art des Extremums nicht prüfen",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (G(4 + √7) ≈ 37,0).")
# ---- AG/LA (A1) WTR: Baumärkte, 20 BE
BAU = ("Zwei Baumärkte A und B: 70 % bzw. 80 % der Kunden kaufen im nächsten Monat wieder beim selben Baumarkt, die "
       "übrigen wechseln")
BAU3 = ("Drei Baumärkte A, B, C; Kundenverteilung als Vektor (a; b; c), Übergang je Monat M · v_n = v_(n+1) mit "
        "M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25)); im Sommermonat A 3700, B 5100, C 1200 Kunden")
row("2018MgrundlegendBAGLAA1WTR", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="zwei Zustände A, B|Schleifen 0,7 und 0,8|Pfeile A→B 0,3, B→A 0,2",
    voraussetzungen="Anteile aus dem Text ablesen|Gegenanteil als Wechsler",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Baumärkte/Kunden", textumfang="kurz",
    gegeben=BAU,
    gesucht="Übergangsdiagramm für das Wechseln der Kunden von einem Monat zum nächsten",
    verfahren="Zwei Knoten mit Schleifen 0,7 und 0,8, Pfeile mit 0,3 und 0,2",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Diagramm mit A (Schleife 0,7), B (Schleife 0,8), A→B 0,3, B→A 0,2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Wechselanteile 0,3 und 0,2 vertauschen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2018-ea-A), hier aus dem Text statt aus der Tabelle.")
row("2018MgrundlegendBAGLAA1WTR", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Wechselzahlen nach einem Übergang berechnen und Gleichgewicht deuten", typ_neben="",
    stichwoerter="A 4000, B 6000 Kunden|0,3 · 4000 = 1200 wechseln von A, 0,2 · 6000 = 1200 von B|Anzahlen bleiben gleich (stationär)",
    voraussetzungen="Anteil mal Anzahl|gleiche Wechselzahlen als Gleichgewicht deuten",
    format="Rechnung|Begründung", operator="Ermitteln Sie|Interpretieren Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Baumärkte/Kunden", textumfang="kurz",
    gegeben=BAU + "; in einem Monat hat A 4000 und B 6000 Kunden",
    gesucht="Anzahl der Wechsler je Baumarkt im Folgemonat mit Deutung",
    verfahren="0,3 · 4000 und 0,2 · 6000 berechnen und vergleichen",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Von A wechseln 1200, von B wechseln 1200 Kunden; die Kundenzahlen beider Baumärkte ändern sich nicht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Bleibenden statt der Wechsler berechnen",
    bemerkung="Standardbezug: K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Gleichungssystem für die Verteilung vor einem Übergang aufstellen", typ_neben="",
    stichwoerter="M · (a; b; c) = (3700; 5100; 1200)|0,63a + 0,18b + 0,3c = 3700 usw.",
    voraussetzungen="Matrix-Vektor-Produkt als Gleichungssystem schreiben|Vormonat als Unbekannte",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Baumärkte/Kunden", textumfang="mittel",
    gegeben=BAU3,
    gesucht="Gleichungssystem für die Kundenzahlen im Monat vor dem Sommermonat",
    verfahren="M · v = Sommerverteilung zeilenweise ausschreiben",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,63a + 0,18b + 0,3c = 3700; 0,27a + 0,72b + 0,45c = 5100; 0,1a + 0,1b + 0,25c = 1200 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="M auf die Sommerverteilung anwenden (Folgemonat statt Vormonat)",
    bemerkung="Standardbezug: K3 II, K4 I, K5 I. AB amtlich: II. Amtlich.")
row("2018MgrundlegendBAGLAA1WTR", "d", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Verteilung nach einem Übergang berechnen und einen Anteil angeben", typ_neben="",
    stichwoerter="B: 0,27 · 3700 + 0,72 · 5100 + 0,45 · 1200 = 5211|C: 10 000 − 3609 − 5211 = 1180|Anteil C etwa 12 %",
    voraussetzungen="Matrixzeile mal Vektor|Gesamtzahl bleibt 10 000",
    format="Rechnung", operator="Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Baumärkte/Kunden", textumfang="mittel",
    gegeben=BAU3 + "; im Folgemonat hat A 3609 Kunden",
    gesucht="Kundenzahlen von B und C im Folgemonat; prozentualer Anteil von C an allen Kunden",
    verfahren="Zweite Matrixzeile auswerten, C als Rest zu 10 000, Anteil bilden",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="B 5211, C 1180; Anteil von C etwa 12 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="C über die dritte Zeile mit Rundungsfehler statt als Rest berechnen (auch 1180)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2018MgrundlegendBAGLAA1WTR", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zustand mit dem kleinsten Wechselanteil aus der Matrix ablesen", typ_neben="",
    stichwoerter="Diagonale 0,63, 0,72, 0,25|größter Bleibeanteil bei B|Wechselanteil 1 − 0,72 = 28 %",
    voraussetzungen="Diagonaleinträge als Bleibeanteile|Wechselanteil als Komplement",
    format="Kurzantwort", operator="Geben Sie an|Nennen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Baumärkte/Kunden", textumfang="kurz",
    gegeben=BAU3,
    gesucht="Baumarkt mit dem kleinsten Anteil wechselnder Kunden und dieser Anteil",
    verfahren="Größten Diagonaleintrag suchen, Komplement bilden",
    schritte="1", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Baumarkt B, Anteil 28 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Spalten- und Zeilensummen verwechseln",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I. AB amtlich: I. Amtlich.")
row("2018MgrundlegendBAGLAA1WTR", "f", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Potenz der Übergangsmatrix als mehrschrittigen Übergang deuten", typ_neben="",
    stichwoerter="M · M · M|Wechselverhalten über drei Monate (Vierteljahr)",
    voraussetzungen="Matrixpotenz als Hintereinanderausführung",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Baumärkte/Kunden", textumfang="kurz",
    gegeben=BAU3,
    gesucht="Bedeutung des Terms M · M · M im Sachzusammenhang",
    verfahren="Dreifache Anwendung von M als Übergang über drei Monate deuten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Der Term beschreibt im Modell das vierteljährliche Wechselverhalten der Kunden (Übergang über drei Monate) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="M³ als dreifache Kundenzahl deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich.")
row("2018MgrundlegendBAGLAA1WTR", "g", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Bereich eines Anteils in Abhängigkeit vom Matrixparameter über die Randwerte ermitteln", typ_neben="",
    stichwoerter="N mit dritter Spalte (0,4(1 − p); 0,6(1 − p); p), p ∈ [0; 1]|A 3650,38 − 470,6p, B 5467,27 − 705,9p, Summe 10 000|C = 882,35 + 1176,5p|Anteil zwischen 8,8 % (p = 0) und 20,6 % (p = 1)",
    voraussetzungen="Rest zur Gesamtzahl als Term in p|Monotonie eines linearen Terms|Randwerte einsetzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Baumärkte/Kunden", textumfang="lang",
    gegeben="Nach Beginn von Rabattaktionen gilt die Matrix N = ((0,63; 0,18; 0,4 · (1 − p)), (0,27; 0,72; 0,6 · (1 − p)), (0,1; 0,1; p)), p ∈ [0; 1]; in einem Monat hat A 3650,38 − 470,6 · p und B 5467,27 − 705,9 · p Kunden, zusammen sind es 10 000",
    gesucht="Bereich, in dem der prozentuale Anteil der Kunden von C in diesem Monat liegen kann",
    verfahren="C = 10 000 − A − B = 882,35 + 1176,5p; linear in p, also Randwerte p = 0 und p = 1 einsetzen und durch 10 000 teilen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="C = 882,35 + 1176,5 · p, Anteil 0,088235 + 0,11765 · p; zwischen etwa 9 % und etwa 21 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="den Anteil nur für einen p-Wert berechnen; Monotonie nicht begründen",
    bemerkung="Standardbezug: K2 II, K3 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „Bereich des Anteils“ in einen linearen Term in p und dessen Randwerte übersetzen.")
row("2018MgrundlegendBAGLAA1WTR", "h", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixparameter aus einer Komponente nach einem Schritt bestimmen", typ_neben="",
    stichwoerter="dritte Zeile von N: 0,1 · 3556 + 0,1 · 5326 + p · 1118 = 1112|p ≈ 0,2",
    voraussetzungen="Matrixzeile mit Parameter auswerten|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Baumärkte/Kunden", textumfang="mittel",
    gegeben="Matrix N wie in g; in einem Monat A 3556, B 5326, C 1118 Kunden, im Folgemonat C 1112 Kunden",
    gesucht="zugehöriger Wert von p",
    verfahren="Dritte Zeile von N auf den Vektor anwenden und gleich 1112 setzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,1 · 3556 + 0,1 · 5326 + p · 1118 = 1112 liefert p ≈ 0,2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die erste Zeile statt der dritten verwenden",
    bemerkung="Standardbezug: K2 II, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
# ---- AG/LA (A2) WTR 1: Quader, 20 BE
QUA = ("Quader mit den Eckpunkten A(4 | 0 | 0), B(4 | 4 | 0), C(0 | 4 | 0) und F(4 | 4 | 3); die Gerade h verläuft "
       "durch B und F")
QUA_SK = ("Schrägbild auf Gitter: Quader mit Grundfläche OABC in der x1x2-Ebene (Kantenlänge 4) und Höhe 3, "
          "Beschriftungen A, B, C, F, Achsen x1, x2, x3; die Gerade h als senkrechte Gerade durch B und F über den "
          "Quader hinaus; gepunktet die Schnittfigur einer Ebene durch A, C und einen Punkt P von h oberhalb von F "
          "(Viereck mit Ecken auf den senkrechten Kanten über A und C).")
row("2018MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Rechtwinkliges gleichschenkliges Dreieck aus den Koordinaten begründen und Flächeninhalt angeben", typ_neben="",
    stichwoerter="OABC ist ein Quadrat mit Seite 4|Dreieck ABC halbes Quadrat, rechter Winkel bei B|Flächeninhalt 8",
    voraussetzungen="Quadrat aus den Koordinaten erkennen|halbes Quadrat als rechtwinklig-gleichschenkliges Dreieck",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text|Zahl",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="kurz",
    gegeben=QUA,
    gesucht="Begründung, dass ABC rechtwinklig und gleichschenklig ist; Flächeninhalt",
    verfahren="OABC ist ein Quadrat (Koordinaten), ABC eine Hälfte davon; Fläche 1/2 · 4 · 4",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="OABC ist ein Quadrat, also ist ABC rechtwinklig und gleichschenklig; Flächeninhalt 8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den rechten Winkel bei A oder C vermuten",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2018MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Geradengleichung durch zwei Punkte aufstellen und windschiefe Lage begründen", typ_neben="",
    stichwoerter="Gerade AC: x = (4; 0; 0) + u · (−1; 1; 0)|h senkrecht durch B|AC liegt in der x1x2-Ebene ohne B, h trifft diese Ebene nur in B|windschief",
    voraussetzungen="Parameterform aus zwei Punkten|windschief: kein Schnittpunkt, nicht parallel",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Term|Text",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="kurz",
    gegeben=QUA,
    gesucht="Gleichung der Geraden durch A und C; Begründung, dass sie windschief zu h ist",
    verfahren="Richtungsvektor AC; h schneidet die x1x2-Ebene nur in B, die Gerade AC liegt in dieser Ebene und geht nicht durch B, die Richtungen sind nicht parallel",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="x = (4; 0; 0) + u · (−1; 1; 0), u ∈ IR; h schneidet die x1x2-Ebene in B, die Gerade AC liegt in dieser Ebene und verläuft nicht durch B (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Windschiefheit nur über fehlende Parallelität begründen",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Geschätzt I nach dem Standardbezug (Lagebeurteilung ohne Rechnung).")
row("2018MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Koordinate eines Punktes aus der Schnittfigur zeichnerisch ermitteln und Vorgehen beschreiben", typ_neben="",
    stichwoerter="Ebene durch A, C und P auf h|Seite der Schnittfigur verlängern bis zur Geraden h|Schnittpunkt liefert x3 = 6",
    voraussetzungen="Schnittfigur im Schrägbild lesen|Verlängerung einer Schnittkante in der Ebene",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="mittel",
    gegeben=QUA + "; gepunktet die Schnittfigur des Quaders mit einer Ebene durch A, C und einen Punkt P von h",
    gesucht="Beschreibung, wie man mithilfe der Abbildung ermittelt, dass P die x3-Koordinate 6 hat",
    verfahren="Eine geeignete Seite der Schnittfigur so verlängern, dass sie h schneidet; der Schnittpunkt ist P, seine Höhe abzulesen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Verlängert man eine passende Seite der Schnittfigur bis zur Geraden h, liefert der Schnittpunkt die x3-Koordinate 6 von P (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P als Punkt der Schnittfigur selbst suchen",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich.")
row("2018MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen eines Teilkörpers als Differenz zweier Pyramiden berechnen und erläutern", typ_neben="",
    stichwoerter="Pyramide ABCP: 1/3 · 8 · 6 = 16|abzuziehen die Pyramide über der Deckfläche mit Grundfläche 1/2 · 2 · 2 und Höhe 3: 2|Teilkörper 14",
    voraussetzungen="Pyramidenvolumen|Teilkörper als Differenz erkennen|Maße aus dem Schrägbild",
    format="Rechnung|Begründung", operator="Berechnen Sie|Erläutern Sie", antwort="Zahl|Text",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="mittel",
    gegeben=QUA + "; Ebene durch A, C und P(4 | 4 | 6) zerlegt den Quader in zwei Teilkörper",
    gesucht="Volumen des Teilkörpers, zu dem B gehört, mit Erläuterung",
    verfahren="Pyramide ABCP (Grundfläche 8, Höhe 6) minus die kleine Pyramide über der Quaderdeckfläche (Grundfläche 2, Höhe 3)",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="V(ABCP) = 1/3 · 8 · 6 = 16, Ergänzungspyramide 1/3 · 2 · 3 = 2, Teilkörper 16 − 2 = 14 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Volumen der Pyramide ABCP als Ergebnis nehmen, ohne den über den Quader hinausragenden Teil abzuziehen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Schätzung III (Zerlegung als Deutung); bei der Prüfung gegen die enge Fassung auf II gesetzt, weil kein Eintrag der Deutungsliste greift – Ergänzung zur Pyramide ist eine Verkettung von Standardschritten.")
row("2018MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Spurpunkt einer Scharebene auf einer Koordinatenachse nachweisen", typ_neben="",
    stichwoerter="E_t: t x1 + t x2 − 4 x3 − 4t = 0|E_(−2): −2x1 − 2x2 − 4x3 + 8 = 0|(0 | 0 | 2) auf der x3-Achse und in E_(−2)",
    voraussetzungen="Punkt auf der x3-Achse: x1 = x2 = 0|Punktprobe in der Koordinatengleichung",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Für P_t(4 | 4 | t) liegen A, C und P_t in E_t: t · x1 + t · x2 − 4 · x3 − 4t = 0; E_6 ist die Ebene der abgebildeten Schnittfigur",
    gesucht="Nachweis, dass (0 | 0 | 2) der Schnittpunkt von E_(−2) mit der x3-Achse ist",
    verfahren="x1 = x2 = 0 und Punktprobe in E_(−2)",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(0 | 0 | 2) liegt wegen x1 = x2 = 0 auf der x3-Achse und wegen −2 · 0 − 2 · 0 − 4 · 2 + 8 = 0 in E_(−2) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="t = 2 statt t = −2 einsetzen",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Geschätzt I (Punktprobe), amtlich II.")
row("2018MgrundlegendBAGLAA2WTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Anzahl der Eckpunkte der Schnittfigur einer Ebenenschar mit einem Quader nach Parameterbereichen angeben", typ_neben="",
    stichwoerter="Dreieck statt Viereck für t ∈ [−3; 3] ohne 0|A und C stets Ecken|0 < t ≤ 3: dritte Ecke auf der Kante BF|−3 ≤ t < 0: auf der gegenüberliegenden Kante über O",
    voraussetzungen="Schnittfigur einer Ebene mit einem Quader nach Lage von P_t|Quaderhöhe 3 als Grenze",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl|Text",
    material="Körper", skizze=QUA_SK, kontext="ohne", textumfang="mittel",
    gegeben="E_t wie in e; die Schnittfigur des Quaders mit E_t ist für manche t ein Dreieck statt eines Vierecks",
    gesucht="alle Werte von t mit Dreieck; Lage der Eckpunkte in Abhängigkeit von t",
    verfahren="P_t innerhalb der Quaderhöhe (|t| ≤ 3, t ≠ 0) liefert ein Dreieck; für t > 0 liegt die dritte Ecke auf BF, für t < 0 auf der Kante über dem Ursprung",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="t ∈ [−3; 3] ohne 0; zwei Ecken sind stets A und C, die dritte liegt für 0 < t ≤ 3 auf der Kante BF, für −3 ≤ t < 0 auf der gegenüberliegenden Seitenkante (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="t = 0 (Ebene enthält die Grundfläche, keine Schnittfigur) nicht ausschließen",
    bemerkung="Standardbezug: K2 III, K4 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (b) Fallunterscheidung nach dem Vorzeichen von t mit verschiedener Lage der dritten Ecke. Typ wiederverwendet (2022-ea-B).")
# ---- AG/LA (A2) WTR 2: Kletteranlage, 20 BE (wortgleich in 2018-be-gk 2.2; Typen von dort)
KLE = ("Kletteranlage im Koordinatensystem (x1x2-Ebene ist der Untergrund, 1 LE = 1 m): Pfähle durch P1(0 | 0 | 0) und "
       "P2(5 | 10 | 0); Kletterwand mit den Eckpunkten A(3 | 0 | 2), B(0 | 3 | 2), E(6 | 0 | 0), F(0 | 6 | 0); "
       "Plattform 2 mit den Eckpunkten R(5 | 7 | 3), S(8 | 13 | 3), T(2 | 10 | 3)")
KLE_SK = ("Schrägbild eines räumlichen Koordinatensystems mit zwei waagerechten Plattformen um senkrechte Pfähle "
          "(Plattform 1 in Höhe 2 um den Pfahl durch P1, Plattform 2 in Höhe 3 um den Pfahl durch P2) und der "
          "geneigten Kletterwand ABFE zwischen Plattform 1 und dem Untergrund; Beschriftungen A, B, E, F, R, S, T.")
row("2018MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Streckenlänge im Raum berechnen", typ_neben="Punkt: Mittelpunkt einer Strecke im Raum bestimmen",
    stichwoerter="Mittelpunkte M1(1,5 | 1,5 | 2) von AB und M2(3 | 3 | 0) von EF|Abstand √(1,5² + 1,5² + 4) ≈ 2,9|Seil 20 % länger: ≈ 3,5 m",
    voraussetzungen="Mittelpunkt einer Strecke|Betrag eines Vektors|Prozentaufschlag",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="mittel",
    gegeben=KLE + "; in den Mittelpunkten der oberen Kante AB und der unteren Kante EF ist ein Seil befestigt, das 20 % länger ist als der Abstand der Mittelpunkte",
    gesucht="Länge des Seils",
    verfahren="Mittelpunkte bestimmen, Abstand berechnen, mit 1,2 multiplizieren",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="1,2 · |M1M2| = 1,2 · √(1,5² + 1,5² + 4) ≈ 3,5; das Seil ist etwa 3,5 m lang (amtlich)",
    zwischenergebnis="M1(1,5 | 1,5 | 2), M2(3 | 3 | 0)", niveau_geschaetzt="I",
    fehlerquelle="20 % vom Abstand als Seillänge nehmen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2018-be-gk 2.2 a; Typen von dort übernommen.")
row("2018MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen", typ_neben="",
    stichwoerter="EF = (−6; 6; 0) = 2 · AB|AE = (3; 0; −2), BF = (0; 3; −2), beide Länge √13|Trapez mit gleich langen Schenkeln",
    voraussetzungen="Vektoren auf Vielfache prüfen|Beträge vergleichen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="kurz",
    gegeben=KLE + "; A, B, E, F liegen in L: 2x1 + 2x2 + 3x3 − 12 = 0",
    gesucht="Nachweis, dass die Kletterwand ein Trapez mit zwei gleich langen gegenüberliegenden Seiten ist",
    verfahren="EF als Vielfaches von AB, Beträge von AE und BF vergleichen",
    schritte="3", zahlenraum="ganz|negativ|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="EF = 2 · AB, also AB ∥ EF (Trapez); |AE| = |BF| = √13 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Parallelität über gleiche Länge statt über das Vielfache begründen",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2018-be-gk 2.2 b; Typ von dort übernommen (der erhöhte Pool verlangt nur das Trapez).")
row("2018MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="Normalenvektor (2; 2; 3) von L, (0; 0; 1) der x1x2-Ebene|cos α = 3/√17|α ≈ 43°",
    voraussetzungen="Winkel zwischen Ebenen über die Normalenvektoren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="kurz",
    gegeben=KLE + "; Kletterwand in L: 2x1 + 2x2 + 3x3 − 12 = 0, Untergrund ist die x1x2-Ebene",
    gesucht="Größe des Winkels zwischen Kletterwand und Untergrund",
    verfahren="cos α = |n · e3| / (|n| · |e3|)",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="Grad", abhaengig_von="",
    ergebnis="cos α = 3/√17, α ≈ 43° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Winkel zwischen Normalenvektor und Ebene (Komplement 47°) angeben",
    bemerkung="Standardbezug: K2 I, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2018-be-gk 2.2 c; Typ von dort übernommen.")
row("2018MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="2", punkte="6", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punktprobe an einer Geraden durchführen",
    typ_neben="Schattenpunkt bei paralleler Projektion bestimmen|Ebene Figur: Schatten einer Fläche in eine Abbildung einzeichnen",
    stichwoerter="Sonnenlicht als parallele Geraden, R'(4 | 2 | 0), T'(1 | 5 | 0)|ET' = 5/6 · EF, T' auf der Strecke EF|Lichtrichtung RR' = (−1; −5; −3)|S' = S + RR' = (7 | 8 | 0)|Schatten RST einzeichnen",
    voraussetzungen="Punkt auf einer Strecke über den Parameter|Richtungsvektor aus Punkt und Schattenpunkt|Verschiebung anwenden|Eintragen ins Schrägbild",
    format="Begründung|Rechnung|Zeichnen", operator="Zeigen Sie|Berechnen Sie|Stellen Sie dar", antwort="Text|Zahl|Grafik",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="mittel",
    gegeben=KLE + "; Sonnenlicht als parallele Geraden; Schattenpunkte der Plattform 2: R'(4 | 2 | 0), S', T'(1 | 5 | 0)",
    gesucht="Nachweis, dass T' auf der Strecke EF liegt; Koordinaten von S'; Schatten der Plattform 2 in der Abbildung",
    verfahren="ET' = (−5; 5; 0) = 5/6 · EF mit 0 ≤ 5/6 ≤ 1; S' = S + (R' − R); Dreieck R'S'T' einzeichnen",
    schritte="4", zahlenraum="ganz|negativ|Bruch", einheiten="m", abhaengig_von="",
    ergebnis="ET' = 5/6 · EF, also T' auf EF; S' = (8; 13; 3) + (−1; −5; −3) = (7 | 8 | 0); Schatten als Dreieck R'S'T' (amtlich)",
    zwischenergebnis="RR' = (−1; −5; −3)", niveau_geschaetzt="II",
    fehlerquelle="T' nur als Punkt der Geraden EF nachweisen, ohne den Parameterbereich",
    bemerkung="Standardbezug: K1 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2018-be-gk 2.2 d; Typen von dort übernommen.")
row("2018MgrundlegendBAGLAA2WTR2", "e", innen="1", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Lösungsweg zur Bestimmung eines Punktes auf einer Geraden beschreiben", typ_neben="",
    stichwoerter="Seil von (0 | 0 | 2) am Pfahl 1 zum Pfahl 2 oberhalb der Plattform 2, berührt die Seite RT|Teilpunkt U von RT im bekannten Verhältnis|Gerade durch (0 | 0 | 2) und U mit der senkrechten Geraden durch P2 schneiden|Höhendifferenz zu R ist der Abstand",
    voraussetzungen="Teilpunkt einer Strecke|Gerade durch zwei Punkte|Schnitt zweier Geraden|Abstand als Koordinatendifferenz",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Körper", skizze=KLE_SK, kontext="Kletteranlage", textumfang="lang",
    gegeben=KLE + "; ein geradliniges Drahtseil von Pfahl 1 (Höhe der Plattform 1, Punkt (0 | 0 | 2)) zu Pfahl 2 oberhalb der Plattform 2 berührt die Plattform 2 an der Seite RT",
    gesucht="Beschreibung, wie der Abstand des oberen Seilendes von der Plattform 2 berechnet werden kann, wenn das Teilverhältnis des Berührpunkts auf RT bekannt wäre",
    verfahren="Teilpunkt U auf RT, Gerade durch (0 | 0 | 2) und U, Schnittpunkt V mit der Pfahlgeraden durch P2 (senkrecht zur x1x2-Ebene), Differenz der x3-Koordinaten von V und R",
    schritte="4", zahlenraum="ganz", einheiten="m", abhaengig_von="",
    ergebnis="U als Teilpunkt von RT bestimmen; Schnittpunkt V der Geraden durch (0 | 0 | 2) und U mit der Geraden durch P2 senkrecht zur x1x2-Ebene berechnen; die Differenz der x3-Koordinaten von V und R ist der Abstand in Metern (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="den Abstand des Seils von der Plattform statt des Endpunkts beschreiben",
    bemerkung="Standardbezug: K2 III, K3 III, K6 III. AB amtlich: III. Amtlich. Eichregel: (a) die Situation in Teilpunkt, Gerade und Schnitt mit der Pfahlgeraden übersetzen. Wortgleich im Landesheft 2018-be-gk 2.2 e; Typ von dort übernommen.")
# ---- Stochastik WTR 1: Jugendliche und Finanzangelegenheiten (Aufgabe 1, 17 BE), Varianzen (Aufgabe 2, 3 BE)
JUG = ("Jugendliche eines Landes: 49,20 % weiblich (W), 47,10 % erledigen Finanzangelegenheiten regelmäßig mit "
       "Smartphone oder Tablet (S), 19,68 % sind weiblich und tun das")
row("2018MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="W∩S 19,68 %, W∩¬S 29,52 %, ¬W∩S 27,42 %, ¬W∩¬S 23,38 %|Ränder 49,20/50,80 und 47,10/52,90",
    voraussetzungen="Vierfeldertafel aus zwei Rand- und einem Schnittanteil ergänzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Jugendliche/Finanzen", textumfang="kurz",
    gegeben=JUG,
    gesucht="vollständig ausgefüllte Vierfeldertafel",
    verfahren="Differenzen der Ränder",
    schritte="3", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="W∩S 19,68 %, W∩¬S 29,52 %, ¬W∩S 27,42 %, ¬W∩¬S 23,38 %; Ränder W 49,20 %, ¬W 50,80 %, S 47,10 %, ¬S 52,90 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="19,68 % als bedingten Anteil lesen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")
row("2018MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Anteil eines Entweder-oder-Ereignisses aus einer Tafel berechnen", typ_neben="",
    stichwoerter="entweder männlich oder S (nicht beides)|¬W∩¬S + W∩S = 23,38 % + 19,68 % = 43,06 %",
    voraussetzungen="„entweder – oder“ als ausschließendes Oder|Felder der Tafel addieren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Jugendliche/Finanzen", textumfang="kurz",
    gegeben=JUG + "; Vierfeldertafel aus a",
    gesucht="Wahrscheinlichkeit, dass eine zufällig ausgewählte Person entweder männlich ist oder ihre Finanzangelegenheiten regelmäßig mit Smartphone oder Tablet erledigt",
    verfahren="Die beiden Felder addieren, in denen genau eine der Eigenschaften zutrifft",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="2018MgrundlegendBStochastikWTR1-1a",
    ergebnis="19,68 % + 23,38 % = 43,06 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das einschließende Oder rechnen (¬W ∪ S = 76,62 %)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2022-ea-B), Thema des Typs.")
row("2018MgrundlegendBStochastikWTR1", "c", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="P_W(S) = 19,68 %/49,20 % = 40 %",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Jugendliche/Finanzen", textumfang="kurz",
    gegeben=JUG,
    gesucht="Nachweis, dass unter den weiblichen Jugendlichen 40 % ihre Finanzangelegenheiten mit Smartphone oder Tablet erledigen",
    verfahren="Schnittanteil durch Randanteil",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="P_W(S) = 19,68 %/49,20 % = 40 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="durch 47,10 % teilen (Bedingung vertauscht)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet. Geschätzt I (ein Quotient), amtlich II.")
row("2018MgrundlegendBStochastikWTR1", "d", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="X: Anzahl unter 50 weiblichen Jugendlichen mit S, B(50; 0,4)|A: X = 25, P ≈ 4,0 %|B: X ≥ 26, P = 1 − P(X ≤ 25) ≈ 5,7 %",
    voraussetzungen="Binomialverteilung mit p = 0,4 aus c|Einzel- und kumulierte Wahrscheinlichkeit am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Jugendliche/Finanzen", textumfang="mittel",
    gegeben=JUG + "; 50 weibliche Jugendliche werden zufällig ausgewählt, P_W(S) = 40 %",
    gesucht="P(A): genau die Hälfte erledigt Finanzangelegenheiten mit Smartphone oder Tablet; P(B): mehr als die Hälfte",
    verfahren="X ~ B(50; 0,4): P(X = 25) und P(X ≥ 26) = 1 − P(X ≤ 25) am Rechner",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="2018MgrundlegendBStochastikWTR1-1c",
    ergebnis="P(A) = P(X = 25) ≈ 4,0 %; P(B) = P(X ≥ 26) = 1 − P(X ≤ 25) ≈ 5,7 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="„mehr als die Hälfte“ als X ≥ 25 ansetzen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,0405; 0,0573).")
row("2018MgrundlegendBStochastikWTR1", "e", innen="1", seite="2", punkte="2", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Ungeeignetheit des Binomialmodells begründen", typ_neben="",
    stichwoerter="zehn Jugendliche, vier nur Smartphone, sechs nur Tablet, drei werden ausgewählt|Ziehen ohne Zurücklegen aus kleiner Gesamtheit|Wahrscheinlichkeit ändert sich je Zug",
    voraussetzungen="Voraussetzungen einer Bernoulli-Kette (konstantes p, Unabhängigkeit)",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Jugendliche/Finanzen", textumfang="kurz",
    gegeben="Gruppe von zehn Jugendlichen, vier nutzen nur Smartphones, sechs nur Tablets; drei werden zufällig ausgewählt",
    gesucht="Begründung, dass die Binomialverteilung für die Anzahl der Smartphone-Nutzer unter den Ausgewählten nicht geeignet ist",
    verfahren="Auswahl ist Ziehen ohne Zurücklegen aus einer kleinen Gesamtheit, die Trefferwahrscheinlichkeit bleibt nicht konstant",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Auswahl entspricht dem Ziehen ohne Zurücklegen; da die Gesamtzahl klein ist, ändert sich die Wahrscheinlichkeit von Zug zu Zug, die Binomialverteilung ist nicht geeignet (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit „zu wenige Versuche“ argumentieren",
    bemerkung="Standardbezug: K1 III, K3 II, K6 III. AB amtlich: III. Amtlich. Typ wiederverwendet (2017-bb-ea). Geschätzt II, amtlich III – Begründung der Modellgrenze zählt im Standardbezug als III.")
row("2018MgrundlegendBStochastikWTR1", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit für genau k einer Sorte beim mehrfachen Ziehen über Pfade berechnen", typ_neben="",
    stichwoerter="genau zwei von drei nur Smartphone|drei Reihenfolgen · 4/10 · 3/9 · 6/8 = 3/10",
    voraussetzungen="Pfadregeln ohne Zurücklegen|Anzahl der Reihenfolgen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Jugendliche/Finanzen", textumfang="kurz",
    gegeben="Zehn Jugendliche, vier nur Smartphone, sechs nur Tablet; drei werden zufällig ausgewählt",
    gesucht="Wahrscheinlichkeit, dass genau zwei der drei nur Smartphones nutzen",
    verfahren="Pfad SST mit 4/10 · 3/9 · 6/8, mal drei Reihenfolgen",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="3 · 4/10 · 3/9 · 6/8 = 30 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Reihenfolgen vergessen (10 %)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MgrundlegendBStochastikWTR1", "", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Verhältnis der Varianzen zweier Binomialverteilungen aus dem Erwartungswert im Diagramm bestimmen", typ_neben="",
    stichwoerter="Y1 ~ B(20; p1), Diagramm mit Maximum bei 8, E(Y1) = 8 ganzzahlig, p1 = 0,4|Y2 ~ B(40; p2) mit E(Y2) = 4, p2 = 0,1|Var(Y1)/Var(Y2) = 4,8/3,6 = 4/3",
    voraussetzungen="Erwartungswert am Diagramm ablesen|n · p und n · p · (1 − p)",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm",
    skizze="Säulendiagramm P(Y1 = k) für k = 0 bis 20, Achse bis 0,2: Säulen ab k = 2 wachsend, Maximum etwa 0,18 bei k = 8, symmetrisch abfallend bis etwa k = 14.",
    kontext="ohne", textumfang="mittel",
    gegeben="Diagramm der Verteilung von Y1 ~ B(20; p1) mit ganzzahligem Erwartungswert; Y2 ~ B(40; p2) mit halb so großem Erwartungswert",
    gesucht="Verhältnis der Varianzen von Y1 und Y2",
    verfahren="E(Y1) = 8 ablesen, p1 = 0,4; E(Y2) = 4, p2 = 0,1; Varianzen n · p · (1 − p) bilden",
    schritte="3", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="p1 = 0,4, p2 = 0,1; Var(Y1)/Var(Y2) = (20 · 0,4 · 0,6)/(40 · 0,1 · 0,9) = 4/3 (amtlich)",
    zwischenergebnis="Var(Y1) = 4,8, Var(Y2) = 3,6", niveau_geschaetzt="III",
    fehlerquelle="das Verhältnis der Standardabweichungen angeben",
    bemerkung="Standardbezug: K2 II, K3 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) den Erwartungswert aus dem Maximum des Diagramms erschließen und in p übersetzen, verkettet mit der Varianzformel.")
# ---- Stochastik WTR 2: Bildschirme, 20 BE (a–d und g in 2018-be-gk 3.2; Typen von dort)
BIL = "Flachbildschirme, im Mittel einer von fünf fehlerhaft; die Anzahl fehlerhafter Geräte unter zufällig ausgewählten ist binomialverteilt (p = 0,2)"
row("2018MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="A: unter 50 höchstens 8 fehlerhaft, P ≈ 30,7 %|B: unter 200 mehr als 30 und weniger als 50, P(31 ≤ X ≤ 49) ≈ 90,8 %",
    voraussetzungen="Kumulierte Binomialwahrscheinlichkeit am Rechner|strikte Ungleichungen in Grenzen übersetzen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="mittel",
    gegeben=BIL,
    gesucht="P(A): von 50 höchstens 8 fehlerhaft; P(B): von 200 mehr als 30 und weniger als 50 fehlerhaft",
    verfahren="P(X ≤ 8) mit n = 50; P(X ≤ 49) − P(X ≤ 30) mit n = 200",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(A) ≈ 30,7 %; P(B) = P(30 < X < 50) ≈ 90,8 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="bei B die Grenzen 30 und 50 einschließen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Im Landesheft 2018-be-gk 3.2 a abgewandelt (Ereignis B mit 50 statt 200 Bildschirmen); Typ von dort übernommen.")
row("2018MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Modalwert einer Binomialverteilung bestimmen", typ_neben="",
    stichwoerter="n = 250, p = 0,2|Erwartungswert 50 ganzzahlig|wahrscheinlichste Anzahl 50",
    voraussetzungen="Erwartungswert n · p|ganzzahliger Erwartungswert ist die wahrscheinlichste Anzahl",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="kurz",
    gegeben=BIL + "; 250 Bildschirme zufällig ausgewählt",
    gesucht="Anzahl fehlerhafter Geräte, die mit der größten Wahrscheinlichkeit auftritt",
    verfahren="Erwartungswert 250 · 0,2 = 50 ist ganzzahlig",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="250 · 0,2 = 50, der Erwartungswert ist ganzzahlig, also ist 50 die gesuchte Anzahl (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den Erwartungswert ohne die Ganzzahligkeitsbegründung als Modalwert nehmen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2018-be-gk 3.2 b; Typ von dort übernommen.")
row("2018MgrundlegendBStochastikWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen", typ_neben="",
    stichwoerter="P(alle fehlerfrei) = 0,8^n|0,8^(n+1) < 0,8^n|Aussage richtig",
    voraussetzungen="Wahrscheinlichkeit für null Treffer als Potenz|Monotonie einer Potenz mit Basis kleiner 1",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="mittel",
    gegeben=BIL + "; Aussage: Wird eine Stichprobe um einen zufällig ausgewählten Bildschirm ergänzt, ist die Wahrscheinlichkeit, dass alle fehlerfrei sind, danach geringer",
    gesucht="Beurteilung der Aussage",
    verfahren="0,8^(n+1) = 0,8 · 0,8^n < 0,8^n",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist richtig: 0,8^(n+1) < 0,8^n (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit einem Zahlenbeispiel statt allgemein begründen",
    bemerkung="Standardbezug: K1 II, K5 II, K6 II. AB amtlich: II. Amtlich. Wortgleich im Landesheft 2018-be-gk 3.2 c; Typ von dort übernommen.")
row("2018MgrundlegendBStochastikWTR2", "d", innen="1", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer bestimmen", typ_neben="",
    stichwoerter="P(keiner von 25 fehlerhaft) = (1 − x)^25 ≥ 0,1|1 − x ≥ 0,1^(1/25)|x ≤ 1 − 0,1^(1/25) ≈ 8,8 %",
    voraussetzungen="Null Treffer als Potenz von 1 − p|Ungleichung durch Wurzelziehen lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="mittel",
    gegeben=BIL + "; nach einer Verbesserung soll P(keiner von 25 fehlerhaft) ≥ 10 % sein",
    gesucht="höchstzulässiger Anteil fehlerhafter Geräte nach der Verbesserung",
    verfahren="(1 − x)^25 ≥ 0,1 nach x auflösen",
    schritte="3", zahlenraum="dezimal|Prozent|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="(1 − x)^25 ≥ 0,1 ⇔ x ≤ 1 − 0,1^(1/25) ≈ 8,8 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die 25. Wurzel als Division durch 25 ausführen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Sachbedingung in (1 − x)^25 ≥ 0,1 übersetzen, verkettet mit dem Auflösen. Wortgleich im Landesheft 2018-be-gk 3.2 d; Typ von dort übernommen.")
row("2018MgrundlegendBStochastikWTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="D Display defekt 10,7 %, N Netzteil defekt 3,0 %, weder noch 87,3 %|D∩N 1,0 %, D∩¬N 9,7 %, ¬D∩N 2,0 %",
    voraussetzungen="Vierfeldertafel aus zwei Rändern und einem Feld ergänzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="kurz",
    gegeben="Für einen zufällig ausgewählten Bildschirm: Display defekt 10,7 %, weder Display noch Netzteil defekt 87,3 %, Netzteil defekt 3,0 %",
    gesucht="vollständig ausgefüllte Vierfeldertafel",
    verfahren="¬D∩¬N = 87,3 %, Ränder 10,7/89,3 und 3,0/97,0, Rest als Differenzen",
    schritte="3", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="D∩N 1,0 %, ¬D∩N 2,0 %, D∩¬N 9,7 %, ¬D∩¬N 87,3 %; Ränder N 3,0 %, ¬N 97,0 %, D 10,7 %, ¬D 89,3 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="87,3 % als Feld „genau eines defekt“ lesen",
    bemerkung="Standardbezug: K2 I, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet. Wortgleich im Landesheft 2018-be-gk 3.2 e (dort bislang als abgewandelt auf den erhöhten Pool vorgemerkt; Umstellung hierher im Abgleichlauf 15). Geschätzt I, amtlich II.")
row("2018MgrundlegendBStochastikWTR2", "f", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="P_D(N) = 0,01/0,107 ≈ 9,3 %",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient aus der Tafel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="kurz",
    gegeben="Vierfeldertafel aus e (D∩N 1,0 %, D 10,7 %)",
    gesucht="Wahrscheinlichkeit, dass ein Bildschirm mit defektem Display ein defektes Netzteil hat",
    verfahren="Schnittanteil durch Randanteil von D",
    schritte="1", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="2018MgrundlegendBStochastikWTR2-1e",
    ergebnis="0,01/0,107 ≈ 9,3 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="durch 3,0 % teilen (Bedingung vertauscht)",
    bemerkung="Standardbezug: K3 II, K4 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet. Wortgleich im Landesheft 2018-be-gk 3.2 f (dort ohne Vermerk; offener Posten in der Stapelliste § 4). Geschätzt I, amtlich II.")
row("2018MgrundlegendBStochastikWTR2", "g", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Ungeeignetheit des Binomialmodells begründen", typ_neben="",
    stichwoerter="40 geprüfte Bildschirme, 6 fehlerhaft, 10 ausgewählt|binomialverteilt wäre auch 7 fehlerhafte möglich|Widerspruch, nicht binomialverteilt",
    voraussetzungen="Wertebereich einer Binomialverteilung|Ziehen ohne Zurücklegen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bildschirme/Produktion", textumfang="kurz",
    gegeben="Von 40 geprüften Bildschirmen, unter denen 6 fehlerhaft sind, werden 10 zufällig ausgewählt",
    gesucht="Beurteilung, ob die Anzahl fehlerhafter Bildschirme unter den ausgewählten binomialverteilt ist",
    verfahren="Bei Binomialverteilung wären 7 fehlerhafte unter den 10 möglich, es gibt aber nur 6",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Nicht binomialverteilt: sonst wären etwa sieben fehlerhafte Bildschirme unter den ausgewählten möglich, im Widerspruch zum Sachzusammenhang (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Binomialverteilung wegen „fehlerhaft oder nicht“ bejahen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich. Typ wiederverwendet. Wortgleich im Landesheft 2018-be-gk 3.2 g (dort bislang auf den erhöhten Pool Stochastik WTR 2 d vorgemerkt, der ebenfalls wortgleich ist; Umstellung hierher im Abgleichlauf 15); Typ vom Landesheft übernommen.")
# ---- Stochastik WTR 3: Hundefutter (Aufgabe 1, 10 BE), Zwölfseiten-Würfel (Aufgabe 2, 10 BE)
HUN = ("Hundefutter: 2/3 der Kunden kaufen Trockenfutter (T), davon 40 % die Light-Variante (L); von den "
       "Nassfutterkäufern wählen 25 % Light; eine Person wird zufällig ausgewählt")
row("2018MgrundlegendBStochastikWTR3", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="erste Stufe T 2/3, ¬T 1/3|zweite Stufe L 0,4/0,6 bzw. 0,25/0,75",
    voraussetzungen="Anteile als Pfadwahrscheinlichkeiten eintragen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Hundefutter/Kunden", textumfang="mittel",
    gegeben=HUN,
    gesucht="beschriftetes Baumdiagramm",
    verfahren="Zwei Stufen T/¬T und L/¬L mit den Anteilen",
    schritte="1", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Baum: T (2/3) mit L 0,4 und ¬L 0,6; ¬T (1/3) mit L 0,25 und ¬L 0,75 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="40 % als Anteil aller Kunden statt der Trockenfutterkäufer eintragen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet.")
row("2018MgrundlegendBStochastikWTR3", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Totale Wahrscheinlichkeit über die Pfadregeln nachweisen", typ_neben="",
    stichwoerter="P(L) = 2/3 · 0,4 + 1/3 · 0,25 = 35 %",
    voraussetzungen="Pfadmultiplikation und -addition",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="keins", skizze="keine", kontext="Hundefutter/Kunden", textumfang="kurz",
    gegeben=HUN,
    gesucht="Nachweis, dass P(L) = 35 %",
    verfahren="Beide Pfade zu L addieren",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="2018MgrundlegendBStochastikWTR3-1a",
    ergebnis="2/3 · 0,4 + 1/3 · 0,25 = 35 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Anteile ohne Gewichtung addieren",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-B).")
row("2018MgrundlegendBStochastikWTR3", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="P_L(¬T) = (1/3 · 0,25)/0,35 ≈ 23,8 %",
    voraussetzungen="Umgekehrte Bedingung über Pfad durch Gesamtwahrscheinlichkeit (Bayes)",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Hundefutter/Kunden", textumfang="kurz",
    gegeben=HUN + "; P(L) = 35 %; die ausgewählte Person hat Light gewählt",
    gesucht="Wahrscheinlichkeit, dass es Nassfutter ist",
    verfahren="Pfad ¬T∩L durch P(L)",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="2018MgrundlegendBStochastikWTR3-1b",
    ergebnis="(1/3 · 0,25)/0,35 ≈ 23,8 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P_¬T(L) = 25 % als Antwort geben (Bedingung vertauscht)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet; hier die umgekehrte Bedingung aus dem Baumdiagramm (Bayes).")
row("2018MgrundlegendBStochastikWTR3", "d", innen="1", seite="1", punkte="2", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Gegenereignis einer Vereinigung im Sachzusammenhang beschreiben", typ_neben="",
    stichwoerter="Ereignis: Gegenereignis von (¬T ∪ L), doppelter Überstrich|De Morgan: T ∩ ¬L|Trockenfutter in der normalen Variante",
    voraussetzungen="De Morgan: Gegenereignis einer Vereinigung ist der Schnitt der Gegenereignisse|doppelten Überstrich lesen",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Hundefutter/Kunden", textumfang="kurz",
    gegeben=HUN + "; Ereignis: Gegenereignis der Vereinigung von „nicht T“ und L (Überstrich über dem ganzen Term)",
    gesucht="Beschreibung des Ereignisses im Sachzusammenhang",
    verfahren="Das Gegenereignis der Vereinigung ist der Schnitt der Gegenereignisse: T und nicht L",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die zufällig ausgewählte Person kauft Trockenfutter in der normalen Variante (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den äußeren Überstrich übersehen und „Nassfutter oder Light“ beschreiben",
    bemerkung="Standardbezug: K1 III, K4 III, K6 II. AB amtlich: III. Amtlich. Geschätzt II (Deutung eines Mengenterms), amtlich III – die Übersetzung über De Morgan zählt im Standardbezug als III. Der doppelte Überstrich ist nur am Bild lesbar, die Textextraktion zeigt „T ∪ L“.")
WUE = ("Zwölfseitiger Spielwürfel, alle Seiten gleich wahrscheinlich, nach dem abgebildeten Netz neun Seiten mit 1 "
       "und drei Seiten mit 2 beschriftet; je Spiel wird viermal geworfen")
WUE_SK = "Netz eines Dodekaeders aus zwölf Fünfecken, neun mit 1 beschriftet, drei mit 2 (die 2-Seiten grau)."
row("2018MgrundlegendBStochastikWTR3", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeiten zweier Extremsummen über die Häufigkeit der Beschriftung vergleichen", typ_neben="",
    stichwoerter="Summe 4 nur bei viermal 1, Summe 8 nur bei viermal 2|mehr Seiten mit 1 als mit 2|(9/12)^4 > (3/12)^4",
    voraussetzungen="Extremsummen als einzige Ergebnisfolgen erkennen|Laplace-Wahrscheinlichkeit aus Seitenzahlen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Figur", skizze=WUE_SK, kontext="Gewinnspiel/Würfel", textumfang="kurz",
    gegeben=WUE,
    gesucht="Begründung, dass die Summe 4 wahrscheinlicher ist als die Summe 8",
    verfahren="Summe 4 heißt viermal 1, Summe 8 viermal 2; die Mehrzahl der Seiten trägt die 1",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Summe 4 genau bei viermal 1, Summe 8 genau bei viermal 2; da mehr Seiten die 1 tragen, ist viermal 1 wahrscheinlicher (amtlich)",
    zwischenergebnis="(3/4)^4 gegen (1/4)^4", niveau_geschaetzt="I",
    fehlerquelle="nur die Anzahl der Seiten vergleichen, ohne die Summen auf die Ergebnisfolgen zurückzuführen",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich. Erste Schätzung II; bei der Prüfung gegen die enge Fassung auf I gesetzt – eine einzelne begründete Beobachtung (Extremsummen heißen lauter gleiche Würfe), keine Verkettung.")
row("2018MgrundlegendBStochastikWTR3", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Summenbedingung bei wiederholtem Wurf in eine Binomialwahrscheinlichkeit übersetzen und nachweisen", typ_neben="",
    stichwoerter="Hauptpreis bei Summe ≥ 7|X: Anzahl der Einsen unter vier Würfen, B(4; 0,75)|Summe ≥ 7 ⇔ X ≤ 1|P(X ≤ 1) ≈ 0,05 = 1/20",
    voraussetzungen="Summe in die Anzahl der Zweien bzw. Einsen übersetzen|kumulierte Binomialwahrscheinlichkeit",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Figur", skizze=WUE_SK, kontext="Gewinnspiel/Würfel", textumfang="mittel",
    gegeben=WUE + "; Hauptpreis bei Summe mindestens 7",
    gesucht="Nachweis, dass im Mittel etwa bei einem von zwanzig Spielen ein Hauptpreis vergeben wird",
    verfahren="Summe ≥ 7 heißt höchstens eine 1 unter vier Würfen; P(X ≤ 1) mit X ~ B(4; 0,75)",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="X: Anzahl der Würfe mit der Zahl 1; P(X ≤ 1) ≈ 0,05 = 1/20 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Summe ≥ 7 als „mindestens drei Zweien“ mit falscher Trefferwahrscheinlichkeit rechnen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,0508).")
row("2018MgrundlegendBStochastikWTR3", "c", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitswert als Potenz angeben", typ_neben="",
    stichwoerter="81/256 = (3/4)^4|viermal die 1, Summe 4",
    voraussetzungen="Bruch als Potenz erkennen|Potenz als Ergebnisfolge deuten",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Figur", skizze=WUE_SK, kontext="Gewinnspiel/Würfel", textumfang="kurz",
    gegeben=WUE + "; Trostpreis für einen Spielausgang mit Wahrscheinlichkeit 81/256",
    gesucht="ein passender Spielausgang mit Begründung",
    verfahren="81/256 = (3/4)^4 als Wahrscheinlichkeit für viermal die 1",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Summe 4 (viermal die Zahl 1), weil (3/4)^4 = 81/256 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="81/256 nicht als Potenz erkennen",
    bemerkung="Standardbezug: K1 I, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2018MgrundlegendBStochastikWTR3", "d", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussagen über Bernoulli-Experiment und Bernoulli-Kette im Sachzusammenhang beurteilen", typ_neben="",
    stichwoerter="ein Wurf mit Ergebnis 1 oder 2: Bernoulli-Experiment, richtig|Spiele mit Trost- oder Hauptpreis: keine Bernoulli-Kette, weil auch kein Preis möglich (Summe 5 oder 6)|falsch",
    voraussetzungen="Bernoulli-Experiment: genau zwei Ergebnisse|Bernoulli-Kette: Wiederholung desselben Bernoulli-Experiments",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Figur", skizze=WUE_SK, kontext="Gewinnspiel/Würfel", textumfang="mittel",
    gegeben=WUE + "; Aussagen: (1) Ein Wurf mit Betrachtung der Zahl ist ein Bernoulli-Experiment; (2) bei mehreren Spielen jeweils festzuhalten, ob Trost- oder Hauptpreis vergeben wird, ist eine Bernoulli-Kette",
    gesucht="Beurteilung beider Aussagen",
    verfahren="(1) zwei mögliche Ergebnisse; (2) ein Spiel hat neben Trost- und Hauptpreis ein drittes Ergebnis (kein Preis, etwa Summe 5)",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(1) richtig: Zufallsexperiment mit genau zwei Ergebnissen; (2) falsch: die Summe kann 5 sein, also gibt es neben Trost- und Hauptpreis ein weiteres Ergebnis (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="(2) bejahen, weil nur zwei Preise genannt werden",
    bemerkung="Standardbezug: K1 III, K3 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (d) sinngemäß – die Definition der Bernoulli-Kette auf den Spielausgang übertragen und das dritte Ergebnis finden.")

NEUE_TYPEN = [
    ("Wendepunkt an vorgegebener Stelle nachweisen und Wendetangente aufstellen", "Analysis", "Kurvenuntersuchung",
     "Für eine genannte Stelle über zweite und dritte Ableitung nachweisen, dass dort ein Wendepunkt liegt, und die Gleichung der Tangente in diesem Punkt aufstellen.",
     "2018MgrundlegendBAnalysisWTR-1a"),
    ("Symmetrie: Punktsymmetrie zum Wendepunkt über die Verschiebung einer ungeraden Funktion begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Verschiebung angeben, mit der ein Graph aus dem Graphen einer nur ungerade Potenzen enthaltenden Funktion hervorgeht, und daraus die Punktsymmetrie zum Wendepunkt folgern.",
     "2018MgrundlegendBAnalysisWTR-1b"),
    ("Körper: Oberflächeninhalt des Rotationskegels eines rechtwinkligen Dreiecks berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Körper erkennen, der bei Rotation eines rechtwinkligen Dreiecks um eine Kathete entsteht (Kegel), und seinen Oberflächeninhalt aus Radius, Höhe und Mantellinie berechnen; die Maße kommen aus Koordinaten oder Funktionswerten.",
     "2018MgrundlegendBAnalysisWTR-1c"),
    ("Integralwert: Ungleichung zweier Integrale über das Vorzeichen des Teilintegrals am Graphen begründen", "Analysis", "Flächeninhalt durch Integration",
     "Ohne Rechnung begründen, dass ein Integral über ein größeres Intervall kleiner ist als über ein Teilintervall, weil das hinzukommende Teilintegral am Graphen negativ ist.",
     "2018MgrundlegendBAnalysisWTR-1e"),
    ("Lage zweier Graphen aus dem Graphen ihrer Differenzfunktion beschreiben", "Analysis", "Kurvenuntersuchung",
     "Aus dem abgebildeten Graphen von h − f die gegenseitige Lage der Graphen von f und h beschreiben: Nullstellen als gemeinsame Punkte, Vorzeichen als Lage über oder unter, Extremstellen als größter Abstand.",
     "2018MgrundlegendBAnalysisWTR-1f"),
    ("Nullstellen und Werte: Stelle zu einem vorgegebenen Funktionswert am Graphen ablesen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus einer Abbildung die Stelle ablesen, an der eine Funktion einen vorgegebenen Wert annimmt, gegebenenfalls nach Umrechnung der Einheit.",
     "2018MgrundlegendBAnalysisWTR-2a"),
    ("Aussage über die Zunahme der Zusatzkosten über Differenzen von Funktionswerten beurteilen", "Analysis", "Ableitung und Änderungsrate",
     "Eine Aussage über das Wachsen der Kosten je zusätzlicher Einheit beurteilen, indem Differenzen aufeinanderfolgender Funktionswerte (oder die Steigung) verglichen werden, etwa mit einem Gegenbeispiel.",
     "2018MgrundlegendBAnalysisWTR-2c"),
    ("Nullstellen und Werte: Gleichheit zweier Funktionswerte durch Einsetzen im Sachzusammenhang nachweisen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Durch Einsetzen einer Stelle in zwei Funktionsterme (etwa Erlös und Kosten) nachweisen, dass die Werte übereinstimmen, und das im Sachzusammenhang deuten (kein Gewinn).",
     "2018MgrundlegendBAnalysisWTR-2d"),
    ("Gewinnbereich als Bereich zwischen den Schnittstellen von Erlösgerade und Kostengraph zeichnerisch bestimmen", "Analysis", "Kurvenuntersuchung",
     "Die Erlösgerade in die Abbildung des Kostengraphen einzeichnen und den Bereich ablesen, in dem sie oberhalb des Kostengraphen liegt (Gewinnzone zwischen den Schnittstellen).",
     "2018MgrundlegendBAnalysisWTR-2e"),
    ("Maximum einer Gewinnfunktion über die Ableitung berechnen", "Analysis", "Kurvenuntersuchung",
     "Die Gewinnfunktion als Differenz von Erlös und Kosten aufstellen, die Stelle des größten Gewinns über die Nullstellen der Ableitung berechnen und die Lösung im zulässigen Bereich auswählen.",
     "2018MgrundlegendBAnalysisWTR-2f"),
    ("Übergangsprozess: Wechselzahlen nach einem Übergang berechnen und Gleichgewicht deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus Bestandszahlen und Wechselanteilen die Anzahl der Wechsler je Zustand berechnen und gleiche Wechselzahlen als unveränderte Bestände (Gleichgewicht) deuten.",
     "2018MgrundlegendBAGLAA1WTR-1b"),
    ("Übergangsprozess: Gleichungssystem für die Verteilung vor einem Übergang aufstellen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus M · v = w mit bekannter Verteilung w nach dem Übergang das lineare Gleichungssystem für die unbekannte Verteilung v davor angeben, ohne es zu lösen.",
     "2018MgrundlegendBAGLAA1WTR-1c"),
    ("Übergangsprozess: Verteilung nach einem Übergang berechnen und einen Anteil angeben", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Mit der Übergangsmatrix die Bestände nach einem Schritt berechnen (auch über die feste Gesamtzahl) und den prozentualen Anteil eines Zustands angeben.",
     "2018MgrundlegendBAGLAA1WTR-1d"),
    ("Übergangsprozess: Zustand mit dem kleinsten Wechselanteil aus der Matrix ablesen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus den Diagonaleinträgen der Übergangsmatrix den Zustand mit dem größten Bleibeanteil bestimmen und den zugehörigen Wechselanteil als Komplement angeben.",
     "2018MgrundlegendBAGLAA1WTR-1e"),
    ("Übergangsprozess: Potenz der Übergangsmatrix als mehrschrittigen Übergang deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen Term wie M · M · M im Sachzusammenhang als Übergang über entsprechend viele Schritte (etwa ein Vierteljahr) beschreiben.",
     "2018MgrundlegendBAGLAA1WTR-1f"),
    ("Übergangsprozess: Bereich eines Anteils in Abhängigkeit vom Matrixparameter über die Randwerte ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen Bestand oder Anteil als Term im Parameter der Übergangsmatrix aufstellen (etwa als Rest zur Gesamtzahl) und aus der Monotonie des Terms den Wertebereich über die Randwerte des Parameters angeben.",
     "2018MgrundlegendBAGLAA1WTR-1g"),
    ("Übergangsprozess: Matrixparameter aus einer Komponente nach einem Schritt bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Den unbekannten Eintrag einer Übergangsmatrix aus einer bekannten Komponente der Verteilung nach einem Schritt über eine lineare Gleichung bestimmen.",
     "2018MgrundlegendBAGLAA1WTR-1h"),
    ("Ebene Figur: Rechtwinkliges gleichschenkliges Dreieck aus den Koordinaten begründen und Flächeninhalt angeben", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Aus achsenparallelen Koordinaten (etwa einem Quadrat) begründen, dass ein Dreieck rechtwinklig und gleichschenklig ist, und seinen Flächeninhalt ohne Vektorrechnung angeben.",
     "2018MgrundlegendBAGLAA2WTR1-1a"),
    ("Geradengleichung durch zwei Punkte aufstellen und windschiefe Lage begründen", "Analytische Geometrie", "Geraden",
     "Die Parametergleichung einer Geraden durch zwei Punkte angeben und begründen, dass sie zu einer anderen Geraden windschief ist (kein gemeinsamer Punkt, nicht parallel), etwa über die Lage in einer Koordinatenebene.",
     "2018MgrundlegendBAGLAA2WTR1-1b"),
    ("Koordinate eines Punktes aus der Schnittfigur zeichnerisch ermitteln und Vorgehen beschreiben", "Analytische Geometrie", "Schnittmengen",
     "Beschreiben, wie eine Koordinate eines Punktes aus dem Schrägbild einer Schnittfigur gewonnen wird, etwa durch Verlängern einer Schnittkante bis zu einer Geraden.",
     "2018MgrundlegendBAGLAA2WTR1-1c"),
    ("Körper: Volumen eines Teilkörpers als Differenz zweier Pyramiden berechnen und erläutern", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Das Volumen eines durch eine Ebene abgeschnittenen Teilkörpers eines Quaders als Differenz einer großen Pyramide und einer kleineren Ergänzungspyramide berechnen und den Ansatz erläutern.",
     "2018MgrundlegendBAGLAA2WTR1-1d"),
    ("Spurpunkt einer Scharebene auf einer Koordinatenachse nachweisen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Für einen Parameterwert einer Ebenenschar nachweisen, dass ein gegebener Punkt auf einer Koordinatenachse liegt und die Ebenengleichung erfüllt.",
     "2018MgrundlegendBAGLAA2WTR1-1e"),
    ("Ziehen ohne Zurücklegen: Wahrscheinlichkeit für genau k einer Sorte beim mehrfachen Ziehen über Pfade berechnen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Beim mehrfachen Ziehen ohne Zurücklegen die Wahrscheinlichkeit für genau k Objekte einer Sorte als Pfadprodukt mal Anzahl der Reihenfolgen berechnen.",
     "2018MgrundlegendBStochastikWTR1-1f"),
    ("Verhältnis der Varianzen zweier Binomialverteilungen aus dem Erwartungswert im Diagramm bestimmen", "Stochastik", "Kenngrößen von Verteilungen",
     "Aus dem Säulendiagramm einer Binomialverteilung den Erwartungswert ablesen, daraus p bestimmen, eine zweite Verteilung über eine Erwartungswertbedingung festlegen und das Verhältnis der Varianzen n · p · (1 − p) berechnen.",
     "2018MgrundlegendBStochastikWTR1-2"),
    ("Gegenereignis einer Vereinigung im Sachzusammenhang beschreiben", "Stochastik", "Ereignisse und Mengenoperationen",
     "Ein als Gegenereignis einer Vereinigung notiertes Ereignis (Überstrich über dem ganzen Term) im Sachzusammenhang beschreiben, indem es nach De Morgan als Schnitt der Gegenereignisse gelesen wird.",
     "2018MgrundlegendBStochastikWTR3-1d"),
    ("Laplace-Experiment: Wahrscheinlichkeiten zweier Extremsummen über die Häufigkeit der Beschriftung vergleichen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Für einen Würfel mit ungleich verteilten Beschriftungen begründen, welche von zwei nur durch eine einzige Ergebnisfolge erreichbaren Summen wahrscheinlicher ist.",
     "2018MgrundlegendBStochastikWTR3-2a"),
    ("Summenbedingung bei wiederholtem Wurf in eine Binomialwahrscheinlichkeit übersetzen und nachweisen", "Stochastik", "Binomialverteilung",
     "Eine Bedingung an die Summe mehrerer Würfe eines zweiwertigen Würfels in eine Bedingung an die Trefferzahl übersetzen und die Wahrscheinlichkeit als kumulierte Binomialwahrscheinlichkeit nachweisen.",
     "2018MgrundlegendBStochastikWTR3-2b"),
    ("Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitswert als Potenz angeben", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Einen vorgegebenen Wahrscheinlichkeitswert als Potenz einer Einzelwahrscheinlichkeit erkennen und ein Ereignis (Ergebnisfolge) angeben, das diese Wahrscheinlichkeit hat.",
     "2018MgrundlegendBStochastikWTR3-2c"),
    ("Aussagen über Bernoulli-Experiment und Bernoulli-Kette im Sachzusammenhang beurteilen", "Stochastik", "Binomialverteilung",
     "Beurteilen, ob ein beschriebenes Zufallsexperiment ein Bernoulli-Experiment und ob eine Wiederholung eine Bernoulli-Kette ist, über die Anzahl der möglichen Ergebnisse.",
     "2018MgrundlegendBStochastikWTR3-2d"),
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
