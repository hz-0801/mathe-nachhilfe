# -*- coding: utf-8 -*-
"""abi-bau.py – Gerüst für die Erfassung eines Hefts im Profil abi.
Version 0.2 · 12.09.2026 · gilt mit katalog-prompt.md v0.3 und abi.md v0.3

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
    "papier": "2018-bb-ea",
    "datei": "BB_18_Ma_Aufgaben.pdf",
    "seiten": 13,
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


_ABB = ("Kartesisches Koordinatensystem, x-Achse von −5 bis 5 mit den ganzen Zahlen beschriftet, "
        "y-Achse von 0 bis 5 mit den ganzen Zahlen beschriftet, Achsen mit x und y benannt. "
        "Dargestellt ist der Graph von f(x) = 4 · x^(−2): zwei zur y-Achse spiegelbildliche Äste, "
        "beide vollständig oberhalb der x-Achse. Der rechte Ast fällt von der y-Achse aus steil "
        "ab, verläuft durch (1 | 4) und (2 | 1) und nähert sich der x-Achse; der linke Ast "
        "entsprechend durch (−1 | 4) und (−2 | 1). Beide Äste schmiegen sich an die y-Achse an "
        "und sind nach oben offen. Keine weiteren Beschriftungen.")

_ST11 = ("Die in IR ohne {0} definierte Funktion f mit f(x) = 4 · x^(−2); ihr Graph heißt Gf und "
         "ist symmetrisch bezüglich der y-Achse. Eine Abbildung zeigt Gf im Bereich von −5 bis 5. ")

row(id="2018-bb-ea-A1.1a", block="A", aufgabe="1.1", titel="Analysis", teilaufgabe="a",
    seite="2", punkte="2",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Parameter einer Parallelen zur x-Achse aus einer Abstandsbedingung berechnen",
    typ_neben="",
    stichwoerter="Potenzfunktion|Parallele zur x-Achse|Schnittpunkte|Achsensymmetrie|Abstand",
    voraussetzungen="Potenzgleichung mit negativem Exponenten lösen|Abstand zweier Punkte auf einer Parallelen zur x-Achse als Differenz der x-Werte erkennen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=_ABB, kontext="ohne", textumfang="mittel",
    gegeben=_ST11 + "Die Gerade, die parallel zur x-Achse durch den Punkt P(0 | p) verläuft, "
            "schneidet Gf in zwei Punkten. Der Abstand dieser beiden Schnittpunkte hat die Länge 1.",
    gesucht="Wert von p",
    verfahren="Die Parallele hat die Gleichung y = p. Aus 4 · x^(−2) = p folgen die Schnittstellen "
              "x = ±2/√p. Wegen der Symmetrie zur y-Achse ist der Abstand der Schnittpunkte "
              "4/√p; aus 4/√p = 1 folgt √p = 4 und damit p.",
    schritte="4", zahlenraum="Bruch|dezimal|ganz|negativ|Potenz|Wurzel", einheiten="",
    abhaengig_von="",
    ergebnis="p = 16; die Schnittpunkte sind (−0,5 | 16) und (0,5 | 16).",
    zwischenergebnis="Schnittstellen x = ±2/√p|Abstand der Schnittpunkte 4/√p|√p = 4",
    niveau_geschaetzt="II",
    fehlerquelle="den Abstand der beiden Schnittpunkte mit der x-Koordinate eines Schnittpunkts "
                 "verwechseln und 2/√p = 1 ansetzen, was p = 4 liefert",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Analysis, a) 2 BE). "
              "Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-A1.1b", block="A", aufgabe="1.1", titel="Analysis", teilaufgabe="b",
    seite="2", punkte="3",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Tangente aus einer Bedingung an das Achsenabschnittsdreieck bestimmen",
    typ_neben="",
    stichwoerter="Tangente|Achsenabschnitte|gleichschenkliges Dreieck|Berührstelle|Potenzfunktion",
    voraussetzungen="Ableitung einer Potenzfunktion mit negativem Exponenten bilden|Tangentengleichung aufstellen|Achsenabschnitte einer Geraden berechnen|Gleichung dritten Grades der Form u³ = 8 lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=_ABB, kontext="ohne", textumfang="mittel",
    gegeben=_ST11 + "Die Koordinatenachsen schließen mit der Tangente an Gf in einem Punkt "
            "Q(u | f(u)) mit u > 0 ein gleichschenkliges Dreieck ein.",
    gesucht="Koordinaten von Q",
    verfahren="f′(x) = −8 · x^(−3) bilden und die Tangente in Q aufstellen. Ihre Achsenabschnitte "
              "sind 3u/2 auf der x-Achse und 12/u² auf der y-Achse. Das Dreieck ist rechtwinklig, "
              "gleichschenklig kann es deshalb nur mit gleich langen Katheten sein: 3u/2 = 12/u² "
              "liefert u³ = 8, also u = 2; damit f(2) berechnen.",
    schritte="6", zahlenraum="Bruch|ganz|negativ|Potenz", einheiten="",
    abhaengig_von="",
    ergebnis="Q(2 | 1); die zugehörige Tangente ist t(x) = 3 − x und schneidet beide Achsen "
             "im Abstand 3 vom Ursprung.",
    zwischenergebnis="f′(x) = −8 · x^(−3)|Achsenabschnitt auf der x-Achse 3u/2|Achsenabschnitt auf "
                     "der y-Achse 12/u²|u³ = 8",
    niveau_geschaetzt="III",
    fehlerquelle="gleichschenklig als Gleichheit von Kathete und Hypotenuse deuten, statt die "
                 "beiden auf den Achsen liegenden Katheten gleichzusetzen",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Analysis, b) 3 BE). "
              "Dass nur die Katheten gleich sein können, muss der Prüfling selbst erkennen; das "
              "hebt die Teilaufgabe auf Niveau III. Eigene Rechnung, mit sympy bestätigt.")

_ST13 = ("Ein Landwirt plant für sein Hoffest ein Glücksrad aus blauen, gelben und roten Sektoren "
         "von je 6°. Ein Dreh kostet einen Euro. Gelb bringt einen Gutschein für eine Packung "
         "Bio-Eier, blau als Hauptgewinn einen Ökokorb, bei rot geht man leer aus. Eine Packung "
         "Bio-Eier kostet den Landwirt 1,50 €, ein Ökokorb 15 €. Die Wahrscheinlichkeit für den "
         "Hauptgewinn soll 5 % betragen, die Chance auf einen Gutschein ein Drittel. ")

row(id="2018-bb-ea-A1.3a", block="A", aufgabe="1.3", titel="Stochastik", teilaufgabe="a",
    seite="3", punkte="3",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Sektorenzahlen eines Glücksrads aus Wahrscheinlichkeiten ermitteln",
    typ_neben="",
    stichwoerter="Glücksrad|Laplace-Experiment|Sektoren zu 6 Grad|Anteil einer Gesamtzahl|Restbestimmung",
    voraussetzungen="Vollwinkel in gleich große Sektoren teilen|Prozentsatz und Bruchteil einer Anzahl berechnen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksrad auf einem Hoffest", textumfang="lang",
    gegeben=_ST13,
    gesucht="Anzahl der blauen, der gelben und der roten Sektoren",
    verfahren="Aus 360° geteilt durch 6° folgen 60 gleich große Sektoren; das Rad ist damit ein "
              "Laplace-Experiment und jede Wahrscheinlichkeit ist der Anteil an diesen 60. "
              "Blau: 5 % von 60; gelb: ein Drittel von 60; rot als Rest zu 60.",
    schritte="4", zahlenraum="Bruch|ganz|Prozent", einheiten="°",
    abhaengig_von="",
    ergebnis="3 blaue, 20 gelbe und 37 rote Sektoren",
    zwischenergebnis="360° : 6° = 60 Sektoren insgesamt",
    niveau_geschaetzt="II",
    fehlerquelle="die Gesamtzahl der Sektoren nicht bestimmen und die Anteile auf 360 Sektoren "
                 "oder auf 100 beziehen",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Stochastik, a) 3 BE). "
              "Die Seite trägt die Kopfzeile 2016; die Aufgabe ist unbereinigt aus dem Heft 2016 "
              "übernommen. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-A1.3b", block="A", aufgabe="1.3", titel="Stochastik", teilaufgabe="b",
    seite="3", punkte="2",
    leitidee="Stochastik", thema="Kenngrößen von Verteilungen",
    typ="Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen",
    typ_neben="",
    stichwoerter="Erwartungswert|auf lange Sicht|Kosten je Dreh|Zufallsgröße|Glücksrad",
    voraussetzungen="Werte einer Zufallsgröße aus dem Sachtext ablesen|mit Prozentsatz und Bruchteil multiplizieren",
    format="Rechnung", operator="Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Glücksrad auf einem Hoffest", textumfang="lang",
    gegeben=_ST13,
    gesucht="Kosten, die dem Landwirt pro Dreh auf lange Sicht entstehen",
    verfahren="Die Kosten je Dreh als Zufallsgröße auffassen: 15 € bei blau, 1,50 € bei gelb, 0 € "
              "bei rot. Den Erwartungswert als Summe der mit den Wahrscheinlichkeiten gewichteten "
              "Werte bilden: 15 · 0,05 + 1,50 · 1/3 + 0.",
    schritte="3", zahlenraum="Bruch|dezimal|Prozent", einheiten="€",
    abhaengig_von="",
    ergebnis="1,25 € Kosten pro Dreh auf lange Sicht",
    zwischenergebnis="15 € · 0,05 = 0,75 €|1,50 € · 1/3 = 0,50 €",
    niveau_geschaetzt="II",
    fehlerquelle="die Einnahme von einem Euro gegenrechnen und 0,25 € angeben, obwohl nach den "
                 "Kosten und nicht nach dem Saldo gefragt ist",
    bemerkung="BE aus der gesammelten Tabelle am Ende von Teil 1 (Teilgebiet Stochastik, b) 2 BE). "
              "Gefragt ist nach den Kosten; mit der Einnahme von einem Euro verrechnet bliebe ein "
              "Verlust von 0,25 € je Dreh. Ohne amtliche Lösung ist nicht auszuschließen, dass der "
              "Erwartungshorizont den Saldo verlangt. Die Seite trägt die Kopfzeile 2016. "
              "Eigene Rechnung, mit sympy bestätigt.")

_ST22 = ("Funktionenschar f_a mit f_a(x) = (1/a)·x³ + 3x² + 5x + 2a; x ∈ IR, a ∈ IR, a ≠ 0, und "
         "die Funktion h mit h(x) = −(1/2)·x^(−3); x ∈ IR, x ≠ 0. Die zugehörigen Graphen sind "
         "G_a und K. ")

_SACH = ("Ein Gartenbesitzer hat in einer Ecke seines Gartens einen Teich angelegt. Der Rand des "
         "Teiches an der Wasseroberfläche wird durch Teile der Graphen G_2 und K modelliert. Im "
         "Intervall von −3 bis −2 verläuft eine Brücke über den Teich; 1 LE = 1 m. Eine "
         "Darstellung zeigt Teichoberfläche und Brücke senkrecht von oben betrachtet. ")

_ABB22 = ("Kartesisches Koordinatensystem, x-Achse von −4 bis 0 mit den ganzen Zahlen beschriftet, "
          "y-Achse von −1 bis 3 mit den ganzen Zahlen beschriftet. Zwei Kurvenstücke umranden "
          "gemeinsam eine geschlossene, längliche Fläche: der mit G_2 beschriftete Bogen läuft von "
          "(−4 | 0) steil aufwärts zu einem Hochpunkt bei etwa (−2,8 | 2,5), fällt zu einem "
          "flachen Tiefpunkt bei etwa (−1,2 | 1,5) und steigt wieder bis etwa (−0,64 | 1,9); das "
          "mit K beschriftete Kurvenstück läuft von (−4 | 0) flach knapp oberhalb der x-Achse nach "
          "rechts und biegt ab etwa x = −1 steil nach oben bis (−0,64 | 1,9). Über dem senkrechten "
          "Streifen zwischen x = −3 und x = −2 liegt ein blassrot hinterlegtes Rechteck, das die "
          "Brücke darstellt; es reicht oben und unten über die Fläche hinaus.")

row(id="2018-bb-ea-B2.2a", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="a",
    seite="7", punkte="6",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Punktsymmetrie am Funktionsterm begründen",
    typ_neben="Grenzverhalten einer Potenzfunktion untersuchen|Ausschluss eines Parameterwerts über das Grenzverhalten begründen",
    stichwoerter="Punktsymmetrie|ungerader Exponent|Grenzwert null|ganzrationale Funktion dritten Grades|Nichtexistenz eines Parameters",
    voraussetzungen="h(−x) bilden und mit −h(x) vergleichen|Grenzwert einer Potenz mit negativem Exponenten kennen|Grenzverhalten einer ganzrationalen Funktion am Grad und am Leitkoeffizienten ablesen",
    format="Kurzantwort|Begründung", operator="Geben Sie an|Begründen Sie|Bestimmen Sie",
    antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=_ST22,
    gesucht="vorliegende Symmetrie des Graphen K mit Begründung|Verhalten der Funktionswerte von h "
            "für x → +∞|Begründung, dass es keine reelle Zahl a gibt, für die die Grenzwerte von h "
            "und von f_a für x → +∞ übereinstimmen",
    verfahren="Aus h(−x) = (1/2)·x^(−3) = −h(x) folgt Punktsymmetrie zum Ursprung; gleichwertig ist "
              "der Hinweis auf den ungeraden Exponenten. Für x → +∞ geht x^(−3) gegen null, also "
              "h(x) gegen null. f_a ist ganzrational vom Grad 3 mit dem Leitkoeffizienten 1/a ≠ 0; "
              "ihre Werte streben für x → +∞ deshalb gegen +∞ oder gegen −∞, niemals gegen null.",
    schritte="4", zahlenraum="Bruch|ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="K ist punktsymmetrisch zum Ursprung, weil h(−x) = −h(x) gilt|für x → +∞ geht h(x) "
             "gegen 0, und zwar von unten|es gibt kein solches a, weil der Grenzwert von h null "
             "ist, der von f_a wegen 1/a ≠ 0 aber immer +∞ oder −∞",
    zwischenergebnis="h(−x) = (1/2)·x^(−3)|Leitkoeffizient von f_a ist 1/a",
    niveau_geschaetzt="II",
    fehlerquelle="die Punktsymmetrie nur behaupten statt über h(−x) = −h(x) oder den ungeraden "
                 "Exponenten zu begründen",
    bemerkung="Drei Leistungen in einer Einheit; thema folgt dem ersten Typ, der Schwerpunkt liegt "
              "jedoch bei den Grenzwerten. Die dritte Leistung allein wäre Niveau III, für die "
              "Einheit insgesamt ist II geschätzt. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B2.2b", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="b",
    seite="7", punkte="7",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Flächeninhalt des Achsenabschnittsdreiecks einer Tangente berechnen",
    typ_neben="Tangentengleichung an einer Stelle ermitteln",
    stichwoerter="Tangente|Berührpunkt|Achsenabschnitte|rechtwinkliges Dreieck|Flächeninhalt",
    voraussetzungen="Ableitung einer Potenzfunktion mit negativem Exponenten bilden|Nullstelle einer linearen Funktion berechnen|Flächeninhalt eines rechtwinkligen Dreiecks aus den Katheten bilden",
    format="Rechnung", operator="Ermitteln Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=_ST22 + "Die Tangente an K im Punkt P(−1 | h(−1)) und die beiden Koordinatenachsen "
            "begrenzen ein Dreieck.",
    gesucht="Flächeninhalt dieses Dreiecks",
    verfahren="h(−1) = 0,5 berechnen, h′(x) = (3/2)·x^(−4) bilden und h′(−1) = 1,5 als Anstieg "
              "nehmen. Die Tangente t(x) = 1,5x + 2 schneidet die y-Achse bei 2 und die x-Achse "
              "bei −4/3. Diese beiden Abschnitte sind die Katheten des rechtwinkligen Dreiecks; "
              "der Flächeninhalt ist ihr halbes Produkt, mit Beträgen gerechnet.",
    schritte="5", zahlenraum="Bruch|dezimal|ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="A = 4/3 ≈ 1,33 Flächeneinheiten",
    zwischenergebnis="P(−1 | 0,5)|h′(x) = (3/2)·x^(−4)|t(x) = 1,5x + 2|Achsenabschnitte −4/3 und 2",
    niveau_geschaetzt="II",
    fehlerquelle="den negativen x-Achsenabschnitt ohne Betrag in die Flächenformel einsetzen und "
                 "einen negativen Flächeninhalt erhalten",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B2.2c", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="c",
    seite="7", punkte="2",
    leitidee="Analysis", thema="Kurvenuntersuchung",
    typ="Fehlen von Extrempunkten über das Vorzeichen der Ableitung begründen",
    typ_neben="",
    stichwoerter="lokale Extrempunkte|notwendige Bedingung|gerader Exponent|stets positiv|strenge Monotonie",
    voraussetzungen="Ableitung einer Potenzfunktion mit negativem Exponenten bilden|Vorzeichen einer Potenz mit geradem Exponenten beurteilen",
    format="Begründung", operator="Begründen Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=_ST22,
    gesucht="Begründung, dass der Graph K keine lokalen Extrempunkte besitzt",
    verfahren="h′(x) = (3/2)·x^(−4) bilden. Wegen des geraden Exponenten ist x^(−4) für jedes "
              "x ≠ 0 positiv, also h′(x) > 0. Die notwendige Bedingung h′(x) = 0 ist damit "
              "nirgends erfüllt.",
    schritte="2", zahlenraum="Bruch|ganz|negativ|Potenz", einheiten="", abhaengig_von="",
    ergebnis="K hat keine lokalen Extrempunkte, weil h′(x) = (3/2)·x^(−4) für alle x ≠ 0 größer "
             "als null ist; h steigt auf beiden Definitionsintervallen streng monoton.",
    zwischenergebnis="h′(x) = (3/2)·x^(−4)",
    niveau_geschaetzt="II",
    fehlerquelle="aus h′(x) ≠ 0 auf globale Monotonie über die Definitionslücke hinweg schließen",
    bemerkung="Typ getrennt von „Fehlen von Extrempunkten einer Schar über die Diskriminante nachweisen“ (2.1 d): dort "
              "wird über die Diskriminante argumentiert, hier über das Vorzeichen einer Potenz. "
              "Vorschlag zur Typenliste steht im Bericht. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B2.2d", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="d",
    seite="7", punkte="6",
    leitidee="Analysis", thema="Tangente, Normale, Schnittwinkel",
    typ="Stellen mit vorgegebenem Tangentenanstieg nachweisen",
    typ_neben="",
    stichwoerter="Tangentenanstieg|Ableitung gleich 1,5|quadratische Gleichung|Diskriminante|genau zwei Lösungen",
    voraussetzungen="Parameterwert in den Scharterm einsetzen|ganzrationale Funktion ableiten|quadratische Gleichung lösen und die Lösungsanzahl an der Diskriminante ablesen",
    format="Rechnung|Begründung", operator="Zeigen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=_ST22 + "Betrachtet wird der Graph G_2, also der Graph von f_2.",
    gesucht="Nachweis, dass es auf G_2 genau zwei Punkte mit dem Tangentenanstieg m = 1,5 gibt",
    verfahren="a = 2 einsetzen, also f_2(x) = 0,5x³ + 3x² + 5x + 4, und ableiten zu "
              "f_2′(x) = 1,5x² + 6x + 5. Dann f_2′(x) = 1,5 setzen; die quadratische Gleichung "
              "1,5x² + 6x + 3,5 = 0 hat die Diskriminante 15 > 0 und damit genau zwei Lösungen. "
              "Das begründet die Anzahl der Punkte.",
    schritte="4", zahlenraum="dezimal|ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="genau zwei Stellen, x = −2 ± √15/3, also x1 ≈ −3,29 und x2 ≈ −0,71; die Punkte sind "
             "rund (−3,29 | 2,22) und (−0,71 | 1,78).",
    zwischenergebnis="f_2(x) = 0,5x³ + 3x² + 5x + 4|f_2′(x) = 1,5x² + 6x + 5|1,5x² + 6x + 3,5 = 0|"
                     "Diskriminante 36 − 21 = 15",
    niveau_geschaetzt="II",
    fehlerquelle="f_2′(x) = 0 statt f_2′(x) = 1,5 setzen und damit die Extremstellen statt der "
                 "gesuchten Stellen berechnen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B2.2e", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="e",
    seite="7", punkte="9",
    leitidee="Analysis", thema="Funktionsscharen und Ortskurven",
    typ="Parameterwert für genau eine waagerechte Tangente bestimmen",
    typ_neben="Nachweisverfahren für einen Sattelpunkt erläutern",
    stichwoerter="waagerechte Tangente|genau eine Lösung|Diskriminante null|Sattelpunkt|Nachweisverfahren beschreiben",
    voraussetzungen="Scharterm nach x ableiten|Diskriminante einer quadratischen Gleichung aufstellen|hinreichende Bedingung für einen Sattelpunkt kennen",
    format="Rechnung|Begründung", operator="Bestimmen Sie|Erläutern Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="lang",
    gegeben=_ST22 + "Es gibt einen Wert des Parameters a, für den der Graph G_a genau einen Punkt "
            "mit waagerechter Tangente besitzt.",
    gesucht="dieser Parameterwert a|Erläuterung, wie sich nachweisen ließe, dass G_a für diesen "
            "Parameterwert dort einen Sattelpunkt besitzt",
    verfahren="f_a′(x) = (3/a)·x² + 6x + 5 ist quadratisch; genau eine Nullstelle bedeutet "
              "Diskriminante null, also 36 − 60/a = 0 und damit a = 5/3. Für den zweiten Teil "
              "genügt die Beschreibung des Verfahrens: zweite Ableitung an der Stelle null und "
              "dritte Ableitung dort ungleich null, gleichwertig ein Vorzeichenwechsel der zweiten "
              "Ableitung; die Rechnung ist nicht verlangt.",
    schritte="4", zahlenraum="Bruch|dezimal|ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="a = 5/3; die waagerechte Tangente liegt bei x = −5/3. Nachweis des Sattelpunkts über "
             "f′′(−5/3) = 0 zusammen mit f′′′(−5/3) = 3,6 ≠ 0 oder über den Vorzeichenwechsel von "
             "f′′ an dieser Stelle.",
    zwischenergebnis="f_a′(x) = (3/a)·x² + 6x + 5|Diskriminante 36 − 60/a|f′(x) = 1,8x² + 6x + 5|"
                     "f′′(x) = 3,6x + 6",
    niveau_geschaetzt="III",
    fehlerquelle="„genau ein Punkt mit waagerechter Tangente“ mit „genau ein Extrempunkt“ "
                 "verwechseln, oder den Fall a < 0 nicht prüfen, in dem die Diskriminante stets "
                 "positiv ist",
    bemerkung="Die zweite Leistung verlangt ausdrücklich nur die Erläuterung des Verfahrens, nicht "
              "die Durchführung; das Ergebnisfeld nennt sie trotzdem, damit die Zeile für ein "
              "Blatt reicht. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B2.2f", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="f",
    seite="7", punkte="9",
    leitidee="Analysis", thema="Funktionsklassen und Eigenschaften",
    typ="Punktprobe mit gerundeten Koordinaten durchführen",
    typ_neben="Umschließendes achsenparalleles Rechteck zu einer krummlinig begrenzten Fläche bestimmen",
    stichwoerter="Punktprobe|Rundung der y-Koordinaten|Schnittpunkte der Randkurven|achsenparalleles Rechteck|lokaler Hochpunkt",
    voraussetzungen="Funktionswerte einsetzen und runden|Extremstellen über die erste Ableitung bestimmen|waagerechte und senkrechte Ausdehnung einer Fläche unterscheiden",
    format="Rechnung|Begründung", operator="Zeigen Sie|Berechnen Sie", antwort="Text|Zahl",
    material="Koordinatensystem", skizze=_ABB22, kontext="Gartenteich", textumfang="lang",
    gegeben=_ST22 + _SACH + "Gegeben sind die Punkte P1(−4 | 0) und P2(−0,64 | 1,9). Der Teich "
            "wird kurzzeitig durch eine rechteckige Plane abgedeckt, deren Seiten parallel zu den "
            "Koordinatenachsen liegen.",
    gesucht="Nachweis, dass P1 und P2 bei entsprechender Rundung der y-Koordinaten auf beiden zur "
            "Modellierung verwendeten Graphen liegen|Seitenlängen, die die Plane mindestens haben "
            "muss",
    verfahren="Für die Punktprobe beide x-Werte sowohl in f_2 als auch in h einsetzen und die "
              "Funktionswerte auf eine Nachkommastelle runden. Für die Plane die waagerechte Seite "
              "als Differenz der beiden x-Werte nehmen und die senkrechte als Abstand zwischen dem "
              "tiefsten Randpunkt (y = 0 bei P1) und dem lokalen Hochpunkt von G_2; dazu "
              "f_2′(x) = 0 lösen und den Funktionswert berechnen.",
    schritte="7", zahlenraum="Bruch|dezimal|ganz|negativ|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="f_2(−4) = 0 und h(−4) = 1/128 ≈ 0,0; f_2(−0,64) ≈ 1,898 und h(−0,64) ≈ 1,907, beide "
             "gerundet 1,9 – beide Punkte liegen damit auf beiden Graphen. Der Hochpunkt von G_2 "
             "liegt bei x = −2 − √6/3 ≈ −2,816 mit y ≈ 2,544. Die Plane muss mindestens 3,36 m "
             "lang und rund 2,55 m breit sein.",
    zwischenergebnis="f_2(−4) = 0|h(−4) ≈ 0,0078|f_2(−0,64) ≈ 1,8977|h(−0,64) ≈ 1,9073|"
                     "Extremstellen von f_2 bei x = −2 ± √6/3|Hochpunkt (−2,816 | 2,544)",
    niveau_geschaetzt="III",
    fehlerquelle="für die senkrechte Seite nur die y-Werte der beiden gegebenen Punkte vergleichen "
                 "und den dazwischenliegenden Hochpunkt von G_2 übersehen",
    bemerkung="P1 und P2 sind die beiden Stellen, an denen die Randkurven G_2 und K "
              "zusammentreffen; die Punktprobe gilt deshalb für beide Graphen. Eigene Rechnung, "
              "mit sympy bestätigt.")

row(id="2018-bb-ea-B2.2g", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="g",
    seite="8|7", punkte="5",
    leitidee="Analysis", thema="Flächeninhalt durch Integration",
    typ="Fläche zwischen zwei Graphen berechnen",
    typ_neben="",
    stichwoerter="senkrechter Lichteinfall|Schattenstreifen|Fläche zwischen zwei Graphen|Integrationsgrenzen aus dem Sachtext|Stammfunktion",
    voraussetzungen="Sachsituation in Integrationsgrenzen übersetzen|Stammfunktion einer Potenz mit negativem Exponenten bilden|bestimmtes Integral auswerten",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Koordinatensystem", skizze=_ABB22, kontext="Gartenteich", textumfang="lang",
    gegeben=_ST22 + _SACH + "Senkrecht zur Teichoberfläche einfallendes Licht erzeugt durch die "
            "Brücke einen Schatten, der zum Teil auf der Wasseroberfläche liegt.",
    gesucht="Größe der Wasseroberfläche, die in diesem Fall im Schatten liegt",
    verfahren="Bei senkrechtem Lichteinfall deckt sich der Schatten mit dem Grundriss der Brücke; "
              "auf dem Wasser ist das genau der Teil der Teichfläche über dem Intervall von −3 bis "
              "−2. Diese Fläche liegt zwischen dem oberen Rand G_2 und dem unteren Rand K, also "
              "das Integral von −3 bis −2 über f_2(x) − h(x) bilden.",
    schritte="4", zahlenraum="Bruch|dezimal|ganz|negativ|Potenz", einheiten="m²", abhaengig_von="",
    ergebnis="A = 337/144 ≈ 2,34 m²",
    zwischenergebnis="Integrand f_2(x) − h(x) = 0,5x³ + 3x² + 5x + 4 + (1/2)·x^(−3)|"
                     "Stammfunktion 0,125x⁴ + x³ + 2,5x² + 4x − (1/4)·x^(−2)",
    niveau_geschaetzt="II",
    fehlerquelle="nur das Integral über f_2 bilden und die untere Randkurve K weglassen",
    bemerkung="Aufgabenseite 8, die zugehörige Abbildung steht auf Seite 7. Der Typ ist der "
              "vorhandene aus 2.1 c; der Lösungsweg ist derselbe. Eigene Rechnung, mit sympy "
              "bestätigt.")

row(id="2018-bb-ea-B2.2h", block="B", aufgabe="2.2", titel="Gartenteich", teilaufgabe="h",
    seite="8", punkte="6",
    leitidee="Analysis", thema="Rekonstruktion von Funktionsgleichungen",
    typ="Ganzrationale Funktion aus Symmetrie und Randbedingungen rekonstruieren",
    typ_neben="Steigungswinkel in einen Anstieg umrechnen",
    stichwoerter="ganzrationale Funktion vierten Grades|Achsensymmetrie|nur gerade Exponenten|Steigungswinkel 45 Grad|lineares Gleichungssystem",
    voraussetzungen="Ansatz aus der Symmetrie aufstellen|Sachangaben in Funktionswerte und Ableitungswerte übersetzen|lineares Gleichungssystem mit zwei Unbekannten lösen",
    format="Rechnung", operator="Ermitteln Sie", antwort="Term",
    material="keins", skizze="keine", kontext="Gartenteich", textumfang="mittel",
    gegeben="Über den Gartenteich führt eine Brücke. Sie soll in einem neuen x-y-Koordinatensystem "
            "durch eine ganzrationale Funktion 4. Grades modelliert werden, die symmetrisch zur "
            "y-Achse verläuft. Die Brücke hat eine Spannweite von 4 Metern, ist in der Mitte "
            "0,5 Meter hoch über der x-Achse und hat an den beiden Enden einen Steigungswinkel von "
            "45° bzw. −45°.",
    gesucht="Gleichung dieser Funktion vierten Grades",
    verfahren="Die Achsensymmetrie lässt nur gerade Exponenten zu: Ansatz p(x) = ax⁴ + bx² + c. "
              "Die Mitte liegt bei x = 0, also c = 0,5. Die Spannweite 4 legt die Enden auf "
              "x = ±2 mit p(2) = 0. Der Steigungswinkel −45° am rechten Ende bedeutet "
              "p′(2) = tan(−45°) = −1. Aus 16a + 4b = −0,5 und 32a + 4b = −1 folgen a und b.",
    schritte="5", zahlenraum="Bruch|dezimal|ganz|negativ|Potenz", einheiten="m", abhaengig_von="",
    ergebnis="p(x) = −(1/32)·x⁴ + 0,5",
    zwischenergebnis="Ansatz p(x) = ax⁴ + bx² + c|c = 0,5|p(2) = 0 liefert 16a + 4b = −0,5|"
                     "p′(2) = −1 liefert 32a + 4b = −1|a = −1/32 und b = 0",
    niveau_geschaetzt="II",
    fehlerquelle="den Steigungswinkel unmittelbar als Anstieg einsetzen, statt über den Tangens zu "
                 "gehen, oder am rechten Ende mit +1 statt −1 rechnen",
    bemerkung="Das Heft nennt das Ergebnis „Parabel“, gemeint ist die ganzrationale Funktion "
              "vierten Grades. Eigene Rechnung, mit sympy bestätigt.")


_ABB31 = ("Schrägbild eines Körpers ohne Koordinatensystem. Oben liegt die Spitze G; von ihr führen "
          "Kanten zu den Ecken eines waagerecht liegenden, grau getönten Dreiecks DEF mit F links, "
          "E rechts und D vorn in der Mitte. Darunter liegt ein kleineres, ebenfalls grau getöntes "
          "Dreieck ABC mit C links, B rechts und A vorn. Die Seitenkanten FC, DA und EB verbinden "
          "die beiden Dreiecke zum Körper. Von C, A und B laufen gestrichelte Linien nach unten "
          "aufeinander zu und treffen sich in einem mit S bezeichneten Punkt unterhalb des "
          "Körpers. Die Abbildung trägt keine Maßangaben.")

_ST31 = ("Das Gebäude eines Museums wird modellhaft durch den abgebildeten Körper ABCDEFG "
         "dargestellt. Die obere Etage entspricht der Pyramide DEFG, die untere Etage dem Körper "
         "ABCDEF, der Teil der Pyramide DEFS ist. Das Dreieck ABC liegt in der x-y-Ebene, das "
         "Dreieck DEF parallel dazu. Im kartesischen Koordinatensystem gilt A(−5 | 5 | 0), "
         "B(−5 | 25 | 0), D(0 | 0 | 15), E(0 | 30 | 15), F(−25 | 5 | 15) und G(−10 | 10 | 35). "
         "Eine Längeneinheit entspricht 1 m in der Realität. ")

row(id="2018-bb-ea-B3.1a", block="B", aufgabe="3.1", titel="Museum", teilaufgabe="a",
    seite="9", punkte="4",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Gegebene Rechnung zum Geradenschnittpunkt erläutern",
    typ_neben="",
    stichwoerter="vorgegebene Rechnung deuten|Geraden DA und EB|Gleichsetzen|Gleichungssystem|Einsetzen des Parameters",
    voraussetzungen="Parameterform einer Geraden aus zwei Punkten erkennen|Gleichsetzungsverfahren kennen|Ortsvektor als Punkt lesen",
    format="Begründung", operator="Erläutern Sie", antwort="Text",
    material="Körper", skizze=_ABB31, kontext="Museumsgebäude", textumfang="lang",
    gegeben=_ST31 + "Abgedruckt ist eine Rechnung: zuerst wird (0 | 0 | 15) + r · (−5 | 5 | −15) "
            "gleich (0 | 30 | 15) + s · (−5 | −5 | −15) gesetzt, woraus r = s = 3 folgt; danach "
            "wird r = 3 eingesetzt und S(−15 | 15 | −30) abgelesen.",
    gesucht="Erläuterung des dargestellten Vorgehens zur Ermittlung der Koordinaten von S",
    verfahren="Erkennen, dass die beiden Terme die Geraden durch D und A sowie durch E und B in "
              "Parameterform sind, denn A − D = (−5 | 5 | −15) und B − E = (−5 | −5 | −15). Das "
              "Gleichsetzen sucht den gemeinsamen Punkt der beiden Seitenkanten, das "
              "Gleichungssystem liefert r = s = 3, und das Einsetzen in eine der beiden Geraden "
              "liefert den Ortsvektor der Pyramidenspitze S.",
    schritte="3", zahlenraum="ganz|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Die beiden Zeilen sind die Geraden DA und EB; ihr Schnittpunkt ist die Spitze S der "
             "Pyramide DEFS. Das Gleichsetzen der Parameterformen liefert r = s = 3, das Einsetzen "
             "von r = 3 in die erste Gerade den Punkt S(−15 | 15 | −30).",
    zwischenergebnis="Richtungsvektor DA = (−5 | 5 | −15)|Richtungsvektor EB = (−5 | −5 | −15)|r = s = 3",
    niveau_geschaetzt="II",
    fehlerquelle="die Rechnung nachvollziehen, ohne die beiden Terme als die Seitenkanten DA und "
                 "EB des Körpers zu benennen",
    bemerkung="Erste Zeile des Katalogs, in der eine fertige Rechnung gedeutet statt durchgeführt "
              "wird; die Leistung sitzt vollständig im Erläutern. Eigene Rechnung, mit sympy "
              "bestätigt.")

row(id="2018-bb-ea-B3.1b", block="B", aufgabe="3.1", titel="Museum", teilaufgabe="b",
    seite="9", punkte="3",
    leitidee="Analytische Geometrie", thema="Orthogonalität",
    typ="Rechtwinkligkeit eines Dreiecks über Skalarprodukte ausschließen",
    typ_neben="",
    stichwoerter="Bodenfläche der oberen Etage|Dreieck DEF|Skalarprodukt|kein rechter Winkel|drei Innenwinkel prüfen",
    voraussetzungen="Verbindungsvektoren aus Punktkoordinaten bilden|Skalarprodukt berechnen|wissen, dass ein Skalarprodukt null genau bei Orthogonalität auftritt",
    format="Begründung", operator="Weisen Sie nach", antwort="Text",
    material="Körper", skizze=_ABB31, kontext="Museumsgebäude", textumfang="lang",
    gegeben=_ST31 + "Die Bodenfläche der oberen Etage ist das Dreieck DEF.",
    gesucht="Nachweis, dass das Dreieck DEF nicht rechtwinklig ist",
    verfahren="Die sechs Verbindungsvektoren bilden und für jede der drei Ecken das Skalarprodukt "
              "der beiden anliegenden Seitenvektoren berechnen. Ist keines davon null, gibt es "
              "keinen rechten Winkel.",
    schritte="4", zahlenraum="ganz|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Bei D ist DE · DF = 150, bei E ist ED · EF = 750, bei F ist FD · FE = 500; kein "
             "Skalarprodukt ist null, also ist das Dreieck DEF nicht rechtwinklig.",
    zwischenergebnis="DE = (0 | 30 | 0)|DF = (−25 | 5 | 0)|EF = (−25 | −25 | 0)",
    niveau_geschaetzt="II",
    fehlerquelle="nur ein Skalarprodukt prüfen und aus dem einen Wert ungleich null auf das ganze "
                 "Dreieck schließen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B3.1c", block="B", aufgabe="3.1", titel="Museum", teilaufgabe="c",
    seite="9", punkte="5",
    leitidee="Analytische Geometrie", thema="Skalarprodukt und Winkel",
    typ="Innenwinkel eines Dreiecks über das Skalarprodukt berechnen",
    typ_neben="Höhe eines Dreiecks im Raum über den Flächeninhalt berechnen",
    stichwoerter="Innenwinkel bei E|Skalarprodukt und Beträge|Höhe auf EF|Flächeninhalt über das Kreuzprodukt|Kontrollangabe",
    voraussetzungen="Betrag eines Vektors berechnen|Kosinusformel für den Winkel zwischen zwei Vektoren anwenden|Flächeninhalt eines Dreiecks im Raum bestimmen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=_ABB31, kontext="Museumsgebäude", textumfang="lang",
    gegeben=_ST31 + "Betrachtet wird das Dreieck DEF. Zur Kontrolle ist angegeben: die Höhe auf "
            "der Seite EF beträgt etwa 21,21 m.",
    gesucht="Größe des Innenwinkels des Dreiecks DEF bei E|Länge der Höhe auf der Seite EF",
    verfahren="Für den Winkel bei E die Vektoren ED und EF bilden und den Kosinus als Quotient aus "
              "Skalarprodukt und Produkt der Beträge berechnen. Für die Höhe den Flächeninhalt des "
              "Dreiecks bestimmen, etwa als halber Betrag des Kreuzprodukts von DE und DF, und "
              "dann die Höhe als doppelten Flächeninhalt geteilt durch die Länge von EF.",
    schritte="6", zahlenraum="dezimal|ganz|negativ|Wurzel", einheiten="m", abhaengig_von="",
    ergebnis="Der Innenwinkel bei E beträgt genau 45°. Die Höhe auf EF ist 15 · √2 ≈ 21,21 m, "
             "in Übereinstimmung mit der Kontrollangabe des Hefts.",
    zwischenergebnis="ED = (0 | −30 | 0)|EF = (−25 | −25 | 0)|cos = 1/√2|Flächeninhalt DEF = 375 m²|"
                     "Länge EF = 25 · √2 ≈ 35,36 m",
    niveau_geschaetzt="II",
    fehlerquelle="die Höhe mit einer Seitenlänge verwechseln und 25 · √2 statt 15 · √2 angeben",
    bemerkung="Die Kontrollangabe des Hefts ist durch eigene Rechnung bestätigt: 15 · √2 = 21,2132. "
              "Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B3.1d", block="B", aufgabe="3.1", titel="Museum", teilaufgabe="d",
    seite="9", punkte="4",
    leitidee="Analytische Geometrie", thema="Flächeninhalt und Volumen im Raum",
    typ="Pyramidenvolumen aus Grundfläche und Höhe berechnen",
    typ_neben="Bedarfsgröße aus einem Volumen im Sachzusammenhang nachweisen",
    stichwoerter="Pyramide DEFG|Grundfläche DEF|Höhe 20 Meter|Rauminhalt 2500 Kubikmeter|elektrische Leistung",
    voraussetzungen="Volumenformel der Pyramide anwenden|Höhe als Abstand zweier paralleler Ebenen ablesen|Dreisatz mit einer Leistungsangabe rechnen",
    format="Rechnung|Begründung", operator="Weisen Sie nach", antwort="Zahl|Text",
    material="Körper", skizze=_ABB31, kontext="Museumsgebäude", textumfang="lang",
    gegeben=_ST31 + "Für die obere Etage, also die Pyramide DEFG, wird eine Anlage zur "
            "Entfeuchtung der Luft installiert, die für 100 m³ Rauminhalt eine elektrische "
            "Leistung von 0,8 Kilowatt benötigt.",
    gesucht="Nachweis, dass für den Betrieb der Anlage eine Leistung von 25 Kilowatt ausreicht",
    verfahren="Die Grundfläche DEF beträgt 375 m². Die Höhe der Pyramide ist der Abstand von G zur "
              "Ebene des Dreiecks DEF; beide Dreiecke liegen waagerecht, also ist die Höhe die "
              "Differenz der z-Werte 35 und 15, also 20 m. Aus V = (1/3) · Grundfläche · Höhe "
              "folgt der Rauminhalt, daraus über den Dreisatz die benötigte Leistung, die mit "
              "25 Kilowatt zu vergleichen ist.",
    schritte="4", zahlenraum="dezimal|ganz", einheiten="m|m³|kW",
    abhaengig_von="2018-bb-ea-B3.1c",
    ergebnis="V = (1/3) · 375 m² · 20 m = 2500 m³; benötigt werden 25 · 0,8 kW = 20 kW. Da 20 kW "
             "kleiner als 25 kW ist, reicht die Leistung aus.",
    zwischenergebnis="Grundfläche DEF = 375 m²|Höhe der Pyramide 20 m|V = 2500 m³|Bedarf 20 kW",
    niveau_geschaetzt="II",
    fehlerquelle="das Volumen des gesamten Körpers statt der oberen Etage berechnen oder den "
                 "Faktor ein Drittel der Pyramidenformel vergessen",
    bemerkung="Die Grundfläche 375 m² fällt bereits in Teilaufgabe c an; die Abhängigkeit ist eingetragen. "
              "Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B3.1e", block="B", aufgabe="3.1", titel="Museum", teilaufgabe="e",
    seite="9", punkte="3",
    leitidee="Analytische Geometrie", thema="Schnittmengen",
    typ="Durchstoßpunkt einer Geraden durch eine Ebene bestimmen",
    typ_neben="",
    stichwoerter="Gerade durch A und G|Ebene des Dreiecks DEF|waagerechte Ebene z gleich 15|Parameter bestimmen|Punkt R",
    voraussetzungen="Gerade durch zwei Punkte in Parameterform aufstellen|erkennen, dass die Ebene des Dreiecks DEF die Gleichung z = 15 hat|Parameter aus einer Koordinatengleichung bestimmen",
    format="Rechnung|Begründung", operator="Weisen Sie nach", antwort="Zahl|Text",
    material="Körper", skizze=_ABB31, kontext="Museumsgebäude", textumfang="lang",
    gegeben=_ST31 + "Behauptet wird, dass sich die Gerade durch A und G und die Ebene, in der das "
            "Dreieck DEF liegt, im Punkt R(−50/7 | 50/7 | 15) schneiden.",
    gesucht="Nachweis dieses Schnittpunkts",
    verfahren="Die Gerade durch A und G aufstellen: Stützvektor A, Richtungsvektor G − A = "
              "(−5 | 5 | 35). Da D, E und F alle den z-Wert 15 haben, ist ihre Ebene z = 15. Die "
              "z-Koordinate der Geraden gleich 15 setzen, den Parameter bestimmen und einsetzen.",
    schritte="4", zahlenraum="Bruch|ganz|negativ", einheiten="m", abhaengig_von="",
    ergebnis="Aus 35t = 15 folgt t = 3/7; Einsetzen liefert R(−50/7 | 50/7 | 15), also rund "
             "(−7,14 | 7,14 | 15). Damit ist der behauptete Schnittpunkt bestätigt.",
    zwischenergebnis="Richtungsvektor AG = (−5 | 5 | 35)|Ebenengleichung z = 15|t = 3/7",
    niveau_geschaetzt="II",
    fehlerquelle="die Ebene des Dreiecks DEF aufwendig aus drei Punkten bestimmen, statt am "
                 "gemeinsamen z-Wert 15 abzulesen",
    bemerkung="Hier ist die Ebene keine Koordinatenebene, sondern parallel dazu; der "
              "Lösungsweg ist derselbe, deshalb ein Typ mit A1.2b. Eine Ebene in Parameterform "
              "verlangt ein Gleichungssystem und wäre ein eigener Typ. Eigene Rechnung, mit "
              "sympy bestätigt.")

row(id="2018-bb-ea-B3.1f", block="B", aufgabe="3.1", titel="Museum", teilaufgabe="f",
    seite="9", punkte="6",
    leitidee="Analytische Geometrie", thema="Abstände",
    typ="Punkt auf einer Strecke mit vorgegebenem Abstand zu einer Ebene bestimmen",
    typ_neben="",
    stichwoerter="Scheinwerfer auf der Strecke RG|Abstand 5 Meter zur Ebene|Hessesche Normalform|Parameter der Strecke|Wand EFG",
    voraussetzungen="Strecke als Gerade mit Parameterbereich schreiben|Abstand Punkt Ebene über die Hessesche Normalform berechnen|Betragsgleichung lösen",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="Körper", skizze=_ABB31, kontext="Museumsgebäude", textumfang="lang",
    gegeben=_ST31 + "An einer Metallstange, die durch die Strecke RG mit R(−50/7 | 50/7 | 15) "
            "dargestellt wird, lässt sich ein punktförmig gedachter Scheinwerfer verschieben. Er "
            "soll aus einer Entfernung von 5 m die Wand beleuchten, die im Modell durch das "
            "Dreieck EFG dargestellt wird. Dieses Dreieck liegt in der Ebene mit der Gleichung "
            "2x − 2y − z = −75.",
    gesucht="Koordinaten des Punktes, der die Position des Scheinwerfers im Modell beschreibt",
    verfahren="Die Strecke RG als Gerade mit einem Parameter zwischen 0 und 1 schreiben. Den "
              "Abstand eines Strecken-Punktes zur Ebene über die Hessesche Normalform ansetzen: "
              "der Normalenvektor (2 | −2 | −1) hat die Länge 3, also ist der Abstand der Betrag "
              "von (2x − 2y − z + 75) geteilt durch 3. Diesen Abstand gleich 5 setzen und nach dem "
              "Parameter auflösen; G selbst liegt in der Ebene, der Abstand nimmt entlang der "
              "Strecke von rund 10,48 m auf 0 ab.",
    schritte="5", zahlenraum="Bruch|dezimal|ganz|negativ", einheiten="m",
    abhaengig_von="2018-bb-ea-B3.1e",
    ergebnis="Der Parameter ist 23/44; der Scheinwerfer sitzt im Punkt "
             "(−95/11 | 95/11 | 280/11), also rund (−8,64 | 8,64 | 25,45).",
    zwischenergebnis="Richtungsvektor RG = (−20/7 | 20/7 | 20)|Betrag des Normalenvektors 3|"
                     "Abstand bei R rund 10,48 m|Parameter 23/44",
    niveau_geschaetzt="III",
    fehlerquelle="den Abstand ohne Normierung des Normalenvektors ansetzen, also nicht durch 3 "
                 "teilen",
    bemerkung="Die zweite Lösung der Betragsgleichung liegt außerhalb der Strecke und entfällt. "
              "Eigene Rechnung, mit sympy bestätigt.")

_ST32 = ("Die Punkte A(−2 | 2 | −1), B(1 | 2 | 2), C(2 | −2 | 1) und D(−1 | −2 | −2) sind in "
         "dieser Reihenfolge Eckpunkte eines Quadrates, das in der Ebene E liegt. ")

row(id="2018-bb-ea-B3.2a", block="B", aufgabe="3.2", titel="Quadrat", teilaufgabe="a",
    seite="10", punkte="2",
    leitidee="Analytische Geometrie", thema="Ebenen",
    typ="Parametergleichung einer Ebene aus Punkten angeben",
    typ_neben="",
    stichwoerter="Parametergleichung|Stützvektor|zwei Spannvektoren|Eckpunkte eines Quadrates",
    voraussetzungen="Verbindungsvektoren aus Punktkoordinaten bilden|Aufbau einer Parameterform kennen",
    format="Kurzantwort", operator="Geben Sie an", antwort="Term",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=_ST32,
    gesucht="eine Parametergleichung der Ebene E",
    verfahren="Einen der vier Punkte als Stützvektor nehmen und zwei nicht parallele "
              "Verbindungsvektoren als Spannvektoren, hier AB und AD.",
    schritte="2", zahlenraum="ganz|negativ", einheiten="", abhaengig_von="",
    ergebnis="E: x = (−2 | 2 | −1) + r · (3 | 0 | 3) + s · (1 | −4 | −1) mit r und s aus IR; "
             "andere Stütz- und Spannvektoren sind gleichwertig.",
    zwischenergebnis="AB = (3 | 0 | 3)|AD = (1 | −4 | −1)",
    niveau_geschaetzt="I",
    fehlerquelle="zwei parallele Vektoren als Spannvektoren wählen, etwa AB und DC",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B3.2b", block="B", aufgabe="3.2", titel="Quadrat", teilaufgabe="b",
    seite="10", punkte="6",
    leitidee="Analytische Geometrie", thema="Scharen von Geraden und Ebenen",
    typ="Parameter einer Geradenschar aus einem vorgegebenen Durchstoßpunkt bestimmen",
    typ_neben="Mittelpunkt eines Quadrates als Diagonalenmittelpunkt bestimmen|Schnittwinkel zweier Geraden über das Skalarprodukt berechnen",
    stichwoerter="Laserstrahl|Punkteschar|Mittelpunkt des Quadrates|Parameter a|Winkel zur Diagonale AC",
    voraussetzungen="Mittelpunkt einer Strecke als halbe Summe der Ortsvektoren berechnen|Gerade in Parameterform mit einem Punkt gleichsetzen|Winkel zwischen zwei Geraden über den Betrag des Skalarprodukts bestimmen",
    format="Rechnung", operator="Ermitteln Sie|Bestimmen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Laserstrahl", textumfang="lang",
    gegeben=_ST32 + "Ein vom Punkt R_a(−6 | 2a − 4 | 6) in Richtung des Vektors v = (1 | 3 | −1) "
            "verlaufender geradliniger Laserstrahl trifft genau im Mittelpunkt M des Quadrates "
            "ABCD auf die Ebene E.",
    gesucht="Wert von a|Größe des Winkels zwischen dem Laserstrahl und der Diagonale AC",
    verfahren="M als Mittelpunkt der Diagonale AC berechnen; hier ergibt sich der Ursprung. Dann "
              "R_a plus Parameter mal v gleich M setzen: aus der ersten und dritten Koordinate "
              "folgt der Parameter 6, aus der zweiten dann a. Für den Winkel den Richtungsvektor v "
              "und den Diagonalenvektor AC nehmen und den Kosinus als Betrag des Skalarprodukts "
              "geteilt durch das Produkt der Beträge bilden.",
    schritte="6", zahlenraum="dezimal|ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="M(0 | 0 | 0) und a = −7. Der Winkel zwischen Laserstrahl und Diagonale AC beträgt "
             "rund 59,8°.",
    zwischenergebnis="M = (0 | 0 | 0)|Parameter 6|AC = (4 | −4 | 2)|cos = 5 · √11 / 33 ≈ 0,5025",
    niveau_geschaetzt="II",
    fehlerquelle="den Winkel ohne Betrag des Skalarprodukts berechnen und den stumpfen "
                 "Nebenwinkel angeben",
    bemerkung="Dass der Mittelpunkt des Quadrates der Koordinatenursprung ist, vereinfacht die "
              "Rechnung erheblich; das ist eine Besonderheit der Zahlenwahl, nicht des Typs. "
              "Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B3.2c", block="B", aufgabe="3.2", titel="Quadrat", teilaufgabe="c",
    seite="10", punkte="2",
    leitidee="Analytische Geometrie", thema="Linearkombination und lineare Abhängigkeit",
    typ="Lage eines durch eine Linearkombination gegebenen Punktes beschreiben",
    typ_neben="",
    stichwoerter="Linearkombination|auf Länge gebrachter Vektor|Seitenlänge drei mal Wurzel zwei|Punkt auf der Seite DC|Abstand 3 von D",
    voraussetzungen="Betrag eines Vektors berechnen|einen Vektor auf eine vorgegebene Länge bringen|Summe von Vektoren geometrisch deuten",
    format="Begründung", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="ohne", textumfang="mittel",
    gegeben=_ST32 + "Der Ortsvektor eines Punktes P wird durch OP = OA + (3 geteilt durch den "
            "Betrag von AB) · AB + AD dargestellt.",
    gesucht="Beschreibung der Lagebeziehung des Punktes P zum Quadrat ABCD",
    verfahren="Der Faktor 3 geteilt durch den Betrag von AB macht aus AB einen Vektor der Länge 3 "
              "in Richtung AB. Von A aus führt AD zum Eckpunkt D; der Rest ist ein Stück der Länge "
              "3 in Richtung AB, also parallel zur Seite DC. Die Seitenlänge des Quadrates ist "
              "3 · √2 ≈ 4,24, also liegt P noch innerhalb der Seite.",
    schritte="3", zahlenraum="dezimal|ganz|negativ|Wurzel", einheiten="", abhaengig_von="",
    ergebnis="P liegt auf der Quadratseite DC, und zwar im Abstand 3 von D; bis C bleiben rund "
             "1,24. In Koordinaten ist P rund (1,12 | −2 | 0,12).",
    zwischenergebnis="Betrag von AB = 3 · √2 ≈ 4,24|Faktor 3 / (3 · √2) = 1 / √2|A plus AD = D",
    niveau_geschaetzt="III",
    fehlerquelle="den Faktor als Streckung mit 3 lesen und P weit außerhalb des Quadrates verorten",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

_ST41 = ("Eine Umfrage ergab, dass zu medizinischen Fragen 73 % der Bevölkerung das Internet "
         "nutzen. 55 % der Internetnutzer nutzen Medinet, einen Ratgeber bei medizinischen Fragen, "
         "der nur im Internet verfügbar ist. ")

row(id="2018-bb-ea-B4.1a", block="B", aufgabe="4.1", titel="Medinet", teilaufgabe="a",
    seite="11", punkte="3",
    leitidee="Stochastik", thema="Baumdiagramm und Pfadregeln",
    typ="Baumdiagramm zu einer zweistufigen Situation erstellen",
    typ_neben="",
    stichwoerter="zweistufiges Baumdiagramm|bedingte Wahrscheinlichkeit als zweite Stufe|Gegenwahrscheinlichkeit|nur im Internet verfügbar",
    voraussetzungen="Gegenwahrscheinlichkeit bilden|einen Prozentsatz als bedingte Wahrscheinlichkeit lesen|Pfadregel anwenden",
    format="Zeichnen", operator="Stellen Sie dar", antwort="Grafik",
    material="keins",
    skizze="Im Heft ist keine Abbildung vorgegeben; das Baumdiagramm ist Teil der Lösung. Erwartet "
           "wird ein zweistufiger Baum: erste Stufe mit den Ästen Internetnutzung ja (0,73) und "
           "nein (0,27); an den Ast ja schließt die zweite Stufe mit Medinet ja (0,55) und Medinet "
           "nein (0,45) an; an den Ast nein schließt Medinet ja (0) und Medinet nein (1) an, weil "
           "der Ratgeber nur im Internet verfügbar ist. Die Pfadenden können mit den "
           "Pfadwahrscheinlichkeiten 0,4015, 0,3285, 0 und 0,27 beschriftet werden.",
    kontext="Internetnutzung bei medizinischen Fragen", textumfang="mittel",
    gegeben=_ST41,
    gesucht="Darstellung des Sachverhalts in einem soweit wie möglich beschrifteten Baumdiagramm",
    verfahren="Die erste Stufe trägt die Internetnutzung mit 0,73 und der Gegenwahrscheinlichkeit "
              "0,27. Die 55 % sind ein Anteil innerhalb der Internetnutzer, also eine bedingte "
              "Wahrscheinlichkeit, und gehören an die zweite Stufe unter den Ast Internetnutzung. "
              "Da Medinet nur im Internet verfügbar ist, trägt der andere Zweig die Werte 0 und 1. "
              "Die Pfadwahrscheinlichkeiten entstehen durch Multiplikation entlang der Pfade.",
    schritte="3", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Zweistufiger Baum mit erster Stufe 0,73 und 0,27, zweiter Stufe 0,55 und 0,45 unter "
             "dem Ast Internet sowie 0 und 1 unter dem Ast kein Internet. Der Pfad Internet und "
             "Medinet hat die Wahrscheinlichkeit 0,73 · 0,55 = 0,4015.",
    zwischenergebnis="P(Internet und Medinet) = 0,4015|P(Internet und nicht Medinet) = 0,3285",
    niveau_geschaetzt="II",
    fehlerquelle="die 55 % als unbedingte Wahrscheinlichkeit an die erste Stufe setzen oder den "
                 "Zweig ohne Internetnutzung unbeschriftet lassen",
    bemerkung="Zweiter Fall im Katalog, in dem skizze ausnahmsweise die vom Prüfling zu "
              "erstellende Darstellung beschreibt und nicht vorhandenes Material. Eigene Rechnung, "
              "mit sympy bestätigt.")

row(id="2018-bb-ea-B4.1b", block="B", aufgabe="4.1", titel="Medinet", teilaufgabe="b",
    seite="11", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer Binomialverteilung für genau k Treffer berechnen",
    typ_neben="",
    stichwoerter="Binomialverteilung|zwölf Personen|genau zehn Treffer|Trefferwahrscheinlichkeit 0,73|Binomialkoeffizient",
    voraussetzungen="Bernoulli-Kette erkennen|Binomialkoeffizient berechnen|Formel der Binomialverteilung anwenden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Internetnutzung bei medizinischen Fragen",
    textumfang="mittel",
    gegeben=_ST41 + "Zwölf Personen werden zufällig ausgewählt.",
    gesucht="Wahrscheinlichkeit dafür, dass sich unter den zwölf Personen genau zehn befinden, die "
            "das Internet nutzen",
    verfahren="Die Auswahl als Bernoulli-Kette der Länge 12 mit der Trefferwahrscheinlichkeit 0,73 "
              "auffassen und die Binomialformel für zehn Treffer anwenden.",
    schritte="2", zahlenraum="dezimal|ganz|Potenz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P ≈ 0,2068, also rund 20,7 %",
    zwischenergebnis="Binomialkoeffizient 12 über 10 = 66",
    niveau_geschaetzt="II",
    fehlerquelle="den Binomialkoeffizienten weglassen und nur das Produkt der "
                 "Einzelwahrscheinlichkeiten angeben",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B4.1c", block="B", aufgabe="4.1", titel="Medinet", teilaufgabe="c",
    seite="11", punkte="2",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben",
    typ_neben="",
    stichwoerter="Term deuten|Gegenereignis|höchstens zehn Treffer|zwölf Personen|Binomialverteilung",
    voraussetzungen="Aufbau der Binomialformel lesen|Gegenereignis erkennen|Summanden als Einzelwahrscheinlichkeiten deuten",
    format="Kurzantwort", operator="Beschreiben Sie", antwort="Text",
    material="keins", skizze="keine", kontext="Internetnutzung bei medizinischen Fragen",
    textumfang="lang",
    gegeben=_ST41 + "Wieder werden zwölf Personen zufällig ausgewählt. Für ein Ereignis B ist der "
            "Term angegeben: P(B) = 1 − (12 über 12) · 0,73^12 · (1 − 0,73)^0 − (12 über 11) · "
            "0,73^11 · (1 − 0,73)^1.",
    gesucht="Beschreibung des Ereignisses B, dessen Wahrscheinlichkeit sich mit diesem Term "
            "berechnen lässt",
    verfahren="Die beiden abgezogenen Summanden als die Wahrscheinlichkeiten für genau zwölf und "
              "genau elf Internetnutzer erkennen. Wird beides von 1 abgezogen, bleibt die "
              "Wahrscheinlichkeit für alle übrigen Trefferzahlen, also für höchstens zehn.",
    schritte="2", zahlenraum="dezimal|ganz|Potenz", einheiten="", abhaengig_von="",
    ergebnis="B ist das Ereignis, dass von den zwölf ausgewählten Personen höchstens zehn das "
             "Internet nutzen; gleichwertig, dass mindestens zwei es nicht nutzen. Der Wert ist "
             "rund 0,8755.",
    zwischenergebnis="P(genau zwölf) ≈ 0,0230|P(genau elf) ≈ 0,1015",
    niveau_geschaetzt="III",
    fehlerquelle="das Gegenereignis nur teilweise bilden und B als genau zehn Nutzer oder als "
                 "mindestens zehn Nutzer beschreiben",
    bemerkung="Reine Deutungsaufgabe ohne eigene Rechnung. Der Term steht im Heft als Bild und ist "
              "nur über die Seitenansicht sicher lesbar. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B4.1d", block="B", aufgabe="4.1", titel="Medinet", teilaufgabe="d",
    seite="11", punkte="3",
    leitidee="Stochastik", thema="Hypergeometrische Verteilung",
    typ="Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen",
    typ_neben="",
    stichwoerter="Ziehen ohne Zurücklegen|zwölf Personen davon sieben|drei Aufrufe|höchstens zwei|Gegenereignis",
    voraussetzungen="hypergeometrische Situation von der Binomialverteilung unterscheiden|Binomialkoeffizienten berechnen|Gegenereignis bilden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Internetnutzung bei medizinischen Fragen",
    textumfang="lang",
    gegeben=_ST41 + "In einer Arztpraxis sitzen 12 Personen, die das Internet zu medizinischen "
            "Fragen nutzen. Von diesen recherchieren 7 bei Medinet. 3 Personen werden aufgerufen.",
    gesucht="Wahrscheinlichkeit dafür, dass unter den aufgerufenen Personen höchstens zwei sind, "
            "die bei Medinet recherchieren",
    verfahren="Aus einer festen Gruppe wird ohne Zurücklegen gezogen, die Verteilung ist also "
              "hypergeometrisch. Statt drei Fälle zu addieren, das Gegenereignis nehmen: alle drei "
              "Aufgerufenen recherchieren bei Medinet, mit der Wahrscheinlichkeit (7 über 3) "
              "geteilt durch (12 über 3).",
    schritte="3", zahlenraum="Bruch|dezimal|ganz", einheiten="", abhaengig_von="",
    ergebnis="P = 1 − 35/220 = 37/44 ≈ 0,8409, also rund 84,1 %",
    zwischenergebnis="(7 über 3) = 35|(12 über 3) = 220|P(genau drei) = 7/44",
    niveau_geschaetzt="II",
    fehlerquelle="binomial mit der festen Wahrscheinlichkeit 7/12 rechnen und das Ziehen ohne "
                 "Zurücklegen übersehen",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

_ST42 = ("In einer großen Gemeinde tragen 62,5 % der Bevölkerung eine Brille. Bei den Frauen "
         "beträgt der Anteil 64,8 %. Bekannt ist außerdem, dass 52,1 % der Bevölkerung Frauen "
         "sind. ")

row(id="2018-bb-ea-B4.2a", block="B", aufgabe="4.2", titel="Brillenträger", teilaufgabe="a",
    seite="12", punkte="5",
    leitidee="Stochastik", thema="Vierfeldertafel",
    typ="Vierfeldertafel aus Anteilen aufstellen",
    typ_neben="Bedingte Wahrscheinlichkeit aus der Vierfeldertafel berechnen",
    stichwoerter="Vierfeldertafel|Randwahrscheinlichkeiten|gemeinsame Wahrscheinlichkeit|bedingte Wahrscheinlichkeit|Mann mit Brille",
    voraussetzungen="Prozentangaben als Wahrscheinlichkeiten lesen|einen Anteil innerhalb einer Teilgruppe als bedingte Wahrscheinlichkeit erkennen|Quotientenformel der bedingten Wahrscheinlichkeit anwenden",
    format="Tabelle|Rechnung", operator="Stellen Sie dar|Berechnen Sie", antwort="Tabelle|Zahl",
    material="keins", skizze="keine", kontext="Brillenträger in einer Gemeinde",
    textumfang="mittel",
    gegeben=_ST42 + "Eine aus der Bevölkerung zufällig ausgewählte Person ist ein Mann.",
    gesucht="Darstellung des Sachverhalts in einer Vierfeldertafel|Wahrscheinlichkeit dafür, dass "
            "dieser Mann eine Brille trägt",
    verfahren="Die Randwerte 0,625 für Brille und 0,521 für Frauen eintragen. Die 64,8 % sind ein "
              "Anteil innerhalb der Frauen, also eine bedingte Wahrscheinlichkeit; daraus folgt "
              "das Feld Frau und Brille als 0,521 · 0,648. Die übrigen Felder über die Randsummen "
              "ergänzen. Die gesuchte Wahrscheinlichkeit ist das Feld Mann und Brille geteilt "
              "durch den Randwert der Männer.",
    schritte="5", zahlenraum="dezimal|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Tafel: Frau mit Brille 0,3376, Frau ohne Brille 0,1834, Mann mit Brille 0,2874, Mann "
             "ohne Brille 0,1916; Randwerte 0,521 Frauen, 0,479 Männer, 0,625 Brille, 0,375 keine "
             "Brille. Die Wahrscheinlichkeit, dass der Mann eine Brille trägt, beträgt rund 0,600, "
             "also 60 %.",
    zwischenergebnis="P(Frau und Brille) = 0,521 · 0,648 = 0,337608|P(Mann und Brille) = 0,625 − "
                     "0,337608 = 0,287392|P(Mann) = 0,479",
    niveau_geschaetzt="II",
    fehlerquelle="die 64,8 % unmittelbar als Feld der Tafel eintragen, also ohne Multiplikation "
                 "mit 0,521",
    bemerkung="Der Wert 0,59998 liegt so nah an 0,6, dass die Zahlen des Hefts offenbar darauf hin "
              "gewählt wurden. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B4.2b", block="B", aufgabe="4.2", titel="Brillenträger", teilaufgabe="b",
    seite="12", punkte="4",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer Binomialverteilung für genau k Treffer berechnen",
    typ_neben="Trefferwahrscheinlichkeit beim Wechsel der Trefferdefinition anpassen",
    stichwoerter="acht Personen alle Brillenträger|20 Personen genau drei ohne Brille|Bernoulli-Kette|Trefferdefinition wechseln|Binomialkoeffizient",
    voraussetzungen="Bernoulli-Kette erkennen|Gegenwahrscheinlichkeit 0,375 bilden|Binomialformel anwenden",
    format="Rechnung", operator="Berechnen Sie", antwort="Zahl",
    material="keins", skizze="keine", kontext="Brillenträger in einer Gemeinde",
    textumfang="mittel",
    gegeben=_ST42 + "Ereignis A: von acht zufällig ausgewählten Personen sind alle Brillenträger. "
            "Ereignis B: von 20 zufällig ausgewählten Personen sind genau drei keine "
            "Brillenträger.",
    gesucht="Wahrscheinlichkeiten der Ereignisse A und B",
    verfahren="Für A ist die Trefferzahl gleich der Kettenlänge, also einfach 0,625 hoch 8. Für B "
              "die Trefferdefinition wechseln: Treffer ist jetzt kein Brillenträger mit der "
              "Wahrscheinlichkeit 0,375, gesucht sind genau drei Treffer bei 20 Versuchen. "
              "Gleichwertig lässt sich mit genau 17 Brillenträgern rechnen.",
    schritte="4", zahlenraum="dezimal|ganz|Potenz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(A) ≈ 0,0233, also rund 2,3 %|P(B) ≈ 0,0204, also rund 2,0 %",
    zwischenergebnis="0,625 hoch 8 ≈ 0,023283|(20 über 3) = 1140|Gegenwahrscheinlichkeit 0,375",
    niveau_geschaetzt="II",
    fehlerquelle="bei B mit der Trefferwahrscheinlichkeit 0,625 und drei Treffern rechnen, also "
                 "die Trefferdefinition nicht mitwechseln",
    bemerkung="Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B4.2c", block="B", aufgabe="4.2", titel="Brillenträger", teilaufgabe="c",
    seite="12", punkte="5",
    leitidee="Stochastik", thema="Binomialverteilung",
    typ="Wahrscheinlichkeit einer Binomialverteilung für genau k Treffer berechnen",
    typ_neben="Wahrscheinlichkeiten über den Erwartungswert vergleichen",
    stichwoerter="genau neun Brillenträger|genau zwölf Brillenträger|Erwartungswert 12,5|Abstand vom Erwartungswert|Vergleich ohne Rechnung",
    voraussetzungen="Binomialformel anwenden|Erwartungswert als Produkt aus Kettenlänge und Trefferwahrscheinlichkeit bilden|Gestalt der Binomialverteilung kennen",
    format="Rechnung|Begründung", operator="Berechnen Sie|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Brillenträger in einer Gemeinde",
    textumfang="lang",
    gegeben=_ST42 + "Ereignis C: von 20 zufällig ausgewählten Personen sind genau neun "
            "Brillenträger. Ereignis D: von 20 zufällig ausgewählten Personen sind genau zwölf "
            "Brillenträger.",
    gesucht="Wahrscheinlichkeit des Ereignisses C|Begründung mit Hilfe des Erwartungswertes, ob "
            "die Wahrscheinlichkeit von D größer oder kleiner ist als die von C",
    verfahren="P(C) mit der Binomialformel für 20 Versuche, die Trefferwahrscheinlichkeit 0,625 "
              "und neun Treffer berechnen. Für den Vergleich den Erwartungswert 20 · 0,625 = 12,5 "
              "bilden. Die Binomialverteilung hat ihr Maximum beim Erwartungswert und fällt zu "
              "beiden Seiten ab; zwölf liegt mit Abstand 0,5 viel näher daran als neun mit Abstand "
              "3,5, also ist P(D) größer als P(C).",
    schritte="4", zahlenraum="dezimal|ganz|Potenz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="P(C) ≈ 0,0504, also rund 5,0 %. P(D) ist größer als P(C), weil zwölf näher am "
             "Erwartungswert 12,5 liegt als neun; zur Kontrolle P(D) ≈ 0,1750.",
    zwischenergebnis="(20 über 9) = 167 960|Erwartungswert 12,5|Abstand von C zum Erwartungswert "
                     "3,5|Abstand von D zum Erwartungswert 0,5",
    niveau_geschaetzt="III",
    fehlerquelle="P(D) ausrechnen und vergleichen, obwohl die Begründung ausdrücklich über den "
                 "Erwartungswert verlangt ist",
    bemerkung="Das Argument trägt nur, weil die Binomialverteilung zum Erwartungswert hin "
              "ansteigt; bei stark schiefen Verteilungen wäre es nicht zulässig. Eigene Rechnung, "
              "mit sympy bestätigt.")

row(id="2018-bb-ea-B4.2d", block="B", aufgabe="4.2", titel="Brillenträger", teilaufgabe="d",
    seite="12|13", punkte="5",
    leitidee="Stochastik", thema="Hypothesentests",
    typ="Entscheidungsregel für einen einseitigen Signifikanztest bestimmen",
    typ_neben="",
    stichwoerter="Nullhypothese höchstens 30 Prozent|Stichprobe 100|Signifikanzniveau 5 Prozent|rechtsseitiger Test|Ablehnungsbereich",
    voraussetzungen="Nullhypothese und Alternative unterscheiden|einseitigen Test als rechtsseitig erkennen|summierte Binomialverteilung aus der Anlage ablesen",
    format="Rechnung|Begründung", operator="Bestimmen Sie", antwort="Zahl|Text",
    material="Tabelle",
    skizze="Anlage auf einer eigenen Seite: Tafel der summierten Binomialverteilungen, auf vier "
           "Nachkommastellen gerundet, wobei die führende Null und das Komma weggelassen sind. "
           "Zeilen nach der Trefferzahl, Spalten nach der Trefferwahrscheinlichkeit; freie Plätze "
           "links unten stehen für 1,0000, rechts oben für 0,0000. Wird die Tafel von unten "
           "gelesen, also für Trefferwahrscheinlichkeiten über 0,5, ist der richtige Wert 1 minus "
           "dem abgelesenen Wert.",
    kontext="Optiker und Werbeaktion", textumfang="lang",
    gegeben=_ST42 + "Ein Optiker vermutet, dass mehr als 30 % der jungen Erwachsenen aus dem "
            "Landkreis Kunden in seinem Geschäft sind. Sollte das nicht der Fall sein, erwägt er "
            "eine Werbeaktion mit Flyern. Um unnötige Kosten zu vermeiden, soll die Nullhypothese, "
            "dass höchstens 30 % der jungen Erwachsenen Kunden bei diesem Optiker sind, mit einer "
            "Stichprobe von 100 jungen Erwachsenen auf einem Signifikanzniveau von 5 % getestet "
            "werden.",
    gesucht="die zugehörige Entscheidungsregel",
    verfahren="Unter der Nullhypothese ist die Trefferzahl binomialverteilt mit 100 Versuchen und "
              "der Trefferwahrscheinlichkeit 0,3. Der Test ist rechtsseitig, weil die Alternative "
              "mehr als 30 % lautet. Gesucht ist die kleinste Trefferzahl, ab der die "
              "Wahrscheinlichkeit für mindestens so viele Treffer höchstens 5 % beträgt; "
              "gleichwertig die kleinste Zahl, bis zu deren Vorgänger die summierte "
              "Wahrscheinlichkeit mindestens 0,95 erreicht.",
    schritte="4", zahlenraum="dezimal|ganz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Ablehnungsbereich von 39 bis 100, Annahmebereich von 0 bis 38. Die Nullhypothese "
             "wird also verworfen, wenn in der Stichprobe mindestens 39 der 100 jungen Erwachsenen "
             "Kunden sind; andernfalls wird sie beibehalten und die Werbeaktion erwogen.",
    zwischenergebnis="P bis 37 ≈ 0,9470|P bis 38 ≈ 0,9660|P ab 38 ≈ 0,0531 und damit zu groß|"
                     "P ab 39 ≈ 0,0340",
    niveau_geschaetzt="III",
    fehlerquelle="die Grenze bei 38 ziehen, weil die summierte Wahrscheinlichkeit bis 37 schon "
                 "nahe bei 0,95 liegt, und damit ein Niveau von 5,3 % in Kauf nehmen",
    bemerkung="Aufgabenseite 12, die Tafel der summierten Binomialverteilungen steht als Anlage "
              "auf Seite 13. Eigene Rechnung, mit sympy bestätigt.")

row(id="2018-bb-ea-B4.2e", block="B", aufgabe="4.2", titel="Brillenträger", teilaufgabe="e",
    seite="12", punkte="6",
    leitidee="Stochastik", thema="Zufallsexperimente und Urnenmodelle",
    typ="Mindestanzahl beim Ziehen ohne Zurücklegen über das Gegenereignis bestimmen",
    typ_neben="",
    stichwoerter="20 Brillenträger|genau eine Designerbrille|ohne Zurücklegen|mindestens 75 Prozent|Gegenereignis",
    voraussetzungen="Gegenereignis bilden|Wahrscheinlichkeit beim Ziehen ohne Zurücklegen bestimmen|Ungleichung nach der Anzahl auflösen",
    format="Rechnung|Begründung", operator="Berechnen Sie|Begründen Sie", antwort="Zahl|Text",
    material="keins", skizze="keine", kontext="Brillenmesse", textumfang="lang",
    gegeben=_ST42 + "Auf einer Brillenmesse befindet sich in einer Gruppe von 20 Brillenträgern "
            "genau eine Person, die eine Designerbrille trägt. Es wird zufällig und nacheinander "
            "ohne Zurücklegen ausgewählt.",
    gesucht="Mindestanzahl auszuwählender Personen, damit die Wahrscheinlichkeit, dass der Träger "
            "der Designerbrille dabei ist, mindestens 75 % beträgt|Begründung des Lösungsansatzes",
    verfahren="Da nur eine einzige Person die Designerbrille trägt, hat jede der 20 Personen "
              "dieselbe Chance, unter den Ausgewählten zu sein; die Wahrscheinlichkeit ist deshalb "
              "die Anzahl der Ausgewählten geteilt durch 20. Gleichwertig über das Gegenereignis: "
              "die Wahrscheinlichkeit, dass die Person nicht dabei ist, ist (20 minus Anzahl) "
              "geteilt durch 20. Die Ungleichung nach der Anzahl auflösen.",
    schritte="3", zahlenraum="Bruch|dezimal|ganz|Prozent", einheiten="", abhaengig_von="",
    ergebnis="Es sind mindestens 15 Personen auszuwählen. Bei 15 Personen beträgt die "
             "Wahrscheinlichkeit genau 0,75, bei 14 nur 0,70.",
    zwischenergebnis="Wahrscheinlichkeit bei k Ausgewählten ist k geteilt durch 20|Ungleichung "
                     "k geteilt durch 20 ist mindestens 0,75",
    niveau_geschaetzt="III",
    fehlerquelle="binomial mit der Einzelwahrscheinlichkeit 1/20 rechnen und das Ziehen ohne "
                 "Zurücklegen übersehen",
    bemerkung="Der Lösungsansatz ist ausdrücklich zu begründen; die Begründung sitzt darin, dass "
              "bei genau einem besonderen Element die Wahrscheinlichkeit linear mit der Anzahl der "
              "Ausgewählten wächst. Eigene Rechnung, mit sympy bestätigt.")


NEUE_TYPEN = [
    ("Parameter einer Parallelen zur x-Achse aus einer Abstandsbedingung berechnen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Aus dem vorgegebenen Abstand der beiden Schnittpunkte einer Parallelen zur x-Achse mit einem "
     "achsensymmetrischen Graphen die Höhe dieser Parallelen bestimmen.",
     "2018-bb-ea-A1.1a"),
    ("Tangente aus einer Bedingung an das Achsenabschnittsdreieck bestimmen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die Berührstelle einer Tangente so bestimmen, dass das von Tangente und Koordinatenachsen "
     "gebildete Dreieck eine vorgegebene Eigenschaft hat, hier Gleichschenkligkeit.",
     "2018-bb-ea-A1.1b"),
    ("Sektorenzahlen eines Glücksrads aus Wahrscheinlichkeiten ermitteln", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Aus dem Sektorenwinkel die Gesamtzahl der Sektoren bestimmen und die geforderten "
     "Wahrscheinlichkeiten in Anzahlen der einzelnen Farben umrechnen.",
     "2018-bb-ea-A1.3a"),
    ("Erwartungswert einer Zufallsgröße im Sachzusammenhang berechnen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Die Werte einer Zufallsgröße aus einem Sachtext ablesen und den Erwartungswert als Summe "
     "der mit ihren Wahrscheinlichkeiten gewichteten Werte bilden.",
     "2018-bb-ea-A1.3b"),
    ("Punktsymmetrie am Funktionsterm begründen", "Analysis", "Funktionsklassen und Eigenschaften",
     "Anhand von f(−x) = −f(x) oder anhand ausschließlich ungerader Exponenten begründen, dass ein "
     "Graph punktsymmetrisch zum Ursprung ist.",
     "2018-bb-ea-B2.2a"),
    ("Grenzverhalten einer Potenzfunktion untersuchen", "Analysis",
     "Grenzwerte und Verhalten im Unendlichen",
     "Das Verhalten der Funktionswerte einer Potenzfunktion mit negativem Exponenten für x gegen "
     "unendlich bestimmen, einschließlich der Annäherungsrichtung.",
     "2018-bb-ea-B2.2a"),
    ("Ausschluss eines Parameterwerts über das Grenzverhalten begründen", "Analysis",
     "Grenzwerte und Verhalten im Unendlichen",
     "Begründen, dass kein Parameterwert eine geforderte Gleichheit von Grenzwerten erfüllt, indem "
     "die möglichen Grenzwerte der Schar mit dem festen Grenzwert der Vergleichsfunktion "
     "verglichen werden.",
     "2018-bb-ea-B2.2a"),
    ("Flächeninhalt des Achsenabschnittsdreiecks einer Tangente berechnen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die Tangente in einem gegebenen Punkt aufstellen, ihre beiden Achsenabschnitte bestimmen und "
     "daraus den Flächeninhalt des von Tangente und Koordinatenachsen begrenzten Dreiecks bilden.",
     "2018-bb-ea-B2.2b"),
    ("Fehlen von Extrempunkten über das Vorzeichen der Ableitung begründen", "Analysis",
     "Kurvenuntersuchung",
     "Begründen, dass ein Graph keine lokalen Extrempunkte hat, indem gezeigt wird, dass die erste "
     "Ableitung im ganzen Definitionsbereich dasselbe Vorzeichen hat.",
     "2018-bb-ea-B2.2c"),
    ("Stellen mit vorgegebenem Tangentenanstieg nachweisen", "Analysis",
     "Tangente, Normale, Schnittwinkel",
     "Die erste Ableitung einem vorgegebenen Anstieg gleichsetzen und über die Diskriminante der "
     "entstehenden Gleichung die Anzahl der Lösungen nachweisen.",
     "2018-bb-ea-B2.2d"),
    ("Parameterwert für genau eine waagerechte Tangente bestimmen", "Analysis",
     "Funktionsscharen und Ortskurven",
     "Den Parameter einer Schar so bestimmen, dass die quadratische Gleichung f_a′(x) = 0 genau "
     "eine Lösung hat, also die Diskriminante null wird.",
     "2018-bb-ea-B2.2e"),
    ("Nachweisverfahren für einen Sattelpunkt erläutern", "Analysis", "Kurvenuntersuchung",
     "In Worten beschreiben, mit welchen Bedingungen an zweite und dritte Ableitung oder über "
     "einen Vorzeichenwechsel sich ein Sattelpunkt nachweisen lässt, ohne die Rechnung "
     "auszuführen.",
     "2018-bb-ea-B2.2e"),
    ("Punktprobe mit gerundeten Koordinaten durchführen", "Analysis",
     "Funktionsklassen und Eigenschaften",
     "Prüfen, ob gegebene Punkte auf einem Graphen liegen, wenn die Koordinaten nur gerundet "
     "angegeben sind, durch Einsetzen und Runden des Funktionswerts.",
     "2018-bb-ea-B2.2f"),
    ("Umschließendes achsenparalleles Rechteck zu einer krummlinig begrenzten Fläche bestimmen",
     "Analysis", "Kurvenuntersuchung",
     "Die Seitenlängen des kleinsten achsenparallelen Rechtecks bestimmen, das eine von "
     "Funktionsgraphen begrenzte Fläche enthält, über die Randpunkte und die Extremstellen der "
     "Randkurven.",
     "2018-bb-ea-B2.2f"),
    ("Ganzrationale Funktion aus Symmetrie und Randbedingungen rekonstruieren", "Analysis",
     "Rekonstruktion von Funktionsgleichungen",
     "Aus einer geforderten Symmetrie den Ansatz verkürzen und die verbliebenen Koeffizienten aus "
     "Funktions- und Ableitungswerten über ein lineares Gleichungssystem bestimmen.",
     "2018-bb-ea-B2.2h"),
    ("Steigungswinkel in einen Anstieg umrechnen", "Analysis", "Tangente, Normale, Schnittwinkel",
     "Einen in Grad gegebenen Steigungswinkel über den Tangens in den Anstieg umrechnen und dabei "
     "das Vorzeichen aus der Lage im Sachzusammenhang bestimmen.",
     "2018-bb-ea-B2.2h"),
    ("Gegebene Rechnung zum Geradenschnittpunkt erläutern", "Analytische Geometrie",
     "Schnittmengen",
     "Eine abgedruckte Rechnung als Gleichsetzen zweier Geraden in Parameterform deuten und "
     "benennen, welche Geraden und welcher Punkt damit bestimmt werden.",
     "2018-bb-ea-B3.1a"),
    ("Rechtwinkligkeit eines Dreiecks über Skalarprodukte ausschließen", "Analytische Geometrie",
     "Orthogonalität",
     "Für alle drei Ecken eines Dreiecks im Raum das Skalarprodukt der anliegenden Seitenvektoren "
     "bilden und aus lauter Werten ungleich null schließen, dass kein rechter Winkel vorliegt.",
     "2018-bb-ea-B3.1b"),
    ("Innenwinkel eines Dreiecks über das Skalarprodukt berechnen", "Analytische Geometrie",
     "Skalarprodukt und Winkel",
     "Den Winkel an einer Ecke eines Dreiecks im Raum aus dem Skalarprodukt der beiden "
     "anliegenden Seitenvektoren und ihren Beträgen bestimmen.",
     "2018-bb-ea-B3.1c"),
    ("Höhe eines Dreiecks im Raum über den Flächeninhalt berechnen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Den Flächeninhalt eines Dreiecks im Raum bestimmen und daraus die Höhe auf einer "
     "vorgegebenen Seite als doppelten Flächeninhalt geteilt durch die Seitenlänge gewinnen.",
     "2018-bb-ea-B3.1c"),
    ("Pyramidenvolumen aus Grundfläche und Höhe berechnen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Das Volumen einer Pyramide im Koordinatensystem aus dem Flächeninhalt der Grundfläche und "
     "dem Abstand der Spitze zu deren Ebene bestimmen.",
     "2018-bb-ea-B3.1d"),
    ("Bedarfsgröße aus einem Volumen im Sachzusammenhang nachweisen", "Analytische Geometrie",
     "Flächeninhalt und Volumen im Raum",
     "Aus einem berechneten Volumen über einen Dreisatz eine Bedarfsgröße wie Leistung oder Menge "
     "bestimmen und gegen einen vorgegebenen Wert prüfen.",
     "2018-bb-ea-B3.1d"),
    ("Punkt auf einer Strecke mit vorgegebenem Abstand zu einer Ebene bestimmen",
     "Analytische Geometrie", "Abstände",
     "Den Parameter eines Punktes auf einer Strecke so bestimmen, dass sein über die Hessesche "
     "Normalform berechneter Abstand zu einer gegebenen Ebene einen vorgegebenen Wert annimmt.",
     "2018-bb-ea-B3.1f"),
    ("Parametergleichung einer Ebene aus Punkten angeben", "Analytische Geometrie", "Ebenen",
     "Aus gegebenen Punkten einer Ebene einen Stützvektor und zwei nicht parallele Spannvektoren "
     "wählen und die Parameterform aufschreiben.",
     "2018-bb-ea-B3.2a"),
    ("Parameter einer Geradenschar aus einem vorgegebenen Durchstoßpunkt bestimmen",
     "Analytische Geometrie", "Scharen von Geraden und Ebenen",
     "Den Scharparameter so bestimmen, dass eine Gerade der Schar einen vorgegebenen Punkt trifft, "
     "indem die Parameterform diesem Punkt gleichgesetzt wird.",
     "2018-bb-ea-B3.2b"),
    ("Mittelpunkt eines Quadrates als Diagonalenmittelpunkt bestimmen", "Analytische Geometrie",
     "Punkte und Strecken im Koordinatensystem",
     "Den Mittelpunkt eines Vierecks im Raum als halbe Summe der Ortsvektoren zweier "
     "gegenüberliegender Eckpunkte berechnen.",
     "2018-bb-ea-B3.2b"),
    ("Schnittwinkel zweier Geraden über das Skalarprodukt berechnen", "Analytische Geometrie",
     "Skalarprodukt und Winkel",
     "Den Winkel zwischen zwei Geraden aus dem Betrag des Skalarprodukts ihrer Richtungsvektoren "
     "und deren Beträgen bestimmen, sodass der spitze Winkel entsteht.",
     "2018-bb-ea-B3.2b"),
    ("Lage eines durch eine Linearkombination gegebenen Punktes beschreiben",
     "Analytische Geometrie", "Linearkombination und lineare Abhängigkeit",
     "Eine als Linearkombination gegebene Punktdarstellung geometrisch deuten und die Lage des "
     "Punktes zu einer Figur in Worten beschreiben.",
     "2018-bb-ea-B3.2c"),
    ("Baumdiagramm zu einer zweistufigen Situation erstellen", "Stochastik",
     "Baumdiagramm und Pfadregeln",
     "Aus einer Wahrscheinlichkeit und einer bedingten Wahrscheinlichkeit ein beschriftetes "
     "zweistufiges Baumdiagramm mit allen Ästen und Pfadwahrscheinlichkeiten aufbauen.",
     "2018-bb-ea-B4.1a"),
    ("Wahrscheinlichkeit einer Binomialverteilung für genau k Treffer berechnen", "Stochastik",
     "Binomialverteilung",
     "Eine Situation als Bernoulli-Kette erkennen und die Wahrscheinlichkeit für eine vorgegebene "
     "Trefferzahl mit der Binomialformel berechnen.",
     "2018-bb-ea-B4.1b"),
    ("Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben", "Stochastik",
     "Binomialverteilung",
     "Einen abgedruckten Term aus Binomialformeln und Gegenwahrscheinlichkeit lesen und das "
     "zugehörige Ereignis in Worten beschreiben.",
     "2018-bb-ea-B4.1c"),
    ("Wahrscheinlichkeit beim Ziehen ohne Zurücklegen über das Gegenereignis berechnen",
     "Stochastik", "Hypergeometrische Verteilung",
     "Eine Auswahl ohne Zurücklegen als hypergeometrische Situation erkennen und die "
     "Wahrscheinlichkeit für höchstens oder mindestens eine Trefferzahl über das Gegenereignis "
     "bestimmen.",
     "2018-bb-ea-B4.1d"),
    ("Vierfeldertafel aus Anteilen aufstellen", "Stochastik", "Vierfeldertafel",
     "Aus Randanteilen und einem Anteil innerhalb einer Teilgruppe die vier Felder einer "
     "Vierfeldertafel vollständig berechnen.",
     "2018-bb-ea-B4.2a"),
    ("Bedingte Wahrscheinlichkeit aus der Vierfeldertafel berechnen", "Stochastik",
     "Bedingte Wahrscheinlichkeit und Bayes",
     "Eine bedingte Wahrscheinlichkeit als Quotient aus einem Feld der Vierfeldertafel und dem "
     "zugehörigen Randwert bestimmen.",
     "2018-bb-ea-B4.2a"),
    ("Trefferwahrscheinlichkeit beim Wechsel der Trefferdefinition anpassen", "Stochastik",
     "Binomialverteilung",
     "Bei einer nach dem Gegenmerkmal gefragten Anzahl die Trefferwahrscheinlichkeit auf die "
     "Gegenwahrscheinlichkeit umstellen oder gleichwertig die Trefferzahl umrechnen.",
     "2018-bb-ea-B4.2b"),
    ("Wahrscheinlichkeiten über den Erwartungswert vergleichen", "Stochastik",
     "Kenngrößen von Verteilungen",
     "Zwei Einzelwahrscheinlichkeiten einer Binomialverteilung ohne Rechnung vergleichen, indem "
     "ihre Abstände zum Erwartungswert betrachtet werden.",
     "2018-bb-ea-B4.2c"),
    ("Entscheidungsregel für einen einseitigen Signifikanztest bestimmen", "Stochastik",
     "Hypothesentests",
     "Zu einer Nullhypothese, einem Stichprobenumfang und einem Signifikanzniveau den "
     "Ablehnungsbereich eines einseitigen Tests aus der summierten Binomialverteilung ablesen.",
     "2018-bb-ea-B4.2d"),
    ("Mindestanzahl beim Ziehen ohne Zurücklegen über das Gegenereignis bestimmen", "Stochastik",
     "Zufallsexperimente und Urnenmodelle",
     "Die kleinste Anzahl zu ziehender Elemente bestimmen, für die eine geforderte "
     "Mindestwahrscheinlichkeit erreicht wird, über das Gegenereignis und eine Ungleichung.",
     "2018-bb-ea-B4.2e"),
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
