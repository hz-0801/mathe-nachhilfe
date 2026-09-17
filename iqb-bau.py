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
    "stapel": "2019-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dateidublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2019MgrundlegendBAnalysisWTR1": 40, "2019MgrundlegendBAnalysisWTR2": 40, "2019MgrundlegendBAGLAA1WTR": 20, "2019MgrundlegendBAGLAA2WTR1": 20,
        "2019MgrundlegendBAGLAA2WTR2": 20, "2019MgrundlegendBStochastikWTR1": 20, "2019MgrundlegendBStochastikWTR2": 20, "2019MgrundlegendBStochastikWTR3": 20,
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
# Stapel 2019-ga-B (WTR-Zweig; Reserve, geöffnet 17.09.2026 in Auftrag C Teil 2 wegen der
# neun Landesheftverweise von 2019-be-gk 3.2 a–f auf AG/LA (A2) WTR 1 und 4.1 c–e auf
# Stochastik WTR 1). Acht Dateien (die sechs CAS-Dateien bleiben Reserve), Standardbezug
# mit Spalte Anforderungsbereich; Analysis je 40 BE, die übrigen 20 BE. AG/LA (A1),
# AG/LA (A2) 1 und 2 sowie Stochastik 1 ohne Aufgabennummer (innen 1).
# ---- Analysis WTR 1: Laktatkonzentration k(x) = 1/40 · (x³ − 30x² + 288x − 815); Aufgabe 1 (a–d, 11 BE), 2 Geraden durch W (a–f, 18 BE), 3 h (a–d, 11 BE)
L1 = ("k(x) = 1/40 · (x³ − 30x² + 288x − 815), in IR definiert; Abbildung 1 zeigt den Graphen; Laktattest: für 8,5 ≤ x ≤ 17,5 beschreibt k die "
      "Laktatkonzentration in mmol/l in Abhängigkeit von der Geschwindigkeit x in km/h")
L1_SK = ("Abb. 1: Koordinatensystem auf Gitter, x von 0 bis 17, y von 0 bis 10 (Schritte 2): Graph von k von links unten steigend, flacher Bogen mit "
         "Hochpunkt bei etwa (8 | 2), Tiefpunkt bei etwa (12 | 1,6), danach steil steigend über (16 | 8)")
row("2019MgrundlegendBAnalysisWTR1", "a", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Prozentuale Abweichung eines Modellwerts vom Messwert berechnen", typ_neben="",
    stichwoerter="k(13) ≈ 1,40|(k(13) − 1,44)/1,44 ≈ −0,028|Abweichung etwa 2,8 %",
    voraussetzungen="Funktionswert berechnen|relative Abweichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle: Geschwindigkeit 9, 13, 17 km/h – Laktatkonzentration 1,92, 1,44, 8,09 mmol/l", kontext="Laktattest / Laufband", textumfang="mittel",
    gegeben=L1 + "; Messwerte: 9 km/h 1,92, 13 km/h 1,44, 17 km/h 8,09 mmol/l",
    gesucht="prozentuale Abweichung des Modellwerts bei 13 km/h vom Messwert",
    verfahren="k(13) berechnen und die Differenz auf den Messwert beziehen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="mmol/l", abhaengig_von="",
    ergebnis="(k(13) − 1,44)/1,44 ≈ −0,028, d. h. die Abweichung beträgt etwa 2,8 % (amtlich)",
    zwischenergebnis="k(13) = 1,4", niveau_geschaetzt="I",
    fehlerquelle="Abweichung auf den Modellwert statt auf den Messwert beziehen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (k(13) = 1,4).")
row("2019MgrundlegendBAnalysisWTR1", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Tiefstelle und Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen", typ_neben="",
    stichwoerter="Anstieg ab dem Tiefpunkt bei x = 12|3,25 wird bei x = 15 überschritten (Ablesen)",
    voraussetzungen="Tiefpunkt am Graphen|Stelle zu einem y-Wert ablesen",
    format="Kurzantwort", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=L1_SK, kontext="Laktattest / Laufband", textumfang="kurz",
    gegeben=L1,
    gesucht="Geschwindigkeit, ab der die Konzentration ansteigt; Geschwindigkeit, bei der 3,25 mmol/l überschritten werden",
    verfahren="Tiefpunkt und Stelle zu y = 3,25 aus Abbildung 1 ablesen",
    schritte="2", zahlenraum="dezimal", einheiten="km/h", abhaengig_von="",
    ergebnis="Ab 12 km/h steigt die Laktatkonzentration an, bei 15 km/h überschreitet sie 3,25 mmol/l (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den Hochpunkt bei 8 als Beginn des Anstiegs nehmen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (k'(12) = 0, k(15) = 3,25).")
row("2019MgrundlegendBAnalysisWTR1", "c", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen", typ_neben="",
    stichwoerter="k'(x) = 1/40 · (3x² − 60x + 288), k''(x) = 1/40 · (6x − 60) = 0 ⇔ x = 10|mit dem Graphen: bei 10 km/h nimmt die Konzentration am stärksten ab",
    voraussetzungen="stärkste Abnahme als Minimum von k' bzw. Wendestelle|zweite Ableitung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=L1_SK, kontext="Laktattest / Laufband", textumfang="kurz",
    gegeben=L1,
    gesucht="Geschwindigkeit, bei der die Laktatkonzentration im Modell am stärksten abnimmt",
    verfahren="k'' = 0 lösen und mit dem Graphen als Stelle stärkster Abnahme bestätigen",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="km/h", abhaengig_von="",
    ergebnis="k'(x) = 1/40 · (3x² − 60x + 288), k''(x) = 1/40 · (6x − 60) = 0 ⇔ x = 10; unter Berücksichtigung des Graphen nimmt die Konzentration bei 10 km/h am stärksten ab (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Nullstelle von k' statt von k'' suchen",
    bemerkung="Standardbezug: K1 I, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2022-ea-B).")
row("2019MgrundlegendBAnalysisWTR1", "d", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate über ein Intervall berechnen", typ_neben="",
    stichwoerter="(k(17,5) − k(12))/(17,5 − 12) ≈ 1,6|mittlere Änderungsrate etwa 1,6 mmol/l je km/h",
    voraussetzungen="Differenzenquotient",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Laktattest / Laufband", textumfang="kurz",
    gegeben=L1,
    gesucht="mittlere Änderungsrate der Laktatkonzentration zwischen 12,0 und 17,5 km/h",
    verfahren="Differenzenquotient von k über [12; 17,5]",
    schritte="2", zahlenraum="dezimal", einheiten="mmol/l je km/h", abhaengig_von="",
    ergebnis="(k(17,5) − k(12))/(17,5 − 12) ≈ 1,6, d. h. die mittlere Änderungsrate beträgt etwa 1,6 mmol/l pro km/h (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="k'(17,5) − k'(12) rechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (1,594).")
W1 = L1 + "; der Graph ist symmetrisch bezüglich seines Wendepunkts W(10 | 13/8); betrachtet werden Geraden durch W"
row("2019MgrundlegendBAnalysisWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Steigungen der Geraden durch den Wendepunkt mit genau einem gemeinsamen Punkt über die Wendetangente eingrenzen", typ_neben="",
    stichwoerter="Wendetangente hat die Steigung k'(10) = −0,3|Geraden durch W mit Steigung m ≤ −0,3 schneiden den Graphen nur in W (Graph liegt links über, rechts unter der Geraden)|alle m ∈ ]−∞; −0,3]",
    voraussetzungen="Wendetangente als Grenzfall|Lage des Graphen zu Geraden durch den Wendepunkt",
    format="Rechnung|Begründung", operator="Ermitteln Sie", antwort="Term",
    material="Koordinatensystem", skizze=L1_SK, kontext="ohne", textumfang="mittel",
    gegeben=W1 + "; eine Gerade durch W mit negativer Steigung hat mit dem Graphen keinen weiteren Punkt gemeinsam",
    gesucht="alle möglichen Steigungen dieser Geraden",
    verfahren="k'(10) als Steigung der Wendetangente berechnen; mit dem Graphen begründen, dass alle steileren fallenden Geraden nur W treffen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="k'(10) = −0,3; unter Berücksichtigung des Graphen von k ergibt sich ]−∞; −0,3] (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur die Wendetangente selbst angeben oder den Rand −0,3 ausschließen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAnalysisWTR1", "b", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: y-Achsenabschnitt einer Geraden durch einen festen Punkt als Term in der Steigung angeben", typ_neben="",
    stichwoerter="y = mx + n durch W: 13/8 = 10m + n|n = 13/8 − 10m",
    voraussetzungen="Geradengleichung|Punkt einsetzen und nach n auflösen",
    format="Rechnung", operator="Stellen Sie auf", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=W1,
    gesucht="Term für den y-Achsenabschnitt n einer Geraden durch W in Abhängigkeit von der Steigung m",
    verfahren="W in y = mx + n einsetzen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="13/8 = m · 10 + n ⇔ n = −10m + 13/8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="n = 10m + 13/8 (Vorzeichen)",
    bemerkung="Standardbezug: K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung I (Punkt einsetzen); der amtliche Bereich ist II.")
row("2019MgrundlegendBAnalysisWTR1", "c", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Punktprobe an einer Geraden rechnerisch zeigen und Gerade einzeichnen", typ_neben="",
    stichwoerter="g(x) = 13/40 · (x − 5), g(10) = 13/40 · 5 = 13/8: W liegt auf g|Gerade durch (5 | 0) und W in Abbildung 1",
    voraussetzungen="Funktionswert einer Geraden|Gerade aus zwei Punkten zeichnen",
    format="Rechnung|Zeichnen", operator="Zeigen Sie|Zeichnen Sie", antwort="Text|Grafik",
    material="Koordinatensystem", skizze=L1_SK, kontext="ohne", textumfang="kurz",
    gegeben=W1 + "; g(x) = 13/40 · (x − 5), in IR definiert",
    gesucht="rechnerischer Nachweis, dass der Graph von g durch W verläuft; Gerade in Abbildung 1",
    verfahren="g(10) berechnen; Gerade über die Nullstelle 5 und W zeichnen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="13/40 · (10 − 5) = 13/8 (amtlich); Zeichnung der Geraden durch (5 | 0) und W",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Steigung 13/40 beim Zeichnen falsch abtragen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAnalysisWTR1", "d", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Lösungen einer Differenzgleichung als Schnittstellen zweier Graphen grafisch beschreiben und angeben", typ_neben="",
    stichwoerter="k(x) − g(x) = 0 ⇔ k(x) = g(x): Schnittstellen der Graphen von k und g|aus Abbildung 1: x₁ = 5, x₂ = 10, x₃ = 15",
    voraussetzungen="Differenz null als Gleichheit der Funktionswerte|Schnittstellen ablesen",
    format="Begründung|Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text|Zahl",
    material="Koordinatensystem", skizze=L1_SK, kontext="ohne", textumfang="kurz",
    gegeben=W1 + "; g(x) = 13/40 · (x − 5); Gleichung k(x) − g(x) = 0",
    gesucht="grafisches Verfahren zur Lösung; die Lösungen",
    verfahren="Schnittstellen der Graphen von k und g in Abbildung 1 ablesen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2019MgrundlegendBAnalysisWTR1-2c",
    ergebnis="Die Lösungen sind die x-Koordinaten der Schnittpunkte der Graphen von k und g: x₁ = 5, x₂ = 10, x₃ = 15 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur den Schnittpunkt W nennen",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (k − g = 1/40 · (x − 5)(x − 10)(x − 15)).")
row("2019MgrundlegendBAnalysisWTR1", "e", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral über die Punktsymmetrie zum Wendepunkt als Dreiecksfläche unter einer Sekante begründen", typ_neben="",
    stichwoerter="k und g schneiden sich in 5, 10 (= W), 15; wegen der Punktsymmetrie zu W sind die beiden Flächenstücke zwischen k und g gleich groß|∫₅¹⁵ k = ∫₅¹⁵ g = Dreieck mit Katheten 15 − 5 und g(15) = k(15)|1/2 · (15 − 5) · k(15)",
    voraussetzungen="Punktsymmetrie überträgt Flächenstücke|Integral einer Geraden als Dreiecksfläche",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=L1_SK, kontext="ohne", textumfang="kurz",
    gegeben=W1 + "; g durch W mit Schnittstellen 5, 10, 15; Behauptung ∫₅¹⁵ k(x) dx = 1/2 · (15 − 5) · k(15)",
    gesucht="Begründung ohne Rechnung",
    verfahren="Flächengleichheit der beiden Stücke zwischen k und g aus der Symmetrie, Fläche unter g als rechtwinkliges Dreieck",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2019MgrundlegendBAnalysisWTR1-2d",
    ergebnis="Wegen der Symmetrie des Graphen von k bezüglich W haben die beiden von k und g eingeschlossenen Flächenstücke gleichen Inhalt; also stimmt die Fläche unter k über [5; 15] mit der unter g überein, einem rechtwinkligen Dreieck mit den Katheten 15 − 5 und k(15) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das Integral über k ausrechnen statt zu begründen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (beide Seiten 65/16).")
row("2019MgrundlegendBAnalysisWTR1", "f", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Existenz einer Grenze mit Integralwert null über den Vorzeichenwechsel und die Stetigkeit am Graphen begründen", typ_neben="",
    stichwoerter="k < 0 für x < 5, k > 0 für x > 5|∫_z^(z+1) k: für z = 4 negativ, für z = 5 positiv|der Wert wächst mit z stetig, also Nullstelle dazwischen",
    voraussetzungen="Vorzeichen des Integranden aus dem Graphen|Integral als stetige Funktion der Grenze",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=L1_SK, kontext="ohne", textumfang="kurz",
    gegeben=W1 + "; Behauptung: es gibt z mit 4 < z < 5 und ∫_z^(z+1) k(x) dx = 0",
    gesucht="Begründung mithilfe von Abbildung 1",
    verfahren="Vorzeichen des Integrals für z = 4 und z = 5 vergleichen, Monotonie und Stetigkeit in z nutzen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Für x < 5 ist k negativ, für x > 5 positiv; das Integral ist für z = 4 negativ und für z = 5 positiv und nimmt für 4 ≤ z ≤ 5 kontinuierlich zu (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="ein konkretes z ausrechnen wollen",
    bemerkung="Standardbezug: K1 II, K4 I, K6 II. AB amtlich: II. Amtlich; eigene Rechnung: z ≈ 4,49.")
H1 = "h(x) = 40/13 · 1/(x − 5), x ≠ 5; Abbildung 2 zeigt den Graphen von h; g(x) = 13/40 · (x − 5) aus Aufgabe 2"
H1_SK = "Abb. 2: Koordinatensystem x von −1 bis 9, y von −2 bis 4: Hyperbel mit senkrechter Asymptote x = 5, linker Ast unter der x-Achse, rechter Ast darüber"
row("2019MgrundlegendBAnalysisWTR1", "a", innen="3", seite="3", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Verschiebung und Streckung der Grundhyperbel aus dem Term beschreiben", typ_neben="",
    stichwoerter="i(x) = 1/x|Verschiebung um 5 in positive x-Richtung, Streckung mit dem Faktor 40/13 in y-Richtung",
    voraussetzungen="Parameter einer Transformation am Term ablesen",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=H1_SK, kontext="ohne", textumfang="kurz",
    gegeben=H1 + "; i(x) = 1/x, x ≠ 0",
    gesucht="Beschreibung, wie der Graph von h aus dem Graphen von i hervorgeht",
    verfahren="Verschiebung aus (x − 5), Streckfaktor 40/13 ablesen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Verschiebung um 5 in positive x-Richtung und Streckung mit dem Faktor 40/13 in y-Richtung (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Verschiebung um −5 angeben",
    bemerkung="Standardbezug: K1 II, K4 II, K6 I. AB amtlich: II. Amtlich. Schätzung I (Parameter ablesen); der amtliche Bereich ist II.")
row("2019MgrundlegendBAnalysisWTR1", "b", innen="3", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Schnittpunkte einer Geraden mit einer Hyperbel über eine quadratische Gleichung berechnen", typ_neben="",
    stichwoerter="g(x) = h(x) ⇔ (x − 5)² = (40/13)²|x = 5 ± 40/13: x = 25/13 oder x = 105/13|Punkte (25/13 | −1) und (105/13 | 1)",
    voraussetzungen="Gleichsetzen und Umstellen zu (x − 5)² = c|Wurzelziehen mit beiden Vorzeichen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=H1_SK, kontext="ohne", textumfang="kurz",
    gegeben=H1,
    gesucht="Koordinaten der beiden gemeinsamen Punkte der Graphen von g und h",
    verfahren="g = h zu (x − 5)² = (40/13)² umformen und lösen, y-Werte berechnen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="g(x) = h(x) ⇔ (x − 5)² = (40/13)² ⇔ x = 25/13 ∨ x = 105/13; Punkte (25/13 | −1) und (105/13 | 1) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur die positive Wurzel nehmen",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAnalysisWTR1", "c", innen="3", seite="3", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Fehlen einer gemeinsamen Tangente zweier Graphen über die Vorzeichen der Steigungen begründen", typ_neben="",
    stichwoerter="h'(x) = −40/13 · 1/(x − 5)² < 0 für alle x ≠ 5|g hat die Steigung 13/40 > 0|eine gemeinsame Tangente müsste beide Steigungen haben",
    voraussetzungen="Steigung einer Hyperbel überall negativ|Steigung einer Geraden",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=H1,
    gesucht="Begründung, dass es keine Gerade gibt, die Tangente an beide Graphen ist",
    verfahren="Vorzeichen der Steigungen vergleichen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Für alle x ≠ 5 ist die Steigung des Graphen von h negativ, die des Graphen von g positiv (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit den Schnittpunkten aus b argumentieren",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. AB amtlich: II. Amtlich.")
row("2019MgrundlegendBAnalysisWTR1", "d", innen="3", seite="3", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Grenzen für ein positives Produkt zweier Integrale über die Vorzeichen der Hyperbeläste angeben und begründen", typ_neben="",
    stichwoerter="links von 5 ist h negativ: Integral über [a; b] ⊂ ]−∞; 5[ mit a < b negativ|rechts von 5 ist h positiv: Integral über [c; d] mit c > d (vertauschte Grenzen) negativ|z. B. a = 1, b = 3, c = 9, d = 6: Produkt zweier negativer Werte positiv",
    voraussetzungen="Vorzeichen eines Integrals aus dem Vorzeichen des Integranden|Vertauschen der Grenzen wechselt das Vorzeichen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="Koordinatensystem", skizze=H1_SK, kontext="ohne", textumfang="mittel",
    gegeben=H1 + "; a, b ∈ ]−∞; 5[ und c, d ∈ ]5; +∞[ mit ∫_a^b h(x) dx · ∫_c^d h(x) dx > 0",
    gesucht="eine Möglichkeit für a, b, c, d mit Begründung",
    verfahren="Vorzeichen beider Integrale über Vorzeichen von h und Reihenfolge der Grenzen steuern",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="z. B. a = 1, b = 3, c = 9, d = 6; für diese Werte sind beide Integrale negativ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="c < d wählen und ein positives mal negatives Integral erhalten",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (beide Integrale negativ, Produkt ≈ 1,37).")
# ---- Analysis WTR 2: Parabelschar f_k(x) = −kx(x − 8) (1 a–j, 31 BE) und CO₂-Konzentration g(x) = −600e^(−0,5x) + 1000 (2 a–d, 9 BE)
P1 = "Schar f_k(x) = −kx · (x − 8), k > 0, in IR definiert; Graph G_k"
P1_SK = ("Koordinatensystem auf Gitter, x von −1 bis 9, y von −1 bis 4: Graph von f_(1/4), nach unten geöffnete Parabel durch (0 | 0) und (8 | 0) mit Hochpunkt (4 | 4)")
row("2019MgrundlegendBAnalysisWTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Nullstellen einer Schar am faktorisierten Term angeben", typ_neben="",
    stichwoerter="−kx(x − 8) = 0 ⇔ x = 0 ∨ x = 8, unabhängig von k",
    voraussetzungen="Produkt gleich null",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=P1,
    gesucht="Nullstellen von f_k",
    verfahren="Faktoren null setzen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="x₁ = 0 und x₂ = 8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Nullstelle 8 mit Vorzeichen −8 lesen",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAnalysisWTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Hochpunkt einer Parabelschar mit Parameterkoordinaten nachweisen", typ_neben="",
    stichwoerter="G_k nach unten geöffnete Parabel (k > 0)|Scheitel in der Mitte der Nullstellen bei x = 4|f_k(4) = 16k",
    voraussetzungen="Öffnung einer Parabel am Vorzeichen|Scheitel symmetrisch zwischen den Nullstellen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=P1 + "; Nullstellen 0 und 8",
    gesucht="Begründung, dass (4 | 16k) der Hochpunkt von G_k ist",
    verfahren="Öffnung und Symmetrie der Parabel nutzen, f_k(4) berechnen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2019MgrundlegendBAnalysisWTR2-1a",
    ergebnis="G_k ist eine nach unten geöffnete Parabel; wegen der Lage der Nullstellen liegt der Hochpunkt bei x = 4, und f_k(4) = 16k (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="mit f'' rechnen und k > 0 nicht nennen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-ea-B).")
row("2019MgrundlegendBAnalysisWTR2", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Abstand der Hochpunkte zweier benachbarter Scharparabeln berechnen", typ_neben="",
    stichwoerter="Hochpunkte (4 | 16k) und (4 | 16(k + 1))|Abstand 16(k + 1) − 16k = 16",
    voraussetzungen="Hochpunkt aus b|gleiche x-Koordinate: Abstand als Differenz der y-Werte",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=P1 + "; Hochpunkt von G_k ist (4 | 16k)",
    gesucht="Abstand der Hochpunkte von G_k und G_(k+1)",
    verfahren="y-Koordinaten der Hochpunkte subtrahieren",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2019MgrundlegendBAnalysisWTR2-1b",
    ergebnis="16 · (k + 1) − 16k = 16 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den Abstand als 16k angeben",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAnalysisWTR2", "d", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem vorgegebenen Flächeninhalt zwischen Graph und x-Achse berechnen", typ_neben="",
    stichwoerter="∫₀⁸ f_k(x) dx = k · [−1/3 x³ + 4x²]₀⁸ = 256/3 · k|256/3 · k = 64/3 ⇔ k = 1/4",
    voraussetzungen="Fläche zwischen Parabel und x-Achse als Integral zwischen den Nullstellen|Stammfunktion mit Parameter|lineare Gleichung in k",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=P1 + "; die Fläche zwischen G_k und der x-Achse hat den Inhalt 64/3",
    gesucht="dieser Wert von k",
    verfahren="Integral von 0 bis 8 als Term in k, gleich 64/3 setzen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2019MgrundlegendBAnalysisWTR2-1a",
    ergebnis="∫₀⁸ f_k(x) dx = k · [−1/3 x³ + 4x²]₀⁸ = 256/3 · k = 64/3 ⇔ k = 1/4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen beim Ausmultiplizieren von −kx(x − 8)",
    bemerkung="Standardbezug: K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B).")
row("2019MgrundlegendBAnalysisWTR2", "e", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Maximumstelle aller Stammfunktionen über den Vorzeichenwechsel des Integranden begründen", typ_neben="",
    stichwoerter="F' = f_(1/4)|f_(1/4) > 0 für 0 < x < 8, f_(1/4) < 0 für x > 8|Maximum jeder Stammfunktion bei x = 8",
    voraussetzungen="Stammfunktion hat die Funktion als Ableitung|Maximum beim Vorzeichenwechsel + → −",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="Koordinatensystem", skizze=P1_SK, kontext="ohne", textumfang="kurz",
    gegeben=P1 + "; k = 1/4",
    gesucht="Stelle, an der jede Stammfunktion von f_(1/4) ihr Maximum annimmt, mit Begründung ohne Stammfunktionsterm",
    verfahren="Vorzeichen von f_(1/4) links und rechts von 8 als Monotonie der Stammfunktion deuten",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Für jede Stammfunktion F gilt F' = f_(1/4); da f_(1/4) > 0 für 0 < x < 8 und < 0 für x > 8, nimmt F ihr Maximum bei x = 8 an (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Maximum der Stammfunktion an der Hochstelle 4 von f vermuten",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich.")
T1 = P1 + "; k = 1/4; Trapeze mit den Ecken A(0 | 0), B(8 | 0), C_u(8 − u | f_(1/4)(u)) und D_u(u | f_(1/4)(u)) für 0 < u < 4"
row("2019MgrundlegendBAnalysisWTR2", "f", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Einbeschriebenes Trapez zu einem Parameterwert in die Abbildung einzeichnen", typ_neben="",
    stichwoerter="u = 1: D₁(1 | 7/4), C₁(7 | 7/4)|Trapez A B C₁ D₁ in die Abbildung",
    voraussetzungen="Funktionswert f_(1/4)(1) = 7/4|Punkte übertragen",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=P1_SK, kontext="ohne", textumfang="mittel",
    gegeben=T1,
    gesucht="Trapez für u = 1 in der Abbildung",
    verfahren="D₁ und C₁ berechnen und mit A, B verbinden",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Zeichnung: Trapez mit den Ecken (0 | 0), (8 | 0), (7 | 1,75), (1 | 1,75) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="C₁ bei x = 8 − u falsch lesen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (f(1) = 7/4).")
row("2019MgrundlegendBAnalysisWTR2", "g", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Term für die Schenkellänge eines einbeschriebenen Trapezes aufstellen", typ_neben="",
    stichwoerter="Schenkel AD_u von (0 | 0) nach (u | f(u))|Länge √(u² + (f_(1/4)(u))²)",
    voraussetzungen="Abstand zweier Punkte|Symmetrie des Trapezes",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Koordinatensystem", skizze=P1_SK, kontext="ohne", textumfang="kurz",
    gegeben=T1,
    gesucht="Term für die Länge der beiden gleich langen Schenkel",
    verfahren="Abstand A–D_u mit dem Satz des Pythagoras",
    schritte="1", zahlenraum="Wurzel", einheiten="", abhaengig_von="",
    ergebnis="√(u² + (f_(1/4)(u))²) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Schenkel als 8 − 2u (Differenz der parallelen Seiten) verwechseln",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich.")
row("2019MgrundlegendBAnalysisWTR2", "h", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Flächenterm eines einbeschriebenen Trapezes über die Mittelparallele geometrisch herleiten", typ_neben="",
    stichwoerter="Fläche = Mittelparallele mal Höhe|parallele Seiten 8 und 8 − 2u, Mittelwert 8 − u|Höhe f_(1/4)(u)|(8 − u) · f_(1/4)(u)",
    voraussetzungen="Trapezformel über die Mittelparallele|Längen der parallelen Seiten aus den Koordinaten",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=P1_SK, kontext="ohne", textumfang="kurz",
    gegeben=T1 + "; Flächenterm (8 − u) · f_(1/4)(u)",
    gesucht="geometrische Überlegung, mit der sich der Term herleiten lässt",
    verfahren="Mittelparallele als Mittelwert von 8 und 8 − 2u, Höhe als Funktionswert",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Der Flächeninhalt ist das Produkt aus der Länge der Mittelparallele, dem Mittelwert 8 − u der parallelen Seiten 8 und 8 − 2u, und der Höhe f_(1/4)(u) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Term als Rechteck 8 − u mal Höhe deuten",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. AB amtlich: II. Amtlich.")
row("2019MgrundlegendBAnalysisWTR2", "i", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Parameter für den größten Flächeninhalt über die Ableitung bestimmen", typ_neben="",
    stichwoerter="T(u) = (8 − u) · f_(1/4)(u) = 1/4 · u³ − 4u² + 16u|T'(u) = 3/4 u² − 8u + 16 = 0 ⇔ u = 8/3 ∨ u = 8|mit 0 < u < 4: u = 8/3",
    voraussetzungen="Zielfunktion ausmultiplizieren|notwendige Bedingung|Definitionsbereich beachten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=T1 + "; Flächeninhalt (8 − u) · f_(1/4)(u); eines der Trapeze hat den größten Inhalt",
    gesucht="zugehöriger Wert von u",
    verfahren="T(u) aufstellen, T' = 0 lösen, Lösung im Intervall wählen",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="2019MgrundlegendBAnalysisWTR2-1h",
    ergebnis="T(u) = (8 − u) · f_(1/4)(u) = 1/4 · u³ − 4u² + 16u; T'(u) = 3/4 u² − 8u + 16 = 0 ⇔ u = 8/3 ∨ u = 8; mit u ∈ ]0; 4[ ergibt sich u = 8/3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="u = 8 als Lösung nehmen; hinreichende Bedingung vergessen",
    bemerkung="Standardbezug: K2 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (T''(8/3) < 0). Typ wiederverwendet (2020-ea-A).")
row("2019MgrundlegendBAnalysisWTR2", "j", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Mittelpunkt des Kreises durch drei Punkte der Ebene über Mittelsenkrechte und Abstandsgleichung berechnen", typ_neben="",
    stichwoerter="Mittelpunkt auf der Mittelsenkrechten von AB: x = 4|gleicher Abstand zu A und E(4 | 8): 4² + y² = (8 − y)² ⇔ y = 3|M(4 | 3)",
    voraussetzungen="Umkreismittelpunkt auf den Mittelsenkrechten|Abstandsgleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Punkte A(0 | 0), B(8 | 0) und E(4 | 8) auf einem Kreis",
    gesucht="Koordinaten des Kreismittelpunkts",
    verfahren="x = 4 aus der Symmetrie, y aus |MA| = |ME|",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Der Mittelpunkt liegt auf der Mittelsenkrechten von A und B (x = 4); aus 4² + y² = (8 − y)² folgt y = 3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="den Mittelpunkt in den Schwerpunkt (4 | 8/3) legen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Radius 5). Ebene Geometrie in einer Analysis-Datei; Thema nach der Fertigkeit (Punkte und Strecken, Klasse Punkt), nicht nach dem Sachgebiet der Datei.")
C2 = ("CO₂-Konzentration in einem Raum: g(x) = −600 · e^(−0,5x) + 1000, in IR definiert, x Zeit in Stunden seit Beginn der Untersuchung, g(x) in ppm")
row("2019MgrundlegendBAnalysisWTR2", "a", innen="2", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Anfangswert eines Bestands als Funktionswert an der Stelle null berechnen", typ_neben="",
    stichwoerter="g(0) = −600 + 1000 = 400 ppm",
    voraussetzungen="Funktionswert an der Stelle 0",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Raumluft / CO₂", textumfang="mittel",
    gegeben=C2,
    gesucht="CO₂-Konzentration zu Beginn der Untersuchung",
    verfahren="g(0) berechnen",
    schritte="1", zahlenraum="ganz", einheiten="ppm", abhaengig_von="",
    ergebnis="g(0) = 400, d. h. die Konzentration beträgt zu Beginn 400 ppm (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="e⁰ = 0 setzen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAnalysisWTR2", "b", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Einhalten einer Schranke über das Vorzeichen des e-Terms begründen", typ_neben="",
    stichwoerter="e^(−0,5x) > 0 für alle x|g(x) = 1000 − 600e^(−0,5x) < 1000: Bedingung erfüllt",
    voraussetzungen="Positivität der e-Funktion|Abschätzung eines Terms",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Raumluft / CO₂", textumfang="kurz",
    gegeben=C2 + "; Wohlfühlbedingung: Konzentration unter 1000 ppm",
    gesucht="ob die Bedingung während der Untersuchung erfüllt war",
    verfahren="g(x) < 1000 aus e^(−0,5x) > 0 folgern",
    schritte="1", zahlenraum="ganz", einheiten="ppm", abhaengig_von="",
    ergebnis="Wegen e^(−0,5x) > 0 gilt g(x) < 1000, die Bedingung war erfüllt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Grenzwert 1000 als erreicht ansehen",
    bemerkung="Standardbezug: K1 II, K3 I, K5 II. AB amtlich: II. Amtlich.")
row("2019MgrundlegendBAnalysisWTR2", "c", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Zeitliche Entwicklung eines Bestands über ein Intervall grafisch darstellen", typ_neben="",
    stichwoerter="Graph von g für 0 ≤ x ≤ 10: von 400 ansteigend, abflachend gegen 1000 (g(10) ≈ 996)",
    voraussetzungen="Wertetabelle oder Rechner|beschränktes Wachstum skizzieren",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Raumluft / CO₂", textumfang="kurz",
    gegeben=C2,
    gesucht="grafische Darstellung der Konzentration für die ersten zehn Stunden",
    verfahren="Koordinatensystem mit passender Skalierung, Graph von g zeichnen",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="ppm", abhaengig_von="",
    ergebnis="Zeichnung: sättigender Anstieg von (0 | 400) gegen 1000 ppm (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="y-Achse nicht bei 0 beginnen lassen ohne Kennzeichnung",
    bemerkung="Standardbezug: K4 I. AB amtlich: I. Amtlich.")
row("2019MgrundlegendBAnalysisWTR2", "d", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Term für die mittlere Änderungsrate über Einheitsintervalle nachweisen und Zeitpunkt des Unterschreitens einer Schranke berechnen", typ_neben="",
    stichwoerter="(g(x + 1) − g(x))/1 = −600e^(−0,5(x+1)) + 600e^(−0,5x) = 600 · (1 − 1/√e) · e^(−0,5x)|600 · (1 − 1/√e) · e^(−0,5x) = 100 ⇔ x = −2 · ln(1/(6 · (1 − 1/√e))) ≈ 1,72|erstmals etwa 103 Minuten nach Beginn",
    voraussetzungen="Differenzenquotient über Länge 1|Potenzgesetze für e^(−0,5(x+1))|Exponentialgleichung mit ln",
    format="Rechnung", operator="Zeigen Sie|Berechnen Sie", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="Raumluft / CO₂", textumfang="mittel",
    gegeben=C2 + "; Behauptung: die mittlere Änderungsrate über jede Stunde ist 600 · (1 − 1/√e) · e^(−0,5x)",
    gesucht="Nachweis des Terms; Zeitpunkt auf eine Minute genau, ab dem die mittlere Änderungsrate erstmals 100 ppm/h unterschreitet",
    verfahren="g(x + 1) − g(x) umformen und ausklammern; Gleichung mit 100 nach x lösen, in Minuten umrechnen",
    schritte="4", zahlenraum="dezimal|Potenz", einheiten="ppm/h, Minuten", abhaengig_von="",
    ergebnis="(g(x + 1) − g(x))/1 = 600 · (1 − 1/√e) · e^(−0,5x); 600 · (1 − 1/√e) · e^(−0,5x) = 100 ⇔ x = −2 · ln(1/(6 · (1 − 1/√e))) ≈ 1,72, also erstmals etwa 103 Minuten nach Beginn (amtlich)",
    zwischenergebnis="1 − 1/√e ≈ 0,393", niveau_geschaetzt="III",
    fehlerquelle="1/√e als e^(−0,5) nicht erkennen; 1,72 h als 1 h 72 min lesen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (x ≈ 1,716 h ≈ 103 min).")
# ---- AG/LA (A1) WTR: Tretbootverleih, Stationen N, S, W (a–f, 20 BE), Aufgabe ohne Nummer (innen 1)
B1 = ("Tretbootverleih mit den Stationen N, S, W; Ausgaben a = (n; s; w), Rückgaben r = (n; s; w) je Tag; r = M · a mit "
      "M = (0,6 0,1 0,2 / 0,1 0,75 0,05 / 0,3 0,15 0,75)")
row("2019MgrundlegendBAGLAA1WTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag und Spaltensumme eins im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="0,05 in Zeile S, Spalte W: Anteil der an W ausgegebenen Boote, die an S zurückgegeben werden|Spaltensumme 1: jedes ausgegebene Boot wird an einer der drei Stationen zurückgegeben",
    voraussetzungen="Zeile = Ziel, Spalte = Ausgangsstation|Spaltensumme als Vollständigkeit",
    format="Begründung", operator="Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Tretbootverleih", textumfang="lang",
    gegeben=B1,
    gesucht="Bedeutung des Eintrags 0,05 und der Spaltensummen 1",
    verfahren="Eintrag nach Zeile und Spalte zuordnen, Spaltensumme als Rückgabe aller Boote deuten",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,05 ist der Anteil der an der Station W ausgegebenen Boote, die an der Station S zurückgegeben werden; alle an einer Station ausgegebenen Boote werden zurückgegeben (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeile und Spalte vertauschen (an S ausgegeben, an W zurück)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich.")
row("2019MgrundlegendBAGLAA1WTR", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="drei Zustände N, S, W|Pfeile mit den neun Anteilen spaltenweise: N → N 0,6, N → S 0,1, N → W 0,3; S → N 0,1, S → S 0,75, S → W 0,15; W → N 0,2, W → S 0,05, W → W 0,75",
    voraussetzungen="Spalten der Matrix als Abgänge",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Tretbootverleih", textumfang="kurz",
    gegeben=B1,
    gesucht="Übergangsdiagramm zu r = M · a",
    verfahren="Einträge spaltenweise als Pfeile eintragen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Übergangsdiagramm mit den Stationen N, S, W und allen neun Anteilen (Bleibeanteile 0,6, 0,75, 0,75) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Pfeilrichtung nach Zeilen statt Spalten",
    bemerkung="Standardbezug: K3 I, K4 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2018-ea-A); Quelle die Matrix.")
row("2019MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Aussage über eine Komponente nach einem Übergang bei gleicher Ausgangsverteilung beurteilen", typ_neben="",
    stichwoerter="a = (w; w; w)|Rückgaben an W: 0,3w + 0,15w + 0,75w = 1,2w|20 % mehr als w: richtig",
    voraussetzungen="Zeile mal Vektor|prozentualer Vergleich",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Tretbootverleih", textumfang="mittel",
    gegeben=B1 + "; Aussage: werden an allen drei Stationen gleich viele Boote ausgegeben, so ist an W die Anzahl der Rückgaben 20 % höher als die der Ausgaben",
    gesucht="Beurteilung der Aussage",
    verfahren="Dritte Zeile von M mit (w; w; w) multiplizieren",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist richtig: 0,3w + 0,15w + 0,75w = w + 0,2w (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Spalte W statt der Zeile W summieren (Summe 1)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAGLAA1WTR", "d", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unbekannte Komponente der Ausgangsverteilung aus dem Ergebnisvektor über ein Gleichungssystem ermitteln", typ_neben="",
    stichwoerter="M · (40; s; w) = (40; 37; 63)|I 24 + 0,1s + 0,2w = 40, II 4 + 0,75s + 0,05w = 37, III 12 + 0,15s + 0,75w = 63|aus I und II: s = 40 (w = 60)",
    voraussetzungen="Matrix mal Vektor mit Unbekannten|lineares Gleichungssystem",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Tretbootverleih", textumfang="mittel",
    gegeben=B1 + "; an einem Dienstag an N 40 Ausgaben und 40 Rückgaben, Rückgaben an S 37, an W 63",
    gesucht="Anzahl der an S ausgegebenen Boote",
    verfahren="Gleichungssystem aus r = M · a aufstellen und nach s lösen",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="Boote", abhaengig_von="",
    ergebnis="M · (40; s; w) = (40; 37; 63) liefert I 24 + 0,1s + 0,2w = 40, II 4 + 0,75s + 0,05w = 37, III 12 + 0,15s + 0,75w = 63; aus II 16 + 3s + 0,2w = 148, mit I 8 − 2,9s = −108 ⇔ s = 40 (amtlich)",
    zwischenergebnis="w = 60", niveau_geschaetzt="II",
    fehlerquelle="Rückgabevektor als Ausgabevektor einsetzen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (s = 40, w = 60, III erfüllt).")
row("2019MgrundlegendBAGLAA1WTR", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Gleichung aus gleichen Komponentensummen von Ausgabe- und Rückgabevektor nachweisen und deuten", typ_neben="",
    stichwoerter="Summe der Ausgaben = Summe der Rückgaben (Spaltensummen 1): a + b + (a + b) = (a + 2) + b + c|c = a + b − 2|an W zwei Boote weniger zurückgegeben als ausgegeben",
    voraussetzungen="Gesamtzahl bleibt erhalten|Gleichung umstellen",
    format="Rechnung|Begründung", operator="Zeigen Sie|Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Tretbootverleih", textumfang="mittel",
    gegeben=B1 + "; Samstag: Ausgaben (a; b; a + b), Rückgaben (a + 2; b; c)",
    gesucht="Nachweis von c = a + b − 2 und Deutung im Sachzusammenhang",
    verfahren="Komponentensummen gleichsetzen; Differenz an W deuten",
    schritte="2", zahlenraum="ganz", einheiten="Boote", abhaengig_von="",
    ergebnis="a + b + a + b = a + 2 + b + c ⇔ c = a + b − 2; an der Station W wurden zwei Boote weniger zurückgegeben, als dort ausgegeben wurden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Gleichung über M · a ausrechnen wollen",
    bemerkung="Standardbezug: K2 I, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAGLAA1WTR", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Mögliche Übergangsmatrix aus Ausgabe- und Rückgabezahlen zweier Stationen mit freiem Parameter ermitteln", typ_neben="",
    stichwoerter="Matrix (p 1 − q / 1 − p q) · (15; 10) = (8; 17)|I 15p + 10(1 − q) = 8, II 15(1 − p) + 10q = 17|II folgt aus I (unterbestimmt): z. B. p = 0, q = 0,2",
    voraussetzungen="Spaltensummen 1 als Ansatz|Gleichungssystem mit einem freien Parameter",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Tretbootverleih", textumfang="lang",
    gegeben="Nebensaison nur Stationen N und S; Mittwoch: an N 15 Ausgaben und 8 Rückgaben, an S 10 Ausgaben und 17 Rückgaben",
    gesucht="eine Matrix, die den Zusammenhang zwischen Ausgaben und Rückgaben darstellen kann",
    verfahren="Matrix mit Spaltensummen 1 ansetzen, Gleichungssystem lösen, einen Parameter frei wählen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="(p 1 − q / 1 − p q) · (15; 10) = (8; 17) liefert 15p + 10(1 − q) = 8 und 15(1 − p) + 10q = 17; aus I folgt 10q = 15p + 2, II ist dann erfüllt; z. B. p = 0 und q = 0,2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die Spaltensummen nicht auf 1 setzen und vier Unbekannte erhalten",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (0 ≤ p ≤ 8/15 erlaubt).")
# ---- AG/LA (A2) WTR 1: Würfel ABCDEFGH mit Trapez IJKL (a–f, 20 BE); Landesheft 2019-be-gk 3.2 a–f vorgemerkt
Wf = ("Würfel ABCDEFGH mit G(5 | 5 | 5) und H(0 | 5 | 5) (A im Ursprung, Kantenlänge 5); I(5 | 0 | 1), J(2 | 5 | 0), K(0 | 5 | 2), L(1 | 0 | 5) auf Kanten des Würfels")
Wf_SK = ("Schrägbild des Würfels: A im Ursprung, B auf der x₁-Achse, D auf der x₂-Achse, E auf der x₃-Achse, G(5 | 5 | 5) hinten oben; Gitternetz in der Grundebene, "
         "Achsen bis 6")
row("2019MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Viereck in ein Schrägbild einzeichnen", typ_neben="",
    stichwoerter="I auf BF (x₁ = 5, x₃ = 1), J auf CD (x₂ = 5), K auf DH, L auf EF|Viereck IJKL",
    voraussetzungen="Punkte auf Kanten im Schrägbild verorten",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Körper", skizze=Wf_SK, kontext="ohne", textumfang="kurz",
    gegeben=Wf,
    gesucht="Viereck IJKL in der Abbildung",
    verfahren="Vier Punkte auf den Kanten eintragen und verbinden",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Zeichnung des Vierecks IJKL mit I auf BF, J auf CD, K auf DH, L auf EF (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="J und K auf falschen Kanten (x₂ = 5 ist die hintere Fläche)",
    bemerkung="Standardbezug: K4 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2018-ea-B). Landesheft 2019-be-gk 3.2 a (wortgleich; dort vorgemerkt).")
row("2019MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Trapez mit zwei gleich langen Seiten über Kollinearität und Seitenlängen nachweisen", typ_neben="",
    stichwoerter="IL = (−4; 0; 4) = 2 · JK mit JK = (−2; 0; 2): parallel und doppelt so lang|IJ = (−3; 5; −1), KL = (1; −5; 3): |IJ| = |KL| = √35",
    voraussetzungen="Parallelität über Vielfache|Betrag eines Vektors",
    format="Rechnung", operator="Zeigen Sie|Weisen Sie nach", antwort="Text",
    material="Körper", skizze=Wf_SK, kontext="ohne", textumfang="kurz",
    gegeben=Wf,
    gesucht="Nachweis, dass IJKL ein Trapez mit zwei gleich langen gegenüberliegenden Seiten ist und IL doppelt so lang wie JK",
    verfahren="IL = 2 · JK zeigen; |IJ| und |KL| berechnen",
    schritte="3", zahlenraum="ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="IL = (−4; 0; 4) = 2 · JK, also IL doppelt so lang und parallel zu JK; |IJ| = √(3² + 5² + 1²) = |KL| (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="IJ und KL als die parallelen Seiten annehmen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ aus der Landeszeile 2019-be-gk 3.2 b (abgewandelt: „Begründen Sie“, „zwei Seiten gleich lang“; dort vorgemerkt, Schätzung dort II – Vorrang des Amtlichen, die Landeszeile zieht im Abgleichlauf nach).")
row("2019MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Innenwinkel eines Vierecks über das Skalarprodukt der Seitenvektoren berechnen", typ_neben="",
    stichwoerter="Winkel bei L zwischen LK = (−1; 5; −3) und LI = (4; 0; −4)|cos φ = 8/√1120|φ ≈ 76°",
    voraussetzungen="Winkelformel mit Skalarprodukt",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=Wf_SK, kontext="ohne", textumfang="kurz",
    gegeben=Wf,
    gesucht="Größe eines Innenwinkels des Trapezes IJKL",
    verfahren="Skalarprodukt zweier Seitenvektoren an einer Ecke",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="cos φ = ((−1; 5; −3) · (4; 0; −4)) / (|(−1; 5; −3)| · |(4; 0; −4)|) = 8/√1120 liefert φ ≈ 76° (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vektoren nicht von derselben Ecke aus ansetzen",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (76,2°). Typ aus der Landeszeile 2019-be-gk 3.2 c (wortgleich; dort vorgemerkt, Schätzung dort I). Schätzung I (Winkelformel anwenden); der amtliche Bereich ist II.")
row("2019MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines Trapezes im Raum über die Höhe zwischen den parallelen Seiten berechnen", typ_neben="",
    stichwoerter="symmetrisches Trapez: Höhe = Abstand der Seitenmitten (3 | 0 | 3) und (1 | 5 | 1) = √33|A = 1/2 · (|IL| + |JK|) · √33 = 1/2 · 3 · √8 · √33 = 3√66",
    voraussetzungen="Mittelpunkte der parallelen Seiten|Trapezformel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=Wf_SK, kontext="ohne", textumfang="kurz",
    gegeben=Wf + "; IL ∥ JK, |IL| = 2 · |JK|, |IJ| = |KL|",
    gesucht="Flächeninhalt des Trapezes IJKL",
    verfahren="Höhe als Abstand der Mittelpunkte der parallelen Seiten, Trapezformel",
    schritte="3", zahlenraum="Wurzel", einheiten="", abhaengig_von="2019MgrundlegendBAGLAA2WTR1-1b",
    ergebnis="Höhe = Abstand von (3 | 0 | 3) und (1 | 5 | 1) = √(2² + 5² + 2²); A = 1/2 · (|IL| + |JK|) · √33 = 3√66 (amtlich)",
    zwischenergebnis="√33 ≈ 5,74", niveau_geschaetzt="II",
    fehlerquelle="Schenkellänge √35 als Höhe verwenden",
    bemerkung="Standardbezug: K2 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (24,37). Typ aus der Landeszeile 2019-be-gk 3.2 d (wortgleich; dort vorgemerkt).")
row("2019MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen",
    typ_neben="Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen",
    stichwoerter="T: 5x₁ + 4x₂ + 5x₃ + v = 0|K einsetzen: 20 + 10 + v = 0 ⇔ v = −30|L: 5 + 25 − 30 = 0, L liegt in T",
    voraussetzungen="parallele Ebene mit gleichem Normalenvektor|Punktprobe",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=Wf + "; S: 5x₁ + 4x₂ + 5x₃ = 0; K liegt in einer zu S parallelen Ebene T",
    gesucht="ob auch L in T liegt",
    verfahren="T mit dem Normalenvektor von S durch K aufstellen, L einsetzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="T: 5x₁ + 4x₂ + 5x₃ + v = 0 mit K ∈ T ⇔ v = −30; wegen 5 · 1 + 4 · 0 + 5 · 5 − 30 = 0 liegt auch L in T (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="v aus S statt aus K übernehmen",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typen aus der Landeszeile 2019-be-gk 3.2 e (wortgleich; dort vorgemerkt, Schätzung dort I). Schätzung I (zwei Routineschritte); der amtliche Bereich ist II.")
row("2019MgrundlegendBAGLAA2WTR1", "f", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen", typ_neben="",
    stichwoerter="GH: (5; 5; 5) + w · (−5; 0; 0)|Gleichsetzen: I 4 − r + 4u = 5 − 5w, II −5u = 5, III r² + 1 = 5|u = −1, r = ±2; w = 3/5 bzw. 7/5|nur w = 3/5 auf der Kante: Teilverhältnis 3 : 2",
    voraussetzungen="Gerade durch zwei Punkte|Gleichungssystem mit quadratischer Gleichung|Parameterbereich einer Strecke",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=Wf_SK, kontext="ohne", textumfang="mittel",
    gegeben=Wf + "; g: x = (4 − r; 0; r² + 1) + u · (4; −5; 0), u ∈ IR; für einen Wert von r schneidet g die Kante GH",
    gesucht="Verhältnis, in dem der Schnittpunkt die Kante GH teilt",
    verfahren="g mit der Geraden GH gleichsetzen, r aus III, u aus II, w aus I; w ∈ [0; 1] wählen",
    schritte="5", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Gleichsetzen mit x = (5; 5; 5) + w · (−5; 0; 0) liefert I 4 − r + 4u = 5 − 5w, II −5u = 5, III r² + 1 = 5; u = −1, r = ±2, w = 3/5 bzw. 7/5; nur w = 3/5 liegt auf GH, die Kante wird im Verhältnis 3 : 2 geteilt (amtlich)",
    zwischenergebnis="Schnittpunkt (2 | 5 | 5)", niveau_geschaetzt="II",
    fehlerquelle="r = 2 mit w = 7/5 als Lösung außerhalb der Kante nicht verwerfen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Typ aus der Landeszeile 2019-be-gk 3.2 f (wortgleich; dort vorgemerkt, Schätzung dort II). Schätzung II (Standardverfahren mit Fallunterscheidung); der amtliche Bereich ist III.")
# ---- AG/LA (A2) WTR 2: Haus als Körper ABCDIJKL (a–g, 20 BE)
Ha = ("Haus als Körper ABCDIJKL: Quader ABCDEFGH und Dachprisma EFGHIJKL; A(0 | 0 | 0), G(10 | 6 | 10), H(0 | 6 | 10), K(10 | 6 | 10,5), L(0 | 6 | 13); "
      "verglaste Fassade IEHL; 1 LE = 1 m")
Ha_SK = ("Schrägbild: Quader über dem Rechteck ABCD (10 × 6) bis zur Höhe 10, darauf ein Dachprisma mit Firstkante IL auf der Höhe 13 über der Kante EH "
         "(x = 0) und der Traufkante JK auf Höhe 10,5 über FG (x = 10); Fassade IEHL vorn links")
row("2019MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen eines Hauses als Quader plus Dachprisma mit Trapezquerschnitt berechnen", typ_neben="",
    stichwoerter="Quader 10 · 6 · 10 = 600|Prisma mit Trapezquerschnitt (Höhen 3 und 0,5 über 10): 1/2 · (3 + 0,5) · 10 · 6 = 105|V = 705 m³",
    voraussetzungen="Volumen Quader und Prisma|Trapezfläche",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=Ha_SK, kontext="Haus / Dachgeschoss", textumfang="mittel",
    gegeben=Ha,
    gesucht="Volumen des Hauses",
    verfahren="Quader und Prisma (Trapezquerschnitt in der xz-Ebene mal Tiefe 6) addieren",
    schritte="2", zahlenraum="dezimal", einheiten="m³", abhaengig_von="",
    ergebnis="10 · 6 · 10 + 1/2 · (0,5 + 3) · 10 · 6 = 705, d. h. das Haus hat ein Volumen von etwa 700 m³ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Dachprisma als Dreiecksprisma mit Höhe 3 ansetzen",
    bemerkung="Standardbezug: K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebene eines Körpers angeben und ihre Schnittfigur mit dem Körper einzeichnen", typ_neben="",
    stichwoerter="Symmetrieebene y = 3 (Mitte der Tiefe 6)|Schnittfigur: Fünfeck aus Rechteck 10 × 10 und Trapez darüber, in der Abbildung eintragen",
    voraussetzungen="Symmetrie des Körpers erkennen|Schnittfigur einer achsenparallelen Ebene",
    format="Kurzantwort|Zeichnen", operator="Geben Sie an|Zeichnen Sie", antwort="Term|Grafik",
    material="Körper", skizze=Ha_SK, kontext="Haus / Dachgeschoss", textumfang="kurz",
    gegeben=Ha,
    gesucht="Gleichung der Symmetrieebene; Seiten der Schnittfigur in der Abbildung",
    verfahren="Mittelebene y = 3 nennen und den Schnitt (Fünfeck) einzeichnen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="y = 3; Zeichnung des Schnittfünfecks (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="x = 5 als Symmetrieebene nehmen (Dach ist nicht symmetrisch in x)",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich.")
row("2019MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Verlauf zweier Ebenen durch das Innere eines Körpers über Punktproben und Vorzeichen untersuchen", typ_neben="",
    stichwoerter="S: 3x − 5y = 0 enthält A und G, also durch das Innere|T: 3x + 5y = 0 hat keinen Punkt mit x, y > 0: verläuft nicht durch das Innere",
    voraussetzungen="Punktprobe|Vorzeichenargument für x, y ≥ 0",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Körper", skizze=Ha_SK, kontext="Haus / Dachgeschoss", textumfang="kurz",
    gegeben=Ha + "; Ebenen S: 3x − 5y = 0 und T: 3x + 5y = 0",
    gesucht="für jede Ebene, ob sie durch das Innere des Körpers verläuft",
    verfahren="Punkte A und G in S einsetzen; für T das Vorzeichen von 3x + 5y im Körper betrachten",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="S verläuft durch das Innere, da A und G die Gleichung erfüllen; T nicht, da kein Punkt mit positiver x- und y-Koordinate die Gleichung erfüllt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="T nur an den Eckpunkten prüfen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
Fa = "Farben zum Mischen: m = (w; r; g; b) Mengen in Litern (weiß, rot, grün, blau), p = (2,50; 3,40; 3,50; 3,20) Preise in Euro je Liter"
row("2019MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Skalarprodukt zweier Sachvektoren als Gesamtpreis deuten", typ_neben="",
    stichwoerter="m · p = Summe Menge mal Preis|Gesamtpreis der Farben",
    voraussetzungen="Skalarprodukt als Summe von Produkten",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Haus / Farben", textumfang="mittel",
    gegeben=Fa,
    gesucht="Bedeutung des Terms m · p",
    verfahren="Skalarprodukt als Gesamtkosten lesen",
    schritte="1", zahlenraum="dezimal", einheiten="Euro", abhaengig_von="",
    ergebnis="Mit dem Term lässt sich der Gesamtpreis für die Farben berechnen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Skalarprodukt als Vektor deuten",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich.")
row("2019MgrundlegendBAGLAA2WTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Mengen aus einem Mischungsverhältnis und einem vorgegebenen Skalarprodukt berechnen", typ_neben="",
    stichwoerter="Verhältnis 12 : 1 : 2 : 3, also m = (12r; r; 2r; 3r)|(12r; r; 2r; 3r) · p = 50r = 250 ⇔ r = 5|60, 5, 10, 15 Liter",
    voraussetzungen="Verhältnis als Vielfache einer Größe|Skalarprodukt ausrechnen|lineare Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Haus / Farben", textumfang="kurz",
    gegeben=Fa + "; m · p = 250; Mischungsverhältnis weiß : rot : grün : blau = 12 : 1 : 2 : 3",
    gesucht="gekaufte Menge jeder Farbe",
    verfahren="m mit Faktor r ansetzen, Skalarprodukt gleich 250 setzen",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="Liter", abhaengig_von="",
    ergebnis="(12r; r; 2r; 3r) · (2,50; 3,40; 3,50; 3,20) = 250 ⇔ 50r = 250 ⇔ r = 5: 60 Liter weiße, 5 Liter rote, 10 Liter grüne und 15 Liter blaue Farbe (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="250 durch die Preissumme teilen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAGLAA2WTR2", "f", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Anteil der Bodenfläche unter einer Mindesthöhe über den Strahlensatz am Dachquerschnitt berechnen", typ_neben="",
    stichwoerter="Dachhöhe fällt linear von 3 (x = 0) auf 0,5 (x = 10)|Höhe ≤ 1 auf dem Streifen der Breite (1 − 0,5)/(3 − 0,5) · 10 = 2 an der Traufseite|Anteil 2 · 6/(10 · 6) = 20 %",
    voraussetzungen="linearer Höhenverlauf|Strahlensatz oder Geradengleichung|Flächenanteil",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=Ha_SK, kontext="Haus / Dachgeschoss", textumfang="mittel",
    gegeben=Ha + "; Raumteile mit höchstens 1 m Höhe zählen nicht zur Wohnfläche",
    gesucht="prozentualer Anteil der Bodenfläche des Dachgeschosses, für den das gilt",
    verfahren="Breite des Streifens mit Dachhöhe ≤ 1 über den Strahlensatz, Anteil an 10 × 6",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="((1 − 0,5)/(3 − 0,5) · 10 · 6)/(10 · 6) = 20 % (amtlich)",
    zwischenergebnis="Streifenbreite 2", niveau_geschaetzt="II",
    fehlerquelle="Höhe 1 auf die Firsthöhe 3 statt auf die Differenz zur Traufhöhe beziehen",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBAGLAA2WTR2", "g", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schattenpunkt bei paralleler Projektion bestimmen", typ_neben="",
    stichwoerter="Licht durch die Fenstereckpunkte, Richtung (3; −2; −2)|Schatten von L(0 | 6 | 13) auf dem Boden z = 10: (0; 6; 13) + t · (3; −2; −2) mit z = 10 ⇒ t = 1,5, Punkt (4,5 | 3 | 10)|beschienene Flächenstücke auf Boden und Wänden einzeichnen",
    voraussetzungen="Gerade mit gegebener Richtung durch einen Punkt|Schnitt mit der Ebene z = 10|Schattenfigur konstruieren",
    format="Rechnung|Zeichnen", operator="Bestimmen Sie|Zeichnen Sie", antwort="Zahl|Grafik",
    material="Körper", skizze=Ha_SK, kontext="Haus / Dachgeschoss", textumfang="lang",
    gegeben=Ha + "; Sonnenlicht durch die Fassade IEHL mit Richtungsvektor (3; −2; −2); ein Eckpunkt des beschienenen Flächenstücks auf dem Boden des Dachgeschosses liegt nicht am Rand",
    gesucht="Koordinaten dieses Eckpunkts; alle beschienenen Flächenstücke in der Abbildung",
    verfahren="Lichtgerade durch L mit dem Boden z = 10 schneiden; Schattenfigur einzeichnen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Mit z = 10: (0; 6; 13) + t · (3; −2; −2) = (x; y; 10) ⇔ t = 1,5 ∧ x = 4,5 ∧ y = 3; Zeichnung der beschienenen Flächenstücke (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="den Schatten von I (auf der Höhe 13, y = 0) statt von L verfolgen; der Schatten von I trifft die Seitenwand y = 0 nicht den Boden",
    bemerkung="Standardbezug: K2 III, K4 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2018-be-gk); hier mit dem Zeichnen der Schattenfigur.")
# ---- Stochastik WTR 1: Führerschein und Fahrprüfung (a–e, 20 BE); Landesheft 2019-be-gk 4.1 c, d, e vorgemerkt
FS = "Land mit 80 % Führerscheinbesitz unter Erwachsenen; 200 zufällig ausgewählte Erwachsene, X = Anzahl mit Führerschein, binomialverteilt (n = 200, p = 0,8)"
row("2019MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer prozentualen Abweichung vom Erwartungswert nach beiden Seiten berechnen", typ_neben="",
    stichwoerter="E(X) = 200 · 0,8 = 160, 5 % davon = 8|P(152 ≤ X ≤ 168) ≈ 86,8 %",
    voraussetzungen="Erwartungswert n · p|prozentuale Abweichung als Intervall|kumulierte Wahrscheinlichkeit mit dem Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Führerschein / Fahrprüfung", textumfang="mittel",
    gegeben=FS,
    gesucht="Wahrscheinlichkeit, dass X vom Erwartungswert um höchstens 5 % abweicht",
    verfahren="Intervall [160 − 8; 160 + 8] bilden und kumuliert berechnen",
    schritte="3", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="200 · 0,8 = 160, 5 % · 160 = 8; P(152 ≤ X ≤ 168) ≈ 86,8 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="5 % als 5 Personen lesen oder nur eine Seite rechnen",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,8677).")
row("2019MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln", typ_neben="",
    stichwoerter="P(X > 160) ≥ 0,9 für B(n; 0,8)|n = 209: 87,57 %; n = 210: 90,04 %|mindestens 210",
    voraussetzungen="Binomialverteilung mit variablem n|systematisches Probieren mit dem Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Führerschein / Fahrprüfung", textumfang="kurz",
    gegeben=FS,
    gesucht="Mindestanzahl Erwachsener, damit mit mindestens 90 % mehr als 160 einen Führerschein besitzen",
    verfahren="P(X > 160) für wachsendes n berechnen, bis 90 % erreicht sind",
    schritte="3", zahlenraum="Prozent", einheiten="Personen", abhaengig_von="",
    ergebnis="P(X > 160) ≈ 87,57 % für n = 209 und ≈ 90,04 % für n = 210; es müssten mindestens 210 Erwachsene ausgewählt werden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="n aus 0,8n = 160 zu 200 schließen",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (0,8757 und 0,9004). Typ wiederverwendet (2024-ea-B).")
FP = ("Fahrprüfungen einer Region: 13 879 Prüflinge, 2 482 davon mindestens 30 Jahre alt; 11 104 haben bestanden, davon 8 870 jünger als 30; "
      "A: Prüfling mindestens 30, B: Prüfung bestanden")
row("2019MgrundlegendBStochastikWTR1", "c", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen", typ_neben="",
    stichwoerter="jünger als 30: 13 879 − 2 482 = 11 397|davon bestanden 8 870|nicht bestanden: 11 397 − 8 870 = 2 527",
    voraussetzungen="Vierfeldertafel mit absoluten Häufigkeiten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Führerschein / Fahrprüfung", textumfang="mittel",
    gegeben=FP,
    gesucht="Anzahl der Prüflinge unter 30, die nicht bestanden haben",
    verfahren="Randsumme der Jüngeren minus Bestandene der Jüngeren",
    schritte="2", zahlenraum="ganz", einheiten="Prüflinge", abhaengig_von="",
    ergebnis="13 879 − 2 482 − 8 870 = 2 527 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="11 104 − 8 870 (die älteren Bestandenen) angeben",
    bemerkung="Standardbezug: K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ aus der Landeszeile 2019-be-gk 4.1 c (wortgleich; dort vorgemerkt).")
row("2019MgrundlegendBStochastikWTR1", "d", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten", typ_neben="",
    stichwoerter="P_A(B) = (11 104 − 8 870)/2 482 ≈ 90,0 %|P(B) = 11 104/13 879 ≈ 80,0 %|nicht gleich: abhängig; die Bestehensquote unterscheidet sich zwischen den Altersgruppen",
    voraussetzungen="bedingte Wahrscheinlichkeit aus absoluten Häufigkeiten|Unabhängigkeitskriterium",
    format="Rechnung|Begründung", operator="Untersuchen Sie|Geben Sie an|Interpretieren Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Führerschein / Fahrprüfung", textumfang="mittel",
    gegeben=FP,
    gesucht="ob P_A(B) und P(B) übereinstimmen; ob A und B unabhängig sind, mit Deutung",
    verfahren="Beide Wahrscheinlichkeiten berechnen und vergleichen",
    schritte="3", zahlenraum="Prozent|Bruch", einheiten="", abhaengig_von="2019MgrundlegendBStochastikWTR1-1c",
    ergebnis="P_A(B) = (11 104 − 8 870)/2 482 ≈ 90,0 %, P(B) = 11 104/13 879 ≈ 80,0 %; A und B sind nicht unabhängig, d. h. der Anteil der Bestehenden ist in den beiden Altersgruppen verschieden groß (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P_B(A) statt P_A(B) berechnen",
    bemerkung="Standardbezug: K3 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,900 und 0,800). Typ aus der Landeszeile 2019-be-gk 4.1 d (wortgleich; dort vorgemerkt).")
row("2019MgrundlegendBStochastikWTR1", "e", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil aus einer quadratischen Gleichung für ein zweistufiges Bestehen berechnen", typ_neben="",
    stichwoerter="q beim ersten Mal, (1 − q) · q/2 beim zweiten Mal|q + (1 − q) · q/2 = 0,9 ⇔ 5q² − 15q + 9 = 0|q = (15 − √45)/10 ≈ 82,9 % (die andere Lösung > 1)",
    voraussetzungen="Pfadregel über zwei Teilnahmen|quadratische Gleichung|Lösung als Anteil auswählen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Führerschein / Fahrprüfung", textumfang="lang",
    gegeben="Nicht bestandene Prüflinge nehmen ein zweites Mal teil; Anteil q beim ersten Mal bestanden, beim zweiten Mal nur halb so großer Anteil; spätestens beim zweiten Mal bestehen 90 %",
    gesucht="Wert von q",
    verfahren="Gleichung q + (1 − q) · q/2 = 0,9 aufstellen und lösen",
    schritte="3", zahlenraum="dezimal|Wurzel|Prozent", einheiten="", abhaengig_von="",
    ergebnis="q + (1 − q) · q/2 = 9/10 ⇔ 5q² − 15q + 9 = 0 ⇔ q = (15 ± √45)/10; mit q ≤ 1 ergibt sich q ≈ 82,9 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="beim zweiten Mal q/2 ohne den Faktor (1 − q) ansetzen",
    bemerkung="Standardbezug: K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,8292). Typ aus der Landeszeile 2019-be-gk 4.1 e (wortgleich; dort vorgemerkt, Schätzung dort III – Vorrang des Amtlichen, die Landeszeile zieht im Abgleichlauf nach).")
# ---- Stochastik WTR 2: Urne mit +1, +2, −3 (1 a–b, 6 BE; 2 a–c, 9 BE; 3 a–b, 5 BE)
U19 = "Urne: 35 % der Kugeln mit „+1“, 25 % mit „+2“, die übrigen 40 % mit „−3“ beschriftet"
row("2019MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit und Pfadwahrscheinlichkeit einer festen Anfangsfolge berechnen", typ_neben="",
    stichwoerter="100-mal Ziehen mit Zurücklegen|P(A) = P(X > 35) = 1 − P(X ≤ 35) ≈ 1 − 0,546 = 45,4 % für B(100; 0,35)|P(B) = 0,35³ ≈ 4,3 %",
    voraussetzungen="Binomialverteilung mit dem Rechner|Pfadregel",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne / Spiel", textumfang="mittel",
    gegeben=U19 + "; 100-mal Ziehen mit Zurücklegen; A: mehr als 35 Kugeln mit +1; B: die ersten drei Kugeln mit +1",
    gesucht="P(A) und P(B)",
    verfahren="1 − P(X ≤ 35) für B(100; 0,35); 0,35³",
    schritte="2", zahlenraum="Prozent|dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="P(A) ≈ 1 − 0,546 = 45,4 %; P(B) = 0,35³ ≈ 4,3 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≥ 35) rechnen; B als Binomialwahrscheinlichkeit für genau drei Treffer deuten",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,4542 und 0,0429).")
row("2019MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Kleinere Gesamtzahl von Kugeln aus gekürzten Anteilen begründen", typ_neben="",
    stichwoerter="35/100 = 7/20, 25/100 = 5/20, 40/100 = 8/20|20 Kugeln (7, 5, 8) genügen",
    voraussetzungen="Anteile als gekürzte Brüche|gemeinsamer Nenner",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Urne / Spiel", textumfang="kurz",
    gegeben=U19,
    gesucht="Nachweis, dass die Gesamtzahl der Kugeln kleiner als 100 sein kann",
    verfahren="Anteile mit dem Nenner 20 schreiben",
    schritte="1", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="35/100 = 7/20, 25/100 = 5/20; eine mögliche Anzahl ist 20 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur die 35 % kürzen und den dritten Anteil vergessen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich.")
SP = U19 + "; Spiel: zweimal Ziehen mit Zurücklegen, Summe der Zahlen; positive Summe = Gewinn in Euro, negative Summe = Verlust"
row("2019MgrundlegendBStochastikWTR2", "a", innen="2", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit einer Summe über alle Ergebnisfolgen mit Reihenfolgen berechnen", typ_neben="",
    stichwoerter="Summe > 3 nur bei (+2, +2)|0,25² = 6,25 %",
    voraussetzungen="Ergebnisfolgen zu einer Summenbedingung|Pfadregel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne / Spiel", textumfang="mittel",
    gegeben=SP,
    gesucht="Wahrscheinlichkeit, mehr als 3 Euro zu gewinnen",
    verfahren="Einzige Folge (+2, +2) erkennen, Pfadwahrscheinlichkeit",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="Euro", abhaengig_von="",
    ergebnis="0,25² = 6,25 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Summe 3 (Folgen +1/+2) mitzählen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2021-be-gk).")
row("2019MgrundlegendBStochastikWTR2", "b", innen="2", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit eines Gewinns über alle günstigen Summenpfade nachweisen", typ_neben="",
    stichwoerter="positive Summe bei (+1, +1), (+1, +2), (+2, +1), (+2, +2)|0,35² + 2 · 0,35 · 0,25 + 0,25² = 36 %",
    voraussetzungen="alle Ergebnisfolgen mit positiver Summe|Pfad- und Summenregel",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Urne / Spiel", textumfang="kurz",
    gegeben=SP,
    gesucht="Nachweis, dass die Gewinnwahrscheinlichkeit 36 % beträgt",
    verfahren="Die vier Folgen ohne −3 zusammenzählen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="0,35² + 2 · 0,35 · 0,25 + 0,25² = 36 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="(+2, −3) mit Summe −1 als Gewinn zählen",
    bemerkung="Standardbezug: K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt ((0,6)² = 0,36).")
row("2019MgrundlegendBStochastikWTR2", "c", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert eines Spielgewinns über die Pfade eines Baumdiagramms berechnen", typ_neben="",
    stichwoerter="Baumdiagramm mit zwei Stufen zu +1, +2, −3|Summen 2, 3, 4, −2, −1, −6 mit ihren Pfadwahrscheinlichkeiten|E = 2 · 0,35² + 3 · 2 · 0,35 · 0,25 + 4 · 0,25² − 2 · 2 · 0,35 · 0,4 − 1 · 2 · 0,25 · 0,4 − 6 · 0,4² = −0,7",
    voraussetzungen="Baumdiagramm mit neun Pfaden|Erwartungswert als gewichtete Summe",
    format="Zeichnen|Rechnung", operator="Ermitteln Sie", antwort="Grafik|Zahl",
    material="keins", skizze="keine", kontext="Urne / Spiel", textumfang="kurz",
    gegeben=SP,
    gesucht="durchschnittlicher Verlust pro Spiel mithilfe eines Baumdiagramms",
    verfahren="Alle neun Pfade mit Summe und Wahrscheinlichkeit, Erwartungswert bilden",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="Euro", abhaengig_von="",
    ergebnis="2 · 0,35² + 3 · 2 · 0,35 · 0,25 + 4 · 0,25² + (−2) · 2 · 0,35 · 0,4 + (−1) · 2 · 0,25 · 0,4 + (−6) · 0,4² = −0,7; pro Spiel ist ein durchschnittlicher Verlust von 70 Cent zu erwarten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Reihenfolgen (Faktor 2) bei gemischten Pfaden vergessen",
    bemerkung="Standardbezug: K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (E = 2 · E(Zahl) = 2 · (−0,35) = −0,7).")
NU = U19 + "; die Urne enthält n Kugeln; zwei Kugeln (+1 und +2) werden hinzugelegt, dann eine Kugel gezogen"
row("2019MgrundlegendBStochastikWTR2", "a", innen="3", seite="2", punkte="2", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeitsterm nach Hinzufügen von Kugeln als Anteil begründen", typ_neben="",
    stichwoerter="Gesamtzahl n + 2|Kugeln mit +1: vorher 0,35n, nachher 0,35n + 1|P = (0,35n + 1)/(n + 2)",
    voraussetzungen="Laplace-Wahrscheinlichkeit als günstige durch mögliche|Anzahlen als Terme in n",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Urne / Spiel", textumfang="mittel",
    gegeben=NU + "; Term (0,35n + 1)/(n + 2)",
    gesucht="Begründung, dass der Term die Wahrscheinlichkeit für eine Kugel mit +1 angibt",
    verfahren="Zähler und Nenner als Anzahlen deuten",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Die Anzahl der Kugeln ist n + 2; vor der Ergänzung sind 0,35 · n Kugeln mit +1 beschriftet, nach der Ergänzung 0,35 · n + 1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Nenner n + 1 setzen",
    bemerkung="Standardbezug: K1 III, K3 II, K6 III. AB amtlich: III. Amtlich. Schätzung II (Term aus Anzahlen erklären); der amtliche Bereich ist III.")
row("2019MgrundlegendBStochastikWTR2", "b", innen="3", seite="2", punkte="3", afb_amtlich="III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Zunahme einer Wahrscheinlichkeit nach Hinzufügen von Kugeln über eine Termdifferenz begründen", typ_neben="",
    stichwoerter="(0,35n + 1)/(n + 2) − 0,35 = (0,35n + 1 − 0,35(n + 2))/(n + 2) = 0,3/(n + 2) > 0",
    voraussetzungen="Differenz zweier Brüche|Vorzeichen eines Terms",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Urne / Spiel", textumfang="kurz",
    gegeben=NU + "; P(+1) nach dem Hinzufügen (0,35n + 1)/(n + 2), vorher 0,35",
    gesucht="Begründung, dass die Wahrscheinlichkeit nach dem Hinzufügen größer ist",
    verfahren="Differenz der beiden Wahrscheinlichkeiten bilden und als positiv nachweisen",
    schritte="2", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="2019MgrundlegendBStochastikWTR2-3a",
    ergebnis="(0,35n + 1)/(n + 2) − 0,35 = (0,35n + 1 − 0,35 · (n + 2))/(n + 2) = 0,3/(n + 2) > 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="nur ein Zahlenbeispiel für n rechnen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt.")
# ---- Stochastik WTR 3: Glücksspiel-Befragung (1 a–d, 12 BE) und Urne mit 4 und x (2 a–c, 8 BE)
GL = ("Befragung von 2 360 Männern und 2 200 Frauen (Glücksspielteilnahme): 2,5 % der Männer und 0,5 % der Frauen mit Anzeichen spielsüchtigen Verhaltens; "
      "M: Person ist ein Mann, S: Anzeichen spielsüchtigen Verhaltens")
row("2019MgrundlegendBStochastikWTR3", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel mit absoluten Häufigkeiten aus Gruppengrößen und bedingten Anteilen vervollständigen", typ_neben="",
    stichwoerter="M∩S = 0,025 · 2 360 = 59, M∩¬S = 2 301|¬M∩S = 0,005 · 2 200 = 11, ¬M∩¬S = 2 189|Ränder 2 360, 2 200, 70, 4 490, 4 560",
    voraussetzungen="Anteile in absolute Häufigkeiten umrechnen|Vierfeldertafel",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Glücksspiel / Befragung", textumfang="mittel",
    gegeben=GL,
    gesucht="vollständig ausgefüllte Vierfeldertafel",
    verfahren="Anzahlen je Feld berechnen, Randsummen bilden",
    schritte="2", zahlenraum="ganz|Prozent", einheiten="Personen", abhaengig_von="",
    ergebnis="M∩S 59, M∩¬S 2 301, ¬M∩S 11, ¬M∩¬S 2 189; Ränder 2 360, 2 200, 70, 4 490, gesamt 4 560 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Prozentangaben direkt als Feldwerte eintragen",
    bemerkung="Standardbezug: K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")
row("2019MgrundlegendBStochastikWTR3", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Bedingte Wahrscheinlichkeit und Schnittwahrscheinlichkeit im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="P_M(S): Wahrscheinlichkeit für Anzeichen, wenn die Person ein Mann ist|P(M ∩ S): Wahrscheinlichkeit, dass die Person ein Mann ist und Anzeichen zeigt",
    voraussetzungen="Unterschied bedingte Wahrscheinlichkeit und Schnitt",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Glücksspiel / Befragung", textumfang="kurz",
    gegeben=GL + "; Terme P_M(S) und P(M ∩ S)",
    gesucht="Bedeutung beider Terme im Sachzusammenhang",
    verfahren="Bedingung und Schnitt in Worte fassen",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="P_M(S) ist die Wahrscheinlichkeit für Anzeichen spielsüchtigen Verhaltens, wenn bekannt ist, dass die Person männlich ist; P(M ∩ S) die Wahrscheinlichkeit, dass die Person männlich ist und die Befragung Anzeichen ergab (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="beide Terme gleich deuten",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2022-bebb-gk).")
row("2019MgrundlegendBStochastikWTR3", "c", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus der Vierfeldertafel mit absoluten Häufigkeiten angeben", typ_neben="",
    stichwoerter="unter den 70 Personen mit Anzeichen sind 11 Frauen|P = 11/70",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient absoluter Häufigkeiten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel / Befragung", textumfang="kurz",
    gegeben=GL + "; Vierfeldertafel aus a",
    gesucht="Wahrscheinlichkeit, dass eine zufällig aus den Personen mit Anzeichen ausgewählte Person eine Frau ist",
    verfahren="11/70 aus der Tafel",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="2019MgrundlegendBStochastikWTR3-1a",
    ergebnis="11/70 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="11/2 200 (Anteil unter den Frauen) angeben",
    bemerkung="Standardbezug: K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (≈ 15,7 %). Schätzung I (Quotient aus der Tafel); der amtliche Bereich ist II.")
row("2019MgrundlegendBStochastikWTR3", "d", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kleinsten Radius einer symmetrischen Umgebung um den Erwartungswert für eine Mindestwahrscheinlichkeit ermitteln", typ_neben="",
    stichwoerter="X ~ B(200; 0,025), E(X) = 5|P(2 ≤ X ≤ 8) ≈ 0,896 < 0,9|P(1 ≤ X ≤ 9) ≈ 0,964 > 0,9: Intervall [1; 9]",
    voraussetzungen="Erwartungswert|symmetrische Umgebung|kumulierte Wahrscheinlichkeiten mit dem Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel / Befragung", textumfang="lang",
    gegeben="200 zufällig ausgewählte befragte Männer; X = Anzahl mit Anzeichen spielsüchtigen Verhaltens, binomialverteilt mit p = 0,025",
    gesucht="kleinstes um E(X) symmetrisches Intervall, in dem X mit mehr als 90 % liegt",
    verfahren="E(X) = 5, Umgebungen [5 − r; 5 + r] mit wachsendem r prüfen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Erwartungswert 200 · 0,025 = 5; P(2 ≤ X ≤ 8) ≈ 0,896 < 0,9, P(1 ≤ X ≤ 9) ≈ 0,964 > 0,9; das gesuchte Intervall ist [1; 9] (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Sigma-Umgebung mit σ ≈ 2,2 ohne Prüfung angeben",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,8960 und 0,9636). Typ wiederverwendet (2023-ea-B).")
UX = "Urne mit fünf Kugeln: drei mit der Zahl 4, zwei mit der natürlichen Zahl x ≠ 4"
row("2019MgrundlegendBStochastikWTR3", "a", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Zufallsexperiment und Ereignis zu einer Potenz der Gegenwahrscheinlichkeit beschreiben", typ_neben="",
    stichwoerter="1 − 0,6³: 0,6 = 3/5 Wahrscheinlichkeit für eine 4|dreimal Ziehen mit Zurücklegen|Ereignis: nicht alle drei Kugeln tragen die 4",
    voraussetzungen="Gegenereignis|Ziehen mit Zurücklegen als Bernoulli-Kette",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Urne / Erwartungswert", textumfang="mittel",
    gegeben=UX + "; Term 1 − 0,6³",
    gesucht="ein Zufallsexperiment und ein Ereignis mit dieser Wahrscheinlichkeit",
    verfahren="0,6³ als dreimal 4 mit Zurücklegen, 1 − … als Gegenereignis",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Zufallsexperiment: dreimal nacheinander eine Kugel ziehen und zurücklegen; Ereignis: nicht alle drei Kugeln tragen die Zahl 4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Ziehen ohne Zurücklegen beschreiben (dann keine Potenz)",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II. AB amtlich: II. Amtlich.")
row("2019MgrundlegendBStochastikWTR3", "b", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Untere Schranke für eine Kugelbeschriftung aus dem Erwartungswert der Summe ohne Rechnung begründen", typ_neben="",
    stichwoerter="zwei Kugeln gleichzeitig, E(Summe) = 12|für x ≤ 5 wäre jede Summe höchstens 10 < 12|also x > 5",
    voraussetzungen="Erwartungswert höchstens so groß wie der größte Wert",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Urne / Erwartungswert", textumfang="kurz",
    gegeben=UX + "; beim gleichzeitigen Ziehen zweier Kugeln ist der Erwartungswert der Summe 12",
    gesucht="Begründung ohne Wahrscheinlichkeiten, dass x > 5",
    verfahren="Maximale Summe für x ≤ 5 mit dem Erwartungswert vergleichen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Für x ≤ 5 wäre die Summe zweier Kugeln höchstens 10, der Erwartungswert könnte dann nicht 12 sein (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="mit dem Mittelwert 4 + x = 12 argumentieren",
    bemerkung="Standardbezug: K1 I, K2 I, K3 I. AB amtlich: I. Amtlich.")
row("2019MgrundlegendBStochastikWTR3", "c", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Kugelbeschriftung aus dem Erwartungswert der Summe beim Ziehen ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="Summen 8 (zwei Vieren) mit 3/5 · 2/4, 4 + x mit 2 · 3/5 · 2/4, 2x mit 2/5 · 1/4|8 · 3/10 + (4 + x) · 6/10 + 2x · 1/10 = 12 ⇔ 24/5 + 4x/5 = 12 ⇔ x = 9",
    voraussetzungen="Ziehen ohne Zurücklegen (Pfade)|Erwartungswert als Gleichung in x",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne / Erwartungswert", textumfang="kurz",
    gegeben=UX + "; Erwartungswert der Summe zweier gleichzeitig gezogener Kugeln 12",
    gesucht="die Zahl x",
    verfahren="Verteilung der Summe ohne Zurücklegen aufstellen, Erwartungswert gleich 12 setzen",
    schritte="3", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="",
    ergebnis="3/5 · 2/4 · 8 + 2 · 3/5 · 2/4 · (4 + x) + 2/5 · 1/4 · 2x = 12 ⇔ 24/5 + 4/5 · x = 12 ⇔ x = 9 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="mit Zurücklegen rechnen (liefert x = 8)",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt.")

NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Nullstellen und Werte: Prozentuale Abweichung eines Modellwerts vom Messwert berechnen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den Funktionswert eines Modells an einer Messstelle berechnen und seine relative Abweichung vom zugehörigen Messwert in Prozent angeben.", "2019MgrundlegendBAnalysisWTR1-1a"),
    ("Nullstellen und Werte: Tiefstelle und Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Am abgebildeten Graphen die Stelle des Tiefpunkts (Beginn des Anstiegs) und die Stelle ablesen, ab der ein vorgegebener Funktionswert überschritten wird, und beide im Sachzusammenhang benennen.", "2019MgrundlegendBAnalysisWTR1-1b"),
    ("Mittlere Änderungsrate über ein Intervall berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Die mittlere Änderungsrate einer Funktion über ein vorgegebenes Intervall als Differenzenquotient mit Einheit berechnen.", "2019MgrundlegendBAnalysisWTR1-1d"),
    ("Steigungen der Geraden durch den Wendepunkt mit genau einem gemeinsamen Punkt über die Wendetangente eingrenzen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Für Geraden durch den Wendepunkt eines Graphen die Menge der Steigungen bestimmen, bei denen kein weiterer gemeinsamer Punkt entsteht, mit der Wendetangentensteigung als Grenzwert und dem Graphen als Begründung.", "2019MgrundlegendBAnalysisWTR1-2a"),
    ("Nullstellen und Werte: y-Achsenabschnitt einer Geraden durch einen festen Punkt als Term in der Steigung angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Für die Geradenschar durch einen festen Punkt den y-Achsenabschnitt als Term in der Steigung aufstellen.", "2019MgrundlegendBAnalysisWTR1-2b"),
    ("Nullstellen und Werte: Punktprobe an einer Geraden rechnerisch zeigen und Gerade einzeichnen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Rechnerisch zeigen, dass ein vorgegebener Punkt auf einer Geraden liegt, und die Gerade in die Abbildung einzeichnen.", "2019MgrundlegendBAnalysisWTR1-2c"),
    ("Lösungen einer Differenzgleichung als Schnittstellen zweier Graphen grafisch beschreiben und angeben", "Analysis", "Gleichungen lösen",
     "Die Lösungen einer Gleichung f(x) − g(x) = 0 als Schnittstellen der beiden Graphen beschreiben und aus der Abbildung ablesen.", "2019MgrundlegendBAnalysisWTR1-2d"),
    ("Integralwert: Integral über die Punktsymmetrie zum Wendepunkt als Dreiecksfläche unter einer Sekante begründen", "Analysis", "Flächeninhalt durch Integration",
     "Ohne Rechnung begründen, dass das Integral über einen zum Wendepunkt punktsymmetrischen Graphen zwischen zwei Schnittstellen mit einer Geraden durch den Wendepunkt gleich der Dreiecksfläche unter dieser Geraden ist.", "2019MgrundlegendBAnalysisWTR1-2e"),
    ("Integralwert: Existenz einer Grenze mit Integralwert null über den Vorzeichenwechsel und die Stetigkeit am Graphen begründen", "Analysis", "Flächeninhalt durch Integration",
     "Mithilfe des Graphen begründen, dass ein Integral über ein verschiebbares Intervall fester Länge für eine Grenze zwischen zwei Werten null wird, weil es dort das Vorzeichen wechselt und stetig von der Grenze abhängt.", "2019MgrundlegendBAnalysisWTR1-2f"),
    ("Transformation: Verschiebung und Streckung der Grundhyperbel aus dem Term beschreiben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus dem Term einer gebrochenrationalen Funktion der Form a/(x − c) die Verschiebung in x-Richtung und die Streckung in y-Richtung gegenüber 1/x beschreiben.", "2019MgrundlegendBAnalysisWTR1-3a"),
    ("Schnittpunkte einer Geraden mit einer Hyperbel über eine quadratische Gleichung berechnen", "Analysis", "Gleichungen lösen",
     "Die gemeinsamen Punkte einer Geraden und einer Hyperbel durch Gleichsetzen, Umformen zu (x − c)² = k und Wurzelziehen berechnen.", "2019MgrundlegendBAnalysisWTR1-3b"),
    ("Fehlen einer gemeinsamen Tangente zweier Graphen über die Vorzeichen der Steigungen begründen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Begründen, dass zwei Graphen keine gemeinsame Tangente haben, weil ihre Steigungen überall verschiedene Vorzeichen haben.", "2019MgrundlegendBAnalysisWTR1-3c"),
    ("Integralwert: Grenzen für ein positives Produkt zweier Integrale über die Vorzeichen der Hyperbeläste angeben und begründen", "Analysis", "Flächeninhalt durch Integration",
     "Integrationsgrenzen so wählen und begründen, dass das Produkt zweier Integrale über verschiedene Äste einer Hyperbel positiv wird, über die Vorzeichen des Integranden und die Reihenfolge der Grenzen.", "2019MgrundlegendBAnalysisWTR1-3d"),
    ("Nullstellen einer Schar am faktorisierten Term angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Nullstellen einer Funktionenschar aus dem faktorisierten Term ablesen und ihre Unabhängigkeit vom Parameter feststellen.", "2019MgrundlegendBAnalysisWTR2-1a"),
    ("Abstand der Hochpunkte zweier benachbarter Scharparabeln berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Abstand der Hochpunkte zweier Scharkurven mit aufeinanderfolgenden Parameterwerten aus den Parameterkoordinaten berechnen.", "2019MgrundlegendBAnalysisWTR2-1c"),
    ("Maximumstelle aller Stammfunktionen über den Vorzeichenwechsel des Integranden begründen", "Analysis", "Stammfunktion und Hauptsatz",
     "Ohne Stammfunktionsterm die Stelle angeben und begründen, an der jede Stammfunktion ihr Maximum annimmt, weil der Integrand dort das Vorzeichen von plus nach minus wechselt.", "2019MgrundlegendBAnalysisWTR2-1e"),
    ("Einbeschriebenes Trapez zu einem Parameterwert in die Abbildung einzeichnen", "Analysis", "Extremalprobleme",
     "Für einen konkreten Parameterwert die Eckpunkte eines dem Graphen einbeschriebenen Trapezes berechnen und das Trapez in die Abbildung einzeichnen.", "2019MgrundlegendBAnalysisWTR2-1f"),
    ("Term für die Schenkellänge eines einbeschriebenen Trapezes aufstellen", "Analysis", "Extremalprobleme",
     "Die Länge der gleich langen Schenkel eines einbeschriebenen Trapezes als Term im Parameter über den Abstand zweier Punkte angeben.", "2019MgrundlegendBAnalysisWTR2-1g"),
    ("Flächenterm eines einbeschriebenen Trapezes über die Mittelparallele geometrisch herleiten", "Analysis", "Extremalprobleme",
     "Einen vorgegebenen Flächenterm eines einbeschriebenen Trapezes als Produkt aus Mittelparallele und Höhe geometrisch begründen.", "2019MgrundlegendBAnalysisWTR2-1h"),
    ("Punkt: Mittelpunkt des Kreises durch drei Punkte der Ebene über Mittelsenkrechte und Abstandsgleichung berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Den Umkreismittelpunkt dreier Punkte der Ebene berechnen, indem eine Koordinate aus einer Mittelsenkrechten und die andere aus der Gleichheit zweier Abstände gewonnen wird.", "2019MgrundlegendBAnalysisWTR2-1j"),
    ("Nullstellen und Werte: Anfangswert eines Bestands als Funktionswert an der Stelle null berechnen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den Anfangswert einer durch eine Funktion beschriebenen Größe als Funktionswert an der Stelle null mit Einheit berechnen.", "2019MgrundlegendBAnalysisWTR2-2a"),
    ("Nullstellen und Werte: Einhalten einer Schranke über das Vorzeichen des e-Terms begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Begründen, dass eine Funktion der Form c − a · e^(−kx) eine Schranke nie erreicht, weil der Exponentialterm stets positiv ist.", "2019MgrundlegendBAnalysisWTR2-2b"),
    ("Nullstellen und Werte: Zeitliche Entwicklung eines Bestands über ein Intervall grafisch darstellen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den Graphen einer Bestandsfunktion über ein vorgegebenes Zeitintervall in einem passend skalierten Koordinatensystem zeichnen.", "2019MgrundlegendBAnalysisWTR2-2c"),
    ("Term für die mittlere Änderungsrate über Einheitsintervalle nachweisen und Zeitpunkt des Unterschreitens einer Schranke berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Den Differenzenquotienten einer Exponentialfunktion über Intervalle der Länge eins auf eine vorgegebene Form bringen und den Zeitpunkt berechnen, ab dem er eine Schranke unterschreitet.", "2019MgrundlegendBAnalysisWTR2-2d"),
    ("Übergangsprozess: Matrixeintrag und Spaltensumme eins im Sachzusammenhang deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Einen Eintrag einer Übergangsmatrix als Anteil zwischen zwei Zuständen und die Spaltensumme eins als Erhaltung der Gesamtheit im Sachzusammenhang erläutern.", "2019MgrundlegendBAGLAA1WTR-1a"),
    ("Übergangsprozess: Aussage über eine Komponente nach einem Übergang bei gleicher Ausgangsverteilung beurteilen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine Behauptung über eine Komponente des Ergebnisvektors bei gleich großen Ausgangskomponenten durch Berechnen der entsprechenden Matrixzeile beurteilen.", "2019MgrundlegendBAGLAA1WTR-1c"),
    ("Übergangsprozess: Unbekannte Komponente der Ausgangsverteilung aus dem Ergebnisvektor über ein Gleichungssystem ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus r = M · a mit teilweise bekannten Komponenten ein lineares Gleichungssystem aufstellen und eine unbekannte Ausgangskomponente berechnen.", "2019MgrundlegendBAGLAA1WTR-1d"),
    ("Übergangsprozess: Gleichung aus gleichen Komponentensummen von Ausgabe- und Rückgabevektor nachweisen und deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus der Erhaltung der Gesamtzahl eine Beziehung zwischen den Komponenten von Ausgangs- und Ergebnisvektor nachweisen und im Sachzusammenhang deuten.", "2019MgrundlegendBAGLAA1WTR-1e"),
    ("Übergangsprozess: Mögliche Übergangsmatrix aus Ausgabe- und Rückgabezahlen zweier Stationen mit freiem Parameter ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine 2×2-Übergangsmatrix mit Spaltensummen eins so ansetzen, dass ein gegebener Ausgangsvektor auf einen gegebenen Ergebnisvektor abgebildet wird, und eine Lösung des unterbestimmten Systems angeben.", "2019MgrundlegendBAGLAA1WTR-1f"),
    ("Körper: Volumen eines Hauses als Quader plus Dachprisma mit Trapezquerschnitt berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Das Volumen eines aus Quader und Prisma mit trapezförmigem Querschnitt zusammengesetzten Körpers aus den Eckpunktkoordinaten berechnen.", "2019MgrundlegendBAGLAA2WTR2-1a"),
    ("Symmetrieebene eines Körpers angeben und ihre Schnittfigur mit dem Körper einzeichnen", "Analytische Geometrie", "Spiegelung",
     "Die Gleichung der Symmetrieebene eines Körpers angeben und die Schnittfigur dieser Ebene mit dem Körper in das Schrägbild einzeichnen.", "2019MgrundlegendBAGLAA2WTR2-1b"),
    ("Punkt und Ebene: Verlauf zweier Ebenen durch das Innere eines Körpers über Punktproben und Vorzeichen untersuchen", "Analytische Geometrie", "Lagebeziehungen",
     "Für Ebenen durch den Ursprung entscheiden, ob sie das Innere eines Körpers treffen, über Punktproben mit Eckpunkten bzw. ein Vorzeichenargument für die Koordinaten im Körper.", "2019MgrundlegendBAGLAA2WTR2-1c"),
    ("Skalarprodukt zweier Sachvektoren als Gesamtpreis deuten", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Das Skalarprodukt eines Mengenvektors mit einem Preisvektor als Gesamtkosten im Sachzusammenhang beschreiben.", "2019MgrundlegendBAGLAA2WTR2-1d"),
    ("Mengen aus einem Mischungsverhältnis und einem vorgegebenen Skalarprodukt berechnen", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Einen Mengenvektor über ein Verhältnis mit einem Faktor ansetzen und den Faktor aus einem vorgegebenen Skalarprodukt mit dem Preisvektor berechnen.", "2019MgrundlegendBAGLAA2WTR2-1e"),
    ("Körper: Anteil der Bodenfläche unter einer Mindesthöhe über den Strahlensatz am Dachquerschnitt berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Den Anteil einer Grundfläche bestimmen, über dem ein schräges Dach eine Mindesthöhe unterschreitet, über den linearen Höhenverlauf im Querschnitt.", "2019MgrundlegendBAGLAA2WTR2-1f"),
    ("Wahrscheinlichkeit einer prozentualen Abweichung vom Erwartungswert nach beiden Seiten berechnen", "Stochastik", "Binomialverteilung",
     "Die Wahrscheinlichkeit berechnen, dass eine binomialverteilte Zufallsgröße um höchstens einen vorgegebenen Prozentsatz vom Erwartungswert abweicht, über ein symmetrisches Intervall.", "2019MgrundlegendBStochastikWTR1-1a"),
    ("Kumulierte Binomialwahrscheinlichkeit und Pfadwahrscheinlichkeit einer festen Anfangsfolge berechnen", "Stochastik", "Binomialverteilung",
     "Für ein Ziehen mit Zurücklegen die Wahrscheinlichkeit eines Mehr-als-Ereignisses kumuliert und die Wahrscheinlichkeit einer festen Anfangsfolge als Potenz berechnen.", "2019MgrundlegendBStochastikWTR2-1a"),
    ("Laplace-Experiment: Kleinere Gesamtzahl von Kugeln aus gekürzten Anteilen begründen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Zeigen, dass vorgegebene Prozentanteile in einer Urne mit weniger als 100 Kugeln realisierbar sind, indem die Anteile auf einen gemeinsamen kleineren Nenner gekürzt werden.", "2019MgrundlegendBStochastikWTR2-1b"),
    ("Wahrscheinlichkeit eines Gewinns über alle günstigen Summenpfade nachweisen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Eine vorgegebene Gewinnwahrscheinlichkeit nachweisen, indem alle Ergebnisfolgen mit positiver Summe über Pfad- und Summenregel zusammengezählt werden.", "2019MgrundlegendBStochastikWTR2-2b"),
    ("Erwartungswert eines Spielgewinns über die Pfade eines Baumdiagramms berechnen", "Stochastik", "Kenngrößen von Verteilungen",
     "Den Erwartungswert des Gewinns eines zweistufigen Spiels aus allen Pfaden eines Baumdiagramms mit ihren Summen und Wahrscheinlichkeiten berechnen.", "2019MgrundlegendBStochastikWTR2-2c"),
    ("Laplace-Experiment: Wahrscheinlichkeitsterm nach Hinzufügen von Kugeln als Anteil begründen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Einen Term der Form (p · n + k)/(n + m) als Laplace-Wahrscheinlichkeit nach dem Hinzufügen von Kugeln über Zähler und Nenner als Anzahlen begründen.", "2019MgrundlegendBStochastikWTR2-3a"),
    ("Laplace-Experiment: Zunahme einer Wahrscheinlichkeit nach Hinzufügen von Kugeln über eine Termdifferenz begründen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Begründen, dass eine Laplace-Wahrscheinlichkeit nach dem Hinzufügen von Kugeln wächst, indem die Differenz der Terme gebildet und als positiv nachgewiesen wird.", "2019MgrundlegendBStochastikWTR2-3b"),
    ("Vierfeldertafel mit absoluten Häufigkeiten aus Gruppengrößen und bedingten Anteilen vervollständigen", "Stochastik", "Vierfeldertafel",
     "Aus den Größen zweier Gruppen und je einem bedingten Anteil die Vierfeldertafel mit absoluten Häufigkeiten und Randsummen ausfüllen.", "2019MgrundlegendBStochastikWTR3-1a"),
    ("Bedingte Wahrscheinlichkeit aus der Vierfeldertafel mit absoluten Häufigkeiten angeben", "Stochastik", "Bedingte Wahrscheinlichkeit und Bayes",
     "Eine bedingte Wahrscheinlichkeit als Quotient zweier absoluter Häufigkeiten aus der Vierfeldertafel angeben.", "2019MgrundlegendBStochastikWTR3-1c"),
    ("Term und Ereignis: Zufallsexperiment und Ereignis zu einer Potenz der Gegenwahrscheinlichkeit beschreiben", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Zu einem Term der Form 1 − pⁿ ein passendes Zufallsexperiment (Ziehen mit Zurücklegen) und das zugehörige Gegenereignis im Sachzusammenhang beschreiben.", "2019MgrundlegendBStochastikWTR3-2a"),
    ("Untere Schranke für eine Kugelbeschriftung aus dem Erwartungswert der Summe ohne Rechnung begründen", "Stochastik", "Kenngrößen von Verteilungen",
     "Ohne Wahrscheinlichkeiten begründen, dass eine unbekannte Kugelbeschriftung größer als ein Wert sein muss, weil sonst der Erwartungswert der Summe nicht erreicht werden könnte.", "2019MgrundlegendBStochastikWTR3-2b"),
    ("Kugelbeschriftung aus dem Erwartungswert der Summe beim Ziehen ohne Zurücklegen berechnen", "Stochastik", "Kenngrößen von Verteilungen",
     "Die Verteilung der Summe zweier ohne Zurücklegen gezogener Kugeln mit einer unbekannten Beschriftung aufstellen und die Unbekannte aus dem vorgegebenen Erwartungswert berechnen.", "2019MgrundlegendBStochastikWTR3-2c"),
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
