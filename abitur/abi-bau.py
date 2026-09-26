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
    "jahr": "2018",
    "papier": "2018-be-gk-cas",
    "datei": "hefte/abi/2018-be-gk-cas.pdf",  # amtliches Heft (Bildungsserver, 18_Ma_GK_CAS_Aufgaben.pdf), 10 Seiten mit Textebene, lokal (abi-quellen.md § 2, § 8)
    "seiten": 10,
    # CAS-Nachtrag (v0.14/v0.15, abi.md § 7, Beschluss vom 26.09.2026 Punkt 3): Zeilen für die 16
    # abweichenden Teilaufgaben (befund-cas-berlin-2026-09-28.md) – eigene Zeilen für Werkzeug, Auftrag,
    # Zuschnitt, ganze Aufgabe; Landes-Dublette für nur BE (1.1 b, d) und nur Zahl (3.1 b); 3.2 a
    # Poolverweis. BE der Zeilen je Aufgabe: 1.1 b 4, c 7, d 3, e 4, f 11, g 8 = 37; 1.2 a 4, b 6,
    # c 4, d 4, e 4, f 4, g 5, h 9 = 40; 3.1 b 5; 3.2 a 4.
    "nachtrag_zu": "2018-be-gk",
    "soll": {"1.1": 37, "1.2": 40, "3.1": 5, "3.2": 4},
    # wortgleiche Teilaufgaben mit gleichen BE ohne Zeile: CAS-Buchstabe → (WTR-Buchstabe, BE)
    "uebernommen": {"1.1": {"a": ("a", 3)},
                    "3.1": {"a": ("a", 2), "c": ("c", 5), "d": ("d", 2), "e": ("e", 6)},
                    "3.2": {"b": ("b", 2), "c": ("c", 3), "d": ("d", 4), "e": ("e", 3), "f": ("f", 2), "g": ("g", 2)}},
    # Aufgaben ohne abweichende Teilaufgabe (Summe je Aufgabe)
    "unveraendert": {"2.1": 20, "2.2": 20},
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
# Heft 2018-be-gk-cas (amtliches Heft 18_Ma_GK_CAS_Aufgaben, 10 Seiten mit Textebene;
# CAS-Nachtrag zu 2018-be-gk, Auftrag Nacht 2026-09-29, Teil 4; Beschluss vom 26.09.2026 Punkt 3).
# Messung und Art je Teilaufgabe: abitur/befund-cas-berlin-2026-09-28.md. Eigene Zeile für die
# Arten Werkzeug, Auftrag, Zuschnitt, ganze Aufgabe; Landes-Dublette („Dublette von: <WTR-id>“,
# abi-bau.py v0.15) für nur BE (1.1 b, d) und nur Zahl (3.1 b); wortgleiche Teilaufgaben übernommen.
# Pool: 3.2 a (nur Zahl gegenüber dem WTR-Heft) ist wortgleich mit der Poolfassung 2018 grundlegend
# Teil B Stochastik WTR 2, Teilaufgabe 1 a (Stapel 2018-ga-B-wtr, erfasst) – Poolverweis statt
# Landes-Dublette. Die CAS-Pooldateien 2018 grundlegend (Analysis CAS 1, 2; Stochastik CAS; AG/LA
# CAS 1, 2) enthalten keine Aufgabe des Hefts. Keine amtlichen Lösungen: jede Zeile „Eigene
# Rechnung“ (sympy); Seiten gerendert.

row(id="2018-be-gk-cas-B1.1b", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="b", seite="2", punkte="4",
    leitidee="Analysis",
    thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    typ_neben="",
    stichwoerter="Querschnittsfläche|Integral|Bauwerk|Differenzfunktion",
    voraussetzungen="Stammfunktion einer ganzrationalen Funktion bilden|bestimmtes Integral berechnen|Integrationsgrenzen aus der Lage der Punkte ablesen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Skizze",
    skizze="Profilzeichnung in einem x-y-Koordinatensystem ohne Achsenteilung. Links der y-Achse liegt das grau ausgefüllte Bauwerk ABCS: A oben links auf dem Graphen von h, B senkrecht darunter, C rechts von B, S senkrecht über C auf der y-Achse; die Oberkante von A nach S ist mit h beschriftet und als Anlaufbahn bezeichnet. Rechts der y-Achse fällt der mit g beschriftete Aufsprunghang von C aus bis zum Tiefpunkt U und steigt danach leicht an; auf dem fallenden Ast ist der Punkt K markiert. Die Fläche unter dem Bauwerk und unter dem Aufsprunghang ist schraffiert.",
    kontext="Skisprunganlage",
    textumfang="kurz",
    gegeben="Bauwerk ABCS mit A(−20 | 74), B(−20 | 50), C(0 | 50) und S(0 | 54); die Oberseite von A nach S verläuft auf dem Graphen von h mit h(x) = 0,05x² + 54, 1 LE = 1 m.",
    gesucht="Inhalt der Querschnittsfläche des Bauwerks ABCS",
    verfahren="Die Fläche wird oben vom Graphen von h, unten von der waagerechten Strecke BC auf der Höhe y = 50 und seitlich von x = −20 und x = 0 begrenzt. Also das Integral der Differenz h(x) − 50 von −20 bis 0 berechnen.",
    schritte="4",
    zahlenraum="ganz|dezimal|negativ",
    einheiten="m|m²",
    abhaengig_von="2018-be-gk-B1.1a",
    ergebnis="A = 640/3 m² ≈ 213,3 m²",
    zwischenergebnis="Integrand h(x) − 50 = 0,05x² + 4|Stammfunktion x³/60 + 4x",
    niveau_geschaetzt="II",
    fehlerquelle="über h statt über h − 50 integrieren und so die Fläche bis zur x-Achse statt bis zur Strecke BC berechnen",
    bemerkung="Dublette von: 2018-be-gk-B1.1b. CAS-Nachtrag zu 2018-be-gk-B1.1b (WTR): nur BE: 4 statt 5 BE, Wortlaut und Angaben gleich. Felder wie in der WTR-Zeile, Fakten des CAS-Hefts (Seite, BE). Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.1c", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="c", seite="2", punkte="7",
    leitidee="Analysis",
    thema="Kurvenuntersuchung",
    typ="Lage und Art aller lokalen Extrempunkte bestimmen",
    typ_neben="Extrempunkt einem Punkt im Sachzusammenhang zuordnen|Mittlere Änderungsrate über ein Intervall berechnen",
    stichwoerter="Extrempunkte|tiefste Stelle U|ohne Kontrollergebnis|mittlere Steigung zwischen C und U",
    voraussetzungen="Ableitungen einer ganzrationalen Funktion bilden|Produkt gleich null setzen|Vorzeichen der zweiten Ableitung deuten|Differenzenquotient bilden",
    format="Rechnung|Begründung",
    operator="Ermitteln Sie|Entscheiden Sie|Berechnen Sie",
    antwort="Zahl|Text",
    material="Skizze",
    skizze="Profil der Skisprunganlage ohne Achsenteilung: links der y-Achse das dunkel ausgefüllte Bauwerk ABCS (A oben links, B unten links, C und S auf der y-Achse, S über C), dessen Oberkante h von A nach S fällt; rechts der y-Achse der schraffierte Aufsprunghang g, der in C waagerecht beginnt, über den Punkt K steil abfällt, im Punkt U auf der x-Achse sein Minimum hat und bis zum Punkt P wieder leicht ansteigt.",
    kontext="Skisprunganlage",
    textumfang="mittel",
    gegeben="Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m; der Hang beginnt am Punkt C(0 | 50). Der Punkt U liegt an der tiefsten Stelle des Aufsprunghangs.",
    gesucht="Lage und Art aller lokalen Extrempunkte des Graphen von g; Entscheidung, welcher Extrempunkt dem Punkt U entspricht; mittlere Steigung des Aufsprunghangs zwischen C und U",
    verfahren="g′(x) = 1/1000 · (1/500 · x³ − 20x) selbst bilden (oder mit dem CAS), null setzen und x ausklammern: x · (x² − 10 000) = 0 liefert x = −100, x = 0 und x = 100. Mit g″(x) = 1/1000 · (3/500 · x² − 20) die Art bestimmen: g″(0) < 0 Hochpunkt, g″(±100) > 0 je ein Tiefpunkt. Der Aufsprunghang beginnt bei C, liegt also rechts der y-Achse; U ist der Tiefpunkt bei x = 100. Die mittlere Steigung zwischen C(0 | 50) und U(100 | 0) als Differenzenquotient.",
    schritte="7",
    zahlenraum="ganz|negativ|dezimal",
    einheiten="m",
    abhaengig_von="",
    ergebnis="Hochpunkt H(0 | 50), Tiefpunkte T₁(−100 | 0) und T₂(100 | 0); U entspricht T₂(100 | 0). Mittlere Steigung zwischen C und U: (0 − 50)/100 = −0,5.",
    zwischenergebnis="g′(x) = 1/1000 · (1/500 · x³ − 20x)|g″(x) = 1/1000 · (3/500 · x² − 20)|g″(0) = −0,02|g″(±100) = 0,04",
    niveau_geschaetzt="II",
    fehlerquelle="den Tiefpunkt bei x = −100 übersehen, beim Ableiten den Vorfaktor 1/1000 verlieren oder die mittlere Steigung ohne Vorzeichen angeben",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.1c (WTR): das Kontrollergebnis g′(x) = 1/1000 · (1/500 · x³ − 20x) fehlt, die Ableitung wird selbst gebildet (Werkzeug); dazu die mittlere Steigung des Aufsprunghangs zwischen C und U (Auftrag, Nebentyp); 7 statt 6 BE. Typ wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.1d", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="d", seite="2", punkte="3",
    leitidee="Analysis",
    thema="Kurvenuntersuchung",
    typ="Zeitpunkt stärkster Abnahme über das Minimum der Ableitung berechnen",
    typ_neben="",
    stichwoerter="stärkstes Gefälle|Wendestelle|zweite Ableitung|notwendige Bedingung",
    voraussetzungen="zweite Ableitung bilden|quadratische Gleichung lösen|Wurzel im Nenner vereinfachen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Skizze",
    skizze="Profilzeichnung in einem x-y-Koordinatensystem ohne Achsenteilung. Links der y-Achse liegt das grau ausgefüllte Bauwerk ABCS: A oben links auf dem Graphen von h, B senkrecht darunter, C rechts von B, S senkrecht über C auf der y-Achse; die Oberkante von A nach S ist mit h beschriftet und als Anlaufbahn bezeichnet. Rechts der y-Achse fällt der mit g beschriftete Aufsprunghang von C aus bis zum Tiefpunkt U und steigt danach leicht an; auf dem fallenden Ast ist der Punkt K markiert. Die Fläche unter dem Bauwerk und unter dem Aufsprunghang ist schraffiert.",
    kontext="Skisprunganlage",
    textumfang="mittel",
    gegeben="Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000) und g'(x) = 1/1000 · (1/500 · x³ − 20x), 1 LE = 1 m. Der Punkt K ist die Stelle des Aufsprunghangs mit dem stärksten Gefälle; für die x-Koordinate genügt die notwendige Bedingung.",
    gesucht="Koordinaten des Punktes K",
    verfahren="Das stärkste Gefälle liegt dort, wo g' minimal wird, also bei g''(x) = 0. Aus 3/500 · x² − 20 = 0 folgt x² = 10 000/3 und im Bereich des Hangs x = 100/√3 ≈ 57,7. Den zugehörigen Funktionswert durch Einsetzen in g bestimmen.",
    schritte="4",
    zahlenraum="ganz|dezimal|Wurzel",
    einheiten="m",
    abhaengig_von="2018-be-gk-cas-B1.1c",
    ergebnis="K(100/√3 | 200/9), also K ≈ (57,7 | 22,2); das Gefälle beträgt dort g'(K) ≈ −0,77.",
    zwischenergebnis="g''(x) = 1/1000 · (3/500 · x² − 20)|x² = 10 000/3|x ≈ 57,74",
    niveau_geschaetzt="II",
    fehlerquelle="die erste statt der zweiten Ableitung null setzen, oder die negative Lösung x = −57,7 angeben, die nicht auf dem Aufsprunghang liegt",
    bemerkung="Dublette von: 2018-be-gk-B1.1d. CAS-Nachtrag zu 2018-be-gk-B1.1d (WTR): nur BE: 3 statt 4 BE, Wortlaut und Angaben gleich. Die Ableitung g′ ist in der CAS-Fassung nicht vorgegeben, sondern in c selbst gebildet. Felder wie in der WTR-Zeile, Fakten des CAS-Hefts (Seite, BE). Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.1e", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="e", seite="2", punkte="4",
    leitidee="Analysis",
    thema="Tangente, Normale, Schnittwinkel",
    typ="Tangentengleichung in einem Punkt des Graphen aufstellen",
    typ_neben="",
    stichwoerter="knickfreie Fortsetzung|Tangente in P(110 | g(110))|geradlinig|Aufsprunghang",
    voraussetzungen="knickfrei als gleiche Steigung deuten|Ableitung an einer Stelle auswerten|Punkt-Steigungs-Form anwenden",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Term",
    material="Skizze",
    skizze="Profil der Skisprunganlage ohne Achsenteilung: links der y-Achse das dunkel ausgefüllte Bauwerk ABCS (A oben links, B unten links, C und S auf der y-Achse, S über C), dessen Oberkante h von A nach S fällt; rechts der y-Achse der schraffierte Aufsprunghang g, der in C waagerecht beginnt, über den Punkt K steil abfällt, im Punkt U auf der x-Achse sein Minimum hat und bis zum Punkt P wieder leicht ansteigt.",
    kontext="Skisprunganlage",
    textumfang="kurz",
    gegeben="Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m. Im Punkt P(110 | g(110)) soll der Aufsprunghang ohne Knick geradlinig fortgesetzt werden.",
    gesucht="Gleichung der Geraden, die diese Fortsetzung beschreibt",
    verfahren="Ohne Knick geradlinig heißt: die Fortsetzung ist die Tangente an den Graphen von g in P. g(110) und g′(110) berechnen und in die Punkt-Steigungs-Form y = g′(110) · (x − 110) + g(110) einsetzen.",
    schritte="3",
    zahlenraum="dezimal|negativ",
    einheiten="m",
    abhaengig_von="",
    ergebnis="t(x) = 0,462x − 48,615 mit P(110 | 2,205) und der Steigung 0,462.",
    zwischenergebnis="g(110) = 441/200 = 2,205|g′(110) = 231/500 = 0,462",
    niveau_geschaetzt="II",
    fehlerquelle="nur den Punkt P übernehmen und die Steigung vergessen oder die Steigung von h statt von g verwenden",
    bemerkung="CAS-Nachtrag, ohne WTR-Gegenstück: die Teilaufgabe steht nur in der CAS-Fassung (Art ganze Aufgabe, Befund vom 28.09.2026). Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.1f", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="f", seite="3", punkte="11",
    leitidee="Analysis",
    thema="Rekonstruktion von Funktionsgleichungen",
    typ="Funktionsgleichung aus knickfreiem Übergang rekonstruieren",
    typ_neben="Schnittpunkt zweier Graphen über eine biquadratische Gleichung berechnen|Schnittwinkel zweier Graphen im gemeinsamen Punkt über die Tangentensteigungen berechnen",
    stichwoerter="Flugbahn|knickfreier Übergang in S|Landepunkt L|Winkel zwischen Flugbahn und Hang",
    voraussetzungen="allgemeinen Ansatz für eine quadratische Funktion aufstellen|Bedingungen in Gleichungen übersetzen|Gleichung vierten Grades mit dem CAS oder durch Substitution lösen|Steigungswinkel über den Arkustangens berechnen",
    format="Rechnung",
    operator="Bestimmen Sie|Berechnen Sie",
    antwort="Term|Zahl",
    material="Skizze",
    skizze="Profil der Skisprunganlage ohne Achsenteilung: links der y-Achse das dunkel ausgefüllte Bauwerk ABCS (A oben links, B unten links, C und S auf der y-Achse, S über C), dessen Oberkante h von A nach S fällt; rechts der y-Achse der schraffierte Aufsprunghang g, der in C waagerecht beginnt, über den Punkt K steil abfällt, im Punkt U auf der x-Achse sein Minimum hat und bis zum Punkt P wieder leicht ansteigt.",
    kontext="Skisprunganlage",
    textumfang="lang",
    gegeben="Anlaufbahn h mit h(x) = 0,05x² + 54 und Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m. Die Flugbahn des Springers ist eine quadratische Funktion f; im Punkt S(0 | 54) geht die Anlaufbahn ohne Knick in die Flugbahn über. Bei x = 60 m hat der Springer eine vertikale Höhe von 4,72 m über dem Aufsprunghang. Kontrollangabe: f(x) = −0,008x² + 54 und L(73,9 | 10,3).",
    gesucht="Funktionsgleichung der Flugbahn f; Koordinaten des Landepunkts L auf dem Aufsprunghang; Winkel zwischen Flugbahn und Aufsprunghang im Punkt L",
    verfahren="Ansatz f(x) = ax² + bx + c; aus f(0) = h(0) und f′(0) = h′(0) folgen c = 54 und b = 0, aus f(60) − g(60) = 4,72 mit g(60) = 20,48 folgt a = −0,008. Dann f(x) = g(x) mit dem CAS (oder über u = x²) lösen, die positive Lösung nehmen und y berechnen. Den Winkel in L aus den Steigungen f′(x_L) und g′(x_L) über die Steigungswinkel (Differenz) oder die Tangensformel bestimmen.",
    schritte="8",
    zahlenraum="ganz|dezimal|Wurzel|negativ",
    einheiten="m|°",
    abhaengig_von="",
    ergebnis="f(x) = −0,008x² + 54; L(73,9 | 10,3) mit x_L = 20 · √(5 + 5√3) ≈ 73,92; in L haben Flugbahn und Hang die Steigungen −1,183 und −0,671, der Winkel zwischen ihnen beträgt etwa 15,9°.",
    zwischenergebnis="c = 54|b = 0|a = −0,008|x_L ≈ 73,920|y_L ≈ 10,287|Steigungswinkel −49,79° und −33,85°",
    niveau_geschaetzt="II",
    fehlerquelle="die Höhe 4,72 m als Funktionswert f(60) statt als Abstand zum Hang deuten oder den Winkel als Differenz der Steigungen statt der Steigungswinkel berechnen",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.1e (WTR): Zuschnitt und Auftrag – die Flugbahn (WTR e) und der Landepunkt L (WTR f) stehen in einer Teilaufgabe, die Skizze der Flugbahn aus WTR f entfällt, neu ist der Winkel zwischen Flugbahn und Aufsprunghang in L; 11 BE gegen 6 + 10 BE. Der Nachtragsvermerk zeigt auf WTR e (erste Leistung, Haupttyp wie dort); WTR f hat deshalb kein eigenes CAS-Gegenstück, der Landepunkt steht hier als Nebentyp. Kontrollangaben des Hefts durch eigene Rechnung bestätigt. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.1g", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="g", seite="3", punkte="8",
    leitidee="Analysis",
    thema="Gleichungen lösen",
    typ="Intervall, in dem eine Modellfunktion mindestens einen vorgegebenen Wert annimmt, über eine Ungleichung bestimmen",
    typ_neben="Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen",
    stichwoerter="vertikaler Abstand|Differenzfunktion|mindestens 5 m|höchstens 6 m|Sicherheit",
    voraussetzungen="Differenzfunktion aufstellen|Gleichung vierten Grades mit dem CAS lösen|Ableitung null setzen|hinreichende Bedingung prüfen",
    format="Rechnung|Begründung",
    operator="Geben Sie an|Weisen Sie nach",
    antwort="Zahl|Text",
    material="Skizze",
    skizze="Profil der Skisprunganlage ohne Achsenteilung: links der y-Achse das dunkel ausgefüllte Bauwerk ABCS (A oben links, B unten links, C und S auf der y-Achse, S über C), dessen Oberkante h von A nach S fällt; rechts der y-Achse der schraffierte Aufsprunghang g, der in C waagerecht beginnt, über den Punkt K steil abfällt, im Punkt U auf der x-Achse sein Minimum hat und bis zum Punkt P wieder leicht ansteigt.",
    kontext="Skisprunganlage",
    textumfang="mittel",
    gegeben="Flugbahn f mit f(x) = −0,008x² + 54 und Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m; der Sprung führt von S(0 | 54) bis zum Landepunkt L(73,9 | 10,3). Aus Sicherheitsgründen darf der vertikale Abstand des Springers zum Hang nicht zu groß werden.",
    gesucht="Intervall, in dem der vertikale Abstand des Springers zum Aufsprunghang mindestens 5 m beträgt; Nachweis, dass der maximale vertikale Abstand während des Fluges höchstens 6 m beträgt",
    verfahren="Die Differenzfunktion d(x) = f(x) − g(x) = −x⁴/2 000 000 + x²/500 + 4 beschreibt den vertikalen Abstand. d(x) = 5 mit dem CAS lösen und die Lösungen im Flugbereich [0; 73,9] als Intervallgrenzen nehmen. Für das Maximum d′(x) = 0 lösen: x = 0 oder x = 20√5; mit dem Vorzeichenwechsel von d′ oder d″(20√5) < 0 als Maximum sichern, d(20√5) = 6.",
    schritte="6",
    zahlenraum="dezimal|Wurzel",
    einheiten="m",
    abhaengig_von="2018-be-gk-cas-B1.1f",
    ergebnis="Der Abstand beträgt mindestens 5 m für 24,2 ≤ x ≤ 58,4 (genau 10 · √(20 − 10√2) ≤ x ≤ 10 · √(20 + 10√2)). Er ist bei x = 20√5 ≈ 44,7 m maximal und beträgt dort genau 6 m, also während des ganzen Fluges höchstens 6 m.",
    zwischenergebnis="d(x) = −x⁴/2 000 000 + x²/500 + 4|d(x) = 5 bei x ≈ 24,20 und x ≈ 58,43|d′(x) = 0 bei x = 0 und x = 20√5|d(20√5) = 6",
    niveau_geschaetzt="II",
    fehlerquelle="die Lösungen von d(x) = 5 ohne Bezug auf den Flugbereich angeben (auch negative Werte) oder die Randstelle x = 0 mit d(0) = 4 für das Maximum halten",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.1g (WTR): neuer Auftrag – das Intervall, in dem der vertikale Abstand mindestens 5 m beträgt (erste Leistung, Haupttyp); der Nachweis des Maximums wie in der WTR-Fassung, aber ohne den Hinweis, dass auf die hinreichende Bedingung verzichtet werden kann (Werkzeug); 8 statt 6 BE. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.2a", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="a", seite="4", punkte="4",
    leitidee="Analysis",
    thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Nullstelle und Grenzverhalten eines Produkts aus Polynom und e-Funktion angeben",
    typ_neben="",
    stichwoerter="Grenzwert|Exponentialfunktion|Verhalten für x → −∞ und x → ∞|Asymptote",
    voraussetzungen="Wachstumsvergleich von Polynom und Exponentialfunktion kennen|Vorzeichen der Faktoren für x → −∞ beurteilen",
    format="Begründung",
    operator="Untersuchen Sie",
    antwort="Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Funktionen f mit f(x) = (x + 1) · e^(−0,5x) und g mit g(x) = x + 1.",
    gesucht="Verhalten der Funktionswerte von f für x → −∞ und für x → ∞",
    verfahren="Für x → ∞ wächst x + 1 über alle Grenzen, e^(−0,5x) fällt gegen null; die Exponentialfunktion ist stärker, also f(x) → 0. Für x → −∞ geht x + 1 gegen −∞ und e^(−0,5x) gegen +∞, das Produkt also gegen −∞ (mit dem CAS bestätigen).",
    schritte="2",
    zahlenraum="dezimal",
    einheiten="",
    abhaengig_von="",
    ergebnis="Für x → ∞ gilt f(x) → 0 (die x-Achse ist waagerechte Asymptote, Annäherung von oben); für x → −∞ gilt f(x) → −∞.",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="für x → −∞ nur den Faktor e^(−0,5x) betrachten und auf +∞ schließen",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.2a (WTR): Auftrag erweitert – zusätzlich das Verhalten für x → −∞; 4 statt 2 BE. Der Hinweis im Aufgabenstamm auf die Anlage mit den Graphen entfällt (die CAS-Fassung hat keine Anlage; Zwischenstamm gehört zur folgenden Teilaufgabe). Typ wie in der WTR-Zeile. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.2b", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="b", seite="4", punkte="6",
    leitidee="Analysis",
    thema="Gleichungen lösen",
    typ="Schnittpunkte zweier Graphen durch Ausklammern eines gemeinsamen Faktors berechnen",
    typ_neben="Schnittwinkel zwischen Tangente und Gerade über die Anstiege berechnen|Ableitung eines Produkts aus x und einer e-Funktion mit Produkt- und Kettenregel bilden",
    stichwoerter="Schnittpunkte S und T|gemeinsamer Faktor x + 1|Satz vom Nullprodukt|Schnittwinkel in S|ohne Kontrollangabe",
    voraussetzungen="gleichsetzen und einen gemeinsamen Faktor ausklammern|Satz vom Nullprodukt|e^(−0,5x) = 1 lösen|Produkt- und Kettenregel anwenden|Steigungswinkel mit dem Arkustangens bestimmen",
    format="Rechnung",
    operator="Bestimmen Sie|Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="mittel",
    gegeben="Funktionen f mit f(x) = (x + 1) · e^(−0,5x) und g mit g(x) = x + 1. Die Graphen haben einen Schnittpunkt S auf der y-Achse und einen weiteren Schnittpunkt T.",
    gesucht="Koordinaten der Punkte S und T; Winkel, unter dem sich die Tangente an den Graphen von f im Punkt S und die Gerade g schneiden",
    verfahren="f(x) = g(x) umformen zu (x + 1) · (e^(−0,5x) − 1) = 0: x = −1 oder e^(−0,5x) = 1, also x = 0. f′ mit Produkt- und Kettenregel bilden, f′(0) = 0,5 ist der Anstieg der Tangente; g hat den Anstieg 1. Schnittwinkel als Differenz der Steigungswinkel arctan 1 − arctan 0,5 oder über tan φ = |(m₂ − m₁)/(1 + m₁ · m₂)| = 1/3.",
    schritte="5",
    zahlenraum="ganz|dezimal|Bruch|negativ",
    einheiten="",
    abhaengig_von="",
    ergebnis="S(0 | 1), T(−1 | 0); f′(0) = 0,5, der Schnittwinkel in S beträgt φ ≈ 18,4°.",
    zwischenergebnis="(x + 1) · (e^(−0,5x) − 1) = 0|f′(x) = (0,5 − 0,5x) · e^(−0,5x)|tan φ = 1/3",
    niveau_geschaetzt="II",
    fehlerquelle="durch x + 1 teilen und die Lösung x = −1 verlieren oder die Anstiege statt der Steigungswinkel voneinander abziehen",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.2b (WTR): S(0 | 1) ist nicht mehr vorgegeben, dazu ist der zweite Schnittpunkt T zu bestimmen (Auftrag); die Kontrollangabe f′(x) = (−0,5x + 0,5) · e^(−0,5x) fehlt (Werkzeug); der Winkel in S wie in der WTR-Fassung; 6 statt 7 BE. Erste Leistung sind die Schnittpunkte – neuer Typ: der Bestand löst Schnittgleichungen mit e-Funktion nur durch Kürzen eines gemeinsamen Exponentialfaktors, hier wird ein gemeinsamer linearer Faktor ausgeklammert; Schnittwinkel und Ableitung wie in der WTR-Zeile als Nebentypen. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.2c", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="c", seite="4", punkte="4",
    leitidee="Analysis",
    thema="Flächeninhalt durch Integration",
    typ="Fläche: Fläche zwischen zwei Graphen als Integral der Differenz berechnen",
    typ_neben="",
    stichwoerter="eingeschlossene Fläche|zweiter Quadrant|Vergleich mit 1/10|ohne vorgegebene Stammfunktion",
    voraussetzungen="Integrationsgrenzen aus den Schnittstellen gewinnen|Lage der Graphen zueinander bestimmen|bestimmtes Integral einer Differenz mit dem CAS berechnen",
    format="Rechnung|Begründung",
    operator="Untersuchen Sie",
    antwort="Zahl|Text",
    material="keins",
    skizze="keine",
    kontext="ohne",
    textumfang="kurz",
    gegeben="Funktionen f mit f(x) = (x + 1) · e^(−0,5x) und g mit g(x) = x + 1. Die Schnittpunkte sind T(−1 | 0) und S(0 | 1). Die Graphen schließen im zweiten Quadranten eine Fläche mit dem Inhalt A vollständig ein.",
    gesucht="Entscheidung, ob der Inhalt A größer als 1/10 ist",
    verfahren="Die Fläche liegt zwischen x = −1 und x = 0; dort verläuft f oberhalb von g (e^(−0,5x) > 1 für x < 0). A als Integral von −1 bis 0 über f(x) − g(x) mit dem CAS berechnen und mit 0,1 vergleichen.",
    schritte="3",
    zahlenraum="dezimal|Bruch|Wurzel|negativ",
    einheiten="",
    abhaengig_von="2018-be-gk-cas-B1.2b",
    ergebnis="A = 4√e − 6,5 ≈ 0,0949 < 1/10; der Inhalt ist nicht größer als 1/10.",
    zwischenergebnis="∫ von −1 bis 0 über f(x) dx = 4√e − 6 ≈ 0,5949|∫ von −1 bis 0 über g(x) dx = 0,5",
    niveau_geschaetzt="II",
    fehlerquelle="g oberhalb von f annehmen und einen negativen Wert erhalten oder auf 0,1 runden und A = 1/10 schließen",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.2c (WTR): die Stammfunktion F(x) = (−2x − 6) · e^(−0,5x) ist weder vorgegeben noch nachzuweisen, der Nachweis der gemeinsamen Nullstelle entfällt (Werkzeug); statt A zu berechnen ist zu entscheiden, ob A größer als 1/10 ist (Auftrag); 4 statt 9 BE. Deshalb ein anderer Haupttyp als in der WTR-Zeile (dort der Nachweis der Stammfunktion, die Fläche Nebentyp). Der Wert liegt knapp unter der Schranke. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.2d", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="d", seite="4", punkte="4",
    leitidee="Analysis",
    thema="Kurvenuntersuchung",
    typ="Extrempunkt eines Produkts aus Polynom und e-Funktion berechnen",
    typ_neben="",
    stichwoerter="höchster Punkt|notwendige und hinreichende Bedingung|Wanderweg|Ableitung null setzen",
    voraussetzungen="Ableitung eines Produkts bilden|Satz vom Nullprodukt|Funktionswert berechnen|Vorzeichenwechsel der Ableitung oder zweite Ableitung prüfen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="Diagramm",
    skizze="Höhenprofil eines Wanderwegs als Flächendiagramm: eine von 0 ausgehende Kurve, die kurz nach dem Start ein flaches Maximum erreicht und danach bis zum rechten Rand fällt; die Fläche darunter ist grau. Beschriftet sind Höhe y, Entfernung x, Start links, Ziel rechts, die Überschrift Wanderung auf dem Maximiliansweg und die x-Werte 0 und 5. Keine Achsenteilung an der Höhenachse.",
    kontext="Wanderweg / Höhenprofil",
    textumfang="mittel",
    gegeben="Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x) für 0 ≤ x ≤ 6, 1 LE = 1 km. Aus b ist f′(x) = (0,5 − 0,5x) · e^(−0,5x) bekannt.",
    gesucht="Koordinaten des höchsten Punktes des Höhenprofils",
    verfahren="f'(x) = 0 setzen; da e^(−0,5x) stets positiv ist, bleibt 0,5 − 0,5x = 0, also x = 1. Den Funktionswert f(1) = 2 · e^(−0,5) berechnen. Dass es ein Maximum ist, zeigt der Vorzeichenwechsel von f′ von plus nach minus bei x = 1 oder f″(1) < 0.",
    schritte="4",
    zahlenraum="dezimal",
    einheiten="km",
    abhaengig_von="2018-be-gk-cas-B1.2b",
    ergebnis="Höchster Punkt (1 | 2 · e^(−0,5)) ≈ (1 | 1,21), also 1 km nach dem Start in etwa 1,21 km Höhe. f″(1) = −0,5 · e^(−0,5) < 0 bestätigt das Maximum.",
    zwischenergebnis="0,5 − 0,5x = 0|x = 1|f(1) = 2 · e^(−0,5)|f″(x) = 0,25 · (x − 3) · e^(−0,5x)",
    niveau_geschaetzt="II",
    fehlerquelle="den Exponentialfaktor als möglichen Nullfaktor behandeln und eine zweite Lösung angeben",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.2d (WTR): der Hinweis, dass die hinreichende Bedingung nicht untersucht werden muss, entfällt (Werkzeug); BE gleich (4). Typ und Ergebnis wie in der WTR-Zeile, dazu der Nachweis des Maximums. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.2e", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="e", seite="4", punkte="4",
    leitidee="Analysis",
    thema="Ableitung und Änderungsrate",
    typ="Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen",
    typ_neben="Intervall, in dem eine Modellfunktion mindestens einen vorgegebenen Wert annimmt, über eine Ungleichung bestimmen",
    stichwoerter="kleinste Steigung|Minimum der Ableitung|Randwerte|Intervall mit f′(x) ≤ −0,2|vier Nachkommastellen",
    voraussetzungen="zweite Ableitung bilden|Extremstelle der Ableitung mit den Randwerten vergleichen|Gleichung f′(x) = −0,2 mit dem CAS lösen",
    format="Rechnung",
    operator="Berechnen Sie|Ermitteln Sie",
    antwort="Zahl",
    material="Diagramm",
    skizze="Höhenprofil eines Wanderwegs als Flächendiagramm: eine von 0 ausgehende Kurve, die kurz nach dem Start ein flaches Maximum erreicht und danach bis zum rechten Rand fällt; die Fläche darunter ist grau. Beschriftet sind Höhe y, Entfernung x, Start links, Ziel rechts, die Überschrift Wanderung auf dem Maximiliansweg und die x-Werte 0 und 5. Keine Achsenteilung an der Höhenachse.",
    kontext="Wanderweg / Höhenprofil",
    textumfang="mittel",
    gegeben="Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x) für 0 ≤ x ≤ 6, 1 LE = 1 km. Aus b ist f′(x) = (0,5 − 0,5x) · e^(−0,5x) bekannt.",
    gesucht="kleinster Wert, den die Steigung des Höhenprofils annehmen kann; möglichst großes Intervall [x₁; x₂] mit auf vier Nachkommastellen gerundeten Grenzen, in dem f′(x) ≤ −0,2 gilt",
    verfahren="f″(x) = 0,25 · (x − 3) · e^(−0,5x) = 0 liefert x = 3; f′ fällt bis 3 und steigt danach, die Randwerte f′(0) = 0,5 und f′(6) ≈ −0,124 sind größer, also ist f′(3) der kleinste Wert. Für das Intervall f′(x) = −0,2 mit dem CAS lösen; die beiden Lösungen um x = 3 sind die Grenzen, dazwischen gilt f′(x) ≤ −0,2.",
    schritte="5",
    zahlenraum="dezimal|negativ",
    einheiten="km",
    abhaengig_von="2018-be-gk-cas-B1.2b",
    ergebnis="Kleinste Steigung f′(3) = −e^(−1,5) ≈ −0,2231. f′(x) ≤ −0,2 im Intervall [2,2042; 4,0869].",
    zwischenergebnis="f″(x) = 0,25 · (x − 3) · e^(−0,5x)|f′(6) ≈ −0,1245|f′(x) = −0,2 bei x ≈ 2,20418 und x ≈ 4,08695",
    niveau_geschaetzt="II",
    fehlerquelle="die kleinste Steigung mit dem kleinsten Funktionswert verwechseln oder die Randwerte des Intervalls [0; 6] nicht prüfen",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.2f (WTR): andere Frage (Art ganze Aufgabe) – berechnet werden die kleinste Steigung und das größte Intervall mit f′(x) ≤ −0,2, statt nachzuweisen, dass es in [2; 6] eine Stelle mit Steigung unter −0,222 gibt; 4 statt 5 BE; im Heft Teilaufgabe e statt f. Typ wie in der WTR-Zeile, das Intervall als Nebentyp (Ungleichung über die Randstellen, hier für die Ableitung). Die auf vier Stellen gerundeten Grenzen 2,2042 und 4,0869 liegen innerhalb des exakten Intervalls. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.2f", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="f", seite="4", punkte="4",
    leitidee="Analysis",
    thema="Ableitung und Änderungsrate",
    typ="Sekantengleichung durch zwei Punkte eines Graphen ermitteln",
    typ_neben="",
    stichwoerter="Sekante|Geradengleichung|zwei Punkte|Näherung|Kontrollangabe",
    voraussetzungen="Funktionswerte berechnen|Anstieg aus zwei Punkten bestimmen|Punkt-Steigungs-Form anwenden",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Term",
    material="Diagramm",
    skizze="Höhenprofil eines Wanderwegs als Flächendiagramm: eine von 0 ausgehende Kurve, die kurz nach dem Start ein flaches Maximum erreicht und danach bis zum rechten Rand fällt; die Fläche darunter ist grau. Beschriftet sind Höhe y, Entfernung x, Start links, Ziel rechts, die Überschrift Wanderung auf dem Maximiliansweg und die x-Werte 0 und 5. Keine Achsenteilung an der Höhenachse.",
    kontext="Wanderweg / Höhenprofil",
    textumfang="kurz",
    gegeben="Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x) für 0 ≤ x ≤ 6, 1 LE = 1 km. Im Intervall [2 ; 6] soll das Profil näherungsweise durch die Gerade s durch die Punkte (2 | f(2)) und (6 | f(6)) ersetzt werden. Kontrollangabe: mit Rundungen s(x) = −0,19x + 1,48.",
    gesucht="Gleichung der Geraden s",
    verfahren="f(2) = 3 · e^(−1) ≈ 1,104 und f(6) = 7 · e^(−3) ≈ 0,349 berechnen, daraus den Anstieg m = (f(6) − f(2))/4 ≈ −0,189 bilden und die Gerade in der Punkt-Steigungs-Form y = m · (x − 2) + f(2) aufstellen.",
    schritte="4",
    zahlenraum="dezimal|negativ",
    einheiten="km",
    abhaengig_von="",
    ergebnis="m ≈ −0,1888 und s(x) ≈ −0,189x + 1,481, gerundet s(x) = −0,19x + 1,48 wie die Kontrollangabe.",
    zwischenergebnis="f(2) = 3 · e^(−1) ≈ 1,1036|f(6) = 7 · e^(−3) ≈ 0,3485",
    niveau_geschaetzt="I",
    fehlerquelle="den Anstieg durch die Differenz der Funktionswerte ohne Division durch die Intervalllänge 4 bestimmen",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.2e (WTR): die Kontrollangabe s(x) = −0,19x + 1,48 kommt dazu (Werkzeug), die Gerade heißt s; BE gleich (4); im Heft Teilaufgabe f statt e. Typ und Ergebnis wie in der WTR-Zeile; Kontrollangabe durch eigene Rechnung bestätigt. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.2g", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="g", seite="5", punkte="5",
    leitidee="Analysis",
    thema="Extremalprobleme",
    typ="Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen",
    typ_neben="",
    stichwoerter="vertikaler Abstand|Sekante oberhalb des Graphen|Differenzfunktion|Intervall [2; 6]",
    voraussetzungen="Differenzfunktion aufstellen|Nullstelle der Ableitung mit dem CAS bestimmen|Randwerte vergleichen",
    format="Rechnung",
    operator="Ermitteln Sie",
    antwort="Zahl",
    material="Diagramm",
    skizze="Höhenprofil eines Wanderwegs als Flächendiagramm: eine von 0 ausgehende Kurve, die kurz nach dem Start ein flaches Maximum erreicht und danach bis zum rechten Rand fällt; die Fläche darunter ist grau. Beschriftet sind Höhe y, Entfernung x, Start links, Ziel rechts, die Überschrift Wanderung auf dem Maximiliansweg und die x-Werte 0 und 5. Keine Achsenteilung an der Höhenachse.",
    kontext="Wanderweg / Höhenprofil",
    textumfang="kurz",
    gegeben="Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x) für 0 ≤ x ≤ 6, 1 LE = 1 km. Im Intervall [2; 6] wird es durch die Gerade s durch (2 | f(2)) und (6 | f(6)) ersetzt, mit Rundungen s(x) = −0,19x + 1,48. Die Gerade s liegt stets oberhalb des Graphen von f.",
    gesucht="maximaler vertikaler Abstand zwischen den Graphen im Intervall [2; 6]",
    verfahren="Differenzfunktion d(x) = s(x) − f(x) bilden, d′(x) = 0 mit dem CAS lösen und d dort berechnen; an den Rändern ist d(2) = d(6) = 0 (Sekante).",
    schritte="3",
    zahlenraum="dezimal",
    einheiten="km|m",
    abhaengig_von="2018-be-gk-cas-B1.2f",
    ergebnis="Mit der exakten Sekante ist der Abstand bei x ≈ 4,39 maximal und beträgt etwa 0,052 km, also rund 52 m; mit der gerundeten Gleichung s(x) = −0,19x + 1,48 ergeben sich x ≈ 4,36 und etwa 0,046 km.",
    zwischenergebnis="d′(x) = 0 bei x ≈ 4,389|d(4,389) ≈ 0,0522|mit gerundetem s: x ≈ 4,358, d ≈ 0,0457",
    niveau_geschaetzt="II",
    fehlerquelle="den Abstand nur an den Rändern oder an einer geschätzten Stelle berechnen oder die Einheit km nicht deuten",
    bemerkung="CAS-Nachtrag, ohne WTR-Gegenstück: die Teilaufgabe steht nur in der CAS-Fassung (Art ganze Aufgabe, Befund vom 28.09.2026); die CAS-Teilaufgabe h entspricht der WTR-Teilaufgabe g. Welche Gerade gemeint ist (exakte Sekante oder die gerundete Kontrollangabe), sagt das Heft nicht; beide Werte stehen im Ergebnis. Die gerundete Gerade liegt bei x = 2 knapp unter dem Graphen, „stets oberhalb“ gilt streng nur für die exakte Sekante. Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B1.2h", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="h", seite="5", punkte="9",
    leitidee="Analysis",
    thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsraten zweier Modelle vergleichen",
    typ_neben="Parameter einer Exponentialfunktion aus zwei Punkten des Graphen bestimmen|Einzige Stelle gleicher Steigung zweier Graphen mit dem Rechner bestimmen",
    stichwoerter="mittlere Steigung|Vergleich|Parameter bestimmen|Logarithmieren|Stelle gleicher Steigung|genau eine positive Lösung",
    voraussetzungen="mittlere Änderungsrate als Differenzenquotient bilden|Beträge vergleichen|Exponentialgleichung durch Logarithmieren lösen|Gleichung f′(x) = h_W′(x) mit dem CAS lösen und die Lösungsanzahl begründen",
    format="Rechnung|Begründung",
    operator="Untersuchen Sie|Ermitteln Sie|Weisen Sie nach|Geben Sie an",
    antwort="Zahl|Term|Text",
    material="Tabelle",
    skizze="Kleine Wertetabelle mit zwei Spalten: x in km mit den Werten 0 und 6, darunter die Höhe h_W(x) in km mit den Werten 1,2 und 0,3.",
    kontext="Wanderweg / Höhenprofil",
    textumfang="lang",
    gegeben="Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x), 1 LE = 1 km. Ähnliche Profile werden durch h(x) = (x + a) · e^(b · x) mit a > 0 und b < 0 beschrieben. Von einem Profil h_W ist bekannt: h_W(0) = 1,2 km und h_W(6) = 0,3 km.",
    gesucht="Vergleich der Beträge der mittleren Steigungen von f und h_W im Intervall [0 ; 6]; Werte von a und b für h_W; Nachweis, dass es genau eine positive Stelle gibt, an der die Steigungen von f und h_W gleich sind, und diese Steigung",
    verfahren="Mittlere Steigung als Differenzenquotient: bei f ist (f(6) − f(0))/6 = (7 · e^(−3) − 1)/6 ≈ −0,109, bei h_W ist (0,3 − 1,2)/6 = −0,15; der Betrag ist bei h_W größer. Für die Parameter aus h_W(0) = a = 1,2 und aus (6 + 1,2) · e^(6b) = 0,3 die Gleichung e^(6b) = 1/24 durch Logarithmieren lösen. Dann h_W′(x) = (1 + b · (x + 1,2)) · e^(bx) bilden und f′(x) = h_W′(x) mit dem CAS lösen; für x > 0 gibt es genau eine Lösung – die Differenz f′ − h_W′ wechselt dort einmal das Vorzeichen von plus nach minus und nähert sich danach von unten der Null, weil e^(bx) mit b ≈ −0,53 schneller abklingt als e^(−0,5x).",
    schritte="8",
    zahlenraum="dezimal|negativ|Bruch",
    einheiten="km",
    abhaengig_von="",
    ergebnis="Die mittlere Steigung beträgt bei f etwa −0,109, bei h_W −0,15; der Betrag ist bei h_W größer. Für h_W gilt a = 1,2 und b = −ln 24 / 6 ≈ −0,53. Die Steigungen sind nur an der Stelle x ≈ 4,68 gleich; die gemeinsame Steigung beträgt dort etwa −0,177.",
    zwischenergebnis="f(0) = 1|f(6) = 7 · e^(−3) ≈ 0,3485|a = 1,2|e^(6b) = 1/24|x ≈ 4,6833|f′(4,6833) ≈ −0,1771",
    niveau_geschaetzt="III",
    fehlerquelle="die Beträge der negativen Steigungen falsch herum vergleichen, oder beim Logarithmieren den Faktor 6 im Exponenten vergessen, oder die Eindeutigkeit nur mit einer einzigen Rechnerlösung begründen, ohne das Verhalten für große x zu betrachten",
    bemerkung="CAS-Nachtrag zu 2018-be-gk-B1.2g (WTR): Auftrag erweitert – dazu der Nachweis, dass es genau eine positive Stelle mit gleicher Steigung von f und h_W gibt, und die Angabe dieser Steigung; BE gleich (9); im Heft Teilaufgabe h statt g. Typ wie in der WTR-Zeile, der neue Auftrag als neuer Nebentyp (der Bestand weist gleiche Ableitungswerte nur an vorgegebenen Stellen nach). Die Eindeutigkeit am Vorzeichen der Differenz f′ − h_W′ geprüft (genau ein Vorzeichenwechsel auf (0; 1000], danach überwiegt der Faktor e^(−0,5x)). Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B3.1b", block="B", aufgabe="3.1", titel="Gewinnspiel", teilaufgabe="b", seite="9", punkte="5",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Einzelwahrscheinlichkeit der Binomialverteilung mit dem Rechner ermitteln",
    typ_neben="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    stichwoerter="Bernoulli-Kette|genau vier Treffer|erstes Spiel gewonnen|mindestens vier weitere Treffer",
    voraussetzungen="Binomialformel anwenden|Unabhängigkeit aufeinanderfolgender Spiele nutzen|Ereignis in zwei unabhängige Teile zerlegen",
    format="Rechnung",
    operator="Berechnen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Gewinnspiel auf einem Schulfest",
    textumfang="kurz",
    gegeben="Ein Spieler spielt das Spiel mit der Gewinnwahrscheinlichkeit p = 0,4 zehnmal; nach jedem Spiel werden die Kugeln zurückgelegt. Ereignis A: genau 4 der 10 Spiele gewonnen. Ereignis B: das erste Spiel gewonnen und von den übrigen 9 noch mindestens vier.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="A mit der Binomialformel für n = 10, p = 0,4 und k = 4 berechnen. B in zwei unabhängige Teile zerlegen: das erste Spiel gewinnen mit 0,4, und von den übrigen 9 Spielen mindestens vier gewinnen, also P(Y ≥ 4) = 1 − P(Y ≤ 3) mit n = 9 (kumuliert, mit dem Rechner); die beiden Wahrscheinlichkeiten multiplizieren.",
    schritte="5",
    zahlenraum="dezimal|Potenz",
    einheiten="",
    abhaengig_von="2018-be-gk-B3.1a",
    ergebnis="P(A) ≈ 0,2508; P(B) = 0,4 · P(Y ≥ 4) ≈ 0,4 · 0,5174 ≈ 0,2070.",
    zwischenergebnis="P(A) = 210 · 0,4⁴ · 0,6⁶|P(mindestens 4 von 9) = 1 − P(Y ≤ 3) ≈ 0,5174",
    niveau_geschaetzt="II",
    fehlerquelle="bei B mit n = 10 statt mit n = 9 für den zweiten Teil rechnen oder mindestens vier als mehr als vier lesen",
    bemerkung="Dublette von: 2018-be-gk-B3.1b. CAS-Nachtrag zu 2018-be-gk-B3.1b (WTR): nur Zahl: Ereignis B mit „von den übrigen 9 noch mindestens vier“ statt „höchstens eins“; BE gleich (5); Ergebnis neu gerechnet. Felder wie in der WTR-Zeile, Fakten des CAS-Hefts (Seite, BE, Angaben und Ergebnis). Eigene Rechnung, mit sympy bestätigt.")
row(id="2018-be-gk-cas-B3.2a", block="B", aufgabe="3.2", titel="Bildschirme", teilaufgabe="a", seite="10", punkte="4",
    afb_amtlich="I",
    leitidee="Stochastik",
    thema="Binomialverteilung",
    typ="Kumulierte Binomialwahrscheinlichkeit mit dem Rechner ermitteln",
    typ_neben="",
    stichwoerter="Binomialverteilung|höchstens acht von 50|mehr als 30 und weniger als 50 von 200|kumulierte Wahrscheinlichkeit|Rechner",
    voraussetzungen="Ereignis in kumulierte Wahrscheinlichkeiten übersetzen|Grenzen richtig einschließen|kumulierte Binomialwahrscheinlichkeiten mit dem Rechner berechnen",
    format="Rechnung",
    operator="Bestimmen Sie",
    antwort="Zahl",
    material="keins",
    skizze="keine",
    kontext="Bildschirmproduktion",
    textumfang="mittel",
    gegeben="Im Mittel ist einer von fünf Bildschirmen fehlerhaft, die Anzahl fehlerhafter Geräte unter zufällig ausgewählten ist binomialverteilt mit p = 0,2. Ereignis A: von 50 zufällig ausgewählten Bildschirmen sind höchstens 8 fehlerhaft. Ereignis B: von 200 zufällig ausgewählten Bildschirmen sind mehr als 30 und weniger als 50 fehlerhaft.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="A ist P(X ≤ 8) mit n = 50; B ist P(31 ≤ Y ≤ 49) = P(Y ≤ 49) − P(Y ≤ 30) mit n = 200; beide kumulierten Werte mit dem Rechner.",
    schritte="3",
    zahlenraum="dezimal|Prozent",
    einheiten="",
    abhaengig_von="",
    ergebnis="P(A) ≈ 30,7 %; P(B) = P(30 < Y < 50) ≈ 90,8 % (amtlich)",
    zwischenergebnis="P(X ≤ 8) ≈ 0,3073|P(31 ≤ Y ≤ 49) ≈ 0,9076",
    niveau_geschaetzt="I",
    fehlerquelle="bei mehr als 30 und weniger als 50 die Grenzen einschließen und P(Y ≤ 50) − P(Y ≤ 30) oder P(Y ≤ 49) − P(Y ≤ 29) rechnen",
    bemerkung="Dublette von: 2018MgrundlegendBStochastikWTR2-1a. CAS-Nachtrag zu 2018-be-gk-B3.2a (WTR): nur Zahl – Ereignis B mit 200 statt 50 Bildschirmen (mehr als 30 und weniger als 50 statt mehr als 10 und weniger als 15); die CAS-Fassung hat keine Anlage, die Werte liefert der Rechner. AB amtlich: I. Wortgleich mit der Poolaufgabe (Teilaufgabe 1 a, gleiche BE; im Heft „Bestimmen Sie“ statt „Berechnen Sie“ und die Ereignisse ohne Anführungszeichen, redaktionell): die Berliner CAS-Fassung übernimmt die Poolfassung (WTR-Datei), die WTR-Fassung des Landes hat B abgewandelt. Deshalb der Poolverweis statt des Verweises auf die WTR-Zeile (abi.md § 7, Pool-Teilaufgaben in Landesheften). Schätzung nach dem amtlichen Bereich der Poolzeile (Vorrang des Amtlichen, Kern § 5): I; die WTR-Zeile schätzt II. Ergebnis aus der Poolzeile übernommen (dort amtlich); Eigene Rechnung bestätigt es, mit sympy (0,3073; 0,9076).")

NEUE_TYPEN = [
    ("Schnittpunkte zweier Graphen durch Ausklammern eines gemeinsamen Faktors berechnen", "Analysis", "Gleichungen lösen",
     "Die Gleichung f(x) = g(x) so umformen, dass ein beiden Termen gemeinsamer Faktor (etwa x + 1) ausgeklammert wird, mit dem Satz vom Nullprodukt alle Schnittstellen bestimmen (dabei nicht durch den Faktor teilen) und die Schnittpunkte angeben.",
     "2018-be-gk-cas-B1.2b"),
    ("Einzige Stelle gleicher Steigung zweier Graphen mit dem Rechner bestimmen", "Analysis", "Ableitung und Änderungsrate",
     "Die Gleichung f′(x) = g′(x) für zwei Funktionen aufstellen, mit dem Rechner lösen und begründen, dass es im betrachteten Bereich genau eine Lösung gibt (Vorzeichen der Differenz der Ableitungen, Verhalten für große x); die gemeinsame Steigung angeben.",
     "2018-be-gk-cas-B1.2h"),
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
