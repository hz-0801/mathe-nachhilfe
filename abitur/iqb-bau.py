# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 1.9 · 17.09.2026 · gilt mit katalog-prompt.md v0.9, abitur-vokabular.md v1.6, iqb.md v1.13, abitur-abgleich.py v0.24, iqb-quellen.csv mit Spalte dateidublette_von und den Geltungsdateien abi-<zielprüfung>-geltung.md v1.0

Änderungen gegenüber 1.8 (Auftrag G, Punkt 2, 17.09.2026): Versionsbindung (abitur-abgleich.py v0.24); sonst unverändert.

Änderungen gegenüber 1.7 (Auftrag F, Punkt 2, 17.09.2026): Das Abgleichskript heißt abitur-abgleich.py (bis 17.09.2026 abgleich.py); nur Text in Kopf, Kommentaren und Meldungen, keine Prüfung geändert – Selbstprüfung byteidentisch zu 1.7.

Änderungen gegenüber 1.6 (Auftrag E, Punkt 4): Die Spalte dublette_von von iqb-quellen.csv heißt dateidublette_von (Dateidublette, iqb.md § 7); nur der Name, keine Logik.

Änderungen gegenüber 1.5 (Auftrag D „Namensschema, Erweiterbarkeit,
Begründungen", Teil 2, 17.09.2026): Die Geltung kommt nicht mehr aus einer
Tabelle in abitur-vokabular.md § 3, sondern je Zielprüfung aus einer eigenen
Datei abi-<zielprüfung>-geltung.md (§ 1, Tabelle „Thema | gilt", ja/nein).
Welche Zielprüfungen gelten, sagt das Profil (iqb.md § 6, Zeile
„Zielprüfungen: be-gk · be-lk · bb-gk · bb-ea" – die Zielprüfungen des
Profils abi, Poolzeilen werden gegen alle gezählt); Datenstruktur (ZIELE,
GELTUNG), Kennzahlen und Abbruchkriterium unverändert – Selbstprüfung und
Berichte byteidentisch zu v1.5. Inhalt der Dateien unverändert aus der
Tabelle erzeugt (namensschema.md § 2).

Änderungen gegenüber 1.4 (Auftrag „Eichung korrigieren, Prüfungsgeschichte und
Prüfungsstruktur festhalten, Heftordner ordnen", 17.09.2026, Entscheidung des
Lehrers): Die Überschreibung der Eichschwelle je Stapel (KONFIG
„eichung_mindestens"/„eichung_grund", v1.4) ist zurückgebaut, die globale
Schwelle in SCHWELLEN gilt für jeden Stapel. Vorrang des Amtlichen (Kern § 5):
eine Zeile, deren Schätzung aus einer Landeszeile übernommen ist (bemerkung
„… aus der Landeszeile übernommen"), muss den amtlichen Bereich treffen – weicht
sie ab, wird die Schätzung korrigiert, nicht die Schwelle; das Skript bricht
sonst ab (Stapellauf und Selbstprüfung). Die neun betroffenen Zeilen von
2022-ga-B hat abitur-abgleich.py Lauf 20 gesetzt.

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
Erfassung stellt abitur-abgleich.py sie auf „Dublette von:" (wortgleich) oder
„Abgewandelt von: <id>; <Unterschied>." (abgewandelte Fassung) um. Beide
Verweise zählen als Landesverwendung; der Bestand des Stapels wird beim Lauf
gegen die Vormerkungen gemeldet.

Änderungen gegenüber 1.1 (Auftrag „abi-Bestand gegen den Pool abgleichen"):
Kennzahl Landesverwendung – Zeilen des Stapels, auf die abi-Zeilen mit
„Dublette von:" verweisen (Kennzahlenzeile, Selbstprüfung je Stapel); Zeilen,
die abi als „Poolaufgabe (nicht erfasst)" vorgemerkt hat, werden beim
Stapellauf gemeldet (Vermerk danach per abitur-abgleich.py umstellen) und in der
Selbstprüfung gegen den Bestand geprüft.

Änderungen gegenüber 1.0 (Entscheidung des Lehrers, 16.09.2026: Themenfeld
bereinigen): leitidee und thema einer Zeile müssen gleich leitidee und thema
ihres Typs in abitur-typen.csv sein (geprüft für ZEILEN und in der
Selbstprüfung für den Bestand); der Schnitt Thema × Klasse × Handlung wird
über das Thema des Typs gemessen (Lauf 13 von abitur-abgleich.py hat den Bestand
darauf gebracht).

Änderungen gegenüber 0.9 (Entscheidung 25, 15.09.2026: gemeinsame Typenliste
für abi und iqb): Sachgebiete, Themen, Geltungstabelle, Gegenstandsklassen und
Handlungen kommen aus abitur-vokabular.md statt aus iqb.md; die Typenliste heißt
abitur-typen.csv und wird mit dem Profil abi geteilt – beispiel_id darf in
abi-katalog.csv zeigen, und ein Typ gilt als verwendet, wenn er in einem der
beiden Kataloge steht (ANDERE_KATALOGE). Umbenennungen laufen über abitur-abgleich.py.

Änderungen gegenüber 0.8 (Entscheidung des Lehrers, 15.09.2026: MMS/CAS als
Delta): Die Erfassungseinheit „Stapel je Rechnerfassung" bleibt für WTR; für
einen mms-/cas-Stapel gilt: vollständig sind die nicht wortgleichen Dateien,
das Soll rechnet nur gegen sie. Wortgleiche Dateien stehen in iqb-quellen.csv
(v0.3, Textvergleich des Abschnitts „1 Aufgabe") mit dateidublette_von auf die
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
Spalte dateidublette_von bekommen keine Zeile und fehlen nicht; Seitenzahl je Datei
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
    "stapel": "2017-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dateidublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2017MgrundlegendAAnalysis11": 5, "2017MgrundlegendAAnalysis12": 5, "2017MgrundlegendAAnalysis2": 5,
        "2017MgrundlegendAAGLAA11": 5,
        "2017MgrundlegendAAGLAA211": 5, "2017MgrundlegendAAGLAA212": 5, "2017MgrundlegendAAGLAA22": 5,
        "2017MgrundlegendAStochastik11": 5, "2017MgrundlegendAStochastik12": 5, "2017MgrundlegendAStochastik2": 5,
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
KERN = "../katalog-prompt.md"  # Umbau 2026-09-19: liegt in der Repo-Wurzel
PROFIL = "iqb.md"                       # nennt die Zielprüfungen (§ 6)
GELTUNG_DATEI = "abi-{ziel}-geltung.md"  # eine Datei je Zielprüfung (namensschema.md § 2)
# Kataloge der anderen Profile mit derselben Typenliste (Entscheidung 25): ihre
# ids gelten für beispiel_id, ihre Typfelder zählen als Verwendung.
ANDERE_KATALOGE = ["abi-katalog.csv"]
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]
QUELLEN_HEAD = ["kennung", "jahr", "niveau", "teil", "sachgebiet", "gruppe",
                "hilfsmittel", "nr", "papier", "stapel", "seiten", "dateidublette_von"]

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


def zielpruefungen():
    """Zielprüfungen des Profils: Zeile „Zielprüfungen: a · b · c …" in PROFIL (§ 6)."""
    m = re.search(r"^Zielprüfungen:\s*([^(\n]+)", lies(PROFIL), re.M)
    if not m:
        sys.exit(f"{PROFIL}: Zeile „Zielprüfungen:“ nicht gefunden.")
    ziele = [z.strip() for z in m.group(1).split("·") if z.strip()]
    if not ziele:
        sys.exit(f"{PROFIL}: keine Zielprüfung genannt.")
    return ziele


def geltung():
    """Geltung je Zielprüfung aus den Dateien GELTUNG_DATEI (§ 1, Tabelle „Thema | gilt", ja/nein),
    Zielprüfungen aus dem Profil; bis v1.5 stand die Tabelle in abitur-vokabular.md § 3.
    Liefert (Zielprüfungen, {thema: Menge der Zielprüfungen mit ja}) wie bisher."""
    ziele = zielpruefungen()
    alle = {t for liste in THEMEN.values() for t in liste}
    tab = {t: set() for t in alle}
    for ziel in ziele:
        pfad = GELTUNG_DATEI.format(ziel=ziel)
        teil = abschnitt(lies(pfad), "Themen", pfad)
        m = re.search(r"^\| Thema \| gilt \|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)", teil, re.M)
        if not m:
            sys.exit(f"{pfad}: Tabelle „Thema | gilt“ nicht gefunden.")
        gesehen = set()
        for zeile in m.group(1).strip().splitlines():
            zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
            if len(zellen) != 2:
                sys.exit(f"{pfad}: Geltungszeile hat {len(zellen)} Zellen: {zeile}")
            thema, wert = zellen
            if wert not in ("ja", "nein"):
                sys.exit(f"{pfad}: Geltung muss ja oder nein sein: {zeile}")
            if thema in gesehen:
                sys.exit(f"{pfad}: Thema doppelt: {thema}")
            if thema not in alle:
                sys.exit(f"{pfad}: Geltungszeile ohne Thema in der Liste: {thema}")
            gesehen.add(thema)
            if wert == "ja":
                tab[thema].add(ziel)
        fehlt = sorted(alle - gesehen)
        if fehlt:
            sys.exit(f"{pfad}: Themen ohne Geltungszeile: {fehlt}")
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
# Stapel 2017-ga-A (Reserve, geöffnet im Auftrag Nacht 2026-09-27 wegen des Landeshefts
# 2017-be-gk – Regel „Eine Vormerkung überlebt keinen Auftrag“, iqb.md § 7; das Heft hat
# keinen hilfsmittelfreien Teil, der Poolabgleich findet keine Teilaufgabe dieses Stapels).
# Zehn Dateien zu je 5 BE, jede mit a und b; Standardbezug ohne Spalte Anforderungsbereich
# (Teil A, Eichung gegen den höchsten Kompetenzeintrag). Keine Dateidublette im Stapel.
# ---- Analysis 1.1: f(x) = 2e^(−x/2) mit Abbildung
A11 = "f(x) = 2 · e^(−1/2 · x), in IR definiert; f'(x) = −e^(−1/2 · x) (vorgegeben)"
A11_SK = ("Koordinatensystem auf Kästchengitter (eine Einheit = zwei Kästchen), x von −1 bis 4, y von 0 bis 4: Graph von f "
          "streng fallend von etwa (−1 | 3,3) über (0 | 2), (1 | 1,2), (2 | 0,7) bis (4 | 0,3), nähert sich der x-Achse")
row("2017MgrundlegendAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen", typ_neben="",
    stichwoerter="Schnittpunkt mit der y-Achse (0 | 2)|f'(0) = −1|y = −x + 2",
    voraussetzungen="Funktionswert an der Stelle 0|Punkt-Steigungs-Form der Geraden",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Koordinatensystem", skizze=A11_SK, kontext="ohne", textumfang="kurz",
    gegeben=A11,
    gesucht="Gleichung der Tangente an den Graphen von f in seinem Schnittpunkt mit der y-Achse",
    verfahren="f(0) = 2 und f'(0) = −1 berechnen und in y = m · x + n einsetzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(0) = 2, f'(0) = −1; damit y = −x + 2 (amtlich)",
    zwischenergebnis="f(0) = 2|f'(0) = −1", niveau_geschaetzt="I",
    fehlerquelle="die Steigung f(0) = 2 statt f'(0) = −1 verwenden",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-A).")
row("2017MgrundlegendAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Flächenstück mit vorgegebenem Inhalt am Graphen einzeichnen und Integralterm angeben", typ_neben="",
    stichwoerter="Fläche unter dem Graphen zwischen y-Achse und x = 1|Kästchen zählen, etwa 1,5|Term ∫ von 0 bis 1 f(x) dx",
    voraussetzungen="Flächeninhalt am Kästchengitter abschätzen|Integral als Flächeninhalt über der x-Achse",
    format="Zeichnen|Kurzantwort", operator="Zeichnen Sie ein|Geben Sie an", antwort="Grafik|Term",
    material="Koordinatensystem", skizze=A11_SK, kontext="ohne", textumfang="mittel",
    gegeben=A11 + "; Abbildung des Graphen",
    gesucht="ein Flächenstück, begrenzt vom Graphen, der x-Achse, der y-Achse und einer Parallelen zur y-Achse, mit Inhalt etwa 1,5, eingezeichnet; Term für seinen Inhalt",
    verfahren="Am Gitter die Fläche unter dem Graphen ab x = 0 abschätzen, bis etwa 1,5 erreicht ist (Grenze x = 1), schraffieren und als bestimmtes Integral angeben",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Flächenstück zwischen Graph, x-Achse, y-Achse und der Geraden x = 1 schraffiert; Term ∫ von 0 bis 1 f(x) dx (amtlich)",
    zwischenergebnis="∫ von 0 bis 1 f(x) dx = 4 − 4e^(−1/2) ≈ 1,57", niveau_geschaetzt="II",
    fehlerquelle="die Parallele zu weit rechts ziehen, weil die Fläche nahe der y-Achse unterschätzt wird, oder die Grenzen im Term vertauschen",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I. Amtlich (Erwartungshorizont zeigt die Schraffur bis x = 1), eigene Rechnung bestätigt: ∫ von 0 bis 1 f(x) dx = 4 − 4e^(−1/2) ≈ 1,57. Neuer Typ: kein vorhandenes Etikett verlangt, ein Flächenstück zu einem vorgegebenen Inhalt erst zu finden und einzuzeichnen.")
# ---- Analysis 1.2: f(x) = x³ + 2x²
A12 = "f: x ↦ x^3 + 2x^2, in IR definiert"
row("2017MgrundlegendAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstellen einer ganzrationalen Funktion durch Ausklammern und Faktorisieren berechnen", typ_neben="",
    stichwoerter="x^2 ausklammern|x^2 · (x + 2) = 0|x1 = −2, x2 = 0 als einzige Nullstellen",
    voraussetzungen="Ausklammern|Satz vom Nullprodukt",
    format="Begründung", operator="Bestätigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=A12,
    gesucht="Bestätigung, dass x1 = −2 und x2 = 0 die einzigen Nullstellen von f sind",
    verfahren="f(x) = 0 setzen, x^2 ausklammern und den Satz vom Nullprodukt anwenden",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(x) = 0 ⇔ x^2 · (x + 2) = 0 ⇔ x = −2 oder x = 0 (amtlich)",
    zwischenergebnis="f(x) = x^2 · (x + 2)", niveau_geschaetzt="I",
    fehlerquelle="nur durch Einsetzen bestätigen, dass −2 und 0 Nullstellen sind, ohne auszuschließen, dass es weitere gibt",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2022-bebb-gk); hier ist die Lösungsmenge vorgegeben und ihre Vollständigkeit zu bestätigen.")
row("2017MgrundlegendAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph und x-Achse zwischen zwei Nullstellen berechnen", typ_neben="",
    stichwoerter="Grenzen −2 und 0 aus den Nullstellen|Stammfunktion 1/4 x^4 + 2/3 x^3|Inhalt 4/3",
    voraussetzungen="Stammfunktion ganzrationaler Funktionen|Hauptsatz|Vorzeichen des Integranden zwischen den Nullstellen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=A12 + "; Nullstellen −2 und 0 (aus a)",
    gesucht="Inhalt der Fläche, die der Graph von f mit der x-Achse einschließt",
    verfahren="Integral von −2 bis 0 über f mit der Stammfunktion 1/4 x^4 + 2/3 x^3 berechnen; der Integrand ist dazwischen nicht negativ",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2017MgrundlegendAAnalysis12-a",
    ergebnis="∫ von −2 bis 0 (x^3 + 2x^2) dx = [1/4 x^4 + 2/3 x^3] von −2 bis 0 = 4/3 (amtlich)",
    zwischenergebnis="F(−2) = 4 − 16/3 = −4/3", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichenfehler bei F(−2) oder über ein falsches Intervall (etwa bis zu einer vermuteten dritten Nullstelle) integrieren",
    bemerkung="Standardbezug: K5 II, K6 I. Amtlich, eigene Rechnung bestätigt. Neuer Typ: die vorhandenen Etiketten verlangen zwei Flächenstücke, die y-Achse als Rand oder eine vorgegebene Stammfunktion.")
# ---- Analysis 2: Graphen I (1 − cos x) und II (sin x); f(x) = k sin(x)
A2_SK = ("Koordinatensystem, x von etwa −π/2 bis 2π + π/4 mit Marken bei π/2, π, 3π/2, 2π, y von −1 bis 2: Graph I gestrichelt "
         "(0 bei x = 0 und 2π, Maximum 2 bei π, Wert 1 bei π/2 und 3π/2), Graph II durchgezogen (Nullstellen 0, π, 2π, Maximum 1 bei π/2, "
         "Minimum −1 bei 3π/2); beide Graphen sind ohne Term angegeben")
row("2017MgrundlegendAAnalysis2", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Graphen von Funktion und Ableitung einander zuordnen", typ_neben="",
    stichwoerter="Graph II Ableitung|Graph I für π/2 <= x <= 3π/2 über der x-Achse|Graph II dort nicht streng monoton steigend",
    voraussetzungen="Vorzeichen der Ableitung und Monotonie|Graphen vergleichen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=A2_SK, kontext="ohne", textumfang="mittel",
    gegeben="Abbildung mit den Graphen I und II einer Funktion und ihrer ersten Ableitungsfunktion (ohne Zuordnung)",
    gesucht="welcher der Graphen die Ableitungsfunktion darstellt, mit Begründung",
    verfahren="Annahme prüfen: wäre I die Ableitung, müsste II dort steigen, wo I positiv ist (π/2 <= x <= 3π/2); II fällt dort, also ist II die Ableitung",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Graph II ist die Ableitung: Graph I liegt für π/2 <= x <= 3π/2 oberhalb der x-Achse; wäre I die Ableitung, müsste II dort streng monoton steigen, was nicht der Fall ist (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Graphen mit der kleineren Amplitude oder den durchgezogenen ohne Begründung für die Ableitung halten",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. Amtlich, eigene Rechnung bestätigt (Graph I ist 1 − cos x, Graph II sin x). Typ wiederverwendet (2026-ga-A).")
row("2017MgrundlegendAAnalysis2", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für einen vorgegebenen Flächeninhalt zwischen Graph und x-Achse bestimmen", typ_neben="",
    stichwoerter="f(x) = k · sin(x), k > 0|∫ von 0 bis π k · sin(x) dx = 2k|2k = 1/2, k = 1/4",
    voraussetzungen="Stammfunktion der Sinusfunktion|Integral mit Parameter|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = k · sin(x), in IR definiert, für einen Wert k > 0; für 0 <= x <= π schließt der Graph mit der x-Achse ein Flächenstück mit Inhalt 1/2 ein",
    gesucht="Wert von k",
    verfahren="Das Integral von 0 bis π über k · sin(x) mit der Stammfunktion −k · cos(x) berechnen und gleich 1/2 setzen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="∫ von 0 bis π k · sin(x) dx = [−k · cos(x)] von 0 bis π = 2k, 2k = 1/2 ⇔ k = 1/4 (amtlich)",
    zwischenergebnis="∫ von 0 bis π k · sin(x) dx = 2k", niveau_geschaetzt="II",
    fehlerquelle="cos(π) = 1 setzen und das Integral null erhalten, oder −cos als Ableitung statt als Stammfunktion nehmen",
    bemerkung="Standardbezug: K2 III, K5 III, K6 II. Amtlich, eigene Rechnung bestätigt. Schätzung II (Routineverkettung Stammfunktion und lineare Gleichung, kein Eintrag der Deutungsliste); der amtliche Bereich ist III. Typ wiederverwendet (2024-ga-B): k ist ein Parameter der Funktion wie bei einer Schar.")
# ---- AG/LA (A1) 1: Matrizen A (3×2) und B (2×2)
M1 = "Matrizen A = ((2; 2), (3; 0), (0; 1)) mit drei Zeilen und zwei Spalten und B = ((3; 0), (1; 2)) (zeilenweise)"
row("2017MgrundlegendAAGLAA11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Definiertheit von Summe und Produkt zweier Matrizen über die Formate entscheiden", typ_neben="",
    stichwoerter="A + B nicht definiert, verschiedene Zeilenzahlen|A · B definiert, Spaltenzahl von A gleich Zeilenzahl von B|Formate 3×2 und 2×2",
    voraussetzungen="Format einer Matrix|Summe nur bei gleichem Format|Produkt: Spaltenzahl des linken gleich Zeilenzahl des rechten Faktors",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=M1,
    gesucht="Entscheidung mit Begründung, ob A + B und A · B definiert sind",
    verfahren="Formate vergleichen: für die Summe gleiche Formate, für das Produkt Spaltenzahl von A gleich Zeilenzahl von B",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="A + B nicht definiert (unterschiedliche Anzahl der Zeilen); A · B definiert (Anzahl der Spalten von A stimmt mit der Anzahl der Zeilen von B überein) (amtlich)",
    zwischenergebnis="A · B = ((8; 4), (9; 0), (1; 2))", niveau_geschaetzt="I",
    fehlerquelle="das Produkt wegen verschiedener Formate für nicht definiert halten",
    bemerkung="Standardbezug: K1 II, K5 I. Amtlich, eigene Rechnung bestätigt. Schätzung I (je Term eine einzelne begründete Beobachtung); der amtliche Bereich ist II (K1 II).")
row("2017MgrundlegendAAGLAA11", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Inverse Matrix über A · B = E bestimmen", typ_neben="",
    stichwoerter="B · C = E mit C = ((a; b), (c; d))|3a = 1, 3b = 0, a + 2c = 0, b + 2d = 1|a = 1/3, b = 0, c = −1/6, d = 1/2",
    voraussetzungen="Matrizenprodukt|Koeffizientenvergleich|lineare Gleichungen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="B = ((3; 0), (1; 2)) (zeilenweise); C = ((a; b), (c; d))",
    gesucht="Werte von a, b, c und d mit B · C = ((1; 0), (0; 1))",
    verfahren="B · C ausmultiplizieren und eintragsweise mit der Einheitsmatrix gleichsetzen; die vier linearen Gleichungen lösen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="B · C = ((3a; 3b), (a + 2c; b + 2d)) = E, damit a = 1/3, b = 0, c = −1/6, d = 1/2 (amtlich)",
    zwischenergebnis="3a = 1, 3b = 0, a + 2c = 0, b + 2d = 1", niveau_geschaetzt="II",
    fehlerquelle="C · B statt B · C ausmultiplizieren oder Zeile mal Spalte vertauschen",
    bemerkung="Standardbezug: K2 I, K5 II. Amtlich, eigene Rechnung bestätigt (C = B^(−1)). Typ wiederverwendet (2020-ga-A).")
# ---- AG/LA (A2) 1.1: A(−2|1|−2), B(1|2|−1), C(1|1|4), D(d|1|4)
P211 = "Punkte A(−2 | 1 | −2), B(1 | 2 | −1), C(1 | 1 | 4) und für eine reelle Zahl d der Punkt D(d | 1 | 4)"
row("2017MgrundlegendAAGLAA211", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Dreieck aus drei Punkten über nicht kollineare Verbindungsvektoren nachweisen",
    typ_neben="Parametergleichung einer Ebene aus Punkten angeben",
    stichwoerter="AB = (3; 1; 1), AC = (3; 0; 6)|AB ≠ r · AC für alle r|Ebene x = (−2; 1; −2) + s · AB + t · AC",
    voraussetzungen="Verbindungsvektoren|Kollinearität prüfen|Parameterform einer Ebene",
    format="Begründung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=P211,
    gesucht="Nachweis, dass A, B und C Eckpunkte eines Dreiecks sind; eine Gleichung der Ebene, in der das Dreieck liegt",
    verfahren="AB und AC bilden und zeigen, dass sie keine Vielfachen voneinander sind; A als Stützvektor, AB und AC als Spannvektoren",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="AB = (3; 1; 1), AC = (3; 0; 6), AB ≠ r · AC für alle r ∈ IR; x = (−2; 1; −2) + s · AB + t · AC, s, t ∈ IR (amtlich)",
    zwischenergebnis="AB = (3; 1; 1)|AC = (3; 0; 6)", niveau_geschaetzt="II",
    fehlerquelle="nur zeigen, dass die Punkte verschieden sind, ohne die Kollinearität auszuschließen",
    bemerkung="Standardbezug: K1 II, K5 I. Amtlich, eigene Rechnung bestätigt (AB × AC = (6; −15; −3) ≠ 0). Erste Schätzung I; bei der Prüfung gegen die enge Fassung auf II gesetzt – Nachweis der Nichtkollinearität und Ebenengleichung aus denselben Spannvektoren sind eine Verkettung von Standardschritten, keine einzelne Beobachtung.")
row("2017MgrundlegendAAGLAA211", "b", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln", typ_neben="",
    stichwoerter="rechter Winkel in B|AB · BD = 0|BD = (d − 1; −1; 5)|3 · (d − 1) − 1 + 5 = 0, d = −1/3",
    voraussetzungen="Skalarprodukt null bei Orthogonalität|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=P211 + "; das Dreieck ABD ist im Punkt B rechtwinklig",
    gesucht="Wert von d",
    verfahren="Skalarprodukt der Schenkelvektoren in B mit d ansetzen und gleich null setzen",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="AB ∘ BD = 0 ⇔ 3 · (d − 1) + 1 · (−1) + 1 · 5 = 0 ⇔ d = −1/3 (amtlich)",
    zwischenergebnis="BD = (d − 1; −1; 5)", niveau_geschaetzt="II",
    fehlerquelle="die Schenkel am falschen Eckpunkt nehmen (etwa AB · AD)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ga-A).")
# ---- AG/LA (A2) 1.2: Quadrat ABCD in z = 4, Pyramide ABCDS mit Volumen 50
Q212 = "Quadrat ABCD mit A(3 | 3 | 4), B(6 | 7 | 4), C(2 | 10 | 4) und D(−1 | 6 | 4) in der Ebene z = 4"
row("2017MgrundlegendAAGLAA212", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines Quadrats über die Seitenlänge nachweisen", typ_neben="",
    stichwoerter="AB = (3; 4; 0)|Seitenlänge |AB| = 5|Flächeninhalt 5^2 = 25",
    voraussetzungen="Betrag eines Vektors|Flächeninhalt des Quadrats",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=Q212,
    gesucht="Nachweis, dass das Quadrat den Flächeninhalt 25 besitzt",
    verfahren="Seitenlänge als Betrag von AB berechnen und quadrieren",
    schritte="2", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="|AB|^2 = (√25)^2 = 25 (amtlich)",
    zwischenergebnis="|AB| = 5", niveau_geschaetzt="I",
    fehlerquelle="die Diagonale AC als Seite nehmen",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt (|AB| = |BC| = 5, AB · BC = 0). Neuer Typ neben dem rechtwinkligen Dreieck aus 2017-ea-A (Kathetenlängen): Figur Quadrat, eine Seitenlänge genügt.")
row("2017MgrundlegendAAGLAA212", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Höhe einer Pyramide aus dem Volumen bestimmen", typ_neben="",
    stichwoerter="V = 1/3 · 25 · h = 50|h = 6|z-Koordinate 4 + 6 = 10 (oder 4 − 6 = −2)",
    voraussetzungen="Volumenformel der Pyramide|Höhe als Abstand zur Ebene z = 4",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=Q212 + "; Grundfläche 25 (aus a); Punkte S, für die die Pyramide ABCDS das Volumen 50 hat",
    gesucht="die z-Koordinate eines solchen Punktes S",
    verfahren="Höhe aus 1/3 · 25 · h = 50 bestimmen und zur z-Koordinate der Grundebene addieren (oder abziehen)",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2017MgrundlegendAAGLAA212-a",
    ergebnis="1/3 · 25 · h = 50 ⇔ h = 6; mögliche z-Koordinate: 10 (amtlich)",
    zwischenergebnis="h = 6", niveau_geschaetzt="II",
    fehlerquelle="den Faktor 1/3 vergessen (h = 2) oder h selbst als z-Koordinate angeben",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt; auch z = −2 ist möglich (verlangt ist einer der Punkte). Typ wiederverwendet (2026-ga-A).")
# ---- AG/LA (A2) 2: P(−3|2|1), g durch P mit Richtung (1; 3; 0), Q(0|a|0)
G22 = "Punkt P(−3 | 2 | 1), Gerade g: x = OP + r · (1; 3; 0), r ∈ IR, und für eine reelle Zahl a der Punkt Q(0 | a | 0); die Strecke PQ steht senkrecht zu g"
row("2017MgrundlegendAAGLAA22", "a", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Parameter eines Punktes aus der Orthogonalität einer Strecke zu einer Geraden bestimmen", typ_neben="",
    stichwoerter="PQ = (3; a − 2; −1)|PQ · (1; 3; 0) = 0|3 + 3 · (a − 2) = 0, a = 1",
    voraussetzungen="Verbindungsvektor|Skalarprodukt null|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=G22,
    gesucht="Wert von a",
    verfahren="Skalarprodukt von PQ mit dem Richtungsvektor von g gleich null setzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="PQ ∘ (1; 3; 0) = 0 ⇔ 3 + 3 · (a − 2) = 0 ⇔ a = 1 (amtlich)",
    zwischenergebnis="PQ = (3; a − 2; −1)", niveau_geschaetzt="II",
    fehlerquelle="den Ortsvektor von Q statt des Verbindungsvektors PQ mit dem Richtungsvektor multiplizieren",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe 2.")
row("2017MgrundlegendAAGLAA22", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Parameterpaare für Geradenpunkte gleichen Abstands zu einem Punkt über die Symmetrie zum Lotfußpunkt angeben", typ_neben="",
    stichwoerter="P ist Lotfußpunkt von Q auf g (r = 0)|gleicher Abstand von Q genau bei gleichem Abstand von P|Wertepaare (b; −b)",
    voraussetzungen="Lotfußpunkt erkennen|Satz des Pythagoras am Lot|Parameter als Vielfaches des Richtungsvektors deuten",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=G22 + "; a = 1, also Q(0 | 1 | 0) (aus a); zwei Parameterwerte r1 und r2 liefern die Punkte R1 und R2 auf g",
    gesucht="alle Wertepaare (r1; r2), für die R1 und R2 den gleichen Abstand von Q haben, mit Begründung",
    verfahren="Weil PQ senkrecht zu g steht, ist P (r = 0) der Lotfußpunkt; nach Pythagoras haben R1 und R2 genau dann gleichen Abstand von Q, wenn sie gleich weit von P entfernt sind, also r2 = −r1",
    schritte="3", zahlenraum="negativ", einheiten="", abhaengig_von="2017MgrundlegendAAGLAA22-a",
    ergebnis="Wertepaare (b; −b) mit b ∈ IR: da PQ senkrecht zu g steht und OP für r = 0 die Gleichung von g erfüllt, haben R1 und R2 für r1 = b und r2 = −b den gleichen Abstand von Q (amtlich)",
    zwischenergebnis="|R Q|^2 = 10r^2 + 11", niveau_geschaetzt="III",
    fehlerquelle="nur ein einzelnes Paar angeben oder den Abstand mit Wurzeln ausrechnen, statt die Symmetrie zum Lotfußpunkt zu nutzen",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. Amtlich, eigene Rechnung bestätigt: |R1Q|^2 − |R2Q|^2 = 10 · (r1 − r2) · (r1 + r2); der Fall r1 = r2 liefert denselben Punkt und steht im Erwartungshorizont nicht. Eichregel: (b) die Symmetrie der Geradenpunkte zum Lotfußpunkt erkennen und ausnutzen. Aufgabengruppe 2.")
# ---- Stochastik 1.1: Binomialverteilung im Säulendiagramm (n = 15, p = 0,4)
S11_SK = ("Säulendiagramm P(X = k) für k = 0 bis 14, senkrechte Achse bis 0,25 mit Linien bei 0,05, 0,1, 0,15, 0,2, 0,25; Säulenhöhen etwa "
          "k = 1: 0,005, 2: 0,02, 3: 0,06, 4: 0,13, 5: 0,19, 6: 0,21, 7: 0,18, 8: 0,12, 9: 0,06, 10: 0,02, 11: 0,01, ab 12 fast null")
row("2017MgrundlegendAStochastik11", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit eines Intervalls aus dem Säulendiagramm einer Verteilung ablesen", typ_neben="",
    stichwoerter="P(5 <= X <= 7)|Säulen 5, 6, 7 ablesen|0,19 + 0,21 + 0,18 = 0,58",
    voraussetzungen="Säulenhöhen ablesen|Intervallwahrscheinlichkeit als Summe",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=S11_SK, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung der Wahrscheinlichkeitsverteilung einer binomialverteilten Zufallsgröße X mit den Parametern n und p",
    gesucht="P(5 <= X <= 7) mithilfe der Abbildung",
    verfahren="Die Höhen der Säulen bei 5, 6 und 7 ablesen und addieren",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(5 <= X <= 7) ≈ 0,19 + 0,21 + 0,18 = 0,58 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Säule bei 7 oder bei 5 weglassen (strikte statt nicht strikte Ungleichung)",
    bemerkung="Standardbezug: K4 II, K5 I. Amtlich (Ablesewerte), eigene Rechnung mit n = 15, p = 0,4 exakt 0,5696. Schätzung I (einzelne Ablesung mit Summe); der amtliche Bereich ist II (K4 II). Typ wiederverwendet (2023-bebb-gk).")
row("2017MgrundlegendAStochastik11", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Parameter einer Binomialverteilung aus Erwartungswert und Standardabweichung bestimmen", typ_neben="",
    stichwoerter="n · p = 6|n · p · (1 − p) = 3,6|1 − p = 0,6, p = 0,4, n = 15",
    voraussetzungen="Erwartungswert und Varianz der Binomialverteilung|Gleichungen durcheinander teilen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="X binomialverteilt mit den Parametern n und p, Erwartungswert 6, Varianz 3,6",
    gesucht="Werte von n und p",
    verfahren="n · p = 6 in n · p · (1 − p) = 3,6 einsetzen, 1 − p = 0,6 und damit p und n bestimmen",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Gleichungen n · p = 6 und n · p · (1 − p) = 3,6 liefern n = 15 und p = 0,4 (amtlich)",
    zwischenergebnis="1 − p = 0,6", niveau_geschaetzt="II",
    fehlerquelle="3,6 als Standardabweichung statt als Varianz verwenden",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-A); hier ist die Varianz statt der Standardabweichung gegeben.")
# ---- Stochastik 1.2: Münze wählt Würfel A (1–6) oder B (1, 1, 2, 2, 3, 3)
S12 = ("Münze und zwei Würfel: Würfel A mit 1, 2, 3, 4, 5, 6, Würfel B mit 1, 1, 2, 2, 3, 3; zuerst wird die Münze geworfen, bei „Kopf“ "
       "wird Würfel A, bei „Zahl“ Würfel B einmal geworfen und die Zahl notiert")
row("2017MgrundlegendAStochastik12", "a", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="erste Stufe K und Z je 1/2|nach K sechs Äste 1 bis 6 je 1/6|nach Z drei Äste 1, 2, 3 je 1/3",
    voraussetzungen="Laplace-Wahrscheinlichkeiten eines Würfels|gleiche Beschriftungen zusammenfassen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Münze und Würfel", textumfang="mittel",
    gegeben=S12,
    gesucht="beschriftetes Baumdiagramm des Zufallsexperiments",
    verfahren="Erste Stufe Münze mit 1/2 und 1/2; nach Kopf sechs Äste mit 1/6, nach Zahl drei Äste mit 1/3 (je zwei gleiche Seiten zusammengefasst)",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Baum: K (1/2) mit den Ästen 1, 2, 3, 4, 5, 6 zu je 1/6; Z (1/2) mit den Ästen 1, 2, 3 zu je 1/3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="für Würfel B sechs Äste mit je 1/6 ohne Zusammenfassen zeichnen und dabei gleiche Zahlen doppelt beschriften",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2025-ga-A).")
row("2017MgrundlegendAStochastik12", "b", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen", typ_neben="",
    stichwoerter="gerade Zahl mit Würfel A: 1/2|gerade Zahl mit Würfel B (nur die 2): 1/3|1/2 · 1/2 + 1/2 · 1/3 = 5/12",
    voraussetzungen="Pfadmultiplikationsregel|Summenregel|gerade Zahlen je Würfel abzählen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Münze und Würfel", textumfang="kurz",
    gegeben=S12 + "; Baumdiagramm aus a",
    gesucht="Wahrscheinlichkeit, dass die gewürfelte Zahl gerade ist",
    verfahren="Je Würfel den Anteil gerader Zahlen bestimmen, mit 1/2 gewichten und addieren",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2017MgrundlegendAStochastik12-a",
    ergebnis="1/2 · 1/2 + 1/2 · 1/3 = 5/12 (amtlich)",
    zwischenergebnis="P(gerade | A) = 1/2|P(gerade | B) = 1/3", niveau_geschaetzt="II",
    fehlerquelle="bei Würfel B die 2 nur einmal zählen (1/6 statt 1/3)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt. Erste Schätzung I; bei der Prüfung gegen die enge Fassung auf II gesetzt – Abzählen der geraden Zahlen je Würfel und Pfadregeln über zwei Zweige sind eine Verkettung von Standardschritten. Typ wiederverwendet (2023-ea-A): die Münze wählt den Würfel wie sonst die Urne.")
# ---- Stochastik 2: Urnen U1 (4 rot, 2 gelb) und U2 (2 rot, 1 gelb, 1 blau)
U2 = "Urne U1 mit vier roten und zwei gelben Kugeln, Urne U2 mit zwei roten, einer gelben und einer blauen Kugel"
row("2017MgrundlegendAStochastik2", "a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen", typ_neben="",
    stichwoerter="Urne zufällig wählen, je 1/2|zweimal mit Zurücklegen|P(rot) aus U1 2/3, aus U2 1/2|1/2 · 2/3 · 2/3 + 1/2 · 1/2 · 1/2",
    voraussetzungen="Pfadmultiplikationsregel|Summenregel|Ziehen mit Zurücklegen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Urnenexperiment", textumfang="mittel",
    gegeben=U2 + "; eine der Urnen wird zufällig ausgewählt, daraus wird zweimal nacheinander eine Kugel mit Zurücklegen gezogen",
    gesucht="Term für die Wahrscheinlichkeit, dass beide gezogenen Kugeln rot sind",
    verfahren="Je Urne die Wahrscheinlichkeit für zweimal Rot als Quadrat bilden, mit 1/2 gewichten und addieren",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/2 · 2/3 · 2/3 + 1/2 · 1/2 · 1/2 (amtlich); Wert 25/72 ≈ 0,35",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Kugeln beider Urnen zusammenlegen (6 von 10 rot) statt die Urnenwahl als erste Stufe zu nehmen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. Amtlich, eigene Rechnung bestätigt (25/72). Typ wiederverwendet (2023-ea-A). Aufgabengruppe 2.")
row("2017MgrundlegendAStochastik2", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="Bedingung gelb oder blau|aus U1: 1/2 · 1/3, aus U2: 1/2 · 1/2|(1/2 · 1/3)/(1/2 · 1/3 + 1/2 · 1/2) = 2/5",
    voraussetzungen="Ereignis „gelb oder blau“ je Urne zusammenfassen|bedingte Wahrscheinlichkeit gegen die Baumrichtung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urnenexperiment", textumfang="mittel",
    gegeben=U2 + "; eine der Urnen wurde zufällig ausgewählt und daraus eine Kugel gezogen; die Kugel ist gelb oder blau",
    gesucht="Wahrscheinlichkeit, dass die Kugel aus der Urne U1 stammt",
    verfahren="Pfad U1 und „gelb oder blau“ durch die Summe beider Pfade zu „gelb oder blau“ teilen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="(1/2 · 1/3)/(1/2 · 1/3 + 1/2 · 1/2) = 12/30 (amtlich)",
    zwischenergebnis="P(gelb oder blau) = 5/12|12/30 = 2/5", niveau_geschaetzt="III",
    fehlerquelle="P(gelb oder blau | U1) = 1/3 statt der umgekehrten bedingten Wahrscheinlichkeit angeben",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. Amtlich, eigene Rechnung bestätigt (12/30 = 2/5). Aufgabengruppe 2.")

NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Integralwert: Flächenstück mit vorgegebenem Inhalt am Graphen einzeichnen und Integralterm angeben", "Analysis", "Flächeninhalt durch Integration",
     "Am abgebildeten Graphen über das Kästchengitter ein von Graph, Achsen und einer Parallelen zur y-Achse begrenztes Flächenstück mit ungefähr vorgegebenem Inhalt finden, einzeichnen und seinen Inhalt als bestimmtes Integral angeben.", "2017MgrundlegendAAnalysis11-b"),
    ("Fläche: Fläche zwischen Graph und x-Achse zwischen zwei Nullstellen berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Den Inhalt der vom Graphen und der x-Achse eingeschlossenen Fläche als bestimmtes Integral zwischen zwei benachbarten Nullstellen berechnen, wenn der Integrand dazwischen sein Vorzeichen nicht wechselt.", "2017MgrundlegendAAnalysis12-b"),
    ("Matrizenalgebra: Definiertheit von Summe und Produkt zweier Matrizen über die Formate entscheiden", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus den Zeilen- und Spaltenzahlen zweier Matrizen entscheiden und begründen, ob ihre Summe (gleiches Format) und ihr Produkt (Spaltenzahl des linken gleich Zeilenzahl des rechten Faktors) definiert sind.", "2017MgrundlegendAAGLAA11-a"),
    ("Ebene Figur: Dreieck aus drei Punkten über nicht kollineare Verbindungsvektoren nachweisen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Nachweisen, dass drei Punkte Eckpunkte eines Dreiecks sind, indem zwei Verbindungsvektoren als nicht kollinear (keine Vielfachen voneinander) gezeigt werden.", "2017MgrundlegendAAGLAA211-a"),
    ("Ebene Figur: Flächeninhalt eines Quadrats über die Seitenlänge nachweisen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den vorgegebenen Flächeninhalt eines im Raum gegebenen Quadrats bestätigen, indem eine Seitenlänge als Vektorbetrag berechnet und quadriert wird.", "2017MgrundlegendAAGLAA212-a"),
    ("Geraden und Ebenen: Parameter eines Punktes aus der Orthogonalität einer Strecke zu einer Geraden bestimmen", "Analytische Geometrie", "Orthogonalität",
     "Die unbekannte Koordinate eines Punktes so bestimmen, dass seine Verbindungsstrecke zu einem Geradenpunkt senkrecht auf der Geraden steht (Skalarprodukt mit dem Richtungsvektor null).", "2017MgrundlegendAAGLAA22-a"),
    ("Parameterpaare für Geradenpunkte gleichen Abstands zu einem Punkt über die Symmetrie zum Lotfußpunkt angeben", "Analytische Geometrie", "Abstände",
     "Alle Parameterpaare angeben, deren Geradenpunkte von einem Punkt außerhalb gleich weit entfernt sind, und über den Lotfußpunkt als Symmetriezentrum begründen (Parameter entgegengesetzt, wenn der Lotfußpunkt zu r = 0 gehört).", "2017MgrundlegendAAGLAA22-b"),
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
        a(not q["dateidublette_von"], f"{i}: Dublette von {q['dateidublette_von']}, bekommt keine Zeile")
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
                     if einheit(q) == s and not q["dateidublette_von"] and k not in kennungen]
            a(not fehlt, f"Stapel {s} im Bestand unvollständig, es fehlen {fehlt}")
            # v0.9: Dubletten eines angefangenen Stapels zeigen auf erfasste Dateien
            for k, q in QUELLE.items():
                if einheit(q) == s and q["dateidublette_von"]:
                    a(q["dateidublette_von"] in kennungen,
                      f"Stapel {s}: {k} ist Dublette von {q['dateidublette_von']}, die nicht im Katalog steht")
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
                offen.append(f"{pid} ist erfasst, in {', '.join(vorgemerkt[pid])} noch vorgemerkt – abitur-abgleich.py")
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
    dubletten = {k for k in im_stapel if QUELLE[k]["dateidublette_von"]}
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
        erste = QUELLE[k]["dateidublette_von"]
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
                           f"Vermerk mit abitur-abgleich.py in „Dublette von:“ umstellen")
    print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
          "(Häufigkeit in Klammern):")
    liste = umschrift_liste(ZEILEN)
    print("  " + ", ".join(f"{w} ({n_}" + ")" for w, n_ in liste) if liste else "  keines")
    for w in warnung:
        print("Hinweis:", w)
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
