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
    "stapel": "2025-ea-B-mms",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2025MerhoehtBAnalysisMMS1": 30, "2025MerhoehtBAnalysisMMS2": 30, "2025MerhoehtBAGLAA1MMS": 20, "2025MerhoehtBAGLAA2MMS": 20,
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
# Stapel 2025-ea-B (MMS-Zweig; Reserve, geöffnet 17.09.2026 in Auftrag C Teil 2 wegen der
# sieben Landesheftverweise von 2025-bebb-lk 2.1 a, c–h auf Analysis MMS 1). Vier nicht
# wortgleiche Dateien (Analysis MMS 1 und 2, AG/LA (A1) MMS, AG/LA (A2) MMS); Stochastik
# MMS 1–3 sind Dubletten der WTR-Dateien und bekommen keine Zeile. Standardbezug mit Spalte
# Anforderungsbereich; Analysis 30 BE, AG/LA je 20 BE; AG/LA (A2) MMS ohne Aufgabennummer.
# ---- Analysis MMS 1: Schar f_k = 1/(2k) · x² · (x − 2k)² (1 a–d, 16 BE) und Regenwasser-Auffangbecken (2 a–d, 14 BE)
# Landesheft 2025-bebb-lk 2.1 a, c, d, e, f, g, h vorgemerkt (WTR-Fassung des Landes; a, d, g, h wortgleich)
E1 = "Schar f_k(x) = 1/(2k) · x² · (x − 2k)², k > 0, in IR definiert; Graph G_k"
row("2025MerhoehtBAnalysisMMS1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Genau zwei Nullstellen einer Schar aus der faktorisierten Form begründen und angeben", typ_neben="",
    stichwoerter="Produkt x² · (x − 2k)² = 0 ⇔ x = 0 ∨ x = 2k|wegen k > 0 zwei verschiedene Stellen",
    voraussetzungen="Produkt gleich null|Faktorisierte Form lesen",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=E1,
    gesucht="Begründung, dass f_k für jedes k genau zwei Nullstellen hat; die Nullstellen",
    verfahren="Faktoren null setzen, k > 0 nutzen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="0 und 2k; wegen k > 0 gibt es genau zwei Nullstellen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die doppelten Nullstellen als vier Nullstellen zählen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ aus der Landeszeile 2025-bebb-lk 2.1 a (wortgleich; dort vorgemerkt). MMS-Anteil: keiner.")
row("2025MerhoehtBAnalysisMMS1", "b", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Abstand des Hochpunkts zu den Tiefpunkten einer Schar in Abhängigkeit vom Parameter berechnen", typ_neben="",
    stichwoerter="f_k'(x) = 0 ⇔ x = 0 ∨ x = k ∨ x = 2k|Hochpunkt (k | k³/2), Tiefpunkte (0 | 0), (2k | 0)|Abstand √(k² + (k³/2)²) = k · √(k⁴ + 4)/2",
    voraussetzungen="Extremstellen über die Ableitung (Rechner)|Abstand zweier Punkte|Symmetrie zu x = k",
    format="Rechnung", operator="Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=E1 + "; der Hochpunkt von G_k hat zu den beiden Tiefpunkten denselben Abstand",
    gesucht="dieser Abstand",
    verfahren="Extremstellen mit dem Rechner, Hochpunkt (k | f_k(k)), Abstand zum Tiefpunkt (0 | 0)",
    schritte="3", zahlenraum="Wurzel|Potenz", einheiten="", abhaengig_von="2025MerhoehtBAnalysisMMS1-1a",
    ergebnis="f_k'(x) = 0 ⇔ x = 0 ∨ x = k ∨ x = 2k; √((k − 0)² + (f_k(k) − f_k(0))²) = k · √(k⁴ + 4)/2 (amtlich)",
    zwischenergebnis="f_k(k) = k³/2", niveau_geschaetzt="II",
    fehlerquelle="Abstand nur in x-Richtung (k) angeben",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ aus der Landeszeile 2025-bebb-lk 2.1 c (abgewandelt: das Heft gibt f_k' vor und fragt „in Abhängigkeit von k“, 5 BE; dort vorgemerkt). MMS-Anteil: Rechner für Ableitung und Nullstellen, Ansatz eigen.")
row("2025MerhoehtBAnalysisMMS1", "c", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral als Flächeninhalt für alle Scharkurven über das Vorzeichen des Terms beurteilen", typ_neben="",
    stichwoerter="Aussage: ∫₋₁¹ f_k(x) dx ist für jedes k der Inhalt der Fläche zwischen G_k, x-Achse, x = −1, x = 1|Term = Produkt dreier nichtnegativer Faktoren 1/(2k), x², (x − 2k)²|kein Flächenstück unterhalb der x-Achse: richtig",
    voraussetzungen="Integral als orientierte Fläche|Vorzeichen eines Produkts",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=E1 + "; Fläche zwischen G_k, x-Achse und den Geraden x = −1 und x = 1 aus mehreren Flächenstücken; Aussage: für jeden Wert von k gibt ∫₋₁¹ f_k(x) dx den Inhalt dieser Fläche an",
    gesucht="Beurteilung der Aussage ohne Berechnung eines Integrals",
    verfahren="Nichtnegativität von f_k am Produkt begründen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Der Term ist ein Produkt dreier Faktoren, die nur nichtnegative Werte annehmen (1/(2k) > 0, x² und (x − 2k)² Quadrate); es gibt keine Flächenstücke unterhalb der x-Achse, die Aussage ist richtig (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="wegen der Nullstelle 2k im Intervall (für k ≤ 1/2) einen Vorzeichenwechsel vermuten",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I, K6 II. AB amtlich: II. Amtlich. Typ aus der Landeszeile 2025-bebb-lk 2.1 d (wortgleich; dort vorgemerkt). MMS-Anteil: keiner.")
row("2025MerhoehtBAnalysisMMS1", "d", innen="1", seite="1", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Aussage über den Flächeninhalt zwischen zwei Scharkurven als Parameterungleichung untersuchen", typ_neben="",
    stichwoerter="f_k(x) = h_k(x) ⇔ x = −k ∨ x = k ∨ x = 2k|Inhalt ∫₋ₖᵏ (h_k − f_k) dx + ∫ₖ²ᵏ (f_k − h_k) dx = 29/10 · k⁴|29/10 · k⁴ < k⁵ ⇔ k > 29/10: für alle k > 3 richtig",
    voraussetzungen="Schnittstellen zweier Scharkurven (Rechner)|Fläche zwischen Graphen mit Vorzeichenwechsel|Ungleichung in k",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=E1 + "; h_k(x) = k/2 · (x − 2k)², in IR definiert; G_k und der Graph von h_k schließen eine Fläche aus zwei Flächenstücken ein; Aussage: für k > 3 ist der Inhalt der Fläche kleiner als k⁵",
    gesucht="Untersuchung, ob die Aussage richtig ist",
    verfahren="Schnittstellen bestimmen, Flächeninhalt als Summe zweier Integrale mit dem Rechner als Term in k, Ungleichung lösen",
    schritte="4", zahlenraum="Potenz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="f_k(x) = h_k(x) ⇔ x = −k ∨ x = k ∨ x = 2k; Flächeninhalt ∫₋ₖᵏ (h_k(x) − f_k(x)) dx + ∫ₖ²ᵏ (f_k(x) − h_k(x)) dx = 29/10 · k⁴; 29/10 · k⁴ < k⁵ gilt für k > 29/10, die Aussage ist für alle k > 3 richtig (amtlich)",
    zwischenergebnis="Schnittstellen −k, k, 2k", niveau_geschaetzt="III",
    fehlerquelle="nur ein Integral von −k bis 2k ohne Vorzeichenwechsel ansetzen",
    bemerkung="Standardbezug: K1 III, K2 II, K4 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Landesheft 2025-bebb-lk 2.1 e (abgewandelt: das Heft gibt die Schritte I und II vor und verlangt ihre Deutung; dort vorgemerkt). MMS-Anteil: Rechner für Schnittstellen und Integrale mit Parameter, Ansatz eigen.")
R2 = ("Regenwasser-Auffangbecken: momentane Zuflussrate r(x) = eˣ · f_(2,5)(x) für 0 ≤ x ≤ 5 (f_(2,5) aus der Schar mit k = 2,5), x Zeit in Stunden seit Beginn "
      "des Zuflusses, r(x) in m³/h")
R2_SK = ("Koordinatensystem x von 0 bis 5, y von 0 bis 180 (Schritte 20): Graph von r, von 0 flach steigend, ab x ≈ 2 steil bis zum Hochpunkt bei etwa (3,7 | 187), "
         "dann steil fallend auf 0 bei x = 5; Rechteck über [4; 5] mit Höhe 120 grau; Fläche unter dem Graphen über [4; 5] schraffiert")
row("2025MerhoehtBAnalysisMMS1", "a", innen="2", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Größte und kleinste Rate im Zeitraum über Ableitung und Randwerte berechnen", typ_neben="",
    stichwoerter="r'(x) = 0 liefert x = 0, x = (1 + √41)/2 ≈ 3,70 und x = 5|r(0) = 0, r(5) = 0, r((1 + √41)/2) ≈ 187|kleinste Rate 0 m³/h, größte etwa 187 m³/h",
    voraussetzungen="Extremwerte auf einem Intervall über Ableitung und Ränder (Rechner)",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Regenwasser / Auffangbecken", textumfang="lang",
    gegeben=R2,
    gesucht="größte und kleinste momentane Zuflussrate im Zeitraum",
    verfahren="Nullstellen von r' mit dem Rechner, Randwerte vergleichen",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="m³/h", abhaengig_von="",
    ergebnis="r'(x) = 0 liefert x = 0, x = (1 + √41)/2 und x = 5; r(0) = 0, r((1 + √41)/2) ≈ 187, r(5) = 0: kleinste Rate 0 m³/h, größte etwa 187 m³/h (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Ränder nicht prüfen und die kleinste Rate vergessen",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (187,16). Landesheft 2025-bebb-lk 2.1 f (abgewandelt: das Heft gibt r' vor und fragt nur den Zeitpunkt des Maximums; dort vorgemerkt). MMS-Anteil: Rechner für Ableitung und Gleichung, Ansatz eigen.")
row("2025MerhoehtBAnalysisMMS1", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Ableitungswert an der Wendestelle als stärksten Anstieg der Rate im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="r' hat auf [0; 5] mit r'(0) = 0, r'(5) = 0 und den Wendestellen x₀, x₁ ihr Maximum bei x₀|r'(x₀) ≈ 100,5: die Zuflussrate steigt zum Zeitpunkt x₀ am stärksten, mit etwa 100,5 m³/h je Stunde",
    voraussetzungen="Wendestelle als Extremstelle der Ableitung|Ableitung der Rate als Änderung der Rate",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Regenwasser / Auffangbecken", textumfang="mittel",
    gegeben=R2 + "; auf [0; 5] hat r genau zwei Wendestellen x₀ und x₁ mit r'(x₀) ≈ 100,5 und r'(x₁) ≈ −240,2; r'(0) = 0 und r'(5) = 0",
    gesucht="Bedeutung des Wertes r'(x₀) im Sachzusammenhang, wie sie aus diesen Angaben folgt",
    verfahren="r'(x₀) als Maximum von r' erkennen und als stärksten Anstieg der Zuflussrate deuten",
    schritte="1", zahlenraum="dezimal", einheiten="m³/h je Stunde", abhaengig_von="",
    ergebnis="Die momentane Zuflussrate steigt im betrachteten Zeitraum mit etwa 100,5 m³/h pro Stunde am stärksten zu dem durch x₀ beschriebenen Zeitpunkt an (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="r'(x₀) als Zuflussrate statt als Änderung der Zuflussrate deuten",
    bemerkung="Standardbezug: K1 I, K2 II, K3 II, K6 II. AB amtlich: II. Amtlich. MMS-Anteil: keiner.")
row("2025MerhoehtBAnalysisMMS1", "c", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integralabschätzung über ein Rechteck und Flächenvergleich am Graphen erläutern und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Rechteck über [4; 5] mit Höhe 120 (Inhalt 120) gegen die schraffierte Fläche unter dem Graphen|der graue Teil des Rechtecks über dem Graphen ist größer als der schraffierte Teil außerhalb des Rechtecks|∫₄⁵ r(x) dx < 120: in der letzten Stunde fließen weniger als 120 m³ zu",
    voraussetzungen="Integral als Fläche unter dem Graphen|Flächenvergleich am Bild",
    format="Begründung", operator="Erläutern Sie|Interpretieren Sie", antwort="Text",
    material="Koordinatensystem", skizze=R2_SK, kontext="Regenwasser / Auffangbecken", textumfang="mittel",
    gegeben=R2 + "; Abbildung mit Rechteck der Höhe 120 über [4; 5] und schraffierter Fläche unter dem Graphen; Aussage ∫₄⁵ r(x) dx < 120",
    gesucht="Erläuterung, wie die Eintragungen die Aussage begründen; Deutung im Sachzusammenhang",
    verfahren="Flächenbilanz Rechteck gegen Fläche unter dem Graphen am Bild, Integral als Zuflussmenge deuten",
    schritte="2", zahlenraum="ganz", einheiten="m³", abhaengig_von="",
    ergebnis="Das Rechteck mit Inhalt 120 hat einen größeren Inhalt als die schraffierte Fläche, weil die nicht schraffierte graue Fläche größer ist als der Teil der schraffierten Fläche außerhalb des Rechtecks; in der letzten Stunde sind weniger als 120 m³ Regenwasser zugeflossen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Integral mit dem Rechner ausrechnen statt am Bild zu argumentieren",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich; eigene Rechnung: ∫₄⁵ r ≈ 87,97. Typ aus der Landeszeile 2025-bebb-lk 2.1 g (wortgleich; dort vorgemerkt). MMS-Anteil: keiner.")
row("2025MerhoehtBAnalysisMMS1", "d", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Term für einen Bestand aus einer Rate über ein Integral angeben", typ_neben="",
    stichwoerter="Anfangsbestand 186 m³|Zufluss ∫₀ˣ r(t) dt|Abpumpen mit konstanter Rate c ab x = 3,5: − c · (x − 3,5)|V(x) = 186 + ∫₀ˣ r(t) dt − c · (x − 3,5)",
    voraussetzungen="Bestand als Anfangswert plus Integral der Rate|konstante Entnahme als linearer Term",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Regenwasser / Auffangbecken", textumfang="lang",
    gegeben=R2 + "; zu Beginn 186 m³ im Becken; nach 3,5 Stunden pumpt eine Pumpe bis zum Ende des Zeitraums mit konstanter Rate ab; der Zufluss folgt weiter r",
    gesucht="Term für das Wasservolumen zu einem beliebigen Zeitpunkt nach dem Einschalten der Pumpe",
    verfahren="Anfangsbestand, Integral der Rate und linearen Abpumpterm zusammensetzen",
    schritte="2", zahlenraum="dezimal", einheiten="m³", abhaengig_von="",
    ergebnis="186 + ∫₀ˣ r(t) dt − c · (x − 3,5), wobei c die konstante Entnahmerate der Pumpe in m³/h beschreibt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das Integral erst ab 3,5 beginnen lassen und den Zufluss davor vergessen",
    bemerkung="Standardbezug: K2 III, K3 III, K4 II, K5 II. AB amtlich: III. Amtlich. Typ aus der Landeszeile 2025-bebb-lk 2.1 h (wortgleich; dort vorgemerkt, Schätzung dort II – Vorrang des Amtlichen, die Landeszeile zieht im Abgleichlauf nach). Enge Fassung: Modellierung des Abpumpterms als eigene Entscheidung, verkettet mit der Integraldarstellung des Zuflusses – III. MMS-Anteil: keiner.")
# ---- Analysis MMS 2: Schar f_b = 1/16 · x² · e^(−bx + 4b) (1 a–c, 12 BE) und Wasserrutsche r = f_(0,25) (2 a–d, 18 BE)
F2 = "Schar f_b(x) = 1/16 · x² · e^(−b · x + 4b), b > 0, in IR definiert; Graph G_b"
row("2025MerhoehtBAnalysisMMS2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Grenzverhalten einer Schar angeben und parameterunabhängigen Funktionswert nachweisen", typ_neben="",
    stichwoerter="x → −∞: x² und e^(−bx + 4b) wachsen, f_b → +∞|x → +∞: e-Faktor dominiert, f_b → 0|f_b(4) = 1/16 · 16 · e⁰ = 1",
    voraussetzungen="Grenzverhalten von Polynom mal e-Funktion|Exponent null an der Stelle 4",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=F2,
    gesucht="Verhalten von f_b für x → −∞ und x → +∞; Nachweis, dass f_b(4) nicht von b abhängt",
    verfahren="Grenzwerte am Term ablesen, x = 4 einsetzen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="lim f_b(x) = +∞ für x → −∞, lim f_b(x) = 0 für x → +∞; f_b(4) = 1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Grenzwert für x → −∞ als 0 angeben",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner.")
row("2025MerhoehtBAnalysisMMS2", "b", innen="1", seite="1", punkte="6", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Lage und Art der Extrempunkte einer Schar bestimmen und Parameter für einen vorgegebenen Abstand der Extrempunkte berechnen", typ_neben="",
    stichwoerter="f_b'(x) = 0 ⇔ x = 0 ∨ x = 2/b|f_b''(0) = 1/8 · e^(4b) > 0, f_b''(2/b) = −1/8 · e^(4b − 2) < 0|Tiefpunkt (0 | 0), Hochpunkt (2/b | 1/(4b²) · e^(4b − 2))|Abstand 6: √((2/b)² + (1/(4b²) · e^(4b − 2))²) = 6 ⇒ b ≈ 0,34",
    voraussetzungen="Extrempunkte mit Parameter über f' und f'' (Rechner)|Abstand zweier Punkte|Gleichung numerisch lösen",
    format="Rechnung", operator="Bestimmen Sie|Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=F2,
    gesucht="Lage und Art der beiden Extrempunkte von G_b; ein Wert von b, für den die Extrempunkte den Abstand 6 haben, auf Hundertstel",
    verfahren="f_b' und f_b'' mit dem Rechner, Nullstellen und Vorzeichen; Abstandsgleichung numerisch lösen",
    schritte="4", zahlenraum="Bruch|Potenz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="f_b'(x) = 0 ⇔ x = 0 ∨ x = 2/b; f_b''(0) > 0, f_b''(2/b) < 0: Tiefpunkt (0 | 0), Hochpunkt (2/b | 1/(4b²) · e^(4b − 2)); √((2/b)² + (1/(4b²) · e^(4b − 2))²) = 6 hat die Lösung b₁ ≈ 0,34 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Abstand nur in x-Richtung ansetzen (2/b = 6)",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (b ≈ 0,3395). MMS-Anteil: Rechner für Ableitungen und die Abstandsgleichung, Ansatz eigen.")
row("2025MerhoehtBAnalysisMMS2", "c", innen="1", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Höchstens eine positive Nullstelle jeder Stammfunktion über die Monotonie aus dem Vorzeichen des Integranden begründen", typ_neben="",
    stichwoerter="F_b' = f_b > 0 für x > 0|F_b auf IR⁺ streng monoton wachsend|höchstens eine positive Nullstelle, also höchstens ein gemeinsamer Punkt mit der positiven x-Achse",
    voraussetzungen="Stammfunktion und Vorzeichen der Ableitung|streng monotone Funktion hat höchstens eine Nullstelle",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=F2 + "; Aussage: der Graph jeder Stammfunktion von f_b hat mit der positiven x-Achse höchstens einen gemeinsamen Punkt",
    gesucht="Begründung ohne Terme von Stammfunktionen",
    verfahren="Positivität von f_b für x > 0 in strenge Monotonie der Stammfunktion übersetzen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Für jede Stammfunktion F_b gilt F_b'(x) = f_b(x) > 0 für x > 0; F_b ist auf IR⁺ streng monoton wachsend und hat dort höchstens eine Nullstelle (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="mit F_b(0) argumentieren, das für verschiedene Stammfunktionen verschieden ist",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. AB amtlich: III. Amtlich. MMS-Anteil: keiner.")
W2 = ("Wasserrutsche: r(x) = 1/16 · x² · e^(−0,25x + 1) (= f_(0,25)), Graph G beschreibt für −4 ≤ x ≤ 10 die Profillinie der Rutschbahn, die x-Achse den Boden und die "
      "Wasseroberfläche, links ein horizontales Startpodest; 1 LE = 1 m")
W2_SK = ("Abb. 1: Koordinatensystem x von −7 bis 12, y von 0 bis 8: waagerechtes Startpodest von x = −6 bis −4 auf Höhe etwa 7,4, Startpunkt bei x = −4; Graph G steil "
         "fallend zur Mulde bei 0 (Boden), dann flach steigend zum Endpunkt bei x = 10 (Höhe etwa 1,4) über der Wasseroberfläche rechts")
row("2025MerhoehtBAnalysisMMS2", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Höhen an den Rändern einer Profillinie als Funktionswerte berechnen", typ_neben="",
    stichwoerter="r(−4) = e² ≈ 7,39: Höhe des Startpodests|r(10) ≈ 1,39: Höhe des Endpunkts",
    voraussetzungen="Funktionswerte an den Intervallrändern (Rechner)",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=W2_SK, kontext="Wasserrutsche", textumfang="lang",
    gegeben=W2,
    gesucht="Höhe des Startpodests über dem Boden und Höhe des Endpunkts über der Wasseroberfläche",
    verfahren="r(−4) und r(10) berechnen",
    schritte="2", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="r(−4) ≈ 7,39, d. h. das Startpodest liegt etwa 7,39 m hoch; r(10) ≈ 1,39, d. h. der Endpunkt liegt etwa 1,39 m über der Wasseroberfläche (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Höhe des Podests am Bild ablesen statt zu rechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (7,389 und 1,395). MMS-Anteil: Rechner für die Werte.")
row("2025MerhoehtBAnalysisMMS2", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Steigungswinkel und Nebenwinkel am Übergang zweier Profilstücke einzeichnen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="r'(−4) = tan α mit α ∈ ]−90°; 0°[: α ≈ −79,8° Steigungswinkel der Rutschbahn im Startpunkt|β = 180° − |α| ≈ 100,2°|β ist der Winkel zwischen Startpodest und Rutschbahn",
    voraussetzungen="Steigungswinkel über den Tangens|Nebenwinkel an der waagerechten Podestkante",
    format="Zeichnen|Kurzantwort", operator="Zeichnen Sie|Geben Sie an", antwort="Grafik|Text",
    material="Koordinatensystem", skizze=W2_SK, kontext="Wasserrutsche", textumfang="mittel",
    gegeben=W2 + "; Gleichungen r'(−4) = tan α mit α ∈ ]−90°; 0°[ und β = 180° − |α|",
    gesucht="Winkel α und β in Abbildung 1 einzeichnen; Bedeutung von β im Sachzusammenhang",
    verfahren="α als Winkel zwischen Tangente im Startpunkt und Waagerechter, β als Nebenwinkel zum Podest eintragen",
    schritte="2", zahlenraum="dezimal", einheiten="°", abhaengig_von="",
    ergebnis="β ist der Winkel zwischen Startpodest und Rutschbahn; Zeichnung: α zwischen der Tangente im Startpunkt und der Waagerechten, β als Nebenwinkel (amtlich)",
    zwischenergebnis="α ≈ −79,8°, β ≈ 100,2°", niveau_geschaetzt="II",
    fehlerquelle="β als Winkel zur Senkrechten deuten",
    bemerkung="Standardbezug: K2 II, K3 I, K4 II, K5 II, K6 II. AB amtlich: II. Amtlich; eigene Rechnung: r'(−4) ≈ −5,54, α ≈ −79,8°. MMS-Anteil: keiner (Zeichnung und Deutung).")
row("2025MerhoehtBAnalysisMMS2", "c", innen="2", seite="2", punkte="6", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Wasservolumen in einer Mulde aus Fläche zwischen Wasserlinie und Graph mal Breite berechnen", typ_neben="",
    stichwoerter="r(x) = 0,05 auf [−4; 10]: x₁ ≈ −0,51, x₂ ≈ 0,58|Querschnitt ∫_(x₁)^(x₂) (0,05 − r(x)) dx|Volumen 1,5 · Integral ≈ 0,054 m³ = 54 Liter",
    voraussetzungen="Schnittstellen mit einer waagerechten Geraden (Rechner)|Fläche zwischen Gerade und Graph|Volumen als Fläche mal Breite, Umrechnung m³ in Liter",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=W2_SK + "; Abb. 2: Ausschnitt der Mulde, x von −0,5 bis 0,5, Wasserlinie bei 0,1 markiert, Wasserfläche zwischen Graph und Linie grau", kontext="Wasserrutsche", textumfang="mittel",
    gegeben=W2 + "; Rutschbahn 1,5 m breit mit senkrechten Wänden; Wasser in der Mulde an der tiefsten Stelle 5 cm hoch (Abb. 2)",
    gesucht="Volumen des Wassers in der Mulde in Litern",
    verfahren="Wasserlinie y = 0,05 mit G schneiden, Fläche dazwischen integrieren, mit 1,5 multiplizieren und in Liter umrechnen",
    schritte="4", zahlenraum="dezimal", einheiten="Liter", abhaengig_von="",
    ergebnis="r(x) = 0,05 hat auf [−4; 10] die Lösungen x₁ ≈ −0,51 und x₂ ≈ 0,58; 1,5 · ∫_(x₁)^(x₂) (0,05 − r(x)) dx ≈ 0,054, also etwa 54 Liter (amtlich)",
    zwischenergebnis="Querschnitt ≈ 0,036 m²", niveau_geschaetzt="II",
    fehlerquelle="5 cm als 5 statt 0,05 in Meter einsetzen; Umrechnung m³ → Liter vergessen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,0545 m³). MMS-Anteil: Rechner für Schnittstellen und Integral, Ansatz eigen.")
row("2025MerhoehtBAnalysisMMS2", "d", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Einsehbarkeit eines Kurvenstücks von einem Punkt aus über die Tangente durch diesen Punkt untersuchen", typ_neben="",
    stichwoerter="Sichtlinie g_a durch (12 | 3) und (a | r(a)) mit Steigung (3 − r(a))/(12 − a)|g_a ist Tangente, wenn r'(a) = (3 − r(a))/(12 − a); Lösung a = 4|r''(4) = −1/16 < 0: (4 | r(4)) liegt auf dem rechtsgekrümmten Teil|Punkte mit a < 4 auf dem rechtsgekrümmten Teil sind nicht einsehbar",
    voraussetzungen="Sekantensteigung gleich Tangentensteigung als Berührbedingung|Krümmung über r''|Sichtbarkeit als Lage über/unter der Tangente",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=W2_SK, kontext="Wasserrutsche", textumfang="lang",
    gegeben=W2 + "; Kamera im Punkt (12 | 3); Sichtlinie zu (a | r(a)) mit −4 ≤ a ≤ 10 als Gerade g_a: y = (3 − r(a))/(12 − a) · x + (3 − (3 − r(a))/(12 − a) · 12)",
    gesucht="rechnerische Untersuchung, ob der rechtsgekrümmte Teil der Rutschbahn von der Kamera vollständig einsehbar ist",
    verfahren="Berührbedingung r'(a) = (3 − r(a))/(12 − a) mit dem Rechner lösen, Krümmung an der Lösung prüfen, verdeckten Bereich benennen",
    schritte="4", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="Für jede Lösung a von r'(a) = (3 − r(a))/(12 − a) ist g_a Tangente an G durch (12 | 3); die Lösung a = 4 liegt wegen r''(4) = −1/16 < 0 auf dem rechtsgekrümmten Teil; die Punkte mit a < 4 dieses Teils sind von der Kamera nicht einsehbar (amtlich)",
    zwischenergebnis="a = 4", niveau_geschaetzt="III",
    fehlerquelle="die Berührbedingung an der falschen Stelle ansetzen (r'(a) statt Sekantensteigung) oder den verdeckten Bereich auf a > 4 legen",
    bemerkung="Standardbezug: K1 III, K2 II, K3 III, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (a = 4, r''(4) = −0,0625). MMS-Anteil: Rechner für die Berührgleichung, Ansatz und Deutung eigen.")
# ---- AG/LA (A1) MMS: Würfel (1 a–b, 7 BE) und zweistufige Produktion (2 a–c, 13 BE)
Q1 = "Würfel mit einer Ecke O im Ursprung, Kanten parallel zu den Achsen, Kantenlänge 4; v = (4; −4; 4) ist der Verbindungsvektor der Ecken O und A"
Q1_SK = "Schrägbild: Würfel mit Ecke O im Ursprung, Achsen x, y, z, Ecke A oben links (Raumdiagonale von O), Vektor v als Pfeil von A nach O eingezeichnet, Kantenmarken 4"
row("2025MerhoehtBAGLAA1MMS", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Verbindungsvektor zweier Würfelecken mit gleicher Länge wie eine Raumdiagonale und nicht kollinear angeben", typ_neben="",
    stichwoerter="Raumdiagonalen haben die Länge 4√3|z. B. u = (4; 4; 4) (andere Raumdiagonale), nicht kollinear zu v",
    voraussetzungen="Betrag eines Vektors|Kollinearität|Ecken des Würfels aus dem Bild",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Körper", skizze=Q1_SK, kontext="ohne", textumfang="mittel",
    gegeben=Q1,
    gesucht="ein Vektor u: Verbindungsvektor zweier Würfelecken, gleich lang wie v, nicht kollinear zu v",
    verfahren="Eine andere Raumdiagonale wählen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="u = (4; 4; 4) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="−v angeben (kollinear)",
    bemerkung="Standardbezug: K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (|u| = |v| = 4√3). Aufgabengruppe A1, außerhalb der Geltung. MMS-Anteil: keiner.")
row("2025MerhoehtBAGLAA1MMS", "b", innen="1", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Kongruenz aller Dreiecke aus Raumdiagonale, Flächendiagonale und Kante begründen und Flächeninhalt berechnen", typ_neben="",
    stichwoerter="jedes Dreieck OAB hat als Seiten die Raumdiagonale OA, eine Flächendiagonale und eine Kante: kongruent|B(4 | −4 | 0): rechter Winkel bei B|Fläche 1/2 · |OB| · |AB| = 1/2 · 4√2 · 4 = 8√2",
    voraussetzungen="Kongruenz über drei gleiche Seiten|rechter Winkel Kante–Flächendiagonale|Dreiecksfläche",
    format="Begründung|Rechnung", operator="Begründen Sie|Ermitteln Sie", antwort="Text|Zahl",
    material="Körper", skizze=Q1_SK, kontext="ohne", textumfang="mittel",
    gegeben=Q1 + "; Dreiecke OAB mit B weiterer Würfelecke",
    gesucht="Begründung, dass alle diese Dreiecke kongruent sind; Flächeninhalt eines dieser Dreiecke",
    verfahren="Seitenarten der Dreiecke vergleichen, ein rechtwinkliges Dreieck OAB berechnen",
    schritte="3", zahlenraum="Wurzel", einheiten="", abhaengig_von="",
    ergebnis="Die Dreiecke sind kongruent, da ihre Seiten stets die Raumdiagonale OA, eine Flächendiagonale und eine Kante sind; für B(4 | −4 | 0) ist der Winkel bei B ein rechter, Flächeninhalt 1/2 · |OB| · |AB| = 8√2 (amtlich)",
    zwischenergebnis="Kantenlänge 4", niveau_geschaetzt="II",
    fehlerquelle="B so wählen, dass OAB nicht rechtwinklig ist, und mit einer falschen Höhe rechnen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung. MMS-Anteil: keiner.")
P2 = ("Zweistufige Produktion: aus Rohstoffen R₁–R₄ drei Zwischenprodukte Z₁–Z₃, daraus Endprodukte E₁–E₃; Tabellen: Zwischenprodukte je ME Endprodukt "
      "(Z₁: 3, 0, 0; Z₂: 1, 4, 0; Z₃: 0, 5, 2) und Rohstoffe je ME Endprodukt (R₁: 9, 12, 0; R₂: 3, 42, 12; R₃: 0, 20, 8; R₄: 0, 10, 4); Auftrag: je 10 ME der drei Endprodukte")
row("2025MerhoehtBAGLAA1MMS", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix berechnen", typ_neben="",
    stichwoerter="Zeile R₂ der Rohstofftabelle mal Auftragsvektor: (3 42 12) · (10; 10; 10) = 570",
    voraussetzungen="Zeile mal Spalte als Bedarf",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze="zwei Tabellen: Zeilen Z₁–Z₃ bzw. R₁–R₄, Spalten E₁–E₃ mit den Bedarfszahlen", kontext="Produktion / Verflechtung", textumfang="mittel",
    gegeben=P2,
    gesucht="benötigte ME des Rohstoffs R₂",
    verfahren="Zeile R₂ mit dem Auftragsvektor multiplizieren",
    schritte="1", zahlenraum="ganz", einheiten="ME", abhaengig_von="",
    ergebnis="(3 42 12) · (10; 10; 10) = 570, für den Auftrag werden 570 ME von R₂ benötigt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Zwischenprodukttabelle statt der Rohstofftabelle nehmen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ea-A). Aufgabengruppe A1, außerhalb der Geltung. MMS-Anteil: Rechner für das Produkt.")
row("2025MerhoehtBAGLAA1MMS", "b", innen="2", seite="2", punkte="6", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Kostengleichung mit Zeilenvektor, Matrix und Auftragsvektor erläutern und lösen", typ_neben="",
    stichwoerter="(3 0 0 / 1 4 0 / 0 5 2) · (10; 10; 10) = (30; 50; 70) Zwischenprodukte|Zeilenvektor (2z z 2z): Kosten je ME Z₁ und Z₃ doppelt so hoch wie z für Z₂|(2z z 2z) · (30; 50; 70) = 1250 ⇔ z = 5",
    voraussetzungen="Matrix mal Vektor als Zwischenproduktbedarf|Zeilenvektor mal Spaltenvektor als Gesamtkosten|lineare Gleichung",
    format="Begründung|Rechnung", operator="Erläutern Sie|Bestimmen Sie|Deuten Sie", antwort="Text|Zahl",
    material="Tabelle", skizze="zwei Tabellen: Zeilen Z₁–Z₃ bzw. R₁–R₄, Spalten E₁–E₃ mit den Bedarfszahlen", kontext="Produktion / Verflechtung", textumfang="mittel",
    gegeben=P2 + "; Fertigungskosten der Zwischenprodukte für den Auftrag 1250 GE; Gleichung (2z z 2z) · (3 0 0 / 1 4 0 / 0 5 2) · (10; 10; 10) = 1250",
    gesucht="Erläuterung der Gleichung im Sachzusammenhang; Lösung und ihre Deutung",
    verfahren="Matrixprodukt als Zwischenproduktmengen, Zeilenvektor als Stückkosten (Z₁, Z₃ doppelt so teuer wie Z₂) deuten, nach z lösen",
    schritte="3", zahlenraum="ganz", einheiten="GE", abhaengig_von="",
    ergebnis="(3 0 0 / 1 4 0 / 0 5 2) · (10; 10; 10) = (30; 50; 70) ist der Vektor der Zwischenproduktmengen; die Kosten je ME für Z₁ und Z₃ sind doppelt so hoch wie z für Z₂; die Gleichung liefert z = 5: die Fertigungskosten für eine ME von Z₂ betragen 5 GE (amtlich)",
    zwischenergebnis="(30; 50; 70)", niveau_geschaetzt="II",
    fehlerquelle="den Zeilenvektor als Mengen statt als Stückkosten deuten",
    bemerkung="Standardbezug: K1 I, K2 I, K3 II, K4 I, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung. MMS-Anteil: Rechner für Matrixprodukte, Deutung eigen.")
row("2025MerhoehtBAGLAA1MMS", "c", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Produktionsmenge aus einer Anteilsbedingung an den Rohstoffverbrauch bei festem Lagerverbrauch ermitteln", typ_neben="",
    stichwoerter="Auftrag (e₁; 10; 25): r₁ = 9e₁ + 120, r₂ = 3e₁ + 720|R₃ und R₄ vollständig verbraucht: 400 + 200 = 600|Anteil r₁/(r₁ + r₂ + 600) = 1/4 ⇔ (9e₁ + 120)/(12e₁ + 1440) = 1/4 ⇔ e₁ = 40",
    voraussetzungen="Rohstoffbedarf als Term in e₁|Anteil als Quotient|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="zwei Tabellen: Zeilen Z₁–Z₃ bzw. R₁–R₄, Spalten E₁–E₃ mit den Bedarfszahlen", kontext="Produktion / Verflechtung", textumfang="lang",
    gegeben=P2 + "; Lager 400 ME R₃ und 200 ME R₄ (werden vollständig verbraucht), R₁ und R₂ unbegrenzt; anderer Auftrag: 10 ME E₂, 25 ME E₃, e₁ ME E₁; Anteil von R₁ an allen Rohstoffen 25 %",
    gesucht="Anzahl der ME von E₁ dieses Auftrags",
    verfahren="r₁ und r₂ als Terme in e₁ aus der Rohstofftabelle, Anteilsgleichung mit 600 für R₃ und R₄ lösen",
    schritte="4", zahlenraum="ganz|Bruch|Prozent", einheiten="ME", abhaengig_von="",
    ergebnis="r₁ = 9e₁ + 120, r₂ = 3e₁ + 720; Anteil r₁/(r₁ + r₂ + 600) = 1/4 ⇔ (9e₁ + 120)/(12e₁ + 1440) = 1/4 ⇔ e₁ = 40 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="R₃ und R₄ aus der Tabelle mit e₁ berechnen statt den Lagerbestand 600 zu nehmen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung. MMS-Anteil: Rechner für die Gleichung, Ansatz eigen.")
# ---- AG/LA (A2) MMS: zusammengesetzter Körper Pyramide ABCDS + ABCDE_kF_k (a–e, 20 BE), Aufgabe ohne Nummer (innen 1)
K2 = ("Punkte A(2 | 0 | 0), B(−2 | 0 | 0), C(−2 | 0 | 3), D(2 | 0 | 3), S(0 | −5 | 0), E_k(0 | k | 0), F_k(0 | k | 30 − 3k) mit 0 < k ≤ 10; zusammengesetzter "
      "Körper aus der Pyramide ABCDS und dem Körper ABCDE_kF_k; ABCD ist ein Rechteck")
K2_SK = ("Schrägbild: Rechteck ABCD in der xz-Ebene (A und B auf der x-Achse, C und D darüber), Spitze S links auf der negativen y-Achse, rechts die Kante E_kF_k "
         "senkrecht über der y-Achse mit F_k oben; Gerade g durch F_k strichpunktiert")
row("2025MerhoehtBAGLAA2MMS", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Rechteck als Quadrat ausschließen und Volumen einer Pyramide über dem Rechteck berechnen", typ_neben="",
    stichwoerter="AB = (−4; 0; 0), BC = (0; 0; 3): nicht alle Seiten gleich lang, kein Quadrat|Pyramidenhöhe = Abstand von S zur xz-Ebene = 5|V = 1/3 · 4 · 3 · 5 = 20",
    voraussetzungen="Seitenlängen über Vektoren|Volumenformel der Pyramide|Höhe als y-Koordinate der Spitze",
    format="Rechnung", operator="Untersuchen Sie|Berechnen Sie", antwort="Text|Zahl",
    material="Körper", skizze=K2_SK, kontext="ohne", textumfang="mittel",
    gegeben=K2,
    gesucht="ob ABCD ein Quadrat ist; Volumen der Pyramide ABCDS",
    verfahren="Seitenvektoren vergleichen, V = 1/3 · Grundfläche · Höhe",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Wegen AB = (−4; 0; 0) und BC = (0; 0; 3) sind nicht alle Seiten gleich lang, ABCD ist kein Quadrat; V = 1/3 · 4 · 3 · 5 = 20 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Höhe als |AS| statt als Abstand von S zur Ebene ABCD nehmen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner.")
row("2025MerhoehtBAGLAA2MMS", "b", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Ortsvektor und Richtungsvektor der Geraden durch die Punkte einer Punktschar nachweisen", typ_neben="",
    stichwoerter="F₁(0 | 1 | 27) als Punkt auf g|F₂ − F₁ = (0; 1; −3) ist Richtungsvektor|allgemein F_k = (0; 0; 30) + k · (0; 1; −3)",
    voraussetzungen="Punktschar als Gerade|Differenz zweier Scharpunkte als Richtungsvektor",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Zeigen Sie", antwort="Term",
    material="Körper", skizze=K2_SK, kontext="ohne", textumfang="kurz",
    gegeben=K2 + "; jeder Punkt F_k liegt auf der Geraden g",
    gesucht="Ortsvektor eines Punkts auf g; Nachweis, dass (0; 1; −3) ein Richtungsvektor von g ist",
    verfahren="Einen Scharpunkt einsetzen, Differenz zweier Scharpunkte bilden",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Ortsvektor von F₁: (0; 1; 27); F₁F₂ = (0; 1; −3) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="E_k statt F_k als Punkt von g nehmen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung I (Scharpunkte einsetzen); der amtliche Bereich ist II. MMS-Anteil: keiner.")
row("2025MerhoehtBAGLAA2MMS", "c", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebene eines zusammengesetzten Körpers über verschiedene Höhen der Teilkörper ausschließen", typ_neben="",
    stichwoerter="ABCDS ist Pyramide mit Höhe 5 (Spitze bei y = −5)|ABCDE_kF_k ist nur für k = 10 eine Pyramide (E₁₀ = F₁₀), Höhe dann 10|Höhen 5 und 10 verschieden: keine Symmetrie zur xz-Ebene, für kein k",
    voraussetzungen="Spiegelung an der xz-Ebene als Vorzeichenwechsel von y|Form der Teilkörper in Abhängigkeit von k",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=K2_SK, kontext="ohne", textumfang="kurz",
    gegeben=K2,
    gesucht="Begründung, dass die xz-Ebene für keinen Wert von k Symmetrieebene des zusammengesetzten Körpers ist",
    verfahren="Beide Teilkörper an der xz-Ebene vergleichen: Pyramide der Höhe 5 gegen Körper, der höchstens (k = 10) eine Pyramide der Höhe 10 ist",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="ABCDS ist eine Pyramide mit Höhe 5; ABCDE_kF_k ist nur für k = 10 eine Pyramide, und diese hat die Höhe 10; der Körper ist daher nicht symmetrisch zur xz-Ebene (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur k = 5 prüfen und die Kante E₅F₅ (Länge 15) übersehen",
    bemerkung="Standardbezug: K1 II, K4 I, K6 II. AB amtlich: II. Amtlich. MMS-Anteil: keiner.")
row("2025MerhoehtBAGLAA2MMS", "d", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Koordinatengleichung einer Ebene aufstellen und Parameter eines Scharpunkts in der Ebene bestimmen", typ_neben="",
    stichwoerter="CD = (4; 0; 0), CS = (2; −5; −3)|Normalenvektor (0; 3; −5) aus CD · n = 0 und CS · n = 0|L: 3y − 5z = d, S einsetzen: d = −15|F_k: 3k − 5 · (30 − 3k) = −15 ⇔ k = 7,5",
    voraussetzungen="Normalenvektor über Orthogonalität zu zwei Spannvektoren|Koordinatengleichung|Punktprobe mit Parameter",
    format="Rechnung", operator="Bestimmen Sie|Ermitteln Sie", antwort="Term|Zahl",
    material="Körper", skizze=K2_SK, kontext="ohne", textumfang="kurz",
    gegeben=K2 + "; Ebene L durch C, D und S",
    gesucht="Koordinatengleichung von L; Wert von k, für den F_k in L liegt",
    verfahren="Normalenvektor aus CD ⊥ n, CS ⊥ n, d über S; F_k einsetzen",
    schritte="4", zahlenraum="ganz|negativ|dezimal", einheiten="", abhaengig_von="",
    ergebnis="CD · n = 0 und CS · n = 0 liefern n = (0; 3; −5); L: 3y − 5z = d mit d = −15 aus S ∈ L; Einsetzen von F_k ergibt k = 7,5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Normalenvektor (0; 3; −5) falsch orientiert und d aus C statt S (gleich, da beide in L)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (n = (0; 12; −20) ~ (0; 3; −5), d = −15, k = 15/2). MMS-Anteil: Rechner für das Gleichungssystem möglich, Ansatz eigen.")
row("2025MerhoehtBAGLAA2MMS", "e", innen="1", seite="2", punkte="6", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Parameter für den maximalen Spitzenwinkel eines gleichschenkligen Dreiecks über die minimale Höhe und die Orthogonalität zur Geraden ermitteln", typ_neben="",
    stichwoerter="DF_kC gleichschenklig mit Basis CD (F_k in der Symmetrieebene x = 0), M(0 | 0 | 3) Mittelpunkt von CD|Winkel bei F_k umso größer, je kleiner die Höhe |MF_k||Höhe minimal, wenn MF_k ⊥ g: (0; k; 27 − 3k) · (0; 1; −3) = 0 ⇔ k = 8,1",
    voraussetzungen="Gleichschenkligkeit über Symmetrie|Spitzenwinkel und Höhe|kürzester Abstand als Lot auf die Gerade",
    format="Rechnung|Begründung", operator="Ermitteln Sie|Erläutern Sie", antwort="Zahl|Text",
    material="Körper", skizze=K2_SK, kontext="ohne", textumfang="mittel",
    gegeben=K2 + "; Innenwinkel des Dreiecks DF_kC bei F_k",
    gesucht="Wert von k, für den dieser Winkel maximal ist, mit Erläuterung des Lösungswegs",
    verfahren="Winkelmaximum in die minimale Höhe MF_k übersetzen, Lotbedingung MF_k · (0; 1; −3) = 0 lösen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="2025MerhoehtBAGLAA2MMS-1b",
    ergebnis="DF_kC ist gleichschenklig mit Basis CD; der Winkel an der Spitze ist umso größer, je kleiner die Höhe |MF_k| mit M = Mittelpunkt von CD ist; sie ist minimal, wenn MF_k senkrecht zum Richtungsvektor von g steht: (0; k; 27 − 3k) · (0; 1; −3) = 0 ⇔ k = 8,1 (amtlich)",
    zwischenergebnis="M(0 | 0 | 3)", niveau_geschaetzt="III",
    fehlerquelle="den Winkel als Funktion von k mit dem Rechner maximieren, ohne den Weg zu erläutern",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (k = 81/10). Verwandt mit „Scharparameter für den minimalen Flächeninhalt eines Schnittdreiecks über die Orthogonalität zur Kante ermitteln“ (2025-ea-B WTR e) und der Gleichung für das flächenkleinste Dreieck (2020-ga-B AG/LA A2 2) – Kandidaten für eine Zusammenziehung. MMS-Anteil: Rechner möglich, Ansatz eigen.")

NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Fläche: Aussage über den Flächeninhalt zwischen zwei Scharkurven als Parameterungleichung untersuchen", "Analysis", "Flächeninhalt durch Integration",
     "Die Schnittstellen zweier Scharkurven bestimmen, den eingeschlossenen Flächeninhalt als Term im Parameter berechnen und eine vorgegebene Ungleichung für einen Parameterbereich prüfen.", "2025MerhoehtBAnalysisMMS1-1d"),
    ("Größte und kleinste Rate im Zeitraum über Ableitung und Randwerte berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Auf einem abgeschlossenen Zeitintervall die größte und die kleinste momentane Änderungsrate über die Nullstellen der Ableitung der Ratenfunktion und die Randwerte bestimmen.", "2025MerhoehtBAnalysisMMS1-2a"),
    ("Ableitungswert an der Wendestelle als stärksten Anstieg der Rate im Sachzusammenhang deuten", "Analysis", "Kurvenuntersuchung",
     "Aus den Werten der Ableitung einer Ratenfunktion an Rändern und Wendestellen erkennen, dass die Rate an einer Wendestelle am stärksten zunimmt, und den Wert mit Einheit im Sachzusammenhang beschreiben.", "2025MerhoehtBAnalysisMMS1-2b"),
    ("Grenzverhalten einer Schar angeben und parameterunabhängigen Funktionswert nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Das Verhalten einer Funktionenschar für x → ±∞ angeben und zeigen, dass der Funktionswert an einer festen Stelle für alle Parameterwerte gleich ist.", "2025MerhoehtBAnalysisMMS2-1a"),
    ("Lage und Art der Extrempunkte einer Schar bestimmen und Parameter für einen vorgegebenen Abstand der Extrempunkte berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Extrempunkte einer Funktionenschar mit Art über erste und zweite Ableitung bestimmen und den Parameterwert numerisch berechnen, für den die Extrempunkte einen vorgegebenen Abstand haben.", "2025MerhoehtBAnalysisMMS2-1b"),
    ("Höchstens eine positive Nullstelle jeder Stammfunktion über die Monotonie aus dem Vorzeichen des Integranden begründen", "Analysis", "Stammfunktion und Hauptsatz",
     "Ohne Stammfunktionsterme begründen, dass jede Stammfunktion auf der positiven Halbachse streng monoton ist, weil der Integrand dort positiv ist, und daher höchstens eine positive Nullstelle hat.", "2025MerhoehtBAnalysisMMS2-1c"),
    ("Nullstellen und Werte: Höhen an den Rändern einer Profillinie als Funktionswerte berechnen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Höhen an den Enden eines durch einen Funktionsgraphen modellierten Profils als Funktionswerte an den Intervallrändern berechnen.", "2025MerhoehtBAnalysisMMS2-2a"),
    ("Steigungswinkel und Nebenwinkel am Übergang zweier Profilstücke einzeichnen und im Sachzusammenhang deuten", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Steigungswinkel eines Graphen in einem Übergangspunkt und seinen Nebenwinkel zu einem waagerechten Anschlussstück in die Abbildung einzeichnen und die Bedeutung des Nebenwinkels im Sachzusammenhang angeben.", "2025MerhoehtBAnalysisMMS2-2b"),
    ("Fläche: Wasservolumen in einer Mulde aus Fläche zwischen Wasserlinie und Graph mal Breite berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Die Schnittstellen einer waagerechten Wasserlinie mit dem Profilgraphen bestimmen, die Fläche dazwischen integrieren und mit der Breite zum Volumen in Litern umrechnen.", "2025MerhoehtBAnalysisMMS2-2c"),
    ("Einsehbarkeit eines Kurvenstücks von einem Punkt aus über die Tangente durch diesen Punkt untersuchen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Über die Berührbedingung Sekantensteigung gleich Ableitung die Tangente von einem festen Punkt an den Graphen bestimmen, die Krümmung an der Berührstelle prüfen und den vom Punkt aus nicht einsehbaren Teil des Graphen benennen.", "2025MerhoehtBAnalysisMMS2-2d"),
    ("Verbindungsvektor zweier Würfelecken mit gleicher Länge wie eine Raumdiagonale und nicht kollinear angeben", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Zu einer vorgegebenen Raumdiagonale eines Würfels einen anderen Verbindungsvektor zweier Ecken gleicher Länge angeben, der nicht kollinear zur vorgegebenen ist.", "2025MerhoehtBAGLAA1MMS-1a"),
    ("Ebene Figur: Kongruenz aller Dreiecke aus Raumdiagonale, Flächendiagonale und Kante begründen und Flächeninhalt berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Begründen, dass alle Dreiecke aus einer Raumdiagonale eines Würfels und einer weiteren Ecke kongruent sind, und den Flächeninhalt an einem rechtwinkligen Vertreter berechnen.", "2025MerhoehtBAGLAA1MMS-1b"),
    ("Verflechtung: Kostengleichung mit Zeilenvektor, Matrix und Auftragsvektor erläutern und lösen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine Gleichung aus Zeilenvektor der Stückkosten, Bedarfsmatrix und Auftragsvektor im Sachzusammenhang erläutern, die unbekannten Stückkosten berechnen und deuten.", "2025MerhoehtBAGLAA1MMS-2b"),
    ("Verflechtung: Produktionsmenge aus einer Anteilsbedingung an den Rohstoffverbrauch bei festem Lagerverbrauch ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Den Rohstoffbedarf als Terme in einer unbekannten Produktionsmenge aufstellen und diese aus einer Anteilsbedingung bestimmen, wobei feste Lagerbestände anderer Rohstoffe vollständig verbraucht werden.", "2025MerhoehtBAGLAA1MMS-2c"),
    ("Körper: Rechteck als Quadrat ausschließen und Volumen einer Pyramide über dem Rechteck berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Über verschieden lange Seitenvektoren zeigen, dass ein Rechteck kein Quadrat ist, und das Volumen der Pyramide über dem Rechteck mit der Höhe als Abstand der Spitze zur Grundebene berechnen.", "2025MerhoehtBAGLAA2MMS-1a"),
    ("Ortsvektor und Richtungsvektor der Geraden durch die Punkte einer Punktschar nachweisen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Für eine parameterabhängige Punktschar auf einer Geraden den Ortsvektor eines Scharpunkts angeben und den Richtungsvektor als Differenz zweier Scharpunkte nachweisen.", "2025MerhoehtBAGLAA2MMS-1b"),
    ("Symmetrieebene eines zusammengesetzten Körpers über verschiedene Höhen der Teilkörper ausschließen", "Analytische Geometrie", "Spiegelung",
     "Begründen, dass eine Koordinatenebene für keinen Parameterwert Symmetrieebene eines aus zwei Teilkörpern zusammengesetzten Körpers ist, weil die Teilkörper verschiedene Höhen oder Formen haben.", "2025MerhoehtBAGLAA2MMS-1c"),
    ("Koordinatengleichung einer Ebene aufstellen und Parameter eines Scharpunkts in der Ebene bestimmen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Die Koordinatengleichung einer Ebene aus drei Punkten aufstellen und den Parameterwert bestimmen, für den ein Punkt einer Punktschar in der Ebene liegt.", "2025MerhoehtBAGLAA2MMS-1d"),
    ("Dreieck: Parameter für den maximalen Spitzenwinkel eines gleichschenkligen Dreiecks über die minimale Höhe und die Orthogonalität zur Geraden ermitteln", "Analytische Geometrie", "Orthogonalität",
     "Den Parameterwert bestimmen, für den der Spitzenwinkel eines gleichschenkligen Dreiecks mit Spitze auf einer Geraden maximal ist, indem die Höhe minimiert und als Lot auf die Gerade über das Skalarprodukt angesetzt wird.", "2025MerhoehtBAGLAA2MMS-1e"),
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
