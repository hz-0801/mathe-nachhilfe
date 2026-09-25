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
    "stapel": "2017-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dateidublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2017MgrundlegendBAnalysisWTR": 40,
        "2017MgrundlegendBAGLAA2WTR1": 20, "2017MgrundlegendBAGLAA2WTR2": 20,
        "2017MgrundlegendBStochastikWTR1": 20, "2017MgrundlegendBStochastikWTR2": 20,
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
# Stapel 2017-ga-B, WTR-Zweig (Reserve, geöffnet im Auftrag Nacht 2026-09-27 wegen des
# Landeshefts 2017-be-gk – Regel „Eine Vormerkung überlebt keinen Auftrag“, iqb.md § 7):
# Aufgabe 3.1 (Smartphone) des Hefts ist Stochastik WTR 1 (1 a, b = 3.1 a, b; 2 a, b, d, e =
# 3.1 c, d, f, g wortgleich; 2 c ↔ 3.1 e abgewandelt). Fünf WTR-Dateien, 40 + 20 + 20 + 20 + 20
# BE; Standardbezug mit Spalte Anforderungsbereich. Die CAS-Dateien (2017-iqb-ga-mms) bleiben
# Reserve. Keine Dateidublette, keine Aufgabendublette.
# ---- Analysis WTR (Aufgabe 1: Senke mit Fluss, 31 BE; Aufgabe 2: Funktion vierten Grades, 9 BE)
ANA = ("Querschnitt einer Senke mit Fluss: Profillinie f(x) = −5x^2 · e^x + 1 für −6 <= x <= 0; linke Uferzone "
       "waagerecht in Höhe f(−6) links von x = −6, rechte Uferzone waagerecht in Höhe 1 rechts von x = 0 (Strecken "
       "parallel zur x-Achse, lückenlos an den Graphen anschließend); die Wasseroberfläche ist ein Abschnitt der "
       "x-Achse; 1 LE = 1 m; gegeben f'(x) = −5x · (2 + x) · e^x, f''(x) = −10e^x − 20x · e^x − 5x^2 · e^x und die "
       "Stammfunktion F(x) = x − 5 · (x^2 − 2x + 2) · e^x")
ANA_SK = ("Abbildung 1: Koordinatensystem auf Kästchengitter (eine Einheit = zwei Kästchen), x von −9 bis 3, y von −2 "
          "bis 1,5; linke Uferzone waagerecht in Höhe etwa 0,55 bis x = −6, der Graph von f fällt von dort, schneidet "
          "die x-Achse bei etwa −4,7, hat den Tiefpunkt bei etwa (−2; −1,7), steigt steil, schneidet die x-Achse bei "
          "etwa −0,6 und endet in (0; 1); rechte Uferzone waagerecht in Höhe 1 ab x = 0; die Fläche zwischen x-Achse "
          "und Graph (Flussquerschnitt) ist grau; Beschriftungen linke Uferzone, rechte Uferzone, Senke")
BRUECKE = "; über die Senke führt eine Brücke (Strecke), ihr Auflagepunkt am rechten Ufer ist B(0; 1,1), ihr linkes Ende liegt auf der linken Uferzone"
row("2017MgrundlegendBAnalysisWTR", "a", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Höhen an den Rändern einer Profillinie als Funktionswerte berechnen", typ_neben="",
    stichwoerter="Höhe der rechten Uferzone f(0) = 1|Höhe der linken Uferzone f(−6) ≈ 0,55|Differenz etwa 45 cm",
    voraussetzungen="Funktionswerte mit e-Funktion am Rechner|Meter in Zentimeter umrechnen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ANA_SK, kontext="Gelände/Fluss", textumfang="kurz",
    gegeben=ANA,
    gesucht="Höhenunterschied zwischen den beiden Uferzonen",
    verfahren="Die Höhen der Uferzonen als f(0) = 1 und f(−6) berechnen und subtrahieren",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="m|cm", abhaengig_von="",
    ergebnis="f(0) − f(−6) ≈ 0,45, d. h. der Höhenunterschied beträgt etwa 45 cm (amtlich)",
    zwischenergebnis="f(−6) = 1 − 180 · e^(−6) ≈ 0,554|f(0) = 1", niveau_geschaetzt="I",
    fehlerquelle="die Höhe der linken Uferzone mit 0 statt mit f(−6) ansetzen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,446 m). Typ wiederverwendet.")
row("2017MgrundlegendBAnalysisWTR", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen", typ_neben="",
    stichwoerter="einen Meter unter der Wasseroberfläche heißt f(x) = −1|zwei Stellen etwa −3,3 und −1,1|Breite etwa 2,2 m",
    voraussetzungen="Wasseroberfläche als x-Achse deuten|Stellen zu einem Funktionswert am Gitter ablesen",
    format="Kurzantwort", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ANA_SK, kontext="Gelände/Fluss", textumfang="kurz",
    gegeben=ANA + "; Abbildung 1",
    gesucht="Breite der Senke einen Meter unterhalb der Wasseroberfläche, mithilfe von Abbildung 1",
    verfahren="In Abbildung 1 die beiden Stellen ablesen, an denen der Graph den Wert −1 annimmt, und ihren Abstand bilden",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Einen Meter unterhalb der Wasseroberfläche ist die Senke etwa 2,2 m breit (amtlich)",
    zwischenergebnis="f(x) = −1 bei x ≈ −3,31 und x ≈ −1,09", niveau_geschaetzt="I",
    fehlerquelle="die Breite an der Wasseroberfläche (y = 0) statt bei y = −1 ablesen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich (Ablesung, im Erwartungshorizont eingezeichnet), eigene Rechnung: 2,22 m. Typ wiederverwendet; hier zwei Stellen zu demselben Wert und ihr Abstand.")
row("2017MgrundlegendBAnalysisWTR", "c", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Funktionalgleichung mit Zeitverschiebung grafisch lösen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="f(x + 3) = f(x)|zwei Punkte der Profillinie auf gleicher Höhe, 3 m voneinander entfernt|waagerechte Sehne der Länge 3|x ≈ −3,9",
    voraussetzungen="Verschiebung des Arguments als waagerechten Abstand deuten|Gleichung am Graphen lösen",
    format="Kurzantwort", operator="Deuten Sie|Bestimmen Sie", antwort="Text|Zahl",
    material="Koordinatensystem", skizze=ANA_SK, kontext="Gelände/Fluss", textumfang="kurz",
    gegeben=ANA + "; Abbildung 1; Gleichung f(x + 3) = f(x)",
    gesucht="Deutung der Gleichung im Sachzusammenhang und eine Lösung mithilfe von Abbildung 1",
    verfahren="Die Gleichung verlangt zwei Punkte der Profillinie auf gleicher Höhe mit 3 m waagerechtem Abstand; in Abbildung 1 eine waagerechte Strecke der Länge 3 zwischen linkem und rechtem Hang suchen und ihren linken Endpunkt ablesen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Die Lösung der Gleichung liefert den Punkt der Profillinie der Senke, für den der auf gleicher Höhe gegenüberliegende Punkt der Profillinie 3 m entfernt ist; x ≈ −3,9 (amtlich)",
    zwischenergebnis="f(−3,86) = f(−0,86) ≈ −0,57", niveau_geschaetzt="III",
    fehlerquelle="f(x + 3) als um 3 nach oben verschobenen Graphen deuten",
    bemerkung="Standardbezug: K2 III, K3 II, K4 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (x ≈ −3,86). Erste Schätzung II; bei der Prüfung gegen die enge Fassung auf III gesetzt – die Gleichung ist erst in eine geometrische Bedingung (waagerechte Sehne der Länge 3) zu übersetzen, die dann am Graphen gelöst wird (Deutungsliste (a) und (d)). Typ wiederverwendet: Verschiebung im Ort statt in der Zeit, ohne Höhenunterschied.")
row("2017MgrundlegendBAnalysisWTR", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen", typ_neben="",
    stichwoerter="Produktregel für −5x^2 · e^x|−10x · e^x − 5x^2 · e^x|−5x · e^x ausklammern",
    voraussetzungen="Produktregel|Ableitung von e^x|Ausklammern",
    format="Rechnung", operator="Leiten Sie her", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = −5x^2 · e^x + 1; angegebene Ableitung f'(x) = −5x · (2 + x) · e^x",
    gesucht="Herleitung der angegebenen Gleichung von f' aus der Funktionsgleichung von f",
    verfahren="Produktregel auf −5x^2 · e^x anwenden, die Konstante fällt weg, und −5x · e^x ausklammern",
    schritte="2", zahlenraum="ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −10x · e^x − 5x^2 · e^x = −5x · (2 + x) · e^x (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Ableitung von e^x als x · e^(x − 1) bilden oder die Konstante 1 mitableiten",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung I (eine Anwendung der Produktregel mit Ausklammern, wie 2024-ga-B Analysis WTR 1 1 a, dort amtlich I); der amtliche Bereich ist II (K5 II). Typ wiederverwendet.")
row("2017MgrundlegendBAnalysisWTR", "e", innen="1", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen", typ_neben="",
    stichwoerter="Tiefpunkt zwischen −2,5 und −1,5 an der Abbildung|f'(x) = 0 ⇔ x = −2 im Intervall|f(−2) ≈ −1,7|Wassertiefe 1,7 m",
    voraussetzungen="Satz vom Nullprodukt an der faktorisierten Ableitung|Randstelle x = 0 ausschließen|Tiefe von der Wasseroberfläche aus messen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ANA_SK, kontext="Gelände/Fluss", textumfang="kurz",
    gegeben=ANA + "; Abbildung 1",
    gesucht="Tiefe des Wassers an der tiefsten Stelle der Senke",
    verfahren="An der Abbildung die Tiefstelle zwischen −2,5 und −1,5 eingrenzen, dort f'(x) = 0 mit der faktorisierten Ableitung lösen (x = −2) und f(−2) berechnen; die Wasseroberfläche liegt auf der x-Achse",
    schritte="3", zahlenraum="dezimal|negativ|Potenz", einheiten="m", abhaengig_von="",
    ergebnis="Für x ∈ [−2,5; −1,5] gilt f'(x) = 0 ⇔ x = −2; f(−2) ≈ −1,7; die Tiefe des Wassers beträgt an der tiefsten Stelle etwa 1,7 m (amtlich)",
    zwischenergebnis="f(−2) = 1 − 20 · e^(−2) ≈ −1,707", niveau_geschaetzt="I",
    fehlerquelle="die Nullstelle x = 0 der Ableitung (Rand der Senke) als Tiefstelle nehmen oder die Tiefe von der Uferzone aus messen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (1,707 m). Erste Schätzung II; bei der Prüfung gegen die enge Fassung auf I gesetzt – ein Extrempunkt über die gegebene faktorisierte Ableitung ist ein einzelnes Standardverfahren, die Art liefert die Abbildung (wie alle Poolzeilen des Typs, I). Typ wiederverwendet, hier für einen Tiefpunkt.")
row("2017MgrundlegendBAnalysisWTR", "f", innen="1", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Streckenlänge im Raum berechnen",
    typ_neben="Neigung einer Strecke in Prozent aus Höhendifferenz und Horizontalabstand berechnen",
    stichwoerter="Brücke von A(−6; f(−6)) nach B(0; 1,1)|Länge √(6^2 + (1,1 − f(−6))^2) ≈ 6,0 m|Steigung (1,1 − f(−6))/6 ≈ 9 %",
    voraussetzungen="Abstand zweier Punkte mit dem Satz des Pythagoras|Steigung als Quotient aus Höhendifferenz und waagerechtem Abstand in Prozent",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ANA_SK, kontext="Gelände/Brücke", textumfang="mittel",
    gegeben=ANA + BRUECKE + "; linker Auflagepunkt im Modell A(−6; f(−6))",
    gesucht="Länge der Brücke und ihre Steigung in Prozent",
    verfahren="f(−6) ≈ 0,554 berechnen; Länge als √(6^2 + (1,1 − f(−6))^2), Steigung als (1,1 − f(−6))/6",
    schritte="3", zahlenraum="dezimal|Wurzel|Prozent", einheiten="m|%", abhaengig_von="",
    ergebnis="√(6^2 + (1,1 − f(−6))^2) ≈ 6,0, d. h. die Brücke ist etwa 6,0 m lang; (1,1 − f(−6))/6 ≈ 9 % (amtlich)",
    zwischenergebnis="1,1 − f(−6) ≈ 0,546|Länge ≈ 6,02 m|Steigung ≈ 9,1 %", niveau_geschaetzt="I",
    fehlerquelle="den Höhenunterschied zur x-Achse statt zur linken Uferzone nehmen oder die Steigung als Winkel angeben",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (6,025 m; 9,10 %). Erste Schätzung II; bei der Prüfung gegen die enge Fassung auf I gesetzt – zwei voneinander unabhängige einzelne Rechnungen (Streckenlänge, Steigung), keine Verkettung. Typ wiederverwendet (Strecke in der Ebene statt im Raum), Nebentyp für die Steigung; leitidee folgt dem Typ, die Aufgabe steht in der Analysis-Datei.")
row("2017MgrundlegendBAnalysisWTR", "g", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Horizontalabstand aus vorgegebener Neigung in Prozent und Höhendifferenz berechnen", typ_neben="",
    stichwoerter="Steigung 6 %|(1,1 − f(−6))/Δx = 0,06|Δx ≈ 9,1|Rand der Senke bei x = −6, Entfernung 3,1 m",
    voraussetzungen="Steigung in Prozent als Quotient|Gleichung nach dem Nenner auflösen|Bezugspunkt Rand der Senke",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ANA_SK, kontext="Gelände/Brücke", textumfang="mittel",
    gegeben=ANA + BRUECKE + " (Höhe f(−6)); die Brücke soll eine Steigung von 6 % haben",
    gesucht="Entfernung des linken Brückenendes vom Rand der Senke",
    verfahren="(1,1 − f(−6))/Δx = 0,06 nach dem waagerechten Abstand Δx zwischen den Auflagepunkten auflösen; der Rand der Senke liegt bei x = −6, also ist die Entfernung Δx − 6",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="m", abhaengig_von="",
    ergebnis="(1,1 − f(−6))/Δx = 0,06 liefert Δx ≈ 9,1; das Ende der Brücke läge 3,1 m vom Rand der Senke entfernt (amtlich)",
    zwischenergebnis="Δx ≈ 9,10", niveau_geschaetzt="III",
    fehlerquelle="Δx selbst als Entfernung vom Rand der Senke angeben",
    bemerkung="Standardbezug: K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Δx ≈ 9,103). Erste Schätzung II; bei der Prüfung gegen die enge Fassung auf III gesetzt – die Sachbedingung (Brücke mit 6 %, Ende auf der linken Uferzone) ist erst in eine Gleichung zu übersetzen und das Ergebnis auf den Rand der Senke umzurechnen (Deutungsliste (a)). Neuer Typ: Umkehrung von „Neigung einer Strecke in Prozent …“ (waagerechter Abstand gesucht); leitidee folgt dem Typ.")
row("2017MgrundlegendBAnalysisWTR", "h", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Maximalen Neigungswinkel über die Wendestelle berechnen und mit einer Schranke vergleichen", typ_neben="",
    stichwoerter="größte Steigung zwischen Tiefpunkt und rechtem Rand|f''(x) = 0 ⇔ x^2 + 4x + 2 = 0|x = −2 + √2|tan α = f'(−2 + √2), α ≈ 67°",
    voraussetzungen="Stelle größter Steigung als Wendestelle|quadratische Gleichung lösen|Steigungswinkel über den Arkustangens",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ANA_SK, kontext="Gelände/Fluss", textumfang="mittel",
    gegeben=ANA + "; betrachtet wird die Profillinie zwischen dem tiefsten Punkt der Senke (x = −2) und ihrem rechten Rand (x = 0)",
    gesucht="Größe des größten Neigungswinkels der Profillinie gegenüber der Horizontalen in diesem Bereich",
    verfahren="Die Stelle größter Steigung ist Wendestelle: f''(x) = 0 ⇔ x^2 + 4x + 2 = 0, im Bereich x = −2 + √2; dort tan α = f'(−2 + √2)",
    schritte="3", zahlenraum="Wurzel|dezimal|negativ", einheiten="°", abhaengig_von="2017MgrundlegendBAnalysisWTR-1e",
    ergebnis="Für x ∈ ]−2; 0[ gilt f''(x) = 0 ⇔ x^2 + 4x + 2 = 0 ⇔ x = −2 + √2; tan α = f'(−2 + √2), d. h. α ≈ 67° (amtlich)",
    zwischenergebnis="x ≈ −0,586|f'(−2 + √2) ≈ 2,31|α ≈ 66,6°", niveau_geschaetzt="II",
    fehlerquelle="die Lösung −2 − √2 außerhalb des Bereichs nehmen oder tan α mit f statt mit f' ansetzen",
    bemerkung="Standardbezug: K3 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (66,55°). Typ wiederverwendet, hier ohne Vergleich mit einer Schranke.")
row("2017MgrundlegendBAnalysisWTR", "i", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Wasservolumen in einer Mulde aus Fläche zwischen Wasserlinie und Graph mal Breite berechnen", typ_neben="",
    stichwoerter="Durchflussrate = Querschnittsfläche mal Fließgeschwindigkeit|Grenzen −4,7 und −0,6|Stammfunktion F gegeben|Betrag des Integrals|2,1 m^3/s",
    voraussetzungen="Integral mit gegebener Stammfunktion|Fläche unterhalb der x-Achse als Betrag|Einheiten m^2 · m/s = m^3/s",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ANA_SK, kontext="Gelände/Fluss", textumfang="mittel",
    gegeben=ANA + "; die Wasseroberfläche wird im Modell näherungsweise durch x ≈ −4,7 und x ≈ −0,6 begrenzt; Fließgeschwindigkeit 0,5 m/s; Durchflussrate = Flächeninhalt des Flussquerschnitts (in m^2) mal Fließgeschwindigkeit (in m/s)",
    gesucht="Durchflussrate",
    verfahren="Den Flächeninhalt des Flussquerschnitts als Betrag des Integrals von −4,7 bis −0,6 über f mit der Stammfunktion F berechnen und mit 0,5 multiplizieren",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="m^2|m/s|m^3/s", abhaengig_von="",
    ergebnis="0,5 · |∫ von −4,7 bis −0,6 f(x) dx| = 0,5 · |[x − 5 · (x^2 − 2x + 2) · e^x] von −4,7 bis −0,6| ≈ 2,1; die Durchflussrate beträgt 2,1 m^3/s (amtlich)",
    zwischenergebnis="∫ von −4,7 bis −0,6 f(x) dx ≈ −4,15", niveau_geschaetzt="II",
    fehlerquelle="das negative Integral ohne Betrag übernehmen",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (2,07). Typ wiederverwendet: Fläche zwischen Wasserlinie und Graph mal Faktor, hier die Fließgeschwindigkeit statt der Breite, Grenzen vorgegeben.")
G2 = "ganzrationale Funktion g vierten Grades, in IR definiert; Abbildung 2 zeigt ihren Graphen"
G2_SK = ("Abbildung 2: Koordinatensystem auf Kästchengitter, x von −1 bis 8, y von −1 bis 8; der Graph von g kommt steil "
         "von oben links, hat den Tiefpunkt (0; 4) und den Hochpunkt (2; 5), fällt durch die Nullstelle bei etwa 5 zum "
         "Tiefpunkt bei etwa (6; −1) und steigt durch die Nullstelle bei etwa 7 steil nach oben")
row("2017MgrundlegendBAnalysisWTR", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Extrempunkte: Fehlen weiterer Extrempunkte über die Höchstzahl nach dem Grad begründen", typ_neben="",
    stichwoerter="Grad 4, Ableitung dritten Grades|höchstens drei Extrempunkte|drei Extrempunkte im Bild",
    voraussetzungen="Zahl der Nullstellen einer ganzrationalen Funktion höchstens gleich dem Grad|Extrempunkte am Graphen erkennen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=G2_SK, kontext="ohne", textumfang="kurz",
    gegeben=G2,
    gesucht="Begründung, dass der Graph von g außerhalb des abgebildeten Bereichs keine Extrempunkte besitzt",
    verfahren="Die Ableitung ist ganzrational vom Grad 3 und hat höchstens drei Nullstellen, also hat der Graph höchstens drei Extrempunkte; drei sind im Bild zu sehen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Als Graph einer ganzrationalen Funktion vierten Grades hat der Graph von g höchstens drei Extrempunkte; diese liegen im dargestellten Bereich (amtlich)",
    zwischenergebnis="Extrempunkte etwa (0; 4), (2; 5), (6; −1)", niveau_geschaetzt="II",
    fehlerquelle="nur mit dem Verlauf am Bildrand argumentieren",
    bemerkung="Standardbezug: K1 II, K4 II, K5 II. AB amtlich: II. Amtlich. Neuer Typ: der vorhandene Typ zur Existenz eines Hochpunkts aus dem Grad schließt auf einen weiteren Extrempunkt, hier wird die Höchstzahl ausgeschöpft.")
row("2017MgrundlegendBAnalysisWTR", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Werte a mit vorgegebener Lösungsanzahl von f(x) = a über die lokalen Extremwerte am Graphen angeben", typ_neben="",
    stichwoerter="Lösungen von g(x) = a als Schnittstellen mit der Parallelen y = a|genau drei Lösungen bei Berührung im Tief- oder Hochpunkt|a = 4 und a = 5",
    voraussetzungen="Gleichung grafisch als Schnitt mit einer Parallelen zur x-Achse lösen|lokale Extremwerte ablesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=G2_SK, kontext="ohne", textumfang="kurz",
    gegeben=G2 + "; betrachtet wird die Gleichung g(x) = a mit a ∈ IR",
    gesucht="alle Werte von a, für die die Gleichung genau drei Lösungen hat",
    verfahren="Lösungen als Schnittstellen des Graphen mit der Parallelen y = a deuten; genau drei, wenn die Parallele den Graphen im Tiefpunkt (0; 4) oder im Hochpunkt (2; 5) berührt (für 4 < a < 5 sind es vier)",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="a = 4 und a = 5 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Intervall 4 < a < 5 angeben, in dem es vier Lösungen gibt",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II. AB amtlich: II. Amtlich. Neuer Typ.")
row("2017MgrundlegendBAnalysisWTR", "c", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Vorzeichen von erster und zweiter Ableitung an einer Stelle aus Monotonie und Krümmung am Graphen bestimmen", typ_neben="",
    stichwoerter="g'(3) · g''(3)|bei x = 3 streng monoton fallend, g'(3) < 0|rechtsgekrümmt vor der Wendestelle, g''(3) < 0|Produkt positiv",
    voraussetzungen="Vorzeichen von g' als Monotonie|Vorzeichen von g'' als Krümmung|Lage der Wendestelle zwischen Hoch- und Tiefpunkt abschätzen",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=G2_SK, kontext="ohne", textumfang="kurz",
    gegeben=G2,
    gesucht="Untersuchung, ob der Wert des Terms g'(3) · g''(3) positiv ist",
    verfahren="Am Graphen: bei x = 3 fällt der Graph (g'(3) < 0) und ist rechtsgekrümmt, weil die Wendestelle zwischen dem Hochpunkt bei 2 und dem Tiefpunkt bei 6 rechts von 3 liegt (g''(3) < 0); das Produkt zweier negativer Zahlen ist positiv",
    schritte="3", zahlenraum="negativ", einheiten="", abhaengig_von="",
    ergebnis="Der Graph von g ist im Punkt (3; g(3)) streng monoton fallend und rechtsgekrümmt; damit ist g'(3) < 0 und g''(3) < 0, der Wert des Terms also positiv (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="aus dem Fallen allein auf einen negativen Wert schließen oder die Krümmung bei x = 3 als Linkskrümmung lesen",
    bemerkung="Standardbezug: K1 III, K4 II, K6 II. AB amtlich: III. Amtlich. Erste Schätzung II; bei der Prüfung gegen die enge Fassung auf III gesetzt – der Term ist über zwei verkettete Deutungen (g' als Monotonie, g'' als Krümmung) in Aussagen über den Graphen zu übersetzen, die Lage der Wendestelle ist erst abzuschätzen (Deutungsliste (d) sinngemäß). Neuer Typ.")
# ---- AG/LA (A2) WTR 1: Pagode, 20 BE
PAG = ("Pagode mit drei Dachetagen aus je vier Dachflächen gleicher Form und Größe; die Dachflächen der mittleren und "
       "oberen Etage sind jeweils parallel zu einer Dachfläche der unteren Etage; die Dachflächen der unteren Etage sind "
       "Vierecke mit den Eckpunkten A1(5,5; −5,5; 6), B1(5,5; 5,5; 6), C1(−5,5; 5,5; 6), D1(−5,5; −5,5; 6), "
       "A2(2; −2; 8,1), B2(2; 2; 8,1), C2(−2; 2; 8,1) und D2(−2; −2; 8,1); die xy-Ebene ist die Horizontale, 1 LE = 1 m")
PAG_SK = ("Foto der Pagode mit drei Dachetagen; darunter ein räumliches Koordinatensystem im Schrägbild auf Kästchengitter "
          "(x-Achse schräg nach vorn links, y-Achse nach rechts, z-Achse nach oben, Achsen bis etwa 8), eingetragen sind "
          "nur die Punkte A1, B1, C1 und D1")
row("2017MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Viereck in ein Schrägbild einzeichnen", typ_neben="",
    stichwoerter="A2, B2, C2, D2 in Höhe 8,1 eintragen|vier Trapeze der unteren Dachetage|Kanten A1A2, B1B2, C1C2, D1D2",
    voraussetzungen="Punkte im Schrägbild eintragen|x-Richtung verkürzt entlang der schrägen Achse",
    format="Zeichnen", operator="Zeichnen Sie ein", antwort="Grafik",
    material="Koordinatensystem|Foto", skizze=PAG_SK, kontext="Architektur/Pagode", textumfang="mittel",
    gegeben=PAG,
    gesucht="die fehlenden Eckpunkte A2, B2, C2, D2 und die Strecken der Kanten der Dachflächen der unteren Etage im abgebildeten Koordinatensystem",
    verfahren="A2 bis D2 im Schrägbild eintragen und die Vierecke A1B1B2A2, B1C1C2B2, C1D1D2C2 und D1A1A2D2 zeichnen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="A2, B2, C2, D2 eingetragen; Kanten A1B1, B1C1, C1D1, D1A1, A2B2, B2C2, C2D2, D2A2 sowie A1A2, B1B2, C1C2, D1D2 gezeichnet (amtlich); die Zeichnung steht im Erwartungshorizont",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die x-Koordinate nicht entlang der schrägen Achse abtragen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (2019-ga-B, gleiche Aufgabenform).")
row("2017MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Trapez mit zwei gleich langen Seiten über Kollinearität und Seitenlängen nachweisen", typ_neben="",
    stichwoerter="A1B1 = (0; 11; 0) und A2B2 = (0; 4; 0) kollinear|A1A2 und B1B2 gleich lang, √28,91 ≈ 5,38|parallele Seiten 11 und 4 verschieden lang, kein Parallelogramm",
    voraussetzungen="Kollinearität als Vielfaches|Vektorbetrag|Parallelogramm hat gleich lange parallele Seiten",
    format="Rechnung|Begründung", operator="Zeigen Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Architektur/Pagode", textumfang="kurz",
    gegeben=PAG,
    gesucht="rechnerischer Nachweis, dass das Viereck A1B1B2A2 ein Trapez ist, in dem zwei gegenüberliegende Seiten gleich lang sind; Begründung, dass es kein Parallelogramm ist",
    verfahren="A1B1 und A2B2 als kollinear nachweisen, |A1A2| = |B1B2| berechnen; weil die parallelen Seiten verschieden lang sind (11 und 4), ist es kein Parallelogramm",
    schritte="3", zahlenraum="dezimal|Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="A1B1 und A2B2 sind kollinear und |A1A2| = |B1B2|; da |A1B1| ≠ |A2B2|, ist A1B1B2A2 kein Parallelogramm (amtlich)",
    zwischenergebnis="A1A2 = (−3,5; 3,5; 2,1)|B1B2 = (−3,5; −3,5; 2,1)|beide Längen √28,91 ≈ 5,38", niveau_geschaetzt="II",
    fehlerquelle="die gleich langen Seiten A1A2 und B1B2 als Beleg für ein Parallelogramm nehmen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2019-ga-B); hier zusätzlich der Ausschluss des Parallelogramms über die verschieden langen parallelen Seiten.")
row("2017MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Mittelpunkt einer Strecke im Raum bestimmen",
    typ_neben="Ebene Figur: Flächeninhalt eines Trapezes im Raum über die Höhe zwischen den parallelen Seiten berechnen",
    stichwoerter="M1(5,5; 0; 6), M2(2; 0; 8,1)|Höhe des symmetrischen Trapezes als Länge von M1M2 ≈ 4,08|Trapezfläche ≈ 30,6 m^2|vier gleiche Dachflächen, etwa 122 m^2",
    voraussetzungen="Mittelpunkt als halbe Summe der Ortsvektoren|Trapezformel|Symmetrie des Trapezes für die Höhe",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Architektur/Pagode", textumfang="kurz",
    gegeben=PAG + "; A1B1B2A2 ist ein Trapez mit zwei gleich langen Schenkeln",
    gesucht="Koordinaten der Mittelpunkte M1 und M2 der Seiten A1B1 bzw. A2B2; gesamter Inhalt der Dachflächen der unteren Etage in Quadratmetern",
    verfahren="M1 und M2 als halbe Summen; |M1M2| = √(3,5^2 + 2,1^2) ist die Höhe des symmetrischen Trapezes; Fläche 1/2 · (11 + 4) · |M1M2|, mal vier",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="m^2", abhaengig_von="2017MgrundlegendBAGLAA2WTR1-1b",
    ergebnis="M1(5,5; 0; 6), M2(2; 0; 8,1); 1/2 · (|A1B1| + |A2B2|) · |M1M2| ≈ 30,6; der gesamte Inhalt der Dachflächen der unteren Etage beträgt etwa 122 m^2 (amtlich)",
    zwischenergebnis="Länge M1M2 ≈ 4,08|Trapezfläche ≈ 30,6 m^2", niveau_geschaetzt="II",
    fehlerquelle="die Schenkellänge |A1A2| statt |M1M2| als Höhe nehmen oder nur eine Dachfläche angeben",
    bemerkung="Standardbezug: K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (122,45 m^2; M1M2 senkrecht zu A1B1). Typ und Nebentyp wiederverwendet; die vier Dachflächen sind gleich (Symmetrie der Pagode).")
row("2017MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen", typ_neben="",
    stichwoerter="g durch A1 und A2|Richtungsvektor (−3,5; 3,5; 2,1)|x = 0 liefert λ = 11/7|Schnittpunkt (0; 0; 9,3)",
    voraussetzungen="Geradengleichung durch zwei Punkte|Punkte der z-Achse haben x = y = 0",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Architektur/Pagode", textumfang="kurz",
    gegeben=PAG + "; die Strecke A1A2 ist Teil einer Geraden g",
    gesucht="Koordinaten des Schnittpunkts von g mit der z-Achse",
    verfahren="g: x = (5,5; −5,5; 6) + λ · (−3,5; 3,5; 2,1); aus x = 0 folgt λ = 11/7, damit y = 0 und z = 9,3",
    schritte="3", zahlenraum="dezimal|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="g: x = (5,5; −5,5; 6) + λ · (−3,5; 3,5; 2,1), λ ∈ IR; 5,5 − 3,5λ = 0 ⇔ λ = 11/7; 6 + 2,1 · 11/7 = 9,3; damit (0; 0; 9,3) (amtlich)",
    zwischenergebnis="λ = 11/7", niveau_geschaetzt="I",
    fehlerquelle="nur x = 0 einsetzen und nicht bestätigen, dass dann auch y = 0 ist",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet: die Kantengerade trifft die z-Achse in der Spitze der gedachten Dachpyramide.")
row("2017MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="E: 3x + 5z = 46,5|Normalenvektoren (0; 0; 1) und (3; 0; 5)|cos φ = 5/√34|φ ≈ 31°",
    voraussetzungen="Neigungswinkel zweier Ebenen als Winkel ihrer Normalenvektoren|Normalenvektor der xy-Ebene",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Architektur/Pagode", textumfang="kurz",
    gegeben=PAG + "; das Viereck A1B1B2A2 liegt in der Ebene E: 3x + 5z = 46,5 und stellt die untere Dachfläche der Südseite dar",
    gesucht="Größe des Neigungswinkels dieser Dachfläche gegenüber der Horizontalen",
    verfahren="Winkel zwischen m = (0; 0; 1) und n = (3; 0; 5) über den Kosinus berechnen",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="Mit m = (0; 0; 1) und n = (3; 0; 5) ergibt sich cos φ = (m ∘ n)/(|m| · |n|), d. h. φ ≈ 31° (amtlich)",
    zwischenergebnis="cos φ = 5/√34|φ ≈ 30,96°", niveau_geschaetzt="II",
    fehlerquelle="den Sinus statt des Kosinus der Normalenvektoren verwenden (Winkel zwischen Ebene und Gerade)",
    bemerkung="Standardbezug: K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Schätzung I; bei der Prüfung gegen die enge Fassung auf II gesetzt – Normalenvektor der Horizontalen wählen und die Winkelformel anwenden ist eine Verkettung von Standardschritten (alle Zeilen des Typs im Bestand II). Typ wiederverwendet.")
row("2017MgrundlegendBAGLAA2WTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Parallele Ebenen über die Normalenvektoren auswählen und über die Konstante der Koordinatengleichung der Höhe nach zuordnen", typ_neben="",
    stichwoerter="parallele Dachflächen, kollineare Normalenvektoren|nur II, III, V, VI kommen infrage|bei gleichem x wächst 3x + 5z mit z|III mittlere, VI obere Etage",
    voraussetzungen="Parallelität von Ebenen über kollineare Normalenvektoren|Konstante der Koordinatengleichung als Lagemaß bei festem x",
    format="Kurzantwort|Begründung", operator="Ordnen Sie zu|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Architektur/Pagode", textumfang="lang",
    gegeben=PAG + "; die untere Dachfläche der Südseite liegt in E: 3x + 5z = 46,5; die Dachflächen der mittleren und oberen Etage der Südseite liegen in zwei der Ebenen I: 3x + 8z = 46,5, II: 3x + 5z = 24,5, III: 3x + 5z = 58, IV: 3x + 10z = 46,5, V: 3x + 5z = 35, VI: 3x + 5z = 68,5",
    gesucht="Zuordnung der beiden Dachflächen zu je einer Gleichung mit Begründung",
    verfahren="Die drei Dachflächen der Südseite sind parallel, also sind die Normalenvektoren kollinear zu (3; 0; 5): I und IV scheiden aus; für Punkte gleicher x-Koordinate wächst 3x + 5z mit der Höhe, also müssen die Konstanten größer als 46,5 sein und mit der Etage wachsen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="III: Dachfläche der mittleren Etage, VI: Dachfläche der oberen Etage; die Normalenvektoren der drei parallelen Flächen sind kollinear (nur II, III, V, VI kommen infrage), und für Punkte gleicher x-Koordinate mit z1 < z2 < z3 gilt 3x + 5z1 < 3x + 5z2 < 3x + 5z3 (amtlich)",
    zwischenergebnis="z-Achsenabschnitte: II 4,9; V 7; E 9,3; III 11,6; VI 13,7", niveau_geschaetzt="III",
    fehlerquelle="II oder V wählen, weil ihre Normalenvektoren ebenfalls passen, ohne die Lage oberhalb der unteren Etage zu prüfen",
    bemerkung="Standardbezug: K1 III, K2 III, K3 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")
# ---- AG/LA (A2) WTR 2: Punkte A, B, C und Solarmodule, 20 BE
SOL = "Punkte A(0; 0; 1), B(2; 6; 1) und C(−4; 8; 5) in einem kartesischen Koordinatensystem"
SOLK = (SOL + "; Solarmodule auf einem Trägergestell, das an einem vertikal stehenden Metallrohr befestigt ist; die "
        "Fläche der Module ist das Rechteck ABCD mit D(−6; 2; 5), der Befestigungspunkt des Rohrs am Gestell ist "
        "M(−2; 4; 3); die x1x2-Ebene ist der horizontale Untergrund, auf dem das Rohr steht; 1 LE = 1 m; "
        "ABCD liegt in E: 3x1 − x2 + 5x3 − 5 = 0")
SOL_SK = ("Abbildung: geneigtes graues Rechteck mit A links, B unten, C rechts und D oben; auf der Fläche M, von M "
          "gestrichelt senkrecht nach unten durch die Fläche, darunter durchgezogen das senkrechte Rohr bis zum Boden")
row("2017MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Parallelität einer Geraden zu einer Koordinatenebene über die z-Koordinaten entscheiden", typ_neben="",
    stichwoerter="A und B haben die x3-Koordinate 1|Richtungsvektor (2; 6; 0)|parallel zur x1x2-Ebene",
    voraussetzungen="Parallelität zu einer Koordinatenebene über eine verschwindende Komponente des Richtungsvektors",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SOL,
    gesucht="Begründung, dass die Gerade AB parallel zur x1x2-Ebene verläuft",
    verfahren="Die x3-Koordinaten von A und B stimmen überein, also hat der Richtungsvektor die x3-Komponente 0",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die x3-Koordinaten der Punkte A und B stimmen überein (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="mit dem Normalenvektor der Ebene statt mit dem Richtungsvektor argumentieren",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich. Typ wiederverwendet; hier ohne Parameter.")
row("2017MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Mittelpunkt einer Strecke im Raum bestimmen",
    typ_neben="Rechten Winkel zwischen zwei Seiten einer Figur über das Skalarprodukt nachweisen",
    stichwoerter="M(−2; 4; 3) Mittelpunkt von AC|OM = OA + 1/2 · AC|BA ∘ BC = 0, rechter Winkel bei B",
    voraussetzungen="Mittelpunkt als halbe Summe|Skalarprodukt null heißt senkrecht",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SOL + "; M(−2; 4; 3)",
    gesucht="Nachweis, dass M der Mittelpunkt der Strecke AC ist und dass das Dreieck ABC bei B einen rechten Winkel hat",
    verfahren="OM = OA + 1/2 · AC prüfen; BA ∘ BC = (−2; −6; 0) ∘ (−6; 2; 4) = 0",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="OM = OA + 1/2 · AC; BA ∘ BC = 0 (amtlich)",
    zwischenergebnis="AC = (−4; 8; 4)|BA = (−2; −6; 0)|BC = (−6; 2; 4)", niveau_geschaetzt="I",
    fehlerquelle="den rechten Winkel mit AB ∘ AC statt am Eckpunkt B prüfen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ und Nebentyp wiederverwendet (der Typ war bisher nur Nebentyp).")
row("2017MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Vierten Eckpunkt eines Quadrats über eine Vektoraddition bestimmen", typ_neben="",
    stichwoerter="Rechteck ABCD|OD = OA + BC|D(−6; 2; 5)",
    voraussetzungen="gegenüberliegende Seiten eines Rechtecks als gleiche Vektoren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SOL + "; das Dreieck ABC hat bei B einen rechten Winkel",
    gesucht="Koordinaten des Punkts D, für den das Viereck ABCD ein Rechteck ist",
    verfahren="OD = OA + BC",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2017MgrundlegendBAGLAA2WTR2-1b",
    ergebnis="OD = OA + BC, D(−6; 2; 5) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="OD = OA + CB rechnen und so ein überschlagenes Viereck erhalten",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Rechteck statt Quadrat, dieselbe Vektoraddition).")
row("2017MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="Parameterform mit AB und AC|Parameter eliminieren|3x1 − x2 + 5x3 − 5 = 0 (Kontrolle vorgegeben)",
    voraussetzungen="Parameterform einer Ebene|Gleichungssystem lösen oder Vektorprodukt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SOL + "; D(−6; 2; 5); das Rechteck ABCD liegt in einer Ebene E; zur Kontrolle 3x1 − x2 + 5x3 − 5 = 0",
    gesucht="eine Gleichung von E in Koordinatenform",
    verfahren="Parameterform mit Stützvektor OA und Spannvektoren AB, AC aufstellen, die Parameter eliminieren (oder Normalenvektor über das Vektorprodukt) und die Konstante mit A bestimmen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="E: x = OA + λ · AB + μ · AC, λ, μ ∈ IR; das Gleichungssystem x1 = 2λ − 4μ, x2 = 6λ + 8μ, x3 = 1 + 4μ liefert 3x1 − x2 + 5x3 − 5 = 0 (amtlich)",
    zwischenergebnis="AB × AC = (24; −8; 40) = 8 · (3; −1; 5)", niveau_geschaetzt="II",
    fehlerquelle="die Konstante mit einem Punkt außerhalb der Ebene bestimmen oder beim Eliminieren ein Vorzeichen verlieren",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Probe mit B, C, D). Erste Schätzung I; bei der Prüfung gegen die enge Fassung auf II gesetzt – Parameterform aufstellen und in die Koordinatenform überführen ist eine Verkettung von Standardschritten (alle Zeilen des Typs im Bestand II). Typ wiederverwendet.")
row("2017MgrundlegendBAGLAA2WTR2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="Neigungswinkel der Modulfläche gegenüber der Horizontalen|Normalenvektoren (0; 0; 1) und (3; −1; 5)|φ ≈ 32,3°|Bedingung 30° bis 36° erfüllt",
    voraussetzungen="Neigungswinkel als Winkel der Normalenvektoren|Vergleich mit einem Intervall",
    format="Rechnung", operator="Prüfen Sie", antwort="Zahl|Text",
    material="Skizze", skizze=SOL_SK, kontext="Technik/Solarmodule", textumfang="mittel",
    gegeben=SOLK + "; für einen möglichst großen Energieertrag sollte der Neigungswinkel der Modulfläche gegenüber der Horizontalen zwischen 30° und 36° liegen",
    gesucht="Prüfung, ob diese Bedingung erfüllt ist",
    verfahren="Winkel zwischen m = (0; 0; 1) und n = (3; −1; 5) über den Kosinus berechnen und mit 30° und 36° vergleichen",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="2017MgrundlegendBAGLAA2WTR2-1d",
    ergebnis="Mit m = (0; 0; 1) und n = (3; −1; 5) ergibt sich cos φ = (m ∘ n)/(|m| · |n|), d. h. φ ≈ 32,3°; die Bedingung ist erfüllt (amtlich)",
    zwischenergebnis="cos φ = 5/√35", niveau_geschaetzt="II",
    fehlerquelle="den Winkel zwischen Normalenvektor und Horizontaler (etwa 57,7°) angeben",
    bemerkung="Standardbezug: K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (32,31°). Schätzung nicht blind: der amtliche Bereich der gleichartigen Teilaufgabe AG/LA (A2) WTR 1 e (II) war schon gelesen; die Schätzung folgt allen Zeilen des Typs im Bestand (II). Typ wiederverwendet.")
row("2017MgrundlegendBAGLAA2WTR2", "f", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Gleichung einer senkrechten Strecke mit Parameterbereich im Sachzusammenhang angeben", typ_neben="",
    stichwoerter="Rohr vom Befestigungspunkt M(−2; 4; 3) senkrecht zum Boden|Richtungsvektor (0; 0; 1)|Parameterbereich [−3; 0]",
    voraussetzungen="senkrecht heißt Richtung der x3-Achse|Boden als x3 = 0|Strecke als Gerade mit eingeschränktem Parameter",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="Skizze", skizze=SOL_SK, kontext="Technik/Solarmodule", textumfang="mittel",
    gegeben=SOLK + "; das Metallrohr lässt sich im Modell durch eine Strecke darstellen",
    gesucht="eine Gleichung dieser Strecke",
    verfahren="Die Strecke verläuft senkrecht von M(−2; 4; 3) bis zum Untergrund x3 = 0: Stützvektor OM, Richtung (0; 0; 1), Parameter von −3 bis 0",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="x = OM + σ · (0; 0; 1), σ ∈ [−3; 0] (amtlich)",
    zwischenergebnis="Fußpunkt des Rohrs (−2; 4; 0)", niveau_geschaetzt="II",
    fehlerquelle="den Parameterbereich weglassen (Gerade statt Strecke) oder σ ∈ [0; 3] mit falscher Richtung wählen",
    bemerkung="Standardbezug: K2 II, K3 II, K6 I. AB amtlich: II. Amtlich. Neuer Typ: die vorhandenen Streckentypen deuten eine gegebene Strecke; hier wird sie aus dem Sachzusammenhang aufgestellt.")
row("2017MgrundlegendBAGLAA2WTR2", "g", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Größeren Flächeninhalt des Schattens eines geneigten Rechtecks bei senkrechtem Lichteinfall begründen", typ_neben="",
    stichwoerter="Licht senkrecht auf die Modulfläche|AB parallel zur x1x2-Ebene, Schattenseite gleich lang|AD geneigt, Schattenseite länger|Skizze des Querschnitts mit Winkel φ",
    voraussetzungen="Flächeninhalt eines Rechtecks als Produkt der Seitenlängen|Hypotenuse länger als Kathete|Querschnitt senkrecht zu AB",
    format="Begründung|Zeichnen", operator="Begründen Sie", antwort="Text|Grafik",
    material="Skizze", skizze=SOL_SK, kontext="Technik/Solarmodule", textumfang="mittel",
    gegeben=SOLK + "; das Sonnenlicht fällt als parallele Geraden senkrecht auf die Modulfläche und erzeugt auf dem horizontalen Untergrund einen rechteckigen Schatten",
    gesucht="Begründung unter Verwendung einer geeignet beschrifteten Skizze, dass der Flächeninhalt des Schattenrechtecks größer ist als der des Rechtecks ABCD",
    verfahren="AB ist parallel zum Boden und wird in wahrer Länge abgebildet; im Querschnitt senkrecht zu AB trifft das senkrecht auf AD fallende Licht den Boden schräg, der Schatten von AD ist die Hypotenuse zu AD als Kathete; Flächeninhalt als Produkt der Seitenlängen",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2017MgrundlegendBAGLAA2WTR2-1a",
    ergebnis="Der Flächeninhalt eines Rechtecks ist das Produkt der Seitenlängen; die Gerade AB verläuft parallel zur x1x2-Ebene, die Gerade AD nicht; damit ist die eine Seite des Schattenrechtecks genauso lang wie AB, die andere länger als AD (amtlich); Skizze: Querschnitt durch A und D, Winkel φ bei A, Lichtstrahlen senkrecht zu AD, Boden waagerecht",
    zwischenergebnis="Schattenseite zu AD = Länge AD/cos φ ≈ 8,85 statt 7,48|Schatten 56 m^2 gegen ABCD ≈ 47,3 m^2", niveau_geschaetzt="III",
    fehlerquelle="beide Seiten als verlängert annehmen oder den Schatten als senkrechte Projektion (kürzer) deuten",
    bemerkung="Standardbezug: K1 III, K4 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung: Schatten 56 m^2, ABCD ≈ 47,3 m^2. Neuer Typ.")
# ---- Stochastik WTR 1: Smartphone (Aufgabe 1: Lieferung, 5 BE; Aufgabe 2: vier Werke, 15 BE) = 2017-be-gk 3.1
SMA = "Ein Hersteller bringt ein neues Smartphone auf den Markt; ein Händler erhält eine Lieferung dieser Smartphones"
WERK = ("Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer "
        "Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften "
        "Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %")
WERK_SK = ("Tabelle mit den Spalten Werk A, B, C, D und den Zeilen „Anteil an der Gesamtzahl“ (10 %, 30 %, 20 %, 40 %) "
           "und „Anteil der fehlerhaften Geräte“ (5 %, 3 %, 4 %, 2 %)")
row("2017MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl ungeordneter Auswahlen ohne Wiederholung über den Binomialkoeffizienten berechnen", typ_neben="",
    stichwoerter="vier aus sechs Farben|Reihenfolge ohne Bedeutung|(6 über 4) = 15",
    voraussetzungen="Binomialkoeffizient als Anzahl der Teilmengen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Handel/Smartphones", textumfang="kurz",
    gegeben=SMA + "; die gelieferten Geräte haben sechs verschiedene Farben; für die Auslage einiger Geräte im Schaufenster sollen vier Farben ausgewählt werden",
    gesucht="Anzahl der Möglichkeiten für diese Auswahl",
    verfahren="Ungeordnete Auswahl von 4 aus 6 ohne Wiederholung: Binomialkoeffizient",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="(6 über 4) = 15 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="geordnet zählen (6 · 5 · 4 · 3 = 360)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich im Landesheft 2017-be-gk 3.1 a (Heft noch nicht erfasst; der Typ ist für beide Fassungen gewählt). Neuer Typ: die Liste kennt nur geordnete Auswahlen ohne Wiederholung.")
row("2017MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit für ausschließlich eine Sorte beim mehrfachen Ziehen als Produkt berechnen", typ_neben="",
    stichwoerter="50 Geräte, 3 fehlerhaft, 10 ausgewählt|A: keines fehlerhaft, (47 über 10)/(50 über 10) ≈ 50,4 %|B über das Gegenereignis ≈ 49,6 %",
    voraussetzungen="Lotto-Modell mit Binomialkoeffizienten|Gegenereignis „mindestens eines“",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Handel/Smartphones", textumfang="mittel",
    gegeben=SMA + "; die Lieferung umfasst 50 Geräte, davon sind drei fehlerhaft; zehn Geräte werden zufällig ausgewählt; A: von den zehn ausgewählten Geräten ist keines fehlerhaft; B: von den zehn ausgewählten Geräten ist mindestens eines fehlerhaft",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="P(A) als Quotient (47 über 10)/(50 über 10) (alle zehn aus den 47 fehlerfreien, ohne Zurücklegen), P(B) = 1 − P(A)",
    schritte="2", zahlenraum="Bruch|Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(A) = (47 über 10)/(50 über 10) ≈ 50,4 %, P(B) = 1 − P(A) ≈ 49,6 % (amtlich)",
    zwischenergebnis="P(A) = 247/490", niveau_geschaetzt="I",
    fehlerquelle="mit Zurücklegen rechnen (0,94^10 ≈ 53,9 %)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (247/490). Erste Schätzung II; bei der Prüfung gegen die enge Fassung auf I gesetzt – eine einzelne Laplace-Rechnung mit Binomialkoeffizienten, B ist nur ihr Gegenereignis (wie Analysis 1 f dieses Stapels). Wortgleich im Landesheft 2017-be-gk 3.1 b; Typ für beide Fassungen gewählt (Lotto-Modell: in Berlin Prüfungsgegenstand, die hypergeometrische Verteilung als Begriff nicht).")
row("2017MgrundlegendBStochastikWTR1", "a", innen="2", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Totale Wahrscheinlichkeit über die Pfadregeln nachweisen", typ_neben="",
    stichwoerter="Werksanteil mal Fehleranteil je Werk|Summe über vier Werke|3 %",
    voraussetzungen="Tabelle als zweistufiges Experiment lesen|Pfadmultiplikation und -addition",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="Tabelle", skizze=WERK_SK, kontext="Produktion/Smartphones", textumfang="mittel",
    gegeben=WERK,
    gesucht="Nachweis, dass der Anteil der fehlerhaften Geräte unter allen hergestellten Geräten 3 % beträgt",
    verfahren="Summe der Produkte aus Werksanteil und Fehleranteil (totale Wahrscheinlichkeit)",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,1 · 0,05 + 0,3 · 0,03 + 0,2 · 0,04 + 0,4 · 0,02 = 3 % (amtlich)",
    zwischenergebnis="0,005 + 0,009 + 0,008 + 0,008 = 0,03", niveau_geschaetzt="I",
    fehlerquelle="die vier Fehleranteile ungewichtet mitteln (3,5 %)",
    bemerkung="Standardbezug: K4 II, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung I (eine Summe von vier Pfadprodukten, wie die Poolzeilen des Typs, alle I); der amtliche Bereich ist II (K4 II, K5 II – die Daten stehen in einer Tabelle statt in einem Baum). Wortgleich im Landesheft 2017-be-gk 3.1 c; Typ für beide Fassungen gewählt.")
row("2017MgrundlegendBStochastikWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="fehlerhaftes Gerät, Werk A gesucht|Schnittanteil 0,1 · 0,05|durch Gesamtanteil 0,03|1/6",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient|Bedingung „fehlerhaft“ im Nenner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze=WERK_SK, kontext="Produktion/Smartphones", textumfang="kurz",
    gegeben=WERK + "; Anteil fehlerhafter Geräte insgesamt 3 %; ein unter allen hergestellten Geräten zufällig ausgewähltes Gerät ist fehlerhaft",
    gesucht="Wahrscheinlichkeit dafür, dass es im Werk A hergestellt wurde",
    verfahren="Schnittanteil 0,1 · 0,05 durch den Gesamtanteil 0,03 teilen (Satz von Bayes)",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="2017MgrundlegendBStochastikWTR1-2a",
    ergebnis="(0,1 · 0,05)/0,03 = 1/6 (amtlich)",
    zwischenergebnis="≈ 16,7 %", niveau_geschaetzt="II",
    fehlerquelle="den Fehleranteil 5 % im Werk A angeben (Bedingung vertauscht)",
    bemerkung="Standardbezug: K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet. Wortgleich im Landesheft 2017-be-gk 3.1 d; Typ für beide Fassungen gewählt.")
row("2017MgrundlegendBStochastikWTR1", "c", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Modalwert einer Binomialverteilung bestimmen", typ_neben="",
    stichwoerter="n = 250, p = 0,05|Erwartungswert 12,5 nicht ganzzahlig|P(X = 12) ≈ 11,6 % > P(X = 13) ≈ 11,2 %|wahrscheinlichste Anzahl 12",
    voraussetzungen="Erwartungswert n · p|Einzelwahrscheinlichkeiten am Rechner|Nachbarwerte vergleichen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Smartphones", textumfang="kurz",
    gegeben=WERK + "; von im Werk A hergestellten Geräten werden 250 zufällig ausgewählt; X: Anzahl der fehlerhaften, binomialverteilt mit n = 250 und p = 0,05",
    gesucht="die Anzahl fehlerhafter Geräte, die darunter mit der größten Wahrscheinlichkeit auftritt",
    verfahren="Erwartungswert 250 · 0,05 = 12,5 ist nicht ganzzahlig; P(X = 12) und P(X = 13) berechnen und vergleichen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Der Erwartungswert von X ist 250 · 0,05 = 12,5; P(X = 12) ≈ 11,6 %, P(X = 13) ≈ 11,2 %; damit ist die gesuchte Anzahl 12 (amtlich)",
    zwischenergebnis="P(X = 12) ≈ 0,1160|P(X = 13) ≈ 0,1117", niveau_geschaetzt="I",
    fehlerquelle="12,5 oder aufgerundet 13 als Anzahl angeben",
    bemerkung="Standardbezug: K1 I, K2 I, K3 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erste Schätzung II; bei der Prüfung gegen die enge Fassung auf I gesetzt – der Vergleich der beiden Nachbarwerte ist das Standardverfahren des Typs, keine Verkettung (die Poolzeile des Typs I). Im Landesheft 2017-be-gk 3.1 e abgewandelt: dort 20 Geräte aus Werk A und die Wahrscheinlichkeit, dass keines fehlerhaft ist (0,95^20 ≈ 35,8 %), anderer Typ.")
row("2017MgrundlegendBStochastikWTR1", "d", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Term 200 · 0,98^s · 0,02 + 0,98^200|0,02 Fehleranteil in Werk D|s = 199|P(X ≤ 1) für n = 200, höchstens eines fehlerhaft",
    voraussetzungen="Bernoulli-Formel für k = 0 und k = 1 erkennen|Summe als kumulierte Wahrscheinlichkeit",
    format="Kurzantwort", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl|Text",
    material="Tabelle", skizze=WERK_SK, kontext="Produktion/Smartphones", textumfang="kurz",
    gegeben=WERK + "; Term 200 · 0,98^s · 0,02 + 0,98^200",
    gesucht="ein Wert von s, für den mit dem Term im Sachzusammenhang die Wahrscheinlichkeit eines Ereignisses berechnet werden kann, und Beschreibung des zugehörigen Ereignisses",
    verfahren="0,02 ist der Fehleranteil in Werk D; 0,98^200 = P(X = 0) und 200 · 0,02 · 0,98^199 = P(X = 1) für n = 200, also s = 199 und die Summe P(X ≤ 1)",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="s = 199; unter 200 im Werk D hergestellten, zufällig ausgewählten Geräten ist höchstens eines fehlerhaft (amtlich)",
    zwischenergebnis="Wert des Terms ≈ 0,0894", niveau_geschaetzt="II",
    fehlerquelle="s = 200 wählen oder das Ereignis als „genau eines fehlerhaft“ beschreiben",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Schätzung III; bei der Prüfung gegen die enge Fassung auf II gesetzt – die einfache Deutung einer Binomialsumme als kumulierte Wahrscheinlichkeit ist nach der Ausnahme zu (d) kein III (die Zeilen des Typs im Bestand überwiegend II). Typ wiederverwendet. Wortgleich im Landesheft 2017-be-gk 3.1 f; Typ für beide Fassungen gewählt.")
row("2017MgrundlegendBStochastikWTR1", "e", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen", typ_neben="",
    stichwoerter="Werk C, Fehleranteil 4 %|mindestens ein fehlerhaftes mit mindestens 95 %|1 − 0,96^n ≥ 0,95|n ≥ 74",
    voraussetzungen="Gegenereignis „kein fehlerhaftes“|Exponentialungleichung durch Logarithmieren oder Probieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze=WERK_SK, kontext="Produktion/Smartphones", textumfang="kurz",
    gegeben=WERK + "; es werden im Werk C hergestellte Geräte zufällig ausgewählt",
    gesucht="Mindestanzahl der auszuwählenden Geräte, damit sich darunter mit einer Wahrscheinlichkeit von mindestens 95 % mindestens ein fehlerhaftes Gerät befindet",
    verfahren="Über das Gegenereignis 1 − 0,96^n ≥ 0,95 ansetzen und durch Logarithmieren oder Probieren nach n auflösen",
    schritte="3", zahlenraum="dezimal|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Ist n die Anzahl auszuwählender Geräte, so gilt 1 − 0,96^n ≥ 0,95 ⇔ n ≥ 74 (amtlich)",
    zwischenergebnis="1 − 0,96^73 ≈ 0,9492|1 − 0,96^74 ≈ 0,9512", niveau_geschaetzt="II",
    fehlerquelle="n ≈ 73,4 abrunden oder mit 0,04^n statt 0,96^n ansetzen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Schätzung II (Gegenereignis, Ungleichung und Logarithmus als Verkettung von Standardschritten, kein Eintrag der Deutungsliste; die Zeilen des Typs im abi-Bestand alle II); der amtliche Bereich ist III (K2 III) – erster amtlicher Bereich für den Typ, Stochastik WTR 2 1 c dieses Stapels ebenso III. Typ wiederverwendet. Wortgleich im Landesheft 2017-be-gk 3.1 g; Typ für beide Fassungen gewählt.")
# ---- Stochastik WTR 2: Pkw (Aufgabe 1: Dieselfahrzeuge und Leistung, 14 BE; Aufgabe 2: Standardabweichung 3, 6 BE)
PKW = ("20 % aller Pkw eines bestimmten Herstellers sind Dieselfahrzeuge; die Anzahl der Dieselfahrzeuge in einer "
       "Stichprobe gilt modellhaft als binomialverteilt; 25 Pkw des Herstellers werden zufällig ausgewählt, davon sind drei rot")
LEI = ("20 % aller Pkw eines Herstellers sind Dieselfahrzeuge; 80 % der Dieselfahrzeuge und 90 % der übrigen Pkw des "
       "Herstellers haben eine Leistung von mehr als 60 kW")
SIG = ("binomialverteilte Zufallsgrößen, die für eine Trefferwahrscheinlichkeit p mit 0 <= p <= 1 die Anzahl der "
       "Treffer bei n Versuchen angeben; die Standardabweichung der Zufallsgrößen ist 3")
row("2017MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="X ~ B(25; 0,2)|A: genau acht, P(X = 8) ≈ 6,2 %|B: mindestens fünf, 1 − P(X ≤ 4) ≈ 57,9 %",
    voraussetzungen="Binomialverteilung am Rechner|„mindestens fünf“ über das Gegenereignis „höchstens vier“",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Fahrzeuge/Statistik", textumfang="mittel",
    gegeben=PKW + "; A: unter den ausgewählten Pkw sind genau acht Dieselfahrzeuge; B: unter den ausgewählten Pkw sind mindestens fünf Dieselfahrzeuge",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="X: Anzahl der Dieselfahrzeuge, B(25; 0,2); P(X = 8) und P(X ≥ 5) = 1 − P(X ≤ 4) mit dem Rechner",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(A) ≈ 6,2 %, P(B) ≈ 1 − 0,421 = 57,9 % (amtlich)",
    zwischenergebnis="P(X ≤ 4) ≈ 0,4207", niveau_geschaetzt="I",
    fehlerquelle="P(X ≥ 5) als 1 − P(X ≤ 5) rechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,0623; 0,5793). Typ und Nebentyp wiederverwendet.")
row("2017MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit für ausschließlich eine Sorte beim mehrfachen Ziehen als Produkt berechnen", typ_neben="",
    stichwoerter="25 Pkw, genau fünf Diesel|die drei roten alle Diesel|5/25 · 4/24 · 3/23 ≈ 0,43 %",
    voraussetzungen="Diesel als zufällig auf die 25 Pkw verteilt|Pfadprodukt ohne Zurücklegen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Fahrzeuge/Statistik", textumfang="kurz",
    gegeben=PKW + "; von den ausgewählten Pkw sind genau fünf Dieselfahrzeuge",
    gesucht="Wahrscheinlichkeit dafür, dass die drei roten Pkw Dieselfahrzeuge sind",
    verfahren="Die fünf Diesel sind zufällig auf die 25 Pkw verteilt; für die drei roten nacheinander ohne Zurücklegen 5/25 · 4/24 · 3/23",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="5/25 · 4/24 · 3/23 ≈ 0,43 % (amtlich)",
    zwischenergebnis="= 1/230", niveau_geschaetzt="II",
    fehlerquelle="mit der Binomialverteilung 0,2^3 = 0,8 % rechnen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (1/230, auch als (22 über 2)/(25 über 5)). Erste Schätzung III; bei der Prüfung gegen die enge Fassung auf II gesetzt – kein Eintrag der Deutungsliste greift, Urnenmodell ohne Zurücklegen mit Pfadprodukt ist eine Verkettung von Standardschritten. Typ wiederverwendet (2023-bebb-gk).")
row("2017MgrundlegendBStochastikWTR2", "c", innen="1", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen", typ_neben="",
    stichwoerter="mindestens ein Diesel mit mindestens 95 %|1 − 0,8^n ≥ 0,95|n = 14",
    voraussetzungen="Gegenereignis „kein Diesel“|Exponentialungleichung durch Logarithmieren oder Probieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Fahrzeuge/Statistik", textumfang="kurz",
    gegeben="20 % aller Pkw eines bestimmten Herstellers sind Dieselfahrzeuge; die Anzahl der Dieselfahrzeuge in einer Stichprobe gilt als binomialverteilt",
    gesucht="Mindestanzahl zufällig ausgewählter Pkw des Herstellers, damit die Wahrscheinlichkeit, dass darunter mindestens ein Dieselfahrzeug ist, mindestens 95 % beträgt",
    verfahren="Über das Gegenereignis 1 − 0,8^n ≥ 0,95 ansetzen und nach n auflösen",
    schritte="3", zahlenraum="dezimal|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="1 − 0,8^13 < 0,95, 1 − 0,8^14 > 0,95; es müssen mindestens 14 Pkw ausgewählt werden (amtlich)",
    zwischenergebnis="1 − 0,8^13 ≈ 0,9450|1 − 0,8^14 ≈ 0,9560", niveau_geschaetzt="II",
    fehlerquelle="n ≈ 13,4 abrunden",
    bemerkung="Standardbezug: K2 III, K3 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Schätzung II (Verkettung von Standardschritten, kein Eintrag der Deutungsliste); der amtliche Bereich ist III (K2 III), wie bei Stochastik WTR 1 2 e dieses Stapels. Typ wiederverwendet.")
row("2017MgrundlegendBStochastikWTR2", "d", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen", typ_neben="",
    stichwoerter="erste Stufe Diesel 20 %, kein Diesel 80 %|zweite Stufe Leistung über 60 kW: 80 % bzw. 90 %",
    voraussetzungen="Anteile als Astwahrscheinlichkeiten|Ereignisse benennen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Fahrzeuge/Statistik", textumfang="kurz",
    gegeben=LEI,
    gesucht="beschriftetes Baumdiagramm zum Sachverhalt",
    verfahren="Erste Stufe D/nicht D, zweite Stufe L/nicht L mit den bedingten Anteilen",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="D 20 % mit L 80 % und nicht L 20 %; nicht D 80 % mit L 90 % und nicht L 10 %; D: ein zufällig ausgewählter Pkw ist Dieselfahrzeug, L: seine Leistung ist größer als 60 kW (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="80 % und 90 % als Anteile an allen Pkw in die erste Stufe schreiben",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet.")
row("2017MgrundlegendBStochastikWTR2", "e", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil über die totale Wahrscheinlichkeit aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(L) = 0,2 · 0,8 + 0,8 · 0,9|88 %",
    voraussetzungen="Pfadmultiplikation und -addition",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Fahrzeuge/Statistik", textumfang="kurz",
    gegeben=LEI,
    gesucht="Wahrscheinlichkeit dafür, dass die Leistung eines zufällig ausgewählten Pkw des Herstellers größer als 60 kW ist",
    verfahren="Beide Pfade zu L addieren",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="2017MgrundlegendBStochastikWTR2-1d",
    ergebnis="0,2 · 0,8 + 0,8 · 0,9 = 88 % (amtlich)",
    zwischenergebnis="0,16 + 0,72", niveau_geschaetzt="I",
    fehlerquelle="die Anteile 80 % und 90 % ungewichtet mitteln",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")
row("2017MgrundlegendBStochastikWTR2", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Versuchszahl aus Standardabweichung und Trefferwahrscheinlichkeit berechnen", typ_neben="",
    stichwoerter="σ = √(n · p · (1 − p)) = 3|p = 0,25|n = 48",
    voraussetzungen="Formel der Standardabweichung der Binomialverteilung|Wurzelgleichung durch Quadrieren lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SIG + "; Trefferwahrscheinlichkeit 25 %",
    gesucht="die zugehörige Anzahl der Versuche",
    verfahren="√(n · 0,25 · 0,75) = 3 quadrieren und nach n auflösen",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="√(n · 0,25 · 0,75) = 3 ⇔ n = 48 (amtlich)",
    zwischenergebnis="n · 0,1875 = 9", niveau_geschaetzt="I",
    fehlerquelle="Standardabweichung und Varianz verwechseln (n = 16)",
    bemerkung="Standardbezug: K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung I (eine Gleichung aus der Formel für σ nach n auflösen); der amtliche Bereich ist II (K2, K5, K6 je II). Neuer Typ; Kandidat für eine Zusammenziehung mit „Stichprobenumfang für eine verdoppelte Standardabweichung der Binomialverteilung ermitteln“.")
row("2017MgrundlegendBStochastikWTR2", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unmöglichkeit einer Standardabweichung bei gegebener Versuchszahl über das Maximum von p · (1 − p) begründen", typ_neben="",
    stichwoerter="n = 9, σ = 3|p · (1 − p) = 1|p · (1 − p) höchstens 1/4|keine Lösung",
    voraussetzungen="Formel der Standardabweichung|Maximum von p · (1 − p) bei p = 1/2",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=SIG + "; Anzahl der Versuche 9",
    gesucht="Begründung, dass es keinen Wert von p geben kann, für den die Anzahl der Versuche 9 ist",
    verfahren="√(9 · p · (1 − p)) = 3 ⇔ p · (1 − p) = 1; p · (1 − p) ist für 0 <= p <= 1 höchstens 1/4, also gibt es keine Lösung",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="√(9 · p · (1 − p)) = 3 ⇔ p · (1 − p) = 1; die Gleichung hat für 0 <= p <= 1 keine Lösung (amtlich)",
    zwischenergebnis="max p · (1 − p) = 1/4", niveau_geschaetzt="II",
    fehlerquelle="die quadratische Gleichung p^2 − p + 1 = 0 lösen wollen, ohne die fehlende reelle Lösung zu deuten",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Neuer Typ.")

NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Horizontalabstand aus vorgegebener Neigung in Prozent und Höhendifferenz berechnen", "Analytische Geometrie", "Geraden",
     "Aus einer vorgegebenen Steigung in Prozent und dem Höhenunterschied zweier Endpunkte den waagerechten Abstand berechnen (Quotient nach dem Nenner auflösen) und auf einen Bezugspunkt im Sachzusammenhang umrechnen.", "2017MgrundlegendBAnalysisWTR-1g"),
    ("Extrempunkte: Fehlen weiterer Extrempunkte über die Höchstzahl nach dem Grad begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Begründen, dass eine ganzrationale Funktion vom Grad n höchstens n − 1 Extrempunkte hat und deshalb außerhalb eines Bildausschnitts, der bereits so viele zeigt, keine weiteren besitzt.", "2017MgrundlegendBAnalysisWTR-2a"),
    ("Nullstellen und Werte: Werte a mit vorgegebener Lösungsanzahl von f(x) = a über die lokalen Extremwerte am Graphen angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Lösungen von f(x) = a als Schnittstellen des Graphen mit der Parallelen y = a deuten und die Werte a angeben, für die es eine vorgegebene Anzahl gibt, meist Berührung in einem lokalen Hoch- oder Tiefpunkt.", "2017MgrundlegendBAnalysisWTR-2b"),
    ("Vorzeichen von erster und zweiter Ableitung an einer Stelle aus Monotonie und Krümmung am Graphen bestimmen", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Am abgebildeten Funktionsgraphen an einer Stelle das Vorzeichen von f' aus dem Steigen oder Fallen und das Vorzeichen von f'' aus der Krümmung (Lage zur Wendestelle) bestimmen und daraus das Vorzeichen eines Terms wie f'(a) · f''(a) folgern.", "2017MgrundlegendBAnalysisWTR-2c"),
    ("Parallele Ebenen über die Normalenvektoren auswählen und über die Konstante der Koordinatengleichung der Höhe nach zuordnen", "Analytische Geometrie", "Ebenen",
     "Aus mehreren Koordinatengleichungen die zu einer gegebenen Ebene parallelen über kollineare Normalenvektoren auswählen und sie über die Konstante (bei festen übrigen Koordinaten wächst sie mit der Höhe) übereinanderliegenden Flächen zuordnen.", "2017MgrundlegendBAGLAA2WTR1-1f"),
    ("Gleichung einer senkrechten Strecke mit Parameterbereich im Sachzusammenhang angeben", "Analytische Geometrie", "Geraden",
     "Eine senkrechte Strecke (etwa ein Rohr oder Mast) von einem gegebenen Punkt bis zur Grundebene als Gerade mit Richtung (0; 0; 1) und passend eingeschränktem Parameterbereich angeben.", "2017MgrundlegendBAGLAA2WTR2-1f"),
    ("Ebene Figur: Größeren Flächeninhalt des Schattens eines geneigten Rechtecks bei senkrechtem Lichteinfall begründen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Mit einer beschrifteten Querschnittsskizze begründen, dass der Schatten eines Rechtecks mit einer waagerechten Seite bei senkrecht auffallendem Parallellicht auf der Grundebene größer ist: die waagerechte Seite bleibt gleich lang, die geneigte wird zur Hypotenuse verlängert.", "2017MgrundlegendBAGLAA2WTR2-1g"),
    ("Anzahl ungeordneter Auswahlen ohne Wiederholung über den Binomialkoeffizienten berechnen", "Stochastik", "Kombinatorik",
     "Die Anzahl der Möglichkeiten, k aus n verschiedenen Objekten ohne Beachtung der Reihenfolge und ohne Wiederholung auszuwählen, als Binomialkoeffizient (n über k) berechnen.", "2017MgrundlegendBStochastikWTR1-1a"),
    ("Versuchszahl aus Standardabweichung und Trefferwahrscheinlichkeit berechnen", "Stochastik", "Kenngrößen von Verteilungen",
     "Aus einer vorgegebenen Standardabweichung und der Trefferwahrscheinlichkeit einer Binomialverteilung die Anzahl der Versuche über σ = √(n · p · (1 − p)) berechnen.", "2017MgrundlegendBStochastikWTR2-2a"),
    ("Unmöglichkeit einer Standardabweichung bei gegebener Versuchszahl über das Maximum von p · (1 − p) begründen", "Stochastik", "Kenngrößen von Verteilungen",
     "Für eine vorgegebene Standardabweichung und Versuchszahl die Gleichung für p · (1 − p) aufstellen und begründen, dass sie keine Lösung hat, weil p · (1 − p) höchstens 1/4 ist.", "2017MgrundlegendBStochastikWTR2-2b"),
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
