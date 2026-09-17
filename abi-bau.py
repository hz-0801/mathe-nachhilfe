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
    "jahr": "2024",
    "papier": "2024-bebb-lk",
    "datei": "hefte/2024-bebb-lk.pdf",  # Stark-Band (Band zum Abitur 2027 LK, Jahrgang 2024), Bildscan der Aufgabenseiten, lokal (abi.md § 2)
    "seiten": 13,
    # Sollpunkte je Aufgabe aus der BE-Spalte; jede Aufgabe des Hefts muss hier
    # stehen (Vollständigkeit). Hilfsmittelfreier Teil: Pflichtaufgaben 1.1–1.4
    # (20 BE) und Wahlaufgaben 1.5–1.10 (30 BE angeboten, zwei zu bearbeiten:
    # Schlüssel 2024 LK 30 / 40 / 25 / 25); Teil B 2.1/2.2 Analysis je 40 zur
    # Wahl, 3 Geometrie 25, 4 Stochastik 25. Angeboten 180, bearbeitet 120.
    # 2.2 hat zwei Aufgabenteile, fortlaufend a–i (Aufgabenteil 2 a–d = f–i);
    # 4 hat drei Aufgabenteile, fortlaufend a–h (Teil 2 a–c = d–f, Teil 3 a–b = g–h).
    "soll": {"1.1": 5, "1.2": 5, "1.3": 5, "1.4": 5, "1.5": 5, "1.6": 5, "1.7": 5, "1.8": 5, "1.9": 5, "1.10": 5,
             "2.1": 40, "2.2": 40, "3": 25, "4": 25},
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
# Heft 2024-bebb-lk (Stark-Band zum Abitur 2027 LK, Jahrgang 2024; 13 Seiten
# Bildscan, nur Aufgabenseiten; Auftrag B, 17.09.2026). Pool 2024 erhöht (Teil A
# und B erfasst): 1.1, 1.2, 1.3, 1.5, 1.6, 1.7, 1.10 (Teil A), 2.2 c, d, f–i,
# 3 a–h, 4 a–h wortgleich – „Dublette von:“, aus den Poolzeilen erzeugt
# (dubletten.py); 3 c und 3 f mit vertauschten BE (Heft 4/3, Pool 3/4);
# 2.2 a, b, e abgewandelt (Schar mit einem Parameter, h mit b und c).
# Landesaufgaben: 1.4, 1.8, 1.9 (Teil A) und ganz 2.1 (Exponentialfunktionen).
# ---- Aufgabe 1: hilfsmittelfreier Teil, Landeseinheiten (Seiten 2, 4)
row(id="2024-bebb-lk-A1.4a", block="A", aufgabe="1.4", titel="Stochastik (1.4)", teilaufgabe="a", seite="2", punkte="2",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit für genau drei aufeinanderfolgende gleichfarbige Kugeln beim Ziehen ohne Zurücklegen berechnen", typ_neben="",
    stichwoerter="günstige Farbfolgen GGGR, RGGG, RRRG, GRRR|je 3/6 · 2/5 · 1/4 · 3/3 = 1/20|Summe 4 · 1/20 = 1/5",
    voraussetzungen="Pfadregeln beim Ziehen ohne Zurücklegen|Aufzählen günstiger Folgen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Urne mit 3 grünen und 3 roten, sonst nicht unterscheidbaren Kugeln; vier Kugeln werden nacheinander ohne Zurücklegen gezogen",
    gesucht="P(genau drei Kugeln gleicher Farbe folgen aufeinander)",
    verfahren="die vier günstigen Farbfolgen aufzählen, Pfadwahrscheinlichkeit je Folge, Summe",
    schritte="3", zahlenraum="Bruch", einheiten="", abhaengig_von="",
    ergebnis="4 · (3/6 · 2/5 · 1/4 · 3/3) = 4 · 1/20 = 1/5",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="nur zwei Folgen (GGGR, RRRG) zählen; vier gleiche Farben mitzählen (bei drei je Farbe unmöglich)",
    bemerkung="Landesaufgabe (nicht im Pool 2024 erhöht). Enge Fassung: günstige Folgen finden und Pfadregel – II. Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-A1.4b", block="A", aufgabe="1.4", titel="Stochastik (1.4)", teilaufgabe="b", seite="2", punkte="3",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Kugelzahl für eine begrenzte Anzahl von Farbreihenfolgen beim Ziehen ohne Zurücklegen begründen", typ_neben="",
    stichwoerter="ohne Einschränkung 2⁴ = 16 Farbfolgen|n = 3: GGGG und RRRR unmöglich, 14 Folgen|n = 2: nur Folgen mit je zwei Kugeln, 6 Folgen",
    voraussetzungen="Zählprinzip 2⁴|Vorrat begrenzt die Folgen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Urne mit n grünen und n roten Kugeln; vier Kugeln nacheinander ohne Zurücklegen; Aussage: es gibt einen Wert für n, so dass es weniger als 16 Möglichkeiten für die Reihenfolge der Farben gibt",
    gesucht="Begründung, dass die Aussage richtig ist",
    verfahren="16 Farbfolgen brauchen vier Kugeln je Farbe; für n = 3 (oder n = 2) fallen Folgen weg",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="richtig: für n = 3 sind GGGG und RRRR unmöglich, es bleiben 14 < 16 Reihenfolgen (für n = 2 nur 6 Reihenfolgen mit je zwei Kugeln jeder Farbe)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="n = 1 vorschlagen (nur zwei Kugeln, vier Ziehungen unmöglich); 2⁴ für jedes n ansetzen",
    bemerkung="Landesaufgabe. Enge Fassung: Zählprinzip mit Vorratsgrenze, ein Fall genügt – II. Eigene Rechnung (Aufzählung mit Python bestätigt: n = 2 → 6, n = 3 → 14, n ≥ 4 → 16).")
row(id="2024-bebb-lk-A1.8a", block="A", aufgabe="1.8", titel="Wahlaufgaben: Analytische Geometrie (1.8)", teilaufgabe="a", seite="4", punkte="5",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Lage einer Geradenschar zu einer Ebene mit Fallunterscheidung nach dem Parameter untersuchen", typ_neben="",
    stichwoerter="n = (−1; 0; 2), u = (−2; 2; −a): n · u = 2 − 2a|a = 1: Stützpunkt (5; −3; 1) erfüllt −5 + 2 = −3, g₁ liegt in E|a ≠ 1: Einsetzen liefert r = −1/2, S_a(3a + 3 | −4 | 1,5a)",
    voraussetzungen="Skalarprodukt Normalen- und Richtungsvektor|Punktprobe|Einsetzen der Geradengleichung mit Parameter",
    format="Rechnung", operator="Untersuchen Sie|Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="E: −x + 2z = −3; Geradenschar g_a: x = (3a + 2; −3; a) + r · (−2; 2; −a), r ∈ IR, a ∈ IR",
    gesucht="Lagebeziehung zwischen g_a und E in Abhängigkeit von a, gegebenenfalls Koordinaten des Schnittpunkts",
    verfahren="Skalarprodukt n · u auswerten; Fall a = 1 mit Punktprobe; sonst Geradenpunkt in die Ebenengleichung einsetzen",
    schritte="4", zahlenraum="ganz|negativ|Bruch", einheiten="", abhaengig_von="",
    ergebnis="n · u = 2 − 2a; für a = 1 liegt g₁ in E (kein echt paralleler Fall); für a ≠ 1 schneidet g_a die Ebene im Punkt S_a(3a + 3 | −4 | 1,5a) (r = −1/2)",
    zwischenergebnis="r = −1/2 unabhängig von a", niveau_geschaetzt="II",
    fehlerquelle="Fall a = 1 als „parallel“ ohne Punktprobe abschließen; Vorzeichenfehler beim Einsetzen des Parameters",
    bemerkung="Landesaufgabe (nicht im Pool 2024 erhöht). Enge Fassung: Standardverfahren mit Parameter und Fallunterscheidung – II. Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-A1.9a", block="A", aufgabe="1.9", titel="Wahlaufgaben: Stochastik (1.9)", teilaufgabe="a", seite="4", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit für genau einen Treffer bei zwei Versuchen berechnen", typ_neben="",
    stichwoerter="2 · 0,2 · 0,8 = 0,32",
    voraussetzungen="Pfadregeln|zwei Reihenfolgen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Geräteproduktion", textumfang="kurz",
    gegeben="Geräte einer großen Serie; ein zufällig ausgewähltes Gerät ist mit p = 0,2 defekt; zwei Geräte werden zufällig ausgewählt",
    gesucht="P(genau eines der beiden Geräte ist defekt)",
    verfahren="zwei Pfade (defekt–heil, heil–defekt) addieren",
    schritte="1", zahlenraum="dezimal", einheiten="", abhaengig_von="",
    ergebnis="2 · 0,2 · 0,8 = 0,32",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Faktor 2 für die Reihenfolge vergessen (0,16)",
    bemerkung="Landesaufgabe (nicht im Pool 2024 erhöht). Typ wiederverwendet (2026-ea-A). Eigene Rechnung.")
row(id="2024-bebb-lk-A1.9b", block="A", aufgabe="1.9", titel="Wahlaufgaben: Stochastik (1.9)", teilaufgabe="b", seite="4", punkte="3",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Wahrscheinlichkeit eines Fehlers aus der Vereinigung zweier unabhängiger Fehler berechnen", typ_neben="",
    stichwoerter="defekt = A ∪ B|P(A ∪ B) = 0,1 + p_B − 0,1 · p_B = 0,2|0,9 · p_B = 0,1, p_B = 1/9 ≈ 0,111|alternativ Gegenereignis: 0,9 · (1 − p_B) = 0,8",
    voraussetzungen="Additionssatz|Produktregel bei Unabhängigkeit|Gegenereignis",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Geräteproduktion", textumfang="kurz",
    gegeben="ein Gerät ist defekt, wenn Fehler A oder Fehler B auftritt; P(defekt) = 0,2; A und B stochastisch unabhängig; P(A) = 0,1, P(B) = p_B",
    gesucht="p_B",
    verfahren="P(A ∪ B) = P(A) + P(B) − P(A) · P(B) gleich 0,2 setzen und nach p_B auflösen",
    schritte="2", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="p_B = 1/9 ≈ 0,111",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="P(A) + P(B) = 0,2 ansetzen (Schnittmenge vergessen, p_B = 0,1)",
    bemerkung="Landesaufgabe. Enge Fassung: Vereinigung mit Unabhängigkeit in eine Gleichung übersetzen – II. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.1 Exponentialfunktionen (Seiten 5–6, 40 BE), Landesaufgabe
SK21 = "Koordinatensystem auf Millimeterpapier, x von −10 bis 16, y von −12 bis 6; Graph I (G_{0,4}): kommt von links knapp oberhalb der x-Achse, Nullstelle bei −5, fällt durch (0 | −5) zum Tiefpunkt bei etwa (0,8 | −5,4), steigt dann steil und schneidet die x-Achse bei 2,5; Graph II (G_{−0,2}): kommt von links unten steil (bei x = −2 etwa −11,6), läuft durch (0 | −5), Hochpunkt bei etwa (5 | −1,8), Tiefpunkt bei (10 | −2,0), nähert sich von unten der x-Achse; beide Graphen treffen sich in (0 | −5)"
row(id="2024-bebb-lk-B2.1a", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="a", seite="5", punkte="3",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Grenzverhalten einer Schar für x → +∞ nach dem Parametervorzeichen angeben", typ_neben="",
    stichwoerter="a > 0: e^(ax) → ∞ und ax² + x − 5 → ∞, f_a → +∞|a < 0: e^(ax) → 0 dominiert das Polynom, f_a → 0|a = 0: f_0(x) = x − 5 → +∞",
    voraussetzungen="Grenzverhalten von e^(ax)|e-Funktion dominiert Polynom",
    format="Kurzantwort", operator="Geben Sie an", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = (ax² + x − 5) · e^(ax), a ∈ IR, definiert in IR; Graphen G_a",
    gesucht="Verhalten der Funktionswerte für x → +∞ in Abhängigkeit von a",
    verfahren="Fallunterscheidung nach dem Vorzeichen von a, Sonderfall a = 0",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="a > 0 und a = 0: f_a(x) → +∞; a < 0: f_a(x) → 0",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Fall a = 0 vergessen; für a < 0 −∞ angeben (Polynom statt e-Term dominieren lassen)",
    bemerkung="Landesaufgabe (nicht im Pool 2024 erhöht). Eigene Rechnung, mit sympy bestätigt (Grenzwerte für a = 0,4, −0,2, 0).")
row(id="2024-bebb-lk-B2.1b", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="b", seite="5", punkte="5",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Anzahl der Nullstellen einer Schar in Abhängigkeit vom Parameter über die Diskriminante ermitteln", typ_neben="",
    stichwoerter="e^(ax) > 0: Nullstellen von ax² + x − 5|a = 0: eine Nullstelle x = 5|a ≠ 0: Diskriminante 1 + 20a|a > −1/20: zwei; a = −1/20: eine (x = 10); a < −1/20: keine",
    voraussetzungen="Produkt null, e-Term nie null|Diskriminante einer quadratischen Gleichung|Sonderfall linearer Term",
    format="Rechnung", operator="Ermitteln Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a wie in a",
    gesucht="Anzahl der Nullstellen von f_a in Abhängigkeit von a",
    verfahren="Nullstellen auf den quadratischen Faktor zurückführen, Diskriminante nach a auswerten",
    schritte="3", zahlenraum="ganz|Bruch|negativ", einheiten="", abhaengig_von="",
    ergebnis="a < −1/20: keine Nullstelle; a = −1/20: genau eine (x = 10); −1/20 < a < 0 und a > 0: zwei Nullstellen; a = 0: genau eine (x = 5)",
    zwischenergebnis="Diskriminante 1 + 20a", niveau_geschaetzt="II",
    fehlerquelle="Fall a = 0 in die Diskriminante einbeziehen (dort ist der Term linear); e^(ax) = 0 als Nullstelle ansetzen",
    bemerkung="Landesaufgabe. Enge Fassung: Standardverfahren Diskriminante mit Fallunterscheidung – II. Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-B2.1c", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="c", seite="5", punkte="3",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen", typ_neben="Gemeinsame Punkte aller Graphen einer Schar bestimmen",
    stichwoerter="Graph I strebt für x → +∞ gegen +∞: a = 0,4|Graph II nähert sich der x-Achse: a = −0,2|f_a(0) = −5 · e⁰ = −5 für alle a: Schnittpunkt (0 | −5)",
    voraussetzungen="Grenzverhalten aus a|Funktionswert an der Stelle 0",
    format="Begründung|Rechnung", operator="Ordnen Sie zu|Begründen Sie|Berechnen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SK21, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung mit den Graphen G_{−0,2} und G_{0,4} (Graphen I und II)",
    gesucht="Zuordnung der Parameter zu I und II mit Begründung; gemeinsamer Schnittpunkt aller G_a mit der y-Achse",
    verfahren="Grenzverhalten aus a (Teilaufgabe a) mit dem Bild vergleichen; f_a(0) berechnen",
    schritte="2", zahlenraum="ganz|negativ|dezimal", einheiten="", abhaengig_von="2024-bebb-lk-B2.1a",
    ergebnis="I: a = 0,4 (Graph strebt gegen +∞), II: a = −0,2 (Graph nähert sich der x-Achse); gemeinsamer Punkt (0 | −5)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="über die Steilheit statt über das Grenzverhalten zuordnen; Schnittpunkt aus dem Bild ablesen statt berechnen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2024-ea-A), Nebentyp (2026-ea-B). Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-B2.1d", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="d", seite="5", punkte="4",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen", typ_neben="Mögliche Extremstellen aus der faktorisierten Ableitung ohne Rechnung angeben",
    stichwoerter="Produktregel: (−0,4x + 1) · e^(−0,2x) + (−0,2x² + x − 5) · (−0,2) · e^(−0,2x)|= (0,04x² − 0,6x + 2) · e^(−0,2x) = 0,04(x − 5)(x − 10) · e^(−0,2x)|mögliche Extremstellen 5 und 10",
    voraussetzungen="Produkt- und Kettenregel|Ausklammern und Faktorisieren|notwendige Bedingung",
    format="Rechnung|Kurzantwort", operator="Zeigen Sie|Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_{−0,2}(x) = (−0,2x² + x − 5) · e^(−0,2x); Behauptung f'_{−0,2}(x) = 0,04(x − 5)(x − 10) · e^(−0,2x)",
    gesucht="Nachweis der Ableitung; mögliche lokale Extremstellen ohne weitere Rechnung",
    verfahren="Produktregel, e-Term ausklammern, quadratischen Faktor in Linearfaktoren zerlegen; Nullstellen der Ableitung ablesen",
    schritte="3", zahlenraum="dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="f'_{−0,2}(x) = (0,04x² − 0,6x + 2) · e^(−0,2x) = 0,04(x − 5)(x − 10) · e^(−0,2x); mögliche Extremstellen x = 5 und x = 10",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="innere Ableitung −0,2 vergessen; Extremstellen zusätzlich mit f'' prüfen (nicht verlangt)",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2021-ea-A). Eigene Rechnung, mit sympy bestätigt (Differenz null).")
row(id="2024-bebb-lk-B2.1e", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="e", seite="5", punkte="4",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Sekantengleichung durch zwei Punkte eines Graphen ermitteln", typ_neben="",
    stichwoerter="f_{−0,2}(5) = −5e^(−1) ≈ −1,839, f_{−0,2}(10) = −15e^(−2) ≈ −2,030|m = (−2,030 + 1,839)/5 ≈ −0,038|n = −1,839 − 5 · (−0,038) ≈ −1,65: S(0 | −1,65)",
    voraussetzungen="Funktionswerte mit e-Term|Zweipunkteform einer Geraden|y-Achsenabschnitt",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_{−0,2} wie in d; Gerade durch (5 | f_{−0,2}(5)) und (10 | f_{−0,2}(10)) schneidet die y-Achse in S; Kontrolle S(0 | −1,65)",
    gesucht="Koordinaten von S näherungsweise",
    verfahren="beide Funktionswerte berechnen, Steigung und y-Achsenabschnitt der Geraden",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="S(0 | −1,65) (genauer −1,6488)",
    zwischenergebnis="f_{−0,2}(5) ≈ −1,84, f_{−0,2}(10) ≈ −2,03, m ≈ −0,0381", niveau_geschaetzt="I",
    fehlerquelle="Rundung der Funktionswerte zu grob (Steigung ist klein)",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2018-be-gk). Eigene Rechnung, mit sympy bestätigt (−1,6488).")
row(id="2024-bebb-lk-B2.1f", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="f", seite="6", punkte="4",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Scharparameter für ein gleichseitiges Dreieck aus den Tangenten an Graph und Spiegelgraph und der y-Achse bestimmen", typ_neben="",
    stichwoerter="k_a = −f_a|f_a(0) = −5, f_a'(0) = 1 − 5a|Tangenten y = (1 − 5a)x − 5 und y = −(1 − 5a)x + 5, Schnitt bei x = 5/(1 − 5a)|Basis auf der y-Achse Länge 10, Höhe 5/|1 − 5a| = 5√3|a = 1/5 − √3/15 ≈ 0,085 oder a = 1/5 + √3/15 ≈ 0,315",
    voraussetzungen="Spiegelung an der x-Achse|Tangente an der Stelle 0 mit Parameter|gleichseitiges Dreieck über Höhe = Seite · √3/2",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Schar k_a durch Spiegelung der Graphen von f_a an der x-Achse; die Tangente an G_a an der Stelle 0, die Tangente an den Graphen von k_a an der Stelle 0 und die y-Achse begrenzen ein gleichseitiges Dreieck; es gibt zwei solche Werte von a",
    gesucht="ein Wert von a",
    verfahren="f_a'(0) = 1 − 5a, Tangenten spiegelbildlich zur x-Achse; Dreieck mit Basis 10 auf der y-Achse und Spitze bei x = 5/(1 − 5a); Höhe gleich 5√3 setzen",
    schritte="4", zahlenraum="Wurzel|Bruch|dezimal", einheiten="", abhaengig_von="",
    ergebnis="a = 1/5 − √3/15 ≈ 0,0845 (oder a = 1/5 + √3/15 ≈ 0,3155)",
    zwischenergebnis="f_a'(0) = 1 − 5a; Spitze des Dreiecks bei x = 5/(1 − 5a)", niveau_geschaetzt="III",
    fehlerquelle="Ableitung an der Stelle 0 ohne Produktregel (nur 1 statt 1 − 5a); Höhe mit der halben Basis verwechseln",
    bemerkung="Landesaufgabe. Enge Fassung: geometrische Bedingung (gleichseitig, Symmetrie der Tangenten) erst in eine Gleichung für a übersetzen – III. Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-B2.1g", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="g", seite="6", punkte="5",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Rechenweg zur Tangente von einem Punkt an den Graphen erläutern und Aufgabenstellung formulieren", typ_neben="",
    stichwoerter="t(x) = mx − 1,65: Gerade durch S(0 | −1,65) aus e|m = h'_{−0,2}(x_Q): t ist Tangente an den Graphen von h_{−0,2} im Punkt Q|h_{−0,2}(x_Q) = t(x_Q): Q liegt auf Gerade und Graph|Lösung x_Q ≈ −1,503, Q(−1,5 | 2,38)|Aufgabe: Berührpunkt der Tangente von S an den Graphen von h_{−0,2} bestimmen",
    voraussetzungen="Tangentenbedingung (Steigung und Punkt)|Deutung einer Gleichungskette|Formulieren einer Aufgabe",
    format="Begründung", operator="Erläutern Sie|Formulieren Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="h_a(x) = e^(a − x) + x − a mit h_a'(x) = −e^(a − x) + 1; vorgelegte Rechnung zu h_{−0,2}: t(x) = mx − 1,65; m = h'_{−0,2}(x_Q) = −e^(−0,2 − x_Q) + 1; h_{−0,2}(x_Q) = t(x_Q) ⇒ x_Q ≈ −1,503, y_Q ≈ 2,38 ⇒ Q(−1,5 | 2,38)",
    gesucht="Erläuterung der Schritte; passende Aufgabenstellung",
    verfahren="Schritte als Geradenansatz durch S, Tangentensteigung und Berührbedingung deuten",
    schritte="3", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="Gesucht ist der Berührpunkt Q der Tangente, die vom Punkt S(0 | −1,65) (aus e) an den Graphen von h_{−0,2} gelegt wird: Geradenansatz durch S mit Steigung m, m gleich der Ableitung in Q, Q auf Gerade und Graph; Lösung Q(−1,5 | 2,38)",
    zwischenergebnis="", niveau_geschaetzt="III",
    fehlerquelle="die Gleichungskette nur nachrechnen statt deuten; Aufgabe ohne den Bezug zu S formulieren",
    bemerkung="Landesaufgabe. Enge Fassung: vorgelegten Lösungsweg in eine Fragestellung zurückübersetzen (a) – III. Eigene Rechnung, mit sympy bestätigt (x_Q ≈ −1,5028, y_Q ≈ 2,3767).")
row(id="2024-bebb-lk-B2.1h", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="h", seite="6", punkte="2",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Scharparameter für einen vorgegebenen Schnittwinkel des Graphen mit der y-Achse bestimmen", typ_neben="",
    stichwoerter="Winkel 45° zur y-Achse: Tangentensteigung ±1|h_a'(0) = −e^a + 1 = −1 ⇒ e^a = 2 ⇒ a = ln 2|h_a'(0) = 1 unmöglich (e^a = 0)",
    voraussetzungen="Steigungswinkel und Steigung|Ableitung an der Stelle 0|Exponentialgleichung",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="h_a und h_a' wie in g",
    gesucht="Wert von a, für den der Graph von h_a die y-Achse im Winkel von 45° schneidet",
    verfahren="h_a'(0) = ±1 ansetzen, Exponentialgleichung lösen",
    schritte="2", zahlenraum="Potenz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="a = ln 2 ≈ 0,69",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Winkel zur y-Achse mit Steigung tan 45° = 1 gleichsetzen, ohne −1 zu prüfen (nur −1 führt zu einer Lösung)",
    bemerkung="Landesaufgabe. Enge Fassung: Winkelbedingung in eine Steigungsgleichung übersetzen, Standardgleichung – II. Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-B2.1i", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="i", seite="6", punkte="4",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Nullstellenfreiheit aller Scharkurven aus dem gemeinsamen Tiefpunktwert beurteilen", typ_neben="",
    stichwoerter="h_a'(x) = 0 ⇔ e^(a − x) = 1 ⇔ x = a|h_a''(x) = e^(a − x) > 0: Tiefpunkt (a | 1), einziger Extrempunkt|globales Minimum 1 > 0: keine Nullstelle|Aussage richtig",
    voraussetzungen="Extrempunkt mit Parameter|Konvexität, globales Minimum|Schluss vom Minimum auf Nullstellenfreiheit",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar h_a wie in g; Aussage: aus einer Untersuchung der Extrempunkte der Graphen der Schar h_a lässt sich schlussfolgern, dass keine Funktion der Schar eine Nullstelle besitzt",
    gesucht="Beurteilung der Aussage",
    verfahren="Extremstelle x = a, Art über h_a'' > 0, Tiefpunkt (a | 1) als einziges globales Minimum, Wert positiv",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="richtig: jeder Graph hat genau einen Extrempunkt, den Tiefpunkt (a | 1); da h_a'' > 0 (und h_a → +∞ an beiden Rändern), ist 1 das globale Minimum, also h_a(x) ≥ 1 > 0 für alle x",
    zwischenergebnis="Tiefpunkt (a | 1)", niveau_geschaetzt="II",
    fehlerquelle="nur den lokalen Tiefpunkt nennen, ohne ihn als globales Minimum zu begründen",
    bemerkung="Landesaufgabe. Enge Fassung: Standardverfahren Extrempunkt mit Parameter, ein Schluss (globales Minimum) – II. Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-B2.1j", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="j", seite="6", punkte="3",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral über eine Summe aus e-Funktion und linearem Term gegen eine Schranke nachweisen", typ_neben="",
    stichwoerter="h_{−0,2}(x) = e^(−0,2 − x) + x + 0,2|Stammfunktion −e^(−0,2 − x) + x²/2 + 0,2x|[…]_{−2}^{6} = e^(1,8) − e^(−6,2) + 17,6 ≈ 23,65 < 24",
    voraussetzungen="Stammfunktion von e^(c − x)|Hauptsatz|Vergleich mit Schranke",
    format="Rechnung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="h_{−0,2}(x) = e^(−0,2 − x) + x + 0,2; Behauptung ∫_{−2}^{6} h_{−0,2}(x) dx < 24",
    gesucht="Nachweis der Ungleichung",
    verfahren="Stammfunktion bilden, Hauptsatz, Wert mit 24 vergleichen",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="", abhaengig_von="",
    ergebnis="∫_{−2}^{6} h_{−0,2}(x) dx = e^(1,8) − e^(−6,2) + 17,6 ≈ 23,65 < 24",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Vorzeichen der Stammfunktion von e^(−0,2 − x) (innere Ableitung −1)",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt (23,6476).")
row(id="2024-bebb-lk-B2.1k", block="B", aufgabe="2.1", titel="Exponentialfunktionen", teilaufgabe="k", seite="6", punkte="3",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Flächeninhalt zwischen Graph und x-Achse am Bild mit einem berechneten Integralwert vergleichen", typ_neben="",
    stichwoerter="Graph II (G_{−0,2}) liegt auf [−2; 6] unterhalb der x-Achse|Abschätzung: von −2 bis 0 Werte zwischen −11,6 und −5 (Fläche über 15), von 0 bis 6 Werte unter −1,8 (über 12)|Fläche größer als 23,65 (exakt ≈ 30,7)",
    voraussetzungen="Fläche als Betrag des Integrals|Abschätzen am Bild",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SK21, kontext="ohne", textumfang="kurz",
    gegeben="Abbildung aus c; Inhalt der Fläche, die Graph II mit der x-Achse über [−2; 6] begrenzt; Vergleichswert aus j (≈ 23,65)",
    gesucht="ob der Flächeninhalt größer oder kleiner als der Wert aus j ist, mithilfe der Abbildung",
    verfahren="Fläche unter der x-Achse aus Kästchen oder Rechtecken abschätzen und mit 23,65 vergleichen",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="2024-bebb-lk-B2.1j",
    ergebnis="größer: die Fläche unter Graph II über [−2; 6] ist größer als 23,65 (Rechtecke 2 · 5 + 6 · 1,8 = 20,8 sind bereits fast der Wert, dazu die Spitze links bis −11,6; exakt ≈ 30,7)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Graph I statt II verwenden; Fläche mit dem (negativen) Integral verwechseln",
    bemerkung="Landesaufgabe. Enge Fassung: Abschätzung am Bild und Vergleich – II. Eigene Rechnung, mit sympy bestätigt (Fläche ≈ 30,70).")
# ---- Aufgabe 2.2 Lesebestätigung, Aufgabenteil 1 a, b, e abgewandelt (Seiten 7–8)
SK22 = "Koordinatensystem x von −4 bis 4, y von −4 bis 4 auf Kästchen; Graph von f₁(x) = x³ − 4x mit Nullstellen −2, 0, 2, Hochpunkt bei etwa (−1,2 | 3,1), Tiefpunkt bei etwa (1,2 | −3,1)"
row(id="2024-bebb-lk-B2.2a", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 1)", teilaufgabe="a", seite="7", punkte="2",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Symmetrie: Symmetrieart am Term über die Exponenten begründen", typ_neben="",
    stichwoerter="ax³ − 4x enthält nur ungerade Exponenten|f_a(−x) = −ax³ + 4x = −f_a(x)",
    voraussetzungen="Kriterium ungerade Exponenten",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SK22, kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a: x ↦ ax³ − 4x, a ∈ IR⁺, definiert in IR; Abbildung mit dem Graphen einer Funktion der Schar",
    gesucht="Begründung, dass jeder Graph der Schar punktsymmetrisch zum Koordinatenursprung ist",
    verfahren="Exponenten prüfen oder f_a(−x) = −f_a(x) nachrechnen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="der Term von f_a ist ein Polynom mit ausschließlich ungeraden Exponenten von x (gleichwertig: f_a(−x) = −f_a(x))",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Symmetrie nur am abgebildeten Graphen ablesen",
    bemerkung="Abgewandelt von: 2024MerhoehtBAnalysisWTR2-1a; der Pool gibt die Schar f_{a;b}(x) = ax³ − bx mit zwei positiven Parametern, das Heft die Schar f_a(x) = ax³ − 4x mit einem Parameter (je 2 BE, Auftrag wortgleich). Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-B2.2b", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 1)", teilaufgabe="b", seite="7", punkte="6",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Tiefpunkt einer Schar mit zwei Parametern nachweisen und Hochpunkt über die Punktsymmetrie begründen", typ_neben="",
    stichwoerter="f_a'(x) = 3ax² − 4, f_a'(√(4/(3a))) = 4 − 4 = 0|f_a''(x) = 6ax > 0 an der Stelle: Tiefpunkt|Punktsymmetrie (a): Hochpunkt bei −√(4/(3a)), also links vom Tiefpunkt",
    voraussetzungen="Ableitungen mit Parameter|hinreichende Bedingung|Symmetrie überträgt Extrempunkte",
    format="Rechnung|Begründung", operator="Weisen Sie nach|Begründen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Schar f_a wie in a",
    gesucht="Nachweis eines Tiefpunkts mit der x-Koordinate √(4/(3a)); Begründung eines Hochpunkts mit kleinerer x-Koordinate",
    verfahren="f_a' und f_a'' an der Stelle, Punktsymmetrie für den Hochpunkt",
    schritte="4", zahlenraum="Wurzel|Bruch", einheiten="", abhaengig_von="2024-bebb-lk-B2.2a",
    ergebnis="f_a'(x) = 3ax² − 4, f_a'(√(4/(3a))) = 3a · 4/(3a) − 4 = 0; f_a''(x) = 6ax, f_a''(√(4/(3a))) = 6a · √(4/(3a)) > 0; wegen der Punktsymmetrie hat der Graph an der Stelle −√(4/(3a)) einen Hochpunkt, dessen x-Koordinate kleiner ist als die des Tiefpunkts",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Hochpunkt erneut mit f'' nachrechnen statt über die Symmetrie; Wurzel aus 4/(3a) falsch vereinfachen",
    bemerkung="Abgewandelt von: 2024MerhoehtBAnalysisWTR2-1b; der Pool weist √(b/(3a)) für die Schar mit zwei Parametern nach, das Heft √(4/(3a)) für f_a(x) = ax³ − 4x (je 6 BE, Aufträge wortgleich). Typ des Pools beibehalten (gleiche Fertigkeit, ein Parameter weniger). Eigene Rechnung, mit sympy bestätigt.")
row(id="2024-bebb-lk-B2.2e", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 1)", teilaufgabe="e", seite="8", punkte="7",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen", typ_neben="",
    stichwoerter="h(3) = 0 ⇒ 27b − 3c = 0 ⇒ c = 9b|h(x) = b · x · (x² − 9), für b > 0 unterhalb der x-Achse auf ]0; 3[|∫_0^3 h = −81b/4 = −40,5 ⇒ b = 2, c = 18",
    voraussetzungen="Nullstellenbedingung|Fläche unterhalb der x-Achse als negatives Integral|zwei Gleichungen für zwei Unbekannte",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="h: x ↦ bx³ − cx mit b, c ∈ IR; für einen Wert von b und einen Wert von c gilt: h hat bei x = 3 eine Nullstelle, und der Graph von h schließt im vierten Quadranten mit der x-Achse ein Flächenstück mit dem Inhalt 40,5 ein",
    gesucht="die zugehörigen Werte von b und c",
    verfahren="c = 9b aus der Nullstelle; Integral von 0 bis 3 gleich −40,5 (Flächenstück unter der Achse) nach b auflösen",
    schritte="4", zahlenraum="dezimal|Bruch", einheiten="", abhaengig_von="",
    ergebnis="b = 2, c = 18 (h(x) = 2x³ − 18x)",
    zwischenergebnis="c = 9b; ∫_0^3 (bx³ − 9bx) dx = −81b/4", niveau_geschaetzt="III",
    fehlerquelle="Integral positiv ansetzen; b < 0 nicht ausschließen (dann liegt das Flächenstück im vierten Quadranten nicht zwischen 0 und 3)",
    bemerkung="Abgewandelt von: 2024MerhoehtBAnalysisWTR2-1c; der Pool fragt nach der Funktion der Schar f_{a;b} (a, b > 0) mit Nullstelle 3 und Flächeninhalt 40,5, das Heft nach h(x) = bx³ − cx mit b, c ∈ IR und denselben Bedingungen (je 7 BE; Werte 2 und 18 wie im Pool a = 2, b = 18). Eichregel: (a) Flächenstück im vierten Quadranten in ein negatives Integral von 0 bis 3 übersetzen, verkettet mit der Nullstellenbedingung. Eigene Rechnung, mit sympy bestätigt.")
# ---- Dubletten aus dem Pool (dubletten.py, map_2024lk.py)
row(id="2024-bebb-lk-A1.1a", block="A", aufgabe="1.1", titel="Analysis (1.1)", teilaufgabe="a", seite="1", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einem Punkt des Graphen angeben",
    typ_neben="",
    stichwoerter="f_a(1) = a + a = 2a|2a = 6|a = 3",
    voraussetzungen="Punkt in den Term einsetzen",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Schar f_a(x) = a · x³ + a · x², definiert in IR, a > 0",
    gesucht="Wert von a, sodass (1; 6) auf dem Graphen von f_a liegt",
    verfahren="x = 1 einsetzen und nach a auflösen",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="a = 3",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="6 = a · 1³ ansetzen und a = 6 angeben",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAAnalysis12-a. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.2 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.1b", block="A", aufgabe="1.1", titel="Analysis (1.1)", teilaufgabe="b", seite="1", punkte="4", afb_amtlich="II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Fläche zwischen Graph und x-Achse in Abhängigkeit vom Scharparameter berechnen",
    typ_neben="",
    stichwoerter="f_a(x) = a x² (x + 1)|Nullstellen −1 und 0|Integral von −1 bis 0|Stammfunktion 1/4 a x⁴ + 1/3 a x³|Inhalt a/12",
    voraussetzungen="Nullstellen durch Ausklammern mit Parameter|Potenzregel der Integration mit Parameter|Vorzeichen des Integranden prüfen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Term",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f_a(x) = a · x³ + a · x² mit a > 0; der Graph schließt mit der x-Achse eine Fläche ein",
    gesucht="Inhalt dieser Fläche in Abhängigkeit von a",
    verfahren="Nullstellen −1 und 0 bestimmen, das Integral über [−1; 0] mit der Stammfunktion auswerten (dort ist f_a ≥ 0)",
    schritte="3",
    zahlenraum="Bruch|negativ|Potenz",
    einheiten="",
    ergebnis="f_a(x) = 0 ⇔ a x² (x + 1) = 0 ⇔ x = −1 oder x = 0; Integral von −1 bis 0 über (a x³ + a x²) dx = [1/4 a x⁴ + 1/3 a x³] von −1 bis 0 = 1/12 a",
    zwischenergebnis="Wert an der Stelle −1: a/4 − a/3 = −a/12",
    niveau_geschaetzt="II",
    fehlerquelle="das Vorzeichen bei der Auswertung an der unteren Grenze verlieren (−a/12 als Inhalt)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAAnalysis12-b. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.2 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.2a", block="A", aufgabe="1.2", titel="Analysis (1.2)", teilaufgabe="a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Vorzeichen der Funktionswerte einer Schar begründen",
    typ_neben="",
    stichwoerter="f_a(x) = x · e^(ax)|e^(ax) > 0|Produkt mit negativem x negativ|unterhalb der x-Achse für x < 0",
    voraussetzungen="Positivität der e-Funktion|Vorzeichen eines Produkts",
    format="Begründung",
    operator="Begründen Sie",
    antwort="Text",
    material="Koordinatensystem",
    skizze="zwei Abbildungen ohne Skalen, je ein Koordinatensystem: Abb. 1 zeigt einen Graphen, der von links unten steil durch den Ursprung steigt, rechts einen Hochpunkt hat und dann flach gegen die x-Achse abfällt; Abb. 2 zeigt einen Graphen, der von links flach knapp unter der x-Achse kommt, einen Tiefpunkt links vom Ursprung hat, durch den Ursprung steigt und rechts steil nach oben verläuft",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Schar f_a(x) = x · e^(a · x), definiert in IR, a ≠ 0; jede f_a hat genau eine Extremstelle",
    gesucht="Begründung, dass der Graph von f_a für x < 0 unterhalb der x-Achse verläuft",
    verfahren="Vorzeichen der beiden Faktoren betrachten",
    schritte="1",
    zahlenraum="negativ|Potenz",
    einheiten="",
    ergebnis="wegen e^(a · x) > 0 sind die Funktionswerte x · e^(a · x) von f_a für negative x ebenfalls negativ",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="das Vorzeichen von a für ausschlaggebend halten",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAAnalysis13-a. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.3 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.2b", block="A", aufgabe="1.2", titel="Analysis (1.2)", teilaufgabe="b", seite="1", punkte="3", afb_amtlich="I|II",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Graph der Schar zum Parametervorzeichen über das Grenzverhalten zuordnen",
    typ_neben="",
    stichwoerter="für a > 0 strebt f_a(x) gegen +∞ für x → +∞|Abb. 1 fällt rechts gegen 0|genau eine Extremstelle|Abb. 2 gehört zu a > 0",
    voraussetzungen="Grenzverhalten von x · e^(ax) nach dem Vorzeichen von a|Anzahl der Extrempunkte am Graphen zählen",
    format="Begründung",
    operator="Entscheiden Sie|Begründen Sie",
    antwort="Text",
    material="Koordinatensystem",
    skizze="zwei Abbildungen ohne Skalen, je ein Koordinatensystem: Abb. 1 zeigt einen Graphen, der von links unten steil durch den Ursprung steigt, rechts einen Hochpunkt hat und dann flach gegen die x-Achse abfällt; Abb. 2 zeigt einen Graphen, der von links flach knapp unter der x-Achse kommt, einen Tiefpunkt links vom Ursprung hat, durch den Ursprung steigt und rechts steil nach oben verläuft",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Schar f_a(x) = x · e^(a · x), a ≠ 0, genau eine Extremstelle je Funktion; Abbildungen 1 und 2 zeigen je einen Graphen der Schar, einer davon für positives a",
    gesucht="Entscheidung, welche Abbildung den Graphen zu positivem a zeigt, mit Begründung",
    verfahren="für a > 0 wächst f_a für x → +∞ unbeschränkt; Abbildung 1 fällt rechts gegen die Achse und müsste dazu einen weiteren Extrempunkt haben, was ausgeschlossen ist",
    schritte="2",
    zahlenraum="Potenz",
    einheiten="",
    ergebnis="Abbildung 2; wegen lim f_a(x) = +∞ für x → +∞ bei a > 0 ist Abbildung 1 aufgrund des Fehlens weiterer Extrempunkte ausgeschlossen",
    zwischenergebnis="Extremstelle bei −1/a",
    niveau_geschaetzt="II",
    fehlerquelle="Abbildung 1 wählen, weil der Graph dort für x > 0 zunächst steigt",
    abhaengig_von="2024-bebb-lk-A1.2a",
    bemerkung="Dublette von: 2024MerhoehtAAnalysis13-b. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.3 b (Abbildungen 1 und 2 wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.3a", block="A", aufgabe="1.3", titel="Analytische Geometrie (1.3)", teilaufgabe="a", seite="1", punkte="2", afb_amtlich="I|II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharparameter für Parallelität von Ebene und Gerade ermitteln",
    typ_neben="",
    stichwoerter="E_a: 2a x1 − 4 x2 + (a − 2) x3 = 12|Normalenvektor (2a; −4; a − 2)|Richtungsvektor (−1; 0; 1)|Skalarprodukt −2a + a − 2 = 0|a = −2",
    voraussetzungen="Parallelität Ebene–Gerade als Normalenvektor senkrecht zum Richtungsvektor|Skalarprodukt mit Parameter",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Ebenenschar E_a: 2a · x1 − 4 · x2 + (a − 2) · x3 = 12, a reell; Gerade x = (0; 1; 1) + b · (−1; 0; 1)",
    gesucht="Wert von a, für den E_a parallel zur Geraden verläuft",
    verfahren="Skalarprodukt von Normalen- und Richtungsvektor gleich null setzen",
    schritte="2",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="(2a; −4; a − 2) · (−1; 0; 1) = 0 ⇔ −2a + a − 2 = 0 ⇔ a = −2",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den Stützpunkt der Geraden in die Ebenengleichung einsetzen",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAAGLAA212-a. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 1.2 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.3b", block="A", aufgabe="1.3", titel="Analytische Geometrie (1.3)", teilaufgabe="b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Zugehörigkeit einer Ebene zu einer Schar prüfen",
    typ_neben="",
    stichwoerter="6 x1 − 8 x2 + x3 = 24|Normalenvektoren kollinear: (2a; −4; a − 2) = k · (6; −8; 1)|k = 0,5|2a = 3 und a − 2 = 0,5 widersprechen sich|nicht zur Schar",
    voraussetzungen="gleiche Ebene heißt Vielfaches der Koordinatengleichung|Gleichungssystem für a und k auf Widerspruch prüfen",
    format="Rechnung",
    operator="Prüfen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Schar E_a: 2a · x1 − 4 · x2 + (a − 2) · x3 = 12; Ebene 6 x1 − 8 x2 + x3 = 24",
    gesucht="Prüfung, ob die Ebene zur Schar gehört",
    verfahren="Normalenvektor der Schar als Vielfaches k des gegebenen ansetzen; aus der zweiten Koordinate k = 0,5, die übrigen Gleichungen für a widersprechen sich",
    schritte="3",
    zahlenraum="ganz|dezimal|negativ",
    einheiten="",
    ergebnis="(2a; −4; a − 2) = k · (6; −8; 1) ergibt k = 0,5; das Gleichungssystem I 2a = 3, II a − 2 = 0,5 besitzt keine Lösung, die Ebene gehört nicht zur Schar",
    zwischenergebnis="aus I a = 1,5, aus II a = 2,5",
    niveau_geschaetzt="II",
    fehlerquelle="nur die rechte Seite vergleichen (24 = 2 · 12) und Zugehörigkeit bejahen",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAAGLAA212-b. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 1.2 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.5a", block="A", aufgabe="1.5", titel="Wahlaufgaben: Analysis (1.5)", teilaufgabe="a", seite="3", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung aus der Abbildung ablesen",
    typ_neben="",
    stichwoerter="Nullstelle der Tangente bei 2|y-Achsenabschnitt −8|Steigung 4|y = 4x − 8",
    voraussetzungen="Geradengleichung aus zwei Gitterpunkten ablesen",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Term",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit x-Achse von −4 bis 7 (Markierungen in Zweierschritten) und y-Achse von −10 bis 12, Gitter; Parabel f_1/2(x) = 1/2 x² mit Scheitel im Ursprung durch (4; 8) (markiert) und (−4; 8); Tangente t im Punkt (4; 8): Gerade mit Steigung 4 durch (2; 0) und (0; −8)",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Schar f_a(x) = a · x² für positives a; Graph von f_1/2 und Tangente t im Punkt (4; f_1/2(4)) in der Abbildung",
    gesucht="Gleichung von t anhand der Abbildung",
    verfahren="zwei Gitterpunkte der Tangente ablesen, etwa (2; 0) und (4; 8)",
    schritte="1",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="y = 4x − 8",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="die Steigung als 2 ablesen",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAAnalysis21-a. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 2.1 a (Abbildung wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.5b", block="A", aufgabe="1.5", titel="Wahlaufgaben: Analysis (1.5)", teilaufgabe="b", seite="3", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="y-Achsenabschnitt der Tangente allgemein nachweisen",
    typ_neben="",
    stichwoerter="Tangente in (u; f_a(u))|m = f_a'(u) = 2au|a u² = 2au · u + n|n = −a u² = −f_a(u)",
    voraussetzungen="Tangentengleichung mit allgemeiner Stelle u und Scharparameter a|Ableitung|nach n auflösen",
    format="Begründung",
    operator="Weisen Sie nach",
    antwort="Text",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit x-Achse von −4 bis 7 (Markierungen in Zweierschritten) und y-Achse von −10 bis 12, Gitter; Parabel f_1/2(x) = 1/2 x² mit Scheitel im Ursprung durch (4; 8) (markiert) und (−4; 8); Tangente t im Punkt (4; 8): Gerade mit Steigung 4 durch (2; 0) und (0; −8)",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f_a(x) = a · x², a > 0; für jedes reelle u die Tangente an den Graphen von f_a im Punkt (u; f_a(u))",
    gesucht="Nachweis, dass diese Tangente die y-Achse im Punkt (0; −f_a(u)) schneidet",
    verfahren="Ansatz y = mx + n mit m = f_a'(u) = 2au, Berührpunkt einsetzen, n bestimmen",
    schritte="3",
    zahlenraum="Potenz",
    einheiten="",
    ergebnis="Gleichung der Tangente y = mx + n; f_a(u) = a · u², m = f_a'(u) = 2a · u; a · u² = 2a · u · u + n ⇔ n = −a · u², d. h. n = −f_a(u)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur a = 1/2 und u = 4 aus a nachrechnen",
    abhaengig_von="2024-bebb-lk-A1.5a",
    bemerkung="Dublette von: 2024MerhoehtAAnalysis21-b. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 2.1 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.6a", block="A", aufgabe="1.6", titel="Wahlaufgaben: Analysis (1.6)", teilaufgabe="a", seite="3", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Flächeninhalt eines Rechtecks aus Nullstellen und Normale als parameterunabhängig nachweisen",
    typ_neben="",
    stichwoerter="f(x) = x (x − a)²|Nullstellen 0 und a als Rechteckecken|h senkrecht zur Tangente in O: Steigung −1/f'(0) = −1/a²|h(x) = −x/a²|Diagonale auf h: vierte Ecke (a; −1/a)|Fläche a · 1/a = 1",
    voraussetzungen="Nullstellen mit Parameter|Normale als Gerade mit Steigung −1/m|Rechteck aus zwei Ecken und Diagonalenrichtung konstruieren|Fläche mit Parameter vereinfachen",
    format="Zeichnen|Begründung",
    operator="Skizzieren Sie|Zeigen Sie",
    antwort="Grafik|Text",
    material="Koordinatensystem",
    skizze="Koordinatensystem ohne Skalen; Graph G von f(x) = x³ − 2a x² + a² x: durch den Ursprung steigend, Hochpunkt zwischen 0 und a, Berührpunkt mit der x-Achse in (a; 0), danach steil steigend; Gerade h (beschriftet) durch den Ursprung mit kleiner negativer Steigung, senkrecht zur Tangente in O",
    kontext="ohne",
    textumfang="lang",
    gegeben="a > 0; f(x) = x³ − 2a x² + a² x mit Graph G, Gerade h durch den Ursprung senkrecht zur Tangente an G im Ursprung; G berührt die x-Achse in (a; 0); Rechteck mit den gemeinsamen Punkten von G und x-Achse als benachbarten Ecken und einer Diagonale auf h",
    gesucht="Skizze des Rechtecks in der Abbildung|Nachweis, dass sein Flächeninhalt nicht von a abhängt",
    verfahren="f'(0) = a² liefert die Steigung −1/a² von h; das Rechteck hat die Ecken (0; 0), (a; 0) und die Höhe |h(a)| = 1/a unterhalb der Achse; Fläche a · 1/a",
    schritte="4",
    zahlenraum="Bruch|negativ|Potenz",
    einheiten="",
    ergebnis="f'(x) = 3x² − 4ax + a²; die Steigung von h beträgt −1/f'(0) = −1/a², also h(x) = −1/a² · x; Flächeninhalt des Rechtecks |h(a)| · a = 1/a · a = 1; Rechteck mit den Ecken (0; 0), (a; 0), (a; −1/a), (0; −1/a) unterhalb der x-Achse",
    zwischenergebnis="f'(0) = a²",
    niveau_geschaetzt="III",
    fehlerquelle="h als Tangente statt als Normale ansetzen (Steigung a²)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAAnalysis22. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 2.2 (eine Teilaufgabe ohne Buchstaben; Abbildung wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.7a", block="A", aufgabe="1.7", titel="Wahlaufgaben: Analytische Geometrie (1.7)", teilaufgabe="a", seite="4", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Kantenlänge eines Würfels aus gegenüberliegenden Oktaederecken nachweisen",
    typ_neben="",
    stichwoerter="A und C gegenüberliegende Flächenmittelpunkte|AC = (−4; −8; 8)|Länge √144 = 12 = Kantenlänge",
    voraussetzungen="Abstand gegenüberliegender Flächenmittelpunkte gleich Kantenlänge|Betrag eines Vektors",
    format="Begründung",
    operator="Weisen Sie nach",
    antwort="Text",
    material="Körper",
    skizze="Schrägbild ohne Koordinatenachsen: gestrichelter Würfel, darin ein Oktaeder mit durchgezogenen Kanten, dessen sechs Ecken die Mittelpunkte der Würfelflächen sind; die vier Ecken A (vorn), B (rechts), C (hinten) und D (links) liegen in einer Ebene, die beiden übrigen oben und unten",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Oktaeder mit den Flächenmittelpunkten eines Würfels als Ecken; A(1; 2; 1), B, C(−3; −6; 9), D liegen in der Ebene H: 2 x1 + x2 + 2 x3 = 6",
    gesucht="Nachweis, dass die Kantenlänge des Würfels 12 beträgt",
    verfahren="A und C sind Mittelpunkte gegenüberliegender Würfelflächen, ihr Abstand ist die Kantenlänge",
    schritte="2",
    zahlenraum="ganz|negativ|Wurzel",
    einheiten="",
    ergebnis="Kantenlänge des Würfels |AC| = |(−4; −8; 8)| = √144 = 12",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="|AC| als Oktaederkante deuten",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAAGLAA221-a. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 2.1 a (Abbildung wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.7b", block="A", aufgabe="1.7", titel="Wahlaufgaben: Analytische Geometrie (1.7)", teilaufgabe="b", seite="4", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen",
    typ_neben="",
    stichwoerter="Mittelpunkt M von AC: (−1; −2; 5) ist der Würfelmittelpunkt|Normalenvektor n = (2; 1; 2) mit |n| = 3|Abstand zur fehlenden Ecke: halbe Kante 6|OM + 2 · n = (3; 0; 9)",
    voraussetzungen="Würfelmittelpunkt als Mitte von AC|Normalenvektor der Ebene normieren|halbe Kantenlänge entlang der Normalen abtragen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild ohne Koordinatenachsen: gestrichelter Würfel, darin ein Oktaeder mit durchgezogenen Kanten, dessen sechs Ecken die Mittelpunkte der Würfelflächen sind; die vier Ecken A (vorn), B (rechts), C (hinten) und D (links) liegen in einer Ebene, die beiden übrigen oben und unten",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Oktaeder im Würfel der Kantenlänge 12; A(1; 2; 1), C(−3; −6; 9) in H: 2 x1 + x2 + 2 x3 = 6; zwei Ecken des Oktaeders liegen nicht in H",
    gesucht="Koordinaten einer dieser beiden Ecken",
    verfahren="Mittelpunkt M von AC ist der Würfelmittelpunkt; die fehlenden Ecken liegen im Abstand 6 (halbe Kante) senkrecht zu H, also M ± 6 · n/|n|",
    schritte="3",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="Mittelpunkt M der Strecke AC: M(−1; −2; 5); Normalenvektor n = (2; 1; 2) mit |n| = 3; OM + 2 · n = (3; 0; 9)",
    zwischenergebnis="zweite Ecke (−5; −4; 1)",
    niveau_geschaetzt="III",
    fehlerquelle="die volle Kantenlänge 12 statt 6 abtragen",
    abhaengig_von="2024-bebb-lk-A1.7a",
    bemerkung="Dublette von: 2024MerhoehtAAGLAA221-b. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 2.1 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-A1.10a", block="A", aufgabe="1.10", titel="Wahlaufgaben: Stochastik (1.10)", teilaufgabe="a", seite="4", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Würfelbeschriftung aus Erwartungswert und Trefferbedingung untersuchen",
    typ_neben="",
    stichwoerter="sichtbar 5, 5, 1|drei verdeckte Seiten aus 3, 4, 5, 6|Erwartungswert 4 heißt Summe 24, verdeckt 13|genau drei verschiedene Zahlen|P(zweimal gleich) = 1/2|3, 5, 5: (4/6)² + 2 · (1/6)² = 1/2|möglich",
    voraussetzungen="Erwartungswert als Mittel der sechs Zahlen|Bedingungen kombinieren|Wahrscheinlichkeit für gleiche Zahl bei zwei Würfen als Summe der Quadrate",
    format="Rechnung",
    operator="Untersuchen Sie",
    antwort="Text",
    material="Figur",
    skizze="Schrägbild eines Würfels mit drei sichtbaren Seiten, beschriftet mit 5 (vorn), 1 (rechts) und 5 (oben)",
    kontext="Würfel",
    textumfang="lang",
    gegeben="Würfel mit sichtbaren Seiten 5, 5, 1; drei unsichtbare Seiten sollen mit Zahlen aus 3, 4, 5, 6 beschriftet werden (Wiederholung erlaubt); Bedingungen: Erwartungswert beim einmaligen Werfen 4, genau drei verschiedene Zahlen auf dem Würfel, P(zweimal dieselbe Zahl bei zwei Würfen) = 1/2",
    gesucht="Untersuchung, ob eine Beschriftung alle drei Eigenschaften erfüllt",
    verfahren="aus E = 4 die Summe 24, also 13 für die verdeckten Seiten; Kandidaten mit genau drei verschiedenen Zahlen prüfen; für 3, 5, 5 die Wahrscheinlichkeit gleicher Zahlen ausrechnen",
    schritte="4",
    zahlenraum="Bruch",
    einheiten="",
    ergebnis="aus dem Erwartungswert 4 ergibt sich für die Summe der drei Zahlen auf den nicht sichtbaren Seiten der Wert 13; mit 3, 5 und 5 treffen die ersten beiden Aussagen zu, und die Wahrscheinlichkeit für zweimal dieselbe Zahl beträgt 4/6 · 4/6 + 2 · 1/6 · 1/6 = 1/2; die Beschriftung ist möglich",
    zwischenergebnis="Alternativen 3, 4, 6 und 4, 4, 5 verletzen die zweite oder dritte Bedingung",
    niveau_geschaetzt="III",
    fehlerquelle="die sichtbaren Seiten beim Erwartungswert vergessen (Summe 13 auf sechs Seiten verteilen)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtAStochastik22. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 2.2 (eine Teilaufgabe ohne Buchstaben; Würfelbild wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B2.2c", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 1)", teilaufgabe="c", seite="7", punkte="7", afb_amtlich="II",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Flächeninhalt des Dreiecks aus Tangente, Gerade und x-Achse berechnen",
    typ_neben="",
    stichwoerter="f'(x) = 3x² − 4, f'(2) = 8, t: y = 8x − 16|Schnitt mit g: 8x − 16 = −x − 2 ⇒ x = 14/9, y = −32/9|Dreieck mit Ecken A(2 | 0), (−2 | 0), Schnittpunkt: 1/2 · 4 · 32/9 = 64/9",
    voraussetzungen="Tangentengleichung|Schnittpunkt zweier Geraden|Nullstelle von g|Dreiecksfläche",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze="Koordinatensystem x von −4 bis 4, y von −4 bis 4; Graph von x³ − 4x mit Nullstellen −2, 0, 2, Hochpunkt bei etwa (−1,2 | 3,1), Tiefpunkt bei etwa (1,2 | −3,1)",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = x³ − 4x; Tangente in A(2 | 0); Gerade g: y = −x − 2",
    gesucht="Flächeninhalt des von t, x-Achse und g eingeschlossenen Dreiecks",
    verfahren="t aufstellen, Schnittpunkt mit g, Grundseite auf der x-Achse, Höhe",
    schritte="4",
    zahlenraum="Bruch|negativ",
    einheiten="",
    ergebnis="f'(x) = 3x² − 4, f'(2) = 8; 0 = 8 · 2 + n ⇔ n = −16, Tangente y = 8x − 16; Schnittpunkt mit g: 8x − 16 = −x − 2 ⇔ x = 14/9, y = −14/9 − 2 = −32/9; Flächeninhalt 1/2 · 4 · 32/9 = 64/9",
    zwischenergebnis="g schneidet die x-Achse bei −2",
    niveau_geschaetzt="II",
    fehlerquelle="Grundseite 2 statt 4 (Nullstelle von g bei −2 übersehen)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAnalysisWTR2-1d. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Pool Teilaufgabe 1 d; das Heft nennt die Funktion f₁ (Mitglied der Schar f_a: x ↦ ax³ − 4x), der Pool f mit f(x) = x³ − 4x – Aufträge und Zahlen gleich. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B2.2d", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 1)", teilaufgabe="d", seite="7", punkte="4", afb_amtlich="III",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Mittelpunkte der Strecken zum Ursprung auf einem gegebenen Graphen allgemein nachweisen",
    typ_neben="",
    stichwoerter="P(x | f(x)), Mittelpunkt (x/2 | f(x)/2)|h(x/2) = 4 (x/2)³ − 4 · x/2 = 1/2 (x³ − 4x) = 1/2 f(x)",
    voraussetzungen="Mittelpunkt als halbe Koordinaten|Punktprobe mit Parameter x",
    format="Begründung",
    operator="Begründen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="mittel",
    gegeben="f(x) = x³ − 4x; h(x) = 4x³ − 4x; Aussage: der Mittelpunkt von P und O liegt für jeden Graphenpunkt P auf dem Graphen von h",
    gesucht="Begründung der Aussage",
    verfahren="Mittelpunkt allgemein ansetzen, in h einsetzen",
    schritte="2",
    zahlenraum="ganz|Bruch",
    einheiten="",
    ergebnis="bezeichnet x die x-Koordinate eines Graphenpunkts P, so ist nachzuweisen, dass (x/2 | f(x)/2) auf dem Graphen von h liegt: h(x/2) = 4 · (x/2)³ − 4 · x/2 = 1/2 · (x³ − 4x) = 1/2 · f(x)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur einen konkreten Punkt prüfen",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAnalysisWTR2-1e. AB amtlich: III. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Pool Teilaufgabe 1 e; das Heft nennt die Vergleichsfunktion f₄ (Mitglied der Schar), der Pool h – derselbe Term 4x³ − 4x. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B2.2f", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 2 a)", teilaufgabe="f", seite="8", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate aus dem Graphen im Sachzusammenhang bestimmen",
    typ_neben="",
    stichwoerter="(4364 − 1701)/1,5 ≈ 1775 je Stunde",
    voraussetzungen="Differenzenquotient aus Tabellenwerten|Zeitraum in Stunden",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Tabelle Zeitpunkt 7:30 bis 15:00 Uhr mit bis dahin eingegangenen Lesebestätigungen: 252, 899, 1701, 2627, 3503, 4364, …, 7552, 7572",
    kontext="Lesebestätigungen/E-Mail",
    textumfang="mittel",
    gegeben="Tabelle der bis zum Zeitpunkt eingegangenen Lesebestätigungen; 8:30 Uhr 1701, 10:00 Uhr 4364",
    gesucht="mittlere Anzahl je Stunde von 8:30 bis 10:00 Uhr",
    verfahren="Differenz durch 1,5 Stunden",
    schritte="1",
    zahlenraum="ganz|dezimal",
    einheiten="Stunden",
    ergebnis="(4364 − 1701)/1,5 ≈ 1775",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="durch 3 Halbstunden statt durch 1,5 teilen",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAnalysisWTR2-2a. AB amtlich: I. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Pool Teilaufgabe 2 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B2.2g", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 2 b)", teilaufgabe="g", seite="8", punkte="3", afb_amtlich="I",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Funktionswert im Sachzusammenhang berechnen",
    typ_neben="",
    stichwoerter="k(2) = u(2) = 800 − 3600 + 4600 = 1800|um 9:00 Uhr momentane Änderungsrate 1800 je Stunde",
    voraussetzungen="richtigen Abschnitt wählen (x = 2 < 3: u)|Deutung als Rate",
    format="Rechnung|Kurzantwort",
    operator="Berechnen Sie|Interpretieren Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Lesebestätigungen/E-Mail",
    textumfang="lang",
    gegeben="k(x) = u(x) = 100x³ − 900x² + 2300x für 0 ≤ x < 3, v(x) = 20x² − 520x + 2880 für 3 ≤ x ≤ 8; x Stunden seit 7:00 Uhr, k(x) momentane Änderungsrate der Anzahl der Lesebestätigungen in 1/h",
    gesucht="k(2) und Deutung",
    verfahren="u(2) berechnen, als Rate um 9:00 Uhr deuten",
    schritte="2",
    zahlenraum="ganz",
    einheiten="1/h|Stunden",
    ergebnis="k(2) = 1800, d. h. um 9:00 Uhr beträgt die momentane Änderungsrate der Anzahl der seit 7:00 Uhr eingegangenen Lesebestätigungen laut Modell 1800 1/h",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="k(2) als Anzahl der Bestätigungen um 9:00 Uhr deuten",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAnalysisWTR2-2b. AB amtlich: I. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Pool Teilaufgabe 2 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B2.2h", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 2 c)", teilaufgabe="h", seite="8", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Eignung eines Modells über das Vorzeichen der Änderungsrate nach einer Nullstelle beurteilen",
    typ_neben="",
    stichwoerter="v(x) = 20(x − 18)(x − 8) wechselt bei 8 das Vorzeichen von plus nach minus|nach 15:00 Uhr negative Änderungsrate: unmöglich (Anzahl kann nicht sinken)",
    voraussetzungen="Vorzeichenwechsel aus der Faktorisierung|Rate einer Anzahl kann nicht negativ sein",
    format="Begründung",
    operator="Begründen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Lesebestätigungen/E-Mail",
    textumfang="kurz",
    gegeben="v(x) = 20 · (x − 18) · (x − 8)",
    gesucht="Begründung, dass v nach 15:00 Uhr (x > 8) ungeeignet ist",
    verfahren="Vorzeichen von v für x etwas größer als 8",
    schritte="2",
    zahlenraum="ganz",
    einheiten="Stunden",
    ergebnis="da v(x) an der Stelle 8 sein Vorzeichen von plus nach minus ändert, würden sich unmittelbar nach 15:00 Uhr negative Änderungsraten ergeben, was in diesem Sachzusammenhang unmöglich ist",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="mit der Nullstelle 18 argumentieren",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAnalysisWTR2-2c. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Pool Teilaufgabe 2 c. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B2.2i", block="B", aufgabe="2.2", titel="Lesebestätigung (Aufgabenteil 2 d)", teilaufgabe="i", seite="9", punkte="5", afb_amtlich="II",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Integral einer Rate berechnen und als Gesamtmenge im Sachzusammenhang deuten",
    typ_neben="Prozentuale Abweichung eines Näherungswerts vom exakten Wert berechnen",
    stichwoerter="10:00 bis 15:00 Uhr: x von 3 bis 8, Abschnitt v|∫_3^8 v = [20/3 x³ − 260x² + 2880x]_3^8 ≈ 3333|Tabelle: 7572 − 4364 = 3208|Abweichung (3333 − 3208)/3208 ≈ 3,9 %",
    voraussetzungen="Zeitraum auf den richtigen Abschnitt abbilden|Integral der Rate als Anzahl|Tabellendifferenz|relative Abweichung",
    format="Rechnung",
    operator="Berechnen Sie|Ermitteln Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Tabelle wie in a",
    kontext="Lesebestätigungen/E-Mail",
    textumfang="mittel",
    gegeben="k wie in b; Tabellenwerte 4364 (10:00 Uhr) und 7572 (15:00 Uhr)",
    gesucht="Anzahl der Lesebestätigungen von 10:00 bis 15:00 Uhr laut Modell; prozentuale Abweichung vom Tabellenwert",
    verfahren="Integral über v von 3 bis 8, Differenz der Tabellenwerte, Quotient",
    schritte="4",
    zahlenraum="ganz|Bruch|Prozent",
    einheiten="Stunden",
    ergebnis="∫_3^8 k(x) dx = [20/3 x³ − 260x² + 2880x]_3^8 ≈ 3333; (3333 − (7572 − 4364))/(7572 − 4364) ≈ 3,9 %",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Integral über u statt v oder Grenzen 10 bis 15",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAnalysisWTR2-2d. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Pool Teilaufgabe 2 d. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B3a", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="a", seite="10", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen",
    typ_neben="",
    stichwoerter="Seitenfläche 1/2 · 6 · √(4² + 3²) = 15|Oberfläche 6 · 6 + 4 · 15 = 96",
    voraussetzungen="Höhe einer Seitenfläche über Pythagoras|Grundfläche plus vier Dreiecke",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Abb. 1: Schrägbild der Pyramide ABCDS mit quadratischer Grundfläche (A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0)) in der xy-Ebene, O im Zentrum, Spitze S(0 | 0 | 4); Abb. 2 zusätzlich mit einer Spurgeraden g_k in der xy-Ebene und dem Lotfußpunkt R_k; Erwartungshorizont g: R_1 auf der Kante BC bei (3 | 0 | 0), R_{−1} auf AD bei (−3 | 0 | 0)",
    kontext="ohne",
    textumfang="kurz",
    gegeben="A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0), S(0 | 0 | 4)",
    gesucht="Oberflächeninhalt der Pyramide",
    verfahren="Seitenhöhe, Dreiecksfläche, Summe",
    schritte="3",
    zahlenraum="ganz|Wurzel",
    einheiten="",
    ergebnis="Inhalt einer Seitenfläche 1/2 · 6 · √(4² + 3²) = 15; Inhalt der Oberfläche 6 · 6 + 4 · 15 = 96",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Kantenlänge |SC| statt Seitenhöhe",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAGLAA2WTR1-1a. AB amtlich: I. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Abbildung 1 wie im Pool. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B3b", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="b", seite="10", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Spiegelung",
    typ="Symmetrieebene eines Körpers unter vorgegebenen Gleichungen auswählen und eine ausschließen",
    typ_neben="",
    stichwoerter="(3) x + y = 0: Diagonalebene durch B, D, S – Symmetrieebene|(1) x − z = 0 enthält S nicht (0 − 4 ≠ 0): keine Symmetrieebene|(2) x + y + z = 4 enthält S, aber nicht O",
    voraussetzungen="Symmetrieebene enthält die Spitze und die Achse|Punktprobe",
    format="Kurzantwort|Begründung",
    operator="Geben Sie an|Begründen Sie",
    antwort="Text",
    material="Körper",
    skizze="Abb. 1: Schrägbild der Pyramide ABCDS mit quadratischer Grundfläche (A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0)) in der xy-Ebene, O im Zentrum, Spitze S(0 | 0 | 4); Abb. 2 zusätzlich mit einer Spurgeraden g_k in der xy-Ebene und dem Lotfußpunkt R_k; Erwartungshorizont g: R_1 auf der Kante BC bei (3 | 0 | 0), R_{−1} auf AD bei (−3 | 0 | 0)",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Gleichungen (1) x − z = 0, (2) x + y + z = 4, (3) x + y = 0; genau eine beschreibt eine Symmetrieebene",
    gesucht="die Symmetrieebene; Begründung für eine der anderen",
    verfahren="Ebene durch S und O suchen, Gegenbeispiel über Punktprobe",
    schritte="2",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="(3) beschreibt eine Ebene, die Symmetrieebene der Pyramide ist; die Koordinaten von S erfüllen Gleichung (1) nicht",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="(2) wegen S ∈ Ebene für die Symmetrieebene halten",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAGLAA2WTR1-1b. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B3c", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="c", seite="10", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen",
    typ_neben="",
    stichwoerter="CD = (−6; 0; 0) ⇒ n1 = 0|CS = (−3; −3; 4): −3n2 + 4n3 = 0 ⇒ n = (0; 4; 3)|4y + 3z = d, C: d = 12",
    voraussetzungen="Normalenvektor aus Skalarprodukten|Punkt einsetzen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Term",
    material="Körper",
    skizze="Abb. 1: Schrägbild der Pyramide ABCDS mit quadratischer Grundfläche (A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0)) in der xy-Ebene, O im Zentrum, Spitze S(0 | 0 | 4); Abb. 2 zusätzlich mit einer Spurgeraden g_k in der xy-Ebene und dem Lotfußpunkt R_k; Erwartungshorizont g: R_1 auf der Kante BC bei (3 | 0 | 0), R_{−1} auf AD bei (−3 | 0 | 0)",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Ebene E durch C, D, S; Kontrolle 4y + 3z = 12",
    gesucht="Koordinatengleichung von E",
    verfahren="Skalarprodukte mit CD und CS, d aus C",
    schritte="3",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="(−6; 0; 0) · n = 0 liefert n1 = 0, (−3; −3; 4) · n = 0 liefert n3 = 3/4 n2; damit ist (0; 4; 3) ein Normalenvektor von E; E: 4y + 3z = d, aus C ∈ E ergibt sich d = 12",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="d aus S: 12 (gleich, aber Kontrolle nötig)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAGLAA2WTR1-1c. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge); afb_amtlich aus der Poolzeile (AB-Spalte). BE im Heft 4 statt 3 im Pool (das Heft verschiebt eine BE von f nach c; Summe 25 unverändert). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B3d", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="d", seite="10", punkte="5", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lösungsweg für den Punkt gleichen Abstands zu allen Seitenflächen einer Pyramide erläutern",
    typ_neben="",
    stichwoerter="I: Lotgerade zu E durch P(0 | 0 | p) mit dem Normalenvektor (0; 4; 3)|II: Q liegt in E – Schnittpunkt der Lotgeraden mit E, also Lotfußpunkt|III: |PQ| = p – Abstand zu E gleich Abstand zur Grundfläche (z = 0), also p; Symmetrie liefert die übrigen Seitenflächen",
    voraussetzungen="Lotgerade und Lotfußpunkt|Abstand Punkt–Ebene als Lotlänge|Abstand zur Grundfläche gleich z-Koordinate|Symmetrie der Pyramide",
    format="Begründung",
    operator="Erläutern Sie",
    antwort="Text",
    material="Körper",
    skizze="Abb. 1: Schrägbild der Pyramide ABCDS mit quadratischer Grundfläche (A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0)) in der xy-Ebene, O im Zentrum, Spitze S(0 | 0 | 4); Abb. 2 zusätzlich mit einer Spurgeraden g_k in der xy-Ebene und dem Lotfußpunkt R_k; Erwartungshorizont g: R_1 auf der Kante BC bei (3 | 0 | 0), R_{−1} auf AD bei (−3 | 0 | 0)",
    kontext="ohne",
    textumfang="lang",
    gegeben="P(0 | 0 | p) im Innern mit gleichem Abstand zu allen vier Seitenflächen und zur Grundfläche; Gleichungssystem I OQ = (0; 0; p) + t · (0; 4; 3), II 4 · 4t + 3 · (p + 3t) = 12, III |PQ| = p",
    gesucht="Erläuterung der geometrischen Überlegungen",
    verfahren="jede Gleichung als Lot, Lotfußpunkt, Abstandsgleichheit deuten",
    schritte="3",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="Q ist ein Punkt der Lotgeraden zu E durch P; Q liegt außerdem in E und ist damit der Schnittpunkt der Lotgeraden mit E; der Abstand von P zu E stimmt mit dem Abstand von P zur Grundfläche überein",
    zwischenergebnis="p = 1,5",
    niveau_geschaetzt="III",
    fehlerquelle="III als Abstand zur Spitze deuten",
    abhaengig_von="2024-bebb-lk-B3c",
    bemerkung="Dublette von: 2024MerhoehtBAGLAA2WTR1-1d. AB amtlich: III. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B3e", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="e", seite="10", punkte="1", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Gemeinsamen Punkt aller Ebenen einer Schar nachweisen",
    typ_neben="",
    stichwoerter="4k · 0 + 4√(1 − k²) · 0 + 3 · 4 = 12 für alle k",
    voraussetzungen="Punktprobe mit Parameter",
    format="Rechnung",
    operator="Zeigen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="E_k: 4k · x + 4√(1 − k²) · y + 3z = 12, k ∈ [−1; 1]; S(0 | 0 | 4)",
    gesucht="Nachweis S ∈ E_k für alle k",
    verfahren="S einsetzen",
    schritte="1",
    zahlenraum="ganz|Wurzel",
    einheiten="",
    ergebnis="wegen 4k · 0 + 4√(1 − k²) · 0 + 3 · 4 = 12 gilt S ∈ E_k",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="keine",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAGLAA2WTR1-1e. AB amtlich: I. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B3f", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="f", seite="10", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Schnittwinkel einer Geraden mit allen Ebenen einer Schar als parameterunabhängig nachweisen",
    typ_neben="",
    stichwoerter="Richtungsvektor von OS: (0; 0; 1)|sin α = |n_k · (0; 0; 1)|/|n_k| = 3/√(16k² + 16 − 16k² + 9) = 3/5|unabhängig von k",
    voraussetzungen="Winkel Gerade–Ebene über den Normalenvektor|Betrag mit Parameter vereinfachen",
    format="Rechnung",
    operator="Weisen Sie nach",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Gerade OS; Schar E_k wie in e",
    gesucht="Nachweis, dass der Schnittwinkel nicht von k abhängt",
    verfahren="Sinus des Winkels mit n_k, k fällt heraus",
    schritte="2",
    zahlenraum="Wurzel|Bruch",
    einheiten="",
    ergebnis="((4k; 4√(1 − k²); 3) · (0; 0; 1)) / (|(4k; 4√(1 − k²); 3)| · |(0; 0; 1)|) = 3/√(16k² + 16 − 16k² + 9) = 3/5; damit ist die Größe des Winkels unabhängig von k",
    zwischenergebnis="α ≈ 36,9°",
    niveau_geschaetzt="II",
    fehlerquelle="cos statt sin (Winkel Gerade–Ebene)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAGLAA2WTR1-1f. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge); afb_amtlich aus der Poolzeile (AB-Spalte). BE im Heft 3 statt 4 im Pool (siehe c). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B3g", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="g", seite="11", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Lotfußpunkte vom Ursprung auf Spurgeraden von Scharebenen einzeichnen",
    typ_neben="",
    stichwoerter="E_{−1}: −4x + 3z = 12, Spur in der xy-Ebene x = −3 (Kante AD) ⇒ R_{−1}(−3 | 0 | 0)|E_1: 4x + 3z = 12, Spur x = 3 (Kante BC) ⇒ R_1(3 | 0 | 0)",
    voraussetzungen="Spurgerade für z = 0|Punkt kleinsten Abstands als Lotfußpunkt|Kantenmitten",
    format="Zeichnen",
    operator="Zeichnen Sie ein",
    antwort="Grafik",
    material="Körper",
    skizze="Abb. 1: Schrägbild der Pyramide ABCDS mit quadratischer Grundfläche (A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0)) in der xy-Ebene, O im Zentrum, Spitze S(0 | 0 | 4); Abb. 2 zusätzlich mit einer Spurgeraden g_k in der xy-Ebene und dem Lotfußpunkt R_k; Erwartungshorizont g: R_1 auf der Kante BC bei (3 | 0 | 0), R_{−1} auf AD bei (−3 | 0 | 0)",
    kontext="ohne",
    textumfang="mittel",
    gegeben="g_k Schnittgerade von E_k mit der xy-Ebene, R_k Punkt auf g_k mit kleinstem Abstand zu O; Abbildung 2",
    gesucht="R_{−1} und R_1 in Abbildung 2",
    verfahren="Spuren von E_{±1} als Kanten AD und BC erkennen, Mittelpunkte markieren",
    schritte="2",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="R_1 als Mittelpunkt der Kante BC, R_{−1} als Mittelpunkt der Kante AD eingezeichnet",
    zwischenergebnis="R_{±1}(±3 | 0 | 0)",
    niveau_geschaetzt="II",
    fehlerquelle="R_k auf die Ecken B, C legen",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBAGLAA2WTR1-1g. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Abbildung 2 wie im Pool. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B3h", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="h", seite="11", punkte="3", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Rotationskörper einer Scharfläche als halben Kegel beschreiben und Volumen bestimmen",
    typ_neben="",
    stichwoerter="R_k durchläuft für k von −1 bis 1 den Halbkreis mit Radius 3 um O (y ≥ 0)|Dreieck OR_kS dreht sich um OS um 180°: halber Kegel mit Radius 3 und Höhe 4|V = 1/2 · 1/3 · π · 9 · 4 = 6π",
    voraussetzungen="Lage der R_k auf einem Halbkreis|Drehung um die Achse erzeugt einen Kegel|Kegelvolumen halbiert",
    format="Kurzantwort|Rechnung",
    operator="Beschreiben Sie|Bestimmen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Abb. 1: Schrägbild der Pyramide ABCDS mit quadratischer Grundfläche (A(−3 | −3 | 0), B(3 | −3 | 0), C(3 | 3 | 0), D(−3 | 3 | 0)) in der xy-Ebene, O im Zentrum, Spitze S(0 | 0 | 4); Abb. 2 zusätzlich mit einer Spurgeraden g_k in der xy-Ebene und dem Lotfußpunkt R_k; Erwartungshorizont g: R_1 auf der Kante BC bei (3 | 0 | 0), R_{−1} auf AD bei (−3 | 0 | 0)",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Fläche OR_kS dreht sich für k von −1 bis 1 um die Strecke OS",
    gesucht="Form und Volumen des entstehenden Körpers",
    verfahren="Bahn der R_k als Halbkreis, halber Kegel",
    schritte="3",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="der Körper hat die Form eines senkrecht zur Grundfläche halbierten Kegels; Volumen 1/6 · π · 3² · 4 = 6π",
    zwischenergebnis="|OR_k| = 3 für alle k",
    niveau_geschaetzt="III",
    fehlerquelle="ganzen Kegel (12π) angeben",
    abhaengig_von="2024-bebb-lk-B3g",
    bemerkung="Dublette von: 2024MerhoehtBAGLAA2WTR1-1h. AB amtlich: III. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B4a", block="B", aufgabe="4", titel="Video-Streamingdienst (Aufgabenteil 1)", teilaufgabe="a", seite="12", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen",
    typ_neben="",
    stichwoerter="A: höchstens 40 Jahre (70 %), B: Komplettpaket|P(B | A) = 80 %, P(B | nicht A) = 50 %",
    voraussetzungen="zweistufiges Baumdiagramm|Gegenwahrscheinlichkeiten",
    format="Zeichnen",
    operator="Stellen Sie dar",
    antwort="Grafik",
    material="keins",
    skizze="keine",
    kontext="Streamingdienst/Abonnenten",
    textumfang="mittel",
    gegeben="70 % höchstens 40 Jahre, davon 80 % Komplettpaket; von den Älteren 50 % Komplettpaket",
    gesucht="beschriftetes Baumdiagramm",
    verfahren="erste Stufe Alter, zweite Stufe Paket",
    schritte="1",
    zahlenraum="Prozent",
    einheiten="",
    ergebnis="Baumdiagramm mit A (70 %), nicht A (30 %); B | A 80 %, nicht B | A 20 %; B | nicht A 50 %, nicht B | nicht A 50 %",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Stufen vertauschen",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBStochastikWTR1-1a. AB amtlich: I. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Der Heftstamm sagt „Bei den über 40-jährigen Abonnenten haben sich 50 %“ statt „Unter denjenigen Abonnenten, die älter als 40 Jahre sind, haben sich 50 %“; Aufträge und Zahlen gleich. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B4b", block="B", aufgabe="4", titel="Video-Streamingdienst (Aufgabenteil 1)", teilaufgabe="b", seite="12", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit über Bayes aus dem Baumdiagramm berechnen",
    typ_neben="",
    stichwoerter="P(A | B) = 0,7 · 0,8 / (0,7 · 0,8 + 0,3 · 0,5) = 0,56/0,71 ≈ 79 %",
    voraussetzungen="Bayes: Pfad durch Summe der Pfade zu B",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Diagramm",
    skizze="Baumdiagramm: A (70 %, höchstens 40 Jahre) / nicht A (30 %), darunter B (Komplettpaket) 80 % bzw. 50 %",
    kontext="Streamingdienst/Abonnenten",
    textumfang="kurz",
    gegeben="Baumdiagramm aus a; Person mit Komplettpaket",
    gesucht="P(höchstens 40 Jahre | Komplettpaket)",
    verfahren="Bayes-Quotient",
    schritte="2",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="0,7 · 0,8 / (0,7 · 0,8 + 0,3 · 0,5) ≈ 79 %",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="P(B | A) = 80 % als Antwort",
    abhaengig_von="2024-bebb-lk-B4a",
    bemerkung="Dublette von: 2024MerhoehtBStochastikWTR1-1b. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B4c", block="B", aufgabe="4", titel="Video-Streamingdienst (Aufgabenteil 1)", teilaufgabe="c", seite="12", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln",
    typ_neben="",
    stichwoerter="X ~ B(n; 0,3), P(X > 5) ≥ 0,99|n = 39: 98,91 %, n = 40: 99,14 %|mindestens 40",
    voraussetzungen="p = 0,3 (älter als 40)|P(X > 5) = 1 − P(X ≤ 5) am Rechner|n durch Probieren",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Streamingdienst/Abonnenten",
    textumfang="mittel",
    gegeben="30 % der Abonnenten älter als 40; mit mindestens 99 % mehr als fünf Ältere unter n Ausgewählten",
    gesucht="kleinstes n",
    verfahren="P(X > 5) für n = 39 und 40 vergleichen",
    schritte="3",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="X Anzahl der Abonnenten, die älter als 40 sind; wegen P(X > 5) ≈ 98,91 % für n = 39 und ≈ 99,14 % für n = 40 (p = 0,3) müssten mindestens 40 Personen zufällig ausgewählt werden",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="P(X ≥ 5) statt P(X > 5)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBStochastikWTR1-1c. AB amtlich: III. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B4d", block="B", aufgabe="4", titel="Video-Streamingdienst (Aufgabenteil 2 a)", teilaufgabe="d", seite="12", punkte="2", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Wahl der Nullhypothese aus der Sicht des Entscheiders begründen",
    typ_neben="",
    stichwoerter="H0: p ≤ 0,6 – Ablehnung nur bei deutlichem Erfolg|vermeiden, den Algorithmus dauerhaft einzusetzen, obwohl er die Zufriedenheit nicht erhöht",
    voraussetzungen="Fehler erster Art als der zu vermeidende Fehler|Nullhypothese als Gegenteil des Erwünschten",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Streamingdienst/Signifikanztest",
    textumfang="lang",
    gegeben="Anteil zufriedener Abonnenten derzeit 60 %; Nullhypothese „Anteil höchstens 60 %“, Stichprobe 200, Signifikanzniveau 5 %; Entscheidung über den dauerhaften Einsatz des Algorithmus",
    gesucht="mögliche Überlegung des Managements zur Wahl dieser Nullhypothese",
    verfahren="den durch das Signifikanzniveau begrenzten Fehler benennen",
    schritte="1",
    zahlenraum="Prozent",
    einheiten="",
    ergebnis="es soll möglichst vermieden werden, den Algorithmus dauerhaft einzusetzen, obwohl der Einsatz die Zufriedenheit unter den Abonnenten nicht erhöht",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den Fehler zweiter Art als Grund nennen",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBStochastikWTR1-2a. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B4e", block="B", aufgabe="4", titel="Video-Streamingdienst (Aufgabenteil 2 b)", teilaufgabe="e", seite="13", punkte="4", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Lücke in einem Lösungsweg zur Ablehnungsgrenze begründen und ergänzen",
    typ_neben="",
    stichwoerter="P(Y ≥ 132) ≈ 0,047 ≤ 0,05 zeigt nur, dass 132 zulässig ist|es könnte ein k < 132 mit P(Y ≥ k) ≤ 0,05 geben|P(Y ≥ 131) ≈ 0,064 > 0,05 ⇒ 132 ist die untere Grenze",
    voraussetzungen="Ablehnungsbereich als größtmöglicher Bereich unter α|Nachbarwert prüfen",
    format="Begründung|Rechnung",
    operator="Begründen Sie|Ergänzen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Streamingdienst/Signifikanztest",
    textumfang="mittel",
    gegeben="Ablehnungsbereich {132; …; 200}; Lösungsschritte: Y Anzahl der zufriedenen Abonnenten, P(Y ≥ 132) ≈ 0,047 (n = 200, p = 0,6)",
    gesucht="Begründung, warum die Schritte nicht ausreichen, und Ergänzung",
    verfahren="Minimalität der Grenze über P(Y ≥ 131) belegen",
    schritte="2",
    zahlenraum="dezimal",
    einheiten="",
    ergebnis="es könnte eine natürliche Zahl k < 132 geben, für die P(Y ≥ k) ≤ 0,05 gilt; P(Y ≥ 131) ≈ 0,064; damit ist 132 die untere Grenze des Ablehnungsbereichs",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="P(Y ≥ 133) prüfen (falsche Richtung)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBStochastikWTR1-2b. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B4f", block="B", aufgabe="4", titel="Video-Streamingdienst (Aufgabenteil 2 c)", teilaufgabe="f", seite="13", punkte="4", afb_amtlich="III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Fehler zweiter Art für selbst gewählte Anteile berechnen und einordnen",
    typ_neben="",
    stichwoerter="p > 0,6 wählen, z. B. 0,61 (H0 falsch)|Fehler 2. Art: Y ≤ 131|P_{0,61}(Y ≤ 131) ≈ 91,7 % > 90 %",
    voraussetzungen="Fehler zweiter Art als Nichtablehnung bei falscher H0|Anteil knapp über 60 % wählen|kumulierte Wahrscheinlichkeit",
    format="Rechnung",
    operator="Weisen Sie nach",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Streamingdienst/Signifikanztest",
    textumfang="kurz",
    gegeben="Ablehnungsbereich {132; …; 200}",
    gesucht="Nachweis, dass der Fehler zweiter Art mehr als 90 % betragen könnte",
    verfahren="p knapp über 0,6 wählen, P(Y ≤ 131) berechnen",
    schritte="2",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="beträgt der Anteil der zufriedenen Abonnenten beispielsweise 61 %, dann trifft die Nullhypothese nicht zu und die Wahrscheinlichkeit des zugehörigen Fehlers zweiter Art beträgt P(Y ≤ 131) ≈ 91,7 % (n = 200, p = 0,61)",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="p ≤ 0,6 wählen (dann kein Fehler zweiter Art)",
    abhaengig_von="2024-bebb-lk-B4e",
    bemerkung="Dublette von: 2024MerhoehtBStochastikWTR1-2c. AB amtlich: III. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B4g", block="B", aufgabe="4", titel="Video-Streamingdienst (Aufgabenteil 3 a)", teilaufgabe="g", seite="13", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anteil der Kennwörter aus einer Teilmenge der Zeichen mit Wiederholung berechnen",
    typ_neben="",
    stichwoerter="26⁸ Kennwörter nur aus Kleinbuchstaben, 80⁸ insgesamt|26⁸/80⁸ ≈ 0,00012 < 0,001",
    voraussetzungen="Anzahl mit Wiederholung als Potenz|Quotient",
    format="Rechnung",
    operator="Zeigen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Kennwörter",
    textumfang="mittel",
    gegeben="80 Zeichen (26 Groß-, 26 Kleinbuchstaben, 10 Ziffern, 18 Sonderzeichen); Kennwörter aus genau acht Zeichen, Wiederholung erlaubt",
    gesucht="Nachweis, dass Kennwörter nur aus Kleinbuchstaben weniger als ein Tausendstel ausmachen",
    verfahren="Potenzen bilden, Quotient",
    schritte="2",
    zahlenraum="Potenz|dezimal",
    einheiten="",
    ergebnis="26⁸/80⁸ ≈ 0,00012 < 0,001",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="8 · 26 statt 26⁸",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBStochastikWTR1-3a. AB amtlich: I. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2024-bebb-lk-B4h", block="B", aufgabe="4", titel="Video-Streamingdienst (Aufgabenteil 3 b)", teilaufgabe="h", seite="13", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl der Kennwörter mit fester Buchstabenfolge und zwei Zusatzzeichen berechnen",
    typ_neben="",
    stichwoerter="Niclas belegt sechs der acht Stellen in fester Reihenfolge|zwei Stellen für Zusatzzeichen: C(8; 2) Lagen|Zusatzzeichen verschieden und nicht aus Niclas: 74 · 73|C(8; 2) · 74 · 73 = 151256",
    voraussetzungen="Lagen der Zusatzstellen als Binomialkoeffizient|verbleibende Zeichen ohne Wiederholung",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Kennwörter",
    textumfang="lang",
    gegeben="acht verschiedene Zeichen; Buchstaben von Niclas in Reihenfolge und Schreibung enthalten; Beispiele Nic4+las, nNicl*as",
    gesucht="Anzahl solcher Kennwörter",
    verfahren="Lagen der zwei freien Stellen mal Zeichenwahl",
    schritte="3",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="C(8; 2) · 74 · 73 = 151256",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="74² (Wiederholung) oder 80 · 79 (Buchstaben von Niclas nicht ausschließen)",
    abhaengig_von="",
    bemerkung="Dublette von: 2024MerhoehtBStochastikWTR1-3b. AB amtlich: II. Wortgleich mit der Poolaufgabe 2024 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")

NEUE_TYPEN = [
    ("Ziehen ohne Zurücklegen: Wahrscheinlichkeit für genau drei aufeinanderfolgende gleichfarbige Kugeln beim Ziehen ohne Zurücklegen berechnen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Beim mehrfachen Ziehen ohne Zurücklegen aus einer zweifarbigen Urne die günstigen Farbfolgen mit genau drei aufeinanderfolgenden gleichen Farben aufzählen und ihre Pfadwahrscheinlichkeiten addieren.",
     "2024-bebb-lk-A1.4a"),
    ("Ziehen ohne Zurücklegen: Kugelzahl für eine begrenzte Anzahl von Farbreihenfolgen beim Ziehen ohne Zurücklegen begründen", "Stochastik", "Zufallsexperimente und Urnenmodelle",
     "Begründen, dass bei n Kugeln je Farbe und mehr als n Ziehungen ohne Zurücklegen nicht alle 2^k Farbfolgen möglich sind, und einen passenden Wert von n mit der Anzahl der Reihenfolgen angeben.",
     "2024-bebb-lk-A1.4b"),
    ("Gerade und Ebene: Lage einer Geradenschar zu einer Ebene mit Fallunterscheidung nach dem Parameter untersuchen", "Analytische Geometrie", "Lagebeziehungen",
     "Für eine Geradenschar mit Parameter im Stütz- und Richtungsvektor die Lage zu einer Ebene über das Skalarprodukt mit dem Normalenvektor unterscheiden (Gerade in der Ebene, parallel, schneidend) und den parameterabhängigen Schnittpunkt berechnen.",
     "2024-bebb-lk-A1.8a"),
    ("Wahrscheinlichkeit eines Fehlers aus der Vereinigung zweier unabhängiger Fehler berechnen", "Stochastik", "Unabhängigkeit",
     "Aus der Gesamtwahrscheinlichkeit für „Fehler A oder B“ und der Wahrscheinlichkeit von A die Wahrscheinlichkeit des unabhängigen Fehlers B berechnen (Additionssatz mit Produkt oder Gegenereignis).",
     "2024-bebb-lk-A1.9b"),
    ("Grenzverhalten einer Schar für x → +∞ nach dem Parametervorzeichen angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Für eine Schar (Polynom mal e-Funktion mit Parameter im Exponenten) das Verhalten der Funktionswerte für x → +∞ in Abhängigkeit vom Vorzeichen des Parameters angeben, einschließlich des Sonderfalls Parameter null.",
     "2024-bebb-lk-B2.1a"),
    ("Anzahl der Nullstellen einer Schar in Abhängigkeit vom Parameter über die Diskriminante ermitteln", "Analysis", "Funktionsscharen und Ortskurven",
     "Die Nullstellen einer Schar auf den quadratischen Faktor zurückführen und die Anzahl (keine, eine, zwei) über die Diskriminante nach Parameterbereichen angeben, mit Sonderfall linearer Faktor.",
     "2024-bebb-lk-B2.1b"),
    ("Mögliche Extremstellen aus der faktorisierten Ableitung ohne Rechnung angeben", "Analysis", "Kurvenuntersuchung",
     "Aus einer vorgegebenen, faktorisierten Ableitung die Nullstellen als mögliche Extremstellen ablesen (notwendige Bedingung, ohne hinreichende Prüfung).",
     "2024-bebb-lk-B2.1d"),
    ("Scharparameter für ein gleichseitiges Dreieck aus den Tangenten an Graph und Spiegelgraph und der y-Achse bestimmen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Tangenten an einen Scharkurve und an ihr Spiegelbild an der x-Achse in derselben Stelle aufstellen, das mit der y-Achse gebildete gleichschenklige Dreieck über Basis und Höhe als gleichseitig ansetzen und den Parameter daraus berechnen.",
     "2024-bebb-lk-B2.1f"),
    ("Rechenweg zur Tangente von einem Punkt an den Graphen erläutern und Aufgabenstellung formulieren", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Einen vorgelegten Rechenweg (Geradenansatz durch einen festen Punkt, Steigung gleich Ableitung an der Berührstelle, Gleichsetzen liefert die Berührstelle) als Bestimmung des Berührpunkts der Tangente von einem Punkt außerhalb an den Graphen erläutern und eine passende Aufgabenstellung formulieren.",
     "2024-bebb-lk-B2.1g"),
    ("Scharparameter für einen vorgegebenen Schnittwinkel des Graphen mit der y-Achse bestimmen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Aus der Bedingung, dass der Graph die y-Achse unter einem vorgegebenen Winkel schneidet, die Tangentensteigung an der Stelle 0 ablesen und den Parameter aus der Ableitung bestimmen.",
     "2024-bebb-lk-B2.1h"),
    ("Nullstellenfreiheit aller Scharkurven aus dem gemeinsamen Tiefpunktwert beurteilen", "Analysis", "Funktionsscharen und Ortskurven",
     "Den einzigen Extrempunkt jeder Scharkurve bestimmen, ihn als globales Minimum begründen und aus seinem positiven Funktionswert schließen, dass keine Funktion der Schar eine Nullstelle hat; Aussage beurteilen.",
     "2024-bebb-lk-B2.1i"),
    ("Integralwert: Integral über eine Summe aus e-Funktion und linearem Term gegen eine Schranke nachweisen", "Analysis", "Flächeninhalt durch Integration",
     "Ein bestimmtes Integral über eine Summe aus e-Term und linearem Term mit Stammfunktion berechnen und mit einer vorgegebenen Schranke vergleichen.",
     "2024-bebb-lk-B2.1j"),
    ("Fläche: Flächeninhalt zwischen Graph und x-Achse am Bild mit einem berechneten Integralwert vergleichen", "Analysis", "Flächeninhalt durch Integration",
     "Den Inhalt der Fläche zwischen einem abgebildeten Graphen und der x-Achse über einem Intervall aus der Abbildung abschätzen (Kästchen, Rechtecke) und mit einem zuvor berechneten Integralwert vergleichen.",
     "2024-bebb-lk-B2.1k"),
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
