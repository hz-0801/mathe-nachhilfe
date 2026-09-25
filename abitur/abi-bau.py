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
    "jahr": "2018",
    "papier": "2018-bb-ea-cas",
    "datei": "hefte/abi/2018-bb-ea-cas.pdf",  # amtliches Heft (Bildungsserver, BB_18_Ma_CAS_Aufgaben_1/_2), 12 Seiten mit Textebene, lokal (abi-quellen.md § 2, § 8)
    "seiten": 12,
    # CAS-Nachtrag (v0.14, abi.md § 7): Zeilen nur für Teilaufgaben, die von der
    # WTR-Fassung 2018-bb-ea abweichen (Wortlaut, Angaben, gesuchtes Ergebnis
    # oder BE). „CAS:“ im Titel tragen 2.1 Vase, 2.2 Gartenteich, 3.1 Museum und
    # 4.2 Brillenträger; Teil 1 (1.1–1.3), 3.2 und 4.1 sind wortgleich mit gleichen
    # BE (Textvergleich aller Teilaufgaben, Seiten gerendert). Die WTR-Fassung hat
    # 13 Seiten, die CAS-Fassung 12: die Anlage zu 4.2 (Tafel der summierten
    # Binomialverteilungen) fehlt.
    "nachtrag_zu": "2018-bb-ea",
    # BE der abweichenden Teilaufgaben je „CAS:“-Aufgabe (BE-Tabellen der CAS-Fassung):
    # 2.1 c 3, d 5, e 7, f 5, g 5, h 5 (neu) = 30; 2.2 b 5, d 6, e 8, f 9, g 3,
    # i 5 (neu) = 36; 3.1 f 6; 4.2 d 5.
    "soll": {"2.1": 30, "2.2": 36, "3.1": 6, "4.2": 5},
    # wortgleiche Teilaufgaben der „CAS:“-Aufgaben ohne Zeile: CAS-Buchstabe → (WTR-Buchstabe, BE)
    "uebernommen": {"2.1": {"a": ("a", 8), "b": ("b", 3), "i": ("h", 2), "j": ("i", 7)},
                    "2.2": {"a": ("a", 6), "c": ("c", 2), "h": ("h", 6)},
                    "3.1": {"a": ("a", 4), "b": ("b", 3), "c": ("c", 5), "d": ("d", 4), "e": ("e", 3)},
                    "4.2": {"a": ("a", 5), "b": ("b", 4), "c": ("c", 5), "e": ("e", 6)}},
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
# Heft 2018-bb-ea-cas (amtliches Heft BB_18_Ma_CAS_Aufgaben_1/_2, 12 Seiten mit
# Textebene; CAS-Nachtrag zu 2018-bb-ea, Auftrag Nacht 2026-09-27, Teil 9).
# Zeilen nur für Teilaufgaben, die von der WTR-Fassung abweichen (abi.md § 7);
# Textvergleich aller Teilaufgaben beider Hefte, jede Aufgabenseite gerendert.
# „CAS:“-Aufgaben 2.1, 2.2, 3.1, 4.2; Teil 1, 3.2 und 4.1 wortgleich.
# Pool: 3.1 Museum ist die Poolaufgabe 2018 erhöht Teil B AG/LA (A2) CAS 1
# (Stapel 2018-ea-B, CAS-Zweig, Reserve) – Vormerkung in f.
ST21 = "Funktionenschar f_a mit f_a(x) = (x² + a) · e^(0,5 − x), a ∈ IR; die Graphen der Schar sind G_a."
SK21 = "Abbildung 2 (Anlage, PDF-Seite 6): Koordinatensystem, x-Achse mit Teilstrichen 1, 2, 3, y-Achse mit Teilstrich 1. Der mit G_0,65 beschriftete Graph beginnt auf der y-Achse bei etwa 1,07, fällt leicht bis etwa x = 0,4, steigt zu einem flachen Hochpunkt bei etwa x = 1,6 und fällt dann bis x = 3 auf etwa 0,79. Die Fläche zwischen Graph und x-Achse über [0; 3] ist grau ausgefüllt und rechts durch eine senkrechte Strecke bei x = 3 begrenzt."
VASE = "Die Funktion f_0,65 mit f_0,65(x) = (x² + 0,65) · e^(0,5 − x) aus der Schar; ihr Graph schließt über [0; 3] mit der x-Achse eine Fläche ein (Abbildung 2). Durch Rotation dieser Fläche um die x-Achse entsteht ein Körper, der modellhaft einer liegenden, nach links geöffneten Vase entspricht; 1 LE = 1 dm."
ST22 = "Funktionenschar f_a mit f_a(x) = (1/a)·x³ + 3x² + 5x + 2a; x ∈ IR, a ∈ IR, a ≠ 0, und die Funktion h mit h(x) = −(1/2)·x^(−3); x ∈ IR, x ≠ 0. Die zugehörigen Graphen sind G_a und K."
TEICH = " Ein Gartenbesitzer hat in einer Ecke seines Gartens einen Teich angelegt. Der Rand des Teiches an der Wasseroberfläche wird durch die Graphen G_2 und K modelliert. Im Intervall von −3 bis −2 verläuft eine Brücke über den Teich; 1 LE = 1 m. Eine Darstellung zeigt Teichoberfläche und Brücke senkrecht von oben betrachtet."
SK22 = "Kartesisches Koordinatensystem, x-Achse von −4 bis 0 mit den ganzen Zahlen beschriftet, y-Achse von −1 bis 3 mit den ganzen Zahlen beschriftet. Zwei Kurvenstücke umranden gemeinsam eine geschlossene, längliche Fläche: der mit G_2 beschriftete Bogen läuft von (−4 | 0) steil aufwärts zu einem Hochpunkt bei etwa (−2,8 | 2,5), fällt zu einem flachen Tiefpunkt bei etwa (−1,2 | 1,5) und steigt wieder bis etwa (−0,64 | 1,9); das mit K beschriftete Kurvenstück läuft von (−4 | 0) flach knapp oberhalb der x-Achse nach rechts und biegt ab etwa x = −1 steil nach oben bis (−0,64 | 1,9). Über dem senkrechten Streifen zwischen x = −3 und x = −2 liegt ein blassrot hinterlegtes Rechteck, das die Brücke darstellt; es reicht oben und unten über die Fläche hinaus."
ST31 = "Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG dargestellt. Die obere Etage entspricht der Pyramide DEFG, die untere Etage dem Körper ABCDEF, der Teil der Pyramide DEFS ist. Das Dreieck ABC liegt in der x-y-Ebene, das Dreieck DEF parallel dazu. Im kartesischen Koordinatensystem gilt A(−5 | 5 | 0), B(−5 | 25 | 0), D(0 | 0 | 15), E(0 | 30 | 15), F(−25 | 5 | 15) und G(−10 | 10 | 35). Eine Längeneinheit entspricht 1 m in der Realität."
SK31 = "Schrägbild eines Körpers ohne Koordinatensystem. Oben liegt die Spitze G; von ihr führen Kanten zu den Ecken eines waagerecht liegenden, grau getönten Dreiecks DEF mit F links, E rechts und D vorn in der Mitte. Darunter liegt ein kleineres, ebenfalls grau getöntes Dreieck ABC mit C links, B rechts und A vorn. Die Seitenkanten FC, DA und EB verbinden die beiden Dreiecke zum Körper. Von C, A und B laufen gestrichelte Linien nach unten aufeinander zu und treffen sich in einem mit S bezeichneten Punkt unterhalb des Körpers. Die Abbildung trägt keine Maßangaben."
ST42 = "In einer großen Gemeinde tragen 62,5 % der Bevölkerung eine Brille. Bei den Frauen beträgt der Anteil 64,8 %. Bekannt ist außerdem, dass 52,1 % der Bevölkerung Frauen sind."
# ---- Aufgabe 2.1 CAS: Vase (Seiten 5–6, 50 BE; Zeilen c, d, e, f, g, h = 30 BE)
row(id="2018-bb-ea-cas-B2.1c", block="B", aufgabe="2.1", titel="Vase", teilaufgabe="c", seite="5", punkte="3",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    typ_neben="",
    stichwoerter="Flächeninhalt|Differenzfunktion|Integral|Randgeraden",
    voraussetzungen="Differenzfunktion bilden|bestimmtes Integral mit dem CAS oder über eine Stammfunktion auswerten",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben=ST21 + " Die Graphen G_2 und G_0, die y-Achse und die Gerade mit der Gleichung x = 3 schließen eine Fläche ein.",
    gesucht="Inhalt A der eingeschlossenen Fläche",
    verfahren="Differenzfunktion f_2 − f_0 = 2 · e^(0,5 − x) bilden und über dem Intervall [0; 3] integrieren, mit dem CAS oder über die Stammfunktion −2 · e^(0,5 − x); da G_2 dort vollständig oberhalb von G_0 liegt, ist kein Vorzeichenwechsel zu beachten.",
    schritte="3",
    zahlenraum="dezimal|Potenz",
    einheiten="",
    ergebnis="A = 2 · (e^0,5 − e^(−2,5)) ≈ 3,13 (FE)",
    zwischenergebnis="f_2(x) − f_0(x) = 2 · e^(0,5 − x)",
    niveau_geschaetzt="II",
    fehlerquelle="beide Funktionen einzeln integrieren und die Differenz der Beträge bilden, oder die Integrationsgrenzen vertauschen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.1c (WTR): Wortlaut und Angaben gleich, 3 statt 4 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt (3,1332725).")
row(id="2018-bb-ea-cas-B2.1d", block="B", aufgabe="2.1", titel="Vase", teilaufgabe="d", seite="5", punkte="5",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameterwerte nach der Anzahl der Extrempunkte über die Lösbarkeit der Extremstellengleichung begründen",
    typ_neben="Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden",
    stichwoerter="Extrempunkt|Funktionenschar|Diskriminante|notwendige Bedingung|ohne Kontrollangabe",
    voraussetzungen="Produkt- und Kettenregel anwenden oder mit dem CAS ableiten|quadratische Gleichung mit Parameter diskutieren",
    format="Rechnung|Begründung",
    operator="Weisen Sie nach",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben=ST21 + " Betrachtet wird der Fall a > 1.",
    gesucht="Nachweis, dass die Graphen G_a für a > 1 keine Extrempunkte besitzen",
    verfahren="f_a′ mit Produkt- und Kettenregel oder mit dem CAS bilden: f_a′(x) = (−x² + 2x − a) · e^(0,5 − x). f_a′(x) = 0 setzen; wegen e^(0,5 − x) > 0 bleibt x² − 2x + a = 0 mit x = 1 ± √(1 − a). Für a > 1 ist der Radikand negativ, es gibt keine reelle Lösung und damit keinen Extrempunkt.",
    schritte="4",
    zahlenraum="ganz|Wurzel|Potenz",
    einheiten="",
    ergebnis="f_a′(x) = (−x² + 2x − a) · e^(0,5 − x). Aus f_a′(x) = 0 folgt x² − 2x + a = 0, also x = 1 ± √(1 − a). Für a > 1 ist 1 − a < 0; die Gleichung hat keine reelle Lösung. Da die notwendige Bedingung nirgends erfüllt ist, besitzt G_a keine Extrempunkte.",
    zwischenergebnis="f_a′(x) = (−x² + 2x − a) · e^(0,5 − x)",
    niveau_geschaetzt="II",
    fehlerquelle="beim Ableiten die innere Ableitung −1 des Exponenten vergessen oder die Nichtexistenz nur an Beispielen zeigen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.1d (WTR): Wortlaut gleich, aber ohne die Kontrollangabe f_a′(x) = (−x² + 2x − a) · e^(0,5 − x) der WTR-Fassung – die Ableitung wird selbst gebildet; BE gleich (5). Typ, Nebentyp und Ergebnis wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-bb-ea-cas-B2.1e", block="B", aufgabe="2.1", titel="Vase", teilaufgabe="e", seite="5", punkte="7",
    leitidee="Analysis", thema="Ableitungsregeln",
    typ="Ableitung eines Produkts mit e-Funktion in vorgegebener Form nachweisen",
    typ_neben="Krümmungsverhalten aus der zweiten Ableitung deuten",
    stichwoerter="zweite Ableitung|Produktregel|Krümmung|Flachpunkt",
    voraussetzungen="zweite Ableitung mit Produkt- und Kettenregel oder mit dem CAS bilden|Terme zusammenfassen|Vorzeichen eines Produkts beurteilen",
    format="Rechnung|Begründung",
    operator="Weisen Sie nach|Erläutern Sie",
    antwort="Term|Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Die Funktion f_2 mit f_2(x) = (x² + 2) · e^(0,5 − x) aus der Schar f_a mit f_a(x) = (x² + a) · e^(0,5 − x), a ∈ IR.",
    gesucht="Nachweis von f_2″(x) = (x − 2)² · e^(0,5 − x); Schlussfolgerungen über den Verlauf von G_2",
    verfahren="f_2 zweimal ableiten (mit dem CAS oder mit Produkt- und Kettenregel, die erste Ableitung aus d) und den Term als vollständiges Quadrat zusammenfassen. Dann das Vorzeichen beurteilen: Quadrat und Exponentialfaktor sind nicht negativ, die Nullstelle bei x = 2 ist doppelt, also ohne Vorzeichenwechsel.",
    schritte="4",
    zahlenraum="ganz|Potenz",
    einheiten="",
    ergebnis="f_2″(x) = (x − 2)² · e^(0,5 − x). Da (x − 2)² ≥ 0 und e^(0,5 − x) > 0 ist, gilt f_2″(x) ≥ 0 für alle x, mit Gleichheit nur bei x = 2 und ohne Vorzeichenwechsel. G_2 ist also auf ganz IR linksgekrümmt, besitzt keinen Wendepunkt und hat bei x = 2 einen Flachpunkt.",
    zwischenergebnis="f_2′(x) = (−x² + 2x − 2) · e^(0,5 − x)",
    niveau_geschaetzt="III",
    fehlerquelle="die Nullstelle von f_2″ bei x = 2 als Wendestelle deuten, ohne den Vorzeichenwechsel zu prüfen",
    abhaengig_von="2018-bb-ea-cas-B2.1d",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.1e (WTR): Wortlaut gleich, 7 statt 8 BE; die erste Ableitung ist in der CAS-Fassung nicht als Kontrollangabe in d vorgegeben, deshalb abhängig von der CAS-Zeile d. Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-bb-ea-cas-B2.1f", block="B", aufgabe="2.1", titel="Vase", teilaufgabe="f", seite="5", punkte="5",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen",
    typ_neben="Näherung durch die Tangente mit dem Funktionswert im Sachzusammenhang vergleichen",
    stichwoerter="Tangente|Linearisierung|relative Abweichung|Prozent",
    voraussetzungen="Ableitung als Steigung nutzen|Punkt-Steigungs-Form|relativen Anteil berechnen",
    format="Rechnung",
    operator="Ermitteln Sie|Zeigen Sie",
    antwort="Term|Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Die Funktion f_2 mit f_2(x) = (x² + 2) · e^(0,5 − x); G_2 verläuft im Intervall [1; 3] annähernd geradlinig und wird vereinfacht durch die Tangente t in x = 2 dargestellt. Zur Kontrolle ist angegeben: t(x) = −2 · e^(−1,5) · x + 10 · e^(−1,5).",
    gesucht="Gleichung der Tangente t; Nachweis, dass t(1) um weniger als 2 % von f_2(1) abweicht",
    verfahren="f_2(2) und f_2′(2) berechnen (mit dem CAS) und in die Punkt-Steigungs-Form einsetzen. Dann t(1) und f_2(1) bestimmen und die Differenz auf f_2(1) beziehen.",
    schritte="5",
    zahlenraum="dezimal|Prozent|Potenz",
    einheiten="",
    ergebnis="t(x) = −2 · e^(−1,5) · x + 10 · e^(−1,5). Mit t(1) = 8 · e^(−1,5) ≈ 1,785 und f_2(1) = 3 · e^(−0,5) ≈ 1,820 beträgt die relative Abweichung rund 1,90 % und liegt damit unter 2 %.",
    zwischenergebnis="f_2(2) = 6 · e^(−1,5)|f_2′(2) = −2 · e^(−1,5)|Differenz ≈ 0,0346",
    niveau_geschaetzt="II",
    fehlerquelle="die Abweichung auf den Tangentenwert statt auf den Funktionswert beziehen oder absolut statt relativ vergleichen",
    abhaengig_von="2018-bb-ea-cas-B2.1d",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.1f (WTR): Wortlaut und Angaben gleich, 5 statt 6 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Die Kontrollangabe des Hefts steht in gegeben und ist durch eigene Rechnung bestätigt. Eigene Rechnung, mit sympy bestätigt (1,89882 %).")
row(id="2018-bb-ea-cas-B2.1g", block="B", aufgabe="2.1", titel="Vase", teilaufgabe="g", seite="5|6", punkte="5",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Stellen mit maximalem Funktionswert einschließlich Rand bestimmen",
    typ_neben="",
    stichwoerter="Randextremum|lokales Maximum|Rotationskörper|Radius",
    voraussetzungen="notwendige und hinreichende Bedingung anwenden|Randwerte eines Intervalls prüfen|Gleichungen mit dem CAS lösen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze=SK21,
    kontext="Vase / Rotationskörper",
    textumfang="mittel",
    gegeben=VASE + " Die Vase nimmt an zwei verschiedenen Stellen einen maximalen Radius von ca. 1,07 dm an.",
    gesucht="die beiden Stellen, an denen der Radius maximal ist, rechnerisch ermittelt",
    verfahren="Der Radius an der Stelle x ist f_0,65(x). Nullstellen der Ableitung bestimmen: x² − 2x + 0,65 = 0 liefert x = 1 ± √0,35, davon ist x ≈ 0,41 ein lokales Minimum und x ≈ 1,59 ein lokales Maximum. Zusätzlich die Randwerte bei x = 0 und x = 3 vergleichen; der linke Rand liefert denselben gerundeten Radius wie das lokale Maximum.",
    schritte="5",
    zahlenraum="dezimal|Wurzel|Potenz",
    einheiten="dm",
    ergebnis="Die beiden Stellen sind x₁ = 0 mit f_0,65(0) = 0,65 · √e ≈ 1,072 dm (Randstelle) und x₂ = 1 + √0,35 ≈ 1,592 mit f_0,65(x₂) ≈ 1,069 dm (lokales Maximum).",
    zwischenergebnis="x = 1 ± √0,35, also 0,408 und 1,592|f_0,65(0,408) ≈ 0,895 (lokales Minimum)|f_0,65(3) ≈ 0,792",
    niveau_geschaetzt="III",
    fehlerquelle="nur die Nullstellen der Ableitung untersuchen und die Randstelle x = 0 übersehen",
    abhaengig_von="2018-bb-ea-cas-B2.1d",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.1g (WTR): „Ermitteln Sie diese beiden Stellen rechnerisch“ statt „Bestimmen Sie diese beiden Stellen“, 5 statt 7 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Die Angabe „ca. 1,07“ verdeckt, dass die beiden Radien nicht gleich sind (1,0717 gegen 1,0685). Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-bb-ea-cas-B2.1h", block="B", aufgabe="2.1", titel="Vase", teilaufgabe="h", seite="5|6", punkte="5",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Rotationsvolumen um die x-Achse berechnen",
    typ_neben="",
    stichwoerter="Rotationsvolumen|Fassungsvermögen|Materialanteil|Liter",
    voraussetzungen="Formel V = π · ∫ (f(x))² dx kennen|Integral mit dem CAS berechnen|1 dm³ = 1 l kennen|Prozentanteil abziehen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze=SK21,
    kontext="Vase / Rotationskörper",
    textumfang="mittel",
    gegeben=VASE + " Der Materialanteil am gesamten Volumen der Vase beträgt 10 %.",
    gesucht="Fassungsvermögen der Vase in Liter",
    verfahren="Das Gesamtvolumen der Vase ist das Rotationsvolumen V = π · ∫ (f_0,65(x))² dx über [0; 3], mit dem CAS berechnet. Das Material nimmt 10 % davon ein, das Fassungsvermögen ist also 90 % von V; 1 dm³ = 1 l.",
    schritte="3",
    zahlenraum="dezimal|Prozent|Potenz",
    einheiten="dm³|l",
    ergebnis="V ≈ 8,98 dm³; das Fassungsvermögen beträgt 0,9 · V ≈ 8,08 l.",
    zwischenergebnis="V = π · ∫ (f_0,65(x))² dx ≈ 8,982 dm³",
    niveau_geschaetzt="II",
    fehlerquelle="die Funktion statt ihres Quadrats integrieren oder den Materialanteil nicht abziehen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag, ohne WTR-Gegenstück: die Teilaufgabe steht nur in der CAS-Fassung; die CAS-Teilaufgaben i und j entsprechen den WTR-Teilaufgaben h und i. Neuer Typ: der Bestand führt unter Rotationsvolumen keinen Typ für das bloße Berechnen eines Rotationsvolumens um die x-Achse. Exakt V = 3π · (343 · e^6 − 25223) · e^(−5) / 800 ≈ 8,982 dm³ (die WTR-Zeile h nennt b(3) ≈ 8,98 dm³). Den Materialanteil am gesamten Volumen als Anteil am Rotationsvolumen gelesen. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 2.2 CAS: Gartenteich (Seiten 7–8, 50 BE; Zeilen b, d, e, f, g, i = 36 BE)
row(id="2018-bb-ea-cas-B2.2b", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="b", seite="7", punkte="5",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen",
    typ_neben="Tangentengleichung in einem Punkt des Graphen aufstellen",
    stichwoerter="Tangente|Berührpunkt|Achsenabschnitte|rechtwinkliges Dreieck|Flächeninhalt",
    voraussetzungen="Ableitung einer Potenzfunktion mit negativem Exponenten bilden|Nullstelle einer linearen Funktion berechnen|Flächeninhalt eines rechtwinkligen Dreiecks aus den Katheten bilden",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="mittel",
    gegeben=ST22 + " Die Tangente an K im Punkt P(−1 | h(−1)) und die beiden Koordinatenachsen begrenzen ein Dreieck.",
    gesucht="Flächeninhalt dieses Dreiecks",
    verfahren="h(−1) = 0,5 berechnen, h′(x) = (3/2)·x^(−4) bilden und h′(−1) = 1,5 als Anstieg nehmen. Die Tangente t(x) = 1,5x + 2 schneidet die y-Achse bei 2 und die x-Achse bei −4/3. Diese beiden Abschnitte sind die Katheten des rechtwinkligen Dreiecks; der Flächeninhalt ist ihr halbes Produkt, mit Beträgen gerechnet.",
    schritte="5",
    zahlenraum="Bruch|dezimal|ganz|negativ|Potenz",
    einheiten="",
    ergebnis="A = 4/3 ≈ 1,33 Flächeneinheiten",
    zwischenergebnis="P(−1 | 0,5)|h′(x) = (3/2)·x^(−4)|t(x) = 1,5x + 2|Achsenabschnitte −4/3 und 2",
    niveau_geschaetzt="II",
    fehlerquelle="den negativen x-Achsenabschnitt ohne Betrag in die Flächenformel einsetzen und einen negativen Flächeninhalt erhalten",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.2b (WTR): Wortlaut und Angaben gleich, 5 statt 7 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-bb-ea-cas-B2.2d", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="d", seite="7", punkte="6",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt der Tangente mit vorgegebener Steigung berechnen",
    typ_neben="",
    stichwoerter="Tangentenanstieg|Ableitung gleich 1,5|quadratische Gleichung|Koordinaten der Berührpunkte",
    voraussetzungen="Parameterwert in den Scharterm einsetzen|ganzrationale Funktion ableiten|quadratische Gleichung lösen, auch mit dem CAS|Funktionswerte berechnen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="mittel",
    gegeben=ST22 + " Betrachtet wird der Graph G_2, also der Graph von f_2.",
    gesucht="Koordinaten der zwei Punkte von G_2, in denen die Tangenten an G_2 den Anstieg m = 1,5 haben",
    verfahren="a = 2 einsetzen, also f_2(x) = 0,5x³ + 3x² + 5x + 4, und ableiten zu f_2′(x) = 1,5x² + 6x + 5. Dann f_2′(x) = 1,5 lösen, also 1,5x² + 6x + 3,5 = 0, und die beiden Lösungen in f_2 einsetzen.",
    schritte="4",
    zahlenraum="dezimal|ganz|negativ|Wurzel",
    einheiten="",
    ergebnis="x = −2 ± √15/3; die Punkte sind (−2 − √15/3 | 2 + √15/18) ≈ (−3,29 | 2,22) und (−2 + √15/3 | 2 − √15/18) ≈ (−0,71 | 1,78).",
    zwischenergebnis="f_2(x) = 0,5x³ + 3x² + 5x + 4|f_2′(x) = 1,5x² + 6x + 5|1,5x² + 6x + 3,5 = 0",
    niveau_geschaetzt="II",
    fehlerquelle="f_2′(x) = 0 statt f_2′(x) = 1,5 setzen oder nur die x-Koordinaten angeben",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.2d (WTR): andere Frage – „Ermitteln Sie die Koordinaten von zwei Punkten …“ statt „Zeigen Sie, dass es genau zwei Punkte … gibt“; BE gleich (6). Deshalb ein anderer Typ als in der WTR-Zeile: berechnet werden die Berührpunkte, die Anzahl ist nicht nachzuweisen. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-bb-ea-cas-B2.2e", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="e", seite="7", punkte="8",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameterwert für genau eine waagerechte Tangente bestimmen",
    typ_neben="Nachweisverfahren für einen Sattelpunkt erläutern",
    stichwoerter="waagerechte Tangente|genau eine Lösung|Diskriminante null|Sattelpunkt|Nachweisverfahren beschreiben",
    voraussetzungen="Scharterm nach x ableiten|Diskriminante einer quadratischen Gleichung aufstellen oder die Gleichung mit dem CAS lösen|hinreichende Bedingung für einen Sattelpunkt kennen",
    format="Rechnung|Begründung",
    operator="Bestimmen Sie|Erläutern Sie",
    antwort="Zahl|Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="lang",
    gegeben=ST22 + " Es gibt einen Wert des Parameters a, für den der Graph G_a genau einen Punkt mit waagerechter Tangente besitzt.",
    gesucht="dieser Parameterwert a|Erläuterung, wie sich nachweisen ließe, dass G_a für diesen Parameterwert dort einen Sattelpunkt besitzt",
    verfahren="f_a′(x) = (3/a)·x² + 6x + 5 ist quadratisch; genau eine Nullstelle bedeutet Diskriminante null, also 36 − 60/a = 0 und damit a = 5/3. Für den zweiten Teil genügt die Beschreibung des Verfahrens: zweite Ableitung an der Stelle null und dritte Ableitung dort ungleich null, gleichwertig ein Vorzeichenwechsel der zweiten Ableitung; die Rechnung ist nicht verlangt.",
    schritte="4",
    zahlenraum="Bruch|dezimal|ganz|negativ",
    einheiten="",
    ergebnis="a = 5/3; die waagerechte Tangente liegt bei x = −5/3. Nachweis des Sattelpunkts über f′′(−5/3) = 0 zusammen mit f′′′(−5/3) = 3,6 ≠ 0 oder über den Vorzeichenwechsel von f′′ an dieser Stelle.",
    zwischenergebnis="f_a′(x) = (3/a)·x² + 6x + 5|Diskriminante 36 − 60/a|f′(x) = 1,8x² + 6x + 5|f′′(x) = 3,6x + 6",
    niveau_geschaetzt="III",
    fehlerquelle="„genau ein Punkt mit waagerechter Tangente“ mit „genau ein Extrempunkt“ verwechseln, oder den Fall a < 0 nicht prüfen, in dem die Diskriminante stets positiv ist",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.2e (WTR): Wortlaut und Angaben gleich, 8 statt 9 BE; Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-bb-ea-cas-B2.2f", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="f", seite="7", punkte="9",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Schnittpunkte zweier Graphen mit dem Rechner ermitteln",
    typ_neben="Umschließendes achsenparalleles Rechteck zu einer krummlinig begrenzten Fläche bestimmen",
    stichwoerter="Schnittpunkte der Randkurven|Gleichung sechsten Grades|Rundung auf zwei Nachkommastellen|achsenparalleles Rechteck|lokaler Hochpunkt",
    voraussetzungen="Gleichung f_2(x) = h(x) aufstellen und mit dem CAS lösen|Extremstellen über die erste Ableitung bestimmen|waagerechte und senkrechte Ausdehnung einer Fläche unterscheiden",
    format="Rechnung",
    operator="Ermitteln Sie|Berechnen Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze=SK22,
    kontext="Gartenteich",
    textumfang="lang",
    gegeben=ST22 + TEICH + " Der Teich wird kurzzeitig durch eine rechteckige Plane abgedeckt, deren Seiten parallel zu den Koordinatenachsen liegen.",
    gesucht="Koordinaten der Schnittpunkte von G_2 und K, auf zwei Nachkommastellen gerundet|Seitenlängen, die die Plane mindestens haben muss",
    verfahren="f_2(x) = h(x) mit f_2(x) = 0,5x³ + 3x² + 5x + 4 mit dem CAS lösen (nach Multiplikation mit 2x³ ein Polynom sechsten Grades mit zwei reellen Lösungen) und die y-Koordinaten berechnen. Für die Plane die waagerechte Seite als Differenz der beiden x-Werte nehmen und die senkrechte als Abstand zwischen dem tiefsten Randpunkt (linker Schnittpunkt, weil K steigt) und dem lokalen Hochpunkt von G_2; dazu f_2′(x) = 0 lösen.",
    schritte="6",
    zahlenraum="dezimal|negativ|Wurzel",
    einheiten="m",
    ergebnis="Schnittpunkte S₁(−4,00 | 0,01) und S₂(−0,64 | 1,90). Der Hochpunkt von G_2 liegt bei x = −2 − √6/3 ≈ −2,82 mit y ≈ 2,54. Die Plane muss mindestens etwa 3,36 m lang und 2,54 m breit sein.",
    zwischenergebnis="x^6 + 6x^5 + 10x^4 + 8x^3 + 1 = 0|x₁ ≈ −3,9984 mit y₁ ≈ 0,0078|x₂ ≈ −0,6413 mit y₂ ≈ 1,8953|Hochpunkt (−2,8165 | 2,5443)|Breite 3,3571, Höhe 2,5365",
    niveau_geschaetzt="III",
    fehlerquelle="für die senkrechte Seite nur die y-Werte der beiden Schnittpunkte vergleichen und den Hochpunkt von G_2 übersehen, oder die Mindestmaße abrunden",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.2f (WTR): andere Frage – die Schnittpunkte von G_2 und K werden berechnet und gerundet, statt die vorgegebenen Punkte P₁(−4 | 0) und P₂(−0,64 | 1,9) durch Einsetzen zu bestätigen; im Aufgabenstamm „durch die Graphen G_2 und K“ statt „durch Teile der Graphen“; BE gleich (9). Deshalb ein anderer Haupttyp als in der WTR-Zeile (neu), der Nebentyp Plane bleibt. Der linke Schnittpunkt liegt nicht genau bei −4 (f_2(−4) = 0, h(−4) = 1/128). Mit den gerundeten Werten ergeben sich 3,36 m und 2,53 m, mit den ungerundeten 3,357 m und 2,537 m, als Mindestmaß aufgerundet 3,36 m und 2,54 m. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-bb-ea-cas-B2.2g", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="g", seite="8|7", punkte="3",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    typ_neben="",
    stichwoerter="senkrechter Lichteinfall|Schattenstreifen|Fläche zwischen zwei Graphen|Integrationsgrenzen aus dem Sachtext",
    voraussetzungen="Sachsituation in Integrationsgrenzen übersetzen|bestimmtes Integral mit dem CAS auswerten",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze=SK22,
    kontext="Gartenteich",
    textumfang="lang",
    gegeben=ST22 + TEICH + " Senkrecht zur Teichoberfläche einfallendes Licht erzeugt durch die Brücke einen Schatten, der zum Teil auf der Wasseroberfläche liegt.",
    gesucht="Größe der Wasseroberfläche, die in diesem Fall im Schatten liegt",
    verfahren="Bei senkrechtem Lichteinfall deckt sich der Schatten mit dem Grundriss der Brücke; auf dem Wasser ist das genau der Teil der Teichfläche über dem Intervall von −3 bis −2. Diese Fläche liegt zwischen dem oberen Rand G_2 und dem unteren Rand K, also das Integral von −3 bis −2 über f_2(x) − h(x) bilden, mit dem CAS.",
    schritte="3",
    zahlenraum="Bruch|dezimal|negativ|Potenz",
    einheiten="m²",
    ergebnis="A = 337/144 ≈ 2,34 m²",
    zwischenergebnis="Integrand f_2(x) − h(x) = 0,5x³ + 3x² + 5x + 4 + (1/2)·x^(−3)",
    niveau_geschaetzt="II",
    fehlerquelle="nur das Integral über f_2 bilden und die untere Randkurve K weglassen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B2.2g (WTR): Wortlaut gleich, 3 statt 5 BE; im Aufgabenstamm „durch die Graphen G_2 und K“ statt „durch Teile der Graphen“. Typ, Lösungsweg und Ergebnis wie in der WTR-Zeile. Aufgabenseite 8, die zugehörige Abbildung steht auf Seite 7. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-bb-ea-cas-B2.2i", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="i", seite="8|7", punkte="5",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Kleinsten Abstand eines Punktes zu einem Graphen über die Abstandsfunktion bestimmen",
    typ_neben="",
    stichwoerter="kleinster Abstand|Koordinatenursprung|Teichrand|Abstandsquadrat|Randstück",
    voraussetzungen="Abstand zweier Punkte mit dem Satz des Pythagoras ausdrücken|Minimum einer Funktion über die Ableitung oder mit dem CAS bestimmen|entscheiden, welches Randstück dem Punkt am nächsten liegt",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Koordinatensystem",
    skizze=SK22,
    kontext="Gartenteich",
    textumfang="mittel",
    gegeben=ST22 + TEICH + " Für einen Grillplatz hat der Gartenbesitzer eine Fläche betoniert; der Koordinatenursprung ist im Modell der Punkt der betonierten Fläche, der den geringsten Abstand zum Teichrand hat.",
    gesucht="geringster Abstand des Koordinatenursprungs zum Teichrand",
    verfahren="Der Ursprung liegt rechts unterhalb des Teichs, am nächsten liegt der untere Rand K. Das Abstandsquadrat d(x)² = x² + (h(x))² = x² + 0,25 · x^(−6) aufstellen und die Ableitung 2x − 1,5 · x^(−7) null setzen: x^8 = 0,75, also x ≈ −0,965, im Randstück zwischen den Schnittpunkten. Zum Vergleich ist der kleinste Abstand zum Randstück von G_2 etwa 1,80.",
    schritte="4",
    zahlenraum="dezimal|negativ|Wurzel|Potenz",
    einheiten="m",
    ergebnis="Der nächste Punkt des Teichrands ist (−0,965 | 0,557) auf K; der Abstand beträgt etwa 1,11 m.",
    zwischenergebnis="d(x)² = x² + 0,25 · x^(−6)|x^8 = 0,75, x ≈ −0,9647|h(−0,9647) ≈ 0,5570|kleinster Abstand zu G_2 ≈ 1,80 bei x ≈ −0,958",
    niveau_geschaetzt="III",
    fehlerquelle="den Abstand nur zu einem Randstück minimieren, ohne das andere zu prüfen, oder das Minimum von d² nicht in den Abstand umrechnen",
    abhaengig_von="2018-bb-ea-cas-B2.2f",
    bemerkung="CAS-Nachtrag, ohne WTR-Gegenstück: die Teilaufgabe steht nur in der CAS-Fassung (die WTR-Fassung endet mit h). Neuer Typ: der Bestand kennt den Abstand eines Punktes von einem Graphen nur als Deutung über die Normalenbedingung. Genau x = −(3/4)^(1/8) und d ≈ 1,1139; die Stelle liegt zwischen den Schnittpunkten aus f (−4,00 und −0,64), deshalb abhängig von f. Aufgabenseite 8, die zugehörige Abbildung steht auf Seite 7. Eigene Rechnung, mit sympy bestätigt.")
# ---- Aufgabe 3.1 CAS: Museum (Seite 9, 25 BE; Zeile f = 6 BE)
row(id="2018-bb-ea-cas-B3.1f", block="B", aufgabe="3.1", titel="Museum", teilaufgabe="f", seite="9", punkte="6",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt auf einer Strecke mit vorgegebenem Abstand zu einer Ebene bestimmen",
    typ_neben="Koordinatengleichung einer Ebene aus Punkten oder Geraden bestimmen",
    stichwoerter="Scheinwerfer auf der Strecke RG|Abstand 5 Meter zur Ebene|Ebene EFG selbst aufstellen|Hessesche Normalform|Parameter der Strecke",
    voraussetzungen="Normalenvektor über das Kreuzprodukt oder ein Gleichungssystem bestimmen|Abstand Punkt Ebene über die Hessesche Normalform berechnen|Strecke als Gerade mit Parameterbereich schreiben",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze=SK31,
    kontext="Museumsgebäude",
    textumfang="lang",
    gegeben=ST31 + " An einer Metallstange, die durch die Strecke RG mit R(−50/7 | 50/7 | 15) dargestellt wird, ist ein punktförmig gedachter Scheinwerfer befestigt, der sich entlang der Stange verschieben lässt. Er soll aus einer Entfernung von 5 m die Wand beleuchten, die im Modell durch das Dreieck EFG dargestellt wird.",
    gesucht="Koordinaten des Punktes, der die Position des Scheinwerfers im Modell beschreibt",
    verfahren="Die Ebene des Dreiecks EFG aus E, F und G aufstellen: Normalenvektor aus EF und EG (Kreuzprodukt oder Gleichungssystem), ergibt 2x − 2y − z = −75. Die Strecke RG mit einem Parameter zwischen 0 und 1 schreiben, den Abstand über die Hessesche Normalform (Normalenvektor der Länge 3) gleich 5 setzen und nach dem Parameter auflösen, mit dem CAS.",
    schritte="6",
    zahlenraum="Bruch|dezimal|ganz|negativ",
    einheiten="m",
    ergebnis="Ebene EFG: 2x − 2y − z = −75. Der Parameter ist 23/44; der Scheinwerfer sitzt im Punkt (−95/11 | 95/11 | 280/11), also rund (−8,64 | 8,64 | 25,45).",
    zwischenergebnis="Normalenvektor (2 | −2 | −1) mit Betrag 3|Abstand bei R rund 10,48 m, bei G 0|Parameter 23/44 auf RG (8/11 auf der Geraden AG)",
    niveau_geschaetzt="III",
    fehlerquelle="den Abstand ohne Normierung des Normalenvektors ansetzen oder die zweite Lösung außerhalb der Strecke nicht verwerfen",
    abhaengig_von="2018-bb-ea-B3.1e",
    bemerkung="Poolaufgabe (nicht erfasst): 2018MerhoehtBAGLAA2CAS1-1f. CAS-Nachtrag zu 2018-bb-ea-B3.1f (WTR): die Ebenengleichung 2x − 2y − z = −75 der WTR-Fassung fehlt, die Ebene des Dreiecks EFG wird selbst aufgestellt (Nebentyp); BE gleich (6). Haupttyp und Ergebnis wie in der WTR-Zeile. Die CAS-Aufgabe 3.1 Museum ist die Poolaufgabe 2018 erhöht Teil B AG/LA (A2) CAS 1 (Pool-BE 4, 3, 4, 4, 3, 7; Heft 4, 3, 5, 4, 3, 6); Teilaufgabe f stimmt in Angaben und Auftrag überein, ist im Heft leicht umformuliert („der sich entlang der Stange verschieben lässt“, „soll beleuchten“) und hat 6 statt 7 BE. Ihr Stapel 2018-ea-B (CAS-Zweig) ist Reserve und nicht erfasst – offener Posten in der Prüfungsliste (§ 4). Schätzung III wie in der WTR-Zeile, deckt sich mit dem Standardbezug der Poolfassung. abhaengig_von zeigt auf die WTR-Zeile 3.1 e, weil die wortgleiche CAS-Teilaufgabe e keine eigene Zeile hat. Die zweite Lösung (Parameter 65/44) liegt außerhalb der Strecke. Eigene Rechnung, mit sympy bestätigt; der Erwartungshorizont der Poolfassung nennt denselben Punkt.")
# ---- Aufgabe 4.2 CAS: Brillenträger (Seite 12, 25 BE; Zeile d = 5 BE)
row(id="2018-bb-ea-cas-B4.2d", block="B", aufgabe="4.2", titel="Brillenträger", teilaufgabe="d", seite="12", punkte="5",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel eines einseitigen Signifikanztests bestimmen",
    typ_neben="",
    stichwoerter="Nullhypothese höchstens 30 Prozent|Stichprobe 100|Signifikanzniveau 5 Prozent|rechtsseitiger Test|Ablehnungsbereich",
    voraussetzungen="Nullhypothese und Alternative unterscheiden|einseitigen Test als rechtsseitig erkennen|kumulierte Binomialwahrscheinlichkeiten mit dem CAS berechnen",
    format="Rechnung|Begründung",
    operator="Bestimmen Sie",
    antwort="Zahl|Text",
    material="keins",
    skizze="keine",
    kontext="Optiker und Werbeaktion",
    textumfang="lang",
    gegeben=ST42 + " Ein Optiker vermutet, dass mehr als 30 % der jungen Erwachsenen aus dem Landkreis Kunden in seinem Geschäft sind. Sollte das nicht der Fall sein, erwägt er eine Werbeaktion mit Flyern. Um unnötige Kosten zu vermeiden, soll die Nullhypothese, dass höchstens 30 % der jungen Erwachsenen Kunden bei diesem Optiker sind, mit einer Stichprobe von 100 jungen Erwachsenen auf einem Signifikanzniveau von 5 % getestet werden.",
    gesucht="die zugehörige Entscheidungsregel",
    verfahren="Unter der Nullhypothese ist die Trefferzahl X binomialverteilt mit 100 Versuchen und der Trefferwahrscheinlichkeit 0,3. Der Test ist rechtsseitig, weil die Alternative mehr als 30 % lautet. Mit dem CAS die kleinste Trefferzahl k suchen, für die P(X ≥ k) höchstens 5 % beträgt.",
    schritte="4",
    zahlenraum="dezimal|ganz|Prozent",
    einheiten="",
    ergebnis="Ablehnungsbereich von 39 bis 100, Annahmebereich von 0 bis 38. Die Nullhypothese wird also verworfen, wenn in der Stichprobe mindestens 39 der 100 jungen Erwachsenen Kunden sind; andernfalls wird sie beibehalten und die Werbeaktion erwogen.",
    zwischenergebnis="P(X ≥ 38) ≈ 0,0530 und damit zu groß|P(X ≥ 39) ≈ 0,0340",
    niveau_geschaetzt="III",
    fehlerquelle="die Grenze bei 38 ziehen, weil P(X ≥ 38) nur knapp über 5 % liegt, oder linksseitig testen",
    abhaengig_von="",
    bemerkung="CAS-Nachtrag zu 2018-bb-ea-B4.2d (WTR): Wortlaut gleich (nur das Komma nach „sein“ fehlt), BE gleich (5); die CAS-Fassung hat keine Anlage – die Tafel der summierten Binomialverteilungen (n = 100) der WTR-Fassung fehlt, die kumulierten Wahrscheinlichkeiten liefert das CAS. Typ und Ergebnis wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")

NEUE_TYPEN = [
    ("Rotationsvolumen um die x-Achse berechnen", "Analysis", "Rotationsvolumen",
     "Das Volumen des Körpers, der bei Rotation der Fläche zwischen einem Graphen und der x-Achse über einem Intervall um die x-Achse entsteht, als π · ∫ (f(x))² dx berechnen (mit dem Rechner oder über eine Stammfunktion) und im Sachzusammenhang angeben, etwa als Fassungsvermögen nach Abzug eines Materialanteils.",
     "2018-bb-ea-cas-B2.1h"),
    ("Schnittpunkte zweier Graphen mit dem Rechner ermitteln", "Analysis", "Gleichungen lösen",
     "Die Gleichung f(x) = g(x), die sich nicht durch elementares Umformen lösen lässt, mit dem Rechner numerisch lösen und die Schnittpunkte mit gerundeten Koordinaten angeben.",
     "2018-bb-ea-cas-B2.2f"),
    ("Kleinsten Abstand eines Punktes zu einem Graphen über die Abstandsfunktion bestimmen", "Analysis", "Extremalprobleme",
     "Den Abstand eines festen Punktes zu einem Punkt des Graphen als Funktion der Stelle aufstellen (meist als Abstandsquadrat), ihr Minimum über die Ableitung oder mit dem Rechner bestimmen und prüfen, dass die Minimalstelle auf dem betrachteten Graphenstück liegt.",
     "2018-bb-ea-cas-B2.2i"),
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
