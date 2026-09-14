# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.8 · 14.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.8

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

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
    "stapel": "2024-ga-B-wtr",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2024MgrundlegendBAnalysisWTR1": 35,
        "2024MgrundlegendBAnalysisWTR2": 35,
        "2024MgrundlegendBAGLAA1WTR": 20,
        "2024MgrundlegendBAGLAA2WTR1": 20,
        "2024MgrundlegendBAGLAA2WTR2": 20,
        "2024MgrundlegendBStochastikWTR1": 20,
        "2024MgrundlegendBStochastikWTR2": 20,
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
# Stapel 2024-ga-B, WTR-Zweig. innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Pool 2024: Analysis-Dateien mit 35 BE. Stochastik WTR 2, Aufgabe 3 ohne Buchstaben (id …-3, iqb-bau.py v0.8).

SOLL = {"2024MgrundlegendBAnalysisWTR1": 35, "2024MgrundlegendBAnalysisWTR2": 35,
        "2024MgrundlegendBAGLAA1WTR": 20, "2024MgrundlegendBAGLAA2WTR1": 20, "2024MgrundlegendBAGLAA2WTR2": 20,
        "2024MgrundlegendBStochastikWTR1": 20, "2024MgrundlegendBStochastikWTR2": 20}

# ---- Analysis WTR 1, Aufgabe 1: f(x) = 2(x² − 1) e^x, Schar h_k
GF1 = "Koordinatensystem x von −3,5 bis 2,5, y von −2,5 bis 2,5; Graph von f: von links nahe 0 leicht steigend, Nullstelle −1, Tiefpunkt bei etwa (0,4 | −2,2), Nullstelle 1, danach steil steigend; Erwartungshorizont d: Graph von h1 gestrichelt mit halben Werten"
row("2024MgrundlegendBAnalysisWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen", typ_neben="",
    stichwoerter="f'(x) = 2(x² − 1) e^x + 2 · 2x · e^x = 2(x² + 2x − 1) e^x",
    voraussetzungen="Produktregel|Ausklammern von e^x",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 2 · (x² − 1) · e^x in IR; Behauptung f'(x) = 2 · (x² + 2x − 1) · e^x",
    gesucht="Nachweis der Ableitung",
    verfahren="Produktregel, zusammenfassen",
    schritte="2", zahlenraum="ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = 2 · (x² − 1) · e^x + 2 · 2x · e^x = 2 · (x² + 2x − 1) · e^x (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Faktor 2 beim zweiten Summanden vergessen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2024MgrundlegendBAnalysisWTR1", "b", innen="1", seite="1", punkte="6", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Nullstellen einer e-Funktion nachweisen und Tiefstelle berechnen", typ_neben="",
    stichwoerter="e^x > 0 ⇒ f(x) = 0 ⇔ x² − 1 = 0 ⇔ x = ±1|f'(x) = 0 für x > 0 ⇔ x² + 2x − 1 = 0 ⇔ x = −1 + √2",
    voraussetzungen="Nullprodukt mit e^x ≠ 0|quadratische Gleichung|Tiefstelle aus der Abbildung im positiven Bereich",
    format="Rechnung", operator="Weisen Sie nach|Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="kurz",
    gegeben="f und f' wie in a; Kontrolle x_T = −1 + √2",
    gesucht="Nachweis genau zweier Nullstellen −1 und 1; x-Koordinate des Tiefpunkts",
    verfahren="f = 0 lösen, f' = 0 lösen, Vorzeichen aus der Abbildung",
    schritte="3", zahlenraum="Wurzel|negativ|Potenz", einheiten="", abhaengig_von="2024MgrundlegendBAnalysisWTR1-1a",
    ergebnis="wegen e^x > 0 für alle x gilt f(x) = 0 ⇔ x² − 1 = 0 ⇔ x = −1 ∨ x = 1; für x > 0 gilt f'(x) = 0 ⇔ x² + 2x − 1 = 0 ⇔ x = −1 + √2 (amtlich)",
    zwischenergebnis="x_T ≈ 0,414; zweite Nullstelle von f' bei −1 − √2 ist die Hochstelle", niveau_geschaetzt="I",
    fehlerquelle="beide Lösungen von f' = 0 als Tiefstellen nennen",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAnalysisWTR1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Eindeutige Lösung einer Flächengleichung über die Monotonie des Flächeninhalts begründen", typ_neben="",
    stichwoerter="f < 0 auf ]−1; 1[, f > 0 für x > 1|∫_{−1}^1 f < 0, ∫_1^b f > 0 und wachsend|f streng monoton zunehmend für x > 1 ⇒ es gibt b mit Ausgleich",
    voraussetzungen="Vorzeichen des Integrals aus dem Graphen|wachsende Fläche rechts von 1|Existenz eines Ausgleichs",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="kurz",
    gegeben="Gleichung ∫_{−1}^1 f(x) dx + ∫_1^b f(x) dx = 0; Abbildung 1",
    gesucht="Begründung, dass es ein b > 1 gibt",
    verfahren="negatives festes Integral gegen positives wachsendes Integral",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Funktionswerte von f sind für −1 < x < 1 negativ und für x > 1 positiv; damit ist ∫_{−1}^1 f(x) dx < 0 und ∫_1^b f(x) dx > 0; für x > 1 ist f streng monoton zunehmend, also gibt es eine Zahl b mit ∫_1^b f(x) dx = −∫_{−1}^1 f(x) dx (amtlich)",
    zwischenergebnis="∫_{−1}^1 f ≈ −2,94, b ≈ 1,56", niveau_geschaetzt="II",
    fehlerquelle="Existenz über konkrete Rechnung statt über den Graphen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-B, dort mit Eindeutigkeit).")

row("2024MgrundlegendBAnalysisWTR1", "d", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Graph eines in y-Richtung gestreckten Scharmitglieds begründen und skizzieren", typ_neben="",
    stichwoerter="h1 = 1/2 h2: Streckung in y-Richtung mit Faktor 1/2|Tiefpunkt bleibt bei derselben Stelle im vierten Quadranten|Graph mit halben Werten skizzieren",
    voraussetzungen="Vorfaktor als Streckung|Extremstellen bleiben erhalten|Skizze",
    format="Begründung|Zeichnen", operator="Begründen Sie|Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=GF1, kontext="ohne", textumfang="mittel",
    gegeben="h_k(x) = k · (x² − 1) · e^x, k > 0; h_2 = f",
    gesucht="Begründung ohne Rechnung, dass der Graph von h1 einen Tiefpunkt im selben Quadranten wie der von h2 hat; Skizze von h1 in Abbildung 1",
    verfahren="h1 als halbierte h2 erkennen, Graph stauchen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="der Graph von h1 geht aus dem Graphen von h2 durch Streckung mit dem Faktor 1/2 in y-Richtung hervor; Skizze mit halbierten Funktionswerten (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Streckung als Verschiebung zeichnen",
    bemerkung="Standardbezug: K1 II, K2 I, K4 II, K6 I. AB amtlich: II. Amtlich.")

row("2024MgrundlegendBAnalysisWTR1", "e", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter für einen vorgegebenen Flächeninhalt zwischen Graph und x-Achse bestimmen", typ_neben="",
    stichwoerter="Nullstellen ±1|∫_{−1}^1 h_k = k [(x² − 2x + 1) e^x]_{−1}^1 = −4k/e|Inhalt 4k/e = 1 ⇒ k = e/4",
    voraussetzungen="Nullstellen als Grenzen|gegebene Stammfunktion|Betrag des Integrals als Fläche",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="H_k(x) = k · (x² − 2x + 1) · e^x Stammfunktion von h_k; Flächenstück zwischen Graph von h_k und x-Achse",
    gesucht="k mit Flächeninhalt 1",
    verfahren="Integral über [−1; 1] in k, Betrag gleich 1",
    schritte="3", zahlenraum="Potenz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="die Nullstellen von h_k sind −1 und 1; ∫_{−1}^1 h_k(x) dx = k · [(x² − 2x + 1) · e^x]_{−1}^1 = −4k/e; da das Flächenstück den Inhalt 1 hat, gilt 4k/e = 1 und somit k = e/4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen des Integrals als Fläche nehmen (k negativ)",
    bemerkung="Standardbezug: K2 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAnalysisWTR1", "f", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktionen mit der x-Achse als Tangente über die Nullstellen der Funktion ermitteln", typ_neben="",
    stichwoerter="Stammfunktionen H2 + c|x-Achse als Tangente: Extrempunkt auf der x-Achse, Extremstellen von H2 sind die Nullstellen ±1 von h2|H2(−1) + c = 0 ⇒ c = −8/e; H2(1) + c = 0 ⇒ c = 0",
    voraussetzungen="Berührung der x-Achse als Extrempunkt mit Wert 0|Extremstellen von H aus Nullstellen von h|Konstante bestimmen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="h2 = f; H2(x) = 2 · (x² − 2x + 1) · e^x; zwei Stammfunktionen mit der x-Achse als Tangente",
    gesucht="je ein Term dieser Stammfunktionen",
    verfahren="Bedingung an c aus H2(±1) + c = 0",
    schritte="3", zahlenraum="Potenz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="die Terme aller Stammfunktionen von h2 lassen sich durch H2(x) + c darstellen; H2(−1) + c = 0 ⇔ c = −8/e, H2(1) + c = 0 ⇔ c = 0 (amtlich)",
    zwischenergebnis="H2(−1) = 8/e, H2(1) = 0", niveau_geschaetzt="III",
    fehlerquelle="Tangentenbedingung an H2' = 0 statt an die Nullstellen von h2 knüpfen (gleich, aber oft übersehen, dass beide Stellen zählen)",
    bemerkung="Standardbezug: K2 III, K4 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (e) Beziehung Stammfunktion – Funktion (Extremstellen von H an den Nullstellen von h) am Graphen gedeutet, verkettet mit der Bedingung H = 0.")

# ---- Analysis WTR 1, Aufgabe 2: Phosphor und Algen
PHOS = "Abb. 2: Koordinatensystem t von 0 bis 40 (Jahre), y von 0 bis 80; Graph von p steigt von 40 auf ein Maximum etwa 85 bei t ≈ 8 und fällt dann gegen etwa 12 bei 40, Wendepunkt bei etwa t = 15; Abb. 3: Graph der Ableitung von a, fällt von 14 bei t = 0 linear auf 0 bei t = 10 und bleibt leicht negativ bis 40"
row("2024MgrundlegendBAnalysisWTR1", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen", typ_neben="",
    stichwoerter="p(t) = 30 bei t ≈ 25",
    voraussetzungen="Ablesen einer Stelle zu einem Wert",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=PHOS, kontext="Gewässer/Phosphor und Algen", textumfang="lang",
    gegeben="p(t) Phosphorkonzentration in mg/m³, t Jahre seit Beobachtungsbeginn, 0 ≤ t ≤ 40; Graph in Abbildung 2",
    gesucht="Zeitpunkt mit Phosphorkonzentration 30 mg/m³",
    verfahren="Waagerechte bei 30 mit dem Graphen schneiden",
    schritte="1", zahlenraum="ganz", einheiten="Jahre|mg/m³", abhaengig_von="",
    ergebnis="etwa 25 Jahre nach Beobachtungsbeginn beträgt die Phosphorkonzentration 30 mg/m³ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Achsen vertauschen (p(30) ablesen)",
    bemerkung="Standardbezug: K3 I, K4 I. AB amtlich: I. Amtlich (Ablesung).")

row("2024MgrundlegendBAnalysisWTR1", "b", innen="2", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendepunkt als Zeitpunkt stärkster Abnahme im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Wendepunkt im fallenden Bereich: Stelle der stärksten Abnahme der Phosphorkonzentration",
    voraussetzungen="Wendepunkt als Extremum der Änderungsrate",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="Koordinatensystem", skizze=PHOS, kontext="Gewässer/Phosphor und Algen", textumfang="kurz",
    gegeben="Graph von p hat für t ≥ 10 einen Wendepunkt",
    gesucht="Bedeutung des Wendepunkts für die Phosphorkonzentration",
    verfahren="Wendepunkt als stärkste Abnahme deuten",
    schritte="1", zahlenraum="ganz", einheiten="Jahre", abhaengig_von="",
    ergebnis="die t-Koordinate des Wendepunkts gibt den Zeitpunkt an, zu dem die Phosphorkonzentration des Gewässers innerhalb des Beobachtungszeitraums am stärksten abnimmt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Wendepunkt als Beginn der Abnahme deuten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich.")

row("2024MgrundlegendBAnalysisWTR1", "c", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Aussage über zwei Größen anhand von Funktionsgraph und Ableitungsgraph beurteilen", typ_neben="",
    stichwoerter="p nimmt ab etwa t = 8 ab|a'(8) > 0 laut Abbildung 3: Algenkonzentration nimmt dort noch zu|Aussage falsch",
    voraussetzungen="Abnahme von p am Graphen|Vorzeichen von a' als Zu- oder Abnahme von a",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=PHOS, kontext="Gewässer/Phosphor und Algen", textumfang="mittel",
    gegeben="Abbildung 2 (p) und Abbildung 3 (a'); Aussage: ab dem Zeitpunkt, ab dem sich die Phosphorkonzentration verringert, verringert sich auch die Algenkonzentration",
    gesucht="Beurteilung",
    verfahren="Maximum von p mit dem Vorzeichen von a' vergleichen",
    schritte="2", zahlenraum="ganz", einheiten="Jahre", abhaengig_von="",
    ergebnis="die Aussage ist falsch; zu dem Zeitpunkt, ab dem die Phosphorkonzentration abnimmt, ist die momentane Änderungsrate der Algenkonzentration positiv (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Abbildung 3 als Graph von a lesen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II. AB amtlich: II. Amtlich.")

row("2024MgrundlegendBAnalysisWTR1", "d", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Anfangsbestand aus Endbestand und Fläche unter dem Ableitungsgraphen ermitteln", typ_neben="",
    stichwoerter="a(10) − a(0) = ∫_0^10 a'(t) dt|Fläche unter a' von 0 bis 10 ≈ Dreieck mit Katheten 10 und 14: 70|a(0) ≈ 100 − 70 = 30 mg/m³",
    voraussetzungen="Integral der Änderungsrate als Bestandsänderung|Fläche am Graphen als Dreieck schätzen|Eintragung in Abbildung 3",
    format="Rechnung|Zeichnen", operator="Bestimmen Sie|Veranschaulichen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=PHOS, kontext="Gewässer/Phosphor und Algen", textumfang="kurz",
    gegeben="a(10) = 100 mg/m³; Graph von a' in Abbildung 3",
    gesucht="a(0) mit Veranschaulichung in Abbildung 3",
    verfahren="Dreiecksfläche unter a' schätzen, von a(10) abziehen",
    schritte="3", zahlenraum="ganz", einheiten="mg/m³|Jahre", abhaengig_von="",
    ergebnis="der Inhalt der Fläche, die der Graph von a' mit der t-Achse im Bereich 0 ≤ t ≤ 10 einschließt, entspricht in etwa dem Inhalt eines rechtwinkligen Dreiecks mit Katheten 10 und 14; wegen 100 − 1/2 · 14 · 10 = 30 beträgt die Algenkonzentration zu Beobachtungsbeginn etwa 30 mg/m³ (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Fläche addieren statt subtrahieren",
    bemerkung="Standardbezug: K2 III, K3 III, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (e) Integral des Ableitungsgraphen als Bestandsänderung gedeutet, verkettet mit der Flächenschätzung als Dreieck.")

# ---- Analysis WTR 2, Aufgabe 1: f(x) = 3/1000 x⁴ − 8/100 x³ + 6/10 x²
GF2 = "Koordinatensystem x von −5 bis 15, y von −2 bis 13; Graph von f: von links oben fallend zum Tiefpunkt im Ursprung, steigend mit Sattelpunkt (10 | 10), danach steigend; Punkt P(0 | −5/8) markiert; Erwartungshorizont c: zwei Tangenten durch P mit positiver und negativer Steigung"
row("2024MgrundlegendBAnalysisWTR2", "a", innen="1", seite="1", punkte="6", afb_amtlich="I|II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Tiefpunkt angeben und Fehlen weiterer Extrempunkte über die Ableitung nachweisen", typ_neben="",
    stichwoerter="T(0 | 0) aus der Abbildung|f'(x) = 12/1000 x³ − 24/100 x² + 12/10 x = 12/1000 x (x − 10)²|Nullstellen 0 und 10|bei 10 kein Vorzeichenwechsel von f'",
    voraussetzungen="Tiefpunkt ablesen|Ableitung faktorisieren|doppelte Nullstelle ohne Vorzeichenwechsel",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Zeigen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GF2, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3/1000 x⁴ − 8/100 x³ + 6/10 x² in IR; Graph in Abbildung 1",
    gesucht="Koordinaten des Tiefpunkts; Nachweis, dass es keine weiteren Extrempunkte gibt",
    verfahren="f' = 0 lösen, Vorzeichenwechsel prüfen",
    schritte="4", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="",
    ergebnis="T(0 | 0); f'(x) = 12/1000 x³ − 24/100 x² + 12/10 x; f'(x) = 0 ⇔ x · (x² − 20x + 100) = 0 ⇔ x · (x − 10)² = 0 ⇔ x = 0 ∨ x = 10; nur bei 0 und 10 können Extrempunkte vorliegen; an der Stelle 10 ändert sich das Vorzeichen von f'(x) nicht (amtlich)",
    zwischenergebnis="f(10) = 10, Sattelpunkt", niveau_geschaetzt="II",
    fehlerquelle="x = 10 als Extremstelle nennen",
    bemerkung="Standardbezug: K1 II, K4 I, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAnalysisWTR2", "b", innen="1", seite="2", punkte="4", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen", typ_neben="",
    stichwoerter="f'(5) = 3/2|f(5) = 55/8|55/8 = 3/2 · 5 + n ⇒ n = −5/8|t: y = 3/2 x − 5/8",
    voraussetzungen="Ableitungswert|Punkt-Steigungs-Form",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Tangente t im Punkt (5 | f(5))",
    gesucht="Gleichung von t",
    verfahren="Steigung f'(5), Achsenabschnitt aus dem Punkt",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="f'(5) = 3/2; 55/8 = 3/2 · 5 + n ⇔ n = −5/8; y = 3/2 x − 5/8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="f(5) mit Bruchrechnung falsch (55/8 = 6,875)",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A). Die Tangente geht durch P(0 | −5/8).")

row("2024MgrundlegendBAnalysisWTR2", "c", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangenten durch einen Punkt der y-Achse an den Graphen skizzieren", typ_neben="",
    stichwoerter="Lineal in P anlegen und an den Graphen drehen: eine Tangente mit positiver Steigung rechts (Berührpunkt bei etwa x = 14), eine mit negativer Steigung links (Berührpunkt bei etwa x = −3)",
    voraussetzungen="Tangente als berührende Gerade|verschiedene Berührpunkte",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=GF2, kontext="ohne", textumfang="kurz",
    gegeben="P(0 | −5/8); t aus b geht durch P",
    gesucht="zwei weitere Tangenten durch P mit Steigungen verschiedenen Vorzeichens in Abbildung 1",
    verfahren="Geraden durch P an den Graphen anlegen",
    schritte="1", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="2024MgrundlegendBAnalysisWTR2-1b",
    ergebnis="zwei Geraden durch P eingezeichnet, die den Graphen rechts (positive Steigung) bzw. links (negative Steigung) berühren (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Sekanten statt Tangenten zeichnen",
    bemerkung="Standardbezug: K4 I. AB amtlich: I. Amtlich.")

row("2024MgrundlegendBAnalysisWTR2", "d", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Streckfaktoren aus der Zuordnung zweier Punkte deuten und berechnen", typ_neben="",
    stichwoerter="g(x) = a · f(b · x): Streckung in y-Richtung mit Faktor a, in x-Richtung mit Faktor 1/b|g(12) = a · f(10) ⇔ 12 = 10a ⇔ a = 6/5|1/b · 10 = 12 ⇔ b = 5/6",
    voraussetzungen="Bedeutung der Faktoren a und b|Punktzuordnung in zwei Gleichungen übersetzen",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=GF2, kontext="ohne", textumfang="mittel",
    gegeben="g(x) = a · f(b · x) mit a, b > 0; (10 | 10) auf dem Graphen von f wird zu (12 | 12) auf dem Graphen von g",
    gesucht="Bedeutung von a und b und ihre Werte",
    verfahren="Streckungen deuten, x- und y-Koordinate getrennt zuordnen",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="der Graph von g wird durch Streckung in y-Richtung mit dem Faktor a und durch Streckung in x-Richtung mit dem Faktor 1/b aus dem Graphen von f erzeugt; g(12) = a · f(10) ⇔ 12 = a · 10 ⇔ a = 6/5; 1/b · 10 = 12 ⇔ b = 5/6 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="b = 6/5 (Streckfaktor mit b statt 1/b)",
    bemerkung="Standardbezug: K2 III, K4 III, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) zwei Deutungen (a als y-Streckung, 1/b als x-Streckung) verkettet mit der Punktzuordnung.")

# ---- Analysis WTR 2, Aufgabe 2: Radfahrer
RAD = "Koordinatensystem x von 0 bis 16 (Sekunden), y von 0 bis 12 (m/s); Graph von Radfahrer A (f bis x = 10, dann waagerecht bei 10) und Radfahrer B (h bis x = 12, dann waagerecht bei 12); A liegt bis etwa x = 6 knapp über B, danach darunter"
row("2024MgrundlegendBAnalysisWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="f(3) = 3,483 ≈ 3,5 m/s",
    voraussetzungen="Einsetzen|Einheit",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=RAD, kontext="Radfahrer/Geschwindigkeit", textumfang="lang",
    gegeben="f aus Aufgabe 1 beschreibt die Geschwindigkeit von Radfahrer A in m/s in den ersten 10 Sekunden, x Sekunden seit dem Start",
    gesucht="Geschwindigkeit von A drei Sekunden nach dem Start",
    verfahren="f(3) berechnen",
    schritte="1", zahlenraum="dezimal", einheiten="m/s|Sekunden", abhaengig_von="",
    ergebnis="f(3) = 3,483, d. h. drei Sekunden nach dem Start beträgt die Geschwindigkeit von Radfahrer A etwa 3,5 m/s (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Wert am Graphen von B ablesen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2024MgrundlegendBAnalysisWTR2", "b", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Schnittstellen zweier Graphen im Sachzusammenhang ablesen", typ_neben="",
    stichwoerter="Schnittpunkt der Graphen bei x_s ≈ 6|A schneller als B vom Start bis x_s",
    voraussetzungen="Ablesen des Schnittpunkts|Vergleich der Graphenlage",
    format="Rechnung|Kurzantwort", operator="Ermitteln Sie|Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=RAD, kontext="Radfahrer/Geschwindigkeit", textumfang="mittel",
    gegeben="genau ein Zeitpunkt x_s mit gleicher Geschwindigkeit; Abbildung 2",
    gesucht="x_s und der Zeitraum, in dem A schneller ist als B",
    verfahren="Schnittstelle ablesen, Lage der Graphen vergleichen",
    schritte="2", zahlenraum="ganz", einheiten="Sekunden", abhaengig_von="",
    ergebnis="x_s ≈ 6; Zeitraum: vom Zeitpunkt des Starts bis zum Zeitpunkt x_s Sekunden nach dem Start (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeitraum nach x_s angeben",
    bemerkung="Standardbezug: K2 I, K3 I, K4 I, K6 I. AB amtlich: I. Amtlich (Ablesung). Typ wiederverwendet (2025-ea-B).")

row("2024MgrundlegendBAnalysisWTR2", "c", innen="2", seite="3", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Differenzfunktion und ihr Maximum aus einem Lösungsweg im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="d(x) = f(x) − h(x): Geschwindigkeitsvorsprung von A in m/s|d' = 0 nur bei x1 ≈ 3,64, d'' < 0: Maximum|d(x1) ≈ 0,37: größter Geschwindigkeitsunterschied in den ersten x_s Sekunden",
    voraussetzungen="Differenz als Vorsprung|notwendige und hinreichende Bedingung als Maximum lesen",
    format="Kurzantwort", operator="Geben Sie an|Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Radfahrer/Geschwindigkeit", textumfang="mittel",
    gegeben="Lösungsweg: d(x) = f(x) − h(x); d'(x) = 0 hat für 0 < x < x_s nur die Lösung x1 ≈ 3,64; d''(x1) ≈ −0,13 < 0; d(x1) ≈ 0,37",
    gesucht="Bedeutung von d(x) für 0 < x < x_s und Deutung von 0,37",
    verfahren="d als Vorsprung, Extremwertschritte als Maximum deuten",
    schritte="2", zahlenraum="dezimal", einheiten="m/s|Sekunden", abhaengig_von="2024MgrundlegendBAnalysisWTR2-2b",
    ergebnis="d(x) gibt für den Zeitpunkt x Sekunden nach dem Start an, um wie viele Meter pro Sekunde Radfahrer A schneller ist als Radfahrer B; der größte Unterschied der Geschwindigkeiten innerhalb der ersten x_s Sekunden beträgt etwa 0,37 m/s (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="0,37 als Vorsprung in Metern deuten",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K6 II. AB amtlich: II. Amtlich.")

row("2024MgrundlegendBAnalysisWTR2", "d", innen="2", seite="3", punkte="6", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Zurückgelegte Strecke aus dem Integral der Geschwindigkeit und einer Phase konstanter Geschwindigkeit berechnen", typ_neben="",
    stichwoerter="∫_0^10 f = [3/5000 x⁵ − 1/50 x⁴ + 1/5 x³]_0^10 = 60 − 200 + 200 = 60|danach 5 s mit 10 m/s: 50|110 m",
    voraussetzungen="Integral der Geschwindigkeit als Weg|Stammfunktion des Polynoms|konstante Phase als Rechteck",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=RAD, kontext="Radfahrer/Geschwindigkeit", textumfang="kurz",
    gegeben="A beschleunigt 10 s nach f, dann konstant mit f(10) = 10 m/s",
    gesucht="Strecke von A in den ersten 15 Sekunden",
    verfahren="Integral von 0 bis 10 plus 10 · 5",
    schritte="3", zahlenraum="Bruch|ganz", einheiten="m|Sekunden", abhaengig_von="",
    ergebnis="∫_0^10 f(x) dx = [3/5000 x⁵ − 1/50 x⁴ + 1/5 x³]_0^10 = 60 − 200 + 200 = 60; 60 + 10 · 5 = 110; die Länge der zurückgelegten Strecke beträgt 110 m (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Integral bis 15 mit f rechnen (f gilt nur bis 10)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAnalysisWTR2", "e", innen="2", seite="3", punkte="3", afb_amtlich="II|III",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Nullstelle eines Differenzintegrals als Zeitpunkt gleicher Strecke deuten und ihre Lage begründen", typ_neben="",
    stichwoerter="∫_0^z (f − h) = 0: Streckenvorsprung von A ist null, beide haben gleich weit|z > x_s: bis x_s ist A stets schneller, also vorn; erst danach kann B aufholen",
    voraussetzungen="Integral der Geschwindigkeitsdifferenz als Streckendifferenz|Vorzeichen von f − h bis x_s",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=RAD, kontext="Radfahrer/Geschwindigkeit", textumfang="kurz",
    gegeben="z mit 0 < z < 10 und ∫_0^z (f(x) − h(x)) dx = 0; x_s aus b",
    gesucht="Bedeutung von z und Begründung, dass z > x_s",
    verfahren="Integral als Streckendifferenz deuten, Lage aus dem Vorzeichen von f − h",
    schritte="2", zahlenraum="ganz", einheiten="Sekunden|m", abhaengig_von="2024MgrundlegendBAnalysisWTR2-2b",
    ergebnis="zum Zeitpunkt, der im Modell durch z angegeben ist, haben beide Radfahrer die gleiche Strecke zurückgelegt; es gilt z > x_s, da sich Radfahrer A in den ersten x_s Sekunden nach dem Start stets vor Radfahrer B befindet (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="z als Zeitpunkt gleicher Geschwindigkeit deuten (das ist x_s)",
    bemerkung="Standardbezug: K1 III, K2 II, K3 III, K4 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (e) Differenzintegral als Streckenbilanz gedeutet, verkettet mit dem Vorzeichenargument für z > x_s.")

# ---- AG/LA (A1) WTR: E-Scooter
row("2024MgrundlegendBAGLAA1WTR", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="drei Knoten A, B, C|Pfeile mit den Spaltenwerten von M: A→A 0,7, A→B 0,2, A→C 0,1, B→A 0,1, B→B 0,8, B→C 0,1, C→A 0,2, C→B 0,2, C→C 0,6",
    voraussetzungen="Spalte = Herkunft|Schleifen für Verbleib",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="E-Scooter/Verteilung", textumfang="lang",
    gegeben="v_{n+1} = M · v_n mit M = ((0,7; 0,1; 0,2), (0,2; 0,8; 0,2), (0,1; 0,1; 0,6)); 900 E-Scooter in Bereichen A, B, C",
    gesucht="Übergangsdiagramm",
    verfahren="Matrixspalten als ausgehende Pfeile",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Übergangsdiagramm mit neun Pfeilen (drei Schleifen 0,7, 0,8, 0,6) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen statt Spalten als Herkunft",
    bemerkung="Standardbezug: K3 I, K4 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A, Definition seit Lauf 5 auch aus der Matrix). Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MgrundlegendBAGLAA1WTR", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Matrix-Vektor-Produkt berechnen", typ_neben="",
    stichwoerter="b = 0,2 · 300 + 0,8 · 200 + 0,2 · 400 = 300|300 E-Scooter am Ende des nächsten Tages in B",
    voraussetzungen="eine Zeile mal Vektor|Deutung",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="E-Scooter/Verteilung", textumfang="kurz",
    gegeben="M · (300; 200; 400) = (a; b; c)",
    gesucht="b und seine Bedeutung",
    verfahren="zweite Zeile von M mit dem Vektor multiplizieren",
    schritte="1", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="b = 0,2 · 300 + 0,8 · 200 + 0,2 · 400 = 300; am Ende des nächsten Tages befinden sich 300 E-Scooter im Bereich B (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Spalte statt Zeile nehmen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A). Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MgrundlegendBAGLAA1WTR", "c", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Spanne einer Komponente nach einem Schritt bei teilweise bekannter Verteilung ermitteln", typ_neben="",
    stichwoerter="Verteilung (300; b; 600 − b), 0 ≤ b ≤ 600|a' = 0,7 · 300 + 0,1b + 0,2(600 − b) = 330 − 0,1b|mindestens 270, höchstens 330",
    voraussetzungen="Verteilung mit einer Unbekannten|erste Zeile von M|linearer Term auf einem Intervall",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="E-Scooter/Verteilung", textumfang="mittel",
    gegeben="am Ende eines Tages ein Drittel der 900 E-Scooter in A",
    gesucht="Mindest- und Höchstzahl in A am Ende des nächsten Tages",
    verfahren="Verteilung parametrisieren, a' als Term in b, Randwerte",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="Verteilung (300; b; 600 − b) mit 0 ≤ b ≤ 600; a = 0,7 · 300 + 0,1 · b + 0,2 · (600 − b) = 330 − 0,1 · b; mit 0 ≤ b ≤ 600 folgt, dass mindestens 270 und höchstens 330 E-Scooter im Bereich A zu erwarten sind (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="b und c unabhängig variieren (Summe 900 vergessen)",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MgrundlegendBAGLAA1WTR", "d", innen="1", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Term mit Matrixpotenz und Zugang im Sachzusammenhang auswählen und deuten", typ_neben="",
    stichwoerter="Dienstag Entnahme von 20 % aus C: diag(1; 1; 0,8) · d|zwei Tage (Mi, Do) M · M, dann Rückgabe diag(0; 0; 0,2) · d am Donnerstag, dann ein Tag M: Vektor g|f: 80 % aus C und alle aus A, B entnommen, Rückgabe nach einem Tag|h: 20 % aus allen Bereichen entnommen, 20 Scooter nach C",
    voraussetzungen="Diagonalmatrix als Entnahme|Reihenfolge der Tage als Matrixpotenzen|Zugang als Summand|Szenarien in Worte fassen",
    format="Begründung|Kurzantwort", operator="Entscheiden Sie|Erläutern Sie", antwort="Text",
    material="keins", skizze="keine", kontext="E-Scooter/Verteilung", textumfang="lang",
    gegeben="Dienstagabend: 20 % der E-Scooter aus C entnommen, nach 48 Stunden nach C zurückgebracht; d Verteilung vor der Entnahme; Vektoren f = M·M·(M·diag(0; 0; 0,2)·d + diag(1; 1; 0,8)·d), g = M·(M·M·diag(1; 1; 0,8)·d + diag(0; 0; 0,2)·d), h = M·(M·M·(d − 0,2d) + (0; 0; 20))",
    gesucht="welcher Vektor den Freitagabend beschreibt; Szenarien für die beiden anderen",
    verfahren="Reihenfolge Entnahme – zwei Tage – Rückgabe – ein Tag mit den Termen vergleichen",
    schritte="4", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="Vektor g ist die passende Beschreibung; Szenario zu f: im Bereich C werden am Ende des Dienstags 80 % der E-Scooter und in den Bereichen A und B alle E-Scooter entnommen, am Ende des Mittwochs werden die entnommenen zurückgebracht; Szenario zu h: in jedem Bereich werden am Ende des Dienstags 20 % entnommen, nach 48 Stunden werden 20 E-Scooter in den Bereich C gebracht (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Anzahl der Tage zwischen Entnahme und Rückgabe falsch zählen",
    bemerkung="Traegerbindung: Kontext (Wochentagsfolge und Wartungsregel nur aus der Trägeraufgabe). Standardbezug: K3 III, K4 III, K5 II, K6 II. AB amtlich: III. Amtlich. Eichregel: (d) Diagonalmatrizen als Entnahme und Zugang deuten, verkettet mit der Tagesfolge. Typ wiederverwendet (2026-ga-B). Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MgrundlegendBAGLAA1WTR", "e", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Unterschiedliche Beträge von Vektoren mit fester Komponentensumme über ein Beispiel begründen", typ_neben="",
    stichwoerter="|(900; 0; 0)| = 900, |(300; 300; 300)| = √270000 ≈ 520|möglich",
    voraussetzungen="Betrag eines Vektors|Beispiel als Begründung",
    format="Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="E-Scooter/Verteilung", textumfang="mittel",
    gegeben="Verteilungsvektoren der 900 E-Scooter als geometrische Vektoren",
    gesucht="ob zwei solche Vektoren unterschiedliche Beträge haben können",
    verfahren="zwei Beispiele mit verschiedenen Beträgen",
    schritte="1", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="dies ist möglich, wie folgendes Beispiel zeigt: |(900; 0; 0)| = 900 und |(300; 300; 300)| = √270000 ≈ 520 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="gleiche Komponentensumme mit gleichem Betrag verwechseln",
    bemerkung="Standardbezug: K1 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

row("2024MgrundlegendBAGLAA1WTR", "f", innen="1", seite="2", punkte="4", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Aussagen über Winkel zwischen Vektoren mit fester Komponentensumme beurteilen", typ_neben="",
    stichwoerter="0°: zwei verschiedene Vektoren mit Summe 900 können keine Vielfachen voneinander sein – falsch|90°: (400; 500; 0) · (0; 0; 900) = 0 – richtig",
    voraussetzungen="Winkel 0° als Kollinearität|Winkel 90° als Skalarprodukt null|Komponentensumme als Nebenbedingung",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="E-Scooter/Verteilung", textumfang="mittel",
    gegeben="Verteilungsvektoren mit Komponentensumme 900; Aussagen: es gibt zwei unterschiedliche mit Winkel 0°; es gibt zwei mit Winkel 90°",
    gesucht="Beurteilung beider Aussagen",
    verfahren="Kollinearität gegen die Summe, Beispiel für Orthogonalität",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die erste Aussage ist falsch: da die Summe der Komponenten jedes Vektors 900 beträgt, können zwei unterschiedliche dieser Vektoren keine Vielfachen voneinander sein; die zweite ist richtig: beispielsweise ist das Skalarprodukt von (400; 500; 0) und (0; 0; 900) null (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="für 0° gleiche Vektoren zulassen",
    bemerkung="Standardbezug: K1 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA (A2) WTR 1: Eingangsüberdachung
DACH = "Schrägbild: Hausdach (schräge Fläche) mit vertikaler Hauswand (2,5 m hoch) und angesetzter Eingangsüberdachung aus dem Dreieck DEF (grau) und den Vierecken ADFC und BEFC; Befestigungspunkte A, B, C am Hausdach; Übergang Dach – Wand in der x-Achse"
row("2024MgrundlegendBAGLAA2WTR1", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines gleichschenkligen Dreiecks über die Höhe zur Basis berechnen", typ_neben="",
    stichwoerter="M Mittelpunkt von DE: (1,5 | 2 | 0)|DE = (−3; 0; 0), MF = (0; −1,2; 1)|Dreieck 1/2 · 3 · √2,44 = 3√61/10 ≈ 2,34|gesamt 2 · 3,6 + 2,34 ≈ 9,5 m²",
    voraussetzungen="Gleichschenkligkeit (|DF| = |EF|)|Höhe als MF|Summe der drei Dachflächen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=DACH, kontext="Eingangsüberdachung", textumfang="lang",
    gegeben="D(3 | 2 | 0), E(0 | 2 | 0), F(1,5 | 0,8 | 1) mit |DF| = |EF|; zwei viereckige Dachflächen je etwa 3,6 m²; 1 LE = 1 m",
    gesucht="Inhalt der zu bedeckenden Fläche (Dreieck plus zwei Vierecke)",
    verfahren="Dreiecksfläche über Basis DE und Höhe MF, addieren",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="m²", abhaengig_von="",
    ergebnis="Mittelpunkt M von DE: M(1,5 | 2 | 0); mit DE = (−3; 0; 0) und MF = (0; −1,2; 1) ergibt sich für den Flächeninhalt des Dreiecks DEF 1/2 · |DE| · |MF| = 3√61/10; wegen 2 · 3,6 + 3√61/10 ≈ 9,5 beträgt der Inhalt der zu bedeckenden Fläche etwa 9,5 m² (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur das Dreieck angeben",
    bemerkung="Standardbezug: K2 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2024MgrundlegendBAGLAA2WTR1", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Teilpunkte einer Strecke in drei gleiche Abschnitte berechnen", typ_neben="",
    stichwoerter="AE = (−3; 2; 0)|OA + 1/3 AE = (2; 2/3; 0)",
    voraussetzungen="Vektor der Strecke|Drittelung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=DACH, kontext="Eingangsüberdachung", textumfang="mittel",
    gegeben="Strebe von A(3 | 0 | 0) nach E(0 | 2 | 0); zwei Befestigungspunkte teilen sie in drei gleiche Abschnitte",
    gesucht="Koordinaten eines Befestigungspunkts",
    verfahren="A + 1/3 · AE",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="mit AE = (−3; 2; 0) gilt OA + 1/3 · AE = (2; 2/3; 0) (amtlich)",
    zwischenergebnis="zweiter Punkt (1 | 4/3 | 0)", niveau_geschaetzt="I",
    fehlerquelle="Mittelpunkt statt Drittelpunkt",
    bemerkung="Standardbezug: K3 I, K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAGLAA2WTR1", "c", innen="1", seite="2", punkte="6", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Innenwinkel zwischen Dachebene und vertikaler Wand über den Neigungswinkel berechnen", typ_neben="Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen",
    stichwoerter="Hausdach 3y + 3,6z = 0, Normalenvektor (0; 3; 3,6)|cos α = 3,6/√(9 + 12,96) ⇒ α ≈ 40° (Neigung gegen die Horizontale)|Innenwinkel Dach – vertikale Wand 90° + 40° = 130°|Dreieck DEF parallel zum Hausdach: 3y + 3,6z = c, E einsetzen: c = 6",
    voraussetzungen="Winkel zwischen Ebene und xy-Ebene|Innenwinkel aus der Abbildung ergänzen|parallele Ebene mit gleichem Normalenvektor|Punkt einsetzen",
    format="Rechnung", operator="Bestimmen Sie|Ermitteln Sie", antwort="Zahl",
    material="Körper", skizze=DACH, kontext="Eingangsüberdachung", textumfang="mittel",
    gegeben="Hausdach in der Ebene 3y + 3,6z = 0; Hauswand vertikal; Übergang Dach – Wand in der x-Achse; Dreieck DEF mit E(0 | 2 | 0)",
    gesucht="Winkel im Inneren des Hauses zwischen Hausdach und Wand; Koordinatengleichung der Ebene des Dreiecks DEF",
    verfahren="Neigungswinkel über Normalenvektoren, Innenwinkel ergänzen; parallele Ebene durch E",
    schritte="4", zahlenraum="dezimal", einheiten="°", abhaengig_von="",
    ergebnis="cos α = ((0; 3; 3,6) · (0; 0; 1)) / (|(0; 3; 3,6)| · |(0; 0; 1)|) liefert α ≈ 40°; somit beträgt die Größe des Winkels zwischen Hausdach und vertikaler Hauswand etwa 130°; die Ebene hat eine Gleichung der Form 3y + 3,6z = c, da E in der Ebene liegt, gilt 3 · 2 + 3,6 · 0 = c, d. h. c = 6 (amtlich)",
    zwischenergebnis="α ≈ 39,8°", niveau_geschaetzt="II",
    fehlerquelle="40° oder 50° als Innenwinkel angeben",
    bemerkung="Traegerbindung: Kontext (welcher Winkel im Inneren des Hauses gemeint ist, zeigt nur die Abbildung; die Parallelität von Dreieck und Hausdach folgt aus AD = BE = CF im Aufgabenstamm). Standardbezug: K1 II, K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAGLAA2WTR1", "d", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Spurpunkt einer Lichtgeraden als Schatten auf der Wand aus einem Lösungsweg erläutern", typ_neben="",
    stichwoerter="Schritt I: Gerade durch E in Lichtrichtung mit y = 0 geschnitten – Schatten von E auf der Wandebene (−1,8 | 0 | −1,2)|Schritt II: x < 0 und −2,5 < z < 0 – der Schatten liegt rechts neben der Überdachung auf der Hauswand",
    voraussetzungen="Spurpunkt mit der xz-Ebene als Schatten|Koordinatenbereiche als Lage auf der Wand deuten",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=DACH, kontext="Eingangsüberdachung", textumfang="lang",
    gegeben="Sonnenlicht in Richtung (−0,9; −1; −0,6); Hauswand in der xz-Ebene, 2,5 m hoch (−2,5 ≤ z ≤ 0); Schritte I: (x; 0; z) = (0; 2; 0) + λ · (−0,9; −1; −0,6) liefert λ = 2 und (−1,8 | 0 | −1,2); II: −1,8 < 0 und −2,5 < −1,2 < 0",
    gesucht="Schlussfolgerungen aus beiden Schritten im Sachzusammenhang",
    verfahren="Schritt I als Schattenpunkt, Schritt II als Lage auf der Wand deuten",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Schritt I liefert im Modell die Lage des Schattens des Eckpunkts E in der xz-Ebene; aus Schritt II ergibt sich in Verbindung mit der Abbildung, dass dieser Schatten rechts von der Eingangsüberdachung auf der vertikalen Hauswand liegt (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Schritt II als Nachweis eines Punkts auf der Überdachung deuten",
    bemerkung="Traegerbindung: Kontext (Lage „rechts von der Überdachung auf der Wand“ nur mit der Abbildung). Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAGLAA2WTR1", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Eckenzahl der Schnittvielecke einer Ebenenschar mit einem Körper und Sonderfälle angeben", typ_neben="",
    stichwoerter="Kanten AD, BE, CF verlaufen in y-Richtung (y von 0 bzw. −1,2 bis 2 bzw. 0,8)|−1,2 < s ≤ 0,8: Schnitt trifft nur die drei Kanten, Dreieck|0,8 < s < 2: F liegt unterhalb, Viereck|0 ≤ s ≤ 0,8: alle drei Kanten getroffen, Querschnitt kongruent",
    voraussetzungen="Körper als Prisma mit Kanten in y-Richtung|Schnittfigur je nach Lage der Ebene|Kongruenz der Querschnitte im Prismenbereich",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Körper", skizze=DACH, kontext="ohne", textumfang="mittel",
    gegeben="Körper K mit Ecken A(3 | 0 | 0), B(0 | 0 | 0), C(1,5 | −1,2 | 1), D(3 | 2 | 0), E(0 | 2 | 0), F(1,5 | 0,8 | 1), fünf Begrenzungsflächen; Schnitt mit y = s für −1,2 < s < 2",
    gesucht="Eckenzahl des Schnittvielecks in Abhängigkeit von s; Intervall der s mit gleicher Form und gleichem Flächeninhalt",
    verfahren="Lage der Ebene gegen die Ecken C, F, A, B, D, E vergleichen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="−1,2 < s ≤ 0,8: drei Ecken; 0,8 < s < 2: vier Ecken; für 0 ≤ s ≤ 0,8 sind sowohl Form als auch Flächeninhalt der zugehörigen Vielecke gleich (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Grenze 0,8 (y-Koordinate von F) übersehen",
    bemerkung="Standardbezug: K2 II, K4 III, K6 II. AB amtlich: III. Amtlich. Eichregel: (b) den Körper als schiefes Prisma mit Kanten in y-Richtung erkennen und daraus die Schnittfiguren und den kongruenten Bereich ableiten.")

# ---- AG/LA (A2) WTR 2: Prisma ABCDEF, Ebene W, Schar
PRIS = "Abb. 1: Schrägbild eines geraden Prismas mit rechtwinkliger Dreiecksgrundfläche ABC (C im Ursprung, A auf der x-Achse, B auf der y-Achse) und Deckfläche DEF bei z = 5, M Mittelpunkt von DE; Abb. 2 zusätzlich mit S(7,5 | 0 | 0) und der Ebene W durch M, F, S; Erwartungshorizont d: Punkt P auf AD"
row("2024MgrundlegendBAGLAA2WTR2", "a", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Oberflächeninhalt eines Prismas über einem rechtwinkligen Dreieck berechnen", typ_neben="",
    stichwoerter="Grundfläche 1/2 · 6 · 8 = 24, zweimal|Mantel 5 · (6 + 8 + 10) = 120|168",
    voraussetzungen="Dreiecksfläche|Hypotenuse mit Pythagoras|Mantel als Höhe mal Umfang",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=PRIS, kontext="ohne", textumfang="kurz",
    gegeben="gerades Prisma ABCDEF mit C(0 | 0 | 0), D(6 | 0 | 5), E(0 | 8 | 5), F(0 | 0 | 5)",
    gesucht="Oberflächeninhalt",
    verfahren="zwei Dreiecke plus drei Rechtecke",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Oberflächeninhalt 6 · 8 + 5 · (6 + 8 + √(6² + 8²)) = 168 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Mantelrechteck über der Hypotenuse vergessen",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAGLAA2WTR2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Lage dreier Punkte auf einem Kreis über den Thaleskreis begründen", typ_neben="",
    stichwoerter="OM = 1/2 (OD + OE): M Mittelpunkt von DE|Dreieck DEF rechtwinklig in F|D, E, F auf dem Thaleskreis über DE mit Mittelpunkt M",
    voraussetzungen="Mittelpunkt einer Strecke|rechter Winkel|Satz des Thales",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=PRIS, kontext="ohne", textumfang="kurz",
    gegeben="D(6 | 0 | 5), E(0 | 8 | 5), F(0 | 0 | 5), M(3 | 4 | 5)",
    gesucht="Begründung, dass D, E, F auf einem Kreis mit Mittelpunkt M liegen",
    verfahren="M als Mittelpunkt von DE, Thaleskreis",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="wegen OM = 1/2 · (OD + OE) ist M der Mittelpunkt der Strecke DE; da das Dreieck DEF in F rechtwinklig ist, liegen D, E und F auf dem Thaleskreis über DE (amtlich)",
    zwischenergebnis="Radius 5", niveau_geschaetzt="II",
    fehlerquelle="drei Abstände ausrechnen statt Thales (auch richtig, aber länger)",
    bemerkung="Standardbezug: K1 I, K2 I, K4 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Geschätzt II (Thales erkennen), amtlich I – das Erkennen eines Satzes zählt in Teil B als Reproduktion.")

row("2024MgrundlegendBAGLAA2WTR2", "c", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene durch drei Punkte bestimmen", typ_neben="",
    stichwoerter="Ansatz ax + by + cz = 30|F: 5c = 30, S: 7,5a = 30, M: 3a + 4b + 5c = 30|c = 6, a = 4, b = −3",
    voraussetzungen="Punkte in die Koordinatenform einsetzen|lineares Gleichungssystem",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=PRIS, kontext="ohne", textumfang="kurz",
    gegeben="W durch M(3 | 4 | 5), F(0 | 0 | 5), S(7,5 | 0 | 0); Kontrolle 4x − 3y + 6z = 30",
    gesucht="Koordinatengleichung von W",
    verfahren="Einsetzen in ax + by + cz = 30",
    schritte="3", zahlenraum="ganz|dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="mit W: ax + by + cz = 30 ergibt sich aus F, M, S ∈ W das Gleichungssystem I 5c = 30, II 3a + 4b + 5c = 30, III 7,5a = 30; aus I und III folgt c = 6 bzw. a = 4; aus II ergibt sich 12 + 4b + 30 = 30 und b = −3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen von b",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B), hier über den Ansatz mit Einsetzen statt über den Normalenvektor.")

row("2024MgrundlegendBAGLAA2WTR2", "d", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punkt und Ebene: Aufgabenstellung zu einer Punktprobe auf einer Kante aus dem Lösungsweg formulieren", typ_neben="",
    stichwoerter="P(6 | 0 | r), 0 ≤ r ≤ 5: Punkt der Kante AD|4 · 6 − 3 · 0 + 6r = 30: P in W|gesucht ist der Punkt von AD in W",
    voraussetzungen="Parametrisierung einer Kante|Punktprobe in der Ebene",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Körper", skizze=PRIS, kontext="ohne", textumfang="kurz",
    gegeben="Lösungsschritte (1) P(6 | 0 | r) mit 0 ≤ r ≤ 5, (2) 4 · 6 − 3 · 0 + 6 · r = 30",
    gesucht="passende Aufgabenstellung",
    verfahren="Kante AD und Ebene W erkennen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2024MgrundlegendBAGLAA2WTR2-1c",
    ergebnis="bestimmen Sie die Koordinaten des Punkts der Strecke AD, der in der Ebene W liegt (amtlich)",
    zwischenergebnis="r = 1, P(6 | 0 | 1)", niveau_geschaetzt="II",
    fehlerquelle="Kante als CF oder AB benennen",
    bemerkung="Standardbezug: K1 II, K4 II, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBAGLAA2WTR2", "e", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Eckenzahl der Schnittvielecke einer Ebenenschar mit einem Körper und Sonderfälle angeben", typ_neben="",
    stichwoerter="Ebene durch M, F, S_t enthält die Gerade MF in der Deckfläche|für 0 ≤ t < 6 schneidet sie die Kante AD und die Grundfläche: Viereck|für t ≥ 6 läuft der Schnitt durch die Seitenfläche ADFC unterhalb von A: Dreieck|t = 0: S_0 = C, Schnitt ist das Rechteck aus C, F, M und dem Fußpunkt (3 | 4 | 0) mit zwei Symmetrieachsen",
    voraussetzungen="Ebene durch die Deckflächenstrecke MF|Lage von S_t zu A(6 | 0 | 0)|Sonderfall t = 0 als Rechteck",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="Körper", skizze=PRIS, kontext="ohne", textumfang="mittel",
    gegeben="Punkte S_t(t | 0 | 0), t ≥ 0; Ebene durch M, F, S_t schneidet das Prisma in einem Vieleck",
    gesucht="Eckenzahl in Abhängigkeit von t; alle t mit zwei Symmetrieachsen",
    verfahren="Schnitt der Ebene mit den Kanten des Prismas nach Lage von S_t",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="0 ≤ t < 6: vier Ecken; t ≥ 6: drei Ecken; zwei Symmetrieachsen: t = 0 (amtlich)",
    zwischenergebnis="t = 0: Rechteck mit Ecken C, F, M und dem Fußpunkt (3 | 4 | 0)", niveau_geschaetzt="III",
    fehlerquelle="t = 6 (S_6 = A) dem Viereck zuschlagen",
    bemerkung="Standardbezug: K2 III, K4 III, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Sonderfall t = 0 (Rechteck) und Grenzfall S_6 = A erkennen. Typ wiederverwendet (2024-ga-B AG/LA A2 WTR 1 e).")

row("2024MgrundlegendBAGLAA2WTR2", "f", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Parameter für einen rechten Winkel über das Skalarprodukt ermitteln", typ_neben="",
    stichwoerter="MF = (−3; −4; 0), MS_t = (t − 3; −4; −5)|MF · MS_t = −3(t − 3) + 16 = 0 ⇔ t = 25/3",
    voraussetzungen="Vektoren vom Scheitel M|Skalarprodukt null",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=PRIS, kontext="ohne", textumfang="kurz",
    gegeben="Dreieck MFS_t mit M(3 | 4 | 5), F(0 | 0 | 5), S_t(t | 0 | 0)",
    gesucht="t für einen rechten Winkel in M",
    verfahren="Skalarprodukt der Schenkel null setzen",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="MF · MS_t = 0 ⇔ (−3; −4; 0) · (t − 3; −4; −5) = 0 ⇔ −3t + 9 + 16 = 0 ⇔ t = 25/3 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vektoren von F statt von M aus",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

# ---- Stochastik WTR 1: Baumarkt, Glücksrad
BAUMG = "Baumdiagramm: erste Drehung 2 (5/6) oder 5 (1/6), zweite Drehung ebenso"
row("2024MgrundlegendBStochastikWTR1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Schnittwahrscheinlichkeit zweier Ereignisse im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="P(nicht T ∩ M) = 0,05: Morgenkunde und kein Treuekunde mit 5 %",
    voraussetzungen="Schnitt und Gegenereignis in Worte fassen",
    format="Kurzantwort", operator="Interpretieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Baumarkt/Kunden", textumfang="mittel",
    gegeben="T Treuekunde (60 %), M Morgenkunde (20 %); P(nicht T ∩ M) = 0,05",
    gesucht="Bedeutung der Gleichung",
    verfahren="Ereignis in Worte übersetzen",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="die Wahrscheinlichkeit dafür, dass die ausgewählte Person ein Morgenkunde und kein Treuekunde ist, beträgt 5 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Schnitt als bedingte Wahrscheinlichkeit lesen",
    bemerkung="Standardbezug: K3 I, K6 II. AB amtlich: II. Amtlich. Geschätzt I: Übersetzen eines Schnittterms in Worte; amtlich II über K6.")

row("2024MgrundlegendBStochastikWTR1", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="P(T) = 0,6, P(M) = 0,2, P(nicht T ∩ M) = 0,05|Felder 0,15, 0,05, 0,45, 0,35",
    voraussetzungen="Ränder und Differenzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Baumarkt/Kunden", textumfang="kurz",
    gegeben="60 % Treuekunden, 20 % Morgenkunden, P(nicht T ∩ M) = 0,05",
    gesucht="vollständige Vierfeldertafel",
    verfahren="Ränder eintragen, Felder als Differenzen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="M und T 0,15, M und nicht T 0,05, nicht M und T 0,45, nicht M und nicht T 0,35; Ränder 0,2 / 0,8 und 0,6 / 0,4 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="0,05 als P(T ∩ M) eintragen",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2024MgrundlegendBStochastikWTR1", "c", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Anteil für genau eines von zwei Ereignissen aus Anteilen und Schnitt berechnen", typ_neben="",
    stichwoerter="entweder T oder M: P(T ∩ nicht M) + P(nicht T ∩ M) = 0,45 + 0,05 = 50 %",
    voraussetzungen="ausschließendes Oder als zwei Felder",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Tabelle", skizze="Vierfeldertafel aus b", kontext="Baumarkt/Kunden", textumfang="kurz",
    gegeben="Vierfeldertafel aus b",
    gesucht="P(entweder Treuekunde oder Morgenkunde)",
    verfahren="zwei Felder addieren",
    schritte="1", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2024MgrundlegendBStochastikWTR1-1b",
    ergebnis="P(T ∩ nicht M) + P(nicht T ∩ M) = 0,45 + 0,05 = 50 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="einschließendes Oder (0,65)",
    bemerkung="Standardbezug: K1 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A).")

row("2024MgrundlegendBStochastikWTR1", "d", innen="1", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Stochastische Unabhängigkeit zweier Ereignisse über die Produktregel untersuchen", typ_neben="",
    stichwoerter="P_T(M) = 0,15/0,6 = 25 % ≠ P(M) = 20 %|nicht unabhängig (gleichwertig: 0,6 · 0,2 = 0,12 ≠ 0,15)",
    voraussetzungen="Unabhängigkeitskriterium über bedingte Wahrscheinlichkeit oder Produkt",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Tabelle", skizze="Vierfeldertafel aus b", kontext="Baumarkt/Kunden", textumfang="kurz",
    gegeben="Vierfeldertafel aus b",
    gesucht="ob T und M stochastisch unabhängig sind",
    verfahren="P_T(M) mit P(M) vergleichen",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="2024MgrundlegendBStochastikWTR1-1b",
    ergebnis="P_T(M) = 0,15/0,6 = 25 %; P(M) = 20 %; aufgrund der Ungleichheit der beiden Wahrscheinlichkeiten sind T und M nicht stochastisch unabhängig (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P(T ∩ M) ≠ 0 als Abhängigkeit deuten",
    bemerkung="Standardbezug: K3 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A); amtlicher Weg über die bedingte Wahrscheinlichkeit, Produktregel gleichwertig.")

row("2024MgrundlegendBStochastikWTR1", "a", innen="2", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm mit aus einer Pfadwahrscheinlichkeit erschlossener Einzelwahrscheinlichkeit erstellen", typ_neben="",
    stichwoerter="P(5 und 5) = p² = 1/36 ⇒ p = 1/6|P(2) = 5/6 (Kontrolle: (5/6)² = 25/36 kleinster Rabatt 4 %)|zweistufiges Baumdiagramm 2/5",
    voraussetzungen="Einzelwahrscheinlichkeit aus der Pfadwahrscheinlichkeit|zweistufiges Diagramm",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine", kontext="Baumarkt/Glücksrad", textumfang="lang",
    gegeben="Glücksrad mit Sektoren 5 und 2, zweimal gedreht; P(beide 5) = 1/36, P(kleinster Rabatt) = 25/36",
    gesucht="beschriftetes Baumdiagramm",
    verfahren="p aus p² = 1/36, Diagramm",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="Baumdiagramm mit 2 (5/6) und 5 (1/6) auf beiden Stufen (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="1/36 als Einzelwahrscheinlichkeit für 5 eintragen",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Geschätzt II (Einzelwahrscheinlichkeit erst erschließen), amtlich I.")

row("2024MgrundlegendBStochastikWTR1", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für k Treffer unmittelbar hintereinander unter n Versuchen berechnen", typ_neben="",
    stichwoerter="genau vier von sieben mit kleinstem Rabatt (25/36), direkt hintereinander: vier Startpositionen|4 · (25/36)⁴ · (11/36)³ ≈ 2,7 %",
    voraussetzungen="Pfadwahrscheinlichkeit|Anzahl der Lagen eines Blocks von vier in sieben",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=BAUMG, kontext="Baumarkt/Glücksrad", textumfang="mittel",
    gegeben="sieben Personen nacheinander; P(kleinster Rabatt) = 25/36",
    gesucht="P(genau viermal kleinster Rabatt, und zwar bei vier Personen unmittelbar hintereinander)",
    verfahren="Block von vier Treffern an 4 Positionen, Pfad mal Anzahl",
    schritte="2", zahlenraum="Bruch|Prozent", einheiten="", abhaengig_von="",
    ergebnis="4 · (25/36)⁴ · (11/36)³ ≈ 2,7 % (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Binomialkoeffizient C(7; 4) = 35 statt 4 Lagen",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBStochastikWTR1", "c", innen="2", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswertgleichung für einen Glücksradparameter aus den Spielregeln herleiten", typ_neben="",
    stichwoerter="Rabatte: 4 mit (1 − q)², 10 mit 2q(1 − q), 25 mit q²|E = 4(1 − q)² + 20q(1 − q) + 25q² = 9|⇔ 4 − 8q + 4q² + 20q − 20q² + 25q² = 9 ⇔ 9q² + 12q − 5 = 0",
    voraussetzungen="Verteilung des Produkts aus zwei Drehungen|Erwartungswert mit Parameter|Umformen",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Baumarkt/Glücksrad", textumfang="lang",
    gegeben="anderes Glücksrad, P(5) = q je Drehung, Rabatt = Produkt der beiden Zahlen; Gleichung 9q² + 12q − 5 = 0",
    gesucht="Nachweis, dass die Gleichung den Wert q für einen mittleren Rabatt von 9 % liefert",
    verfahren="Erwartungswert des Rabatts in q aufstellen, gleich 9 setzen, umformen",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="Prozent", abhaengig_von="",
    ergebnis="4 · (1 − q)² + 2 · 10 · q · (1 − q) + 25 · q² = 9 ⇔ 4 − 8q + 4q² + 20q − 20q² + 25q² = 9 ⇔ 9q² + 12q − 5 = 0 (amtlich)",
    zwischenergebnis="q = 1/3", niveau_geschaetzt="III",
    fehlerquelle="Rabatt 10 nur einmal (Pfad 2–5 und 5–2 beide zählen)",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Spielregel in einen Erwartungswertterm in q übersetzen. Typ wiederverwendet (Teil A).")

# ---- Stochastik WTR 2: Studierende, Standardabweichung
SIG = "Koordinatensystem ohne Skalen, p-Achse mit Teilstrichen, σ-Achse; Halbkreisbogen von (0 | 0) über das Maximum bei p = 0,5 zurück auf die p-Achse bei p = 1; Erwartungshorizont: 0 und 1 an der p-Achse, 60 an der σ-Achse auf Höhe des Werts bei p = 0,4"
row("2024MgrundlegendBStochastikWTR2", "a", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Ereignisse und Mengenoperationen",
    typ="Wahrscheinlichkeit des Gegenereignisses einer Vereinigung nachweisen und als Ereignis angeben", typ_neben="",
    stichwoerter="P(nicht L ∩ nicht D) = 1 − P(L ∪ D) = 1 − 0,72 = 0,28|Ereignis: weder Laptop noch Desktop-PC",
    voraussetzungen="De Morgan|Gegenwahrscheinlichkeit",
    format="Rechnung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Studierende/Endgeräte", textumfang="mittel",
    gegeben="P(L) = 0,56, P(D) = 0,33, P(mindestens eines) = 0,72",
    gesucht="Nachweis P(nicht L ∩ nicht D) = 0,28 und das Ereignis in Worten",
    verfahren="Gegenereignis der Vereinigung",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(nicht L ∩ nicht D) = 1 − 0,72 = 0,28; Ereignis: die ausgewählte Person besitzt weder einen Laptop noch einen Desktop-PC (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="1 − 0,56 − 0,33 rechnen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBStochastikWTR2", "b", innen="1", seite="1", punkte="4", afb_amtlich="I",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen", typ_neben="",
    stichwoerter="P(L ∩ D) = 0,56 + 0,33 − 0,72 = 0,17|Felder 0,17, 0,39, 0,16, 0,28|P(L ∩ nicht D) = 0,39",
    voraussetzungen="Schnitt aus der Vereinigung|Ränder und Differenzen",
    format="Tabelle|Kurzantwort", operator="Stellen Sie dar|Geben Sie an", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Studierende/Endgeräte", textumfang="kurz",
    gegeben="P(L) = 0,56, P(D) = 0,33, P(nicht L ∩ nicht D) = 0,28",
    gesucht="vollständige Vierfeldertafel und P(Laptop, aber kein Desktop-PC)",
    verfahren="Felder aus Rändern und 0,28, Feld ablesen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="2024MgrundlegendBStochastikWTR2-1a",
    ergebnis="L und D 0,17, L und nicht D 0,39, nicht L und D 0,16, nicht L und nicht D 0,28; Ränder 0,56 / 0,44 und 0,33 / 0,67; P(L ∩ nicht D) = 0,39 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="0,28 als P(nicht L) eintragen",
    bemerkung="Standardbezug: K4 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B).")

row("2024MgrundlegendBStochastikWTR2", "c", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen", typ_neben="",
    stichwoerter="P_D(L) = 0,17/0,33 ≈ 0,52",
    voraussetzungen="bedingte Wahrscheinlichkeit aus der Vierfeldertafel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze="Vierfeldertafel aus b", kontext="Studierende/Endgeräte", textumfang="kurz",
    gegeben="Auswahl unter den Desktop-Besitzern",
    gesucht="P(Laptop | Desktop)",
    verfahren="Schnitt durch Rand",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2024MgrundlegendBStochastikWTR2-1b",
    ergebnis="P_D(L) = 0,17/0,33 ≈ 0,52 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="durch 0,56 teilen (Richtung der Bedingung)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A, Definition seit Lauf 5 auch mit Vierfeldertafel).")

row("2024MgrundlegendBStochastikWTR2", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln", typ_neben="",
    stichwoerter="höchstens 70 % von 900: X ≤ 630|P(X ≤ 630) ≈ 0,91 (n = 900, p = 0,68)",
    voraussetzungen="Anteil in Anzahl umrechnen|kumulierte Verteilung am Rechner",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Studierende/Endgeräte", textumfang="mittel",
    gegeben="X Anzahl unter 900 Personen, die ein Software-Problem selbst lösen, binomialverteilt mit p = 0,68",
    gesucht="P(höchstens 70 % der 900)",
    verfahren="0,7 · 900 = 630, P(X ≤ 630)",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="0,7 · 900 = 630; P(X ≤ 630) ≈ 0,91 (n = 900, p = 0,68) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≤ 70)",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2024MgrundlegendBStochastikWTR2", "b", innen="2", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kleinste Umgebungsbreite unterhalb des Erwartungswerts für eine Mindestwahrscheinlichkeit ermitteln", typ_neben="",
    stichwoerter="μ = 0,68 · 900 = 612|P(601 ≤ X ≤ 612) ≈ 0,307 ≥ 0,3, P(602 ≤ X ≤ 612) ≈ 0,287 < 0,3|k = 11",
    voraussetzungen="Erwartungswert n · p|Intervallwahrscheinlichkeit am Rechner|kleinstes k durch Probieren",
    format="Rechnung", operator="Berechnen Sie|Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Studierende/Endgeräte", textumfang="kurz",
    gegeben="X wie in a; Bedingung P(μ − k ≤ X ≤ μ) ≥ 30 %",
    gesucht="μ und kleinstes natürliches k",
    verfahren="μ berechnen, Intervalle nach unten verlängern",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="μ = 0,68 · 900 = 612; aus P(601 ≤ X ≤ 612) ≈ 0,307 und P(602 ≤ X ≤ 612) ≈ 0,287 folgt k = 11 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="symmetrische Umgebung μ ± k rechnen",
    bemerkung="Standardbezug: K2 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt.")

row("2024MgrundlegendBStochastikWTR2", "", innen="3", seite="2", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Achsen des Graphen der Standardabweichung in Abhängigkeit von p skalieren und erläutern", typ_neben="",
    stichwoerter="p läuft von 0 bis 1: Nullstellen des Bogens bei 0 und 1|σ = √(n p (1 − p)), z. B. p = 0,4: σ = √(15000 · 0,4 · 0,6) = 60|60 auf der σ-Achse in Höhe des Graphenpunkts über p = 0,4 eintragen",
    voraussetzungen="Definitionsbereich von p|Formel für σ|einen Gitterwert berechnen und eintragen",
    format="Eintragen|Begründung", operator="Ergänzen Sie|Erläutern Sie", antwort="Grafik",
    material="Diagramm", skizze=SIG, kontext="ohne", textumfang="mittel",
    gegeben="binomialverteilte Zufallsgrößen mit n = 15000 und p; Abbildung: σ in Abhängigkeit von p ohne Achsenwerte",
    gesucht="Skalierung beider Achsen mit Erläuterung",
    verfahren="p-Achse 0 bis 1 aus dem Bogen, σ für einen Gitterwert von p berechnen",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="der kleinste Wert für p ist 0, der größte ist 1; zu jedem p lässt sich σ berechnen, beispielsweise für p = 0,4: σ = √(n · p · (1 − p)) = √(15000 · 0,4 · 0,6) = 60; Eintragungen 0 und 1 an der p-Achse, 60 an der σ-Achse (amtlich)",
    zwischenergebnis="Maximum σ ≈ 61,2 bei p = 0,5", niveau_geschaetzt="III",
    fehlerquelle="σ-Achse über das Maximum skalieren, das auf keiner Gitterlinie liegt",
    bemerkung="Standardbezug: K1 III, K2 III, K4 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) den Bogen als Graph von √(np(1 − p)) erkennen und einen passenden Gitterwert wählen. Aufgabe 3 ohne Teilaufgabenbuchstaben (id …-3).")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Nullstellen einer e-Funktion nachweisen und Tiefstelle berechnen", "Analysis", "Kurvenuntersuchung",
     "Die Nullstellen eines Produkts aus Polynom und e-Funktion über das Nullprodukt nachweisen und die Tiefstelle aus der gegebenen Ableitung berechnen.",
     "2024MgrundlegendBAnalysisWTR1-1b"),
    ("Transformation: Graph eines in y-Richtung gestreckten Scharmitglieds begründen und skizzieren", "Analysis", "Funktionsklassen und Eigenschaften",
     "Ein Scharmitglied als in y-Richtung gestreckte Fassung eines abgebildeten Graphen erkennen, Folgerungen für Extrempunkte begründen und den Graphen skizzieren.",
     "2024MgrundlegendBAnalysisWTR1-1d"),
    ("Scharparameter für einen vorgegebenen Flächeninhalt zwischen Graph und x-Achse bestimmen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Parameter einer Schar bestimmen, für den das vom Graphen und der x-Achse eingeschlossene Flächenstück einen vorgegebenen Inhalt hat.",
     "2024MgrundlegendBAnalysisWTR1-1e"),
    ("Stammfunktionen mit der x-Achse als Tangente über die Nullstellen der Funktion ermitteln", "Analysis", "Stammfunktion und Hauptsatz",
     "Die Konstanten der Stammfunktionen ermitteln, deren Graphen die x-Achse berühren, über die Bedingung H(x0) + c = 0 an den Nullstellen von h.",
     "2024MgrundlegendBAnalysisWTR1-1f"),
    ("Nullstellen und Werte: Stelle zu einem Funktionswert am Graphen im Sachzusammenhang ablesen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Stelle ablesen, an der ein abgebildeter Graph einen vorgegebenen Wert annimmt, und sie im Sachzusammenhang angeben.",
     "2024MgrundlegendBAnalysisWTR1-2a"),
    ("Wendepunkt als Zeitpunkt stärkster Abnahme im Sachzusammenhang deuten", "Analysis", "Kurvenuntersuchung",
     "Die Bedeutung eines Wendepunkts im fallenden Bereich als Zeitpunkt der stärksten Abnahme beschreiben.",
     "2024MgrundlegendBAnalysisWTR1-2b"),
    ("Aussage über zwei Größen anhand von Funktionsgraph und Ableitungsgraph beurteilen", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Eine Aussage über das Zusammenspiel zweier Größen beurteilen, wenn von der einen der Graph und von der anderen der Ableitungsgraph vorliegt.",
     "2024MgrundlegendBAnalysisWTR1-2c"),
    ("Anfangsbestand aus Endbestand und Fläche unter dem Ableitungsgraphen ermitteln", "Analysis", "Rekonstruktion von Beständen",
     "Einen Bestand zu Beginn aus einem späteren Bestand und der am Ableitungsgraphen geschätzten Fläche (Integral der Änderungsrate) ermitteln.",
     "2024MgrundlegendBAnalysisWTR1-2d"),
    ("Tiefpunkt angeben und Fehlen weiterer Extrempunkte über die Ableitung nachweisen", "Analysis", "Kurvenuntersuchung",
     "Den Tiefpunkt aus der Abbildung angeben und über die faktorisierte Ableitung nachweisen, dass eine weitere Nullstelle der Ableitung kein Extrempunkt ist.",
     "2024MgrundlegendBAnalysisWTR2-1a"),
    ("Tangenten durch einen Punkt der y-Achse an den Graphen skizzieren", "Analysis", "Tangente, Normale, Schnittwinkel",
     "In die Abbildung Tangenten an den Graphen skizzieren, die durch einen vorgegebenen Punkt außerhalb des Graphen verlaufen.",
     "2024MgrundlegendBAnalysisWTR2-1c"),
    ("Transformation: Streckfaktoren aus der Zuordnung zweier Punkte deuten und berechnen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Bedeutung der Faktoren in g(x) = a · f(b · x) als Streckungen angeben und a und b aus der Zuordnung eines Punktes berechnen.",
     "2024MgrundlegendBAnalysisWTR2-1d"),
    ("Differenzfunktion und ihr Maximum aus einem Lösungsweg im Sachzusammenhang deuten", "Analysis", "Kurvenuntersuchung",
     "Die Differenz zweier Sachfunktionen und die Schritte einer Extremwertbestimmung an ihr im Sachzusammenhang deuten.",
     "2024MgrundlegendBAnalysisWTR2-2c"),
    ("Zurückgelegte Strecke aus dem Integral der Geschwindigkeit und einer Phase konstanter Geschwindigkeit berechnen", "Analysis", "Rekonstruktion von Beständen",
     "Einen Weg als Integral einer Geschwindigkeitsfunktion über die Beschleunigungsphase plus Produkt aus konstanter Geschwindigkeit und Zeit berechnen.",
     "2024MgrundlegendBAnalysisWTR2-2d"),
    ("Nullstelle eines Differenzintegrals als Zeitpunkt gleicher Strecke deuten und ihre Lage begründen", "Analysis", "Rekonstruktion von Beständen",
     "Die Nullstelle von ∫_0^z (f − h) als Zeitpunkt gleicher zurückgelegter Strecke deuten und ihre Lage relativ zum Schnittpunkt der Geschwindigkeiten begründen.",
     "2024MgrundlegendBAnalysisWTR2-2e"),
    ("Übergangsprozess: Spanne einer Komponente nach einem Schritt bei teilweise bekannter Verteilung ermitteln", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Bei nur teilweise bekannter Verteilung die Komponente nach einem Übergangsschritt als linearen Term einer Unbekannten aufstellen und Mindest- und Höchstwert ermitteln.",
     "2024MgrundlegendBAGLAA1WTR-1c"),
    ("Unterschiedliche Beträge von Vektoren mit fester Komponentensumme über ein Beispiel begründen", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Mit einem Beispiel entscheiden, ob Vektoren mit gleicher Komponentensumme verschiedene Beträge haben können.",
     "2024MgrundlegendBAGLAA1WTR-1e"),
    ("Aussagen über Winkel zwischen Vektoren mit fester Komponentensumme beurteilen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Aussagen über Winkel von 0° (Kollinearität) und 90° (Skalarprodukt null) zwischen Vektoren mit fester Komponentensumme beurteilen.",
     "2024MgrundlegendBAGLAA1WTR-1f"),
    ("Punkt: Teilpunkte einer Strecke in drei gleiche Abschnitte berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Die Koordinaten der Punkte berechnen, die eine Strecke in gleiche Abschnitte teilen.",
     "2024MgrundlegendBAGLAA2WTR1-1b"),
    ("Innenwinkel zwischen Dachebene und vertikaler Wand über den Neigungswinkel berechnen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Den Neigungswinkel einer Ebene gegen die Horizontale über Normalenvektoren berechnen und zum verlangten Innenwinkel gegen eine vertikale Wand ergänzen.",
     "2024MgrundlegendBAGLAA2WTR1-1c"),
    ("Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen", "Analytische Geometrie", "Ebenen",
     "Die Koordinatengleichung einer zu einer gegebenen Ebene parallelen Ebene durch einen Punkt aufstellen (gleicher Normalenvektor, Punkt einsetzen; Nebenleistung).",
     "2024MgrundlegendBAGLAA2WTR1-1c"),
    ("Gerade und Ebene: Spurpunkt einer Lichtgeraden als Schatten auf der Wand aus einem Lösungsweg erläutern", "Analytische Geometrie", "Lagebeziehungen",
     "Einen vorgelegten Lösungsweg erläutern, in dem der Schnittpunkt einer Geraden in Lichtrichtung mit einer Koordinatenebene als Schattenpunkt bestimmt und seine Lage über Koordinatenbereiche gedeutet wird.",
     "2024MgrundlegendBAGLAA2WTR1-1d"),
    ("Körper: Eckenzahl der Schnittvielecke einer Ebenenschar mit einem Körper und Sonderfälle angeben", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Für eine Schar von Ebenen die Eckenzahl des Schnittvielecks mit einem Körper in Abhängigkeit vom Parameter angeben und Sonderfälle (kongruente Schnitte, Symmetrieachsen) nennen.",
     "2024MgrundlegendBAGLAA2WTR1-1e"),
    ("Körper: Oberflächeninhalt eines Prismas über einem rechtwinkligen Dreieck berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Oberflächeninhalt eines geraden Prismas aus zwei Dreiecksflächen und den Mantelrechtecken berechnen.",
     "2024MgrundlegendBAGLAA2WTR2-1a"),
    ("Ebene Figur: Lage dreier Punkte auf einem Kreis über den Thaleskreis begründen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Begründen, dass drei Punkte auf einem Kreis mit gegebenem Mittelpunkt liegen, indem der Mittelpunkt als Streckenmitte und der rechte Winkel (Thales) erkannt werden.",
     "2024MgrundlegendBAGLAA2WTR2-1b"),
    ("Punkt und Ebene: Aufgabenstellung zu einer Punktprobe auf einer Kante aus dem Lösungsweg formulieren", "Analytische Geometrie", "Lagebeziehungen",
     "Zu Lösungsschritten mit parametrisiertem Kantenpunkt und Einsetzen in eine Ebenengleichung die passende Aufgabenstellung angeben.",
     "2024MgrundlegendBAGLAA2WTR2-1d"),
    ("Term und Ereignis: Schnittwahrscheinlichkeit zweier Ereignisse im Sachzusammenhang deuten", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Eine Gleichung der Form P(A ∩ B) = c im Sachzusammenhang in Worte übersetzen.",
     "2024MgrundlegendBStochastikWTR1-1a"),
    ("Baumdiagramm mit aus einer Pfadwahrscheinlichkeit erschlossener Einzelwahrscheinlichkeit erstellen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Ein zweistufiges Baumdiagramm erstellen, dessen Einzelwahrscheinlichkeit erst aus einer gegebenen Pfadwahrscheinlichkeit erschlossen werden muss.",
     "2024MgrundlegendBStochastikWTR1-2a"),
    ("Wahrscheinlichkeit für k Treffer unmittelbar hintereinander unter n Versuchen berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit berechnen, dass unter n Versuchen genau k Treffer auftreten und diese unmittelbar aufeinander folgen (Pfad mal Anzahl der Blocklagen).",
     "2024MgrundlegendBStochastikWTR1-2b"),
    ("Wahrscheinlichkeit des Gegenereignisses einer Vereinigung nachweisen und als Ereignis angeben", "Stochastik", "Ereignisse und Mengenoperationen",
     "P(nicht A ∩ nicht B) als 1 − P(A ∪ B) nachweisen und das Ereignis im Sachzusammenhang angeben.",
     "2024MgrundlegendBStochastikWTR2-1a"),
    ("Kleinste Umgebungsbreite unterhalb des Erwartungswerts für eine Mindestwahrscheinlichkeit ermitteln", "Stochastik", "Binomialverteilung",
     "Das kleinste k ermitteln, für das P(μ − k ≤ X ≤ μ) eine vorgegebene Schranke erreicht.",
     "2024MgrundlegendBStochastikWTR2-2b"),
    ("Achsen des Graphen der Standardabweichung in Abhängigkeit von p skalieren und erläutern", "Stochastik", "Kenngrößen von Verteilungen",
     "In der Abbildung von σ(p) = √(np(1 − p)) die Achsen skalieren (p von 0 bis 1, σ über einen berechneten Gitterwert) und das Vorgehen erläutern.",
     "2024MgrundlegendBStochastikWTR2-3"),
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
