# -*- coding: utf-8 -*-
"""abi-bau.py – Gerüst für die Erfassung eines Hefts im Profil abi.
Version 0.8 · 16.09.2026 · gilt mit katalog-prompt.md v0.5, abitur-vokabular.md v1.2 und abi.md v0.14

Je Heft werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" und unter „AB HIER UNVERÄNDERT" bleibt unverändert.

Änderungen gegenüber 0.7 (Heft 2022-bebb-lk, 16.09.2026): Die Eichschwelle
zählt nur eigene Schätzungen. Eine Dublette, die die Schätzung ihrer Poolzeile
trägt, ist dort schon gemessen (Eichung des Stapels in iqb-pruefungen.md); sie
für die Schwelle des Hefts noch einmal zu zählen, misst nichts Neues, sondern
nur die zufällige Teilmenge des Pools, die das Heft übernimmt (2022-bebb-lk:
27 von 32 geerbten Zeilen, 84 %, alle fünf Abweichungen in der Poolzeile
vermerkt). Die Kennzahl Eichung je Heft nennt weiter alle gewerteten Zeilen
und weist die geerbten aus; die Schwelle greift bei mindestens zehn eigenen
gewerteten Zeilen. Die Schätzung selbst bleibt unverändert (keine
nachträgliche Anpassung an den Standardbezug, iqb.md § 7).

Änderungen gegenüber 0.6 (Auftrag „Geltung klären, Reste schließen, vier
Stark-Hefte erfassen", 16.09.2026): Geltung je Heft – ein Heft wird gegen die
Zielprüfung(en) seines papier-Kürzels gemessen (ziele_von: be-gk, be-lk,
bb-ea; gemeinsame Hefte bebb-gk gegen be-gk und bb-gk, bebb-lk gegen be-lk
und bb-ea); eine Zeile liegt in der Geltung, wenn ihr Thema in mindestens
einer dieser Spalten gilt, der Bericht nennt beide Spalten einzeln und
daneben weiter alle vier Zielprüfungen (abitur-vokabular.md § 3).

Änderungen gegenüber 0.5 (Auftrag „Reserve öffnen, Verweise schließen",
16.09.2026): Die Vormerkung „Poolaufgabe (nicht erfasst …)" ist ein
Übergangszustand – offener Posten, bis der Stapel erfasst ist; danach stellt
abgleich.py sie auf „Dublette von:" (wortgleich) oder auf den neuen Verweis
„Abgewandelt von: <Kennung>; <Unterschied>." (abgewandelte Fassung, kein
geteilter Typ verlangt) um. Beide Verweise werden geprüft (Kennung, Feldanfang,
Poolzeile erfasst); die Poolquote zählt „Abgewandelt von" wie bisher die
abgewandelte Vormerkung.

Änderungen gegenüber 0.4 (Auftrag „Heft 2023 nachprüfen, abi-Bestand gegen
den Pool abgleichen"): Poolquote je Heft als Kennzahl (Zeilen und BE, die
wortgleich im Pool stehen; in der Kennzahlenzeile und in der Selbstprüfung je
Heft); Vermerk „Poolaufgabe (nicht erfasst): <Kennung>" als Vorstufe des
Verweises „Dublette von:", geprüft (Kennung, Feldanfang, noch nicht erfasst);
Pool-Kennungen mit Aufgabennummer vom ASCII-Minus-Test ausgenommen (schon im
Heftlauf 2023).

Änderungen gegenüber 0.3 (Entscheidung des Lehrers, 16.09.2026: Themenfeld
bereinigen): leitidee und thema einer Zeile müssen gleich leitidee und thema
ihres Typs in abitur-typen.csv sein (geprüft für ZEILEN und in der
Selbstprüfung für den Bestand); der Schnitt Thema × Klasse × Handlung wird
über das Thema des Typs gemessen (Lauf 13 von abgleich.py hat den Bestand
darauf gebracht). Wie iqb-bau.py v1.1.

Änderungen gegenüber 0.2 (Entscheidung 25, 15.09.2026: gemeinsame Typenliste
für abi und iqb, abi auf dem Typenschnitt nach Entscheidung 24) – das Skript
zieht auf den Stand von iqb-bau.py v1.0 nach:
  - Sachgebiete, Themen, Geltungstabelle, Gegenstandsklassen und Handlungen
    kommen aus abitur-vokabular.md; das Profil abi.md liefert kein Vokabular mehr.
  - Typenliste abitur-typen.csv, geteilt mit iqb: beispiel_id darf in iqb-katalog.csv
    zeigen, ein Typ gilt als verwendet, wenn er in einem der Kataloge steht
    (ANDERE_KATALOGE). Präfixregel (abitur-vokabular.md § 4) für Typenliste und
    NEUE_TYPEN.
  - SCHWELLEN: Qualitätsschranke im Skript („?", ersatzweise, Eichung).
  - Eichung, wo ein amtlicher Bereich vorliegt (afb_amtlich, in Teil B
    zusätzlich „AB amtlich: …" in bemerkung wie im Profil iqb); die Hefte bis
    2018 haben keinen und zählen nicht.
  - Vollständigkeit: jede Aufgabe in KONFIG["soll"] muss Zeilen haben, jede
    Punktsumme stimmen; KONFIG["probe"] = True prüft, schreibt aber nichts.
  - Pool-Teilaufgaben in Landesheften (abi.md § 7): eigene Zeile mit
    geteiltem Typ, Verweis „Dublette von: <iqb-id>" in bemerkung; das Skript
    prüft, dass die id im iqb-Katalog steht und typ wie typ_neben gleich sind.
  - Trägerbindung wie im Profil iqb: feste Markierung „Traegerbindung: Kontext"
    am Anfang von bemerkung, kein eigenes Feld.
  - Kennzahlenzeile je Heft (Typen neu, Eichung, Wiederverwendung im Niveau,
    Geltung, Schnitt) für abi-pruefungen.md § 2.
  - papier-Kürzel bebb für die gemeinsamen Hefte 2019–2025; aufgabe darf ein-
    oder zweistufig sein (Aufgabe 3 gegen 2.1).
Umbenennungen und Zusammenziehungen laufen über abgleich.py (Kern § 9).

Ablauf:
  1. abitur-vokabular.md, katalog-prompt.md, abi-katalog.csv, iqb-katalog.csv und
     abitur-typen.csv neben dieses Skript legen (aus dem Repo).
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen.
  3. python abi-bau.py – schreibt beide CSV-Dateien, gibt Prüftabelle und
     Bericht aus. Bei einem Fehler wird nichts geschrieben.
  4. Ist ZEILEN leer, läuft nur die Selbstprüfung über den Gesamtbestand.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    "jahr": "2020",
    "papier": "2020-be-gk",
    "datei": "hefte/2020-be-gk.pdf",  # Stark-Band Berlin GK (Band zum Abitur 2021), PDF mit Textebene, lokal (abi.md § 2)
    "seiten": 49,
    # Sollpunkte je Aufgabe aus der BE-Spalte; jede Aufgabe des Hefts muss hier
    # stehen (Vollständigkeit). Hilfsmittelfreier Teil (Aufgabe 1) als 1.1 bis 1.5
    # in Heftreihenfolge (Analysis 1, Analysis 2, Geometrie 1, Geometrie 2,
    # Stochastik; alle Pflicht, 25 BE). Teil B: je Sachgebiet zwei Aufgaben zur
    # Wahl (2.1/2.2 Analysis 35 BE, 3.1/3.2 Geometrie 20, 4.1/4.2 Stochastik 20);
    # bearbeitet 25 + 35 + 20 + 20 = 100 BE, angeboten 175.
    "soll": {"1.1": 5, "1.2": 5, "1.3": 5, "1.4": 5, "1.5": 5,
             "2.1": 35, "2.2": 35, "3.1": 20, "3.2": 20, "4.1": 20, "4.2": 20},
    "probe": False,
}

# ========================================= QUELLEN UND PRÜFUNG, NICHT ÄNDERN
KAT = "abi-katalog.csv"
TYP = "abitur-typen.csv"
VOKABULAR = "abitur-vokabular.md"
KERN = "katalog-prompt.md"
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]
# Kataloge der anderen Profile mit derselben Typenliste (Entscheidung 25): ihre
# ids gelten für beispiel_id und für „Dublette von:", ihre Typfelder zählen als
# Verwendung.
ANDERE_KATALOGE = ["iqb-katalog.csv"]

PFLICHT = ("id jahr papier block aufgabe titel teilaufgabe seite punkte hilfsmittel leitidee "
           "thema typ format operator antwort material skizze kontext textumfang gegeben gesucht "
           "verfahren schritte ergebnis niveau_geschaetzt fehlerquelle").split()

# Qualitätsschranke (abi.md § 7, wie iqb.md § 7). Anteile beziehen sich auf die
# Zeilen des Hefts; „mindestens" ist die Zahl, die immer erlaubt ist.
SCHWELLEN = {
    "fragezeichen_anteil": 0.10, "fragezeichen_mindestens": 2,
    "neue_typen_anteil": None, "neue_typen_ab_bestand": 100,
    "ersatzweise_anteil": 0.10, "ersatzweise_mindestens": 2,
    # Eichung gegen den amtlichen Bereich, ab dieser Zahl eigener gewerteter Zeilen
    # scharf; geerbte Schätzungen der Dubletten zählen nicht (v0.8).
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
# Felder, die bewusst umlautfrei sind: Dateinamen und papier-Kürzel (abi.md § 4).
OHNE_UMLAUT = ("id", "papier", "abhaengig_von")
# Kennungen des Pools, wie sie in bemerkung zitiert werden (Dublette von: …).
KENNUNG = re.compile(r"(?:\d{4}|Beispielaufgaben)M(?:erhoeht|grundlegend)[AB]"
                     r"(?:Analysis|AGLAA1|AGLAA2|Stochastik)(?:WTR|CAS|MMS)?\d*(?:-\d*[a-z]?)?")
PAPIER = re.compile(r"(\d{4})-(be|bb|bebb)-(gk|lk|ea)(-(cas|mms))?")
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


def geltung():
    """Geltungstabelle aus abitur-vokabular.md § 3: Thema × Zielprüfung, ja/nein.
    Liefert (Zielprüfungen, {thema: Menge der Zielprüfungen mit ja})."""
    profil = abschnitt(lies(VOKABULAR), "Geltung", VOKABULAR)
    m = re.search(r"^\| Thema \|(.+?)\|\s*\n\|[-| ]+\|\s*\n((?:\|.*\|\s*\n)+)", profil, re.M)
    if not m:
        sys.exit(f"{VOKABULAR}: Geltungstabelle nicht gefunden.")
    ziele = [z.strip() for z in m.group(1).split("|") if z.strip()]
    tab = {}
    for zeile in m.group(2).strip().splitlines():
        zellen = [c.strip() for c in zeile.strip().strip("|").split("|")]
        if len(zellen) != len(ziele) + 1:
            sys.exit(f"{VOKABULAR}: Geltungszeile hat {len(zellen)} Zellen: {zeile}")
        thema, werte = zellen[0], zellen[1:]
        if any(w not in ("ja", "nein") for w in werte):
            sys.exit(f"{VOKABULAR}: Geltung muss ja oder nein sein: {zeile}")
        tab[thema] = {z for z, w in zip(ziele, werte) if w == "ja"}
    alle = {t for liste in THEMEN.values() for t in liste}
    fehlt = sorted(alle - set(tab))
    if fehlt:
        sys.exit(f"{VOKABULAR}: Themen ohne Geltungszeile: {fehlt}")
    fremd = sorted(set(tab) - alle)
    if fremd:
        sys.exit(f"{VOKABULAR}: Geltungszeilen ohne Thema in der Liste: {fremd}")
    return ziele, tab


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


# typ → (leitidee, thema) aus abitur-typen.csv und NEUE_TYPEN; füllt main(). Seit v0.4
# (Lauf 13) trägt jede Zeile leitidee und thema ihres Typs, der Schnitt liest sie hier.
TYP_THEMA = {}


def pruefe_thema(z, a):
    """Zeilenthema = Typthema (abitur-vokabular.md § 4, Entscheidung 16.09.2026)."""
    if z["typ"] in TYP_THEMA:
        a(TYP_THEMA[z["typ"]] == (z["leitidee"], z["thema"]),
          f"{z['id']}: leitidee/thema ({z['leitidee']}, {z['thema']}) weichen vom Typ ab "
          f"{TYP_THEMA[z['typ']]}")


def niveau_von(papier):
    """Niveau aus dem papier-Kürzel: gk, lk oder ea (abi.md § 4)."""
    m = PAPIER.fullmatch(papier)
    return m.group(3) if m else ""


def ziele_von(papier):
    """Zielprüfungen, gegen die ein Heft gemessen wird (abitur-vokabular.md § 3, Entscheidung
    des Lehrers 16.09.2026): be-gk → be-gk, be-lk → be-lk, bb-ea → bb-ea; gemeinsame Hefte
    bebb-gk → be-gk und bb-gk, bebb-lk → be-lk und bb-ea. Eine Zeile liegt in der Geltung des
    Hefts, wenn ihr Thema in mindestens einer dieser Spalten gilt; der Bericht nennt beide."""
    m = PAPIER.fullmatch(papier)
    if not m:
        return []
    land, niveau = m.group(2), m.group(3)
    if land == "bebb":
        return ["be-gk", "bb-gk"] if niveau == "gk" else ["be-lk", "bb-ea"]
    return [f"{land}-{niveau}"]


def in_geltung(z, ziele=None):
    """True, wenn das Thema der Zeile in mindestens einer Zielprüfung ihres Hefts gilt."""
    ziele = ziele or ziele_von(z["papier"])
    return any(ziel in GELTUNG.get(z["thema"], set()) for ziel in ziele)


HEAD, VOK, LEITIDEEN, THEMEN = vokabular()
ZIELE, GELTUNG = geltung()
KLASSEN = klassen()
HANDLUNG = handlungen()

# ======================================================== AB HIER JE HEFT
ZEILEN = []


def row(**kw):
    z = {k: "" for k in HEAD}
    z.update(jahr=KONFIG["jahr"], papier=KONFIG["papier"], stern="")
    unbekannt = set(kw) - set(HEAD)
    if unbekannt:
        sys.exit(f"unbekanntes Feld: {sorted(unbekannt)}")
    z.update(kw)
    if not z["hilfsmittel"]:
        z["hilfsmittel"] = "nein" if z["block"] == "A" else "ja"
    ZEILEN.append(z)


# ============================================================ ZEILEN JE HEFT
# Heft 2020-be-gk (Stark-Band zum Abitur 2021, Berlin Grundkurs; 49 Seiten A5 mit
# Tipps und Verlagslösungen, Textebene; Auftrag B, 17.09.2026). Hilfsmittelfreier
# Teil mit fünf Einheiten zu je 5 BE, Teil B mit Wahl in allen drei Sachgebieten
# (Analysis 35 statt 40 BE wie 2019). Pool 2020 grundlegend: Teil A erfasst
# (Analysis 2 = Analysis 1.2, Stochastik = Stochastik 1.1 wortgleich), Teil B
# Reserve (4.2 Unternehmen: Aufgabenteil 2 wortgleich mit Stochastik WTR 1
# Aufgabe 2, Aufgabenteil 1 mit anderen Zahlen – Vormerkungen). Landesaufgaben:
# Analysis 1, Geometrie 1 und 2 (Teil A), 2.1 Exponentialfunktion, 2.2
# Teststrecke, 3.1 Ebenen, 3.2 Theater, 4.1 Würfel. Verlagslösungen sind kein
# Erwartungshorizont: ergebnis ohne „amtlich“, afb_amtlich der Landeszeilen leer.
# ---- Aufgabe 1: hilfsmittelfreier Teil (Seite 1), 5 × 5 BE
row(id="2020-be-gk-A1.1a", block="A", aufgabe="1.1", titel="Analysis 1", teilaufgabe="a", seite="1", punkte="1",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Funktion aus einer gegebenen Stammfunktion durch Ableiten bestimmen", typ_neben="",
    stichwoerter="F(x) = 2x⁴ − x + 1|f = F'|f(x) = 8x³ − 1",
    voraussetzungen="Stammfunktion heißt F' = f|Potenzregel",
    format="Kurzantwort", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="F(x) = 2x⁴ − x + 1 ist eine Stammfunktion einer Funktion f",
    gesucht="Gleichung von f",
    verfahren="F ableiten",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(x) = 8x³ − 1",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="F aufleiten statt ableiten",
    bemerkung="Landesaufgabe (nicht im Pool 2020). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-A1.1b", block="A", aufgabe="1.1", titel="Analysis 1", teilaufgabe="b", seite="1", punkte="4",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktionen mit vorgegebenem vertikalem Abstand zum Graphen einer Stammfunktion angeben", typ_neben="",
    stichwoerter="alle Stammfunktionen 2x⁴ − x + C|Abstand 3 LE in y-Richtung|C = 4 und C = −2",
    voraussetzungen="Stammfunktionen unterscheiden sich um eine Konstante|Verschiebung in y-Richtung",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="F(x) = 2x⁴ − x + 1 ist eine Stammfunktion von f; f(x) = 8x³ − 1 (aus a)",
    gesucht="Gleichung aller Stammfunktionen von f; die zwei Stammfunktionen, deren Graphen von dem von F den Abstand 3 LE in Richtung der y-Achse haben",
    verfahren="F + C; C so wählen, dass der Graph um 3 nach oben bzw. unten verschoben ist",
    schritte="2", zahlenraum="ganz|negativ", einheiten="LE", abhaengig_von="2020-be-gk-A1.1a",
    ergebnis="Alle Stammfunktionen: 2x⁴ − x + C, C ∈ IR; gesucht F₁(x) = 2x⁴ − x + 4 und F₂(x) = 2x⁴ − x − 2",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur eine der beiden Stammfunktionen nennen oder den Abstand auf x beziehen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-A1.3a", block="A", aufgabe="1.3", titel="Geometrie 1", teilaufgabe="a", seite="1", punkte="3",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Kollinearität dreier Punkte über die Verbindungsvektoren nachweisen", typ_neben="",
    stichwoerter="AB = (1 | 2 | 1), AC = (−2 | −4 | −2) = −2 · AB|g: x = (3 | 4 | −1) + r · (1 | 2 | 1)|C für r = −2",
    voraussetzungen="Verbindungsvektoren|Kollinearität oder Punktprobe",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(3 | 4 | −1), B(4 | 6 | 0), C(1 | 0 | −3)",
    gesucht="Nachweis, dass A, B und C auf einer Geraden g liegen",
    verfahren="Gerade durch A und B aufstellen und C per Punktprobe prüfen (r = −2), oder AC = −2 · AB",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="g: x = (3 | 4 | −1) + r · (1 | 2 | 1); C liegt auf g für r = −2 (AC = −2 · AB), also liegen alle drei Punkte auf g",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur zwei Koordinaten bei der Punktprobe prüfen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-A1.3b", block="A", aufgabe="1.3", titel="Geometrie 1", teilaufgabe="b", seite="1", punkte="2",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Zweiten Punkt auf einer Geraden mit gleichem Abstand zu einem Geradenpunkt über den Richtungsvektor angeben", typ_neben="",
    stichwoerter="D = A − AB|r = −1 in g|D(2 | 2 | −2)",
    voraussetzungen="Parameter einer Geraden als Abstandsmaß",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(3 | 4 | −1), B(4 | 6 | 0) auf g: x = (3 | 4 | −1) + r · (1 | 2 | 1) (aus a)",
    gesucht="Koordinaten eines weiteren Punktes D auf g mit demselben Abstand zu A wie B",
    verfahren="AB von A abziehen (r = −1)",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2020-be-gk-A1.3a",
    ergebnis="D(2 | 2 | −2)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="D = B (gleicher Abstand, aber nicht weiterer Punkt) oder r = 2 (doppelter Abstand)",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-A1.4a", block="A", aufgabe="1.4", titel="Geometrie 2", teilaufgabe="a", seite="1", punkte="1",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Streckenlänge im Raum berechnen", typ_neben="",
    stichwoerter="AB = (−3 | 4 | 0)|Betrag 5",
    voraussetzungen="Betrag eines Vektors",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(7 | −3 | 5), B(4 | 1 | 5)",
    gesucht="Abstand der Punkte A und B",
    verfahren="Betrag des Verbindungsvektors",
    schritte="1", zahlenraum="ganz|negativ", einheiten="LE", abhaengig_von="",
    ergebnis="|AB| = √(9 + 16 + 0) = 5 LE",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Koordinaten addieren statt subtrahieren",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-bb-ea). Eigene Rechnung.")
row(id="2020-be-gk-A1.4b", block="A", aufgabe="1.4", titel="Geometrie 2", teilaufgabe="b", seite="1", punkte="4",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Parameter einer Ecke aus dem Flächeninhalt eines gleichschenkligen Dreiecks bestimmen", typ_neben="",
    stichwoerter="Höhe h = 2 · 10 / 5 = 4|Basis AB parallel zur x-y-Ebene (z = 5), Höhe senkrecht dazu|Mittelpunkt M(5,5 | −1 | 5)|C(5,5 | −1 | 9) oder C(5,5 | −1 | 1)",
    voraussetzungen="Dreiecksfläche aus Basis und Höhe|Mittelpunkt einer Strecke|Höhe im gleichschenkligen Dreieck halbiert die Basis",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(7 | −3 | 5), B(4 | 1 | 5), |AB| = 5 (aus a)",
    gesucht="Koordinaten eines möglichen Punktes C, sodass ABC gleichschenklig mit Basis AB ist, den Flächeninhalt 10 FE hat und senkrecht zur x-y-Ebene steht",
    verfahren="Höhe aus A = 1/2 · g · h; C senkrecht (in z-Richtung) über oder unter dem Mittelpunkt von AB im Abstand h",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="FE|LE", abhaengig_von="2020-be-gk-A1.4a",
    ergebnis="h = 4; M(5,5 | −1 | 5); C(5,5 | −1 | 9) (oder C(5,5 | −1 | 1))",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="C über A oder B statt über der Basismitte setzen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2022-ga-A: Ecke aus dem Flächeninhalt eines gleichschenkligen Dreiecks); hier ohne Parameter, mit der Lagebedingung senkrecht zur x-y-Ebene. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.1 Exponentialfunktion (Seiten 8–9), 35 BE, Landesaufgabe
EF = "f(x) = (6x − 3) · e^(−x), x ∈ IR"
EF_SK = "Anlage Seite 9: Koordinatensystem auf Gitter, x von 0 bis 7, y von −3 bis 9, mit der Skizze des Graphen von f' (startet bei 9, fällt steil, Nullstelle bei 1,5, Minimum ≈ −0,6 bei x ≈ 2,5, nähert sich von unten der x-Achse); der Graph von f ist in e einzuzeichnen"
row(id="2020-be-gk-B2.1a", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="a", seite="8", punkte="2",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstelle und y-Achsenschnittpunkt eines Produkts mit e-Funktion angeben", typ_neben="",
    stichwoerter="6x − 3 = 0 ⇔ x = 0,5 (e-Faktor nie null)|f(0) = −3|S_x(0,5 | 0), S_y(0 | −3)",
    voraussetzungen="Satz vom Nullprodukt|e-Funktion positiv",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EF,
    gesucht="Schnittpunkte des Graphen von f mit den Koordinatenachsen",
    verfahren="Ersten Faktor null setzen; f(0) berechnen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="S_x(0,5 | 0), S_y(0 | −3)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="e^(−x) = 0 als Nullstelle ansetzen",
    bemerkung="Landesaufgabe (nicht im Pool 2020). Typ wiederverwendet (2024-bebb-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.1b", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="b", seite="8", punkte="2",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben", typ_neben="",
    stichwoerter="x → +∞: e^(−x) dominiert, f(x) → 0|x → −∞: (6x − 3) → −∞ und e^(−x) → +∞, f(x) → −∞",
    voraussetzungen="Grenzverhalten von Polynom · e-Funktion",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EF,
    gesucht="Verhalten der Funktionswerte für x → +∞ und x → −∞",
    verfahren="Dominanz des Exponentialfaktors",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f(x) → 0 für x → +∞; f(x) → −∞ für x → −∞",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="für x → −∞ wegen e^(−x) → ∞ das Vorzeichen des ersten Faktors übersehen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2023-bebb-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.1c", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="c", seite="8", punkte="4",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen",
    typ_neben="Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen",
    stichwoerter="Produktregel: 6 · e^(−x) + (6x − 3) · (−e^(−x)) = (−6x + 9) · e^(−x)|f'(x) = 0 ⇔ x = 1,5|f(1,5) = 6 · e^(−1,5) ≈ 1,34",
    voraussetzungen="Produkt- und Kettenregel|Satz vom Nullprodukt",
    format="Rechnung", operator="Weisen Sie nach|Ermitteln Sie", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EF + "; der Graph hat genau einen lokalen Extrempunkt",
    gesucht="Nachweis von f'(x) = (−6x + 9) · e^(−x); Koordinaten des Extrempunkts",
    verfahren="Produktregel anwenden und ausklammern; f' = 0 lösen, Funktionswert berechnen (Art nicht verlangt)",
    schritte="4", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = (−6x + 9) · e^(−x); Extrempunkt P(1,5 | 6 · e^(−1,5)) ≈ P(1,5 | 1,34)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="innere Ableitung −1 von e^(−x) vergessen",
    bemerkung="Landesaufgabe. Typen wiederverwendet (2021-ea-A, 2025-ga-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.1d", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="d", seite="8|9", punkte="3",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Art eines Extrempunkts aus dem Vorzeichenwechsel am Ableitungsgraphen begründen", typ_neben="",
    stichwoerter="f' > 0 für x < 1,5, f' < 0 für x > 1,5 (Skizze)|Vorzeichenwechsel + nach −|Hochpunkt",
    voraussetzungen="Monotonie aus dem Vorzeichen der Ableitung",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=EF_SK, kontext="ohne", textumfang="kurz",
    gegeben=EF + "; Skizze des Graphen von f' in der Anlage; Extremstelle x = 1,5 (aus c)",
    gesucht="Begründung mithilfe der Skizze, dass der Extrempunkt ein Hochpunkt ist",
    verfahren="Vorzeichen von f' links und rechts von 1,5 ablesen",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="2020-be-gk-B2.1c",
    ergebnis="Der Graph von f' liegt für x < 1,5 oberhalb und für x > 1,5 unterhalb der x-Achse: f steigt vor 1,5 und fällt danach, also Hochpunkt",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="mit f'' argumentieren, obwohl die Skizze verlangt ist",
    bemerkung="Landesaufgabe. Eigene Überlegung; Verlagslösung argumentiert gleich.")
row(id="2020-be-gk-B2.1e", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="e", seite="8|9", punkte="3",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen", typ_neben="",
    stichwoerter="Punkte S_y(0 | −3), S_x(0,5 | 0), Hochpunkt (1,5 | 1,34)|Annäherung an die x-Achse von oben|x ≥ 0",
    voraussetzungen="Ergebnisse aus a bis d zusammenführen",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=EF_SK, kontext="ohne", textumfang="kurz",
    gegeben=EF + "; Achsenschnittpunkte, Grenzverhalten und Hochpunkt aus a bis d; Koordinatensystem der Anlage mit dem Graphen von f'",
    gesucht="Graph von f für x ≥ 0 in der Anlage",
    verfahren="Bekannte Punkte eintragen und den Verlauf mit dem Grenzverhalten verbinden",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="2020-be-gk-B2.1c",
    ergebnis="Graph von 0 bei −3 steigend durch (0,5 | 0) zum Hochpunkt (1,5 | 1,34), danach fallend gegen die x-Achse",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="den Graphen von f' als f zeichnen oder die Nullstelle 0,5 auslassen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-be-gk). Eigene Lösung.")
row(id="2020-be-gk-B2.1f", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="f", seite="8", punkte="4",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung und Schnittwinkel der Tangente mit der x-Achse bestimmen", typ_neben="",
    stichwoerter="f(1) = 3/e, f'(1) = 3/e|t(x) = 3/e · x (Ursprungsgerade)|tan α = 3/e, α ≈ 47,8°",
    voraussetzungen="Tangente über Punkt und Steigung|Steigungswinkel über den Tangens",
    format="Rechnung", operator="Ermitteln Sie|Berechnen Sie", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EF + "; f'(x) = (−6x + 9) · e^(−x); Punkt P(1 | f(1))",
    gesucht="Gleichung der Tangente t in P; Schnittwinkel der Tangente mit der x-Achse",
    verfahren="Steigung f'(1), y-Achsenabschnitt aus P; α = arctan(m)",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="°", abhaengig_von="",
    ergebnis="t(x) = 3/e · x ≈ 1,10 · x (geht durch den Ursprung); α = arctan(3/e) ≈ 47,8°",
    zwischenergebnis="f(1) = f'(1) = 3/e ≈ 1,104", niveau_geschaetzt="II",
    fehlerquelle="n = f(1) setzen statt aus der Punktbedingung berechnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2026-ga-B). Eigene Rechnung, mit sympy bestätigt (47,82°).")
row(id="2020-be-gk-B2.1g", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="g", seite="8", punkte="5",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen", typ_neben="",
    stichwoerter="d(x) = f(x) − f'(x) = (12x − 12) · e^(−x)|d'(x) = (24 − 12x) · e^(−x) = 0 ⇔ x = 2|d(2) = 12 · e^(−2) ≈ 1,62",
    voraussetzungen="Differenzfunktion|Produktregel|notwendige Bedingung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=EF + "; f'(x) = (−6x + 9) · e^(−x); im Bereich x ≥ 1 gibt es eine Stelle x_M maximalen senkrechten Abstands der Graphen von f und f'; Nachweis des Maximums nicht verlangt",
    gesucht="x_M und der Abstand der Graphen an dieser Stelle",
    verfahren="Differenz d = f − f' bilden (f liegt für x > 1 oberhalb), d' = 0 lösen, d(x_M) berechnen",
    schritte="4", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="2020-be-gk-B2.1c",
    ergebnis="x_M = 2; Abstand d(2) = 12 · e^(−2) ≈ 1,62",
    zwischenergebnis="d(x) = (12x − 12) · e^(−x)|d'(x) = (24 − 12x) · e^(−x)", niveau_geschaetzt="II",
    fehlerquelle="Abstand als f'(x) − f(x) mit negativem Vorzeichen führen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-be-gk 1.1 g); hier zwischen Graph und Ableitungsgraph. Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.1h", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="h", seite="8", punkte="3",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion durch Ableiten nachweisen",
    typ_neben="Stammfunktion mit einer Wertebedingung bestimmen",
    stichwoerter="F' = f zeigen (Produktregel)|H = F + C|H(0) = −3 + C = 17 ⇔ C = 20",
    voraussetzungen="Definition der Stammfunktion|Integrationskonstante",
    format="Begründung|Kurzantwort", operator="Beschreiben Sie|Geben Sie an", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EF + "; F(x) = (−6x − 3) · e^(−x)",
    gesucht="Beschreibung, wie nachgewiesen wird, dass F Stammfunktion von f ist; Stammfunktion H mit H(0) = 17",
    verfahren="F ableiten und mit f vergleichen; H = F + C mit C aus H(0) = 17",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="F ableiten (Produktregel) und zeigen, dass F'(x) = f(x); H(x) = (−6x − 3) · e^(−x) + 20",
    zwischenergebnis="F(0) = −3", niveau_geschaetzt="II",
    fehlerquelle="H = F + 17 setzen ohne F(0) zu beachten",
    bemerkung="Landesaufgabe. Typen wiederverwendet (2020-ea-A, 2026-ea-A). Eigene Rechnung, mit sympy bestätigt (F' = f).")
row(id="2020-be-gk-B2.1i", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="i", seite="8", punkte="4",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph, x-Achse und zwei senkrechten Geraden mit vorgegebener Stammfunktion berechnen", typ_neben="",
    stichwoerter="Integral von 1 bis 5 über f = F(5) − F(1)|−33 · e^(−5) + 9 · e^(−1) ≈ 3,09|f > 0 auf [1; 5]",
    voraussetzungen="Hauptsatz|Vorzeichen des Integranden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EF + "; Stammfunktion F(x) = (−6x − 3) · e^(−x) (aus h); Fläche zwischen Graph, x-Achse, x = 1 und x = 5",
    gesucht="Flächeninhalt",
    verfahren="Bestimmtes Integral mit F, da f auf [1; 5] positiv ist",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="FE", abhaengig_von="2020-be-gk-B2.1h",
    ergebnis="A = F(5) − F(1) = −33 · e^(−5) + 9 · e^(−1) ≈ 3,09 FE",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen von F(1) = −9/e falsch behandeln",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt (3,0886).")
row(id="2020-be-gk-B2.1j", block="B", aufgabe="2.1", titel="Exponentialfunktion", teilaufgabe="j", seite="8", punkte="5",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Stelle mit parallelen Tangenten an Graph und Ableitungsgraph über f' = f'' ermitteln", typ_neben="",
    stichwoerter="Steigung an f: f'(x), an f': f''(x) = (6x − 15) · e^(−x)|f'(x) = f''(x) ⇔ −6x + 9 = 6x − 15 ⇔ x = 2|x_T = 2",
    voraussetzungen="Ableitung des Ableitungsgraphen ist f''|Produktregel|Gleichung lösen",
    format="Rechnung", operator="Untersuchen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EF + "; f'(x) = (−6x + 9) · e^(−x)",
    gesucht="ob es eine Stelle x_T gibt, an der die Tangente an den Graphen von f parallel zur Tangente an den Graphen von f' ist",
    verfahren="f'' bilden, f'(x) = f''(x) lösen (e-Faktor kürzen)",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2020-be-gk-B2.1c",
    ergebnis="Ja: f''(x) = (6x − 15) · e^(−x); f' = f'' genau für x_T = 2",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="Parallelität als f(x) = f'(x) ansetzen",
    bemerkung="Landesaufgabe. Enge Fassung: die Einsicht, dass die Tangentensteigung an f' durch f'' gegeben ist, muss selbst gefunden werden – III. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.2 Teststrecke (Seiten 16–17), 35 BE, Landesaufgabe
TS = "f(x) = −0,01 · (x − 8) · (x + 1)², x ∈ IR"
TS2 = "f(x) = −1/100 x³ + 3/50 x² + 3/20 x + 2/25 (ausmultiplizierte Form aus b)"
TS_SK = "Anlage Seite 17: Koordinatensystem auf Millimetergitter, x von −2 bis 11, y von −2 bis 2 (Schrittweite 0,5), leer; Abbildung 1 auf Seite 16: perspektivische Skizze der Teststrecke (Profil mit Bogen) ohne Werte"
row(id="2020-be-gk-B2.2a", block="B", aufgabe="2.2", titel="Teststrecke", teilaufgabe="a", seite="16", punkte="2",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstellen aus der faktorisierten Form angeben", typ_neben="",
    stichwoerter="x = 8 und x = −1 (doppelt)",
    voraussetzungen="Satz vom Nullprodukt",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=TS,
    gesucht="Nullstellen von f",
    verfahren="Faktoren null setzen",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="x₁ = 8, x₂ = −1 (doppelte Nullstelle)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen der Nullstellen aus (x − 8) und (x + 1) vertauschen",
    bemerkung="Landesaufgabe (nicht im Pool 2020). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.2b", block="B", aufgabe="2.2", titel="Teststrecke", teilaufgabe="b", seite="16", punkte="5",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Termgleichheit zweier Darstellungen einer ganzrationalen Funktion durch Ausmultiplizieren nachweisen",
    typ_neben="Grenzverhalten einer ganzrationalen Funktion angeben",
    stichwoerter="(x − 8)(x² + 2x + 1) = x³ − 6x² − 15x − 8|mal −1/100|x → +∞: f → −∞, x → −∞: f → +∞ (Grad 3, Leitkoeffizient negativ)",
    voraussetzungen="binomische Formel|Polynommultiplikation|Grenzverhalten über den höchsten Grad",
    format="Rechnung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=TS,
    gesucht="Nachweis von f(x) = −1/100 x³ + 3/50 x² + 3/20 x + 2/25; Verhalten für x → +∞ und x → −∞",
    verfahren="Ausmultiplizieren; Grenzverhalten am Summanden höchsten Grades",
    schritte="3", zahlenraum="Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f(x) = −1/100 · (x³ − 6x² − 15x − 8) = −1/100 x³ + 3/50 x² + 3/20 x + 2/25; f(x) → −∞ für x → +∞, f(x) → +∞ für x → −∞",
    zwischenergebnis="(x + 1)² = x² + 2x + 1", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichenfehler beim Ausmultiplizieren mit (x − 8)",
    bemerkung="Landesaufgabe. Termumformung als Fertigkeit unter Gleichungen lösen abgelegt (kein Thema für Termumformungen in der Liste). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.2c", block="B", aufgabe="2.2", titel="Teststrecke", teilaufgabe="c", seite="16", punkte="9",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Lage und Art aller lokalen Extrempunkte bestimmen", typ_neben="",
    stichwoerter="f'(x) = −3/100 x² + 3/25 x + 3/20 = 0 ⇔ x² − 4x − 5 = 0 ⇔ x = −1, x = 5|f''(x) = −3/50 x + 3/25|f''(−1) = 9/50 > 0: Tiefpunkt (−1 | 0)|f''(5) = −9/50 < 0: Hochpunkt (5 | 1,08)",
    voraussetzungen="Ableitungen|p-q-Formel|hinreichende Bedingung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=TS2,
    gesucht="Lage und Art der Extrempunkte des Graphen von f",
    verfahren="f' = 0 lösen, f'' an den Stellen auswerten, Funktionswerte berechnen",
    schritte="6", zahlenraum="Bruch|dezimal|negativ", einheiten="", abhaengig_von="2020-be-gk-B2.2b",
    ergebnis="Tiefpunkt T(−1 | 0), Hochpunkt H(5 | 27/25) = H(5 | 1,08)",
    zwischenergebnis="f'(x) = −3/100 x² + 3/25 x + 3/20|f''(x) = −3/50 x + 3/25", niveau_geschaetzt="II",
    fehlerquelle="beim Normieren der quadratischen Gleichung die Vorzeichen kippen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-be-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.2d", block="B", aufgabe="2.2", titel="Teststrecke", teilaufgabe="d", seite="16|17", punkte="4",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen", typ_neben="",
    stichwoerter="Graph von f: f(−2) = 0,1, Tiefpunkt (−1 | 0), Hochpunkt (5 | 1,08), Nullstelle 8|Graph von f': nach unten geöffnete Parabel mit Nullstellen −1 und 5, Scheitel (2 | 0,27)",
    voraussetzungen="Ergebnisse aus a bis c|Ableitungsgraph als Parabel",
    format="Zeichnen", operator="Skizzieren Sie", antwort="Grafik",
    material="Koordinatensystem", skizze=TS_SK, kontext="ohne", textumfang="kurz",
    gegeben=TS2 + "; f'(x) = −3/100 x² + 3/25 x + 3/20; Bereich −2 ≤ x ≤ 8; leeres Koordinatensystem in der Anlage",
    gesucht="Graphen von f und f' im Bereich −2 ≤ x ≤ 8",
    verfahren="Nullstellen, Extrempunkte und Randwerte eintragen und verbinden; f' als Parabel durch die Extremstellen von f",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="2020-be-gk-B2.2c",
    ergebnis="f: von (−2 | 0,1) über den Tiefpunkt (−1 | 0) steigend zum Hochpunkt (5 | 1,08), dann fallend zur Nullstelle 8; f': Parabel mit Nullstellen −1 und 5, Scheitel (2 | 0,27), negativ außerhalb",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Extremstellen von f nicht als Nullstellen von f' zeichnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-be-gk). Eigene Lösung, Werte mit sympy bestätigt.")
row(id="2020-be-gk-B2.2e", block="B", aufgabe="2.2", titel="Teststrecke", teilaufgabe="e", seite="16", punkte="2",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Wendepunkt des Funktionsgraphen aus dem Extrempunkt des Ableitungsgraphen erläutern", typ_neben="",
    stichwoerter="Hochpunkt von f' bei x = 2|f''(2) = 0 mit Vorzeichenwechsel|Wendepunkt von f bei x = 2, dort größte Steigung",
    voraussetzungen="Zusammenhang f', f'' und Wendepunkt",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Der Graph von f' hat einen Hochpunkt (bei x = 2, aus d)",
    gesucht="Schlussfolgerungen für den Graphen von f",
    verfahren="Extremstelle von f' ist Nullstelle von f'' mit Vorzeichenwechsel",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="An der Stelle des Hochpunkts von f' hat f einen Wendepunkt (Krümmungswechsel von links nach rechts); dort ist die Steigung von f am größten",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="auf einen Extrempunkt von f schließen",
    bemerkung="Landesaufgabe. Eigene Überlegung; Verlagslösung stimmt überein.")
row(id="2020-be-gk-B2.2f", block="B", aufgabe="2.2", titel="Teststrecke", teilaufgabe="f", seite="16|17", punkte="3",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Gerade als Tangente in einem vorgegebenen Punkt über Funktionswert und Ableitung nachweisen",
    typ_neben="Tangente mit gegebener Gleichung in die Abbildung einzeichnen",
    stichwoerter="f'(6) = −0,21, f(6) = 0,98|t(x) = −0,21x + 2,24|Nullstelle von t bei x ≈ 10,67",
    voraussetzungen="Tangente über Steigung und Punkt|Gerade zeichnen",
    format="Rechnung|Zeichnen", operator="Weisen Sie nach|Zeichnen Sie", antwort="Term|Grafik",
    material="Koordinatensystem", skizze=TS_SK, kontext="Straßenbau / Teststrecke", textumfang="mittel",
    gegeben=TS2 + "; Profillinie der Teststrecke für −1 ≤ x ≤ 8, 1 LE = 1 m, Fahrbahn 5 m breit; Tangente t im Punkt P(6 | f(6)) soll den Knick bei x = 8 vermeiden",
    gesucht="Nachweis von t(x) = −0,21x + 2,24; Tangente in die Anlage einzeichnen",
    verfahren="f'(6) und f(6) berechnen, n aus P; Gerade durch P und die Nullstelle 10,67 zeichnen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="m", abhaengig_von="2020-be-gk-B2.2c",
    ergebnis="f'(6) = −21/100 = −0,21, f(6) = 49/50 = 0,98, also t(x) = −0,21x + 2,24; Nullstelle bei x = 32/3 ≈ 10,67",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="f(6) falsch aus der faktorisierten Form berechnen",
    bemerkung="Landesaufgabe. Typen wiederverwendet (2026-bb-gk, 2025-ea-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.2g", block="B", aufgabe="2.2", titel="Teststrecke", teilaufgabe="g", seite="16", punkte="5",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Querschnittsfläche zwischen Tangente und Graph als Dreieck minus Integral berechnen und mit der Breite zum Volumen umrechnen", typ_neben="",
    stichwoerter="Dreieck unter t von 6 bis 10,67: 1/2 · 4,67 · 0,98 ≈ 2,29|Integral von 6 bis 8 über f = 1,18|Querschnitt ≈ 1,11 m²|Volumen ≈ 1,11 · 5 ≈ 5,5 m³",
    voraussetzungen="Dreiecksfläche|bestimmtes Integral|Volumen = Querschnitt · Breite",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=TS_SK, kontext="Straßenbau / Teststrecke", textumfang="mittel",
    gegeben=TS2 + "; Tangente t(x) = −0,21x + 2,24 (aus f) mit Nullstelle 10,67; Fahrbahn 5 m breit; neue Aufschüttung unterhalb von t im Bereich 6 ≤ x ≤ 10,67 (zwischen t und dem Graphen bzw. der x-Achse)",
    gesucht="benötigte Erde in Kubikmetern",
    verfahren="Fläche unter t (Dreieck mit Basis 4,67 und Höhe 0,98) minus Fläche unter f von 6 bis 8, mal Breite 5",
    schritte="4", zahlenraum="dezimal", einheiten="m|m²|m³", abhaengig_von="2020-be-gk-B2.2f",
    ergebnis="Querschnitt ≈ 2,29 − 1,18 = 1,11 m² (exakt ≈ 1,107); Volumen ≈ 5,5 m³ (mit gerundeten Werten 5,55, exakt 5,53)",
    zwischenergebnis="Integral von 6 bis 8 über f = 1,18", niveau_geschaetzt="III",
    fehlerquelle="das Integral von 6 bis 10,67 über f bilden (f ist dort teils negativ) oder die Breite vergessen",
    bemerkung="Landesaufgabe. Enge Fassung: Zerlegung der Fläche in Dreieck und Integral selbst finden und mit der Breite zum Volumen zusammenführen – III. Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B2.2h", block="B", aufgabe="2.2", titel="Teststrecke", teilaufgabe="h", seite="17", punkte="5",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt der Tangente mit vorgegebener Steigung berechnen", typ_neben="",
    stichwoerter="größte Steigung f'(2) = 0,27|f'(x) = −0,27 ⇔ x² − 4x − 14 = 0|x = 2 + √18 ≈ 6,24 (x > 5)",
    voraussetzungen="Ableitungswert an der Wendestelle|quadratische Gleichung|Auswahl der Lösung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Straßenbau / Teststrecke", textumfang="mittel",
    gegeben=TS2 + "; f'(x) = −3/100 x² + 3/25 x + 3/20; die Profillinie hat bei x = 2 den größten Steigungswinkel (f'(2) = 0,27); gesucht eine Tangente mit x > 5, deren Gefälle ebenso groß ist",
    gesucht="Stelle x > 5, an der die Tangente die Steigung −0,27 hat",
    verfahren="f'(x) = −0,27 lösen, Lösung x > 5 wählen",
    schritte="3", zahlenraum="dezimal|Wurzel|negativ", einheiten="m", abhaengig_von="2020-be-gk-B2.2c",
    ergebnis="x = 2 + √18 ≈ 6,24 (die zweite Lösung 2 − √18 ≈ −2,24 entfällt)",
    zwischenergebnis="f'(2) = 27/100", niveau_geschaetzt="II",
    fehlerquelle="f'(x) = 0,27 (Steigung statt Gefälle) lösen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2026-ea-B). Eigene Rechnung, mit sympy bestätigt (6,2426).")
# ---- Aufgabe 3.1 Ebenen (Seite 25), 20 BE, Landesaufgabe
EB = "E₁: x = (3 | 0 | 0) + r · (−3 | 9 | 0) + s · (−3 | 0 | 4), r, s ∈ IR; E₂: 6x + 2y + 9z = 18"
row(id="2020-be-gk-B3.1a", block="B", aufgabe="3.1", titel="Ebenen", teilaufgabe="a", seite="25", punkte="3",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="Normalenvektor aus dem Kreuzprodukt (36 | 12 | 27) ~ (12 | 4 | 9)|Stützpunkt (3 | 0 | 0) einsetzen|12x + 4y + 9z = 36",
    voraussetzungen="Kreuzprodukt oder Eliminieren der Parameter|Normalenform",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EB + "; Kontrollergebnis E₁: 12x + 4y + 9z = 36",
    gesucht="Koordinatenform von E₁",
    verfahren="Normalenvektor über das Kreuzprodukt der Spannvektoren, d aus dem Stützpunkt",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="E₁: 12x + 4y + 9z = 36",
    zwischenergebnis="n = (12 | 4 | 9)", niveau_geschaetzt="II",
    fehlerquelle="Vorzeichenfehler im Kreuzprodukt",
    bemerkung="Landesaufgabe (nicht im Pool 2020). Typ wiederverwendet (2018-ea-A); hier aus der Parameterform. Kontrollergebnis bestätigt (sympy).")
row(id="2020-be-gk-B3.1b", block="B", aufgabe="3.1", titel="Ebenen", teilaufgabe="b", seite="25", punkte="2",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Spurpunkte einer Ebene auf den Koordinatenachsen bestimmen", typ_neben="",
    stichwoerter="x = 36/12 = 3, y = 36/4 = 9, z = 36/9 = 4|(3 | 0 | 0), (0 | 9 | 0), (0 | 0 | 4)",
    voraussetzungen="jeweils zwei Koordinaten null setzen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E₁: 12x + 4y + 9z = 36",
    gesucht="die drei Schnittpunkte von E₁ mit den Koordinatenachsen",
    verfahren="Achsenabschnitte aus der Koordinatengleichung",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2020-be-gk-B3.1a",
    ergebnis="S_x(3 | 0 | 0), S_y(0 | 9 | 0), S_z(0 | 0 | 4)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Koeffizienten statt Quotienten angeben",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2017-bb-ea). Eigene Rechnung.")
row(id="2020-be-gk-B3.1c", block="B", aufgabe="3.1", titel="Ebenen", teilaufgabe="c", seite="25", punkte="3",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen", typ_neben="",
    stichwoerter="d = |12 · 0 + 4 · 0 + 9 · 0 − 36| / √(144 + 16 + 81) = 36/√241 ≈ 2,32",
    voraussetzungen="Hessesche Normalform|Betrag des Normalenvektors",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="E₁: 12x + 4y + 9z = 36",
    gesucht="Abstand von E₁ zum Koordinatenursprung",
    verfahren="Hessesche Normalform mit dem Ursprung",
    schritte="2", zahlenraum="dezimal|Wurzel", einheiten="LE", abhaengig_von="2020-be-gk-B3.1a",
    ergebnis="d = 36/√241 ≈ 2,32 LE",
    zwischenergebnis="|n| = √241", niveau_geschaetzt="I",
    fehlerquelle="den Betrag des Normalenvektors vergessen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2017-bb-ea). Eigene Rechnung, mit sympy bestätigt (2,319).")
row(id="2020-be-gk-B3.1d", block="B", aufgabe="3.1", titel="Ebenen", teilaufgabe="d", seite="25", punkte="4",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Lage zweier Ebenen über die Normalenvektoren entscheiden und Schnittgerade berechnen", typ_neben="",
    stichwoerter="(12 | 4 | 9) und (6 | 2 | 9) nicht kollinear|Parameterform von E₁ in E₂: 18 − 18r + 18s + 18r − 36s = 18 ⇔ s = 0|g: x = (3 | 0 | 0) + r · (−3 | 9 | 0)",
    voraussetzungen="Kollinearität von Normalenvektoren|Einsetzen der Parameterform",
    format="Begründung|Rechnung", operator="Begründen Sie|Ermitteln Sie", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=EB + " mit E₁: 12x + 4y + 9z = 36",
    gesucht="Begründung, dass E₁ und E₂ nicht parallel sind; Schnittgerade von E₁ und E₂",
    verfahren="Normalenvektoren vergleichen; x, y, z aus der Parameterform von E₁ in E₂ einsetzen, s = 0, in E₁ einsetzen",
    schritte="4", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2020-be-gk-B3.1a",
    ergebnis="Nicht parallel, da (12 | 4 | 9) kein Vielfaches von (6 | 2 | 9) ist; Schnittgerade g: x = (3 | 0 | 0) + r · (−3 | 9 | 0), r ∈ IR (die Spurgerade von E₁ in der x-y-Ebene)",
    zwischenergebnis="s = 0", niveau_geschaetzt="II",
    fehlerquelle="beide Koordinatengleichungen gleichsetzen und nicht nach einem Parameter auflösen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B3.1e", block="B", aufgabe="3.1", titel="Ebenen", teilaufgabe="e", seite="25", punkte="3",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Pyramidenvolumen aus Grundfläche und Höhe berechnen", typ_neben="",
    stichwoerter="Grundfläche Dreieck OAB rechtwinklig: 1/2 · 3 · 9 = 13,5|Höhe 4 (z-Koordinate von C)|V = 1/3 · 13,5 · 4 = 18",
    voraussetzungen="Pyramidenvolumen|rechtwinkliges Dreieck in der Koordinatenebene",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Pyramide mit den Eckpunkten A(3 | 0 | 0), B(0 | 9 | 0), C(0 | 0 | 4) und dem Ursprung",
    gesucht="Volumen der Pyramide",
    verfahren="V = 1/3 · Grundfläche · Höhe mit dem Dreieck OAB in der x-y-Ebene und Höhe 4",
    schritte="2", zahlenraum="dezimal", einheiten="VE", abhaengig_von="",
    ergebnis="V = 18 VE",
    zwischenergebnis="A_G = 13,5", niveau_geschaetzt="I",
    fehlerquelle="Grundfläche als 3 · 9 (Rechteck) nehmen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-bb-ea). Eigene Rechnung.")
row(id="2020-be-gk-B3.1f", block="B", aufgabe="3.1", titel="Ebenen", teilaufgabe="f", seite="25", punkte="5",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lotfußpunkt auf einer Geraden über das Skalarprodukt mit dem Richtungsvektor berechnen", typ_neben="",
    stichwoerter="g_AB: x = (3 | 0 | 0) + r · (−3 | 9 | 0)|PC = (3r − 3 | −9r | 4)|PC · (−3 | 9 | 0) = 0 ⇔ 9 − 90r = 0 ⇔ r = 0,1|P(2,7 | 0,9 | 0)",
    voraussetzungen="allgemeiner Geradenpunkt|Orthogonalität über das Skalarprodukt",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="A(3 | 0 | 0), B(0 | 9 | 0), C(0 | 0 | 4); auf g_AB liegt P so, dass g_PC senkrecht zu g_AB ist",
    gesucht="Punkt P",
    verfahren="P(r) auf g_AB ansetzen, Skalarprodukt von PC mit dem Richtungsvektor null setzen",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="r = 1/10, P(2,7 | 0,9 | 0)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Orthogonalität zu OC statt zu AB fordern",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-ea-B). Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 3.2 Theater (Seite 31), 20 BE, Landesaufgabe
TH = "Lagerhalle mit quadratischer Grundfläche ABCD (Seite 10 m, in der x-y-Ebene, A im Ursprung, B auf der x-Achse, D auf der y-Achse) und Höhe 6 m (E, F, G, H oben); dreieckige Plane ELK mit E(0 | 0 | 6), K(2 | 10 | 6), L(10 | 0 | 4); 1 LE = 1 m"
TH_SK = "Schrägbild der Halle als Quader mit Achsen, Ecken A bis H beschriftet; grau die dreieckige Plane ELK (E oben links, K auf der Kante GH, L auf der Kante BF) und der geneigte Boden des Zuschauerraums; zweite Skizze zu e: Bühne als Fläche in Höhe 0,8 m an der Seite BC bis zum Boden"
row(id="2020-be-gk-B3.2a", block="B", aufgabe="3.2", titel="Theater", teilaufgabe="a", seite="31", punkte="4",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Koordinaten eines Eckpunkts eines Prismas angeben",
    typ_neben="Ebene Figur: Gleichschenkligkeit oder Gleichseitigkeit eines Dreiecks über die Seitenlängen prüfen",
    stichwoerter="H(0 | 10 | 6), G(10 | 10 | 6)|EK = (2 | 10 | 0), EL = (10 | 0 | −2), beide Länge √104|KL Länge √168|gleichschenklig mit Basis KL",
    voraussetzungen="Quaderecken aus Kantenlängen|Beträge von Vektoren",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Untersuchen Sie", antwort="Zahl|Text",
    material="Körper", skizze=TH_SK, kontext="Theaterbau", textumfang="mittel",
    gegeben=TH,
    gesucht="Koordinaten von H und G; ob die Plane ein gleichschenkliges Dreieck ist",
    verfahren="Ecken aus Seitenlänge und Höhe; Seitenlängen des Dreiecks ELK vergleichen",
    schritte="3", zahlenraum="ganz|Wurzel|negativ", einheiten="m", abhaengig_von="",
    ergebnis="H(0 | 10 | 6), G(10 | 10 | 6); |EK| = |EL| = √104 ≈ 10,2 m, |KL| = √168 ≈ 13,0 m: gleichschenklig (Basis KL)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="nur zwei Seiten berechnen und die dritte nicht prüfen",
    bemerkung="Landesaufgabe (nicht im Pool 2020). Typen wiederverwendet (2026-ga-A, 2023-bebb-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B3.2b", block="B", aufgabe="3.2", titel="Theater", teilaufgabe="b", seite="31", punkte="4",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen", typ_neben="",
    stichwoerter="E_P: x = (10 | 0 | 4) + r · (−10 | 0 | 2) + s · (−8 | 10 | 2)|Normalenvektor (5 | −1 | 25)|5x − y + 25z = 150",
    voraussetzungen="Parameterform aus drei Punkten|Kreuzprodukt oder Eliminieren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Körper", skizze=TH_SK, kontext="Theaterbau", textumfang="kurz",
    gegeben=TH + "; Kontrollergebnis E_P: 5x − y + 25z = 150",
    gesucht="Gleichung der Ebene E_P der Plane in Parameter- und in Koordinatenform",
    verfahren="Stützpunkt L, Spannvektoren LE und LK; Normalenvektor über das Kreuzprodukt, d aus L",
    schritte="4", zahlenraum="ganz|negativ", einheiten="m", abhaengig_von="",
    ergebnis="E_P: x = (10 | 0 | 4) + r · (−10 | 0 | 2) + s · (−8 | 10 | 2), r, s ∈ IR; Koordinatenform 5x − y + 25z = 150",
    zwischenergebnis="n = (−20 | 4 | −100) ~ (5 | −1 | 25)", niveau_geschaetzt="II",
    fehlerquelle="d mit einem Punkt außerhalb der Plane berechnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-ea-A). Kontrollergebnis bestätigt (sympy).")
row(id="2020-be-gk-B3.2c", block="B", aufgabe="3.2", titel="Theater", teilaufgabe="c", seite="31", punkte="4",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen",
    typ_neben="Schnittpunkt einer Ebene mit einer senkrechten Kante berechnen",
    stichwoerter="gleicher Normalenvektor, B(10 | 0 | 0) einsetzen: d = 50|E_B: 5x − y + 25z = 50|höchster Bodenpunkt auf der Kante DH (x = 0, y = 10): 25z = 60 ⇔ z = 2,4",
    voraussetzungen="parallele Ebenen|Koordinaten einer Kante einsetzen",
    format="Begründung|Rechnung", operator="Begründen Sie|Ermitteln Sie", antwort="Text|Zahl",
    material="Körper", skizze=TH_SK, kontext="Theaterbau", textumfang="mittel",
    gegeben=TH + "; E_P: 5x − y + 25z = 150; Boden des Zuschauerraums in der Ebene E_B parallel zur Plane durch B(10 | 0 | 0)",
    gesucht="Begründung für E_B: 5x − y + 25z = 50; maximale Höhe des Bodens über der Grundfläche",
    verfahren="Normalenvektor übernehmen, d aus B; größte Höhe an der Ecke D' über D (x = 0, y = 10)",
    schritte="3", zahlenraum="dezimal", einheiten="m", abhaengig_von="2020-be-gk-B3.2b",
    ergebnis="E_B: 5x − y + 25z = 50 (Normalenvektor von E_P, B erfüllt 50 = 50); maximale Höhe 2,4 m (Punkt D'(0 | 10 | 2,4))",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Höhe an einer falschen Ecke berechnen (bei A': z = 2)",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2024-ga-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B3.2d", block="B", aufgabe="3.2", titel="Theater", teilaufgabe="d", seite="31", punkte="3",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Abstand zweier Punkte auf parallelen Ebenen mit dem Abstand der Ebenen vergleichen", typ_neben="",
    stichwoerter="L(10 | 0 | 4) auf der Plane, B(10 | 0 | 0) auf dem Boden: |LB| = 4|LB steht nicht senkrecht auf den Ebenen|Abstand < 4 (rechnerisch 100/√651 ≈ 3,92)",
    voraussetzungen="Abstand paralleler Ebenen als kürzeste Verbindung|Hessesche Normalform als Alternative",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Körper", skizze=TH_SK, kontext="Theaterbau", textumfang="kurz",
    gegeben=TH + "; E_P: 5x − y + 25z = 150, E_B: 5x − y + 25z = 50",
    gesucht="Begründung, dass der Abstand der Plane vom Boden kleiner als 4 m ist",
    verfahren="Die Strecke LB (Länge 4) verbindet Punkte beider Ebenen, ist aber nicht senkrecht zu ihnen; der Abstand ist die kürzeste Verbindung, also kleiner",
    schritte="1", zahlenraum="ganz", einheiten="m", abhaengig_von="2020-be-gk-B3.2c",
    ergebnis="Abstand < 4 m, weil die Verbindungsstrecke LB (4 m) schräg zu den parallelen Ebenen liegt; rechnerisch 100/√651 ≈ 3,92 m",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="|LB| = 4 als Abstand der Ebenen nehmen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2023-bebb-gk 3 c). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B3.2e", block="B", aufgabe="3.2", titel="Theater", teilaufgabe="e", seite="31", punkte="5",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Trapezfläche zwischen einer geneigten Ebene und einer waagerechten Ebene in einem Quader berechnen", typ_neben="",
    stichwoerter="Schnitt von E_B mit z = 0,8: 5x − y = 30|y = 0: x = 6, y = 10: x = 8|Bühne von x = 6 bzw. 8 bis x = 10, Breite 10|Trapez (4 + 2)/2 · 10 = 30 m²",
    voraussetzungen="Schnittgerade über die Koordinatengleichung|Trapezformel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=TH_SK, kontext="Theaterbau", textumfang="mittel",
    gegeben=TH + "; E_B: 5x − y + 25z = 50; Bühnenboden parallel zur Grundfläche in 0,8 m Höhe von der Seite BC bis zum Zuschauerboden",
    gesucht="Größe der trapezförmigen Bühnenfläche",
    verfahren="z = 0,8 in E_B: Schnittgerade 5x − y = 30, Schnittpunkte mit den Seitenflächen y = 0 (x = 6) und y = 10 (x = 8); Trapez mit den parallelen Seiten 4 und 2 und der Höhe 10",
    schritte="4", zahlenraum="dezimal", einheiten="m|m²", abhaengig_von="2020-be-gk-B3.2c",
    ergebnis="Bühnenfläche A = (4 + 2)/2 · 10 = 30 m²",
    zwischenergebnis="S₁(6 | 0 | 0,8), S₂(8 | 10 | 0,8)", niveau_geschaetzt="III",
    fehlerquelle="die Schnittgerade in der Grundfläche (z = 0) statt in 0,8 m Höhe bestimmen",
    bemerkung="Landesaufgabe. Enge Fassung: Schnittgerade, Begrenzung durch die Seitenflächen und Trapezfläche selbst zusammenführen – III. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 4.1 Würfel (Seite 37), 20 BE, Landesaufgabe
WF = "Zwei Würfel mit gleich wahrscheinlichen Seiten: 5er-Würfel mit den Seiten 5, 6, 1, 2, 5, 4 (P(5) = 1/3, P(4) = P(6) = P(1) = P(2) = 1/6), 6er-Würfel mit den Seiten 6, 1, 2, 4, 6, 5 (P(6) = 1/3, P(5) = P(4) = P(1) = P(2) = 1/6)"
WF_SK = "Zwei Würfelnetze (Kreuzform) mit Beschriftung: 5er-Würfel 5 oben, 6 1 2 in der Mitte, 5 und 4 unten; 6er-Würfel 6 oben, 1 2 4 in der Mitte, 6 und 5 unten"
row(id="2020-be-gk-B4.1a", block="B", aufgabe="4.1", titel="Würfel", teilaufgabe="a", seite="37", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", typ_neben="",
    stichwoerter="n = 10, p = 1/3|P(X = 4) = (10 über 4) · (1/3)⁴ · (2/3)⁶ ≈ 0,228|P(X = 0) = (2/3)¹⁰ ≈ 0,017",
    voraussetzungen="Trefferwahrscheinlichkeit aus dem Netz ablesen|Bernoulli-Formel",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur", skizze=WF_SK, kontext="Würfelspiel", textumfang="mittel",
    gegeben=WF + "; der 6er-Würfel wird 10-mal geworfen",
    gesucht="P(A): genau 4-mal eine 6; P(B): keine 6",
    verfahren="Bernoulli-Formel mit p = 1/3",
    schritte="2", zahlenraum="Bruch|Potenz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(A) ≈ 0,228 (22,8 %); P(B) = (2/3)¹⁰ ≈ 0,017 (1,7 %)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="p = 1/6 statt 1/3 (zwei Seiten zeigen die 6)",
    bemerkung="Landesaufgabe (nicht im Pool 2020). Typ wiederverwendet (2019-be-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B4.1b", block="B", aufgabe="4.1", titel="Würfel", teilaufgabe="b", seite="37", punkte="4",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm mit Abbruchbedingung erstellen",
    typ_neben="Wahrscheinlichkeit für spätestens den dritten Erfolg über die Pfade oder das Gegenereignis berechnen",
    stichwoerter="je Versuch 6 mit 1/3, keine 6 mit 2/3, Abbruch nach der 6|P = 1/3 + 2/3 · 1/3 + (2/3)² · 1/3 = 19/27 ≈ 0,704|Gegenereignis (2/3)³",
    voraussetzungen="Baumdiagramm mit Abbruch|Pfad- und Summenregel",
    format="Zeichnen|Rechnung", operator="Erstellen Sie|Ermitteln Sie", antwort="Grafik|Zahl",
    material="Figur", skizze=WF_SK, kontext="Würfelspiel", textumfang="mittel",
    gegeben=WF + "; Luisa würfelt mit dem 6er-Würfel höchstens dreimal, bei einer 6 darf sie anfangen, sonst Pedro",
    gesucht="Baumdiagramm; Wahrscheinlichkeit, dass Luisa anfangen darf",
    verfahren="Dreistufiges Baumdiagramm, das nach einer 6 endet; Summe der Pfade mit 6 oder 1 − (2/3)³",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(Luisa fängt an) = 19/27 ≈ 0,704",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="alle drei Würfe ohne Abbruch zeichnen oder P(6) = 1/6 verwenden",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2023-ea-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B4.1c", block="B", aufgabe="4.1", titel="Würfel", teilaufgabe="c", seite="37", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen", typ_neben="",
    stichwoerter="1 − (2/3)ⁿ ≥ 0,95|(2/3)ⁿ ≤ 0,05|n ≥ ln 0,05 / ln(2/3) ≈ 7,39, also n = 8",
    voraussetzungen="Gegenereignis „keine 6“|Logarithmieren mit Umkehr des Relationszeichens",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Würfelspiel", textumfang="kurz",
    gegeben=WF + "; 6er-Würfel, P(6) = 1/3",
    gesucht="Mindestzahl der Würfe, um mit mindestens 95 % Wahrscheinlichkeit mindestens eine 6 zu würfeln",
    verfahren="Ungleichung über das Gegenereignis, logarithmieren",
    schritte="3", zahlenraum="Bruch|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="n ≥ 7,39, also mindestens 8 Würfe",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Relationszeichen beim Teilen durch ln(2/3) < 0 nicht umkehren",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2017-bb-ea). Eigene Rechnung, mit sympy bestätigt (7,388).")
row(id="2020-be-gk-B4.1d", block="B", aufgabe="4.1", titel="Würfel", teilaufgabe="d", seite="37", punkte="2",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit einer vorgegebenen Augensumme bei zwei Würfen über Pfade berechnen", typ_neben="",
    stichwoerter="Summe 11 nur als 5 + 6 oder 6 + 5|1/3 · 1/3 + 1/6 · 1/6 = 5/36",
    voraussetzungen="Pfad- und Summenregel mit ungleichen Wahrscheinlichkeiten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur", skizze=WF_SK, kontext="Würfelspiel", textumfang="kurz",
    gegeben=WF + "; beide Würfel werden gleichzeitig geworfen",
    gesucht="P(C): Augensumme 11",
    verfahren="Beide Kombinationen (5er-Würfel 5 und 6er-Würfel 6; 5er-Würfel 6 und 6er-Würfel 5) addieren",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="P(C) = 1/3 · 1/3 + 1/6 · 1/6 = 5/36 ≈ 0,139",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur eine Kombination zählen oder mit 1/6 · 1/6 · 2 rechnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2020-ea-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B4.1e", block="B", aufgabe="4.1", titel="Würfel", teilaufgabe="e", seite="37", punkte="3",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeit für drei verschiedene Ergebnisse über Pfadprodukt und Reihenfolgen nachweisen", typ_neben="",
    stichwoerter="Summe 15 aus 4, 5, 6 (6 Reihenfolgen) oder 5, 5, 5|6 · 1/6 · 1/3 · 1/6 = 1/18|(1/3)³ = 1/27|1/18 + 1/27 = 5/54",
    voraussetzungen="Zerlegung der Summe in Augenzahlen|Anzahl der Reihenfolgen|Pfadregel",
    format="Rechnung", operator="Zeigen Sie", antwort="Zahl",
    material="Figur", skizze=WF_SK, kontext="Würfelspiel", textumfang="mittel",
    gegeben=WF + "; Luisa würfelt dreimal mit dem 5er-Würfel und braucht genau die Augensumme 15",
    gesucht="Nachweis, dass P(Augensumme 15) = 5/54",
    verfahren="Mögliche Tripel (4, 5, 6 in sechs Reihenfolgen; 5, 5, 5) mit ihren Pfadwahrscheinlichkeiten addieren",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="P = 6 · (1/6 · 1/3 · 1/6) + (1/3)³ = 1/18 + 1/27 = 5/54",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die sechs Reihenfolgen von 4, 5, 6 nicht zählen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-ea-B); die Seiten sind gleich wahrscheinlich, die Augenzahlen nicht. Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B4.1f", block="B", aufgabe="4.1", titel="Würfel", teilaufgabe="f", seite="37", punkte="3",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Behauptung über die größere Wahrscheinlichkeit einer Augensumme bei zwei Würfeln über die Pfade widerlegen", typ_neben="",
    stichwoerter="4, 5, 6 in beliebiger Reihenfolge: bei beiden Würfeln 1/18|5, 5, 5: 5er-Würfel 1/27, 6er-Würfel 1/216|5er-Würfel hat die größere Wahrscheinlichkeit",
    voraussetzungen="Ergebnis aus e|Vergleich der Pfade",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Figur", skizze=WF_SK, kontext="Würfelspiel", textumfang="kurz",
    gegeben=WF + "; Pedro (6er-Würfel) behauptet, seine Wahrscheinlichkeit für die Augensumme 15 sei größer als Luisas (5er-Würfel, 5/54 aus e)",
    gesucht="Begründung, dass die Behauptung falsch ist",
    verfahren="Der Anteil 4, 5, 6 ist für beide Würfel gleich; nur 5, 5, 5 unterscheidet sich, und dort ist der 5er-Würfel deutlich besser",
    schritte="1", zahlenraum="Bruch", einheiten="", abhaengig_von="2020-be-gk-B4.1e",
    ergebnis="Falsch: 4, 5, 6 ist bei beiden gleich wahrscheinlich (1/18), 5, 5, 5 beim 5er-Würfel 1/27, beim 6er-Würfel nur 1/216; insgesamt 5/54 = 20/216 gegen 13/216",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur die höhere Wahrscheinlichkeit einer 6 beim 6er-Würfel betrachten",
    bemerkung="Landesaufgabe. Verbale Begründung genügt (Verlagslösung); Zahlen zur Kontrolle mit sympy bestätigt.")
# ---- Aufgabe 4.2 Unternehmen (Seiten 43–44), 20 BE – Pool 2020 grundlegend Stochastik WTR 1 (Reserve): Aufgabenteil 1 abgewandelt (Zahlen), Aufgabenteil 2 wortgleich
UN = "In einem großen Unternehmen ist 1/3 der Beschäftigten weiblich; 50 Beschäftigte werden zufällig ausgewählt, die Anzahl X der weiblichen darunter ist binomialverteilt (n = 50, p = 1/3)"
UN2 = "Befragung: 3,5 % der weiblichen und 10,5 % der anderen Beschäftigten sind unzufrieden; Baumdiagramm mit erster Stufe w / nicht w, zweiter Stufe u / nicht u, an den Ästen x (nicht w, dann nicht u) und y (Pfad w und u)"
row(id="2020-be-gk-B4.2a", block="B", aufgabe="4.2", titel="Unternehmen (Aufgabenteil 1)", teilaufgabe="a", seite="43|44", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", typ_neben="",
    stichwoerter="P(X ≥ 17) = 1 − P(X ≤ 16) = 1 − 0,4868 = 0,5132 (Tabelle n = 50, p = 1/3)",
    voraussetzungen="Gegenereignis|Tabelle der summierten Binomialverteilung (Anlage)",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Tabelle", skizze="Anlage Seite 44: Tabelle der summierten Binomialverteilung für n = 50 (p = 0,05 bis 0,5), vier Nachkommastellen", kontext="Unternehmen / Beschäftigte", textumfang="mittel",
    gegeben=UN + "; Tabelle in der Anlage",
    gesucht="P(mindestens 17 weibliche unter den 50)",
    verfahren="1 − F(50; 1/3; 16) aus der Tabelle",
    schritte="2", zahlenraum="Bruch|dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(X ≥ 17) ≈ 0,513 (51,3 %)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="P(X ≤ 17) statt P(X ≤ 16) abziehen",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2020MgrundlegendBStochastikWTR1-1a; das Heft hat 1/3 statt 29 %, 50 statt 40 Beschäftigte und mindestens 17 statt 12. Reserve-Stapel 2020-ga-B. Typ wiederverwendet (2019-be-gk). Eigene Rechnung, mit sympy bestätigt (0,5132).")
row(id="2020-be-gk-B4.2b", block="B", aufgabe="4.2", titel="Unternehmen (Aufgabenteil 1)", teilaufgabe="b", seite="43", punkte="3",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="(50 über 13)(1/3)¹³(2/3)³⁷ + (50 über 14)(1/3)¹⁴(2/3)³⁶ ≈ 0,158|P(X = 13) + P(X = 14)|13 oder 14 weibliche Beschäftigte",
    voraussetzungen="Bernoulli-Term lesen",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=UN + "; Aussage (50 über 13) · (1/3)¹³ · (2/3)³⁷ + (50 über 14) · (1/3)¹⁴ · (2/3)³⁶ ≈ 0,158",
    gesucht="Bedeutung der Aussage im Sachzusammenhang",
    verfahren="Summanden als P(X = 13) und P(X = 14) deuten",
    schritte="1", zahlenraum="Bruch|Potenz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="Die Wahrscheinlichkeit, dass unter den 50 ausgewählten Beschäftigten genau 13 oder genau 14 weiblich sind, beträgt etwa 15,8 %",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Summe als „mindestens 13“ deuten",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2020MgrundlegendBStochastikWTR1-1b; der Pool hat eine Summe für k ≤ 10 mit n = 40, p = 0,29 (≈ 0,36). Reserve-Stapel 2020-ga-B. Typ wiederverwendet (2026-ga-B). Term am Bild geprüft; eigene Rechnung, mit sympy bestätigt (0,1577).")
row(id="2020-be-gk-B4.2c", block="B", aufgabe="4.2", titel="Unternehmen (Aufgabenteil 1)", teilaufgabe="c", seite="43", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", typ_neben="",
    stichwoerter="nicht weiblich viermal so viele: a + 4a = 50 ⇔ a = 10|P(X = 10) = (50 über 10) · (1/3)¹⁰ · (2/3)⁴⁰ ≈ 0,016",
    voraussetzungen="Anzahl aus dem Verhältnis|Bernoulli-Formel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=UN,
    gesucht="Wahrscheinlichkeit, dass die Anzahl der nicht weiblichen viermal so groß ist wie die der weiblichen",
    verfahren="Anzahl 10 weibliche aus a + 4a = 50, dann P(X = 10)",
    schritte="2", zahlenraum="Bruch|Potenz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="P(X = 10) ≈ 0,016 (1,6 %)",
    zwischenergebnis="a = 10", niveau_geschaetzt="II",
    fehlerquelle="P(X = 40) (nicht weibliche) mit p = 1/3 berechnen",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2020MgrundlegendBStochastikWTR1-1c; das Heft sagt viermal statt dreimal so groß (n = 50 statt 40). Reserve-Stapel 2020-ga-B. Eigene Rechnung, mit sympy bestätigt (0,0157).")
row(id="2020-be-gk-B4.2d", block="B", aufgabe="4.2", titel="Unternehmen (Aufgabenteil 1)", teilaufgabe="d", seite="43", punkte="3",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussage über die Stelle des Maximums der Binomialverteilung über den Erwartungswert beurteilen", typ_neben="",
    stichwoerter="E(X) = 50 · 1/3 = 16,67|Maximum der Verteilung bei den Nachbarn des Erwartungswerts|16 oder 17",
    voraussetzungen="Erwartungswert n · p|Lage des Maximums einer Binomialverteilung",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=UN,
    gesucht="Begründung ohne Wahrscheinlichkeitsrechnung, dass die Verteilung von X für 16 oder 17 den größten Wert hat",
    verfahren="Erwartungswert berechnen; das Maximum liegt bei einer der beiden benachbarten ganzen Zahlen",
    schritte="1", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="E(X) = 50/3 ≈ 16,67; die Binomialverteilung ist am Erwartungswert am größten, also bei 16 oder 17",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Maximum bei n/2 = 25 vermuten",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2020MgrundlegendBStochastikWTR1-1d; das Heft sagt 16 oder 17 statt 11 oder 12. Reserve-Stapel 2020-ga-B. Typ wiederverwendet (2025-ga-B). Eigene Rechnung.")
row(id="2020-be-gk-B4.2e", block="B", aufgabe="4.2", titel="Unternehmen (Aufgabenteil 2 a)", teilaufgabe="e", seite="43", punkte="3",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Fehlende Wahrscheinlichkeiten im Baumdiagramm über die Pfadregel ermitteln", typ_neben="",
    stichwoerter="x = 1 − 0,105 = 0,895|y = 1/3 · 0,035 ≈ 0,0117",
    voraussetzungen="Summenregel an einem Knoten|Pfadregel",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Diagramm", skizze="Baumdiagramm (Seite 43): erste Stufe w und nicht w, zweite Stufe u und nicht u; am Ast nicht w → nicht u steht x, am Ende des Pfads w → u steht y; die Wahrscheinlichkeiten 1/3, 3,5 %, 10,5 % stehen im Text", kontext="Unternehmen / Beschäftigte", textumfang="mittel",
    gegeben=UN2 + "; 1/3 der Beschäftigten ist weiblich",
    gesucht="Werte von x und y",
    verfahren="x als Gegenwahrscheinlichkeit am Knoten nicht w; y als Pfadprodukt 1/3 · 0,035",
    schritte="2", zahlenraum="dezimal|Prozent|Bruch", einheiten="", abhaengig_von="",
    ergebnis="x = 0,895 (89,5 %); y = 1/3 · 0,035 ≈ 0,0117 (1,17 %)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="y als Astwahrscheinlichkeit 0,035 statt als Pfadprodukt angeben",
    bemerkung="Poolaufgabe (nicht erfasst): 2020MgrundlegendBStochastikWTR1-2a. Wortgleich mit der Poolaufgabe 2020 grundlegend Stochastik WTR 1, Aufgabe 2 a (Reserve-Stapel 2020-ga-B); im Heft Aufgabenteil 2 a, hier fortlaufend e. Typ wiederverwendet (2026-ga-A). Eigene Rechnung.")
row(id="2020-be-gk-B4.2f", block="B", aufgabe="4.2", titel="Unternehmen (Aufgabenteil 2 b)", teilaufgabe="f", seite="43", punkte="3",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen", typ_neben="",
    stichwoerter="P(u) = 1/3 · 0,035 + 2/3 · 0,105 ≈ 0,0817|P(nicht w ∩ u) = 0,07|P_u(nicht w) = 0,07 / 0,0817 ≈ 0,857",
    voraussetzungen="totale Wahrscheinlichkeit|bedingte Wahrscheinlichkeit als Quotient|Vierfeldertafel als Hilfe",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Diagramm", skizze="Baumdiagramm wie in e", kontext="Unternehmen / Beschäftigte", textumfang="kurz",
    gegeben=UN2 + "; 1/3 weiblich; die ausgewählte Person ist unzufrieden (Hinweis: Vierfeldertafel)",
    gesucht="Wahrscheinlichkeit, dass sie nicht weiblich ist",
    verfahren="P(nicht w ∩ u) durch P(u), etwa aus der Vierfeldertafel",
    schritte="3", zahlenraum="dezimal|Prozent|Bruch", einheiten="", abhaengig_von="",
    ergebnis="P_u(nicht w) = 0,07 / 0,08167 ≈ 0,857 (85,7 %)",
    zwischenergebnis="P(u) ≈ 8,17 %", niveau_geschaetzt="II",
    fehlerquelle="P(u) nur aus einem Ast bilden",
    bemerkung="Poolaufgabe (nicht erfasst): 2020MgrundlegendBStochastikWTR1-2b. Wortgleich mit der Poolaufgabe (Reserve-Stapel 2020-ga-B; der Verlagshinweis auf die Vierfeldertafel steht auch im Pool). Typ wiederverwendet (2024-ea-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2020-be-gk-B4.2g", block="B", aufgabe="4.2", titel="Unternehmen (Aufgabenteil 2 c)", teilaufgabe="g", seite="44", punkte="4",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil aus einem Verhältnis zweier Pfadwahrscheinlichkeiten berechnen", typ_neben="",
    stichwoerter="Anteil a weiblich|5 · a · 0,04 = (1 − a) · 0,1|0,3a = 0,1 ⇔ a = 1/3",
    voraussetzungen="Pfadwahrscheinlichkeiten mit unbekanntem Anteil|lineare Gleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Unternehmen / Beschäftigte", textumfang="mittel",
    gegeben="Abteilung: 4 % der weiblichen und 10 % der anderen Beschäftigten sind unzufrieden; der Anteil der unzufriedenen nicht weiblichen Beschäftigten ist fünfmal so groß wie der Anteil der unzufriedenen weiblichen",
    gesucht="Anteil der weiblichen Beschäftigten in der Abteilung",
    verfahren="Anteil a ansetzen, Pfadprodukte ins Verhältnis setzen und die lineare Gleichung lösen",
    schritte="3", zahlenraum="dezimal|Prozent|Bruch", einheiten="", abhaengig_von="",
    ergebnis="a = 1/3 ≈ 33,3 %",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="das Verhältnis der bedingten Anteile (10 % zu 4 %) statt der Pfadwahrscheinlichkeiten ansetzen",
    bemerkung="Poolaufgabe (nicht erfasst): 2020MgrundlegendBStochastikWTR1-2c. Wortgleich mit der Poolaufgabe (Reserve-Stapel 2020-ga-B). Enge Fassung: Gleichung aus dem Text selbst aufstellen – III. Eigene Rechnung, mit sympy bestätigt.")
# ---- Dubletten aus dem Pool (dubletten.py, map_2020gk.py)
row(id="2020-be-gk-A1.2a", block="A", aufgabe="1.2", titel="Analysis 2", teilaufgabe="a", seite="1", punkte="5", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Quadratische Funktion aus Ursprung und Tangentengleichung bestimmen",
    typ_neben="",
    stichwoerter="f(x) = ax² + bx + c, f(0) = 0 gibt c = 0|Tangente y = 4x − 2 in (2; f(2)): f(2) = 6, f'(2) = 4|I 4a + 2b = 6, II 4a + b = 4|b = 2, a = 1/2",
    voraussetzungen="Punkt auf der Tangente als Funktionswert|Tangentensteigung als Ableitungswert|Gleichungssystem",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Term",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="quadratische Funktion f durch den Ursprung; Tangente in (2; f(2)) mit y = 4x − 2",
    gesucht="Funktionsterm von f",
    verfahren="drei Bedingungen aufstellen und lösen",
    schritte="3",
    zahlenraum="Bruch|negativ",
    einheiten="",
    ergebnis="f(x) = ax² + bx + c; f(0) = 0 ⇔ c = 0; f(2) = 4 · 2 − 2 = 6 und f'(2) = 4 liefern I 4a + 2b = 6, II 4a + b = 4; aus I und II ergibt sich b = 2 und damit a = 1/2",
    zwischenergebnis="f(x) = 1/2 x² + 2x",
    niveau_geschaetzt="II",
    fehlerquelle="f(2) = 4 statt 6 ansetzen (Achsenabschnitt der Tangente übersehen)",
    abhaengig_von="",
    bemerkung="Dublette von: 2020MgrundlegendAAnalysis12. Wortgleich mit der Poolaufgabe 2020 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.2 (ohne Teilaufgaben, deshalb dort id ohne Buchstaben; hier a). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2020-be-gk-A1.5a", block="A", aufgabe="1.5", titel="Stochastik", teilaufgabe="a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen",
    typ_neben="",
    stichwoerter="drei blaue, zwei rote|blau dann rot 3/5 · 2/4, rot dann blau 2/5 · 3/4|Summe 3/5",
    voraussetzungen="Pfadregel ohne Zurücklegen|beide Reihenfolgen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Urne/Kugelspiel",
    textumfang="kurz",
    gegeben="Behälter mit drei blauen und zwei roten Kugeln; zwei Kugeln werden entnommen",
    gesucht="Wahrscheinlichkeit für zwei verschiedene Farben",
    verfahren="zwei Pfade addieren",
    schritte="2",
    zahlenraum="Bruch",
    einheiten="",
    ergebnis="3/5 · 2/4 + 2/5 · 3/4 = 3/5",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="nur einen Pfad rechnen (3/10)",
    abhaengig_von="",
    bemerkung="Dublette von: 2020MgrundlegendAStochastik11-a. Wortgleich mit der Poolaufgabe 2020 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 1.1 a; das Heft fügt „nacheinander“ ein (zwei Kugeln werden zufällig nacheinander entnommen), sonst wortgleich. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2020-be-gk-A1.5b", block="A", aufgabe="1.5", titel="Stochastik", teilaufgabe="b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Gewinnwahrscheinlichkeiten in einem Wechselspiel vergleichen",
    typ_neben="",
    stichwoerter="erste Spielerin gewinnt sofort mit 2/5|oder blau, blau, rot: 3/5 · 2/4 · 2/3|zusammen 3/5 > 1/2",
    voraussetzungen="Pfade ohne Zurücklegen mit Abbruch bei rot|Gewinnpfade der ersten Spielerin summieren|mit 1/2 vergleichen",
    format="Rechnung",
    operator="Weisen Sie nach",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Urne/Kugelspiel",
    textumfang="mittel",
    gegeben="Behälter wieder mit drei blauen und zwei roten Kugeln; zwei Spielerinnen ziehen abwechselnd ohne Zurücklegen; wer zuerst rot zieht, gewinnt",
    gesucht="Nachweis, dass die zuerst ziehende Spielerin im Vorteil ist",
    verfahren="Gewinnwahrscheinlichkeit der ersten Spielerin über die Pfade 1. Zug rot und 3. Zug rot",
    schritte="3",
    zahlenraum="Bruch",
    einheiten="",
    ergebnis="für die Wahrscheinlichkeit dafür, dass die Spielerin gewinnt, die die erste Kugel entnimmt, gilt 2/5 + 3/5 · 2/4 · 2/3 = 3/5 > 1/2",
    zwischenergebnis="spätestens im vierten Zug fällt rot; 5. Zug entfällt",
    niveau_geschaetzt="II",
    fehlerquelle="mit Zurücklegen rechnen oder den Pfad blau, blau, rot vergessen",
    abhaengig_von="",
    bemerkung="Dublette von: 2020MgrundlegendAStochastik11-b. Wortgleich mit der Poolaufgabe 2020 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 1.1 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")

NEUE_TYPEN = [
    ("Funktion aus einer gegebenen Stammfunktion durch Ableiten bestimmen", "Analysis", "Stammfunktion und Hauptsatz",
     "Aus einem als Stammfunktion bezeichneten Term F die Funktion f = F' durch Ableiten angeben.",
     "2020-be-gk-A1.1a"),
    ("Stammfunktionen mit vorgegebenem vertikalem Abstand zum Graphen einer Stammfunktion angeben", "Analysis", "Stammfunktion und Hauptsatz",
     "Die Menge aller Stammfunktionen F + C angeben und daraus die beiden Stammfunktionen nennen, deren Graphen um einen vorgegebenen Abstand in y-Richtung über bzw. unter dem Graphen einer gegebenen Stammfunktion liegen.",
     "2020-be-gk-A1.1b"),
    ("Kollinearität dreier Punkte über die Verbindungsvektoren nachweisen", "Analytische Geometrie", "Geraden",
     "Nachweisen, dass drei Punkte auf einer Geraden liegen: Gerade durch zwei Punkte aufstellen und Punktprobe mit dem dritten, oder Kollinearität der Verbindungsvektoren zeigen.",
     "2020-be-gk-A1.3a"),
    ("Punkt: Zweiten Punkt auf einer Geraden mit gleichem Abstand zu einem Geradenpunkt über den Richtungsvektor angeben", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Zu einem Punkt A auf einer Geraden und einem zweiten Geradenpunkt B den Punkt D auf der anderen Seite von A mit gleichem Abstand angeben, indem der Verbindungsvektor AB von A abgezogen wird.",
     "2020-be-gk-A1.3b"),
    ("Art eines Extrempunkts aus dem Vorzeichenwechsel am Ableitungsgraphen begründen", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Aus einer Skizze des Ableitungsgraphen die Art eines bekannten Extrempunkts der Funktion begründen: Vorzeichenwechsel von f' von + nach − heißt Hochpunkt, von − nach + Tiefpunkt.",
     "2020-be-gk-B2.1d"),
    ("Fläche: Fläche zwischen Graph, x-Achse und zwei senkrechten Geraden mit vorgegebener Stammfunktion berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Den Inhalt der Fläche zwischen dem Graphen, der x-Achse und zwei senkrechten Geraden als bestimmtes Integral mit einer vorgegebenen oder zuvor nachgewiesenen Stammfunktion berechnen, bei einheitlichem Vorzeichen des Integranden.",
     "2020-be-gk-B2.1i"),
    ("Stelle mit parallelen Tangenten an Graph und Ableitungsgraph über f' = f'' ermitteln", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Untersuchen, ob es eine Stelle gibt, an der die Tangente an den Graphen von f parallel zur Tangente an den Graphen von f' ist, über die Gleichung f'(x) = f''(x).",
     "2020-be-gk-B2.1j"),
    ("Nullstellen und Werte: Nullstellen aus der faktorisierten Form angeben", "Analysis", "Funktionsklassen und Eigenschaften",
     "Die Nullstellen einer in Linearfaktoren gegebenen ganzrationalen Funktion ablesen, doppelte Nullstellen eingeschlossen.",
     "2020-be-gk-B2.2a"),
    ("Termgleichheit zweier Darstellungen einer ganzrationalen Funktion durch Ausmultiplizieren nachweisen", "Analysis", "Gleichungen lösen",
     "Zeigen, dass eine faktorisierte und eine ausmultiplizierte Funktionsgleichung denselben Term beschreiben, durch Ausmultiplizieren oder Zusammenfassen.",
     "2020-be-gk-B2.2b"),
    ("Wendepunkt des Funktionsgraphen aus dem Extrempunkt des Ableitungsgraphen erläutern", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Erläutern, dass ein Hoch- oder Tiefpunkt des Graphen von f' einer Wendestelle von f entspricht (f'' = 0 mit Vorzeichenwechsel), und die Folgerung für den Graphen von f nennen.",
     "2020-be-gk-B2.2e"),
    ("Fläche: Querschnittsfläche zwischen Tangente und Graph als Dreieck minus Integral berechnen und mit der Breite zum Volumen umrechnen", "Analysis", "Flächeninhalt durch Integration",
     "Die Fläche unterhalb einer Tangente und oberhalb des Graphen bis zu deren Nullstelle als Dreiecksfläche minus Integral (oder als Summe zweier Teilflächen) berechnen und mit einer Breite zum Volumen im Sachzusammenhang umrechnen.",
     "2020-be-gk-B2.2g"),
    ("Lage zweier Ebenen über die Normalenvektoren entscheiden und Schnittgerade berechnen", "Analytische Geometrie", "Schnittmengen",
     "Begründen, dass zwei Ebenen nicht parallel sind (Normalenvektoren nicht kollinear), und die Schnittgerade berechnen, indem die Parameterform der einen Ebene in die Koordinatenform der anderen eingesetzt wird.",
     "2020-be-gk-B3.1d"),
    ("Schnittpunkt einer Ebene mit einer senkrechten Kante berechnen", "Analytische Geometrie", "Schnittmengen",
     "Für eine Kante parallel zu einer Koordinatenachse (zwei Koordinaten fest) die dritte Koordinate des Schnittpunkts mit einer Ebene in Koordinatenform berechnen, etwa als größte Höhe einer geneigten Ebene über einer Grundfläche.",
     "2020-be-gk-B3.2c"),
    ("Ebene Figur: Trapezfläche zwischen einer geneigten Ebene und einer waagerechten Ebene in einem Quader berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Die Schnittgerade einer geneigten Ebene mit einer waagerechten Ebene (z fest) über die Koordinatengleichung bestimmen, ihre Schnittpunkte mit den Seitenflächen des Quaders berechnen und den Flächeninhalt des so begrenzten Trapezes angeben.",
     "2020-be-gk-B3.2e"),
    ("Wahrscheinlichkeit für spätestens den dritten Erfolg über die Pfade oder das Gegenereignis berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Bei bis zu drei Versuchen mit fester Trefferwahrscheinlichkeit und Abbruch nach dem ersten Treffer die Wahrscheinlichkeit für einen Treffer über die Summe der Pfade oder über 1 − (1 − p)³ berechnen.",
     "2020-be-gk-B4.1b"),
    ("Behauptung über die größere Wahrscheinlichkeit einer Augensumme bei zwei Würfeln über die Pfade widerlegen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Für zwei verschieden beschriftete Würfel begründen, mit welchem die Wahrscheinlichkeit einer vorgegebenen Augensumme größer ist, über den Vergleich der beitragenden Pfade ohne vollständige Rechnung.",
     "2020-be-gk-B4.1f"),
    ("Anteil aus einem Verhältnis zweier Pfadwahrscheinlichkeiten berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Aus der Angabe, dass ein Pfad (etwa unzufrieden und nicht weiblich) k-mal so wahrscheinlich ist wie ein anderer, mit bekannten bedingten Wahrscheinlichkeiten eine lineare Gleichung für den unbekannten Anteil aufstellen und lösen.",
     "2020-be-gk-B4.2g"),
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


# Feste Markierungen in bemerkung (abi.md § 7; wie iqb.md § 7), bewusst umlautfrei.
MARKE_KONTEXT = "Traegerbindung: Kontext"
MARKE_DUBLETTE = re.compile(r"Dublette von: (" + KENNUNG.pattern + r")")
# Vorstufe des Verweises (v0.5, Lauf 14): Poolaufgabe, deren Stapel im Profil iqb
# noch nicht erfasst ist; die Kennung ist die voraussichtliche iqb-id. Wird zum
# „Dublette von:", sobald der Stapel erfasst ist (abgleich.py).
MARKE_POOL_OFFEN = re.compile(r"Poolaufgabe \(nicht erfasst(, abgewandelt)?\): (" + KENNUNG.pattern + r")")
# Abgewandelte Poolaufgabe mit erfasster Poolzeile (v0.6, Lauf 15): kein Dublettenverweis
# (nicht wortgleich), aber ein Verweis auf die Poolzeile; der Unterschied folgt nach „;".
MARKE_ABGEWANDELT = re.compile(r"Abgewandelt von: (" + KENNUNG.pattern + r"); ")
OFFENE_POSTEN = []  # Vermerke, deren Poolzeile inzwischen erfasst ist (Ausgabe am Ende, kein Abbruch)


def pool_stand(z, andere):
    """'dublette' (Verweis auf erfasste Poolzeile), 'offen' (wortgleich, Pool nicht erfasst),
    'abgewandelt' (Vormerkung oder Verweis auf abgewandelte Poolzeile) oder '' – für die Poolquote je Heft."""
    if MARKE_DUBLETTE.search(z["bemerkung"]):
        return "dublette"
    if MARKE_ABGEWANDELT.search(z["bemerkung"]):
        return "abgewandelt"
    m = MARKE_POOL_OFFEN.search(z["bemerkung"])
    if m:
        return "abgewandelt" if m.group(1) else "offen"
    return ""


def poolquote(zeilen, andere):
    """Zeilen und BE je Heft, die wortgleich im Pool stehen (erfasst oder nicht),
    dazu die abgewandelten; Text für die Kennzahlenzeile."""
    st = [(pool_stand(z, andere), int(z["punkte"])) for z in zeilen if z["punkte"].isdigit()]
    be = sum(p for _, p in st)
    wort = [(s, p) for s, p in st if s in ("dublette", "offen")]
    abw = [(s, p) for s, p in st if s == "abgewandelt"]
    txt = (f"Pool {len(wort)} von {len(zeilen)} Zeilen, {sum(p for _, p in wort)} von {be} BE "
           f"({100 * sum(p for _, p in wort) / be if be else 0:.0f} %)")
    offen = sum(1 for s, _ in wort if s == "offen")
    if offen:
        txt += f", davon {offen} Zeilen mit nicht erfasster Poolzeile"
    if abw:
        txt += f"; abgewandelt {len(abw)} Zeilen, {sum(p for _, p in abw)} BE"
    return txt
AB_SPALTE = re.compile(r"AB amtlich: (I{1,3})\.")
ENG = re.compile(r"Schätzung enge Fassung: (I{1,3})")


def ohne_feldnamen(v):
    """Feldnamen des Schemas, Kennungen und Markierungen aus dem Text nehmen. Sie sind
    bewusst umlautfrei und stehen in bemerkung als Fachwort, ohne Umschrift zu sein."""
    t = KENNUNG.sub(" ", v).lower()
    t = t.replace(MARKE_KONTEXT.lower(), " ")
    for f in sorted(HEAD, key=len, reverse=True):
        t = t.replace(f, " ")
    return t


def umschrift_liste(zeilen):
    """Sichtprüfung, kein Assert: alle Wörter mit ss, ae, oe oder ue."""
    worte = {}
    for z in zeilen:
        for k, v in z.items():
            if k in OHNE_UMLAUT:
                continue
            for w in re.findall(r"[^\W\d_]+", ohne_feldnamen(v), re.UNICODE):
                if any(p in w for p in ("ss", "ae", "oe", "ue")):
                    worte[w] = worte.get(w, 0) + 1
    return sorted(worte.items())


def hoechster_afb(v):
    return max(ORD.get(t, 0) for t in v.split("|")) if v else 0


def typen_von(z):
    t = set()
    for feld in ("typ", "typ_neben"):
        t |= {s for s in z[feld].split("|") if s}
    return t


def pruefe_zeile(z, a, andere, heftkennung=True):
    """Alle Prüfungen, die eine einzelne Zeile aus sich selbst und den anderen
    Katalogen (Dublettenverweis) bestehen kann."""
    i = z["id"] or "(ohne id)"
    for k in PFLICHT:
        a(z[k].strip() != "", f"{i}: Pflichtfeld leer: {k}")
    a(z["block"] in ("A", "B"), f"{i}: block muss A oder B sein")
    a(z["stern"] == "", f"{i}: stern ist im Profil abi immer leer")
    a(z["hilfsmittel"] == ("nein" if z["block"] == "A" else "ja"),
      f"{i}: hilfsmittel passt nicht zu block {z['block']}")
    a(PAPIER.fullmatch(z["papier"]) is not None, f"{i}: papier folgt nicht dem Muster Jahr-Land-Niveau[-cas|-mms]")
    a(z["papier"].startswith(z["jahr"] + "-"), f"{i}: papier beginnt nicht mit dem Jahr")
    if z["jahr"] <= "2018":
        a(z["afb_amtlich"] == "", f"{i}: afb_amtlich ist für {z['jahr']} nicht ausgewiesen")
    elif z["afb_amtlich"]:
        a(AFB.fullmatch(z["afb_amtlich"]) is not None, f"{i}: afb_amtlich ungültig: {z['afb_amtlich']}")
        teile = z["afb_amtlich"].split("|")
        a([ORD[t] for t in teile if t in ORD] == sorted({ORD[t] for t in teile if t in ORD}),
          f"{i}: afb_amtlich nicht aufsteigend ohne Wiederholung")
    a(re.fullmatch(r"\d+(\.\d+)?", z["aufgabe"]), f"{i}: aufgabe muss eine Nummer wie 3 oder 2.1 sein")
    a(re.fullmatch(r"[a-z]", z["teilaufgabe"]), f"{i}: teilaufgabe muss ein Kleinbuchstabe sein")
    a(z["id"] == f"{z['papier']}-{z['block']}{z['aufgabe']}{z['teilaufgabe']}",
      f"{i}: id folgt nicht dem Muster papier-BlockAufgabeTeilaufgabe")
    if heftkennung:
        a(z["jahr"] == KONFIG["jahr"] and z["papier"] == KONFIG["papier"],
          f"{i}: Heftkennung passt nicht zu KONFIG")
    a(re.fullmatch(r"\d+", z["punkte"]) and int(z["punkte"]) > 0, f"{i}: punkte ungültig")
    a(re.fullmatch(r"\d+(\|\d+)?", z["seite"]), f"{i}: seite ungültig (Zahl oder Zahl|Zahl)")
    for s in z["seite"].split("|"):
        if s.isdigit() and heftkennung:
            a(int(s) <= KONFIG["seiten"], f"{i}: Seite {s} größer als der Heftumfang")
    a(re.fullmatch(r"\d+", z["schritte"]), f"{i}: schritte muss eine Zahl sein")
    a(z["leitidee"] in THEMEN, f"{i}: Sachgebiet unbekannt: {z['leitidee']}")
    a(z["thema"] in THEMEN.get(z["leitidee"], []),
      f"{i}: Thema passt nicht zum Sachgebiet: {z['thema']}")
    for feld in ("format", "antwort", "material", "zahlenraum"):
        for teil in [s for s in z[feld].split("|") if s]:
            a(teil in VOK[feld], f"{i}: {feld} hat unbekannten Wert: {teil}")
    for feld in ("textumfang", "niveau_geschaetzt"):
        a(z[feld] in VOK[feld], f"{i}: {feld} ungültig: {z[feld]}")
    b = z["bemerkung"]
    # Trägerbindung: nur die feste Markierung am Feldanfang
    a("Trägerbindung" not in b and "Traegerbindung: frei" not in b,
      f"{i}: Trägerbindung nur als „{MARKE_KONTEXT}“ am Anfang von bemerkung (kein Vermerk heißt frei)")
    if MARKE_KONTEXT.lower() in b.lower():
        a(b.startswith(MARKE_KONTEXT) and (b[len(MARKE_KONTEXT):len(MARKE_KONTEXT) + 1] in (".", " ")),
          f"{i}: Markierung „{MARKE_KONTEXT}“ muss am Anfang von bemerkung stehen, gefolgt von Punkt oder Klammer")
    # Pool-Teilaufgabe (abi.md § 7): Verweis auf die iqb-Zeile, geteilter Typ
    m = MARKE_DUBLETTE.search(b)
    if "Dublette von" in b:
        a(m is not None, f"{i}: „Dublette von:“ ohne gültige Pool-Kennung in bemerkung")
    if m:
        ref = andere.get(m.group(1))
        a(ref is not None, f"{i}: Dublette von {m.group(1)}, aber die Zeile steht in keinem anderen Katalog")
        if ref:
            a(z["typ"] == ref["typ"],
              f"{i}: Dublette von {m.group(1)}, aber typ weicht ab (geteilter Typ verlangt; typ_neben darf Nebenleistungen des Landeshefts nennen)")
            a(z["punkte"] == ref["punkte"] or "BE" in b,
              f"{i}: Dublette von {m.group(1)} mit anderer Punktzahl – bemerkung muss die BE nennen")
    # Vorstufe (v0.5): Poolaufgabe, deren Stapel noch nicht erfasst ist
    mo = MARKE_POOL_OFFEN.search(b)
    if "Poolaufgabe (nicht erfasst" in b:
        a(mo is not None, f"{i}: „Poolaufgabe (nicht erfasst …):“ ohne gültige Pool-Kennung in bemerkung")
    if mo:
        a(b.startswith("Poolaufgabe (nicht erfasst"), f"{i}: Vermerk „Poolaufgabe (nicht erfasst …)“ muss am Anfang von bemerkung stehen")
        # Übergangszustand (abi.md § 7): erfasste Poolzeile heißt offener Posten, kein Fehler
        if mo.group(2) in andere:
            OFFENE_POSTEN.append(f"{i}: Poolzeile {mo.group(2)} ist erfasst – Vermerk mit abgleich.py in „Dublette von:“ umstellen")
        a(m is None, f"{i}: „Dublette von:“ und „Poolaufgabe (nicht erfasst)“ zugleich")
    # Abgewandelte Poolaufgabe mit erfasster Poolzeile (v0.6): Verweis am Anfang, Zeile muss stehen
    ma = MARKE_ABGEWANDELT.search(b)
    if "Abgewandelt von" in b:
        a(ma is not None, f"{i}: „Abgewandelt von:“ ohne gültige Pool-Kennung oder ohne „; Unterschied“ in bemerkung")
    if ma:
        a(b.startswith("Abgewandelt von"), f"{i}: Verweis „Abgewandelt von:“ muss am Anfang von bemerkung stehen")
        a(ma.group(1) in andere, f"{i}: Abgewandelt von {ma.group(1)}, aber die Zeile steht in keinem anderen Katalog")
        a(m is None and mo is None, f"{i}: „Abgewandelt von:“ neben einem weiteren Poolvermerk")
    for k, v in z.items():
        a("?" not in v or k == "bemerkung" or z["bemerkung"].strip() != "",
          f"{i}: Fragezeichen in {k} ohne Grund in bemerkung")
        # Pool-Kennungen (…WTR3-1a) tragen den Bindestrich vor der Aufgabennummer, v0.4
        a(not re.search(r"(?<=[\d\s(])-(?=\d)", KENNUNG.sub(" ", v)),
          f"{i}: ASCII-Bindestrich als Minus in {k}")
        if k not in OHNE_UMLAUT:
            treffer = [w for w in UMSCHRIFT if w in ohne_feldnamen(v)]
            a(not treffer, f"{i}: ASCII-Umschrift in {k}: {treffer}")


def amtlich_von(z):
    """Amtlicher Bereich für die Eichung: die Spalte „AB amtlich" aus bemerkung, sonst das
    Maximum über afb_amtlich; 0, wenn nichts ausgewiesen ist (Hefte bis 2018)."""
    m = AB_SPALTE.search(z["bemerkung"])
    if m:
        return ORD[m.group(1)]
    return hoechster_afb(z["afb_amtlich"])


def geschaetzt_eng(z):
    m = ENG.search(z["bemerkung"])
    return m.group(1) if m else z["niveau_geschaetzt"]


def geerbt(z, andere):
    """Dublette, die die Schätzung ihrer Poolzeile trägt (v0.8): dort schon geeicht."""
    m = MARKE_DUBLETTE.search(z["bemerkung"])
    return bool(m and m.group(1) in andere
                and andere[m.group(1)]["niveau_geschaetzt"] == z["niveau_geschaetzt"])


def eichung(zeilen, eng=False, andere=None):
    """Trefferquote der Schätzung gegen den amtlichen Bereich. Rückgabe: Treffer,
    Abweichungen, Zahl der gewerteten Zeilen (nur Zeilen mit amtlichem Bereich).
    Mit andere (Poolzeilen) werden geerbte Schätzungen (Dubletten) übergangen (v0.8)."""
    treffer, abw, gewertet = 0, [], 0
    for z in zeilen:
        amt = amtlich_von(z)
        if not amt or (andere is not None and geerbt(z, andere)):
            continue
        gewertet += 1
        wert = geschaetzt_eng(z) if eng else z["niveau_geschaetzt"]
        if amt == ORD.get(wert, 0):
            treffer += 1
        else:
            abw.append(f"{z['id']} geschätzt {wert}, amtlich höchstens "
                       f"{[k for k, v in ORD.items() if v == amt][0]}")
    return treffer, abw, gewertet


def schnitt(z):
    """Schnittwert Thema × Gegenstandsklasse × Handlung (abitur-vokabular.md § 4); Thema des Typs (v0.4)."""
    return (TYP_THEMA.get(z["typ"], ("", z["thema"]))[1], klasse_von(z["typ"]),
            HANDLUNG.get(z["format"].split("|")[0], "?"))


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
    # andere Kataloge derselben Typenliste (Entscheidung 25)
    andere_liste = [dict(zip(HEAD, r)) for p in ANDERE_KATALOGE for r in lade(p, HEAD)[1]]
    andere = {z["id"]: z for z in andere_liste}
    andere_typen = set()
    for z in andere_liste:
        andere_typen |= typen_von(z)
    print(f"Vokabular: {len(HEAD)} Felder, {len(LEITIDEEN)} Sachgebiete, "
          f"{sum(len(v) for v in THEMEN.values())} Themen – gelesen aus {KERN} und {VOKABULAR}; "
          f"{len(andere)} Zeilen aus {ANDERE_KATALOGE}")

    # ---- Selbstprüfung: kein neues Heft, nur die vorhandenen Zeilen prüfen
    if not ZEILEN:
        for z in alt:
            a(len(z) == len(HEAD), f"{z.get('id')}: Feldzahl weicht ab")
            pruefe_zeile(z, a, andere, heftkennung=False)
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
        a(not (ids & set(andere)), f"ids auch in einem anderen Katalog: {sorted(ids & set(andere))[:5]}")
        for z in alt:
            for dep in [s for s in z["abhaengig_von"].split("|") if s]:
                a(dep in ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
        for r in alt_typ:
            a(r[1] in THEMEN and r[2] in THEMEN.get(r[1], []),
              f"Typ {r[0]}: Sachgebiet oder Thema unbekannt")
            a(r[4] in ids or r[4] in andere, f"Typ {r[0]}: beispiel_id in keinem Katalog")
            pruefe_typname(r[0], r[2], a, TYP)
        if fehler:
            print(f"\nSelbstprüfung: {len(fehler)} Fehler")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        hefte = sorted({z["papier"] for z in alt})
        eigene = {t for z in alt for t in typen_von(z)}
        print(f"Selbstprüfung bestanden: {len(alt)} Katalogzeilen aus {len(hefte)} Heften, {len(alt_typ)} Typen "
              f"(gemeinsame Liste, {len(eigene - andere_typen)} nur hier, {len(eigene & andere_typen)} in beiden "
              f"Katalogen), alle Typen verwendet. ZEILEN ist leer, nichts geschrieben.")
        treffer, abw, gew = eichung(alt)
        if gew:
            print(f"Eichung über den Bestand: {treffer} von {gew} gewerteten Zeilen ({100 * treffer // gew} %); "
                  f"{len(alt) - gew} Zeilen ohne amtlichen Bereich.")
        else:
            print(f"Eichung: keine Zeile mit amtlichem Bereich ({len(alt)} Zeilen).")
        print("Außerhalb der Geltung: " + ", ".join(
            f"{ziel} {sum(1 for z in alt if ziel not in GELTUNG.get(z['thema'], set()))}"
            for ziel in ZIELE) + f" von {len(alt)} Zeilen (jede Zeile gegen jede Zielprüfung)")
        # Geltung des eigenen Hefts (v0.7): Zielprüfungen aus dem papier-Kürzel, bebb gegen beide
        for h in hefte:
            zh = [z for z in alt if z["papier"] == h]
            ziele = ziele_von(h)
            aus = [z["id"] for z in zh if not in_geltung(z, ziele)]
            print(f"Geltung {h} ({' oder '.join(ziele)}): {len(zh) - len(aus)} von {len(zh)} Zeilen in Geltung"
                  + (f", außerhalb: {', '.join(aus)}" if aus else "")
                  + "".join(f"; nur {ziel}: {sum(1 for z in zh if ziel not in GELTUNG.get(z['thema'], set()))} außerhalb" for ziel in ziele if len(ziele) > 1))
        werte = {schnitt(z) for z in alt}
        andere_werte = {schnitt(z) for z in andere_liste}
        print(f"Schnitt: {len(werte)} Werte auf {len(alt)} Zeilen, {len(werte - andere_werte)} davon nicht "
              f"in {ANDERE_KATALOGE}; Dublettenverweise: "
              f"{sum(1 for z in alt if MARKE_DUBLETTE.search(z['bemerkung']))}, abgewandelt: "
              f"{sum(1 for z in alt if MARKE_ABGEWANDELT.search(z['bemerkung']))}")
        # Poolquote je Heft (v0.5): Kennzahl für abi-pruefungen.md § 2
        for h in hefte:
            print(f"Poolquote {h}: {poolquote([z for z in alt if z['papier'] == h], andere)}")
        offen = sum(1 for z in alt if MARKE_POOL_OFFEN.search(z["bemerkung"]))  # Übergangszustand (v0.6)
        print(f"Offene Posten (Poolaufgabe (nicht erfasst …), Übergangszustand): {offen} Zeilen"
              + (f", davon {len(OFFENE_POSTEN)} mit inzwischen erfasster Poolzeile:" if OFFENE_POSTEN else ""))
        for o in OFFENE_POSTEN:
            print("  -", o)
        print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
              "(Häufigkeit in Klammern):")
        liste = umschrift_liste(alt)
        print("  " + ", ".join(f"{w} ({n})" for w, n in liste) if liste else "  keines")
        return

    # ---- Normalfall: neues Heft anhängen
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
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog des Hefts")
        a(len(t[3]) > 20, f"Typ {t[0]}: Definition zu knapp")
        if len(t) == 5:
            pruefe_typname(t[0], t[2], a, "NEUE_TYPEN")
    a(len({t[0] for t in NEUE_TYPEN}) == len(NEUE_TYPEN), "doppelter Typ in NEUE_TYPEN")

    # Vollständigkeit und Punkte je Aufgabe (Kern § 7): jede Aufgabe aus KONFIG["soll"]
    # muss Zeilen haben, jede Punktsumme stimmen; Aufgaben ohne Soll sind ein Fehler.
    aufgaben = sorted({z["aufgabe"] for z in ZEILEN})
    for nr in aufgaben:
        a(nr in KONFIG["soll"], f"Aufgabe {nr}: kein Soll in KONFIG")
    fehlt = sorted(set(KONFIG["soll"]) - set(aufgaben))
    if fehlt and not probe:
        a(False, f"Heft {KONFIG['papier']} unvollständig, es fehlen die Aufgaben {fehlt}")
    elif fehlt:
        warnung.append(f"Probelauf: {len(fehlt)} von {len(KONFIG['soll'])} Aufgaben fehlen noch: {fehlt}")
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr and z["punkte"].isdigit())
        if nr in aufgaben:
            a(ist == soll, f"Aufgabe {nr}: Punkte {ist}, Soll {soll}")
    if KONFIG.get("soll_teil1"):
        teil1 = [z for z in ZEILEN + alt
                 if z["block"] == "A" and z["papier"] == KONFIG["papier"]]
        ist1 = sum(int(z["punkte"]) for z in teil1 if z["punkte"].isdigit())
        a(probe or ist1 == KONFIG["soll_teil1"], f"Teil A: Punkte {ist1}, Soll {KONFIG['soll_teil1']}")

    verwendet = set()
    for z in ZEILEN:
        pruefe_zeile(z, a, andere)
        for t in typen_von(z):
            verwendet.add(t)
            a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        pruefe_thema(z, a)
        for dep in [s for s in z["abhaengig_von"].split("|") if s]:
            a(dep in neue_ids or dep in alt_ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
    warnung += OFFENE_POSTEN
    alle_verwendet = set(verwendet) | andere_typen
    for z in alt:
        alle_verwendet |= typen_von(z)
    a(not (typ_namen - alle_verwendet), f"Typen unbenutzt: {sorted(typ_namen - alle_verwendet)}")

    # Qualitätsschranke (abi.md § 7)
    n = len(ZEILEN)
    unsicher = [z["id"] for z in ZEILEN if any("?" in v for v in z.values())]
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
    # Eichschwelle nur über eigene Schätzungen; geerbte Schätzungen der Dubletten
    # sind im Pool gemessen (v0.8).
    treffer_eng, abw_eng, gew = eichung(ZEILEN, eng=True, andere=andere)
    if gew >= SCHWELLEN["eichung_ab_zeilen"]:
        a(treffer_eng / gew >= SCHWELLEN["eichung_mindestens"],
          f"Schwelle gerissen: Eichung {treffer_eng} von {gew} eigenen Zeilen "
          f"({100 * treffer_eng / gew:.0f} %), verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %: "
          f"{'; '.join(abw_eng)}")
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
    print(f"\nHeft {KONFIG['papier']}{' (Probelauf, nichts geschrieben)' if probe else ''} – "
          f"{len(ZEILEN)} Zeilen aus {len(aufgaben)} Aufgaben, {len(NEUE_TYPEN)} Typen neu, "
          f"Katalog {'bliebe' if probe else 'jetzt'} {len(alt_kat) + len(ZEILEN)} Zeilen\n")
    print(f"{'id':<22} {'BE':>2} {'afb':<8} {'thema':<34} {'typ':<46} ergebnis")
    for z in ZEILEN:
        print(f"{z['id']:<22} {z['punkte']:>2} {z['afb_amtlich']:<8} {z['thema'][:34]:<34} "
              f"{z['typ'][:46]:<46} {z['ergebnis'][:40]}")
    print()
    for nr in aufgaben:
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        print(f"Aufgabe {nr}: Ist {ist} / Soll {KONFIG['soll'].get(nr, '–')}")
    haupt = {z["typ"] for z in ZEILEN} | {z["typ"] for z in alt}
    neben = set()
    for z in ZEILEN + alt:
        neben |= {s for s in z["typ_neben"].split("|") if s}
    print(f"Typen: {len(typ_namen)} in der gemeinsamen Liste; im Heft {len(verwendet)} verwendet, "
          f"davon {len(neu & verwendet)} neu, {len(verwendet & andere_typen)} aus {ANDERE_KATALOGE}")
    treffer, abw, gew_alle = eichung(ZEILEN)
    geerbte = sum(1 for z in ZEILEN if amtlich_von(z) and geerbt(z, andere))
    if gew_alle:
        print(f"Eichung: {treffer} von {gew_alle} gewerteten Zeilen treffen den amtlichen Bereich"
              + (f" ({n - gew_alle} ohne amtlichen Bereich)" if gew_alle != n else "")
              + (f"; davon {geerbte} Zeilen mit geerbter Schätzung (Dubletten, im Pool geeicht), "
                 f"{gew_alle - geerbte} eigene" if geerbte else "")
              + (f"; Abweichungen: {'; '.join(abw)}" if abw else ""))
    else:
        print("Eichung: keine Zeile mit amtlichem Bereich.")
    print(f"Schwellen: {len(unsicher)} Zeilen mit „?“ (erlaubt {grenze_frage}), "
          f"{len(ersatz)} ohne passendes Thema (erlaubt {grenze_ersatz}), "
          f"Eichung eigener Zeilen {100 * treffer_eng / gew if gew else 0:.0f} % "
          f"(verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %"
          f"{', nicht scharf' if gew < SCHWELLEN['eichung_ab_zeilen'] else ''})")
    # Wiederverwendung im selben Niveau (gk, lk, ea) und Schnitt (abitur-vokabular.md § 4)
    niveau = niveau_von(KONFIG["papier"])
    im_niveau = set()
    for z in alt:
        if niveau_von(z["papier"]) == niveau:
            im_niveau |= typen_von(z)
    wieder = verwendet & im_niveau
    schnitt_alt = {schnitt(z) for z in alt if niveau_von(z["papier"]) == niveau}
    schnitt_alle = {schnitt(z) for z in alt} | {schnitt(z) for z in andere_liste}
    schnitt_neu = {schnitt(z) for z in ZEILEN}
    schnitt_bekannt = sum(1 for z in ZEILEN if schnitt(z) in schnitt_alt)
    # Geltung des Hefts (v0.7): eigene Zielprüfung(en) aus dem papier-Kürzel; bei bebb-Heften
    # liegt eine Zeile in der Geltung, wenn ihr Thema in einer der beiden Spalten gilt.
    ziele_heft = ziele_von(KONFIG["papier"])
    aus_heft = [z["id"] for z in ZEILEN if not in_geltung(z, ziele_heft)]
    geltung_txt = (f"Heft ({' oder '.join(ziele_heft)}) {len(aus_heft)}"
                   + ("".join(f", nur {ziel} {len(ausserhalb[ziel])}" for ziel in ziele_heft) if len(ziele_heft) > 1 else "")
                   + "; alle Zielprüfungen: " + ", ".join(f"{ziel} {len(ids)}" for ziel, ids in ausserhalb.items()))
    if aus_heft:
        print(f"Außerhalb der Geltung des Hefts ({' oder '.join(ziele_heft)}): {', '.join(aus_heft)}")
    for ziel, ids in ausserhalb.items():
        if ids:
            print(f"Außerhalb der Geltung {ziel}: {', '.join(ids)}")
    print(f"Kennzahlen: | {KONFIG['papier']} | {n} | {len(verwendet)} | {len(neu & verwendet)} "
          f"({100 * len(neu & verwendet) / len(verwendet):.0f} %) | "
          + (f"{treffer} von {gew_alle} ({100 * treffer / gew_alle:.0f} %)"
             + (f", davon {geerbte} geerbt" if geerbte else "") if gew_alle else "–")
          + f" | {len(unsicher)} | {len(ersatz)} | {len(wieder)} von {len(verwendet)} "
          f"({100 * len(wieder) / len(verwendet):.0f} %) | {geltung_txt} | "
          f"Schnitt {len(schnitt_neu)} Werte, {schnitt_bekannt} von {n} Zeilen im Niveau bekannt "
          f"({100 * schnitt_bekannt / n:.0f} %), {len(schnitt_neu - schnitt_alle)} Werte neu im Gesamtbestand | "
          f"{poolquote(ZEILEN, andere)} |")
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
          "(Häufigkeit in Klammern):")
    liste = umschrift_liste(ZEILEN)
    print("  " + ", ".join(f"{w} ({n_})" for w, n_ in liste) if liste else "  keines")
    for w in warnung:
        print("Hinweis:", w)
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
