# Zentralabitur Mathematik Berlin/Brandenburg – Hefte und Erfassungsstatus
Stand 15.09.2026 · Profil abi · gepflegt vom Katalog-Prompt

## 1 Quelle

Jahresseite: https://bildungsserver.berlin-brandenburg.de/abituraufgaben-2011
Dateien unter …/fileadmin/bbb/unterricht/pruefungen/abitur_bb/Zabi_Mathematik/
Kürzel, Serverdateien und Seitenzahlen stehen vollständig in abi-quellen.md;
Zeiten, Wahlstruktur und BE-Verteilung in abi-aufbau.md und abi-struktur.json.

Veröffentlicht sind nur die Jahrgänge 2011–2018. Für die Landesaufgaben
2017/2018 gibt es keine amtlichen Lösungen; alle Ergebnisse im Katalog sind
eigene Rechnung. Für Poolaufgaben des IQB ab Prüfungsjahr 2019 liegt der
Erwartungshorizont vor. Amtliche Vorgaben und ihre Änderungen stehen gesondert
in vorgaben.md.

## 2 Hefte im Bestand (Schnitt ab 2017)

| Jahr | Papier | Land | Niveau | Rechner | Seiten | Zeit | BE | Status |
|---|---|---|---|---|---|---|---|---|
| 2017 | 2017-be-gk | BE | grundlegend | WTR | 8 | 210 | 80 | nicht erfasst |
| 2017 | 2017-be-lk | BE | erhöht | WTR | 10 | 270 | 100 | teilweise abgedeckt · drei Aufgaben wortgleich in 2017-bb-ea, drei eigene noch nicht erfasst |
| 2017 | 2017-bb-ea | BB | erhöht | WTR | 10 | 270 | 100 | **erfasst 2026-09-12, 36 Zeilen** (alle Aufgaben, beide Wahlwege) · Leitfassung erhöht |
| 2017 | 2017-be-gk-cas | BE | grundlegend | CAS | 8 | 210 | 80 | zurückgestellt – Nachtrag nach WTR |
| 2017 | 2017-be-lk-cas | BE | erhöht | CAS | 9 | 270 | 100 | zurückgestellt – Nachtrag nach WTR |
| 2017 | 2017-bb-ea-cas | BB | erhöht | CAS | 10 | 270 | 100 | zurückgestellt – Nachtrag nach WTR |
| 2018 | 2018-be-gk | BE | grundlegend | WTR | 11 | 210 | 80 | **erfasst 2026-09-12, 36 Zeilen** (alle Aufgaben, beide Wahlwege) · Leitfassung grundlegend |
| 2018 | 2018-be-lk | BE | erhöht | WTR | 11 | 270 | 100 | teilweise abgedeckt · vier Aufgaben gleichlautend in 2018-bb-ea, zwei eigene noch nicht erfasst |
| 2018 | 2018-bb-ea | BB | erhöht | WTR | 13 | 270 | 100 | **erfasst 2026-09-12, 41 Zeilen** (alle Aufgaben, beide Wahlwege) |
| 2018 | 2018-be-gk-cas | BE | grundlegend | CAS | 10 | 210 | 80 | zurückgestellt – Nachtrag nach WTR |
| 2018 | 2018-be-lk-cas | BE | erhöht | CAS | 9 | 270 | 100 | zurückgestellt – Nachtrag nach WTR |
| 2018 | 2018-bb-ea-cas | BB | erhöht | CAS | 12 | 270 | 100 | zurückgestellt – Nachtrag nach WTR |
| 2023 | 2023-bebb-gk | BE/BB | grundlegend | WTR | 14 (Scan, nur Aufgabenseiten) | – (nicht im Scan) | 185 angeboten, 140 bei Wahl 2.1/2.2 (Teil-A-Wahl nicht im Scan) | **erfasst 2026-09-16, 58 Zeilen** (alle Aufgaben, beide Wahlwege; 11 Zeilen Pool-Dubletten mit Verweis) · gesichtet 2026-09-15 (§ 4) |

Leitfassung je Jahr und Niveau: erhöht bb-ea, grundlegend be-gk (abi.md § 7).
Wortgleiche Zwillinge des anderen Landes werden nicht als Zeile erfasst,
sondern hier notiert; eine eigene Zeile nur bei abweichender Teilung, erkennbar
am BE-Vektor.

**Kennzahlen je Heft** (Ausgabe von abi-bau.py ab v0.3; Hefte bis 2018 vor
dem Umstellungslauf erfasst, ohne Kennzahlenzeile). Spalten: Zeilen, verwendete
Typen, davon neu, Eichung (Zeilen mit amtlichem Bereich), „?“, ersatzweise,
Wiederverwendung im Niveau, außerhalb der Geltung je Zielprüfung, Schnitt,
Poolquote (Zeilen und angebotene BE, die wortgleich im Pool stehen – erfasst
als „Dublette von:" oder vorgemerkt als „Poolaufgabe (nicht erfasst)";
abgewandelte getrennt). Die Poolquote gibt abi-bau.py seit v0.5 je Heft aus
(Selbstprüfung und Kennzahlenzeile); die Hefte bis 2018 haben sonst keine
Kennzahlenzeile (vor v0.3 erfasst).

| Heft | Zeilen | Typen | neu | Eichung | ? | ersatzw. | im Niveau bekannt | außerhalb der Geltung | Schnitt | Pool (Zeilen; BE angeboten) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017-bb-ea | 36 | – | – | – | – | – | – | – | – | 6 von 36; 15 von 185 (8 %), alle vorgemerkt (Pool 2017 nicht erfasst) |
| 2018-be-gk | 36 | – | – | – | – | – | – | – | – | 9 von 36; 31 von 160 (19 %), alle vorgemerkt (Pool 2018 Teil B nicht erfasst); abgewandelt 2 Zeilen, 7 BE |
| 2018-bb-ea | 41 | – | – | – | – | – | – | – | – | 4 von 41; 10 von 185 (5 %) |
| 2023-bebb-gk | 58 | 59 | 38 (64 %) | 11 von 11 (100 %) | 3 | 0 | 7 von 59 (12 %) | be-gk 0, be-lk 0, bb-gk 0, bb-ea 0 | 42 Werte, 24 von 58 Zeilen im Niveau bekannt (41 %), 1 Wert neu im Gesamtbestand | 11 von 58; 30 von 185 (16 %) |

## 3 Nicht im Bestand

2011–2016 liegen auf dem Server, werden aber nicht aufgenommen (zeitlicher
Schnitt bei 2017, alter Rahmenlehrplan 2006). 2019 ff. sind aus
urheberrechtlichen Gründen nicht veröffentlicht; für Berlin Grundkurs
2019–2022 gibt es sieben Verlagsbände beim Lehrer, noch nicht hochgeladen.
Gescannte Verlagshefte (Stark) liegen lokal unter hefte/ und bleiben über
.gitignore außerhalb des Repos (urheberrechtlich geschützt); erstes Heft
2023-bebb-gk (§ 2, § 4).

## 4 Befunde zu einzelnen Heften

**2018-bb-ea.** Die Kopfzeile der Seite mit Aufgabe 1.3 (Glücksrad, Stochastik
im hilfsmittelfreien Teil) nennt das Jahr **2016**. Die Aufgabe ist offenbar
unverändert aus dem Heft 2016 übernommen und die Kopfzeile nicht bereinigt
worden. Beim Typenabgleich ist das keine Dublette innerhalb von 2018; ob die
Aufgabe im Heft 2016 wortgleich steht, ist ungeprüft, weil 2016 nicht im
Bestand ist.

**2018-bb-ea.** Teil 1 trägt in der Kopfzeile „Land Brandenburg“, Teil 2
„Länder Berlin und Brandenburg“. Damit ist am Heft selbst belegt, was abi.md
§ 1 aus den Deckblättern schließt: der hilfsmittelfreie Teil ist
brandenburgisch, die Sachgebietsaufgaben stammen aus dem gemeinsamen Werk.

**2018-bb-ea.** Die BE des hilfsmittelfreien Teils stehen nicht an den
einzelnen Aufgaben, sondern gesammelt in einer Tabelle am Ende von Teil 1
(Analysis 2 + 3, Geometrie 2 + 3, Stochastik 3 + 2 = 15).

**2018-bb-ea.** Die Wahlaufgaben sind ungleich gewichtet: 3.1 hat 25 BE, 3.2
nur 10; bei Aufgabenstellung 4 ist es umgekehrt (4.1 zehn, 4.2 fünfundzwanzig).
Erst die Kopplung 3.1 mit 4.1 beziehungsweise 3.2 mit 4.2 bringt beide Wege auf
35 BE und damit auf die 100 BE der Prüfung. Die Kopplung ist also nicht nur
inhaltlich begründet, sie gleicht die Punkte aus.

**2018-bb-ea.** Die BE-Tabellen sind in der Textextraktion mit
`pdftotext -layout` vollständig enthalten, auch die gegliederte Tabelle von
Teil 1. Das Rendern der Seiten bleibt für Abbildungen, Formelbilder und
Vektorschreibweisen nötig, nicht für die Punkte.

**2018-bb-ea.** Die beiden Analysisaufgaben sind gegensätzlich gebaut. In 2.1
ist `abhaengig_von` in sechs von elf Zeilen belegt, in 2.2 in keiner von acht:
dort steht jede Teilaufgabe für sich. Die Kettenstruktur ist damit eine
Eigenschaft der einzelnen Aufgabe, keine des Prüfungsformats.

**2017-bb-ea.** Aufbau wie 2018: Teil 1 hilfsmittelfrei mit den drei
Sachgebietsaufgaben 1.1 bis 1.3 zu je zwei Teilaufgaben (2 + 3 BE je Aufgabe,
Summe 15), Teil 2 mit den Wahlpaaren 2.1/2.2 (je 50 BE), 3.1/3.2 und 4.1/4.2.
Die Gewichtung der gekoppelten Wahlaufgaben ist dieselbe wie 2018: 3.1 hat 25 BE
und 4.1 zehn, 3.2 zehn und 4.2 fünfundzwanzig; erst die Kopplung bringt beide
Wege auf 35 BE. Der Punktausgleich über die Kopplung ist damit kein Einzelfall
von 2018, sondern in beiden erfassten Jahrgängen gleich gebaut.

**2017-bb-ea.** Wie 2018 trägt Teil 1 die Kopfzeile „Land Brandenburg“, Teil 2
„Länder Berlin und Brandenburg“. Die BE des hilfsmittelfreien Teils stehen auch
hier gesammelt in einer Tabelle am Ende von Teil 1, gegliedert nach Teilgebiet
und Buchstabe.

**2017-bb-ea.** Die Zeichnungsvorlage zu Aufgabe 2.2 c (Koordinatensystem mit
dem Graphen G_0,15) steht auf der Folgeseite; die betreffende Zeile trägt
deshalb die Seitenangabe 5|6. Die Maße des Vordachs in Aufgabe 3.1 (1,80 m Höhe,
1,40 m Breite) stehen ausschließlich in Abbildung 2 und fehlen in der
Textextraktion – ohne das gerenderte Bild ist 3.1 e und f nicht lösbar.

**2017-be-lk gegen 2017-bb-ea: die Zwillingsannahme trägt nur zur Hälfte.** Das
Berliner LK-Heft enthält drei Aufgaben, die im Brandenburger Heft wortgleich und
mit gleichem BE-Vektor stehen: Straßenverlauf (6-10-9-6-10-9), Zelt
(5-4-5-3-3-5) und Freizeit (8-4-5-4-4). Daneben stehen dort drei eigene
Aufgaben, die Brandenburg nicht hat: Verbindungsbrücke (Analysis, 50 BE),
Solarmodule (Analytische Geometrie, 25 BE) und Autopanne (Stochastik, 25 BE).
Umgekehrt fehlen in Berlin Eisbecher, Gartenpavillon und Vereinsjubiläum. Die
Regel „eine Leitfassung je Jahr und Niveau“ lässt die drei Berliner Aufgaben
also unerfasst; sie sind kein Doppel, sondern eine Lücke von 100 BE.

**2018-be-lk gegen 2018-bb-ea: derselbe Befund, kleiner.** Vase, Gartenteich,
Museum und Brillenträger stehen in beiden Heften; Quader und Smartphone gibt es
nur in Berlin, Quadrat und Medinet nur in Brandenburg. Ob Quader und Quadrat
dieselbe Aufgabe unter anderem Namen sind, ist ungeprüft.

**2018-be-gk.** Der Aufbau des grundlegenden Niveaus ist am Heft bestätigt: kein
hilfsmittelfreier Teil, drei Aufgabenstellungen mit je zwei Wahlaufgaben,
40 + 20 + 20 = 80 BE, 210 Minuten. Alle Zeilen tragen deshalb block B. Anders
als auf erhöhtem Niveau sind die beiden Wege gleich gewichtet: 1.1 und 1.2 haben
je 40 BE, 2.1 und 2.2 je 20, 3.1 und 3.2 je 20. Ein Punktausgleich über eine
Kopplung wie in bb-ea ist deshalb nicht nötig, und es gibt keine.

**2018-be-gk: die Typenliste trägt über die Niveaugrenze, aber ungleichmäßig.**
Von den 50 im Heft verwendeten Typen waren 16 aus den beiden LK-Heften bekannt,
also 32 Prozent – deutlich mehr als die 18 Prozent, die 2017 gegen 2018 auf
erhöhtem Niveau erreicht wurden. Der Unterschied sitzt im Sachgebiet: in der
Stochastik waren 7 von 14 Typen bekannt, in der Analytischen Geometrie 5 von 16,
in der Analysis nur 4 von 20. Die Stochastik prüft auf beiden Niveaus dieselben
Fertigkeiten, die Analysis nicht.

**2018-be-gk: der Grundkurs bringt eigene Themen, nicht nur eigene Typen.** Vier
Themen sind zum ersten Mal belegt, und zwar genau die elementaren: Ableitung und
Änderungsrate, Stammfunktion und Hauptsatz, Geraden, Lagebeziehungen. Die beiden
LK-Hefte haben sie übersprungen, weil sie dort Voraussetzung sind statt
Prüfungsgegenstand. Für die Heft-Phase heißt das: Basisaufgaben zu den Grundlagen
kommen eher aus den GK-Heften als aus den LK-Heften.

**2018-be-gk.** Fünf der 36 Teilaufgaben enthalten eine Kontrollangabe in eckigen
Klammern (1.1 c, 1.1 e, 1.1 f, 1.2 b, 2.1 a), in den beiden LK-Heften sind es
zusammen sechs von 77. Alle fünf wurden durch eigene Rechnung bestätigt.

**2018-be-gk.** Die BE-Tabellen der ersten Wahlaufgabe jeder Aufgabenstellung
sind mit „Teilaufgabe“ überschrieben, die der zweiten mit „Aufgabenteil“ – über
alle drei Aufgabenstellungen hinweg. Das ist ein Hinweis darauf, dass die beiden
Wahlaufgaben aus verschiedenen Quellen zusammengestellt wurden; für die Erfassung
ist es ohne Folgen.

**2018-be-gk.** Zwei Aufgaben haben eine Anlage: die Graphen zu 1.2 stehen auf
Seite 5 unter dem Schluss der Aufgabe, die Tabelle der summierten
Binomialverteilungen zu 3.2 auf Seite 11. Die betreffenden Zeilen tragen die
Seitenangaben 4|5 und 10|11. Das zu 1.1 f gehörende Koordinatensystem steht
dagegen auf derselben Seite wie die Teilaufgabe.

**Berlin und Brandenburg: Zeitleiste der Zusammenarbeit.** Berlin führte das
Zentralabitur 2006/2007 ein, seit dem Schuljahr 2009/2010 entwickeln beide Länder
die Aufgaben für Deutsch, Englisch, Französisch und Mathematik gemeinsam
(LISUM); die Serverpfade heißen entsprechend „gemeinsames_Abitur_Be_BB". Bis 2013
gab es je Niveau ein Heft ohne Länderkennzeichnung, ab 2014 drei Hefte je Jahrgang
mit landeseigener Auswahl aus einem gemeinsamen Werk. Das LISUM wurde Ende 2024
aufgelöst; seit dem Abitur 2026 erstellt Berlin über das BLiQ und Brandenburg über
das LIBRA getrennt. Am Dokument belegt: die Prüfungsschwerpunkte 2027 erscheinen
für beide Länder getrennt und unterscheiden sich im Grundkurs inhaltlich deutlich
(Brandenburg mit hypergeometrischer Verteilung, Bayes, Kolmogorow, Hessescher
Normalenform und Ableitung der Sinus- und Kosinusfunktion; Berlin ohne all das,
dafür mit Wurzelgleichungen, Lotto-Modell und Sachkontexten). Struktur und
Arbeitszeit sind gleich: Teil A und B, drei Pflichtaufgaben plus je eine aus drei
je Aufgabengruppe, 285 Minuten, Teil A innerhalb der ersten 100 Minuten. Die
Verlagsaussage, die Prüfungen seien ab 2018 vollkommen übereinstimmend, ist damit
doppelt widerlegt – am Heftvergleich 2017/2018 und an der heutigen Lage.

**Arbeitszeit Grundkurs.** Die Prüfungsschwerpunkte 2027 nennen für Berlin und
Brandenburg je 285 Minuten. Der in einem früheren Arbeitsstand aus den Berliner
Fachbriefen 21 und 22 abgeleitete Wert von 255 Minuten gilt nicht mehr; ob er
je galt oder falsch abgeleitet war, ist nicht geklärt und für den Katalog ohne
Folgen.

**Brandenburg auf grundlegendem Niveau.** Die Frage ist beantwortet: Brandenburg
hat eine eigene zentrale Prüfung. PS_Mathematik_GK_2027.pdf liegt unter
.../abitur_bb/RS_ZA_2027/ und beschreibt Struktur, Hilfsmittel und Arbeitszeit
vollständig. Nicht veröffentlicht werden nur die Aufgabenhefte.

**2023-bebb-gk (Stark-Band, Scan hefte/2023-bebb-gk.pdf, gesichtet
15.09.2026, nicht erfasst).** 14 Seiten, reiner Bildscan; alle
Aufgabenseiten vorhanden, keine Lösungen (Verlagsseiten 2023-1 bis 4, 13 bis
15, 23 bis 25, 31 bis 32, 38 bis 39; die Lücken sind die Tipp- und
Lösungsseiten des Bands). Kopf „Berlin/Brandenburg – Mathematik Grundkurs
2023". Aufgabenbestand:

| Aufgabe | Teilaufgaben | BE | Summe im Heft |
|---|---|---|---|
| 1 hilfsmittelfreier Teil: Analysis 1 (Tangenten an symmetrischem Graphen), Analysis 2 (Integral und Stammfunktion am Graphen), Analysis 3 (x³ − 3x², Berührung mit 9x + 5), Analytische Geometrie 1 (Gerade g, h durch A und B(5; 1; b)), Analytische Geometrie 2 (Dreieck A(1; 0; 2), B(3; 2; 10), C(4; 3; 5)), Stochastik 1 (Urne 3 rot, 2 weiß), Stochastik 2 (Histogramm, B(12; 0,25)) | je a, b: 2 + 3, 1 + 4, 2 + 3, 1 + 4, 2 + 3, 2 + 3, 2 + 3 | 7 × 5 | 35 ✓ |
| 2.1 Beistelltisch (Analysis, f(x) = 0,5 (x² − 4) e^x, Tischplatte) | a–m | 2, 5, 2, 4, 2, 5, 5, 2, 2, 3, 4, 5, 4 | 45 ✓ |
| 2.2 Temperatursteuerung (Analysis, f(x) = x³ − 12x² + 45x − 50, Backofen) | a–k | 4, 6, 3, 5, 4, 3, 5, 1, 4, 4, 6 | 45 ✓ |
| 3 Körper (Analytische Geometrie, ABCDEF in x + y + z = 4 und 2x + 2y + 2z = 5) | a–i | 4, 2, 3, 3, 3, 3, 4, 4, 4 | 30 ✓ |
| 4 Lehrkräfte (Stochastik, Aufgabenteil 1 a–h, Aufgabenteil 2 a–c) | 1: 3, 2, 2, 3, 2, 3, 1, 4; 2: 3, 2, 5 | 20 + 10 | 30 ✓ |

Wahl: 2.1 oder 2.2 (Analysis); 3 und 4 ohne Alternative; ob im
hilfsmittelfreien Teil alle sieben Aufgaben zu bearbeiten sind, steht nicht
auf den gescannten Seiten. Angeboten 185 BE, bei Wahl in Aufgabe 2 zu
bearbeiten 140 BE (35 + 45 + 30 + 30). Alle Summen des Hefts (35, 45, 45, 30,
30) stimmen mit den Teilaufgaben überein.

*Pool-Abgleich (gegen iqb-katalog.csv, Bestand 1061 Zeilen: Teil A 2018 bis
2026 vollständig, Teil B WTR 2023 bis 2026 grundlegend; Suche über gegeben,
gesucht, verfahren, stichwoerter und Zahlen, kein Textvergleich möglich).*

| Aufgabe | BE | Pool-Fundstelle | Sicherheit |
|---|---|---|---|
| 1 Analysis 1 | 5 | 2023MgrundlegendAAnalysis12 a, b (t1: y = 4/3 x + 4, Umfang des Dreiecks) | sicher – Zahlen und Aufträge gleich |
| 1 Analysis 2 | 5 | nicht im Pool (2023-ga-A Analysis 1.3 ist x⁴ − 4x³; kein Treffer in anderen Jahrgängen) | sicher |
| 1 Analysis 3 | 5 | nicht im Pool | sicher |
| 1 Analytische Geometrie 1 | 5 | 2023MgrundlegendAAGLAA212 a, b (g durch (2; 3; −7), B(5; 1; b)) | sicher |
| 1 Analytische Geometrie 2 | 5 | nicht im Pool | sicher |
| 1 Stochastik 1 | 5 | nicht im Pool (2019-ga-A Stochastik 1.2 hat 3 rote und 7 weiße, andere Aufträge) | sicher |
| 1 Stochastik 2 | 5 | nicht im Pool | sicher |
| 2.1 Beistelltisch | 45 | nicht im Pool | sicher |
| 2.2 Temperatursteuerung | 45 | nicht im Pool | sicher |
| 3 Körper | 30 | nicht im Pool | sicher |
| 4 Lehrkräfte | 30 | 2023MgrundlegendBStochastikWTR3: Aufgabenteil 1 a–e = 1a–e (12 BE), Aufgabenteil 2 a und c = 2a, 2b (8 BE); Aufgabenteil 1 f–h (mindestens n für 95 %, Präsentation 6 von 20 Lehrkräften: 8 BE) und Aufgabenteil 2 b (Aussage zum erwarteten Gewinn: 2 BE) sind Landeszusatz | sicher für die 20 BE (Zahlen und Aufträge gleich); der Zusatz ist im Pool nicht enthalten |

Anteil im Pool: 3 von 11 Aufgaben (zwei ganz, eine zu zwei Dritteln), 30 von
185 angebotenen BE (16 %), 30 von 140 zu bearbeitenden BE (21 %); im
hilfsmittelfreien Teil 10 von 35 BE (29 %), in Teil B 20 von 105 zu
bearbeitenden BE (19 %). Die Vermutung hoher Überschneidung bestätigt sich
für 2023 nicht: neun der elf Aufgaben sind Landesaufgaben, und die
übernommene Poolaufgabe ist um ein Drittel verlängert. Vorbehalt: Pool-Teil B
2022 und früher ist nicht erfasst (Reserve); eine Verwendung älterer
Poolaufgaben ist möglich, aber nicht üblich.

*Scan und Aufwand.* Rendern über pypdf und pillow (Seitenbilder 1800 bis
2300 Pixel breit, auf 1600 Pixel Breite als JPEG und in zwei Hälften mit 1800
Pixel), 21 s für 14 Seiten; das PDF selbst (90 MB) ist für das Read-Werkzeug
zu groß. Lesen: 14 Seiten in knapp 3 Minuten (21:55 bis 21:58 Uhr, aus den
Dateizeiten), rund 12 Sekunden je Seite einschließlich Aufnahme der BE; der
Pool-Abgleich danach etwa 5 Minuten (zwei Suchläufe über den Katalog, Sicht
der Trefferzeilen). Scanqualität: 13 Seiten klar; Seite 14
(Verlagsseite 2023-39, Aufgabe 4 Aufgabenteil 2) ist unscharf mit
Durchscheinen der Rückseite, in der vergrößerten Hälfte aber lesbar (Term
8 · (4/9)² + 2 · 2 · 4/9 · 5/9 + 1/2 · (5/9)² gegen den Pool bestätigt).
Durchscheinen der Rückseiten auf fast allen Seiten, ohne Folgen für das
Lesen. Fehlende Seiten: keine.

*Vorschlag für die Erfassung (nicht umgesetzt):* papier 2023-bebb-gk;
hilfsmittelfreier Teil als block A mit aufgabe 1.1 bis 1.7 in Heftreihenfolge,
Teil B block B mit aufgabe 2.1, 2.2, 3, 4 (Aufgabenteil 1 und 2 als 4.1 und
4.2); die im Pool stehenden Teilaufgaben nicht neu erfassen, sondern über
den Typ auf die iqb-Zeile verweisen – oder als abi-Zeile mit Verweis in
bemerkung, je nach Entscheidung des Lehrers zur Zusammenführung (iqb.md
§ 9). *(Umgesetzt am 16.09.2026 als abi-Zeile mit Verweis, unten.)*

**2023-bebb-gk erfasst (16.09.2026, Auftrag „Themenfeld bereinigen, dann
Stark-Heft 2023 erfassen", Punkt 5; abi-bau.py v0.4, erstes Heft nach dem
gemeinsamen Schnitt).** 58 Zeilen aus 12 Aufgaben (1.1 bis 1.7 der
hilfsmittelfreie Teil in Heftreihenfolge, 2.1, 2.2, 3, 4.1, 4.2); alle zwölf
Punktsummen stimmen (7 × 5, 45, 45, 30, 20, 10 = 185 BE). Selbstprüfung beider
Bau-Skripte bestanden (abi 171 Zeilen aus 4 Heften, iqb 1061 Zeilen, 913 Typen,
69 in beiden Katalogen), Lauf aus dem HEAD-Stand byteidentisch.

*Typen.* 59 verwendet, 38 neu (64 %), 19 aus dem iqb-Katalog übernommen, 2
aus dem eigenen Bestand (Lage und Art aller lokalen Extrempunkte bestimmen;
Mindestanzahl von Versuchen einer Bernoulli-Kette). Die neuen Typen nach
Thema: Kurvenuntersuchung 7 (Extremstellen aus f′ = 0; Aussagen nahe dem
Tiefpunkt ohne Rechnung; Monotonie aus bekanntem Extrempunkt; Wendepunkte über
f″; Graphen skizzieren und Tangentenaussage beurteilen; Mittelwert am Graphen
ablesen; umschließender Quader mit Maßstab), Tangente/Normale 4 (waagerechte
Tangente an vorgegebener Stelle; Dreiecke aus Wendetangente und Normale;
Schnittwinkel zweier Graphen; Tangente aufstellen und weiteren gemeinsamen
Punkt), Funktionsklassen 5 (Achsenschnittpunkte; Raute aus
Achsenschnittpunkten; gespiegelte Randlinien; y-Achsenschnittpunkt und
Nullstellenzahl aus Faktoren; Streckfaktor und Verschiebung durch
Koeffizientenvergleich), Flächeninhalt durch Integration 3, Stammfunktion 1,
Ableitungsgraph 2, Grenzwerte 1, Gleichungen lösen 1, Rekonstruktion 1,
Analytische Geometrie 8, Stochastik 5. Fast alles davon sind
Standardfertigkeiten, die der Pool in Teil A nicht stellt, weil er sie in
Ketten bündelt (Wendepunkte berechnen, Extremstellen ohne Art, Achsenschnittpunkte
eines Graphen); das Landesheft fragt sie einzeln und mit eigener Punktzahl.
Vorschläge für den nächsten Abgleichlauf: „Grenzverhalten eines Produkts aus
Polynom und e-Funktion angeben" neben „Nullstelle und Grenzverhalten …" (iqb,
mit Nullstelle) – zusammenziehen, wenn die Nullstelle als Nebenleistung
gelten darf; „Punkt: Teilpunkte einer Strecke in drei gleiche Abschnitte
berechnen" allgemein als Teilverhältnis fassen (3 a nutzt ihn für 1 : 3);
„Transformation: Terme der an den Koordinatenachsen gespiegelten Randlinien
angeben" gegen „Term und Intervall des an der y-Achse gespiegelten Graphen"
prüfen.

*Schnitt.* 42 Werte auf 58 Zeilen; 24 Zeilen (41 %) liegen auf Werten, die
das grundlegende Niveau (Pool ga und Heft 2018-be-gk) schon hat; **ein Wert
neu im Gesamtbestand**: Flächeninhalt durch Integration × Fläche × zeichnen
(2.1 m, Randlinien an der Sehne spiegeln und Lösungsweg beschreiben). Gegen
das grundlegende Niveau allein sind zwei Werte neu (dazu Kurvenuntersuchung ×
– × zeichnen, das der Pool nur auf erhöhtem Niveau hat). Gesamtbestand nach
dem Heft: 184 Schnittwerte (be-gk 150, bb-ea 171). Das ist derselbe Befund wie
in der Messung vom 15.09.2026: das Landesheft liegt fast vollständig auf dem
Poolschnitt, obwohl 64 % seiner Typen neu sind – der Schnitt trägt, der Typ
bleibt Feinetikett.

*Eichung.* 11 von 11 gewerteten Zeilen (100 %) – das sind genau die elf
Pool-Dubletten, deren afb_amtlich und „AB amtlich" aus dem Standardbezug der
Poolzeile übernommen sind; die Schätzung wurde vor dem Blick auf die Poolzeile
gesetzt, trifft aber naturgemäß dieselben Bereiche wie bei der Poolerfassung.
Die 47 Landeszeilen haben keinen amtlichen Bereich (kein Erwartungshorizont
im Scan). Die Eichung eines Landeshefts misst also nur den Poolanteil.

*Poolquote.* 11 von 58 Teilaufgaben (19 %) und 30 von 185 angebotenen BE
(16 %; von 140 zu bearbeitenden 21 %) stehen wortgleich im Pool 2023
grundlegend: Teil A Analysis 1 (1.2 a, b) und AG/LA (A2) 1.2 (a, b), Teil B
Stochastik WTR 3 (Aufgabenteil 1 a–e, Aufgabenteil 2 a und c). Zum Vergleich
2018-bb-ea Teil 1: 4 von 4 Analysis-/Geometriezeilen (10 von 15 BE, 67 %) aus
dem Pool. Die Quote schwankt zwischen den Jahrgängen stark und wird je Heft
mitgeführt (Spalte „Pool" in der Kennzahlentabelle § 2).

*Unsichere Zeilen* (3, erlaubt 5): 1.2 a (Integral näherungsweise aus der
Abbildung, ≈ 2,9), 1.7 a (P(3 < X < 6) aus dem Säulendiagramm, ≈ 0,29), 2.2 h
(Durchschnittstemperatur am Graphen, ≈ 230 °C) – Ablesewerte ohne amtliche
Lösung. Kontextgebunden (Traegerbindung: Kontext) 8 Zeilen: 2.1 i–m
(Tischplatte, Maßstab, Karton) und 2.2 h, i, k (Backofen); 14 %, wie in
den Teil-B-Stapeln des Pools (8 %) eher selten. Nicht lesbare Abbildungen:
keine; Seite 14 (Aufgabenteil 2) unscharf, der Erwartungswertterm ist gegen
die Poolzeile geprüft. Themen, die nicht passten: keine („ersatzweise" 0);
Geltung: alle 58 Zeilen liegen für alle vier Zielprüfungen in der Geltung – die
Aufgaben 4.1 g/h (6 aus 20, Lotto-Modell) stehen unter Zufallsexperimente und
Urnenmodelle, nicht unter Hypergeometrische Verteilung, weil Berlin die
Verteilung als Begriff nicht verlangt (abitur-vokabular.md § 3).

*Befunde am Heft.* (1) 2.2 k verlangt eine Funktion dritten Grades mit
k(0) = 20, k′(0) = 130 und Hochpunkt H(5 | 220); die vier Bedingungen liefern
eindeutig k(x) = 2x³ − 28x² + 130x + 20, aber k″(5) = 4 > 0 – H ist bei dieser
Funktion ein Tiefpunkt. Das Heft meint mit „Hochpunkt" nur die Bedingungen
k(5) = 220 und k′(5) = 0 (Steckbriefaufgabe); in bemerkung festgehalten.
*Nachgeprüft 16.09.2026 (Auftrag des Lehrers) am Scan in voller Auflösung
(Seite 10, Ausschnitt doppelt vergrößert):* Wortlaut „… ganzrationalen
Funktion k vom Grad 3 beschrieben werden, die folgende drei Eigenschaften
hat: I: k(0) = 20; II: k′(0) = 130; III: H(5 | 220) ist Hochpunkt des Graphen
von k. Ermitteln Sie die Funktionsgleichung der Funktion k." Drei
Eigenschaften, aus III zwei Gleichungen (k(5) = 220, k′(5) = 0), zusammen
vier – genau die Erfassung. Keine Abweichung, also die erste Lage: der
Widerspruch (k″(5) = 4 > 0; Hochpunkt bei x = 13/3 ≈ 4,33 mit k ≈ 220,3,
Tiefpunkt bei 5 mit k = 220) steckt im Heft und bleibt so vermerkt; Zeile
unverändert.
(2) 3 b: Lage zweier Ebenen unter Thema Ebenen abgelegt, nicht unter
Lagebeziehungen (dort nur die Klassen Punkt und Ebene, Gerade und Ebene) – analog
zur Lesart in abitur-vokabular.md § 4, nach der Lagen zweier Geraden unter
Geraden liegen; keine neue Klasse nötig. (3) Der Stark-Scan hat keine
Lösungen, alle 58 Ergebnisse sind eigene Rechnung (sympy), die elf Poolzeilen
zusätzlich gegen die amtlichen Ergebnisse der iqb-Zeilen geprüft. (4) 1.5 b
(Punkt D mit gleichen Abständen) hat unendlich viele Lösungen, erfasst ist die
naheliegende Punktspiegelung am Seitenmittelpunkt (Raute).

*Trägt abi-bau.py v0.4 das Heft?* Ja, mit einer Anpassung: der Test auf
ASCII-Minus schlug bei Pool-Kennungen mit Aufgabennummer („WTR3-1a") in
bemerkung an; die Kennungen werden jetzt vor dem Test ausgeblendet (wie beim
Umlaut-Test). Alles andere trug: zweistufige und einstufige Aufgabennummern
(2.1, 3, 4.1), Kürzel bebb, Dublettenverweis mit Typ- und Punktvergleich,
afb_amtlich nur bei Poolzeilen, Eichung ab 10 gewerteten Zeilen scharf,
Vollständigkeit über KONFIG["soll"] mit zwölf Aufgaben, Kennzahlenzeile. Nicht
im Skript, aber gebraucht: nichts. Offen bleibt, wie eine Poolquote je Heft
automatisch ausgegeben wird – die Zahl „Pool-Dubletten" steht in der
Kennzahlenzeile, die BE-Summe der Dubletten nicht (hier 30 von 185, von Hand).

*Aufwand.* Lesen der 14 Scanseiten mit Typsuche 12 Minuten, Rechnen (sympy)
und Bau der 58 Zeilen 12 Minuten, Lauf, HEAD-Rerun und Selbstprüfungen 3
Minuten – 27 Minuten bis zur bestandenen Selbstprüfung (07:58 bis 08:25 Uhr),
Nachführen etwa 10 Minuten. Rund 28 Sekunden je Zeile; vergleichbar mit den
Teil-B-Stapeln des Pools (16 bis 29 Minuten für 45 bis 69 Zeilen). Die
Sichtung am Vortag (Seiten rendern, BE-Tabelle, Pool-Abgleich, 8 Minuten)
kommt hinzu.

**Pool-Abgleich des abi-Bestands bis 2018 (Auftrag des Lehrers, 16.09.2026,
Punkt 2; Abgleichlauf 14).** Zwei Stufen. (1) Gegen den erfassten Pool
(iqb-katalog.csv, 1061 Zeilen): Wortmengen- und Zahlenvergleich aller 113
Zeilen über gegeben, gesucht, stichwoerter, verfahren, ergebnis; einzige
Treffer sind die vier schon bekannten Zeilen 2018-bb-ea A1.1 a, b und A1.2
a, b (Pool 2018 erhöht Teil A). Kein weiterer Treffer, auch nicht bei
niedriger Schwelle (sechs Kandidatenpaare gesichtet, alle verschieden). Das
ist erwartbar: Der erfasste Pool deckt Teil A 2018–2026 und Teil B
2022–2026, die Landeshefte 2017/2018 konnten nur aus Pool 2017 (Teil A und
B) und Pool 2018 (Teil A und B) schöpfen – Pool 2017 und Teil B 2018 sind
Reserve. (2) Deshalb zusätzlich gegen die 49 nicht erfassten Pooldateien
2017 (Teil A und B, WTR) und 2018 Teil B (WTR), Text mit pypdf aus den
PDFs, Vergleich je Aufgabe, Treffer von Hand am Wortlaut geprüft:

| Heft | Aufgabe | Poolaufgabe (nicht erfasst) | Befund |
|---|---|---|---|
| 2017-bb-ea | Teil 1 Analysis (A1.1 a, b) | 2017 erhöht A Analysis 1.1 a, b | wortgleich (Zahlen, Aufträge, BE 2 + 3) |
| 2017-bb-ea | Teil 1 Geometrie (A1.2 a, b) | 2017 erhöht A AG/LA (A2) 2 a, b | wortgleich (2 + 3) |
| 2017-bb-ea | Teil 1 Stochastik (A1.3 a, b) | 2017 erhöht A Stochastik 2 a, b | wortgleich (2 + 3) |
| 2017-bb-ea | Teil B 2.1–4.2 | – | kein Treffer in 2017 erhöht/grundlegend Teil B |
| 2018-bb-ea | Teil 1 Stochastik (A1.3) | – | nicht im Pool 2018 (die anderen zwei Aufgaben des Teils 1 sind Pool, Lauf 12) |
| 2018-bb-ea | Teil B 2.1–4.2 | – | kein Treffer in 2018 erhöht Teil B |
| 2018-be-gk | 2.2 Kletteranlage (a–e) | 2018 grundlegend B AG/LA (A2) WTR 2 a–e | wortgleich, 20 von 20 BE (die erhöhte Fassung WTR 2 hat dieselben a–d, andere e/f) |
| 2018-be-gk | 3.2 Bildschirme b, c, d | 2018 grundlegend B Stochastik WTR 2 b, c, d | wortgleich (2 + 3 + 4 BE) |
| 2018-be-gk | 3.2 a | 2018 grundlegend B Stochastik WTR 2 a | abgewandelt: Ereignis B mit 50 statt 200 Bildschirmen (4 BE) |
| 2018-be-gk | 3.2 e | 2018 erhöht B Stochastik WTR 2 b | abgewandelt: Netzteil-Anteil 3,0 % vorgegeben statt „entweder–oder 11,7 %“ (3 statt 4 BE) |
| 2018-be-gk | 3.2 f | (2018 erhöht B Stochastik WTR 2 c) | Landesvariante: bedingte Wahrscheinlichkeit statt Unabhängigkeit, kein Vermerk |
| 2018-be-gk | 3.2 g | 2018 erhöht B Stochastik WTR 2 d | wortgleich (2 BE) |
| 2018-be-gk | 1.1, 1.2, 2.1, 3.1 | – | kein Treffer in 2018 grundlegend/erhöht Teil B |

Verweise: Die 15 wortgleichen Zeilen tragen seit Lauf 14 die Vorstufe
„Poolaufgabe (nicht erfasst): <voraussichtliche iqb-id>." (abi.md § 7), die
zwei abgewandelten „(nicht erfasst, abgewandelt)" mit dem Unterschied. Der
Verweis nach Entscheidung 3 („Dublette von:") setzt eine erfasste Poolzeile
voraus – abi-bau.py prüft ihn gegen iqb-katalog.csv und verlangt denselben
typ; die betroffenen Stapel 2017-ea-A (11 Dateien), 2018-ga-B-wtr (6) und
2018-ea-B-wtr (7) sind Reserve. Wird einer davon erfasst, meldet iqb-bau.py
die vorgemerkten Zeilen, und ein Abgleichlauf stellt den Vermerk um und
gleicht die Typen ab. Ob die Reserve dafür geöffnet wird, entscheidet der
Lehrer; ohne Erfassung bleiben die Poolzeilen ohne Erwartungshorizont und
Standardbezug im abi-Katalog, was für die Eichung nichts ändert (Landeshefte
bis 2018 haben ohnehin keinen amtlichen Bereich).

*Poolquote je Heft* (abi-bau.py v0.5, Selbstprüfung; wortgleich = erfasst
oder vorgemerkt, angebotene BE):

| Heft | Zeilen im Pool | BE im Pool (angeboten) | davon hilfsmittelfreier Teil | abgewandelt |
|---|---|---|---|---|
| 2017-bb-ea | 6 von 36 | 15 von 185 (8 %) | 15 von 15 (100 %) | – |
| 2018-bb-ea | 4 von 41 | 10 von 185 (5 %) | 10 von 15 (67 %) | – |
| 2018-be-gk | 9 von 36 | 31 von 160 (19 %) | kein hilfsmittelfreier Teil | 2 Zeilen, 7 BE (mit ihnen 38 von 160, 24 %) |
| 2023-bebb-gk | 11 von 58 | 30 von 185 (16 %) | 10 von 35 (29 %) | – |

Muster: Brandenburg erhöht (2017, 2018) nimmt den Pool nur im
hilfsmittelfreien Teil 1 – 2017 ganz, 2018 zwei der drei Aufgaben – und
schreibt Teil B selbst (0 von 170 BE). Berlin grundlegend 2018 hat keinen
hilfsmittelfreien Teil und nimmt stattdessen zwei Teil-B-Aufgaben aus dem
grundlegenden Pool, eine wortgleich (Kletteranlage), eine aus beiden
Niveaus zusammengesetzt und leicht verändert (Bildschirme); im Wahlweg
2.2/3.2 sind das 38 von 80 zu bearbeitenden BE, im Wahlweg 2.1/3.1 null. Das
gemeinsame Heft 2023 mischt: zwei von sieben Aufgaben des hilfsmittelfreien
Teils und zwei Drittel einer Teil-B-Aufgabe. Die Quote nach angebotenen BE
liegt also 2017 bis 2023 zwischen 5 % und 19 %, ohne Trend über die Jahre;
was schwankt, ist die Stelle, an der der Pool eingesetzt wird (Teil 1 bei
bb-ea, Teil B bei be-gk, beides 2023). Die 2018 nahe 100 % vom 15.09.2026
galten nur für den hilfsmittelfreien Teil. Mit vier Heften ist das eine
Beobachtung, keine Statistik.

*Etiketten der 17 Zeilen nach dem gemeinsamen Schnitt:* keine, die falsch
läge – Thema, Klasse und Handlung passen zu Aufgabe und Lösungsweg. Sieben
der 17 tragen Typen, die auch der iqb-Katalog verwendet (Gleichschenkligkeit
des Achsendreiecks der Tangente, Erwartungswertbedingung, Trapez,
Neigungswinkel, Punktprobe, kumulierte Binomialwahrscheinlichkeit,
Vierfeldertafel), zehn abi-eigene Typen (Nullstelle einer
Exponentialfunktion durch Logarithmieren; Dreiecksfläche aus Spurpunkten;
Normalenvektor als Ortsvektor; Umlegen zwischen Urnen; Streckenlänge im
Raum; Lösungsweg für einen Punkt auf einer Geraden; Modalwert;
Stichprobenvergrößerung; Trefferwahrscheinlichkeit aus der Bedingung an null
Treffer; Ungeeignetheit des Binomialmodells). Diese zehn sind gegen die
Poolzeile abzugleichen, sobald ihr Stapel erfasst ist – erst dann gibt es
ein zweites Etikett für dieselbe Aufgabe, und der Abgleichlauf entscheidet.
Bis dahin ist nichts zu ändern: Ein abi-eigener Typ ist kein falsches
Etikett, solange kein Zwilling im Bestand steht.

**Umstellungslauf 12 – gemeinsame Typenliste für abi und iqb (Entscheidung
25, Auftrag „Weg A umsetzen", 15.09.2026).** Grundlage abi-iqb-typen.md
(Messung vom selben Tag). Zwei Commits: erst abitur-vokabular.md, abgleich.py
v0.12 (vorher iqb-abgleich.py), abi-bau.py v0.3, iqb-bau.py v1.0 und die
Dokumente; dann der Lauf.

*Typenliste.* Vorher iqb-typen.csv 792 und abi-typen.csv 146 (zusammen 938),
nachher abitur-typen.csv 875: 63 abi-Typen sind in iqb-Typen aufgegangen –
50 inhaltsgleiche mit anderem Namen (Klasse a), 2 mit gleichem Namen
(Baumdiagramm zu einer zweistufigen Situation erstellen; Stammfunktion durch
Ableiten nachweisen), 11 überlappende Paare mit erweiterter Definition (M1–M11
unten); dabei drei iqb-Typen umbenannt (Umfang des Dreiecks aus Tangente und
Koordinatenachsen → Flächeninhalt oder Umfang …; Laplace-Wahrscheinlichkeit
für den ersten Zug → … als Anteil der günstigen Fälle angeben; Nullstelle oder
Schnittstelle mit einer waagerechten Geraden durch Einsetzen → Punkt,
Nullstelle oder Schnittstelle durch Einsetzen nachweisen). 15 abi-Typen in
Klassen-Themen tragen jetzt den Präfix, 2 haben das Thema gewechselt (Graphen
einer Funktion in ein vorgegebenes Koordinatensystem einzeichnen →
Kurvenuntersuchung; Existenz eines Geradenschnittpunkts über die gemeinsame
Ebene begründen → Geraden). 83 abi-Typen stehen ohne iqb-Verwendung in der
Liste (55 aus Klasse b, 27 aus c, dazu Nr. 134), 56 Typen
werden in beiden Katalogen verwendet, 736 nur in iqb. Zehn (a)-Ziele
bekamen eine erweiterte Definition, weil sie den abi-Fall noch nicht nannten
(Polynom statt x vor der e-Funktion, zweite Ableitung, f(−x) neben der
Parität der Exponenten, Wertemenge und Steigung „wenn verlangt", Normale in
einem Graphenpunkt, Trapezfläche „wenn verlangt", totale Wahrscheinlichkeit,
Hochpunkt über die notwendige Bedingung).

*Umetikettiert.* abi-katalog.csv: 98 Typfelder in 75 von 113 Zeilen (dazu die
vier Dublettenverweise unten, alle in diesen 75); iqb-katalog.csv: 5
Typfelder in 5 Zeilen (die drei Umbenennungen). Zusammen 80 Zeilen, unter
der Haltemarke von 100. Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung
beider Bau-Skripte bestanden (abi 113 Zeilen, iqb 1061 Zeilen, 875 Typen,
alle verwendet, 29 Stapel vollständig).

*Schnittwerte.* Gemeinsamer Bestand nach dem Lauf: 189 Werte nach dem Thema
der Zeile (iqb 180, abi 61, Schnitt 52), davon 153 in be-gk und 176 in bb-ea;
nach dem Thema des Typs, das nach abitur-vokabular.md § 4 die Klasse trägt,
183 (iqb 178, abi 58). Von den 8 neuen abi-Werten der Messung bleiben 5:
Extremalprobleme · zeichnen, Linearkombination und lineare Abhängigkeit ·
begründen, Rotationsvolumen · berechnen, Rotationsvolumen · zeichnen (beide
außerhalb be-gk), Ziehen ohne Zurücklegen · begründen; die drei Werte mit
offener Klasse sind durch die Klassenentscheidungen in vorhandene Werte
gefallen. Nach dem Thema der Zeile zählt die Messung vier weitere,
scheinbar neue Werte (etwa Orthogonalität · Ebene Figur · begründen), die
nur daher rühren, dass 13 abi-Zeilen und 8 iqb-Zeilen ein anderes Thema
tragen als ihr Typ – die Bau-Skripte messen den Schnitt bisher mit dem
Zeilenthema. Nicht geändert; Vorschlag: den Schnitt in beiden Skripten auf
das Thema des Typs stellen.

*Die vier Klassenentscheidungen.* (1) Definitionsbereich einer
Logarithmusfunktion angeben → Klasse „Nullstellen und Werte", Lesart in
abitur-vokabular.md § 4 um Definitions- und Wertemengen erweitert (iqb führt
Wertemengen schon dort); keine neue Klasse. (2) Graphen einer Funktion in
ein vorgegebenes Koordinatensystem einzeichnen → Thema Kurvenuntersuchung
(ohne Klassen), wie „Graphen zu vorgegebenen Nullstellen, Extrem- und
Wendestellen skizzieren" in iqb. (3) Existenz eines Geradenschnittpunkts über
die gemeinsame Ebene begründen → Thema Geraden, wo iqb Lagen zweier Geraden
führt; Lagebeziehungen bleibt bei Punkt/Gerade gegen Ebene. (4) Eckpunkt
eines Quadrates nachweisen → in den iqb-Typ „Ebene Figur: Benachbarte Ecke
eines Quadrats über den Diagonalenschnittpunkt als Spurpunkt nachweisen"
aufgegangen (M11) – es ist dieselbe Aufgabe (2018-bb-ea A1.2b = Pool 2018
AGLAA22 b), Thema Punkte und Strecken.

*(b)-Zusammenziehungen M1–M11* (Definition jeweils erweitert): M1
Parameterwert einer Schar aus einer Funktionswertbedingung exakt bestimmen →
Scharparameter aus einem Punkt des Graphen angeben; M2 Art eines
Extrempunktes über den Vorzeichenwechsel der ersten Ableitung begründen →
Extrempunkt an vorgegebener Stelle nachweisen (beide Wege, wie Lauf 6 bei
der Unabhängigkeit); M3 Parabelgleichung aus Symmetrie und einer
Flächenbedingung rekonstruieren → Scharparameter aus einer Nullstelle und
einem Flächeninhalt bestimmen; M4 Flächeninhalt des Achsenabschnittsdreiecks
einer Tangente → Flächeninhalt oder Umfang des Dreiecks aus Tangente und
Koordinatenachsen berechnen (wie Lauf 11: das Maß steht in der Zeile); M5
Lage eines Punktes auf einer Strecke über die Parameterform nachweisen →
Punktprobe an einer Geraden durchführen; M6 Mittelpunkt eines Quadrates als
Diagonalenmittelpunkt → Punkt: Mittelpunkt einer Strecke im Raum bestimmen
(abi-intern); M7 Wahrscheinlichkeit eines Intervalls als Differenz
kumulierter Werte → Kumulierte Binomialwahrscheinlichkeit mit dem Rechner
ermitteln; M8 Wahrscheinlichkeit aus den Sektorwinkeln eines Glücksrads →
Laplace-Wahrscheinlichkeit als Anteil der günstigen Fälle angeben; M9
Wahrscheinlichkeit für den ersten Treffer bei der k-ten Wiederholung →
Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt
berechnen; M10 Punktprobe mit gerundeten Koordinaten → Nullstellen und Werte:
Punkt, Nullstelle oder Schnittstelle durch Einsetzen nachweisen; M11 wie
oben. **Abweichung vom Auftrag:** statt der in der Messung geschätzten „rund
25" sind es elf. Beim Prüfen jedes Paars nach Kern § 6 erwiesen sich die
Bündelungsfälle (Ursache 1 der Messung) als nicht zusammenziehbar, ohne die
Leistung einer Zeile zu ändern – ein abi-Typ, der nur die Nebenleistung
trägt (Maßstab, Streckenlänge, Mittelpunkt), kann nicht in einen iqb-Typ
aufgehen, der die ganze Teilaufgabe meint; und die Kurzaufgabe-gegen-Kette-
Fälle (Ursache 2) unterscheiden sich in der Handlung, also im Schnitt.
Zusätzlich wurde Nr. 134 (Wahrscheinlichkeit für wenigstens einen Treffer
über das Gegenereignis) von (a) nach (b) zurückgestuft und nicht
zusammengezogen: das iqb-Gegenstück meint das Komplement (kein Abbruch in n
Wiederholungen), das nächste iqb-Etikett ist auf zwei Stufen festgelegt.

*Strittige (b)-Paare, getrennt gelassen (je eine Zeile):* Nr. 25 Graphen
einer Schar beschriften – iqb trennt nach Lösungsweg (y-Achsenabschnitt,
Spiegelung), der abi-Typ nennt keinen; Nr. 30 Nullstelle einer
Exponentialfunktion durch Logarithmieren – das iqb-Etikett bündelt den
Anfangswert, eine abi-Zeile ohne ihn passte nicht unter den Namen; Nr. 44
Lage und Art aller lokalen Extrempunkte bestimmen – iqb kennt nur
„Extremstellen berechnen und Monotonieverhalten angeben", andere Leistung;
Nr. 74 Abstand Punkt–Ebene mit der Hesseschen Normalform – Lösungsweg, den
der Pool nicht benutzt; Nr. 88 Pyramidenvolumen aus Grundfläche und Höhe –
ein allgemeines Etikett würde drei spezialisierte iqb-Typen schlucken, das
ist eine Abgleichentscheidung über iqb-Zeilen, nicht über abi; Nr. 96
Orthogonalität zweier Ebenen nachweisen gegen Parameter bestimmen – wie
beim rechten Winkel mit Parameter in iqb getrennt gehalten; Nr. 127
Mindestanzahl über das Gegenereignis durch Logarithmieren gegen Probieren am
Rechner – Lösungsweg; Nr. 138 Erwartungswert einer Zufallsgröße im
Sachzusammenhang berechnen – der Pool fragt ihn nie allein, der abi-Typ ist
der Grundtyp und bleibt.

*Pool-Teilaufgaben in Landesheften (Entscheidung 3 des Auftrags).* Regel in
abi.md § 7 und iqb.md § 7; abi-bau.py prüft „Dublette von: <iqb-id>" gegen
iqb-katalog.csv und verlangt denselben typ. Ein Feld dublette_von gibt es im
Kern nicht (37 Felder, Schema-Version 2); die Markierung in bemerkung ersetzt
es, eine Schemaänderung wäre eine am Kern und ist nicht gemacht. Beim
Zusammenziehen fiel auf, dass der hilfsmittelfreie Teil 2018-bb-ea die
Poolaufgaben 2018 erhöht Analysis 2 und AG/LA A2 2 wortgleich stellt (gleiche
Zahlen, Aufträge, BE; die Stochastik-Aufgabe stammt aus dem Heft 2016): die
vier Zeilen 2018-bb-ea A1.1a, A1.1b, A1.2a, A1.2b tragen seit Lauf 12 den
Verweis (Feldkorrektur bemerkung, innerhalb der 75 Zeilen). 2017-bb-ea Teil 1
ist nicht prüfbar, weil der Pool 2017 erhöht Teil A Reserve ist.

*Beim Verschieben des Vokabulars aufgefallen* (abitur-vokabular.md § 7): abi.md
führte 46 Themen, iqb.md 49; abi.md nannte Wurzelgleichungen als nur erhöht,
die Berliner Schwerpunkte 2027 verlangen sie im GK; die Geltungstabelle stand
in iqb.md, beschreibt aber die Zielprüfungen des Profils abi; die Lücken aus
abi.md § 6 (Maßstab, Streckenlänge, Geschwindigkeit, Zeichnen, Punkt in
Entfernung) sind im Pool längst unter Themen abgelegt. Zum Kern
(katalog-prompt.md), nicht verschoben, sondern gemeldet: § 5 „Die Werte für
… leitidee und thema kommen aus dem Profil" und § 6 „Leitidee und Thema
sind fest und stehen im Profil" – für abi und iqb stehen sie jetzt in
abitur-vokabular.md, das Profil verweist darauf; § 6 „Änderungen an
bestehenden Etiketten schlägst du im Bericht vor und führst sie nicht selbst
aus" ist seit den Abgleichläufen durch CLAUDE.md überschrieben (Skript mit
Regeln, Liste alt → neu); die Handlungsklassen (format → Handlung) gehören
inhaltlich neben Kern § 5, stehen aber im Vokabular; der Kern-Standardname
„typen.csv" ist vom Profil msa belegt, deshalb abitur-typen.csv. Nichts
davon verändert den Kern. *(Nachtrag 16.09.2026: Kern v0.4 zieht die drei
Punkte nach, siehe unten.)*

**Themenfeld bereinigen – Abgleichlauf 13 (Auftrag des Lehrers, 16.09.2026,
Entscheidung 26; abgleich.py v0.13, abi-bau.py v0.4, iqb-bau.py v1.1,
abitur-vokabular.md v1.1, Kern v0.4).** Anlass: 21 Zeilen (13 abi, 8 iqb)
trugen ein anderes Thema als ihr Typ; die Skripte zählten den Schnitt mit dem
Zeilenthema, also 189 statt 183 Werte im Gesamtbestand. Regel seitdem:
Zeilenthema = Typthema, geprüft in beiden Bau-Skripten (neue Zeilen und
Bestand) und in abgleich.py nach jedem Lauf; der Schnitt wird über das Thema
des Typs gemessen.

*Die 21 Fälle mit Entscheidung* (Z = Zeile folgt dem Typ, T = Typ wechselt das
Thema, Zeilen folgen):

| Zeile | Zeilenthema bisher | Typ (Thema des Typs) | Entscheidung |
|---|---|---|---|
| 2018-bb-ea-A1.2b | Orthogonalität | Ebene Figur: Benachbarte Ecke eines Quadrats … (Punkte und Strecken) | Z – Quadratfragen liegen laut Lesart § 4 unter Punkte und Strecken; die iqb-Zeile derselben Aufgabe steht dort |
| 2018-bb-ea-B2.1b | Funktionsscharen und Ortskurven | Nullstellen und Werte: Schnittpunkt mit der y-Achse und Steigung … (Funktionsklassen) | Z – erste Leistung ist der y-Achsenschnitt, die Schar ist Kontext; Scharparameter steht in typ_neben |
| 2018-bb-ea-B2.1d | Kurvenuntersuchung | Parameterwerte nach der Anzahl der Extrempunkte … (Funktionsscharen) | Z – Parameterbereiche einer Schar |
| 2018-bb-ea-B3.2c | Linearkombination und lineare Abhängigkeit | Lage eines Punktes zu einem Vektorterm im Quader beschreiben (Vektoren und Rechenoperationen) | Z – Ortsvektorterm auswerten, keine Frage nach Darstellbarkeit oder Abhängigkeit |
| 2018-bb-ea-B4.1c | Binomialverteilung | Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben (Zufallsexperimente) | Z – wie zwölf iqb-Zeilen desselben Typs; der Binomialterm ist Gegenstand, nicht Thema |
| 2017-bb-ea-B2.1e | Rekonstruktion von Funktionsgleichungen | Scharparameter aus einer Nullstelle und einem Flächeninhalt bestimmen (Funktionsscharen) | Z – Zusammenziehung M3 aus Lauf 12; die Zeile hätte dort schon folgen müssen |
| 2017-bb-ea-B2.2e | Analysis / Gleichungen lösen | Punkt auf einer Geraden mit vorgegebenem Abstand zum Aufpunkt bestimmen (Analytische Geometrie / Geraden) | Z – auch leitidee wechselt: gleiche Fertigkeit wie 2019-ga-A AGLAA22 a (Richtungsvektor normieren, Vielfaches ansetzen); die Teilaufgabe steht in der Analysis-Aufgabe Straßenverlauf, Vermerk in bemerkung. Strittig: die einzige Zeile, bei der das Sachgebiet der Aufgabenstellung vom Typ abweicht |
| 2017-bb-ea-B4.2a | Zufallsgrößen und Verteilungen | Pfadwahrscheinlichkeit einer vorgegebenen Ergebnisfolge als Produkt berechnen (Baumdiagramm) | Z – bemerkung sagte selbst „thema folgt dem ersten Typ"; dazu stand der Typ noch einmal in typ_neben (gestrichen) |
| 2017-bb-ea-B4.2c | Bedingte Wahrscheinlichkeit und Bayes | Fehlenden Anteil im Baumdiagramm aus einer Randwahrscheinlichkeit berechnen (Baumdiagramm) | Z – Pfadsumme gleich Randwahrscheinlichkeit ist Pfadregel, keine Bedingung; drei iqb-Zeilen liegen dort |
| 2018-be-gk-B1.2f | Ableitung und Änderungsrate | Kleinste Tangentensteigung über das Minimum der Ableitung bestimmen (Tangente, Normale, Schnittwinkel) | T → Ableitung und Änderungsrate – die Fertigkeit ist der Extremwert von f′ (Gefälle größer als 22,2 %); die Tangente ist nur die Wortwahl der Poolaufgabe. iqb-Zeile 2019MgrundlegendAAnalysis12-b folgt |
| 2018-be-gk-B2.1c | Lagebeziehungen | Existenz eines Geradenschnittpunkts über die gemeinsame Ebene begründen (Geraden) | Z – Klassenentscheidung (3) aus Lauf 12, Zeile war nicht nachgezogen |
| 2018-be-gk-B2.2b | Punkte und Strecken im Koordinatensystem | Ebene Figur: Trapez über parallele Seiten nachweisen und Flächeninhalt berechnen (Flächeninhalt und Volumen im Raum) | T → Punkte und Strecken – die feste Leistung ist der Nachweis über kollineare Seitenvektoren, der Flächeninhalt kommt „wenn verlangt" (die abi-Zeile verlangt ihn nicht); Klasse Ebene Figur gibt es in beiden Themen, kein Umbenennen. iqb-Zeile 2026MgrundlegendBAGLAA2WTR2-1a folgt |
| 2018-be-gk-B3.1e | Zufallsexperimente und Urnenmodelle | Unbekannte Größe aus einer Erwartungswertbedingung bestimmen (Kenngrößen von Verteilungen) | Z – elf Zeilen desselben Typs liegen unter Kenngrößen |
| 2025MgrundlegendAAGLAA221-b | Spiegelung | Punkt mit vorgegebenem Abstand zur Ebene auf der Lotgeraden bestimmen (Abstände) | Z – der Spiegel ist Kontext, gerechnet wird der Abstand auf der Lotgeraden wie in 2026-ea-A und 2024-ea-A |
| 2025MgrundlegendAStochastik13-b | Hypergeometrische Verteilung | Term und Ereignis: Ereignis zu einem gegebenen Wahrscheinlichkeitsterm beschreiben (Zufallsexperimente) | Z – Vermerk „Erste Fundstelle des Themas Hypergeometrische Verteilung" ersetzt; das Thema behält vier Zeilen mit zwei eigenen Typen |
| 2025MgrundlegendAStochastik22-b | Zufallsexperimente und Urnenmodelle | Unbekannte Größe aus einer Erwartungswertbedingung bestimmen (Kenngrößen) | Z – wie 2018-be-gk-B3.1e |
| 2025MerhoehtAAGLAA221-a | Scharen von Geraden und Ebenen | Punktprobe an einer Geraden durchführen (Geraden) | Z – bemerkung nannte selbst „gleicher Lösungsweg, hier mit Scharparameter"; Vermerk angepasst. Folge: die Zeile gilt jetzt auch für be-gk und bb-gk |
| 2026MgrundlegendBStochastikWTR1-1a | Binomialverteilung | Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen (Kombinatorik) | T → Zufallsexperimente und Urnenmodelle mit Präfix „Term und Ereignis:" – das Ergänzen eines Terms ist Aufstellen eines Wahrscheinlichkeitsterms (Lesart § 4), ob mit Binomialkoeffizienten oder Anordnungszahl; Kombinatorik als Thema hätte für die beiden Binomialterme nicht gestimmt. Beispielzeile 2026MerhoehtAStochastik21-b folgt |
| 2022MerhoehtBStochastikWTR1-1e | Binomialverteilung | dito | T, wie oben |
| 2025MerhoehtBStochastikWTR2-2b | Bedingte Wahrscheinlichkeit und Bayes | Verhältnis zweier Pfadwahrscheinlichkeiten im Baumdiagramm prüfen (Baumdiagramm) | Z – zwei Pfade berechnen und vergleichen, keine Bedingung |
| 2025MerhoehtBStochastikWTR3-2b | Bedingte Wahrscheinlichkeit und Bayes | dito | Z, wortgleich mit WTR 2 2b |

Bilanz: 18 Zeilen folgen ihrem Typ, drei Typen wechseln das Thema (mit drei
weiteren iqb-Zeilen, die ihnen folgen), ein Präfix, keine Umbenennung
sonst, 875 Typen unverändert. Feldkorrektur in 23 Zeilen (21 + zwei
iqb-Zeilen der gewechselten Typen; 2018-be-gk-B1.2f und B2.2b behalten ihr
Zeilenthema, weil der Typ zu ihnen kommt) und zusätzlich 2018-be-gk-B3.2a,
wo der Typ ebenfalls doppelt in typ_neben stand – 24 Zeilen berührt. Fünf
Vermerke in bemerkung angepasst.

*Schnittwerte.* Gesamtbestand nach Lauf 13: 183 Werte (be-gk 149, bb-ea
170), iqb allein 178 (146, 165), abi 58, davon 5 nicht im Pool. Vorher 189
nach Zeilenthema und 183 nach Typthema – die sechs Werte Unterschied waren
genau sechs Phantomwerte, die nur das Zeilenthema erzeugte (Binomialverteilung
× Term und Ereignis × angeben; Funktionsscharen × Nullstellen und Werte ×
angeben; Hypergeometrische Verteilung × Term und Ereignis × angeben;
Lagebeziehungen × – × begründen; Orthogonalität × Ebene Figur × begründen;
Zufallsexperimente × – × berechnen); umgekehrt gab es keinen Wert, den nur
das Typthema kannte. Die Wertemenge nach Lauf 13 ist genau die Menge nach
Typthema vor dem Lauf – die drei Typwechsel haben keinen Wert erzeugt oder
gelöscht, weil ihre Zielwerte schon belegt waren. Nach der Bereinigung gibt
es nur noch eine Zählweise.

*Abbruchentscheidungen Teil B nachgerechnet* (schnitt_teilb2.py im
Scratchpad, Erfassungsreihenfolge, neu im Bestand innerhalb der Geltung,
Zielprüfung des Niveaus): grundlegend 7 / 3 / 2 / 2 (2026-, 2025-, 2024-,
2023-ga-B), erhöht 9 / 0 / 7 / 4 / 3 (2026-, 2025-, 2024-, 2023-, 2022-ea-B)
– Zeile für Zeile identisch mit der Reihe vom 14./15.09.2026, keine
Entscheidung kippt; auch die Reihe nach Typthema auf dem alten Stand war
schon dieselbe – beide Zählweisen liefern für jeden Teil-B-Stapel dieselben
Zahlen. Zur Kontrolle auch mit den abi-Zeilen als Vorbestand gerechnet (was
die Reihe nie tat): 5 / 2 / 2 / 2 und 6 / 0 / 6 / 3 / 3 – dieselben Stapel
über und unter fünf.

*Kern v0.4 (Punkt 3 des Auftrags).* Kopf: ein Profil darf sein Vokabular in
eine Datei auslagern, mehrere Profile dürfen sie und eine Typenliste teilen,
„im Profil" meint dann diese Datei. § 5: Tabelle format → Handlung (aus
abitur-vokabular.md § 5 hierher, das Vokabular verweist nur noch; beide
Bau-Skripte lesen sie jetzt aus dem Kern); Absatz „Markierungen in
bemerkung" („Dublette von: <id>." und „Traegerbindung: Kontext", kein
eigenes Feld). § 6: Leitidee und Thema „im Profil oder in der
Vokabulardatei"; ob das Zeilenthema dem Typthema folgen muss, regelt das
Profil (abi/iqb gleich, fhr Punkt-Schwerpunkt); Etikettenänderungen gehören
nicht in den Heftlauf, sondern werden im Abgleichlauf (§ 9) per Skript
ausgeführt. § 9 entsprechend. Schema-Version 2 unverändert, keine
Feldänderung. **msa und fhr unberührt:** fhr-bau.py und
fhr-typenbibliothek.py lesen katalog-prompt.md nicht (nur Versionsvermerk im
Kopf), msa hat kein Skript; die Formliste in § 5 steht unverändert im selben
Klammerausdruck; fhr.md § 6 behält seine Regel, dass thema bei mehrleistigen
Zeilen dem Punkt-Schwerpunkt folgt – der Kern verweist jetzt ausdrücklich
darauf; keine msa-/fhr-Datei geändert.

*dublette_von (Punkt 4).* Befund: ein Katalogfeld dublette_von gibt es
nirgends – nicht im Kern (37 Felder), nicht in einem Katalog. Das Wort
bezeichnet allein eine Spalte von iqb-quellen.csv (Datei zeigt auf
wortgleiche Datei, keine Zeile). Der Zeilenverweis einer Pool-Teilaufgabe im
Landesheft ist die Markierung „Dublette von: <iqb-id>." in bemerkung. So
stand es schon in abi.md § 7 und hier oben; iqb.md § 7 und CLAUDE.md § 4
nannten die Spalte ohne die Abgrenzung, der Kern nannte gar nichts. Jetzt
sagen Kern § 5, abi.md § 7, iqb.md § 7, CLAUDE.md § 2/§ 4 und dieser Eintrag
dasselbe.

## 5 Änderungslog

| Datum | Änderung |
|---|---|
| 2026-09-16 | Kennzahl Poolquote je Heft: Spalte „Pool (Zeilen; BE angeboten)“ in der Kennzahlentabelle § 2, Zeilen für 2017-bb-ea, 2018-be-gk und 2018-bb-ea ergänzt (Selbstprüfung abi-bau.py v0.5 gibt sie je Heft aus); Gegenstück „in Landesheften“ je Stapel in iqb-pruefungen.md § 2 (iqb-bau.py v1.2). Selbstprüfung beider Skripte bestanden. |
| 2026-09-16 | Pool-Abgleich des Bestands bis 2018 (Abgleichlauf 14, abgleich.py v0.14): gegen den erfassten Pool keine weiteren Treffer; gegen die nicht erfassten Pooldateien 2017 (A, B) und 2018 (B) 15 wortgleiche Zeilen (2017-bb-ea Teil 1 ganz = Pool 2017 erhöht A; 2018-be-gk 2.2 a–e = Pool 2018 grundlegend B AG/LA (A2) WTR 2; 3.2 b, c, d, g = Pool 2018 Stochastik WTR 2 ga/ea) und 2 abgewandelte (3.2 a, e) – Vermerk „Poolaufgabe (nicht erfasst[, abgewandelt]): <id>“ in bemerkung (Feldkorrektur, 17 Zeilen), Regel in abi.md § 7 (v0.10), iqb.md § 7 (v1.4), Kern § 5; abi-bau.py v0.5 prüft den Vermerk und gibt die Poolquote je Heft aus. Typen unverändert (913). Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung beider Skripte bestanden. Tabelle, Quoten und Muster in § 4. |
| 2026-09-16 | 2023-bebb-gk 2.2 k nachgeprüft (Scan in voller Auflösung): drei Eigenschaften I k(0) = 20, II k′(0) = 130, III Hochpunkt H(5 \| 220) – Erfassung stimmt, Widerspruch im Heft (H ist Tiefpunkt der eindeutig bestimmten Funktion) bleibt vermerkt. Keine Katalogänderung. |
| 2026-09-16 | Heft 2023-bebb-gk erfasst (Stark-Scan, abi-bau.py v0.4): 58 Zeilen aus 12 Aufgaben, Katalog 171 Zeilen, Typenliste 913 (38 neu, 19 iqb-Typen übernommen), 11 Pool-Dubletten mit „Dublette von:“ (30 von 185 BE). Alle Punktsummen geprüft, Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung beider Skripte bestanden. Eichung 11 von 11 (nur Poolzeilen), 3 Zeilen mit „?“ (Ablesewerte), 0 ersatzweise, 8 kontextgebunden; Schnitt 42 Werte, 1 neu im Gesamtbestand (184). Skriptanpassung: Pool-Kennungen vom ASCII-Minus-Test ausgenommen. Befunde in § 4. |
| 2026-09-16 | Abgleichlauf 13 (abgleich.py v0.13, Entscheidung 26 „Themenfeld bereinigen"): Zeilenthema = Typthema. abi-katalog.csv: 11 Zeilen leitidee/thema aus dem Typ (2018-bb-ea A1.2b, B2.1b, B2.1d, B3.2c, B4.1c; 2017-bb-ea B2.1e, B2.2e [auch leitidee], B4.2a, B4.2c; 2018-be-gk B2.1c, B3.1e), 2 Zeilen behalten ihr Thema, weil der Typ wechselt (2018-be-gk B1.2f: „Kleinste Tangentensteigung …" → Ableitung und Änderungsrate; B2.2b: „Ebene Figur: Trapez …" → Punkte und Strecken); doppelte Nennung des typ in typ_neben gestrichen (2017-bb-ea B4.2a, 2018-be-gk B3.2a); Vermerke in bemerkung (B4.2a, B2.2e). iqb: 8 Zeilen plus 3 Folgezeilen, ein Präfix („Term und Ereignis: Fehlende Werte in einem Wahrscheinlichkeitsterm bestimmen", Zufallsexperimente). Typen 875 unverändert; Schnitt 183 Werte (vorher 189 nach Zeilenthema), Teil-B-Reihen unverändert. abi-bau.py v0.4, iqb-bau.py v1.1 (Assert, Schnitt über Typthema, Handlungen aus dem Kern), Kern v0.4, abitur-vokabular.md v1.1, abi.md v0.9, iqb.md v1.3, konzept.md Entscheidung 26. Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung beider Skripte bestanden. |
| 2026-09-15 | Umstellungslauf 12 (abgleich.py v0.12, Entscheidung 25): abi-typen.csv und iqb-typen.csv → abitur-typen.csv (938 → 875 Typen); 50 abi-Typen in inhaltsgleiche iqb-Typen aufgegangen, 2 gleichnamig, 11 überlappende Paare zusammengezogen (M1–M11, drei iqb-Umbenennungen), 15 Präfixe, 2 Themenwechsel; abi-katalog.csv 98 Typfelder in 75 Zeilen umetikettiert, iqb-katalog.csv 5 Typfelder in 5 Zeilen; Feldkorrektur „Dublette von:“ in 4 Zeilen (2018-bb-ea Teil 1 = Pool 2018 erhöht). Lauf aus dem HEAD-Stand byteidentisch, Selbstprüfung beider Bau-Skripte bestanden. Bericht mit Klassenentscheidungen und strittigen Paaren in § 4. |
| 2026-09-15 | Weg A vorbereitet (Entscheidung 25): abitur-vokabular.md v1.0 (Sachgebiete, Themenliste, Geltungstabelle, Gegenstandsklassen, Handlungen, Rechnerfassung – aus iqb.md und abi.md, Abweichungen in § 7); abgleich.py v0.12 (vorher iqb-abgleich.py, zwei Kataloge, Lauf 12); abi-bau.py v0.3 auf dem Stand von iqb-bau.py v1.0 (Präfixregel, Schwellen, Eichung, Vollständigkeit, Dublettenverweis, Trägerbindung, Kennzahlen; Zeilenblock geleert); iqb-bau.py v1.0 (Vokabular aus abitur-vokabular.md, gemeinsame Typenliste, Zeilenblock geleert); abi.md v0.8, iqb.md v1.2, CLAUDE.md, konzept.md Entscheidung 25, README.md. Katalog und Typen unverändert; läuft erst mit dem Umstellungslauf. |
| 2026-09-15 | Typenlisten abi und iqb verglichen (Messung, nichts geändert): abi-iqb-typen.md – 146 abi-Typen gegen 792 iqb-Typen, Klassen (a) 53, (b) 66, (c) 27; auf der Schnittebene liegen 104 von 113 abi-Zeilen auf iqb-Schnittwerten (52 von 60 Werten bekannt, 8 neu, 4 Klassenentscheidungen offen); Aufwand Weg A (gemeinsame Typenliste, 77 Zeilen per Skript umetikettiert) gegen Weg B (Stark-Hefte ins alte Gerüst); Empfehlung Weg A vor dem ersten Stark-Heft. Entscheidung beim Lehrer. |
| 2026-09-15 | Stark-Heft 2023-bebb-gk gesichtet (Scan lokal unter hefte/, per .gitignore vom Repo ausgeschlossen): Aufgabenbestand mit BE-Summen und Pool-Abgleich in § 4 – 30 von 185 BE im Pool 2023 (Teil A Analysis 1 und AG 1, Aufgabe 4 zu 20 von 30 BE). Kürzel `bebb` für gemeinsame Hefte 2019–2025 in abi.md v0.7 § 4. Keine Zeile erfasst, keine Katalogdatei geändert. |
| 2026-09-12 | Quellenlage geklärt: gemeinsame Aufgabenentwicklung Berlin/Brandenburg seit 2009/10, seit dem Abitur 2026 getrennt (LISUM aufgelöst). Prüfungsschwerpunkte 2027 beider Länder verglichen – Struktur und Arbeitszeit gleich, Inhalte verschieden. Brandenburg hat eine eigene Prüfung auf grundlegendem Niveau. Befunde in § 4, abi.md auf v0.5 (§ 1 Zeitleiste, § 3 Kataloge 2027, § 4 Schreibweise afb_amtlich, § 9). |
| 2026-09-12 | 2018-be-gk vollständig erfasst: 36 Zeilen, Katalog jetzt 113 Zeilen, Typenliste 146. Alle sechs Punktsummen gegen die BE-Tabellen geprüft (40-40-20-20-20-20), zwei Läufe aus frischen Repo-Kopien byteidentisch, Selbstprüfung über den Gesamtbestand bestanden. 34 Typen neu, 16 der 50 verwendeten Typen waren bekannt (32 Prozent). Erstes Heft auf grundlegendem Niveau; sechs Befunde in § 4 ergänzt. |
| 2026-09-12 | 2017-bb-ea vollständig erfasst: 36 Zeilen, Katalog jetzt 77 Zeilen, Typenliste 112. Alle neun Punktsummen und die Teil-1-Summe 15 gegen die BE-Tabellen geprüft, Lauf zweimal byteidentisch, Selbstprüfung über den Gesamtbestand bestanden. 53 Typen neu, nur 12 der 65 verwendeten Typen waren aus 2018 bekannt. Befunde in § 4 ergänzt, darunter der Vergleich mit den Berliner LK-Heften. |
| 2026-09-12 | Feldprobe nachgetragen: die 11 Zeilen der Aufgaben 1.2 und 2.1 und ihre 21 Typen stehen jetzt in ZEILEN und NEUE_TYPEN von abi-bau.py. Vollrebuild aus leeren Katalogdateien reproduziert Katalog und Typenliste byteidentisch. 2018-bb-ea ist damit vollständig aus dem Skript herstellbar. |
| 2026-09-12 | Typenliste bereinigt: „Fehlen von Extrempunkten einer Schar nachweisen“ in „… über die Diskriminante nachweisen“ umbenannt; „Schnittpunkt Gerade Koordinatenebene berechnen“ und „Durchstoßpunkt einer Geraden durch eine Ebene nachweisen“ zu „Durchstoßpunkt einer Geraden durch eine Ebene bestimmen“ zusammengelegt (gleicher Lösungsweg). Katalog unverändert 41 Zeilen, Typenliste jetzt 59, davon 21 nur als typ_neben. |
| 2026-09-12 | 2018-bb-ea vollständig erfasst: 30 Zeilen ergänzt (1.1, 1.3, 2.2, 3.1, 3.2, 4.1, 4.2), Katalog jetzt 41 Zeilen, Typenliste 60. Punktsummen aller sieben Aufgaben gegen die BE-Tabellen geprüft. Drei Befunde in § 4 ergänzt. |
| 2026-09-12 | Datei angelegt. Bestand aus abi-quellen.md übernommen, Feldprobe an 2018-bb-ea (11 Zeilen, Aufgaben 1.2 und 2.1) eingetragen, Befunde § 4 aufgenommen. |
