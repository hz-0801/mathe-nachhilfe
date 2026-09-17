# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 1.5 · 17.09.2026 · gilt mit katalog-prompt.md v0.6, abitur-vokabular.md v1.2 und iqb.md v1.8

Änderungen gegenüber 1.4 (Auftrag „Eichung korrigieren, Prüfungsgeschichte und
Prüfungsstruktur festhalten, Heftordner ordnen", 17.09.2026, Entscheidung des
Lehrers): Die Überschreibung der Eichschwelle je Stapel (KONFIG
„eichung_mindestens"/„eichung_grund", v1.4) ist zurückgebaut, die globale
Schwelle in SCHWELLEN gilt für jeden Stapel. Vorrang des Amtlichen (Kern § 5):
eine Zeile, deren Schätzung aus einer Landeszeile übernommen ist (bemerkung
„… aus der Landeszeile übernommen"), muss den amtlichen Bereich treffen – weicht
sie ab, wird die Schätzung korrigiert, nicht die Schwelle; das Skript bricht
sonst ab (Stapellauf und Selbstprüfung). Die neun betroffenen Zeilen von
2022-ga-B hat abgleich.py Lauf 20 gesetzt.

Änderungen gegenüber 1.3 (Stapel 2022-ga-B, 17.09.2026; in 1.5 zurückgebaut): Die Eichschwelle darf
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
    "stapel": "2021-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2021MgrundlegendBAnalysisWTR": 35, "2021MgrundlegendBAGLAA1WTR": 20, "2021MgrundlegendBAGLAA2WTR1": 20, "2021MgrundlegendBAGLAA2WTR2": 20,
        "2021MgrundlegendBStochastikWTR1": 20, "2021MgrundlegendBStochastikWTR2": 20, "2021MgrundlegendBStochastikWTR3": 20,
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
# Ein row(kennung, teilaufgabe, ...) je Teilaufgabe; id, jahr, papier, block,
# aufgabe, titel, stern und hilfsmittel leitet row() aus der Kennung ab.
# Stapel 2021-ga-B (WTR-Zweig; Reserve, geöffnet 17.09.2026 in Auftrag C Teil 2 wegen der
# zwölf Landesheftverweise von 2021-be-gk 3 a, c, d, g, h, i auf AG/LA (A2) WTR 1 und
# 4 a, c, d, g, h, i auf Stochastik WTR 2). Sieben Dateien (die fünf CAS-Dateien bleiben
# Reserve), Standardbezug mit Spalte Anforderungsbereich; Analysis 35 BE, die übrigen 20 BE.
# ---- Analysis WTR: f(x) = −5/16 x⁴ + 5x³, Aufgabe 1 (a–f, 24 BE) und Glyzerintank (2 a–d, 11 BE)
A1 = "f(x) = −5/16 x⁴ + 5x³, in IR definiert; die Abbildung zeigt den Graphen von f"
A1_SK = ("Koordinatensystem auf Gitter, x von −4 bis 18, y von −400 bis 2400 (Schritte 400): Graph von f mit Sattelpunkt im Ursprung, "
         "steigend bis zum Hochpunkt (12 | 2160), danach steil fallend durch (16 | 0)")
row("2021MgrundlegendBAnalysisWTR", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Hochpunkt mit vorgegebenen Koordinaten und waagerechte Tangente im Ursprung rechnerisch nachweisen", typ_neben="",
    stichwoerter="f'(x) = −5/4 x³ + 15x², f''(x) = −15/4 x² + 30x|f(12) = 2160, f'(12) = 0, f''(12) = −180 < 0: Hochpunkt|f'(0) = 0: Tangente in (0 | 0) parallel zur x-Achse",
    voraussetzungen="Potenzregel|hinreichende Bedingung für Extrempunkte|Tangentensteigung als Ableitungswert",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Koordinatensystem", skizze=A1_SK, kontext="ohne", textumfang="kurz",
    gegeben=A1,
    gesucht="Nachweis, dass (12 | 2160) Hochpunkt ist und die Tangente in (0 | 0) parallel zur x-Achse verläuft",
    verfahren="f' und f'' bilden, Werte an den Stellen 12 und 0 prüfen",
    schritte="3", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −5/4 x³ + 15x², f''(x) = −15/4 x² + 30x; f(12) = 2160, f'(12) = 0, f''(12) = −180 < 0, also Hochpunkt; f'(0) = 0, also Tangente parallel zur x-Achse (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="f''(12) nicht prüfen; f'(0) = 0 als Extremstelle deuten",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2021MgrundlegendBAnalysisWTR", "b", innen="1", seite="1", punkte="7", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Gerade durch die beiden Wendepunkte aufstellen und parallele Gerade mit genau einem gemeinsamen Punkt einzeichnen", typ_neben="",
    stichwoerter="f''(x) = 0 ⇔ x · (−15/4 x + 30) = 0 ⇔ x = 0 ∨ x = 8|f(0) = 0, f(8) = 1280: g: y = 160x|parallele Gerade mit genau einem Punkt mit dem Graphen auf [0; 8]: Tangente an den Bogen (Berührpunkt zwischen den Wendepunkten) oder Gerade durch einen Randpunkt",
    voraussetzungen="Wendestellen über f'' = 0 mit Vorzeichenwechsel|Geradengleichung durch zwei Punkte|Parallele mit Berührbedingung zeichnen",
    format="Rechnung|Zeichnen", operator="Bestimmen Sie|Zeichnen Sie", antwort="Term|Grafik",
    material="Koordinatensystem", skizze=A1_SK, kontext="ohne", textumfang="mittel",
    gegeben=A1,
    gesucht="Gleichung der Geraden g durch die beiden Wendepunkte; in der Abbildung eine zu g parallele Gerade, die für 0 ≤ x ≤ 8 mit dem Graphen genau einen Punkt gemeinsam hat",
    verfahren="Wendestellen berechnen, g aus (0 | 0) und (8 | 1280); Parallele als Tangente an den Bogen zwischen den Wendepunkten einzeichnen",
    schritte="4", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2021MgrundlegendBAnalysisWTR-1a",
    ergebnis="f''(x) = 0 ⇔ x = 0 ∨ x = 8; mit f(0) = 0 und f(8) = 1280 ergibt sich y = 160x; Zeichnung einer Parallelen zu g, die den Graphen zwischen den Wendepunkten berührt (amtlich)",
    zwischenergebnis="Wendepunkte (0 | 0) und (8 | 1280)", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichenwechsel von f'' bei 0 nicht prüfen; Parallele durch beide Randpunkte zeichnen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (parallele Tangente y = 160x − 400 berührt bei x = 4, weitere Schnittstellen 4 ± √96 liegen außerhalb von [0; 8]).")
H1 = A1 + "; Schar h_a(x) = 5a x², a ∈ IR, in IR definiert"
row("2021MgrundlegendBAnalysisWTR", "c", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Graph eines in y-Richtung gestreckten Scharmitglieds begründen und skizzieren", typ_neben="",
    stichwoerter="h₄(x) = 20x² = 4/3 · 15x² = 4/3 · h₃(x)|Streckung in y-Richtung mit dem Faktor 4/3",
    voraussetzungen="Streckung in y-Richtung als Faktor vor dem Term",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=H1,
    gesucht="Beschreibung, wie der Graph von h₄ aus dem Graphen von h₃ erzeugt werden kann",
    verfahren="Quotient der Vorfaktoren 20/15 als Streckfaktor in y-Richtung nennen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Der Graph von h₄ entsteht aus dem Graphen von h₃ durch eine Streckung in y-Richtung mit dem Faktor 4/3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Streckung in x-Richtung mit Faktor √(3/4) angeben oder eine Verschiebung vermuten",
    bemerkung="Standardbezug: K1 II, K4 I, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2024-ga-B); hier nur die Beschreibung, keine Skizze.")
row("2021MgrundlegendBAnalysisWTR", "d", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameter einer Schar aus einem vorgegebenen Punkt auf dem Graphen bestimmen", typ_neben="",
    stichwoerter="f(4) = −80 + 320 = 240|h_a(4) = 80a = 240 ⇔ a = 3",
    voraussetzungen="Funktionswert berechnen|lineare Gleichung im Parameter",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=H1,
    gesucht="Wert von a, für den (4 | f(4)) auf dem Graphen von h_a liegt",
    verfahren="f(4) berechnen und h_a(4) = f(4) nach a lösen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="h_a(4) = f(4) ⇔ 5a · 16 = 240 ⇔ a = 3 (amtlich)",
    zwischenergebnis="f(4) = 240", niveau_geschaetzt="I",
    fehlerquelle="f(4) falsch berechnen (Vorzeichen bei −5/16 · 256)",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2021MgrundlegendBAnalysisWTR", "e", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameter für genau zwei gemeinsame Punkte von Graph und Scharparabel über die Diskriminante bestimmen", typ_neben="",
    stichwoerter="f(x) = h_a(x) ⇔ −5/16 x² · (x² − 16x + 16a) = 0|x = 0 ∨ x = 8 ± √(64 − 16a)|genau zwei Punkte ⇔ 64 − 16a = 0 ⇔ a = 4",
    voraussetzungen="Gleichsetzen und x² ausklammern|Lösungsformel|Anzahl der Lösungen über die Diskriminante",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=H1 + "; es gibt genau einen positiven Wert von a, für den die Graphen von f und h_a genau zwei gemeinsame Punkte haben",
    gesucht="dieser Wert von a",
    verfahren="Schnittgleichung faktorisieren, quadratischen Faktor mit Diskriminante null ansetzen",
    schritte="4", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="f(x) = h_a(x) ⇔ −5/16 x² · (x² − 16x + 16a) = 0 ⇔ x = 0 ∨ x = 8 ± √(64 − 16a); 64 − 16a = 0 ⇔ a = 4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die Lösung x = 0 vergessen und drei Lösungen des quadratischen Faktors suchen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt.")
row("2021MgrundlegendBAnalysisWTR", "f", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Nullwert eines Integrals über eine Differenzfunktion mit drei Schnittstellen als Flächengleichheit deuten", typ_neben="",
    stichwoerter="drei Lösungen 0, 6, 10: drei gemeinsame Punkte|∫₀¹⁰ (f − h_(3,75)) dx = 0: die beiden Flächenstücke zwischen den Graphen über [0; 6] und [6; 10] sind gleich groß und liegen auf verschiedenen Seiten",
    voraussetzungen="Schnittstellen als Lösungen der Gleichung|Integral der Differenz als orientierte Fläche",
    format="Begründung", operator="Deuten Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=H1 + "; f(x) = h_(3,75)(x) hat genau die Lösungen x₁ = 0, x₂ = 6, x₃ = 10 und ∫₀¹⁰ (f(x) − h_(3,75)(x)) dx = 0",
    gesucht="Deutung mit Bezug auf die Graphen von f und h_(3,75)",
    verfahren="Lösungen als gemeinsame Punkte, Integral null als Flächengleichheit mit Vorzeichenwechsel deuten",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Die Graphen von f und h_(3,75) haben genau drei gemeinsame Punkte und schließen zwei Flächenstücke gleichen Inhalts ein, die auf verschiedenen Seiten des Graphen von h_(3,75) liegen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das Integral null als „keine Fläche zwischen den Graphen“ deuten",
    bemerkung="Standardbezug: K1 III, K4 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Lösungen 0, 6, 10; Integral 0).")
G1 = ("Glyzerintank: f(x) = −5/16 x⁴ + 5x³ beschreibt für 0 ≤ x ≤ 20 die momentane Änderungsrate des Tankinhalts in kg/h, x Zeit in Stunden seit "
      "Beobachtungsbeginn; zu Beobachtungsbeginn 1200 kg im Tank; die Abbildung zeigt den Graphen von f")
row("2021MgrundlegendBAnalysisWTR", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Koordinaten eines Punktes des Ratengraphen im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="(4 | 240): vier Stunden nach Beobachtungsbeginn beträgt die momentane Änderungsrate 240 kg/h",
    voraussetzungen="Bedeutung von x und f(x) im Sachzusammenhang",
    format="Kurzantwort", operator="Interpretieren Sie", antwort="Text",
    material="Koordinatensystem", skizze=A1_SK, kontext="Glyzerintank", textumfang="mittel",
    gegeben=G1 + "; (4 | 240) liegt auf dem Graphen von f",
    gesucht="Bedeutung der Koordinaten im Sachzusammenhang",
    verfahren="x als Zeit, f(x) als momentane Änderungsrate benennen",
    schritte="1", zahlenraum="ganz", einheiten="kg/h", abhaengig_von="",
    ergebnis="Vier Stunden nach Beobachtungsbeginn beträgt die momentane Änderungsrate des Tankinhalts 240 kg pro Stunde (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="240 als Tankinhalt deuten",
    bemerkung="Standardbezug: K3 I, K6 I. AB amtlich: I. Amtlich.")
row("2021MgrundlegendBAnalysisWTR", "b", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zeitpunkt des größten Bestands aus dem Vorzeichenwechsel der Rate begründen", typ_neben="",
    stichwoerter="Aussage: nach zwölf Stunden ist die größte Menge im Tank|falsch, denn f ist nach x = 12 zunächst noch positiv (Nullstelle erst bei 16): der Inhalt nimmt weiter zu",
    voraussetzungen="positive Rate bedeutet Zunahme des Bestands|Maximum des Bestands bei der Nullstelle der Rate mit Vorzeichenwechsel",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=A1_SK, kontext="Glyzerintank", textumfang="kurz",
    gegeben=G1 + "; Aussage: Zwölf Stunden nach Beobachtungsbeginn ist die größte Menge Glyzerin im Tank enthalten",
    gesucht="Beurteilung der Aussage",
    verfahren="Hochpunkt der Rate bei 12 von der Nullstelle der Rate bei 16 unterscheiden",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist falsch, da die momentane Änderungsrate nach dem Zeitpunkt zwölf Stunden zunächst positiv ist (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Maximum der Rate mit dem Maximum des Bestands verwechseln",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2023-ea-B).")
row("2021MgrundlegendBAnalysisWTR", "c", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Bestandsänderung grafisch als Fläche unter dem Ratengraphen bestimmen", typ_neben="",
    stichwoerter="Fläche unter dem Graphen von f zwischen x = 8 und x = 10|Kästchen 2 × 200: etwa 8 Kästchen|8 · 2 · 200 kg = 3200 kg",
    voraussetzungen="Zunahme des Bestands als Integral der Rate|Flächeninhalt über Kästchen abschätzen",
    format="Zeichnen|Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=A1_SK, kontext="Glyzerintank", textumfang="kurz",
    gegeben=G1,
    gesucht="grafisch bestimmte Zunahme des Tankinhalts zwischen acht und zehn Stunden",
    verfahren="Fläche unter dem Graphen über [8; 10] schraffieren und die Kästchen auszählen",
    schritte="2", zahlenraum="ganz", einheiten="kg", abhaengig_von="",
    ergebnis="Der Tankinhalt nimmt um etwa 8 · 2 · 200 kg = 3200 kg zu (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Differenz f(10) − f(8) statt der Fläche nehmen",
    bemerkung="Standardbezug: K2 I, K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (∫₈¹⁰ f = 3178).")
row("2021MgrundlegendBAnalysisWTR", "d", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Bestand nach einem Zeitraum aus Anfangsbestand und Integral der Änderungsrate berechnen", typ_neben="",
    stichwoerter="∫₀²⁰ f(x) dx = [−1/16 x⁵ + 5/4 x⁴]₀²⁰ = 0|Bestand 1200 + 0 = 1200 kg",
    voraussetzungen="Bestand = Anfangsbestand + Integral der Rate|Stammfunktion einer ganzrationalen Funktion",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glyzerintank", textumfang="kurz",
    gegeben=G1,
    gesucht="Glyzerinmenge im Tank 20 Stunden nach Beobachtungsbeginn",
    verfahren="Integral der Rate von 0 bis 20 zum Anfangsbestand addieren",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="kg", abhaengig_von="",
    ergebnis="∫₀²⁰ f(x) dx = [−1/16 x⁵ + 5/4 x⁴]₀²⁰ = 0, d. h. 20 Stunden nach Beobachtungsbeginn befinden sich im Tank 1200 kg Glyzerin (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Integral als Endbestand ohne den Anfangsbestand deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
# ---- AG/LA (A1) WTR: Taxiunternehmen A, B, C (a–f, 20 BE), Aufgabe ohne Nummer (innen 1)
T1 = ("Taxiunternehmen A, B, C; Kundenverteilung als Vektor (a; b; c); Übergang von Monat n zum nächsten v_(n+1) = M · v_n mit "
      "M = (0,1 0,1 0,7 / 0,3 0,8 0,2 / 0,6 0,1 0,1); M⁻¹ = 1/30 · (−6 −6 54 / −9 41 −19 / 45 −5 −5); feste Gruppe von 7000 Kunden")
row("2021MgrundlegendBAGLAA1WTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="drei Zustände A, B, C mit Pfeilen und den neun Übergangsanteilen|Spalte = Ausgangsunternehmen: A → A 0,1, A → B 0,3, A → C 0,6; B → A 0,1, B → B 0,8, B → C 0,1; C → A 0,7, C → B 0,2, C → C 0,1",
    voraussetzungen="Spalten der Übergangsmatrix als Abgänge eines Zustands lesen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Taxiunternehmen", textumfang="mittel",
    gegeben=T1,
    gesucht="Übergangsdiagramm der Kundenverteilung von einem Monat zum nächsten",
    verfahren="Einträge der Matrix spaltenweise als Pfeile zwischen A, B, C eintragen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Übergangsdiagramm mit den Zuständen A, B, C und allen neun Übergangsanteilen (Bleibeanteile 0,1, 0,8, 0,1) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauschen (A → C mit 0,7 statt 0,6)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2018-ea-A); Quelle hier die Matrix statt der Tabelle.")
row("2021MgrundlegendBAGLAA1WTR", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Stationäre Verteilung mit vorgegebener Gesamtzahl berechnen und einen Anteil beurteilen", typ_neben="",
    stichwoerter="a = 1600, b + c = 5400|erste Zeile: 0,1 · 1600 + 0,1 · b + 0,7 · (5400 − b) = 1600 ⇔ 0,6b = 2340 ⇔ b = 3900|c = 1500",
    voraussetzungen="stationär: M · v = v|Gesamtzahl als Nebenbedingung|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Taxiunternehmen", textumfang="kurz",
    gegeben=T1 + "; es gibt eine unveränderliche Verteilung mit 1600 Kunden von A",
    gesucht="diese Verteilung",
    verfahren="Erste Zeile von M · v = v mit a = 1600 und c = 5400 − b nach b lösen",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="Kunden", abhaengig_von="",
    ergebnis="0,1 · 1600 + 0,1 · b + 0,7 · (5400 − b) = 1600 ⇔ 0,6b = 2340 ⇔ b = 3900; c = 5400 − 3900 = 1500 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="alle drei Gleichungen aufstellen und sich in der Auflösung verlieren",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ea-B); hier ohne den beurteilten Anteil.")
row("2021MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="4", afb_amtlich="I|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Spanne einer Komponente nach einem Schritt bei teilweise bekannter Verteilung ermitteln", typ_neben="",
    stichwoerter="a = 2000, c = 5000 − b|B im Folgemonat: 0,3 · 2000 + 0,8b + 0,2 · (5000 − b) = 1600 + 0,6b|0 ≤ b ≤ 5000: mindestens 1600, höchstens 4600",
    voraussetzungen="zweite Zeile von M · v|Term in b mit Randwerten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Taxiunternehmen", textumfang="kurz",
    gegeben=T1 + "; in einem Monat hat A 2000 Kunden",
    gesucht="alle möglichen Anzahlen der Kunden von B im folgenden Monat",
    verfahren="Anzahl von B im Folgemonat als Term in b aufstellen und b von 0 bis 5000 laufen lassen",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="Kunden", abhaengig_von="",
    ergebnis="0,3 · 2000 + 0,8b + 0,2 · (5000 − b) = 1600 + 0,6b; mit 0 ≤ b ≤ 5000 beträgt die Anzahl mindestens 1600 und höchstens 4600 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur einen Beispielwert für b einsetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 I, K5 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ga-B).")
row("2021MgrundlegendBAGLAA1WTR", "d", innen="1", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Vorherige Verteilung über die inverse Matrix berechnen und prozentuale Abnahme einer Komponente angeben", typ_neben="",
    stichwoerter="M⁻¹ · (2800; 2400; 1800) = (2200; 1300; 3500)|C von 3500 auf 1800: (3500 − 1800)/3500 ≈ 49 %",
    voraussetzungen="Rückrechnung mit der inversen Matrix|prozentuale Abnahme",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Taxiunternehmen", textumfang="mittel",
    gegeben=T1 + "; im Mai hat A 2800, B 2400, C 1800 Kunden",
    gesucht="Verteilung im April und prozentuale Abnahme der Kunden von C von April zu Mai",
    verfahren="Maivektor mit M⁻¹ multiplizieren, Abnahme von C auf den Aprilwert beziehen",
    schritte="3", zahlenraum="ganz|Bruch|Prozent", einheiten="Kunden", abhaengig_von="",
    ergebnis="1/30 · (−6 −6 54 / −9 41 −19 / 45 −5 −5) · (2800; 2400; 1800) = (2200; 1300; 3500); (3500 − 1800)/3500 ≈ 49 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Abnahme auf den Maiwert beziehen (94 %)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
T1N = (T1 + "; geändertes Wechselverhalten: der Bleibeanteil bei B sinkt, die zusätzlich wechselnden Kunden gehen je zur Hälfte zu A und C; die "
       "Wechselanteile von A und C bleiben, diese Kunden wechseln aber nicht mehr zu B; zur Auswahl P = (0,1 0,18 0,9 / 0 0,68 0 / 0,9 0,14 0,1) und "
       "Q = (0,1 0,18 0,9 / 0 0,64 0 / 0,9 0,18 0,1)")
row("2021MgrundlegendBAGLAA1WTR", "e", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Geänderte Übergangsmatrix aus zwei Vorschlägen nach dem beschriebenen Wechselverhalten auswählen und begründen", typ_neben="",
    stichwoerter="zusätzliche Wechsler von B müssen je zur Hälfte zu A und C: zweite Spalte 0,18 / 0,64 / 0,18 (gleiche Anteile nach A und C)|bei P gingen 0,18 zu A, aber 0,14 zu C: nicht hälftig|Q",
    voraussetzungen="Spalten der Übergangsmatrix als Abgänge|Aufteilung zusätzlicher Wechsler",
    format="Kurzantwort|Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Taxiunternehmen", textumfang="lang",
    gegeben=T1N,
    gesucht="die Matrix, die das geänderte Wechselverhalten beschreibt, mit Begründung",
    verfahren="Zweite Spalte beider Matrizen gegen die Bedingung „hälftig auf A und C“ prüfen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Q beschreibt das geänderte Wechselverhalten; bei P würden sich die zusätzlich wechselnden Kunden von B nicht je zur Hälfte auf A und C verteilen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur die Nullen in der zweiten Zeile prüfen, die beide Matrizen erfüllen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich.")
row("2021MgrundlegendBAGLAA1WTR", "f", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zeitpunkt für das Unterschreiten eines Anteils der Populationsgröße über einen konstanten Faktor bestimmen", typ_neben="",
    stichwoerter="in Q: Bleibeanteil 0,64 < 1, Zugänge zu B aus A und C sind 0|Anzahl bei B nach n Monaten 0,64ⁿ · b₀|0,64ⁿ < 0,01 ⇔ n > log_0,64(0,01) ≈ 10,3: erstmals im elften Monat",
    voraussetzungen="Matrixzeile als Zugänge lesen|geometrische Abnahme|Logarithmus zur Lösung einer Exponentialungleichung",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Ermitteln Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Taxiunternehmen", textumfang="mittel",
    gegeben=T1N + "; ab der Änderung nimmt die Kundenzahl von B stetig ab",
    gesucht="wie sich die Abnahme in der gewählten Matrix zeigt; Monat, in dem die Kundenzahl von B erstmals unter 1 % des Werts unmittelbar vor der Änderung liegt",
    verfahren="Zweite Zeile von Q deuten (nur 0,64 · b, keine Zugänge), 0,64ⁿ < 0,01 nach n lösen",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="Monate", abhaengig_von="2021MgrundlegendBAGLAA1WTR-1e",
    ergebnis="Der Bleibeanteil bei B ist mit 0,64 kleiner als 1, die Anteile von A und C, die zu B wechseln, sind 0; 0,64ⁿ < 0,01 ⇔ n > log_0,64(0,01) ≈ 10,3, erstmals im elften Monat nach der Änderung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="n = 10 angeben (dort noch 1,15 %)",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,64¹⁰ ≈ 0,0115, 0,64¹¹ ≈ 0,0074). Typ wiederverwendet (2024-ea-B).")
# ---- AG/LA (A2) WTR 1: Holzkörper (a–f, 20 BE); Landesheft 2021-be-gk 3 a, c, d, g, h, i vorgemerkt
K1 = ("Holzkörper mit den Eckpunkten A(0 | 0 | 0), B(10 | 0 | 0), C(10 | 10 | 0), D(0 | 10 | 0) und E(0 | 10 | 6) (Pyramide über dem Quadrat ABCD, "
      "Spitze E senkrecht über D); B, D und E liegen in der Symmetrieebene des Körpers; 1 LE = 1 cm")
K1_SK = ("Schrägbild: Quadrat ABCD in der xy-Ebene (A im Ursprung, B auf der x-Achse, D auf der y-Achse), Spitze E senkrecht über D, "
         "Kanten AE, BE, CE; Dreieck BCE grau; verdeckte Kante AD gestrichelt")
row("2021MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Rechten Winkel und Kathetenlängen eines Dreiecks nachweisen",
    typ_neben="Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen",
    stichwoerter="CB · CE = (0; −10; 0) · (−10; 0; 6) = 0: rechter Winkel bei C|Oberfläche = Quadrat 100 + Dreiecke ADE und CDE je 1/2 · 10 · 6 + Dreiecke ABE und BCE je 1/2 · 10 · √136|10² + 10 · 6 + 10 · √136 = 160 + 10 · √136 ≈ 277 cm²",
    voraussetzungen="Skalarprodukt gleich null|Flächen der Seitendreiecke|Betrag eines Vektors",
    format="Rechnung", operator="Zeigen Sie|Berechnen Sie", antwort="Text|Zahl",
    material="Körper", skizze=K1_SK, kontext="Holzkörper", textumfang="mittel",
    gegeben=K1,
    gesucht="Nachweis, dass BCE rechtwinklig ist; Inhalt der Oberfläche des Körpers",
    verfahren="Skalarprodukt CB · CE; Oberfläche aus Quadrat und vier Dreiecken",
    schritte="4", zahlenraum="ganz|Wurzel", einheiten="cm²", abhaengig_von="",
    ergebnis="CB · CE = 0; 10² + 10 · 6 + 10 · √136 = 160 + 10 · √136 ≈ 277, d. h. die Oberfläche beträgt etwa 277 cm² (amtlich)",
    zwischenergebnis="|CE| = √136", niveau_geschaetzt="I",
    fehlerquelle="Dreieck ADE oder BCE vergessen; |CE| als 10 annehmen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (276,6). Typen aus dem Bestand (2026-ga-A, 2024-ea-B). Landesheft 2021-be-gk 3 a (wortgleich bis auf „Gesamtoberfläche“; dort vorgemerkt, Schätzung dort II – Vorrang des Amtlichen, die Landeszeile zieht im Abgleichlauf nach).")
row("2021MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="L: x = OC + r · CB + s · CE liefert x = 10 − 10s, y = 10 − 10r, z = 6s|z = 6s, x = 10 − 10s: x = 10 − 5/3 z|3x + 5z = 30",
    voraussetzungen="Parameterform aus drei Punkten|Parameter eliminieren oder Normalenvektor über Kreuzprodukt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=K1_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=K1,
    gesucht="Koordinatengleichung der Ebene L durch B, C, E",
    verfahren="Parameterform aufstellen und Parameter eliminieren",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="Aus x = 10 − 10s, y = 10 − 10r, z = 6s ergibt sich x = 10 − 5/3 z, also 3x + 5z = 30 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="y-Koordinate in die Gleichung aufnehmen, obwohl die Ebene parallel zur y-Achse ist",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ea-A). Landesheft 2021-be-gk 3 c (wortgleich; dort vorgemerkt).")
row("2021MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="Winkel zwischen Grundfläche und Seitenfläche BCE|tan φ = |DE|/|CD| = 6/10 (Neigung an der Kante BC)|φ ≈ 31°",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren oder über das Steigungsdreieck|Tangens",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=K1_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=K1,
    gesucht="Größe des Winkels zwischen der Grundfläche und der Seitenfläche BCE",
    verfahren="Steigungsdreieck DE/CD oder Normalenvektoren (0; 0; 1) und (3; 0; 5)",
    schritte="2", zahlenraum="dezimal", einheiten="°", abhaengig_von="",
    ergebnis="tan φ = |DE|/|CD| = 6/10, d. h. φ ≈ 31° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Winkel zwischen CE und der Grundfläche (≈ 23°) berechnen",
    bemerkung="Standardbezug: K3 I, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (30,96°). Typ wiederverwendet (2026-ea-B). Landesheft 2021-be-gk 3 d (wortgleich; dort vorgemerkt).")
row("2021MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Rechenweg für die kürzeste Linie über eine Kante aus Lotfußpunkt und Symmetrie erläutern", typ_neben="",
    stichwoerter="P(10 − 10t | 10t | 6t) allgemeiner Punkt der Kante BE|PC · PB = 0 ⇔ t = 25/59: PC senkrecht zu BE, kürzeste Verbindung von C zur Kante|Symmetrie: Linie von A über P nach C ist 2 · |PC| ≈ 15,2",
    voraussetzungen="Punkt auf einer Strecke mit Parameter|Lot als kürzeste Verbindung|Symmetrieebene durch B, D, E",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=K1_SK, kontext="Holzkörper", textumfang="mittel",
    gegeben=K1 + "; kürzeste Linie von A über die Kante BE nach C; Rechnung: P(10 − 10t | 10t | 6t), PC · PB = 0 ⇔ t = 25/59, 2 · |PC| ≈ 15,2",
    gesucht="Erläuterung des Vorgehens",
    verfahren="P als Punkt der Kante deuten, Orthogonalität als Kürzestbedingung, Verdopplung über die Symmetrie erklären",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="cm", abhaengig_von="",
    ergebnis="P ist der Punkt der Linie auf BE; wegen der Symmetrie des Körpers ist die Länge 2 · |PC|; da die Linie möglichst kurz sein soll, steht PC senkrecht auf PB (amtlich)",
    zwischenergebnis="t = 25/59", niveau_geschaetzt="III",
    fehlerquelle="PC · PB = 0 als Bedingung für den Mittelpunkt der Kante deuten",
    bemerkung="Standardbezug: K1 III, K3 II, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (15,18). Typ wiederverwendet (2021-be-gk). Landesheft 2021-be-gk 3 g (wortgleich; dort vorgemerkt).")
row("2021MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Spurgerade einer Ebene in einer Koordinatenebene in das Schrägbild einzeichnen", typ_neben="",
    stichwoerter="F = Schnittpunkt von L mit der z-Achse: F(0 | 0 | 6)|Spurgerade in der xz-Ebene: Gerade BF|Spurgerade in der yz-Ebene: Gerade FE (z = 6)",
    voraussetzungen="Spurpunkt auf der z-Achse aus der Koordinatengleichung|Spurgeraden durch zwei Spurpunkte",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Körper", skizze=K1_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=K1 + "; L: 3x + 5z = 30; F = Schnittpunkt von L mit der z-Achse",
    gesucht="F und die Schnittgeraden von L mit der xz- und der yz-Ebene in der Abbildung",
    verfahren="F(0 | 0 | 6) eintragen, Geraden BF und FE einzeichnen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2021MgrundlegendBAGLAA2WTR1-1b",
    ergebnis="F(0 | 0 | 6); Spurgerade in der xz-Ebene BF, in der yz-Ebene die Gerade FE; Zeichnung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="F auf der Höhe von E, aber nicht auf der z-Achse eintragen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2017-ea-A). Landesheft 2021-be-gk 3 h (wortgleich; dort vorgemerkt).")
row("2021MgrundlegendBAGLAA2WTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumenverhältnis zweier Körper über Formeln ohne Zahlenwerte ermitteln", typ_neben="",
    stichwoerter="V(ABCDE) = 1/3 · |AB|² · |DE| (Pyramide)|V(ABCDEF) = 1/2 · |AB|² · |DE| (halber Quader, Prisma mit Dreiecksquerschnitt)|Verhältnis 3/2: um 50 % größer",
    voraussetzungen="Volumenformeln Pyramide und Prisma|Verhältnis ohne Zahlenwerte",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=K1_SK, kontext="Holzkörper", textumfang="kurz",
    gegeben=K1 + "; Körper ABCDEF mit F(0 | 0 | 6)",
    gesucht="um wie viel Prozent das Volumen von ABCDEF größer ist als das von ABCDE, ohne konkrete Volumina zu berechnen",
    verfahren="Beide Volumina als Formeln in |AB| und |DE| schreiben und den Quotienten bilden",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="V(ABCDE) = 1/3 · |AB|² · |DE|, V(ABCDEF) = 1/2 · |AB|² · |DE| = 3/2 · V, also um 50 % größer (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Prisma als Quader ansetzen (Faktor 3 statt 3/2)",
    bemerkung="Standardbezug: K1 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2021-be-gk). Landesheft 2021-be-gk 3 i (wortgleich; dort vorgemerkt, Schätzung dort III – Vorrang des Amtlichen, die Landeszeile zieht im Abgleichlauf nach).")
# ---- AG/LA (A2) WTR 2: Rasenfläche und Mähroboter (a–e, 20 BE)
R1 = ("Ebene Rasenfläche mit den Eckpunkten A(0 | 0 | 0), B(18 | 0 | 1,5), C(12 | 10 | 1), D(12 | 15 | 1), E(0 | 15 | 0); AB ∥ DE; 1 LE = 1 m; "
      "Mähroboter: Mittelpunkt der kreisförmigen Unterseite (Radius 20 cm) berührt die Fläche, Start P(3,6 | 8 | 0,3), Bewegung entlang der Geraden g durch P "
      "mit Richtungsvektor (12; −4; 1) auf den Rand BC zu")
R1_SK = ("Schrägbild: graues Fünfeck ABCDE, A auf der x₃-Achse (Ursprung), B links vorn, C und D rechts unten, E rechts auf der x₂-Achse; Punkt P im Inneren")
row("2021MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Parallelität zweier Seiten und rechten Winkel eines Vierecks über Vektoren nachweisen", typ_neben="",
    stichwoerter="AE = (0; 15; 0) = 3 · CD mit CD = (0; 5; 0): parallel|CD · DE = (0; 5; 0) · (−12; 0; −1) = 0: rechter Winkel",
    voraussetzungen="Parallelität über Vielfache|Skalarprodukt gleich null",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Figur", skizze=R1_SK, kontext="Rasenfläche / Mähroboter", textumfang="mittel",
    gegeben=R1,
    gesucht="Nachweis, dass AE und CD parallel sind und CD und DE einen rechten Winkel einschließen",
    verfahren="Vektoren AE, CD, DE bilden; Vielfaches und Skalarprodukt prüfen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="AE = (0; 15; 0) = 3 · CD; CD · DE = (0; 5; 0) · (−12; 0; −1) = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="DE mit ED verwechseln (Vorzeichen, hier unerheblich)",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2021MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächenterm eines Vierecks als Rechteck plus rechtwinkliges Dreieck erläutern", typ_neben="",
    stichwoerter="Ansatz |AE| · |DE| + 1/2 · (|AB| − |DE|) · (|AE| − |CD|)|Größe: Inhalt der Rasenfläche|Zerlegung in das Rechteck mit den Seiten AE und DE und das rechtwinklige Dreieck mit den Katheten |AB| − |DE| und |AE| − |CD|",
    voraussetzungen="Fläche eines Trapezes durch Zerlegung|Rechteck- und Dreiecksformel",
    format="Kurzantwort|Begründung", operator="Nennen Sie|Erläutern Sie", antwort="Text",
    material="Figur", skizze=R1_SK, kontext="Rasenfläche / Mähroboter", textumfang="mittel",
    gegeben=R1 + "; Ansatz |AE| · |DE| + 1/2 · (|AB| − |DE|) · (|AE| − |CD|)",
    gesucht="die mit dem Ansatz berechnete Größe und die Erläuterung des Ansatzes",
    verfahren="Fläche in Rechteck und rechtwinkliges Dreieck zerlegen und die Faktoren zuordnen",
    schritte="2", zahlenraum="ganz", einheiten="m²", abhaengig_von="",
    ergebnis="Der Ansatz liefert den Inhalt der Rasenfläche: Rechteck mit den Seitenlängen |AE| und |DE| plus rechtwinkliges Dreieck mit den Katheten |AB| − |DE| und |AE| − |CD| (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Dreieck mit den Katheten |AB| und |AE| ansetzen",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung: Fläche 15 · 12,04 + 1/2 · 6,02 · 10 ≈ 211 m². Schätzung II (Zerlegung erkennen und zuordnen); der amtliche Bereich ist I.")
row("2021MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Parameter aus dem Schnitt zweier Geraden ermitteln", typ_neben="",
    stichwoerter="g: (3,6; 8; 0,3) + λ · (12; −4; 1), BC: (18; 0; 1,5) + μ · (−6; 10; −0,5)|I 12λ + 6μ = 14,4, II 4λ + 10μ = 8, III λ + 0,5μ = 1,2|λ = 1, μ = 0,4: Q(15,6 | 4 | 1,3)",
    voraussetzungen="Gleichsetzen zweier Geraden|lineares Gleichungssystem|Probe in der dritten Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze=R1_SK, kontext="Rasenfläche / Mähroboter", textumfang="mittel",
    gegeben=R1 + "; Kontrolle: Q(15,6 | 4 | 1,3)",
    gesucht="Koordinaten des Punkts Q, in dem g die Strecke BC schneidet",
    verfahren="g und die Gerade BC gleichsetzen, λ aus zwei Gleichungen, dritte als Probe",
    schritte="4", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="12λ + 6μ = 14,4, 4λ + 10μ = 8, λ + 0,5μ = 1,2; aus I und II folgt λ = 1, damit Q(15,6 | 4 | 1,3) (amtlich)",
    zwischenergebnis="μ = 0,4", niveau_geschaetzt="II",
    fehlerquelle="dritte Gleichung nicht prüfen; μ außerhalb [0; 1] nicht bemerken",
    bemerkung="Standardbezug: K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2023-ga-A).")
row("2021MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Schnittwinkel zweier Geraden über das Skalarprodukt berechnen", typ_neben="",
    stichwoerter="cos φ = |(−6; 10; −0,5) · (12; −4; 1)| / (√136,25 · √161)|cos φ ≈ 0,760|φ ≈ 41°",
    voraussetzungen="Winkelformel mit Skalarprodukt und Beträgen",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="Figur", skizze=R1_SK, kontext="Rasenfläche / Mähroboter", textumfang="kurz",
    gegeben=R1 + "; Behauptung: der Winkel, unter dem sich der Roboter dem Rand BC nähert, beträgt etwa 41°",
    gesucht="Nachweis des Winkels",
    verfahren="Winkel zwischen den Richtungsvektoren von g und BC über das Skalarprodukt",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="°", abhaengig_von="",
    ergebnis="cos φ = |(−6; 10; −0,5) · (12; −4; 1)| / (√(36 + 100 + 0,25) · √(144 + 16 + 1)) liefert φ ≈ 41° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Betrag im Zähler weglassen und 139° erhalten",
    bemerkung="Standardbezug: K3 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (40,6°). Typ wiederverwendet (2018-bb-ea). Schätzung I (Winkelformel anwenden); der amtliche Bereich ist II.")
row("2021MgrundlegendBAGLAA2WTR2", "e", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt auf einer Geraden mit vorgegebenem Abstand zu einer zweiten Geraden über eine Skizze und den Sinus berechnen", typ_neben="",
    stichwoerter="Skizze: Rand BC, Gerade g durch Q, Roboterkreis berührt den Rand: Abstand des Mittelpunkts S vom Rand 0,2|rechtwinkliges Dreieck mit Winkel φ bei Q: |QS| = 0,2 / sin φ ≈ 0,306|S = Q − |QS| · (12; −4; 1)/√161 ≈ (15,3 | 4,1 | 1,3)",
    voraussetzungen="Abstand als Radius|Sinus im rechtwinkligen Dreieck|Punkt auf der Geraden über den Einheitsvektor",
    format="Zeichnen|Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze=R1_SK, kontext="Rasenfläche / Mähroboter", textumfang="mittel",
    gegeben=R1 + "; Q(15,6 | 4 | 1,3), Winkel φ ≈ 41°; der Roboter ändert die Richtung, sobald der Rand seiner Unterseite (Radius 0,2) den Rand BC erreicht; S = Position des Mittelpunkts in diesem Moment",
    gesucht="Koordinaten von S mithilfe einer geeigneten Skizze",
    verfahren="|QS| = 0,2/sin φ aus der Skizze, S von Q aus um |QS| entgegen der Bewegungsrichtung",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="2021MgrundlegendBAGLAA2WTR2-1d",
    ergebnis="|QS| = 0,2/sin φ; S = (15,6; 4; 1,3) − 1/√(144 + 16 + 1) · (12; −4; 1) · |QS| ≈ (15,3 | 4,1 | 1,3) (amtlich)",
    zwischenergebnis="|QS| ≈ 0,306", niveau_geschaetzt="III",
    fehlerquelle="S um 0,2 statt um 0,2/sin φ vor Q setzen",
    bemerkung="Standardbezug: K2 III, K3 II, K4 II, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (S ≈ (15,31 | 4,10 | 1,28)).")
# ---- Stochastik WTR 1: Joghurtbecher mit Motiven (a–f, 20 BE)
J1 = ("Joghurtbecher auf Paletten zu je 20 Bechern; unter jedem Deckel genau eines von sechs Motiven; gegenwärtig wird jedes Motiv zufällig "
      "(je 1/6) ausgewählt; drei Becher werden nacheinander geöffnet")
row("2021MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen", typ_neben="",
    stichwoerter="Motiv 1 im ersten und dritten, nicht im zweiten Becher|1/6 · 5/6 · 1/6 = 5/216",
    voraussetzungen="Pfadregel|Gegenwahrscheinlichkeit 5/6",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Joghurtbecher / Sammelmotive", textumfang="mittel",
    gegeben=J1,
    gesucht="Wahrscheinlichkeit, dass sich nur im ersten und dritten Becher das Motiv 1 befindet",
    verfahren="Produkt der drei Einzelwahrscheinlichkeiten",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="(1/6)² · 5/6 = 5/216 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="„nur“ überlesen und (1/6)² rechnen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2019-ea-A).")
row("2021MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="(6 · 5 · 4)/6³|Zähler: geordnete Auswahl dreier verschiedener Motive|drei unterschiedliche Motive in den drei Bechern",
    voraussetzungen="Laplace-Wahrscheinlichkeit als Quotient|Zählprinzip ohne Wiederholung",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Joghurtbecher / Sammelmotive", textumfang="kurz",
    gegeben=J1 + "; Term (6 · 5 · 4)/6³",
    gesucht="ein Ereignis im Sachzusammenhang mit dieser Wahrscheinlichkeit",
    verfahren="Zähler als Anzahl der Folgen mit lauter verschiedenen Motiven deuten",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Die drei Becher enthalten drei unterschiedliche Motive (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Term als „Motive 1, 2, 3 in dieser Reihenfolge“ deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2026-ea-A).")
J2 = ("geplante Änderung: Motiv 6 künftig mit Wahrscheinlichkeit p; X = Anzahl der Becher mit Motiv 6 auf einer Palette (n = 20); die Abbildung zeigt "
      "für einen Wert von p die Wahrscheinlichkeitsverteilung von X")
J2_SK = ("Säulendiagramm P(X = k) für k = 0 bis 20 ohne y-Skala: Säulen bei 0 (mittel), 1 (hoch), 2 (höchste), 3 (mittel), 4 (klein), 5 und 6 (sehr klein), ab 7 nichts")
row("2021MgrundlegendBStochastikWTR1", "c", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussagen über kumulierte Wahrscheinlichkeit und Trefferwahrscheinlichkeit aus dem Säulendiagramm einer Binomialverteilung beurteilen", typ_neben="",
    stichwoerter="I: P(X < 2) > 50 %: die Säulen zu k = 0 und 1 machen nicht mehr als die Hälfte der Gesamtfläche aus – falsch|II: p > 1/6: dann wäre E(X) > 20/6 ≈ 3,3 und die Säule zu k = 2 nicht die höchste – falsch",
    voraussetzungen="Säulenhöhen als Wahrscheinlichkeiten, Summe 1|Maximum der Verteilung nahe n · p",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Diagramm", skizze=J2_SK, kontext="Joghurtbecher / Sammelmotive", textumfang="mittel",
    gegeben=J1 + "; " + J2 + "; Aussage I: P(weniger als zwei Becher mit Motiv 6) > 50 %; Aussage II: p > 1/6",
    gesucht="Beurteilung beider Aussagen",
    verfahren="Säulenanteile für k < 2 abschätzen; Lage des Maximums mit n · p vergleichen",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Aussage I ist falsch, da der Flächenanteil der Säulen zu k < 2 nicht größer als 50 % ist; Aussage II ist falsch, da für p > 1/6 wegen 20 · 1/6 ≈ 3,3 die Säule zu k = 2 nicht die höchste wäre (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Aussage II mit der Säule zu k = 2 statt mit dem Erwartungswert 20p begründen wollen",
    bemerkung="Standardbezug: K1 II, K3 I, K4 II, K6 II. AB amtlich: II. Amtlich; eigene Rechnung: für p = 0,1 ist P(X < 2) ≈ 0,39 und das Maximum bei k = 2.")
J3 = ("nach der Änderung: Motiv 6 mit Wahrscheinlichkeit 1/36, die anderen fünf Motive gleich wahrscheinlich (je 7/36); Paletten zu 20 Bechern")
row("2021MgrundlegendBStochastikWTR1", "d", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen", typ_neben="",
    stichwoerter="Term (m über n) · (35/36)ⁿ · (1/36)^(40−n) + (35/36)⁴⁰|zwei Paletten: m = 40, n = 39|P(X = 39) + P(X = 40) für X = Anzahl der Becher ohne Motiv 6 unter 40: mindestens 39 Becher ohne Motiv 6",
    voraussetzungen="Bernoulli-Term (n über k) pᵏ(1 − p)^(n−k)|Summe zweier Einzelwahrscheinlichkeiten als Mindestens-Ereignis",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Joghurtbecher / Sammelmotive", textumfang="mittel",
    gegeben=J3 + "; Term (m über n) · (35/36)ⁿ · (1/36)^(40−n) + (35/36)⁴⁰",
    gesucht="je ein Wert von m und n, sodass der Term eine Wahrscheinlichkeit im Sachzusammenhang angibt; das zugehörige Ereignis",
    verfahren="Exponentensumme 40 als zwei Paletten lesen, zweiten Summanden als k = 40 erkennen, ersten als k = 39",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="m = 40, n = 39; Ereignis: auf zwei Paletten befinden sich mindestens 39 Becher, die nicht das Motiv 6 enthalten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="n = 40 wählen und den Binomialkoeffizienten (40 über 40) = 1 übersehen, sodass der Term doppelt zählt",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2026-ea-A).")
row("2021MgrundlegendBStochastikWTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert der Kosten pro Stück aus einer Wahrscheinlichkeitstabelle berechnen", typ_neben="",
    stichwoerter="Motive 1–5 je 7/36, Motiv 6 1/36|Kosten 4, 4, 2, 2, 2, 9 Cent|7/36 · (2 · 4 + 3 · 2) + 1/36 · 9 ≈ 3,0 Cent",
    voraussetzungen="Erwartungswert als gewichtete Summe|fehlende Wahrscheinlichkeiten aus der Summe 1",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle: Motiv 1 bis 6, Zeile Wahrscheinlichkeit (nur bei Motiv 6: 1/36), Zeile Kosten pro Becher 4, 4, 2, 2, 2, 9 Cent", kontext="Joghurtbecher / Sammelmotive", textumfang="mittel",
    gegeben=J3 + "; Kosten der Prämien je Becher: Motiv 1 und 2 je 4 Cent, Motiv 3 bis 5 je 2 Cent, Motiv 6 9 Cent",
    gesucht="mittlere Kosten pro Becher",
    verfahren="Wahrscheinlichkeiten 7/36 ergänzen, Erwartungswert der Kosten bilden",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="Cent", abhaengig_von="",
    ergebnis="7/36 · (2 · 4 ct + 3 · 2 ct) + 1/36 · 9 ct ≈ 3,0 ct (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die fünf Motive mit je 1/6 statt 7/36 gewichten",
    bemerkung="Standardbezug: K2 I, K3 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (107/36 ≈ 2,97).")
row("2021MgrundlegendBStochastikWTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Bedingte Wahrscheinlichkeit einer Teilgruppe aus totaler Wahrscheinlichkeit und der anderen Teilgruppe berechnen", typ_neben="",
    stichwoerter="1/5 farbig, 4/5 schwarz-weiß|P(Motiv 6) = 1/5 · x + 4/5 · 1/48 = 1/36|x = 5 · (1/36 − 4/5 · 1/48) = 1/18",
    voraussetzungen="totale Wahrscheinlichkeit über zwei Zweige|lineare Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Joghurtbecher / Sammelmotive", textumfang="mittel",
    gegeben=J3 + "; 1/5 der Becher farbig, die übrigen schwarz-weiß; unter den schwarz-weißen Bechern hat Motiv 6 die Wahrscheinlichkeit 1/48",
    gesucht="Wahrscheinlichkeit, dass ein zufällig gewählter farbiger Becher das Motiv 6 enthält",
    verfahren="Totale Wahrscheinlichkeit 1/36 als gewichtete Summe ansetzen und nach dem unbekannten Zweig auflösen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/5 · x + 4/5 · 1/48 = 1/36 ⇔ x = 5 · (1/36 − 4/5 · 1/48) = 1/18 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="1/36 als Wahrscheinlichkeit unter den farbigen Bechern ansetzen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt.")
# ---- Stochastik WTR 2: Smartphone-Spiel (a–g, 20 BE); Landesheft 2021-be-gk 4 a, c, d, g, h, i vorgemerkt
S1 = "Smartphone-Spiel: jeden Sonntag zehn Versuche, je Versuch mit 40 % ein Stern; X = Anzahl der Sterne bei zehn Versuchen, binomialverteilt (n = 10, p = 0,4)"
row("2021MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", typ_neben="",
    stichwoerter="P(X > 6) = 1 − P(X ≤ 6) ≈ 5 %",
    voraussetzungen="Gegenereignis|kumulierte Binomialverteilung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=S1,
    gesucht="Wahrscheinlichkeit, bei zehn Versuchen mehr als sechs Sterne zu gewinnen",
    verfahren="1 − P(X ≤ 6) mit dem Rechner",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(X > 6) ≈ 5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≥ 6) rechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,0548). Typ wiederverwendet (2019-be-gk). Landesheft 2021-be-gk 4 a (abgewandelt: dort zusätzlich ein zweites Ereignis; dort vorgemerkt).")
row("2021MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Aussage über den Ausgleich eines beobachteten Anteils bei weiteren Versuchen über die Unabhängigkeit beurteilen", typ_neben="",
    stichwoerter="Aussage: nach dreimal acht Sternen ist die Chance auf acht Sterne deutlich kleiner|falsch: die Wahrscheinlichkeit je Versuch ist bei allen Versuchen gleich",
    voraussetzungen="Unabhängigkeit der Versuche|konstante Trefferwahrscheinlichkeit",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Smartphone-Spiel", textumfang="mittel",
    gegeben=S1 + "; Aussage eines Spielers: nach acht Sternen an drei Sonntagen sei die Chance auf acht Sterne an diesem Sonntag deutlich kleiner",
    gesucht="Beurteilung der Aussage",
    verfahren="Konstanz der Trefferwahrscheinlichkeit und Unabhängigkeit der Sonntage nennen",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist falsch, da die Wahrscheinlichkeit dafür, einen Stern zu gewinnen, bei allen Versuchen gleich groß ist (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="mit der Seltenheit von viermal acht Sternen argumentieren",
    bemerkung="Standardbezug: K1 I, K3 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2017-ea-A). Landesheft 2021-be-gk 4 c (wortgleich; dort vorgemerkt, Schätzung dort II – Vorrang des Amtlichen, die Landeszeile zieht im Abgleichlauf nach).")
row("2021MgrundlegendBStochastikWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Fehlerwahrscheinlichkeit einer Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden", typ_neben="",
    stichwoerter="P(X = 5) = B(10; 0,4; 5) ≈ 0,20|Y = Anzahl der Spieler mit fünf Sternen, B(4; 0,20)|P(Y = 2) ≈ 15 %",
    voraussetzungen="Einzelwahrscheinlichkeit der Binomialverteilung|zweistufige Binomialverteilung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=S1 + "; vier Spieler nutzen an einem Sonntag je zehn Versuche",
    gesucht="Wahrscheinlichkeit, dass zwei der vier Spieler jeweils fünf Sterne gewinnen",
    verfahren="P(X = 5) als Trefferwahrscheinlichkeit einer B(4; p)-Verteilung, dann P(Y = 2)",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(X = 5) ≈ 0,20; mit Y = Anzahl der Spieler mit fünf Sternen gilt P(Y = 2) ≈ 15 % (amtlich)",
    zwischenergebnis="P(X = 5) ≈ 0,2007", niveau_geschaetzt="II",
    fehlerquelle="P(X = 5)² rechnen und die Auswahl der zwei Spieler (Faktor 6) sowie die anderen beiden vergessen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,1544). Typ wiederverwendet (2023-ea-B). Landesheft 2021-be-gk 4 d (abgewandelt: dort „genau zwei … genau fünf“; dort vorgemerkt).")
row("2021MgrundlegendBStochastikWTR2", "d", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Trefferwahrscheinlichkeit aus einer kumulierten Wahrscheinlichkeit auf ganze Prozent durch Probieren ermitteln", typ_neben="",
    stichwoerter="P(X ≤ 3) ≈ 62 % gesucht p|p = 0,32: 59,6 %; p = 0,31: 62,3 %|p ≈ 31 %",
    voraussetzungen="kumulierte Binomialverteilung mit dem Rechner|systematisches Probieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Smartphone-Spiel", textumfang="mittel",
    gegeben=S1 + "; nach einer Änderung von p beträgt P(höchstens drei Sterne bei zehn Versuchen) etwa 62 %",
    gesucht="die geänderte Wahrscheinlichkeit p auf ganze Prozent",
    verfahren="P(X ≤ 3) für Werte von p mit dem Rechner berechnen, bis etwa 62 % erreicht sind",
    schritte="3", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(X ≤ 3) ≈ 59,6 % für p = 0,32 und ≈ 62,3 % für p = 0,31; die Wahrscheinlichkeit müsste also etwa 31 % betragen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="p aus E(X) = 3 zu 30 % schließen",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,5956 und 0,6234).")
S2 = "Bonuspunkte beim täglichen Start des Spiels: 10 Punkte mit 50 %, 20 mit 40 %, 50 mit 10 %"
row("2021MgrundlegendBStochastikWTR2", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen", typ_neben="",
    stichwoerter="von Tag zu Tag weniger: 50, dann 20, dann 10|0,1 · 0,4 · 0,5 = 2 %",
    voraussetzungen="einzig mögliche fallende Folge erkennen|Pfadregel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle: Bonuspunkte 10, 20, 50 mit Wahrscheinlichkeiten 50 %, 40 %, 10 %", kontext="Smartphone-Spiel", textumfang="mittel",
    gegeben=S2 + "; ein Spieler startet an drei aufeinanderfolgenden Tagen",
    gesucht="Wahrscheinlichkeit, dass er von Tag zu Tag weniger Bonuspunkte erhält",
    verfahren="Folge 50, 20, 10 als einzigen Pfad, Produkt bilden",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,1 · 0,4 · 0,5 = 2 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Reihenfolgen mit gleichen Punktzahlen mitzählen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2019-ea-A). Landesheft 2021-be-gk 4 g (wortgleich; dort vorgemerkt).")
row("2021MgrundlegendBStochastikWTR2", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit einer Summe über alle Ergebnisfolgen mit Reihenfolgen berechnen", typ_neben="",
    stichwoerter="80 Punkte an vier Tagen: 50 + 10 + 10 + 10 (vier Reihenfolgen) oder 20 + 20 + 20 + 20|4 · 0,1 · 0,5³ + 0,4⁴ ≈ 8 %",
    voraussetzungen="Zerlegungen der Summe finden|Anzahl der Reihenfolgen|Pfadregel und Summenregel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle: Bonuspunkte 10, 20, 50 mit Wahrscheinlichkeiten 50 %, 40 %, 10 %", kontext="Smartphone-Spiel", textumfang="kurz",
    gegeben=S2 + "; ein Spieler startet an vier Tagen",
    gesucht="Wahrscheinlichkeit für insgesamt 80 Bonuspunkte",
    verfahren="Beide Zerlegungen von 80 mit ihren Reihenfolgen zusammenzählen",
    schritte="3", zahlenraum="dezimal|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="4 · 0,1 · 0,5³ + 0,4⁴ ≈ 8 % (amtlich)",
    zwischenergebnis="0,05 + 0,0256 = 0,0756", niveau_geschaetzt="II",
    fehlerquelle="die Zerlegung 20 + 20 + 20 + 20 oder die vier Reihenfolgen übersehen",
    bemerkung="Standardbezug: K1 I, K2 II, K3 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,0756). Typ wiederverwendet (2021-be-gk). Landesheft 2021-be-gk 4 h (wortgleich; dort vorgemerkt).")
row("2021MgrundlegendBStochastikWTR2", "g", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Zwei Wahrscheinlichkeiten einer Verteilung aus dem Erwartungswert und der Summe 1 bestimmen", typ_neben="",
    stichwoerter="Erwartungswert je Tag 3000/200 = 15|10x + 20 · (0,9 − x) + 50 · 0,1 = 15 ⇔ −10x = −8 ⇔ x = 0,8|P(10) = 80 %, P(20) = 10 %",
    voraussetzungen="Erwartungswert als gewichtete Summe|Summe der Wahrscheinlichkeiten 1|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle: Bonuspunkte 10, 20, 50 mit Wahrscheinlichkeiten 50 %, 40 %, 10 %", kontext="Smartphone-Spiel", textumfang="mittel",
    gegeben=S2 + "; die Wahrscheinlichkeiten für 10 und 20 werden so geändert, dass die Spieler in 200 Tagen im Mittel 3000 Bonuspunkte erhalten",
    gesucht="die beiden geänderten Wahrscheinlichkeiten",
    verfahren="Erwartungswert 15 je Tag ansetzen, P(20) = 0,9 − P(10) einsetzen, lineare Gleichung lösen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="x · 10 + (0,9 − x) · 20 + 0,1 · 50 = 3000/200 ⇔ −10x = −8 ⇔ x = 0,8; die geänderte Wahrscheinlichkeit für 10 Bonuspunkte beträgt 80 %, die für 20 Bonuspunkte 10 % (amtlich)",
    zwischenergebnis="Erwartungswert 15", niveau_geschaetzt="III",
    fehlerquelle="3000 als Erwartungswert je Tag nehmen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2021-be-gk). Landesheft 2021-be-gk 4 i (wortgleich; dort vorgemerkt, Schätzung dort II – Vorrang des Amtlichen, die Landeszeile zieht im Abgleichlauf nach).")
# ---- Stochastik WTR 3: Gehaltszufriedenheit und Befragung (a–g, 20 BE)
W1 = ("Großes Unternehmen: 77 % aller Beschäftigten sind mit ihrem Gehalt zufrieden; 5 % aller Beschäftigten sind in der Werbeabteilung und nicht zufrieden; "
      "12 % aller Beschäftigten gehören zur Werbeabteilung")
row("2021MgrundlegendBStochastikWTR3", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="W: Werbeabteilung, Z: zufrieden|W∩Z 7 %, W∩¬Z 5 %, ¬W∩Z 70 %, ¬W∩¬Z 18 %|Ränder 12 %, 88 %, 77 %, 23 %",
    voraussetzungen="Vierfeldertafel mit Randsummen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="mittel",
    gegeben=W1,
    gesucht="vollständig ausgefüllte Vierfeldertafel",
    verfahren="Randwerte eintragen, Felder durch Differenzen ergänzen",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="W∩Z 7 %, W∩¬Z 5 %, ¬W∩Z 70 %, ¬W∩¬Z 18 %; Ränder W 12 %, ¬W 88 %, Z 77 %, ¬Z 23 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="5 % als bedingten Anteil innerhalb der Werbeabteilung lesen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")
row("2021MgrundlegendBStochastikWTR3", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Anteile aus der Vierfeldertafel vergleichen", typ_neben="",
    stichwoerter="Anteil Unzufriedener in der Werbeabteilung 5 %/12 % ≈ 42 %|im übrigen Unternehmen 18 %/88 % ≈ 20 %|größer",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient aus der Tafel",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=W1,
    gesucht="ob der Anteil der Unzufriedenen in der Werbeabteilung größer ist als im übrigen Unternehmen",
    verfahren="Beide bedingten Anteile aus der Vierfeldertafel bilden und vergleichen",
    schritte="2", zahlenraum="Prozent|Bruch", einheiten="", abhaengig_von="2021MgrundlegendBStochastikWTR3-1a",
    ergebnis="In der Werbeabteilung 5 %/12 % ≈ 42 %, im übrigen Unternehmen 18 %/88 % ≈ 20 %: der Anteil ist in der Werbeabteilung größer (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="5 % mit 18 % vergleichen (absolute statt bedingte Anteile)",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")
row("2021MgrundlegendBStochastikWTR3", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X: Anzahl der Zufriedenen unter 500, B(500; 0,77)|P(X > 400) ≈ 5 %",
    voraussetzungen="Binomialmodell|kumulierte Wahrscheinlichkeit mit dem Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=W1 + "; 500 zufällig ausgewählte Beschäftigte",
    gesucht="Wahrscheinlichkeit, dass mehr als 400 davon mit ihrem Gehalt zufrieden sind",
    verfahren="1 − P(X ≤ 400) für B(500; 0,77)",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(X > 400) ≈ 5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≥ 400) rechnen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,048). Typ wiederverwendet (2026-ga-B).")
row("2021MgrundlegendBStochastikWTR3", "d", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="1 − Σ_(i=0)^400 (600 über i) · 0,23ⁱ · 0,77^(600−i)|Summe = P(höchstens 400 Unzufriedene unter 600), Gegenereignis: mehr als 400 nicht zufrieden",
    voraussetzungen="Bernoulli-Term mit p = 0,23 als „nicht zufrieden“ lesen|Gegenereignis",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=W1 + "; Term 1 − Σ_(i=0)^400 (600 über i) · 0,23ⁱ · 0,77^(600−i)",
    gesucht="Bedeutung des Terms im Sachzusammenhang",
    verfahren="Erfolgswahrscheinlichkeit 0,23 als „nicht zufrieden“ erkennen, Summe als kumulierte Wahrscheinlichkeit, 1 − … als Gegenereignis",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Der Term gibt die Wahrscheinlichkeit dafür an, dass unter 600 zufällig ausgewählten Beschäftigten mehr als 400 mit ihrem Gehalt nicht zufrieden sind (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="0,23 als Zufriedenheitsanteil lesen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2026-ga-B).")
W2 = ("Befragung zur Absicht, das Unternehmen in zwölf Monaten zu verlassen: 70 % erhalten Frage A (Absicht, das Unternehmen zu verlassen), 30 % Frage B (Absicht zu bleiben); "
      "nur die Person kennt ihre Frage und antwortet wahrheitsgemäß; Baumdiagramm mit A (Ja mit x, Nein mit y) und B")
W2_SK = "Baumdiagramm: Wurzel, Äste zu A und B (Kästchen); von A Äste zu Ja (Beschriftung x) und Nein (Beschriftung y); von B keine weiteren Äste"
row("2021MgrundlegendBStochastikWTR3", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Astwahrscheinlichkeit im Baumdiagramm einer Befragung im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="y am Ast A → Nein|Anteil derjenigen mit Frage A, die mit Nein antworten (nicht gehen wollen)",
    voraussetzungen="Astwahrscheinlichkeit als bedingter Anteil",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Diagramm", skizze=W2_SK, kontext="Unternehmen / Befragung", textumfang="lang",
    gegeben=W2,
    gesucht="Bedeutung von y im Sachzusammenhang",
    verfahren="y als bedingten Anteil auf der Stufe Frage A lesen",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="y gibt für die Befragten, denen die Frage A zugeordnet wurde, den Anteil derjenigen an, die mit „Nein“ geantwortet haben (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="y als Anteil aller Nein-Antworten deuten",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich.")
row("2021MgrundlegendBStochastikWTR3", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil einer Eigenschaft aus einer Randomized-Response-Befragung über die totale Wahrscheinlichkeit nachweisen", typ_neben="",
    stichwoerter="x = Anteil der Gehwilligen|P(Ja) = 0,7 · x + 0,3 · (1 − x) = 1024/2700|0,4x = 1024/2700 − 0,3 ⇔ x ≈ 20 %",
    voraussetzungen="totale Wahrscheinlichkeit über beide Fragen|Ja bei B bedeutet Bleiben, also Anteil 1 − x|lineare Gleichung",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="Diagramm", skizze=W2_SK, kontext="Unternehmen / Befragung", textumfang="lang",
    gegeben=W2 + "; von 2700 Beschäftigten antworten 1024 mit Ja; der Anteil der Gehwilligen ist in beiden Fragegruppen gleich",
    gesucht="Nachweis, dass etwa 20 % der Beschäftigten das Unternehmen verlassen wollen",
    verfahren="Ja-Anteil als 0,7 · x + 0,3 · (1 − x) ansetzen und nach x lösen",
    schritte="3", zahlenraum="dezimal|Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,7 · x + 0,3 · (1 − x) = 1024/2700 ⇔ 0,4x = 1024/2700 − 0,3 liefert x ≈ 20 % (amtlich)",
    zwischenergebnis="1024/2700 ≈ 0,379", niveau_geschaetzt="III",
    fehlerquelle="Ja bei Frage B ebenfalls als Gehwillige zählen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (0,198).")
row("2021MgrundlegendBStochastikWTR3", "g", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(gehen | Ja) = P(A ∩ Ja ∩ gehen)/P(Ja) = 0,7 · 0,2 / (1024/2700) ≈ 37 %",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient|Ja-Anteil aus f",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=W2_SK, kontext="Unternehmen / Befragung", textumfang="kurz",
    gegeben=W2 + "; 1024 von 2700 antworten Ja; Anteil der Gehwilligen 20 %; eine Person mit Antwort Ja wird zufällig ausgewählt",
    gesucht="Wahrscheinlichkeit, dass sie das Unternehmen verlassen will",
    verfahren="Pfad A → Ja (gehen) durch die Gesamtwahrscheinlichkeit für Ja teilen",
    schritte="2", zahlenraum="dezimal|Bruch|Prozent", einheiten="", abhaengig_von="2021MgrundlegendBStochastikWTR3-1f",
    ergebnis="0,7 · 0,2 / (1024/2700) ≈ 37 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="alle Gehwilligen (20 %) durch den Ja-Anteil teilen, obwohl Gehwillige mit Frage B Nein antworten",
    bemerkung="Standardbezug: K3 II, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,369). Typ wiederverwendet (2024-ea-B).")

NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Hochpunkt mit vorgegebenen Koordinaten und waagerechte Tangente im Ursprung rechnerisch nachweisen", "Analysis", "Kurvenuntersuchung",
     "Mit erster und zweiter Ableitung einen vorgegebenen Punkt als Hochpunkt bestätigen und über f'(0) = 0 zeigen, dass die Tangente im Ursprung parallel zur x-Achse verläuft.", "2021MgrundlegendBAnalysisWTR-1a"),
    ("Gerade durch die beiden Wendepunkte aufstellen und parallele Gerade mit genau einem gemeinsamen Punkt einzeichnen", "Analysis", "Kurvenuntersuchung",
     "Die Wendestellen über die zweite Ableitung berechnen, die Gerade durch die Wendepunkte angeben und in der Abbildung eine dazu parallele Gerade einzeichnen, die den Graphen in einem Intervall genau einmal trifft.", "2021MgrundlegendBAnalysisWTR-1b"),
    ("Parameter einer Schar aus einem vorgegebenen Punkt auf dem Graphen bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameterwert bestimmen, für den ein vorgegebener Punkt auf dem Graphen der Scharfunktion liegt, durch Einsetzen und Lösen einer linearen Gleichung.", "2021MgrundlegendBAnalysisWTR-1d"),
    ("Parameter für genau zwei gemeinsame Punkte von Graph und Scharparabel über die Diskriminante bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Schnittgleichung zweier Graphen faktorisieren und den Parameterwert bestimmen, für den der quadratische Faktor eine doppelte Lösung hat, sodass genau zwei gemeinsame Punkte entstehen.", "2021MgrundlegendBAnalysisWTR-1e"),
    ("Integralwert: Nullwert eines Integrals über eine Differenzfunktion mit drei Schnittstellen als Flächengleichheit deuten", "Analysis", "Flächeninhalt durch Integration",
     "Drei Lösungen einer Schnittgleichung als gemeinsame Punkte und den Integralwert null der Differenzfunktion als zwei gleich große Flächenstücke auf verschiedenen Seiten deuten.", "2021MgrundlegendBAnalysisWTR-1f"),
    ("Koordinaten eines Punktes des Ratengraphen im Sachzusammenhang deuten", "Analysis", "Ableitung und Änderungsrate",
     "Die beiden Koordinaten eines Punktes auf dem Graphen einer momentanen Änderungsrate als Zeitpunkt und Rate mit Einheiten im Sachzusammenhang interpretieren.", "2021MgrundlegendBAnalysisWTR-2a"),
    ("Bestandsänderung grafisch als Fläche unter dem Ratengraphen bestimmen", "Analysis", "Rekonstruktion von Beständen",
     "Die Änderung eines Bestands in einem Zeitraum als Fläche unter dem abgebildeten Graphen der Änderungsrate durch Auszählen der Kästchen näherungsweise bestimmen.", "2021MgrundlegendBAnalysisWTR-2c"),
    ("Bestand nach einem Zeitraum aus Anfangsbestand und Integral der Änderungsrate berechnen", "Analysis", "Rekonstruktion von Beständen",
     "Den Bestand am Ende eines Zeitraums als Summe aus Anfangsbestand und bestimmtem Integral der Änderungsrate berechnen.", "2021MgrundlegendBAnalysisWTR-2d"),
    ("Übergangsprozess: Vorherige Verteilung über die inverse Matrix berechnen und prozentuale Abnahme einer Komponente angeben", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Mit der gegebenen inversen Übergangsmatrix die Verteilung des Vormonats berechnen und die prozentuale Abnahme einer Komponente beim Übergang angeben.", "2021MgrundlegendBAGLAA1WTR-1d"),
    ("Übergangsprozess: Geänderte Übergangsmatrix aus zwei Vorschlägen nach dem beschriebenen Wechselverhalten auswählen und begründen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Von zwei vorgeschlagenen Übergangsmatrizen diejenige auswählen, deren Spalten das im Text beschriebene geänderte Wechselverhalten wiedergeben, und die Auswahl an den Einträgen begründen.", "2021MgrundlegendBAGLAA1WTR-1e"),
    ("Ebene Figur: Parallelität zweier Seiten und rechten Winkel eines Vierecks über Vektoren nachweisen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Für ein durch Koordinaten gegebenes Viereck zwei Seiten über ein Vielfaches als parallel und zwei Seiten über das Skalarprodukt null als senkrecht nachweisen.", "2021MgrundlegendBAGLAA2WTR2-1a"),
    ("Ebene Figur: Flächenterm eines Vierecks als Rechteck plus rechtwinkliges Dreieck erläutern", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Einen vorgegebenen Term aus Streckenlängen als Flächeninhalt eines Vierecks deuten, das sich in ein Rechteck und ein rechtwinkliges Dreieck zerlegen lässt.", "2021MgrundlegendBAGLAA2WTR2-1b"),
    ("Punkt auf einer Geraden mit vorgegebenem Abstand zu einer zweiten Geraden über eine Skizze und den Sinus berechnen", "Analytische Geometrie", "Abstände",
     "Den Punkt einer Geraden bestimmen, der von einer zweiten, sie schneidenden Geraden einen vorgegebenen Abstand hat, indem aus einer Skizze die Entfernung zum Schnittpunkt über den Sinus des Schnittwinkels gewonnen wird.", "2021MgrundlegendBAGLAA2WTR2-1e"),
    ("Aussagen über kumulierte Wahrscheinlichkeit und Trefferwahrscheinlichkeit aus dem Säulendiagramm einer Binomialverteilung beurteilen", "Stochastik", "Binomialverteilung",
     "Anhand des abgebildeten Säulendiagramms einer Binomialverteilung eine Aussage über eine kumulierte Wahrscheinlichkeit über Flächenanteile und eine Aussage über die Trefferwahrscheinlichkeit über die Lage des Maximums beurteilen.", "2021MgrundlegendBStochastikWTR1-1c"),
    ("Erwartungswert der Kosten pro Stück aus einer Wahrscheinlichkeitstabelle berechnen", "Stochastik", "Kenngrößen von Verteilungen",
     "Aus einer Tabelle mit Wahrscheinlichkeiten und Kosten je Ausgang die mittleren Kosten als Erwartungswert berechnen, wobei fehlende Wahrscheinlichkeiten aus der Summe 1 ergänzt werden.", "2021MgrundlegendBStochastikWTR1-1e"),
    ("Bedingte Wahrscheinlichkeit einer Teilgruppe aus totaler Wahrscheinlichkeit und der anderen Teilgruppe berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Aus der Gesamtwahrscheinlichkeit eines Merkmals, den Anteilen zweier Teilgruppen und der bedingten Wahrscheinlichkeit in einer Teilgruppe die bedingte Wahrscheinlichkeit in der anderen Teilgruppe über eine lineare Gleichung berechnen.", "2021MgrundlegendBStochastikWTR1-1f"),
    ("Trefferwahrscheinlichkeit aus einer kumulierten Wahrscheinlichkeit auf ganze Prozent durch Probieren ermitteln", "Stochastik", "Binomialverteilung",
     "Den Parameter p einer Binomialverteilung mit dem Rechner durch systematisches Probieren so bestimmen, dass eine vorgegebene kumulierte Wahrscheinlichkeit näherungsweise erreicht wird.", "2021MgrundlegendBStochastikWTR2-1d"),
    ("Astwahrscheinlichkeit im Baumdiagramm einer Befragung im Sachzusammenhang deuten", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Eine als Variable beschriftete Astwahrscheinlichkeit eines Baumdiagramms als bedingten Anteil innerhalb einer Befragtengruppe beschreiben.", "2021MgrundlegendBStochastikWTR3-1e"),
    ("Anteil einer Eigenschaft aus einer Randomized-Response-Befragung über die totale Wahrscheinlichkeit nachweisen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Bei einer Befragung mit zwei zufällig zugeteilten, komplementären Fragen den Anteil der Merkmalsträger aus dem beobachteten Ja-Anteil über die totale Wahrscheinlichkeit als lineare Gleichung bestimmen.", "2021MgrundlegendBStochastikWTR3-1f"),
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


def pruefe_vorrang(z, a):
    """Vorrang des Amtlichen (v1.5, Kern § 5): eine aus einer Landeszeile übernommene
    Schätzung darf nicht neben dem amtlichen Bereich liegen."""
    amt = amtlich_von(z)
    if "aus der Landeszeile übernommen" in z["bemerkung"] and amt and ORD.get(z["niveau_geschaetzt"], 0) != amt:
        a(False, f"{z['id']}: übernommene Schätzung {z['niveau_geschaetzt']} neben dem amtlichen Bereich "
                 f"{[k for k, v in ORD.items() if v == amt][0]} – Vorrang des Amtlichen (Kern § 5), Schätzung korrigieren")


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
            pruefe_vorrang(z, a)
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
    # Die Schwelle gilt für jeden Stapel gleich (v1.5; die Überschreibung je Stapel
    # aus v1.4 ist zurückgebaut). Vorrang des Amtlichen (Kern § 5): übernommene
    # Schätzungen müssen den amtlichen Bereich treffen.
    a("eichung_mindestens" not in KONFIG, "KONFIG: eichung_mindestens je Stapel gibt es seit v1.5 nicht mehr")
    for z in ZEILEN:
        pruefe_vorrang(z, a)
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
