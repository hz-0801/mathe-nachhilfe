# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 1.4 · 17.09.2026 · gilt mit katalog-prompt.md v0.5, abitur-vokabular.md v1.2 und iqb.md v1.7

Änderungen gegenüber 1.3 (Stapel 2022-ga-B, 17.09.2026): Die Eichschwelle darf
je Stapel in KONFIG überschrieben werden („eichung_mindestens" mit Pflichtfeld
„eichung_grund"); der Bericht nennt den abweichenden Wert und den Grund. Anlass:
19 der 52 Zeilen von 2022-ga-B tragen die Schätzung der wortgleichen
Landeszeilen 2022-bebb-gk (dort ohne Standardbezug geschätzt, hier unverändert
übernommen, damit die Dubletten nach dem Abgleichlauf geerbt bleiben); die 33
eigenen Schätzungen treffen 31, die 19 übernommenen 10. Die globale Schwelle
bleibt 85 %.

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
    "stapel": "2022-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2022MgrundlegendBAnalysisWTR1": 35, "2022MgrundlegendBAnalysisWTR2": 35, "2022MgrundlegendBAGLAA1WTR": 20,
        "2022MgrundlegendBAGLAA2WTR1": 20, "2022MgrundlegendBAGLAA2WTR2": 20,
        "2022MgrundlegendBStochastikWTR1": 20, "2022MgrundlegendBStochastikWTR2": 20,
    },
    # True: Probelauf – prüfen und berichten, nichts schreiben, Stapel darf
    # unvollständig sein. False: Stapel muss vollständig sein, dann schreiben.
    "probe": False,
    # Eichschwelle für diesen Stapel (v1.4, sonst SCHWELLEN): 19 der 52 Zeilen tragen
    # die Schätzung der wortgleichen Landeszeilen 2022-bebb-gk, dort ohne
    # Standardbezug geschätzt und hier unverändert übernommen (Dubletten bleiben nach
    # Lauf 18 geerbt); eigene Schätzungen 31 von 33, übernommene 10 von 19.
    "eichung_mindestens": 0.75,
    "eichung_grund": "19 Zeilen mit übernommener Schätzung der Landeszeilen 2022-bebb-gk (10 Treffer), eigene 31 von 33",
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
# Stapel 2022-ga-B (WTR-Zweig; Reserve, geöffnet 17.09.2026 wegen der 19
# Landesheftverweise von 2022-bebb-gk auf Analysis WTR 2, AG/LA (A2) WTR 2 und
# Stochastik WTR 1). Sieben Dateien, Standardbezug mit Spalte Anforderungs-
# bereich; Analysis-Dateien mit 35 BE. Die 19 vorgemerkten Zeilen sind aus den
# Landeszeilen erzeugt (gen_pool22.py: Typ und Felder von dort, Standardbezug
# und amtliches Ergebnis aus der Pooldatei), die übrigen 33 von Hand.
# ---- Analysis WTR 1: Aufgabe 1 (Graph fünften Grades, 23 BE), Aufgabe 2 (Übertopf, 12 BE)
A1 = "f(x) = 1/80 x⁵ − 1/6 x³ + x, definiert in IR; Abbildung 1 zeigt G_f; W(2 | f(2)) ist Wendepunkt"
A1_SK = ("Koordinatensystem auf Gitter, x von −2,5 bis 3,5, y von −1,5 bis 2,5: Graph G_f, punktsymmetrisch zum "
         "Ursprung, steigend mit Sattelpunkten bei (−2 | −16/15) und (2 | 16/15), Beschriftung Abb. 1")
row("2022MgrundlegendBAnalysisWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstelle null am Term ohne konstanten Summanden begründen", typ_neben="",
    stichwoerter="f(x) = x · (1/80 x⁴ − 1/6 x² + 1)|kein konstanter Summand: f(0) = 0|weitere Nullstellen am Graphen nicht vorhanden",
    voraussetzungen="Nullstelle als Funktionswert null|Ausklammern von x",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="Koordinatensystem", skizze=A1_SK, kontext="ohne", textumfang="kurz",
    gegeben=A1,
    gesucht="die Nullstelle von f mit Begründung am Term",
    verfahren="x ausklammern bzw. fehlenden konstanten Summanden nennen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="x = 0; f ist ein Polynom ohne konstanten Summanden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Nullstellen des Klammerterms suchen",
    bemerkung="Standardbezug: K1 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2022MgrundlegendBAnalysisWTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Weiteren Wendepunkt über die Punktsymmetrie ohne Rechnung begründen", typ_neben="",
    stichwoerter="nur ungerade Exponenten: G_f punktsymmetrisch zum Ursprung|Spiegelbild des Wendepunkts W(2 | f(2)) ist (−2 | f(−2))",
    voraussetzungen="Symmetriekriterium am Term|Punktspiegelung überträgt Wendepunkte",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=A1_SK, kontext="ohne", textumfang="kurz",
    gegeben=A1,
    gesucht="Begründung ohne Rechnung, dass (−2 | f(−2)) ebenfalls Wendepunkt ist",
    verfahren="Punktsymmetrie am Term ablesen, Wendepunkt spiegeln",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f enthält nur Potenzen mit ungeraden Exponenten, G_f ist punktsymmetrisch zum Ursprung; das Spiegelbild von W ist Wendepunkt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="mit f'' rechnen statt zu begründen",
    bemerkung="Standardbezug: K1 I, K2 I, K4 I, K6 I. AB amtlich: I. Amtlich. Erste Schätzung II; nach der engen Fassung eine begründete Beobachtung (Symmetrie am Term ablesbar) – I.")
row("2022MgrundlegendBAnalysisWTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung als Quadrat eines Produkts von Linearfaktoren nachweisen", typ_neben="",
    stichwoerter="f'(x) = 1/16 x⁴ − 1/2 x² + 1 = 1/16 (x⁴ − 8x² + 16)|= 1/16 (x² − 4)² = 1/16 ((x − 2)(x + 2))²",
    voraussetzungen="Potenzregel|binomische Formel|dritte binomische Formel",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=A1 + "; Behauptung f'(x) = 1/16 (x − 2)² (x + 2)²",
    gesucht="Nachweis der Ableitung in der faktorisierten Form",
    verfahren="Ableiten, 1/16 ausklammern, binomische Formeln",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 1/16 x⁴ − 1/2 x² + 1 = 1/16 (x² − 4)² = 1/16 ((x − 2)(x + 2))² (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="x⁴ − 8x² + 16 nicht als Quadrat erkennen; stattdessen die rechte Seite ausmultiplizieren ist gleichwertig",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erste Schätzung II; nach der engen Fassung eine einzelne Rechnung (Ableiten und Ausmultiplizieren der Vorgabe) – I.")
row("2022MgrundlegendBAnalysisWTR1", "d", innen="1", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Schnittpunkt zweier Tangenten nachweisen und Tangenten einzeichnen", typ_neben="",
    stichwoerter="f'(0) = 1, f(0) = 0: t₁(x) = x|f'(2) = 0, f(2) = 16/15: t₂(x) = 16/15|t₁(16/15) = 16/15 = t₂(16/15)|beide Geraden in Abbildung 1",
    voraussetzungen="Tangentengleichung aus Punkt und Ableitungswert|waagerechte Tangente im Sattelpunkt|Schnittpunkt zweier Geraden",
    format="Rechnung|Zeichnen", operator="Weisen Sie nach|Zeichnen Sie", antwort="Text|Grafik",
    material="Koordinatensystem", skizze=A1_SK, kontext="ohne", textumfang="kurz",
    gegeben=A1 + "; f'(x) = 1/16 (x − 2)² (x + 2)²; Tangente in O und Tangente in W",
    gesucht="Nachweis, dass sich die Tangenten in (16/15 | 16/15) schneiden; beide Tangenten in Abbildung 1",
    verfahren="Beide Tangentengleichungen aufstellen, Punkt einsetzen; zeichnen",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="2022MgrundlegendBAnalysisWTR1-1c",
    ergebnis="t₁: y = x, t₂: y = 16/15; beide enthalten (16/15 | 16/15) (amtlich)",
    zwischenergebnis="f(2) = 16/15", niveau_geschaetzt="II",
    fehlerquelle="f'(2) ≠ 0 rechnen; Tangente in W nicht als waagerecht erkennen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2022MgrundlegendBAnalysisWTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Näherungswert eines Integrals als Trapezfläche am Graphen begründen", typ_neben="",
    stichwoerter="Fläche unter G_f über [0; 2] ≈ Trapez unter den Tangenten t₁ und t₂|Trapez mit Höhe 16/15 (Abstand der y-Werte 0 und 16/15) und parallelen Seiten 2 (x-Achse bis x = 2) und 14/15 (auf y = 16/15 von 16/15 bis 2)|Term 1/2 · (2 + 14/15) · 16/15 ist die Trapezformel",
    voraussetzungen="Integral als Fläche unter dem Graphen|Trapezformel|Lage der Tangenten aus d",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=A1_SK, kontext="ohne", textumfang="kurz",
    gegeben=A1 + "; Tangenten t₁: y = x und t₂: y = 16/15 aus d; Term 1/2 · (2 + 14/15) · 16/15",
    gesucht="geometrische Begründung, dass Integral und Term annähernd übereinstimmen",
    verfahren="Fläche unter G_f über [0; 2] mit dem Trapez zwischen x-Achse, t₁, t₂ und x = 2 vergleichen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="2022MgrundlegendBAnalysisWTR1-1d",
    ergebnis="Der Integralwert stimmt näherungsweise mit dem Inhalt des Trapezes überein, dessen Höhe 16/15 beträgt und dessen parallele Seiten die Längen 2 und 14/15 haben (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Term nicht als Trapezformel erkennen; Höhe und Seiten vertauschen",
    bemerkung="Standardbezug: K1 II, K4 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (b) Trapez aus den Tangenten erst erkennen und dem Term zuordnen. Verwandt mit „Näherungswert eines Integrals als Dreiecksfläche am Graphen begründen“ (2025-ga-B) – Kandidat für eine Zusammenziehung.")
row("2022MgrundlegendBAnalysisWTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Prozentuale Abweichung eines Näherungswerts vom exakten Wert berechnen", typ_neben="",
    stichwoerter="∫₀² f(x) dx = [1/480 x⁶ − 1/24 x⁴ + 1/2 x²]₀² = 22/15|Näherung 1/2 · (2 + 14/15) · 16/15 = 352/225|(352/225 − 22/15)/(22/15) ≈ 6,7 %",
    voraussetzungen="Stammfunktion ganzrationaler Terme|Hauptsatz|relative Abweichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=A1 + "; Näherungswert 1/2 · (2 + 14/15) · 16/15 aus e",
    gesucht="prozentuale Abweichung des Näherungswerts vom exakten Integralwert",
    verfahren="Integral exakt berechnen, Differenz durch den exakten Wert teilen",
    schritte="3", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="2022MgrundlegendBAnalysisWTR1-1e",
    ergebnis="∫₀² f(x) dx = 22/15; Abweichung ≈ 7 % (genau 6,7 %) (amtlich)",
    zwischenergebnis="Stammfunktion 1/480 x⁶ − 1/24 x⁴ + 1/2 x²", niveau_geschaetzt="II",
    fehlerquelle="Abweichung auf den Näherungswert beziehen",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-B).")
row("2022MgrundlegendBAnalysisWTR1", "g", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Parameter einer Sinusfunktion aus Extremstelle und Funktionswert bestimmen", typ_neben="",
    stichwoerter="Extremstelle 2 als Viertelperiode: 2b = π/2 ⇔ b = π/4|g(2) = f(2) = 16/15 ⇔ a · sin(π/2) = a = 16/15",
    voraussetzungen="Extremstellen von a · sin(bx) bei bx = π/2|Funktionswert einsetzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=A1 + "; g(x) = a · sin(bx), a, b > 0, auf [−2; 2] Näherung von f; 2 ist Extremstelle von g; g(2) = f(2)",
    gesucht="die passenden Werte von a und b",
    verfahren="b aus der Lage des ersten Hochpunkts, a aus dem Funktionswert",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="b = π/4, a = 16/15 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Periode 2 statt Viertelperiode 2 ansetzen (b = π)",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Verwandt mit „Parameter einer Sinusfunktion aus zwei aufeinanderfolgenden Extrempunkten bestimmen“ (2022-ea-B), hier Extremstelle und Wert.")
A2T = "Übertopf, rotationssymmetrisch mit kreisförmiger Grundfläche und Höhe 40 cm; Profillinie des Mantels im Längsschnitt h(x) = 5 − 10/x², definiert in IR ohne 0, Rotationsachse ist die y-Achse; 1 LE = 10 cm (Abbildung 2)"
A2_SK = ("Koordinatensystem auf Gitter, x von −3 bis 3, y von 0 bis 4: Profil des Übertopfs – waagerechte Grundfläche auf der x-Achse von "
         "etwa −1,4 bis 1,4, Mantellinien h(x) beidseitig steil ansteigend von (±√2 | 0) bis zur Höhe 4 bei x ≈ ±3,2; Beschriftungen Mantel, Grundfläche, Abb. 2")
row("2022MgrundlegendBAnalysisWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Durchmesser der Grundfläche eines Rotationskörpers aus der Nullstelle der Profilfunktion mit Maßstab nachweisen", typ_neben="",
    stichwoerter="h(x) = 0 ⇔ 5 = 10/x² ⇔ x² = 2 ⇔ x = ±√2|Durchmesser 2√2 LE|2√2 · 10 cm ≈ 28 cm",
    voraussetzungen="Bruchgleichung|Nullstelle als Rand der Grundfläche|Maßstab",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=A2_SK, kontext="Übertopf/Pflanzgefäß", textumfang="mittel",
    gegeben=A2T,
    gesucht="Nachweis, dass die Grundfläche einen Durchmesser von etwa 28 cm hat",
    verfahren="Nullstellen von h, Abstand verdoppeln, mit 10 cm multiplizieren",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="cm", abhaengig_von="",
    ergebnis="h(x) = 0 ⇔ x = ±√2; 2 · √2 · 10 cm ≈ 28 cm (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Radius statt Durchmesser; Maßstab vergessen",
    bemerkung="Standardbezug: K2 I, K3 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2022MgrundlegendBAnalysisWTR1", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Passung eines Zylinders in ein Gefäß über die Höhe aus dem Volumen prüfen", typ_neben="",
    stichwoerter="Zylinder r = 12 cm, V = 16 000 cm³: h = 16 000/(π · 144) ≈ 35 cm|35 cm < 40 cm Höhe des Übertopfs|Radius 12 cm = 1,2 LE kleiner als der Grundflächenradius √2 LE ≈ 1,41: der Zylinder steht auf der Grundfläche, der Mantel weitet sich nach außen – passt",
    voraussetzungen="Zylindervolumen|Einheiten Liter und cm³|Vergleich mit Höhe und Öffnung",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=A2_SK, kontext="Übertopf/Pflanzgefäß", textumfang="mittel",
    gegeben=A2T + "; zylinderförmiger Pflanztopf mit Durchmesser 24 cm und Volumen 16 Liter",
    gesucht="ob der Pflanztopf in den Übertopf passt, ohne über den oberen Rand hinauszuragen",
    verfahren="Höhe des Zylinders aus dem Volumen, mit 40 cm vergleichen; Durchmesser gegen die Grundfläche",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="cm", abhaengig_von="2022MgrundlegendBAnalysisWTR1-2a",
    ergebnis="π · (12 cm)² · h = 16 000 cm³ liefert h ≈ 35 cm; mit Durchmesser 24 cm (kleiner als 28 cm) und Höhe etwa 35 cm passt der Pflanztopf hinein (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="16 Liter als 16 cm³ oder 1600 cm³ umrechnen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (h = 35,4 cm).")
row("2022MgrundlegendBAnalysisWTR1", "c", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für ein vorgegebenes Verhältnis zweier Radien einer Profilkurve berechnen", typ_neben="",
    stichwoerter="Grundfläche: h_k(x) = 0 ⇔ x = √(10/k)|oberer Rand (Höhe 4): h_k(x) = 4 ⇔ x = √(10/(k − 4))|√(10/(k − 4)) = 2 · √(10/k) ⇔ 10/(k − 4) = 40/k ⇔ 4(k − 4) = k ⇔ k = 16/3",
    voraussetzungen="Radien als positive Lösungen von h_k = 0 bzw. h_k = 4|Wurzelgleichung|Bruchgleichung mit Parameter",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=A2_SK, kontext="Übertopf/Pflanzgefäß", textumfang="mittel",
    gegeben="Übertöpfe der Höhe 40 cm mit Profil h_k(x) = k − 10/x², k > 4; Radius des oberen Rands doppelt so groß wie der Radius der Grundfläche",
    gesucht="der Wert von k",
    verfahren="Beide Radien als Terme in k, Bedingung als Gleichung, lösen",
    schritte="4", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="k = 16/3 (amtlich)",
    zwischenergebnis="Radien √(10/k) und √(10/(k − 4))",
    niveau_geschaetzt="III",
    fehlerquelle="oberen Rand bei y = 40 statt y = 4 (Maßstab) ansetzen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Radienverhältnis erst in eine Gleichung mit zwei Wurzeltermen übersetzen.")
# ---- Analysis WTR 2: Aufgabe 1 (f(x) = (x + 2) · e^(−x), 22 BE), Aufgabe 2 (Tauchroboter, 13 BE);
#      1 a, b, d und 2 a–d wortgleich mit 2022-bebb-gk 2.1 (aus den Landeszeilen erzeugt), 1 c, e, f von Hand
A3 = "f(x) = (x + 2) · e^(−x), definiert in IR, mit f'(x) = −(x + 1) · e^(−x)"
row("2022MgrundlegendBAnalysisWTR2", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Passende Abbildung des Graphen über einen Funktionswert auswählen", typ_neben="",
    stichwoerter="f(1) = 3/e ≈ 1,1|Abbildung I zeigt bei 1 keinen Wert nahe 1,1 (Graph steigt), Abbildung III liegt zu tief (f(0) = 2 stimmt nur in I und II)|Abbildung II",
    voraussetzungen="Funktionswert berechnen|Graphen an einem Wert unterscheiden",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm", skizze="Drei Abbildungen I, II, III mit Koordinatensystemen x von −2 bis 3, y von −1 bis 3: I Graph mit Hochpunkt bei etwa (−1 | 2,7), fallend bis etwa (1 | 1) und dann wieder steigend; II Graph mit Hochpunkt (−1 | e), durch (0 | 2), monoton fallend gegen die x-Achse; III wie II, aber flacher mit y-Achsenschnitt 1", kontext="ohne", textumfang="kurz",
    gegeben=A3 + "; Abbildungen I, II, III",
    gesucht="die Abbildung, die den Graphen von f zeigt, mit Begründung",
    verfahren="Einen Funktionswert (etwa f(0) = 2 oder f(1) ≈ 1,1) mit den Abbildungen vergleichen",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f(1) ≈ 1,1; dazu passt nur Abbildung II (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur f(0) = 2 prüfen (schließt III aus, nicht I)",
    bemerkung="Standardbezug: K1 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erste Schätzung II; nach der engen Fassung eine begründete Beobachtung (ein Funktionswert) – I. Im Landesheft 2022-bebb-gk 2.1 c durch eine Landesfassung ersetzt.")
row("2022MgrundlegendBAnalysisWTR2", "e", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Bild des Graphen unter Spiegelung, Streckung und Verschiebung als Ableitungsgraph nachweisen", typ_neben="",
    stichwoerter="Spiegelung an der x-Achse: −f(x); Streckung 1/e in y-Richtung: −1/e · f(x); Verschiebung um 1 nach rechts: g(x) = −1/e · f(x − 1)|g(x) = −1/e · (x + 1) · e^(−x + 1) = −(x + 1) · e^(−x) = f'(x)",
    voraussetzungen="Transformationen als Termänderungen|Potenzgesetz e^(−x + 1) = e · e^(−x)",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=A3 + "; Graph von g entsteht aus dem Graphen von f durch Spiegelung an der x-Achse, Streckung mit 1/e in y-Richtung und Verschiebung um 1 in positive x-Richtung",
    gesucht="Nachweis, dass g(x) = f'(x)",
    verfahren="Transformationen nacheinander in den Term übersetzen und vereinfachen",
    schritte="3", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="g(x) = −1/e · ((x − 1) + 2) · e^(−x + 1) = −1/e · (x + 1) · e^(−x) · e = −(x + 1) · e^(−x) = f'(x) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Verschiebung nach rechts als f(x + 1) ansetzen; Faktor e aus e^(−x + 1) vergessen",
    bemerkung="Standardbezug: K2 II, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Im Landesheft 2022-bebb-gk nicht enthalten (Landeszusätze d–f, h, i).")
row("2022MgrundlegendBAnalysisWTR2", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Integrationsgrenzen und Faktor für ein Integral über den transformierten Graphen bestimmen", typ_neben="",
    stichwoerter="f(x) = −e · g(x + 1)|∫₀² f(x) dx = −e · ∫₀² g(x + 1) dx = −e · ∫₁³ g(x) dx|Spiegelung liefert Faktor −1, Streckung Faktor e, Verschiebung verschobene Grenzen: a = 1, b = 3, k = −e",
    voraussetzungen="Umkehrung der Transformationen|Substitution der Verschiebung in den Grenzen|Streckfaktor vor dem Integral",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=A3 + "; g(x) = f'(x) entsteht aus f durch Spiegelung, Streckung mit 1/e und Verschiebung um 1; Gleichung ∫₀² f(x) dx = k · ∫ₐᵇ g(x) dx",
    gesucht="reelle Zahlen a, b und k",
    verfahren="Jede Transformation in Faktor oder Grenzverschiebung übersetzen",
    schritte="3", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="2022MgrundlegendBAnalysisWTR2-1e",
    ergebnis="a = 1, b = 3, k = −e (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Verschiebung nicht in die Grenzen übertragen; k = −1/e statt −e",
    bemerkung="Standardbezug: K1 III, K2 II, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) drei Transformationen in Faktor und Grenzen übersetzen, verkettet.")
# ---- AG/LA (A1) WTR: Transportunternehmen (20 BE)
TU = "Transportunternehmen mit 150 Fahrzeugen an den Standorten A, B, C; Verteilung (a; b; c) abends; Übergang v_(n+1) = M · v_n mit M = ((0,7; 0,5; 0,1), (0,2; 0,2; 0,6), (0,1; 0,3; 0,3))"
row("2022MgrundlegendBAGLAA1WTR", "a", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm zur Matrix auswählen und fehlende Werte angeben", typ_neben="",
    stichwoerter="Spalten von M sind die Abgänge je Standort: von B 0,5 nach A, 0,2 bleibt, 0,3 nach C|Diagramm II hat 0,3 von B nach C und 0,2 als Schleife an B|p = 0,5 (B → A), q = 0,6 (C → B)",
    voraussetzungen="Lesen einer Übergangsmatrix spaltenweise|Übergangsdiagramm",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text|Zahl",
    material="Diagramm", skizze="Zwei Übergangsdiagramme I und II mit den Knoten A, B, C, Schleifen 0,7 an A, 0,2 an B, 0,3 an C; I: Pfeile A→B 0,2, B→A p, A→C 0,1, C→A 0,1, B→C q, C→B 0,3; II: A→B 0,2, B→A p, A→C 0,1, C→A 0,1, B→C 0,3, C→B q", kontext="Transportunternehmen/Fahrzeugstandorte", textumfang="mittel",
    gegeben=TU + "; Diagramme I und II mit Platzhaltern p und q",
    gesucht="das passende Diagramm und die Werte von p und q",
    verfahren="Einträge von M mit den Pfeilen vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Diagramm II; p = 0,5, q = 0,6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen statt Spalten als Abgänge lesen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erste Schätzung II; nach der engen Fassung Ablesen ohne Verkettung – I.")
row("2022MgrundlegendBAGLAA1WTR", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Verteilung nach einem Übergang berechnen und einen Anteil angeben", typ_neben="",
    stichwoerter="a₁ = 0,7 · 20 + 0,5 · 60 + 0,1 · 70 = 51|51/150 = 34 %",
    voraussetzungen="Matrix-Vektor-Produkt (eine Zeile)|Anteil an der Gesamtzahl",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Transportunternehmen/Fahrzeugstandorte", textumfang="kurz",
    gegeben=TU + "; Sonntagabend 20 Fahrzeuge in A, 60 in B, 70 in C",
    gesucht="prozentualer Anteil der Fahrzeuge in A am Montagabend",
    verfahren="Erste Zeile von M mit dem Vektor multiplizieren, durch 150 teilen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="(0,7 · 20 + 0,5 · 60 + 0,1 · 70)/150 = 34 % (amtlich)",
    zwischenergebnis="51 Fahrzeuge", niveau_geschaetzt="I",
    fehlerquelle="Anzahl 51 statt Anteil abgeben",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ga-B).")
row("2022MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Komponentensumme eines Produkts mit der diagonalfreien Matrix als Wechslerzahl deuten", typ_neben="",
    stichwoerter="Matrix = M mit Nullen auf der Diagonale|Bleiber (0,7 · 20, 0,2 · 60, 0,3 · 70) entfallen|a₁ + b₁ + c₁ = Anzahl der Fahrzeuge, die im Laufe des Montags den Standort wechseln",
    voraussetzungen="Bedeutung der Diagonaleinträge (Verbleib)|Komponentensumme als Gesamtzahl",
    format="Begründung", operator="Deuten Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Transportunternehmen/Fahrzeugstandorte", textumfang="mittel",
    gegeben=TU + "; Gleichung ((0; 0,5; 0,1), (0,2; 0; 0,6), (0,1; 0,3; 0)) · (20; 60; 70) = (a₁; b₁; c₁)",
    gesucht="Deutung des Terms a₁ + b₁ + c₁ ohne Rechnung, mit Begründung",
    verfahren="Matrix als M ohne Diagonale erkennen, Diagonale als Verbleib deuten",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Anzahl der Fahrzeuge, die im Laufe des Montags den Standort wechseln; die Matrix entsteht aus M durch Nullsetzen der Diagonale, damit entfallen die Fahrzeuge, die den Standort nicht wechseln (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Term als Gesamtzahl aller Fahrzeuge deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Erste Schätzung III über (d); nach der engen Fassung nur eine Deutung (Diagonale = Verbleib), die Komponentensumme ist Routine – II.")
row("2022MgrundlegendBAGLAA1WTR", "d", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Fehlende Einträge einer Matrixpotenz über Zeile mal Spalte und Spaltensumme berechnen", typ_neben="",
    stichwoerter="r = 0,2 · 0,1 + 0,2 · 0,6 + 0,6 · 0,3 = 0,32|s = 1 − 0,4 − 0,32 = 0,28 (Spaltensumme 1) oder 0,1 · 0,1 + 0,3 · 0,6 + 0,3 · 0,3",
    voraussetzungen="Matrixmultiplikation|Spaltensummen einer stochastischen Matrix",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Transportunternehmen/Fahrzeugstandorte", textumfang="kurz",
    gegeben=TU + "; M² = ((0,6; 0,48; 0,4), (0,24; 0,32; r), (0,16; 0,2; s))",
    gesucht="die Werte von r und s",
    verfahren="Zeile 2 mal Spalte 3 von M; s über die Spaltensumme",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="r = 0,32, s = 0,28 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeile mit Zeile multiplizieren",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2022MgrundlegendBAGLAA1WTR", "e", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Aussagen über Anteile nach zwei Übergängen mit M² beurteilen", typ_neben="",
    stichwoerter="A₁: M² · (0; 150; 0) hat B-Komponente 0,32 · 150, also 32 %: richtig|A₂: Verteilung (a; b; 0): B-Komponente 0,24a + 0,32b ≥ 0,24(a + b) = 0,24 · 150: richtig",
    voraussetzungen="M² für zwei Schritte|Komponentenrechnung|Abschätzung mit unbekannten Anteilen",
    format="Begründung|Rechnung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Transportunternehmen/Fahrzeugstandorte", textumfang="lang",
    gegeben=TU + "; M² aus d; A₁: alle 150 in B am Dienstag ⇒ Donnerstag 32 % in B; A₂: keins in C am Dienstag ⇒ Donnerstag mindestens 24 % in B",
    gesucht="Beurteilung beider Aussagen",
    verfahren="A₁ mit der zweiten Zeile von M² nachrechnen; A₂ über 0,24a + 0,32b ≥ 0,24(a + b) begründen",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2022MgrundlegendBAGLAA1WTR-1d",
    ergebnis="Beide Aussagen sind richtig: 0,32 · 150 Fahrzeuge in B; für (a; b; 0) gilt 0,24a + 0,32b ≥ 0,24 · (a + b) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="A₂ nur an einem Zahlenbeispiel prüfen; M statt M² verwenden",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Schätzung III über (c); nach dem Prinzip ist 0,24a + 0,32b ≥ 0,24(a + b) eine Abschätzung mit mitgeführten Parametern, keine hergeleitete Beziehung – II.")
row("2022MgrundlegendBAGLAA1WTR", "f", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Term für die Verteilung mit zwischenzeitlichem Abgang über Diagonalmatrix und Matrixpotenzen angeben", typ_neben="",
    stichwoerter="Sonntag → Dienstagabend: M² · v|Mittwochmorgen: 10 % von B weg (Faktor 0,9 über Diagonalmatrix), 3 Fahrzeuge von A weg (Vektor (3; 0; 0))|Mittwoch → Freitagabend: M³|Term M³ · (((1; 0; 0), (0; 0,9; 0), (0; 0; 1)) · M² · v − (3; 0; 0))",
    voraussetzungen="Matrixpotenzen für mehrere Tage|Diagonalmatrix als anteilige Änderung|Reihenfolge der Operationen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Transportunternehmen/Fahrzeugstandorte", textumfang="lang",
    gegeben=TU + "; Mittwochmorgen verlassen 10 % der Fahrzeuge in B und drei Fahrzeuge in A die Standorte für die Woche; gesucht die Verteilung am Freitagabend aus der Verteilung v am Sonntagabend",
    gesucht="ein Term für die Verteilung am Freitagabend in Abhängigkeit von v",
    verfahren="Tage zählen (2 Übergänge bis Dienstag, 3 bis Freitag), Abgang als Diagonalmatrix und Vektor dazwischen",
    schritte="4", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="M³ · (((1; 0; 0), (0; 0,9; 0), (0; 0; 1)) · M² · v − (3; 0; 0)) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Anzahl der Übergänge falsch zählen; den Abgang vor M² setzen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 III, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Abgang und Zeitpunkte erst in Matrizenterme übersetzen.")
# ---- AG/LA (A2) WTR 1: Klettergarten (20 BE)
KW = "Kletterwand als ebenes Viereck mit A(6|7|4), B(10|5|5), C(9|5,5|8), D(5|7,5|7); x₁x₂-Ebene ist der Boden, 1 LE = 1 m"
SEIL = "Stahlseil zwischen zwei 8 m hohen Masten mit Fußpunkten F₁(0|0|0) und F₂(2,5|6|0), befestigt in 6 m bzw. 4,7 m Höhe, geradlinig"
row("2022MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen und Rechteck über das Skalarprodukt ausschließen", typ_neben="",
    stichwoerter="AB = (4; −2; 1) = DC: Parallelogramm|AB · AD = (4; −2; 1) · (−1; 0,5; 3) = −2 ≠ 0: kein rechter Winkel",
    voraussetzungen="Verbindungsvektoren|Parallelogrammkriterium|Skalarprodukt und rechter Winkel",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Klettergarten", textumfang="mittel",
    gegeben=KW,
    gesucht="Nachweis, dass die Wand ein Parallelogramm, aber kein Rechteck ist",
    verfahren="AB mit DC vergleichen, Skalarprodukt AB · AD",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="AB = DC = (4; −2; 1); AB · AD = −2 ≠ 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur die Parallelität einer Seite prüfen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Geschätzt II (zwei Nachweise), amtlich I; verwandt mit „Parallelogramm über gleiche Verbindungsvektoren nachweisen“ (2021-ea-A) und „Parallelogramm als Rechteck über das Skalarprodukt nachweisen“ (2026-ea-B).")
row("2022MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Vertikale Lage einer Fläche über einen Normalenvektor mit x₃-Komponente null nachweisen", typ_neben="",
    stichwoerter="Normalenvektor n von ABD: AB · n = 0 und AD · n = 0|I 4n₁ − 2n₂ + n₃ = 0, II −n₁ + 0,5n₂ + 3n₃ = 0 ⇒ n₃ = 0|n steht senkrecht auf (0; 0; 1): Wand vertikal",
    voraussetzungen="Normalenvektor aus zwei Spannvektoren|vertikal heißt parallel zur x₃-Richtung|Gleichungssystem",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Klettergarten", textumfang="mittel",
    gegeben=KW,
    gesucht="Nachweis, dass die Wand vertikal ausgerichtet ist",
    verfahren="Normalenvektor der Wandebene bestimmen, dritte Komponente null zeigen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="Aus AB · n = 0 und AD · n = 0 folgt n₃ = 0; der Normalenvektor steht senkrecht zum Normalenvektor der x₁x₂-Ebene, die Wand ist vertikal (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="vertikal mit „Normalenvektor (0; 0; 1)“ verwechseln",
    bemerkung="Standardbezug: K2 I, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Kreuzprodukt (−6,5; −13; 0)).")
row("2022MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Größeren Teil einer Wand über die Lage der Diagonalen begründen", typ_neben="",
    stichwoerter="Diagonale DB halbiert das Parallelogramm|D liegt höher als B (x₃ 7 gegen 5): die horizontale Linie durch D verläuft oberhalb von DB|der untere Teil enthält die untere Hälfte ganz und mehr",
    voraussetzungen="Diagonale halbiert ein Parallelogramm|horizontal heißt gleiche x₃-Koordinate",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Klettergarten", textumfang="mittel",
    gegeben=KW + "; horizontale Linie auf der Wand durch D teilt sie in zwei Teile",
    gesucht="Begründung, dass der untere Teil den größeren Flächeninhalt hat",
    verfahren="Mit der Diagonale DB vergleichen, die die Wand halbiert",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die gerade Linie DB teilt die Wand in zwei gleich große Teile; da D höher liegt als B, verläuft die horizontale Linie oberhalb von DB, der untere Teil ist größer (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Teilflächen berechnen wollen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich. Eichregel: (b) Diagonale als halbierende Hilfslinie erst finden – geschätzt III, amtlich II.")
row("2022MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Körper in ein räumliches Koordinatensystem einzeichnen", typ_neben="",
    stichwoerter="Masten als senkrechte Strecken über F₁ und F₂ bis Höhe 8|Seil als Strecke von (0; 0; 6) nach (2,5; 6; 4,7)",
    voraussetzungen="Schrägbild mit x₁ nach vorn|Punkte mit drei Koordinaten eintragen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="Koordinatensystem", skizze="Leeres dreidimensionales Koordinatensystem auf Gitter (Schrägbild, x₁ nach vorn links, x₂ nach rechts, x₃ nach oben) zum Eintragen", kontext="Klettergarten", textumfang="mittel",
    gegeben=SEIL,
    gesucht="Darstellung der Masten und des Seils im Koordinatensystem",
    verfahren="Fußpunkte, Mastspitzen und Befestigungspunkte eintragen und verbinden",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Zeichnung: zwei senkrechte Masten der Höhe 8 über F₁ und F₂, Seil von (0 | 0 | 6) nach (2,5 | 6 | 4,7) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="F₂ mit x₁ = 2,5 und x₂ = 6 vertauschen",
    bemerkung="Standardbezug: K4 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2017-bb-ea).")
row("2022MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Neigung einer Strecke in Prozent aus Höhendifferenz und Horizontalabstand berechnen", typ_neben="",
    stichwoerter="Horizontalabstand |F₁F₂| = |(2,5; 6; 0)| = 6,5|Höhendifferenz 6 − 4,7 = 1,3|Neigung 1,3/6,5 = 20 %",
    voraussetzungen="Betrag eines Vektors|Neigung als Quotient aus Höhe und Grundseite",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Klettergarten", textumfang="kurz",
    gegeben=SEIL,
    gesucht="Neigung des Seils in Prozent",
    verfahren="Abstand der Fußpunkte, Höhenunterschied, Quotient",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="m", abhaengig_von="",
    ergebnis="|F₁F₂| = 6,5; (6 − 4,7)/6,5 = 20 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Seillänge statt Horizontalabstand als Bezug",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2022MgrundlegendBAGLAA2WTR1", "f", innen="1", seite="2", punkte="5", afb_amtlich="I|II|III",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Höhenunterschied zweier übereinanderliegender Punkte auf Seilgeraden bestimmen", typ_neben="",
    stichwoerter="unteres Seil: x = (0; 0; 6) + s · (2,5; 6; −1,3)|oberes Seil h waagerecht in Höhe 8 mit x₂ = 3|gleiche x₂-Koordinate: 6s = 3 ⇔ s = 0,5, Höhe 6 − 0,65 = 5,35|Abstand 8 − 5,35 = 2,65 m",
    voraussetzungen="Geradengleichung aus zwei Punkten|„vertikal über“ heißt gleiche x₁- und x₂-Koordinaten|Parameter aus einer Koordinate",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Klettergarten", textumfang="mittel",
    gegeben=SEIL + "; oberes Seil entlang h: x = (−1; 3; 8) + t · (5; 0; 0); ein Punkt des oberen Seils liegt vertikal über einem Punkt des unteren",
    gesucht="Abstand dieser beiden Punkte",
    verfahren="Untere Seilgerade aufstellen, Punkt mit x₂ = 3 bestimmen, Höhendifferenz",
    schritte="4", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="Unterer Punkt in Höhe 5,35 m (s = 0,5), oberes Seil in 8 m: Abstand 2,65 m (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Abstand der Geraden (windschief) berechnen statt des vertikalen Abstands",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K4 II, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „vertikal übereinander“ erst als gleiche x₂-Koordinate übersetzen, verkettet mit der Geradengleichung.")
# ---- AG/LA (A2) WTR 2: Kirchturmdach (20 BE); a–d, f wortgleich mit 2022-bebb-gk 3 b, d, e, f, i, e abgewandelt (3 g) – alle aus den Landeszeilen erzeugt
# ---- Stochastik WTR 1: Paketzentrum (20 BE); a, b, c, e, f wortgleich mit 2022-bebb-gk 4 b, c, e, h, i, g abgewandelt (4 j) – aus den Landeszeilen erzeugt; d von Hand
row("2022MgrundlegendBStochastikWTR1", "d", innen="1", seite="1", punkte="2", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Produkt aus Potenz und kumulierter Binomialsumme als Ereignis beschreiben", typ_neben="",
    stichwoerter="0,9¹⁴: die ersten 14 Pakete haben nicht das Ziel A|Σ (6 über i) 0,1ⁱ 0,9⁶⁻ⁱ für i = 0 bis 3: von den weiteren 6 höchstens 3 mit Ziel A, also mindestens 3 nicht|Ereignis: von 20 Paketen haben die ersten 14 und von den weiteren 6 mindestens 3 nicht das Ziel A",
    voraussetzungen="Potenz als feste Folge|kumulierte Binomialsumme als „höchstens“|Unabhängigkeit der Abschnitte",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Paketzentrum", textumfang="mittel",
    gegeben="Paketzentrum: 10 % der Pakete haben das Ziel A; 20 Pakete zufällig ausgewählt; Term 0,9¹⁴ · Σ_{i=0}^{3} (6 über i) · 0,1ⁱ · 0,9⁶⁻ⁱ",
    gesucht="ein passendes Ereignis",
    verfahren="Faktoren als Abschnitte der 20 Pakete deuten",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Von den 20 ausgewählten Paketen haben die ersten 14 und von den weiteren 6 mindestens 3 nicht das Ziel A (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Summe als „höchstens 3 mit Ziel A unter allen 20“ deuten",
    bemerkung="Standardbezug: K1 III, K3 II, K4 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (d) zwei Deutungen verkettet (Potenz als Anfangsstück, Summe als kumulierte Wahrscheinlichkeit). Im Landesheft 2022-bebb-gk durch Landeszusätze ersetzt.")
# ---- Stochastik WTR 2: Krankheit (Aufgabe 1, 8 BE), Studien (Aufgabe 2, 5 BE), Risikogruppen (Aufgabe 3, 7 BE)
KR = "Krankheit durch Bakterien: ein Drittel aller Menschen infiziert sich im Laufe des Lebens, bei 8 % der Infizierten bricht die Krankheit aus"
row("2022MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="I: infiziert 1/3, nicht infiziert 2/3|K: Krankheit bricht aus 0,08 unter I, 0,92 nicht|unter nicht Infizierten bricht sie nie aus (1)",
    voraussetzungen="Stufen und Äste eines Baumdiagramms|Beschriftung mit Ereignissen und Wahrscheinlichkeiten",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Krankheit/Infektion", textumfang="mittel",
    gegeben=KR,
    gesucht="beschriftetes Baumdiagramm",
    verfahren="Zwei Stufen I/¬I und K/¬K mit den Anteilen",
    schritte="1", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Baumdiagramm: I 1/3 mit K 0,08 und ¬K 0,92; ¬I 2/3 mit ¬K 1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="8 % auf alle Menschen statt auf die Infizierten beziehen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2025-ga-A).")
row("2022MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil über die totale Wahrscheinlichkeit aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(¬K) = 1/3 · 0,92 + 2/3 · 1 ≈ 97,3 %",
    voraussetzungen="Pfadmultiplikation und Pfadaddition",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Krankheit/Infektion", textumfang="kurz",
    gegeben=KR,
    gesucht="Anteil der Menschen, bei denen die Krankheit nicht ausbricht",
    verfahren="Beide Pfade zu ¬K addieren",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="2022MgrundlegendBStochastikWTR2-1a",
    ergebnis="1/3 · 0,92 + 2/3 ≈ 97,3 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur 1/3 · 0,92 rechnen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2022MgrundlegendBStochastikWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(I | ¬K) = (1/3 · 0,92)/(1/3 · 0,92 + 2/3) ≈ 31,5 %",
    voraussetzungen="Bedingte Wahrscheinlichkeit als Quotient|totale Wahrscheinlichkeit im Nenner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Krankheit/Infektion", textumfang="kurz",
    gegeben=KR + "; bei einem Menschen bricht die Krankheit nicht aus",
    gesucht="Wahrscheinlichkeit, dass er sich infiziert hat",
    verfahren="Pfad I∧¬K durch P(¬K) teilen",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="2022MgrundlegendBStochastikWTR2-1b",
    ergebnis="≈ 31,5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Bedingung umkehren (P(¬K | I) = 0,92)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ea-B).")
row("2022MgrundlegendBStochastikWTR2", "a", innen="2", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Stichprobenumfang aus dem Erwartungswert berechnen und Einzelwahrscheinlichkeit ermitteln", typ_neben="",
    stichwoerter="n · 1/3 = 200 ⇔ n = 600|P(X = 200) für n = 600, p = 1/3: ≈ 3,5 %",
    voraussetzungen="Erwartungswert n · p|Einzelwahrscheinlichkeit mit dem Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Krankheit/Studie", textumfang="mittel",
    gegeben="Anzahl der Infizierten unter den Teilnehmenden binomialverteilt mit p = 1/3; Erwartungswert 200",
    gesucht="Anzahl der Teilnehmenden; Wahrscheinlichkeit für genau 200 Infizierte",
    verfahren="n aus n · p = 200, dann Binomialwahrscheinlichkeit",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="n = 600; P(X = 200) ≈ 3,5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="kumulierte statt Einzelwahrscheinlichkeit",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Verwandt mit „Einzelwahrscheinlichkeit einer Binomialverteilung aus n und Erwartungswert berechnen“ (2020-ga-A), hier n aus dem Erwartungswert.")
row("2022MgrundlegendBStochastikWTR2", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Stichprobenumfang zu einer vorgegebenen Einzelwahrscheinlichkeit mit dem Rechner suchen", typ_neben="",
    stichwoerter="P(X = 30) = 3,6 % bei p = 1/3|systematisches Probieren mit n: n = 109 liefert ≈ 3,6 % (n = 110: 3,3 %, n = 105: 5,0 %)|eine mögliche Anzahl 109 (Werte weit weg vom Erwartungswert 3n möglich)",
    voraussetzungen="Einzelwahrscheinlichkeit mit Parameter n|systematisches Probieren am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Krankheit/Studie", textumfang="kurz",
    gegeben="zweite Studie, Anzahl der Infizierten binomialverteilt mit p = 1/3; P(X = 30) ≈ 3,6 %",
    gesucht="eine mögliche Anzahl der Teilnehmenden",
    verfahren="n variieren, bis P(X = 30) ≈ 0,036",
    schritte="3", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="n = 109 als eine mögliche Anzahl (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="n = 90 aus 30/p ansetzen und nicht prüfen",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (109: 3,63 %).")
RG = "Wahrscheinlichkeitsverteilungen für die Anzahl der Erkrankten unter je 1000 Infizierten in drei Risikogruppen A, B, C (Abbildung)"
RG_SK = ("Säulendiagramm, x von 0 bis 150, y von 0 bis 0,05: drei glockenförmige Verteilungen – A schmal um 50 (Maximum ≈ 0,057), B um 80 "
         "(≈ 0,046), C breit um 120 (≈ 0,039); Beschriftungen A, B, C")
row("2022MgrundlegendBStochastikWTR2", "a", innen="3", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussagen über Verteilungen verschiedener Gruppen am Säulendiagramm beurteilen", typ_neben="",
    stichwoerter="I: Säulen von B und C bei 99 etwa gleich hoch (≈ 0,01): richtig|II: Erwartungswert für C (≈ 120) ist größer als für A und B – die Wahrscheinlichkeit auszubrechen ist für C größer, nicht geringer: falsch",
    voraussetzungen="Säulenhöhe als Wahrscheinlichkeit|Lage des Maximums als Erwartungswert n · p",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Diagramm", skizze=RG_SK, kontext="Krankheit/Risikogruppen", textumfang="lang",
    gegeben=RG + "; Aussage I: für B und C sind die Wahrscheinlichkeiten für genau 99 Erkrankte etwa gleich; Aussage II: die Ausbruchswahrscheinlichkeit ist für C geringer als für A und B",
    gesucht="Beurteilung beider Aussagen",
    verfahren="Säulenhöhen bei 99 vergleichen; Lage der Verteilungen mit p verknüpfen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="I richtig (Säulen für 99 bei B und C etwa gleich hoch); II falsch (der Erwartungswert ist für C am größten, also auch p) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Breite der Verteilung als kleinere Wahrscheinlichkeit deuten",
    bemerkung="Standardbezug: K1 II, K3 I, K4 I. AB amtlich: II. Amtlich.")
row("2022MgrundlegendBStochastikWTR2", "b", innen="3", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Monotonie der Varianz einer Binomialverteilung in p über die Parabel begründen", typ_neben="",
    stichwoerter="Var = 1000 · p · (1 − p)|Graph in p: nach unten geöffnete Parabel mit Nullstellen 0 und 1, Scheitel bei p = 0,5|für 0 < p < 0,5 wächst der Term mit p: Behauptung richtig",
    voraussetzungen="Varianzformel n · p · (1 − p)|Parabel und Scheitel|Monotonie links vom Scheitel",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Krankheit/Risikogruppen", textumfang="mittel",
    gegeben="Behauptung: für binomialverteilte Zufallsgrößen mit n = 1000 und 0 < p < 0,5 nimmt die Varianz mit steigendem p zu",
    gesucht="Beurteilung der Behauptung",
    verfahren="Varianz als Funktion von p betrachten, Parabelform und Scheitel nutzen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Richtig: 1000 · p · (1 − p) ist eine nach unten geöffnete Parabel mit Nullstellen 0 und 1 und Hochpunkt bei p = 0,5, für 0 < p < 0,5 also steigend (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur zwei Zahlenbeispiele vergleichen",
    bemerkung="Standardbezug: K1 III, K2 III, K6 III. AB amtlich: III. Amtlich. Eichregel: (c) allgemeiner Nachweis über die Parabel in p.")
# ---- aus den Landeszeilen erzeugt (gen_pool22.py)
row("2022MgrundlegendBAnalysisWTR2", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Achsenschnittpunkte angeben und Hochpunkt aus der gegebenen Ableitung begründen",
    typ_neben="",
    stichwoerter="Schnittpunkte (−2 | 0) und (0 | 2)|f'(x) = 0 ⇔ x = −1, f' > 0 für x < −1 und f' < 0 für x > −1|Hochpunkt (−1 | e)",
    voraussetzungen="Nullstelle des linearen Faktors|Vorzeichenwechsel der gegebenen Ableitung|Funktionswert",
    format="Kurzantwort|Begründung",
    operator="Geben Sie an|Begründen Sie",
    antwort="Zahl|Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = (x + 2) · e^(−x), definiert in IR, mit f'(x) = −(x + 1) · e^(−x)",
    gesucht="Schnittpunkte des Graphen mit den Koordinatenachsen; Begründung, dass der Graph einen Hochpunkt hat, und dessen Koordinaten",
    verfahren="x + 2 = 0 und f(0); Nullstelle von f' mit Vorzeichenwechsel von + nach −, f(−1)",
    schritte="3",
    zahlenraum="ganz|negativ|Potenz",
    einheiten="",
    ergebnis="(−2 | 0), (0 | 2); f'(x) = 0 ⇔ x = −1 mit Vorzeichenwechsel von + nach −, Hochpunkt (−1 | e) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Hochpunkt ohne Vorzeichenwechsel oder zweite Ableitung begründen",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B2.1a (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAnalysisWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben",
    typ_neben="",
    stichwoerter="lim f(x) = 0 für x → +∞|Graph nähert sich der x-Achse von oben (asymptotisch)",
    voraussetzungen="e-Funktion dominiert das Polynom",
    format="Kurzantwort",
    operator="Geben Sie an|Beschreiben Sie",
    antwort="Zahl|Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = (x + 2) · e^(−x), definiert in IR, mit f'(x) = −(x + 1) · e^(−x)",
    gesucht="Grenzwert von f für x → +∞; Verlauf des Graphen dort",
    verfahren="e^(−x) fällt schneller als x + 2 wächst",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="Grenzwert 0; der Graph nähert sich der x-Achse asymptotisch von oben (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Grenzwert ∞ wegen des Faktors x + 2",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B2.1b (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAnalysisWTR2", "d", innen="1", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Umfang des Achsendreiecks einer Tangente berechnen und Umkreismittelpunkt angeben",
    typ_neben="",
    stichwoerter="f(0) = 2, f'(0) = −1, t: y = −x + 2|Achsenschnittpunkte (2 | 0), (0 | 2)|Umfang 2 + 2 + 2√2 = 4 + 2√2 ≈ 6,83|Punkt mit gleichem Abstand zu allen Ecken: Mittelpunkt der Hypotenuse (1 | 1)",
    voraussetzungen="Tangentengleichung|Achsenschnittpunkte|Pythagoras|Umkreismittelpunkt eines rechtwinkligen Dreiecks",
    format="Rechnung|Kurzantwort",
    operator="Berechnen Sie|Geben Sie an",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="mittel",
    gegeben="f(x) = (x + 2) · e^(−x), definiert in IR, mit f'(x) = −(x + 1) · e^(−x); Tangente im Punkt (0 | f(0)) bildet mit den Achsen ein Dreieck",
    gesucht="Umfang dieses Dreiecks; Punkt mit gleichem Abstand zu allen Eckpunkten",
    verfahren="Tangente aufstellen, Achsenschnitte, Umfang; Thales: Hypotenusenmitte",
    schritte="4",
    zahlenraum="ganz|Wurzel",
    einheiten="",
    ergebnis="Umfang 4 + √8 = 4 + 2√2 ≈ 6,83; Punkt (1 | 1) (amtlich)",
    zwischenergebnis="t: y = −x + 2",
    niveau_geschaetzt="III",
    fehlerquelle="Schwerpunkt statt Umkreismittelpunkt angeben",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B2.1g (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAnalysisWTR2", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Maximum eines Bestands an vorgegebener Stelle im Sachzusammenhang nachweisen",
    typ_neben="",
    stichwoerter="h'(t) = 27/40 t² − 27t + 405/2, h'(10) = 0|h''(10) = −13,5 < 0 (oder Abbildung)|h(10) = 900",
    voraussetzungen="Ableitung|hinreichende Bedingung|Funktionswert",
    format="Rechnung",
    operator="Weisen Sie nach",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze="Koordinatensystem t von 0 bis 30, h(t) von 0 bis 1000: Graph steigt vom Ursprung zum Hochpunkt (10 | 900) und fällt dann bis (30 | 0), mit Wendepunkt um t = 20.",
    kontext="Tauchroboter",
    textumfang="mittel",
    gegeben="Tauchroboter, vertikale Bewegung für 0 ≤ t ≤ 30 mit h(t) = 9/40 t³ − 27/2 t² + 405/2 t, t Zeit in Minuten, h(t) Abstand von der Wasseroberfläche in Metern; Abbildung des Graphen",
    gesucht="Nachweis, dass der Roboter nach 10 Minuten den größten Abstand hat und dieser 900 m beträgt",
    verfahren="h'(10) = 0, Maximum über h'' oder die Abbildung, h(10)",
    schritte="3",
    zahlenraum="Bruch|ganz",
    einheiten="m|min",
    ergebnis="h'(10) = 0, in Verbindung mit der Abbildung Maximum bei 10; h(10) = 900 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="nur h(10) = 900 zeigen, ohne das Maximum zu begründen",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B2.1j (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAnalysisWTR2", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Zurückgelegten Weg aus Hin- und Rückbewegung über Funktionswerte berechnen",
    typ_neben="",
    stichwoerter="Abstieg 0 bis 10 Minuten: 900 m|Aufstieg 10 bis 15: 900 − h(15) = 900 − 759,4 = 140,6 m|Weg ≈ 1041 m",
    voraussetzungen="Weg als Summe der Beträge der Höhenänderungen|Funktionswert h(15)",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze="Koordinatensystem t von 0 bis 30, h(t) von 0 bis 1000: Graph steigt vom Ursprung zum Hochpunkt (10 | 900) und fällt dann bis (30 | 0), mit Wendepunkt um t = 20.",
    kontext="Tauchroboter",
    textumfang="kurz",
    gegeben="Tauchroboter, vertikale Bewegung für 0 ≤ t ≤ 30 mit h(t) = 9/40 t³ − 27/2 t² + 405/2 t, t Zeit in Minuten, h(t) Abstand von der Wasseroberfläche in Metern; Abbildung des Graphen; Maximum 900 m bei t = 10",
    gesucht="zurückgelegter Weg in den ersten 15 Minuten",
    verfahren="900 + (900 − h(15))",
    schritte="2",
    zahlenraum="dezimal",
    einheiten="m",
    ergebnis="900 + 900 − h(15) ≈ 1040 m (genau 1040,6) (amtlich)",
    zwischenergebnis="h(15) = 759,375",
    niveau_geschaetzt="III",
    fehlerquelle="h(15) als Weg nehmen",
    abhaengig_von="2022MgrundlegendBAnalysisWTR2-2a",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B2.1k (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAnalysisWTR2", "c", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten",
    typ_neben="",
    stichwoerter="Wendestelle t = 20 im fallenden Bereich|Zeitpunkt der größten Geschwindigkeit beim Aufstieg",
    voraussetzungen="Wendepunkt als Extremum der Änderungsrate",
    format="Kurzantwort",
    operator="Beschreiben Sie",
    antwort="Text",
    material="Koordinatensystem",
    skizze="Koordinatensystem t von 0 bis 30, h(t) von 0 bis 1000: Graph steigt vom Ursprung zum Hochpunkt (10 | 900) und fällt dann bis (30 | 0), mit Wendepunkt um t = 20.",
    kontext="Tauchroboter",
    textumfang="kurz",
    gegeben="Tauchroboter, vertikale Bewegung für 0 ≤ t ≤ 30 mit h(t) = 9/40 t³ − 27/2 t² + 405/2 t, t Zeit in Minuten, h(t) Abstand von der Wasseroberfläche in Metern; Abbildung des Graphen",
    gesucht="Bedeutung des Wendepunkts für die Bewegung",
    verfahren="Wendepunkt bei t = 20 deuten",
    schritte="1",
    zahlenraum="ganz",
    einheiten="min",
    ergebnis="Die t-Koordinate des Wendepunkts gibt den Zeitpunkt an, zu dem der Roboter während des Aufsteigens die größte Geschwindigkeit hat (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Wendepunkt als Richtungswechsel deuten",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B2.1l (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAnalysisWTR2", "d", innen="2", seite="2", punkte="5", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Länge des Zeitraums mit Mindeständerungsrate über die Lösungen von f'(x) = c berechnen",
    typ_neben="",
    stichwoerter="Abstiegsphase 0 ≤ t ≤ 10|h'(t) ≥ 29,7 ⇔ t² − 40t + 256 ≥ 0|Lösungen 8 und 32|Zeitraum von 0 bis 8 Minuten",
    voraussetzungen="Geschwindigkeit als Ableitung|quadratische Ungleichung|Phase eingrenzen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze="Koordinatensystem t von 0 bis 30, h(t) von 0 bis 1000: Graph steigt vom Ursprung zum Hochpunkt (10 | 900) und fällt dann bis (30 | 0), mit Wendepunkt um t = 20.",
    kontext="Tauchroboter",
    textumfang="mittel",
    gegeben="Tauchroboter, vertikale Bewegung für 0 ≤ t ≤ 30 mit h(t) = 9/40 t³ − 27/2 t² + 405/2 t, t Zeit in Minuten, h(t) Abstand von der Wasseroberfläche in Metern; Abbildung des Graphen; Phase des zunehmenden Abstands (0 bis 10 Minuten)",
    gesucht="Zeitraum in dieser Phase, in dem die Geschwindigkeit mindestens 29,7 m/min beträgt",
    verfahren="h'(t) = 29,7 lösen, Lösung in der Phase auswählen",
    schritte="3",
    zahlenraum="dezimal|ganz",
    einheiten="m/min|min",
    ergebnis="h'(t) = 29,7 ⇔ t² − 40t + 256 = 0 ⇔ t = 8 oder t = 32; mit der Abbildung: der Zeitraum dauert von Beobachtungsbeginn bis 8 Minuten danach (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="t = 32 nicht ausschließen",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K4 I, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Abgewandelte Fassung im Landesheft 2022-bebb-gk 2.1 m: dort „mindestens 29,7“ (Randpunkt eingeschlossen), hier „größer als 29,7“. Landesheft 2022-bebb-gk B2.1m (abgewandelt, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ aus der Landeszeile, Felder auf die Poolfassung angepasst.")
row("2022MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Parametergleichung einer Ebene aus Punkten angeben",
    typ_neben="Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen",
    stichwoerter="L: x = (8; 8; 0) + s · (−4; 0; 6) + t · (0; −4; 6)|S = C + 1 · CG + 1 · CF|S liegt in L",
    voraussetzungen="Parameterform aus drei Punkten|Gleichungssystem für s und t",
    format="Kurzantwort|Rechnung",
    operator="Geben Sie an|Zeigen Sie",
    antwort="Term|Text",
    material="Körper",
    skizze="Schrägbild des Dachs im Koordinatensystem: Quadrat ABCD in der xy-Ebene, darüber die Giebelspitzen E, F, G, H über den Kantenmitten in Höhe 6 und die Spitze S über der Mitte in Höhe 12; graue Giebeldreiecke, Kanten von S zu E, F, G, H; Beschriftungen A bis H, S, Achsen x, y, z.",
    kontext="Kirchturm/Dach",
    textumfang="kurz",
    gegeben="Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m; Ebene L durch C, G und F",
    gesucht="Parametergleichung von L; Nachweis, dass S in L liegt",
    verfahren="Richtungsvektoren CG und CF; OS = OC + s · CG + t · CF lösen",
    schritte="3",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="L: x = (8; 8; 0) + s · (−4; 0; 6) + t · (0; −4; 6); s = t = 1 liefert S (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="dritte Koordinate beim Nachweis nicht prüfen",
    abhaengig_von="",
    bemerkung="Standardbezug: K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B3b (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Raute über vier gleich lange Seiten nachweisen",
    typ_neben="",
    stichwoerter="|CG| = |CF| = |GS| = |FS| = √52|alle vier Seiten gleich lang: Raute",
    voraussetzungen="Beträge von Verbindungsvektoren|Raute als Viereck mit vier gleichen Seiten (Parallelität folgt)",
    format="Rechnung",
    operator="Weisen Sie nach",
    antwort="Text",
    material="Körper",
    skizze="Schrägbild des Dachs im Koordinatensystem: Quadrat ABCD in der xy-Ebene, darüber die Giebelspitzen E, F, G, H über den Kantenmitten in Höhe 6 und die Spitze S über der Mitte in Höhe 12; graue Giebeldreiecke, Kanten von S zu E, F, G, H; Beschriftungen A bis H, S, Achsen x, y, z.",
    kontext="Kirchturm/Dach",
    textumfang="kurz",
    gegeben="Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m",
    gesucht="Nachweis, dass CGSF eine Raute ist",
    verfahren="Vier Seitenlängen berechnen (oder CG = FS und CF = GS mit gleichen Längen)",
    schritte="2",
    zahlenraum="Wurzel",
    einheiten="m",
    ergebnis="Alle vier Seiten haben die Länge √52, CG = FS und CF = GS: Raute (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="nur zwei Seiten vergleichen",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B3d (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen",
    typ_neben="",
    stichwoerter="M1: x = 8 enthält die Seite BC, M3: z = 6 ist waagerecht|M2: x − y = 0 ist die Symmetrieebene: enthält die z-Achse, S und die Diagonale AC, steht senkrecht auf der Grundfläche",
    voraussetzungen="Symmetrie des Dachs erkennen|Lage einer Ebene aus der Koordinatengleichung",
    format="Kurzantwort|Begründung",
    operator="Geben Sie an|Beschreiben Sie",
    antwort="Term|Text",
    material="Körper",
    skizze="Schrägbild des Dachs im Koordinatensystem: Quadrat ABCD in der xy-Ebene, darüber die Giebelspitzen E, F, G, H über den Kantenmitten in Höhe 6 und die Spitze S über der Mitte in Höhe 12; graue Giebeldreiecke, Kanten von S zu E, F, G, H; Beschriftungen A bis H, S, Achsen x, y, z.",
    kontext="Kirchturm/Dach",
    textumfang="kurz",
    gegeben="Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m; Ebenen M1: x = 8, M2: x − y = 0, M3: z = 6; eine ist Symmetrieebene des Dachs",
    gesucht="diese Ebene mit Beschreibung ihrer Lage",
    verfahren="M2 enthält die Diagonale AC und die Spitze S",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="M₂ ist die Symmetrieebene; sie verläuft durch A, C und S (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="M3 wählen (waagerechte Ebene durch die Giebelspitzen ist keine Symmetrieebene)",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B3e (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="2", punkte="6", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Innenwinkel einer Raute und Gesamtfläche der Dachflächen berechnen",
    typ_neben="",
    stichwoerter="SG = (0; 4; −6), SF = (4; 0; −6), cos φ = 36/52|φ ≈ 46,2°|Rautenfläche = |SG × SF| = √1408 ≈ 37,5|vier Dachflächen ≈ 150,1 m²",
    voraussetzungen="Winkel über das Skalarprodukt|Flächeninhalt eines Parallelogramms (Kreuzprodukt oder Diagonalen)|Vervierfachen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild des Dachs im Koordinatensystem: Quadrat ABCD in der xy-Ebene, darüber die Giebelspitzen E, F, G, H über den Kantenmitten in Höhe 6 und die Spitze S über der Mitte in Höhe 12; graue Giebeldreiecke, Kanten von S zu E, F, G, H; Beschriftungen A bis H, S, Achsen x, y, z.",
    kontext="Kirchturm/Dach",
    textumfang="kurz",
    gegeben="Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m; Raute CGSF",
    gesucht="Innenwinkel bei S; gesamter Flächeninhalt der vier Dachflächen",
    verfahren="Winkel zwischen SG und SF; Rautenfläche über Kreuzprodukt oder Diagonalen, mal 4",
    schritte="4",
    zahlenraum="Wurzel|dezimal",
    einheiten="Grad|m²",
    ergebnis="cos φ = 36/52, φ ≈ 46°; Gesamtfläche 2 · √32 · √176 ≈ 150 m² (amtlich)",
    zwischenergebnis="Rautenfläche ≈ 37,5",
    niveau_geschaetzt="II",
    fehlerquelle="Rautenfläche als Seite mal Seite rechnen",
    abhaengig_von="",
    bemerkung="Standardbezug: K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B3f (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBAGLAA2WTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Verhältnis zweier Abstände über den Strahlensatz an der Pyramidenspitze begründen",
    typ_neben="",
    stichwoerter="F und G liegen in Höhe 6, S in Höhe 12, Q1 und Q2 in Höhe 0|Strahlensatz von S aus: Q1Q2 = 2 · FG|Verhältnis 2 : 1",
    voraussetzungen="zentrische Streckung von S aus|Höhenverhältnis 12 : 6",
    format="Kurzantwort|Begründung",
    operator="Geben Sie an|Begründen Sie",
    antwort="Zahl|Text",
    material="Körper",
    skizze="Schrägbild des Dachs im Koordinatensystem: Quadrat ABCD in der xy-Ebene, darüber die Giebelspitzen E, F, G, H über den Kantenmitten in Höhe 6 und die Spitze S über der Mitte in Höhe 12; graue Giebeldreiecke, Kanten von S zu E, F, G, H; Beschriftungen A bis H, S, Achsen x, y, z.",
    kontext="Kirchturm/Dach",
    textumfang="mittel",
    gegeben="Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m; q1 durch S und F, q2 durch S und G schneiden die xy-Ebene in Q1 bzw. Q2",
    gesucht="Verhältnis des Abstands von Q1 und Q2 zum Abstand von F und G, mit Begründung",
    verfahren="F, G halbieren die Strecken SQ1, SQ2 (Höhe 6 von 12), Strahlensatz",
    schritte="2",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="Die Dreiecke SQ₁Q₂ und SFG haben bei S einen gemeinsamen Innenwinkel, Q₁Q₂ ist parallel zu FG, also sind sie ähnlich; SQ₁ ist doppelt so lang wie SF, der Abstand von Q₁ und Q₂ also doppelt so groß wie der von F und G (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Q1, Q2 ausrechnen und nur numerisch vergleichen",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 II, K2 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Abgewandelte Fassung im Landesheft 2022-bebb-gk 3 g: der Pool verlangt die Begründung ohne Berechnung von Q₁ und Q₂, das Heft lässt den Weg offen. Landesheft 2022-bebb-gk B3g (abgewandelt, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ aus der Landeszeile, Felder auf die Poolfassung angepasst.")
row("2022MgrundlegendBAGLAA2WTR2", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lösungsweg für den Lotfußpunkt eines Punktes auf einer Geraden beschreiben",
    typ_neben="",
    stichwoerter="Mittelpunkt M von EG: (4 | 4 | 6)|Gerade SF: x = S + t · SF|R = Lotfußpunkt: (R − M) · SF = 0 nach t lösen (t = 9/13)|R ≈ (6,8 | 4 | 7,8)",
    voraussetzungen="Mittelpunkt|Punkt auf einer Geraden mit Parameter|Orthogonalität als kürzeste Verbindung",
    format="Begründung",
    operator="Beschreiben Sie",
    antwort="Text",
    material="Körper",
    skizze="Schrägbild des Dachs im Koordinatensystem: Quadrat ABCD in der xy-Ebene, darüber die Giebelspitzen E, F, G, H über den Kantenmitten in Höhe 6 und die Spitze S über der Mitte in Höhe 12; graue Giebeldreiecke, Kanten von S zu E, F, G, H; Beschriftungen A bis H, S, Achsen x, y, z.",
    kontext="Kirchturm/Dach",
    textumfang="mittel",
    gegeben="Kirchturmdach: Eckpunkte A(0 | 0 | 0), B(8 | 0 | 0), C(8 | 8 | 0), D(0 | 8 | 0), E(4 | 0 | 6), F(8 | 4 | 6), G(4 | 8 | 6), H(0 | 4 | 6), S(4 | 4 | 12); vier gleiche viereckige Dachflächen (Rauten wie CGSF) und vier dreieckige Giebelflächen; 1 LE = 1 m; Stahlträger EG, von dessen Mittelpunkt eine möglichst kurze Stütze zum Balken SF verläuft; Auftreffpunkt R auf SF, R ≠ F, S",
    gesucht="Beschreibung, wie die Koordinaten von R ermittelt werden könnten",
    verfahren="M bestimmen, allgemeinen Punkt R(t) auf SF ansetzen, Skalarprodukt MR · SF = 0 lösen, t einsetzen",
    schritte="3",
    zahlenraum="ganz|Bruch",
    einheiten="",
    ergebnis="Mittelpunkt N von EG bestimmen; mit OR = OS + σ · SF liefert (OR − ON) · SF = 0 den Wert von σ und damit R (R = (88/13 | 4 | 102/13)) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Mittelpunkt von SF statt Lotfußpunkt nehmen",
    abhaengig_von="",
    bemerkung="Standardbezug: K2 III, K3 II, K4 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B3i (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="X ~ B(100; 0,07)|P(X = 9) = F(9) − F(8) = 0,8380 − 0,7340 = 0,104|P(X < 9) = F(8) = 0,734",
    voraussetzungen="Tabelle der summierten Binomialverteilung lesen|Einzelwert als Differenz",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Paketzentrum",
    textumfang="kurz",
    gegeben="Paketzentrum: 10 % der Pakete haben das Ziel A, 7 % das Ziel B; 100 zufällig ausgewählte Pakete",
    gesucht="P(genau neun mit Ziel B); P(weniger als neun mit Ziel B)",
    verfahren="Werte aus der Tabelle (p = 0,07, n = 100)",
    schritte="2",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="P(X = 9) ≈ 10 %; P(X < 9) ≈ 73 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="P(X < 9) als F(9) lesen",
    abhaengig_von="",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B4b (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Prozentuale Abweichung einer Anzahl vom Erwartungswert berechnen",
    typ_neben="",
    stichwoerter="E(X) = 100 · 0,07 = 7|(9 − 7)/7 ≈ 28,6 %",
    voraussetzungen="Erwartungswert n · p|relative Abweichung",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Paketzentrum",
    textumfang="kurz",
    gegeben="Paketzentrum: 10 % der Pakete haben das Ziel A, 7 % das Ziel B; Anlage mit Tabelle der summierten Binomialverteilung; unter 100 Paketen haben genau neun das Ziel B",
    gesucht="prozentuale Abweichung dieser Anzahl vom Erwartungswert",
    verfahren="Erwartungswert 7, Differenz durch 7",
    schritte="2",
    zahlenraum="Prozent|dezimal",
    einheiten="",
    ergebnis="(9 − 7)/7 ≈ 29 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Abweichung auf 100 statt auf 7 beziehen",
    abhaengig_von="",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B4c (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBStochastikWTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer bestimmen",
    typ_neben="",
    stichwoerter="(1 − p)^20 = 0,54|1 − p = 0,54^(1/20)|p ≈ 0,030, etwa 3 %",
    voraussetzungen="Null Treffer als Potenz|20. Wurzel",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Paketzentrum",
    textumfang="kurz",
    gegeben="Paketzentrum: 10 % der Pakete haben das Ziel A, 7 % das Ziel B; Anlage mit Tabelle der summierten Binomialverteilung; 20 Pakete zufällig ausgewählt; P(keines mit Ziel C) ≈ 54 %",
    gesucht="Anteil der Pakete mit Ziel C unter allen Paketen",
    verfahren="(1 − p)^20 = 0,54 nach p auflösen",
    schritte="2",
    zahlenraum="dezimal|Prozent|Wurzel",
    einheiten="",
    ergebnis="(1 − x)²⁰ = 0,54 ⇔ x = 1 − ²⁰√0,54 ≈ 3 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="0,54/20 rechnen",
    abhaengig_von="",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B4e (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBStochastikWTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen",
    typ_neben="",
    stichwoerter="S∩Z = 0,08 · 0,10 = 0,008|S∩¬Z 0,042, ¬S∩Z 0,092, ¬S∩¬Z 0,858|Ränder S 0,05, Z 0,10",
    voraussetzungen="Schnitt aus bedingter Wahrscheinlichkeit|Differenzen der Ränder",
    format="Tabelle",
    operator="Stellen Sie dar",
    antwort="Tabelle",
    material="keins",
    skizze="keine",
    kontext="Paketzentrum",
    textumfang="kurz",
    gegeben="P(S) = 5 %, P(Z) = 10 %, P_Z(S) = 8 %",
    gesucht="vollständige Vierfeldertafel",
    verfahren="S∩Z = 0,008, Rest aus den Rändern",
    schritte="3",
    zahlenraum="dezimal",
    einheiten="",
    ergebnis="S∩Z 0,008, S∩¬Z 0,042, ¬S∩Z 0,092, ¬S∩¬Z 0,858; Ränder S 0,05, ¬S 0,95, Z 0,10, ¬Z 0,90 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="8 % direkt als Feld S∩Z eintragen",
    abhaengig_von="",
    bemerkung="Standardbezug: K2 II, K3 I, K4 I, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B4h (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBStochastikWTR1", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen",
    typ_neben="",
    stichwoerter="P_S(Z) = 0,008/0,05 = 0,16|P_¬S(Z) = 0,092/0,95 ≈ 0,097|Anteile verschieden: nicht unabhängig",
    voraussetzungen="bedingte Anteile aus der Tafel",
    format="Rechnung",
    operator="Untersuchen Sie",
    antwort="Text",
    material="Tabelle",
    skizze="Vierfeldertafel aus h.",
    kontext="Paketzentrum",
    textumfang="kurz",
    gegeben="Vierfeldertafel aus h",
    gesucht="ob der Anteil der Pakete mit Ziel A unter den schweren ebenso groß ist wie unter den nicht schweren",
    verfahren="Beide bedingten Anteile berechnen und vergleichen",
    schritte="2",
    zahlenraum="dezimal",
    einheiten="",
    ergebnis="Der Anteil der schweren Pakete ist unter denen mit Ziel A (8 %) anders als unter allen (5 %), also sind S und Z abhängig und die Anteile stimmen nicht überein (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="P_Z(S) mit P_S(Z) verwechseln",
    abhaengig_von="2022MgrundlegendBStochastikWTR1-1e",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Landesheft 2022-bebb-gk B4i (wortgleich, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ, Schätzung und Felder aus der Landeszeile übernommen.")
row("2022MgrundlegendBStochastikWTR1", "g", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil in der Restgruppe über die totale Wahrscheinlichkeit einordnen",
    typ_neben="",
    stichwoerter="0,05 = 0,10 · 0,08 + 0,07 · 0,02 + 0,83 · x|x = (0,05 − 0,008 − 0,0014)/0,83 ≈ 0,049|kleiner als 5 % (A und B liegen mit 8 % über, 2 % unter dem Mittel, das Gewicht von A überwiegt)",
    voraussetzungen="totale Wahrscheinlichkeit über drei Gruppen|Gleichung nach dem Anteil lösen",
    format="Rechnung|Begründung",
    operator="Untersuchen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Paketzentrum",
    textumfang="mittel",
    gegeben="P(S) = 5 %; unter Ziel A (10 %) 8 % schwer, unter Ziel B (7 %) 2 % schwer",
    gesucht="ob der Anteil schwerer Pakete unter denen mit anderem Ziel kleiner, gleich oder größer als 5 % ist",
    verfahren="Gleichung der totalen Wahrscheinlichkeit nach x auflösen",
    schritte="2",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="Unter allen Paketen ist der Anteil mit Ziel A größer als der mit Ziel B; damit liegt der Anteil der schweren Pakete unter denen mit Ziel A oder B insgesamt über 5 %, unter den übrigen also unter 5 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Anteile 8 % und 2 % ungewichtet mitteln",
    abhaengig_von="",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Abgewandelte Fassung im Landesheft 2022-bebb-gk 4 j: der Pool verlangt die Begründung ohne Berechnung des Anteils, das Heft lässt die Rechnung zu. Landesheft 2022-bebb-gk B4j (abgewandelt, dort vorgemerkt; Lauf 18 stellt den Vermerk um); Typ aus der Landeszeile, Felder auf die Poolfassung angepasst.")
NEUE_TYPEN = [
    ("Nullstellen und Werte: Nullstelle null am Term ohne konstanten Summanden begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Nullstelle 0 eines Polynoms angeben und damit begründen, dass der Term keinen konstanten Summanden hat (x lässt sich ausklammern).",
     "2022MgrundlegendBAnalysisWTR1-1a"),
    ("Symmetrie: Weiteren Wendepunkt über die Punktsymmetrie ohne Rechnung begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus den ungeraden Exponenten die Punktsymmetrie zum Ursprung ablesen und daraus schließen, dass das Spiegelbild eines bekannten Wendepunkts ebenfalls Wendepunkt ist.",
     "2022MgrundlegendBAnalysisWTR1-1b"),
    ("Ableitung als Quadrat eines Produkts von Linearfaktoren nachweisen", "Analysis", "Ableitungsregeln",
     "Eine ganzrationale Funktion ableiten und den Ableitungsterm über binomische Formeln in eine vorgegebene Form als Quadrat eines Produkts von Linearfaktoren bringen.",
     "2022MgrundlegendBAnalysisWTR1-1c"),
    ("Schnittpunkt zweier Tangenten nachweisen und Tangenten einzeichnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Zwei Tangenten eines Graphen aufstellen, einen vorgegebenen Punkt als gemeinsamen Punkt nachweisen und beide Geraden in die Abbildung einzeichnen.",
     "2022MgrundlegendBAnalysisWTR1-1d"),
    ("Integralwert: Näherungswert eines Integrals als Trapezfläche am Graphen begründen", "Analysis", "Flächeninhalt durch Integration",
     "Einen vorgegebenen Term als Inhalt eines Trapezes (etwa aus Tangenten und Achsen) erkennen und begründen, dass er den Wert eines Integrals näherungsweise wiedergibt.",
     "2022MgrundlegendBAnalysisWTR1-1e"),
    ("Parameter einer Sinusfunktion aus Extremstelle und Funktionswert bestimmen", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Für g(x) = a · sin(bx) den Parameter b aus einer vorgegebenen Extremstelle (Viertelperiode) und a aus einem Funktionswert bestimmen.",
     "2022MgrundlegendBAnalysisWTR1-1g"),
    ("Nullstellen und Werte: Durchmesser der Grundfläche eines Rotationskörpers aus der Nullstelle der Profilfunktion mit Maßstab nachweisen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Nullstelle der Profilfunktion eines rotationssymmetrischen Körpers berechnen, verdoppeln und mit dem Maßstab in den realen Durchmesser umrechnen.",
     "2022MgrundlegendBAnalysisWTR1-2a"),
    ("Körper: Passung eines Zylinders in ein Gefäß über die Höhe aus dem Volumen prüfen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Aus Durchmesser und Volumen eines Zylinders seine Höhe berechnen und mit Höhe und Öffnung eines Gefäßes vergleichen, ob er hineinpasst.",
     "2022MgrundlegendBAnalysisWTR1-2b"),
    ("Scharparameter für ein vorgegebenes Verhältnis zweier Radien einer Profilkurve berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Radien eines rotationssymmetrischen Körpers an zwei Höhen als Terme im Scharparameter aufstellen, ein vorgegebenes Verhältnis als Gleichung ansetzen und den Parameter berechnen.",
     "2022MgrundlegendBAnalysisWTR1-2c"),
    ("Nullstellen und Werte: Passende Abbildung des Graphen über einen Funktionswert auswählen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Unter mehreren Abbildungen die des Graphen auswählen, indem ein Funktionswert berechnet und mit den Abbildungen verglichen wird.",
     "2022MgrundlegendBAnalysisWTR2-1c"),
    ("Transformation: Bild des Graphen unter Spiegelung, Streckung und Verschiebung als Ableitungsgraph nachweisen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Vorgegebene Transformationen (Spiegelung, Streckung, Verschiebung) in den Funktionsterm übersetzen und zeigen, dass der entstehende Term die Ableitung ist.",
     "2022MgrundlegendBAnalysisWTR2-1e"),
    ("Transformation: Integrationsgrenzen und Faktor für ein Integral über den transformierten Graphen bestimmen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Für ∫ f = k · ∫ g mit g als transformiertem f die Verschiebung in die Grenzen und Spiegelung und Streckung in den Faktor k übersetzen.",
     "2022MgrundlegendBAnalysisWTR2-1f"),
    ("Übergangsprozess: Übergangsdiagramm zur Matrix auswählen und fehlende Werte angeben", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Unter mehreren Übergangsdiagrammen das zur Übergangsmatrix passende auswählen und die Platzhalter an den Pfeilen aus der Matrix belegen.",
     "2022MgrundlegendBAGLAA1WTR-1a"),
    ("Übergangsprozess: Komponentensumme eines Produkts mit der diagonalfreien Matrix als Wechslerzahl deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Erkennen, dass eine Matrix aus der Übergangsmatrix durch Nullsetzen der Diagonale entsteht, und die Komponentensumme des Produkts mit dem Zustandsvektor als Anzahl der Wechsler deuten.",
     "2022MgrundlegendBAGLAA1WTR-1c"),
    ("Matrizenalgebra: Fehlende Einträge einer Matrixpotenz über Zeile mal Spalte und Spaltensumme berechnen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einzelne Einträge von M² über Zeile mal Spalte berechnen oder über die Spaltensumme 1 einer stochastischen Matrix ergänzen.",
     "2022MgrundlegendBAGLAA1WTR-1d"),
    ("Übergangsprozess: Aussagen über Anteile nach zwei Übergängen mit M² beurteilen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aussagen über die Verteilung nach zwei Übergängen mit den Einträgen von M² prüfen, auch allgemein mit unbekannten Anfangsanteilen (Abschätzung).",
     "2022MgrundlegendBAGLAA1WTR-1e"),
    ("Übergangsprozess: Term für die Verteilung mit zwischenzeitlichem Abgang über Diagonalmatrix und Matrixpotenzen angeben", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen Term aufstellen, der Übergänge über mehrere Tage als Matrixpotenzen und einen zwischenzeitlichen anteiligen und absoluten Abgang als Diagonalmatrix und Vektor verkettet.",
     "2022MgrundlegendBAGLAA1WTR-1f"),
    ("Ebene Figur: Parallelogramm über gleiche Verbindungsvektoren nachweisen und Rechteck über das Skalarprodukt ausschließen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Ein Viereck über gleiche gegenüberliegende Verbindungsvektoren als Parallelogramm nachweisen und über ein von null verschiedenes Skalarprodukt benachbarter Seiten ausschließen, dass es ein Rechteck ist.",
     "2022MgrundlegendBAGLAA2WTR1-1a"),
    ("Vertikale Lage einer Fläche über einen Normalenvektor mit x₃-Komponente null nachweisen", "Analytische Geometrie", "Ebenen",
     "Aus zwei Spannvektoren einen Normalenvektor bestimmen und aus seiner dritten Komponente null schließen, dass die Fläche senkrecht auf der Grundebene steht.",
     "2022MgrundlegendBAGLAA2WTR1-1b"),
    ("Ebene Figur: Größeren Teil einer Wand über die Lage der Diagonalen begründen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Begründen, welcher Teil eines durch eine horizontale Linie geteilten Parallelogramms größer ist, indem die Linie mit der flächenhalbierenden Diagonale verglichen wird.",
     "2022MgrundlegendBAGLAA2WTR1-1c"),
    ("Neigung einer Strecke in Prozent aus Höhendifferenz und Horizontalabstand berechnen", "Analytische Geometrie", "Geraden",
     "Die Neigung einer Strecke im Raum als Quotient aus Höhendifferenz und Abstand der Fußpunkte in Prozent berechnen.",
     "2022MgrundlegendBAGLAA2WTR1-1e"),
    ("Höhenunterschied zweier übereinanderliegender Punkte auf Seilgeraden bestimmen", "Analytische Geometrie", "Geraden",
     "„Vertikal übereinander“ als Gleichheit der ersten beiden Koordinaten übersetzen, den Parameter der unteren Geraden bestimmen und die Differenz der Höhen berechnen.",
     "2022MgrundlegendBAGLAA2WTR1-1f"),
    ("Term und Ereignis: Produkt aus Potenz und kumulierter Binomialsumme als Ereignis beschreiben", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Einen Term q^m · Σ B(k; p; i) als Ereignis mit einem festen Anfangsabschnitt und einer „höchstens“-Bedingung im Restabschnitt beschreiben.",
     "2022MgrundlegendBStochastikWTR1-1d"),
    ("Anteil über die totale Wahrscheinlichkeit aus dem Baumdiagramm berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit eines Ereignisses der zweiten Stufe als Summe der Pfadwahrscheinlichkeiten berechnen.",
     "2022MgrundlegendBStochastikWTR2-1b"),
    ("Stichprobenumfang aus dem Erwartungswert berechnen und Einzelwahrscheinlichkeit ermitteln", "Stochastik", "Binomialverteilung",
     "Aus n · p = μ den Umfang n berechnen und die Wahrscheinlichkeit für genau μ Treffer mit dem Rechner ermitteln.",
     "2022MgrundlegendBStochastikWTR2-2a"),
    ("Stichprobenumfang zu einer vorgegebenen Einzelwahrscheinlichkeit mit dem Rechner suchen", "Stochastik", "Binomialverteilung",
     "Ein n finden, für das P(X = k) einen vorgegebenen Wert annimmt, durch systematisches Probieren am Rechner.",
     "2022MgrundlegendBStochastikWTR2-2b"),
    ("Aussagen über Verteilungen verschiedener Gruppen am Säulendiagramm beurteilen", "Stochastik", "Binomialverteilung",
     "Aussagen über Einzelwahrscheinlichkeiten und Trefferwahrscheinlichkeiten mehrerer Binomialverteilungen an ihren Säulendiagrammen (Säulenhöhe, Lage des Maximums) beurteilen.",
     "2022MgrundlegendBStochastikWTR2-3a"),
    ("Monotonie der Varianz einer Binomialverteilung in p über die Parabel begründen", "Stochastik", "Kenngrößen von Verteilungen",
     "Die Varianz n · p · (1 − p) als Funktion von p als nach unten geöffnete Parabel mit Scheitel bei 0,5 deuten und daraus die Monotonie für 0 < p < 0,5 begründen.",
     "2022MgrundlegendBStochastikWTR2-3b"),
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
    # Schwelle je Stapel überschreibbar (v1.4), nur mit Begründung in KONFIG.
    eich_min = KONFIG.get("eichung_mindestens", SCHWELLEN["eichung_mindestens"])
    if "eichung_mindestens" in KONFIG:
        a(bool(KONFIG.get("eichung_grund")), "KONFIG: eichung_mindestens ohne eichung_grund")
    if gew >= SCHWELLEN["eichung_ab_zeilen"]:
        a(treffer_eng / gew >= eich_min,
          f"Schwelle gerissen: Eichung (enge Fassung) {treffer_eng} von {gew} "
          f"({100 * treffer_eng / gew:.0f} %), verlangt {100 * eich_min:.0f} %: "
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
          f"Eichung {100 * treffer_eng / gew if gew else 0:.0f} % (verlangt {100 * eich_min:.0f} %"
          + (f", für diesen Stapel statt {100 * SCHWELLEN['eichung_mindestens']:.0f} %: {KONFIG['eichung_grund']}" if "eichung_mindestens" in KONFIG else "") + ")")
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
