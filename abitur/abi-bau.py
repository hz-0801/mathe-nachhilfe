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
    "papier": "2017-bb-ea-cas",
    "datei": "hefte/abi/2017-bb-ea-cas.pdf",  # amtliches Heft (Bildungsserver, BB_17_Ma_CAS_Aufgaben), 10 Seiten mit Textebene, lokal (abi-quellen.md § 2, § 8)
    "seiten": 10,
    # CAS-Nachtrag (v0.14, abi.md § 7): Zeilen nur für Teilaufgaben, die von der
    # WTR-Fassung 2017-bb-ea abweichen (Wortlaut, Angaben, gesuchtes Ergebnis
    # oder BE). „CAS:“ im Titel tragen 2.1 Eisbecher, 2.2 Straßenverlauf, 3.1 Zelt
    # und 4.2 Freizeit; Teil 1 (1.1–1.3), 3.2 und 4.1 sind wortgleich mit gleichen
    # BE (Textvergleich aller Teilaufgaben, Seiten gerendert).
    "nachtrag_zu": "2017-bb-ea",
    # BE der abweichenden Teilaufgaben je „CAS:“-Aufgabe (BE-Tabellen der CAS-Fassung):
    # 2.1 a 7, b 7, c 13, e 6 (neu), f 6 = 39; 2.2 b 9, d 5 (neu), g 5 = 19;
    # 3.1 c 4, e 4, f 5 = 13; 4.2 a 8, b 4, d 4 = 16.
    "soll": {"2.1": 39, "2.2": 19, "3.1": 13, "4.2": 16},
    # wortgleiche Teilaufgaben der „CAS:“-Aufgaben ohne Zeile: CAS-Buchstabe → (WTR-Buchstabe, BE)
    "uebernommen": {"2.1": {"d": ("d", 4), "g": ("f", 7)},
                    "2.2": {"a": ("a", 6), "c": ("c", 9), "e": ("d", 6), "f": ("e", 10)},
                    "3.1": {"a": ("a", 5), "b": ("b", 4), "d": ("d", 3)},
                    "4.2": {"c": ("c", 5), "e": ("e", 4)}},
    # Aufgaben ohne „CAS:“, wortgleich mit gleichen BE (Summe je Aufgabe)
    "unveraendert": {"1.1": 5, "1.2": 5, "1.3": 5, "3.2": 10, "4.1": 10},
    # angeboten wie im WTR-Heft: 15 + 50 + 50 + 25 + 10 + 10 + 25 (beide Wahlwege)
    "be_angeboten": 185,
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
# Heft 2017-bb-ea-cas (amtliches Heft BB_17_Ma_CAS_Aufgaben, 10 Seiten mit
# Textebene; CAS-Nachtrag zu 2017-bb-ea, Auftrag Nacht 2026-09-27, Teil 9).
# Zeilen nur für Teilaufgaben, die von der WTR-Fassung abweichen (abi.md § 7);
# Textvergleich aller Teilaufgaben beider Hefte, jede Aufgabenseite gerendert.
# „CAS:“-Aufgaben 2.1, 2.2, 3.1, 4.2; Teil 1, 3.2 und 4.1 wortgleich.
# Pool: 3.1 Zelt ist wortgleich die Poolaufgabe 2017 erhöht Teil B AG/LA (A2)
# CAS 2 (Stapel 2017-ea-B, CAS-Zweig, Reserve) – Vormerkung in c, e, f.
# ---- Aufgabe 2.1 CAS: Eisbecher (Seite 4, 50 BE; Zeilen a, b, c, e, f = 39 BE)
SK21 = "Halber Längsquerschnitt eines Eisbechers im ersten Quadranten (x-Achse mit 1 beschriftet, y-Achse mit 1 und 2): innen der Graph G_h von (0 | 1) nach rechts oben bis (1,5 | h(1,5)) ≈ (1,5 | 2,28), außen der flachere Graph G_k; dunkel getönt die Becherwand zwischen G_h und G_k und der Fuß zwischen der Parabel p und der x-Achse von x = 0 bis 1; hell getönt die Fläche links oben zwischen y-Achse, G_h und der Waagerechten durch den oberen Randpunkt; eine gestrichelte Senkrechte bei x = 1,5 begrenzt das Bild rechts."
row(id="2017-bb-ea-cas-B2.1a", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="a", seite="4", punkte="7",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Definitionsbereich einer Logarithmusfunktion angeben",
    typ_neben="Gemeinsame Punkte aller Graphen einer Schar bestimmen|Scharparameter aus einem Punkt des Graphen angeben",
    stichwoerter="Logarithmusfunktion|Definitionsbereich|Funktionenschar|gemeinsamer Punkt",
    voraussetzungen="Definitionsbereich des natürlichen Logarithmus kennen|Logarithmusgleichung exponenzieren oder mit dem CAS lösen|mit dem Parameter rechnen",
    format="Kurzantwort|Begründung|Rechnung",
    operator="Geben Sie an|Zeigen Sie|Ermitteln Sie",
    antwort="Term|Text|Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Funktionenschar f_a mit f_a(x) = ln(a · x² + 1); a ∈ IR, a > 0. Die Graphen dieser Funktionen sind G_a.",
    gesucht="Definitionsbereich von f_a; Nachweis, dass alle Graphen G_a durch den Koordinatenursprung verlaufen; exakter Wert von a mit f_a(2) = 2",
    verfahren="Für a > 0 ist a · x² + 1 ≥ 1 > 0, der Logarithmus also für jedes x definiert. f_a(0) = ln 1 = 0 unabhängig von a. Aus ln(4a + 1) = 2 folgt durch Exponenzieren (oder mit dem CAS) 4a + 1 = e², also a = (e² − 1)/4.",
    schritte="4",
    zahlenraum="ganz|Potenz",
    einheiten="",
    ergebnis="D = IR. Wegen f_a(0) = ln 1 = 0 verläuft jeder Graph G_a durch O(0 | 0). a = (e² − 1)/4 ≈ 1,597",
    zwischenergebnis="4a + 1 = e²",
    niveau_geschaetzt="II",
    fehlerquelle="den Definitionsbereich ohne Rücksicht auf a > 0 einschränken oder den exakten Wert von a durch einen gerundeten ersetzen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B2.1a (WTR): Wortlaut und Angaben gleich, 7 statt 8 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Drei Leistungen in einer Einheit; thema folgt dem ersten Typ. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B2.1b", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="b", seite="4", punkte="7",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gemeinsamen Extrempunkt einer Funktionenschar nachweisen",
    typ_neben="Extrempunkt an vorgegebener Stelle nachweisen",
    stichwoerter="Funktionenschar|gemeinsamer Extrempunkt|Vorzeichenwechsel|Tiefpunkt",
    voraussetzungen="Kettenregel anwenden oder mit dem CAS ableiten|Ableitung des natürlichen Logarithmus kennen|Vorzeichenwechselkriterium kennen",
    format="Begründung|Rechnung",
    operator="Zeigen Sie|Begründen Sie",
    antwort="Text|Term",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Funktionenschar f_a mit f_a(x) = ln(a · x² + 1); a ∈ IR, a > 0, mit den Graphen G_a.",
    gesucht="Nachweis, dass alle Graphen G_a einen gemeinsamen lokalen Extrempunkt haben; Begründung ohne Zuhilfenahme der zweiten Ableitung, dass dieser Extrempunkt für a > 0 ein Tiefpunkt ist",
    verfahren="f_a'(x) = 2a · x / (a · x² + 1). Der Nenner ist stets positiv, also ist x = 0 für jedes a die einzige Nullstelle der Ableitung; f_a(0) = 0 liefert für alle Graphen denselben Punkt. Der Zähler 2a · x wechselt bei a > 0 an der Stelle 0 das Vorzeichen von minus nach plus, also liegt ein Tiefpunkt vor.",
    schritte="4",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="f_a'(x) = 2a · x / (a · x² + 1) mit der einzigen Nullstelle x = 0 und f_a(0) = 0: alle Graphen haben den gemeinsamen Extrempunkt T(0 | 0). Für x < 0 ist f_a'(x) < 0, für x > 0 ist f_a'(x) > 0 – Vorzeichenwechsel von minus nach plus, also ein Tiefpunkt.",
    zwischenergebnis="f_a'(x) = 2a · x / (a · x² + 1)|f_a(0) = 0",
    niveau_geschaetzt="II",
    fehlerquelle="den Nenner als möglichen Nullfaktor behandeln oder die geforderte Begründung doch über die zweite Ableitung führen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B2.1b (WTR): Wortlaut und Angaben gleich, 7 statt 8 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B2.1c", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="c", seite="4", punkte="13",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Schranke für den Anstieg der Tangenten einer Schar begründen",
    typ_neben="Tangentengleichung in einem Punkt des Graphen aufstellen|Gerade senkrecht zu einer gegebenen Tangente durch einen Punkt aufstellen|Flächeninhalt des von Tangente, Normale und y-Achse begrenzten Dreiecks berechnen",
    stichwoerter="Tangentenschar|Anstiegsschranke|Normale|Dreiecksfläche",
    voraussetzungen="Ableitung einer Schar bilden|Term durch Umformen abschätzen|Normale als Gerade mit dem negativen Kehrwert des Anstiegs aufstellen",
    format="Begründung|Rechnung",
    operator="Begründen Sie|Ermitteln Sie",
    antwort="Text|Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Funktionenschar f_a mit f_a(x) = ln(a · x² + 1), a > 0. Die Tangenten an G_a im Punkt B_a(1 | f_a(1)) sind t_a. Für a = 1 ist f_1(x) = ln(x² + 1) mit B_1(1 | ln 2). [Kontrollergebnis: t_1: y = x + ln 2 − 1]",
    gesucht="Begründung, dass keine der Tangenten t_a einen Anstieg größer als 2 haben kann; Flächeninhalt des Dreiecks, das von der y-Achse sowie der Tangente und der Normalen an G_1 im Punkt B_1 begrenzt wird",
    verfahren="Anstieg m(a) = f_a'(1) = 2a/(a + 1) = 2 − 2/(a + 1); für a > 0 ist der Subtrahend positiv, also m(a) < 2. Für a = 1 ist m = 1, damit t_1: y = x + ln 2 − 1 und n_1: y = −x + ln 2 + 1. Beide Geraden schneiden die y-Achse in ln 2 − 1 und ln 2 + 1; die Grundseite auf der y-Achse ist 2 LE lang, die zugehörige Höhe ist der x-Abstand 1 des Punktes B_1.",
    schritte="7",
    zahlenraum="ganz",
    einheiten="",
    ergebnis="m(a) = 2a/(a + 1) = 2 − 2/(a + 1) < 2 für alle a > 0, der Anstieg bleibt also stets unter 2. t_1: y = x + ln 2 − 1, n_1: y = −x + ln 2 + 1; das Dreieck hat die Grundseite 2 und die Höhe 1, sein Flächeninhalt ist A = 1 FE.",
    zwischenergebnis="m(a) = 2a/(a + 1)|t_1: y = x + ln 2 − 1|n_1: y = −x + ln 2 + 1|Achsenschnittpunkte (0 | ln 2 − 1) und (0 | ln 2 + 1)",
    niveau_geschaetzt="III",
    fehlerquelle="den Grenzwert 2 des Anstiegs als angenommenen Wert deuten statt als obere Schranke, oder bei der Dreiecksfläche die Grundseite auf der y-Achse mit der Höhe verwechseln",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B2.1c (WTR): Wortlaut und Angaben gleich, 13 statt 14 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Das Kontrollergebnis t_1 ist im Heft abgedruckt und durch eigene Rechnung bestätigt. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B2.1e", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="e", seite="4", punkte="6",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    typ_neben="Fläche: Flächenmaßstab eines Modells auf eine Realfläche anwenden",
    stichwoerter="Querschnittsfläche|befüllbarer Teil|waagerechte Randgerade|Integral der Differenz|Maßstab",
    voraussetzungen="obere Begrenzung als Randwert h(1,5) aus dem Bild erkennen|Integral mit dem CAS berechnen|Flächenmaßstab 1 FE = 16 cm² anwenden",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Figur",
    skizze=SK21,
    kontext="Eisbecher / Füllvolumen",
    textumfang="mittel",
    gegeben="Halber Längsquerschnitt eines Eisbechers im Intervall [0; 1,5]: Innenrand ist der Graph von h mit h(x) = 0,75 · f_2(x) + 1 = 0,75 · ln(2x² + 1) + 1, Außenrand der Graph von k mit k(x) = 1,75 · ln(2,5x + 1) − 0,5; der Becher entsteht durch Rotation um die y-Achse, 1 LE = 4 cm. Im Bild hell dargestellt ist die Querschnittsfläche zwischen der y-Achse, dem Graphen von h und der Waagerechten durch den oberen Randpunkt (1,5 | h(1,5)); bei Rotation um die y-Achse entspricht sie dem Volumen des befüllbaren Teils.",
    gesucht="Größe der hell dargestellten Querschnittsfläche",
    verfahren="Obere Begrenzung ist die Waagerechte y = h(1,5) = 0,75 · ln 5,5 + 1 ≈ 2,279. Die Fläche ist das Integral der Differenz von 0 bis 1,5: A = ∫ (h(1,5) − h(x)) dx = 1,5 · h(1,5) − ∫ h(x) dx, mit dem CAS berechnet; mit 1 FE = 16 cm² in cm² umrechnen.",
    schritte="4",
    zahlenraum="dezimal",
    einheiten="cm²",
    ergebnis="A = 1,5 · h(1,5) − ∫ h(x) dx (Grenzen 0 und 1,5) ≈ 3,418 − 2,367 ≈ 1,051 FE, also etwa 16,8 cm².",
    zwischenergebnis="h(1,5) = 0,75 · ln 5,5 + 1 ≈ 2,279|∫ h(x) dx von 0 bis 1,5 ≈ 2,367|A ≈ 1,051 FE",
    niveau_geschaetzt="II",
    fehlerquelle="die Fläche unter dem Graphen von h statt zwischen Graph und oberer Randgeraden berechnen oder den Flächenmaßstab mit 4 statt 16 ansetzen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag, ohne WTR-Gegenstück: die Teilaufgabe steht nur in der CAS-Fassung; die CAS-Teilaufgaben f und g entsprechen den WTR-Teilaufgaben e und f. Die obere Begrenzung ist dem Bild entnommen: die helle Fläche endet oben waagerecht in Höhe des Randpunkts von G_h bei x = 1,5. Exakt A = 9/4 − (3√2/4) · arctan(3√2/2), gegengeprüft über die Umkehrfunktion x(y) (Integral über y von 1 bis h(1,5)). Das Heft nennt keine Einheit; Ergebnis in FE und cm². Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B2.1f", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="f", seite="4", punkte="6",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen",
    typ_neben="",
    stichwoerter="Parabel|Symmetrie|Flächenbedingung|Maßstab|Rekonstruktion",
    voraussetzungen="Integral einer quadratischen Funktion bilden oder mit dem CAS berechnen|Flächenmaßstab 1 FE = 16 cm² anwenden|Ansatz mit Symmetrie verkürzen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Term",
    material="Figur",
    skizze="Im halben Längsquerschnitt des Eisbechers liegt unten am Fuß die zur y-Achse symmetrische Parabel p; die dunkel getönte Fläche zwischen ihr und der x-Achse reicht von der y-Achse bis zur Nullstelle der Parabel bei x = 1 und ist am linken Rand 0,2 LE hoch.",
    kontext="Verpackung / Eisbecher",
    textumfang="mittel",
    gegeben="Der Fuß des Eisbechers, dessen oberer Rand im Querschnitt durch die zur y-Achse symmetrische quadratische Parabel p modelliert wird, hat am Boden einen Durchmesser von 8 cm und eine Querschnittsfläche von 64/15 cm². Es gilt 1 LE = 4 cm. [Kontrollergebnis: p(x) = −0,2x² + 0,2]",
    gesucht="Gleichung der Parabel p",
    verfahren="Symmetrie zur y-Achse liefert den Ansatz p(x) = a · x² + c. Der Durchmesser 8 cm entspricht 2 LE, also ist p(1) = 0 und damit a = −c, das heißt p(x) = c · (1 − x²). Die Querschnittsfläche 64/15 cm² entspricht wegen 1 FE = 16 cm² genau 4/15 FE. Aus dem Integral von −1 bis 1 über c · (1 − x²) folgt 4c/3 = 4/15; Integral und Gleichung mit dem CAS.",
    schritte="5",
    zahlenraum="dezimal|Bruch",
    einheiten="cm|cm²",
    ergebnis="c = 0,2, also p(x) = −0,2x² + 0,2",
    zwischenergebnis="Ansatz p(x) = c · (1 − x²)|Fläche in Flächeneinheiten: 4c/3|64/15 cm² = 4/15 FE",
    niveau_geschaetzt="III",
    fehlerquelle="die Querschnittsfläche ohne die Umrechnung 1 FE = 16 cm² einsetzen oder nur die halbe Fläche von 0 bis 1 ansetzen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B2.1e (WTR): Wortlaut und Angaben gleich, in der CAS-Fassung Teilaufgabe f mit 6 statt 9 BE (das CAS übernimmt Integral und Gleichung); Typ und Ergebnis wie in der WTR-Zeile. Das Kontrollergebnis ist im Heft abgedruckt und durch eigene Rechnung bestätigt; die Bestätigung gelingt nur mit der vollen Querschnittsfläche von −1 bis 1. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.2 CAS: Straßenverlauf (Seiten 5–6, 50 BE; Zeilen b, d, g = 19 BE)
row(id="2017-bb-ea-cas-B2.2b", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="b", seite="5", punkte="9",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gemeinsamen Extrempunkt einer Funktionenschar nachweisen",
    typ_neben="Extrempunkt an vorgegebener Stelle nachweisen|Fehlen von Wendepunkten über die zweite Ableitung nachweisen",
    stichwoerter="Funktionenschar|gemeinsamer Tiefpunkt|zweite Ableitung|Wendepunkte",
    voraussetzungen="Ableitung von Exponentialfunktionen mit Kettenregel oder CAS bilden|Exponentialgleichung lösen|hinreichendes Kriterium für Extrem- und Wendestellen kennen",
    format="Rechnung|Begründung",
    operator="Zeigen Sie|Ermitteln Sie|Untersuchen Sie",
    antwort="Term|Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Funktionenschar f_a mit f_a(x) = e^(2ax) + e^(−2ax); x ∈ IR, a ∈ IR, a ≠ 0, mit den Graphen G_a.",
    gesucht="Nachweis, dass alle Graphen G_a denselben lokalen Extrempunkt besitzen; dessen Art und Koordinaten; Untersuchung auf mögliche Wendepunkte",
    verfahren="f_a'(x) = 2a · (e^(2ax) − e^(−2ax)); Nullsetzen führt auf e^(4ax) = 1 und damit auf x = 0 für jedes a, mit f_a(0) = 2. f_a''(x) = 4a² · (e^(2ax) + e^(−2ax)) ist für a ≠ 0 stets positiv: an der Stelle 0 liegt ein Tiefpunkt, und weil die zweite Ableitung nirgends null wird, gibt es keine Wendepunkte.",
    schritte="6",
    zahlenraum="ganz|Potenz",
    einheiten="",
    ergebnis="Alle Graphen haben den gemeinsamen Tiefpunkt T(0 | 2). Wegen f_a''(x) = 4a² · f_a(x) > 0 für alle x besitzt kein Graph G_a einen Wendepunkt.",
    zwischenergebnis="f_a'(x) = 2a · (e^(2ax) − e^(−2ax))|e^(4ax) = 1|f_a''(x) = 4a² · f_a(x)",
    niveau_geschaetzt="II",
    fehlerquelle="aus e^(4ax) = 1 auf 4ax = 1 statt auf 4ax = 0 schließen oder die Wendepunkte nur an einem Beispielgraphen prüfen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B2.2b (WTR): Wortlaut und Angaben gleich, 9 statt 10 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B2.2d", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="d", seite="5", punkte="5",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Identische Graphen einer Schar zu entgegengesetzten Parameterwerten begründen",
    typ_neben="Scharparameter aus einem Punkt des Graphen angeben",
    stichwoerter="Funktionenschar|entgegengesetzter Parameter|identische Graphen|Exponentialgleichung|Punktprobe",
    voraussetzungen="f_(−a) am Term bilden und mit f_a vergleichen|Exponentialgleichung durch Substitution oder mit dem CAS lösen|natürlichen Logarithmus anwenden",
    format="Begründung|Rechnung",
    operator="Begründen Sie|Ermitteln Sie",
    antwort="Text|Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Funktionenschar f_a mit f_a(x) = e^(2ax) + e^(−2ax); x ∈ IR, a ∈ IR, a ≠ 0, mit den Graphen G_a; Punkt R(2 | 4).",
    gesucht="Begründung, dass es zu jedem Graphen G_a1 der Schar einen zweiten Graphen G_a2 der Schar gibt, der mit G_a1 identisch ist; die reellen Zahlen a1 und a2, für die G_a1 und G_a2 durch R(2 | 4) verlaufen",
    verfahren="f_(−a)(x) = e^(−2ax) + e^(2ax) = f_a(x) für alle x, also ist G_(−a) = G_a; zu a1 gehört a2 = −a1 ≠ a1. Punktprobe f_a(2) = 4: e^(4a) + e^(−4a) = 4; mit u = e^(4a) folgt u² − 4u + 1 = 0, u = 2 ± √3, also 4a = ±ln(2 + √3) (oder mit dem CAS lösen).",
    schritte="4",
    zahlenraum="dezimal|Wurzel|Potenz|negativ",
    einheiten="",
    ergebnis="Wegen f_(−a)(x) = f_a(x) für alle x ist G_(−a) mit G_a identisch, a2 = −a1. Durch R(2 | 4): e^(4a) + e^(−4a) = 4 liefert a1 = ln(2 + √3)/4 ≈ 0,329 und a2 = −ln(2 + √3)/4 ≈ −0,329.",
    zwischenergebnis="e^(4a) = 2 ± √3|4a = ±ln(2 + √3) ≈ ±1,317",
    niveau_geschaetzt="II",
    fehlerquelle="die Achsensymmetrie der Graphen (x durch −x ersetzen) mit der Symmetrie im Parameter (a durch −a ersetzen) verwechseln oder nur eine Lösung der Exponentialgleichung angeben",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag, ohne WTR-Gegenstück: die Teilaufgabe steht nur in der CAS-Fassung; die CAS-Teilaufgaben e, f, g entsprechen den WTR-Teilaufgaben d, e, f. Neuer Typ: gefragt ist die Identität zweier Scharkurven über f_(−a) = f_a, nicht die Achsensymmetrie in x aus Teilaufgabe a. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B2.2g", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="g", seite="6", punkte="5",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Abschnittsweise begrenzte Fläche durch Integration berechnen",
    typ_neben="Fläche: Flächenmaßstab eines Modells auf eine Realfläche anwenden",
    stichwoerter="Integral|abschnittsweise Berandung|Flächenmaßstab|Hektar",
    voraussetzungen="Integrale mit dem CAS berechnen|Integral einer linearen Funktion berechnen|Prozentanteil bilden|1 ha = 10 000 m² kennen",
    format="Rechnung",
    operator="Ermitteln Sie|Geben Sie an",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Landwirtschaft",
    textumfang="mittel",
    gegeben="Es gilt 1 LE = 150 m. Die Landstraße wird für 0 ≤ x ≤ 4 durch den Graphen von f_0,15(x) = e^(0,3x) + e^(−0,3x) modelliert, die Schnellstraße für x ≥ 4 durch die Gerade y = 0,9x. Die von den beiden Koordinatenachsen, der Landstraße, der Schnellstraße und der Geraden x = 7 eingeschlossene Fläche nutzt ein Landwirt zu 80 % für den Anbau von Getreide.",
    gesucht="Größe der Getreideanbaufläche in Hektar",
    verfahren="Die Fläche in zwei Abschnitten integrieren: von 0 bis 4 unter dem Graphen von f_0,15 (mit dem CAS), von 4 bis 7 unter der Geraden. Die Summe mit 1 FE = 150² m² = 22 500 m² in Quadratmeter umrechnen und davon 80 % nehmen.",
    schritte="5",
    zahlenraum="dezimal|Prozent|Potenz",
    einheiten="m²|ha",
    ergebnis="Integral von 0 bis 4 ≈ 10,063 FE, Integral von 4 bis 7 = 14,85 FE, zusammen ≈ 24,913 FE ≈ 560 544 m². Davon 80 % sind rund 448 435 m², also etwa 44,8 ha.",
    zwischenergebnis="Integral von 0 bis 4 ≈ 10,063|Integral von 4 bis 7 = 14,85|Gesamtfläche ≈ 24,913 FE",
    niveau_geschaetzt="II",
    fehlerquelle="den Flächenmaßstab mit 150 statt mit 150² ansetzen oder die Umrechnung von Quadratmetern in Hektar vergessen",
    abhaengig_von="2017-bb-ea-B2.2d",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B2.2f (WTR): Wortlaut und Angaben gleich, in der CAS-Fassung Teilaufgabe g mit 5 statt 9 BE – die Integrale rechnet das CAS; Typ und Ergebnis wie in der WTR-Zeile. Die Schnellstraße y = 0,9x stammt aus der CAS-Teilaufgabe e, die wortgleich die WTR-Teilaufgabe d ist und keine eigene Zeile hat; abhaengig_von zeigt deshalb auf 2017-bb-ea-B2.2d. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 3.1 CAS: Zelt (Seite 7, 25 BE; Zeilen c, e, f = 13 BE) – Poolaufgabe 2017 erhöht B AG/LA (A2) CAS 2
SK31 = "Abbildung 2 zeigt das Zelt als Schrägbild einer Pyramide. An der rechten vorderen Wand ist ein dunkel ausgefülltes waagerechtes Vordach aufgespannt, darunter die helle Öffnung in der Wand; zwei senkrechte Stangen stützen die äußere Vordachkante. Rechts daneben zwei Maßangaben: 1,80 m als Höhe des Vordachs über dem Boden und 1,40 m als Breite zwischen den beiden Stangen."
row(id="2017-bb-ea-cas-B3.1c", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="c", seite="7", punkte="4",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt mit gleichem Abstand zu allen Seitenflächen über die Symmetrieachse bestimmen",
    typ_neben="Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen",
    stichwoerter="Lichtquelle|Abstand zur Ebene|Symmetrieachse|Hessesche Normalform",
    voraussetzungen="Hessesche Normalform aufstellen|Betragsgleichung lösen|Symmetrie eines Körpers ausnutzen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Camping",
    textumfang="kurz",
    gegeben="Pyramide ABCDS mit quadratischer Grundfläche der Seitenlänge 5 und der Spitze S(2,5 | 2,5 | 3,9); der Grundflächenmittelpunkt ist M(2,5 | 2,5 | 0). Die Wand ABS liegt in der Ebene E: −39y + 25z = 0. Im Zelt hängt eine Lichtquelle so, dass sie von jeder der vier Wände 80 cm Abstand hat; 1 LE entspricht 1 m.",
    gesucht="Koordinaten des Punktes, der die Lichtquelle im Modell darstellt",
    verfahren="Aus der Symmetrie der Pyramide folgt, dass der Punkt auf der Senkrechten durch M liegt, also die Form L(2,5 | 2,5 | z) hat. Abstand zu E über die Hessesche Normalform: |−39 · 2,5 + 25z| / √(39² + 25²) = 0,8 mit √2146 ≈ 46,32. Von den beiden Lösungen die im Zeltinneren wählen.",
    schritte="5",
    zahlenraum="dezimal",
    einheiten="m|cm",
    ergebnis="Aus 97,5 − 25z = 0,8 · √2146 ≈ 37,06 folgt z ≈ 2,418; die Lichtquelle liegt bei L(2,5 | 2,5 | 2,42). Die zweite Lösung z ≈ 5,38 liegt oberhalb der Spitze und entfällt.",
    zwischenergebnis="√2146 ≈ 46,32|0,8 · √2146 ≈ 37,06",
    niveau_geschaetzt="II",
    fehlerquelle="die Betragsgleichung nur mit einem Vorzeichen lösen und den Punkt außerhalb des Zelts angeben, oder 80 cm nicht in 0,8 LE umrechnen",
    abhaengig_von="2017-bb-ea-B3.1a",
    bemerkung="Poolaufgabe (nicht erfasst): 2017MerhoehtBAGLAA2CAS2-1c. CAS-Nachtrag zu 2017-bb-ea-B3.1c (WTR): Wortlaut gleich, 4 statt 5 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Die CAS-Aufgabe 3.1 Zelt ist wortgleich die Poolaufgabe 2017 erhöht Teil B AG/LA (A2) CAS 2 (Zahlen, Aufträge, BE 5, 4, 4, 3, 4, 5); ihr Stapel 2017-ea-B (CAS-Zweig) ist Reserve und nicht erfasst – offener Posten in der Prüfungsliste (§ 4). Schätzung: die WTR-Zeile trägt III; die übernommene Schätzung folgt dem Standardbezug der Poolfassung (Anforderungsbereich II), Vorrang des Amtlichen (Kern § 5). abhaengig_von zeigt auf die WTR-Zeile 3.1 a, weil die wortgleiche CAS-Teilaufgabe a keine eigene Zeile hat. Eigene Rechnung, mit sympy bestätigt; der Erwartungshorizont der Poolfassung nennt z ≈ 2,4.")
row(id="2017-bb-ea-cas-B3.1e", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="e", seite="7", punkte="4",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Strecke in einer geneigten Ebene über einen Höhenschnitt bestimmen",
    typ_neben="Streckenlänge im Raum berechnen|Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen",
    stichwoerter="Vordach|geneigte Wand|Höhenschnitt|äußere Vordachkante|y-Koordinate",
    voraussetzungen="Koordinatengleichung nach einer Koordinate auflösen|Satz des Pythagoras anwenden|Maße aus einer Abbildung entnehmen",
    format="Rechnung|Begründung",
    operator="Weisen Sie nach|Bestimmen Sie",
    antwort="Zahl|Text",
    material="Figur",
    skizze=SK31,
    kontext="Camping",
    textumfang="lang",
    gegeben="Die Zeltwand CDS liegt in der Ebene F: 39y + 25z = 195, mit C(5 | 5 | 0) und D(0 | 5 | 0). Ein Teil dieser Wand wird mithilfe zweier Stangen zu einem waagerechten Vordach in 1,80 m Höhe aufgespannt; die dadurch entstehende Öffnung ist im Modell ein Rechteck, dessen eine Seite so auf der Strecke CD liegt, dass der eine Endpunkt von C ebenso weit entfernt ist wie der andere von D. Die Breite des Vordachs beträgt laut Abbildung 1,40 m; 1 LE entspricht 1 m. Alle Punkte der Vordachkante, an deren Enden die beiden Stangen befestigt sind, haben im Modell die gleiche y-Koordinate. [Zur Kontrolle: Die y-Koordinate beträgt etwa 5,98.]",
    gesucht="Nachweis, dass die Länge des Vordachs etwa 2,14 m beträgt; y-Koordinate der äußeren Vordachkante",
    verfahren="Die Klappkante des Rechtecks liegt in der Wandebene in 1,80 m Höhe: aus 39y + 25 · 1,8 = 195 folgt y = 150/39 ≈ 3,846. Die Vordachlänge ist die Rechteckseite von der Bodenkante CD (y = 5, z = 0) bis zu dieser Kante, in der Wandebene gemessen, also √((5 − 3,846)² + 1,8²). Das waagerechte Vordach klappt diese Länge senkrecht zu CD nach außen, die äußere Kante liegt also bei y = 3,846 + 2,138.",
    schritte="5",
    zahlenraum="dezimal|Wurzel",
    einheiten="m",
    ergebnis="y(z = 1,8) = 150/39 ≈ 3,846; die Länge beträgt √(1,154² + 1,8²) ≈ 2,138 m, also etwa 2,14 m. Die äußere Vordachkante hat die y-Koordinate 3,846 + 2,138 ≈ 5,98.",
    zwischenergebnis="y(z = 1,8) ≈ 3,846|Differenz in y-Richtung ≈ 1,154|Vordachlänge ≈ 2,138",
    niveau_geschaetzt="II",
    fehlerquelle="die Vordachlänge als waagerechten Abstand messen und die Neigung der Zeltwand außer Acht lassen, oder die äußere Kante von der Bodenkante y = 5 statt von der Klappkante aus abtragen",
    abhaengig_von="",
    bemerkung="Poolaufgabe (nicht erfasst): 2017MerhoehtBAGLAA2CAS2-1e. CAS-Nachtrag zu 2017-bb-ea-B3.1e (WTR): zusätzlicher Auftrag – y-Koordinate der äußeren Vordachkante bestimmen, mit Kontrollangabe etwa 5,98 (in der WTR-Fassung eine Angabe in Teilaufgabe f); 4 statt 3 BE. Die Maße 1,80 m und 1,40 m stehen nur in Abbildung 2. Kontrollangabe durch eigene Rechnung bestätigt (5,984). Schätzung: die WTR-Zeile trägt III; die übernommene Schätzung folgt dem Standardbezug der Poolfassung (Anforderungsbereich II), Vorrang des Amtlichen (Kern § 5). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B3.1f", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="f", seite="7", punkte="5",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Ganzzahligen Scharparameter aus einer Bereichsbedingung an den Durchstoßpunkt bestimmen",
    typ_neben="Schnittpunkt von Gerade und Ebene berechnen",
    stichwoerter="Sonnenstrahl|Richtungsvektor mit Parameter|Vordach|ganzzahlige Lösung",
    voraussetzungen="Geradengleichung aus Punkt und Richtungsvektor aufstellen|Parameter aus einer Koordinatenbedingung bestimmen|Lösungsbereich abschätzen",
    format="Rechnung",
    operator="Ermitteln Sie|Geben Sie an",
    antwort="Zahl",
    material="Figur",
    skizze="Dieselbe Abbildung 2 wie in Teilaufgabe e: Zelt als Schrägbild mit dunkel ausgefülltem waagerechtem Vordach an der rechten vorderen Wand, zwei Stützstangen und den Maßangaben 1,80 m für die Höhe und 1,40 m für die Breite.",
    kontext="Camping",
    textumfang="lang",
    gegeben="Zelt als Pyramide ABCDS mit dem Bodenmittelpunkt M(2,5 | 2,5 | 0). Das waagerechte Vordach liegt in 1,80 m Höhe, ist 1,40 m breit und mittig zur Kante CD angesetzt; seine wandseitige Kante liegt bei y ≈ 3,85, die äußere Kante nach dem Kontrollergebnis aus Teilaufgabe e bei y ≈ 5,98. Auf das Zelt treffendes Sonnenlicht verläuft längs paralleler Geraden mit dem Richtungsvektor (0,5 | −4,2 | a) und fällt durch ein kleines Loch im Vordach genau auf den Mittelpunkt des Zeltbodens; für a kommen verschiedene ganzzahlige Werte infrage.",
    gesucht="Ein möglicher ganzzahliger Wert für a und die Koordinaten des zugehörigen Punktes, der eine mögliche Position des Lochs im Vordach darstellt",
    verfahren="Gerade durch M mit dem gegebenen Richtungsvektor ansetzen und die Vordachhöhe z = 1,8 fordern: t = 1,8/a. Damit sind x = 2,5 + 0,5 · 1,8/a und y = 2,5 − 4,2 · 1,8/a. Das Loch muss auf dem Vordach liegen, also y zwischen 3,85 und 5,98 und x zwischen 1,8 und 3,2; das führt auf negative ganzzahlige Werte von a.",
    schritte="6",
    zahlenraum="dezimal|negativ",
    einheiten="m",
    ergebnis="Möglich sind a = −3, a = −4 und a = −5. Für a = −3 ist t = −0,6 und das Loch liegt bei (2,2 | 5,02 | 1,8).",
    zwischenergebnis="t = 1,8/a|a = −4: (2,275 | 4,39 | 1,8)|a = −5: (2,32 | 4,012 | 1,8)",
    niveau_geschaetzt="III",
    fehlerquelle="das Vorzeichen von a nicht prüfen und einen Punkt außerhalb des Vordachs angeben",
    abhaengig_von="2017-bb-ea-cas-B3.1e",
    bemerkung="Poolaufgabe (nicht erfasst): 2017MerhoehtBAGLAA2CAS2-1f. CAS-Nachtrag zu 2017-bb-ea-B3.1f (WTR): Auftrag, Zahlen und BE (5) gleich; der Hinweis der WTR-Fassung, dass die äußere Vordachkante die y-Koordinate 5,98 hat, entfällt – in der CAS-Fassung ist der Wert Kontrollergebnis von Teilaufgabe e (daher abhängig von e). Typ und Ergebnis wie in der WTR-Zeile; die Schätzung III der WTR-Zeile deckt sich mit dem Standardbezug der Poolfassung. Die wandseitige Kante bei y ≈ 3,85 steht im Heft nicht ausdrücklich. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 4.2 CAS: Freizeit (Seite 10, 25 BE; Zeilen a, b, d = 16 BE)
row(id="2017-bb-ea-cas-B4.2a", block="B", aufgabe="4.2", titel="Freizeit", teilaufgabe="a", seite="10", punkte="8",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="Bernoulli-Kette|erster Treffer|festgelegte Positionen|Intervallwahrscheinlichkeit",
    voraussetzungen="Pfadregel für unabhängige Wiederholungen anwenden|strikte Ungleichungen in ganzzahlige Grenzen übersetzen|kumulierte Binomialwahrscheinlichkeit mit dem CAS berechnen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Freizeitverhalten",
    textumfang="lang",
    gegeben="In der deutschen Bevölkerung ab 14 Jahre sehen 96 % mindestens einmal pro Woche fern, 72,6 % lesen gern und 60,3 % arbeiten gern am Computer. Ereignis A: Zufällig ausgewählte Personen werden nacheinander befragt, erst die fünfte antwortet, dass sie gern am Computer arbeitet. Ereignis B: Von acht zufällig ausgewählten Personen arbeiten nur die dritte und die fünfte gern am Computer. Ereignis C: Unter 100 zufällig ausgewählten Personen befinden sich mehr als 78 und weniger als 92, die mindestens einmal pro Woche fernsehen.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A, B und C",
    verfahren="A als Kette von vier Nichttreffern und einem Treffer: 0,397⁴ · 0,603. B mit festgelegten Positionen über die Pfadregel ohne Binomialkoeffizient: 0,603² · 0,397⁶. C als Binomialverteilung mit n = 100 und p = 0,96 über P(79 ≤ X ≤ 91) = P(X ≤ 91) − P(X ≤ 78), mit dem CAS.",
    schritte="6",
    zahlenraum="dezimal|Prozent|Potenz",
    einheiten="",
    ergebnis="P(A) = 0,397⁴ · 0,603 ≈ 0,0150; P(B) = 0,603² · 0,397⁶ ≈ 0,00142; P(C) = P(79 ≤ X ≤ 91) ≈ 0,0190.",
    zwischenergebnis="0,397⁴ ≈ 0,02484|P(X ≤ 91) ≈ 0,0190|P(X ≤ 78) ≈ 6 · 10⁻¹¹|Erwartungswert 96",
    niveau_geschaetzt="II",
    fehlerquelle="bei C die Grenzen 78 und 92 mitzählen, obwohl die Ungleichungen streng sind, oder bei B den Binomialkoeffizienten ansetzen, obwohl die Positionen der beiden Treffer festgelegt sind",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B4.2a (WTR): Ereignisse A und B gleich, C geändert – statt „unter 20 mehr als 18“ jetzt „unter 100 mehr als 78 und weniger als 92“ (Intervall bei großem n statt Summe zweier Einzelwerte); BE gleich (8). P(C) ist klein, weil der Erwartungswert 96 oberhalb des Intervalls liegt. Drei Ereignisse in einer Einheit, zwei davon Pfadprodukte (ein Typ); thema folgt dem Typ. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B4.2b", block="B", aufgabe="4.2", titel="Freizeit", teilaufgabe="b", seite="10", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen",
    typ_neben="",
    stichwoerter="Höchstanzahl|Gegenereignis|Logarithmus|Stichprobenumfang",
    voraussetzungen="Gegenereignis bilden|Exponentialungleichung durch Logarithmieren oder mit dem CAS lösen|auf die nächste ganze Zahl abrunden",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Freizeitverhalten",
    textumfang="mittel",
    gegeben="72,6 % der deutschen Bevölkerung ab 14 Jahre lesen in ihrer Freizeit gern, die übrigen 27,4 % nicht.",
    gesucht="Größte Anzahl zufällig ausgewählter Personen, für die die Wahrscheinlichkeit, wenigstens eine Person zu finden, die in ihrer Freizeit nicht gern liest, unter 98 % liegt",
    verfahren="Gegenereignis: alle Ausgewählten lesen gern. Aus 1 − 0,726ⁿ < 0,98 folgt 0,726ⁿ > 0,02, also n < ln 0,02 / ln 0,726 ≈ 12,22; abrunden und mit n = 12 und n = 13 prüfen.",
    schritte="4",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    ergebnis="n < 12,22, es dürften also höchstens 12 Personen ausgewählt werden (n = 12: 1 − 0,726¹² ≈ 0,9786 < 0,98; n = 13: ≈ 0,9844).",
    zwischenergebnis="0,726ⁿ > 0,02|ln 0,02 / ln 0,726 ≈ 12,22",
    niveau_geschaetzt="II",
    fehlerquelle="wie bei der Mindestanzahl aufrunden oder beim Logarithmieren mit negativem Logarithmus das Ungleichheitszeichen nicht umdrehen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B4.2b (WTR): Frage umgekehrt – höchstens statt mindestens, Wahrscheinlichkeit unter statt mindestens 98 %; Ergebnis 12 statt 13, BE gleich (4). Gleicher Lösungsweg (Gegenereignis, Logarithmieren), nur die Rundungsrichtung kehrt sich um; deshalb derselbe Typ, obwohl sein Etikett „Mindestanzahl“ nennt (Vorschlag zur Typenliste im Bericht). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-bb-ea-cas-B4.2d", block="B", aufgabe="4.2", titel="Freizeit", teilaufgabe="d", seite="10", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Modalwert einer Binomialverteilung bestimmen",
    stichwoerter="Stornierung|Binomialformel|Term angeben|größte Wahrscheinlichkeit",
    voraussetzungen="Bernoulli-Kette erkennen|Binomialformel mit dem Binomialkoeffizienten aufschreiben|Erwartungswert n · p als Orientierung nutzen",
    format="Rechnung|Kurzantwort",
    operator="Geben Sie an|Ermitteln Sie",
    antwort="Term|Zahl",
    material="keins",
    skizze="keine",
    kontext="Lesung / Kartenverkauf",
    textumfang="lang",
    gegeben="Ein Buchhändler organisiert eine Lesung in einem Saal mit 175 Plätzen. Da im Mittel 6 % der bestellten Karten storniert werden, lässt er 180 Kartenreservierungen annehmen. k ist die Anzahl der stornierten Karten.",
    gesucht="Term für P(k), mit dem die Wahrscheinlichkeit für genau k Stornierungen berechnet werden kann; größter Wert dieser Wahrscheinlichkeit",
    verfahren="Bernoulli-Kette mit n = 180 und p = 0,06: P(k) = C(180; k) · 0,06^k · 0,94^(180 − k). Der größte Wert liegt beim Modalwert in der Nähe des Erwartungswerts n · p = 10,8; die Werte um 10 und 11 mit dem CAS vergleichen.",
    schritte="4",
    zahlenraum="dezimal|Prozent|Potenz",
    einheiten="",
    ergebnis="P(k) = C(180; k) · 0,06^k · 0,94^(180 − k); der größte Wert wird bei k = 10 erreicht: P(10) ≈ 0,1246 gegenüber P(11) ≈ 0,1230 und P(9) ≈ 0,1142.",
    zwischenergebnis="Erwartungswert n · p = 10,8",
    niveau_geschaetzt="II",
    fehlerquelle="den größten Wert beim gerundeten Erwartungswert 11 vermuten oder die Stornierungen mit p = 0,94 als Treffer ansetzen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2017-bb-ea-B4.2d (WTR): Wortlaut der Teilaufgabe gleich, Angabe im Aufgabenstamm geändert – 6 % statt 5 % Stornierungen; größter Wert bei k = 10 statt bei k = 9, BE gleich (4). Die geänderte Stammangabe berührt Teilaufgabe e nicht (dort gleiche Rechnung, keine Zeile). Die Saalkapazität von 175 Plätzen wird nicht gebraucht. Eigene Rechnung, mit sympy bestätigt.")

NEUE_TYPEN = [
    ("Identische Graphen einer Schar zu entgegengesetzten Parameterwerten begründen", "Analysis", "Funktionsscharen und Ortskurven",
     "Am Scharterm zeigen, dass f_(−a) = f_a für alle x gilt, dass also zu jedem Parameterwert ein zweiter, entgegengesetzter mit identischem Graphen gehört (Symmetrie im Parameter, nicht in x).",
     "2017-bb-ea-cas-B2.2d"),
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
