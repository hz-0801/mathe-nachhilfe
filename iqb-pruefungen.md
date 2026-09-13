# IQB-Aufgabenpool Mathematik – Stapel und Erfassungsstatus
Stand 13.09.2026 · Profil iqb · gepflegt vom Katalog-Prompt

## 1 Quelle

Gemeinsame Abituraufgabenpools der Länder, Fach Mathematik, IQB. Dateien und
Kennungen in iqb-quellen.md und iqb-quellen.csv; Aufbau, Kürzel und Regeln in
iqb.md. Amtliche Lösungen liegen für jede Aufgabe vor (Erwartungshorizont);
der Standardbezug liefert afb_amtlich. Amtliche Vorgaben stehen gesondert in
abi-vorgaben.md.

## 2 Stapel Prüfungsteil A

Ein Stapel ist ein Prüfungsteil eines Pooljahrs auf einem Niveau (iqb.md § 7);
Reihenfolge von oben nach unten. „weiter" ist der nächste Stapel mit Status
„nicht erfasst".

| Stapel | Dateien | Status |
|---|---|---|
| 2026-ga-A | 19 (18 + 1 Dublette) | **erfasst 2026-09-13, 33 Zeilen** · 34 Typen neu · Eichung 30 von 33 |
| 2026-ea-A | 20 | **erfasst 2026-09-13, 37 Zeilen** · 32 Typen neu, 7 wiederverwendet · Eichung 34 von 37 |
| 2025-ga-A | 17 (16 + 1 Dublette) | **erfasst 2026-09-13, 31 Zeilen** · 31 Typen neu, 2 wiederverwendet · Eichung weit 29, eng 30 von 31 |
| 2025-ea-A | 20 (19 + 1 Dublette) | **erfasst 2026-09-13, 34 Zeilen** · 31 Typen neu, 4 wiederverwendet · Eichung eng 30 von 34 |
| 2024-ga-A | 17 (16 + 1 Dublette) | **erfasst 2026-09-13, 30 Zeilen** · 27 Typen neu, 4 wiederverwendet · Eichung eng 26 von 30 |
| 2024-ea-A | 19 | nicht erfasst |
| 2023-ga-A | 14 (13 + 1 Dublette) | nicht erfasst |
| 2023-ea-A | 18 | nicht erfasst |
| 2022-ga-A | 14 | nicht erfasst |
| 2022-ea-A | 17 | nicht erfasst |
| 2021-ga-A | 13 (11 + 2 Dubletten) | nicht erfasst |
| 2021-ea-A | 19 (17 + 2 Dubletten) | nicht erfasst |
| 2020-ga-A | 10 | nicht erfasst |
| 2020-ea-A | 15 | nicht erfasst |
| 2019-ga-A | 11 | nicht erfasst |
| 2019-ea-A | 10 | nicht erfasst |
| 2018-ga-A | 12 | nicht erfasst |
| 2018-ea-A | 12 | nicht erfasst |
| 2017-ga-A | 10 | nicht erfasst |
| 2017-ea-A | 11 | nicht erfasst |
| bsp-ga-A | 16 (12 + 4 Dubletten) | nicht erfasst |
| bsp-ea-A | 14 (12 + 2 Dubletten) | nicht erfasst |

Dubletten: wortgleiche Dateien unter beiden AG/LA-Alternativen (iqb.md § 7,
Spalte dublette_von in iqb-quellen.csv); sie bekommen keine Zeile. Teil A hat
damit 313 zu erfassende Aufgaben.

Kennzahlen je Stapel (Zeile „Kennzahlen:" aus iqb-bau.py; Grundlage für die
Schwellenwerte nach drei Stapeln, iqb.md § 7):

| Stapel | Zeilen | Typen verwendet | davon neu | Eichung | „?" | ersatzweise | Wiederverwendung im selben Niveau | außerhalb der Geltung be-gk, be-lk, bb-gk, bb-ea |
|---|---|---|---|---|---|---|---|---|
| 2026-ga-A | 33 | 34 | 34 (100 %) | 30 von 33 (91 %) | 0 | 0 | – | 0, 0, 0, 0 |
| 2026-ea-A | 37 | 39 | 32 (82 %) | 34 von 37 (92 %), enge Fassung 36 (97 %) | 0 | 0 | – (erster Stapel erhöht) | 7, 6, 7, 6 |
| 2025-ga-A | 31 | 33 | 31 (94 %) | weit 29 von 31 (94 %), eng 30 (97 %) | 0 | 0 | 1 von 33 aus 2026-ga-A (3 %) | 2, 2, 1, 1 |
| 2025-ea-A | 34 | 35 | 31 (89 %) | eng 30 von 34 (88 %) | 0 | 0 | 2 von 35 aus 2026-ea-A (6 %) | 8, 2, 8, 2 |
| 2024-ga-A | 30 | 31 | 27 (87 %) | eng 26 von 30 (87 %) | 0 | 1 | 2 von 31 aus 2026-ga-A und 2025-ga-A (6 %) | 4, 4, 4, 4 |

„Davon neu" zählt gegen den Gesamtbestand; die letzte Spalte ist die
Konvergenzmessung innerhalb eines Niveaus (Typen des Stapels, die schon im
vorigen Stapel desselben Niveaus vorkamen).

## 3 Zurückgestellt

Prüfungsteil B (296 Dateien, 20 Stapel Jahr-Niveau-B plus zwei mit
Beispielaufgaben) liegt, bis Teil A durch ist und die Kennzahlen stehen. Die
Kürzel für Teil B sind in iqb.md § 4 vorläufig festgelegt.

## 4 Befunde

**Sondierung 13.09.2026.** 624 Dateien, Kennungen eindeutig zerlegbar. Der
Standardbezug ist eine Matrix Teilaufgabe × K1–K6 mit I, II, III in den Zellen –
bis zu sechs Bereiche je Teilaufgabe, nicht einer. Das Rechnerkürzel in Teil B
heißt 2017–2021 CAS, ab 2022 MMS. AG/LA hat zwei Alternativen: A1
Vektorgeometrie ohne Ebenen mit Matrizen, A2 mit Geraden, Ebenen, Abständen
(die Berlin-Brandenburger Fassung).

**Probelauf 2026MgrundlegendAAnalysis11.** Zwei Teilaufgaben, 5 BE, beide
Zeilen ohne „?", Eichung 2 von 2 (a: geschätzt I, amtlich I; b: geschätzt II,
amtlich I|II). Der 37-Feld-Satz trägt den Pool ohne Änderung: afb_amtlich ist
gefüllt, titel hält die Alternative A1/A2, aufgabe die Aufgabengruppe, bemerkung
die Standardbezug-Zeile. Nichts geschrieben; die zwei Zeilen gingen mit dem
Stapel 2026-ga-A in den Katalog.

**Stapel 2026-ga-A.** 19 Dateien, davon eine Dublette; 18 Aufgaben, 33 Zeilen,
alle 5 BE je Datei bestätigt, kein „?", kein „ersatzweise". Lauf aus frischer
Kopie byteidentisch, Selbstprüfung über den Bestand bestanden.

**Dubletten im Pool.** Aufgaben, die für beide AG/LA-Alternativen taugen,
nennen in der Kurzbeschreibung nur „AG/LA" und liegen wortgleich unter A1 und
A2 (2026MgrundlegendAAGLAA112 = …212). Der erste Textvergleich des Abschnitts
„1 Aufgabe" über alle 328 Teil-A-Dateien fand 13 Paare; die Absicherung vom
selben Tag (Auftrag des Lehrers) verglich alle drei Abschnitte – Aufgabe,
Erwartungshorizont, Standardbezug – und zusätzlich die Bildobjekte: bei allen
Paaren gleich, ein Paar nur in der Bildkodierung verschieden
(BeispielaufgabenMerhoehtAAGLAA111/211), eines nur im Leerraum („1: 3" gegen
„1:3", 2024MgrundlegendAAGLAA112/212). Der Scan vergleicht seitdem alle drei
Abschnitte ohne Leerraum und findet 15 Paare, alle AG/LA; sie stehen in
iqb-quellen.csv (dublette_von). Eine Fassung mit gleicher Aufgabe, aber
anderem Erwartungshorizont oder Standardbezug gibt es in Teil A nicht; die
Regel dafür (eigene Zeile, geteilter Typ) steht in iqb.md § 7. Sechzehn
Teil-A-Dateien haben drei Seiten (Bewertungshinweise rutschen auf Seite 3),
die Seitenzahl steht in iqb-quellen.csv.

**Ungegliederte Aufgaben.** Vier der 18 Aufgaben haben keine
Teilaufgabenbuchstaben, alle in Gruppe 2 (AGLAA12, AGLAA221, Stochastik21,
Stochastik22 mit je 5 BE); die beiden Analysis-Aufgaben der Gruppe 2 sind
gegliedert. Nach Kern § 4 eine Zeile;
teilaufgabe leer, id gleich Kennung. Auch der Standardbezug lässt die
Teilaufgabenspalte leer.

**Lineare Gleichungssysteme unter AG/LA.** 2026MgrundlegendAAGLAA12 ist ein
reines LGS; der Pool führt es unter AG/LA (A1), abi.md § 5 führt LGS unter
Analysis. Das Thema steht jetzt in beiden Listen von iqb.md § 6.

**Eichung 2026-ga-A: 30 von 33.** Drei Abweichungen: Analysis 1.4 a (Graph der
Funktion vom Ableitungsgraphen unterscheiden) geschätzt II, amtlich I;
Analysis 2.1 b (Produktregel mit Werten aus dem Graphen) geschätzt II, amtlich
III; Stochastik 2.2 (n und p aus μ und σ) geschätzt II, amtlich III. Muster:
die eigene Schätzung hält Ablesen plus Regelanwendung für II, der
Standardbezug setzt Kombinieren mehrerer Regeln (K2, K4) auf III. Zu wenig
Zeilen für eine Regeländerung; nach drei Stapeln prüfen.

**Typen.** 34 neue Typen bei 34 verwendeten, einer nur als typ_neben
(Orthogonalität von Gerade und Ebene über Normalen- und Richtungsvektor
begründen). Ein Etikett aus abi-typen.csv übernommen: Punktprobe an einer
Ebenengleichung durchführen. Kurzaufgaben des Teils A tragen je Teilaufgabe
fast immer nur eine Leistung; typ_neben ist in 2 von 33 Zeilen belegt, in den
abi-Kontextaufgaben war es ein Drittel.

**Kurzbeschreibung gegen Kennung.** Bei den Dubletten nennt die Kurzbeschreibung
das Sachgebiet als „AG/LA" ohne Alternative, die Fußzeile aber AGLA(A1) bzw.
AGLA(A2). titel folgt der Kennung (iqb.md § 4).

**Stapel 2026-ea-A.** 20 Dateien, keine Dublette, 37 Zeilen, alle 5 BE je Datei
bestätigt, kein „?", kein „ersatzweise". Lauf aus dem HEAD-Stand byteidentisch,
Selbstprüfung über den Bestand (70 Zeilen, 66 Typen, 2 Stapel) bestanden.
Drei ungegliederte Aufgaben (Analysis 2.2, 2.3, AGLAA223). AGLAA11 ist die
einzige Aufgabe der Gruppe 1 (aufgabe „1"); ihr Stamm steht auf Seite 1, die
Teilaufgaben mit dem Diagramm auf Seite 2 (seite 1|2).

**Erhöhtes Niveau: Matrizen in AG/LA A1.** Alle drei A1-Aufgaben des Stapels sind
Matrizenaufgaben (Übergangsmatrix, Eigenvektor und Inverse, orthogonale
Matrizen); sechs Zeilen unter dem Thema Matrizen und Übergangsprozesse, das in
Berlin und Brandenburg nicht Prüfungsgegenstand ist. Auf grundlegendem Niveau
2026 waren die A1-Aufgaben noch Vektorgeometrie ohne Matrizen.

**Varianten über die Niveaus.** 2026MerhoehtAAGLAA212 hat denselben
Aufgabenstamm wie 2026MgrundlegendAAGLAA213 (Prisma), mit anderer
Teilaufgabe b; 2026MerhoehtAStochastik21 ist die Würfelaufgabe aus dem
grundlegenden Sondierungsbeispiel (Kennung identisch, in 2026-ga-A nicht
enthalten). Typen wurden wiederverwendet, keine Dubletten im Sinn von § 7.

**Typen 2026-ea-A.** 39 verwendet, 32 neu, 7 aus 2026-ga-A wiederverwendet
(Prisma-Eckpunkt, Flächengleichheit, Punktprobe, Orthogonalität Gerade–Ebene,
rechter Winkel mit Parameter, Gleichschenkligkeit mit Parameter,
Bernoulli-Term); ein Etikett aus abi-typen.csv (Ereignis zu einem gegebenen
Wahrscheinlichkeitsterm beschreiben). Vorschlag für den Abgleich: die Definition
von „Parameter eines Punktes aus einer Flächengleichheit bestimmen" auf Dreieck
gegen Rechteck erweitern (AGLAA212-b).

**Eichung 2026-ea-A: 34 von 37.** Abweichungen: Analysis 1.1 a (Spiegelung
angeben) geschätzt I, amtlich bis II; Analysis 1.1 b (Schnittstelle, Ableitung,
Winkelbedingung) und Stochastik 1.1 b (μ, σ, Intervall, Diagramm) nach der Regel
„Kombinieren heißt III" geschätzt III, amtlich bis II. Die Regel trifft in
diesem Stapel alle 12 Zeilen mit amtlich III, überschätzt aber zwei
Verkettungen aus Routineschritten. Gegenbefund zum ersten Stapel; nach dem
dritten Stapel entscheiden, ob „Kombinieren" auf Verkettungen mit einer
Deutung oder Fallunterscheidung einzugrenzen ist.

**Stapel 2025-ga-A.** 17 Dateien, eine Dublette (AGLAA222 = AGLAA12), 31
Zeilen aus 16 Dateien, alle 5 BE bestätigt, kein „?", kein „ersatzweise". Lauf
aus dem HEAD-Stand byteidentisch, Selbstprüfung über den Bestand (101 Zeilen,
97 Typen, 3 Stapel) bestanden. Zwei ungegliederte Aufgaben (AGLAA11 als einzige
Aufgabe der Gruppe 1, Kurzbeschreibung „AG/LA (1)"). Erste Fundstelle des
Themas Hypergeometrische Verteilung (Stochastik 1.3 b).

**Eichung doppelt gerechnet (Auftrag des Lehrers).** Weite Fassung
„Kombinieren heißt III": 29 von 31; enge Fassung „III nur bei Verkettung mit
Deutung oder Fallunterscheidung": 30 von 31. Die weite Fassung überschätzt
AGLAA11 (Gleichungssystem aus M · v = v aufstellen und lösen) und AGLAA212-b
(Mittelpunkt, Höhe, Fläche), amtlich je II; die enge unterschätzt nur Analysis
2.2 a (Ableitung und Bruchgleichung), amtlich III über K5. Rückblick auf
2026-ea-A: die enge Fassung hätte dort 36 statt 34 von 37 getroffen; 2026-ga-A
ist in beiden Fassungen 30 von 33. **Entscheidung: die enge Fassung bleibt**
(iqb.md § 7, v0.3). Die Zeilen tragen die Schätzung der beim Erfassen
geltenden Fassung, die enge steht bei Abweichung in bemerkung.

**Wiederverwendung innerhalb des Niveaus.** Von 33 in 2025-ga-A verwendeten
Typen kam genau einer in 2026-ga-A vor (Punktprobe an einer Ebenengleichung),
ein zweiter in 2026-ea-A (Ereignis zu einem gegebenen Wahrscheinlichkeitsterm
beschreiben, dreimal verwendet). Konvergenz innerhalb des grundlegenden Niveaus
nach zwei Jahrgängen: 3 %. Zum Vergleich abi: 2017-bb-ea gegen 2018-bb-ea
18 %, 2018-be-gk gegen die LK-Hefte 32 % – dort aber Kontextaufgaben mit
mehr Zeilen je Typ. Die Kurzaufgaben des Teils A sind nach zwei Jahrgängen noch
nahezu disjunkt; zwei Typennamen aus abi-typen.csv übernommen (Baumdiagramm
zu einer zweistufigen Situation erstellen, Anzahl der Kugeln aus einer
Fairnessbedingung bestimmen). Vorschlag für den Abgleich: „Vektor als
Normalenvektor einer Ebene über Kollinearität nachweisen" mit „Orthogonalität
von Gerade und Ebene über Normalen- und Richtungsvektor begründen"
zusammenziehen (dieselbe Prüfung).

**Typenschnitt gemessen (Auftrag des Lehrers, 13.09.2026, Bestand 101
Zeilen).** Wiederverwendung je Stapel, Anteil der Zeilen, deren Schlüssel
schon in einem früheren Stapel vorkam:

| Stapel | nach typ gesamt | nach typ im Niveau | nach thema gesamt | nach thema im Niveau |
|---|---|---|---|---|
| 2026-ea-A | 6 von 37 (16 %) | – | 25 von 37 (68 %) | – |
| 2025-ga-A | 3 von 31 (10 %) | 1 von 31 (3 %) | 29 von 31 (94 %) | 24 von 31 (77 %) |

Zeilen je Wert: Haupttyp 1,09 (101 Zeilen auf 93 Typen; 86 Typen kommen
einmal vor, 6 zweimal, 1 dreimal; grundlegend 1,03, erhöht 1,00). Thema 3,48
(29 belegte Themen; grundlegend 2,46 auf 26, erhöht 1,85 auf 20). 30 der 48
Themen sind belegt; unbelegt vor allem die LK-Themen (uneigentliche
Integrale, Rotationsvolumen, Normalverteilung, Hypothesentests) und Ebenen,
Schnittmengen, Skalarprodukt und Winkel, Vierfeldertafel, Unabhängigkeit.
Zwischenschnitt Thema × Handlungsklasse (berechnen, begründen, angeben,
zeichnen, aus format): 56 Werte, 1,8 Zeilen je Wert; 2025-ga-A gegen
2026-ga-A 12 von 31 Zeilen bekannt (39 %).

Lesart: Der Typ nach Kern § 6 ist für die Kurzaufgaben des Teils A so fein,
dass fast jede Zeile ihr eigenes Etikett trägt; eine Kette aus mehreren
Originalen (blatt-konzept.md § 3) kommt so nicht zustande. Das Thema
konvergiert dagegen schon nach einem Jahrgang auf drei Viertel. **Vorschlag,
nicht umgesetzt, ohne Änderung am Kern:** (1) Für Teil A stützt der Blattbau
Kette und Decke auf `thema` statt auf `typ`; der Typ bleibt als Feinetikett
für die Auswahl der Sprossen. (2) Beim ersten Abgleichlauf über ein
vollständiges Niveau (Kern § 9 erlaubt das Vereinheitlichen) die Teil-A-Typen
gröber schneiden: Gegenstand auf Themenebene plus Handlung, Zielgröße etwa
drei Zeilen je Typ – das entspricht dem Zwischenschnitt Thema × Handlungsklasse
(1,8 Zeilen je Wert nach drei Stapeln, steigend). Die Feinheit wandert nach
`stichwoerter` und `verfahren`, wo sie schon steht. Erst nach dem Abgleich
eine Schranke für neue Typen setzen.

**Matrizen auch auf grundlegendem Niveau.** 2025MgrundlegendAAGLAA11 ist eine
Matrizenaufgabe; der Befund aus 2026-ea-A gilt also nicht nur für erhöht. Im
Bestand jetzt 7 Zeilen unter Matrizen und Übergangsprozesse. Vorschlag zur
Kennzeichnung (Auftrag des Lehrers, nicht umgesetzt): kein neues Feld und
keine Zeilenmarkierung, sondern die Geltung am Thema führen – siehe Bericht
und iqb.md § 6.

**Stapel 2025-ea-A.** 20 Dateien, eine Dublette (AGLAA224 = AGLAA121), 34
Zeilen aus 19 Dateien, alle 5 BE bestätigt, kein „?", kein „ersatzweise". Lauf
aus dem HEAD-Stand byteidentisch, Selbstprüfung über den Bestand (135 Zeilen,
128 Typen, 4 Stapel) bestanden. Vier ungegliederte Aufgaben (Analysis 2.2,
AGLAA122, Stochastik 2.1, 2.3); AGLAA11 wieder einzige Aufgabe der Gruppe 1.
Datei AGLAA212 mit drei Seiten; Stochastik 1.2 b steht auf Seite 2. Erste
Fundstellen der Themen Umkehrfunktion (Analysis 2.2), Skalarprodukt und Winkel
(AGLAA211), Schnittmengen (AGLAA212 b), Scharen von Geraden und Ebenen (AGLAA221,
222), Unabhängigkeit (Stochastik 2.3); alle rechnerischen Ergebnisse mit sympy
bestätigt. Erster Stapel nach der engen Fassung als geltender Regel: die Zeilen
tragen die enge Schätzung direkt, kein Vermerk in bemerkung.

**Eichung 2025-ea-A: eng 30 von 34 (88 %), Schranke 85 % gehalten.**
Abweichungen: AGLAA121 a (gestaffeltes Gleichungssystem für a = 0 lösen) und
AGLAA211 a (Ankreuzen: Ergebnisart von Skalarprodukt-Ausdrücken) geschätzt I,
amtlich bis II; Stochastik 1.1 b (Auszahlung aus der Fairnessbedingung)
geschätzt III nach dem Regelbeispiel „faires Spiel als Erwartungswert gleich
Einsatz", amtlich II; Stochastik 2.1 (n und p aus P(X = 1) = 14 · P(X = 0) und
E = 10) geschätzt II als algebraische Verkettung ohne Deutung, amtlich III über
K2 und K5. Die Regel trifft 12 von 13 Zeilen mit amtlich III. Die beiden
letzten Abweichungen sind Messwerte zur Regel selbst: der Standardbezug setzt
die Fairnessdeutung hier nur II, die algebraische Verkettung mit Ersatz
n · p = 10 dagegen III; nach einem weiteren Stapel prüfen, ob „faires Spiel"
aus der Beispielliste der Deutungen fällt.

**Typen 2025-ea-A.** 35 verwendet, 31 neu, 4 wiederverwendet: 2 aus 2026-ea-A
(Symmetrieebenen eines Körpers, dort mit Begründung, hier nur Angabe; Unbekannte
Werte einer Zufallsgröße aus dem Erwartungswert), 1 aus 2026-ga-A (Extrempunkt
an vorgegebener Stelle nachweisen), 1 aus 2025-ga-A (Punktprobe an einer
Geraden, hier mit Scharparameter). Konvergenz innerhalb des erhöhten Niveaus
nach zwei Jahrgängen: 6 % (2 von 35), grundlegend waren es 3 %. Vorschläge für
den Abgleich: „Graph einer Stammfunktion unter vorgegebenen Graphen begründet
auswählen" mit „Graph der Funktion vom Graphen der Ableitung unterscheiden"
(2026-ga-A) zusammenziehen; „Verhältnis zweier Trefferwahrscheinlichkeiten aus
den Erwartungswerten im Diagramm nachweisen" mit „Trefferwahrscheinlichkeit aus
dem ganzzahligen Erwartungswert im Diagramm ermitteln" (2026-ga-A); „Integralwert
aus der Symmetrie des Graphen angeben" mit „Integral mit Wert null am Graphen
veranschaulichen" (2026-ea-A). Getrennt gehalten: „Lösungsanzahl eines
gestaffelten Gleichungssystems mit Parameter durch Fallunterscheidung
begründen" gegen „Lösbarkeit eines Gleichungssystems mit Parameter beurteilen"
(2025-ga-A), anderer Lösungsweg.

**Geltung 2025-ea-A.** Außerhalb der Geltung be-gk 8, be-lk 2, bb-gk 8, bb-ea
2 von 34: Matrizen (AGLAA11 b, AGLAA122) für alle vier Zielprüfungen,
Funktionsscharen (Analysis 1.1 a, b) und Scharen von Geraden und Ebenen
(AGLAA221 a, b, AGLAA222 a, b) nur für die Grundkurse. Bestand jetzt be-gk 17,
be-lk 10, bb-gk 16, bb-ea 9 von 135 Zeilen. Scharen kommen auf erhöhtem Niveau
in beiden Jahrgängen vor, 2026-ea-A eine Zeile (Analysis 2.2, Gruppe 2), hier
sechs, davon die Funktionsschar in Gruppe 1 (Analysis 1.1) und die Geraden- und
Ebenenscharen in Gruppe 2.

**Stapel 2024-ga-A.** 17 Dateien, eine Dublette (AGLAA212 = AGLAA112), 30
Zeilen aus 16 Dateien, alle 5 BE bestätigt, kein „?", einmal „ersatzweise"
(AGLAA112: ebene Figur aus Vektoren unter Flächeninhalt und Volumen im Raum).
Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung über den Bestand (165
Zeilen, 155 Typen, 5 Stapel) bestanden. Drei ungegliederte Aufgaben (Analysis
2.2, AGLAA112, AGLAA221); AGLAA211 mit drei Teilaufgaben a–c; Stochastik 2.2
mit drei Seiten (Teilaufgaben auf Seite 2). Kein neues Thema; neue
Gegenstände sind die Verflechtungsmatrix mit Diagramm (AGLAA111), das
Randomized-Response-Verfahren (Stochastik 2.2) und die Abstandsbedingung beim
Abzählen (Stochastik 1.3). Die Dateinamen tragen ab diesem Jahrgang die Endung „.docx" in der
Fußzeile, die Kennung ist unverändert.

**Eichung 2024-ga-A: eng 26 von 30 (87 %), Schranke 85 % gehalten** – mit dem
gefeuerten Eintrag der Deutungsliste je Abweichung (Auftrag des Lehrers):

| Zeile | geschätzt | amtlich | Eintrag der Deutungsliste |
|---|---|---|---|
| Analysis 1.3 b (Verschiebung zwischen zwei Graphen beurteilen) | III | II | „Aussage beurteilen" hat gefeuert; die Beurteilung ist ein Steigungsvergleich an einer Stelle. |
| AGLAA12 b (alle Fixvektoren) | II | III | kein Eintrag hat gefeuert (Produkt, Gleichsetzen, Auflösen); amtlich III über K1/K2 für die zweiparametrige Lösungsmenge. |
| Stochastik 1.2 b (Erwartungswert gegen Einsatz) | III | II | „faires Spiel als Erwartungswert gleich Einsatz" hat gefeuert – dritter Fall über dem Standardbezug (2025-ga-A Stochastik 2.2 b traf, 2025-ea-A Stochastik 1.1 b und hier nicht). |
| Stochastik 2.1 a (Pfad aus dem Sachtext) | I | II | kein Eintrag; als einzelne Rechnung I, amtlich II über K2/K3 (Sachtext in einen Pfad übersetzen). |

Treffer mit gefeuertem Eintrag: Analysis 2.2 („Bedingung in Gleichung
übersetzen": mittlere Änderungsrate als Geradensteigung), AGLAA221 (derselbe
Eintrag: Diagonalenschnittpunkt als Spurpunkt), Stochastik 2.2 a und b
(derselbe Eintrag: Verneinung der Frage, Ja-Anteil als Pfadsumme). Treffer
ohne Eintrag, aber III: Analysis 2.1 b (allgemeiner Nachweis mit Parameter u)
und Stochastik 2.1 b (Ungleichung mit Binomialsumme in eine Sachaussage
übersetzen). Nicht gefeuert, obwohl der Wortlaut es zuließe, und Treffer:
Analysis 1.2 b („Symmetrie ausnutzen" – die Symmetrie ist in a gegeben, die
Fläche eine Routinekette), AGLAA111 b („Bedingung in Gleichung übersetzen" –
die Übersetzung ist wörtlich: doppelt, viermal).

Lesart nach fünf Stapeln: (1) „faires Spiel" und „Aussage beurteilen" schneiden
zu weit – beide feuern auch bei Aufgaben, die der Standardbezug mit II belegt;
Kandidat für die Einschränkung: III nur, wenn die Deutung selbst eine
Modellierungsentscheidung ist (Bedingung erst finden), nicht, wenn sie
wörtlich vorgegeben ist („gleichen sich aus", „Verschiebung"). (2) Der Liste
fehlen zwei Einträge, die in der Praxis III liefern: „allgemeiner Nachweis mit
Parameter (verallgemeinern)" (2024 Analysis 2.1 b, 2025-ea-A Analysis 2.1 a
und AGLAA222 b, alle amtlich III) und „Term oder Ungleichung in eine
Sachaussage übersetzen" (Stochastik 2.1 b, amtlich III). (3) Offen bleibt der
Eintrag „Lösungsmenge mit freien Parametern beschreiben" (AGLAA12 b, amtlich
III; 2025-ga-A AGLAA11 amtlich II). Keine Änderung an iqb.md § 7 in diesem
Lauf; Vorschlag zur Entscheidung.

**Typen 2024-ga-A.** 31 verwendet, 27 neu, 4 wiederverwendet: Koordinaten
eines Eckpunkts eines Prismas (2026-ga-A), Ereignis zu einem gegebenen
Wahrscheinlichkeitsterm beschreiben (viertes Vorkommen), Abbildung zwischen
zwei Graphen angeben und Wahrscheinlichkeit für genau einen Treffer bei zwei
Versuchen (beide 2026-ea-A). Konvergenz im grundlegenden Niveau nach drei
Jahrgängen: 6 % (2 von 31). Vorschlag für den Abgleich: „Parameter für einen
rechten Winkel über das Skalarprodukt ermitteln" mit „Rechten Winkel eines
Dreiecks mit Parameter nachweisen" (2026-ga-A) zusammenziehen.

**Geltung 2024-ga-A.** Außerhalb der Geltung 4, 4, 4, 4 von 30: nur Matrizen
(AGLAA111 a, b; AGLAA12 a, b) – im dritten Jahrgang grundlegend wieder eine
volle Aufgabengruppe AG/LA (A1) mit Matrizen. Bestand jetzt be-gk 21, be-lk 14,
bb-gk 20, bb-ea 13 von 165 Zeilen.

**Zwischenschnitt Thema × Handlungsklasse durchgerechnet (Auftrag des
Lehrers, Bestand 165 Zeilen, nicht umgesetzt).** Handlungsklasse aus dem
ersten Wert von `format`: Rechnung → berechnen (73 Zeilen), Begründung →
begründen (47), Kurzantwort/Ankreuzen → angeben (35), Zeichnen/Eintragen →
zeichnen (10). Ergebnis: 75 Werte statt 149 Haupttypen, 2,20 Zeilen je Wert
(grundlegend 1,84 auf 51 Werte, erhöht 1,39 auf 51); Verteilung 33 × 1, 20 × 2,
11 × 3, 4 × 4, 4 × 5, 1 × 7, 2 × 8 Zeilen. Wiederverwendung im Niveau je
Stapel unter diesem Schnitt gegen `typ`: 2025-ga-A 39 % gegen 3 %, 2025-ea-A
32 % gegen 6 %, 2024-ga-A 67 % gegen 7 %. Die zwanzig größten Gruppen als
beispielhafte Typenliste (Zeilen darunter in Klammern):

| Schnittwert | Zeilen | Zeilen darunter (heutige Typen) |
|---|---|---|
| Flächeninhalt und Volumen im Raum · berechnen | 8 | Pyramidenhöhe aus Volumen, Flächengleichheit (2×), Prisma über Raute, gleichschenkliges Dreieck, Würfel-Teilkörper, Dreieck/Trapez, Quadrat aus Spurpunkt |
| Matrizen und Übergangsprozesse · berechnen | 8 | Zykluslänge, Vektorparameter, inverse Matrix, Matrixparameter (2×), Vertauschbarkeit, Verflechtungseintrag, Fixvektoren |
| Baumdiagramm und Pfadregeln · berechnen | 7 | fehlende Astwahrscheinlichkeiten, Vergleich zweier Geräte, ungerade Summe, Produktereignis bei n Würfen, lauter Treffer, Pfad aus Sachtext, Anteil aus Befragung |
| Funktionsklassen und Eigenschaften · begründen | 5 | Sinus-Extrempunkte, fehlende Punktsymmetrie, Nullstelle einsetzen, ungerade Exponenten, Verschiebung beurteilen |
| Kenngrößen von Verteilungen · berechnen | 5 | p aus ganzzahligem E, n und p aus E und σ, Sigma-Intervall, unbekannte Werte aus E (2×) |
| Orthogonalität · begründen | 5 | rechter Winkel (3×, davon 2× mit Parameter), Gerade–Ebene, Normalenvektor über Skalarprodukte |
| Zufallsexperimente und Urnenmodelle · angeben | 5 | Ereignis zu Term (4×), Laplace erster Zug |
| Binomialverteilung · angeben | 4 | Werte aus Säulendiagramm, Bernoulli-Term (2×), Sachaussage zu Binomialsumme |
| Binomialverteilung · berechnen | 4 | genau ein Treffer bei zwei Versuchen (2×), Einzelwert aus Symmetrie, n und p aus Verhältnis |
| Flächeninhalt durch Integration · berechnen | 4 | zwei Graphen mit Stammfunktion, Graph und Achsen, Flächenhalbierung, zwei Flächenstücke |
| Punkte und Strecken im Koordinatensystem · angeben | 4 | Prisma-Eckpunkt (3×), Ecke mit Vorzeichen nach Verschiebung |
| Funktionsklassen und Eigenschaften · angeben | 3 | Abbildung zwischen Graphen (2×), Wertemenge |
| Funktionsscharen und Ortskurven · berechnen | 3 | Scharparameter für waagerechte Tangente, Steigung im Ursprung, Punktsymmetrie der Schar |
| Kenngrößen von Verteilungen · begründen | 3 | Parität von n, Verhältnis der p aus E, Erwartungswert gegen Einsatz |
| Lagebeziehungen · begründen | 3 | Punktprobe Ebene (2×), Parallelität zur xy-Ebene |
| Lineare Gleichungssysteme · begründen | 3 | Lösung einsetzen, Lösbarkeit mit Parameter, Fallunterscheidung |
| Matrizen und Übergangsprozesse · begründen | 3 | Übergangsdiagramm, Existenz von Matrizen, Existenz von Kernvektoren |
| Orthogonalität · berechnen | 3 | Punkt aus Orthogonalität und Ebene, zwei Geraden, Parameter für rechten Winkel |
| Scharen von Geraden und Ebenen · begründen | 3 | Punktprobe an Schar, Identität der Schar, Nichtparallelität |
| Spiegelung · berechnen | 3 | Spiegelpunkt an Ebene, an Punkt, Abstand zum Spiegelbild |

Lesart: Der Schnitt bündelt, was im Blattbau als Kette taugt (Flächeninhalt
im Raum · berechnen, Baumdiagramm · berechnen, Orthogonalität · begründen), und
konvergiert im grundlegenden Niveau nach drei Jahrgängen auf zwei Drittel.
Er wirft aber Ungleiches zusammen: unter Matrizen · berechnen liegen
Verflechtung, Übergangsmatrix und Matrizenalgebra; unter Funktionsklassen ·
begründen Symmetrie, Nullstelle und Verschiebung. Eine Zwischenstufe (Thema ×
Handlung × Gegenstandsklasse, etwa „Symmetrie") läge zwischen 1,1 und 2,2
Zeilen je Wert. 33 der 75 Werte sind noch Einzelstücke, vor allem zeichnen und
die LK-Themen. Vorschlag bleibt wie in der Typenschnittmessung: Blattbau für
Teil A auf `thema` (oder auf diesem Schnitt), Typ als Feinetikett; gröberer
Schnitt erst beim Abgleichlauf.

## 5 Änderungslog

| Datum | Änderung |
|---|---|
| 2026-09-13 | 2024-ga-A vollständig erfasst: 30 Zeilen aus 16 Dateien (eine Dublette), Katalog 165 Zeilen, Typenliste 155. Alle Punktsummen geprüft (je 5), Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung bestanden. Eichung eng 26 von 30 (87 %), je Abweichung der gefeuerte Eintrag der Deutungsliste in § 4 (Vorschlag: „faires Spiel" und „Aussage beurteilen" einschränken, „allgemeiner Nachweis" und „Term in Sachaussage" ergänzen – nicht umgesetzt). Zwischenschnitt Thema × Handlungsklasse über 165 Zeilen in § 4 (75 Werte, 2,20 je Wert, Wiederverwendung im Niveau 67 % gegen 7 % nach typ; nicht umgesetzt). |
| 2026-09-13 | 2025-ea-A vollständig erfasst: 34 Zeilen aus 19 Dateien (eine Dublette), Katalog 135 Zeilen, Typenliste 128. Alle Punktsummen geprüft (je 5), Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung bestanden. Eichung eng 30 von 34 (88 %), Schranke 85 % gehalten; Wiederverwendung im Niveau 2 von 35; außerhalb der Geltung be-gk 8, be-lk 2, bb-gk 8, bb-ea 2. Befunde in § 4 (Messwerte zur engen Fassung, Scharen auf erhöhtem Niveau, Vorschläge für den Abgleich). |
| 2026-09-13 | Vorarbeiten vor 2025-ea-A: Typenschnitt gemessen (§ 4, Vorschlag nicht umgesetzt); Schranke für neue Typen deaktiviert, Eichschranke 85 % nach der engen Fassung scharf; Geltungstabelle aus den vier Prüfungsschwerpunkten 2027 in iqb.md § 6 (v0.4), iqb-bau.py v0.3 zählt Zeilen außerhalb der Geltung je Zielprüfung und die Wiederverwendung im Niveau als Kennzahlen; abi-vorgaben.md ergänzt. |
| 2026-09-13 | 2025-ga-A vollständig erfasst: 31 Zeilen aus 16 Dateien (eine Dublette), Katalog 101 Zeilen, Typenliste 97. Alle Punktsummen geprüft, Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung bestanden. Eichung doppelt gerechnet (weit 29, eng 30 von 31); Entscheidung für die enge Fassung, iqb.md v0.3 § 7. Wiederverwendung innerhalb des Niveaus als Kennzahl aufgenommen. Befunde in § 4 (Matrizen auch grundlegend, Hypergeometrische Verteilung belegt). |
| 2026-09-13 | 2026-ea-A vollständig erfasst: 37 Zeilen aus 20 Dateien, Katalog 70 Zeilen, Typenliste 66. Alle 20 Punktsummen geprüft (je 5), Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung bestanden, Eichung 34 von 37, Kennzahlen in § 4. Befunde in § 4 (Matrizen auf erhöhtem Niveau, Varianten über die Niveaus, Gegenbefund zur Regel „Kombinieren heißt III"). |
| 2026-09-13 | Dublettenprüfung abgesichert (alle Paare in drei Abschnitten und Bildobjekten gleich, Regel bleibt; Scan verschärft, 15 statt 13 Paare, Teil A 313 Aufgaben). iqb.md § 7: Fassungsregel, Erfassungshinweis „Kombinieren heißt III", Kennzahlen je Stapel; iqb-bau.py gibt die Kennzahlenzeile aus. |
| 2026-09-13 | 2026-ga-A vollständig erfasst: 33 Zeilen aus 18 Dateien (eine Dublette ohne Zeile), Katalog 33 Zeilen, Typenliste 34. Alle 18 Punktsummen gegen die BE-Spalte geprüft (je 5), Lauf aus frischer Kopie byteidentisch, Selbstprüfung bestanden, Eichung 30 von 33. iqb.md v0.2: § 4 ungegliederte Aufgaben und titel bei „AG/LA", § 6 Lineare Gleichungssysteme auch unter Analytische Geometrie, § 7 Dubletten, § 8 aus dem Katalog. iqb-quellen.csv um seiten und dublette_von ergänzt (Scan aller 328 Teil-A-Dateien: 13 Dublettenpaare, 16 Dateien mit drei Seiten); iqb-quellen.py angelegt. iqb-bau.py v0.2: Dubletten, ungegliederte Aufgaben, Seitenzahl aus der Quelle. Befunde in § 4. |
| 2026-09-13 | Profil iqb angelegt (iqb.md v0.1, iqb-quellen.md, iqb-quellen.csv, iqb-bau.py v0.1, diese Datei). Probelauf an 2026MgrundlegendAAnalysis11 bestanden. Schwellenwerte nach iqb.md § 7 als Vorschlag. |
