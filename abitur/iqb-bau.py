# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 1.10 · 29.09.2026 · gilt mit katalog-prompt.md v0.9, abitur-vokabular.md v1.6, iqb.md v1.18, abitur-abgleich.py v0.28, iqb-quellen.csv mit Spalte dateidublette_von und den Geltungsdateien abi-<zielprüfung>-geltung.md v1.0

Änderungen gegenüber 1.9 (Auftrag Nacht 2026-09-29, Teil 3; Beschluss vom 26.09.2026, beschluss-2026-09-26.md
Punkt 2): Liste EICHUNG_UNTERSCHRITTEN (neben SCHWELLEN) für Stapel, die mit dokumentierter Unterschreitung der
Eichschwelle erfasst sind – darin nur 2018-ea-B-cas mit seinem gemessenen Wert (Treffer der engen Fassung von
gewerteten Zeilen) und dem Verweis auf den Beschluss. Die Schwelle bleibt 85 % für alle Stapel; das ist keine
Wiedereinführung der Überschreibung je Stapel aus v1.4 (kein anderer Grenzwert, kein KONFIG-Feld): Im Stapellauf
wird die gerissene Schwelle nur dann zur Warnung, wenn der Stapel in der Liste steht und die Messung genau den
Listenwert ergibt, sonst bleibt sie ein Fehler; die Selbstprüfung rechnet für jeden Eintrag die Eichung aus dem
Bestand und meldet sie als Zeile „Warnung: …“ (auch eine Abweichung vom Listenwert nur als Meldung). Stapel
2018-ea-B-cas erfasst (KONFIG, ZEILEN, NEUE_TYPEN); die übrigen Prüfungen unverändert.

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
    "stapel": "2018-ea-B-cas",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dateidublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll. Delta-Stapel: keine Dateidublette, keine Aufgabendublette, kein Abzug.
    "soll": {
        "2018MerhoehtBAnalysisCAS1": 50, "2018MerhoehtBAnalysisCAS2": 50, "2018MerhoehtBAnalysisCAS3": 50,
        "2018MerhoehtBAGLAA1CAS1": 25, "2018MerhoehtBAGLAA1CAS2": 25,
        "2018MerhoehtBAGLAA2CAS1": 25, "2018MerhoehtBAGLAA2CAS2": 25,
        "2018MerhoehtBStochastikCAS1": 25, "2018MerhoehtBStochastikCAS2": 25,
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
# Dokumentierte Unterschreitung der Eichschwelle (v1.10; Beschluss vom 26.09.2026, beschluss-2026-09-26.md
# Punkt 2; iqb.md § 7). Die Schwelle in SCHWELLEN bleibt für alle Stapel 85 %; dies ist keine Überschreibung je
# Stapel wie in v1.4 (zurückgebaut in v1.5). Ein Stapel steht hier nur mit seinem gemessenen Wert (Treffer der
# engen Fassung, gewertete Zeilen) und dem Verweis auf den Beschluss: der Stapellauf macht aus dem Fehler eine
# Warnung, wenn die Messung genau diesen Wert ergibt, sonst bleibt es ein Fehler; die Selbstprüfung meldet jeden
# Eintrag als Warnung mit dem Wert aus dem Bestand.
EICHUNG_UNTERSCHRITTEN = {
    "2018-ea-B-cas": (69, 85, "beschluss-2026-09-26.md Punkt 2"),
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
# Stapel 2018-ea-B, CAS-Zweig – Delta-Stapel zum WTR-Zweig (Auftrag Nacht 2026-09-29, Teil 3; Beschluss vom 26.09.2026,
# beschluss-2026-09-26.md Punkt 2; iqb.md § 7 „MMS/CAS als Delta“). iqb-quellen.csv führt für keine der neun CAS-Dateien
# eine dateidublette_von (am 28.09.2026 nachgemessen; Stochastik CAS 1 ~ WTR 1 Ähnlichkeit 0,988, aber andere Zahlen);
# alle neun bilden den Stapel: 3 · 50 + 6 · 25 = 300 BE, 85 Zeilen. Keine Aufgabendublette. Geteilte Teilaufgaben:
# Stochastik CAS 1 1 d, 2 a, 2 b = Stochastik WTR 1 1 d, 2 a, 2 b (Typ geteilt, Felder aus der WTR-Zeile übernommen;
# 2 c abgewandelt). Landeshefte: AG/LA (A2) CAS 1 (Museum) ist 2018-bb-ea-cas B3.1 und – mit vorgegebener
# Ebenengleichung in f – 2018-bb-ea B3.1 (WTR-Fassung des Landes); Verweise per abitur-abgleich.py Lauf 27.
# Schätzungen: geprüfter Stand des ersten Versuchs vom 28.09.2026 (abitur/arbeitsstand/2018-ea-B-cas/, 67 von 85),
# dazu Deutungsliste (f) an Stochastik CAS 1 1 b und CAS 2 1 b (69 von 85, dokumentierte Unterschreitung,
# EICHUNG_UNTERSCHRITTEN). Zeilen von drei Zeilen-Agenten je Dateigruppe geschrieben, im Stapellauf gemeinsam geprüft.
# ---- Analysis CAS 1 (Aufgabe 1: Schar f_r mit Dreieck A_rB_rC, 27 BE; Aufgabe 2: Papierflieger Typ P, 7 BE;
# Aufgabe 3: Flugkurve Typ S, 11 BE; Aufgabe 4: Flugkurve Typ G ohne Teilaufgabenbuchstaben, 5 BE)
FR = "Für r ∈ IR, r ≠ 0, ist die Schar der in IR definierten Funktionen f_r mit f_r(x) = −1/r · x^2 + 4/r · x + 2 gegeben"
DREI = ("; für r > −2 und r ≠ 0 sind A_r(2 − √(4 + 2r); 0), B_r(2 + √(4 + 2r); 0) und C(4; 2) Punkte des Graphen von f_r; "
        "untersucht wird, für welche Werte von r das Dreieck A_rB_rC rechtwinklig ist")
F6_SK = ("zu erstellende Skizze (Erwartungshorizont): Koordinatensystem auf Kästchengitter, x von −4 bis 8 (Beschriftung −4, −2, 0, "
         "2, 4, 6, 8), y von etwa −1 bis 3 (Beschriftung 2); nach unten geöffnete Parabel f_6 mit Scheitel (2; 8/3), Nullstellen "
         "−2 und 6, durch (0; 2) und (4; 2)")
F6B_SK = (F6_SK + "; darin schraffiert das Flächenstück über der x-Achse: unter dem Graphen von −2 bis 0 (1. Summand), das "
          "Rechteck 0 <= x <= 4, 0 <= y <= 2 (2. Summand) und unter dem Graphen von 4 bis 6 (3. Summand); das Stück zwischen "
          "y = 2 und dem Scheitelbogen über 0 <= x <= 4 gehört nicht dazu")
PAPIER = ("Papierflieger: Koordinatensystem mit der x-Achse entlang des horizontalen Bodens und der y-Achse durch den "
          "Abwurfpunkt; x ist die horizontale Entfernung vom Abwurfpunkt, der Funktionswert die Flughöhe, jeweils in Metern; "
          "die Größe der Papierflieger wird vernachlässigt; f_4(x) = −1/4 · x^2 + x + 2 (Funktion der Schar "
          "f_r(x) = −1/r · x^2 + 4/r · x + 2 für r = 4)")
PAPIER_SK = ("schematische Abbildung ohne Achsen und Maße: links ein Werfer (Strichmännchen) auf dem waagerechten Boden, an "
             "seiner erhobenen Hand der Papierflieger; von dort drei Flugkurven: Parabelflug (P) als nach unten geöffneter "
             "Bogen, der rechts auf dem Boden endet; Gleitflug (G) folgt dem Bogen bis kurz hinter den höchsten Punkt und "
             "geht dann ohne Knick in eine flach fallende Gerade über, die rechts aus dem Bild läuft; Sturzflug (S) steigt "
             "früh immer steiler an, bis er fast senkrecht ist, und fällt dann als senkrechte Linie bis zum Boden")
FLUG_T = ("; bei einer Anfangsgeschwindigkeit von 6,3 m/s beschreibt y(t) = −5t^2 + 4,45t + 2 modellhaft die momentane Höhe "
          "des Papierfliegers und v(t) = √(100t^2 − 89t + 40) näherungsweise seine momentane Geschwindigkeit; t ist die Zeit "
          "seit dem Abwurf in s, y(t) in m, v(t) in m/s")
S_TYP = ("; Flugkurve vom Typ S: im ersten Teil durch f_4 beschrieben, ab einer horizontalen Entfernung von 0,5 m vom "
         "Abwurfpunkt durch s(x) = a/(x − 1,5) + b mit a, b ∈ IR; die Flugkurve hat keinen Knick; der Papierflieger steigt, "
         "bis er einen Steigungswinkel von 85° erreicht, und stürzt dann vertikal ab")
row("2018MerhoehtBAnalysisCAS1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen einer Funktion in ein Koordinatensystem einzeichnen", typ_neben="",
    stichwoerter="f_6(x) = −1/6 · x^2 + 2/3 · x + 2|Scheitel (2; 8/3)|Nullstellen −2 und 6|y-Achsenabschnitt 2",
    voraussetzungen="Scheitel einer Parabel|Nullstellen einer quadratischen Funktion|Wertetabelle",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=F6_SK, kontext="ohne", textumfang="kurz",
    gegeben=FR + "; r = 6", gesucht="Skizze des Graphen von f_6 in einem Koordinatensystem",
    verfahren="f_6(x) = −1/6 · x^2 + 2/3 · x + 2 aufstellen; Scheitel, Nullstellen und y-Achsenabschnitt berechnen oder eine Wertetabelle mit dem Rechner anlegen und die Parabel skizzieren",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="Nach unten geöffnete Parabel mit Scheitel (2; 8/3), Nullstellen −2 und 6 und y-Achsenabschnitt 2; Skizze im Erwartungshorizont (amtlich)",
    zwischenergebnis="f_6(0) = f_6(4) = 2",
    niveau_geschaetzt="I", fehlerquelle="die Parabel nach oben geöffnet zeichnen, weil der Faktor −1/r übersehen wird",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich (Skizze im Erwartungshorizont, kennzeichnende Punkte eigene Rechnung bestätigt). Die Teilaufgabe verlangt selbst eine Skizze; skizze beschreibt die zu erstellende Darstellung nach dem Erwartungshorizont. Der Erwartungshorizont von 1 a steht unten auf Seite 3 und war beim Schätzen in Sicht. Typ wiederverwendet. CAS-Anteil: Graph mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS1", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Flächenstück zu einer Summe aus Integralen und Rechteck am Graphen markieren und Summanden zuordnen", typ_neben="",
    stichwoerter="Term ∫ von −2 bis 0 f_6(x) dx + 4 · 2 + ∫ von 4 bis 6 f_6(x) dx|Rechteck 4 · 2 unter der Geraden y = 2|zwei Randstücke unter dem Graphen|Inhalt 112/9 = 12 4/9",
    voraussetzungen="Integral als Flächeninhalt bei f >= 0|Rechteckfläche|Nullstellen und die Punkte (0; 2), (4; 2) des Graphen",
    format="Eintragen|Kurzantwort", operator="Markieren Sie|ordnen Sie zu|Geben Sie an", antwort="Grafik|Zahl",
    material="Koordinatensystem", skizze=F6B_SK, kontext="ohne", textumfang="mittel",
    gegeben=FR + "; f_6(x) = −1/6 · x^2 + 2/3 · x + 2 mit den Nullstellen −2 und 6 und f_6(0) = f_6(4) = 2; Term ∫ von −2 bis 0 f_6(x) dx + 4 · 2 + ∫ von 4 bis 6 f_6(x) dx",
    gesucht="in der Skizze aus Teilaufgabe 1 a ein Flächenstück, dessen Inhalt mit dem Term berechnet werden kann, mit Zuordnung jedes Summanden zu einem Teil des Flächenstücks; Inhalt des Flächenstücks",
    verfahren="Die Integrale sind die Flächen zwischen Graph und x-Achse über [−2; 0] und [4; 6], 4 · 2 das Rechteck über [0; 4] bis zur Höhe 2 = f_6(0) = f_6(4); Integrale mit dem Rechner berechnen und addieren",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2018MerhoehtBAnalysisCAS1-1a",
    ergebnis="Flächenstück zwischen der x-Achse und der Linie aus dem Graphen von f_6 über [−2; 0], der Strecke y = 2 über [0; 4] und dem Graphen über [4; 6]; 1. Summand linkes Randstück, 2. Summand Rechteck, 3. Summand rechtes Randstück; der Inhalt ist 12 4/9 (amtlich)",
    zwischenergebnis="beide Integrale je 20/9",
    niveau_geschaetzt="II", fehlerquelle="die ganze Fläche unter der Parabel von −2 bis 6 markieren und die Kappe über y = 2 mitzählen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (112/9 ≈ 12,44). Schätzung II (Flächenstück zum Term finden, Summanden am Graphen zuordnen, Inhalt angeben – Verkettung); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: vorhandene Typen begründen oder schätzen Integralwerte über Rechteck und Integral ab oder berechnen Flächen daraus, keiner markiert zu einem vorgegebenen Summenterm das Flächenstück und ordnet die Summanden zu. CAS-Anteil: Integrale mit dem Rechner, Zuordnung eigen.")
row("2018MerhoehtBAnalysisCAS1", "c", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Extrempunkt einer Schar mit Art nach dem Parametervorzeichen bestimmen", typ_neben="",
    stichwoerter="f_r'(x) = 2/r · (2 − x) = 0 ⇔ x = 2|f_r(2) = 4/r + 2|Leitkoeffizient −1/r|r < 0 Minimum, r > 0 Maximum",
    voraussetzungen="Ableitung mit Parameter|Öffnung einer Parabel am Vorzeichen des Leitkoeffizienten|Funktionswert mit Parameter",
    format="Begründung|Kurzantwort", operator="Zeigen Sie|Geben Sie an|nennen Sie", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FR,
    gesucht="Nachweis, dass jede Funktion der Schar bei x = 2 ein Extremum hat; Art des Extremums in Abhängigkeit von r; zugehöriger Funktionswert",
    verfahren="f_r'(x) = 0 liefert x = 2; die Art folgt aus dem Vorzeichen des Leitkoeffizienten −1/r (oder aus f_r''(x) = −2/r); f_r(2) berechnen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f_r'(x) = 0 ⇔ x = 2, f_r(2) = 4/r + 2; als quadratische Funktion hat f_r für r < 0 ein Minimum und für r > 0 ein Maximum (amtlich)",
    zwischenergebnis="f_r''(x) = −2/r",
    niveau_geschaetzt="II", fehlerquelle="die Art ohne Rücksicht auf das Vorzeichen von r angeben (Minus vor dem x^2 als Maximum für alle r)",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Der Erwartungshorizont schreibt f(2) für f_r(2) (Druckfehler der Quelle). Schätzung II (die Fallunterscheidung verlangt der Text wörtlich – „in Abhängigkeit von r angeben“ –, Vorzeichen eines einzelnen Faktors: Routinekette); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet. CAS-Anteil: Ableitung und Gleichung mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS1", "d", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gemeinsame Punkte aller Graphen einer Schar bestimmen", typ_neben="",
    stichwoerter="f_r(0) = 2 für alle r|Symmetrie aller Graphen zur Geraden x = 2|gemeinsame Punkte (0; 2) und (4; 2)|zwei Parabeln haben höchstens zwei gemeinsame Punkte",
    voraussetzungen="Gleichsetzen zweier Scharfunktionen oder Symmetrie zur Scheitelgeraden|Zahl der gemeinsamen Punkte zweier Parabeln",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FR + "; jede Funktion der Schar hat bei x = 2 ein Extremum",
    gesucht="Koordinaten der Punkte, durch die alle Graphen der Schar verlaufen",
    verfahren="f_r1(x) = f_r2(x) mit r1 ≠ r2 liefert x = 0 oder x = 4, der Parameter fällt heraus; alternativ f_r(0) = 2 und Spiegelung an der Geraden x = 2",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2018MerhoehtBAnalysisCAS1-1c",
    ergebnis="Zwei verschiedene Parabeln haben höchstens zwei gemeinsame Punkte; da f_r(0) = 2 gilt und alle Graphen symmetrisch zur Geraden x = 2 sind, verlaufen alle Graphen der Schar durch (0; 2) und (4; 2) (amtlich)",
    zwischenergebnis="f_r(4) = 2",
    niveau_geschaetzt="II", fehlerquelle="nur den y-Achsenabschnitt (0; 2) angeben und den zweiten Punkt übersehen",
    bemerkung="Standardbezug: K1 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Gleichsetzen liefert x = 0 und x = 4). Typ wiederverwendet; der Erwartungshorizont argumentiert über die Symmetrie statt über das Gleichsetzen, das Ergebnis ist gleich. CAS-Anteil: Gleichsetzen und Lösen mit dem Rechner möglich.")
row("2018MerhoehtBAnalysisCAS1", "e", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Anzahl der Nullstellen einer Schar in Abhängigkeit vom Parameter über die Diskriminante ermitteln", typ_neben="",
    stichwoerter="f_r(x) = 0 ⇔ x^2 − 4x − 2r = 0|x = 2 ± √(4 + 2r)|Diskriminante 16 + 8r|r < −2 keine, r = −2 eine, r > −2 zwei Nullstellen",
    voraussetzungen="quadratische Gleichung mit Parameter lösen|Radikand auf sein Vorzeichen untersuchen|Fallunterscheidung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=FR, gesucht="Anzahl der Nullstellen von f_r in Abhängigkeit von r",
    verfahren="f_r(x) = 0 mit −r multiplizieren und nach x lösen: x = 2 ± √(4 + 2r); die Anzahl hängt vom Vorzeichen von 4 + 2r ab",
    schritte="3", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="f_r(x) = 0 ⇔ x = 2 − √(4 + 2r) ∨ x = 2 + √(4 + 2r); da 4 + 2r > 0 ⇔ r > −2, hat f_r für r < −2 keine Nullstelle, für r = −2 genau eine Nullstelle und für r > −2 genau zwei Nullstellen (amtlich)",
    zwischenergebnis="für r = −2: f_r(x) = 1/2 · (x − 2)^2, doppelte Nullstelle 2",
    niveau_geschaetzt="III", fehlerquelle="r = 0 als eigenen Fall behandeln, obwohl r ≠ 0 vorausgesetzt ist, oder den Fall r = −2 vergessen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Schätzung III (Diskriminante 16 + 8r, drei Fälle mit verschiedenem Ausgang ausgeführt – Nullfall-Regel: zählt –, Verkettung mit Fallunterscheidung); amtlich II – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Beleg für den Kandidaten „vom Text verlangte Fallunterscheidung ist amtlich II“ (iqb.md § 7). Typ wiederverwendet (hier ohne linearen Faktor). CAS-Anteil: quadratische Gleichung mit dem Rechner lösen, Fallunterscheidung eigen.")
row("2018MerhoehtBAnalysisCAS1", "f", innen="1", seite="1|2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Rechten Winkel in einem Dreieck aus Scharpunkten für bestimmte Ecken und Parameterbereiche ausschließen", typ_neben="",
    stichwoerter="rechter Winkel bei A_r oder B_r nur, wenn C senkrecht darüber läge|A_r, B_r und C auf demselben Graphen|für −2 < r < 0: 2 < x_B < 4|stumpfer Innenwinkel bei B_r",
    voraussetzungen="A_r und B_r liegen auf der x-Achse|ein Funktionsgraph hat zu jedem x nur einen Punkt|Lage einer Nullstelle für einen Parameterbereich abschätzen|stumpfer Winkel aus der Lage von C",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=FR + DREI,
    gesucht="Begründung der beiden Aussagen: weder bei A_r noch bei B_r kann ein rechter Winkel liegen; für −2 < r < 0 ist das Dreieck nicht rechtwinklig",
    verfahren="A_rB_r liegt auf der x-Achse; ein rechter Winkel bei A_r oder B_r verlangte, dass C senkrecht darüber liegt, also dieselbe x-Koordinate hat – unmöglich für verschiedene Punkte eines Graphen; für −2 < r < 0 ist 0 < √(4 + 2r) < 2, also 2 < x_B < 4, und der Winkel bei B_r ist stumpf",
    schritte="3", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="Einen rechten Winkel bei A_r oder B_r hätte das Dreieck genau dann, wenn die x-Koordinate von A_r bzw. B_r mit der von C übereinstimmte; das ist nicht möglich, da die drei Punkte auf demselben Funktionsgraphen liegen. Für −2 < r < 0 gilt für die x-Koordinate von B_r: 2 < x < 4; damit hat das Dreieck bei B_r einen stumpfen Innenwinkel und ist nicht rechtwinklig (amtlich)",
    zwischenergebnis="B_rA_r ∘ B_rC = 4 · (r + 2 − √(2r + 4)) < 0 für −2 < r < 0",
    niveau_geschaetzt="III", fehlerquelle="nur einen Zahlenwert von r prüfen, statt den ganzen Bereich zu begründen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Skalarprodukt bei B_r negativ, etwa −1,66 für r = −1). Schätzung III nach Deutungsliste (a): die Bedingungen für einen rechten Winkel sind erst aus der Geometrie zu übersetzen (C senkrecht über A_r oder B_r; Lage von B_r zwischen 2 und 4 als stumpfer Winkel), verkettet mit zwei Begründungen. Neuer Typ: vorhandene Typen weisen einen rechten Winkel über das Skalarprodukt nach, keiner schließt ihn für Ecken und Parameterbereiche einer Figur aus Scharpunkten aus. CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS1", "g", innen="1", seite="1|2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Ansätze für einen rechten Winkel in einem Dreieck aus Scharpunkten über Skalarprodukt und Steigungsprodukt erläutern", typ_neben="",
    stichwoerter="(−√(4 + 2r) − 2; −2) ∘ (√(4 + 2r) − 2; −2) = 0|Verbindungsvektoren von C zu A_r und B_r|2/(2 + √(4 + 2r)) · 2/(2 − √(4 + 2r)) = −1|Steigungen der Geraden A_rC und B_rC",
    voraussetzungen="Skalarprodukt null heißt senkrecht|Steigungsprodukt −1 heißt senkrecht|Verbindungsvektor und Steigung aus zwei Punkten",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=FR + DREI + "; jeder der beiden Ansätze (−√(4 + 2r) − 2; −2) ∘ (√(4 + 2r) − 2; −2) = 0 und 2/(2 + √(4 + 2r)) · 2/(2 − √(4 + 2r)) = −1 liefert die gesuchten Werte von r",
    gesucht="Erläuterung der beiden Ansätze",
    verfahren="Die Vektoren als Verbindungsvektoren CA_r und CB_r erkennen und Skalarprodukt null als rechten Winkel bei C deuten; die Brüche als Steigungen der Geraden A_rC und B_rC erkennen und Produkt −1 als Orthogonalität deuten",
    schritte="2", zahlenraum="Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="Die beiden Vektoren sind die Verbindungsvektoren von C zu A_r bzw. zu B_r; ist ihr Skalarprodukt null, so ist das Dreieck rechtwinklig. Die beiden Faktoren sind die Steigungen der Geraden durch A_r und C bzw. durch B_r und C; ist ihr Produkt −1, so ist das Dreieck rechtwinklig (amtlich)",
    zwischenergebnis="CA_r ∘ CB_r = 4 − 2r|Steigungsprodukt −2/r|beide Ansätze liefern r = 2",
    niveau_geschaetzt="III", fehlerquelle="die Vektoren als Ortsvektoren von A_r und B_r deuten oder nicht sagen, dass der rechte Winkel bei C liegt",
    bemerkung="Standardbezug: K4 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (beide Ansätze liefern r = 2). Erste Schätzung: II; korrigiert nach Deutungsliste (d) wie 2025MgrundlegendBAGLAA2WTR2, Teilaufgabe 1 d: die vorgegebenen Ansätze als Verbindungsvektoren bzw. Steigungen und als Rechtwinkligkeitsbedingung deuten (zwei Deutungen verkettet). Neuer Typ: vorhanden ist das Erläutern einer gegebenen Rechnung zum Geradenschnittpunkt, nicht zweier Rechtwinkligkeitsansätze an einer Figur aus Scharpunkten. CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS1", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="Flugkurve vom Typ P|Flugweite als positive Nullstelle von f_4|x = 2 + 2√3 ≈ 5,46",
    voraussetzungen="Flugweite als Nullstelle deuten|quadratische Gleichung lösen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Skizze", skizze=PAPIER_SK, kontext="Papierflieger/Flugkurve", textumfang="mittel",
    gegeben=PAPIER + "; ein Papierflieger bewegt sich entlang einer Flugkurve vom Typ P, die für x >= 0 durch f_4 beschrieben wird",
    gesucht="Nachweis, dass die Flugweite etwa 5,46 m beträgt",
    verfahren="f_4(x) = 0 für x >= 0 lösen",
    schritte="1", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="f_4(x) = 0 und x >= 0 liefern x ≈ 5,46 (amtlich)",
    zwischenergebnis="exakt x = 2 + 2√3; zweite Lösung 2 − 2√3 < 0 entfällt",
    niveau_geschaetzt="I", fehlerquelle="die negative Lösung nicht verwerfen oder den Scheitel als Flugweite nehmen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (5,464). Typ wiederverwendet. CAS-Anteil: Gleichung mit dem Rechner lösen.")
row("2018MerhoehtBAnalysisCAS1", "b", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="y(t) = −5t^2 + 4,45t + 2|Landung bei y(t) = 0|Flugzeit t ≈ 1,22 s",
    voraussetzungen="Landung als Nullstelle der Höhenfunktion deuten|quadratische Gleichung lösen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Skizze", skizze=PAPIER_SK, kontext="Papierflieger/Flugkurve", textumfang="mittel",
    gegeben=PAPIER + FLUG_T,
    gesucht="Nachweis auf der Grundlage dieses Modells, dass die Flugzeit etwa 1,22 s beträgt",
    verfahren="Die Landung ist y(t) = 0; die positive Lösung ist die Flugzeit",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="s", abhaengig_von="",
    ergebnis="y(t) = 0 liefert t ≈ 1,22 (amtlich)",
    zwischenergebnis="zweite Lösung t ≈ −0,33 entfällt",
    niveau_geschaetzt="I", fehlerquelle="die Nullstelle von f_4 statt der von y(t) verwenden oder den höchsten Punkt als Landung deuten",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (1,218). Schätzung I (Nullstelle von y(t) nachweisen, eine Rechnung); amtlich II – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet. CAS-Anteil: Gleichung mit dem Rechner lösen.")
row("2018MerhoehtBAnalysisCAS1", "c", innen="2", seite="2|3", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen",
    typ_neben="Integral der Geschwindigkeit als zurückgelegten Weg im Sachzusammenhang deuten",
    stichwoerter="Auftreffen bei t ≈ 1,22 s|v(1,22) ≈ 9,0 m/s|∫ von 0 bis 1,22 v(t) dt|Länge der Flugkurve vom Abwurf bis zur Landung",
    voraussetzungen="Zeitpunkt des Auftreffens aus der Flugzeit|Integral einer Geschwindigkeit als zurückgelegter Weg",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|beschreiben Sie", antwort="Zahl|Text",
    material="Skizze", skizze=PAPIER_SK, kontext="Papierflieger/Flugkurve", textumfang="mittel",
    gegeben=PAPIER + FLUG_T + "; die Flugzeit beträgt etwa 1,22 s; Term ∫ von 0 bis 1,22 v(t) dt",
    gesucht="Geschwindigkeit des Papierfliegers unmittelbar vor dem Auftreffen auf dem Boden; Bedeutung des Terms im Sachzusammenhang",
    verfahren="v(1,22) berechnen; das Integral der Geschwindigkeit über die Flugzeit ist der zurückgelegte Weg entlang der Flugkurve",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="m/s|m", abhaengig_von="2018MerhoehtBAnalysisCAS1-2b",
    ergebnis="v(1,22) ≈ 9,0, d. h. die Geschwindigkeit beträgt etwa 9,0 m/s; mit dem Term kann die Länge der Flugkurve vom Abwurf bis zur Landung berechnet werden (amtlich)",
    zwischenergebnis="∫ von 0 bis 1,22 v(t) dt ≈ 7,09|Bogenlänge des Graphen von f_4 von 0 bis 5,46 ≈ 7,08",
    niveau_geschaetzt="II", fehlerquelle="den Term als Flugweite (waagerechte Entfernung 5,46 m) statt als Länge der Flugkurve deuten",
    bemerkung="Standardbezug: K4 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (8,96; der Term ergibt etwa 7,09 m, passend zur Bogenlänge 7,08 m des Graphen von f_4 bis zur Landung). Typ wiederverwendet. Neuer Nebentyp: vorhanden ist nur „Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten“ (mit Berechnung), hier wird der Term nur gedeutet. CAS-Anteil: Funktionswert mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS1", "a", innen="3", seite="3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Funktionsgleichung aus knickfreiem Übergang und einer Wertbedingung rekonstruieren", typ_neben="",
    stichwoerter="s(x) = a/(x − 1,5) + b ab x = 0,5|kein Knick: s(0,5) = f_4(0,5) und s'(0,5) = f_4'(0,5)|f_4(0,5) = 2,4375, f_4'(0,5) = 0,75|a = −0,75, b = 1,6875",
    voraussetzungen="knickfrei heißt gleicher Funktionswert und gleiche Steigung|Ableitung von a/(x − 1,5)|lineares Gleichungssystem",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=PAPIER_SK, kontext="Papierflieger/Flugkurve", textumfang="mittel",
    gegeben=PAPIER + S_TYP + "; zur Kontrolle: a = −0,75, b = 1,6875",
    gesucht="die Werte von a und b",
    verfahren="s(0,5) = f_4(0,5) und s'(0,5) = f_4'(0,5) mit s'(x) = −a/(x − 1,5)^2 aufstellen: −a + b = 2,4375 und −a = 0,75",
    schritte="3", zahlenraum="dezimal|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="s(0,5) = f_4(0,5) ∧ s'(0,5) = f_4'(0,5) ⇔ a = −0,75 ∧ b = 1,6875 (amtlich)",
    zwischenergebnis="f_4(0,5) = 39/16|f_4'(0,5) = 3/4",
    niveau_geschaetzt="II", fehlerquelle="nur gleiche Funktionswerte fordern oder beim Ableiten von a/(x − 1,5) das Vorzeichen verlieren",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (hier gebrochenrationaler Ansatz mit zwei Parametern allein aus gleichem Wert und gleicher Steigung an der Übergangsstelle, ohne weitere Wertbedingung). CAS-Anteil: Gleichungssystem mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS1", "b", innen="3", seite="3", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt der Tangente mit vorgegebener Steigung berechnen", typ_neben="",
    stichwoerter="Steigungswinkel 85°|s'(x) = tan 85° ≈ 11,43|Lösung links der Polstelle x = 1,5|x ≈ 1,24 m",
    voraussetzungen="Steigung aus dem Steigungswinkel über den Tangens|Gleichung mit dem Rechner lösen|Lösung links der Polstelle wählen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Skizze", skizze=PAPIER_SK, kontext="Papierflieger/Flugkurve", textumfang="kurz",
    gegeben=PAPIER + S_TYP + "; s(x) = −0,75/(x − 1,5) + 1,6875",
    gesucht="Nachweis, dass der Papierflieger den Steigungswinkel von 85° in einer horizontalen Entfernung von etwa 1,24 m vom Abwurfpunkt erreicht",
    verfahren="s'(x) = 0,75/(x − 1,5)^2 = tan 85° mit x < 1,5 lösen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="m|°", abhaengig_von="2018MerhoehtBAnalysisCAS1-3a",
    ergebnis="s'(x) = tan(85°) ∧ x < 1,5 liefert x ≈ 1,24 (amtlich)",
    zwischenergebnis="tan 85° ≈ 11,43|zweite Lösung x ≈ 1,76 hinter der Polstelle",
    niveau_geschaetzt="II", fehlerquelle="tan 85° im Bogenmaß auswerten oder die Lösung rechts der Polstelle nehmen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (1,2438). Typ wiederverwendet, Steigung aus tan 85°. CAS-Anteil: Gleichung mit dem Rechner lösen.")
row("2018MerhoehtBAnalysisCAS1", "c", innen="3", seite="3", punkte="6", afb_amtlich="II",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Kurvenlänge über eine vorgegebene Integralformel berechnen und mit der Länge von Streckenzügen vergleichen", typ_neben="",
    stichwoerter="L = ∫ von a bis b √(1 + (h'(x))^2) dx|Bogen von f_4 über [0; 0,5]|Bogen von s über [0,5; 1,24]|senkrechter Absturz der Länge s(1,24)|etwa 7,56 m",
    voraussetzungen="Flugkurve abschnittsweise zusammensetzen|vorgegebene Formel mit der Ableitung auswerten|Integral numerisch berechnen|Absturzhöhe als Funktionswert",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Skizze", skizze=PAPIER_SK, kontext="Papierflieger/Flugkurve", textumfang="mittel",
    gegeben=PAPIER + S_TYP + "; s(x) = −0,75/(x − 1,5) + 1,6875; den Steigungswinkel 85° erreicht der Papierflieger bei x ≈ 1,24; ist ein Kurvenstück Graph einer in [a; b] definierten Funktion h mit Ableitung h', so gilt für seine Länge L = ∫ von a bis b √(1 + (h'(x))^2) dx",
    gesucht="Länge der Flugkurve des Papierfliegers",
    verfahren="Bogenlänge von f_4 über [0; 0,5] und von s über [0,5; 1,24] mit der Formel numerisch berechnen und die Länge s(1,24) des senkrechten Absturzes addieren",
    schritte="4", zahlenraum="dezimal", einheiten="m", abhaengig_von="2018MerhoehtBAnalysisCAS1-3a|2018MerhoehtBAnalysisCAS1-3b",
    ergebnis="∫ von 0 bis 0,5 √(1 + (f_4'(x))^2) dx + ∫ von 0,5 bis 1,24 √(1 + (s'(x))^2) dx + s(1,24) ≈ 7,56; die Flugkurve ist etwa 7,56 m lang (amtlich)",
    zwischenergebnis="Bogen von f_4 ≈ 0,665|Bogen von s ≈ 2,324|s(1,24) ≈ 4,572",
    niveau_geschaetzt="II", fehlerquelle="den senkrechten Absturz vergessen oder nur die Bogenlänge von s ansetzen",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (7,561 mit der gerundeten Stelle 1,24). Mit der ungerundeten Stelle 1,2438 liefert die eigene Rechnung etwa 7,65 (Bogen von s ≈ 2,368, Absturz ≈ 4,615): wegen der steilen Kurve reagiert das Ergebnis stark auf die Rundung aus 3 b; das amtliche Ergebnis bleibt. Typ wiederverwendet, hier abschnittsweise (zwei Bögen plus senkrechter Absturz) und ohne Vergleich mit Streckenzügen. Thema ersatzweise Stammfunktion und Hauptsatz (Kurvenlänge über ein Integral hat keine Themenzeile). CAS-Anteil: Integrale numerisch mit dem Rechner, Zerlegung eigen.")
row("2018MerhoehtBAnalysisCAS1", "", innen="4", seite="3", punkte="5", afb_amtlich="III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt einer Tangente durch einen vorgegebenen Punkt berechnen", typ_neben="",
    stichwoerter="Flugkurve vom Typ G|Gerade g(x) = m · x + n mit g(17,6) = 0|Übergang ohne Knick als Tangente an f_4|Übergangsstelle x ≈ 2,39|Höhe etwa 3,0 m",
    voraussetzungen="ohne Knick heißt gleicher Wert und gleiche Steigung|Tangente durch einen Punkt außerhalb des Graphen|Gleichungssystem mit dem Rechner lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Skizze", skizze=PAPIER_SK, kontext="Papierflieger/Flugkurve", textumfang="mittel",
    gegeben=PAPIER + "; Flugkurve vom Typ G: im ersten Teil durch f_4 beschrieben, ab einem bestimmten Punkt bis zum Boden durch eine Gerade; der Übergang vom ersten zum zweiten Teil erfolgt ohne Knick; die Flugweite beträgt 17,6 m",
    gesucht="Höhe, in der der gekrümmte Teil der Flugkurve in den geradlinigen übergeht",
    verfahren="g(x) = m · x + n mit g(17,6) = 0, g(u) = f_4(u) und g'(u) = f_4'(u) für u < 17,6 lösen; f_4(u) berechnen",
    schritte="4", zahlenraum="dezimal", einheiten="m", abhaengig_von="",
    ergebnis="g(x) = m · x + n; g(17,6) = 0 ∧ g(x) = f_4(x) ∧ g'(x) = f_4'(x) liefert für x < 17,6: x ≈ 2,39; f_4(2,39) ≈ 3,0, d. h. der Übergang erfolgt in einer Höhe von etwa 3,0 m (amtlich)",
    zwischenergebnis="u^2 − 35,2u + 78,4 = 0|u ≈ 2,389, zweite Lösung u ≈ 32,8 entfällt|Steigung der Geraden ≈ −0,195",
    niveau_geschaetzt="III", fehlerquelle="den Übergang im höchsten Punkt oder an der Nullstelle 5,46 annehmen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (2,389; 2,962). Schätzung III nach Deutungsliste (a): „ohne Knick“ und die geradlinige Fortsetzung bis zum Boden sind erst als Tangente an den Graphen von f_4 durch den äußeren Punkt (17,6; 0) zu übersetzen. Aufgabe ohne Teilaufgabenbuchstaben, eine Zeile mit 5 BE. Typ wiederverwendet. CAS-Anteil: Gleichungssystem mit dem Rechner lösen, Ansatz eigen.")
# ---- Analysis CAS 2 (Aufgabe 1: ganzrationale Funktion vierten Grades, 24 BE; Aufgabe 2: Glukosewert eines
# Diabetespatienten mit Anschlussfunktion h_k, 26 BE)
GLU = ("Gegeben ist die in IR definierte Funktion f mit f(x) = −1/10^6 · x^4 + 4/9375 · x^3 − 13/250 · x^2 + 8/5 · x + 140")
EXTR = "; Extremstellen 20, 100 und 200: Hochpunkte (20; 11584/75) und (200; 580/3), Tiefpunkt (100; 320/3)"
GLUK = (GLU + "; mit einem CGM-Gerät wird der Glukosewert eines Patienten ständig gemessen: f beschreibt für 0 <= x <= 240 "
        "modellhaft seine Entwicklung, x ist die seit Beobachtungsbeginn vergangene Zeit in Minuten, f(x) der Glukosewert "
        "in mg/dl")
GLUK_SK = ("Abbildung neben dem Text: Koordinatensystem auf Kästchengitter, x-Achse von 0 bis 240 (Beschriftung 0, 40, 80, "
           "…, 240, ein Kästchen 20), y-Achse von 0 bis 200 (Beschriftung 40, 80, …, 200, ein Kästchen 20); Graph von f für "
           "0 <= x <= 240: beginnt bei (0; 140), steigt zum Hochpunkt bei etwa (20; 154), fällt zum Tiefpunkt bei etwa "
           "(100; 107), steigt zum Hochpunkt bei etwa (200; 193) und fällt steil bis etwa (240; 109)")
F2_SK = ("zu erstellende Skizze (Erwartungshorizont): Graph von f im Koordinatensystem mit x von etwa −10 bis 280 "
         "(Beschriftung 0, 40, …, 280) und y von 0 bis 200; gestrichelte Strecke vom Ursprung zum Graphenpunkt (u; f(u)) "
         "bei u ≈ 217, gestrichelte Senkrechten bei x = u und x = 240; A1 ist das Dreieck unter der Strecke über [0; u], A2 "
         "die Fläche unter dem Graphen über [u; 240], A3 die Fläche zwischen Graph und Strecke über [0; u]")
H_K = ("; zum Zeitpunkt 240 Minuten nimmt der Patient Traubenzucker zu sich, die anschließende Entwicklung soll im Modell "
       "durch eine Funktion g beschrieben werden; Bedingung: Glukosewert und momentane Änderungsrate zum Zeitpunkt 240 "
       "Minuten sollen unabhängig davon sein, ob sie mit f oder mit g ermittelt werden; dazu werden zunächst die in IR "
       "definierten Funktionen h_k mit h_k(x) = 50 − 50 · (k · x + 1)^2 · e^(−k · x), k ∈ IR+, betrachtet")
row("2018MerhoehtBAnalysisCAS2", "a", innen="1", seite="1", punkte="5", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Lage und Art aller lokalen Extrempunkte bestimmen", typ_neben="",
    stichwoerter="f'(x) = 0 ⇔ x = 20, 100, 200|f''(20) = −36/625 < 0, f''(100) = 4/125 > 0, f''(200) = −9/125 < 0|Hochpunkte (20; 11584/75) und (200; 580/3)|Tiefpunkt (100; 320/3)",
    voraussetzungen="Ableitungen einer ganzrationalen Funktion|Nullstellen der ersten Ableitung|zweite Ableitung als Kriterium",
    format="Rechnung", operator="Berechnen Sie|bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=GLU + "; zur Kontrolle: die Extremstellen sind 20, 100 und 200",
    gesucht="Koordinaten und Art der Extrempunkte des Graphen von f",
    verfahren="f'(x) = 0 lösen, das Vorzeichen von f'' an den drei Stellen bestimmen, Funktionswerte berechnen",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 0 ⇔ x = 20 ∨ x = 100 ∨ x = 200; f''(20) = −36/625 < 0, f''(100) = 4/125 > 0, f''(200) = −9/125 < 0; Hochpunkte (20; 11584/75) und (200; 580/3), Tiefpunkt (100; 320/3) (amtlich)",
    zwischenergebnis="11584/75 ≈ 154,45|580/3 ≈ 193,33|320/3 ≈ 106,67",
    niveau_geschaetzt="II", fehlerquelle="nur die Extremstellen ohne y-Koordinaten angeben oder die Art ohne zweite Ableitung aus der Kontrollangabe raten",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Der Erwartungshorizont von 1 a bis 1 c steht unten auf Seite 3 und war beim Schätzen in Sicht. Schätzung II (Ableitung, Gleichung, zweite Ableitung – Verkettung nach der Liste); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet. CAS-Anteil: Ableitungen, Gleichung und Funktionswerte mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: y-Achsenschnittpunkt angeben und Anzahl der Nullstellen aus Grenzverhalten und Tiefpunkt ohne Rechnung begründen", typ_neben="",
    stichwoerter="Schnittpunkt mit der y-Achse (0; 140)|f(x) → −∞ für x → ±∞|Tiefpunkt (100; 320/3) über der x-Achse|genau zwei Nullstellen",
    voraussetzungen="Verhalten im Unendlichen am Leitkoeffizienten|Lage des einzigen Tiefpunkts zur x-Achse|Vorzeichenwechsel als Nullstelle",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=GLU + EXTR,
    gesucht="Koordinaten des Schnittpunkts des Graphen von f mit der y-Achse; Begründung ohne weitere Rechnung, dass f genau zwei Nullstellen hat",
    verfahren="f(0) = 140; der Graph kommt von −∞ und geht nach −∞, sein einziger Tiefpunkt liegt über der x-Achse; also schneidet er die x-Achse links des ersten und rechts des zweiten Hochpunkts je genau einmal",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="2018MerhoehtBAnalysisCAS2-1a",
    ergebnis="Schnittpunkt mit der y-Achse: (0; 140); da f(x) für x → ±∞ gegen −∞ strebt und die y-Koordinate des Tiefpunkts positiv ist, hat f genau zwei Nullstellen (amtlich)",
    zwischenergebnis="Nullstellen etwa −35,1 und 256,6",
    niveau_geschaetzt="II", fehlerquelle="aus dem Grad 4 auf bis zu vier Nullstellen schließen, ohne den Tiefpunkt zu nutzen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (Nullstellen etwa −35,07 und 256,61). Der Erwartungshorizont von 1 a bis 1 c steht unten auf Seite 3 und war beim Schätzen in Sicht. Schätzung II (Anzahl der Nullstellen ohne Rechnung aus Verhalten im Unendlichen und Tiefpunkt begründen); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: der vorhandene Typ mit y-Achsenschnittpunkt ermittelt die Nullstellen aus der faktorisierten Form (anderer Weg). CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS2", "c", innen="1", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Gleichung f(t) = f(t − c) für gleiche Werte im Abstand c mit dem Rechner lösen", typ_neben="",
    stichwoerter="50 < x < 130|zwei x-Werte im Abstand 60 mit gleichem Funktionswert|f(x) = f(x + 60) ⇔ x ≈ 69,2|Paar 69,2 und 129,2, Funktionswert etwa 120,2",
    voraussetzungen="Bedingung als Gleichung f(x) = f(x + 60) ansetzen|Gleichung mit dem Rechner lösen|Lösung im Bereich wählen",
    format="Rechnung", operator="Bestimmen Sie|geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=GLU + "; für 50 < x < 130 gibt es ein Paar von x-Werten, die sich um 60 unterscheiden und deren Funktionswerte übereinstimmen",
    gesucht="dieses Paar von x-Werten und der zugehörige Funktionswert",
    verfahren="f(x) = f(x + 60) mit dem Rechner lösen, die Lösung mit 50 < x und x + 60 < 130 wählen, f(x) berechnen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Für 50 < x < 130 liefert f(x) = f(x + 60): x ≈ 69,2; die gesuchten x-Werte sind x ≈ 69,2 und x ≈ 129,2, der zugehörige Funktionswert ist etwa 120,2 (amtlich)",
    zwischenergebnis="weitere reelle Lösungen x ≈ −4,38 und x ≈ 165,2 außerhalb des Bereichs",
    niveau_geschaetzt="II", fehlerquelle="f(x) = f(x) + 60 statt f(x) = f(x + 60) ansetzen",
    bemerkung="Standardbezug: K2 III, K5 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (69,153; 129,153; 120,20). Der Erwartungshorizont von 1 a bis 1 c steht unten auf Seite 3 und war beim Schätzen in Sicht. Schätzung II (die Bedingung „um 60 unterscheiden … übereinstimmen“ gibt der Text wörtlich vor – Ausnahme zu (a)); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet. CAS-Anteil: Gleichung mit dem Rechner lösen, Ansatz eigen.")
row("2018MerhoehtBAnalysisCAS2", "d", innen="1", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extremstelle zwischen zwei Stellen mit gleichem Funktionswert ohne Rechnung begründen", typ_neben="",
    stichwoerter="f(69,2) = f(129,2)|f ganzrational, also stetig und differenzierbar|zwischen zwei Stellen mit gleichem Wert mindestens eine Extremstelle|Satz von Rolle",
    voraussetzungen="Stetigkeit und Differenzierbarkeit ganzrationaler Funktionen|eine nicht konstante Funktion hat zwischen zwei gleichen Werten ein Maximum oder Minimum",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=GLU + "; für 50 < x < 130 gibt es ein Paar von x-Werten im Abstand 60 mit übereinstimmenden Funktionswerten (x ≈ 69,2 und x ≈ 129,2)",
    gesucht="Begründung, dass sich daraus schließen lässt, dass f für 50 < x < 130 mindestens eine Extremstelle hat",
    verfahren="Eine ganzrationale, nicht konstante Funktion, die an zwei Stellen denselben Wert annimmt, muss dazwischen die Richtung wechseln; dort liegt eine Extremstelle",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2018MerhoehtBAnalysisCAS2-1c",
    ergebnis="Für 50 < x < 130 gibt es ein Paar von x-Werten mit übereinstimmenden Funktionswerten; da f ganzrational ist, liegt zwischen diesen mindestens eine Extremstelle (amtlich)",
    zwischenergebnis="tatsächlich liegt der Tiefpunkt bei x = 100 dazwischen",
    niveau_geschaetzt="III", fehlerquelle="mit der Extremstelle 100 aus Teilaufgabe 1 a statt mit den Informationen aus 1 c argumentieren",
    bemerkung="Standardbezug: K1 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (f'(100) = 0 zwischen 69,2 und 129,2). Schätzung III nach dem Prinzip der engen Fassung: die Beziehung zwischen gleichen Funktionswerten und einer Extremstelle dazwischen wird hergeleitet (Satz von Rolle), nicht nachgerechnet. Neuer Typ: kein vorhandener Typ schließt aus gleichen Funktionswerten auf eine Extremstelle. CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS2", "e", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Senkrechte Gerade zur Halbierung einer Fläche über den Flächenterm bestimmen", typ_neben="",
    stichwoerter="Flächenstück zwischen Graph, Koordinatenachsen und x = 240|∫ von 0 bis k f(x) dx = ∫ von k bis 240 f(x) dx|k ≈ 135,5|Gerade x = 135,5",
    voraussetzungen="f(x) > 0 auf [0; 240]|Halbierung als Gleichung zweier Integrale|Gleichung mit dem Rechner lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=GLU + "; der Graph von f schließt mit den Koordinatenachsen und der Geraden x = 240 ein Flächenstück ein",
    gesucht="Gleichung der zur y-Achse parallelen Geraden, die dieses Flächenstück halbiert",
    verfahren="Ansatz x = k: ∫ von 0 bis k f(x) dx = ∫ von k bis 240 f(x) dx (oder gleich der Hälfte von ∫ von 0 bis 240 f(x) dx) mit dem Rechner nach k lösen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="∫ von 0 bis k f(x) dx = ∫ von k bis 240 f(x) dx liefert k ≈ 135,5, d. h. die Gerade wird näherungsweise durch die Gleichung x = 135,5 beschrieben (amtlich)",
    zwischenergebnis="∫ von 0 bis 240 f(x) dx = 867648/25 ≈ 34706",
    niveau_geschaetzt="II", fehlerquelle="die Intervallmitte x = 120 angeben oder den Funktionswert statt der Fläche halbieren",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (135,46). Typ wiederverwendet (hier ganzrationale Funktion, Gleichung mit dem Rechner statt über den Logarithmus). CAS-Anteil: Integrale und Gleichung mit dem Rechner, Ansatz eigen.")
row("2018MerhoehtBAnalysisCAS2", "f", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Lösungsschritte zu einem Flächenverhältnis von Segment und Dreieck geometrisch deuten und Flächen einzeichnen", typ_neben="",
    stichwoerter="1/2 · u · f(u) + ∫ von u bis 240 f(x) dx = 2/3 · ∫ von 0 bis 240 f(x) dx für u ≈ 217|zweite Gerade durch den Ursprung und (u; f(u))|Dreieck A1 unter der Geraden|A1 + A2 = 2/3 · (A1 + A2 + A3)",
    voraussetzungen="1/2 · u · f(u) als Dreiecksfläche erkennen|Integral als Fläche unter dem Graphen|Teilung einer Fläche durch eine Strecke",
    format="Zeichnen|Kurzantwort", operator="Veranschaulichen Sie", antwort="Grafik|Text",
    material="keins", skizze=F2_SK, kontext="ohne", textumfang="mittel",
    gegeben=GLU + "; das Flächenstück zwischen dem Graphen von f, den Koordinatenachsen und der Geraden x = 240; Aussage zu einer zweiten Geraden, die das Flächenstück teilt: für u ≈ 217 gilt 1/2 · u · f(u) + ∫ von u bis 240 f(x) dx = 2/3 · ∫ von 0 bis 240 f(x) dx",
    gesucht="Veranschaulichung der Aussage mit einer geeigneten Skizze",
    verfahren="1/2 · u · f(u) als Dreieck mit den Ecken (0; 0), (u; 0) und (u; f(u)) deuten, ∫ von u bis 240 f(x) dx als Fläche rechts von x = u; die Gerade durch den Ursprung und (u; f(u)) teilt das Flächenstück so, dass der Teil unter ihr zusammen mit dem rechten Streifen zwei Drittel ausmacht",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Skizze mit der Strecke vom Ursprung zu (u; f(u)) und den Teilflächen A1 (Dreieck unter der Strecke), A2 (unter dem Graphen über [u; 240]) und A3 (zwischen Graph und Strecke); es gilt A1 + A2 = 2/3 · (A1 + A2 + A3) (amtlich)",
    zwischenergebnis="u ≈ 216,96|A1 ≈ 19643, A2 ≈ 3494, A3 ≈ 11569",
    niveau_geschaetzt="III", fehlerquelle="die zweite Gerade senkrecht bei x = u zeichnen statt als Strecke vom Ursprung zu (u; f(u))",
    bemerkung="Standardbezug: K2 III, K4 III, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (u ≈ 216,96). Die Teilaufgabe verlangt selbst eine Skizze; skizze beschreibt die zu erstellende Darstellung nach dem Erwartungshorizont. Schätzung III nach Deutungsliste (d): die Gerade durch den Ursprung und (u; f(u)) ist erst zu finden, Dreieck und Restfläche als Deutung der Terme verkettet. Typ wiederverwendet (hier eine vorgegebene Gleichung statt vorgelegter Lösungsschritte, Teilung durch eine Ursprungsgerade). CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS2", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Bereich mit Funktionswerten über einer Schranke aus dem Graphen bestimmen", typ_neben="",
    stichwoerter="Glukosewert über 170 mg/dl|Schnitt mit der Geraden y = 170|zwischen etwa 170 und 223 Minuten|etwa 53 Minuten",
    voraussetzungen="Schranke als waagerechte Gerade|Schnittstellen am Graphen oder mit dem Rechner bestimmen|Dauer als Differenz",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GLUK_SK, kontext="Medizin/Glukosewert", textumfang="mittel",
    gegeben=GLUK + "; hohe Glukosewerte über längere Zeit gelten als Risikofaktor",
    gesucht="wie lange im betrachteten Zeitraum Glukosewerte über 170 mg/dl gemessen wurden",
    verfahren="f(x) = 170 für 0 <= x <= 240 lösen (oder Graph und Gerade y = 170 schneiden); f liegt nur zwischen den beiden Schnittstellen hinter dem Tiefpunkt über 170; Differenz bilden",
    schritte="2", zahlenraum="dezimal", einheiten="min", abhaengig_von="",
    ergebnis="Mithilfe des Graphen von f und der Geraden y = 170 ergibt sich, dass Glukosewerte über 170 mg/dl zwischen etwa 170 Minuten und 223 Minuten nach Beobachtungsbeginn und damit etwa 53 Minuten lang gemessen wurden (amtlich)",
    zwischenergebnis="Schnittstellen 169,84 und 222,77",
    niveau_geschaetzt="II", fehlerquelle="den ersten Hochpunkt (etwa 154 mg/dl) für einen Wert über 170 halten",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (52,93). Schätzung II (f(x) = 170 lösen, Dauer als Differenz); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet. CAS-Anteil: Gleichung mit dem Rechner lösen oder Schnittpunkte am Graphen bestimmen.")
row("2018MerhoehtBAnalysisCAS2", "b", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Größte und kleinste Rate im Zeitraum über Ableitung und Randwerte berechnen", typ_neben="",
    stichwoerter="stärkster Anstieg als größter Wert von f'|f''(x) = 0 ∧ f'''(x) < 0 ⇔ x ≈ 158,7|f'(158,7) ≈ 1,3 < f'(0) = 1,6|am stärksten zu Beobachtungsbeginn",
    voraussetzungen="Maximum der Ableitung über die zweite und dritte Ableitung|Randwerte vergleichen|Ableitungen mit dem Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GLUK_SK, kontext="Medizin/Glukosewert", textumfang="kurz",
    gegeben=GLUK,
    gesucht="Zeitpunkt im betrachteten Zeitraum, zu dem der Glukosewert am stärksten ansteigt",
    verfahren="Lokales Maximum von f' über f''(x) = 0 und f'''(x) < 0 bestimmen und mit den Randwerten f'(0) und f'(240) vergleichen",
    schritte="3", zahlenraum="dezimal", einheiten="min", abhaengig_von="",
    ergebnis="f''(x) = 0 ∧ f'''(x) < 0 liefert x ≈ 158,7; da f'(0) = 1,6 und f'(158,7) ≈ 1,3, steigt der Glukosewert zu Beobachtungsbeginn am stärksten an (amtlich)",
    zwischenergebnis="zweite Wendestelle x ≈ 54,6 mit f' ≈ −0,91|f'(240) ≈ −4,93",
    niveau_geschaetzt="II", fehlerquelle="die innere Wendestelle 158,7 angeben, ohne den Randwert bei x = 0 zu prüfen",
    bemerkung="Standardbezug: K1 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (158,73; f'(158,73) ≈ 1,345). Typ wiederverwendet (hier nur die größte Rate, sie liegt am Rand). CAS-Anteil: Ableitungen und Gleichung mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS2", "c", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Differenzen- und Differentialquotient durch Sekante und Tangente veranschaulichen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="I: (f(100) − f(20))/(100 − 20) als Steigung der Sekante|mittlere Änderungsrate von 20 bis 100 Minuten|II: lim für x → 60 von (f(60) − f(x))/(60 − x) als Steigung der Tangente in (60; f(60))|momentane Änderungsrate nach 60 Minuten",
    voraussetzungen="Differenzenquotient als Sekantensteigung|Grenzwert des Differenzenquotienten als Tangentensteigung|Änderungsrate im Sachzusammenhang mit Einheit",
    format="Eintragen|Kurzantwort", operator="Veranschaulichen Sie|geben Sie an", antwort="Grafik|Text",
    material="Koordinatensystem", skizze=GLUK_SK + "; einzutragen (Erwartungshorizont): die fallende Sekante I durch etwa (20; 154) und (100; 107) und die steilere fallende Tangente II in (60; 128)",
    kontext="Medizin/Glukosewert", textumfang="mittel",
    gegeben=GLUK + "; Terme I: (f(100) − f(20))/(100 − 20) und II: lim für x → 60 von (f(60) − f(x))/(60 − x)",
    gesucht="Veranschaulichung jedes Terms in der Abbildung durch eine Gerade und seine Bedeutung im Sachzusammenhang",
    verfahren="Zu I die Sekante durch die Graphenpunkte bei 20 und 100, zu II die Tangente im Graphenpunkt bei 60 einzeichnen; die Steigungen als mittlere bzw. momentane Änderungsrate des Glukosewerts deuten",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="mg/dl pro Minute", abhaengig_von="",
    ergebnis="Sekante durch (20; f(20)) und (100; f(100)) sowie Tangente in (60; f(60)); I: mittlere Änderungsrate des Glukosewerts im Zeitraum von 20 Minuten bis 100 Minuten nach Beobachtungsbeginn; II: momentane Änderungsrate des Glukosewerts 60 Minuten nach Beobachtungsbeginn (amtlich)",
    zwischenergebnis="I = −224/375 ≈ −0,60|II = f'(60) = −112/125 ≈ −0,90",
    niveau_geschaetzt="I", fehlerquelle="für II eine Sekante zwischen zwei festen Punkten zeichnen oder I als Änderung statt als Änderung pro Minute deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II. AB amtlich: II. Amtlich (Geraden in der Abbildung des Erwartungshorizonts), eigene Rechnung bestätigt (Sekantensteigung −0,597, Tangentensteigung −0,896). Schätzung I (Reproduktion: Sekantensteigung als mittlere, Grenzwert als momentane Änderungsrate); amtlich II – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: vorhandene Typen berechnen oder deuten die mittlere Änderungsrate, keiner veranschaulicht Differenzen- und Differentialquotient zugleich als Sekante und Tangente. CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS2", "d", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Länge des Zeitraums mit Mindeständerungsrate über die Lösungen von f'(x) = c berechnen", typ_neben="",
    stichwoerter="|f'(x)| <= 0,3|f'(x) = 0,3 und f'(x) = −0,3|drei Zeiträume um die Extremstellen 20, 100 und 200|zusammen etwa 38 Minuten",
    voraussetzungen="Betragsungleichung als zwei Gleichungen|Gleichungen mit dem Rechner lösen|Teilintervalle zuordnen und addieren",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GLUK_SK, kontext="Medizin/Glukosewert", textumfang="kurz",
    gegeben=GLUK,
    gesucht="wie lange die momentane Änderungsrate des Glukosewerts im betrachteten Zeitraum insgesamt zwischen −0,3 mg/dl pro Minute und +0,3 mg/dl pro Minute lag",
    verfahren="|f'(x)| <= 0,3 lösen: f'(x) = 0,3 und f'(x) = −0,3 liefern sechs Stellen; die drei Zeiträume um die Extremstellen bestimmen und ihre Längen addieren",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="min", abhaengig_von="",
    ergebnis="Mit |f'(x)| <= 0,3 lag die momentane Änderungsrate von etwa 15,2 bis 25,8 Minuten, von etwa 90,3 bis 109,3 Minuten und von etwa 195,5 bis 203,9 Minuten im angegebenen Bereich, insgesamt also etwa 38 Minuten lang (amtlich)",
    zwischenergebnis="Randstellen 15,21; 25,80; 90,27; 109,26; 195,53; 203,92",
    niveau_geschaetzt="II", fehlerquelle="nur f'(x) = 0,3 lösen oder die Zeiträume zwischen falschen Randstellen bilden",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (37,97). Typ wiederverwendet, hier |f'(x)| <= 0,3 mit mehreren Teilintervallen. CAS-Anteil: Gleichungen oder Ungleichung mit dem Rechner lösen.")
row("2018MerhoehtBAnalysisCAS2", "e", innen="2", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Mittelwert einer Funktion als Integral geteilt durch die Intervalllänge berechnen und deuten",
    typ_neben="Prozentuale Abweichung eines Näherungswerts vom exakten Wert berechnen",
    stichwoerter="Mittelwert 1/80 · ∫ von 20 bis 100 f(x) dx ≈ 129,2|Durchschnitt der neun Messwerte f(20), f(30), …, f(100) ≈ 129,3|Integralmittel etwa 0,1 % kleiner",
    voraussetzungen="vorgegebene Mittelwertformel anwenden|arithmetisches Mittel von neun Funktionswerten|prozentuale Abweichung bezogen auf den Vergleichswert",
    format="Rechnung", operator="Berechnen Sie|Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GLUK_SK, kontext="Medizin/Glukosewert", textumfang="mittel",
    gegeben=GLUK + "; der Mittelwert der Funktionswerte von f für x ∈ [a; b] kann mit 1/(b − a) · ∫ von a bis b f(x) dx berechnet werden; von 20 bis 100 Minuten wurden im Abstand von jeweils zehn Minuten Glukosewerte gemessen, beginnend 20 Minuten nach Beobachtungsbeginn",
    gesucht="Mittelwert aller Glukosewerte von 20 bis 100 Minuten nach Beobachtungsbeginn; seine prozentuale Abweichung vom Durchschnitt der im Abstand von zehn Minuten gemessenen Werte",
    verfahren="1/80 · ∫ von 20 bis 100 f(x) dx mit dem Rechner; Mittel der neun Werte f(20), f(30), …, f(100); Differenz durch den Durchschnitt der Messwerte teilen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="mg/dl|%", abhaengig_von="",
    ergebnis="Mittelwert aller Glukosewerte: 1/80 · ∫ von 20 bis 100 f(x) dx ≈ 129,2; Mittelwert der im Abstand von zehn Minuten gemessenen Werte: 1/9 · (f(20) + f(30) + … + f(100)) ≈ 129,3; der Mittelwert aller Glukosewerte ist etwa 0,1 % kleiner (amtlich)",
    zwischenergebnis="48448/375 ≈ 129,195|9701/75 ≈ 129,347|Abweichung ≈ −0,12 %",
    niveau_geschaetzt="II", fehlerquelle="durch 8 statt durch 9 Messwerte teilen oder die Abweichung auf den falschen Grundwert beziehen",
    bemerkung="Standardbezug: K3 I, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (129,195 und 129,347; Abweichung −0,12 %, amtlich gerundet 0,1 %). Typ und Nebentyp wiederverwendet. CAS-Anteil: Integral und Funktionswerte mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS2", "f", innen="2", seite="3", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Parameter einer Exponentialfunktion aus der Änderungsrate zum Anfangszeitpunkt bestimmen", typ_neben="",
    stichwoerter="h_k(x) = 50 − 50 · (k · x + 1)^2 · e^(−k · x)|h_k'(0) = −50k|f'(240) = −616/125|k = 308/3125",
    voraussetzungen="Produkt- und Kettenregel|Ableitung an der Stelle 0|lineare Gleichung in k",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Medizin/Glukosewert", textumfang="mittel",
    gegeben=GLUK + H_K,
    gesucht="Wert von k, für den die momentane Änderungsrate von h_k zum Zeitpunkt 0 mit der momentanen Änderungsrate von f zum Zeitpunkt 240 Minuten übereinstimmt",
    verfahren="h_k'(0) = f'(240) aufstellen und nach k lösen",
    schritte="2", zahlenraum="Bruch|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="h_k'(0) = f'(240) ⇔ k = 308/3125 (amtlich)",
    zwischenergebnis="h_k'(0) = −50k|f'(240) = −4,928|k ≈ 0,0986",
    niveau_geschaetzt="II", fehlerquelle="h_k(0) = f(240) statt der Ableitungen gleichsetzen",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (hier ist die Änderungsrate erst als f'(240) zu berechnen). CAS-Anteil: Ableitungen und Gleichung mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS2", "g", innen="2", seite="3", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Verschiebung für einen Anschluss mit gleichem Funktionswert und gleicher Steigung beschreiben und Funktionsterm angeben", typ_neben="",
    stichwoerter="Wert und Änderungsrate bei 240 für f und g gleich|h_k(0) = 0 und h_k'(0) = f'(240) für k = 308/3125|Verschiebung um 240 in positive x-Richtung und um f(240) in positive y-Richtung|g(x) = h_k(x − 240) + f(240)",
    voraussetzungen="Bedingung in g(240) = f(240) und g'(240) = f'(240) übersetzen|Verschiebung in x- und y-Richtung am Term|h_k(0) = 0 erkennen",
    format="Kurzantwort", operator="Beschreiben Sie|geben Sie an", antwort="Text|Term",
    material="keins", skizze="keine", kontext="Medizin/Glukosewert", textumfang="mittel",
    gegeben=GLUK + H_K + "; für k = 308/3125 stimmt h_k'(0) mit f'(240) überein; die Bedingung für g lässt sich erfüllen, wenn der Graph von g durch eine geeignete Verschiebung aus dem Graphen von h_k für k = 308/3125 hervorgeht",
    gesucht="Beschreibung dieser Verschiebung und ein Funktionsterm von g",
    verfahren="Wegen h_k(0) = 0 und h_k'(0) = f'(240) den Graphen um 240 nach rechts und um f(240) nach oben verschieben; dann gilt g(240) = f(240) und g'(240) = f'(240)",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="2018MerhoehtBAnalysisCAS2-2f",
    ergebnis="Der Graph von g geht aus dem Graphen von h_k mit k = 308/3125 durch eine Verschiebung um 240 in positive x-Richtung und um f(240) in positive y-Richtung hervor; g(x) = h_k(x − 240) + f(240) mit k = 308/3125 (amtlich)",
    zwischenergebnis="f(240) = 2732/25 = 109,28|g(240) = 109,28 und g'(240) = −4,928",
    niveau_geschaetzt="III", fehlerquelle="um 240 nach links verschieben (h_k(x + 240)) oder die Verschiebung in y-Richtung vergessen",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (g(240) = f(240) = 2732/25, g'(240) = f'(240) = −616/125). Erste Schätzung: II; korrigiert nach Deutungsliste (a): die Bedingung „unabhängig davon, ob mit f oder g ermittelt“ ist erst in g(240) = f(240) und g'(240) = f'(240) zu übersetzen; die Ausnahme „in einer vorigen Teilaufgabe“ gehört zu (b), nicht zu (a). Neuer Typ: vorhandene Transformationstypen beschreiben oder beurteilen eine Verschiebung am Term, keiner wählt sie für einen Anschluss mit gleichem Wert und gleicher Steigung. CAS-Anteil: keiner.")
# ---- Analysis CAS 3 (Aufgabe 1: Wurzelschar f_k(x) = √(k · x^2 + 400), 27 BE; Aufgabe 2: Hängebrücke, 23 BE)
WURZ = "Für k ∈ IR+ ist die Schar der in IR definierten Funktionen f_k mit f_k(x) = √(k · x^2 + 400) gegeben"
GFUN = "; zusätzlich ist die in IR definierte Funktion g mit g(x) = 1/10 · x^2 + 20 gegeben"
MITTEL = ("; die mittlere Abweichung der Funktionswerte von f_5 und g in einem Intervall a <= x <= b kann mit dem Term "
          "1/(b − a) · ∫ von a bis b |f_5(x) − g(x)| dx berechnet werden")
BRUECKE = ("Hängebrücke (Abbildung 1, schematisch) im Koordinatensystem mit 1 LE = 1 m, Materialstärken vernachlässigt: zwei "
           "vertikale Pfeiler bei x = −250 und x = 250 (Länge der Brücke 500 m), waagerechte Fahrbahn 12 m über der x-Achse "
           "(y = 12), das Drahtseil ist an den Pfeilern in 72,8 m Höhe über der x-Achse befestigt (Befestigungspunkte "
           "(−250; 72,8) und (250; 72,8)) und hängt symmetrisch zur y-Achse durch; gegeben sind die in IR definierten "
           "Funktionen g_r mit g_r(x) = r · x^2 + 20, r ∈ IR")
BR_SK = ("Abbildung 1: Koordinatensystem, x-Achse strichpunktiert auf Höhe der Wasseroberfläche, y-Achse strichpunktiert in "
         "der Brückenmitte; links und rechts je ein vertikaler Pfeiler (dicke Linie), Abstand 500 m (Bemaßung „500 m, Länge "
         "der Brücke“); waagerechte Fahrbahn 12 m über der x-Achse (Bemaßung 12 m), darunter grau das Wasser; das Drahtseil "
         "hängt als nach oben geöffneter Bogen von den oberen Pfeilerenden (Bemaßung 72,8 m über der x-Achse) bis knapp über "
         "die Fahrbahn in der Mitte; senkrechte Hänger verbinden Seil und Fahrbahn; Beschriftungen vertikaler Pfeiler, "
         "Drahtseil, Fahrbahn, Wasser, Abb. 1")
HST = ("; ein zwischen den Befestigungspunkten unbelastet hängendes Drahtseil könnte mit einer der in IR definierten Funktionen "
       "h_s,t mit h_s,t(x) = s/2 · (e^(x/s) + e^(−x/s)) + t, s ∈ IR mit s ≠ 0, t ∈ IR, beschrieben werden (Hinweis: "
       "1/2 · (e^x + e^(−x)) heißt in einigen CAS cosh(x), 1/2 · (e^x − e^(−x)) heißt sinh(x))")
ABB2_SK = ("Abbildung 2: Koordinatenachsen ohne Skalierung mit drei zur y-Achse symmetrischen Graphen von h_s,t mit gleichem t: "
           "I (durchgezogen) nach oben geöffnet und schmal, Tiefpunkt knapp oberhalb der x-Achse; II (gestrichelt) nach oben "
           "geöffnet und breiter, Tiefpunkt höher als der von I; III (strichpunktiert) nach unten geöffnet, Hochpunkt unterhalb "
           "der x-Achse")
LAENGE = ("; das belastete Drahtseil ist 514,5 m lang, das unbelastete soll die gleiche Länge haben; die Länge des Graphen von "
          "h_s,t zwischen (−v; h_s,t(−v)) und (v; h_s,t(v)) mit v ∈ IR+ ist s · (e^(v/s) − e^(−v/s))")
row("2018MerhoehtBAnalysisCAS3", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen einer Funktion in ein Koordinatensystem einzeichnen",
    typ_neben="Symmetrie: Symmetrieart am Term über die Exponenten begründen",
    stichwoerter="Graph von f_5 mit Tiefpunkt (0; 20)|symmetrisch zur y-Achse|f_k(−x) = f_k(x) für alle k",
    voraussetzungen="Wertetabelle einer Wurzelfunktion|Achsensymmetrie über f(−x) = f(x)",
    format="Zeichnen|Begründung", operator="Skizzieren Sie|geben Sie an|Begründen Sie", antwort="Grafik|Text",
    material="Koordinatensystem",
    skizze=("Zu erstellende Skizze (nach dem Erwartungshorizont): Koordinatensystem mit x von −30 bis 30 und y von 0 bis 70, "
            "Gitter; Graph von f_5 symmetrisch zur y-Achse mit Tiefpunkt (0; 20), durch (±10; 30), (±20; 49) und (±30; 70), "
            "für große |x| fast geradlinig ansteigend"),
    kontext="ohne", textumfang="kurz",
    gegeben=WURZ + "; f_5(x) = √(5x^2 + 400)",
    gesucht="Skizze des Graphen von f_5 und dessen Symmetrie; Begründung, dass der Graph von f_k für jedes k dieselbe Symmetrie hat",
    verfahren="Wertetabelle von f_5 und Graph skizzieren; x kommt im Term nur als x^2 vor, also f_k(−x) = f_k(x) für alle x und alle k",
    schritte="2", zahlenraum="Wurzel|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Skizze des Graphen von f_5 (Tiefpunkt (0; 20), durch (±30; 70)); der Graph von f_5 ist symmetrisch bezüglich der y-Achse; für alle x ∈ IR gilt f_k(−x) = f_k(x), jeder Graph von f_k ist also ebenfalls achsensymmetrisch zur y-Achse (amtlich)",
    zwischenergebnis="f_5(0) = 20|f_5(±10) = 30|f_5(±30) = 70",
    niveau_geschaetzt="I", fehlerquelle="die Symmetrie nur am Graphen von f_5 ablesen und für f_k nicht allgemein begründen",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (f_k(−x) − f_k(x) = 0; Punkte der Skizze eigene Rechnung). skizze beschreibt die zu erstellende Skizze nach dem Erwartungshorizont. Typ und Nebentyp wiederverwendet; die Definition des Nebentyps deckt den Weg über f_k(−x) = f_k(x). CAS-Anteil: Graph mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS3", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Vorzeichen aller Funktionswerte einer Schar am Term begründen", typ_neben="",
    stichwoerter="k · x^2 >= 0|Radikand k · x^2 + 400 > 0|f_k(x) > 0, keine Nullstellen",
    voraussetzungen="Quadrat nicht negativ|Wurzel aus einer positiven Zahl ist positiv",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=WURZ,
    gesucht="Begründung anhand des Funktionsterms, dass f_k keine Nullstellen hat",
    verfahren="Für k > 0 ist k · x^2 >= 0, der Radikand also mindestens 400 und die Wurzel positiv",
    schritte="1", zahlenraum="Wurzel|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Für alle x ∈ IR gilt k · x^2 >= 0 und damit k · x^2 + 400 > 0, d. h. f_k(x) > 0; f_k hat keine Nullstellen (amtlich)",
    zwischenergebnis="f_k(x) >= 20",
    niveau_geschaetzt="I", fehlerquelle="nur zeigen, dass der Radikand nicht negativ ist, ohne ihn von null abzugrenzen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS3", "c", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Extrempunkte einer Schar mit Art in Abhängigkeit vom Parameter bestimmen", typ_neben="",
    stichwoerter="Extremstelle x = 0 wegen der Symmetrie|f_k(0) = 20, f_k(x) > 20 für x ≠ 0|Tiefpunkt (0; 20) für alle k",
    voraussetzungen="Kettenregel für Wurzelfunktionen|Extremstelle über f' = 0 oder über Symmetrie und Wertevergleich",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=WURZ + "; der Graph von f_k ist symmetrisch zur y-Achse",
    gesucht="Koordinaten und Art des Extrempunkts des Graphen von f_k",
    verfahren="f_k'(x) = k · x/√(k · x^2 + 400) = 0 nur für x = 0, f_k''(0) = k/20 > 0; oder wie im Erwartungshorizont: wegen der Symmetrie liegt der Extrempunkt bei x = 0, und f_k(x) > 20 = f_k(0) für x ≠ 0",
    schritte="3", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="2018MerhoehtBAnalysisCAS3-1a",
    ergebnis="Wegen der Symmetrie hat der Extrempunkt die x-Koordinate 0; mit f_k(0) = 20 und f_k(x) > 20 für alle x ≠ 0 besitzt der Graph von f_k den Tiefpunkt (0; 20) (amtlich)",
    zwischenergebnis="f_k'(x) = k · x/√(k · x^2 + 400)|f_k''(0) = k/20",
    niveau_geschaetzt="II", fehlerquelle="die Art nicht begründen oder den Tiefpunkt vom Parameter abhängig angeben",
    bemerkung="Standardbezug: K1 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (f_k' = 0 nur für x = 0, f_k''(0) = k/20 > 0). Typ wiederverwendet; der Erwartungshorizont argumentiert ohne Ableitung über Symmetrie und Wertevergleich, die Typdefinition nennt den Weg über die Ableitungen, und der Tiefpunkt hängt hier nicht vom Parameter ab. CAS-Anteil: Ableitungen mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS3", "d", innen="1", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Stellen, deren Tangente die y-Achse oberhalb einer Schranke schneidet, über eine Ungleichung bestimmen", typ_neben="",
    stichwoerter="Tangente an f_5 in (c; f_5(c))|y-Achsenabschnitt 80√5/√(c^2 + 80)|Ungleichung > 10|−4√15 < c < 4√15",
    voraussetzungen="Tangentengleichung mit allgemeiner Stelle|Wurzelungleichung umformen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=WURZ + "; f_5(x) = √(5x^2 + 400); Tangente an den Graphen von f_5 im Punkt (c; f_5(c)), c ∈ IR",
    gesucht="alle c, für die diese Tangente die y-Achse in einem Punkt mit einer y-Koordinate größer als 10 schneidet",
    verfahren="Tangente y = f_5'(c) · (x − c) + f_5(c) an x = 0 auswerten: f_5(c) − c · f_5'(c) = 400/√(5c^2 + 400) = 80√5/√(c^2 + 80); die Ungleichung > 10 führt auf c^2 < 240",
    schritte="3", zahlenraum="Wurzel|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="y-Koordinate des Schnittpunkts der Tangente mit der y-Achse: 80√5/√(c^2 + 80); 80√5/√(c^2 + 80) > 10 ⇔ −4√15 < c < 4√15 (amtlich)",
    zwischenergebnis="f_5'(c) = 5c/√(5c^2 + 400)|c^2 < 240|4√15 ≈ 15,49",
    niveau_geschaetzt="II", fehlerquelle="die Ungleichung beim Quadrieren oder Kehrwertbilden falsch herum umformen und |c| > 4√15 angeben",
    bemerkung="Standardbezug: K1 II, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (offenes Intervall von −4√15 bis 4√15, 4√15 ≈ 15,49). Schätzung II (y-Achsenabschnitt der Tangente als Term, Ungleichung lösen – Verkettung); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: vorhandene Tangententypen weisen eine Aussage über den y-Achsenabschnitt für alle Stellen nach oder bestimmen Berührpunkte aus Steigung oder äußerem Punkt; hier werden die Stellen über eine Ungleichung für den Achsenabschnitt bestimmt. CAS-Anteil: Tangente und Ungleichung mit dem Rechner, Ansatz eigen.")
row("2018MerhoehtBAnalysisCAS3", "e", innen="1", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="y-Achsenabschnitt der Tangente allgemein nachweisen", typ_neben="",
    stichwoerter="Tangente in (x0; f_k(x0)) durch den Ursprung|f_k'(x0) · x0 = f_k(x0)|y-Achsenabschnitt 400/√(k · x0^2 + 400) > 0|keine Lösung",
    voraussetzungen="Tangentengleichung mit allgemeiner Stelle und Parameter|Ursprung als Punktprobe|Gleichung ohne Lösung erkennen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=WURZ,
    gesucht="Nachweis, dass für jeden Wert von k keine Tangente an den Graphen von f_k durch den Koordinatenursprung verläuft",
    verfahren="Die Tangente in (x0; f_k(x0)) geht genau dann durch den Ursprung, wenn f_k'(x0) · x0 = f_k(x0); das führt auf k · x0^2 = k · x0^2 + 400, also auf keine Lösung (gleichwertig: der y-Achsenabschnitt 400/√(k · x0^2 + 400) ist stets positiv)",
    schritte="3", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="",
    ergebnis="Würde die Tangente an den Graphen von f_k im Punkt (x0; f_k(x0)) durch den Koordinatenursprung verlaufen, müsste f_k'(x0) · x0 = f_k(x0) gelten; diese Gleichung hat jedoch keine Lösung (amtlich)",
    zwischenergebnis="f_k(x0) − x0 · f_k'(x0) = 400/√(k · x0^2 + 400)",
    niveau_geschaetzt="III", fehlerquelle="nur für einzelne Werte von k oder einzelne Stellen prüfen statt allgemein",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Gleichung ohne Lösung, y-Achsenabschnitt 400/√(k · x0^2 + 400) > 0). Schätzung III nach Deutungsliste (c): allgemeiner Nachweis für alle k und alle Stellen, bei dem eine Beziehung hergeleitet wird. Typ wiederverwendet. CAS-Anteil: Tangententerm mit dem Rechner möglich, Nachweis eigen.")
row("2018MerhoehtBAnalysisCAS3", "f", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameterwerte für mehr als einen gemeinsamen Punkt zweier Graphen über die Lösbarkeit der Schnittgleichung bestimmen", typ_neben="",
    stichwoerter="f_k(x) = g(x)|x^2 · (k − 4 − x^2/100) = 0|x = 0 oder x = ±10√(k − 4)|k > 4",
    voraussetzungen="Wurzelgleichung durch Quadrieren lösen (g > 0)|Ausklammern|Lösbarkeit von x^2 = Term im Parameter",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=WURZ + GFUN,
    gesucht="alle k, für die der Graph von f_k und der Graph von g mehr als einen gemeinsamen Punkt haben",
    verfahren="f_k(x) = g(x) quadrieren (g(x) > 0): k · x^2 + 400 = (x^2/10 + 20)^2 ⇔ x^2 · (k − 4 − x^2/100) = 0; neben x = 0 gibt es genau für k > 4 die weiteren Lösungen x = ±10√(k − 4)",
    schritte="3", zahlenraum="Wurzel|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f_k(x) = g(x) ⇔ x = −10√(k − 4) ∨ x = 0 ∨ x = 10√(k − 4); nur für k > 4 nehmen −10√(k − 4) und 10√(k − 4) Werte ungleich null an, die Graphen haben dann mehr als einen gemeinsamen Punkt (amtlich)",
    zwischenergebnis="gemeinsamer Punkt (0; 20) für alle k|für k = 4 nur x = 0",
    niveau_geschaetzt="III", fehlerquelle="k = 4 mitzählen, obwohl dann nur der Punkt (0; 20) gemeinsam ist",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Lösungen 0 und ±10√(k − 4)). Schätzung III (Bedingung k > 4 erst gefunden, zwei Fälle mit verschiedenem Ausgang – Nullfall-Regel: zählt); amtlich II – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: vorhandene Typen bestimmen gemeinsame Punkte aller Graphen einer Schar oder die Anzahl der Nullstellen nach dem Parameter; hier entscheidet die Lösbarkeit der Schnittgleichung mit einem festen Graphen. CAS-Anteil: Schnittgleichung mit dem Rechner lösen, Deutung eigen.")
row("2018MerhoehtBAnalysisCAS3", "g", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Mittelwert einer Funktion als Integral geteilt durch die Intervalllänge berechnen und deuten", typ_neben="",
    stichwoerter="mittlere Abweichung von f_5 und g|1/15 · ∫ von 0 bis 15 |f_5(x) − g(x)| dx|etwa 0,65",
    voraussetzungen="vorgegebenen Integralterm auswerten|Integral mit Betrag numerisch berechnen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=WURZ + GFUN + MITTEL,
    gesucht="die mittlere Abweichung der Funktionswerte von f_5 und g im Intervall 0 <= x <= 15",
    verfahren="Den vorgegebenen Term mit a = 0 und b = 15 mit dem Rechner auswerten",
    schritte="1", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="1/15 · ∫ von 0 bis 15 |f_5(x) − g(x)| dx ≈ 0,65 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I", fehlerquelle="den Betrag weglassen, sodass sich positive und negative Abweichungen teilweise aufheben",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,654). Schätzung I: mittlere Abweichung mit dem Rechner, eine Rechnung. Typ wiederverwendet; Term und Deutung sind vorgegeben, berechnet wird numerisch statt über eine Stammfunktion. CAS-Anteil: Integral mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS3", "h", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Gewichtetes Mittel zweier Teilintegrale als Mittelwert über die Vorzeichenbereiche der Differenz begründen", typ_neben="",
    stichwoerter="f_5(x) − g(x) >= 0 für 0 <= x <= 10, <= 0 für 10 <= x <= 15|Teilmittelwerte auf [0; 10] und [10; 15]|Gewichte 2/3 und 1/3 als Anteile der Intervalllängen",
    voraussetzungen="Schnittstelle zweier Graphen|Betrag abschnittsweise auflösen|gewichtetes Mittel",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=WURZ + GFUN + MITTEL + "; die mittlere Abweichung auf 0 <= x <= 15 könnte auch mit dem Term 2/3 · 1/10 · ∫ von 0 bis 10 (f_5(x) − g(x)) dx + 1/3 · 1/5 · ∫ von 10 bis 15 (g(x) − f_5(x)) dx berechnet werden",
    gesucht="ein sinnvoller Gedankengang, mit dem man zu diesem Term gelangt",
    verfahren="Die Graphen schneiden sich bei x = 10; links davon ist f_5 − g >= 0, rechts <= 0, der Betrag wird abschnittsweise aufgelöst; die beiden Integralterme sind die mittleren Abweichungen auf den Teilintervallen, gewichtet mit 10/15 und 5/15",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Es gilt f_5(x) − g(x) >= 0 für 0 <= x <= 10 und f_5(x) − g(x) <= 0 für 10 <= x <= 15; damit sind 1/10 · ∫ von 0 bis 10 (f_5(x) − g(x)) dx und 1/5 · ∫ von 10 bis 15 (g(x) − f_5(x)) dx die mittleren Abweichungen in den Intervallen [0; 10] bzw. [10; 15]; jede wird entsprechend der Länge ihres Intervalls gewichtet (amtlich)",
    zwischenergebnis="f_5(10) = g(10) = 30|Teilmittelwerte etwa 0,275 und 1,412|gewichtet 0,654",
    niveau_geschaetzt="III", fehlerquelle="die Gewichte 2/3 und 1/3 nicht auf die Intervalllängen zurückführen oder den Vorzeichenwechsel bei x = 10 übersehen",
    bemerkung="Standardbezug: K1 III, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Schnittstelle x = 10, gewichtetes Mittel 0,654 wie in g). Schätzung III nach Deutungsliste (d): zwei Deutungen verkettet (Vorzeichenbereiche der Differenz statt Betrag, Gewichte als Anteile der Intervalllängen). Neuer Typ: der vorhandene Mittelwerttyp berechnet und deutet einen Integralmittelwert; hier wird ein zusammengesetzter Term als gewichtetes Mittel zweier Teilmittelwerte begründet. CAS-Anteil: Schnittstelle mit dem Rechner, Gedankengang eigen.")
row("2018MerhoehtBAnalysisCAS3", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben", typ_neben="",
    stichwoerter="Befestigungspunkte (±250; 72,8)|Symmetrie: ein Punkt genügt|g_r(250) = 72,8|r = 0,0008448",
    voraussetzungen="Werte aus der Abbildung in Koordinaten übersetzen|Punktprobe|lineare Gleichung lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=BR_SK, kontext="Bauwesen/Hängebrücke", textumfang="mittel",
    gegeben=BRUECKE + "; zur Kontrolle: r = 0,0008448",
    gesucht="der Wert von r, für den der Graph von g_r den Verlauf des Drahtseils bezüglich seiner beiden Befestigungspunkte an den Pfeilern beschreibt",
    verfahren="Wegen der Symmetrie genügt ein Befestigungspunkt: g_r(250) = 72,8 ⇔ 62500 · r = 52,8",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Wegen der Symmetrie des Graphen von g_r genügt es, einen der beiden Befestigungspunkte zu betrachten; g_r(250) = 72,8 liefert r = 0,0008448 (amtlich)",
    zwischenergebnis="62500 · r = 52,8",
    niveau_geschaetzt="I", fehlerquelle="die Höhe über der Fahrbahn (60,8) statt über der x-Achse einsetzen oder x = 500 statt 250 nehmen",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (r = 66/78125 = 0,0008448). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS3", "b", innen="2", seite="2", punkte="6", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph, x-Achse und waagerechter Gerade aus Rechteck und Integral berechnen", typ_neben="",
    stichwoerter="Planen von der Fahrbahn (y = 12) bis 25 m darüber (y = 37)|g(x) = 37 bei x ≈ ±141,86|zwei Rechtecke 25 · (250 − x2)|∫ von x1 bis x2 (g(x) − 12) dx|etwa 9285 m^2",
    voraussetzungen="Fläche abschnittsweise zerlegen|Schnittstellen mit einer waagerechten Geraden|Integral der Differenz zur Fahrbahn",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=BR_SK, kontext="Bauwesen/Hängebrücke", textumfang="mittel",
    gegeben=BRUECKE + "; das Drahtseil wird durch g_0,0008448(x) = 0,0008448 · x^2 + 20 beschrieben; auf einer Seite der Fahrbahn ist der Bereich zwischen Fahrbahn und Drahtseil über die gesamte Länge der Brücke bis zu einer Höhe von 25 m über der Fahrbahn mit bedruckten Kunststoffplanen bespannt",
    gesucht="Inhalt der bespannten Fläche",
    verfahren="g_0,0008448(x) = 12 + 25 liefert x1 < x2; außerhalb von x1 <= x <= x2 reichen die Planen bis zur Höhe 25 m (zwei Rechtecke), dazwischen bis zum Seil: 2 · (250 − x2) · 25 + ∫ von x1 bis x2 (g_0,0008448(x) − 12) dx",
    schritte="4", zahlenraum="dezimal", einheiten="m^2", abhaengig_von="2018MerhoehtBAnalysisCAS3-2a",
    ergebnis="Mit den Lösungen x1 und x2 (x1 < x2) der Gleichung g_0,0008448(x) = 12 + 25 ergibt sich 2 · (250 − x2) · 25 + ∫ von x1 bis x2 (g_0,0008448(x) − 12) dx ≈ 9285; der Inhalt der bespannten Fläche beträgt etwa 9285 m^2 (amtlich)",
    zwischenergebnis="x1,2 ≈ ±141,86|Rechtecke zusammen etwa 5407 m^2|Integral etwa 3877 m^2",
    niveau_geschaetzt="II", fehlerquelle="bis zur x-Achse statt bis zur Fahrbahn integrieren oder die Begrenzung auf 25 m Höhe übersehen",
    bemerkung="Standardbezug: K3 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (9284,6). Erste Schätzung: III; korrigiert nach der Ausnahme zu Deutungsliste (a): „bis zu einer Höhe von 25 m über der Fahrbahn“ gibt die obere Grenze y = 37 wörtlich vor. Typ wiederverwendet; die untere Grenze ist hier die Fahrbahn y = 12, nicht die x-Achse – der Typname passt erst nach Verschiebung um 12 (Vorschlag für den Abgleich: „x-Achse“ im Namen durch eine allgemeine waagerechte Grundlinie ersetzen). CAS-Anteil: Gleichung und Integral mit dem Rechner, Zerlegung eigen.")
row("2018MerhoehtBAnalysisCAS3", "c", innen="2", seite="3", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter den Graphen über den y-Achsenabschnitt zuordnen", typ_neben="",
    stichwoerter="drei Graphen von h_s,t mit gleichem t|h_s,t(0) = s + t|y-Achsenabschnitt wächst mit s|Reihenfolge III, I, II",
    voraussetzungen="Funktionswert an der Stelle 0|Graphen am y-Achsenabschnitt vergleichen",
    format="Kurzantwort|Begründung", operator="Ordnen Sie|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=ABB2_SK, kontext="Bauwesen/Hängebrücke", textumfang="kurz",
    gegeben=BRUECKE + HST + "; Abbildung 2 zeigt die Graphen I, II und III dreier Funktionen h_s,t, die sich nur im Wert von s unterscheiden",
    gesucht="Reihenfolge der Graphen nach der Größe von s, beginnend mit dem kleinsten, mit Begründung",
    verfahren="h_s,t(0) = s + t; bei gleichem t ist der y-Achsenabschnitt umso größer, je größer s ist; III schneidet die y-Achse am tiefsten, II am höchsten",
    schritte="2", zahlenraum="negativ", einheiten="", abhaengig_von="",
    ergebnis="Reihenfolge III, I, II; Begründung: h_s,t(0) = s + t, d. h. die y-Koordinate des Schnittpunkts des Graphen von h_s,t mit der y-Achse wird mit zunehmendem Wert von s größer (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II", fehlerquelle="nach der Öffnungsweite ordnen und die Lage des Graphen III mit negativem s übersehen",
    bemerkung="Standardbezug: K1 II, K4 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (h_s,t(0) = s + t). Typ wiederverwendet; der Erwartungshorizont ordnet über den y-Achsenabschnitt s + t, der Typ passt (die im ersten Versuch notierte Zuordnung über Öffnung nach dem Vorzeichen und Weite nach dem Betrag ist ein gleichwertiger zweiter Weg). CAS-Anteil: keiner.")
row("2018MerhoehtBAnalysisCAS3", "d", innen="2", seite="3", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Krümmungsverhalten aus der zweiten Ableitung deuten", typ_neben="",
    stichwoerter="durchhängendes Seil linksgekrümmt|h_s,t''(x) = (e^(x/s) + e^(−x/s))/(2s)|> 0 ⇔ s > 0",
    voraussetzungen="Linkskrümmung über f'' > 0|zweite Ableitung einer e-Funktion mit Parameter|Vorzeichen eines Bruchs",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Skizze", skizze=BR_SK, kontext="Bauwesen/Hängebrücke", textumfang="kurz",
    gegeben=BRUECKE + HST,
    gesucht="ob s für die Funktion h_s,t, die das unbelastete Drahtseil beschreiben könnte, positiv oder negativ ist, mit Begründung",
    verfahren="Das durchhängende Seil verlangt einen linksgekrümmten Graphen; h_s,t''(x) = (e^(x/s) + e^(−x/s))/(2s) hat einen positiven Zähler, ist also genau für s > 0 positiv",
    schritte="2", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="s ist positiv: damit h_s,t das unbelastete Drahtseil beschreiben kann, muss der zugehörige Graph linksgekrümmt sein; h_s,t''(x) = (e^(x/s) + e^(−x/s))/(2s) > 0 ⇔ s > 0 (amtlich)",
    zwischenergebnis="h_s,t'(x) = 1/2 · (e^(x/s) − e^(−x/s))",
    niveau_geschaetzt="II", fehlerquelle="beim Ableiten den inneren Faktor 1/s vergessen und das Vorzeichen von s nicht aus der Krümmung erschließen",
    bemerkung="Standardbezug: K1 II, K3 I, K4 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (h'' = cosh(x/s)/s). Typ wiederverwendet; hier wird umgekehrt aus der geforderten Linkskrümmung auf das Vorzeichen des Parameters geschlossen. CAS-Anteil: zweite Ableitung mit dem Rechner.")
row("2018MerhoehtBAnalysisCAS3", "e", innen="2", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Zwei Parameter einer Funktion aus einer vorgegebenen Bogenlängenformel und einem Punkt bestimmen", typ_neben="",
    stichwoerter="Seillänge 514,5 m|s · (e^(250/s) − e^(−250/s)) = 514,5|s ≈ 601,9|h_s,t(250) = 72,8 liefert t ≈ −581,8",
    voraussetzungen="Formel mit v = 250 belegen|transzendente Gleichung mit dem Rechner lösen|Punktprobe für t",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=BR_SK, kontext="Bauwesen/Hängebrücke", textumfang="mittel",
    gegeben=BRUECKE + HST + LAENGE + "; für das unbelastete Seil ist s > 0; zur Kontrolle: s ≈ 601,9, t ≈ −581,8",
    gesucht="die Werte von s und t für die Funktion h_s,t, die das unbelastete Drahtseil beschreiben könnte",
    verfahren="Mit v = 250: s · (e^(250/s) − e^(−250/s)) = 514,5 mit dem Rechner nach s > 0 lösen; dann h_s,t(250) = 72,8 nach t auflösen",
    schritte="3", zahlenraum="dezimal|negativ|Potenz", einheiten="", abhaengig_von="2018MerhoehtBAnalysisCAS3-2d",
    ergebnis="s · (e^(250/s) − e^(−250/s)) = 514,5 liefert für s ∈ IR+: s ≈ 601,9; mit h_s,t(250) = 72,8 erhält man t ≈ −581,8 (amtlich)",
    zwischenergebnis="s/2 · (e^(250/s) + e^(−250/s)) ≈ 654,6",
    niveau_geschaetzt="II", fehlerquelle="die halbe Brückenlänge nicht als v einsetzen (v = 500) oder t vor s bestimmen wollen",
    bemerkung="Standardbezug: K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (s ≈ 601,92, t ≈ −581,79; die Längenformel folgt aus ∫ von −v bis v √(1 + (h_s,t'(x))^2) dx). Neuer Typ: vorhandene Rekonstruktionstypen setzen Punkt- und Steigungsbedingungen an, der Bogenlängentyp berechnet eine Länge; hier bestimmt eine vorgegebene Längenformel den einen Parameter und ein Punkt den zweiten. CAS-Anteil: transzendente Gleichung mit dem Rechner lösen, Ansatz eigen.")
row("2018MerhoehtBAnalysisCAS3", "f", innen="2", seite="3", punkte="4", afb_amtlich="I|II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Lage zweier Graphen mit gemeinsamen Endpunkten über die Steigungen in den Endpunkten begründen", typ_neben="",
    stichwoerter="g'(±250) ≈ ±0,422|h'(±250) ≈ ±0,427|unbelastetes Seil fällt steiler ab, nahe den Pfeilern unterhalb|h(0) ≈ 20,13 > g(0) = 20, in der Mitte oberhalb",
    voraussetzungen="Ableitungen an den Befestigungspunkten|Steigungsvergleich an einem gemeinsamen Punkt als Lagevergleich deuten|Funktionswerte vergleichen",
    format="Rechnung|Begründung", operator="Bestimmen Sie|Begründen Sie", antwort="Zahl|Text",
    material="Skizze", skizze=BR_SK, kontext="Bauwesen/Hängebrücke", textumfang="mittel",
    gegeben=BRUECKE + HST + "; das belastete Drahtseil wird durch g_0,0008448(x) = 0,0008448 · x^2 + 20 beschrieben, das unbelastete durch h_601,9;−581,8; beide verlaufen durch die Befestigungspunkte (−250; 72,8) und (250; 72,8)",
    gesucht="Steigungen des belasteten und des unbelasteten Drahtseils in den beiden Befestigungspunkten; Begründung mithilfe dieser Steigungen, dass das unbelastete Seil nicht vollständig oberhalb oder unterhalb des belasteten verlaufen würde",
    verfahren="Beide Ableitungen bei x = ±250 berechnen; das unbelastete Seil fällt von den Befestigungspunkten aus steiler ab, liegt dort also unterhalb; wegen h(0) > g(0) liegt es in der Mitte oberhalb",
    schritte="4", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="2018MerhoehtBAnalysisCAS3-2a|2018MerhoehtBAnalysisCAS3-2e",
    ergebnis="g'_0,0008448(−250) ≈ −0,422, h'_601,9;−581,8(−250) ≈ −0,427, g'_0,0008448(250) ≈ 0,422, h'_601,9;−581,8(250) ≈ 0,427; das unbelastete Drahtseil fällt von beiden Befestigungspunkten aus steiler ab als das belastete, verläuft in unmittelbarer Nähe dieser Punkte also unterhalb; da außerdem h_601,9;−581,8(0) > g_0,0008448(0), verläuft es im Bereich seines tiefsten Punkts oberhalb des belasteten (amtlich)",
    zwischenergebnis="h_601,9;−581,8(0) ≈ 20,13|g_0,0008448(0) = 20",
    niveau_geschaetzt="III", fehlerquelle="nur die Steigungen vergleichen und den Wertevergleich in der Mitte weglassen, sodass nur die Lage nahe den Pfeilern begründet ist",
    bemerkung="Standardbezug: K1 III, K5 I, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (±0,4224 und ±0,4274; h(0) ≈ 20,13). Der Erwartungshorizont schreibt im Schluss g_0,000845 statt g_0,0008448 (Rundung, ohne Folgen). Schätzung III: Beziehung hergeleitet (aus den Steigungen an den gemeinsamen Endpunkten und dem Wertevergleich in der Mitte auf die Lage geschlossen), Symmetrie ausgenutzt. Neuer Typ: vorhandene Tangententypen vergleichen Steigungen an einem Punkt oder bestimmen Schnittwinkel; hier wird aus den Steigungen an gemeinsamen Endpunkten auf die gegenseitige Lage zweier Graphen geschlossen. CAS-Anteil: Ableitungen und Funktionswerte mit dem Rechner, Schluss eigen.")
# ---- AG/LA (A1) CAS 1: Baumärkte, 25 BE (eine Aufgabe, a bis h); Kontext und Matrix M wie 2018MgrundlegendBAGLAA1WTR,
# Aufgabenstellungen und Zahlen verschieden (keine Dateidublette, keine geteilte Teilaufgabe)
BAUM1 = ("Drei Baumärkte A, B, C in einer Stadt; das Übergangsdiagramm beschreibt das Wechselverhalten der Kunden von einem "
         "Monat zum nächsten zunächst so: A bleibt 0,3, A → B 0,5, A → C 0,2; B bleibt 0,5, B → A 0,4, B → C 0,1; C bleibt 0,5, "
         "C → A 0,2, C → B 0,3")
BAUM_SK = ("Übergangsdiagramm: drei Kreise A (oben), B (unten links) und C (unten rechts) im Dreieck; Schleifen an A mit 0,3, an B "
           "mit 0,5, an C mit 0,5; Doppelpfeile zwischen A und B (B → A 0,4, A → B 0,5), zwischen A und C (A → C 0,2, C → A 0,2) "
           "und zwischen B und C (B → C 0,1 oben, C → B 0,3 unten)")
BAUM2 = ("Drei Baumärkte A, B, C; nach Maßnahmen der Baumärkte A (Sortiment) und B (Kundenservice) wird die Verteilung der "
         "Kunden als Vektor (a; b; c) der Anzahlen dargestellt und entwickelt sich von einem Monat n zum nächsten nach "
         "M · v_n = v_(n+1) mit M = ((0,63; 0,18; 0,3), (0,27; 0,72; 0,45), (0,1; 0,1; 0,25))")
SOMMER = "; in einem auf die Maßnahmen folgenden Sommermonat hat A 3539, B 5281 und C 1180 Kunden"
RABATT = ("; Baumarkt C fürchtet, den notwendigen Anteil von 25 % der Kunden nicht zu erreichen, und führt Rabattaktionen "
          "durch; ab dem Monat, in dem sie beginnen, gilt N = ((0,63; 0,18; 0,4 · (1 − p)), (0,27; 0,72; 0,6 · (1 − p)), "
          "(0,1; 0,1; p)) mit 0 <= p <= 1")
row("2018MerhoehtBAGLAA1CAS1", "a", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Gleichungssystem für die Verteilung vor einem Übergang aufstellen", typ_neben="",
    stichwoerter="Übergangsmatrix aus dem Diagramm|0,3a + 0,4b + 0,2c = 3500 usw.|Vormonat a = 3400, b = 5800, c = 800",
    voraussetzungen="Übergangsdiagramm in eine Matrix übersetzen|lineares Gleichungssystem lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=BAUM_SK, kontext="Kundenwechsel/Baumärkte", textumfang="mittel",
    gegeben=BAUM1 + "; in einem Monat hat A 3500, B 4840 und C 1660 Kunden",
    gesucht="die Anzahlen der Kunden der drei Baumärkte im vorhergehenden Monat",
    verfahren="Aus dem Diagramm die Matrix mit den Spalten (0,3; 0,5; 0,2), (0,4; 0,5; 0,1), (0,2; 0,3; 0,5) bilden; das Gleichungssystem für den Vormonat aufstellen und lösen",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Das Gleichungssystem 0,3 · a + 0,4 · b + 0,2 · c = 3500, 0,5 · a + 0,5 · b + 0,3 · c = 4840, 0,2 · a + 0,1 · b + 0,5 · c = 1660 liefert a = 3400, b = 5800, c = 800 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II", fehlerquelle="die Matrix zeilen- statt spaltenweise aus dem Diagramm ablesen (Übergänge vertauscht)",
    bemerkung="Standardbezug: K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (3400; 5800; 800; Spaltensummen 1). Typ wiederverwendet, hier auch gelöst – die Typdefinition sagt „ohne es zu lösen“ (Vorschlag für den Abgleich: Definition um das Lösen erweitern oder einen eigenen Typ „… aufstellen und lösen“ bilden). CAS-Anteil: Gleichungssystem mit dem Rechner, Matrix aus dem Diagramm eigen.")
row("2018MerhoehtBAGLAA1CAS1", "b", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unmöglichkeit einer Verteilung über eine negative Vorgängerkomponente begründen", typ_neben="",
    stichwoerter="mit M^−1 zurückrechnen|(M^−1)^5 · v ≈ (−14466; −23189; 47654)|negative Kundenzahl nicht sinnvoll|höchstens vier Monate",
    voraussetzungen="inverse Matrix|Matrixpotenz als mehrfacher Rückschritt|negative Anzahl als Widerspruch deuten",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Kundenwechsel/Baumärkte", textumfang="mittel",
    gegeben=BAUM2 + SOMMER,
    gesucht="Nachweis, dass die Maßnahmen der Baumärkte A und B höchstens vier Monate zurückliegen",
    verfahren="Vom Sommermonat aus mit M^−1 zurückrechnen: vier Rückschritte liefern noch nichtnegative Anzahlen, der fünfte eine negative Komponente; das Modell mit M kann also nicht schon fünf Monate gegolten haben",
    schritte="3", zahlenraum="negativ|dezimal", einheiten="", abhaengig_von="",
    ergebnis="(M^−1)^5 · (3539; 5281; 1180) ≈ (−14466; −23189; 47654); ein negativer Wert für die Anzahl der Kunden eines Baumarkts ist im Sachzusammenhang nicht sinnvoll (amtlich)",
    zwischenergebnis="(M^−1)^4 · (3539; 5281; 1180) ≈ (1009; 843; 8148)",
    niveau_geschaetzt="II", fehlerquelle="mit M statt mit M^−1 rechnen, also vorwärts statt zurück",
    bemerkung="Standardbezug: K1 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt ((M^−1)^5 · v ≈ (−14465,6; −23188,7; 47654,3); (M^−1)^4 · v noch nichtnegativ). Erste Schätzung: III; korrigiert: kein Eintrag (a) bis (e) der Deutungsliste greift, die negative Anzahl als Widerspruch ist die einfache Deutung (derselbe Typ in 2026-ga-B-mms amtlich II). Typ wiederverwendet, hier fünf Schritte zurück. CAS-Anteil: Inverse und Matrixpotenz mit dem Rechner, Deutung eigen.")
row("2018MerhoehtBAGLAA1CAS1", "c", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Vorherige Verteilung über die inverse Matrix berechnen und prozentuale Abnahme einer Komponente angeben", typ_neben="",
    stichwoerter="M^−1 · (3539; 5281; 1180) ≈ (3544; 5256; 1200)|Gesamtzahl 10000|35,4 %, 52,6 %, 12 %",
    voraussetzungen="inverse Matrix|Anteil als Quotient an der Gesamtzahl",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kundenwechsel/Baumärkte", textumfang="kurz",
    gegeben=BAUM2 + SOMMER,
    gesucht="die prozentualen Anteile der Kunden der drei Baumärkte an der Gesamtzahl im Monat vor dem Sommermonat",
    verfahren="M^−1 · (3539; 5281; 1180) berechnen und jede Komponente durch die Gesamtzahl 10000 teilen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="%", abhaengig_von="",
    ergebnis="M^−1 · (3539; 5281; 1180) ≈ (3544; 5256; 1200); 3544/10000 ≈ 35,4 %, 5256/10000 ≈ 52,6 %, 1200/10000 = 12 % (amtlich)",
    zwischenergebnis="Summe der Komponenten 10000",
    niveau_geschaetzt="I", fehlerquelle="die Anteile des Sommermonats statt des Vormonats angeben",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (3544,4; 5255,6; 1200). Erste Schätzung: II; korrigiert nach der Grundregel: eine Rechnung mit der Inversen, Anteile nur Division (derselbe Typ in 2021-ga-B amtlich I). Typ wiederverwendet, hier prozentuale Anteile statt Abnahme und die Inverse mit dem Rechner statt gegeben. CAS-Anteil: Inverse und Produkt mit dem Rechner.")
row("2018MerhoehtBAGLAA1CAS1", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Einträge der Grenzmatrix im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="lim M^n für n → ∞|gleiche Spalten (0,3529; 0,5294; 0,1176)|langfristig A 35,3 %, B 52,9 %, C 11,8 %",
    voraussetzungen="Grenzmatrix mit dem Rechner|gleiche Spalten als langfristige Verteilung deuten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kundenwechsel/Baumärkte", textumfang="mittel",
    gegeben=BAUM2 + "; das Wechselverhalten der Kunden bleibt konstant",
    gesucht="wie sich die prozentualen Anteile der Kunden der drei Baumärkte nach den Maßnahmen langfristig entwickeln würden",
    verfahren="M^n für großes n mit dem Rechner berechnen (oder den Fixvektor mit Summe 1 bestimmen); die gleichen Spalten geben die langfristigen Anteile",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="%", abhaengig_von="",
    ergebnis="lim M^n für n → ∞ ≈ ((0,3529; 0,3529; 0,3529), (0,5294; 0,5294; 0,5294), (0,1176; 0,1176; 0,1176)); der Anteil der Kunden von A läge langfristig bei etwa 35,3 %, von B bei etwa 52,9 % und von C bei etwa 11,8 % (amtlich)",
    zwischenergebnis="exakt 6/17, 9/17 und 2/17",
    niveau_geschaetzt="II", fehlerquelle="eine Zeile statt einer Spalte der Grenzmatrix als Verteilung lesen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Fixvektor (6/17; 9/17; 2/17) ≈ (0,3529; 0,5294; 0,1176), M^200 gleich). Typ wiederverwendet, hier die Grenzmatrix erst mit dem Rechner ermittelt. CAS-Anteil: Matrixpotenz bzw. Grenzwert mit dem Rechner, Deutung eigen.")
row("2018MerhoehtBAGLAA1CAS1", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zustand mit dem kleinsten Wechselanteil aus der Matrix ablesen", typ_neben="",
    stichwoerter="Diagonale 0,63, 0,72, 0,25|größter Bleibeanteil bei B|Wechselanteil 1 − 0,72 = 28 %",
    voraussetzungen="Diagonaleinträge als Bleibeanteile|Wechselanteil als Komplement",
    format="Kurzantwort", operator="Geben Sie an|Nennen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Kundenwechsel/Baumärkte", textumfang="kurz",
    gegeben=BAUM2,
    gesucht="der Baumarkt, bei dem der Anteil der Kunden, die nach Beginn der Maßnahmen von einem Monat zum nächsten zu einem anderen Baumarkt wechseln, am kleinsten ist, und dieser Anteil",
    verfahren="Den größten Diagonaleintrag von M suchen (0,72 bei B); der Wechselanteil ist 1 − 0,72",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="%", abhaengig_von="",
    ergebnis="Baumarkt B; Anteil 28 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I", fehlerquelle="den Bleibeanteil 72 % statt des Wechselanteils nennen",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (1 − 0,72 = 0,28). Typ wiederverwendet (wie 2018MgrundlegendBAGLAA1WTR, Teilaufgabe 1 e, mit derselben Matrix). CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA1CAS1", "f", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixparameter aus einer Komponente nach einem Schritt bestimmen", typ_neben="",
    stichwoerter="erste Zeile von N|0,63 · 3400 + 0,18 · 5200 + 0,4 · (1 − p) · 1400 = 3022|p = 1,1 liegt nicht in [0; 1]|nicht im Einklang mit dem Modell",
    voraussetzungen="eine Komponente eines Matrix-Vektor-Produkts|lineare Gleichung lösen|Parameterbereich prüfen",
    format="Rechnung|Begründung", operator="Untersuchen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Kundenwechsel/Baumärkte", textumfang="mittel",
    gegeben=BAUM2 + RABATT + "; in einem Monat nach Beginn der Aktionen hat A 3400, B 5200 und C 1400 Kunden, im folgenden Monat hat A 3022 Kunden",
    gesucht="ob diese Kundenzahl mit dem Modell mit der Matrix N in Einklang steht",
    verfahren="Die erste Komponente von N · (3400; 5200; 1400) gleich 3022 setzen, nach p auflösen und mit dem Bereich 0 <= p <= 1 vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,63 · 3400 + 0,18 · 5200 + 0,4 · (1 − p) · 1400 = 3022 ⇔ p = 1,1; da 1,1 nicht in [0; 1] liegt, steht die Kundenzahl nicht im Einklang mit dem Modell (amtlich)",
    zwischenergebnis="560 · (1 − p) = −56",
    niveau_geschaetzt="II", fehlerquelle="p = 1,1 als Lösung annehmen, ohne den Bereich des Parameters zu prüfen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (p = 11/10). Typ wiederverwendet, hier mit Prüfung des Parameterbereichs. CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA1CAS1", "g", innen="1", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Bereich eines Anteils in Abhängigkeit vom Matrixparameter über die Randwerte ermitteln", typ_neben="",
    stichwoerter="N · (3530; 5294; 1176)|dritte Komponente 882,4 + 1176p|Anteil 0,08824 + 0,1176p|etwa 9 % bis etwa 21 %",
    voraussetzungen="Matrix-Vektor-Produkt mit Parameter|linearer Term ist monoton|Randwerte p = 0 und p = 1",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kundenwechsel/Baumärkte", textumfang="mittel",
    gegeben=BAUM2 + RABATT + "; im Monat vor Beginn der Aktionen hat A 3530, B 5294 und C 1176 Kunden (zusammen 10000)",
    gesucht="in welchem Bereich der prozentuale Anteil der Kunden von C im folgenden Monat liegen kann",
    verfahren="Dritte Komponente von N · (3530; 5294; 1176) als Term in p berechnen, durch 10000 teilen und die Randwerte p = 0 und p = 1 einsetzen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="%", abhaengig_von="",
    ergebnis="N · (3530; 5294; 1176) hat die dritte Komponente 882,4 + 1176p; (882,4 + 1176p)/10000 = 0,08824 + 0,1176p; damit liegt der Anteil der Kunden von C im folgenden Monat im Bereich von etwa 9 % bis etwa 21 % (amtlich)",
    zwischenergebnis="p = 0: 8,824 %|p = 1: 20,584 %",
    niveau_geschaetzt="III", fehlerquelle="nur einen Wert von p einsetzen oder den Anteil an der Summe der ersten beiden Komponenten bilden",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (8,824 % und 20,584 %). Erste Schätzung: II; korrigiert nach Deutungsliste (a) wie 2018MgrundlegendBAGLAA1WTR, Teilaufgabe 1 g (gleicher Typ): „Bereich des Anteils“ erst in einen in p linearen Term mit Randwerten übersetzen. Typ wiederverwendet. CAS-Anteil: Produkt mit Parameter mit dem Rechner, Randwerte eigen.")
row("2018MerhoehtBAGLAA1CAS1", "h", innen="1", seite="3", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Nichtnegativen stationären Vektor für alle Parameterwerte nachweisen und ein ganzzahliges Beispiel deuten", typ_neben="",
    stichwoerter="Ansatz (x; y; 10000 − x − y)|N · v_p = v_p|x = 40000 · (p − 1)/(10p − 11), y = 60000 · (p − 1)/(10p − 11), z = 10000/(11 − 10p)|v_0,1 = (3600; 5400; 1000)|Verteilung bleibt unverändert",
    voraussetzungen="stationären Vektor mit vorgegebener Summe über ein Gleichungssystem mit Parameter|Vorzeichen von Brüchen im Parameterbereich|Parameter für ganzzahlige Werte wählen",
    format="Begründung|Rechnung", operator="Zeigen Sie|Bestimmen Sie|interpretieren Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Kundenwechsel/Baumärkte", textumfang="mittel",
    gegeben=BAUM2 + RABATT,
    gesucht="Nachweis, dass es für jedes p mit 0 <= p <= 1 einen Vektor v_p mit nichtnegativen Komponenten und der Spaltensumme 10000 gibt, für den N · v_p = v_p gilt; für ein geeignet gewähltes p ein solcher Vektor mit ganzzahligen Komponenten und seine Bedeutung im Sachzusammenhang",
    verfahren="N · (x; y; 10000 − x − y) = (x; y; 10000 − x − y) nach x und y lösen; für 0 <= p <= 1 ist p − 1 <= 0 und 10p − 11 < 0, also x, y >= 0, und 10000/(11 − 10p) > 0; p = 0,1 liefert ganze Zahlen",
    schritte="4", zahlenraum="Bruch|negativ|ganz", einheiten="", abhaengig_von="",
    ergebnis="N · (x; y; 10000 − x − y) = (x; y; 10000 − x − y) liefert für 0 <= p <= 1: x = 40000 · (p − 1)/(10p − 11) >= 0, y = 60000 · (p − 1)/(10p − 11) >= 0, 10000 − x − y = 10000/(11 − 10p) >= 0; v_0,1 = (3600; 5400; 1000); die durch den Vektor beschriebene Verteilung der Kunden bleibt von einem Monat zum nächsten unverändert (amtlich)",
    zwischenergebnis="p = 0: (40000/11; 60000/11; 10000/11)|p = 1: (0; 0; 10000)",
    niveau_geschaetzt="III", fehlerquelle="nur für einzelne p rechnen statt allgemein oder die Nichtnegativität für den ganzen Bereich nicht begründen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Probe N · v_p = v_p symbolisch, v_0,1 = (3600; 5400; 1000)). Der Erwartungshorizont schreibt „von einer Woche zur nächsten“, das Modell beschreibt Monate (Druckfehler der Quelle). Schätzung III nach Deutungsliste (c): allgemeiner Nachweis mit Parameter (Vorzeichen der Komponenten für alle p hergeleitet). Neuer Typ: vorhandene Typen bestimmen einen stationären Vektor für feste Einträge oder den Bereich eines Anteils; hier werden Existenz und Nichtnegativität für den ganzen Parameterbereich nachgewiesen und ein ganzzahliges Beispiel gewählt. CAS-Anteil: Gleichungssystem mit Parameter mit dem Rechner, Vorzeichenprüfung und Wahl von p eigen.")
# ---- AG/LA (A1) CAS 2: Taufliegen, 25 BE (Aufgabe 1: Population ohne Eingriff, 9 BE; Aufgabe 2: Entnahme, 8 BE;
# Aufgabe 3: dritte Population, 8 BE)
FLIEGE = ("Taufliegen: eine fertig entwickelte Fliege (Vollinsekt) legt wöchentlich bis zu 400 Eier; innerhalb der ersten Woche "
          "nach dem Legen entsteht eine Puppe, innerhalb der zweiten aus der Puppe ein Vollinsekt; betrachtet werden Populationen "
          "weiblicher Tiere unter Laborbedingungen, Zusammensetzung (E; P; V) mit E Anzahl der Eier, aus denen weibliche Larven "
          "schlüpfen können, P Anzahl der Puppen, V Anzahl der Vollinsekten")
LMAT = "; Entwicklung von einer Woche n zur nächsten nach v_(n+1) = L · v_n mit L = ((0; 0; 200), (0,03; 0; 0), (0; 0,11; 0,7))"
START1 = "; zu Beginn der Beobachtung besteht die Population nur aus 230 Vollinsekten"
ENTN = ("; einer zweiten Population werden am Ende jeder Woche a Vollinsekten entnommen, ihre Entwicklung folgt "
        "v_(n+1) = L · v_n − (0; 0; a)")
MMAT = ("; eine dritte Population entwickelt sich nach v_(n+1) = M · v_n mit M = ((0; 0; 100), (0,09; 0; 0), (0; 0,15; 0,9))")
row("2018MerhoehtBAGLAA1CAS2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Eintrag 200: Eier je Vollinsekt und Woche|Eintrag 0,11: Anteil der Puppen, die zu Vollinsekten werden",
    voraussetzungen="Zeile und Spalte eines Eintrags als Ziel- und Ausgangszustand lesen",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Population Taufliegen", textumfang="mittel",
    gegeben=FLIEGE + LMAT + START1,
    gesucht="Bedeutung der Matrixeinträge 200 und 0,11 im Sachzusammenhang",
    verfahren="200 steht in der Zeile E und der Spalte V, 0,11 in der Zeile V und der Spalte P",
    schritte="1", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Ein Vollinsekt legt wöchentlich 200 Eier, aus denen weibliche Larven schlüpfen können; 11 % der Puppen entwickeln sich zu Vollinsekten (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I", fehlerquelle="Zeile und Spalte vertauschen und 0,11 als Anteil der Vollinsekten deuten, die zu Puppen werden",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA1CAS2", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zustände nach einem und zwei Schritten aus einem Anfangszustand berechnen", typ_neben="",
    stichwoerter="v_0 = (0; 0; 230)|v_6 = L^6 · v_0, V_6 ≈ 336|v_10 = L^10 · v_0, V_10 ≈ 652",
    voraussetzungen="Anfangsvektor aufstellen|Matrixpotenz mit dem Rechner",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Population Taufliegen", textumfang="kurz",
    gegeben=FLIEGE + LMAT + START1,
    gesucht="Nachweis, dass sechs Wochen nach Beobachtungsbeginn etwa 336 und zehn Wochen danach etwa 652 Vollinsekten zur Population gehören",
    verfahren="v_0 = (0; 0; 230) aufstellen und L^6 · v_0 sowie L^10 · v_0 mit dem Rechner berechnen",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="v_0 = (0; 0; 230), v_6 = L^6 · v_0 ≈ (E_6; P_6; 336), v_10 = L^10 · v_0 ≈ (E_10; P_10; 652) (amtlich)",
    zwischenergebnis="v_6 ≈ (52360; 1606; 336)|v_10 ≈ (108813; 2765; 652)",
    niveau_geschaetzt="I", fehlerquelle="den Anfangsvektor als (230; 0; 0) ansetzen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (335,5 und 652,5). Typ wiederverwendet, hier nach 6 und 10 Schritten über Matrixpotenzen. CAS-Anteil: Matrixpotenzen mit dem Rechner.")
row("2018MerhoehtBAGLAA1CAS2", "c", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Jährlichen Wachstumsfaktor aus zwei Zuständen im Abstand mehrerer Schritte nachweisen", typ_neben="",
    stichwoerter="v_14 = L^14 · v_0, V_14 ≈ 1241|652/336 ≈ 1,94 und 1241/652 ≈ 1,90|Zunahme um etwa 92 % je vier Wochen|1,92^(1/4) ≈ 1,18, wöchentlich etwa 18 %",
    voraussetzungen="Quotient als Wachstumsfaktor|prozentuale Zunahme aus dem Faktor|vierte Wurzel für den Faktor je Woche",
    format="Begründung|Rechnung", operator="Zeigen Sie|Bestimmen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Biologie/Population Taufliegen", textumfang="mittel",
    gegeben=FLIEGE + LMAT + START1 + "; nach 6 Wochen etwa 336, nach 10 Wochen etwa 652 Vollinsekten; Vermutung: ab sechs Wochen nach Beobachtungsbeginn nimmt die Anzahl der Vollinsekten innerhalb von jeweils vier Wochen um etwa 92 % zu",
    gesucht="Nachweis, dass die Vermutung zwischen 6 und 10 sowie zwischen 10 und 14 Wochen näherungsweise zutrifft; passend zur Vermutung die durchschnittliche wöchentliche Zunahme der Anzahl der Vollinsekten in Prozent",
    verfahren="L^14 · v_0 berechnen; die Quotienten V_10/V_6 und V_14/V_10 mit 1,92 vergleichen; wöchentlicher Faktor als vierte Wurzel aus 1,92",
    schritte="4", zahlenraum="dezimal|Prozent|Wurzel", einheiten="%", abhaengig_von="2018MerhoehtBAGLAA1CAS2-1b",
    ergebnis="v_14 = L^14 · v_0 ≈ (E_14; P_14; 1241); 652/336 ≈ 1,94 und 1241/652 ≈ 1,90 entsprechen jeweils näherungsweise einer Zunahme von etwa 92 %; k = 1,92^(1/4) ≈ 1,18, d. h. die Anzahl nimmt wöchentlich um etwa 18 % zu (amtlich)",
    zwischenergebnis="V_14 ≈ 1240,6",
    niveau_geschaetzt="II", fehlerquelle="92 % durch 4 teilen (23 % je Woche) statt die vierte Wurzel aus 1,92 zu ziehen",
    bemerkung="Standardbezug: K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (1,945; 1,901; 1,1771). Typ wiederverwendet, hier ein wöchentlicher Faktor (vierte Wurzel) und nur die Komponente V über Quotienten statt aller Komponenten über den Faktor hoch n. CAS-Anteil: Matrixpotenz und Wurzel mit dem Rechner.")
row("2018MerhoehtBAGLAA1CAS2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Zustände nach einem und zwei Schritten aus einem Anfangszustand berechnen", typ_neben="",
    stichwoerter="v_0 = (0; 4000; 0)|Entnahme (0; 0; 10) je Woche|v_1 = (0; 0; 430)|v_2 = (86000; 0; 291)",
    voraussetzungen="Matrix-Vektor-Produkt|Vektor subtrahieren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Population Taufliegen", textumfang="kurz",
    gegeben=FLIEGE + LMAT + ENTN + "; zu Beginn besteht die Population nur aus 4000 Puppen; am Ende jeder Woche werden 10 Vollinsekten entnommen",
    gesucht="Zusammensetzung der Population zwei Wochen nach Beobachtungsbeginn",
    verfahren="Zweimal v_(n+1) = L · v_n − (0; 0; 10) anwenden",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="v_0 = (0; 4000; 0), v_1 = L · v_0 − (0; 0; 10) = (0; 0; 430), v_2 = L · v_1 − (0; 0; 10) = (86000; 0; 291) (amtlich)",
    zwischenergebnis="L · v_0 = (0; 0; 440)|L · v_1 = (86000; 0; 301)",
    niveau_geschaetzt="I", fehlerquelle="die Entnahme vor statt nach der Multiplikation abziehen",
    bemerkung="Standardbezug: K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet, hier mit Entnahme nach jedem Schritt. CAS-Anteil: Matrix-Vektor-Produkte mit dem Rechner.")
row("2018MerhoehtBAGLAA1CAS2", "b", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Aussage über laufende gegenüber einmaliger Entnahme im Sachzusammenhang beurteilen", typ_neben="",
    stichwoerter="fünf Wochen je 10 Vollinsekten gegen einmal 50 am Ende|entnommene Tiere vermehren sich nicht mehr|Aussage falsch",
    voraussetzungen="Wirkung eines Eingriffs auf die folgenden Übergänge|Linearität des Modells",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Population Taufliegen", textumfang="mittel",
    gegeben=FLIEGE + LMAT + ENTN + "; Aussage: Entnimmt man der Population während eines Zeitraums von fünf Wochen am Ende jeder Woche 10 Vollinsekten, führt dies zur gleichen Zusammensetzung, wie wenn erst nach Ablauf des gesamten Zeitraums 50 Vollinsekten entnommen werden",
    gesucht="Beurteilung der Aussage",
    verfahren="Bei einmaliger Entnahme am Ende entwickelt sich die Population fünf Wochen ungestört nach L; bei wöchentlicher Entnahme fehlen die entnommenen Tiere in den folgenden Wochen bei der Eiablage und beim Überleben – die Zusammensetzungen unterscheiden sich",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist falsch: werden die Vollinsekten erst nach Ablauf des Zeitraums entnommen, kann sich die Population vorher ungestört gemäß L entwickeln; bei wöchentlicher Entnahme können die entnommenen Tiere nicht mehr zur Vermehrung beitragen, sodass die Population am Ende des Zeitraums weniger Eier, Puppen und Vollinsekten enthalten wird (amtlich)",
    zwischenergebnis="Unterschied unabhängig vom Anfangszustand: bei wöchentlicher Entnahme 6386 Eier und 131,4 Puppen weniger, aber etwa 6,4 Vollinsekten mehr",
    niveau_geschaetzt="II", fehlerquelle="wegen 5 · 10 = 50 die Aussage für richtig halten, ohne die Wirkung auf die Vermehrung zu bedenken",
    bemerkung="Standardbezug: K1 III, K6 II. AB amtlich: III. Amtlich; die eigene Rechnung bestätigt das Urteil „falsch“, nicht aber die Begründung für die Vollinsekten: der Unterschied der beiden Zustände hängt nicht vom Anfangszustand ab (Summe L^j · (0; 0; 10) für j = 0 bis 4 gegen (0; 0; 50)); bei wöchentlicher Entnahme sind es nach fünf Wochen 6386 Eier und 131,4 Puppen weniger, aber etwa 6,4 Vollinsekten mehr (43,57 statt 50 fehlen) – der Erwartungshorizont behauptet weniger Vollinsekten. Schätzung II (Aussage beurteilen, kein Eintrag der Deutungsliste); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: vorhandene Entnahmetypen berechnen Zustände oder die Entnahmemenge für einen stationären Zustand; hier wird eine Aussage über den Zeitpunkt der Entnahme beurteilt. CAS-Anteil: keiner (Vergleichsrechnung mit dem Rechner möglich).")
row("2018MerhoehtBAGLAA1CAS2", "c", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Anteil zu entfernender Individuen für einen stationären Zustand berechnen", typ_neben="",
    stichwoerter="dauerhaft 20000 Eier und 600 Puppen|L · (20000; 600; V) − (0; 0; a) = (20000; 600; V)|V = 100|a = 36",
    voraussetzungen="stationären Zustand als Gleichung ansetzen|lineares Gleichungssystem mit zwei Unbekannten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Population Taufliegen", textumfang="kurz",
    gegeben=FLIEGE + LMAT + ENTN + "; zur Population sollen dauerhaft 20000 Eier und 600 Puppen gehören",
    gesucht="Anzahl der Vollinsekten in der Population und Anzahl der Vollinsekten, die am Ende jeder Woche entnommen werden müssen",
    verfahren="Stationären Zustand ansetzen: L · (20000; 600; V) − (0; 0; a) = (20000; 600; V); erste Zeile 200V = 20000, dritte Zeile 66 + 0,7V − a = V",
    schritte="3", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="L · (20000; 600; V) − (0; 0; a) = (20000; 600; V) ⇔ V = 100 ∧ a = 36; die Population hat 100 Vollinsekten, am Ende jeder Woche müssen 36 entnommen werden (amtlich)",
    zwischenergebnis="0,03 · 20000 = 600 (zweite Zeile erfüllt)",
    niveau_geschaetzt="II", fehlerquelle="die Entnahme a in der Gleichung vergessen oder mit positivem Vorzeichen ansetzen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (V = 100, a = 36). Typ wiederverwendet, hier eine absolute Anzahl a über einen Entnahmevektor statt eines Anteils (Definition nennt den Anteil P'/P). CAS-Anteil: Gleichungssystem mit dem Rechner, Ansatz eigen.")
row("2018MerhoehtBAGLAA1CAS2", "a", innen="3", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Parameter eines Vektors aus einer Matrix-Vektor-Gleichung bestimmen", typ_neben="",
    stichwoerter="Ansatz (b · x; 4x; x)|M · v = c · v|c = 1,5|b = 200/3",
    voraussetzungen="Verhältnisse in einen Vektoransatz übersetzen|konstanter Wachstumsfaktor als M · v = c · v|Gleichungssystem komponentenweise",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Population Taufliegen", textumfang="mittel",
    gegeben=FLIEGE + MMAT + "; es gibt Zusammensetzungen mit drei Eigenschaften: die Anzahlen der Eier und der Vollinsekten stehen im Verhältnis b : 1; die Anzahl der Puppen ist viermal so groß wie die Anzahl der Vollinsekten; die Anzahlen der Eier, Puppen und Vollinsekten wachsen von einer Woche zur nächsten jeweils mit einem konstanten Faktor c",
    gesucht="die Werte von b und c",
    verfahren="Ansatz v = (b · x; 4x; x), M · v = c · v: dritte Zeile 0,15 · 4x + 0,9x = c · x liefert c = 1,5; erste Zeile 100x = c · b · x liefert b = 200/3; zweite Zeile 0,09 · b · x = 6x als Probe",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="M · (b · x; 4 · x; x) = c · (b · x; 4 · x; x) ⇔ b = 200/3 ∧ c = 1,5 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II", fehlerquelle="das Verhältnis b : 1 als (x; 4x; b · x) umgekehrt ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (b = 200/3, c = 3/2). Schätzung II (Eigenschaften in (b · V; 4V; V) und M · v = c · v übersetzen, Verhältnisse wörtlich vorgegeben); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet, hier mit zwei Unbekannten (Eintrag und Faktor). CAS-Anteil: Gleichungssystem mit dem Rechner, Ansatz eigen.")
row("2018MerhoehtBAGLAA1CAS2", "b", innen="3", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Langfristige Entwicklung aus M³ als Vielfachem der Einheitsmatrix durch Fallunterscheidung beschreiben", typ_neben="",
    stichwoerter="Insektizid: Überlebensanteil der Vollinsekten 0 statt 0,9|N = ((0; 0; 100), (0,09; 0; 0), (0; 0,15; 0))|N^3 = 1,35 · E|Aussage richtig",
    voraussetzungen="Matrix an eine veränderte Sachlage anpassen|Matrixpotenz|M^n = c · E als Wachstum mit dem Faktor c je n Schritte deuten",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Population Taufliegen", textumfang="mittel",
    gegeben=FLIEGE + MMAT + "; ein Insektizid bewirkt, dass von einer Woche zur nächsten stets alle Vollinsekten sterben; die Überlebenschancen der Eier und Puppen und die Fruchtbarkeit der Vollinsekten bleiben unverändert; Aussage: im Rhythmus von drei Wochen betrachtet steigen die Anzahl der Eier, die Anzahl der Puppen und die Anzahl der Vollinsekten jeweils exponentiell an",
    gesucht="Beurteilung der Aussage",
    verfahren="In M den Eintrag 0,9 durch 0 ersetzen; N^3 = 1,35 · E berechnen, also v_(n+3) = 1,35 · v_n und nach 3x Wochen der Faktor 1,35^x",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist richtig: die Entwicklung von einer Woche zur nächsten wird durch N = ((0; 0; 100), (0,09; 0; 0), (0; 0,15; 0)) beschrieben, und es gilt N^(3x) · v_n = 1,35^x · v_n (amtlich)",
    zwischenergebnis="N^3 = 1,35 · E",
    niveau_geschaetzt="II", fehlerquelle="die Matrix M unverändert verwenden oder den Überlebensanteil der Vollinsekten auf 0 setzen, aber auch die Fruchtbarkeit streichen",
    bemerkung="Standardbezug: K1 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (N^3 = 27/20 · E). Erste Schätzung: III; korrigiert nach dem Prinzip der Deutungsliste: der Dreiwochenrhythmus steht in der zu beurteilenden Aussage, der Sonderfall N^3 = 1,35 · E ist nicht erst zu finden ((b) nur bei gefundenem Sonderfall). Typ wiederverwendet, hier ohne Fallunterscheidung. CAS-Anteil: Matrixpotenz mit dem Rechner.")
# ---- AG/LA (A2) CAS 1: Museum, 25 BE (eine Aufgabe, a–f). Landesheft: dieselbe Aufgabe steht als 2018-bb-ea-cas B3.1
# (CAS-Heft Brandenburg) und, mit vorgegebener Ebenengleichung in f, als 2018-bb-ea B3.1 (WTR-Fassung des Landes).
MUSEUM = ("Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG dargestellt; die obere Etage "
          "entspricht der Pyramide DEFG, die untere Etage dem Körper ABCDEF, der Teil der Pyramide DEFS ist; die Ebene, in "
          "der das Dreieck ABC liegt, beschreibt die Horizontale, das Dreieck DEF liegt parallel zu dieser Ebene; "
          "A(−5; 5; 0), B(−5; 25; 0), D(0; 0; 15), E(0; 30; 15), F(−25; 5; 15), G(−10; 10; 35); 1 LE = 1 m")
MUSEUM_SK = ("Schrägbild des Körpers ohne Koordinatenachsen und ohne Maße: oben die Spitze G, von ihr Kanten zu den Ecken "
             "des waagerecht liegenden, grau getönten Dreiecks DEF (F links, E rechts, D vorn in der Mitte); darunter das "
             "kleinere, ebenfalls grau getönte Dreieck ABC (C links, A vorn, B rechts); die Seitenkanten FC, DA und EB "
             "verbinden beide Dreiecke; von C, A und B laufen gestrichelte Verlängerungen nach unten zusammen und treffen "
             "sich im Punkt S unterhalb des Körpers")
row("2018MerhoehtBAGLAA2CAS1", "a", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Gegebene Rechnung zum Geradenschnittpunkt erläutern", typ_neben="",
    stichwoerter="Gerade AD mit Richtung (−5; 5; −15)|Gerade BE mit Richtung (−5; −5; −15)|Gleichsetzen liefert r = s = 3|Einsetzen liefert die Spitze S(−15; 15; −30)",
    voraussetzungen="Parameterform einer Geraden aus Stützpunkt und Richtungsvektor erkennen|Schnittpunkt zweier Geraden durch Gleichsetzen",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=MUSEUM_SK, kontext="Architektur/Museum", textumfang="lang",
    gegeben=MUSEUM + "; abgedruckte Rechnung: (0; 0; 15) + r · (−5; 5; −15) = (0; 30; 15) + s · (−5; −5; −15) ⇔ r = s = 3; (0; 0; 15) + 3 · (−5; 5; −15) = (−15; 15; −30), d. h. S(−15; 15; −30)",
    gesucht="Erläuterung des dargestellten Vorgehens zur Ermittlung der Koordinaten von S",
    verfahren="Die beiden Terme als Geraden AD (Stützpunkt D, Richtung DA) und BE (Stützpunkt E, Richtung EB) erkennen; das Gleichsetzen liefert die Parameter des Schnittpunkts, das Einsetzen von r = 3 in die Gerade AD die Koordinaten der Spitze S",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Alle Punkte der Gerade AD lassen sich durch (0; 0; 15) + r · (−5; 5; −15), r ∈ IR, darstellen, alle Punkte der Gerade BE durch (0; 30; 15) + s · (−5; −5; −15), s ∈ IR; der erste Schritt liefert die Werte von r und s, die zum Schnittpunkt S der beiden Geraden gehören, im zweiten Schritt werden die Koordinaten von S als Punkt der Gerade AD ermittelt (amtlich)",
    zwischenergebnis="DA = (−5; 5; −15)|EB = (−5; −5; −15)", niveau_geschaetzt="II",
    fehlerquelle="die Rechnung nur nacherzählen, ohne die Terme als die Kantengeraden AD und BE zu benennen",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (r = s = 3, S(−15; 15; −30)). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA2CAS1", "b", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen", typ_neben="",
    stichwoerter="Bodenfläche der oberen Etage: Dreieck DEF|drei Skalarprodukte der Seitenvektoren|keines gleich null",
    voraussetzungen="Verbindungsvektoren bilden|Skalarprodukt null genau bei Orthogonalität|alle drei Ecken prüfen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Körper", skizze=MUSEUM_SK, kontext="Architektur/Museum", textumfang="lang",
    gegeben=MUSEUM + "; die Bodenfläche der oberen Etage ist das Dreieck DEF",
    gesucht="Nachweis, dass die Bodenfläche der oberen Etage nicht rechtwinklig ist",
    verfahren="Für jede der drei Ecken das Skalarprodukt zweier Seitenvektoren berechnen; keines ist null, also hat das Dreieck keinen rechten Winkel",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="DE ∘ DF ≠ 0, DE ∘ EF ≠ 0, DF ∘ EF ≠ 0 (amtlich)",
    zwischenergebnis="DE = (0; 30; 0)|DF = (−25; 5; 0)|EF = (−25; −25; 0)|DE ∘ DF = 150, DE ∘ EF = −750, DF ∘ EF = 500", niveau_geschaetzt="I",
    fehlerquelle="nur ein Skalarprodukt prüfen und daraus auf das ganze Dreieck schließen",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (150; −750; 500). Typ wiederverwendet. CAS-Anteil: Skalarprodukte mit dem Rechner möglich.")
row("2018MerhoehtBAGLAA2CAS1", "c", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Winkel zwischen zwei Kanten über das Skalarprodukt berechnen",
    typ_neben="Ebene Figur: Höhe eines Dreiecks im Raum über den Flächeninhalt berechnen",
    stichwoerter="Innenwinkel bei E: cos ε = (ED ∘ EF)/(|ED| · |EF|)|ε = 45°|Höhe zur Seite EF über den Flächeninhalt|h = 15√2 ≈ 21,21",
    voraussetzungen="Winkelformel mit Skalarprodukt und Beträgen|Flächeninhalt eines Dreiecks im Raum|Höhe als doppelter Flächeninhalt durch Grundseite",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=MUSEUM_SK, kontext="Architektur/Museum", textumfang="lang",
    gegeben=MUSEUM + "; betrachtet wird das Dreieck DEF",
    gesucht="Größe des Innenwinkels des Dreiecks DEF bei E; Länge der Höhe zur Seite EF",
    verfahren="cos ε = (ED ∘ EF)/(|ED| · |EF|); für die Höhe den doppelten Flächeninhalt |ED × EF| durch |EF| teilen",
    schritte="4", zahlenraum="ganz|negativ|Wurzel", einheiten="°|m", abhaengig_von="",
    ergebnis="cos ε = (ED ∘ EF)/(|ED| · |EF|), d. h. ε = 45°; Länge der Höhe aus h · |EF| = 2 · Flächeninhalt: h = 15√2 (amtlich)",
    zwischenergebnis="ED = (0; −30; 0)|EF = (−25; −25; 0)|ED ∘ EF = 750|cos ε = √2/2|Flächeninhalt DEF = 375|EF = 25√2|h ≈ 21,21", niveau_geschaetzt="II",
    fehlerquelle="den Winkel zwischen DE und EF (Außenwinkel 135°) statt zwischen ED und EF berechnen oder die Seitenlänge als Höhe angeben",
    bemerkung="Standardbezug: K2 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (45°; 15√2 ≈ 21,213). Der Erwartungshorizont schreibt h · |EF| = |DE ∘ EF| mit dem Skalarprodukt; gemeint ist der doppelte Flächeninhalt |DE × EF| – wegen ε = 45° haben beide den Betrag 750, das Ergebnis stimmt (Befund der Quelle). Typ und Nebentyp wiederverwendet. CAS-Anteil: Skalarprodukt, Vektorprodukt und Winkel mit dem Rechner.")
row("2018MerhoehtBAGLAA2CAS1", "d", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Pyramidenvolumen aus Grundfläche und Höhe berechnen",
    typ_neben="Körper: Bedarfsgröße aus einem Volumen im Sachzusammenhang nachweisen",
    stichwoerter="obere Etage: Pyramide DEFG|Höhe von F auf DE ist 25|Pyramidenhöhe 35 − 15 = 20|Volumen 2500 m^3|25 · 0,8 kW = 20 kW <= 25 kW",
    voraussetzungen="Grundfläche eines Dreiecks aus Grundseite und Höhe|Höhe der Pyramide als Differenz der x3-Koordinaten bei waagerechter Grundfläche|Dreisatz",
    format="Rechnung|Begründung", operator="Weisen Sie nach", antwort="Zahl|Text",
    material="Körper", skizze=MUSEUM_SK, kontext="Architektur/Museum", textumfang="lang",
    gegeben=MUSEUM + "; für die obere Etage wird eine Anlage zur Entfeuchtung der Luft installiert, die für 100 m^3 Rauminhalt eine elektrische Leistung von 0,8 Kilowatt benötigt",
    gesucht="Nachweis, dass für den Betrieb der Anlage eine Leistung von 25 Kilowatt ausreichend ist",
    verfahren="Grundfläche DEF als 1/2 · |DE| · 25 (Höhe von F auf DE), Pyramidenhöhe 35 − 15 = 20; V = 1/3 · Grundfläche · Höhe; je 100 m^3 werden 0,8 kW benötigt, Bedarf mit 25 kW vergleichen",
    schritte="4", zahlenraum="ganz|dezimal", einheiten="m^3|kW", abhaengig_von="",
    ergebnis="Im Dreieck DEF hat die Höhe von F auf die Seite DE die Länge 25; Volumen der Pyramide DEFG: 1/3 · 1/2 · |DE| · 25 · (35 − 15) = 2500; 25 · 0,8 kW = 20 kW, d. h. die Leistung ist ausreichend (amtlich)",
    zwischenergebnis="|DE| = 30|Grundfläche 375", niveau_geschaetzt="II",
    fehlerquelle="das Volumen des ganzen Körpers statt der oberen Etage berechnen oder den Faktor 1/3 vergessen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (2500; 20 kW). Typ und Nebentyp wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA2CAS1", "e", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schnittpunkt von Gerade und Ebene berechnen", typ_neben="",
    stichwoerter="Ebene des Dreiecks DEF: x3 = 15|Gerade AG: (−5; 5; 0) + t · (−5; 5; 35)|t = 3/7|R(−50/7; 50/7; 15)",
    voraussetzungen="Ebene parallel zur Grundebene an der gemeinsamen x3-Koordinate erkennen|Gerade durch zwei Punkte|Punktprobe",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Körper", skizze=MUSEUM_SK, kontext="Architektur/Museum", textumfang="lang",
    gegeben=MUSEUM + "; Punkt R(−50/7; 50/7; 15)",
    gesucht="Nachweis, dass sich die Gerade AG und die Ebene, in der das Dreieck DEF liegt, im Punkt R schneiden",
    verfahren="D, E, F und R haben die x3-Koordinate 15; die Gerade AG aufstellen und zeigen, dass R sie für einen Parameterwert erfüllt",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="R hat wie D, E und F die x3-Koordinate 15; Gleichung der Gerade AG: x = (−5; 5; 0) + t · (−5; 5; 35), t ∈ IR; die Koordinaten von R erfüllen diese Gleichung für t = 3/7 (amtlich)",
    zwischenergebnis="35t = 15 ⇔ t = 3/7", niveau_geschaetzt="I",
    fehlerquelle="nur zeigen, dass R in der Ebene liegt, und die Punktprobe mit der Gerade AG vergessen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (t = 3/7). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA2CAS1", "f", innen="1", seite="2", punkte="7", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt auf einer Strecke mit vorgegebenem Abstand zu einer Ebene bestimmen",
    typ_neben="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen",
    stichwoerter="Scheinwerfer auf der Strecke RG|Wand EFG: 2x1 − 2x2 − x3 + 75 = 0|Abstand 5 über die Hessesche Normalform|t = 8/11 auf der Gerade AG|(−95/11; 95/11; 280/11)",
    voraussetzungen="Ebene aus drei Punkten in Koordinatenform|Strecke als Geradenstück mit Parameterbereich|Abstand Punkt–Ebene|Betragsgleichung lösen und Lösung auswählen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=MUSEUM_SK, kontext="Architektur/Museum", textumfang="mittel",
    gegeben=MUSEUM + "; R(−50/7; 50/7; 15) ist der Schnittpunkt der Gerade AG mit der Ebene des Dreiecks DEF; an einer Metallstange, die durch die Strecke RG dargestellt wird, ist ein Scheinwerfer befestigt, dessen Größe vernachlässigt wird; er beleuchtet aus einer Entfernung von 5 m die Wand, die im Modell durch das Dreieck EFG dargestellt wird",
    gesucht="Koordinaten des Punkts, der die Position des Scheinwerfers im Modell beschreibt",
    verfahren="Ebene EFG aus x = OE + u · EF + v · EG in Koordinatenform bringen; Punkte der Strecke RG als (−5 − 5t; 5 + 5t; 35t) mit 3/7 <= t <= 1 ansetzen; Abstand zur Ebene gleich 5 setzen und die Lösung auf der Strecke wählen",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="m", abhaengig_von="2018MerhoehtBAGLAA2CAS1-1e",
    ergebnis="Das aus x = OE + u · EF + v · EG resultierende Gleichungssystem x1 = −25u − 10v, x2 = 30 − 25u − 20v, x3 = 15 + 20v liefert für die Ebene, in der das Dreieck EFG liegt: 2x1 − 2x2 − x3 + 75 = 0; für t <= 1 gilt |2 · (−5 − 5t) − 2 · (5 + 5t) − 35t + 75|/3 = 5 ⇔ t = 8/11; Koordinaten des gesuchten Punkts: x1 = −95/11, x2 = 95/11, x3 = 280/11 (amtlich)",
    zwischenergebnis="Normalenvektor (2; −2; −1) mit Betrag 3|Abstand(t) = |55 − 55t|/3|zweite Lösung t = 14/11 außerhalb der Strecke|Abstand bei R etwa 10,48|Punkt etwa (−8,64; 8,64; 25,45)", niveau_geschaetzt="II",
    fehlerquelle="den Abstand ohne Division durch den Betrag des Normalenvektors ansetzen oder die Lösung außerhalb der Strecke nehmen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (t = 8/11 und 14/11, nur 8/11 im Bereich 3/7 <= t <= 1; auf RG von R aus der Anteil 23/44). Schätzung II (Ebene aufstellen, Punkt der Strecke mit Parameter, Abstand gleich 5, Lösung auf der Strecke wählen; der Abstand ist wörtlich vorgegeben – Verkettung); amtlich III – keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ und Nebentyp wiederverwendet. CAS-Anteil: Gleichungssystem und Betragsgleichung mit dem Rechner, Ansatz eigen.")
# ---- AG/LA (A2) CAS 2: Obelisk, 25 BE (eine Aufgabe, a–g; Pyramidenstumpf mit aufgesetzter Pyramide, Schatten der Spitze)
OBEL = ("Modell eines Obelisken (nicht maßstabsgetreu) im kartesischen Koordinatensystem; die xy-Ebene beschreibt den "
        "ebenen Untergrund, 1 LE = 1 m; der untere Teilkörper ABCDEFGH mit B(0,45; 0,45; 0) ist ein Stumpf einer geraden "
        "Pyramide, der Mittelpunkt des Quadrats ABCD ist der Koordinatenursprung, das Quadrat EFGH ist parallel zur "
        "xy-Ebene; der obere Teilkörper EFGHS mit E(0,35; −0,35; 7,16) ist eine gerade Pyramide, ihre Spitze S liegt auf "
        "der z-Achse und stellt die Spitze des Obelisken dar")
OBEL_SK = ("Schrägbild des schlanken, grau getönten Obelisken ohne Maße: unten das Quadrat ABCD in der xy-Ebene (A vorn "
           "links, B vorn rechts, C hinten rechts, D hinten links, verdeckte Kanten gestrichelt), vier fast senkrechte "
           "Seitenkanten zum kleineren Quadrat EFGH (E über A, F über B, G über C, H über D), darauf die flache Pyramide mit "
           "der Spitze S; die z-Achse steigt durch die Mitte senkrecht über S hinaus, die y-Achse zeigt nach rechts, die "
           "x-Achse schräg nach vorn links")
LICHT = "; Sonnenlicht fällt im Modell in parallelen Geraden mit dem Richtungsvektor v = (1; 1; −2) auf den Obelisken"
row("2018MerhoehtBAGLAA2CAS2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Spitze einer Pyramide als Schnittpunkt einer Kantengeraden mit einer Koordinatenachse berechnen", typ_neben="",
    stichwoerter="A(0,45; −0,45; 0) aus B und dem Mittelpunkt im Ursprung|Gerade AE: (0,45; −0,45; 0) + r · (−0,1; 0,1; 7,16)|x = y = 0 bei r = 4,5|Schnittpunkt (0; 0; 32,22)",
    voraussetzungen="Eckpunkt eines Quadrats aus Symmetrie|Gerade durch zwei Punkte|Schnitt mit einer Koordinatenachse",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=OBEL_SK, kontext="Bauwerk/Obelisk", textumfang="lang",
    gegeben=OBEL + "; zur Kontrolle: z-Koordinate des Schnittpunkts 32,22",
    gesucht="Koordinaten des Schnittpunkts der Gerade AE mit der z-Achse",
    verfahren="A(0,45; −0,45; 0) folgt aus B und dem Mittelpunkt im Ursprung; Gerade AE aufstellen, x- und y-Koordinate gleich 0 setzen und r einsetzen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Gerade durch A und E: x = (0,45; −0,45; 0) + r · (−0,1; 0,1; 7,16), r ∈ IR; die x- und die y-Koordinate des Schnittpunkts sind jeweils 0, dafür gilt r = 4,5, d. h. z = 4,5 · 7,16 = 32,22; Schnittpunkt (0; 0; 32,22) (amtlich)",
    zwischenergebnis="Richtungsvektor AE = (−0,1; 0,1; 7,16)", niveau_geschaetzt="I",
    fehlerquelle="A falsch aus B ablesen (etwa (−0,45; 0,45; 0)) oder mit E statt A als Stützpunkt falsch weiterrechnen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (r = 9/2, z = 32,22). Erste Schätzung: II; korrigiert nach der Grundregel wie bei diesem Typ in 2023-ga-B und 2017-ga-B (amtlich I): der Schnitt einer Kantengeraden mit der Achse ist eine Rechnung, A folgt aus der Symmetrie. Typ wiederverwendet (hier ist der Schnittpunkt die Spitze der ergänzten Pyramide, nicht S). CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA2CAS2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Strecke gegen die Horizontale über ihre Projektion berechnen", typ_neben="",
    stichwoerter="alle vier Seitenkanten gleich geneigt|Projektion von AE bzw. Abstand 0,45 · √2 des Fußpunkts von der Achse|tan α = 32,22/(0,45 · √2)|α ≈ 89°",
    voraussetzungen="rechtwinkliges Dreieck aus Achse, Fußpunkt und Achsenschnittpunkt|Tangens oder Winkel zwischen Vektor und Projektion",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=OBEL_SK, kontext="Bauwerk/Obelisk", textumfang="kurz",
    gegeben=OBEL + "; die Gerade AE schneidet die z-Achse im Punkt (0; 0; 32,22)",
    gesucht="Größe der Neigungswinkel der Seitenkanten des unteren Teilkörpers gegenüber dem Untergrund",
    verfahren="Im rechtwinkligen Dreieck aus Ursprung, A und (0; 0; 32,22): tan α = 32,22/|OA| mit |OA| = 0,45 · √2; alternativ Winkel zwischen AE und seiner Projektion (−0,1; 0,1; 0)",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="°", abhaengig_von="2018MerhoehtBAGLAA2CAS2-1a",
    ergebnis="Es gilt tan α = 32,22/(0,45 · √2), d. h. α ≈ 89° (amtlich)",
    zwischenergebnis="0,45 · √2 ≈ 0,636|tan α ≈ 50,63|α ≈ 88,87°", niveau_geschaetzt="II",
    fehlerquelle="den Abstand des Fußpunkts von der Achse als 0,45 statt 0,45 · √2 nehmen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (88,87°, auch über die Projektion). Schätzung II (Verkettung: Kantenvektor, Projektion bzw. Winkel mit der Horizontalen); amtlich I – keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet. CAS-Anteil: Winkel mit dem Rechner.")
row("2018MerhoehtBAGLAA2CAS2", "c", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines Trapezes im Raum über die Höhe zwischen den parallelen Seiten berechnen", typ_neben="",
    stichwoerter="Seitenfläche ABFE als symmetrisches Trapez|parallele Seiten |AB| = 0,9 und |EF| = 0,7|Höhe |(−0,1; 0; 7,16)| ≈ 7,16|Flächeninhalt etwa 5,7 m^2",
    voraussetzungen="Seitenflächen eines geraden Pyramidenstumpfs sind gleichschenklige Trapeze|Höhe als Abstand der Seitenmitten|Trapezformel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=OBEL_SK, kontext="Bauwerk/Obelisk", textumfang="kurz",
    gegeben=OBEL,
    gesucht="Flächeninhalt einer der Seitenflächen des unteren Teilkörpers",
    verfahren="Seitenfläche ABFE: |AB| = 0,9, |EF| = 0,7; Höhe als Betrag des Vektors von der Mitte von AB (0,45; 0; 0) zur Mitte von EF (0,35; 0; 7,16); A = 1/2 · (|AB| + |EF|) · h",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="m^2", abhaengig_von="",
    ergebnis="1/2 · (|AB| + |EF|) · |(−0,1; 0; 7,16)| ≈ 5,7, d. h. der Flächeninhalt beträgt etwa 5,7 m^2 (amtlich)",
    zwischenergebnis="|AB| = 0,9|EF| = 0,7|Höhe ≈ 7,161", niveau_geschaetzt="II",
    fehlerquelle="die Höhe 7,16 des Stumpfs statt der Höhe der geneigten Seitenfläche nehmen oder die Seitenkante AE als Trapezhöhe verwenden",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (5,729). Typ wiederverwendet. CAS-Anteil: Beträge mit dem Rechner.")
row("2018MerhoehtBAGLAA2CAS2", "d", innen="1", seite="2", punkte="5", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen eines Teilkörpers als Differenz zweier Pyramiden berechnen und erläutern", typ_neben="",
    stichwoerter="Stumpf = ganze Pyramide mit Spitze (0; 0; 32,22) minus Ergänzungspyramide über EFGH|1/3 · 0,9^2 · 32,22 − 1/3 · 0,7^2 · (32,22 − 7,16)|Volumen ≈ 4,61 m^3|Granit 2,6 t je m^3|Masse etwa 12 t",
    voraussetzungen="Pyramidenstumpf zur Pyramide ergänzen|Pyramidenvolumen|Dichte mal Volumen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=OBEL_SK, kontext="Bauwerk/Obelisk", textumfang="kurz",
    gegeben=OBEL + "; die Kantengeraden des Stumpfs schneiden die z-Achse im Punkt (0; 0; 32,22); der untere Teilkörper besteht aus Granit, ein Kubikmeter hat eine Masse von 2,6 Tonnen",
    gesucht="Masse des unteren Teilkörpers",
    verfahren="Volumen der ganzen Pyramide über ABCD mit Höhe 32,22 minus Volumen der Ergänzungspyramide über EFGH mit Höhe 32,22 − 7,16; mit 2,6 t je m^3 multiplizieren",
    schritte="3", zahlenraum="dezimal", einheiten="m^3|t", abhaengig_von="2018MerhoehtBAGLAA2CAS2-1a",
    ergebnis="(1/3 · |AB|^2 · 32,22 − 1/3 · |EF|^2 · (32,22 − 7,16)) · 2,6 t ≈ 12 t; die Masse beträgt etwa 12 t (amtlich)",
    zwischenergebnis="Volumen ≈ 4,606 m^3|Masse ≈ 11,98 t", niveau_geschaetzt="II",
    fehlerquelle="die Höhe der Ergänzungspyramide als 7,16 statt 32,22 − 7,16 nehmen oder nur die große Pyramide berechnen",
    bemerkung="Standardbezug: K2 I, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (4,606 m^3; 11,98 t; auch mit der Stumpfformel). Der Erwartungshorizont druckt 32,22 − 7,61 statt 32,22 − 7,16 (Druckfehler der Quelle; mit 7,61 ergäben sich 12,17 t, das gerundete Ergebnis 12 t bleibt). Typ wiederverwendet, hier mit Masse, ohne Erläuterung und am Pyramidenstumpf statt am Quader. CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA2CAS2", "e", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen", typ_neben="",
    stichwoerter="I x = 0,45, II y = 0, III x − y = 0, IV x − z = 0|Symmetrieebenen enthalten die z-Achse|II und III ja, I und IV nein|kein Punkt des Modells mit x > 0,45",
    voraussetzungen="Symmetrieebenen einer geraden quadratischen Pyramide|Lage einer Ebene aus ihrer Koordinatengleichung",
    format="Kurzantwort|Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Körper", skizze=OBEL_SK, kontext="Bauwerk/Obelisk", textumfang="mittel",
    gegeben=OBEL + "; Gleichungen I x = 0,45, II y = 0, III x − y = 0, IV x − z = 0",
    gesucht="für jede Gleichung die Entscheidung, ob sie eine Symmetrieebene des Obelisken beschreibt; für eine Gleichung die Begründung, dass sie keine solche Ebene darstellt",
    verfahren="Symmetrieebenen enthalten die z-Achse und eine Seitenmitte oder eine Diagonale des Grundquadrats: y = 0 (Mitten von AB und CD) und x − y = 0 (durch B und D); x = 0,45 und x − z = 0 enthalten die z-Achse nicht",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Die Gleichungen II und III beschreiben Symmetrieebenen, die Gleichungen I und IV nicht; die Gleichung x = 0,45 stellt keine Symmetrieebene dar, da das Modell des Obelisken keine Punkte enthält, deren x-Koordinate größer als 0,45 ist (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="x − y = 0 verwerfen, weil die Diagonalebene nicht parallel zu einer Seite ist",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Spiegelung aller Eckpunkte an den vier Ebenen). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA2CAS2", "f", innen="1", seite="2", punkte="2", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Lage des Schattens einer Pyramidenspitze über den Vergleich von Kantenneigung und Lichteinfall begründen", typ_neben="",
    stichwoerter="Licht mit v = (1; 1; −2) fällt in der Ebene x − y = 0 der Kante FS|Einfallswinkel gegen den Untergrund etwa 54,7°|Schatten auf dem Untergrund nur bei steilerer Kante FS|steilere Kante heißt höherer oberer Teilkörper",
    voraussetzungen="Schatten eines Punkts als Schnitt der Lichtgeraden|Neigungswinkel gegen den Untergrund|Neigung und Höhe der Pyramide verknüpfen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=OBEL_SK, kontext="Bauwerk/Sonnenlicht", textumfang="kurz",
    gegeben=OBEL + LICHT,
    gesucht="Begründung, dass der Schatten der Spitze des Obelisken nur dann auf dem Untergrund liegt, wenn der obere Teilkörper ausreichend hoch ist",
    verfahren="Die Lichtgerade durch S verläuft in derselben senkrechten Ebene wie die Kante FS; sie bleibt nur dann außerhalb des Obelisken, wenn FS steiler gegen den Untergrund geneigt ist als das Licht; die Neigung von FS wächst mit der Höhe des oberen Teilkörpers",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="°", abhaengig_von="",
    ergebnis="Der Schatten der Spitze des Obelisken liegt nur dann auf dem Untergrund, wenn der Winkel zwischen der durch FS dargestellten Seitenkante und dem Untergrund größer ist als der Winkel, unter dem das Sonnenlicht auf den Untergrund trifft (amtlich)",
    zwischenergebnis="Einfallswinkel des Lichts: tan = √2, etwa 54,7°|Bedingung z_S − 7,16 > 0,7, also z_S > 7,86", niveau_geschaetzt="III",
    fehlerquelle="mit einer beliebigen Seitenkante statt der in Lichtrichtung liegenden Kante FS argumentieren",
    bemerkung="Standardbezug: K1 III, K3 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Einfallswinkel 54,74°, Grenzhöhe 7,86 m, mit Teilaufgabe g verträglich). Erste Schätzung: II; korrigiert nach Deutungsliste (a) und dem Prinzip: die Bedingung „Schatten auf dem Untergrund bzw. auf dem unteren Teilkörper“ ist erst als Vergleich von Kantenneigung und Lichteinfall zu finden. Neuer Typ: vorhandene Schattentypen berechnen einen Schattenpunkt, hier wird die Bedingung für seine Lage qualitativ über zwei Neigungswinkel begründet. CAS-Anteil: keiner.")
row("2018MerhoehtBAGLAA2CAS2", "g", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Höhe einer Spitze aus dem Abstand ihres Schattenpunkts zu einem Punkt bestimmen", typ_neben="",
    stichwoerter="Lichtgerade (0; 0; z_S) + t · (1; 1; −2)|Schatten S'(z_S/2; z_S/2; 0)|Abstand |BS'| = 5,1|z_S ≈ 8,1",
    voraussetzungen="Gerade mit Parameter im Stützpunkt|Schnitt mit der xy-Ebene|Abstand zweier Punkte|quadratische Gleichung, positive Lösung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=OBEL_SK, kontext="Bauwerk/Sonnenlicht", textumfang="kurz",
    gegeben=OBEL + LICHT + "; der Schatten der Spitze liegt auf dem Untergrund und hat von dem Punkt, der im Modell durch B dargestellt wird, den Abstand 5,1 m",
    gesucht="Höhe des Obelisken",
    verfahren="Lichtgerade durch S(0; 0; z_S) mit Richtung v mit der xy-Ebene schneiden: S'(z_S/2; z_S/2; 0); |BS'| = 5,1 nach z_S > 0 lösen",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="Gerade durch S mit dem Richtungsvektor v: x = (0; 0; z_S) + t · (1; 1; −2), t ∈ IR; z_S − 2t = 0 ⇔ t = z_S/2 liefert als Schnittpunkt mit der xy-Ebene S'(z_S/2; z_S/2; 0); für z_S > 0 liefert |BS'| = 5,1: z_S ≈ 8,1, d. h. die Höhe des Obelisken beträgt etwa 8,1 m (amtlich)",
    zwischenergebnis="2 · (z_S/2 − 0,45)^2 = 5,1^2|z_S = 0,9 + 5,1 · √2 ≈ 8,112", niveau_geschaetzt="II",
    fehlerquelle="den Schattenpunkt mit fester Höhe berechnen oder den Abstand zum Ursprung statt zu B ansetzen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (8,112; z_S > 7,86 wie in f verlangt). Schätzung II (Schattenpunkt (h/2; h/2; 0) bestimmen, Abstand zu B gleich 5,1 setzen – Abstand wörtlich vorgegeben, Verkettung); amtlich III – keine Regel als falsch angewandt erkannt, Abweichung bleibt. Neuer Typ: vorhanden sind Schattenpunkte bei bekannter Höhe, hier ist die Höhe die Unbekannte im Stützpunkt der Lichtgeraden. CAS-Anteil: Gleichung mit dem Rechner lösen, Ansatz eigen.")
# ---- Stochastik CAS 1 (Aufgabe 1: Kunststoffteile, 15 BE; Aufgabe 2: Glücksrad, 10 BE). Geteilt mit dem WTR-Zweig
# (2018MerhoehtBStochastikWTR1): 1 d, 2 a, 2 b wortgleich (im CAS-Stamm Stichprobe 500 statt 200); 2 c abgewandelt.
KUNST = ("Ein Unternehmen stellt Kunststoffteile her; erfahrungsgemäß sind 4 % der hergestellten Teile fehlerhaft; die "
         "Anzahl fehlerhafter Teile unter zufällig ausgewählten kann als binomialverteilt angenommen werden")
GRANULAT = ("; nach einem Wechsel des Granulats vermutet der Produktionsleiter, dass sich der Anteil der fehlerhaften Teile "
            "reduziert hat; getestet wird die Nullhypothese „Der Anteil der fehlerhaften Teile beträgt mindestens 4 %.“ "
            "auf der Grundlage einer Stichprobe von 500 Teilen auf einem Signifikanzniveau von 5 %")
RAD = ("Glücksrad mit den Sektoren Blau 180°, Rot 120°, Grün 60°; Einsatz 5 Euro für drei Drehungen; dreimal die gleiche "
       "Farbe: 10 Euro Auszahlung; drei verschiedene Farben: anderer Betrag; sonst nichts; P(dreimal gleiche Farbe) = 1/6")
GETEILT = ("Teilaufgabe wortgleich mit dem WTR-Zweig (2018-ea-B-wtr, Datei 2018MerhoehtBStochastikWTR1, Teilaufgabe {}), "
           "geteilter Typ, Felder übernommen; Schätzung aus der WTR-Zeile übernommen.")
row("2018MerhoehtBStochastikCAS1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="X ~ B(800; 0,04)|P(X = 30) ≈ 6,9 %|mindestens 5 % von 800 = mindestens 40: P(X >= 40) ≈ 9,1 %",
    voraussetzungen="Binomialverteilung am Rechner|Anteil in Anzahl umrechnen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Qualität", textumfang="kurz",
    gegeben=KUNST + "; 800 Teile werden zufällig ausgewählt; A: genau 30 der Teile sind fehlerhaft; B: mindestens 5 % der Teile sind fehlerhaft",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="Einzel- und kumulierte Wahrscheinlichkeit mit n = 800, p = 0,04; 5 % von 800 sind 40",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="X: Anzahl der fehlerhaften Kunststoffteile; P(X = 30) ≈ 6,9 %; 5 % · 800 = 40, P(X >= 40) ≈ 9,1 % (amtlich)",
    zwischenergebnis="P(X = 30) ≈ 0,0693|P(X >= 40) ≈ 0,0912", niveau_geschaetzt="I",
    fehlerquelle="„mindestens 5 %“ als X >= 5 lesen oder P(X > 40) statt P(X >= 40) berechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,0693; 0,0912). Typ und Nebentyp wiederverwendet (wie WTR 1 1 a mit n = 50). CAS-Anteil: Binomialwerte mit dem Rechner.")
row("2018MerhoehtBStochastikCAS1", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln", typ_neben="",
    stichwoerter="Y: Anzahl fehlerfreier Teile, p = 0,96|P(Y >= 100) >= 0,95|n = 107: 93,4 %, n = 108: 97,0 %|mindestens 108 Teile",
    voraussetzungen="Trefferdefinition wechseln (fehlerfrei)|Binomialmodell mit unbekanntem n|Probieren am Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Qualität", textumfang="mittel",
    gegeben=KUNST,
    gesucht="Mindestanzahl zufällig auszuwählender Teile, damit davon mit einer Wahrscheinlichkeit von mindestens 95 % mindestens 100 Teile keinen Fehler haben",
    verfahren="Y ~ B(n; 0,96) für die fehlerfreien Teile; das kleinste n mit P(Y >= 100) >= 0,95 durch Probieren mit dem Rechner suchen",
    schritte="3", zahlenraum="Prozent|dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="Y: Anzahl der Kunststoffteile, die keinen Fehler haben; P(Y >= 100) ≈ 93,4 % für n = 107 und ≈ 97,0 % für n = 108 (p = 0,96); es müssen mindestens 108 Teile ausgewählt werden (amtlich)",
    zwischenergebnis="n = 106: 0,867|n = 107: 0,934|n = 108: 0,970", niveau_geschaetzt="III",
    fehlerquelle="mit p = 0,04 (fehlerhaft) statt 0,96 rechnen oder n = 100 annehmen",
    bemerkung="Standardbezug: K1 I, K2 III, K3 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (0,9344; 0,9705). Erste Schätzung: II (Probieren am Rechner, damals kein Listeneintrag); korrigiert nach Deutungsliste (f) (iqb.md v1.17 § 7, Beschluss vom 26.09.2026 Punkt 2): Mindestumfang für eine Mindestwahrscheinlichkeit bestimmen ist III. Typ wiederverwendet (mindestens 100 Treffer = mehr als 99). CAS-Anteil: Probieren mit dem Rechner, Ansatz eigen.")
row("2018MerhoehtBStochastikCAS1", "c", innen="1", seite="1", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel eines einseitigen Signifikanztests bestimmen", typ_neben="",
    stichwoerter="H0: p >= 0,04, n = 500, α = 5 %|linksseitig: P(X <= k) <= 0,05 ⇔ k <= 12|Ablehnung bei höchstens zwölf fehlerhaften Teilen",
    voraussetzungen="Ablehnungsbereich links|kumulierte Wahrscheinlichkeit gegen α",
    format="Rechnung", operator="Bestimmen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Produktion/Qualität", textumfang="mittel",
    gegeben=KUNST + GRANULAT,
    gesucht="zugehörige Entscheidungsregel",
    verfahren="Größtes k mit P(X <= k) <= 0,05 für X ~ B(500; 0,04)",
    schritte="2", zahlenraum="Prozent|ganz", einheiten="", abhaengig_von="",
    ergebnis="P(X <= k) <= 5 % ⇔ k <= 12 (n = 500, p = 0,04); sind höchstens zwölf der 500 Teile fehlerhaft, so wird die Nullhypothese abgelehnt (amtlich)",
    zwischenergebnis="P(X <= 12) ≈ 0,036|P(X <= 13) ≈ 0,062", niveau_geschaetzt="II",
    fehlerquelle="rechtsseitig testen, weil die Nullhypothese „mindestens“ enthält",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,0362; 0,0623). Typ wiederverwendet (wie WTR 1 1 c mit n = 200). CAS-Anteil: kumulierte Werte mit dem Rechner.")
row("2018MerhoehtBStochastikCAS1", "d", innen="1", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Wahl der Nullhypothese aus der Sicht des Entscheiders begründen", typ_neben="",
    stichwoerter="teures Granulat soll nicht ohne Nutzen dauerhaft eingesetzt werden|Fehler erster Art: irrtümlich eine Reduktion annehmen|höchstens 5 %",
    voraussetzungen="Fehler erster Art als kontrollierter Fehler|Nullhypothese als das, was man absichern will",
    format="Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Produktion/Qualität", textumfang="mittel",
    gegeben="Kunststoffteile, 4 % fehlerhaft; die Anzahl fehlerhafter Teile unter zufällig ausgewählten ist binomialverteilt; H0: Anteil mindestens 4 %, getestet mit einer Stichprobe von 500 Teilen auf dem Signifikanzniveau 5 %; das neue Granulat ist teurer",
    gesucht="Überlegung, die zur Wahl der Nullhypothese geführt haben könnte, mit Begründung",
    verfahren="Der teure Wechsel soll nur bei nachgewiesener Verbesserung erfolgen; das Risiko, irrtümlich eine Reduktion anzunehmen, ist durch α begrenzt",
    schritte="1", zahlenraum="Prozent", einheiten="", abhaengig_von="",
    ergebnis="Es soll möglichst vermieden werden, das teurere neue Granulat dauerhaft einzusetzen, obwohl sich der Anteil der fehlerhaften Teile nicht reduziert hat; das Risiko, aufgrund des Testergebnisses irrtümlich von einer Reduktion auszugehen, beträgt höchstens 5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="mit dem Fehler zweiter Art argumentieren",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. AB amtlich: III. Amtlich. " + GETEILT.format("1d") + " Die übernommene Schätzung II der WTR-Zeile weicht vom amtlichen Bereich III ab; nach dem Vorrang des Amtlichen für übernommene Schätzungen (Kern § 5) auf III gesetzt (erste Schätzung: II). Die WTR-Zeile trägt ihre eigene Schätzung mit eigenem Standardbezug und bleibt. Im CAS-Stamm Stichprobe 500 statt 200, für d ohne Belang. CAS-Anteil: keiner.")
row("2018MerhoehtBStochastikCAS1", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeit für drei verschiedene Ergebnisse über Pfadprodukt und Reihenfolgen nachweisen", typ_neben="",
    stichwoerter="P(B) = 1/2, P(R) = 1/3, P(G) = 1/6|3! Reihenfolgen|3! · 1/2 · 1/3 · 1/6 = 1/6",
    voraussetzungen="Sektorwinkel als Wahrscheinlichkeit|Anzahl der Reihenfolgen",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Tabelle", skizze="Tabelle mit den Farben Blau, Rot, Grün und den Mittelpunktswinkeln 180°, 120°, 60°.", kontext="Glücksspiel", textumfang="mittel",
    gegeben=RAD,
    gesucht="Nachweis, dass P(drei verschiedene Farben) = 1/6",
    verfahren="Pfadprodukt mal 3! Reihenfolgen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="3! · 1/2 · 1/3 · 1/6 = 1/6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Reihenfolgen vergessen (1/36)",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. " + GETEILT.format("2a") + " CAS-Anteil: keiner.")
row("2018MerhoehtBStochastikCAS1", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen", typ_neben="",
    stichwoerter="Gewinn: 1/6 · (10 − 5) + 1/6 · (a − 5) + 4/6 · (−5) = 0|a = 20",
    voraussetzungen="Erwartungswert des Gewinns|faires Spiel als Erwartungswert null",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksspiel", textumfang="kurz",
    gegeben=RAD + "; Einsätze und Auszahlungen gleichen sich auf lange Sicht aus",
    gesucht="Auszahlung bei drei verschiedenen Farben",
    verfahren="Erwartungswert des Gewinns gleich null setzen",
    schritte="2", zahlenraum="Bruch|ganz", einheiten="Euro", abhaengig_von="2018MerhoehtBStochastikCAS1-2a",
    ergebnis="1/6 · (10 − 5) + 1/6 · (a − 5) − 4/6 · 5 = 0 ⇔ a = 20 Euro (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Einsatz bei den Auszahlungen nicht abziehen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. " + GETEILT.format("2b") + " CAS-Anteil: keiner.")
row("2018MerhoehtBStochastikCAS1", "c", innen="2", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Sektorwinkel eines Glücksrads aus einer Wahrscheinlichkeitsbedingung berechnen", typ_neben="",
    stichwoerter="geändertes Rad mit vergrößertem blauen Sektor: P(G) = p, P(R) = 2p, P(B) = 1 − 3p|Pfad R–R–B: 2p · 2p · (1 − 3p) = 0,036|p = (√37 + 1)/60 wegen P(B) > 0,5|Blau etwa 233°",
    voraussetzungen="Baumdiagramm mit Parameter lesen|Gleichung dritten Grades mit dem Rechner lösen|Lösung über die Sachbedingung auswählen|Anteil in Winkel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze="Ausschnitt eines dreistufigen Baumdiagramms: vom Start drei Äste (oben unbeschriftet, in der Mitte zu R mit 2p beschriftet, unten zu G); von R ein Ast nach oben (unbeschriftet) und einer zu R; vom zweiten R Äste zu B (daneben die Pfadwahrscheinlichkeit 0,036), zu R und zu G (Ast mit p beschriftet)", kontext="Glücksspiel", textumfang="mittel",
    gegeben=RAD + "; die Sektorgrößen werden geändert, dabei wird der blaue Sektor vergrößert; Baumdiagramm für die drei Drehungen des geänderten Rads: P(R) = 2p, P(G) = p, Pfad Rot–Rot–Blau 0,036",
    gesucht="Größe des Mittelpunktswinkels des blauen Sektors",
    verfahren="P(B) = 1 − 3p; Pfadregel 2p · 2p · (1 − 3p) = 0,036 nach p lösen; die Lösung mit P(B) > 0,5 (Blau vergrößert) wählen; Winkel P(B) · 360°",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="°", abhaengig_von="",
    ergebnis="2p · 2p · (1 − p − 2p) = 0,036 liefert für 0,5 < 1 − p − 2p <= 1: p = (√37 + 1)/60; damit (1 − p − 2p) · 360° ≈ 233° (amtlich)",
    zwischenergebnis="p ≈ 0,118, P(B) ≈ 0,646|weitere positive Lösung p = 0,3 (Blau 36°, verkleinert) entfällt", niveau_geschaetzt="II",
    fehlerquelle="die Lösung p = 0,3 nehmen, bei der der blaue Sektor kleiner wird",
    bemerkung="Standardbezug: K2 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (p = 3/10 und (1 ± √37)/60; 232,5°). Schätzung nicht blind: beim Ansehen von Seite 3 lag der Standardbezug offen, bevor 2 c geschätzt war (Pfadgleichung aufstellen, lösen, Lösung mit vergrößertem Blau wählen: Verkettung, II). Abgewandelt gegenüber 2018MerhoehtBStochastikWTR1, Teilaufgabe 2 c (dort grüner Sektor verkleinert, zwei Drehungen, Pfad R–B 0,14), Typ geteilt. CAS-Anteil: Gleichung dritten Grades mit dem Rechner lösen, Ansatz eigen.")
# ---- Stochastik CAS 2: Geldscheine, 25 BE (Aufgabe 1: umlauffähige Scheine im Café, 7 BE; Aufgabe 2: Behälter mit
# 380 Scheinen, 5 BE; Aufgabe 3: gefälschte Scheine 2015, 5 BE; Aufgabe 4: Test einer Kassiererin, 8 BE)
CAFE = ("Wird den Tageseinnahmen eines Cafés ein Geldschein zufällig entnommen, so ist er mit der Wahrscheinlichkeit 2 % "
        "nicht mehr umlauffähig")
BEH = ("In einem Behälter befinden sich 380 Geldscheine: 44 zu 5 €, 60 zu 10 €, 72 zu 20 €, 204 zu 50 €; sechs davon "
       "sind nicht mehr umlauffähig, darunter zwei mit einem Wert von jeweils 50 €")
BEH_SK = "Tabelle mit zwei Zeilen: Wert des Scheins (5 €, 10 €, 20 €, 50 €) und Anzahl (44, 60, 72, 204)"
EZB = ("In der ersten Hälfte des Jahres 2015 hat die Europäische Zentralbank von etwa 17 Milliarden im Umlauf befindlichen "
       "Geldscheinen insgesamt 454000 gefälschte Scheine aussortiert; Verteilung nach Abbildung 1: 5 €: 6800, 10 €: 10800, "
       "20 €: 248500, 50 €: 142000, 100 €: 38600, 200 €: 5000, 500 €: 2300")
EZB_SK = ("Abbildung 1: Säulendiagramm „Anzahl gefälschter Geldscheine“; waagerecht die Scheinwerte € 5, € 10, € 20, € 50, "
          "€ 100, € 200, € 500, senkrecht die Anzahl von 0 bis 300000 in Schritten von 50000; schwarze Säulen mit "
          "aufgedruckten Werten 6800, 10800, 248500, 142000, 38600, 5000, 2300")
KASSE = ("Eine Kassiererin behauptet, nur durch Tasten und Betrachten erkennen zu können, ob ein Geldschein echt oder "
         "gefälscht ist; ein Kollege legt ihr testweise zehn Geldscheine vor, sie entscheidet für jeden, ob er echt oder "
         "gefälscht ist; wird die Nullhypothese „Die Wahrscheinlichkeit dafür, dass sich die Kassiererin korrekt "
         "entscheidet, beträgt höchstens 50 %.“ auf einem Signifikanzniveau von 5 % abgelehnt, gibt der Kollege seine "
         "Zweifel auf")
GUETE_SK = ("Abbildung 2: Koordinatensystem auf Kästchengitter, waagerecht p von 0,4 bis 0,6 (Teilstriche 0,4; 0,45; 0,5; "
           "0,55; 0,6), senkrecht y von 0 bis etwa 0,28 (Teilstriche 0,05 bis 0,25); steigende, nach links flach "
           "auslaufende Kurve: bei p = 0,4 fast 0, bei p = 0,5 etwa 0,04, bei p = 0,55 etwa 0,12, bei p = 0,58 etwa "
           "0,22, am oberen Rand bei p etwa 0,6")
row("2018MerhoehtBStochastikCAS2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="Y ~ B(200; 0,02)|ausschließlich umlauffähig: P(Y = 0) ≈ 1,8 %|höchstens zwei nicht umlauffähig: P(Y <= 2) ≈ 23,5 %",
    voraussetzungen="Binomialmodell für die Scheine|„ausschließlich umlauffähig“ als null Treffer|kumulierte Wahrscheinlichkeit am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Geldscheine/Café", textumfang="kurz",
    gegeben=CAFE + "; unter den Tageseinnahmen befinden sich insgesamt 200 Geldscheine",
    gesucht="Wahrscheinlichkeit, dass darunter ausschließlich umlauffähige Scheine sind; Wahrscheinlichkeit, dass darunter höchstens zwei nicht mehr umlauffähige Scheine sind",
    verfahren="Y ~ B(200; 0,02) für die nicht mehr umlauffähigen Scheine: P(Y = 0) und P(Y <= 2)",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Y: Anzahl nicht mehr umlauffähiger Geldscheine; P(Y = 0) ≈ 1,8 %, P(Y <= 2) ≈ 23,5 % (n = 200, p = 0,02) (amtlich)",
    zwischenergebnis="P(Y = 0) = 0,98^200 ≈ 0,0176|P(Y <= 2) ≈ 0,2351", niveau_geschaetzt="I",
    fehlerquelle="P(Y < 2) statt P(Y <= 2) berechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,0176; 0,2351). Typ und Nebentyp wiederverwendet. CAS-Anteil: Binomialwerte mit dem Rechner.")
row("2018MerhoehtBStochastikCAS2", "b", innen="1", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln", typ_neben="",
    stichwoerter="Y ~ B(n; 0,02)|P(Y >= 4) > 0,9|n = 332: 89,98 %, n = 333: 90,10 %|mindestens 333 Scheine",
    voraussetzungen="Binomialmodell mit unbekanntem n|„mindestens vier“ als Y >= 4|Probieren am Rechner",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Geldscheine/Café", textumfang="kurz",
    gegeben=CAFE,
    gesucht="Anzahl der Geldscheine, die mindestens zu den Tageseinnahmen gehören müssen, damit darunter mit einer Wahrscheinlichkeit von mehr als 90 % mindestens vier nicht mehr umlauffähige Scheine sind",
    verfahren="Für Y ~ B(n; 0,02) das kleinste n mit P(Y >= 4) > 0,9 durch Probieren mit dem Rechner suchen",
    schritte="3", zahlenraum="Prozent|dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="P(Y >= 4) ≈ 89,98 % für n = 332 und ≈ 90,10 % für n = 333 (p = 0,02); in der Kasse müssen sich mindestens 333 Geldscheine befinden (amtlich)",
    zwischenergebnis="n = 331: 0,8985|n = 332: 0,8998|n = 333: 0,9010", niveau_geschaetzt="III",
    fehlerquelle="über den Erwartungswert n · 0,02 = 4 den Wert n = 200 ansetzen oder P(Y > 4) prüfen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (0,89976; 0,90101). Erste Schätzung: II (Mindestanzahl durch Probieren, wie CAS 1 1 b); korrigiert nach Deutungsliste (f) (iqb.md v1.17 § 7, Beschluss vom 26.09.2026 Punkt 2): Mindestanzahl für eine Mindestwahrscheinlichkeit bestimmen ist III. Typ wiederverwendet (mindestens vier Treffer = mehr als drei). CAS-Anteil: Probieren mit dem Rechner, Ansatz eigen.")
row("2018MerhoehtBStochastikCAS2", "a", innen="2", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben", typ_neben="",
    stichwoerter="Scheine unter 50 €: 44 + 60 + 72 = 176|davon 6 − 2 = 4 nicht umlauffähig|(176 − 4)/380 ≈ 45,3 %",
    voraussetzungen="günstige Fälle aus Tabelle und Text zählen|nicht umlauffähige Scheine abziehen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze=BEH_SK, kontext="Geldscheine/Behälter", textumfang="kurz",
    gegeben=BEH + "; ein Geldschein wird zufällig entnommen",
    gesucht="Wahrscheinlichkeit, dass der Schein einen Wert unter 50 € hat und umlauffähig ist",
    verfahren="Günstig sind die umlauffähigen Scheine unter 50 €: 176 Scheine unter 50 €, davon 4 nicht umlauffähig; Anteil an 380",
    schritte="2", zahlenraum="Prozent|ganz", einheiten="", abhaengig_von="",
    ergebnis="(176 − 4)/380 ≈ 45,3 % (amtlich)",
    zwischenergebnis="172/380 ≈ 0,4526", niveau_geschaetzt="II",
    fehlerquelle="alle sechs nicht umlauffähigen Scheine abziehen (170/380)",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,4526). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBStochastikCAS2", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="(6 über 2) · (374 über 5)/(380 über 7)|sieben Scheine ohne Zurücklegen|genau zwei nicht umlauffähig",
    voraussetzungen="hypergeometrischen Term lesen|Ziehen ohne Zurücklegen als Zufallsexperiment",
    format="Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text",
    material="Tabelle", skizze=BEH_SK, kontext="Geldscheine/Behälter", textumfang="kurz",
    gegeben=BEH + "; Term (6 über 2) · (374 über 5)/(380 über 7)",
    gesucht="im Sachzusammenhang ein Zufallsexperiment, bei dem die Wahrscheinlichkeit eines Ereignisses mit dem Term berechnet werden kann; dieses Ereignis",
    verfahren="380 Scheine insgesamt, 7 gezogen; 6 nicht umlauffähige, davon 2 gezogen; 374 umlauffähige, davon 5 gezogen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Zufallsexperiment: Aus dem Behälter werden sieben Geldscheine zufällig entnommen; Ereignis: Von den entnommenen Scheinen sind zwei nicht mehr umlauffähig (amtlich)",
    zwischenergebnis="Termwert ≈ 0,0041", niveau_geschaetzt="II",
    fehlerquelle="Ziehen mit Zurücklegen beschreiben oder „mindestens zwei“ statt „genau zwei“ angeben",
    bemerkung="Standardbezug: K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Termwert 0,00415). Typ wiederverwendet (Zufallsexperiment und Ereignis beschreiben). CAS-Anteil: keiner.")
row("2018MerhoehtBStochastikCAS2", "a", innen="3", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="X: Wert eines zufällig ausgewählten gefälschten Scheins|Anzahlen aus dem Säulendiagramm durch 454000|E(X) ≈ 40 €",
    voraussetzungen="relative Häufigkeiten als Wahrscheinlichkeiten|Werte aus einem Säulendiagramm ablesen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=EZB_SK, kontext="Geldscheine/Fälschungen", textumfang="kurz",
    gegeben=EZB + "; einer der aussortierten gefälschten Scheine wird zufällig ausgewählt; X beschreibt seinen Wert in Euro",
    gesucht="Erwartungswert von X",
    verfahren="Werte mit den Anzahlen gewichten, summieren und durch 454000 teilen",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="Euro", abhaengig_von="",
    ergebnis="1/454000 · (6800 · 5 € + 10800 · 10 € + 248500 · 20 € + 142000 · 50 € + 38600 · 100 € + 5000 · 200 € + 2300 · 500 €) ≈ 40 € (amtlich)",
    zwischenergebnis="Summe 18222000 €|E(X) = 9111/227 ≈ 40,14", niveau_geschaetzt="I",
    fehlerquelle="das arithmetische Mittel der sieben Scheinwerte bilden oder durch 17 Milliarden teilen",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (40,14; die Anzahlen ergeben 454000). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2018MerhoehtBStochastikCAS2", "b", innen="3", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Aussage über Wahrscheinlichkeiten aus absoluten Anzahlen ohne Grundgesamtheit beurteilen", typ_neben="",
    stichwoerter="Aussage: 20-€-Schein fast doppelt so oft gefälscht wie 50-€-Schein|Diagramm zeigt nur Anzahlen der Fälschungen|Umlaufzahlen je Scheinwert fehlen|Aussage falsch",
    voraussetzungen="Wahrscheinlichkeit als Anteil an der jeweiligen Grundgesamtheit|absolute und relative Häufigkeit unterscheiden",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Diagramm", skizze=EZB_SK, kontext="Geldscheine/Fälschungen", textumfang="mittel",
    gegeben=EZB + "; Aussage: aus Abbildung 1 lässt sich schließen, dass die Wahrscheinlichkeit, dass ein unter allen umlaufenden Scheinen zufällig ausgewählter 20-€-Schein gefälscht ist, fast doppelt so hoch war wie bei einem zufällig ausgewählten 50-€-Schein",
    gesucht="Beurteilung der Aussage",
    verfahren="Die Wahrscheinlichkeit, dass ein 20-€-Schein gefälscht ist, ist der Anteil der Fälschungen an allen umlaufenden 20-€-Scheinen; die Abbildung nennt nur die Anzahl der Fälschungen, nicht die Zahl der umlaufenden Scheine je Wert",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Die Aussage ist falsch: der beschriebene Zusammenhang zwischen gefälschten 20-€-Scheinen und gefälschten 50-€-Scheinen lässt sich aus der Abbildung nicht schließen, da nicht angegeben ist, wie viele Scheine dieser Werte 2015 jeweils im Umlauf waren (amtlich)",
    zwischenergebnis="248500/142000 ≈ 1,75 ist nur das Verhältnis der Fälschungsanzahlen", niveau_geschaetzt="II",
    fehlerquelle="das Verhältnis 248500 : 142000 ≈ 1,75 als Verhältnis der Wahrscheinlichkeiten nehmen und die Aussage bestätigen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Verhältnis 1,75 der Anzahlen). Neuer Typ: vorhandene Beurteilungstypen prüfen eine Aussage an gegebenen Wahrscheinlichkeiten, hier fehlt die Grundgesamtheit, und die Aussage ist aus absoluten Anzahlen nicht zu entscheiden. CAS-Anteil: keiner.")
row("2018MerhoehtBStochastikCAS2", "a", innen="4", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel eines einseitigen Signifikanztests bestimmen", typ_neben="",
    stichwoerter="Z: Anzahl korrekter Entscheidungen, H0: p <= 0,5, n = 10, α = 5 %|rechtsseitig: P(Z >= k) <= 0,05|Ablehnung ab neun korrekten Entscheidungen",
    voraussetzungen="Ablehnungsbereich rechts|kumulierte Wahrscheinlichkeit gegen α",
    format="Rechnung", operator="Bestimmen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bank/Echtheitsprüfung", textumfang="mittel",
    gegeben=KASSE,
    gesucht="zugehörige Entscheidungsregel",
    verfahren="Kleinstes k mit P(Z >= k) <= 0,05 für Z ~ B(10; 0,5)",
    schritte="2", zahlenraum="Prozent|ganz", einheiten="", abhaengig_von="",
    ergebnis="Z: Anzahl der korrekten Entscheidungen; P(Z >= k) <= 0,05 (n = 10, p = 0,5); trifft die Kassiererin für mindestens neun Scheine die korrekte Entscheidung, so wird die Nullhypothese abgelehnt (amtlich)",
    zwischenergebnis="P(Z >= 8) ≈ 0,055|P(Z >= 9) ≈ 0,011", niveau_geschaetzt="II",
    fehlerquelle="k = 8 wählen, weil 0,055 gerundet 5 % ergibt",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,0547; 0,0107). Typ wiederverwendet (hier rechtsseitig). CAS-Anteil: kumulierte Werte mit dem Rechner.")
row("2018MerhoehtBStochastikCAS2", "b", innen="4", seite="2|3", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Fehler zweiter Art aus dem Graphen der Ablehnwahrscheinlichkeit ermitteln", typ_neben="",
    stichwoerter="Fehler zweiter Art: H0 falsch (p > 0,5), aber nicht abgelehnt|für p = 0,58: Ablehnwahrscheinlichkeit etwa 0,22|Fehler zweiter Art etwa 0,78",
    voraussetzungen="Fehler zweiter Art als Gegenwahrscheinlichkeit der Ablehnung|zulässiges p wählen|Wert am Graphen ablesen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze=GUETE_SK, kontext="Bank/Echtheitsprüfung", textumfang="mittel",
    gegeben=KASSE + "; bei einem weiteren Test mit unveränderter Nullhypothese und unverändertem Signifikanzniveau werden n Scheine vorgelegt; p ist die Wahrscheinlichkeit einer richtigen Entscheidung bei einem Schein; Abbildung 2 zeigt für ein bestimmtes n die Wahrscheinlichkeit, dass das Testergebnis im Ablehnungsbereich liegt, in Abhängigkeit von p",
    gesucht="für ein geeignet gewähltes Beispiel mithilfe von Abbildung 2 die Wahrscheinlichkeit für den zugehörigen Fehler zweiter Art",
    verfahren="Ein p > 0,5 wählen (dann ist die Nullhypothese falsch), die Ablehnwahrscheinlichkeit an der Kurve ablesen und den Fehler zweiter Art als Gegenwahrscheinlichkeit bilden",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Beispiel p = 58 %: die Wahrscheinlichkeit für den zugehörigen Fehler zweiter Art beträgt etwa 1 − 22 % = 78 %; p muss größer als 50 % gewählt werden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="p <= 0,5 wählen, wo die Nullhypothese wahr ist, oder den abgelesenen Wert selbst als Fehler zweiter Art angeben",
    bemerkung="Standardbezug: K2 III, K4 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Ablesung etwa 0,22 bei p = 0,58; die Kurve passt etwa zu n = 30 mit Ablehnung ab 20 korrekten Entscheidungen: 0,049 bei p = 0,5, 0,220 bei p = 0,58). Eichregel: (d) Güte aus der Abbildung ablesen und als Gegenwahrscheinlichkeit zum Fehler zweiter Art deuten, verkettet mit der Wahl eines zulässigen p. Typ wiederverwendet. CAS-Anteil: keiner.")
NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Integralwert: Flächenstück zu einer Summe aus Integralen und Rechteck am Graphen markieren und Summanden zuordnen", "Analysis", "Flächeninhalt durch Integration",
     "Zu einem vorgegebenen Term aus Integralen und einem Rechteckinhalt ein passendes Flächenstück am Graphen markieren, jedem Summanden einen Teil davon zuordnen und den Inhalt angeben.", "2018MerhoehtBAnalysisCAS1-1b"),
    ("Rechten Winkel in einem Dreieck aus Scharpunkten für bestimmte Ecken und Parameterbereiche ausschließen", "Analysis", "Funktionsscharen und Ortskurven",
     "Für ein Dreieck aus Punkten des Graphen einer Schar begründen, dass an bestimmten Ecken oder für bestimmte Parameterbereiche kein rechter Winkel liegen kann, etwa über die Lage der Punkte auf dem Graphen oder einen stumpfen Innenwinkel.", "2018MerhoehtBAnalysisCAS1-1f"),
    ("Ansätze für einen rechten Winkel in einem Dreieck aus Scharpunkten über Skalarprodukt und Steigungsprodukt erläutern", "Analysis", "Funktionsscharen und Ortskurven",
     "Vorgegebene Gleichungen als Skalarprodukt der Verbindungsvektoren gleich null bzw. als Produkt der Geradensteigungen gleich −1 erkennen und als Bedingung für einen rechten Winkel in einem Dreieck aus Scharpunkten erläutern.", "2018MerhoehtBAnalysisCAS1-1g"),
    ("Integral der Geschwindigkeit als zurückgelegten Weg im Sachzusammenhang deuten", "Analysis", "Rekonstruktion von Beständen",
     "Ein Integral über eine Geschwindigkeitsfunktion ohne Berechnung als den in diesem Zeitraum zurückgelegten Weg (etwa die Länge einer Flugbahn) im Sachzusammenhang deuten.", "2018MerhoehtBAnalysisCAS1-2c"),
    ("Nullstellen und Werte: y-Achsenschnittpunkt angeben und Anzahl der Nullstellen aus Grenzverhalten und Tiefpunkt ohne Rechnung begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den Schnittpunkt mit der y-Achse angeben und die Anzahl der Nullstellen ohne Rechnung aus dem Verhalten im Unendlichen und der Lage eines Extrempunkts zur x-Achse begründen.", "2018MerhoehtBAnalysisCAS2-1b"),
    ("Extremstelle zwischen zwei Stellen mit gleichem Funktionswert ohne Rechnung begründen", "Analysis", "Kurvenuntersuchung",
     "Aus zwei Stellen, an denen eine ganzrationale (stetig differenzierbare) Funktion denselben Wert annimmt, ohne Rechnung auf mindestens eine Extremstelle dazwischen schließen.", "2018MerhoehtBAnalysisCAS2-1d"),
    ("Differenzen- und Differentialquotient durch Sekante und Tangente veranschaulichen und im Sachzusammenhang deuten", "Analysis", "Ableitung und Änderungsrate",
     "Einen Differenzenquotienten als Sekante und den Grenzwert eines Differenzenquotienten als Tangente in eine Abbildung einzeichnen und als mittlere bzw. momentane Änderungsrate im Sachzusammenhang deuten.", "2018MerhoehtBAnalysisCAS2-2c"),
    ("Transformation: Verschiebung für einen Anschluss mit gleichem Funktionswert und gleicher Steigung beschreiben und Funktionsterm angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Eine Verschiebung eines Graphen in x- und y-Richtung so wählen und beschreiben, dass der verschobene Graph an einer Stelle mit gleichem Funktionswert und gleicher Steigung an einen anderen Graphen anschließt, und den Funktionsterm angeben.", "2018MerhoehtBAnalysisCAS2-2g"),
    ("Stellen, deren Tangente die y-Achse oberhalb einer Schranke schneidet, über eine Ungleichung bestimmen", "Analysis", "Tangente, Normale, Schnittwinkel", "Den y-Achsenabschnitt der Tangente an einer allgemeinen Stelle c als Term f(c) − c · f'(c) aufstellen und die Stellen c bestimmen, für die er eine vorgegebene Schranke übertrifft, indem die Ungleichung gelöst wird.", "2018MerhoehtBAnalysisCAS3-1d"),
    ("Parameterwerte für mehr als einen gemeinsamen Punkt zweier Graphen über die Lösbarkeit der Schnittgleichung bestimmen", "Analysis", "Funktionsscharen und Ortskurven", "Die Schnittgleichung eines Scharmitglieds mit einem festen Graphen in Abhängigkeit vom Parameter lösen und aus der Lösbarkeit der entstehenden Gleichung (etwa x^2 gleich einem Term im Parameter) die Parameterwerte angeben, für die es mehr als einen gemeinsamen Punkt gibt.", "2018MerhoehtBAnalysisCAS3-1f"),
    ("Integralwert: Gewichtetes Mittel zweier Teilintegrale als Mittelwert über die Vorzeichenbereiche der Differenz begründen", "Analysis", "Flächeninhalt durch Integration", "Einen zusammengesetzten Term aus zwei Integralmittelwerten mit Gewichten erklären: die Differenz zweier Funktionen wechselt an einer Schnittstelle das Vorzeichen, die Teilterme sind die mittleren Abweichungen auf den Teilintervallen, die Gewichte deren Anteile an der Gesamtlänge.", "2018MerhoehtBAnalysisCAS3-1h"),
    ("Zwei Parameter einer Funktion aus einer vorgegebenen Bogenlängenformel und einem Punkt bestimmen", "Analysis", "Rekonstruktion von Funktionsgleichungen", "Eine vorgegebene Formel für die Länge eines Graphenstücks mit einer bekannten Länge gleichsetzen und nach dem einen Parameter (mit dem Rechner) lösen, danach den zweiten Parameter aus einem bekannten Punkt des Graphen bestimmen.", "2018MerhoehtBAnalysisCAS3-2e"),
    ("Lage zweier Graphen mit gemeinsamen Endpunkten über die Steigungen in den Endpunkten begründen", "Analysis", "Tangente, Normale, Schnittwinkel", "Für zwei Graphen mit gemeinsamen Endpunkten die Steigungen dort vergleichen, daraus die Lage nahe den Endpunkten erschließen und mit einem Funktionswertvergleich im Inneren begründen, dass keiner der Graphen vollständig oberhalb oder unterhalb des anderen verläuft.", "2018MerhoehtBAnalysisCAS3-2f"),
    ("Übergangsprozess: Nichtnegativen stationären Vektor für alle Parameterwerte nachweisen und ein ganzzahliges Beispiel deuten", "Analytische Geometrie", "Matrizen und Übergangsprozesse", "Für eine Übergangsmatrix mit Parameter den stationären Vektor mit vorgegebener Summe allgemein bestimmen, die Nichtnegativität aller Komponenten für den ganzen Parameterbereich nachweisen und für einen geeignet gewählten Parameterwert einen ganzzahligen Vektor angeben und als gleichbleibende Verteilung deuten.", "2018MerhoehtBAGLAA1CAS1-1h"),
    ("Übergangsprozess: Aussage über laufende gegenüber einmaliger Entnahme im Sachzusammenhang beurteilen", "Analytische Geometrie", "Matrizen und Übergangsprozesse", "Eine Aussage beurteilen, ob wiederholte Entnahmen nach jedem Übergang zum selben Zustand führen wie eine gleich große einmalige Entnahme am Ende, und das Urteil mit der Wirkung der entnommenen Individuen auf die folgenden Übergänge begründen.", "2018MerhoehtBAGLAA1CAS2-2b"),
    ("Lage des Schattens einer Pyramidenspitze über den Vergleich von Kantenneigung und Lichteinfall begründen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Begründen, unter welcher Bedingung der Schatten der Spitze einer Pyramide bei parallelem Licht auf den Untergrund fällt, indem der Neigungswinkel der in Lichtrichtung liegenden Kante mit dem Einfallswinkel des Lichts gegen den Untergrund verglichen wird.", "2018MerhoehtBAGLAA2CAS2-1f"),
    ("Höhe einer Spitze aus dem Abstand ihres Schattenpunkts zu einem Punkt bestimmen", "Analytische Geometrie", "Schnittmengen",
     "Den Schattenpunkt einer Spitze mit unbekannter Höhe als Schnittpunkt der Lichtgeraden mit der Grundebene in Abhängigkeit von der Höhe bestimmen und die Höhe aus dem vorgegebenen Abstand dieses Schattenpunkts zu einem festen Punkt berechnen.", "2018MerhoehtBAGLAA2CAS2-1g"),
    ("Laplace-Experiment: Aussage über Wahrscheinlichkeiten aus absoluten Anzahlen ohne Grundgesamtheit beurteilen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Eine Aussage über das Verhältnis zweier Wahrscheinlichkeiten beurteilen, die aus absoluten Anzahlen (etwa eines Säulendiagramms) gezogen wird, und begründen, dass sie ohne die Größe der jeweiligen Grundgesamtheit nicht folgt.", "2018MerhoehtBStochastikCAS2-3b"),
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
        # v1.10: Stapel mit dokumentierter Unterschreitung der Eichschwelle – Warnung, kein Fehler;
        # die Eichung wird aus dem Bestand gerechnet und mit dem Listenwert verglichen (nur Meldung).
        for s, (t_liste, n_liste, beleg) in sorted(EICHUNG_UNTERSCHRITTEN.items()):
            zs = [z for z in alt if kennung_aus_id(z["id"])[0] in QUELLE
                  and einheit(QUELLE[kennung_aus_id(z["id"])[0]]) == s]
            t_ist, _, n_ist = eichung(zs, eng=True)
            if not n_ist:
                print(f"Warnung: Stapel {s} steht in EICHUNG_UNTERSCHRITTEN, hat im Bestand aber keine gewertete Zeile")
                continue
            print(f"Warnung: Stapel {s} mit dokumentierter Unterschreitung der Eichschwelle ({beleg}): "
                  f"Eichung (enge Fassung) im Bestand {t_ist} von {n_ist} ({100 * t_ist / n_ist:.1f} %), Schwelle "
                  f"{100 * SCHWELLEN['eichung_mindestens']:.0f} % unverändert"
                  + ("" if (t_ist, n_ist) == (t_liste, n_liste)
                     else f"; Listenwert {t_liste} von {n_liste} weicht vom Bestand ab"))
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
    doku = EICHUNG_UNTERSCHRITTEN.get(stapel)  # v1.10: dokumentierte Unterschreitung, Schwelle unverändert
    if gew >= SCHWELLEN["eichung_ab_zeilen"]:
        if treffer_eng / gew < SCHWELLEN["eichung_mindestens"] and doku and doku[:2] == (treffer_eng, gew):
            warnung.append(f"Eichung (enge Fassung) {treffer_eng} von {gew} ({100 * treffer_eng / gew:.1f} %) unter "
                           f"der Schwelle {100 * SCHWELLEN['eichung_mindestens']:.0f} % – dokumentierte "
                           f"Unterschreitung nach {doku[2]} (EICHUNG_UNTERSCHRITTEN), Schwelle unverändert; "
                           f"Abweichungen: {'; '.join(abw_eng)}")
        else:
            a(treffer_eng / gew >= SCHWELLEN["eichung_mindestens"],
              f"Schwelle gerissen: Eichung (enge Fassung) {treffer_eng} von {gew} "
              f"({100 * treffer_eng / gew:.0f} %), verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %"
              + (f" (EICHUNG_UNTERSCHRITTEN nennt {doku[0]} von {doku[1]}, gemessen {treffer_eng} von {gew})"
                 if doku else "") + f": {'; '.join(abw_eng)}")
            if doku and treffer_eng / gew >= SCHWELLEN["eichung_mindestens"]:
                warnung.append(f"Stapel {stapel} steht in EICHUNG_UNTERSCHRITTEN, erreicht die Schwelle aber "
                               f"({treffer_eng} von {gew}) – Eintrag streichen")
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
