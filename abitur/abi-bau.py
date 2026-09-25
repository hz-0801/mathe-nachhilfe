# -*- coding: utf-8 -*-
"""abi-bau.py – Gerüst für die Erfassung eines Hefts im Profil abi.
Version 0.14 · 27.09.2026 · gilt mit katalog-prompt.md v0.9, abitur-vokabular.md v1.6, abi.md v0.30, abitur-abgleich.py v0.24 und den Geltungsdateien abi-<zielprüfung>-geltung.md v1.0

Änderungen gegenüber 0.13 (Auftrag Nacht 2026-09-27, Teil 9: CAS-Nachtrag
2017-bb-ea-cas, 27.09.2026): Nachtragsmodus für die Rechnerfassung eines schon
erfassten WTR-Hefts (abi.md § 7, „CAS-Hefte 2017/2018"). Eine Zeile bekommt
nur eine Teilaufgabe, die von der WTR-Fassung abweicht; die Vollständigkeit
lässt sich deshalb nicht mehr allein aus KONFIG["soll"] prüfen. Neue Schlüssel
in KONFIG, nur im Nachtrag:
  - "nachtrag_zu": papier des WTR-Hefts (2017-bb-ea); papier muss es mit dem
    Zusatz -cas oder -mms sein.
  - "soll": je Aufgabe mit abweichenden Teilaufgaben (in Brandenburg die
    „CAS:"-Aufgaben) die Summe der BE dieser Teilaufgaben – die Punktprüfung
    der Zeilen bleibt so scharf wie bisher.
  - "uebernommen": je solcher Aufgabe die wortgleichen Teilaufgaben mit gleichen
    BE, die keine Zeile bekommen, als CAS-Buchstabe → (WTR-Buchstabe, BE); die
    BE müssen die der WTR-Zeile sein. Die Buchstaben verschieben sich, wo die
    CAS-Fassung eine Teilaufgabe einschiebt (2017: 2.1 g = WTR f).
  - "unveraendert": die übrigen Aufgaben des Hefts mit ihren BE; das WTR-Heft
    muss sie im Katalog mit genau diesen Punktsummen führen.
  - "be_angeboten": die angebotenen BE des Hefts (alle Aufgaben, beide
    Wahlwege, wie bei jedem Heft in KONFIG["soll"] gezählt; 2017-bb-ea: 185,
    abi-pruefungen.md § 2). soll + uebernommen + unveraendert muss sie ergeben,
    und je abweichender Aufgabe soll + uebernommen die Aufgabensumme der
    WTR-Fassung; soll und unveraendert zusammen decken genau die Aufgaben des
    WTR-Hefts.
Jede Zeile des Nachtrags trägt am Anfang von bemerkung „CAS-Nachtrag zu
<WTR-id> (WTR): …" (Zeile derselben Aufgabe im WTR-Heft) oder „CAS-Nachtrag,
ohne WTR-Gegenstück: …"; ein Poolvermerk („Dublette von:", „Poolaufgabe (nicht
erfasst …)", „Abgewandelt von:") steht davor, weil die Skripte ihn am Anfang
verlangen. Kein WTR-Buchstabe darf zweimal belegt sein (Zeile und
Übernommenes); WTR-Teilaufgaben ohne CAS-Gegenstück sind ein Hinweis, kein
Fehler. Die Selbstprüfung prüft zusätzlich jeden Nachtragsvermerk im Bestand
(Form, Stellung, Verweis auf eine Zeile derselben Aufgabe im WTR-Heft). Alles
Übrige – Pflichtfelder, Vokabular, Typen samt Präfix, Zeilenthema = Typthema,
Minus und Umlaute, Schwellen – gilt unverändert; ohne "nachtrag_zu" verhält
sich das Skript wie 0.13.

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
  5. CAS-Nachtrag zu einem erfassten WTR-Heft: KONFIG["nachtrag_zu"] und die
     Schlüssel aus den Änderungen zu 0.14 setzen, ZEILEN nur mit den
     abweichenden Teilaufgaben füllen.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    "jahr": "2017",
    "papier": "2017-be-gk",
    "datei": "hefte/abi/2017-be-gk.pdf",  # amtliches Heft (Bildungsserver, 17_Ma_GK_Aufgaben.pdf), 8 Seiten mit Textebene, lokal (abi-quellen.md § 2, § 8)
    "seiten": 8,
    # Sollpunkte je Aufgabe aus den BE-Tabellen; jede Aufgabe des Hefts muss hier
    # stehen (Vollständigkeit). Grundlegendes Niveau bis 2018 (abi.md § 7): kein
    # hilfsmittelfreier Teil, alle Zeilen block B, soll_teil1 entfällt; drei
    # Aufgabenstellungen mit je zwei Wahlaufgaben 40/40, 20/20, 20/20 – 160 BE
    # angeboten, 80 bearbeitet. BE-Vektoren: 1.1 9-6-6-5-5-9, 1.2 11-3-5-5-9-7,
    # 2.1 7-5-4-4, 2.2 2-4-5-4-5, 3.1 2-3-2-3-2-4-4, 3.2 5-3-5-3-4.
    "soll": {"1.1": 40, "1.2": 40, "2.1": 20, "2.2": 20, "3.1": 20, "3.2": 20},
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
# Heft 2017-be-gk (amtliches Heft 17_Ma_GK_Aufgaben.pdf, 8 Seiten mit Textebene;
# Leitfassung grundlegend 2017). Text mit pdftotext -layout, jede Aufgabenseite
# gerendert (Abbildungen 1.1, Foto 1.1 e, Fotos 1.2 und 2.1, Schrägbilder 2.2,
# Würfelnetz und Glücksräder 3.2, Anlage Seite 8). Keine amtlichen Lösungen:
# jede Zeile „Eigene Rechnung“ (sympy). Pool: 3.1 Smartphone ist die Poolaufgabe
# 2017 grundlegend Teil B Stochastik WTR 1 (Stapel 2017-ga-B, erfasst) – a, b, c,
# d, f, g wortgleich („Dublette von:“), e abgewandelt („Abgewandelt von:“);
# Textvergleich aller übrigen Teilaufgaben gegen die 45 Pooldateien 2017 beider
# Niveaus ohne weiteren Treffer.
ST11 = "Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Bauelements wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke des Bauteils liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f."
SK11 = "Profilzeichnung in einem x-y-Koordinatensystem ohne Achsenteilung: grau ausgefülltes Brückenteil zwischen der y-Achse und einer senkrechten rechten Kante, unten auf der x-Achse. Die obere Begrenzung ist der mit f beschriftete Graph; er beginnt im Eckpunkt A auf der y-Achse knapp über der x-Achse mit waagerechter Tangente, steigt S-förmig und erreicht im Eckpunkt B über der rechten Kante wieder waagerecht seinen höchsten Punkt. Links von A und rechts von B schließen waagerechte Linien (Anschlussschienen) an, gestrichelte Kurvenstücke setzen den Graphen über A hinaus nach links oben und über B hinaus nach rechts unten fort. Die rechte Kante ist mit „Höhe“, die Unterkante mit „Länge“ beschriftet; Zahlenwerte stehen nicht in der Abbildung."
ST12 = "Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m."
SK12 = "Schwarz-weißes Foto eines Berliner Veranstaltungsortes: mehrere gleichartige, spitz zulaufende weiße Dachelemente vor einem Hochhaus; das Foto dient nur der Veranschaulichung und enthält keine Maße."
ST21 = "Ein Jet hebt im Punkt P0(1140 | 240 | 0) von einer nach Nordosten zeigenden Startbahn ab und erreicht eine Sekunde später die Position P1(1200 | 251 | 30). Er verändert seine Richtung beim Starten nicht nach rechts oder links, fliegt geradlinig und zunächst mit gleichbleibender Geschwindigkeit. Flughafen und Stadt liegen in der x-y-Ebene, 1 LE = 1 m."
SK21 = "Schwarz-weißes Foto eines startenden Flugzeugs über einem Flughafengebäude mit Tower und Kraftwerksschornsteinen im Hintergrund; das Foto enthält keine Maße."
ST22 = "Verpackung für Schokotrüffel: gerader quadratischer Pyramidenstumpf ABCDEFGH mit aufgesetzter gerader quadratischer Pyramide EFGHS als Deckel. Kantenlänge AB = 10 cm, Kantenlänge EF der Deckfläche 8 cm, Höhe des Stumpfs 6 cm, Gesamthöhe der Verpackung 9 cm, 1 LE = 1 cm. Eckpunkte B(10 | 10 | 0), D(0 | 0 | 0), F(9 | 9 | 6), Spitze S(5 | 5 | 9)."
SK22 = "Schrägbild ohne Koordinatenachsen: unten die quadratische Grundfläche ABCD (A vorn links, B vorn rechts, C hinten rechts, D hinten links), darüber die kleinere quadratische Deckfläche EFGH (E über A, F über B, G über C, H über D), die Seitenkanten AE, BF, CG, DH laufen nach oben leicht zusammen; auf der Deckfläche sitzt die Pyramide mit der Spitze S über der Mitte. Verdeckte Kanten (an D und H) sind gestrichelt. Keine Maßangaben in der Abbildung."
SK22E = "Zweites Schrägbild desselben Körpers (ohne gestrichelte Kanten): auf den Seitenkanten AE, BF und CG sind in halber Stumpfhöhe die Punkte P1, P2 und P3 markiert. Dünne Linien verbinden A mit P2, P2 mit C, P1 mit B und B mit P3 – je zwei Drähte kreuzen sich auf den sichtbaren Seitenflächen ABFE und BCGF; P4 auf DH und die übrigen Drähte liegen verdeckt."
TAB31 = "Tabelle mit den Spalten Werk A, B, C, D und den Zeilen „Anteil an der Gesamtzahl“ (10 %, 30 %, 20 %, 40 %) und „Anteil der fehlerhaften Geräte“ (5 %, 3 %, 4 %, 2 %)."
ST31 = "Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %."
ST32 = "Ein Würfel W, durch Neubeschriftung aus einem Laplace-Würfel entstanden, trägt viermal die 2 und zweimal die 1. Glücksrad G1 hat zehn gleich große Sektoren: 4 rot, 4 blau, 2 weiß; Glücksrad G2 hat vier gleich große Sektoren: 2 rot, 1 blau, 1 schwarz. Ein gedrehtes Rad bleibt zufällig auf einem Sektor stehen, nie auf einer Grenze."
SK32 = "Abbildung neben dem Text: Würfelnetz W in Kreuzform mit den Feldern 2 (oben), 1, 2, 2, 2 (mittlere Reihe) und 1 (unten); Glücksrad G1 mit zehn gleichen Sektoren, im Uhrzeigersinn von oben links b, r, r, r, r, w, w, b, b, b (r rot, b blau, w weiß); Glücksrad G2 in vier Viertel geteilt: b oben links, r oben rechts, r unten links, s unten rechts (s schwarz). Über jedem Rad zeigt ein Pfeil oben links als Zeiger auf den Rand."
TAB32 = " Anlage Seite 8: Tabelle der summierten Binomialverteilung für n = 5, 10, 15, 20 und p = 0,05; 0,10; 1/6; 0,20; 0,25; 0,30; 1/3; 0,40; 0,45; 0,50 (vier Nachkommastellen, „0,“ weggelassen; für p > 0,5 von unten zu lesen)."

# ---- Aufgabe 1.1: Holzeisenbahn (Seite 2, 40 BE)
row(id="2017-be-gk-B1.1a", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="a", seite="2", punkte="9",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Lage und Art aller lokalen Extrempunkte bestimmen",
    typ_neben="Extrempunkt einem Punkt im Sachzusammenhang zuordnen",
    stichwoerter="Extrempunkte|zweite Ableitung|knickfreier Übergang|waagerechte Tangente",
    voraussetzungen="Ableitungen einer ganzrationalen Funktion bilden|x ausklammern und Nullprodukt anwenden|waagerechte Tangente als Ableitung null deuten",
    format="Rechnung|Begründung",
    operator="Ermitteln Sie|Weisen Sie nach|Begründen Sie",
    antwort="Zahl|Text",
    material="Skizze",
    skizze=SK11,
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="mittel",
    gegeben=ST11 + " In den oberen Eckpunkten A und B geht die Oberkante ohne Knick in die waagerechten Anschlussschienen über. Kontrollangabe: f′(x) = −3/500 · x² + 3/25 · x sowie A(0 | f(0)) bzw. B(20 | f(20)).",
    gesucht="Extrempunkte von f mit Nachweis ihrer Art; Begründung, warum die Extrempunkte mit den Eckpunkten A und B übereinstimmen müssen",
    verfahren="f′(x) = 0 setzen und x ausklammern: x · (−3/500 · x + 3/25) = 0 liefert x = 0 und x = 20. Mit f″(x) = −3/250 · x + 3/25 die Art bestimmen: f″(0) > 0 Tiefpunkt, f″(20) < 0 Hochpunkt. Knickfreier Übergang in waagerechte Schienen heißt Steigung null in A und B, also f′ = 0 dort – die Eckpunkte sind die Stellen mit waagerechter Tangente.",
    schritte="5",
    zahlenraum="ganz|Bruch",
    einheiten="cm",
    ergebnis="Tiefpunkt T(0 | 1) = A, Hochpunkt H(20 | 9) = B. Ohne Knick in waagerechte Schienen heißt: die Tangente an den Graphen ist in A und B waagerecht, f′ ist dort null; die einzigen solchen Stellen sind die Extremstellen 0 und 20.",
    zwischenergebnis="f″(x) = −3/250 · x + 3/25|f″(0) = 0,12|f″(20) = −0,12|f(20) = 9",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Nullstellen der Ableitung angeben, ohne die Art über f″ nachzuweisen, oder den knickfreien Übergang nur über gleiche Höhe statt über gleiche Steigung begründen",
    abhaengig_von="",
    bemerkung="Kontrollangabe f′ und die Lage von A und B durch eigene Rechnung bestätigt. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.1b", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="b", seite="2", punkte="6",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate über ein Intervall berechnen",
    typ_neben="Stelle mit lokaler gleich mittlerer Änderungsrate bestimmen",
    stichwoerter="mittlere Steigung|Differenzenquotient|lokale Steigung|quadratische Gleichung",
    voraussetzungen="Differenzenquotient bilden|quadratische Gleichung lösen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Skizze",
    skizze=SK11,
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="kurz",
    gegeben=ST11 + " Das Brückenteil reicht von A(0 | 1) bis B(20 | 9); f′(x) = −3/500 · x² + 3/25 · x.",
    gesucht="mittlere Steigung des Brückenteils; Stellen, an denen die lokale Steigung von f gleich der mittleren Steigung ist",
    verfahren="Mittlere Steigung als Differenzenquotient (f(20) − f(0))/20. Dann f′(x) = 0,4 setzen, mit −500/3 multiplizieren und die quadratische Gleichung x² − 20x + 200/3 = 0 mit der Lösungsformel lösen.",
    schritte="4",
    zahlenraum="dezimal|Bruch|Wurzel",
    einheiten="cm",
    ergebnis="Mittlere Steigung m = (9 − 1)/20 = 0,4. f′(x) = 0,4 an den Stellen x = 10 ± 10/√3, also x₁ ≈ 4,23 und x₂ ≈ 15,77.",
    zwischenergebnis="x² − 20x + 200/3 = 0|Diskriminante 100/3",
    niveau_geschaetzt="II",
    fehlerquelle="die mittlere Steigung als Mittelwert von f′(0) und f′(20) bilden oder nur eine der beiden Lösungen angeben",
    abhaengig_von="2017-be-gk-B1.1a",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.1c", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="c", seite="2", punkte="6",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Maximalen Neigungswinkel über die Wendestelle berechnen und mit einer Schranke vergleichen",
    typ_neben="",
    stichwoerter="größter Anstieg|Wendepunkt|Steigungswinkel|Grenzwinkel 32°",
    voraussetzungen="zweite Ableitung bilden|Steigung über den Arkustangens in einen Winkel umrechnen",
    format="Rechnung|Begründung",
    operator="Bestimmen Sie|Berechnen Sie|Entscheiden Sie",
    antwort="Zahl|Text",
    material="Skizze",
    skizze=SK11,
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="mittel",
    gegeben=ST11 + " f′(x) = −3/500 · x² + 3/25 · x. Für batteriebetriebene Lokomotiven darf der Anstiegswinkel an keiner Stelle größer als 32° sein; ein Nachweis mit hinreichender Bedingung ist nicht verlangt.",
    gesucht="Punkt mit dem größten Anstieg; maximaler Anstiegswinkel und Entscheidung, ob das 32°-Kriterium erfüllt ist",
    verfahren="Der größte Anstieg liegt, wo f′ maximal ist: f″(x) = −3/250 · x + 3/25 = 0 liefert x = 10. Den Punkt über f(10) angeben, die Steigung f′(10) berechnen und über tan α = f′(10) den Winkel bestimmen; mit 32° vergleichen.",
    schritte="4",
    zahlenraum="ganz|dezimal",
    einheiten="cm|°",
    ergebnis="Größter Anstieg im Wendepunkt W(10 | 5) mit f′(10) = 0,6; α = arctan 0,6 ≈ 31,0° < 32°, das Kriterium ist erfüllt.",
    zwischenergebnis="f″(x) = −3/250 · x + 3/25|f′(10) = 0,6|α ≈ 30,96°",
    niveau_geschaetzt="II",
    fehlerquelle="die Steigung 0,6 direkt mit 32 vergleichen, ohne sie in einen Winkel umzurechnen, oder den Hochpunkt als Punkt größten Anstiegs nennen",
    abhaengig_von="",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.1d", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="d", seite="2", punkte="5",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Volumen eines Körpers mit konstanter Tiefe aus der Fläche zwischen Graph und x-Achse berechnen",
    typ_neben="",
    stichwoerter="Querschnittsfläche|bestimmtes Integral|Tiefe|Volumen",
    voraussetzungen="Stammfunktion einer ganzrationalen Funktion bilden|bestimmtes Integral berechnen|Prismenvolumen als Grundfläche mal Tiefe",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Skizze",
    skizze=SK11,
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="kurz",
    gegeben=ST11 + " Das Brückenteil reicht von x = 0 bis x = 20 und hat eine Tiefe von 4 cm.",
    gesucht="Volumen des gesamten Brückenteils",
    verfahren="Die Querschnittsfläche ist die Fläche zwischen dem Graphen von f und der x-Achse über [0; 20]: Integral mit der Stammfunktion F(x) = −1/2000 · x⁴ + 1/50 · x³ + x berechnen. Das Bauteil ist ein Prisma mit dieser Grundfläche, also mit der Tiefe 4 cm multiplizieren.",
    schritte="3",
    zahlenraum="ganz|Bruch",
    einheiten="cm²|cm³",
    ergebnis="Querschnittsfläche ∫₀²⁰ f(x) dx = 100 cm², Volumen V = 4 · 100 = 400 cm³.",
    zwischenergebnis="F(20) − F(0) = −80 + 160 + 20 = 100",
    niveau_geschaetzt="II",
    fehlerquelle="die Tiefe vergessen und nur die Querschnittsfläche angeben oder über [0; 25] statt [0; 20] integrieren",
    abhaengig_von="2017-be-gk-B1.1a",
    bemerkung="Neuer Typ: die Liste kennt das Hochrechnen einer Integralfläche mit einer Breite nur für Wassermulden und Flächen zwischen Tangente und Graph. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.1e", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="e", seite="2", punkte="5",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Schnittwinkel zwischen Tangente und Gerade über die Anstiege berechnen",
    typ_neben="",
    stichwoerter="Tangenten|Steigungswinkel|Schnittwinkel|Grenzwinkel 25°",
    voraussetzungen="Ableitungswerte einsetzen|Steigung über den Arkustangens in einen Winkel umrechnen",
    format="Rechnung|Begründung",
    operator="Berechnen Sie|Beurteilen Sie",
    antwort="Zahl|Text",
    material="Skizze|Foto",
    skizze="Foto zweier Holzwaggons auf der Rampe des Brückenteils mit eingezeichnetem Koordinatensystem ohne Teilung: der Graph f verläuft vom flachen Beginn an der y-Achse ansteigend nach rechts oben; auf ihm sind P1 links unten und P2 rechts oben markiert. Die Tangente t1 an P1 verläuft flach ansteigend, die Tangente t2 an P2 steil; beide schneiden sich rechts von P1 unterhalb des Graphen, der Winkel α zwischen ihnen ist markiert.",
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="mittel",
    gegeben=ST11 + " f′(x) = −3/500 · x² + 3/25 · x. Der Neigungswinkel zwischen zwei angehängten Waggons darf nicht größer als 25° werden; untersucht werden die Tangenten t1 und t2 an den Graphen von f in P1(1,5 | f(1,5)) und P2(8,5 | f(8,5)).",
    gesucht="Schnittwinkel zwischen t1 und t2; Beurteilung, ob der Neigungswinkel zu groß wird",
    verfahren="Die Steigungen der Tangenten über f′(1,5) und f′(8,5) berechnen, beide Steigungswinkel über den Arkustangens bestimmen und den Schnittwinkel als Differenz der Steigungswinkel bilden; mit 25° vergleichen.",
    schritte="4",
    zahlenraum="dezimal",
    einheiten="°",
    ergebnis="f′(1,5) = 0,1665 mit α₁ ≈ 9,45°, f′(8,5) = 0,5865 mit α₂ ≈ 30,39°; Schnittwinkel α ≈ 20,9° < 25°, der Neigungswinkel wird nicht zu groß.",
    zwischenergebnis="α₁ ≈ 9,453°|α₂ ≈ 30,392°",
    niveau_geschaetzt="II",
    fehlerquelle="die Differenz der Steigungen statt der Steigungswinkel nehmen oder den Taschenrechner im Bogenmaß rechnen lassen",
    abhaengig_von="",
    bemerkung="Beide Geraden sind Tangenten an denselben Graphen; der Typ verlangt eine Tangente und eine gegebene Gerade, der Lösungsweg über die Differenz der Steigungswinkel ist derselbe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.1f", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="f", seite="2", punkte="9",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Ganzrationale Funktion dritten Grades aus Wert- und Steigungsbedingungen rekonstruieren",
    typ_neben="",
    stichwoerter="Steckbrief|Ansatz ax³ + bx² + c|Extrempunkte in den Eckpunkten|Gleichungssystem",
    voraussetzungen="Sachangaben in Bedingungen übersetzen|lineares Gleichungssystem mit zwei Unbekannten lösen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Term",
    material="Skizze",
    skizze=SK11,
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="mittel",
    gegeben="Ein verändertes Brückenteil der Holzeisenbahn soll 25 cm lang sein, links 1,5 cm und rechts 11,5 cm hoch; in beiden oberen Eckpunkten sollen wieder die Extrempunkte liegen. Die linke untere Ecke liegt im Koordinatenursprung, 1 LE = 1 cm. Das Profil wird durch g mit g(x) = ax³ + bx² + c modelliert.",
    gesucht="Funktionsgleichung von g",
    verfahren="Bedingungen: g(0) = 1,5 liefert c = 1,5; g′(0) = 0 gilt für den Ansatz ohne linearen Term von selbst; g′(25) = 0 und g(25) = 11,5 ergeben 1875a + 50b = 0 und 15 625a + 625b = 10. Aus der ersten b = −37,5a, eingesetzt −7812,5a = 10.",
    schritte="5",
    zahlenraum="dezimal|negativ",
    einheiten="cm",
    ergebnis="g(x) = −0,00128x³ + 0,048x² + 1,5 (a = −4/3125, b = 6/125, c = 3/2).",
    zwischenergebnis="c = 1,5|b = −37,5a|a = −0,00128|b = 0,048",
    niveau_geschaetzt="II",
    fehlerquelle="die Bedingung g′(0) = 0 als eigene Gleichung für einen nicht vorhandenen linearen Koeffizienten ansetzen oder die Höhe rechts als g(25) = 10 statt 11,5 nehmen",
    abhaengig_von="",
    bemerkung="Der vorgegebene Ansatz hat nur drei Koeffizienten; der Typ passt, weil der Lösungsweg (Bedingungen, lineares Gleichungssystem) derselbe ist. Eigene Rechnung, mit sympy bestätigt (Hochpunkt bei x = 25, Tiefpunkt bei x = 0).")

# ---- Aufgabe 1.2: Dachformen (Seite 3, 40 BE)
row(id="2017-be-gk-B1.2a", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="a", seite="3", punkte="11",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstelle und y-Achsenschnittpunkt eines Produkts mit e-Funktion angeben",
    typ_neben="Lage und Art aller lokalen Extrempunkte bestimmen",
    stichwoerter="Achsenschnittpunkte|Produkt mit e-Funktion|Extrempunkte|zweite Ableitung",
    voraussetzungen="Satz vom Nullprodukt|binomische Formel erkennen|Produktregel anwenden|quadratische Gleichung lösen",
    format="Rechnung",
    operator="Bestimmen Sie|Ermitteln Sie",
    antwort="Zahl",
    material="Foto",
    skizze=SK12,
    kontext="Architektur / Dach",
    textumfang="mittel",
    gegeben=ST12 + " Kontrollangabe: f′(x) = (−x² + 4x − 3) · e^(−x).",
    gesucht="Koordinaten der Schnittpunkte des Graphen von f mit den Koordinatenachsen; Art und Lage aller Extrempunkte des Graphen von f",
    verfahren="f(0) = 1 liefert den y-Achsenschnittpunkt; da e^(−x) > 0, ist f(x) = 0 genau für (x − 1)² = 0. Für die Extrempunkte −x² + 4x − 3 = 0 lösen (x = 1, x = 3) und die Art mit f″(x) = (x² − 6x + 7) · e^(−x) oder über den Vorzeichenwechsel von f′ bestimmen.",
    schritte="6",
    zahlenraum="ganz|Potenz|dezimal",
    einheiten="",
    ergebnis="Schnittpunkt mit der y-Achse (0 | 1), mit der x-Achse (1 | 0) (doppelte Nullstelle). Tiefpunkt T(1 | 0), Hochpunkt H(3 | 4e^(−3)) ≈ (3 | 0,199).",
    zwischenergebnis="f″(x) = (x² − 6x + 7) · e^(−x)|f″(1) = 2/e > 0|f″(3) = −2e^(−3) < 0",
    niveau_geschaetzt="I",
    fehlerquelle="eine Nullstelle des Faktors e^(−x) suchen oder die Nullstelle x = 1 wegen des Berührens nicht als Tiefpunkt erkennen",
    abhaengig_von="",
    bemerkung="Die Aufgabe fragt nach allen Extrempunkten des Graphen, der Hochpunkt bei x = 3 liegt außerhalb des Modellintervalls [0; 2]. Kontrollangabe f′ durch eigene Rechnung bestätigt. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.2b", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="b", seite="3", punkte="3",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen",
    typ_neben="",
    stichwoerter="Graph zeichnen|Wertetabelle|Intervall [0; 2]|Tiefpunkt",
    voraussetzungen="Funktionswerte mit e-Funktion berechnen|Koordinatensystem passend skalieren",
    format="Zeichnen",
    operator="Zeichnen Sie",
    antwort="Grafik",
    material="keins",
    skizze="Im Heft ist kein Koordinatensystem vorgegeben; die Darstellung ist Teil der Lösung. Gefordert ist der Graph von f über [0; 2]: fallend von (0 | 1) über (0,5 | 0,15) zum Tiefpunkt (1 | 0) auf der x-Achse, danach flach steigend über (1,5 | 0,06) bis (2 | 0,14).",
    kontext="Architektur / Dach",
    textumfang="kurz",
    gegeben=ST12 + " Bekannt sind der Schnittpunkt (0 | 1) mit der y-Achse und der Tiefpunkt T(1 | 0).",
    gesucht="Graph von f im Intervall [0; 2]",
    verfahren="Eine Wertetabelle mit Schrittweite 0,25 oder 0,5 anlegen, die markanten Punkte (0 | 1) und T(1 | 0) eintragen und den Graphen glatt verbinden.",
    schritte="2",
    zahlenraum="dezimal",
    einheiten="",
    ergebnis="Kennzeichnende Punkte: (0 | 1), (0,25 | 0,44), (0,5 | 0,15), (0,75 | 0,03), T(1 | 0), (1,25 | 0,02), (1,5 | 0,06), (1,75 | 0,10), (2 | 0,14); der Graph berührt die x-Achse in T und steigt danach nur schwach.",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="den Graphen bei x = 1 mit einem Knick statt mit waagerechter Tangente zeichnen oder unter die x-Achse führen",
    abhaengig_von="2017-be-gk-B1.2a",
    bemerkung="Das Heft gibt kein Koordinatensystem vor; der Typ nennt ein vorgegebenes, der Lösungsweg (Punkte berechnen, eintragen, verbinden) ist derselbe. Das Feld skizze beschreibt die vom Prüfling zu erstellende Zeichnung, nicht vorhandenes Material. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.2c", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="c", seite="3", punkte="5",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen",
    typ_neben="",
    stichwoerter="maximale Steigung|Nullstelle der zweiten Ableitung|notwendige Bedingung|Wurzel",
    voraussetzungen="zweite Ableitung mit der Produktregel bilden|quadratische Gleichung lösen|Lösung im Intervall auswählen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Foto",
    skizze=SK12,
    kontext="Architektur / Dach",
    textumfang="kurz",
    gegeben=ST12 + " f′(x) = (−x² + 4x − 3) · e^(−x). Im Intervall [0; 2] gibt es eine Stelle x_P, an der der Graph von f die maximale positive Steigung hat; die notwendige Bedingung genügt.",
    gesucht="Wert von x_P und Steigung des Graphen von f an dieser Stelle",
    verfahren="Die Steigung f′ wird maximal, wo f″(x) = (x² − 6x + 7) · e^(−x) null ist: x² − 6x + 7 = 0 liefert x = 3 ± √2, im Intervall nur x_P = 3 − √2. Die Steigung durch Einsetzen in f′ berechnen.",
    schritte="4",
    zahlenraum="dezimal|Wurzel|Potenz",
    einheiten="",
    ergebnis="x_P = 3 − √2 ≈ 1,586; f′(x_P) ≈ 0,170.",
    zwischenergebnis="f″(x) = (x² − 6x + 7) · e^(−x)|3 + √2 ≈ 4,41 liegt außerhalb|f′(2) ≈ 0,135",
    niveau_geschaetzt="II",
    fehlerquelle="f′(x) = 0 statt f″(x) = 0 setzen oder die Lösung 3 + √2 außerhalb des Intervalls nehmen",
    abhaengig_von="",
    bemerkung="Der Typ nennt die kleinste oder größte Tangentensteigung; hier die größte positive. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.2d", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="d", seite="3", punkte="5",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion durch Ableiten nachweisen",
    typ_neben="Fläche: Fläche zwischen Graph und Koordinatenachsen berechnen|Fläche: Flächenmaßstab eines Modells auf eine Realfläche anwenden",
    stichwoerter="Stammfunktion|Produktregel|Trennwand|Flächenmaßstab",
    voraussetzungen="Produktregel anwenden|bestimmtes Integral über eine Stammfunktion auswerten|Längenmaßstab quadrieren",
    format="Begründung|Rechnung",
    operator="Zeigen Sie|Berechnen Sie",
    antwort="Text|Zahl",
    material="Foto",
    skizze=SK12,
    kontext="Architektur / Dach",
    textumfang="mittel",
    gegeben=ST12 + " Unter einem Dachelement soll eine Trennwand errichtet werden, die im Intervall [0; 1] durch den Graphen von f und die x-Achse begrenzt ist. F(x) = (−x² − 1) · e^(−x).",
    gesucht="Nachweis, dass F eine Stammfunktion von f ist; Flächeninhalt der Trennwand in m²",
    verfahren="F mit der Produktregel ableiten: F′(x) = −2x · e^(−x) − (−x² − 1) · e^(−x) = (x² − 2x + 1) · e^(−x) = f(x). Dann ∫₀¹ f(x) dx = F(1) − F(0) berechnen; 1 LE = 10 m heißt 1 FE = 100 m².",
    schritte="4",
    zahlenraum="dezimal|Potenz",
    einheiten="m|m²",
    ergebnis="F′ = f. Fläche 1 − 2/e ≈ 0,264 FE, also etwa 26,4 m².",
    zwischenergebnis="F(1) = −2/e|F(0) = −1|1 − 2/e ≈ 0,2642",
    niveau_geschaetzt="II",
    fehlerquelle="mit 10 statt 100 umrechnen oder beim Ableiten von F das Vorzeichen des e-Faktors verlieren",
    abhaengig_von="",
    bemerkung="Die Trennwand wird links von der y-Achse begrenzt, rechts berührt der Graph bei x = 1 die x-Achse – Fläche zwischen Graph und beiden Koordinatenachsen. Eigene Rechnung, mit sympy bestätigt (26,42 m²).")
row(id="2017-be-gk-B1.2e", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="e", seite="3", punkte="9",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen",
    typ_neben="Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen|Fläche: Flächenmaßstab eines Modells auf eine Realfläche anwenden",
    stichwoerter="Tangente in R(0 | 1)|Achsendreieck|eingesparte Wandfläche|Flächenmaßstab",
    voraussetzungen="Ableitung an einer Stelle auswerten|Nullstelle einer linearen Funktion|Dreiecksfläche berechnen|Längenmaßstab quadrieren",
    format="Rechnung",
    operator="Ermitteln Sie|Berechnen Sie",
    antwort="Term|Zahl",
    material="Foto",
    skizze=SK12,
    kontext="Architektur / Dach",
    textumfang="mittel",
    gegeben=ST12 + " f′(x) = (−x² + 4x − 3) · e^(−x). Die Trennwand unter dem Graphen über [0; 1] hat etwa 26,4 m². Statt ihrer soll eine kleinere Wand verwendet werden, die durch die Koordinatenachsen und die Tangente an den Graphen von f im Punkt R(0 | 1) begrenzt ist.",
    gesucht="Gleichung der Tangente in R; eingesparte Wandfläche in m²",
    verfahren="Steigung f′(0) = −3, also t(x) = −3x + 1. Die Tangente schneidet die x-Achse bei x = 1/3; das Achsendreieck hat den Inhalt 1/2 · 1 · 1/3 = 1/6 FE = 100/6 m². Die Einsparung ist die Differenz zur Trennwandfläche aus d.",
    schritte="4",
    zahlenraum="Bruch|dezimal",
    einheiten="m²",
    ergebnis="t(x) = −3x + 1; kleinere Wand 1/6 FE ≈ 16,7 m², eingespart werden 100 · (5/6 − 2/e) ≈ 9,8 m².",
    zwischenergebnis="Nullstelle der Tangente x = 1/3|Dreieck 1/6 FE|Trennwand 1 − 2/e FE",
    niveau_geschaetzt="II",
    fehlerquelle="die eingesparte Fläche mit gerundeten Zwischenwerten (26,4 − 17) statt exakt berechnen oder den Flächenmaßstab vergessen",
    abhaengig_von="2017-be-gk-B1.2d",
    bemerkung="Mit gerundeten Zwischenwerten 26,4 m² − 16,7 m² ≈ 9,7 m²; exakt 9,76 m². Die Tangente liegt über [0; 1/3] unterhalb des Graphen (f(1/3) ≈ 0,32), die kleinere Wand liegt also ganz in der Trennwand. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B1.2f", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="f", seite="3", punkte="7",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Existenz einer quadratischen Funktion zu vier Wert- und Steigungsbedingungen über das überbestimmte Gleichungssystem untersuchen",
    typ_neben="",
    stichwoerter="quadratische Funktion|tangential|vier Bedingungen|überbestimmtes Gleichungssystem",
    voraussetzungen="Berühren als gleichen Funktionswert und gleiche Steigung deuten|lineares Gleichungssystem lösen|Widerspruch erkennen",
    format="Kurzantwort|Rechnung|Begründung",
    operator="Geben Sie an|Untersuchen Sie",
    antwort="Term|Text",
    material="Foto",
    skizze=SK12,
    kontext="Architektur / Dach",
    textumfang="kurz",
    gegeben=ST12 + " f′(x) = (−x² + 4x − 3) · e^(−x), also f′(0) = −3 und f′(1) = 0. Der Graph einer quadratischen Funktion p soll in den Punkten R(0 | 1) und S(1 | 0) tangential zum Graphen von f verlaufen.",
    gesucht="vier Bedingungen für p; Untersuchung, ob es eine solche Funktion p gibt",
    verfahren="Ansatz p(x) = ax² + bx + c. Bedingungen p(0) = 1, p′(0) = −3, p(1) = 0, p′(1) = 0. Die ersten drei liefern c = 1, b = −3, a = 2; die vierte prüfen: p′(1) = 2a + b = 1 ≠ 0.",
    schritte="4",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="p(0) = 1, p′(0) = −3, p(1) = 0, p′(1) = 0. Aus den ersten drei folgt p(x) = 2x² − 3x + 1, damit p′(1) = 1 ≠ 0 – das Gleichungssystem ist widersprüchlich, eine solche Funktion p gibt es nicht.",
    zwischenergebnis="c = 1|b = −3|a = 2|p′(1) = 1",
    niveau_geschaetzt="III",
    fehlerquelle="nur drei Bedingungen verwenden und die gefundene Parabel als Lösung angeben, ohne die vierte zu prüfen",
    abhaengig_von="2017-be-gk-B1.2a",
    bemerkung="Neuer Typ: die vorhandenen Rekonstruktionstypen enden mit einer Funktionsgleichung; hier ist das System aus vier Bedingungen für drei Koeffizienten überbestimmt und das Ergebnis eine Existenzaussage (nein). Eigene Rechnung, mit sympy bestätigt (keine Lösung).")

# ---- Aufgabe 2.1: Startbahn Ost (Seite 4, 20 BE)
row(id="2017-be-gk-B2.1a", block="B", aufgabe="2.1", titel="Startbahn Ost", teilaufgabe="a", seite="4", punkte="7",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Geradengleichung durch zwei Punkte aufstellen",
    typ_neben="Körper: Geschwindigkeit entlang einer Kante aus Kantenlänge und Zeit berechnen|Schnittwinkel zwischen Gerade und Ebene über Richtungs- und Normalenvektor berechnen",
    stichwoerter="Richtungsvektor|Flugbahn|Geschwindigkeit in km/h|Startwinkel",
    voraussetzungen="Verbindungsvektor bilden|Betrag eines Vektors berechnen|m/s in km/h umrechnen|Normalenvektor der x-y-Ebene kennen",
    format="Kurzantwort|Rechnung",
    operator="Geben Sie an|Berechnen Sie",
    antwort="Term|Zahl",
    material="Foto",
    skizze=SK21,
    kontext="Luftfahrt / Flugbahn",
    textumfang="mittel",
    gegeben=ST21,
    gesucht="Richtungsvektor r = P0P1 und Gleichung der Geraden g der Flugbahn unmittelbar nach dem Start; Länge der in einer Sekunde zurückgelegten Strecke; Startgeschwindigkeit in km/h; Startwinkel",
    verfahren="r = P1 − P0 bilden und g mit Stützpunkt P0 aufschreiben. Die Strecke ist |r|, das ist zugleich die Geschwindigkeit in m/s; mit 3,6 multiplizieren. Der Startwinkel ist der Winkel zwischen g und der x-y-Ebene: sin α = |r · (0 | 0 | 1)|/|r|.",
    schritte="5",
    zahlenraum="ganz|dezimal|Wurzel",
    einheiten="m|m/s|km/h|°",
    ergebnis="r = (60 | 11 | 30); g: x = (1140 | 240 | 0) + t · (60 | 11 | 30). Strecke |r| = √4621 ≈ 68,0 m, Geschwindigkeit ≈ 244,7 km/h, Startwinkel α ≈ 26,2°.",
    zwischenergebnis="|r| ≈ 67,98 m|sin α = 30/√4621",
    niveau_geschaetzt="II",
    fehlerquelle="den Startwinkel mit dem Richtungsvektor der Startbahn statt mit der Ebene berechnen oder beim Umrechnen durch 3,6 teilen",
    abhaengig_von="",
    bemerkung="Die Geschwindigkeit ist die Länge des Verbindungsvektors je Sekunde; der Nebentyp nennt eine Kante, hier ist es der Flugweg in einer Sekunde. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B2.1b", block="B", aufgabe="2.1", titel="Startbahn Ost", teilaufgabe="b", seite="4", punkte="5",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen",
    typ_neben="",
    stichwoerter="Verlängerung der Startbahn|Entfernung 7 km|Richtungsvektor in der x-y-Ebene|Rundung",
    voraussetzungen="Richtung der Startbahn als Projektion des Flugrichtungsvektors erkennen|Betrag eines Vektors berechnen|km in m umrechnen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Foto",
    skizze=SK21,
    kontext="Luftfahrt / Flugbahn",
    textumfang="kurz",
    gegeben=ST21 + " In gerader Verlängerung der Startbahn liegt 7 km von P0 entfernt das Rathaus Pankow; auch Zwischenergebnisse sind ganzzahlig zu runden. Kontrollergebnis: R(8040 | 1505 | 0).",
    gesucht="Koordinaten des Rathauses R",
    verfahren="Die Startbahn hat die Richtung (60 | 11 | 0) (Flugrichtung ohne Höhenanteil) mit der Länge 61. 7000 m entsprechen 7000/61 ≈ 114,75, gerundet 115 Vielfachen dieses Vektors; R = P0 + 115 · (60 | 11 | 0).",
    schritte="4",
    zahlenraum="ganz",
    einheiten="m|km",
    ergebnis="R(8040 | 1505 | 0)",
    zwischenergebnis="|(60 | 11 | 0)| = 61|7000/61 ≈ 114,75 ≈ 115",
    niveau_geschaetzt="II",
    fehlerquelle="den Flugrichtungsvektor mit Höhenanteil statt der Startbahnrichtung verwenden oder mit 7 statt 7000 rechnen",
    abhaengig_von="2017-be-gk-B2.1a",
    bemerkung="Kontrollergebnis durch eigene Rechnung bestätigt; es folgt nur mit dem auf 115 gerundeten Faktor (ungerundet R ≈ (8025,3 | 1502,3 | 0)), darum die Rundungsanweisung. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B2.1c", block="B", aufgabe="2.1", titel="Startbahn Ost", teilaufgabe="c", seite="4", punkte="4",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Höhenunterschied zweier übereinanderliegender Punkte auf Seilgeraden bestimmen",
    typ_neben="",
    stichwoerter="Richtungswechsel|Überfliegen|gleiche x- und y-Koordinaten|Flughöhe",
    voraussetzungen="Geradengleichung aus Punkt und Richtungsvektor aufstellen|Parameter aus einer Koordinate bestimmen und mit einer zweiten prüfen",
    format="Begründung|Rechnung",
    operator="Weisen Sie nach|Bestimmen Sie",
    antwort="Text|Zahl",
    material="Foto",
    skizze=SK21,
    kontext="Luftfahrt / Flugbahn",
    textumfang="mittel",
    gegeben="Ein Jet ändert 10 Sekunden nach dem Start im Punkt P10(1740 | 350 | 300) seine Geschwindigkeit und fliegt weniger steil mit dem Richtungsvektor r_neu = (90 | 16,5 | 4,5) geradlinig weiter. Das Rathaus Pankow liegt in R(8040 | 1505 | 0) in der x-y-Ebene, 1 LE = 1 m.",
    gesucht="rechnerischer Nachweis, dass der Jet das Rathaus überfliegt; Höhe, in der das Rathaus überflogen wird",
    verfahren="Neue Flugbahn h: x = (1740 | 350 | 300) + s · (90 | 16,5 | 4,5). Überfliegen heißt: ein Punkt von h hat dieselbe x- und y-Koordinate wie R. Aus 1740 + 90s = 8040 folgt s = 70; die y-Koordinate 350 + 70 · 16,5 = 1505 stimmt. Die Höhe ist die z-Koordinate 300 + 70 · 4,5.",
    schritte="4",
    zahlenraum="ganz|dezimal",
    einheiten="m",
    ergebnis="Mit s = 70 ist der Punkt (8040 | 1505 | 615) auf der Flugbahn senkrecht über R; der Jet überfliegt das Rathaus in 615 m Höhe.",
    zwischenergebnis="s = 70|y = 1505",
    niveau_geschaetzt="II",
    fehlerquelle="eine volle Punktprobe mit z = 0 durchführen und aus dem Widerspruch schließen, der Jet treffe das Rathaus nicht",
    abhaengig_von="2017-be-gk-B2.1b",
    bemerkung="Der Typ („übereinanderliegende Punkte“: gleiche x- und y-Koordinaten, Parameter, Höhe) trägt hier den Überflug eines Bodenpunkts; das Etikett nennt Seilgeraden (Vorschlag im Bericht). P10 = P0 + 10 · r bestätigt. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B2.1d", block="B", aufgabe="2.1", titel="Startbahn Ost", teilaufgabe="d", seite="4", punkte="4",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Gerade und Ebene: Parallelität einer Geraden zu einer Ebene über das Skalarprodukt von Richtungs- und Normalenvektor nachweisen",
    typ_neben="Schnittpunkt einer Ebene mit einer senkrechten Kante berechnen",
    stichwoerter="Wolkendecke|Normalenvektor|Skalarprodukt null|Sichtbarkeit",
    voraussetzungen="Normalenvektor aus der Koordinatengleichung ablesen|Skalarprodukt berechnen|Punktprobe in einer Ebene",
    format="Begründung|Rechnung",
    operator="Weisen Sie nach|Untersuchen Sie",
    antwort="Text|Zahl",
    material="Foto",
    skizze=SK21,
    kontext="Luftfahrt / Flugbahn",
    textumfang="mittel",
    gegeben="Die untere Begrenzung einer dichten Wolkendecke liegt in der Ebene E: x − 20z = −1560. Die neue Flugbahn des Jets ist h: x = (1740 | 350 | 300) + s · (90 | 16,5 | 4,5); er überfliegt das Rathaus R(8040 | 1505 | 0) in 615 m Höhe. Der Bürgermeister schaut vom Rathaus in dem Moment nach oben, in dem der Jet genau darüber ist; 1 LE = 1 m.",
    gesucht="Nachweis, dass die neue Flugbahn parallel zur Wolkenuntergrenze verläuft; Untersuchung, ob der Bürgermeister den Jet sehen kann oder nur die Wolkendecke",
    verfahren="Normalenvektor n = (1 | 0 | −20) von E; r_neu · n = 90 − 90 = 0, also ist h parallel zu E (P10 erfüllt die Gleichung nicht, h liegt nicht in E). Über dem Rathaus x = 8040 in E einsetzen: 8040 − 20z = −1560 liefert die Höhe der Wolkenuntergrenze; mit der Flughöhe 615 m vergleichen.",
    schritte="4",
    zahlenraum="ganz|negativ",
    einheiten="m",
    ergebnis="r_neu · n = 0, die Flugbahn ist parallel zur Wolkenuntergrenze (echt parallel, 1740 − 6000 = −4260 ≠ −1560). Über dem Rathaus liegt die Wolkenuntergrenze in 480 m Höhe, der Jet fliegt in 615 m, also oberhalb – der Bürgermeister sieht nur die Wolkendecke.",
    zwischenergebnis="n = (1 | 0 | −20)|z = 480",
    niveau_geschaetzt="II",
    fehlerquelle="Richtungsvektor und Normalenvektor auf Kollinearität statt auf Orthogonalität prüfen oder die Wolkenhöhe über P10 statt über dem Rathaus berechnen",
    abhaengig_von="2017-be-gk-B2.1c",
    bemerkung="Neuer Typ: die Liste kennt die Parallelität von Gerade und Ebene nur für Scharen (Parameter bestimmen) und für Koordinatenebenen. Eigene Rechnung, mit sympy bestätigt.")

# ---- Aufgabe 2.2: Schokotrüffel (Seite 5, 20 BE)
row(id="2017-be-gk-B2.2a", block="B", aufgabe="2.2", titel="Schokotrüffel", teilaufgabe="a", seite="5", punkte="2",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Eckpunkte eines Pyramidenstumpfs aus Symmetrie und Kantenlängen angeben",
    typ_neben="",
    stichwoerter="Pyramidenstumpf|Eckpunkte|Symmetrieachse|Deckfläche",
    voraussetzungen="Lage der Grundfläche aus B und D erschließen|Mittelachse des Stumpfs nutzen",
    format="Kurzantwort",
    operator="Geben Sie an",
    antwort="Zahl",
    material="Körper",
    skizze=SK22,
    kontext="Verpackung",
    textumfang="kurz",
    gegeben=ST22,
    gesucht="Koordinaten der Eckpunkte A, E und H",
    verfahren="BD ist Diagonale der Grundfläche mit der Kantenlänge 10, also A(10 | 0 | 0) und C(0 | 10 | 0). Die Deckfläche liegt in 6 cm Höhe, ist 8 cm breit und sitzt mittig über dem Mittelpunkt (5 | 5): ihre Ecken haben die x- und y-Koordinaten 1 oder 9, passend zur Lage von F(9 | 9 | 6).",
    schritte="2",
    zahlenraum="ganz",
    einheiten="cm",
    ergebnis="A(10 | 0 | 0), E(9 | 1 | 6), H(1 | 1 | 6)",
    zwischenergebnis="Mittelachse x = 5, y = 5|C(0 | 10 | 0)|G(1 | 9 | 6)",
    niveau_geschaetzt="I",
    fehlerquelle="E senkrecht über A mit (10 | 0 | 6) ansetzen und die Verjüngung des Stumpfs übersehen",
    abhaengig_von="",
    bemerkung="Neuer Typ: der vorhandene Typ für Prismen gewinnt die Deckfläche durch Verschieben, beim Stumpf kommt sie aus der Mittelachse und der kleineren Kantenlänge. Eigene Rechnung, Lage aller Ecken mit sympy geprüft.")
row(id="2017-be-gk-B2.2b", block="B", aufgabe="2.2", titel="Schokotrüffel", teilaufgabe="b", seite="5", punkte="4",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen",
    typ_neben="",
    stichwoerter="Seitenwand ABFE|Normalenvektor|Kreuzprodukt|Koordinatenform",
    voraussetzungen="Spannvektoren bilden|Normalenvektor über Kreuzprodukt oder Skalarprodukte bestimmen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Term",
    material="Körper",
    skizze=SK22,
    kontext="Verpackung",
    textumfang="kurz",
    gegeben=ST22 + " A(10 | 0 | 0), E(9 | 1 | 6). Kontrollangabe: E1: 6x + z = 60.",
    gesucht="Gleichung der Ebene E1, in der die Seitenwand ABFE liegt, in Koordinatenform",
    verfahren="Spannvektoren AB = (0 | 10 | 0) und AF = (−1 | 9 | 6); Normalenvektor AB × AF = (60 | 0 | 10), gekürzt (6 | 0 | 1). Die Konstante aus A: 6 · 10 + 0 = 60; Probe mit E und F.",
    schritte="3",
    zahlenraum="ganz|negativ",
    einheiten="",
    ergebnis="E1: 6x + z = 60",
    zwischenergebnis="n = (6 | 0 | 1)",
    niveau_geschaetzt="I",
    fehlerquelle="einen Normalenvektor wählen, der nur zu einem der Spannvektoren senkrecht steht, oder die Konstante mit einem Punkt außerhalb der Wand bestimmen",
    abhaengig_von="2017-be-gk-B2.2a",
    bemerkung="Kontrollangabe durch eigene Rechnung bestätigt (A, B, E, F erfüllen 6x + z = 60). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B2.2c", block="B", aufgabe="2.2", titel="Schokotrüffel", teilaufgabe="c", seite="5", punkte="5",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Neigungswinkel einer Ebene gegen eine Koordinatenebene über die Normalenvektoren berechnen",
    typ_neben="Streckenlänge im Raum berechnen",
    stichwoerter="Neigungswinkel der Seitenwand|Normalenvektoren|größter Abstand|Diagonale",
    voraussetzungen="Winkelformel für Normalenvektoren|Betrag eines Vektors|Eckpunkte als Kandidaten für den größten Abstand erkennen",
    format="Rechnung",
    operator="Ermitteln Sie|Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze=SK22,
    kontext="Verpackung",
    textumfang="kurz",
    gegeben=ST22 + " A(10 | 0 | 0), C(0 | 10 | 0), E(9 | 1 | 6), G(1 | 9 | 6), H(1 | 1 | 6); die Seitenwand ABFE liegt in E1: 6x + z = 60, die Grundfläche ABCD in der x-y-Ebene.",
    gesucht="Größe des Winkels γ zwischen Seitenwand ABFE und Grundfläche ABCD; größter Abstand zweier Punkte innerhalb der Verpackung",
    verfahren="cos γ = |(6 | 0 | 1) · (0 | 0 | 1)| / (√37 · 1) = 1/√37. Der größte Abstand liegt zwischen zwei Ecken des Körpers; die Längen der Grundflächendiagonale AC, der Raumdiagonalen wie DF und der Strecken zur Spitze vergleichen.",
    schritte="4",
    zahlenraum="dezimal|Wurzel",
    einheiten="cm|°",
    ergebnis="γ ≈ 80,5°. Der größte Abstand ist die Diagonale der Grundfläche: |AC| = |BD| = 10√2 ≈ 14,14 cm (die Raumdiagonale DF ist mit √198 ≈ 14,07 cm etwas kürzer).",
    zwischenergebnis="cos γ = 1/√37 ≈ 0,1644|γ ≈ 80,54°|√198 ≈ 14,07|√131 ≈ 11,45 (A bis S)",
    niveau_geschaetzt="II",
    fehlerquelle="die Raumdiagonale DF als größten Abstand nehmen, weil sie über die Höhe führt, obwohl die Grundflächendiagonale beim sich verjüngenden Stumpf länger ist",
    abhaengig_von="2017-be-gk-B2.2b",
    bemerkung="Beide Werte runden auf 14,1 cm; streng ist die Grundflächendiagonale mit 14,14 cm die längste Strecke. Eigene Rechnung, mit sympy bestätigt (alle Eckenabstände verglichen).")
row(id="2017-be-gk-B2.2d", block="B", aufgabe="2.2", titel="Schokotrüffel", teilaufgabe="d", seite="5", punkte="4",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen",
    typ_neben="",
    stichwoerter="Deckel|Seitendreiecke|Seitenhöhe|Goldfolie",
    voraussetzungen="Pyramidenhöhe aus den Koordinaten ablesen|Satz des Pythagoras|Dreiecksfläche",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze=SK22,
    kontext="Verpackung",
    textumfang="kurz",
    gegeben=ST22 + " Die vier Seitenflächen des pyramidenförmigen Deckels über der Deckfläche EFGH (Kantenlänge 8 cm, in 6 cm Höhe) werden mit Goldfolie überzogen; die Spitze liegt in 9 cm Höhe.",
    gesucht="benötigte Goldfolie in cm² für einen Deckel",
    verfahren="Pyramidenhöhe 9 − 6 = 3 cm; Seitenhöhe eines Dreiecks über der halben Kante 4 cm mit Pythagoras √(3² + 4²) = 5 cm. Vier Dreiecke mit Grundseite 8 cm und Höhe 5 cm.",
    schritte="3",
    zahlenraum="ganz",
    einheiten="cm|cm²",
    ergebnis="Für einen Deckel werden 4 · 1/2 · 8 · 5 = 80 cm² Goldfolie benötigt.",
    zwischenergebnis="Pyramidenhöhe 3 cm|Seitenhöhe 5 cm",
    niveau_geschaetzt="II",
    fehlerquelle="die Pyramidenhöhe 3 cm statt der Seitenhöhe 5 cm als Dreieckshöhe nehmen oder die Deckfläche EFGH mitzählen",
    abhaengig_von="2017-be-gk-B2.2a",
    bemerkung="Gefragt ist nur die Mantelfläche (ohne die Grundfläche des Deckels); der Typ nennt die Oberfläche, der Lösungsweg über die Seitenhöhe ist derselbe. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B2.2e", block="B", aufgabe="2.2", titel="Schokotrüffel", teilaufgabe="e", seite="5", punkte="5",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Körper: Gesamtlänge der Dachkanten einer Pyramide mit Zuschlag berechnen",
    typ_neben="Punkt: Mittelpunkt einer Strecke im Raum bestimmen",
    stichwoerter="Messingdraht|Kantenmittelpunkt|Streckenlänge|Gesamtlänge",
    voraussetzungen="Punkt in halber Höhe als Kantenmitte erkennen|Betrag eines Verbindungsvektors|Symmetrie der vier Seitenflächen nutzen",
    format="Begründung|Rechnung",
    operator="Zeigen Sie",
    antwort="Text|Zahl",
    material="Körper",
    skizze=SK22E,
    kontext="Verpackung",
    textumfang="mittel",
    gegeben=ST22 + " A(10 | 0 | 0), E(9 | 1 | 6). Die vier großen Seitenflächen des Stumpfs werden durch Messingdraht verstärkt: der Punkt P1 auf der Kante AE wird mit den Ecken D und B verbunden, P2, P3 und P4 auf BF, CG und DH ebenso mit den entsprechenden Ecken. P1 bis P4 liegen 3 cm über der Grundfläche.",
    gesucht="Nachweis, dass 80 cm Draht pro Verpackung ausreichen",
    verfahren="P1 liegt in halber Stumpfhöhe auf AE, ist also die Kantenmitte (9,5 | 0,5 | 3). |P1D| und |P1B| als Beträge der Verbindungsvektoren berechnen; aus Symmetrie sind alle acht Drähte gleich lang. Gesamtlänge 8 · |P1D| mit 80 cm vergleichen.",
    schritte="4",
    zahlenraum="dezimal|Wurzel",
    einheiten="cm",
    ergebnis="P1(9,5 | 0,5 | 3); |P1D| = |P1B| = √99,5 ≈ 9,97 cm; acht Drähte zusammen 8 · √99,5 = 4√398 ≈ 79,8 cm < 80 cm, der Draht reicht.",
    zwischenergebnis="P1D = (−9,5 | −0,5 | −3)|√99,5 ≈ 9,975",
    niveau_geschaetzt="II",
    fehlerquelle="nur vier statt acht Drähte zählen oder P1 senkrecht über A mit (10 | 0 | 3) ansetzen",
    abhaengig_von="2017-be-gk-B2.2a",
    bemerkung="Die Lage von P1 auf der Kante AE und die Zahl von zwei Drähten je Punkt stehen im Text und in der zweiten Abbildung. Der Typ nennt Dachkanten mit Zuschlag; der Lösungsweg (Länge als Vektorbetrag, mit der Anzahl hochrechnen, mit einer Vorgabe vergleichen) ist derselbe. Eigene Rechnung, mit sympy bestätigt.")

# ---- Aufgabe 3.1: Smartphone (Seite 6, 20 BE) – Poolaufgabe 2017 grundlegend Teil B Stochastik WTR 1
row(id="2017-be-gk-B3.1a", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="a", seite="6", punkte="2",
    afb_amtlich="I",
    leitidee="Stochastik", thema="Kombinatorik",
    typ="Anzahl ungeordneter Auswahlen ohne Wiederholung über den Binomialkoeffizienten berechnen",
    typ_neben="",
    stichwoerter="vier aus sechs Farben|Reihenfolge ohne Bedeutung|Binomialkoeffizient",
    voraussetzungen="Binomialkoeffizient als Anzahl der Teilmengen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Handel / Smartphones",
    textumfang="kurz",
    gegeben="Ein Händler erhält eine Lieferung neuer Smartphones in sechs verschiedenen Farben. Für die Auslage einiger Geräte im Schaufenster sollen vier Farben ausgewählt werden.",
    gesucht="Anzahl der Möglichkeiten für diese Auswahl",
    verfahren="Ungeordnete Auswahl von 4 aus 6 ohne Wiederholung: Binomialkoeffizient (6 über 4).",
    schritte="1",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="(6 über 4) = 15 (amtlich)",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="geordnet zählen (6 · 5 · 4 · 3 = 360)",
    abhaengig_von="",
    bemerkung="Dublette von: 2017MgrundlegendBStochastikWTR1-1a. AB amtlich: I. Wortgleich mit der Poolaufgabe (Teilaufgabe 1 a, gleiche BE). Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy.")
row(id="2017-be-gk-B3.1b", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="b", seite="6", punkte="3",
    afb_amtlich="I",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Ziehen ohne Zurücklegen: Wahrscheinlichkeit für ausschließlich eine Sorte beim mehrfachen Ziehen als Produkt berechnen",
    typ_neben="",
    stichwoerter="50 Geräte, 3 fehlerhaft|10 ausgewählt|keines fehlerhaft|Gegenereignis",
    voraussetzungen="Lotto-Modell mit Binomialkoeffizienten|Gegenereignis „mindestens eines“",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Handel / Smartphones",
    textumfang="mittel",
    gegeben="Eine Lieferung neuer Smartphones umfasst 50 Geräte, davon sind drei fehlerhaft. Aus der Lieferung werden zehn Geräte zufällig ausgewählt. A: Von den zehn ausgewählten Geräten ist keines fehlerhaft. B: Von den zehn ausgewählten Geräten ist mindestens eines fehlerhaft.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="P(A) als Quotient (47 über 10)/(50 über 10) (alle zehn aus den 47 fehlerfreien, ohne Zurücklegen) oder als Produkt 47/50 · 46/49 · … · 38/41; P(B) = 1 − P(A).",
    schritte="2",
    zahlenraum="Bruch|Prozent|dezimal",
    einheiten="",
    ergebnis="P(A) = (47 über 10)/(50 über 10) ≈ 50,4 %, P(B) = 1 − P(A) ≈ 49,6 % (amtlich)",
    zwischenergebnis="P(A) = 247/490",
    niveau_geschaetzt="I",
    fehlerquelle="mit Zurücklegen rechnen (0,94^10 ≈ 53,9 %)",
    abhaengig_von="",
    bemerkung="Dublette von: 2017MgrundlegendBStochastikWTR1-1b. AB amtlich: I. Wortgleich mit der Poolaufgabe (Teilaufgabe 1 b, gleiche BE; der Pool setzt die Ereignisse in Anführungszeichen). Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy (247/490).")
row(id="2017-be-gk-B3.1c", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="c", seite="6", punkte="2",
    afb_amtlich="I|II",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Totale Wahrscheinlichkeit über die Pfadregeln nachweisen",
    typ_neben="",
    stichwoerter="Werksanteil mal Fehleranteil|Summe über vier Werke|3 %",
    voraussetzungen="Tabelle als zweistufiges Experiment lesen|Pfadmultiplikation und -addition",
    format="Rechnung",
    operator="Weisen Sie nach",
    antwort="Zahl",
    material="Tabelle",
    skizze=TAB31,
    kontext="Produktion / Smartphones",
    textumfang="mittel",
    gegeben=ST31,
    gesucht="Nachweis, dass der Anteil der fehlerhaften Geräte unter allen hergestellten Geräten 3 % beträgt",
    verfahren="Summe der Produkte aus Werksanteil und Fehleranteil bilden (totale Wahrscheinlichkeit).",
    schritte="2",
    zahlenraum="Prozent|dezimal",
    einheiten="",
    ergebnis="0,1 · 0,05 + 0,3 · 0,03 + 0,2 · 0,04 + 0,4 · 0,02 = 3 % (amtlich)",
    zwischenergebnis="0,005 + 0,009 + 0,008 + 0,008 = 0,03",
    niveau_geschaetzt="II",
    fehlerquelle="die vier Fehleranteile ungewichtet mitteln (3,5 %)",
    abhaengig_von="",
    bemerkung="Dublette von: 2017MgrundlegendBStochastikWTR1-2a. AB amtlich: II. Wortgleich mit der Poolaufgabe (Teilaufgabe 2 a, gleiche BE; im Heft laufen die Buchstaben von 1 a–b und 2 a–e als a–g durch). Schätzung nach dem amtlichen Bereich der Poolzeile (Vorrang des Amtlichen, Kern § 5): II; die Poolzeile schätzt I. Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy.")
row(id="2017-be-gk-B3.1d", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="d", seite="6", punkte="3",
    afb_amtlich="II",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus Anteil und Schnittanteil berechnen",
    typ_neben="",
    stichwoerter="fehlerhaftes Gerät|Werk A gesucht|Schnittanteil|1/6",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient|Bedingung „fehlerhaft“ im Nenner",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze=TAB31,
    kontext="Produktion / Smartphones",
    textumfang="kurz",
    gegeben=ST31 + " Der Anteil fehlerhafter Geräte unter allen hergestellten beträgt 3 %. Ein unter allen hergestellten Geräten zufällig ausgewähltes Gerät ist fehlerhaft.",
    gesucht="Wahrscheinlichkeit dafür, dass es im Werk A hergestellt wurde",
    verfahren="Schnittanteil 0,1 · 0,05 durch den Gesamtanteil 0,03 teilen (Satz von Bayes).",
    schritte="2",
    zahlenraum="Bruch|dezimal",
    einheiten="",
    ergebnis="(0,1 · 0,05)/0,03 = 1/6 (amtlich)",
    zwischenergebnis="≈ 16,7 %",
    niveau_geschaetzt="II",
    fehlerquelle="den Fehleranteil 5 % im Werk A angeben (Bedingung vertauscht)",
    abhaengig_von="2017-be-gk-B3.1c",
    bemerkung="Dublette von: 2017MgrundlegendBStochastikWTR1-2b. AB amtlich: II. Wortgleich mit der Poolaufgabe (Teilaufgabe 2 b, gleiche BE). Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy.")
row(id="2017-be-gk-B3.1e", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="e", seite="6", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen",
    typ_neben="",
    stichwoerter="Werk A|20 Geräte|kein fehlerhaftes|Bernoulli-Kette",
    voraussetzungen="Stichprobe aus großer Stückzahl als Bernoulli-Kette modellieren|Potenz der Gegenwahrscheinlichkeit",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze=TAB31,
    kontext="Produktion / Smartphones",
    textumfang="kurz",
    gegeben=ST31 + " Von im Werk A hergestellten Geräten werden 20 zufällig ausgewählt.",
    gesucht="Wahrscheinlichkeit dafür, dass darunter kein fehlerhaftes Gerät ist",
    verfahren="Anzahl X der fehlerhaften Geräte ist binomialverteilt mit n = 20 und p = 0,05; P(X = 0) = 0,95^20.",
    schritte="1",
    zahlenraum="dezimal|Potenz|Prozent",
    einheiten="",
    ergebnis="P(X = 0) = 0,95^20 ≈ 0,358, also etwa 35,8 %.",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="mit dem Fehleranteil 3 % aller Geräte statt 5 % aus Werk A rechnen oder 1 − 0,95^20 angeben",
    abhaengig_von="",
    bemerkung="Abgewandelt von: 2017MgrundlegendBStochastikWTR1-2c; das Heft zieht 20 Geräte aus Werk A und fragt nach keinem fehlerhaften (0,95^20), der Pool zieht 250 und fragt nach der wahrscheinlichsten Anzahl fehlerhafter (Modalwert 12); gleiche BE (2). Anderer Typ als die Poolzeile. Eigene Rechnung, mit sympy bestätigt (0,3585).")
row(id="2017-be-gk-B3.1f", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="f", seite="6", punkte="4",
    afb_amtlich="I|II",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Binomialsumme als Sachaussage formulieren",
    typ_neben="",
    stichwoerter="Term 200 · 0,98^s · 0,02 + 0,98^200|Fehleranteil Werk D|s = 199|höchstens eines fehlerhaft",
    voraussetzungen="Bernoulli-Formel für k = 0 und k = 1 erkennen|Summe als kumulierte Wahrscheinlichkeit",
    format="Kurzantwort",
    operator="Geben Sie an|Beschreiben Sie",
    antwort="Zahl|Text",
    material="Tabelle",
    skizze=TAB31,
    kontext="Produktion / Smartphones",
    textumfang="kurz",
    gegeben=ST31 + " Term 200 · 0,98^s · 0,02 + 0,98^200.",
    gesucht="ein Wert von s, für den mit dem Term im Sachzusammenhang die Wahrscheinlichkeit eines Ereignisses berechnet werden kann; Beschreibung des zugehörigen Ereignisses",
    verfahren="0,02 ist der Fehleranteil in Werk D; 0,98^200 = P(X = 0) und 200 · 0,02 · 0,98^199 = P(X = 1) für n = 200, also s = 199 und die Summe P(X ≤ 1).",
    schritte="2",
    zahlenraum="dezimal|Potenz",
    einheiten="",
    ergebnis="s = 199; unter 200 im Werk D hergestellten, zufällig ausgewählten Geräten ist höchstens eines fehlerhaft (amtlich)",
    zwischenergebnis="Wert des Terms ≈ 0,0894",
    niveau_geschaetzt="II",
    fehlerquelle="s = 200 wählen oder das Ereignis als „genau eines fehlerhaft“ beschreiben",
    abhaengig_von="",
    bemerkung="Dublette von: 2017MgrundlegendBStochastikWTR1-2d. AB amtlich: II. Wortgleich mit der Poolaufgabe (Teilaufgabe 2 d, gleiche BE). Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy (0,0894).")
row(id="2017-be-gk-B3.1g", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="g", seite="6", punkte="4",
    afb_amtlich="II|III",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen",
    typ_neben="",
    stichwoerter="Werk C, Fehleranteil 4 %|mindestens ein fehlerhaftes|mindestens 95 %|n ≥ 74",
    voraussetzungen="Gegenereignis „kein fehlerhaftes“|Exponentialungleichung durch Logarithmieren oder Probieren",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze=TAB31,
    kontext="Produktion / Smartphones",
    textumfang="kurz",
    gegeben=ST31 + " Es werden im Werk C hergestellte Geräte zufällig ausgewählt.",
    gesucht="Mindestanzahl der auszuwählenden Geräte, damit sich darunter mit einer Wahrscheinlichkeit von mindestens 95 % mindestens ein fehlerhaftes Gerät befindet",
    verfahren="Über das Gegenereignis 1 − 0,96^n ≥ 0,95 ansetzen und durch Logarithmieren oder Probieren nach n auflösen.",
    schritte="3",
    zahlenraum="dezimal|Prozent|Potenz",
    einheiten="",
    ergebnis="Ist n die Anzahl auszuwählender Geräte, so gilt 1 − 0,96^n ≥ 0,95 ⇔ n ≥ 74 (amtlich)",
    zwischenergebnis="1 − 0,96^73 ≈ 0,9492|1 − 0,96^74 ≈ 0,9512",
    niveau_geschaetzt="III",
    fehlerquelle="n ≈ 73,4 abrunden oder mit 0,04^n statt 0,96^n ansetzen",
    abhaengig_von="",
    bemerkung="Dublette von: 2017MgrundlegendBStochastikWTR1-2e. AB amtlich: III. Wortgleich mit der Poolaufgabe (Teilaufgabe 2 e, gleiche BE). Schätzung nach dem amtlichen Bereich der Poolzeile (Vorrang des Amtlichen, Kern § 5): III; die Poolzeile schätzt II. Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy.")

# ---- Aufgabe 3.2: Zufallsexperimente (Seite 7, Anlage Seite 8, 20 BE)
row(id="2017-be-gk-B3.2a", block="B", aufgabe="3.2", titel="Zufallsexperimente", teilaufgabe="a", seite="7", punkte="5",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit zweier Stufen aus dem Sachtext berechnen",
    typ_neben="Wahrscheinlichkeit für ein zweistufiges Experiment mit zufälliger Urnenzusammensetzung berechnen",
    stichwoerter="Würfel wählt das Glücksrad|Pfadregel|totale Wahrscheinlichkeit|Weiß oder Rot",
    voraussetzungen="Laplace-Wahrscheinlichkeiten an Würfelnetz und Glücksrädern abzählen|Pfadmultiplikation und -addition",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Skizze",
    skizze=SK32,
    kontext="Glücksspiel / Würfel und Glücksrad",
    textumfang="mittel",
    gegeben=ST32 + " Tom würfelt mit W, anschließend dreht Lisa das Glücksrad, das der Würfel anzeigt (bei 1 G1, bei 2 G2). A1: W zeigt 2 und G2 zeigt anschließend Rot. A2: Das gedrehte Glücksrad zeigt Weiß oder Rot.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A1 und A2",
    verfahren="P(1) = 1/3, P(2) = 2/3; P(Rot | G2) = 1/2, P(Weiß oder Rot | G1) = 6/10, P(Weiß oder Rot | G2) = 1/2. A1 als Pfadprodukt, A2 als Summe der beiden Pfade über G1 und G2.",
    schritte="4",
    zahlenraum="Bruch|dezimal",
    einheiten="",
    ergebnis="P(A1) = 2/3 · 1/2 = 1/3; P(A2) = 1/3 · 0,6 + 2/3 · 0,5 = 8/15 ≈ 0,533.",
    zwischenergebnis="P(W = 2) = 2/3|P(Weiß oder Rot | G1) = 0,6",
    niveau_geschaetzt="II",
    fehlerquelle="für A2 die Anteile von Weiß und Rot beider Räder ungewichtet mitteln oder auf G2 ein weißes Feld annehmen",
    abhaengig_von="",
    bemerkung="Die Sektoranteile stehen nur in der Abbildung (G1: 4 rot, 4 blau, 2 weiß; G2: 2 rot, 1 blau, 1 schwarz), ebenso die Beschriftung des Würfels. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B3.2b", block="B", aufgabe="3.2", titel="Zufallsexperimente", teilaufgabe="b", seite="7", punkte="3",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Gleich wahrscheinliche Ergebnisse eines zweistufigen Experiments über die Pfadwahrscheinlichkeiten ermitteln",
    typ_neben="",
    stichwoerter="Würfel und Glücksrad gleichzeitig|sechs Ergebnisse|Pfadprodukte|gleiche Wahrscheinlichkeit",
    voraussetzungen="Ergebnismenge eines zusammengesetzten Experiments aufstellen|Unabhängigkeit als Produktregel nutzen",
    format="Rechnung|Kurzantwort",
    operator="Ermitteln Sie",
    antwort="Text",
    material="Skizze",
    skizze=SK32,
    kontext="Glücksspiel / Würfel und Glücksrad",
    textumfang="kurz",
    gegeben=ST32 + " Tom wirft den Würfel W und Lisa dreht gleichzeitig das Glücksrad G2. Von den jetzt möglichen sechs Ergebnissen haben drei die gleiche Wahrscheinlichkeit.",
    gesucht="die drei Ergebnisse mit gleicher Wahrscheinlichkeit",
    verfahren="Alle sechs Paare (Augenzahl; Farbe) aufstellen und ihre Wahrscheinlichkeiten als Produkte berechnen: P(1) = 1/3, P(2) = 2/3 mit P(rot) = 1/2, P(blau) = P(schwarz) = 1/4; die drei gleichen Werte heraussuchen.",
    schritte="3",
    zahlenraum="Bruch",
    einheiten="",
    ergebnis="(1; Rot), (2; Blau) und (2; Schwarz) haben je die Wahrscheinlichkeit 1/6; die übrigen: (1; Blau) und (1; Schwarz) je 1/12, (2; Rot) 1/3.",
    zwischenergebnis="1/3 · 1/2 = 2/3 · 1/4 = 1/6",
    niveau_geschaetzt="II",
    fehlerquelle="die sechs Ergebnisse für gleich wahrscheinlich halten oder nur die beiden Ergebnisse mit 1/12 finden",
    abhaengig_von="",
    bemerkung="Neuer Typ: die Pfadtypen der Liste berechnen einzelne Pfade oder Summen, hier wird die ganze Verteilung aufgestellt und nach gleichen Werten durchsucht. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B3.2c", block="B", aufgabe="3.2", titel="Zufallsexperimente", teilaufgabe="c", seite="7|8", punkte="5",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen",
    typ_neben="",
    stichwoerter="zehnmal drehen|genau viermal Rot|mindestens fünfmal Rot|Tabelle der summierten Binomialverteilung",
    voraussetzungen="Trefferwahrscheinlichkeit 0,4 am Glücksrad abzählen|Bernoulli-Formel|Gegenereignis bei kumulierten Werten",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Skizze|Tabelle",
    skizze=SK32 + TAB32,
    kontext="Glücksspiel / Würfel und Glücksrad",
    textumfang="kurz",
    gegeben=ST32 + " Lisa dreht das Glücksrad G1 zehnmal. C1: G1 zeigt genau viermal Rot. C2: G1 zeigt mindestens fünfmal Rot. Kontrollangabe: P(C2) ≈ 0,3669.",
    gesucht="Wahrscheinlichkeiten der Ereignisse C1 und C2",
    verfahren="X: Anzahl Rot, binomialverteilt mit n = 10 und p = 0,4. P(C1) = P(X = 4) mit der Bernoulli-Formel oder als Differenz P(X ≤ 4) − P(X ≤ 3) aus der Tabelle; P(C2) = 1 − P(X ≤ 4).",
    schritte="3",
    zahlenraum="dezimal|Bruch",
    einheiten="",
    ergebnis="P(C1) = (10 über 4) · 0,4⁴ · 0,6⁶ ≈ 0,2508; P(C2) = 1 − 0,6331 = 0,3669.",
    zwischenergebnis="P(X ≤ 4) = 0,6331|P(X ≤ 3) = 0,3823",
    niveau_geschaetzt="I",
    fehlerquelle="P(X ≥ 5) als 1 − P(X ≤ 5) ablesen oder p = 0,5 annehmen, weil Rot und Blau gleich viele Felder haben",
    abhaengig_von="",
    bemerkung="Kontrollangabe P(C2) ≈ 0,3669 durch eigene Rechnung bestätigt. Die Trefferwahrscheinlichkeit 0,4 folgt nur aus der Abbildung von G1. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B3.2d", block="B", aufgabe="3.2", titel="Zufallsexperimente", teilaufgabe="d", seite="7", punkte="3",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen",
    typ_neben="",
    stichwoerter="30 Wiederholungen|Ereignis C2 als Treffer|genau die Hälfte|Behauptung unter 5 %",
    voraussetzungen="Ereignis eines Teilexperiments als Treffer einer neuen Bernoulli-Kette deuten|Bernoulli-Formel mit Dezimalwerten",
    format="Rechnung|Begründung",
    operator="Prüfen Sie",
    antwort="Zahl|Text",
    material="Skizze",
    skizze=SK32,
    kontext="Glücksspiel / Würfel und Glücksrad",
    textumfang="mittel",
    gegeben=ST32 + " Das zehnmalige Drehen von G1 wird 30-mal durchgespielt; C2: G1 zeigt dabei mindestens fünfmal Rot, P(C2) ≈ 0,3669. Tom behauptet, die Wahrscheinlichkeit, dass C2 in genau der Hälfte aller Fälle eintritt, liege unter 5 %.",
    gesucht="Prüfung der Behauptung",
    verfahren="Y: Anzahl der Durchgänge mit C2, binomialverteilt mit n = 30 und p = 0,3669. P(Y = 15) = (30 über 15) · 0,3669^15 · 0,6331^15 berechnen und mit 0,05 vergleichen.",
    schritte="2",
    zahlenraum="dezimal|Potenz|Prozent",
    einheiten="",
    ergebnis="P(Y = 15) ≈ 0,048 < 0,05; die Behauptung trifft zu.",
    zwischenergebnis="(30 über 15) = 155 117 520",
    niveau_geschaetzt="II",
    fehlerquelle="mit p = 0,4 (Rot bei einer Drehung) statt mit P(C2) rechnen oder P(Y ≤ 15) statt P(Y = 15) bilden",
    abhaengig_von="2017-be-gk-B3.2c",
    bemerkung="Die Tabelle der Anlage reicht nicht bis n = 30; die Bernoulli-Formel ist nötig. Der Wert liegt knapp unter 5 % (mit p = 0,3669 oder exakt 0,04797). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-B3.2e", block="B", aufgabe="3.2", titel="Zufallsexperimente", teilaufgabe="e", seite="7|8", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit für Gewinn und Extrapreis über die Aufteilung einer Bernoulli-Kette in zwei Abschnitte berechnen",
    typ_neben="",
    stichwoerter="20 Drehungen|erste zehn genau fünfmal Rot|insgesamt höchstens neunmal Rot|Produkt unabhängiger Abschnitte",
    voraussetzungen="Bedingung für die zweiten zehn Drehungen ableiten|Tabelle der summierten Binomialverteilung lesen|Produktregel für unabhängige Abschnitte",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Skizze|Tabelle",
    skizze=SK32 + TAB32,
    kontext="Glücksspiel / Würfel und Glücksrad",
    textumfang="mittel",
    gegeben=ST32 + " Das Glücksrad G1 (Rot mit Wahrscheinlichkeit 0,4) soll 20-mal gedreht werden.",
    gesucht="Wahrscheinlichkeit dafür, dass unter den ersten zehn Drehungen genau fünfmal Rot und insgesamt höchstens neunmal Rot das Ergebnis ist",
    verfahren="Die Kette in die ersten und die letzten zehn Drehungen teilen: in den ersten genau 5 Treffer, in den letzten dann höchstens 4. Beide Abschnitte sind unabhängig und binomialverteilt mit n = 10, p = 0,4; P(X = 5) · P(X ≤ 4) aus der Tabelle bilden.",
    schritte="3",
    zahlenraum="dezimal",
    einheiten="",
    ergebnis="P = P(X = 5) · P(X ≤ 4) ≈ 0,2007 · 0,6331 ≈ 0,127.",
    zwischenergebnis="P(X = 5) = 0,8338 − 0,6331 = 0,2007|P(X ≤ 4) = 0,6331",
    niveau_geschaetzt="II",
    fehlerquelle="für die zweiten zehn Drehungen höchstens neun Treffer ansetzen oder mit n = 20 und P(X ≤ 9) rechnen",
    abhaengig_von="2017-be-gk-B3.2c",
    bemerkung="Der Typ trägt ein Etikett aus einem Glücksspielkontext (Gewinn und Extrapreis); der Lösungsweg – Kette in zwei unabhängige Abschnitte zerlegen, Bedingung für den Rest ableiten, Produkt bilden – ist derselbe. Eigene Rechnung, mit sympy bestätigt (0,1270).")

NEUE_TYPEN = [
    ("Fläche: Volumen eines Körpers mit konstanter Tiefe aus der Fläche zwischen Graph und x-Achse berechnen", "Analysis", "Flächeninhalt durch Integration",
     "Die Querschnittsfläche zwischen einem Graphen und der x-Achse über einem Intervall als bestimmtes Integral berechnen und mit einer konstanten Tiefe (Breite) zum Volumen eines prismatischen Bauteils im Sachzusammenhang multiplizieren.",
     "2017-be-gk-B1.1d"),
    ("Existenz einer quadratischen Funktion zu vier Wert- und Steigungsbedingungen über das überbestimmte Gleichungssystem untersuchen", "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Aus der Forderung, dass eine Parabel einen Graphen in zwei Punkten berührt, vier Bedingungen (zwei Werte, zwei Steigungen) für die drei Koeffizienten aufstellen, mit drei davon die Koeffizienten bestimmen und an der vierten entscheiden, ob es eine solche Funktion gibt.",
     "2017-be-gk-B1.2f"),
    ("Gerade und Ebene: Parallelität einer Geraden zu einer Ebene über das Skalarprodukt von Richtungs- und Normalenvektor nachweisen", "Analytische Geometrie", "Lagebeziehungen",
     "Nachweisen, dass eine Gerade zu einer Ebene in Koordinatenform parallel ist, indem das Skalarprodukt ihres Richtungsvektors mit dem Normalenvektor null ist; mit einer Punktprobe ausschließen, dass die Gerade in der Ebene liegt.",
     "2017-be-gk-B2.1d"),
    ("Körper: Eckpunkte eines Pyramidenstumpfs aus Symmetrie und Kantenlängen angeben", "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Aus gegebenen Eckpunkten eines geraden quadratischen Pyramidenstumpfs, seinen Kantenlängen und dem Schrägbild die Koordinaten weiterer Ecken angeben: Grundfläche aus der Diagonalen, Deckfläche mittig über der Mittelachse in der Stumpfhöhe.",
     "2017-be-gk-B2.2a"),
    ("Gleich wahrscheinliche Ergebnisse eines zweistufigen Experiments über die Pfadwahrscheinlichkeiten ermitteln", "Stochastik", "Baumdiagramm und Pfadregeln",
     "Für ein aus zwei unabhängigen Stufen zusammengesetztes Experiment (etwa Würfel und Glücksrad) alle Ergebnisse mit ihren Pfadwahrscheinlichkeiten aufstellen und diejenigen mit gleicher Wahrscheinlichkeit angeben.",
     "2017-be-gk-B3.2b"),
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
# CAS-Nachtrag (v0.14, abi.md § 7): jede Zeile verweist auf die WTR-Teilaufgabe, von der sie
# abweicht, oder sagt, dass es keine gibt; ein Poolvermerk darf davor stehen.
MARKE_NACHTRAG = re.compile(r"CAS-Nachtrag zu (\S+) \(WTR\): ")
MARKE_NACHTRAG_OHNE = "CAS-Nachtrag, ohne WTR-Gegenstück: "
POOLVERMERKE = ("Dublette von:", "Poolaufgabe (nicht erfasst", "Abgewandelt von:")


def wtr_papier(papier):
    """WTR-Heft zu einem Heft mit Rechnerzusatz (2017-bb-ea-cas → 2017-bb-ea), sonst leer."""
    m = PAPIER.fullmatch(papier)
    return papier[:m.start(4)] if m and m.group(4) else ""


def pruefe_nachtrag_zeile(z, a, nach_id):
    """Nachtragsvermerk einer Zeile (v0.14): genau einer, am Anfang von bemerkung oder direkt
    hinter einem Poolvermerk; der Verweis zeigt auf eine Zeile derselben Aufgabe im WTR-Heft
    des papier-Kürzels. Rückgabe: die WTR-id oder ""."""
    i, b = z["id"], z["bemerkung"]
    m = MARKE_NACHTRAG.search(b)
    ohne = b.find(MARKE_NACHTRAG_OHNE)
    a((m is not None) != (ohne >= 0),
      f"{i}: Nachtragszeile braucht genau einen Vermerk „CAS-Nachtrag zu <WTR-id> (WTR): …“ "
      f"oder „{MARKE_NACHTRAG_OHNE}…“")
    pos = m.start() if m else ohne
    a(pos <= 0 or b.startswith(POOLVERMERKE),
      f"{i}: Nachtragsvermerk muss am Anfang von bemerkung stehen (davor nur ein Poolvermerk)")
    wtr = wtr_papier(z["papier"])
    a(wtr != "", f"{i}: Nachtragsvermerk in einem Heft ohne Rechnerzusatz (-cas/-mms)")
    if not m:
        return ""
    ref = nach_id.get(m.group(1))
    a(ref is not None and ref["papier"] == wtr and ref["block"] == z["block"]
      and ref["aufgabe"] == z["aufgabe"],
      f"{i}: CAS-Nachtrag zu {m.group(1)} – keine Zeile derselben Aufgabe im WTR-Heft {wtr or '?'}")
    return m.group(1)


def pruefe_nachtrag(alt, a, warnung):
    """Nachtragsmodus (v0.14): Zeilen und KONFIG gegen das WTR-Heft im Katalog prüfen.
    soll = BE der Zeilen je Aufgabe (wie sonst); uebernommen = wortgleiche Teilaufgaben ohne
    Zeile (BE gleich der WTR-Zeile); unveraendert = Aufgabensummen des WTR-Hefts; je
    abweichender Aufgabe soll + uebernommen = Aufgabensumme der WTR-Fassung; alles zusammen
    be_angeboten. Rückgabe: Berichtszeilen."""
    wtr = KONFIG["nachtrag_zu"]
    soll, ueb = KONFIG["soll"], KONFIG.get("uebernommen", {})
    unv, gesamt = KONFIG.get("unveraendert", {}), KONFIG.get("be_angeboten")
    a(wtr_papier(KONFIG["papier"]) == wtr,
      f"Nachtrag: papier {KONFIG['papier']} ist nicht {wtr} mit Zusatz -cas oder -mms")
    wz = [z for z in alt if z["papier"] == wtr]
    a(bool(wz), f"Nachtrag: WTR-Heft {wtr} steht nicht im Katalog")
    nach_id = {z["id"]: z for z in alt}
    wtr_teil = {(z["aufgabe"], z["teilaufgabe"]): z for z in wz}
    summe = {}
    for z in wz:
        summe[z["aufgabe"]] = summe.get(z["aufgabe"], 0) + int(z["punkte"])
    a(not (set(soll) & set(unv)), f"Nachtrag: Aufgaben in soll und unveraendert zugleich: {sorted(set(soll) & set(unv))}")
    a(set(soll) | set(unv) == set(summe),
      f"Nachtrag: soll und unveraendert decken die Aufgaben des WTR-Hefts nicht genau ab "
      f"(WTR {sorted(summe)}, KONFIG {sorted(set(soll) | set(unv))})")
    for nr, be in unv.items():
        a(summe.get(nr) == be, f"Nachtrag: Aufgabe {nr} unverändert mit {be} BE, im WTR-Heft {summe.get(nr, 0)}")
    a(set(ueb) <= set(soll), f"Nachtrag: uebernommen nennt Aufgaben ohne soll: {sorted(set(ueb) - set(soll))}")
    belegt = {}  # WTR-Teilaufgabe → wer sie belegt (Zeile oder Übernommenes)
    for z in ZEILEN:
        ref = pruefe_nachtrag_zeile(z, a, nach_id)
        if ref in nach_id:
            belegt.setdefault((nach_id[ref]["aufgabe"], nach_id[ref]["teilaufgabe"]), []).append(z["id"])
    txt = []
    for nr, karte in ueb.items():
        zeilen_nr = {z["teilaufgabe"] for z in ZEILEN if z["aufgabe"] == nr}
        teile = []
        for cas_b, (w_b, be) in karte.items():
            a(cas_b not in zeilen_nr, f"Nachtrag: {nr} {cas_b}) ist übernommen und hat zugleich eine Zeile")
            ref = wtr_teil.get((nr, w_b))
            a(ref is not None and int(ref["punkte"]) == be,
              f"Nachtrag: {nr} {cas_b}) übernommen von WTR {w_b}) mit {be} BE – "
              + (f"die WTR-Zeile hat {ref['punkte']} BE" if ref else "keine WTR-Zeile"))
            belegt.setdefault((nr, w_b), []).append(f"übernommen {cas_b})")
            teile.append(f"{cas_b} = WTR {w_b} ({be})")
        ist = soll[nr] + sum(be for _, be in karte.values())
        a(ist == summe.get(nr), f"Nachtrag: Aufgabe {nr} soll {soll[nr]} + übernommen "
                                f"{ist - soll[nr]} = {ist}, WTR-Aufgabe {summe.get(nr, 0)} BE")
        txt.append(f"Aufgabe {nr}: Zeilen {soll[nr]} + übernommen {ist - soll[nr]} ({', '.join(teile)}) "
                   f"= {ist} / Aufgabe WTR {summe.get(nr, 0)}")
    for nr in soll:
        if nr not in ueb:
            a(soll[nr] == summe.get(nr), f"Nachtrag: Aufgabe {nr} ohne übernommene Teilaufgaben, "
                                         f"soll {soll[nr]} gegen WTR-Aufgabe {summe.get(nr, 0)} BE")
    doppelt = {k: v for k, v in belegt.items() if len(v) > 1}
    a(not doppelt, f"Nachtrag: WTR-Teilaufgaben mehrfach belegt: {doppelt}")
    frei = sorted(f"{nr} {b})" for (nr, b) in wtr_teil if nr in soll and (nr, b) not in belegt)
    if frei:
        warnung.append(f"Nachtrag: WTR-Teilaufgaben ohne CAS-Gegenstück: {', '.join(frei)}")
    s_soll, s_ueb = sum(soll.values()), sum(be for k in ueb.values() for _, be in k.values())
    s_unv = sum(unv.values())
    a(gesamt is not None and s_soll + s_ueb + s_unv == gesamt,
      f"Nachtrag: soll {s_soll} + übernommen {s_ueb} + unverändert {s_unv} = {s_soll + s_ueb + s_unv}, "
      f"be_angeboten {gesamt}")
    txt.append(f"Unverändert ({', '.join(f'{nr} {be}' for nr, be in unv.items())}): {s_unv} BE, "
               f"im WTR-Heft {wtr} gleich")
    txt.append(f"Nachtrag zu {wtr}: Zeilen {s_soll} + übernommen {s_ueb} + unverändert {s_unv} = "
               f"{s_soll + s_ueb + s_unv} / angeboten {gesamt}")
    return txt


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
        # CAS-Nachtrag (v0.14): jeder Nachtragsvermerk im Bestand zeigt auf eine WTR-Zeile
        nach_id = {z["id"]: z for z in alt}
        nachtrag = [z for z in alt if "CAS-Nachtrag" in z["bemerkung"]]
        for z in nachtrag:
            pruefe_nachtrag_zeile(z, a, nach_id)
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
        if nachtrag:
            print(f"CAS-Nachtrag: {len(nachtrag)} Zeilen ("
                  + ", ".join(f"{h} zu {wtr_papier(h)} {sum(1 for z in nachtrag if z['papier'] == h)}"
                              for h in sorted({z['papier'] for z in nachtrag}))
                  + "), jeder Nachtragsvermerk zeigt auf eine WTR-Zeile derselben Aufgabe.")
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
    # CAS-Nachtrag (v0.14): übernommene und unveränderte Aufgaben gegen das WTR-Heft
    nachtrag_txt = pruefe_nachtrag(alt, a, warnung) if KONFIG.get("nachtrag_zu") else []

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
    for t_ in nachtrag_txt:
        print(t_)
    haupt ={z["typ"] for z in ZEILEN} | {z["typ"] for z in alt}
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
