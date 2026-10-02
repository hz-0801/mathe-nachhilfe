> Lehrerentscheid 02.10.2026: Empfehlungen der Gruppe „Katalog“ übernehmen; zusätzlich aufnehmen (statt „nicht aufnehmen“): Ungleichungen und Ungleichungssysteme, Kathetensatz und Höhensatz, negativer Streckfaktor, Intervallschachtelung, Beweise – mit Marke (Gymnasium/Vorrat) nach ziel.md § 1 („Klasse und Schulform filtern nicht; sie ordnen“). Satz von Vieta offen. Umsetzung in Katalog und Bank steht aus.

# Abgleich: Duden „Wissen – Üben – Testen, Mathematik 9“ (2017), Kapitel 2, gegen katalog/lineare-gleichungssysteme.md (2.1 gegen katalog/lineare-gleichungen.md)

Stand 2026-10-02. Gelesen: PDF-Seiten 13–23 (Buchseiten 13–23) mit 85 dpi, keine Seite mit 110 dpi; Klassenarbeiten S. 24–26 nicht gelesen. Katalog: Lerneinheiten, Typen je Lerneinheit, Sprossen je Verfahrenstyp, Abgrenzungen und „Nicht aufgenommen“; bei lineare-gleichungen.md nur Lerneinheiten und Sprossen. Bank: aufgabenbank/bank/lineare-gleichungssysteme/ e1–e5 (Kette 1 je Sprosse angesehen). Neue Bankzeilen: neu-lineare-gleichungssysteme-duden9.jsonl (22 Zeilen), gebaut und nachgerechnet mit baue_neu_lgs.py, Mischlauf misch_lgs.py.

Buchaufgaben: 2.1 Lineare Gleichungen 4 (Nr. 1–4) · 2.2 grafisch 4 (Nr. 5–8) · 2.3 rechnerisch 6 (Nr. 9–14) · 2.4 drei Variablen 10 (Nr. 15–24) · 2.5 Ungleichungssysteme 4 (Nr. 25–28) – zusammen 28, dazu vier Wissen-Kästen mit Beispielen (S. 14 Ungleichungen, S. 18 und S. 20 Sachaufgaben, S. 22 Halbebenen).

## Kurzfassung

Dem Schüler fehlt auf einem Blatt vor allem das Ordnen: Das Buch gibt Gleichungssysteme fast nie fertig als ax + by = c, sondern mit Klammern, Variablen auf beiden Seiten oder Brüchen, und die Bank übt nur fertig geordnete Systeme. Zweitens denkt er nie rückwärts: eine zweite Gleichung so wählen, dass das System parallel, identisch oder durch einen vorgegebenen Punkt läuft. Drittens behandelt das Buch drei Variablen mit vollem Gaußverfahren und Sachaufgaben schon in Klasse 9, der Katalog führt sie nur als Sek-II-Einheit 5 ohne volles System und ohne Aufstellen aus einem Text. Lineare Ungleichungen (eine Variable und Halbebenen-Systeme) stehen im Buch, im Katalog weder als Sprosse noch unter „Nicht aufgenommen“. Alles andere im Buch deckt der Katalog; die Bank bekommt nur andere Zahlenarten und Formen.

## A „Im Buch, nicht im Katalog“

| Nr. | Gruppe | Typ | Buchstelle | Was der Schüler ohne ihn nicht übt | Vorschlag | Bankzeilen |
|---|---|---|---|---|---|---|
| A1 | Bank | Lösung prüfen mit Dezimalzahlen und Bruchgleichung, mehrere Kandidaten, Taschenrechner | S. 14 Nr. 1 | Er prüft Kandidaten nur an ganzzahligen Gleichungen ohne Bruchstrich. | lineare-gleichungen.md Einheit 1 „Lösung prüfen“; Bankzeilen dort, nicht in diesem Lauf. | 0 |
| A2 | Katalog | Lineare Ungleichung in einer Variablen lösen, Zeichen beim Teilen durch eine negative Zahl umdrehen, Lösungsmenge am Zahlenstrahl | S. 14 Wissen + Nr. 4 | Er weiß nicht, dass sich das Zeichen beim Teilen durch −4 umdreht, und stellt keine Lösungsmenge als Strahl dar. | Kein Sek-I-Ort. Befund: lineare-gleichungssysteme.md (Voraussetzungen, Sek-II-Zeile) verweist auf „lineare-gleichungen.md Einheit 3“, dort steht keine Ungleichung. Empfehlung: Verweis berichtigen (Ort nur gleichungen-loesen.md Einheit 4, Sek II); als Sek-I-Sprosse nicht aufnehmen, solange kein RLP-/P10-Beleg vorliegt. | 0 |
| A3 | Bank | Zahlenrätsel mit aufeinanderfolgenden Zahlen und mit zwei Produkten | S. 14 Nr. 3 | Er übersetzt nur „das Doppelte plus …“, nicht „vier aufeinanderfolgende Zahlen“. | lineare-gleichungen.md Einheit 4 „Zahlenrätsel“; Bankzeilen dort. | 0 |
| A4 | Bank | Gleichung mit Klammern auf beiden Seiten, Dezimalfaktor vor der Klammer, Faktor (−1) vor einer Klammer | S. 14 Nr. 2 | Er löst Klammern nur mit ganzzahligem Faktor auf einer Seite. | lineare-gleichungen.md Einheit 3 „Klammer“; Bankzeilen dort. | 0 |
| A5 | Bank | LGS grafisch, Gleichungen in Form ax + by = c mit Bruch-Vorzahlen | S. 16 Nr. 7 | Er stellt nur ganzzahlige Gleichungen nach y um, bevor er zeichnet. | e1 Kette 1, Sprosse 4 „zwei Geraden zeichnen“, Variante 4. | 1 |
| A6 | Bank | Bild ohne Gleichungen: Schnittpunkt ablesen, beide Gleichungen mit dem Steigungsdreieck bestimmen, Punkt rechnerisch prüfen | S. 16 Nr. 5 | Er liest nur ab, wenn die Gleichungen daneben stehen, und prüft den abgelesenen Punkt nie. | e1 Kette 1, Sprosse 6 „Lösung an einem gegebenen Bild ablesen“, Variante 4. | 1 |
| A7 | Bank | Lösungsanzahl erst nach dem Umstellen entscheiden; eine Gleichung mit Klammer oder Dezimalzahl, auch der Fall „genau eine“ | S. 16 Nr. 6 | Er erkennt parallel und identisch nur, wenn beide Gleichungen schon y = … heißen. | e1 Kette 1, Sprosse 7 „Sonderfälle“, Varianten 4–6. | 3 |
| A8 | Katalog | Zur gegebenen Gleichung die zweite wählen: parallel durch einen Punkt, Schnitt in vorgegebenem Punkt, identisch | S. 16 Nr. 8 | Er denkt nie rückwärts von der gewünschten Lösungsanzahl zur Gleichung; das zeigt, ob er die Sonderfälle verstanden oder nur auswendig gelernt hat. | Neue Sprosse e1 Kette 1 nach Sprosse 7 (NEU-zweite-gerade). Empfehlung: aufnehmen. | 3 |
| A9 | Bank | Einsetzen, wenn die umzustellende Gleichung eine Dezimalzahl trägt | S. 18 Nr. 10c | Er rechnet Dezimalzahlen nur in Geld-Sachaufgaben, nie im nackten System. | e2 Kette 1, Sprosse 6 „Dezimalzahlen (Geld)“, Variante 4. | 1 |
| A10 | Bank | Addition: beide Gleichungen vervielfachen, Dezimalzahl rechts, negative Lösung | S. 18 Nr. 9b | Er vervielfacht beide Gleichungen nur bei ganzen rechten Seiten. | e3 Kette 1, Sprosse 4 „beide vervielfachen“, Variante 4. | 1 |
| A11 | Katalog | Gleichungen erst ordnen: Klammern auflösen, Variablen auf beiden Seiten, Brüche, „= 0“-Form – dann lösen | S. 18 Nr. 9c, 11a–c; S. 20 Nr. 17 | Er bekommt in der Bank jedes System fertig geordnet und scheitert, sobald eine Gleichung 2(x + y) − 3 = y + 5 heißt – im Buch ist das die Regel, nicht die Ausnahme. | Neue Sprosse e3 Kette 1 nach Sprosse 5 „negative Zahlen“ (NEU-ordnen); GYM wie die Kette. Empfehlung: aufnehmen; zu prüfen, ob sie besser in die Einsetzen-Kette (für alle) gehört. | 3 |
| A12 | Katalog | Geradengleichung durch zwei Punkte über ein LGS mit m und n | S. 18 Nr. 12 | Er bestimmt m und n nur über die Steigungsformel, nie als zwei Gleichungen. | Nicht aufnehmen: lineare-funktionen.md Einheit 4 führt „aus zwei Punkten“; der LGS-Weg ist dort ein zweiter Rechenweg. | 0 |
| A13 | Bank | Tiere und Beine: aufstellen, lösen, Antwortsatz | S. 18 Nr. 13 | Die Bank hat Anzahl-und-Bestand nur mit Rädern und Betten und dort nur zum Aufstellen. | e4 Kette 1, Sprosse 7 „aufstellen, lösen, zuordnen, Antwortsatz“, Variante 4. | 1 |
| A14 | Bank | Zahlenrätsel: Summe und Differenz aus Vielfachen | S. 18 Nr. 14 | Er übersetzt nur einfache Differenzen („um 7 größer“). | e4 Kette 1, Sprosse 4 „Zahlenrätsel“, Variante 4. | 1 |
| A15 | Bank | Lösung eines Systems mit drei Variablen aus mehreren Tripeln durch Einsetzen auswählen | S. 20 Nr. 15 | Er setzt nur ein vorgegebenes Tripel ein, muss nie verwerfen. | e5 Kette 1, Sprosse 1 (Grundfall), Variante 6. | 1 |
| A16 | Bank | Gestaffeltes System ohne Parameter, unterste Gleichung schon gelöst | S. 20 Nr. 16 | Die Bank hat gestaffelte Systeme nur mit Parameter. | e5 Kette 1, Sprosse 2, Variante 4. | 1 |
| A17 | Katalog | Volles System 3 × 3 (jede Gleichung mit allen Variablen) in zwei Schritten auf Dreiecksform, Probe in allen drei Gleichungen | S. 19 Wissen; S. 20 Nr. 18 | Er löst nur Systeme, in denen schon Variablen fehlen; das eigentliche Eliminieren in zwei Runden übt er nie. | Neue Sprosse e5 Kette 1 nach Sprosse 3 (NEU-dreiecksform). GYM (Kl. 9 im Buch). Empfehlung: aufnehmen. | 2 |
| A18 | Katalog | Sachaufgaben mit drei Unbekannten aufstellen und lösen (Zahlen aus paarweisen Summen, Quader, Ziffern, Alter, drei Artikel) | S. 20 Wissen; S. 21 Nr. 19–23 | Er liest ein Dreiersystem nur (Mischungsbilanz), stellt aber keins aus einem Text auf. | Neue Sprosse e5 Kette 1 nach NEU-dreiecksform (NEU-sach-drei-variablen). GYM. Empfehlung: aufnehmen. | 3 |
| A19 | Katalog | System mit vier Variablen (Gaußverfahren) | S. 21 Nr. 24 | Er löst nie ein 4 × 4-System. | Nicht aufnehmen: „bis zu vier Variablen“ nur RLP FOS als Werkzeug der Rekonstruktion (rekonstruktion-von-funktionsgleichungen.md). GYM. | 0 |
| A20 | Katalog | Lineare Ungleichung mit zwei Variablen als Halbebene; Ungleichungssysteme zeichnen, aus einem Bild angeben, Punkte prüfen, Dreieck/Viereck beschreiben | S. 22 Wissen; S. 23 Nr. 25–28 | Er stellt Lösungsmengen nie als Fläche dar. | Nicht im Katalog, auch nicht unter „Nicht aufgenommen“ (Suche „Halbebene“, „Ungleichung“ in den Einträgen: kein Sek-I-Treffer). Empfehlung: unter „Nicht aufgenommen“ eintragen (kein RLP-Beleg im Eintrag, keine P10). GYM. | 0 |

Zählung: 20 Zeilen, 12 Bank (davon 3 für lineare-gleichungen.md ohne Bankzeile in diesem Lauf), 8 Katalog.

## B „Reihenfolge weicht ab“

| Nr. | Gruppe | Was | Buch | Katalog | Was der Schüler sonst nicht übt / Folge | Empfehlung |
|---|---|---|---|---|---|---|
| B1 | Katalog | Reihenfolge der Verfahren | Additionsverfahren zuerst, dann Einsetzen, dann Gleichsetzen (S. 17) | Einsetzen (Einheit 2) vor Addition (Einheit 3) | Keine Lücke, nur andere Folge; das Buch setzt Addition als Hauptverfahren, der Katalog das Einsetzen, weil die P10 nur dieses verlangt. | Katalog behalten. |
| B2 | Katalog | Drei Variablen | Klasse 9, direkt nach zwei Variablen (2.4), mit Sachaufgaben | Einheit 5 „Sek II“; zugleich unter „Nicht aufgenommen: drei Variablen (H)“ – Widerspruch zur Verortung („seit dem Sek-II-Teil hier“) | Ein Gymnasiast der Klasse 9 bekommt keine Einheit 5, weil sie nur Sek-II-Marken trägt. | Marke „GYM Kl. 9“ an Einheit 5 für Sprossen 1–3, NEU-dreiecksform und NEU-sach-drei-variablen; „drei Variablen“ aus „Nicht aufgenommen“ streichen. |

## C „Im Katalog, im Buch nicht“

- e1: Zahlenpaar prüfen (Vorstufe); Lösungspaare in eine Tabelle (nur im Wissen-Kasten S. 15, keine Übung); eine einzelne Gerade zeichnen; Probe als eigene Sprosse; systematisches Probieren mit Tabelle; Prüfungshöhe Zimmer und Betten
- e2: Vorstufe „fast fertige Gleichung“; nach x umstellen als eigene Sprosse; Minus vor der Klammer beim Einsetzen; Bruch als Lösung (Vorrat); Prüfungshöhe Preise mit Dezimalzahlen
- e3: Vorstufe gleiche Vorzahl/Gegenzahl; Sonderfälle rechnerisch (0 = 5, 0 = 0); Verfahren begründen (Nr. 11 verlangt nur Wählen)
- e4: Vorstufe „Was ist unbekannt?“; nur aufstellen (ohne Lösen); Variablen einer gegebenen Gleichung benennen; Gleichung als Satz; Probe im Text; Mischungen (Vorrat); Prüfungshöhe Rosen und Tulpen
- alle Einheiten: Fehler finden; Begründen
- Sek-II-Zeilen: Lösungsgerade zeichnen; Eindeutigkeit begründen; Koeffizienten für ein unlösbares System; Mischungsbilanz deuten; Lösungsschar mit Parameter; Fallunterscheidung am Koeffizienten; erweitertes System; Nichtnegativität (das Buch zeigt die drei Lösbarkeitsfälle nur im Wissen-Kasten S. 19)

Zählung: 23 Punkte.

## Leere Sprossen

leere_sprossen.json nennt für diesen Eintrag fünf leere Sprossen (Vorstufen der Ketten Sachaufgaben, Grafisch Sek II, Addition Sek II, Sachaufgaben Sek II, Einheit 5). Alle fünf haben in der Bank je vier Zeilen (Sprosse 0); die Bank kürzt den sprosse_text gegenüber dem Katalog, daher der Fehlalarm des Abgleichskripts. Keine Bankzeile nötig.

## Platzhalter in der jsonl

| Platzhalter | Bedeutung | Ziel-Bankdatei | vorgeschlagene Stelle |
|---|---|---|---|
| NEU-zweite-gerade | A8 | e1.jsonl, Kette 1 | nach Sprosse 7 „Sonderfälle“; alte 8–9 rücken um eins |
| NEU-ordnen | A11 | e3.jsonl, Kette 1 | nach Sprosse 5 „negative Zahlen“; alte 6–9 rücken um eins |
| NEU-dreiecksform | A17 | e5.jsonl, Kette 1 | nach Sprosse 3; alte 4–8 rücken um zwei |
| NEU-sach-drei-variablen | A18 | e5.jsonl, Kette 1 | nach NEU-dreiecksform |

Zusätze an vorhandenen Sprossen übernehmen sprosse_text, merkmal und hoehe der Bank; die Buchform steht im Feld herkunft.

## Mischlauf

Bank-Kopie + 22 Zeilen (e1 50 → 58, e2 44 → 45, e3 57 → 61, e4 65 → 67, e5 36 → 43), Sprossen neu nummeriert, bank-pruef.py: Abweichungen 0, Warnungen 10. Neun Warnungen sind Überzahl an vorhandenen Sprossen (vier statt drei, sechs statt drei an e1 Sprosse 7, sechs statt fünf am e5-Grundfall) – gewollt, der Lehrer streicht beim Einspielen oder hebt die Menge; eine ist Unterzahl (NEU-dreiecksform zwei statt drei Zeilen). Die Formprobe-Hinweise (24) und die Urteilszeile sind dieselben wie in der unveränderten Bank bis auf ein „sonst“ mehr (Ankreuzzeile e5 Sprosse 1). Behoben im Lauf: merkmal und sprosse_text uneinheitlich (Zusätze nahmen eigene Texte), Sperre „3x + 2y“ aus dem Merkkasten (e2 Sprosse 6, Zahlen geändert), zwei pruef-Werte nicht an der Ergebnisstelle.
