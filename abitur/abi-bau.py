# -*- coding: utf-8 -*-
"""abi-bau.py – Gerüst für die Erfassung eines Hefts im Profil abi.
Version 0.15 · 29.09.2026 · gilt mit katalog-prompt.md v0.9, abitur-vokabular.md v1.6, abi.md v0.31, abitur-abgleich.py v0.29 und den Geltungsdateien abi-<zielprüfung>-geltung.md v1.0

Änderungen gegenüber 0.14 (Auftrag Nacht 2026-09-29, Teil 4: Nachtrag der
Berliner CAS-Hefte 2017/2018, beschluss-2026-09-26.md Punkt 3): Landes-Dublette.
Eine Nachtragszeile, deren Teilaufgabe sich von der WTR-Fassung nur in den BE
oder nur in Zahlenwerten unterscheidet (Art „nur BE", „nur Zahl" oder beides,
abitur/befund-cas-berlin-2026-09-28.md), bekommt eine Zeile mit „Dublette von:
<id der WTR-Zeile>." am Anfang von bemerkung – der Verweis zeigt auf eine
Zeile des abi-Katalogs, nicht auf den Pool. Geprüft (pruefe_zeile, auch in der
Selbstprüfung): die WTR-Zeile steht im Katalog, im WTR-Heft des papier-Kürzels
(wtr_papier) und in derselben Aufgabe; typ gleich; afb_amtlich gleich dem der
WTR-Zeile (leer oder aus deren Poolverweis – die Regel „afb_amtlich genau bei
Dublette von:" gilt nur für den Poolverweis); bemerkung nennt den Vermerk
„nur BE: …", „nur Zahl: …" oder „nur BE und Zahl: …" (bei anderer Punktzahl
BE-Vermerk Pflicht, bei „nur BE" andere Punktzahl Pflicht, bei „nur Zahl"
gleiche); der Nachtragsvermerk „CAS-Nachtrag zu <WTR-id> (WTR): …" zeigt auf
dieselbe Zeile. Poolquote, geerbte Eichung und die Dublettenzählung der
Selbstprüfung bleiben beim Poolverweis (MARKE_DUBLETTE unverändert); eine
Landes-Dublette zählt dort nicht. Die Selbstprüfung nennt die Landes-Dubletten
in einer eigenen Zeile, nur wenn es welche gibt – für den Bestand ohne sie ist
die Ausgabe byteidentisch zu 0.14. iqb-bau.py liest „Dublette von:" nur mit
Pool-Kennung und übergeht den Verweis.

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
    "papier": "2017-be-gk-cas",
    "datei": "hefte/abi/2017-be-gk-cas.pdf",  # amtliches Heft (Bildungsserver, 17_Ma_GK_CAS_Aufgaben.pdf), 8 Seiten mit Textebene, lokal (abi-quellen.md § 2, § 8)
    "seiten": 8,
    # CAS-Nachtrag (v0.14/v0.15, abi.md § 7, Beschluss vom 26.09.2026 Punkt 3): Zeilen für die 16
    # abweichenden Teilaufgaben (befund-cas-berlin-2026-09-28.md) – eigene Zeilen für Werkzeug, Auftrag,
    # Zuschnitt, ganze Aufgabe; Landes-Dublette für nur BE (1.1 b, c; 1.2 e; 2.2 d; 3.2 c).
    # BE der Zeilen je Aufgabe: 1.1 a 8, b 4, c 5, e 10, f 8 = 35; 1.2 a 5, b 9, d 3, e 7, f 4 = 28;
    # 2.2 c 6, d 3 = 9; 3.1 e 2, g 4 = 6; 3.2 c 4, d 4 = 8.
    "nachtrag_zu": "2017-be-gk",
    "soll": {"1.1": 35, "1.2": 28, "2.2": 9, "3.1": 6, "3.2": 8},
    # wortgleiche Teilaufgaben mit gleichen BE ohne Zeile: CAS-Buchstabe → (WTR-Buchstabe, BE)
    "uebernommen": {"1.1": {"d": ("e", 5)},
                    "1.2": {"c": ("c", 5), "g": ("f", 7)},
                    "2.2": {"a": ("a", 2), "b": ("b", 4), "e": ("e", 5)},
                    "3.1": {"a": ("a", 2), "b": ("b", 3), "c": ("c", 2), "d": ("d", 3), "f": ("f", 4)},
                    "3.2": {"a": ("a", 5), "b": ("b", 3), "e": ("e", 4)}},
    # Aufgaben ohne abweichende Teilaufgabe (Summe je Aufgabe)
    "unveraendert": {"2.1": 20},
    # angeboten wie im WTR-Heft: 40 + 40 + 20 + 20 + 20 + 20 (beide Wahlwege)
    "be_angeboten": 160,
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
# Heft 2017-be-gk-cas (amtliches Heft 17_Ma_GK_CAS_Aufgaben, 8 Seiten mit Textebene;
# CAS-Nachtrag zu 2017-be-gk, Auftrag Nacht 2026-09-29, Teil 4; Beschluss vom 26.09.2026 Punkt 3).
# Messung und Art je Teilaufgabe: abitur/befund-cas-berlin-2026-09-28.md. Eigene Zeile für die
# Arten Werkzeug, Auftrag, Zuschnitt, ganze Aufgabe; Landes-Dublette („Dublette von: <WTR-id>“,
# abi-bau.py v0.15) für nur BE; wortgleiche Teilaufgaben übernommen. Pool: 3.1 Smartphone ist die
# CAS-Poolfassung 2017 grundlegend Teil B Stochastik (Stapel 2017-ga-B-cas, erfasst) – e und g
# weichen vom WTR-Heft ab und bekommen „Dublette von:“ auf die Poolzeile. Kontexte der übrigen
# Aufgaben in den Pooldateien 2017/2018 gesucht: kein Treffer. Keine amtlichen Lösungen: jede
# Zeile „Eigene Rechnung“ (sympy); Seiten gerendert (Abbildung zu 1.1 e mit der Stütze 3 cm).

row(id="2017-be-gk-cas-B1.1a", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="a", seite="2", punkte="8",
    leitidee="Analysis",
    thema="Kurvenuntersuchung",
    typ="Lage und Art aller lokalen Extrempunkte bestimmen",
    typ_neben="Extrempunkt einem Punkt im Sachzusammenhang zuordnen",
    stichwoerter="Extrempunkte|zweite Ableitung|knickfreier Übergang|waagerechte Tangente|ohne vorgegebene Ableitung",
    voraussetzungen="Ableitungen einer ganzrationalen Funktion bilden|x ausklammern und Nullprodukt anwenden|waagerechte Tangente als Ableitung null deuten",
    format="Rechnung|Begründung",
    operator="Ermitteln Sie|Weisen Sie nach|Begründen Sie",
    antwort="Zahl|Text",
    material="Skizze",
    skizze="Profilzeichnung in einem x-y-Koordinatensystem ohne Achsenteilung: grau ausgefülltes Brückenteil zwischen der y-Achse und einer senkrechten rechten Kante, unten auf der x-Achse. Die obere Begrenzung ist der mit f beschriftete Graph; er beginnt im Eckpunkt A auf der y-Achse knapp über der x-Achse mit waagerechter Tangente, steigt S-förmig und erreicht im Eckpunkt B über der rechten Kante wieder waagerecht seinen höchsten Punkt. Links von A und rechts von B schließen waagerechte Linien (Anschlussschienen) an, gestrichelte Kurvenstücke setzen den Graphen über A hinaus nach links oben und über B hinaus nach rechts unten fort. Die rechte Kante ist mit „Höhe“, die Unterkante mit „Länge“ beschriftet; Zahlenwerte stehen nicht in der Abbildung.",
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="mittel",
    gegeben="Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Brückenteils wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. In den oberen Eckpunkten A und B geht die Oberkante ohne Knick in die waagerechten Anschlussschienen über. Kontrollangabe: A(0 | f(0)) bzw. B(20 | f(20)).",
    gesucht="Extrempunkte von f mit Nachweis ihrer Art; Begründung, warum die Extrempunkte mit den Eckpunkten A und B übereinstimmen müssen",
    verfahren="f′(x) = −3/500 · x² + 3/25 · x selbst bilden (von Hand oder mit dem CAS), null setzen und x ausklammern: x · (−3/500 · x + 3/25) = 0 liefert x = 0 und x = 20. Mit f″(x) = −3/250 · x + 3/25 die Art bestimmen: f″(0) > 0 Tiefpunkt, f″(20) < 0 Hochpunkt. Knickfreier Übergang in waagerechte Schienen heißt Steigung null in A und B, also f′ = 0 dort – die Eckpunkte sind die Stellen mit waagerechter Tangente.",
    schritte="6",
    zahlenraum="ganz|Bruch",
    einheiten="cm",
    abhaengig_von="",
    ergebnis="Tiefpunkt T(0 | 1) = A, Hochpunkt H(20 | 9) = B. Ohne Knick in waagerechte Schienen heißt: die Tangente an den Graphen ist in A und B waagerecht, f′ ist dort null; die einzigen solchen Stellen sind die Extremstellen 0 und 20.",
    zwischenergebnis="f′(x) = −3/500 · x² + 3/25 · x|f″(x) = −3/250 · x + 3/25|f″(0) = 0,12|f″(20) = −0,12|f(20) = 9",
    niveau_geschaetzt="II",
    fehlerquelle="die Ableitung falsch bilden (etwa 3/50 · x statt 3/25 · x) oder die Art nicht über f″ nachweisen, oder den knickfreien Übergang nur über gleiche Höhe statt über gleiche Steigung begründen",
    bemerkung="CAS-Nachtrag zu 2017-be-gk-B1.1a (WTR): die Kontrollangabe f′(x) = −3/500 · x² + 3/25 · x der WTR-Fassung fehlt, die Ableitung wird selbst gebildet; die Kontrollangabe für A und B bleibt; 8 statt 9 BE. Typ, Nebentyp und Ergebnis wie in der WTR-Zeile. Im Aufgabenstamm „des Brückenteils“ statt „des Bauelements“ (redaktionell). Kontrollangabe A, B durch eigene Rechnung bestätigt. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B1.1b", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="b", seite="2", punkte="4",
    leitidee="Analysis",
    thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsrate über ein Intervall berechnen",
    typ_neben="Stelle mit lokaler gleich mittlerer Änderungsrate bestimmen",
    stichwoerter="mittlere Steigung|Differenzenquotient|lokale Steigung|quadratische Gleichung",
    voraussetzungen="Differenzenquotient bilden|quadratische Gleichung lösen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Skizze",
    skizze="Profilzeichnung in einem x-y-Koordinatensystem ohne Achsenteilung: grau ausgefülltes Brückenteil zwischen der y-Achse und einer senkrechten rechten Kante, unten auf der x-Achse. Die obere Begrenzung ist der mit f beschriftete Graph; er beginnt im Eckpunkt A auf der y-Achse knapp über der x-Achse mit waagerechter Tangente, steigt S-förmig und erreicht im Eckpunkt B über der rechten Kante wieder waagerecht seinen höchsten Punkt. Links von A und rechts von B schließen waagerechte Linien (Anschlussschienen) an, gestrichelte Kurvenstücke setzen den Graphen über A hinaus nach links oben und über B hinaus nach rechts unten fort. Die rechte Kante ist mit „Höhe“, die Unterkante mit „Länge“ beschriftet; Zahlenwerte stehen nicht in der Abbildung.",
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="kurz",
    gegeben="Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Brückenteils wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke des Bauteils liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. Das Brückenteil reicht von A(0 | 1) bis B(20 | 9); f′(x) = −3/500 · x² + 3/25 · x.",
    gesucht="mittlere Steigung des Brückenteils; Stellen, an denen die lokale Steigung von f gleich der mittleren Steigung ist",
    verfahren="Mittlere Steigung als Differenzenquotient (f(20) − f(0))/20. Dann f′(x) = 0,4 setzen, mit −500/3 multiplizieren und die quadratische Gleichung x² − 20x + 200/3 = 0 mit der Lösungsformel lösen.",
    schritte="4",
    zahlenraum="dezimal|Bruch|Wurzel",
    einheiten="cm",
    abhaengig_von="2017-be-gk-cas-B1.1a",
    ergebnis="Mittlere Steigung m = (9 − 1)/20 = 0,4. f′(x) = 0,4 an den Stellen x = 10 ± 10/√3, also x₁ ≈ 4,23 und x₂ ≈ 15,77.",
    zwischenergebnis="x² − 20x + 200/3 = 0|Diskriminante 100/3",
    niveau_geschaetzt="II",
    fehlerquelle="die mittlere Steigung als Mittelwert von f′(0) und f′(20) bilden oder nur eine der beiden Lösungen angeben",
    bemerkung="Dublette von: 2017-be-gk-B1.1b. CAS-Nachtrag zu 2017-be-gk-B1.1b (WTR): nur BE: 4 statt 6 BE, Wortlaut und Angaben gleich. Felder wie in der WTR-Zeile, Fakten des CAS-Hefts (Seite, BE). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B1.1c", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="c", seite="2", punkte="5",
    leitidee="Analysis",
    thema="Kurvenuntersuchung",
    typ="Maximalen Neigungswinkel über die Wendestelle berechnen",
    typ_neben="",
    stichwoerter="größter Anstieg|Wendepunkt|Steigungswinkel|Grenzwinkel 32°",
    voraussetzungen="zweite Ableitung bilden|Steigung über den Arkustangens in einen Winkel umrechnen",
    format="Rechnung|Begründung",
    operator="Bestimmen Sie|Berechnen Sie|Entscheiden Sie",
    antwort="Zahl|Text",
    material="Skizze",
    skizze="Profilzeichnung in einem x-y-Koordinatensystem ohne Achsenteilung: grau ausgefülltes Brückenteil zwischen der y-Achse und einer senkrechten rechten Kante, unten auf der x-Achse. Die obere Begrenzung ist der mit f beschriftete Graph; er beginnt im Eckpunkt A auf der y-Achse knapp über der x-Achse mit waagerechter Tangente, steigt S-förmig und erreicht im Eckpunkt B über der rechten Kante wieder waagerecht seinen höchsten Punkt. Links von A und rechts von B schließen waagerechte Linien (Anschlussschienen) an, gestrichelte Kurvenstücke setzen den Graphen über A hinaus nach links oben und über B hinaus nach rechts unten fort. Die rechte Kante ist mit „Höhe“, die Unterkante mit „Länge“ beschriftet; Zahlenwerte stehen nicht in der Abbildung.",
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="mittel",
    gegeben="Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Brückenteils wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke des Bauteils liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. f′(x) = −3/500 · x² + 3/25 · x. Für batteriebetriebene Lokomotiven darf der Anstiegswinkel an keiner Stelle größer als 32° sein; ein Nachweis mit hinreichender Bedingung ist nicht verlangt.",
    gesucht="Punkt mit dem größten Anstieg; maximaler Anstiegswinkel und Entscheidung, ob das 32°-Kriterium erfüllt ist",
    verfahren="Der größte Anstieg liegt, wo f′ maximal ist: f″(x) = −3/250 · x + 3/25 = 0 liefert x = 10. Den Punkt über f(10) angeben, die Steigung f′(10) berechnen und über tan α = f′(10) den Winkel bestimmen; mit 32° vergleichen.",
    schritte="4",
    zahlenraum="ganz|dezimal",
    einheiten="cm|°",
    abhaengig_von="",
    ergebnis="Größter Anstieg im Wendepunkt W(10 | 5) mit f′(10) = 0,6; α = arctan 0,6 ≈ 31,0° < 32°, das Kriterium ist erfüllt.",
    zwischenergebnis="f″(x) = −3/250 · x + 3/25|f′(10) = 0,6|α ≈ 30,96°",
    niveau_geschaetzt="II",
    fehlerquelle="die Steigung 0,6 direkt mit 32 vergleichen, ohne sie in einen Winkel umzurechnen, oder den Hochpunkt als Punkt größten Anstiegs nennen",
    bemerkung="Dublette von: 2017-be-gk-B1.1c. CAS-Nachtrag zu 2017-be-gk-B1.1c (WTR): nur BE: 5 statt 6 BE, Wortlaut und Angaben gleich. Felder wie in der WTR-Zeile, Fakten des CAS-Hefts (Seite, BE). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B1.1e", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="e", seite="3", punkte="10",
    leitidee="Analysis",
    thema="Kurvenuntersuchung",
    typ="Lage eines Graphen zwischen zwei Geraden auf einem Intervall über die Differenzfunktionen nachweisen",
    typ_neben="Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen",
    stichwoerter="parallele Geraden g_u und g_o|Differenzfunktion|faktorisierte Differenz|kleinster vertikaler Abstand|Holzbrett",
    voraussetzungen="Differenz zweier Funktionsterme bilden und faktorisieren|Extremstellen einer ganzrationalen Funktion über die Ableitung bestimmen|Vorzeichen eines Produkts beurteilen|Randwerte eines Intervalls vergleichen",
    format="Begründung|Rechnung",
    operator="Weisen Sie nach|Ermitteln Sie",
    antwort="Text|Zahl",
    material="Skizze",
    skizze="Abbildung zu e) (Seite 3): Koordinatensystem ohne Achsenteilung mit dem Graphen f von A auf der y-Achse bis B. Zwei parallele gestrichelte Geraden steigen nach rechts oben: g_o verläuft durch A und oberhalb des Graphen, g_u schneidet die x-Achse rechts vom Ursprung und verläuft unterhalb des Graphen. Grau ausgefüllt ist das Brückenteil: oben der Graph von f, unten zuerst die x-Achse, dann g_u bis zu einer senkrechten Kante, rechts davon eine senkrechte Stütze unter B, die auf der x-Achse steht; die Breite der Stütze ist mit 3 cm bemaßt.",
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="lang",
    gegeben="Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Brückenteils wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. Um Material zu sparen, wird das Brückenteil aus zwei Holzbrettern hergestellt; das eine Brett wird von den Geraden g_u(x) = 45/100 · x − 2 und g_o(x) = 45/100 · x + 1 begrenzt.",
    gesucht="Nachweis, dass der Graph von f für x ∈ [0; 20] vollständig in dem Bereich zwischen g_u und g_o liegt; die Stelle im Bereich 0 < x < 20, an der der vertikale Abstand der Geraden g_u zum Graphen von f am geringsten ist, und dieser minimale Abstand",
    verfahren="Die Differenzen g_o(x) − f(x) = x · (x − 15)²/500 und d(x) = f(x) − g_u(x) = −x³/500 + 3/50 · x² − 9/20 · x + 3 bilden (mit dem CAS faktorisieren). Die erste ist für x ≥ 0 nicht negativ (null nur bei 0 und 15, dort berührt f die Gerade g_o). Für die zweite d′(x) = −3/500 · (x − 5) · (x − 15) = 0 lösen: lokales Minimum bei x = 5 mit d(5) = 2 > 0, lokales Maximum bei x = 15; mit den Randwerten d(0) = 3 und d(20) = 2 ist d auf [0; 20] positiv. Die Stelle 5 liefert den kleinsten vertikalen Abstand im Inneren.",
    schritte="6",
    zahlenraum="ganz|Bruch|dezimal",
    einheiten="cm",
    abhaengig_von="",
    ergebnis="g_o(x) − f(x) = x · (x − 15)²/500 ≥ 0 und f(x) − g_u(x) ≥ 2 > 0 für x ∈ [0; 20]; der Graph liegt im Bereich zwischen den Geraden (er berührt g_o in A und bei x = 15). Der vertikale Abstand von g_u zum Graphen ist bei x = 5 am geringsten und beträgt dort 2 cm.",
    zwischenergebnis="d(x) = −x³/500 + 3/50 · x² − 9/20 · x + 3|d′(x) = −3/500 · (x − 5) · (x − 15)|d(5) = 2|d(15) = 3|d(0) = 3|d(20) = 2",
    niveau_geschaetzt="II",
    fehlerquelle="den Nachweis nur an einzelnen Stellen führen, den Randwert d(20) = 2 mit dem inneren Minimum verwechseln oder den Abstand senkrecht zur Geraden statt vertikal messen",
    bemerkung="CAS-Nachtrag, ohne WTR-Gegenstück: die Teilaufgabe steht nur in der CAS-Fassung (Art ganze Aufgabe, Befund vom 28.09.2026); die CAS-Teilaufgabe d entspricht der WTR-Teilaufgabe e. Neuer Typ: der Bestand kennt die Lage zweier Graphen über ihre Differenz nur als Ungleichung zwischen zwei Termen oder aus einem abgebildeten Differenzgraphen, nicht als Nachweis, dass ein Graph auf einem Intervall zwischen zwei Geraden liegt. Nebentyp: das Etikett nennt den maximalen Abstand, hier ist das Minimum der Differenzfunktion gesucht (Abgleichlauf 28). Der Randwert d(20) = 2 ist gleich dem inneren Minimum; gefragt ist nur 0 < x < 20. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B1.1f", block="B", aufgabe="1.1", titel="Holzeisenbahn", teilaufgabe="f", seite="3", punkte="8",
    leitidee="Analysis",
    thema="Flächeninhalt durch Integration",
    typ="Fläche: Volumen eines Körpers mit konstantem Querschnitt aus der Fläche zwischen Graph und waagerechter Gerade berechnen",
    typ_neben="Fläche: Abschnittsweise begrenzte Fläche durch Integration berechnen",
    stichwoerter="Querschnittsfläche|abschnittsweise Unterkante|Gerade g_u|Stütze am rechten Rand|Tiefe 4 cm",
    voraussetzungen="Nullstelle einer linearen Funktion berechnen|bestimmtes Integral mit dem CAS oder über eine Stammfunktion berechnen|Fläche in Teilflächen zerlegen|Prismenvolumen als Grundfläche mal Tiefe",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Skizze",
    skizze="Abbildung zu e) (Seite 3): Koordinatensystem ohne Achsenteilung mit dem Graphen f von A auf der y-Achse bis B. Zwei parallele gestrichelte Geraden steigen nach rechts oben: g_o verläuft durch A und oberhalb des Graphen, g_u schneidet die x-Achse rechts vom Ursprung und verläuft unterhalb des Graphen. Grau ausgefüllt ist das Brückenteil: oben der Graph von f, unten zuerst die x-Achse, dann g_u bis zu einer senkrechten Kante, rechts davon eine senkrechte Stütze unter B, die auf der x-Achse steht; die Breite der Stütze ist mit 3 cm bemaßt.",
    kontext="Spielzeug / Holzeisenbahn",
    textumfang="mittel",
    gegeben="Brückenteil einer Holzeisenbahn; die obere Begrenzungslinie des Brückenteils wird durch f mit f(x) = −1/500 · x³ + 3/50 · x² + 1 beschrieben, 1 LE = 1 cm. Die linke untere Ecke liegt im Koordinatenursprung, die oberen Eckpunkte A und B liegen auf dem Graphen von f. Das Brückenteil wird aus zwei Holzbrettern hergestellt; das eine wird unten von g_u(x) = 45/100 · x − 2 begrenzt. Das in der Abbildung zu e) grau dargestellte Brückenteil einschließlich der senkrechten Stütze am rechten Rand (in der Abbildung 3 cm breit) hat eine Tiefe von 4 cm.",
    gesucht="Volumen des gesamten Brückenteils",
    verfahren="Die Querschnittsfläche ist die Fläche unter dem Graphen von f über [0; 20] ohne das weiße Dreieck zwischen x-Achse und g_u: g_u hat die Nullstelle 40/9, die Stütze beginnt bei x = 20 − 3 = 17. Also A = ∫₀²⁰ f(x) dx − ∫ von 40/9 bis 17 über g_u(x) dx (gleichwertig: Fläche unter f über [0; 40/9] und [17; 20] plus Fläche zwischen f und g_u über [40/9; 17]), mit dem CAS. Mit der Tiefe 4 cm multiplizieren.",
    schritte="5",
    zahlenraum="Bruch|dezimal",
    einheiten="cm|cm²|cm³",
    abhaengig_von="2017-be-gk-cas-B1.1e",
    ergebnis="Querschnittsfläche A = 100 − 12769/360 = 23231/360 ≈ 64,53 cm², Volumen V = 4 · A = 23231/90 ≈ 258,1 cm³.",
    zwischenergebnis="∫₀²⁰ f(x) dx = 100|Nullstelle von g_u bei 40/9 ≈ 4,44|∫ von 40/9 bis 17 über g_u(x) dx = 12769/360 ≈ 35,47|g_u(17) = 5,65",
    niveau_geschaetzt="II",
    fehlerquelle="die ganze Fläche unter f nehmen (400 cm³ wie in der WTR-Fassung), die Stütze vergessen und nur zwischen f und g_u integrieren oder die Tiefe nicht einrechnen",
    bemerkung="CAS-Nachtrag zu 2017-be-gk-B1.1d (WTR): andere Frage – gesucht ist das Volumen des grau dargestellten Brückenteils aus der Abbildung zu e (unten durch x-Achse und g_u begrenzt, mit Stütze am rechten Rand), nicht des vollen Brückenteils unter dem Graphen; 8 statt 5 BE; im Heft Teilaufgabe f statt d. Typ wie in der WTR-Zeile, Nebentyp für die zusammengesetzte Querschnittsfläche. Die Lage der Stütze (x = 17 bis 20) folgt aus der Bemaßung 3 cm in der Abbildung. Eigene Rechnung, mit sympy bestätigt (258,12 cm³).")
row(id="2017-be-gk-cas-B1.2a", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="a", seite="4", punkte="5",
    leitidee="Analysis",
    thema="Funktionsklassen und Eigenschaften",
    typ="Nullstellen und Werte: Nullstelle und y-Achsenschnittpunkt eines Produkts mit e-Funktion angeben",
    typ_neben="Graphen einer Funktion in ein Koordinatensystem einzeichnen",
    stichwoerter="Achsenschnittpunkte|Produkt mit e-Funktion|doppelte Nullstelle|Graph zeichnen|Intervall [0; 2]",
    voraussetzungen="Satz vom Nullprodukt|binomische Formel erkennen|Funktionswerte mit e-Funktion berechnen|Koordinatensystem passend skalieren",
    format="Rechnung|Zeichnen",
    operator="Bestimmen Sie|Zeichnen Sie",
    antwort="Zahl|Grafik",
    material="Foto",
    skizze="Schwarz-weißes Foto eines Berliner Veranstaltungsortes: mehrere gleichartige, spitz zulaufende weiße Dachelemente vor einem Hochhaus; das Foto dient nur der Veranschaulichung und enthält keine Maße. Ein Koordinatensystem ist nicht vorgegeben; zu zeichnen ist der Graph von f über [0; 2]: fallend von (0 | 1) über (0,5 | 0,15) zum Tiefpunkt (1 | 0) auf der x-Achse, danach flach steigend bis (2 | 0,14).",
    kontext="Architektur / Dach",
    textumfang="kurz",
    gegeben="Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m.",
    gesucht="Koordinaten der Schnittpunkte des Graphen von f mit den Koordinatenachsen; Graph von f im Intervall [0; 2]",
    verfahren="f(0) = 1 liefert den y-Achsenschnittpunkt; da e^(−x) > 0 ist, gilt f(x) = 0 genau für (x − 1)² = 0. Für die Zeichnung eine Wertetabelle über [0; 2] anlegen (mit dem CAS), die Punkte (0 | 1) und (1 | 0) eintragen und glatt verbinden; bei x = 1 berührt der Graph die x-Achse.",
    schritte="4",
    zahlenraum="ganz|dezimal|Potenz",
    einheiten="",
    abhaengig_von="",
    ergebnis="Schnittpunkt mit der y-Achse (0 | 1), mit der x-Achse (1 | 0) (doppelte Nullstelle, der Graph berührt dort die x-Achse). Kennzeichnende Punkte für die Zeichnung: (0 | 1), (0,5 | 0,15), (1 | 0), (1,5 | 0,06), (2 | 0,14).",
    zwischenergebnis="f(x) = (x − 1)² · e^(−x)|f(0,5) ≈ 0,152|f(1,5) ≈ 0,056|f(2) ≈ 0,135",
    niveau_geschaetzt="I",
    fehlerquelle="eine Nullstelle des Faktors e^(−x) suchen oder den Graphen bei x = 1 mit einem Knick statt mit waagerechter Tangente zeichnen",
    bemerkung="CAS-Nachtrag zu 2017-be-gk-B1.2b (WTR): Zuschnitt – die Schnittpunkte mit den Koordinatenachsen (in der WTR-Fassung Teil von a) und das Zeichnen des Graphen (WTR b) stehen in einer Teilaufgabe; die Extrempunkte aus WTR a stehen in b (Zeile 2017-be-gk-cas-B1.2b, Nachtragsvermerk auf WTR a); 5 BE gegen 11 + 3 BE. Das Feld skizze nennt das Foto und die vom Prüfling zu erstellende Zeichnung. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B1.2b", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="b", seite="4", punkte="9",
    leitidee="Analysis",
    thema="Ableitungsregeln",
    typ="Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden",
    typ_neben="Lage und Art aller lokalen Extrempunkte bestimmen|Wendepunkte über die zweite Ableitung berechnen",
    stichwoerter="erste Ableitung|Ableitungsregeln angeben|Extrempunkte|zwei Wendepunkte|ohne Kontrollangabe",
    voraussetzungen="Produkt- und Kettenregel anwenden und benennen|quadratische Gleichung lösen|zweite Ableitung bilden|Art über f″ oder den Vorzeichenwechsel bestimmen",
    format="Rechnung|Kurzantwort",
    operator="Bilden Sie|Geben Sie an|Bestimmen Sie|Ermitteln Sie",
    antwort="Term|Text|Zahl",
    material="Foto",
    skizze="Schwarz-weißes Foto eines Berliner Veranstaltungsortes: mehrere gleichartige, spitz zulaufende weiße Dachelemente vor einem Hochhaus; das Foto dient nur der Veranschaulichung und enthält keine Maße.",
    kontext="Architektur / Dach",
    textumfang="mittel",
    gegeben="Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m. Der Graph von f hat zwei Wendepunkte.",
    gesucht="erste Ableitung von f mit Angabe der verwendeten Ableitungsregeln; Art und Lage aller Extrempunkte des Graphen von f; Koordinaten der beiden Wendepunkte",
    verfahren="Mit Produkt- und Kettenregel: f′(x) = (2x − 2) · e^(−x) − (x² − 2x + 1) · e^(−x) = (−x² + 4x − 3) · e^(−x). f′(x) = 0 liefert x = 1 und x = 3; die Art über f″(x) = (x² − 6x + 7) · e^(−x) oder über den Vorzeichenwechsel von f′. Die Wendestellen aus f″(x) = 0: x = 3 ± √2 (mit dem CAS), Funktionswerte einsetzen.",
    schritte="7",
    zahlenraum="ganz|dezimal|Wurzel|Potenz",
    einheiten="",
    abhaengig_von="",
    ergebnis="f′(x) = (−x² + 4x − 3) · e^(−x) (Produktregel, für e^(−x) die Kettenregel). Tiefpunkt T(1 | 0), Hochpunkt H(3 | 4e^(−3)) ≈ (3 | 0,199). Wendepunkte W₁(3 − √2 | f(3 − √2)) ≈ (1,59 | 0,070) und W₂(3 + √2 | f(3 + √2)) ≈ (4,41 | 0,141).",
    zwischenergebnis="f″(x) = (x² − 6x + 7) · e^(−x)|f″(1) = 2/e > 0|f″(3) = −2e^(−3) < 0|f‴(x) = −(x² − 8x + 13) · e^(−x), an beiden Wendestellen ungleich null",
    niveau_geschaetzt="II",
    fehlerquelle="beim Ableiten von e^(−x) die innere Ableitung −1 vergessen oder nur die Wendestelle im Modellintervall [0; 2] angeben, obwohl beide Wendepunkte verlangt sind",
    bemerkung="CAS-Nachtrag zu 2017-be-gk-B1.2a (WTR): Zuschnitt, Auftrag und Werkzeug – die Extrempunkte aus WTR a stehen hier, die Kontrollangabe f′(x) = (−x² + 4x − 3) · e^(−x) fehlt; neu verlangt sind die Ableitung mit Angabe der Ableitungsregeln und die beiden Wendepunkte; 9 BE, die Achsenschnittpunkte aus WTR a stehen in a. Erste Leistung ist das Ableiten (typ), Extrem- und Wendepunkte stehen in typ_neben. Hochpunkt und zweiter Wendepunkt liegen außerhalb des Modellintervalls [0; 2]. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B1.2d", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="d", seite="4", punkte="3",
    leitidee="Analysis",
    thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen Graph und x-Achse aus einem Flächenstück berechnen",
    typ_neben="Fläche: Flächenmaßstab eines Modells auf eine Realfläche anwenden",
    stichwoerter="Trennwand|bestimmtes Integral|ohne vorgegebene Stammfunktion|Flächenmaßstab",
    voraussetzungen="bestimmtes Integral mit dem CAS oder über eine Stammfunktion auswerten|Längenmaßstab quadrieren",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Foto",
    skizze="Schwarz-weißes Foto eines Berliner Veranstaltungsortes: mehrere gleichartige, spitz zulaufende weiße Dachelemente vor einem Hochhaus; das Foto dient nur der Veranschaulichung und enthält keine Maße.",
    kontext="Architektur / Dach",
    textumfang="kurz",
    gegeben="Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m. Unter einem Dachelement soll eine Trennwand errichtet werden, die im Intervall [0; 1] durch den Graphen von f und die x-Achse begrenzt ist.",
    gesucht="Flächeninhalt der Trennwand in m²",
    verfahren="Die Trennwand ist die Fläche zwischen Graph und x-Achse über [0; 1] (f ≥ 0, bei x = 1 berührt der Graph die x-Achse); das Integral von 0 bis 1 über f mit dem CAS berechnen (Stammfunktion (−x² − 1) · e^(−x)). 1 LE = 10 m heißt 1 FE = 100 m².",
    schritte="3",
    zahlenraum="dezimal|Potenz",
    einheiten="m|m²",
    abhaengig_von="",
    ergebnis="∫₀¹ f(x) dx = 1 − 2/e ≈ 0,264 FE, also etwa 26,4 m².",
    zwischenergebnis="Stammfunktion (−x² − 1) · e^(−x)|1 − 2/e ≈ 0,2642",
    niveau_geschaetzt="I",
    fehlerquelle="mit 10 statt 100 umrechnen oder über [0; 2] statt über [0; 1] integrieren",
    bemerkung="CAS-Nachtrag zu 2017-be-gk-B1.2d (WTR): der Nachweis der vorgegebenen Stammfunktion F(x) = (−x² − 1) · e^(−x) entfällt, F ist nicht angegeben – das Integral liefert das CAS; 3 statt 5 BE. Deshalb ein anderer Haupttyp als in der WTR-Zeile (dort der Nachweis der Stammfunktion, die Fläche Nebentyp). Eigene Rechnung, mit sympy bestätigt (26,42 m²).")
row(id="2017-be-gk-cas-B1.2e", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="e", seite="4", punkte="7",
    leitidee="Analysis",
    thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen",
    typ_neben="Flächeninhalt oder Umfang des Dreiecks aus Tangente und Koordinatenachsen berechnen|Fläche: Flächenmaßstab eines Modells auf eine Realfläche anwenden",
    stichwoerter="Tangente in R(0 | 1)|Achsendreieck|eingesparte Wandfläche|Flächenmaßstab",
    voraussetzungen="Ableitung an einer Stelle auswerten|Nullstelle einer linearen Funktion|Dreiecksfläche berechnen|Längenmaßstab quadrieren",
    format="Rechnung",
    operator="Ermitteln Sie|Berechnen Sie",
    antwort="Term|Zahl",
    material="Foto",
    skizze="Schwarz-weißes Foto eines Berliner Veranstaltungsortes: mehrere gleichartige, spitz zulaufende weiße Dachelemente vor einem Hochhaus; das Foto dient nur der Veranschaulichung und enthält keine Maße.",
    kontext="Architektur / Dach",
    textumfang="mittel",
    gegeben="Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m. f′(x) = (−x² + 4x − 3) · e^(−x). Die Trennwand unter dem Graphen über [0; 1] hat etwa 26,4 m². Statt ihrer soll eine kleinere Wand verwendet werden, die durch die Koordinatenachsen und die Tangente an den Graphen von f im Punkt R(0 | 1) begrenzt ist.",
    gesucht="Gleichung der Tangente in R; eingesparte Wandfläche in m²",
    verfahren="Steigung f′(0) = −3, also t(x) = −3x + 1. Die Tangente schneidet die x-Achse bei x = 1/3; das Achsendreieck hat den Inhalt 1/2 · 1 · 1/3 = 1/6 FE = 100/6 m². Die Einsparung ist die Differenz zur Trennwandfläche aus d.",
    schritte="4",
    zahlenraum="Bruch|dezimal",
    einheiten="m²",
    abhaengig_von="2017-be-gk-cas-B1.2d",
    ergebnis="t(x) = −3x + 1; kleinere Wand 1/6 FE ≈ 16,7 m², eingespart werden 100 · (5/6 − 2/e) ≈ 9,8 m².",
    zwischenergebnis="Nullstelle der Tangente x = 1/3|Dreieck 1/6 FE|Trennwand 1 − 2/e FE",
    niveau_geschaetzt="II",
    fehlerquelle="die eingesparte Fläche mit gerundeten Zwischenwerten (26,4 − 17) statt exakt berechnen oder den Flächenmaßstab vergessen",
    bemerkung="Dublette von: 2017-be-gk-B1.2e. CAS-Nachtrag zu 2017-be-gk-B1.2e (WTR): nur BE: 7 statt 9 BE, Wortlaut und Angaben gleich. Die Ableitung f′ ist in der CAS-Fassung nicht vorgegeben, sondern in b selbst gebildet. Felder wie in der WTR-Zeile, Fakten des CAS-Hefts (Seite, BE). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B1.2f", block="B", aufgabe="1.2", titel="Dachformen", teilaufgabe="f", seite="4", punkte="4",
    leitidee="Analysis",
    thema="Tangente, Normale, Schnittwinkel",
    typ="Berührpunkt der Tangente mit vorgegebener Steigung berechnen",
    typ_neben="Steigungswinkel in einen Anstieg umrechnen",
    stichwoerter="Gefälle 45°|Steigung −1|Gleichung f′(x) = −1|Rechner",
    voraussetzungen="Gefällewinkel über den Tangens in eine negative Steigung umrechnen|Gleichung mit e-Funktion mit dem CAS lösen|Lösung im Modellintervall auswählen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Foto",
    skizze="Schwarz-weißes Foto eines Berliner Veranstaltungsortes: mehrere gleichartige, spitz zulaufende weiße Dachelemente vor einem Hochhaus; das Foto dient nur der Veranschaulichung und enthält keine Maße.",
    kontext="Architektur / Dach",
    textumfang="kurz",
    gegeben="Die äußere Kante eines geplanten Dachelements wird im Intervall [0; 2] annähernd durch f mit f(x) = (x² − 2x + 1) · e^(−x) beschrieben, 1 LE = 10 m. Aus b ist f′(x) = (−x² + 4x − 3) · e^(−x) bekannt.",
    gesucht="Koordinaten des Punktes Q, in dem das Dachelement ein Gefälle von 45° hat",
    verfahren="Ein Gefälle von 45° bedeutet die Steigung tan(−45°) = −1. Die Gleichung (−x² + 4x − 3) · e^(−x) = −1 mit dem CAS lösen; im Intervall [0; 2] gibt es genau eine Lösung (f′ steigt dort von −3 bis 0 bei x = 1 und ist danach positiv). Den Funktionswert einsetzen.",
    schritte="3",
    zahlenraum="dezimal|negativ|Potenz",
    einheiten="m",
    abhaengig_von="2017-be-gk-cas-B1.2b",
    ergebnis="Q ≈ (0,41 | 0,23), in Realmaßen bei x ≈ 4,1 m in etwa 2,3 m Höhe.",
    zwischenergebnis="f′(x) = −1 bei x ≈ 0,4145|f(0,4145) ≈ 0,2264",
    niveau_geschaetzt="II",
    fehlerquelle="die Steigung +1 statt −1 ansetzen (Gefälle heißt fallend) oder f(x) = −1 statt f′(x) = −1 lösen",
    bemerkung="CAS-Nachtrag, ohne WTR-Gegenstück: die Teilaufgabe steht nur in der CAS-Fassung (Art ganze Aufgabe, Befund vom 28.09.2026); die CAS-Teilaufgabe g entspricht der WTR-Teilaufgabe f. Das Gefälle von 45° als Steigung −1 gelesen (Winkel gegen die Waagerechte). Die Gleichung ist nur numerisch lösbar. Eigene Rechnung, mit sympy bestätigt (nsolve).")
row(id="2017-be-gk-cas-B2.2c", block="B", aufgabe="2.2", titel="Schokotrüffel", teilaufgabe="c", seite="6", punkte="6",
    leitidee="Analytische Geometrie",
    thema="Skalarprodukt und Winkel",
    typ="Stumpfen Winkel zwischen zwei benachbarten Seitenflächen einer Pyramide über die Normalenvektoren berechnen",
    typ_neben="Streckenlänge berechnen",
    stichwoerter="Seitenwand ABFE|Deckelfläche EFS|Winkel an der Kante EF|Normalenvektoren|größter Abstand",
    voraussetzungen="Normalenvektor einer Ebene aus drei Punkten bestimmen|Winkel zwischen Normalenvektoren berechnen|stumpfen Innenwinkel als Ergänzung zu 180° erkennen|Eckenabstände vergleichen",
    format="Rechnung",
    operator="Ermitteln Sie|Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild ohne Koordinatenachsen: unten die quadratische Grundfläche ABCD (A vorn links, B vorn rechts, C hinten rechts, D hinten links), darüber die kleinere quadratische Deckfläche EFGH (E über A, F über B, G über C, H über D), die Seitenkanten AE, BF, CG, DH laufen nach oben leicht zusammen; auf der Deckfläche sitzt die Pyramide mit der Spitze S über der Mitte. Verdeckte Kanten (an D und H) sind gestrichelt. Keine Maßangaben in der Abbildung.",
    kontext="Verpackung",
    textumfang="mittel",
    gegeben="Verpackung für Schokotrüffel: gerader quadratischer Pyramidenstumpf ABCDEFGH mit aufgesetzter gerader quadratischer Pyramide EFGHS als Deckel. Kantenlänge AB = 10 cm, Kantenlänge EF der Deckfläche 8 cm, Höhe des Stumpfs 6 cm, Gesamthöhe der Verpackung 9 cm, 1 LE = 1 cm. Eckpunkte B(10 | 10 | 0), D(0 | 0 | 0), F(9 | 9 | 6), Spitze S(5 | 5 | 9). A(10 | 0 | 0), C(0 | 10 | 0), E(9 | 1 | 6), G(1 | 9 | 6), H(1 | 1 | 6); die Seitenwand ABFE liegt in E1: 6x + z = 60.",
    gesucht="Größe des Winkels γ, den die Seitenwand ABFE mit der angrenzenden dreieckigen Deckelfläche EFS einschließt; größter Abstand zweier Punkte innerhalb der Verpackung",
    verfahren="Normalenvektor der Ebene EFS aus EF und ES bestimmen, etwa (3 | 0 | 4) (Ebene 3x + 4z = 51), dazu (6 | 0 | 1) von E1. Der Winkel zwischen den Normalenvektoren ist 43,7°; die beiden Flächen schließen an der Kante EF den stumpfen Winkel γ = 180° − 43,7° ein (Kontrolle über die Vektoren von der Mitte von EF zur Spitze S und zur Mitte von AB). Für den größten Abstand die Eckenabstände vergleichen: die Diagonale der Grundfläche ist länger als die Raumdiagonale DF.",
    schritte="5",
    zahlenraum="dezimal|Wurzel",
    einheiten="cm|°",
    abhaengig_von="2017-be-gk-B2.2b",
    ergebnis="γ ≈ 136,3° (die Ebenen schneiden sich unter 43,7°). Der größte Abstand ist die Diagonale der Grundfläche: |AC| = |BD| = 10√2 ≈ 14,14 cm (die Raumdiagonale DF ist mit √198 ≈ 14,07 cm etwas kürzer).",
    zwischenergebnis="Normalenvektor von EFS (3 | 0 | 4)|cos φ = 22/(5 · √37) ≈ 0,7234|φ ≈ 43,67°|γ = 180° − φ ≈ 136,33°",
    niveau_geschaetzt="II",
    fehlerquelle="den Schnittwinkel der Ebenen (43,7°) statt des von den Flächen eingeschlossenen stumpfen Winkels angeben oder die Raumdiagonale DF als größten Abstand nehmen",
    bemerkung="CAS-Nachtrag zu 2017-be-gk-B2.2c (WTR): anderer Auftrag – gesucht ist der Winkel zwischen der Seitenwand ABFE und der angrenzenden Deckelfläche EFS statt mit der Grundfläche ABCD; 6 statt 5 BE; der größte Abstand wie in der WTR-Fassung. Deshalb ein anderer Haupttyp (stumpfer Winkel zwischen zwei Nachbarflächen); das Etikett nennt eine Pyramide, hier grenzen die Stumpfwand und die Deckelpyramide an der Kante EF aneinander, der Lösungsweg ist derselbe. Den eingeschlossenen Winkel als Innenwinkel des Körpers an der Kante EF gelesen (stumpf). abhaengig_von zeigt auf die WTR-Zeile b, weil die wortgleiche CAS-Teilaufgabe b keine eigene Zeile hat. Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B2.2d", block="B", aufgabe="2.2", titel="Schokotrüffel", teilaufgabe="d", seite="6", punkte="3",
    leitidee="Analytische Geometrie",
    thema="Flächeninhalt und Volumen im Raum",
    typ="Körper: Oberflächeninhalt einer quadratischen Pyramide berechnen",
    typ_neben="",
    stichwoerter="Deckel|Seitendreiecke|Seitenhöhe|Goldfolie",
    voraussetzungen="Pyramidenhöhe aus den Koordinaten ablesen|Satz des Pythagoras|Dreiecksfläche",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Körper",
    skizze="Schrägbild ohne Koordinatenachsen: unten die quadratische Grundfläche ABCD (A vorn links, B vorn rechts, C hinten rechts, D hinten links), darüber die kleinere quadratische Deckfläche EFGH (E über A, F über B, G über C, H über D), die Seitenkanten AE, BF, CG, DH laufen nach oben leicht zusammen; auf der Deckfläche sitzt die Pyramide mit der Spitze S über der Mitte. Verdeckte Kanten (an D und H) sind gestrichelt. Keine Maßangaben in der Abbildung.",
    kontext="Verpackung",
    textumfang="kurz",
    gegeben="Verpackung für Schokotrüffel: gerader quadratischer Pyramidenstumpf ABCDEFGH mit aufgesetzter gerader quadratischer Pyramide EFGHS als Deckel. Kantenlänge AB = 10 cm, Kantenlänge EF der Deckfläche 8 cm, Höhe des Stumpfs 6 cm, Gesamthöhe der Verpackung 9 cm, 1 LE = 1 cm. Eckpunkte B(10 | 10 | 0), D(0 | 0 | 0), F(9 | 9 | 6), Spitze S(5 | 5 | 9). Die vier Seitenflächen des pyramidenförmigen Deckels über der Deckfläche EFGH (Kantenlänge 8 cm, in 6 cm Höhe) werden mit Goldfolie überzogen; die Spitze liegt in 9 cm Höhe.",
    gesucht="benötigte Goldfolie in cm² für einen Deckel",
    verfahren="Pyramidenhöhe 9 − 6 = 3 cm; Seitenhöhe eines Dreiecks über der halben Kante 4 cm mit Pythagoras √(3² + 4²) = 5 cm. Vier Dreiecke mit Grundseite 8 cm und Höhe 5 cm.",
    schritte="3",
    zahlenraum="ganz",
    einheiten="cm|cm²",
    abhaengig_von="2017-be-gk-B2.2a",
    ergebnis="Für einen Deckel werden 4 · 1/2 · 8 · 5 = 80 cm² Goldfolie benötigt.",
    zwischenergebnis="Pyramidenhöhe 3 cm|Seitenhöhe 5 cm",
    niveau_geschaetzt="II",
    fehlerquelle="die Pyramidenhöhe 3 cm statt der Seitenhöhe 5 cm als Dreieckshöhe nehmen oder die Deckfläche EFGH mitzählen",
    bemerkung="Dublette von: 2017-be-gk-B2.2d. CAS-Nachtrag zu 2017-be-gk-B2.2d (WTR): nur BE: 3 statt 4 BE, Wortlaut und Angaben gleich. Felder wie in der WTR-Zeile, Fakten des CAS-Hefts (Seite, BE). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B3.1e", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="e", seite="7", punkte="2",
    afb_amtlich="I",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Modalwert einer Binomialverteilung bestimmen",
    typ_neben="",
    stichwoerter="n = 250, p = 0,05|Erwartungswert 12,5 nicht ganzzahlig|P(X = 12) ≈ 11,6 % > P(X = 13) ≈ 11,2 %|wahrscheinlichste Anzahl 12",
    voraussetzungen="Erwartungswert n · p|Einzelwahrscheinlichkeiten am Rechner|Nachbarwerte vergleichen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Tabelle mit den Spalten Werk A, B, C, D und den Zeilen „Anteil an der Gesamtzahl“ (10 %, 30 %, 20 %, 40 %) und „Anteil der fehlerhaften Geräte“ (5 %, 3 %, 4 %, 2 %).",
    kontext="Produktion / Smartphones",
    textumfang="kurz",
    gegeben="Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %. Von im Werk A hergestellten Geräten werden 250 zufällig ausgewählt; X: Anzahl der fehlerhaften, binomialverteilt mit n = 250 und p = 0,05.",
    gesucht="die Anzahl fehlerhafter Geräte, die darunter mit der größten Wahrscheinlichkeit auftritt",
    verfahren="Erwartungswert 250 · 0,05 = 12,5 ist nicht ganzzahlig; P(X = 12) und P(X = 13) berechnen und vergleichen.",
    schritte="2",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    abhaengig_von="",
    ergebnis="Der Erwartungswert von X ist 250 · 0,05 = 12,5; P(X = 12) ≈ 11,6 %, P(X = 13) ≈ 11,2 %; damit ist die gesuchte Anzahl 12 (amtlich)",
    zwischenergebnis="P(X = 12) ≈ 0,1160|P(X = 13) ≈ 0,1117",
    niveau_geschaetzt="I",
    fehlerquelle="12,5 oder aufgerundet 13 als Anzahl angeben",
    bemerkung="Dublette von: 2017MgrundlegendBStochastikCAS-2c. CAS-Nachtrag zu 2017-be-gk-B3.1e (WTR): Zahl und Auftrag – 250 statt 20 Geräte aus Werk A, gefragt die wahrscheinlichste Anzahl fehlerhafter Geräte statt der Wahrscheinlichkeit für kein fehlerhaftes; anderer Typ als die WTR-Zeile. AB amtlich: I. Wortgleich mit der CAS-Poolaufgabe (Teilaufgabe 2 c, gleiche BE; im Heft laufen die Buchstaben von 1 a–b und 2 a–e als a–g durch); Felder aus der Poolzeile. Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy (0,11597; 0,11174).")
row(id="2017-be-gk-cas-B3.1g", block="B", aufgabe="3.1", titel="Smartphone", teilaufgabe="g", seite="7", punkte="4",
    afb_amtlich="III",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Mindestumfang für eine Mindestwahrscheinlichkeit von mehr als k Treffern ermitteln",
    typ_neben="",
    stichwoerter="Werk C, 4 % fehlerhaft: fehlerfrei mit p = 0,96|P(X >= 500) >= 0,9|n = 526: 88,5 %, n = 527: 91,9 %|mindestens 527 Geräte",
    voraussetzungen="Trefferdefinition wechseln (nicht fehlerhaft)|Binomialmodell mit unbekanntem n|Probieren am Rechner",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Tabelle",
    skizze="Tabelle mit den Spalten Werk A, B, C, D und den Zeilen „Anteil an der Gesamtzahl“ (10 %, 30 %, 20 %, 40 %) und „Anteil der fehlerhaften Geräte“ (5 %, 3 %, 4 %, 2 %).",
    kontext="Produktion / Smartphones",
    textumfang="mittel",
    gegeben="Ein Hersteller bringt ein neues Smartphone auf den Markt. Die Geräte werden in vier Werken in jeweils großer Stückzahl hergestellt; Anteil an der Gesamtzahl: Werk A 10 %, B 30 %, C 20 %, D 40 %; Anteil der fehlerhaften Geräte unter den im Werk hergestellten: A 5 %, B 3 %, C 4 %, D 2 %. Es werden im Werk C hergestellte Geräte zufällig ausgewählt.",
    gesucht="Mindestanzahl der auszuwählenden Geräte, damit sich darunter mit einer Wahrscheinlichkeit von mindestens 90 % mindestens 500 Geräte befinden, die nicht fehlerhaft sind",
    verfahren="X: Anzahl der nicht fehlerhaften Geräte, binomialverteilt mit p = 0,96; das kleinste n mit P(X >= 500) >= 0,9 durch Probieren mit dem Rechner suchen.",
    schritte="3",
    zahlenraum="Prozent|dezimal|ganz",
    einheiten="",
    abhaengig_von="",
    ergebnis="Ist n die Anzahl auszuwählender Geräte, so liefert Probieren für n = 526: P(X >= 500) ≈ 88,5 % und für n = 527: P(X >= 500) ≈ 91,9 %; es müssen mindestens 527 Geräte ausgewählt werden (amtlich)",
    zwischenergebnis="n = 525: 0,842|n = 526: 0,885|n = 527: 0,919",
    niveau_geschaetzt="III",
    fehlerquelle="mit p = 0,04 (fehlerhaft) rechnen oder n aus dem Erwartungswert 500/0,96 ≈ 521 bestimmen",
    bemerkung="Dublette von: 2017MgrundlegendBStochastikCAS-2e. CAS-Nachtrag zu 2017-be-gk-B3.1g (WTR): Zahl und Auftrag – 90 % statt 95 %, mindestens 500 fehlerfreie statt mindestens ein fehlerhaftes Gerät; anderer Typ als die WTR-Zeile. AB amtlich: III. Wortgleich mit der CAS-Poolaufgabe (Teilaufgabe 2 e, gleiche BE; im Heft laufen die Buchstaben von 1 a–b und 2 a–e als a–g durch); Felder aus der Poolzeile. Deutungsliste (f) der Poolzeile: Mindestumfang für eine Mindestwahrscheinlichkeit, amtlich III. Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy (0,8853; 0,9189).")
row(id="2017-be-gk-cas-B3.2c", block="B", aufgabe="3.2", titel="Zufallsexperimente", teilaufgabe="c", seite="8", punkte="4",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Binomialwahrscheinlichkeit mit der Bernoulli-Formel oder der Tabelle berechnen",
    typ_neben="",
    stichwoerter="zehnmal drehen|genau viermal Rot|mindestens fünfmal Rot|Kontrollangabe P(C2)",
    voraussetzungen="Trefferwahrscheinlichkeit 0,4 am Glücksrad abzählen|Bernoulli-Formel|Gegenereignis bei kumulierten Werten",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="Skizze",
    skizze="Abbildung neben dem Text: Würfelnetz W in Kreuzform mit den Feldern 2 (oben), 1, 2, 2, 2 (mittlere Reihe) und 1 (unten); Glücksrad G1 mit zehn gleichen Sektoren, im Uhrzeigersinn von oben links b, r, r, r, r, w, w, b, b, b (r rot, b blau, w weiß); Glücksrad G2 in vier Viertel geteilt: b oben links, r oben rechts, r unten links, s unten rechts (s schwarz). Über jedem Rad zeigt ein Pfeil oben links als Zeiger auf den Rand.",
    kontext="Glücksspiel / Würfel und Glücksrad",
    textumfang="kurz",
    gegeben="Ein Würfel W, durch Neubeschriftung aus einem Laplace-Würfel entstanden, trägt viermal die 2 und zweimal die 1. Glücksrad G1 hat zehn gleich große Sektoren: 4 rot, 4 blau, 2 weiß; Glücksrad G2 hat vier gleich große Sektoren: 2 rot, 1 blau, 1 schwarz. Ein gedrehtes Rad bleibt zufällig auf einem Sektor stehen, nie auf einer Grenze. Lisa dreht das Glücksrad G1 zehnmal. C1: G1 zeigt genau viermal Rot. C2: G1 zeigt mindestens fünfmal Rot. Kontrollangabe: P(C2) ≈ 0,3669.",
    gesucht="Wahrscheinlichkeiten der Ereignisse C1 und C2",
    verfahren="X: Anzahl Rot, binomialverteilt mit n = 10 und p = 0,4. P(C1) = P(X = 4) mit der Bernoulli-Formel oder dem Rechner; P(C2) = 1 − P(X ≤ 4) mit dem Rechner.",
    schritte="3",
    zahlenraum="dezimal|Bruch",
    einheiten="",
    abhaengig_von="",
    ergebnis="P(C1) = (10 über 4) · 0,4⁴ · 0,6⁶ ≈ 0,2508; P(C2) = 1 − 0,6331 = 0,3669.",
    zwischenergebnis="P(X ≤ 4) = 0,6331|P(X ≤ 3) = 0,3823",
    niveau_geschaetzt="I",
    fehlerquelle="P(X ≥ 5) als 1 − P(X ≤ 5) ablesen oder p = 0,5 annehmen, weil Rot und Blau gleich viele Felder haben",
    bemerkung="Dublette von: 2017-be-gk-B3.2c. CAS-Nachtrag zu 2017-be-gk-B3.2c (WTR): nur BE: 4 statt 5 BE, Wortlaut und Angaben gleich. Die CAS-Fassung hat keine Anlage (Tafel der summierten Binomialverteilung); die kumulierte Wahrscheinlichkeit liefert der Rechner, die Kontrollangabe P(C2) ≈ 0,3669 steht wie in der WTR-Fassung. Der Befund vom 28.09.2026 führt die Teilaufgabe als nur BE (Text wortgleich); typ bleibt der der WTR-Zeile. Felder wie in der WTR-Zeile, Fakten des CAS-Hefts (Seite, BE). Eigene Rechnung, mit sympy bestätigt.")
row(id="2017-be-gk-cas-B3.2d", block="B", aufgabe="3.2", titel="Zufallsexperimente", teilaufgabe="d", seite="8", punkte="4",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Trefferzahlen mit einer Einzelwahrscheinlichkeit über einer Schranke mit dem Rechner ermitteln",
    typ_neben="Fehlerwahrscheinlichkeit einer Einheit binomial berechnen und als Trefferwahrscheinlichkeit einer zweiten Binomialverteilung verwenden",
    stichwoerter="30 Durchgänge|Ereignis C2 als Treffer|Einzelwahrscheinlichkeiten über 10 %|genau fünf Werte|Behauptung prüfen",
    voraussetzungen="Ereignis eines Teilexperiments als Treffer einer neuen Bernoulli-Kette deuten|Einzelwahrscheinlichkeiten einer Binomialverteilung mit dem Rechner tabellieren|Werte mit einer Schranke vergleichen und zählen",
    format="Rechnung|Begründung",
    operator="Prüfen Sie",
    antwort="Zahl|Text",
    material="Skizze",
    skizze="Abbildung neben dem Text: Würfelnetz W in Kreuzform mit den Feldern 2 (oben), 1, 2, 2, 2 (mittlere Reihe) und 1 (unten); Glücksrad G1 mit zehn gleichen Sektoren, im Uhrzeigersinn von oben links b, r, r, r, r, w, w, b, b, b (r rot, b blau, w weiß); Glücksrad G2 in vier Viertel geteilt: b oben links, r oben rechts, r unten links, s unten rechts (s schwarz). Über jedem Rad zeigt ein Pfeil oben links als Zeiger auf den Rand.",
    kontext="Glücksspiel / Würfel und Glücksrad",
    textumfang="mittel",
    gegeben="Ein Würfel W, durch Neubeschriftung aus einem Laplace-Würfel entstanden, trägt viermal die 2 und zweimal die 1. Glücksrad G1 hat zehn gleich große Sektoren: 4 rot, 4 blau, 2 weiß; Glücksrad G2 hat vier gleich große Sektoren: 2 rot, 1 blau, 1 schwarz. Ein gedrehtes Rad bleibt zufällig auf einem Sektor stehen, nie auf einer Grenze. Lisa dreht das Glücksrad G1 zehnmal; C2: G1 zeigt mindestens fünfmal Rot, P(C2) ≈ 0,3669. Tom spielt das zehnmalige Drehen in Gedanken 30-mal durch und bestimmt die Wahrscheinlichkeit dafür, dass C2 genau i-mal eintritt (i = 0; 1; …; 30). Er behauptet, dass für genau fünf Werte von i diese Wahrscheinlichkeit größer als 10 % ist.",
    gesucht="Prüfung der Behauptung",
    verfahren="Y: Anzahl der Durchgänge mit C2, binomialverteilt mit n = 30 und p = P(C2) ≈ 0,3669. Mit dem CAS die Einzelwahrscheinlichkeiten P(Y = i) für i = 0 bis 30 tabellieren und die Werte über 0,1 zählen; die Verteilung steigt bis i = 11 (Erwartungswert ≈ 11) und fällt danach, es genügt also, die Werte um den Erwartungswert und ihre Nachbarn zu prüfen.",
    schritte="3",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    abhaengig_von="2017-be-gk-cas-B3.2c",
    ergebnis="P(Y = i) > 10 % genau für i = 9, 10, 11, 12, 13 (≈ 11,7 %, 14,2 %, 15,0 %, 13,7 %, 11,0 %); P(Y = 8) ≈ 8,2 % und P(Y = 14) ≈ 7,8 % liegen darunter. Die Behauptung trifft zu.",
    zwischenergebnis="Erwartungswert 30 · 0,3669 ≈ 11,0|P(Y = 8) ≈ 0,0824|P(Y = 14) ≈ 0,0776",
    niveau_geschaetzt="II",
    fehlerquelle="mit p = 0,4 (Rot bei einer Drehung) statt mit P(C2) rechnen oder kumulierte statt Einzelwahrscheinlichkeiten mit 10 % vergleichen",
    bemerkung="CAS-Nachtrag zu 2017-be-gk-B3.2d (WTR): anderer Auftrag bei gleichem Gegenstand – geprüft wird, ob genau fünf Werte von i eine Wahrscheinlichkeit über 10 % haben, statt ob die Wahrscheinlichkeit für genau 15 Eintritte unter 5 % liegt; 4 statt 3 BE. Neuer Typ: der Bestand kennt einzelne Binomialwahrscheinlichkeiten und Grenzen kumulierter Wahrscheinlichkeiten, nicht das Auszählen der Trefferzahlen, deren Einzelwahrscheinlichkeit eine Schranke überschreitet. Mit p = 0,3669 (Kontrollangabe) und mit dem exakten P(C2) = 3582976/9765625 dieselben fünf Werte. Eigene Rechnung, mit sympy bestätigt.")

NEUE_TYPEN = [
    ("Lage eines Graphen zwischen zwei Geraden auf einem Intervall über die Differenzfunktionen nachweisen", "Analysis", "Kurvenuntersuchung",
     "Nachweisen, dass ein Graph auf einem Intervall ganz in dem Streifen zwischen zwei Geraden liegt: die Differenzen zu beiden Geraden bilden und zeigen, dass sie dort nicht negativ sind – über eine Faktorisierung (Vorzeichen der Faktoren) oder über das Minimum der Differenzfunktion samt Randwerten.",
     "2017-be-gk-cas-B1.1e"),
    ("Trefferzahlen mit einer Einzelwahrscheinlichkeit über einer Schranke mit dem Rechner ermitteln", "Stochastik", "Binomialverteilung",
     "Für eine Binomialverteilung die Einzelwahrscheinlichkeiten P(X = k) mit dem Rechner tabellieren, die Trefferzahlen k bestimmen, deren Wahrscheinlichkeit eine vorgegebene Schranke überschreitet, und daran eine Aussage über ihre Anzahl prüfen.",
     "2017-be-gk-cas-B3.2d"),
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
# Landes-Dublette (v0.15, Beschluss vom 26.09.2026 Punkt 3): Nachtragszeile, die sich von ihrer
# WTR-Zeile nur in BE oder Zahlen unterscheidet; Verweis auf die Zeile des WTR-Hefts (abi-Katalog).
LANDES_ID = r"\d{4}-(?:be|bb|bebb)-(?:gk|lk|ea)-[AB]\d+(?:\.\d+)?[a-z]"
MARKE_LANDESDUBLETTE = re.compile(r"Dublette von: (" + LANDES_ID + r")\. ")
VERMERK_LANDESDUBLETTE = re.compile(r"\bnur (BE und Zahl|BE|Zahl): ")
ABI_ZEILEN = {}  # id → Zeile des abi-Katalogs (Ziel der Landes-Dublette); füllt main()


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
    # Landes-Dublette (v0.15): afb_amtlich wie die WTR-Zeile, geprüft unten.
    ml = MARKE_LANDESDUBLETTE.match(z["bemerkung"])
    if ml is None:
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
        a(m is not None or ml is not None, f"{i}: „Dublette von:“ ohne gültige Pool-Kennung in bemerkung")
    # Landes-Dublette (v0.15): Verweis auf die WTR-Zeile derselben Aufgabe, typ und afb_amtlich
    # gleich, Vermerk „nur BE: …“ / „nur Zahl: …“, Nachtragsvermerk auf dieselbe Zeile
    if ml:
        a(m is None and "Poolaufgabe (nicht erfasst" not in b and "Abgewandelt von" not in b,
          f"{i}: Landes-Dublette neben einem Poolvermerk")
        wtr = wtr_papier(z["papier"])
        ref = ABI_ZEILEN.get(ml.group(1))
        a(ref is not None and ref["papier"] == wtr and ref["block"] == z["block"]
          and ref["aufgabe"] == z["aufgabe"],
          f"{i}: Dublette von {ml.group(1)} – keine Zeile derselben Aufgabe im WTR-Heft {wtr or '?'}")
        if ref:
            a(z["typ"] == ref["typ"], f"{i}: Dublette von {ml.group(1)}, aber typ weicht ab")
            a(z["afb_amtlich"] == ref["afb_amtlich"],
              f"{i}: Dublette von {ml.group(1)}, aber afb_amtlich weicht von der WTR-Zeile ab")
            mv = VERMERK_LANDESDUBLETTE.search(b)
            a(mv is not None, f"{i}: Landes-Dublette ohne Vermerk „nur BE: …“, „nur Zahl: …“ "
                              f"oder „nur BE und Zahl: …“ in bemerkung")
            if mv:
                a((z["punkte"] != ref["punkte"]) == (mv.group(1) != "Zahl"),
                  f"{i}: Vermerk „nur {mv.group(1)}“ passt nicht zu {z['punkte']} BE gegen "
                  f"{ref['punkte']} BE der WTR-Zeile")
            mn = MARKE_NACHTRAG.search(b)
            a(mn is not None and mn.group(1) == ml.group(1),
              f"{i}: Landes-Dublette braucht „CAS-Nachtrag zu {ml.group(1)} (WTR): …“")
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
    ABI_ZEILEN.update({z["id"]: z for z in alt})  # Ziel der Landes-Dublette (v0.15)
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
        landes = [z for z in alt if MARKE_LANDESDUBLETTE.match(z["bemerkung"])]
        if landes:  # v0.15: nur wenn es welche gibt (Ausgabe sonst wie 0.14)
            print(f"Landes-Dubletten (Dublette von: <WTR-id>): {len(landes)} Zeilen ("
                  + ", ".join(f"{h} {sum(1 for z in landes if z['papier'] == h)}"
                              for h in sorted({z['papier'] for z in landes}))
                  + "), jede zeigt auf eine WTR-Zeile derselben Aufgabe mit gleichem typ und afb_amtlich.")
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
    landes = [z["id"] for z in ZEILEN if MARKE_LANDESDUBLETTE.match(z["bemerkung"])]
    if landes:  # v0.15
        print(f"Landes-Dubletten (Dublette von: <WTR-id>): {len(landes)} – {', '.join(landes)}")
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
