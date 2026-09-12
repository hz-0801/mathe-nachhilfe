# PROFIL FHR – Fachhochschulreifeprüfung, Mathematik, Brandenburg
Version 0.9 · 12.09.2026 · Kennung fhr · gilt mit Kern v0.3 (Schema-Version 2)

## 1 Prüfung

Zentrale schriftliche Prüfung zum Erwerb der Fachhochschulreife im Land Brandenburg, Fach Mathematik. Sie gilt für die Bildungsgänge der Fachoberschule, den doppelqualifizierenden Bildungsgang und das Zusatzangebot im Rahmen einer Berufsausbildung; Rechtsgrundlage ist die Fachoberschul- und Fachhochschulreifeverordnung (FOSFHRV), die Aufgaben werden nach § 31 Absatz 1 zentral festgelegt. Sagt der Lehrer FOS, FHR oder Fachhochschulreife, ist dieses Profil gemeint. Nur ein Niveau, keine Wahlaufgaben, keine Anforderungsbereiche im Heft. Bestand: die Hefte 2023–2026 laut fhr-pruefungen.md.

Inhaltliche Grundlage ist der am 01.08.2019 in Kraft getretene Rahmenlehrplan Mathematik für die Fachoberschule, konkretisiert durch die jährlichen Prüfungsschwerpunkte. Der Stoff ist Analysis und Stochastik; Geometrie, Trigonometrie und Gleichungslehre kommen nur als Werkzeug vor.

## 2 Ablage und Quellen

Basis-URL der Katalogdateien: https://raw.githubusercontent.com/hz-0801/mathe-nachhilfe/main/ (alle Dateien flach in der Wurzel; bei anderer Ablage nur diese Zeile ändern).
Katalogdateien dieses Profils: fhr-pruefungen.md, fhr-typen.csv, fhr-katalog.csv.
Hefte: frei zugänglich auf dem Bildungsserver Berlin-Brandenburg unter https://bildungsserver.berlin-brandenburg.de/fileadmin/bbb/unterricht/pruefungen/Fachoberschule_BB/Pruefungsaufgaben/ ; Dateinamen und Zuordnung stehen in fhr-pruefungen.md, geholt wird mit curl. Prüfungsschwerpunkte und Rundschreiben liegen in den Nachbarordnern Pruefungsschwerpunkte/ und Pruefungstermine/. Ein Upload durch den Lehrer ist nicht nötig.
Gerüst für Erfassung und Prüfung: fhr-bau.py (Datensätze, Sollpunkte, Asserts, Ausgabe). Je Heft werden nur die Datensätze und die Sollpunkte ausgetauscht.
Amtliche Lösungen liegen für jedes Heft vor: die Hefte sind „Unterlagen für die Lehrkraft" und enthalten den Erwartungshorizont mit verbindlicher Punkteverteilung. Für dieses Profil gilt Kern § 3 d in der Fassung „amtliche Lösung vorhanden": sie ist maßgeblich, eigene Rechnung ist Kontrolle, ergebnis trägt den Zusatz „amtlich".
Amtliche Vorgaben: die Prüfungsschwerpunkte des jeweiligen Schuljahres und das Rundschreiben des MBJS zu Terminen und Fristen. Sie gehören nach vorgaben.md und werden jährlich geprüft.

## 3 Aufbau der Hefte

Ein Heft ist ein Aufgabenvorschlag für einen Prüfungstermin. Zum Haupttermin stellt das Ministerium zwei gleichwertige Vorschläge bereit; die Lehrkraft wählt einen aus. Für den Nachschreibetermin gibt es einen weiteren Vorschlag, der im Bestand fehlt.

Ein Heft enthält drei voneinander unabhängige, mehrteilige Aufgaben mit Überschrift – zweimal Differential- und Integralrechnung, einmal Stochastik –, laut Prüfungsschwerpunkten sind auch vier möglich, im Bestand kommen nur drei vor. Punkte: 30 + 20 + 20 = 70 (2026: 27 + 23 + 20 = 70). Arbeitszeit 180 Minuten. Jede Aufgabe gliedert sich in Teilaufgaben a) bis h) mit Aufgabenstamm; am Ende jeder Aufgabe steht eine Punktetabelle „Aufgabenteil / Punkte" mit Summe. Praxisbezug ist möglich, in der Analysis meist nicht vorhanden, in der Stochastik in der Regel gegeben.

Drei Seitensorten: Aufgabenseite (Aufgabentext, Punktetabelle), Erwartungshorizont („Teil / Erwartete Teilleistung / Pkt.") und als letzte Seite der Gutachtenbogen. Ausnahme 2023 C: dort fehlt der Gutachtenbogen, die Datei endet nach dem Erwartungshorizont mit „Seite 8 von 9"; die Punkteaufteilung kommt dann aus dem Erwartungshorizont, der ohnehin feiner aufteilt. Der Gutachtenbogen listet jede Teilleistung in Worten mit ihrem BE-Soll und ist die bequemste Quelle für die Punkteaufteilung; er fasst gelegentlich gröber zusammen als der Erwartungshorizont (2026 C, 3a: Gutachten 2 + 2, Erwartungshorizont 1 + 1 + 2).

Zwischenergebnisse sind mitunter als Vorgabe oder als „Zur Kontrolle" in späteren Teilaufgaben genannt, damit ein Quereinstieg möglich ist.

Hilfsmittel durchgehend: Formelsammlung, Nachschlagewerk Rechtschreibung, Taschenrechner ohne Programmierbarkeit, Grafik, numerisches Differenzieren oder Integrieren und ohne automatisches Gleichungslösen. Nichtganzzahlige Ergebnisse werden auf zwei Dezimalstellen gerundet.

Die Aufgabenüberschrift ist nicht die Leitidee. Eine Aufgabe „Integralrechnung" enthält regelmäßig Teilaufgaben der Differentialrechnung (Wertetabelle, Skizze, Funktionsgleichung aus drei Punkten). titel hält die Überschrift, leitidee den Inhalt der Teilaufgabe.

## 4 Kürzel und Werte

papier: A | B | C – der Buchstabe des Aufgabenvorschlags aus dem Dateinamen. Pro Jahrgang liegen zwei Vorschläge zum gleichen Termin vor, die Buchstaben wechseln (2023 A und C, 2024 B und C, 2025 A und C, 2026 B und C). Was die Buchstaben bedeuten, ist nicht belegt (?); sie sind hier nur Kennung und keine Aussage über Haupt- oder Nachschreibetermin – die Prüfungsdaten sind je Jahrgang identisch.
block: leer. Das Heft hat keine Teile, und es gibt keine Basisaufgaben ohne Stamm. Deshalb entfällt die Zweiteilung des Katalogs aus Kern § 1; alle Zeilen gehen in fhr-katalog.csv.
id: Jahr-papier-AufgabeTeilaufgabe, z. B. 2026-C-1a, 2026-C-3e, 2024-B-2d.
jahr: Jahr der Prüfung, nicht des Schuljahres (Heft „26_FOS_Ma_LH_C", Schuljahr 2025/2026, Prüfung 05.06.2026 → 2026).
stern: leer (kein zweites Niveau).
hilfsmittel: ja in allen Zeilen.
afb_amtlich: leer. Erwartungshorizont und Gutachtenbogen weisen nur Punkte aus, keine Anforderungsbereiche.
seite: Seite des Aufgabentexts im PDF, nicht die Seite des Erwartungshorizonts.

Schreibweisen in den Feldern:
Potenzen mit ^ (f(x) = −6x^5 + 18,75x^4), Ableitungen f'(x), f''(x), f'''(x), Definitionsbereich „x aus IR" wie im Heft.
Koordinaten als P(x; y) mit Semikolon, nicht mit „|" wie im Heft – „|" trennt im Schema Mehrfachwerte. Das Semikolon im Feld ist unschädlich, weil jedes Feld in Anführungszeichen steht; ein Skript darf eine Zeile nie mit einem einfachen Trennen an „;" zerlegen, sondern nur mit einem CSV-Leser.
Intervalle als −3 <= x <= 3. Malpunkt „·", Euro „€", Prozent „%" hinter der Zahl mit Leerzeichen.

## 5 Leitideen

Differentialrechnung · Integralrechnung · Stochastik · Grundlagen

Die ersten drei sind die Gliederung der Prüfungsschwerpunkte und gleichzeitig die Überschriften der Aufgaben im Heft. „Grundlagen" ist eine Zutat dieses Profils: die Hefte verlangen innerhalb der Aufgaben Stoff, den die Schwerpunkte nicht als Inhalt führen, weil Kompetenzen dort ausdrücklich nicht auf Themengebiete beschränkt sind. Im Probelauf bestätigt durch 2026-C-3b (Grundwert aus 20 % Reduzierung, mitten in der Stochastik-Aufgabe) und den Nebentyp Masse aus Volumen und Dichte in 2026-C-2e.

## 6 Themenliste

Feste Ebene zwischen Leitidee und Typ. Die Klammer nennt den Schwerpunktstand: **27** nur Prüfungsschwerpunkte 2026/27 (Prüfung 2027), **28** nur 2027/28 (Prüfung 2028), ohne Angabe in beiden. Der Stand ist kein Katalogfeld, sondern wird über das Thema gefiltert – das Schema bleibt unverändert.

Differentialrechnung: Ableitungen bilden · Nullstellen ganzrationaler Funktionen · Extrem- und Sattelpunkte · Monotonie und Krümmung · Wendepunkte · Symmetrie nachweisen · Verhalten im Unendlichen · Graph zeichnen und zuordnen · Anstieg und Tangente · Normale (28) · Schnittpunkte von Funktionsgraphen · Funktionsgleichung bestimmen · Extremwertaufgaben (27)

Integralrechnung: Stammfunktion bilden · Bestimmtes Integral berechnen · Fläche zwischen Graph und x-Achse · Fläche zwischen zwei Graphen · Rotationsvolumen um die x-Achse (27) · Körpervolumen aus Grundfläche und Länge (28)

Stochastik: Daten darstellen und aufbereiten · Statistische Kenngrößen · Mehrstufige Zufallsexperimente · Baumdiagramm und Pfadregeln · Unabhängigkeit von Ereignissen · Erwartungswert · Kombinatorische Abzählverfahren (27)

Grundlagen: Prozentrechnung · Gleichungen lösen · Größen und Einheiten · Terme umformen

Anmerkungen zum Stand:
- Funktionsgleichung bestimmen reicht 2027 bis zum zweiten, 2028 bis zum vierten Grad (dritter und vierter nur über Symmetrie). Das Vorkommen 2026-C-2c ist quadratisch, gilt also für beide Jahrgänge.
- Unabhängigkeit von Ereignissen und Körpervolumen aus Grundfläche und Länge stehen erst in den Schwerpunkten 2027/28, kommen aber bereits 2026 vor (2026-C-3e, 2026-C-2e). Beide Themen haben damit eine Ankeraufgabe.
- Kombinatorische Abzählverfahren ist seit 2026 B belegt (2026-B-3d Kombination mit Wiederholung, 2026-B-3e Permutation mit Wiederholung).
- Normale ist seit 2025 A belegt (2025-A-1h, Normalengleichung an einer Stelle samt Einzeichnen). Extremwertaufgaben sind seit 2025 A belegt (2025-A-2d bis 2025-A-2f, Trainingsfläche mit 46 m Material als Kette aus Einzelwerten, Zielfunktion und Maximum).
- Rotationsvolumen um die x-Achse ist seit 2024 C belegt (2024-C-2c, Football-Spielball). Damit hat jedes Thema der Themenliste eine Ankeraufgabe außer Erwartungswert. Die Wortsuche hatte die Normale auch für 2023 A angezeigt; dieses Heft ist noch nicht erfasst.
- Einstufige Laplace-Experimente haben kein eigenes Thema. 2023-C-3b (Ergebnismenge angeben, Laplace-Bedingung begründen, zwei Wahrscheinlichkeiten vergleichen) läuft beim nächstliegenden Thema Baumdiagramm und Pfadregeln. Ein Thema „Laplace-Wahrscheinlichkeit" unter Stochastik wäre die Alternative; beim Abgleichlauf zu entscheiden.
- Erwartungswert kommt in keinem der 16 auf dem Bildungsserver liegenden Hefte 2019–2026 vor (Wortsuche). Das Thema steht in beiden Schwerpunktfassungen und bleibt in der Liste, ist aber als Prüfungsinhalt bisher unbelegt.
- Mehrstufige Zufallsexperimente und Baumdiagramm und Pfadregeln bleiben getrennt. Arbeitsregel seit 2025 C: zweistufige Versuche mit Zurücklegen gehen nach Baumdiagramm und Pfadregeln (2026-C-3d, 2026-B-3c), Versuche mit drei oder mehr Stufen oder ohne Zurücklegen nach Mehrstufige Zufallsexperimente (2025-C-3c ohne Zurücklegen, 2025-A-3e dreistufig mit Zurücklegen). Damit hat auch das zweite Thema eine Ankeraufgabe.

## 7 Besonderheiten beim Erfassen

- Drei Seitensorten je Heft. Die Aufgabe steht auf der Aufgabenseite, ergebnis und zwischenergebnis kommen aus dem Erwartungshorizont, die Punkteaufteilung aus dem Gutachtenbogen. Nichts aus Erwartungshorizont oder Gutachtenbogen gehört in gegeben oder gesucht.
- punkte kommt aus der Punktetabelle am Ende der Aufgabe und bleibt ungeteilt. Die feinere Aufteilung steht in bemerkung, mit der Formulierung des Gutachtenbogens (Kern § 4).
- Elementargeometrie als Werkzeug: Dreiecks-, Rechteck- und Körperflächen kommen in Analysis-Aufgaben vor, die Themenliste hat dafür keinen Eintrag. Solche Teilaufgaben werden beim nächstliegenden Thema geführt (2026-B-1h bei Anstieg und Tangente, weil das Dreieck von der Tangente eingeschlossen wird; 2025-A-2d bei Extremwertaufgaben, weil die Rechteckfläche der erste Schritt einer Extremwertaufgabe ist) und im Bericht gemeldet. Reine Umrechnungen über einen Maßstab gehen nach Grundlagen / Größen und Einheiten.
- Eine Teilaufgabe verlangt oft zwei oder drei Leistungen ohne eigene Buchstaben („Ermitteln Sie … und bestimmen Sie …", „Prüfen Sie, ob …"). Das bleibt eine Zeile: gesucht, ergebnis und format nennen alle Leistungen in ihrer Reihenfolge, typ ist die erste, typ_neben die weiteren.
- thema bei mehrleistigen Zeilen nach dem Punkt-Schwerpunkt wählen, auch wenn der typ in fhr-typen.csv unter einem anderen Thema steht; der Fall gehört in den Bericht (2025-A-1c, 2024-C-1d; 2024-B-2a: Achsensymmetrie begründen 1 BE, Achsen einzeichnen 2 BE, daher Graph zeichnen und zuordnen).
- Aussagenlisten: Verlangt eine Teilaufgabe Begründungen zu mehreren durchnummerierten Aussagen ((I) bis (IV) in 2024-B-1b), bleibt das nach Kern § 4 eine Zeile; stichwoerter nennt den Inhalt jeder Aussage, ergebnis die Begründung jeder Aussage in derselben Reihenfolge.
- Aufgaben ohne Funktionsgleichung: Manche Teilaufgaben argumentieren allein am abgebildeten Graphen (2024-B-1a, 2024-B-1b, 2025-A-1b). skizze muss den Verlauf dann so genau beschreiben, dass Extrempunkte, Nullstellen und Krümmungswechsel daraus hervorgehen; gegeben nennt ausdrücklich, dass keine Funktionsgleichung vorliegt.
- Vorgegebene Zwischen- und Kontrollergebnisse: Nennt eine Teilaufgabe ein Ergebnis aus einem früheren Teil, steht der Wert in gegeben und die frühere Kennung trotzdem in abhaengig_von.
- Der Funktionsterm steht im Stamm und gehört vollständig in gegeben jeder Zeile, die ihn braucht – sonst fällt die Zeile durch den Nachbau-Test.
- Zu rendern sind alle Aufgabenseiten: Abbildungsauswahl (mehrere Graphen), vorgedruckte Wertetabellen und Preistabellen. Bei Widerspruch gilt das Bild.
- Zeichnet der Prüfling das Material selbst (Koordinatensystem mit frei gewählter Achseneinteilung, Baumdiagramm, Diagramm), ist material „keins"; skizze beschreibt dann, was entstehen soll.
- ergebnis trägt bei amtlicher Übernahme den Zusatz „amtlich". Weicht die eigene Rechnung ab, bleibt das amtliche Ergebnis in ergebnis und die Abweichung steht in bemerkung. Der Erwartungshorizont rechnet gelegentlich mit gerundeten Zwischenwerten weiter (2026-C-3b: amtlich 204 €, exakt 203,90 €; 2024-C-1d: f''(2,77) amtlich 4,16, mit der ungerundeten Stelle 4,15; 2024-B-1e: Wendepunkte amtlich (2,06; −13,67) und (−1,46; 3,99), mit den ungerundeten Wendestellen −13,63 und 3,98).
- Rundung zwei Dezimalstellen; „rund" oder „etwa" übernehmen, wo der Erwartungshorizont ≈ setzt.
- Stochastik-Aufgaben mischen regelmäßig Prozentrechnung und Gleichungen hinein. Solche Teilaufgaben bekommen leitidee Grundlagen, nicht Stochastik.

## 8 Beispielzeilen

Vier Zeilen aus dem Heft 2026 C, je eine Leitidee, zur Lesbarkeit als Feld = Wert; in fhr-katalog.csv stehen dieselben Werte als eine Zeile in der Reihenfolge der Kopfzeile. Dieser Abschnitt wird aus dem Katalog erzeugt und weicht deshalb nicht von ihm ab.

    id = 2026-C-1c · jahr = 2026 · papier = C · block =  · aufgabe = 1 · titel = Differentialrechnung · teilaufgabe = c · seite = 2
    punkte = 3 · stern =  · hilfsmittel = ja · afb_amtlich = 
    leitidee = Differentialrechnung · thema = Ableitungen bilden · typ = Ableitung ganzrationale Funktion · typ_neben =  · stichwoerter = Potenzregel|Faktorregel|Summenregel|dritte Ableitung · voraussetzungen = 
    format = Rechnung · operator = Notieren Sie · antwort = Term
    material = keins · skizze = keine · kontext = ohne · textumfang = kurz
    gegeben = f(x) = −6x^5 + 18,75x^4 + 20x^3 − 90x^2; x aus IR · gesucht = erste, zweite und dritte Ableitung von f · verfahren = Potenz-, Faktor- und Summenregel dreimal hintereinander anwenden · schritte = 3 · zahlenraum = dezimal|negativ|Potenz · einheiten =  · abhaengig_von = 
    ergebnis = f'(x) = −30x^4 + 75x^3 + 60x^2 − 180x|f''(x) = −120x^3 + 225x^2 + 120x − 180|f'''(x) = −360x^2 + 450x + 120 (amtlich) · zwischenergebnis = 
    niveau_geschaetzt = I · fehlerquelle = Exponenten nicht um eins senken oder den Faktor 18,75 nicht mit 4 multiplizieren · bemerkung = Gutachten: Notieren der ersten bis dritten Ableitung 3 BE

    id = 2026-C-2e · jahr = 2026 · papier = C · block =  · aufgabe = 2 · titel = Integralrechnung · teilaufgabe = e · seite = 4
    punkte = 2 · stern =  · hilfsmittel = ja · afb_amtlich = 
    leitidee = Integralrechnung · thema = Körpervolumen aus Grundfläche und Länge · typ = Volumen aus Querschnittsfläche und Länge · typ_neben = Masse aus Volumen und Dichte · stichwoerter = Querschnitt|Prisma|Einheiten umrechnen|Dichte|Aluminiumprofil · voraussetzungen = mm^3 in cm^3 umrechnen|Längeneinheit im Koordinatensystem deuten
    format = Rechnung · operator = Berechnen Sie · antwort = Zahl
    material = keins · skizze = keine · kontext = Bauteil/Autobau · textumfang = mittel
    gegeben = die Fläche aus Teilaufgabe d ist der Querschnitt eines Aluminiumprofils, rund 54,33 FE; eine Längeneinheit im Koordinatensystem entspricht einem Millimeter; Profillänge 2 m; ein Kubikzentimeter Aluminium wiegt 2,7 g · gesucht = Masse eines zwei Meter langen Aluminiumprofils · verfahren = Querschnittsfläche in mm^2 mit der Länge in mm multiplizieren, das Volumen in cm^3 umrechnen und mit der Dichte multiplizieren · schritte = 3 · zahlenraum = dezimal · einheiten = mm^2|mm|mm^3|cm^3|g · abhaengig_von = 2026-C-2d
    ergebnis = Masse rund 293,38 g (amtlich) · zwischenergebnis = V = 54,33 mm^2 · 2000 mm = 108 660 mm^3 = 108,66 cm^3
    niveau_geschaetzt = II · fehlerquelle = mm^3 mit dem Faktor 10 statt 1000 in cm^3 umrechnen · bemerkung = Gutachten: Berechnen von Volumen und Masse eines Bauteils 2 BE

    id = 2026-C-3b · jahr = 2026 · papier = C · block =  · aufgabe = 3 · titel = Stochastik · teilaufgabe = b · seite = 7
    punkte = 2 · stern =  · hilfsmittel = ja · afb_amtlich = 
    leitidee = Grundlagen · thema = Prozentrechnung · typ = Grundwert aus Prozentwert berechnen · typ_neben = Differenzbetrag aus Stückzahlen berechnen · stichwoerter = Rabatt 20 %|Grundwert|Originalpreis|Mehreinnahme · voraussetzungen = verminderten Grundwert erkennen|mit Anzahlen multiplizieren
    format = Rechnung · operator = Ermitteln Sie|Berechnen Sie · antwort = Zahl
    material = Tabelle · skizze = Preistabelle aus dem Aufgabenstamm wird weiterverwendet · kontext = Einzelhandel/Rabatt · textumfang = mittel
    gegeben = Preistabelle: reduzierter Verkaufspreis 15,99 € (PG 1) mit Anzahl 24, 23,99 € (PG 2) mit Anzahl 10, 31,99 € (PG 3) mit Anzahl 6; insgesamt 40 T-Shirts; die Preisreduzierung betrug 20 % · gesucht = Originalpreise aller drei Preisgruppen|Mehreinnahmen bei gleichen Verkaufszahlen ohne Reduzierung · verfahren = die reduzierten Preise entsprechen 80 %, also mit 100 durch 80 auf den Originalpreis hochrechnen; die Preisdifferenzen mit den Anzahlen multiplizieren und summieren · schritte = 4 · zahlenraum = dezimal|Prozent · einheiten = € · abhaengig_von = 
    ergebnis = Originalpreise 19,99 €, 29,99 € und 39,99 €|Mehreinnahmen 204 € (amtlich) · zwischenergebnis = Preisdifferenzen 4 €, 6 € und 8 €
    niveau_geschaetzt = II · fehlerquelle = 20 % auf den reduzierten Preis aufschlagen statt den Grundwert zu berechnen · bemerkung = Gutachten: Ermitteln der Originalpreise und Mehreinnahmen 2 BE; eigene Rechnung mit ungerundeten Originalpreisen ergibt 203,90 €, der Erwartungshorizont rechnet mit den gerundeten Preisen und erhält 204 €

    id = 2026-C-3e · jahr = 2026 · papier = C · block =  · aufgabe = 3 · titel = Stochastik · teilaufgabe = e · seite = 7
    punkte = 4 · stern =  · hilfsmittel = ja · afb_amtlich = 
    leitidee = Stochastik · thema = Unabhängigkeit von Ereignissen · typ = Vierfeldertafel vervollständigen · typ_neben = Stochastische Unabhängigkeit prüfen · stichwoerter = Vierfeldertafel|Randhäufigkeit|Unabhängigkeit|Produkt der Wahrscheinlichkeiten · voraussetzungen = Gegenereignis bilden|Wahrscheinlichkeit als Anteil an 40 angeben
    format = Rechnung|Begründung · operator = Ermitteln Sie|Prüfen Sie · antwort = Zahl|Text
    material = Tabelle · skizze = Preistabelle aus dem Aufgabenstamm wird weiterverwendet, keine Vierfeldertafel vorgedruckt · kontext = Einzelhandel/Kundschaft · textumfang = lang
    gegeben = Preistabelle: reduzierter Verkaufspreis 15,99 € (PG 1) mit Anzahl 24, 23,99 € (PG 2) mit Anzahl 10, 31,99 € (PG 3) mit Anzahl 6; insgesamt 40 T-Shirts; von den 24 T-Shirts der PG 1 kauften 16 Frauen; 6 Männer kauften teurere T-Shirts, also nicht aus PG 1; Ereignis F ein T-Shirt wird von einer Frau gekauft, Ereignis G ein T-Shirt der PG 1 wird gekauft · gesucht = Anzahl der an Frauen und an Männer verkauften T-Shirts|Prüfung, ob F und G stochastisch unabhängig sind · verfahren = Vierfeldertafel mit den Randsummen 24, 16 und 40 füllen; dann P(G) · P(F) mit P(G und F) vergleichen · schritte = 5 · zahlenraum = dezimal|Bruch · einheiten =  · abhaengig_von = 
    ergebnis = 26 T-Shirts an Frauen und 14 an Männer|P(G) · P(F) = 0,39 ist ungleich P(G und F) = 0,4, also sind F und G stochastisch abhängig (amtlich) · zwischenergebnis = Vierfeldertafel: PG 1 und Frau 16, PG 1 und Mann 8, teurer und Frau 10, teurer und Mann 6|P(G) = 24/40, P(F) = 26/40, P(G und F) = 16/40
    niveau_geschaetzt = III · fehlerquelle = die 6 Männer der PG 1 zuordnen und dadurch falsche Randsummen erhalten · bemerkung = Gutachten: Ermitteln der Verkaufszahlen an Frauen und Männern 2 BE, Prüfen der Bedingung für stochastische Unabhängigkeit 2 BE

Ein „?" hinter einem Wert bedeutet: plausibel, aber nicht am Bild geprüft; der Grund steht dann in bemerkung. In diesen Beispielzeilen kommt es nicht vor.

## 9 Offene Punkte

- Bedeutung der Buchstaben A, B, C ist nicht belegt.
- Umfang: erfasst werden 2023–2026 (acht Hefte). Die Jahrgänge 2019–2022 liegen auf dem Bildungsserver und bleiben Reserve; sie liefern nach der Wortsuche kein Thema, das der Bestand nicht schon enthält, und stehen unter älteren, teils coronabedingt gekürzten Vorgaben. Herangezogen werden sie nur, wenn beim Blattbau ein Typ zu wenige Originale für eine Kette hat.
- Nachschreibe-Vorschläge fehlen für alle Jahrgänge.
- Kein Thema für einstufige Laplace-Experimente (§ 6); die drei Typen Ergebnismenge eines Zufallsexperiments angeben, Laplace-Bedingung begründen und Laplace-Wahrscheinlichkeit berechnen hängen deshalb unter Baumdiagramm und Pfadregeln.
- Erwartungswert ohne Fundstelle (§ 6). Die Überlappung Mehrstufige Zufallsexperimente / Baumdiagramm und Pfadregeln ist mit der Arbeitsregel in § 6 geklärt.
- msa.md schreibt Koordinaten mit „|" und damit mit dem Zeichen des Mehrfachwerts; dieses Profil weicht bewusst ab. Vorschlag zur Nachbesserung an msa.md, hier nicht ausgeführt.
