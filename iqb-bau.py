# -*- coding: utf-8 -*-
"""iqb-bau.py – Gerüst für die Erfassung eines Stapels im Profil iqb.
Version 0.5 · 14.09.2026 · gilt mit katalog-prompt.md v0.3 und iqb.md v0.7

Je Stapel werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" bleibt unverändert.

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
    "stapel": "2019-ga-A",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2019MgrundlegendAAnalysis11": 5,
        "2019MgrundlegendAAnalysis12": 5,
        "2019MgrundlegendAAnalysis2": 5,
        "2019MgrundlegendAAGLAA11": 5,
        "2019MgrundlegendAAGLAA12": 5,
        "2019MgrundlegendAAGLAA211": 5,
        "2019MgrundlegendAAGLAA212": 5,
        "2019MgrundlegendAAGLAA22": 5,
        "2019MgrundlegendAStochastik11": 5,
        "2019MgrundlegendAStochastik12": 5,
        "2019MgrundlegendAStochastik2": 5,
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
# Ein Eintrag je Teilaufgabe. Nicht genannte Felder bleiben leer.
# niveau_geschaetzt nach der Deutungsliste v0.7; bei III nennt bemerkung den Eintrag.

# ---- Analysis 1.1: zwei Parabeln
row("2019MgrundlegendAAnalysis11", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Schnittstellen zweier Graphen durch Lösen einer quadratischen Gleichung nachweisen", typ_neben="",
    stichwoerter="g(x) = h(x) ⇔ 2x² − 2x − 4 = 0 ⇔ x² − x − 2 = 0|höchstens zwei Lösungen|x = −1 und x = 2 durch Einsetzen bestätigen",
    voraussetzungen="Gleichsetzen|quadratische Gleichung hat höchstens zwei Lösungen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g(x) = x² − 3 und h(x) = −x² + 2x + 1 in IR",
    gesucht="Nachweis, dass sich die Graphen nur für x = −1 und x = 2 schneiden",
    verfahren="quadratische Gleichung g(x) = h(x) lösen oder beide Werte einsetzen und Lösungszahl begründen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="g(x) = h(x) hat als quadratische Gleichung höchstens zwei Lösungen; g(−1) = −2 = h(−1), g(2) = 1 = h(2) (amtlich)",
    zwischenergebnis="2x² − 2x − 4 = 0",
    niveau_geschaetzt="I",
    fehlerquelle="das „nur“ nicht begründen (Lösungszahl einer quadratischen Gleichung)",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2019MgrundlegendAAnalysis11", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen", typ_neben="",
    stichwoerter="h über g auf [−1; 2]|Integral von −1 bis 2 über (h(x) − g(x)) dx = Integral über (−2x² + 2x + 4) dx|[−2/3 x³ + x² + 4x] von −1 bis 2 = 9",
    voraussetzungen="Schnittstellen aus a als Grenzen|Differenzfunktion|Stammfunktion",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="g(x) = x² − 3, h(x) = −x² + 2x + 1; Schnittstellen −1 und 2",
    gesucht="Inhalt der von beiden Graphen eingeschlossenen Fläche",
    verfahren="Integral der Differenz zwischen den Schnittstellen",
    schritte="3", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="2019MgrundlegendAAnalysis11-a",
    ergebnis="Integral von −1 bis 2 über (h(x) − g(x)) dx = Integral von −1 bis 2 über (−2x² + 2x + 4) dx = [−2/3 x³ + x² + 4x] von −1 bis 2 = −16/3 + 4 + 8 − 2/3 − 1 + 4 = 9 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen beim Einsetzen der unteren Grenze −1",
    bemerkung="Standardbezug: K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (zusammengezogener Typ aus Abgleichlauf 3).")

# ---- Analysis 1.2: kubische Funktion
row("2019MgrundlegendAAnalysis12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Stellen mit vorgegebenem Funktionswert durch Ausklammern berechnen", typ_neben="",
    stichwoerter="f(x) = 1 ⇔ 1/3 x³ − 4/3 x = 0 ⇔ 1/3 x · (x² − 4) = 0|x = −2, x = 0, x = 2",
    voraussetzungen="Gleichung f(x) = 1|Ausklammern von x|Satz vom Nullprodukt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/3 x³ − 4/3 x + 1 in IR; Gerade y = 1",
    gesucht="x-Koordinaten der Schnittpunkte von Graph und Gerade",
    verfahren="f(x) = 1 setzen, x ausklammern, Nullprodukt",
    schritte="2", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(x) = 1 ⇔ 1/3 x · (x² − 4) = 0 ⇔ x = −2 ∨ x = 0 ∨ x = 2 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Lösung x = 0 beim Kürzen durch x verlieren",
    bemerkung="Standardbezug: K2 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2019MgrundlegendAAnalysis12", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen", typ_neben="",
    stichwoerter="f'(x) = x² − 4/3|f' nimmt bei x = 0 den kleinsten Wert an|Steigung −4/3",
    voraussetzungen="Tangentensteigung als Ableitungswert|Minimum einer nach oben geöffneten Parabel (oder f'' = 0)",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 1/3 x³ − 4/3 x + 1; unter den Tangenten an den Graphen hat eine die kleinste Steigung",
    gesucht="Steigung dieser Tangente",
    verfahren="Ableitung bilden, ihr Minimum bestimmen",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = x² − 4/3 nimmt für x = 0 den kleinsten Wert an, die Tangente hat also die Steigung −4/3 (amtlich)",
    zwischenergebnis="Wendestelle 0",
    niveau_geschaetzt="II",
    fehlerquelle="Minimum von f statt von f' suchen",
    bemerkung="Standardbezug: K1 II, K2 II, K5 I. Amtlich, eigene Rechnung bestätigt. Verkettung Ableitung → Minimum der Ableitung ohne Deutung, II.")

# ---- Analysis 2: sin x − 2
SIN_SKIZZE = ("Koordinatensystem mit Gitter, x-Achse von etwa −π bis 4π mit Marken 0, π, 2π, 3π, y-Achse mit Marken −2 und 2; "
              "kein Graph eingezeichnet")
row("2019MgrundlegendAAnalysis2", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Transformation: Verschobenen Graphen in die Abbildung skizzieren", typ_neben="",
    stichwoerter="Sinuskurve um 2 nach unten verschoben|Werte zwischen −3 und −1|Nullstellen von sin bei kπ liegen auf y = −2",
    voraussetzungen="Graph der Sinusfunktion|Verschiebung in y-Richtung",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=SIN_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = sin(x) − 2 in IR; Koordinatensystem mit Gitter für −π ≤ x ≤ 4π",
    gesucht="Skizze des Graphen von f im Koordinatensystem",
    verfahren="Sinuskurve um 2 nach unten verschoben einzeichnen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="Sinuskurve mit Mittellinie y = −2, Hochpunkte bei y = −1 (x = π/2, 5π/2), Tiefpunkte bei y = −3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Kurve um 2 nach rechts statt nach unten verschieben",
    bemerkung="Standardbezug: K4 I. Amtlich. Typ wiederverwendet.")

row("2019MgrundlegendAAnalysis2", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Gleichschenkligkeit des Dreiecks aus Tangente und Koordinatenachsen allgemein begründen", typ_neben="",
    stichwoerter="f'(2kπ) = cos(2kπ) = 1 für alle k|Tangente mit Steigung 1 schneidet die Achsen im gleichen Abstand vom Ursprung|zwei gleich lange Seiten",
    voraussetzungen="Ableitung von sin|cos(2kπ) = 1|Steigung 1 heißt gleiche Achsenabschnitte (bis aufs Vorzeichen)",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SIN_SKIZZE, kontext="ohne", textumfang="mittel",
    gegeben="f(x) = sin(x) − 2; Tangenten in den Punkten (2kπ | f(2kπ)) mit k ∈ IN; jede schließt mit den Koordinatenachsen ein Dreieck ein",
    gesucht="Begründung, dass jedes dieser Dreiecke gleichschenklig ist",
    verfahren="Tangentensteigung 1 nachweisen und in gleiche Abstände der Achsenschnittpunkte vom Ursprung übersetzen",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(2kπ) = cos(2kπ) = 1 für alle k ∈ IN, d. h. die betrachteten Tangenten haben die Steigung 1; bei jeder Tangente haben die Schnittpunkte mit den Koordinatenachsen also den gleichen Abstand vom Koordinatenursprung, damit hat jedes der Dreiecke zwei gleich lange Seiten (amtlich)",
    zwischenergebnis="Tangente y = x − 2kπ − 2, Achsenabschnitte 2kπ + 2 und −(2kπ + 2)",
    niveau_geschaetzt="III",
    fehlerquelle="nur für k = 0 rechnen statt allgemein zu argumentieren",
    bemerkung="Standardbezug: K1 III, K2 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (c) allgemeiner Nachweis für alle k mit der hergeleiteten Beziehung Steigung 1 ⇒ gleiche Achsenabschnitte.")

# ---- AG/LA (A1) 1: Brutgebiete
BRUT_SKIZZE = ("Übergangsdiagramm mit zwei Kreisen A und B; Schleife an A mit 0,9, Schleife an B mit 0,8; "
               "Pfeil von A nach B mit 0,1, Pfeil von B nach A mit 0,2")
row("2019MgrundlegendAAGLAA11", "a", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsgleichung mit Matrix aus dem Diagramm aufstellen und Variablen deuten", typ_neben="",
    stichwoerter="(a_{n+1}; b_{n+1}) = ((0,9; 0,2), (0,1; 0,8)) · (a_n; b_n)|a_n, b_n Anteile der in A bzw. B brütenden Vögel im Jahr n|Spalten des Diagramms als Spalten der Matrix",
    voraussetzungen="Übergangsmatrix aus dem Diagramm (Spaltensumme 1)|Verteilung als Vektor|Bedeutung der Variablen",
    format="Kurzantwort", operator="Stellen Sie dar|Geben Sie an", antwort="Term",
    material="Diagramm", skizze=BRUT_SKIZZE, kontext="Vögel/Brutgebiete", textumfang="mittel",
    gegeben="Vögel brüten jährlich in Gebiet A oder B; Übergangsdiagramm mit 0,9 (A bleibt), 0,1 (A → B), 0,2 (B → A), 0,8 (B bleibt)",
    gesucht="Gleichung mit einer Matrix für die Änderung der Verteilung von einem Jahr zum nächsten und Bedeutung aller Variablen",
    verfahren="Matrix aus dem Diagramm ablesen, Vektorgleichung aufstellen, Variablen benennen",
    schritte="2", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="(a_{n+1}; b_{n+1}) = ((0,9; 0,2), (0,1; 0,8)) · (a_n; b_n); dabei sind a_n und b_n die Anteile der in A bzw. B brütenden Vögel im Jahr n, a_{n+1} und b_{n+1} die im Jahr n + 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Matrix transponiert aufstellen (Zeilensumme 1)",
    bemerkung="Standardbezug: K3 II, K4 I, K5 I. Amtlich. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2019MgrundlegendAAGLAA11", "b", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Anteil nach zwei Übergängen aus dem Diagramm berechnen", typ_neben="",
    stichwoerter="Start (1; 0)|nach zwei Jahren in A: 0,9 · 0,9 + 0,1 · 0,2 = 0,83|83 %",
    voraussetzungen="zwei Pfade über zwei Jahre|Produkt und Summe der Übergangsanteile",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=BRUT_SKIZZE, kontext="Vögel/Brutgebiete", textumfang="kurz",
    gegeben="Übergangsdiagramm aus a; in einem Jahr brüten alle Vögel in A",
    gesucht="prozentualer Anteil der Vögel, die zwei Jahre später in A brüten",
    verfahren="beide Pfade A → A → A und A → B → A addieren (oder M² · (1; 0))",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="%", abhaengig_von="2019MgrundlegendAAGLAA11-a",
    ergebnis="0,9² + 0,1 · 0,2 = 83 % (amtlich)",
    zwischenergebnis="nach einem Jahr (0,9; 0,1)",
    niveau_geschaetzt="I",
    fehlerquelle="Pfad über B vergessen (81 %)",
    bemerkung="Standardbezug: K4 I, K5 I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A1) 2: Käferpopulation
row("2019MgrundlegendAAGLAA12", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Quadrat einer Matrix mit Parameter berechnen", typ_neben="",
    stichwoerter="M = ((0; 0; a), (1/4; 0; 0), (0; 1/2; 0))|M² = ((0; a/2; 0), (0; 0; a/4), (1/8; 0; 0))",
    voraussetzungen="Matrixmultiplikation Zeile mal Spalte",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Käfer/Population", textumfang="mittel",
    gegeben="Population (E; L; K) aus Eiern, Larven, Käfern; Übergang je Monat durch M = ((0; 0; a), (1/4; 0; 0), (0; 1/2; 0)) mit a > 0",
    gesucht="Matrix M²",
    verfahren="M · M ausmultiplizieren",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="M² = ((0; a/2; 0), (0; 0; a/4), (1/8; 0; 0)) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Einträge elementweise quadrieren",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

row("2019MgrundlegendAAGLAA12", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Langfristige Entwicklung aus M³ als Vielfachem der Einheitsmatrix durch Fallunterscheidung beschreiben", typ_neben="",
    stichwoerter="M³ = a/8 · E: alle drei Monate Faktor a/8 auf jede Anzahl|a < 8 Aussterben|a = 8 Rückkehr zu den Anfangswerten alle drei Monate|a > 8 dauerhafte Zunahme",
    voraussetzungen="M³ · v = a/8 · v deuten|Vielfaches der Einheitsmatrix|Fallunterscheidung nach a",
    format="Kurzantwort", operator="Interpretieren Sie|Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Käfer/Population", textumfang="mittel",
    gegeben="M aus a; M³ = a/8 · E (Einheitsmatrix mit Faktor a/8)",
    gesucht="Deutung der Gleichung im Sachzusammenhang und langfristige Entwicklung der Population in Abhängigkeit von a",
    verfahren="Faktor a/8 je drei Monate deuten, drei Fälle a < 8, a = 8, a > 8",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="2019MgrundlegendAAGLAA12-a",
    ergebnis="jeweils innerhalb von drei Monaten verändern sich die Anzahlen der Eier, Larven und Käfer mit dem Faktor a/8; für a < 8 stirbt die Population langfristig aus, für a = 8 erreichen die Anzahlen alle drei Monate die Anfangswerte, für a > 8 nehmen sie dauerhaft zu (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur „Faktor a/8“ nennen, ohne die Fälle zu unterscheiden",
    bemerkung="Standardbezug: K1 III, K3 III, K6 II. Amtlich. Eichregel: Fallunterscheidung a < 8, a = 8, a > 8 mit verschiedenem Ausgang (Grundregel). Vom Typ „Entwicklung einer Population aus einer Potenz der inversen Matrix beschreiben“ (2023-ea-A) getrennt: dort inverse Matrix und fester Zyklus, hier Vielfaches der Einheitsmatrix mit Parameter. Aufgabengruppe A1, außerhalb der Geltung Berlin/Brandenburg.")

# ---- AG/LA (A2) 1.1: Punkte A, B, C
row("2019MgrundlegendAAGLAA211", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punkt auf einer Geraden mit vorgegebener Koordinate angeben", typ_neben="",
    stichwoerter="x-Koordinate: 0 − r = 4 ⇔ r = −4|z_B = 2 + (−4) · (−2) = 10",
    voraussetzungen="Parameter aus einer Koordinate|Einsetzen in die dritte Koordinate",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(0 | 2 | 2), B(4 | −1 | z_B), C(−3 | y_C | 6); B liegt auf der Geraden x = (0; 2; 2) + r · (−1; 0,75; −2)",
    gesucht="Wert von z_B",
    verfahren="r aus der x-Koordinate, z aus der Geradengleichung",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="0 − r = 4 ⇔ r = −4, d. h. z_B = 2 + 8 = 10 (amtlich)",
    zwischenergebnis="Probe y: 2 + (−4) · 0,75 = −1",
    niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen von r · (−2)",
    bemerkung="Standardbezug: K5 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2019MgrundlegendAAGLAA211", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Untere Schranke für den Abstand zweier Punkte mit einer unbekannten Koordinate nachweisen", typ_neben="",
    stichwoerter="|AC| = √(9 + (y_C − 2)² + 16)|(y_C − 2)² ≥ 0|Abstand mindestens √25 = 5",
    voraussetzungen="Abstandsformel mit Variable|Quadrat nichtnegativ|Monotonie der Wurzel",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(0 | 2 | 2), C(−3 | y_C | 6) mit unbekanntem y_C",
    gesucht="Nachweis, dass der Abstand von A und C mindestens 5 beträgt",
    verfahren="Abstandsterm in y_C aufstellen und nach unten abschätzen",
    schritte="2", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="|AC| = √(9 + (y_C − 2)² + 16); wegen (y_C − 2)² ≥ 0 beträgt der Abstand mindestens √(9 + 16) = 5 (amtlich)",
    zwischenergebnis="Gleichheit für y_C = 2",
    niveau_geschaetzt="II",
    fehlerquelle="y_C = 2 setzen, ohne zu begründen, dass dies das Minimum ist",
    bemerkung="Standardbezug: K1 II, K2 II, K5 II. Amtlich, eigene Rechnung bestätigt. Abschätzung über ein nichtnegatives Quadrat ist Routine, keine zu findende Deutung, II.")

# ---- AG/LA (A2) 1.2: gerades Prisma
row("2019MgrundlegendAAGLAA212", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen", typ_neben="",
    stichwoerter="BA = (−√20; −4; 0), BC = (−√20; 4; 0)|BA · BC = 20 − 16 = 4 ≠ 0",
    voraussetzungen="Verbindungsvektoren|Skalarprodukt ungleich null heißt kein rechter Winkel",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="gerades Prisma ABCDEF mit Grundfläche A(0 | −4 | 0), B(√20 | 0 | 0), C(0 | 4 | 0)",
    gesucht="Nachweis, dass das Dreieck ABC bei B nicht rechtwinklig ist",
    verfahren="Skalarprodukt der Schenkelvektoren bei B",
    schritte="2", zahlenraum="ganz|Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="BA = (−√20; −4; 0), BC = (−√20; 4; 0), BA · BC = 20 − 16 ≠ 0 (amtlich)",
    zwischenergebnis="Skalarprodukt 4",
    niveau_geschaetzt="I",
    fehlerquelle="(√20)² = 20 falsch berechnen",
    bemerkung="Standardbezug: K1 I, K5 I. Amtlich, eigene Rechnung bestätigt.")

row("2019MgrundlegendAAGLAA212", "b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Höhe eines Prismas aus dem Mantelflächeninhalt bestimmen", typ_neben="",
    stichwoerter="|AB| = |BC| = √(20 + 16) = 6, |AC| = 8|Mantel = Umfang · h = (6 + 6 + 8) · h = 60|h = 3",
    voraussetzungen="Mantelfläche eines geraden Prismas als Umfang mal Höhe|Seitenlängen über Beträge",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="gerades Prisma über dem Dreieck ABC aus a; Inhalt der Mantelfläche 60",
    gesucht="Höhe des Prismas",
    verfahren="Umfang des Dreiecks berechnen, Mantel = Umfang · h nach h auflösen",
    schritte="3", zahlenraum="ganz|Wurzel", einheiten="", abhaengig_von="2019MgrundlegendAAGLAA212-a",
    ergebnis="AC = (0; 8; 0), (|AB| + |BC| + |AC|) · h = (6 + 6 + 8) · h = 60 ⇔ h = 3 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Grundflächen zur Mantelfläche dazurechnen",
    bemerkung="Standardbezug: K2 II, K5 I. Amtlich, eigene Rechnung bestätigt.")

# ---- AG/LA (A2) 2: Punkte und Gerade
ABC_SKIZZE = ("Koordinatensystem als Schrägbild mit Achsen x (nach vorn links), y (nach rechts), z (nach oben); "
              "B im Ursprung, C auf der y-Achse, A oberhalb von C; keine Skalen")
row("2019MgrundlegendAAGLAA22", "a", seite="1", punkte="2", afb_amtlich="",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen", typ_neben="",
    stichwoerter="|(−2; 1; 2)| = 3|Abstand 6 heißt Parameter ±2|(0; 4; 2) + 2 · (−2; 1; 2) = (−4; 6; 6)",
    voraussetzungen="Betrag des Richtungsvektors|Vielfaches mit vorgegebener Länge|Punkt der Geraden",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ABC_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="A(0 | 4 | 2), B(0 | 0 | 0), C(0 | 4 | 0); Gerade g durch A mit Richtungsvektor (−2; 1; 2)",
    gesucht="Koordinaten eines Punkts auf g mit Abstand 6 von A",
    verfahren="Richtungsvektor auf Länge 6 strecken und an A ansetzen",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="|(−2; 1; 2)| = 3, (0; 4; 2) + 2 · (−2; 1; 2) = (−4; 6; 6); damit (−4 | 6 | 6) (amtlich)",
    zwischenergebnis="ebenso (4 | 2 | −2)",
    niveau_geschaetzt="II",
    fehlerquelle="Abstand 6 als Parameter 6 nehmen (Länge 18)",
    bemerkung="Standardbezug: keine Eintragung (Zeile a der Matrix ist leer, nur BE 2). Amtlich, eigene Rechnung bestätigt. Zählt in der Eichung nicht (iqb-bau.py v0.5).")

row("2019MgrundlegendAAGLAA22", "b", seite="1", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkte mit gleichem Abstand zu drei Eckpunkten eines rechtwinkligen Dreiecks über den Thaleskreis ermitteln", typ_neben="",
    stichwoerter="Dreieck ABC bei C rechtwinklig|C auf dem Thaleskreis über AB|Mittelpunkt M(0; 2; 1) von AB gleich weit von A, B, C|weitere Punkte auf der Lotgeraden zur yz-Ebene durch M, z. B. (1; 2; 1)",
    voraussetzungen="rechten Winkel erkennen|Thaleskreis: Mittelpunkt der Hypotenuse als Umkreismittelpunkt|Lot auf die Dreiecksebene",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=ABC_SKIZZE, kontext="ohne", textumfang="kurz",
    gegeben="A(0 | 4 | 2), B(0 | 0 | 0), C(0 | 4 | 0) in der yz-Ebene",
    gesucht="Koordinaten zweier Punkte mit gleichem Abstand zu A, B und C",
    verfahren="rechten Winkel bei C erkennen, Mittelpunkt der Hypotenuse AB, dann Lotgerade zur Dreiecksebene",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="das Dreieck ABC ist in C rechtwinklig, C liegt also auf dem Thaleskreis über AB, d. h. der Mittelpunkt M(0 | 2 | 1) von AB hat von A, B und C den gleichen Abstand; alle weiteren Punkte mit dieser Eigenschaft liegen auf der Lotgeraden zur yz-Ebene durch M, beispielsweise (1 | 2 | 1) (amtlich)",
    zwischenergebnis="Abstand √5",
    niveau_geschaetzt="III",
    fehlerquelle="drei Abstandsgleichungen ansetzen und im Gleichungssystem stecken bleiben",
    bemerkung="Standardbezug: K1 III, K2 III, K6 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (b) Sonderfall erkennen – rechter Winkel bei C, Thaleskreis – und mit dem Lot verketten.")

# ---- Stochastik 1.1: Chor
row("2019MgrundlegendAStochastik11", "a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Laplace-Wahrscheinlichkeit für den ersten Zug angeben", typ_neben="",
    stichwoerter="20 andere Mitglieder, 11 Frauen|11/20",
    voraussetzungen="Leiterin herausrechnen|günstige durch mögliche",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Chor/Preisverleihung", textumfang="mittel",
    gegeben="Chor aus 12 Frauen und 9 Männern, eine Frau leitet; die Leiterin nimmt teil, das zweite Mitglied wird zufällig aus den übrigen gewählt",
    gesucht="Wahrscheinlichkeit, dass das zweite Mitglied eine Frau ist",
    verfahren="Anteil der Frauen unter den 20 übrigen",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="11/20 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="12/21 (Leiterin nicht abziehen)",
    bemerkung="Standardbezug: K3 I, K6 I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet.")

row("2019MgrundlegendAStochastik11", "b", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen", typ_neben="",
    stichwoerter="11 Frauen, 9 Männer unter den anderen Mitgliedern|mehr Frauenpaare als Männerpaare",
    voraussetzungen="Vergleich der Anzahlen ohne Rechnung",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Chor/Preisverleihung", textumfang="mittel",
    gegeben="die Leiterin kann nicht teilnehmen; zwei der anderen 20 Mitglieder (11 Frauen, 9 Männer) werden zufällig ausgewählt",
    gesucht="Begründung ohne Rechnung, dass P(zwei Frauen) > P(zwei Männer)",
    verfahren="Anzahl der Frauen mit der der Männer vergleichen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="die Anzahl der Frauen unter den anderen Mitgliedern ist größer als die der Männer (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="doch rechnen (55/190 gegen 36/190) statt zu begründen",
    bemerkung="Standardbezug: K1 I, K3 I. Amtlich. Typ wiederverwendet.")

row("2019MgrundlegendAStochastik11", "c", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="(11 über 1) · (9 über 1) / (20 über 2) = 99/190|ebenso 2 · 11/20 · 9/19",
    voraussetzungen="Auswahl von zwei aus 20 ohne Reihenfolge|günstige Paare Frau–Mann|oder Pfadregel mit zwei Reihenfolgen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Chor/Preisverleihung", textumfang="kurz",
    gegeben="zwei der 20 anderen Mitglieder (11 Frauen, 9 Männer) werden zufällig ausgewählt",
    gesucht="Wahrscheinlichkeit, dass eine Frau und ein Mann ausgewählt werden",
    verfahren="Anzahl günstiger Paare durch Anzahl aller Paare (oder zwei Pfade ohne Zurücklegen)",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="(11 über 1) · (9 über 1) / (20 über 2) = 99/190 (amtlich)",
    zwischenergebnis="≈ 0,521",
    niveau_geschaetzt="II",
    fehlerquelle="nur einen Pfad Frau–Mann rechnen (99/380)",
    bemerkung="Standardbezug: K3 II, K5 II. Amtlich, eigene Rechnung bestätigt. Erwartungshorizont mit Binomialkoeffizienten (hypergeometrisch), gleichwertig über zwei Pfade ohne Zurücklegen; Thema Zufallsexperimente und Urnenmodelle wie bei den früheren Zeilen dieses Typs, Typ wiederverwendet.")

# ---- Stochastik 1.2: Urne 3 rot, 7 weiß
URNE_SKIZZE = ("zwei Säulendiagramme I und II über 0 bis 10 mit y-Marken 0,2 und 0,4; I: Säulen bei 0 bis 7, Maximum etwa 0,3 bei 3, "
               "bei 1 und 2 etwa 0,2 und 0,25, bei 4 etwa 0,2, bei 5 etwa 0,1; II: Säulen bei 3 bis 10, Maximum etwa 0,38 bei 7, "
               "bei 6 etwa 0,3, bei 8 etwa 0,35, bei 5 etwa 0,15, bei 9 etwa 0,18 – Summe deutlich über 1")
row("2019MgrundlegendAStochastik12", "a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit für höchstens einmal bei zwei Zügen über das Gegenereignis berechnen", typ_neben="",
    stichwoerter="Gegenereignis: beide weiß, 0,7 · 0,7 = 0,49|1 − 0,49 = 0,51",
    voraussetzungen="Ziehen mit Zurücklegen|Gegenereignis „beide weiß“|Pfadregel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="Urne mit 3 roten und 7 weißen Kugeln; zweimal Ziehen mit Zurücklegen",
    gesucht="Wahrscheinlichkeit, dass höchstens eine der entnommenen Kugeln weiß ist",
    verfahren="1 minus Wahrscheinlichkeit für zwei weiße",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="1 − 7/10 · 7/10 = 51/100 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="„höchstens eine“ als „genau eine“ lesen (0,42)",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Wahrscheinlichkeit für mindestens einmal über das Gegenereignis im Baumdiagramm nachweisen“ getrennt: anderes Ereignis (höchstens einmal), kein Baumdiagramm vorgelegt.")

row("2019MgrundlegendAStochastik12", "b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Unpassende Säulendiagramme zu einer Binomialverteilung begründet ausschließen", typ_neben="",
    stichwoerter="X ~ B(10; 0,7), E(X) = 7|I: Maximum bei 3 statt nahe 7|II: Summe der Säulen größer als 1",
    voraussetzungen="Erwartungswert n · p|Lage des Maximums nahe dem Erwartungswert|Summe einer Verteilung ist 1",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Diagramm", skizze=URNE_SKIZZE, kontext="Urne/Kugelspiel", textumfang="mittel",
    gegeben="zehnmal Ziehen mit Zurücklegen aus 3 roten und 7 weißen Kugeln; X Anzahl der weißen Kugeln; zwei Säulendiagramme I und II",
    gesucht="Begründung ohne Berechnung von Wahrscheinlichkeiten, dass keines der Diagramme die Verteilung von X zeigt",
    verfahren="I über den Erwartungswert 7 ausschließen, II über die Summe der Säulen",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="I: der Erwartungswert von X ist 7, damit ist die Wahrscheinlichkeit für drei weiße Kugeln nicht am größten; II: die Summe der Werte einer Wahrscheinlichkeitsverteilung ist nicht größer als 1 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="bei II nur die Lage des Maximums prüfen (passt) und das Diagramm nicht ausschließen",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2021-ga-A).")

# ---- Stochastik 2: Bonbons
row("2019MgrundlegendAStochastik2", "a", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", typ_neben="",
    stichwoerter="Gewinn mit 0,8 (Zitrone oder Orange), kein Gewinn 0,2|(10 über 7) · 0,8⁷ · 0,2³ = P(genau 7 Gewinne bei 10 Spielen)",
    voraussetzungen="0,8 als Wahrscheinlichkeit eines Gewinns erkennen|Bernoulli-Formel lesen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="Spiel/Bonbons", textumfang="mittel",
    gegeben="Spiel mit P(Zitronenbonbon) = 30 %, P(Orangenbonbon) = 50 %, P(kein Gewinn) = 20 %; zehnmalige Teilnahme; Term (10 über 7) · 0,8⁷ · 0,2³",
    gesucht="ein Ereignis, dessen Wahrscheinlichkeit der Term angibt",
    verfahren="0,8 als Gewinnwahrscheinlichkeit deuten, Bernoulli-Term lesen",
    schritte="1", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="„Die Person gewinnt sieben Bonbons.“ (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="0,8 als Wahrscheinlichkeit für „kein Zitronenbonbon“ deuten (0,7 wäre richtig)",
    bemerkung="Standardbezug: K1 II, K3 II, K6 I. Amtlich. Typ wiederverwendet; 0,8 muss erst als Summe 0,3 + 0,5 erkannt werden.")

row("2019MgrundlegendAStochastik2", "b", seite="1", punkte="4", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Anzahl einer Sorte aus der Wahrscheinlichkeit für zwei verschiedene Sorten bestimmen", typ_neben="",
    stichwoerter="k Orangen-, 6 − k Zitronenbonbons|P(Z, O) + P(O, Z) = (6 − k)/6 · k/5 + k/6 · (6 − k)/5 = 3/5|k² − 6k + 9 = 0 ⇔ (k − 3)² = 0 ⇔ k = 3",
    voraussetzungen="Variable für die Anzahl|zwei Pfade ohne Zurücklegen|quadratische Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Spiel/Bonbons", textumfang="mittel",
    gegeben="Person mit sechs gewonnenen Bonbons (Zitrone oder Orange); zwei zufällig ausgewählt und verschenkt; P(ein Zitronen- und ein Orangenbonbon) = 3/5",
    gesucht="Anzahl der gewonnenen Orangenbonbons",
    verfahren="Wahrscheinlichkeit in k aufstellen, Gleichung lösen",
    schritte="3", zahlenraum="Bruch|ganz", einheiten="", abhaengig_von="",
    ergebnis="(6 − k)/6 · k/5 + k/6 · (6 − k)/5 = 3/5 ⇔ 6k − k² + 6k − k² = 18 ⇔ k² − 6k + 9 = 0 ⇔ (k − 3)² = 0 ⇔ k = 3 (amtlich)",
    zwischenergebnis="drei Orangen-, drei Zitronenbonbons",
    niveau_geschaetzt="III",
    fehlerquelle="nur einen Pfad ansetzen (dann keine ganzzahlige Lösung)",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) die Sachbedingung mit unbekannter Anzahl in eine Gleichung übersetzen (zwei Pfade ohne Zurücklegen), verkettet mit einer quadratischen Gleichung.")


# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("Schnittstellen zweier Graphen durch Lösen einer quadratischen Gleichung nachweisen", "Analysis", "Gleichungen lösen",
     "Zeigen, dass zwei Graphen genau die genannten Schnittstellen haben, indem die Gleichsetzung auf eine "
     "quadratische Gleichung führt (höchstens zwei Lösungen, Werte einsetzen oder lösen).",
     "2019MgrundlegendAAnalysis11-a"),
    ("Stellen mit vorgegebenem Funktionswert durch Ausklammern berechnen", "Analysis", "Gleichungen lösen",
     "Die Stellen bestimmen, an denen eine ganzrationale Funktion einen vorgegebenen Wert annimmt "
     "(Gleichung f(x) = c, Ausklammern, Satz vom Nullprodukt).",
     "2019MgrundlegendAAnalysis12-a"),
    ("Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die kleinste (oder größte) Steigung aller Tangenten an einen Graphen bestimmen, indem die Ableitung "
     "als Funktion untersucht und ihr Extremwert ermittelt wird.",
     "2019MgrundlegendAAnalysis12-b"),
    ("Gleichschenkligkeit des Dreiecks aus Tangente und Koordinatenachsen allgemein begründen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Für alle Tangenten einer beschriebenen Familie begründen, dass das mit den Koordinatenachsen gebildete "
     "Dreieck gleichschenklig ist (Steigung ±1 nachweisen, gleiche Achsenabschnitte folgern).",
     "2019MgrundlegendAAnalysis2-b"),
    ("Übergangsprozess: Übergangsgleichung mit Matrix aus dem Diagramm aufstellen und Variablen deuten", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Zu einem Übergangsdiagramm die Gleichung v_{n+1} = M · v_n mit der Übergangsmatrix aufstellen und die "
     "Bedeutung aller Variablen im Sachzusammenhang angeben.",
     "2019MgrundlegendAAGLAA11-a"),
    ("Übergangsprozess: Anteil nach zwei Übergängen aus dem Diagramm berechnen", "Analytische Geometrie",
     "Matrizen und Übergangsprozesse",
     "Den Anteil in einem Zustand nach zwei Schritten aus einer Startverteilung berechnen (Pfade im "
     "Übergangsdiagramm addieren oder M² anwenden).",
     "2019MgrundlegendAAGLAA11-b"),
    ("Matrizenalgebra: Quadrat einer Matrix mit Parameter berechnen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Das Produkt M · M für eine Matrix mit einem Parameter in den Einträgen ausrechnen und angeben.",
     "2019MgrundlegendAAGLAA12-a"),
    ("Übergangsprozess: Langfristige Entwicklung aus M³ als Vielfachem der Einheitsmatrix durch Fallunterscheidung beschreiben",
     "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Eine Gleichung M^n = c · E im Sachzusammenhang deuten (alle Anzahlen ändern sich je n Schritte mit dem "
     "Faktor c) und die langfristige Entwicklung nach dem Parameter unterscheiden (c < 1, c = 1, c > 1).",
     "2019MgrundlegendAAGLAA12-b"),
    ("Untere Schranke für den Abstand zweier Punkte mit einer unbekannten Koordinate nachweisen", "Analytische Geometrie", "Abstände",
     "Zeigen, dass der Abstand zweier Punkte, von denen einer eine unbekannte Koordinate hat, einen Wert nicht "
     "unterschreitet (Abstandsterm aufstellen, nichtnegatives Quadrat abschätzen).",
     "2019MgrundlegendAAGLAA211-b"),
    ("Dreieck: Nichtrechtwinkligkeit in einem Eckpunkt über das Skalarprodukt nachweisen", "Analytische Geometrie", "Orthogonalität",
     "Zeigen, dass ein Dreieck in einem Eckpunkt keinen rechten Winkel hat, indem das Skalarprodukt der "
     "Schenkelvektoren als ungleich null nachgewiesen wird.",
     "2019MgrundlegendAAGLAA212-a"),
    ("Körper: Höhe eines Prismas aus dem Mantelflächeninhalt bestimmen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Die Höhe eines geraden Prismas aus dem Inhalt der Mantelfläche bestimmen (Seitenlängen der Grundfläche "
     "über Beträge, Mantel gleich Umfang mal Höhe).",
     "2019MgrundlegendAAGLAA212-b"),
    ("Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen", "Analytische Geometrie", "Geraden",
     "Einen Punkt der Geraden bestimmen, der vom Aufpunkt einen vorgegebenen Abstand hat (Betrag des "
     "Richtungsvektors, passendes Vielfaches ansetzen).",
     "2019MgrundlegendAAGLAA22-a"),
    ("Punkte mit gleichem Abstand zu drei Eckpunkten eines rechtwinkligen Dreiecks über den Thaleskreis ermitteln",
     "Analytische Geometrie", "Abstände",
     "Punkte mit gleichem Abstand zu drei gegebenen Punkten ermitteln, wenn diese ein rechtwinkliges Dreieck "
     "bilden (Mittelpunkt der Hypotenuse als Umkreismittelpunkt, weitere Punkte auf dem Lot zur Dreiecksebene).",
     "2019MgrundlegendAAGLAA22-b"),
    ("Wahrscheinlichkeit für höchstens einmal bei zwei Zügen über das Gegenereignis berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Bei zwei Zügen mit Zurücklegen die Wahrscheinlichkeit dafür berechnen, dass ein Merkmal höchstens einmal "
     "auftritt (1 minus Wahrscheinlichkeit für zweimal).",
     "2019MgrundlegendAStochastik12-a"),
    ("Ziehen ohne Zurücklegen: Anzahl einer Sorte aus der Wahrscheinlichkeit für zwei verschiedene Sorten bestimmen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die unbekannte Anzahl einer Sorte in einer kleinen Gesamtheit aus der vorgegebenen Wahrscheinlichkeit "
     "bestimmen, beim zweimaligen Ziehen ohne Zurücklegen je eines von zwei Sorten zu erhalten (zwei Pfade, "
     "quadratische Gleichung).",
     "2019MgrundlegendAStochastik2-b"),
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
    ist die Aufgabe ungegliedert (Kennung, '', '')."""
    m = re.fullmatch(r"(" + KENNUNG.pattern + r")(?:-(\d*)([a-z]))?", i)
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
        a(not re.search(r"(?<=[\d\s(])-(?=\d)", v),
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
        amt = hoechster_afb(z["afb_amtlich"])
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
        stapel = {QUELLE[k]["stapel"] for k in kennungen if k in QUELLE}
        for s in sorted(stapel):
            fehlt = [k for k, q in QUELLE.items()
                     if q["stapel"] == s and not q["dublette_von"] and k not in kennungen]
            a(not fehlt, f"Stapel {s} im Bestand unvollständig, es fehlen {fehlt}")
        je_datei = {}
        for z in alt:
            je_datei.setdefault(kennung_aus_id(z["id"])[0], []).append(z["teilaufgabe"])
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
    im_stapel = {k for k, q in QUELLE.items() if q["stapel"] == stapel}
    dubletten = {k for k in im_stapel if QUELLE[k]["dublette_von"]}
    a(im_stapel, f"Stapel {stapel} unbekannt in {QUELLEN}")
    dateien = {z["_kennung"] for z in ZEILEN}
    for k in sorted(dateien - im_stapel):
        a(False, f"{k}: gehört nicht zum Stapel {stapel}")
    je_datei = {}
    for z in ZEILEN:
        je_datei.setdefault(z["_kennung"], []).append(z["teilaufgabe"])
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
