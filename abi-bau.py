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
    "jahr": "2017",
    "papier": "2017-bb-ea",
    "datei": "BB_17_Ma_Aufgaben.pdf",
    "seiten": 10,
    # Sollpunkte je Aufgabe. Teil 1 aus der gesammelten Tabelle am Ende von
    # Teil 1, Teil 2 aus der Tabelle am Ende jeder Aufgabe. Werte, die noch
    # nicht am Heft geprüft sind, weglassen – fehlende Einträge melden.
    "soll": {"1.1": 5, "1.2": 5, "1.3": 5,
             "2.1": 50, "2.2": 50, "3.1": 25, "3.2": 10, "4.1": 10, "4.2": 25},
    # Kein soll_gesamt: das Heft enthält Wahlaufgaben, die Summe aller
    # erfassten Zeilen ist deshalb größer als die 100 BE der Prüfung.
    "soll_teil1": 15,
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
# Vorlage:
#   row(id="2018-bb-ea-B2.2a", block="B", aufgabe="2.2", titel="Gartenteich",
#       teilaufgabe="a", seite="7", punkte="5",
#       leitidee="Analysis", thema="...", typ="...", typ_neben="",
#       stichwoerter="...|...", voraussetzungen="",
#       format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
#       material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
#       gegeben="...", gesucht="...", verfahren="...", schritte="3",
#       zahlenraum="dezimal", einheiten="", abhaengig_von="",
#       ergebnis="...", zwischenergebnis="",
#       niveau_geschaetzt="II", fehlerquelle="...", bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-A1.1a", block="A", aufgabe="1.1", titel="Analysis", teilaufgabe="a",
    seite="2", punkte="2",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Nullstelle einer Exponentialfunktion durch Logarithmieren bestimmen",
    typ_neben="",
    stichwoerter="Exponentialfunktion|Nullstelle|Logarithmieren|hilfsmittelfrei",
    voraussetzungen="Exponentialgleichung nach dem Exponenten auflösen|Logarithmus als "
                    "Umkehrung der Exponentialfunktion kennen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktion f mit f(x) = 2 · e^(0,5 · x) − 1; x ∈ IR.",
    gesucht="Nullstelle der Funktion f",
    verfahren="f(x) = 0 setzen, nach der Exponentialfunktion auflösen und logarithmieren: "
              "e^(0,5 · x) = 0,5, also 0,5 · x = ln 0,5.",
    schritte="3", zahlenraum="dezimal", einheiten="",
    abhaengig_von="",
    ergebnis="x = 2 · ln 0,5 = −2 · ln 2 ≈ −1,39",
    zwischenergebnis="e^(0,5 · x) = 0,5",
    niveau_geschaetzt="I",
    fehlerquelle="den Faktor 2 vor der Exponentialfunktion beim Logarithmieren mitziehen oder "
                 "den Faktor 0,5 im Exponenten vergessen",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Analysis, a) 2 BE); "
              "an der Aufgabe selbst steht keine Punktangabe. Eigene Rechnung.")

row(id="2017-bb-ea-A1.1b", block="A", aufgabe="1.1", titel="Analysis", teilaufgabe="b",
    seite="2", punkte="3",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Gleichschenkligkeit des Achsenabschnittsdreiecks einer Tangente nachweisen",
    typ_neben="Tangentengleichung an einer Stelle ermitteln",
    stichwoerter="Tangente|Achsenabschnitte|gleichschenkliges Dreieck|hilfsmittelfrei",
    voraussetzungen="Ableitung der Exponentialfunktion bilden|Punkt-Steigungs-Form aufstellen|"
                    "Achsenschnittpunkte einer Geraden bestimmen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktion f mit f(x) = 2 · e^(0,5 · x) − 1; x ∈ IR. Die Tangente an den Graphen von f "
            "im Punkt S(0 | 1) begrenzt mit den beiden Koordinatenachsen ein Dreieck.",
    gesucht="Nachweis, dass dieses Dreieck gleichschenklig ist",
    verfahren="f'(x) = e^(0,5 · x), also f'(0) = 1 und t: y = x + 1. Die Schnittpunkte der "
              "Tangente mit den Achsen sind (0 | 1) und (−1 | 0); das Dreieck ist im "
              "Koordinatenursprung rechtwinklig, seine beiden Katheten sind je 1 LE lang.",
    schritte="4", zahlenraum="ganz", einheiten="",
    abhaengig_von="",
    ergebnis="t: y = x + 1 mit den Achsenschnittpunkten (−1 | 0) und (0 | 1). Beide Katheten "
             "haben die Länge 1, das Dreieck ist also gleichschenklig (und zugleich "
             "rechtwinklig).",
    zwischenergebnis="f'(0) = 1|t: y = x + 1",
    niveau_geschaetzt="II",
    fehlerquelle="die Gleichschenkligkeit an der Zeichnung ablesen, statt die beiden "
                 "Achsenabschnitte zu berechnen und zu vergleichen",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Analysis, b) 3 BE). "
              "Eigene Rechnung.")

row(id="2017-bb-ea-A1.2a", block="A", aufgabe="1.2", titel="Analytische Geometrie",
    teilaufgabe="a", seite="2", punkte="2",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Flächeninhalt eines Dreiecks aus den Spurpunkten einer Ebene berechnen",
    typ_neben="Spurpunkte einer Ebene auf den Koordinatenachsen bestimmen",
    stichwoerter="Ebene|Spurpunkte|rechtwinkliges Dreieck|hilfsmittelfrei",
    voraussetzungen="Koordinatengleichung einer Ebene lesen|Flächenformel für das rechtwinklige "
                    "Dreieck anwenden",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Ebene E: 2x + y − 2z = −18. Der Schnittpunkt von E mit der x-Achse, der Schnittpunkt "
            "von E mit der y-Achse und der Koordinatenursprung sind die Eckpunkte eines Dreiecks.",
    gesucht="Flächeninhalt dieses Dreiecks",
    verfahren="Spurpunkte durch Nullsetzen der jeweils anderen Koordinaten bestimmen: "
              "S_x(−9 | 0 | 0) und S_y(0 | −18 | 0). Das Dreieck ist im Ursprung rechtwinklig, "
              "seine Katheten liegen auf den Achsen und sind 9 und 18 LE lang: A = 0,5 · 9 · 18.",
    schritte="3", zahlenraum="ganz|negativ", einheiten="",
    abhaengig_von="",
    ergebnis="S_x(−9 | 0 | 0), S_y(0 | −18 | 0), A = 81 FE",
    zwischenergebnis="S_x(−9 | 0 | 0)|S_y(0 | −18 | 0)",
    niveau_geschaetzt="II",
    fehlerquelle="die negativen Achsenabschnitte als negative Seitenlängen in die Flächenformel "
                 "einsetzen",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Geometrie, a) 2 BE). "
              "Eigene Rechnung.")

row(id="2017-bb-ea-A1.2b", block="A", aufgabe="1.2", titel="Analytische Geometrie",
    teilaufgabe="b", seite="2", punkte="3",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Normalenvektor als Ortsvektor eines Ebenenpunktes bestimmen",
    typ_neben="",
    stichwoerter="Normalenvektor|Ortsvektor|Punktprobe|hilfsmittelfrei",
    voraussetzungen="Normalenvektor aus der Koordinatenform ablesen|Vielfache eines Vektors "
                    "ansetzen|lineare Gleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Ebene E: 2x + y − 2z = −18.",
    gesucht="Koordinaten des Vektors, der zugleich Normalenvektor von E und Ortsvektor eines "
            "Punktes der Ebene E ist",
    verfahren="Jeder Normalenvektor ist ein Vielfaches von (2 | 1 | −2). Diesen Ansatz "
              "t · (2 | 1 | −2) als Punkt in die Ebenengleichung einsetzen: "
              "4t + t + 4t = −18, also 9t = −18.",
    schritte="3", zahlenraum="ganz|negativ", einheiten="",
    abhaengig_von="",
    ergebnis="t = −2, der gesuchte Vektor ist (−4 | −2 | 4).",
    zwischenergebnis="Ansatz t · (2 | 1 | −2)|9t = −18",
    niveau_geschaetzt="II",
    fehlerquelle="den Normalenvektor selbst einsetzen und aus dem Widerspruch schließen, es gebe "
                 "keinen solchen Vektor, statt ein Vielfaches anzusetzen",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Geometrie, b) 3 BE). "
              "Eigene Rechnung.")

row(id="2017-bb-ea-A1.3a", block="A", aufgabe="1.3", titel="Stochastik", teilaufgabe="a",
    seite="2", punkte="2",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Wahrscheinlichkeit bei zweistufigem Umlegen zwischen Urnen berechnen",
    typ_neben="",
    stichwoerter="Urnen|Umlegen|Pfadregel|Fallunterscheidung|hilfsmittelfrei",
    voraussetzungen="Pfadregeln anwenden|veränderte Urneninhalte nach dem ersten Zug "
                    "berücksichtigen",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="Figur",
    skizze="Drei nach oben offene, rechteckig gezeichnete Urnen nebeneinander, beschriftet mit "
           "Urne A, Urne B und Urne C. Urne A enthält vier Kugeln (zwei weiße, zwei schwarze), "
           "Urne B drei Kugeln (zwei weiße, eine schwarze), Urne C zwei weiße Kugeln. Schwarze "
           "Kugeln sind ausgefüllt, weiße nur umrandet gezeichnet.",
    kontext="ohne", textumfang="mittel",
    gegeben="Drei Urnen: Urne A mit zwei weißen und zwei schwarzen Kugeln, Urne B mit zwei weißen "
            "und einer schwarzen Kugel, Urne C mit zwei weißen Kugeln. Aus Urne A wird zunächst "
            "eine Kugel zufällig entnommen und in Urne B gelegt, anschließend wird aus Urne B "
            "eine Kugel zufällig entnommen und in Urne C gelegt.",
    gesucht="Wahrscheinlichkeit dafür, dass sich danach in Urne C zwei weiße und eine schwarze "
            "Kugel befinden",
    verfahren="In Urne C liegen bereits zwei weiße Kugeln; das Ereignis tritt genau dann ein, "
              "wenn die zweite gezogene Kugel schwarz ist. Zwei Pfade: Urne A liefert schwarz "
              "(Wahrscheinlichkeit 2/4), dann enthält B zwei weiße und zwei schwarze Kugeln "
              "(2/4); Urne A liefert weiß (2/4), dann enthält B drei weiße und eine schwarze "
              "Kugel (1/4). Pfadwahrscheinlichkeiten multiplizieren und addieren.",
    schritte="4", zahlenraum="Bruch", einheiten="",
    abhaengig_von="",
    ergebnis="P = 0,5 · 0,5 + 0,5 · 0,25 = 3/8 = 0,375",
    zwischenergebnis="Pfad schwarz–schwarz: 1/4|Pfad weiß–schwarz: 1/8",
    niveau_geschaetzt="II",
    fehlerquelle="übersehen, dass sich der Inhalt von Urne B durch die umgelegte Kugel ändert, "
                 "und mit unveränderten Wahrscheinlichkeiten rechnen",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Stochastik, a) "
              "2 BE). Die Urneninhalte stehen nur in der Abbildung. Eigene Rechnung.")

row(id="2017-bb-ea-A1.3b", block="A", aufgabe="1.3", titel="Stochastik", teilaufgabe="b",
    seite="2", punkte="3",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Auszahlung eines fairen Spiels aus der Fairnessbedingung bestimmen",
    typ_neben="Totale Wahrscheinlichkeit bei zufälliger Auswahl einer Urne berechnen",
    stichwoerter="Glücksspiel|faires Spiel|Erwartungswert|totale Wahrscheinlichkeit|"
                 "hilfsmittelfrei",
    voraussetzungen="Pfadregeln anwenden|Erwartungswert einer Zufallsgröße bilden|lineare "
                    "Gleichung lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur",
    skizze="Dieselbe Abbildung wie in Teilaufgabe a: drei nach oben offene Urnen nebeneinander, "
           "Urne A mit zwei weißen und zwei schwarzen, Urne B mit zwei weißen und einer "
           "schwarzen, Urne C mit zwei weißen Kugeln; schwarze Kugeln ausgefüllt, weiße "
           "umrandet.",
    kontext="Glücksspiel", textumfang="mittel",
    gegeben="Drei Urnen mit den Inhalten der Abbildung: A mit zwei weißen und zwei schwarzen, B "
            "mit zwei weißen und einer schwarzen, C mit zwei weißen Kugeln. Spielregel: Es wird "
            "ein Einsatz von 1 Euro eingezahlt, danach wird eine der drei Urnen zufällig "
            "ausgewählt und aus dieser eine Kugel zufällig gezogen. Nur bei einer schwarzen "
            "Kugel wird ein bestimmter Geldbetrag ausgezahlt.",
    gesucht="Höhe des Geldbetrags, damit Einsätze und Auszahlungen auf lange Sicht ausgeglichen "
            "sind",
    verfahren="Wahrscheinlichkeit für Schwarz über die drei gleich wahrscheinlichen Urnen: "
              "1/3 · (2/4 + 1/3 + 0) = 5/18. Fairness bedeutet, dass der erwartete Gewinn null "
              "ist: Auszahlung · 5/18 = 1 Euro.",
    schritte="4", zahlenraum="Bruch|dezimal", einheiten="Euro",
    abhaengig_von="",
    ergebnis="P(schwarz) = 5/18; die Auszahlung muss 18/5 Euro = 3,60 Euro betragen.",
    zwischenergebnis="P(schwarz) = 1/3 · (1/2 + 1/3 + 0) = 5/18",
    niveau_geschaetzt="II",
    fehlerquelle="die Wahrscheinlichkeiten der drei Urnen addieren, ohne sie vorher mit 1/3 zu "
                 "gewichten, oder die leere Urne C auslassen",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Stochastik, b) "
              "3 BE). Ausgeglichen heißt hier: erwartete Auszahlung gleich Einsatz; die "
              "Auszahlung schließt den Einsatz ein. Eigene Rechnung.")

row(id="2017-bb-ea-B2.1a", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="a",
    seite="4", punkte="8",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Definitionsbereich einer Logarithmusfunktion angeben",
    typ_neben="Gemeinsamen Punkt aller Graphen einer Schar nachweisen|Parameterwert einer Schar "
              "aus einer Funktionswertbedingung exakt bestimmen",
    stichwoerter="Logarithmusfunktion|Definitionsbereich|Funktionenschar|gemeinsamer Punkt",
    voraussetzungen="Definitionsbereich des natürlichen Logarithmus kennen|Logarithmusgleichung "
                    "exponenzieren|mit dem Parameter rechnen",
    format="Kurzantwort|Begründung|Rechnung",
    operator="Geben Sie an|Zeigen Sie|Ermitteln Sie", antwort="Term|Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktionenschar f_a mit f_a(x) = ln(a · x² + 1); a ∈ IR, a > 0. Die Graphen dieser "
            "Funktionen sind G_a.",
    gesucht="Definitionsbereich von f_a; Nachweis, dass alle Graphen G_a durch den "
            "Koordinatenursprung verlaufen; exakter Wert von a mit f_a(2) = 2",
    verfahren="Für a > 0 ist a · x² + 1 ≥ 1 > 0, der Logarithmus also für jedes x definiert. "
              "f_a(0) = ln 1 = 0 unabhängig von a. Aus ln(4a + 1) = 2 folgt durch Exponenzieren "
              "4a + 1 = e², also a = (e² − 1)/4.",
    schritte="4", zahlenraum="ganz|Potenz", einheiten="",
    abhaengig_von="",
    ergebnis="D = IR. Wegen f_a(0) = ln 1 = 0 verläuft jeder Graph G_a durch O(0 | 0). "
             "a = (e² − 1)/4 ≈ 1,597",
    zwischenergebnis="4a + 1 = e²",
    niveau_geschaetzt="II",
    fehlerquelle="den Definitionsbereich ohne Rücksicht auf a > 0 einschränken oder den exakten "
                 "Wert von a durch einen gerundeten ersetzen",
    bemerkung="Drei Leistungen in einer Einheit; thema folgt dem ersten Typ, die beiden weiteren "
              "Themen erscheinen nur über typ_neben. Eigene Rechnung.")

row(id="2017-bb-ea-B2.1b", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="b",
    seite="4", punkte="8",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gemeinsamen Extrempunkt einer Funktionenschar nachweisen",
    typ_neben="Art eines Extrempunktes über den Vorzeichenwechsel der ersten Ableitung begründen",
    stichwoerter="Funktionenschar|gemeinsamer Extrempunkt|Vorzeichenwechsel|Tiefpunkt",
    voraussetzungen="Kettenregel anwenden|Ableitung des natürlichen Logarithmus kennen|"
                    "Vorzeichenwechselkriterium kennen",
    format="Begründung|Rechnung", operator="Zeigen Sie|Begründen Sie", antwort="Text|Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktionenschar f_a mit f_a(x) = ln(a · x² + 1); a ∈ IR, a > 0, mit den Graphen G_a.",
    gesucht="Nachweis, dass alle Graphen G_a einen gemeinsamen lokalen Extrempunkt haben; "
            "Begründung ohne Zuhilfenahme der zweiten Ableitung, dass dieser Extrempunkt für "
            "a > 0 ein Tiefpunkt ist",
    verfahren="f_a'(x) = 2a · x / (a · x² + 1). Der Nenner ist stets positiv, also ist x = 0 für "
              "jedes a die einzige Nullstelle der Ableitung; f_a(0) = 0 liefert für alle Graphen "
              "denselben Punkt. Der Zähler 2a · x wechselt bei a > 0 an der Stelle 0 das "
              "Vorzeichen von minus nach plus, also liegt ein Tiefpunkt vor.",
    schritte="4", zahlenraum="ganz", einheiten="",
    abhaengig_von="",
    ergebnis="f_a'(x) = 2a · x / (a · x² + 1) mit der einzigen Nullstelle x = 0 und f_a(0) = 0: "
             "alle Graphen haben den gemeinsamen Extrempunkt T(0 | 0). Für x < 0 ist "
             "f_a'(x) < 0, für x > 0 ist f_a'(x) > 0 – Vorzeichenwechsel von minus nach plus, "
             "also ein Tiefpunkt.",
    zwischenergebnis="f_a'(x) = 2a · x / (a · x² + 1)|f_a(0) = 0",
    niveau_geschaetzt="II",
    fehlerquelle="den Nenner als möglichen Nullfaktor behandeln oder die geforderte Begründung "
                 "doch über die zweite Ableitung führen",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B2.1c", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="c",
    seite="4", punkte="14",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Schranke für den Anstieg der Tangenten einer Schar begründen",
    typ_neben="Tangentengleichung an einer Stelle ermitteln|Normalengleichung an einer Stelle "
              "ermitteln|Flächeninhalt des von Tangente, Normale und y-Achse begrenzten Dreiecks "
              "berechnen",
    stichwoerter="Tangentenschar|Anstiegsschranke|Normale|Dreiecksfläche",
    voraussetzungen="Ableitung einer Schar bilden|Term durch Polynomdivision oder Umformen "
                    "abschätzen|Normale als Gerade mit dem negativen Kehrwert des Anstiegs "
                    "aufstellen",
    format="Begründung|Rechnung", operator="Begründen Sie|Ermitteln Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben="Funktionenschar f_a mit f_a(x) = ln(a · x² + 1), a > 0. Die Tangenten an G_a im "
            "Punkt B_a(1 | f_a(1)) sind t_a. Für a = 1 ist f_1(x) = ln(x² + 1) mit "
            "B_1(1 | ln 2). [Kontrollergebnis: t_1: y = x + ln 2 − 1]",
    gesucht="Begründung, dass keine der Tangenten t_a einen Anstieg größer als 2 haben kann; "
            "Flächeninhalt des Dreiecks, das von der y-Achse sowie der Tangente und der Normalen "
            "an G_1 im Punkt B_1 begrenzt wird",
    verfahren="Anstieg m(a) = f_a'(1) = 2a/(a + 1) = 2 − 2/(a + 1); für a > 0 ist der "
              "Subtrahend positiv, also m(a) < 2. Für a = 1 ist m = 1, damit t_1: y = x + ln 2 − 1 "
              "und n_1: y = −x + ln 2 + 1. Beide Geraden schneiden die y-Achse in ln 2 − 1 und "
              "ln 2 + 1; die Grundseite auf der y-Achse ist 2 LE lang, die zugehörige Höhe ist "
              "der x-Abstand 1 des Punktes B_1.",
    schritte="7", zahlenraum="ganz", einheiten="",
    abhaengig_von="",
    ergebnis="m(a) = 2a/(a + 1) = 2 − 2/(a + 1) < 2 für alle a > 0, der Anstieg bleibt also "
             "stets unter 2. t_1: y = x + ln 2 − 1, n_1: y = −x + ln 2 + 1; das Dreieck hat die "
             "Grundseite 2 und die Höhe 1, sein Flächeninhalt ist A = 1 FE.",
    zwischenergebnis="m(a) = 2a/(a + 1)|t_1: y = x + ln 2 − 1|n_1: y = −x + ln 2 + 1|"
                     "Achsenschnittpunkte (0 | ln 2 − 1) und (0 | ln 2 + 1)",
    niveau_geschaetzt="III",
    fehlerquelle="den Grenzwert 2 des Anstiegs als angenommenen Wert deuten statt als obere "
                 "Schranke, oder bei der Dreiecksfläche die Grundseite auf der y-Achse mit der "
                 "Höhe verwechseln",
    bemerkung="Das Kontrollergebnis t_1 ist im Heft abgedruckt und durch eigene Rechnung "
              "bestätigt. Mit 14 BE die umfangreichste Teilaufgabe des Hefts. Eigene Rechnung.")

row(id="2017-bb-ea-B2.1d", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="d",
    seite="4", punkte="4",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Umbeschriebenes Prisma zu einem Rotationskörper bestimmen",
    typ_neben="",
    stichwoerter="Rotationskörper|maximaler Radius|Verpackung|Maßstab",
    voraussetzungen="Randwerte einer Funktion berechnen|Längenmaßstab 1 LE = 4 cm anwenden|"
                    "Durchmesser aus dem Radius bilden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur",
    skizze="Halber Längsquerschnitt eines Eisbechers im ersten Quadranten: zwei von links unten "
           "nach rechts oben verlaufende Kurven, innen der Graph G_h, außen der Graph G_k; die "
           "dunkel getönte Fläche zwischen beiden ist die Becherwand, die hellere Fläche links "
           "davon der Innenraum. Unten sitzt zwischen x-Achse und der Parabel p der Fuß. Auf der "
           "x-Achse ist 1 beschriftet, auf der y-Achse 1 und 2; rechts begrenzt eine gestrichelte "
           "Senkrechte bei x = 1,5 die Fläche.",
    kontext="Verpackung / Eisbecher", textumfang="lang",
    gegeben="Der halbe Längsquerschnitt eines Eisbechers wird im Intervall [0; 1,5] durch Teile "
            "der Graphen von h mit h(x) = 0,75 · f_2(x) + 1 = 0,75 · ln(2x² + 1) + 1 und von k "
            "mit k(x) = 1,75 · ln(2,5x + 1) − 0,5, eine zur y-Achse symmetrische quadratische "
            "Parabel p und die beiden Koordinatenachsen begrenzt. Der Eisbecher entsteht durch "
            "Rotation dieser Fläche um die y-Achse, 1 LE = 4 cm. Je zwölf Eisbecher werden "
            "stehend in einem quaderförmigen Karton mit zwölf gleich großen quaderförmigen "
            "Fächern verpackt.",
    gesucht="Kantenlängen, die ein Fach für einen stehenden Eisbecher mindestens haben muss",
    verfahren="Der größte Radius des Rotationskörpers ist der Randwert x = 1,5 LE, also 6 cm; die "
              "Grundfläche eines Fachs muss deshalb mindestens 12 cm mal 12 cm messen. Die Höhe "
              "ist der größte Funktionswert am rechten Rand: h(1,5) = 0,75 · ln 5,5 + 1.",
    schritte="4", zahlenraum="dezimal", einheiten="cm",
    abhaengig_von="",
    ergebnis="Ein Fach muss mindestens 12 cm mal 12 cm messen und rund 9,2 cm hoch sein "
             "(Radius 1,5 LE = 6 cm; Höhe h(1,5) ≈ 2,279 LE ≈ 9,11 cm).",
    zwischenergebnis="h(1,5) = 0,75 · ln 5,5 + 1 ≈ 2,279|Durchmesser 2 · 1,5 LE = 12 cm",
    niveau_geschaetzt="II",
    fehlerquelle="den Radius statt des Durchmessers als Kantenlänge nehmen oder die Umrechnung "
                 "1 LE = 4 cm vergessen",
    bemerkung="Die Becherhöhe ist der Funktionswert von h am Rand x = 1,5, nicht der von k "
              "(k(1,5) ≈ 2,227). Der vorhandene Typ ist übernommen; seine Definition nennt "
              "bislang nur Grundfläche und Mindestvolumen, hier sind es Grundfläche und Höhe. "
              "Eigene Rechnung.")

row(id="2017-bb-ea-B2.1e", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="e",
    seite="4", punkte="9",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Parabelgleichung aus Symmetrie und einer Flächenbedingung rekonstruieren",
    typ_neben="",
    stichwoerter="Parabel|Symmetrie|Flächenbedingung|Maßstab|Rekonstruktion",
    voraussetzungen="Integral einer quadratischen Funktion bilden|Flächenmaßstab 1 FE = 16 cm² "
                    "anwenden|Ansatz mit Symmetrie verkürzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="Figur",
    skizze="Im halben Längsquerschnitt des Eisbechers liegt unten am Fuß die zur y-Achse "
           "symmetrische Parabel p; die dunkel getönte Fläche zwischen ihr und der x-Achse reicht "
           "von der y-Achse bis zur Nullstelle der Parabel bei x = 1 und ist am linken Rand "
           "0,2 LE hoch.",
    kontext="Verpackung / Eisbecher", textumfang="mittel",
    gegeben="Der Fuß des Eisbechers, dessen oberer Rand im Querschnitt durch die zur y-Achse "
            "symmetrische quadratische Parabel p modelliert wird, hat am Boden einen Durchmesser "
            "von 8 cm und eine Querschnittsfläche von 64/15 cm². Es gilt 1 LE = 4 cm. "
            "[Kontrollergebnis: p(x) = −0,2x² + 0,2]",
    gesucht="Gleichung der Parabel p",
    verfahren="Symmetrie zur y-Achse liefert den Ansatz p(x) = a · x² + c. Der Durchmesser 8 cm "
              "entspricht 2 LE, also ist p(1) = 0 und damit a = −c, das heißt "
              "p(x) = c · (1 − x²). Die Querschnittsfläche 64/15 cm² entspricht wegen "
              "1 FE = 16 cm² genau 4/15 FE. Aus dem Integral von −1 bis 1 über c · (1 − x²) "
              "folgt 4c/3 = 4/15.",
    schritte="5", zahlenraum="dezimal|Bruch", einheiten="cm|cm²",
    abhaengig_von="",
    ergebnis="c = 0,2, also p(x) = −0,2x² + 0,2",
    zwischenergebnis="Ansatz p(x) = c · (1 − x²)|Fläche in Flächeneinheiten: 4c/3|"
                     "64/15 cm² = 4/15 FE",
    niveau_geschaetzt="III",
    fehlerquelle="die Querschnittsfläche ohne die Umrechnung 1 FE = 16 cm² einsetzen oder nur "
                 "die halbe Fläche von 0 bis 1 ansetzen",
    bemerkung="Das Kontrollergebnis ist im Heft abgedruckt und durch eigene Rechnung bestätigt; "
              "die Bestätigung gelingt nur mit der vollen Querschnittsfläche von −1 bis 1. "
              "Eigene Rechnung.")

row(id="2017-bb-ea-B2.1f", block="B", aufgabe="2.1", titel="Eisbecher", teilaufgabe="f",
    seite="4", punkte="7",
    leitidee="Analysis", thema="Rotationsvolumen",
    typ="Fehlerhaftes Verfahren zur Volumenberechnung beurteilen und berichtigen",
    typ_neben="Rotationsvolumen um die y-Achse über die Umkehrfunktion aufstellen|"
              "Volumenmaßstab zwischen Modell und Wirklichkeit umrechnen",
    stichwoerter="Rotation um die y-Achse|Volumenmaßstab|Dichte|Fehleranalyse",
    voraussetzungen="Formel für das Rotationsvolumen um die y-Achse kennen|Umkehrung einer "
                    "Parabel bilden|Masse als Produkt aus Volumen und Dichte kennen",
    format="Begründung", operator="Beurteilen Sie|Beschreiben Sie", antwort="Text",
    material="keins",
    skizze="Im Heft ist zu dieser Teilaufgabe keine Abbildung vorgegeben; eine Skizze ist "
           "ausdrücklich freigestellt. Sinnvoll ist der Fuß als Rotationskörper um die y-Achse "
           "mit der Parabel p als oberem Rand und einer waagerechten Scheibe der Dicke Δy mit "
           "dem Radius x(y).",
    kontext="Verpackung / Eisbecher", textumfang="lang",
    gegeben="Der Fuß des Eisbechers entsteht durch Rotation der Fläche zwischen der Parabel p mit "
            "p(x) = −0,2x² + 0,2 und der x-Achse um die y-Achse; es gilt 1 LE = 4 cm. Zur "
            "Berechnung der Masse des Fußes geht ein Schüler so vor: (1) Volumen in VE über "
            "V = π · Integral von 0 bis 1 über (p(x))² dx; (2) Umwandeln in cm³ über den Ansatz "
            "1 VE / 4 cm³ = V / V(cm³); (3) Multiplizieren des erhaltenen Wertes mit der Dichte "
            "des Materials.",
    gesucht="Beurteilung der drei Teilschritte jeweils einzeln und Beschreibung, wie fehlerhafte "
            "Schritte zu berichtigen sind",
    verfahren="Schritt 1 gehört zur Rotation um die x-Achse. Bei Rotation um die y-Achse ist über "
              "y zu integrieren: aus y = −0,2x² + 0,2 folgt x² = 1 − 5y, also "
              "V = π · Integral von 0 bis 0,2 über (1 − 5y) dy. Schritt 2 überträgt den "
              "Längenmaßstab ohne Potenzierung: aus 1 LE = 4 cm folgt 1 VE = 4³ cm³ = 64 cm³. "
              "Schritt 3 ist richtig, sofern Volumen und Dichte in zueinander passenden "
              "Einheiten stehen.",
    schritte="5", zahlenraum="dezimal|Potenz", einheiten="cm³",
    abhaengig_von="2017-bb-ea-B2.1e",
    ergebnis="(1) falsch – die Rotation um die y-Achse verlangt "
             "V = π · Integral von 0 bis 0,2 über (1 − 5y) dy = 0,1 · π VE ≈ 0,314 VE. "
             "(2) falsch – es gilt 1 VE = 64 cm³, nicht 4 cm³; der Wert ist mit 64 zu "
             "multiplizieren, hier also rund 20,1 cm³. (3) richtig – die Masse ist das Produkt "
             "aus Volumen und Dichte, wenn die Einheiten zusammenpassen.",
    zwischenergebnis="x² = 1 − 5y|V = 0,1 · π VE ≈ 0,314 VE|V ≈ 20,1 cm³",
    niveau_geschaetzt="III",
    fehlerquelle="die Rotationsachse nicht prüfen und den Ansatz für die x-Achse übernehmen, oder "
                 "den Längenmaßstab ohne dritte Potenz auf das Volumen übertragen",
    bemerkung="Die Zahlenwerte 0,314 VE und 20,1 cm³ sind eigene Rechnung; das Heft verlangt nur "
              "die Beurteilung und die Berichtigung. Das Feld skizze beschreibt eine "
              "freigestellte, vom Prüfling zu erstellende Darstellung, nicht vorhandenes "
              "Aufgabenmaterial. Eigene Rechnung.")

row(id="2017-bb-ea-B2.2a", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="a",
    seite="5", punkte="6",
    leitidee="Analysis", thema="Grenzwerte und Verhalten im Unendlichen",
    typ="Grenzverhalten einer Exponentialfunktion untersuchen",
    typ_neben="Nullstellenfreiheit über das Vorzeichen des Funktionsterms begründen|"
              "Achsensymmetrie am Funktionsterm nachweisen",
    stichwoerter="Funktionenschar|Grenzverhalten|Nullstellenfreiheit|Achsensymmetrie",
    voraussetzungen="Verhalten der Exponentialfunktion für große und kleine Argumente kennen|"
                    "Symmetriekriterium f(−x) = f(x) anwenden",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie|Weisen Sie nach",
    antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktionenschar f_a mit f_a(x) = e^(2ax) + e^(−2ax); x ∈ IR, a ∈ IR, a ≠ 0. Die "
            "zugehörigen Graphen sind G_a.",
    gesucht="Verhalten der Funktionswerte für a > 0 bei x → +∞ und bei x → −∞; Begründung, dass "
            "keine Funktion f_a eine Nullstelle hat; Nachweis, dass alle Graphen G_a "
            "achsensymmetrisch zur y-Achse verlaufen",
    verfahren="Für a > 0 wächst e^(2ax) bei x → +∞ unbeschränkt, während e^(−2ax) gegen null "
              "geht; bei x → −∞ vertauschen sich die Rollen. Beide Summanden sind stets positiv, "
              "also ist f_a(x) > 0. Für die Symmetrie f_a(−x) bilden und mit f_a(x) vergleichen.",
    schritte="4", zahlenraum="ganz|Potenz", einheiten="",
    abhaengig_von="",
    ergebnis="Für a > 0 gilt f_a(x) → +∞ sowohl für x → +∞ als auch für x → −∞. Als Summe zweier "
             "stets positiver Exponentialterme ist f_a(x) > 0, es gibt also keine Nullstelle. "
             "Wegen f_a(−x) = e^(−2ax) + e^(2ax) = f_a(x) ist jeder Graph achsensymmetrisch zur "
             "y-Achse.",
    zwischenergebnis="f_a(−x) = e^(−2ax) + e^(2ax)",
    niveau_geschaetzt="II",
    fehlerquelle="beim Grenzverhalten nur den wachsenden Summanden betrachten und das Vorzeichen "
                 "von a außer Acht lassen",
    bemerkung="Drei Leistungen in einer Einheit; thema folgt dem ersten Typ. Eigene Rechnung.")

row(id="2017-bb-ea-B2.2b", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="b",
    seite="5", punkte="10",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Gemeinsamen Extrempunkt einer Funktionenschar nachweisen",
    typ_neben="Art eines Extrempunktes über die zweite Ableitung bestimmen|Fehlen von "
              "Wendepunkten über die zweite Ableitung nachweisen",
    stichwoerter="Funktionenschar|gemeinsamer Tiefpunkt|zweite Ableitung|Wendepunkte",
    voraussetzungen="Ableitung von Exponentialfunktionen mit Kettenregel bilden|Exponential"
                    "gleichung lösen|hinreichendes Kriterium für Extrem- und Wendestellen kennen",
    format="Rechnung|Begründung", operator="Zeigen Sie|Ermitteln Sie|Untersuchen Sie",
    antwort="Term|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="Funktionenschar f_a mit f_a(x) = e^(2ax) + e^(−2ax); x ∈ IR, a ∈ IR, a ≠ 0, mit den "
            "Graphen G_a.",
    gesucht="Nachweis, dass alle Graphen G_a denselben lokalen Extrempunkt besitzen; dessen Art "
            "und Koordinaten; Untersuchung auf mögliche Wendepunkte",
    verfahren="f_a'(x) = 2a · (e^(2ax) − e^(−2ax)); Nullsetzen führt auf e^(4ax) = 1 und damit "
              "auf x = 0 für jedes a, mit f_a(0) = 2. f_a''(x) = 4a² · (e^(2ax) + e^(−2ax)) ist "
              "für a ≠ 0 stets positiv: an der Stelle 0 liegt ein Tiefpunkt, und weil die zweite "
              "Ableitung nirgends null wird, gibt es keine Wendepunkte.",
    schritte="6", zahlenraum="ganz|Potenz", einheiten="",
    abhaengig_von="",
    ergebnis="Alle Graphen haben den gemeinsamen Tiefpunkt T(0 | 2). Wegen "
             "f_a''(x) = 4a² · f_a(x) > 0 für alle x besitzt kein Graph G_a einen Wendepunkt.",
    zwischenergebnis="f_a'(x) = 2a · (e^(2ax) − e^(−2ax))|e^(4ax) = 1|f_a''(x) = 4a² · f_a(x)",
    niveau_geschaetzt="II",
    fehlerquelle="aus e^(4ax) = 1 auf 4ax = 1 statt auf 4ax = 0 schließen oder die Wendepunkte "
                 "nur an einem Beispielgraphen prüfen",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B2.2c", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="c",
    seite="5|6", punkte="9",
    leitidee="Analysis", thema="Extremalprobleme",
    typ="Dreieck zu Schnittpunkten mit einer Parallelen zur x-Achse einzeichnen",
    typ_neben="Existenz eines Flächenmaximums ohne Rechnung begründen|Zielfunktion für den "
              "Flächeninhalt eines Dreiecks aufstellen",
    stichwoerter="Parallele zur x-Achse|Dreieck|Zielfunktion|Randverhalten|Maximum",
    voraussetzungen="Achsensymmetrie des Graphen nutzen|Flächenformel für das Dreieck anwenden|"
                    "offene und abgeschlossene Intervalle unterscheiden",
    format="Zeichnen|Begründung|Rechnung",
    operator="Zeichnen Sie ein|Begründen Sie|Ermitteln Sie", antwort="Grafik|Text|Term",
    material="Koordinatensystem",
    skizze="Vorgegeben ist ein Koordinatensystem von x = −6 bis 6 und y = 0 bis etwa 7,5 mit dem "
           "bereits eingezeichneten Graphen G_0,15: eine nach oben geöffnete, zur y-Achse "
           "symmetrische Kurve mit dem Tiefpunkt (0 | 2), die am Rand bei x = ±6 etwa den Wert "
           "7,3 erreicht, beschriftet mit G_0,15. Einzuzeichnen sind eine Parallele zur x-Achse "
           "y = k mit 2 < k < 6, deren beide Schnittpunkte A_k und B_k mit dem Graphen und das "
           "Dreieck A_k B_k C mit C(0 | 6).",
    kontext="ohne", textumfang="lang",
    gegeben="Funktionenschar f_a mit f_a(x) = e^(2ax) + e^(−2ax); für a = 0,15 ist "
            "f_0,15(x) = e^(0,3x) + e^(−0,3x) mit dem Graphen G_0,15. Dieser wird von den "
            "Parallelen zur x-Achse mit der Gleichung y = k; 2 < k < 6 in den Punkten A_k und "
            "B_k geschnitten. A_k, B_k und der Punkt C(0 | 6) bilden ein Dreieck. Ein "
            "Koordinatensystem mit dem Graphen G_0,15 ist auf der Folgeseite abgedruckt.",
    gesucht="Zeichnung eines der möglichen Dreiecke A_k B_k C; Begründung ohne Rechnung, dass "
            "keines der Dreiecke einen minimalen Flächeninhalt haben kann, wohl aber eines einen "
            "maximalen; Gleichung für den Flächeninhalt in Abhängigkeit vom x-Wert des im "
            "I. Quadranten liegenden Eckpunktes",
    verfahren="Wegen der Achsensymmetrie liegen A_k und B_k spiegelbildlich zur y-Achse: ist u "
              "der x-Wert des Eckpunktes im I. Quadranten, so ist die Grundseite 2u lang und die "
              "Höhe 6 − k = 6 − f_0,15(u). Für k gegen 2 schrumpft die Grundseite, für k gegen 6 "
              "die Höhe gegen null; da beide Randwerte wegen 2 < k < 6 nicht angenommen werden, "
              "gibt es kein kleinstes Dreieck, wegen der Stetigkeit im Inneren aber ein größtes.",
    schritte="5", zahlenraum="dezimal|Potenz", einheiten="",
    abhaengig_von="",
    ergebnis="A(u) = u · (6 − e^(0,3u) − e^(−0,3u)). Ein minimaler Flächeninhalt existiert nicht, "
             "weil die Fläche an den offenen Rändern k → 2 und k → 6 beliebig klein wird, ohne "
             "den Wert null anzunehmen; ein maximaler Flächeninhalt existiert, weil die Fläche "
             "im offenen Inneren stetig und positiv ist und zu beiden Rändern hin abfällt.",
    zwischenergebnis="Grundseite A_k B_k = 2u|Höhe 6 − f_0,15(u)",
    niveau_geschaetzt="III",
    fehlerquelle="die Randfälle k = 2 und k = 6 als mögliche Dreiecke zulassen und daraus auf ein "
                 "Minimum schließen",
    bemerkung="Das Koordinatensystem steht auf der folgenden Seite; seite nennt Aufgabenseite "
              "und Anlage. Das Feld skizze beschreibt sowohl das vorgegebene Material als auch "
              "die zu erstellende Zeichnung. Zur Einordnung: das Maximum liegt bei u ≈ 3,56 mit "
              "A ≈ 9,78 FE, im Heft ist es nicht gefordert. Das Einzeichnen hat in der "
              "Themenliste Analysis kein eigenes Thema; ersatzweise Extremalprobleme. Eigene "
              "Rechnung.")

row(id="2017-bb-ea-B2.2d", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="d",
    seite="5", punkte="6",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Näherungsweise tangentiale Einmündung einer Geraden nachweisen",
    typ_neben="",
    stichwoerter="knickfreier Anschluss|Tangente|Näherung|Modellierung",
    voraussetzungen="Funktionswert und Ableitungswert an einer Stelle berechnen|Bedingungen für "
                    "eine Tangente kennen",
    format="Rechnung|Begründung", operator="Zeigen Sie", antwort="Text|Zahl",
    material="keins", skizze="keine", kontext="Straßenbau", textumfang="mittel",
    gegeben="Für diese Teilaufgabe gilt 1 LE = 150 m. Eine langgezogene Kurve auf einer "
            "Landstraße wird im Intervall [−2; 4] näherungsweise durch den Graphen G_0,15 von "
            "f_0,15(x) = e^(0,3x) + e^(−0,3x) modelliert. Im Punkt P(4 | f_0,15(4)) mündet sie "
            "tangential, also ohne Knick, in eine zunächst geradlinig verlaufende Schnellstraße.",
    gesucht="Nachweis, dass ein Teil der Schnellstraße für x ≥ 4 näherungsweise durch einen Teil "
            "der Geraden g mit y = 0,9x modelliert werden kann",
    verfahren="Funktionswert und Anstieg an der Stelle 4 mit den Werten der Geraden vergleichen: "
              "f_0,15(4) = e^(1,2) + e^(−1,2) gegen g(4) = 3,6 sowie "
              "f_0,15'(4) = 0,3 · (e^(1,2) − e^(−1,2)) gegen den Anstieg 0,9.",
    schritte="4", zahlenraum="dezimal|Potenz", einheiten="m",
    abhaengig_von="",
    ergebnis="f_0,15(4) ≈ 3,621 gegenüber g(4) = 3,6 und f_0,15'(4) ≈ 0,906 gegenüber dem "
             "Anstieg 0,9: Berührpunkt und Anstieg stimmen bis auf wenige Tausendstel überein, "
             "die Gerade ist also eine geeignete Näherung.",
    zwischenergebnis="f_0,15(4) ≈ 3,6213|f_0,15'(4) ≈ 0,9057",
    niveau_geschaetzt="II",
    fehlerquelle="nur den Funktionswert vergleichen und die Übereinstimmung der Anstiege nicht "
                 "prüfen",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B2.2e", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="e",
    seite="5", punkte="10",
    leitidee="Analysis", thema="Gleichungen lösen",
    typ="Punkt in vorgegebener Entfernung auf einer Geraden bestimmen",
    typ_neben="Gleichungssystem zur Bestimmung einer Parabelgleichung aufstellen",
    stichwoerter="Streckenlänge|Maßstab|knickfreier Übergang|Gleichungssystem|Parabel",
    voraussetzungen="Satz des Pythagoras in der Ebene anwenden|Maßstab 1 LE = 150 m umrechnen|"
                    "Bedingungen für Punkt und Anstieg in Gleichungen übersetzen",
    format="Rechnung", operator="Ermitteln Sie|Stellen Sie auf", antwort="Zahl|Term",
    material="keins", skizze="keine", kontext="Straßenbau", textumfang="lang",
    gegeben="Es gilt 1 LE = 150 m. Die Schnellstraße verläuft ab dem Punkt P(4 | 3,6) entlang der "
            "Geraden g mit y = 0,9x über eine Strecke von 2,1 km geradlinig bis zum Punkt S und "
            "führt dann knickfrei durch eine scharfe Rechtskurve auf eine Bundesstraße. Die "
            "Rechtskurve wird durch eine quadratische Parabel beschrieben, auf der unter anderem "
            "der Punkt Q(15,5 | 13,3) liegt. [Zur Kontrolle: S(14,4 | 13)]",
    gesucht="Koordinaten des Punktes S; Gleichungssystem zur Ermittlung der Parabelgleichung",
    verfahren="2,1 km entsprechen 14 LE. Von P aus in Richtung (1 | 0,9) weitergehen: die Länge "
              "14 verteilt sich auf Δx = 14 / √(1 + 0,81) und Δy = 0,9 · Δx; daraus folgen die "
              "Koordinaten von S. Für die Parabel y = ax² + bx + c drei Bedingungen aufstellen: "
              "Punkt S, Punkt Q und knickfreier Anschluss, also Anstieg 0,9 an der Stelle 14,4.",
    schritte="6", zahlenraum="dezimal|Wurzel", einheiten="m|km",
    abhaengig_von="2017-bb-ea-B2.2d",
    ergebnis="S(14,4 | 13) – eigene Rechnung liefert (14,406 | 12,966). Gleichungssystem: "
             "207,36a + 14,4b + c = 13; 240,25a + 15,5b + c = 13,3; 28,8a + b = 0,9.",
    zwischenergebnis="2,1 km = 14 LE|Δx = 14/√1,81 ≈ 10,406",
    niveau_geschaetzt="III",
    fehlerquelle="die Streckenlänge 14 LE als Zuwachs in x-Richtung nehmen, statt sie über den "
                 "Pythagoras auf Δx und Δy aufzuteilen",
    bemerkung="Die Kontrollangabe S(14,4 | 13) ist im Heft abgedruckt und durch eigene Rechnung "
              "bestätigt; sie ist gerundet. Das Gleichungssystem ist nur aufzustellen, nicht zu "
              "lösen. Eigene Rechnung.")

row(id="2017-bb-ea-B2.2f", block="B", aufgabe="2.2", titel="Straßenverlauf", teilaufgabe="f",
    seite="6", punkte="9",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Abschnittsweise begrenzte Fläche durch Integration berechnen",
    typ_neben="Flächenmaßstab eines Modells auf eine Realfläche anwenden",
    stichwoerter="Integral|abschnittsweise Berandung|Flächenmaßstab|Hektar",
    voraussetzungen="Stammfunktion von Exponentialfunktionen bilden|Integral einer linearen "
                    "Funktion berechnen|Prozentanteil bilden|1 ha = 10 000 m² kennen",
    format="Rechnung", operator="Ermitteln Sie|Geben Sie an", antwort="Zahl",
    material="keins", skizze="keine", kontext="Landwirtschaft", textumfang="mittel",
    gegeben="Es gilt 1 LE = 150 m. Die Landstraße wird für 0 ≤ x ≤ 4 durch den Graphen von "
            "f_0,15(x) = e^(0,3x) + e^(−0,3x) modelliert, die Schnellstraße für x ≥ 4 durch die "
            "Gerade y = 0,9x. Die von den beiden Koordinatenachsen, der Landstraße, der "
            "Schnellstraße und der Geraden x = 7 eingeschlossene Fläche nutzt ein Landwirt zu "
            "80 % für den Anbau von Getreide.",
    gesucht="Größe der Getreideanbaufläche in Hektar",
    verfahren="Die Fläche in zwei Abschnitten integrieren: von 0 bis 4 unter dem Graphen von "
              "f_0,15 mit der Stammfunktion (10/3) · (e^(0,3x) − e^(−0,3x)), von 4 bis 7 unter "
              "der Geraden. Die Summe mit 1 FE = 150² m² = 22 500 m² in Quadratmeter umrechnen "
              "und davon 80 % nehmen.",
    schritte="6", zahlenraum="dezimal|Prozent|Potenz", einheiten="m²|ha",
    abhaengig_von="2017-bb-ea-B2.2d",
    ergebnis="Integral von 0 bis 4 ≈ 10,063 FE, Integral von 4 bis 7 = 14,85 FE, zusammen "
             "≈ 24,913 FE ≈ 560 544 m². Davon 80 % sind rund 448 435 m², also etwa 44,8 ha.",
    zwischenergebnis="Integral von 0 bis 4 ≈ 10,063|Integral von 4 bis 7 = 14,85|"
                     "Gesamtfläche ≈ 24,913 FE",
    niveau_geschaetzt="II",
    fehlerquelle="den Flächenmaßstab mit 150 statt mit 150² ansetzen oder die Umrechnung von "
                 "Quadratmetern in Hektar vergessen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2017-bb-ea-B3.1a", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="a",
    seite="7", punkte="5",
    leitidee="Analytische Geometrie", thema="Punkte und Strecken im Koordinatensystem",
    typ="Koordinaten der Eckpunkte einer Pyramide aus der Beschreibung angeben",
    typ_neben="Mittelpunkt eines Quadrates als Diagonalenmittelpunkt bestimmen|Körper in ein "
              "räumliches Koordinatensystem einzeichnen",
    stichwoerter="Pyramide|quadratische Grundfläche|Spitze|Schrägbild",
    voraussetzungen="Lage von Punkten auf den Koordinatenachsen lesen|Mittelpunkt einer Strecke "
                    "berechnen|räumliches Koordinatensystem zeichnen",
    format="Kurzantwort|Zeichnen", operator="Geben Sie an|Zeichnen Sie ein", antwort="Zahl|Grafik",
    material="Koordinatensystem",
    skizze="Abbildung 1 zeigt ein leeres räumliches Koordinatensystem ohne Skalierung: z-Achse "
           "nach oben, y-Achse nach rechts, x-Achse nach vorn links. Einzuzeichnen ist die "
           "Pyramide ABCDS mit quadratischer Grundfläche in der x-y-Ebene, Kantenlänge 5, und "
           "der Spitze S senkrecht über dem Grundflächenmittelpunkt in der Höhe 3,9.",
    kontext="Camping", textumfang="lang",
    gegeben="Ein geschlossenes Zelt auf horizontalem Untergrund hat die Form einer Pyramide mit "
            "quadratischer Grundfläche; es ist 3,90 m hoch, die Seitenlänge des Zeltbodens "
            "beträgt 5,00 m. Im Modell ist die Pyramide ABCDS mit der Spitze S dargestellt: A "
            "liegt im Koordinatenursprung, B auf dem positiven Teil der x-Achse, D auf dem "
            "positiven Teil der y-Achse, C hat die Koordinaten (5 | 5 | 0); M ist der "
            "Mittelpunkt der Grundfläche. Das Dreieck ABS liegt in der Ebene E: −39y + 25z = 0. "
            "Eine Längeneinheit entspricht einem Meter.",
    gesucht="Koordinaten der Punkte B, D, M und S; Zeichnung der Pyramide in ein Koordinaten"
            "system gemäß Abbildung 1",
    verfahren="Aus der Seitenlänge 5 und der Lage auf den Achsen folgen B und D; M ist der "
              "Mittelpunkt der Diagonale von A nach C; S liegt senkrecht über M in der Höhe 3,9. "
              "Kontrolle mit der Ebenengleichung: −39 · 2,5 + 25 · 3,9 = 0.",
    schritte="3", zahlenraum="dezimal", einheiten="m",
    abhaengig_von="",
    ergebnis="B(5 | 0 | 0), D(0 | 5 | 0), M(2,5 | 2,5 | 0), S(2,5 | 2,5 | 3,9); die Pyramide "
             "wird mit quadratischer Grundfläche in der x-y-Ebene und der Spitze über M "
             "eingezeichnet.",
    zwischenergebnis="Probe: −39 · 2,5 + 25 · 3,9 = 0",
    niveau_geschaetzt="I",
    fehlerquelle="die Spitze über einem Eckpunkt statt über dem Mittelpunkt der Grundfläche "
                 "annehmen",
    bemerkung="Das Feld skizze beschreibt das vorgegebene leere Koordinatensystem (Abbildung 1) "
              "und die zu erstellende Zeichnung. Eigene Rechnung.")

row(id="2017-bb-ea-B3.1b", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="b",
    seite="7", punkte="4",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Schnittwinkel zweier Ebenen über die Normalenvektoren berechnen",
    typ_neben="Koordinatengleichung einer Ebene aus drei Punkten aufstellen",
    stichwoerter="Zeltwände|Normalenvektoren|Schnittwinkel|Nebenwinkel",
    voraussetzungen="Koordinatengleichung einer Ebene aufstellen|Skalarprodukt und Beträge "
                    "berechnen|spitzen und stumpfen Winkel unterscheiden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Camping", textumfang="kurz",
    gegeben="Pyramide ABCDS mit A(0 | 0 | 0), B(5 | 0 | 0), C(5 | 5 | 0), D(0 | 5 | 0) und "
            "S(2,5 | 2,5 | 3,9); die Zeltwände sind die Dreiecke ABS, BCS, CDS und ADS. Das "
            "Dreieck ABS liegt in der Ebene E: −39y + 25z = 0. Jeweils zwei benachbarte "
            "Zeltwände schließen im Inneren des Zelts einen stumpfen Winkel ein.",
    gesucht="Größe dieses stumpfen Winkels",
    verfahren="Die Ebene der Nachbarwand BCS aufstellen: 39x + 25z = 195 mit dem Normalenvektor "
              "(39 | 0 | 25); E hat den Normalenvektor (0 | −39 | 25). Über "
              "cos φ = (n_1 · n_2)/(|n_1| · |n_2|) = 625/2146 den Winkel zwischen den "
              "Normalenvektoren bestimmen; der Innenwinkel des Zelts ist dessen Nebenwinkel.",
    schritte="4", zahlenraum="dezimal", einheiten="Grad",
    abhaengig_von="2017-bb-ea-B3.1a",
    ergebnis="cos φ = 625/2146 ≈ 0,2912, also φ ≈ 73,1°; der stumpfe Innenwinkel zwischen zwei "
             "benachbarten Zeltwänden beträgt rund 106,9°.",
    zwischenergebnis="Ebene BCS: 39x + 25z = 195|n_1 = (0 | −39 | 25), n_2 = (39 | 0 | 25)|"
                     "φ ≈ 73,1°",
    niveau_geschaetzt="II",
    fehlerquelle="den berechneten spitzen Winkel als Antwort angeben, ohne zum stumpfen "
                 "Innenwinkel überzugehen",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B3.1c", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="c",
    seite="7", punkte="5",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt mit gleichem Abstand zu allen Seitenflächen über die Symmetrieachse bestimmen",
    typ_neben="Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen",
    stichwoerter="Lichtquelle|Abstand zur Ebene|Symmetrieachse|Hessesche Normalform",
    voraussetzungen="Hessesche Normalform aufstellen|Betragsgleichung lösen|Symmetrie eines "
                    "Körpers ausnutzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Camping", textumfang="kurz",
    gegeben="Pyramide ABCDS mit quadratischer Grundfläche der Seitenlänge 5 und der Spitze "
            "S(2,5 | 2,5 | 3,9); der Grundflächenmittelpunkt ist M(2,5 | 2,5 | 0). Die Wand ABS "
            "liegt in der Ebene E: −39y + 25z = 0. Im Zelt hängt eine Lichtquelle so, dass sie "
            "von jeder der vier Wände 80 cm Abstand hat; 1 LE entspricht 1 m.",
    gesucht="Koordinaten des Punktes, der die Lichtquelle im Modell darstellt",
    verfahren="Aus der Symmetrie der Pyramide folgt, dass der Punkt auf der Senkrechten durch M "
              "liegt, also die Form L(2,5 | 2,5 | z) hat. Abstand zu E über die Hessesche "
              "Normalform: |−39 · 2,5 + 25z| / √(39² + 25²) = 0,8 mit √2146 ≈ 46,32. Von den "
              "beiden Lösungen die im Zeltinneren wählen.",
    schritte="5", zahlenraum="dezimal", einheiten="m|cm",
    abhaengig_von="2017-bb-ea-B3.1a",
    ergebnis="Aus 97,5 − 25z = 0,8 · √2146 ≈ 37,06 folgt z ≈ 2,418; die Lichtquelle liegt bei "
             "L(2,5 | 2,5 | 2,42). Die zweite Lösung z ≈ 5,38 liegt oberhalb der Spitze und "
             "entfällt.",
    zwischenergebnis="√2146 ≈ 46,32|0,8 · √2146 ≈ 37,06",
    niveau_geschaetzt="III",
    fehlerquelle="die Betragsgleichung nur mit einem Vorzeichen lösen und den Punkt außerhalb des "
                 "Zelts angeben, oder 80 cm nicht in 0,8 LE umrechnen",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B3.1d", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="d",
    seite="7", punkte="3",
    leitidee="Analytische Geometrie", thema="Linearkombination und lineare Abhängigkeit",
    typ="Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen",
    typ_neben="",
    stichwoerter="Linearkombination|Ortsvektor|Strecke|Parameterdarstellung",
    voraussetzungen="mit Ortsvektoren rechnen|Parameterform einer Strecke kennen|Terme umformen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Camping", textumfang="kurz",
    gegeben="Pyramide ABCDS mit C(5 | 5 | 0) und S(2,5 | 2,5 | 3,9). Der Ortsvektor eines Punktes "
            "P lässt sich in der Form OP = r · OC + s · OS mit r, s ∈ [0; 1] und r + s = 1 "
            "darstellen.",
    gesucht="Nachweis, dass P auf der Strecke CS liegt",
    verfahren="r = 1 − s einsetzen und umformen: OP = (1 − s) · OC + s · OS = OC + s · (OS − OC) "
              "= OC + s · CS. Das ist die Parameterdarstellung der Strecke von C nach S, die für "
              "s ∈ [0; 1] genau diese Strecke durchläuft.",
    schritte="3", zahlenraum="ganz", einheiten="",
    abhaengig_von="",
    ergebnis="OP = OC + s · CS mit s ∈ [0; 1]; für s = 0 ist P = C, für s = 1 ist P = S, "
             "dazwischen liegt P auf der Strecke CS.",
    zwischenergebnis="OP = (1 − s) · OC + s · OS",
    niveau_geschaetzt="II",
    fehlerquelle="an einem einzelnen Zahlenbeispiel prüfen, statt allgemein mit r = 1 − s "
                 "umzuformen",
    bemerkung="Der vorhandene Typ zum Beschreiben einer Linearkombination bleibt getrennt: dort "
              "wird eine Lage in Worten gedeutet, hier wird sie durch Umformung nachgewiesen. "
              "Eigene Rechnung.")

row(id="2017-bb-ea-B3.1e", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="e",
    seite="7", punkte="3",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Strecke in einer geneigten Ebene über einen Höhenschnitt bestimmen",
    typ_neben="Streckenlänge im Raum berechnen",
    stichwoerter="Vordach|geneigte Wand|Höhenschnitt|Rechteckseite",
    voraussetzungen="Koordinatengleichung nach einer Koordinate auflösen|Satz des Pythagoras "
                    "anwenden|Maße aus einer Abbildung entnehmen",
    format="Rechnung|Begründung", operator="Weisen Sie nach", antwort="Zahl|Text",
    material="Figur",
    skizze="Abbildung 2 zeigt das Zelt als Schrägbild einer Pyramide. An der rechten vorderen "
           "Wand ist ein dunkel ausgefülltes waagerechtes Vordach aufgespannt, darunter die helle "
           "dreieckige Öffnung; zwei senkrechte Stangen stützen die äußere Vordachkante. Rechts "
           "daneben zwei Maßangaben: 1,80 m als Höhe des Vordachs über dem Boden und 1,40 m als "
           "Breite zwischen den beiden Stangen.",
    kontext="Camping", textumfang="lang",
    gegeben="Die Zeltwand CDS liegt in der Ebene F: 39y + 25z = 195, mit C(5 | 5 | 0) und "
            "D(0 | 5 | 0). Ein Teil dieser Wand wird mithilfe zweier Stangen zu einem "
            "waagerechten Vordach in 1,80 m Höhe aufgespannt; die dadurch entstehende Öffnung "
            "ist im Modell ein Rechteck, dessen eine Seite so auf der Strecke CD liegt, dass der "
            "eine Endpunkt von C ebenso weit entfernt ist wie der andere von D. Die Breite des "
            "Vordachs beträgt laut Abbildung 1,40 m; 1 LE entspricht 1 m.",
    gesucht="Nachweis, dass die Länge des Vordachs etwa 2,14 m beträgt",
    verfahren="Die Klappkante des Rechtecks liegt in der Wandebene in 1,80 m Höhe: aus "
              "39y + 25 · 1,8 = 195 folgt y = 150/39 ≈ 3,846. Die Vordachlänge ist die "
              "Rechteckseite von der Bodenkante CD (y = 5, z = 0) bis zu dieser Kante, in der "
              "Wandebene gemessen, also √((5 − 3,846)² + 1,8²).",
    schritte="4", zahlenraum="dezimal|Wurzel", einheiten="m",
    abhaengig_von="",
    ergebnis="y(z = 1,8) = 150/39 ≈ 3,846; die Länge beträgt √(1,154² + 1,8²) ≈ 2,138 m, also "
             "etwa 2,14 m.",
    zwischenergebnis="y(z = 1,8) ≈ 3,846|Differenz in y-Richtung ≈ 1,154",
    niveau_geschaetzt="III",
    fehlerquelle="die Vordachlänge als waagerechten Abstand messen und die Neigung der Zeltwand "
                 "außer Acht lassen",
    bemerkung="Die Maße 1,80 m und 1,40 m stehen nur in Abbildung 2. Die eigene Rechnung "
              "bestätigt zugleich die in Teilaufgabe f genannte y-Koordinate 5,98 der äußeren "
              "Vordachkante: 3,846 + 2,138 = 5,984. Eigene Rechnung.")

row(id="2017-bb-ea-B3.1f", block="B", aufgabe="3.1", titel="Zelt", teilaufgabe="f",
    seite="7", punkte="5",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Ganzzahligen Scharparameter aus einer Bereichsbedingung an den Durchstoßpunkt bestimmen",
    typ_neben="Durchstoßpunkt einer Geraden durch eine Ebene bestimmen",
    stichwoerter="Sonnenstrahl|Richtungsvektor mit Parameter|Vordach|ganzzahlige Lösung",
    voraussetzungen="Geradengleichung aus Punkt und Richtungsvektor aufstellen|Parameter aus "
                    "einer Koordinatenbedingung bestimmen|Lösungsbereich abschätzen",
    format="Rechnung", operator="Ermitteln Sie|Geben Sie an", antwort="Zahl",
    material="Figur",
    skizze="Dieselbe Abbildung 2 wie in Teilaufgabe e: Zelt als Schrägbild mit dunkel "
           "ausgefülltem waagerechtem Vordach an der rechten vorderen Wand, zwei Stützstangen "
           "und den Maßangaben 1,80 m für die Höhe und 1,40 m für die Breite.",
    kontext="Camping", textumfang="lang",
    gegeben="Zelt als Pyramide ABCDS mit dem Bodenmittelpunkt M(2,5 | 2,5 | 0). Das waagerechte "
            "Vordach liegt in 1,80 m Höhe, ist 1,40 m breit und mittig zur Kante CD angesetzt; "
            "seine wandseitige Kante liegt bei y ≈ 3,85, alle Punkte der äußeren Kante, an deren "
            "Enden die beiden Stangen befestigt sind, haben die y-Koordinate 5,98. Auf das Zelt "
            "treffendes Sonnenlicht verläuft längs paralleler Geraden mit dem Richtungsvektor "
            "(0,5 | −4,2 | a) und fällt durch ein kleines Loch im Vordach genau auf den "
            "Mittelpunkt des Zeltbodens; für a kommen verschiedene ganzzahlige Werte infrage.",
    gesucht="Ein möglicher ganzzahliger Wert für a und die Koordinaten des zugehörigen Punktes, "
            "der eine mögliche Position des Lochs im Vordach darstellt",
    verfahren="Gerade durch M mit dem gegebenen Richtungsvektor ansetzen und die Vordachhöhe "
              "z = 1,8 fordern: t = 1,8/a. Damit sind x = 2,5 + 0,5 · 1,8/a und "
              "y = 2,5 − 4,2 · 1,8/a. Das Loch muss auf dem Vordach liegen, also y zwischen 3,85 "
              "und 5,98 und x zwischen 1,8 und 3,2; das führt auf negative ganzzahlige Werte "
              "von a.",
    schritte="6", zahlenraum="dezimal|negativ", einheiten="m",
    abhaengig_von="2017-bb-ea-B3.1e",
    ergebnis="Möglich sind a = −3, a = −4 und a = −5. Für a = −3 ist t = −0,6 und das Loch liegt "
             "bei (2,2 | 5,02 | 1,8).",
    zwischenergebnis="t = 1,8/a|a = −4: (2,275 | 4,39 | 1,8)|a = −5: (2,32 | 4,012 | 1,8)",
    niveau_geschaetzt="III",
    fehlerquelle="das Vorzeichen von a nicht prüfen und einen Punkt außerhalb des Vordachs "
                 "angeben",
    bemerkung="Die wandseitige Kante bei y ≈ 3,85 folgt aus Teilaufgabe e und steht im Heft "
              "nicht ausdrücklich; sie begrenzt den zulässigen Bereich nach unten. Eigene "
              "Rechnung, mit sympy bestätigt.")

row(id="2017-bb-ea-B3.2a", block="B", aufgabe="3.2", titel="Gartenpavillon", teilaufgabe="a",
    seite="8", punkte="3",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Schnittwinkel zwischen Gerade und Ebene berechnen",
    typ_neben="",
    stichwoerter="Dachkante|Neigungswinkel|Grundflächenebene|Richtungsvektor",
    voraussetzungen="Richtungsvektor einer Geraden ablesen|Normalenvektor der x-y-Ebene kennen|"
                    "Winkelformel für Gerade und Ebene anwenden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Figur",
    skizze="Schrägbild eines Pavillons: ein Quader mit quadratischer Grundfläche, deren "
           "Mittelpunkt im Koordinatenursprung liegt, darauf eine gerade quadratische Pyramide "
           "mit der Spitze S auf der z-Achse. Eingezeichnet sind die z-Achse nach oben, die "
           "y-Achse nach rechts, die x-Achse nach vorn links sowie die Punkte S oben, E an der "
           "oberen vorderen Quaderecke und A senkrecht darunter am Boden; verdeckte Kanten sind "
           "gestrichelt.",
    kontext="Gartenbau", textumfang="lang",
    gegeben="Ein Pavillon wird vereinfacht als zusammengesetzter Körper aus einem Quader mit "
            "quadratischer Grundfläche und einer aufgesetzten geraden quadratischen Pyramide "
            "aufgefasst. Eine der senkrechten Kanten ist die Strecke AE mit A(1,5 | 1,5 | 0) und "
            "E(1,5 | 1,5 | 2,1); der Mittelpunkt der in der x-y-Ebene liegenden Grundfläche ist "
            "O(0 | 0 | 0). Eine der in der Spitze S zusammentreffenden Dachkanten ist Teil der "
            "Geraden g: x = (−1,5 | 1,5 | 2,1) + t · (−1,5 | 1,5 | −1); t ∈ IR. Es gilt "
            "1 LE = 1 m.",
    gesucht="Neigungswinkel einer Dachkante gegenüber der Grundflächenebene",
    verfahren="Winkel zwischen dem Richtungsvektor (−1,5 | 1,5 | −1) und der x-y-Ebene mit dem "
              "Normalenvektor (0 | 0 | 1) über sin α = |v_z| / |v| bestimmen; "
              "|v| = √(2,25 + 2,25 + 1) = √5,5.",
    schritte="3", zahlenraum="dezimal|Wurzel", einheiten="Grad",
    abhaengig_von="",
    ergebnis="|v| = √5,5 ≈ 2,345 und sin α = 1/√5,5 ≈ 0,4264, also α ≈ 25,2°.",
    zwischenergebnis="|v| = √5,5 ≈ 2,345",
    niveau_geschaetzt="II",
    fehlerquelle="den Winkel zwischen Richtungs- und Normalenvektor angeben, statt ihn auf die "
                 "Ebene zu beziehen",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B3.2b", block="B", aufgabe="3.2", titel="Gartenpavillon", teilaufgabe="b",
    seite="8", punkte="2",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Gesamthöhe eines zusammengesetzten Körpers über die Spitze bestimmen",
    typ_neben="Durchstoßpunkt einer Geraden durch eine Ebene bestimmen",
    stichwoerter="Pavillon|Spitze|z-Achse|Gesamthöhe",
    voraussetzungen="Geradenparameter aus einer Koordinatenbedingung bestimmen|Punkt durch "
                    "Einsetzen berechnen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="Figur",
    skizze="Dasselbe Schrägbild wie in Teilaufgabe a: Quader mit quadratischer Grundfläche um den "
           "Koordinatenursprung, darauf die Pyramide mit der Spitze S auf der z-Achse; "
           "beschriftet sind S, E und A sowie die drei Koordinatenachsen.",
    kontext="Gartenbau", textumfang="mittel",
    gegeben="Pavillon aus Quader und aufgesetzter gerader quadratischer Pyramide; der "
            "Grundflächenmittelpunkt ist O(0 | 0 | 0), die Quaderkante AE reicht von "
            "A(1,5 | 1,5 | 0) bis E(1,5 | 1,5 | 2,1). Eine Dachkante ist Teil der Geraden "
            "g: x = (−1,5 | 1,5 | 2,1) + t · (−1,5 | 1,5 | −1); 1 LE = 1 m.",
    gesucht="Gesamthöhe des Pavillons",
    verfahren="Die Spitze liegt auf g und zugleich auf der z-Achse, also über dem "
              "Grundflächenmittelpunkt: aus −1,5 − 1,5 · t = 0 folgt t = −1. Einsetzen liefert "
              "den Punkt; die Gesamthöhe ist dessen z-Koordinate.",
    schritte="3", zahlenraum="dezimal", einheiten="m",
    abhaengig_von="",
    ergebnis="t = −1 und S(0 | 0 | 3,1); der Pavillon ist 3,1 m hoch.",
    zwischenergebnis="t = −1",
    niveau_geschaetzt="II",
    fehlerquelle="die Quaderhöhe 2,1 m und die Pyramidenhöhe verwechseln oder nur die "
                 "Pyramidenhöhe angeben",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B3.2c", block="B", aufgabe="3.2", titel="Gartenpavillon", teilaufgabe="c",
    seite="8", punkte="3",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Koordinatengleichung einer Ebene aus Gerade und Punkt nachweisen",
    typ_neben="",
    stichwoerter="Dachfläche|Ebene durch Gerade und Punkt|Punktprobe|Normalenvektor",
    voraussetzungen="Punktprobe in einer Koordinatengleichung durchführen|Orthogonalität über das "
                    "Skalarprodukt prüfen",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="keins", skizze="keine", kontext="Gartenbau", textumfang="mittel",
    gegeben="Eine der dreieckigen Teilflächen des Pavillondaches liegt in der Ebene H, die die "
            "Gerade g: x = (−1,5 | 1,5 | 2,1) + t · (−1,5 | 1,5 | −1) und den Punkt "
            "E(1,5 | 1,5 | 2,1) enthält.",
    gesucht="Nachweis, dass die Ebene H durch die Gleichung 3y + 4,5z = 13,95 beschrieben werden "
            "kann",
    verfahren="Stützpunkt von g und Punkt E in die Gleichung einsetzen; anschließend zeigen, dass "
              "der Richtungsvektor von g orthogonal zum Normalenvektor (0 | 3 | 4,5) ist, damit "
              "die ganze Gerade in H liegt.",
    schritte="3", zahlenraum="dezimal", einheiten="",
    abhaengig_von="",
    ergebnis="Für (−1,5 | 1,5 | 2,1) und für E(1,5 | 1,5 | 2,1) ergibt 3y + 4,5z jeweils 13,95. "
             "Wegen 3 · 1,5 + 4,5 · (−1) = 0 steht der Richtungsvektor von g senkrecht auf dem "
             "Normalenvektor, also liegt g ganz in H; damit beschreibt die Gleichung die Ebene "
             "durch g und E.",
    zwischenergebnis="3 · 1,5 + 4,5 · 2,1 = 13,95|n · v = 0",
    niveau_geschaetzt="II",
    fehlerquelle="nur den Stützpunkt einsetzen und die Richtung der Geraden nicht prüfen",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B3.2d", block="B", aufgabe="3.2", titel="Gartenpavillon", teilaufgabe="d",
    seite="8", punkte="2",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Lotgerade von einem Punkt auf eine Ebene angeben",
    typ_neben="",
    stichwoerter="Lampe|kleinster Abstand|Lotgerade|Normalenvektor",
    voraussetzungen="Normalenvektor aus der Koordinatenform ablesen|Parameterform einer Geraden "
                    "aufschreiben|Lotfußpunkt als Punkt kleinsten Abstands kennen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="Gartenbau", textumfang="kurz",
    gegeben="Eine Dachteilfläche des Pavillons liegt in der Ebene H: 3y + 4,5z = 13,95. Im "
            "Inneren des Pavillons befindet sich eine Lampe, vereinfacht durch den Punkt "
            "L(0 | 1 | 2) modelliert.",
    gesucht="Gleichung einer Geraden k, auf der neben L auch der Punkt der Ebene H liegt, der den "
            "kleinsten Abstand zu L hat",
    verfahren="Der Punkt kleinsten Abstands ist der Lotfußpunkt; die gesuchte Gerade ist das Lot "
              "durch L, also die Gerade mit dem Normalenvektor von H als Richtungsvektor.",
    schritte="2", zahlenraum="dezimal", einheiten="",
    abhaengig_von="2017-bb-ea-B3.2c",
    ergebnis="k: x = (0 | 1 | 2) + r · (0 | 3 | 4,5); r ∈ IR, gleichwertig mit dem "
             "Richtungsvektor (0 | 2 | 3).",
    zwischenergebnis="",
    niveau_geschaetzt="I",
    fehlerquelle="einen Richtungsvektor innerhalb der Ebene statt des Normalenvektors verwenden",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B4.1a", block="B", aufgabe="4.1", titel="Vereinsjubiläum", teilaufgabe="a",
    seite="9", punkte="2",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen aufstellen",
    typ_neben="",
    stichwoerter="Vierfeldertafel|Randhäufigkeiten|Prozentanteil|absolute Zahlen",
    voraussetzungen="Prozentwert einer Gesamtzahl berechnen|Randsummen einer Vierfeldertafel "
                    "ergänzen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Vereinsfest", textumfang="mittel",
    gegeben="Zu einer Autogrammstunde haben 30 Frauen und 50 Männer je eine Frage eingereicht. "
            "75 Prozent aller eingereichten Fragen beziehen sich auf den Fußball, die übrigen "
            "sind eher allgemeiner Natur. Die Fragen der Frauen verteilen sich zu gleichen "
            "Teilen auf rein fußballerische und allgemeine.",
    gesucht="Anzahl der von Männern gestellten Fragen, die eher allgemeine Dinge betreffen",
    verfahren="Insgesamt sind es 80 Fragen, davon 25 % allgemeine, also 20. Von den Frauen "
              "stammen 15 allgemeine Fragen; die Differenz entfällt auf die Männer.",
    schritte="3", zahlenraum="ganz|Prozent", einheiten="",
    abhaengig_von="",
    ergebnis="20 − 15 = 5 Fragen von Männern betreffen eher allgemeine Dinge.",
    zwischenergebnis="80 Fragen insgesamt|20 allgemeine Fragen|15 allgemeine Fragen von Frauen",
    niveau_geschaetzt="I",
    fehlerquelle="die 75 Prozent auf die Männerfragen statt auf alle Fragen beziehen",
    bemerkung="Der vorhandene Typ wird übernommen, obwohl hier absolute Häufigkeiten statt "
              "Anteilen gegeben sind; der Lösungsweg ist derselbe. Eigene Rechnung.")

row(id="2017-bb-ea-B4.1b", block="B", aufgabe="4.1", titel="Vereinsjubiläum", teilaufgabe="b",
    seite="9", punkte="4",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Bedingte Wahrscheinlichkeit aus der Vierfeldertafel berechnen",
    typ_neben="",
    stichwoerter="Losentscheid|bedingte Wahrscheinlichkeit|Teilgruppe|Vierfeldertafel",
    voraussetzungen="bedingte Wahrscheinlichkeit als Anteil innerhalb einer Teilgruppe deuten|"
                    "Vierfeldertafel auswerten",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Vereinsfest", textumfang="mittel",
    gegeben="Unter den 80 Personen, die je eine Frage eingereicht haben (30 Frauen, 50 Männer), "
            "wird eine Jahreskarte verlost. 20 der Fragen sind eher allgemeiner Natur, davon 15 "
            "von Frauen und 5 von Männern. Bekannt ist bereits, dass der Gewinner eine eher "
            "allgemeine Frage gestellt hat.",
    gesucht="Wahrscheinlichkeit dafür, dass die Jahreskarte von einem Mann gewonnen wird",
    verfahren="Bedingte Wahrscheinlichkeit: Anteil der Männer unter den 20 Personen mit "
              "allgemeiner Frage, also 5/20.",
    schritte="2", zahlenraum="Bruch|dezimal", einheiten="",
    abhaengig_von="2017-bb-ea-B4.1a",
    ergebnis="P(Mann | allgemeine Frage) = 5/20 = 0,25",
    zwischenergebnis="",
    niveau_geschaetzt="II",
    fehlerquelle="die Wahrscheinlichkeit auf alle 80 Personen beziehen und 5/80 angeben",
    bemerkung="Eigene Rechnung.")

row(id="2017-bb-ea-B4.1c", block="B", aufgabe="4.1", titel="Vereinsjubiläum", teilaufgabe="c",
    seite="9", punkte="4",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen",
    typ_neben="Wahrscheinlichkeit aus den Sektorwinkeln eines Glücksrads bestimmen",
    stichwoerter="Glücksrad|Sektorwinkel|Erwartungswert|Gewinn je Wurst",
    voraussetzungen="Wahrscheinlichkeit aus Winkelanteilen bestimmen|Erwartungswert einer "
                    "Zufallsgröße bilden|Selbstkosten aus Preis und Gewinn erschließen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Imbissstand", textumfang="lang",
    gegeben="Eine Bratwurst kostet 1,50 €, der Betreiber erzielt dabei 0,30 € Gewinn je "
            "verkaufter Wurst. Er stellt ein Glücksrad aus schwarzen und weißen Sektoren auf; "
            "die weißen Sektoren nehmen zusammen einen Winkel von 36° ein. Wer Weiß dreht, "
            "erhält die Wurst kostenlos.",
    gesucht="Betrag, auf den sich der Gewinn pro abgegebener Bratwurst durch die Aktion "
            "verringert",
    verfahren="P(weiß) = 36°/360° = 0,1. Bei Weiß entgehen dem Betreiber die Selbstkosten von "
              "1,50 € − 0,30 € = 1,20 €. Erwartungswert des Gewinns: "
              "0,9 · 0,30 € + 0,1 · (−1,20 €).",
    schritte="4", zahlenraum="dezimal", einheiten="Euro|Grad",
    abhaengig_von="",
    ergebnis="P(weiß) = 0,1; der erwartete Gewinn beträgt 0,27 € − 0,12 € = 0,15 € je "
             "abgegebener Bratwurst, sinkt also von 0,30 € auf 0,15 € und damit um die Hälfte.",
    zwischenergebnis="P(weiß) = 0,1|Verlust bei Weiß 1,20 €",
    niveau_geschaetzt="III",
    fehlerquelle="bei einer kostenlos abgegebenen Wurst nur den entgangenen Gewinn von 0,30 € "
                 "statt der Selbstkosten von 1,20 € ansetzen",
    bemerkung="Das Heft nennt keinen Einkaufspreis; die Selbstkosten von 1,20 € folgen aus Preis "
              "minus Gewinn. Die Frageformulierung nennt den neuen Gewinn, die Verringerung "
              "beträgt ebenfalls 0,15 €. Eigene Rechnung.")

row(id="2017-bb-ea-B4.2a", block="B", aufgabe="4.2", titel="Freizeit", teilaufgabe="a",
    seite="10", punkte="8",
    leitidee="Stochastik", thema="Zufallsgrößen und Verteilungen",
    typ="Wahrscheinlichkeit für den ersten Treffer bei der k-ten Wiederholung berechnen",
    typ_neben="Wahrscheinlichkeit einer festgelegten Trefferfolge berechnen|Kumulierte "
              "Wahrscheinlichkeit einer Binomialverteilung berechnen",
    stichwoerter="Bernoulli-Kette|erster Treffer|festgelegte Positionen|kumulierte "
                 "Wahrscheinlichkeit",
    voraussetzungen="Pfadregel für unabhängige Wiederholungen anwenden|Binomialformel anwenden|"
                    "Ereignis mehr als 18 in Einzelfälle zerlegen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Freizeitverhalten", textumfang="lang",
    gegeben="In der deutschen Bevölkerung ab 14 Jahre sehen 96 % mindestens einmal pro Woche "
            "fern, 72,6 % lesen gern und 60,3 % arbeiten gern am Computer. Ereignis A: Zufällig "
            "ausgewählte Personen werden nacheinander befragt, erst die fünfte antwortet, dass "
            "sie gern am Computer arbeitet. Ereignis B: Von acht zufällig ausgewählten Personen "
            "arbeiten nur die dritte und die fünfte gern am Computer. Ereignis C: Unter 20 "
            "zufällig ausgewählten Personen befinden sich mehr als 18, die mindestens einmal pro "
            "Woche fernsehen.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A, B und C",
    verfahren="A als Kette von vier Nichttreffern und einem Treffer: 0,397⁴ · 0,603. B mit "
              "festgelegten Positionen über die Pfadregel ohne Binomialkoeffizient: "
              "0,603² · 0,397⁶. C als Binomialverteilung mit n = 20 und p = 0,96 über "
              "P(X = 19) + P(X = 20).",
    schritte="6", zahlenraum="dezimal|Prozent|Potenz", einheiten="",
    abhaengig_von="",
    ergebnis="P(A) = 0,397⁴ · 0,603 ≈ 0,0150; P(B) = 0,603² · 0,397⁶ ≈ 0,00142; "
             "P(C) = 20 · 0,96¹⁹ · 0,04 + 0,96²⁰ ≈ 0,8103.",
    zwischenergebnis="0,397⁴ ≈ 0,02484|0,96²⁰ ≈ 0,4420|P(X = 19) ≈ 0,3683",
    niveau_geschaetzt="II",
    fehlerquelle="bei B den Binomialkoeffizienten ansetzen, obwohl die Positionen der beiden "
                 "Treffer festgelegt sind",
    bemerkung="Drei Ereignisse in einer Einheit; thema folgt dem ersten Typ. Eigene Rechnung, "
              "mit sympy bestätigt.")

row(id="2017-bb-ea-B4.2b", block="B", aufgabe="4.2", titel="Freizeit", teilaufgabe="b",
    seite="10", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen",
    typ_neben="",
    stichwoerter="Mindestwahrscheinlichkeit|Gegenereignis|Logarithmus|Stichprobenumfang",
    voraussetzungen="Gegenereignis bilden|Exponentialungleichung durch Logarithmieren lösen|auf "
                    "die nächste ganze Zahl aufrunden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Freizeitverhalten", textumfang="mittel",
    gegeben="72,6 % der deutschen Bevölkerung ab 14 Jahre lesen in ihrer Freizeit gern, die "
            "übrigen 27,4 % nicht.",
    gesucht="Mindestanzahl der Personen, die befragt werden müssten, um mit einer "
            "Mindestwahrscheinlichkeit von 98 % wenigstens eine Person zu finden, die nicht gern "
            "liest",
    verfahren="Gegenereignis: alle Befragten lesen gern. Aus 1 − 0,726ⁿ ≥ 0,98 folgt "
              "0,726ⁿ ≤ 0,02, also n ≥ ln 0,02 / ln 0,726; aufrunden.",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="",
    abhaengig_von="",
    ergebnis="n ≥ 12,22, es müssen also mindestens 13 Personen befragt werden.",
    zwischenergebnis="0,726ⁿ ≤ 0,02|ln 0,02 / ln 0,726 ≈ 12,22",
    niveau_geschaetzt="II",
    fehlerquelle="beim Logarithmieren einer Ungleichung mit negativem Logarithmus das "
                 "Ungleichheitszeichen nicht umdrehen oder abrunden",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2017-bb-ea-B4.2c", block="B", aufgabe="4.2", titel="Freizeit", teilaufgabe="c",
    seite="10", punkte="5",
    leitidee="Stochastik", thema="Bedingte Wahrscheinlichkeit und Bayes",
    typ="Anteil einer Teilgruppe aus der totalen Wahrscheinlichkeit berechnen",
    typ_neben="Baumdiagramm zu einer zweistufigen Situation erstellen",
    stichwoerter="totale Wahrscheinlichkeit|Frauenanteil|Baumdiagramm|Vierfeldertafel",
    voraussetzungen="Satz von der totalen Wahrscheinlichkeit anwenden|lineare Gleichung mit einer "
                    "Unbekannten lösen|reduziertes Baumdiagramm zeichnen",
    format="Rechnung|Zeichnen", operator="Berechnen Sie|Veranschaulichen Sie",
    antwort="Zahl|Grafik",
    material="keins",
    skizze="Im Heft ist keine Abbildung vorgegeben; zu erstellen ist ein reduziertes "
           "Baumdiagramm mit der ersten Stufe weiblich (Anteil w) und männlich (1 − w) und der "
           "zweiten Stufe liest gern mit 0,76 beziehungsweise 0,69, alternativ eine "
           "Vierfeldertafel mit denselben Werten und der Randwahrscheinlichkeit 0,726.",
    kontext="Freizeitverhalten", textumfang="mittel",
    gegeben="72,6 % der deutschen Bevölkerung ab 14 Jahre lesen in ihrer Freizeit gern. Dabei "
            "lesen 76 % der weiblichen und 69 % der männlichen Bevölkerung gern.",
    gesucht="Anteil der Frauen in der deutschen Bevölkerung; Veranschaulichung des Lösungsansatzes "
            "durch ein reduziertes Baumdiagramm oder eine Vierfeldertafel",
    verfahren="Frauenanteil w ansetzen und die totale Wahrscheinlichkeit bilden: "
              "0,76 · w + 0,69 · (1 − w) = 0,726, also 0,07 · w = 0,036.",
    schritte="4", zahlenraum="dezimal|Prozent", einheiten="",
    abhaengig_von="",
    ergebnis="w = 0,036/0,07 = 18/35 ≈ 0,514; der Frauenanteil beträgt rund 51,4 %.",
    zwischenergebnis="0,07 · w = 0,036",
    niveau_geschaetzt="II",
    fehlerquelle="den Mittelwert aus 76 % und 69 % bilden, statt mit den unbekannten Anteilen zu "
                 "gewichten",
    bemerkung="Das Feld skizze beschreibt eine vom Prüfling zu erstellende Darstellung, nicht "
              "vorhandenes Aufgabenmaterial. Eigene Rechnung.")

row(id="2017-bb-ea-B4.2d", block="B", aufgabe="4.2", titel="Freizeit", teilaufgabe="d",
    seite="10", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer Binomialverteilung für genau k Treffer berechnen",
    typ_neben="Modalwert einer Binomialverteilung bestimmen",
    stichwoerter="Stornierung|Binomialformel|Term angeben|größte Wahrscheinlichkeit",
    voraussetzungen="Bernoulli-Kette erkennen|Binomialformel mit dem Binomialkoeffizienten "
                    "aufschreiben|Erwartungswert n · p als Orientierung nutzen",
    format="Rechnung|Kurzantwort", operator="Geben Sie an|Ermitteln Sie", antwort="Term|Zahl",
    material="keins", skizze="keine", kontext="Lesung / Kartenverkauf", textumfang="lang",
    gegeben="Ein Buchhändler organisiert eine Lesung in einem Saal mit 175 Plätzen. Da im Mittel "
            "5 % der bestellten Karten storniert werden, lässt er 180 Kartenreservierungen "
            "annehmen. k ist die Anzahl der stornierten Karten.",
    gesucht="Term für P(k), mit dem die Wahrscheinlichkeit für genau k Stornierungen berechnet "
            "werden kann; größter Wert dieser Wahrscheinlichkeit",
    verfahren="Bernoulli-Kette mit n = 180 und p = 0,05: P(k) = C(180; k) · 0,05^k · "
              "0,95^(180 − k). Der größte Wert liegt beim Modalwert in der Nähe des "
              "Erwartungswerts n · p = 9; die Werte um 9 herum vergleichen.",
    schritte="4", zahlenraum="dezimal|Prozent|Potenz", einheiten="",
    abhaengig_von="",
    ergebnis="P(k) = C(180; k) · 0,05^k · 0,95^(180 − k); der größte Wert wird bei k = 9 "
             "erreicht: P(9) ≈ 0,1352 gegenüber P(8) ≈ 0,1344 und P(10) ≈ 0,1217.",
    zwischenergebnis="Erwartungswert n · p = 9",
    niveau_geschaetzt="II",
    fehlerquelle="die Stornierungen als Treffer mit p = 0,95 ansetzen oder den größten Wert bei "
                 "k = 5 vermuten",
    bemerkung="Die Saalkapazität von 175 Plätzen wird in dieser Teilaufgabe nicht gebraucht. "
              "Eigene Rechnung, mit sympy bestätigt.")

row(id="2017-bb-ea-B4.2e", block="B", aufgabe="4.2", titel="Freizeit", teilaufgabe="e",
    seite="10", punkte="4",
    leitidee="Stochastik", thema="Hypergeometrische Verteilung",
    typ="Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen",
    typ_neben="Ungeeignetheit des Binomialmodells begründen",
    stichwoerter="Auslosung|ohne Zurücklegen|bestimmte Person|Modellkritik",
    voraussetzungen="Anzahl der Auswahlmöglichkeiten mit Binomialkoeffizienten bestimmen|"
                    "Gegenereignis bilden|Voraussetzungen der Binomialverteilung kennen",
    format="Rechnung|Begründung", operator="Berechnen Sie|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Lesung / Kartenverkauf", textumfang="mittel",
    gegeben="An der Lesung nehmen 174 Besucher teil, darunter ein Deutschkurs und dessen "
            "Lehrerin. Aus den Teilnehmern werden fünf Personen ausgelost, die je eine Freikarte "
            "für die nächste Veranstaltung erhalten.",
    gesucht="Wahrscheinlichkeit dafür, dass die Lehrerin unter den fünf Gewinnern ist; "
            "Begründung, dass das Modell der Binomialverteilung dafür ungeeignet ist",
    verfahren="Ziehen ohne Zurücklegen: über das Gegenereignis "
              "P = 1 − C(173; 5)/C(174; 5) = 1 − 169/174, gleichwertig zur Überlegung, dass "
              "jede der 174 Personen dieselbe Chance hat, unter den fünf Gezogenen zu sein. Die "
              "Binomialverteilung setzt unabhängige Wiederholungen mit gleichbleibender "
              "Trefferwahrscheinlichkeit voraus.",
    schritte="3", zahlenraum="Bruch|dezimal", einheiten="",
    abhaengig_von="",
    ergebnis="P = 5/174 ≈ 0,0287. Die Binomialverteilung ist ungeeignet, weil ohne Zurücklegen "
             "gezogen wird: Die Trefferwahrscheinlichkeit ändert sich von Zug zu Zug, die Züge "
             "sind nicht unabhängig.",
    zwischenergebnis="C(173; 5)/C(174; 5) = 169/174",
    niveau_geschaetzt="II",
    fehlerquelle="mit fünf unabhängigen Zügen und der festen Wahrscheinlichkeit 1/174 rechnen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")


NEUE_TYPEN = [
    ("Nullstelle einer Exponentialfunktion durch Logarithmieren bestimmen", "Analysis",
     "Gleichungen lösen",
     "Eine Gleichung der Form c · e^(kx) + d = 0 nach der Exponentialfunktion auflösen und durch "
     "Logarithmieren die Nullstelle exakt angeben.",
     "2017-bb-ea-A1.1a"),
    ("Gleichschenkligkeit des Achsenabschnittsdreiecks einer Tangente nachweisen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die Achsenschnittpunkte einer Tangente berechnen und aus dem Vergleich der beiden "
     "Achsenabschnitte eine Eigenschaft des entstehenden Dreiecks nachweisen.",
     "2017-bb-ea-A1.1b"),
    ("Flächeninhalt eines Dreiecks aus den Spurpunkten einer Ebene berechnen",
     "Analytische Geometrie", "Flächeninhalt und Volumen im Raum",
     "Aus den Spurpunkten einer Ebene auf zwei Koordinatenachsen und dem Koordinatenursprung ein "
     "rechtwinkliges Dreieck bilden und seinen Flächeninhalt aus den Achsenabschnitten "
     "bestimmen.",
     "2017-bb-ea-A1.2a"),
    ("Spurpunkte einer Ebene auf den Koordinatenachsen bestimmen", "Analytische Geometrie",
     "Schnittmengen",
     "Aus der Koordinatengleichung einer Ebene die Schnittpunkte mit den Koordinatenachsen "
     "bestimmen, indem die jeweils anderen Koordinaten null gesetzt werden.",
     "2017-bb-ea-A1.2a"),
    ("Normalenvektor als Ortsvektor eines Ebenenpunktes bestimmen", "Analytische Geometrie",
     "Ebenen",
     "Ein Vielfaches des Normalenvektors als Ortsvektor ansetzen, in die Koordinatengleichung der "
     "Ebene einsetzen und den Faktor bestimmen.",
     "2017-bb-ea-A1.2b"),
    ("Wahrscheinlichkeit bei zweistufigem Umlegen zwischen Urnen berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Ein zweistufiges Urnenexperiment mit Umlegen einer Kugel als Baum auffassen, die durch den "
     "ersten Zug veränderten Inhalte berücksichtigen und die Pfadwahrscheinlichkeiten "
     "zusammenfassen.",
     "2017-bb-ea-A1.3a"),
    ("Auszahlung eines fairen Spiels aus der Fairnessbedingung bestimmen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Die unbekannte Auszahlung eines Glücksspiels so bestimmen, dass der erwartete Gewinn null "
     "ist, indem Erwartungswert und Einsatz gleichgesetzt werden.",
     "2017-bb-ea-A1.3b"),
    ("Totale Wahrscheinlichkeit bei zufälliger Auswahl einer Urne berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit eines Ereignisses über mehrere gleich wahrscheinliche Teilversuche "
     "hinweg bestimmen, indem die bedingten Wahrscheinlichkeiten gewichtet addiert werden.",
     "2017-bb-ea-A1.3b"),
    ("Definitionsbereich einer Logarithmusfunktion angeben", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Den größtmöglichen Definitionsbereich einer Logarithmusfunktion aus der Bedingung "
     "bestimmen, dass das Argument positiv sein muss, gegebenenfalls in Abhängigkeit von einem "
     "Parameter.",
     "2017-bb-ea-B2.1a"),
    ("Gemeinsamen Punkt aller Graphen einer Schar nachweisen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Zeigen, dass ein Punkt auf allen Graphen einer Schar liegt, indem der Funktionswert an "
     "dieser Stelle vom Parameter unabhängig ist.",
     "2017-bb-ea-B2.1a"),
    ("Parameterwert einer Schar aus einer Funktionswertbedingung exakt bestimmen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Den Scharparameter aus einer Bedingung an einen Funktionswert bestimmen, indem die "
     "entstehende Gleichung exakt, also ohne Rundung, nach dem Parameter aufgelöst wird.",
     "2017-bb-ea-B2.1a"),
    ("Gemeinsamen Extrempunkt einer Funktionenschar nachweisen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Die Ableitung der Schar bilden, ihre Nullstelle als parameterunabhängig nachweisen und aus "
     "dem zugehörigen Funktionswert den für alle Graphen gemeinsamen Extrempunkt angeben.",
     "2017-bb-ea-B2.1b"),
    ("Art eines Extrempunktes über den Vorzeichenwechsel der ersten Ableitung begründen",
     "Analysis", "Kurvenuntersuchung",
     "Ohne zweite Ableitung begründen, ob an einer Stelle ein Hoch- oder Tiefpunkt vorliegt, "
     "indem das Vorzeichen der ersten Ableitung links und rechts der Stelle bestimmt wird.",
     "2017-bb-ea-B2.1b"),
    ("Schranke für den Anstieg der Tangenten einer Schar begründen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Den Tangentenanstieg an einer festen Stelle als Term im Scharparameter aufstellen und durch "
     "Umformen oder Grenzwertbetrachtung zeigen, dass er eine Schranke nicht überschreitet.",
     "2017-bb-ea-B2.1c"),
    ("Normalengleichung an einer Stelle ermitteln", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Gleichung der Normalen an einen Graphen an einer gegebenen Stelle aus Funktionswert und "
     "negativem Kehrwert der Ableitung bestimmen.",
     "2017-bb-ea-B2.1c"),
    ("Flächeninhalt des von Tangente, Normale und y-Achse begrenzten Dreiecks berechnen",
     "Analysis", "Tangente, Normale, Schnittwinkel",
     "Die Achsenschnittpunkte von Tangente und Normale bestimmen und aus der Strecke auf der "
     "Achse als Grundseite und dem Abstand des Berührpunktes als Höhe den Flächeninhalt "
     "berechnen.",
     "2017-bb-ea-B2.1c"),
    ("Parabelgleichung aus Symmetrie und einer Flächenbedingung rekonstruieren", "Analysis",
     "Rekonstruktion von Funktionsgleichungen",
     "Den Ansatz einer achsensymmetrischen Parabel über eine Nullstelle verkürzen und den "
     "verbliebenen Koeffizienten aus einer vorgegebenen Flächengröße über das Integral "
     "bestimmen.",
     "2017-bb-ea-B2.1e"),
    ("Fehlerhaftes Verfahren zur Volumenberechnung beurteilen und berichtigen", "Analysis",
     "Rotationsvolumen",
     "Die Teilschritte einer vorgelegten fremden Rechnung einzeln auf Richtigkeit prüfen, die "
     "fehlerhaften benennen und die richtige Vorgehensweise beschreiben.",
     "2017-bb-ea-B2.1f"),
    ("Rotationsvolumen um die y-Achse über die Umkehrfunktion aufstellen", "Analysis",
     "Rotationsvolumen",
     "Für die Rotation einer Fläche um die y-Achse den Funktionsterm nach x² auflösen und das "
     "Volumenintegral über y aufstellen und auswerten.",
     "2017-bb-ea-B2.1f"),
    ("Volumenmaßstab zwischen Modell und Wirklichkeit umrechnen", "Analysis", "Rotationsvolumen",
     "Aus dem Längenmaßstab eines Modells den Volumenmaßstab als dritte Potenz bilden und ein in "
     "Volumeneinheiten berechnetes Volumen in Realmaße umrechnen.",
     "2017-bb-ea-B2.1f"),
    ("Nullstellenfreiheit über das Vorzeichen des Funktionsterms begründen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Begründen, dass eine Funktion keine Nullstelle hat, indem der Funktionsterm als Summe oder "
     "Produkt stets positiver Bestandteile erkannt wird.",
     "2017-bb-ea-B2.2a"),
    ("Achsensymmetrie am Funktionsterm nachweisen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Die Symmetrie eines Graphen zur y-Achse nachweisen, indem f(−x) gebildet und mit f(x) "
     "verglichen wird.",
     "2017-bb-ea-B2.2a"),
    ("Art eines Extrempunktes über die zweite Ableitung bestimmen", "Analysis",
     "Kurvenuntersuchung",
     "Mit dem Vorzeichen der zweiten Ableitung an einer Stelle mit waagerechter Tangente "
     "entscheiden, ob ein Hoch- oder ein Tiefpunkt vorliegt.",
     "2017-bb-ea-B2.2b"),
    ("Fehlen von Wendepunkten über die zweite Ableitung nachweisen", "Analysis",
     "Kurvenuntersuchung",
     "Zeigen, dass ein Graph keine Wendepunkte besitzt, indem die zweite Ableitung als nirgends "
     "null nachgewiesen wird.",
     "2017-bb-ea-B2.2b"),
    ("Dreieck zu Schnittpunkten mit einer Parallelen zur x-Achse einzeichnen", "Analysis",
     "Extremalprobleme",
     "In ein vorgegebenes Koordinatensystem mit Graph eine Parallele zur x-Achse, ihre beiden "
     "Schnittpunkte mit dem Graphen und das daraus mit einem festen Punkt gebildete Dreieck "
     "eintragen.",
     "2017-bb-ea-B2.2c"),
    ("Existenz eines Flächenmaximums ohne Rechnung begründen", "Analysis", "Extremalprobleme",
     "Aus dem Verhalten einer Flächenfunktion an den offenen Rändern des zulässigen Bereichs "
     "begründen, dass ein größter Wert angenommen wird, ein kleinster dagegen nicht.",
     "2017-bb-ea-B2.2c"),
    ("Zielfunktion für den Flächeninhalt eines Dreiecks aufstellen", "Analysis",
     "Extremalprobleme",
     "Grundseite und Höhe eines Dreiecks durch eine gemeinsame Variable ausdrücken und daraus die "
     "Flächeninhaltsfunktion als Gleichung aufstellen.",
     "2017-bb-ea-B2.2c"),
    ("Näherungsweise tangentiale Einmündung einer Geraden nachweisen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Zeigen, dass eine Gerade an einer Anschlussstelle näherungsweise Tangente eines Graphen "
     "ist, indem Funktionswert und Anstieg mit den Werten der Geraden verglichen werden.",
     "2017-bb-ea-B2.2d"),
    ("Punkt in vorgegebener Entfernung auf einer Geraden bestimmen", "Analysis",
     "Gleichungen lösen",
     "Von einem Ausgangspunkt aus einen Punkt auf einer Geraden bestimmen, dessen Entfernung "
     "vorgegeben ist, indem die Länge über den Satz des Pythagoras auf die Koordinatenzuwächse "
     "verteilt wird.",
     "2017-bb-ea-B2.2e"),
    ("Gleichungssystem zur Bestimmung einer Parabelgleichung aufstellen", "Analysis",
     "Lineare Gleichungssysteme",
     "Aus Punktbedingungen und einer Anstiegsbedingung ein lineares Gleichungssystem für die "
     "Koeffizienten einer quadratischen Funktion aufstellen, ohne es zu lösen.",
     "2017-bb-ea-B2.2e"),
    ("Abschnittsweise begrenzte Fläche durch Integration berechnen", "Analysis",
     "Flächeninhalt durch Integration",
     "Eine Fläche, deren oberer Rand abschnittsweise durch verschiedene Funktionen gegeben ist, "
     "in Teilintegrale zerlegen und die Teilflächen addieren.",
     "2017-bb-ea-B2.2f"),
    ("Flächenmaßstab eines Modells auf eine Realfläche anwenden", "Analysis",
     "Flächeninhalt durch Integration",
     "Aus dem Längenmaßstab eines Modells den Flächenmaßstab als zweite Potenz bilden und eine in "
     "Flächeneinheiten berechnete Fläche in Realmaße umrechnen.",
     "2017-bb-ea-B2.2f"),
    ("Koordinaten der Eckpunkte einer Pyramide aus der Beschreibung angeben",
     "Analytische Geometrie", "Punkte und Strecken im Koordinatensystem",
     "Aus Angaben zu Lage, Seitenlänge und Höhe eines Körpers die Koordinaten seiner Eckpunkte "
     "und der Spitze bestimmen.",
     "2017-bb-ea-B3.1a"),
    ("Körper in ein räumliches Koordinatensystem einzeichnen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Einen durch Koordinaten gegebenen Körper als Schrägbild in ein vorgegebenes räumliches "
     "Koordinatensystem eintragen.",
     "2017-bb-ea-B3.1a"),
    ("Schnittwinkel zweier Ebenen über die Normalenvektoren berechnen", "Analytische Geometrie",
     "Skalarprodukt und Winkel",
     "Den Winkel zwischen zwei Ebenen aus dem Skalarprodukt ihrer Normalenvektoren bestimmen und "
     "je nach Fragestellung den spitzen Winkel oder seinen Nebenwinkel angeben.",
     "2017-bb-ea-B3.1b"),
    ("Koordinatengleichung einer Ebene aus drei Punkten aufstellen", "Analytische Geometrie",
     "Ebenen",
     "Aus drei Punkten einer Ebene einen Normalenvektor gewinnen und die Koordinatengleichung "
     "aufstellen.",
     "2017-bb-ea-B3.1b"),
    ("Punkt mit gleichem Abstand zu allen Seitenflächen über die Symmetrieachse bestimmen",
     "Analytische Geometrie", "Abstände",
     "Aus der Symmetrie eines Körpers schließen, dass der gesuchte Punkt auf der Mittelsenkrechten "
     "liegt, und seine verbleibende Koordinate aus einer Abstandsbedingung zu einer Seitenfläche "
     "bestimmen.",
     "2017-bb-ea-B3.1c"),
    ("Abstand eines Punktes von einer Ebene mit der Hesseschen Normalform berechnen",
     "Analytische Geometrie", "Abstände",
     "Die Koordinatengleichung einer Ebene normieren und den Abstand eines Punktes durch "
     "Einsetzen seiner Koordinaten bestimmen.",
     "2017-bb-ea-B3.1c"),
    ("Lage eines Punktes auf einer Strecke über eine Linearkombination nachweisen",
     "Analytische Geometrie", "Linearkombination und lineare Abhängigkeit",
     "Eine Linearkombination zweier Ortsvektoren mit der Nebenbedingung, dass die Koeffizienten "
     "zusammen eins ergeben, in die Parameterform einer Strecke umformen und so die Lage des "
     "Punktes nachweisen.",
     "2017-bb-ea-B3.1d"),
    ("Strecke in einer geneigten Ebene über einen Höhenschnitt bestimmen",
     "Analytische Geometrie", "Abstände",
     "Zu einer vorgegebenen Höhe den zugehörigen Punkt einer geneigten Ebene bestimmen und die "
     "Länge der Strecke von einer Grundkante dorthin in der Ebene berechnen.",
     "2017-bb-ea-B3.1e"),
    ("Ganzzahligen Scharparameter aus einer Bereichsbedingung an den Durchstoßpunkt bestimmen",
     "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Den Parameter im Richtungsvektor einer Geradenschar so bestimmen, dass der Durchstoßpunkt "
     "durch eine Ebene in einem vorgegebenen Bereich liegt, und daraus zulässige ganzzahlige "
     "Werte angeben.",
     "2017-bb-ea-B3.1f"),
    ("Schnittwinkel zwischen Gerade und Ebene berechnen", "Analytische Geometrie",
     "Skalarprodukt und Winkel",
     "Den Neigungswinkel einer Geraden gegenüber einer Ebene über den Sinus aus Richtungs- und "
     "Normalenvektor bestimmen.",
     "2017-bb-ea-B3.2a"),
    ("Gesamthöhe eines zusammengesetzten Körpers über die Spitze bestimmen",
     "Analytische Geometrie", "Schnittmengen",
     "Die Spitze eines Körpers als Punkt einer Kantengeraden über der Symmetrieachse bestimmen "
     "und ihre Höhe als Gesamthöhe angeben.",
     "2017-bb-ea-B3.2b"),
    ("Koordinatengleichung einer Ebene aus Gerade und Punkt nachweisen", "Analytische Geometrie",
     "Ebenen",
     "Eine vorgegebene Koordinatengleichung als Ebene durch eine Gerade und einen Punkt "
     "bestätigen, indem Punktproben durchgeführt und Richtungsvektor und Normalenvektor als "
     "orthogonal nachgewiesen werden.",
     "2017-bb-ea-B3.2c"),
    ("Lotgerade von einem Punkt auf eine Ebene angeben", "Analytische Geometrie", "Abstände",
     "Die Gerade durch einen Punkt mit dem Normalenvektor einer Ebene als Richtungsvektor "
     "aufstellen, auf der der Punkt kleinsten Abstands liegt.",
     "2017-bb-ea-B3.2d"),
    ("Wahrscheinlichkeit aus den Sektorwinkeln eines Glücksrads bestimmen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die Wahrscheinlichkeit eines Ergebnisses beim Glücksrad als Anteil des zugehörigen "
     "Mittelpunktswinkels am Vollwinkel bestimmen.",
     "2017-bb-ea-B4.1c"),
    ("Wahrscheinlichkeit für den ersten Treffer bei der k-ten Wiederholung berechnen",
     "Stochastik", "Zufallsgrößen und Verteilungen",
     "Die Wahrscheinlichkeit dafür berechnen, dass bei unabhängigen Wiederholungen erst der k-te "
     "Versuch ein Treffer ist, als Produkt aus Nichttreffern und einem Treffer.",
     "2017-bb-ea-B4.2a"),
    ("Wahrscheinlichkeit einer festgelegten Trefferfolge berechnen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Die Wahrscheinlichkeit einer Bernoulli-Kette mit festgelegten Trefferpositionen über die "
     "Pfadregel ohne Binomialkoeffizient bestimmen.",
     "2017-bb-ea-B4.2a"),
    ("Kumulierte Wahrscheinlichkeit einer Binomialverteilung berechnen", "Stochastik",
     "Binomialverteilung",
     "Ein Ereignis wie mindestens oder mehr als k Treffer in Einzelfälle zerlegen und die "
     "Wahrscheinlichkeiten summieren oder über das Gegenereignis bestimmen.",
     "2017-bb-ea-B4.2a"),
    ("Mindestanzahl von Versuchen einer Bernoulli-Kette über das Gegenereignis bestimmen",
     "Stochastik", "Binomialverteilung",
     "Die kleinste Zahl unabhängiger Wiederholungen bestimmen, für die mindestens ein Treffer mit "
     "vorgegebener Mindestwahrscheinlichkeit auftritt, über das Gegenereignis und Logarithmieren.",
     "2017-bb-ea-B4.2b"),
    ("Anteil einer Teilgruppe aus der totalen Wahrscheinlichkeit berechnen", "Stochastik",
     "Bedingte Wahrscheinlichkeit und Bayes",
     "Den unbekannten Anteil einer Teilgruppe bestimmen, indem die Gesamtwahrscheinlichkeit als "
     "gewichtete Summe der bedingten Wahrscheinlichkeiten angesetzt und die Gleichung gelöst "
     "wird.",
     "2017-bb-ea-B4.2c"),
    ("Modalwert einer Binomialverteilung bestimmen", "Stochastik", "Binomialverteilung",
     "Die Trefferzahl mit der größten Einzelwahrscheinlichkeit bestimmen, indem die Werte in der "
     "Umgebung des Erwartungswerts verglichen werden.",
     "2017-bb-ea-B4.2d"),
    ("Ungeeignetheit des Binomialmodells begründen", "Stochastik", "Binomialverteilung",
     "Begründen, dass eine Situation nicht binomialverteilt ist, weil ohne Zurücklegen gezogen "
     "wird und die Trefferwahrscheinlichkeit deshalb nicht gleich bleibt.",
     "2017-bb-ea-B4.2e"),
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
