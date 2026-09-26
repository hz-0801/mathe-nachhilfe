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
    "stapel": "2017-ea-B-cas",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dateidublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll. Delta-Stapel: keine Dateidublette, keine Aufgabendublette, kein Abzug.
    "soll": {
        "2017MerhoehtBAnalysisCAS1": 50, "2017MerhoehtBAnalysisCAS2": 50,
        "2017MerhoehtBAGLAA2CAS1": 25, "2017MerhoehtBAGLAA2CAS2": 25,
        "2017MerhoehtBStochastikCAS1": 25, "2017MerhoehtBStochastikCAS2": 25,
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
# Stapel 2017-ea-B, CAS-Zweig – Delta-Stapel zum WTR-Zweig (Auftrag Nacht 2026-09-28, Teil 2 Punkt 2; iqb.md § 7
# „MMS/CAS als Delta“). iqb-quellen.csv führt für keine der sechs CAS-Dateien eine dateidublette_von (Nachlauf
# scanne_teil_b vom 28.09.2026 ohne Abweichung, Ähnlichkeit zu jeder WTR-Datei desselben Sachgebiets höchstens 0,85);
# alle sechs bilden den Stapel: 50 + 50 + 25 + 25 + 25 + 25 = 200 BE. Keine Aufgabendublette (keine ganze nummerierte
# Aufgabe steht wortgleich im WTR-Zweig). Geteilte Teilaufgaben: AG/LA (A2) CAS 1 a, b, c, d, f, g, h = AG/LA (A2) WTR 1
# a, b, c, d, e, f, g (d mit Kontrollangabe und 3 statt 4 BE, g mit 4 statt 5 BE) – Typ geteilt, Felder aus der WTR-Zeile
# übernommen. Landeshefte: AG/LA (A2) CAS 2 ist 2017-bb-ea-cas B3.1 (Zelt) und 2017-be-lk-cas 2.2; 2017-bb-ea B3.1 ist die
# WTR-Fassung des Landes dazu.
# ---- Analysis CAS 1 (Aufgabe 1: Schar x^2 · e^(−ax), 20 BE; Aufgabe 2: Kiellinie eines Schiffs, 30 BE)
EXA = "Für a ∈ IR+ ist die Schar der in IR definierten Funktionen f_a mit f_a(x) = x^2 · e^(−a · x) gegeben; der Graph von f_a heißt G_a"
KIEL = ("Längsschnitt eines Schiffs mit horizontalem Deck; im Koordinatensystem mit Ursprung an der Bugspitze B und "
        "x-Achse entlang der Decklinie beschreibt k(x) = −0,3x^2 · e^(−0,2x) für 0 <= x <= 20 die Kiellinie; 1 LE = 1 m")
KIEL_SK = ("schematischer Längsschnitt des Schiffs: waagerechte Decklinie von der Bugspitze (links) bis zum Heck (rechts), "
           "am Heck eine kurze senkrechte Wand nach unten; die Kiellinie fällt von der Bugspitze steil zum tiefsten Punkt "
           "etwa in der Mitte und steigt flach zum unteren Ende der Heckwand an; zwei waagerechte gestrichelte Linien: "
           "der Boden der Kajüte von der Kiellinie vorn bis zur Heckwand und darunter, kürzer, der Boden des Stauraums nahe "
           "dem tiefsten Punkt; Beschriftungen Bugspitze, Deck, Heck, Kiel, Boden der Kajüte, Boden des Stauraums; keine Maße")
KPUNKTE = ("; E ist der Endpunkt des Kiels am Heck (x = 20), B die Bugspitze, T(10; k(10)) der Tiefpunkt, "
           "P(10 − 5√2; k(10 − 5√2)) ein Wendepunkt des Graphen von k")
row("2017MerhoehtBAnalysisCAS1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben", typ_neben="",
    stichwoerter="Punkt (1; 1/2) auf G_a|e^(−a) = 1/2|a = ln 2",
    voraussetzungen="Punktprobe|Exponentialgleichung durch Logarithmieren lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EXA, gesucht="der Wert von a, für den der Punkt (1; 1/2) auf G_a liegt",
    verfahren="f_a(1) = e^(−a) = 1/2 setzen und logarithmieren",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f_a(1) = 1/2 ⇔ a = ln 2 (amtlich)", zwischenergebnis="e^(−a) = 1/2",
    niveau_geschaetzt="I", fehlerquelle="1^2 übersehen und e^(−a) = 1 ansetzen oder das Vorzeichen beim Logarithmieren verlieren",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBAnalysisCAS1", "b", innen="1", seite="1", punkte="7", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Extrempunkte einer Schar mit Art in Abhängigkeit vom Parameter bestimmen", typ_neben="",
    stichwoerter="f_a'(x) = 0 bei x = 0 und x = 2/a|Tiefpunkt (0; 0), Hochpunkt (2/a; 4/(e^2a^2))|Hochpunkt im ersten Quadranten|mit wachsendem a nach links und nach unten",
    voraussetzungen="Produkt- und Kettenregel|Extremstellen über erste und zweite Ableitung|Vorzeichen von Termen mit a > 0",
    format="Rechnung|Begründung", operator="Bestimmen Sie|Begründen Sie|beschreiben Sie", antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=EXA + "; zur Kontrolle: Extremstellen x1 = 0, x2 = 2/a",
    gesucht="Koordinaten und Art der Extrempunkte von G_a in Abhängigkeit von a; Begründung, dass der Hochpunkt für jedes a im ersten Quadranten liegt; Beschreibung, wie sich seine Lage mit a ändert",
    verfahren="f_a'(x) = x · e^(−ax) · (2 − ax) = 0 liefert x = 0 und x = 2/a; f_a''(0) > 0, f_a''(2/a) < 0; Koordinaten einsetzen; beide Koordinaten des Hochpunkts sind für a > 0 positiv und fallen mit wachsendem a",
    schritte="4", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Tiefpunkt (0; 0), Hochpunkt (2/a; 4/(e^2a^2)); der Hochpunkt liegt im ersten Quadranten, da 2/a > 0 und 4/(e^2a^2) > 0; mit zunehmendem a bewegt er sich in negative x-Richtung und in negative y-Richtung (amtlich)",
    zwischenergebnis="f_a'(x) = (2x − ax^2) · e^(−ax)|f_a''(0) = 2 > 0|f_a''(2/a) = −2e^(−2) < 0",
    niveau_geschaetzt="II", fehlerquelle="den Tiefpunkt (0; 0) übersehen oder die Lageänderung nur für die x-Koordinate beschreiben",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Schätzung II (Ableitung bilden und Gleichung lösen ist nach der Liste eine Verkettung, dazu Quadrant und Lageänderung); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: die vorhandenen Scharextremtypen unterscheiden die Art nach dem Parametervorzeichen oder berechnen zusätzlich einen Parameter. CAS-Anteil: Ableitungen und Lösung von f_a' = 0 mit dem Rechner möglich, Ansatz eigen.")
row("2017MerhoehtBAnalysisCAS1", "c", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Lage der Extrempunkte einer Schar auf einer gegebenen Kurve durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="Kurve y = x^2/e^2|Tiefpunkt: 0^2/e^2 = 0|Hochpunkt: (2/a)^2/e^2 = 4/(e^2a^2)",
    voraussetzungen="Koordinaten mit Parameter in eine Gleichung einsetzen|Termumformung",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EXA + "; Tiefpunkt (0; 0) und Hochpunkt (2/a; 4/(e^2a^2)) von G_a",
    gesucht="Nachweis, dass die Extrempunkte von G_a für alle a auf dem Graphen der Funktion mit y = x^2/e^2 liegen",
    verfahren="Die x-Koordinaten beider Extrempunkte in x^2/e^2 einsetzen und mit der y-Koordinate vergleichen",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2017MerhoehtBAnalysisCAS1-1b",
    ergebnis="Wegen 0^2/e^2 = 0 und (2/a)^2/e^2 = 4/(e^2a^2) liegen für jeden Wert von a Tiefpunkt und Hochpunkt auf dem gegebenen Graphen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II", fehlerquelle="nur den Hochpunkt prüfen oder den Parameter vor dem Einsetzen festlegen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ: die vorhandenen Ortskurventypen bestimmen die Kurve durch Elimination, hier wird eine gegebene Kurve durch Einsetzen bestätigt (auch Analysis CAS 2 1 e). CAS-Anteil: keiner.")
row("2017MerhoehtBAnalysisCAS1", "d", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Parameter für den größten Flächeninhalt über die Ableitung bestimmen",
    typ_neben="Flächeninhaltsterm eines Dreiecks unter dem Graphen begründen",
    stichwoerter="Dreieck A(0; 0), B(b; 0), C(b; f_0,2(b))|A(b) = 1/2 · b · f_0,2(b)|Maximum bei b = 15|3375/(2e^3) ≈ 84,0",
    voraussetzungen="Dreiecksfläche mit Grundseite und Höhe|Ableitung eines Produkts mit e-Funktion|Maximum über Ableitung",
    format="Rechnung", operator="Bestimmen Sie|geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f_0,2(x) = x^2 · e^(−0,2x) mit Graph G_0,2; für b ∈ IR+ die Punkte A(0; 0), B(b; 0) und C mit der x-Koordinate b auf G_0,2",
    gesucht="der Wert von b, für den der Flächeninhalt des Dreiecks ABC maximal ist, und der zugehörige Flächeninhalt",
    verfahren="Rechter Winkel bei B: A(b) = 1/2 · b · f_0,2(b) = 1/2 · b^3 · e^(−0,2b); A'(b) = 0 für b > 0 liefert b = 15 (Vorzeichenwechsel von + nach −); A(15) berechnen",
    schritte="4", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="A(b) = 1/2 · b · f_0,2(b) nimmt für b = 15 den größten Wert an; der größte Wert ist 3375/(2e^3) (amtlich)",
    zwischenergebnis="A'(b) = (3b^2/2 − b^3/10) · e^(−0,2b)|A(15) ≈ 84,0",
    niveau_geschaetzt="II", fehlerquelle="die Höhe b statt f_0,2(b) nehmen oder den Faktor 1/2 vergessen",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (84,02). Typ und Nebentyp wiederverwendet (Teil A 2020). CAS-Anteil: Ableitung und Nullstelle mit dem Rechner, Zielfunktion eigen.")
row("2017MerhoehtBAnalysisCAS1", "e", innen="1", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Uneigentliche Integrale",
    typ="Beschränktheit eines Flächeninhalts mit variabler Grenze über den Integralterm nachweisen", typ_neben="",
    stichwoerter="Fläche zwischen G_0,2, x-Achse und x = p|∫ von 0 bis p f_0,2(x) dx = 250 − 5(p^2 + 10p + 50) · e^(−p/5)|abgezogener Term positiv|kleiner als 250 für alle p",
    voraussetzungen="Integral mit variabler oberer Grenze|f_0,2(x) >= 0|Vorzeichen eines Produkts",
    format="Rechnung|Begründung", operator="Berechnen Sie|Zeigen Sie", antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=EXA + "; G_a, die x-Achse und die Gerade x = p mit p ∈ IR+ schließen ein Flächenstück ein; a = 0,2",
    gesucht="die Größe dieses Flächenstücks für a = 0,2 (als Term in p); Nachweis, dass der Inhalt auch für beliebig große p kleiner als 250 ist",
    verfahren="Wegen f_0,2(x) >= 0 ist der Inhalt ∫ von 0 bis p f_0,2(x) dx = 250 − 5 · (p^2 + 10p + 50) · e^(−p/5); da p^2 + 10p + 50 > 0 und e^(−p/5) > 0, wird von 250 stets eine positive Zahl abgezogen",
    schritte="3", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="∫ von 0 bis p f_0,2(x) dx = 250 − 5 · (p^2 + 10p + 50) · e^(−p/5); da p^2 + 10p + 50 > 0 und e^(−p/5) > 0 für alle p ∈ IR+, ist das Integral kleiner als 250 (amtlich)",
    zwischenergebnis="Grenzwert für p → ∞: 250",
    niveau_geschaetzt="III", fehlerquelle="nur den Grenzwert 250 angeben, ohne zu zeigen, dass er nicht erreicht wird",
    bemerkung="Standardbezug: K1 III, K2 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Stammfunktion mit sympy, Grenzwert 250). Erste Schätzung: II; korrigiert nach Deutungsliste (c): die Schranke für alle p ist ein allgemeiner Nachweis mit Parameter, bei dem eine Beziehung hergeleitet wird (250 minus ein stets positiver Term), nicht das Nachrechnen einer Identität. Neuer Typ. CAS-Anteil: Integral mit variabler Grenze mit dem Rechner, Abschätzung eigen.")
row("2017MerhoehtBAnalysisCAS1", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Abbildung zwischen zwei Graphen angeben", typ_neben="",
    stichwoerter="k(x) = −0,3 · f_0,2(x)|Stauchung mit 0,3 in y-Richtung|Spiegelung an der x-Achse",
    voraussetzungen="Faktor vor dem Funktionsterm als Streckung in y-Richtung|negatives Vorzeichen als Spiegelung",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Skizze", skizze=KIEL_SK, kontext="Schiffbau/Kiellinie", textumfang="kurz",
    gegeben=KIEL + "; k(x) = −0,3 · f_0,2(x) mit f_0,2(x) = x^2 · e^(−0,2x)",
    gesucht="Beschreibung, wie der Graph von k aus dem Graphen von f_0,2 hervorgeht",
    verfahren="Der Faktor 0,3 staucht in y-Richtung, das Minuszeichen spiegelt an der x-Achse",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="Der Graph von k geht aus dem Graphen von f_0,2 durch eine Stauchung mit dem Faktor 0,3 in y-Richtung und eine Spiegelung an der x-Achse hervor (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I", fehlerquelle="die Stauchung als Streckung in x-Richtung beschreiben",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich. Der Erwartungshorizont schreibt „f2“ für f_0,2 (Druckfehler der Quelle). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBAnalysisCAS1", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt eines Produkts aus Polynom und e-Funktion berechnen", typ_neben="",
    stichwoerter="tiefster Punkt des Kiels bei x = 10|k(10) = −30e^(−2) ≈ −4,06|Endpunkt am Heck k(20) ≈ −2,20|Höhendifferenz etwa 1,86 m",
    voraussetzungen="Produkt- und Kettenregel|Extremstelle über k' = 0|Funktionswerte als Höhen deuten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=KIEL_SK, kontext="Schiffbau/Kiellinie", textumfang="kurz",
    gegeben=KIEL, gesucht="Höhendifferenz in Metern zwischen dem tiefsten Punkt des Kiels und dem Endpunkt des Kiels am Heck",
    verfahren="k'(x) = 0 im Inneren liefert x = 10 (Minimum); k(20) − k(10) berechnen",
    schritte="3", zahlenraum="dezimal|negativ|Potenz", einheiten="m", abhaengig_von="",
    ergebnis="Der tiefste Punkt der Kiellinie hat die x-Koordinate 10; k(20) − k(10) ≈ 1,86, d. h. die Höhendifferenz beträgt etwa 1,86 m (amtlich)",
    zwischenergebnis="k(10) ≈ −4,060|k(20) ≈ −2,198",
    niveau_geschaetzt="II", fehlerquelle="den Betrag k(10) als Höhendifferenz angeben und den Endpunkt am Heck vergessen",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (1,862). Typ wiederverwendet (Tiefpunkt statt Hochpunkt, dann Differenz zum Randwert). CAS-Anteil: Ableitung und Werte mit dem Rechner, Ansatz eigen.")
row("2017MerhoehtBAnalysisCAS1", "c", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Maximalen Neigungswinkel über die Wendestelle berechnen und mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="größter Neigungswinkel an der Wendestelle zwischen Bug und Tiefpunkt|k''(x) = 0 ⇔ x = 10 − 5√2|tan α = k'(10 − 5√2)|etwa 34,7°",
    voraussetzungen="steilste Stelle als Wendestelle|Steigungswinkel über tan α = Steigung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=KIEL_SK, kontext="Schiffbau/Kiellinie", textumfang="kurz",
    gegeben=KIEL + "; der Kiel hat in einem Punkt seinen größten Neigungswinkel gegen die Horizontale",
    gesucht="Größe dieses Neigungswinkels",
    verfahren="Nach der Abbildung liegt der Punkt zwischen Bug und tiefstem Punkt; k''(x) = 0 für 0 < x < 10 liefert x = 10 − 5√2; tan α = k'(10 − 5√2)",
    schritte="3", zahlenraum="dezimal|negativ|Wurzel", einheiten="°", abhaengig_von="",
    ergebnis="Für 0 < x < 10: k''(x) = 0 ⇔ x = 10 − 5√2; tan α = k'(10 − 5√2), α ≈ −34,7°; der Neigungswinkel beträgt etwa 34,7° (amtlich)",
    zwischenergebnis="k'(10 − 5√2) ≈ −0,692",
    niveau_geschaetzt="II", fehlerquelle="die zweite Wendestelle 10 + 5√2 nehmen oder den Winkel an der Bugspitze berechnen",
    bemerkung="Standardbezug: K3 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (34,67°). Typ wiederverwendet, hier ohne Vergleich mit einer Schranke. CAS-Anteil: zweite Ableitung und Gleichung mit dem Rechner.")
row("2017MerhoehtBAnalysisCAS1", "d", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Waagerechte Ausdehnung eines Profils in vorgegebener Höhe über die Stellen mit vorgegebenem Funktionswert berechnen", typ_neben="",
    stichwoerter="Boden der Kajüte 2,20 m unter Deck|k(x) = −2,2|x ≈ 4,07 und x ≈ 19,99|Länge etwa 15,9 m",
    voraussetzungen="Tiefe unter Deck als negativer Funktionswert|Gleichung mit dem Rechner lösen|Länge als Differenz der Stellen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=KIEL_SK, kontext="Schiffbau/Kiellinie", textumfang="kurz",
    gegeben=KIEL + "; der horizontal liegende Boden der Kajüte liegt 2,20 m unterhalb des Decks",
    gesucht="Länge des Bodens der Kajüte in Längsrichtung des Schiffs in Metern",
    verfahren="k(x) = −2,2 für 0 <= x <= 20 lösen; die Länge ist die Differenz der beiden Lösungen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Für 0 <= x <= 20 liefert k(x) = −2,2: x ≈ 4,07 sowie x ≈ 19,99; der Boden ist also etwa 15,9 m lang (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II", fehlerquelle="k(x) = 2,2 ansetzen oder nur die vordere Lösung finden, weil die hintere knapp vor dem Heck liegt",
    bemerkung="Standardbezug: K2 II, K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (4,067 und 19,990). Neuer Typ (auch Analysis CAS 2 2 a). CAS-Anteil: Gleichung mit dem Rechner lösen, Ansatz eigen.")
row("2017MerhoehtBAnalysisCAS1", "e", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Gleichung f(t) = f(t − c) für gleiche Werte im Abstand c mit dem Rechner lösen und im Graphen darstellen", typ_neben="",
    stichwoerter="Boden des Stauraums 6 m lang|waagerechte Sehne: k(x) = k(x + 6)|x ≈ 7,30, k(7,30) ≈ −3,7|etwa 1,5 m unter dem Kajütenboden",
    voraussetzungen="waagerechte Strecke der Länge 6 zwischen zwei Graphenpunkten als Gleichung ansetzen|Gleichung mit dem Rechner lösen|Höhen vergleichen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Skizze", skizze=KIEL_SK, kontext="Schiffbau/Kiellinie", textumfang="mittel",
    gegeben=KIEL + "; der Boden der Kajüte liegt 2,20 m unter Deck; der Boden des Stauraums unterhalb der Kajüte hat in Längsrichtung eine Länge von 6 m",
    gesucht="rechnerisch in Metern, wie weit der Boden des Stauraums unterhalb des Bodens der Kajüte liegt",
    verfahren="Die Endpunkte des Stauraumbodens liegen auf gleicher Höhe im Abstand 6: k(x) = k(x + 6) für 0 <= x <= 14 lösen; k(x) mit −2,2 vergleichen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="2017MerhoehtBAnalysisCAS1-2d",
    ergebnis="Für 0 <= x <= 20 liefert k(x) = k(x + 6): x ≈ 7,30; k(7,30) ≈ −3,7; damit liegt der Boden des Stauraums etwa 1,5 m unterhalb des Bodens der Kajüte (amtlich)",
    zwischenergebnis="k(7,30) ≈ −3,71",
    niveau_geschaetzt="III", fehlerquelle="die Länge 6 m von der Mitte des Tiefpunkts aus symmetrisch abtragen, obwohl die Kiellinie nicht symmetrisch ist",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (7,298; −3,712; 1,51). Eichregel: (a) die waagerechte Strecke der Länge 6 erst als Gleichung k(x) = k(x + 6) ansetzen (wie 2017-ga-B Analysis 1 c). Typ wiederverwendet (2026-ea-B-mms, dort als f(t) = f(t − c)); die Höhenlage ist ein Ablesen mehr. CAS-Anteil: Gleichung mit dem Rechner lösen, Ansatz eigen.")
row("2017MerhoehtBAnalysisCAS1", "f", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Länge der Verbindungsstrecke zweier Graphenpunkte als Näherung der Bogenlänge berechnen", typ_neben="",
    stichwoerter="Streckenzug B–P–T–E|Punkte B(0; 0), P(10 − 5√2; k(10 − 5√2)), T(10; k(10)), E(20; k(20))|Summe der drei Streckenlängen ≈ 21,0",
    voraussetzungen="Funktionswerte als Koordinaten|Abstand zweier Punkte mit dem Satz des Pythagoras",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Skizze", skizze=KIEL_SK, kontext="Schiffbau/Kiellinie", textumfang="mittel",
    gegeben=KIEL + KPUNKTE + "; verbindet man B, P, T und E in dieser Reihenfolge durch Strecken, liefert die Summe der Längen einen Näherungswert für die Länge der Kiellinie; zur Kontrolle: 21,0",
    gesucht="dieser Näherungswert",
    verfahren="Die Koordinaten der vier Punkte über k berechnen und die drei Streckenlängen mit dem Satz des Pythagoras addieren",
    schritte="4", zahlenraum="dezimal|negativ|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="√((10 − 5√2)^2 + (k(10 − 5√2))^2) + √((10 − (10 − 5√2))^2 + (k(10) − k(10 − 5√2))^2) + √((20 − 10)^2 + (k(20) − k(10))^2) ≈ 21,0 (amtlich)",
    zwischenergebnis="Streckenlängen etwa 3,57, 7,26 und 10,17",
    niveau_geschaetzt="II", fehlerquelle="nur die waagerechten Abstände addieren (Ergebnis 20)",
    bemerkung="Standardbezug: K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (20,98; der Erwartungshorizont schreibt f für k). Erste Schätzung: I; korrigiert nach der Grundregel der engen Fassung: Funktionswerte als Koordinaten, drei Streckenlängen und ihre Summe sind eine Verkettung von Standardschritten wie „Mittelpunkt und Höhe und Fläche“ (bleibt II), keine einzelne Rechnung. Typ wiederverwendet, hier drei Strecken. CAS-Anteil: Funktionswerte und Wurzeln mit dem Rechner.")
row("2017MerhoehtBAnalysisCAS1", "g", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Verfahren zur beliebig genauen Näherung einer Kurvenlänge über verfeinerte Streckenzüge beschreiben", typ_neben="",
    stichwoerter="Intervall [0; 20] in n gleich große Teile|Graphenpunkte der Teilungsstellen durch Strecken verbinden|Summe der Streckenlängen|n hinreichend groß",
    voraussetzungen="Streckenzug aus Graphenpunkten|Verfeinerung als Grenzprozess",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Skizze", skizze=KIEL_SK, kontext="Schiffbau/Kiellinie", textumfang="kurz",
    gegeben=KIEL + "; Streckenzüge zwischen Punkten auf dem Graphen von k nähern die Länge der Kiellinie an",
    gesucht="Beschreibung, wie man unter Verwendung von Streckenzügen einen beliebig genauen Wert für die Länge der Kiellinie erhalten kann",
    verfahren="Das Intervall in n gleiche Teile teilen, die Graphenpunkte der Teilungsstellen der Reihe nach verbinden, die Streckenlängen addieren und n immer größer wählen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2017MerhoehtBAnalysisCAS1-2f",
    ergebnis="Man teilt das Intervall von x0 = 0 bis xn = 20 durch x1, x2, …, x(n−1) in n gleich große Teile und verbindet die Punkte des Graphen von k mit den x-Koordinaten x0, x1, … und xn durch Strecken; die Summe der Längen stimmt mit der Länge der Kiellinie beliebig genau überein, wenn n hinreichend groß ist (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II", fehlerquelle="nur mehr Punkte nennen, ohne die Verfeinerung gegen null gehender Teilstücke zu fordern",
    bemerkung="Standardbezug: K1 II, K2 III, K6 III. AB amtlich: III. Amtlich. Schätzung II (Beschreiben eines bekannten Verfahrens, kein Eintrag der Deutungsliste); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Thema ersatzweise Funktionsklassen und Eigenschaften (Kurvenlänge hat keine Themenzeile; wie der Näherungstyp aus 2018-ea-B). Neuer Typ. CAS-Anteil: keiner.")
row("2017MerhoehtBAnalysisCAS1", "h", innen="2", seite="2|3", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Kurvenlänge über eine vorgegebene Integralformel berechnen und mit der Länge von Streckenzügen vergleichen", typ_neben="",
    stichwoerter="s = ∫ von a bis b √(1 + (h'(x))^2) dx|Länge der Kiellinie ≈ 21,2 > 21,0|Kiellinie länger als jeder Streckenzug|Strecke kürzer als der Graphenbogen zwischen ihren Endpunkten",
    voraussetzungen="vorgegebene Formel mit der Ableitung auswerten|Integral numerisch berechnen|Strecke als kürzeste Verbindung",
    format="Rechnung|Begründung", operator="Berechnen Sie|Formulieren Sie|Begründen Sie", antwort="Zahl|Text",
    material="Skizze", skizze=KIEL_SK, kontext="Schiffbau/Kiellinie", textumfang="mittel",
    gegeben=KIEL + "; für ein Kurvenstück einer in [a; b] definierten Funktion h gilt für die Länge s = ∫ von a bis b √(1 + (h'(x))^2) dx; Näherung durch den Streckenzug B–P–T–E: 21,0",
    gesucht="Länge der Kiellinie im Modell; allgemeine Aussage zur Länge der Kiellinie im Vergleich zur Länge der Streckenzüge aus Teilaufgabe g mit Begründung",
    verfahren="∫ von 0 bis 20 √(1 + (k'(x))^2) dx mit dem Rechner auswerten; jede Strecke eines Streckenzugs ist kürzer als das Graphenstück zwischen ihren Endpunkten",
    schritte="3", zahlenraum="dezimal", einheiten="m", abhaengig_von="2017MerhoehtBAnalysisCAS1-2f|2017MerhoehtBAnalysisCAS1-2g",
    ergebnis="∫ von 0 bis 20 √(1 + (k'(x))^2) dx ≈ 21,2 > 21,0; die Länge der Kiellinie ist stets größer als die Länge eines der betrachteten Streckenzüge, da jede Strecke des Streckenzugs kürzer ist als das Stück des Graphen von k zwischen ihren beiden Endpunkten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II", fehlerquelle="h statt h' unter die Wurzel setzen oder die Aussage nur für den einen Streckenzug aus f formulieren",
    bemerkung="Standardbezug: K1 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (21,185). Schätzung II (Formel vorgegeben, Begründung über die Strecke als kürzeste Verbindung, kein Eintrag der Deutungsliste); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Thema ersatzweise Stammfunktion und Hauptsatz (Kurvenlänge über ein Integral hat keine Themenzeile). Neuer Typ. CAS-Anteil: Integral numerisch mit dem Rechner, Aussage eigen.")
# ---- Analysis CAS 2 (Gläser-Serie: Aufgabe 1 Schar, 14 BE; Aufgabe 2 Cocktailglas, 16 BE; Aufgabe 3 Sektglas, 13 BE;
# Aufgabe 4 Likörglas aus zwei Parabeln, 7 BE)
GLAS = ("Längsschnitte von fünf rotationssymmetrischen Gläsern einer Serie (Füße und Stiele nicht abgebildet); die "
        "Rotationsachsen liegen auf der y-Achse, 1 LE = 1 cm; jeder Längsschnitt wird durch eine der in IR definierten "
        "Funktionen f_k mit f_k(x) = −3/512 · k · x^4 + 3/32 · k^2 · x^2, k ∈ IR+, beschrieben; f_2 gehört zum Likörglas, "
        "f_3 zum Cocktailglas; das Sektglas ist 12 cm hoch, sein Rand hat einen Durchmesser von 6 cm; die Materialstärke "
        "wird vernachlässigt")
GLAS_SK = ("Abbildung: Koordinatensystem auf Kästchengitter, x von etwa −5 bis 5 (Beschriftung −4, −2, 0, 2, 4), y von 0 bis "
           "12 (Beschriftung 2 bis 12); fünf zur y-Achse symmetrische Graphen durch den Ursprung, mit I bis V beschriftet: "
           "I steigt am steilsten und erreicht y = 12 bei x = ±3 (oberer Bildrand); II endet waagerecht auslaufend in etwa "
           "(±4,9; 10,1); III endet in etwa (±4,6; 7,4), IV in etwa (±4,4; 5,2), V endet waagerecht auslaufend in (±4; 3)")
COCK = ("Cocktailglas der Serie: Längsschnitt f_3(x) = −9/512 · x^4 + 27/32 · x^2 für −2√6 <= x <= 2√6, Rotationsachse "
        "auf der y-Achse, 1 LE = 1 cm")
HALM = ("; im Glas steht ein 20 cm langer gerader Strohhalm (Durchmesser vernachlässigt), dessen unterer Endpunkt im Modell "
        "ein Punkt des Graphen von f_3 ist")
SEKT = ("Sektglas der Serie (12 cm hoch, Randdurchmesser 6 cm, k ≈ 4,06); ein Hochpunkt des Graphen der zugehörigen Funktion "
        "hat die Koordinaten x ≈ 5,7 und y ≈ 25,2, ein Wendepunkt x ≈ 3,3 und y ≈ 14,0")
SEKTP = ("Das Sektglas steht mit vertikaler Rotationsachse und wird mit Flüssigkeit gefüllt; für −3 <= x <= 3 wird sein "
         "Längsschnitt näherungsweise durch p(x) = 4/3 · x^2 beschrieben")
row("2017MerhoehtBAnalysisCAS2", "a", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter den Graphen über Lage zur x-Achse und Höhe der Hochpunkte zuordnen", typ_neben="",
    stichwoerter="Likörglas f_2: Hochpunkt (4; 3), Graph V|Cocktailglas f_3: Hochpunkt (2√6; 81/8), Graph II",
    voraussetzungen="Funktionswerte oder Hochpunkte zweier Scharmitglieder berechnen|Werte am Gitter vergleichen",
    format="Kurzantwort", operator="Ordnen Sie zu", antwort="Text",
    material="Koordinatensystem", skizze=GLAS_SK, kontext="Gläser/Rotationskörper", textumfang="lang",
    gegeben=GLAS, gesucht="Zuordnung der Graphen aus der Abbildung zum Likörglas und zum Cocktailglas",
    verfahren="Charakteristische Werte von f_2 und f_3 berechnen (etwa die Hochpunkte (4; 3) und (4,9; 10,1)) und mit den Graphen vergleichen",
    schritte="2", zahlenraum="Bruch|Wurzel", einheiten="cm", abhaengig_von="",
    ergebnis="Likörglas: Graph V; Cocktailglas: Graph II (amtlich)", zwischenergebnis="f_2(4) = 3|f_3(2√6) = 81/8",
    niveau_geschaetzt="I", fehlerquelle="die Graphen nach der Steilheit bei kleinen x zuordnen, wo sie kaum zu unterscheiden sind",
    bemerkung="Standardbezug: K1 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Beobachtung oder Rechnung): zwei voneinander unabhängige Einzelrechnungen mit Ablesen, keine Verkettung (wie 2017-ea-B-wtr Analysis WTR 3 1 b). Typ wiederverwendet (2017-ea-B-wtr Analysis WTR 3 1 e); hier ohne Lage zur x-Achse, nur über die Hochpunkte – Vorschlag für den Abgleich: Etikett auf „… über die Lage der Hochpunkte zuordnen“ fassen. CAS-Anteil: Funktionswerte mit dem Rechner.")
row("2017MerhoehtBAnalysisCAS2", "b", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben", typ_neben="",
    stichwoerter="Sektglas 12 cm hoch, Randdurchmesser 6 cm|Randpunkt (3; 12)|f_k(3) = 12|k ≈ 4,06",
    voraussetzungen="Höhe und Durchmesser in einen Graphenpunkt übersetzen|quadratische Gleichung in k mit dem Rechner lösen|negative Lösung verwerfen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GLAS_SK, kontext="Gläser/Rotationskörper", textumfang="kurz",
    gegeben=GLAS, gesucht="der zum Sektglas gehörende Wert von k",
    verfahren="Der Rand liegt bei x = 3 in der Höhe 12: f_k(3) = 12 nach k auflösen, k > 0",
    schritte="2", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="f_k(3) = 12 liefert k ≈ 4,06 (amtlich)", zwischenergebnis="27/32 · k^2 − 243/512 · k − 12 = 0|zweite Lösung k ≈ −3,50 entfällt",
    niveau_geschaetzt="II", fehlerquelle="den Durchmesser 6 als x-Wert nehmen (f_k(6) = 12)",
    bemerkung="Standardbezug: K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (4,063). Typ wiederverwendet. CAS-Anteil: Gleichung mit dem Rechner lösen, Punkt eigen.")
row("2017MerhoehtBAnalysisCAS2", "c", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Symmetrieart am Term über die Exponenten begründen", typ_neben="",
    stichwoerter="nur gerade Exponenten 4 und 2|f_k(−x) = f_k(x)|symmetrisch zur y-Achse für jedes k",
    voraussetzungen="Achsensymmetrie bei geraden Exponenten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Gläser/Rotationskörper", textumfang="kurz",
    gegeben="f_k(x) = −3/512 · k · x^4 + 3/32 · k^2 · x^2, x ∈ IR, k ∈ IR+",
    gesucht="Begründung, dass der Graph von f_k für jedes k ∈ IR+ symmetrisch bezüglich der y-Achse ist",
    verfahren="Der Term enthält nur Potenzen von x mit geradem Exponenten, also f_k(−x) = f_k(x)",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Der Term von f_k enthält nur Potenzen von x mit geradem Exponenten (amtlich)", zwischenergebnis="",
    niveau_geschaetzt="I", fehlerquelle="mit einem einzelnen Zahlenbeispiel f_k(−1) = f_k(1) argumentieren",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBAnalysisCAS2", "d", innen="1", seite="2", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Extrempunkte einer Schar mit Art in Abhängigkeit vom Parameter bestimmen", typ_neben="",
    stichwoerter="f_k'(x) = 0 bei x = 0 und x = ±2√(2k)|f_k''(0) > 0: Minimum|f_k''(±2√(2k)) < 0: Maxima",
    voraussetzungen="Ableitung einer Funktion vierten Grades mit Parameter|Ausklammern|zweite Ableitung als Kriterium",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Gläser/Rotationskörper", textumfang="kurz",
    gegeben="f_k(x) = −3/512 · k · x^4 + 3/32 · k^2 · x^2, x ∈ IR, k ∈ IR+; zur Kontrolle: eine Extremstelle ist x = 2√(2k)",
    gesucht="Lage und Art der Extremstellen von f_k",
    verfahren="f_k'(x) = −3/128 · k · x^3 + 3/16 · k^2 · x = 0 liefert x = 0 und x^2 = 8k; Vorzeichen von f_k'' an den drei Stellen prüfen",
    schritte="3", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="f_k'(x) = 0 ⇔ x = −2√(2k) ∨ x = 0 ∨ x = 2√(2k); f_k''(−2√(2k)) < 0, f_k''(0) > 0, f_k''(2√(2k)) < 0; damit hat f_k ein Minimum bei x = 0 sowie Maxima bei x = −2√(2k) und x = 2√(2k) (amtlich)",
    zwischenergebnis="f_k''(0) = 3k^2/16|f_k''(±2√(2k)) = −3k^2/8",
    niveau_geschaetzt="I", fehlerquelle="die negative Extremstelle −2√(2k) vergessen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Analysis CAS 1 1 b). CAS-Anteil: Ableitungen und Gleichung mit dem Rechner.")
row("2017MerhoehtBAnalysisCAS2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Lage der Extrempunkte einer Schar auf einer gegebenen Kurve durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="Kurve y = 3/4096 · x^6|Hochpunkt (2√(2k); 3/8 · k^3)|3/4096 · (2√(2k))^6 = 3/8 · k^3",
    voraussetzungen="Potenz einer Wurzel mit Parameter vereinfachen|y-Koordinate des Hochpunkts berechnen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Gläser/Rotationskörper", textumfang="kurz",
    gegeben="f_k(x) = −3/512 · k · x^4 + 3/32 · k^2 · x^2, k ∈ IR+; die Extremstelle mit positiver x-Koordinate ist x = 2√(2k)",
    gesucht="Nachweis, dass alle Extrempunkte mit positiver x-Koordinate auf dem Graphen der Funktion mit y = 3/4096 · x^6 liegen",
    verfahren="f_k(2√(2k)) = 3/8 · k^3 berechnen und mit 3/4096 · (2√(2k))^6 = 3/4096 · 512 k^3 vergleichen",
    schritte="2", zahlenraum="Bruch|Wurzel|Potenz", einheiten="", abhaengig_von="2017MerhoehtBAnalysisCAS2-1d",
    ergebnis="3/4096 · (2√(2k))^6 = 3/8 · k^3 = f_k(2√(2k)) (amtlich)", zwischenergebnis="(2√(2k))^6 = 512k^3",
    niveau_geschaetzt="II", fehlerquelle="(2√(2k))^6 falsch potenzieren (etwa 64k^3)",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Analysis CAS 1 1 c). CAS-Anteil: Termvereinfachung mit dem Rechner möglich.")
row("2017MerhoehtBAnalysisCAS2", "a", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Waagerechte Ausdehnung eines Profils in vorgegebener Höhe über die Stellen mit vorgegebenem Funktionswert berechnen", typ_neben="",
    stichwoerter="Randhöhe f_3(2√6) = 81/8|Linie 2 cm tiefer bei 65/8|f_3(x) = 65/8 ⇔ x = ±2/3 · √30|Umfang 2π · 2/3 · √30 ≈ 23 cm",
    voraussetzungen="Randhöhe als Funktionswert am Rand|Gleichung vierten Grades im Bereich lösen|Kreisumfang",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Gläser/Rotationskörper", textumfang="kurz",
    gegeben=COCK + "; um das Glas verläuft 2 cm unterhalb des Rands eine eingeschliffene Linie",
    gesucht="Länge dieser Linie",
    verfahren="Randhöhe f_3(2√6) = 81/8, Linie in der Höhe 65/8; f_3(x) = 65/8 im Bereich lösen liefert den Radius 2/3 · √30; Umfang 2πr",
    schritte="3", zahlenraum="Bruch|Wurzel", einheiten="cm", abhaengig_von="",
    ergebnis="f_3(2√6) − 2 = 65/8; für −2√6 <= x <= 2√6 gilt f_3(x) = 65/8 ⇔ x = −2/3 · √30 ∨ x = 2/3 · √30; 2 · 2/3 · √30 · π ≈ 23; die Linie ist etwa 23 cm lang (amtlich)",
    zwischenergebnis="Radius 2/3 · √30 ≈ 3,65|Lösungen ±2/3 · √78 außerhalb des Bereichs",
    niveau_geschaetzt="II", fehlerquelle="die Linie 2 cm unter dem Rand in waagerechter statt senkrechter Richtung abtragen oder die Lösungen außerhalb des Bereichs nehmen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (22,94). Typ wiederverwendet (Analysis CAS 1 2 d), hier mit dem Radius als halber Ausdehnung und dem Kreisumfang. CAS-Anteil: Gleichung mit dem Rechner lösen, Ansatz eigen.")
row("2017MerhoehtBAnalysisCAS2", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Krümmungsverhalten aus der zweiten Ableitung deuten", typ_neben="",
    stichwoerter="konvex heißt linksgekrümmt|f_3''(x) = 0 ⇔ x = ±2√2|unterer Bereich konvex|x ∈ [−2√2; 2√2]",
    voraussetzungen="Linkskrümmung über f'' > 0|Wendestellen berechnen|Bereich über Abbildung oder Testwert zuordnen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GLAS_SK, kontext="Gläser/Rotationskörper", textumfang="mittel",
    gegeben=COCK + "; die Form eines Glases heißt in einem Bereich konvex, wenn der zugehörige Graph dort linksgekrümmt ist",
    gesucht="x-Koordinaten des Bereichs, in dem das Cocktailglas konvex ist",
    verfahren="f_3''(x) = 0 lösen; nach der Abbildung (oder f_3''(0) > 0) ist der untere Bereich zwischen den Wendestellen konvex",
    schritte="2", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="Der Abbildung ist zu entnehmen, dass das Glas in seinem unteren Bereich konvex ist; f_3''(x) = 0 ⇔ x = −2√2 ∨ x = 2√2; damit x ∈ [−2√2; 2√2] (amtlich)",
    zwischenergebnis="f_3''(x) = −27/128 · x^2 + 27/16",
    niveau_geschaetzt="II", fehlerquelle="die Bereiche außerhalb der Wendestellen als konvex angeben",
    bemerkung="Standardbezug: K3 I, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Schätzung: I; korrigiert nach der Liste der engen Fassung: zweite Ableitung bilden, f'' = 0 lösen und den Bereich zuordnen ist eine Verkettung wie „Ableitung bilden und eine Bruchgleichung lösen“ (bleibt II). Typ wiederverwendet. CAS-Anteil: zweite Ableitung und Gleichung mit dem Rechner.")
row("2017MerhoehtBAnalysisCAS2", "c", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente aufstellen und weiteren gemeinsamen Punkt mit dem Graphen berechnen", typ_neben="",
    stichwoerter="Strohhalm berührt das Glas in (4; f_3(4))|Tangente y = 9/4 · x|unterer Endpunkt (0; 0)|Abstand √97|20 − √97 ≈ 10,2 cm",
    voraussetzungen="Berühren als Tangente deuten|Schnittpunkt Tangente–Graph|Abstand zweier Punkte",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Gläser/Strohhalm", textumfang="mittel",
    gegeben=COCK + HALM + "; außerdem berührt der Strohhalm das Glas im Punkt (4; f_3(4))",
    gesucht="Länge des Abschnitts des Strohhalms zwischen dem Berührpunkt und seinem oberen Endpunkt",
    verfahren="Tangente in (4; 9) aufstellen, weiteren Schnittpunkt mit dem Graphen im Glas bestimmen (Ursprung), Abstand zum Berührpunkt von 20 abziehen",
    schritte="4", zahlenraum="Bruch|Wurzel", einheiten="cm", abhaengig_von="",
    ergebnis="Tangente an f_3 in (4; f_3(4)): y = 9/4 · x; Schnittpunkt mit dem Graphen von f_3: (0; 0); Abstand √(4^2 + (f_3(4))^2) = √97; 20 − √97 ≈ 10,2, der Abschnitt ist etwa 10,2 cm lang (amtlich)",
    zwischenergebnis="f_3(4) = 9|f_3'(4) = 9/4|weitere Schnittstelle x = −8 außerhalb des Glases",
    niveau_geschaetzt="II", fehlerquelle="die Schnittstelle x = −8 außerhalb des Glases nehmen oder 20 cm vom Ursprung senkrecht abtragen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (10,15). Erste Schätzung: III; korrigiert nach der Ausnahme zu Deutungsliste (a): „berührt das Glas im Punkt (4; f_3(4))“ gibt die Tangentenbedingung wörtlich vor, die Übersetzung ist nicht zu finden; Tangente, Schnittpunkt und Abstand sind eine Verkettung (II). Typ wiederverwendet. CAS-Anteil: Tangente und Schnitt mit dem Rechner, Modell eigen.")
row("2017MerhoehtBAnalysisCAS2", "d", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt einer Tangente durch einen vorgegebenen Graphenpunkt berechnen", typ_neben="",
    stichwoerter="unterer Endpunkt P(−1; f_3(−1))|Berührpunkt Q(u; f_3(u)) mit u > 0|P liegt auf der Tangente in Q|u = (1 + √142)/3",
    voraussetzungen="allgemeine Tangentengleichung in u|Punktprobe mit P|Gleichung vierten Grades mit dem Rechner lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Gläser/Strohhalm", textumfang="mittel",
    gegeben=COCK + HALM + "; die Lage wird so verändert, dass der untere Endpunkt P(−1; f_3(−1)) ist und der Strohhalm das Glas in Q(u; f_3(u)) mit u > 0 berührt",
    gesucht="der Wert von u",
    verfahren="Tangente in Q: y = f_3'(u) · (x − u) + f_3(u); P einsetzen: f_3(−1) = f_3'(u) · (−1 − u) + f_3(u) nach u > 0 lösen",
    schritte="3", zahlenraum="Bruch|Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="Tangente an f_3 in Q: y = f_3'(u) · (x − u) + f_3(u); da P auf der Tangente liegt, gilt f_3(−1) = f_3'(u) · (−1 − u) + f_3(u) ⇔ u = (1 + √142)/3 (amtlich)",
    zwischenergebnis="u ≈ 4,31; weitere Lösungen u = −1 und u = (1 − √142)/3 entfallen",
    niveau_geschaetzt="II", fehlerquelle="die Tangente in P statt in Q ansetzen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (4,305). Schätzung II (Tangente von einem Punkt an den Graphen als Standardverfahren); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: vorhanden sind Tangenten mit vorgegebener Steigung oder vorgegebenem Berührpunkt. CAS-Anteil: Gleichung mit dem Rechner lösen, Ansatz eigen.")
row("2017MerhoehtBAnalysisCAS2", "a", innen="3", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Verlauf eines Graphen im Sachzusammenhang beschreiben", typ_neben="",
    stichwoerter="Hochpunkt x ≈ 5,7 außerhalb des Glases (Rand bei x = 3)|kein waagerechter Auslauf am Rand|Wendepunkt x ≈ 3,3 außerhalb|Sektglas vollständig konvex, Cocktailglas nicht",
    voraussetzungen="Definitionsbereich des Glases mit Lage von Hoch- und Wendepunkt vergleichen|Krümmung und Tangente im Sachzusammenhang deuten",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=GLAS_SK, kontext="Gläser/Rotationskörper", textumfang="mittel",
    gegeben=SEKT + "; Cocktailglas f_3 für −2√6 <= x <= 2√6 mit Hochpunkten am Rand und Wendestellen ±2√2 im Glas",
    gesucht="zwei wesentliche Unterschiede der Form des Sektglases zur Form des Cocktailglases im Sachzusammenhang unter Berücksichtigung der gegebenen Punkte",
    verfahren="Beim Sektglas liegen Hochpunkt und Wendepunkt außerhalb von −3 <= x <= 3: der Rand läuft nicht waagerecht aus, und das Glas ist durchgehend konvex; das Cocktailglas endet im Hochpunkt und hat einen konkaven oberen Bereich",
    schritte="2", zahlenraum="dezimal", einheiten="cm", abhaengig_von="2017MerhoehtBAnalysisCAS2-2b",
    ergebnis="Den Koordinaten des Hochpunkts lässt sich entnehmen, dass das Sektglas im Gegensatz zum Cocktailglas zum Rand hin nicht senkrecht zur Rotationsachse ausläuft, den Koordinaten des Wendepunkts, dass das Sektglas im Gegensatz zum Cocktailglas vollständig konvex ist (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II", fehlerquelle="Höhe und Breite vergleichen, ohne die gegebenen Punkte auf den Bereich des Glases zu beziehen",
    bemerkung="Standardbezug: K3 II, K4 II, K6 II. AB amtlich: II. Amtlich. Erste Schätzung: III (nach Deutungsliste (b)); korrigiert nach dem Prinzip der engen Fassung: (b) meint eine Symmetrie oder einen Sonderfall, die erst zu erkennen sind; hier nennt die Aufgabe die Punkte ausdrücklich („unter Berücksichtigung der gegebenen Punkte“), der Vergleich mit dem Bereich des Glases ist vorgegeben. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBAnalysisCAS2", "b", innen="3", seite="2|3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Umkehrfunktion",
    typ="Radius der Flüssigkeitsoberfläche in Abhängigkeit von der Füllhöhe über die Umkehrung der Profilfunktion nachweisen", typ_neben="",
    stichwoerter="Füllhöhe h = p(r) = 4/3 · r^2|nach r auflösen, r >= 0|r(h) = 1/2 · √(3h)",
    voraussetzungen="Füllhöhe als Funktionswert, Radius als x-Wert deuten|quadratische Gleichung nach der positiven Lösung auflösen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Gläser/Füllhöhe", textumfang="kurz",
    gegeben=SEKTP, gesucht="Nachweis, dass sich der Radius der Flüssigkeitsoberfläche in Abhängigkeit von der Füllhöhe h durch r(h) = 1/2 · √(3h) bestimmen lässt",
    verfahren="Bei der Füllhöhe h ist der Radius der Oberfläche die positive Stelle r mit p(r) = h: h = 4/3 · r^2 nach r >= 0 auflösen",
    schritte="2", zahlenraum="Bruch|Wurzel", einheiten="cm", abhaengig_von="",
    ergebnis="Für r >= 0 gilt: h(r) = 4/3 · r^2 ⇔ r(h) = 1/2 · √(3h) (amtlich)", zwischenergebnis="r^2 = 3h/4",
    niveau_geschaetzt="II", fehlerquelle="h und r vertauschen und r = 4/3 · h^2 ansetzen",
    bemerkung="Standardbezug: K1 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ: verwandt mit „Querschnittsfläche eines Rotationskörpers in Abhängigkeit von der Füllhöhe als Term nachweisen“ (2017-ea-B-wtr), dort die Fläche und ohne Umkehrung. CAS-Anteil: keiner.")
row("2017MerhoehtBAnalysisCAS2", "c", innen="3", seite="3", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen einer Funktion in ein Koordinatensystem einzeichnen", typ_neben="",
    stichwoerter="Parabel p(x) = 4/3 · x^2 für −3 <= x <= 3|r(h) = 1/2 · √(3h) für h >= 0|zwei eigene Koordinatensysteme",
    voraussetzungen="Wertetabelle|geeignete Achsenskalierung",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze="Im Erwartungshorizont zwei Koordinatensysteme: links die Parabel p mit x von −4 bis 4 und p(x) bis 12, rechts der Wurzelgraph r mit h von 0 bis 12 und r(h) bis 4", kontext="Gläser/Füllhöhe", textumfang="kurz",
    gegeben=SEKTP + "; r(h) = 1/2 · √(3h), h ∈ IR0+",
    gesucht="die Graphen von p und von r jeweils in ein geeignetes Koordinatensystem",
    verfahren="Wertetabellen anlegen, Achsen passend skalieren und beide Graphen zeichnen",
    schritte="2", zahlenraum="Bruch|Wurzel|negativ", einheiten="", abhaengig_von="2017MerhoehtBAnalysisCAS2-3b",
    ergebnis="Parabel durch (0; 0), (±1,5; 3), (±3; 12); Wurzelgraph durch (0; 0), (3; 1,5), (12; 3); Zeichnung im Erwartungshorizont (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I", fehlerquelle="r(h) als gespiegelte Parabel über die ganze h-Achse zeichnen",
    bemerkung="Standardbezug: K4 I. AB amtlich: I. Amtlich (Zeichnung im Erwartungshorizont, Punkte eigene Rechnung). Typ wiederverwendet. CAS-Anteil: Graphen mit dem Rechner.")
row("2017MerhoehtBAnalysisCAS2", "d", innen="3", seite="3", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Rotationsvolumen um die y-Achse über die Umkehrfunktion aufstellen", typ_neben="",
    stichwoerter="Füllhöhe 6 cm|V = π · ∫ von 0 bis 6 (r(h))^2 dh|27π/2 ≈ 42 cm^3",
    voraussetzungen="Rotation um die Achse der Füllhöhe|Scheibenformel mit r(h)",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Gläser/Füllhöhe", textumfang="kurz",
    gegeben=SEKTP + "; r(h) = 1/2 · √(3h) ist der Radius der Oberfläche bei der Füllhöhe h",
    gesucht="Volumen der Flüssigkeit bei einer Füllhöhe von 6 cm unter Verwendung von r(h)",
    verfahren="Das Volumen als Rotationskörper um die h-Achse: V = π · ∫ von 0 bis 6 (r(h))^2 dh = π · ∫ von 0 bis 6 3h/4 dh",
    schritte="2", zahlenraum="Bruch", einheiten="cm^3", abhaengig_von="2017MerhoehtBAnalysisCAS2-3b",
    ergebnis="π · ∫ von 0 bis 6 (r(h))^2 dh ≈ 42; das Volumen der Flüssigkeit beträgt etwa 42 cm^3 (amtlich)",
    zwischenergebnis="exakt 27π/2", niveau_geschaetzt="II", fehlerquelle="um die x-Achse rotieren (π · ∫ p(x)^2 dx) statt über die Füllhöhe zu integrieren",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (42,41). Schätzung II (r(h) vorgegeben, Scheibenformel über h); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet (2017-bb-ea B2.1 f). CAS-Anteil: Integral mit dem Rechner.")
row("2017MerhoehtBAnalysisCAS2", "", innen="4", seite="3", punkte="7", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Funktionsgleichung aus knickfreiem Übergang und einer Wertbedingung rekonstruieren",
    typ_neben="Wendepunkte über die zweite Ableitung berechnen",
    stichwoerter="Likörglas f_2 für 0 <= x <= 4|Scheitel in Tiefpunkt (0; 0) und Hochpunkt (4; 3)|Übergang ohne Knick an der Wendestelle 4/3 · √3|p1(x) = ax^2, p2(x) = −b(x − 4)^2 + 3",
    voraussetzungen="Extrem- und Wendepunkt von f_2|Scheitelpunktform|ohne Knick heißt gleicher Wert und gleiche Steigung|Gleichungssystem mit Wurzeln",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Gläser/Profil aus Parabeln", textumfang="lang",
    gegeben="f_2(x) = −3/256 · x^4 + 3/8 · x^2 (Likörglas); der Längsschnitt soll für 0 <= x <= 4 durch zwei quadratische Funktionen p1 und p2 beschrieben werden: die Scheitelpunkte ihrer Graphen liegen im Tiefpunkt bzw. im Hochpunkt des Graphen von f_2; die Graphen gehen ohne Knick ineinander über, und zwar an der x-Koordinate des Wendepunkts des Graphen von f_2",
    gesucht="Funktionsgleichungen von p1 und p2",
    verfahren="Tiefpunkt (0; 0), Hochpunkt (4; 3) und Wendestelle 4/3 · √3 von f_2 bestimmen; Ansatz p1(x) = ax^2 und p2(x) = −b(x − 4)^2 + 3; p1 = p2 und p1' = p2' an der Wendestelle liefern a und b",
    schritte="5", zahlenraum="Bruch|Wurzel", einheiten="", abhaengig_von="2017MerhoehtBAnalysisCAS2-1d",
    ergebnis="Der Graph von f_2 hat den Tiefpunkt (0; 0) und den Hochpunkt (4; 3), die Wendestelle ist 4/3 · √3; damit p1(x) = ax^2, p2(x) = −b · (x − 4)^2 + 3; die Bedingungen p1(4/3 · √3) = p2(4/3 · √3) und p1'(4/3 · √3) = p2'(4/3 · √3) liefern a = 3/16 · √3 und b = 3/32 · (3 + √3) (amtlich)",
    zwischenergebnis="a ≈ 0,325|b ≈ 0,444",
    niveau_geschaetzt="III", fehlerquelle="nur gleiche Funktionswerte an der Übergangsstelle fordern und die Steigungsbedingung vergessen",
    bemerkung="Standardbezug: K2 III, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (sympy exakt). Erste Schätzung: II (Bedingungen für wörtlich gehalten); korrigiert nach Deutungsliste (a): „ohne Knick ineinander übergehen“ ist nicht wörtlich „gleiche Steigung“ und erst in p1' = p2' zu übersetzen, die Scheitel werden erst über Extrempunkte von f_2 zu Ansätzen – Verkettung mit Übersetzung. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 7 BE. Typ und Nebentyp wiederverwendet. CAS-Anteil: Gleichungssystem und Wendestelle mit dem Rechner, Ansatz eigen.")
# ---- AG/LA (A2) CAS 1: Spielplatzturm, 25 BE – Fassung von AG/LA (A2) WTR 1 mit zusätzlicher Teilaufgabe e
# (Neigungswinkel); a, b, c, d, f, g, h = WTR 1 a, b, c, d, e, f, g (d mit Kontrollangabe und 3 statt 4 BE, g 4 statt 5 BE)
TURM = ("Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken "
        "und einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten "
        "sind A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze "
        "des Dachs ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m")
TURM_SK = ("schematisches Schrägbild des Turms: vier senkrechte Pfosten mit den unteren Enden A, B, C, D und den oberen "
           "Enden E, F, G, H, oben das Viereck EFGH als Rahmen aus Balken und darüber die Dachpyramide mit Spitze S; "
           "die Kante von H nach unten gestrichelt")
GETEILT = ("Teilaufgabe wortgleich mit dem WTR-Zweig (2017-ea-B-wtr, Datei 2017MerhoehtBAGLAA2WTR1, Teilaufgabe {}), "
           "geteilter Typ, Felder übernommen; Schätzung aus der WTR-Zeile übernommen.")
row("2017MerhoehtBAGLAA2CAS1", "a", innen="1", seite="1", punkte="1", afb_amtlich="I",
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
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. " + GETEILT.format("1a") + " CAS-Anteil: keiner.")
row("2017MerhoehtBAGLAA2CAS1", "b", innen="1", seite="1", punkte="5", afb_amtlich="I",
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
    zwischenergebnis="EF = (1; 5; 0)|FG = (−5; 1; 0)||EF| = |FG| = √26", niveau_geschaetzt="I",
    fehlerquelle="nur gleiche Seitenlängen zeigen (Raute) oder nur den rechten Winkel (Rechteck)",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. " + GETEILT.format("1b") + " Die übernommene Schätzung II der WTR-Zeile weicht vom amtlichen Bereich I ab; nach dem Vorrang des Amtlichen für übernommene Schätzungen (Kern § 5) auf I gesetzt (erste Schätzung: II). Die WTR-Zeile trägt ihre eigene Schätzung mit eigenem Standardbezug und bleibt. CAS-Anteil: Vektorrechnung mit dem Rechner möglich.")
row("2017MerhoehtBAGLAA2CAS1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrie einer geraden Pyramide bezüglich einer Koordinatenachse über Grundflächenmittelpunkt und Spitze begründen", typ_neben="",
    stichwoerter="gerade Pyramide mit quadratischer Grundfläche EFGH parallel zur x1x2-Ebene|Mittelpunkt der Grundfläche (0; 0; 4)|Spitze S(0; 0; 5) auf der x3-Achse",
    voraussetzungen="Mittelpunkt eines Quadrats als Diagonalenmitte|gerade Pyramide: Spitze über dem Mittelpunkt",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="kurz",
    gegeben=TURM + "; H(−3; −2; 4); EFGH ist ein Quadrat",
    gesucht="Begründung, dass die Pyramide EFGHS symmetrisch bezüglich der x3-Achse ist",
    verfahren="Der Mittelpunkt der Grundfläche (Mitte von EG) ist (0; 0; 4) und liegt wie S auf der x3-Achse; die Grundfläche ist ein Quadrat parallel zur x1x2-Ebene, die Pyramide gerade",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2017MerhoehtBAGLAA2CAS1-1b",
    ergebnis="Die Pyramide ist gerade und hat eine quadratische Grundfläche, die parallel zur x1x2-Ebene ist; der Mittelpunkt der Grundfläche liegt ebenso auf der x3-Achse wie die Spitze S (amtlich)",
    zwischenergebnis="Mitte von EG (0; 0; 4)", niveau_geschaetzt="II",
    fehlerquelle="nur die Lage von S auf der x3-Achse nennen",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. " + GETEILT.format("1c") + " CAS-Anteil: keiner.")
row("2017MerhoehtBAGLAA2CAS1", "d", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="Ebene L durch E, F und S|Spannvektoren EF = (1; 5; 0), ES = (−2; 3; 1)|5x1 − x2 + 13x3 = 65",
    voraussetzungen="Parameterform|Parameter eliminieren oder Vektorprodukt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Spielplatz/Turm", textumfang="kurz",
    gegeben=TURM + "; die Punkte E, F und S liegen in einer Ebene L; zur Kontrolle: 5x1 − x2 + 13x3 = 65",
    gesucht="eine Gleichung von L in Koordinatenform",
    verfahren="L: x = OE + r · EF + s · ES; aus x1 = 2 + r − 2s, x2 = −3 + 5r + 3s, x3 = 4 + s die Parameter eliminieren",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="L: x = OE + r · EF + s · ES; das Gleichungssystem x1 = 2 + r − 2s, x2 = −3 + 5r + 3s, x3 = 4 + s liefert L: 5x1 − x2 + 13x3 = 65 (amtlich)",
    zwischenergebnis="EF × ES = (5; −1; 13)", niveau_geschaetzt="II",
    fehlerquelle="die Konstante mit einem Punkt außerhalb der Ebene bestimmen",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Probe mit E, F, S). " + GETEILT.format("1d") + " In der CAS-Fassung mit Kontrollangabe und 3 statt 4 BE. CAS-Anteil: Gleichungssystem mit dem Rechner.")
row("2017MerhoehtBAGLAA2CAS1", "e", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="Dachfläche EFS in L: 5x1 − x2 + 13x3 = 65|Horizontale mit Normalenvektor (0; 0; 1)|cos φ = 13/√195|φ ≈ 21,4°",
    voraussetzungen="Normalenvektor aus der Koordinatengleichung ablesen|Winkel zwischen Ebenen über die Normalenvektoren",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="kurz",
    gegeben=TURM + "; die Dachfläche EFS liegt in L: 5x1 − x2 + 13x3 = 65",
    gesucht="Größe des Neigungswinkels der Dachfläche EFS gegenüber der Horizontalen",
    verfahren="Mit m = (0; 0; 1) und n = (5; −1; 13): cos φ = (m ∘ n)/(|m| · |n|) = 13/√195",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2017MerhoehtBAGLAA2CAS1-1d",
    ergebnis="Mit m = (0; 0; 1) und n = (5; −1; 13) ergibt sich cos φ = (m ∘ n)/(|m| · |n|), d. h. φ ≈ 21,4° (amtlich)",
    zwischenergebnis="|n| = √195", niveau_geschaetzt="II",
    fehlerquelle="mit dem Sinus statt dem Kosinus rechnen oder den Winkel zur Senkrechten angeben",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (21,42°). Erste Schätzung: I; korrigiert nach der Grundregel der engen Fassung: Normalenvektor der Horizontalen wählen und die Winkelformel für Ebenen anwenden ist eine Verkettung (II), wie in 2017-ga-B AG/LA (A2) WTR 1 e schon korrigiert – ungleich angewandt. Eigene Teilaufgabe der CAS-Fassung (im WTR-Zweig fehlt sie). Typ wiederverwendet. CAS-Anteil: Winkel mit dem Rechner.")
row("2017MerhoehtBAGLAA2CAS1", "f", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Länge eines Schattens auf einer Dachfläche über Schnitt von Lichtgerade und Ebene beschreiben", typ_neben="",
    stichwoerter="Stange von S bis T|Lichtgerade durch T mit Richtung v|Schnittpunkt mit der Ebene L|Schattenlänge als Abstand zu S",
    voraussetzungen="Schatten eines Punkts als Schnittpunkt Lichtgerade–Ebene|Abstand zweier Punkte",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="mittel",
    gegeben=TURM + "; die Dachfläche EFS liegt in L: 5x1 − x2 + 13x3 = 65; an der Spitze S ist eine gerade Stange befestigt, deren oberer Endpunkt T ist; das Sonnenlicht fällt in parallelen Geraden mit dem Richtungsvektor v; der Schatten der Stange liegt vollständig auf der Dachfläche EFS",
    gesucht="Beschreibung, wie man die Länge dieses Schattens berechnen kann, wenn die Koordinaten von T und v bekannt sind",
    verfahren="Die Gerade durch T mit Richtung v mit L schneiden; der Schatten reicht von S bis zu diesem Schnittpunkt, seine Länge ist der Abstand der beiden Punkte",
    schritte="2", zahlenraum="ganz", einheiten="m", abhaengig_von="2017MerhoehtBAGLAA2CAS1-1d",
    ergebnis="Man berechnet die Koordinaten des Schnittpunkts der Ebene L und der Geraden, die durch T verläuft und den Richtungsvektor v hat; der Abstand dieses Schnittpunkts vom Punkt S ist die Länge des Schattens in Metern (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Schatten mit der x1x2-Ebene statt mit der Dachebene schneiden",
    bemerkung="Standardbezug: K2 II, K3 II, K6 II. AB amtlich: II. Amtlich. " + GETEILT.format("1e") + " CAS-Anteil: keiner.")
row("2017MerhoehtBAGLAA2CAS1", "g", innen="1", seite="2", punkte="4", afb_amtlich="III",
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
    bemerkung="Standardbezug: K2 III, K3 III, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (t = ±0,4, nur 0,4 im Bereich). " + GETEILT.format("1f") + " In der CAS-Fassung 4 statt 5 BE. CAS-Anteil: Gleichung mit dem Rechner, Ansatz eigen.")
row("2017MerhoehtBAGLAA2CAS1", "h", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
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
    bemerkung="Standardbezug: K2 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (alle Lösungen liegen auf einem Kreis, die beiden Teilpunkte genügen). " + GETEILT.format("1g") + " CAS-Anteil: keiner.")
# ---- AG/LA (A2) CAS 2: Zelt, 25 BE – im Landesheft 2017-bb-ea-cas als B3.1 CAS (Zelt), in 2017-be-lk-cas als 2.2;
# 2017-bb-ea B3.1 ist die WTR-Fassung des Landes dazu (im Pool gibt es keine WTR-Fassung)
ZELT = ("Ein geschlossenes Zelt auf horizontalem Untergrund hat die Form einer Pyramide mit quadratischer Grundfläche; die "
        "seitlichen Kanten bilden vier gleich lange Stangen; das Zelt ist 3,90 m hoch, die Seitenlänge des Zeltbodens beträgt "
        "5,00 m; Modell: Pyramide ABCDS mit Spitze S, A im Koordinatenursprung, B auf dem positiven Teil der x-Achse, D auf "
        "dem positiven Teil der y-Achse, C(5; 5; 0), M Mittelpunkt der Grundfläche; das Dreieck ABS liegt in der Ebene "
        "E: −39y + 25z = 0; 1 LE = 1 m")
ZELT_SK1 = "Abbildung 1: räumliches Achsenkreuz als Vorlage, z nach oben, y nach rechts, x schräg nach vorn links (Schrägbild)"
VORDACH = ("; betrachtet wird die Zeltwand CDS; ein Teil dieser Wand kann mit zwei weiteren Stangen zu einem horizontalen "
           "Vordach aufgespannt werden; die dadurch entstehende Öffnung in der Wand ist im Modell ein Rechteck, dessen eine "
           "Seite so auf der Strecke CD liegt, dass ihr einer Endpunkt von C ebenso weit entfernt ist wie der andere von D; "
           "nach Abbildung 2 liegt das Vordach 1,80 m über dem Boden, die Öffnung ist 1,40 m breit")
ZELT_SK2 = ("Abbildung 2: Schrägbild der grauen Zeltpyramide; in der rechten vorderen Wand eine rechteckige Öffnung, deren "
            "ausgeschnittenes Wandstück als waagerechtes schwarzes Vordach nach außen aufgespannt ist und vorn auf zwei "
            "senkrechten Stangen ruht; Maßpfeile: Höhe des Vordachs über dem Boden 1,80 m, Breite der Öffnung am Boden 1,40 m")
row("2017MerhoehtBAGLAA2CAS2", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Koordinaten der Eckpunkte eines beschriebenen Körpers wählen",
    typ_neben="Punkt: Mittelpunkt einer Strecke im Raum bestimmen|Körper: Körper in ein räumliches Koordinatensystem einzeichnen",
    stichwoerter="B(5; 0; 0), D(0; 5; 0)|M(2,5; 2,5; 0)|S(2,5; 2,5; 3,9) über M|Pyramide ins Schrägbild zeichnen",
    voraussetzungen="Quadrat in der xy-Ebene aus einem Eckpunkt und Achsenlage|Spitze einer geraden Pyramide über dem Mittelpunkt|Schrägbild zeichnen",
    format="Kurzantwort|Zeichnen", operator="Geben Sie an|zeichnen Sie ein", antwort="Zahl|Grafik",
    material="Koordinatensystem", skizze=ZELT_SK1, kontext="Zelt/Pyramide", textumfang="lang",
    gegeben=ZELT, gesucht="Koordinaten der Punkte B, D, M und S; Zeichnung der Pyramide in ein Koordinatensystem gemäß Abbildung 1",
    verfahren="B und D aus der Seitenlänge 5 auf den Achsen, M als Mitte von AC, S 3,9 über M; Punkte ins Schrägbild eintragen und verbinden",
    schritte="3", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="B(5; 0; 0), D(0; 5; 0), M(2,5; 2,5; 0), S(2,5; 2,5; 3,9); Schrägbild der Pyramide mit Grundfläche ABCD und Spitze S (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I", fehlerquelle="S über A statt über M setzen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich (Zeichnung im Erwartungshorizont). Der Erwartungshorizont von a steht unten auf der Seite des Aufgabentexts und war beim Schätzen in Sicht. Typ und Nebentypen wiederverwendet (wie 2017-bb-ea-B3.1a). CAS-Anteil: keiner.")
row("2017MerhoehtBAGLAA2CAS2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Stumpfen Winkel zwischen zwei benachbarten Seitenflächen einer Pyramide über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="E: −39y + 25z = 0 mit Normalenvektor (0; −39; 25)|Ebene ADS aus Symmetrie mit (−39; 0; 25)|Winkel der Normalen 73,1°|Innenwinkel 180° − 73,1° = 106,9°",
    voraussetzungen="Normalenvektor der Nachbarwand über die Symmetrie der Pyramide|Winkel zwischen Normalenvektoren|stumpfen Innenwinkel als Ergänzung zu 180°",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Zelt/Pyramide", textumfang="kurz",
    gegeben=ZELT + "; jeweils zwei benachbarte Zeltwände schließen im Inneren des Zelts einen stumpfen Winkel ein",
    gesucht="Größe dieses Winkels",
    verfahren="Normalenvektor der Wand ADS n = (−39; 0; 25) (Vertauschen der Rollen von x und y), m = (0; −39; 25); cos φ = (m ∘ n)/(|m| · |n|) = 625/2146; der Innenwinkel ist 180° − φ",
    schritte="3", zahlenraum="ganz|negativ|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="Ein Normalenvektor der Ebene, in der das Dreieck ADS liegt, ist n = (−39; 0; 25); mit m = (0; −39; 25) ergibt sich cos φ = (m ∘ n)/(|m| · |n|), d. h. φ ≈ 73,1°; die Größe des Winkels beträgt etwa 180° − 73,1° = 106,9° (amtlich)",
    zwischenergebnis="m ∘ n = 625|Beträge von m und n je √2146", niveau_geschaetzt="II",
    fehlerquelle="den spitzen Winkel 73,1° angeben, obwohl nach dem stumpfen Innenwinkel gefragt ist",
    bemerkung="Standardbezug: K2 II, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (106,93°). Neuer Typ: vorhanden sind Neigungswinkel gegen Koordinatenebenen und der Innenwinkel Dach–senkrechte Wand, nicht der Winkel zweier Seitenflächen. CAS-Anteil: Winkel mit dem Rechner.")
row("2017MerhoehtBAGLAA2CAS2", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt mit gleichem Abstand zu allen Seitenflächen über die Symmetrieachse bestimmen",
    typ_neben="Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen",
    stichwoerter="Lichtquelle 80 cm von jeder Wand|Punkt auf der Achse (2,5; 2,5; z_L)|Abstand zu E gleich 0,8|z_L ≈ 2,4",
    voraussetzungen="Symmetrie der geraden Pyramide|Abstand Punkt–Ebene über die Hessesche Normalform|Lösung im Zelt auswählen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Zelt/Pyramide", textumfang="kurz",
    gegeben=ZELT + "; im Zelt ist eine Lichtquelle so aufgehängt, dass sie von jeder der vier Wände einen Abstand von 80 cm hat",
    gesucht="Koordinaten des Punkts, der die Lichtquelle im Modell darstellt",
    verfahren="Wegen der Symmetrie liegt der Punkt auf der Achse durch M und S: (2,5; 2,5; z_L); |−39 · 2,5 + 25 · z_L|/√(39^2 + 25^2) = 0,8 mit z_L <= 3,9 lösen",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="Koordinaten des Punkts: (2,5; 2,5; z_L); für z_L <= 3,9 liefert |−39 · 2,5 + 25 · z_L|/√(39^2 + 25^2) = 0,8: z_L ≈ 2,4 (amtlich)",
    zwischenergebnis="√2146 ≈ 46,32|zweite Lösung z ≈ 5,38 außerhalb des Zelts", niveau_geschaetzt="II",
    fehlerquelle="0,8 m senkrecht unter der Spitze abtragen statt senkrecht zur Wand",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (2,418). Erste Schätzung: III (nach Deutungsliste (b)); korrigiert nach der Ausnahme zu (b): die Symmetrieachse ist in Teilaufgabe a bestimmt (S senkrecht über M), die Symmetrie ist nicht erst zu erkennen; Achse und Abstandsgleichung sind eine Verkettung (II). Typ und Nebentyp wiederverwendet (wie 2017-bb-ea-B3.1c). CAS-Anteil: Betragsgleichung mit dem Rechner.")
row("2017MerhoehtBAGLAA2CAS2", "d", innen="1", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Linearkombination und lineare Abhängigkeit",
    typ="Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen", typ_neben="",
    stichwoerter="OP = r · OC + s · OS mit r, s ∈ [0; 1], r + s = 1|OP = OC + s · CS|s ∈ [0; 1]",
    voraussetzungen="r = 1 − s einsetzen|Parameterform einer Strecke",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Zelt/Pyramide", textumfang="kurz",
    gegeben=ZELT + "; der Ortsvektor eines Punkts P lässt sich als OP = r · OC + s · OS mit r, s ∈ [0; 1] und r + s = 1 darstellen",
    gesucht="Nachweis, dass P auf der Strecke CS liegt",
    verfahren="r = 1 − s einsetzen und umformen: OP = OC + s · (OS − OC) = OC + s · CS; wegen s ∈ [0; 1] liegt P auf der Strecke",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="OP = (1 − s) · OC + s · OS = OC + s · (OS − OC) = OC + s · CS; da s ∈ [0; 1], liegt P auf der Strecke CS (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II", fehlerquelle="nur die Gerade CS zeigen und die Einschränkung s ∈ [0; 1] nicht nutzen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 III. AB amtlich: III. Amtlich. Schätzung II nach dem Prinzip der engen Fassung (Nachrechnen einer Identität mit mitgeführtem Parameter, Ausnahme zu (c)); amtlich III – die Regel ist richtig angewandt, der Standardbezug trägt sie hier nicht; Abweichung bleibt. Typ wiederverwendet (wie 2017-bb-ea-B3.1d). CAS-Anteil: keiner.")
row("2017MerhoehtBAGLAA2CAS2", "e", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Strecke in einer geneigten Ebene über einen Höhenschnitt bestimmen",
    typ_neben="Streckenlänge berechnen|Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen",
    stichwoerter="Oberkante der Öffnung in 1,80 m Höhe|horizontaler Abstand 1,8/3,9 · 2,5 ≈ 1,15 m|Vordachlänge √(1,80^2 + 1,15^2) ≈ 2,14 m|äußere Kante bei y ≈ 5,98",
    voraussetzungen="Strahlensatz in der Wand CDS|Satz des Pythagoras|Vordach als hochgeklapptes Wandstück horizontal abtragen",
    format="Begründung|Rechnung", operator="Weisen Sie nach|Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=ZELT_SK2, kontext="Zelt/Vordach", textumfang="lang",
    gegeben=ZELT + VORDACH + "; alle Punkte der Kante des Vordachs, an deren Enden die beiden Stangen befestigt sind, haben im Modell die gleiche y-Koordinate; zur Kontrolle: etwa 5,98",
    gesucht="Nachweis, dass die Länge des Vordachs etwa 2,14 m beträgt; diese y-Koordinate",
    verfahren="Die Wand CDS steigt auf 2,5 m waagerecht um 3,9 m: bis 1,80 m Höhe liegt die Oberkante 1,8/3,9 · 2,5 m waagerecht innen; Vordachlänge = Länge der Öffnung in der Wand = √(1,8^2 + (1,8/3,9 · 2,5)^2); y = 5 − 1,8/3,9 · 2,5 + Vordachlänge",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="Die horizontale Entfernung von oberer und unterer Kante der Öffnung beträgt 1,8/3,9 · 2,5 m; damit ergibt sich für die Länge des Vordachs √(1,80^2 + (1,8/3,9 · 2,5)^2) ≈ 2,14; y-Koordinate: 5 − 1,8/3,9 · 2,5 + √(1,80^2 + (1,8/3,9 · 2,5)^2) ≈ 5,98 (amtlich)",
    zwischenergebnis="Oberkante bei y ≈ 3,85", niveau_geschaetzt="II",
    fehlerquelle="die Vordachlänge als Höhe 1,80 m oder als waagerechten Abstand 1,15 m nehmen",
    bemerkung="Standardbezug: K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (2,138; 5,984; Probe 39y + 25z = 195 für die Oberkante). Erste Schätzung: III (nach Deutungsliste (a)); korrigiert nach der Ausnahme zu (a): Text und Abbildung 2 geben die Übersetzung vor (ein Teil der Wand wird zum horizontalen Vordach, Höhe 1,80 m eingezeichnet, Länge und y-Koordinate als Kontrollwerte genannt); Strahlensatz, Pythagoras und Abtragen sind eine Verkettung (II). Die Maße 1,80 m und 1,40 m stehen nur in Abbildung 2. Typ und Nebentypen wiederverwendet (wie 2017-bb-ea-cas-B3.1e). CAS-Anteil: keiner.")
row("2017MerhoehtBAGLAA2CAS2", "f", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Ganzzahligen Scharparameter aus einer Bereichsbedingung an den Durchstoßpunkt bestimmen",
    typ_neben="Schnittpunkt von Gerade und Ebene berechnen",
    stichwoerter="Lichtstrahl durch M(2,5; 2,5; 0) mit Richtung (0,5; −4,2; a)|Loch im Vordach: z = 1,8, x ∈ [1,8; 3,2], y ∈ [3,85; 5,98]|a = −3: Loch (2,2; 5,02; 1,8)|möglich a = −5, −4, −3",
    voraussetzungen="Gerade durch M mit Parameterrichtung|Schnitt mit der Ebene z = 1,8|Bereichsbedingungen aus Öffnungsbreite und Vordachlage|ganzzahlige Werte durch Probieren",
    format="Rechnung", operator="Ermitteln Sie|geben Sie an", antwort="Zahl",
    material="Skizze", skizze=ZELT_SK2, kontext="Zelt/Sonnenlicht", textumfang="lang",
    gegeben=ZELT + VORDACH + "; die äußere Kante des Vordachs liegt bei y ≈ 5,98; Sonnenlicht fällt zu einem Zeitpunkt in parallelen Geraden mit dem Richtungsvektor (0,5; −4,2; a) und trifft durch ein kleines Loch im Vordach genau den Mittelpunkt M des Zeltbodens; für a kommen verschiedene ganzzahlige Werte infrage",
    gesucht="einer dieser Werte von a und die Koordinaten des zugehörigen Punkts, der eine mögliche Position des Lochs darstellt",
    verfahren="Loch (xP; yP; 1,8) mit xP ∈ [1,8; 3,2] und yP ∈ [3,85; 5,98]; (2,5; 2,5; 0) + t · (0,5; −4,2; a) = (xP; yP; 1,8); ganzzahlige a probieren",
    schritte="4", zahlenraum="dezimal|negativ|ganz", einheiten="m", abhaengig_von="2017MerhoehtBAGLAA2CAS2-1e",
    ergebnis="Bedingungen xP ∈ [1,8; 3,2], yP ∈ [b; c] mit b = 5 − 1,8/3,9 · 2,5 ≈ 3,85 und c ≈ 5,98, zP = 1,8 und (2,5; 2,5; 0) + t · (0,5; −4,2; a) = (xP; yP; 1,8); Probieren liefert für a = −3: xP = 2,2, yP = 5,02 (amtlich)",
    zwischenergebnis="t = 1,8/a|yP = 2,5 − 7,56/a|zulässig a ∈ {−5; −4; −3}", niveau_geschaetzt="III",
    fehlerquelle="die Bedingung an die x-Koordinate (Breite der Öffnung) oder die wandseitige Kante bei y ≈ 3,85 übersehen",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (a = −5, −4, −3 zulässig). Typ und Nebentyp wiederverwendet (wie 2017-bb-ea-B3.1f). CAS-Anteil: Gleichungssystem mit dem Rechner, Bedingungen eigen.")
# ---- Stochastik CAS 1: Haushaltsgrößen 2013, 25 BE (eigene Aufgabe, im WTR-Zweig Samenkörner)
HAUS = ("Anteile der Haushalte in Deutschland 2013 nach Größe: 1-Personen-Haushalte 40,5 %, 2-Personen-Haushalte 34,5 %, "
        "3-Personen-Haushalte 12,5 %, 4-Personen-Haushalte 9,2 %, Haushalte mit mindestens 5 Personen 3,3 %")
HAUS_SK = "Tabelle mit zwei Spalten: Haushaltsgröße (1, 2, 3, 4 Personen, mindestens 5 Personen) und Anteil (40,5 %, 34,5 %, 12,5 %, 9,2 %, 3,3 %)"
row("2017MerhoehtBStochastikCAS1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="100 zufällig ausgewählte Haushalte|A: genau 40 Ein-Personen-Haushalte, p = 0,405|B: mindestens 50 Mehrpersonenhaushalte, p = 0,595|P(A) ≈ 8,1 %, P(B) ≈ 97,8 %",
    voraussetzungen="Binomialmodell für eine Stichprobe|Mehrpersonenhaushalt als Gegenereignis zum Ein-Personen-Haushalt|kumulierte Wahrscheinlichkeit mit dem Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze=HAUS_SK, kontext="Statistik/Haushalte", textumfang="mittel",
    gegeben=HAUS + "; für eine Umfrage 2013 werden 100 Haushalte zufällig ausgewählt; A: genau vierzig 1-Personen-Haushalte; B: mindestens die Hälfte der ausgewählten Haushalte sind Mehrpersonenhaushalte",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="X ~ B(100; 0,405): P(X = 40); Y ~ B(100; 0,595) für die Mehrpersonenhaushalte: P(Y >= 50)",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(A) ≈ 8,1 %, P(B) ≈ 97,8 % (amtlich)", zwischenergebnis="P(A) ≈ 0,0808|P(B) ≈ 0,9784",
    niveau_geschaetzt="I", fehlerquelle="für B die Wahrscheinlichkeit der Mehrpersonenhaushalte als 1 − 0,033 statt 1 − 0,405 nehmen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ und Nebentyp wiederverwendet. CAS-Anteil: Binomialwerte mit dem Rechner.")
row("2017MerhoehtBStochastikCAS1", "b", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Term 1 − (0,967^100 + 100 · 0,033 · 0,967^99)|p = 0,033 für mindestens 5 Personen|Gegenereignis von null oder einem Treffer|mindestens zwei solche Haushalte",
    voraussetzungen="Summanden als P(X = 0) und P(X = 1) erkennen|Gegenereignis",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Tabelle", skizze=HAUS_SK, kontext="Statistik/Haushalte", textumfang="kurz",
    gegeben=HAUS + "; 100 Haushalte werden zufällig ausgewählt; Term 1 − (0,967^100 + 100 · 0,033 · 0,967^99)",
    gesucht="Bedeutung des Terms im Sachzusammenhang",
    verfahren="0,033 ist der Anteil der Haushalte mit mindestens 5 Personen; die Summe ist P(X = 0) + P(X = 1), der Term also P(X >= 2)",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Mit dem Term kann die Wahrscheinlichkeit dafür berechnet werden, dass in mindestens zwei der ausgewählten Haushalte mindestens fünf Personen lebten (amtlich)",
    zwischenergebnis="Wert ≈ 0,846", niveau_geschaetzt="II", fehlerquelle="„höchstens einer“ statt „mindestens zwei“ angeben",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,846). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBStochastikCAS1", "", innen="2", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="Bedingung Mehrpersonenhaushalt, Anteil 1 − 0,405|3-Personen-Haushalt 0,125|0,125/0,595 ≈ 21,0 %",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient|Anteil der Bedingung über das Gegenereignis",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze=HAUS_SK, kontext="Statistik/Haushalte", textumfang="kurz",
    gegeben=HAUS + "; ein 2013 zufällig ausgewählter Mehrpersonenhaushalt",
    gesucht="Wahrscheinlichkeit, dass es sich um einen 3-Personen-Haushalt handelte",
    verfahren="0,125/(1 − 0,405) berechnen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,125/(1 − 0,405) ≈ 21,0 % (amtlich)", zwischenergebnis="1 − 0,405 = 0,595",
    niveau_geschaetzt="I", fehlerquelle="12,5 % ohne Bedingung angeben",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,2101). Erste Schätzung: II; korrigiert nach der Grundregel der engen Fassung (I bleibt die einzelne Rechnung): ein Quotient, der Nenner über das Gegenereignis ist kein eigener Schritt (wie 2017-ga-B Stochastik WTR 1 1 b). Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 3 BE. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBStochastikCAS1", "", innen="3", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit einer Summe über alle Ergebnisfolgen mit Reihenfolgen berechnen", typ_neben="",
    stichwoerter="drei Haushalte mit zusammen genau fünf Personen|Zerlegungen 1 + 1 + 3 und 1 + 2 + 2|je drei Reihenfolgen|3 · 0,405^2 · 0,125 + 3 · 0,405 · 0,345^2 ≈ 20,6 %",
    voraussetzungen="Zerlegungen der Summe systematisch finden|Reihenfolgen zählen|Pfadregeln",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze=HAUS_SK, kontext="Statistik/Haushalte", textumfang="kurz",
    gegeben=HAUS + "; drei Haushalte werden 2013 zufällig ausgewählt",
    gesucht="Wahrscheinlichkeit, dass in den drei Haushalten insgesamt genau fünf Personen lebten",
    verfahren="Mögliche Größen: {1; 1; 3} und {1; 2; 2}, je drei Anordnungen; Pfadwahrscheinlichkeiten addieren",
    schritte="3", zahlenraum="dezimal|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="3 · 0,405^2 · 0,125 + 3 · 0,405 · 0,345^2 ≈ 20,6 % (amtlich)", zwischenergebnis="0,0615 + 0,1446",
    niveau_geschaetzt="II", fehlerquelle="die Reihenfolgen nicht mitzählen oder Haushalte mit mindestens 5 Personen einbeziehen",
    bemerkung="Standardbezug: K3 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,2061). Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 3 BE. Typ wiederverwendet (2021-be-gk B4 h). CAS-Anteil: keiner.")
row("2017MerhoehtBStochastikCAS1", "", innen="4", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln", typ_neben="",
    stichwoerter="Y Anzahl der 2-Personen-Haushalte, p = 0,345|P(Y > 20) >= 0,95|n >= 80",
    voraussetzungen="Binomialmodell mit unbekanntem n|„mehr als zwanzig“ als Y >= 21|Probieren oder Tabellenkalkulation mit dem Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze=HAUS_SK, kontext="Statistik/Haushalte", textumfang="kurz",
    gegeben=HAUS + "; Anteil der 2-Personen-Haushalte 34,5 %",
    gesucht="wie viele Haushalte man 2013 mindestens hätte auswählen müssen, damit darunter mit einer Wahrscheinlichkeit von mindestens 95 % mehr als zwanzig 2-Personen-Haushalte sind",
    verfahren="Für Y ~ B(n; 0,345) das kleinste n mit P(Y > 20) >= 0,95 durch Probieren mit dem Rechner suchen",
    schritte="3", zahlenraum="ganz|dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Y: Anzahl der 2-Personen-Haushalte; ist n die Anzahl der auszuwählenden Haushalte, so gilt P(Y > 20) >= 0,95 ⇔ n >= 80 (amtlich)",
    zwischenergebnis="n = 79: 0,9476|n = 80: 0,9551",
    niveau_geschaetzt="II", fehlerquelle="P(Y >= 20) statt P(Y > 20) ansetzen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 4 BE. Typ wiederverwendet. Schätzung II nach der engen Fassung (kein Listeneintrag); amtlich III – keine Regel als falsch angewandt erkannt, Abweichung bleibt. Mindestumfang für eine Mindestwahrscheinlichkeit im Pool erneut amtlich III (Kandidat für die Deutungsliste nach 2017-ga-B, nicht gesetzt). CAS-Anteil: Probieren mit dem Rechner, Ansatz eigen.")
row("2017MerhoehtBStochastikCAS1", "", innen="5", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Gesamtzahl der Gruppen aus der Personenzahl und der mittleren Gruppengröße unter einer vereinfachenden Annahme schätzen", typ_neben="",
    stichwoerter="80 Millionen Menschen|Annahme: Haushalte mit mindestens 5 Personen haben genau 5|mittlere Haushaltsgröße 2,003|etwa 40 Millionen Haushalte",
    voraussetzungen="gewichtetes Mittel über die Anteile|vereinfachende Annahme treffen und nennen|Gesamtzahl über Division",
    format="Rechnung|Begründung", operator="Bestimmen Sie|erläutern Sie", antwort="Zahl|Text",
    material="Tabelle", skizze=HAUS_SK, kontext="Statistik/Haushalte", textumfang="kurz",
    gegeben=HAUS + "; 2013 lebten in Deutschland insgesamt etwa 80 Millionen Menschen",
    gesucht="Näherungswert für die Gesamtzahl der Haushalte 2013 mit Erläuterung des Vorgehens",
    verfahren="Vereinfachend 5 Personen je Haushalt der letzten Gruppe; (1 · 0,405 + 2 · 0,345 + 3 · 0,125 + 4 · 0,092 + 5 · 0,033) · x = 80 000 000 nach x lösen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Geht man vereinfachend davon aus, dass in den Haushalten mit mindestens 5 Personen genau fünf Personen lebten, und bezeichnet die Anzahl der Haushalte mit x, so ergibt sich aus (1 · 0,405 + 2 · 0,345 + 3 · 0,125 + 4 · 0,092 + 5 · 0,033) · x = 80000000 eine Gesamtzahl von etwa 40 Millionen Haushalten (amtlich)",
    zwischenergebnis="mittlere Haushaltsgröße 2,003|x ≈ 39,9 Millionen",
    niveau_geschaetzt="III", fehlerquelle="80 Millionen durch die Zahl der Größenklassen teilen oder die Annahme für die letzte Gruppe nicht nennen",
    bemerkung="Standardbezug: K2 III, K3 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (39,94 Millionen). Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 4 BE. Neuer Typ. CAS-Anteil: keiner.")
row("2017MerhoehtBStochastikCAS1", "", innen="6", seite="2", punkte="6", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Wahl der Nullhypothese aus der Sicht des Entscheiders begründen",
    typ_neben="Entscheidungsregel eines einseitigen Signifikanztests bestimmen",
    stichwoerter="Vermutung 2014: Anteil der 1-Personen-Haushalte größer als 2013|irrtümliches Annehmen der Vermutung vermeiden|H0: p <= 0,405|n = 500, α = 5 %|Ablehnung ab 222",
    voraussetzungen="zu vermeidenden Fehler als Fehler erster Art in die Nullhypothese legen|rechtsseitiger Test|kumulierte Binomialwahrscheinlichkeit mit dem Rechner",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|bestimmen Sie", antwort="Text|Zahl",
    material="Tabelle", skizze=HAUS_SK, kontext="Statistik/Haushalte", textumfang="mittel",
    gegeben=HAUS + "; 2014 wurde vermutet, dass der tatsächliche Anteil der 1-Personen-Haushalte größer als 2013 ist; Test mit einer Stichprobe von 500 Haushalten auf dem Signifikanzniveau 5 %; möglichst vermieden werden soll, irrtümlich davon auszugehen, dass die Vermutung zutrifft",
    gesucht="passende Nullhypothese und zugehörige Entscheidungsregel",
    verfahren="Die Vermutung wird Gegenhypothese, H0: p <= 0,405; Z ~ B(500; 0,405), kleinstes k mit P(Z >= k) <= 0,05",
    schritte="3", zahlenraum="ganz|dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Nullhypothese: „Der tatsächliche Anteil der 1-Personen-Haushalte beträgt höchstens 40,5 %.“; Z: Anzahl der 1-Personen-Haushalte, P(Z >= k) <= 5 %; befinden sich in der Stichprobe mindestens 222 1-Personen-Haushalte, so wird die Nullhypothese abgelehnt (amtlich)",
    zwischenergebnis="P(Z >= 221) ≈ 0,051|P(Z >= 222) ≈ 0,042",
    niveau_geschaetzt="II", fehlerquelle="die Vermutung als Nullhypothese wählen und linksseitig testen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (k = 222). Erste Schätzung: III (Deutung und Verkettung); korrigiert nach dem Prinzip der engen Fassung: die Wahl der Nullhypothese folgt aus dem im Text wörtlich genannten zu vermeidenden Fehler, kein Eintrag (a) bis (e) greift; Nullhypothese und Entscheidungsregel sind eine Verkettung (II). Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 6 BE. Typ und Nebentyp wiederverwendet (erste Leistung: Nullhypothese). CAS-Anteil: kumulierte Werte mit dem Rechner, Ansatz eigen.")
# ---- Stochastik CAS 2: Glutenunverträglichkeit und Teststreifen, 25 BE (eigene Aufgabe, im WTR-Zweig Samenkörner)
GLUT = ("In Deutschland liegt bei 1 % der Bevölkerung eine Glutenunverträglichkeit vor; ein Schnelltest heißt positiv, wenn "
        "er die Unverträglichkeit anzeigt; liegt sie vor, ist er mit 98 % positiv; liegt sie nicht vor, ist er mit 4 % "
        "dennoch positiv; der Test wird bei einer zufällig ausgewählten Person durchgeführt")
BAUM_SK = ("zweistufiges Baumdiagramm: erste Stufe G (1 %) und nicht G (99 %), zweite Stufe P und nicht P; bei G: P 98 %, "
           "nicht P 2 %; bei nicht G: P 4 %, nicht P 96 %")
STREIF = ("Teststreifen mit Indikator: bei weniger als 15 mg ist ein Streifen unbrauchbar; Ziel des Herstellers: höchstens "
          "10 % unbrauchbar; Qualitätskontrolle mit einer Stichprobe von 100 Streifen, nur bei mindestens 16 unbrauchbaren "
          "wird das Herstellungsverfahren verbessert")
row("2017MerhoehtBStochastikCAS2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="G: Glutenunverträglichkeit, P: Test positiv|1 % und 99 %|98 % und 2 %, 4 % und 96 %",
    voraussetzungen="Gegenwahrscheinlichkeiten ergänzen|bedingte Angaben als Äste der zweiten Stufe",
    format="Zeichnen", operator="Erstellen Sie", antwort="Grafik",
    material="keins", skizze=BAUM_SK, kontext="Medizin/Schnelltest", textumfang="mittel",
    gegeben=GLUT, gesucht="ein beschriftetes Baumdiagramm zum Sachzusammenhang",
    verfahren="Erste Stufe Unverträglichkeit ja oder nein, zweite Stufe Testergebnis; alle Äste mit Wahrscheinlichkeiten beschriften",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Baumdiagramm mit G (1 %), nicht G (99 %); bei G: P 98 %, nicht P 2 %; bei nicht G: P 4 %, nicht P 96 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I", fehlerquelle="die Stufen vertauschen und 98 % als P(G | P) eintragen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich (Zeichnung). Der Erwartungshorizont von 1 a steht unten auf Seite 2 und war beim Schätzen in Sicht. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBStochastikCAS2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen",
    typ_neben="Anteil über die totale Wahrscheinlichkeit aus dem Baumdiagramm berechnen",
    stichwoerter="A: Unverträglichkeit und positiv, 0,01 · 0,98 = 0,98 %|B: Test negativ, 0,01 · 0,02 + 0,99 · 0,96 ≈ 95,06 %",
    voraussetzungen="Produktregel|Summenregel über zwei Pfade",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=BAUM_SK, kontext="Medizin/Schnelltest", textumfang="kurz",
    gegeben=GLUT + "; A: Unverträglichkeit liegt vor und Testergebnis positiv; B: Testergebnis negativ",
    gesucht="Wahrscheinlichkeiten von A und B",
    verfahren="P(A) als Pfadprodukt, P(B) als Summe der beiden Pfade mit negativem Test",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2017MerhoehtBStochastikCAS2-1a",
    ergebnis="P(A) = 0,01 · 0,98 = 0,98 %; P(B) = 0,01 · 0,02 + 0,99 · 0,96 ≈ 95,06 % (amtlich)", zwischenergebnis="",
    niveau_geschaetzt="I", fehlerquelle="für B nur den Pfad nicht G–nicht P nehmen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ und Nebentyp wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBStochastikCAS2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(G | P)|0,01 · 0,98/(0,01 · 0,98 + 0,99 · 0,04)|≈ 19,8 %",
    voraussetzungen="Bedingung als Summe zweier Pfade im Nenner|Satz von Bayes",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze=BAUM_SK, kontext="Medizin/Schnelltest", textumfang="kurz",
    gegeben=GLUT, gesucht="Wahrscheinlichkeit, dass eine Glutenunverträglichkeit vorliegt, wenn das Testergebnis positiv ist",
    verfahren="P(G | P) = P(G ∩ P)/P(P) mit P(P) = 0,01 · 0,98 + 0,99 · 0,04",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2017MerhoehtBStochastikCAS2-1b",
    ergebnis="0,01 · 0,98/(0,01 · 0,98 + 0,99 · 0,04) ≈ 19,8 % (amtlich)", zwischenergebnis="P(P) = 0,0494",
    niveau_geschaetzt="II", fehlerquelle="P(P | G) = 98 % angeben",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,1984). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MerhoehtBStochastikCAS2", "", innen="2", seite="1|2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer prozentualen Abweichung vom Erwartungswert nach beiden Seiten berechnen", typ_neben="",
    stichwoerter="20 000 zufällig ausgewählte Personen, p = 0,01|E(X) = 200, 10 % davon = 20|Abweichung um mehr als 10 %: 1 − P(180 <= X <= 220)|≈ 14,5 %",
    voraussetzungen="Binomialmodell als geeignetes Modell|symmetrisches Intervall um den Erwartungswert|kumulierte Werte mit dem Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Medizin/Studie", textumfang="mittel",
    gegeben="Bei 1 % der Bevölkerung Deutschlands liegt eine Glutenunverträglichkeit vor; für eine Studie werden 20 000 Personen zufällig ausgewählt; X ist die Anzahl der ausgewählten Personen mit Glutenunverträglichkeit",
    gesucht="in einem geeigneten Modell die Wahrscheinlichkeit, dass X um mehr als 10 % vom Erwartungswert abweicht",
    verfahren="X ~ B(20 000; 0,01), E(X) = 200; mehr als 10 % Abweichung heißt X < 180 oder X > 220; 1 − P(180 <= X <= 220)",
    schritte="3", zahlenraum="ganz|dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="E(X) = 0,01 · 20000 = 200; 10 % · 200 = 20; 1 − P(180 <= X <= 220) ≈ 14,5 % (amtlich)",
    zwischenergebnis="P(X < 180) ≈ 0,071|P(X > 220) ≈ 0,074",
    niveau_geschaetzt="II", fehlerquelle="die Grenzen 180 und 220 dem Abweichungsbereich zuschlagen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,1450). Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 4 BE. Typ wiederverwendet. CAS-Anteil: kumulierte Werte mit dem Rechner.")
row("2017MerhoehtBStochastikCAS2", "a", innen="3", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Fehlentscheidungen eines Tests im Sachzusammenhang beschreiben", typ_neben="",
    stichwoerter="Verbesserung, obwohl höchstens 10 % unbrauchbar (unnötige Verbesserung)|keine Verbesserung, obwohl mehr als 10 % unbrauchbar",
    voraussetzungen="Entscheidungsregel mit der wahren Lage vergleichen|zwei Fehlerarten im Sachzusammenhang",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Qualitätskontrolle/Teststreifen", textumfang="mittel",
    gegeben=STREIF, gesucht="Beschreibung der Fehlentscheidungen, die bei dieser Qualitätskontrolle auftreten können",
    verfahren="Beide Kombinationen aus wahrem Anteil und Entscheidung benennen, die nicht zusammenpassen",
    schritte="2", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Obwohl höchstens 10 % der hergestellten Teststreifen unbrauchbar sind, entscheidet man sich aufgrund der Kontrolle für eine Verbesserung des Verfahrens; obwohl mehr als 10 % unbrauchbar sind, entscheidet man sich nicht für eine Verbesserung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II", fehlerquelle="die Fehler auf einzelne Streifen statt auf die Entscheidung über das Verfahren beziehen",
    bemerkung="Standardbezug: K1 II, K6 II. AB amtlich: II. Amtlich. Neuer Typ: vorhanden ist das Beschreiben nur zusammen mit einer Berechnung des Fehlers zweiter Art. CAS-Anteil: keiner.")
row("2017MerhoehtBStochastikCAS2", "b", innen="3", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Ablehnungsgrenze bei größerem Stichprobenumfang ohne höheren Fehler erster Art bestimmen", typ_neben="",
    stichwoerter="unnötige Verbesserung als Fehler erster Art, p = 0,1|bisher P(Y >= 16) bei n = 100 ≈ 0,040|neu n = 200: P(Y >= k) <= P(Y >= 16)|k >= 29",
    voraussetzungen="Irrtumswahrscheinlichkeit der alten Regel berechnen|kleinstes k für die neue Stichprobe mit dem Rechner suchen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Qualitätskontrolle/Teststreifen", textumfang="mittel",
    gegeben=STREIF + "; künftig wird eine Stichprobe von 200 Teststreifen genommen; die Wahrscheinlichkeit für eine unnötige Verbesserung soll sich dadurch nicht erhöhen",
    gesucht="Mindestanzahl unbrauchbarer Teststreifen, ab der man sich nun für die Verbesserung entscheidet",
    verfahren="α alt = P(Y >= 16) für Y ~ B(100; 0,1); kleinstes k mit P(Y >= k) <= α alt für Y ~ B(200; 0,1)",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Y: Anzahl unbrauchbarer Teststreifen; ist k die Anzahl, ab der man sich für die Verbesserung entscheidet, gilt P(Y >= k) bei n = 200 <= P(Y >= 16) bei n = 100, p = 0,1 ⇔ k >= 29 (amtlich)",
    zwischenergebnis="P(Y >= 16) ≈ 0,0399 (n = 100)|n = 200: P(Y >= 28) ≈ 0,0434, P(Y >= 29) ≈ 0,0271",
    niveau_geschaetzt="III", fehlerquelle="die Grenze einfach verdoppeln (32) oder das Signifikanzniveau 5 % statt der alten Irrtumswahrscheinlichkeit nehmen",
    bemerkung="Standardbezug: K2 III, K3 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Neuer Typ. CAS-Anteil: kumulierte Werte mit dem Rechner, Ansatz eigen.")
row("2017MerhoehtBStochastikCAS2", "c", innen="3", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Normalverteilung und Sigma-Regeln",
    typ="Standardabweichung einer Normalverteilung aus einer vorgegebenen Wahrscheinlichkeit bei festem Erwartungswert ermitteln", typ_neben="",
    stichwoerter="Indikatormenge normalverteilt, μ = 20 mg, σ = 4,0 mg|P(Z < 15) ≈ 10,6 %|halbiert ≈ 5,3 %|neue σ ≈ 3,1 mg",
    voraussetzungen="Wahrscheinlichkeit der Normalverteilung mit dem Rechner|Gleichung in σ lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Qualitätskontrolle/Teststreifen", textumfang="mittel",
    gegeben="Die Indikatormenge Z auf den Teststreifen ist normalverteilt; ein Streifen mit weniger als 15 mg ist unbrauchbar; vor der Verbesserung μ = 20 mg und σ = 4,0 mg; durch die Verbesserung wurde die Wahrscheinlichkeit für einen unbrauchbaren Streifen halbiert, μ blieb unverändert",
    gesucht="die geänderte Standardabweichung",
    verfahren="P(Z < 15) mit σ = 4 berechnen, halbieren und die Gleichung P(Z < 15) = 5,3 % nach σ lösen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="mg", abhaengig_von="",
    ergebnis="Z: Indikatormenge in mg; für σ = 4,0 mg gilt P(Z < 15) ≈ 10,6 %; P(Z < 15) ≈ 5,3 % liefert eine Standardabweichung von etwa 3,1 mg (amtlich)",
    zwischenergebnis="σ ≈ 3,09",
    niveau_geschaetzt="II", fehlerquelle="σ halbieren statt die Wahrscheinlichkeit",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (3,090). Schätzung II („halbiert“ ist wörtlich vorgegeben, Verkettung zweier Rechnerschritte); amtlich III – keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: vorhanden ist die Bestimmung des Erwartungswerts aus einer Wahrscheinlichkeit. CAS-Anteil: Normalverteilung und Gleichung mit dem Rechner.")
NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Extrempunkte einer Schar mit Art in Abhängigkeit vom Parameter bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Extrempunkte einer Funktionenschar über die Nullstellen der ersten Ableitung und das Vorzeichen der zweiten Ableitung mit Koordinaten und Art in Abhängigkeit vom Parameter bestimmen, ohne Fallunterscheidung nach dem Parameter.", "2017MerhoehtBAnalysisCAS1-1b"),
    ("Lage der Extrempunkte einer Schar auf einer gegebenen Kurve durch Einsetzen nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die parameterabhängigen Koordinaten der Extrempunkte einer Schar in die Gleichung einer vorgegebenen Kurve einsetzen und die Gleichheit für alle Parameterwerte zeigen.", "2017MerhoehtBAnalysisCAS1-1c"),
    ("Beschränktheit eines Flächeninhalts mit variabler Grenze über den Integralterm nachweisen", "Analysis", "Uneigentliche Integrale",
     "Den Inhalt einer Fläche mit variabler oberer Grenze als Term berechnen und zeigen, dass er für alle Grenzen unter einer Schranke bleibt, weil von ihr stets ein positiver Term abgezogen wird.", "2017MerhoehtBAnalysisCAS1-1e"),
    ("Waagerechte Ausdehnung eines Profils in vorgegebener Höhe über die Stellen mit vorgegebenem Funktionswert berechnen", "Analysis", "Gleichungen lösen",
     "Eine vorgegebene Höhe oder Tiefe als Funktionswert ansetzen, die Stellen im Definitionsbereich lösen und die waagerechte Ausdehnung (Länge, Radius, Umfang) daraus berechnen.", "2017MerhoehtBAnalysisCAS1-2d"),
    ("Nullstellen und Werte: Verfahren zur beliebig genauen Näherung einer Kurvenlänge über verfeinerte Streckenzüge beschreiben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Beschreiben, wie die Länge eines Graphenstücks über Streckenzüge durch Punkte des Graphen bei immer feinerer Teilung des Intervalls beliebig genau angenähert wird.", "2017MerhoehtBAnalysisCAS1-2g"),
    ("Kurvenlänge über eine vorgegebene Integralformel berechnen und mit der Länge von Streckenzügen vergleichen", "Analysis", "Stammfunktion und Hauptsatz",
     "Die Länge eines Graphenstücks mit der vorgegebenen Formel ∫ √(1 + (f'(x))^2) dx numerisch berechnen und begründen, dass sie größer ist als die Länge jedes einbeschriebenen Streckenzugs.", "2017MerhoehtBAnalysisCAS1-2h"),
    ("Berührpunkt einer Tangente durch einen vorgegebenen Graphenpunkt berechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Tangente in einem Punkt mit unbekannter Stelle u allgemein aufstellen, einen vorgegebenen Punkt einsetzen und die Gleichung nach u lösen; unpassende Lösungen ausschließen.", "2017MerhoehtBAnalysisCAS2-2d"),
    ("Radius der Flüssigkeitsoberfläche in Abhängigkeit von der Füllhöhe über die Umkehrung der Profilfunktion nachweisen", "Analysis", "Umkehrfunktion",
     "Bei einem Gefäß mit vertikaler Rotationsachse die Füllhöhe als Funktionswert der Profilfunktion deuten und diese Gleichung nach dem Radius (positive Lösung) auflösen.", "2017MerhoehtBAnalysisCAS2-3b"),
    ("Stumpfen Winkel zwischen zwei benachbarten Seitenflächen einer Pyramide über die Normalenvektoren berechnen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Den Normalenvektor der Nachbarfläche (etwa über die Symmetrie der Pyramide) bestimmen, den Winkel zwischen den Normalenvektoren berechnen und den stumpfen Innenwinkel als Ergänzung zu 180° angeben.", "2017MerhoehtBAGLAA2CAS2-1b"),
    ("Gesamtzahl der Gruppen aus der Personenzahl und der mittleren Gruppengröße unter einer vereinfachenden Annahme schätzen", "Stochastik", "Kenngrößen von Verteilungen",
     "Aus einer Verteilung der Gruppengrößen mit offener oberer Klasse unter einer genannten Annahme die mittlere Gruppengröße als gewichtetes Mittel berechnen und die Gesamtzahl der Personen dadurch teilen.", "2017MerhoehtBStochastikCAS1-5"),
    ("Fehlentscheidungen eines Tests im Sachzusammenhang beschreiben", "Stochastik", "Hypothesentests",
     "Für eine vorgegebene Entscheidungsregel beide möglichen Fehlentscheidungen (wahrer Anteil und Entscheidung passen nicht zusammen) in Worten des Sachzusammenhangs beschreiben.", "2017MerhoehtBStochastikCAS2-3a"),
    ("Ablehnungsgrenze bei größerem Stichprobenumfang ohne höheren Fehler erster Art bestimmen", "Stochastik", "Hypothesentests",
     "Die Irrtumswahrscheinlichkeit einer bestehenden Entscheidungsregel berechnen und für einen größeren Stichprobenumfang die kleinste Grenze bestimmen, deren Irrtumswahrscheinlichkeit nicht größer ist.", "2017MerhoehtBStochastikCAS2-3b"),
    ("Standardabweichung einer Normalverteilung aus einer vorgegebenen Wahrscheinlichkeit bei festem Erwartungswert ermitteln", "Stochastik", "Normalverteilung und Sigma-Regeln",
     "Bei festem Erwartungswert die Standardabweichung einer Normalverteilung so bestimmen, dass eine Intervallwahrscheinlichkeit einen vorgegebenen (etwa halbierten) Wert annimmt.", "2017MerhoehtBStochastikCAS2-3c"),
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
