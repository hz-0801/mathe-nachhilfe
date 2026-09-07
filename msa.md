# PROFIL MSA – Prüfung am Ende der Jahrgangsstufe 10, Mathematik, Brandenburg
Version 0.3 · 05.09.2026 · Kennung msa · gilt mit Kern v0.3

## 1 Prüfung

Zentrale schriftliche Prüfung für Oberschulen und Gesamtschulen im Land Brandenburg, Fach Mathematik, zwei Niveaus: EBR (erweiterte Berufsbildungsreife) und FOR (Fachoberschulreife, entspricht dem MSA). Sagt der Lehrer MSA, meint er FOR. Bestand: die Hefte 2014–2026 und die Musteraufgaben 2028 laut pruefungen.md. Gymnasialhefte gehören nicht dazu.

## 2 Ablage und Quellen

Basis-URL der Katalogdateien: https://raw.githubusercontent.com/hz-0801/mathe-nachhilfe/main/ (alle Dateien liegen flach im Wurzelverzeichnis; bei anderer Ablage nur diese Zeile ändern).
Hefte: Adresse und Dateinamen stehen in pruefungen.md; die Domain bildungsserver.berlin-brandenburg.de ist aus der Sandbox erreichbar, Hefte werden mit curl geholt.
Amtliche Lösungen gibt es nur für die Musteraufgaben 2028 (Fachbrief Mathematik Nr. 10, Erwartungshorizont mit Bewertungseinheiten, Anforderungsbereich, Standardbezug). Für alle Hefte sind die Ergebnisse eigene Rechnung.
Amtliche Vorgaben und Formatwechsel stehen in vorgaben.md; für die Erfassung reicht dieses Profil.

## 3 Aufbau der Hefte

Integriertes Heft 2014–2025 (papier OS): 135 Minuten (2021–2023: 165); 60 Bewertungseinheiten. Aufgabe 1 „Basisaufgaben" mit 10 Punkten, neun bis zehn Buchstaben à 1–2 Punkte, überwiegend Ankreuzen und Kurzantwort, oft mit kleiner Abbildung. Danach sechs Kontextaufgaben mit Titel („Zahlenscheiben", „Rampe", „Kita") à 6–11 Punkte, jede mit Aufgabenstamm und Buchstaben. Jede Einheit trägt ihre Punkte als „(n P)". Ein Sternchen vor dem Buchstaben („*c)") kennzeichnet Einheiten, die nur FOR-Schüler lösen müssen; EBR-Schüler lösen die Aufgaben ohne Stern (40 BE). Taschenrechner, Formelsammlung und beiliegendes Formelblatt sind durchgehend erlaubt. Keine Wahlaufgaben, keine Anforderungsbereiche im Heft.
Getrennte Hefte ab 2026 (papier EBR, FOR): gleicher Aufbau, keine Sternchen; EBR 40 BE, FOR 60 BE, je 135 Minuten.
Musteraufgaben 2028 (papier MUSTER-EBR, MUSTER-FOR): neues Format mit hilfsmittelfreiem Teil (10 BE) und Aufgaben mit Hilfsmitteln, je 50 BE; mit Erwartungshorizont.

## 4 Kürzel und Werte

papier: OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR
block: Basis (Aufgabe 1 „Basisaufgaben"; ab 2028 der hilfsmittelfreie Teil) → katalog-basis.csv; Kontext (alle übrigen Aufgaben) → katalog-kontext.csv
id: Jahr-papier-BlockkürzelAufgabeTeilaufgabe mit Blockkürzel B oder K: 2025-OS-B1a, 2025-OS-K3b, 2026-FOR-K4c, 2028-MUSTER-FOR-B1a
stern: ja/nein in OS-Heften; in allen anderen Heften leer
hilfsmittel: ja; nein nur im hilfsmittelfreien Teil der Musteraufgaben 2028
afb_amtlich: nur bei Musteraufgaben 2028 aus dem Erwartungshorizont; sonst leer
seite: Seite im PDF des Hefts; bei Musteraufgaben Seite im Fachbrief 10

## 5 Leitideen (Rahmenlehrplan 1–10 Berlin-Brandenburg)

Zahlen und Operationen · Größen und Messen · Raum und Form · Gleichungen und Funktionen · Daten und Zufall

## 6 Themenliste

Feste Ebene zwischen Leitidee und Typ. Stand v0.2, im Probelauf zu prüfen; Ergänzungen nur über den Bericht.

Zahlen und Operationen: Rationale Zahlen rechnen · Brüche und Dezimalzahlen · Prozentrechnung · Zinsrechnung · Zehnerpotenzen und Näherungswerte · Potenzen und Wurzeln · Terme umformen · Runden und Überschlag
Größen und Messen: Einheiten umrechnen · Flächeninhalt und Umfang · Volumen und Oberfläche · Satz des Pythagoras · Trigonometrie im rechtwinkligen Dreieck · Sinussatz · Maßstab
Raum und Form: Ebene Figuren und Winkel · Körper, Netze, Schrägbilder · Symmetrie und Abbildungen · Ähnlichkeit und Strahlensätze · Kongruenz und Konstruktion · Koordinaten und Zeichnen
Gleichungen und Funktionen: Lineare Gleichungen · Lineare Gleichungssysteme · Quadratische Gleichungen · Zuordnungen proportional und antiproportional · Lineare Funktionen · Quadratische Funktionen · Exponentialfunktionen und Wachstum · Trigonometrische Funktionen · Funktionen allgemein
Daten und Zufall: Daten darstellen · Kenngrößen · Diagramme lesen und beurteilen · Wahrscheinlichkeit einstufig · Wahrscheinlichkeit mehrstufig · Zählen und Kombinatorik

## 7 Besonderheiten beim Erfassen

- Basisaufgaben tragen oft kleine Abbildungen (Figur, Netz, Graph, Ankreuzfelder); die Textextraktion verliert dort Buchstaben und mischt Ziffern aus Abbildungen in den Text. Deshalb jede Seite rendern; bei Widerspruch gilt das Bild.
- Versteckte Leistungen: Nach der Rechnung folgt ohne Buchstaben „X behauptet … Entscheiden Sie … Begründen Sie" (2025, Aufgabe 3b). Eine Zeile, beide Leistungen erfasst, Punkte ungeteilt.
- Ankreuz-Basisaufgaben: ergebnis nennt die richtige Option in ihrem Wortlaut, nicht ihre Position.
- Zeichenaufgaben im Koordinatensystem: skizze nennt Achsenbereiche und Gitter; ergebnis die kennzeichnenden Punkte.
- Fehlende Inhalte 2021–2023 sind Vorgabe, kein Trend (vorgaben.md). Beim Erfassen ohne Bedeutung.
- Musteraufgaben 2028: ergebnis und afb_amtlich aus dem Erwartungshorizont, ergebnis mit Zusatz „amtlich"; eigene Rechnung als Kontrolle.

## 8 Beispielzeilen

Vier Zeilen aus dem Heft 2025, zur Lesbarkeit als Feld = Wert; in den CSV-Dateien stehen dieselben Werte als eine Zeile in der Reihenfolge der Kopfzeile.

    id = 2025-OS-B1a · jahr = 2025 · papier = OS · block = Basis · aufgabe = 1 · titel = Basisaufgaben · teilaufgabe = a · seite = 2
    punkte = 1 · stern = nein · hilfsmittel = ja · afb_amtlich =
    leitidee = Zahlen und Operationen · thema = Prozentrechnung · typ = Grundwert berechnen · typ_neben = · stichwoerter = Prozent|Rabatt|Grundwert · voraussetzungen =
    format = Kurzantwort · operator = Geben Sie an · antwort = Zahl
    material = keins · skizze = keine · kontext = Einkauf/Rabatt · textumfang = kurz
    gegeben = Rabatt 6 €, das sind 20 % des alten Preises · gesucht = alter Preis · verfahren = 6 € entsprechen 20 %, also 1 % = 0,30 €, 100 % = 30 € · schritte = 1 · zahlenraum = ganz|Prozent · einheiten = € · abhaengig_von =
    ergebnis = 30 € · zwischenergebnis =
    niveau_geschaetzt = I · fehlerquelle = 20 % von 6 € statt Grundwert rechnen · bemerkung =

    id = 2025-OS-B1b · jahr = 2025 · papier = OS · block = Basis · aufgabe = 1 · titel = Basisaufgaben · teilaufgabe = b · seite = 2
    punkte = 1 · stern = nein · hilfsmittel = ja · afb_amtlich =
    leitidee = Größen und Messen · thema = Einheiten umrechnen · typ = Zeiteinheiten umrechnen · typ_neben = · stichwoerter = Stunden|Minuten|Dezimalzeit · voraussetzungen =
    format = Kurzantwort · operator = Geben Sie an · antwort = Zahl
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = 1,5 h · gesucht = Angabe in Minuten · verfahren = 1,5 · 60 · schritte = 1 · zahlenraum = dezimal · einheiten = h|min · abhaengig_von =
    ergebnis = 90 min · zwischenergebnis =
    niveau_geschaetzt = I · fehlerquelle = 1,5 h als 1 h 50 min lesen · bemerkung =

    id = 2025-OS-K3b · jahr = 2025 · papier = OS · block = Kontext · aufgabe = 3 · titel = Zahlenscheiben · teilaufgabe = b · seite = 6
    punkte = 3 · stern = nein · hilfsmittel = ja · afb_amtlich =
    leitidee = Daten und Zufall · thema = Wahrscheinlichkeit mehrstufig · typ = Wahrscheinlichkeit zweistufig unabhängig · typ_neben = Behauptung prüfen · stichwoerter = Glücksrad|Pfadregel|Laplace|Behauptung · voraussetzungen = Brüche multiplizieren
    format = Rechnung|Begründung · operator = Berechnen Sie|Entscheiden Sie|Begründen Sie · antwort = Zahl|Text
    material = Figur · skizze = zwei Kreisscheiben nebeneinander, je vier gleich große Sektoren durch zwei Durchmesser, über jeder ein Pfeil von oben; linke Scheibe im Uhrzeigersinn von oben 1, 2, 1, 3; rechte Scheibe 2, 3, 2, 1 · kontext = Glücksspiel · textumfang = mittel
    gegeben = zwei Scheiben mit je vier gleich großen Sektoren, links 1, 2, 1, 3, rechts 2, 3, 2, 1; beide werden gedreht, gelesen wird erst die linke, dann die rechte Ziffer; Behauptung: P(22) ist gleich P(33) · gesucht = P(33)|Entscheidung zur Behauptung mit Begründung · verfahren = P(3 links) = 1/4, P(3 rechts) = 1/4, Pfadregel multiplizieren; für 22 ist P = 1/4 · 2/4 · schritte = 3 · zahlenraum = Bruch · einheiten = · abhaengig_von =
    ergebnis = P(33) = 1/16|Behauptung falsch, da P(22) = 1/8 · zwischenergebnis = P(22) = 2/16
    niveau_geschaetzt = II · fehlerquelle = Sektoren zählen statt Anteile bilden (P(3) = 1/3) · bemerkung =

    id = 2025-OS-K5a · jahr = 2025 · papier = OS · block = Kontext · aufgabe = 5 · titel = Funktionen · teilaufgabe = a · seite = 10
    punkte = 4 · stern = nein · hilfsmittel = ja · afb_amtlich =
    leitidee = Gleichungen und Funktionen · thema = Lineare Funktionen · typ = Gerade durch zwei Punkte zeichnen · typ_neben = Eigenschaften eines Graphen beurteilen|Geradengleichung aus zwei Punkten · stichwoerter = lineare Funktion|Monotonie|y-Achsenabschnitt|Gleichung aufstellen · voraussetzungen = Steigung aus zwei Punkten
    format = Zeichnen|Ankreuzen|Kurzantwort · operator = Zeichnen Sie|Entscheiden Sie|Geben Sie an · antwort = Grafik|Kreuz|Term
    material = Koordinatensystem · skizze = Koordinatensystem x von −4 bis 4, y von −2 bis 7, Gitter 1, ohne eingezeichnete Punkte · kontext = ohne · textumfang = mittel
    gegeben = Gerade f durch A(−2|6) und B(3|−1,5); zwei Aussagen zum Ankreuzen: f verläuft monoton steigend; f schneidet die y-Achse in (0|3) · gesucht = Graph von f|wahr/falsch je Aussage|eine Gleichung von f · verfahren = m = (−1,5 − 6)/(3 − (−2)) = −1,5; n aus A: 6 = −1,5 · (−2) + n, n = 3 · schritte = 3 · zahlenraum = negativ|dezimal · einheiten = · abhaengig_von =
    ergebnis = Gerade durch A und B|Aussage 1 falsch, Aussage 2 wahr|f(x) = −1,5x + 3 · zwischenergebnis = m = −1,5
    niveau_geschaetzt = II · fehlerquelle = Vorzeichen der Steigung · bemerkung = drei Leistungen in einer Einheit

Ein „?" hinter einem Wert bedeutet: plausibel, aber nicht am Bild geprüft; der Grund steht dann in bemerkung. In diesen Beispielzeilen kommt es nicht vor.
