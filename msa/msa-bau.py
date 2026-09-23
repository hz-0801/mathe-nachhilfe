# -*- coding: utf-8 -*-
"""msa-bau.py – Gerüst für die Erfassung eines Hefts im Profil msa und Selbstprüfung des Bestands.
Version 0.3 · 23.09.2026 · gilt mit katalog-prompt.md v0.9 und msa.md v0.7

Änderungen gegenüber 0.2 (Auftrag Gymnasialhefte, 23.09.2026): papier-Muster um
GYM erweitert (msa.md § 4); KONFIG führt daneben „dateien" (Liste, weil ab 2019
zwei PDF je Heft), der Altwert „datei" bleibt gültig – beide Felder sind rein
informativ und werden vom Skript nicht ausgewertet. Zeilen mit papier GYM
werden unabhängig von block nach msa-katalog-gym.csv geschrieben (beide
Blöcke in einer Datei, Feld block trennt sie wie gehabt); OS/EBR/FOR/MUSTER
unverändert nach msa-katalog-basis.csv/msa-katalog-kontext.csv. Die
Selbstprüfung liest jetzt alle drei Katalogdateien. KONFIG["seiten"] darf für
zweiteilige Hefte ein dict {block: seiten} sein (Seite zählt je PDF-Datei neu,
die beiden Gymnasialteile haben getrennte Fußzeilen "Seite N von M"); ein
einzelner int bleibt wie bisher gültig. Selbstprüfung für OS/EBR/FOR/MUSTER
byteidentisch zu 0.2 (393 Zeilen, 185 Typen, gleiche Hashes, vor dem ersten
GYM-Heft geprüft).

Änderungen gegenüber 0.1 (Auftrag F, Punkt 1, 17.09.2026): Die Dateien des
Profils tragen das Präfix msa- (KAT, TYP: msa-katalog-basis.csv,
msa-katalog-kontext.csv, msa-typen.csv; namensschema.md § 4, Variante B).
Nur die Namen, keine Prüfung geändert; Selbstprüfung byteidentisch zu 0.1.

Angelegt in Auftrag E (Punkt 6, 17.09.2026). Der msa-Bestand (2014–2026, 393
Zeilen in zwei Katalogdateien, 185 Typen) wurde ohne Skript im Chat erfasst
(Kern v0.3, konzept.md § 7); dieses Gerüst folgt fhr-bau.py v0.2 und prüft
nach Kern § 7, damit msa denselben Weg hat wie die anderen Profile: Skript
prüft, Skript schreibt, keine Handedits in den CSV-Dateien.

Je Heft werden nur KONFIG, ZEILEN und NEUE_TYPEN ausgetauscht. Zwei
Katalogdateien (msa.md § 4, Entscheidung 14): block „Basis" → msa-katalog-basis.csv,
block „Kontext" → msa-katalog-kontext.csv. Leitideen und Themenliste liest das
Skript aus msa.md § 5 und § 6.

Ist ZEILEN leer, läuft die Selbstprüfung über den Bestand (beide Kataloge
gegen Kern § 5 und msa.md, jede Typenverwendung, jede beispiel_id, kein Typ
unbenutzt) und schreibt nichts – außer eine Feldkorrektur in TYPEN_KORREKTUR
steht noch aus.

TYPEN_KORREKTUR: Feldkorrektur an msa-typen.csv (leitidee, thema, definition eines
vorhandenen Typs). Das Profil msa hat kein Abgleichskript; die Korrektur läuft
deshalb hier, wird einmal angewendet (Liste alt → neu im Bericht) und ist
danach wirkungslos, weil der Zielzustand schon steht – ein erneuter Lauf
schreibt nichts. Angewendet 17.09.2026 (Auftrag E, Punkt 6; Vorschlag 4 aus
befund-typenlisten.md § 3): „Behauptung prüfen" bekommt Leitidee und Thema
seiner ersten Fundstelle 2025-OS-K3b, weil der Kern § 6 jedem Typ leitidee und
thema gibt; der Typ bleibt Nebentyp über alle Leitideen (Definition).

Ablauf:
  1. katalog-prompt.md, msa.md, msa-typen.csv, msa-katalog-basis.csv, msa-katalog-kontext.csv
     neben dieses Skript legen (aus dem Repo).
  2. KONFIG, ZEILEN, NEUE_TYPEN füllen – oder leer lassen für die Selbstprüfung.
  3. python msa-bau.py – schreibt die CSV-Dateien, gibt Prüftabelle und Bericht
     aus. Bei einem Fehler wird nichts geschrieben.
"""
import csv, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")

# ===================================================================== KONFIG
# ===================================================================== KONFIG
KONFIG = {
    "jahr": "2020",
    "papier": "GYM",     # OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM (msa.md § 4)
    "datei": "",         # zweiteiliges Heft ab 2019, siehe "dateien"
    "dateien": ["20_P10_Ma_Gym_A_1.pdf", "20_P10_Ma_Gym_A_2.pdf"],
    "seiten": {"Basis": 3, "Kontext": 9},  # eigene Fußzeile je Teildatei (msa.md § 3)
    "soll": {"1": 5, "2": 5, "3": 10, "4": 11, "5": 10, "6": 9},
    "soll_gesamt": 50,
}

# ---- technischer Block, nicht ändern ----
HEAD = ("id;jahr;papier;block;aufgabe;titel;teilaufgabe;seite;punkte;stern;hilfsmittel;afb_amtlich;"
        "leitidee;thema;typ;typ_neben;stichwoerter;voraussetzungen;format;operator;antwort;material;"
        "skizze;kontext;textumfang;gegeben;gesucht;verfahren;schritte;zahlenraum;einheiten;"
        "abhaengig_von;ergebnis;zwischenergebnis;niveau_geschaetzt;fehlerquelle;bemerkung").split(";")

ZEILEN = []

def row(**kw):
    z = {k: "" for k in HEAD}
    z.update(jahr=KONFIG["jahr"], papier=KONFIG["papier"], stern="", hilfsmittel="ja", afb_amtlich="")
    unbekannt = set(kw) - set(HEAD)
    if unbekannt:
        sys.exit(f"unbekanntes Feld: {sorted(unbekannt)}")
    z.update(kw)
    ZEILEN.append(z)

# ============================================================ ZEILEN JE HEFT

# Neue Typen: (typ, leitidee, thema, definition, beispiel_id)
NEUE_TYPEN = [
    ("x-Werte einer quadratischen Funktion zu gegebenem Funktionswert berechnen", "Gleichungen und Funktionen",
     "Quadratische Funktionen",
     "Zu einem gegebenen Funktionswert einer quadratischen Funktion der Form f(x)=x²+c die beiden "
     "zugehörigen x-Werte durch Auflösen nach x (Wurzelziehen) berechnen; abzugrenzen von „Nullstellen "
     "quadratische Funktion berechnen“, bei der der Funktionswert 0 ist.",
     "2020-GYM-B2a"),
    ("Fehlende Schnittpunkte zweier Funktionen über Wertebereiche begründen", "Gleichungen und Funktionen",
     "Quadratische Funktionen",
     "Begründen, dass zwei Funktionsgraphen keine gemeinsamen Punkte besitzen, indem die Wertebereiche "
     "beider Funktionen bestimmt und als disjunkt (ohne Überschneidung) nachgewiesen werden.",
     "2020-GYM-B2b"),
    ("Parameter einer Wurzelfunktion aus einem Punkt bestimmen", "Gleichungen und Funktionen",
     "Funktionen allgemein",
     "Den Wurzelexponenten n einer Funktion der Form g(x)=ⁿ√x aus einem gegebenen Punkt des Graphen durch "
     "Einsetzen und Lösen bestimmen und die Funktionsgleichung angeben.",
     "2020-GYM-K3a"),
    ("Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen", "Gleichungen und Funktionen",
     "Funktionen allgemein",
     "Den Graphen der Umkehrfunktion einer Wurzelfunktion durch Spiegelung an der Geraden y=x skizzieren "
     "(die Umkehrfunktion von ⁿ√x ist xⁿ) und den Wertebereich der Umkehrfunktion für ein gegebenes "
     "Intervall angeben.",
     "2020-GYM-K3b"),
    ("Anstieg einer linearen Funktion aus Punkt und y-Achsenabschnitt berechnen", "Gleichungen und Funktionen",
     "Lineare Funktionen",
     "Anstieg einer linearen Funktion mit gegebenem y-Achsenabschnitt aus einem bekannten Punkt des "
     "Graphen durch Einsetzen und Auflösen berechnen.",
     "2020-GYM-K3c"),
    ("Grundfläche eines Prismas im Körpernetz kennzeichnen", "Raum und Form", "Körper, Netze, Schrägbilder",
     "In einem Körpernetz eines Prismas eine Fläche markieren, die als Grundfläche des Prismas dienen kann "
     "(eine der beiden deckungsgleichen Vielecksflächen, nicht eine der rechteckigen Seitenflächen).",
     "2020-GYM-K5a"),
    ("Maße eines Körpers aus einem bemaßten Netz im Maßstab ablesen", "Raum und Form",
     "Körper, Netze, Schrägbilder",
     "Reale Maße eines Körpers aus einem im Maßstab gezeichneten, nur mit einem Maßstabsbalken (ohne "
     "Zahlenangaben) versehenen Körpernetz durch Ausmessen der Zeichnung und Umrechnen über den Maßstab "
     "bestimmen.",
     "2020-GYM-K5b"),
    ("Kugeldurchmesser aus Anzahl nebeneinanderliegender Kugeln bestimmen", "Größen und Messen",
     "Volumen und Oberfläche",
     "Durchmesser einer Kugel aus der Anzahl gleich großer, nebeneinander auf einer Fläche angeordneter "
     "Kugeln und der Kantenlänge der Fläche bestimmen (Fläche geteilt durch Kugeln je Reihe).",
     "2020-GYM-K5d"),
]

row(id="2020-GYM-B1a", block="Basis", aufgabe="1", titel="", teilaufgabe="a", seite="2",
    punkte="2", hilfsmittel="nein", leitidee="Größen und Messen", thema="Satz des Pythagoras",
    typ="Pythagoras Hypotenuse",
    stichwoerter="rechtwinkliges Dreieck|Hypotenuse|Katheten", format="Rechnung", operator="Ermitteln Sie",
    antwort="Zahl", material="Figur",
    skizze="Dreieck ABC mit rechtem Winkel bei C, eingebettet in eine Figur mit zwei parallelen Geraden g "
           "und h durch B bzw. A/C und einer weiteren Geraden durch B und A",
    kontext="ohne", textumfang="kurz",
    gegeben="rechtwinkliges Dreieck ABC mit rechtem Winkel bei C; |BC| = 6 cm, |AC| = 8 cm",
    gesucht="Länge der Hypotenuse AB",
    verfahren="Satz des Pythagoras: |AB| = √(6² + 8²)", schritte="1", zahlenraum="ganz", einheiten="cm",
    ergebnis="|AB| = 10 cm", niveau_geschaetzt="I",
    fehlerquelle="6 cm oder 8 cm fälschlich als Hypotenuse statt als Kathete verwenden")

row(id="2020-GYM-B1b", block="Basis", aufgabe="1", titel="", teilaufgabe="b", seite="2",
    punkte="3", hilfsmittel="nein", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Winkel an geschnittenen Parallelen bestimmen",
    stichwoerter="Parallele|Stufenwinkel|Wechselwinkel|Dreieckswinkelsumme", format="Rechnung",
    operator="Geben Sie an", antwort="Zahl", material="Figur",
    skizze="zwei Parallelen g (durch B) und h (durch A, C); Gerade durch B und einen Punkt P auf g "
           "oberhalb von B mit 120° am Schnittpunkt mit g; Gerade AB schneidet g bei B mit 65° zwischen "
           "dem Strahl BP und BA; rechtwinkliges Dreieck ABC mit rechtem Winkel bei C; bei A liegen die "
           "Winkel α (links), φ (oben rechts) und β (unten rechts, an C angrenzend)",
    kontext="ohne", textumfang="mittel",
    gegeben="g ∥ h; Winkel 120° zwischen g und der Geraden BP (P auf g oberhalb B); Winkel 65° zwischen "
            "dem Strahl BP und der Strecke BA; rechter Winkel bei C zwischen CA und CB",
    gesucht="Winkel α, β und φ bei A",
    verfahren="Hilfspunkt P auf g, an dem die Gerade PA g unter 120° schneidet: im Dreieck PAB ist der "
              "Winkel bei P gleich 180° − 120° = 60° (Nebenwinkel zu 120° auf g), der Winkel bei B ist "
              "65° (gegeben); Winkelsumme im Dreieck PAB liefert den Winkel bei A zwischen AP und AB: "
              "α = 180° − 60° − 65° = 55°; da g ∥ h, ist φ als Stufenwinkel zum 65°-Winkel bei B (an der "
              "Geraden AB als Schneidender) gleich φ = 65°; α + β + φ = 180° (Winkel an der Geraden h bei "
              "A auf einer Seite von PA), also β = 180° − 55° − 65° = 60°",
    schritte="4", zahlenraum="ganz", einheiten="Grad", ergebnis="α = 55°, β = 60°, φ = 65°",
    niveau_geschaetzt="III",
    fehlerquelle="120° unmittelbar als Stufen- oder Wechselwinkel zu einem der gesuchten Winkel bei A "
                 "übernehmen, ohne den Nebenwinkel bei P zu bilden",
    bemerkung="Die Skizze ist ausdrücklich nicht maßstabsgerecht (im Heft vermerkt) und weicht in den "
              "gezeichneten Winkelgrößen deutlich von den berechneten Werten ab; die Zuordnung der drei "
              "Geraden (g durch B, h durch A/C, Gerade PA durch den 120°-Punkt und A) wurde über die "
              "Vektordaten der PDF-Seite (Liniensegmente, Beschriftungspositionen) bestimmt, die Winkel "
              "selbst über Nebenwinkel-, Stufenwinkel- und Dreieckswinkelsumme errechnet und durch die "
              "Winkelsumme 180° im Hilfsdreieck PAB gegengeprüft (55° + 65° + 60° = 180°, stimmt).")

row(id="2020-GYM-B2a", block="Basis", aufgabe="2", titel="", teilaufgabe="a", seite="3",
    punkte="2", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="x-Werte einer quadratischen Funktion zu gegebenem Funktionswert berechnen",
    stichwoerter="quadratische Funktion|Funktionswert|symmetrische Lösungen", format="Kurzantwort",
    operator="Geben Sie an", antwort="Zahl", material="keins",
    skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="quadratische Funktion f mit f(x) = x² − 2; Punkte P1(x1|23) und P2(x2|23) auf dem Graphen",
    gesucht="Werte für x1 und x2",
    verfahren="x² − 2 = 23 ⟹ x² = 25 ⟹ x = ±5", schritte="1", zahlenraum="ganz",
    ergebnis="x1 = 5, x2 = −5 (oder umgekehrt)", niveau_geschaetzt="II",
    fehlerquelle="nur die positive Lösung x=5 angeben und die zweite (symmetrische) Lösung x=−5 übersehen")

row(id="2020-GYM-B2b", block="Basis", aufgabe="2", titel="", teilaufgabe="b", seite="3",
    punkte="3", hilfsmittel="nein", leitidee="Gleichungen und Funktionen", thema="Quadratische Funktionen",
    typ="Fehlende Schnittpunkte zweier Funktionen über Wertebereiche begründen",
    stichwoerter="Wertebereich|Parabel|Begründung|keine Schnittpunkte", format="Begründung",
    operator="Begründen Sie", antwort="Text", material="keins",
    skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="f(x) = x² − 2 und h(x) = −x² − 3",
    gesucht="Begründung, dass f und h keine gemeinsamen Schnittpunkte besitzen",
    verfahren="f hat den Scheitelpunkt (Minimum) bei (0|−2), also f(x) ≥ −2 für alle x; h hat den "
              "Scheitelpunkt (Maximum) bei (0|−3), also h(x) ≤ −3 für alle x; da −2 > −3, gilt f(x) ≥ −2 "
              "> −3 ≥ h(x) für alle x, die Graphen können sich also nie treffen",
    schritte="2", zahlenraum="ganz",
    ergebnis="kein gemeinsamer Punkt, da Wertebereich von f (≥ −2) und Wertebereich von h (≤ −3) disjunkt "
             "sind", niveau_geschaetzt="III",
    fehlerquelle="x² − 2 = −x² − 3 gleichsetzen und aus der negativen Diskriminante (2x² = −1) nur „keine "
                 "Lösung“ ohne inhaltliche Begründung über die Wertebereiche folgern")

row(id="2020-GYM-K3a", block="Kontext", aufgabe="3", titel="Funktionen", teilaufgabe="a", seite="2",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Funktionen allgemein",
    typ="Parameter einer Wurzelfunktion aus einem Punkt bestimmen",
    stichwoerter="Wurzelfunktion|Wurzelexponent|Graph", format="Rechnung", operator="Ermitteln Sie",
    antwort="Term", material="Figur",
    skizze="Graph einer Wurzelfunktion durch den Ursprung, streng monoton steigend und konkav, "
           "Punkt P(8|2) markiert, Koordinatensystem 0 bis 10",
    kontext="ohne", textumfang="kurz",
    gegeben="Funktion g der Form g(x) = ⁿ√x; Punkt P(8|2) liegt auf dem Graphen von g",
    gesucht="Wert für n und Funktionsgleichung von g",
    verfahren="8^(1/n) = 2 ⟹ 2^n = 8 ⟹ n = 3", schritte="1", zahlenraum="ganz",
    ergebnis="n = 3, g(x) = ³√x", niveau_geschaetzt="II",
    fehlerquelle="n mit dem Funktionswert 2 verwechseln oder g(x) = 8/x (indirekte Proportionalität) "
                 "statt der Wurzelfunktion ansetzen")

row(id="2020-GYM-K3b", block="Kontext", aufgabe="3", titel="Funktionen", teilaufgabe="b", seite="3",
    punkte="4", leitidee="Gleichungen und Funktionen", thema="Funktionen allgemein",
    typ="Umkehrfunktion einer Wurzelfunktion durch Spiegelung an y=x bestimmen",
    stichwoerter="Spiegelung|Umkehrfunktion|Wertebereich|Winkelhalbierende", format="Zeichnen|Kurzantwort",
    operator="Skizzieren Sie|Geben Sie an", antwort="Grafik|Zahl", material="Koordinatensystem",
    skizze="Graph von g (³√x) im 1. Quadranten wird an der Geraden y=x gespiegelt; gesucht ist der "
           "gespiegelte Graph im Intervall [0;2] im selben Koordinatensystem (0 bis 10)",
    kontext="ohne", textumfang="kurz",
    gegeben="g(x) = ³√x; Spiegelung des Graphen von g im 1. Quadranten an der Geraden y = x ergibt g′",
    gesucht="Graph von g′ im Intervall [0;2] und Wertebereich von g′ in diesem Intervall",
    verfahren="Spiegelung an y=x vertauscht x- und y-Werte, die Umkehrfunktion der Wurzelfunktion ³√x ist "
              "die Potenzfunktion x³, also g′(x) = x³; g′ ist auf [0;2] streng monoton steigend mit "
              "g′(0)=0 und g′(2)=8",
    schritte="2", zahlenraum="ganz", abhaengig_von="2020-GYM-K3a",
    ergebnis="g′(x) = x³; Wertebereich von g′ auf [0;2] ist [0;8]", niveau_geschaetzt="III",
    fehlerquelle="den Graphen an der y-Achse statt an der Geraden y=x spiegeln, oder den Wertebereich mit "
                 "dem Definitionsbereich [0;2] verwechseln")

row(id="2020-GYM-K3c", block="Kontext", aufgabe="3", titel="Funktionen", teilaufgabe="c", seite="3",
    punkte="3", leitidee="Gleichungen und Funktionen", thema="Lineare Funktionen",
    typ="Anstieg einer linearen Funktion aus Punkt und y-Achsenabschnitt berechnen",
    typ_neben="Nullstelle lineare Funktion berechnen",
    stichwoerter="lineare Funktion|Anstieg|Nullstelle|y-Achsenabschnitt", format="Rechnung|Kurzantwort",
    operator="Berechnen Sie|Geben Sie an", antwort="Zahl|Zahl", material="keins",
    skizze="keine", kontext="ohne", textumfang="kurz",
    gegeben="lineare Funktion h mit h(x) = mx − 2; der Punkt P(8|2) liegt auf dem Graphen von h",
    gesucht="Anstieg m von h und Nullstelle von h",
    verfahren="2 = m·8 − 2 ⟹ 8m = 4 ⟹ m = 0,5; Nullstelle: 0,5x − 2 = 0 ⟹ x = 4", schritte="2",
    zahlenraum="dezimal", abhaengig_von="2020-GYM-K3a",
    ergebnis="m = 0,5; Nullstelle x = 4", niveau_geschaetzt="II",
    fehlerquelle="das Vorzeichen des y-Achsenabschnitts −2 beim Einsetzen vertauschen")

row(id="2020-GYM-K4a", block="Kontext", aufgabe="4", titel="Seilbahn", teilaufgabe="a", seite="4",
    punkte="1", leitidee="Raum und Form", thema="Ebene Figuren und Winkel",
    typ="Strecke aus Teilstrecken berechnen",
    stichwoerter="Höhenunterschied|Seilbahn|Differenz", format="Kurzantwort", operator="Geben Sie an",
    antwort="Zahl", material="Tabelle",
    skizze="Dreieck aus Talstation T, Zwischenstation Z, Bergstation B mit Winkel α bei Z; Tabelle mit "
           "Höhenangaben, horizontaler Entfernung und maximaler Steigung",
    kontext="Freizeit/Technik", textumfang="kurz",
    gegeben="Talstation 670 m über dem Meeresspiegel; Bergstation 1250 m über dem Meeresspiegel",
    gesucht="Höhenunterschied, der durch die Seilbahn überwunden wird",
    verfahren="1250 m − 670 m", schritte="1", zahlenraum="ganz", einheiten="m",
    ergebnis="580 m", niveau_geschaetzt="I", fehlerquelle="keine (einfache Differenz)")

row(id="2020-GYM-K4b", block="Kontext", aufgabe="4", titel="Seilbahn", teilaufgabe="b", seite="4",
    punkte="2", leitidee="Größen und Messen", thema="Trigonometrie im rechtwinkligen Dreieck",
    typ="Neigungswinkel einer Geraden berechnen", typ_neben="Steigung in Prozent deuten",
    stichwoerter="Steigungswinkel|Steigung in Prozent|Tangens", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Tabelle",
    skizze="keine (Hinweistext: 1 % Steigung = 1 m Höhenunterschied auf 100 m horizontale Entfernung)",
    kontext="Freizeit/Technik", textumfang="mittel",
    gegeben="maximale Steigung der Seilbahn 150 %",
    gesucht="zur maximalen Steigung gehörender Steigungswinkel",
    verfahren="150 % Steigung bedeutet ein Verhältnis Höhe zu horizontaler Strecke von 1,5; "
              "Steigungswinkel = arctan(1,5)", schritte="2", zahlenraum="dezimal", einheiten="Grad",
    ergebnis="≈ 56,3°", niveau_geschaetzt="II",
    fehlerquelle="150 % direkt als Winkel verwenden oder durch 180° statt über den Tangens umrechnen")

row(id="2020-GYM-K4c", block="Kontext", aufgabe="4", titel="Seilbahn", teilaufgabe="c", seite="4",
    punkte="3", leitidee="Größen und Messen", thema="Sinussatz",
    typ="Winkel im allgemeinen Dreieck über Kosinussatz berechnen",
    stichwoerter="Kosinussatz|Dreieck TZB|eingeschlossener Winkel", format="Rechnung",
    operator="Berechnen Sie", antwort="Zahl", material="Tabelle|Figur",
    skizze="Dreieck TZB mit den Seiten TZ, ZB, TB und dem gesuchten Winkel α bei Z",
    kontext="Freizeit/Technik", textumfang="mittel",
    gegeben="Dreieck TZB mit TB = 775 m (direkte Verbindung Tal-/Bergstation), Gesamtlänge der Seilbahn "
            "TZ + ZB = 945 m, TZ = 510 m (also ZB = 945 m − 510 m = 435 m)",
    gesucht="Winkel α zwischen den Teilabschnitten TZ und ZB (Winkel bei Z im Dreieck TZB)",
    verfahren="Kosinussatz: TB² = TZ² + ZB² − 2·TZ·ZB·cos(α), aufgelöst nach α", schritte="2",
    zahlenraum="dezimal", einheiten="Grad", abhaengig_von="2020-GYM-K4a",
    ergebnis="α ≈ 109,9°", niveau_geschaetzt="III",
    fehlerquelle="TB fälschlich als dritte Seilbahnstrecke statt als direkte Verbindung verwenden, oder "
                 "ZB nicht aus 945 m − 510 m ermitteln")

row(id="2020-GYM-K4d", block="Kontext", aufgabe="4", titel="Seilbahn", teilaufgabe="d", seite="4",
    punkte="5", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Transportanzahl aus Volumen und Masse berechnen", typ_neben="Volumen Zylinder berechnen",
    stichwoerter="Holzstamm|Nutzlast|Zylindervolumen|Dichte", format="Begründung",
    operator="Zeigen Sie rechnerisch", antwort="Text", material="keins",
    skizze="keine", kontext="Freizeit/Technik", textumfang="mittel",
    gegeben="maximale Nutzlast 250 kg; jeder Holzstamm ist ein Zylinder mit Länge 2 m und Durchmesser "
            "20 cm (Radius 0,1 m); 1 m³ Holz wiegt 1,3 t",
    gesucht="Nachweis, dass gleichzeitig maximal drei Stämme transportiert werden können",
    verfahren="Volumen je Stamm V = π·0,1²·2 ≈ 0,0628 m³; Masse je Stamm ≈ 0,0628·1300 kg ≈ 81,7 kg; drei "
              "Stämme ≈ 245,0 kg ≤ 250 kg (zulässig), vier Stämme ≈ 326,7 kg > 250 kg (nicht zulässig)",
    schritte="3", zahlenraum="dezimal", einheiten="m|kg", abhaengig_von="2020-GYM-K4a",
    ergebnis="ein Stamm ≈ 81,7 kg; drei Stämme ≈ 245,0 kg ≤ 250 kg; vier Stämme ≈ 326,7 kg > 250 kg, also "
             "maximal drei Stämme", niveau_geschaetzt="III",
    fehlerquelle="die Dichte 1,3 t/m³ als 1,3 kg/m³ verwenden oder den Durchmesser statt des Radius in die "
                 "Volumenformel einsetzen")

row(id="2020-GYM-K5a", block="Kontext", aufgabe="5", titel="Verpackung", teilaufgabe="a", seite="5",
    punkte="1", leitidee="Raum und Form", thema="Körper, Netze, Schrägbilder",
    typ="Grundfläche eines Prismas im Körpernetz kennzeichnen",
    stichwoerter="Körpernetz|Prisma|Grundfläche|fünfeckig", format="Ankreuzen", operator="Kennzeichnen Sie",
    antwort="Kreuz", material="Figur",
    skizze="Körpernetz eines fünfseitigen Prismas: mittleres Band aus fünf aneinandergereihten Rechtecken "
           "(Mantelflächen), oben und unten je eine fünfeckige (hausförmige) Fläche als Grund- bzw. "
           "Deckfläche, Maßstabsbalken 1 cm am Rand",
    kontext="Freizeit/Konsum", textumfang="kurz",
    gegeben="Körpernetz eines Prismas (Verpackung für Schokokugeln) im Maßstab 1:3",
    gesucht="eine Fläche im Netz, die Grundfläche des Prismas sein kann",
    verfahren="Grundfläche und Deckfläche eines Prismas sind die beiden deckungsgleichen Vielecksflächen, "
              "hier die beiden fünfeckigen (hausförmigen) Flächen an den Enden des Netzes, nicht die "
              "rechteckigen Mantelflächen", schritte="1",
    ergebnis="eine der beiden fünfeckigen Flächen am oberen oder unteren Rand des Netzes",
    niveau_geschaetzt="I",
    fehlerquelle="eine der rechteckigen Mantelflächen als Grundfläche markieren")

row(id="2020-GYM-K5b", block="Kontext", aufgabe="5", titel="Verpackung", teilaufgabe="b", seite="5",
    punkte="3", leitidee="Raum und Form", thema="Körper, Netze, Schrägbilder",
    typ="Maße eines Körpers aus einem bemaßten Netz im Maßstab ablesen",
    typ_neben="Volumen Prisma berechnen",
    stichwoerter="Körpernetz|Maßstab|Fünfeck|Prismenvolumen", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur",
    skizze="wie 2020-GYM-K5a; keine Zahlenmaße im Netz, nur ein Maßstabsbalken „1 cm“",
    kontext="Freizeit/Konsum", textumfang="kurz", abhaengig_von="2020-GYM-K5a",
    gegeben="Körpernetz im Maßstab 1:3, bemaßt nur durch einen 1-cm-Maßstabsbalken; aus dem Netz "
            "ausgemessen (auf der Zeichnung): Breite der fünfeckigen Grundfläche 3 cm, Höhe des "
            "rechteckigen Teils der Grundfläche 2 cm, Höhe des dreieckigen (Dach-)Teils 2 cm, Länge des "
            "Prismas (Breite der Mantelrechtecke in Längsrichtung) 3 cm",
    gesucht="Volumen der Verpackung",
    verfahren="reale Maße = gezeichnete Maße · 3 (Maßstab 1:3): Grundflächenbreite 9 cm, Rechteckhöhe "
              "6 cm, Dreieckshöhe 6 cm, Prismenlänge 9 cm; Grundfläche (Fünfeck) = Rechteck + Dreieck = "
              "9 cm · 6 cm + 0,5 · 9 cm · 6 cm = 54 cm² + 27 cm² = 81 cm²; Volumen = Grundfläche · Länge "
              "= 81 cm² · 9 cm",
    schritte="3", zahlenraum="dezimal", einheiten="cm|cm²|cm³",
    ergebnis="V = 729 cm³ ≈ 0,73 L?", niveau_geschaetzt="III",
    fehlerquelle="den Maßstab 1:3 auf die bereits umgerechneten Flächen- oder Volumenwerte statt auf die "
                 "Längen anwenden",
    bemerkung="Ergebnis unsicher: Das Heft gibt für das Netz keine Zahlenmaße an, nur einen gezeichneten "
              "1-cm-Maßstabsbalken. Die Längen wurden aus der PDF-Vektorgrafik ausgemessen (Pixel- und "
              "Vektorkoordinaten von Linien und Maßstabsbalken, Maßstabsbalken ≈ 24,1 pt = 1 cm auf der "
              "Zeichnung) und auf glatte Zentimeterwerte (3/2/2/3 cm) gerundet; diese runden Werte bilden "
              "für die Dachschräge ein sauberes Steigungsdreieck im Verhältnis 1,5 zu 2 zu 2,5 "
              "(gestrecktes Dreieck im Verhältnis 3 zu 4 zu 5), was für die Richtigkeit der Rundung "
              "spricht, aber nicht mit letzter Sicherheit auf dem amtlichen Originalmaß beruht.")

row(id="2020-GYM-K5c", block="Kontext", aufgabe="5", titel="Verpackung", teilaufgabe="c", seite="6",
    punkte="3", leitidee="Raum und Form", thema="Körper, Netze, Schrägbilder",
    typ="Körper im Schrägbild darstellen",
    stichwoerter="Schrägbild|Prisma|Verpackung", format="Zeichnen", operator="Zeichnen Sie",
    antwort="Grafik", material="keins",
    skizze="Schrägbild des fünfseitigen Prismas (Grundfläche Fünfeck, fünf rechteckige Seitenflächen)",
    kontext="Freizeit/Konsum", textumfang="kurz", abhaengig_von="2020-GYM-K5a",
    gegeben="Prisma mit fünfeckiger Grundfläche (Maße aus Teilaufgabe b)",
    gesucht="Schrägbild des Körpers",
    verfahren="Grundfläche als Fünfeck perspektivisch verzerrt zeichnen, Kanten parallel und verkürzt in "
              "die Tiefe führen, Deckfläche kongruent versetzt einzeichnen", schritte="1",
    ergebnis="Schrägbild eines fünfseitigen Prismas", niveau_geschaetzt="II",
    fehlerquelle="Kanten nicht parallel oder ohne einheitliche Verkürzung in die Tiefe zeichnen")

row(id="2020-GYM-K5d", block="Kontext", aufgabe="5", titel="Verpackung", teilaufgabe="d", seite="6",
    punkte="3", leitidee="Größen und Messen", thema="Volumen und Oberfläche",
    typ="Kugeldurchmesser aus Anzahl nebeneinanderliegender Kugeln bestimmen",
    typ_neben="Volumen Kugel berechnen",
    stichwoerter="Schokokugel|Kugelpackung|Kugelvolumen", format="Rechnung", operator="Berechnen Sie",
    antwort="Zahl", material="Figur", abhaengig_von="2020-GYM-K5b",
    skizze="16 gleich große Kreise (Schokokugeln von oben) liegen nebeneinander auf dem rechteckigen Boden "
           "der Verpackung (9 cm × 9 cm), angeordnet in einem 4×4-Raster",
    kontext="Freizeit/Konsum", textumfang="mittel",
    gegeben="16 gleich große Schokokugeln liegen nebeneinander auf dem quadratischen Boden der Verpackung "
            "(Seitenlänge 9 cm, aus Teilaufgabe b); Anordnung 4 Kugeln je Reihe in beiden Richtungen "
            "(4 × 4 = 16 Kugeln)",
    gesucht="maximal mögliches Volumen einer Schokokugel",
    verfahren="Durchmesser d = 9 cm : 4 = 2,25 cm, Radius r = 1,125 cm; V = 4/3 · π · r³", schritte="2",
    zahlenraum="dezimal", einheiten="cm|cm³",
    ergebnis="d = 2,25 cm; V ≈ 5,96 cm³", niveau_geschaetzt="III",
    fehlerquelle="16 Kugeln als eine Reihe (statt 4×4-Raster) auffassen und den Durchmesser durch 16 statt "
                 "durch 4 teilen")

row(id="2020-GYM-K6a", block="Kontext", aufgabe="6", titel="Handballtraining", teilaufgabe="a", seite="7",
    punkte="2", leitidee="Daten und Zufall", thema="Zählen und Kombinatorik",
    typ="Anzahl der Auswahlmöglichkeiten (Kombination) bestimmen",
    stichwoerter="Handschlag|Kombination|Trainer", format="Rechnung", operator="Ermitteln Sie",
    antwort="Zahl", material="keins",
    skizze="keine", kontext="Freizeit/Sport", textumfang="kurz",
    gegeben="20 Sportler begrüßen sich untereinander mit Handschlag; zusätzlich begrüßt der Trainer jeden "
            "der 20 Sportler mit Handschlag",
    gesucht="Gesamtzahl der Handschläge",
    verfahren="Handschläge der Sportler untereinander: Anzahl der 2er-Kombinationen aus 20, C(20,2) = 190; "
              "dazu die 20 Handschläge des Trainers", schritte="2", zahlenraum="ganz",
    ergebnis="190 + 20 = 210 Handschläge", niveau_geschaetzt="II",
    fehlerquelle="die Handschläge des Trainers vergessen oder C(20,2) mit 20² verwechseln (Reihenfolge "
                 "der Begrüßung zählt nicht doppelt)")

row(id="2020-GYM-K6b", block="Kontext", aufgabe="6", titel="Handballtraining", teilaufgabe="b", seite="7",
    punkte="2", leitidee="Daten und Zufall", thema="Wahrscheinlichkeit mehrstufig",
    typ="Wahrscheinlichkeit mehrstufig ohne Zurücklegen",
    stichwoerter="Trainingsshirts|ohne Zurücklegen|fünfstufig", format="Rechnung",
    operator="Bestimmen Sie", antwort="Zahl", material="keins",
    skizze="keine", kontext="Freizeit/Sport", textumfang="mittel",
    gegeben="24 Trainingsshirts (je 6 rote, gelbe, blaue, grüne) in einer Kiste; ein Kapitän greift ohne "
            "hinzusehen gleichzeitig 5 Shirts",
    gesucht="Wahrscheinlichkeit, dass alle 5 gegriffenen Shirts rot sind",
    verfahren="Ziehen ohne Zurücklegen, fünfstufig: P = 6/24 · 5/23 · 4/22 · 3/21 · 2/20", schritte="1",
    zahlenraum="Bruch",
    ergebnis="P = 1/7084 ≈ 0,00014", niveau_geschaetzt="III",
    fehlerquelle="mit Zurücklegen rechnen (P = (6/24)^5) statt die Anzahl roter und verbliebener Shirts "
                 "je Stufe zu verringern",
    bemerkung="Die Aufgabe zieht fünf Shirts in einem Griff (fünfstufig ohne Zurücklegen); der "
              "Typ „Wahrscheinlichkeit mehrstufig ohne Zurücklegen“ ist bisher nur für zwei- oder "
              "dreistufige Versuche belegt, das zugrunde liegende Prinzip (je Stufe verkleinerte "
              "Grundmenge) ist aber identisch, daher hier wiederverwendet statt eines neuen Typs.")

row(id="2020-GYM-K6c", block="Kontext", aufgabe="6", titel="Handballtraining", teilaufgabe="c", seite="8",
    punkte="5", leitidee="Daten und Zufall", thema="Kenngrößen",
    typ="Spannweite berechnen", typ_neben="Modalwert bestimmen|Kreisdiagramm zeichnen",
    stichwoerter="Spannweite|Modalwert|Kreisdiagramm|Trefferzahlen",
    format="Kurzantwort|Kurzantwort|Zeichnen",
    operator="Geben Sie an|Geben Sie an|Stellen Sie dar", antwort="Zahl|Zahl|Grafik",
    material="Tabelle",
    skizze="Kreisdiagramm mit den Anteilen der Spieler nach Trefferzahl (1 bis 5 Treffer)",
    kontext="Freizeit/Sport", textumfang="mittel",
    gegeben="Trefferzahlen von 10 Spielern beim 7-Meter-Werfen (je 5 Würfe): 3; 5; 4; 3; 3; 5; 1; 2; 4; 3",
    gesucht="Spannweite, Modalwert mit Interpretation, Kreisdiagramm der Trefferzahlen",
    verfahren="Spannweite = Maximum − Minimum = 5 − 1; Modalwert = häufigster Wert der Liste; "
              "Kreisdiagramm: je Trefferzahl Anzahl der Spieler zu 360° ins Verhältnis setzen (1 Treffer: "
              "1 Spieler → 36°, 2 Treffer: 1 Spieler → 36°, 3 Treffer: 4 Spieler → 144°, 4 Treffer: "
              "2 Spieler → 72°, 5 Treffer: 2 Spieler → 72°)",
    schritte="3", zahlenraum="ganz",
    ergebnis="Spannweite = 4; Modalwert = 3 Treffer (4 von 10 Spielern trafen dreimal, am häufigsten); "
             "Kreisdiagramm mit Sektoren 36°/36°/144°/72°/72° für 1/2/3/4/5 Treffer",
    niveau_geschaetzt="II",
    fehlerquelle="beim Kreisdiagramm die Trefferzahlen selbst statt der Häufigkeiten je Trefferzahl "
                 "verwenden")
# Feldkorrektur an vorhandenen Typen: typ -> {feld: neuer Wert}; siehe Kopf.
TYPEN_KORREKTUR = {
    "Behauptung prüfen": {
        "leitidee": "Daten und Zufall",
        "thema": "Wahrscheinlichkeit mehrstufig",
        "definition": ("Eine vorgegebene Aussage rechnerisch oder argumentativ als wahr oder falsch "
                       "nachweisen; leitideenübergreifend, tritt nur als typ_neben auf. Leitidee und "
                       "Thema nach der ersten Fundstelle 2025-OS-K3b (zugeordnet 17.09.2026, Kern § 6: "
                       "jeder Typ trägt leitidee und thema); die Zeilen behalten ihr eigenes Thema."),
    },
}
# ======================================================== AB HIER UNVERÄNDERT
KAT = {"Basis": "msa-katalog-basis.csv", "Kontext": "msa-katalog-kontext.csv"}
GYM_DATEI = "msa-katalog-gym.csv"  # papier GYM: beide Blöcke in einer Datei, Feld block trennt sie
TYP = "msa-typen.csv"
PROFIL = "msa.md"
KERN = "../katalog-prompt.md"  # Umbau 2026-09-19: liegt in der Repo-Wurzel
TYP_HEAD = ["typ", "leitidee", "thema", "definition", "beispiel_id", "status"]
STATUS = {"gültig", "neu"}
PAPIER = re.compile(r"\d{4}-(OS|EBR|FOR|MUSTER-EBR|MUSTER-FOR|GYM)-[BK]\d+[a-z]?")
# Stämme, die eine ASCII-Umschrift von ä, ö, ü oder ß verraten (wie fhr-bau.py).
UMSCHRIFT = ("flaeche", "laenge", "naechst", "haeufig", "zufaell", "waehl", "aender", "aeusser",
 "gefaess", "verhaeltnis", "erklaer", "zaehl", "traeg", "gaeng", "maessig", "hoehe", "groesse",
 "groess", "loesung", "loes", "moegl", "koerper", "oeffn", "schoen", "pruef", "stueck", "gewuerz",
 "kruemmung", "ueber", "fuer", "muess", "fuehr", "gueltig", "zurueck", "huelle", "schluessel",
 "urspruengl", "gross", "massstab", "masszahl", "schliess", "heisst", "weiss", "strasse",
 "gemaess", "fuss")
PFLICHT = ("id jahr papier block aufgabe teilaufgabe seite punkte hilfsmittel leitidee thema typ format "
           "operator antwort material skizze kontext textumfang gegeben gesucht verfahren schritte "
           "ergebnis niveau_geschaetzt fehlerquelle").split()


def lies(pfad):
    if not os.path.exists(pfad):
        sys.exit(f"{pfad} fehlt – Datei neben das Skript legen.")
    return io.open(pfad, encoding="utf-8").read()


def liste_aus_klammer(text, feld):
    """'feld (a; b c; d)' -> {'a','b','d'} – erstes Wort je Teil (Kern § 5)."""
    m = re.search(r"\b" + re.escape(feld) + r" \(([^()]*)\)", text)
    if not m:
        sys.exit(f"{KERN}: Werteliste für {feld} nicht gefunden.")
    return {t.strip().split()[0] for t in m.group(1).split(";") if t.strip()}


def vokabular():
    """Kopfzeile und Formvokabular aus dem Kern, Leitideen und Themen aus msa.md § 5–6."""
    kern, profil = lies(KERN), lies(PROFIL)
    m = re.search(r"^Kopfzeile:\s*\n(id;.+)$", kern, re.M)
    if not m or m.group(1).strip().split(";") != HEAD:
        sys.exit(f"{KERN}: Kopfzeile fehlt oder weicht von HEAD ab.")
    v = {feld: liste_aus_klammer(kern, feld)
         for feld in ("format", "antwort", "material", "zahlenraum", "textumfang", "niveau_geschaetzt")}
    m = re.search(r"^## 5 Leitideen.*?\n\s*\n(.+?)\n", profil, re.S | re.M)
    if not m:
        sys.exit(f"{PROFIL}: Leitideen (§ 5) nicht gefunden.")
    leitideen = [s.strip() for s in m.group(1).split("·") if s.strip()]
    sec = profil.split("## 6 Themenliste", 1)[1].split("\n## ", 1)[0]
    themen = {}
    for l in sec.splitlines():
        m = re.match(r"^([^:]+): (.+)$", l)
        if m and m.group(1).strip() in leitideen:
            themen[m.group(1).strip()] = [s.strip() for s in m.group(2).split("·") if s.strip()]
    fehlt = [l for l in leitideen if l not in themen]
    if fehlt:
        sys.exit(f"{PROFIL}: keine Themenzeile für {fehlt}")
    return v, leitideen, themen


VOK, LEITIDEEN, THEMEN = vokabular()


def lade(pfad, kopf):
    if not os.path.exists(pfad):
        return kopf, []
    with io.open(pfad, encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh, delimiter=";"))
    if not rows:
        return kopf, []
    if rows[0] != kopf:
        sys.exit(f"{pfad}: Kopfzeile weicht ab")
    return rows[0], rows[1:]


def schreibe(pfad, kopf, zeilen):
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as fh:
        w = csv.writer(fh, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(kopf)
        for z in zeilen:
            w.writerow(z)


def pruefe_zeile(z, a, typ_namen, alle_ids, konfig=None):
    """Prüfungen je Katalogzeile nach Kern § 5 und § 7; konfig nur für neue Zeilen."""
    i = z["id"]
    for k in PFLICHT:
        a(z[k].strip() != "", f"{i}: Pflichtfeld leer: {k}")
    a(PAPIER.fullmatch(i) is not None, f"{i}: Kennung folgt nicht dem Muster Jahr-papier-BlockAufgabeTeilaufgabe")
    a(i.startswith(f"{z['jahr']}-{z['papier']}-"), f"{i}: jahr oder papier passt nicht zur Kennung")
    a(z["block"] in KAT, f"{i}: block muss Basis oder Kontext sein")
    a(i.split("-")[-1][0] == ("B" if z["block"] == "Basis" else "K"), f"{i}: Blockkürzel passt nicht zu block")
    a(z["leitidee"] in THEMEN, f"{i}: Leitidee unbekannt: {z['leitidee']}")
    a(z["thema"] in THEMEN.get(z["leitidee"], []), f"{i}: Thema passt nicht zur Leitidee: {z['thema']}")
    a(z["stern"] in ("ja", "nein", ""), f"{i}: stern ungültig")
    a(z["hilfsmittel"] in ("ja", "nein"), f"{i}: hilfsmittel ungültig")
    a(z["afb_amtlich"] == "" or re.fullmatch(r"I{1,3}(\|I{1,3})*", z["afb_amtlich"]), f"{i}: afb_amtlich ungültig")
    for feld in ("textumfang", "niveau_geschaetzt"):
        a(z[feld] in VOK[feld], f"{i}: {feld} ungültig: {z[feld]}")
    for feld in ("format", "antwort", "material", "zahlenraum"):
        for teil in [s for s in z[feld].split("|") if s]:
            a(teil in VOK[feld], f"{i}: {feld} hat unbekannten Wert: {teil}")
    for feld in ("typ", "typ_neben"):
        for t in [s for s in z[feld].split("|") if s]:
            a(t in typ_namen, f"{i}: Typ nicht in {TYP}: {t}")
    for dep in [s for s in z["abhaengig_von"].split("|") if s]:
        a(dep in alle_ids, f"{i}: abhaengig_von zeigt ins Leere: {dep}")
    for k, v in z.items():
        a("?" not in v or k == "bemerkung" or z["bemerkung"].strip() != "",
          f"{i}: Fragezeichen in {k} ohne Grund in bemerkung")
        a(not re.search(r"(?<=[\d\s(])-(?=\d)", v), f"{i}: ASCII-Bindestrich als Minus in {k}")
        a(k in ("stichwoerter",) or not [w for w in UMSCHRIFT if w in v.lower()],
          f"{i}: ASCII-Umschrift in {k}: {v[:40]}")
    if konfig:
        a(z["jahr"] == konfig["jahr"] and z["papier"] == konfig["papier"], f"{i}: Heftkennung falsch")
        grenze = konfig["seiten"][z["block"]] if isinstance(konfig["seiten"], dict) else konfig["seiten"]
        a(int(z["seite"]) <= grenze, f"{i}: Seite größer als der Heftumfang")


def main():
    fehler = []
    def a(cond, msg):
        if not cond:
            fehler.append(msg)

    alt = {b: lade(p, HEAD)[1] for b, p in KAT.items()}
    alt_gym = lade(GYM_DATEI, HEAD)[1]
    _, alt_typ = lade(TYP, TYP_HEAD)
    typ_namen = {r[0] for r in alt_typ} | {t[0] for t in NEUE_TYPEN}

    # Feldkorrektur an der Typenliste (Kopf): nur, was noch nicht so dasteht
    korrigiert = []
    for r in alt_typ:
        if r[0] in TYPEN_KORREKTUR:
            for feld, neu in TYPEN_KORREKTUR[r[0]].items():
                j = TYP_HEAD.index(feld)
                if r[j] != neu:
                    korrigiert.append((r[0], feld, r[j], neu)); r[j] = neu
    fremd = sorted(set(TYPEN_KORREKTUR) - {r[0] for r in alt_typ})
    a(not fremd, f"TYPEN_KORREKTUR nennt unbekannte Typen: {fremd}")

    if not ZEILEN:
        # ------------------------------------------------ Selbstprüfung des Bestands
        alle = [dict(zip(HEAD, r)) for b in KAT for r in alt[b]] + [dict(zip(HEAD, r)) for r in alt_gym]
        alle_ids = [z["id"] for z in alle]
        a(len(set(alle_ids)) == len(alle_ids), "doppelte id im Bestand")
        for b in KAT:
            for r in alt[b]:
                z = dict(zip(HEAD, r))
                a(z["papier"] != "GYM", f"{z['id']}: GYM-Zeile steht in {KAT[b]}, gehört nach {GYM_DATEI}")
                a(z["block"] == b, f"{z['id']}: steht in {KAT[b]}, trägt aber block {z['block']}")
                pruefe_zeile(z, a, typ_namen, set(alle_ids))
        for r in alt_gym:
            z = dict(zip(HEAD, r))
            a(z["papier"] == "GYM", f"{z['id']}: Nicht-GYM-Zeile steht in {GYM_DATEI}")
            a(z["block"] in KAT, f"{z['id']}: block muss Basis oder Kontext sein")
            pruefe_zeile(z, a, typ_namen, set(alle_ids))
        verwendet = {t for z in alle for f in ("typ", "typ_neben") for t in z[f].split("|") if t}
        for r in alt_typ:
            t = dict(zip(TYP_HEAD, r))
            a(t["leitidee"] in THEMEN and t["thema"] in THEMEN.get(t["leitidee"], []),
              f"Typ {t['typ']}: Leitidee oder Thema unbekannt ({t['leitidee']} / {t['thema']})")
            a(t["beispiel_id"] in alle_ids, f"Typ {t['typ']}: beispiel_id nicht im Katalog")
            a(t["typ"] in verwendet, f"Typ {t['typ']}: in keiner Zeile verwendet")
            a(t["status"] in STATUS, f"Typ {t['typ']}: status ungültig: {t['status']}")
            a(len(t["definition"]) > 20, f"Typ {t['typ']}: Definition zu knapp")
        if fehler:
            print(f"Selbstprüfung: {len(fehler)} Fehler:")
            for f_ in fehler:
                print(" -", f_)
            sys.exit(1)
        if korrigiert:
            schreibe(TYP, TYP_HEAD, alt_typ)
            print(f"Feldkorrektur an {TYP} ({len(korrigiert)} Felder):")
            for typ, feld, vorher, nachher in korrigiert:
                print(f"  {typ} · {feld}: {vorher!r} → {nachher!r}")
        n_b, n_k, n_g = len(alt["Basis"]), len(alt["Kontext"]), len(alt_gym)
        hefte = sorted({(z["jahr"], z["papier"]) for z in alle})
        print(f"Selbstprüfung bestanden: {n_b + n_k} Katalogzeilen ({n_b} Basis, {n_k} Kontext) plus "
              f"{n_g} GYM-Zeilen aus {len(hefte)} Heften, {len(alt_typ)} Typen, alle verwendet, jede "
              f"beispiel_id im Katalog. ZEILEN ist leer, "
              f"{'nur die Feldkorrektur geschrieben' if korrigiert else 'nichts geschrieben'}.")
        return

    # ------------------------------------------------------- Heftlauf
    alt_ids = {r[0] for b in KAT for r in alt[b]} | {r[0] for r in alt_gym}
    neue_ids = [z["id"] for z in ZEILEN]
    a(len(set(neue_ids)) == len(neue_ids), "doppelte id in ZEILEN")
    for i in neue_ids:
        a(i not in alt_ids, f"{i}: Kennung steht schon im Katalog")
    for t in NEUE_TYPEN:
        a(t[0] not in {r[0] for r in alt_typ}, f"Typ {t[0]}: steht schon in {TYP}")
        a(t[1] in THEMEN and t[2] in THEMEN.get(t[1], []), f"Typ {t[0]}: Leitidee oder Thema unbekannt")
        a(t[4] in neue_ids or t[4] in alt_ids, f"Typ {t[0]}: beispiel_id nicht im Katalog")
        a(len(t[3]) > 20, f"Typ {t[0]}: Definition zu knapp")
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        a(ist == soll, f"Aufgabe {nr}: Punkte {ist}, Soll {soll}")
    a(sum(int(z["punkte"]) for z in ZEILEN) == KONFIG["soll_gesamt"],
      f"Gesamtpunktzahl weicht von {KONFIG['soll_gesamt']} ab")
    verwendet = set()
    for z in ZEILEN:
        pruefe_zeile(z, a, typ_namen, alt_ids | set(neue_ids), KONFIG)
        verwendet |= {t for f in ("typ", "typ_neben") for t in z[f].split("|") if t}
    a(not ({t[0] for t in NEUE_TYPEN} - verwendet),
      f"neue Typen unbenutzt: {sorted({t[0] for t in NEUE_TYPEN} - verwendet)}")
    if fehler:
        print(f"ABBRUCH – {len(fehler)} Fehler, nichts geschrieben:")
        for f_ in fehler:
            print(" -", f_)
        sys.exit(1)

    for b, p in KAT.items():
        neu = [[z[k] for k in HEAD] for z in ZEILEN if z["block"] == b and z["papier"] != "GYM"]
        if neu:
            schreibe(p, HEAD, alt[b] + neu)
    neu_gym = [[z[k] for k in HEAD] for z in ZEILEN if z["papier"] == "GYM"]
    if neu_gym:
        schreibe(GYM_DATEI, HEAD, alt_gym + neu_gym)
    schreibe(TYP, TYP_HEAD, alt_typ + [[t[0], t[1], t[2], t[3], t[4], "neu"] for t in NEUE_TYPEN])

    # Rückweg: geschriebene Dateien mit echtem Leser einlesen und vergleichen
    DATEIEN_GESCHRIEBEN = [(p, [z for z in ZEILEN if z["block"] == b and z["papier"] != "GYM"], alt[b])
                            for b, p in KAT.items()] + [(GYM_DATEI, [z for z in ZEILEN if z["papier"] == "GYM"], alt_gym)]
    for p, zeilen_p, alt_p in DATEIEN_GESCHRIEBEN:
        if not zeilen_p:
            continue
        _, zurueck = lade(p, HEAD)
        for gel, z in zip(zurueck[len(alt_p):], zeilen_p):
            if len(gel) != 37 or any(v != z[k] for k, v in zip(HEAD, gel)):
                sys.exit(f"{z['id']}: Rückweg verändert die Zeile")
        roh = io.open(p, encoding="utf-8", newline="").read()
        if "\r" in roh or not all(l.startswith('"') and l.endswith('"') for l in roh.splitlines()):
            sys.exit(f"{p}: Ausgabe nicht vollständig gequotet oder CRLF")

    print(f"Heft {KONFIG['jahr']} {KONFIG['papier']} – {len(ZEILEN)} Zeilen, {len(NEUE_TYPEN)} Typen neu\n")
    print(f"{'id':<16} {'P':>2}  {'thema':<38} {'typ':<44} ergebnis")
    for z in ZEILEN:
        print(f"{z['id']:<16} {z['punkte']:>2}  {z['thema']:<38} {z['typ']:<44} {z['ergebnis'][:60]}")
    print()
    for nr, soll in KONFIG["soll"].items():
        ist = sum(int(z["punkte"]) for z in ZEILEN if z["aufgabe"] == nr)
        print(f"Aufgabe {nr}: Ist {ist} / Soll {soll}")
    print(f"Gesamt: {sum(int(z['punkte']) for z in ZEILEN)} / {KONFIG['soll_gesamt']}")
    unsicher = [z["id"] for z in ZEILEN if any("?" in v for v in z.values())]
    print("Unsichere Zeilen:", ", ".join(unsicher) if unsicher else "keine")
    print("Alle Prüfungen bestanden.")


if __name__ == "__main__":
    main()
