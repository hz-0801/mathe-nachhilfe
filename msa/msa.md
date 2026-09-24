# PROFIL MSA – Prüfung am Ende der Jahrgangsstufe 10, Mathematik, Brandenburg
Version 0.9 · 24.09.2026 · Kennung msa · gilt mit Kern v0.9 (Schema-Version 2, unverändert seit Kern v0.3)
Änderungen gegenüber 0.8 (Auftrag Abgleichlauf GYM, 24.09.2026): § 4 Satz zum Abgleichlauf (61 GYM-Typen zusammengeführt oder umbenannt, Typenzahl 293 → 264); § 6 Themenliste „Sinussatz" → „Sinus- und Kosinussatz" (fünf GYM-Zeilen prüfen den Kosinussatz). werkzeuge/typen-abgleich.py neu, liest das mit.
Änderungen gegenüber 0.7 (Auftrag Gymnasialhefte, Entscheidung 18 neu gefasst): § 1 Absatz Gymnasium (Bestand um GYM 2014–2025 erweitert, Grund die zentrale Klassenarbeit ab 2025/26); § 3 Aufbau der Gymnasialhefte (am Heft geprüft: 2014 und 2019); § 4 papier GYM, id-Beispiele, block-Ausnahme (eigene Katalogdatei msa-katalog-gym.csv), hilfsmittel- und seite-Ausnahmen. msa-bau.py v0.3 liest das mit.
Änderungen gegenüber 0.6 (Auftrag O, Punkt 2): § 2 verweist auf die angelegte msa-quellen.md (Quelle, Jahresseite, Verzeichnis der Hefte mit papier-Kürzel, lokaler Heftordner hefte/msa/ mit Erfassungsstand; Zahlen aus befund-quellenbestand-2026-09-18.md).
Änderungen gegenüber 0.5 (Auftrag G, Punkt 4): § 6 Zeilenthema – die eigene Regel „Thema der Aufgabenstellung" ist entschieden, nicht mehr offen (konzept.md Entscheidung 26); Kernbindung entsprechend.
Änderungen gegenüber 0.4 (Auftrag F, Punkt 1 und 5): Die Dateien dieses Profils tragen das Präfix msa- wie die der anderen Profile – typen.csv → msa-typen.csv, katalog-basis.csv → msa-katalog-basis.csv, katalog-kontext.csv → msa-katalog-kontext.csv, pruefungen.md → msa-pruefungen.md, vorgaben.md → msa-vorgaben.md (Variante B nach namensschema.md § 4; Inhalt unverändert, Historie per git mv erhalten). Verweise in der Kernbindung, § 1, § 2, § 4 und § 7 nachgezogen; § 2 nennt die Katalogdateien in einer Zeile; msa-bau.py v0.2 liest die neuen Namen. Kernbindung v0.9 (Kern § 1 nennt die neuen Namen). Punkt 5: Kern § 6 setzt Zeilenthema = Typthema mit Vorbehalt für das Profil – § 6 nennt die eigene Regel dieses Profils (Thema der Aufgabenstellung; 42 von 393 Zeilen weichen ab); Kern § 5 macht die Eichung zur Kennzahl nur bei amtlichen Anforderungsbereichen – hier entfällt sie, bis Zeilen mit afb_amtlich erfasst sind (Kernbindung).
Änderungen gegenüber 0.3 (Auftrag E, Punkt 1 und 2): § 2 Umgebungsangabe „Sandbox" gestrichen; § 6 Probelauf als abgeschlossen benannt; § 4 Koordinatenschreibweise mit „|" festgehalten (Vorschlag aus fhr.md § 9 hierher verschoben); Kernbindung von v0.3 auf v0.8 gehoben (Durchsicht unten). Punkt 6: msa-bau.py v0.1 angelegt (§ 2), Typ „Behauptung prüfen" mit Leitidee und Thema seiner ersten Fundstelle.

Kernbindung (17.09.2026, Auftrag E, Punkt 2; 0.9 nach Auftrag F, Punkt 1): Die Kernänderungen 0.4 bis 0.9
sind für dieses Profil durchgesehen, keine widerspricht ihm. Ausgelagertes
Vokabular (0.4) ist erlaubt, nicht verlangt – dieses Profil führt seines in
§ 5–6. Die Handlung je format (0.4, § 5) bündelt Zeilen für den Schnitt der
Profile abi und iqb und bindet dieses Profil nicht. Die Markierungen „Dublette
von:", die Vormerkung und „Abgewandelt von:" (0.5, § 5) setzen eine mit einem
anderen Katalog geteilte Typenliste voraus, die es hier nicht gibt; die
Trägerbindung gilt für abi und iqb. Vorrang des Amtlichen und Maßstab der
Schätzung (0.6, 0.7, § 5) gelten auch hier: ein amtlicher Anforderungsbereich liegt nur bei den Musteraufgaben 2028 vor (§ 4); wird er erfasst, steht er in afb_amtlich, die eigene Schätzung entsteht vorher und wird nicht angepasst, die Eichung ist dann Kennzahl (Kern § 5, 0.9: Kennzahl in Profilen mit amtlichen Anforderungsbereichen); solange keine Zeile afb_amtlich trägt, entfällt sie – heute bei allen Heften Schätzung ohne Maßstab. Zeilenthema (0.9, § 6): der Kern setzt Zeilenthema = Typthema als Regel mit dem Vorbehalt, dass ein Profil eine eigene festlegt; dieses Profil legt seine eigene fest (§ 6: Thema der Aufgabenstellung, so seit der Erfassung 2026-09-05 unter Kern v0.3; 42 von 393 Zeilen weichen vom Thema ihres Typs ab, Stand 17.09.2026). msa behält die eigene Regel (entschieden am 17.09.2026, Auftrag G; konzept.md Entscheidung 26); msa-bau.py prüft die Gleichheit deshalb nicht.

## 1 Prüfung

Zentrale schriftliche Prüfung für Oberschulen und Gesamtschulen im Land Brandenburg, Fach Mathematik, zwei Niveaus: EBR (erweiterte Berufsbildungsreife) und FOR (Fachoberschulreife, entspricht dem MSA). Sagt der Lehrer MSA, meint er FOR. Bestand: die Hefte 2014–2026 und die Musteraufgaben 2028 laut msa-pruefungen.md.

Gymnasium: Bis 2025 schrieb auch das Gymnasium eine P10 in Mathematik, mit eigenen Gymnasialheften (gleicher Termin, andere Aufgaben als OS/EBR/FOR). Seit 2025/26 entfällt die P10 am Gymnasium; an ihre Stelle tritt eine zentrale Klassenarbeit in Klasse 10 (90 Minuten, 35 BE, davon 10 BE hilfsmittelfrei; msa-vorgaben.md § 2, Fachbrief 10). Die 19 Gymnasialhefte 2014–2025 sind seit dem 23.09.2026 Bestand unter dem eigenen papier-Kürzel GYM (§ 4), mit eigener Katalogdatei msa-katalog-gym.csv, aber derselben Themen- und Typenliste wie OS/EBR/FOR (konzept.md Entscheidung 18). Die zentrale Klassenarbeit selbst ist kein GYM-Heft und noch nicht erfasst: neues Format, eigenes Kürzel erst bei Bedarf (Entscheidung 18, Kippbedingung).

## 2 Ablage und Quellen

Basis-URL der Katalogdateien: https://raw.githubusercontent.com/hz-0801/mathe-nachhilfe/main/ (alle Dateien liegen flach im Wurzelverzeichnis; bei anderer Ablage nur diese Zeile ändern).
Katalogdateien dieses Profils: msa-pruefungen.md (Heftliste), msa-typen.csv (Typenliste), msa-katalog-basis.csv und msa-katalog-kontext.csv (Katalog, § 4); bis zum 17.09.2026 ohne Präfix (typen.csv, katalog-basis.csv, katalog-kontext.csv, pruefungen.md, vorgaben.md).
Hefte: Adresse und Dateinamen stehen in msa-pruefungen.md; sie werden mit curl vom Bildungsserver (bildungsserver.berlin-brandenburg.de) geholt. Quellenverzeichnis mit Jahresseite, Serverdateien je papier-Kürzel, den Dateien ohne Katalogeintrag (2026 EBR, Gymnasialhefte) und dem lokalen Heftordner hefte/msa/ samt Erfassungsstand: msa-quellen.md (seit 18.09.2026, Auftrag O Punkt 2).
Amtliche Lösungen gibt es nur für die Musteraufgaben 2028 (Fachbrief Mathematik Nr. 10, Erwartungshorizont mit Bewertungseinheiten, Anforderungsbereich, Standardbezug). Für alle Hefte sind die Ergebnisse eigene Rechnung.
Amtliche Vorgaben und Formatwechsel stehen in msa-vorgaben.md; für die Erfassung reicht dieses Profil.
Gerüst für Erfassung und Prüfung: msa-bau.py (seit 17.09.2026, Auftrag E Punkt 6; der Bestand 2014–2026 wurde davor ohne Skript erfasst). Es liest Kopfzeile und Formvokabular aus katalog-prompt.md § 5, Leitideen und Themenliste aus § 5 und § 6 dieser Datei, schreibt msa-katalog-basis.csv, msa-katalog-kontext.csv und msa-typen.csv nur, wenn alle Prüfungen bestehen, und prüft bei leerem ZEILEN den Bestand (Selbstprüfung). Feldkorrekturen an msa-typen.csv laufen über TYPEN_KORREKTUR im Skript, nicht von Hand.

## 3 Aufbau der Hefte

Integriertes Heft 2014–2025 (papier OS): 135 Minuten (2021–2023: 165); 60 Bewertungseinheiten. Aufgabe 1 „Basisaufgaben" mit 10 Punkten, neun bis zehn Buchstaben à 1–2 Punkte, überwiegend Ankreuzen und Kurzantwort, oft mit kleiner Abbildung. Danach sechs Kontextaufgaben mit Titel („Zahlenscheiben", „Rampe", „Kita") à 6–11 Punkte, jede mit Aufgabenstamm und Buchstaben. Jede Einheit trägt ihre Punkte als „(n P)". Ein Sternchen vor dem Buchstaben („*c)") kennzeichnet Einheiten, die nur FOR-Schüler lösen müssen; EBR-Schüler lösen die Aufgaben ohne Stern (40 BE). Taschenrechner, Formelsammlung und beiliegendes Formelblatt sind durchgehend erlaubt. Keine Wahlaufgaben, keine Anforderungsbereiche im Heft.
Getrennte Hefte ab 2026 (papier EBR, FOR): gleicher Aufbau, keine Sternchen; EBR 40 BE, FOR 60 BE, je 135 Minuten.
Musteraufgaben 2028 (papier MUSTER-EBR, MUSTER-FOR): neues Format mit hilfsmittelfreiem Teil (10 BE) und Aufgaben mit Hilfsmitteln, je 50 BE; mit Erwartungshorizont.

Gymnasialhefte (papier GYM), am Heft geprüft (2014 und 2019 gelesen, nicht angenommen): 135 Minuten, 50 Bewertungseinheiten, fünf Aufgaben – Aufgabe 1 „Basisaufgaben" mit 10 Punkten (neun bis zehn Buchstaben à 1 P, vereinzelt 2 P; Ankreuzen und Kurzantwort, häufig mit kleiner Abbildung, kein Sternchen-System), danach vier Kontextaufgaben mit Titel à 8–12 Punkte, jede mit Aufgabenstamm und Buchstaben, Punkte als „(n P)"; kein EBR/FOR-Unterschied, keine Wahlaufgaben, keine Anforderungsbereiche im Heft. 2014–2018 ein Heft (Taschenrechner, Formelsammlung, Kurvenschablonen, Zeichengeräte und Duden durchgehend erlaubt). Ab 2019 zwei Dateien: Teil 1 „hilfsmittelfreier Teil" (nur Aufgabe 1, 25 der 135 Minuten, ohne jedes Hilfsmittel, eigene Seitenzählung 1–3) und Teil 2 „Aufgaben 2 bis 5" (mit Taschenrechner, Formelsammlung, Kurvenschablonen, Zeichengeräten, Wörterbuch; eigene Seitenzählung 1–9, unabhängig von Teil 1). Keine amtlichen Lösungen, wie bei OS/EBR/FOR.

## 4 Kürzel und Werte

Abgleichlauf 2026-09-24 (Gegenlese des Lehrers nach der GYM-Erfassung, Kern § 9): 61 der 108 neuen GYM-Typen über werkzeuge/typen-abgleich.py und msa/gym-abgleich.csv vereinheitlicht (29 zu vorhandenen Typen zusammengezogen, 32 umbenannt), Typenzahl 293 → 264; Log in msa/gym-abgleich-log.md.

papier: OS | EBR | FOR | MUSTER-EBR | MUSTER-FOR | GYM
block: Basis (Aufgabe 1 „Basisaufgaben"; ab 2028 bzw. bei GYM ab 2019 der hilfsmittelfreie Teil) → msa-katalog-basis.csv; Kontext (alle übrigen Aufgaben) → msa-katalog-kontext.csv. Ausnahme papier GYM: beide Blöcke in einer Datei, msa-katalog-gym.csv (Feld block trennt sie), damit die übrigen Kataloge und alles, was sie liest, unverändert bleiben.
id: Jahr-papier-BlockkürzelAufgabeTeilaufgabe mit Blockkürzel B oder K: 2025-OS-B1a, 2025-OS-K3b, 2026-FOR-K4c, 2028-MUSTER-FOR-B1a, 2019-GYM-B1a, 2019-GYM-K2a
stern: ja/nein in OS-Heften; in allen anderen Heften leer (auch GYM: kein Sternchen-System)
hilfsmittel: ja; nein im hilfsmittelfreien Teil der Musteraufgaben 2028 und im hilfsmittelfreien Teil (Block Basis) der Gymnasialhefte ab 2019 (2014–2018 durchgehend ja, § 3)
afb_amtlich: nur bei Musteraufgaben 2028 aus dem Erwartungshorizont; sonst leer (auch GYM: keine amtlichen Lösungen)
seite: Seite im PDF des Hefts; bei Musteraufgaben Seite im Fachbrief 10; bei GYM ab 2019 die Seite in der jeweiligen Teildatei (eigene Fußzeile „Seite N von M" je Teil, § 3)
Koordinaten: in diesem Profil wie im Heft mit „|" (A(−2|6)). Das Zeichen trennt sonst Mehrfachwerte in einem Feld (Kern § 5); fhr und iqb schreiben deshalb P(x; y). Eine Umstellung der msa-Zeilen ist offen (Vorschlag aus fhr.md, 13.09.2026); bis dahin darf ein Skript Koordinatenfelder dieses Profils nicht an „|" trennen.

## 5 Leitideen (Rahmenlehrplan 1–10 Berlin-Brandenburg)

Zahlen und Operationen · Größen und Messen · Raum und Form · Gleichungen und Funktionen · Daten und Zufall

## 6 Themenliste

Feste Ebene zwischen Leitidee und Typ. Stand seit dem Probelauf (die ersten drei Hefte 2025, 2026 FOR und 2024, 05.09.2026, konzept.md § 7) unverändert und mit allen zwölf Heften bestätigt; Ergänzungen nur über den Bericht. Zeilenthema: in diesem Profil trägt die Zeile das Thema der Aufgabenstellung, auch wenn ihr Typ in msa-typen.csv unter einem anderen Thema steht – eigene Regel nach Kern § 6, entschieden am 17.09.2026 (Auftrag G; konzept.md Entscheidung 26): msa behält sie, die Kernregel Zeilenthema = Typthema wird nicht übernommen. 42 von 393 Zeilen weichen vom Thema ihres Typs ab; die Regel kippt bei einem Leser, der das Zeilenthema profilübergreifend auswertet.

Zahlen und Operationen: Rationale Zahlen rechnen · Brüche und Dezimalzahlen · Prozentrechnung · Zinsrechnung · Zehnerpotenzen und Näherungswerte · Potenzen und Wurzeln · Terme umformen · Runden und Überschlag
Größen und Messen: Einheiten umrechnen · Flächeninhalt und Umfang · Volumen und Oberfläche · Satz des Pythagoras · Trigonometrie im rechtwinkligen Dreieck · Sinus- und Kosinussatz · Maßstab
Raum und Form: Ebene Figuren und Winkel · Körper, Netze, Schrägbilder · Symmetrie und Abbildungen · Ähnlichkeit und Strahlensätze · Kongruenz und Konstruktion · Koordinaten und Zeichnen
Gleichungen und Funktionen: Lineare Gleichungen · Lineare Gleichungssysteme · Quadratische Gleichungen · Zuordnungen proportional und antiproportional · Lineare Funktionen · Quadratische Funktionen · Exponentialfunktionen und Wachstum · Trigonometrische Funktionen · Funktionen allgemein
Daten und Zufall: Daten darstellen · Kenngrößen · Diagramme lesen und beurteilen · Wahrscheinlichkeit einstufig · Wahrscheinlichkeit mehrstufig · Zählen und Kombinatorik

## 7 Besonderheiten beim Erfassen

- Basisaufgaben tragen oft kleine Abbildungen (Figur, Netz, Graph, Ankreuzfelder); die Textextraktion verliert dort Buchstaben und mischt Ziffern aus Abbildungen in den Text. Deshalb jede Seite rendern; bei Widerspruch gilt das Bild.
- Versteckte Leistungen: Nach der Rechnung folgt ohne Buchstaben „X behauptet … Entscheiden Sie … Begründen Sie" (2025, Aufgabe 3b). Eine Zeile, beide Leistungen erfasst, Punkte ungeteilt.
- Ankreuz-Basisaufgaben: ergebnis nennt die richtige Option in ihrem Wortlaut, nicht ihre Position.
- Zeichenaufgaben im Koordinatensystem: skizze nennt Achsenbereiche und Gitter; ergebnis die kennzeichnenden Punkte.
- Fehlende Inhalte 2021–2023 sind Vorgabe, kein Trend (msa-vorgaben.md). Beim Erfassen ohne Bedeutung.
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
