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
    "stapel": "2017-ga-B-cas",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dateidublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll. Delta-Stapel: keine Dateidublette; Aufgabendublette Stochastik CAS
    # Aufgabe 1 (= Stochastik WTR 1 Aufgabe 1, 5 BE) ohne Zeile, Soll 15 statt 20;
    # AG/LA (A2) CAS 1 druckt die Summe 25, die Teilaufgaben ergeben 20 (Soll 20).
    "soll": {
        "2017MgrundlegendBAnalysisCAS": 40, "2017MgrundlegendBAGLAA1CAS": 20,
        "2017MgrundlegendBAGLAA2CAS1": 20, "2017MgrundlegendBAGLAA2CAS2": 20,
        "2017MgrundlegendBStochastikCAS": 15,
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
# Stapel 2017-ga-B, CAS-Zweig – Delta-Stapel zum WTR-Zweig (Auftrag Nacht 2026-09-29, Teil 4, vor dem Nachtrag der Berliner
# CAS-Hefte; Regel „Eine Vormerkung überlebt keinen Auftrag“ und „MMS/CAS als Delta“, iqb.md § 7). Anlass: 2017-be-gk-cas 3.1
# ist wortgleich mit Stochastik CAS (Heft 3.1 e = Pool 2 c, g = 2 e; befund-cas-berlin-2026-09-28.md). iqb-quellen.csv führt
# für keine der fünf CAS-Dateien eine dateidublette_von (nachgemessen am Text: Analysis CAS und AG/LA (A2) CAS 1, 2 sind
# andere Aufgaben als die WTR-Dateien, zu AG/LA (A1) CAS gibt es keine WTR-Datei, Stochastik CAS weicht von WTR 1 in 2 e ab).
# Aufgabendublette: Stochastik CAS Aufgabe 1 (a, b) = Stochastik WTR 1 Aufgabe 1, keine Zeile, Soll 15 statt 20.
# Geteilt mit Stochastik WTR 1: 2 a–d (Felder übernommen, GETEILT). Wortgleich mit dem Pool 2017 erhöht (andere
# Trägeraufgabe, geteilter Typ): AG/LA (A1) CAS 1 a, c, e, f (= 2017MerhoehtBAGLAA1WTR 1 a, d, e, f), AG/LA (A2) CAS 1 a–c
# (= 2017MerhoehtBAGLAA2WTR1 und CAS1 1 a–c). 5 Dateien, 115 BE, 38 Zeilen. Schätzungen blind vor Erwartungshorizont und
# Standardbezug (erster Stand 28 von 38), nach Prüfung der Abweichungen 33 von 38 (Korrekturen mit Regel in bemerkung).
# ---- Analysis CAS: Temperaturverlauf beim Erhitzen, Halten und Abkühlen, 40 BE (Aufgabe 1: gesteuerter Vorgang f und
# Abkühlen h, 23 BE; Aufgabe 2: Schar f_k, 17 BE)
TEMP = ("In einem Produktionsprozess werden Flüssigkeiten erhitzt, eine Zeit lang bei konstanter Temperatur gehalten und "
        "anschließend wieder abgekühlt; bei einem durchgehend gesteuerten Vorgang beschreibt f(t) = 23 + 20 · t · e^(−t/10) "
        "(t in Minuten seit Beginn, f(t) in °C) den Temperaturverlauf während des Erhitzens und des Abkühlens modellhaft")
MESS = ("; Messwerte (Zeit in Minuten: Temperatur in °C): 0: 23,0; 2: 54,0; 4: 76,9; 10: 76,8; 15: 77,3; 20: 76,8; "
        "40: 37,9; 60: 26,0; 80: 23,2")
MESS_SK = ("Tabelle mit zwei Zeilen: Zeit in Minuten (0, 2, 4, 10, 15, 20, 40, 60, 80) und Temperatur in °C (23,0; 54,0; "
           "76,9; 76,8; 77,3; 76,8; 37,9; 26,0; 23,2)")
ABK = ("; betrachtet wird nun ein Vorgang, bei dem die Steuerung zwanzig Minuten nach Beginn abgeschaltet wird; das "
       "anschließende Abkühlen beschreibt für t >= 20 die Funktion h mit h(t) = 23 + b · e^(c · t) und b, c ∈ IR")
F_SK = ("zu erstellende Skizze (Erwartungshorizont): Koordinatensystem auf Kästchengitter, t von 0 bis 80, y von 0 bis 100; "
        "Graph beginnt bei (0; 23), steigt steil auf den Hochpunkt (10; 96,6), fällt danach flacher (bei t = 40 etwa 38) und "
        "nähert sich bis t = 80 der Geraden y = 23")
FK = ("Die Steuerung kann so variiert werden, dass sich der Temperaturverlauf für t >= 0 durch eine der Funktionen f_k mit "
      "f_k(t) = 23 + 20 · t · e^(−k · t/10) und k ∈ IR+ beschreiben lässt (t in Minuten seit Beginn, f_k(t) in °C)")
ABB1_SK = ("Abbildung 1: Koordinatensystem auf Kästchengitter, t von 0 bis 60 (Beschriftung 0, 10, …, 60), y von 0 bis 160 "
           "(Beschriftung 20, 40, …, 160); vier Graphen, alle beginnend bei (0; 23): A mit Hochpunkt bei etwa (2; 38), danach "
           "rasch auf etwa 23 fallend; B mit Hochpunkt bei etwa (5; 60), danach fallend und ab etwa t = 40 nahe 23; C mit "
           "Hochpunkt bei etwa (20; 170), danach langsam fallend auf etwa 75 bei t = 60; D mit Hochpunkt bei etwa (25; 145), "
           "danach steil fallend, schneidet die t-Achse bei etwa t = 55 und verläuft darunter weiter")
ABB2_SK = ("Abbildung 2: Koordinatensystem auf Kästchengitter, waagerecht Zeit in Minuten von 0 bis 12, senkrecht "
           "Änderungsrate in Grad pro Minute von −2 bis 6; der Graph beginnt bei (0; 0), steigt steil auf ein Maximum von etwa "
           "5,5 bei t ≈ 1,6, fällt, schneidet die Zeitachse bei t = 4, erreicht ein Minimum von etwa −1,8 bei t ≈ 6 und "
           "nähert sich danach von unten langsam der Zeitachse")
row("2017MgrundlegendBAnalysisCAS", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Prozentuale Abweichung eines Modellwerts vom Messwert berechnen", typ_neben="",
    stichwoerter="f(0) = 23, Abweichung 0 %|f(2) ≈ 55,7|(f(2) − 54,0)/54,0 ≈ 3,2 %",
    voraussetzungen="Funktionswert einer e-Funktion berechnen|relative Abweichung auf den Messwert beziehen",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze=MESS_SK, kontext="Produktion/Temperaturverlauf", textumfang="mittel",
    gegeben=TEMP + MESS,
    gesucht="Temperaturen, die f für den Beginn des Vorgangs und für den Zeitpunkt zwei Minuten danach liefert; jeweils die prozentuale Abweichung von den Messwerten",
    verfahren="f(0) und f(2) berechnen; Abweichung als (f(2) − 54,0)/54,0 in Prozent",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="°C", abhaengig_von="",
    ergebnis="f(0) = 23, Abweichung 0 %; f(2) ≈ 55,7, (f(2) − 54,0)/54,0 ≈ 3,2 % (amtlich)",
    zwischenergebnis="f(2) = 23 + 40 · e^(−0,2) ≈ 55,75", niveau_geschaetzt="I",
    fehlerquelle="die Abweichung auf den Modellwert statt auf den Messwert beziehen oder nur die Differenz in °C angeben",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (55,749; 3,24 %). Typ wiederverwendet. CAS-Anteil: Funktionswerte mit dem Rechner.")
row("2017MgrundlegendBAnalysisCAS", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt eines Produkts aus Polynom und e-Funktion berechnen", typ_neben="",
    stichwoerter="f'(t) = 2 · (10 − t) · e^(−t/10)|einzige Nullstelle t = 10, f''(10) ≠ 0|f(10) = 23 + 200/e ≈ 96,6|deutlich über allen Messwerten",
    voraussetzungen="Produkt- und Kettenregel|e-Faktor stets positiv|hinreichende Bedingung",
    format="Begründung|Rechnung", operator="Zeigen Sie|vergleichen Sie", antwort="Text|Zahl",
    material="Tabelle", skizze=MESS_SK, kontext="Produktion/Temperaturverlauf", textumfang="mittel",
    gegeben=TEMP + MESS,
    gesucht="Nachweis, dass der Graph von f genau einen Extrempunkt hat; Vergleich der zugehörigen Temperatur mit den Messwerten",
    verfahren="f'(t) = 2 · (10 − t) · e^(−t/10) ist nur für t = 10 null, f''(10) ≠ 0; f(10) berechnen und mit den Messwerten (höchstens 77,3 °C) vergleichen",
    schritte="3", zahlenraum="dezimal", einheiten="°C", abhaengig_von="",
    ergebnis="f'(t) = 0 ⇔ t = 10, f''(10) ≠ 0; f(10) ≈ 96,6; die Temperatur von etwa 96,6 °C ist deutlich größer als die Messwerte (amtlich)",
    zwischenergebnis="f''(10) = −2/e ≈ −0,74|f(10) = 23 + 200/e", niveau_geschaetzt="I",
    fehlerquelle="nur f'(10) = 0 zeigen, ohne weitere Nullstellen der Ableitung auszuschließen, oder f(10) nur mit dem Messwert bei t = 10 vergleichen",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (f''(10) = −2/e ≈ −0,736; f(10) ≈ 96,58). Erste Schätzung: II (als Verkettung gewertet); korrigiert nach der Grundregel der engen Fassung (iqb.md § 7: I bleibt die einzelne Rechnung, auch wenn sie begründet wird): der Extrempunkt über f' = 0 und f'' ist das Standardverfahren des Typs, keine Verkettung zweier Verfahren, der Vergleich mit den Messwerten eine einzelne Beobachtung (Zeilen des Typs im grundlegenden Niveau, 2017-ga-B WTR, 2020-ga-B und 2025-ga-B: geschätzt I, amtlich I). Typ wiederverwendet. CAS-Anteil: Ableitung und Gleichung mit dem Rechner.")
row("2017MgrundlegendBAnalysisCAS", "c", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen einer Funktion in ein Koordinatensystem einzeichnen", typ_neben="Verlauf eines Graphen im Sachzusammenhang beschreiben",
    stichwoerter="Skizze für 0 <= t <= 80|Hochpunkt (10; 96,6)|für große t Annäherung an y = 23|Temperatur nähert sich 23 °C",
    voraussetzungen="Graph mit dem Rechner darstellen und übertragen|Grenzwert von t · e^(−t/10)|Asymptote im Sachzusammenhang",
    format="Zeichnen|Kurzantwort", operator="Skizzieren Sie|Beschreiben Sie|deuten Sie", antwort="Grafik|Text",
    material="Koordinatensystem", skizze=F_SK, kontext="Produktion/Temperaturverlauf", textumfang="mittel",
    gegeben=TEMP,
    gesucht="Skizze des Graphen von f für 0 <= t <= 80; Beschreibung des Verlaufs für große t und Deutung im Sachzusammenhang",
    verfahren="Graph mit dem Rechner darstellen und skizzieren; 20 · t · e^(−t/10) geht für große t gegen 0, der Graph nähert sich y = 23; die Flüssigkeit kühlt auf 23 °C ab",
    schritte="2", zahlenraum="dezimal", einheiten="°C", abhaengig_von="",
    ergebnis="Skizze im Erwartungshorizont; für große Werte von t nähert sich der Graph von f der Geraden mit der Gleichung y = 23 an, die Temperatur der Flüssigkeit also mit der Zeit 23 °C (amtlich)",
    zwischenergebnis="f(40) ≈ 37,7|f(80) ≈ 23,5", niveau_geschaetzt="I",
    fehlerquelle="den Graphen gegen 0 statt gegen 23 laufen lassen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich (Skizze im Erwartungshorizont), eigene Rechnung bestätigt (Grenzwert 23; f(80) ≈ 23,54). Die Teilaufgabe verlangt selbst eine Skizze; skizze beschreibt die zu erstellende Darstellung nach dem Erwartungshorizont. Erste Schätzung: II (als Verkettung mit Deutung gewertet); korrigiert nach der Grundregel der engen Fassung (iqb.md § 7): Skizze mit dem Rechner, Grenzverhalten und die einfache Deutung als Endtemperatur sind einzelne Beobachtungen nebeneinander, keine Kette, in der ein Ergebnis das nächste speist (Typ im Pool dreimal geschätzt I, amtlich I; Nebentyp 2018-ga-B und 2018-ea-B: I). Typ und Nebentyp wiederverwendet. CAS-Anteil: Graph mit dem Rechner.")
row("2017MgrundlegendBAnalysisCAS", "d", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Intervall, in dem eine Modellfunktion mindestens einen vorgegebenen Wert annimmt, über eine Ungleichung bestimmen",
    typ_neben="Graphen einer Funktion in ein Koordinatensystem einzeichnen",
    stichwoerter="f(t) >= 77|t1 ≈ 4,0 und t2 ≈ 20,0|Haltephase als waagerechte Strecke bei 77 °C",
    voraussetzungen="Ungleichung über die Schnittstellen mit y = 77 lösen|Modell im Sachzusammenhang abändern",
    format="Rechnung|Zeichnen", operator="Bestimmen Sie|stellen Sie dar", antwort="Zahl|Grafik",
    material="Koordinatensystem",
    skizze="zu ergänzende Darstellung (Erwartungshorizont): im Koordinatensystem aus Teilaufgabe c verläuft die Temperatur entlang des Graphen von f bis (4,0; 77), dann waagerecht bei 77 bis (20,0; 77) und danach wieder entlang des Graphen; der Bogen um den Hochpunkt (10; 96,6) entfällt",
    kontext="Produktion/Temperaturverlauf", textumfang="mittel",
    gegeben=TEMP + "; der Zeitabschnitt, in dem die Flüssigkeit konstant bei 77 °C gehalten wird, entspricht im Modell dem Intervall, in dem f mindestens diese Temperatur liefert",
    gesucht="Zeitabschnitt der Haltephase; Darstellung des zugehörigen Temperaturverlaufs im Koordinatensystem aus Teilaufgabe c",
    verfahren="f(t) >= 77 mit dem Rechner lösen (Schnittstellen von f mit y = 77); im Intervall den Graphen durch die waagerechte Strecke y = 77 ersetzen",
    schritte="2", zahlenraum="dezimal", einheiten="min|°C", abhaengig_von="2017MgrundlegendBAnalysisCAS-1c",
    ergebnis="f(t) >= 77 liefert den Zeitabschnitt [t1; t2] mit t1 ≈ 4,0 und t2 ≈ 20,0; der Temperaturverlauf folgt dem Graphen bis t1, bleibt bis t2 bei 77 °C und folgt danach wieder dem Graphen (amtlich)",
    zwischenergebnis="t1 ≈ 4,05|t2 ≈ 20,05", niveau_geschaetzt="II",
    fehlerquelle="nur eine Lösung von f(t) = 77 bestimmen oder den Hochpunkt im dargestellten Verlauf stehen lassen",
    bemerkung="Standardbezug: K4 I, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (4,047; 20,050). Neuer Typ: vorhandene Typen berechnen oder lesen eine Stelle zu einem Funktionswert ab, hier ist das ganze Intervall einer Ungleichung gesucht und im Sachzusammenhang als Haltephase dargestellt; Thema Gleichungen lösen (Ungleichung mit dem Rechner). CAS-Anteil: Ungleichung mit dem Rechner lösen.")
row("2017MgrundlegendBAnalysisCAS", "e", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Zwei Parameter einer Exponentialfunktion aus Funktionswert und Änderungsrate an einer Stelle bestimmen", typ_neben="",
    stichwoerter="h(20) = 77|h'(20) = −3,5|b · e^(20c) = 54 und b · c · e^(20c) = −3,5|c = −7/108 ≈ −0,065, b ≈ 197,4",
    voraussetzungen="Ableitung einer e-Funktion mit Parameter|momentane Änderungsrate als Ableitungswert|Gleichungssystem mit zwei Unbekannten",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Temperaturverlauf", textumfang="mittel",
    gegeben=TEMP + ABK + "; zu Beginn des Abkühlens soll die Temperatur 77 °C und die momentane Änderungsrate der Temperatur −3,5 °C pro Minute betragen",
    gesucht="passende Werte von b und c",
    verfahren="h(20) = 77 und h'(20) = b · c · e^(20c) = −3,5 ansetzen; aus b · e^(20c) = 54 folgt 54c = −3,5, also c = −7/108, dann b = 54 · e^(−20c)",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="Aus h(20) = 77 und h'(20) = −3,5 ergibt sich b ≈ 197,4, c ≈ −0,065 (amtlich)",
    zwischenergebnis="b · e^(20c) = 54|c = −7/108 ≈ −0,0648|b ≈ 197,41", niveau_geschaetzt="II",
    fehlerquelle="den Beginn des Abkühlens bei t = 0 statt bei t = 20 ansetzen oder die Änderungsrate positiv einsetzen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (c = −7/108 ≈ −0,0648; b ≈ 197,41). Neuer Typ: vorhanden ist der Exponentialparameter aus der Änderungsrate zum Anfangszeitpunkt allein; hier zwei Parameter aus Funktionswert und Änderungsrate an einer späteren Stelle über ein Gleichungssystem. CAS-Anteil: Gleichungssystem mit dem Rechner lösen.")
row("2017MgrundlegendBAnalysisCAS", "f", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen", typ_neben="",
    stichwoerter="d(t) = f(t) − h(t) für t >= 20|größter Betrag bei t ≈ 25,9|größte Abweichung etwa 2,2 °C",
    voraussetzungen="Differenzfunktion als Abweichung|Extremstelle mit dem Rechner|Betrag und Randverhalten beachten",
    format="Rechnung", operator="Ermitteln Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Temperaturverlauf", textumfang="mittel",
    gegeben=TEMP + ABK + "; b = 197,4 und c = −0,065",
    gesucht="für die Phase des Abkühlens der Zeitpunkt, zu dem die Werte von f und h am stärksten voneinander abweichen, und die zugehörige Abweichung",
    verfahren="Differenzfunktion d(t) = f(t) − h(t) aufstellen; den größten Betrag von d für t >= 20 über d'(t) = 0 mit dem Rechner bestimmen und mit dem Randverhalten vergleichen (d(20) ≈ 0,3, für große t gegen 0)",
    schritte="3", zahlenraum="dezimal", einheiten="min|°C", abhaengig_von="2017MgrundlegendBAnalysisCAS-1e",
    ergebnis="Betrachtet wird d mit d(t) = f(t) − h(t); der Betrag der Funktionswerte von d nimmt für t >= 20 bei t ≈ 25,9 seinen größten Wert an, der größte Wert ist etwa 2,2 (amtlich)",
    zwischenergebnis="d(25,9) ≈ 2,20|d(20) ≈ 0,34|d(80) ≈ −0,55", niveau_geschaetzt="II",
    fehlerquelle="den Hochpunkt von f oder eine Schnittstelle von f und h statt des Maximums der Differenz suchen",
    bemerkung="Standardbezug: K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (t ≈ 25,86; 2,199). Schätzung II (Differenzfunktion aufstellen, Extremstelle mit dem Rechner, Randvergleich – Verkettung, kein Listeneintrag); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt. Typ wiederverwendet (hier ohne vorgegebene Schranke: Zeitpunkt und Wert der größten Abweichung). CAS-Anteil: Extremstelle der Differenzfunktion mit dem Rechner.")
row("2017MgrundlegendBAnalysisCAS", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter den Graphen über die Lage der Hochpunkte zuordnen", typ_neben="",
    stichwoerter="Hochpunkt (10/k; 23 + 200/(e · k))|je größer k, desto früher und niedriger das Maximum|k = 0,5: C, k = 2: B, k = 5: A",
    voraussetzungen="Graphen der Schar mit dem Rechner darstellen|Hochpunkt in Abhängigkeit vom Parameter",
    format="Kurzantwort", operator="Ordnen Sie zu", antwort="Text",
    material="Diagramm", skizze=ABB1_SK, kontext="Produktion/Temperaturverlauf", textumfang="kurz",
    gegeben=FK + "; die Graphen A, B und C in Abbildung 1 gehören jeweils zu einem der Werte k = 0,5, k = 2 und k = 5",
    gesucht="Zuordnung der drei Werte von k zu den Graphen",
    verfahren="Graphen mit dem Rechner darstellen oder die Hochpunkte (10/k; 23 + 200/(e · k)) vergleichen: je größer k, desto früher und niedriger der Hochpunkt",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="k = 0,5: C, k = 2: B, k = 5: A (amtlich)",
    zwischenergebnis="Hochpunkte (20; 170,2), (5; 59,8), (2; 37,7)", niveau_geschaetzt="I",
    fehlerquelle="den größten Parameterwert dem höchsten Graphen zuordnen",
    bemerkung="Standardbezug: K1 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (Hochpunkte bei 170,2; 59,8; 37,7). Typ wiederverwendet. CAS-Anteil: Graphen mit dem Rechner.")
row("2017MgrundlegendBAnalysisCAS", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Graph über eine gemeinsame Eigenschaft aller Scharfunktionen als nicht zur Schar gehörend begründen", typ_neben="",
    stichwoerter="20 · t · e^(−k · t/10) >= 0 für t >= 0|f_k(t) >= 23 für alle k|Graph D fällt unter y = 23",
    voraussetzungen="Vorzeichen eines Produkts mit e-Faktor|Schranke für alle Parameterwerte",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Diagramm", skizze=ABB1_SK, kontext="Produktion/Temperaturverlauf", textumfang="kurz",
    gegeben=FK + "; Graph D in Abbildung 1 fällt nach seinem Hochpunkt bei etwa (25; 145) steil ab und schneidet die t-Achse bei etwa t = 55",
    gesucht="Begründung, dass Graph D zu keiner der Funktionen f_k gehören kann",
    verfahren="Für t >= 0 ist 20 · t · e^(−k · t/10) >= 0, also f_k(t) >= 23; Graph D liegt für große t unter y = 23 (sogar unter der t-Achse)",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Es gilt f_k(t) >= 23 für alle t >= 0; der Graph D liegt für große Werte von t unterhalb der Geraden mit der Gleichung y = 23 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit der Höhe des Hochpunkts argumentieren, die für ein passendes k erreichbar wäre",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich. Neuer Typ: vorhandene Typen ordnen Graphen Parameterwerten zu; hier wird ein Graph über eine allen Scharfunktionen gemeinsame Schranke ausgeschlossen. CAS-Anteil: keiner.")
row("2017MgrundlegendBAnalysisCAS", "c", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für eine vorgegebene Höhe des Hochpunkts berechnen", typ_neben="",
    stichwoerter="f_k'(t) = 0 ⇔ t = 10/k|f_k(10/k) = 23 + 200/(e · k) = 98|k = 8/(3e) ≈ 0,98",
    voraussetzungen="Ableitung einer Schar mit Produkt- und Kettenregel|Höchsttemperatur als Funktionswert am Hochpunkt|Gleichung nach dem Parameter lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Temperaturverlauf", textumfang="kurz",
    gegeben=FK,
    gesucht="Wert von k, für den die Flüssigkeit im Modell eine Höchsttemperatur von 98 °C erreicht",
    verfahren="f_k'(t) = 0 liefert t = 10/k; f_k(10/k) = 23 + 200/(e · k) = 98 nach k lösen",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="f_k'(t) = 0 ⇔ t = 10/k; f_k(10/k) = 98 ⇔ k = 8/(3e) (amtlich)",
    zwischenergebnis="f_k(10/k) = 23 + 200/(e · k)|k ≈ 0,981", niveau_geschaetzt="II",
    fehlerquelle="f_k(t) = 98 ohne die Extremstelle ansetzen",
    bemerkung="Standardbezug: K2 II, K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (k = 8/(3e) ≈ 0,9810). Neuer Typ: vorhandene Typen bestimmen den Scharparameter aus Lage, Abstand oder Fläche der Extrempunkte, keiner aus der vorgegebenen Höhe des Hochpunkts. CAS-Anteil: Ableitung und Gleichung mit dem Rechner.")
row("2017MgrundlegendBAnalysisCAS", "d", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Einzigen Wendepunkt einer Schar nachweisen und angeben",
    typ_neben="Wendepunkt als Zeitpunkt stärkster Zu- oder Abnahme im Sachzusammenhang deuten",
    stichwoerter="f_k''(t) = 0 ⇔ t = 20/k|W(20/k; 23 + 400/(k · e^2))|Zeitpunkt der stärksten Temperaturabnahme",
    voraussetzungen="zweite Ableitung einer Schar|Wendestelle als Extremstelle der Änderungsrate",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Beschreiben Sie", antwort="Term|Text",
    material="keins", skizze="keine", kontext="Produktion/Temperaturverlauf", textumfang="kurz",
    gegeben=FK,
    gesucht="Koordinaten des Wendepunkts des Graphen von f_k in Abhängigkeit von k; Bedeutung der x-Koordinate im Sachzusammenhang",
    verfahren="f_k''(t) = 0 ⇔ t = 20/k (mit Vorzeichenwechsel); f_k(20/k) berechnen; an der Wendestelle ist f_k' minimal, die Temperatur nimmt dort am stärksten ab",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f_k''(t) = 0 ⇔ t = 20/k, f_k(20/k) = 23 + 400/(k · e^2); die x-Koordinate des Wendepunkts gibt den Zeitpunkt an, zu dem die Änderung der Temperatur der Flüssigkeit am größten ist (amtlich)",
    zwischenergebnis="f_k'(20/k) = −20/e^2 ≈ −2,7", niveau_geschaetzt="II",
    fehlerquelle="die Wendestelle als Zeitpunkt der höchsten Temperatur deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (f_k'(20/k) = −20/e^2 für alle k). Der Erwartungshorizont spricht von der größten Änderung; gemeint ist die stärkste Abnahme (f_k' ist an der Wendestelle minimal, der stärkste Anstieg liegt bei t = 0). Typ und Nebentyp wiederverwendet. CAS-Anteil: zweite Ableitung und Gleichung mit dem Rechner.")
row("2017MgrundlegendBAnalysisCAS", "e", innen="2", seite="2|3", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Bestandsänderung grafisch als Fläche unter dem Ratengraphen bestimmen",
    typ_neben="Graph einer Stammfunktion durch einen Punkt skizzieren",
    stichwoerter="Fläche unter dem Ratengraphen von 0 bis 4|Zunahme um etwa 12 °C|Hochpunkt der Temperatur bei t = 4, Wendepunkte bei t ≈ 1,6 und t ≈ 6",
    voraussetzungen="Integral der Änderungsrate als Bestandsänderung|Kästchen auszählen|Vorzeichen und Extremstellen der Rate auf den Bestand übertragen",
    format="Rechnung|Kurzantwort|Zeichnen", operator="Bestimmen Sie|Geben Sie an|Skizzieren Sie", antwort="Zahl|Text|Grafik",
    material="Diagramm",
    skizze=ABB2_SK + "; zu erstellende Skizze (Erwartungshorizont): Temperatur in °C über der Zeit von 0 bis 12 Minuten, Beginn bei etwa 10, Anstieg bis zum Hochpunkt bei t = 4 etwa 12 Grad höher, danach fallend und flach auslaufend",
    kontext="Produktion/Temperaturverlauf", textumfang="mittel",
    gegeben="Für einen gesteuerten Temperaturverlauf zeigt der Graph in Abbildung 2 die Änderungsrate der Temperatur in Grad pro Minute in Abhängigkeit von der Zeit in Minuten seit Beginn des Vorgangs; die Rate ist für 0 < t < 4 positiv und für t > 4 negativ",
    gesucht="Näherungswert für die Änderung der Temperatur in den ersten vier Minuten und Angabe, ob die Temperatur zu- oder abnimmt; Skizze eines möglichen Temperaturverlaufs für die ersten zwölf Minuten",
    verfahren="Fläche zwischen Ratengraph und Zeitachse von 0 bis 4 durch Auszählen der Kästchen abschätzen, positive Rate heißt Zunahme; Skizze: Temperatur steigt bis t = 4 (Hochpunkt), Wendepunkte an den Extremstellen der Rate, danach fallend",
    schritte="3", zahlenraum="dezimal", einheiten="°C|min", abhaengig_von="",
    ergebnis="Durch Abschätzen des Inhalts der Fläche, die der Graph für die ersten vier Minuten mit der Zeitachse einschließt, ergibt sich, dass die Temperatur um etwa 12 ° steigt; Skizze eines möglichen Temperaturverlaufs im Erwartungshorizont (amtlich)",
    zwischenergebnis="Maximum der Rate etwa 5,5 bei t ≈ 1,6|Nullstelle der Rate bei t = 4", niveau_geschaetzt="III",
    fehlerquelle="den Wert der Rate bei t = 4 als Änderung angeben oder im Temperaturgraphen bei t = 4 einen Tiefpunkt zeichnen",
    bemerkung="Standardbezug: K2 III, K3 II, K4 III. AB amtlich: III. Amtlich (Näherung und Skizze im Erwartungshorizont); eigene Abschätzung am Bild (Trapezsumme mit Schrittweite 0,5) etwa 13, im Rahmen der Ablesegenauigkeit. Eichregel: Deutungsliste (e), die Beziehung zwischen Änderungsrate und Bestand am Graphen deuten (Fläche als Änderung, Temperaturverlauf aus dem Ratengraphen skizzieren). Die Teilaufgabe verlangt selbst eine Skizze; skizze beschreibt Abbildung 2 und die zu erstellende Darstellung. Typ und Nebentyp wiederverwendet (Nebentyp hier ohne vorgegebenen Punkt, ein möglicher Verlauf). CAS-Anteil: keiner.")
# ---- AG/LA (A1) CAS: Wölfe, 20 BE (Aufgabe 1: Population der weiblichen Wölfe mit L und M, 14 BE; Aufgabe 2: Matrix N, 6 BE).
# Aufgabe 1 a, c, e, f wortgleich mit 2017MerhoehtBAGLAA1WTR 1 a, d, e, f (Pool 2017 erhöht, dort x statt 0,4 in L).
WOLF = ("Population der weiblichen Wölfe in einem großen, abgeschlossenen Gebiet: im ersten Lebensjahr Welpen (W), im zweiten "
        "Jungtiere (J), ab dem dritten Lebensjahr geschlechtsreife Rudelführerinnen (R); jede Rudelführerin bringt pro Jahr "
        "durchschnittlich drei weibliche Welpen zur Welt; Zusammensetzung als Vektor (W; J; R), zu Beginn v_0; Entwicklung von "
        "einem Jahr zum nächsten: v_(n+1) = L · v_n mit L = ((0; 0; 3), (0,4; 0; 0), (0; 0,7; 0,8)) (Zeilen)")
WOLF_M = ("Population der weiblichen Wölfe als Vektor (W; J; R) aus Welpen, Jungtieren und Rudelführerinnen; zwei Jahre nach "
          "Beobachtungsbeginn ändern sich die Umweltbedingungen; von da an beschreibt v_(n+2) = M · v_n mit M = ((0; 3; 3,75), "
          "(0; 0; 2), (0,24; 0,45; 0,56)) (Zeilen) die Entwicklung im Zwei-Jahres-Rhythmus; sechs Jahre nach Beobachtungsbeginn "
          "ist v_6 = (600; 173; 165)")
NMAT = "Matrix N = ((0; 0; 4), (0,25; 0; 0), (0; 0,4; 0,6)) (Zeilen) und Vektoren u = (u1; u2; u3)"
row("2017MgrundlegendBAGLAA1CAS", "a", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="W → J mit 0,4|J → R mit 0,7|R → R mit 0,8|R → W mit 3",
    voraussetzungen="Spalte als Ausgangszustand, Zeile als Zielzustand lesen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins",
    skizze="zu erstellendes Übergangsdiagramm (Erwartungshorizont): Knoten W, J, R im Dreieck; Pfeil W → J mit 0,4, J → R mit 0,7, R → W mit 3 und eine Schleife an R mit 0,8",
    kontext="Biologie/Wolfspopulation", textumfang="lang",
    gegeben=WOLF,
    gesucht="Darstellung der Entwicklung der Population in einem Übergangsdiagramm",
    verfahren="Für jeden von null verschiedenen Eintrag einen Pfeil vom Spalten- zum Zeilenzustand mit dem Eintrag beschriften",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Diagramm mit den Knoten W, J, R: W → J mit 0,4, J → R mit 0,7, R → R (Schleife) mit 0,8, R → W mit 3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauschen (Pfeil R → J mit 0,7)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Teilaufgabe wortgleich mit 2017MerhoehtBAGLAA1WTR, Teilaufgabe 1 a (Pool 2017 erhöht; im Stamm dort x statt 0,4), andere Trägeraufgabe, geteilter Typ (iqb.md § 7). Die Teilaufgabe verlangt selbst ein Diagramm; skizze beschreibt die zu erstellende Darstellung nach dem Erwartungshorizont. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA1CAS", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Matrixeintrag im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Überlebensrate der Welpen: Eintrag 0,4 (Zeile 2, Spalte 1)|höhere Sterblichkeit, kleinerer Eintrag",
    voraussetzungen="Eintrag als Anteil eines Übergangs lesen|Überlebensrate und Sterblichkeitsrate ergänzen sich",
    format="Kurzantwort", operator="Nennen Sie|Beschreiben Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="mittel",
    gegeben=WOLF,
    gesucht="Eintrag der Matrix L, der die Überlebensrate der Welpen angibt; Änderung dieses Eintrags bei einer Erhöhung der Sterblichkeitsrate der Welpen",
    verfahren="Der Übergang W → J steht in Zeile 2, Spalte 1; eine höhere Sterblichkeit heißt eine kleinere Überlebensrate",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Eintrag 0,4; bei einer Erhöhung der Sterblichkeitsrate der Welpen würde der Wert des Eintrags kleiner werden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="den Eintrag 3 (Geburten) oder 0,8 (Rudelführerinnen) nennen",
    bemerkung="Standardbezug: K1 I, K3 I, K4 I. AB amtlich: I. Amtlich. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA1CAS", "c", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unbekannte Anzahl aus einer Bedingung an den Folgezustand berechnen", typ_neben="",
    stichwoerter="R_1 = 0,7 · J_0 + 0,8 · R_0|R_0 = 39, R_1 = 55|J_0 = 34",
    voraussetzungen="Zeile des Matrix-Vektor-Produkts|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="mittel",
    gegeben=WOLF + "; zu Beobachtungsbeginn gehören 39 Rudelführerinnen zur Population, ein Jahr später 55",
    gesucht="Anzahl der Jungtiere zu Beobachtungsbeginn",
    verfahren="Dritte Zeile von v_1 = L · v_0: 0,7 · J + 0,8 · 39 = 55",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Da innerhalb des ersten Jahres 70 % der Jungtiere zu Rudelführerinnen heranwachsen und 80 % der Rudelführerinnen überleben: 0,7 · J + 0,8 · 39 = 55 ⇔ J = 34 (amtlich)",
    zwischenergebnis="0,8 · 39 = 31,2", niveau_geschaetzt="II",
    fehlerquelle="die überlebenden Rudelführerinnen nicht berücksichtigen (J = 55/0,7)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (J = 34). Teilaufgabe wortgleich mit 2017MerhoehtBAGLAA1WTR, Teilaufgabe 1 d, andere Trägeraufgabe, geteilter Typ. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA1CAS", "d", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Vorherige Verteilung über die inverse Matrix berechnen", typ_neben="",
    stichwoerter="v_6 = M · v_4|v_4 = M^(−1) · v_6|(313; 92; 87)",
    voraussetzungen="Zwei-Jahres-Schritt rückwärts|inverse Matrix mit dem Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="mittel",
    gegeben=WOLF_M,
    gesucht="Anzahl der Welpen, Jungtiere und Rudelführerinnen vier Jahre nach Beobachtungsbeginn",
    verfahren="Aus v_6 = M · v_4 folgt v_4 = M^(−1) · v_6; mit dem Rechner auswerten",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="v_4 = M^(−1) · v_6 ≈ (313; 92; 87) (amtlich)",
    zwischenergebnis="M^(−1) · v_6 = (313,4; 91,875; 86,5)", niveau_geschaetzt="II",
    fehlerquelle="M · v_6 statt M^(−1) · v_6 rechnen oder die Einjahresmatrix L verwenden",
    bemerkung="Standardbezug: K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (313,40; 91,875; 86,5). Typ wiederverwendet. CAS-Anteil: inverse Matrix mit dem Rechner.")
row("2017MgrundlegendBAGLAA1CAS", "e", innen="1", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Verteilung nach einem Übergang berechnen", typ_neben="",
    stichwoerter="v_8 = M · v_6|(1138; 330; 314) gerundet",
    voraussetzungen="Matrix-Vektor-Produkt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="kurz",
    gegeben=WOLF_M,
    gesucht="Anzahl der Welpen, Jungtiere und Rudelführerinnen acht Jahre nach Beobachtungsbeginn",
    verfahren="v_8 = M · v_6 zeilenweise oder mit dem Rechner",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="v_8 = M · v_6 ≈ (1138; 330; 314) (amtlich)",
    zwischenergebnis="M · v_6 = (1137,75; 330; 314,25)", niveau_geschaetzt="I",
    fehlerquelle="M zweimal anwenden, weil acht Jahre zwei Jahre nach sechs Jahren sind",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (1137,75; 330; 314,25). Teilaufgabe wortgleich mit 2017MerhoehtBAGLAA1WTR, Teilaufgabe 1 e (dort 2 BE), andere Trägeraufgabe, geteilter Typ. Typ wiederverwendet. CAS-Anteil: Matrix-Vektor-Produkt mit dem Rechner.")
row("2017MgrundlegendBAGLAA1CAS", "f", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Wachstumsfaktor je Schritt aus zwei Zuständen im Abstand mehrerer Schritte nachweisen", typ_neben="",
    stichwoerter="v_10 ≈ (2168; 629; 598), v_12 ≈ (4126; 1195; 1138)|Faktor je Jahr 1,38, über zwei Jahre 1,38^2|1,38^2 · v_10 ≈ v_12",
    voraussetzungen="Faktor über zwei Jahre als Quadrat des Jahresfaktors|komponentenweise vergleichen",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="mittel",
    gegeben=WOLF_M + "; v_10 ≈ (2168; 629; 598) und v_12 ≈ (4126; 1195; 1138); aus diesen Vektoren soll ein Faktor ermittelt werden, mit dem die Anzahl jeder Altersgruppe von einem Jahr zum nächsten zunimmt",
    gesucht="rechnerischer Nachweis, dass dieser Faktor für jede der drei Altersgruppen etwa 1,38 beträgt",
    verfahren="1,38^2 · v_10 berechnen und mit v_12 vergleichen (oder die Quotienten der Komponenten und ihre Wurzeln)",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="1,38^2 · (2168; 629; 598) ≈ (4129; 1198; 1139) ≈ v_12 (amtlich)",
    zwischenergebnis="Quotienten 1,903; 1,900; 1,903|Wurzeln 1,380; 1,378; 1,380", niveau_geschaetzt="II",
    fehlerquelle="den Quotienten 4126/2168 ≈ 1,90 als Faktor je Jahr angeben",
    bemerkung="Standardbezug: K1 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Quotienten 1,903; 1,900; 1,903). Teilaufgabe wortgleich mit 2017MerhoehtBAGLAA1WTR, Teilaufgabe 1 f, andere Trägeraufgabe, geteilter Typ. Typ wiederverwendet. CAS-Anteil: Rechnung mit dem Rechner.")
row("2017MgrundlegendBAGLAA1CAS", "g", innen="1", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Eignung eines Populationsmodells zur langfristigen Beschreibung beurteilen", typ_neben="",
    stichwoerter="ungebremstes Wachstum mit Faktor 1,38 je Jahr|Umweltbedingungen ändern sich|Modell muss nach wenigen Jahren angepasst werden",
    voraussetzungen="Modellannahmen im Sachzusammenhang prüfen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Biologie/Wolfspopulation", textumfang="mittel",
    gegeben=WOLF_M + "; das Modell liefert ein Wachstum aller Altersgruppen mit einem Faktor von etwa 1,38 je Jahr",
    gesucht="Beurteilung der Beschreibung der Entwicklung durch die Matrix M hinsichtlich ihrer Eignung zur langfristigen Beschreibung",
    verfahren="Unbegrenztes exponentielles Wachstum ist in einem abgeschlossenen Gebiet unrealistisch; die Umweltbedingungen und damit die Übergänge ändern sich",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Das Modell ist zur langfristigen Beschreibung der Entwicklung der Population nicht geeignet; es ist davon auszugehen, dass sich diese mit den Umweltbedingungen ändert und damit das Modell im Abstand weniger Jahre angepasst werden muss (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Modell wegen der Rundungen statt wegen des unbegrenzten Wachstums kritisieren",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich. Abgewandelt gegenüber 2017MerhoehtBAGLAA1WTR, Teilaufgabe 1 h (dort „das verwendete Modell“, hier „die Beschreibung der Entwicklung … durch die Matrix M“), geteilter Typ. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA1CAS", "a", innen="2", seite="2", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Nullvektor als einzige Lösung von M · u = 0 nachweisen", typ_neben="",
    stichwoerter="N · u = 0 als homogenes Gleichungssystem|det N = 0,4 ≠ 0|einzige Lösung u = 0",
    voraussetzungen="Matrix-Vektor-Gleichung als Gleichungssystem|eindeutige Lösbarkeit",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=NMAT,
    gesucht="Nachweis, dass es keinen Vektor u ≠ 0 mit N · u = 0 gibt",
    verfahren="Das Gleichungssystem N · u = 0 mit dem Rechner lösen (oder det N ≠ 0): einzige Lösung ist der Nullvektor",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="N · u = 0 ⇔ u = 0 (amtlich)",
    zwischenergebnis="det N = 0,4", niveau_geschaetzt="I",
    fehlerquelle="nur einen Vektor u ≠ 0 mit N · u ≠ 0 angeben",
    bemerkung="Standardbezug: K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (det N = 2/5, Kern nur der Nullvektor). Schätzung I (eine Rechnung mit dem Rechner, begründet); amtlich II – bei der Prüfung keine Regel als falsch angewandt erkannt (kein Typ mit Vorbild, der verwandte Typ „Existenz mehrerer Lösungen von M · a = 0 begründen“ fragt das Gegenteil), Abweichung bleibt. Neuer Typ: der vorhandene Typ zeigt weitere Lösungen neben dem Nullvektor, hier ist die eindeutige Lösbarkeit nachzuweisen. CAS-Anteil: Gleichungssystem oder Determinante mit dem Rechner.")
row("2017MgrundlegendBAGLAA1CAS", "b", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Alle Vektoren mit M · v = t · v für festes t bestimmen", typ_neben="",
    stichwoerter="(N − E) · u = 0|u = t · (4; 1; 1)|(4t)^2 + t^2 + t^2 = 1800|u = ±(40; 10; 10)",
    voraussetzungen="Fixvektoren als Lösungen eines homogenen Gleichungssystems|Lösungsmenge mit Parameter|Betragsbedingung einsetzen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=NMAT + "; für einen Vektor u gilt |u|^2 = 1800",
    gesucht="Lösungen der Gleichung N · u = u",
    verfahren="(N − E) · u = 0 lösen: u = t · (4; 1; 1) mit t ∈ IR; (4t)^2 + t^2 + t^2 = 1800 liefert t = ±10",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="N · u = u ⇔ u = (4t; t; t) mit t ∈ IR; (4t)^2 + t^2 + t^2 = 1800 ⇔ t = −10 ∨ t = 10; damit ergeben sich als Lösungen −(40; 10; 10) und (40; 10; 10) (amtlich)",
    zwischenergebnis="18t^2 = 1800", niveau_geschaetzt="II",
    fehlerquelle="nur die positive Lösung angeben oder die Betragsbedingung als 4t + t + t = 1800 lesen",
    bemerkung="Standardbezug: K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Kern von N − E: (4; 1; 1)). Schätzung II (Fixvektoren mit Parameter, Betragsbedingung: Verkettung); amtlich III – bei der Prüfung keine Regel als falsch angewandt erkannt: „Lösungsmenge mit freien Parametern beschreiben“ ist in iqb.md § 7 offen, kein Listeneintrag; Abweichung bleibt. N ist die Matrix aus 2017MerhoehtBAGLAA1WTR, Aufgabe 2 b. Typ wiederverwendet. CAS-Anteil: Gleichungssystem mit dem Rechner.")
# ---- AG/LA (A2) CAS 1: Turm auf einem Spielplatz, 20 BE (eine Aufgabe, a–f; die Aufgabe druckt als Summe 25, die BE der
# Teilaufgaben ergeben 20 wie der Erwartungshorizont). a–c wortgleich mit 2017MerhoehtBAGLAA2WTR1 und CAS1 1 a–c.
TURM = ("Ein Turm auf einem Spielplatz besteht aus vier 4,50 m langen, vertikal stehenden Pfosten, vier horizontalen Balken und "
        "einem Dach in Form einer geraden Pyramide; die Dicke der Bauteile wird vernachlässigt; die Enden der Pfosten sind "
        "A(2; −3; z), B, C und D(−3; −2; z) mit z ∈ IR sowie E(2; −3; 4), F(3; 2; 4), G(−2; 3; 4) und H; die Spitze des Dachs "
        "ist S(0; 0; 5); die x1x2-Ebene ist der Untergrund, 1 LE = 1 m")
TURM_SK = ("schematisches Schrägbild des Turms: vier senkrechte Pfosten mit den unteren Enden A, B, C, D und den oberen Enden E, "
           "F, G, H, oben das Viereck EFGH als Rahmen aus Balken und darüber die Dachpyramide mit Spitze S; die Kante von H "
           "nach unten gestrichelt")
row("2017MgrundlegendBAGLAA2CAS1", "a", innen="1", seite="1", punkte="1", afb_amtlich="I",
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
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Höhe 4 als Tiefe angeben oder 4,5 − 4 als Höhe über dem Boden deuten",
    bemerkung="Standardbezug: K1 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Teilaufgabe wortgleich mit 2017MerhoehtBAGLAA2WTR1 und 2017MerhoehtBAGLAA2CAS1, Teilaufgabe 1 a (Pool 2017 erhöht, gleicher Stamm), andere Trägeraufgabe, geteilter Typ (iqb.md § 7). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA2CAS1", "b", innen="1", seite="1", punkte="5", afb_amtlich="I",
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
    zwischenergebnis="EF = HG = (1; 5; 0)|FG = (−5; 1; 0)|√26", niveau_geschaetzt="II",
    fehlerquelle="nur gleiche Seitenlängen zeigen (Raute) oder nur den rechten Winkel (Rechteck)",
    bemerkung="Standardbezug: K1 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (|EF| = |FG| = √26). Schätzung II (Vektoraddition, Parallelogramm, Orthogonalität und Längen verkettet); amtlich I – bei der Prüfung keine Regel als falsch angewandt erkannt, Abweichung bleibt (wie bei der wortgleichen Teilaufgabe 2017MerhoehtBAGLAA2WTR1, 1 b: geschätzt II, amtlich I, dort ebenso beibehalten). Teilaufgabe wortgleich mit 2017MerhoehtBAGLAA2WTR1 und 2017MerhoehtBAGLAA2CAS1, Teilaufgabe 1 b, geteilter Typ und Nebentyp. CAS-Anteil: Vektorrechnung mit dem Rechner möglich.")
row("2017MgrundlegendBAGLAA2CAS1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrie einer geraden Pyramide bezüglich einer Koordinatenachse über Grundflächenmittelpunkt und Spitze begründen", typ_neben="",
    stichwoerter="gerade Pyramide mit quadratischer Grundfläche EFGH parallel zur x1x2-Ebene|Mittelpunkt der Grundfläche (0; 0; 4)|Spitze S(0; 0; 5) auf der x3-Achse",
    voraussetzungen="Mittelpunkt eines Quadrats als Diagonalenmitte|gerade Pyramide: Spitze über dem Mittelpunkt",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="mittel",
    gegeben=TURM + "; H(−3; −2; 4); EFGH ist ein Quadrat",
    gesucht="Begründung, dass die Pyramide EFGHS symmetrisch bezüglich der x3-Achse ist",
    verfahren="Der Mittelpunkt der Grundfläche (Mitte von EG) ist (0; 0; 4) und liegt wie S auf der x3-Achse; die Grundfläche ist ein Quadrat parallel zur x1x2-Ebene, die Pyramide gerade",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2017MgrundlegendBAGLAA2CAS1-1b",
    ergebnis="Die Pyramide ist gerade und hat eine quadratische Grundfläche, die parallel zur x1x2-Ebene ist; der Mittelpunkt der Grundfläche liegt ebenso auf der x3-Achse wie die Spitze S (amtlich)",
    zwischenergebnis="Mitte von EG = Mitte von FH = (0; 0; 4)", niveau_geschaetzt="II",
    fehlerquelle="nur die Lage von S auf der x3-Achse nennen",
    bemerkung="Standardbezug: K1 II, K2 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Mittelpunkt (0; 0; 4)). Teilaufgabe wortgleich mit 2017MerhoehtBAGLAA2WTR1 und 2017MerhoehtBAGLAA2CAS1, Teilaufgabe 1 c, geteilter Typ. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA2CAS1", "d", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen", typ_neben="",
    stichwoerter="Mittelpunkt von EF: M(2,5; −0,5; 4)|Dreieck EFS: ½ · |EF| · |MS| ≈ 7,0|vier kongruente Dachdreiecke, etwa 28 m²",
    voraussetzungen="Höhe eines gleichschenkligen Dreiecks von der Basismitte zur Spitze|Vektorbetrag|gerade Pyramide: vier gleiche Seitenflächen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="kurz",
    gegeben=TURM + "; EFGH ist ein Quadrat mit H(−3; −2; 4), die Pyramide EFGHS ist gerade",
    gesucht="Inhalt der gesamten Dachfläche in Quadratmetern",
    verfahren="Mittelpunkt M von EF, Höhe |MS| des gleichschenkligen Dreiecks EFS, Flächeninhalt ½ · |EF| · |MS|; die vier Dachdreiecke sind kongruent, also mal 4",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="m²", abhaengig_von="2017MgrundlegendBAGLAA2CAS1-1b",
    ergebnis="Mittelpunkt der Seite EF: M(2,5; −0,5; 4); ½ · |EF| · |MS| ≈ 7,0; die Dachfläche hat einen Flächeninhalt von etwa 28 m² (amtlich)",
    zwischenergebnis="|EF| = √26|MS = (−2,5; 0,5; 1), |MS| = √7,5|Dreieck √195/2 ≈ 6,98", niveau_geschaetzt="II",
    fehlerquelle="die Grundfläche EFGH mitzählen oder die Seitenkante |ES| statt der Höhe verwenden",
    bemerkung="Standardbezug: K3 I, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (4 · √195/2 ≈ 27,93; über das Kreuzprodukt ebenso). Typ wiederverwendet (hier mal vier kongruente Dreiecke). CAS-Anteil: Beträge mit dem Rechner.")
row("2017MgrundlegendBAGLAA2CAS1", "e", innen="1", seite="1|2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schattenpunkt auf einer Kante als Schnittpunkt von Lichtgerade und Kantengerade berechnen", typ_neben="",
    stichwoerter="Stange mit oberem Endpunkt T(0; 0; 5,5)|Lichtrichtung (5; −1; −3)|Lichtgerade durch T mit Gerade EF schneiden|r = 0,5, Punkt (2,5; −0,5; 4)",
    voraussetzungen="Gerade in Parameterform|zwei Geraden gleichsetzen|Schattenpunkt als Schnittpunkt der Lichtgeraden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="mittel",
    gegeben=TURM + "; an der Spitze des Dachs ist eine gerade Stange mit dem oberen Endpunkt T(0; 0; 5,5) befestigt; Sonnenlicht wird durch parallele Geraden mit dem Richtungsvektor (5; −1; −3) beschrieben; der untere Endpunkt des Schattens liegt auf der Dachkante EF",
    gesucht="Koordinaten des Punkts, der den unteren Endpunkt des Schattens darstellt",
    verfahren="Lichtgerade durch T mit dem Richtungsvektor (5; −1; −3) und die Gerade durch E und F gleichsetzen: (0; 0; 5,5) + r · (5; −1; −3) = (2; −3; 4) + s · (1; 5; 0); r = 0,5 einsetzen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="Für r, s ∈ IR liefert (0; 0; 5,5) + r · (5; −1; −3) = (2; −3; 4) + s · (1; 5; 0): r = 0,5; damit (2,5; −0,5; 4) (amtlich)",
    zwischenergebnis="s = 0,5: der Punkt ist der Mittelpunkt von EF", niveau_geschaetzt="II",
    fehlerquelle="die Lichtgerade mit der Grundebene z = 0 statt mit der Dachkante schneiden",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (r = s = 1/2). Neuer Typ: vorhandene Schattentypen schneiden die Lichtgerade mit einer Ebene oder beschreiben die Schattenlänge auf der Dachfläche (2017MerhoehtBAGLAA2WTR1, 1 e); hier liegt der Schattenpunkt auf einer Kante und wird als Schnitt zweier Geraden berechnet. CAS-Anteil: Gleichungssystem mit dem Rechner.")
row("2017MgrundlegendBAGLAA2CAS1", "f", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punkt auf einer Geraden mit vorgegebenem Abstand zu einem festen Punkt über eine quadratische Gleichung bestimmen", typ_neben="",
    stichwoerter="Balken 2,10 m, unteres Ende I(2; −3; 3,5) am Pfosten AE|oberes Ende J(2 + t; −3 + 5t; 4) auf EF|IJ = 2,1 für 0 <= t <= 1: t = 0,4|Verhältnis 2 : 3",
    voraussetzungen="Punkt auf einer Strecke mit Parameter|Abstand zweier Punkte|quadratische Gleichung, Lösung im Bereich wählen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Skizze", skizze=TURM_SK, kontext="Spielplatz/Turm", textumfang="mittel",
    gegeben=TURM + "; zur Stabilisierung werden zusätzliche Balken der Länge 2,10 m verwendet; ein solcher Balken ist mit einem Ende in 3,50 m Höhe über dem Untergrund an dem Pfosten AE befestigt, mit dem anderen Ende an einem der beiden darauf liegenden horizontalen Balken; der obere Befestigungspunkt teilt diesen Balken in zwei Abschnitte",
    gesucht="Verhältnis der Längen der beiden Abschnitte",
    verfahren="I(2; −3; 3,5) auf AE; J auf der Geraden durch E und F: (2 + t; −3 + 5t; 4); |IJ| = 2,1 für 0 <= t <= 1 liefert t = 0,4; Verhältnis 0,4 : 0,6 (auf EH ebenso)",
    schritte="4", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="I(2; −3; 3,5), J(2 + t; −3 + 5t; 4); für 0 <= t <= 1 gilt |IJ| = 2,1 ⇔ t = 0,4; damit ergibt sich als Verhältnis 2 : 3 (amtlich)",
    zwischenergebnis="26t^2 + 0,25 = 4,41|t = ±0,4", niveau_geschaetzt="III",
    fehlerquelle="den Höhenunterschied 0,5 m übersehen und |EJ| = 2,1 ansetzen oder t = −0,4 mitzählen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (t = ±2/5, nur 2/5 im Bereich; auf EH ebenso 2 : 3). Eichregel: Deutungsliste (a), die Balkenlänge erst in eine Abstandsbedingung mit einem Punkt auf der Balkengeraden übersetzen. Abgewandelt gegenüber 2017MerhoehtBAGLAA2WTR1, 1 f und 2017MerhoehtBAGLAA2CAS1, 1 g (dort an einem der Pfosten, hier am Pfosten AE), geteilter Typ. Die Aufgabe druckt als BE-Summe 25; die Teilaufgaben ergeben 20 wie der Erwartungshorizont, Soll 20. Typ wiederverwendet. CAS-Anteil: Gleichung mit dem Rechner, Ansatz eigen.")
# ---- AG/LA (A2) CAS 2: Pyramide als Zelt, 20 BE (eine Aufgabe, a–g)
ZELT = ("Gerade Pyramide ABCDS mit A(0; 0; 0), B(5; 0; 0), C(5; 5; 0), D(0; 5; 0) und der Spitze S(2,5; 2,5; 3,9) in einem "
        "kartesischen Koordinatensystem")
ZELT2 = ZELT + "; die Pyramide stellt modellhaft ein geschlossenes Zelt auf horizontalem Untergrund dar, 1 LE = 1 m"
row("2017MgrundlegendBAGLAA2CAS2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Körper in ein räumliches Koordinatensystem einzeichnen", typ_neben="",
    stichwoerter="Grundquadrat ABCD in der x1x2-Ebene|Spitze S(2,5; 2,5; 3,9) über der Mitte|verdeckte Kanten gestrichelt",
    voraussetzungen="Punkte im Schrägbild eintragen|Pyramide aus Grundfläche und Spitze",
    format="Zeichnen", operator="Zeichnen Sie ein", antwort="Grafik",
    material="Koordinatensystem",
    skizze="zu erstellende Zeichnung (Erwartungshorizont): räumliches Koordinatensystem, x-Achse schräg nach vorn (5 markiert), y-Achse nach rechts (5), z-Achse nach oben (3); Grundquadrat A, B, C, D in der xy-Ebene mit A im Ursprung und D auf der y-Achse, Spitze S über der Mitte; die von A ausgehenden, verdeckten Kanten gestrichelt",
    kontext="ohne", textumfang="kurz",
    gegeben=ZELT,
    gesucht="Zeichnung der Pyramide in einem Koordinatensystem",
    verfahren="Eckpunkte im Schrägbild eintragen und verbinden, verdeckte Kanten gestrichelt",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Schrägbild der Pyramide im Erwartungshorizont (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="S über einer Ecke statt über der Mitte der Grundfläche einzeichnen",
    bemerkung="Standardbezug: K4 I. AB amtlich: I. Amtlich (Zeichnung im Erwartungshorizont). Die Teilaufgabe verlangt selbst eine Zeichnung; skizze beschreibt die zu erstellende Darstellung nach dem Erwartungshorizont. Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA2CAS2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Quadrat in einer Koordinatenebene ohne Vektoren über Seitenlängen und Achsenlage begründen", typ_neben="",
    stichwoerter="alle Seiten der Länge 5|A im Ursprung, B und D auf den Koordinatenachsen|rechter Winkel bei A",
    voraussetzungen="Streckenlänge bei achsenparallelen Seiten|Koordinatenachsen stehen senkrecht",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=ZELT,
    gesucht="Begründung ohne Verwendung von Vektoren, dass die Grundfläche der Pyramide ein Quadrat ist",
    verfahren="Alle Seiten haben die Länge 5 (Differenz einer Koordinate); A ist der Ursprung, B und D liegen auf den Koordinatenachsen, also ist der Winkel bei A ein rechter",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Alle Seiten des Vierecks ABCD haben die Länge 5; da A der Koordinatenursprung ist sowie B und D auf den Koordinatenachsen liegen, hat das Viereck bei A einen rechten Winkel (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur gleiche Seitenlängen nennen (Raute)",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich. Neuer Typ: vorhandene Quadrattypen weisen das Quadrat mit Vektoren nach (Gegenseitenvektoren, Skalarprodukt); hier ohne Vektoren aus achsenparalleler Lage und Seitenlängen. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA2CAS2", "c", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen", typ_neben="",
    stichwoerter="Seitenhöhe √(3,9^2 + 2,5^2) ≈ 4,63|½ · 5 · 4,63 ≈ 11,6",
    voraussetzungen="Höhe der Seitenfläche über den Satz des Pythagoras|Dreiecksfläche",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=ZELT,
    gesucht="Inhalt einer Seitenfläche der Pyramide",
    verfahren="Höhe der Seitenfläche vom Mittelpunkt einer Grundkante zur Spitze: √(3,9^2 + 2,5^2); Flächeninhalt ½ · 5 · Höhe",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="½ · 5 · √(3,9^2 + 2,5^2) ≈ 11,6 (amtlich)",
    zwischenergebnis="Seitenhöhe √21,46 ≈ 4,63", niveau_geschaetzt="II",
    fehlerquelle="die Pyramidenhöhe 3,9 als Höhe der Seitenfläche nehmen",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (11,581). Schätzung II (Mittelpunkt, Höhe und Fläche – nach der Liste der Routineverkettungen in iqb.md § 7 II); amtlich I – die Regel ist wörtlich angewandt, keine falsch angewandte Regel erkannt, Abweichung bleibt (die Poolzeilen des Typs amtlich I). Typ wiederverwendet. CAS-Anteil: keiner.")
row("2017MgrundlegendBAGLAA2CAS2", "d", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="Ebene durch A, B und S|Parameterform mit AB und AS|E: −39y + 25z = 0 (Kontrollangabe)",
    voraussetzungen="Parameterform einer Ebene|Parameter eliminieren oder Normalenvektor über das Vektorprodukt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=ZELT + "; die Punkte A, B und S liegen in einer Ebene E; zur Kontrolle: E: −39y + 25z = 0",
    gesucht="Gleichung von E in Koordinatenform",
    verfahren="Parameterform E: x = OA + r · AB + s · AS aufstellen und aus x = 5r + 2,5s, y = 2,5s, z = 3,9s die Parameter eliminieren (oder Normalenvektor AB × AS)",
    schritte="3", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="E: x = OA + r · AB + s · AS; das Gleichungssystem x = 5r + 2,5s, y = 2,5s, z = 3,9s liefert E: −39y + 25z = 0 (amtlich)",
    zwischenergebnis="AB × AS = (0; −19,5; 12,5)", niveau_geschaetzt="II",
    fehlerquelle="einen Normalenvektor wählen, der nur zu AB senkrecht ist",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Probe mit S: −39 · 2,5 + 25 · 3,9 = 0). Erste Schätzung: I (als einzelne Rechnung mit Kontrollangabe gewertet); korrigiert nach der Grundregel der engen Fassung (iqb.md § 7) wie beim Typ (im Pool alle Zeilen geschätzt II, amtlich II, darunter 2017MgrundlegendBAGLAA2WTR2, 1 d): Normalenvektor aus zwei Richtungsvektoren und Konstante aus einem Punkt sind eine Verkettung zweier Standardschritte, keine einzelne Rechnung. Typ wiederverwendet. CAS-Anteil: Gleichungssystem oder Vektorprodukt mit dem Rechner.")
row("2017MgrundlegendBAGLAA2CAS2", "e", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen", typ_neben="",
    stichwoerter="m = (0; 0; 1), n = (0; −39; 25)|cos φ = |m ∘ n|/(|m| · |n|)|φ ≈ 57,3°",
    voraussetzungen="Winkel zweier Ebenen über die Normalenvektoren|Horizontale als x1x2-Ebene",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Zelt", textumfang="kurz",
    gegeben=ZELT2 + "; E: −39y + 25z = 0 enthält die Zeltwand ABS",
    gesucht="Größe des Neigungswinkels einer Zeltwand gegenüber der Horizontalen",
    verfahren="Winkel zwischen dem Normalenvektor m = (0; 0; 1) der Horizontalen und n = (0; −39; 25) von E: cos φ = |m ∘ n|/(|m| · |n|)",
    schritte="2", zahlenraum="dezimal", einheiten="°", abhaengig_von="2017MgrundlegendBAGLAA2CAS2-1d",
    ergebnis="Mit m = (0; 0; 1) und n = (0; −39; 25) ergibt sich für den Neigungswinkel φ der Zeltwand, die durch das Dreieck ABS dargestellt wird: cos φ = (m ∘ n)/(|m| · |n|), d. h. φ ≈ 57,3° (amtlich)",
    zwischenergebnis="cos φ = 25/√2146 ≈ 0,540|tan φ = 3,9/2,5", niveau_geschaetzt="II",
    fehlerquelle="den Winkel zur Senkrechten angeben (32,7°)",
    bemerkung="Standardbezug: K3 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (57,34°; ebenso über tan φ = 3,9/2,5). Erste Schätzung: I (als einzelne Rechnung gewertet); korrigiert nach der Grundregel der engen Fassung (iqb.md § 7) wie beim Typ (im Pool alle Zeilen geschätzt II, amtlich II, darunter 2017MgrundlegendBAGLAA2WTR1, 1 e und WTR 2, 1 e): Normalenvektoren wählen und die Winkelformel anwenden ist eine Verkettung, keine einzelne Rechnung. Typ wiederverwendet. CAS-Anteil: Winkel mit dem Rechner.")
row("2017MgrundlegendBAGLAA2CAS2", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punkt auf einer Geraden mit vorgegebener Koordinate angeben", typ_neben="",
    stichwoerter="Lichtgerade durch L mit Richtungsvektor (7,5; −12,5; −3,9) trifft B(5; 0; 0)|z-Koordinate von L ist 1,3|t = 1/3|x_L = 5/2, y_L = 25/6",
    voraussetzungen="Gerade in Parameterform|Parameter aus einer Koordinate bestimmen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Zelt", textumfang="mittel",
    gegeben=ZELT2 + "; Sonnenlicht wird zu einem bestimmten Zeitpunkt durch parallele Geraden mit dem Richtungsvektor (7,5; −12,5; −3,9) beschrieben; es trifft durch ein kleines Loch L(x_L; y_L; 1,3) in einer Zeltwand genau auf den Eckpunkt B des Zeltbodens",
    gesucht="Werte von x_L und y_L",
    verfahren="(x_L; y_L; 1,3) + t · (7,5; −12,5; −3,9) = (5; 0; 0): aus der dritten Zeile t = 1/3, dann x_L und y_L",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Für t ∈ IR liefert (x_L; y_L; 1,3) + t · (7,5; −12,5; −3,9) = (5; 0; 0): x_L = 5/2, y_L = 25/6 (amtlich)",
    zwischenergebnis="t = 1/3|L(2,5; 4,17; 1,3) liegt in der Wand CDS", niveau_geschaetzt="II",
    fehlerquelle="den Richtungsvektor mit falschem Vorzeichen ansetzen (Loch jenseits von B)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (t = 1/3; L liegt in der Ebene durch C, D und S). Typ wiederverwendet (Punkt der Lichtgeraden durch B mit vorgegebener Höhe 1,3). CAS-Anteil: Gleichungssystem mit dem Rechner möglich.")
row("2017MgrundlegendBAGLAA2CAS2", "g", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Anteil der Bodenfläche unter einer Mindesthöhe über den Strahlensatz am Dachquerschnitt berechnen", typ_neben="",
    stichwoerter="aufrecht stehen: Zelthöhe mindestens 1,2 m|Randstreifen 1,2/3,9 · 2,5 m breit|inneres Quadrat mit Seite 2 · (2,5 − 1,2/3,9 · 2,5) m|Anteil (1 − 1,2/3,9)^2 ≈ 48 %",
    voraussetzungen="linearer Höhenverlauf der Seitenflächen|Strahlensatz im Querschnitt|Flächenverhältnis ähnlicher Quadrate",
    format="Rechnung|Zeichnen", operator="Bestimmen Sie|Veranschaulichen Sie", antwort="Zahl|Grafik",
    material="Skizze",
    skizze="zu erstellende Skizze (Erwartungshorizont): rechtwinkliges Dreieck als halber Querschnitt durch die Spitze, senkrechte Kathete 3,9 m (Zelthöhe), waagerechte Kathete 2,5 m (halbe Bodenbreite); nahe der Außenecke eine senkrechte Strecke der Länge 1,2 m bis zur Dachlinie, die den Randstreifen abgrenzt",
    kontext="Zelt", textumfang="mittel",
    gegeben=ZELT2 + "; auf einem Teil des Zeltbodens hat ein 1,20 m großes Kind die Möglichkeit, aufrecht zu stehen",
    gesucht="Anteil des Flächeninhalts dieses Teils am Flächeninhalt des gesamten Zeltbodens; Veranschaulichung des Vorgehens an einer geeignet beschrifteten Skizze",
    verfahren="Aufrecht stehen heißt Zelthöhe mindestens 1,2 m; die Höhe fällt von der Mitte (3,9 m) linear zum Rand; nach dem Strahlensatz ist der Randstreifen mit weniger als 1,2 m Höhe 1,2/3,9 · 2,5 m breit; die Stehfläche ist ein Quadrat mit der Seite 2 · (2,5 − 1,2/3,9 · 2,5) m; Anteil an (5 m)^2",
    schritte="4", zahlenraum="Bruch|dezimal|Prozent", einheiten="m|m²", abhaengig_von="",
    ergebnis="(2 · (2,5 m − 1,2/3,9 · 2,5 m))^2/(5 m)^2 ≈ 48 % (amtlich)",
    zwischenergebnis="Randstreifen ≈ 0,77 m|Seite des inneren Quadrats ≈ 3,46 m|Anteil 81/169", niveau_geschaetzt="III",
    fehlerquelle="den Anteil linear als 1 − 1,2/3,9 ≈ 69 % statt quadratisch angeben",
    bemerkung="Standardbezug: K1 II, K2 III, K4 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (81/169 ≈ 47,9 %). Eichregel: Deutungsliste (a), „aufrecht stehen“ erst in die Bedingung Zelthöhe mindestens 1,2 m übersetzen und über den Querschnitt auf die Grundfläche zurückführen. Die Teilaufgabe verlangt selbst eine Skizze; skizze beschreibt die zu erstellende Darstellung nach dem Erwartungshorizont. Typ wiederverwendet (dort der Anteil unter der Mindesthöhe, hier der darüber). CAS-Anteil: keiner.")
# ---- Stochastik CAS: Smartphones, 20 BE, davon 15 BE mit Zeilen. Aufgabe 1 (a, b; 5 BE) ist wortgleich mit
# 2017MgrundlegendBStochastikWTR1, Aufgabe 1 – Aufgabendublette, keine Zeile (iqb.md § 7). Aufgabe 2 a–d wortgleich mit WTR 1
# (geteilt, Felder übernommen), 2 e abgewandelt (90 % und mindestens 500 fehlerfreie statt 95 % und mindestens ein fehlerhaftes).
# Landesheft: 2017-be-gk-cas 3.1 ist diese Datei wortgleich (Heft a–g = Pool 1 a, 1 b, 2 a–e).
GERAETE = ("Ein Hersteller bringt ein neues Smartphone auf den Markt; die Geräte werden in vier Werken in jeweils großer Stückzahl "
           "hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den "
           "im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %")
WERK_SK = ("Tabelle mit den Spalten Werk A, B, C, D und den Zeilen „Anteil an der Gesamtzahl“ (10 %, 30 %, 20 %, 40 %) und "
           "„Anteil der fehlerhaften Geräte“ (5 %, 3 %, 4 %, 2 %)")
GETEILT = ("Teilaufgabe wortgleich mit dem WTR-Zweig (2017-ga-B-wtr, Datei 2017MgrundlegendBStochastikWTR1, Teilaufgabe {}), "
           "geteilter Typ, Felder übernommen; Schätzung aus der WTR-Zeile übernommen.")
row("2017MgrundlegendBStochastikCAS", "a", innen="2", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Totale Wahrscheinlichkeit über die Pfadregeln nachweisen", typ_neben="",
    stichwoerter="Werksanteil mal Fehleranteil je Werk|Summe über vier Werke|3 %",
    voraussetzungen="Tabelle als zweistufiges Experiment lesen|Pfadmultiplikation und -addition",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="Tabelle", skizze=WERK_SK, kontext="Produktion/Smartphones", textumfang="mittel",
    gegeben=GERAETE,
    gesucht="Nachweis, dass der Anteil der fehlerhaften Geräte unter allen hergestellten Geräten 3 % beträgt",
    verfahren="Summe der Produkte aus Werksanteil und Fehleranteil (totale Wahrscheinlichkeit)",
    schritte="2", zahlenraum="Prozent|dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,1 · 0,05 + 0,3 · 0,03 + 0,2 · 0,04 + 0,4 · 0,02 = 3 % (amtlich)",
    zwischenergebnis="0,005 + 0,009 + 0,008 + 0,008 = 0,03", niveau_geschaetzt="II",
    fehlerquelle="die vier Fehleranteile ungewichtet mitteln (3,5 %)",
    bemerkung="Standardbezug: K4 II, K5 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (3/100). " + GETEILT.format("2a") + " Die übernommene Schätzung I der WTR-Zeile weicht vom amtlichen Bereich II ab; nach dem Vorrang des Amtlichen für übernommene Schätzungen (Kern § 5) auf II gesetzt (erste Schätzung: I). Die WTR-Zeile trägt ihre eigene Schätzung und bleibt. Wortgleich auch im Landesheft 2017-be-gk-cas 3.1 c (dort wie im WTR-Heft). CAS-Anteil: keiner.")
row("2017MgrundlegendBStochastikCAS", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="fehlerhaftes Gerät, Werk A gesucht|Schnittanteil 0,1 · 0,05|durch Gesamtanteil 0,03|1/6",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient|Bedingung „fehlerhaft“ im Nenner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze=WERK_SK, kontext="Produktion/Smartphones", textumfang="kurz",
    gegeben=GERAETE + "; Anteil fehlerhafter Geräte insgesamt 3 %; ein unter allen hergestellten Geräten zufällig ausgewähltes Gerät ist fehlerhaft",
    gesucht="Wahrscheinlichkeit dafür, dass es im Werk A hergestellt wurde",
    verfahren="Schnittanteil 0,1 · 0,05 durch den Gesamtanteil 0,03 teilen (Satz von Bayes)",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="2017MgrundlegendBStochastikCAS-2a",
    ergebnis="(0,1 · 0,05)/0,03 = 1/6 (amtlich)",
    zwischenergebnis="≈ 16,7 %", niveau_geschaetzt="II",
    fehlerquelle="den Fehleranteil 5 % im Werk A angeben (Bedingung vertauscht)",
    bemerkung="Standardbezug: K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (1/6). " + GETEILT.format("2b") + " Wortgleich auch im Landesheft 2017-be-gk-cas 3.1 d. CAS-Anteil: keiner.")
row("2017MgrundlegendBStochastikCAS", "c", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Modalwert einer Binomialverteilung bestimmen", typ_neben="",
    stichwoerter="n = 250, p = 0,05|Erwartungswert 12,5 nicht ganzzahlig|P(X = 12) ≈ 11,6 % > P(X = 13) ≈ 11,2 %|wahrscheinlichste Anzahl 12",
    voraussetzungen="Erwartungswert n · p|Einzelwahrscheinlichkeiten am Rechner|Nachbarwerte vergleichen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Smartphones", textumfang="kurz",
    gegeben=GERAETE + "; von im Werk A hergestellten Geräten werden 250 zufällig ausgewählt; X: Anzahl der fehlerhaften, binomialverteilt mit n = 250 und p = 0,05",
    gesucht="die Anzahl fehlerhafter Geräte, die darunter mit der größten Wahrscheinlichkeit auftritt",
    verfahren="Erwartungswert 250 · 0,05 = 12,5 ist nicht ganzzahlig; P(X = 12) und P(X = 13) berechnen und vergleichen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Der Erwartungswert von X ist 250 · 0,05 = 12,5; P(X = 12) ≈ 11,6 %, P(X = 13) ≈ 11,2 %; damit ist die gesuchte Anzahl 12 (amtlich)",
    zwischenergebnis="P(X = 12) ≈ 0,1160|P(X = 13) ≈ 0,1117", niveau_geschaetzt="I",
    fehlerquelle="12,5 oder aufgerundet 13 als Anzahl angeben",
    bemerkung="Standardbezug: K1 I, K2 I, K3 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (0,11597; 0,11174). " + GETEILT.format("2c") + " Wortgleich im Landesheft 2017-be-gk-cas 3.1 e (Berliner CAS-Heft; das WTR-Heft 2017-be-gk 3.1 e weicht davon ab). CAS-Anteil: Binomialwerte mit dem Rechner.")
row("2017MgrundlegendBStochastikCAS", "d", innen="2", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Term 200 · 0,98^s · 0,02 + 0,98^200|0,02 Fehleranteil in Werk D|s = 199|P(X ≤ 1) für n = 200, höchstens eines fehlerhaft",
    voraussetzungen="Bernoulli-Formel für k = 0 und k = 1 erkennen|Summe als kumulierte Wahrscheinlichkeit",
    format="Kurzantwort", operator="Geben Sie an|Beschreiben Sie", antwort="Zahl|Text",
    material="Tabelle", skizze=WERK_SK, kontext="Produktion/Smartphones", textumfang="kurz",
    gegeben=GERAETE + "; Term 200 · 0,98^s · 0,02 + 0,98^200",
    gesucht="ein Wert von s, für den mit dem Term im Sachzusammenhang die Wahrscheinlichkeit eines Ereignisses berechnet werden kann, und Beschreibung des zugehörigen Ereignisses",
    verfahren="0,02 ist der Fehleranteil in Werk D; 0,98^200 = P(X = 0) und 200 · 0,02 · 0,98^199 = P(X = 1) für n = 200, also s = 199 und die Summe P(X ≤ 1)",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="s = 199; unter 200 im Werk D hergestellten, zufällig ausgewählten Geräten ist höchstens eines fehlerhaft (amtlich)",
    zwischenergebnis="Wert des Terms ≈ 0,0894", niveau_geschaetzt="II",
    fehlerquelle="s = 200 wählen oder das Ereignis als „genau eines fehlerhaft“ beschreiben",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (0,08937). " + GETEILT.format("2d") + " Wortgleich auch im Landesheft 2017-be-gk-cas 3.1 f. CAS-Anteil: keiner.")
row("2017MgrundlegendBStochastikCAS", "e", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln", typ_neben="",
    stichwoerter="Werk C, 4 % fehlerhaft: fehlerfrei mit p = 0,96|P(X >= 500) >= 0,9|n = 526: 88,5 %, n = 527: 91,9 %|mindestens 527 Geräte",
    voraussetzungen="Trefferdefinition wechseln (nicht fehlerhaft)|Binomialmodell mit unbekanntem n|Probieren am Rechner",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze=WERK_SK, kontext="Produktion/Smartphones", textumfang="mittel",
    gegeben=GERAETE + "; es werden im Werk C hergestellte Geräte zufällig ausgewählt",
    gesucht="Mindestanzahl der auszuwählenden Geräte, damit sich darunter mit einer Wahrscheinlichkeit von mindestens 90 % mindestens 500 Geräte befinden, die nicht fehlerhaft sind",
    verfahren="X: Anzahl der nicht fehlerhaften Geräte, binomialverteilt mit p = 0,96; das kleinste n mit P(X >= 500) >= 0,9 durch Probieren mit dem Rechner suchen",
    schritte="3", zahlenraum="Prozent|dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="Ist n die Anzahl auszuwählender Geräte, so liefert Probieren für n = 526: P(X >= 500) ≈ 88,5 % und für n = 527: P(X >= 500) ≈ 91,9 %; es müssen mindestens 527 Geräte ausgewählt werden (amtlich)",
    zwischenergebnis="n = 525: 0,842|n = 526: 0,885|n = 527: 0,919", niveau_geschaetzt="III",
    fehlerquelle="mit p = 0,04 (fehlerhaft) rechnen oder n aus dem Erwartungswert 500/0,96 ≈ 521 bestimmen",
    bemerkung="Standardbezug: K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (0,8854; 0,9189). Eichregel: Deutungsliste (f), Mindestumfang für eine Mindestwahrscheinlichkeit bestimmen. Abgewandelt gegenüber 2017MgrundlegendBStochastikWTR1, Teilaufgabe 2 e (dort 95 % und mindestens ein fehlerhaftes Gerät über das Gegenereignis), anderer Typ. Wortgleich im Landesheft 2017-be-gk-cas 3.1 g (Berliner CAS-Heft; das WTR-Heft 2017-be-gk 3.1 g folgt der WTR-Fassung). Typ wiederverwendet (mindestens 500 Treffer = mehr als 499). Aufgabendublette: Aufgabe 1 (a, b; 5 BE) dieser Datei ist wortgleich mit 2017MgrundlegendBStochastikWTR1, Aufgabe 1 und bekommt keine Zeile; Soll der Datei 15 statt 20 BE (iqb.md § 7). CAS-Anteil: Probieren mit dem Rechner, Ansatz eigen.")
NEUE_TYPEN = [
    # ("Typname", "Sachgebiet", "Thema", "Definition in einem Satz.", "beispiel_id"),
    ("Intervall, in dem eine Modellfunktion mindestens einen vorgegebenen Wert annimmt, über eine Ungleichung bestimmen", "Analysis", "Gleichungen lösen",
     "Die Ungleichung f(x) >= c für eine Modellfunktion über ihre Randstellen f(x) = c (mit dem Rechner) lösen und das Intervall im Sachzusammenhang angeben, etwa als Zeitabschnitt, in dem ein Mindestwert erreicht wird.", "2017MgrundlegendBAnalysisCAS-1d"),
    ("Zwei Parameter einer Exponentialfunktion aus Funktionswert und Änderungsrate an einer Stelle bestimmen", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Für einen Ansatz wie a + b · e^(c · x) aus einem vorgegebenen Funktionswert und einer vorgegebenen momentanen Änderungsrate an derselben Stelle das Gleichungssystem für b und c aufstellen und lösen.", "2017MgrundlegendBAnalysisCAS-1e"),
    ("Graph über eine gemeinsame Eigenschaft aller Scharfunktionen als nicht zur Schar gehörend begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Begründen, dass ein abgebildeter Graph zu keiner Funktion einer Schar gehören kann, weil er eine Eigenschaft verletzt, die für alle Parameterwerte gilt (etwa eine gemeinsame untere Schranke oder ein gemeinsames Grenzverhalten).", "2017MgrundlegendBAnalysisCAS-2b"),
    ("Scharparameter für eine vorgegebene Höhe des Hochpunkts berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Hochpunkt einer Schar in Abhängigkeit vom Parameter bestimmen und den Parameter so berechnen, dass der Funktionswert am Hochpunkt einen vorgegebenen Wert (etwa eine Höchsttemperatur) hat.", "2017MgrundlegendBAnalysisCAS-2c"),
    ("Matrizenalgebra: Nullvektor als einzige Lösung von M · u = 0 nachweisen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Zeigen, dass die Gleichung M · u = 0 für eine gegebene Matrix nur vom Nullvektor erfüllt wird, über das homogene Gleichungssystem oder eine Determinante ungleich null.", "2017MgrundlegendBAGLAA1CAS-2a"),
    ("Schattenpunkt auf einer Kante als Schnittpunkt von Lichtgerade und Kantengerade berechnen", "Analytische Geometrie", "Schnittmengen",
     "Den Schattenpunkt eines Punktes bei parallelem Licht, der auf einer Kante eines Körpers liegt, als Schnittpunkt der Lichtgeraden durch den Punkt mit der Geraden durch die Kante berechnen.", "2017MgrundlegendBAGLAA2CAS1-1e"),
    ("Ebene Figur: Quadrat in einer Koordinatenebene ohne Vektoren über Seitenlängen und Achsenlage begründen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Ohne Vektorrechnung begründen, dass ein Viereck in einer Koordinatenebene ein Quadrat ist: gleiche Seitenlängen aus den Koordinaten und ein rechter Winkel, weil zwei Seiten auf den Koordinatenachsen liegen.", "2017MgrundlegendBAGLAA2CAS2-1b"),
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
