# Zentralabitur Mathematik Berlin/Brandenburg – Hefte und Erfassungsstatus
Stand 12.09.2026 · Profil abi · gepflegt vom Katalog-Prompt

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

Leitfassung je Jahr und Niveau: erhöht bb-ea, grundlegend be-gk (abi.md § 7).
Wortgleiche Zwillinge des anderen Landes werden nicht als Zeile erfasst,
sondern hier notiert; eine eigene Zeile nur bei abweichender Teilung, erkennbar
am BE-Vektor.

## 3 Nicht im Bestand

2011–2016 liegen auf dem Server, werden aber nicht aufgenommen (zeitlicher
Schnitt bei 2017, alter Rahmenlehrplan 2006). 2019 ff. sind aus
urheberrechtlichen Gründen nicht veröffentlicht; für Berlin Grundkurs
2019–2022 gibt es sieben Verlagsbände beim Lehrer, noch nicht hochgeladen.

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

## 5 Änderungslog

| Datum | Änderung |
|---|---|
| 2026-09-12 | Quellenlage geklärt: gemeinsame Aufgabenentwicklung Berlin/Brandenburg seit 2009/10, seit dem Abitur 2026 getrennt (LISUM aufgelöst). Prüfungsschwerpunkte 2027 beider Länder verglichen – Struktur und Arbeitszeit gleich, Inhalte verschieden. Brandenburg hat eine eigene Prüfung auf grundlegendem Niveau. Befunde in § 4, abi.md auf v0.5 (§ 1 Zeitleiste, § 3 Kataloge 2027, § 4 Schreibweise afb_amtlich, § 9). |
| 2026-09-12 | 2018-be-gk vollständig erfasst: 36 Zeilen, Katalog jetzt 113 Zeilen, Typenliste 146. Alle sechs Punktsummen gegen die BE-Tabellen geprüft (40-40-20-20-20-20), zwei Läufe aus frischen Repo-Kopien byteidentisch, Selbstprüfung über den Gesamtbestand bestanden. 34 Typen neu, 16 der 50 verwendeten Typen waren bekannt (32 Prozent). Erstes Heft auf grundlegendem Niveau; sechs Befunde in § 4 ergänzt. |
| 2026-09-12 | 2017-bb-ea vollständig erfasst: 36 Zeilen, Katalog jetzt 77 Zeilen, Typenliste 112. Alle neun Punktsummen und die Teil-1-Summe 15 gegen die BE-Tabellen geprüft, Lauf zweimal byteidentisch, Selbstprüfung über den Gesamtbestand bestanden. 53 Typen neu, nur 12 der 65 verwendeten Typen waren aus 2018 bekannt. Befunde in § 4 ergänzt, darunter der Vergleich mit den Berliner LK-Heften. |
| 2026-09-12 | Feldprobe nachgetragen: die 11 Zeilen der Aufgaben 1.2 und 2.1 und ihre 21 Typen stehen jetzt in ZEILEN und NEUE_TYPEN von abi-bau.py. Vollrebuild aus leeren Katalogdateien reproduziert Katalog und Typenliste byteidentisch. 2018-bb-ea ist damit vollständig aus dem Skript herstellbar. |
| 2026-09-12 | Typenliste bereinigt: „Fehlen von Extrempunkten einer Schar nachweisen“ in „… über die Diskriminante nachweisen“ umbenannt; „Schnittpunkt Gerade Koordinatenebene berechnen“ und „Durchstoßpunkt einer Geraden durch eine Ebene nachweisen“ zu „Durchstoßpunkt einer Geraden durch eine Ebene bestimmen“ zusammengelegt (gleicher Lösungsweg). Katalog unverändert 41 Zeilen, Typenliste jetzt 59, davon 21 nur als typ_neben. |
| 2026-09-12 | 2018-bb-ea vollständig erfasst: 30 Zeilen ergänzt (1.1, 1.3, 2.2, 3.1, 3.2, 4.1, 4.2), Katalog jetzt 41 Zeilen, Typenliste 60. Punktsummen aller sieben Aufgaben gegen die BE-Tabellen geprüft. Drei Befunde in § 4 ergänzt. |
| 2026-09-12 | Datei angelegt. Bestand aus abi-quellen.md übernommen, Feldprobe an 2018-bb-ea (11 Zeilen, Aufgaben 1.2 und 2.1) eingetragen, Befunde § 4 aufgenommen. |
