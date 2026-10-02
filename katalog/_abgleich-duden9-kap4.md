> Lehrerentscheid 02.10.2026: Empfehlungen der Gruppe „Katalog“ übernehmen; zusätzlich aufnehmen (statt „nicht aufnehmen“): Ungleichungen und Ungleichungssysteme, Kathetensatz und Höhensatz, negativer Streckfaktor, Intervallschachtelung, Beweise – mit Marke (Gymnasium/Vorrat) nach ziel.md § 1 („Klasse und Schulform filtern nicht; sie ordnen“). Satz von Vieta offen. Umsetzung in Katalog und Bank steht aus.

# Abgleich: Duden „Wissen – Üben – Testen, Mathematik 9“ (2017), Kapitel 4, gegen katalog/quadratische-gleichungen.md

Messversuch „Lehrbuch als Quelle für Katalog und Aufgabenbank“, 2026-10-01.
Gelesen: PDF-Seiten 44–61 (18 Seiten, als Bild). Katalogstand: Klon
mathe-nachhilfe (flach, nur letzter Commit); Bank: Klon aufgabenbank,
bank/quadratische-gleichungen (Stand 27.09., Katalog-Commit 99da689).
Kein Wortlaut und keine Zahl aus dem Buch in den Bankzeilen; vom Buch
stammen nur Typ und Stufung.

## Kurzfassung

Das Buch bestätigt die Verfahrensleiter des Katalogs weitgehend; einem
Blatt aus der Bank fehlen nach dem Buch vor allem die Umkehrungen (von
den Lösungen zurück zur Gleichung, reinquadratisch und in Produktform)
und das Erkennen eines vollständigen Quadrats, mit dem x² − 6x + 9 = 0
ohne Formel gelöst wird. Es fehlen außerdem das grafische Lösen mit
Normalparabel und Gerade, das der RLP auf G verlangt, und – nur
Gymnasium – die Aufgabe, eine Zahl der Gleichung so zu wählen, dass sie
zwei, eine oder keine Lösung hat. Normieren übt die Bank nur mit
ganzzahliger Vorzahl, das Buch auch mit 0,5 und ¼, und dass sich nach
dem Ausmultiplizieren das x-Glied aufheben kann, kommt in der Bank nicht
vor. Die Katalogsprosse „Zahl der Lösungen an der allgemeinen Form
entscheiden, ohne zu lösen“ (Fachbrief 10) fehlt in der Bank ganz; das
Buch liefert dafür die Form (p, q ablesen, ankreuzen). Umgekehrt fehlen
dem Buch alle prüfungsnahen Formen des Katalogs (Einsetzen, wahr/falsch,
Fehler finden, Sachaufgaben), und ein gutes Drittel seiner Aufgaben
(19 von 55: Bruch-, Wurzelgleichungen, Ungleichungen) liegt bewusst
außerhalb des Eintrags.

## A „Im Buch, nicht im Katalog“

Einheiten nach dem Katalog (seit 27.09.: 1 Wurzelziehen, 2 p-q-Formel,
3 Nullprodukt, 4 Sachaufgaben). „Bankzeilen“ nennt die Zahl der
Entwürfe in `neu-quadratische-gleichungen-duden9.jsonl`.

| Nr. | Typ | Buchstelle | Was der Schüler ohne ihn nicht üben würde | Vorschlag | Bankzeilen |
|---|---|---|---|---|---|
| A1 | Normalform als vollständiges Quadrat erkennen und direkt lösen (x² − 6x + 9 = 0 → (x − 3)² = 0; auch mit Zahl rechts) | S. 47 Nr. 7; S. 56 Nr. 4; S. 58 Nr. 12 | Er rechnet jede ausmultiplizierte Quadratklammer stur mit der Formel und sieht nie, dass sie Rückwärtsrechnen ist. | Aufnehmen, Einheit 1, neue Sprosse direkt nach „(x − d)² = null: genau eine Lösung“ (Platzhalter NEU-quadrat-erkennen); für alle, Voraussetzung binomische Formeln (Blatt 0). Kein Lösungsverfahren „quadratische Ergänzung“ – nur das Erkennen einer fertigen binomischen Formel. | 3 |
| A2 | Umkehrung reinquadratisch: zu gegebenen Lösungen (±a, nur 0) die Gleichung angeben | S. 56 Nr. 2 | Er geht nur von der Gleichung zur Lösung, nie zurück; das ± bleibt Rechenregel statt Einsicht. | Aufnehmen, Einheit 1, Sprosse nach „Gleichung ohne Lösung selbst angeben“ (deren Erweiterung; NEU-umkehrung-rein); für alle. | 3 |
| A3 | Umkehrung Produktform: aus zwei Lösungen (x − a)·(x − b) = 0 bilden und ausmultiplizieren | S. 48 Nr. 12; S. 61 Nr. 24 | Er erfährt nicht, dass Lösungen und Faktoren dasselbe sind. | Aufnehmen, Einheit 3, Sprosse vor der Prüfungshöhe (NEU-umkehrung-produkt); für alle (nur Produktform und Ausmultiplizieren, beides Blatt 0). | 3 |
| A4 | Normalform nach dem Lösen in Linearfaktoren zerlegen, auch mit Vorzahl (5x² + … = 5(x + …)(x + …)) | S. 48 Nr. 11; S. 56 Nr. 5; S. 61 Nr. 24 | – | Bewusst weglassen: Katalog „Nicht aufgenommen: Linearfaktordarstellung (H)“ [→GOST]; der für alle tragfähige Teil steckt in A3. GYM. | 0 |
| A5 | Satz von Vieta: zweite Lösung aus einer, Lösungen prüfen, ganzzahlige Lösungen über Summe und Produkt finden | S. 49 Nr. 14; S. 57 Nr. 6; S. 61 Nr. 23 | Eine schnelle Probe ohne Einsetzen und das Raten ganzzahliger Lösungen. | Katalog führt Vieta unter „Nicht aufgenommen … höchstens Probe“; LISUM-PH nennt „ggf. Vieta“ in beiden Reihen. Vorschlag: Vorrat-Sprosse Einheit 2 direkt nach „Probe mit einer Lösung“ (NEU-vieta), für alle als Vorrat. Lehrerentscheidung nötig (ändert „Nicht aufgenommen“). | 3 |
| A6 | Zahl p so wählen, dass ganzzahlige Lösungen entstehen | S. 50 Nr. 18 | – | Bewusst weglassen: offenes Problemlösen mit Vieta, GYM; ohne A5 nicht sinnvoll. | 0 |
| A7 | Parameter: für welche Werte einer Zahl in der Gleichung zwei, eine, keine Lösung (Diskriminante als Bedingung) | S. 60 Nr. 19–20; S. 57 Nr. 10 (als Ungleichung) | Er liest den Wert unter der Wurzel nur ab, nutzt ihn nie als Bedingung. | Aufnehmen als GYM-Sprosse in Einheit 2 nach „denselben Wert ‚Diskriminante‘ nennen“ (NEU-parameter); Diskriminante ist im Katalog schon GYM. | 3 |
| A8 | Formvariablen in den Koeffizienten (−2ax² − 4abx = 0) | S. 56 Nr. 3c | – | Bewusst weglassen: Rechnen mit Formvariablen, GYM/GOST. | 0 |
| A9 | Grafisch lösen mit Normalparabel und Gerade (x² = −px − q; Schnittstellen ablesen) | S. 50 Wissen und Nr. 16; S. 57 Nr. 7 | RLP G „grafisch“: der Katalog liest nur die Lösungszahl an waagerechter Gerade und Nullstellen an der verschobenen Parabel ab; das Verfahren mit Normalparabel und schräger Gerade fehlt. | Aufnehmen als Typ ohne Kette in Einheit 2, Vorrat [RLP G] (NEU-grafisch); für alle. Abgrenzung: Schnittpunkte als P10-Typ bleiben in quadratische-funktionen.md. | 3 |
| A10 | Nur in die Normalform umformen, Vorzahl als Bruch oder Dezimalzahl (−¼x², 4,2x², 0,5x²) | S. 47 Nr. 6; S. 58 Nr. 11 | Normieren mit ganzer Vorzahl, aber nicht mit 0,5 – genau die Form der Wurfparabeln. | Kein neuer Typ; zwei Bankzeilen an der Sprosse „Normieren“ (Bank: nur ganzzahlige Vorzahlen). | 2 |
| A11 | Klammer auflösen, x-Glied hebt sich weg, dann Wurzelziehen statt Formel | S. 45 Nr. 4f; S. 50 Nr. 17 | Er glaubt, nach dem Ausmultiplizieren komme immer die Formel. | Kein neuer Typ; zwei Bankzeilen an der Sprosse „Klammer oder Produkt zuerst auflösen“. | 2 |
| A12 | Andere Variablennamen (z², t², u², k) | S. 45 Nr. 3e–f, 4e–f; S. 50 Nr. 17b | Die Unbekannte heißt immer x. | Kein Typ; Hinweis für künftige Varianten der Bank, keine Zeilen. | 0 |
| A13 | Rechte Seite als Wurzelterm, Vorzeichen beurteilen (x² = Zahl − Wurzel) | S. 45 Nr. 1d, 2f | – | Bewusst weglassen: Feinheit der Wurzelterme, GYM. | 0 |
| A14 | „Rechenabkürzung“ über den Betrag: √(x²) = \|x\| | S. 45 Wissen und Nr. 4; S. 56 Nr. 2a, 2e | – | Bewusst weglassen: Katalog schreibt x₁, x₂ (A9 „eine Form“), Betrag ist nicht Stoff des Eintrags. | 0 |
| A15 | Quadratische Ergänzung als Lösungsverfahren | S. 46 Wissen; S. 47 Nr. 7; S. 55 Nr. 29; S. 56 Nr. 4 | – | Bewusst weglassen: Katalog „Nicht aufgenommen“ (RLP-Zeile (12) H; Lösungsverfahren nur Gymnasialreihe Z. 1953). GYM. | 0 |
| A16 | Herleitung der p-q-Formel als Lückentext | S. 49 Nr. 13 | – | Bewusst weglassen: setzt quadratische Ergänzung voraus. GYM. | 0 |
| A17 | Term-, Äquivalenz- oder keine Umformung je Zeile benennen | S. 47 Nr. 8 | – | Weglassen hier: Äquivalenzumformungen gehören zu lineare-gleichungen.md (Abgrenzung im Katalog). | 0 |
| A18 | Zeigen, dass Quadrieren, Teilen durch x, Multiplizieren mit 2x die Lösungsmenge ändern | S. 48 Nr. 9 | – | Teil „durch x teilen“ ist im Katalog (Begründen und Fehler finden, Einheit 3; Bank hat Zeilen) – Dublette. Quadrieren gehört zu Wurzelgleichungen – weglassen. | 0 |
| A19 | Bruchgleichungen: Definitionsmenge, Nenner faktorisieren, Hauptnenner, Überkreuzmultiplikation, Probe | S. 51–52 Nr. 19, 21, 22; S. 57 Nr. 8; S. 59 Nr. 14a, 14c | – | Bewusst weglassen: Katalog „Nicht aufgenommen: Bruchgleichungen“; die auf quadratische Gleichungen führenden Fälle GYM. | 0 |
| A20 | Wurzelgleichungen: Definitionsmenge, isolieren, quadrieren, Probe (auch zwei Wurzeln) | S. 51–53 Nr. 20, 23, 24; S. 57 Nr. 9; S. 59 Nr. 14b | – | Bewusst weglassen: RLP H, „Nicht aufgenommen“ [→GOST]. | 0 |
| A21 | Goldener Schnitt: Verhältnis nachrechnen | S. 53 Wissen und Nr. 25 | – | Bewusst weglassen: Nachweis mit Wurzeltermen, GYM. | 0 |
| A22 | Quadratische Ungleichungen grafisch, rechnerisch, mit Ergänzung, als Sachaufgabe | S. 54–55 Nr. 26–30; S. 57 Nr. 10; S. 59 Nr. 15, 17; S. 61 Nr. 25 | – | Bewusst weglassen. Katalogbefund: Ungleichungen stehen nicht einmal unter „Nicht aufgenommen“ und nicht im RLP-Zitat des Eintrags – eine Zeile „quadratische Ungleichungen (Lehrwerk Kl. 9, nicht RLP-Sek-I-Zitat)“ dort ergänzen; Stufe an der Quelle nicht geprüft. | 0 |
| A23 | Zweite Nullstelle und Gleichung einer verschobenen Normalparabel aus dem Graphen | S. 58 Nr. 13 | – | Weglassen hier: gehört zu quadratische-funktionen.md (Abgrenzung); nutzt Vieta. | 0 |
| A24 | Geometrische Bedeutung der Diskriminante; Nullstellen und Scheitel einer Parabel | S. 60 Nr. 21 | – | Weglassen hier: „Zahl der Nullstellen am Scheitel“ steht in quadratische-funktionen.md Einheit 2 und 4. | 0 |
| A25 | Rechteck mit Weg ringsum (Fläche des Wegs gegeben) | S. 61 Nr. 22 | – | Im Katalog (Prüfungshöhe Sachaufgaben, Quadrat mit Rand); Bank hat „Pool mit Weg“ (e4, Prüfungssprosse) – Dublette. | 0 |

Zum Vorschlag A9 und A10/A11: Die Bank bekommt Zeilen an bestehenden
Sprossen, der Katalog bleibt dort unverändert.

### Platzhalter in der jsonl

| Platzhalter | Bedeutung | Ziel-Bankdatei (heutige Nummerierung der Bank) | vorgeschlagene Stelle |
|---|---|---|---|
| NEU-quadrat-erkennen | A1 | e1.jsonl, Kette 2 | nach Sprosse 10 („(x − d)² = null“) |
| NEU-umkehrung-rein | A2 | e1.jsonl, Kette 2 | nach Sprosse 13 („Gleichung ohne Lösung selbst angeben“), vor der Prüfungshöhe |
| NEU-umkehrung-produkt | A3 | e2.jsonl (Bank: Nullprodukt), Kette 1 | nach Sprosse 9, vor der Prüfungshöhe |
| NEU-parameter | A7 | e3.jsonl (Bank: p-q-Formel), Kette 3 | nach der Sprosse „Diskriminante nennen“ |
| NEU-vieta | A5 | e3.jsonl, Kette 3 | nach „Probe mit einer Lösung“ |
| NEU-grafisch | A9 | e3.jsonl, eigene Kette (Typ ohne Kette, kette_nr 5) | nach Kette 4 „Gerade und Parabel gleichsetzen“; Pflichtkette wird 6 |

Außerdem ohne Platzhalter: drei Zeilen für die Katalogsprosse „Zahl der
Lösungen einer Gleichung in allgemeiner Form … entscheiden und
begründen“ (Bank e3, Kette 3, als Sprosse 8 – die alten Sprossen 8–13
rücken um eins), je zwei Zeilen an „Normieren“ (Sprosse 4, Varianten 4–5)
und an „Klammer oder Produkt zuerst auflösen“ (alte Sprosse 11,
Varianten 4–5).

## B „Reihenfolge weicht ab“

| Nr. | Buch | Katalog | Urteil |
|---|---|---|---|
| B1 | Ausklammern x² + px = 0 kommt vor der p-q-Formel (S. 46, Nr. 5 vor Nr. 10); die Produktform mit zwei Klammern und die Linearfaktoren dagegen erst danach (Nr. 11–12). | Seit 27.09. Nullprodukt (mit Ausklammern) geschlossen als Einheit 3 nach der p-q-Formel. | Für das Ausklammern ist die Buchfolge besser: x² + px = 0 ist wie x² = c eine Vorform mit einem fehlenden Glied, und nach der eigenen Sprossenregel des Katalogs („Vorformen vor dem Universalverfahren“) gehört gerade sie nach vorn – wer erst die Formel mit q = 0 lernt, rechnet die leichteste Form am umständlichsten. Für die Produktform stützt das Buch dagegen den Tausch vom 27.09. Da das Ausklammern GYM ist, betrifft eine Änderung nur Gymnasiasten. Zwei Wege: (a) alles bleibt – einfache Einheitenfolge, der Gymnasiast lernt x² + px = 0 erst nach der Formel; (b) die drei Ausklammern-Sprossen als GYM-Vorform ans Ende von Einheit 1 – die Leiter folgt der eigenen Regel, Einheit 3 verliert drei Sprossen und die Bank muss umziehen. Das Buch ist die fünfte Quelle gegen die heutige Folge (neben LS 9, Fundamente 9, Sekundo 10, LISUM-PH). |
| B2 | (x − d)² = c rückwärts rechnen erscheint nur als Schritt der quadratischen Ergänzung (S. 46), ohne eigene Übung. | Einheit 1, Sprossen „quadrierte Klammer … d positiv“, „d negativ“, „= null“. | Katalog besser: Rückwärtsrechnen ist Wurzelziehen mit einem Schritt mehr, braucht keine Ergänzung und ist die P10-Hauptmarke (2021-OS-K7c). |
| B3 | Normalform herstellen ist ein eigener Schritt vor jedem Verfahren (S. 44 Wissen, Nr. 6 vor Nr. 10). | Normieren ist Sprosse 4 der p-q-Kette, nach „p, q positiv“, „p oder q negativ“, „ordnen“. | Katalog besser: Der Schüler erlebt die Formel zuerst an fertigen Normalformen und hat Erfolg, bevor das Teilen dazukommt; ein Merkmal je Sprosse. |
| B4 | Reinquadratisch: Nr. 2 mischt Quadratzahl, Nicht-Quadratzahl und Freistellen in einer Übung; Nr. 4 bringt Vorzahl und Bruchvorzahl zusammen. | Getrennte Sprossen (Quadratzahl → keine Quadratzahl → negativ → Vorzahl/Zahl dazu → a·x² + b = c). | Katalog besser: Bei Fehlern sieht man, welches Merkmal fehlt. Gleich ist der Einstieg: Lösbarkeit ankreuzen vor dem Rechnen (Nr. 1 = Vorstufe). |
| B5 | Diskriminante als Begriff für alle, gleich mit der p-q-Formel eingeführt (S. 46); Lösungszahl erst nach Vieta geübt (Nr. 15). | Erst „Wert unter der Wurzel null/negativ“ ohne Begriff, dann Entscheiden ohne Lösen, Begriff zuletzt und GYM. | Katalog besser: Der OS-Schüler braucht die Regel, nicht den Namen (Begriff Stufe H, Gymnasialreihe Z. 1965). |
| B6 | Grafisch lösen als Verfahren für Normalformen, nach den rechnerischen Verfahren (S. 50). | Grafisch nur als Lösungszahl am Graphen (Einheit 1, Sprosse 12) und Kontrolle (Einheit 2, Pflicht). | Ort gleich spät, das ist richtig (P10 rechnet); das Buch zeigt aber, dass das grafische Lösen als eigener Typ fehlt – siehe A9. |
| B7 | Sachaufgaben ohne eigene Stufe, nur in den Klassenarbeiten (S. 61 Nr. 22, 25) und als Ungleichung (S. 55 Nr. 30). | Eigene Einheit 4 mit Leiter vom Zahlenrätsel bis zum Rechteck mit Klammer. | Katalog besser: Der Schüler braucht die Stufen Aufstellen → Lösen → Lösung prüfen, die das Buch überspringt. |

## C „Im Katalog, im Buch nicht“

- Erkennungsschritt „Quadratisch oder linear?“ – Einstieg
- Grundvorstellung: Zahlen in x² = neun einsetzen (Blatt 0) – Kern
- Seitenlänge eines Quadrats aus der Fläche (2020-OS-B1d) – P10
- Radius aus Volumen und Höhe (2022-OS-K2d) – P10
- (x − d)² = c rückwärts rechnen als Übung – P10
- Lösung durch Einsetzen prüfen (Einheit 1, 2, 3) – P10
- Zahl der Lösungen am Graphen (Parabel und waagerechte Gerade) – Darstellung
- Gleichung ohne Lösung selbst angeben – P10
- Zwei Aussagen wahr/falsch (2021-OS-K7c) – P10
- Näherungswert einer Wurzel-Lösung runden – P10
- Produkt gleich einer Zahl ungleich null: Satz nicht anwendbar – Fallstrick
- Unter vier Werten den passenden ankreuzen (2025-OS-B1h) – P10
- Vorstufen „Steht rechts eine Null?“, „Welche Lösung passt zur Frage?“ – Einstieg
- Fehler finden (alle Einheiten) – Pflicht
- Begründen (alle Einheiten; nur S. 48 Nr. 9 kommt nahe) – Pflicht
- Zahlenrätsel, Produkt einer Zahl mit ihrem Nachfolger – Vorrat
- Rechteck mit Seitenbeziehung und Fläche – Kern
- Negative Lösung im Kontext ausschließen, Antwortsatz mit Einheit – Kern

## Befunde außerhalb der Tabellen

1. Bank und Katalog sind verschieden nummeriert: Die Bank (Stand 27.09.,
   Katalog-Commit 99da689) führt e2 = Nullprodukt, e3 = p-q-Formel; der
   Katalog hat die Einheiten am 27.09. getauscht (2 = p-q-Formel,
   3 = Nullprodukt), die Mappe (30.09.) ebenso. Die neuen Zeilen tragen
   die Nummern der Bankdateien, in die sie gehören; ein Umzug der Bank
   nimmt sie mit.
2. Die Katalogsprosse „Zahl der Lösungen einer Gleichung in allgemeiner
   Form … entscheiden und begründen“ (Fachbrief 10) fehlt in der Bank
   ganz – sie kam nach dem Bankstand in den Katalog. Drei Zeilen liegen
   jetzt vor.
3. Das Prüfskript meldet im unveränderten Bestand eine Abweichung:
   e3-k3-s13-v9 trägt (x − 3)² − 2 aus dem Original 2025-OS-K5b (Sperre;
   die Mappe ist jünger als die Bank). Nicht von diesem Versuch; im
   Mischlauf erscheint sie als e3-k3-s16-v9.
4. `quelle`: Zeilen an bestehenden Sprossen tragen die Zeilennummer der
   Bank (106/108, Stand-Commit), Zeilen an neuen Sprossen die des
   heutigen Katalogs (103, 104, 105, 25, 125) – der Stand-Commit ist im
   flachen Klon nicht einsehbar.
5. Schreibweise: Das Buch führt durchgehend L = {…}; der Katalog hat
   Mengenklammern bewusst ausgeschlossen (A9, 11h). Kein Typ, keine
   Änderung – nur festgehalten, dass das Lehrwerk anders schreibt.

## Anhang: Aufgabenliste des Kapitels

Schwierigkeit nach dem Läufersymbol des Buchs (drei Graustufen) und dem
Inhalt; bei 110 dpi sind die Stufen nicht immer sicher zu trennen, die
Angabe ist daher eine Einschätzung.

### 4.1 Rein quadratische Gleichungen (S. 44–45), 4 Übungen
| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 45 | 1 | Vorzeichen von q ankreuzen, Zahl der Lösungen ohne Rechnen | leicht | Ankreuzen |
| 45 | 2 | Durch Wurzelziehen lösen, auch Freistellen und Wurzelterm rechts | leicht | Rechnen |
| 45 | 3 | Wenn möglich lösen, Lösungsmenge; Brüche, andere Variablen | mittel | Rechnen |
| 45 | 4 | Mit Betrag-Abkürzung lösen; Vorzahl, Bruchvorzahl, Klammer mit wegfallendem x-Glied | schwer | Rechnen |

### 4.2 Gemischt quadratische Gleichungen (S. 46–50), 14 Übungen
| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 47 | 5 | Durch Ausklammern lösen, auch Vorzahl und erst ordnen | leicht | Rechnen |
| 47 | 6 | In die Normalform umwandeln (ohne Lösen), auch mit Klammern | leicht | Umformen |
| 47 | 7 | Ankreuzen, was direkt mit binomischer Formel geht; Rest mit quadratischer Ergänzung | schwer | Ankreuzen + Rechnen |
| 47 | 8 | Je Zeile Term-, Äquivalenz- oder keine Umformung benennen | schwer | Zuordnen |
| 48 | 9 | Zeigen, dass Quadrieren, Teilen durch x, Mal 2x keine Äquivalenzumformung ist | schwer | Begründen (Lösungsmengen vergleichen) |
| 48 | 10 | p-q-Formel, ggf. erst normieren | mittel | Rechnen |
| 48 | 11 | In Produktschreibweise (Linearfaktoren) bringen, auch Vorzahl | schwer | Umformen |
| 48 | 12 | Aus Produktform die allgemeine Form und die Lösungen ohne Rechnen | mittel | Tabelle, Umkehrung |
| 49 | 13 | Lücken in der Herleitung der p-q-Formel füllen | schwer | Lückentext |
| 49 | 14 | Vieta: zweite Lösung bestimmen; Lösungsmenge prüfen | mittel | Rechnen nach Beispielspalte |
| 50 | 15 | p, q ablesen, Diskriminante ankreuzen, Zahl der Lösungen | mittel | Tabelle, Ankreuzen |
| 50 | 16 | Zeichnerisch lösen (Normalparabel und Gerade) | mittel | Zeichnen |
| 50 | 17 | Lösungsmenge nach Klammerauflösen | schwer | Rechnen |
| 50 | 18 | p so bestimmen, dass ganzzahlige Lösungen entstehen | schwer | Problemlösen, Umkehrung |

### 4.3 Bruch- und Wurzelgleichungen (S. 51–53), 7 Übungen
| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 52 | 19 | Nenner faktorisieren, Definitionsmenge | mittel | Tabelle, Lücke |
| 52 | 20 | Definitionsmenge einer Wurzelgleichung, auch mit Parameter | mittel | Lücke |
| 52 | 21 | Bruchgleichungen lösen (Hauptnenner) | schwer | Rechnen |
| 52 | 22 | Bruchgleichungen durch Überkreuzmultiplikation | mittel | Rechnen |
| 53 | 23 | Wurzelgleichungen: Definitions- und Lösungsmenge | schwer | Rechnen |
| 53 | 24 | Wurzelgleichungen mit zwei Wurzeln | schwer | Rechnen |
| 53 | 25 | Goldener Schnitt: Verhältnis nachrechnen | schwer | Nachweis |

### 4.4 Quadratische Ungleichungen (S. 54–55), 5 Übungen
| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 55 | 26 | Lösungsmenge am Graphen mit ≤/≥ angeben | leicht | Ablesen |
| 55 | 27 | Grafisch lösen | mittel | Zeichnen |
| 55 | 28 | Rechnerisch lösen | mittel | Rechnen |
| 55 | 29 | Mit quadratischer Ergänzung lösen | schwer | Rechnen |
| 55 | 30 | Sachaufgabe Zaun an der Wand, Mindestfläche | schwer | Sachaufgabe |

### Klassenarbeiten 1–3 (S. 56–61), 25 Aufgaben
| S. | Nr. | Typ | Schw. | Form |
|---|---|---|---|---|
| 56 | 1 | Reinquadratisch lösen, auch Produkt (x − a)(x + a) und ohne Lösung | leicht | Rechnen |
| 56 | 2 | Ausgangsgleichung aus Lösungsmenge, Betrag oder Produkt notieren | mittel | Umkehrung |
| 56 | 3 | Ausklammern, auch Bruchvorzahl und Formvariablen | mittel | Rechnen |
| 56 | 4 | Binomisch lösbare ankreuzen, dann Ergänzung und p-q-Formel | schwer | Ankreuzen + Rechnen |
| 56 | 5 | In Produktdarstellung umformen | schwer | Umformen |
| 57 | 6 | Lösungsmenge mit Vieta | mittel | Tabelle |
| 57 | 7 | Zeichnerisch lösen | mittel | Zeichnen |
| 57 | 8 | Bruchgleichung: Nenner faktorisieren, Definitionsmenge, Hauptnenner, lösen | schwer | Lücke + Rechnen |
| 57 | 9 | Wurzelgleichung mit zwei Wurzeln | schwer | Rechnen |
| 57 | 10 | Ungleichung mit Parameter: eine, keine Lösung, Intervalle | schwer | Begründen |
| 58 | 11 | In die Normalform umformen, Dezimal- und Bruchvorzahl | leicht | Umformen |
| 58 | 12 | Geschicktesten Rechenweg ankreuzen, dann lösen | mittel | Ankreuzen + Rechnen |
| 58 | 13 | Verschobene Normalparabel: zweite Nullstelle, Funktionsgleichung | schwer | Ablesen + Rechnen |
| 59 | 14 | Bruch- und Wurzelgleichungen: Definitions- und Lösungsmenge | schwer | Rechnen |
| 59 | 15 | Lösungsmenge einer Ungleichung am Graphen notieren | mittel | Ablesen |
| 59 | 16 | Schnittpunkte Gerade–Parabel aus Gleichung bestimmen | mittel | Rechnen |
| 59 | 17 | Ungleichung lösen, Parabel zeichnen, Lösung markieren | mittel | Rechnen + Zeichnen |
| 60 | 18 | Gemischte Gleichungen, auch Wurzel im Faktor, Minus vor x² | mittel | Rechnen |
| 60 | 19 | Parameter a: Fallunterscheidung über die Diskriminante | schwer | Lückengerüst |
| 60 | 20 | Fälle aus Nr. 19 für drei Werte prüfen | mittel | Rechnen |
| 60 | 21 | p-q-Formel, Nullstellen, Scheitel, zeichnen, Bedeutung der Diskriminante | mittel | Rechnen + Zeichnen + Begründen |
| 61 | 22 | Garten mit Weg ringsum, Wegfläche gegeben | schwer | Sachaufgabe |
| 61 | 23 | p, q notieren, Lösungen mit Vieta | mittel | Tabelle |
| 61 | 24 | Terme mit den Ergebnissen aus Nr. 23 in Linearfaktoren | mittel | Umformen |
| 61 | 25 | Zaun 80 m, Fläche höchstens 300 m²: Bedingungen für die Seiten | schwer | Sachaufgabe, Ungleichung |

Summe: 55 Aufgabennummern (4 + 14 + 7 + 5 + 25).
