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
    "jahr": "2019",
    "papier": "2019-be-gk",
    "datei": "hefte/2019-be-gk.pdf",  # Stark-Band Berlin GK (Band zum Abitur 2021), PDF mit Textebene, lokal (abi.md § 2)
    "seiten": 46,
    # Sollpunkte je Aufgabe aus der BE-Spalte; jede Aufgabe des Hefts muss hier
    # stehen (Vollständigkeit). Der hilfsmittelfreie Teil (Aufgabe 1) zählt als
    # 1.1 bis 1.4 in Heftreihenfolge (Analysis 1, Analysis 2, Geometrie,
    # Stochastik; alle Pflicht, 20 BE). Teil B: je Sachgebiet zwei Aufgaben zur
    # Wahl (2.1/2.2 Analysis 40 BE, 3.1/3.2 Geometrie 20 BE, 4.1/4.2 Stochastik
    # 20 BE); bearbeitet 20 + 40 + 20 + 20 = 100 BE, angeboten 200.
    "soll": {"1.1": 5, "1.2": 5, "1.3": 5, "1.4": 5,
             "2.1": 40, "2.2": 40, "3.1": 20, "3.2": 20, "4.1": 20, "4.2": 20},
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
# Heft 2019-be-gk (Stark-Band zum Abitur 2021, Berlin Grundkurs; 46 Seiten A5 mit
# Tipps und Verlagslösungen, Textebene; Auftrag B, 17.09.2026). Erstes Berliner
# Heft mit hilfsmittelfreiem Teil (Aufgabe 1: vier Einheiten zu je 5 BE), Teil B
# mit Wahl in allen drei Sachgebieten. Pool 2019 grundlegend: Teil A erfasst
# (Analysis 2 = Analysis 1.1 wortgleich, Stochastik = Stochastik 1.1 mit
# abgewandelter Teilaufgabe c), Teil B Reserve (3.2 Würfel = AG/LA (A2) WTR 1,
# 4.1 Führerschein c–e = Stochastik WTR 1 – Vormerkungen). Landesaufgaben:
# Analysis 1, Geometrie (Teil A), 2.1 Kiri-Bäume, 2.2 Hormonpflaster, 3.1 Tunnel,
# 4.2 Würfelspiel, 4.1 a–b. Verlagslösungen sind kein Erwartungshorizont:
# ergebnis ohne „amtlich“, afb_amtlich der Landeszeilen leer.
# ---- Aufgabe 1: hilfsmittelfreier Teil (Seiten 1–2), 4 × 5 BE
A1 = "f(x) = −5x⁴ − 3x² + x, definiert in IR"
row(id="2019-be-gk-A1.1a", block="A", aufgabe="1.1", titel="Analysis 1", teilaufgabe="a", seite="1", punkte="2",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitungsfunktion und Stammfunktion einer ganzrationalen Funktion angeben", typ_neben="",
    stichwoerter="Potenzregel|f'(x) = −20x³ − 6x + 1|F(x) = −x⁵ − x³ + 1/2 x²",
    voraussetzungen="Potenzregel für Ableitung und Stammfunktion",
    format="Kurzantwort", operator="Ermitteln Sie|Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=A1,
    gesucht="Gleichung der Ableitungsfunktion f'; Gleichung einer Stammfunktion F",
    verfahren="Summandenweise mit der Potenzregel ableiten und aufleiten; eine Stammfunktion ohne Konstante genügt",
    schritte="2", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="f'(x) = −20x³ − 6x + 1; F(x) = −x⁵ − x³ + 1/2 x² (+ C)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="beim Aufleiten den Exponenten nicht erhöhen oder den Faktor 1/2 bei x²/2 vergessen",
    bemerkung="Landesaufgabe (nicht im Pool 2019). Eigene Rechnung, mit sympy bestätigt; Verlagslösung stimmt überein.")
row(id="2019-be-gk-A1.1b", block="A", aufgabe="1.1", titel="Analysis 1", teilaufgabe="b", seite="1", punkte="3",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extremstelle über den Vorzeichenwechsel der Ableitung in ein Intervall einschließen", typ_neben="",
    stichwoerter="f'(0) = 1 > 0, f'(1) = −25 < 0|Vorzeichenwechsel von + nach −|Intervall [0; 1]",
    voraussetzungen="Ableitung aus a|Vorzeichenwechselkriterium für ein Maximum",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=A1 + "; der Graph von f hat ein Maximum an der Stelle x_Max; Ableitung f'(x) = −20x³ − 6x + 1 aus a",
    gesucht="Intervall der Länge 1, in dem x_Max liegen muss, mit Begründung",
    verfahren="Werte der Ableitung an ganzzahligen Stellen prüfen: f'(0) = 1 > 0 und f'(1) = −25 < 0, also Vorzeichenwechsel von + nach − in [0; 1] und dort eine Maximumstelle; die Nullstelle wird nicht berechnet",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="2019-be-gk-A1.1a",
    ergebnis="x_Max ∈ [0; 1], weil f'(0) = 1 > 0 und f'(1) = −25 < 0 (Vorzeichenwechsel von + nach −); alternativ f''(x) = −60x² − 6 < 0 überall, also ist jede Nullstelle von f' eine Maximumstelle (tatsächlich x_Max ≈ 0,154)",
    zwischenergebnis="f'(0) = 1|f'(1) = −25", niveau_geschaetzt="II",
    fehlerquelle="die Nullstelle von f' exakt berechnen wollen (kubische Gleichung) statt das Intervall zu begründen",
    bemerkung="Landesaufgabe. Enge Fassung: Zwischenwertargument am Vorzeichen der Ableitung, ein Schluss ohne Rechnung – II. Eigene Rechnung, mit sympy bestätigt (Nullstelle 0,1544).")
G1 = "Gerade g: x = (5 | 3 | 6) + r · (2 | −5 | −1), r ∈ IR"
row(id="2019-be-gk-A1.3a", block="A", aufgabe="1.3", titel="Geometrie", teilaufgabe="a", seite="1", punkte="3",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Echt parallele und senkrecht schneidende Gerade zu einer gegebenen Geraden angeben", typ_neben="",
    stichwoerter="gleicher Richtungsvektor, anderer Stützpunkt nicht auf g|Richtungsvektor mit Skalarprodukt null, z. B. (1 | 0 | 2)|gemeinsamer Punkt (5 | 3 | 6)",
    voraussetzungen="Parameterform einer Geraden|Skalarprodukt|Punktprobe",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=G1,
    gesucht="Gleichung einer Geraden p, die echt parallel zu g verläuft; Gleichung einer Geraden s, die g senkrecht schneidet",
    verfahren="p: Richtungsvektor von g übernehmen, Stützpunkt außerhalb von g wählen (Punktprobe). s: Richtungsvektor mit Skalarprodukt null zu (2 | −5 | −1) wählen, Stützpunkt auf g (etwa den Stützpunkt von g)",
    schritte="3", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="z. B. p: x = (5 | 4 | 6) + k · (2 | −5 | −1); s: x = (5 | 3 | 6) + t · (1 | 0 | 2) (Skalarprodukt 2 + 0 − 2 = 0)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="für p einen Stützpunkt auf g wählen (dann gleich g) oder für s den Schnittpunkt vergessen",
    bemerkung="Landesaufgabe. Enge Fassung: zwei Bedingungen je Gerade selbst zusammensetzen, keine Rechnung außer dem Skalarprodukt – II. Eigene Rechnung, mit sympy bestätigt; Verlagslösung wählt dieselben Vektoren.")
row(id="2019-be-gk-A1.3b", block="A", aufgabe="1.3", titel="Geometrie", teilaufgabe="b", seite="1", punkte="2",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Schnitt einer senkrecht schneidenden Geraden mit einer parallelen Geraden beurteilen", typ_neben="",
    stichwoerter="g und p spannen eine Ebene auf|s kann aus dieser Ebene herausführen|windschief zu p",
    voraussetzungen="Lagen zweier Geraden im Raum|Raumvorstellung",
    format="Begründung", operator="Entscheiden Sie begründet", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=G1 + "; p echt parallel zu g, s schneidet g senkrecht (aus a)",
    gesucht="Entscheidung mit Begründung, ob jede mögliche Gerade s auch p schneidet",
    verfahren="g und p liegen in einer Ebene; eine Gerade s, die g senkrecht schneidet, muss nicht in dieser Ebene liegen und ist dann windschief zu p",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="2019-be-gk-A1.3a",
    ergebnis="Nein: g und p legen eine Ebene fest; s kann g senkrecht schneiden und dabei aus dieser Ebene herausführen, dann ist s windschief zu p und schneidet p nicht",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="annehmen, dass senkrecht zu g auch senkrecht zu p immer einen Schnittpunkt bedeutet (nur in der Ebene richtig)",
    bemerkung="Landesaufgabe. Enge Fassung: räumliches Gegenbeispiel ohne Rechnung, eine Deutung – II. Eigene Überlegung; Verlagslösung argumentiert gleich.")
row(id="2019-be-gk-A1.4c", block="A", aufgabe="1.4", titel="Stochastik", teilaufgabe="c", seite="2", punkte="3",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit beim zweimaligen Ziehen ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="11 Frauen, 9 Männer|zwei Personen ohne Zurücklegen|Term (11 über 1) · (9 über 1) / (20 über 2) oder 2 · 11/20 · 9/19",
    voraussetzungen="Ziehen ohne Zurücklegen als Pfade oder Binomialkoeffizienten",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Chor / Preisverleihung", textumfang="kurz",
    gegeben="Chor aus 12 Frauen und 9 Männern, die Leiterin (eine Frau) kann nicht teilnehmen; zwei der anderen 20 Mitglieder (11 Frauen, 9 Männer) werden zufällig ausgewählt",
    gesucht="Term für die Wahrscheinlichkeit, dass eine Frau und ein Mann ausgewählt werden",
    verfahren="Zwei Pfade (Frau–Mann, Mann–Frau) mit Pfadregel oder günstige durch mögliche Auswahlen mit Binomialkoeffizienten",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="P = 11/20 · 9/19 + 9/20 · 11/19 = (11 · 9) / (20 über 2) = 99/190 ≈ 0,52 (nur der Term verlangt)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur einen der beiden Pfade nehmen oder mit Zurücklegen rechnen (11/20 · 9/20)",
    bemerkung="Abgewandelt von: 2019MgrundlegendAStochastik11-c; das Heft verlangt nur einen Term („Geben Sie einen Term an“), der Pool die Wahrscheinlichkeit („Bestimmen Sie“). AB amtlich der Poolzeile: II. Typ der Poolzeile übernommen (gleiche Fertigkeit). Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.1 Kiri-Bäume (Seiten 8–9), 40 BE, Landesaufgabe
KB = "Wachstum eines Baums A für t ≥ 0 bis zur maximalen Höhe: h(t) = −0,1 · t⁴ + 20 · t², t in Jahren, h(t) Höhe in cm"
KB2 = "Baum B: g(t) = a · t³ + b · t² (t Jahre, g(t) cm)"
row(id="2019-be-gk-B2.1a", block="B", aufgabe="2.1", titel="Kiri-Bäume", teilaufgabe="a", seite="8", punkte="10",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen",
    typ_neben="Maximum einer ganzrationalen Funktion im Sachzusammenhang über die Ableitung berechnen",
    stichwoerter="h(2) = 78,4, h(8) = 870,4|h'(t) = −0,4t³ + 40t = 0 ⇔ t = 0 oder t = 10|h''(10) = −80 < 0|h(10) = 1000 cm|Wachstumsdauer 10 Jahre",
    voraussetzungen="Funktionswerte berechnen|Ableitung und notwendige/hinreichende Bedingung|Sachbezug t ≥ 0",
    format="Rechnung", operator="Bestimmen Sie|Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="Foto", skizze="Foto eines Kiri-Baums (Darstellung der Prüfungskommission), ohne Werte", kontext="Baumwachstum", textumfang="mittel",
    gegeben=KB,
    gesucht="Höhe nach 2 und nach 8 Jahren; maximale Höhe; Anzahl der Jahre, die der Baum wächst",
    verfahren="Funktionswerte einsetzen; h'(t) = −0,4t³ + 40t = t · (−0,4t² + 40) = 0 mit t = 10 (t = 0 Minimum, −10 entfällt), h''(10) < 0; h(10) = 1000",
    schritte="6", zahlenraum="dezimal", einheiten="cm|Jahre", abhaengig_von="",
    ergebnis="h(2) = 78,4 cm, h(8) = 870,4 cm; maximale Höhe h(10) = 1000 cm (10 m) nach 10 Jahren; der Baum wächst 10 Jahre",
    zwischenergebnis="h'(t) = −0,4t³ + 40t|t_E = 10|h''(10) = −80", niveau_geschaetzt="II",
    fehlerquelle="t = 0 als Maximum werten oder t = −10 nicht ausschließen",
    bemerkung="Landesaufgabe (nicht im Pool 2019). Drei Leistungen: Funktionswerte, Maximum mit hinreichender Bedingung, Wachstumsdauer als Maximumstelle. Eigene Rechnung, mit sympy bestätigt; Verlagslösung stimmt überein.")
row(id="2019-be-gk-B2.1b", block="B", aufgabe="2.1", titel="Kiri-Bäume", teilaufgabe="b", seite="8", punkte="4",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Größte Änderungsrate über das Maximum der Ableitung im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="h''(t) = −1,2t² + 40 = 0 ⇔ t = √(100/3) ≈ 5,77|h'(5,77) ≈ 154 cm/Jahr|nur notwendiges Kriterium verlangt",
    voraussetzungen="Wachstumsgeschwindigkeit = Ableitung|zweite Ableitung|Wurzelgleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Baumwachstum", textumfang="kurz",
    gegeben=KB + "; Ableitung h'(t) = −0,4t³ + 40t (aus a)",
    gesucht="höchste Wachstumsgeschwindigkeit des Baums A in cm/Jahr (Bearbeitung mit dem notwendigen Kriterium genügt)",
    verfahren="Maximum von h' über h''(t) = 0: t² = 100/3, t = 10/√3 ≈ 5,77 (negativ entfällt); h'(t_m) = 800√3/9 ≈ 154",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="cm/Jahr", abhaengig_von="2019-be-gk-B2.1a",
    ergebnis="t_m = 10/√3 ≈ 5,77 Jahre, höchste Wachstumsgeschwindigkeit h'(t_m) = 800√3/9 ≈ 154 cm/Jahr",
    zwischenergebnis="h''(t) = −1,2t² + 40|t_m ≈ 5,77", niveau_geschaetzt="II",
    fehlerquelle="das Maximum von h statt von h' suchen oder t_m als Ergebnis angeben statt h'(t_m)",
    bemerkung="Landesaufgabe. Gegenstück zum Typ „Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen“ (2018-be-gk 1.2 f); Kandidat für eine Zusammenziehung im Abgleichlauf. Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B2.1c", block="B", aufgabe="2.1", titel="Kiri-Bäume", teilaufgabe="c", seite="8", punkte="5",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren", typ_neben="",
    stichwoerter="g(5) = 500: 125a + 25b = 500|g'(5) = 150: 75a + 10b = 150|a = −2, b = 30",
    voraussetzungen="Ableitung des Ansatzes|lineares Gleichungssystem mit zwei Unbekannten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Baumwachstum", textumfang="kurz",
    gegeben=KB2 + "; nach 5 Jahren 500 cm hoch, Wachstumsgeschwindigkeit dann 150 cm/Jahr; Kontrollergebnis g(t) = −2t³ + 30t²",
    gesucht="Funktionsgleichung von g",
    verfahren="g'(t) = 3at² + 2bt; Bedingungen g(5) = 500 und g'(5) = 150 als LGS lösen",
    schritte="4", zahlenraum="ganz|negativ", einheiten="cm|Jahre", abhaengig_von="",
    ergebnis="a = −2, b = 30: g(t) = −2t³ + 30t²",
    zwischenergebnis="125a + 25b = 500|75a + 10b = 150", niveau_geschaetzt="II",
    fehlerquelle="die Steigungsbedingung in g statt in g' einsetzen",
    bemerkung="Landesaufgabe. Kontrollergebnis im Heft durch eigene Rechnung bestätigt (sympy).")
row(id="2019-be-gk-B2.1d", block="B", aufgabe="2.1", titel="Kiri-Bäume", teilaufgabe="d", seite="8", punkte="7",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen",
    typ_neben="Zeitpunkte gleicher Änderungsrate zweier Modelle über die Gleichung der Ableitungen berechnen",
    stichwoerter="h(0) = g(0) = 0|h'(t) = g'(t): −0,4t³ + 40t = −6t² + 60t|t · (0,4t² − 6t + 20) = 0 ⇔ t = 0, 5, 10",
    voraussetzungen="Ableitungen beider Modelle|Gleichung dritten Grades durch Ausklammern und p-q-Formel lösen",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Baumwachstum", textumfang="kurz",
    gegeben=KB + "; " + KB2 + " mit g(t) = −2t³ + 30t² (aus c); beide beginnen bei t = 0",
    gesucht="Höhe beider Bäume zu Beobachtungsbeginn; Zeiten mit gleicher Wachstumsgeschwindigkeit",
    verfahren="Funktionswerte bei t = 0; Ableitungen gleichsetzen, t ausklammern, quadratische Gleichung 0,4t² − 6t + 20 = 0 lösen",
    schritte="4", zahlenraum="dezimal", einheiten="cm|Jahre", abhaengig_von="2019-be-gk-B2.1c",
    ergebnis="Beide Bäume sind zu Beginn 0 cm hoch; gleiche Wachstumsgeschwindigkeit bei t = 0, t = 5 und t = 10 Jahren",
    zwischenergebnis="g'(t) = −6t² + 60t|0,4t² − 6t + 20 = 0 ⇔ t = 5 oder t = 10", niveau_geschaetzt="II",
    fehlerquelle="die Funktionen statt der Ableitungen gleichsetzen oder t = 0 beim Ausklammern verlieren",
    bemerkung="Landesaufgabe. Erste Leistung trivial (Startwert 0), Hauptleistung in typ_neben. Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B2.1e", block="B", aufgabe="2.1", titel="Kiri-Bäume", teilaufgabe="e", seite="8", punkte="4",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Zeitpunkte größter Differenz zweier Änderungsraten über die Extremstellen der Differenzfunktion berechnen", typ_neben="",
    stichwoerter="d(t) = g'(t) − h'(t) = 0,4t³ − 6t² + 20t|d'(t) = 1,2t² − 12t + 20 = 0|t ≈ 2,1 und t ≈ 7,9",
    voraussetzungen="Differenzfunktion aufstellen|quadratische Gleichung|hinreichende Bedingung nicht gefordert",
    format="Rechnung", operator="Untersuchen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Baumwachstum", textumfang="kurz",
    gegeben="h'(t) = −0,4t³ + 40t und g'(t) = −6t² + 60t (Wachstumsgeschwindigkeiten der Bäume A und B aus a und c), 0 ≤ t ≤ 10",
    gesucht="Zeiten, zu denen die Wachstumsgeschwindigkeiten am stärksten voneinander abweichen (ohne hinreichende Bedingung)",
    verfahren="Differenz d = g' − h' bilden, d' = 0 lösen: t² − 10t + 50/3 = 0, t = 5 ∓ 5/√3",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="Jahre", abhaengig_von="2019-be-gk-B2.1c",
    ergebnis="t = 5 − 5/√3 ≈ 2,1 Jahre (B wächst am stärksten schneller) und t = 5 + 5/√3 ≈ 7,9 Jahre (A am stärksten schneller)",
    zwischenergebnis="d(t) = 0,4t³ − 6t² + 20t|d'(t) = 1,2t² − 12t + 20", niveau_geschaetzt="II",
    fehlerquelle="die Differenz der Höhen statt der Geschwindigkeiten untersuchen oder den Betrag bilden und nur ein Maximum finden",
    bemerkung="Landesaufgabe. Enge Fassung: Modell der Differenzfunktion ist vorgezeichnet („Wachstumsgeschwindigkeiten abweichen“), Rechnung Standard – II. Eigene Rechnung, mit sympy bestätigt (2,113 und 7,887).")
row(id="2019-be-gk-B2.1f", block="B", aufgabe="2.1", titel="Kiri-Bäume", teilaufgabe="f", seite="9", punkte="4",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen", typ_neben="",
    stichwoerter="Wertetabelle g'(t) für t = 0, 2, 4, 5, 6, 8, 10|Werte 0, 96, 144, 150, 144, 96, 0|Parabel mit Scheitel (5 | 150) neben dem Graphen von h'",
    voraussetzungen="Funktionswerte von g' berechnen|Punkte in ein Koordinatensystem übertragen",
    format="Tabelle|Zeichnen", operator="Ergänzen Sie|Zeichnen Sie", antwort="Tabelle|Grafik",
    material="Koordinatensystem", skizze="Anlage: Koordinatensystem auf Gitter, t von 0 bis 10 (Jahre), Wachstumsgeschwindigkeit in cm/Jahr von 0 bis 160; eingezeichnet der Graph von h' (Nullstellen 0 und 10, Maximum ≈ 154 bei t ≈ 5,8, Beschriftung h'); Wertetabelle mit t = 0, 2, 4, 5, 6, 8, 10 und den vorgegebenen Werten g'(2) = 96, g'(5) = 150, g'(8) = 96, übrige Felder leer", kontext="Baumwachstum", textumfang="kurz",
    gegeben="g'(t) = −6t² + 60t (aus c); Anlage mit dem Graphen von h' und einer teilweise gefüllten Wertetabelle",
    gesucht="Wertetabelle ergänzen (g'(0), g'(4), g'(6), g'(10)); Graph von g' für 0 ≤ t ≤ 10 in die Anlage einzeichnen",
    verfahren="Werte einsetzen und die Parabel durch die sieben Punkte zeichnen",
    schritte="2", zahlenraum="ganz", einheiten="cm/Jahr|Jahre", abhaengig_von="2019-be-gk-B2.1c",
    ergebnis="g'(0) = 0, g'(4) = 144, g'(6) = 144, g'(10) = 0; Graph von g': nach unten geöffnete Parabel mit Scheitel (5 | 150), Nullstellen 0 und 10, schneidet h' bei t = 5",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Werte von g statt g' berechnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-be-gk 1.1 f). Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B2.1g", block="B", aufgabe="2.1", titel="Kiri-Bäume", teilaufgabe="g", seite="9", punkte="6",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Integral der Differenz zweier Änderungsraten berechnen und als Bestandsdifferenz deuten", typ_neben="",
    stichwoerter="Integral von 0 bis 5 über (g' − h') = [0,1t⁴ − 2t³ + 10t²] = 62,5|Höhenunterschied nach 5 Jahren|gleiche Starthöhe 0 (d), Schnittstelle 5 (f)",
    voraussetzungen="Integral einer Differenzfunktion|Hauptsatz: Integral der Rate = Bestandsänderung",
    format="Rechnung|Begründung", operator="Berechnen Sie|Interpretieren Sie", antwort="Zahl|Text",
    material="Koordinatensystem", skizze="wie f: Anlage mit den Graphen von h' und g', die im I. Quadranten zwei Teilflächen einschließen (Schnittstellen 0, 5, 10)", kontext="Baumwachstum", textumfang="mittel",
    gegeben="Graphen von g'(t) = −6t² + 60t und h'(t) = −0,4t³ + 40t schließen im I. Quadranten zwei Teilflächen ein; Intervall I = [0; 5]; aus d: beide Bäume starten mit Höhe 0, aus f: Schnittstelle der Graphen bei t = 5",
    gesucht="Flächeninhalt der Teilfläche in [0; 5]; Interpretation im Sachzusammenhang unter Einbeziehung von d und f",
    verfahren="Auf [0; 5] gilt g' ≥ h'; Integral der Differenz 0,4t³ − 6t² + 20t von 0 bis 5 = 62,5; Deutung: Integral der Geschwindigkeitsdifferenz = Höhenunterschied, da beide bei 0 starten",
    schritte="4", zahlenraum="dezimal", einheiten="cm", abhaengig_von="2019-be-gk-B2.1d|2019-be-gk-B2.1f",
    ergebnis="Flächeninhalt 62,5 (FE); Baum B ist nach 5 Jahren 62,5 cm (ca. 63 cm) höher als Baum A, weil beide mit Höhe 0 starten und B bis t = 5 die größere Wachstumsgeschwindigkeit hat",
    zwischenergebnis="Stammfunktion 0,1t⁴ − 2t³ + 10t²", niveau_geschaetzt="III",
    fehlerquelle="das Integral als Höhe eines Baums statt als Höhenunterschied deuten",
    bemerkung="Landesaufgabe. Enge Fassung: Rechnung plus Deutung des Integrals der Ratendifferenz als Bestandsdifferenz unter Rückgriff auf zwei Teilaufgaben – Kombinieren mit Deutung, III. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.2 Hormonpflaster (Seiten 17–19), 40 BE, Landesaufgabe
HP = "Hormonspiegel h(t) = 8t · e^(−0,04t) + 50, t ≥ 0 Zeit in Tagen ab Behandlungsbeginn, h(t) Anteil am Sollwert in Prozent (Ausgangswert 50 %)"
HP_SK = "Koordinatensystem auf Gitter, t von 0 bis 140 (Tage), y in Prozentpunkten von 0 bis 140: Graph von h startet bei 50, steigt steil auf ein Maximum bei etwa (25 | 124) und fällt danach langsam gegen 50; Beschriftung h"
row(id="2019-be-gk-B2.2a", block="B", aufgabe="2.2", titel="Hormonpflaster", teilaufgabe="a", seite="17", punkte="3",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben", typ_neben="",
    stichwoerter="8t · e^(−0,04t) → 0, e-Faktor dominiert|h(t) → 50|Hormonspiegel nähert sich dem Ausgangswert 50 %",
    voraussetzungen="Grenzverhalten von t · e^(−kt)",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="Koordinatensystem", skizze=HP_SK, kontext="Medizin / Hormonpflaster", textumfang="lang",
    gegeben=HP,
    gesucht="Verhalten der Funktionswerte von h für t → +∞",
    verfahren="Der Faktor e^(−0,04t) geht schneller gegen 0, als t wächst; der Summand 50 bleibt",
    schritte="1", zahlenraum="dezimal", einheiten="%|Tage", abhaengig_von="",
    ergebnis="h(t) → 50 für t → +∞ (der Hormonspiegel fällt langfristig auf den Ausgangswert 50 % zurück)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="wegen des Faktors 8t Wachstum gegen unendlich annehmen",
    bemerkung="Landesaufgabe (nicht im Pool 2019). Typ wiederverwendet (2023-bebb-gk 2.1 a). Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B2.2b", block="B", aufgabe="2.2", titel="Hormonpflaster", teilaufgabe="b", seite="17", punkte="7",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen", typ_neben="",
    stichwoerter="h'(t) = (8 − 0,32t) · e^(−0,04t)|h'(t) = 0 ⇔ t = 25|h(25) = 200/e + 50 ≈ 123,6|nur notwendige Bedingung verlangt",
    voraussetzungen="Produkt- und Kettenregel|e-Faktor nie null",
    format="Rechnung", operator="Ermitteln Sie|Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=HP_SK, kontext="Medizin / Hormonpflaster", textumfang="kurz",
    gegeben=HP + "; Kontrollergebnis h'(t) = (8 − 0,32t) · e^(−0,04t)",
    gesucht="Zeitpunkt des maximalen Hormonspiegels und dessen Wert (Verwendung der notwendigen Bedingung genügt)",
    verfahren="Ableiten mit Produkt- und Kettenregel, ersten Faktor null setzen, Funktionswert berechnen",
    schritte="4", zahlenraum="dezimal", einheiten="%|Tage", abhaengig_von="",
    ergebnis="t = 25 Tage; h(25) = 200 · e^(−1) + 50 ≈ 123,6 %",
    zwischenergebnis="h'(t) = (8 − 0,32t) · e^(−0,04t)", niveau_geschaetzt="II",
    fehlerquelle="Kettenregel beim Ableiten von e^(−0,04t) vergessen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2025-ga-B). Kontrollergebnis und Werte durch eigene Rechnung bestätigt (sympy: 123,576).")
row(id="2019-be-gk-B2.2c", block="B", aufgabe="2.2", titel="Hormonpflaster", teilaufgabe="c", seite="18", punkte="5",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen",
    typ_neben="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen",
    stichwoerter="h''(t) = (−0,64 + 0,0128t) · e^(−0,04t) = 0 ⇔ t = 50|h(50) ≈ 104,1|h'(50) ≈ −1,08 % pro Tag",
    voraussetzungen="Wendestelle als Extremstelle der Ableitung|zweite Ableitung vorgegeben",
    format="Rechnung", operator="Ermitteln Sie|Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=HP_SK, kontext="Medizin / Hormonpflaster", textumfang="mittel",
    gegeben=HP + "; ohne Nachweis: h''(t) = (−0,64 + 0,0128t) · e^(−0,04t); h'(t) = (8 − 0,32t) · e^(−0,04t) aus b",
    gesucht="Zeitpunkt, an dem der Hormonspiegel am stärksten fällt (notwendige Bedingung genügt); Hormonspiegel und lokale Änderungsrate zu diesem Zeitpunkt",
    verfahren="h''(t) = 0 lösen (erster Faktor), dann h(50) und h'(50) berechnen",
    schritte="4", zahlenraum="dezimal|negativ", einheiten="%|Tage|% pro Tag", abhaengig_von="2019-be-gk-B2.2b",
    ergebnis="t = 50 Tage; h(50) = 400 · e^(−2) + 50 ≈ 104,1 %; h'(50) = −8 · e^(−2) ≈ −1,08 % pro Tag",
    zwischenergebnis="−0,64 + 0,0128t = 0", niveau_geschaetzt="II",
    fehlerquelle="die Nullstelle von h' (Maximum) statt von h'' nehmen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2022-ea-B); hier über die vorgegebene zweite Ableitung. Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B2.2d", block="B", aufgabe="2.2", titel="Hormonpflaster", teilaufgabe="d", seite="18", punkte="3",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate aus dem Funktionsterm im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="(h(7) − h(0)) / 7|h(7) ≈ 92,3, h(0) = 50|≈ 6,0 Prozentpunkte pro Tag",
    voraussetzungen="Differenzenquotient",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Medizin / Hormonpflaster", textumfang="kurz",
    gegeben=HP,
    gesucht="mittlere Änderungsrate des Hormonspiegels in den ersten sieben Tagen",
    verfahren="Differenzenquotient über [0; 7]",
    schritte="2", zahlenraum="dezimal", einheiten="% pro Tag|Tage", abhaengig_von="",
    ergebnis="(h(7) − h(0)) / 7 ≈ (92,3 − 50) / 7 ≈ 6,0 Prozentpunkte pro Tag",
    zwischenergebnis="h(7) = 56 · e^(−0,28) + 50 ≈ 92,32", niveau_geschaetzt="I",
    fehlerquelle="h'(7) (momentane Rate) statt des Differenzenquotienten berechnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2017-ea-A). Eigene Rechnung, mit sympy bestätigt (6,046).")
row(id="2019-be-gk-B2.2e", block="B", aufgabe="2.2", titel="Hormonpflaster", teilaufgabe="e", seite="18", punkte="4",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Mittelwert einer Funktion als Integral geteilt durch die Intervalllänge berechnen und deuten", typ_neben="",
    stichwoerter="Stammfunktion H(t) = (−200t − 5000) · e^(−0,04t) + 50t vorgegeben|1/70 · (H(70) − H(0)) ≈ 104,9 > 100|mittlerer Hormonspiegel über 70 Tage",
    voraussetzungen="Hauptsatz mit vorgegebener Stammfunktion|Integral als Mittelwert deuten",
    format="Rechnung", operator="Weisen Sie nach", antwort="Zahl",
    material="keins", skizze="keine", kontext="Medizin / Hormonpflaster", textumfang="kurz",
    gegeben=HP + "; ohne Nachweis verwendbar: H(t) = (−200t − 5000) · e^(−0,04t) + 50t ist eine Stammfunktion von h",
    gesucht="Nachweis, dass 1/70 · Integral von 0 bis 70 über h(t) dt > 100 gilt",
    verfahren="Integral mit der Stammfunktion auswerten: H(70) − H(0) = −19000 · e^(−2,8) + 3500 + 5000; durch 70 teilen",
    schritte="3", zahlenraum="dezimal", einheiten="%|Tage", abhaengig_von="",
    ergebnis="1/70 · (H(70) − H(0)) = 1/70 · (8500 − 19000 · e^(−2,8)) ≈ 104,9 > 100; der mittlere Hormonspiegel der ersten 70 Tage liegt über dem Sollwert",
    zwischenergebnis="H(70) = −19000 · e^(−2,8) + 3500|H(0) = −5000", niveau_geschaetzt="II",
    fehlerquelle="H(0) = −5000 vergessen (Vorzeichen) oder den Faktor 1/70 weglassen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2023-bebb-gk 2.2 i); hier mit vorgegebener Stammfunktion, Nachweis einer Ungleichung. Eigene Rechnung, mit sympy bestätigt (104,92).")
row(id="2019-be-gk-B2.2f", block="B", aufgabe="2.2", titel="Hormonpflaster", teilaufgabe="f", seite="18", punkte="6",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen",
    typ_neben="Stelle zu einem vorgegebenen Wert einer linearen Funktion über eine Ungleichung berechnen",
    stichwoerter="m = h'(70) ≈ −0,88|h(70) ≈ 84,1|g(t) ≈ −0,88t + 145,7|g(t) ≤ 50 ⇔ t ≥ 108,75",
    voraussetzungen="Ableitungswert als Tangentensteigung|Punkt-Steigungs-Form|lineare Ungleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="Medizin / Hormonpflaster", textumfang="mittel",
    gegeben=HP + "; nach 70 Tagen wird das Pflaster entfernt, danach verläuft der Hormonspiegel entlang der Tangente g im Punkt P(70 | h(70)); Kontrollergebnis g(t) ≈ −0,88 · t + 145,7; h'(t) = (8 − 0,32t) · e^(−0,04t)",
    gesucht="Gleichung von g; Zeitpunkt, ab dem g(t) ≤ 50 gilt",
    verfahren="m = h'(70), n aus g(70) = h(70); lineare Ungleichung −0,88t + 145,7 ≤ 50 nach t auflösen",
    schritte="4", zahlenraum="dezimal|negativ", einheiten="%|Tage", abhaengig_von="2019-be-gk-B2.2b",
    ergebnis="g(t) ≈ −0,88 · t + 145,7 (exakt m = −14,4 · e^(−2,8) ≈ −0,876, n ≈ 145,3); g(t) ≤ 50 ab t ≈ 108,75 Tagen (mit exakten Werten ≈ 108,9)",
    zwischenergebnis="h'(70) ≈ −0,876|h(70) ≈ 84,05", niveau_geschaetzt="II",
    fehlerquelle="beim Auflösen der Ungleichung durch eine negative Zahl das Relationszeichen nicht umkehren",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2025-ga-A). Kontrollergebnis mit gerundeten Werten; eigene Rechnung mit sympy (108,89 exakt, 108,75 mit den gerundeten Heftwerten).")
row(id="2019-be-gk-B2.2g", block="B", aufgabe="2.2", titel="Hormonpflaster", teilaufgabe="g", seite="18", punkte="6",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Parameter einer Exponentialfunktion aus einer Ungleichung für einen Funktionswert im Sachzusammenhang ermitteln", typ_neben="",
    stichwoerter="h_k(t) = k · t · e^(−0,04t) + 50|h_k(70) ≥ 100 ⇔ 70k · e^(−2,8) ≥ 50|k ≥ 50 · e^(2,8) / 70 ≈ 11,75",
    voraussetzungen="Ungleichung mit Parameter|Exponentialwert auswerten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Medizin / Hormonpflaster", textumfang="mittel",
    gegeben="Erhöhte Wirkstoffmenge: h_k(t) = k · t · e^(−0,04t) + 50, t ≥ 0, k ≥ 0",
    gesucht="Wert von k, ab dem der Hormonspiegel am 70. Tag noch mindestens 100 erreicht",
    verfahren="h_k(70) ≥ 100 nach k auflösen",
    schritte="3", zahlenraum="dezimal", einheiten="%|Tage", abhaengig_von="",
    ergebnis="k ≥ 50 · e^(2,8) / 70 ≈ 11,75",
    zwischenergebnis="70k · e^(−2,8) ≥ 50", niveau_geschaetzt="II",
    fehlerquelle="e^(−2,8) auf die falsche Seite bringen (k ≥ 50 · e^(−2,8) / 70)",
    bemerkung="Landesaufgabe. Schar h_k im Grundkurs; das Thema Funktionsscharen gilt für be-gk nicht, die Fertigkeit ist das Lösen der Ungleichung in k, deshalb Thema Gleichungen lösen. Eigene Rechnung, mit sympy bestätigt (11,746).")
row(id="2019-be-gk-B2.2h", block="B", aufgabe="2.2", titel="Hormonpflaster", teilaufgabe="h", seite="18|19", punkte="6",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Einfluss eines multiplikativen Parameters auf den Graphen im Vergleich mit dem Ausgangsgraphen beschreiben", typ_neben="",
    stichwoerter="gleicher Startwert 50|gleicher Grenzwert 50|h_k liegt für k > 8 oberhalb von h|größeres Maximum|Maximumstelle stets t = 25",
    voraussetzungen="Grenzwert und Extremstelle von t · e^(−0,04t)|Graphen lesen",
    format="Begründung", operator="Vergleichen Sie", antwort="Text",
    material="Koordinatensystem", skizze="Koordinatensystem auf Gitter, t von 0 bis 140, y in Prozentpunkten 0 bis 140: Graph von h (Maximum ≈ 124 bei 25) und darüber der Graph von h_10 (Maximum ≈ 142 bei 25), beide von 50 startend und gegen 50 fallend; Beschriftungen h, h_10", kontext="Medizin / Hormonpflaster", textumfang="mittel",
    gegeben="h(t) = 8t · e^(−0,04t) + 50 und h_k(t) = k · t · e^(−0,04t) + 50 mit k > 8; Abbildung mit h und h_10",
    gesucht="mindestens drei Gemeinsamkeiten oder Unterschiede der Graphen von h und h_k",
    verfahren="Startwert, Grenzwert, Lage zueinander, Maximum und Maximumstelle aus Term und Abbildung vergleichen",
    schritte="0", zahlenraum="dezimal", einheiten="%|Tage", abhaengig_von="",
    ergebnis="Gemeinsam: Startwert h_k(0) = h(0) = 50, Grenzwert 50 für t → ∞, Maximumstelle t = 25 für jedes k; Unterschiede: für t > 0 liegt h_k oberhalb von h, das Maximum von h_k ist größer (h_10(25) ≈ 142 gegen 123,6)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="eine Verschiebung der Maximumstelle behaupten (der Faktor k ändert sie nicht)",
    bemerkung="Landesaufgabe. Thema Funktionsscharen gilt für be-gk nicht (Geltungstabelle); das Heft fragt es trotzdem. Eigene Rechnung, mit sympy bestätigt (Maximumstelle 25 für alle k).")
# ---- Aufgabe 3.1 Tunnel (Seite 25), 20 BE, Landesaufgabe
TU = "Autotunnel als Teil einer Geraden von S(0 | 40 | 6) nach N(30 | 65 | 7); x-y-Ebene auf Meeresspiegelhöhe, 1 LE = 100 m"
row(id="2019-be-gk-B3.1a", block="B", aufgabe="3.1", titel="Tunnel", teilaufgabe="a", seite="25", punkte="5",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Geradengleichung durch zwei Punkte aufstellen",
    typ_neben="Streckenlänge im Raum berechnen|Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen",
    stichwoerter="g: x = (0 | 40 | 6) + r · (30 | 25 | 1)|Länge √1526 ≈ 39,06 LE ≈ 3906 m|sin α = 1/√1526, α ≈ 1,5°",
    voraussetzungen="Verbindungsvektor|Betrag eines Vektors|Winkel Gerade–Ebene mit Normalenvektor (0 | 0 | 1)",
    format="Kurzantwort|Rechnung", operator="Geben Sie an|Berechnen Sie|Ermitteln Sie", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="Tunnelbau", textumfang="mittel",
    gegeben=TU,
    gesucht="Gleichung der Geraden g; Länge des Autotunnels; Winkel, in dem g zur x-y-Ebene ansteigt",
    verfahren="Richtungsvektor N − S; Betrag mal 100 m; sin α = |u · n| / (|u| · |n|) mit n = (0 | 0 | 1)",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="m|LE|°", abhaengig_von="",
    ergebnis="g: x = (0 | 40 | 6) + r · (30 | 25 | 1), r ∈ IR; Länge |SN| = √1526 ≈ 39,06 LE ≈ 3906 m; Anstiegswinkel sin α = 1/√1526, α ≈ 1,5°",
    zwischenergebnis="SN = (30 | 25 | 1)", niveau_geschaetzt="II",
    fehlerquelle="den Maßstab 1 LE = 100 m vergessen oder cos statt sin für den Winkel Gerade–Ebene nehmen",
    bemerkung="Landesaufgabe (nicht im Pool 2019). Drei Leistungen; die Nebentypen sind Bestandstypen (2018-bb-ea, 2023-ga-B). Eigene Rechnung, mit sympy bestätigt (39,064; 1,467°).")
row(id="2019-be-gk-B3.1b", block="B", aufgabe="3.1", titel="Tunnel", teilaufgabe="b", seite="25", punkte="5",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Durchstoßpunkt einer achsenparallelen Geraden mit einer Ebene berechnen und Abstand im Sachzusammenhang angeben", typ_neben="",
    stichwoerter="Lotgerade h: x = (15 | 52,5 | 6,5) + t · (0 | 0 | 1)|Einsetzen in F: 7 · (6,5 + t) = 475,5 − 412,5 ⇔ t = 2,5|D(15 | 52,5 | 9)|2,5 LE = 250 m, plus 2 m",
    voraussetzungen="Gerade in Ebene einsetzen|Maßstab",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Tunnelbau", textumfang="mittel",
    gegeben=TU + "; Nothaltebucht L(15 | 52,5 | 6,5); Lüftungsrohr senkrecht zum Meeresspiegel nach oben, ragt 2 m aus dem Berg; Bergoberfläche F: 10x + 5y + 7z = 475,5",
    gesucht="Länge des Lüftungsrohrs",
    verfahren="Senkrechte Gerade durch L (Richtung (0 | 0 | 1)) mit F schneiden, z-Differenz mal 100 m plus 2 m",
    schritte="4", zahlenraum="dezimal", einheiten="m|LE", abhaengig_von="",
    ergebnis="Durchstoßpunkt D(15 | 52,5 | 9); Rohr im Berg 2,5 LE = 250 m, insgesamt 252 m",
    zwischenergebnis="t_D = 2,5", niveau_geschaetzt="II",
    fehlerquelle="den Abstand von L zur Ebene (Lot senkrecht zu F) statt der senkrechten Strecke berechnen oder die 2 m vergessen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B3.1c", block="B", aufgabe="3.1", titel="Tunnel", teilaufgabe="c", seite="25", punkte="5",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Parallelität zweier Geraden über die Richtungsvektoren prüfen",
    typ_neben="Punkt auf einer Geraden mit vorgegebener Koordinate angeben",
    stichwoerter="AB = (40 | 5 | −0,5) nicht kollinear zu (30 | 25 | 1)|nicht parallel|z = 6,4 ⇔ 6,5 − 0,5t = 6,4 ⇔ t = 0,2|P(28 | 61 | 6,4)",
    voraussetzungen="Kollinearität prüfen|Parameter aus einer Koordinate bestimmen",
    format="Rechnung", operator="Untersuchen Sie|Bestimmen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Tunnelbau", textumfang="mittel",
    gegeben=TU + "; Bahntunnel als Gerade durch A(20 | 60 | 6,5) und B(60 | 65 | 6)",
    gesucht="ob der Bahntunnel parallel zum Autotunnel verläuft; Punkt P des Bahntunnels in 640 m Höhe",
    verfahren="Richtungsvektoren (40 | 5 | −0,5) und (30 | 25 | 1) auf Vielfache prüfen; z-Koordinate 6,4 in die Gerade AB einsetzen",
    schritte="4", zahlenraum="dezimal|negativ", einheiten="m|LE", abhaengig_von="2019-be-gk-B3.1a",
    ergebnis="Nicht parallel (kein gemeinsamer Faktor: 40/30 ≠ 5/25); P(28 | 61 | 6,4)",
    zwischenergebnis="t = 0,2 auf AB", niveau_geschaetzt="II",
    fehlerquelle="640 m nicht in 6,4 LE umrechnen",
    bemerkung="Landesaufgabe. Nebentyp wiederverwendet (2025-ga-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B3.1d", block="B", aufgabe="3.1", titel="Tunnel", teilaufgabe="d", seite="25", punkte="5",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Punkt: Begegnungspunkt zweier gleichzeitig startender Bewegungen auf einer Strecke aus den Geschwindigkeiten berechnen", typ_neben="",
    stichwoerter="Tunnellänge |AB| = √1625,25 ≈ 40,31 LE ≈ 4031 m|gleiche Zeit: s/100 = (4031 − s)/80|s ≈ 2240 m",
    voraussetzungen="Streckenlänge|Weg = Geschwindigkeit · Zeit|lineare Gleichung",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Tunnelbau / Züge", textumfang="mittel",
    gegeben="Bahntunnel von A(20 | 60 | 6,5) nach B(60 | 65 | 6), 1 LE = 100 m; Güterzug ab A mit 80 km/h, Personenzug ab B mit 100 km/h, gleichzeitiger Start",
    gesucht="Weg des Personenzugs im Tunnel, bis die Loks aneinander vorbeifahren",
    verfahren="Tunnellänge als |AB| · 100 m; Zeiten gleichsetzen: s/100 = (L − s)/80, nach s auflösen (s = L · 100/180)",
    schritte="4", zahlenraum="dezimal", einheiten="m|km|km/h", abhaengig_von="",
    ergebnis="L ≈ 4031 m; s = 5/9 · L ≈ 2240 m (≈ 2,24 km)",
    zwischenergebnis="|AB| ≈ 40,31 LE", niveau_geschaetzt="III",
    fehlerquelle="den Weg des Güterzugs angeben oder die Geschwindigkeiten als Anteile 100/80 direkt verwenden",
    bemerkung="Landesaufgabe. Enge Fassung: eigener Ansatz über die Gleichheit der Zeiten, nicht vorgegeben – III. Eigene Rechnung, mit sympy bestätigt (2239,7 m).")
# ---- Aufgabe 3.2 Würfel (Seite 31), 20 BE – Pool 2019 grundlegend AG/LA (A2) WTR 1 (Reserve, nicht erfasst): Vormerkungen
WU = "Würfel ABCDEFGH mit G(5 | 5 | 5) und H(0 | 5 | 5) im Koordinatensystem; I(5 | 0 | 1), J(2 | 5 | 0), K(0 | 5 | 2), L(1 | 0 | 5) liegen auf Kanten"
WU_SK = "Schrägbild des Würfels ABCDEFGH (Kantenlänge 5, A im Ursprung, B auf der x-Achse, D auf der y-Achse, E auf der z-Achse) mit Achsen und Beschriftung aller Ecken; die Punkte I, J, K, L sind nicht eingezeichnet"
row(id="2019-be-gk-B3.2a", block="B", aufgabe="3.2", titel="Würfel", teilaufgabe="a", seite="31", punkte="2",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Viereck in ein Schrägbild einzeichnen", typ_neben="",
    stichwoerter="I auf Kante BF, J auf CD, K auf DH, L auf EF|Viereck IJKL",
    voraussetzungen="Punkte im Schrägbild verorten",
    format="Zeichnen", operator="Zeichnen Sie", antwort="Grafik",
    material="Körper", skizze=WU_SK, kontext="ohne", textumfang="kurz",
    gegeben=WU,
    gesucht="Viereck IJKL in die Abbildung einzeichnen",
    verfahren="Die vier Punkte auf den Kanten markieren und verbinden",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Viereck IJKL mit I auf BF (x = 5, z = 1), J auf CD (x = 2, y = 5), K auf DH (y = 5, z = 2), L auf EF (x = 1, z = 5)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Punkte auf falsche Kanten setzen",
    bemerkung="Poolaufgabe (nicht erfasst): 2019MgrundlegendBAGLAA2WTR1-1a. Wortgleich mit der Poolaufgabe 2019 grundlegend AG/LA (A2) WTR 1 a (Reserve-Stapel 2019-ga-B); Typ aus dem Bestand (2018-ea-B). Eigene Lösung.")
row(id="2019-be-gk-B3.2b", block="B", aufgabe="3.2", titel="Würfel", teilaufgabe="b", seite="31", punkte="4",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Ebene Figur: Trapez mit zwei gleich langen Seiten über Kollinearität und Seitenlängen nachweisen", typ_neben="",
    stichwoerter="IL = (−4 | 0 | 4) = 2 · JK mit JK = (−2 | 0 | 2)|IL ∥ JK und |IL| = 2 · |JK||IJ = (−3 | 5 | −1), KL = (1 | −5 | 3), beide Länge √35",
    voraussetzungen="Verbindungsvektoren|Kollinearität|Beträge",
    format="Begründung|Rechnung", operator="Begründen Sie|Weisen Sie nach", antwort="Text",
    material="Körper", skizze=WU_SK, kontext="ohne", textumfang="kurz",
    gegeben=WU,
    gesucht="Begründung, dass IJKL ein Trapez mit zwei gleich langen Seiten ist; Nachweis, dass IL doppelt so lang ist wie JK",
    verfahren="IL = 2 · JK zeigt Parallelität und das Längenverhältnis; |IJ| = |KL| = √35 über Beträge",
    schritte="3", zahlenraum="ganz|Wurzel|negativ", einheiten="", abhaengig_von="",
    ergebnis="IL = (−4 | 0 | 4) = 2 · (−2 | 0 | 2) = 2 · JK: IL ∥ JK (Trapez) und |IL| = 2 · |JK| (√32 = 2 · √8); |IJ| = |KL| = √35, also zwei gleich lange Schenkel",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur die Parallelität zeigen und die gleich langen Seiten vergessen",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2019MgrundlegendBAGLAA2WTR1-1b; das Heft sagt „Begründen Sie“ und „zwei Seiten gleich lang“, der Pool „Zeigen Sie“ und „zwei gegenüberliegende Seiten gleich lang“. Reserve-Stapel 2019-ga-B. Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B3.2c", block="B", aufgabe="3.2", titel="Würfel", teilaufgabe="c", seite="31", punkte="2",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Innenwinkel eines Vierecks über das Skalarprodukt der Seitenvektoren berechnen", typ_neben="",
    stichwoerter="Winkel bei I zwischen IL = (−4 | 0 | 4) und IJ = (−3 | 5 | −1)|cos φ = 8 / (√32 · √35) ≈ 0,239|φ ≈ 76,2°",
    voraussetzungen="Skalarprodukt und Beträge|Arkuskosinus",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=WU_SK, kontext="ohne", textumfang="kurz",
    gegeben=WU + "; Trapez IJKL aus b",
    gesucht="Größe eines Innenwinkels des Trapezes IJKL",
    verfahren="cos φ = (IL · IJ) / (|IL| · |IJ|) für den Winkel bei I",
    schritte="2", zahlenraum="ganz|Wurzel|negativ", einheiten="°", abhaengig_von="2019-be-gk-B3.2b",
    ergebnis="Innenwinkel bei I (und bei L): φ ≈ 76,2°; bei J und K entsprechend ≈ 103,8°",
    zwischenergebnis="IL · IJ = 12 + 0 − 4 = 8", niveau_geschaetzt="I",
    fehlerquelle="Vektoren mit falscher Orientierung (Außenwinkel) verwenden",
    bemerkung="Poolaufgabe (nicht erfasst): 2019MgrundlegendBAGLAA2WTR1-1c. Wortgleich mit der Poolaufgabe (Reserve-Stapel 2019-ga-B). Eigene Rechnung, mit sympy bestätigt (76,17°).")
row(id="2019-be-gk-B3.2d", block="B", aufgabe="3.2", titel="Würfel", teilaufgabe="d", seite="31", punkte="4",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Ebene Figur: Flächeninhalt eines Trapezes im Raum über die Höhe zwischen den parallelen Seiten berechnen", typ_neben="",
    stichwoerter="Mittelpunkte M1(3 | 0 | 3) von IL und M2(1 | 5 | 1) von JK|Höhe |M1M2| = √33|A = 1/2 · (√32 + √8) · √33 = 3√66 ≈ 24,37",
    voraussetzungen="Trapezformel|Mittelpunkt einer Strecke|Betrag",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=WU_SK, kontext="ohne", textumfang="kurz",
    gegeben=WU + "; IL ∥ JK mit |IL| = √32, |JK| = √8 (aus b), gleich lange Schenkel",
    gesucht="Flächeninhalt des Trapezes IJKL",
    verfahren="Höhe als Abstand der Mittelpunkte der parallelen Seiten (symmetrisches Trapez), dann Trapezformel",
    schritte="3", zahlenraum="Wurzel|dezimal", einheiten="FE", abhaengig_von="2019-be-gk-B3.2b",
    ergebnis="A = 1/2 · (√32 + √8) · √33 = 3√66 ≈ 24,37 FE",
    zwischenergebnis="h = √33", niveau_geschaetzt="II",
    fehlerquelle="die Schenkellänge √35 als Höhe verwenden",
    bemerkung="Poolaufgabe (nicht erfasst): 2019MgrundlegendBAGLAA2WTR1-1d. Wortgleich mit der Poolaufgabe (Reserve-Stapel 2019-ga-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B3.2e", block="B", aufgabe="3.2", titel="Würfel", teilaufgabe="e", seite="31", punkte="3",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer parallelen Ebene durch einen Punkt aufstellen",
    typ_neben="Punkt und Ebene: Punktprobe an einer Ebenengleichung durchführen",
    stichwoerter="T: 5x + 4y + 5z = d mit K: d = 30|L: 5 + 0 + 25 = 30|L liegt in T",
    voraussetzungen="parallele Ebenen haben gleichen Normalenvektor|Punktprobe",
    format="Rechnung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben=WU + "; Ebene S: 5x + 4y + 5z = 0; K liegt in einer zu S parallelen Ebene T",
    gesucht="ob auch L in T liegt",
    verfahren="T mit dem Normalenvektor von S durch K aufstellen (d = 30), L einsetzen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="T: 5x + 4y + 5z = 30; L(1 | 0 | 5) erfüllt 5 + 25 = 30, also liegt L in T",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="L in S statt in T einsetzen",
    bemerkung="Poolaufgabe (nicht erfasst): 2019MgrundlegendBAGLAA2WTR1-1e. Wortgleich mit der Poolaufgabe (Reserve-Stapel 2019-ga-B; der Pool schreibt x₁, x₂, x₃). Typen aus dem Bestand (2024-ga-B, 2026-ga-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B3.2f", block="B", aufgabe="3.2", titel="Würfel", teilaufgabe="f", seite="31", punkte="5",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen", typ_neben="",
    stichwoerter="g: x = (4 − r | 0 | r² + 1) + u · (4 | −5 | 0)|Kante GH: x = (5 | 5 | 5) + w · (−5 | 0 | 0), 0 ≤ w ≤ 1|u = −1, r = ±2, w = 3/5 oder 7/5|r = −2, Schnittpunkt teilt GH im Verhältnis 3 : 2",
    voraussetzungen="Gleichsetzen zweier Geraden|LGS mit drei Unbekannten|Parameterbereich einer Kante",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=WU_SK, kontext="ohne", textumfang="mittel",
    gegeben=WU + "; Gerade g: x = (4 − r | 0 | r² + 1) + u · (4 | −5 | 0), u ∈ IR, schneidet für einen Wert von r die Kante GH",
    gesucht="Verhältnis, in dem der Schnittpunkt die Kante GH teilt",
    verfahren="g mit der Geraden GH gleichsetzen: aus y folgt u = −1, aus z folgt r² + 1 = 5, aus x folgt w; nur w ∈ [0; 1] (r = −2, w = 3/5) liegt auf der Kante",
    schritte="5", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="r = −2, Schnittpunkt S(2 | 5 | 5) mit w = 3/5; S teilt GH im Verhältnis 3 : 2 (|GS| : |SH| = 3 : 2)",
    zwischenergebnis="u = −1|r² = 4|w = 3/5 bzw. 7/5", niveau_geschaetzt="II",
    fehlerquelle="r = 2 mit w = 7/5 nicht ausschließen (Punkt außerhalb der Kante)",
    bemerkung="Poolaufgabe (nicht erfasst): 2019MgrundlegendBAGLAA2WTR1-1f. Wortgleich mit der Poolaufgabe (Reserve-Stapel 2019-ga-B). Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 4.1 Führerschein (Seiten 37–38), 20 BE – a, b Landesfassung, c–e Pool Stochastik WTR 1 (Reserve): Vormerkungen
FS = "In einem Land besitzen 80 % der Erwachsenen einen Führerschein; 100 Erwachsene werden zufällig ausgewählt, die Anzahl X der Führerscheinbesitzer darunter gilt als binomialverteilt"
FS2 = "Fahrprüfungen einer Region: 13 879 Prüflinge, davon 2 482 mindestens 30 Jahre alt; 11 104 haben bestanden, davon 8 870 jünger als 30; Ereignisse A: mindestens 30 Jahre alt, B: Prüfung bestanden"
row(id="2019-be-gk-B4.1a", block="B", aufgabe="4.1", titel="Führerschein", teilaufgabe="a", seite="37|38", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", typ_neben="",
    stichwoerter="n = 100, p = 0,8|P(X = 80) = (100 über 80) · 0,8⁸⁰ · 0,2²⁰ ≈ 0,099|P(X ≤ 75) = 1 − 0,8686 = 0,1314 aus der Tabelle (p = 0,2, von unten gelesen)",
    voraussetzungen="Bernoulli-Formel|Tabelle summierter Binomialverteilungen lesen (Anlage)",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle", skizze="Anlage Seite 38: Tabelle der summierten Binomialverteilung für n = 100 (p = 0,02 bis 0,5), vier Nachkommastellen", kontext="Führerschein", textumfang="mittel",
    gegeben=FS + "; Tabelle der summierten Binomialverteilung n = 100 in der Anlage",
    gesucht="P(E1): genau 80 Führerscheinbesitzer; P(E2): höchstens 75 Führerscheinbesitzer",
    verfahren="E1 mit der Bernoulli-Formel; E2 aus der Tabelle über das Gegenereignis (Anzahl ohne Führerschein ≥ 25 bei p = 0,2)",
    schritte="3", zahlenraum="dezimal|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="P(E1) = P(X = 80) ≈ 0,099 (9,9 %); P(E2) = P(X ≤ 75) ≈ 0,131 (13,1 %)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="die Tabelle für p = 0,8 nicht „von unten“ lesen (1 − Tabellenwert)",
    bemerkung="Landesfassung: der Pool (Stochastik WTR 1 a, 200 Erwachsene, Abweichung vom Erwartungswert um höchstens 5 %) stellt eine andere Frage mit demselben Aufgabenstamm; keine Dublette. Eigene Rechnung, mit sympy bestätigt (0,0993; 0,1313).")
row(id="2019-be-gk-B4.1b", block="B", aufgabe="4.1", titel="Führerschein", teilaufgabe="b", seite="37", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen", typ_neben="",
    stichwoerter="1 − 0,8ⁿ ≥ 0,99|0,8ⁿ ≤ 0,01|n ≥ ln 0,01 / ln 0,8 ≈ 20,6, also n = 21",
    voraussetzungen="Gegenereignis „alle haben einen Führerschein“|Logarithmieren mit Umkehr des Relationszeichens",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Führerschein", textumfang="kurz",
    gegeben="80 % der Erwachsenen besitzen einen Führerschein; n Erwachsene werden zufällig ausgewählt",
    gesucht="kleinstes n, sodass mit mindestens 99 % Wahrscheinlichkeit mindestens eine Person ohne Führerschein darunter ist",
    verfahren="Gegenereignis: alle n mit Führerschein, 0,8ⁿ ≤ 0,01, logarithmieren",
    schritte="3", zahlenraum="dezimal|Prozent|Potenz", einheiten="", abhaengig_von="",
    ergebnis="n ≥ 20,6, also mindestens 21 Erwachsene",
    zwischenergebnis="0,8ⁿ ≤ 0,01", niveau_geschaetzt="II",
    fehlerquelle="beim Teilen durch ln 0,8 < 0 das Relationszeichen nicht umkehren",
    bemerkung="Landesfassung (der Pool fragt in b nach mehr als 160 Führerscheinbesitzern mit 90 %; andere Frage). Typ wiederverwendet (2017-bb-ea 4.2 b). Eigene Rechnung, mit sympy bestätigt (20,64).")
row(id="2019-be-gk-B4.1c", block="B", aufgabe="4.1", titel="Führerschein", teilaufgabe="c", seite="37", punkte="2",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen", typ_neben="",
    stichwoerter="13 879 − 2 482 − 8 870 = 2 527|jünger als 30 und nicht bestanden",
    voraussetzungen="Vierfeldertafel mit absoluten Zahlen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Fahrprüfung", textumfang="mittel",
    gegeben=FS2,
    gesucht="Anzahl der Prüflinge, die jünger als 30 waren und nicht bestanden haben",
    verfahren="Gesamtzahl minus mindestens 30-Jährige minus jüngere Bestandene",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="2 527 Prüflinge",
    zwischenergebnis="jünger als 30: 11 397", niveau_geschaetzt="I",
    fehlerquelle="11 104 − 8 870 = 2 234 (Bestandene ab 30) als Antwort nehmen",
    bemerkung="Poolaufgabe (nicht erfasst): 2019MgrundlegendBStochastikWTR1-1c. Wortgleich mit der Poolaufgabe 2019 grundlegend Stochastik WTR 1 c (Reserve-Stapel 2019-ga-B). Eigene Rechnung.")
row(id="2019-be-gk-B4.1d", block="B", aufgabe="4.1", titel="Führerschein", teilaufgabe="d", seite="37", punkte="5",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten", typ_neben="",
    stichwoerter="P_A(B) = (11 104 − 8 870) / 2 482 = 2 234 / 2 482 ≈ 0,900|P(B) = 11 104 / 13 879 ≈ 0,800|ungleich, also abhängig|Ältere bestehen häufiger",
    voraussetzungen="bedingte Wahrscheinlichkeit aus absoluten Zahlen|Definition der Unabhängigkeit",
    format="Rechnung|Begründung", operator="Untersuchen Sie|Geben Sie an|Interpretieren Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Fahrprüfung", textumfang="mittel",
    gegeben=FS2,
    gesucht="ob P_A(B) und P(B) übereinstimmen; ob A und B stochastisch unabhängig sind; Deutung im Sachzusammenhang",
    verfahren="Beide Wahrscheinlichkeiten als Quotienten berechnen und vergleichen",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P_A(B) ≈ 90,0 % ≠ P(B) ≈ 80,0 %: A und B sind nicht unabhängig; Prüflinge ab 30 Jahren bestehen häufiger als der Durchschnitt",
    zwischenergebnis="Bestandene ab 30: 2 234", niveau_geschaetzt="II",
    fehlerquelle="P_A(B) mit P(A ∩ B) verwechseln",
    bemerkung="Poolaufgabe (nicht erfasst): 2019MgrundlegendBStochastikWTR1-1d. Wortgleich mit der Poolaufgabe (Reserve-Stapel 2019-ga-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B4.1e", block="B", aufgabe="4.1", titel="Führerschein", teilaufgabe="e", seite="37", punkte="5",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Anteil aus einer quadratischen Gleichung für ein zweistufiges Bestehen berechnen", typ_neben="",
    stichwoerter="q + (1 − q) · q/2 = 0,9|q² − 3q + 1,8 = 0|q ≈ 0,829 (2,17 entfällt)",
    voraussetzungen="Pfadregel über zwei Versuche|p-q-Formel|Lösung als Anteil auswählen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Fahrprüfung", textumfang="mittel",
    gegeben="Anteil q der Prüflinge, die beim ersten Mal bestehen; wer nicht besteht, nimmt ein zweites Mal teil und besteht dann mit dem halben Anteil q/2; insgesamt bestehen 90 % spätestens beim zweiten Mal",
    gesucht="Wert von q",
    verfahren="Gleichung q + (1 − q) · q/2 = 0,9 aufstellen und als quadratische Gleichung lösen",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="q = (3 − √1,8) / 2 ≈ 0,829 (82,9 %); die zweite Lösung ≈ 2,17 ist kein Anteil",
    zwischenergebnis="q² − 3q + 1,8 = 0", niveau_geschaetzt="III",
    fehlerquelle="den Anteil im zweiten Versuch auf alle Prüflinge statt auf die Durchgefallenen beziehen",
    bemerkung="Poolaufgabe (nicht erfasst): 2019MgrundlegendBStochastikWTR1-1e. Wortgleich mit der Poolaufgabe (Reserve-Stapel 2019-ga-B). Enge Fassung: Modell aus dem Text selbst aufstellen, quadratische Gleichung – III. Eigene Rechnung, mit sympy bestätigt (0,8292).")
# ---- Aufgabe 4.2 Würfelspiel (Seite 42), 20 BE, Landesaufgabe
WS = "Sven und Tom würfeln täglich mit einem fairen Würfel: zuerst Sven, dann Tom; ist Svens Augenzahl kleiner als Toms, bringt Sven den Müll hinunter, sonst Tom"
row(id="2019-be-gk-B4.2a", block="B", aufgabe="4.2", titel="Würfelspiel", teilaufgabe="a", seite="42", punkte="2",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen", typ_neben="",
    stichwoerter="Sven 4: 1/6|Tom 5 oder 6: 2/6|1/6 · 1/3 = 1/18",
    voraussetzungen="Pfadregel|Summenregel",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Foto", skizze="Zeichnung eines Würfels ohne Werte", kontext="Würfelspiel / Haushalt", textumfang="mittel",
    gegeben=WS,
    gesucht="Wahrscheinlichkeit, dass Sven eine 4 gewürfelt hat und den Müll hinunterbringen muss",
    verfahren="P(4) · P(Tom 5 oder 6)",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="1/6 · 2/6 = 1/18",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Toms Wurf ≥ 4 statt > 4 zählen",
    bemerkung="Landesaufgabe (nicht im Pool 2019). Typ wiederverwendet (2024-ga-A). Eigene Rechnung.")
row(id="2019-be-gk-B4.2b", block="B", aufgabe="4.2", titel="Würfelspiel", teilaufgabe="b", seite="42", punkte="5",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Wahrscheinlichkeit eines Vergleichsereignisses beim Wurf zweier Würfel über die Ergebnistabelle nachweisen", typ_neben="",
    stichwoerter="15 Ergebnisse mit Sven < Tom von 36|p = 15/36 = 5/12|Tabelle Sven 1: Tom 2–6 (5), Sven 2: 4, 3: 3, 4: 2, 5: 1",
    voraussetzungen="Laplace-Wahrscheinlichkeit|systematisches Abzählen",
    format="Begründung|Tabelle", operator="Zeigen Sie|Fertigen Sie an", antwort="Text|Tabelle",
    material="keins", skizze="keine", kontext="Würfelspiel / Haushalt", textumfang="mittel",
    gegeben=WS,
    gesucht="Nachweis, dass P(Sven bringt den Müll hinunter) = 5/12; tabellarische Übersicht aller Ergebnisse, bei denen Sven muss",
    verfahren="Alle Paare (Sven, Tom) mit Sven < Tom auflisten: 5 + 4 + 3 + 2 + 1 = 15 von 36",
    schritte="2", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="15 günstige von 36 gleich wahrscheinlichen Ergebnissen: p = 15/36 = 5/12; Tabelle der 15 Paare (1,2) … (1,6), (2,3) … (2,6), (3,4), (3,5), (3,6), (4,5), (4,6), (5,6)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="gleiche Augenzahlen mitzählen (dann 21/36)",
    bemerkung="Landesaufgabe. Eigene Rechnung.")
row(id="2019-be-gk-B4.2c", block="B", aufgabe="4.2", titel="Würfelspiel", teilaufgabe="c", seite="42", punkte="2",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="X binomialverteilt mit n = 30, p = 5/12|E(X) = 30 · 5/12 = 12,5",
    voraussetzungen="Erwartungswert n · p der Binomialverteilung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Würfelspiel / Haushalt", textumfang="kurz",
    gegeben=WS + "; im nächsten Monat wird 30-mal gewürfelt, p = 5/12 für Sven (aus b)",
    gesucht="Erwartungswert dafür, wie oft Sven im nächsten Monat den Müll hinunterbringt",
    verfahren="E(X) = n · p",
    schritte="1", zahlenraum="Bruch|dezimal", einheiten="", abhaengig_von="2019-be-gk-B4.2b",
    ergebnis="E(X) = 30 · 5/12 = 12,5",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="mit 1/2 statt 5/12 rechnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-bb-ea). Eigene Rechnung.")
row(id="2019-be-gk-B4.2d", block="B", aufgabe="4.2", titel="Würfelspiel", teilaufgabe="d", seite="42", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen",
    typ_neben="Wahrscheinlichkeit für wenigstens einen Treffer über das Gegenereignis berechnen",
    stichwoerter="P(X = 12) = (30 über 12) · (5/12)¹² · (7/12)¹⁸ ≈ 0,145|B: Tom mindestens einmal ⇔ nicht Sven 30-mal|P(B) = 1 − (5/12)³⁰",
    voraussetzungen="Bernoulli-Formel|Gegenereignis",
    format="Rechnung|Kurzantwort", operator="Berechnen Sie|Geben Sie an", antwort="Zahl|Term",
    material="keins", skizze="keine", kontext="Würfelspiel / Haushalt", textumfang="mittel",
    gegeben=WS + "; X = Anzahl der Tage von 30, an denen Sven muss, binomialverteilt mit p = 5/12",
    gesucht="P(A): Sven genau 12-mal; Term für P(B): Tom mindestens einmal",
    verfahren="Bernoulli-Formel für A; B über das Gegenereignis „Sven an allen 30 Tagen“",
    schritte="3", zahlenraum="Bruch|Potenz|dezimal", einheiten="", abhaengig_von="2019-be-gk-B4.2b",
    ergebnis="P(A) ≈ 0,145 (14,5 %); P(B) = 1 − (5/12)³⁰ (≈ 1)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="für B das Ereignis „Tom genau einmal“ ansetzen",
    bemerkung="Landesaufgabe. Nebentyp wiederverwendet (2018-be-gk 3.1 c). Eigene Rechnung, mit sympy bestätigt (0,1449).")
row(id="2019-be-gk-B4.2e", block="B", aufgabe="4.2", titel="Würfelspiel", teilaufgabe="e", seite="42", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren", typ_neben="",
    stichwoerter="Summe der Bernoulli-Terme für k = 10, 11, 12|P(10 ≤ X ≤ 12)|Sven mindestens 10-mal und höchstens 12-mal in 30 Tagen",
    voraussetzungen="Bernoulli-Term lesen",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Würfelspiel / Haushalt", textumfang="kurz",
    gegeben="Term (30 über 10) · (5/12)¹⁰ · (7/12)²⁰ + (30 über 11) · (5/12)¹¹ · (7/12)¹⁹ + (30 über 12) · (5/12)¹² · (7/12)¹⁸ im Spiel aus dem Stamm (30 Tage, p = 5/12)",
    gesucht="Bedeutung des Terms im Sachzusammenhang",
    verfahren="Jeden Summanden als P(X = k) lesen und die Summe als Intervallwahrscheinlichkeit deuten",
    schritte="1", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="P(10 ≤ X ≤ 12): Wahrscheinlichkeit, dass Sven in den 30 Tagen mindestens 10-mal und höchstens 12-mal den Müll hinunterbringt (≈ 0,372)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="die Summe als „genau 10 oder 12“ statt als Intervall deuten",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2026-ga-B). Term am Bild geprüft (Textextraktion verliert die Binomialkoeffizienten). Eigene Rechnung, mit sympy bestätigt.")
row(id="2019-be-gk-B4.2f", block="B", aufgabe="4.2", titel="Würfelspiel", teilaufgabe="f", seite="42", punkte="5",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit für höchstens k einer Sorte über Binomialkoeffizienten berechnen", typ_neben="",
    stichwoerter="5 schwarze, 5 weiße Kugeln, 7 mit einem Griff|schwarz = Toms Tage|höchstens 3 schwarze: 2 oder 3 schwarze (mindestens 2, weil nur 5 weiße)|[(5 über 2)(5 über 5) + (5 über 3)(5 über 4)] / (10 über 7) = 60/120 = 1/2",
    voraussetzungen="Ziehen ohne Zurücklegen mit Binomialkoeffizienten (Lotto-Modell)|Fallunterscheidung über die möglichen Anzahlen",
    format="Rechnung|Begründung", operator="Bestimmen Sie|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Würfelspiel / Haushalt", textumfang="lang",
    gegeben="Neues Verfahren: 5 schwarze und 5 weiße Kugeln, 7 werden mit einem Griff gezogen; die Anzahl der schwarzen Kugeln ist die Anzahl der Tage, an denen Tom in der Woche muss",
    gesucht="Wahrscheinlichkeit, dass Tom in der folgenden Woche weniger als 4-mal an der Reihe ist, mit Begründung des Ansatzes",
    verfahren="Ziehen ohne Zurücklegen: günstige Fälle 2 oder 3 schwarze Kugeln (weniger als 2 schwarze ist bei 7 gezogenen unmöglich), Binomialkoeffizienten durch (10 über 7)",
    schritte="4", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="P(Y ≤ 3) = (10 + 50) / 120 = 1/2",
    zwischenergebnis="(10 über 7) = 120", niveau_geschaetzt="II",
    fehlerquelle="binomial mit p = 1/2 rechnen (Ziehen mit Zurücklegen) oder die Fälle 0 und 1 schwarze mitzählen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2023-bebb-gk 4.1 h). Eigene Rechnung, mit sympy bestätigt.")
# ---- Dubletten aus dem Pool (dubletten.py, map_2019gk.py)
row(id="2019-be-gk-A1.2a", block="A", aufgabe="1.2", titel="Analysis 2", teilaufgabe="a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Schnittstellen zweier Graphen durch Lösen einer quadratischen Gleichung nachweisen",
    typ_neben="",
    stichwoerter="g(x) = h(x) ⇔ 2x² − 2x − 4 = 0 ⇔ x² − x − 2 = 0|höchstens zwei Lösungen|x = −1 und x = 2 durch Einsetzen bestätigen",
    voraussetzungen="Gleichsetzen|quadratische Gleichung hat höchstens zwei Lösungen",
    format="Begründung",
    operator="Zeigen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="g(x) = x² − 3 und h(x) = −x² + 2x + 1 in IR",
    gesucht="Nachweis, dass sich die Graphen nur für x = −1 und x = 2 schneiden",
    verfahren="quadratische Gleichung g(x) = h(x) lösen oder beide Werte einsetzen und Lösungszahl begründen",
    schritte="2",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="g(x) = h(x) hat als quadratische Gleichung höchstens zwei Lösungen; g(−1) = −2 = h(−1), g(2) = 1 = h(2)",
    zwischenergebnis="2x² − 2x − 4 = 0",
    niveau_geschaetzt="I",
    fehlerquelle="das „nur“ nicht begründen (Lösungszahl einer quadratischen Gleichung)",
    abhaengig_von="",
    bemerkung="Dublette von: 2019MgrundlegendAAnalysis11-a. Wortgleich mit der Poolaufgabe 2019 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.1 a; im Heft die zweite Analysis-Einheit des hilfsmittelfreien Teils. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2019-be-gk-A1.2b", block="A", aufgabe="1.2", titel="Analysis 2", teilaufgabe="b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    typ_neben="",
    stichwoerter="h über g auf [−1; 2]|Integral von −1 bis 2 über (h(x) − g(x)) dx = Integral über (−2x² + 2x + 4) dx|[−2/3 x³ + x² + 4x] von −1 bis 2 = 9",
    voraussetzungen="Schnittstellen aus a als Grenzen|Differenzfunktion|Stammfunktion",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="g(x) = x² − 3, h(x) = −x² + 2x + 1; Schnittstellen −1 und 2",
    gesucht="Inhalt der von beiden Graphen eingeschlossenen Fläche",
    verfahren="Integral der Differenz zwischen den Schnittstellen",
    schritte="3",
    zahlenraum="ganz|Bruch|negativ",
    einheiten="",
    ergebnis="Integral von −1 bis 2 über (h(x) − g(x)) dx = Integral von −1 bis 2 über (−2x² + 2x + 4) dx = [−2/3 x³ + x² + 4x] von −1 bis 2 = −16/3 + 4 + 8 − 2/3 − 1 + 4 = 9",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Vorzeichen beim Einsetzen der unteren Grenze −1",
    abhaengig_von="2019-be-gk-A1.2a",
    bemerkung="Dublette von: 2019MgrundlegendAAnalysis11-b. Wortgleich mit der Poolaufgabe 2019 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.1 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2019-be-gk-A1.4a", block="A", aufgabe="1.4", titel="Stochastik", teilaufgabe="a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben",
    typ_neben="",
    stichwoerter="20 andere Mitglieder, 11 Frauen|11/20",
    voraussetzungen="Leiterin herausrechnen|günstige durch mögliche",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Chor/Preisverleihung",
    textumfang="mittel",
    gegeben="Chor aus 12 Frauen und 9 Männern, eine Frau leitet; die Leiterin nimmt teil, das zweite Mitglied wird zufällig aus den übrigen gewählt",
    gesucht="Wahrscheinlichkeit, dass das zweite Mitglied eine Frau ist",
    verfahren="Anteil der Frauen unter den 20 übrigen",
    schritte="1",
    zahlenraum="Bruch",
    einheiten="",
    ergebnis="11/20",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="12/21 (Leiterin nicht abziehen)",
    abhaengig_von="",
    bemerkung="Dublette von: 2019MgrundlegendAStochastik11-a. Wortgleich mit der Poolaufgabe 2019 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 1.1 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2019-be-gk-A1.4b", block="A", aufgabe="1.4", titel="Stochastik", teilaufgabe="b", seite="2", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen",
    typ_neben="",
    stichwoerter="11 Frauen, 9 Männer unter den anderen Mitgliedern|mehr Frauenpaare als Männerpaare",
    voraussetzungen="Vergleich der Anzahlen ohne Rechnung",
    format="Begründung",
    operator="Begründen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Chor/Preisverleihung",
    textumfang="mittel",
    gegeben="die Leiterin kann nicht teilnehmen; zwei der anderen 20 Mitglieder (11 Frauen, 9 Männer) werden zufällig ausgewählt",
    gesucht="Begründung ohne Rechnung, dass P(zwei Frauen) > P(zwei Männer)",
    verfahren="Anzahl der Frauen mit der der Männer vergleichen",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="die Anzahl der Frauen unter den anderen Mitgliedern ist größer als die der Männer",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="doch rechnen (55/190 gegen 36/190) statt zu begründen",
    abhaengig_von="",
    bemerkung="Dublette von: 2019MgrundlegendAStochastik11-b. Wortgleich mit der Poolaufgabe 2019 grundlegend (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 1.1 b; Teilaufgabe c ist im Heft abgewandelt (Term statt Wert). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")

NEUE_TYPEN = [
    ("Ableitungsfunktion und Stammfunktion einer ganzrationalen Funktion angeben", "Analysis", "Ableitungsregeln",
     "Zu einem ganzrationalen Term die Ableitungsfunktion mit der Potenzregel und eine Stammfunktion angeben, ohne weitere Auswertung.",
     "2019-be-gk-A1.1a"),
    ("Extremstelle über den Vorzeichenwechsel der Ableitung in ein Intervall einschließen", "Analysis", "Kurvenuntersuchung",
     "Ein Intervall vorgegebener Länge angeben, in dem eine Extremstelle liegen muss, und es über die Vorzeichen der Ableitung an den Intervallenden (Vorzeichenwechsel) begründen, ohne die Stelle zu berechnen.",
     "2019-be-gk-A1.1b"),
    ("Echt parallele und senkrecht schneidende Gerade zu einer gegebenen Geraden angeben", "Analytische Geometrie", "Geraden",
     "Zu einer Geraden in Parameterform eine echt parallele Gerade (gleicher Richtungsvektor, Stützpunkt außerhalb) und eine sie senkrecht schneidende Gerade (Richtungsvektor mit Skalarprodukt null, gemeinsamer Punkt) angeben.",
     "2019-be-gk-A1.3a"),
    ("Schnitt einer senkrecht schneidenden Geraden mit einer parallelen Geraden beurteilen", "Analytische Geometrie", "Geraden",
     "Entscheiden und begründen, ob jede Gerade, die eine Gerade g senkrecht schneidet, auch eine zu g parallele Gerade schneidet – nein, weil sie windschief zur Parallelen liegen kann.",
     "2019-be-gk-A1.3b"),
    ("Maximum einer ganzrationalen Funktion im Sachzusammenhang über die Ableitung berechnen", "Analysis", "Kurvenuntersuchung",
     "Den größten Wert einer ganzrationalen Modellfunktion (etwa eine maximale Höhe) über die Nullstellen der Ableitung mit Prüfung der hinreichenden Bedingung berechnen und die zugehörige Stelle im Sachzusammenhang deuten.",
     "2019-be-gk-B2.1a"),
    ("Größte Änderungsrate über das Maximum der Ableitung im Sachzusammenhang berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Die größte momentane Änderungsrate (etwa eine höchste Wachstumsgeschwindigkeit) als Maximum der Ableitungsfunktion über die Nullstelle der zweiten Ableitung berechnen; Gegenstück zur kleinsten Tangentensteigung.",
     "2019-be-gk-B2.1b"),
    ("Zeitpunkte gleicher Änderungsrate zweier Modelle über die Gleichung der Ableitungen berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Die Ableitungen zweier Modellfunktionen gleichsetzen und die Lösungen der Gleichung als Zeitpunkte gleicher Änderungsrate im Sachzusammenhang angeben.",
     "2019-be-gk-B2.1d"),
    ("Zeitpunkte größter Differenz zweier Änderungsraten über die Extremstellen der Differenzfunktion berechnen", "Analysis", "Ableitung und Änderungsrate",
     "Die Differenz der Ableitungen zweier Modellfunktionen bilden und ihre Extremstellen über die notwendige Bedingung als Zeitpunkte größter Abweichung der Änderungsraten bestimmen.",
     "2019-be-gk-B2.1e"),
    ("Integral der Differenz zweier Änderungsraten berechnen und als Bestandsdifferenz deuten", "Analysis", "Rekonstruktion von Beständen",
     "Das Integral über die Differenz zweier Ableitungsfunktionen in einem Intervall berechnen und als Unterschied der Bestände (etwa Höhenunterschied) am Intervallende deuten, wenn beide Bestände am Anfang gleich sind.",
     "2019-be-gk-B2.1g"),
    ("Stelle zu einem vorgegebenen Wert einer linearen Funktion über eine Ungleichung berechnen", "Analysis", "Gleichungen lösen",
     "Für eine lineare Funktion (etwa eine Tangente) die Stellen berechnen, ab denen ein vorgegebener Wert unterschritten oder überschritten wird, über eine lineare Ungleichung.",
     "2019-be-gk-B2.2f"),
    ("Parameter einer Exponentialfunktion aus einer Ungleichung für einen Funktionswert im Sachzusammenhang ermitteln", "Analysis", "Gleichungen lösen",
     "Für eine Funktion mit multiplikativem Parameter k die Bedingung an einen Funktionswert (etwa Mindestwert zu einem Zeitpunkt) als Ungleichung in k aufstellen und den kleinsten zulässigen Wert von k berechnen.",
     "2019-be-gk-B2.2g"),
    ("Einfluss eines multiplikativen Parameters auf den Graphen im Vergleich mit dem Ausgangsgraphen beschreiben", "Analysis", "Funktionsscharen und Ortskurven",
     "Den Graphen einer Funktion mit einem Parameter im Vorfaktor eines Summanden mit dem Ausgangsgraphen vergleichen und Gemeinsamkeiten und Unterschiede (Startwert, Grenzwert, Lage, Maximum, Extremstelle) angeben.",
     "2019-be-gk-B2.2h"),
    ("Geradengleichung durch zwei Punkte aufstellen", "Analytische Geometrie", "Geraden",
     "Aus zwei gegebenen Punkten eine Parametergleichung der Geraden mit Stütz- und Richtungsvektor angeben.",
     "2019-be-gk-B3.1a"),
    ("Durchstoßpunkt einer achsenparallelen Geraden mit einer Ebene berechnen und Abstand im Sachzusammenhang angeben", "Analytische Geometrie", "Schnittmengen",
     "Eine zu einer Koordinatenachse parallele Gerade durch einen Punkt mit einer Ebene in Koordinatenform schneiden und aus der Koordinatendifferenz die Länge der Strecke bis zum Durchstoßpunkt mit Maßstab und Zuschlag angeben.",
     "2019-be-gk-B3.1b"),
    ("Parallelität zweier Geraden über die Richtungsvektoren prüfen", "Analytische Geometrie", "Geraden",
     "Die Richtungsvektoren zweier Geraden auf Kollinearität prüfen und daraus entscheiden, ob die Geraden parallel sind.",
     "2019-be-gk-B3.1c"),
    ("Punkt: Begegnungspunkt zweier gleichzeitig startender Bewegungen auf einer Strecke aus den Geschwindigkeiten berechnen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Für zwei Objekte, die gleichzeitig von den Enden einer Strecke bekannter Länge mit konstanten Geschwindigkeiten aufeinander zufahren, den bis zur Begegnung zurückgelegten Weg über die Gleichheit der Zeiten berechnen.",
     "2019-be-gk-B3.1d"),
    ("Ebene Figur: Trapez mit zwei gleich langen Seiten über Kollinearität und Seitenlängen nachweisen", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Für ein Viereck im Raum die Parallelität zweier Seiten über kollineare Verbindungsvektoren, die Gleichheit der beiden anderen Seitenlängen über Beträge und ein Längenverhältnis der parallelen Seiten aus dem Kollinearitätsfaktor nachweisen.",
     "2019-be-gk-B3.2b"),
    ("Innenwinkel eines Vierecks über das Skalarprodukt der Seitenvektoren berechnen", "Analytische Geometrie", "Skalarprodukt und Winkel",
     "Einen Innenwinkel eines Vierecks im Raum als Winkel zwischen den beiden vom Eckpunkt ausgehenden Seitenvektoren über das Skalarprodukt berechnen.",
     "2019-be-gk-B3.2c"),
    ("Ebene Figur: Flächeninhalt eines Trapezes im Raum über die Höhe zwischen den parallelen Seiten berechnen", "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Den Flächeninhalt eines Trapezes im Raum mit der Trapezformel berechnen; die Höhe als Abstand der Mittelpunkte der parallelen Seiten (symmetrisches Trapez) oder als Abstand einer Ecke von der Trägergeraden der Gegenseite.",
     "2019-be-gk-B3.2d"),
    ("Schnittpunkt einer parameterabhängigen Geraden mit einer Kante und Teilverhältnis bestimmen", "Analytische Geometrie", "Schnittmengen",
     "Eine Gerade, deren Stützvektor einen Parameter enthält, mit der Geraden durch eine Körperkante gleichsetzen, den Parameterwert mit Schnittpunkt auf der Kante über das lineare Gleichungssystem finden und das Teilverhältnis aus dem Kantenparameter angeben.",
     "2019-be-gk-B3.2f"),
    ("Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen", "Stochastik", "Binomialverteilung",
     "Einzelwahrscheinlichkeit P(X = k) mit der Bernoulli-Formel und kumulierte Wahrscheinlichkeit P(X ≤ k) aus der Tabelle der summierten Binomialverteilung (ohne Rechnerfunktion) bestimmen.",
     "2019-be-gk-B4.1a"),
    ("Fehlende absolute Häufigkeit über die Vierfeldertafel berechnen", "Stochastik", "Vierfeldertafel",
     "Aus Gesamtzahl, Randsummen und einem Feld einer Vierfeldertafel mit absoluten Häufigkeiten ein fehlendes Feld durch Subtraktion berechnen.",
     "2019-be-gk-B4.1c"),
    ("Unabhängigkeit über den Vergleich von bedingter und unbedingter Wahrscheinlichkeit untersuchen und deuten", "Stochastik", "Unabhängigkeit",
     "Eine bedingte Wahrscheinlichkeit P_A(B) aus absoluten Häufigkeiten berechnen, mit P(B) vergleichen, daraus über stochastische Unabhängigkeit entscheiden und den Unterschied im Sachzusammenhang deuten.",
     "2019-be-gk-B4.1d"),
    ("Anteil aus einer quadratischen Gleichung für ein zweistufiges Bestehen berechnen", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Aus einer Sachbeschreibung mit unbekanntem Anteil q (erster Versuch) und abhängigem Anteil im zweiten Versuch die Gleichung für die Gesamtwahrscheinlichkeit aufstellen (q + (1 − q) · q/2 = Vorgabe) und die sinnvolle Lösung der quadratischen Gleichung bestimmen.",
     "2019-be-gk-B4.1e"),
    ("Laplace-Experiment: Wahrscheinlichkeit eines Vergleichsereignisses beim Wurf zweier Würfel über die Ergebnistabelle nachweisen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Für zwei nacheinander geworfene Würfel alle Ergebnisse auflisten, bei denen die erste Augenzahl kleiner (größer) als die zweite ist, und die Wahrscheinlichkeit als Anteil an den 36 gleich wahrscheinlichen Ergebnissen nachweisen.",
     "2019-be-gk-B4.2b"),
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
