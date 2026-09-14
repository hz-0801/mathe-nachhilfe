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
    "stapel": "2026-ga-B-mms",
    # Sollpunkte je Datei aus der BE-Summe am Ende von Abschnitt 1 Aufgabe.
    # Dubletten (Spalte dublette_von in iqb-quellen.csv) bekommen keine Zeile
    # und kein Soll.
    "soll": {
        "2026MgrundlegendBAnalysisMMS1": 25,
        "2026MgrundlegendBAnalysisMMS2": 25,
        "2026MgrundlegendBAGLAA1MMS": 15,
        "2026MgrundlegendBAGLAA2MMS1": 15,
        "2026MgrundlegendBAGLAA2MMS2": 15,
        "2026MgrundlegendBStochastikMMS1": 15,
        "2026MgrundlegendBStochastikMMS2": 15,
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
# Stapel 2026-ga-B, MMS-Zweig (Delta gegen den WTR-Zwilling). innen = Aufgabennummer in der Datei (unnummerierte Einzelaufgabe: 1).
# Pool 2026 grundlegend: Analysis 25 BE, AG/LA und Stochastik 15 BE. Drei der sieben Dateien sind wortgleich mit dem WTR-Zwilling
# (AG/LA A2 MMS 1, Stochastik MMS 1 und 2); ihre Zeilen sind aus dem WTR-Zweig übernommen (Vermerk in bemerkung).
# bemerkung trägt je Zeile „MMS-Anteil: …" (rein Rechnerbedienung | Rechner für die Lösung, Ansatz eigen | keiner).

SOLL = {"2026MgrundlegendBAnalysisMMS1": 25, "2026MgrundlegendBAnalysisMMS2": 25,
        "2026MgrundlegendBAGLAA1MMS": 15, "2026MgrundlegendBAGLAA2MMS1": 15, "2026MgrundlegendBAGLAA2MMS2": 15,
        "2026MgrundlegendBStochastikMMS1": 15, "2026MgrundlegendBStochastikMMS2": 15}

# ---- Analysis MMS 1, Aufgabe 1: Kupfererz k(x) = 80e^1,5 − (4x + 80)e^(−0,05x + 1,5)
KA = "Abbildung 1: Koordinatensystem mit Kästchenraster, x von 0 bis 22 (Jahre), y von 0 bis 6 (Mio. t/Jahr); Graph von k' steigt von (0 | 0) rechtsgekrümmt bis etwa (20 | 6,6) und verläuft dort flach"
row("2026MgrundlegendBAnalysisMMS1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen", typ_neben="Zeitpunkt für einen vorgegebenen Bestand aus der Funktionsgleichung mit dem Rechner ermitteln",
    stichwoerter="k(8) ≈ 22|k(x) = 100 numerisch: x ≈ 20,8|etwa 21 Jahre",
    voraussetzungen="Funktionswert mit dem Rechner|Gleichung numerisch lösen",
    format="Rechnung", operator="Zeigen Sie|Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bergbau/Kupfererz", textumfang="mittel",
    gegeben="k(x) = 80e^1,5 − (4x + 80) · e^(−0,05x + 1,5) für x ≥ 0, x Zeit in Jahren, k(x) Gesamtmenge in Millionen Tonnen",
    gesucht="Nachweis k(8) ≈ 22; Zeitpunkt mit k(x) = 100",
    verfahren="Funktionswert berechnen, Gleichung k(x) = 100 mit dem Rechner lösen",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="Mio. t|Jahre", abhaengig_von="",
    ergebnis="k(8) ≈ 22; k(x) = 100 liefert x ≈ 20,8, Zeitpunkt etwa 21 Jahre nach Beginn des Abbaus (amtlich)",
    zwischenergebnis="k(8) ≈ 22,07", niveau_geschaetzt="I",
    fehlerquelle="Ergebnis 20,8 nicht als Zeitpunkt mit Einheit angeben",
    bemerkung="Standardbezug: K2 I, K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: rein Rechnerbedienung (Term eingeben, Gleichung numerisch lösen). Typ wiederverwendet (2026-ga-B).")

row("2026MgrundlegendBAnalysisMMS1", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Gleichung für die mittlere Änderungsrate lösen und Lösung im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="(k(c) − k(0))/c = 1,9|kleinere Lösung c ≈ 5|durchschnittlich 1,9 Mio. t pro Jahr bis etwa Ende des fünften Jahres",
    voraussetzungen="Differenzenquotient als mittlere Änderungsrate|Gleichung numerisch lösen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Deuten Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bergbau/Kupfererz", textumfang="mittel",
    gegeben="Gleichung (k(c) − k(0))/c = 1,9 mit c ∈ IR hat genau zwei Lösungen",
    gesucht="kleinere Lösung; Deutung von Gleichung und Lösung",
    verfahren="Gleichung mit dem Rechner lösen, linke Seite als mittlere Abbaurate über [0; c] deuten",
    schritte="2", zahlenraum="dezimal", einheiten="Mio. t/Jahr|Jahre", abhaengig_von="",
    ergebnis="c ≈ 5; im Zeitraum bis etwa zum Ende des fünften Jahres werden durchschnittlich 1,9 Millionen Tonnen Kupfererz pro Jahr abgebaut (amtlich)",
    zwischenergebnis="zweite Lösung c ≈ 188,5", niveau_geschaetzt="II",
    fehlerquelle="Quotient als momentane Abbaurate deuten",
    bemerkung="Standardbezug: K3 II, K4 I, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: Rechner für die Lösung, Deutung eigen.")

row("2026MgrundlegendBAnalysisMMS1", "c", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Zeitpunkt und Größe der maximalen Änderungsrate über die zweite Ableitung berechnen", typ_neben="",
    stichwoerter="k''(x) = 0 ⇔ x = 20|k'(20) ≈ 6,6",
    voraussetzungen="Maximum der Rate als Wendestelle von k|Ableitungen mit dem Rechner",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=KA, kontext="Bergbau/Kupfererz", textumfang="mittel",
    gegeben="k' momentane Abbaurate in Mio. t/Jahr; Graph von k' in Abbildung 1",
    gesucht="Zeitpunkt der größten Abbaurate und größter Wert",
    verfahren="Nullstelle von k'' berechnen, k' dort auswerten",
    schritte="2", zahlenraum="dezimal", einheiten="Jahre|Mio. t/Jahr", abhaengig_von="",
    ergebnis="k''(x) = 0 ⇔ x = 20; Zeitpunkt 20 Jahre ab Beginn des Abbaus, größter Wert der momentanen Abbaurate etwa 6,6 Millionen Tonnen pro Jahr (amtlich)",
    zwischenergebnis="k'(20) ≈ 6,59", niveau_geschaetzt="I",
    fehlerquelle="k'(x) = 0 statt k''(x) = 0",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: Rechner für Ableitung und Lösung, Ansatz eigen. Kein Rückgriff auf „Zeitpunkt der größten Rate aus der Ableitung angeben“ (dort Nullstelle einer gegebenen Ableitung, hier zweite Ableitung selbst bilden).")

row("2026MgrundlegendBAnalysisMMS1", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Länge des Zeitraums mit Mindeständerungsrate über die Lösungen von f'(x) = c berechnen", typ_neben="",
    stichwoerter="k'(x) = 5 ⇔ x₁ ≈ 8,6, x₂ ≈ 38,8|x₂ − x₁ ≈ 30,2|etwa 30 Jahre",
    voraussetzungen="Rate als Ableitung|Gleichung numerisch lösen|Differenz der Lösungen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=KA, kontext="Bergbau/Kupfererz", textumfang="kurz",
    gegeben="k' wie in c; Schranke fünf Millionen Tonnen pro Jahr",
    gesucht="Länge des Zeitraums mit k'(x) ≥ 5, rechnerisch",
    verfahren="Gleichung k'(x) = 5 mit dem Rechner lösen, Differenz der beiden Lösungen",
    schritte="2", zahlenraum="dezimal", einheiten="Jahre", abhaengig_von="",
    ergebnis="k'(x) = 5 ⇔ x = x₁ ∨ x = x₂ mit x₁ ≈ 8,6 und x₂ ≈ 38,8; x₂ − x₁ ≈ 30,2, Länge des Zeitraums etwa 30 Jahre (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur die erste Lösung, Zeitraum bis 20 Jahre aus der Abbildung",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: Rechner für die Lösung, Ansatz eigen (zweite Lösung außerhalb der Abbildung).")

row("2026MgrundlegendBAnalysisMMS1", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Größten jährlichen Zuwachs einer Rate über die Rechtskrümmung des Graphen begründen", typ_neben="",
    stichwoerter="Graph von k' rechtsgekrümmt|Zuwachs im ersten Jahr etwa 0,9 ist der größte|kein Jahr mit Zuwachs 1",
    voraussetzungen="Krümmung am Graphen erkennen|Zuwachs über ein Jahr als Differenz von Funktionswerten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=KA, kontext="Bergbau/Kupfererz", textumfang="mittel",
    gegeben="Graph von k' in Abbildung 1; Aussage: in den ersten 20 Jahren gibt es keinen Zeitpunkt, ab dem die Abbaurate innerhalb eines Jahres um eine Million Tonnen pro Jahr zunimmt",
    gesucht="Begründung am Graphen, dass die Aussage wahr ist",
    verfahren="Rechtskrümmung ⇒ jährliche Zuwächse fallen; größter Zuwachs im ersten Jahr ablesen und mit 1 vergleichen",
    schritte="2", zahlenraum="dezimal", einheiten="Mio. t/Jahr", abhaengig_von="",
    ergebnis="Der Graph von k' ist im abgebildeten Bereich rechtsgekrümmt; damit ist der Zuwachs der momentanen Abbaurate im ersten Jahr mit etwa 0,9 Millionen Tonnen pro Jahr der größte jährliche Zuwachs im betrachteten Zeitraum (amtlich)",
    zwischenergebnis="k'(1) − k'(0) ≈ 0,85", niveau_geschaetzt="II",
    fehlerquelle="Steigung k'' statt Zuwachs über ein Jahr betrachten",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner.")

# ---- Analysis MMS 1, Aufgabe 2: f(x) = e^(−x+2) − 1, h(x) = −2x − 2
FH = "Abbildung 2: Koordinatensystem x von −3 bis 5, y von −5 bis 7; Graph G_f fallende e-Kurve von links oben durch (0 | e² − 1) und (2 | 0), nähert sich −1; Gerade G_h mit Steigung −2 durch (−1 | 0) und (0 | −2)"
row("2026MgrundlegendBAnalysisMMS1", "a", innen="2", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Schnittpunkt mit der y-Achse und Steigung des Graphen dort angeben", typ_neben="",
    stichwoerter="f(0) = e² − 1|f'(0) = −e²",
    voraussetzungen="Funktionswert an der Stelle 0|Ableitung der e-Funktion mit Kettenregel",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=FH, kontext="ohne", textumfang="kurz",
    gegeben="f(x) = e^(−x+2) − 1 und h(x) = −2x − 2 in IR; Graphen in Abbildung 2",
    gesucht="Schnittpunkt von G_f mit der y-Achse und Steigung dort",
    verfahren="x = 0 einsetzen, Ableitung an der Stelle 0",
    schritte="2", zahlenraum="Potenz|negativ", einheiten="", abhaengig_von="",
    ergebnis="(0 | e² − 1); Steigung −e² (amtlich)",
    zwischenergebnis="≈ (0 | 6,39), Steigung ≈ −7,39", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen der inneren Ableitung",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner (auch mit Rechner lösbar).")

row("2026MgrundlegendBAnalysisMMS1", "b", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Ergebnis eines Lösungswegs als y-Achsenabschnitt der parallelen Tangente deuten", typ_neben="",
    stichwoerter="f'(x) = h'(x) ⇔ x = 2 − ln 2|y = −2x + n durch (2 − ln 2 | 1)|n = 5 − 2 ln 2 als y-Achsenabschnitt der zu G_h parallelen Tangente",
    voraussetzungen="Parallele Tangente über gleiche Steigung|Geradengleichung y = mx + n",
    format="Begründung", operator="Interpretieren Sie", antwort="Text",
    material="Koordinatensystem", skizze=FH, kontext="ohne", textumfang="mittel",
    gegeben="Lösungsschritte: f'(x) = h'(x) ⇔ x = 2 − ln 2; mit y = −2x + n und f(2 − ln 2) = 1 ergibt sich n = 5 − 2 · ln 2",
    gesucht="geometrische Bedeutung von n = 5 − 2 ln 2",
    verfahren="Schritte als Aufstellen der zu G_h parallelen Tangente erkennen, n als y-Achsenabschnitt deuten",
    schritte="1", zahlenraum="Potenz", einheiten="", abhaengig_von="",
    ergebnis="Die zu G_h parallele Tangente an G_f schneidet die y-Achse im Punkt (0 | n) (amtlich)",
    zwischenergebnis="n ≈ 3,61", niveau_geschaetzt="II",
    fehlerquelle="n als Schnittpunkt von G_f und G_h deuten",
    bemerkung="Standardbezug: K1 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner.")

row("2026MgrundlegendBAnalysisMMS1", "c", innen="2", seite="2", punkte="5", afb_amtlich="III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Parallele Gerade zur Halbierung einer Fläche über ein Achsendreieck bestimmen", typ_neben="",
    stichwoerter="g: y = −2x + a, a > 0|Dreieck unter g: 1/2 · a/2 · a = a²/4|∫₀² f(x) dx = e² − 3|a = √(2e² − 6)",
    voraussetzungen="Fläche zwischen Graph und Achsen als Integral|Dreiecksfläche aus Achsenabschnitten|Gleichung nach a auflösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Koordinatensystem", skizze=FH, kontext="ohne", textumfang="kurz",
    gegeben="G_f schließt mit den Koordinatenachsen eine Fläche ein; g parallel zu G_h halbiert diese Fläche",
    gesucht="Gleichung von g",
    verfahren="Ansatz y = −2x + a, Dreieck zwischen g und den Achsen gleich der halben Fläche unter G_f setzen",
    schritte="4", zahlenraum="Potenz|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="g: y = −2x + a mit a ∈ IR⁺; g schneidet die x-Achse bei a/2; 1/2 · a/2 · a = 1/2 · ∫₀² f(x) dx ⇔ a = √(2e² − 6) (amtlich)",
    zwischenergebnis="a ≈ 2,96", niveau_geschaetzt="III",
    fehlerquelle="Dreieck oberhalb von g statt unterhalb, oder Fläche unter G_f bis 2 statt bis zur Nullstelle",
    bemerkung="Standardbezug: K2 III, K4 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Halbierungsbedingung in eine Gleichung für a übersetzen, verkettet mit der Dreiecksgeometrie. MMS-Anteil: Rechner für Integral und Gleichung, Ansatz eigen. Kein Rückgriff auf „Fläche: Senkrechte Gerade zur Halbierung …“ (anderer Lösungsweg: Dreieck statt Integral mit variabler Grenze).")

# ---- Analysis MMS 2: f(x) = 3/16(x³ + 2x² − 4x − 8), Dachrinne
DR = "Abbildung: Koordinatensystem x von −2 bis 2, y von −2 bis 0; Profillinie (Graph G) von (−2 | 0) fallend über (0 | −1,5) zum Tiefpunkt (2/3 | −1,78), steigend nach (2 | 0); darunter parallel die Außenlinie des Blechs (Dicke 0,7 mm)"
row("2026MgrundlegendBAnalysisMMS2", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstellen berechnen und Grenzverhalten einer ganzrationalen Funktion angeben", typ_neben="",
    stichwoerter="f(x) = 0 ⇔ x ∈ {−2; 2}|(x + 2)²(x − 2)|x → −∞: f(x) → −∞",
    voraussetzungen="Nullstellen einer kubischen Funktion mit dem Rechner|Grenzverhalten über den führenden Term",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = 3/16 · (x³ + 2x² − 4x − 8) in IR, Graph G",
    gesucht="Nullstellen; Verhalten für x → −∞",
    verfahren="Gleichung lösen (Rechner oder Faktorisierung), Grad und Leitkoeffizient betrachten",
    schritte="2", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="f(x) = 0 ⇔ x ∈ {−2; 2}; f(x) → −∞ für x → −∞ (amtlich)",
    zwischenergebnis="doppelte Nullstelle −2", niveau_geschaetzt="I",
    fehlerquelle="Grenzverhalten mit dem Vorzeichen des konstanten Glieds begründen",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: Rechner für die Nullstellen, Grenzverhalten eigen.")

row("2026MgrundlegendBAnalysisMMS2", "b", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Extrempunkte: Existenz eines Hochpunkts aus dem Grad und einem Tiefpunkt begründen und Koordinaten angeben", typ_neben="",
    stichwoerter="ganzrational dritten Grades: kein oder zwei Extrempunkte|Tiefpunkt vorhanden ⇒ Hochpunkt|Hochpunkt (−2 | 0)",
    voraussetzungen="Anzahl der Extrempunkte bei Grad 3|Hochpunkt an der doppelten Nullstelle",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f wie in a; Tiefpunkt von G bei x = 2/3",
    gesucht="Begründung eines Hochpunkts; seine Koordinaten",
    verfahren="Über den Grad argumentieren, Hochpunkt aus f' = 0 oder aus der doppelten Nullstelle",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2026MgrundlegendBAnalysisMMS2-1a",
    ergebnis="Da f ganzrational dritten Grades ist, hat der Graph keinen oder zwei Extrempunkte; da ein Tiefpunkt vorliegt, ist der andere Extrempunkt ein Hochpunkt; (−2 | 0) (amtlich)",
    zwischenergebnis="f'(x) = 3/16(3x² + 4x − 4), Nullstellen −2 und 2/3", niveau_geschaetzt="II",
    fehlerquelle="Hochpunkt nur berechnen, Existenz nicht begründen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Abweichung: meine Schätzung II (Existenzargument über den Grad), amtlich I. MMS-Anteil: Rechner für f' = 0, Begründung eigen.")

row("2026MgrundlegendBAnalysisMMS2", "c", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Wendestelle nachweisen und Winkel der Wendetangente mit der x-Achse über die Steigung −1 zeigen", typ_neben="",
    stichwoerter="f''(−2/3) = 0|f'(−2/3) = −1 ⇒ 45°",
    voraussetzungen="Wendestelle über f'' = 0|tan 45° = 1",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="G hat genau einen Wendepunkt; Behauptung: Wendestelle −2/3, Wendetangente schließt mit der x-Achse 45° ein",
    gesucht="Nachweis beider Aussagen",
    verfahren="Zweite Ableitung an der Stelle −2/3 null, erste Ableitung dort −1",
    schritte="2", zahlenraum="Bruch|negativ", einheiten="°", abhaengig_von="",
    ergebnis="f''(−2/3) = 0; f'(−2/3) = −1 (amtlich)",
    zwischenergebnis="f''(x) = 3/16(6x + 4)", niveau_geschaetzt="I",
    fehlerquelle="Steigung −1 nicht mit 45° in Verbindung bringen",
    bemerkung="Standardbezug: K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: Rechner für die Ableitungen, Ansatz eigen.")

row("2026MgrundlegendBAnalysisMMS2", "d", innen="1", seite="1", punkte="2", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt der Tangente mit vorgegebener Steigung berechnen", typ_neben="",
    stichwoerter="45° ⇒ f'(x) = 1|x = (−2 ± 4√2)/3",
    voraussetzungen="Winkel 45° als Steigung ±1|quadratische Gleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f wie in a; neben dem Wendepunkt zwei weitere Punkte mit Tangentenwinkel 45°",
    gesucht="x-Koordinaten dieser beiden Punkte",
    verfahren="f'(x) = 1 lösen",
    schritte="2", zahlenraum="Wurzel|Bruch|negativ", einheiten="", abhaengig_von="2026MgrundlegendBAnalysisMMS2-1c",
    ergebnis="f'(x) = 1 ⇔ x ∈ {(−2 + 4√2)/3; (−2 − 4√2)/3} (amtlich)",
    zwischenergebnis="≈ 1,22 und ≈ −2,55", niveau_geschaetzt="II",
    fehlerquelle="nur f'(x) = 1, nicht auch −1 bedenken (hier liefert −1 nur die Wendestelle)",
    bemerkung="Standardbezug: K2 II, K4 II, K5 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: Rechner für die Gleichung, Ansatz eigen. Typ wiederverwendet (2026-ea-B).")

row("2026MgrundlegendBAnalysisMMS2", "e", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Passung eines Profils in einen Karton über Breite und Tiefe aus Nullstellen und Tiefpunkt prüfen", typ_neben="",
    stichwoerter="Breite 4 LE · 5 cm = 20 cm ≤ 21 cm|Tiefe |f(2/3)| · 5 ≈ 8,9 cm ≤ 9,5 cm|Karton geeignet",
    voraussetzungen="Maßstab 1 LE = 5 cm|Breite aus Nullstellen, Tiefe aus Tiefpunkt|Blechdicke vernachlässigbar klein",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=DR, kontext="Dachrinne/Verpackung", textumfang="mittel",
    gegeben="Dachrinne 3 m lang, Blech 0,7 mm; Profillinie der Innenseite für −2 ≤ x ≤ 2 durch G, 1 LE = 5 cm; Karton innen 21 cm × 9,5 cm",
    gesucht="ob der Karton als Verpackung geeignet ist",
    verfahren="Breite und Tiefe der Rinne in cm berechnen und mit den Kartonmaßen vergleichen",
    schritte="3", zahlenraum="dezimal", einheiten="cm", abhaengig_von="2026MgrundlegendBAnalysisMMS2-1a",
    ergebnis="4 · 5 = 20; |f(2/3)| · 5 ≈ 8,9; somit ist der Karton für das Stück der Dachrinne aus dem 0,7 mm dicken Blech geeignet (amtlich)",
    zwischenergebnis="f(2/3) = −16/9", niveau_geschaetzt="II",
    fehlerquelle="Maßstab vergessen oder Tiefe an der Stelle 0 statt am Tiefpunkt",
    bemerkung="Standardbezug: K1 I, K2 II, K3 II, K4 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner.")

row("2026MgrundlegendBAnalysisMMS2", "f", innen="1", seite="2", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Aufgabenstellung zu einem Volumen aus Fläche zwischen Graph und Gerade und Maßstab formulieren und erläutern", typ_neben="",
    stichwoerter="f(x) = −1 ⇔ x₁ ≈ −3,03, x₂ ≈ −0,56, x₃ ≈ 1,59|∫ von x₂ bis x₃ (−1 − f(x)) dx ≈ 1,09|1,09 · 5² · 300 = 8175 cm³|Wasservolumen bei 5 cm fehlender Höhe",
    voraussetzungen="Fläche zwischen Graph und Gerade als Integral|Umrechnungsfaktor 5² für Flächen|Volumen als Fläche mal Länge",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Erläutern Sie", antwort="Text",
    material="Koordinatensystem", skizze=DR, kontext="Dachrinne/Verpackung", textumfang="lang",
    gegeben="Rechenschritte: f(x) = −1 ⇔ x = x₁ ∨ x₂ ∨ x₃ (≈ −3,03; −0,56; 1,59); ∫ von x₂ bis x₃ (−1 − f(x)) dx ≈ 1,09; 1,09 · 5² · 300 = 8175; also etwa 8175 cm³",
    gesucht="passende Aufgabenstellung; Erläuterung des Lösungswegs",
    verfahren="y = −1 als Wasserstand 5 cm unter dem Rand deuten, Integral als Querschnittsfläche, Faktor 25 und Länge 300 cm",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="cm³", abhaengig_von="",
    ergebnis="Aufgabenstellung: Berechnen Sie das Volumen des Wassers im betrachteten Stück der Dachrinne, wenn bis zur vollständigen Befüllung noch 5 cm an Höhe fehlen; Erläuterung: Schnittstellen von G mit y = −1 berechnen, Fläche zwischen G und dieser Geraden berechnen, mit dem Umrechnungsfaktor beim Flächeninhalt das Volumen berechnen (amtlich)",
    zwischenergebnis="Fläche ≈ 1,086", niveau_geschaetzt="II",
    fehlerquelle="Faktor 5² als 5 lesen; x₁ außerhalb der Rinne mitverwenden",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner (Lösungsweg vorgegeben).")

row("2026MgrundlegendBAnalysisMMS2", "g", innen="1", seite="2", punkte="6", afb_amtlich="III",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Radius eines flächengleichen Halbkreisprofils aus einem Integral bestimmen und Materialmasse berechnen", typ_neben="",
    stichwoerter="5² · |∫₋₂² f(x) dx| = πr²/2 ⇒ r = 10√(2/π)|Blechfläche 1/2π((r + 0,07)² − r²)|Masse ≈ 4737 g",
    voraussetzungen="Querschnittsfläche als Integral|Halbkreisfläche|Kreisringhälfte für das Blech|Masse aus Volumen und Dichte",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=DR, kontext="Dachrinne/Verpackung", textumfang="lang",
    gegeben="zweite Dachrinne: gleiche Länge 3 m, gleiche Blechdicke 0,07 cm, gleiches maximales Wasservolumen, Innenprofil Halbkreis; Dichte 8,96 g/cm³",
    gesucht="Masse des Stücks der zweiten Dachrinne",
    verfahren="Innenradius aus der Flächengleichheit mit dem Integral über f, Blechquerschnitt als halber Kreisring, mal Länge mal Dichte",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="cm|g", abhaengig_von="",
    ergebnis="Radius r innen in cm: 5² · |∫₋₂² f(x) dx| = πr²/2 ⇒ r = 10√(2/π); Masse in Gramm: 1/2 · π · ((r + 0,07)² − r²) · 300 · 8,96 ≈ 4737 (amtlich)",
    zwischenergebnis="Integral −4, Querschnitt 100 cm², r ≈ 7,98 cm", niveau_geschaetzt="III",
    fehlerquelle="Blech als Vollhalbkreis statt als Ring rechnen",
    bemerkung="Standardbezug: K2 III, K3 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Flächengleichheit übersetzen, verkettet mit Ring, Länge und Dichte. MMS-Anteil: Rechner für das Integral, Ansatz eigen.")

# ---- AG/LA A1 MMS: Kundenverteilung, P = (0,6 0 0 | 0,3 0,6 0,2 | 0,1 0,4 0,8)
row("2026MgrundlegendBAGLAA1MMS", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Übergangsdiagramm aus der Übergangstabelle zeichnen", typ_neben="",
    stichwoerter="Spalten von P als Abgänge|Schleifen 0,6, 0,6, 0,8|A → B 0,3, A → C 0,1, B → C 0,4, C → B 0,2",
    voraussetzungen="Spaltenkonvention der Übergangsmatrix lesen",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins", skizze="keine; Erwartungshorizont: Diagramm mit Knoten A, B, C, Schleifen 0,6 an A und B, 0,8 an C, Pfeile A → B 0,3, A → C 0,1, B → C 0,4, C → B 0,2", kontext="Kunden/Dienstleister", textumfang="lang",
    gegeben="6000 Kunden in Gruppen A, B, C; v_{n+1} = P · v_n mit P = ((0,6; 0; 0), (0,3; 0,6; 0,2), (0,1; 0,4; 0,8)) (zeilenweise)",
    gesucht="Übergangsdiagramm",
    verfahren="Einträge p_ij als Übergang von Spalte j nach Zeile i als Pfeile zeichnen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="Diagramm mit Schleifen 0,6 (A), 0,6 (B), 0,8 (C) und Pfeilen A → B 0,3, A → C 0,1, B → C 0,4, C → B 0,2 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Zeilen und Spalten vertauscht",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich. Typ wiederverwendet (Teil A), Definition deckt die Matrix als Quelle. MMS-Anteil: keiner. Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MgrundlegendBAGLAA1MMS", "b", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Matrizenalgebra: Matrix-Vektor-Produkt berechnen", typ_neben="",
    stichwoerter="C: 6000 − 2500 − 1900 = 1600|P · (2500; 1900; 1600) = (1500; 2210; 2290)",
    voraussetzungen="Restgruppe aus der Gesamtzahl|Matrix-Vektor-Produkt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kunden/Dienstleister", textumfang="kurz",
    gegeben="P wie in a; Ende eines Jahres 2500 in A, 1900 in B, Rest in C",
    gesucht="Kundenverteilung am Ende des nächsten Jahres",
    verfahren="Restgruppe bilden, Matrix mal Vektor",
    schritte="2", zahlenraum="ganz", einheiten="Kunden", abhaengig_von="",
    ergebnis="P · (2500; 1900; 1600) = (1500; 2210; 2290) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="1600 vergessen und mit Nullvektor-Komponente rechnen",
    bemerkung="Standardbezug: K3 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A). MMS-Anteil: rein Rechnerbedienung (Matrixprodukt). Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MgrundlegendBAGLAA1MMS", "c", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unmöglichkeit einer Verteilung über eine negative Vorgängerkomponente begründen", typ_neben="",
    stichwoerter="P · (a; b; c) = (3204; 2004; 792) lösen|c = −15|negative Anzahl unmöglich",
    voraussetzungen="Lineares Gleichungssystem mit dem Rechner lösen|Anzahlen sind nicht negativ",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Kunden/Dienstleister", textumfang="mittel",
    gegeben="Aussage: am Ende des Jahres nach Beobachtungsbeginn ist (3204; 2004; 792) die Kundenverteilung",
    gesucht="Begründung, dass die Aussage im Modell falsch ist",
    verfahren="Vorgängerverteilung aus P · v₀ = v₁ berechnen, negative Komponente als Widerspruch",
    schritte="2", zahlenraum="ganz|negativ", einheiten="Kunden", abhaengig_von="",
    ergebnis="P · (a; b; c) = (3204; 2004; 792) ⇒ c = −15; der Parameter c kann keinen negativen Wert annehmen (amtlich)",
    zwischenergebnis="a = 5340, b = 675", niveau_geschaetzt="II",
    fehlerquelle="Summe 6000 prüfen und für ausreichend halten",
    bemerkung="Standardbezug: K1 II, K2 II, K3 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: Rechner für das Gleichungssystem, Ansatz und Argument eigen. Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MgrundlegendBAGLAA1MMS", "d", innen="1", seite="2", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Konstante prozentuale Abnahme einer Gruppe ohne Zugänge aus der Matrix begründen", typ_neben="Übergangsprozess: Zeitpunkt für das Unterschreiten eines Anteils der Populationsgröße über einen konstanten Faktor bestimmen",
    stichwoerter="erste Zeile von P: 0,6 bleibt, keine Zugänge aus B, C|Abnahme 40 % je Jahr|0,6ⁿ < 0,02 ⇒ n > 7,7|acht Jahre",
    voraussetzungen="Zeile der Matrix lesen|Exponentialungleichung lösen",
    format="Begründung|Rechnung", operator="Begründen Sie|Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kunden/Dienstleister", textumfang="mittel",
    gegeben="P wie in a; Anzahl in A erstmals unter zwei Prozent des Anfangswerts",
    gesucht="Begründung der Abnahme um 40 %; Anzahl der vergangenen Jahre",
    verfahren="Erste Zeile von P deuten, 0,6ⁿ < 0,02 lösen und aufrunden",
    schritte="3", zahlenraum="dezimal|Prozent|Potenz", einheiten="Jahre", abhaengig_von="",
    ergebnis="Vom Ende eines Jahres zum Ende des nächsten verbleiben 60 % der Kunden in A, und es gibt keine Wechsel aus B bzw. C nach A; 0,6ⁿ < 0,02 ⇒ n > 7,7, acht Jahre sind vergangen (amtlich)",
    zwischenergebnis="n > 7,66", niveau_geschaetzt="II",
    fehlerquelle="n = 7 statt 8 (erstmals unterschritten)",
    bemerkung="Standardbezug: K1 II, K3 II, K4 I, K5 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Zeitpunkt als typ_neben wiederverwendet (2024-ea-B). MMS-Anteil: Rechner für die Ungleichung, Ansatz eigen. Aufgabengruppe A1, außerhalb der Geltung.")

row("2026MgrundlegendBAGLAA1MMS", "e", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Matrizen und Übergangsprozesse",
    typ="Übergangsprozess: Unbekannte der Übergangsmatrix und des Bestands aus einem stationären Vektor bestimmen", typ_neben="",
    stichwoerter="stationär: P' · v = v|v = (6000 − 5b; b; 4b)|Übergangsrate B → C als x, B bleibt 1 − x|x = 0,8",
    voraussetzungen="Stationäre Verteilung als Fixvektor|Spaltensumme eins|Gleichungssystem lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Kunden/Dienstleister", textumfang="lang",
    gegeben="Es gibt eine unveränderliche Verteilung mit viermal so vielen Kunden in C wie in B; Übergangsrate B → C wird angepasst, andere Raten zwischen verschiedenen Gruppen unverändert",
    gesucht="Übergangsrate von B nach C im angepassten Modell",
    verfahren="Angepasste Matrix mit x und 1 − x, Fixvektor (6000 − 5b; b; 4b) ansetzen, Gleichungssystem lösen",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="((0,6; 0; 0), (0,3; 1 − x; 0,2), (0,1; x; 0,8)) · (6000 − 5b; b; 4b) = (6000 − 5b; b; 4b) liefert x = 0,8; die Übergangsrate beträgt 80 % (amtlich)",
    zwischenergebnis="b = 1200", niveau_geschaetzt="III",
    fehlerquelle="Verbleibrate von B nicht auf 1 − x anpassen",
    bemerkung="Standardbezug: K2 III, K3 III, K4 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Stationarität und Verhältnis 4 : 1 in ein Gleichungssystem mit angepasster Matrix übersetzen. Typ wiederverwendet (Lauf 6). MMS-Anteil: Rechner für das Gleichungssystem, Ansatz eigen. Aufgabengruppe A1, außerhalb der Geltung.")

# ---- AG/LA A2 MMS 2: Quader O(0|0|0), A(4|0|0), B(4|4|0), C(0|4|0), D(0|0|5), E(4|0|5), F(4|4|5), G(0|4|5); S(2|2|3)
QU = "Abbildung 1: Schrägbild eines Quaders mit Grundfläche OABC (Quadrat 4 × 4) in der xy-Ebene und Höhe 5 (Deckfläche DEFG); Achsen x, y, z; Abbildung 2: derselbe Quader mit der Pyramide OABCS, Spitze S innen"
row("2026MgrundlegendBAGLAA2MMS2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Vektoren und Rechenoperationen",
    typ="Punkt aus einer Linearkombination von Kantenvektoren in das Schrägbild einzeichnen", typ_neben="",
    stichwoerter="OR = 1/2 OA + 1/2 AB + BF|R(2 | 2 | 5) Mittelpunkt der Deckfläche",
    voraussetzungen="Vektorkette im Körper verfolgen|Punkt im Schrägbild einzeichnen",
    format="Zeichnen", operator="Zeichnen Sie ein", antwort="Grafik",
    material="Körper", skizze=QU, kontext="ohne", textumfang="kurz",
    gegeben="Quader mit O(0|0|0), A(4|0|0), B(4|4|0), G(0|4|5); OABC quadratisch; OR = 1/2 · OA + 1/2 · AB + BF",
    gesucht="Punkt R in Abbildung 1",
    verfahren="Halbe Kanten OA und AB und ganze Kante BF abtragen",
    schritte="1", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="R ist der Mittelpunkt der Deckfläche DEFG, R(2 | 2 | 5) (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="BF als halbe Kante abtragen",
    bemerkung="Standardbezug: K4 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. MMS-Anteil: keiner.")

row("2026MgrundlegendBAGLAA2MMS2", "b", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebene einer Pyramide unter vorgegebenen Gleichungen auswählen und eine ausschließen", typ_neben="",
    stichwoerter="I x + y = 0, II x − y = 0, III z = 2|II ist Symmetrieebene (Diagonalebene)|III schneidet AE nicht im Mittelpunkt (Höhe 5)",
    voraussetzungen="Symmetrieebenen eines Quaders|Kantenmittelpunkt prüfen",
    format="Kurzantwort|Begründung", operator="Entscheiden Sie|Begründen Sie", antwort="Text",
    material="Körper", skizze=QU, kontext="ohne", textumfang="mittel",
    gegeben="genau eine der Gleichungen I x + y = 0, II x − y = 0, III z = 2 beschreibt eine Symmetrieebene des Quaders",
    gesucht="welche; Begründung für eine andere, dass sie keine ist",
    verfahren="Diagonalebene durch O und B erkennen; für III die Kante AE betrachten",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Gleichung II; die zu Gleichung III gehörende Ebene schneidet die Kante AE nicht in deren Mittelpunkt (amtlich)",
    zwischenergebnis="Mittelpunkt von AE bei z = 2,5", niveau_geschaetzt="II",
    fehlerquelle="x + y = 0 mit der Diagonalebene verwechseln",
    bemerkung="Standardbezug: K1 II, K4 I, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2024-ea-B), hier ein Quader – Vorschlag für den Abgleich: Etikett auf „eines Körpers“ fassen (Definition sagt es schon). MMS-Anteil: keiner.")

row("2026MgrundlegendBAGLAA2MMS2", "c", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Winkel zwischen zwei Kanten über das Skalarprodukt berechnen", typ_neben="",
    stichwoerter="AS = (−2; 2; 3), AB = (0; 4; 0)|cos α = 8/(√17 · 4)|α ≈ 61°",
    voraussetzungen="Winkelformel des Skalarprodukts|Beträge",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=QU, kontext="ohne", textumfang="kurz",
    gegeben="S(2|2|3) Spitze der Pyramide OABCS",
    gesucht="Winkel zwischen den Kanten AS und AB",
    verfahren="Skalarprodukt der Kantenvektoren durch das Produkt der Beträge",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="°", abhaengig_von="",
    ergebnis="cos α = ((−2; 2; 3) · (0; 4; 0)) / (|(−2; 2; 3)| · |(0; 4; 0)|) liefert α ≈ 61° (amtlich)",
    zwischenergebnis="cos α = 2/√17", niveau_geschaetzt="II",
    fehlerquelle="Vektoren SA und AB (falsche Orientierung) ergeben den Nebenwinkel",
    bemerkung="Standardbezug: K2 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ga-B). MMS-Anteil: Rechner für die Auswertung, Ansatz eigen.")

row("2026MgrundlegendBAGLAA2MMS2", "d", innen="1", seite="2", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punktprobe an einer Geraden durchführen", typ_neben="",
    stichwoerter="g: x = (4; 0; 0) + t(−4; 4; 5)|(2; 2; 3) = (4; 0; 0) + t(−4; 4; 5) ohne Lösung",
    voraussetzungen="Geradengleichung aus zwei Punkten|Parameter aus den Koordinaten vergleichen",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Zeigen Sie", antwort="Term",
    material="Körper", skizze=QU, kontext="ohne", textumfang="kurz",
    gegeben="A(4|0|0), G(0|4|5), S(2|2|3)",
    gesucht="Gleichung der Geraden AG; Nachweis, dass S nicht auf ihr liegt",
    verfahren="Stützpunkt A, Richtungsvektor AG; Punktprobe mit S auf Widerspruch",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="x = (4; 0; 0) + t · (−4; 4; 5), t ∈ IR; die Gleichung (2; 2; 3) = (4; 0; 0) + t · (−4; 4; 5) hat keine Lösung (amtlich)",
    zwischenergebnis="t = 1/2 aus x und y, aber z: 5t = 3", niveau_geschaetzt="I",
    fehlerquelle="nur zwei Koordinaten prüfen",
    bemerkung="Standardbezug: K1 I, K2 I, K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Teil A), hier mit Aufstellen der Geradengleichung. MMS-Anteil: keiner.")

row("2026MgrundlegendBAGLAA2MMS2", "e", innen="1", seite="2", punkte="4", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Parameter für einen Volumenanteil zweier gegenläufiger Pyramiden im Quader bestimmen", typ_neben="",
    stichwoerter="V Quader = 4² · 5 = 80|Pyramiden mit Höhen 3 − k und 5 − (3 + k)|1/3 · 16 · (3 − k) + 1/3 · 16 · (2 − k) = 20|k = 5/8",
    voraussetzungen="Pyramidenvolumen|Höhen aus den z-Koordinaten der Spitzen|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=QU, kontext="ohne", textumfang="mittel",
    gegeben="Pyramiden OABCS_k mit S_k(2|2|3 − k) und DEFGQ_k mit Q_k(2|2|3 + k), 0 ≤ k < 2; Summe der Volumen 25 % des Quadervolumens",
    gesucht="Wert von k",
    verfahren="Beide Pyramidenvolumen als Terme in k, Summe gleich 20 setzen",
    schritte="3", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="Volumen des Quaders 4² · 5 = 80; 1/3 · 4² · (3 − k) + 1/3 · 4² · (5 − (3 + k)) = 20 ⇔ k = 5/8 (amtlich)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Höhe der oberen Pyramide als 3 + k statt 5 − (3 + k)",
    bemerkung="Standardbezug: K2 III, K4 III, K5 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) Volumenanteil in eine Gleichung für k übersetzen, mit beiden Höhen aus der Lage der Spitzen. MMS-Anteil: keiner.")

# ---- 2026MgrundlegendBAGLAA2MMS1: wortgleich mit 2026MgrundlegendBAGLAA2WTR1 (Zwilling im WTR-Zweig), Zeilen übernommen
row("2026MgrundlegendBAGLAA2MMS1", "a", innen="1", seite="1", punkte="3", afb_amtlich="I",
    leitidee="Analytische Geometrie",
    thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Lage eines Dreiecks parallel zu einer Koordinatenebene und symmetrisch zu einer anderen begründen",
    typ_neben="",
    stichwoerter="A, B, C haben x = 10: Ebene x = 10 parallel zur yz-Ebene|A in der xz-Ebene, B und C unterscheiden sich nur im Vorzeichen von y",
    voraussetzungen="gleiche Koordinate als Parallelität|Symmetrie zur xz-Ebene als Vorzeichenwechsel von y",
    format="Begründung",
    operator="Begründen Sie",
    antwort="Text",
    material="Körper",
    skizze="Schrägbild eines geraden Prismas ABCDEF: Grundfläche Dreieck ABC bei x = 10 (A auf der x-Achse, B und C bei z = 20 mit y = ±5), Deckfläche DEF mit D im Ursprung; Kanten AD, BE, CF parallel zur x-Achse; Koordinatenachsen x, y, z",
    kontext="ohne",
    textumfang="mittel",
    gegeben="gerades Prisma ABCDEF mit A(10 | 0 | 0), B(10 | 5 | 20), C(10 | −5 | 20), D(0 | 0 | 0)",
    gesucht="Begründung, dass ABC parallel zur yz-Ebene und symmetrisch zur xz-Ebene liegt",
    verfahren="Koordinaten vergleichen",
    schritte="2",
    zahlenraum="ganz|negativ",
    einheiten="",
    abhaengig_von="",
    ergebnis="Parallelität: ABC liegt in der Ebene x = 10; Symmetrie: A liegt in der xz-Ebene, die Koordinaten von B und C unterscheiden sich nur im Vorzeichen der y-Koordinate (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Symmetrie zur yz-Ebene behaupten",
    bemerkung="Standardbezug: K1 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBAGLAA2WTR1, Teilaufgabe 1a), Zeile übernommen.")
row("2026MgrundlegendBAGLAA2MMS1", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie",
    thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen eines geraden Prismas über einem Dreieck nachweisen",
    typ_neben="",
    stichwoerter="Grundfläche 1/2 · 10 · 20 = 100 (Basis BC = 10, Höhe 20)|Prismenhöhe |AD| = 10|V = 1000",
    voraussetzungen="Dreiecksfläche aus Basis und Höhe|Prisma: Grundfläche mal Höhe",
    format="Begründung",
    operator="Zeigen Sie",
    antwort="Text",
    material="Körper",
    skizze="Schrägbild eines geraden Prismas ABCDEF: Grundfläche Dreieck ABC bei x = 10 (A auf der x-Achse, B und C bei z = 20 mit y = ±5), Deckfläche DEF mit D im Ursprung; Kanten AD, BE, CF parallel zur x-Achse; Koordinatenachsen x, y, z",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Prisma aus a, Grundfläche ABC in x = 10, D(0 | 0 | 0)",
    gesucht="Nachweis, dass das Volumen 1000 beträgt",
    verfahren="Dreiecksfläche mal Kantenlänge AD",
    schritte="2",
    zahlenraum="ganz",
    einheiten="",
    abhaengig_von="",
    ergebnis="1/2 · (5 − (−5)) · 20 · 10 = 1000 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Pyramidenformel mit 1/3 verwenden",
    bemerkung="Standardbezug: K5 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Vom Typ „Körper: Volumen eines Prismas über einer Raute berechnen“ getrennt (Dreieck, Nachweis). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBAGLAA2WTR1, Teilaufgabe 1b), Zeile übernommen.")
row("2026MgrundlegendBAGLAA2MMS1", "c", innen="1", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie",
    thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen",
    typ_neben="",
    stichwoerter="Normalenvektor senkrecht zu DB = (10; 5; 20) und DA = (10; 0; 0): n = (0; 4; −1)|4y − z = c, D einsetzen: c = 0",
    voraussetzungen="Normalenvektor über Skalarprodukte oder Kreuzprodukt|Punkt einsetzen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Term",
    material="Körper",
    skizze="Schrägbild eines geraden Prismas ABCDEF: Grundfläche Dreieck ABC bei x = 10 (A auf der x-Achse, B und C bei z = 20 mit y = ±5), Deckfläche DEF mit D im Ursprung; Kanten AD, BE, CF parallel zur x-Achse; Koordinatenachsen x, y, z",
    kontext="ohne",
    textumfang="kurz",
    gegeben="A(10 | 0 | 0), B(10 | 5 | 20), D(0 | 0 | 0); Kontrolle 4y − z = 0",
    gesucht="Koordinatengleichung der Ebene ABD",
    verfahren="Normalenvektor aus zwei Richtungsvektoren, Konstante über einen Punkt",
    schritte="3",
    zahlenraum="ganz|negativ",
    einheiten="",
    abhaengig_von="",
    ergebnis="n · (0; 5; 20) = 0 ∧ n · (−10; 0; 0) = 0 liefert n = (0; 4; −1) als Normalenvektor; die Ebene hat eine Gleichung der Form 4y − z = c; da D in der Ebene liegt, folgt 4y − z = 0 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Normalenvektor (0; 1; 4) (Komponenten vertauscht)",
    bemerkung="Standardbezug: K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Koordinatengleichung der Ebene durch zwei sich schneidende Geraden bestimmen“ (2018-ea-A) getrennt (drei Punkte; Abgleich prüfen). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBAGLAA2WTR1, Teilaufgabe 1c), Zeile übernommen.")
row("2026MgrundlegendBAGLAA2MMS1", "d", innen="1", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie",
    thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Füllvolumen eines gedrehten Behälters am Graphen ergänzen und Grenzwinkel deuten",
    typ_neben="",
    stichwoerter="Fassungsvermögen 1000 cm³ = 1 Liter, halb voll: 0,5 Liter|bis zum Winkel α bleibt das Volumen 0,5 (waagerechte Strecke)|α: Winkel, bei dem das Wasser auszulaufen beginnt",
    voraussetzungen="Volumen aus b in Liter umrechnen|bis zum Überlaufen bleibt das Volumen konstant|Bedeutung des Knickpunkts",
    format="Eintragen|Kurzantwort",
    operator="Zeichnen Sie ein|Geben Sie an",
    antwort="Grafik",
    material="Diagramm",
    skizze="Abb. 2: Prisma in Ausgangslage und um die Achse AD gedreht, Drehpfeil bis 120°; Abb. 3: Koordinatensystem Drehwinkel 0° bis 90° gegen Wasservolumen in Litern 0 bis 1,1; Graph nur von α (≈ 55°) bei 0,5 Liter fallend bis β (≈ 76°) bei 0 eingezeichnet",
    kontext="Behälter/Drehung",
    textumfang="lang",
    gegeben="Behälter = Prisma (1000 cm³, Öffnung BEFC), halb gefüllt; Drehung um die Achse AD bis 120°; Graph Volumen gegen Drehwinkel für [α; β] vorgegeben",
    gesucht="Graph für [0°; α[ und Bedeutung von α",
    verfahren="konstante 0,5 Liter bis α einzeichnen, α als Beginn des Auslaufens deuten",
    schritte="2",
    zahlenraum="dezimal",
    einheiten="Liter|°",
    abhaengig_von="2026MgrundlegendBAGLAA2MMS1-1b",
    ergebnis="waagerechte Strecke bei 0,5 Litern von 0° bis α; bei diesem Drehwinkel beginnt das Wasser aus dem Behälter zu laufen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Graph ab 0° fallend zeichnen",
    bemerkung="Traegerbindung: Kontext (Behälter, Öffnung, Drehung und halbe Füllung sind nur aus der Trägeraufgabe zu verstehen; ohne sie ist die Zeile nicht nachbaubar). Standardbezug: K1 II, K3 II, K4 II, K6 II. AB amtlich: II. Amtlich. Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBAGLAA2WTR1, Teilaufgabe 1d), Zeile übernommen.")
row("2026MgrundlegendBAGLAA2MMS1", "e", innen="1", seite="2", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie",
    thema="Skalarprodukt und Winkel",
    typ="Winkel zwischen einer Seitenfläche und der Horizontalen als Grenzwinkel im Sachzusammenhang bestimmen",
    typ_neben="",
    stichwoerter="Wasser ist ganz ausgelaufen, wenn die Seitenwand ADEB waagerecht liegt|Winkel zwischen Ebene ABD (n = (0; 4; −1)) und xy-Ebene (n = (0; 0; 1))|cos β = 1/√17, β ≈ 76°",
    voraussetzungen="β als Winkel, bei dem die Wand ADEB horizontal wird|Winkel zwischen Ebenen über Normalenvektoren|Normalenvektor aus c",
    format="Rechnung",
    operator="Bestimmen Sie|Erläutern Sie",
    antwort="Zahl",
    material="Diagramm",
    skizze="Abb. 2: Prisma in Ausgangslage und um die Achse AD gedreht, Drehpfeil bis 120°; Abb. 3: Koordinatensystem Drehwinkel 0° bis 90° gegen Wasservolumen in Litern 0 bis 1,1; Graph nur von α (≈ 55°) bei 0,5 Liter fallend bis β (≈ 76°) bei 0 eingezeichnet",
    kontext="Behälter/Drehung",
    textumfang="mittel",
    gegeben="Ebene ABD: 4y − z = 0 (aus c); Drehung um AD; β Drehwinkel, bei dem das Volumen 0 erreicht",
    gesucht="rechnerisch ein geeigneter Wert für β mit Erläuterung des Ansatzes",
    verfahren="Winkel zwischen der Wandebene ABD und der xy-Ebene über die Normalenvektoren",
    schritte="3",
    zahlenraum="Wurzel|dezimal",
    einheiten="°",
    abhaengig_von="2026MgrundlegendBAGLAA2MMS1-1c",
    ergebnis="cos β = |(0; 4; −1) · (0; 0; 1)| / (|(0; 4; −1)| · |(0; 0; 1)|) = 1/√17 liefert β ≈ 76°; wenn sich die Seitenwand ADEB in horizontaler Lage befindet, ist das gesamte Wasser aus dem Behälter gelaufen (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Winkel zwischen Kante AB und der xy-Ebene nehmen (≈ 44°) oder α statt β rechnen",
    bemerkung="Traegerbindung: Kontext. Standardbezug: K1 III, K2 II, K3 III, K4 III, K5 II, K6 II. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (a) „Behälter leer“ in „Wand ADEB horizontal“ und in den Winkel zwischen Ebene ABD und xy-Ebene übersetzen, verkettet mit der Winkelberechnung. Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBAGLAA2WTR1, Teilaufgabe 1e), Zeile übernommen.")

# ---- 2026MgrundlegendBStochastikMMS1: wortgleich mit 2026MgrundlegendBStochastikWTR1 (Zwilling im WTR-Zweig), Zeilen übernommen
row("2026MgrundlegendBStochastikMMS1", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen",
    typ_neben="",
    stichwoerter="(b über 3) · c³ · 0,25⁷ mit b = 10, c = 0,75|a = 3: genau drei sammeln Treuepunkte",
    voraussetzungen="Bernoulli-Formel mit n = 10, p = 0,75|Exponenten 3 und 7 ergänzen sich zu 10",
    format="Kurzantwort",
    operator="Geben Sie an|Beschreiben Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Supermarkt/Treuepunkte",
    textumfang="lang",
    gegeben="75 % des Kundenkreises sammeln Treuepunkte; X Anzahl der Sammler unter 10 zufällig Ausgewählten, binomialverteilt; Term P(X = a) = (b über 3) · c³ · 0,25⁷",
    gesucht="Werte a, b, c und Beschreibung des Ereignisses",
    verfahren="Platzhalter aus n, p und k lesen",
    schritte="1",
    zahlenraum="ganz|dezimal",
    einheiten="",
    abhaengig_von="",
    ergebnis="a = 3; b = 10; c = 0,75; genau drei Personen sammeln Treuepunkte (amtlich)",
    zwischenergebnis="P ≈ 0,0031",
    niveau_geschaetzt="I",
    fehlerquelle="a = 7 (Exponent von 0,25 als Trefferzahl)",
    bemerkung="Standardbezug: K3 I, K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2026-ea-A; Thema hier Binomialverteilung). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR1, Teilaufgabe 1a), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS1", "b", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    typ_neben="",
    stichwoerter="P(X < 8) = P(X ≤ 7) mit n = 10, p = 0,75|≈ 47,4 %",
    voraussetzungen="„weniger als 8“ als X ≤ 7|kumulierte Binomialverteilung am WTR",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Supermarkt/Treuepunkte",
    textumfang="kurz",
    gegeben="X binomialverteilt mit n = 10, p = 0,75",
    gesucht="P(X < 8)",
    verfahren="kumulierte Wahrscheinlichkeit am Rechner",
    schritte="1",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    abhaengig_von="",
    ergebnis="P(X < 8) ≈ 47,4 % (n = 10, p = 0,75) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="P(X ≤ 8) rechnen (≈ 75,6 %)",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Erster Typ mit Rechnereinsatz (Teil B). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR1, Teilaufgabe 1b), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS1", "c", innen="1", seite="2", punkte="2", afb_amtlich="II",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Wahrscheinlichkeit über die Verteilung der Gegenzufallsgröße im Diagramm erläutern",
    typ_neben="",
    stichwoerter="Y = 10 − X ist B(10; 0,25)-verteilt|P(X = 6) = P(Y = 4)|Säule bei k = 4 ablesen",
    voraussetzungen="Gegenzufallsgröße mit p' = 1 − p|Zuordnung k ↔ n − k",
    format="Begründung",
    operator="Erläutern Sie",
    antwort="Text",
    material="Diagramm",
    skizze="Säulendiagramm P(Y = k) für k = 0 bis 10 mit y-Marken 0,1 bis 0,3: Säulen bei 0 etwa 0,06, 1 etwa 0,19, 2 etwa 0,28, 3 etwa 0,25, 4 etwa 0,15, 5 etwa 0,06, 6 etwa 0,02, danach kaum sichtbar",
    kontext="Supermarkt/Treuepunkte",
    textumfang="mittel",
    gegeben="Abbildung: Verteilung von Y mit n = 10, p = 0,25; X Anzahl der Sammler mit p = 0,75",
    gesucht="Erläuterung, wie man mit der Abbildung P(X = 6) ermittelt",
    verfahren="X = 6 Sammler heißt Y = 4 Nichtsammler",
    schritte="1",
    zahlenraum="ganz|dezimal",
    einheiten="",
    abhaengig_von="",
    ergebnis="wegen P(X = 6) = P(Y = 4) (n = 10; p = 0,75 bzw. 0,25) entspricht in der Abbildung der Wert für k = 4 der gesuchten Wahrscheinlichkeit (amtlich)",
    zwischenergebnis="≈ 0,146",
    niveau_geschaetzt="II",
    fehlerquelle="Säule bei k = 6 ablesen",
    bemerkung="Standardbezug: K1 II, K2 II, K4 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Eine Deutung (Gegenzufallsgröße) ohne Verkettung, II. Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR1, Teilaufgabe 1c), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS1", "a", innen="2", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik",
    thema="Baumdiagramm und Pfadregeln",
    typ="Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen",
    typ_neben="",
    stichwoerter="P(w und T) = 0,75 · 0,8 = 0,6|P(nicht w und nicht T) = 0,25 · 0,4 = 0,1|0,6 = 6 · 0,1: wahr",
    voraussetzungen="Pfadregel|Gegenwahrscheinlichkeiten 0,25 und 1 − a|Vergleich als Faktor",
    format="Begründung",
    operator="Untersuchen Sie",
    antwort="Text",
    material="Diagramm",
    skizze="Baumdiagramm: erste Stufe T (75 %) und nicht T; zweite Stufe w (80 %) und nicht w unter T, w (a) und nicht w unter nicht T",
    kontext="Supermarkt/Treuepunkte",
    textumfang="lang",
    gegeben="75 % sammeln (T); unter den Sammlern 80 % weiblich; unter den Nichtsammlern Anteil a weiblich; a = 0,6",
    gesucht="ob P(weiblich und T) sechsmal so groß ist wie P(nicht weiblich und nicht T)",
    verfahren="beide Pfade berechnen und vergleichen",
    schritte="2",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    abhaengig_von="",
    ergebnis="wegen 0,75 · 0,8 = 6 · 0,25 · 0,4 ist die Aussage wahr (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="1 − a = 0,4 nicht bilden und mit a = 0,6 rechnen",
    bemerkung="Standardbezug: K1 II, K3 II, K6 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR1, Teilaufgabe 2a), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS1", "b", innen="2", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik",
    thema="Baumdiagramm und Pfadregeln",
    typ="Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen",
    typ_neben="",
    stichwoerter="P(nicht w) = 0,75 · 0,2 + 0,25 · (1 − a) = 0,3|0,4 − 0,25a = 0,3|a = 0,4",
    voraussetzungen="Randwahrscheinlichkeit als Summe zweier Pfade|lineare Gleichung",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Diagramm",
    skizze="Baumdiagramm: erste Stufe T (75 %) und nicht T; zweite Stufe w (80 %) und nicht w unter T, w (a) und nicht w unter nicht T",
    kontext="Supermarkt/Treuepunkte",
    textumfang="kurz",
    gegeben="Baumdiagramm wie in a; Anteil der nicht weiblichen Personen im Kundenkreis 30 %",
    gesucht="Anteil a",
    verfahren="Summe der Pfade zu „nicht weiblich“ gleich 0,3 setzen",
    schritte="2",
    zahlenraum="dezimal",
    einheiten="",
    abhaengig_von="",
    ergebnis="0,75 · 0,2 + 0,25 · (1 − a) = 0,3 ⇔ 0,4 − 0,25a = 0,3 ⇔ a = 0,4 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Pfad 0,75 · 0,2 vergessen",
    bemerkung="Standardbezug: K2 I, K3 II, K4 II, K5 II. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Anteil aus dem Ergebnis eines Befragungsverfahrens berechnen“ getrennt (Randwahrscheinlichkeit statt Ja-Häufigkeit; Abgleich prüfen). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR1, Teilaufgabe 2b), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS1", "c", innen="2", seite="2", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik",
    thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Monotonie einer bedingten Wahrscheinlichkeit bei Änderung eines Anteils beurteilen",
    typ_neben="",
    stichwoerter="P(T | nicht w) = 0,75 · 0,2 / (0,75 · 0,2 + 0,25 · (1 − a))|a steigt ⇒ Nenner fällt ⇒ Quotient steigt|Aussage wahr",
    voraussetzungen="bedingte Wahrscheinlichkeit als Bayes-Quotient in a|Monotonie eines Bruchs im Nenner",
    format="Begründung",
    operator="Beurteilen Sie",
    antwort="Text",
    material="Diagramm",
    skizze="Baumdiagramm: erste Stufe T (75 %) und nicht T; zweite Stufe w (80 %) und nicht w unter T, w (a) und nicht w unter nicht T",
    kontext="Supermarkt/Treuepunkte",
    textumfang="lang",
    gegeben="ein Jahr später: weiterhin 75 % Sammler, 80 % davon weiblich, a gestiegen; Aussage: P(T | nicht weiblich) ist größer als vor einem Jahr",
    gesucht="Beurteilung der Aussage",
    verfahren="Term in a aufstellen und Monotonie begründen",
    schritte="3",
    zahlenraum="dezimal",
    einheiten="",
    abhaengig_von="",
    ergebnis="die Aussage ist wahr; mit dem Term 0,75 · 0,2 / (0,75 · 0,2 + 0,25 · (1 − a)) kann die beschriebene Wahrscheinlichkeit berechnet werden; wenn a steigt, nimmt der Nenner ab und der Quotient zu (amtlich)",
    zwischenergebnis="a = 0,4: 0,5; a = 0,6: 0,6",
    niveau_geschaetzt="III",
    fehlerquelle="mit Zahlenbeispiel statt allgemein argumentieren; Zähler für abhängig von a halten",
    bemerkung="Standardbezug: K1 III, K2 II, K3 II, K5 II, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt. Eichregel: (d) Sachaussage in einen Bayes-Term mit Parameter übersetzen und mit der Monotonie des Bruchs verketten. Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR1, Teilaufgabe 2c), Zeile übernommen.")

# ---- 2026MgrundlegendBStochastikMMS2: wortgleich mit 2026MgrundlegendBStochastikWTR2 (Zwilling im WTR-Zweig), Zeilen übernommen
row("2026MgrundlegendBStochastikMMS2", "a", innen="1", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik",
    thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen vervollständigen",
    typ_neben="",
    stichwoerter="Ränder 0,32 / 0,68 und 0,4 / 0,6|Innenfelder 0,14, 0,26, 0,18, 0,42",
    voraussetzungen="Randsummen aus den Anteilen|Differenzen",
    format="Tabelle",
    operator="Ergänzen Sie",
    antwort="Tabelle",
    material="Tabelle",
    skizze="Vierfeldertafel H / nicht H gegen L / nicht L, nur 0,14 (H und L) und die Summe 1 eingetragen",
    kontext="Playlist/Musik",
    textumfang="mittel",
    gegeben="32 % Hip-Hop-Songs (H), 40 % mindestens 4 Minuten lang (L), P(H und L) = 0,14",
    gesucht="fehlende Wahrscheinlichkeiten der Vierfeldertafel",
    verfahren="Ränder eintragen, Innenfelder als Differenzen",
    schritte="2",
    zahlenraum="dezimal",
    einheiten="",
    abhaengig_von="",
    ergebnis="H und L 0,14, nicht H und L 0,26, H und nicht L 0,18, nicht H und nicht L 0,42; Ränder 0,4, 0,6, 0,32, 0,68 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="0,32 · 0,4 als Schnitt ansetzen (Unabhängigkeit unterstellt)",
    bemerkung="Standardbezug: K4 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR2, Teilaufgabe 1a), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS2", "b", innen="1", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik",
    thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen",
    typ_neben="",
    stichwoerter="P(L | H) = 0,14/0,32 ≈ 43,8 %",
    voraussetzungen="Bedingung als Nenner|Schnitt aus der Vierfeldertafel",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Vierfeldertafel aus a",
    kontext="Playlist/Musik",
    textumfang="kurz",
    gegeben="P(H) = 0,32, P(H und L) = 0,14",
    gesucht="P(L | H)",
    verfahren="Quotient",
    schritte="1",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    abhaengig_von="2026MgrundlegendBStochastikMMS2-1a",
    ergebnis="0,14/0,32 ≈ 43,8 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="0,14/0,4 (Bedingung vertauscht)",
    bemerkung="Standardbezug: K2 II, K3 II, K5 I, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (2022-ga-A; hier mit Vierfeldertafel – Definition „ohne Vierfeldertafel“ beim Abgleich lockern). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR2, Teilaufgabe 1b), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS2", "c", innen="1", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    typ_neben="",
    stichwoerter="X ~ B(20; 0,32)|P(X > 5) = 1 − P(X ≤ 5) ≈ 65,7 %",
    voraussetzungen="„mehr als 5“ als Gegenereignis von X ≤ 5|kumulierte Verteilung am WTR",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Playlist/Musik",
    textumfang="mittel",
    gegeben="20 zufällig ausgewählte Lieder, Anzahl der Hip-Hop-Songs binomialverteilt mit p = 0,32",
    gesucht="P(mehr als 5 Hip-Hop-Songs)",
    verfahren="1 − P(X ≤ 5) am Rechner",
    schritte="2",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    abhaengig_von="",
    ergebnis="X: Anzahl der Hip-Hop-Songs; P(X > 5) ≈ 65,7 % (n = 20, p = 0,32) (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="P(X ≥ 5) rechnen",
    bemerkung="Standardbezug: K3 I, K5 I, K6 I. AB amtlich: I. Amtlich, eigene Rechnung bestätigt. Typ wiederverwendet (Stochastik WTR 1 dieses Stapels). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR2, Teilaufgabe 1c), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS2", "d", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren",
    typ_neben="",
    stichwoerter="Summe k = 0 bis 8 von (20 über k) · 0,32^k · 0,68^(20 − k) = P(X ≤ 8)|höchstens acht Hip-Hop-Songs unter den 20 Liedern, etwa 84,3 %",
    voraussetzungen="Binomialsumme als kumulierte Wahrscheinlichkeit|n = 20, p = 0,32 im Sachzusammenhang",
    format="Kurzantwort",
    operator="Beschreiben Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Playlist/Musik",
    textumfang="mittel",
    gegeben="20 Lieder, p = 0,32; Aussage Summe k = 0 bis 8 von (20 über k) · 0,32^k · 0,68^(20 − k) ≈ 0,843",
    gesucht="Bedeutung der Aussage im Sachzusammenhang",
    verfahren="Summe als P(X ≤ 8) lesen",
    schritte="1",
    zahlenraum="dezimal|Potenz",
    einheiten="",
    abhaengig_von="",
    ergebnis="die Wahrscheinlichkeit dafür, dass unter den ausgewählten Liedern höchstens acht Hip-Hop-Songs sind, beträgt etwa 84,3 % (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="„genau acht“ statt „höchstens acht“",
    bemerkung="Standardbezug: K1 II, K3 II, K4 II, K6 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Vom Typ „Sachaussage zu einer Ungleichung mit Binomialsumme formulieren“ getrennt (Gleichung mit Wert statt Ungleichung mit Parameter; Abgleich prüfen). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR2, Teilaufgabe 1d), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS2", "e", innen="1", seite="2", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik",
    thema="Lage- und Streumaße einer Stichprobe",
    typ="Fehlenden Wert aus dem arithmetischen Mittel berechnen",
    typ_neben="",
    stichwoerter="Summe der fünf Längen 4:45 + 3:56 + 3:35 + 4:36 + 4:08 = 21:00|6 · 4:05 = 24:30|sechstes Lied 3:30",
    voraussetzungen="Mittelwert als Summe durch Anzahl|Zeitangaben in Sekunden umrechnen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Tabelle Nummer 1 bis 5 mit Längen 4:45, 3:56, 3:35, 4:36, 4:08",
    kontext="Playlist/Musik",
    textumfang="mittel",
    gegeben="Längen der ersten fünf Lieder 4:45, 3:56, 3:35, 4:36, 4:08; Durchschnitt der ersten sechs 4:05",
    gesucht="Länge des sechsten Liedes",
    verfahren="Gesamtsumme aus dem Mittelwert minus Summe der fünf",
    schritte="3",
    zahlenraum="ganz",
    einheiten="Minuten|Sekunden",
    abhaengig_von="",
    ergebnis="die Summe der Längen der ersten fünf Lieder beträgt 21 Minuten; die Länge des sechsten Liedes ist somit 6 · (4 min 5 s) − 21 min = 3 min 30 s (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="4:05 als 4,05 Minuten rechnen",
    bemerkung="Standardbezug: K1 I, K2 II, K4 I, K5 I. AB amtlich: II. Amtlich, eigene Rechnung bestätigt. Erste Fundstelle des Themas Lage- und Streumaße einer Stichprobe. Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR2, Teilaufgabe 1e), Zeile übernommen.")
row("2026MgrundlegendBStochastikMMS2", "f", innen="1", seite="2", punkte="3", afb_amtlich="I|II|III",
    leitidee="Stochastik",
    thema="Kombinatorik",
    typ="Anzahl der Sitzordnungen mit Abstandsbedingung berechnen",
    typ_neben="",
    stichwoerter="zwei kurze Lieder (k), drei lange (l)|Muster ohne kk nebeneinander: klkll, kllkl, klllk, lklkl, lkllk, llklk – sechs|je Muster 2! · 3! Anordnungen|6 · 2 · 6 = 72",
    voraussetzungen="kurze und lange Lieder aus der Tabelle zählen|zulässige Muster aufzählen|Permutationen innerhalb der Sorten",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Tabelle wie in e",
    kontext="Playlist/Musik",
    textumfang="lang",
    gegeben="fünf Lieder mit Längen aus der Tabelle (zwei unter 4 Minuten); jedes genau einmal; kurze Lieder nicht direkt nacheinander",
    gesucht="Anzahl der zulässigen Reihenfolgen",
    verfahren="Muster der Sorten aufzählen, mit den Anordnungen innerhalb der Sorten multiplizieren",
    schritte="3",
    zahlenraum="ganz",
    einheiten="",
    abhaengig_von="",
    ergebnis="genau zwei der Lieder sind kürzer als 4 Minuten; mit k für kurz und l für lang sind sechs Anordnungen möglich: klkll, kllkl, klllk, lklkl, lkllk, llklk; somit gibt es insgesamt 6 · 2! · 3! = 72 Möglichkeiten (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Muster zählen und die 2! · 3! vergessen (6) oder 5! − 4! · 2 = 72 ohne Begründung",
    bemerkung="Standardbezug: K1 II, K2 III, K3 II, K5 I, K6 III. AB amtlich: III. Amtlich, eigene Rechnung bestätigt (Aufzählung). Eichregel: (a) die Regel „nicht direkt nacheinander“ in zulässige Muster übersetzen, verkettet mit dem Abzählen der Anordnungen. Typ wiederverwendet (2024-ga-A; dort Personen und Plätze, gleiche Fertigkeit). Wortgleich mit dem WTR-Zwilling (2026-ga-B-wtr, Datei 2026MgrundlegendBStochastikWTR2, Teilaufgabe 1f), Zeile übernommen.")

NEUE_TYPEN = [
    ("Zeitpunkt für einen vorgegebenen Bestand aus der Funktionsgleichung mit dem Rechner ermitteln", "Analysis", "Gleichungen lösen",
     "Die Gleichung f(x) = c für einen vorgegebenen Bestandswert mit dem Rechner numerisch lösen und die Lösung als Zeitpunkt mit Einheit angeben.",
     "2026MgrundlegendBAnalysisMMS1-1a"),
    ("Gleichung für die mittlere Änderungsrate lösen und Lösung im Sachzusammenhang deuten", "Analysis", "Ableitung und Änderungsrate",
     "Eine Gleichung der Form (f(c) − f(0))/c = m mit dem Rechner lösen, den Quotienten als mittlere Änderungsrate über [0; c] und die Lösung als Zeitraum im Sachzusammenhang deuten.",
     "2026MgrundlegendBAnalysisMMS1-1b"),
    ("Zeitpunkt und Größe der maximalen Änderungsrate über die zweite Ableitung berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Die Stelle der größten Änderungsrate als Nullstelle der zweiten Ableitung berechnen und den Wert der Rate dort angeben.",
     "2026MgrundlegendBAnalysisMMS1-1c"),
    ("Länge des Zeitraums mit Mindeständerungsrate über die Lösungen von f'(x) = c berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Die beiden Lösungen der Gleichung f'(x) = c mit dem Rechner bestimmen und ihre Differenz als Länge des Zeitraums angeben, in dem die Rate mindestens c beträgt.",
     "2026MgrundlegendBAnalysisMMS1-1d"),
    ("Größten jährlichen Zuwachs einer Rate über die Rechtskrümmung des Graphen begründen", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Am Graphen einer Rate über die Rechtskrümmung begründen, dass der Zuwachs über ein Zeitintervall fester Länge am Anfang am größten ist, und ihn mit einer Schranke vergleichen.",
     "2026MgrundlegendBAnalysisMMS1-1e"),
    ("Nullstellen und Werte: Schnittpunkt mit der y-Achse und Steigung des Graphen dort angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Den Schnittpunkt eines Graphen mit der y-Achse als (0 | f(0)) und die Steigung dort als f'(0) angeben.",
     "2026MgrundlegendBAnalysisMMS1-2a"),
    ("Ergebnis eines Lösungswegs als y-Achsenabschnitt der parallelen Tangente deuten", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Einen vorgegebenen Lösungsweg (f'(x) = m, Punkt einsetzen) als Aufstellen der zu einer Geraden parallelen Tangente erkennen und das Ergebnis als y-Achsenabschnitt dieser Tangente deuten.",
     "2026MgrundlegendBAnalysisMMS1-2b"),
    ("Fläche: Parallele Gerade zur Halbierung einer Fläche über ein Achsendreieck bestimmen", "Analysis", "Flächeninhalt durch Integration",
     "Eine zu einer gegebenen Geraden parallele Gerade so bestimmen, dass das von ihr mit den Achsen gebildete Dreieck die Hälfte der Fläche zwischen Graph und Achsen hat (Dreiecksfläche in a gleich halbem Integral).",
     "2026MgrundlegendBAnalysisMMS1-2c"),
    ("Nullstellen und Werte: Nullstellen berechnen und Grenzverhalten einer ganzrationalen Funktion angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Nullstellen einer ganzrationalen Funktion berechnen (Rechner oder Faktorisierung) und das Verhalten für x → ±∞ über Grad und Leitkoeffizient angeben.",
     "2026MgrundlegendBAnalysisMMS2-1a"),
    ("Extrempunkte: Existenz eines Hochpunkts aus dem Grad und einem Tiefpunkt begründen und Koordinaten angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Begründen, dass eine ganzrationale Funktion dritten Grades mit einem Tiefpunkt auch einen Hochpunkt hat, und dessen Koordinaten angeben.",
     "2026MgrundlegendBAnalysisMMS2-1b"),
    ("Wendestelle nachweisen und Winkel der Wendetangente mit der x-Achse über die Steigung −1 zeigen", "Analysis", "Kurvenuntersuchung",
     "Eine vorgegebene Wendestelle über f'' = 0 nachweisen und über f' = ±1 zeigen, dass die Wendetangente mit der x-Achse einen Winkel von 45° einschließt.",
     "2026MgrundlegendBAnalysisMMS2-1c"),
    ("Passung eines Profils in einen Karton über Breite und Tiefe aus Nullstellen und Tiefpunkt prüfen", "Analysis", "Kurvenuntersuchung",
     "Breite (aus den Nullstellen) und Tiefe (aus dem Tiefpunkt) eines durch einen Graphen beschriebenen Profils mit Maßstab berechnen und mit vorgegebenen Innenmaßen vergleichen.",
     "2026MgrundlegendBAnalysisMMS2-1e"),
    ("Fläche: Aufgabenstellung zu einem Volumen aus Fläche zwischen Graph und Gerade und Maßstab formulieren und erläutern", "Analysis", "Flächeninhalt durch Integration",
     "Zu einem Lösungsweg aus Schnittstellen mit einer waagerechten Geraden, Integral der Differenz und Umrechnung mit Maßstab und Länge eine passende Aufgabenstellung im Sachzusammenhang formulieren und die Schritte erläutern.",
     "2026MgrundlegendBAnalysisMMS2-1f"),
    ("Fläche: Radius eines flächengleichen Halbkreisprofils aus einem Integral bestimmen und Materialmasse berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Den Radius eines Halbkreises mit gleichem Flächeninhalt wie eine Integralfläche (mit Maßstab) bestimmen und daraus mit Wanddicke, Länge und Dichte die Masse eines halben Kreisrings berechnen.",
     "2026MgrundlegendBAnalysisMMS2-1g"),
    ("Übergangsprozess: Unmöglichkeit einer Verteilung über eine negative Vorgängerkomponente begründen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus P · v₀ = v₁ den Vorgängervektor berechnen und aus einer negativen Komponente begründen, dass v₁ im Modell nicht auftreten kann.",
     "2026MgrundlegendBAGLAA1MMS-1c"),
    ("Übergangsprozess: Konstante prozentuale Abnahme einer Gruppe ohne Zugänge aus der Matrix begründen", "Analytische Geometrie", "Matrizen und Übergangsprozesse",
     "Aus der Zeile einer Übergangsmatrix (Verbleibrate, keine Zugänge) begründen, dass eine Gruppe je Schritt um einen festen Prozentsatz abnimmt.",
     "2026MgrundlegendBAGLAA1MMS-1d"),
    ("Punkt aus einer Linearkombination von Kantenvektoren in das Schrägbild einzeichnen", "Analytische Geometrie", "Vektoren und Rechenoperationen",
     "Einen durch eine Linearkombination von Kantenvektoren eines Körpers gegebenen Punkt in das Schrägbild einzeichnen.",
     "2026MgrundlegendBAGLAA2MMS2-1a"),
    ("Körper: Parameter für einen Volumenanteil zweier gegenläufiger Pyramiden im Quader bestimmen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Für zwei Pyramiden über Grund- und Deckfläche eines Quaders mit parameterabhängigen Spitzen den Parameter so bestimmen, dass die Summe ihrer Volumen einen vorgegebenen Anteil des Quadervolumens hat.",
     "2026MgrundlegendBAGLAA2MMS2-1e"),
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
