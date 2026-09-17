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
    "stapel": "2020-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2020MgrundlegendBAnalysisWTR1": 35, "2020MgrundlegendBAnalysisWTR2": 35, "2020MgrundlegendBAGLAA1WTR": 20,
        "2020MgrundlegendBAGLAA2WTR": 20, "2020MgrundlegendBStochastikWTR1": 20, "2020MgrundlegendBStochastikWTR2": 20,
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
# Stapel 2020-ga-B (WTR-Zweig; Reserve, geöffnet 17.09.2026 in Auftrag C Teil 2 wegen
# der sieben Landesheftverweise von 2020-be-gk 4.2 a–g auf Stochastik WTR 1). Sechs
# Dateien, Standardbezug mit Spalte Anforderungsbereich; Analysis-Dateien mit 35 BE,
# die übrigen mit 20 BE. AG/LA (A2) Aufgabe 2 ohne Teilaufgabenbuchstaben (id …-2).
# ---- Analysis WTR 1: Logo eines Anglergeschäfts (Fisch), eine Aufgabe a–i, 35 BE
F1 = ("Logo eines Geschäfts für Anglerbedarf: untere Begrenzungslinie des Fischs u(x) = 1/8 x³, obere Begrenzungslinie "
      "v(x) = 1/4 x² · (4 − x) (beide in IR definiert), Wasseroberfläche y = 5/4; die obere Spitze der Schwanzflosse liegt auf der "
      "Wasseroberfläche, die Strecke zwischen oberer und unterer Spitze der Schwanzflosse steht senkrecht dazu")
F1_SK = ("Logo ohne Koordinatensystem: Fisch aus zwei Bögen (unten der Graph von u, oben der von v) von der Schwanzflosse links unten "
         "bis zur Kopfspitze rechts oben, die Schwanzflosse mit senkrechter Kante, obere Spitze auf der Wasserlinie; das Wasser als "
         "grau unterlegtes Rechteck, der Fischteil unter Wasser dunkelgrau")
row("2020MgrundlegendBAnalysisWTR1", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Gemeinsame Punkte zweier Graphen als einzige durch Ausklammern nachweisen",
    typ_neben="Ableitung eines ganzrationalen Produkts durch Ausmultiplizieren nachweisen",
    stichwoerter="u(x) = v(x) ⇔ 1/8 x³ = −1/4 x³ + x² ⇔ x² · (3/8 x − 1) = 0|x = 0 oder x = 8/3; u(0) = 0, u(8/3) = 64/27|v(x) = −1/4 x³ + x², v'(x) = −3/4 x² + 2x",
    voraussetzungen="Gleichsetzen und Ausklammern|Produkt gleich null|Potenzregel",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="Figur", skizze=F1_SK, kontext="Logo / Anglerbedarf", textumfang="mittel",
    gegeben=F1 + "; Behauptungen: P(0 | 0) und Q(8/3 | 64/27) sind die einzigen gemeinsamen Punkte; v'(x) = −3/4 x² + 2x",
    gesucht="Nachweis beider Behauptungen",
    verfahren="u = v ausmultiplizieren, x² ausklammern, Lösungen und Funktionswerte angeben; v ausmultiplizieren und ableiten",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="u(x) = v(x) ⇔ x² · (3/8 x − 1) = 0 ⇔ x = 0 ∨ x = 8/3, also P(0 | 0) und Q(8/3 | 64/27); v(x) = −1/4 x³ + x² liefert v'(x) = −3/4 x² + 2x (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="durch x² dividieren und die Lösung 0 verlieren",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAnalysisWTR1", "b", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen", typ_neben="",
    stichwoerter="v''(x) = −3/2 x + 2|v'(8/3) = 0 und v''(8/3) = −2 < 0|Q ist Hochpunkt",
    voraussetzungen="notwendige und hinreichende Bedingung für Extrempunkte|zweite Ableitung",
    format="Rechnung", operator="Weisen Sie nach|Geben Sie an", antwort="Text",
    material="Figur", skizze=F1_SK, kontext="Logo / Anglerbedarf", textumfang="kurz",
    gegeben=F1 + "; v'(x) = −3/4 x² + 2x; Q(8/3 | 64/27)",
    gesucht="Nachweis, dass Q Extrempunkt des Graphen von v ist, und die Art des Extrempunkts",
    verfahren="v'(8/3) = 0 zeigen, Vorzeichen von v''(8/3) prüfen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="2020MgrundlegendBAnalysisWTR1-1a",
    ergebnis="v''(x) = −3/2 x + 2; v'(8/3) = 0 und v''(8/3) < 0, d. h. Q ist Hochpunkt des Graphen von v (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur v'(8/3) = 0 zeigen und die Art nicht begründen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-A).")
row("2020MgrundlegendBAnalysisWTR1", "c", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Aussage über den Vergleich der Steigungen zweier Graphen auf einem Intervall mit Gegenbeispiel beurteilen", typ_neben="",
    stichwoerter="Aussage: für alle x in ]0; 8/3[ ist v'(x) > u'(x)|u'(x) = 3/8 x²|v'(2) = 1 < 3/2 = u'(2): falsch",
    voraussetzungen="Steigung als Ableitungswert|Widerlegen durch ein Gegenbeispiel",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Figur", skizze=F1_SK, kontext="Logo / Anglerbedarf", textumfang="kurz",
    gegeben=F1 + "; v'(x) = −3/4 x² + 2x; Aussage: für jeden Wert von x ∈ ]0; 8/3[ ist die Steigung des Graphen von v größer als die des Graphen von u",
    gesucht="Beurteilung der Aussage",
    verfahren="u' bilden und eine Stelle im Intervall angeben, an der u' ≥ v' ist",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="2020MgrundlegendBAnalysisWTR1-1a",
    ergebnis="Die Aussage ist falsch: mit u'(x) = 3/8 x² gilt v'(2) = 1 < 3/2 = u'(2) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Aussage nur an einer Stelle bestätigen und daraus auf das ganze Intervall schließen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAnalysisWTR1", "d", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Ausdehnung einer Figur in x-Richtung aus der Ausdehnung in y-Richtung über Funktionswerte ermitteln", typ_neben="",
    stichwoerter="Ausdehnung in y-Richtung 539/216 vom Hochpunkt Q bis zur unteren Spitze|y-Koordinate der unteren Spitze 64/27 − 539/216 = −1/8|u(x) = −1/8 ⇔ x = −1|Ausdehnung in x-Richtung 8/3 − (−1) = 11/3",
    voraussetzungen="Hochpunkt Q als höchster Punkt|Gleichung x³ = c lösen|Differenz der äußersten x-Koordinaten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur", skizze=F1_SK, kontext="Logo / Anglerbedarf", textumfang="kurz",
    gegeben=F1 + "; Q(8/3 | 64/27) Hochpunkt; Ausdehnung des Fischs in y-Richtung 539/216; Kontrolle: Ausdehnung in x-Richtung 11/3",
    gesucht="Ausdehnung des Fischs in x-Richtung",
    verfahren="y-Koordinate der unteren Spitze aus 64/27 − 539/216, zugehörige Stelle über u(x) = −1/8, Abstand zur Kopfspitze 8/3",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2020MgrundlegendBAnalysisWTR1-1b",
    ergebnis="Untere Spitze: 64/27 − 539/216 = −1/8; u(x) = −1/8 ⇔ x = −1; Ausdehnung in x-Richtung 8/3 + 1 = 11/3 (amtlich)",
    zwischenergebnis="y = −1/8, x = −1", niveau_geschaetzt="II",
    fehlerquelle="die Ausdehnung in y-Richtung von der Wasseroberfläche 5/4 statt vom Hochpunkt aus messen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 I, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAnalysisWTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen", typ_neben="",
    stichwoerter="Schwanzflosse zwischen x = −1 und x = 0|∫₋₁⁰ (v(x) − u(x)) dx = ∫₋₁⁰ (−3/8 x³ + x²) dx|[−3/32 x⁴ + 1/3 x³]₋₁⁰ = 3/32 + 1/3 = 41/96",
    voraussetzungen="Fläche zwischen zwei Graphen als Integral der Differenz|Stammfunktion ganzrationaler Terme",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze=F1_SK, kontext="Logo / Anglerbedarf", textumfang="kurz",
    gegeben=F1 + "; Schwanzflosse zwischen der senkrechten Kante bei x = −1 und dem Punkt P(0 | 0)",
    gesucht="Flächeninhalt der Schwanzflosse",
    verfahren="Integral von v − u über [−1; 0]",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2020MgrundlegendBAnalysisWTR1-1d",
    ergebnis="∫₋₁⁰ (v(x) − u(x)) dx = [−3/32 x⁴ + 1/3 x³]₋₁⁰ = 3/32 + 1/3 = 41/96 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Grenzen 0 und 8/3 (Fischkörper) statt −1 und 0 wählen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-A).")
row("2020MgrundlegendBAnalysisWTR1", "f", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Aufgabenstellung zu einer Summe zweier Integrale formulieren und die Integrale als Teilflächen im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="x₁: Lösung von v(x) = 5/4 mit 0 < x ≤ 8/3, x₂: Lösung von u(x) = 5/4|∫₋₁^x₁ (v − u) dx + ∫_x₁^x₂ (5/4 − u) dx|Fläche des unter Wasser liegenden (dunkelgrauen) Fischteils",
    voraussetzungen="Integral als Fläche zwischen zwei Graphen|Integrationsgrenzen als Schnittstellen deuten",
    format="Begründung", operator="Formulieren Sie|Beschreiben Sie", antwort="Text",
    material="Figur", skizze=F1_SK, kontext="Logo / Anglerbedarf", textumfang="mittel",
    gegeben=F1 + "; x₁ Lösung von v(x) = 5/4 für 0 < x ≤ 8/3, x₂ Lösung von u(x) = 5/4; Term ∫₋₁^x₁ (v(x) − u(x)) dx + ∫_x₁^x₂ (5/4 − u(x)) dx",
    gesucht="passende Aufgabenstellung und Bedeutung der beiden Integrale",
    verfahren="Beide Integrale als Flächenstücke zwischen den Randlinien bzw. der Wasseroberfläche deuten und die Summe als Fläche des Fischteils unter Wasser erkennen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Aufgabenstellung: Bestimmen Sie den Flächeninhalt des dunkelgrau markierten (unter Wasser liegenden) Teils des Fischs. Die Integrale sind die Inhalte der Flächen zwischen den Graphen von u und v über [−1; x₁] bzw. zwischen der Geraden y = 5/4 und dem Graphen von u über [x₁; x₂] (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das zweite Integral als Fläche zwischen u und v deuten",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K4 II, K6 II. AB amtlich: III. Amtlich.")
F1K = F1 + "; verändertes Logo: obere Begrenzungslinie weiter v, untere Begrenzungslinie u_k(x) = k · 1/8 x³ mit k > 0; die Kopfspitze ist der gemeinsame Punkt der Graphen von u_k und v mit der x-Koordinate 8/(k + 2)"
row("2020MgrundlegendBAnalysisWTR1", "g", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Wendepunkt einer Schar im Ursprung mit der x-Achse als Wendetangente nachweisen", typ_neben="",
    stichwoerter="u_k''(x) = 3/4 k x mit Vorzeichenwechsel bei 0: Wendepunkt (0 | 0)|u_k'(x) = 3/8 k x², u_k'(0) = 0|Tangente im Wendepunkt ist y = 0",
    voraussetzungen="Wendepunkt einer kubischen Parabel|Tangentensteigung als Ableitungswert",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Logo / Anglerbedarf", textumfang="mittel",
    gegeben=F1K,
    gesucht="Nachweis, dass die x-Achse für alle k Tangente an den Graphen von u_k in dessen Wendepunkt ist",
    verfahren="Wendepunkt (0 | 0) angeben und u_k'(0) = 0 zeigen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Der Wendepunkt des Graphen von u_k ist (0 | 0); mit u_k'(x) = 3/8 k x² gilt u_k'(0) = 0, die Tangente dort ist die x-Achse (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den Wendepunkt über u_k'' = 0 zwar finden, aber den Vorzeichenwechsel nicht nennen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAnalysisWTR1", "h", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameter einer Schar aus einer vorgegebenen Ausdehnung einer Figur bestimmen", typ_neben="",
    stichwoerter="obere Spitze bei y = 5/4, Ausdehnung 3/2: untere Spitze bei y = −1/4|u_k(−1) = −1/8 k = −1/4|k = 2",
    voraussetzungen="Lage der Schwanzflosse (senkrechte Kante bei x = −1)|lineare Gleichung in k",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Logo / Anglerbedarf", textumfang="kurz",
    gegeben=F1K + "; die Ausdehnung der Schwanzflosse in y-Richtung soll 3/2 betragen",
    gesucht="Wert von k",
    verfahren="y-Koordinate der unteren Spitze 5/4 − 3/2 = −1/4 mit u_k(−1) gleichsetzen",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2020MgrundlegendBAnalysisWTR1-1d",
    ergebnis="u_k(−1) = 5/4 − 3/2 ⇔ −1/8 k = −1/4 ⇔ k = 2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Ausdehnung vom Hochpunkt statt von der Wasseroberfläche aus ansetzen",
    bemerkung="Standardbezug: K2 II, K3 I, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAnalysisWTR1", "i", innen="1", seite="2", punkte="4", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameter einer Schar aus gleichen Winkeln zweier Graphen mit einer Strecke bestimmen und Lage eines Punktes prüfen", typ_neben="",
    stichwoerter="gleiche Winkel mit der senkrechten Kante: v'(−1) = −u_k'(−1)|v'(−1) = −11/4, u_k'(−1) = 3/8 k = 11/4 ⇔ k = 22/3|Kopfspitze bei x = 8/(22/3 + 2) = 6/7|u_(22/3)(6/7) = 198/343 < 5/4",
    voraussetzungen="Winkel zwischen Graph und Senkrechter über die Steigung|Betrag gleicher Steigungen|Funktionswert mit der Wasserlinie vergleichen",
    format="Rechnung", operator="Prüfen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Logo / Anglerbedarf", textumfang="mittel",
    gegeben=F1K + "; die Graphen von u_k und v schließen mit der Strecke zwischen oberer und unterer Spitze der Schwanzflosse je einen Winkel ein; für einen Wert von k sind beide Winkel gleich groß",
    gesucht="Prüfung, ob die Kopfspitze für diesen Wert von k oberhalb der Wasseroberfläche liegt",
    verfahren="k aus u_k'(−1) = −v'(−1) bestimmen, Kopfspitze über 8/(k + 2) und u_k vergleichen mit 5/4",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="2020MgrundlegendBAnalysisWTR1-1a",
    ergebnis="v'(−1) = −11/4; u_k'(−1) = 3/8 k = 11/4 ⇔ k = 22/3; u_(22/3)(8/(22/3 + 2)) = 198/343 < 5/4, d. h. die Kopfspitze liegt nicht oberhalb der Wasseroberfläche (amtlich)",
    zwischenergebnis="k = 22/3", niveau_geschaetzt="III",
    fehlerquelle="gleiche Winkel als gleiche Steigungen statt entgegengesetzt gleiche Steigungen ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 I, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt.")
# ---- Analysis WTR 2: Produkt aus Polynom und e-Funktion, Aufgabe 1 (a–h, 26 BE) und Schar g_b (2 a–c, 9 BE)
F2 = "f(x) = 1/10 · x · (3 − x) · eˣ, x ∈ IR; Abbildung 1 zeigt den Graphen von f; f'(x) = −1/10 · (x² − x − 3) · eˣ"
F2_SK = ("Abb. 1: Koordinatensystem auf Gitter, x von −1 bis 3,5, y von −0,5 bis 2,5: Graph von f durch den Ursprung, von links der "
         "x-Achse anschmiegend, Hochpunkt bei etwa (2,3 | 1,6), Nullstelle 3, danach steil fallend")
row("2020MgrundlegendBAnalysisWTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen",
    typ_neben="Nullstellen und Werte: Nullstellen aus der faktorisierten Form angeben",
    stichwoerter="Nullstellen 0 und 3|f'(x) = 0 ⇔ x² − x − 3 = 0 ⇔ x = (1 ± √13)/2|x = (1 + √13)/2 ≈ 2,3 (Hochstelle nach Abbildung), y ≈ 1,6",
    voraussetzungen="Produkt gleich null|quadratische Gleichung|Art des Extremums aus der Abbildung",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=F2_SK, kontext="ohne", textumfang="kurz",
    gegeben=F2,
    gesucht="Nullstellen von f; Koordinaten des Hochpunkts",
    verfahren="Nullstellen am Produkt ablesen; f' = 0 lösen, Hochstelle aus der Abbildung wählen, Funktionswert berechnen",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Nullstellen 0 und 3; Hochpunkt bei x = (1 + √13)/2 ≈ 2,3 mit y = f((1 + √13)/2) ≈ 1,6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die negative Lösung (1 − √13)/2 als Hochstelle nehmen",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (x ≈ 2,303, y ≈ 1,606). Typ wiederverwendet (2025-ga-B), Nebentyp aus 2020-be-gk.")
row("2020MgrundlegendBAnalysisWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Grenzwert für x gegen unendlich angeben und Verlauf des Graphen beschreiben", typ_neben="",
    stichwoerter="lim f(x) für x → −∞ ist 0, weil eˣ → 0 und das Polynom nur polynomial wächst|Graph nähert sich asymptotisch der x-Achse",
    voraussetzungen="Grenzverhalten der e-Funktion|e-Funktion dominiert Polynom",
    format="Begründung", operator="Beschreiben Sie|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=F2_SK, kontext="ohne", textumfang="kurz",
    gegeben=F2,
    gesucht="Verlauf des Graphen für x → −∞ mit Begründung am Term",
    verfahren="Grenzwert von eˣ nennen und den Faktor x · (3 − x) als untergeordnet begründen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Wegen lim eˣ = 0 für x → −∞ gilt lim f(x) = 0; der Graph nähert sich für x → −∞ asymptotisch der x-Achse (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="aus x · (3 − x) → −∞ auf f → −∞ schließen",
    bemerkung="Standardbezug: K4 I, K5 I, K6 II. AB amtlich: II. Amtlich. Typ wiederverwendet (2022-bebb-gk). Enge Fassung: Grenzwert angeben wäre I, die Begründung am Term (Dominanz der e-Funktion) stellt einen Zusammenhang her – II.")
row("2020MgrundlegendBAnalysisWTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente durch einen vorgegebenen Punkt am Graphen einzeichnen und ihre Gleichung ablesen", typ_neben="",
    stichwoerter="Gerade durch (0 | 1/2), die den Graphen berührt (Berührpunkt etwa (2,1 | 1,55))|Steigung am Bild etwa 1/2|y = 1/2 x + 1/2",
    voraussetzungen="Tangente als berührende Gerade|Geradengleichung aus Achsenabschnitt und Steigung",
    format="Zeichnen|Kurzantwort", operator="Zeichnen Sie|Geben Sie an", antwort="Grafik|Term",
    material="Koordinatensystem", skizze=F2_SK, kontext="ohne", textumfang="kurz",
    gegeben=F2 + "; eine Tangente an den Graphen von f verläuft durch (0 | 1/2)",
    gesucht="diese Tangente in Abbildung 1; eine Gleichung der eingezeichneten Geraden",
    verfahren="Lineal durch (0 | 1/2) an den Graphen anlegen, Steigung ablesen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="y = 1/2 x + 1/2, Ablesewert der Steigung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Tangente im Punkt (0 | f(0)) statt durch (0 | 1/2) zeichnen",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich. Eigene Rechnung: Berührstelle t mit f(t) − t · f'(t) = 1/2 liegt bei t ≈ 2,13, dort f'(t) ≈ 0,5.")
row("2020MgrundlegendBAnalysisWTR2", "d", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Steigungswinkel des Graphen in einem Punkt über die Ableitung berechnen", typ_neben="",
    stichwoerter="tan α = f'(0) = 0,3|α ≈ 16,7°",
    voraussetzungen="Steigungswinkel über den Tangens der Ableitung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=F2,
    gesucht="Größe des Steigungswinkels des Graphen im Koordinatenursprung",
    verfahren="f'(0) berechnen und den Arkustangens bilden",
    schritte="2", zahlenraum="dezimal", einheiten="°", abhaengig_von="",
    ergebnis="tan α = f'(0) = 0,3, d. h. α ≈ 16,7° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Rechner im Bogenmaß",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAnalysisWTR2", "e", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion durch Ableiten nachweisen", typ_neben="",
    stichwoerter="F(x) = −1/10 · (x² − 5x + 5) · eˣ|F'(x) = −1/10 · (2x − 5) · eˣ − 1/10 · (x² − 5x + 5) · eˣ = −1/10 · (x² − 3x) · eˣ = 1/10 · x · (3 − x) · eˣ = f(x)",
    voraussetzungen="Produktregel|Ableitung von eˣ|Zusammenfassen",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=F2 + "; F(x) = −1/10 · (x² − 5x + 5) · eˣ, in IR definiert",
    gesucht="Nachweis, dass F eine Stammfunktion von f ist",
    verfahren="F mit der Produktregel ableiten und zu f zusammenfassen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="F'(x) = −1/10 · (2x − 5) · eˣ − 1/10 · (x² − 5x + 5) · eˣ = −1/10 · (x² − 3x) · eˣ = f(x) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Produktregel ohne den Faktor eˣ im zweiten Summanden",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2020-ea-A). Enge Fassung: Produktregel mit anschließendem Zusammenfassen auf die Zielform – II.")
row("2020MgrundlegendBAnalysisWTR2", "f", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral als Flächeninhalt zwischen Graph und x-Achse deuten und über die Stammfunktion berechnen", typ_neben="",
    stichwoerter="∫₀³ f(x) dx = Inhalt der Fläche zwischen Graph und x-Achse über [0; 3] (f ≥ 0 dort)|F(3) − F(0) = 1/10 · e³ + 1/2 ≈ 2,5",
    voraussetzungen="Integral als Flächeninhalt bei nichtnegativem Integranden|Hauptsatz",
    format="Begründung|Rechnung", operator="Deuten Sie|Berechnen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=F2 + "; F(x) = −1/10 · (x² − 5x + 5) · eˣ; Integral ∫₀³ f(x) dx",
    gesucht="geometrische Deutung des Integrals und sein Wert",
    verfahren="Fläche zwischen Graph und x-Achse über [0; 3] nennen, F(3) − F(0) berechnen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2020MgrundlegendBAnalysisWTR2-1e",
    ergebnis="Inhalt des Flächenstücks, das der Graph von f für 0 ≤ x ≤ 3 mit der x-Achse einschließt; ∫₀³ f(x) dx = F(3) − F(0) = 1/10 · e³ + 1/2 ≈ 2,5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="F(0) = −1/2 vergessen",
    bemerkung="Standardbezug: K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (2,509).")
row("2020MgrundlegendBAnalysisWTR2", "g", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Existenz einer oberen Grenze mit Integralwert null über den Flächenausgleich ohne Rechnung begründen", typ_neben="",
    stichwoerter="für x > 3 ist f negativ und f(x) → −∞|Fläche unterhalb der x-Achse wächst unbeschränkt, Fläche oberhalb ist fest (≈ 2,5)|es gibt a > 3 mit gleich großen Flächen, dort ist das Integral null",
    voraussetzungen="Integral als orientierte Fläche|Vorzeichen von f|Grenzverhalten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=F2 + "; Behauptung: es gibt eine positive Zahl a mit ∫₀ᵃ f(x) dx = 0",
    gesucht="Begründung ohne Rechnung",
    verfahren="Flächenstücke oberhalb (über [0; 3]) und unterhalb der x-Achse (ab 3, unbeschränkt wachsend) vergleichen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Für x > 3 sind die Funktionswerte negativ und lim f(x) = −∞ für x → +∞; also gibt es einen Wert von a, für den das Flächenstück unterhalb der x-Achse über [3; a] genauso groß ist wie das oberhalb über [0; 3] (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="a mit der Nullstelle 3 verwechseln (dort ist das Integral positiv)",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich.")
row("2020MgrundlegendBAnalysisWTR2", "h", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Tiefpunkt aller Stammfunktionen auf der y-Achse über den Vorzeichenwechsel von f begründen und Stammfunktion mit Tiefpunkt im Ursprung bestimmen", typ_neben="",
    stichwoerter="H(x) = F(x) + c, H' = f|f(0) = 0, f < 0 für x < 0 und f > 0 für 0 < x < 3: Vorzeichenwechsel − nach + bei 0|Tiefpunkt bei x = 0, also auf der y-Achse|H(0) = 0 ⇔ F(0) + c = 0 ⇔ c = 1/2",
    voraussetzungen="Stammfunktionen unterscheiden sich um eine Konstante|Extremstelle über Vorzeichenwechsel der Ableitung|Wert von F(0)",
    format="Begründung|Rechnung", operator="Begründen Sie|Bestimmen Sie", antwort="Text|Term",
    material="Koordinatensystem", skizze=F2_SK, kontext="ohne", textumfang="mittel",
    gegeben=F2 + "; F(x) = −1/10 · (x² − 5x + 5) · eˣ ist eine Stammfunktion",
    gesucht="Begründung ohne den Term von F, dass der Graph jeder Stammfunktion einen Tiefpunkt auf der y-Achse hat; die Stammfunktion mit Tiefpunkt im Ursprung",
    verfahren="Vorzeichenwechsel von f bei 0 aus Term oder Abbildung; H(0) = F(0) + c = 0 nach c lösen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2020MgrundlegendBAnalysisWTR2-1e",
    ergebnis="H(x) = F(x) + c mit H' = f; H'(0) = 0, H' < 0 für x < 0 und H' > 0 für x > 0 nahe 0, also Tiefpunkt bei x = 0 (auf der y-Achse); H(0) = 0 ⇔ F(0) + c = 0 ⇔ c = 1/2 (amtlich)",
    zwischenergebnis="F(0) = −1/2", niveau_geschaetzt="III",
    fehlerquelle="mit F'' argumentieren statt mit dem Vorzeichenwechsel von f",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt.")
G2 = ("Schar g_b(x) = 1/10 · x · (x − b) · eˣ, b ∈ IR₀⁺, x ∈ IR; g_b'(x) = 1/10 · (x² + (2 − b) · x − b) · eˣ; Abbildung 2 zeigt die Graphen "
      "von g₂ und g₃; f(x) = 1/10 · x · (3 − x) · eˣ aus Aufgabe 1")
G2_SK = ("Abb. 2: Koordinatensystem auf Gitter, x von −1 bis 3,5, y von −1,5 bis 1,5: Graph von g₂ (durchgezogen, Nullstellen 0 und 2, "
         "Tiefpunkt etwa (1,4 | −0,6), danach steil steigend) und von g₃ (gestrichelt, Nullstellen 0 und 3, Tiefpunkt etwa (2,3 | −1,6))")
row("2020MgrundlegendBAnalysisWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Spiegelung an der x-Achse als Scharmitglied nachweisen", typ_neben="",
    stichwoerter="Figur symmetrisch zur x-Achse ⇔ g_b(x) = −f(x)|x − b = −(3 − x) ⇔ b = 3",
    voraussetzungen="Spiegelung an der x-Achse als Vorzeichenwechsel|Koeffizientenvergleich",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=G2_SK, kontext="ohne", textumfang="kurz",
    gegeben=G2,
    gesucht="Wert von b, für den die Graphen von g_b und f eine zur x-Achse symmetrische Figur einschließen",
    verfahren="g_b = −f ansetzen und b ablesen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="g_b(x) = −f(x) ⇔ x − b = −(3 − x) ⇔ b = 3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="b = 2 aus der Abbildung raten",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ea-B).")
row("2020MgrundlegendBAnalysisWTR2", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gemeinsamen Punkt von Scharkurve und ihrem Ableitungsgraphen in Abhängigkeit vom Parameter berechnen", typ_neben="",
    stichwoerter="g_b(x) = g_b'(x) ⇔ x² − bx = x² + (2 − b)x − b ⇔ 2x = b|x = b/2",
    voraussetzungen="Gleichsetzen, Kürzen des Faktors 1/10 · eˣ|lineare Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=G2 + "; für jeden Wert von b haben die Graphen von g_b und g_b' einen gemeinsamen Punkt",
    gesucht="x-Koordinate dieses Punkts in Abhängigkeit von b",
    verfahren="g_b = g_b' setzen, gemeinsamen Faktor kürzen, nach x auflösen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="g_b(x) = g_b'(x) ⇔ x² − bx = x² + 2x − bx − b ⇔ x = b/2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Faktor eˣ nicht kürzen und eine Exponentialgleichung ansetzen",
    bemerkung="Standardbezug: K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAnalysisWTR2", "c", innen="2", seite="2", punkte="4", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Flächenstück zwischen zwei Scharkurven und der x-Achse markieren und Gleichung für den Parameter aus dem Flächeninhalt angeben", typ_neben="",
    stichwoerter="für b = 2: Flächenstück zwischen g₂, g₃ und der x-Achse im vierten Quadranten (zwischen x = 2 und x = 3 unter der x-Achse bis zum Graphen von g₂ … )|Inhalt = |∫₀^(b+1) g_(b+1)(x) dx| − |∫₀ᵇ g_b(x) dx||Gleichung |∫₀^(b+1) g_(b+1)(x) dx| − |∫₀ᵇ g_b(x) dx| = 5",
    voraussetzungen="Nullstellen 0 und b der Scharkurven|Fläche unterhalb der x-Achse als Betrag des Integrals|Differenz zweier Flächen",
    format="Eintragen|Kurzantwort", operator="Markieren Sie|Geben Sie an", antwort="Grafik|Term",
    material="Koordinatensystem", skizze=G2_SK, kontext="ohne", textumfang="mittel",
    gegeben=G2 + "; für jeden Wert von b schließen die Graphen von g_b und g_(b+1) im vierten Quadranten mit der x-Achse ein Flächenstück ein; für einen Wert von b hat es den Inhalt 5",
    gesucht="Markierung des Flächenstücks für b = 2 in Abbildung 2; eine Gleichung zur Bestimmung des Werts von b",
    verfahren="Flächenstück zwischen den beiden Graphen unter der x-Achse markieren; Inhalt als Differenz der Beträge der beiden Integrale von 0 bis zur jeweiligen Nullstelle ansetzen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Markierung: Fläche zwischen dem Graphen von g₃ (unten) und dem Graphen von g₂ bzw. der x-Achse (oben) über [0; 3]; Gleichung |∫₀^(b+1) g_(b+1)(x) dx| − |∫₀ᵇ g_b(x) dx| = 5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das Integral von g_(b+1) − g_b von 0 bis b + 1 ansetzen und die x-Achse als Begrenzung vergessen",
    bemerkung="Standardbezug: K1 II, K2 III, K4 I, K5 II. AB amtlich: III. Amtlich.")
# ---- AG/LA (A1) WTR: Aufgabe 1 Verflechtung Rohstoffe – Zwischenprodukte – Endprodukte (1 a–d, 9 BE), Aufgabe 2 Raute ABCD (2 a–c, 11 BE)
V1 = ("Herstellungsprozess: aus den Rohstoffen R₁, R₂, R₃ werden die Zwischenprodukte Z₁, Z₂ und daraus die Endprodukte E₁, E₂, E₃ hergestellt; "
      "Bedarf je Mengeneinheit laut Diagramm: Z₁ braucht 2 R₁, 1 R₃; Z₂ braucht 1 R₁, 1 R₂, 2 R₃; E₁ braucht 3 Z₁; E₂ braucht 1 Z₁ und 5 Z₂; "
      "E₃ braucht 7 Z₁ und 1 Z₂; Gleichungen (r₁; r₂; r₃) = A · (z₁; z₂) und (z₁; z₂) = B · (e₁; e₂; e₃)")
V1_SK = ("Verflechtungsdiagramm mit drei Spalten von Kreisen: links R₁, R₂, R₃, in der Mitte Z₁, Z₂, rechts E₁, E₂, E₃; Pfeile mit Bedarfszahlen "
         "R₁→Z₁ 2, R₁→Z₂ 1, R₂→Z₂ 1, R₃→Z₁ 1, R₃→Z₂ 2, Z₁→E₁ 3, Z₁→E₂ 1, Z₁→E₃ 7, Z₂→E₂ 5, Z₂→E₃ 1")
row("2020MgrundlegendBAGLAA1WTR", "a", innen="1", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Matrix-Vektor-Gleichung mit konkreten Zahlen im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="(3; 3; 6) = A · (0; 3)|3 Mengeneinheiten Z₂ brauchen 3 R₁, 3 R₂ und 6 R₃",
    voraussetzungen="Bedeutung der Vektoren r und z|Matrix-Vektor-Produkt als Bedarf",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Diagramm", skizze=V1_SK, kontext="Produktion / Verflechtung", textumfang="mittel",
    gegeben=V1 + "; Gleichung (3; 3; 6) = A · (0; 3)",
    gesucht="Bedeutung der Gleichung im Sachzusammenhang",
    verfahren="Vektor (0; 3) als Bestellung von 3 Mengeneinheiten Z₂ lesen, linke Seite als Rohstoffbedarf",
    schritte="1", zahlenraum="ganz", einheiten="Mengeneinheiten", abhaengig_von="",
    ergebnis="Zur Herstellung von 3 Mengeneinheiten von Z₂ sind 3 Mengeneinheiten von R₁, 3 von R₂ und 6 von R₃ erforderlich (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Ein- und Ausgangsvektor vertauschen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich.")
row("2020MgrundlegendBAGLAA1WTR", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Format der Bedarfsmatrix aus der Anzahl der Stufenprodukte begründen", typ_neben="",
    stichwoerter="(z₁; z₂) = B · (e₁; e₂; e₃): B hat zwei Zeilen und drei Spalten|Matrix II (3 1 7 / 0 5 1)",
    voraussetzungen="Zeilen- und Spaltenzahl einer Matrix aus dem Produkt|Einträge aus dem Diagramm",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm", skizze=V1_SK, kontext="Produktion / Verflechtung", textumfang="mittel",
    gegeben=V1 + "; drei Matrizen zur Auswahl: I (3 0 / 1 5 / 7 1), II (3 1 7 / 0 5 1), III (3 1 7 / 0 5 1 / 0 0 0)",
    gesucht="die Matrix, die B darstellt, mit Begründung",
    verfahren="Format aus der Gleichung ableiten (2 × 3), passende Matrix wählen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Aus (z₁; z₂) = B · (e₁; e₂; e₃) folgt, dass B zwei Zeilen und drei Spalten hat: Matrix II (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Matrix I (transponiert) wählen, weil sie die Pfeile zeilenweise wiedergibt",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2023-ga-B).")
row("2020MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Eintrag der Gesamtmatrix aus dem Diagramm bestätigen und Nulleintrag begründen", typ_neben="",
    stichwoerter="A · B = (6 7 15 / a 5 1 / 9 13 23)|a = Bedarf an R₂ je Mengeneinheit E₁|E₁ braucht nur Z₁, und Z₁ braucht kein R₂: a = 0",
    voraussetzungen="Gesamtmatrix als Rohstoffbedarf je Endprodukt|Pfade im Diagramm",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Diagramm", skizze=V1_SK, kontext="Produktion / Verflechtung", textumfang="kurz",
    gegeben=V1 + "; A · B = (6 7 15 / a 5 1 / 9 13 23)",
    gesucht="Begründung im Sachzusammenhang, dass a = 0 gilt",
    verfahren="a als Bedarf an R₂ für eine Mengeneinheit E₁ deuten und den Pfad R₂ → Z₂ → E₁ als nicht vorhanden erkennen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="a ist die Anzahl der Mengeneinheiten von R₂ für eine Mengeneinheit von E₁; E₁ benötigt nur Z₁, das ohne R₂ hergestellt wird, also a = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="a durch Ausrechnen des Matrixprodukts bestimmen statt im Sachzusammenhang zu begründen",
    bemerkung="Standardbezug: K1 I, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich. Typ wiederverwendet (2023-ga-B).")
row("2020MgrundlegendBAGLAA1WTR", "d", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Produktionsmengen aus dem Rohstoffverbrauch über ein Gleichungssystem ermitteln", typ_neben="",
    stichwoerter="(6 7 15 / 0 5 1 / 9 13 23) · (e₁; e₂; 0) = (510; 150; 840)|6e₁ + 7e₂ = 510, 5e₂ = 150, 9e₁ + 13e₂ = 840|e₂ = 30, e₁ = 50; dritte Gleichung erfüllt",
    voraussetzungen="Gesamtmatrix A · B|lineares Gleichungssystem mit e₃ = 0",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=V1_SK, kontext="Produktion / Verflechtung", textumfang="mittel",
    gegeben=V1 + "; A · B = (6 7 15 / 0 5 1 / 9 13 23); Vorrat 510 R₁, 150 R₂, 840 R₃; nur E₁ und E₂ werden hergestellt",
    gesucht="Mengeneinheiten von E₁ und E₂, die die Rohstoffe vollständig aufbrauchen",
    verfahren="Gleichungssystem aus A · B · (e₁; e₂; 0) = Vorrat aufstellen und lösen",
    schritte="3", zahlenraum="ganz", einheiten="Mengeneinheiten", abhaengig_von="2020MgrundlegendBAGLAA1WTR-1c",
    ergebnis="6e₁ + 7e₂ = 510, 5e₂ = 150, 9e₁ + 13e₂ = 840; e₂ = 30 und e₁ = 50: 50 Mengeneinheiten E₁ und 30 Mengeneinheiten E₂ (amtlich)",
    zwischenergebnis="e₂ = 30", niveau_geschaetzt="II",
    fehlerquelle="mit A oder B allein statt mit A · B rechnen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2021-ga-A).")
R2 = "Viereck ABCD mit A(5 | 0 | 0), B(0 | 8 | −6), C(−5 | 0 | 0) und D(0 | −8 | 6)"
row("2020MgrundlegendBAGLAA1WTR", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Raute über gleiche Seitenvektoren nachweisen und Quadrat über das Skalarprodukt ausschließen", typ_neben="",
    stichwoerter="AB = (−5; 8; −6) = DC, AD = (−5; −8; 6) = BC|Parallelogramm mit |AB| = |AD| = √125: Raute|AB · AD = 25 − 64 − 36 ≠ 0: kein rechter Winkel, kein Quadrat",
    voraussetzungen="Parallelogramm über gleiche Seitenvektoren|Betrag eines Vektors|Skalarprodukt und rechter Winkel",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=R2,
    gesucht="Nachweis, dass ABCD eine Raute, aber kein Quadrat ist",
    verfahren="Seitenvektoren vergleichen, Längen berechnen, Skalarprodukt zweier benachbarter Seiten prüfen",
    schritte="3", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="AB = (−5; 8; −6) = DC und AD = (−5; −8; 6) = BC mit gleichen Beträgen; AB · AD ≠ 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur vier gleiche Seitenlängen zeigen und die Parallelität nicht nennen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAGLAA1WTR", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächenformel einer Raute als halbes Diagonalenprodukt mit einer Skizze begründen", typ_neben="",
    stichwoerter="Skizze: Raute mit Diagonalen AC und BD, umschließendes Rechteck mit den Seiten |AC| und |BD|, achsenparallel zu den Diagonalen|die Diagonalen zerlegen das Rechteck in acht kongruente Dreiecke, vier davon bilden die Raute|Fläche = 1/2 · |AC| · |BD|",
    voraussetzungen="Diagonalen einer Raute stehen senkrecht und halbieren sich|Flächenvergleich am Rechteck",
    format="Zeichnen|Begründung", operator="Begründen Sie", antwort="Grafik|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=R2 + "; Term 1/2 · |AC| · |BD|",
    gesucht="Begründung mithilfe einer Skizze, dass der Term den Flächeninhalt der Raute liefert",
    verfahren="Raute mit Diagonalen in ein Rechteck der Seiten |AC| und |BD| einbetten und den Anteil 1/2 begründen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Der Flächeninhalt der Raute ist halb so groß wie der eines Rechtecks mit den Seitenlängen |AC| und |BD| (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Formel nur zitieren statt am Rechteck zu begründen",
    bemerkung="Standardbezug: K1 II, K4 I, K6 II. AB amtlich: II. Amtlich.")
row("2020MgrundlegendBAGLAA1WTR", "c", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Berührpunkt des Inkreises einer Raute über Lage auf der Seite und Orthogonalität zum Mittelpunkt begründen", typ_neben="",
    stichwoerter="AP = (−1; 1,6; −1,2) = 1/5 · AB: P liegt auf AB|Kreismittelpunkt = Diagonalenschnittpunkt = Ursprung|OP · AB = −20 + 12,8 + 7,2 = 0: OP senkrecht zu AB, also Berührpunkt",
    voraussetzungen="Punkt auf einer Strecke über Vielfaches des Richtungsvektors|Inkreismittelpunkt einer Raute|Tangente senkrecht zum Radius",
    format="Rechnung|Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=R2 + "; ein Kreis berührt jede der vier Seiten; P(4 | 1,6 | −1,2)",
    gesucht="Begründung, dass P einer der Berührpunkte ist",
    verfahren="P auf AB nachweisen, Mittelpunkt des Kreises als Diagonalenschnittpunkt (Ursprung) erkennen, OP ⊥ AB zeigen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="2020MgrundlegendBAGLAA1WTR-2a",
    ergebnis="AP = 1/5 · AB, also P auf AB; Mittelpunkt des Kreises ist der Diagonalenschnittpunkt, der Koordinatenursprung; OP · AB = −20 + 12,8 + 7,2 = 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur P ∈ AB zeigen und die Orthogonalität zum Mittelpunkt weglassen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt.")
# ---- AG/LA (A2) WTR: Aufgabe 1 Sonnensegel (1 a–e, 16 BE), Aufgabe 2 Dreiecke RST_λ (eine Aufgabe ohne Buchstaben, 4 BE)
S2 = ("Sonnensegel als Dreieck ABC mit A(−1 | 1 | 2), B(−1 | 5 | 2), C(−4 | 3 | 3) zwischen drei Masten; Untergrund = x₁x₂-Ebene; 1 LE = 1 m; "
      "die Ebene des Dreiecks hat eine Gleichung der Form x₁ + 3x₃ = j")
row("2020MgrundlegendBAGLAA2WTR", "a", innen="1", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Konstante einer Koordinatengleichung durch Einsetzen eines Punktes bestimmen", typ_neben="",
    stichwoerter="A einsetzen: j = −1 + 3 · 2 = 5",
    voraussetzungen="Punktprobe in einer Koordinatengleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Sonnensegel", textumfang="mittel",
    gegeben=S2,
    gesucht="Wert von j",
    verfahren="Koordinaten eines Eckpunkts einsetzen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="j = −1 + 3 · 2 = 5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="x₂-Koordinate mit einrechnen",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAGLAA2WTR", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigung einer Ebene in Prozent über den Winkel zur Koordinatenebene prüfen", typ_neben="",
    stichwoerter="Normalenvektoren (1; 0; 3) und (0; 0; 1)|cos α = 3/√10|tan α = 1/3 ≈ 33 % > 30 %: Bedingung erfüllt",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren|Neigung in Prozent als Tangens",
    format="Rechnung", operator="Prüfen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Sonnensegel", textumfang="kurz",
    gegeben=S2 + "; Bedingung: Neigung des Segels mindestens 30 %",
    gesucht="Prüfung, ob die Bedingung erfüllt ist",
    verfahren="Winkel zwischen der Segelebene und der x₁x₂-Ebene über die Normalenvektoren, Tangens mit 0,3 vergleichen",
    schritte="3", zahlenraum="Wurzel|Prozent", einheiten="", abhaengig_von="2020MgrundlegendBAGLAA2WTR-1a",
    ergebnis="cos α = 3/√10 liefert tan α = 1/3 > 30 %, die Bedingung ist erfüllt (amtlich)",
    zwischenergebnis="α ≈ 18,4°", niveau_geschaetzt="II",
    fehlerquelle="Neigung in Prozent mit dem Winkel in Grad gleichsetzen",
    bemerkung="Standardbezug: K2 II, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2020MgrundlegendBAGLAA2WTR", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Ursprüngliche Länge einer Strecke aus der Streckenlänge und einer prozentualen Verlängerung berechnen", typ_neben="",
    stichwoerter="Seite parallel zum Untergrund: AB mit |AB| = 4|4/1,04 ≈ 3,85 m",
    voraussetzungen="Parallelität zur x₁x₂-Ebene über gleiche x₃-Koordinaten|Betrag eines Vektors|Prozentrechnung (Grundwert)",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Sonnensegel", textumfang="kurz",
    gegeben=S2 + "; die zum Untergrund parallele Seite ist 4 % länger als vor dem ersten Aufspannen",
    gesucht="Länge dieser Seite vor dem ersten Aufspannen",
    verfahren="Seite AB als parallele Seite erkennen, Länge 4 durch 1,04 teilen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="m", abhaengig_von="",
    ergebnis="1/1,04 · |AB| = 4/1,04 ≈ 3,85, d. h. etwa 3,85 m (amtlich)",
    zwischenergebnis="|AB| = 4", niveau_geschaetzt="I",
    fehlerquelle="4 % von 4 abziehen statt durch 1,04 zu teilen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
S2S = S2 + "; Schatten der unteren Eckpunkte A und B auf dem Untergrund: A'(−5 | 3 | 0), B'(−5 | 7 | 0) (paralleles Sonnenlicht)"
row("2020MgrundlegendBAGLAA2WTR", "d", innen="1", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schattenpunkt bei paralleler Projektion bestimmen", typ_neben="",
    stichwoerter="Lichtrichtung AA' = (−4; 2; −2)|OC + μ · AA' mit x₃ = 0: 3 − 2μ = 0, μ = 1,5|C'(−10 | 6 | 0)",
    voraussetzungen="Richtungsvektor des Lichts aus Punkt und Schattenpunkt|Gerade mit x₃ = 0 schneiden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Sonnensegel", textumfang="mittel",
    gegeben=S2S + "; Kontrolle: (−10 | 6 | 0)",
    gesucht="Koordinaten des Schattens des oberen Eckpunkts C",
    verfahren="Lichtgerade durch C mit Richtung AA' aufstellen und x₃ = 0 setzen",
    schritte="3", zahlenraum="ganz|negativ|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Mit AA' = (−4; 2; −2) und OC + μ · AA' = (x₁; x₂; 0) folgt μ = 1,5, x₁ = −10 und x₂ = 6: C'(−10 | 6 | 0) (amtlich)",
    zwischenergebnis="μ = 1,5", niveau_geschaetzt="II",
    fehlerquelle="Lichtrichtung aus B und B' anders als aus A und A' vermuten oder x₃ = 3 belassen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-be-gk).")
row("2020MgrundlegendBAGLAA2WTR", "e", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Schattendreieck in der Grundebene zeichnen und seinen Flächeninhalt berechnen", typ_neben="",
    stichwoerter="Dreieck A'B'C' in der x₁x₂-Ebene mit A'(−5 | 3), B'(−5 | 7), C'(−10 | 6)|Grundseite A'B' = 4, Höhe 5|1/2 · 4 · 5 = 10 m²",
    voraussetzungen="Punkte in der x₁x₂-Ebene zeichnen|Dreiecksfläche aus Grundseite und Höhe",
    format="Zeichnen|Rechnung", operator="Stellen Sie dar|Bestimmen Sie", antwort="Grafik|Zahl",
    material="keins", skizze="keine", kontext="Sonnensegel", textumfang="kurz",
    gegeben=S2S + "; C'(−10 | 6 | 0)",
    gesucht="grafische Darstellung des Schattens in der x₁x₂-Ebene und sein Flächeninhalt",
    verfahren="Dreieck A'B'C' in ein x₁x₂-Koordinatensystem zeichnen, Fläche über achsenparallele Grundseite und Höhe",
    schritte="2", zahlenraum="ganz|negativ", einheiten="m²", abhaengig_von="2020MgrundlegendBAGLAA2WTR-1d",
    ergebnis="1/2 · 4 · 5 = 10, d. h. der Flächeninhalt des Schattens beträgt 10 m² (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Höhe als Abstand von C' zu A' statt zur Geraden A'B' nehmen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
T2 = ("Gerade t: x = (−2; 3; −1) + λ · (−1; 0; 3), λ ∈ IR, die die Gerade durch R(−1 | 2 | 3) und S(−1 | 4 | 3) nicht schneidet; zu jedem λ gehört der Punkt "
      "T_λ von t, jeder Punkt T_λ hat von R und S den gleichen Abstand; unter den Dreiecken RST_λ hat eines den kleinsten Flächeninhalt")
T2_SK = ("Skizze ohne Koordinatensystem: Gerade t schräg oben mit dem Punkt T_λ, darunter die Punkte R (links unten) und S (rechts) auf einer "
         "strichpunktierten Geraden, Dreieck RST_λ eingezeichnet")
row("2020MgrundlegendBAGLAA2WTR", "", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Gleichung für den Parameter des flächenkleinsten gleichschenkligen Dreiecks über die Orthogonalität von Höhe und Gerade begründen", typ_neben="",
    stichwoerter="RST_λ gleichschenklig mit Basis RS, M(−1 | 3 | 3) Mittelpunkt von RS|Fläche 1/2 · |RS| · |MT_λ| minimal ⇔ |MT_λ| minimal|MT_λ = (−1 − λ; 0; −4 + 3λ) senkrecht zum Richtungsvektor (−1; 0; 3) von t: MT_λ · (−1; 0; 3) = 0",
    voraussetzungen="Höhe eines gleichschenkligen Dreiecks durch den Basismittelpunkt|kürzester Abstand als Lot|Skalarprodukt gleich null",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Skizze", skizze=T2_SK, kontext="ohne", textumfang="lang",
    gegeben=T2 + "; Behauptung: der zugehörige Wert von λ löst (−1 − λ; 0; −4 + 3λ) · (−1; 0; 3) = 0",
    gesucht="Begründung der Gleichung",
    verfahren="Flächeninhalt als 1/2 · |RS| · |MT_λ| schreiben, Minimum bei minimalem |MT_λ|, d. h. MT_λ senkrecht zu t",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Die Dreiecke sind gleichschenklig mit Basis RS und Mittelpunkt M(−1 | 3 | 3); ihr Flächeninhalt 1/2 · |RS| · |MT_λ| ist genau dann am kleinsten, wenn |MT_λ| am kleinsten ist, also MT_λ senkrecht zum Richtungsvektor von t steht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die Fläche über den Abstand T_λ zu R statt über die Höhe ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 III. AB amtlich: III. Amtlich. Aufgabe 2 ohne Teilaufgabenbuchstaben (id …-2).")
# ---- Stochastik WTR 1: Beschäftigte eines Unternehmens (1 a–d, 10 BE; 2 a–c, 10 BE); Landesheft 2020-be-gk 4.2 a–g vorgemerkt
U1 = ("Großes Unternehmen, 29 % der Beschäftigten sind weiblich; 40 Beschäftigte werden zufällig ausgewählt, die Anzahl X der weiblichen "
      "darunter ist binomialverteilt (n = 40, p = 0,29)")
row("2020MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="P(X ≥ 12) = 1 − P(X ≤ 11)|Σ_(k=12)^40 B(40; 0,29; k) ≈ 50,4 %",
    voraussetzungen="Gegenereignis|kumulierte Binomialverteilung mit dem Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="mittel",
    gegeben=U1,
    gesucht="P(mindestens 12 weibliche unter den 40)",
    verfahren="1 − P(X ≤ 11) mit dem Rechner",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Σ_(k=12)^40 B(40; 0,29; k) ≈ 50,4 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≤ 12) statt P(X ≤ 11) abziehen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,5041). Typ wiederverwendet (2026-ga-B). Landesheft 2020-be-gk 4.2 a (abgewandelt: dort 1/3, 50 Beschäftigte, mindestens 17; dort vorgemerkt).")
row("2020MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Σ_(k=0)^10 (40 über k) · 0,29ᵏ · 0,71^(40−k) ≈ 0,36|Summe der Einzelwahrscheinlichkeiten für k = 0 bis 10 = P(X ≤ 10)",
    voraussetzungen="Bernoulli-Term lesen|Summe als kumulierte Wahrscheinlichkeit",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=U1 + "; Aussage Σ_(k=0)^10 (40 über k) · 0,29ᵏ · 0,71^(40−k) ≈ 0,36",
    gesucht="Bedeutung der Aussage im Sachzusammenhang",
    verfahren="Summanden als P(X = k) deuten, Summe als P(X ≤ 10)",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Die Wahrscheinlichkeit dafür, dass von den ausgewählten Beschäftigten höchstens zehn weiblich sind, beträgt etwa 36 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Summe als „genau 10“ oder „mindestens 10“ deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,3590). Typ wiederverwendet (2026-ga-B). Landesheft 2020-be-gk 4.2 b (abgewandelt: dort zwei Summanden k = 13 und 14 bei n = 50; dort vorgemerkt).")
row("2020MgrundlegendBStochastikWTR1", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", typ_neben="",
    stichwoerter="nicht weiblich dreimal so viele: a + 3a = 40 ⇔ a = 10|B(40; 0,29; 10) ≈ 12,3 %",
    voraussetzungen="Anzahl aus dem Verhältnis|Bernoulli-Formel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=U1,
    gesucht="Wahrscheinlichkeit, dass die Anzahl der nicht weiblichen dreimal so groß ist wie die der weiblichen",
    verfahren="Anzahl 10 weibliche aus a + 3a = 40, dann P(X = 10)",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="B(40; 0,29; 10) ≈ 12,3 % (amtlich)",
    zwischenergebnis="a = 10", niveau_geschaetzt="I",
    fehlerquelle="P(X = 30) (nicht weibliche) mit p = 0,29 berechnen",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,1231). Typ wiederverwendet (2019-be-gk). Landesheft 2020-be-gk 4.2 c (abgewandelt: dort viermal so groß bei n = 50; dort vorgemerkt).")
row("2020MgrundlegendBStochastikWTR1", "d", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen", typ_neben="",
    stichwoerter="E(X) = 40 · 0,29 = 11,6|größter Wert der Verteilung bei einer der beiden zu 11,6 benachbarten natürlichen Zahlen: 11 oder 12",
    voraussetzungen="Erwartungswert n · p|Lage des Maximums einer Binomialverteilung",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=U1,
    gesucht="Begründung ohne Berechnung von Wahrscheinlichkeiten, dass die Verteilung von X bei 11 oder 12 den größten Wert hat",
    verfahren="Erwartungswert berechnen; das Maximum liegt bei einer der beiden benachbarten ganzen Zahlen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="E(X) = 40 · 0,29 = 11,6; damit hat die Wahrscheinlichkeitsverteilung von X ihren größten Wert für eine der beiden zu 11,6 benachbarten natürlichen Zahlen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Maximum bei n/2 = 20 vermuten",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (P(X = 11) ≈ 0,1370, P(X = 12) ≈ 0,1353). Typ wiederverwendet (2025-ga-B). Landesheft 2020-be-gk 4.2 d (abgewandelt: dort 16 oder 17 bei n = 50, p = 1/3; dort vorgemerkt).")
U2 = ("Befragung im Unternehmen (29 % der Beschäftigten weiblich): 3,5 % der weiblichen und 10,5 % der anderen Beschäftigten sind unzufrieden; "
      "eine Person wird zufällig ausgewählt; Baumdiagramm mit erster Stufe w / nicht w, zweiter Stufe u / nicht u, an den Ästen x (nicht w, dann nicht u) und y (Pfad w und u)")
U2_SK = ("Baumdiagramm: Wurzel, erste Stufe w und w̄ (Kästchen), zweite Stufe je u und ū; y steht am Ende des Pfads w → u, x am Ast w̄ → ū; "
         "alle übrigen Wahrscheinlichkeiten fehlen")
row("2020MgrundlegendBStochastikWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Fehlende Wahrscheinlichkeiten im Baumdiagramm über die Pfadregel ermitteln", typ_neben="",
    stichwoerter="x = 100 % − 10,5 % = 89,5 %|y = 0,29 · 0,035 ≈ 0,01",
    voraussetzungen="Summenregel an einem Knoten|Pfadregel",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=U2_SK, kontext="Unternehmen / Beschäftigte", textumfang="mittel",
    gegeben=U2,
    gesucht="Werte von x und y",
    verfahren="x als Gegenwahrscheinlichkeit am Knoten nicht w; y als Pfadprodukt 0,29 · 0,035",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="x = 100 % − 10,5 % = 89,5 %; y = 0,29 · 0,035 ≈ 0,01 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="y als Astwahrscheinlichkeit 0,035 statt als Pfadprodukt angeben",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,01015). Typ wiederverwendet (2026-ga-A). Landesheft 2020-be-gk 4.2 e (dort mit 1/3 statt 29 % weiblich, sonst wortgleich; dort vorgemerkt).")
row("2020MgrundlegendBStochastikWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(u) = 0,71 · 0,105 + 0,29 · 0,035|P(nicht w ∩ u) = 0,71 · 0,105|0,71 · 0,105 / (0,71 · 0,105 + 0,29 · 0,035) ≈ 88,0 %",
    voraussetzungen="totale Wahrscheinlichkeit|bedingte Wahrscheinlichkeit als Quotient",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=U2_SK, kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=U2 + "; die ausgewählte Person ist unzufrieden",
    gesucht="Wahrscheinlichkeit, dass sie nicht weiblich ist",
    verfahren="P(nicht w ∩ u) durch P(u)",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2020MgrundlegendBStochastikWTR1-2a",
    ergebnis="0,71 · 0,105 / (0,71 · 0,105 + 0,29 · 0,035) ≈ 88,0 % (amtlich)",
    zwischenergebnis="P(u) ≈ 8,47 %", niveau_geschaetzt="II",
    fehlerquelle="P(u) nur aus einem Ast bilden",
    bemerkung="Standardbezug: K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,8802). Typ wiederverwendet (2024-ea-B). Landesheft 2020-be-gk 4.2 f (dort mit 1/3 statt 29 % weiblich, Ergebnis 85,7 %; dort vorgemerkt).")
row("2020MgrundlegendBStochastikWTR1", "c", innen="2", seite="2", punkte="4", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil aus einem Verhältnis zweier Pfadwahrscheinlichkeiten berechnen", typ_neben="",
    stichwoerter="Anteil a weiblich|5 · 0,04 · a = 0,1 · (1 − a)|0,3a = 0,1 ⇔ a = 1/3",
    voraussetzungen="Pfadwahrscheinlichkeiten mit unbekanntem Anteil|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="mittel",
    gegeben="Abteilung des Unternehmens: 4 % der weiblichen und 10 % der anderen Beschäftigten sind unzufrieden; der Anteil der unzufriedenen nicht weiblichen Beschäftigten ist fünfmal so groß wie der Anteil der unzufriedenen weiblichen",
    gesucht="Anteil der weiblichen Beschäftigten in der Abteilung",
    verfahren="Anteil a ansetzen, Pfadprodukte ins Verhältnis setzen und die lineare Gleichung lösen",
    schritte="3", zahlenraum="dezimal|Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Mit dem Anteil a der weiblichen Beschäftigten gilt 5 · 0,04 · a = 0,1 · (1 − a) ⇔ 0,3a = 0,1 ⇔ a = 1/3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das Verhältnis der bedingten Anteile (10 % zu 4 %) statt der Pfadwahrscheinlichkeiten ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2020-be-gk). Landesheft 2020-be-gk 4.2 g (wortgleich; dort vorgemerkt).")
# ---- Stochastik WTR 2: Postunternehmen Q (1 a–d, 12 BE; 2 a–c, 8 BE)
P1 = ("Postunternehmen Q befördert jährlich etwa 60 Millionen Briefe und stellt 95 % aller Briefe am ersten Werktag nach der Einlieferung zu; "
      "für 2000 zufällig ausgewählte Briefe wird untersucht, ob sie am ersten Werktag zugestellt werden")
row("2020MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialverteilung einer Zufallsgröße über die Bernoulli-Bedingungen begründen", typ_neben="",
    stichwoerter="je Brief nur zugestellt oder nicht|2000 aus sehr vielen Briefen zufällig gewählt: Wahrscheinlichkeit 0,95 bei jedem Brief praktisch gleich|feste Anzahl n = 2000",
    voraussetzungen="Bernoulli-Kette: zwei Ausgänge, feste Länge, konstante Wahrscheinlichkeit",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Postzustellung", textumfang="mittel",
    gegeben=P1,
    gesucht="Begründung, dass die Binomialverteilung für Vorhersagen geeignet ist",
    verfahren="Bernoulli-Bedingungen im Sachzusammenhang nennen",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Für jeden Brief wird nur untersucht, ob er am ersten Werktag zugestellt wird oder nicht; da die 2000 Briefe aus der sehr großen Anzahl zufällig ausgewählt sind, ist die Wahrscheinlichkeit für eine Zustellung bei allen gleich groß (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Unabhängigkeit bzw. gleiche Wahrscheinlichkeit trotz Ziehens ohne Zurücklegen nicht begründen",
    bemerkung="Standardbezug: K1 I, K3 II, K6 II. AB amtlich: II. Amtlich. Typ wiederverwendet (2023-ga-B).")
row("2020MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="X: Anzahl der am ersten Werktag zugestellten Briefe, B(2000; 0,95)|P(A) = P(X ≥ 1900) ≈ 52,7 %|P(B) = P(X < 1900) = 1 − P(X ≥ 1900) ≈ 47,3 %",
    voraussetzungen="Ereignis in die Zufallsgröße übersetzen|kumulierte Binomialverteilung mit dem Rechner|Gegenereignis",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Postzustellung", textumfang="mittel",
    gegeben=P1 + "; A: mindestens 1900 der Briefe werden am ersten Werktag zugestellt; B: mehr als 100 der Briefe werden nicht am ersten Werktag zugestellt",
    gesucht="P(A) und P(B)",
    verfahren="P(X ≥ 1900) mit dem Rechner; B als Gegenereignis von A",
    schritte="3", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(A) = P(X ≥ 1900) ≈ 52,7 %; P(B) = 1 − P(X ≥ 1900) ≈ 47,3 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="B als „mindestens 100 nicht zugestellt“ lesen und P(X ≤ 1900) rechnen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,5266 und 0,4734). Typ wiederverwendet (2026-ga-B).")
row("2020MgrundlegendBStochastikWTR2", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Summenterme der Binomialverteilung auf ein vorgegebenes Mindestens-Ereignis prüfen und begründen", typ_neben="",
    stichwoerter="Ereignis: mindestens 100 Briefe nicht am ersten Werktag zugestellt ⇔ X ≤ 1900|Term I = 1 − Σ_(k=101)^2000 (2000 über k) · 0,05ᵏ · 0,95^(2000−k) = P(höchstens 100 nicht zugestellt): nein|Term II = Σ_(k=0)^1900 (2000 über k) · 0,95ᵏ · 0,05^(2000−k) = P(X ≤ 1900): ja",
    voraussetzungen="Summenterm als kumulierte Wahrscheinlichkeit lesen|Erfolg und Misserfolg vertauschen|Gegenereignis",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Postzustellung", textumfang="lang",
    gegeben=P1 + "; Term I: 1 − Σ_(k=101)^2000 (2000 über k) · 0,05ᵏ · 0,95^(2000−k); Term II: Σ_(k=0)^1900 (2000 über k) · 0,95ᵏ · 0,05^(2000−k); Ereignis: mindestens 100 der Briefe werden nicht am ersten Werktag zugestellt",
    gesucht="für jeden Term die Entscheidung mit Begründung, ob er die Wahrscheinlichkeit des Ereignisses angibt",
    verfahren="Beide Terme als Wahrscheinlichkeit einer Zufallsgröße (nicht zugestellte bzw. zugestellte Briefe) lesen und mit dem Ereignis vergleichen",
    schritte="2", zahlenraum="Potenz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Term I gibt die Wahrscheinlichkeit nicht an: er beschreibt, dass höchstens 100 Briefe nicht am ersten Werktag zugestellt werden. Term II gibt sie an: höchstens 1900 Briefe am ersten Werktag, also mindestens 100 nicht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Term I wegen der Wahrscheinlichkeit 0,05 für „nicht zugestellt“ vorschnell bejahen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K5 II. AB amtlich: II. Amtlich.")
row("2020MgrundlegendBStochastikWTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Stichprobenumfang für eine verdoppelte Standardabweichung der Binomialverteilung ermitteln", typ_neben="",
    stichwoerter="σ = √(n · 0,95 · 0,05)|2 · √(2000 · 0,95 · 0,05) = √(8000 · 0,95 · 0,05)|n = 8000",
    voraussetzungen="Standardabweichung der Binomialverteilung|Verdopplung von σ bedeutet Vervierfachung von n",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Postzustellung", textumfang="kurz",
    gegeben=P1,
    gesucht="Anzahl der Briefe, bei der die Standardabweichung der Anzahl der zugestellten Briefe doppelt so groß ist wie bei 2000",
    verfahren="σ-Formel ansetzen, Faktor 2 unter die Wurzel als Faktor 4 bei n",
    schritte="2", zahlenraum="Wurzel|ganz", einheiten="", abhaengig_von="",
    ergebnis="2 · √(2000 · 0,95 · 0,05) = √(8000 · 0,95 · 0,05), d. h. es müssten 8000 Briefe ausgewählt werden (amtlich)",
    zwischenergebnis="σ₂₀₀₀ ≈ 9,75", niveau_geschaetzt="II",
    fehlerquelle="n verdoppeln statt vervierfachen",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
P2 = ("Große Firma versendet einen Teil ihrer Briefe mit Q (95 % am ersten Werktag zugestellt), den anderen Teil mit einem anderen Unternehmen; "
      "Baumdiagramm (Abb. 1): Q mit 0,6, dann E (zugestellt) 0,95 und Ē 0,05; nicht Q mit 0,4, dann E und Ē mit a; ein Brief wird zufällig ausgewählt")
P2_SK = ("Abb. 1: Baumdiagramm mit Wurzel, erste Stufe Q (0,6) und Q̄ (0,4), zweite Stufe nach Q: E (0,95) und Ē (0,05); nach Q̄: E (ohne Angabe) und Ē (a)")
row("2020MgrundlegendBStochastikWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil über die totale Wahrscheinlichkeit aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="a = 0,25|0,6 · 0,05 + 0,4 · 0,25 = 0,13",
    voraussetzungen="Pfadregel und Summenregel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=P2_SK, kontext="Postzustellung", textumfang="mittel",
    gegeben=P2 + "; a = 0,25",
    gesucht="Wahrscheinlichkeit, dass der ausgewählte Brief nicht am ersten Werktag zugestellt wird",
    verfahren="Beide Pfade zu Ē multiplizieren und addieren",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,6 · 0,05 + 0,4 · 0,25 = 0,13 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur den Pfad über Q rechnen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2022-ga-B).")
row("2020MgrundlegendBStochastikWTR2", "b", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Unabhängigkeit über den Vergleich zweier bedingter Anteile untersuchen", typ_neben="",
    stichwoerter="P(E | Q) = 0,95, P(E | nicht Q) = 1 − 0,25 = 0,75|verschieden: abhängig",
    voraussetzungen="Unabhängigkeit ⇔ gleiche bedingte Wahrscheinlichkeiten",
    format="Rechnung", operator="Prüfen Sie", antwort="Text",
    material="Diagramm", skizze=P2_SK, kontext="Postzustellung", textumfang="mittel",
    gegeben=P2 + "; a = 0,25; Ereignisse „Brief wird von Q befördert“ und „Brief wird am ersten Werktag zugestellt“",
    gesucht="Prüfung auf stochastische Unabhängigkeit",
    verfahren="Zustellwahrscheinlichkeiten bei Q und beim anderen Unternehmen vergleichen",
    schritte="1", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Bei Beförderung durch Q beträgt die Zustellwahrscheinlichkeit 95 %, beim anderen Unternehmen 75 %; die Ereignisse sind stochastisch abhängig (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Produktregel mit P(Q ∩ E) = 0,6 · 0,95 gegen P(Q) · P(E) rechnen und sich verrechnen",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2022-bebb-gk).")
P2_SK2 = ("Abb. 2: Koordinatensystem a von 0 bis 1, Werte 0 bis 1,2 (Gitter 0,2); vier Graphen: A gestrichelt von (0 | 1) leicht steigend nach (1 | 1,2); "
          "B Gerade von (0 | 1) nach (1 | 0); C gepunktet von (0 | 0,6) fallend nach (1 | 0,2); D strichpunktiert von (0 | 1) steil fallend, dann flach gegen etwa 0,1 bei a = 1")
row("2020MgrundlegendBStochastikWTR2", "c", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Graph einer bedingten Wahrscheinlichkeit in Abhängigkeit von einem Parameter über Randwerte ohne Rechnung zuordnen", typ_neben="",
    stichwoerter="gesucht P(Q | nicht E) als Funktion von a|a = 0: der andere Anbieter stellt immer zu, nicht zugestellte Briefe stammen sicher von Q: Wert 1|a = 1: Wert größer als 0 (Q liefert weiter 5 % nicht zu)|nur Graph D",
    voraussetzungen="Bedeutung von a im Baumdiagramm|bedingte Wahrscheinlichkeit qualitativ|Randwerte eines Graphen prüfen",
    format="Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Diagramm", skizze=P2_SK + "; " + P2_SK2, kontext="Postzustellung", textumfang="lang",
    gegeben=P2 + "; der ausgewählte Brief wurde nicht am ersten Werktag zugestellt; Abb. 2 zeigt vier Graphen A bis D in Abhängigkeit von a",
    gesucht="der Graph, der P(Q | nicht zugestellt) in Abhängigkeit von a darstellt, mit Begründung ohne Rechnung",
    verfahren="Werte für a = 0 (sicher Q, also 1) und a = 1 (größer als 0) überlegen und mit den Graphen vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Die Wahrscheinlichkeit ist maximal 1 und wird für a = 0 angenommen (dann stammt jeder nicht zugestellte Brief sicher von Q); auch für a = 1 ist sie größer als 0; das erfüllt nur Graph D (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Graph B wählen, weil die Wahrscheinlichkeit mit a fällt, ohne den Wert bei a = 1 zu prüfen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II, K4 II, K6 II. AB amtlich: III. Amtlich; eigene Rechnung: P(Q | Ē) = 0,03/(0,03 + 0,4a), also 1 bei a = 0 und 0,07 bei a = 1.")

NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Gemeinsame Punkte zweier Graphen als einzige durch Ausklammern nachweisen", "Analysis", "Gleichungen lösen",
     "Zwei Funktionsterme gleichsetzen, die Differenz faktorisieren (x² ausklammern) und aus dem Produkt gleich null die einzigen Schnittstellen samt Punkten angeben.", "2020MgrundlegendBAnalysisWTR1-1a"),
    ("Ableitung eines ganzrationalen Produkts durch Ausmultiplizieren nachweisen", "Analysis", "Ableitungsregeln",
     "Einen als Produkt gegebenen ganzrationalen Term ausmultiplizieren und mit der Potenzregel den vorgegebenen Ableitungsterm bestätigen.", "2020MgrundlegendBAnalysisWTR1-1a"),
    ("Aussage über den Vergleich der Steigungen zweier Graphen auf einem Intervall mit Gegenbeispiel beurteilen", "Analysis", "Ableitung und Änderungsrate",
     "Eine Allaussage über die Steigungen zweier Graphen auf einem Intervall durch eine Stelle widerlegen, an der die Ableitungswerte die Aussage verletzen.", "2020MgrundlegendBAnalysisWTR1-1c"),
    ("Nullstellen und Werte: Ausdehnung einer Figur in x-Richtung aus der Ausdehnung in y-Richtung über Funktionswerte ermitteln", "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus der vorgegebenen Höhe einer von Graphen begrenzten Figur den Funktionswert eines Randpunkts bestimmen, die zugehörige Stelle über die Funktionsgleichung berechnen und daraus die Breite der Figur bilden.", "2020MgrundlegendBAnalysisWTR1-1d"),
    ("Fläche: Aufgabenstellung zu einer Summe zweier Integrale formulieren und die Integrale als Teilflächen im Sachzusammenhang deuten", "Analysis", "Flächeninhalt durch Integration",
     "Zu einem vorgegebenen Term aus zwei Integralen über Differenzfunktionen eine passende Aufgabe im Sachzusammenhang nennen und jedes Integral als Flächenstück zwischen den beteiligten Graphen bzw. Geraden beschreiben.", "2020MgrundlegendBAnalysisWTR1-1f"),
    ("Wendepunkt einer Schar im Ursprung mit der x-Achse als Wendetangente nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Für eine Schar kubischer Parabeln den Wendepunkt im Ursprung angeben und über die Ableitung an der Stelle 0 zeigen, dass die x-Achse dort für alle Parameterwerte Tangente ist.", "2020MgrundlegendBAnalysisWTR1-1g"),
    ("Parameter einer Schar aus einer vorgegebenen Ausdehnung einer Figur bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus der vorgegebenen Höhe einer von einer Scharkurve begrenzten Figur den Funktionswert an einer festen Stelle ableiten und die entstehende lineare Gleichung nach dem Parameter lösen.", "2020MgrundlegendBAnalysisWTR1-1h"),
    ("Parameter einer Schar aus gleichen Winkeln zweier Graphen mit einer Strecke bestimmen und Lage eines Punktes prüfen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameter so bestimmen, dass zwei Graphen mit einer senkrechten Strecke gleiche Winkel einschließen (entgegengesetzt gleiche Steigungen), und anschließend einen abhängigen Punkt gegen eine Schranke prüfen.", "2020MgrundlegendBAnalysisWTR1-1i"),
    ("Tangente durch einen vorgegebenen Punkt am Graphen einzeichnen und ihre Gleichung ablesen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Eine Tangente an einen abgebildeten Graphen durch einen vorgegebenen Punkt außerhalb des Graphen zeichnerisch anlegen und ihre Gleichung aus Achsenabschnitt und abgelesener Steigung angeben.", "2020MgrundlegendBAnalysisWTR2-1c"),
    ("Steigungswinkel des Graphen in einem Punkt über die Ableitung berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Steigungswinkel eines Graphen in einem Punkt als Arkustangens des Ableitungswerts berechnen.", "2020MgrundlegendBAnalysisWTR2-1d"),
    ("Integralwert: Integral als Flächeninhalt zwischen Graph und x-Achse deuten und über die Stammfunktion berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Ein bestimmtes Integral über einen nichtnegativen Integranden als Flächeninhalt zwischen Graph und x-Achse beschreiben und mit einer vorgegebenen Stammfunktion berechnen.", "2020MgrundlegendBAnalysisWTR2-1f"),
    ("Integralwert: Existenz einer oberen Grenze mit Integralwert null über den Flächenausgleich ohne Rechnung begründen", "Analysis", "Flächeninhalt durch Integration",
     "Ohne Rechnung begründen, dass es eine obere Integrationsgrenze gibt, für die sich die Flächenstücke oberhalb und unterhalb der x-Achse ausgleichen, weil der Graph nach der Nullstelle unbeschränkt negativ wird.", "2020MgrundlegendBAnalysisWTR2-1g"),
    ("Tiefpunkt aller Stammfunktionen auf der y-Achse über den Vorzeichenwechsel von f begründen und Stammfunktion mit Tiefpunkt im Ursprung bestimmen", "Analysis", "Stammfunktion und Hauptsatz",
     "Aus dem Vorzeichenwechsel des Integranden bei 0 folgern, dass jede Stammfunktion dort einen Tiefpunkt hat, und die Integrationskonstante so wählen, dass der Tiefpunkt im Ursprung liegt.", "2020MgrundlegendBAnalysisWTR2-1h"),
    ("Gemeinsamen Punkt von Scharkurve und ihrem Ableitungsgraphen in Abhängigkeit vom Parameter berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Scharfunktion und ihre Ableitung gleichsetzen, den gemeinsamen positiven Faktor kürzen und die x-Koordinate des gemeinsamen Punkts als Term im Parameter angeben.", "2020MgrundlegendBAnalysisWTR2-2b"),
    ("Fläche: Flächenstück zwischen zwei Scharkurven und der x-Achse markieren und Gleichung für den Parameter aus dem Flächeninhalt angeben", "Analysis", "Flächeninhalt durch Integration",
     "Das von zwei benachbarten Scharkurven und der x-Achse begrenzte Flächenstück in der Abbildung markieren und seinen Inhalt als Differenz der Beträge zweier Integrale ansetzen, um daraus eine Gleichung für den Parameter zu erhalten.", "2020MgrundlegendBAnalysisWTR2-2c"),
    ("Verflechtung: Matrix-Vektor-Gleichung mit konkreten Zahlen im Sachzusammenhang deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine Gleichung der Form Bedarfsvektor = Matrix · Mengenvektor mit konkreten Zahlen als Aussage über benötigte Mengen im Herstellungsprozess formulieren.", "2020MgrundlegendBAGLAA1WTR-1a"),
    ("Ebene Figur: Raute über gleiche Seitenvektoren nachweisen und Quadrat über das Skalarprodukt ausschließen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Ein Viereck über gleiche gegenüberliegende Seitenvektoren als Parallelogramm, über gleiche Seitenlängen als Raute nachweisen und mit einem Skalarprodukt ungleich null ausschließen, dass es ein Quadrat ist.", "2020MgrundlegendBAGLAA1WTR-2a"),
    ("Ebene Figur: Flächenformel einer Raute als halbes Diagonalenprodukt mit einer Skizze begründen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "An einer Skizze begründen, dass der Flächeninhalt einer Raute die Hälfte des Rechtecks mit den Diagonalenlängen als Seiten ist.", "2020MgrundlegendBAGLAA1WTR-2b"),
    ("Ebene Figur: Berührpunkt des Inkreises einer Raute über Lage auf der Seite und Orthogonalität zum Mittelpunkt begründen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Für einen vorgegebenen Punkt zeigen, dass er auf einer Rautenseite liegt und dass seine Verbindung zum Diagonalenschnittpunkt senkrecht auf der Seite steht, damit er Berührpunkt des einbeschriebenen Kreises ist.", "2020MgrundlegendBAGLAA1WTR-2c"),
    ("Konstante einer Koordinatengleichung durch Einsetzen eines Punktes bestimmen", "Analytische Geometrie", "Ebenen",
     "Die rechte Seite einer Koordinatengleichung mit vorgegebenen Koeffizienten durch Einsetzen eines Punktes der Ebene berechnen.", "2020MgrundlegendBAGLAA2WTR-1a"),
    ("Neigung einer Ebene in Prozent über den Winkel zur Koordinatenebene prüfen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Den Winkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen und seinen Tangens als Neigung in Prozent mit einer Vorgabe vergleichen.", "2020MgrundlegendBAGLAA2WTR-1b"),
    ("Punkt: Ursprüngliche Länge einer Strecke aus der Streckenlänge und einer prozentualen Verlängerung berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Die Länge einer Strecke aus den Koordinaten berechnen und über eine angegebene prozentuale Verlängerung auf die ursprüngliche Länge zurückrechnen.", "2020MgrundlegendBAGLAA2WTR-1c"),
    ("Ebene Figur: Schattendreieck in der Grundebene zeichnen und seinen Flächeninhalt berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Die drei Schattenpunkte einer Dreiecksfläche in einem ebenen Koordinatensystem darstellen und den Flächeninhalt des Schattendreiecks über Grundseite und Höhe berechnen.", "2020MgrundlegendBAGLAA2WTR-1e"),
    ("Dreieck: Gleichung für den Parameter des flächenkleinsten gleichschenkligen Dreiecks über die Orthogonalität von Höhe und Gerade begründen", "Analytische Geometrie", "Orthogonalität",
     "Begründen, dass unter gleichschenkligen Dreiecken mit fester Basis und Spitze auf einer Geraden das flächenkleinste dasjenige ist, dessen Höhe senkrecht auf der Geraden steht, und dies als Skalarproduktgleichung im Parameter ausdrücken.", "2020MgrundlegendBAGLAA2WTR-2"),
    ("Summenterme der Binomialverteilung auf ein vorgegebenes Mindestens-Ereignis prüfen und begründen", "Stochastik", "Binomialverteilung",
     "Für vorgegebene Summenterme mit Binomialkoeffizienten entscheiden und begründen, ob sie die Wahrscheinlichkeit eines Mindestens-Ereignisses angeben, wobei Erfolg und Misserfolg vertauscht sein können.", "2020MgrundlegendBStochastikWTR2-1c"),
    ("Stichprobenumfang für eine verdoppelte Standardabweichung der Binomialverteilung ermitteln", "Stochastik", "Kenngrößen von Verteilungen",
     "Über σ = √(n · p · (1 − p)) den Stichprobenumfang bestimmen, bei dem die Standardabweichung doppelt so groß ist wie bei einem gegebenen Umfang.", "2020MgrundlegendBStochastikWTR2-1d"),
    ("Graph einer bedingten Wahrscheinlichkeit in Abhängigkeit von einem Parameter über Randwerte ohne Rechnung zuordnen", "Stochastik", "Bedingte Wahrscheinlichkeit und Bayes",
     "Unter mehreren abgebildeten Graphen denjenigen einer bedingten Wahrscheinlichkeit als Funktion eines Parameters über die Werte an den Rändern des Parameterbereichs auswählen und begründen.", "2020MgrundlegendBStochastikWTR2-2c"),
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
