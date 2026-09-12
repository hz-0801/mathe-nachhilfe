# -*- coding: utf-8 -*-
"""abi-bau.py – Gerüst für die Erfassung eines Hefts im Profil abi.
Version 0.2 · 12.09.2026 · gilt mit katalog-prompt.md v0.3 und abi.md v0.4

Je Heft werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Alles darunter
bleibt unverändert.

Unterschied zu fhr-bau.py: Das Skript hält keine Kopie der zulässigen Werte.
Kopfzeile und Formvokabular liest es aus katalog-prompt.md Abschnitt 5, die
Sachgebiete und die Themenliste aus abi.md Abschnitt 5 und 6. Beide Dateien
müssen neben dem Skript liegen. Eine Kopie im Skript prüft nur, ob das Skript
mit sich selbst übereinstimmt.

Ablauf:
  1. abi.md, katalog-prompt.md, abi-katalog.csv und abi-typen.csv neben dieses
     Skript legen (aus dem Repo, mit geprüftem SHA).
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen.
  3. python3 abi-bau.py – schreibt beide CSV-Dateien, gibt Prüftabelle und
     Bericht aus. Bei einem Fehler wird nichts geschrieben.
  4. Ist ZEILEN leer, läuft nur die Selbstprüfung: Vokabular parsen und die
     vorhandenen Katalogzeilen dagegen prüfen. Nichts wird geschrieben.

Änderungen gegenüber 0.1: Der Umschrift-Assert blendet die Feldnamen des Schemas
aus, damit ein Feldname im Fließtext einer bemerkung nicht anschlägt. Neu ist die
Umschrift-Liste am Ende des Berichts – jedes Wort mit ss, ae, oe oder ue zur
Sichtprüfung. Sie ist kein Assert: die Positivliste UMSCHRIFT findet nur, was in
ihr steht, die Liste zeigt alles.
"""
import csv, io, os, re, sys

# ===================================================================== KONFIG
KONFIG = {
    "jahr": "2018",
    "papier": "2018-be-gk",
    "datei": "18_Ma_GK_Aufgaben.pdf",
    "seiten": 11,
    # Sollpunkte je Aufgabe aus der BE-Tabelle am Ende jeder Aufgabe. Das Heft
    # hat keinen hilfsmittelfreien Teil, deshalb kein soll_teil1.
    "soll": {"1.1": 40, "1.2": 40, "2.1": 20, "2.2": 20, "3.1": 20, "3.2": 20},
    # Kein soll_gesamt: das Heft enthält Wahlaufgaben, die Summe aller
    # erfassten Zeilen ist deshalb größer als die 80 BE der Prüfung.
}

# ========================================= QUELLEN UND PRÜFUNG, NICHT ÄNDERN
KAT = "abi-katalog.csv"
TYP = "abi-typen.csv"
PROFIL = "abi.md"
KERN = "katalog-prompt.md"
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]

PFLICHT = ("id jahr papier block aufgabe titel teilaufgabe seite punkte hilfsmittel leitidee "
           "thema typ format operator antwort material skizze kontext textumfang gegeben gesucht "
           "verfahren schritte ergebnis niveau_geschaetzt fehlerquelle").split()

# Stämme, die eine ASCII-Umschrift von ä, ö, ü oder ß verraten. Positivliste,
# weil ein Mustertest auf ae|oe|ue|ss bei Koeffizient oder Quader fehlschlägt.
UMSCHRIFT = ("flaeche", "laenge", "naechst", "haeufig", "zufaell", "waehl", "aender", "aeusser",
 "gefaess", "verhaeltnis", "erklaer", "zaehl", "traeg", "gaeng", "maessig", "hoehe", "groesse",
 "groess", "loesung", "loes", "moegl", "koerper", "oeffn", "schoen", "pruef", "stueck",
 "kruemmung", "ueber", "fuer", "muess", "fuehr", "gueltig", "zurueck", "huelle", "schluessel",
 "urspruengl", "gross", "massstab", "masszahl", "schliess", "heisst", "weiss", "strasse",
 "gemaess", "fuss", "flaechen", "abstaend", "schaerfe", "raeum", "waehrend", "naeher",
 "gegenueber", "unabhaeng", "abhaeng", "zulaessig", "moeglich", "hoeher")
# Felder, die bewusst umlautfrei sind: Dateinamen und papier-Kürzel (abi.md § 4).
OHNE_UMLAUT = ("id", "papier", "abhaengig_von")


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


HEAD, VOK, LEITIDEEN, THEMEN = vokabular()

# ======================================================== AB HIER JE HEFT
ZEILEN = []


def row(**kw):
    z = {k: "" for k in HEAD}
    z.update(jahr=KONFIG["jahr"], papier=KONFIG["papier"], stern="", afb_amtlich="")
    unbekannt = set(kw) - set(HEAD)
    if unbekannt:
        sys.exit(f"unbekanntes Feld: {sorted(unbekannt)}")
    z.update(kw)
    if not z["hilfsmittel"]:
        z["hilfsmittel"] = "nein" if z["block"] == "A" else "ja"
    ZEILEN.append(z)


# ============================================================ ZEILEN JE HEFT
# Ein Eintrag je Teilaufgabe. Nicht genannte Felder bleiben leer; jahr, papier,
# stern, afb_amtlich und hilfsmittel setzt row() selbst.
# Heft 2018-be-gk: kein hilfsmittelfreier Teil, alle Zeilen block B.
# Vorlage:
#   row(id="2018-be-gk-B1.1a", block="B", aufgabe="1.1", titel="Skisprunganlage",
#       teilaufgabe="a", seite="2", punkte="3",
#       leitidee="Analysis", thema="...", typ="...", typ_neben="",
#       stichwoerter="...|...", voraussetzungen="",
#       format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
#       material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
#       gegeben="...", gesucht="...", verfahren="...", schritte="3",
#       zahlenraum="dezimal", einheiten="", abhaengig_von="",
#       ergebnis="...", zwischenergebnis="",
#       niveau_geschaetzt="II", fehlerquelle="...", bemerkung="Eigene Rechnung.")

SKIZZE_11 = ("Profilzeichnung in einem x-y-Koordinatensystem ohne Achsenteilung. Links der "
             "y-Achse liegt das grau ausgefüllte Bauwerk ABCS: A oben links auf dem Graphen von "
             "h, B senkrecht darunter, C rechts von B, S senkrecht über C auf der y-Achse; die "
             "Oberkante von A nach S ist mit h beschriftet und als Anlaufbahn bezeichnet. Rechts "
             "der y-Achse fällt der mit g beschriftete Aufsprunghang von C aus bis zum "
             "Tiefpunkt U und steigt danach leicht an; auf dem fallenden Ast ist der Punkt K "
             "markiert. Die Fläche unter dem Bauwerk und unter dem Aufsprunghang ist "
             "schraffiert.")

SKIZZE_11KS = ("Vorgegebenes Koordinatensystem mit Gitternetz: x-Achse von −10 bis 120 (in m), "
               "y-Achse von 0 bis über 70 (in m), Rasterweite 10. Eingezeichnet sind der grau "
               "ausgefüllte Querschnitt des Bauwerks zwischen x = −20 und x = 0 mit der Oberkante "
               "h sowie der Graph von g, der bei (0 | 50) beginnt, bei (100 | 0) sein Minimum hat "
               "und danach wieder ansteigt; S ist an der y-Achse beschriftet.")

row(id="2018-be-gk-B1.1a", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="a",
    seite="2", punkte="3",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Vertikalen Abstand zweier Punkte als Differenz von Funktionswerten berechnen",
    typ_neben="Schnittpunkt mit der y-Achse angeben",
    stichwoerter="Skisprunganlage|Funktionswert|Höhenunterschied|Bauwerk",
    voraussetzungen="Funktionswerte einsetzen|Lage der Punkte aus der Abbildung entnehmen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=SKIZZE_11, kontext="Skisprunganlage", textumfang="mittel",
    gegeben="Profil einer Skisprunganlage mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000) für "
            "den Aufsprunghang und h(x) = 0,05x² + 54 für die Anlaufbahn, 1 LE = 1 m. Die "
            "Anlaufbahn ist die Oberseite des Bauwerks ABCS und verläuft von A bis S auf dem "
            "Graphen von h. S und C liegen auf der y-Achse, die Strecke von B nach C ist "
            "waagerecht und 20 m lang.",
    gesucht="Höhenunterschied zwischen S und C; Länge der Strecke von A nach B",
    verfahren="S und C sind die Schnittpunkte der beiden Graphen mit der y-Achse: h(0) = 54 und "
              "g(0) = 50, also liegt S 4 m höher. Da BC waagerecht und 20 m lang ist, hat B die "
              "x-Koordinate −20 und die Höhe von C; A liegt senkrecht darüber auf dem Graphen von "
              "h. Die Länge von AB ist die Differenz h(−20) − 50.",
    schritte="4", zahlenraum="ganz|dezimal|negativ", einheiten="m",
    abhaengig_von="",
    ergebnis="S liegt 4 m höher als C. A(−20 | 74) und B(−20 | 50), also ist die Strecke AB "
             "24 m lang.",
    zwischenergebnis="h(0) = 54|g(0) = 50|h(−20) = 74",
    niveau_geschaetzt="II",
    fehlerquelle="die Länge von AB als Abstand zweier Punkte mit dem Satz des Pythagoras "
                 "berechnen, obwohl die Strecke senkrecht verläuft, oder B bei x = +20 ansetzen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B1.1b", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="b",
    seite="2", punkte="5",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche zwischen zwei Graphen berechnen",
    typ_neben="",
    stichwoerter="Querschnittsfläche|Integral|Bauwerk|Differenzfunktion",
    voraussetzungen="Stammfunktion einer ganzrationalen Funktion bilden|bestimmtes Integral "
                    "berechnen|Integrationsgrenzen aus der Lage der Punkte ablesen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Skizze", skizze=SKIZZE_11, kontext="Skisprunganlage", textumfang="kurz",
    gegeben="Bauwerk ABCS mit A(−20 | 74), B(−20 | 50), C(0 | 50) und S(0 | 54); die Oberseite "
            "von A nach S verläuft auf dem Graphen von h mit h(x) = 0,05x² + 54, 1 LE = 1 m.",
    gesucht="Inhalt der Querschnittsfläche des Bauwerks ABCS",
    verfahren="Die Fläche wird oben vom Graphen von h, unten von der waagerechten Strecke BC auf "
              "der Höhe y = 50 und seitlich von x = −20 und x = 0 begrenzt. Also das Integral der "
              "Differenz h(x) − 50 von −20 bis 0 berechnen.",
    schritte="4", zahlenraum="ganz|dezimal|negativ", einheiten="m|m²",
    abhaengig_von="2018-be-gk-B1.1a",
    ergebnis="A = 640/3 m² ≈ 213,3 m²",
    zwischenergebnis="Integrand h(x) − 50 = 0,05x² + 4|Stammfunktion x³/60 + 4x",
    niveau_geschaetzt="II",
    fehlerquelle="über h statt über h − 50 integrieren und so die Fläche bis zur x-Achse statt "
                 "bis zur Strecke BC berechnen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B1.1c", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="c",
    seite="2", punkte="6",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Lage und Art aller lokalen Extrempunkte bestimmen",
    typ_neben="Extrempunkt einem Punkt im Sachzusammenhang zuordnen",
    stichwoerter="Extrempunkte|notwendige und hinreichende Bedingung|tiefste Stelle|Aufsprunghang",
    voraussetzungen="Ableitungen einer ganzrationalen Funktion bilden|Produkt gleich null "
                    "setzen|Vorzeichen der zweiten Ableitung deuten",
    format="Rechnung|Begründung", operator="Ermitteln Sie|Entscheiden Sie", antwort="Zahl|Text",
    material="Skizze", skizze=SKIZZE_11, kontext="Skisprunganlage", textumfang="mittel",
    gegeben="Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m; der "
            "Hang beginnt am Punkt C(0 | 50). Der Punkt U liegt an der tiefsten Stelle des "
            "Aufsprunghangs. Als Kontrollergebnis ist g'(x) = 1/1000 · (1/500 · x³ − 20x) "
            "angegeben.",
    gesucht="Lage und Art aller lokalen Extrempunkte des Graphen von g; Entscheidung, welcher "
            "Extrempunkt dem Punkt U entspricht",
    verfahren="g'(x) = 0 setzen und x ausklammern: x · (x² − 10 000) = 0 liefert x = −100, x = 0 "
              "und x = 100. Mit der zweiten Ableitung g''(x) = 1/1000 · (3/500 · x² − 20) die Art "
              "bestimmen: g''(0) < 0 ergibt einen Hochpunkt, g''(±100) > 0 je einen Tiefpunkt. Der "
              "Aufsprunghang beginnt bei C, liegt also rechts der y-Achse; U ist der Tiefpunkt "
              "bei x = 100.",
    schritte="6", zahlenraum="ganz|negativ", einheiten="m",
    abhaengig_von="",
    ergebnis="Hochpunkt H(0 | 50), Tiefpunkte T₁(−100 | 0) und T₂(100 | 0). U entspricht "
             "T₂(100 | 0).",
    zwischenergebnis="g''(x) = 1/1000 · (3/500 · x² − 20)|g''(0) = −0,02|g''(±100) = 0,04",
    niveau_geschaetzt="II",
    fehlerquelle="nur die Nullstellen der Ableitung angeben, ohne die Art über die zweite "
                 "Ableitung zu bestimmen, oder den Tiefpunkt bei x = −100 übersehen",
    bemerkung="Das Kontrollergebnis für g' ist durch eigene Rechnung bestätigt. Die Aufgabe fragt "
              "nach allen lokalen Extrempunkten des Graphen, deshalb steht auch der Tiefpunkt bei "
              "x = −100 im Ergebnis, obwohl er außerhalb des Aufsprunghangs liegt. Eigene "
              "Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B1.1d", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="d",
    seite="2", punkte="4",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Stelle des stärksten Gefälles über die zweite Ableitung bestimmen",
    typ_neben="",
    stichwoerter="stärkstes Gefälle|Wendestelle|zweite Ableitung|notwendige Bedingung",
    voraussetzungen="zweite Ableitung bilden|quadratische Gleichung lösen|Wurzel im Nenner "
                    "vereinfachen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Skizze", skizze=SKIZZE_11, kontext="Skisprunganlage", textumfang="mittel",
    gegeben="Aufsprunghang g mit g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000) und "
            "g'(x) = 1/1000 · (1/500 · x³ − 20x), 1 LE = 1 m. Der Punkt K ist die Stelle des "
            "Aufsprunghangs mit dem stärksten Gefälle; für die x-Koordinate genügt die "
            "notwendige Bedingung.",
    gesucht="Koordinaten des Punktes K",
    verfahren="Das stärkste Gefälle liegt dort, wo g' minimal wird, also bei g''(x) = 0. Aus "
              "3/500 · x² − 20 = 0 folgt x² = 10 000/3 und im Bereich des Hangs x = 100/√3 ≈ 57,7. "
              "Den zugehörigen Funktionswert durch Einsetzen in g bestimmen.",
    schritte="4", zahlenraum="ganz|dezimal|Wurzel", einheiten="m",
    abhaengig_von="2018-be-gk-B1.1c",
    ergebnis="K(100/√3 | 200/9), also K ≈ (57,7 | 22,2); das Gefälle beträgt dort "
             "g'(K) ≈ −0,77.",
    zwischenergebnis="g''(x) = 1/1000 · (3/500 · x² − 20)|x² = 10 000/3|x ≈ 57,74",
    niveau_geschaetzt="II",
    fehlerquelle="die erste statt der zweiten Ableitung null setzen, oder die negative Lösung "
                 "x = −57,7 angeben, die nicht auf dem Aufsprunghang liegt",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B1.1e", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="e",
    seite="2", punkte="6",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Quadratische Funktion aus knickfreiem Übergang und einer Wertbedingung rekonstruieren",
    typ_neben="",
    stichwoerter="Flugbahn|knickfreier Übergang|quadratische Funktion|Bedingungen",
    voraussetzungen="allgemeinen Ansatz für eine quadratische Funktion aufstellen|Bedingungen in "
                    "Gleichungen übersetzen|lineare Gleichung lösen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Term",
    material="Skizze", skizze=SKIZZE_11, kontext="Skisprunganlage", textumfang="mittel",
    gegeben="Anlaufbahn h mit h(x) = 0,05x² + 54 und Aufsprunghang g mit "
            "g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m. Die Flugbahn des "
            "Springers ist eine quadratische Funktion f; im Punkt S(0 | 54) geht die Anlaufbahn "
            "ohne Knick in die Flugbahn über. Bei x = 60 m hat der Springer eine vertikale Höhe "
            "von 4,72 m über dem Aufsprunghang. Als Kontrolle ist f(x) = −0,008x² + 54 angegeben.",
    gesucht="Funktionsgleichung der Flugbahn f",
    verfahren="Ansatz f(x) = ax² + bx + c. Knickfreier Übergang in S heißt f(0) = h(0) = 54, also "
              "c = 54, und f'(0) = h'(0) = 0, also b = 0. Die dritte Bedingung ist "
              "f(60) − g(60) = 4,72 mit g(60) = 20,48; daraus 3600a + 54 = 25,2 und a = −0,008.",
    schritte="5", zahlenraum="ganz|dezimal|negativ", einheiten="m",
    abhaengig_von="",
    ergebnis="f(x) = −0,008x² + 54",
    zwischenergebnis="c = 54|b = 0|g(60) = 20,48|f(60) = 25,2",
    niveau_geschaetzt="II",
    fehlerquelle="die Höhe 4,72 m als Funktionswert f(60) statt als Abstand zum Aufsprunghang "
                 "deuten, oder den knickfreien Übergang nur über den Funktionswert und nicht "
                 "über die Steigung ansetzen",
    bemerkung="Das Kontrollergebnis ist durch eigene Rechnung bestätigt. Eigene Rechnung, mit "
              "sympy bestätigt.")

row(id="2018-be-gk-B1.1f", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="f",
    seite="3", punkte="10",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Schnittpunkt zweier Graphen über eine biquadratische Gleichung berechnen",
    typ_neben="Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen",
    stichwoerter="Landepunkt|biquadratische Gleichung|Substitution|Flugbahn einzeichnen",
    voraussetzungen="Gleichung durch Substitution u = x² auf eine quadratische zurückführen|"
                    "quadratische Gleichung lösen|Lösungen auf den Sachzusammenhang prüfen|"
                    "Funktionswerte für eine Wertetabelle berechnen",
    format="Rechnung|Zeichnen", operator="Berechnen Sie|Skizzieren Sie", antwort="Zahl|Grafik",
    material="Koordinatensystem", skizze=SKIZZE_11KS, kontext="Skisprunganlage",
    textumfang="mittel",
    gegeben="Flugbahn f mit f(x) = −0,008x² + 54 und Aufsprunghang g mit "
            "g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m. Der Springer landet im "
            "Punkt L auf dem Aufsprunghang. Ein Koordinatensystem mit beiden Graphen ist "
            "vorgegeben. Als Kontrolle ist L(73,9 | 10,3) angegeben.",
    gesucht="Koordinaten des Landepunktes L; Skizze der Flugbahn im vorgegebenen "
            "Koordinatensystem",
    verfahren="f(x) = g(x) setzen und ordnen: x⁴/2 000 000 − 0,002x² − 4 = 0, also nach "
              "Multiplikation x⁴ − 4000x² − 8 000 000 = 0. Mit u = x² die quadratische Gleichung "
              "u² − 4000u − 8 000 000 = 0 lösen; nur die positive Lösung u = 2000 + 2000√3 ist "
              "brauchbar, daraus x = √u ≈ 73,9 und y = g(73,9) ≈ 10,3. Für die Zeichnung die "
              "nach unten geöffnete Parabel von S(0 | 54) über (60 | 25,2) bis L eintragen.",
    schritte="6", zahlenraum="ganz|dezimal|Wurzel|negativ", einheiten="m",
    abhaengig_von="2018-be-gk-B1.1e",
    ergebnis="u = 2000 + 2000√3 ≈ 5464,1, also L(73,9 | 10,3). Die Flugbahn ist eine nach unten "
             "geöffnete Parabel mit Scheitel S(0 | 54), die durch (40 | 41,2) und (60 | 25,2) "
             "verläuft und im Punkt L auf dem Graphen von g endet.",
    zwischenergebnis="x⁴ − 4000x² − 8 000 000 = 0|u = 2000 + 2000√3|x ≈ 73,92|g(73,92) ≈ 10,29",
    niveau_geschaetzt="II",
    fehlerquelle="beim Rücksubstituieren die negative Wurzel mitnehmen oder die negative Lösung "
                 "für u weiterverwenden, obwohl u = x² nicht negativ sein kann",
    bemerkung="Die Angaben f) und das Koordinatensystem stehen auf derselben Seite 3. Das Feld "
              "skizze beschreibt das vorgegebene Koordinatensystem; die Flugbahn ist einzutragen. "
              "Das Einzeichnen in ein vorgegebenes Koordinatensystem hat in der Themenliste "
              "Analysis kein eigenes Thema, ersatzweise Funktionsklassen und Eigenschaften für "
              "den Nebentyp. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B1.1g", block="B", aufgabe="1.1", titel="Skisprunganlage", teilaufgabe="g",
    seite="3", punkte="6",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen",
    typ_neben="",
    stichwoerter="vertikaler Abstand|Differenzfunktion|Maximum|Sicherheit",
    voraussetzungen="Differenzfunktion aufstellen|ableiten und null setzen|Produkt gleich null "
                    "setzen",
    format="Begründung|Rechnung", operator="Weisen Sie nach", antwort="Text|Zahl",
    material="Koordinatensystem", skizze=SKIZZE_11KS, kontext="Skisprunganlage",
    textumfang="mittel",
    gegeben="Flugbahn f mit f(x) = −0,008x² + 54 und Aufsprunghang g mit "
            "g(x) = 1/1000 · (1/2000 · x⁴ − 10x² + 50 000), 1 LE = 1 m; der Sprung führt von "
            "S(0 | 54) bis zum Landepunkt L(73,9 | 10,3). Auf die hinreichende Bedingung darf "
            "verzichtet werden.",
    gesucht="Nachweis, dass der maximale vertikale Abstand des Springers zum Hang höchstens 6 m "
            "beträgt",
    verfahren="Die Differenzfunktion d(x) = f(x) − g(x) beschreibt den vertikalen Abstand. "
              "d'(x) = 0,004x − x³/500 000 = 0 liefert nach Ausklammern x = 0 und x² = 2000, also "
              "x = 20√5 ≈ 44,7 im Flugbereich. Einsetzen ergibt d(20√5) = 38 − 32 = 6.",
    schritte="5", zahlenraum="ganz|dezimal|Wurzel", einheiten="m",
    abhaengig_von="2018-be-gk-B1.1e",
    ergebnis="Der Abstand ist bei x = 20√5 ≈ 44,7 m maximal und beträgt dort genau 6 m; damit ist "
             "der vertikale Abstand während des ganzen Fluges höchstens 6 m.",
    zwischenergebnis="d(x) = −0,008x² + 4 − x⁴/2 000 000 + 0,01x²|d'(x) = 0,004x − x³/500 000|"
                     "x = 20√5 ≈ 44,72|f(44,72) = 38|g(44,72) = 32",
    niveau_geschaetzt="II",
    fehlerquelle="den Abstand als Abstand Punkt–Kurve senkrecht zum Hang deuten statt als "
                 "vertikale Differenz, oder die Lösung x = 0 der Ableitung als Maximum nehmen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt; das Maximum ist exakt 6 m.")

SKIZZE_12 = ("Höhenprofil eines Wanderwegs als Flächendiagramm: eine von 0 ausgehende Kurve, die "
             "kurz nach dem Start ein flaches Maximum erreicht und danach bis zum rechten Rand "
             "fällt; die Fläche darunter ist grau. Beschriftet sind Höhe y, Entfernung x, Start "
             "links, Ziel rechts, die Überschrift Wanderung auf dem Maximiliansweg und die "
             "x-Werte 0 und 5. Keine Achsenteilung an der Höhenachse.")

SKIZZE_12ANL = ("Anlage: Koordinatensystem mit x von −1 bis 7 und y von 0 bis über 3, Rasterweite "
                "1. Eingezeichnet sind die Gerade g durch (−1 | 0) mit dem Anstieg 1 und der "
                "Graph von f, der ebenfalls bei (−1 | 0) beginnt, oberhalb von g verläuft, bei "
                "x = 1 ein flaches Maximum mit y ≈ 1,2 hat und danach auf die x-Achse zufällt; "
                "beide Graphen sind mit f und g beschriftet.")

row(id="2018-be-gk-B1.2a", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="a",
    seite="4", punkte="2",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Grenzverhalten einer Exponentialfunktion untersuchen",
    typ_neben="",
    stichwoerter="Grenzwert|Exponentialfunktion|Verhalten im Unendlichen|Asymptote",
    voraussetzungen="Wachstumsvergleich von Polynom und Exponentialfunktion kennen",
    format="Begründung", operator="Untersuchen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktion f mit f(x) = (x + 1) · e^(−0,5x).",
    gesucht="Verhalten der Funktionswerte von f für x → +∞",
    verfahren="Der Faktor x + 1 wächst über alle Grenzen, der Faktor e^(−0,5x) fällt gegen null; "
              "die Exponentialfunktion ist dabei stärker, also gehen die Funktionswerte gegen "
              "null.",
    schritte="2", zahlenraum="dezimal", einheiten="",
    abhaengig_von="",
    ergebnis="Für x → +∞ gilt f(x) → 0; die x-Achse ist waagerechte Asymptote, die Annäherung "
             "erfolgt von oben.",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="aus dem Produkt aus wachsendem und fallendem Faktor auf einen unbestimmten "
                 "Grenzwert schließen, statt das stärkere Wachstum der Exponentialfunktion zu "
                 "nutzen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B1.2b", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="b",
    seite="4", punkte="7",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Schnittwinkel zwischen Tangente und Gerade über die Anstiege berechnen",
    typ_neben="Ableitung mit Produkt- und Kettenregel bilden",
    stichwoerter="Schnittwinkel|Tangente|Anstieg|Steigungswinkel",
    voraussetzungen="Produkt- und Kettenregel anwenden|Steigungswinkel mit dem Arkustangens "
                    "bestimmen|Winkeldifferenz bilden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktionen f mit f(x) = (x + 1) · e^(−0,5x) und g mit g(x) = x + 1; beide Graphen "
            "schneiden die y-Achse im Punkt S(0 | 1). Als Kontrolle ist "
            "f'(x) = (−0,5x + 0,5) · e^(−0,5x) angegeben.",
    gesucht="Winkel, unter dem sich die Tangente an den Graphen von f im Punkt S und die Gerade g "
            "schneiden",
    verfahren="f' mit Produkt- und Kettenregel bilden und f'(0) = 0,5 als Anstieg der Tangente "
              "bestimmen; g hat den Anstieg 1. Die beiden Steigungswinkel sind arctan 0,5 ≈ 26,6° "
              "und arctan 1 = 45°, der Schnittwinkel ist ihre Differenz. Gleichwertig über "
              "tan φ = |(m₂ − m₁)/(1 + m₁ · m₂)| = 1/3.",
    schritte="4", zahlenraum="dezimal|Bruch", einheiten="",
    abhaengig_von="",
    ergebnis="f'(0) = 0,5; mit tan φ = 1/3 ergibt sich φ ≈ 18,4°.",
    zwischenergebnis="f'(x) = (0,5 − 0,5x) · e^(−0,5x)|f'(0) = 0,5|arctan 0,5 ≈ 26,57°|"
                     "arctan 1 = 45°",
    niveau_geschaetzt="II",
    fehlerquelle="die Anstiege statt der Steigungswinkel voneinander abziehen, oder beim "
                 "Ableiten die innere Ableitung −0,5 vergessen",
    bemerkung="Das Kontrollergebnis für f' ist durch eigene Rechnung bestätigt. Eigene Rechnung, "
              "mit sympy bestätigt.")

row(id="2018-be-gk-B1.2c", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="c",
    seite="4|5", punkte="9",
    leitidee="Analysis", thema="Stammfunktion und Hauptsatz",
    typ="Stammfunktion durch Ableiten nachweisen",
    typ_neben="Einzige Nullstelle über den positiven Exponentialfaktor nachweisen|"
              "Fläche zwischen zwei Graphen berechnen",
    stichwoerter="Stammfunktion|Nullstelle|eingeschlossene Fläche|zweiter Quadrant",
    voraussetzungen="Produkt- und Kettenregel anwenden|Satz vom Nullprodukt|bestimmtes Integral "
                    "einer Differenz berechnen|Integrationsgrenzen aus den Nullstellen gewinnen",
    format="Begründung|Rechnung", operator="Weisen Sie nach|Zeigen Sie|Berechnen Sie",
    antwort="Text|Zahl",
    material="Koordinatensystem", skizze=SKIZZE_12ANL, kontext="ohne", textumfang="mittel",
    gegeben="Funktionen f mit f(x) = (x + 1) · e^(−0,5x) und g mit g(x) = x + 1 sowie F mit "
            "F(x) = (−2x − 6) · e^(−0,5x). Die Graphen von f und g schließen im zweiten "
            "Quadranten eine Fläche mit dem Inhalt A vollständig ein; die Graphen sind in der "
            "Anlage dargestellt.",
    gesucht="Nachweis, dass F eine Stammfunktion von f ist; Nachweis, dass beide Funktionen nur "
            "bei x = −1 eine Nullstelle haben; Wert von A",
    verfahren="F mit Produkt- und Kettenregel ableiten: F'(x) = −2e^(−0,5x) + (−2x − 6) · (−0,5) "
              "· e^(−0,5x) = (x + 1) · e^(−0,5x) = f(x). Da e^(−0,5x) stets positiv ist, wird f "
              "nur für x + 1 = 0 null; g wird ebenfalls nur bei x = −1 null. Die Fläche liegt "
              "zwischen der gemeinsamen Nullstelle x = −1 und der y-Achse, dort verläuft f "
              "oberhalb von g: A = Integral von −1 bis 0 über f(x) − g(x).",
    schritte="6", zahlenraum="ganz|dezimal|negativ|Wurzel", einheiten="",
    abhaengig_von="",
    ergebnis="F'(x) = (x + 1) · e^(−0,5x) = f(x), also ist F eine Stammfunktion. Beide Funktionen "
             "haben nur bei x = −1 eine Nullstelle. A = 4√e − 6,5 ≈ 0,09 FE.",
    zwischenergebnis="F'(x) = (x + 1) · e^(−0,5x)|F(0) = −6|F(−1) = −4√e ≈ −6,595|Integral über g "
                     "von −1 bis 0 ist 0,5",
    niveau_geschaetzt="II",
    fehlerquelle="die Fläche als Integral über f allein berechnen, oder die Grenzen vertauschen "
                 "und einen negativen Flächeninhalt angeben",
    bemerkung="seite nennt die Aufgabenseite und die Anlage mit den Graphen. Eigene Rechnung, mit "
              "sympy bestätigt.")

row(id="2018-be-gk-B1.2d", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="d",
    seite="4", punkte="4",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Hochpunkt über die notwendige Bedingung bestimmen",
    typ_neben="",
    stichwoerter="höchster Punkt|notwendige Bedingung|Wanderweg|Ableitung null setzen",
    voraussetzungen="Ableitung eines Produkts bilden|Satz vom Nullprodukt|Funktionswert berechnen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Diagramm", skizze=SKIZZE_12, kontext="Wanderweg / Höhenprofil", textumfang="mittel",
    gegeben="Das Höhenprofil eines Wanderwegs wird durch f mit f(x) = (x + 1) · e^(−0,5x) für "
            "0 ≤ x ≤ 6 beschrieben, 1 LE = 1 km; f'(x) = (0,5 − 0,5x) · e^(−0,5x). Die "
            "hinreichende Bedingung muss nicht untersucht werden.",
    gesucht="Koordinaten des höchsten Punktes des Höhenprofils",
    verfahren="f'(x) = 0 setzen; da e^(−0,5x) stets positiv ist, bleibt 0,5 − 0,5x = 0, also "
              "x = 1. Den Funktionswert f(1) = 2 · e^(−0,5) berechnen.",
    schritte="3", zahlenraum="dezimal", einheiten="km",
    abhaengig_von="2018-be-gk-B1.2b",
    ergebnis="Höchster Punkt (1 | 2 · e^(−0,5)) ≈ (1 | 1,21), also 1 km nach dem Start in etwa "
             "1,21 km Höhe.",
    zwischenergebnis="0,5 − 0,5x = 0|x = 1|f(1) = 2 · e^(−0,5)",
    niveau_geschaetzt="II",
    fehlerquelle="den Exponentialfaktor als möglichen Nullfaktor behandeln und eine zweite "
                 "Lösung angeben",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B1.2e", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="e",
    seite="4", punkte="4",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Sekantengleichung durch zwei Punkte eines Graphen ermitteln",
    typ_neben="",
    stichwoerter="Sekante|Geradengleichung|zwei Punkte|Näherung",
    voraussetzungen="Funktionswerte berechnen|Anstieg aus zwei Punkten bestimmen|"
                    "Punkt-Steigungs-Form anwenden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="Diagramm", skizze=SKIZZE_12, kontext="Wanderweg / Höhenprofil", textumfang="kurz",
    gegeben="Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x) für 0 ≤ x ≤ 6, 1 LE = 1 km. Im "
            "Intervall [2 ; 6] soll das Profil näherungsweise durch die Gerade durch die Punkte "
            "(2 | f(2)) und (6 | f(6)) ersetzt werden.",
    gesucht="Gleichung dieser Geraden",
    verfahren="f(2) = 3 · e^(−1) ≈ 1,104 und f(6) = 7 · e^(−3) ≈ 0,349 berechnen, daraus den "
              "Anstieg m = (f(6) − f(2))/4 ≈ −0,189 bilden und die Gerade in der "
              "Punkt-Steigungs-Form y = m · (x − 2) + f(2) aufstellen.",
    schritte="4", zahlenraum="dezimal|negativ", einheiten="km",
    abhaengig_von="",
    ergebnis="m ≈ −0,1888 und y ≈ −0,189x + 1,481",
    zwischenergebnis="f(2) = 3 · e^(−1) ≈ 1,1036|f(6) = 7 · e^(−3) ≈ 0,3485",
    niveau_geschaetzt="I",
    fehlerquelle="den Anstieg durch die Differenz der Funktionswerte ohne Division durch die "
                 "Intervalllänge 4 bestimmen",
    bemerkung="Der Anstieg der Sekante ist die mittlere Änderungsrate; deshalb Thema Ableitung "
              "und Änderungsrate, obwohl das Ergebnis eine Geradengleichung ist. Eigene Rechnung, "
              "mit sympy bestätigt.")

row(id="2018-be-gk-B1.2f", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="f",
    seite="4", punkte="5",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Unterschreiten einer Steigungsschranke über das Minimum der Ableitung nachweisen",
    typ_neben="",
    stichwoerter="Steigung|Schranke|Minimum der Ableitung|Wendestelle",
    voraussetzungen="zweite Ableitung bilden|Extremstelle der ersten Ableitung bestimmen|"
                    "Zahlenwerte vergleichen",
    format="Begründung|Rechnung", operator="Weisen Sie nach", antwort="Text|Zahl",
    material="Diagramm", skizze=SKIZZE_12, kontext="Wanderweg / Höhenprofil", textumfang="kurz",
    gegeben="Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x) für 0 ≤ x ≤ 6 und "
            "f'(x) = (0,5 − 0,5x) · e^(−0,5x), 1 LE = 1 km.",
    gesucht="Nachweis, dass es im Intervall [2 ; 6] eine Stelle gibt, an der die Steigung des "
            "Höhenprofils kleiner als −0,222 ist",
    verfahren="Die Steigung ist im Intervall dort am kleinsten, wo f' sein Minimum hat, also bei "
              "f''(x) = 0,25 · (x − 3) · e^(−0,5x) = 0 und damit bei x = 3. Dort ist "
              "f'(3) = −e^(−1,5) ≈ −0,2231 und damit kleiner als −0,222. Es genügt auch, den "
              "Wert f'(3) zu berechnen und mit der Schranke zu vergleichen.",
    schritte="4", zahlenraum="dezimal|negativ", einheiten="",
    abhaengig_von="",
    ergebnis="An der Stelle x = 3 ist f'(3) = −e^(−1,5) ≈ −0,223 < −0,222; damit ist die Existenz "
             "einer solchen Stelle nachgewiesen.",
    zwischenergebnis="f''(x) = 0,25 · (x − 3) · e^(−0,5x)|x = 3|f'(3) = −e^(−1,5)",
    niveau_geschaetzt="III",
    fehlerquelle="die mittlere Steigung aus e) als Beleg nehmen; sie beträgt nur etwa −0,189 und "
                 "liegt über der Schranke",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B1.2g", block="B", aufgabe="1.2", titel="Höhenprofil", teilaufgabe="g",
    seite="5", punkte="9",
    leitidee="Analysis", thema="Ableitung und Änderungsrate",
    typ="Mittlere Änderungsraten zweier Modelle vergleichen",
    typ_neben="Parameter einer Exponentialfunktion aus zwei Wertepaaren bestimmen",
    stichwoerter="mittlere Steigung|Vergleich|Parameter bestimmen|Logarithmieren",
    voraussetzungen="mittlere Änderungsrate als Differenzenquotient bilden|Beträge vergleichen|"
                    "Exponentialgleichung durch Logarithmieren lösen",
    format="Rechnung|Begründung", operator="Untersuchen Sie|Ermitteln Sie", antwort="Zahl|Term",
    material="Tabelle",
    skizze="Kleine Wertetabelle mit zwei Spalten: x in km mit den Werten 0 und 6, darunter die "
           "Höhe h_W(x) in km mit den Werten 1,2 und 0,3.",
    kontext="Wanderweg / Höhenprofil", textumfang="mittel",
    gegeben="Höhenprofil f mit f(x) = (x + 1) · e^(−0,5x), 1 LE = 1 km. Ähnliche Profile werden "
            "durch h(x) = (x + a) · e^(b · x) mit a > 0 und b < 0 beschrieben. Von einem Profil "
            "h_W ist bekannt: h_W(0) = 1,2 km und h_W(6) = 0,3 km.",
    gesucht="Vergleich der Beträge der mittleren Steigungen von f und h_W im Intervall [0 ; 6]; "
            "Werte von a und b für h_W",
    verfahren="Mittlere Steigung als Differenzenquotient: bei f ist (f(6) − f(0))/6 = "
              "(7 · e^(−3) − 1)/6 ≈ −0,109, bei h_W ist (0,3 − 1,2)/6 = −0,15; der Betrag ist bei "
              "h_W größer. Für die Parameter aus h_W(0) = a = 1,2 und aus "
              "(6 + 1,2) · e^(6b) = 0,3 die Gleichung e^(6b) = 1/24 durch Logarithmieren lösen.",
    schritte="6", zahlenraum="dezimal|negativ|Bruch", einheiten="km",
    abhaengig_von="",
    ergebnis="Die mittlere Steigung beträgt bei f etwa −0,109, bei h_W −0,15; der Betrag ist bei "
             "h_W größer. Für h_W gilt a = 1,2 und b = −ln 24 / 6 ≈ −0,53.",
    zwischenergebnis="f(0) = 1|f(6) = 7 · e^(−3) ≈ 0,3485|a = 1,2|e^(6b) = 1/24",
    niveau_geschaetzt="III",
    fehlerquelle="die Beträge der negativen Steigungen falsch herum vergleichen, oder beim "
                 "Logarithmieren den Faktor 6 im Exponenten vergessen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

FOTO_21 = ("Fotografie einer Brücke über eine Autobahn, aufgenommen von der Fahrbahn aus. Die "
           "Eckpunkte der seitlichen Streben sind beschriftet: A und C am linken Widerlager "
           "(C oberhalb von A), B und D am rechten Widerlager (D oberhalb von B); die Strebe von "
           "A nach B bildet die Unterkante, die von C nach D die Oberkante des Fachwerks. Auf der "
           "Fahrbahn sind die Fahrzeugpositionen P (vorn) und Q (weiter hinten) markiert.")

row(id="2018-be-gk-B2.1a", block="B", aufgabe="2.1", titel="Brücke", teilaufgabe="a",
    seite="6", punkte="4",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus drei Punkten aufstellen",
    typ_neben="",
    stichwoerter="Normalenvektor|Koordinatenform|Ebene durch drei Punkte|Brückenstrebe",
    voraussetzungen="Verbindungsvektoren bilden|Kreuzprodukt oder lineares Gleichungssystem für "
                    "den Normalenvektor|Punktprobe zur Bestimmung des absoluten Glieds",
    format="Rechnung", operator="Ermitteln Sie|Geben Sie an", antwort="Term",
    material="Foto", skizze=FOTO_21, kontext="Brücke über eine Autobahn", textumfang="mittel",
    gegeben="Seitliche Streben einer Brücke im Koordinatensystem durch A(0 | 0 | 5), "
            "B(4,4 | 44 | 5), C(0,2 | 2 | 7) und D(4,8 | 48 | 9); die Fahrbahn liegt in der "
            "x-y-Ebene, 1 LE = 1 m. Die Punkte A, B und C liegen in der Ebene E. Als Kontrolle "
            "ist E: −10x + y = 0 angegeben.",
    gesucht="Normalenvektor der Ebene E; Gleichung von E in Koordinatenform",
    verfahren="Die Verbindungsvektoren AB = (4,4 | 44 | 0) und AC = (0,2 | 2 | 2) bilden und ihr "
              "Kreuzprodukt n = (88 | −8,8 | 0) berechnen; gekürzt ist n = (10 | −1 | 0). Mit dem "
              "Ansatz 10x − y = d und dem Punkt A folgt d = 0, also E: −10x + y = 0.",
    schritte="4", zahlenraum="ganz|dezimal|negativ", einheiten="m",
    abhaengig_von="",
    ergebnis="n = (10 | −1 | 0) beziehungsweise (−10 | 1 | 0); E: −10x + y = 0",
    zwischenergebnis="AB = (4,4 | 44 | 0)|AC = (0,2 | 2 | 2)|n = (88 | −8,8 | 0)",
    niveau_geschaetzt="II",
    fehlerquelle="beim Kreuzprodukt die Komponenten vertauschen, oder das absolute Glied nicht "
                 "über eine Punktprobe bestimmen",
    bemerkung="Das Kontrollergebnis ist durch eigene Rechnung bestätigt. Eigene Rechnung, mit "
              "sympy bestätigt.")

row(id="2018-be-gk-B2.1b", block="B", aufgabe="2.1", titel="Brücke", teilaufgabe="b",
    seite="6", punkte="3",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Punktprobe an einer Ebenengleichung durchführen",
    typ_neben="Orthogonalität zweier Ebenen über die Normalenvektoren nachweisen",
    stichwoerter="Punktprobe|Orthogonalität zweier Ebenen|Normalenvektor|x-y-Ebene",
    voraussetzungen="Koordinaten in eine Ebenengleichung einsetzen|Skalarprodukt bilden|"
                    "Normalenvektor der x-y-Ebene kennen",
    format="Begründung", operator="Weisen Sie nach|Zeigen Sie", antwort="Text",
    material="Foto", skizze=FOTO_21, kontext="Brücke über eine Autobahn", textumfang="kurz",
    gegeben="Ebene E: −10x + y = 0 und der Punkt D(4,8 | 48 | 9); die Fahrbahn liegt in der "
            "x-y-Ebene, 1 LE = 1 m.",
    gesucht="Nachweis, dass D in E liegt; Nachweis, dass E orthogonal zur x-y-Ebene liegt",
    verfahren="D in die Ebenengleichung einsetzen: −10 · 4,8 + 48 = 0, die Gleichung ist erfüllt. "
              "Für die Orthogonalität das Skalarprodukt der Normalenvektoren "
              "n_E = (−10 | 1 | 0) und n_xy = (0 | 0 | 1) bilden; es ist null, also stehen die "
              "Ebenen senkrecht aufeinander.",
    schritte="3", zahlenraum="ganz|dezimal|negativ", einheiten="m",
    abhaengig_von="2018-be-gk-B2.1a",
    ergebnis="−10 · 4,8 + 48 = 0, also liegt D in E. n_E · n_xy = 0, also steht E senkrecht auf "
             "der x-y-Ebene; gleichwertig: der Normalenvektor von E hat die z-Komponente null.",
    zwischenergebnis="n_E = (−10 | 1 | 0)|n_xy = (0 | 0 | 1)",
    niveau_geschaetzt="II",
    fehlerquelle="für orthogonale Ebenen ein Skalarprodukt der Normalenvektoren ungleich null "
                 "erwarten, weil die Bedingung mit der für orthogonale Geraden verwechselt wird",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B2.1c", block="B", aufgabe="2.1", titel="Brücke", teilaufgabe="c",
    seite="6", punkte="6",
    leitidee="Analytische Geometrie", thema="Lagebeziehungen",
    typ="Existenz eines Geradenschnittpunkts über die gemeinsame Ebene begründen",
    typ_neben="Schnittwinkel zweier Geraden über das Skalarprodukt berechnen",
    stichwoerter="windschief oder schneidend|gemeinsame Ebene|Richtungsvektoren|Schnittwinkel",
    voraussetzungen="Richtungsvektoren auf Vielfache prüfen|Skalarprodukt und Beträge berechnen|"
                    "Arkuskosinus anwenden",
    format="Begründung|Rechnung", operator="Begründen Sie|Berechnen Sie", antwort="Text|Zahl",
    material="Foto", skizze=FOTO_21, kontext="Brücke über eine Autobahn", textumfang="mittel",
    gegeben="A(0 | 0 | 5), B(4,4 | 44 | 5), C(0,2 | 2 | 7) und D(4,8 | 48 | 9) liegen alle in der "
            "Ebene E: −10x + y = 0. Die Gerade g verläuft durch A und B, die Gerade h durch C und "
            "D; 1 LE = 1 m.",
    gesucht="Begründung, dass g und h einen Schnittpunkt haben müssen; Schnittwinkel der beiden "
            "Geraden",
    verfahren="Alle vier Punkte liegen in E, also liegen auch beide Geraden in dieser Ebene. Ihre "
              "Richtungsvektoren (4,4 | 44 | 0) und (4,6 | 46 | 2) sind keine Vielfachen "
              "voneinander, die Geraden sind also nicht parallel; zwei nicht parallele Geraden "
              "einer Ebene schneiden sich. Den Winkel über "
              "cos φ = |u · v| / (|u| · |v|) berechnen.",
    schritte="5", zahlenraum="ganz|dezimal", einheiten="m",
    abhaengig_von="2018-be-gk-B2.1b",
    ergebnis="Beide Geraden liegen in E und sind nicht parallel, also schneiden sie sich. Mit "
             "u · v = 2044,24, |u| ≈ 44,22 und |v| ≈ 46,27 ist cos φ ≈ 0,9991 und φ ≈ 2,5°.",
    zwischenergebnis="u = (4,4 | 44 | 0)|v = (4,6 | 46 | 2)|u · v = 2044,24|Schnittpunkt "
                     "(−4,4 | −44 | 5)",
    niveau_geschaetzt="II",
    fehlerquelle="aus der Ähnlichkeit der Richtungsvektoren auf Parallelität schließen, oder die "
                 "Existenz des Schnittpunkts durch Gleichsetzen nachrechnen, statt sie mit der "
                 "gemeinsamen Ebene zu begründen",
    bemerkung="Der Schnittpunkt liegt bei (−4,4 | −44 | 5) und damit außerhalb des abgebildeten "
              "Brückenteils; gefragt ist nur die Begründung der Existenz. Eigene Rechnung, mit "
              "sympy bestätigt.")

row(id="2018-be-gk-B2.1d", block="B", aufgabe="2.1", titel="Brücke", teilaufgabe="d",
    seite="6", punkte="2",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Streckenlänge im Raum berechnen",
    typ_neben="Geschwindigkeit aus Weg und Zeit berechnen und in Kilometer pro Stunde umrechnen",
    stichwoerter="Betrag eines Vektors|zurückgelegte Strecke|Geschwindigkeit|Einheiten umrechnen",
    voraussetzungen="Verbindungsvektor bilden|Betrag berechnen|Meter je Sekunde in Kilometer je "
                    "Stunde umrechnen",
    format="Rechnung", operator="Berechnen Sie|Geben Sie an", antwort="Zahl",
    material="Foto", skizze=FOTO_21, kontext="Brücke über eine Autobahn", textumfang="mittel",
    gegeben="Ein Fahrzeug bewegt sich mit konstanter Geschwindigkeit geradlinig; zunächst ist es "
            "im Punkt P(82 | 40 | 0) und 1,5 s später im Punkt Q(42 | 36 | 0), 1 LE = 1 m.",
    gesucht="in 1,5 s zurückgelegte Strecke; Geschwindigkeit des Fahrzeugs in Kilometern je "
            "Stunde",
    verfahren="Den Vektor PQ = (−40 | −4 | 0) bilden und seinen Betrag berechnen. Die "
              "Geschwindigkeit ist der Quotient aus Weg und Zeit; das Ergebnis in Metern je "
              "Sekunde mit 3,6 multiplizieren.",
    schritte="3", zahlenraum="ganz|dezimal|negativ|Wurzel", einheiten="m|s|km/h",
    abhaengig_von="",
    ergebnis="|PQ| = 4√101 ≈ 40,2 m; v ≈ 26,8 m je Sekunde, also etwa 96,5 km je Stunde.",
    zwischenergebnis="PQ = (−40 | −4 | 0)|1616 unter der Wurzel",
    niveau_geschaetzt="I",
    fehlerquelle="beim Umrechnen durch 3,6 teilen statt zu multiplizieren",
    bemerkung="Die Umrechnung in Kilometer je Stunde ist eine Sachrechnung ohne eigenes Thema in "
              "der Themenliste Analytische Geometrie; der Nebentyp steht ersatzweise unter Punkte "
              "und Strecken im Koordinatensystem. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B2.1e", block="B", aufgabe="2.1", titel="Brücke", teilaufgabe="e",
    seite="6", punkte="5",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Zeit bis zum Erreichen einer Ebene aus dem Geradenparameter bestimmen",
    typ_neben="Durchstoßpunkt einer Geraden durch eine Ebene bestimmen",
    stichwoerter="Fahrtdauer|Geradengleichung|senkrecht unter der Strebe|Parameter deuten",
    voraussetzungen="Geradengleichung aus zwei Punkten aufstellen|Parameter aus einer "
                    "Koordinatengleichung bestimmen|Parameter als Vielfaches der Zeitspanne "
                    "deuten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Foto", skizze=FOTO_21, kontext="Brücke über eine Autobahn", textumfang="mittel",
    gegeben="Das Fahrzeug fährt geradlinig und gleichförmig von P(82 | 40 | 0) über Q(42 | 36 | 0) "
            "weiter; für die Strecke von P nach Q braucht es 1,5 s. Die Strebe durch A(0 | 0 | 5) "
            "und B(4,4 | 44 | 5) liegt in der Ebene E: −10x + y = 0, die senkrecht auf der "
            "Fahrbahn steht; 1 LE = 1 m.",
    gesucht="Zeit, die das Fahrzeug von Q bis zu dem Punkt braucht, der genau vertikal unter der "
            "Strebe durch A und B liegt",
    verfahren="Genau vertikal unter der Strebe liegen die Punkte der Fahrbahn, die in der Ebene E "
              "liegen, weil E senkrecht auf der Fahrbahn steht und die Strebe enthält. Die "
              "Fahrzeugbahn x = Q + r · (−40 | −4 | 0) in E einsetzen: "
              "−10 · (42 − 40r) + (36 − 4r) = 0 ergibt r = 32/33. Da r = 1 der Zeitspanne 1,5 s "
              "entspricht, ist die gesuchte Zeit 1,5 s · 32/33.",
    schritte="5", zahlenraum="ganz|dezimal|Bruch|negativ", einheiten="m|s",
    abhaengig_von="2018-be-gk-B2.1d",
    ergebnis="r = 32/33, der Punkt ist (3,2 | 32,1 | 0); die Fahrzeit beträgt 16/11 s ≈ 1,45 s.",
    zwischenergebnis="Bahn x = (42 | 36 | 0) + r · (−40 | −4 | 0)|396r = 384",
    niveau_geschaetzt="III",
    fehlerquelle="den Fußpunkt als Lotfußpunkt auf die Gerade durch A und B bestimmen, statt den "
                 "Durchstoßpunkt der Fahrbahnbahn mit der senkrechten Ebene E zu suchen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

SKIZZE_22 = ("Schrägbild eines räumlichen Koordinatensystems mit x nach vorn (Teilung bis 12), y "
             "nach rechts (Teilung bis 16) und z nach oben (Teilung bis 6). Dargestellt sind zwei "
             "waagerechte, grau ausgefüllte Plattformen, jede um einen senkrechten Pfahl gebaut: "
             "Plattform 1 in Höhe z = 2 um den Pfahl 1 durch P₁(0 | 0 | 0) mit den beschrifteten "
             "Eckpunkten A, B, C und D, Plattform 2 in Höhe z = 3 um den Pfahl 2 durch "
             "P₂(5 | 10 | 0) mit den Eckpunkten R, S und T. Zwischen der Plattform 1 und dem "
             "Untergrund liegt die grau ausgefüllte, geneigte Kletterwand mit den Eckpunkten A, "
             "B oben und E, F auf dem Untergrund; sie ist mit Kletterwand beschriftet.")

row(id="2018-be-gk-B2.2a", block="B", aufgabe="2.2", titel="Kletteranlage", teilaufgabe="a",
    seite="7", punkte="3",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Streckenlänge im Raum berechnen",
    typ_neben="Mittelpunkt einer Strecke im Raum bestimmen",
    stichwoerter="Kantenmittelpunkte|Abstand|Seillänge|prozentualer Zuschlag",
    voraussetzungen="Mittelpunkt als halbe Summe der Ortsvektoren bilden|Betrag eines Vektors "
                    "berechnen|einen Zuschlag von 20 Prozent berechnen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=SKIZZE_22, kontext="Kletteranlage", textumfang="mittel",
    gegeben="Die Kletterwand ist das Viereck mit den Eckpunkten A(3 | 0 | 2), B(0 | 3 | 2) als "
            "oberer Kante und E(6 | 0 | 0), F(0 | 6 | 0) als unterer Kante; 1 LE = 1 m. In den "
            "Mittelpunkten der oberen und der unteren Kante sind die Enden eines Seils "
            "befestigt, das 20 Prozent länger ist als der Abstand dieser Mittelpunkte.",
    gesucht="Länge des Seils",
    verfahren="Die Mittelpunkte M₁ = (1,5 | 1,5 | 2) der Kante AB und M₂ = (3 | 3 | 0) der Kante "
              "EF bestimmen, den Betrag des Verbindungsvektors (1,5 | 1,5 | −2) berechnen und das "
              "Ergebnis mit 1,2 multiplizieren.",
    schritte="4", zahlenraum="ganz|dezimal|Wurzel|negativ", einheiten="m",
    abhaengig_von="",
    ergebnis="M₁(1,5 | 1,5 | 2), M₂(3 | 3 | 0), Abstand √8,5 ≈ 2,92 m; das Seil ist etwa 3,50 m "
             "lang.",
    zwischenergebnis="M₁M₂ = (1,5 | 1,5 | −2)|8,5 unter der Wurzel",
    niveau_geschaetzt="II",
    fehlerquelle="die Seillänge als 20 Prozent des Abstands statt als das 1,2fache berechnen, "
                 "oder die Mittelpunkte der Seitenkanten statt der oberen und unteren Kante nehmen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B2.2b", block="B", aufgabe="2.2", titel="Kletteranlage", teilaufgabe="b",
    seite="7", punkte="3",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Trapezform eines Vierecks im Raum nachweisen",
    typ_neben="",
    stichwoerter="Trapez|Parallelität|gleich lange Schenkel|Vektorvergleich",
    voraussetzungen="Richtungsvektoren auf Vielfache prüfen|Beträge von Vektoren vergleichen",
    format="Begründung", operator="Zeigen Sie", antwort="Text",
    material="Körper", skizze=SKIZZE_22, kontext="Kletteranlage", textumfang="kurz",
    gegeben="Kletterwand mit den Eckpunkten A(3 | 0 | 2), B(0 | 3 | 2), E(6 | 0 | 0) und "
            "F(0 | 6 | 0), 1 LE = 1 m.",
    gesucht="Nachweis, dass die Kletterwand ein Trapez ist, in dem zwei gegenüberliegende Seiten "
            "gleich lang sind",
    verfahren="AB = (−3 | 3 | 0) und EF = (−6 | 6 | 0) = 2 · AB, also sind diese beiden Seiten "
              "parallel und die Wand ist ein Trapez. Für die Schenkel AE = (3 | 0 | −2) und "
              "BF = (0 | 3 | −2) ist |AE| = |BF| = √13, sie sind also gleich lang.",
    schritte="4", zahlenraum="ganz|negativ|Wurzel", einheiten="m",
    abhaengig_von="",
    ergebnis="EF = 2 · AB, also AB parallel zu EF und damit ein Trapez; |AE| = |BF| = √13 ≈ 3,61 m, "
             "die beiden Schenkel sind gleich lang.",
    zwischenergebnis="AB = (−3 | 3 | 0)|EF = (−6 | 6 | 0)|AE = (3 | 0 | −2)|BF = (0 | 3 | −2)",
    niveau_geschaetzt="II",
    fehlerquelle="Parallelität aus gleich langen Vektoren statt aus dem Vielfachenverhältnis "
                 "schließen, oder die falschen Seitenpaare vergleichen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B2.2c", block="B", aufgabe="2.2", titel="Kletteranlage", teilaufgabe="c",
    seite="7", punkte="3",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Schnittwinkel zweier Ebenen über die Normalenvektoren berechnen",
    typ_neben="",
    stichwoerter="Neigungswinkel|Normalenvektoren|Kletterwand|Untergrund",
    voraussetzungen="Normalenvektor aus der Koordinatengleichung ablesen|Skalarprodukt und "
                    "Beträge berechnen|Arkuskosinus anwenden",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Körper", skizze=SKIZZE_22, kontext="Kletteranlage", textumfang="kurz",
    gegeben="Die Punkte A(3 | 0 | 2), B(0 | 3 | 2), E(6 | 0 | 0) und F(0 | 6 | 0) der Kletterwand "
            "liegen in der Ebene L: 2x + 2y + 3z − 12 = 0; der Untergrund ist die x-y-Ebene, "
            "1 LE = 1 m.",
    gesucht="Größe des Winkels zwischen Kletterwand und Untergrund",
    verfahren="Die Normalenvektoren n_L = (2 | 2 | 3) und n_xy = (0 | 0 | 1) ablesen und "
              "cos φ = |n_L · n_xy| / (|n_L| · |n_xy|) = 3/√17 berechnen; der Winkel zwischen den "
              "Normalen ist zugleich der Winkel zwischen den Ebenen.",
    schritte="3", zahlenraum="ganz|dezimal|Wurzel", einheiten="",
    abhaengig_von="",
    ergebnis="cos φ = 3/√17 ≈ 0,7276, also φ ≈ 43,3°.",
    zwischenergebnis="n_L = (2 | 2 | 3)|n_xy = (0 | 0 | 1)|√17 ≈ 4,123",
    niveau_geschaetzt="II",
    fehlerquelle="den Nebenwinkel 136,7° angeben, oder den Winkel zwischen Normalenvektor und "
                 "Ebene mit dem Winkel zwischen den Ebenen verwechseln",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B2.2d", block="B", aufgabe="2.2", titel="Kletteranlage", teilaufgabe="d",
    seite="7", punkte="6",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Lage eines Punktes auf einer Strecke über die Parameterform nachweisen",
    typ_neben="Schattenpunkt bei paralleler Projektion bestimmen|"
              "Schatten einer Fläche in eine Abbildung einzeichnen",
    stichwoerter="Schatten|parallele Lichtstrahlen|Punkt auf einer Strecke|Schattendreieck",
    voraussetzungen="Parameterform einer Strecke aufstellen|Parameter auf das Intervall von 0 bis "
                    "1 prüfen|Richtungsvektor aus zwei zugeordneten Punkten gewinnen|"
                    "Durchstoßpunkt mit der x-y-Ebene bestimmen",
    format="Begründung|Rechnung|Zeichnen",
    operator="Zeigen Sie|Berechnen Sie|Stellen Sie dar", antwort="Text|Zahl|Grafik",
    material="Körper", skizze=SKIZZE_22, kontext="Kletteranlage", textumfang="mittel",
    gegeben="Sonnenlicht wird durch parallele Geraden beschrieben. Die Plattform 2 hat die "
            "Eckpunkte R(5 | 7 | 3), S(8 | 13 | 3) und T(2 | 10 | 3), ihre Schattenpunkte auf dem "
            "Untergrund sind R'(4 | 2 | 0), S' und T'(1 | 5 | 0); außerdem sind E(6 | 0 | 0) und "
            "F(0 | 6 | 0) gegeben, 1 LE = 1 m.",
    gesucht="Nachweis, dass T' auf der Strecke EF liegt; Koordinaten von S'; Darstellung des "
            "Schattens der Plattform 2 in der Abbildung",
    verfahren="Die Strecke EF als E + t · (F − E) ansetzen und T' einsetzen: aus 6 − 6t = 1 folgt "
              "t = 5/6, die übrigen Koordinaten stimmen und t liegt zwischen 0 und 1. Die "
              "Lichtrichtung ist R'− R = (−1 | −5 | −3); von S aus in dieser Richtung bis z = 0 "
              "gehen liefert S'. Danach das Dreieck R'S'T' in die Abbildung eintragen.",
    schritte="5", zahlenraum="ganz|Bruch|negativ", einheiten="m",
    abhaengig_von="",
    ergebnis="T' = E + 5/6 · (F − E) mit 5/6 zwischen 0 und 1, also liegt T' auf der Strecke EF. "
             "S'(7 | 8 | 0). Der Schatten ist das Dreieck mit den Ecken R'(4 | 2 | 0), "
             "S'(7 | 8 | 0) und T'(1 | 5 | 0) auf dem Untergrund.",
    zwischenergebnis="t = 5/6|Lichtrichtung (−1 | −5 | −3)|Probe mit T und T' bestätigt die "
                     "Richtung",
    niveau_geschaetzt="II",
    fehlerquelle="nur zeigen, dass T' auf der Geraden durch E und F liegt, ohne den Parameter auf "
                 "das Intervall von 0 bis 1 zu prüfen",
    bemerkung="Das Feld skizze beschreibt das vorgegebene Schrägbild; der Schatten ist darin zu "
              "ergänzen. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B2.2e", block="B", aufgabe="2.2", titel="Kletteranlage", teilaufgabe="e",
    seite="8", punkte="5",
    leitidee="Analytische Geometrie", thema="Geraden",
    typ="Lösungsweg zur Bestimmung eines Punktes auf einer Geraden beschreiben",
    typ_neben="",
    stichwoerter="Drahtseil|Teilverhältnis|Lösungsweg beschreiben|Höhe am Pfahl",
    voraussetzungen="Teilpunkt einer Strecke über das Teilverhältnis ansetzen|Gerade durch zwei "
                    "Punkte aufstellen|Schnitt mit einer senkrechten Geraden bilden",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="Körper", skizze=SKIZZE_22, kontext="Kletteranlage", textumfang="lang",
    gegeben="Ein geradlinig gespanntes Drahtseil ist am Pfahl 1 durch P₁(0 | 0 | 0) in Höhe der "
            "Plattform 1 befestigt, also im Punkt (0 | 0 | 2), und am Pfahl 2 durch "
            "P₂(5 | 10 | 0) oberhalb der Plattform 2, die in der Höhe z = 3 liegt. Das Seil "
            "berührt die Plattform 2 an der Seite RT mit R(5 | 7 | 3) und T(2 | 10 | 3). Das "
            "Verhältnis, in dem der Berührpunkt die Strecke RT teilt, ist als bekannt "
            "vorausgesetzt; 1 LE = 1 m.",
    gesucht="Beschreibung eines Verfahrens, mit dem sich der Abstand des Befestigungspunktes am "
            "Pfahl 2 von der Plattform 2 berechnen lässt",
    verfahren="Aus dem bekannten Teilverhältnis den Berührpunkt X als R + k · (T − R) bestimmen. "
              "Das Seil ist die Gerade durch den Befestigungspunkt (0 | 0 | 2) und X. Der Pfahl 2 "
              "ist die senkrechte Gerade mit x = 5 und y = 10; den Schnittpunkt dieser Geraden "
              "mit der Seilgeraden bestimmen. Der gesuchte Abstand ist die Differenz zwischen "
              "seiner z-Koordinate und der Plattformhöhe 3.",
    schritte="4", zahlenraum="ganz", einheiten="m",
    abhaengig_von="",
    ergebnis="Beschreibung des Weges: Berührpunkt X aus dem Teilverhältnis auf RT bestimmen, "
             "Gerade durch (0 | 0 | 2) und X aufstellen, ihren Schnittpunkt mit der Senkrechten "
             "durch P₂ berechnen und von dessen z-Koordinate die Plattformhöhe 3 abziehen.",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="den Abstand als Abstand des Punktes von der Plattformebene im Sinne eines "
                 "Lotfußpunkts beschreiben, obwohl die Plattform waagerecht liegt und die "
                 "Höhendifferenz gemeint ist",
    bemerkung="Gefragt ist nur die Beschreibung des Verfahrens, keine Zahlenrechnung; das "
              "Teilverhältnis wird im Heft nicht angegeben. Eigene Rechnung nicht erforderlich.")

row(id="2018-be-gk-B3.1a", block="B", aufgabe="3.1", titel="Gewinnspiel", teilaufgabe="a",
    seite="9", punkte="2",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Wahrscheinlichkeit beim Ziehen ohne Zurücklegen mit der Pfadregel nachweisen",
    typ_neben="",
    stichwoerter="Urne|ohne Zurücklegen|Pfadregel|Gewinnwahrscheinlichkeit",
    voraussetzungen="zweistufiges Ziehen ohne Zurücklegen modellieren|Pfadregel anwenden|"
                    "alternativ mit Binomialkoeffizienten abzählen",
    format="Begründung|Rechnung", operator="Weisen Sie nach", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Gewinnspiel auf einem Schulfest",
    textumfang="mittel",
    gegeben="In einem Topf liegen 2 schwarze und 4 weiße Kugeln. Bei einem Spiel werden zwei "
            "Kugeln mit einem Griff, also ohne Zurücklegen, gezogen. Der Spieler gewinnt genau "
            "dann, wenn keine schwarze Kugel dabei ist.",
    gesucht="Nachweis, dass die Gewinnwahrscheinlichkeit p = 0,4 beträgt",
    verfahren="Zweistufiges Ziehen ohne Zurücklegen: beide Kugeln weiß mit der Pfadregel "
              "4/6 · 3/5 = 12/30. Gleichwertig über Binomialkoeffizienten: die Zahl der "
              "Möglichkeiten, 2 der 4 weißen Kugeln zu ziehen, geteilt durch die Zahl der "
              "Möglichkeiten, 2 der 6 Kugeln zu ziehen.",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="",
    abhaengig_von="",
    ergebnis="p = 4/6 · 3/5 = 2/5 = 0,4; gleichwertig 6/15 = 0,4.",
    zwischenergebnis="4/6 · 3/5 = 12/30",
    niveau_geschaetzt="I",
    fehlerquelle="mit Zurücklegen rechnen und (4/6)² = 4/9 erhalten",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.1b", block="B", aufgabe="3.1", titel="Gewinnspiel", teilaufgabe="b",
    seite="9", punkte="5",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer Binomialverteilung für genau k Treffer berechnen",
    typ_neben="Kumulierte Wahrscheinlichkeit einer Binomialverteilung berechnen",
    stichwoerter="Bernoulli-Kette|genau vier Treffer|erstes Spiel gewonnen|höchstens ein Treffer",
    voraussetzungen="Binomialformel anwenden|Unabhängigkeit aufeinanderfolgender Spiele nutzen|"
                    "Ereignis in zwei unabhängige Teile zerlegen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Gewinnspiel auf einem Schulfest", textumfang="kurz",
    gegeben="Ein Spieler spielt das Spiel mit der Gewinnwahrscheinlichkeit p = 0,4 zehnmal; nach "
            "jedem Spiel werden die Kugeln zurückgelegt. Ereignis A: genau 4 der 10 Spiele "
            "gewonnen. Ereignis B: das erste Spiel gewonnen und von den übrigen 9 höchstens eins.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="A mit der Binomialformel für n = 10, p = 0,4 und k = 4 berechnen. B in zwei "
              "unabhängige Teile zerlegen: das erste Spiel gewinnen mit 0,4, und von den übrigen "
              "9 Spielen höchstens eines gewinnen, also 0,6⁹ + 9 · 0,4 · 0,6⁸; die beiden "
              "Wahrscheinlichkeiten multiplizieren.",
    schritte="5", zahlenraum="dezimal|Potenz", einheiten="",
    abhaengig_von="2018-be-gk-B3.1a",
    ergebnis="P(A) ≈ 0,2508; P(B) = 0,4 · (0,6⁹ + 9 · 0,4 · 0,6⁸) ≈ 0,0282.",
    zwischenergebnis="P(A) = 210 · 0,4⁴ · 0,6⁶|P(höchstens 1 von 9) ≈ 0,0705",
    niveau_geschaetzt="II",
    fehlerquelle="bei B mit n = 10 statt mit n = 9 für den zweiten Teil rechnen, oder höchstens "
                 "eins als genau eins lesen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.1c", block="B", aufgabe="3.1", titel="Gewinnspiel", teilaufgabe="c",
    seite="9", punkte="5",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Behauptung zur Monotonie einer Wahrscheinlichkeit an Beispielwerten prüfen",
    typ_neben="Wahrscheinlichkeit für wenigstens einen Treffer über das Gegenereignis berechnen",
    stichwoerter="wenigstens ein Treffer|Gegenereignis|Monotonie|Behauptung prüfen",
    voraussetzungen="Gegenereignis bilden|Potenzen vergleichen|eine Behauptung an Beispielen "
                    "widerlegen",
    format="Rechnung|Begründung", operator="Entscheiden Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Gewinnspiel auf einem Schulfest", textumfang="mittel",
    gegeben="Das Spiel hat die Gewinnwahrscheinlichkeit p = 0,4 und wird n-mal gespielt. Ereignis "
            "C: wenigstens eins von n Spielen wird gewonnen. Eine Spielerin behauptet, P(C) werde "
            "kleiner, wenn n größer wird.",
    gesucht="Entscheidung über die Behauptung anhand zweier berechneter Wahrscheinlichkeiten",
    verfahren="P(C) über das Gegenereignis kein Gewinn bestimmen: P(C) = 1 − 0,6ⁿ. Zwei Werte "
              "berechnen, etwa n = 1 mit 0,4 und n = 10 mit etwa 0,994; da 0,6ⁿ mit wachsendem n "
              "kleiner wird, wächst P(C). Die Behauptung ist damit widerlegt.",
    schritte="3", zahlenraum="dezimal|Potenz", einheiten="",
    abhaengig_von="2018-be-gk-B3.1a",
    ergebnis="P(C) = 1 − 0,6ⁿ; für n = 1 ist P(C) = 0,4, für n = 10 ist P(C) ≈ 0,9940. P(C) wird "
             "also größer, die Behauptung ist falsch.",
    zwischenergebnis="0,6¹⁰ ≈ 0,0060",
    niveau_geschaetzt="II",
    fehlerquelle="P(C) als Summe der Einzelwahrscheinlichkeiten aufschreiben und im Rechenaufwand "
                 "steckenbleiben, statt das Gegenereignis zu nutzen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.1d", block="B", aufgabe="3.1", titel="Gewinnspiel", teilaufgabe="d",
    seite="9", punkte="2",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen",
    typ_neben="",
    stichwoerter="Erwartungswert|Einsatz und Auszahlung|langfristiger Gewinn|Anbieter",
    voraussetzungen="Zufallsgröße für den Gewinn festlegen|Erwartungswert als gewichtete Summe "
                    "bilden|Vorzeichen im Sachzusammenhang deuten",
    format="Rechnung|Begründung", operator="Zeigen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Gewinnspiel auf einem Schulfest", textumfang="kurz",
    gegeben="Der Einsatz beträgt 1 € je Spiel. Mit der Wahrscheinlichkeit 0,4 werden 2 € "
            "ausgezahlt, sonst ist der Einsatz verloren.",
    gesucht="Nachweis, dass das Spiel aus Sicht des Anbieters auf lange Sicht gewinnbringend ist",
    verfahren="Den Erwartungswert der Auszahlung bilden: 0,4 · 2 € = 0,80 €. Er ist kleiner als "
              "der Einsatz von 1 €, der Anbieter nimmt also im Mittel 0,20 € je Spiel ein.",
    schritte="2", zahlenraum="dezimal", einheiten="Euro",
    abhaengig_von="2018-be-gk-B3.1a",
    ergebnis="Erwartete Auszahlung 0,80 € gegenüber 1 € Einsatz; der Anbieter gewinnt im Mittel "
             "0,20 € je Spiel, das Spiel ist für ihn auf lange Sicht gewinnbringend.",
    zwischenergebnis="0,4 · 2 € = 0,80 €",
    niveau_geschaetzt="II",
    fehlerquelle="den Einsatz von 1 € nicht gegenrechnen und die Auszahlung allein als Gewinn "
                 "deuten",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.1e", block="B", aufgabe="3.1", titel="Gewinnspiel", teilaufgabe="e",
    seite="9", punkte="6",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Anzahl der Kugeln aus einer Fairnessbedingung bestimmen",
    typ_neben="Wahrscheinlichkeit beim Ziehen ohne Zurücklegen mit der Pfadregel nachweisen",
    stichwoerter="faires Spiel|Urnenzusammensetzung|quadratische Gleichung|Gegenprobe",
    voraussetzungen="Wahrscheinlichkeit in Abhängigkeit von einer Unbekannten aufstellen|"
                    "quadratische Gleichung lösen|Lösung auf den Sachzusammenhang prüfen",
    format="Rechnung|Begründung", operator="Zeigen Sie|Ermitteln Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Gewinnspiel auf einem Schulfest",
    textumfang="mittel",
    gegeben="Zu den 4 weißen Kugeln kommen 11 weitere weiße, zu den 2 schwarzen kommen x "
            "schwarze. Es werden weiterhin zwei Kugeln mit einem Griff gezogen; gewonnen wird "
            "nur, wenn keine schwarze Kugel dabei ist. Das Spiel ist fair, wenn die "
            "Gewinnwahrscheinlichkeit q = 0,5 beträgt.",
    gesucht="Nachweis, dass x = 2 nicht zu q = 0,5 führt; Anzahl der zuzugebenden schwarzen "
            "Kugeln für ein faires Spiel",
    verfahren="Mit 15 weißen und 2 + x schwarzen Kugeln, also 17 + x insgesamt, ist "
              "q(x) = 15/(17 + x) · 14/(16 + x). Für x = 2 ergibt das 35/57 ≈ 0,614, also nicht "
              "0,5. Die Gleichung q(x) = 0,5 führt auf (17 + x) · (16 + x) = 420, also "
              "x² + 33x − 148 = 0 mit der brauchbaren Lösung x = 4.",
    schritte="6", zahlenraum="Bruch|dezimal|ganz", einheiten="",
    abhaengig_von="2018-be-gk-B3.1a",
    ergebnis="Für x = 2 ist q = 35/57 ≈ 0,614 und damit nicht 0,5. Aus x² + 33x − 148 = 0 folgt "
             "x = 4 (die zweite Lösung x = −37 entfällt); bei 15 weißen und 6 schwarzen Kugeln "
             "ist q = 105/210 = 0,5, das Spiel ist fair.",
    zwischenergebnis="q(x) = 210/((17 + x) · (16 + x))|q(2) = 35/57|(17 + x) · (16 + x) = 420",
    niveau_geschaetzt="III",
    fehlerquelle="beim Ziehen ohne Zurücklegen im zweiten Faktor den Nenner nicht um eins "
                 "verringern, oder die negative Lösung der quadratischen Gleichung mitnehmen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.2a", block="B", aufgabe="3.2", titel="Bildschirme", teilaufgabe="a",
    seite="10|11", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Kumulierte Wahrscheinlichkeit einer Binomialverteilung berechnen",
    typ_neben="Wahrscheinlichkeit eines Intervalls als Differenz kumulierter Werte berechnen",
    stichwoerter="Binomialverteilung|höchstens acht|Intervall|Tabelle der summierten "
                 "Binomialverteilung",
    voraussetzungen="Tabellenwerte für summierte Binomialverteilungen lesen|Ereignis in "
                    "kumulierte Wahrscheinlichkeiten übersetzen|Grenzen richtig einschließen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Tabelle",
    skizze="Anlage: Tabelle der summierten Binomialverteilung für n = 50 mit den Spalten für "
           "p von 0,05 bis 0,5 und den Zeilen k von 0 bis 37; die Werte sind auf vier "
           "Nachkommastellen gerundet und ohne die führende Null angegeben.",
    kontext="Bildschirmproduktion", textumfang="mittel",
    gegeben="Im Mittel ist einer von fünf Bildschirmen fehlerhaft, die Anzahl fehlerhafter Geräte "
            "ist binomialverteilt mit p = 0,2. Es werden 50 Bildschirme zufällig ausgewählt. "
            "Ereignis A: höchstens 8 fehlerhaft. Ereignis B: mehr als 10 und weniger als 15 "
            "fehlerhaft.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="A ist P(X ≤ 8) und wird direkt aus der Tabelle abgelesen. B ist "
              "P(11 ≤ X ≤ 14) = P(X ≤ 14) − P(X ≤ 10); beide Werte ablesen und subtrahieren.",
    schritte="3", zahlenraum="dezimal", einheiten="",
    abhaengig_von="",
    ergebnis="P(A) = P(X ≤ 8) ≈ 0,3073; P(B) = P(X ≤ 14) − P(X ≤ 10) ≈ 0,9393 − 0,5836 ≈ 0,3557.",
    zwischenergebnis="P(X ≤ 14) ≈ 0,9393|P(X ≤ 10) ≈ 0,5836",
    niveau_geschaetzt="II",
    fehlerquelle="bei mehr als 10 und weniger als 15 die Grenzen einschließen und P(X ≤ 15) − "
                 "P(X ≤ 9) rechnen",
    bemerkung="seite nennt die Aufgabenseite und die Anlage mit der Tabelle. Die Tabellenwerte "
              "stimmen mit der eigenen Rechnung überein. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.2b", block="B", aufgabe="3.2", titel="Bildschirme", teilaufgabe="b",
    seite="10", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Modalwert einer Binomialverteilung bestimmen",
    typ_neben="",
    stichwoerter="wahrscheinlichste Trefferzahl|Erwartungswert|Binomialverteilung|n gleich 250",
    voraussetzungen="Erwartungswert n · p berechnen|Einzelwahrscheinlichkeiten in der Umgebung "
                    "vergleichen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirmproduktion", textumfang="kurz",
    gegeben="Die Anzahl fehlerhafter Geräte unter 250 zufällig ausgewählten Bildschirmen ist "
            "binomialverteilt mit p = 0,2.",
    gesucht="Anzahl fehlerhafter Bildschirme, die mit der größten Wahrscheinlichkeit auftritt",
    verfahren="Den Erwartungswert 250 · 0,2 = 50 bestimmen und die Einzelwahrscheinlichkeiten in "
              "seiner Umgebung vergleichen; alternativ über (n + 1) · p = 50,2 und Abrunden.",
    schritte="2", zahlenraum="ganz|dezimal", einheiten="",
    abhaengig_von="",
    ergebnis="50 fehlerhafte Bildschirme; P(X = 50) ≈ 0,0630 ist größer als P(X = 49) und "
             "P(X = 51).",
    zwischenergebnis="n · p = 50|(n + 1) · p = 50,2",
    niveau_geschaetzt="II",
    fehlerquelle="den Erwartungswert angeben, ohne zu prüfen, ob die Nachbarwerte kleinere "
                 "Wahrscheinlichkeiten haben",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.2c", block="B", aufgabe="3.2", titel="Bildschirme", teilaufgabe="c",
    seite="10", punkte="3",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen",
    typ_neben="",
    stichwoerter="alle fehlerfrei|Stichprobe vergrößern|Potenz|Aussage beurteilen",
    voraussetzungen="Wahrscheinlichkeit für null Treffer als Potenz schreiben|Potenzen mit "
                    "Basis kleiner eins vergleichen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bildschirmproduktion", textumfang="mittel",
    gegeben="Die Anzahl fehlerhafter Bildschirme ist binomialverteilt mit p = 0,2. Zu beurteilen "
            "ist die Aussage, dass die Wahrscheinlichkeit dafür, dass alle Geräte fehlerfrei "
            "sind, geringer wird, wenn eine Stichprobe um einen zufällig ausgewählten Bildschirm "
            "ergänzt wird.",
    gesucht="Beurteilung der Aussage",
    verfahren="Bei n Geräten ist die Wahrscheinlichkeit 0,8ⁿ, bei n + 1 Geräten "
              "0,8^(n+1) = 0,8 · 0,8ⁿ. Da mit 0,8 multipliziert wird, ist der Wert kleiner; die "
              "Aussage trifft zu.",
    schritte="2", zahlenraum="dezimal|Potenz", einheiten="",
    abhaengig_von="",
    ergebnis="Die Aussage ist richtig: 0,8^(n+1) = 0,8 · 0,8ⁿ < 0,8ⁿ, die Wahrscheinlichkeit wird "
             "mit jedem weiteren Gerät um den Faktor 0,8 kleiner.",
    zwischenergebnis="",
    niveau_geschaetzt="III",
    fehlerquelle="die Aussage nur an einem Zahlenbeispiel prüfen und den allgemeinen Grund nicht "
                 "nennen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.2d", block="B", aufgabe="3.2", titel="Bildschirme", teilaufgabe="d",
    seite="10", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null "
        "Treffer bestimmen",
    typ_neben="",
    stichwoerter="Anteil fehlerhafter Geräte|kein Treffer|Wurzel ziehen|Mindestwahrscheinlichkeit",
    voraussetzungen="Ansatz (1 − p)ⁿ aufstellen|Ungleichung durch Wurzelziehen lösen|"
                    "Ergebnis als Anteil deuten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirmproduktion", textumfang="mittel",
    gegeben="Nach einer Verbesserung soll die Wahrscheinlichkeit dafür, dass unter 25 zufällig "
            "ausgewählten Bildschirmen keiner fehlerhaft ist, mindestens 10 Prozent betragen.",
    gesucht="höchster Anteil fehlerhafter Geräte nach der Verbesserung",
    verfahren="Ansatz (1 − p)²⁵ ≥ 0,1 aufstellen und die 25. Wurzel ziehen: "
              "1 − p ≥ 0,1^(1/25) ≈ 0,9120, also p ≤ 0,0880.",
    schritte="3", zahlenraum="dezimal|Prozent|Wurzel", einheiten="",
    abhaengig_von="",
    ergebnis="p ≤ 1 − 0,1^(1/25) ≈ 0,088; der Anteil fehlerhafter Geräte darf höchstens etwa "
             "8,8 Prozent betragen.",
    zwischenergebnis="0,1^(1/25) ≈ 0,91201",
    niveau_geschaetzt="II",
    fehlerquelle="beim Ziehen der Wurzel das Ungleichheitszeichen falsch umdrehen oder p und "
                 "1 − p verwechseln",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.2e", block="B", aufgabe="3.2", titel="Bildschirme", teilaufgabe="e",
    seite="10", punkte="3",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen aufstellen",
    typ_neben="",
    stichwoerter="Vierfeldertafel|Display|Netzteil|weder noch",
    voraussetzungen="Gegenwahrscheinlichkeiten bilden|Randsummen zur Ergänzung nutzen",
    format="Tabelle", operator="Stellen Sie dar", antwort="Tabelle",
    material="keins", skizze="keine", kontext="Bildschirmproduktion", textumfang="mittel",
    gegeben="Für einen zufällig ausgewählten Bildschirm gilt: das Display ist mit der "
            "Wahrscheinlichkeit 10,7 Prozent defekt, das Netzteil mit 3,0 Prozent, und mit "
            "87,3 Prozent ist weder das Display noch das Netzteil defekt.",
    gesucht="vollständig ausgefüllte Vierfeldertafel",
    verfahren="Aus dem Rand für das Display folgt der Gegenwert 89,3 Prozent; das Feld Display "
              "heil und Netzteil defekt ergibt sich als 89,3 − 87,3 = 2,0 Prozent. Damit ist das "
              "Feld Display defekt und Netzteil defekt 3,0 − 2,0 = 1,0 Prozent und das Feld "
              "Display defekt und Netzteil heil 10,7 − 1,0 = 9,7 Prozent.",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="",
    abhaengig_von="",
    ergebnis="Display und Netzteil defekt 1,0 Prozent; nur Display defekt 9,7 Prozent; nur "
             "Netzteil defekt 2,0 Prozent; keines defekt 87,3 Prozent. Ränder: Display 10,7 zu "
             "89,3 Prozent, Netzteil 3,0 zu 97,0 Prozent.",
    zwischenergebnis="Display heil 89,3 Prozent|nur Netzteil defekt 2,0 Prozent",
    niveau_geschaetzt="II",
    fehlerquelle="die 87,3 Prozent als Wahrscheinlichkeit dafür lesen, dass das Display heil ist, "
                 "statt dass beide Bauteile heil sind",
    bemerkung="Die Definition des Typs nennt Randanteile und einen Anteil innerhalb einer "
              "Teilgruppe; hier sind zwei Randanteile und ein Innenfeld gegeben. Die Definition "
              "sollte verallgemeinert werden, Vorschlag im Bericht. Eigene Rechnung, mit sympy "
              "bestätigt.")

row(id="2018-be-gk-B3.2f", block="B", aufgabe="3.2", titel="Bildschirme", teilaufgabe="f",
    seite="10", punkte="2",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus der Vierfeldertafel berechnen",
    typ_neben="",
    stichwoerter="bedingte Wahrscheinlichkeit|defektes Display|defektes Netzteil|Quotient",
    voraussetzungen="bedingte Wahrscheinlichkeit als Quotient ansetzen|Werte aus der "
                    "Vierfeldertafel entnehmen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Bildschirmproduktion", textumfang="kurz",
    gegeben="Vierfeldertafel mit den Werten: Display und Netzteil defekt 1,0 Prozent, nur Display "
            "defekt 9,7 Prozent, nur Netzteil defekt 2,0 Prozent, keines defekt 87,3 Prozent; der "
            "Rand für ein defektes Display beträgt 10,7 Prozent.",
    gesucht="Wahrscheinlichkeit dafür, dass ein Bildschirm mit defektem Display auch ein defektes "
            "Netzteil hat",
    verfahren="Den Quotienten aus dem Feld beide defekt und dem Rand defektes Display bilden: "
              "0,010 geteilt durch 0,107.",
    schritte="2", zahlenraum="dezimal|Prozent", einheiten="",
    abhaengig_von="2018-be-gk-B3.2e",
    ergebnis="P ≈ 0,0935, also etwa 9,3 Prozent.",
    zwischenergebnis="0,010 / 0,107",
    niveau_geschaetzt="II",
    fehlerquelle="durch den Rand für das defekte Netzteil statt für das defekte Display teilen "
                 "und die Bedingung damit vertauschen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-be-gk-B3.2g", block="B", aufgabe="3.2", titel="Bildschirme", teilaufgabe="g",
    seite="10", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Ungeeignetheit des Binomialmodells begründen",
    typ_neben="",
    stichwoerter="ohne Zurücklegen|Trefferwahrscheinlichkeit ändert sich|Binomialmodell|"
                 "Stichprobenumfang",
    voraussetzungen="Bedingungen einer Bernoulli-Kette kennen|Auswahl ohne Zurücklegen erkennen",
    format="Begründung", operator="Beurteilen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Bildschirmproduktion", textumfang="mittel",
    gegeben="Von vierzig geprüften Bildschirmen, unter denen sechs fehlerhaft sind, werden "
            "nacheinander zehn zufällig ausgewählt.",
    gesucht="Beurteilung, ob die Anzahl fehlerhafter Bildschirme unter den ausgewählten "
            "binomialverteilt ist",
    verfahren="Prüfen, ob die Bedingungen einer Bernoulli-Kette erfüllt sind. Es wird aus einer "
              "festen Menge ohne Zurücklegen gezogen, die Wahrscheinlichkeit für ein fehlerhaftes "
              "Gerät ändert sich also von Zug zu Zug; bei zehn aus vierzig ist der Anteil zu "
              "groß, um das zu vernachlässigen.",
    schritte="0", zahlenraum="Bruch|dezimal", einheiten="",
    abhaengig_von="",
    ergebnis="Nein. Die Auswahl erfolgt ohne Zurücklegen, die Trefferwahrscheinlichkeit bleibt "
             "also nicht bei 6/40 = 0,15, sondern hängt von den vorherigen Zügen ab; die Anzahl "
             "ist hypergeometrisch verteilt. Da ein Viertel des Bestands gezogen wird, ist auch "
             "eine Näherung durch die Binomialverteilung nicht zu rechtfertigen.",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="aus der festen Fehlerquote 6/40 auf eine konstante Trefferwahrscheinlichkeit "
                 "schließen",
    bemerkung="Zum Vergleich: die Wahrscheinlichkeit für genau zwei fehlerhafte Geräte beträgt "
              "hypergeometrisch etwa 0,321, binomial mit p = 0,15 etwa 0,276. Eigene Rechnung, "
              "mit sympy bestätigt.")


NEUE_TYPEN = [
    ("Vertikalen Abstand zweier Punkte als Differenz von Funktionswerten berechnen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Den senkrechten Abstand zweier Punkte, die dieselbe x-Koordinate haben, als Differenz der "
     "zugehörigen Funktionswerte berechnen.",
     "2018-be-gk-B1.1a"),
    ("Lage und Art aller lokalen Extrempunkte bestimmen", "Analysis", "Kurvenuntersuchung",
     "Alle Stellen mit waagerechter Tangente über die erste Ableitung bestimmen, ihre Art mit der "
     "zweiten Ableitung entscheiden und die Extrempunkte mit beiden Koordinaten angeben.",
     "2018-be-gk-B1.1c"),
    ("Extrempunkt einem Punkt im Sachzusammenhang zuordnen", "Analysis", "Kurvenuntersuchung",
     "Aus mehreren berechneten Extrempunkten denjenigen auswählen, der einem im Sachtext "
     "benannten Punkt entspricht, und die Auswahl begründen.",
     "2018-be-gk-B1.1c"),
    ("Stelle des stärksten Gefälles über die zweite Ableitung bestimmen", "Analysis",
     "Kurvenuntersuchung",
     "Die Stelle mit dem stärksten Anstieg oder Gefälle als Extremstelle der ersten Ableitung "
     "bestimmen, indem die zweite Ableitung null gesetzt wird.",
     "2018-be-gk-B1.1d"),
    ("Quadratische Funktion aus knickfreiem Übergang und einer Wertbedingung rekonstruieren",
     "Analysis", "Rekonstruktion von Funktionsgleichungen",
     "Aus der Forderung, dass zwei Graphen an einer Stelle ohne Knick ineinander übergehen, die "
     "Bedingungen gleicher Funktionswert und gleicher Anstieg gewinnen und mit einer weiteren "
     "Bedingung die Gleichung einer quadratischen Funktion bestimmen.",
     "2018-be-gk-B1.1e"),
    ("Schnittpunkt zweier Graphen über eine biquadratische Gleichung berechnen", "Analysis",
     "Gleichungen lösen",
     "Zwei Funktionsterme gleichsetzen, die entstehende Gleichung vierten Grades mit der "
     "Substitution u = x² auf eine quadratische zurückführen und die brauchbare Lösung "
     "zurücksubstituieren.",
     "2018-be-gk-B1.1f"),
    ("Graphen einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Den Verlauf einer Funktion mit Hilfe einiger berechneter Punkte in ein vorgegebenes "
     "Koordinatensystem eintragen, das bereits andere Graphen enthält.",
     "2018-be-gk-B1.1f"),
    ("Maximalen vertikalen Abstand zweier Graphen über die Differenzfunktion nachweisen",
     "Analysis", "Extremalprobleme",
     "Die Differenz zweier Funktionen als Zielfunktion aufstellen, ihre Extremstelle bestimmen "
     "und den größten vertikalen Abstand gegen eine vorgegebene Schranke prüfen.",
     "2018-be-gk-B1.1g"),
    ("Schnittwinkel zwischen Tangente und Gerade über die Anstiege berechnen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Den Anstieg der Tangente über die Ableitung bestimmen und den Winkel zur gegebenen Geraden "
     "aus beiden Anstiegen berechnen, über die Differenz der Steigungswinkel oder über die "
     "Tangensformel.",
     "2018-be-gk-B1.2b"),
    ("Stammfunktion durch Ableiten nachweisen", "Analysis", "Stammfunktion und Hauptsatz",
     "Eine vorgegebene Funktion ableiten und zeigen, dass die Ableitung mit dem gegebenen "
     "Integranden übereinstimmt.",
     "2018-be-gk-B1.2c"),
    ("Einzige Nullstelle über den positiven Exponentialfaktor nachweisen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Bei einem Produkt aus Polynom und Exponentialfunktion begründen, dass nur der Polynomfaktor "
     "null werden kann, und daraus die vollständige Nullstellenmenge angeben.",
     "2018-be-gk-B1.2c"),
    ("Hochpunkt über die notwendige Bedingung bestimmen", "Analysis", "Kurvenuntersuchung",
     "Die erste Ableitung null setzen, die Extremstelle bestimmen und den zugehörigen "
     "Funktionswert angeben, ohne die hinreichende Bedingung zu prüfen.",
     "2018-be-gk-B1.2d"),
    ("Sekantengleichung durch zwei Punkte eines Graphen ermitteln", "Analysis",
     "Ableitung und Änderungsrate",
     "Zu zwei Stellen die Funktionswerte berechnen, daraus den Anstieg der Sekante als "
     "Differenzenquotient bilden und die Geradengleichung aufstellen.",
     "2018-be-gk-B1.2e"),
    ("Unterschreiten einer Steigungsschranke über das Minimum der Ableitung nachweisen",
     "Analysis", "Ableitung und Änderungsrate",
     "Die Existenz einer Stelle mit einer Steigung unterhalb einer vorgegebenen Schranke zeigen, "
     "indem die Extremstelle der ersten Ableitung bestimmt und der dortige Wert mit der Schranke "
     "verglichen wird.",
     "2018-be-gk-B1.2f"),
    ("Mittlere Änderungsraten zweier Modelle vergleichen", "Analysis",
     "Ableitung und Änderungsrate",
     "Für zwei Funktionen auf demselben Intervall den Differenzenquotienten bilden und die "
     "Beträge der mittleren Änderungsraten vergleichen.",
     "2018-be-gk-B1.2g"),
    ("Parameter einer Exponentialfunktion aus zwei Wertepaaren bestimmen", "Analysis",
     "Rekonstruktion von Funktionsgleichungen",
     "Aus zwei gegebenen Funktionswerten die Parameter eines Terms der Form (x + a) · e^(b · x) "
     "bestimmen, wobei der zweite Parameter durch Logarithmieren gewonnen wird.",
     "2018-be-gk-B1.2g"),
    ("Punktprobe an einer Ebenengleichung durchführen", "Analytische Geometrie",
     "Lagebeziehungen",
     "Die Koordinaten eines Punktes in die Koordinatengleichung einer Ebene einsetzen und aus dem "
     "Erfülltsein der Gleichung auf die Lage in der Ebene schließen.",
     "2018-be-gk-B2.1b"),
    ("Orthogonalität zweier Ebenen über die Normalenvektoren nachweisen", "Analytische Geometrie",
     "Orthogonalität",
     "Zeigen, dass zwei Ebenen senkrecht aufeinander stehen, indem das Skalarprodukt ihrer "
     "Normalenvektoren null ergibt.",
     "2018-be-gk-B2.1b"),
    ("Existenz eines Geradenschnittpunkts über die gemeinsame Ebene begründen",
     "Analytische Geometrie", "Lagebeziehungen",
     "Begründen, dass zwei Geraden sich schneiden müssen, weil sie in einer gemeinsamen Ebene "
     "liegen und ihre Richtungsvektoren keine Vielfachen voneinander sind.",
     "2018-be-gk-B2.1c"),
    ("Geschwindigkeit aus Weg und Zeit berechnen und in Kilometer pro Stunde umrechnen",
     "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Aus einer im Koordinatensystem bestimmten Streckenlänge und der zugehörigen Zeitspanne die "
     "Geschwindigkeit berechnen und die Einheit von Metern je Sekunde in Kilometer je Stunde "
     "umrechnen.",
     "2018-be-gk-B2.1d"),
    ("Zeit bis zum Erreichen einer Ebene aus dem Geradenparameter bestimmen",
     "Analytische Geometrie", "Schnittmengen",
     "Eine geradlinige und gleichförmige Bewegung als Gerade beschreiben, den Parameter des "
     "Durchstoßpunkts mit einer Ebene bestimmen und ihn als Vielfaches der bekannten Zeitspanne "
     "in eine Zeit umrechnen.",
     "2018-be-gk-B2.1e"),
    ("Mittelpunkt einer Strecke im Raum bestimmen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Den Mittelpunkt einer Strecke als halbe Summe der Ortsvektoren ihrer Endpunkte berechnen.",
     "2018-be-gk-B2.2a"),
    ("Trapezform eines Vierecks im Raum nachweisen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Aus den Koordinaten der vier Eckpunkte nachweisen, dass ein Viereck ein Trapez ist, indem "
     "zwei Seitenvektoren als Vielfache voneinander erkannt und die Längen der übrigen Seiten "
     "verglichen werden.",
     "2018-be-gk-B2.2b"),
    ("Lage eines Punktes auf einer Strecke über die Parameterform nachweisen",
     "Analytische Geometrie", "Geraden",
     "Einen durch Koordinaten gegebenen Punkt in die Parameterform einer Strecke einsetzen, den "
     "Parameter bestimmen und prüfen, ob er zwischen null und eins liegt.",
     "2018-be-gk-B2.2d"),
    ("Schattenpunkt bei paralleler Projektion bestimmen", "Analytische Geometrie", "Schnittmengen",
     "Aus einem Punkt und seinem bekannten Schattenpunkt die Richtung der parallelen Lichtstrahlen "
     "gewinnen und damit den Schattenpunkt eines weiteren Punktes als Durchstoßpunkt mit der "
     "Grundebene berechnen.",
     "2018-be-gk-B2.2d"),
    ("Schatten einer Fläche in eine Abbildung einzeichnen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Die berechneten Schattenpunkte in ein vorgegebenes Schrägbild eintragen und zur "
     "Schattenfläche verbinden.",
     "2018-be-gk-B2.2d"),
    ("Lösungsweg zur Bestimmung eines Punktes auf einer Geraden beschreiben",
     "Analytische Geometrie", "Geraden",
     "Ohne Zahlenrechnung beschreiben, wie ein gesuchter Punkt über einen Teilpunkt, eine Gerade "
     "durch zwei Punkte und deren Schnitt mit einer weiteren Geraden bestimmt und daraus eine "
     "Länge gewonnen wird.",
     "2018-be-gk-B2.2e"),
    ("Wahrscheinlichkeit beim Ziehen ohne Zurücklegen mit der Pfadregel nachweisen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Das zweifache Ziehen ohne Zurücklegen als zweistufiges Experiment beschreiben und die "
     "Wahrscheinlichkeit eines Ergebnisses mit der Pfadmultiplikationsregel oder über "
     "Binomialkoeffizienten bestimmen.",
     "2018-be-gk-B3.1a"),
    ("Behauptung zur Monotonie einer Wahrscheinlichkeit an Beispielwerten prüfen", "Stochastik",
     "Binomialverteilung",
     "Eine Behauptung über das Wachsen oder Fallen einer von der Versuchszahl abhängigen "
     "Wahrscheinlichkeit prüfen, indem zwei Werte berechnet und verglichen werden.",
     "2018-be-gk-B3.1c"),
    ("Wahrscheinlichkeit für wenigstens einen Treffer über das Gegenereignis berechnen",
     "Stochastik", "Binomialverteilung",
     "Die Wahrscheinlichkeit für mindestens einen Treffer in einer Bernoulli-Kette als "
     "Gegenwahrscheinlichkeit zu keinem Treffer angeben.",
     "2018-be-gk-B3.1c"),
    ("Anzahl der Kugeln aus einer Fairnessbedingung bestimmen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die Gewinnwahrscheinlichkeit eines Urnenspiels in Abhängigkeit von der Zahl zugegebener "
     "Kugeln aufstellen, sie der Fairnessbedingung gleichsetzen und die entstehende quadratische "
     "Gleichung lösen.",
     "2018-be-gk-B3.1e"),
    ("Wahrscheinlichkeit eines Intervalls als Differenz kumulierter Werte berechnen", "Stochastik",
     "Binomialverteilung",
     "Ein Ereignis der Form mehr als a und weniger als b Treffer in die Differenz zweier "
     "kumulierter Wahrscheinlichkeiten übersetzen und die Grenzen dabei richtig einschließen.",
     "2018-be-gk-B3.2a"),
    ("Aussage zur Änderung einer Wahrscheinlichkeit bei größerer Stichprobe beurteilen",
     "Stochastik", "Binomialverteilung",
     "Beurteilen, wie sich eine Wahrscheinlichkeit ändert, wenn der Stichprobenumfang um eins "
     "wächst, und die Antwort allgemein über den Faktor der Potenz begründen.",
     "2018-be-gk-B3.2c"),
    ("Trefferwahrscheinlichkeit aus einer Bedingung an die Wahrscheinlichkeit für null Treffer "
     "bestimmen", "Stochastik", "Binomialverteilung",
     "Aus einer Mindestwahrscheinlichkeit für das Ausbleiben jedes Treffers die zulässige "
     "Trefferwahrscheinlichkeit bestimmen, indem der Ansatz (1 − p)ⁿ nach p aufgelöst wird.",
     "2018-be-gk-B3.2d"),
]


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
    """Feldnamen des Schemas aus dem Text nehmen. Sie sind bewusst umlautfrei und
    stehen in bemerkung als Fachwort (abhaengig_von), ohne Umschrift zu sein."""
    t = v.lower()
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


def pruefe_zeile(z, a, heftkennung=True):
    """Alle Prüfungen, die eine einzelne Zeile aus sich selbst bestehen kann."""
    i = z["id"] or "(ohne id)"
    for k in PFLICHT:
        a(z[k].strip() != "", f"{i}: Pflichtfeld leer: {k}")
    a(z["block"] in ("A", "B"), f"{i}: block muss A oder B sein")
    a(z["stern"] == "", f"{i}: stern ist im Profil abi immer leer")
    a(z["hilfsmittel"] == ("nein" if z["block"] == "A" else "ja"),
      f"{i}: hilfsmittel passt nicht zu block {z['block']}")
    if z["jahr"] <= "2018":
        a(z["afb_amtlich"] == "", f"{i}: afb_amtlich ist für {z['jahr']} nicht ausgewiesen")
    a(re.fullmatch(r"\d+\.\d+", z["aufgabe"]), f"{i}: aufgabe muss zweistufig sein (2.1)")
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
    for k, v in z.items():
        a("?" not in v or k == "bemerkung" or z["bemerkung"].strip() != "",
          f"{i}: Fragezeichen in {k} ohne Grund in bemerkung")
        a(not re.search(r"(?<=[\d\s(])-(?=\d)", v),
          f"{i}: ASCII-Bindestrich als Minus in {k}")
        if k not in OHNE_UMLAUT:
            treffer = [w for w in UMSCHRIFT if w in ohne_feldnamen(v)]
            a(not treffer, f"{i}: ASCII-Umschrift in {k}: {treffer}")


def main():
    fehler, warnung = [], []
    def a(cond, msg):
        if not cond:
            fehler.append(msg)

    _, alt_kat = lade(KAT, HEAD)
    _, alt_typ = lade(TYP, TYP_HEAD)
    alt = [dict(zip(HEAD, r)) for r in alt_kat]
    print(f"Vokabular: {len(HEAD)} Felder, {len(LEITIDEEN)} Sachgebiete, "
          f"{sum(len(v) for v in THEMEN.values())} Themen – gelesen aus {KERN} und {PROFIL}")

    # ---- Selbstprüfung: kein neues Heft, nur die vorhandenen Zeilen prüfen
    if not ZEILEN:
        for z in alt:
            a(len(z) == len(HEAD), f"{z.get('id')}: Feldzahl weicht ab")
            pruefe_zeile(z, a, heftkennung=False)
        typ_namen = {r[0] for r in alt_typ}
        benutzt = set()
        for z in alt:
            for feld in ("typ", "typ_neben"):
                for t in [s for s in z[feld].split("|") if s]:
                    benutzt.add(t)
                    a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        a(not (typ_namen - benutzt), f"Typen unbenutzt: {sorted(typ_namen - benutzt)}")
        for r in alt_typ:
            a(r[1] in THEMEN and r[2] in THEMEN.get(r[1], []),
              f"Typ {r[0]}: Sachgebiet oder Thema unbekannt")
            a(r[4] in {z["id"] for z in alt}, f"Typ {r[0]}: beispiel_id nicht im Katalog")
        if fehler:
            print(f"\nSelbstprüfung: {len(fehler)} Fehler")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        print(f"Selbstprüfung bestanden: {len(alt)} Katalogzeilen, {len(alt_typ)} Typen, "
              f"alle Typen verwendet. ZEILEN ist leer, nichts geschrieben.")
        print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
              "(Häufigkeit in Klammern):")
        liste = umschrift_liste(alt)
        print("  " + ", ".join(f"{w} ({n})" for w, n in liste) if liste else "  keines")
        return

    # ---- Normalfall: neues Heft anhängen
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

    # Punkte je Aufgabe. Kein Gesamtsoll: Wahlaufgaben.
    aufgaben = sorted({z["aufgabe"] for z in ZEILEN})
    for nr in aufgaben:
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr and z["punkte"].isdigit())
        if nr in KONFIG["soll"]:
            a(ist == KONFIG["soll"][nr], f"Aufgabe {nr}: Punkte {ist}, Soll {KONFIG['soll'][nr]}")
        else:
            warnung.append(f"Aufgabe {nr}: kein Soll in KONFIG hinterlegt, Ist {ist}")
    if "soll_teil1" in KONFIG:
        teil1 = [z for z in ZEILEN + alt
                 if z["block"] == "A" and z["papier"] == KONFIG["papier"]]
        ist1 = sum(int(z["punkte"]) for z in teil1 if z["punkte"].isdigit())
        voll = {z["aufgabe"] for z in teil1}
        if len(voll) >= 3:
            a(ist1 == KONFIG["soll_teil1"],
              f"Teil 1: Punkte {ist1}, Soll {KONFIG['soll_teil1']}")
        else:
            warnung.append(f"Teil 1 unvollständig ({len(voll)} von 3 Aufgaben), Summe {ist1}")

    verwendet = set()
    for z in ZEILEN:
        pruefe_zeile(z, a)
        for feld in ("typ", "typ_neben"):
            for t in [s for s in z[feld].split("|") if s]:
                verwendet.add(t)
                a(t in typ_namen, f"{z['id']}: Typ nicht in {TYP}: {t}")
        for dep in [s for s in z["abhaengig_von"].split("|") if s]:
            a(dep in neue_ids or dep in alt_ids, f"{z['id']}: abhaengig_von zeigt ins Leere: {dep}")
    for z in alt:
        for feld in ("typ", "typ_neben"):
            verwendet |= {s for s in z[feld].split("|") if s}
    a(not (typ_namen - verwendet), f"Typen unbenutzt: {sorted(typ_namen - verwendet)}")

    if fehler:
        print(f"ABBRUCH – {len(fehler)} Fehler, nichts geschrieben:")
        for f_ in fehler:
            print(" -", f_)
        sys.exit(1)

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
    print(f"\nHeft {KONFIG['papier']} – {len(ZEILEN)} Zeilen neu, {len(NEUE_TYPEN)} Typen neu, "
          f"Katalog jetzt {len(alt_kat) + len(ZEILEN)} Zeilen\n")
    print(f"{'id':<20} {'BE':>2}  {'thema':<38} {'typ':<46} ergebnis")
    for z in ZEILEN:
        print(f"{z['id']:<20} {z['punkte']:>2}  {z['thema']:<38} {z['typ']:<46} {z['ergebnis'][:50]}")
    print()
    for nr in aufgaben:
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        print(f"Aufgabe {nr}: Ist {ist} / Soll {KONFIG['soll'].get(nr, '–')}")
    print(f"Summe aller erfassten Zeilen: {sum(int(z['punkte']) for z in ZEILEN)} BE "
          f"(nicht die Prüfungssumme – Wahlaufgaben)")
    haupt = {z["typ"] for z in ZEILEN} | {z["typ"] for z in alt}
    neben = set()
    for z in ZEILEN + alt:
        neben |= {s for s in z["typ_neben"].split("|") if s}
    print(f"Typen: {len(haupt | neben)} gesamt, {len(neben - haupt)} nur als typ_neben")
    unsicher = [z["id"] for z in ZEILEN if any("?" in v for v in z.values())]
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    print("\nUmschrift-Sichtprüfung – jedes Wort mit ss, ae, oe oder ue "
          "(Häufigkeit in Klammern):")
    liste = umschrift_liste(ZEILEN)
    print("  " + ", ".join(f"{w} ({n})" for w, n in liste) if liste else "  keines")
    for w in warnung:
        print("Hinweis:", w)
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
