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
    "stapel": "2017-ea-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dateidublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2017MerhoehtBAnalysisWTR1": 50, "2017MerhoehtBAnalysisWTR2": 50, "2017MerhoehtBAnalysisWTR3": 50,
        "2017MerhoehtBAGLAA1WTR": 25,
        "2017MerhoehtBAGLAA2WTR1": 25, "2017MerhoehtBAGLAA2WTR2": 25, "2017MerhoehtBAGLAA2WTR3": 25,
        "2017MerhoehtBStochastikWTR": 25,
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
# Stapel 2017-ea-B, WTR-Zweig (Reserve, geöffnet im Auftrag Nacht 2026-09-28, Teil 2 Punkt 1, wegen der
# Landesheftverweise aus 2017-bb-ea-cas B3.1 auf den CAS-Zweig 2017MerhoehtBAGLAA2CAS2 – Regel „Eine Vormerkung
# überlebt keinen Auftrag“, iqb.md § 7; der WTR-Zweig ist vor dem CAS-Delta zu erfassen). Acht WTR-Dateien,
# 50 + 50 + 50 + 25 + 25 + 25 + 25 + 25 = 275 BE; Standardbezug mit Spalte Anforderungsbereich. Keine
# Dateidublette, keine Aufgabendublette. Poolabgleich: keine Teilaufgabe steht in 2017-bb-ea, 2017-bb-ea-cas
# oder 2017-be-gk (B3.1 Zelt ist nur die CAS-Datei 2); AG/LA (A2) WTR 2 steht als Aufgabe 2.1 im nicht erfassten
# Heft 2017-be-lk. Die CAS-Dateien (2017-iqb-ea-mms) sind der Delta-Stapel 2017-ea-B-cas (Teil 2 Punkt 2).
# ---- Analysis WTR 1 (Aufgabe 1: Wasserbecken am Graphen, 17 BE; Aufgabe 2: Änderungsrate g, 18 BE;
# Aufgabe 3: Schar h_c(x) = c · sin(cx), 15 BE)
BECK = ("Abbildung 1 zeigt den Graphen einer Funktion f, die für 0 <= t <= 15 das Volumen des Wassers in einem Becken "
        "in Abhängigkeit von der Zeit beschreibt; t ist die seit Beobachtungsbeginn vergangene Zeit in Stunden, f(t) das "
        "Volumen in Kubikmetern")
BECK_SK = ("Abbildung 1: Koordinatensystem auf Kästchengitter, t von −1 bis 21 (ein Kästchen = 1 h, Beschriftung 0, 5, 10, "
           "15, 20), y von −50 bis 600 (ein Kästchen = 50 m^3, Beschriftung 0 bis 600 in Hunderterschritten); der Graph von "
           "f geht durch (0; 100), steigt steil zum Hochpunkt bei etwa (3; 570), fällt durch etwa (5; 490) zum Tiefpunkt "
           "bei etwa (10,5; 200), steigt zum Hochpunkt bei etwa (13,8; 240), fällt durch etwa (15; 200) steil und "
           "schneidet die t-Achse bei etwa 17 (über den Definitionsbereich hinaus gezeichnet)")
RATE = ("Für ein anderes Becken beschreibt g(t) = 0,4 · (2t^3 − 39t^2 + 180t) für 0 <= t <= 15 die momentane "
        "Änderungsrate des Wasservolumens in m^3/h, t in Stunden seit Beobachtungsbeginn; G(t) = 0,2 · (t^4 − 26t^3 + "
        "180t^2) ist eine Stammfunktion von g")
SIN = "Für jeden Wert c ∈ IR+ ist die in IR definierte Funktion h_c mit h_c(x) = c · sin(cx) gegeben"
SIN_SK = ("Abbildung 2: Koordinatensystem auf Gitter, x von −π bis 3π (Beschriftung in Schritten von π/2), y von −3 bis "
          "3; eingezeichnet ist der Graph von h_1 (Sinuskurve mit Amplitude 1 und Periode 2π, Nullstellen bei 0, π, 2π, "
          "3π, −π)")
row("2017MerhoehtBAnalysisWTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert an einer Stelle am Graphen im Sachzusammenhang ablesen",
    typ_neben="Nullstellen und Werte: Bereich mit Funktionswerten über einer Schranke aus dem Graphen bestimmen",
    stichwoerter="Volumen nach fünf Stunden f(5) ≈ 490 m^3|Zeitraum mit f(t) >= 350|etwa 0,9 h bis 6,8 h",
    voraussetzungen="Werte am Kästchengitter ablesen|Bedingung f(t) >= 350 als Bereich über der Parallelen y = 350 lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=BECK_SK, kontext="Wasserbecken/Volumen", textumfang="kurz",
    gegeben=BECK,
    gesucht="Volumen des Wassers fünf Stunden nach Beobachtungsbeginn; Zeitraum, in dem das Volumen mindestens 350 m^3 beträgt",
    verfahren="f(5) am Graphen ablesen; die Schnittstellen des Graphen mit der Parallelen y = 350 ablesen, dazwischen liegt der Graph darüber",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="m^3|h", abhaengig_von="",
    ergebnis="Etwa 490 m^3; der Zeitraum beginnt etwa 0,9 h und endet etwa 6,8 h nach Beobachtungsbeginn (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den zweiten Bereich um das Nebenmaximum mitzählen, obwohl der Graph dort unter 350 bleibt",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich (Ablesung). Neuer Typ für das Ablesen eines Funktionswerts; Nebentyp wiederverwendet.")
row("2017MerhoehtBAnalysisWTR1", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Momentane Änderungsrate am Graphen über eine eingezeichnete Tangente bestimmen", typ_neben="",
    stichwoerter="Tangente im Punkt (2; f(2))|Steigungsdreieck Δy/Δt ≈ 360/4|etwa 90 m^3/h",
    voraussetzungen="Tangente an einen Graphen zeichnen|Steigung über ein Steigungsdreieck|Einheit der Änderungsrate",
    format="Rechnung|Zeichnen", operator="Bestimmen Sie", antwort="Zahl|Grafik",
    material="Koordinatensystem", skizze=BECK_SK, kontext="Wasserbecken/Volumen", textumfang="kurz",
    gegeben=BECK,
    gesucht="momentane Änderungsrate des Wasservolumens zwei Stunden nach Beobachtungsbeginn",
    verfahren="In Abbildung 1 die Tangente im Punkt (2; f(2)) einzeichnen und ihre Steigung über ein Steigungsdreieck bestimmen",
    schritte="2", zahlenraum="ganz", einheiten="m^3/h", abhaengig_von="",
    ergebnis="Δy/Δt ≈ 360/4 = 90; die momentane Änderungsrate beträgt etwa 90 m^3/h (amtlich), Tangente und Steigungsdreieck im Erwartungshorizont eingezeichnet",
    zwischenergebnis="Steigungsdreieck mit Δt = 4 und Δy ≈ 360", niveau_geschaetzt="I",
    fehlerquelle="den Funktionswert f(2) statt der Tangentensteigung angeben oder die Sekante durch (0; 100) nehmen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, Ablesewert zeichnungsabhängig. Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Rechnung) – Tangente anlegen und Steigung ablesen ist ein einzelnes Standardverfahren, keine Verkettung zweier Verfahren. Neuer Typ: die Liste kennt die Tangentensteigung am Graphen nur zusammen mit einer mittleren Steigung.")
row("2017MerhoehtBAnalysisWTR1", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Zeitpunkt bei gleichbleibender Änderungsrate über den Schnitt der Tangente mit der Zeitachse grafisch bestimmen", typ_neben="",
    stichwoerter="Änderungsrate ab t = 15 konstant|Tangente im Punkt (15; f(15))|Schnitt mit der t-Achse|etwa 19 h",
    voraussetzungen="konstante Änderungsrate als lineare Fortsetzung mit der Tangentensteigung deuten|Tangente zeichnen|Schnittpunkt ablesen",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text|Zahl",
    material="Koordinatensystem", skizze=BECK_SK, kontext="Wasserbecken/Volumen", textumfang="mittel",
    gegeben=BECK + "; die fünfzehn Stunden nach Beobachtungsbeginn vorliegende momentane Änderungsrate bleibt bis zu dem Zeitpunkt erhalten, zu dem das Becken kein Wasser mehr enthält",
    gesucht="Beschreibung eines Verfahrens, mit dem man diesen Zeitpunkt grafisch bestimmen kann; der Zeitpunkt",
    verfahren="Die Tangente im Punkt (15; f(15)) einzeichnen; ihr Schnittpunkt mit der t-Achse liefert den Zeitpunkt",
    schritte="2", zahlenraum="ganz", einheiten="h", abhaengig_von="",
    ergebnis="Man zeichnet die Tangente an den Graphen von f im Punkt (15; f(15)) ein; die t-Koordinate ihres Schnittpunkts mit der t-Achse ist der gesuchte Zeitpunkt; etwa 19 Stunden nach Beobachtungsbeginn (amtlich)",
    zwischenergebnis="f(15) ≈ 200, Tangentensteigung etwa −50 m^3/h", niveau_geschaetzt="III",
    fehlerquelle="die Nullstelle des Graphen bei etwa 17 statt des Schnitts der Tangente angeben",
    bemerkung="Standardbezug: K3 II, K4 II, K6 II. AB amtlich: II. Amtlich. Schätzung III nach Deutungsliste (a): die gleichbleibende Rate ist erst als Tangente zu deuten (wie die mittlere Rate als Sekante); der amtliche Bereich ist II – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR1", "d", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Funktionalgleichung mit Verschiebung grafisch lösen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="f(t + 6) = f(t) − 350|Volumen sechs Stunden später um 350 m^3 kleiner|Lösung t ≈ 3 (weitere t ≈ 4)",
    voraussetzungen="Verschiebung des Arguments als Zeitabstand deuten|zwei Graphenpunkte mit festem Abstand in t- und y-Richtung suchen",
    format="Kurzantwort", operator="Interpretieren Sie|Geben Sie an", antwort="Text|Zahl",
    material="Koordinatensystem", skizze=BECK_SK, kontext="Wasserbecken/Volumen", textumfang="kurz",
    gegeben=BECK + "; Gleichung f(t + 6) = f(t) − 350",
    gesucht="Interpretation der Gleichung im Sachzusammenhang; eine Lösung der Gleichung",
    verfahren="Die Gleichung beschreibt Zeitpunkte, zu denen das Volumen um 350 m^3 größer ist als sechs Stunden später; am Graphen zwei Punkte im waagerechten Abstand 6 mit Höhenunterschied 350 suchen (etwa (3; 570) und (9; 220))",
    schritte="2", zahlenraum="ganz", einheiten="h|m^3", abhaengig_von="",
    ergebnis="Die Lösung liefert Zeitpunkte, zu denen das Volumen des Wassers 350 m^3 größer ist als sechs Stunden später; t ≈ 3 (Hinweis: weitere Lösung t ≈ 4) (amtlich)",
    zwischenergebnis="f(3) ≈ 570, f(9) ≈ 220", niveau_geschaetzt="III",
    fehlerquelle="f(t + 6) als um 6 nach oben verschobenen Graphen deuten",
    bemerkung="Standardbezug: K2 III, K3 II, K4 II. AB amtlich: III. Amtlich (Ablesung). Typ wiederverwendet (2017-ga-B Analysis 1 c, hier mit Höhenunterschied).")
row("2017MerhoehtBAnalysisWTR1", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Termformen für einen abgebildeten Graphen über Symmetrie und Zahl der Wendepunkte ausschließen", typ_neben="",
    stichwoerter="Form I y = −0,3t^4 + at^2 + 100 nur gerade Exponenten, achsensymmetrisch|Form II ganzrational dritten Grades, genau ein Wendepunkt|Graph weder symmetrisch noch mit nur einem Wendepunkt",
    voraussetzungen="Achsensymmetrie über gerade Exponenten|Zahl der Wendepunkte einer Funktion dritten Grades|Wendepunkte am Graphen erkennen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=BECK_SK, kontext="Wasserbecken/Volumen", textumfang="kurz",
    gegeben=BECK + "; Form I: y = −0,3t^4 + at^2 + 100, a ∈ IR; Form II: y = 8,5t^3 + 3,7t^2 + bt + 100, b ∈ IR",
    gesucht="Begründung, dass die Funktionsgleichung von f weder die Form I noch die Form II hat",
    verfahren="Form I enthält nur gerade Exponenten, ihr Graph ist symmetrisch zur y-Achse, der abgebildete nicht; Form II hat den Grad 3 und damit genau einen Wendepunkt, der abgebildete Graph hat mindestens zwei",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Der Graph einer Funktion der Form I ist symmetrisch bezüglich der y-Achse; der Graph einer Funktion der Form II hat nur einen Wendepunkt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Form II mit dem Argument ausschließen, dass der Graph für große t fällt, obwohl der Leitkoeffizient nur außerhalb des Bereichs wirkt",
    bemerkung="Standardbezug: K1 II, K4 II, K5 II. AB amtlich: II. Amtlich. Neuer Typ: die vorhandenen Symmetrietypen begründen eine Symmetrie am Term, hier werden zwei Termformen am Graphen ausgeschlossen.")
row("2017MerhoehtBAnalysisWTR1", "a", innen="2", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Größte und kleinste Rate im Zeitraum über Ableitung und Randwerte berechnen", typ_neben="",
    stichwoerter="g'(t) = 0,4 · (6t^2 − 78t + 180)|t = 3 und t = 10|Randwerte g(0) = 0, g(15) = 270|Randmaximum bei t = 15",
    voraussetzungen="Ableitung einer ganzrationalen Funktion|quadratische Gleichung|globales Maximum über Randwerte",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Wasserbecken/Änderungsrate", textumfang="mittel",
    gegeben=RATE,
    gesucht="Zeitpunkt im beschriebenen Zeitraum, zu dem die momentane Änderungsrate des Wasservolumens maximal ist",
    verfahren="g'(t) = 0 ⇔ t^2 − 13t + 30 = 0 ⇔ t = 3 oder t = 10; g an diesen Stellen und an den Rändern 0 und 15 vergleichen",
    schritte="3", zahlenraum="ganz|dezimal|negativ", einheiten="h|m^3/h", abhaengig_von="",
    ergebnis="g'(t) = 0,4 · (6t^2 − 78t + 180), g'(t) = 0 ⇔ t = 3 ∨ t = 10; wegen g(0) = 0, g(3) = 97,2, g(10) = −40 und g(15) = 270 ist die momentane Änderungsrate 15 Stunden nach Beobachtungsbeginn maximal (amtlich)",
    zwischenergebnis="g(3) = 97,2|g(10) = −40|g(15) = 270", niveau_geschaetzt="II",
    fehlerquelle="nur die lokale Maximalstelle t = 3 angeben und den Randwert übersehen",
    bemerkung="Standardbezug: K1 I, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet, hier nur die größte Rate (am Rand).")
row("2017MerhoehtBAnalysisWTR1", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zeitraum der Abnahme eines Bestands über Nullstellen und Vorzeichen der Änderungsrate berechnen", typ_neben="",
    stichwoerter="Volumen nimmt ab, wo g(t) < 0|g(t) = 0 ⇔ t = 0, 7,5, 12|g(10) < 0|zwischen 7,5 h und 12 h",
    voraussetzungen="Änderungsrate negativ heißt Bestand nimmt ab|x ausklammern und quadratische Gleichung lösen|Vorzeichen über einen Testwert",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Wasserbecken/Änderungsrate", textumfang="kurz",
    gegeben=RATE,
    gesucht="rechnerisch der Zeitraum, in dem das Volumen des Wassers abnimmt",
    verfahren="g(t) = 0 ⇔ 2t · (t^2 − 19,5t + 90) = 0 ⇔ t = 0, 7,5 oder 12; mit einem Testwert (g(10) < 0) das Intervall mit negativer Rate bestimmen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="h", abhaengig_von="",
    ergebnis="g(t) = 0 ⇔ 2t · (t^2 − 19,5t + 90) = 0 ⇔ t = 0 ∨ t = 7,5 ∨ t = 12; da g(10) < 0, liegt der Zeitraum zwischen 7,5 und 12 Stunden nach Beobachtungsbeginn (amtlich)",
    zwischenergebnis="g(10) = −40", niveau_geschaetzt="II",
    fehlerquelle="den Zeitraum mit fallender Rate (g' < 0) statt negativer Rate angeben",
    bemerkung="Standardbezug: K1 I, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ: der vorhandene Typ begründet die Zunahme auf einem gegebenen Intervall, hier wird das Intervall berechnet.")
row("2017MerhoehtBAnalysisWTR1", "c", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Bestand nach einem Zeitraum aus Anfangsbestand und Integral der Änderungsrate berechnen", typ_neben="",
    stichwoerter="nach drei Stunden 350 m^3|V(0) = 350 − ∫ von 0 bis 3 g(t) dt|G(3) − G(0) = 199,8|etwa 150 m^3",
    voraussetzungen="Zunahme als Integral der Änderungsrate|Integral über die gegebene Stammfunktion|Gleichung nach dem Anfangsbestand auflösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Wasserbecken/Änderungsrate", textumfang="kurz",
    gegeben=RATE + "; drei Stunden nach Beobachtungsbeginn sind im Becken 350 m^3 Wasser enthalten",
    gesucht="Volumen des Wassers zu Beobachtungsbeginn",
    verfahren="Die Zunahme von 0 bis 3 als ∫ von 0 bis 3 g(t) dt = G(3) − G(0) berechnen und von 350 abziehen",
    schritte="2", zahlenraum="dezimal", einheiten="m^3", abhaengig_von="",
    ergebnis="350 − ∫ von 0 bis 3 g(t) dt = 350 − [G(t)] von 0 bis 3 ≈ 150; zu Beobachtungsbeginn enthielt das Becken etwa 150 m^3 Wasser (amtlich)",
    zwischenergebnis="G(3) = 199,8|V(0) = 150,2", niveau_geschaetzt="II",
    fehlerquelle="die Zunahme zu 350 addieren statt abzuziehen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (150,2). Schätzung II (Bestandsgleichung als Standardverfahren, kein Listeneintrag); amtlich III – wie beim graphischen Typ „Anfangsbestand aus Endbestand und Fläche unter dem Ableitungsgraphen ermitteln“ (amtlich III). Bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet, hier rückwärts: Anfangsbestand aus späterem Bestand.")
row("2017MerhoehtBAnalysisWTR1", "d", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zeitpunkt mit gleichem Bestand wie zu Beginn über das Integral der Änderungsrate gleich null untersuchen", typ_neben="",
    stichwoerter="gleiches Volumen wie zu Beginn heißt ∫ von 0 bis x g(t) dt = 0|G(x) − G(0) = 0|x^2 · (x^2 − 26x + 180) = 0|Diskriminante negativ, nur x = 0",
    voraussetzungen="Bestandsänderung als Integral der Rate|Stammfunktion einsetzen|quadratische Gleichung ohne reelle Lösung erkennen",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Wasserbecken/Änderungsrate", textumfang="kurz",
    gegeben=RATE,
    gesucht="rechnerische Untersuchung, ob es nach Beobachtungsbeginn einen Zeitpunkt gibt, zu dem das Wasservolumen ebenso groß ist wie zu Beobachtungsbeginn",
    verfahren="Gleiches Volumen heißt ∫ von 0 bis x g(t) dt = 0, also G(x) − G(0) = 0,2 · x^2 · (x^2 − 26x + 180) = 0; der quadratische Faktor hat keine reelle Nullstelle, es bleibt nur x = 0",
    schritte="3", zahlenraum="ganz|negativ", einheiten="h", abhaengig_von="",
    ergebnis="∫ von 0 bis x g(t) dt = 0 ⇔ [G(t)] von 0 bis x = 0 ⇔ x^2 · (x^2 − 26x + 180) = 0 ⇔ x = 0; es gibt nach Beobachtungsbeginn keinen solchen Zeitpunkt (amtlich)",
    zwischenergebnis="Diskriminante 26^2 − 4 · 180 = −44 < 0", niveau_geschaetzt="III",
    fehlerquelle="g(t) = 0 statt des Integrals gleich null ansetzen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR1", "a", innen="3", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Graph der Schar zu einem Parameterwert in die Abbildung skizzieren", typ_neben="",
    stichwoerter="h_(1/2): Amplitude 1/2, Periode 4π|h_2: Amplitude 2, Periode π|in Abbildung 2 zu h_1",
    voraussetzungen="Amplitude und Periode aus c · sin(cx) ablesen|Sinuskurve skizzieren",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=SIN_SK, kontext="ohne", textumfang="kurz",
    gegeben=SIN + "; Abbildung 2 zeigt den Graphen von h_1",
    gesucht="Skizze der Graphen von h_c für c = 1/2 und c = 2 in Abbildung 2",
    verfahren="h_(1/2): Amplitude 1/2, Periode 4π, Nullstellen bei Vielfachen von 2π; h_2: Amplitude 2, Periode π, Nullstellen bei Vielfachen von π/2",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Graph zu c = 1/2 (gestrichelt): Hochpunkt (π; 1/2), Nullstelle 2π, Tiefpunkt (3π; −1/2); Graph zu c = 2 (gepunktet): Hochpunkte (π/4; 2), (5π/4; 2), Tiefpunkte (3π/4; −2), Nullstellen bei Vielfachen von π/2 (amtlich), Skizze im Erwartungshorizont",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur die Periode oder nur die Amplitude ändern",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich. Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung – Amplitude und Periode stehen beide unmittelbar im Term c · sin(cx), jede Skizze ist ein einzelnes Standardverfahren; anders als Analysis WTR 2 1 h, wo die Streckung erst aus einer Funktionalgleichung zu lesen ist. Typ wiederverwendet.")
row("2017MerhoehtBAnalysisWTR1", "b", innen="3", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen", typ_neben="",
    stichwoerter="benachbarte positive Nullstelle u = π/c|∫ von 0 bis π/c c · sin(cx) dx|[−cos(cx)] = 2|Inhalt unabhängig von c",
    voraussetzungen="Nullstellen der Sinusfunktion|Stammfunktion von c · sin(cx) mit linearer Kette|Integral über eine Halbperiode",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SIN + "; eine Nullstelle von h_c ist 0, die benachbarte positive Nullstelle heißt u",
    gesucht="u in Abhängigkeit von c; Inhalt des Flächenstücks, das der Graph von h_c für 0 <= x <= u mit der x-Achse einschließt",
    verfahren="sin(cx) = 0 ⇔ cx = kπ, also u = π/c; Stammfunktion −cos(cx), Integral von 0 bis π/c",
    schritte="3", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="Mit u = π/c ergibt sich ∫ von 0 bis π/c h_c(x) dx = [−cos(cx)] von 0 bis π/c = 2 (amtlich)",
    zwischenergebnis="u = π/c", niveau_geschaetzt="II",
    fehlerquelle="die Stammfunktion ohne Nachdifferenzieren als −c · cos(cx) ansetzen",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet; der Inhalt hängt hier nicht von c ab.")
row("2017MerhoehtBAnalysisWTR1", "c", innen="3", seite="3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Extrempunkt einer trigonometrischen Schar ohne Ableitung über benachbarte Nullstellen bestimmen", typ_neben="",
    stichwoerter="ohne Ableitungsfunktion|Mitte der Nullstellen π/c und 2π/c|x = 3π/(2c), y = −c",
    voraussetzungen="Symmetrie der Sinuskurve zwischen zwei Nullstellen|Nullstellen von h_c|Funktionswert berechnen",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SIN + "; die Nullstellen sind die Vielfachen von π/c",
    gesucht="Beschreibung, wie man ohne Verwendung einer Ableitungsfunktion die Koordinaten eines Tiefpunkts in Abhängigkeit von c ermitteln kann; die Koordinaten eines Tiefpunkts",
    verfahren="Die x-Koordinate eines Tiefpunkts ist der Mittelwert der Nullstellen π/c und 2π/c (dort ist der Graph unterhalb der x-Achse), die y-Koordinate der Funktionswert dort",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2017MerhoehtBAnalysisWTR1-3b",
    ergebnis="Die x-Koordinate eines Tiefpunkts ergibt sich als Mittelwert der beiden kleinsten positiven Nullstellen von h_c, die y-Koordinate als entsprechender Funktionswert; x = 3π/(2c), y = −c (amtlich)",
    zwischenergebnis="h_c(3π/(2c)) = c · sin(3π/2) = −c", niveau_geschaetzt="II",
    fehlerquelle="die Mitte von 0 und π/c nehmen und so einen Hochpunkt angeben",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR1", "d", innen="3", seite="3", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Term einer höheren Ableitung einer Sinusfunktion über die Periodizität der Ableitungen angeben", typ_neben="",
    stichwoerter="jede Ableitung liefert den Faktor c|Folge sin, cos, −sin, −cos mit Periode 4|103 = 4 · 25 + 3|−c^104 · cos(cx)",
    voraussetzungen="Ableitung von sin und cos mit linearer Kette|Periodizität der Ableitungsfolge erkennen|Rest bei Division durch 4",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SIN,
    gesucht="ein Term der 103. Ableitung von h_c",
    verfahren="Die ersten Ableitungen bilden: c^2 · cos(cx), −c^3 · sin(cx), −c^4 · cos(cx), c^5 · sin(cx); das Muster wiederholt sich nach vier Schritten, jede Ableitung liefert einen Faktor c; 103 lässt bei Division durch 4 den Rest 3",
    schritte="3", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="h_c^(103)(x) = −c^104 · cos(cx) (amtlich)",
    zwischenergebnis="h_c'(x) = c^2 · cos(cx)|h_c''(x) = −c^3 · sin(cx)|h_c'''(x) = −c^4 · cos(cx)", niveau_geschaetzt="III",
    fehlerquelle="den Exponenten von c als 103 statt 104 angeben oder das Vorzeichen aus dem falschen Rest bestimmen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
# ---- Analysis WTR 2 (Aufgabe 1: Schar f_k mit Integralfunktionen, 32 BE; Aufgabe 2: Schale aus Stein, 18 BE)
FK = ("Für jedes k ∈ IR+ ist die Funktion f_k mit f_k(x) = k^2x^3 − 6kx^2 + 9x, x ∈ IR, gegeben; ihr Graph heißt G_k")
FK_SK = ("Abbildung 1: Koordinatensystem auf Kästchengitter, x von −1 bis 11 (ein Kästchen = 1), y von −1 bis 17 "
         "(ein Kästchen = 1, Beschriftung in Zweierschritten); Graph II geht durch den Ursprung, hat den Hochpunkt (3; 12) "
         "und berührt die x-Achse im Tiefpunkt (9; 0); Graph I ist Graph II um 4 nach oben verschoben (y-Achsenabschnitt "
         "4, Hochpunkt (3; 16), Tiefpunkt (9; 4)); beide kommen von unten links und steigen rechts steil an")
F1_SK = ("Abbildung 2: Koordinatensystem auf Kästchengitter, x von −1 bis 11, y von −9 bis 9 (Beschriftung in Zweierschritten); "
         "Graph G_1 von f_1(x) = x^3 − 6x^2 + 9x: kommt von unten links, geht durch den Ursprung, Hochpunkt (1; 4), berührt "
         "die x-Achse im Tiefpunkt (3; 0) und steigt dann steil an")
LM = ("f_1(x) = x^3 − 6x^2 + 9x mit Graph G_1 (Abbildung 2: Nullstelle 0 mit Vorzeichenwechsel von minus nach plus, "
      "Hochpunkt (1; 4), doppelte Nullstelle 3 im Tiefpunkt); betrachtet werden die in IR definierten Funktionen L und M "
      "mit L(x) = ∫ von 0 bis x f_1(t) dt und M(x) = ∫ von 3 bis x f_1(t) dt")
SCH = ("Eine große rotationssymmetrische Schale ist aus einem Steinblock gefertigt; ein Kubikmeter des Steins hat eine "
       "Masse von 2700 kg; im Querschnitt wird die Schale durch die Graphen von p(x) = √(6x), 0 <= x <= 6 (Außenseite), "
       "und q(x) = √(4x − 8), 2 <= x <= 6 (Innenseite), und ihre Spiegelbilder an der x-Achse dargestellt; die x-Achse ist "
       "die Rotationsachse, 1 LE = 1 dm")
SCH_SK = ("Abbildung 3: Koordinatensystem, x von −1 bis 7, y von −7 bis 7; Querschnitt der liegenden Schale: äußere Kurve "
          "y = ±√(6x) vom Ursprung bis x = 6 (y = ±6), innere Kurve y = ±√(4x − 8) von (2; 0) bis x = 6 (y = ±4); bei x = 6 "
          "senkrechte Randstücke von 4 bis 6 und von −4 bis −6")
row("2017MerhoehtBAnalysisWTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Grenzverhalten einer ganzrationalen Funktion angeben", typ_neben="",
    stichwoerter="Leitterm k^2x^3 mit k^2 > 0|x → −∞: f_k(x) → −∞|x → +∞: f_k(x) → +∞",
    voraussetzungen="Verhalten über Grad und Vorzeichen des Leitkoeffizienten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FK,
    gesucht="Verhalten von f_k für x → −∞ und x → +∞",
    verfahren="Der Leitterm k^2x^3 hat ungeraden Grad und positiven Koeffizienten",
    schritte="1", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="lim für x → −∞ von f_k(x) = −∞, lim für x → +∞ von f_k(x) = +∞ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den Leitkoeffizienten k^2 für negativ halten, weil k gesucht ist",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich. Typ wiederverwendet (mit Parameter).")
row("2017MerhoehtBAnalysisWTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstellen einer ganzrationalen Funktion durch Ausklammern und Faktorisieren berechnen", typ_neben="",
    stichwoerter="x ausklammern|k^2x^2 − 6kx + 9 = (kx − 3)^2|Nullstellen 0 und 3/k",
    voraussetzungen="Ausklammern|binomische Formel oder p-q-Formel mit Parameter|Satz vom Nullprodukt",
    format="Rechnung", operator="Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FK,
    gesucht="Nullstellen von f_k",
    verfahren="f_k(x) = x · (k^2x^2 − 6kx + 9) = x · (kx − 3)^2 = 0",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f_k(x) = 0 ⇔ x = 0 ∨ x = 3/k (amtlich)",
    zwischenergebnis="f_k(x) = x · (kx − 3)^2", niveau_geschaetzt="I",
    fehlerquelle="die doppelte Nullstelle 3/k übersehen oder nur x = 0 angeben",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Rechnung) – Nullstellen durch Ausklammern und Faktorisieren sind ein einzelnes Standardverfahren, keine Verkettung zweier Verfahren. Typ wiederverwendet (mit Parameter).")
row("2017MerhoehtBAnalysisWTR2", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Symmetrieart am Term über die Exponenten begründen", typ_neben="",
    stichwoerter="Exponenten 3 und 1 ungerade, 2 gerade|weder punktsymmetrisch zum Ursprung noch achsensymmetrisch zur y-Achse",
    voraussetzungen="Symmetrie ganzrationaler Funktionen über die Parität der Exponenten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FK,
    gesucht="Begründung, dass G_k weder bezüglich des Koordinatenursprungs noch bezüglich der y-Achse symmetrisch ist",
    verfahren="Der Term enthält Potenzen von x mit geraden und mit ungeraden Exponenten",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_k ist eine ganzrationale Funktion, deren Term Potenzen von x mit geraden und ungeraden Exponenten enthält (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur eine der beiden Symmetriearten ausschließen",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet, hier für fehlende Symmetrie.")
row("2017MerhoehtBAnalysisWTR2", "d", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung mit Parameter in faktorisierter Form nachweisen", typ_neben="",
    stichwoerter="f_k'(x) = 3k^2x^2 − 12kx + 9|3 · (kx − 1) · (kx − 3) ausmultiplizieren",
    voraussetzungen="Potenzregel mit Parameter|Ausmultiplizieren",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FK,
    gesucht="Nachweis, dass f_k'(x) = 3 · (kx − 1) · (kx − 3) eine Gleichung der ersten Ableitungsfunktion ist",
    verfahren="f_k ableiten und den vorgegebenen Term ausmultiplizieren, beide stimmen überein",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_k'(x) = 3k^2x^2 − 12kx + 9 und 3 · (kx − 1) · (kx − 3) = 3k^2x^2 − 12kx + 9 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="k beim Ableiten wie eine Variable behandeln",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung I (eine Rechnung, ableiten und ausmultiplizieren); amtlich II – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt (wie 2017-ga-B Analysis 1 d). Typ wiederverwendet.")
row("2017MerhoehtBAnalysisWTR2", "e", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus dem Abstand der Extremstellen berechnen", typ_neben="",
    stichwoerter="f_k'(x) = 0 ⇔ x = 1/k oder x = 3/k|Differenz 2/k = 6|k = 1/3",
    voraussetzungen="Satz vom Nullprodukt an der faktorisierten Ableitung|Bruchgleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FK + "; f_k'(x) = 3 · (kx − 1) · (kx − 3); G_k hat zwei Extrempunkte",
    gesucht="derjenige Wert von k, für den sich die x-Koordinaten der beiden Extrempunkte von G_k um 6 unterscheiden",
    verfahren="Extremstellen 1/k und 3/k (Vorzeichenwechsel der Ableitung); 3/k − 1/k = 6 nach k auflösen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="2017MerhoehtBAnalysisWTR2-1d",
    ergebnis="f_k'(x) = 0 ⇔ x = 1/k ∨ x = 3/k; 3/k − 1/k = 6 ⇔ k = 1/3 (amtlich)",
    zwischenergebnis="Extremstellen 1/k und 3/k", niveau_geschaetzt="II",
    fehlerquelle="die Differenz der y-Koordinaten gleich 6 setzen",
    bemerkung="Standardbezug: K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "f", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Parallelität der Wendetangenten einer Schar über eine parameterunabhängige Steigung nachweisen", typ_neben="",
    stichwoerter="Wendepunkt (2/k; 2/k)|f_k'(2/k) = −3 für jedes k|gleiche Steigung heißt parallel",
    voraussetzungen="Ableitungswert mit Parameter berechnen|parallele Geraden haben gleiche Steigung",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FK + "; f_k'(x) = 3 · (kx − 1) · (kx − 3); für jeden Wert von k wird die Tangente an G_k im Wendepunkt (2/k; 2/k) betrachtet",
    gesucht="Nachweis, dass die Tangenten für unterschiedliche Werte von k parallel zueinander sind",
    verfahren="f_k'(2/k) = 3 · (2 − 1) · (2 − 3) = −3 hängt nicht von k ab",
    schritte="2", zahlenraum="negativ|Bruch", einheiten="", abhaengig_von="2017MerhoehtBAnalysisWTR2-1d",
    ergebnis="Für jeden Wert von k ist die Steigung der betrachteten Tangente f_k'(2/k) = −3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Tangentengleichung für ein einzelnes k aufstellen statt allgemein",
    bemerkung="Standardbezug: K1 II, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (f_k''(2/k) = 0, f_k(2/k) = 2/k). Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "g", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Graphen einer Scharfunktion und ihrer in y-Richtung verschobenen Fassung zuordnen und Parameter und Verschiebung bestimmen", typ_neben="",
    stichwoerter="h(x) = f_k(x) + d, d ≠ 0|nur G_k geht durch den Ursprung|d = 4 aus dem y-Achsenabschnitt von I|k = 1/3 aus den Extremstellen 3 und 9",
    voraussetzungen="f_k(0) = 0 für alle k|Verschiebung in y-Richtung|Extremstellen 1/k und 3/k",
    format="Kurzantwort|Begründung", operator="Ordnen Sie zu|Begründen Sie|Bestimmen Sie", antwort="Text|Zahl",
    material="Koordinatensystem", skizze=FK_SK, kontext="ohne", textumfang="mittel",
    gegeben=FK + "; die Extremstellen von G_k sind 1/k und 3/k; Abbildung 1 zeigt für einen bestimmten Wert von k den Graphen von f_k und den Graphen der Funktion h mit h(x) = f_k(x) + d, d ∈ IR \\ {0}",
    gesucht="Zuordnung der beiden Funktionen zu den Graphen I und II mit Begründung; die Werte von k und d",
    verfahren="Nur G_k geht durch den Ursprung, also ist II der Graph von f_k; d als y-Achsenabschnitt von I; k aus der Lage der Extremstellen von II (1/k = 3)",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2017MerhoehtBAnalysisWTR2-1e",
    ergebnis="I: h, II: f_k; nur der Graph II verläuft durch den Koordinatenursprung; der Schnittpunkt von I mit der y-Achse liefert d = 4, die Lage der Extrempunkte von II k = 1/3 (amtlich)",
    zwischenergebnis="f_(1/3) hat Hochpunkt (3; 12) und Tiefpunkt (9; 0)", niveau_geschaetzt="II",
    fehlerquelle="den höher liegenden Graphen I für f_k halten",
    bemerkung="Standardbezug: K1 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ: die vorhandenen Zuordnungstypen ordnen Scharmitglieder einander zu, hier eine Scharfunktion und ihre Verschiebung.")
row("2017MerhoehtBAnalysisWTR2", "h", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Streckungen in x- und y-Richtung aus einer Funktionalgleichung f2(x) = a · f1(bx) beschreiben", typ_neben="",
    stichwoerter="f_2(x) = 1/2 · f_1(2x)|Streckung in x-Richtung mit 1/2|Streckung in y-Richtung mit 1/2",
    voraussetzungen="Wirkung von b in f(bx) als Streckung mit 1/b|Wirkung eines Faktors vor f",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FK + "; für alle x ∈ IR gilt f_2(x) = 1/2 · f_1(2x)",
    gesucht="Beschreibung, wie der Graph von f_2 aus dem Graphen von f_1 hervorgeht",
    verfahren="Der Faktor 2 im Argument staucht in x-Richtung (Faktor 1/2), der Vorfaktor 1/2 staucht in y-Richtung",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Der Graph von f_2 geht aus dem Graphen von f_1 durch Streckung mit dem Faktor 1/2 in x-Richtung und Streckung mit dem Faktor 1/2 in y-Richtung hervor (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Streckung in x-Richtung mit dem Faktor 2 statt 1/2 angeben",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (f_2(x) − 1/2 · f_1(2x) = 0). Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "i", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Extrempunkt einer Integralfunktion ohne Rechnung über den Vorzeichenwechsel des Integranden begründen", typ_neben="",
    stichwoerter="L(0) = 0|L' = f_1|f_1(0) = 0 mit Vorzeichenwechsel von minus nach plus|Tiefpunkt (0; 0)",
    voraussetzungen="Integralfunktion mit gleichen Grenzen null|Ableitung der Integralfunktion ist der Integrand|Vorzeichenwechsel am Graphen ablesen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=F1_SK, kontext="ohne", textumfang="kurz",
    gegeben=LM,
    gesucht="Begründung ohne Rechnung, dass der Punkt (0; 0) Tiefpunkt des Graphen von L ist",
    verfahren="L(0) = 0; L' = f_1 hat bei 0 eine Nullstelle, links davon ist f_1 negativ, rechts positiv",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="L(0) = 0, L'(x) = f_1(x), f_1(0) = 0, f_1(x) < 0 für x < 0, f_1(x) > 0 für x > 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur L(0) = 0 zeigen und den Vorzeichenwechsel weglassen",
    bemerkung="Standardbezug: K1 II, K4 II, K5 II. AB amtlich: II. Amtlich. Erste Schätzung: III; korrigiert nach dem Prinzip der Deutungsliste (eine Deutung zählt nur, wenn sie zu finden ist) – der Tiefpunkt ist vorgegeben, (e) greift nicht; zu begründen bleibt eine Routine. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "j", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Waagerechte Tangente und Wendepunkt einer Integralfunktion an einer doppelten Nullstelle des Integranden begründen", typ_neben="",
    stichwoerter="f_1(3) = 0: Tangente an L bei x = 3 parallel zur x-Achse|f_1 hat bei 3 einen Tiefpunkt: L hat dort einen Wendepunkt|Sattelpunkt",
    voraussetzungen="L' = f_1, L'' = f_1'|Extremstelle von L' als Wendestelle von L",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=F1_SK, kontext="ohne", textumfang="kurz",
    gegeben=LM,
    gesucht="zwei besondere Eigenschaften des Graphen von L bei x = 3 mit Begründung",
    verfahren="L'(3) = f_1(3) = 0, also waagerechte Tangente; f_1 = L' hat bei 3 einen Tiefpunkt, also ist 3 Wendestelle von L",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Tangente an den Graphen von L im Punkt (3; L(3)) verläuft parallel zur x-Achse, weil f_1(3) = 0; der Graph von L besitzt im Punkt (3; L(3)) einen Wendepunkt, weil der Graph von f_1 im Punkt (3; f_1(3)) einen Tiefpunkt hat (amtlich)",
    zwischenergebnis="L(3) = 27/4", niveau_geschaetzt="III",
    fehlerquelle="aus L'(3) = 0 auf einen Extrempunkt schließen, obwohl kein Vorzeichenwechsel vorliegt",
    bemerkung="Standardbezug: K1 III, K4 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (L(3) = 27/4). Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "k", innen="1", seite="2", punkte="2", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Integralfunktionen mit verschiedenen unteren Grenzen als Verschiebung in y-Richtung begründen", typ_neben="",
    stichwoerter="M(x) = L(x) − ∫ von 0 bis 3 f_1(t) dt|Integral von 0 bis 3 positiv, weil f_1 dort nicht negativ|Verschiebung nach unten um 27/4",
    voraussetzungen="Intervalladditivität des Integrals|Vorzeichen eines Integrals aus der Lage des Graphen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=F1_SK, kontext="ohne", textumfang="kurz",
    gegeben=LM,
    gesucht="Begründung, dass der Graph der Funktion M aus dem Graphen der Funktion L durch eine Verschiebung in negative y-Richtung hervorgeht",
    verfahren="∫ von 3 bis x = ∫ von 0 bis x − ∫ von 0 bis 3, also M(x) = L(x) − L(3); L(3) > 0, weil der Graph von f_1 zwischen 0 und 3 oberhalb der x-Achse liegt",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="M(x) = L(x) − ∫ von 0 bis 3 f_1(t) dt; der Abbildung ist zu entnehmen, dass ∫ von 0 bis 3 f_1(t) dt > 0 gilt (amtlich)",
    zwischenergebnis="∫ von 0 bis 3 f_1(t) dt = 27/4", niveau_geschaetzt="III",
    fehlerquelle="die Verschiebung in x-Richtung um 3 annehmen",
    bemerkung="Standardbezug: K1 III, K4 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (27/4). Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Differenz zweier Funktionswerte als Abstand im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="p(6) − q(6) = 6 − 4 = 2|senkrechter Abstand von Außen- und Innenseite am oberen Rand|Breite des Rands in dm",
    voraussetzungen="Funktionswerte als Abstände zur Rotationsachse deuten",
    format="Kurzantwort", operator="Interpretieren Sie", antwort="Text",
    material="Koordinatensystem", skizze=SCH_SK, kontext="Steinmetz/Schale", textumfang="kurz",
    gegeben=SCH,
    gesucht="Interpretation des Terms p(6) − q(6) im Sachzusammenhang",
    verfahren="p(6) und q(6) sind die Radien von Außen- und Innenseite am oberen Rand; ihre Differenz ist die Breite des Rands",
    schritte="1", zahlenraum="ganz|Wurzel", einheiten="dm", abhaengig_von="",
    ergebnis="Der Term gibt die Breite des Rands der Schale in Dezimetern an (amtlich)",
    zwischenergebnis="p(6) − q(6) = 2", niveau_geschaetzt="I",
    fehlerquelle="den Term als Höhe der Schale oder als Dicke des Bodens deuten",
    bemerkung="Standardbezug: K1 I, K3 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung: 2 dm. Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Beobachtung) – eine einzelne Deutung zweier Funktionswerte ohne Verkettung, die Ausnahme zu (d) setzt die Grenze nach oben, nicht II. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "b", innen="2", seite="3", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Graph der Füllhöhe in Abhängigkeit von der Zeit über die Gefäßform auswählen und begründen", typ_neben="",
    stichwoerter="konstante Zuflussrate|Durchmesser nimmt nach oben zu|Füllhöhe wächst immer langsamer|Graph II",
    voraussetzungen="Änderungsrate der Füllhöhe umgekehrt zur Querschnittsfläche|rechtsgekrümmter Graph heißt abnehmende Rate",
    format="Kurzantwort|Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Diagramm", skizze="drei Skizzen Füllhöhe gegen Zeit ohne Skalierung: I Ursprungsgerade, II vom Ursprung rechtsgekrümmt steigend (flacher werdend), III vom Ursprung linksgekrümmt steigend (steiler werdend)", kontext="Steinmetz/Schale", textumfang="mittel",
    gegeben=SCH + "; in die aufrecht stehende Schale wird mit konstanter Zuflussrate Wasser gefüllt",
    gesucht="Entscheidung, welcher der Graphen I, II und III die Füllhöhe in Abhängigkeit von der Zeit beschreibt, mit Begründung",
    verfahren="Die Schale wird nach oben weiter, bei konstanter Zuflussrate steigt die Füllhöhe immer langsamer: rechtsgekrümmter Graph",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Graph II; da der Durchmesser der Schale nach oben hin zunimmt, nimmt die Änderungsrate der Füllhöhe mit der Zeit ab (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Graph III wählen, weil die Schale oben breiter ist",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "c", innen="2", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Querschnittsfläche eines Rotationskörpers in Abhängigkeit von der Füllhöhe als Term nachweisen", typ_neben="",
    stichwoerter="Boden des Innenraums bei x = 2|Füllhöhe h entspricht x = 2 + h|Radius q(2 + h) = √(4h)|A(h) = π · 4h",
    voraussetzungen="Füllhöhe in die x-Koordinate übersetzen|Kreisfläche π · r^2",
    format="Begründung", operator="Weisen Sie nach", antwort="Term",
    material="Koordinatensystem", skizze=SCH_SK, kontext="Steinmetz/Schale", textumfang="kurz",
    gegeben=SCH + "; die aufrecht stehende Schale wird mit Wasser gefüllt, h ist die Füllhöhe in dm",
    gesucht="Nachweis, dass der Flächeninhalt A der Wasseroberfläche (in dm^2) mit A(h) = 4πh berechnet werden kann",
    verfahren="Die Wasseroberfläche ist ein Kreis mit Radius q(2 + h), weil der Innenraum bei x = 2 beginnt; A(h) = π · (q(2 + h))^2",
    schritte="2", zahlenraum="Wurzel", einheiten="dm|dm^2", abhaengig_von="",
    ergebnis="A(h) = π · (q(2 + h))^2 = 4πh (amtlich)",
    zwischenergebnis="(q(2 + h))^2 = 4h", niveau_geschaetzt="II",
    fehlerquelle="q(h) statt q(2 + h) einsetzen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR2", "d", innen="2", seite="3", punkte="4", afb_amtlich="III",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Integralfunktion im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="s(x) = π · ∫ von 2 bis 2 + x (q(t))^2 dt|Wasservolumen bei Füllhöhe x|Definitionsbereich [0; 4]",
    voraussetzungen="Rotationsvolumen π · ∫ f^2|obere Grenze 2 + x als Füllhöhe x|Füllhöhe höchstens 4 dm",
    format="Kurzantwort", operator="Interpretieren Sie|Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=SCH_SK, kontext="Steinmetz/Schale", textumfang="kurz",
    gegeben=SCH + "; die aufrecht stehende Schale wird mit Wasser gefüllt; s(x) = π · ∫ von 2 bis 2 + x (q(t))^2 dt",
    gesucht="Interpretation der Funktion s im Sachzusammenhang; größter im Sachzusammenhang sinnvoller Definitionsbereich von s",
    verfahren="s(x) ist das Volumen des Rotationskörpers zwischen Boden (x = 2) und Füllhöhe x, also das Wasservolumen; x reicht von 0 bis zur Randhöhe 6 − 2 = 4",
    schritte="2", zahlenraum="ganz", einheiten="dm|dm^3", abhaengig_von="",
    ergebnis="Die Funktion s beschreibt das Volumen des Wassers in der Schale in dm^3 in Abhängigkeit von der Füllhöhe x in dm; Definitionsbereich [0; 4] (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="den Definitionsbereich [2; 6] aus den Grenzen von q übernehmen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 III. AB amtlich: III. Amtlich. Typ wiederverwendet.")
row("2017MerhoehtBAnalysisWTR2", "e", innen="2", seite="3", punkte="6", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Masse eines Hohlkörpers aus der Differenz zweier Rotationsvolumina berechnen", typ_neben="",
    stichwoerter="Volumen außen π · ∫ von 0 bis 6 6x dx = 108π|Hohlraum π · ∫ von 2 bis 6 (4x − 8) dx = 32π|76π dm^3|2,7 kg/dm^3, etwa 645 kg",
    voraussetzungen="Rotationsvolumen um die x-Achse|Differenz aus Vollkörper und Hohlraum|1 m^3 = 1000 dm^3",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=SCH_SK, kontext="Steinmetz/Schale", textumfang="kurz",
    gegeben=SCH,
    gesucht="Masse der Schale",
    verfahren="Volumen des Steins als Rotationsvolumen der Außenkurve p über [0; 6] minus Rotationsvolumen der Innenkurve q über [2; 6]; 2700 kg/m^3 = 2,7 kg/dm^3",
    schritte="4", zahlenraum="Wurzel|dezimal", einheiten="dm^3|kg", abhaengig_von="",
    ergebnis="π · ∫ von 0 bis 6 (p(x))^2 dx − π · ∫ von 2 bis 6 (q(x))^2 dx = π · [3x^2] von 0 bis 6 − π · [2x^2 − 8x] von 2 bis 6 = 76π; 76π · 2,7 ≈ 645, d. h. die Masse der Schale beträgt etwa 645 kg (amtlich)",
    zwischenergebnis="108π − 32π = 76π ≈ 238,8 dm^3", niveau_geschaetzt="III",
    fehlerquelle="beide Integrale über [0; 6] erstreckt oder die Einheit dm^3 nicht in m^3 umgerechnet",
    bemerkung="Standardbezug: K2 III, K3 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (644,7 kg). Erste Schätzung: II; korrigiert nach Deutungsliste (a) – der Stein ist erst geometrisch als Vollkörper minus Hohlraum mit verschiedenen Grenzen zu erkennen und in zwei Integrale zu übersetzen; dieselbe Regel war bei Analysis WTR 3 2 d (Querschnitt des Unterbaus) angewandt, hier nicht – Regel ungleich angewandt. Neuer Typ.")
# ---- Analysis WTR 3 (Aufgabe 1: Schar f_k(x) = −x^4 + 6kx^2, 22 BE; Aufgabe 2: Trainingsgerät, 28 BE)
FS = "Gegeben ist die Schar der Funktionen f_k mit f_k(x) = −x^4 + 6kx^2, x ∈ IR und k ∈ IR; der Graph von f_k heißt G_k"
FS_SK = ("Abbildung 1: Koordinatensystem, x von etwa −1,8 bis 1,8, y von −2 bis 3,5; Graph I (durchgezogen) steigt vom "
         "Ursprung nach beiden Seiten steil über den Bildrand; Graph II (gestrichelt) geht durch den Ursprung und hat zwei "
         "Hochpunkte bei etwa (±1,2; 2,2), fällt außen steil; Graph III (gepunktet) liegt unterhalb der x-Achse, "
         "berührt sie im Ursprung und fällt nach beiden Seiten")
GER = ("Ein Trainingsgerät zur Schulung der Koordination besteht aus einem Unterbau und einem 2 cm dicken Standbrett "
       "(60 cm breit, 40 cm lang), das seitlich ohne Überstand mit dem Unterbau abschließt; das Gerät hat auf seiner "
       "gesamten Länge den gleichen Querschnitt; bei horizontal ausgerichtetem Standbrett wird die untere Profillinie des "
       "Unterbaus für −3 <= x <= 3 durch p(x) = −1/48 · (x^4 − 18x^2) beschrieben; der horizontale Untergrund ist die "
       "x-Achse, 1 LE = 1 dm")
GER_SK = ("Abbildung 2: Schrägbild des Geräts: waagerechtes Standbrett (Breite 60 cm, Länge 40 cm), darunter der Unterbau mit "
          "nach unten gewölbter Profillinie; Abbildung 3: Koordinatensystem, x von −3,5 bis 3,5, y von 0 bis 2; der Graph von "
          "p berührt die x-Achse im Ursprung (Tiefpunkt) und steigt nach beiden Seiten bis etwa (±3; 1,7), dort Hochpunkte")
row("2017MerhoehtBAnalysisWTR3", "a", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Nullstellen einer Funktionenschar mit Fallunterscheidung ermitteln", typ_neben="",
    stichwoerter="−x^2 · (x^2 − 6k) = 0|k <= 0: nur x = 0|k > 0: x = 0 und x = ±√(6k)|eine bzw. drei Nullstellen",
    voraussetzungen="x^2 ausklammern|Wurzel nur aus nicht negativen Zahlen|Fallunterscheidung nach dem Vorzeichen von k",
    format="Rechnung", operator="Bestimmen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FS,
    gesucht="Anzahl der Nullstellen von f_k in Abhängigkeit von k",
    verfahren="f_k(x) = −x^2 · (x^2 − 6k) = 0; x^2 = 6k hat für k > 0 zwei Lösungen, für k < 0 keine, für k = 0 fällt sie mit x = 0 zusammen",
    schritte="3", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="f_k(x) = 0 ⇔ −x^2 · (x^2 − 6k) = 0; damit hat f_k für k <= 0 genau eine Nullstelle, für k > 0 genau drei Nullstellen (amtlich)",
    zwischenergebnis="Nullstellen für k > 0: 0, −√(6k), √(6k)", niveau_geschaetzt="III",
    fehlerquelle="für k = 0 drei Nullstellen zählen oder den Fall k < 0 übersehen",
    bemerkung="Standardbezug: K1 II, K2 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung III nach der Grundregel (Verkettung und Fallunterscheidung mit zwei ausgeführten Fällen verschiedenen Ausgangs, Nullfall-Regel erfüllt); amtlich II – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt (Befund zur Nullfall-Regel in der Stapelliste, § 4). Typ wiederverwendet.")
row("2017MerhoehtBAnalysisWTR3", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Symmetrieart am Term über die Exponenten begründen",
    typ_neben="Vorzeichen der Funktionswerte einer Schar begründen",
    stichwoerter="nur gerade Exponenten, achsensymmetrisch|k <= 0: −x^4 <= 0 und 6kx^2 <= 0|Graph nicht oberhalb der x-Achse",
    voraussetzungen="Achsensymmetrie über gerade Exponenten|Vorzeichen von Summanden abschätzen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FS,
    gesucht="Begründung, dass G_k für alle k symmetrisch bezüglich der y-Achse ist und für k <= 0 nicht oberhalb der x-Achse verläuft",
    verfahren="Der Term enthält nur gerade Exponenten; für k <= 0 sind beide Summanden höchstens null",
    schritte="2", zahlenraum="negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Der Term von f_k enthält nur Potenzen von x mit geradem Exponenten; ist k <= 0, so gilt für alle x ∈ IR: −x^4 <= 0, 6kx^2 <= 0, d. h. f_k(x) <= 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Symmetrie nur für einen Wert von k prüfen",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich. Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Beobachtung, auch begründet) – zwei voneinander unabhängige Einzelbeobachtungen, keine Verkettung (wie 2017-ga-B Analysis 1 f). Typ und Nebentyp wiederverwendet.")
row("2017MerhoehtBAnalysisWTR3", "c", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Extrempunkt einer Schar mit Art nach dem Parametervorzeichen bestimmen", typ_neben="",
    stichwoerter="f_k'(x) = −4x^3 + 12kx|x = 0, x = ±√(3k)|f_k''(±√(3k)) = −24k < 0|Hochpunkte (±√(3k); 9k^2)",
    voraussetzungen="Ableitungen mit Parameter|hinreichende Bedingung über f''|Symmetrie für den zweiten Hochpunkt",
    format="Begründung|Rechnung", operator="Weisen Sie nach|Bestimmen Sie", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FS + "; k > 0; zur Kontrolle: Koordinaten eines Hochpunkts (√(3k); 9k^2)",
    gesucht="Nachweis, dass G_k für k > 0 genau zwei Hochpunkte besitzt; Koordinaten dieser Hochpunkte in Abhängigkeit von k",
    verfahren="f_k'(x) = 0 ⇔ x = 0 ∨ x = ±√(3k); f_k''(0) = 12k > 0 (Tiefpunkt), f_k''(±√(3k)) = −24k < 0 (Hochpunkte); Funktionswert 9k^2",
    schritte="4", zahlenraum="Wurzel|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f_k'(x) = −4x^3 + 12kx = 0 ⇔ x = 0 ∨ x = −√(3k) ∨ x = √(3k); f_k''(x) = −12x^2 + 12k, f_k''(0) = 12k > 0, f_k''(±√(3k)) = −24k < 0; f_k(±√(3k)) = 9k^2; Hochpunkte (−√(3k); 9k^2), (√(3k); 9k^2) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Stelle x = 0 als dritten Hochpunkt zählen",
    bemerkung="Standardbezug: K1 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (hier für k > 0 nur die Hochpunkte).")
row("2017MerhoehtBAnalysisWTR3", "d", innen="1", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Anzahl gemeinsamer Punkte einer Schar mit einer waagerechten Geraden über die Höhe der Hochpunkte nach Parameterbereichen angeben", typ_neben="",
    stichwoerter="Hochpunkthöhe 9k^2 gegen y = 4|9k^2 = 4 ⇔ k = 2/3|0 < k < 2/3 keine, k = 2/3 zwei, k > 2/3 vier gemeinsame Punkte",
    voraussetzungen="Verlauf des Graphen aus Symmetrie, Tiefpunkt im Ursprung und zwei Hochpunkten|quadratische Gleichung in k",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FS + "; k > 0; G_k hat die Hochpunkte (±√(3k); 9k^2) und im Ursprung einen Tiefpunkt",
    gesucht="Untersuchung mithilfe der Lage eines der beiden Hochpunkte, wie viele gemeinsame Punkte G_k und die Gerade y = 4 haben, in Abhängigkeit von k",
    verfahren="Hochpunkthöhe 9k^2 mit 4 vergleichen: 9k^2 = 4 ⇔ k = 2/3; liegt der Hochpunkt unter der Geraden, keine Schnittpunkte, auf ihr zwei Berührpunkte, darüber je Hälfte zwei, also vier",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2017MerhoehtBAnalysisWTR3-1c",
    ergebnis="Für k > 0 gilt 9k^2 = 4 ⇔ k = 2/3; damit haben G_k und die Gerade für 0 < k < 2/3 keine, für k = 2/3 genau zwei und für k > 2/3 genau vier gemeinsame Punkte (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="für k > 2/3 nur zwei Schnittpunkte zählen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR3", "e", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter den Graphen über Lage zur x-Achse und Höhe der Hochpunkte zuordnen", typ_neben="",
    stichwoerter="k = −1/2: Graph nicht oberhalb der x-Achse, III|k = 1: Hochpunkthöhe 9, I|k = 1/2: Hochpunkthöhe 9/4, II",
    voraussetzungen="Ergebnisse zu Vorzeichen und Hochpunkten der Schar nutzen",
    format="Kurzantwort|Begründung", operator="Ordnen Sie zu|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=FS_SK, kontext="ohne", textumfang="mittel",
    gegeben=FS + "; die Graphen in Abbildung 1 gehören zu k = −1/2, k = 1/2 und k = 1; für k <= 0 verläuft G_k nicht oberhalb der x-Achse, für k > 0 hat G_k die Hochpunkte (±√(3k); 9k^2)",
    gesucht="Zuordnung der drei Werte von k zu den Graphen mit Begründung",
    verfahren="Nur Graph III verläuft nicht oberhalb der x-Achse: k = −1/2; k = 1 hätte Hochpunkte der Höhe 9, Graph II hat sie nicht: k = 1 zu I, k = 1/2 zu II",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2017MerhoehtBAnalysisWTR3-1b|2017MerhoehtBAnalysisWTR3-1c",
    ergebnis="Da die Graphen I und II teilweise oberhalb der x-Achse verlaufen, gehört k = −1/2 zum Graphen III; da Graph II keinen Hochpunkt mit y-Koordinate 9 hat, gehört k = 1 zum Graphen I, folglich k = 1/2 zum Graphen II (amtlich)",
    zwischenergebnis="k = 1/2: Hochpunkte (±√(3/2); 9/4)", niveau_geschaetzt="II",
    fehlerquelle="den steileren Graphen I dem kleineren k zuordnen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. AB amtlich: II. Amtlich. Neuer Typ: die vorhandenen Zuordnungstypen der Schar nutzen Grenzverhalten, y-Achsenabschnitt oder Spiegelung.")
row("2017MerhoehtBAnalysisWTR3", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral der Differenz aus waagerechter Gerade und Funktion als Flächeninhalt mit einer Skizze deuten", typ_neben="",
    stichwoerter="∫ von 0 bis √(3k) (9k^2 − f_k(x)) dx|y = 9k^2 waagerechte Tangente im Hochpunkt|Fläche zwischen G_k, y-Achse und dieser Geraden im I. Quadranten",
    voraussetzungen="Integral einer Differenz als Fläche zwischen zwei Graphen|Hochpunkt (√(3k); 9k^2)|Skizze anfertigen",
    format="Zeichnen|Begründung", operator="Deuten Sie", antwort="Grafik|Text",
    material="keins", skizze="vom Prüfling anzufertigen: G_k für ein k > 0 mit Hochpunkt (√(3k); 9k^2), die Gerade y = 9k^2 und das schraffierte Flächenstück zwischen y-Achse, Gerade und Graph im I. Quadranten", kontext="ohne", textumfang="kurz",
    gegeben=FS + "; k > 0; Hochpunkt (√(3k); 9k^2); Integral ∫ von 0 bis √(3k) (9k^2 − f_k(x)) dx",
    gesucht="geometrische Deutung des Integrals mithilfe einer geeigneten Skizze",
    verfahren="9k^2 ist die Höhe des Hochpunkts, der Integrand die Differenz zwischen der waagerechten Geraden y = 9k^2 und dem Graphen; das Integral ist der Inhalt der Fläche zwischen Gerade, Graph und y-Achse",
    schritte="2", zahlenraum="Wurzel|Potenz", einheiten="", abhaengig_von="2017MerhoehtBAnalysisWTR3-1c",
    ergebnis="Der Wert des Integrals ist der Inhalt der Fläche, die G_k mit der y-Achse und der Geraden y = 9k^2 im I. Quadranten einschließt (amtlich), Skizze mit schraffierter Fläche im Erwartungshorizont",
    zwischenergebnis="Integralwert 24√3/5 · k^(5/2)", niveau_geschaetzt="II",
    fehlerquelle="die Fläche zwischen Graph und x-Achse schraffieren",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. AB amtlich: II. Amtlich, eigene Rechnung: Integralwert 24√3/5 · k^(5/2). Erste Schätzung: III; korrigiert nach Deutungsliste (b), Ausnahme – die Höhe 9k^2 des Hochpunkts ist in Teilaufgabe c gezeigt; (e) betrifft Stammfunktion und Integralfunktion, nicht die Flächendeutung; es bleibt eine Deutung (Fläche zwischen zwei Graphen), II. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR3", "a", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Graph eines in y-Richtung gestreckten Scharmitglieds begründen und skizzieren", typ_neben="",
    stichwoerter="p(x) = 1/48 · (−x^4 + 18x^2) = 1/48 · f_3(x)|6k = 18, k = 3|Streckung mit 1/48 in y-Richtung",
    voraussetzungen="Koeffizientenvergleich|Faktor vor dem Term als Streckung in y-Richtung",
    format="Kurzantwort", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl|Text",
    material="Koordinatensystem", skizze=GER_SK, kontext="Sport/Trainingsgerät", textumfang="mittel",
    gegeben=GER + "; Schar f_k(x) = −x^4 + 6kx^2; der Graph von p geht durch eine Streckung aus einem der Graphen von f_k hervor",
    gesucht="passender Wert von k und Beschreibung der Streckung",
    verfahren="p(x) = 1/48 · (−x^4 + 18x^2) mit f_k vergleichen: 6k = 18",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="k = 3; Streckung mit dem Faktor 1/48 in y-Richtung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="k = 18 angeben oder die Streckung in x-Richtung beschreiben",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")
row("2017MerhoehtBAnalysisWTR3", "b", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Graph eines in y-Richtung gestreckten Scharmitglieds begründen und skizzieren", typ_neben="",
    stichwoerter="G_3 hat Tiefpunkt im Ursprung und zwei Hochpunkte gleicher Höhe|Streckung mit positivem Faktor erhält Art und Lage der Extremstellen",
    voraussetzungen="Ergebnisse zur Schar f_k übertragen|Streckung in y-Richtung mit positivem Faktor",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GER_SK, kontext="Sport/Trainingsgerät", textumfang="kurz",
    gegeben=GER + "; p = 1/48 · f_3 mit f_3(x) = −x^4 + 18x^2; G_3 hat im Ursprung einen Tiefpunkt und genau zwei Hochpunkte (±3; 81)",
    gesucht="Begründung, dass der Graph von p im Koordinatenursprung einen Tiefpunkt hat und genau zwei Hochpunkte besitzt, die in ihren y-Koordinaten übereinstimmen",
    verfahren="Die Eigenschaften von G_3 bleiben bei der Streckung mit dem positiven Faktor 1/48 in y-Richtung erhalten",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="2017MerhoehtBAnalysisWTR3-2a",
    ergebnis="G_3 hat im Koordinatenursprung einen Tiefpunkt und genau zwei Hochpunkte, die in ihren y-Koordinaten übereinstimmen; da der Graph von p durch eine Streckung mit positivem Faktor in y-Richtung aus G_3 hervorgeht, gilt dies auch für den Graphen von p (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Ableitung von p neu berechnen, ohne die Streckung zu nutzen, und dabei die Art nicht prüfen",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich. Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Beobachtung) – die Eigenschaften stehen aus Aufgabe 1 fest und werden über eine einzige Beobachtung (positiver Streckfaktor) übertragen. Typ wiederverwendet.")
row("2017MerhoehtBAnalysisWTR3", "c", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Höhen an den Rändern einer Profillinie als Funktionswerte berechnen", typ_neben="",
    stichwoerter="Höchste Stelle der Profillinie am Rand|p(3) = 27/16 dm|27/16 · 10 cm + 2 cm ≈ 18,9 cm",
    voraussetzungen="Randhochpunkte (±3; p(3))|dm in cm umrechnen|Brettdicke addieren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GER_SK, kontext="Sport/Trainingsgerät", textumfang="kurz",
    gegeben=GER + "; der Graph von p hat die Hochpunkte (±3; p(3)), dort schließt das Standbrett an",
    gesucht="Höhe des Trainingsgeräts in Zentimetern",
    verfahren="p(3) = 27/16 dm berechnen, in cm umrechnen und die 2 cm des Standbretts addieren",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="dm|cm", abhaengig_von="",
    ergebnis="p(3) = 27/16; 27/16 · 10 cm + 2 cm ≈ 18,9 cm (amtlich)",
    zwischenergebnis="p(3) = 1,6875", niveau_geschaetzt="I",
    fehlerquelle="die Brettdicke vergessen oder dm als cm lesen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (18,875 cm). Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Rechnung) – ein Funktionswert mit Einheitenumrechnung und Addition, keine Verkettung von Verfahren (wie 2017-ga-B Analysis 1 a). Typ wiederverwendet.")
row("2017MerhoehtBAnalysisWTR3", "d", innen="2", seite="2", punkte="7", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Wasservolumen in einer Mulde aus Fläche zwischen Wasserlinie und Graph mal Breite berechnen", typ_neben="",
    stichwoerter="Querschnitt des Unterbaus zwischen y = p(3) und dem Graphen|2 · ∫ von 0 bis 3 (p(3) − p(x)) dx = 5,4 dm^2|Prisma 21600 cm^3 plus Brett 4800 cm^3|0,5 g/cm^3, 13,2 kg",
    voraussetzungen="Fläche zwischen Gerade und Graph als Integral|Symmetrie nutzen|Prismenvolumen|Einheiten dm^2 in cm^2",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GER_SK, kontext="Sport/Trainingsgerät", textumfang="mittel",
    gegeben=GER + "; p(3) = 27/16; Unterbau und Standbrett sind ohne Hohlraum aus Holz; ein Kubikzentimeter des Holzes hat eine Masse von 0,5 g",
    gesucht="Masse des Trainingsgeräts in Kilogramm",
    verfahren="Querschnittsfläche des Unterbaus als Fläche zwischen der Geraden y = p(3) und dem Graphen von p über [−3; 3]; mal Länge 40 cm; Volumen des Bretts 60 · 40 · 2 cm^3 addieren; mit 0,5 g/cm^3 multiplizieren",
    schritte="5", zahlenraum="Bruch|dezimal", einheiten="dm^2|cm^3|g|kg", abhaengig_von="2017MerhoehtBAnalysisWTR3-2c",
    ergebnis="Volumen des Unterbaus: 2 · ∫ von 0 bis 3 (p(3) − p(x)) dx = 2 · [27/16 · x + 1/240 · x^5 − 1/8 · x^3] von 0 bis 3 = 5,4; 5,4 · (10 cm)^2 · 40 cm = 21600 cm^3; Volumen des Standbretts 60 cm · 40 cm · 2 cm = 4800 cm^3; Masse 26400 cm^3 · 0,5 g/cm^3 = 13,2 kg (amtlich)",
    zwischenergebnis="Querschnitt 27/5 dm^2 = 540 cm^2", niveau_geschaetzt="III",
    fehlerquelle="die Fläche unter dem Graphen statt über ihm nehmen oder das Standbrett vergessen",
    bemerkung="Standardbezug: K2 II, K3 III, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (13,2 kg). Typ wiederverwendet: Fläche zwischen waagerechter Gerade und Graph mal Länge, hier ein Holzkörper statt Wasser, dazu Brett und Masse (Umbenennung des Typs als Vorschlag für den Abgleichlauf).")
row("2017MerhoehtBAnalysisWTR3", "e", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente im Ursprung als Gerade durch zwei Punkte nachweisen", typ_neben="",
    stichwoerter="g durch (1; p(1)) und (3; p(3))|p(1) = 17/48|Steigung (27/16 − 17/48)/2 = 2/3|p'(1) = 2/3",
    voraussetzungen="Steigung einer Geraden durch zwei Punkte|Ableitung von p",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Sport/Trainingsgerät", textumfang="kurz",
    gegeben="p(x) = −1/48 · (x^4 − 18x^2); die Gerade g verläuft durch die Punkte (1; p(1)) und (3; p(3))",
    gesucht="Nachweis, dass g die Tangente an den Graphen von p im Punkt (1; p(1)) ist",
    verfahren="Die Steigung von g aus den beiden Punkten mit p'(1) vergleichen; g geht durch den Berührpunkt",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="p(1) = 17/48; (27/16 − 17/48)/2 = 2/3 = p'(1) (amtlich)",
    zwischenergebnis="p'(x) = −1/48 · (4x^3 − 36x)", niveau_geschaetzt="II",
    fehlerquelle="nur zeigen, dass g durch (1; p(1)) geht",
    bemerkung="Standardbezug: K1 II, K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet, hier im Punkt (1; p(1)) statt im Ursprung (Umbenennung des Typs als Vorschlag für den Abgleichlauf).")
row("2017MerhoehtBAnalysisWTR3", "f", innen="2", seite="3", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Steigungswinkel des Graphen in einem Punkt über die Ableitung berechnen", typ_neben="",
    stichwoerter="tan α = 2/3|α ≈ 33,7°",
    voraussetzungen="Steigungswinkel über den Arkustangens",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Sport/Trainingsgerät", textumfang="kurz",
    gegeben="Die Gerade g ist die Tangente an den Graphen von p(x) = −1/48 · (x^4 − 18x^2) im Punkt (1; p(1)) mit der Steigung 2/3",
    gesucht="Größe des Steigungswinkels von g",
    verfahren="α = arctan(2/3)",
    schritte="1", zahlenraum="Bruch|dezimal", einheiten="°", abhaengig_von="2017MerhoehtBAnalysisWTR3-2e",
    ergebnis="tan α = 2/3, d. h. α ≈ 33,7° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den Taschenrechner im Bogenmaß rechnen lassen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (33,69°). Typ wiederverwendet (Tangentensteigung aus e).")
row("2017MerhoehtBAnalysisWTR3", "g", innen="2", seite="3", punkte="2", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Steigungswinkel einer Tangente als größten Kippwinkel im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Gerät rollt auf dem Unterbau|g berührt die Profillinie in (1; p(1)) und geht durch den Rand (3; p(3))|um α geneigt berührt der Rand den Boden",
    voraussetzungen="Boden beim Kippen als Tangente an die Profillinie deuten|Randpunkt des Brettes als Kontaktpunkt",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=GER_SK, kontext="Sport/Trainingsgerät", textumfang="kurz",
    gegeben=GER + "; die Gerade g durch (1; p(1)) und (3; p(3)) ist die Tangente an den Graphen von p im Punkt (1; p(1)), ihr Steigungswinkel ist etwa 33,7°; er hat für das Gerät hinsichtlich dessen Bewegungsfreiheit eine besondere Bedeutung",
    gesucht="Beschreibung dieser Bedeutung",
    verfahren="Wird das Gerät gekippt, liegt der Boden als Tangente an der Profillinie; ist er die Gerade g, berührt der Rand (3; p(3)) den Boden – weiter lässt sich das Gerät nicht neigen",
    schritte="2", zahlenraum="dezimal", einheiten="°", abhaengig_von="2017MerhoehtBAnalysisWTR3-2f",
    ergebnis="Wird das Trainingsgerät in Querrichtung um die Größe des Steigungswinkels geneigt, so hat sein Rand Kontakt zum Boden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="den Winkel als Neigung der Profillinie im Punkt (1; p(1)) ohne Bezug zur Kippbewegung beschreiben",
    bemerkung="Standardbezug: K1 II, K3 III, K6 II. AB amtlich: III. Amtlich. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR3", "h", innen="2", seite="3", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Zwei Parameter einer Exponentialfunktion aus zwei Punktbedingungen über ein lineares Gleichungssystem bestimmen", typ_neben="",
    stichwoerter="q(x) = a − c · e^(−x^2)|q(0) = 0 ⇔ a = c|q(3) = a − c · e^(−9) = 27/16|a = c = 27/(16 · (1 − e^(−9)))",
    voraussetzungen="Punktbedingungen einsetzen|lineares Gleichungssystem in a und c|e^0 = 1",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="Sport/Trainingsgerät", textumfang="mittel",
    gegeben="Die Profillinie soll nun durch q(x) = a − c · e^(−x^2), a, c ∈ IR+, x ∈ [−3; 3] beschrieben werden; der Graph von q soll durch den Ursprung verlaufen, die y-Koordinaten seiner Randpunkte sollen mit denen des Graphen von p(x) = −1/48 · (x^4 − 18x^2) übereinstimmen (p(±3) = 27/16)",
    gesucht="Werte von a und c",
    verfahren="q(0) = a − c = 0 und q(3) = a − c · e^(−9) = 27/16 (wegen der Symmetrie genügt ein Rand); aus a = c folgt a · (1 − e^(−9)) = 27/16",
    schritte="3", zahlenraum="Bruch|Potenz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Mit q(0) = 0 ⇔ a = c und q(3) = a − c · e^(−9) = 27/16 ergibt sich a · (1 − e^(−9)) = 27/16 ⇔ a = 27/(16 · (1 − e^(−9))) = c (amtlich)",
    zwischenergebnis="a = c ≈ 1,6877", niveau_geschaetzt="II",
    fehlerquelle="e^(−0) = 0 setzen und so a = 0 erhalten",
    bemerkung="Standardbezug: K2 II, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (1,6877). Schätzung II (beide Bedingungen wörtlich vorgegeben, (a) greift nicht); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ.")
row("2017MerhoehtBAnalysisWTR3", "i", innen="2", seite="3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Unmöglichkeit waagerechter Tangenten an den Rändern über die Ableitung mit Parametern begründen", typ_neben="",
    stichwoerter="parallel zur x-Achse auslaufen heißt q'(±3) = 0|q'(x) = 2cx · e^(−x^2)|für c > 0 und x = ±3 nicht null",
    voraussetzungen="waagerechte Tangente heißt Ableitung null|Kettenregel für e^(−x^2)|e-Funktion ist nie null",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Sport/Trainingsgerät", textumfang="kurz",
    gegeben="q(x) = a − c · e^(−x^2), a, c ∈ IR+, x ∈ [−3; 3]",
    gesucht="Begründung, dass a und c nicht so gewählt werden können, dass der Graph von q zu seinen Randpunkten hin parallel zur x-Achse ausläuft",
    verfahren="q'(x) = 2cx · e^(−x^2); an x = ±3 ist das Produkt wegen c > 0 und e^(−9) > 0 von null verschieden",
    schritte="2", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="q'(x) = 2cx · e^(−x^2) ≠ 0 für x = −3 und x = 3 (amtlich)",
    zwischenergebnis="q'(3) = 6c · e^(−9)", niveau_geschaetzt="II",
    fehlerquelle="nur einen konkreten Wert von c untersuchen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
# ---- AG/LA (A1) WTR: Wölfe (Aufgabe 1, 17 BE) und Matrizen mit N · u = u (Aufgabe 2, 8 BE)
WOLF = ("Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten "
        "Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr "
        "durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; "
        "Entwicklung von einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (x; 0; 0), (0; 0,7; 0,8)) (Zeilen)")
WOLF2 = ("Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach "
         "Beobachtungsbeginn ändern sich die Umweltbedingungen; die Entwicklung im Zwei-Jahres-Rhythmus beschreibt "
         "v_(n+2) = M · v_n mit M = ((0; 3; 3,75), (0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen); sechs Jahre nach "
         "Beobachtungsbeginn ist v_6 = (600; 173; 165), die Population besteht aus 938 Tieren")
NU = "Betrachtet werden 3x3-Matrizen N und Vektoren u = (u1; u2; u3) mit u ≠ (0; 0; 0), für die N · u = u gilt"
row("2017MerhoehtBAGLAA1WTR", "a", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="W → J mit x|J → R mit 0,7|R → R mit 0,8|R → W mit 3",
    voraussetzungen="Spalte als Ausgangszustand, Zeile als Zielzustand lesen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="lang",
    gegeben=WOLF,
    gesucht="Darstellung der Entwicklung der Population in einem Übergangsdiagramm",
    verfahren="Für jeden von null verschiedenen Eintrag einen Pfeil vom Spalten- zum Zeilenzustand mit dem Eintrag beschriften",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Diagramm mit den Knoten W, J, R: W → J mit x, J → R mit 0,7, R → R (Schleife) mit 0,8, R → W mit 3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauschen (Pfeil R → J mit 0,7)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Diagramm aus der Matrix).")
row("2017MerhoehtBAGLAA1WTR", "b", innen="1", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="x als Anteil der Welpen, die zu Jungtieren werden|Überleben des ersten Lebensjahres",
    voraussetzungen="Eintrag als Übergangsanteil lesen",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="lang",
    gegeben=WOLF,
    gesucht="Bedeutung von x im Sachzusammenhang",
    verfahren="Der Eintrag in Zeile J, Spalte W gibt den Übergang von Welpen zu Jungtieren an",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="x ist der Anteil der Welpen, die innerhalb ihres ersten Lebensjahres zu Jungtieren heranwachsen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="x als Geburtenrate deuten",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet.")
row("2017MerhoehtBAGLAA1WTR", "c", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixparameter aus einer Überlebensrate über zwei Stufen bestimmen", typ_neben="",
    stichwoerter="72 % sterben in den ersten zwei Lebensjahren|28 % werden Rudelführerinnen|0,7 · x = 0,28|x = 0,4",
    voraussetzungen="Gegenanteil bilden|Anteile über zwei Übergänge multiplizieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="lang",
    gegeben=WOLF + "; 72 % der Tiere sterben innerhalb der ersten zwei Lebensjahre",
    gesucht="Wert von x",
    verfahren="28 % überleben die ersten zwei Lebensjahre und werden Rudelführerinnen: x · 0,7 = 0,28",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="28 % der Tiere überleben die ersten beiden Lebensjahre und werden zu Rudelführerinnen; damit 0,7 · x = 0,28 ⇔ x = 0,4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="0,72 statt 0,28 ansetzen oder 0,7 und x addieren",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBAGLAA1WTR", "d", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unbekannte Anzahl aus einer Bedingung an den Folgezustand berechnen", typ_neben="",
    stichwoerter="R_1 = 0,7 · J_0 + 0,8 · R_0|R_0 = 39, R_1 = 55|J_0 = 34",
    voraussetzungen="Zeile des Matrix-Vektor-Produkts|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="lang",
    gegeben=WOLF + "; x = 0,4; zu Beobachtungsbeginn gehören 39 Rudelführerinnen zur Population, ein Jahr später 55",
    gesucht="Anzahl der Jungtiere zu Beobachtungsbeginn",
    verfahren="Dritte Zeile von v_1 = L · v_0: 0,7 · J + 0,8 · 39 = 55",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Da innerhalb des ersten Jahres 70 % der Jungtiere zu Rudelführerinnen heranwachsen und 80 % der Rudelführerinnen überleben: 0,7 · J + 0,8 · 39 = 55 ⇔ J = 34 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die überlebenden Rudelführerinnen nicht berücksichtigen (J = 55/0,7)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")
row("2017MerhoehtBAGLAA1WTR", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Verteilung nach einem Übergang berechnen und einen Anteil angeben", typ_neben="",
    stichwoerter="v_8 = M · v_6|(1138; 330; 314) gerundet",
    voraussetzungen="Matrix-Vektor-Produkt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="lang",
    gegeben=WOLF2,
    gesucht="Anzahl der Welpen, Jungtiere und Rudelführerinnen acht Jahre nach Beobachtungsbeginn",
    verfahren="v_8 = M · v_6 zeilenweise berechnen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="v_8 = M · v_6 = (3 · 173 + 3,75 · 165; 2 · 165; 0,24 · 600 + 0,45 · 173 + 0,56 · 165) ≈ (1138; 330; 314) (amtlich)",
    zwischenergebnis="(1137,75; 330; 314,25)", niveau_geschaetzt="I",
    fehlerquelle="M zweimal anwenden, weil acht Jahre zwei Schritte nach sechs Jahren sind",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet, hier ohne Anteil (nur die Verteilung nach einem Schritt).")
row("2017MerhoehtBAGLAA1WTR", "f", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Jährlichen Wachstumsfaktor aus zwei Zuständen im Abstand mehrerer Schritte nachweisen", typ_neben="",
    stichwoerter="v_10 ≈ (2168; 629; 598), v_12 ≈ (4126; 1195; 1138)|Faktor je Jahr 1,38, über zwei Jahre 1,38^2|1,38^2 · v_10 ≈ v_12",
    voraussetzungen="Faktor über zwei Jahre als Quadrat des Jahresfaktors|komponentenweise vergleichen",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="lang",
    gegeben=WOLF2 + "; v_10 ≈ (2168; 629; 598) und v_12 ≈ (4126; 1195; 1138); aus diesen Vektoren soll ein Faktor ermittelt werden, mit dem die Anzahl jeder Altersgruppe von einem Jahr zum nächsten zunimmt",
    gesucht="rechnerischer Nachweis, dass dieser Faktor für jede der drei Altersgruppen etwa 1,38 beträgt",
    verfahren="1,38^2 · v_10 berechnen und mit v_12 vergleichen (oder die Quotienten der Komponenten und ihre Wurzeln)",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="1,38^2 · (2168; 629; 598) ≈ (4129; 1198; 1139) ≈ v_12 (amtlich)",
    zwischenergebnis="√(4126/2168) ≈ 1,380, √(1195/629) ≈ 1,378, √(1138/598) ≈ 1,379", niveau_geschaetzt="II",
    fehlerquelle="den Quotienten 4126/2168 ≈ 1,90 als Faktor je Jahr angeben",
    bemerkung="Standardbezug: K1 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBAGLAA1WTR", "g", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zeitpunkt für das Unterschreiten eines Anteils der Populationsgröße über einen konstanten Faktor bestimmen", typ_neben="",
    stichwoerter="938 · 1,38^(t − 6) = 45000|t ≈ 18|Gesamtzahl der Tiere etwa 18 Jahre nach Beobachtungsbeginn",
    voraussetzungen="Exponentialgleichung mit dem Logarithmus lösen|938 als Gesamtzahl nach sechs Jahren",
    format="Rechnung|Kurzantwort", operator="Bestimmen Sie|Interpretieren Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="kurz",
    gegeben=WOLF2 + "; die Anzahl jeder Altersgruppe nimmt je Jahr etwa mit dem Faktor 1,38 zu; Gleichung 938 · 1,38^(t − 6) = 45000 mit t ∈ [6; +∞[",
    gesucht="Lösung der Gleichung; Interpretation der Zahl 45000 im Sachzusammenhang unter Verwendung der Lösung",
    verfahren="1,38^(t − 6) = 45000/938, t − 6 = ln(45000/938)/ln(1,38); 45000 ist die Gesamtzahl der Tiere zum Zeitpunkt t",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="2017MerhoehtBAGLAA1WTR-1f",
    ergebnis="938 · 1,38^(t − 6) = 45000 liefert t ≈ 18; die Zahl 45000 gibt die Anzahl der Tiere an, aus denen die Population etwa 18 Jahre nach Beobachtungsbeginn besteht (amtlich)",
    zwischenergebnis="t ≈ 18,02", niveau_geschaetzt="II",
    fehlerquelle="45000 als Zahl der Welpen deuten oder t − 6 als Antwort geben",
    bemerkung="Standardbezug: K1 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (18,02). Typ wiederverwendet: hier Überschreiten einer Anzahl mit vorgegebener Gleichung statt Unterschreiten eines Anteils.")
row("2017MerhoehtBAGLAA1WTR", "h", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Eignung eines Populationsmodells zur langfristigen Beschreibung beurteilen", typ_neben="",
    stichwoerter="ungebremstes Wachstum mit Faktor 1,38|Umweltbedingungen ändern sich|Modell muss nach wenigen Jahren angepasst werden",
    voraussetzungen="Modellannahmen im Sachzusammenhang prüfen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="kurz",
    gegeben=WOLF2 + "; das Modell liefert ein Wachstum aller Altersgruppen mit dem Faktor 1,38 je Jahr",
    gesucht="Beurteilung des verwendeten Modells hinsichtlich seiner Eignung zur langfristigen Beschreibung der Entwicklung der Population",
    verfahren="Unbegrenztes exponentielles Wachstum ist in einem abgeschlossenen Gebiet unrealistisch; die Umweltbedingungen und damit die Übergänge ändern sich",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Das Modell ist zur langfristigen Beschreibung nicht geeignet; es ist davon auszugehen, dass sich die Entwicklung mit den Umweltbedingungen ändert und das Modell im Abstand weniger Jahre angepasst werden muss (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Modell wegen der Rundungen statt wegen des unbegrenzten Wachstums kritisieren",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich. Neuer Typ.")
row("2017MerhoehtBAGLAA1WTR", "a", innen="2", seite="2|3", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Gleichung mit inverser Matrix über die Eigenvektorbeziehung lösen", typ_neben="",
    stichwoerter="(N · N^(−1)) · u = a · u ⇔ u = a · u ⇔ a = 1|N^(−1) · u = N^(−1) · N · u = u|(N + N^(−1)) · u = 2u, a = 2",
    voraussetzungen="N · N^(−1) = E|Distributivgesetz für Matrizen|u ≠ 0",
    format="Begründung|Rechnung", operator="Prüfen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=NU + "; N^(−1) ist die inverse Matrix zu einer der Matrizen N; Gleichungen (N · N^(−1)) · u = a · u und (N + N^(−1)) · u = a · u",
    gesucht="Prüfung für jede der beiden Gleichungen, ob es einen Wert von a ∈ IR gibt, für den sie erfüllt ist",
    verfahren="N · N^(−1) = E liefert u = a · u, also a = 1; aus N · u = u folgt durch Multiplikation mit N^(−1) N^(−1) · u = u, also (N + N^(−1)) · u = 2u und a = 2",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(N · N^(−1)) · u = a · u ⇔ u = a · u ⇔ a = 1; mit (N + N^(−1)) · u = N · u + N^(−1) · u = u + N^(−1) · N · u = 2u ergibt sich (N + N^(−1)) · u = a · u ⇔ a = 2 (amtlich)",
    zwischenergebnis="N^(−1) · u = u", niveau_geschaetzt="III",
    fehlerquelle="N^(−1) konkret berechnen wollen oder a = 0 wegen u = a · u zulassen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. AB amtlich: III. Amtlich. Typ wiederverwendet.")
row("2017MerhoehtBAGLAA1WTR", "b", innen="2", seite="3", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Beziehung zwischen den Komponenten eines Fixvektors über das Gleichungssystem N · u = u nachweisen", typ_neben="",
    stichwoerter="N = ((0; 0; 4), (0,25; 0; 0), (0; 0,4; 0,6))|dritte Zeile 0,4u2 + 0,6u3 = u3|u2 = u3",
    voraussetzungen="Matrix-Vektor-Produkt zeilenweise|lineare Gleichung umformen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=NU + "; N = ((0; 0; 4), (0,25; 0; 0), (0; 0,4; 0,6)) (Zeilen)",
    gesucht="Nachweis, dass für diese Matrix u2 = u3 gilt",
    verfahren="Die dritte Zeile von N · u = u lautet 0,4u2 + 0,6u3 = u3, also 0,4u2 = 0,4u3",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="N · u = u liefert 0,4u2 + 0,6u3 = u3 ⇔ 0,4u2 = 0,4u3 ⇔ u2 = u3 (amtlich)",
    zwischenergebnis="alle Lösungen u = (4u3; u3; u3)", niveau_geschaetzt="II",
    fehlerquelle="die erste Zeile allein betrachten und u1 = 4u3 als Ergebnis angeben",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (u = (4u3; u3; u3)). Schätzung II (ein lineares Gleichungssystem zeilenweise); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ.")
# ---- AG/LA (A2) WTR 1: Spielplatzturm, 25 BE
TURM = ("Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken "
        "und einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten "
        "sind A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze "
        "des Dachs ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m")
TURM_SK = ("schematisches Schrägbild des Turms: vier senkrechte Pfosten mit den unteren Enden A, B, C, D und den oberen "
           "Enden E, F, G, H, oben das Viereck EFGH als Rahmen aus Balken und darüber die Dachpyramide mit Spitze S; "
           "die Kante von H nach unten gestrichelt")
row("2017MerhoehtBAGLAA2WTR1", "a", innen="1", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Unbekannte Höhenkoordinate eines Endpunkts einer senkrechten Strecke aus ihrer Länge bestimmen", typ_neben="",
    stichwoerter="Pfosten 4,50 m lang, oberes Ende in Höhe 4|unteres Ende bei z = −0,5|0,5 m im Untergrund",
    voraussetzungen="senkrechte Strecke: nur die dritte Koordinate ändert sich|Untergrund als x3 = 0",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="mittel",
    gegeben=TURM,
    gesucht="wie tief die Pfosten in den Untergrund hineinreichen",
    verfahren="z = 4 − 4,5 = −0,5; die Pfosten reichen 0,5 m unter die x1x2-Ebene",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Die Pfosten ragen 0,5 m in den Untergrund hinein (amtlich)",
    zwischenergebnis="z = −0,5", niveau_geschaetzt="I",
    fehlerquelle="die Höhe 4 als Tiefe angeben oder 4,5 − 4 als Höhe über dem Boden deuten",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBAGLAA2WTR1", "b", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Vierten Eckpunkt eines Parallelogramms über eine Vektoraddition bestimmen",
    typ_neben="Ebene Figur: Quadrat über gleiche Gegenseitenvektoren, Orthogonalität und gleiche Seitenlängen nachweisen",
    stichwoerter="H = E + FG = (−3; −2; 4)|EF = HG, Parallelogramm|EF ∘ FG = 0 und |EF| = |FG| = √26, Quadrat",
    voraussetzungen="gegenüberliegende Seitenvektoren gleich|Skalarprodukt null heißt senkrecht|Vektorbetrag",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Weisen Sie nach", antwort="Zahl|Text",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="mittel",
    gegeben=TURM,
    gesucht="Koordinaten des Punkts H; Nachweis, dass das Viereck EFGH ein Quadrat ist",
    verfahren="OH = OE + FG; EF = HG zeigt das Parallelogramm, EF ∘ FG = 0 den rechten Winkel und |EF| = |FG| gleiche Seiten",
    schritte="4", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="H(−3; −2; 4); wegen EF = HG ist es ein Parallelogramm, wegen EF ∘ FG = 0 und |EF| = |FG| ein Quadrat (amtlich)",
    zwischenergebnis="EF = (1; 5; 0)|FG = (−5; 1; 0)||EF| = |FG| = √26", niveau_geschaetzt="II",
    fehlerquelle="nur gleiche Seitenlängen zeigen (Raute) oder nur den rechten Winkel (Rechteck)",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Schätzung II (Vektoraddition, Parallelogramm, Orthogonalität und Längen verkettet, wie „Mittelpunkt und Höhe und Fläche“ der Liste); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet (erste Leistung: H), neuer Nebentyp für den Quadratnachweis.")
row("2017MerhoehtBAGLAA2WTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrie einer geraden Pyramide bezüglich einer Koordinatenachse über Grundflächenmittelpunkt und Spitze begründen", typ_neben="",
    stichwoerter="gerade Pyramide mit quadratischer Grundfläche EFGH parallel zur x1x2-Ebene|Mittelpunkt der Grundfläche (0; 0; 4)|Spitze S(0; 0; 5) auf der x3-Achse",
    voraussetzungen="Mittelpunkt eines Quadrats als Diagonalenmitte|gerade Pyramide: Spitze über dem Mittelpunkt",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="kurz",
    gegeben=TURM + "; H(−3; −2; 4); EFGH ist ein Quadrat",
    gesucht="Begründung, dass die Pyramide EFGHS symmetrisch bezüglich der x3-Achse ist",
    verfahren="Der Mittelpunkt der Grundfläche (Mitte von EG) ist (0; 0; 4) und liegt wie S auf der x3-Achse; die Grundfläche ist ein Quadrat parallel zur x1x2-Ebene, die Pyramide gerade",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2017MerhoehtBAGLAA2WTR1-1b",
    ergebnis="Die Pyramide ist gerade und hat eine quadratische Grundfläche, die parallel zur x1x2-Ebene ist; der Mittelpunkt der Grundfläche liegt ebenso auf der x3-Achse wie die Spitze S (amtlich)",
    zwischenergebnis="Mitte von EG (0; 0; 4)", niveau_geschaetzt="II",
    fehlerquelle="nur die Lage von S auf der x3-Achse nennen",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ: der vorhandene Typ begründet die Symmetrie zweier Punkte zu einer Achse, hier die eines Körpers.")
row("2017MerhoehtBAGLAA2WTR1", "d", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="Ebene L durch E, F und S|Spannvektoren EF = (1; 5; 0), ES = (−2; 3; 1)|5x1 − x2 + 13x3 = 65",
    voraussetzungen="Parameterform|Parameter eliminieren oder Vektorprodukt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Spielplatz/Turm", textumfang="kurz",
    gegeben=TURM + "; die Punkte E, F und S liegen in einer Ebene L",
    gesucht="eine Gleichung von L in Koordinatenform",
    verfahren="L: x = OE + r · EF + s · ES; aus x1 = 2 + r − 2s, x2 = −3 + 5r + 3s, x3 = 4 + s die Parameter eliminieren",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="L: x = OE + r · EF + s · ES; das Gleichungssystem x1 = 2 + r − 2s, x2 = −3 + 5r + 3s, x3 = 4 + s liefert L: 5x1 − x2 + 13x3 = 65 (amtlich)",
    zwischenergebnis="EF × ES = (5; −1; 13)", niveau_geschaetzt="II",
    fehlerquelle="die Konstante mit einem Punkt außerhalb der Ebene bestimmen",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Probe mit E, F, S). Typ wiederverwendet.")
row("2017MerhoehtBAGLAA2WTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Länge eines Schattens auf einer Dachfläche über Schnitt von Lichtgerade und Ebene beschreiben", typ_neben="",
    stichwoerter="Stange von S bis T|Lichtgerade durch T mit Richtung v|Schnittpunkt mit der Ebene L|Schattenlänge als Abstand zu S",
    voraussetzungen="Schatten eines Punkts als Schnittpunkt Lichtgerade–Ebene|Abstand zweier Punkte",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="mittel",
    gegeben=TURM + "; die Dachfläche EFS liegt in L: 5x1 − x2 + 13x3 = 65; an der Spitze S ist eine gerade Stange befestigt, deren oberer Endpunkt T ist; das Sonnenlicht fällt in parallelen Geraden mit dem Richtungsvektor v; der Schatten der Stange liegt vollständig auf der Dachfläche EFS",
    gesucht="Beschreibung, wie man die Länge dieses Schattens berechnen kann, wenn die Koordinaten von T und v bekannt sind",
    verfahren="Die Gerade durch T mit Richtung v mit L schneiden; der Schatten reicht von S bis zu diesem Schnittpunkt, seine Länge ist der Abstand der beiden Punkte",
    schritte="2", zahlenraum="ganz", einheiten="m", abhaengig_von="2017MerhoehtBAGLAA2WTR1-1d",
    ergebnis="Man berechnet die Koordinaten des Schnittpunkts der Ebene L und der Geraden, die durch T verläuft und den Richtungsvektor v hat; der Abstand dieses Schnittpunkts vom Punkt S ist die Länge des Schattens in Metern (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Schatten mit der x1x2-Ebene statt mit der Dachebene schneiden",
    bemerkung="Standardbezug: K2 II, K3 II, K6 II. AB amtlich: II. Amtlich. Neuer Typ: die vorhandenen Schattentypen berechnen Schattenpunkte, hier wird der Weg zur Schattenlänge beschrieben.")
row("2017MerhoehtBAGLAA2WTR1", "f", innen="1", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punkt auf einer Geraden mit vorgegebenem Abstand zu einem festen Punkt über eine quadratische Gleichung bestimmen", typ_neben="",
    stichwoerter="Strebe 2,10 m von Höhe 3,50 m am Pfosten zum Balken EF in Höhe 4|I(2; −3; 3,5), J(2 + t; −3 + 5t; 4)|√(t^2 + (5t)^2 + 0,5^2) = 2,1 ⇔ t = 0,4|Verhältnis 2 : 3",
    voraussetzungen="Punkt einer Strecke mit Parameter|Abstand zweier Punkte|Parameter als Teilverhältnis deuten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="lang",
    gegeben=TURM + "; zur Stabilisierung ist ein 2,10 m langer Balken mit einem Ende in 3,50 m Höhe am Pfosten AE befestigt, mit dem anderen Ende am darauf liegenden horizontalen Balken EF; der obere Befestigungspunkt teilt den Balken EF in zwei Abschnitte",
    gesucht="Verhältnis der Längen der beiden Abschnitte",
    verfahren="I(2; −3; 3,5) auf AE; J = OE + t · EF = (2 + t; −3 + 5t; 4) mit 0 <= t <= 1; |IJ| = 2,1 liefert t = 0,4; der Parameter teilt EF im Verhältnis 0,4 : 0,6",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="Für I auf AE und J auf EF gilt I(2; −3; 3,5), J(2 + t; −3 + 5t; 4) auf g: x = OE + t · EF; für 0 <= t <= 1: |IJ| = √(t^2 + (5t)^2 + 0,5^2) = 2,1 ⇔ t = 0,4; damit ergibt sich als Verhältnis 2 : 3 (amtlich)",
    zwischenergebnis="Abschnitte etwa 2,04 m und 3,06 m (|EF| = √26)", niveau_geschaetzt="III",
    fehlerquelle="die Strebe waagerecht annehmen (2,1 m auf EF abtragen) oder das Verhältnis 2,1 : (√26 − 2,1) bilden",
    bemerkung="Standardbezug: K2 III, K3 III, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (t = ±0,4, nur 0,4 im Bereich). Neuer Typ (auch AG/LA (A2) WTR 3 1 g).")
row("2017MerhoehtBAGLAA2WTR1", "g", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkte mit vorgegebenem Abstandsverhältnis zu zwei senkrechten Geraden über innere und äußere Teilung bestimmen", typ_neben="",
    stichwoerter="Fußpunkte der Pfosten A'(2; −3; 0), B'(3; 2; 0)|Abstand zu AE doppelt so groß wie zu BF|P1 = A' + 2/3 · A'B' = (8/3; 1/3; 0)|P2 = A' + 2 · A'B' = (4; 7; 0)",
    voraussetzungen="Abstand zu einer senkrechten Geraden als Abstand in der x1x2-Ebene|Teilpunkte auf der Verbindungsgeraden",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="mittel",
    gegeben=TURM + "; B(3; 2; z); eine vertikale Kletterstange hat den Fußpunkt P in der x1x2-Ebene und soll vom Pfosten AE doppelt so weit entfernt sein wie vom Pfosten BF",
    gesucht="Koordinaten von P für zwei mögliche Positionen der Kletterstange",
    verfahren="In der x1x2-Ebene die Fußpunkte A' und B' der Pfosten nehmen; auf ihrer Verbindungsgeraden den inneren Teilpunkt (2/3 von A' aus) und den äußeren Teilpunkt (doppelte Strecke von A' aus) bestimmen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Mit A'(2; −3; 0) und B'(3; 2; 0): OP1 = OA' + 2/3 · A'B', P1(8/3; 1/3; 0); OP2 = OA' + 2 · A'B', P2(4; 7; 0) (amtlich)",
    zwischenergebnis="|P1A'| = 2√26/3, |P1B'| = √26/3", niveau_geschaetzt="III",
    fehlerquelle="nur den Punkt zwischen den Pfosten angeben oder die Abstände vertauschen",
    bemerkung="Standardbezug: K2 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (alle Lösungen liegen auf einem Kreis, die beiden Teilpunkte genügen). Neuer Typ.")
# ---- AG/LA (A2) WTR 2: Rechteck ABCD und Solarmodule, 25 BE; im Landesheft 2017-be-lk als Aufgabe 2.1 (Heft nicht erfasst)
SOLE = "Viereck ABCD mit A(0; 0; 1), B(2; 6; 1), C(−4; 8; 5) und D(−6; 2; 5) in einem kartesischen Koordinatensystem; der Schnittpunkt der Diagonalen heißt M"
SOLEK = (SOLE + "; Solarmodule auf einem Trägergestell, das an einem vertikal stehenden Metallrohr befestigt ist; die Fläche "
         "der Module ist zu einem bestimmten Zeitpunkt das Rechteck ABCD, das Metallrohr eine Strecke, der Befestigungspunkt "
         "am Gestell M(−2; 4; 3); die x1x2-Ebene ist die Horizontale; 1 LE = 0,8 m; ABCD liegt in E: 3x1 − x2 + 5x3 − 5 = 0")
SOLE_SK = ("Abbildung: geneigtes graues Rechteck mit A links, B unten, C rechts und D oben; auf der Fläche M, von M gestrichelt "
           "senkrecht nach unten durch die Fläche, darunter durchgezogen das senkrechte Rohr")
BELK = "; im Landesheft 2017-be-lk (nicht erfasst) als Aufgabe 2.1 {} wortgleich bis auf die Achsenbezeichnung x-y-Ebene"
row("2017MerhoehtBAGLAA2WTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden", typ_neben="",
    stichwoerter="A und B haben die x3-Koordinate 1|Richtungsvektor (2; 6; 0)|parallel zur x1x2-Ebene",
    voraussetzungen="Parallelität zu einer Koordinatenebene über eine verschwindende Komponente",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SOLE,
    gesucht="Begründung, dass die Gerade AB parallel zur x1x2-Ebene verläuft",
    verfahren="Die x3-Koordinaten von A und B stimmen überein, der Richtungsvektor hat die x3-Komponente 0",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die x3-Koordinaten der Punkte A und B stimmen überein (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="mit dem Normalenvektor einer Ebene statt mit dem Richtungsvektor argumentieren",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich. Schätzung nicht blind: die wortgleiche Teilaufgabe 2017-ga-B AG/LA (A2) WTR 2 1 a stand mit amtlichem Bereich im Muster. Wortgleich mit 2017-ga-B AG/LA (A2) WTR 2 1 a (andere Trägeraufgabe, geteilter Typ, iqb.md § 7)" + BELK.format("a (dort mit b zu 6 BE zusammengefasst)") + ". Typ wiederverwendet.")
row("2017MerhoehtBAGLAA2WTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Parallelogramm als Rechteck über das Skalarprodukt nachweisen",
    typ_neben="Punkt: Mittelpunkt einer Strecke im Raum bestimmen",
    stichwoerter="AB = DC, Parallelogramm|AB ∘ AD = 0, rechter Winkel|M als Mitte der Diagonale AC, M(−2; 4; 3)",
    voraussetzungen="gleiche Gegenseitenvektoren|Skalarprodukt null heißt senkrecht|Mittelpunkt als halbe Summe",
    format="Begründung|Kurzantwort", operator="Weisen Sie nach|Geben Sie an", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SOLE,
    gesucht="Nachweis, dass das Viereck ABCD ein Rechteck ist; Koordinaten von M",
    verfahren="AB = DC = (2; 6; 0) zeigt das Parallelogramm, AB ∘ AD = (2; 6; 0) ∘ (−6; 2; 4) = 0 den rechten Winkel; M als Mitte von AC",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="AB = DC, AB ∘ AD = 0; M(−2; 4; 3) (amtlich)",
    zwischenergebnis="AB = (2; 6; 0)|AD = (−6; 2; 4)", niveau_geschaetzt="II",
    fehlerquelle="nur den rechten Winkel bei A zeigen, ohne das Parallelogramm nachzuweisen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Schätzung II (Parallelogramm, rechter Winkel und Mittelpunkt verkettet); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt" + BELK.format("a") + ". Typ und Nebentyp wiederverwendet.")
row("2017MerhoehtBAGLAA2WTR2", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="Parameterform mit AB und AC|Parameter eliminieren|3x1 − x2 + 5x3 − 5 = 0 (Kontrolle vorgegeben)",
    voraussetzungen="Parameterform einer Ebene|Gleichungssystem lösen oder Vektorprodukt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SOLE + "; das Rechteck ABCD liegt in einer Ebene E; zur Kontrolle 3x1 − x2 + 5x3 − 5 = 0",
    gesucht="eine Gleichung von E in Koordinatenform",
    verfahren="Parameterform mit Stützvektor OA und Spannvektoren AB, AC aufstellen und die Parameter eliminieren (oder Normalenvektor über das Vektorprodukt)",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="E: x = OA + λ · AB + μ · AC, λ, μ ∈ IR; das Gleichungssystem x1 = 2λ − 4μ, x2 = 6λ + 8μ, x3 = 1 + 4μ liefert 3x1 − x2 + 5x3 − 5 = 0 (amtlich)",
    zwischenergebnis="AB × AC = (24; −8; 40) = 8 · (3; −1; 5)", niveau_geschaetzt="II",
    fehlerquelle="beim Eliminieren ein Vorzeichen verlieren",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung nicht blind: die wortgleiche Teilaufgabe 2017-ga-B AG/LA (A2) WTR 2 1 d stand mit amtlichem Bereich im Muster. Wortgleich mit 2017-ga-B AG/LA (A2) WTR 2 1 d (andere Trägeraufgabe, geteilter Typ)" + BELK.format("b") + ". Typ wiederverwendet.")
row("2017MerhoehtBAGLAA2WTR2", "d", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="Neigungswinkel φ der Modulfläche gegen die Horizontale|Normalenvektoren (0; 0; 1) und (3; −1; 5)|φ ≈ 32,3°|Bedingung 30° bis 36° erfüllt",
    voraussetzungen="Neigungswinkel als Winkel der Normalenvektoren|Vergleich mit einem Intervall",
    format="Rechnung", operator="Prüfen Sie", antwort="Zahl|Text",
    material="Skizze", skizze=SOLE_SK, kontext="Technik/Solarmodule", textumfang="mittel",
    gegeben=SOLEK + "; für einen möglichst großen Energieertrag sollte die Größe des Neigungswinkels φ der Modulfläche gegenüber der Horizontalen zwischen 30° und 36° liegen",
    gesucht="Prüfung, ob diese Bedingung erfüllt ist",
    verfahren="Winkel zwischen m = (0; 0; 1) und n = (3; −1; 5) über den Kosinus berechnen und mit 30° und 36° vergleichen",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2017MerhoehtBAGLAA2WTR2-1c",
    ergebnis="Mit m = (0; 0; 1) und n = (3; −1; 5) ergibt sich cos φ = (m ∘ n)/(|m| · |n|), d. h. φ ≈ 32,3°; die Bedingung ist erfüllt (amtlich)",
    zwischenergebnis="cos φ = 5/√35", niveau_geschaetzt="II",
    fehlerquelle="den Winkel zwischen Normalenvektor und Horizontaler (etwa 57,7°) angeben",
    bemerkung="Standardbezug: K3 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (32,31°). Schätzung nicht blind: die gleichlautende Teilaufgabe 2017-ga-B AG/LA (A2) WTR 2 1 e stand mit amtlichem Bereich im Muster. Wortgleich mit 2017-ga-B AG/LA (A2) WTR 2 1 e bis auf das Winkelsymbol φ (andere Trägeraufgabe, geteilter Typ)" + BELK.format("c") + ". Typ wiederverwendet.")
row("2017MerhoehtBAGLAA2WTR2", "e", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Größeren Flächeninhalt des Schattens eines geneigten Rechtecks bei senkrechtem Lichteinfall begründen", typ_neben="",
    stichwoerter="Schattenterm |AB| · |AD|/cos φ · (0,8 m)^2|AB parallel zur x1x2-Ebene, Schattenbreite |AB||cos φ = |AD|/|FG|, Schattenlänge |AD|/cos φ|Faktor (0,8 m)^2 für den Maßstab",
    voraussetzungen="Rechteckfläche|Kosinus im rechtwinkligen Dreieck|Querschnittsskizze mit Lichtstrahlen senkrecht zu AD|Maßstab bei Flächen quadrieren",
    format="Begründung|Zeichnen", operator="Begründen Sie", antwort="Text|Grafik",
    material="Skizze", skizze=SOLE_SK, kontext="Technik/Solarmodule", textumfang="mittel",
    gegeben=SOLEK + "; φ ist der Neigungswinkel der Modulfläche gegen die Horizontale; das Sonnenlicht fällt als parallele Geraden senkrecht auf die Modulfläche und erzeugt auf dem horizontalen Untergrund einen rechteckigen Schatten",
    gesucht="Begründung unter Verwendung einer geeignet beschrifteten Skizze, dass der Flächeninhalt des Schattens mit dem Term |AB| · |AD|/cos φ · (0,8 m)^2 berechnet werden kann",
    verfahren="AB ist parallel zum Boden, also ist |AB| die Breite des Schattenrechtecks; im Querschnitt durch A und D mit den Schattenpunkten F und G ist AD Ankathete zu φ im rechtwinkligen Dreieck mit Hypotenuse FG, also |FG| = |AD|/cos φ; (0,8 m)^2 rechnet Flächeneinheiten in m^2 um",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="m^2", abhaengig_von="2017MerhoehtBAGLAA2WTR2-1a|2017MerhoehtBAGLAA2WTR2-1d",
    ergebnis="Da die Gerade AB parallel zur x1x2-Ebene verläuft, ist |AB| die Breite des Rechtecks, das den Schatten im Modell darstellt; da cos φ = |AD|/|FG| gilt, ist |AD|/cos φ die Länge dieses Rechtecks; durch den Faktor (0,8 m)^2 wird der Maßstab berücksichtigt (amtlich); Skizze: Querschnitt mit A, D, dem Winkel φ bei A, Lichtstrahlen senkrecht zu AD und den Schattenpunkten F, G auf dem Boden",
    zwischenergebnis="|AB| = 2√10, |AD| = 2√14, Schatten etwa 35,8 m^2", niveau_geschaetzt="III",
    fehlerquelle="die Länge des Schattens als |AD| · cos φ (senkrechte Projektion) ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III, K4 II. AB amtlich: III. Amtlich, eigene Rechnung: Schatten 35,84 m^2. Schätzung nicht blind: die gleichartige Teilaufgabe 2017-ga-B AG/LA (A2) WTR 2 1 g (dort nur „größer als ABCD“) stand mit amtlichem Bereich im Muster" + BELK.format("d") + ". Typ wiederverwendet: dieselbe Querschnittsbegründung, hier für den Flächenterm statt für den Vergleich (Umbenennung als Vorschlag für den Abgleichlauf).")
row("2017MerhoehtBAGLAA2WTR2", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Radius der Kreisbahn eines Punkts bei Drehung um eine Achse als Abstand zur Achse über den Lotfußpunkt berechnen", typ_neben="",
    stichwoerter="Drehachse senkrecht durch M(−2; 4; 3)|Lotfußpunkt von A auf die Achse L(−2; 4; 1)|Radius |LA| = 2√5|2√5 · 0,8 m ≈ 3,6 m",
    voraussetzungen="Drehung um eine Achse: Kreis um den Lotfußpunkt|senkrechte Achse: Lotfußpunkt in der Höhe des Punkts|Maßstab",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=SOLE_SK, kontext="Technik/Solarmodule", textumfang="mittel",
    gegeben=SOLEK + "; das Metallrohr lässt sich mit dem Trägergestell um die Längsachse des Rohrs drehen, die Neigung des Gestells bleibt dabei unverändert; betrachtet wird der untere linke Eckpunkt A der Modulfläche",
    gesucht="Radius des Kreises, auf dem sich dieser Eckpunkt bei der Drehung des Metallrohrs bewegt",
    verfahren="Die Drehachse ist die Senkrechte durch M; der Lotfußpunkt von A auf sie ist L(−2; 4; 1); Radius |LA| in LE, mal 0,8 m",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="m", abhaengig_von="2017MerhoehtBAGLAA2WTR2-1b",
    ergebnis="Fußpunkt des Lots von A auf die Strecke, die das Metallrohr darstellt: L(−2; 4; 1); |LA| = 2√5, 2√5 · 0,8 m ≈ 3,6 m (amtlich)",
    zwischenergebnis="LA = (2; −4; 0)", niveau_geschaetzt="III",
    fehlerquelle="den Abstand |MA| statt des Abstands zur Achse nehmen oder den Maßstab vergessen",
    bemerkung="Standardbezug: K2 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (3,58 m). Schätzung III nach Deutungsliste (a): der Radius ist erst als Abstand zur Drehachse zu übersetzen (wie „Abstand zum Spiegelbild“); amtlich II – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt" + BELK.format("e") + ". Neuer Typ.")
row("2017MerhoehtBAGLAA2WTR2", "g", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Gleichen Abstand zweier Punkte von einer Drehachse ohne Rechnung über die Symmetrie begründen", typ_neben="",
    stichwoerter="M Diagonalenschnittpunkt, A und B gleich weit von M|AB parallel zur x1x2-Ebene, Rohr senkrecht dazu|gleicher Abstand vom Rohr",
    voraussetzungen="Diagonalen eines Rechtecks halbieren sich und sind gleich lang|Höhe gleich, Achse senkrecht",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Skizze", skizze=SOLE_SK, kontext="Technik/Solarmodule", textumfang="kurz",
    gegeben=SOLEK + "; bei der Drehung um die Längsachse des Rohrs bewegt sich A auf einem Kreis mit dem Radius 2√5 LE",
    gesucht="Begründung ohne Rechnung, dass dieser Radius entsprechend auch für den unteren rechten Eckpunkt B gilt",
    verfahren="A und B sind gleich weit vom Diagonalenschnittpunkt M entfernt; AB liegt waagerecht, das Rohr steht senkrecht; damit haben A und B denselben Abstand von der Rohrachse",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2017MerhoehtBAGLAA2WTR2-1f",
    ergebnis="A und B haben vom Schnittpunkt der Diagonalen des Rechtecks ABCD den gleichen Abstand; die Strecke AB verläuft parallel zur x1x2-Ebene, die Strecke, die das Metallrohr darstellt, senkrecht dazu; damit haben A und B von dieser Strecke den gleichen Abstand (amtlich)",
    zwischenergebnis="Lotfußpunkt von B: (−2; 4; 1), |LB| = 2√5", niveau_geschaetzt="III",
    fehlerquelle="mit der gleichen Länge der Seiten AD und BC statt mit dem Abstand zu M argumentieren",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt" + BELK.format("f") + ". Neuer Typ.")
# ---- AG/LA (A2) WTR 3: Radarstation und Flugzeug, 25 BE
FLUG = ("Eine Radarstation überwacht ein Flugzeug; die x1x2-Ebene ist die Horizontale, 1 LE = 1 km; die Radarstation ist "
        "R(18; 0; −1); um 14.00 Uhr ist das Flugzeug in A(0; 0; 0), danach bewegt es sich entlang einer Geraden durch "
        "B(8; 4; 1), die Position um 14.02 Uhr; ab 14.14 Uhr fliegt es in gleicher Himmelsrichtung horizontal weiter und "
        "bleibt im Modell in der Ebene, die A und B enthält und zur x1x2-Ebene senkrecht steht; von 14.00 bis 14.14 Uhr "
        "fliegt es mit konstanter Geschwindigkeit")
FLUG_SK = ("schematische Abbildung: waagerechte Linie (Horizontale), von ihrem linken Punkt eine flach ansteigende Strecke "
           "(Flugbahn bis 14.14 Uhr) bis zu einem markierten Punkt, von dort ein waagerechter Pfeil nach rechts (Weiterflug)")
ANS = ("; zu einem bestimmten Zeitpunkt zwischen 14.00 und 14.14 Uhr ist die Entfernung des Flugzeugs von der Radarstation am "
       "geringsten; die seit Beobachtungsbeginn vergangene Zeit soll in Minuten bestimmt werden; Ansatz I: d(s) = |(18 − 8s; "
       "−4s; −1 − s)| = √(81s^2 − 286s + 325), d'(s) = 0; Ansatz II: (8; 4; 1) ∘ (18 − 8s; −4s; −1 − s) = 0")
row("2017MerhoehtBAGLAA2WTR3", "a", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen", typ_neben="",
    stichwoerter="Steigungswinkel gegen die Horizontale|sin α = AB ∘ n/(|AB| · |n|) mit n = (0; 0; 1)|α ≈ 6,4°|Position um 14.10 Uhr (40; 20; 5)",
    voraussetzungen="Winkel zwischen Gerade und Ebene über den Sinus|konstante Geschwindigkeit: je 2 Minuten ein Vektor AB",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Luftfahrt/Radar", textumfang="lang",
    gegeben=FLUG,
    gesucht="Größe des Steigungswinkels der Flugbahn gegenüber der Horizontalen bis 14.14 Uhr; Koordinaten des Punkts, der die Position um 14.10 Uhr darstellt",
    verfahren="Winkel zwischen AB = (8; 4; 1) und der x1x2-Ebene über den Normalenvektor (0; 0; 1); 14.10 Uhr ist fünfmal die Zeit von 14.00 bis 14.02 Uhr: OA + 5 · AB",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="Mit n = (0; 0; 1) ergibt sich sin α = (AB ∘ n)/(|AB| · |n|), d. h. α ≈ 6,4°; Koordinaten des Punkts (40; 20; 5) (amtlich)",
    zwischenergebnis="|AB| = 9, sin α = 1/9", niveau_geschaetzt="II",
    fehlerquelle="den Kosinus statt des Sinus verwenden (α ≈ 83,6°)",
    bemerkung="Standardbezug: K3 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (6,38°). Typ wiederverwendet; die Position um 14.10 Uhr ist Teil der Leistung ohne eigenes Etikett.")
row("2017MerhoehtBAGLAA2WTR3", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Positionen bei gleichförmiger Bewegung zu vorgegebenen Zeitpunkten in eine schematische Abbildung einzeichnen", typ_neben="",
    stichwoerter="Strecke von 14.00 bis 14.14 Uhr in sieben gleiche Teile|14.02 Uhr nach 1/7|14.10 Uhr nach 5/7",
    voraussetzungen="konstante Geschwindigkeit heißt gleiche Wegstücke in gleichen Zeiten",
    format="Zeichnen", operator="Zeichnen Sie ein", antwort="Grafik",
    material="Skizze", skizze=FLUG_SK, kontext="Luftfahrt/Radar", textumfang="kurz",
    gegeben=FLUG + "; die Abbildung zeigt schematisch die Flugbahn und die Horizontale",
    gesucht="Positionen des Flugzeugs zu den Zeitpunkten 14.02 Uhr und 14.10 Uhr in der Abbildung",
    verfahren="Die ansteigende Strecke (14.00 bis 14.14 Uhr, 14 Minuten) in sieben gleiche Abschnitte teilen; 14.02 Uhr am Ende des ersten, 14.10 Uhr am Ende des fünften",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Punkt 14.02 Uhr nach 1/7 und Punkt 14.10 Uhr nach 5/7 der ansteigenden Strecke eingezeichnet (amtlich), Zeichnung im Erwartungshorizont",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Punkte auf der Horizontalen statt auf der Flugbahn markieren",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I. AB amtlich: I. Amtlich. Neuer Typ.")
row("2017MerhoehtBAGLAA2WTR3", "c", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Geschwindigkeit entlang einer Kante aus Kantenlänge und Zeit berechnen", typ_neben="",
    stichwoerter="|AB| = 9 km in 2 Minuten|1/2 · 9 · 60 = 270|270 km/h",
    voraussetzungen="Vektorbetrag|Minuten in Stunden umrechnen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Luftfahrt/Radar", textumfang="kurz",
    gegeben=FLUG,
    gesucht="Geschwindigkeit des Flugzeugs bis 14.14 Uhr in km/h",
    verfahren="|AB| = √(64 + 16 + 1) = 9 km in 2 min, also 9/2 km je Minute, mal 60",
    schritte="2", zahlenraum="Wurzel|ganz", einheiten="km|min|km/h", abhaengig_von="",
    ergebnis="1/2 · |AB| · 60 = 270, d. h. die Geschwindigkeit des Flugzeugs beträgt 270 km/h (amtlich)",
    zwischenergebnis="|AB| = 9", niveau_geschaetzt="I",
    fehlerquelle="die 2 Minuten nicht in Stunden umrechnen",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Flugstrecke statt Körperkante).")
row("2017MerhoehtBAGLAA2WTR3", "d", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Gleichung einer senkrechten Strecke mit Parameterbereich im Sachzusammenhang angeben", typ_neben="",
    stichwoerter="x = s · (8; 4; 1)|14.14 Uhr nach sieben Zwei-Minuten-Schritten|0 <= s <= 7",
    voraussetzungen="Gerade durch den Ursprung|Parameterbereich aus der Zeit",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Luftfahrt/Radar", textumfang="kurz",
    gegeben=FLUG,
    gesucht="eine Gleichung der Strecke, die die Flugbahn von 14.00 Uhr bis 14.14 Uhr beschreibt",
    verfahren="Stützvektor OA = 0, Richtungsvektor AB; s zählt Zwei-Minuten-Schritte, bis 14.14 Uhr also bis s = 7",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="x = s · (8; 4; 1); 0 <= s <= 7 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Parameterbereich 0 <= s <= 14 aus den Minuten nehmen",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. AB amtlich: I. Amtlich. Schätzung II (Richtung und Parameterbereich aus der Zeit verkettet); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet: hier keine senkrechte, sondern eine schräge Strecke mit Parameterbereich (Umbenennung als Vorschlag für den Abgleichlauf).")
row("2017MerhoehtBAGLAA2WTR3", "e", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lösungsweg für den Lotfußpunkt eines Punktes auf einer Geraden beschreiben", typ_neben="",
    stichwoerter="Ansatz I: d(s) Entfernung 2s Minuten nach Beginn, Minimum mit d'(s) = 0|Ansatz II: Richtungsvektor und Verbindungsvektor senkrecht, Skalarprodukt null",
    voraussetzungen="Verbindungsvektor und Betrag als Entfernung|Parameter s als Zeit in Zwei-Minuten-Schritten|Minimum über die Ableitung|Lotbedingung",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Luftfahrt/Radar", textumfang="lang",
    gegeben=FLUG + ANS,
    gesucht="Erläuterung jedes der beiden Lösungsansätze",
    verfahren="I: der Vektor ist die Verbindung von der Flugzeugposition zur Station, sein Betrag d(s) die Entfernung 2s Minuten nach Beginn, ihr Minimum über d'(s) = 0; II: bei geringster Entfernung steht der Verbindungsvektor senkrecht auf der Flugrichtung",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2017MerhoehtBAGLAA2WTR3-1d",
    ergebnis="I: Die Entfernung des Flugzeugs von der Radarstation wird in Abhängigkeit von der Zeit durch eine Funktion d beschrieben; d(s) ist die Entfernung 2s Minuten nach Beobachtungsbeginn; die geringste Entfernung lässt sich mit der Differentialrechnung bestimmen. II: Bei geringster Entfernung stehen der Richtungsvektor der Geraden, entlang derer sich das Flugzeug bewegt, und der Verbindungsvektor zwischen Flugzeug und Radarstation zueinander senkrecht; das Skalarprodukt ist dann null (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="s als Zeit in Minuten deuten oder den Ansatz II als Parallelität lesen",
    bemerkung="Standardbezug: K1 III, K3 III, K6 III. AB amtlich: III. Amtlich. Erste Schätzung: II; korrigiert nach Deutungsliste (d) – je Ansatz werden mehrere Deutungen verkettet (Verbindungsvektor, Betrag als Entfernung, s als Zwei-Minuten-Schritt, Ableitung null als Minimum bzw. Skalarprodukt null als Lot); die Ausnahme „einfache Deutung“ war falsch angewandt. Typ wiederverwendet (Lotfußpunkt auf einer Geraden, hier mit zwei Ansätzen).")
row("2017MerhoehtBAGLAA2WTR3", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lotfußpunkt auf einer Geraden über das Skalarprodukt mit dem Richtungsvektor berechnen", typ_neben="",
    stichwoerter="d'(s) = 0 ⇔ 162s − 286 = 0 oder 143 − 81s = 0|s = 143/81|etwa 3,5 Minuten|geringste Entfernung etwa 8,5 km",
    voraussetzungen="Ableitung einer Wurzelfunktion oder Skalarprodukt|Parameter in Minuten umrechnen|Abstand berechnen",
    format="Rechnung", operator="Setzen Sie fort|Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Luftfahrt/Radar", textumfang="mittel",
    gegeben=FLUG + ANS,
    gesucht="Fortsetzung eines der beiden Ansätze bis zur Lösung; geringste Entfernung des Flugzeugs von der Radarstation",
    verfahren="Ansatz II: 8 · (18 − 8s) − 16s − 1 − s = 143 − 81s = 0, s = 143/81 (etwa 3,5 min); d(143/81) berechnen",
    schritte="3", zahlenraum="Bruch|Wurzel|dezimal", einheiten="min|km", abhaengig_von="2017MerhoehtBAGLAA2WTR3-1e",
    ergebnis="d'(s) = 0 ⇔ 162s − 286 = 0 ⇔ s = 143/81, d. h. etwa 3,5 Minuten nach Beobachtungsbeginn ist die Entfernung am geringsten; d(143/81) ≈ 8,5, d. h. die geringste Entfernung beträgt etwa 8,5 km (amtlich)",
    zwischenergebnis="d_min = 2√1469/9 ≈ 8,52", niveau_geschaetzt="II",
    fehlerquelle="s = 143/81 schon als Minutenzahl angeben",
    bemerkung="Standardbezug: K3 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (3,53 min; 8,52 km). Schätzung II (Standardverfahren Lotfußpunkt oder Minimum); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet (Ansatz II; der Erwartungshorizont führt Ansatz I aus).")
row("2017MerhoehtBAGLAA2WTR3", "g", innen="1", seite="2", punkte="7", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punkt auf einer Geraden mit vorgegebenem Abstand zu einem festen Punkt über eine quadratische Gleichung bestimmen", typ_neben="",
    stichwoerter="Position um 14.14 Uhr (56; 28; 7)|Weiterflug x = (56; 28; 7) + u · (8; 4; 0), u > 0|Abstand zu R gleich 70|80u^2 + 832u + 2292 = 4900, u ≈ 2,5|(76; 38; 7) gerundet",
    voraussetzungen="gleiche Himmelsrichtung horizontal heißt Richtung (8; 4; 0)|Abstand zweier Punkte|quadratische Gleichung, positive Lösung wählen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Luftfahrt/Radar", textumfang="mittel",
    gegeben=FLUG + "; ist das Flugzeug mehr als 70 km von der Radarstation entfernt, kann es von dieser nicht mehr erfasst werden",
    gesucht="Koordinaten des Punkts, an dem das Flugzeug nach 14.14 Uhr den Erfassungsbereich der Radarstation verlässt",
    verfahren="Position um 14.14 Uhr 7 · AB = (56; 28; 7); Weiterflug mit Richtung (8; 4; 0); |OP − OR| = 70 ergibt eine quadratische Gleichung in u, positive Lösung einsetzen",
    schritte="4", zahlenraum="dezimal|Wurzel|negativ", einheiten="km", abhaengig_von="2017MerhoehtBAGLAA2WTR3-1d",
    ergebnis="x = (56; 28; 7) + u · (8; 4; 0), u ∈ IR+; |(56 + 8u − 18; 28 + 4u; 7 + 1)| = 70 ⇔ 80u^2 + 832u + 2292 = 4900: u ≈ 2,5; damit x1 ≈ 76, x2 ≈ 38, x3 = 7 (amtlich)",
    zwischenergebnis="u ≈ 2,523|(76,18; 38,09; 7)", niveau_geschaetzt="II",
    fehlerquelle="den Weiterflug mit der ansteigenden Richtung (8; 4; 1) rechnen oder die negative Lösung nehmen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (u ≈ 2,523). Erste Schätzung: III; korrigiert nach Deutungsliste (a), Ausnahme – die Richtung des Weiterflugs ist durch das Modell (horizontal, in der senkrechten Ebene durch A und B) wörtlich vorgegeben; es bleibt eine Verkettung von Standardschritten. Typ wiederverwendet (neu in diesem Stapel mit AG/LA (A2) WTR 1 1 f).")
# ---- Stochastik WTR: Samenkörner für Salatgurken, 25 BE
SAM = ("Ein Großhändler bietet Samenkörner für Salatgurken in zwei Qualitätsstufen an: ein Samenkorn der Stufe A keimt mit "
       "95 %, eines der Stufe B mit 70 %; ein Gemüseanbaubetrieb kauft Samenkörner beider Stufen, davon 65 % der Stufe A, "
       "und sät alle")
row("2017MerhoehtBStochastikWTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="erste Stufe A 65 %, B 35 %|zweite Stufe keimt: A 95 %, B 70 %|Ereignisse A, B, K",
    voraussetzungen="Gegenwahrscheinlichkeiten ergänzen|Ereignisse benennen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Landwirtschaft/Saatgut", textumfang="mittel",
    gegeben=SAM,
    gesucht="beschriftetes Baumdiagramm zum Sachverhalt",
    verfahren="Erste Stufe Qualitätsstufe A (0,65) oder B (0,35), zweite Stufe keimt K oder keimt nicht; Äste 0,95/0,05 und 0,7/0,3",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Baum: A (65 %) mit K (95 %) und K quer (5 %); B (35 %) mit K (70 %) und K quer (30 %); A: Samenkorn gehört zur Stufe A, B: zur Stufe B, K: Samenkorn keimt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Stufen auf der zweiten statt auf der ersten Ebene ansetzen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet.")
row("2017MerhoehtBStochastikWTR", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P_K(B) gegen die Richtung des Baums|0,35 · 0,7/(0,65 · 0,95 + 0,35 · 0,7)|etwa 28,4 %",
    voraussetzungen="Pfadmultiplikation|totale Wahrscheinlichkeit des Keimens",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Landwirtschaft/Saatgut", textumfang="kurz",
    gegeben=SAM + "; ein keimendes Samenkorn wird zufällig ausgewählt",
    gesucht="Wahrscheinlichkeit dafür, dass es sich um ein Samenkorn der Qualitätsstufe B handelt",
    verfahren="P_K(B) = P(B ∩ K)/P(K) mit P(K) als Summe der beiden Keimpfade",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2017MerhoehtBStochastikWTR-1a",
    ergebnis="0,35 · 0,7/(0,65 · 0,95 + 0,35 · 0,7) ≈ 28,4 % (amtlich)",
    zwischenergebnis="P(K) = 0,8625", niveau_geschaetzt="II",
    fehlerquelle="P(B) · P_B(K) = 24,5 % statt der bedingten Wahrscheinlichkeit angeben",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,2841). Typ wiederverwendet.")
row("2017MerhoehtBStochastikWTR", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", typ_neben="",
    stichwoerter="n = 200, p = 0,7|E: genau 140 keimen, etwa 6,1 %|F: mehr als 130 und weniger als 150, P(X <= 149) − P(X <= 130) ≈ 85,8 %",
    voraussetzungen="Grenzen „mehr als“ und „weniger als“ in ganzzahlige Schranken übersetzen|kumulierte Wahrscheinlichkeiten am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Landwirtschaft/Saatgut", textumfang="mittel",
    gegeben=SAM + "; E: von 200 gesäten Samenkörnern der Qualitätsstufe B keimen genau 140; F: von 200 gesäten Samenkörnern der Qualitätsstufe B keimen mehr als 130 und weniger als 150",
    gesucht="Wahrscheinlichkeiten der Ereignisse E und F",
    verfahren="X binomialverteilt mit n = 200 und p = 0,7; P(X = 140) und P(131 <= X <= 149) = P(X <= 149) − P(X <= 130)",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(E) ≈ 6,1 %, P(F) ≈ 0,9305 − 0,0728 ≈ 85,8 % (amtlich)",
    zwischenergebnis="P(X = 140) ≈ 0,0615|P(X <= 149) ≈ 0,9305|P(X <= 130) ≈ 0,0728", niveau_geschaetzt="I",
    fehlerquelle="P(X <= 150) − P(X <= 130) mit den Grenzen 150 und 130 einschließlich rechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,0615; 0,8577). Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Rechnung) – zwei voneinander unabhängige Rechnerwerte, keine Verkettung. Typ wiederverwendet.")
row("2017MerhoehtBStochastikWTR", "d", innen="1", seite="1", punkte="2", afb_amtlich="III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="1 − (Summe i = 0 bis 120 + Summe i = 160 bis 200) der Binomialterme mit n = 200, p = 0,7|Gegenereignis zu höchstens 120 oder mindestens 160|mindestens 121 und höchstens 159 keimen",
    voraussetzungen="Binomialsumme als kumulierte Wahrscheinlichkeit|Gegenereignis einer Vereinigung",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Landwirtschaft/Saatgut", textumfang="kurz",
    gegeben=SAM + "; Term 1 − (Σ von i = 0 bis 120 (200 über i) · 0,7^i · 0,3^(200 − i) + Σ von i = 160 bis 200 (200 über i) · 0,7^i · 0,3^(200 − i))",
    gesucht="Bedeutung des Terms im Sachzusammenhang",
    verfahren="Die erste Summe ist P(X <= 120), die zweite P(X >= 160) für die Zahl X der keimenden unter 200 Samenkörnern der Stufe B; das Gegenereignis ist 121 <= X <= 159",
    schritte="2", zahlenraum="Potenz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Mit dem Term kann die Wahrscheinlichkeit dafür berechnet werden, dass von 200 gesäten Samenkörnern der Qualitätsstufe B mindestens 121 und höchstens 159 keimen (amtlich)",
    zwischenergebnis="Wert etwa 0,9974", niveau_geschaetzt="III",
    fehlerquelle="die Grenzen 120 und 160 in das Ereignis einschließen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 III. AB amtlich: III. Amtlich, eigene Rechnung: 0,9974. Erste Schätzung: II; korrigiert nach Deutungsliste (d) – zwei Binomialsummen als kumulierte Wahrscheinlichkeiten deuten und daraus das Gegenereignis bilden sind verkettete Deutungen; die Ausnahme „einfache Deutung einer Binomialsumme“ (2017-ga-B Stochastik WTR 1 2 d) trifft auf eine einzelne Summe, nicht auf diesen Term. Typ wiederverwendet.")
row("2017MerhoehtBStochastikWTR", "e", innen="1", seite="1|2", punkte="6", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Kosten je Erfolg zweier Varianten über Pfadwahrscheinlichkeiten vergleichen", typ_neben="",
    stichwoerter="fruchttragende Pflanze: A 0,95 · 0,85, B 0,7 · 0,75|Kosten je fruchttragender Pflanze 17 ct/(0,95 · 0,85) ≈ 21 ct, 12 ct/(0,7 · 0,75) ≈ 23 ct|Beschränkung auf B nicht sinnvoll",
    voraussetzungen="Pfadmultiplikation|Kosten je Erfolg als Preis durch Erfolgswahrscheinlichkeit|Ertrag je fruchttragender Pflanze unabhängig von der Stufe",
    format="Rechnung|Begründung", operator="Prüfen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Landwirtschaft/Saatgut", textumfang="lang",
    gegeben=SAM + "; Preis je Samenkorn Stufe A 17 ct, Stufe B 12 ct; aus einem gekeimten Samenkorn wächst eine Gurkenpflanze, die mit 15 % (Stufe A) bzw. 25 % (Stufe B) wegen Wetter oder Schädlingen keine Früchte trägt; die mittlere Zahl geernteter Gurken je fruchttragender Pflanze ist unabhängig von der Stufe; alle Gurken werden zum gleichen Preis verkauft",
    gesucht="Prüfung, ob es für den Anbaubetrieb finanziell sinnvoll wäre, sich auf Samenkörner der Qualitätsstufe B zu beschränken",
    verfahren="Wahrscheinlichkeit einer fruchttragenden Pflanze je Samenkorn: A 0,95 · 0,85, B 0,7 · 0,75; Kosten je fruchttragender Pflanze als Preis durch diese Wahrscheinlichkeit vergleichen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="ct", abhaengig_von="",
    ergebnis="Die Wahrscheinlichkeit, dass aus einem Samenkorn eine fruchttragende Pflanze heranwächst, beträgt für A 0,95 · 0,85, für B 0,7 · 0,75; damit entstehen pro Pflanze für A Kosten von 17 ct/(0,95 · 0,85) ≈ 21 ct, für B 12 ct/(0,7 · 0,75) ≈ 23 ct; es wäre finanziell nicht sinnvoll, sich auf Stufe B zu beschränken (amtlich)",
    zwischenergebnis="0,8075 und 0,525|21,05 ct und 22,86 ct", niveau_geschaetzt="III",
    fehlerquelle="nur die Preise je Samenkorn oder nur die Keimraten vergleichen",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
row("2017MerhoehtBStochastikWTR", "f", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel eines einseitigen Signifikanztests bestimmen", typ_neben="",
    stichwoerter="H0: p <= 0,7, Signifikanzniveau 5 %|n = 100|P(Z > k) <= 0,05|mehr als 77 keimende: H0 ablehnen",
    voraussetzungen="rechtsseitiger Test|kumulierte Binomialwahrscheinlichkeiten am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Landwirtschaft/Saatgut", textumfang="lang",
    gegeben="Der Großhändler behauptet, die Keimwahrscheinlichkeit eines Samenkorns der Stufe B habe sich durch eine Weiterentwicklung auf mehr als 70 % erhöht; die Nullhypothese „Die Wahrscheinlichkeit für das Keimen eines Samenkorns der Qualitätsstufe B ist höchstens 70 %.“ soll auf einem Signifikanzniveau von 5 % getestet werden; dazu werden 100 Samenkörner gesät",
    gesucht="Entscheidungsregel des Tests",
    verfahren="Z Anzahl der keimenden, binomialverteilt mit n = 100, p = 0,7; kleinstes k mit P(Z > k) <= 0,05 suchen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Z: Anzahl der keimenden Samenkörner; P(Z > k) <= 5 % für n = 100, p = 0,7; keimen mehr als 77 Samenkörner, so wird die Nullhypothese abgelehnt (amtlich)",
    zwischenergebnis="P(Z > 76) ≈ 0,0755|P(Z > 77) ≈ 0,0479", niveau_geschaetzt="II",
    fehlerquelle="den Ablehnungsbereich links ansetzen oder k = 76 wählen",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")
row("2017MerhoehtBStochastikWTR", "g", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Konfidenzintervalle",
    typ="Verträglichkeit einer vermuteten Trefferwahrscheinlichkeit über das 1,96σ-Intervall um den Erwartungswert prüfen", typ_neben="",
    stichwoerter="n = 50, p = 0,6, 27 keimen|μ = 30, σ = √12|[μ − 1,96σ; μ + 1,96σ] ≈ [23,2; 36,8]|27 liegt darin, verträglich",
    voraussetzungen="Erwartungswert und Standardabweichung der Binomialverteilung|Intervall nach der vorgegebenen Regel",
    format="Rechnung", operator="Untersuchen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Landwirtschaft/Saatgut", textumfang="lang",
    gegeben="Für eine Qualitätsstufe C wird eine Keimwahrscheinlichkeit von 60 % vermutet; von 50 gesäten Samenkörnern keimen 27; eine Wahrscheinlichkeit von 60 % ist bei einer Sicherheitswahrscheinlichkeit von 95 % mit dieser Anzahl verträglich, wenn 27 im Intervall [μ − 1,96σ; μ + 1,96σ] liegt, μ und σ von B(50; 0,6)",
    gesucht="Untersuchung, ob die vermutete Wahrscheinlichkeit von 60 % mit 27 keimenden Samenkörnern verträglich ist",
    verfahren="μ = 50 · 0,6 = 30, σ = √(50 · 0,6 · 0,4) ≈ 3,46; Intervallgrenzen berechnen und 27 einordnen",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="μ = 50 · 0,6, σ = √(50 · 0,6 · 0,4), μ − 1,96σ ≈ 23,2, μ + 1,96σ ≈ 36,8; damit ist die vermutete Wahrscheinlichkeit bei einer Sicherheitswahrscheinlichkeit von 95 % mit der Anzahl der keimenden Samenkörner verträglich (amtlich)",
    zwischenergebnis="σ ≈ 3,464", niveau_geschaetzt="II",
    fehlerquelle="die relative Häufigkeit 0,54 statt der Anzahl 27 mit dem Intervall vergleichen",
    bemerkung="Standardbezug: K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (23,21; 36,79). Neuer Typ.")

NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Nullstellen und Werte: Funktionswert an einer Stelle am Graphen im Sachzusammenhang ablesen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den Funktionswert an einer vorgegebenen Stelle aus einem abgebildeten Graphen ablesen und im Sachzusammenhang mit Einheit angeben.", "2017MerhoehtBAnalysisWTR1-1a"),
    ("Momentane Änderungsrate am Graphen über eine eingezeichnete Tangente bestimmen", "Analysis", "Ableitung und Änderungsrate",
     "In einen abgebildeten Graphen die Tangente an einer Stelle einzeichnen und ihre Steigung über ein Steigungsdreieck als momentane Änderungsrate mit Einheit angeben.", "2017MerhoehtBAnalysisWTR1-1b"),
    ("Zeitpunkt bei gleichbleibender Änderungsrate über den Schnitt der Tangente mit der Zeitachse grafisch bestimmen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Eine ab einem Zeitpunkt gleichbleibende momentane Änderungsrate als Tangente an den Graphen deuten, das Verfahren beschreiben und den Zeitpunkt als Schnittstelle der Tangente mit der Zeitachse ablesen.", "2017MerhoehtBAnalysisWTR1-1c"),
    ("Symmetrie: Termformen für einen abgebildeten Graphen über Symmetrie und Zahl der Wendepunkte ausschließen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Begründen, dass ein abgebildeter Graph zu keiner von mehreren vorgegebenen Termformen gehört, etwa weil eine Form nur gerade Exponenten hat (Achsensymmetrie) oder als Funktion dritten Grades nur einen Wendepunkt besitzt.", "2017MerhoehtBAnalysisWTR1-1e"),
    ("Zeitraum der Abnahme eines Bestands über Nullstellen und Vorzeichen der Änderungsrate berechnen", "Analysis", "Rekonstruktion von Beständen",
     "Die Nullstellen einer als Term gegebenen Änderungsrate berechnen und über das Vorzeichen (Testwert) den Zeitraum bestimmen, in dem der Bestand abnimmt.", "2017MerhoehtBAnalysisWTR1-2b"),
    ("Zeitpunkt mit gleichem Bestand wie zu Beginn über das Integral der Änderungsrate gleich null untersuchen", "Analysis", "Rekonstruktion von Beständen",
     "Die Bedingung „gleicher Bestand wie zu Beginn“ als Integral der Änderungsrate von null bis x gleich null ansetzen, über die Stammfunktion lösen und die Lösungen nach dem Beginn beurteilen.", "2017MerhoehtBAnalysisWTR1-2d"),
    ("Extrempunkt einer trigonometrischen Schar ohne Ableitung über benachbarte Nullstellen bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Ohne Ableitungsfunktion die Extremstelle einer Schar wie c · sin(cx) als Mitte zweier benachbarter Nullstellen bestimmen, das Verfahren beschreiben und die Koordinaten in Abhängigkeit vom Parameter angeben.", "2017MerhoehtBAnalysisWTR1-3c"),
    ("Term einer höheren Ableitung einer Sinusfunktion über die Periodizität der Ableitungen angeben", "Analysis", "Ableitungsregeln",
     "Aus den ersten Ableitungen einer Funktion wie c · sin(cx) die Periode vier der Ableitungsfolge und den Faktor je Ableitung erkennen und einen Term einer hohen Ableitung über den Rest bei Division durch vier angeben.", "2017MerhoehtBAnalysisWTR1-3d"),
    ("Scharparameter aus dem Abstand der Extremstellen berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Extremstellen einer Schar in Abhängigkeit vom Parameter bestimmen und den Parameter so berechnen, dass ihre Differenz einen vorgegebenen Wert hat.", "2017MerhoehtBAnalysisWTR2-1e"),
    ("Parallelität der Wendetangenten einer Schar über eine parameterunabhängige Steigung nachweisen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Ableitungswert einer Schar an ihrer parameterabhängigen Wendestelle berechnen und zeigen, dass er nicht vom Parameter abhängt, sodass alle Wendetangenten parallel sind.", "2017MerhoehtBAnalysisWTR2-1f"),
    ("Graphen einer Scharfunktion und ihrer in y-Richtung verschobenen Fassung zuordnen und Parameter und Verschiebung bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Zwei abgebildete Graphen einer Scharfunktion f_k und von f_k + d über eine gemeinsame Eigenschaft der Schar (etwa Verlauf durch den Ursprung) zuordnen, d aus dem y-Achsenabschnitt und k aus der Lage der Extrempunkte bestimmen.", "2017MerhoehtBAnalysisWTR2-1g"),
    ("Transformation: Streckungen in x- und y-Richtung aus einer Funktionalgleichung f2(x) = a · f1(bx) beschreiben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus einer Beziehung f2(x) = a · f1(bx) beschreiben, wie der Graph von f2 aus dem von f1 hervorgeht: Streckung mit 1/b in x-Richtung und mit a in y-Richtung.", "2017MerhoehtBAnalysisWTR2-1h"),
    ("Extrempunkt einer Integralfunktion ohne Rechnung über den Vorzeichenwechsel des Integranden begründen", "Analysis", "Stammfunktion und Hauptsatz",
     "Ohne Rechnung begründen, dass eine Integralfunktion an einer Stelle einen Extrempunkt hat, weil ihre Ableitung (der Integrand) dort eine Nullstelle mit Vorzeichenwechsel hat, und den Funktionswert über gleiche Grenzen angeben.", "2017MerhoehtBAnalysisWTR2-1i"),
    ("Waagerechte Tangente und Wendepunkt einer Integralfunktion an einer doppelten Nullstelle des Integranden begründen", "Analysis", "Stammfunktion und Hauptsatz",
     "An einer doppelten Nullstelle (Extremstelle) des Integranden zwei Eigenschaften der Integralfunktion angeben und begründen: waagerechte Tangente wegen L' = f = 0 und Wendepunkt wegen des Extremums von L' = f.", "2017MerhoehtBAnalysisWTR2-1j"),
    ("Integralfunktionen mit verschiedenen unteren Grenzen als Verschiebung in y-Richtung begründen", "Analysis", "Stammfunktion und Hauptsatz",
     "Über die Intervalladditivität zeigen, dass sich zwei Integralfunktionen mit verschiedenen unteren Grenzen um das Integral zwischen diesen Grenzen unterscheiden, und aus dessen Vorzeichen am Graphen die Richtung der Verschiebung begründen.", "2017MerhoehtBAnalysisWTR2-1k"),
    ("Nullstellen und Werte: Differenz zweier Funktionswerte als Abstand im Sachzusammenhang deuten", "Analysis", "Funktionsklassen und Eigenschaften",
     "Einen Term wie p(a) − q(a) aus zwei Modellfunktionen als senkrechten Abstand zweier Randkurven an einer Stelle im Sachzusammenhang deuten, etwa als Breite eines Rands.", "2017MerhoehtBAnalysisWTR2-2a"),
    ("Graph der Füllhöhe in Abhängigkeit von der Zeit über die Gefäßform auswählen und begründen", "Analysis", "Ableitung und Änderungsrate",
     "Unter mehreren Graphen der Füllhöhe gegen die Zeit bei konstanter Zuflussrate den passenden auswählen und über die Gefäßform begründen (wächst der Querschnitt nach oben, nimmt die Änderungsrate der Füllhöhe ab).", "2017MerhoehtBAnalysisWTR2-2b"),
    ("Querschnittsfläche eines Rotationskörpers in Abhängigkeit von der Füllhöhe als Term nachweisen", "Analysis", "Rotationsvolumen",
     "Die Füllhöhe in die Koordinate längs der Rotationsachse übersetzen und die Fläche der Flüssigkeitsoberfläche als π · r^2 mit dem Randfunktionswert als Radius nachweisen.", "2017MerhoehtBAnalysisWTR2-2c"),
    ("Masse eines Hohlkörpers aus der Differenz zweier Rotationsvolumina berechnen", "Analysis", "Rotationsvolumen",
     "Das Materialvolumen eines rotationssymmetrischen Hohlkörpers als Rotationsvolumen der Außenkurve minus Rotationsvolumen der Innenkurve (mit eigenen Grenzen) berechnen und mit der Dichte nach Einheitenumrechnung die Masse bestimmen.", "2017MerhoehtBAnalysisWTR2-2e"),
    ("Anzahl gemeinsamer Punkte einer Schar mit einer waagerechten Geraden über die Höhe der Hochpunkte nach Parameterbereichen angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Die parameterabhängige Höhe der Hochpunkte einer Schar mit einer waagerechten Geraden vergleichen und die Anzahl der gemeinsamen Punkte für die Parameterbereiche darunter, gleich und darüber angeben.", "2017MerhoehtBAnalysisWTR3-1d"),
    ("Scharparameter den Graphen über Lage zur x-Achse und Höhe der Hochpunkte zuordnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Abgebildete Graphen einer Schar vorgegebenen Parameterwerten zuordnen, indem Ergebnisse zur Lage unterhalb der x-Achse und zur parameterabhängigen Hochpunkthöhe verwendet werden.", "2017MerhoehtBAnalysisWTR3-1e"),
    ("Integralwert: Integral der Differenz aus waagerechter Gerade und Funktion als Flächeninhalt mit einer Skizze deuten", "Analysis", "Flächeninhalt durch Integration",
     "Ein Integral der Form ∫ (c − f(x)) dx mit c als Höhe eines Hochpunkts geometrisch als Inhalt der Fläche zwischen der Geraden y = c, dem Graphen und einer Achse deuten und in einer Skizze kennzeichnen.", "2017MerhoehtBAnalysisWTR3-1f"),
    ("Steigungswinkel einer Tangente als größten Kippwinkel im Sachzusammenhang deuten", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Steigungswinkel einer Tangente an eine Profillinie, die zugleich durch einen Randpunkt geht, als größten Neigungswinkel deuten, bei dem ein auf der Profillinie kippender Körper mit dem Rand den Boden berührt.", "2017MerhoehtBAnalysisWTR3-2g"),
    ("Zwei Parameter einer Exponentialfunktion aus zwei Punktbedingungen über ein lineares Gleichungssystem bestimmen", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Für eine Modellfunktion wie a − c · e^(−x^2) zwei vorgegebene Punktbedingungen einsetzen und das in a und c lineare Gleichungssystem exakt lösen.", "2017MerhoehtBAnalysisWTR3-2h"),
    ("Unmöglichkeit waagerechter Tangenten an den Rändern über die Ableitung mit Parametern begründen", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Eine Forderung „parallel zur x-Achse auslaufen“ als Ableitung null an den Rändern übersetzen und über den Ableitungsterm mit positiven Parametern zeigen, dass sie für keine Parameterwahl erfüllbar ist.", "2017MerhoehtBAnalysisWTR3-2i"),
    ("Übergangsprozess: Matrixparameter aus einer Überlebensrate über zwei Stufen bestimmen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus einem Anteil, der über zwei aufeinanderfolgende Übergänge überlebt (etwa 28 % in zwei Lebensjahren), mit dem bekannten zweiten Übergangsanteil den unbekannten Matrixeintrag als Quotient bestimmen.", "2017MerhoehtBAGLAA1WTR-1c"),
    ("Übergangsprozess: Jährlichen Wachstumsfaktor aus zwei Zuständen im Abstand mehrerer Schritte nachweisen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus zwei Zustandsvektoren im Abstand von n Jahren nachweisen, dass alle Komponenten mit einem gemeinsamen Faktor je Jahr wachsen, indem der Faktor hoch n mit dem ersten Vektor multipliziert und mit dem zweiten verglichen wird.", "2017MerhoehtBAGLAA1WTR-1f"),
    ("Übergangsprozess: Eignung eines Populationsmodells zur langfristigen Beschreibung beurteilen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Ein Übergangsmodell mit konstantem Wachstum auf seine langfristige Eignung beurteilen, etwa weil sich Umweltbedingungen ändern und unbegrenztes Wachstum unrealistisch ist.", "2017MerhoehtBAGLAA1WTR-1h"),
    ("Matrizenalgebra: Beziehung zwischen den Komponenten eines Fixvektors über das Gleichungssystem N · u = u nachweisen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Für eine gegebene Matrix N aus einer Zeile des Gleichungssystems N · u = u eine Beziehung zwischen den Komponenten eines Fixvektors (etwa u2 = u3) herleiten.", "2017MerhoehtBAGLAA1WTR-2b"),
    ("Punkt: Unbekannte Höhenkoordinate eines Endpunkts einer senkrechten Strecke aus ihrer Länge bestimmen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Bei einer senkrechten Strecke bekannter Länge mit bekanntem oberem Endpunkt die dritte Koordinate des unteren Endpunkts bestimmen und im Sachzusammenhang (etwa als Tiefe im Untergrund) angeben.", "2017MerhoehtBAGLAA2WTR1-1a"),
    ("Ebene Figur: Quadrat über gleiche Gegenseitenvektoren, Orthogonalität und gleiche Seitenlängen nachweisen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Ein Viereck im Raum als Quadrat nachweisen: gleiche gegenüberliegende Seitenvektoren (Parallelogramm), Skalarprodukt benachbarter Seiten null und gleiche Längen benachbarter Seiten.", "2017MerhoehtBAGLAA2WTR1-1b"),
    ("Symmetrie einer geraden Pyramide bezüglich einer Koordinatenachse über Grundflächenmittelpunkt und Spitze begründen", "Analytische Geometrie", "Spiegelung",
     "Begründen, dass eine gerade Pyramide mit quadratischer, zu einer Koordinatenebene paralleler Grundfläche symmetrisch zu einer Koordinatenachse ist, weil Grundflächenmittelpunkt und Spitze auf dieser Achse liegen.", "2017MerhoehtBAGLAA2WTR1-1c"),
    ("Gerade und Ebene: Länge eines Schattens auf einer Dachfläche über Schnitt von Lichtgerade und Ebene beschreiben", "Analytische Geometrie", "Lagebeziehungen",
     "Beschreiben, wie die Länge des Schattens einer Stange auf einer ebenen Fläche berechnet wird: Gerade durch den Endpunkt in Lichtrichtung mit der Ebene schneiden und den Abstand des Schnittpunkts zum Fußpunkt der Stange bestimmen.", "2017MerhoehtBAGLAA2WTR1-1e"),
    ("Punkt auf einer Geraden mit vorgegebenem Abstand zu einem festen Punkt über eine quadratische Gleichung bestimmen", "Analytische Geometrie", "Geraden",
     "Einen Punkt einer Geraden oder Strecke mit Parameter ansetzen, seinen Abstand zu einem festen Punkt außerhalb gleich einem vorgegebenen Wert setzen und die quadratische Gleichung lösen; die im Sachzusammenhang passende Lösung auswählen.", "2017MerhoehtBAGLAA2WTR1-1f"),
    ("Punkte mit vorgegebenem Abstandsverhältnis zu zwei senkrechten Geraden über innere und äußere Teilung bestimmen", "Analytische Geometrie", "Abstände",
     "Punkte einer Koordinatenebene bestimmen, deren Abstände zu zwei senkrechten Geraden ein vorgegebenes Verhältnis haben, indem die Fußpunkte der Geraden verbunden und innerer und äußerer Teilpunkt der Verbindungsstrecke berechnet werden.", "2017MerhoehtBAGLAA2WTR1-1g"),
    ("Radius der Kreisbahn eines Punkts bei Drehung um eine Achse als Abstand zur Achse über den Lotfußpunkt berechnen", "Analytische Geometrie", "Abstände",
     "Bei einer Drehung um eine Achse den Radius der Kreisbahn eines Punkts als Abstand zur Achse berechnen: Lotfußpunkt auf der Achse bestimmen (bei senkrechter Achse in der Höhe des Punkts) und die Streckenlänge gegebenenfalls maßstäblich umrechnen.", "2017MerhoehtBAGLAA2WTR2-1f"),
    ("Gleichen Abstand zweier Punkte von einer Drehachse ohne Rechnung über die Symmetrie begründen", "Analytische Geometrie", "Abstände",
     "Ohne Rechnung begründen, dass zwei Punkte einer Figur denselben Abstand von einer Drehachse haben, etwa weil sie gleich weit vom Achsenpunkt der Figur entfernt sind und ihre Verbindung senkrecht zur Achse liegt.", "2017MerhoehtBAGLAA2WTR2-1g"),
    ("Punkt: Positionen bei gleichförmiger Bewegung zu vorgegebenen Zeitpunkten in eine schematische Abbildung einzeichnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Bei gleichförmiger Bewegung auf einer Strecke die Positionen zu vorgegebenen Zeitpunkten als Teilpunkte im Verhältnis der Zeiten in eine schematische Abbildung einzeichnen.", "2017MerhoehtBAGLAA2WTR3-1b"),
    ("Kosten je Erfolg zweier Varianten über Pfadwahrscheinlichkeiten vergleichen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Für zwei Varianten die Wahrscheinlichkeit eines Erfolgs als Pfadprodukt berechnen, die Kosten je Erfolg als Stückpreis durch diese Wahrscheinlichkeit bilden und vergleichen, welche Variante wirtschaftlich günstiger ist.", "2017MerhoehtBStochastikWTR-1e"),
    ("Verträglichkeit einer vermuteten Trefferwahrscheinlichkeit über das 1,96σ-Intervall um den Erwartungswert prüfen", "Stochastik", "Konfidenzintervalle",
     "Für eine vermutete Trefferwahrscheinlichkeit Erwartungswert und Standardabweichung der Binomialverteilung berechnen, das Intervall [μ − 1,96σ; μ + 1,96σ] bilden und prüfen, ob die beobachtete Trefferzahl darin liegt (Verträglichkeit bei 95 %).", "2017MerhoehtBStochastikWTR-1g"),
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
