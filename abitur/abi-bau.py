# -*- coding: utf-8 -*-
"""abi-bau.py – Gerüst für die Erfassung eines Hefts im Profil abi.
Version 0.13 · 18.09.2026 · gilt mit katalog-prompt.md v0.9, abitur-vokabular.md v1.6, abi.md v0.27, abitur-abgleich.py v0.24 und den Geltungsdateien abi-<zielprüfung>-geltung.md v1.0

Änderungen gegenüber 0.12 (Auftrag O, Punkt 3, 18.09.2026): KONFIG datei zeigt
auf hefte/abi/… – der Heftordner ist seit Auftrag N je Profil unterteilt
(abi-quellen.md § 8); Versionsbindung abi.md v0.27. Nur Text und ein Pfad,
keine Prüfung geändert – Selbstprüfung byteidentisch zu 0.12.

Änderungen gegenüber 0.11 (Auftrag G, Punkt 2, 17.09.2026): Versionsbindung
(abitur-abgleich.py v0.24); sonst unverändert.

Änderungen gegenüber 0.10 (Auftrag F, Punkt 2, 17.09.2026): Das Abgleichskript
heißt abitur-abgleich.py (bis 17.09.2026 abgleich.py); nur Text in Kopf,
Kommentaren und Meldungen, keine Prüfung geändert – Selbstprüfung
byteidentisch zu 0.10.

Je Heft werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles unter
„QUELLEN UND PRÜFUNG" und unter „AB HIER UNVERÄNDERT" bleibt unverändert.

Änderungen gegenüber 0.9 (Auftrag D „Namensschema, Erweiterbarkeit,
Begründungen", Teil 2, 17.09.2026): Die Geltung kommt nicht mehr aus einer
Tabelle in abitur-vokabular.md § 3, sondern je Zielprüfung aus einer eigenen
Datei abi-<zielprüfung>-geltung.md (§ 1, Tabelle „Thema | gilt", ja/nein;
§ 2 ausgeschlossene Aufgabenformen, § 3 Rechnerfassung – beide ohne
Skriptfilter). Welche Zielprüfungen gelten, sagt das Profil (abi.md § 6,
Zeile „Zielprüfungen: be-gk · be-lk · bb-gk · bb-ea"); ziele_von und die
Kennzahlen sind unverändert, die Datenstruktur (ZIELE, GELTUNG) auch –
Selbstprüfung und Berichte byteidentisch zu v0.9. Inhalt der Dateien
unverändert aus der Tabelle erzeugt (namensschema.md § 2).

Änderungen gegenüber 0.8 (Auftrag C, Teil 0, Entscheidung des Lehrers,
17.09.2026): Die Eichschwelle für Landeshefte ist ausgesetzt
(SCHWELLEN["eichung_mindestens"] = None): sie prüft die Erfassungsqualität am
amtlichen Anforderungsbereich, der bei Landesheften für die meisten Zeilen
fehlt; wo er vorliegt, trafen die Landesschätzungen 22 von 41 (54 %) gegen
94 % im Pool – gemessen wird dort die Schwierigkeit der Aufgabe, nicht die
Arbeit. Die Eichquote bleibt Kennzahl in Bericht und Selbstprüfung, ohne
Abbruch; für Poolstapel gilt weiter 85 % (iqb-bau.py). Maßstab der
Schätzung (Kern § 5 v0.7): niveau_geschaetzt ist genau dort messbar, wo
afb_amtlich gefüllt ist; leer heißt Schätzung ohne Maßstab, ohne eigene
Markierung. Dafür trägt jede Dublette afb_amtlich aus ihrer Poolzeile, auch
in den Heften bis 2018 (Lauf 22 hat die 21 Zeilen nachgezogen); die Regel
„afb_amtlich leer für Jahrgänge bis 2018" ist ersetzt durch „afb_amtlich
genau bei Dublette von:" – eine Landeszeile hat nie einen amtlichen Bereich.
Selbstprüfung und Heftbericht weisen die Zeilen ohne Maßstab aus.

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
abitur-abgleich.py sie auf „Dublette von:" (wortgleich) oder auf den neuen Verweis
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
über das Thema des Typs gemessen (Lauf 13 von abitur-abgleich.py hat den Bestand
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
  - SCHWELLEN: Qualitätsschranke im Skript („?", ersatzweise; Eichung bis v0.8).
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
Umbenennungen und Zusammenziehungen laufen über abitur-abgleich.py (Kern § 9).

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
    "jahr": "2025",
    "papier": "2025-bebb-lk",
    "datei": "hefte/abi/2025-bebb-lk.pdf",  # Stark-Band (Band zum Abitur 2027 LK, Jahrgang 2025), Bildscan der Aufgabenseiten, lokal (abi.md § 2)
    "seiten": 11,
    # Sollpunkte je Aufgabe aus der BE-Spalte; jede Aufgabe des Hefts muss hier
    # stehen (Vollständigkeit). Hilfsmittelfreier Teil: Pflichtaufgaben 1.1–1.4
    # (20 BE) und Wahlaufgaben 1.5–1.10 (30 BE angeboten, zwei zu bearbeiten:
    # Schlüssel seit 2025 LK 30 / 30 / 20 / 20); Teil B 2.1/2.2 Analysis je 30
    # zur Wahl, 3 Geometrie 20, 4 Stochastik 20. Angeboten 150, bearbeitet 100.
    # 2.1 und 2.2 haben je zwei Aufgabenteile, fortlaufend a–h bzw. a–i;
    # 4 hat zwei Aufgabenteile, fortlaufend a–f (Aufgabenteil 2 a–d = c–f).
    "soll": {"1.1": 5, "1.2": 5, "1.3": 5, "1.4": 5, "1.5": 5, "1.6": 5, "1.7": 5, "1.8": 5, "1.9": 5, "1.10": 5,
             "2.1": 30, "2.2": 30, "3": 20, "4": 20},
    "probe": False,
}

# ========================================= QUELLEN UND PRÜFUNG, NICHT ÄNDERN
KAT = "abi-katalog.csv"
TYP = "abitur-typen.csv"
VOKABULAR = "abitur-vokabular.md"
KERN = "../katalog-prompt.md"  # Umbau 2026-09-19: liegt in der Repo-Wurzel
PROFIL = "abi.md"                       # nennt die Zielprüfungen (§ 6)
GELTUNG_DATEI = "abi-{ziel}-geltung.md"  # eine Datei je Zielprüfung (namensschema.md § 2)
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
    # Eichung gegen den amtlichen Bereich: als Schranke ausgesetzt (None, v0.9,
    # Entscheidung des Lehrers 17.09.2026 – Landeshefte haben für die meisten
    # Zeilen keinen Maßstab); bleibt Kennzahl. Ein Wert wie 0.85 schaltet sie
    # wieder scharf, ab eichung_ab_zeilen eigenen gewerteten Zeilen; geerbte
    # Schätzungen der Dubletten zählen nicht (v0.8).
    "eichung_mindestens": None, "eichung_ab_zeilen": 10,
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
    Zielprüfungen aus dem Profil; bis v0.9 stand die Tabelle in abitur-vokabular.md § 3.
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
# Heft 2025-bebb-lk (Stark-Band zum Abitur 2027 LK, Jahrgang 2025; 11 Seiten
# Bildscan, nur Aufgabenseiten; Auftrag B, 17.09.2026). Pool 2025 erhöht (Teil A
# und Teil B WTR erfasst): der ganze hilfsmittelfreie Teil 1.1–1.10, 3 a–e und
# 4 a–f wortgleich – „Dublette von:“, aus den Poolzeilen erzeugt (dubletten.py).
# 2.1 Regenwasser ist die WTR-Fassung der Poolaufgabe Analysis MMS 1 (Stapel
# 2025-ea-B, MMS-Teil nicht erfasst): a, d, g, h wortgleich (Vormerkungen),
# c, e, f abgewandelt, b Landeszusatz. 2.2 Blutzucker: Landesaufgabe (in keiner
# Pooldatei 2025, auch nicht in den MMS-Dateien beider Niveaus).
# ---- Aufgabe 2.1 Regenwasser (Seiten 5–6, 30 BE)
SK21 = "Koordinatensystem x von 0 bis 5, y von 0 bis 200 (Schritt 20); Graph von r: von (0 | 0) zunächst flach, ab x ≈ 2,5 steil ansteigend zum Maximum bei etwa (3,7 | 187), dann steil fallend auf (5 | 0); grau unterlegtes Rechteck von x = 4 bis 5 und y = 0 bis 120; schraffiert die Fläche zwischen Rechteckoberkante und Graph – links von x ≈ 4,7 oberhalb des Rechtecks (Graph über 120), rechts davon innerhalb des Rechtecks (Graph unter 120)"
row(id="2025-bebb-lk-B2.1a", block="B", aufgabe="2.1", titel="Regenwasser (Aufgabenteil 1)", teilaufgabe="a", seite="5", punkte="3",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Genau zwei Nullstellen einer Schar aus der faktorisierten Form begründen und angeben", typ_neben="",
    stichwoerter="f_k(x) = 1/(2k) · x² · (x − 2k)²|Produkt null: x = 0 oder x = 2k|2k > 0, also zwei verschiedene Stellen (je doppelte Nullstelle)",
    voraussetzungen="Satz vom Nullprodukt|Parameter positiv",
    format="Begründung|Kurzantwort", operator="Begründen Sie|Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_k(x) = 1/(2k) · x² · (x − 2k)² = 1/(2k) x⁴ − 2x³ + 2kx², k ∈ IR⁺, definiert in IR; Graph G_k",
    gesucht="Begründung, dass f_k für jedes k genau zwei Nullstellen hat; die Nullstellen",
    verfahren="faktorisierte Form: Faktoren x² und (x − 2k)² null setzen",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="Nullstellen 0 und 2k (beide doppelt); wegen k > 0 sind es genau zwei verschiedene Stellen",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="am ausmultiplizierten Term x⁴-Gleichung lösen wollen; doppelte Nullstellen doppelt zählen",
    bemerkung="Poolaufgabe (nicht erfasst): 2025MerhoehtBAnalysisMMS1-1a. Reserve-Stapel 2025-ea-B (MMS-Fassung; das Heft ist die WTR-Fassung des Landes, Aufgabenteil 1 a wortgleich). Eigene Rechnung, mit sympy bestätigt.")
row(id="2025-bebb-lk-B2.1b", block="B", aufgabe="2.1", titel="Regenwasser (Aufgabenteil 1)", teilaufgabe="b", seite="5", punkte="3",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung mit Parameter in faktorisierter Form nachweisen", typ_neben="",
    stichwoerter="f_k'(x) = 2/k x³ − 6x² + 4kx|ausklammern: 2/k · x · (x² − 3kx + 2k²) = 2/k · x · (x − k)(x − 2k)|= 1/k · x · (x − 2k) · (2x − 2k)",
    voraussetzungen="Potenzregel mit Parameter|Faktorisieren eines quadratischen Terms mit Parameter",
    format="Rechnung", operator="Zeigen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_k wie in a; Behauptung f_k'(x) = 1/k · x · (x − 2k) · (2x − 2k)",
    gesucht="Nachweis der Ableitung in der angegebenen Form",
    verfahren="ausmultiplizierte Form ableiten und faktorisieren, oder die angegebene Form ausmultiplizieren und vergleichen",
    schritte="2", zahlenraum="ganz|Bruch", einheiten="", abhaengig_von="",
    ergebnis="f_k'(x) = 2/k x³ − 6x² + 4kx = 1/k · x · (x − 2k) · (2x − 2k)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Produktregel am faktorisierten Term ohne Zusammenfassen; Vorzeichen beim Faktorisieren",
    bemerkung="Landeszusatz zur Poolaufgabe Analysis MMS 1 (nicht im Pool; die MMS-Fassung braucht die Ableitung nicht). Typ wiederverwendet (2021-ea-A). Eigene Rechnung, mit sympy bestätigt.")
row(id="2025-bebb-lk-B2.1c", block="B", aufgabe="2.1", titel="Regenwasser (Aufgabenteil 1)", teilaufgabe="c", seite="5", punkte="5",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Abstand des Hochpunkts zu den Tiefpunkten einer Schar in Abhängigkeit vom Parameter berechnen", typ_neben="",
    stichwoerter="f_k' = 0 bei 0, k, 2k|Tiefpunkte (0 | 0) und (2k | 0) (Nullstellen, f_k ≥ 0)|Hochpunkt H(k | f_k(k)) = (k | k³/2)|Abstand √(k² + k⁶/4)",
    voraussetzungen="Extremstellen aus der faktorisierten Ableitung|Art über Vorzeichen oder f ≥ 0|Abstand zweier Punkte",
    format="Rechnung", operator="Berechnen Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_k und f_k' aus b; der Hochpunkt von G_k hat zu den beiden Tiefpunkten denselben Abstand",
    gesucht="dieser Abstand in Abhängigkeit von k",
    verfahren="Nullstellen von f_k' als Extremstellen, Hochpunkt (k | k³/2), Tiefpunkte auf der x-Achse; Abstand mit Pythagoras",
    schritte="4", zahlenraum="Wurzel|Potenz", einheiten="", abhaengig_von="2025-bebb-lk-B2.1b",
    ergebnis="Hochpunkt (k | k³/2), Tiefpunkte (0 | 0) und (2k | 0); Abstand d(k) = √(k² + k⁶/4)",
    zwischenergebnis="f_k(k) = k³/2", niveau_geschaetzt="II",
    fehlerquelle="Art der Extrempunkte nicht begründen; k³/2 falsch (1/(2k) · k² · k² = k³/2)",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2025MerhoehtBAnalysisMMS1-1b; der Pool fragt den Abstand ohne Hinweis (4 BE), das Heft mit Hinweis auf f_k' aus b und „in Abhängigkeit von k“ (5 BE). Reserve-Stapel 2025-ea-B. Enge Fassung: Standardverfahren mit Parameter, Art über f ≥ 0 – II. Eigene Rechnung, mit sympy bestätigt.")
row(id="2025-bebb-lk-B2.1d", block="B", aufgabe="2.1", titel="Regenwasser (Aufgabenteil 1)", teilaufgabe="d", seite="5", punkte="4",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral als Flächeninhalt für alle Scharkurven über das Vorzeichen des Terms beurteilen", typ_neben="",
    stichwoerter="f_k(x) = 1/(2k) · x² · (x − 2k)² ≥ 0 für alle x (Quadrate, k > 0)|Graph liegt über [−1; 1] nie unterhalb der x-Achse|Integral von −1 bis 1 = Summe der Flächenstücke (Trennung bei 0 und ggf. 2k ≤ 1)|Aussage richtig",
    voraussetzungen="Integral als Flächenbilanz|Vorzeichen eines Produkts von Quadraten",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Fläche zwischen G_k, der x-Achse und den Geraden x = −1 und x = 1, aus mehreren Flächenstücken; Aussage: für jeden Wert von k gibt ∫_{−1}^{1} f_k(x) dx den Inhalt der Fläche an; ohne Integralwert",
    gesucht="Beurteilung der Aussage",
    verfahren="Vorzeichen des Terms auf dem Intervall aus der faktorisierten Form",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="richtig: f_k(x) ≥ 0 für alle x, der Graph liegt nirgends unterhalb der x-Achse, also ist das Integral gleich der Summe der Inhalte aller Flächenstücke (Nullstellen 0 und für k ≤ 1/2 auch 2k trennen die Stücke)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="wegen der Nullstellen im Intervall Teilintegrale mit Beträgen verlangen; Vorzeichen nur an Beispielen prüfen",
    bemerkung="Poolaufgabe (nicht erfasst): 2025MerhoehtBAnalysisMMS1-1c. Reserve-Stapel 2025-ea-B (wortgleich). Enge Fassung: Deutung des Integrals als Bilanz mit einem Strukturargument – II. Eigene Überlegung, Vorzeichen mit sympy geprüft.")
row(id="2025-bebb-lk-B2.1e", block="B", aufgabe="2.1", titel="Regenwasser (Aufgabenteil 1)", teilaufgabe="e", seite="5", punkte="5",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Lösungsschritte zur Fläche zwischen zwei Scharkurven geometrisch deuten und Parameterungleichung untersuchen", typ_neben="",
    stichwoerter="I: f_k(x) = h_k(x) liefert die Schnittstellen −k, k, 2k der Graphen|II: Summe der Differenzintegrale = Inhalt der von G_k und dem Graphen von h_k eingeschlossenen Fläche (h_k oben auf [−k; k], f_k oben auf [k; 2k]) = 29/10 · k⁴|29/10 · k⁴ < k⁵ ⇔ k > 2,9: Aussage für k > 3 richtig",
    voraussetzungen="Schnittstellen durch Gleichsetzen|Fläche zwischen Graphen als Differenzintegral mit Wechsel der oberen Funktion|Potenzungleichung mit Parameter",
    format="Begründung|Rechnung", operator="Interpretieren Sie|Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="lang",
    gegeben="h_k(x) = k/2 · (x − 2k)²; Schritte I: f_k(x) = h_k(x) ⇔ x = −k ∨ x = k ∨ x = 2k; II: ∫_{−k}^{k} (h_k − f_k) dx + ∫_{k}^{2k} (f_k − h_k) dx = 29/10 · k⁴; Aussage: für k > 3 ist die Summe der beiden Integrale kleiner als k⁵",
    gesucht="geometrische Deutung beider Schritte in Bezug auf die Graphen; Untersuchung der Aussage",
    verfahren="I als Schnittstellen, II als Flächeninhalt zwischen den Graphen deuten; 29/10 · k⁴ < k⁵ nach k auflösen",
    schritte="3", zahlenraum="Bruch|Potenz", einheiten="", abhaengig_von="",
    ergebnis="I: die Graphen von f_k und h_k schneiden sich an den Stellen −k, k und 2k; II: der Term ist der Inhalt der von beiden Graphen zwischen −k und 2k eingeschlossenen Fläche (zwei Flächenstücke, bis k liegt h_k oben, danach f_k), er beträgt 29/10 · k⁴; die Aussage ist richtig, denn 29/10 · k⁴ < k⁵ ⇔ 29/10 < k, was für k > 3 gilt",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Ungleichung durch k⁴ teilen ohne k > 0 zu nennen; Wechsel der oberen Funktion bei x = k nicht erklären",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2025MerhoehtBAnalysisMMS1-1d; der Pool verlangt nur „Untersuchen Sie, ob … kleiner als k⁵“ (MMS-Rechnung), das Heft gibt die Schritte I und II vor und verlangt ihre Deutung, dann die Untersuchung (je 5 BE). Reserve-Stapel 2025-ea-B. Enge Fassung: vorgelegte Schritte deuten und eine Standardungleichung lösen – II. Eigene Rechnung, mit sympy bestätigt (Schnittstellen und 29/10 · k⁴).")
row(id="2025-bebb-lk-B2.1f", block="B", aufgabe="2.1", titel="Regenwasser (Aufgabenteil 2 a)", teilaufgabe="f", seite="6", punkte="3",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Zeitpunkt und Größe der maximalen Rate über die Ableitung der Ratenfunktion berechnen", typ_neben="",
    stichwoerter="r'(x) = 1/5 · x · (x − 5) · (x² − x − 10) · e^x = 0|zwischen 2 und 4 nur x² − x − 10 = 0: x = (1 + √41)/2 ≈ 3,70|Vorzeichenwechsel + nach − (oder Aufgabentext: genau ein Maximum)",
    voraussetzungen="notwendige Bedingung an vorgegebener Ableitung|quadratische Gleichung",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Regenwasser/Auffangbecken", textumfang="mittel",
    gegeben="r(x) = e^x · f_{2,5}(x) = 1/5 · x² · (x − 5)² · e^x für 0 ≤ x ≤ 5 (Zuflussrate in m³/h, x in Stunden); r'(x) = 1/5 · x · (x − 5) · (x² − x − 10) · e^x; zu genau einem Zeitpunkt zwischen zwei und vier Stunden ist die Zuflussrate am größten",
    gesucht="dieser Zeitpunkt",
    verfahren="Nullstellen von r' im Intervall ]2; 4[ über den quadratischen Faktor",
    schritte="2", zahlenraum="Wurzel|dezimal", einheiten="h", abhaengig_von="",
    ergebnis="x = (1 + √41)/2 ≈ 3,70, also etwa 3 Stunden 42 Minuten nach Beginn (Rate dort ≈ 187 m³/h)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Nullstellen 0 und 5 der Ableitung als Kandidaten nehmen; negative Lösung −2,70 nicht ausschließen",
    bemerkung="Poolaufgabe (nicht erfasst, abgewandelt): 2025MerhoehtBAnalysisMMS1-2a; der Pool verlangt größte und kleinste Zuflussrate ohne Ableitung (MMS, 4 BE), das Heft gibt r' vor und fragt nur den Zeitpunkt des Maximums zwischen 2 und 4 (3 BE). Reserve-Stapel 2025-ea-B. Typ wiederverwendet (2026-ga-B), hier nur der Zeitpunkt. Eigene Rechnung, mit sympy bestätigt.")
row(id="2025-bebb-lk-B2.1g", block="B", aufgabe="2.1", titel="Regenwasser (Aufgabenteil 2 b)", teilaufgabe="g", seite="6", punkte="4",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integralabschätzung über ein Rechteck und Flächenvergleich am Graphen erläutern und im Sachzusammenhang deuten", typ_neben="",
    stichwoerter="Rechteck [4; 5] × [0; 120] hat den Inhalt 120|Integral = Rechteck + Fläche über der Oberkante (links, bis x ≈ 4,7) − Fläche unter der Oberkante ohne Graph (rechts)|schraffierte Überfläche sichtbar kleiner als schraffierte Fehlfläche ⇒ Integral < 120|Deutung: in der fünften Stunde fließen weniger als 120 m³ zu",
    voraussetzungen="Integral als Fläche unter dem Graphen|Flächenvergleich am Bild|Integral einer Rate als Menge",
    format="Begründung", operator="Erläutern Sie|Interpretieren Sie", antwort="Text",
    material="Koordinatensystem", skizze=SK21, kontext="Regenwasser/Auffangbecken", textumfang="mittel",
    gegeben="Abbildung des Graphen von r mit Rechteck und Schraffuren; Aussage ∫_4^5 r(x) dx < 120",
    gesucht="Erläuterung, wie die Eintragungen die Aussage begründen; Deutung im Sachzusammenhang",
    verfahren="Rechteckinhalt 120 mit Über- und Fehlfläche vergleichen",
    schritte="2", zahlenraum="ganz", einheiten="m³", abhaengig_von="",
    ergebnis="Die Fläche unter dem Graphen über [4; 5] ist das Rechteck (Inhalt 120) plus dem schraffierten Stück oberhalb der Oberkante minus dem schraffierten Stück innerhalb des Rechtecks über dem Graphen; das zweite ist erkennbar größer, also ist das Integral kleiner als 120. Deutung: zwischen der vierten und fünften Stunde fließen weniger als 120 m³ Regenwasser in das Becken (eigene Rechnung ≈ 88 m³)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="das Rechteck als Obersumme ansehen, obwohl der Graph links über 120 liegt; Deutung als Füllstand statt als Zuflussmenge",
    bemerkung="Poolaufgabe (nicht erfasst): 2025MerhoehtBAnalysisMMS1-2c. Reserve-Stapel 2025-ea-B (wortgleich; im Pool Teilaufgabe 2 c). Enge Fassung: Flächenbilanz am Bild und Deutung – II. Eigene Überlegung, Integral mit sympy geprüft (87,97).")
row(id="2025-bebb-lk-B2.1h", block="B", aufgabe="2.1", titel="Regenwasser (Aufgabenteil 2 c)", teilaufgabe="h", seite="6", punkte="3",
    leitidee="Analysis", thema="Rekonstruktion von Beständen",
    typ="Term für einen Bestand aus einer Rate über ein Integral angeben", typ_neben="",
    stichwoerter="Anfangsbestand 186|Zufluss bis t: ∫_0^t r(x) dx|Abpumpen ab 3,5 mit konstanter Rate p: p · (t − 3,5)|V(t) = 186 + ∫_0^t r(x) dx − p · (t − 3,5)",
    voraussetzungen="Integral einer Rate als Menge|lineare Abnahme bei konstanter Rate|Zeitverschiebung",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Regenwasser/Auffangbecken", textumfang="mittel",
    gegeben="Becken zu Beginn mit 186 m³ gefüllt; nach 3,5 Stunden wird eine Pumpe eingeschaltet, die bis zum Ende des Zeitraums mit konstanter Rate abpumpt; Zufluss weiterhin r",
    gesucht="Term für das Wasservolumen zu einem beliebigen Zeitpunkt t nach dem Einschalten der Pumpe",
    verfahren="Anfangswert plus Integral der Zuflussrate minus Pumpmenge seit 3,5 h",
    schritte="1", zahlenraum="dezimal", einheiten="m³|m³/h", abhaengig_von="",
    ergebnis="V(t) = 186 + ∫_0^t r(x) dx − p · (t − 3,5) für 3,5 ≤ t ≤ 5, p die konstante Pumprate in m³/h",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Pumpmenge als p · t ansetzen; Integral erst ab 3,5 laufen lassen",
    bemerkung="Poolaufgabe (nicht erfasst): 2025MerhoehtBAnalysisMMS1-2d. Reserve-Stapel 2025-ea-B (wortgleich; im Pool Teilaufgabe 2 d). Typ wiederverwendet (2021-ea-A), hier mit zusätzlichem linearem Abpumpterm. Eigene Überlegung.")
# ---- Aufgabe 2.2 Blutzucker (Seiten 7–8, 30 BE), Landesaufgabe
SK22A = "Abb. 1: Koordinatensystem x von −4 bis 3, y von −3 bis 3; Graph von f_0'(x) = (x² − 2x) · e^x: von links nahe der x-Achse ansteigend zum Hochpunkt bei etwa (−1,4 | 1,2), fällt durch (0 | 0) zum Tiefpunkt bei etwa (1,4 | −3,4), steigt steil durch (2 | 0)"
SK22C = "Abb. 2: Koordinatensystem t von −0,5 bis 4 (Schritt 0,5), y von −45 bis 20 (Schritt 5); Graph von h'': beginnt bei t = 0 oberhalb von 20, fällt steil durch die t-Achse bei t ≈ 0,6 zum Tiefpunkt bei etwa (1,4 | −44), steigt wieder und schneidet die t-Achse bei t ≈ 3,4"
row(id="2025-bebb-lk-B2.2a", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 1)", teilaufgabe="a", seite="7", punkte="2",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Stellen mit vorgegebenem Anstieg und Wendestelle am Graphen der Ableitung ablesen", typ_neben="",
    stichwoerter="f_0' = 1 an drei Stellen: x ≈ −2,3, x ≈ −0,8, x ≈ 2,1|Wendestelle von f_0 = Extremstelle von f_0': x ≈ −1,4 (oder 1,4)",
    voraussetzungen="Ableitungswert als Anstieg|Wendestelle als Extremstelle der Ableitung",
    format="Kurzantwort", operator="Geben Sie an", antwort="Zahl",
    material="Koordinatensystem", skizze=SK22A, kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = (x − 2)² · e^(x + a), a ∈ IR; Abb. 1 mit dem Graphen von f_0'(x) = (x² − 2x) · e^x",
    gesucht="die drei Stellen mit Anstieg 1 von f_0; eine Wendestelle von f_0, näherungsweise",
    verfahren="waagerechte Linie y = 1 mit dem Ableitungsgraphen schneiden; Extremstelle des Ableitungsgraphen ablesen",
    schritte="1", zahlenraum="dezimal|negativ", einheiten="", abhaengig_von="",
    ergebnis="x ≈ −2,3, x ≈ −0,8, x ≈ 2,1; Wendestelle x ≈ −1,4 (ebenso x ≈ 1,4)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Nullstellen des Ableitungsgraphen als Wendestellen lesen; nur zwei Stellen mit Anstieg 1 finden",
    bemerkung="Landesaufgabe (in keiner Pooldatei 2025). Eigene Rechnung, mit sympy bestätigt (−2,27, −0,79, 2,06; Wendestellen ±√2).")
row(id="2025-bebb-lk-B2.2b", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 1)", teilaufgabe="b", seite="7", punkte="2",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Integral der Ableitung als Differenz von Funktionswerten berechnen", typ_neben="",
    stichwoerter="∫_0^2 f_0'(x) dx = f_0(2) − f_0(0)|f_0(2) = 0, f_0(0) = 4 · e⁰ = 4|Wert −4",
    voraussetzungen="Hauptsatz: f_0 ist Stammfunktion von f_0'",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_0(x) = (x − 2)² · e^x und f_0' wie in a",
    gesucht="∫_0^2 f_0'(x) dx",
    verfahren="Hauptsatz mit f_0 als Stammfunktion",
    schritte="1", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="f_0(2) − f_0(0) = 0 − 4 = −4",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="f_0' integrieren wollen statt f_0 einzusetzen; Vorzeichen",
    bemerkung="Landesaufgabe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2025-bebb-lk-B2.2c", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 1)", teilaufgabe="c", seite="7", punkte="3",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Integrationsgrenzen mit Integral null über die zweite Ableitung am Graphen der Ableitung angeben", typ_neben="",
    stichwoerter="∫_c^d f_0''(x) dx = f_0'(d) − f_0'(c)|null genau für f_0'(c) = f_0'(d)|z. B. c = 0, d = 2 (beide Nullstellen von f_0') oder c ≈ −2,3, d ≈ −0,8 (beide Wert 1)",
    voraussetzungen="Hauptsatz mit f_0' als Stammfunktion von f_0''|Ablesen gleicher Werte am Graphen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=SK22A, kontext="ohne", textumfang="kurz",
    gegeben="Abb. 1 (Graph von f_0'); gesucht c ≠ d mit ∫_c^d f_0''(x) dx = 0",
    gesucht="näherungsweise Werte für c und d mit Begründung",
    verfahren="Integral über f_0'' als Differenz zweier Werte von f_0' deuten und zwei Stellen mit gleichem Wert ablesen",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="", abhaengig_von="",
    ergebnis="z. B. c = 0 und d = 2, da f_0'(0) = f_0'(2) = 0 und das Integral gleich f_0'(d) − f_0'(c) ist (ebenso jedes Paar mit gleichem Ableitungswert)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="f_0'' aufstellen und integrieren wollen; Flächenbilanz von f_0' statt Werte von f_0' betrachten",
    bemerkung="Landesaufgabe. Enge Fassung: Hauptsatz auf die zweite Ableitung übertragen und am Bild lesen – II. Eigene Rechnung, mit sympy bestätigt.")
row(id="2025-bebb-lk-B2.2d", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 1)", teilaufgabe="d", seite="7", punkte="2",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Schnittstelle von Graph und Ableitungsgraph nachweisen", typ_neben="",
    stichwoerter="f_0(2) = 0 · e² = 0|f_0'(2) = (4 − 4) · e² = 0|gemeinsamer Punkt (2 | 0)",
    voraussetzungen="Einsetzen in beide Terme",
    format="Rechnung", operator="Zeigen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f_0(x) = (x − 2)² · e^x, f_0'(x) = (x² − 2x) · e^x",
    gesucht="Nachweis, dass sich die Graphen von f_0' und f_0 an der Stelle 2 schneiden",
    verfahren="beide Funktionswerte an der Stelle 2 berechnen",
    schritte="1", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_0(2) = 0 = f_0'(2), gemeinsamer Punkt (2 | 0)",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Gleichung f_0 = f_0' allgemein lösen wollen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2022-bebb-gk). Eigene Rechnung, mit sympy bestätigt.")
row(id="2025-bebb-lk-B2.2e", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 1)", teilaufgabe="e", seite="7", punkte="3",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Ableitung einer Schar als Vielfaches der Ableitung eines Scharmitglieds nachweisen", typ_neben="",
    stichwoerter="f_a(x) = (x − 2)² · e^x · e^a = e^a · f_0(x)|f_a'(x) = e^a · f_0'(x)|alternativ Produktregel: (2(x − 2) + (x − 2)²) · e^(x + a) = (x² − 2x) · e^x · e^a",
    voraussetzungen="Potenzgesetz e^(x + a) = e^x · e^a|konstanter Faktor beim Ableiten oder Produktregel",
    format="Rechnung", operator="Weisen Sie nach", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Schar f_a(x) = (x − 2)² · e^(x + a); Behauptung f_a'(x) = f_0'(x) · e^a",
    gesucht="Nachweis der Beziehung",
    verfahren="e^a als konstanten Faktor abspalten oder Produktregel mit Vergleich",
    schritte="2", zahlenraum="ganz", einheiten="", abhaengig_von="",
    ergebnis="f_a'(x) = e^a · (x² − 2x) · e^x = f_0'(x) · e^a",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Kettenregel für e^(x + a) mit innerer Ableitung ungleich 1; Produktregel ohne Zusammenfassen",
    bemerkung="Landesaufgabe. Enge Fassung: Standardrechnung mit Parameter im Exponenten – II. Eigene Rechnung, mit sympy bestätigt.")
row(id="2025-bebb-lk-B2.2f", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 1)", teilaufgabe="f", seite="7", punkte="5",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Extrempunkte aller Scharkurven aus dem Ableitungsgraphen eines Scharmitglieds ohne Rechnung begründen", typ_neben="",
    stichwoerter="f_a' = e^a · f_0' mit e^a > 0: gleiche Nullstellen und gleiche Vorzeichen wie f_0'|Abb. 1: f_0' > 0 für x < 0, < 0 auf ]0; 2[, > 0 für x > 2, sonst keine Nullstellen|bei 0 Wechsel + nach −: Hochpunkt H(0 | f_a(0)) = (0 | 4e^a); bei 2 Wechsel − nach +: Tiefpunkt T(2 | 0)|genau je einer",
    voraussetzungen="Vorzeichenwechselkriterium|positiver Faktor erhält Vorzeichen|Ablesen am Ableitungsgraphen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="Koordinatensystem", skizze=SK22A, kontext="ohne", textumfang="mittel",
    gegeben="Beziehung aus e und Abb. 1; Aussage: alle Graphen von f_a haben genau einen Tiefpunkt T(2 | f_a(2)) und genau einen Hochpunkt H(0 | f_a(0)); ohne Rechnung",
    gesucht="Begründung, dass die Aussage wahr ist",
    verfahren="Vorzeichenverlauf von f_0' aus der Abbildung auf f_a' übertragen, Vorzeichenwechsel an den Nullstellen 0 und 2",
    schritte="3", zahlenraum="ganz", einheiten="", abhaengig_von="2025-bebb-lk-B2.2e",
    ergebnis="wegen f_a' = e^a · f_0' und e^a > 0 hat f_a' genau die Nullstellen 0 und 2 mit denselben Vorzeichenwechseln wie f_0' in Abb. 1 (+ nach − bei 0, − nach + bei 2); daher hat jeder Graph genau den Hochpunkt H(0 | 4e^a) und den Tiefpunkt T(2 | 0)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Koordinaten der Punkte nicht als Funktionswerte von f_a angeben; die Ausschließlichkeit („genau einen“) nicht über das Fehlen weiterer Nullstellen begründen",
    bemerkung="Landesaufgabe. Enge Fassung: Vorzeichenwechselkriterium am Bild mit einem Übertragungsargument (positiver Faktor) – II. Eigene Rechnung, mit sympy bestätigt (Extremstellen 0 und 2, f_a(0) = 4e^a).")
row(id="2025-bebb-lk-B2.2g", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 2 a)", teilaufgabe="g", seite="8", punkte="7",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Hochpunkt eines Produkts aus Polynom und e-Funktion berechnen", typ_neben="",
    stichwoerter="h'(t) = (80t − 40t²) · e^(1 − t) = 40t(2 − t) · e^(1 − t)|h'(t) = 0 ⇒ t = 2 (t = 0 ist Rand)|h''(2) = −80/e < 0: Maximum|h(2) = 160/e + 90 ≈ 148,9|Rand: h(0) = 90, h(4) ≈ 121,9",
    voraussetzungen="Produktregel mit e^(1 − t)|hinreichende Bedingung mit vorgegebener zweiter Ableitung|Randwerte eines Intervalls",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Medizin / Blutzucker", textumfang="mittel",
    gegeben="h(t) = 40t² · e^(1 − t) + 90 für 0 ≤ t ≤ 4 (Blutzuckerwert in mg/dl, t Stunden nach der Nahrungsaufnahme); Hinweis: h''(t) = (40t² − 160t + 80) · e^(1 − t) ohne Nachweis verwendbar",
    gesucht="maximaler Blutzuckerwert des Patienten",
    verfahren="h' aufstellen und null setzen, Art über h'', Wert berechnen und mit den Randwerten vergleichen",
    schritte="4", zahlenraum="dezimal|Potenz", einheiten="mg/dl|h", abhaengig_von="",
    ergebnis="Maximum bei t = 2 mit h(2) = 160/e + 90 ≈ 148,9 mg/dl (Randwerte 90 und ≈ 121,9 kleiner)",
    zwischenergebnis="h'(t) = 40t(2 − t) · e^(1 − t); h''(2) ≈ −29,4", niveau_geschaetzt="II",
    fehlerquelle="innere Ableitung −1 bei e^(1 − t) vergessen; Randwerte nicht prüfen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2025-ga-B), hier im Sachzusammenhang mit Randvergleich. Eigene Rechnung, mit sympy bestätigt (148,86).")
row(id="2025-bebb-lk-B2.2h", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 2 b)", teilaufgabe="h", seite="8", punkte="3",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate aus dem Funktionsterm im Sachzusammenhang berechnen", typ_neben="",
    stichwoerter="h(4) ≈ 121,86, h(2) ≈ 148,86|1/2 · (h(4) − h(2)) ≈ −13,5|mittlere Änderungsrate zwischen der zweiten und der vierten Stunde",
    voraussetzungen="Differenzenquotient|Deutung mit Einheit",
    format="Rechnung|Begründung", operator="Berechnen Sie|Interpretieren Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Medizin / Blutzucker", textumfang="kurz",
    gegeben="h wie in g; Term 1/2 · (h(4) − h(2))",
    gesucht="Wert des Terms und Deutung im Sachzusammenhang",
    verfahren="Funktionswerte einsetzen, als Differenzenquotient über [2; 4] deuten",
    schritte="2", zahlenraum="dezimal|negativ", einheiten="mg/dl|h", abhaengig_von="",
    ergebnis="≈ −13,5: zwischen der zweiten und der vierten Stunde nach der Nahrungsaufnahme sinkt der Blutzuckerwert im Mittel um 13,5 mg/dl je Stunde",
    zwischenergebnis="", niveau_geschaetzt="I",
    fehlerquelle="Term als momentane Änderungsrate deuten; Einheit weglassen",
    bemerkung="Landesaufgabe. Typ wiederverwendet (2017-ea-A). Eigene Rechnung, mit sympy bestätigt (−13,50).")
row(id="2025-bebb-lk-B2.2i", block="B", aufgabe="2.2", titel="Blutzucker (Aufgabenteil 2 c)", teilaufgabe="i", seite="8", punkte="3",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Zeitpunkt der maximalen Änderungsrate am Graphen der zweiten Ableitung ablesen und begründen", typ_neben="",
    stichwoerter="Zuwachsrate = h'; maximal, wo h'' von + nach − wechselt|Abb. 2: Nullstelle mit Wechsel + nach − bei t ≈ 0,6|bei t ≈ 3,4 Wechsel − nach +: Minimum von h'",
    voraussetzungen="h' als Änderungsrate|Extremum von h' über Vorzeichenwechsel von h''",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=SK22C, kontext="Medizin / Blutzucker", textumfang="kurz",
    gegeben="Abb. 2 mit dem Graphen von h''",
    gesucht="näherungsweise der Zeitpunkt der maximalen Zuwachsrate des Blutzuckerwerts, mit Begründung",
    verfahren="Nullstelle von h'' mit Vorzeichenwechsel von + nach − ablesen",
    schritte="1", zahlenraum="dezimal", einheiten="h", abhaengig_von="",
    ergebnis="t ≈ 0,6 h (etwa 35 Minuten nach der Nahrungsaufnahme): dort wechselt h'' von + nach −, h' hat ein Maximum (exakt 2 − √2 ≈ 0,59)",
    zwischenergebnis="", niveau_geschaetzt="II",
    fehlerquelle="Tiefpunkt von h'' (t ≈ 1,4) als Zeitpunkt nehmen; die zweite Nullstelle 3,4 (Minimum der Rate) wählen",
    bemerkung="Landesaufgabe. Enge Fassung: zwei Ableitungsstufen am Bild verketten – II. Eigene Rechnung, mit sympy bestätigt (2 − √2).")
# ---- Dubletten aus dem Pool (dubletten.py, map_2025lk.py)
row(id="2025-bebb-lk-A1.1a", block="A", aufgabe="1.1", titel="Analysis (1.1)", teilaufgabe="a", seite="1", punkte="2", afb_amtlich="I",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Extrempunkt an vorgegebener Stelle nachweisen",
    typ_neben="",
    stichwoerter="f'(x) = 3/4 x² − 3|f'(2) = 0|f''(2) ≠ 0 vorgegeben|Extremstelle 2",
    voraussetzungen="Potenzregel|notwendige und hinreichende Bedingung für Extremstellen",
    format="Rechnung",
    operator="Zeigen Sie",
    antwort="Text",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit x-Achse von −10 bis 10 und y-Achse von −7 bis 4, Gitter; Graph II (beschriftet oben rechts): W-Form mit Hochpunkt (0; 3), Nullstellen bei etwa ±1,5 und ±4,7, Tiefpunkten bei etwa (±3,5; −6), außerhalb von ±5 steil steigend; Graph I (beschriftet unten rechts): flache Welle mit Hochpunkt (0; 1), Nullstellen bei etwa ±2,5, Tiefpunkten bei etwa (±8; −7), an den Rändern wieder steigend",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = 1/4 x³ − 3x, definiert in IR; es gilt f''(2) ≠ 0",
    gesucht="Nachweis, dass 2 eine Extremstelle von f ist",
    verfahren="f' bilden und f'(2) = 0 zeigen; zusammen mit f''(2) ≠ 0 folgt die Extremstelle",
    schritte="2",
    zahlenraum="Bruch|Potenz",
    einheiten="",
    ergebnis="f'(x) = 3/4 x² − 3; f'(2) = 0",
    zwischenergebnis="f''(2) = 3",
    niveau_geschaetzt="I",
    fehlerquelle="f(2) = −4 berechnen und als Nachweis ansehen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAnalysis12-a. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.2 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.1b", block="A", aufgabe="1.1", titel="Analysis (1.1)", teilaufgabe="b", seite="1", punkte="3", afb_amtlich="II",
    leitidee="Analysis", thema="Ableitungsgraph und Funktionsgraph",
    typ="Graphen von Funktion und Ableitung einander zuordnen",
    typ_neben="",
    stichwoerter="Graph II|Extremstelle 2 von f ist Wendestelle von F|Nullstellen von f sind Extremstellen von F|Nullstellen 0 und ±2√3 ≈ ±3,46",
    voraussetzungen="F' = f|Extremstellen von f als Wendestellen von F deuten|Nullstellen einer kubischen Funktion",
    format="Kurzantwort|Begründung",
    operator="Geben Sie an|Begründen Sie",
    antwort="Text",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit x-Achse von −10 bis 10 und y-Achse von −7 bis 4, Gitter; Graph II (beschriftet oben rechts): W-Form mit Hochpunkt (0; 3), Nullstellen bei etwa ±1,5 und ±4,7, Tiefpunkten bei etwa (±3,5; −6), außerhalb von ±5 steil steigend; Graph I (beschriftet unten rechts): flache Welle mit Hochpunkt (0; 1), Nullstellen bei etwa ±2,5, Tiefpunkten bei etwa (±8; −7), an den Rändern wieder steigend",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = 1/4 x³ − 3x mit der Extremstelle 2; zwei abgebildete Graphen I und II, einer davon ist der Graph einer Stammfunktion von f",
    gesucht="dieser Graph mit Begründung",
    verfahren="der Graph jeder Stammfunktion F hat an der Extremstelle 2 von f einen Wendepunkt; Graph II wendet bei 2, Graph I nicht (oder: F hat Extremstellen bei den Nullstellen 0 und ±3,46 von f, das passt nur zu Graph II)",
    schritte="2",
    zahlenraum="ganz|negativ|Wurzel",
    einheiten="",
    ergebnis="Graph II; der Graph jeder Stammfunktion F von f hat im Punkt (2; F(2)) einen Wendepunkt",
    zwischenergebnis="Nullstellen von f: 0, −2√3, 2√3|Tiefpunkte von Graph II bei etwa ±3,5",
    niveau_geschaetzt="II",
    fehlerquelle="den Graphen von f selbst suchen und Graph I wegen des Hochpunkts bei 0 wählen",
    abhaengig_von="2025-bebb-lk-A1.1a",
    bemerkung="Dublette von: 2025MerhoehtAAnalysis12-b. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.2 b (Graphen I und II wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.2a", block="A", aufgabe="1.2", titel="Analysis (1.2)", teilaufgabe="a", seite="1", punkte="1", afb_amtlich="I|II",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Integralwert: Integral mit Wert null am Graphen begründen",
    typ_neben="",
    stichwoerter="Integral von 0 bis π über 3 cos x|Flächen über und unter der Achse gleich groß|Wert 0",
    voraussetzungen="Integral als orientierten Flächeninhalt deuten|Symmetrie des Kosinus zu π/2",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit x-Achse von −π bis 2π (Markierungen −π, −π/2, 0, π/2, π, 3π/2, 2π) und y-Achse von −3 bis 3, Gitter; Graph von f(x) = 3 · cos(x): Hochpunkte (0; 3) und (2π; 3), Tiefpunkte (−π; −3) und (π; −3), Nullstellen bei ±π/2 und 3π/2",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = 3 · cos(x), definiert in IR, Graph in der Abbildung; Integral von 0 bis π über f(x) dx",
    gesucht="Wert des Integrals",
    verfahren="am Graphen: die Fläche über der x-Achse in [0; π/2] ist so groß wie die darunter in [π/2; π], die orientierten Inhalte heben sich auf",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="0",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="den Flächeninhalt 6 statt des Integralwerts angeben",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAnalysis13-a. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.3 a (Abbildung wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.2b", block="A", aufgabe="1.2", titel="Analysis (1.2)", teilaufgabe="b", seite="1", punkte="4", afb_amtlich="I|II",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Parameter einer Linearkombination aus Funktion und Gerade aus zwei Punkten bestimmen",
    typ_neben="",
    stichwoerter="g(x) = a · f(x) + b · x|g(0) = −3|g(π/2) = 3π/4|cos(0) = 1, cos(π/2) = 0|a = −1, b = 3/2",
    voraussetzungen="Punkte in den Term einsetzen|Werte des Kosinus an 0 und π/2|Gleichung mit π lösen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit x-Achse von −π bis 2π (Markierungen −π, −π/2, 0, π/2, π, 3π/2, 2π) und y-Achse von −3 bis 3, Gitter; Graph von f(x) = 3 · cos(x): Hochpunkte (0; 3) und (2π; 3), Tiefpunkte (−π; −3) und (π; −3), Nullstellen bei ±π/2 und 3π/2",
    kontext="ohne",
    textumfang="mittel",
    gegeben="f(x) = 3 · cos(x); g(x) = a · f(x) + b · x mit reellen a und b; die Punkte (0; −3) und (π/2; 3π/4) liegen auf dem Graphen von g",
    gesucht="a und b",
    verfahren="beide Punkte einsetzen: 3a · cos(0) + b · 0 = −3 liefert a; 3a · cos(π/2) + b · π/2 = 3π/4 liefert b",
    schritte="2",
    zahlenraum="Bruch|negativ",
    einheiten="",
    ergebnis="3a · cos(0) + b · 0 = −3, also a = −1; 3a · cos(π/2) + b · π/2 = 3π/4, also b = 3/2",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="cos(π/2) mit 1 oder cos(0) mit 0 verwechseln",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAnalysis13-b. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 1.3 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.3a", block="A", aufgabe="1.3", titel="Analytische Geometrie (1.3)", teilaufgabe="a", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Volumen eines Teilkörpers eines Würfels berechnen",
    typ_neben="",
    stichwoerter="Ebene K durch A, B und Mittelpunkt von FG|Teilkörper ist ein Dreiecksprisma|Grundfläche 1/2 · 2 · 4 = 4, Länge 4|Viertel des Würfels|Volumen 16",
    voraussetzungen="Schnittkörper im Schrägbild erkennen|Prismenvolumen|Mittelpunkt einer Kante",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild eines Würfels ABCDEFGH der Kantenlänge 4 im Koordinatensystem: A im Ursprung, B(4; 0; 0) auf der x-Achse (nach vorn links), D(0; 4; 0) auf der y-Achse (nach rechts), E(0; 0; 4) auf der z-Achse, C(4; 4; 0), F(4; 0; 4), G(4; 4; 4), H(0; 4; 4); Ebene K als graues Viereck durch A, B und die Mittelpunkte (4; 2; 4) von FG und (0; 2; 4) von EH; verdeckte Kanten gestrichelt, Achsen x, y, z beschriftet",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Würfel ABCDEFGH der Kantenlänge 4, drei Seitenflächen in den Koordinatenebenen; A(0; 0; 0), B(4; 0; 0); Ebene K enthält A, B und den Mittelpunkt der Kante FG; K teilt den Würfel in zwei Teilkörper",
    gesucht="Volumen des kleineren Teilkörpers",
    verfahren="der kleinere Teilkörper ist ein Prisma mit dreieckiger Grundfläche (Dreieck A, E, Mittelpunkt von EH in der Ebene x = 0) und Länge 4; Grundfläche 1/2 · 2 · 4 = 4",
    schritte="2",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="Volumen 1/4 · 4³ = 16",
    zwischenergebnis="Mittelpunkt von FG: (4; 2; 4)|K: z = 2y",
    niveau_geschaetzt="I",
    fehlerquelle="den Teilkörper als halben Würfel (32) ansehen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAGLAA212-a. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 1.2 a (Würfelbild wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.3b", block="A", aufgabe="1.3", titel="Analytische Geometrie (1.3)", teilaufgabe="b", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Schnittfigur einer Ebene mit einem Würfel einzeichnen",
    typ_neben="Schnittgerade zweier Ebenen aus dem Schrägbild angeben",
    stichwoerter="Ebene L durch E, F und Mittelpunkt (4; 2; 0) von BC|Schnittfigur Rechteck E, F, (4; 2; 0), (0; 2; 0)|K und L enthalten Geraden parallel zur x-Achse|Schnittgerade durch (0; 1; 2) mit Richtung (1; 0; 0)",
    voraussetzungen="Schnittfigur über parallele Schnittkanten konstruieren|Schnittgerade zweier Ebenen aus zwei gemeinsamen Punkten oder aus Symmetrie|Geradengleichung in Parameterform",
    format="Zeichnen|Kurzantwort",
    operator="Zeichnen Sie|Geben Sie an",
    antwort="Grafik|Term",
    material="Körper",
    skizze="Schrägbild eines Würfels ABCDEFGH der Kantenlänge 4 im Koordinatensystem: A im Ursprung, B(4; 0; 0) auf der x-Achse (nach vorn links), D(0; 4; 0) auf der y-Achse (nach rechts), E(0; 0; 4) auf der z-Achse, C(4; 4; 0), F(4; 0; 4), G(4; 4; 4), H(0; 4; 4); Ebene K als graues Viereck durch A, B und die Mittelpunkte (4; 2; 4) von FG und (0; 2; 4) von EH; verdeckte Kanten gestrichelt, Achsen x, y, z beschriftet",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Würfel ABCDEFGH der Kantenlänge 4 wie in der Abbildung, Ebene K durch A, B und den Mittelpunkt von FG; Ebene L enthält E(0; 0; 4), F(4; 0; 4) und den Mittelpunkt (4; 2; 0) der Kante BC",
    gesucht="Schnittfigur von L mit dem Würfel in der Abbildung|Gleichung der Schnittgeraden von K und L",
    verfahren="L schneidet die Flächen x = 4 und x = 0 in parallelen Strecken von F bzw. E zu den Kantenmitten (4; 2; 0) bzw. (0; 2; 0), die Schnittfigur ist ein Rechteck; beide Ebenen enthalten Geraden in x-Richtung, die Schnittgerade verläuft durch den Schnittpunkt (0; 1; 2) der Schnittstrecken in der Ebene x = 0",
    schritte="3",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="Schnittfigur: Rechteck mit den Ecken E, F, (4; 2; 0) und (0; 2; 0); Schnittgerade x = (0; 1; 2) + t · (1; 0; 0), t reell",
    zwischenergebnis="K: z = 2y|L: 2y + z = 4",
    niveau_geschaetzt="II",
    fehlerquelle="die Schnittfigur an den Ecken B und C enden lassen statt an den Kantenmitten",
    abhaengig_von="2025-bebb-lk-A1.3a",
    bemerkung="Dublette von: 2025MerhoehtAAGLAA212-b. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 1.2 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.4a", block="A", aufgabe="1.4", titel="Stochastik (1.4)", teilaufgabe="a", seite="2", punkte="2", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit für lauter gleiche Ergebnisse als Potenz berechnen",
    typ_neben="",
    stichwoerter="Würfel zweimal|keine 3|5/6 je Wurf|(5/6)² = 25/36",
    voraussetzungen="Gegenwahrscheinlichkeit beim Würfel|Pfadregel für unabhängige Würfe",
    format="Begründung",
    operator="Begründen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Würfelspiel",
    textumfang="kurz",
    gegeben="Spiel: ein Würfel mit den Zahlen 1 bis 6 wird zweimal geworfen",
    gesucht="Begründung, dass die Wahrscheinlichkeit für keine 3 bei beiden Würfen 25/36 beträgt",
    verfahren="Wahrscheinlichkeit 5/6 für keine 3 bei einem Wurf, Pfadregel für beide Würfe",
    schritte="1",
    zahlenraum="Bruch|Potenz",
    einheiten="",
    ergebnis="die Wahrscheinlichkeit, bei einem Wurf nicht die 3 zu erzielen, beträgt 5/6; (5/6)² = 25/36",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="5/6 + 5/6 oder 1 − 1/36 rechnen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAStochastik11-a. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 1.1 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.4b", block="A", aufgabe="1.4", titel="Stochastik (1.4)", teilaufgabe="b", seite="2", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Unbekannte Größe aus einer Erwartungswertbedingung bestimmen",
    typ_neben="",
    stichwoerter="Einsatz 2 €|Auszahlung 0, 5, x je nach Anzahl der Dreien|P(genau eine 3) = 10/36, P(zwei Dreien) = 1/36|Ausgleich auf lange Sicht heißt Erwartungswert gleich Einsatz|x = 22",
    voraussetzungen="Wahrscheinlichkeiten für 0, 1, 2 Dreien über Pfade|faires Spiel als Erwartungswert gleich Einsatz deuten|lineare Gleichung lösen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Tabelle mit zwei Zeilen: Anzahl der Würfe mit der Zahl 3 (0, 1, 2) und Auszahlung in Euro (0, 5, x)",
    kontext="Würfelspiel",
    textumfang="mittel",
    gegeben="Würfel zweimal geworfen; Einsatz 2 €; Auszahlung 0 € bei keiner 3, 5 € bei genau einer 3, x € bei zwei Dreien; auf lange Sicht gleichen sich Einsätze und Auszahlungen aus",
    gesucht="Wert von x",
    verfahren="Erwartungswert der Auszahlung 1/36 · x + 10/36 · 5 gleich 2 setzen",
    schritte="2",
    zahlenraum="Bruch|ganz",
    einheiten="€",
    ergebnis="1/36 · x + 10/36 · 5 = 2 ⇔ x = 22",
    zwischenergebnis="P(genau eine 3) = 2 · 1/6 · 5/6 = 10/36",
    niveau_geschaetzt="III",
    fehlerquelle="P(genau eine 3) = 5/36 ansetzen (nur eine Reihenfolge)",
    abhaengig_von="2025-bebb-lk-A1.4a",
    bemerkung="Dublette von: 2025MerhoehtAStochastik11-b. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 1.1 b (Tabelle wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.5a", block="A", aufgabe="1.5", titel="Wahlaufgaben: Analysis (1.5)", teilaufgabe="a", seite="3", punkte="5", afb_amtlich="II|III",
    leitidee="Analysis", thema="Umkehrfunktion",
    typ="Flächenbeziehung zwischen Funktion und Umkehrfunktion über die Spiegelung an y = x beurteilen",
    typ_neben="",
    stichwoerter="Integral über g − f von 0 bis x_S|Fläche zwischen G_f und G_g|Integral über x − f(x)|Fläche zwischen y = x und G_f|Spiegelung an y = x|doppelter Inhalt|Aussage wahr",
    voraussetzungen="Integral einer Differenz als Fläche zwischen Graphen deuten|Graph der Umkehrfunktion als Spiegelbild an y = x|Symmetrie einer Fläche ausnutzen",
    format="Begründung",
    operator="Beurteilen Sie",
    antwort="Text",
    material="Koordinatensystem",
    skizze="Koordinatensystem im ersten Quadranten ohne Skalen, Ursprung mit 0 beschriftet; zwei Kurven vom Ursprung aus: G_g (oben, beschriftet) rechtsgekrümmt wie eine Wurzelfunktion, G_f (unten, beschriftet) linksgekrümmt; beide schneiden sich außer im Ursprung in einem Punkt rechts oben, danach liegt G_f oberhalb",
    kontext="ohne",
    textumfang="mittel",
    gegeben="f und g definiert in IR_0^+, g ist die Umkehrfunktion von f; Graphen G_f und G_g in der Abbildung schneiden sich nur im Ursprung und im Punkt (x_S; f(x_S)); Aussage: Integral von 0 bis x_S über (g(x) − f(x)) dx = 2 · Integral von 0 bis x_S über (x − f(x)) dx",
    gesucht="Beurteilung der Aussage",
    verfahren="linkes Integral als Inhalt der von G_f und G_g eingeschlossenen Fläche deuten, rechtes als Inhalt der Fläche zwischen der Geraden y = x und G_f; G_g ist das Spiegelbild von G_f an y = x, die Gerade halbiert die Fläche",
    schritte="3",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="die Aussage ist wahr: das linke Integral ist der Inhalt der von G_f und G_g eingeschlossenen Fläche, das rechte der Inhalt der von y = x und G_f eingeschlossenen Fläche; weil G_g durch Spiegelung von G_f an y = x entsteht, ist der erste Inhalt doppelt so groß wie der zweite",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Gerade y = x nicht als Symmetrieachse erkennen und die Aussage für falsch halten",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAnalysis22. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 2.2 (eine Teilaufgabe ohne Buchstaben; Abbildung wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.6a", block="A", aufgabe="1.6", titel="Wahlaufgaben: Analysis (1.6)", teilaufgabe="a", seite="3", punkte="1", afb_amtlich="I",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente mit gegebener Gleichung in die Abbildung einzeichnen",
    typ_neben="",
    stichwoerter="y = 1/2 x − 1/2|durch (1; 0) und P(3; 1)|Gerade zeichnen",
    voraussetzungen="Gerade aus der Gleichung über zwei Punkte zeichnen",
    format="Zeichnen",
    operator="Zeichnen Sie",
    antwort="Grafik",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit x-Achse von 0 bis etwa 9 (Markierungen 2, 4, 6, 8) und y-Achse von 0 bis 4 (Markierungen 2, 4), Gitter mit Schrittweite 1; Graph G von f(x) = √(x − 2): beginnt in (2; 0), verläuft durch P(3; 1) (markiert und beschriftet) und (6; 2), flach steigend bis etwa (9; 2,6); G beschriftet",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = √(x − 2) für x ≥ 2, Graph G und Punkt P(3; 1) in der Abbildung; die Gerade y = 1/2 x − 1/2 ist die Tangente an G in P und hat mit G nur P gemeinsam",
    gesucht="die Tangente in der Abbildung",
    verfahren="zwei Punkte der Geraden bestimmen, etwa (1; 0) und (3; 1), und die Gerade durchziehen",
    schritte="1",
    zahlenraum="Bruch",
    einheiten="",
    ergebnis="Gerade durch (1; 0) und P(3; 1), Steigung 1/2, berührt G in P und verläuft rechts von P oberhalb von G",
    zwischenergebnis="weiterer Punkt (5; 2)",
    niveau_geschaetzt="I",
    fehlerquelle="die Gerade durch den Ursprung zeichnen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAnalysis23-a. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 2.3 a (Abbildung wie im Pool). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.6b", block="A", aufgabe="1.6", titel="Wahlaufgaben: Analysis (1.6)", teilaufgabe="b", seite="3", punkte="4", afb_amtlich="II|III",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Steigungen aller Sekanten durch einen Punkt des Graphen angeben",
    typ_neben="",
    stichwoerter="Geraden durch P und einen weiteren Punkt von G|Sekante durch (2; 0) hat Steigung 1|Steigungen nähern sich der Tangentensteigung 1/2|rechts von P Steigungen zwischen 0 und 1/2|1/2 < m ≤ 1 oder 0 < m < 1/2",
    voraussetzungen="Sekantensteigung als Differenzenquotient|Tangente als Grenzlage der Sekanten|Verhalten des Graphen am Rand und im Unendlichen deuten",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Term",
    material="Koordinatensystem",
    skizze="Koordinatensystem mit x-Achse von 0 bis etwa 9 (Markierungen 2, 4, 6, 8) und y-Achse von 0 bis 4 (Markierungen 2, 4), Gitter mit Schrittweite 1; Graph G von f(x) = √(x − 2): beginnt in (2; 0), verläuft durch P(3; 1) (markiert und beschriftet) und (6; 2), flach steigend bis etwa (9; 2,6); G beschriftet",
    kontext="ohne",
    textumfang="kurz",
    gegeben="f(x) = √(x − 2) für x ≥ 2, Graph G, P(3; 1); die Tangente in P hat die Steigung 1/2 und mit G nur P gemeinsam; betrachtet werden alle Geraden, die mit G sowohl P als auch einen weiteren Punkt gemeinsam haben",
    gesucht="Steigungen dieser Geraden",
    verfahren="links von P: Sekantensteigung von 1 (durch (2; 0)) fallend gegen 1/2; rechts von P: von 1/2 fallend gegen 0, weil G rechtsgekrümmt ist und flacher wird; die Tangentensteigung selbst kommt nicht vor",
    schritte="3",
    zahlenraum="Bruch",
    einheiten="",
    ergebnis="m ist genau dann Steigung einer solchen Geraden, wenn 1/2 < m ≤ 1 oder 0 < m < 1/2 gilt",
    zwischenergebnis="Sekantensteigung (√(x − 2) − 1)/(x − 3) = 1/(√(x − 2) + 1)",
    niveau_geschaetzt="III",
    fehlerquelle="1/2 einschließen oder die Steigung 1 der Sekante durch (2; 0) übersehen",
    abhaengig_von="2025-bebb-lk-A1.6a",
    bemerkung="Dublette von: 2025MerhoehtAAnalysis23-b. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Analysis 2.3 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.7a", block="A", aufgabe="1.7", titel="Wahlaufgaben: Analytische Geometrie (1.7)", teilaufgabe="a", seite="3", punkte="2", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punktprobe an einer Geraden durchführen",
    typ_neben="",
    stichwoerter="g_k: x = (5 − 6k; 3k; 4 − 9k) + r · (2; −1; 3)|Ansatz (0; 0; 0)|zweite Koordinate r = 3k|erste Koordinate 0 = 5|Widerspruch für jedes k",
    voraussetzungen="Parameteransatz koordinatenweise|Scharparameter mitführen|Widerspruch erkennen",
    format="Begründung",
    operator="Zeigen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Geradenschar g_k: x = (5 − 6k; 3k; 4 − 9k) + r · (2; −1; 3), r reell, für jede reelle Zahl k",
    gesucht="Nachweis, dass der Ursprung für keinen Wert von k auf g_k liegt",
    verfahren="Ursprung gleichsetzen; aus der zweiten Koordinate r = 3k, in die erste eingesetzt 0 = 5",
    schritte="2",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="aus 0 = 3k − r folgt r = 3k; eingesetzt in 0 = 5 − 6k + 2r führt das zur falschen Aussage 0 = 5",
    zwischenergebnis="dritte Koordinate: 4 − 9k + 9k = 4 ≠ 0 ebenfalls Widerspruch",
    niveau_geschaetzt="II",
    fehlerquelle="k und r als denselben Parameter behandeln",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAGLAA221-a. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 2.1 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.7b", block="A", aufgabe="1.7", titel="Wahlaufgaben: Analytische Geometrie (1.7)", teilaufgabe="b", seite="3", punkte="3", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Identität aller Geraden einer Schar beurteilen",
    typ_neben="",
    stichwoerter="Stützvektor (5 − 6k; 3k; 4 − 9k) = (5; 0; 4) − 3k · (2; −1; 3)|Stützpunkt liegt auf der Geraden zu k = 0|gleicher Richtungsvektor|Aussage wahr",
    voraussetzungen="Stützvektor als Punkt plus Vielfaches des Richtungsvektors zerlegen|Identität von Geraden über gemeinsamen Punkt und Richtung",
    format="Begründung",
    operator="Beurteilen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="g_k: x = (5 − 6k; 3k; 4 − 9k) + r · (2; −1; 3), r reell; Aussage: alle Geraden g_k sind identisch",
    gesucht="Beurteilung der Aussage",
    verfahren="den Stützvektor als (5; 0; 4) − 3k · (2; −1; 3) schreiben; damit hat jede g_k die Darstellung (5; 0; 4) + r' · (2; −1; 3) mit r' = r − 3k",
    schritte="2",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="der Vektor (5 − 6k; 3k; 4 − 9k) lässt sich als (5; 0; 4) − 3k · (2; −1; 3) schreiben; jede g_k wird durch x = (5; 0; 4) + r' · (2; −1; 3) mit r' = r − 3k beschrieben, die Aussage ist wahr",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="wegen verschiedener Stützvektoren auf verschiedene, parallele Geraden schließen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAGLAA221-b. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 2.1 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.8a", block="A", aufgabe="1.8", titel="Wahlaufgaben: Analytische Geometrie (1.8)", teilaufgabe="a", seite="4", punkte="1", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Koordinatenebene senkrecht zu allen Ebenen einer Schar angeben",
    typ_neben="",
    stichwoerter="E_k: kx + (2 − k) · y = k|kein z in der Gleichung|Normalenvektor (k; 2 − k; 0)|alle E_k parallel zur z-Achse|senkrecht zur xy-Ebene",
    voraussetzungen="fehlende Koordinate in der Ebenengleichung als Parallelität zur Achse deuten|Normalenvektor ablesen",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Schar der Ebenen E_k: k · x + (2 − k) · y = k mit reellem k",
    gesucht="die Koordinatenebene, zu der alle Ebenen der Schar senkrecht stehen",
    verfahren="der Normalenvektor (k; 2 − k; 0) liegt für jedes k in der xy-Ebene, also stehen alle E_k senkrecht auf der xy-Ebene",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="xy-Ebene",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die xz- oder yz-Ebene nennen, weil z in der Gleichung fehlt",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAAGLAA222-a. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 2.2 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.8b", block="A", aufgabe="1.8", titel="Wahlaufgaben: Analytische Geometrie (1.8)", teilaufgabe="b", seite="4", punkte="4", afb_amtlich="II|III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Nichtparallelität verschiedener Ebenen einer Schar über die Normalenvektoren nachweisen",
    typ_neben="",
    stichwoerter="E_a und E_b mit a ≠ b|Normalenvektoren (a; 2 − a; 0) und (b; 2 − b; 0)|Ansatz (a; 2 − a; 0) = r · (b; 2 − b; 0)|a = rb und 2 − a = 2r − rb|r = 1, also a = b|Widerspruch",
    voraussetzungen="Parallelität von Ebenen über kollineare Normalenvektoren|Gleichungssystem mit zwei Scharparametern lösen|Widerspruch zur Voraussetzung a ≠ b",
    format="Begründung",
    operator="Zeigen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Schar E_k: k · x + (2 − k) · y = k, k reell",
    gesucht="Nachweis, dass je zwei verschiedene Ebenen der Schar nicht parallel sind",
    verfahren="zwei Ebenen E_a und E_b mit a ≠ b betrachten und annehmen, die Normalenvektoren seien Vielfache voneinander; aus den beiden Koordinatengleichungen folgt r = 1 und damit a = b",
    schritte="3",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="für E_a und E_b mit a ≠ b liefert (a; 2 − a; 0) = r · (b; 2 − b; 0) die Gleichungen a = rb und 2 − a = 2r − rb, also 2 − a = 2r − a und r = 1; das ist wegen a ≠ b nicht möglich",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="nur zwei konkrete Werte von k prüfen",
    abhaengig_von="2025-bebb-lk-A1.8a",
    bemerkung="Dublette von: 2025MerhoehtAAGLAA222-b. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A AG/LA (A2) 2.2 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.9a", block="A", aufgabe="1.9", titel="Wahlaufgaben: Stochastik (1.9)", teilaufgabe="a", seite="4", punkte="2", afb_amtlich="I|II",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Laplace-Experiment: Vergleich zweier Wahrscheinlichkeiten über die Anzahl der Ergebnisse begründen",
    typ_neben="",
    stichwoerter="X Produkt zweier Augenzahlen|10 = 2 · 5, 15 = 3 · 5|je zwei Reihenfolgen|gleich viele günstige Ergebnisse|Laplace",
    voraussetzungen="Zerlegung einer Zahl in zwei Faktoren von 1 bis 6|Laplace-Wahrscheinlichkeit über Anzahlen",
    format="Begründung",
    operator="Begründen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Würfel",
    textumfang="kurz",
    gegeben="Würfel mit den Zahlen 1 bis 6, zweimal geworfen; X ist das Produkt der beiden Zahlen",
    gesucht="Begründung, dass P(X = 10) = P(X = 15)",
    verfahren="alle Faktorzerlegungen von 10 und 15 mit Faktoren von 1 bis 6 aufzählen; beide Male genau zwei Ergebnisse von 36",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="bis auf Vertauschung der Faktoren sind 2 · 5 und 3 · 5 die einzigen Möglichkeiten, 10 bzw. 15 als Produkt zweier erzielter Zahlen darzustellen; somit sind die Wahrscheinlichkeiten gleich groß",
    zwischenergebnis="P(X = 10) = P(X = 15) = 2/36",
    niveau_geschaetzt="II",
    fehlerquelle="1 · 10 als Zerlegung mitzählen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAStochastik22-a. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 2.2 a. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.9b", block="A", aufgabe="1.9", titel="Wahlaufgaben: Stochastik (1.9)", teilaufgabe="b", seite="4", punkte="3", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Term für die Wahrscheinlichkeit eines Produktereignisses bei n Würfen ermitteln",
    typ_neben="",
    stichwoerter="n Würfe, n > 2|Produkt 2, 3 oder 5|genau ein Wurf zeigt 2, 3 oder 5, alle anderen 1|Position des Wurfs n-fach wählbar|3 · n · 1/6 · (1/6)^(n − 1)",
    voraussetzungen="Primzahl als Produkt nur mit Einsen deuten|Pfadregel mit n Stufen|Anzahl der Reihenfolgen als Faktor n",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Term",
    material="keins",
    skizze="keine",
    kontext="Würfel",
    textumfang="mittel",
    gegeben="Würfel mit den Zahlen 1 bis 6 wird n-mal geworfen, n > 2; Ereignis: das Produkt der n Zahlen ist 2, 3 oder 5",
    gesucht="Term für die Wahrscheinlichkeit dieses Ereignisses",
    verfahren="das Produkt ist genau dann 2, 3 oder 5, wenn genau ein Wurf diese Zahl zeigt und alle anderen Würfe 1 zeigen; drei Zahlen, n mögliche Positionen, Pfadwahrscheinlichkeit (1/6)^n",
    schritte="3",
    zahlenraum="Bruch|Potenz",
    einheiten="",
    ergebnis="3 · n · 1/6 · (1/6)^(n − 1)",
    zwischenergebnis="für n = 3: 9/216 (Abzählen bestätigt)",
    niveau_geschaetzt="III",
    fehlerquelle="den Faktor n für die Position des Wurfs vergessen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAStochastik22-b. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 2.2 b. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-A1.10a", block="A", aufgabe="1.10", titel="Wahlaufgaben: Stochastik (1.10)", teilaufgabe="a", seite="4", punkte="5", afb_amtlich="II|III",
    leitidee="Stochastik", thema="Unabhängigkeit",
    typ="Wahrscheinlichkeit eines Ereignisses aus Unabhängigkeit und einer Schnittwahrscheinlichkeit bestimmen",
    typ_neben="",
    stichwoerter="A und B unabhängig|P(B) = P(A) + 0,6|P(A und nicht B) = 0,04|x · (1 − (x + 0,6)) = 0,04|x² − 0,4x + 0,04 = 0|x = 0,2",
    voraussetzungen="Unabhängigkeit als Produktregel für A und das Gegenereignis von B|Gegenwahrscheinlichkeit|quadratische Gleichung mit doppelter Lösung",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="zwei stochastisch unabhängige Ereignisse A und B mit P(B) = P(A) + 0,6 und P(A und nicht B) = 0,04",
    gesucht="P(A)",
    verfahren="mit x = P(A): P(nicht B) = 1 − (x + 0,6) = 0,4 − x; Unabhängigkeit liefert x · (0,4 − x) = 0,04; quadratische Gleichung lösen",
    schritte="3",
    zahlenraum="dezimal",
    einheiten="",
    ergebnis="mit x = P(A) gilt x · (0,4 − x) = 0,04 ⇔ x² − 0,4x + 0,04 = 0 ⇔ x = 0,2",
    zwischenergebnis="P(B) = 0,8|(x − 0,2)² = 0",
    niveau_geschaetzt="III",
    fehlerquelle="P(A und nicht B) = P(A) − P(B) oder P(A) · P(B) ansetzen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtAStochastik23. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile. Pool Teil A Stochastik 2.3 (eine Teilaufgabe ohne Buchstaben). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B3a", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="a", seite="9", punkte="4", afb_amtlich="I",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Kürzeste und längste Kante und Volumen einer Pyramide über einem Drachenviereck berechnen",
    typ_neben="",
    stichwoerter="|AB| = |(2; 2; 0)| = 2√2 kürzeste|Drachenfläche 1/2 · 6 · 4 = 12|V = 1/3 · 12 · 6 = 24",
    voraussetzungen="Kantenlängen als Beträge|Drachenfläche aus den Diagonalen|Pyramidenvolumen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild: Pyramide ABCDS, Grundfläche Drachenviereck in der xy-Ebene mit A im Ursprung, B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), Spitze S(0 | 0 | 6) senkrecht über A; Erwartungshorizont d: Dreieck BDQ_2 mit Q_2(0 | 2 | 4) eingezeichnet",
    kontext="ohne",
    textumfang="kurz",
    gegeben="A(0 | 0 | 0), B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), S(0 | 0 | 6); ABCD Drachenviereck",
    gesucht="Länge der kürzesten Kante und Volumen",
    verfahren="Kantenlängen vergleichen, Grundfläche über Diagonalen, Volumen",
    schritte="3",
    zahlenraum="Wurzel|ganz",
    einheiten="",
    ergebnis="kleinste Kantenlänge |AB| = |(2; 2; 0)| = 2√2; Grundfläche 1/2 · 6 · 4 = 12; Volumen 1/3 · 12 · 6 = 24",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Drachenfläche ohne den Faktor 1/2",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBAGLAA2WTR-1a. AB amtlich: I. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Abbildung (Pyramide auf Gitternetz) wie im Pool. Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B3b", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="b", seite="9", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Normalenvektor aus der Orthogonalität zu Vielfachen der Spannvektoren begründen",
    typ_neben="",
    stichwoerter="(−1; 2; 0) kollinear zu BC = (−2; 4; 0)|(−1; −1; 3) kollinear zu BS = (−2; −2; 6)|n senkrecht zu beiden Spannvektoren ⇒ Normalenvektor",
    voraussetzungen="Kollinearität erkennen|Normalenvektor als Vektor senkrecht zu zwei aufspannenden Vektoren",
    format="Begründung",
    operator="Begründen Sie",
    antwort="Text",
    material="Körper",
    skizze="Schrägbild: Pyramide ABCDS, Grundfläche Drachenviereck in der xy-Ebene mit A im Ursprung, B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), Spitze S(0 | 0 | 6) senkrecht über A; Erwartungshorizont d: Dreieck BDQ_2 mit Q_2(0 | 2 | 4) eingezeichnet",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Vektoren n ≠ 0 mit n · (−1; 2; 0) = 0 und n · (−1; −1; 3) = 0; Ebene E durch B, C, S",
    gesucht="Begründung, dass ein solcher Vektor Normalenvektor von E ist",
    verfahren="die beiden Vektoren als Vielfache von BC und BS erkennen",
    schritte="2",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="(−1; 2; 0) ist kollinear zu BC, (−1; −1; 3) ist kollinear zu BS; da BC und BS die Ebene E aufspannen und n zu diesen Vektoren senkrecht steht, ist n ein Normalenvektor von E",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="n konkret ausrechnen statt zu begründen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBAGLAA2WTR-1b. AB amtlich: II. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B3c", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="c", seite="9", punkte="3", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen",
    typ_neben="",
    stichwoerter="n = (2; 1; 1), n_xy = (0; 0; 1)|cos α = 1/√6|α ≈ 65,9°",
    voraussetzungen="Winkel zwischen Ebenen über Normalenvektoren",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild: Pyramide ABCDS, Grundfläche Drachenviereck in der xy-Ebene mit A im Ursprung, B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), Spitze S(0 | 0 | 6) senkrecht über A; Erwartungshorizont d: Dreieck BDQ_2 mit Q_2(0 | 2 | 4) eingezeichnet",
    kontext="ohne",
    textumfang="kurz",
    gegeben="E: 2x + y + z = 6",
    gesucht="Winkel zwischen E und der xy-Ebene",
    verfahren="Winkelformel mit Normalenvektoren",
    schritte="2",
    zahlenraum="Wurzel|dezimal",
    einheiten="°",
    ergebnis="cos α = ((2; 1; 1) · (0; 0; 1)) / (|(2; 1; 1)| · |(0; 0; 1)|) = 1/√6 liefert α ≈ 65,9°",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Betrag von (2; 1; 1) als √5",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBAGLAA2WTR-1c. AB amtlich: II. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B3d", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="d", seite="9", punkte="4", afb_amtlich="II",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharebene für einen Parameterwert angeben und Schnittfigur mit der Pyramide einzeichnen",
    typ_neben="",
    stichwoerter="F_2: 2y + 0 · z = 4 ⇔ y = 2|Ebene durch B und D parallel zur xz-Ebene|Q_2 auf SC mit y = 2: (0 | 2 | 4)|Dreieck BDQ_2 einzeichnen",
    voraussetzungen="Parameter einsetzen|Ebene y = 2 im Schrägbild|Schnittpunkt mit der Kante SC",
    format="Kurzantwort|Zeichnen",
    operator="Geben Sie an|Zeichnen Sie ein",
    antwort="Term",
    material="Körper",
    skizze="Schrägbild: Pyramide ABCDS, Grundfläche Drachenviereck in der xy-Ebene mit A im Ursprung, B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), Spitze S(0 | 0 | 6) senkrecht über A; Erwartungshorizont d: Dreieck BDQ_2 mit Q_2(0 | 2 | 4) eingezeichnet",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Schar F_k: k · y + (k − 2) · z = 2k, k ∈ ]0; 3[; jede F_k schneidet die Pyramide im Dreieck BDQ_k mit Q_k auf SC",
    gesucht="Gleichung von F_2 und Schnittfigur in der Abbildung",
    verfahren="k = 2 einsetzen, Q_2 auf SC bestimmen, Dreieck zeichnen",
    schritte="3",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="Gleichung von F_2: y = 2; Schnittfigur Dreieck BDQ_2 mit Q_2(0 | 2 | 4) eingezeichnet",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="Q_2 auf der Kante AS statt SC suchen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBAGLAA2WTR-1d. AB amtlich: II. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B3e", block="B", aufgabe="3", titel="Pyramide", teilaufgabe="e", seite="9", punkte="6", afb_amtlich="III",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Scharparameter für den minimalen Flächeninhalt eines Schnittdreiecks über die Orthogonalität zur Kante ermitteln",
    typ_neben="",
    stichwoerter="Grundseite BD fest, Höhe |MQ_k| mit M Mittelpunkt von BD|minimal, wenn MQ_k ⊥ SC, dann F_k ⊥ SC|Normalenvektor (0; k; k − 2) = λ · (0; 6; −6)|k = 6λ, k − 2 = −6λ ⇒ k = 1",
    voraussetzungen="Dreiecksfläche mit fester Grundseite über die Höhe|kürzester Abstand als Lot|Ebene senkrecht zur Kante: Normalenvektor kollinear zum Richtungsvektor",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild: Pyramide ABCDS, Grundfläche Drachenviereck in der xy-Ebene mit A im Ursprung, B(2 | 2 | 0), C(0 | 6 | 0), D(−2 | 2 | 0), Spitze S(0 | 0 | 6) senkrecht über A; Erwartungshorizont d: Dreieck BDQ_2 mit Q_2(0 | 2 | 4) eingezeichnet",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Schar F_k wie in d; Dreiecke BDQ_k; es gibt k mit minimalem Flächeninhalt",
    gesucht="dieser Wert von k",
    verfahren="Minimum der Höhe als Lot von M auf SC, Orthogonalität der Ebene zur Kante, Kollinearität lösen",
    schritte="4",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="der Flächeninhalt des Dreiecks BDQ_k ist minimal, wenn |MQ_k| am kleinsten ist, M Mittelpunkt von BD; die zugehörige Ebene F_k steht dann senkrecht zur Kante SC; (0; k; k − 2) = λ · (0; 6; −6) ⇒ k = 6λ ∧ k − 2 = −6λ ⇒ k − 2 = −k ⇒ k = 1",
    zwischenergebnis="Q_1(0 | 4 | 2), Kontrolle über die Ableitung von |MQ_t|² bestätigt",
    niveau_geschaetzt="III",
    fehlerquelle="Flächeninhalt als Funktion von k aufstellen und ableiten (lang, fehleranfällig)",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBAGLAA2WTR-1e. AB amtlich: III. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B4a", block="B", aufgabe="4", titel="Naturpark (Aufgabenteil 1)", teilaufgabe="a", seite="10", punkte="1", afb_amtlich="I",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="",
    stichwoerter="X ~ B(300; 0,14), P(X = 36) ≈ 4 %",
    voraussetzungen="Einzelwahrscheinlichkeit am Rechner",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Naturpark/Radausflügler",
    textumfang="kurz",
    gegeben="14 % Radausflügler, Anzahl binomialverteilt; Stichprobe 300",
    gesucht="P(genau 36 Radausflügler)",
    verfahren="P(X = 36) am Rechner",
    schritte="1",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="X Anzahl der Radausflügler; P(X = 36) ≈ 4 % (n = 300, p = 0,14)",
    zwischenergebnis="4,2 %",
    niveau_geschaetzt="I",
    fehlerquelle="kumulierte statt Einzelwahrscheinlichkeit",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBStochastikWTR2-1a. AB amtlich: I. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B4b", block="B", aufgabe="4", titel="Naturpark (Aufgabenteil 1)", teilaufgabe="b", seite="10", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer relativen Abweichung vom Erwartungswert nach oben berechnen",
    typ_neben="",
    stichwoerter="μ = 300 · 0,14 = 42|mindestens 10 % größer: X ≥ 46,2, also X ≥ 47|P(X ≥ 47) ≈ 22 %",
    voraussetzungen="Erwartungswert n · p|Schranke aufrunden|Gegenereignis am Rechner",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Naturpark/Radausflügler",
    textumfang="kurz",
    gegeben="X wie in a",
    gesucht="P(Anzahl um mindestens 10 % größer als der Erwartungswert)",
    verfahren="μ berechnen, 1,1μ aufrunden, P(X ≥ 47)",
    schritte="3",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="μ = 300 · 0,14 = 42; P(X ≥ 47) ≈ 22 % (n = 300, p = 0,14)",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="X ≥ 46 rechnen (46 < 46,2)",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBStochastikWTR2-1b. AB amtlich: II. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B4c", block="B", aufgabe="4", titel="Naturpark (Aufgabenteil 2 a)", teilaufgabe="c", seite="10", punkte="3", afb_amtlich="I",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen",
    typ_neben="",
    stichwoerter="A: spätestens am Vortag gebucht (80 %), B: genutzt|P(B | A) = 90 %, P(B | nicht A) = 95 %",
    voraussetzungen="zweistufiges Baumdiagramm|Gegenwahrscheinlichkeiten",
    format="Zeichnen",
    operator="Stellen Sie dar",
    antwort="Grafik",
    material="keins",
    skizze="keine",
    kontext="Naturpark/Shuttlebus",
    textumfang="mittel",
    gegeben="80 % der Fahrkarten spätestens am Vortag gebucht, davon 90 % genutzt; von den am Tag gebuchten 95 % genutzt",
    gesucht="beschriftetes Baumdiagramm",
    verfahren="erste Stufe Buchungszeitpunkt, zweite Stufe Nutzung",
    schritte="1",
    zahlenraum="Prozent",
    einheiten="",
    ergebnis="Baumdiagramm mit A (80 %), nicht A (20 %); B | A 90 %, nicht B | A 10 %; B | nicht A 95 %, nicht B | nicht A 5 %",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="Stufen vertauschen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBStochastikWTR2-2a. AB amtlich: I. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B4d", block="B", aufgabe="4", titel="Naturpark (Aufgabenteil 2 b)", teilaufgabe="d", seite="10", punkte="3", afb_amtlich="II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen",
    typ_neben="",
    stichwoerter="P(A | nicht B) = 0,8 · 0,1 / P(nicht B) = 0,08/P(nicht B)|P(nicht A | nicht B) = 0,2 · 0,05 / P(nicht B) = 0,01/P(nicht B)|Verhältnis 8, Aussage richtig",
    voraussetzungen="bedingte Wahrscheinlichkeit als Pfad durch Gesamtwahrscheinlichkeit|gemeinsamer Nenner kürzt sich",
    format="Begründung",
    operator="Beurteilen Sie",
    antwort="Text",
    material="Diagramm",
    skizze="Baumdiagramm: A (80 %, Buchung spätestens am Vortag) / nicht A (20 %), darunter B (genutzt) 90 % bzw. 95 % und nicht B 10 % bzw. 5 %",
    kontext="Naturpark/Shuttlebus",
    textumfang="mittel",
    gegeben="Baumdiagramm aus a; nicht genutzte Fahrkarte; Aussage: P(Vortag | nicht genutzt) ist achtmal so groß wie P(am Tag | nicht genutzt)",
    gesucht="Beurteilung",
    verfahren="beide bedingten Wahrscheinlichkeiten als Brüche mit gleichem Nenner",
    schritte="3",
    zahlenraum="dezimal",
    einheiten="",
    ergebnis="P(A | nicht B) = 0,8 · 0,1 / P(nicht B) = 0,08 / P(nicht B); P(nicht A | nicht B) = 0,2 · 0,05 / P(nicht B) = 0,01 / P(nicht B); die Aussage ist richtig",
    zwischenergebnis="P(nicht B) = 0,09",
    niveau_geschaetzt="II",
    fehlerquelle="unbedingte Pfade 0,08 und 0,01 vergleichen und die Bedingung übersehen (Ergebnis gleich, Begründung unvollständig)",
    abhaengig_von="2025-bebb-lk-B4c",
    bemerkung="Dublette von: 2025MerhoehtBStochastikWTR2-2b. AB amtlich: II. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B4e", block="B", aufgabe="4", titel="Naturpark (Aufgabenteil 2 c)", teilaufgabe="e", seite="10", punkte="5", afb_amtlich="II",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel eines einseitigen Signifikanztests bestimmen",
    typ_neben="",
    stichwoerter="H0: p ≤ 0,14, n = 500, α = 8 %|Y ~ B(500; 0,14): P(Y ≥ 81) ≈ 9,0 %, P(Y ≥ 82) ≈ 7,1 %|Ablehnung bei mindestens 82",
    voraussetzungen="rechtsseitiger Test|kleinstes k mit P(Y ≥ k) ≤ α am Rechner",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="Naturpark/Signifikanztest",
    textumfang="lang",
    gegeben="Nullhypothese: Anteil der Radausflügler höchstens 14 %; Signifikanzniveau 8 %; Stichprobe 500; Busse laufen nur bei Ablehnung weiter",
    gesucht="Entscheidungsregel",
    verfahren="kumulierte Wahrscheinlichkeiten von oben an der Grenze vergleichen",
    schritte="3",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="Y Anzahl der Radausflügler; P(Y ≥ 81) ≈ 9,0 %, P(Y ≥ 82) ≈ 7,1 % (n = 500, p = 0,14); befinden sich mindestens 82 Radausflügler in der Stichprobe, so wird die Nullhypothese abgelehnt",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="linksseitig testen",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBStochastikWTR2-2c. AB amtlich: II. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")
row(id="2025-bebb-lk-B4f", block="B", aufgabe="4", titel="Naturpark (Aufgabenteil 2 d)", teilaufgabe="f", seite="11", punkte="5", afb_amtlich="III",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Mindestanteil für eine Schranke des Fehlers zweiter Art ermitteln und den Fehler im Sachzusammenhang beschreiben",
    typ_neben="",
    stichwoerter="n = 200, Ablehnung bei mehr als 35|Fehler 2. Art: H0 nicht abgelehnt (Y ≤ 35), obwohl p > 0,14|P_{0,20}(Y ≤ 35) ≈ 22 %, P_{0,21}(Y ≤ 35) ≈ 13 % ≤ 15 %|p mindestens 21 %|Deutung: Anteil gestiegen, Busse trotzdem eingestellt",
    voraussetzungen="Fehler zweiter Art als Annahmebereich unter der Alternative|Anteil auf ganze Prozent probieren|Deutung über die Entscheidung",
    format="Rechnung|Kurzantwort",
    operator="Ermitteln Sie|Beschreiben Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Naturpark/Signifikanztest",
    textumfang="lang",
    gegeben="Test mit n = 200; Ablehnung bei mehr als 35 Radausflüglern; Fehler zweiter Art höchstens 15 %; Busse laufen nur bei Ablehnung weiter",
    gesucht="Mindestanteil auf ganze Prozent und Bedeutung des Fehlers zweiter Art",
    verfahren="P_p(Y ≤ 35) für p in ganzen Prozent, kleinstes p mit ≤ 15 %; deuten",
    schritte="3",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="P(Y ≤ 35) ≈ 22 % für p = 0,20 und ≈ 13 % für p = 0,21 (n = 200); der tatsächliche Anteil müsste mindestens 21 % betragen; obwohl der Anteil der Radausflügler auf über 14 % gestiegen ist, entscheidet man sich aufgrund des Testergebnisses dafür, den Betrieb der Shuttlebusse einzustellen",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="Fehler zweiter Art als P(Y > 35) unter p = 0,14 rechnen (das ist der Fehler erster Art)",
    abhaengig_von="",
    bemerkung="Dublette von: 2025MerhoehtBStochastikWTR2-2d. AB amtlich: III. Wortgleich mit der Poolaufgabe 2025 erhöht (Zahlen, Aufträge, BE); afb_amtlich aus der Poolzeile (AB-Spalte). Ergebnis aus der Poolzeile übernommen (dort amtlich und nachgerechnet).")

NEUE_TYPEN = [
    ("Genau zwei Nullstellen einer Schar aus der faktorisierten Form begründen und angeben", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus einem faktorisierten Scharterm (Produkt von Quadraten) begründen, dass jede Funktion der Schar genau zwei Nullstellen hat, und diese in Abhängigkeit vom Parameter angeben.",
     "2025-bebb-lk-B2.1a"),
    ("Abstand des Hochpunkts zu den Tiefpunkten einer Schar in Abhängigkeit vom Parameter berechnen", "Analysis", "Funktionsscharen und Ortskurven",
     "Hoch- und Tiefpunkte einer Schar aus der faktorisierten Ableitung bestimmen und den (gleichen) Abstand des Hochpunkts zu den Tiefpunkten als Term im Parameter berechnen.",
     "2025-bebb-lk-B2.1c"),
    ("Integralwert: Integral als Flächeninhalt für alle Scharkurven über das Vorzeichen des Terms beurteilen", "Analysis", "Flächeninhalt durch Integration",
     "Ohne Integration beurteilen, ob ein bestimmtes Integral für jeden Parameterwert den Inhalt der aus mehreren Stücken bestehenden Fläche angibt, über das Vorzeichen des Scharterms auf dem Intervall.",
     "2025-bebb-lk-B2.1d"),
    ("Fläche: Lösungsschritte zur Fläche zwischen zwei Scharkurven geometrisch deuten und Parameterungleichung untersuchen", "Analysis", "Flächeninhalt durch Integration",
     "Vorgelegte Schritte (Gleichsetzen liefert die Schnittstellen, Summe zweier Differenzintegrale liefert den Flächenterm) in Bezug auf die Graphen deuten und eine Ungleichung zwischen dem Flächenterm und einer Potenz des Parameters für einen Parameterbereich untersuchen.",
     "2025-bebb-lk-B2.1e"),
    ("Integralwert: Integralabschätzung über ein Rechteck und Flächenvergleich am Graphen erläutern und im Sachzusammenhang deuten", "Analysis", "Flächeninhalt durch Integration",
     "Erläutern, wie ein eingezeichnetes Rechteck und die schraffierten Über- und Fehlflächen am Graphen einer Rate eine Ungleichung für ein bestimmtes Integral begründen, und die Ungleichung als Mengenaussage im Sachzusammenhang deuten.",
     "2025-bebb-lk-B2.1g"),
    ("Stellen mit vorgegebenem Anstieg und Wendestelle am Graphen der Ableitung ablesen", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Aus dem abgebildeten Graphen der Ableitung die Stellen mit einem vorgegebenen Ableitungswert (Anstieg der Funktion) und eine Wendestelle der Funktion (Extremstelle der Ableitung) näherungsweise angeben.",
     "2025-bebb-lk-B2.2a"),
    ("Integral der Ableitung als Differenz von Funktionswerten berechnen", "Analysis", "Stammfunktion und Hauptsatz",
     "Ein bestimmtes Integral über die Ableitung einer Funktion nach dem Hauptsatz als Differenz zweier Funktionswerte der Funktion berechnen.",
     "2025-bebb-lk-B2.2b"),
    ("Integrationsgrenzen mit Integral null über die zweite Ableitung am Graphen der Ableitung angeben", "Analysis", "Stammfunktion und Hauptsatz",
     "Grenzen c ≠ d angeben, für die das Integral über die zweite Ableitung null ist, indem am Graphen der ersten Ableitung zwei Stellen mit gleichem Ableitungswert abgelesen werden (Hauptsatz), mit Begründung.",
     "2025-bebb-lk-B2.2c"),
    ("Ableitung einer Schar als Vielfaches der Ableitung eines Scharmitglieds nachweisen", "Analysis", "Funktionsscharen und Ortskurven",
     "Nachweisen, dass die Ableitung jeder Funktion einer Schar mit Parameter im Exponenten das e^a-fache der Ableitung des Scharmitglieds zum Parameter null ist (Abspalten des konstanten Faktors oder Produktregel).",
     "2025-bebb-lk-B2.2e"),
    ("Extrempunkte aller Scharkurven aus dem Ableitungsgraphen eines Scharmitglieds ohne Rechnung begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Aus dem abgebildeten Ableitungsgraphen eines Scharmitglieds und der Beziehung f_a' = e^a · f_0' (positiver Faktor) begründen, dass alle Graphen der Schar genau einen Hoch- und einen Tiefpunkt an denselben Stellen haben, und deren Koordinaten angeben.",
     "2025-bebb-lk-B2.2f"),
    ("Zeitpunkt der maximalen Änderungsrate am Graphen der zweiten Ableitung ablesen und begründen", "Analysis", "Ableitungsgraph und Funktionsgraph",
     "Aus dem abgebildeten Graphen der zweiten Ableitung einer Bestandsfunktion den Zeitpunkt der größten Änderungsrate als Nullstelle mit Vorzeichenwechsel von plus nach minus (Maximum der ersten Ableitung) ablesen und begründen.",
     "2025-bebb-lk-B2.2i"),
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
# „Dublette von:", sobald der Stapel erfasst ist (abitur-abgleich.py).
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
    # Maßstab der Schätzung (Kern § 5 v0.7): afb_amtlich genau bei Dubletten, aus der
    # Poolzeile; eine Landeszeile hat keinen amtlichen Bereich (Schätzung ohne Maßstab).
    a(bool(z["afb_amtlich"]) == ("Dublette von:" in z["bemerkung"]),
      f"{i}: afb_amtlich {'gefüllt ohne' if z['afb_amtlich'] else 'leer trotz'} Dublettenverweis")
    if z["afb_amtlich"]:
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
            OFFENE_POSTEN.append(f"{i}: Poolzeile {mo.group(2)} ist erfasst – Vermerk mit abitur-abgleich.py in „Dublette von:“ umstellen")
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
    Maximum über afb_amtlich; 0, wenn nichts ausgewiesen ist (Schätzung ohne Maßstab)."""
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
                  f"{len(alt) - gew} Zeilen ohne Maßstab (afb_amtlich leer, Kern § 5). Kennzahl, keine Schranke.")
            print("Ohne Maßstab je Heft: " + ", ".join(
                f"{h} {sum(1 for z in alt if z['papier'] == h and not amtlich_von(z))} von {sum(1 for z in alt if z['papier'] == h)}"
                for h in sorted({z['papier'] for z in alt})))
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
    if SCHWELLEN["eichung_mindestens"] is not None and gew >= SCHWELLEN["eichung_ab_zeilen"]:
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
              + (f" ({n - gew_alle} ohne Maßstab: afb_amtlich leer)" if gew_alle != n else "")
              + (f"; davon {geerbte} Zeilen mit geerbter Schätzung (Dubletten, im Pool geeicht), "
                 f"{gew_alle - geerbte} eigene" if geerbte else "")
              + (f"; Abweichungen: {'; '.join(abw)}" if abw else ""))
    else:
        print(f"Eichung: keine Zeile mit amtlichem Bereich ({n} Zeilen ohne Maßstab).")
    print(f"Schwellen: {len(unsicher)} Zeilen mit „?“ (erlaubt {grenze_frage}), "
          f"{len(ersatz)} ohne passendes Thema (erlaubt {grenze_ersatz}), "
          f"Eichung eigener Zeilen {100 * treffer_eng / gew if gew else 0:.0f} % von {gew} "
          + ("(Kennzahl; Schranke ausgesetzt, Entscheidung des Lehrers 17.09.2026)" if SCHWELLEN["eichung_mindestens"] is None else
             f"(verlangt {100 * SCHWELLEN['eichung_mindestens']:.0f} %"
             f"{', nicht scharf' if gew < SCHWELLEN['eichung_ab_zeilen'] else ''})"))
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
