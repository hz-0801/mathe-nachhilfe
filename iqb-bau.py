# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.9 · 15.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v1.0

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

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
  1. iqb.md, katalog-prompt.md, iqb-quellen.csv, iqb-katalog.csv und
     iqb-typen.csv neben dieses Skript legen (aus dem Repo, geprüfter SHA).
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen.
  3. python iqb-bau.py – schreibt beide CSV-Dateien, gibt Prüftabelle und
     Bericht aus. Bei einem Fehler wird nichts geschrieben.
  4. Ist ZEILEN leer, läuft nur die Selbstprüfung über den Gesamtbestand.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    # Stapel nach Spalte stapel in iqb-quellen.csv: Jahr-Niveau-Teil
    "stapel": "2026-ea-B-mms",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2026MerhoehtBAnalysisMMS1": 30,
        "2026MerhoehtBAnalysisMMS2": 30,
        "2026MerhoehtBAGLAA1MMS": 20,
        "2026MerhoehtBAGLAA2MMS2": 20,
        "2026MerhoehtBStochastikMMS3": 8,
    },
    # True: Probelauf – prüfen und berichten, nichts schreiben, Stapel darf
    # unvollständig sein. False: Stapel muss vollständig sein, dann schreiben.
    "probe": False,
}

# ========================================= QUELLEN UND PRÜFUNG, NICHT ÄNDERN
KAT = "iqb-katalog.csv"
TYP = "iqb-typen.csv"
QUELLEN = "iqb-quellen.csv"
PROFIL = "iqb.md"
KERN = "katalog-prompt.md"
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


def vokabular():
    """Kopfzeile und Formvokabular aus dem Kern, Sachgebiete und Themen aus dem Profil."""
    kern, profil = lies(KERN), lies(PROFIL)

    m = re.search(r"^Kopfzeile:\s*\n(id;.+)$", kern, re.M)
    if not m:
        sys.exit(f"{KERN}: Kopfzeile nicht gefunden.")
    head = m.group(1).strip().split(";")

    v = {feld: liste_aus_klammer(kern, feld, KERN)
         for feld in ("format", "antwort", "material", "zahlenraum",
                      "textumfang", "niveau_geschaetzt")}

    m = re.search(r"trägt das Sachgebiet:\s*\*\*(.+?)\*\*", profil, re.S)
    if not m:
        sys.exit(f"{PROFIL}: Sachgebiete nicht gefunden.")
    leitideen = [s.strip() for s in re.sub(r"\s+", " ", m.group(1)).split("·") if s.strip()]

    themen = {}
    for m in re.finditer(r"^\*\*([^*:]+):\*\*(.+?)(?=\n\s*\n)", profil, re.S | re.M):
        name = m.group(1).strip()
        if name not in leitideen:
            continue
        themen[name] = [s.strip() for s in re.sub(r"\s+", " ", m.group(2)).split("·") if s.strip()]
    fehlt = [l for l in leitideen if l not in themen]
    if fehlt:
        sys.exit(f"{PROFIL}: keine Themenzeile für {fehlt}")
    return head, v, leitideen, themen


def geltung():
    """Geltungstabelle aus iqb.md § 6: Thema × Zielprüfung, ja/nein.
    Liefert (Zielprüfungen, {thema: Menge der Zielprüfungen mit ja})."""
    profil = lies(PROFIL)
    m = re.search(r"^\| Thema \|(.+?)\|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)", profil, re.M)
    if not m:
        sys.exit(f"{PROFIL}: Geltungstabelle nicht gefunden.")
    ziele = [z.strip() for z in m.group(1).split("|") if z.strip()]
    tab = {}
    for zeile in m.group(2).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != len(ziele) + 1:
            sys.exit(f"{PROFIL}: Geltungszeile hat {len(zellen)} Zellen: {zeile}")
        thema, werte = zellen[0], zellen[1:]
        if any(w not in ("ja", "nein") for w in werte):
            sys.exit(f"{PROFIL}: Geltung muss ja oder nein sein: {zeile}")
        tab[thema] = {z for z, w in zip(ziele, werte) if w == "ja"}
    alle = {t for liste in THEMEN.values() for t in liste}
    fehlt = sorted(alle - set(tab))
    if fehlt:
        sys.exit(f"{PROFIL}: Themen ohne Geltungszeile: {fehlt}")
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{PROFIL}: Geltungszeilen ohne Thema in der Liste: {fremd}")
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
    """Gegenstandsklassen je Thema aus iqb.md § 6 (Tabelle „Thema | Gegenstandsklassen").
    Liefert {thema: [Klasse, ...]}; Themen ohne Zeile führen keine Unterklasse."""
    profil = lies(PROFIL)
    m = re.search(r"^\| Thema \| Gegenstandsklassen \|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)",
                  profil, re.M)
    if not m:
        sys.exit(f"{PROFIL}: Tabelle der Gegenstandsklassen nicht gefunden.")
    tab = {}
    for zeile in m.group(1).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != 2:
            sys.exit(f"{PROFIL}: Klassenzeile hat {len(zellen)} Zellen: {zeile}")
        tab[zellen[0]] = [k.strip() for k in zellen[1].split("·") if k.strip()]
    alle = {t for liste in THEMEN.values() for t in liste}
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{PROFIL}: Klassenzeilen ohne Thema in der Liste: {fremd}")
    return tab


HANDLUNG = {"Rechnung": "berechnen", "Begründung": "begründen", "Kurzantwort": "angeben",
            "Ankreuzen": "angeben", "Zeichnen": "zeichnen", "Eintragen": "zeichnen",
            "Konstruieren": "zeichnen", "Tabelle": "angeben"}


def klasse_von(typ):
    """Gegenstandsklasse aus dem Typnamen (Wort vor dem Doppelpunkt) oder leer."""
    m = re.match(r"([^:]+): ", typ)
    return m.group(1) if m else ""


def pruefe_typname(typ, thema, a, wo):
    """Präfixregel iqb.md § 6: Themen mit Klassen verlangen ein gültiges Präfix, andere keins."""
    k = klasse_von(typ)
    if thema in KLASSEN:
        a(k in KLASSEN[thema],
          f"{wo}: Typ „{typ}“ braucht ein Präfix aus {KLASSEN[thema]} (Thema {thema})")
    else:
        a(k == "", f"{wo}: Typ „{typ}“ trägt ein Präfix, Thema {thema} führt keine Klassen")


HEAD, VOK, LEITIDEEN, THEMEN = vokabular()
ZIELE, GELTUNG = geltung()
KLASSEN = klassen()
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
# Stapel 2026-ea-B, MMS-Zweig (Delta gegen den WTR-Zweig, iqb.md § 7). innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Pool 2026 erhöht: Analysis 30 BE, AG/LA und Stochastik 20 BE. Drei der acht MMS-Dateien sind Dubletten der WTR-Dateien
# (AG/LA A2 MMS 1, Stochastik MMS 1 und 2, iqb-quellen.csv) und bekommen keine Zeile; Stochastik MMS 3 Aufgabe 1 ist wortgleich
# mit Stochastik WTR 2 Aufgabe 1 (Dublette unterhalb der Dateiebene, Soll 8). Wortgleiche Teilaufgaben in nicht wortgleichen
# Dateien (AG/LA A1 1a, 2a, 2b, 2d; Stochastik MMS 3 2b, 2c) teilen den Typ, die Felder sind aus der WTR-Zeile übernommen.
# bemerkung trägt je Zeile „MMS-Anteil: …" (rein Rechnerbedienung | Rechner für die Lösung, Ansatz eigen | keiner).

SOLL = {"2026MerhoehtBAnalysisMMS1": 30, "2026MerhoehtBAnalysisMMS2": 30, "2026MerhoehtBAGLAA1MMS": 20,
        "2026MerhoehtBAGLAA2MMS2": 20, "2026MerhoehtBStochastikMMS3": 8}

# ---- Analysis MMS 1 (eine unnummerierte Aufgabe, innen 1): Schar f_a(x) = 60/a · x · (x − a)², Strandbad
KS = "Koordinatensystem x von 0 bis 12 (Stunden seit 9:00 Uhr), y von 0 bis 1200 (Rate in 1/h); Graph von g (durchgezogen) steigt von (0 | 0) bis etwa (3,7 | 1076) und fällt auf (11 | 0); Graph von h (gestrichelt) beginnt flach bei 0, steigt ab etwa x = 2 bis etwa (8,5 | 1200) und fällt auf (12 | 0); Fläche I unter g links vom Schnittpunkt (etwa x = 6,4), Fläche III unter h rechts davon, Fläche II unter beiden Graphen dazwischen"
row("2026MerhoehtBAnalysisMMS1", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Nullstellen einer Schar am Term begründen und Tangentensteigungen dort nachweisen", typ_neben="",
    stichwoerter="Produkt 60/a · x · (x − a)² null nur für x = 0 oder x = a|f_a'(0) = 60a|f_a'(a) = 0 und f_a(a) = 0",
    voraussetzungen="Satz vom Nullprodukt|Produktregel|Tangente als Gerade mit Steigung f'",
    format="Begründung", operator="Begründen Sie|Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f_a(x) = 60/a · x · (x − a)², a > 0; Graph G_a; Punkte A(0; 0) und B(a; 0)",
    gesucht="Begründung, dass G_a die x-Achse nur in A und B schneidet; Nachweis f_a'(0) = 60a und x-Achse als Tangente in B",
    verfahren="Faktoren des Terms null setzen; Ableitung bilden (Rechner), f_a'(0) und f_a'(a) auswerten, f_a(a) = 0 mit f_a'(a) = 0 als Tangente deuten",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="60/a · x · (x − a)² = 0 ⇔ x = 0 ∨ x = a; f_a'(0) = 60a; f_a'(a) = 0, mit f_a(a) = 0 ist die x-Achse Tangente in B (amtlich)",
    zwischenergebnis="f_a'(x) = 60/a · ((x − a)² + 2x(x − a))", niveau_geschaetzt="I",
    fehlerquelle="f_a'(a) = 0 zeigen, aber nicht erwähnen, dass B auf der x-Achse liegt",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Drei Reproduktionen mit mitgeführtem Parameter, in Teil B amtlich I (wie 2026-ga-B Analysis WTR 1, 1c). MMS-Anteil: Rechner für die Ableitung, Ansatz eigen.")

row("2026MerhoehtBAnalysisMMS1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem vorgegebenen Flächeninhalt zwischen Graph und x-Achse berechnen", typ_neben="",
    stichwoerter="∫₀^a f_a(x) dx = 5a³|5a³ = 10|a = ³√2",
    voraussetzungen="Integral mit Parametergrenzen (Rechner)|Gleichung dritten Grades lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = 60/a · x · (x − a)², a > 0; G_a schließt mit der x-Achse eine Fläche ein (zwischen 0 und a)",
    gesucht="a mit Flächeninhalt 10",
    verfahren="Integral von 0 bis a als Term in a berechnen (Rechner), gleich 10 setzen, auflösen",
    schritte="2", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="2026MerhoehtBAnalysisMMS1-1a",
    ergebnis="∫₀^a f_a(x) dx = 10 ⇔ a = ³√2 (amtlich)",
    zwischenergebnis="∫₀^a f_a(x) dx = 5a³", niveau_geschaetzt="II",
    fehlerquelle="Grenzen 0 und a nicht als Nullstellen aus a erkennen; a = ³√2 ≈ 1,26 auf 2 runden",
    bemerkung="Standardbezug: K2 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt: 5a³ = 10. MMS-Anteil: Rechner für Integral und Gleichung, Ansatz eigen.")

row("2026MerhoehtBAnalysisMMS1", "c", innen="1", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für einen Wendepunkt auf einer Geraden berechnen", typ_neben="",
    stichwoerter="f_a''(x) = 0 ⇔ x = 2a/3|f_a(2a/3) = 40a²/9|2a/3 = 40a²/9 ⇔ a = 3/20",
    voraussetzungen="zweite Ableitung (Rechner)|Punktprobe an y = x|Gleichung mit Parameter lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = 60/a · x · (x − a)², a > 0; Gerade y = x",
    gesucht="a, für das der Wendepunkt von G_a auf y = x liegt",
    verfahren="Wendestelle aus f_a'' = 0 als Term in a, Funktionswert dort, Bedingung f_a(x_W) = x_W nach a lösen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f_a''(x) = 0 ⇔ x = 2a/3; 2a/3 = f_a(2a/3) ⇔ a = 3/20 (amtlich)",
    zwischenergebnis="f_a(2a/3) = 40a²/9", niveau_geschaetzt="II",
    fehlerquelle="die Lösung a = 0 der Gleichung mitführen (a > 0 vorausgesetzt)",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Die Bedingung „Wendepunkt auf der Geraden“ ist wörtlich vorgegeben (Punktprobe), keine Deutung. MMS-Anteil: Rechner für Ableitungen und Gleichung, Ansatz eigen.")

row("2026MerhoehtBAnalysisMMS1", "d", innen="1", seite="1|2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Streckfaktoren aus dem Term ablesen und Flächengleichheit der Bilddreiecke über das Produkt der Faktoren beurteilen", typ_neben="",
    stichwoerter="w_a(x) = 11/10 · f_a(11/10 · (12 − x))|s_x = 10/11, s_y = 11/10|Grundseite AB mit s_x gestreckt, Höhe y_C mit s_y|s_x · s_y = 1, Aussage wahr",
    voraussetzungen="Streckung in x-Richtung mit Faktor 1/k bei f(k · x)|Streckung in y-Richtung|Flächeninhalt eines Dreiecks aus Grundseite und Höhe",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Beurteilen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="lang",
    gegeben="w_a(x) = 11/10 · f_a(11/10 · (12 − x)) entsteht aus G_a durch Streckung mit s_x in x-Richtung, Streckung mit s_y in y-Richtung, Spiegelung an der y-Achse, Verschiebung um 12 in x-Richtung; Punkte A(0; 0), B(a; 0), C(x_C; f_a(x_C)) mit 0 < x_C < a auf G_a und ihre Bilder A', B', C' auf dem Graphen von w_a; Aussage: die Dreiecke ABC und A'B'C' sind flächengleich",
    gesucht="s_x und s_y; Beurteilung der Aussage",
    verfahren="Faktor 11/10 im Argument als Streckung um 10/11 in x-Richtung, Vorfaktor 11/10 als Streckung in y-Richtung deuten; Grundseite A'B' = s_x · AB und Höhe y_C' = s_y · y_C, Produkt s_x · s_y = 1 liefert gleichen Flächeninhalt",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="s_x = 10/11, s_y = 11/10; die Aussage ist wahr: mit AB und A'B' als Grundseiten und den y-Koordinaten von C und C' als Höhen gilt |A'B'| = s_x · |AB| und y_C' = s_y · y_C, wegen s_x · s_y = 1 sind die Inhalte gleich (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="s_x = 11/10 (Faktor im Argument nicht invertieren); Spiegelung und Verschiebung als flächenändernd ansehen",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Termidentität geprüft). Eichregel: (c) allgemeiner Nachweis mit den Faktoren, Beziehung s_x · s_y = 1 wird hergeleitet. MMS-Anteil: keiner.")

row("2026MerhoehtBAnalysisMMS1", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Aussage über eine Rate aus dem Nullabschnitt einer abschnittsweise definierten Funktion begründen", typ_neben="",
    stichwoerter="x = 11 entspricht 20:00 Uhr|g(x) = 0 für 11 < x ≤ 12 und g(11) = f_11(11) = 0|Eingangsrate null",
    voraussetzungen="Zeit in Modellvariable umrechnen|abschnittsweise Definition lesen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Strandbad/Besucherzahl", textumfang="mittel",
    gegeben="g(x) = f_11(x) für 0 ≤ x ≤ 11 und g(x) = 0 für 11 < x ≤ 12, x Stunden seit 9:00 Uhr, g(x) Eingangsrate in 1/h; Aussage: das Modell steht in Einklang damit, dass ab 20:00 Uhr kein Gast mehr eingelassen wird",
    gesucht="Begründung der Aussage",
    verfahren="20:00 Uhr als x = 11 erkennen, g(x) = 0 für x ≥ 11 als Eingangsrate null deuten",
    schritte="2", zahlenraum="ganz", einheiten="h", abhaengig_von="",
    ergebnis="im Modell entspricht x = 11 dem Zeitpunkt 20:00 Uhr; für x ≥ 11 ist g(x) = 0, die Eingangsrate ist gemäß dem Modell null (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Uhrzeit 20:00 mit x = 20 gleichsetzen",
    bemerkung="Standardbezug: K1 I, K3 I, K6 I. AB amtlich: I. Amtlich. MMS-Anteil: keiner.")

row("2026MerhoehtBAnalysisMMS1", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Zeitpunkt und Größe der maximalen Änderungsrate über die zweite Ableitung berechnen", typ_neben="",
    stichwoerter="g'(x) = 0 ⇔ x = 11/3 ∨ x = 11|g(11/3) = 9680/9 ≈ 1076, g(11) = 0|12:40 Uhr",
    voraussetzungen="Extremum der Rate über deren Ableitung|Randstelle prüfen|Dezimalstunden in Uhrzeit umrechnen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Strandbad/Besucherzahl", textumfang="kurz",
    gegeben="g wie in e (g = f_11 auf [0; 11]); die Eingangsrate hat genau ein Maximum",
    gesucht="Zeitpunkt und Wert der größten Eingangsrate, rechnerisch",
    verfahren="g'(x) = 0 mit dem Rechner lösen, Werte an den Kandidaten vergleichen, 11/3 h nach 9:00 Uhr umrechnen",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="h|1/h", abhaengig_von="",
    ergebnis="g'(x) = 0 ⇔ x = 11/3 ∨ x = 11; g(11/3) = 9680/9, g(11) = 0; um 12:40 Uhr ist die Eingangsrate mit etwa 1076 1/h am größten (amtlich)",
    zwischenergebnis="11/3 h = 3 h 40 min", niveau_geschaetzt="II",
    fehlerquelle="x = 11/3 als Uhrzeit 11:20 lesen; x = 11 als Maximum nehmen",
    bemerkung="Standardbezug: K3 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B-mms Analysis MMS 1, 1c): dort ist die Rate als Ableitung k' gegeben (k'' = 0), hier ist die Rate g selbst die Funktion (g' = 0) – gleiche Fertigkeit, Vorschlag für den Abgleich: Etikett und Definition auf „Ableitung der Rate“ fassen. MMS-Anteil: Rechner für Ableitung und Gleichung, Ansatz eigen.")

row("2026MerhoehtBAnalysisMMS1", "g", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Gleichheit der Flächen unter Eingangs- und Ausgangsrate als gleiche Gesamtzahl im Sachzusammenhang erläutern", typ_neben="",
    stichwoerter="Fläche unter g = Anzahl aller eintretenden Gäste|Fläche unter h = Anzahl aller Gäste, die gehen|I + II = II + III|jeder Gast betritt und verlässt das Bad",
    voraussetzungen="Integral einer Rate als Bestand|Flächen am Graphen zerlegen",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Koordinatensystem", skizze=KS, kontext="Strandbad/Besucherzahl", textumfang="mittel",
    gegeben="g Eingangsrate, h Ausgangsrate in 1/h auf [0; 12]; die Graphen und die x-Achse schließen die Flächen I (unter g, links vom Schnittpunkt), II (unter beiden) und III (unter h, rechts) ein; außerhalb der Öffnungszeit ist kein Gast im Bad",
    gesucht="Erläuterung im Sachzusammenhang, dass I und III gleichen Inhalt haben",
    verfahren="Flächen unter g und unter h als Gesamtzahl der eintretenden bzw. gehenden Gäste deuten, beide gleich, gemeinsamer Teil II herausnehmen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Inhalt der Fläche zwischen dem Graphen von g und der x-Achse ist die Anzahl aller Gäste, die das Bad betreten, der unter h die Anzahl aller, die es verlassen; am betrachteten Tag betreten ebenso viele Gäste das Bad, wie es verlassen, also sind die Inhalte von I und III gleich (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Flächen I und III direkt vergleichen, ohne den gemeinsamen Teil II zu erwähnen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K6 II. AB amtlich: II. Amtlich. Einfache Deutung der Integrale als Anzahlen, keine Verkettung zweier Deutungen. MMS-Anteil: keiner.")

row("2026MerhoehtBAnalysisMMS1", "h", innen="1", seite="2|3", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Maximum einer Integralfunktion über die Nullstelle des Integranden begründen und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="D'(x) = g(x) − h(x)|x_S einzige Nullstelle von D' in [2; 11]|Vorzeichenwechsel von plus nach minus|größte Zahl gleichzeitig anwesender Gäste",
    voraussetzungen="Hauptsatz: Ableitung einer Integralfunktion ist der Integrand|hinreichende Bedingung über Vorzeichenwechsel|Differenz der Raten als Rate des Bestands",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=KS, kontext="Strandbad/Besucherzahl", textumfang="mittel",
    gegeben="D(x) = ∫₀^x (g(t) − h(t)) dt auf [0; 12]; D nimmt sein Maximum in [2; 11] an; dort schneiden sich die Graphen von g und h genau einmal, bei x_S",
    gesucht="Begründung, dass das Maximum an der Stelle x_S liegt; Bedeutung des Maximums",
    verfahren="D' = g − h, x_S als einzige Nullstelle mit Vorzeichenwechsel von plus nach minus (g > h davor, h > g danach); D als Zahl der anwesenden Gäste deuten",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="in [2; 11] ist x_S wegen D'(x) = g(x) − h(x) die einzige Nullstelle von D', mit Vorzeichenwechsel von plus nach minus, also nimmt D dort das Maximum an; das Maximum ist die größte Anzahl der Gäste, die sich am betrachteten Tag gleichzeitig im Strandbad befinden (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Maximum von D beim Maximum von g vermuten; D als Gesamtzahl der Gäste deuten",
    bemerkung="Standardbezug: K1 III, K2 II, K3 III, K5 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (e) Beziehung zwischen Integrand und Integralfunktion am Graphen deuten, verkettet mit der Sachdeutung als Bestand. MMS-Anteil: keiner.")


# ---- Analysis MMS 2, Aufgabe 1: Wachstumsrate r(t) = 3/4 · t · (t + 4) · e^(−t/2), Pflanze
KR = "Abbildung 1: Koordinatensystem mit Kästchenraster, t von 0 bis 13 (Wochen), y von 0 bis 4 (cm pro Woche); Graph von r beginnt in (0 | 0), steigt bis zum Hochpunkt bei etwa (2,8 | 3,5) und fällt dann langsam gegen 0 (bei t = 13 etwa 0,3)"
row("2026MerhoehtBAnalysisMMS2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Ungleichung für einen Funktionswert im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="r(10) < 1|Wachstumsrate zehn Wochen nach dem Einpflanzen kleiner als 1 cm pro Woche",
    voraussetzungen="Funktionswert mit Variable und Einheit lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Koordinatensystem", skizze=KR, kontext="Pflanzenwachstum", textumfang="mittel",
    gegeben="r(t) = 3/4 · t · (t + 4) · e^(−t/2) Wachstumsrate in cm pro Woche, t Wochen seit dem Einpflanzen; Anfangshöhe 3 cm; r(10) < 1",
    gesucht="Bedeutung von r(10) < 1 im Sachzusammenhang",
    verfahren="Argument als Zeitpunkt, Wert als Rate mit Einheit aussprechen",
    schritte="1", zahlenraum="ganz", einheiten="cm/Woche|Wochen", abhaengig_von="",
    ergebnis="zehn Wochen nach dem Einpflanzen ist die Wachstumsrate der Pflanze kleiner als 1 Zentimeter pro Woche (amtlich)",
    zwischenergebnis="r(10) ≈ 0,71", niveau_geschaetzt="I",
    fehlerquelle="r(10) als Höhe der Pflanze deuten",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt (r(10) ≈ 0,71). MMS-Anteil: keiner.")

row("2026MerhoehtBAnalysisMMS2", "b", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Gleichung f(t) = f(t − c) für gleiche Werte im Abstand c mit dem Rechner lösen und im Graphen darstellen", typ_neben="",
    stichwoerter="r(t) = r(t − 5)|t ≈ 6,0|waagerechte Strecke von (1 | r(1)) nach (6 | r(6)) mit Senkrechten zur t-Achse",
    voraussetzungen="Bedingung „genauso groß wie fünf Wochen davor“ als Gleichung ansetzen|Gleichung numerisch lösen|Punkte gleicher Höhe eintragen",
    format="Rechnung|Zeichnen", operator="Berechnen Sie|Stellen Sie dar", antwort="Zahl|Grafik",
    material="Koordinatensystem", skizze=KR, kontext="Pflanzenwachstum", textumfang="kurz",
    gegeben="r wie in a; es gibt einen Zeitpunkt, zu dem die Wachstumsrate genauso groß ist wie fünf Wochen davor",
    gesucht="dieser Zeitpunkt; Darstellung des Sachverhalts in Abbildung 1",
    verfahren="r(t) = r(t − 5) mit dem Rechner lösen; in der Abbildung die Punkte bei t ≈ 1 und t ≈ 6 auf gleicher Höhe markieren und verbinden",
    schritte="2", zahlenraum="dezimal", einheiten="Wochen", abhaengig_von="",
    ergebnis="r(t) = r(t − 5) liefert t ≈ 6,0; der gesuchte Zeitpunkt ist ungefähr sechs Wochen nach dem Einpflanzen; Darstellung: waagerechte gestrichelte Strecke zwischen den Graphenpunkten bei t ≈ 1 und t ≈ 6 (amtlich)",
    zwischenergebnis="r(1) ≈ r(6) ≈ 2,3", niveau_geschaetzt="II",
    fehlerquelle="r(t) = r(5) statt r(t − 5) ansetzen; die triviale Lösung r(t) = r(t) für t = 2,5 vermuten",
    bemerkung="Standardbezug: K2 II, K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt: t ≈ 5,98. Die Übersetzung „genauso groß wie fünf Wochen davor“ ist wörtlich vorgegeben, keine Deutung. Thema Gleichungen lösen, weil die Leistung das Aufstellen und numerische Lösen der Gleichung ist. MMS-Anteil: Rechner für die Lösung, Ansatz eigen.")

row("2026MerhoehtBAnalysisMMS2", "c", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Zeitpunkt der maximalen Rate über die Ableitung der Ratenfunktion berechnen", typ_neben="",
    stichwoerter="r'(t) = 0|t = 2√2 ≈ 2,8 Wochen",
    voraussetzungen="schnellstes Wachstum als Maximum der Rate|Ableitung mit dem Rechner|Gleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Pflanzenwachstum", textumfang="kurz",
    gegeben="r wie in a",
    gesucht="Zeitpunkt, zu dem die Pflanze am schnellsten wächst",
    verfahren="r'(t) = 0 lösen (positive Lösung), als Zeitpunkt angeben",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="Wochen", abhaengig_von="",
    ergebnis="r'(t) = 0 liefert t = 2√2, die Pflanze wächst etwa 2,8 Wochen nach dem Einpflanzen am schnellsten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="r''(t) = 0 lösen (Wendestelle der Rate statt Maximum der Rate)",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Nicht wiederverwendet: „Zeitpunkt der größten Rate aus der Ableitung angeben“ (dort ist die Ableitung als Term gegeben und der Zeitpunkt wird angegeben, hier wird r' gebildet und die Gleichung gelöst). MMS-Anteil: Rechner für Ableitung und Gleichung, Ansatz eigen.")

row("2026MerhoehtBAnalysisMMS2", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Integralfunktion einer Rate und ihren Grenzwert als Bestand und Endwert im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="w' = r, w(0) = 0|w(t) Zunahme der Höhe seit dem Einpflanzen|w(t) + 3 Höhe|lim (w(t) + 3) = 27: Höhe strebt gegen 27 cm",
    voraussetzungen="Stammfunktion einer Rate als Bestandszunahme|Anfangswert addieren|Grenzwert als Endzustand deuten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Pflanzenwachstum", textumfang="mittel",
    gegeben="w mit w' = r und w(0) = 0; lim (w(t) + 3) = 27 für t → ∞; Anfangshöhe 3 cm",
    gesucht="Bedeutung von w(t) und des Wertes 27 im Sachzusammenhang",
    verfahren="w als Integral der Rate ab 0 deuten (Höhenzunahme), w(t) + 3 als Höhe, Grenzwert als Höhe, der sich die Pflanze nähert",
    schritte="2", zahlenraum="ganz", einheiten="cm", abhaengig_von="",
    ergebnis="w(t) gibt die Zunahme der Höhe der Pflanze seit dem Einpflanzen in Zentimetern an; der Wert 27 gibt an, dass die Höhe der Pflanze gegen 27 cm strebt (amtlich)",
    zwischenergebnis="∫₀^∞ r(t) dt = 24", niveau_geschaetzt="II",
    fehlerquelle="w(t) als Höhe der Pflanze deuten (Anfangshöhe 3 cm vergessen)",
    bemerkung="Standardbezug: K2 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Integral über [0; ∞) gleich 24). MMS-Anteil: keiner.")

# ---- Analysis MMS 2, Aufgabe 2: Schar f_a(x) = 3/4 · (x² − a²) · e^(1 − x/a), h(x) = k · ln x
KA2 = "Abbildung 2: Koordinatensystem mit Kästchenraster, x von 0 bis 10, y von −3 bis 4; Graph von f_1' (durchgezogen) beginnt bei (0 | 2), steigt kurz auf etwa (0,4 | 2,2), fällt durch (1 | 1,5) und die x-Achse bei etwa x = 2,4 auf einen Tiefpunkt nahe (3,5 | −0,3) und nähert sich von unten der x-Achse; Graph von h' (gestrichelt) fällt von großen Werten bei x nahe 0 durch (1 | 1,5) monoton gegen 0; einziger gemeinsamer Punkt (1 | f_1'(1))"
row("2026MerhoehtBAnalysisMMS2", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Nullstellen einer Schar angeben und Vorzeichen des y-Achsenabschnitts begründen", typ_neben="",
    stichwoerter="x² − a² = 0 ⇔ x = ±a|f_a(0) = −3/4 · a² · e < 0 wegen a² > 0",
    voraussetzungen="Nullprodukt mit e-Faktor ungleich null|Vorzeichen eines Terms mit Parameter",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_a(x) = 3/4 · (x² − a²) · e^(1 − x/a), a > 0; Graph G_a",
    gesucht="Nullstellen von f_a; Begründung, dass G_a die y-Achse unterhalb der x-Achse schneidet",
    verfahren="x² − a² = 0 lösen; f_a(0) berechnen und Vorzeichen begründen",
    schritte="2", zahlenraum="negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="Nullstellen −a und a; f_a(0) = −3/4 · a² · e < 0 wegen a² > 0 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur x = a als Nullstelle angeben",
    bemerkung="Standardbezug: K1 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner.")

row("2026MerhoehtBAnalysisMMS2", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Parameter einer Logarithmusfunktion aus einer gemeinsamen Tangente mit einer Scharkurve berechnen und Tangentengleichung angeben", typ_neben="",
    stichwoerter="h(1) = 0 = f_1(1)|h'(1) = k = f_1'(1) = 3/2|y = 3/2 · x − 3/2",
    voraussetzungen="gemeinsame Tangente heißt gleicher Punkt und gleiche Steigung|Ableitung von k · ln x|Punkt-Steigungs-Form",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f_1(x) = 3/4 · (x² − 1) · e^(1 − x); h(x) = k · ln x auf IR⁺ mit k > 0; die Graphen von f_1 und h haben im Punkt (1; 0) eine gemeinsame Tangente",
    gesucht="k und eine Gleichung der gemeinsamen Tangente",
    verfahren="f_1'(1) berechnen (Rechner), mit h'(1) = k gleichsetzen; Tangente durch (1; 0) mit Steigung 3/2",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="h'(1) = f_1'(1) ⇔ k = 3/2; Tangente y = 3/2 · x − 3/2 (amtlich)",
    zwischenergebnis="f_1'(1) = 3/2", niveau_geschaetzt="II",
    fehlerquelle="k aus h(1) = f_1(1) bestimmen wollen (liefert 0 = 0)",
    bemerkung="Standardbezug: K2 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: Rechner für die Ableitung, Ansatz eigen.")

row("2026MerhoehtBAnalysisMMS2", "c", innen="2", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Anzahl der gemeinsamen Punkte zweier Graphen aus dem Vergleich ihrer Ableitungsgraphen begründen", typ_neben="",
    stichwoerter="genau ein gemeinsamer Punkt (1 | 0)|für x > 1 ist h' > f_1', die Differenz h − f_1 wächst ab 0|für x < 1 ist h' > f_1', die Differenz f_1 − h wächst mit abnehmendem x ab 0",
    voraussetzungen="Vorzeichen der Ableitung der Differenz als Monotonie|gemeinsamer Punkt als Nullstelle der Differenz|Abbildung lesen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="Koordinatensystem", skizze=KA2, kontext="ohne", textumfang="mittel",
    gegeben="Abbildung 2 mit den Graphen von f_1' und h'; einziger gemeinsamer Punkt der Ableitungsgraphen (1; f_1'(1)); f_1(1) = h(1) = 0 aus b",
    gesucht="Anzahl der gemeinsamen Punkte der Graphen von f_1 und h, ohne weitere Rechnung mit Abbildung 2 begründet",
    verfahren="Differenz h − f_1 betrachten: sie ist bei x = 1 null und wegen h' > f_1' rechts von 1 streng wachsend, links von 1 (mit abnehmendem x) ebenfalls betragsmäßig wachsend, also sonst nie null",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2026MerhoehtBAnalysisMMS2-2b",
    ergebnis="die Graphen besitzen genau einen gemeinsamen Punkt: für x > 1 wird die Differenz h(x) − f_1(x) wegen h'(x) > f_1'(x) für zunehmende x kontinuierlich größer und ist wegen h(1) − f_1(1) = 0 positiv; für x < 1 wird f_1(x) − h(x) wegen h'(x) > f_1'(x) für abnehmende x kontinuierlich größer und ist ebenfalls positiv (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="aus dem einen Schnittpunkt der Ableitungsgraphen direkt auf einen Schnittpunkt der Graphen schließen, ohne die Monotonie der Differenz",
    bemerkung="Standardbezug: K1 III, K2 II, K4 II, K6 III. AB amtlich: III. Amtlich. Eichregel: (e) Beziehung zwischen Ableitungsgraphen und Graphen deuten – aus h' > f_1' auf die Monotonie der Differenz schließen, verkettet mit dem gemeinsamen Punkt aus b. MMS-Anteil: keiner.")

row("2026MerhoehtBAnalysisMMS2", "d", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für Hoch- und Tiefpunkt als Gegenecken eines achsenparallelen Quadrats bestimmen", typ_neben="",
    stichwoerter="f_a'(x) = 0 ⇔ x = a − a√2 ∨ x = a + a√2|Quadrat: Differenz der x-Koordinaten gleich Differenz der y-Koordinaten|a ≈ 0,82",
    voraussetzungen="Extremstellen einer Schar (Rechner)|Quadratbedingung als Gleichung|Gleichung numerisch lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="f_a(x) = 3/4 · (x² − a²) · e^(1 − x/a), a > 0; jeder Graph hat einen Tiefpunkt T_a und einen Hochpunkt H_a; für einen Wert von a sind T_a und H_a gegenüberliegende Ecken eines achsenparallelen Quadrats",
    gesucht="dieser Wert von a auf Hundertstel gerundet",
    verfahren="Extremstellen als Terme in a berechnen; Bedingung: waagerechter Abstand der Extremstellen gleich Differenz der Funktionswerte; Gleichung in a mit dem Rechner lösen",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="", abhaengig_von="",
    ergebnis="f_a'(x) = 0 ⇔ x = a − a√2 ∨ x = a + a√2; (a + a√2) − (a − a√2) = f_a(a + a√2) − f_a(a − a√2) liefert a ≈ 0,82 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Quadratbedingung als gleiche Koordinaten eines Punktes statt als gleiche Kantenlängen ansetzen",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt: a ≈ 0,823. Eichregel: (a) die geometrische Bedingung „gegenüberliegende Ecken eines achsenparallelen Quadrats“ muss erst in eine Gleichung übersetzt werden. MMS-Anteil: Rechner für Extremstellen und Gleichung, Ansatz eigen.")

row("2026MerhoehtBAnalysisMMS2", "e", innen="2", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Prozentuale Abweichung einer Dreiecksnäherung vom Flächeninhalt zwischen Scharkurve und Achsen als parameterunabhängig nachweisen", typ_neben="",
    stichwoerter="Dreieck O, (0 | f_a(0)), (a | 0): Inhalt −1/2 · a · f_a(0)|Fläche −∫₀^a f_a(x) dx|Quotient e/(2(4 − e)) ≈ 1,06|Abweichung etwa 6 %",
    voraussetzungen="Fläche unterhalb der x-Achse als negatives Integral|Integral mit Parametergrenze (Rechner)|Quotient kürzen|prozentuale Abweichung",
    format="Begründung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="lang",
    gegeben="f_a wie in a; im vierten Quadranten schließt G_a mit den Koordinatenachsen eine Fläche ein; Vergleichsdreieck mit den Ecken O, Schnittpunkt mit der y-Achse (0; f_a(0)) und Schnittpunkt mit der positiven x-Achse (a; 0)",
    gesucht="Nachweis, dass die prozentuale Abweichung des Dreiecksinhalts vom Flächeninhalt nicht von a abhängt; Wert der Abweichung",
    verfahren="Dreiecksinhalt −1/2 · a · f_a(0) und Flächeninhalt −∫₀^a f_a(x) dx als Terme in a (Rechner), Quotient bilden und kürzen",
    schritte="3", zahlenraum="Potenz|Prozent", einheiten="", abhaengig_von="2026MerhoehtBAnalysisMMS2-2a",
    ergebnis="(−1/2 · a · f_a(0)) / (−∫₀^a f_a(x) dx) = e/(2 · (4 − e)) ≈ 1,06, unabhängig von a; die prozentuale Abweichung beträgt etwa 6 % (amtlich)",
    zwischenergebnis="Dreieck 3/8 · a³ · e|Fläche 3/4 · a³ · (4 − e)", niveau_geschaetzt="II",
    fehlerquelle="Integral mit Vorzeichen als Fläche nehmen (negativer Quotient); Abweichung als 1,06 statt 6 % angeben",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt (Quotient exakt e/(8 − 2e)). Kein Eintrag der Deutungsliste: der Nachweis ist das Nachrechnen eines Quotienten mit mitgeführtem Parameter, a kürzt sich – Routine, II. MMS-Anteil: Rechner für das Integral, Ansatz eigen.")


# ---- AG/LA A1 MMS: Quader (Aufgabe 1) und Verflechtung (Aufgabe 2); 1a, 2a, 2b, 2d wortgleich mit dem WTR-Zweig (erzeugte Zeilen unten)
row("2026MerhoehtBAGLAA1MMS", "b", innen="1", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Oberflächeninhalt berechnen", typ_neben="",
    stichwoerter="AG = (−6; 8; h), CE = (6; −8; h)|AG · CE = −100 + h² = 0 ⇔ h = 10|Oberfläche 2 · (6 · 8 + 6 · 10 + 8 · 10) = 376",
    voraussetzungen="Eckpunkte des Quaders ergänzen|Skalarprodukt null für Orthogonalität|Oberfläche eines Quaders",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze="Schrägbild eines Quaders ABCDEFGH, aufgespannt von u (AB), v (AD), w (AE); A vorn links unten",
    kontext="ohne", textumfang="mittel",
    gegeben="A(6; 0; 0), B(6; 8; 0), C(0; 8; 0), E(6; 0; h) mit h > 0; die Raumdiagonalen AG und CE schneiden sich senkrecht",
    gesucht="h und der Inhalt der Oberfläche des Quaders",
    verfahren="G(0; 8; h) ergänzen, Skalarprodukt der Diagonalenvektoren null setzen, h > 0 wählen; Oberfläche aus den drei Kantenlängen 6, 8, 10",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="AG · CE = 0 ⇔ h = 10; Inhalt der Oberfläche 2 · (6 · 8 + 6 · 10 + 8 · 10) = 376 (amtlich)",
    zwischenergebnis="AG = (−6; 8; h), CE = (6; −8; h)", niveau_geschaetzt="II",
    fehlerquelle="h = −10 nicht ausschließen; nur drei Seitenflächen addieren",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung. Die WTR-Fassung (1b) verlangt statt der Oberfläche das Volumen; Vorschlag für den Abgleich: beide Etiketten zu „… und Volumen oder Oberflächeninhalt berechnen“ zusammenziehen. MMS-Anteil: Rechner für Skalarprodukt und Gleichung, Ansatz eigen.")

row("2026MerhoehtBAGLAA1MMS", "c", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Maximale Produktionsmenge aus dem Rohstoffvorrat ermitteln", typ_neben="",
    stichwoerter="e2 = 2e, e1 = e|N · (e; 2e) = (98e; 103e; 118e)|118e ≤ 1298 ⇔ e ≤ 11|maximal 22 ME von E2",
    voraussetzungen="Auftrag als Vektor mit Parameter|Gesamtmatrix mal Vektor|schärfste der drei Ungleichungen|Verdopplung nicht vergessen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Produktion/Verflechtung", textumfang="mittel",
    gegeben="N = R · Z = ((32; 33), (35; 34), (40; 39)); von jedem Rohstoff 1298 ME vorhanden; doppelt so viele ME von E2 wie von E1",
    gesucht="maximale Anzahl ME von E2 für diesen Auftrag",
    verfahren="Endproduktvektor (e; 2e) ansetzen, Rohstoffbedarf N · (e; 2e) als Terme in e, jede Komponente höchstens 1298, kleinste Schranke nehmen, e2 = 2e",
    schritte="4", zahlenraum="ganz", einheiten="", abhaengig_von="2026MerhoehtBAGLAA1MMS-2b",
    ergebnis="aus N · (e; 2e) = (98e; 103e; 118e) und 118e ≤ 1298 folgt e ≤ 11; es können maximal 22 Mengeneinheiten von E2 gefertigt werden (amtlich)",
    zwischenergebnis="1298/118 = 11", niveau_geschaetzt="II",
    fehlerquelle="e = 11 als Antwort geben statt e2 = 22; die Schranke aus der ersten Zeile (98e) nehmen",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B-wtr, dort e1 = 0 und 429 ME): gleiche Fertigkeit, anderer Auftrag; deshalb keine geteilte Zeile. Aufgabengruppe A1, außerhalb der Geltung. MMS-Anteil: Rechner für Matrix-Vektor-Produkt und Ungleichung, Ansatz eigen.")

# ---- AG/LA A2 MMS 2 (eine unnummerierte Aufgabe, innen 1): Dreieck ABC in E, Ebenenschar E_m durch Drehung um g
KD = "Abbildung 1: Koordinatensystem x1 (nach vorn links), x2 (nach rechts), x3 (nach oben); Dreieck ABC grau mit A auf der x1-Achse, B auf der x2-Achse, C auf der x3-Achse; Seite AB als Strecke vorn, Höhen von C gestrichelt"
KL = "Abbildung 2: zwei Koordinatensysteme (x1, x2, x3) mit je einem grauen Dreieck; Lage 1: Ecken auf der positiven x1-Achse, der positiven x2-Achse und der negativen x3-Achse (Dreieck unter der x1x2-Ebene); Lage 2: Ecken auf der positiven x1-Achse, der negativen x2-Achse und der positiven x3-Achse"
row("2026MerhoehtBAGLAA2MMS2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen", typ_neben="",
    stichwoerter="M(6; 6; 0) Mitte von AB|AB = (−12; 12; 0), MC = (−6; −6; 6)|1/2 · 12√2 · 6√3 = 36√6",
    voraussetzungen="Mittelpunkt einer Strecke|Betrag eines Vektors|Dreiecksfläche aus Grundseite und Höhe",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=KD, kontext="ohne", textumfang="mittel",
    gegeben="A(12; 0; 0), B(0; 12; 0), C(0; 0; 6) Schnittpunkte der Ebene E mit den Koordinatenachsen, Eckpunkte des Dreiecks ABC",
    gesucht="Flächeninhalt des Dreiecks ABC",
    verfahren="AC = BC, also gleichschenklig: Mittelpunkt M von AB, Höhe |MC|, Fläche 1/2 · |AB| · |MC| (oder halber Betrag des Vektorprodukts)",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="1/2 · |AB| · |MC| = 36√6 mit dem Mittelpunkt M(6; 6; 0) der Seite AB (amtlich)",
    zwischenergebnis="|AB| = 12√2|MC = (−6; −6; 6), |MC| = 6√3", niveau_geschaetzt="I",
    fehlerquelle="Höhe als |OC| = 6 nehmen (Lot von C fällt nicht auf AB)",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt: 36√6 ≈ 88,2. Typ wiederverwendet (Teil A). MMS-Anteil: Rechner für Beträge, Ansatz eigen.")

row("2026MerhoehtBAGLAA2MMS2", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="n ⊥ AB und n ⊥ AC|n = (1; 1; 2)|d = 12 aus A|x1 + x2 + 2x3 = 12",
    voraussetzungen="Normalenvektor aus zwei Skalarprodukten oder Vektorprodukt|Konstante über Punktprobe",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Koordinatensystem", skizze=KD, kontext="ohne", textumfang="kurz",
    gegeben="A(12; 0; 0), B(0; 12; 0), C(0; 0; 6) in E; Kontrolle x1 + x2 + 2x3 = 12",
    gesucht="Koordinatengleichung von E",
    verfahren="Normalenvektor aus AB · n = 0 und AC · n = 0 (oder Achsenabschnittsform x1/12 + x2/12 + x3/6 = 1), d aus A",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="AB · n = 0 ∧ AC · n = 0 liefert n = (1; 1; 2); aus A ∈ E folgt d = 12, also E: x1 + x2 + 2x3 = 12 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Normalenvektor (1; 1; 1) aus den Achsenabschnitten raten",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Lauf 7). MMS-Anteil: Rechner für Gleichungssystem oder Vektorprodukt, Ansatz eigen.")

row("2026MerhoehtBAGLAA2MMS2", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Aussage über das Innere eines Dreiecks unter Koordinatentausch mit einem Gegenbeispiel widerlegen", typ_neben="",
    stichwoerter="P(1; 1; 5) innen: 1 + 1 + 2 · 5 = 12, alle Koordinaten positiv|Q(1; 5; 1): 1 + 5 + 2 · 1 = 8 ≠ 12, nicht in E|Aussage falsch",
    voraussetzungen="Punkt im Innern des Achsendreiecks über Ebenengleichung und positive Koordinaten|Punktprobe|Gegenbeispiel genügt",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=KD, kontext="ohne", textumfang="mittel",
    gegeben="E: x1 + x2 + 2x3 = 12; Aussage: für jeden Punkt P(u; v; w) im Innern des Dreiecks ABC liegt auch Q(u; w; v) im Innern von ABC",
    gesucht="Begründung, dass die Aussage falsch ist",
    verfahren="einen inneren Punkt mit v ≠ w wählen (Ebenengleichung erfüllt, alle Koordinaten positiv), den vertauschten Punkt in die Ebenengleichung einsetzen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="2026MerhoehtBAGLAA2MMS2-1b",
    ergebnis="P(1; 1; 5) liegt im Innern von ABC, da 1 + 1 + 2 · 5 = 12 gilt und alle Koordinaten positiv sind; Q(1; 5; 1) liegt wegen 1 + 5 + 2 · 1 ≠ 12 nicht in E (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="einen Punkt mit v = w wählen (dann ist Q = P); vergessen zu prüfen, dass P wirklich innen liegt",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Widerlegen durch ein Gegenbeispiel mit Punktprobe, keine Deutung im Sinn der Liste. MMS-Anteil: keiner.")

row("2026MerhoehtBAGLAA2MMS2", "d", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Lage einer Geraden in einer Ebene durch Einsetzen nachweisen", typ_neben="",
    stichwoerter="g: (3; 1; 4) + r · (1; −1; 0)|(3 + r) + (1 − r) + 2 · 4 = 12 für alle r",
    voraussetzungen="allgemeinen Geradenpunkt in die Koordinatengleichung einsetzen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E: x1 + x2 + 2x3 = 12; g: x = (3; 1; 4) + r · (1; −1; 0), r ∈ IR",
    gesucht="Nachweis, dass g in E liegt",
    verfahren="Koordinaten des allgemeinen Geradenpunkts einsetzen, r fällt heraus",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MerhoehtBAGLAA2MMS2-1b",
    ergebnis="Einsetzen von (3 + r; 1 − r; 4) in die Gleichung von E liefert die wahre Aussage 3 + r + 1 − r + 2 · 4 = 12 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur den Stützpunkt prüfen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A). MMS-Anteil: keiner.")

row("2026MerhoehtBAGLAA2MMS2", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharparameter für einen vorgegebenen Winkel zwischen Ebene und Scharebene berechnen", typ_neben="",
    stichwoerter="E_m: x1 + x2 − m · x3 = 4(1 − m), Drehung um g|cos 60° = |(1; 1; 2) · (1; 1; −m)| / (√6 · √(2 + m²))|m = (8 − 3√6)/5 ∨ m = (8 + 3√6)/5",
    voraussetzungen="Winkel zwischen Ebenen über die Normalenvektoren|Betragsgleichung mit Parameter lösen|Drehung liefert zwei Lagen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="E: x1 + x2 + 2x3 = 12; Schar E_m: x1 + x2 − m · x3 = 4 · (1 − m), m ∈ IR, jede E_m entsteht aus E durch Drehung um g; Drehwinkel 60°",
    gesucht="alle m, für die E_m einer um 60° gedrehten Lage entspricht",
    verfahren="Normalenvektoren (1; 1; 2) und (1; 1; −m), Winkelformel gleich cos 60° = 1/2 setzen, nach m auflösen (Rechner)",
    schritte="3", zahlenraum="Wurzel|Bruch", einheiten="Grad", abhaengig_von="2026MerhoehtBAGLAA2MMS2-1b",
    ergebnis="cos 60° = |(1; 1; 2) · (1; 1; −m)| / (|(1; 1; 2)| · |(1; 1; −m)|) ⇔ m = (8 − 3√6)/5 ∨ m = (8 + 3√6)/5 (amtlich)",
    zwischenergebnis="m ≈ 0,13 und m ≈ 3,07", niveau_geschaetzt="II",
    fehlerquelle="Betrag im Zähler weglassen und nur eine Lösung finden",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Nicht wiederverwendet: „Scharparameter für einen vorgegebenen Schnittwinkel zwischen Achse und Ebene ermitteln“ (Sinusformel Gerade–Ebene, hier Kosinusformel Ebene–Ebene). MMS-Anteil: Rechner für die Gleichung, Ansatz eigen.")

row("2026MerhoehtBAGLAA2MMS2", "f", innen="1", seite="2", punkte="6", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Mögliche Lage des Achsendreiecks einer Ebenenschar über die Vorzeichen der Achsenabschnitte entscheiden und den Parameterbereich bestimmen", typ_neben="",
    stichwoerter="A_m(4(1 − m); 0; 0), B_m(0; 4(1 − m); 0), C_m(0; 0; 4 − 4/m)|x1-Abschnitt und x2-Abschnitt haben stets gleiches Vorzeichen: Lage 2 unmöglich|Lage 1: 4(1 − m) > 0 und 4 − 4/m < 0 ⇔ 0 < m < 1",
    voraussetzungen="Achsenschnittpunkte einer Ebene mit Parameter|Vorzeichen von Termen mit Parameter|Bruchungleichung mit Fallunterscheidung",
    format="Begründung|Rechnung", operator="Entscheiden Sie|Begründen Sie|Bestimmen Sie", antwort="Text|Term",
    material="Koordinatensystem", skizze=KL, kontext="ohne", textumfang="lang",
    gegeben="E_m: x1 + x2 − m · x3 = 4 · (1 − m), m ≠ 0, m ≠ 1; Achsenschnittpunkte A_m, B_m, C_m; Abbildung 2 mit Lage 1 (A, B positiv, C negativ) und Lage 2 (A positiv, B negativ, C positiv)",
    gesucht="welche Lage das Dreieck A_mB_mC_m nicht annehmen kann, mit Begründung; alle m für die andere Lage",
    verfahren="Achsenabschnitte als Terme in m; x1- und x2-Abschnitt gleich, also gleiches Vorzeichen (Lage 2 ausgeschlossen); Lage 1 als Ungleichungssystem 4(1 − m) > 0 und 4 − 4/m < 0 lösen",
    schritte="4", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="A_m(4 · (1 − m); 0; 0), B_m(0; 4 · (1 − m); 0), C_m(0; 0; 4 − 4/m); Lage 2 wird nicht angenommen, da die x1-Koordinate von A_m und die x2-Koordinate von B_m für jedes m das gleiche Vorzeichen haben; Lage 1 genau dann, wenn 4 · (1 − m) > 0 (m < 1) und 4 − 4/m < 0 (0 < m < 1), also 0 < m < 1 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="4 − 4/m < 0 mit m multiplizieren ohne Vorzeichenfall; Lage 1 und 2 in der Abbildung verwechseln",
    bemerkung="Standardbezug: K1 III, K2 III, K4 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Lage des Dreiecks in Vorzeichenbedingungen der Achsenabschnitte übersetzen, mit Fallunterscheidung an der Bruchungleichung. MMS-Anteil: Rechner für die Ungleichungen, Ansatz eigen.")

# 2026MerhoehtBAGLAA1MMS 1a = 2026MerhoehtBAGLAA1WTR-1a
row("2026MerhoehtBAGLAA1MMS", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie",
    thema="Vektoren und Rechenoperationen",
    typ="Verbindungsvektor zweier Kantenmittelpunkte als Linearkombination der Kantenvektoren angeben",
    typ_neben="",
    stichwoerter="M1 Mitte von BC, M2 Mitte von EF|M1M2 = −½ u − ½ v + w|r = s = −1/2, t = 1",
    voraussetzungen="Mittelpunkte über halbe Kanten|Vektorkette im Quader",
    format="Zeichnen|Kurzantwort",
    operator="Zeichnen Sie ein|Geben Sie an",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild eines Quaders ABCDEFGH, aufgespannt von u (AB), v (AD), w (AE); A vorn links unten",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Quader ABCDEFGH von u, v, w aufgespannt; M1 Mittelpunkt von BC, M2 Mittelpunkt von EF",
    gesucht="Strecke M1M2 in der Abbildung und r, s, t mit M1M2 = r u + s v + t w",
    verfahren="Weg von M1 über B und A nach E und M2 als Vektorkette",
    schritte="2",
    zahlenraum="Bruch|negativ",
    einheiten="",
    abhaengig_von="",
    ergebnis="r = s = −1/2; t = 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen von r (Richtung von u)",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung. Teilaufgabe wortgleich mit dem WTR-Zweig (2026-ea-B-wtr, Datei 2026MerhoehtBAGLAA1WTR, Teilaufgabe 1a), geteilter Typ, Felder übernommen. MMS-Anteil: keiner (Zeichnen, Linearkombination ablesen).")

# 2026MerhoehtBAGLAA1MMS 2a = 2026MerhoehtBAGLAA1WTR-2a
row("2026MerhoehtBAGLAA1MMS", "a", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie",
    thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Rohstoffbedarf über die Verflechtungsmatrix berechnen",
    typ_neben="",
    stichwoerter="z = Z · (1; 1) = (5; 5; 4)|r1 = 5 · 5 + 4 · 5 + 5 · 4 = 65",
    voraussetzungen="zweistufige Verflechtung|Matrix-Vektor-Produkt|eine Zeile der Rohstoffmatrix",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Produktion/Verflechtung",
    textumfang="lang",
    gegeben="R · z = r mit R = ((5; 4; 5), (4; 5; 6), (5; 6; 6)); Z · e = z mit Z = ((2; 3), (3; 2), (2; 2)); je eine ME von E1 und E2",
    gesucht="ME der drei Zwischenprodukte und des Rohstoffs R1",
    verfahren="Z · (1; 1), dann erste Zeile von R mal z",
    schritte="2",
    zahlenraum="ganz",
    einheiten="",
    abhaengig_von="",
    ergebnis="(z1; z2; z3) = ((2; 3), (3; 2), (2; 2)) · (1; 1) = (5; 5; 4); r1 = 5 · 5 + 4 · 5 + 5 · 4 = 65 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="R mit e statt mit z multiplizieren",
    bemerkung="Standardbezug: K2 II, K3 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zweistufig). Aufgabengruppe A1, außerhalb der Geltung. Teilaufgabe wortgleich mit dem WTR-Zweig (2026-ea-B-wtr, Datei 2026MerhoehtBAGLAA1WTR, Teilaufgabe 2a), geteilter Typ, Felder übernommen. MMS-Anteil: Rechner für die Matrix-Vektor-Produkte, Ansatz eigen.")

# 2026MerhoehtBAGLAA1MMS 2b = 2026MerhoehtBAGLAA1WTR-2b
row("2026MerhoehtBAGLAA1MMS", "b", innen="2", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie",
    thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Gesamtmatrix im Sachzusammenhang deuten",
    typ_neben="",
    stichwoerter="R · Z = ((32; 33), (35; 34), (40; 39)) ordnet Endproduktmengen direkt Rohstoffmengen zu",
    voraussetzungen="Produkt zweier Bedarfsmatrizen als Gesamtbedarf",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Produktion/Verflechtung",
    textumfang="kurz",
    gegeben="R · Z = ((32; 33), (35; 34), (40; 39))",
    gesucht="Bedeutung der Matrix",
    verfahren="Gesamtmatrix als Rohstoff-Endprodukt-Verflechtung deuten",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    abhaengig_von="",
    ergebnis="mithilfe der berechneten Matrix können aus gegebenen Anzahlen der Mengeneinheiten der beiden Endprodukte die hierfür benötigten Anzahlen der Mengeneinheiten der drei Rohstoffe berechnet werden (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauscht deuten",
    bemerkung="Standardbezug: K3 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung. Teilaufgabe wortgleich mit dem WTR-Zweig (2026-ea-B-wtr, Datei 2026MerhoehtBAGLAA1WTR, Teilaufgabe 2b), geteilter Typ, Felder übernommen. In der MMS-Fassung ist N nur als Produkt bezeichnet, nicht ausgerechnet (Rechner); die Deutung ist dieselbe. MMS-Anteil: Rechner für das Produkt, Deutung eigen.")

# 2026MerhoehtBAGLAA1MMS 2d = 2026MerhoehtBAGLAA1WTR-2d
row("2026MerhoehtBAGLAA1MMS", "d", innen="2", seite="2", punkte="5", afb_amtlich="I|II|III",
    leitidee="Analytische Geometrie",
    thema="Matrizen und Übergangsprozesse",
    typ="Verflechtung: Maximale Kostensteigerung eines Rohstoffs aus einer Kostenschranke bestimmen",
    typ_neben="",
    stichwoerter="Kosten je ME E1 heute: 32 · 5 + 35 · 6 + 40 · 7 = 650|nach fünf Jahren: (160 + 210) · 1,03⁵ + 280 · x⁵|≤ 1,2 · 650 ⇔ x ≤ ⁵√((780 − 370 · 1,03⁵)/280) ≈ 1,0463|höchstens etwa 4,6 % pro Jahr",
    voraussetzungen="Rohstoffbedarf je ME E1 aus der Gesamtmatrix|Kosten als Summe Menge mal Preis|exponentielles Wachstum über fünf Jahre|Ungleichung nach x auflösen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Tabelle Rohstoff R1, R2, R3 mit Anschaffungskosten 5, 6, 7 je ME",
    kontext="Produktion/Verflechtung",
    textumfang="lang",
    gegeben="Kosten je ME 5, 6, 7 GE; R1, R2 steigen 3 % je Jahr; Gesamtkosten der Rohstoffe für E1 dürfen in fünf Jahren um höchstens 20 % steigen",
    gesucht="maximaler jährlicher prozentualer Anstieg für R3",
    verfahren="Kostenterm heute und in fünf Jahren aufstellen, Ungleichung nach dem Wachstumsfaktor lösen",
    schritte="5",
    zahlenraum="dezimal|Potenz|Prozent",
    einheiten="GE|Prozent",
    abhaengig_von="2026MerhoehtBAGLAA1MMS-2b",
    ergebnis="K0 = 32 · 5 + 35 · 6 + 40 · 7 = 650; K5 = (32 · 5 + 35 · 6) · 1,03⁵ + 40 · 7 · x⁵ = 370 · 1,03⁵ + 280 · x⁵; mit K5 ≤ 1,2 · K0 folgt x ≤ ⁵√((1,2 · 650 − 370 · 1,03⁵)/280) ≈ 1,0463; der maximale Anstieg beträgt etwa 4,6 % pro Jahr (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Anstieg linear (5 · 3 %) statt exponentiell ansetzen",
    bemerkung="Standardbezug: K2 III, K3 III, K4 I, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Kostenschranke in eine Ungleichung mit Wachstumsfaktor übersetzen, verkettet über Matrix, Kosten und Wurzel. Aufgabengruppe A1, außerhalb der Geltung. Teilaufgabe wortgleich mit dem WTR-Zweig (2026-ea-B-wtr, Datei 2026MerhoehtBAGLAA1WTR, Teilaufgabe 2d), geteilter Typ, Felder übernommen. In der MMS-Fassung 5 statt 6 BE (Lösen der Ungleichung im Rechner). MMS-Anteil: Rechner für die Lösung x^5, Ansatz eigen.")

# 2026MerhoehtBStochastikMMS3 2b = 2026MerhoehtBStochastikWTR3-2b
row("2026MerhoehtBStochastikMMS3", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik",
    thema="Konfidenzintervalle",
    typ="Anteil mit genau k von n Konfidenzintervallen verträglich aus dem Diagramm angeben",
    typ_neben="",
    stichwoerter="p = 0,73 liegt in allen Intervallen außer Nummer 13",
    voraussetzungen="verträglich heißt vom Intervall überdeckt|Senkrechte im Diagramm",
    format="Kurzantwort|Begründung",
    operator="Geben Sie an|Begründen Sie",
    antwort="Zahl",
    material="Diagramm",
    skizze="Abb. 2: 20 waagerechte Strecken (Konfidenzintervalle 1 bis 20) über einer p-Achse von 0,64 bis 0,8, Breite je etwa 0,08; Nummer 14 endet bei etwa 0,75, Nummer 13 liegt ganz rechts von 0,73",
    kontext="Fahrgemeinschaften/Konfidenzintervalle",
    textumfang="kurz",
    gegeben="Abbildung 2 mit 20 Konfidenzintervallen",
    gesucht="ein p, das mit genau 19 der 20 Ergebnisse verträglich ist, mit Begründung",
    verfahren="Senkrechte suchen, die genau 19 Intervalle schneidet",
    schritte="1",
    zahlenraum="dezimal",
    einheiten="",
    abhaengig_von="",
    ergebnis="für p = 0,73 ist der Abbildung zu entnehmen, dass alle Konfidenzintervalle bis auf das mit der Nummer 13 diesen Wert von p überdecken (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="p wählen, das alle 20 Intervalle trifft",
    bemerkung="Traegerbindung: Kontext (nur mit Abbildung 2 lösbar). Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich. Teilaufgabe wortgleich mit dem WTR-Zweig (2026-ea-B-wtr, Datei 2026MerhoehtBStochastikWTR3, Teilaufgabe 2b), geteilter Typ, Felder übernommen. MMS-Anteil: keiner.")

# 2026MerhoehtBStochastikMMS3 2c = 2026MerhoehtBStochastikWTR3-2c
row("2026MerhoehtBStochastikMMS3", "c", innen="2", seite="3", punkte="3", afb_amtlich="I|II|III",
    leitidee="Stochastik",
    thema="Konfidenzintervalle",
    typ="Anzahl überdeckender Konfidenzintervalle als binomialverteilt begründen und Wahrscheinlichkeit berechnen",
    typ_neben="",
    stichwoerter="jedes Intervall überdeckt p mit etwa 95 %, unabhängig|Y ~ B(20; 0,95)|P(Y = 19) ≈ 0,38 < 0,42",
    voraussetzungen="Sicherheitswahrscheinlichkeit als Trefferwahrscheinlichkeit|Bernoulli-Kette|Einzelwahrscheinlichkeit am Rechner",
    format="Begründung|Rechnung",
    operator="Geben Sie an|Erläutern Sie|Zeigen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Fahrgemeinschaften/Konfidenzintervalle",
    textumfang="lang",
    gegeben="20 weitere Stichproben (n = 500), Konfidenzintervalle zu 95 %, p konstant; Y Anzahl der Intervalle, die p überdecken; Aussage: P(genau 19) < 42 %",
    gesucht="Verteilung von Y mit Erläuterung und Nachweis der Aussage",
    verfahren="Y binomialverteilt mit n = 20, q = 0,95; P(Y = 19) berechnen",
    schritte="3",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    abhaengig_von="",
    ergebnis="für jedes Konfidenzintervall hat die Wahrscheinlichkeit, p zu überdecken, etwa den Wert der Sicherheitswahrscheinlichkeit; daher kann Y als binomialverteilt mit n = 20 und q = 0,95 angenommen werden; P(Y = 19) ≈ 0,38 < 0,42 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="P(Y ≥ 19) statt P(Y = 19)",
    bemerkung="Standardbezug: K1 III, K2 II, K3 III, K5 I. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Sicherheitswahrscheinlichkeit als Trefferwahrscheinlichkeit einer Bernoulli-Kette deuten, verkettet mit der Binomialrechnung. Aufgabe 1 dieser Datei ist wortgleich mit Stochastik WTR 2, Aufgabe 1 (Dublette, keine Zeile, Soll 8). Teilaufgabe wortgleich mit dem WTR-Zweig (2026-ea-B-wtr, Datei 2026MerhoehtBStochastikWTR3, Teilaufgabe 2c), geteilter Typ, Felder übernommen. MMS-Anteil: Rechner für die Binomialwahrscheinlichkeit, Ansatz eigen.")



# ---- Stochastik MMS 3: Aufgabe 1 (Kraftfahrzeuge, 12 BE) wortgleich mit Stochastik WTR 2 Aufgabe 1 – keine Zeile, Soll 8;
#      Aufgabe 2 (Fahrgemeinschaften, Konfidenzintervalle): 2a eigen, 2b und 2c wortgleich mit WTR 3 (erzeugte Zeilen unten)
KK = "Abb. 2: 20 waagerechte Strecken (Konfidenzintervalle 1 bis 20) über einer p-Achse von 0,64 bis 0,8, Breite je etwa 0,08; Nummer 14 reicht von etwa 0,67 bis 0,75, Nummer 13 liegt ganz rechts von 0,73"
row("2026MerhoehtBStochastikMMS3", "a", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Konfidenzintervalle",
    typ="Grenzen eines Konfidenzintervalls aus dem Stichprobenergebnis über die Näherungsformel berechnen und im Diagramm zuordnen", typ_neben="",
    stichwoerter="h = 356/500 = 0,712|(356/500 − p)² = 1,96² · p(1 − p)/500|p1 ≈ 0,671, p2 ≈ 0,750|Nummer 14",
    voraussetzungen="Stichprobenanteil bilden|Betragsgleichung als quadratische Gleichung in p (Rechner)|Intervall im Diagramm wiedererkennen",
    format="Rechnung|Kurzantwort", operator="Ermitteln Sie|Geben Sie an", antwort="Zahl",
    material="Diagramm", skizze=KK, kontext="Fahrgemeinschaften/Konfidenzintervalle", textumfang="lang",
    gegeben="20 Stichproben vom Umfang 500; Konfidenzintervall zu 95 % aus |h − p| = 1,96 · √(p(1 − p)/n); Abbildung 2 mit den Intervallen 1 bis 20; in einer Stichprobe fahren 356 Personen allein",
    gesucht="Grenzen des zugehörigen Konfidenzintervalls auf Tausendstel genau, rechnerisch; seine Nummer",
    verfahren="h = 0,712 einsetzen, Gleichung nach p lösen (zwei Lösungen), Intervall im Diagramm suchen",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="|356/500 − p| = 1,96 · √(p(1 − p)/500) liefert das Konfidenzintervall [p1; p2] mit p1 ≈ 0,671 und p2 ≈ 0,750; Nummer des Konfidenzintervalls: 14 (amtlich)",
    zwischenergebnis="h = 0,712", niveau_geschaetzt="II",
    fehlerquelle="Näherung h ± 1,96 · √(h(1 − h)/n) statt der Gleichung in p (liefert 0,672 und 0,752)",
    bemerkung="Traegerbindung: Kontext (Zuordnung der Nummer nur aus Abbildung 2). Standardbezug: K2 I, K3 I, K4 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. In der WTR-Fassung (WTR 3, 2a) ist umgekehrt die obere Grenze 0,75 gegeben und die Anzahl 356 gesucht – anderer Lösungsweg, eigener Typ; Aufgabe 1 dieser Datei ist wortgleich mit Stochastik WTR 2 (und WTR 3), Aufgabe 1, und bekommt keine Zeile (Soll 8). MMS-Anteil: Rechner für die Gleichung in p, Ansatz eigen.")

NEUE_TYPEN = [
    ("Nullstellen einer Schar am Term begründen und Tangentensteigungen dort nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus dem faktorisierten Term einer Schar begründen, dass nur die angegebenen Nullstellen existieren, und die Steigungen in diesen Punkten über die Ableitung nachweisen (etwa die x-Achse als Tangente).", "2026MerhoehtBAnalysisMMS1-1a"),
    ("Scharparameter aus einem vorgegebenen Flächeninhalt zwischen Graph und x-Achse berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Das Integral zwischen den parameterabhängigen Nullstellen als Term im Parameter berechnen, gleich dem vorgegebenen Flächeninhalt setzen und den Parameter bestimmen.", "2026MerhoehtBAnalysisMMS1-1b"),
    ("Scharparameter für einen Wendepunkt auf einer Geraden berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Wendestelle einer Schar als Term im Parameter bestimmen und den Parameter so berechnen, dass der Wendepunkt eine gegebene Geradengleichung erfüllt.", "2026MerhoehtBAnalysisMMS1-1c"),
    ("Transformation: Streckfaktoren aus dem Term ablesen und Flächengleichheit der Bilddreiecke über das Produkt der Faktoren beurteilen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Aus w(x) = s · f(k · (c − x)) die Streckfaktoren in x- und y-Richtung angeben und beurteilen, ob ein Dreieck aus Graphenpunkten und sein Bild flächengleich sind (Grundseite mit s_x, Höhe mit s_y gestreckt, Produkt der Faktoren).", "2026MerhoehtBAnalysisMMS1-1d"),
    ("Nullstellen und Werte: Aussage über eine Rate aus dem Nullabschnitt einer abschnittsweise definierten Funktion begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Eine Sachaussage (ab einem Zeitpunkt passiert nichts mehr) damit begründen, dass die abschnittsweise definierte Ratenfunktion dort den Wert null hat; Zeitpunkt in die Modellvariable umrechnen.", "2026MerhoehtBAnalysisMMS1-1e"),
    ("Gleichheit der Flächen unter Eingangs- und Ausgangsrate als gleiche Gesamtzahl im Sachzusammenhang erläutern", "Analysis", "Rekonstruktion von Beständen",
     "Die Flächen unter zwei Ratengraphen als Gesamtzahlen (Zugänge, Abgänge) deuten und daraus erläutern, dass zwei Teilflächen gleich groß sind, weil die Gesamtzahlen übereinstimmen.", "2026MerhoehtBAnalysisMMS1-1g"),
    ("Maximum einer Integralfunktion über die Nullstelle des Integranden begründen und im Sachzusammenhang deuten", "Analysis", "Stammfunktion und Hauptsatz",
     "Für D(x) = ∫(g − h) begründen, dass das Maximum an der Schnittstelle der Graphen von g und h liegt (D' = g − h mit Vorzeichenwechsel von plus nach minus), und das Maximum als größten Bestand deuten.", "2026MerhoehtBAnalysisMMS1-1h"),
    ("Nullstellen und Werte: Ungleichung für einen Funktionswert im Sachzusammenhang deuten", "Analysis", "Funktionsklassen und Eigenschaften",
     "Eine Aussage der Form f(t0) < c für eine Modellfunktion in Worten des Sachzusammenhangs mit Zeitpunkt, Größe und Einheit angeben.", "2026MerhoehtBAnalysisMMS2-1a"),
    ("Gleichung f(t) = f(t − c) für gleiche Werte im Abstand c mit dem Rechner lösen und im Graphen darstellen", "Analysis", "Gleichungen lösen",
     "Die Bedingung, dass eine Größe zu einem Zeitpunkt denselben Wert hat wie c Zeiteinheiten davor, als Gleichung f(t) = f(t − c) ansetzen, numerisch lösen und beide Punkte im Graphen markieren.", "2026MerhoehtBAnalysisMMS2-1b"),
    ("Zeitpunkt der maximalen Rate über die Ableitung der Ratenfunktion berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Für eine als Term gegebene Ratenfunktion den Zeitpunkt der größten Rate über die Nullstelle ihrer Ableitung berechnen.", "2026MerhoehtBAnalysisMMS2-1c"),
    ("Integralfunktion einer Rate und ihren Grenzwert als Bestand und Endwert im Sachzusammenhang deuten", "Analysis", "Rekonstruktion von Beständen",
     "Die Funktion w mit w' = r und w(0) = 0 als Zunahme des Bestands seit dem Start deuten und den Grenzwert von w plus Anfangswert als Endwert des Bestands angeben.", "2026MerhoehtBAnalysisMMS2-1d"),
    ("Nullstellen einer Schar angeben und Vorzeichen des y-Achsenabschnitts begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Nullstellen einer Schar aus einem Faktor angeben und begründen, dass der Schnittpunkt mit der y-Achse für jeden Parameterwert unterhalb (oder oberhalb) der x-Achse liegt.", "2026MerhoehtBAnalysisMMS2-2a"),
    ("Parameter einer Logarithmusfunktion aus einer gemeinsamen Tangente mit einer Scharkurve berechnen und Tangentengleichung angeben", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Den Parameter k in k · ln x so berechnen, dass der Graph mit einem anderen Graphen in einem gemeinsamen Punkt dieselbe Tangente hat (Steigungen gleichsetzen), und die Tangentengleichung angeben.", "2026MerhoehtBAnalysisMMS2-2b"),
    ("Anzahl der gemeinsamen Punkte zweier Graphen aus dem Vergleich ihrer Ableitungsgraphen begründen", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Aus abgebildeten Ableitungsgraphen (eine Ableitung durchgehend größer als die andere) und einem bekannten gemeinsamen Punkt über die Monotonie der Differenz begründen, wie viele gemeinsame Punkte die Graphen haben.", "2026MerhoehtBAnalysisMMS2-2c"),
    ("Scharparameter für Hoch- und Tiefpunkt als Gegenecken eines achsenparallelen Quadrats bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Extremstellen einer Schar als Terme im Parameter bestimmen und den Parameter so berechnen, dass waagerechter und senkrechter Abstand der Extrempunkte gleich sind.", "2026MerhoehtBAnalysisMMS2-2d"),
    ("Fläche: Prozentuale Abweichung einer Dreiecksnäherung vom Flächeninhalt zwischen Scharkurve und Achsen als parameterunabhängig nachweisen", "Analysis", "Flächeninhalt durch Integration",
     "Den Inhalt des Dreiecks aus Ursprung und Achsenschnittpunkten und den Inhalt der vom Graphen und den Achsen eingeschlossenen Fläche als Terme im Parameter berechnen, den Quotienten kürzen und die Abweichung in Prozent angeben.", "2026MerhoehtBAnalysisMMS2-2e"),
    ("Geraden und Ebenen: Höhe eines Quaders aus der Orthogonalität der Raumdiagonalen bestimmen und Oberflächeninhalt berechnen", "Analytische Geometrie", "Orthogonalität",
     "Die unbekannte Höhe eines Quaders aus dem verschwindenden Skalarprodukt zweier Raumdiagonalen bestimmen und den Oberflächeninhalt berechnen.", "2026MerhoehtBAGLAA1MMS-1b"),
    ("Punkt und Ebene: Aussage über das Innere eines Dreiecks unter Koordinatentausch mit einem Gegenbeispiel widerlegen", "Analytische Geometrie", "Lagebeziehungen",
     "Eine Allaussage über Punkte im Innern eines Achsendreiecks widerlegen: einen inneren Punkt über Ebenengleichung und positive Koordinaten wählen und zeigen, dass der Punkt mit vertauschten Koordinaten die Ebenengleichung nicht erfüllt.", "2026MerhoehtBAGLAA2MMS2-1c"),
    ("Scharparameter für einen vorgegebenen Winkel zwischen Ebene und Scharebene berechnen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Über die Kosinusformel für die Normalenvektoren alle Parameterwerte berechnen, für die eine Ebene der Schar mit einer festen Ebene einen vorgegebenen Winkel einschließt (Betragsgleichung, zwei Lösungen).", "2026MerhoehtBAGLAA2MMS2-1e"),
    ("Mögliche Lage des Achsendreiecks einer Ebenenschar über die Vorzeichen der Achsenabschnitte entscheiden und den Parameterbereich bestimmen", "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Die Achsenschnittpunkte einer Ebenenschar als Terme im Parameter angeben, aus ihren Vorzeichen begründen, welche abgebildete Lage des Achsendreiecks unmöglich ist, und für die mögliche Lage den Parameterbereich über Ungleichungen bestimmen.", "2026MerhoehtBAGLAA2MMS2-1f"),
    ("Grenzen eines Konfidenzintervalls aus dem Stichprobenergebnis über die Näherungsformel berechnen und im Diagramm zuordnen", "Stochastik", "Konfidenzintervalle",
     "Aus absoluter Häufigkeit und Umfang den Stichprobenanteil bilden, die Gleichung |h − p| = 1,96 · √(p(1 − p)/n) nach p lösen und das Intervall unter abgebildeten Konfidenzintervallen wiederfinden.", "2026MerhoehtBStochastikMMS3-2a"),
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
    print(f"Vokabular: {len(HEAD)} Felder, {len(LEITIDEEN)} Sachgebiete, "
          f"{sum(len(v) for v in THEMEN.values())} Themen – gelesen aus {KERN} und {PROFIL}; "
          f"{len(QUELLE)} Kennungen aus {QUELLEN}")

    # ---- Selbstprüfung: kein neuer Stapel, nur die vorhandenen Zeilen prüfen
    if not ZEILEN:
        for z in alt:
            a(len(z) == len(HEAD), f"{z.get('id')}: Feldzahl weicht ab")
            pruefe_zeile(z, a)
        typ_namen = {r[0] for r in alt_typ}
        benutzt = set()
        for z in alt:
            for t in typen_von(z):
                benutzt.add(t)
                a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        a(not (typ_namen - benutzt), f"Typen unbenutzt: {sorted(typ_namen - benutzt)}")
        ids = {z["id"] for z in alt}
        a(len(ids) == len(alt), "doppelte id im Katalog")
        for z in alt:
            for dep in [s for s in z["abhaengig_von"].split("|") if s]:
                a(dep in ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
        for r in alt_typ:
            a(r[1] in THEMEN and r[2] in THEMEN.get(r[1], []),
              f"Typ {r[0]}: Sachgebiet oder Thema unbekannt")
            a(r[4] in ids, f"Typ {r[0]}: beispiel_id nicht im Katalog")
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
        if fehler:
            print(f"\nSelbstprüfung: {len(fehler)} Fehler")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        treffer, abw, gew = eichung(alt)
        treffer_eng, _, _ = eichung(alt, eng=True)
        print(f"Selbstprüfung bestanden: {len(alt)} Katalogzeilen, {len(alt_typ)} Typen, "
              f"alle Typen verwendet, {len(stapel)} Stapel vollständig. ZEILEN ist leer, nichts geschrieben.")
        if gew:
            print(f"Eichung über den Bestand: {treffer} von {gew} gewerteten Zeilen treffen den höchsten "
                  f"amtlichen Bereich ({100 * treffer // gew} %), enge Fassung {treffer_eng} "
                  f"({100 * treffer_eng // gew} %); {len(alt) - gew} Zeilen ohne Standardbezug.")
            print("Außerhalb der Geltung: " + ", ".join(
                f"{ziel} {sum(1 for z in alt if ziel not in GELTUNG.get(z['thema'], set()))}"
                for ziel in ZIELE) + f" von {len(alt)} Zeilen")
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
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog")
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
        for dep in [s for s in z["abhaengig_von"].split("|") if s]:
            a(dep in neue_ids or dep in alt_ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
    alle_verwendet = set(verwendet)
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
    if gew >= SCHWELLEN["eichung_ab_zeilen"]:
        a(treffer_eng / gew >= SCHWELLEN["eichung_mindestens"],
          f"Schwelle gerissen: Eichung (enge Fassung) {treffer_eng} von {gew} "
          f"({100 * treffer_eng / gew:.0f} %), verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %: "
          f"{'; '.join(abw_eng)}")
    # Geltung (iqb.md § 6): Zeilen, deren Thema für eine Zielprüfung nicht gilt
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
    # Schnitt Thema × Gegenstandsklasse × Handlung (iqb.md § 6): Werte des Stapels,
    # davon schon in einem Stapel desselben Niveaus vorhanden
    def schnitt(z):
        return (z["thema"], klasse_von(z["typ"]), HANDLUNG.get(z["format"].split("|")[0], "?"))
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
    print(f"Kennzahlen: | {stapel} | {n} | {len(verwendet)} | {len(neu & verwendet)} "
          f"({100 * len(neu & verwendet) / len(verwendet):.0f} %) | {treffer} von {gew} "
          f"({100 * treffer / gew if gew else 0:.0f} %)"
          + (f", eng {treffer_eng} ({100 * treffer_eng / gew:.0f} %)" if treffer_eng != treffer else "")
          + f" | {len(unsicher)} | {len(ersatz)} | {len(wieder)} von {len(verwendet)} "
          f"({100 * len(wieder) / len(verwendet):.0f} %) | {geltung_txt} | "
          f"Schnitt {len(schnitt_neu)} Werte, {schnitt_bekannt} von {n} Zeilen bekannt "
          f"({100 * schnitt_bekannt / n:.0f} %) |")
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
          "(Häufigkeit in Klammern):")
    liste = umschrift_liste(ZEILEN)
    print("  " + ", ".join(f"{w} ({n_}" + ")" for w, n_ in liste) if liste else "  keines")
    for w in warnung:
        print("Hinweis:", w)
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
